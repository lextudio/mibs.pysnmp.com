# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-GTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-GTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:47 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

(jnxMobileGatewayPgwGgsn,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewayPgwGgsn")

(EnabledStatus,) = mibBuilder.importSymbols(
    "JUNIPER-MIMSTP-MIB",
    "EnabledStatus")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

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

jnxMbgPgwGtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2)
)
jnxMbgPgwGtpMib.setRevisions(
        ("2011-01-28 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgPgwGtpNotifications_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpNotifications = _JnxMbgPgwGtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0)
)
_JnxMbgPgwGtpObjects_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpObjects = _JnxMbgPgwGtpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1)
)
_JnxMbgPgwGtpCGlblCfgGroup_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpCGlblCfgGroup = _JnxMbgPgwGtpCGlblCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1)
)
_JnxMbgPgwGtpGWName_Type = DisplayString
_JnxMbgPgwGtpGWName_Object = MibScalar
jnxMbgPgwGtpGWName = _JnxMbgPgwGtpGWName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 1),
    _JnxMbgPgwGtpGWName_Type()
)
jnxMbgPgwGtpGWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpGWName.setStatus("deprecated")
_JnxMbgPgwGtpPeerHistory_Type = Unsigned32
_JnxMbgPgwGtpPeerHistory_Object = MibScalar
jnxMbgPgwGtpPeerHistory = _JnxMbgPgwGtpPeerHistory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 2),
    _JnxMbgPgwGtpPeerHistory_Type()
)
jnxMbgPgwGtpPeerHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerHistory.setStatus("deprecated")
_JnxMbgPgwGtpN3Reqs_Type = Unsigned32
_JnxMbgPgwGtpN3Reqs_Object = MibScalar
jnxMbgPgwGtpN3Reqs = _JnxMbgPgwGtpN3Reqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 3),
    _JnxMbgPgwGtpN3Reqs_Type()
)
jnxMbgPgwGtpN3Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpN3Reqs.setStatus("deprecated")
_JnxMbgPgwGtpT3Resp_Type = Unsigned32
_JnxMbgPgwGtpT3Resp_Object = MibScalar
jnxMbgPgwGtpT3Resp = _JnxMbgPgwGtpT3Resp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 4),
    _JnxMbgPgwGtpT3Resp_Type()
)
jnxMbgPgwGtpT3Resp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpT3Resp.setStatus("deprecated")
_JnxMbgPgwGtpCtrlEchIntr_Type = Unsigned32
_JnxMbgPgwGtpCtrlEchIntr_Object = MibScalar
jnxMbgPgwGtpCtrlEchIntr = _JnxMbgPgwGtpCtrlEchIntr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 5),
    _JnxMbgPgwGtpCtrlEchIntr_Type()
)
jnxMbgPgwGtpCtrlEchIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCtrlEchIntr.setStatus("deprecated")
_JnxMbgPgwGtpCtrlNoPathMgmt_Type = Unsigned32
_JnxMbgPgwGtpCtrlNoPathMgmt_Object = MibScalar
jnxMbgPgwGtpCtrlNoPathMgmt = _JnxMbgPgwGtpCtrlNoPathMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 6),
    _JnxMbgPgwGtpCtrlNoPathMgmt_Type()
)
jnxMbgPgwGtpCtrlNoPathMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCtrlNoPathMgmt.setStatus("deprecated")
_JnxMbgPgwGtpCtrlIfName_Type = DisplayString
_JnxMbgPgwGtpCtrlIfName_Object = MibScalar
jnxMbgPgwGtpCtrlIfName = _JnxMbgPgwGtpCtrlIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 7),
    _JnxMbgPgwGtpCtrlIfName_Type()
)
jnxMbgPgwGtpCtrlIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCtrlIfName.setStatus("deprecated")
_JnxMbgPgwGtpCtrlIfRtbId_Type = Unsigned32
_JnxMbgPgwGtpCtrlIfRtbId_Object = MibScalar
jnxMbgPgwGtpCtrlIfRtbId = _JnxMbgPgwGtpCtrlIfRtbId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 8),
    _JnxMbgPgwGtpCtrlIfRtbId_Type()
)
jnxMbgPgwGtpCtrlIfRtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCtrlIfRtbId.setStatus("deprecated")


class _JnxMbgPgwGtpCtrlIPv4Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCtrlIPv4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_JnxMbgPgwGtpCtrlIPv4Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCtrlIPv4Addr_Object = MibScalar
jnxMbgPgwGtpCtrlIPv4Addr = _JnxMbgPgwGtpCtrlIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 9),
    _JnxMbgPgwGtpCtrlIPv4Addr_Type()
)
jnxMbgPgwGtpCtrlIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCtrlIPv4Addr.setStatus("deprecated")


class _JnxMbgPgwGtpCtrlIPv6Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCtrlIPv6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxMbgPgwGtpCtrlIPv6Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCtrlIPv6Addr_Object = MibScalar
jnxMbgPgwGtpCtrlIPv6Addr = _JnxMbgPgwGtpCtrlIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 10),
    _JnxMbgPgwGtpCtrlIPv6Addr_Type()
)
jnxMbgPgwGtpCtrlIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCtrlIPv6Addr.setStatus("deprecated")
_JnxMbgPgwGtpDataN3Reqs_Type = Unsigned32
_JnxMbgPgwGtpDataN3Reqs_Object = MibScalar
jnxMbgPgwGtpDataN3Reqs = _JnxMbgPgwGtpDataN3Reqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 11),
    _JnxMbgPgwGtpDataN3Reqs_Type()
)
jnxMbgPgwGtpDataN3Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataN3Reqs.setStatus("deprecated")
_JnxMbgPgwGtpDataT3Resp_Type = Unsigned32
_JnxMbgPgwGtpDataT3Resp_Object = MibScalar
jnxMbgPgwGtpDataT3Resp = _JnxMbgPgwGtpDataT3Resp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 12),
    _JnxMbgPgwGtpDataT3Resp_Type()
)
jnxMbgPgwGtpDataT3Resp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataT3Resp.setStatus("deprecated")
_JnxMbgPgwGtpDataEchIntr_Type = Unsigned32
_JnxMbgPgwGtpDataEchIntr_Object = MibScalar
jnxMbgPgwGtpDataEchIntr = _JnxMbgPgwGtpDataEchIntr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 13),
    _JnxMbgPgwGtpDataEchIntr_Type()
)
jnxMbgPgwGtpDataEchIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataEchIntr.setStatus("deprecated")
_JnxMbgPgwGtpDataNoPathMgmt_Type = Unsigned32
_JnxMbgPgwGtpDataNoPathMgmt_Object = MibScalar
jnxMbgPgwGtpDataNoPathMgmt = _JnxMbgPgwGtpDataNoPathMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 14),
    _JnxMbgPgwGtpDataNoPathMgmt_Type()
)
jnxMbgPgwGtpDataNoPathMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataNoPathMgmt.setStatus("deprecated")
_JnxMbgPgwGtpDataIfName_Type = DisplayString
_JnxMbgPgwGtpDataIfName_Object = MibScalar
jnxMbgPgwGtpDataIfName = _JnxMbgPgwGtpDataIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 15),
    _JnxMbgPgwGtpDataIfName_Type()
)
jnxMbgPgwGtpDataIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataIfName.setStatus("deprecated")
_JnxMbgPgwGtpDataIfRtbId_Type = Unsigned32
_JnxMbgPgwGtpDataIfRtbId_Object = MibScalar
jnxMbgPgwGtpDataIfRtbId = _JnxMbgPgwGtpDataIfRtbId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 16),
    _JnxMbgPgwGtpDataIfRtbId_Type()
)
jnxMbgPgwGtpDataIfRtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataIfRtbId.setStatus("deprecated")


class _JnxMbgPgwGtpDataIPv4Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpDataIPv4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_JnxMbgPgwGtpDataIPv4Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpDataIPv4Addr_Object = MibScalar
jnxMbgPgwGtpDataIPv4Addr = _JnxMbgPgwGtpDataIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 17),
    _JnxMbgPgwGtpDataIPv4Addr_Type()
)
jnxMbgPgwGtpDataIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataIPv4Addr.setStatus("deprecated")


class _JnxMbgPgwGtpDataIPv6Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpDataIPv6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxMbgPgwGtpDataIPv6Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpDataIPv6Addr_Object = MibScalar
jnxMbgPgwGtpDataIPv6Addr = _JnxMbgPgwGtpDataIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 1, 18),
    _JnxMbgPgwGtpDataIPv6Addr_Type()
)
jnxMbgPgwGtpDataIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDataIPv6Addr.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpGlblCfgGroup_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpCGnGpGlblCfgGroup = _JnxMbgPgwGtpCGnGpGlblCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2)
)
_JnxMbgPgwGtpCGnGpGWName_Type = DisplayString
_JnxMbgPgwGtpCGnGpGWName_Object = MibScalar
jnxMbgPgwGtpCGnGpGWName = _JnxMbgPgwGtpCGnGpGWName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 1),
    _JnxMbgPgwGtpCGnGpGWName_Type()
)
jnxMbgPgwGtpCGnGpGWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpGWName.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpPeerHistory_Type = Unsigned32
_JnxMbgPgwGtpCGnGpPeerHistory_Object = MibScalar
jnxMbgPgwGtpCGnGpPeerHistory = _JnxMbgPgwGtpCGnGpPeerHistory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 2),
    _JnxMbgPgwGtpCGnGpPeerHistory_Type()
)
jnxMbgPgwGtpCGnGpPeerHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpPeerHistory.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpN3Reqs_Type = Unsigned32
_JnxMbgPgwGtpCGnGpN3Reqs_Object = MibScalar
jnxMbgPgwGtpCGnGpN3Reqs = _JnxMbgPgwGtpCGnGpN3Reqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 3),
    _JnxMbgPgwGtpCGnGpN3Reqs_Type()
)
jnxMbgPgwGtpCGnGpN3Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpN3Reqs.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpT3Resp_Type = Unsigned32
_JnxMbgPgwGtpCGnGpT3Resp_Object = MibScalar
jnxMbgPgwGtpCGnGpT3Resp = _JnxMbgPgwGtpCGnGpT3Resp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 4),
    _JnxMbgPgwGtpCGnGpT3Resp_Type()
)
jnxMbgPgwGtpCGnGpT3Resp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpT3Resp.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpCtrlEchIntr_Type = Unsigned32
_JnxMbgPgwGtpCGnGpCtrlEchIntr_Object = MibScalar
jnxMbgPgwGtpCGnGpCtrlEchIntr = _JnxMbgPgwGtpCGnGpCtrlEchIntr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 5),
    _JnxMbgPgwGtpCGnGpCtrlEchIntr_Type()
)
jnxMbgPgwGtpCGnGpCtrlEchIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpCtrlEchIntr.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpCtrlNoPathMgmt_Type = Unsigned32
_JnxMbgPgwGtpCGnGpCtrlNoPathMgmt_Object = MibScalar
jnxMbgPgwGtpCGnGpCtrlNoPathMgmt = _JnxMbgPgwGtpCGnGpCtrlNoPathMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 6),
    _JnxMbgPgwGtpCGnGpCtrlNoPathMgmt_Type()
)
jnxMbgPgwGtpCGnGpCtrlNoPathMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpCtrlNoPathMgmt.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpCtrlIfName_Type = DisplayString
_JnxMbgPgwGtpCGnGpCtrlIfName_Object = MibScalar
jnxMbgPgwGtpCGnGpCtrlIfName = _JnxMbgPgwGtpCGnGpCtrlIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 7),
    _JnxMbgPgwGtpCGnGpCtrlIfName_Type()
)
jnxMbgPgwGtpCGnGpCtrlIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpCtrlIfName.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpCtrlIfRtbId_Type = Unsigned32
_JnxMbgPgwGtpCGnGpCtrlIfRtbId_Object = MibScalar
jnxMbgPgwGtpCGnGpCtrlIfRtbId = _JnxMbgPgwGtpCGnGpCtrlIfRtbId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 8),
    _JnxMbgPgwGtpCGnGpCtrlIfRtbId_Type()
)
jnxMbgPgwGtpCGnGpCtrlIfRtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpCtrlIfRtbId.setStatus("deprecated")


class _JnxMbgPgwGtpCGnGpCtrlIPv4Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCGnGpCtrlIPv4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_JnxMbgPgwGtpCGnGpCtrlIPv4Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCGnGpCtrlIPv4Addr_Object = MibScalar
jnxMbgPgwGtpCGnGpCtrlIPv4Addr = _JnxMbgPgwGtpCGnGpCtrlIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 9),
    _JnxMbgPgwGtpCGnGpCtrlIPv4Addr_Type()
)
jnxMbgPgwGtpCGnGpCtrlIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpCtrlIPv4Addr.setStatus("deprecated")


class _JnxMbgPgwGtpCGnGpCtrlIPv6Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCGnGpCtrlIPv6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxMbgPgwGtpCGnGpCtrlIPv6Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCGnGpCtrlIPv6Addr_Object = MibScalar
jnxMbgPgwGtpCGnGpCtrlIPv6Addr = _JnxMbgPgwGtpCGnGpCtrlIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 10),
    _JnxMbgPgwGtpCGnGpCtrlIPv6Addr_Type()
)
jnxMbgPgwGtpCGnGpCtrlIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpCtrlIPv6Addr.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpDataN3Reqs_Type = Unsigned32
_JnxMbgPgwGtpCGnGpDataN3Reqs_Object = MibScalar
jnxMbgPgwGtpCGnGpDataN3Reqs = _JnxMbgPgwGtpCGnGpDataN3Reqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 11),
    _JnxMbgPgwGtpCGnGpDataN3Reqs_Type()
)
jnxMbgPgwGtpCGnGpDataN3Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataN3Reqs.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpDataT3Resp_Type = Unsigned32
_JnxMbgPgwGtpCGnGpDataT3Resp_Object = MibScalar
jnxMbgPgwGtpCGnGpDataT3Resp = _JnxMbgPgwGtpCGnGpDataT3Resp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 12),
    _JnxMbgPgwGtpCGnGpDataT3Resp_Type()
)
jnxMbgPgwGtpCGnGpDataT3Resp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataT3Resp.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpDataEchIntr_Type = Unsigned32
_JnxMbgPgwGtpCGnGpDataEchIntr_Object = MibScalar
jnxMbgPgwGtpCGnGpDataEchIntr = _JnxMbgPgwGtpCGnGpDataEchIntr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 13),
    _JnxMbgPgwGtpCGnGpDataEchIntr_Type()
)
jnxMbgPgwGtpCGnGpDataEchIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataEchIntr.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpDataNoPathMgmt_Type = Unsigned32
_JnxMbgPgwGtpCGnGpDataNoPathMgmt_Object = MibScalar
jnxMbgPgwGtpCGnGpDataNoPathMgmt = _JnxMbgPgwGtpCGnGpDataNoPathMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 14),
    _JnxMbgPgwGtpCGnGpDataNoPathMgmt_Type()
)
jnxMbgPgwGtpCGnGpDataNoPathMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataNoPathMgmt.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpDataIfName_Type = DisplayString
_JnxMbgPgwGtpCGnGpDataIfName_Object = MibScalar
jnxMbgPgwGtpCGnGpDataIfName = _JnxMbgPgwGtpCGnGpDataIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 15),
    _JnxMbgPgwGtpCGnGpDataIfName_Type()
)
jnxMbgPgwGtpCGnGpDataIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataIfName.setStatus("deprecated")
_JnxMbgPgwGtpCGnGpDataIfRtbId_Type = Unsigned32
_JnxMbgPgwGtpCGnGpDataIfRtbId_Object = MibScalar
jnxMbgPgwGtpCGnGpDataIfRtbId = _JnxMbgPgwGtpCGnGpDataIfRtbId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 16),
    _JnxMbgPgwGtpCGnGpDataIfRtbId_Type()
)
jnxMbgPgwGtpCGnGpDataIfRtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataIfRtbId.setStatus("deprecated")


class _JnxMbgPgwGtpCGnGpDataIPv4Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCGnGpDataIPv4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_JnxMbgPgwGtpCGnGpDataIPv4Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCGnGpDataIPv4Addr_Object = MibScalar
jnxMbgPgwGtpCGnGpDataIPv4Addr = _JnxMbgPgwGtpCGnGpDataIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 17),
    _JnxMbgPgwGtpCGnGpDataIPv4Addr_Type()
)
jnxMbgPgwGtpCGnGpDataIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataIPv4Addr.setStatus("deprecated")


class _JnxMbgPgwGtpCGnGpDataIPv6Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCGnGpDataIPv6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxMbgPgwGtpCGnGpDataIPv6Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCGnGpDataIPv6Addr_Object = MibScalar
jnxMbgPgwGtpCGnGpDataIPv6Addr = _JnxMbgPgwGtpCGnGpDataIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 2, 18),
    _JnxMbgPgwGtpCGnGpDataIPv6Addr_Type()
)
jnxMbgPgwGtpCGnGpDataIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGnGpDataIPv6Addr.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8GlblCfgGroup_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpCS5S8GlblCfgGroup = _JnxMbgPgwGtpCS5S8GlblCfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3)
)
_JnxMbgPgwGtpCS5S8GWName_Type = DisplayString
_JnxMbgPgwGtpCS5S8GWName_Object = MibScalar
jnxMbgPgwGtpCS5S8GWName = _JnxMbgPgwGtpCS5S8GWName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 1),
    _JnxMbgPgwGtpCS5S8GWName_Type()
)
jnxMbgPgwGtpCS5S8GWName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8GWName.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8PeerHistory_Type = Unsigned32
_JnxMbgPgwGtpCS5S8PeerHistory_Object = MibScalar
jnxMbgPgwGtpCS5S8PeerHistory = _JnxMbgPgwGtpCS5S8PeerHistory_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 2),
    _JnxMbgPgwGtpCS5S8PeerHistory_Type()
)
jnxMbgPgwGtpCS5S8PeerHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8PeerHistory.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8N3Reqs_Type = Unsigned32
_JnxMbgPgwGtpCS5S8N3Reqs_Object = MibScalar
jnxMbgPgwGtpCS5S8N3Reqs = _JnxMbgPgwGtpCS5S8N3Reqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 3),
    _JnxMbgPgwGtpCS5S8N3Reqs_Type()
)
jnxMbgPgwGtpCS5S8N3Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8N3Reqs.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8T3Resp_Type = Unsigned32
_JnxMbgPgwGtpCS5S8T3Resp_Object = MibScalar
jnxMbgPgwGtpCS5S8T3Resp = _JnxMbgPgwGtpCS5S8T3Resp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 4),
    _JnxMbgPgwGtpCS5S8T3Resp_Type()
)
jnxMbgPgwGtpCS5S8T3Resp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8T3Resp.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8CtrlEchIntr_Type = Unsigned32
_JnxMbgPgwGtpCS5S8CtrlEchIntr_Object = MibScalar
jnxMbgPgwGtpCS5S8CtrlEchIntr = _JnxMbgPgwGtpCS5S8CtrlEchIntr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 5),
    _JnxMbgPgwGtpCS5S8CtrlEchIntr_Type()
)
jnxMbgPgwGtpCS5S8CtrlEchIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8CtrlEchIntr.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8CtrlNoPathMgmt_Type = Unsigned32
_JnxMbgPgwGtpCS5S8CtrlNoPathMgmt_Object = MibScalar
jnxMbgPgwGtpCS5S8CtrlNoPathMgmt = _JnxMbgPgwGtpCS5S8CtrlNoPathMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 6),
    _JnxMbgPgwGtpCS5S8CtrlNoPathMgmt_Type()
)
jnxMbgPgwGtpCS5S8CtrlNoPathMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8CtrlNoPathMgmt.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8CtrlIfName_Type = DisplayString
_JnxMbgPgwGtpCS5S8CtrlIfName_Object = MibScalar
jnxMbgPgwGtpCS5S8CtrlIfName = _JnxMbgPgwGtpCS5S8CtrlIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 7),
    _JnxMbgPgwGtpCS5S8CtrlIfName_Type()
)
jnxMbgPgwGtpCS5S8CtrlIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8CtrlIfName.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8CtrlIfRtbId_Type = Unsigned32
_JnxMbgPgwGtpCS5S8CtrlIfRtbId_Object = MibScalar
jnxMbgPgwGtpCS5S8CtrlIfRtbId = _JnxMbgPgwGtpCS5S8CtrlIfRtbId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 8),
    _JnxMbgPgwGtpCS5S8CtrlIfRtbId_Type()
)
jnxMbgPgwGtpCS5S8CtrlIfRtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8CtrlIfRtbId.setStatus("deprecated")


class _JnxMbgPgwGtpCS5S8CtrlIPv4Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCS5S8CtrlIPv4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_JnxMbgPgwGtpCS5S8CtrlIPv4Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCS5S8CtrlIPv4Addr_Object = MibScalar
jnxMbgPgwGtpCS5S8CtrlIPv4Addr = _JnxMbgPgwGtpCS5S8CtrlIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 9),
    _JnxMbgPgwGtpCS5S8CtrlIPv4Addr_Type()
)
jnxMbgPgwGtpCS5S8CtrlIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8CtrlIPv4Addr.setStatus("deprecated")


class _JnxMbgPgwGtpCS5S8CtrlIPv6Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCS5S8CtrlIPv6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxMbgPgwGtpCS5S8CtrlIPv6Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCS5S8CtrlIPv6Addr_Object = MibScalar
jnxMbgPgwGtpCS5S8CtrlIPv6Addr = _JnxMbgPgwGtpCS5S8CtrlIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 10),
    _JnxMbgPgwGtpCS5S8CtrlIPv6Addr_Type()
)
jnxMbgPgwGtpCS5S8CtrlIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8CtrlIPv6Addr.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8DataN3Reqs_Type = Unsigned32
_JnxMbgPgwGtpCS5S8DataN3Reqs_Object = MibScalar
jnxMbgPgwGtpCS5S8DataN3Reqs = _JnxMbgPgwGtpCS5S8DataN3Reqs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 11),
    _JnxMbgPgwGtpCS5S8DataN3Reqs_Type()
)
jnxMbgPgwGtpCS5S8DataN3Reqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataN3Reqs.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8DataT3Resp_Type = Unsigned32
_JnxMbgPgwGtpCS5S8DataT3Resp_Object = MibScalar
jnxMbgPgwGtpCS5S8DataT3Resp = _JnxMbgPgwGtpCS5S8DataT3Resp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 12),
    _JnxMbgPgwGtpCS5S8DataT3Resp_Type()
)
jnxMbgPgwGtpCS5S8DataT3Resp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataT3Resp.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8DataEchIntr_Type = Unsigned32
_JnxMbgPgwGtpCS5S8DataEchIntr_Object = MibScalar
jnxMbgPgwGtpCS5S8DataEchIntr = _JnxMbgPgwGtpCS5S8DataEchIntr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 13),
    _JnxMbgPgwGtpCS5S8DataEchIntr_Type()
)
jnxMbgPgwGtpCS5S8DataEchIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataEchIntr.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8DataNoPathMgmt_Type = Unsigned32
_JnxMbgPgwGtpCS5S8DataNoPathMgmt_Object = MibScalar
jnxMbgPgwGtpCS5S8DataNoPathMgmt = _JnxMbgPgwGtpCS5S8DataNoPathMgmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 14),
    _JnxMbgPgwGtpCS5S8DataNoPathMgmt_Type()
)
jnxMbgPgwGtpCS5S8DataNoPathMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataNoPathMgmt.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8DataIfName_Type = DisplayString
_JnxMbgPgwGtpCS5S8DataIfName_Object = MibScalar
jnxMbgPgwGtpCS5S8DataIfName = _JnxMbgPgwGtpCS5S8DataIfName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 15),
    _JnxMbgPgwGtpCS5S8DataIfName_Type()
)
jnxMbgPgwGtpCS5S8DataIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataIfName.setStatus("deprecated")
_JnxMbgPgwGtpCS5S8DataIfRtbId_Type = Unsigned32
_JnxMbgPgwGtpCS5S8DataIfRtbId_Object = MibScalar
jnxMbgPgwGtpCS5S8DataIfRtbId = _JnxMbgPgwGtpCS5S8DataIfRtbId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 16),
    _JnxMbgPgwGtpCS5S8DataIfRtbId_Type()
)
jnxMbgPgwGtpCS5S8DataIfRtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataIfRtbId.setStatus("deprecated")


class _JnxMbgPgwGtpCS5S8DataIPv4Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCS5S8DataIPv4Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_JnxMbgPgwGtpCS5S8DataIPv4Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCS5S8DataIPv4Addr_Object = MibScalar
jnxMbgPgwGtpCS5S8DataIPv4Addr = _JnxMbgPgwGtpCS5S8DataIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 17),
    _JnxMbgPgwGtpCS5S8DataIPv4Addr_Type()
)
jnxMbgPgwGtpCS5S8DataIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataIPv4Addr.setStatus("deprecated")


class _JnxMbgPgwGtpCS5S8DataIPv6Addr_Type(InetAddress):
    """Custom type jnxMbgPgwGtpCS5S8DataIPv6Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_JnxMbgPgwGtpCS5S8DataIPv6Addr_Type.__name__ = "InetAddress"
_JnxMbgPgwGtpCS5S8DataIPv6Addr_Object = MibScalar
jnxMbgPgwGtpCS5S8DataIPv6Addr = _JnxMbgPgwGtpCS5S8DataIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 3, 18),
    _JnxMbgPgwGtpCS5S8DataIPv6Addr_Type()
)
jnxMbgPgwGtpCS5S8DataIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCS5S8DataIPv6Addr.setStatus("deprecated")
_JnxMbgPgwGtpV2Stats_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpV2Stats = _JnxMbgPgwGtpV2Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4)
)
_JnxMbgPgwV2NumMsgRx_Type = Counter64
_JnxMbgPgwV2NumMsgRx_Object = MibScalar
jnxMbgPgwV2NumMsgRx = _JnxMbgPgwV2NumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 1),
    _JnxMbgPgwV2NumMsgRx_Type()
)
jnxMbgPgwV2NumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2NumMsgRx.setStatus("deprecated")
_JnxMbgPgwV2NumBytesRx_Type = Counter64
_JnxMbgPgwV2NumBytesRx_Object = MibScalar
jnxMbgPgwV2NumBytesRx = _JnxMbgPgwV2NumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 2),
    _JnxMbgPgwV2NumBytesRx_Type()
)
jnxMbgPgwV2NumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2NumBytesRx.setStatus("deprecated")
_JnxMbgPgwUnSupportedMsg_Type = Counter64
_JnxMbgPgwUnSupportedMsg_Object = MibScalar
jnxMbgPgwUnSupportedMsg = _JnxMbgPgwUnSupportedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 3),
    _JnxMbgPgwUnSupportedMsg_Type()
)
jnxMbgPgwUnSupportedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUnSupportedMsg.setStatus("deprecated")
_JnxMbgPgwProtocolErr_Type = Counter64
_JnxMbgPgwProtocolErr_Object = MibScalar
jnxMbgPgwProtocolErr = _JnxMbgPgwProtocolErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 4),
    _JnxMbgPgwProtocolErr_Type()
)
jnxMbgPgwProtocolErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwProtocolErr.setStatus("deprecated")
_JnxMbgPgwT3RespTmrExp_Type = Counter64
_JnxMbgPgwT3RespTmrExp_Object = MibScalar
jnxMbgPgwT3RespTmrExp = _JnxMbgPgwT3RespTmrExp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 5),
    _JnxMbgPgwT3RespTmrExp_Type()
)
jnxMbgPgwT3RespTmrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwT3RespTmrExp.setStatus("deprecated")
_JnxMbgPgwmsgRedirectRX_Type = Counter64
_JnxMbgPgwmsgRedirectRX_Object = MibScalar
jnxMbgPgwmsgRedirectRX = _JnxMbgPgwmsgRedirectRX_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 6),
    _JnxMbgPgwmsgRedirectRX_Type()
)
jnxMbgPgwmsgRedirectRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwmsgRedirectRX.setStatus("deprecated")
_JnxMbgPgwmsgRedirectTX_Type = Counter64
_JnxMbgPgwmsgRedirectTX_Object = MibScalar
jnxMbgPgwmsgRedirectTX = _JnxMbgPgwmsgRedirectTX_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 7),
    _JnxMbgPgwmsgRedirectTX_Type()
)
jnxMbgPgwmsgRedirectTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwmsgRedirectTX.setStatus("deprecated")
_JnxMbgPgwCreateSessReqRx_Type = Counter64
_JnxMbgPgwCreateSessReqRx_Object = MibScalar
jnxMbgPgwCreateSessReqRx = _JnxMbgPgwCreateSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 8),
    _JnxMbgPgwCreateSessReqRx_Type()
)
jnxMbgPgwCreateSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCreateSessReqRx.setStatus("deprecated")
_JnxMbgPgwCreateSessRspRx_Type = Counter64
_JnxMbgPgwCreateSessRspRx_Object = MibScalar
jnxMbgPgwCreateSessRspRx = _JnxMbgPgwCreateSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 9),
    _JnxMbgPgwCreateSessRspRx_Type()
)
jnxMbgPgwCreateSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCreateSessRspRx.setStatus("deprecated")
_JnxMbgPgwModBrReqRx_Type = Counter64
_JnxMbgPgwModBrReqRx_Object = MibScalar
jnxMbgPgwModBrReqRx = _JnxMbgPgwModBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 10),
    _JnxMbgPgwModBrReqRx_Type()
)
jnxMbgPgwModBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrReqRx.setStatus("deprecated")
_JnxMbgPgwModBrRspRx_Type = Counter64
_JnxMbgPgwModBrRspRx_Object = MibScalar
jnxMbgPgwModBrRspRx = _JnxMbgPgwModBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 11),
    _JnxMbgPgwModBrRspRx_Type()
)
jnxMbgPgwModBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrRspRx.setStatus("deprecated")
_JnxMbgPgwDelSessReqRx_Type = Counter64
_JnxMbgPgwDelSessReqRx_Object = MibScalar
jnxMbgPgwDelSessReqRx = _JnxMbgPgwDelSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 12),
    _JnxMbgPgwDelSessReqRx_Type()
)
jnxMbgPgwDelSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelSessReqRx.setStatus("deprecated")
_JnxMbgPgwDelSessRspRx_Type = Counter64
_JnxMbgPgwDelSessRspRx_Object = MibScalar
jnxMbgPgwDelSessRspRx = _JnxMbgPgwDelSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 13),
    _JnxMbgPgwDelSessRspRx_Type()
)
jnxMbgPgwDelSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelSessRspRx.setStatus("deprecated")
_JnxMbgPgwCngNotifReqRx_Type = Counter64
_JnxMbgPgwCngNotifReqRx_Object = MibScalar
jnxMbgPgwCngNotifReqRx = _JnxMbgPgwCngNotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 14),
    _JnxMbgPgwCngNotifReqRx_Type()
)
jnxMbgPgwCngNotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCngNotifReqRx.setStatus("deprecated")
_JnxMbgPgwCngNotifRspRx_Type = Counter64
_JnxMbgPgwCngNotifRspRx_Object = MibScalar
jnxMbgPgwCngNotifRspRx = _JnxMbgPgwCngNotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 15),
    _JnxMbgPgwCngNotifRspRx_Type()
)
jnxMbgPgwCngNotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCngNotifRspRx.setStatus("deprecated")
_JnxMbgPgwModBrCmdRx_Type = Counter64
_JnxMbgPgwModBrCmdRx_Object = MibScalar
jnxMbgPgwModBrCmdRx = _JnxMbgPgwModBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 16),
    _JnxMbgPgwModBrCmdRx_Type()
)
jnxMbgPgwModBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrCmdRx.setStatus("deprecated")
_JnxMbgPgwModBrFlrIndRx_Type = Counter64
_JnxMbgPgwModBrFlrIndRx_Object = MibScalar
jnxMbgPgwModBrFlrIndRx = _JnxMbgPgwModBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 17),
    _JnxMbgPgwModBrFlrIndRx_Type()
)
jnxMbgPgwModBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrFlrIndRx.setStatus("deprecated")
_JnxMbgPgwDelBrCmdRx_Type = Counter64
_JnxMbgPgwDelBrCmdRx_Object = MibScalar
jnxMbgPgwDelBrCmdRx = _JnxMbgPgwDelBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 18),
    _JnxMbgPgwDelBrCmdRx_Type()
)
jnxMbgPgwDelBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrCmdRx.setStatus("deprecated")
_JnxMbgPgwDelBrFlrIndRx_Type = Counter64
_JnxMbgPgwDelBrFlrIndRx_Object = MibScalar
jnxMbgPgwDelBrFlrIndRx = _JnxMbgPgwDelBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 19),
    _JnxMbgPgwDelBrFlrIndRx_Type()
)
jnxMbgPgwDelBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrFlrIndRx.setStatus("deprecated")
_JnxMbgPgwBrResCmdRx_Type = Counter64
_JnxMbgPgwBrResCmdRx_Object = MibScalar
jnxMbgPgwBrResCmdRx = _JnxMbgPgwBrResCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 20),
    _JnxMbgPgwBrResCmdRx_Type()
)
jnxMbgPgwBrResCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwBrResCmdRx.setStatus("deprecated")
_JnxMbgPgwBrResFlrIndRx_Type = Counter64
_JnxMbgPgwBrResFlrIndRx_Object = MibScalar
jnxMbgPgwBrResFlrIndRx = _JnxMbgPgwBrResFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 21),
    _JnxMbgPgwBrResFlrIndRx_Type()
)
jnxMbgPgwBrResFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwBrResFlrIndRx.setStatus("deprecated")
_JnxMbgPgwDlDataNotiFlrIndRx_Type = Counter64
_JnxMbgPgwDlDataNotiFlrIndRx_Object = MibScalar
jnxMbgPgwDlDataNotiFlrIndRx = _JnxMbgPgwDlDataNotiFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 22),
    _JnxMbgPgwDlDataNotiFlrIndRx_Type()
)
jnxMbgPgwDlDataNotiFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDlDataNotiFlrIndRx.setStatus("deprecated")
_JnxMbgPgwTraceSessActRx_Type = Counter64
_JnxMbgPgwTraceSessActRx_Object = MibScalar
jnxMbgPgwTraceSessActRx = _JnxMbgPgwTraceSessActRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 23),
    _JnxMbgPgwTraceSessActRx_Type()
)
jnxMbgPgwTraceSessActRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwTraceSessActRx.setStatus("deprecated")
_JnxMbgPgwTraceSessDeactRx_Type = Counter64
_JnxMbgPgwTraceSessDeactRx_Object = MibScalar
jnxMbgPgwTraceSessDeactRx = _JnxMbgPgwTraceSessDeactRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 24),
    _JnxMbgPgwTraceSessDeactRx_Type()
)
jnxMbgPgwTraceSessDeactRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwTraceSessDeactRx.setStatus("deprecated")
_JnxMbgPgwCrtBrReqRx_Type = Counter64
_JnxMbgPgwCrtBrReqRx_Object = MibScalar
jnxMbgPgwCrtBrReqRx = _JnxMbgPgwCrtBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 25),
    _JnxMbgPgwCrtBrReqRx_Type()
)
jnxMbgPgwCrtBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtBrReqRx.setStatus("deprecated")
_JnxMbgPgwCrtBrRspRx_Type = Counter64
_JnxMbgPgwCrtBrRspRx_Object = MibScalar
jnxMbgPgwCrtBrRspRx = _JnxMbgPgwCrtBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 26),
    _JnxMbgPgwCrtBrRspRx_Type()
)
jnxMbgPgwCrtBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtBrRspRx.setStatus("deprecated")
_JnxMbgPgwUpdBrReqRx_Type = Counter64
_JnxMbgPgwUpdBrReqRx_Object = MibScalar
jnxMbgPgwUpdBrReqRx = _JnxMbgPgwUpdBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 27),
    _JnxMbgPgwUpdBrReqRx_Type()
)
jnxMbgPgwUpdBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdBrReqRx.setStatus("deprecated")
_JnxMbgPgwUpdBrRspRx_Type = Counter64
_JnxMbgPgwUpdBrRspRx_Object = MibScalar
jnxMbgPgwUpdBrRspRx = _JnxMbgPgwUpdBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 28),
    _JnxMbgPgwUpdBrRspRx_Type()
)
jnxMbgPgwUpdBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdBrRspRx.setStatus("deprecated")
_JnxMbgPgwDelBrReqRx_Type = Counter64
_JnxMbgPgwDelBrReqRx_Object = MibScalar
jnxMbgPgwDelBrReqRx = _JnxMbgPgwDelBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 29),
    _JnxMbgPgwDelBrReqRx_Type()
)
jnxMbgPgwDelBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrReqRx.setStatus("deprecated")
_JnxMbgPgwDelBrRspRx_Type = Counter64
_JnxMbgPgwDelBrRspRx_Object = MibScalar
jnxMbgPgwDelBrRspRx = _JnxMbgPgwDelBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 30),
    _JnxMbgPgwDelBrRspRx_Type()
)
jnxMbgPgwDelBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrRspRx.setStatus("deprecated")
_JnxMbgPgwDelConnSetReqRx_Type = Counter64
_JnxMbgPgwDelConnSetReqRx_Object = MibScalar
jnxMbgPgwDelConnSetReqRx = _JnxMbgPgwDelConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 31),
    _JnxMbgPgwDelConnSetReqRx_Type()
)
jnxMbgPgwDelConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelConnSetReqRx.setStatus("deprecated")
_JnxMbgPgwDelConnSetRspRx_Type = Counter64
_JnxMbgPgwDelConnSetRspRx_Object = MibScalar
jnxMbgPgwDelConnSetRspRx = _JnxMbgPgwDelConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 32),
    _JnxMbgPgwDelConnSetRspRx_Type()
)
jnxMbgPgwDelConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelConnSetRspRx.setStatus("deprecated")
_JnxMbgPgwDlDataNotifRx_Type = Counter64
_JnxMbgPgwDlDataNotifRx_Object = MibScalar
jnxMbgPgwDlDataNotifRx = _JnxMbgPgwDlDataNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 33),
    _JnxMbgPgwDlDataNotifRx_Type()
)
jnxMbgPgwDlDataNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDlDataNotifRx.setStatus("deprecated")
_JnxMbgPgwDlDataAckRx_Type = Counter64
_JnxMbgPgwDlDataAckRx_Object = MibScalar
jnxMbgPgwDlDataAckRx = _JnxMbgPgwDlDataAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 34),
    _JnxMbgPgwDlDataAckRx_Type()
)
jnxMbgPgwDlDataAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDlDataAckRx.setStatus("deprecated")
_JnxMbgPgwUpdConnSetReqRx_Type = Counter64
_JnxMbgPgwUpdConnSetReqRx_Object = MibScalar
jnxMbgPgwUpdConnSetReqRx = _JnxMbgPgwUpdConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 35),
    _JnxMbgPgwUpdConnSetReqRx_Type()
)
jnxMbgPgwUpdConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdConnSetReqRx.setStatus("deprecated")
_JnxMbgPgwUpdConnSetRspRx_Type = Counter64
_JnxMbgPgwUpdConnSetRspRx_Object = MibScalar
jnxMbgPgwUpdConnSetRspRx = _JnxMbgPgwUpdConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 36),
    _JnxMbgPgwUpdConnSetRspRx_Type()
)
jnxMbgPgwUpdConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdConnSetRspRx.setStatus("deprecated")
_JnxMbgPgwV2EchoReqRx_Type = Counter64
_JnxMbgPgwV2EchoReqRx_Object = MibScalar
jnxMbgPgwV2EchoReqRx = _JnxMbgPgwV2EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 37),
    _JnxMbgPgwV2EchoReqRx_Type()
)
jnxMbgPgwV2EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2EchoReqRx.setStatus("deprecated")
_JnxMbgPgwV2EchoRespRx_Type = Counter64
_JnxMbgPgwV2EchoRespRx_Object = MibScalar
jnxMbgPgwV2EchoRespRx = _JnxMbgPgwV2EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 38),
    _JnxMbgPgwV2EchoRespRx_Type()
)
jnxMbgPgwV2EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2EchoRespRx.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsPage_Type = Counter64
_JnxMbgPgwGtpV2ICsPage_Object = MibScalar
jnxMbgPgwGtpV2ICsPage = _JnxMbgPgwGtpV2ICsPage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 39),
    _JnxMbgPgwGtpV2ICsPage_Type()
)
jnxMbgPgwGtpV2ICsPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsPage.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsReqAccept_Type = Counter64
_JnxMbgPgwGtpV2ICsReqAccept_Object = MibScalar
jnxMbgPgwGtpV2ICsReqAccept = _JnxMbgPgwGtpV2ICsReqAccept_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 40),
    _JnxMbgPgwGtpV2ICsReqAccept_Type()
)
jnxMbgPgwGtpV2ICsReqAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsReqAccept.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsAcceptPart_Type = Counter64
_JnxMbgPgwGtpV2ICsAcceptPart_Object = MibScalar
jnxMbgPgwGtpV2ICsAcceptPart = _JnxMbgPgwGtpV2ICsAcceptPart_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 41),
    _JnxMbgPgwGtpV2ICsAcceptPart_Type()
)
jnxMbgPgwGtpV2ICsAcceptPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsAcceptPart.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsNewPTSubLT_Type = Counter64
_JnxMbgPgwGtpV2ICsNewPTSubLT_Object = MibScalar
jnxMbgPgwGtpV2ICsNewPTSubLT = _JnxMbgPgwGtpV2ICsNewPTSubLT_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 42),
    _JnxMbgPgwGtpV2ICsNewPTSubLT_Type()
)
jnxMbgPgwGtpV2ICsNewPTSubLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsNewPTSubLT.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsNewPTNPref_Type = Counter64
_JnxMbgPgwGtpV2ICsNewPTNPref_Object = MibScalar
jnxMbgPgwGtpV2ICsNewPTNPref = _JnxMbgPgwGtpV2ICsNewPTNPref_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 43),
    _JnxMbgPgwGtpV2ICsNewPTNPref_Type()
)
jnxMbgPgwGtpV2ICsNewPTNPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsNewPTNPref.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsNewPTSIAddrbr_Type = Counter64
_JnxMbgPgwGtpV2ICsNewPTSIAddrbr_Object = MibScalar
jnxMbgPgwGtpV2ICsNewPTSIAddrbr = _JnxMbgPgwGtpV2ICsNewPTSIAddrbr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 44),
    _JnxMbgPgwGtpV2ICsNewPTSIAddrbr_Type()
)
jnxMbgPgwGtpV2ICsNewPTSIAddrbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsNewPTSIAddrbr.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsCtxNotFnd_Type = Counter64
_JnxMbgPgwGtpV2ICsCtxNotFnd_Object = MibScalar
jnxMbgPgwGtpV2ICsCtxNotFnd = _JnxMbgPgwGtpV2ICsCtxNotFnd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 45),
    _JnxMbgPgwGtpV2ICsCtxNotFnd_Type()
)
jnxMbgPgwGtpV2ICsCtxNotFnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsCtxNotFnd.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsInvMsgFmt_Type = Counter64
_JnxMbgPgwGtpV2ICsInvMsgFmt_Object = MibScalar
jnxMbgPgwGtpV2ICsInvMsgFmt = _JnxMbgPgwGtpV2ICsInvMsgFmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 46),
    _JnxMbgPgwGtpV2ICsInvMsgFmt_Type()
)
jnxMbgPgwGtpV2ICsInvMsgFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInvMsgFmt.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsVerNotSupp_Type = Counter64
_JnxMbgPgwGtpV2ICsVerNotSupp_Object = MibScalar
jnxMbgPgwGtpV2ICsVerNotSupp = _JnxMbgPgwGtpV2ICsVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 47),
    _JnxMbgPgwGtpV2ICsVerNotSupp_Type()
)
jnxMbgPgwGtpV2ICsVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsVerNotSupp.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsInvLen_Type = Counter64
_JnxMbgPgwGtpV2ICsInvLen_Object = MibScalar
jnxMbgPgwGtpV2ICsInvLen = _JnxMbgPgwGtpV2ICsInvLen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 48),
    _JnxMbgPgwGtpV2ICsInvLen_Type()
)
jnxMbgPgwGtpV2ICsInvLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInvLen.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsServNotSupp_Type = Counter64
_JnxMbgPgwGtpV2ICsServNotSupp_Object = MibScalar
jnxMbgPgwGtpV2ICsServNotSupp = _JnxMbgPgwGtpV2ICsServNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 49),
    _JnxMbgPgwGtpV2ICsServNotSupp_Type()
)
jnxMbgPgwGtpV2ICsServNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsServNotSupp.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsManIEIncorr_Type = Counter64
_JnxMbgPgwGtpV2ICsManIEIncorr_Object = MibScalar
jnxMbgPgwGtpV2ICsManIEIncorr = _JnxMbgPgwGtpV2ICsManIEIncorr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 50),
    _JnxMbgPgwGtpV2ICsManIEIncorr_Type()
)
jnxMbgPgwGtpV2ICsManIEIncorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsManIEIncorr.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsManIEMiss_Type = Counter64
_JnxMbgPgwGtpV2ICsManIEMiss_Object = MibScalar
jnxMbgPgwGtpV2ICsManIEMiss = _JnxMbgPgwGtpV2ICsManIEMiss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 51),
    _JnxMbgPgwGtpV2ICsManIEMiss_Type()
)
jnxMbgPgwGtpV2ICsManIEMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsManIEMiss.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsOptIEIncorr_Type = Counter64
_JnxMbgPgwGtpV2ICsOptIEIncorr_Object = MibScalar
jnxMbgPgwGtpV2ICsOptIEIncorr = _JnxMbgPgwGtpV2ICsOptIEIncorr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 52),
    _JnxMbgPgwGtpV2ICsOptIEIncorr_Type()
)
jnxMbgPgwGtpV2ICsOptIEIncorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsOptIEIncorr.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsSysFail_Type = Counter64
_JnxMbgPgwGtpV2ICsSysFail_Object = MibScalar
jnxMbgPgwGtpV2ICsSysFail = _JnxMbgPgwGtpV2ICsSysFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 53),
    _JnxMbgPgwGtpV2ICsSysFail_Type()
)
jnxMbgPgwGtpV2ICsSysFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsSysFail.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsNoRes_Type = Counter64
_JnxMbgPgwGtpV2ICsNoRes_Object = MibScalar
jnxMbgPgwGtpV2ICsNoRes = _JnxMbgPgwGtpV2ICsNoRes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 54),
    _JnxMbgPgwGtpV2ICsNoRes_Type()
)
jnxMbgPgwGtpV2ICsNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsNoRes.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsTFTSMANTErr_Type = Counter64
_JnxMbgPgwGtpV2ICsTFTSMANTErr_Object = MibScalar
jnxMbgPgwGtpV2ICsTFTSMANTErr = _JnxMbgPgwGtpV2ICsTFTSMANTErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 55),
    _JnxMbgPgwGtpV2ICsTFTSMANTErr_Type()
)
jnxMbgPgwGtpV2ICsTFTSMANTErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsTFTSMANTErr.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsTFTSysErr_Type = Counter64
_JnxMbgPgwGtpV2ICsTFTSysErr_Object = MibScalar
jnxMbgPgwGtpV2ICsTFTSysErr = _JnxMbgPgwGtpV2ICsTFTSysErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 56),
    _JnxMbgPgwGtpV2ICsTFTSysErr_Type()
)
jnxMbgPgwGtpV2ICsTFTSysErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsTFTSysErr.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsPktFltrsMantErr_Type = Counter64
_JnxMbgPgwGtpV2ICsPktFltrsMantErr_Object = MibScalar
jnxMbgPgwGtpV2ICsPktFltrsMantErr = _JnxMbgPgwGtpV2ICsPktFltrsMantErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 57),
    _JnxMbgPgwGtpV2ICsPktFltrsMantErr_Type()
)
jnxMbgPgwGtpV2ICsPktFltrsMantErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsPktFltrsMantErr.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsPktFltrSynErr_Type = Counter64
_JnxMbgPgwGtpV2ICsPktFltrSynErr_Object = MibScalar
jnxMbgPgwGtpV2ICsPktFltrSynErr = _JnxMbgPgwGtpV2ICsPktFltrSynErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 58),
    _JnxMbgPgwGtpV2ICsPktFltrSynErr_Type()
)
jnxMbgPgwGtpV2ICsPktFltrSynErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsPktFltrSynErr.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsMissUnkownAPN_Type = Counter64
_JnxMbgPgwGtpV2ICsMissUnkownAPN_Object = MibScalar
jnxMbgPgwGtpV2ICsMissUnkownAPN = _JnxMbgPgwGtpV2ICsMissUnkownAPN_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 59),
    _JnxMbgPgwGtpV2ICsMissUnkownAPN_Type()
)
jnxMbgPgwGtpV2ICsMissUnkownAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsMissUnkownAPN.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsUnexpRepeatIE_Type = Counter64
_JnxMbgPgwGtpV2ICsUnexpRepeatIE_Object = MibScalar
jnxMbgPgwGtpV2ICsUnexpRepeatIE = _JnxMbgPgwGtpV2ICsUnexpRepeatIE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 60),
    _JnxMbgPgwGtpV2ICsUnexpRepeatIE_Type()
)
jnxMbgPgwGtpV2ICsUnexpRepeatIE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsUnexpRepeatIE.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsGREKeyNotFnd_Type = Counter64
_JnxMbgPgwGtpV2ICsGREKeyNotFnd_Object = MibScalar
jnxMbgPgwGtpV2ICsGREKeyNotFnd = _JnxMbgPgwGtpV2ICsGREKeyNotFnd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 61),
    _JnxMbgPgwGtpV2ICsGREKeyNotFnd_Type()
)
jnxMbgPgwGtpV2ICsGREKeyNotFnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsGREKeyNotFnd.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsRelocFail_Type = Counter64
_JnxMbgPgwGtpV2ICsRelocFail_Object = MibScalar
jnxMbgPgwGtpV2ICsRelocFail = _JnxMbgPgwGtpV2ICsRelocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 62),
    _JnxMbgPgwGtpV2ICsRelocFail_Type()
)
jnxMbgPgwGtpV2ICsRelocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsRelocFail.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsDeniedINRat_Type = Counter64
_JnxMbgPgwGtpV2ICsDeniedINRat_Object = MibScalar
jnxMbgPgwGtpV2ICsDeniedINRat = _JnxMbgPgwGtpV2ICsDeniedINRat_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 63),
    _JnxMbgPgwGtpV2ICsDeniedINRat_Type()
)
jnxMbgPgwGtpV2ICsDeniedINRat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsDeniedINRat.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsPTNotSupp_Type = Counter64
_JnxMbgPgwGtpV2ICsPTNotSupp_Object = MibScalar
jnxMbgPgwGtpV2ICsPTNotSupp = _JnxMbgPgwGtpV2ICsPTNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 64),
    _JnxMbgPgwGtpV2ICsPTNotSupp_Type()
)
jnxMbgPgwGtpV2ICsPTNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsPTNotSupp.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsAllDynAddrOcc_Type = Counter64
_JnxMbgPgwGtpV2ICsAllDynAddrOcc_Object = MibScalar
jnxMbgPgwGtpV2ICsAllDynAddrOcc = _JnxMbgPgwGtpV2ICsAllDynAddrOcc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 65),
    _JnxMbgPgwGtpV2ICsAllDynAddrOcc_Type()
)
jnxMbgPgwGtpV2ICsAllDynAddrOcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsAllDynAddrOcc.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsNOTFTUECTXEXIS_Type = Counter64
_JnxMbgPgwGtpV2ICsNOTFTUECTXEXIS_Object = MibScalar
jnxMbgPgwGtpV2ICsNOTFTUECTXEXIS = _JnxMbgPgwGtpV2ICsNOTFTUECTXEXIS_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 66),
    _JnxMbgPgwGtpV2ICsNOTFTUECTXEXIS_Type()
)
jnxMbgPgwGtpV2ICsNOTFTUECTXEXIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsNOTFTUECTXEXIS.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsProtoNotSupp_Type = Counter64
_JnxMbgPgwGtpV2ICsProtoNotSupp_Object = MibScalar
jnxMbgPgwGtpV2ICsProtoNotSupp = _JnxMbgPgwGtpV2ICsProtoNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 67),
    _JnxMbgPgwGtpV2ICsProtoNotSupp_Type()
)
jnxMbgPgwGtpV2ICsProtoNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsProtoNotSupp.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsUENotResp_Type = Counter64
_JnxMbgPgwGtpV2ICsUENotResp_Object = MibScalar
jnxMbgPgwGtpV2ICsUENotResp = _JnxMbgPgwGtpV2ICsUENotResp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 68),
    _JnxMbgPgwGtpV2ICsUENotResp_Type()
)
jnxMbgPgwGtpV2ICsUENotResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsUENotResp.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsUERefuses_Type = Counter64
_JnxMbgPgwGtpV2ICsUERefuses_Object = MibScalar
jnxMbgPgwGtpV2ICsUERefuses = _JnxMbgPgwGtpV2ICsUERefuses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 69),
    _JnxMbgPgwGtpV2ICsUERefuses_Type()
)
jnxMbgPgwGtpV2ICsUERefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsUERefuses.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsServDenied_Type = Counter64
_JnxMbgPgwGtpV2ICsServDenied_Object = MibScalar
jnxMbgPgwGtpV2ICsServDenied = _JnxMbgPgwGtpV2ICsServDenied_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 70),
    _JnxMbgPgwGtpV2ICsServDenied_Type()
)
jnxMbgPgwGtpV2ICsServDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsServDenied.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsUnablePageUE_Type = Counter64
_JnxMbgPgwGtpV2ICsUnablePageUE_Object = MibScalar
jnxMbgPgwGtpV2ICsUnablePageUE = _JnxMbgPgwGtpV2ICsUnablePageUE_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 71),
    _JnxMbgPgwGtpV2ICsUnablePageUE_Type()
)
jnxMbgPgwGtpV2ICsUnablePageUE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsUnablePageUE.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsNoMem_Type = Counter64
_JnxMbgPgwGtpV2ICsNoMem_Object = MibScalar
jnxMbgPgwGtpV2ICsNoMem = _JnxMbgPgwGtpV2ICsNoMem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 72),
    _JnxMbgPgwGtpV2ICsNoMem_Type()
)
jnxMbgPgwGtpV2ICsNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsNoMem.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsUserAUTHFail_Type = Counter64
_JnxMbgPgwGtpV2ICsUserAUTHFail_Object = MibScalar
jnxMbgPgwGtpV2ICsUserAUTHFail = _JnxMbgPgwGtpV2ICsUserAUTHFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 73),
    _JnxMbgPgwGtpV2ICsUserAUTHFail_Type()
)
jnxMbgPgwGtpV2ICsUserAUTHFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsUserAUTHFail.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsAPNAccessDenied_Type = Counter64
_JnxMbgPgwGtpV2ICsAPNAccessDenied_Object = MibScalar
jnxMbgPgwGtpV2ICsAPNAccessDenied = _JnxMbgPgwGtpV2ICsAPNAccessDenied_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 74),
    _JnxMbgPgwGtpV2ICsAPNAccessDenied_Type()
)
jnxMbgPgwGtpV2ICsAPNAccessDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsAPNAccessDenied.setStatus("deprecated")
_JnxMbgPgwGtpV2ICsReqRej_Type = Counter64
_JnxMbgPgwGtpV2ICsReqRej_Object = MibScalar
jnxMbgPgwGtpV2ICsReqRej = _JnxMbgPgwGtpV2ICsReqRej_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 75),
    _JnxMbgPgwGtpV2ICsReqRej_Type()
)
jnxMbgPgwGtpV2ICsReqRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsReqRej.setStatus("deprecated")
_JnxMbgPgwV2NumMsgTx_Type = Counter64
_JnxMbgPgwV2NumMsgTx_Object = MibScalar
jnxMbgPgwV2NumMsgTx = _JnxMbgPgwV2NumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 76),
    _JnxMbgPgwV2NumMsgTx_Type()
)
jnxMbgPgwV2NumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2NumMsgTx.setStatus("deprecated")
_JnxMbgPgwV2NumBytesTx_Type = Counter64
_JnxMbgPgwV2NumBytesTx_Object = MibScalar
jnxMbgPgwV2NumBytesTx = _JnxMbgPgwV2NumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 77),
    _JnxMbgPgwV2NumBytesTx_Type()
)
jnxMbgPgwV2NumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2NumBytesTx.setStatus("deprecated")
_JnxMbgPgwCreateSessReqTx_Type = Counter64
_JnxMbgPgwCreateSessReqTx_Object = MibScalar
jnxMbgPgwCreateSessReqTx = _JnxMbgPgwCreateSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 78),
    _JnxMbgPgwCreateSessReqTx_Type()
)
jnxMbgPgwCreateSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCreateSessReqTx.setStatus("deprecated")
_JnxMbgPgwCreateSessRspTx_Type = Counter64
_JnxMbgPgwCreateSessRspTx_Object = MibScalar
jnxMbgPgwCreateSessRspTx = _JnxMbgPgwCreateSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 79),
    _JnxMbgPgwCreateSessRspTx_Type()
)
jnxMbgPgwCreateSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCreateSessRspTx.setStatus("deprecated")
_JnxMbgPgwModBrReqTx_Type = Counter64
_JnxMbgPgwModBrReqTx_Object = MibScalar
jnxMbgPgwModBrReqTx = _JnxMbgPgwModBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 80),
    _JnxMbgPgwModBrReqTx_Type()
)
jnxMbgPgwModBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrReqTx.setStatus("deprecated")
_JnxMbgPgwModBrRspTx_Type = Counter64
_JnxMbgPgwModBrRspTx_Object = MibScalar
jnxMbgPgwModBrRspTx = _JnxMbgPgwModBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 81),
    _JnxMbgPgwModBrRspTx_Type()
)
jnxMbgPgwModBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrRspTx.setStatus("deprecated")
_JnxMbgPgwDelSessReqTx_Type = Counter64
_JnxMbgPgwDelSessReqTx_Object = MibScalar
jnxMbgPgwDelSessReqTx = _JnxMbgPgwDelSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 82),
    _JnxMbgPgwDelSessReqTx_Type()
)
jnxMbgPgwDelSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelSessReqTx.setStatus("deprecated")
_JnxMbgPgwDelSessRspTx_Type = Counter64
_JnxMbgPgwDelSessRspTx_Object = MibScalar
jnxMbgPgwDelSessRspTx = _JnxMbgPgwDelSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 83),
    _JnxMbgPgwDelSessRspTx_Type()
)
jnxMbgPgwDelSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelSessRspTx.setStatus("deprecated")
_JnxMbgPgwCngNotifReqTx_Type = Counter64
_JnxMbgPgwCngNotifReqTx_Object = MibScalar
jnxMbgPgwCngNotifReqTx = _JnxMbgPgwCngNotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 84),
    _JnxMbgPgwCngNotifReqTx_Type()
)
jnxMbgPgwCngNotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCngNotifReqTx.setStatus("deprecated")
_JnxMbgPgwCngNotifRspTx_Type = Counter64
_JnxMbgPgwCngNotifRspTx_Object = MibScalar
jnxMbgPgwCngNotifRspTx = _JnxMbgPgwCngNotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 85),
    _JnxMbgPgwCngNotifRspTx_Type()
)
jnxMbgPgwCngNotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCngNotifRspTx.setStatus("deprecated")
_JnxMbgPgwModBrCmdTx_Type = Counter64
_JnxMbgPgwModBrCmdTx_Object = MibScalar
jnxMbgPgwModBrCmdTx = _JnxMbgPgwModBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 86),
    _JnxMbgPgwModBrCmdTx_Type()
)
jnxMbgPgwModBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrCmdTx.setStatus("deprecated")
_JnxMbgPgwModBrFlrIndTx_Type = Counter64
_JnxMbgPgwModBrFlrIndTx_Object = MibScalar
jnxMbgPgwModBrFlrIndTx = _JnxMbgPgwModBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 87),
    _JnxMbgPgwModBrFlrIndTx_Type()
)
jnxMbgPgwModBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwModBrFlrIndTx.setStatus("deprecated")
_JnxMbgPgwDelBrCmdTx_Type = Counter64
_JnxMbgPgwDelBrCmdTx_Object = MibScalar
jnxMbgPgwDelBrCmdTx = _JnxMbgPgwDelBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 88),
    _JnxMbgPgwDelBrCmdTx_Type()
)
jnxMbgPgwDelBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrCmdTx.setStatus("deprecated")
_JnxMbgPgwDelBrFlrIndTx_Type = Counter64
_JnxMbgPgwDelBrFlrIndTx_Object = MibScalar
jnxMbgPgwDelBrFlrIndTx = _JnxMbgPgwDelBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 89),
    _JnxMbgPgwDelBrFlrIndTx_Type()
)
jnxMbgPgwDelBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrFlrIndTx.setStatus("deprecated")
_JnxMbgPgwBrResCmdTx_Type = Counter64
_JnxMbgPgwBrResCmdTx_Object = MibScalar
jnxMbgPgwBrResCmdTx = _JnxMbgPgwBrResCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 90),
    _JnxMbgPgwBrResCmdTx_Type()
)
jnxMbgPgwBrResCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwBrResCmdTx.setStatus("deprecated")
_JnxMbgPgwBrResFlrIndTx_Type = Counter64
_JnxMbgPgwBrResFlrIndTx_Object = MibScalar
jnxMbgPgwBrResFlrIndTx = _JnxMbgPgwBrResFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 91),
    _JnxMbgPgwBrResFlrIndTx_Type()
)
jnxMbgPgwBrResFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwBrResFlrIndTx.setStatus("deprecated")
_JnxMbgPgwDlDataNotiFlrIndTx_Type = Counter64
_JnxMbgPgwDlDataNotiFlrIndTx_Object = MibScalar
jnxMbgPgwDlDataNotiFlrIndTx = _JnxMbgPgwDlDataNotiFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 92),
    _JnxMbgPgwDlDataNotiFlrIndTx_Type()
)
jnxMbgPgwDlDataNotiFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDlDataNotiFlrIndTx.setStatus("deprecated")
_JnxMbgPgwTraceSessActTx_Type = Counter64
_JnxMbgPgwTraceSessActTx_Object = MibScalar
jnxMbgPgwTraceSessActTx = _JnxMbgPgwTraceSessActTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 93),
    _JnxMbgPgwTraceSessActTx_Type()
)
jnxMbgPgwTraceSessActTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwTraceSessActTx.setStatus("deprecated")
_JnxMbgPgwTraceSessDeactTx_Type = Counter64
_JnxMbgPgwTraceSessDeactTx_Object = MibScalar
jnxMbgPgwTraceSessDeactTx = _JnxMbgPgwTraceSessDeactTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 94),
    _JnxMbgPgwTraceSessDeactTx_Type()
)
jnxMbgPgwTraceSessDeactTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwTraceSessDeactTx.setStatus("deprecated")
_JnxMbgPgwCrtBrReqTx_Type = Counter64
_JnxMbgPgwCrtBrReqTx_Object = MibScalar
jnxMbgPgwCrtBrReqTx = _JnxMbgPgwCrtBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 95),
    _JnxMbgPgwCrtBrReqTx_Type()
)
jnxMbgPgwCrtBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtBrReqTx.setStatus("deprecated")
_JnxMbgPgwCrtBrRspTx_Type = Counter64
_JnxMbgPgwCrtBrRspTx_Object = MibScalar
jnxMbgPgwCrtBrRspTx = _JnxMbgPgwCrtBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 96),
    _JnxMbgPgwCrtBrRspTx_Type()
)
jnxMbgPgwCrtBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtBrRspTx.setStatus("deprecated")
_JnxMbgPgwUpdBrReqTx_Type = Counter64
_JnxMbgPgwUpdBrReqTx_Object = MibScalar
jnxMbgPgwUpdBrReqTx = _JnxMbgPgwUpdBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 97),
    _JnxMbgPgwUpdBrReqTx_Type()
)
jnxMbgPgwUpdBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdBrReqTx.setStatus("deprecated")
_JnxMbgPgwUpdBrRspTx_Type = Counter64
_JnxMbgPgwUpdBrRspTx_Object = MibScalar
jnxMbgPgwUpdBrRspTx = _JnxMbgPgwUpdBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 98),
    _JnxMbgPgwUpdBrRspTx_Type()
)
jnxMbgPgwUpdBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdBrRspTx.setStatus("deprecated")
_JnxMbgPgwDelBrReqTx_Type = Counter64
_JnxMbgPgwDelBrReqTx_Object = MibScalar
jnxMbgPgwDelBrReqTx = _JnxMbgPgwDelBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 99),
    _JnxMbgPgwDelBrReqTx_Type()
)
jnxMbgPgwDelBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrReqTx.setStatus("deprecated")
_JnxMbgPgwDelBrRspTx_Type = Counter64
_JnxMbgPgwDelBrRspTx_Object = MibScalar
jnxMbgPgwDelBrRspTx = _JnxMbgPgwDelBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 100),
    _JnxMbgPgwDelBrRspTx_Type()
)
jnxMbgPgwDelBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelBrRspTx.setStatus("deprecated")
_JnxMbgPgwDelConnSetReqTx_Type = Counter64
_JnxMbgPgwDelConnSetReqTx_Object = MibScalar
jnxMbgPgwDelConnSetReqTx = _JnxMbgPgwDelConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 101),
    _JnxMbgPgwDelConnSetReqTx_Type()
)
jnxMbgPgwDelConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelConnSetReqTx.setStatus("deprecated")
_JnxMbgPgwDelConnSetRspTx_Type = Counter64
_JnxMbgPgwDelConnSetRspTx_Object = MibScalar
jnxMbgPgwDelConnSetRspTx = _JnxMbgPgwDelConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 102),
    _JnxMbgPgwDelConnSetRspTx_Type()
)
jnxMbgPgwDelConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelConnSetRspTx.setStatus("deprecated")
_JnxMbgPgwDlDataNotifTx_Type = Counter64
_JnxMbgPgwDlDataNotifTx_Object = MibScalar
jnxMbgPgwDlDataNotifTx = _JnxMbgPgwDlDataNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 103),
    _JnxMbgPgwDlDataNotifTx_Type()
)
jnxMbgPgwDlDataNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDlDataNotifTx.setStatus("deprecated")
_JnxMbgPgwDlDataAckTx_Type = Counter64
_JnxMbgPgwDlDataAckTx_Object = MibScalar
jnxMbgPgwDlDataAckTx = _JnxMbgPgwDlDataAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 104),
    _JnxMbgPgwDlDataAckTx_Type()
)
jnxMbgPgwDlDataAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDlDataAckTx.setStatus("deprecated")
_JnxMbgPgwUpdConnSetReqTx_Type = Counter64
_JnxMbgPgwUpdConnSetReqTx_Object = MibScalar
jnxMbgPgwUpdConnSetReqTx = _JnxMbgPgwUpdConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 105),
    _JnxMbgPgwUpdConnSetReqTx_Type()
)
jnxMbgPgwUpdConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdConnSetReqTx.setStatus("deprecated")
_JnxMbgPgwUpdConnSetRspTx_Type = Counter64
_JnxMbgPgwUpdConnSetRspTx_Object = MibScalar
jnxMbgPgwUpdConnSetRspTx = _JnxMbgPgwUpdConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 106),
    _JnxMbgPgwUpdConnSetRspTx_Type()
)
jnxMbgPgwUpdConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdConnSetRspTx.setStatus("deprecated")
_JnxMbgPgwV2EchoReqTx_Type = Counter64
_JnxMbgPgwV2EchoReqTx_Object = MibScalar
jnxMbgPgwV2EchoReqTx = _JnxMbgPgwV2EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 107),
    _JnxMbgPgwV2EchoReqTx_Type()
)
jnxMbgPgwV2EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2EchoReqTx.setStatus("deprecated")
_JnxMbgPgwV2EchoRespTx_Type = Counter64
_JnxMbgPgwV2EchoRespTx_Object = MibScalar
jnxMbgPgwV2EchoRespTx = _JnxMbgPgwV2EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 4, 108),
    _JnxMbgPgwV2EchoRespTx_Type()
)
jnxMbgPgwV2EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2EchoRespTx.setStatus("deprecated")
_JnxMbgPgwGtpV1Stats_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpV1Stats = _JnxMbgPgwGtpV1Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5)
)
_JnxMbgPgwV1NumMsgRx_Type = Counter64
_JnxMbgPgwV1NumMsgRx_Object = MibScalar
jnxMbgPgwV1NumMsgRx = _JnxMbgPgwV1NumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 1),
    _JnxMbgPgwV1NumMsgRx_Type()
)
jnxMbgPgwV1NumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NumMsgRx.setStatus("deprecated")
_JnxMbgPgwV1NumBytesRx_Type = Counter64
_JnxMbgPgwV1NumBytesRx_Object = MibScalar
jnxMbgPgwV1NumBytesRx = _JnxMbgPgwV1NumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 2),
    _JnxMbgPgwV1NumBytesRx_Type()
)
jnxMbgPgwV1NumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NumBytesRx.setStatus("deprecated")
_JnxMbgPgwV1UnSupportedMsg_Type = Counter64
_JnxMbgPgwV1UnSupportedMsg_Object = MibScalar
jnxMbgPgwV1UnSupportedMsg = _JnxMbgPgwV1UnSupportedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 3),
    _JnxMbgPgwV1UnSupportedMsg_Type()
)
jnxMbgPgwV1UnSupportedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1UnSupportedMsg.setStatus("deprecated")
_JnxMbgPgwProtErr_Type = Counter64
_JnxMbgPgwProtErr_Object = MibScalar
jnxMbgPgwProtErr = _JnxMbgPgwProtErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 4),
    _JnxMbgPgwProtErr_Type()
)
jnxMbgPgwProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwProtErr.setStatus("deprecated")
_JnxMbgPgwV1T3RespTmrExp_Type = Counter64
_JnxMbgPgwV1T3RespTmrExp_Object = MibScalar
jnxMbgPgwV1T3RespTmrExp = _JnxMbgPgwV1T3RespTmrExp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 5),
    _JnxMbgPgwV1T3RespTmrExp_Type()
)
jnxMbgPgwV1T3RespTmrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1T3RespTmrExp.setStatus("deprecated")
_JnxMbgPgwMsgRedirectRx_Type = Counter64
_JnxMbgPgwMsgRedirectRx_Object = MibScalar
jnxMbgPgwMsgRedirectRx = _JnxMbgPgwMsgRedirectRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 6),
    _JnxMbgPgwMsgRedirectRx_Type()
)
jnxMbgPgwMsgRedirectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMsgRedirectRx.setStatus("deprecated")
_JnxMbgPgwMsgRedirectTx_Type = Counter64
_JnxMbgPgwMsgRedirectTx_Object = MibScalar
jnxMbgPgwMsgRedirectTx = _JnxMbgPgwMsgRedirectTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 7),
    _JnxMbgPgwMsgRedirectTx_Type()
)
jnxMbgPgwMsgRedirectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwMsgRedirectTx.setStatus("deprecated")
_JnxMbgPgwSuppExtHdrNot_Type = Counter64
_JnxMbgPgwSuppExtHdrNot_Object = MibScalar
jnxMbgPgwSuppExtHdrNot = _JnxMbgPgwSuppExtHdrNot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 8),
    _JnxMbgPgwSuppExtHdrNot_Type()
)
jnxMbgPgwSuppExtHdrNot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwSuppExtHdrNot.setStatus("deprecated")
_JnxMbgPgwV1EchoReqRx_Type = Counter64
_JnxMbgPgwV1EchoReqRx_Object = MibScalar
jnxMbgPgwV1EchoReqRx = _JnxMbgPgwV1EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 9),
    _JnxMbgPgwV1EchoReqRx_Type()
)
jnxMbgPgwV1EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1EchoReqRx.setStatus("deprecated")
_JnxMbgPgwV1EchoRespRx_Type = Counter64
_JnxMbgPgwV1EchoRespRx_Object = MibScalar
jnxMbgPgwV1EchoRespRx = _JnxMbgPgwV1EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 10),
    _JnxMbgPgwV1EchoRespRx_Type()
)
jnxMbgPgwV1EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1EchoRespRx.setStatus("deprecated")
_JnxMbgPgwCrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwCrtPdpCxtReqRx_Object = MibScalar
jnxMbgPgwCrtPdpCxtReqRx = _JnxMbgPgwCrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 11),
    _JnxMbgPgwCrtPdpCxtReqRx_Type()
)
jnxMbgPgwCrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwCrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwCrtPdpCxtRspRx_Object = MibScalar
jnxMbgPgwCrtPdpCxtRspRx = _JnxMbgPgwCrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 12),
    _JnxMbgPgwCrtPdpCxtRspRx_Type()
)
jnxMbgPgwCrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwUpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwUpdPdpCxtReqRx_Object = MibScalar
jnxMbgPgwUpdPdpCxtReqRx = _JnxMbgPgwUpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 13),
    _JnxMbgPgwUpdPdpCxtReqRx_Type()
)
jnxMbgPgwUpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwUpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwUpdPdpCxtRspRx_Object = MibScalar
jnxMbgPgwUpdPdpCxtRspRx = _JnxMbgPgwUpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 14),
    _JnxMbgPgwUpdPdpCxtRspRx_Type()
)
jnxMbgPgwUpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwDelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwDelPdpCxtReqRx_Object = MibScalar
jnxMbgPgwDelPdpCxtReqRx = _JnxMbgPgwDelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 15),
    _JnxMbgPgwDelPdpCxtReqRx_Type()
)
jnxMbgPgwDelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwDelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwDelPdpCxtRspRx_Object = MibScalar
jnxMbgPgwDelPdpCxtRspRx = _JnxMbgPgwDelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 16),
    _JnxMbgPgwDelPdpCxtRspRx_Type()
)
jnxMbgPgwDelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwCrtAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwCrtAAPdpCxtReqRx_Object = MibScalar
jnxMbgPgwCrtAAPdpCxtReqRx = _JnxMbgPgwCrtAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 17),
    _JnxMbgPgwCrtAAPdpCxtReqRx_Type()
)
jnxMbgPgwCrtAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtAAPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwCrtAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwCrtAAPdpCxtRspRx_Object = MibScalar
jnxMbgPgwCrtAAPdpCxtRspRx = _JnxMbgPgwCrtAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 18),
    _JnxMbgPgwCrtAAPdpCxtRspRx_Type()
)
jnxMbgPgwCrtAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtAAPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwDelAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwDelAAPdpCxtReqRx_Object = MibScalar
jnxMbgPgwDelAAPdpCxtReqRx = _JnxMbgPgwDelAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 19),
    _JnxMbgPgwDelAAPdpCxtReqRx_Type()
)
jnxMbgPgwDelAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelAAPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwDelAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwDelAAPdpCxtRspRx_Object = MibScalar
jnxMbgPgwDelAAPdpCxtRspRx = _JnxMbgPgwDelAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 20),
    _JnxMbgPgwDelAAPdpCxtRspRx_Type()
)
jnxMbgPgwDelAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelAAPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwErrorIndRx_Type = Counter64
_JnxMbgPgwErrorIndRx_Object = MibScalar
jnxMbgPgwErrorIndRx = _JnxMbgPgwErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 21),
    _JnxMbgPgwErrorIndRx_Type()
)
jnxMbgPgwErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwErrorIndRx.setStatus("deprecated")
_JnxMbgPgwNotifReqRx_Type = Counter64
_JnxMbgPgwNotifReqRx_Object = MibScalar
jnxMbgPgwNotifReqRx = _JnxMbgPgwNotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 22),
    _JnxMbgPgwNotifReqRx_Type()
)
jnxMbgPgwNotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifReqRx.setStatus("deprecated")
_JnxMbgPgwNotifRspRx_Type = Counter64
_JnxMbgPgwNotifRspRx_Object = MibScalar
jnxMbgPgwNotifRspRx = _JnxMbgPgwNotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 23),
    _JnxMbgPgwNotifRspRx_Type()
)
jnxMbgPgwNotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifRspRx.setStatus("deprecated")
_JnxMbgPgwNotifRejReqRx_Type = Counter64
_JnxMbgPgwNotifRejReqRx_Object = MibScalar
jnxMbgPgwNotifRejReqRx = _JnxMbgPgwNotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 24),
    _JnxMbgPgwNotifRejReqRx_Type()
)
jnxMbgPgwNotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifRejReqRx.setStatus("deprecated")
_JnxMbgPgwNotifRejRspRx_Type = Counter64
_JnxMbgPgwNotifRejRspRx_Object = MibScalar
jnxMbgPgwNotifRejRspRx = _JnxMbgPgwNotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 25),
    _JnxMbgPgwNotifRejRspRx_Type()
)
jnxMbgPgwNotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifRejRspRx.setStatus("deprecated")
_JnxMbgPgwRtInfReqRx_Type = Counter64
_JnxMbgPgwRtInfReqRx_Object = MibScalar
jnxMbgPgwRtInfReqRx = _JnxMbgPgwRtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 26),
    _JnxMbgPgwRtInfReqRx_Type()
)
jnxMbgPgwRtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwRtInfReqRx.setStatus("deprecated")
_JnxMbgPgwRtInfRspRx_Type = Counter64
_JnxMbgPgwRtInfRspRx_Object = MibScalar
jnxMbgPgwRtInfRspRx = _JnxMbgPgwRtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 27),
    _JnxMbgPgwRtInfRspRx_Type()
)
jnxMbgPgwRtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwRtInfRspRx.setStatus("deprecated")
_JnxMbgPgwFailRptReqRx_Type = Counter64
_JnxMbgPgwFailRptReqRx_Object = MibScalar
jnxMbgPgwFailRptReqRx = _JnxMbgPgwFailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 28),
    _JnxMbgPgwFailRptReqRx_Type()
)
jnxMbgPgwFailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwFailRptReqRx.setStatus("deprecated")
_JnxMbgPgwFailRptRspRx_Type = Counter64
_JnxMbgPgwFailRptRspRx_Object = MibScalar
jnxMbgPgwFailRptRspRx = _JnxMbgPgwFailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 29),
    _JnxMbgPgwFailRptRspRx_Type()
)
jnxMbgPgwFailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwFailRptRspRx.setStatus("deprecated")
_JnxMbgPgwNotMSPresReqRx_Type = Counter64
_JnxMbgPgwNotMSPresReqRx_Object = MibScalar
jnxMbgPgwNotMSPresReqRx = _JnxMbgPgwNotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 30),
    _JnxMbgPgwNotMSPresReqRx_Type()
)
jnxMbgPgwNotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotMSPresReqRx.setStatus("deprecated")
_JnxMbgPgwNotMSPresRspRx_Type = Counter64
_JnxMbgPgwNotMSPresRspRx_Object = MibScalar
jnxMbgPgwNotMSPresRspRx = _JnxMbgPgwNotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 31),
    _JnxMbgPgwNotMSPresRspRx_Type()
)
jnxMbgPgwNotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotMSPresRspRx.setStatus("deprecated")
_JnxMbgPgwGTPICsReqAccepted_Type = Counter64
_JnxMbgPgwGTPICsReqAccepted_Object = MibScalar
jnxMbgPgwGTPICsReqAccepted = _JnxMbgPgwGTPICsReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 32),
    _JnxMbgPgwGTPICsReqAccepted_Type()
)
jnxMbgPgwGTPICsReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsReqAccepted.setStatus("deprecated")
_JnxMbgPgwGTPICsNonExist_Type = Counter64
_JnxMbgPgwGTPICsNonExist_Object = MibScalar
jnxMbgPgwGTPICsNonExist = _JnxMbgPgwGTPICsNonExist_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 33),
    _JnxMbgPgwGTPICsNonExist_Type()
)
jnxMbgPgwGTPICsNonExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsNonExist.setStatus("deprecated")
_JnxMbgPgwGTPICsInvMsgFmt_Type = Counter64
_JnxMbgPgwGTPICsInvMsgFmt_Object = MibScalar
jnxMbgPgwGTPICsInvMsgFmt = _JnxMbgPgwGTPICsInvMsgFmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 34),
    _JnxMbgPgwGTPICsInvMsgFmt_Type()
)
jnxMbgPgwGTPICsInvMsgFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsInvMsgFmt.setStatus("deprecated")
_JnxMbgPgwGTPICsIMSINotKnown_Type = Counter64
_JnxMbgPgwGTPICsIMSINotKnown_Object = MibScalar
jnxMbgPgwGTPICsIMSINotKnown = _JnxMbgPgwGTPICsIMSINotKnown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 35),
    _JnxMbgPgwGTPICsIMSINotKnown_Type()
)
jnxMbgPgwGTPICsIMSINotKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsIMSINotKnown.setStatus("deprecated")
_JnxMbgPgwGTPICsMSGRPSDetach_Type = Counter64
_JnxMbgPgwGTPICsMSGRPSDetach_Object = MibScalar
jnxMbgPgwGTPICsMSGRPSDetach = _JnxMbgPgwGTPICsMSGRPSDetach_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 36),
    _JnxMbgPgwGTPICsMSGRPSDetach_Type()
)
jnxMbgPgwGTPICsMSGRPSDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsMSGRPSDetach.setStatus("deprecated")
_JnxMbgPgwGTPICsMSNotGRPSResp_Type = Counter64
_JnxMbgPgwGTPICsMSNotGRPSResp_Object = MibScalar
jnxMbgPgwGTPICsMSNotGRPSResp = _JnxMbgPgwGTPICsMSNotGRPSResp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 37),
    _JnxMbgPgwGTPICsMSNotGRPSResp_Type()
)
jnxMbgPgwGTPICsMSNotGRPSResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsMSNotGRPSResp.setStatus("deprecated")
_JnxMbgPgwGTPICsMSRefuses_Type = Counter64
_JnxMbgPgwGTPICsMSRefuses_Object = MibScalar
jnxMbgPgwGTPICsMSRefuses = _JnxMbgPgwGTPICsMSRefuses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 38),
    _JnxMbgPgwGTPICsMSRefuses_Type()
)
jnxMbgPgwGTPICsMSRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsMSRefuses.setStatus("deprecated")
_JnxMbgPgwGTPICsVerNotSupp_Type = Counter64
_JnxMbgPgwGTPICsVerNotSupp_Object = MibScalar
jnxMbgPgwGTPICsVerNotSupp = _JnxMbgPgwGTPICsVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 39),
    _JnxMbgPgwGTPICsVerNotSupp_Type()
)
jnxMbgPgwGTPICsVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsVerNotSupp.setStatus("deprecated")
_JnxMbgPgwGTPICsNoRes_Type = Counter64
_JnxMbgPgwGTPICsNoRes_Object = MibScalar
jnxMbgPgwGTPICsNoRes = _JnxMbgPgwGTPICsNoRes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 40),
    _JnxMbgPgwGTPICsNoRes_Type()
)
jnxMbgPgwGTPICsNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsNoRes.setStatus("deprecated")
_JnxMbgPgwGTPICsServNotSupp_Type = Counter64
_JnxMbgPgwGTPICsServNotSupp_Object = MibScalar
jnxMbgPgwGTPICsServNotSupp = _JnxMbgPgwGTPICsServNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 41),
    _JnxMbgPgwGTPICsServNotSupp_Type()
)
jnxMbgPgwGTPICsServNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsServNotSupp.setStatus("deprecated")
_JnxMbgPgwGTPICsManIEIncrt_Type = Counter64
_JnxMbgPgwGTPICsManIEIncrt_Object = MibScalar
jnxMbgPgwGTPICsManIEIncrt = _JnxMbgPgwGTPICsManIEIncrt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 42),
    _JnxMbgPgwGTPICsManIEIncrt_Type()
)
jnxMbgPgwGTPICsManIEIncrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsManIEIncrt.setStatus("deprecated")
_JnxMbgPgwGTPICsManIEMiss_Type = Counter64
_JnxMbgPgwGTPICsManIEMiss_Object = MibScalar
jnxMbgPgwGTPICsManIEMiss = _JnxMbgPgwGTPICsManIEMiss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 43),
    _JnxMbgPgwGTPICsManIEMiss_Type()
)
jnxMbgPgwGTPICsManIEMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsManIEMiss.setStatus("deprecated")
_JnxMbgPgwGTPICsOptIEIncrt_Type = Counter64
_JnxMbgPgwGTPICsOptIEIncrt_Object = MibScalar
jnxMbgPgwGTPICsOptIEIncrt = _JnxMbgPgwGTPICsOptIEIncrt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 44),
    _JnxMbgPgwGTPICsOptIEIncrt_Type()
)
jnxMbgPgwGTPICsOptIEIncrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsOptIEIncrt.setStatus("deprecated")
_JnxMbgPgwGTPICsSysFail_Type = Counter64
_JnxMbgPgwGTPICsSysFail_Object = MibScalar
jnxMbgPgwGTPICsSysFail = _JnxMbgPgwGTPICsSysFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 45),
    _JnxMbgPgwGTPICsSysFail_Type()
)
jnxMbgPgwGTPICsSysFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsSysFail.setStatus("deprecated")
_JnxMbgPgwGTPICsRoamRestrict_Type = Counter64
_JnxMbgPgwGTPICsRoamRestrict_Object = MibScalar
jnxMbgPgwGTPICsRoamRestrict = _JnxMbgPgwGTPICsRoamRestrict_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 46),
    _JnxMbgPgwGTPICsRoamRestrict_Type()
)
jnxMbgPgwGTPICsRoamRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsRoamRestrict.setStatus("deprecated")
_JnxMbgPgwGTPICsPTMSISigMismatch_Type = Counter64
_JnxMbgPgwGTPICsPTMSISigMismatch_Object = MibScalar
jnxMbgPgwGTPICsPTMSISigMismatch = _JnxMbgPgwGTPICsPTMSISigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 47),
    _JnxMbgPgwGTPICsPTMSISigMismatch_Type()
)
jnxMbgPgwGTPICsPTMSISigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsPTMSISigMismatch.setStatus("deprecated")
_JnxMbgPgwGTPICsGPRSConnSupp_Type = Counter64
_JnxMbgPgwGTPICsGPRSConnSupp_Object = MibScalar
jnxMbgPgwGTPICsGPRSConnSupp = _JnxMbgPgwGTPICsGPRSConnSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 48),
    _JnxMbgPgwGTPICsGPRSConnSupp_Type()
)
jnxMbgPgwGTPICsGPRSConnSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsGPRSConnSupp.setStatus("deprecated")
_JnxMbgPgwGTPICsAuthFail_Type = Counter64
_JnxMbgPgwGTPICsAuthFail_Object = MibScalar
jnxMbgPgwGTPICsAuthFail = _JnxMbgPgwGTPICsAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 49),
    _JnxMbgPgwGTPICsAuthFail_Type()
)
jnxMbgPgwGTPICsAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsAuthFail.setStatus("deprecated")
_JnxMbgPgwGTPICsUserAuthFail_Type = Counter64
_JnxMbgPgwGTPICsUserAuthFail_Object = MibScalar
jnxMbgPgwGTPICsUserAuthFail = _JnxMbgPgwGTPICsUserAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 50),
    _JnxMbgPgwGTPICsUserAuthFail_Type()
)
jnxMbgPgwGTPICsUserAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPICsUserAuthFail.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsCtxNotFnd_Type = Counter64
_JnxMbgPgwGTPV1ICsCtxNotFnd_Object = MibScalar
jnxMbgPgwGTPV1ICsCtxNotFnd = _JnxMbgPgwGTPV1ICsCtxNotFnd_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 51),
    _JnxMbgPgwGTPV1ICsCtxNotFnd_Type()
)
jnxMbgPgwGTPV1ICsCtxNotFnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsCtxNotFnd.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsAllDynPDPAddr_Type = Counter64
_JnxMbgPgwGTPV1ICsAllDynPDPAddr_Object = MibScalar
jnxMbgPgwGTPV1ICsAllDynPDPAddr = _JnxMbgPgwGTPV1ICsAllDynPDPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 52),
    _JnxMbgPgwGTPV1ICsAllDynPDPAddr_Type()
)
jnxMbgPgwGTPV1ICsAllDynPDPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsAllDynPDPAddr.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsNoMem_Type = Counter64
_JnxMbgPgwGTPV1ICsNoMem_Object = MibScalar
jnxMbgPgwGTPV1ICsNoMem = _JnxMbgPgwGTPV1ICsNoMem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 53),
    _JnxMbgPgwGTPV1ICsNoMem_Type()
)
jnxMbgPgwGTPV1ICsNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsNoMem.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsRelocFail_Type = Counter64
_JnxMbgPgwGTPV1ICsRelocFail_Object = MibScalar
jnxMbgPgwGTPV1ICsRelocFail = _JnxMbgPgwGTPV1ICsRelocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 54),
    _JnxMbgPgwGTPV1ICsRelocFail_Type()
)
jnxMbgPgwGTPV1ICsRelocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsRelocFail.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsUnkManExthdr_Type = Counter64
_JnxMbgPgwGTPV1ICsUnkManExthdr_Object = MibScalar
jnxMbgPgwGTPV1ICsUnkManExthdr = _JnxMbgPgwGTPV1ICsUnkManExthdr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 55),
    _JnxMbgPgwGTPV1ICsUnkManExthdr_Type()
)
jnxMbgPgwGTPV1ICsUnkManExthdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsUnkManExthdr.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsSMANTTFTErr1_Type = Counter64
_JnxMbgPgwGTPV1ICsSMANTTFTErr1_Object = MibScalar
jnxMbgPgwGTPV1ICsSMANTTFTErr1 = _JnxMbgPgwGTPV1ICsSMANTTFTErr1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 56),
    _JnxMbgPgwGTPV1ICsSMANTTFTErr1_Type()
)
jnxMbgPgwGTPV1ICsSMANTTFTErr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsSMANTTFTErr1.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsSYNTFTErr2_Type = Counter64
_JnxMbgPgwGTPV1ICsSYNTFTErr2_Object = MibScalar
jnxMbgPgwGTPV1ICsSYNTFTErr2 = _JnxMbgPgwGTPV1ICsSYNTFTErr2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 57),
    _JnxMbgPgwGTPV1ICsSYNTFTErr2_Type()
)
jnxMbgPgwGTPV1ICsSYNTFTErr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsSYNTFTErr2.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsSMNTPktFltrErr1_Type = Counter64
_JnxMbgPgwGTPV1ICsSMNTPktFltrErr1_Object = MibScalar
jnxMbgPgwGTPV1ICsSMNTPktFltrErr1 = _JnxMbgPgwGTPV1ICsSMNTPktFltrErr1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 58),
    _JnxMbgPgwGTPV1ICsSMNTPktFltrErr1_Type()
)
jnxMbgPgwGTPV1ICsSMNTPktFltrErr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsSMNTPktFltrErr1.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsSYNPktFltrErr2_Type = Counter64
_JnxMbgPgwGTPV1ICsSYNPktFltrErr2_Object = MibScalar
jnxMbgPgwGTPV1ICsSYNPktFltrErr2 = _JnxMbgPgwGTPV1ICsSYNPktFltrErr2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 59),
    _JnxMbgPgwGTPV1ICsSYNPktFltrErr2_Type()
)
jnxMbgPgwGTPV1ICsSYNPktFltrErr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsSYNPktFltrErr2.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsMissUnknownAPN_Type = Counter64
_JnxMbgPgwGTPV1ICsMissUnknownAPN_Object = MibScalar
jnxMbgPgwGTPV1ICsMissUnknownAPN = _JnxMbgPgwGTPV1ICsMissUnknownAPN_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 60),
    _JnxMbgPgwGTPV1ICsMissUnknownAPN_Type()
)
jnxMbgPgwGTPV1ICsMissUnknownAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsMissUnknownAPN.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsUnknownPDPAddr_Type = Counter64
_JnxMbgPgwGTPV1ICsUnknownPDPAddr_Object = MibScalar
jnxMbgPgwGTPV1ICsUnknownPDPAddr = _JnxMbgPgwGTPV1ICsUnknownPDPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 61),
    _JnxMbgPgwGTPV1ICsUnknownPDPAddr_Type()
)
jnxMbgPgwGTPV1ICsUnknownPDPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsUnknownPDPAddr.setStatus("deprecated")
_JnxMbgPgwGTPV1ICsNoTFTCtxExist_Type = Counter64
_JnxMbgPgwGTPV1ICsNoTFTCtxExist_Object = MibScalar
jnxMbgPgwGTPV1ICsNoTFTCtxExist = _JnxMbgPgwGTPV1ICsNoTFTCtxExist_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 62),
    _JnxMbgPgwGTPV1ICsNoTFTCtxExist_Type()
)
jnxMbgPgwGTPV1ICsNoTFTCtxExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV1ICsNoTFTCtxExist.setStatus("deprecated")
_JnxMbgPgwV1NumMsgTx_Type = Counter64
_JnxMbgPgwV1NumMsgTx_Object = MibScalar
jnxMbgPgwV1NumMsgTx = _JnxMbgPgwV1NumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 63),
    _JnxMbgPgwV1NumMsgTx_Type()
)
jnxMbgPgwV1NumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NumMsgTx.setStatus("deprecated")
_JnxMbgPgwV1NumBytesTx_Type = Counter64
_JnxMbgPgwV1NumBytesTx_Object = MibScalar
jnxMbgPgwV1NumBytesTx = _JnxMbgPgwV1NumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 64),
    _JnxMbgPgwV1NumBytesTx_Type()
)
jnxMbgPgwV1NumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NumBytesTx.setStatus("deprecated")
_JnxMbgPgwV1EchoReqTx_Type = Counter64
_JnxMbgPgwV1EchoReqTx_Object = MibScalar
jnxMbgPgwV1EchoReqTx = _JnxMbgPgwV1EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 65),
    _JnxMbgPgwV1EchoReqTx_Type()
)
jnxMbgPgwV1EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1EchoReqTx.setStatus("deprecated")
_JnxMbgPgwV1EchoRespTx_Type = Counter64
_JnxMbgPgwV1EchoRespTx_Object = MibScalar
jnxMbgPgwV1EchoRespTx = _JnxMbgPgwV1EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 66),
    _JnxMbgPgwV1EchoRespTx_Type()
)
jnxMbgPgwV1EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1EchoRespTx.setStatus("deprecated")
_JnxMbgPgwCrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwCrtPdpCxtReqTx_Object = MibScalar
jnxMbgPgwCrtPdpCxtReqTx = _JnxMbgPgwCrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 67),
    _JnxMbgPgwCrtPdpCxtReqTx_Type()
)
jnxMbgPgwCrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwCrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwCrtPdpCxtRspTx_Object = MibScalar
jnxMbgPgwCrtPdpCxtRspTx = _JnxMbgPgwCrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 68),
    _JnxMbgPgwCrtPdpCxtRspTx_Type()
)
jnxMbgPgwCrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwUpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwUpdPdpCxtReqTx_Object = MibScalar
jnxMbgPgwUpdPdpCxtReqTx = _JnxMbgPgwUpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 69),
    _JnxMbgPgwUpdPdpCxtReqTx_Type()
)
jnxMbgPgwUpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwUpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwUpdPdpCxtRspTx_Object = MibScalar
jnxMbgPgwUpdPdpCxtRspTx = _JnxMbgPgwUpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 70),
    _JnxMbgPgwUpdPdpCxtRspTx_Type()
)
jnxMbgPgwUpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUpdPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwDelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwDelPdpCxtReqTx_Object = MibScalar
jnxMbgPgwDelPdpCxtReqTx = _JnxMbgPgwDelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 71),
    _JnxMbgPgwDelPdpCxtReqTx_Type()
)
jnxMbgPgwDelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwDelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwDelPdpCxtRspTx_Object = MibScalar
jnxMbgPgwDelPdpCxtRspTx = _JnxMbgPgwDelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 72),
    _JnxMbgPgwDelPdpCxtRspTx_Type()
)
jnxMbgPgwDelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwCrtAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwCrtAAPdpCxtReqTx_Object = MibScalar
jnxMbgPgwCrtAAPdpCxtReqTx = _JnxMbgPgwCrtAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 73),
    _JnxMbgPgwCrtAAPdpCxtReqTx_Type()
)
jnxMbgPgwCrtAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtAAPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwCrtAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwCrtAAPdpCxtRspTx_Object = MibScalar
jnxMbgPgwCrtAAPdpCxtRspTx = _JnxMbgPgwCrtAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 74),
    _JnxMbgPgwCrtAAPdpCxtRspTx_Type()
)
jnxMbgPgwCrtAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwCrtAAPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwDelAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwDelAAPdpCxtReqTx_Object = MibScalar
jnxMbgPgwDelAAPdpCxtReqTx = _JnxMbgPgwDelAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 75),
    _JnxMbgPgwDelAAPdpCxtReqTx_Type()
)
jnxMbgPgwDelAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelAAPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwDelAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwDelAAPdpCxtRspTx_Object = MibScalar
jnxMbgPgwDelAAPdpCxtRspTx = _JnxMbgPgwDelAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 76),
    _JnxMbgPgwDelAAPdpCxtRspTx_Type()
)
jnxMbgPgwDelAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwDelAAPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwErrorIndTx_Type = Counter64
_JnxMbgPgwErrorIndTx_Object = MibScalar
jnxMbgPgwErrorIndTx = _JnxMbgPgwErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 77),
    _JnxMbgPgwErrorIndTx_Type()
)
jnxMbgPgwErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwErrorIndTx.setStatus("deprecated")
_JnxMbgPgwNotifReqTx_Type = Counter64
_JnxMbgPgwNotifReqTx_Object = MibScalar
jnxMbgPgwNotifReqTx = _JnxMbgPgwNotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 78),
    _JnxMbgPgwNotifReqTx_Type()
)
jnxMbgPgwNotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifReqTx.setStatus("deprecated")
_JnxMbgPgwNotifRspTx_Type = Counter64
_JnxMbgPgwNotifRspTx_Object = MibScalar
jnxMbgPgwNotifRspTx = _JnxMbgPgwNotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 79),
    _JnxMbgPgwNotifRspTx_Type()
)
jnxMbgPgwNotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifRspTx.setStatus("deprecated")
_JnxMbgPgwNotifRejReqTx_Type = Counter64
_JnxMbgPgwNotifRejReqTx_Object = MibScalar
jnxMbgPgwNotifRejReqTx = _JnxMbgPgwNotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 80),
    _JnxMbgPgwNotifRejReqTx_Type()
)
jnxMbgPgwNotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifRejReqTx.setStatus("deprecated")
_JnxMbgPgwNotifRejRspTx_Type = Counter64
_JnxMbgPgwNotifRejRspTx_Object = MibScalar
jnxMbgPgwNotifRejRspTx = _JnxMbgPgwNotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 81),
    _JnxMbgPgwNotifRejRspTx_Type()
)
jnxMbgPgwNotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotifRejRspTx.setStatus("deprecated")
_JnxMbgPgwRtInfReqTx_Type = Counter64
_JnxMbgPgwRtInfReqTx_Object = MibScalar
jnxMbgPgwRtInfReqTx = _JnxMbgPgwRtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 82),
    _JnxMbgPgwRtInfReqTx_Type()
)
jnxMbgPgwRtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwRtInfReqTx.setStatus("deprecated")
_JnxMbgPgwRtInfRspTx_Type = Counter64
_JnxMbgPgwRtInfRspTx_Object = MibScalar
jnxMbgPgwRtInfRspTx = _JnxMbgPgwRtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 83),
    _JnxMbgPgwRtInfRspTx_Type()
)
jnxMbgPgwRtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwRtInfRspTx.setStatus("deprecated")
_JnxMbgPgwFailRptReqTx_Type = Counter64
_JnxMbgPgwFailRptReqTx_Object = MibScalar
jnxMbgPgwFailRptReqTx = _JnxMbgPgwFailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 84),
    _JnxMbgPgwFailRptReqTx_Type()
)
jnxMbgPgwFailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwFailRptReqTx.setStatus("deprecated")
_JnxMbgPgwFailRptRspTx_Type = Counter64
_JnxMbgPgwFailRptRspTx_Object = MibScalar
jnxMbgPgwFailRptRspTx = _JnxMbgPgwFailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 85),
    _JnxMbgPgwFailRptRspTx_Type()
)
jnxMbgPgwFailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwFailRptRspTx.setStatus("deprecated")
_JnxMbgPgwNotMSPresReqTx_Type = Counter64
_JnxMbgPgwNotMSPresReqTx_Object = MibScalar
jnxMbgPgwNotMSPresReqTx = _JnxMbgPgwNotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 86),
    _JnxMbgPgwNotMSPresReqTx_Type()
)
jnxMbgPgwNotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotMSPresReqTx.setStatus("deprecated")
_JnxMbgPgwNotMSPresRspTx_Type = Counter64
_JnxMbgPgwNotMSPresRspTx_Object = MibScalar
jnxMbgPgwNotMSPresRspTx = _JnxMbgPgwNotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 5, 87),
    _JnxMbgPgwNotMSPresRspTx_Type()
)
jnxMbgPgwNotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwNotMSPresRspTx.setStatus("deprecated")
_JnxMbgPgwGtpPeerStatsTable_Object = MibTable
jnxMbgPgwGtpPeerStatsTable = _JnxMbgPgwGtpPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6)
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerStatsTable.setStatus("deprecated")
_JnxMbgPgwGtpPeerEntry_Object = MibTableRow
jnxMbgPgwGtpPeerEntry = _JnxMbgPgwGtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1)
)
jnxMbgPgwGtpPeerEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerRmtAddr"),
    (0, "JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerLclAddr"),
    (0, "JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerRtgInst"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerEntry.setStatus("deprecated")
_JnxMbgPgwGtpPeerRmtAddr_Type = IpAddress
_JnxMbgPgwGtpPeerRmtAddr_Object = MibTableColumn
jnxMbgPgwGtpPeerRmtAddr = _JnxMbgPgwGtpPeerRmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 1),
    _JnxMbgPgwGtpPeerRmtAddr_Type()
)
jnxMbgPgwGtpPeerRmtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerRmtAddr.setStatus("deprecated")
_JnxMbgPgwGtpPeerLclAddr_Type = IpAddress
_JnxMbgPgwGtpPeerLclAddr_Object = MibTableColumn
jnxMbgPgwGtpPeerLclAddr = _JnxMbgPgwGtpPeerLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 2),
    _JnxMbgPgwGtpPeerLclAddr_Type()
)
jnxMbgPgwGtpPeerLclAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerLclAddr.setStatus("deprecated")
_JnxMbgPgwGtpPeerRtgInst_Type = Unsigned32
_JnxMbgPgwGtpPeerRtgInst_Object = MibTableColumn
jnxMbgPgwGtpPeerRtgInst = _JnxMbgPgwGtpPeerRtgInst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 3),
    _JnxMbgPgwGtpPeerRtgInst_Type()
)
jnxMbgPgwGtpPeerRtgInst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerRtgInst.setStatus("deprecated")
_JnxMbgPgwGtpDropCounter_Type = Counter64
_JnxMbgPgwGtpDropCounter_Object = MibTableColumn
jnxMbgPgwGtpDropCounter = _JnxMbgPgwGtpDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 4),
    _JnxMbgPgwGtpDropCounter_Type()
)
jnxMbgPgwGtpDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpDropCounter.setStatus("deprecated")
_JnxMbgPgwGtpPktAllocFail_Type = Counter64
_JnxMbgPgwGtpPktAllocFail_Object = MibTableColumn
jnxMbgPgwGtpPktAllocFail = _JnxMbgPgwGtpPktAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 5),
    _JnxMbgPgwGtpPktAllocFail_Type()
)
jnxMbgPgwGtpPktAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPktAllocFail.setStatus("deprecated")
_JnxMbgPgwGtpPktSendFail_Type = Counter64
_JnxMbgPgwGtpPktSendFail_Object = MibTableColumn
jnxMbgPgwGtpPktSendFail = _JnxMbgPgwGtpPktSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 6),
    _JnxMbgPgwGtpPktSendFail_Type()
)
jnxMbgPgwGtpPktSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPktSendFail.setStatus("deprecated")
_JnxMbgPgwGtpIPVerErrRx_Type = Counter64
_JnxMbgPgwGtpIPVerErrRx_Object = MibTableColumn
jnxMbgPgwGtpIPVerErrRx = _JnxMbgPgwGtpIPVerErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 7),
    _JnxMbgPgwGtpIPVerErrRx_Type()
)
jnxMbgPgwGtpIPVerErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpIPVerErrRx.setStatus("deprecated")
_JnxMbgPgwGtpIPProtoErrRx_Type = Counter64
_JnxMbgPgwGtpIPProtoErrRx_Object = MibTableColumn
jnxMbgPgwGtpIPProtoErrRx = _JnxMbgPgwGtpIPProtoErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 8),
    _JnxMbgPgwGtpIPProtoErrRx_Type()
)
jnxMbgPgwGtpIPProtoErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpIPProtoErrRx.setStatus("deprecated")
_JnxMbgPgwGtpPktLenErrRx_Type = Counter64
_JnxMbgPgwGtpPktLenErrRx_Object = MibTableColumn
jnxMbgPgwGtpPktLenErrRx = _JnxMbgPgwGtpPktLenErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 9),
    _JnxMbgPgwGtpPktLenErrRx_Type()
)
jnxMbgPgwGtpPktLenErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPktLenErrRx.setStatus("deprecated")
_JnxMbgPgwGtpUnkMsgRx_Type = Counter64
_JnxMbgPgwGtpUnkMsgRx_Object = MibTableColumn
jnxMbgPgwGtpUnkMsgRx = _JnxMbgPgwGtpUnkMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 10),
    _JnxMbgPgwGtpUnkMsgRx_Type()
)
jnxMbgPgwGtpUnkMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpUnkMsgRx.setStatus("deprecated")
_JnxMbgPgwGtpMemAllocFailed_Type = Counter64
_JnxMbgPgwGtpMemAllocFailed_Object = MibTableColumn
jnxMbgPgwGtpMemAllocFailed = _JnxMbgPgwGtpMemAllocFailed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 6, 1, 11),
    _JnxMbgPgwGtpMemAllocFailed_Type()
)
jnxMbgPgwGtpMemAllocFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpMemAllocFailed.setStatus("deprecated")
_JnxMbgPgwGtpNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpNotificationVars = _JnxMbgPgwGtpNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7)
)
_JnxMbgPgwGtpPeerName_Type = DisplayString
_JnxMbgPgwGtpPeerName_Object = MibScalar
jnxMbgPgwGtpPeerName = _JnxMbgPgwGtpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7, 1),
    _JnxMbgPgwGtpPeerName_Type()
)
jnxMbgPgwGtpPeerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerName.setStatus("current")


class _JnxMbgPgwGtpAlarmThrshld_Type(Integer32):
    """Custom type jnxMbgPgwGtpAlarmThrshld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("thresholdhigh", 1),
          ("thresholdlow", 0))
    )


_JnxMbgPgwGtpAlarmThrshld_Type.__name__ = "Integer32"
_JnxMbgPgwGtpAlarmThrshld_Object = MibScalar
jnxMbgPgwGtpAlarmThrshld = _JnxMbgPgwGtpAlarmThrshld_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7, 2),
    _JnxMbgPgwGtpAlarmThrshld_Type()
)
jnxMbgPgwGtpAlarmThrshld.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpAlarmThrshld.setStatus("deprecated")


class _JnxMbgPgwGtpAlarmState_Type(Integer32):
    """Custom type jnxMbgPgwGtpAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("alarmcleared", 0),
          ("alarmraised", 1))
    )


_JnxMbgPgwGtpAlarmState_Type.__name__ = "Integer32"
_JnxMbgPgwGtpAlarmState_Object = MibScalar
jnxMbgPgwGtpAlarmState = _JnxMbgPgwGtpAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7, 3),
    _JnxMbgPgwGtpAlarmState_Type()
)
jnxMbgPgwGtpAlarmState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpAlarmState.setStatus("deprecated")
_JnxMbgPgwGtpAlarmStatCounter_Type = Unsigned32
_JnxMbgPgwGtpAlarmStatCounter_Object = MibScalar
jnxMbgPgwGtpAlarmStatCounter = _JnxMbgPgwGtpAlarmStatCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7, 4),
    _JnxMbgPgwGtpAlarmStatCounter_Type()
)
jnxMbgPgwGtpAlarmStatCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpAlarmStatCounter.setStatus("current")
_JnxMbgPgwGtpInterfaceType_Type = DisplayString
_JnxMbgPgwGtpInterfaceType_Object = MibScalar
jnxMbgPgwGtpInterfaceType = _JnxMbgPgwGtpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7, 5),
    _JnxMbgPgwGtpInterfaceType_Type()
)
jnxMbgPgwGtpInterfaceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpInterfaceType.setStatus("current")
_JnxMbgPgwGtpGwName_Type = DisplayString
_JnxMbgPgwGtpGwName_Object = MibScalar
jnxMbgPgwGtpGwName = _JnxMbgPgwGtpGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7, 6),
    _JnxMbgPgwGtpGwName_Type()
)
jnxMbgPgwGtpGwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpGwName.setStatus("current")
_JnxMbgPgwGtpGwIndex_Type = Unsigned32
_JnxMbgPgwGtpGwIndex_Object = MibScalar
jnxMbgPgwGtpGwIndex = _JnxMbgPgwGtpGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 7, 7),
    _JnxMbgPgwGtpGwIndex_Type()
)
jnxMbgPgwGtpGwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpGwIndex.setStatus("current")
_JnxMbgPgwGtpV0Stats_ObjectIdentity = ObjectIdentity
jnxMbgPgwGtpV0Stats = _JnxMbgPgwGtpV0Stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8)
)
_JnxMbgPgwV0NumMsgRx_Type = Counter64
_JnxMbgPgwV0NumMsgRx_Object = MibScalar
jnxMbgPgwV0NumMsgRx = _JnxMbgPgwV0NumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 1),
    _JnxMbgPgwV0NumMsgRx_Type()
)
jnxMbgPgwV0NumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NumMsgRx.setStatus("deprecated")
_JnxMbgPgwV0NumBytesRx_Type = Counter64
_JnxMbgPgwV0NumBytesRx_Object = MibScalar
jnxMbgPgwV0NumBytesRx = _JnxMbgPgwV0NumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 2),
    _JnxMbgPgwV0NumBytesRx_Type()
)
jnxMbgPgwV0NumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NumBytesRx.setStatus("deprecated")
_JnxMbgPgwV0UnSupportedMsg_Type = Counter64
_JnxMbgPgwV0UnSupportedMsg_Object = MibScalar
jnxMbgPgwV0UnSupportedMsg = _JnxMbgPgwV0UnSupportedMsg_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 3),
    _JnxMbgPgwV0UnSupportedMsg_Type()
)
jnxMbgPgwV0UnSupportedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0UnSupportedMsg.setStatus("deprecated")
_JnxMbgPgwV0ProtErr_Type = Counter64
_JnxMbgPgwV0ProtErr_Object = MibScalar
jnxMbgPgwV0ProtErr = _JnxMbgPgwV0ProtErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 4),
    _JnxMbgPgwV0ProtErr_Type()
)
jnxMbgPgwV0ProtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ProtErr.setStatus("deprecated")
_JnxMbgPgwV0T3RespTmrExp_Type = Counter64
_JnxMbgPgwV0T3RespTmrExp_Object = MibScalar
jnxMbgPgwV0T3RespTmrExp = _JnxMbgPgwV0T3RespTmrExp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 5),
    _JnxMbgPgwV0T3RespTmrExp_Type()
)
jnxMbgPgwV0T3RespTmrExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0T3RespTmrExp.setStatus("deprecated")
_JnxMbgPgwV0MsgRedirectRx_Type = Counter64
_JnxMbgPgwV0MsgRedirectRx_Object = MibScalar
jnxMbgPgwV0MsgRedirectRx = _JnxMbgPgwV0MsgRedirectRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 6),
    _JnxMbgPgwV0MsgRedirectRx_Type()
)
jnxMbgPgwV0MsgRedirectRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0MsgRedirectRx.setStatus("deprecated")
_JnxMbgPgwV0MsgRedirectTx_Type = Counter64
_JnxMbgPgwV0MsgRedirectTx_Object = MibScalar
jnxMbgPgwV0MsgRedirectTx = _JnxMbgPgwV0MsgRedirectTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 7),
    _JnxMbgPgwV0MsgRedirectTx_Type()
)
jnxMbgPgwV0MsgRedirectTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0MsgRedirectTx.setStatus("deprecated")
_JnxMbgPgwV0SuppExtHdrNot_Type = Counter64
_JnxMbgPgwV0SuppExtHdrNot_Object = MibScalar
jnxMbgPgwV0SuppExtHdrNot = _JnxMbgPgwV0SuppExtHdrNot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 8),
    _JnxMbgPgwV0SuppExtHdrNot_Type()
)
jnxMbgPgwV0SuppExtHdrNot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0SuppExtHdrNot.setStatus("deprecated")
_JnxMbgPgwV0EchoReqRx_Type = Counter64
_JnxMbgPgwV0EchoReqRx_Object = MibScalar
jnxMbgPgwV0EchoReqRx = _JnxMbgPgwV0EchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 9),
    _JnxMbgPgwV0EchoReqRx_Type()
)
jnxMbgPgwV0EchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0EchoReqRx.setStatus("deprecated")
_JnxMbgPgwV0EchoRespRx_Type = Counter64
_JnxMbgPgwV0EchoRespRx_Object = MibScalar
jnxMbgPgwV0EchoRespRx = _JnxMbgPgwV0EchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 10),
    _JnxMbgPgwV0EchoRespRx_Type()
)
jnxMbgPgwV0EchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0EchoRespRx.setStatus("deprecated")
_JnxMbgPgwV0CrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0CrtPdpCxtReqRx_Object = MibScalar
jnxMbgPgwV0CrtPdpCxtReqRx = _JnxMbgPgwV0CrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 11),
    _JnxMbgPgwV0CrtPdpCxtReqRx_Type()
)
jnxMbgPgwV0CrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwV0CrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0CrtPdpCxtRspRx_Object = MibScalar
jnxMbgPgwV0CrtPdpCxtRspRx = _JnxMbgPgwV0CrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 12),
    _JnxMbgPgwV0CrtPdpCxtRspRx_Type()
)
jnxMbgPgwV0CrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwV0UpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0UpdPdpCxtReqRx_Object = MibScalar
jnxMbgPgwV0UpdPdpCxtReqRx = _JnxMbgPgwV0UpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 13),
    _JnxMbgPgwV0UpdPdpCxtReqRx_Type()
)
jnxMbgPgwV0UpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0UpdPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwV0UpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0UpdPdpCxtRspRx_Object = MibScalar
jnxMbgPgwV0UpdPdpCxtRspRx = _JnxMbgPgwV0UpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 14),
    _JnxMbgPgwV0UpdPdpCxtRspRx_Type()
)
jnxMbgPgwV0UpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0UpdPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwV0DelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0DelPdpCxtReqRx_Object = MibScalar
jnxMbgPgwV0DelPdpCxtReqRx = _JnxMbgPgwV0DelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 15),
    _JnxMbgPgwV0DelPdpCxtReqRx_Type()
)
jnxMbgPgwV0DelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwV0DelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0DelPdpCxtRspRx_Object = MibScalar
jnxMbgPgwV0DelPdpCxtRspRx = _JnxMbgPgwV0DelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 16),
    _JnxMbgPgwV0DelPdpCxtRspRx_Type()
)
jnxMbgPgwV0DelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwV0CrtAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0CrtAAPdpCxtReqRx_Object = MibScalar
jnxMbgPgwV0CrtAAPdpCxtReqRx = _JnxMbgPgwV0CrtAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 17),
    _JnxMbgPgwV0CrtAAPdpCxtReqRx_Type()
)
jnxMbgPgwV0CrtAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtAAPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwV0CrtAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0CrtAAPdpCxtRspRx_Object = MibScalar
jnxMbgPgwV0CrtAAPdpCxtRspRx = _JnxMbgPgwV0CrtAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 18),
    _JnxMbgPgwV0CrtAAPdpCxtRspRx_Type()
)
jnxMbgPgwV0CrtAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtAAPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwV0DelAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0DelAAPdpCxtReqRx_Object = MibScalar
jnxMbgPgwV0DelAAPdpCxtReqRx = _JnxMbgPgwV0DelAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 19),
    _JnxMbgPgwV0DelAAPdpCxtReqRx_Type()
)
jnxMbgPgwV0DelAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelAAPdpCxtReqRx.setStatus("deprecated")
_JnxMbgPgwV0DelAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0DelAAPdpCxtRspRx_Object = MibScalar
jnxMbgPgwV0DelAAPdpCxtRspRx = _JnxMbgPgwV0DelAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 20),
    _JnxMbgPgwV0DelAAPdpCxtRspRx_Type()
)
jnxMbgPgwV0DelAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelAAPdpCxtRspRx.setStatus("deprecated")
_JnxMbgPgwV0ErrorIndRx_Type = Counter64
_JnxMbgPgwV0ErrorIndRx_Object = MibScalar
jnxMbgPgwV0ErrorIndRx = _JnxMbgPgwV0ErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 21),
    _JnxMbgPgwV0ErrorIndRx_Type()
)
jnxMbgPgwV0ErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ErrorIndRx.setStatus("deprecated")
_JnxMbgPgwV0NotifReqRx_Type = Counter64
_JnxMbgPgwV0NotifReqRx_Object = MibScalar
jnxMbgPgwV0NotifReqRx = _JnxMbgPgwV0NotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 22),
    _JnxMbgPgwV0NotifReqRx_Type()
)
jnxMbgPgwV0NotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifReqRx.setStatus("deprecated")
_JnxMbgPgwV0NotifRspRx_Type = Counter64
_JnxMbgPgwV0NotifRspRx_Object = MibScalar
jnxMbgPgwV0NotifRspRx = _JnxMbgPgwV0NotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 23),
    _JnxMbgPgwV0NotifRspRx_Type()
)
jnxMbgPgwV0NotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifRspRx.setStatus("deprecated")
_JnxMbgPgwV0NotifRejReqRx_Type = Counter64
_JnxMbgPgwV0NotifRejReqRx_Object = MibScalar
jnxMbgPgwV0NotifRejReqRx = _JnxMbgPgwV0NotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 24),
    _JnxMbgPgwV0NotifRejReqRx_Type()
)
jnxMbgPgwV0NotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifRejReqRx.setStatus("deprecated")
_JnxMbgPgwV0NotifRejRspRx_Type = Counter64
_JnxMbgPgwV0NotifRejRspRx_Object = MibScalar
jnxMbgPgwV0NotifRejRspRx = _JnxMbgPgwV0NotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 25),
    _JnxMbgPgwV0NotifRejRspRx_Type()
)
jnxMbgPgwV0NotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifRejRspRx.setStatus("deprecated")
_JnxMbgPgwV0RtInfReqRx_Type = Counter64
_JnxMbgPgwV0RtInfReqRx_Object = MibScalar
jnxMbgPgwV0RtInfReqRx = _JnxMbgPgwV0RtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 26),
    _JnxMbgPgwV0RtInfReqRx_Type()
)
jnxMbgPgwV0RtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0RtInfReqRx.setStatus("deprecated")
_JnxMbgPgwV0RtInfRspRx_Type = Counter64
_JnxMbgPgwV0RtInfRspRx_Object = MibScalar
jnxMbgPgwV0RtInfRspRx = _JnxMbgPgwV0RtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 27),
    _JnxMbgPgwV0RtInfRspRx_Type()
)
jnxMbgPgwV0RtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0RtInfRspRx.setStatus("deprecated")
_JnxMbgPgwV0FailRptReqRx_Type = Counter64
_JnxMbgPgwV0FailRptReqRx_Object = MibScalar
jnxMbgPgwV0FailRptReqRx = _JnxMbgPgwV0FailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 28),
    _JnxMbgPgwV0FailRptReqRx_Type()
)
jnxMbgPgwV0FailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0FailRptReqRx.setStatus("deprecated")
_JnxMbgPgwV0FailRptRspRx_Type = Counter64
_JnxMbgPgwV0FailRptRspRx_Object = MibScalar
jnxMbgPgwV0FailRptRspRx = _JnxMbgPgwV0FailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 29),
    _JnxMbgPgwV0FailRptRspRx_Type()
)
jnxMbgPgwV0FailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0FailRptRspRx.setStatus("deprecated")
_JnxMbgPgwV0NotMSPresReqRx_Type = Counter64
_JnxMbgPgwV0NotMSPresReqRx_Object = MibScalar
jnxMbgPgwV0NotMSPresReqRx = _JnxMbgPgwV0NotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 30),
    _JnxMbgPgwV0NotMSPresReqRx_Type()
)
jnxMbgPgwV0NotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotMSPresReqRx.setStatus("deprecated")
_JnxMbgPgwV0NotMSPresRspRx_Type = Counter64
_JnxMbgPgwV0NotMSPresRspRx_Object = MibScalar
jnxMbgPgwV0NotMSPresRspRx = _JnxMbgPgwV0NotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 31),
    _JnxMbgPgwV0NotMSPresRspRx_Type()
)
jnxMbgPgwV0NotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotMSPresRspRx.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsReqAccepted_Type = Counter64
_JnxMbgPgwGTPV0ICsReqAccepted_Object = MibScalar
jnxMbgPgwGTPV0ICsReqAccepted = _JnxMbgPgwGTPV0ICsReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 32),
    _JnxMbgPgwGTPV0ICsReqAccepted_Type()
)
jnxMbgPgwGTPV0ICsReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsReqAccepted.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsNonExist_Type = Counter64
_JnxMbgPgwGTPV0ICsNonExist_Object = MibScalar
jnxMbgPgwGTPV0ICsNonExist = _JnxMbgPgwGTPV0ICsNonExist_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 33),
    _JnxMbgPgwGTPV0ICsNonExist_Type()
)
jnxMbgPgwGTPV0ICsNonExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsNonExist.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsInvMsgFmt_Type = Counter64
_JnxMbgPgwGTPV0ICsInvMsgFmt_Object = MibScalar
jnxMbgPgwGTPV0ICsInvMsgFmt = _JnxMbgPgwGTPV0ICsInvMsgFmt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 34),
    _JnxMbgPgwGTPV0ICsInvMsgFmt_Type()
)
jnxMbgPgwGTPV0ICsInvMsgFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsInvMsgFmt.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsIMSINotKnown_Type = Counter64
_JnxMbgPgwGTPV0ICsIMSINotKnown_Object = MibScalar
jnxMbgPgwGTPV0ICsIMSINotKnown = _JnxMbgPgwGTPV0ICsIMSINotKnown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 35),
    _JnxMbgPgwGTPV0ICsIMSINotKnown_Type()
)
jnxMbgPgwGTPV0ICsIMSINotKnown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsIMSINotKnown.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsMSGRPSDetach_Type = Counter64
_JnxMbgPgwGTPV0ICsMSGRPSDetach_Object = MibScalar
jnxMbgPgwGTPV0ICsMSGRPSDetach = _JnxMbgPgwGTPV0ICsMSGRPSDetach_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 36),
    _JnxMbgPgwGTPV0ICsMSGRPSDetach_Type()
)
jnxMbgPgwGTPV0ICsMSGRPSDetach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsMSGRPSDetach.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsMSNotGRPSResp_Type = Counter64
_JnxMbgPgwGTPV0ICsMSNotGRPSResp_Object = MibScalar
jnxMbgPgwGTPV0ICsMSNotGRPSResp = _JnxMbgPgwGTPV0ICsMSNotGRPSResp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 37),
    _JnxMbgPgwGTPV0ICsMSNotGRPSResp_Type()
)
jnxMbgPgwGTPV0ICsMSNotGRPSResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsMSNotGRPSResp.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsMSRefuses_Type = Counter64
_JnxMbgPgwGTPV0ICsMSRefuses_Object = MibScalar
jnxMbgPgwGTPV0ICsMSRefuses = _JnxMbgPgwGTPV0ICsMSRefuses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 38),
    _JnxMbgPgwGTPV0ICsMSRefuses_Type()
)
jnxMbgPgwGTPV0ICsMSRefuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsMSRefuses.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsVerNotSupp_Type = Counter64
_JnxMbgPgwGTPV0ICsVerNotSupp_Object = MibScalar
jnxMbgPgwGTPV0ICsVerNotSupp = _JnxMbgPgwGTPV0ICsVerNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 39),
    _JnxMbgPgwGTPV0ICsVerNotSupp_Type()
)
jnxMbgPgwGTPV0ICsVerNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsVerNotSupp.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsNoRes_Type = Counter64
_JnxMbgPgwGTPV0ICsNoRes_Object = MibScalar
jnxMbgPgwGTPV0ICsNoRes = _JnxMbgPgwGTPV0ICsNoRes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 40),
    _JnxMbgPgwGTPV0ICsNoRes_Type()
)
jnxMbgPgwGTPV0ICsNoRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsNoRes.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsServNotSupp_Type = Counter64
_JnxMbgPgwGTPV0ICsServNotSupp_Object = MibScalar
jnxMbgPgwGTPV0ICsServNotSupp = _JnxMbgPgwGTPV0ICsServNotSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 41),
    _JnxMbgPgwGTPV0ICsServNotSupp_Type()
)
jnxMbgPgwGTPV0ICsServNotSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsServNotSupp.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsManIEIncrt_Type = Counter64
_JnxMbgPgwGTPV0ICsManIEIncrt_Object = MibScalar
jnxMbgPgwGTPV0ICsManIEIncrt = _JnxMbgPgwGTPV0ICsManIEIncrt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 42),
    _JnxMbgPgwGTPV0ICsManIEIncrt_Type()
)
jnxMbgPgwGTPV0ICsManIEIncrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsManIEIncrt.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsManIEMiss_Type = Counter64
_JnxMbgPgwGTPV0ICsManIEMiss_Object = MibScalar
jnxMbgPgwGTPV0ICsManIEMiss = _JnxMbgPgwGTPV0ICsManIEMiss_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 43),
    _JnxMbgPgwGTPV0ICsManIEMiss_Type()
)
jnxMbgPgwGTPV0ICsManIEMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsManIEMiss.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsOptIEIncrt_Type = Counter64
_JnxMbgPgwGTPV0ICsOptIEIncrt_Object = MibScalar
jnxMbgPgwGTPV0ICsOptIEIncrt = _JnxMbgPgwGTPV0ICsOptIEIncrt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 44),
    _JnxMbgPgwGTPV0ICsOptIEIncrt_Type()
)
jnxMbgPgwGTPV0ICsOptIEIncrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsOptIEIncrt.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsSysFail_Type = Counter64
_JnxMbgPgwGTPV0ICsSysFail_Object = MibScalar
jnxMbgPgwGTPV0ICsSysFail = _JnxMbgPgwGTPV0ICsSysFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 45),
    _JnxMbgPgwGTPV0ICsSysFail_Type()
)
jnxMbgPgwGTPV0ICsSysFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsSysFail.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsRoamRestrict_Type = Counter64
_JnxMbgPgwGTPV0ICsRoamRestrict_Object = MibScalar
jnxMbgPgwGTPV0ICsRoamRestrict = _JnxMbgPgwGTPV0ICsRoamRestrict_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 46),
    _JnxMbgPgwGTPV0ICsRoamRestrict_Type()
)
jnxMbgPgwGTPV0ICsRoamRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsRoamRestrict.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsPTMSISigMismatch_Type = Counter64
_JnxMbgPgwGTPV0ICsPTMSISigMismatch_Object = MibScalar
jnxMbgPgwGTPV0ICsPTMSISigMismatch = _JnxMbgPgwGTPV0ICsPTMSISigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 47),
    _JnxMbgPgwGTPV0ICsPTMSISigMismatch_Type()
)
jnxMbgPgwGTPV0ICsPTMSISigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsPTMSISigMismatch.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsGPRSConnSupp_Type = Counter64
_JnxMbgPgwGTPV0ICsGPRSConnSupp_Object = MibScalar
jnxMbgPgwGTPV0ICsGPRSConnSupp = _JnxMbgPgwGTPV0ICsGPRSConnSupp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 48),
    _JnxMbgPgwGTPV0ICsGPRSConnSupp_Type()
)
jnxMbgPgwGTPV0ICsGPRSConnSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsGPRSConnSupp.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsAuthFail_Type = Counter64
_JnxMbgPgwGTPV0ICsAuthFail_Object = MibScalar
jnxMbgPgwGTPV0ICsAuthFail = _JnxMbgPgwGTPV0ICsAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 49),
    _JnxMbgPgwGTPV0ICsAuthFail_Type()
)
jnxMbgPgwGTPV0ICsAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsAuthFail.setStatus("deprecated")
_JnxMbgPgwGTPV0ICsUserAuthFail_Type = Counter64
_JnxMbgPgwGTPV0ICsUserAuthFail_Object = MibScalar
jnxMbgPgwGTPV0ICsUserAuthFail = _JnxMbgPgwGTPV0ICsUserAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 50),
    _JnxMbgPgwGTPV0ICsUserAuthFail_Type()
)
jnxMbgPgwGTPV0ICsUserAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPV0ICsUserAuthFail.setStatus("deprecated")
_JnxMbgPgwV0NumMsgTx_Type = Counter64
_JnxMbgPgwV0NumMsgTx_Object = MibScalar
jnxMbgPgwV0NumMsgTx = _JnxMbgPgwV0NumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 51),
    _JnxMbgPgwV0NumMsgTx_Type()
)
jnxMbgPgwV0NumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NumMsgTx.setStatus("deprecated")
_JnxMbgPgwV0NumBytesTx_Type = Counter64
_JnxMbgPgwV0NumBytesTx_Object = MibScalar
jnxMbgPgwV0NumBytesTx = _JnxMbgPgwV0NumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 52),
    _JnxMbgPgwV0NumBytesTx_Type()
)
jnxMbgPgwV0NumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NumBytesTx.setStatus("deprecated")
_JnxMbgPgwV0EchoReqTx_Type = Counter64
_JnxMbgPgwV0EchoReqTx_Object = MibScalar
jnxMbgPgwV0EchoReqTx = _JnxMbgPgwV0EchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 53),
    _JnxMbgPgwV0EchoReqTx_Type()
)
jnxMbgPgwV0EchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0EchoReqTx.setStatus("deprecated")
_JnxMbgPgwV0EchoRespTx_Type = Counter64
_JnxMbgPgwV0EchoRespTx_Object = MibScalar
jnxMbgPgwV0EchoRespTx = _JnxMbgPgwV0EchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 54),
    _JnxMbgPgwV0EchoRespTx_Type()
)
jnxMbgPgwV0EchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0EchoRespTx.setStatus("deprecated")
_JnxMbgPgwV0CrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0CrtPdpCxtReqTx_Object = MibScalar
jnxMbgPgwV0CrtPdpCxtReqTx = _JnxMbgPgwV0CrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 55),
    _JnxMbgPgwV0CrtPdpCxtReqTx_Type()
)
jnxMbgPgwV0CrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwV0CrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0CrtPdpCxtRspTx_Object = MibScalar
jnxMbgPgwV0CrtPdpCxtRspTx = _JnxMbgPgwV0CrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 56),
    _JnxMbgPgwV0CrtPdpCxtRspTx_Type()
)
jnxMbgPgwV0CrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwV0UpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0UpdPdpCxtReqTx_Object = MibScalar
jnxMbgPgwV0UpdPdpCxtReqTx = _JnxMbgPgwV0UpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 57),
    _JnxMbgPgwV0UpdPdpCxtReqTx_Type()
)
jnxMbgPgwV0UpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0UpdPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwV0UpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0UpdPdpCxtRspTx_Object = MibScalar
jnxMbgPgwV0UpdPdpCxtRspTx = _JnxMbgPgwV0UpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 58),
    _JnxMbgPgwV0UpdPdpCxtRspTx_Type()
)
jnxMbgPgwV0UpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0UpdPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwV0DelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0DelPdpCxtReqTx_Object = MibScalar
jnxMbgPgwV0DelPdpCxtReqTx = _JnxMbgPgwV0DelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 59),
    _JnxMbgPgwV0DelPdpCxtReqTx_Type()
)
jnxMbgPgwV0DelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwV0DelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0DelPdpCxtRspTx_Object = MibScalar
jnxMbgPgwV0DelPdpCxtRspTx = _JnxMbgPgwV0DelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 60),
    _JnxMbgPgwV0DelPdpCxtRspTx_Type()
)
jnxMbgPgwV0DelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwV0CrtAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0CrtAAPdpCxtReqTx_Object = MibScalar
jnxMbgPgwV0CrtAAPdpCxtReqTx = _JnxMbgPgwV0CrtAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 61),
    _JnxMbgPgwV0CrtAAPdpCxtReqTx_Type()
)
jnxMbgPgwV0CrtAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtAAPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwV0CrtAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0CrtAAPdpCxtRspTx_Object = MibScalar
jnxMbgPgwV0CrtAAPdpCxtRspTx = _JnxMbgPgwV0CrtAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 62),
    _JnxMbgPgwV0CrtAAPdpCxtRspTx_Type()
)
jnxMbgPgwV0CrtAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0CrtAAPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwV0DelAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0DelAAPdpCxtReqTx_Object = MibScalar
jnxMbgPgwV0DelAAPdpCxtReqTx = _JnxMbgPgwV0DelAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 63),
    _JnxMbgPgwV0DelAAPdpCxtReqTx_Type()
)
jnxMbgPgwV0DelAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelAAPdpCxtReqTx.setStatus("deprecated")
_JnxMbgPgwV0DelAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0DelAAPdpCxtRspTx_Object = MibScalar
jnxMbgPgwV0DelAAPdpCxtRspTx = _JnxMbgPgwV0DelAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 64),
    _JnxMbgPgwV0DelAAPdpCxtRspTx_Type()
)
jnxMbgPgwV0DelAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0DelAAPdpCxtRspTx.setStatus("deprecated")
_JnxMbgPgwV0ErrorIndTx_Type = Counter64
_JnxMbgPgwV0ErrorIndTx_Object = MibScalar
jnxMbgPgwV0ErrorIndTx = _JnxMbgPgwV0ErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 65),
    _JnxMbgPgwV0ErrorIndTx_Type()
)
jnxMbgPgwV0ErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ErrorIndTx.setStatus("deprecated")
_JnxMbgPgwV0NotifReqTx_Type = Counter64
_JnxMbgPgwV0NotifReqTx_Object = MibScalar
jnxMbgPgwV0NotifReqTx = _JnxMbgPgwV0NotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 66),
    _JnxMbgPgwV0NotifReqTx_Type()
)
jnxMbgPgwV0NotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifReqTx.setStatus("deprecated")
_JnxMbgPgwV0NotifRspTx_Type = Counter64
_JnxMbgPgwV0NotifRspTx_Object = MibScalar
jnxMbgPgwV0NotifRspTx = _JnxMbgPgwV0NotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 67),
    _JnxMbgPgwV0NotifRspTx_Type()
)
jnxMbgPgwV0NotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifRspTx.setStatus("deprecated")
_JnxMbgPgwV0NotifRejReqTx_Type = Counter64
_JnxMbgPgwV0NotifRejReqTx_Object = MibScalar
jnxMbgPgwV0NotifRejReqTx = _JnxMbgPgwV0NotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 68),
    _JnxMbgPgwV0NotifRejReqTx_Type()
)
jnxMbgPgwV0NotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifRejReqTx.setStatus("deprecated")
_JnxMbgPgwV0NotifRejRspTx_Type = Counter64
_JnxMbgPgwV0NotifRejRspTx_Object = MibScalar
jnxMbgPgwV0NotifRejRspTx = _JnxMbgPgwV0NotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 69),
    _JnxMbgPgwV0NotifRejRspTx_Type()
)
jnxMbgPgwV0NotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotifRejRspTx.setStatus("deprecated")
_JnxMbgPgwV0RtInfReqTx_Type = Counter64
_JnxMbgPgwV0RtInfReqTx_Object = MibScalar
jnxMbgPgwV0RtInfReqTx = _JnxMbgPgwV0RtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 70),
    _JnxMbgPgwV0RtInfReqTx_Type()
)
jnxMbgPgwV0RtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0RtInfReqTx.setStatus("deprecated")
_JnxMbgPgwV0RtInfRspTx_Type = Counter64
_JnxMbgPgwV0RtInfRspTx_Object = MibScalar
jnxMbgPgwV0RtInfRspTx = _JnxMbgPgwV0RtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 71),
    _JnxMbgPgwV0RtInfRspTx_Type()
)
jnxMbgPgwV0RtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0RtInfRspTx.setStatus("deprecated")
_JnxMbgPgwV0FailRptReqTx_Type = Counter64
_JnxMbgPgwV0FailRptReqTx_Object = MibScalar
jnxMbgPgwV0FailRptReqTx = _JnxMbgPgwV0FailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 72),
    _JnxMbgPgwV0FailRptReqTx_Type()
)
jnxMbgPgwV0FailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0FailRptReqTx.setStatus("deprecated")
_JnxMbgPgwV0FailRptRspTx_Type = Counter64
_JnxMbgPgwV0FailRptRspTx_Object = MibScalar
jnxMbgPgwV0FailRptRspTx = _JnxMbgPgwV0FailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 73),
    _JnxMbgPgwV0FailRptRspTx_Type()
)
jnxMbgPgwV0FailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0FailRptRspTx.setStatus("deprecated")
_JnxMbgPgwV0NotMSPresReqTx_Type = Counter64
_JnxMbgPgwV0NotMSPresReqTx_Object = MibScalar
jnxMbgPgwV0NotMSPresReqTx = _JnxMbgPgwV0NotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 74),
    _JnxMbgPgwV0NotMSPresReqTx_Type()
)
jnxMbgPgwV0NotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotMSPresReqTx.setStatus("deprecated")
_JnxMbgPgwV0NotMSPresRspTx_Type = Counter64
_JnxMbgPgwV0NotMSPresRspTx_Object = MibScalar
jnxMbgPgwV0NotMSPresRspTx = _JnxMbgPgwV0NotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 8, 75),
    _JnxMbgPgwV0NotMSPresRspTx_Type()
)
jnxMbgPgwV0NotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0NotMSPresRspTx.setStatus("deprecated")
_JnxMbgPgwGtpCPerPeerStatsTable_Object = MibTable
jnxMbgPgwGtpCPerPeerStatsTable = _JnxMbgPgwGtpCPerPeerStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9)
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCPerPeerStatsTable.setStatus("current")
_JnxMbgPgwGtpPerPeerStatsEntry_Object = MibTableRow
jnxMbgPgwGtpPerPeerStatsEntry = _JnxMbgPgwGtpPerPeerStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1)
)
jnxMbgPgwGtpPerPeerStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwPPGtpRmtAddr"),
    (0, "JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwPPGtpLclAddr"),
    (0, "JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwPPGtpRtgInst"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPerPeerStatsEntry.setStatus("current")
_JnxMbgPgwPPGtpRmtAddr_Type = IpAddress
_JnxMbgPgwPPGtpRmtAddr_Object = MibTableColumn
jnxMbgPgwPPGtpRmtAddr = _JnxMbgPgwPPGtpRmtAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 1),
    _JnxMbgPgwPPGtpRmtAddr_Type()
)
jnxMbgPgwPPGtpRmtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpRmtAddr.setStatus("current")
_JnxMbgPgwPPGtpLclAddr_Type = IpAddress
_JnxMbgPgwPPGtpLclAddr_Object = MibTableColumn
jnxMbgPgwPPGtpLclAddr = _JnxMbgPgwPPGtpLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 2),
    _JnxMbgPgwPPGtpLclAddr_Type()
)
jnxMbgPgwPPGtpLclAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpLclAddr.setStatus("current")
_JnxMbgPgwPPGtpRtgInst_Type = Unsigned32
_JnxMbgPgwPPGtpRtgInst_Object = MibTableColumn
jnxMbgPgwPPGtpRtgInst = _JnxMbgPgwPPGtpRtgInst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 3),
    _JnxMbgPgwPPGtpRtgInst_Type()
)
jnxMbgPgwPPGtpRtgInst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpRtgInst.setStatus("current")
_JnxMbgPgwPPRxPacketsDropped_Type = Counter64
_JnxMbgPgwPPRxPacketsDropped_Object = MibTableColumn
jnxMbgPgwPPRxPacketsDropped = _JnxMbgPgwPPRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 4),
    _JnxMbgPgwPPRxPacketsDropped_Type()
)
jnxMbgPgwPPRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPRxPacketsDropped.setStatus("current")
_JnxMbgPgwPPPacketAllocFail_Type = Counter64
_JnxMbgPgwPPPacketAllocFail_Object = MibTableColumn
jnxMbgPgwPPPacketAllocFail = _JnxMbgPgwPPPacketAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 5),
    _JnxMbgPgwPPPacketAllocFail_Type()
)
jnxMbgPgwPPPacketAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPPacketAllocFail.setStatus("current")
_JnxMbgPgwPPPacketSendFail_Type = Counter64
_JnxMbgPgwPPPacketSendFail_Object = MibTableColumn
jnxMbgPgwPPPacketSendFail = _JnxMbgPgwPPPacketSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 6),
    _JnxMbgPgwPPPacketSendFail_Type()
)
jnxMbgPgwPPPacketSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPPacketSendFail.setStatus("current")
_JnxMbgPgwPPIPVerErrRx_Type = Counter64
_JnxMbgPgwPPIPVerErrRx_Object = MibTableColumn
jnxMbgPgwPPIPVerErrRx = _JnxMbgPgwPPIPVerErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 7),
    _JnxMbgPgwPPIPVerErrRx_Type()
)
jnxMbgPgwPPIPVerErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPIPVerErrRx.setStatus("current")
_JnxMbgPgwPPIPProtoErrRx_Type = Counter64
_JnxMbgPgwPPIPProtoErrRx_Object = MibTableColumn
jnxMbgPgwPPIPProtoErrRx = _JnxMbgPgwPPIPProtoErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 8),
    _JnxMbgPgwPPIPProtoErrRx_Type()
)
jnxMbgPgwPPIPProtoErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPIPProtoErrRx.setStatus("current")
_JnxMbgPgwPPGTPPortErrRx_Type = Counter64
_JnxMbgPgwPPGTPPortErrRx_Object = MibTableColumn
jnxMbgPgwPPGTPPortErrRx = _JnxMbgPgwPPGTPPortErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 9),
    _JnxMbgPgwPPGTPPortErrRx_Type()
)
jnxMbgPgwPPGTPPortErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGTPPortErrRx.setStatus("current")
_JnxMbgPgwPPGTPUnknVerRx_Type = Counter64
_JnxMbgPgwPPGTPUnknVerRx_Object = MibTableColumn
jnxMbgPgwPPGTPUnknVerRx = _JnxMbgPgwPPGTPUnknVerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 10),
    _JnxMbgPgwPPGTPUnknVerRx_Type()
)
jnxMbgPgwPPGTPUnknVerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGTPUnknVerRx.setStatus("current")
_JnxMbgPgwPPPcktLenErrRx_Type = Counter64
_JnxMbgPgwPPPcktLenErrRx_Object = MibTableColumn
jnxMbgPgwPPPcktLenErrRx = _JnxMbgPgwPPPcktLenErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 11),
    _JnxMbgPgwPPPcktLenErrRx_Type()
)
jnxMbgPgwPPPcktLenErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPPcktLenErrRx.setStatus("current")
_JnxMbgPgwPPUnknMsgRx_Type = Counter64
_JnxMbgPgwPPUnknMsgRx_Object = MibTableColumn
jnxMbgPgwPPUnknMsgRx = _JnxMbgPgwPPUnknMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 12),
    _JnxMbgPgwPPUnknMsgRx_Type()
)
jnxMbgPgwPPUnknMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPUnknMsgRx.setStatus("current")
_JnxMbgPgwPPProtocolErrRx_Type = Counter64
_JnxMbgPgwPPProtocolErrRx_Object = MibTableColumn
jnxMbgPgwPPProtocolErrRx = _JnxMbgPgwPPProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 13),
    _JnxMbgPgwPPProtocolErrRx_Type()
)
jnxMbgPgwPPProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPProtocolErrRx.setStatus("current")
_JnxMbgPgwPPV2UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwPPV2UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwPPV2UnSupportedMsgRx = _JnxMbgPgwPPV2UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 14),
    _JnxMbgPgwPPV2UnSupportedMsgRx_Type()
)
jnxMbgPgwPPV2UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwPPV2T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwPPV2T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwPPV2T3RespTmrExpRx = _JnxMbgPgwPPV2T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 15),
    _JnxMbgPgwPPV2T3RespTmrExpRx_Type()
)
jnxMbgPgwPPV2T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwPPV2GlbNumMsgRx_Type = Counter64
_JnxMbgPgwPPV2GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwPPV2GlbNumMsgRx = _JnxMbgPgwPPV2GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 16),
    _JnxMbgPgwPPV2GlbNumMsgRx_Type()
)
jnxMbgPgwPPV2GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbNumMsgRx.setStatus("current")
_JnxMbgPgwPPV2GlbNumMsgTx_Type = Counter64
_JnxMbgPgwPPV2GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwPPV2GlbNumMsgTx = _JnxMbgPgwPPV2GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 17),
    _JnxMbgPgwPPV2GlbNumMsgTx_Type()
)
jnxMbgPgwPPV2GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbNumMsgTx.setStatus("current")
_JnxMbgPgwPPV2GlbNumBytesRx_Type = Counter64
_JnxMbgPgwPPV2GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwPPV2GlbNumBytesRx = _JnxMbgPgwPPV2GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 18),
    _JnxMbgPgwPPV2GlbNumBytesRx_Type()
)
jnxMbgPgwPPV2GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbNumBytesRx.setStatus("current")
_JnxMbgPgwPPV2GlbNumBytesTx_Type = Counter64
_JnxMbgPgwPPV2GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwPPV2GlbNumBytesTx = _JnxMbgPgwPPV2GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 19),
    _JnxMbgPgwPPV2GlbNumBytesTx_Type()
)
jnxMbgPgwPPV2GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbNumBytesTx.setStatus("current")
_JnxMbgPgwPPV2GlbEchoReqRx_Type = Counter64
_JnxMbgPgwPPV2GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwPPV2GlbEchoReqRx = _JnxMbgPgwPPV2GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 20),
    _JnxMbgPgwPPV2GlbEchoReqRx_Type()
)
jnxMbgPgwPPV2GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbEchoReqRx.setStatus("current")
_JnxMbgPgwPPV2GlbEchoReqTx_Type = Counter64
_JnxMbgPgwPPV2GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwPPV2GlbEchoReqTx = _JnxMbgPgwPPV2GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 21),
    _JnxMbgPgwPPV2GlbEchoReqTx_Type()
)
jnxMbgPgwPPV2GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbEchoReqTx.setStatus("current")
_JnxMbgPgwPPV2GlbEchoRespRx_Type = Counter64
_JnxMbgPgwPPV2GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwPPV2GlbEchoRespRx = _JnxMbgPgwPPV2GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 22),
    _JnxMbgPgwPPV2GlbEchoRespRx_Type()
)
jnxMbgPgwPPV2GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbEchoRespRx.setStatus("current")
_JnxMbgPgwPPV2GlbEchoRespTx_Type = Counter64
_JnxMbgPgwPPV2GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwPPV2GlbEchoRespTx = _JnxMbgPgwPPV2GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 23),
    _JnxMbgPgwPPV2GlbEchoRespTx_Type()
)
jnxMbgPgwPPV2GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2GlbEchoRespTx.setStatus("current")
_JnxMbgPgwPPV2VerNotSupRx_Type = Counter64
_JnxMbgPgwPPV2VerNotSupRx_Object = MibTableColumn
jnxMbgPgwPPV2VerNotSupRx = _JnxMbgPgwPPV2VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 24),
    _JnxMbgPgwPPV2VerNotSupRx_Type()
)
jnxMbgPgwPPV2VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2VerNotSupRx.setStatus("current")
_JnxMbgPgwPPV2VerNotSupTx_Type = Counter64
_JnxMbgPgwPPV2VerNotSupTx_Object = MibTableColumn
jnxMbgPgwPPV2VerNotSupTx = _JnxMbgPgwPPV2VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 25),
    _JnxMbgPgwPPV2VerNotSupTx_Type()
)
jnxMbgPgwPPV2VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2VerNotSupTx.setStatus("current")
_JnxMbgPgwPPV2CreateSessReqRx_Type = Counter64
_JnxMbgPgwPPV2CreateSessReqRx_Object = MibTableColumn
jnxMbgPgwPPV2CreateSessReqRx = _JnxMbgPgwPPV2CreateSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 26),
    _JnxMbgPgwPPV2CreateSessReqRx_Type()
)
jnxMbgPgwPPV2CreateSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CreateSessReqRx.setStatus("current")
_JnxMbgPgwPPV2CreateSessReqTx_Type = Counter64
_JnxMbgPgwPPV2CreateSessReqTx_Object = MibTableColumn
jnxMbgPgwPPV2CreateSessReqTx = _JnxMbgPgwPPV2CreateSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 27),
    _JnxMbgPgwPPV2CreateSessReqTx_Type()
)
jnxMbgPgwPPV2CreateSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CreateSessReqTx.setStatus("current")
_JnxMbgPgwPPV2CreateSessRspRx_Type = Counter64
_JnxMbgPgwPPV2CreateSessRspRx_Object = MibTableColumn
jnxMbgPgwPPV2CreateSessRspRx = _JnxMbgPgwPPV2CreateSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 28),
    _JnxMbgPgwPPV2CreateSessRspRx_Type()
)
jnxMbgPgwPPV2CreateSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CreateSessRspRx.setStatus("current")
_JnxMbgPgwPPV2CreateSessRspTx_Type = Counter64
_JnxMbgPgwPPV2CreateSessRspTx_Object = MibTableColumn
jnxMbgPgwPPV2CreateSessRspTx = _JnxMbgPgwPPV2CreateSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 29),
    _JnxMbgPgwPPV2CreateSessRspTx_Type()
)
jnxMbgPgwPPV2CreateSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CreateSessRspTx.setStatus("current")
_JnxMbgPgwPPV2ModBrReqRx_Type = Counter64
_JnxMbgPgwPPV2ModBrReqRx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrReqRx = _JnxMbgPgwPPV2ModBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 30),
    _JnxMbgPgwPPV2ModBrReqRx_Type()
)
jnxMbgPgwPPV2ModBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrReqRx.setStatus("current")
_JnxMbgPgwPPV2ModBrReqTx_Type = Counter64
_JnxMbgPgwPPV2ModBrReqTx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrReqTx = _JnxMbgPgwPPV2ModBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 31),
    _JnxMbgPgwPPV2ModBrReqTx_Type()
)
jnxMbgPgwPPV2ModBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrReqTx.setStatus("current")
_JnxMbgPgwPPV2ModBrRspRx_Type = Counter64
_JnxMbgPgwPPV2ModBrRspRx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrRspRx = _JnxMbgPgwPPV2ModBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 32),
    _JnxMbgPgwPPV2ModBrRspRx_Type()
)
jnxMbgPgwPPV2ModBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrRspRx.setStatus("current")
_JnxMbgPgwPPV2ModBrRspTx_Type = Counter64
_JnxMbgPgwPPV2ModBrRspTx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrRspTx = _JnxMbgPgwPPV2ModBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 33),
    _JnxMbgPgwPPV2ModBrRspTx_Type()
)
jnxMbgPgwPPV2ModBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrRspTx.setStatus("current")
_JnxMbgPgwPPV2DelSessReqRx_Type = Counter64
_JnxMbgPgwPPV2DelSessReqRx_Object = MibTableColumn
jnxMbgPgwPPV2DelSessReqRx = _JnxMbgPgwPPV2DelSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 34),
    _JnxMbgPgwPPV2DelSessReqRx_Type()
)
jnxMbgPgwPPV2DelSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelSessReqRx.setStatus("current")
_JnxMbgPgwPPV2DelSessReqTx_Type = Counter64
_JnxMbgPgwPPV2DelSessReqTx_Object = MibTableColumn
jnxMbgPgwPPV2DelSessReqTx = _JnxMbgPgwPPV2DelSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 35),
    _JnxMbgPgwPPV2DelSessReqTx_Type()
)
jnxMbgPgwPPV2DelSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelSessReqTx.setStatus("current")
_JnxMbgPgwPPV2DelSessRspRx_Type = Counter64
_JnxMbgPgwPPV2DelSessRspRx_Object = MibTableColumn
jnxMbgPgwPPV2DelSessRspRx = _JnxMbgPgwPPV2DelSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 36),
    _JnxMbgPgwPPV2DelSessRspRx_Type()
)
jnxMbgPgwPPV2DelSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelSessRspRx.setStatus("current")
_JnxMbgPgwPPV2DelSessRspTx_Type = Counter64
_JnxMbgPgwPPV2DelSessRspTx_Object = MibTableColumn
jnxMbgPgwPPV2DelSessRspTx = _JnxMbgPgwPPV2DelSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 37),
    _JnxMbgPgwPPV2DelSessRspTx_Type()
)
jnxMbgPgwPPV2DelSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelSessRspTx.setStatus("current")
_JnxMbgPgwPPV2CrtBrReqRx_Type = Counter64
_JnxMbgPgwPPV2CrtBrReqRx_Object = MibTableColumn
jnxMbgPgwPPV2CrtBrReqRx = _JnxMbgPgwPPV2CrtBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 38),
    _JnxMbgPgwPPV2CrtBrReqRx_Type()
)
jnxMbgPgwPPV2CrtBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrtBrReqRx.setStatus("current")
_JnxMbgPgwPPV2CrtBrReqTx_Type = Counter64
_JnxMbgPgwPPV2CrtBrReqTx_Object = MibTableColumn
jnxMbgPgwPPV2CrtBrReqTx = _JnxMbgPgwPPV2CrtBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 39),
    _JnxMbgPgwPPV2CrtBrReqTx_Type()
)
jnxMbgPgwPPV2CrtBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrtBrReqTx.setStatus("current")
_JnxMbgPgwPPV2CrtBrRspRx_Type = Counter64
_JnxMbgPgwPPV2CrtBrRspRx_Object = MibTableColumn
jnxMbgPgwPPV2CrtBrRspRx = _JnxMbgPgwPPV2CrtBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 40),
    _JnxMbgPgwPPV2CrtBrRspRx_Type()
)
jnxMbgPgwPPV2CrtBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrtBrRspRx.setStatus("current")
_JnxMbgPgwPPV2CrtBrRspTx_Type = Counter64
_JnxMbgPgwPPV2CrtBrRspTx_Object = MibTableColumn
jnxMbgPgwPPV2CrtBrRspTx = _JnxMbgPgwPPV2CrtBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 41),
    _JnxMbgPgwPPV2CrtBrRspTx_Type()
)
jnxMbgPgwPPV2CrtBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrtBrRspTx.setStatus("current")
_JnxMbgPgwPPV2UpdBrReqRx_Type = Counter64
_JnxMbgPgwPPV2UpdBrReqRx_Object = MibTableColumn
jnxMbgPgwPPV2UpdBrReqRx = _JnxMbgPgwPPV2UpdBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 42),
    _JnxMbgPgwPPV2UpdBrReqRx_Type()
)
jnxMbgPgwPPV2UpdBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdBrReqRx.setStatus("current")
_JnxMbgPgwPPV2UpdBrReqTx_Type = Counter64
_JnxMbgPgwPPV2UpdBrReqTx_Object = MibTableColumn
jnxMbgPgwPPV2UpdBrReqTx = _JnxMbgPgwPPV2UpdBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 43),
    _JnxMbgPgwPPV2UpdBrReqTx_Type()
)
jnxMbgPgwPPV2UpdBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdBrReqTx.setStatus("current")
_JnxMbgPgwPPV2UpdBrRspRx_Type = Counter64
_JnxMbgPgwPPV2UpdBrRspRx_Object = MibTableColumn
jnxMbgPgwPPV2UpdBrRspRx = _JnxMbgPgwPPV2UpdBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 44),
    _JnxMbgPgwPPV2UpdBrRspRx_Type()
)
jnxMbgPgwPPV2UpdBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdBrRspRx.setStatus("current")
_JnxMbgPgwPPV2UpdBrRspTx_Type = Counter64
_JnxMbgPgwPPV2UpdBrRspTx_Object = MibTableColumn
jnxMbgPgwPPV2UpdBrRspTx = _JnxMbgPgwPPV2UpdBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 45),
    _JnxMbgPgwPPV2UpdBrRspTx_Type()
)
jnxMbgPgwPPV2UpdBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdBrRspTx.setStatus("current")
_JnxMbgPgwPPV2DelBrReqRx_Type = Counter64
_JnxMbgPgwPPV2DelBrReqRx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrReqRx = _JnxMbgPgwPPV2DelBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 46),
    _JnxMbgPgwPPV2DelBrReqRx_Type()
)
jnxMbgPgwPPV2DelBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrReqRx.setStatus("current")
_JnxMbgPgwPPV2DelBrReqTx_Type = Counter64
_JnxMbgPgwPPV2DelBrReqTx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrReqTx = _JnxMbgPgwPPV2DelBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 47),
    _JnxMbgPgwPPV2DelBrReqTx_Type()
)
jnxMbgPgwPPV2DelBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrReqTx.setStatus("current")
_JnxMbgPgwPPV2DelBrRspRx_Type = Counter64
_JnxMbgPgwPPV2DelBrRspRx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrRspRx = _JnxMbgPgwPPV2DelBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 48),
    _JnxMbgPgwPPV2DelBrRspRx_Type()
)
jnxMbgPgwPPV2DelBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrRspRx.setStatus("current")
_JnxMbgPgwPPV2DelBrRspTx_Type = Counter64
_JnxMbgPgwPPV2DelBrRspTx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrRspTx = _JnxMbgPgwPPV2DelBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 49),
    _JnxMbgPgwPPV2DelBrRspTx_Type()
)
jnxMbgPgwPPV2DelBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrRspTx.setStatus("current")
_JnxMbgPgwPPV2DelConnSetReqRx_Type = Counter64
_JnxMbgPgwPPV2DelConnSetReqRx_Object = MibTableColumn
jnxMbgPgwPPV2DelConnSetReqRx = _JnxMbgPgwPPV2DelConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 50),
    _JnxMbgPgwPPV2DelConnSetReqRx_Type()
)
jnxMbgPgwPPV2DelConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelConnSetReqRx.setStatus("current")
_JnxMbgPgwPPV2DelConnSetReqTx_Type = Counter64
_JnxMbgPgwPPV2DelConnSetReqTx_Object = MibTableColumn
jnxMbgPgwPPV2DelConnSetReqTx = _JnxMbgPgwPPV2DelConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 51),
    _JnxMbgPgwPPV2DelConnSetReqTx_Type()
)
jnxMbgPgwPPV2DelConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelConnSetReqTx.setStatus("current")
_JnxMbgPgwPPV2DelConnSetRspRx_Type = Counter64
_JnxMbgPgwPPV2DelConnSetRspRx_Object = MibTableColumn
jnxMbgPgwPPV2DelConnSetRspRx = _JnxMbgPgwPPV2DelConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 52),
    _JnxMbgPgwPPV2DelConnSetRspRx_Type()
)
jnxMbgPgwPPV2DelConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelConnSetRspRx.setStatus("current")
_JnxMbgPgwPPV2DelConnSetRspTx_Type = Counter64
_JnxMbgPgwPPV2DelConnSetRspTx_Object = MibTableColumn
jnxMbgPgwPPV2DelConnSetRspTx = _JnxMbgPgwPPV2DelConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 53),
    _JnxMbgPgwPPV2DelConnSetRspTx_Type()
)
jnxMbgPgwPPV2DelConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelConnSetRspTx.setStatus("current")
_JnxMbgPgwPPV2UpdConnSetReqRx_Type = Counter64
_JnxMbgPgwPPV2UpdConnSetReqRx_Object = MibTableColumn
jnxMbgPgwPPV2UpdConnSetReqRx = _JnxMbgPgwPPV2UpdConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 54),
    _JnxMbgPgwPPV2UpdConnSetReqRx_Type()
)
jnxMbgPgwPPV2UpdConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdConnSetReqRx.setStatus("current")
_JnxMbgPgwPPV2UpdConnSetReqTx_Type = Counter64
_JnxMbgPgwPPV2UpdConnSetReqTx_Object = MibTableColumn
jnxMbgPgwPPV2UpdConnSetReqTx = _JnxMbgPgwPPV2UpdConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 55),
    _JnxMbgPgwPPV2UpdConnSetReqTx_Type()
)
jnxMbgPgwPPV2UpdConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdConnSetReqTx.setStatus("current")
_JnxMbgPgwPPV2UpdConnSetRspRx_Type = Counter64
_JnxMbgPgwPPV2UpdConnSetRspRx_Object = MibTableColumn
jnxMbgPgwPPV2UpdConnSetRspRx = _JnxMbgPgwPPV2UpdConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 56),
    _JnxMbgPgwPPV2UpdConnSetRspRx_Type()
)
jnxMbgPgwPPV2UpdConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdConnSetRspRx.setStatus("current")
_JnxMbgPgwPPV2UpdConnSetRspTx_Type = Counter64
_JnxMbgPgwPPV2UpdConnSetRspTx_Object = MibTableColumn
jnxMbgPgwPPV2UpdConnSetRspTx = _JnxMbgPgwPPV2UpdConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 57),
    _JnxMbgPgwPPV2UpdConnSetRspTx_Type()
)
jnxMbgPgwPPV2UpdConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2UpdConnSetRspTx.setStatus("current")
_JnxMbgPgwPPV2ModBrCmdRx_Type = Counter64
_JnxMbgPgwPPV2ModBrCmdRx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrCmdRx = _JnxMbgPgwPPV2ModBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 58),
    _JnxMbgPgwPPV2ModBrCmdRx_Type()
)
jnxMbgPgwPPV2ModBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrCmdRx.setStatus("current")
_JnxMbgPgwPPV2ModBrCmdTx_Type = Counter64
_JnxMbgPgwPPV2ModBrCmdTx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrCmdTx = _JnxMbgPgwPPV2ModBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 59),
    _JnxMbgPgwPPV2ModBrCmdTx_Type()
)
jnxMbgPgwPPV2ModBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrCmdTx.setStatus("current")
_JnxMbgPgwPPV2ModBrFlrIndRx_Type = Counter64
_JnxMbgPgwPPV2ModBrFlrIndRx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrFlrIndRx = _JnxMbgPgwPPV2ModBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 60),
    _JnxMbgPgwPPV2ModBrFlrIndRx_Type()
)
jnxMbgPgwPPV2ModBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrFlrIndRx.setStatus("current")
_JnxMbgPgwPPV2ModBrFlrIndTx_Type = Counter64
_JnxMbgPgwPPV2ModBrFlrIndTx_Object = MibTableColumn
jnxMbgPgwPPV2ModBrFlrIndTx = _JnxMbgPgwPPV2ModBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 61),
    _JnxMbgPgwPPV2ModBrFlrIndTx_Type()
)
jnxMbgPgwPPV2ModBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ModBrFlrIndTx.setStatus("current")
_JnxMbgPgwPPV2DelBrCmdRx_Type = Counter64
_JnxMbgPgwPPV2DelBrCmdRx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrCmdRx = _JnxMbgPgwPPV2DelBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 62),
    _JnxMbgPgwPPV2DelBrCmdRx_Type()
)
jnxMbgPgwPPV2DelBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrCmdRx.setStatus("current")
_JnxMbgPgwPPV2DelBrCmdTx_Type = Counter64
_JnxMbgPgwPPV2DelBrCmdTx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrCmdTx = _JnxMbgPgwPPV2DelBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 63),
    _JnxMbgPgwPPV2DelBrCmdTx_Type()
)
jnxMbgPgwPPV2DelBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrCmdTx.setStatus("current")
_JnxMbgPgwPPV2DelBrFlrIndRx_Type = Counter64
_JnxMbgPgwPPV2DelBrFlrIndRx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrFlrIndRx = _JnxMbgPgwPPV2DelBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 64),
    _JnxMbgPgwPPV2DelBrFlrIndRx_Type()
)
jnxMbgPgwPPV2DelBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrFlrIndRx.setStatus("current")
_JnxMbgPgwPPV2DelBrFlrIndTx_Type = Counter64
_JnxMbgPgwPPV2DelBrFlrIndTx_Object = MibTableColumn
jnxMbgPgwPPV2DelBrFlrIndTx = _JnxMbgPgwPPV2DelBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 65),
    _JnxMbgPgwPPV2DelBrFlrIndTx_Type()
)
jnxMbgPgwPPV2DelBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelBrFlrIndTx.setStatus("current")
_JnxMbgPgwPPV2BrResCmdRx_Type = Counter64
_JnxMbgPgwPPV2BrResCmdRx_Object = MibTableColumn
jnxMbgPgwPPV2BrResCmdRx = _JnxMbgPgwPPV2BrResCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 66),
    _JnxMbgPgwPPV2BrResCmdRx_Type()
)
jnxMbgPgwPPV2BrResCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2BrResCmdRx.setStatus("current")
_JnxMbgPgwPPV2BrResCmdTx_Type = Counter64
_JnxMbgPgwPPV2BrResCmdTx_Object = MibTableColumn
jnxMbgPgwPPV2BrResCmdTx = _JnxMbgPgwPPV2BrResCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 67),
    _JnxMbgPgwPPV2BrResCmdTx_Type()
)
jnxMbgPgwPPV2BrResCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2BrResCmdTx.setStatus("current")
_JnxMbgPgwPPV2BrResFlrIndRx_Type = Counter64
_JnxMbgPgwPPV2BrResFlrIndRx_Object = MibTableColumn
jnxMbgPgwPPV2BrResFlrIndRx = _JnxMbgPgwPPV2BrResFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 68),
    _JnxMbgPgwPPV2BrResFlrIndRx_Type()
)
jnxMbgPgwPPV2BrResFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2BrResFlrIndRx.setStatus("current")
_JnxMbgPgwPPV2BrResFlrIndTx_Type = Counter64
_JnxMbgPgwPPV2BrResFlrIndTx_Object = MibTableColumn
jnxMbgPgwPPV2BrResFlrIndTx = _JnxMbgPgwPPV2BrResFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 69),
    _JnxMbgPgwPPV2BrResFlrIndTx_Type()
)
jnxMbgPgwPPV2BrResFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2BrResFlrIndTx.setStatus("current")
_JnxMbgPgwPPV2RelAcsBrReqRx_Type = Counter64
_JnxMbgPgwPPV2RelAcsBrReqRx_Object = MibTableColumn
jnxMbgPgwPPV2RelAcsBrReqRx = _JnxMbgPgwPPV2RelAcsBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 70),
    _JnxMbgPgwPPV2RelAcsBrReqRx_Type()
)
jnxMbgPgwPPV2RelAcsBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2RelAcsBrReqRx.setStatus("obsolete")
_JnxMbgPgwPPV2RelAcsBrReqTx_Type = Counter64
_JnxMbgPgwPPV2RelAcsBrReqTx_Object = MibTableColumn
jnxMbgPgwPPV2RelAcsBrReqTx = _JnxMbgPgwPPV2RelAcsBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 71),
    _JnxMbgPgwPPV2RelAcsBrReqTx_Type()
)
jnxMbgPgwPPV2RelAcsBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2RelAcsBrReqTx.setStatus("obsolete")
_JnxMbgPgwPPV2RelAcsBrRespRx_Type = Counter64
_JnxMbgPgwPPV2RelAcsBrRespRx_Object = MibTableColumn
jnxMbgPgwPPV2RelAcsBrRespRx = _JnxMbgPgwPPV2RelAcsBrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 72),
    _JnxMbgPgwPPV2RelAcsBrRespRx_Type()
)
jnxMbgPgwPPV2RelAcsBrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2RelAcsBrRespRx.setStatus("obsolete")
_JnxMbgPgwPPV2RelAcsBrRespTx_Type = Counter64
_JnxMbgPgwPPV2RelAcsBrRespTx_Object = MibTableColumn
jnxMbgPgwPPV2RelAcsBrRespTx = _JnxMbgPgwPPV2RelAcsBrRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 73),
    _JnxMbgPgwPPV2RelAcsBrRespTx_Type()
)
jnxMbgPgwPPV2RelAcsBrRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2RelAcsBrRespTx.setStatus("obsolete")
_JnxMbgPgwPPV2CrIndTunReqRx_Type = Counter64
_JnxMbgPgwPPV2CrIndTunReqRx_Object = MibTableColumn
jnxMbgPgwPPV2CrIndTunReqRx = _JnxMbgPgwPPV2CrIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 74),
    _JnxMbgPgwPPV2CrIndTunReqRx_Type()
)
jnxMbgPgwPPV2CrIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrIndTunReqRx.setStatus("obsolete")
_JnxMbgPgwPPV2CrIndTunReqTx_Type = Counter64
_JnxMbgPgwPPV2CrIndTunReqTx_Object = MibTableColumn
jnxMbgPgwPPV2CrIndTunReqTx = _JnxMbgPgwPPV2CrIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 75),
    _JnxMbgPgwPPV2CrIndTunReqTx_Type()
)
jnxMbgPgwPPV2CrIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrIndTunReqTx.setStatus("obsolete")
_JnxMbgPgwPPV2CrIndTunRespRx_Type = Counter64
_JnxMbgPgwPPV2CrIndTunRespRx_Object = MibTableColumn
jnxMbgPgwPPV2CrIndTunRespRx = _JnxMbgPgwPPV2CrIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 76),
    _JnxMbgPgwPPV2CrIndTunRespRx_Type()
)
jnxMbgPgwPPV2CrIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrIndTunRespRx.setStatus("obsolete")
_JnxMbgPgwPPV2CrIndTunRespTx_Type = Counter64
_JnxMbgPgwPPV2CrIndTunRespTx_Object = MibTableColumn
jnxMbgPgwPPV2CrIndTunRespTx = _JnxMbgPgwPPV2CrIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 77),
    _JnxMbgPgwPPV2CrIndTunRespTx_Type()
)
jnxMbgPgwPPV2CrIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2CrIndTunRespTx.setStatus("obsolete")
_JnxMbgPgwPPV2DelIndTunReqRx_Type = Counter64
_JnxMbgPgwPPV2DelIndTunReqRx_Object = MibTableColumn
jnxMbgPgwPPV2DelIndTunReqRx = _JnxMbgPgwPPV2DelIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 78),
    _JnxMbgPgwPPV2DelIndTunReqRx_Type()
)
jnxMbgPgwPPV2DelIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelIndTunReqRx.setStatus("obsolete")
_JnxMbgPgwPPV2DelIndTunReqTx_Type = Counter64
_JnxMbgPgwPPV2DelIndTunReqTx_Object = MibTableColumn
jnxMbgPgwPPV2DelIndTunReqTx = _JnxMbgPgwPPV2DelIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 79),
    _JnxMbgPgwPPV2DelIndTunReqTx_Type()
)
jnxMbgPgwPPV2DelIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelIndTunReqTx.setStatus("obsolete")
_JnxMbgPgwPPV2DelIndTunRespRx_Type = Counter64
_JnxMbgPgwPPV2DelIndTunRespRx_Object = MibTableColumn
jnxMbgPgwPPV2DelIndTunRespRx = _JnxMbgPgwPPV2DelIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 80),
    _JnxMbgPgwPPV2DelIndTunRespRx_Type()
)
jnxMbgPgwPPV2DelIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelIndTunRespRx.setStatus("obsolete")
_JnxMbgPgwPPV2DelIndTunRespTx_Type = Counter64
_JnxMbgPgwPPV2DelIndTunRespTx_Object = MibTableColumn
jnxMbgPgwPPV2DelIndTunRespTx = _JnxMbgPgwPPV2DelIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 81),
    _JnxMbgPgwPPV2DelIndTunRespTx_Type()
)
jnxMbgPgwPPV2DelIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DelIndTunRespTx.setStatus("obsolete")
_JnxMbgPgwPPV2DlDataNotifRx_Type = Counter64
_JnxMbgPgwPPV2DlDataNotifRx_Object = MibTableColumn
jnxMbgPgwPPV2DlDataNotifRx = _JnxMbgPgwPPV2DlDataNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 82),
    _JnxMbgPgwPPV2DlDataNotifRx_Type()
)
jnxMbgPgwPPV2DlDataNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DlDataNotifRx.setStatus("obsolete")
_JnxMbgPgwPPV2DlDataNotifTx_Type = Counter64
_JnxMbgPgwPPV2DlDataNotifTx_Object = MibTableColumn
jnxMbgPgwPPV2DlDataNotifTx = _JnxMbgPgwPPV2DlDataNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 83),
    _JnxMbgPgwPPV2DlDataNotifTx_Type()
)
jnxMbgPgwPPV2DlDataNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DlDataNotifTx.setStatus("obsolete")
_JnxMbgPgwPPV2DlDataAckRx_Type = Counter64
_JnxMbgPgwPPV2DlDataAckRx_Object = MibTableColumn
jnxMbgPgwPPV2DlDataAckRx = _JnxMbgPgwPPV2DlDataAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 84),
    _JnxMbgPgwPPV2DlDataAckRx_Type()
)
jnxMbgPgwPPV2DlDataAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DlDataAckRx.setStatus("obsolete")
_JnxMbgPgwPPV2DlDataAckTx_Type = Counter64
_JnxMbgPgwPPV2DlDataAckTx_Object = MibTableColumn
jnxMbgPgwPPV2DlDataAckTx = _JnxMbgPgwPPV2DlDataAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 85),
    _JnxMbgPgwPPV2DlDataAckTx_Type()
)
jnxMbgPgwPPV2DlDataAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DlDataAckTx.setStatus("obsolete")
_JnxMbgPgwPPV2DlDataNotiFlrIndRx_Type = Counter64
_JnxMbgPgwPPV2DlDataNotiFlrIndRx_Object = MibTableColumn
jnxMbgPgwPPV2DlDataNotiFlrIndRx = _JnxMbgPgwPPV2DlDataNotiFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 86),
    _JnxMbgPgwPPV2DlDataNotiFlrIndRx_Type()
)
jnxMbgPgwPPV2DlDataNotiFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DlDataNotiFlrIndRx.setStatus("obsolete")
_JnxMbgPgwPPV2DlDataNotiFlrIndTx_Type = Counter64
_JnxMbgPgwPPV2DlDataNotiFlrIndTx_Object = MibTableColumn
jnxMbgPgwPPV2DlDataNotiFlrIndTx = _JnxMbgPgwPPV2DlDataNotiFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 87),
    _JnxMbgPgwPPV2DlDataNotiFlrIndTx_Type()
)
jnxMbgPgwPPV2DlDataNotiFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2DlDataNotiFlrIndTx.setStatus("obsolete")
_JnxMbgPgwPPV2StopPagingIndRx_Type = Counter64
_JnxMbgPgwPPV2StopPagingIndRx_Object = MibTableColumn
jnxMbgPgwPPV2StopPagingIndRx = _JnxMbgPgwPPV2StopPagingIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 88),
    _JnxMbgPgwPPV2StopPagingIndRx_Type()
)
jnxMbgPgwPPV2StopPagingIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2StopPagingIndRx.setStatus("obsolete")
_JnxMbgPgwPPV2StopPagingIndTx_Type = Counter64
_JnxMbgPgwPPV2StopPagingIndTx_Object = MibTableColumn
jnxMbgPgwPPV2StopPagingIndTx = _JnxMbgPgwPPV2StopPagingIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 89),
    _JnxMbgPgwPPV2StopPagingIndTx_Type()
)
jnxMbgPgwPPV2StopPagingIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2StopPagingIndTx.setStatus("obsolete")
_JnxMbgPgwPPV2ICsPageRx_Type = Counter64
_JnxMbgPgwPPV2ICsPageRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPageRx = _JnxMbgPgwPPV2ICsPageRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 90),
    _JnxMbgPgwPPV2ICsPageRx_Type()
)
jnxMbgPgwPPV2ICsPageRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPageRx.setStatus("obsolete")
_JnxMbgPgwPPV2ICsPageTx_Type = Counter64
_JnxMbgPgwPPV2ICsPageTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPageTx = _JnxMbgPgwPPV2ICsPageTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 91),
    _JnxMbgPgwPPV2ICsPageTx_Type()
)
jnxMbgPgwPPV2ICsPageTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPageTx.setStatus("obsolete")
_JnxMbgPgwPPV2ICsReqAcceptRx_Type = Counter64
_JnxMbgPgwPPV2ICsReqAcceptRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsReqAcceptRx = _JnxMbgPgwPPV2ICsReqAcceptRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 92),
    _JnxMbgPgwPPV2ICsReqAcceptRx_Type()
)
jnxMbgPgwPPV2ICsReqAcceptRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsReqAcceptRx.setStatus("current")
_JnxMbgPgwPPV2ICsReqAcceptTx_Type = Counter64
_JnxMbgPgwPPV2ICsReqAcceptTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsReqAcceptTx = _JnxMbgPgwPPV2ICsReqAcceptTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 93),
    _JnxMbgPgwPPV2ICsReqAcceptTx_Type()
)
jnxMbgPgwPPV2ICsReqAcceptTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsReqAcceptTx.setStatus("current")
_JnxMbgPgwPPV2ICsAcceptPartRx_Type = Counter64
_JnxMbgPgwPPV2ICsAcceptPartRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAcceptPartRx = _JnxMbgPgwPPV2ICsAcceptPartRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 94),
    _JnxMbgPgwPPV2ICsAcceptPartRx_Type()
)
jnxMbgPgwPPV2ICsAcceptPartRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAcceptPartRx.setStatus("current")
_JnxMbgPgwPPV2ICsAcceptPartTx_Type = Counter64
_JnxMbgPgwPPV2ICsAcceptPartTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAcceptPartTx = _JnxMbgPgwPPV2ICsAcceptPartTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 95),
    _JnxMbgPgwPPV2ICsAcceptPartTx_Type()
)
jnxMbgPgwPPV2ICsAcceptPartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAcceptPartTx.setStatus("current")
_JnxMbgPgwPPV2ICsNewPTNPrefRx_Type = Counter64
_JnxMbgPgwPPV2ICsNewPTNPrefRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNewPTNPrefRx = _JnxMbgPgwPPV2ICsNewPTNPrefRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 96),
    _JnxMbgPgwPPV2ICsNewPTNPrefRx_Type()
)
jnxMbgPgwPPV2ICsNewPTNPrefRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNewPTNPrefRx.setStatus("current")
_JnxMbgPgwPPV2ICsNewPTNPrefTx_Type = Counter64
_JnxMbgPgwPPV2ICsNewPTNPrefTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNewPTNPrefTx = _JnxMbgPgwPPV2ICsNewPTNPrefTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 97),
    _JnxMbgPgwPPV2ICsNewPTNPrefTx_Type()
)
jnxMbgPgwPPV2ICsNewPTNPrefTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNewPTNPrefTx.setStatus("current")
_JnxMbgPgwPPV2ICsNewPTSIAdbrRx_Type = Counter64
_JnxMbgPgwPPV2ICsNewPTSIAdbrRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNewPTSIAdbrRx = _JnxMbgPgwPPV2ICsNewPTSIAdbrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 98),
    _JnxMbgPgwPPV2ICsNewPTSIAdbrRx_Type()
)
jnxMbgPgwPPV2ICsNewPTSIAdbrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNewPTSIAdbrRx.setStatus("current")
_JnxMbgPgwPPV2ICsNewPTSIAdbrTx_Type = Counter64
_JnxMbgPgwPPV2ICsNewPTSIAdbrTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNewPTSIAdbrTx = _JnxMbgPgwPPV2ICsNewPTSIAdbrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 99),
    _JnxMbgPgwPPV2ICsNewPTSIAdbrTx_Type()
)
jnxMbgPgwPPV2ICsNewPTSIAdbrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNewPTSIAdbrTx.setStatus("current")
_JnxMbgPgwPPV2ICsCtxNotFndRx_Type = Counter64
_JnxMbgPgwPPV2ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsCtxNotFndRx = _JnxMbgPgwPPV2ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 100),
    _JnxMbgPgwPPV2ICsCtxNotFndRx_Type()
)
jnxMbgPgwPPV2ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsCtxNotFndRx.setStatus("current")
_JnxMbgPgwPPV2ICsCtxNotFndTx_Type = Counter64
_JnxMbgPgwPPV2ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsCtxNotFndTx = _JnxMbgPgwPPV2ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 101),
    _JnxMbgPgwPPV2ICsCtxNotFndTx_Type()
)
jnxMbgPgwPPV2ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsCtxNotFndTx.setStatus("current")
_JnxMbgPgwPPV2ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwPPV2ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsInvMsgFmtRx = _JnxMbgPgwPPV2ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 102),
    _JnxMbgPgwPPV2ICsInvMsgFmtRx_Type()
)
jnxMbgPgwPPV2ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwPPV2ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwPPV2ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsInvMsgFmtTx = _JnxMbgPgwPPV2ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 103),
    _JnxMbgPgwPPV2ICsInvMsgFmtTx_Type()
)
jnxMbgPgwPPV2ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwPPV2ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwPPV2ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsVerNotSuppRx = _JnxMbgPgwPPV2ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 104),
    _JnxMbgPgwPPV2ICsVerNotSuppRx_Type()
)
jnxMbgPgwPPV2ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwPPV2ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwPPV2ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsVerNotSuppTx = _JnxMbgPgwPPV2ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 105),
    _JnxMbgPgwPPV2ICsVerNotSuppTx_Type()
)
jnxMbgPgwPPV2ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwPPV2ICsInvLenRx_Type = Counter64
_JnxMbgPgwPPV2ICsInvLenRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsInvLenRx = _JnxMbgPgwPPV2ICsInvLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 106),
    _JnxMbgPgwPPV2ICsInvLenRx_Type()
)
jnxMbgPgwPPV2ICsInvLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsInvLenRx.setStatus("current")
_JnxMbgPgwPPV2ICsInvLenTx_Type = Counter64
_JnxMbgPgwPPV2ICsInvLenTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsInvLenTx = _JnxMbgPgwPPV2ICsInvLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 107),
    _JnxMbgPgwPPV2ICsInvLenTx_Type()
)
jnxMbgPgwPPV2ICsInvLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsInvLenTx.setStatus("current")
_JnxMbgPgwPPV2ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwPPV2ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsServNotSuppRx = _JnxMbgPgwPPV2ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 108),
    _JnxMbgPgwPPV2ICsServNotSuppRx_Type()
)
jnxMbgPgwPPV2ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwPPV2ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwPPV2ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsServNotSuppTx = _JnxMbgPgwPPV2ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 109),
    _JnxMbgPgwPPV2ICsServNotSuppTx_Type()
)
jnxMbgPgwPPV2ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwPPV2ICsManIEIncorrRx_Type = Counter64
_JnxMbgPgwPPV2ICsManIEIncorrRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsManIEIncorrRx = _JnxMbgPgwPPV2ICsManIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 110),
    _JnxMbgPgwPPV2ICsManIEIncorrRx_Type()
)
jnxMbgPgwPPV2ICsManIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsManIEIncorrRx.setStatus("current")
_JnxMbgPgwPPV2ICsManIEIncorrTx_Type = Counter64
_JnxMbgPgwPPV2ICsManIEIncorrTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsManIEIncorrTx = _JnxMbgPgwPPV2ICsManIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 111),
    _JnxMbgPgwPPV2ICsManIEIncorrTx_Type()
)
jnxMbgPgwPPV2ICsManIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsManIEIncorrTx.setStatus("current")
_JnxMbgPgwPPV2ICsManIEMissRx_Type = Counter64
_JnxMbgPgwPPV2ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsManIEMissRx = _JnxMbgPgwPPV2ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 112),
    _JnxMbgPgwPPV2ICsManIEMissRx_Type()
)
jnxMbgPgwPPV2ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsManIEMissRx.setStatus("current")
_JnxMbgPgwPPV2ICsManIEMissTx_Type = Counter64
_JnxMbgPgwPPV2ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsManIEMissTx = _JnxMbgPgwPPV2ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 113),
    _JnxMbgPgwPPV2ICsManIEMissTx_Type()
)
jnxMbgPgwPPV2ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsManIEMissTx.setStatus("current")
_JnxMbgPgwPPV2ICsOptIEIncorrRx_Type = Counter64
_JnxMbgPgwPPV2ICsOptIEIncorrRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsOptIEIncorrRx = _JnxMbgPgwPPV2ICsOptIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 114),
    _JnxMbgPgwPPV2ICsOptIEIncorrRx_Type()
)
jnxMbgPgwPPV2ICsOptIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsOptIEIncorrRx.setStatus("current")
_JnxMbgPgwPPV2ICsOptIEIncorrTx_Type = Counter64
_JnxMbgPgwPPV2ICsOptIEIncorrTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsOptIEIncorrTx = _JnxMbgPgwPPV2ICsOptIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 115),
    _JnxMbgPgwPPV2ICsOptIEIncorrTx_Type()
)
jnxMbgPgwPPV2ICsOptIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsOptIEIncorrTx.setStatus("current")
_JnxMbgPgwPPV2ICsSysFailRx_Type = Counter64
_JnxMbgPgwPPV2ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsSysFailRx = _JnxMbgPgwPPV2ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 116),
    _JnxMbgPgwPPV2ICsSysFailRx_Type()
)
jnxMbgPgwPPV2ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsSysFailRx.setStatus("current")
_JnxMbgPgwPPV2ICsSysFailTx_Type = Counter64
_JnxMbgPgwPPV2ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsSysFailTx = _JnxMbgPgwPPV2ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 117),
    _JnxMbgPgwPPV2ICsSysFailTx_Type()
)
jnxMbgPgwPPV2ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsSysFailTx.setStatus("current")
_JnxMbgPgwPPV2ICsNoResRx_Type = Counter64
_JnxMbgPgwPPV2ICsNoResRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNoResRx = _JnxMbgPgwPPV2ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 118),
    _JnxMbgPgwPPV2ICsNoResRx_Type()
)
jnxMbgPgwPPV2ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNoResRx.setStatus("current")
_JnxMbgPgwPPV2ICsNoResTx_Type = Counter64
_JnxMbgPgwPPV2ICsNoResTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNoResTx = _JnxMbgPgwPPV2ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 119),
    _JnxMbgPgwPPV2ICsNoResTx_Type()
)
jnxMbgPgwPPV2ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNoResTx.setStatus("current")
_JnxMbgPgwPPV2ICsTFTSMANTErRx_Type = Counter64
_JnxMbgPgwPPV2ICsTFTSMANTErRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsTFTSMANTErRx = _JnxMbgPgwPPV2ICsTFTSMANTErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 120),
    _JnxMbgPgwPPV2ICsTFTSMANTErRx_Type()
)
jnxMbgPgwPPV2ICsTFTSMANTErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsTFTSMANTErRx.setStatus("current")
_JnxMbgPgwPPV2ICsTFTSMANTErTx_Type = Counter64
_JnxMbgPgwPPV2ICsTFTSMANTErTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsTFTSMANTErTx = _JnxMbgPgwPPV2ICsTFTSMANTErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 121),
    _JnxMbgPgwPPV2ICsTFTSMANTErTx_Type()
)
jnxMbgPgwPPV2ICsTFTSMANTErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsTFTSMANTErTx.setStatus("current")
_JnxMbgPgwPPV2ICsTFTSysErrRx_Type = Counter64
_JnxMbgPgwPPV2ICsTFTSysErrRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsTFTSysErrRx = _JnxMbgPgwPPV2ICsTFTSysErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 122),
    _JnxMbgPgwPPV2ICsTFTSysErrRx_Type()
)
jnxMbgPgwPPV2ICsTFTSysErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsTFTSysErrRx.setStatus("current")
_JnxMbgPgwPPV2ICsTFTSysErrTx_Type = Counter64
_JnxMbgPgwPPV2ICsTFTSysErrTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsTFTSysErrTx = _JnxMbgPgwPPV2ICsTFTSysErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 123),
    _JnxMbgPgwPPV2ICsTFTSysErrTx_Type()
)
jnxMbgPgwPPV2ICsTFTSysErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsTFTSysErrTx.setStatus("current")
_JnxMbgPgwPPV2ICsPkFltManErrRx_Type = Counter64
_JnxMbgPgwPPV2ICsPkFltManErrRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPkFltManErrRx = _JnxMbgPgwPPV2ICsPkFltManErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 124),
    _JnxMbgPgwPPV2ICsPkFltManErrRx_Type()
)
jnxMbgPgwPPV2ICsPkFltManErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPkFltManErrRx.setStatus("current")
_JnxMbgPgwPPV2ICsPkFltManErrTx_Type = Counter64
_JnxMbgPgwPPV2ICsPkFltManErrTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPkFltManErrTx = _JnxMbgPgwPPV2ICsPkFltManErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 125),
    _JnxMbgPgwPPV2ICsPkFltManErrTx_Type()
)
jnxMbgPgwPPV2ICsPkFltManErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPkFltManErrTx.setStatus("current")
_JnxMbgPgwPPV2ICsPkFltSynErrRx_Type = Counter64
_JnxMbgPgwPPV2ICsPkFltSynErrRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPkFltSynErrRx = _JnxMbgPgwPPV2ICsPkFltSynErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 126),
    _JnxMbgPgwPPV2ICsPkFltSynErrRx_Type()
)
jnxMbgPgwPPV2ICsPkFltSynErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPkFltSynErrRx.setStatus("current")
_JnxMbgPgwPPV2ICsPkFltSynErrTx_Type = Counter64
_JnxMbgPgwPPV2ICsPkFltSynErrTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPkFltSynErrTx = _JnxMbgPgwPPV2ICsPkFltSynErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 127),
    _JnxMbgPgwPPV2ICsPkFltSynErrTx_Type()
)
jnxMbgPgwPPV2ICsPkFltSynErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPkFltSynErrTx.setStatus("current")
_JnxMbgPgwPPV2ICsMisUnknAPNRx_Type = Counter64
_JnxMbgPgwPPV2ICsMisUnknAPNRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsMisUnknAPNRx = _JnxMbgPgwPPV2ICsMisUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 128),
    _JnxMbgPgwPPV2ICsMisUnknAPNRx_Type()
)
jnxMbgPgwPPV2ICsMisUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsMisUnknAPNRx.setStatus("current")
_JnxMbgPgwPPV2ICsMisUnknAPNTx_Type = Counter64
_JnxMbgPgwPPV2ICsMisUnknAPNTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsMisUnknAPNTx = _JnxMbgPgwPPV2ICsMisUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 129),
    _JnxMbgPgwPPV2ICsMisUnknAPNTx_Type()
)
jnxMbgPgwPPV2ICsMisUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsMisUnknAPNTx.setStatus("current")
_JnxMbgPgwPPV2ICsUnexpRptIERx_Type = Counter64
_JnxMbgPgwPPV2ICsUnexpRptIERx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUnexpRptIERx = _JnxMbgPgwPPV2ICsUnexpRptIERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 130),
    _JnxMbgPgwPPV2ICsUnexpRptIERx_Type()
)
jnxMbgPgwPPV2ICsUnexpRptIERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUnexpRptIERx.setStatus("current")
_JnxMbgPgwPPV2ICsUnexpRptIETx_Type = Counter64
_JnxMbgPgwPPV2ICsUnexpRptIETx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUnexpRptIETx = _JnxMbgPgwPPV2ICsUnexpRptIETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 131),
    _JnxMbgPgwPPV2ICsUnexpRptIETx_Type()
)
jnxMbgPgwPPV2ICsUnexpRptIETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUnexpRptIETx.setStatus("current")
_JnxMbgPgwPPV2ICsGREKeyNtFdRx_Type = Counter64
_JnxMbgPgwPPV2ICsGREKeyNtFdRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsGREKeyNtFdRx = _JnxMbgPgwPPV2ICsGREKeyNtFdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 132),
    _JnxMbgPgwPPV2ICsGREKeyNtFdRx_Type()
)
jnxMbgPgwPPV2ICsGREKeyNtFdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsGREKeyNtFdRx.setStatus("current")
_JnxMbgPgwPPV2ICsGREKeyNtFdTx_Type = Counter64
_JnxMbgPgwPPV2ICsGREKeyNtFdTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsGREKeyNtFdTx = _JnxMbgPgwPPV2ICsGREKeyNtFdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 133),
    _JnxMbgPgwPPV2ICsGREKeyNtFdTx_Type()
)
jnxMbgPgwPPV2ICsGREKeyNtFdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsGREKeyNtFdTx.setStatus("current")
_JnxMbgPgwPPV2ICsRelocFailRx_Type = Counter64
_JnxMbgPgwPPV2ICsRelocFailRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsRelocFailRx = _JnxMbgPgwPPV2ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 134),
    _JnxMbgPgwPPV2ICsRelocFailRx_Type()
)
jnxMbgPgwPPV2ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsRelocFailRx.setStatus("current")
_JnxMbgPgwPPV2ICsRelocFailTx_Type = Counter64
_JnxMbgPgwPPV2ICsRelocFailTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsRelocFailTx = _JnxMbgPgwPPV2ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 135),
    _JnxMbgPgwPPV2ICsRelocFailTx_Type()
)
jnxMbgPgwPPV2ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsRelocFailTx.setStatus("current")
_JnxMbgPgwPPV2ICsDeniedINRatRx_Type = Counter64
_JnxMbgPgwPPV2ICsDeniedINRatRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsDeniedINRatRx = _JnxMbgPgwPPV2ICsDeniedINRatRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 136),
    _JnxMbgPgwPPV2ICsDeniedINRatRx_Type()
)
jnxMbgPgwPPV2ICsDeniedINRatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsDeniedINRatRx.setStatus("current")
_JnxMbgPgwPPV2ICsDeniedINRatTx_Type = Counter64
_JnxMbgPgwPPV2ICsDeniedINRatTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsDeniedINRatTx = _JnxMbgPgwPPV2ICsDeniedINRatTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 137),
    _JnxMbgPgwPPV2ICsDeniedINRatTx_Type()
)
jnxMbgPgwPPV2ICsDeniedINRatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsDeniedINRatTx.setStatus("current")
_JnxMbgPgwPPV2ICsPTNotSuppRx_Type = Counter64
_JnxMbgPgwPPV2ICsPTNotSuppRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPTNotSuppRx = _JnxMbgPgwPPV2ICsPTNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 138),
    _JnxMbgPgwPPV2ICsPTNotSuppRx_Type()
)
jnxMbgPgwPPV2ICsPTNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPTNotSuppRx.setStatus("current")
_JnxMbgPgwPPV2ICsPTNotSuppTx_Type = Counter64
_JnxMbgPgwPPV2ICsPTNotSuppTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPTNotSuppTx = _JnxMbgPgwPPV2ICsPTNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 139),
    _JnxMbgPgwPPV2ICsPTNotSuppTx_Type()
)
jnxMbgPgwPPV2ICsPTNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPTNotSuppTx.setStatus("current")
_JnxMbgPgwPPV2ICsAllDynAdOccRx_Type = Counter64
_JnxMbgPgwPPV2ICsAllDynAdOccRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAllDynAdOccRx = _JnxMbgPgwPPV2ICsAllDynAdOccRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 140),
    _JnxMbgPgwPPV2ICsAllDynAdOccRx_Type()
)
jnxMbgPgwPPV2ICsAllDynAdOccRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAllDynAdOccRx.setStatus("current")
_JnxMbgPgwPPV2ICsAllDynAdOccTx_Type = Counter64
_JnxMbgPgwPPV2ICsAllDynAdOccTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAllDynAdOccTx = _JnxMbgPgwPPV2ICsAllDynAdOccTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 141),
    _JnxMbgPgwPPV2ICsAllDynAdOccTx_Type()
)
jnxMbgPgwPPV2ICsAllDynAdOccTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAllDynAdOccTx.setStatus("current")
_JnxMbgPgwPPV2ICsNOTFTUECTXRx_Type = Counter64
_JnxMbgPgwPPV2ICsNOTFTUECTXRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNOTFTUECTXRx = _JnxMbgPgwPPV2ICsNOTFTUECTXRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 142),
    _JnxMbgPgwPPV2ICsNOTFTUECTXRx_Type()
)
jnxMbgPgwPPV2ICsNOTFTUECTXRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNOTFTUECTXRx.setStatus("current")
_JnxMbgPgwPPV2ICsNOTFTUECTXTx_Type = Counter64
_JnxMbgPgwPPV2ICsNOTFTUECTXTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNOTFTUECTXTx = _JnxMbgPgwPPV2ICsNOTFTUECTXTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 143),
    _JnxMbgPgwPPV2ICsNOTFTUECTXTx_Type()
)
jnxMbgPgwPPV2ICsNOTFTUECTXTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNOTFTUECTXTx.setStatus("current")
_JnxMbgPgwPPV2ICsProtoNtSupRx_Type = Counter64
_JnxMbgPgwPPV2ICsProtoNtSupRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsProtoNtSupRx = _JnxMbgPgwPPV2ICsProtoNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 144),
    _JnxMbgPgwPPV2ICsProtoNtSupRx_Type()
)
jnxMbgPgwPPV2ICsProtoNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsProtoNtSupRx.setStatus("current")
_JnxMbgPgwPPV2ICsProtoNtSupTx_Type = Counter64
_JnxMbgPgwPPV2ICsProtoNtSupTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsProtoNtSupTx = _JnxMbgPgwPPV2ICsProtoNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 145),
    _JnxMbgPgwPPV2ICsProtoNtSupTx_Type()
)
jnxMbgPgwPPV2ICsProtoNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsProtoNtSupTx.setStatus("current")
_JnxMbgPgwPPV2ICsUENotRespRx_Type = Counter64
_JnxMbgPgwPPV2ICsUENotRespRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUENotRespRx = _JnxMbgPgwPPV2ICsUENotRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 146),
    _JnxMbgPgwPPV2ICsUENotRespRx_Type()
)
jnxMbgPgwPPV2ICsUENotRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUENotRespRx.setStatus("current")
_JnxMbgPgwPPV2ICsUENotRespTx_Type = Counter64
_JnxMbgPgwPPV2ICsUENotRespTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUENotRespTx = _JnxMbgPgwPPV2ICsUENotRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 147),
    _JnxMbgPgwPPV2ICsUENotRespTx_Type()
)
jnxMbgPgwPPV2ICsUENotRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUENotRespTx.setStatus("current")
_JnxMbgPgwPPV2ICsUERefusesRx_Type = Counter64
_JnxMbgPgwPPV2ICsUERefusesRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUERefusesRx = _JnxMbgPgwPPV2ICsUERefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 148),
    _JnxMbgPgwPPV2ICsUERefusesRx_Type()
)
jnxMbgPgwPPV2ICsUERefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUERefusesRx.setStatus("current")
_JnxMbgPgwPPV2ICsUERefusesTx_Type = Counter64
_JnxMbgPgwPPV2ICsUERefusesTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUERefusesTx = _JnxMbgPgwPPV2ICsUERefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 149),
    _JnxMbgPgwPPV2ICsUERefusesTx_Type()
)
jnxMbgPgwPPV2ICsUERefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUERefusesTx.setStatus("current")
_JnxMbgPgwPPV2ICsServDeniedRx_Type = Counter64
_JnxMbgPgwPPV2ICsServDeniedRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsServDeniedRx = _JnxMbgPgwPPV2ICsServDeniedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 150),
    _JnxMbgPgwPPV2ICsServDeniedRx_Type()
)
jnxMbgPgwPPV2ICsServDeniedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsServDeniedRx.setStatus("current")
_JnxMbgPgwPPV2ICsServDeniedTx_Type = Counter64
_JnxMbgPgwPPV2ICsServDeniedTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsServDeniedTx = _JnxMbgPgwPPV2ICsServDeniedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 151),
    _JnxMbgPgwPPV2ICsServDeniedTx_Type()
)
jnxMbgPgwPPV2ICsServDeniedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsServDeniedTx.setStatus("current")
_JnxMbgPgwPPV2ICsUnabPageUERx_Type = Counter64
_JnxMbgPgwPPV2ICsUnabPageUERx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUnabPageUERx = _JnxMbgPgwPPV2ICsUnabPageUERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 152),
    _JnxMbgPgwPPV2ICsUnabPageUERx_Type()
)
jnxMbgPgwPPV2ICsUnabPageUERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUnabPageUERx.setStatus("current")
_JnxMbgPgwPPV2ICsUnabPageUETx_Type = Counter64
_JnxMbgPgwPPV2ICsUnabPageUETx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUnabPageUETx = _JnxMbgPgwPPV2ICsUnabPageUETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 153),
    _JnxMbgPgwPPV2ICsUnabPageUETx_Type()
)
jnxMbgPgwPPV2ICsUnabPageUETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUnabPageUETx.setStatus("current")
_JnxMbgPgwPPV2ICsNoMemRx_Type = Counter64
_JnxMbgPgwPPV2ICsNoMemRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNoMemRx = _JnxMbgPgwPPV2ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 154),
    _JnxMbgPgwPPV2ICsNoMemRx_Type()
)
jnxMbgPgwPPV2ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNoMemRx.setStatus("current")
_JnxMbgPgwPPV2ICsNoMemTx_Type = Counter64
_JnxMbgPgwPPV2ICsNoMemTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsNoMemTx = _JnxMbgPgwPPV2ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 155),
    _JnxMbgPgwPPV2ICsNoMemTx_Type()
)
jnxMbgPgwPPV2ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsNoMemTx.setStatus("current")
_JnxMbgPgwPPV2ICsUserAUTHFlRx_Type = Counter64
_JnxMbgPgwPPV2ICsUserAUTHFlRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUserAUTHFlRx = _JnxMbgPgwPPV2ICsUserAUTHFlRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 156),
    _JnxMbgPgwPPV2ICsUserAUTHFlRx_Type()
)
jnxMbgPgwPPV2ICsUserAUTHFlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUserAUTHFlRx.setStatus("current")
_JnxMbgPgwPPV2ICsUserAUTHFlTx_Type = Counter64
_JnxMbgPgwPPV2ICsUserAUTHFlTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUserAUTHFlTx = _JnxMbgPgwPPV2ICsUserAUTHFlTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 157),
    _JnxMbgPgwPPV2ICsUserAUTHFlTx_Type()
)
jnxMbgPgwPPV2ICsUserAUTHFlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUserAUTHFlTx.setStatus("current")
_JnxMbgPgwPPV2ICsAPNAcsDenRx_Type = Counter64
_JnxMbgPgwPPV2ICsAPNAcsDenRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAPNAcsDenRx = _JnxMbgPgwPPV2ICsAPNAcsDenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 158),
    _JnxMbgPgwPPV2ICsAPNAcsDenRx_Type()
)
jnxMbgPgwPPV2ICsAPNAcsDenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAPNAcsDenRx.setStatus("current")
_JnxMbgPgwPPV2ICsAPNAcsDenTx_Type = Counter64
_JnxMbgPgwPPV2ICsAPNAcsDenTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAPNAcsDenTx = _JnxMbgPgwPPV2ICsAPNAcsDenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 159),
    _JnxMbgPgwPPV2ICsAPNAcsDenTx_Type()
)
jnxMbgPgwPPV2ICsAPNAcsDenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAPNAcsDenTx.setStatus("current")
_JnxMbgPgwPPV2ICsReqRejRx_Type = Counter64
_JnxMbgPgwPPV2ICsReqRejRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsReqRejRx = _JnxMbgPgwPPV2ICsReqRejRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 160),
    _JnxMbgPgwPPV2ICsReqRejRx_Type()
)
jnxMbgPgwPPV2ICsReqRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsReqRejRx.setStatus("current")
_JnxMbgPgwPPV2ICsReqRejTx_Type = Counter64
_JnxMbgPgwPPV2ICsReqRejTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsReqRejTx = _JnxMbgPgwPPV2ICsReqRejTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 161),
    _JnxMbgPgwPPV2ICsReqRejTx_Type()
)
jnxMbgPgwPPV2ICsReqRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsReqRejTx.setStatus("current")
_JnxMbgPgwPPV2ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwPPV2ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPTMSISigMMRx = _JnxMbgPgwPPV2ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 162),
    _JnxMbgPgwPPV2ICsPTMSISigMMRx_Type()
)
jnxMbgPgwPPV2ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwPPV2ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwPPV2ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsPTMSISigMMTx = _JnxMbgPgwPPV2ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 163),
    _JnxMbgPgwPPV2ICsPTMSISigMMTx_Type()
)
jnxMbgPgwPPV2ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwPPV2ICsIMSINotKnRx_Type = Counter64
_JnxMbgPgwPPV2ICsIMSINotKnRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsIMSINotKnRx = _JnxMbgPgwPPV2ICsIMSINotKnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 164),
    _JnxMbgPgwPPV2ICsIMSINotKnRx_Type()
)
jnxMbgPgwPPV2ICsIMSINotKnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsIMSINotKnRx.setStatus("current")
_JnxMbgPgwPPV2ICsIMSINotKnTx_Type = Counter64
_JnxMbgPgwPPV2ICsIMSINotKnTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsIMSINotKnTx = _JnxMbgPgwPPV2ICsIMSINotKnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 165),
    _JnxMbgPgwPPV2ICsIMSINotKnTx_Type()
)
jnxMbgPgwPPV2ICsIMSINotKnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsIMSINotKnTx.setStatus("current")
_JnxMbgPgwPPV2ICsCondIEMsRx_Type = Counter64
_JnxMbgPgwPPV2ICsCondIEMsRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsCondIEMsRx = _JnxMbgPgwPPV2ICsCondIEMsRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 166),
    _JnxMbgPgwPPV2ICsCondIEMsRx_Type()
)
jnxMbgPgwPPV2ICsCondIEMsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsCondIEMsRx.setStatus("current")
_JnxMbgPgwPPV2ICsCondIEMsTx_Type = Counter64
_JnxMbgPgwPPV2ICsCondIEMsTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsCondIEMsTx = _JnxMbgPgwPPV2ICsCondIEMsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 167),
    _JnxMbgPgwPPV2ICsCondIEMsTx_Type()
)
jnxMbgPgwPPV2ICsCondIEMsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsCondIEMsTx.setStatus("current")
_JnxMbgPgwPPV2ICsAPNResTIncRx_Type = Counter64
_JnxMbgPgwPPV2ICsAPNResTIncRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAPNResTIncRx = _JnxMbgPgwPPV2ICsAPNResTIncRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 168),
    _JnxMbgPgwPPV2ICsAPNResTIncRx_Type()
)
jnxMbgPgwPPV2ICsAPNResTIncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAPNResTIncRx.setStatus("current")
_JnxMbgPgwPPV2ICsAPNResTIncTx_Type = Counter64
_JnxMbgPgwPPV2ICsAPNResTIncTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsAPNResTIncTx = _JnxMbgPgwPPV2ICsAPNResTIncTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 169),
    _JnxMbgPgwPPV2ICsAPNResTIncTx_Type()
)
jnxMbgPgwPPV2ICsAPNResTIncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsAPNResTIncTx.setStatus("current")
_JnxMbgPgwPPV2ICsUnknownRx_Type = Counter64
_JnxMbgPgwPPV2ICsUnknownRx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUnknownRx = _JnxMbgPgwPPV2ICsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 170),
    _JnxMbgPgwPPV2ICsUnknownRx_Type()
)
jnxMbgPgwPPV2ICsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUnknownRx.setStatus("current")
_JnxMbgPgwPPV2ICsUnknownTx_Type = Counter64
_JnxMbgPgwPPV2ICsUnknownTx_Object = MibTableColumn
jnxMbgPgwPPV2ICsUnknownTx = _JnxMbgPgwPPV2ICsUnknownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 171),
    _JnxMbgPgwPPV2ICsUnknownTx_Type()
)
jnxMbgPgwPPV2ICsUnknownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ICsUnknownTx.setStatus("current")
_JnxMbgPgwPPV1ProtocolErrRx_Type = Counter64
_JnxMbgPgwPPV1ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwPPV1ProtocolErrRx = _JnxMbgPgwPPV1ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 172),
    _JnxMbgPgwPPV1ProtocolErrRx_Type()
)
jnxMbgPgwPPV1ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ProtocolErrRx.setStatus("current")
_JnxMbgPgwPPV1UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwPPV1UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwPPV1UnSupportedMsgRx = _JnxMbgPgwPPV1UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 173),
    _JnxMbgPgwPPV1UnSupportedMsgRx_Type()
)
jnxMbgPgwPPV1UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwPPV1T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwPPV1T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwPPV1T3RespTmrExpRx = _JnxMbgPgwPPV1T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 174),
    _JnxMbgPgwPPV1T3RespTmrExpRx_Type()
)
jnxMbgPgwPPV1T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwPPV1GlbNumMsgRx_Type = Counter64
_JnxMbgPgwPPV1GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwPPV1GlbNumMsgRx = _JnxMbgPgwPPV1GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 175),
    _JnxMbgPgwPPV1GlbNumMsgRx_Type()
)
jnxMbgPgwPPV1GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbNumMsgRx.setStatus("current")
_JnxMbgPgwPPV1GlbNumMsgTx_Type = Counter64
_JnxMbgPgwPPV1GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwPPV1GlbNumMsgTx = _JnxMbgPgwPPV1GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 176),
    _JnxMbgPgwPPV1GlbNumMsgTx_Type()
)
jnxMbgPgwPPV1GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbNumMsgTx.setStatus("current")
_JnxMbgPgwPPV1GlbNumBytesRx_Type = Counter64
_JnxMbgPgwPPV1GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwPPV1GlbNumBytesRx = _JnxMbgPgwPPV1GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 177),
    _JnxMbgPgwPPV1GlbNumBytesRx_Type()
)
jnxMbgPgwPPV1GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbNumBytesRx.setStatus("current")
_JnxMbgPgwPPV1GlbNumBytesTx_Type = Counter64
_JnxMbgPgwPPV1GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwPPV1GlbNumBytesTx = _JnxMbgPgwPPV1GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 178),
    _JnxMbgPgwPPV1GlbNumBytesTx_Type()
)
jnxMbgPgwPPV1GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbNumBytesTx.setStatus("current")
_JnxMbgPgwPPV1GlbEchoReqRx_Type = Counter64
_JnxMbgPgwPPV1GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwPPV1GlbEchoReqRx = _JnxMbgPgwPPV1GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 179),
    _JnxMbgPgwPPV1GlbEchoReqRx_Type()
)
jnxMbgPgwPPV1GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbEchoReqRx.setStatus("current")
_JnxMbgPgwPPV1GlbEchoReqTx_Type = Counter64
_JnxMbgPgwPPV1GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwPPV1GlbEchoReqTx = _JnxMbgPgwPPV1GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 180),
    _JnxMbgPgwPPV1GlbEchoReqTx_Type()
)
jnxMbgPgwPPV1GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbEchoReqTx.setStatus("current")
_JnxMbgPgwPPV1GlbEchoRespRx_Type = Counter64
_JnxMbgPgwPPV1GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwPPV1GlbEchoRespRx = _JnxMbgPgwPPV1GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 181),
    _JnxMbgPgwPPV1GlbEchoRespRx_Type()
)
jnxMbgPgwPPV1GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbEchoRespRx.setStatus("current")
_JnxMbgPgwPPV1GlbEchoRespTx_Type = Counter64
_JnxMbgPgwPPV1GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwPPV1GlbEchoRespTx = _JnxMbgPgwPPV1GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 182),
    _JnxMbgPgwPPV1GlbEchoRespTx_Type()
)
jnxMbgPgwPPV1GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1GlbEchoRespTx.setStatus("current")
_JnxMbgPgwPPV1VerNotSupRx_Type = Counter64
_JnxMbgPgwPPV1VerNotSupRx_Object = MibTableColumn
jnxMbgPgwPPV1VerNotSupRx = _JnxMbgPgwPPV1VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 183),
    _JnxMbgPgwPPV1VerNotSupRx_Type()
)
jnxMbgPgwPPV1VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1VerNotSupRx.setStatus("current")
_JnxMbgPgwPPV1VerNotSupTx_Type = Counter64
_JnxMbgPgwPPV1VerNotSupTx_Object = MibTableColumn
jnxMbgPgwPPV1VerNotSupTx = _JnxMbgPgwPPV1VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 184),
    _JnxMbgPgwPPV1VerNotSupTx_Type()
)
jnxMbgPgwPPV1VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1VerNotSupTx.setStatus("current")
_JnxMbgPgwPPV1CrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV1CrtPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV1CrtPdpCxtReqRx = _JnxMbgPgwPPV1CrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 185),
    _JnxMbgPgwPPV1CrtPdpCxtReqRx_Type()
)
jnxMbgPgwPPV1CrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV1CrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV1CrtPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV1CrtPdpCxtReqTx = _JnxMbgPgwPPV1CrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 186),
    _JnxMbgPgwPPV1CrtPdpCxtReqTx_Type()
)
jnxMbgPgwPPV1CrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV1CrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV1CrtPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV1CrtPdpCxtRspRx = _JnxMbgPgwPPV1CrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 187),
    _JnxMbgPgwPPV1CrtPdpCxtRspRx_Type()
)
jnxMbgPgwPPV1CrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV1CrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV1CrtPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV1CrtPdpCxtRspTx = _JnxMbgPgwPPV1CrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 188),
    _JnxMbgPgwPPV1CrtPdpCxtRspTx_Type()
)
jnxMbgPgwPPV1CrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV1UpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV1UpdPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV1UpdPdpCxtReqRx = _JnxMbgPgwPPV1UpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 189),
    _JnxMbgPgwPPV1UpdPdpCxtReqRx_Type()
)
jnxMbgPgwPPV1UpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1UpdPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV1UpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV1UpdPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV1UpdPdpCxtReqTx = _JnxMbgPgwPPV1UpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 190),
    _JnxMbgPgwPPV1UpdPdpCxtReqTx_Type()
)
jnxMbgPgwPPV1UpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1UpdPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV1UpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV1UpdPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV1UpdPdpCxtRspRx = _JnxMbgPgwPPV1UpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 191),
    _JnxMbgPgwPPV1UpdPdpCxtRspRx_Type()
)
jnxMbgPgwPPV1UpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1UpdPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV1UpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV1UpdPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV1UpdPdpCxtRspTx = _JnxMbgPgwPPV1UpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 192),
    _JnxMbgPgwPPV1UpdPdpCxtRspTx_Type()
)
jnxMbgPgwPPV1UpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1UpdPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV1DelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV1DelPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV1DelPdpCxtReqRx = _JnxMbgPgwPPV1DelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 193),
    _JnxMbgPgwPPV1DelPdpCxtReqRx_Type()
)
jnxMbgPgwPPV1DelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV1DelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV1DelPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV1DelPdpCxtReqTx = _JnxMbgPgwPPV1DelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 194),
    _JnxMbgPgwPPV1DelPdpCxtReqTx_Type()
)
jnxMbgPgwPPV1DelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV1DelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV1DelPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV1DelPdpCxtRspRx = _JnxMbgPgwPPV1DelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 195),
    _JnxMbgPgwPPV1DelPdpCxtRspRx_Type()
)
jnxMbgPgwPPV1DelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV1DelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV1DelPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV1DelPdpCxtRspTx = _JnxMbgPgwPPV1DelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 196),
    _JnxMbgPgwPPV1DelPdpCxtRspTx_Type()
)
jnxMbgPgwPPV1DelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV1CrtAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV1CrtAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV1CrtAAPdpCxtReqRx = _JnxMbgPgwPPV1CrtAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 197),
    _JnxMbgPgwPPV1CrtAAPdpCxtReqRx_Type()
)
jnxMbgPgwPPV1CrtAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV1CrtAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV1CrtAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV1CrtAAPdpCxtReqTx = _JnxMbgPgwPPV1CrtAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 198),
    _JnxMbgPgwPPV1CrtAAPdpCxtReqTx_Type()
)
jnxMbgPgwPPV1CrtAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV1CrtAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV1CrtAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV1CrtAAPdpCxtRspRx = _JnxMbgPgwPPV1CrtAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 199),
    _JnxMbgPgwPPV1CrtAAPdpCxtRspRx_Type()
)
jnxMbgPgwPPV1CrtAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV1CrtAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV1CrtAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV1CrtAAPdpCxtRspTx = _JnxMbgPgwPPV1CrtAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 200),
    _JnxMbgPgwPPV1CrtAAPdpCxtRspTx_Type()
)
jnxMbgPgwPPV1CrtAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1CrtAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV1DelAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV1DelAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV1DelAAPdpCxtReqRx = _JnxMbgPgwPPV1DelAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 201),
    _JnxMbgPgwPPV1DelAAPdpCxtReqRx_Type()
)
jnxMbgPgwPPV1DelAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV1DelAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV1DelAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV1DelAAPdpCxtReqTx = _JnxMbgPgwPPV1DelAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 202),
    _JnxMbgPgwPPV1DelAAPdpCxtReqTx_Type()
)
jnxMbgPgwPPV1DelAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV1DelAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV1DelAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV1DelAAPdpCxtRspRx = _JnxMbgPgwPPV1DelAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 203),
    _JnxMbgPgwPPV1DelAAPdpCxtRspRx_Type()
)
jnxMbgPgwPPV1DelAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV1DelAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV1DelAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV1DelAAPdpCxtRspTx = _JnxMbgPgwPPV1DelAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 204),
    _JnxMbgPgwPPV1DelAAPdpCxtRspTx_Type()
)
jnxMbgPgwPPV1DelAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1DelAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV1ErrorIndRx_Type = Counter64
_JnxMbgPgwPPV1ErrorIndRx_Object = MibTableColumn
jnxMbgPgwPPV1ErrorIndRx = _JnxMbgPgwPPV1ErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 205),
    _JnxMbgPgwPPV1ErrorIndRx_Type()
)
jnxMbgPgwPPV1ErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ErrorIndRx.setStatus("current")
_JnxMbgPgwPPV1ErrorIndTx_Type = Counter64
_JnxMbgPgwPPV1ErrorIndTx_Object = MibTableColumn
jnxMbgPgwPPV1ErrorIndTx = _JnxMbgPgwPPV1ErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 206),
    _JnxMbgPgwPPV1ErrorIndTx_Type()
)
jnxMbgPgwPPV1ErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ErrorIndTx.setStatus("current")
_JnxMbgPgwPPV1NotifReqRx_Type = Counter64
_JnxMbgPgwPPV1NotifReqRx_Object = MibTableColumn
jnxMbgPgwPPV1NotifReqRx = _JnxMbgPgwPPV1NotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 207),
    _JnxMbgPgwPPV1NotifReqRx_Type()
)
jnxMbgPgwPPV1NotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifReqRx.setStatus("current")
_JnxMbgPgwPPV1NotifReqTx_Type = Counter64
_JnxMbgPgwPPV1NotifReqTx_Object = MibTableColumn
jnxMbgPgwPPV1NotifReqTx = _JnxMbgPgwPPV1NotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 208),
    _JnxMbgPgwPPV1NotifReqTx_Type()
)
jnxMbgPgwPPV1NotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifReqTx.setStatus("current")
_JnxMbgPgwPPV1NotifRspRx_Type = Counter64
_JnxMbgPgwPPV1NotifRspRx_Object = MibTableColumn
jnxMbgPgwPPV1NotifRspRx = _JnxMbgPgwPPV1NotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 209),
    _JnxMbgPgwPPV1NotifRspRx_Type()
)
jnxMbgPgwPPV1NotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifRspRx.setStatus("current")
_JnxMbgPgwPPV1NotifRspTx_Type = Counter64
_JnxMbgPgwPPV1NotifRspTx_Object = MibTableColumn
jnxMbgPgwPPV1NotifRspTx = _JnxMbgPgwPPV1NotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 210),
    _JnxMbgPgwPPV1NotifRspTx_Type()
)
jnxMbgPgwPPV1NotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifRspTx.setStatus("current")
_JnxMbgPgwPPV1NotifRejReqRx_Type = Counter64
_JnxMbgPgwPPV1NotifRejReqRx_Object = MibTableColumn
jnxMbgPgwPPV1NotifRejReqRx = _JnxMbgPgwPPV1NotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 211),
    _JnxMbgPgwPPV1NotifRejReqRx_Type()
)
jnxMbgPgwPPV1NotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifRejReqRx.setStatus("current")
_JnxMbgPgwPPV1NotifRejReqTx_Type = Counter64
_JnxMbgPgwPPV1NotifRejReqTx_Object = MibTableColumn
jnxMbgPgwPPV1NotifRejReqTx = _JnxMbgPgwPPV1NotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 212),
    _JnxMbgPgwPPV1NotifRejReqTx_Type()
)
jnxMbgPgwPPV1NotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifRejReqTx.setStatus("current")
_JnxMbgPgwPPV1NotifRejRspRx_Type = Counter64
_JnxMbgPgwPPV1NotifRejRspRx_Object = MibTableColumn
jnxMbgPgwPPV1NotifRejRspRx = _JnxMbgPgwPPV1NotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 213),
    _JnxMbgPgwPPV1NotifRejRspRx_Type()
)
jnxMbgPgwPPV1NotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifRejRspRx.setStatus("current")
_JnxMbgPgwPPV1NotifRejRspTx_Type = Counter64
_JnxMbgPgwPPV1NotifRejRspTx_Object = MibTableColumn
jnxMbgPgwPPV1NotifRejRspTx = _JnxMbgPgwPPV1NotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 214),
    _JnxMbgPgwPPV1NotifRejRspTx_Type()
)
jnxMbgPgwPPV1NotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotifRejRspTx.setStatus("current")
_JnxMbgPgwPPV1RtInfReqRx_Type = Counter64
_JnxMbgPgwPPV1RtInfReqRx_Object = MibTableColumn
jnxMbgPgwPPV1RtInfReqRx = _JnxMbgPgwPPV1RtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 215),
    _JnxMbgPgwPPV1RtInfReqRx_Type()
)
jnxMbgPgwPPV1RtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1RtInfReqRx.setStatus("current")
_JnxMbgPgwPPV1RtInfReqTx_Type = Counter64
_JnxMbgPgwPPV1RtInfReqTx_Object = MibTableColumn
jnxMbgPgwPPV1RtInfReqTx = _JnxMbgPgwPPV1RtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 216),
    _JnxMbgPgwPPV1RtInfReqTx_Type()
)
jnxMbgPgwPPV1RtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1RtInfReqTx.setStatus("current")
_JnxMbgPgwPPV1RtInfRspRx_Type = Counter64
_JnxMbgPgwPPV1RtInfRspRx_Object = MibTableColumn
jnxMbgPgwPPV1RtInfRspRx = _JnxMbgPgwPPV1RtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 217),
    _JnxMbgPgwPPV1RtInfRspRx_Type()
)
jnxMbgPgwPPV1RtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1RtInfRspRx.setStatus("current")
_JnxMbgPgwPPV1RtInfRspTx_Type = Counter64
_JnxMbgPgwPPV1RtInfRspTx_Object = MibTableColumn
jnxMbgPgwPPV1RtInfRspTx = _JnxMbgPgwPPV1RtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 218),
    _JnxMbgPgwPPV1RtInfRspTx_Type()
)
jnxMbgPgwPPV1RtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1RtInfRspTx.setStatus("current")
_JnxMbgPgwPPV1FailRptReqRx_Type = Counter64
_JnxMbgPgwPPV1FailRptReqRx_Object = MibTableColumn
jnxMbgPgwPPV1FailRptReqRx = _JnxMbgPgwPPV1FailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 219),
    _JnxMbgPgwPPV1FailRptReqRx_Type()
)
jnxMbgPgwPPV1FailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1FailRptReqRx.setStatus("current")
_JnxMbgPgwPPV1FailRptReqTx_Type = Counter64
_JnxMbgPgwPPV1FailRptReqTx_Object = MibTableColumn
jnxMbgPgwPPV1FailRptReqTx = _JnxMbgPgwPPV1FailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 220),
    _JnxMbgPgwPPV1FailRptReqTx_Type()
)
jnxMbgPgwPPV1FailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1FailRptReqTx.setStatus("current")
_JnxMbgPgwPPV1FailRptRspRx_Type = Counter64
_JnxMbgPgwPPV1FailRptRspRx_Object = MibTableColumn
jnxMbgPgwPPV1FailRptRspRx = _JnxMbgPgwPPV1FailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 221),
    _JnxMbgPgwPPV1FailRptRspRx_Type()
)
jnxMbgPgwPPV1FailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1FailRptRspRx.setStatus("current")
_JnxMbgPgwPPV1FailRptRspTx_Type = Counter64
_JnxMbgPgwPPV1FailRptRspTx_Object = MibTableColumn
jnxMbgPgwPPV1FailRptRspTx = _JnxMbgPgwPPV1FailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 222),
    _JnxMbgPgwPPV1FailRptRspTx_Type()
)
jnxMbgPgwPPV1FailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1FailRptRspTx.setStatus("current")
_JnxMbgPgwPPV1NotMSPresReqRx_Type = Counter64
_JnxMbgPgwPPV1NotMSPresReqRx_Object = MibTableColumn
jnxMbgPgwPPV1NotMSPresReqRx = _JnxMbgPgwPPV1NotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 223),
    _JnxMbgPgwPPV1NotMSPresReqRx_Type()
)
jnxMbgPgwPPV1NotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotMSPresReqRx.setStatus("current")
_JnxMbgPgwPPV1NotMSPresReqTx_Type = Counter64
_JnxMbgPgwPPV1NotMSPresReqTx_Object = MibTableColumn
jnxMbgPgwPPV1NotMSPresReqTx = _JnxMbgPgwPPV1NotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 224),
    _JnxMbgPgwPPV1NotMSPresReqTx_Type()
)
jnxMbgPgwPPV1NotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotMSPresReqTx.setStatus("current")
_JnxMbgPgwPPV1NotMSPresRspRx_Type = Counter64
_JnxMbgPgwPPV1NotMSPresRspRx_Object = MibTableColumn
jnxMbgPgwPPV1NotMSPresRspRx = _JnxMbgPgwPPV1NotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 225),
    _JnxMbgPgwPPV1NotMSPresRspRx_Type()
)
jnxMbgPgwPPV1NotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotMSPresRspRx.setStatus("current")
_JnxMbgPgwPPV1NotMSPresRspTx_Type = Counter64
_JnxMbgPgwPPV1NotMSPresRspTx_Object = MibTableColumn
jnxMbgPgwPPV1NotMSPresRspTx = _JnxMbgPgwPPV1NotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 226),
    _JnxMbgPgwPPV1NotMSPresRspTx_Type()
)
jnxMbgPgwPPV1NotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1NotMSPresRspTx.setStatus("current")
_JnxMbgPgwPPV1ICsReqAcceptedRx_Type = Counter64
_JnxMbgPgwPPV1ICsReqAcceptedRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsReqAcceptedRx = _JnxMbgPgwPPV1ICsReqAcceptedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 227),
    _JnxMbgPgwPPV1ICsReqAcceptedRx_Type()
)
jnxMbgPgwPPV1ICsReqAcceptedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsReqAcceptedRx.setStatus("current")
_JnxMbgPgwPPV1ICsReqAcceptedTx_Type = Counter64
_JnxMbgPgwPPV1ICsReqAcceptedTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsReqAcceptedTx = _JnxMbgPgwPPV1ICsReqAcceptedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 228),
    _JnxMbgPgwPPV1ICsReqAcceptedTx_Type()
)
jnxMbgPgwPPV1ICsReqAcceptedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsReqAcceptedTx.setStatus("current")
_JnxMbgPgwPPV1ICsNonExistRx_Type = Counter64
_JnxMbgPgwPPV1ICsNonExistRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNonExistRx = _JnxMbgPgwPPV1ICsNonExistRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 229),
    _JnxMbgPgwPPV1ICsNonExistRx_Type()
)
jnxMbgPgwPPV1ICsNonExistRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNonExistRx.setStatus("current")
_JnxMbgPgwPPV1ICsNonExistTx_Type = Counter64
_JnxMbgPgwPPV1ICsNonExistTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNonExistTx = _JnxMbgPgwPPV1ICsNonExistTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 230),
    _JnxMbgPgwPPV1ICsNonExistTx_Type()
)
jnxMbgPgwPPV1ICsNonExistTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNonExistTx.setStatus("current")
_JnxMbgPgwPPV1ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwPPV1ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsInvMsgFmtRx = _JnxMbgPgwPPV1ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 231),
    _JnxMbgPgwPPV1ICsInvMsgFmtRx_Type()
)
jnxMbgPgwPPV1ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwPPV1ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwPPV1ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsInvMsgFmtTx = _JnxMbgPgwPPV1ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 232),
    _JnxMbgPgwPPV1ICsInvMsgFmtTx_Type()
)
jnxMbgPgwPPV1ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwPPV1ICsIMSINotKnownRx_Type = Counter64
_JnxMbgPgwPPV1ICsIMSINotKnownRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsIMSINotKnownRx = _JnxMbgPgwPPV1ICsIMSINotKnownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 233),
    _JnxMbgPgwPPV1ICsIMSINotKnownRx_Type()
)
jnxMbgPgwPPV1ICsIMSINotKnownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsIMSINotKnownRx.setStatus("current")
_JnxMbgPgwPPV1ICsIMSINotKnownTx_Type = Counter64
_JnxMbgPgwPPV1ICsIMSINotKnownTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsIMSINotKnownTx = _JnxMbgPgwPPV1ICsIMSINotKnownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 234),
    _JnxMbgPgwPPV1ICsIMSINotKnownTx_Type()
)
jnxMbgPgwPPV1ICsIMSINotKnownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsIMSINotKnownTx.setStatus("current")
_JnxMbgPgwPPV1ICsMSGRPSDetachRx_Type = Counter64
_JnxMbgPgwPPV1ICsMSGRPSDetachRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMSGRPSDetachRx = _JnxMbgPgwPPV1ICsMSGRPSDetachRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 235),
    _JnxMbgPgwPPV1ICsMSGRPSDetachRx_Type()
)
jnxMbgPgwPPV1ICsMSGRPSDetachRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMSGRPSDetachRx.setStatus("current")
_JnxMbgPgwPPV1ICsMSGRPSDetachTx_Type = Counter64
_JnxMbgPgwPPV1ICsMSGRPSDetachTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMSGRPSDetachTx = _JnxMbgPgwPPV1ICsMSGRPSDetachTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 236),
    _JnxMbgPgwPPV1ICsMSGRPSDetachTx_Type()
)
jnxMbgPgwPPV1ICsMSGRPSDetachTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMSGRPSDetachTx.setStatus("current")
_JnxMbgPgwPPV1ICsMSNotGRPSRespRx_Type = Counter64
_JnxMbgPgwPPV1ICsMSNotGRPSRespRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMSNotGRPSRespRx = _JnxMbgPgwPPV1ICsMSNotGRPSRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 237),
    _JnxMbgPgwPPV1ICsMSNotGRPSRespRx_Type()
)
jnxMbgPgwPPV1ICsMSNotGRPSRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMSNotGRPSRespRx.setStatus("current")
_JnxMbgPgwPPV1ICsMSNotGRPSRespTx_Type = Counter64
_JnxMbgPgwPPV1ICsMSNotGRPSRespTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMSNotGRPSRespTx = _JnxMbgPgwPPV1ICsMSNotGRPSRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 238),
    _JnxMbgPgwPPV1ICsMSNotGRPSRespTx_Type()
)
jnxMbgPgwPPV1ICsMSNotGRPSRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMSNotGRPSRespTx.setStatus("current")
_JnxMbgPgwPPV1ICsMSRefusesRx_Type = Counter64
_JnxMbgPgwPPV1ICsMSRefusesRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMSRefusesRx = _JnxMbgPgwPPV1ICsMSRefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 239),
    _JnxMbgPgwPPV1ICsMSRefusesRx_Type()
)
jnxMbgPgwPPV1ICsMSRefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMSRefusesRx.setStatus("current")
_JnxMbgPgwPPV1ICsMSRefusesTx_Type = Counter64
_JnxMbgPgwPPV1ICsMSRefusesTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMSRefusesTx = _JnxMbgPgwPPV1ICsMSRefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 240),
    _JnxMbgPgwPPV1ICsMSRefusesTx_Type()
)
jnxMbgPgwPPV1ICsMSRefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMSRefusesTx.setStatus("current")
_JnxMbgPgwPPV1ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwPPV1ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsVerNotSuppRx = _JnxMbgPgwPPV1ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 241),
    _JnxMbgPgwPPV1ICsVerNotSuppRx_Type()
)
jnxMbgPgwPPV1ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwPPV1ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwPPV1ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsVerNotSuppTx = _JnxMbgPgwPPV1ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 242),
    _JnxMbgPgwPPV1ICsVerNotSuppTx_Type()
)
jnxMbgPgwPPV1ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwPPV1ICsNoResRx_Type = Counter64
_JnxMbgPgwPPV1ICsNoResRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNoResRx = _JnxMbgPgwPPV1ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 243),
    _JnxMbgPgwPPV1ICsNoResRx_Type()
)
jnxMbgPgwPPV1ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNoResRx.setStatus("current")
_JnxMbgPgwPPV1ICsNoResTx_Type = Counter64
_JnxMbgPgwPPV1ICsNoResTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNoResTx = _JnxMbgPgwPPV1ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 244),
    _JnxMbgPgwPPV1ICsNoResTx_Type()
)
jnxMbgPgwPPV1ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNoResTx.setStatus("current")
_JnxMbgPgwPPV1ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwPPV1ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsServNotSuppRx = _JnxMbgPgwPPV1ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 245),
    _JnxMbgPgwPPV1ICsServNotSuppRx_Type()
)
jnxMbgPgwPPV1ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwPPV1ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwPPV1ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsServNotSuppTx = _JnxMbgPgwPPV1ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 246),
    _JnxMbgPgwPPV1ICsServNotSuppTx_Type()
)
jnxMbgPgwPPV1ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwPPV1ICsManIEIncrtRx_Type = Counter64
_JnxMbgPgwPPV1ICsManIEIncrtRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsManIEIncrtRx = _JnxMbgPgwPPV1ICsManIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 247),
    _JnxMbgPgwPPV1ICsManIEIncrtRx_Type()
)
jnxMbgPgwPPV1ICsManIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsManIEIncrtRx.setStatus("current")
_JnxMbgPgwPPV1ICsManIEIncrtTx_Type = Counter64
_JnxMbgPgwPPV1ICsManIEIncrtTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsManIEIncrtTx = _JnxMbgPgwPPV1ICsManIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 248),
    _JnxMbgPgwPPV1ICsManIEIncrtTx_Type()
)
jnxMbgPgwPPV1ICsManIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsManIEIncrtTx.setStatus("current")
_JnxMbgPgwPPV1ICsManIEMissRx_Type = Counter64
_JnxMbgPgwPPV1ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsManIEMissRx = _JnxMbgPgwPPV1ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 249),
    _JnxMbgPgwPPV1ICsManIEMissRx_Type()
)
jnxMbgPgwPPV1ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsManIEMissRx.setStatus("current")
_JnxMbgPgwPPV1ICsManIEMissTx_Type = Counter64
_JnxMbgPgwPPV1ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsManIEMissTx = _JnxMbgPgwPPV1ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 250),
    _JnxMbgPgwPPV1ICsManIEMissTx_Type()
)
jnxMbgPgwPPV1ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsManIEMissTx.setStatus("current")
_JnxMbgPgwPPV1ICsOptIEIncrtRx_Type = Counter64
_JnxMbgPgwPPV1ICsOptIEIncrtRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsOptIEIncrtRx = _JnxMbgPgwPPV1ICsOptIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 251),
    _JnxMbgPgwPPV1ICsOptIEIncrtRx_Type()
)
jnxMbgPgwPPV1ICsOptIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsOptIEIncrtRx.setStatus("current")
_JnxMbgPgwPPV1ICsOptIEIncrtTx_Type = Counter64
_JnxMbgPgwPPV1ICsOptIEIncrtTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsOptIEIncrtTx = _JnxMbgPgwPPV1ICsOptIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 252),
    _JnxMbgPgwPPV1ICsOptIEIncrtTx_Type()
)
jnxMbgPgwPPV1ICsOptIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsOptIEIncrtTx.setStatus("current")
_JnxMbgPgwPPV1ICsSysFailRx_Type = Counter64
_JnxMbgPgwPPV1ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSysFailRx = _JnxMbgPgwPPV1ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 253),
    _JnxMbgPgwPPV1ICsSysFailRx_Type()
)
jnxMbgPgwPPV1ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSysFailRx.setStatus("current")
_JnxMbgPgwPPV1ICsSysFailTx_Type = Counter64
_JnxMbgPgwPPV1ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSysFailTx = _JnxMbgPgwPPV1ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 254),
    _JnxMbgPgwPPV1ICsSysFailTx_Type()
)
jnxMbgPgwPPV1ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSysFailTx.setStatus("current")
_JnxMbgPgwPPV1ICsRoamRestrictRx_Type = Counter64
_JnxMbgPgwPPV1ICsRoamRestrictRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsRoamRestrictRx = _JnxMbgPgwPPV1ICsRoamRestrictRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 255),
    _JnxMbgPgwPPV1ICsRoamRestrictRx_Type()
)
jnxMbgPgwPPV1ICsRoamRestrictRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsRoamRestrictRx.setStatus("current")
_JnxMbgPgwPPV1ICsRoamRestrictTx_Type = Counter64
_JnxMbgPgwPPV1ICsRoamRestrictTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsRoamRestrictTx = _JnxMbgPgwPPV1ICsRoamRestrictTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 256),
    _JnxMbgPgwPPV1ICsRoamRestrictTx_Type()
)
jnxMbgPgwPPV1ICsRoamRestrictTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsRoamRestrictTx.setStatus("current")
_JnxMbgPgwPPV1ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwPPV1ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsPTMSISigMMRx = _JnxMbgPgwPPV1ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 257),
    _JnxMbgPgwPPV1ICsPTMSISigMMRx_Type()
)
jnxMbgPgwPPV1ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwPPV1ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwPPV1ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsPTMSISigMMTx = _JnxMbgPgwPPV1ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 258),
    _JnxMbgPgwPPV1ICsPTMSISigMMTx_Type()
)
jnxMbgPgwPPV1ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwPPV1ICsGPRSConnSuppRx_Type = Counter64
_JnxMbgPgwPPV1ICsGPRSConnSuppRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsGPRSConnSuppRx = _JnxMbgPgwPPV1ICsGPRSConnSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 259),
    _JnxMbgPgwPPV1ICsGPRSConnSuppRx_Type()
)
jnxMbgPgwPPV1ICsGPRSConnSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsGPRSConnSuppRx.setStatus("current")
_JnxMbgPgwPPV1ICsGPRSConnSuppTx_Type = Counter64
_JnxMbgPgwPPV1ICsGPRSConnSuppTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsGPRSConnSuppTx = _JnxMbgPgwPPV1ICsGPRSConnSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 260),
    _JnxMbgPgwPPV1ICsGPRSConnSuppTx_Type()
)
jnxMbgPgwPPV1ICsGPRSConnSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsGPRSConnSuppTx.setStatus("current")
_JnxMbgPgwPPV1ICsAuthFailRx_Type = Counter64
_JnxMbgPgwPPV1ICsAuthFailRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsAuthFailRx = _JnxMbgPgwPPV1ICsAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 261),
    _JnxMbgPgwPPV1ICsAuthFailRx_Type()
)
jnxMbgPgwPPV1ICsAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsAuthFailRx.setStatus("current")
_JnxMbgPgwPPV1ICsAuthFailTx_Type = Counter64
_JnxMbgPgwPPV1ICsAuthFailTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsAuthFailTx = _JnxMbgPgwPPV1ICsAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 262),
    _JnxMbgPgwPPV1ICsAuthFailTx_Type()
)
jnxMbgPgwPPV1ICsAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsAuthFailTx.setStatus("current")
_JnxMbgPgwPPV1ICsUserAuthFailRx_Type = Counter64
_JnxMbgPgwPPV1ICsUserAuthFailRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsUserAuthFailRx = _JnxMbgPgwPPV1ICsUserAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 263),
    _JnxMbgPgwPPV1ICsUserAuthFailRx_Type()
)
jnxMbgPgwPPV1ICsUserAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsUserAuthFailRx.setStatus("current")
_JnxMbgPgwPPV1ICsUserAuthFailTx_Type = Counter64
_JnxMbgPgwPPV1ICsUserAuthFailTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsUserAuthFailTx = _JnxMbgPgwPPV1ICsUserAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 264),
    _JnxMbgPgwPPV1ICsUserAuthFailTx_Type()
)
jnxMbgPgwPPV1ICsUserAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsUserAuthFailTx.setStatus("current")
_JnxMbgPgwPPV1ICsCtxNotFndRx_Type = Counter64
_JnxMbgPgwPPV1ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsCtxNotFndRx = _JnxMbgPgwPPV1ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 265),
    _JnxMbgPgwPPV1ICsCtxNotFndRx_Type()
)
jnxMbgPgwPPV1ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsCtxNotFndRx.setStatus("current")
_JnxMbgPgwPPV1ICsCtxNotFndTx_Type = Counter64
_JnxMbgPgwPPV1ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsCtxNotFndTx = _JnxMbgPgwPPV1ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 266),
    _JnxMbgPgwPPV1ICsCtxNotFndTx_Type()
)
jnxMbgPgwPPV1ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsCtxNotFndTx.setStatus("current")
_JnxMbgPgwPPV1ICsAllDynPDPAdRx_Type = Counter64
_JnxMbgPgwPPV1ICsAllDynPDPAdRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsAllDynPDPAdRx = _JnxMbgPgwPPV1ICsAllDynPDPAdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 267),
    _JnxMbgPgwPPV1ICsAllDynPDPAdRx_Type()
)
jnxMbgPgwPPV1ICsAllDynPDPAdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsAllDynPDPAdRx.setStatus("current")
_JnxMbgPgwPPV1ICsAllDynPDPAdTx_Type = Counter64
_JnxMbgPgwPPV1ICsAllDynPDPAdTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsAllDynPDPAdTx = _JnxMbgPgwPPV1ICsAllDynPDPAdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 268),
    _JnxMbgPgwPPV1ICsAllDynPDPAdTx_Type()
)
jnxMbgPgwPPV1ICsAllDynPDPAdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsAllDynPDPAdTx.setStatus("current")
_JnxMbgPgwPPV1ICsNoMemRx_Type = Counter64
_JnxMbgPgwPPV1ICsNoMemRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNoMemRx = _JnxMbgPgwPPV1ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 269),
    _JnxMbgPgwPPV1ICsNoMemRx_Type()
)
jnxMbgPgwPPV1ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNoMemRx.setStatus("current")
_JnxMbgPgwPPV1ICsNoMemTx_Type = Counter64
_JnxMbgPgwPPV1ICsNoMemTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNoMemTx = _JnxMbgPgwPPV1ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 270),
    _JnxMbgPgwPPV1ICsNoMemTx_Type()
)
jnxMbgPgwPPV1ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNoMemTx.setStatus("current")
_JnxMbgPgwPPV1ICsRelocFailRx_Type = Counter64
_JnxMbgPgwPPV1ICsRelocFailRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsRelocFailRx = _JnxMbgPgwPPV1ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 271),
    _JnxMbgPgwPPV1ICsRelocFailRx_Type()
)
jnxMbgPgwPPV1ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsRelocFailRx.setStatus("current")
_JnxMbgPgwPPV1ICsRelocFailTx_Type = Counter64
_JnxMbgPgwPPV1ICsRelocFailTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsRelocFailTx = _JnxMbgPgwPPV1ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 272),
    _JnxMbgPgwPPV1ICsRelocFailTx_Type()
)
jnxMbgPgwPPV1ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsRelocFailTx.setStatus("current")
_JnxMbgPgwPPV1ICsUnkManExhdrRx_Type = Counter64
_JnxMbgPgwPPV1ICsUnkManExhdrRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsUnkManExhdrRx = _JnxMbgPgwPPV1ICsUnkManExhdrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 273),
    _JnxMbgPgwPPV1ICsUnkManExhdrRx_Type()
)
jnxMbgPgwPPV1ICsUnkManExhdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsUnkManExhdrRx.setStatus("current")
_JnxMbgPgwPPV1ICsUnkManExhdrTx_Type = Counter64
_JnxMbgPgwPPV1ICsUnkManExhdrTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsUnkManExhdrTx = _JnxMbgPgwPPV1ICsUnkManExhdrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 274),
    _JnxMbgPgwPPV1ICsUnkManExhdrTx_Type()
)
jnxMbgPgwPPV1ICsUnkManExhdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsUnkManExhdrTx.setStatus("current")
_JnxMbgPgwPPV1ICsSMANTTFTEr1Rx_Type = Counter64
_JnxMbgPgwPPV1ICsSMANTTFTEr1Rx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSMANTTFTEr1Rx = _JnxMbgPgwPPV1ICsSMANTTFTEr1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 275),
    _JnxMbgPgwPPV1ICsSMANTTFTEr1Rx_Type()
)
jnxMbgPgwPPV1ICsSMANTTFTEr1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSMANTTFTEr1Rx.setStatus("current")
_JnxMbgPgwPPV1ICsSMANTTFTEr1Tx_Type = Counter64
_JnxMbgPgwPPV1ICsSMANTTFTEr1Tx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSMANTTFTEr1Tx = _JnxMbgPgwPPV1ICsSMANTTFTEr1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 276),
    _JnxMbgPgwPPV1ICsSMANTTFTEr1Tx_Type()
)
jnxMbgPgwPPV1ICsSMANTTFTEr1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSMANTTFTEr1Tx.setStatus("current")
_JnxMbgPgwPPV1ICsSYNTFTErr2Rx_Type = Counter64
_JnxMbgPgwPPV1ICsSYNTFTErr2Rx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSYNTFTErr2Rx = _JnxMbgPgwPPV1ICsSYNTFTErr2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 277),
    _JnxMbgPgwPPV1ICsSYNTFTErr2Rx_Type()
)
jnxMbgPgwPPV1ICsSYNTFTErr2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSYNTFTErr2Rx.setStatus("current")
_JnxMbgPgwPPV1ICsSYNTFTErr2Tx_Type = Counter64
_JnxMbgPgwPPV1ICsSYNTFTErr2Tx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSYNTFTErr2Tx = _JnxMbgPgwPPV1ICsSYNTFTErr2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 278),
    _JnxMbgPgwPPV1ICsSYNTFTErr2Tx_Type()
)
jnxMbgPgwPPV1ICsSYNTFTErr2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSYNTFTErr2Tx.setStatus("current")
_JnxMbgPgwPPV1ICsSMNTPkFlEr1Rx_Type = Counter64
_JnxMbgPgwPPV1ICsSMNTPkFlEr1Rx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSMNTPkFlEr1Rx = _JnxMbgPgwPPV1ICsSMNTPkFlEr1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 279),
    _JnxMbgPgwPPV1ICsSMNTPkFlEr1Rx_Type()
)
jnxMbgPgwPPV1ICsSMNTPkFlEr1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSMNTPkFlEr1Rx.setStatus("current")
_JnxMbgPgwPPV1ICsSMNTPkFlEr1Tx_Type = Counter64
_JnxMbgPgwPPV1ICsSMNTPkFlEr1Tx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSMNTPkFlEr1Tx = _JnxMbgPgwPPV1ICsSMNTPkFlEr1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 280),
    _JnxMbgPgwPPV1ICsSMNTPkFlEr1Tx_Type()
)
jnxMbgPgwPPV1ICsSMNTPkFlEr1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSMNTPkFlEr1Tx.setStatus("current")
_JnxMbgPgwPPV1ICsSYNPkFlErr2Rx_Type = Counter64
_JnxMbgPgwPPV1ICsSYNPkFlErr2Rx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSYNPkFlErr2Rx = _JnxMbgPgwPPV1ICsSYNPkFlErr2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 281),
    _JnxMbgPgwPPV1ICsSYNPkFlErr2Rx_Type()
)
jnxMbgPgwPPV1ICsSYNPkFlErr2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSYNPkFlErr2Rx.setStatus("current")
_JnxMbgPgwPPV1ICsSYNPkFlErr2Tx_Type = Counter64
_JnxMbgPgwPPV1ICsSYNPkFlErr2Tx_Object = MibTableColumn
jnxMbgPgwPPV1ICsSYNPkFlErr2Tx = _JnxMbgPgwPPV1ICsSYNPkFlErr2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 282),
    _JnxMbgPgwPPV1ICsSYNPkFlErr2Tx_Type()
)
jnxMbgPgwPPV1ICsSYNPkFlErr2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsSYNPkFlErr2Tx.setStatus("current")
_JnxMbgPgwPPV1ICsMissUnknAPNRx_Type = Counter64
_JnxMbgPgwPPV1ICsMissUnknAPNRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMissUnknAPNRx = _JnxMbgPgwPPV1ICsMissUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 283),
    _JnxMbgPgwPPV1ICsMissUnknAPNRx_Type()
)
jnxMbgPgwPPV1ICsMissUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMissUnknAPNRx.setStatus("current")
_JnxMbgPgwPPV1ICsMissUnknAPNTx_Type = Counter64
_JnxMbgPgwPPV1ICsMissUnknAPNTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsMissUnknAPNTx = _JnxMbgPgwPPV1ICsMissUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 284),
    _JnxMbgPgwPPV1ICsMissUnknAPNTx_Type()
)
jnxMbgPgwPPV1ICsMissUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsMissUnknAPNTx.setStatus("current")
_JnxMbgPgwPPV1ICsUnknPDPAdRx_Type = Counter64
_JnxMbgPgwPPV1ICsUnknPDPAdRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsUnknPDPAdRx = _JnxMbgPgwPPV1ICsUnknPDPAdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 285),
    _JnxMbgPgwPPV1ICsUnknPDPAdRx_Type()
)
jnxMbgPgwPPV1ICsUnknPDPAdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsUnknPDPAdRx.setStatus("current")
_JnxMbgPgwPPV1ICsUnknPDPAdTx_Type = Counter64
_JnxMbgPgwPPV1ICsUnknPDPAdTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsUnknPDPAdTx = _JnxMbgPgwPPV1ICsUnknPDPAdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 286),
    _JnxMbgPgwPPV1ICsUnknPDPAdTx_Type()
)
jnxMbgPgwPPV1ICsUnknPDPAdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsUnknPDPAdTx.setStatus("current")
_JnxMbgPgwPPV1ICsNoTFTCtxExRx_Type = Counter64
_JnxMbgPgwPPV1ICsNoTFTCtxExRx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNoTFTCtxExRx = _JnxMbgPgwPPV1ICsNoTFTCtxExRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 287),
    _JnxMbgPgwPPV1ICsNoTFTCtxExRx_Type()
)
jnxMbgPgwPPV1ICsNoTFTCtxExRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNoTFTCtxExRx.setStatus("current")
_JnxMbgPgwPPV1ICsNoTFTCtxExTx_Type = Counter64
_JnxMbgPgwPPV1ICsNoTFTCtxExTx_Object = MibTableColumn
jnxMbgPgwPPV1ICsNoTFTCtxExTx = _JnxMbgPgwPPV1ICsNoTFTCtxExTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 288),
    _JnxMbgPgwPPV1ICsNoTFTCtxExTx_Type()
)
jnxMbgPgwPPV1ICsNoTFTCtxExTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1ICsNoTFTCtxExTx.setStatus("current")
_JnxMbgPgwPPV0ProtocolErrRx_Type = Counter64
_JnxMbgPgwPPV0ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwPPV0ProtocolErrRx = _JnxMbgPgwPPV0ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 289),
    _JnxMbgPgwPPV0ProtocolErrRx_Type()
)
jnxMbgPgwPPV0ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ProtocolErrRx.setStatus("current")
_JnxMbgPgwPPV0UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwPPV0UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwPPV0UnSupportedMsgRx = _JnxMbgPgwPPV0UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 290),
    _JnxMbgPgwPPV0UnSupportedMsgRx_Type()
)
jnxMbgPgwPPV0UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwPPV0T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwPPV0T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwPPV0T3RespTmrExpRx = _JnxMbgPgwPPV0T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 291),
    _JnxMbgPgwPPV0T3RespTmrExpRx_Type()
)
jnxMbgPgwPPV0T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwPPV0GlbNumMsgRx_Type = Counter64
_JnxMbgPgwPPV0GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNumMsgRx = _JnxMbgPgwPPV0GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 292),
    _JnxMbgPgwPPV0GlbNumMsgRx_Type()
)
jnxMbgPgwPPV0GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNumMsgRx.setStatus("current")
_JnxMbgPgwPPV0GlbNumMsgTx_Type = Counter64
_JnxMbgPgwPPV0GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNumMsgTx = _JnxMbgPgwPPV0GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 293),
    _JnxMbgPgwPPV0GlbNumMsgTx_Type()
)
jnxMbgPgwPPV0GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNumMsgTx.setStatus("current")
_JnxMbgPgwPPV0GlbNumBytesRx_Type = Counter64
_JnxMbgPgwPPV0GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNumBytesRx = _JnxMbgPgwPPV0GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 294),
    _JnxMbgPgwPPV0GlbNumBytesRx_Type()
)
jnxMbgPgwPPV0GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNumBytesRx.setStatus("current")
_JnxMbgPgwPPV0GlbNumBytesTx_Type = Counter64
_JnxMbgPgwPPV0GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNumBytesTx = _JnxMbgPgwPPV0GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 295),
    _JnxMbgPgwPPV0GlbNumBytesTx_Type()
)
jnxMbgPgwPPV0GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNumBytesTx.setStatus("current")
_JnxMbgPgwPPV0GlbEchoReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbEchoReqRx = _JnxMbgPgwPPV0GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 296),
    _JnxMbgPgwPPV0GlbEchoReqRx_Type()
)
jnxMbgPgwPPV0GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbEchoReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbEchoReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbEchoReqTx = _JnxMbgPgwPPV0GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 297),
    _JnxMbgPgwPPV0GlbEchoReqTx_Type()
)
jnxMbgPgwPPV0GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbEchoReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbEchoRespRx_Type = Counter64
_JnxMbgPgwPPV0GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbEchoRespRx = _JnxMbgPgwPPV0GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 298),
    _JnxMbgPgwPPV0GlbEchoRespRx_Type()
)
jnxMbgPgwPPV0GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbEchoRespRx.setStatus("current")
_JnxMbgPgwPPV0GlbEchoRespTx_Type = Counter64
_JnxMbgPgwPPV0GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbEchoRespTx = _JnxMbgPgwPPV0GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 299),
    _JnxMbgPgwPPV0GlbEchoRespTx_Type()
)
jnxMbgPgwPPV0GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbEchoRespTx.setStatus("current")
_JnxMbgPgwPPV0GlbVerNotSupRx_Type = Counter64
_JnxMbgPgwPPV0GlbVerNotSupRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbVerNotSupRx = _JnxMbgPgwPPV0GlbVerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 300),
    _JnxMbgPgwPPV0GlbVerNotSupRx_Type()
)
jnxMbgPgwPPV0GlbVerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbVerNotSupRx.setStatus("current")
_JnxMbgPgwPPV0GlbVerNotSupTx_Type = Counter64
_JnxMbgPgwPPV0GlbVerNotSupTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbVerNotSupTx = _JnxMbgPgwPPV0GlbVerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 301),
    _JnxMbgPgwPPV0GlbVerNotSupTx_Type()
)
jnxMbgPgwPPV0GlbVerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbVerNotSupTx.setStatus("current")
_JnxMbgPgwPPV0GlbCrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbCrtPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrtPdpCxtReqRx = _JnxMbgPgwPPV0GlbCrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 302),
    _JnxMbgPgwPPV0GlbCrtPdpCxtReqRx_Type()
)
jnxMbgPgwPPV0GlbCrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrtPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbCrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbCrtPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrtPdpCxtReqTx = _JnxMbgPgwPPV0GlbCrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 303),
    _JnxMbgPgwPPV0GlbCrtPdpCxtReqTx_Type()
)
jnxMbgPgwPPV0GlbCrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrtPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbCrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbCrtPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrtPdpCxtRspRx = _JnxMbgPgwPPV0GlbCrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 304),
    _JnxMbgPgwPPV0GlbCrtPdpCxtRspRx_Type()
)
jnxMbgPgwPPV0GlbCrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrtPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbCrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbCrtPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrtPdpCxtRspTx = _JnxMbgPgwPPV0GlbCrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 305),
    _JnxMbgPgwPPV0GlbCrtPdpCxtRspTx_Type()
)
jnxMbgPgwPPV0GlbCrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrtPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbUpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbUpdPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbUpdPdpCxtReqRx = _JnxMbgPgwPPV0GlbUpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 306),
    _JnxMbgPgwPPV0GlbUpdPdpCxtReqRx_Type()
)
jnxMbgPgwPPV0GlbUpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbUpdPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbUpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbUpdPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbUpdPdpCxtReqTx = _JnxMbgPgwPPV0GlbUpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 307),
    _JnxMbgPgwPPV0GlbUpdPdpCxtReqTx_Type()
)
jnxMbgPgwPPV0GlbUpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbUpdPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbUpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbUpdPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbUpdPdpCxtRspRx = _JnxMbgPgwPPV0GlbUpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 308),
    _JnxMbgPgwPPV0GlbUpdPdpCxtRspRx_Type()
)
jnxMbgPgwPPV0GlbUpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbUpdPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbUpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbUpdPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbUpdPdpCxtRspTx = _JnxMbgPgwPPV0GlbUpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 309),
    _JnxMbgPgwPPV0GlbUpdPdpCxtRspTx_Type()
)
jnxMbgPgwPPV0GlbUpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbUpdPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbDelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbDelPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDelPdpCxtReqRx = _JnxMbgPgwPPV0GlbDelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 310),
    _JnxMbgPgwPPV0GlbDelPdpCxtReqRx_Type()
)
jnxMbgPgwPPV0GlbDelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDelPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbDelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbDelPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDelPdpCxtReqTx = _JnxMbgPgwPPV0GlbDelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 311),
    _JnxMbgPgwPPV0GlbDelPdpCxtReqTx_Type()
)
jnxMbgPgwPPV0GlbDelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDelPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbDelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbDelPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDelPdpCxtRspRx = _JnxMbgPgwPPV0GlbDelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 312),
    _JnxMbgPgwPPV0GlbDelPdpCxtRspRx_Type()
)
jnxMbgPgwPPV0GlbDelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDelPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbDelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbDelPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDelPdpCxtRspTx = _JnxMbgPgwPPV0GlbDelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 313),
    _JnxMbgPgwPPV0GlbDelPdpCxtRspTx_Type()
)
jnxMbgPgwPPV0GlbDelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDelPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbCrAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbCrAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrAAPdpCxtReqRx = _JnxMbgPgwPPV0GlbCrAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 314),
    _JnxMbgPgwPPV0GlbCrAAPdpCxtReqRx_Type()
)
jnxMbgPgwPPV0GlbCrAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbCrAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbCrAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrAAPdpCxtReqTx = _JnxMbgPgwPPV0GlbCrAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 315),
    _JnxMbgPgwPPV0GlbCrAAPdpCxtReqTx_Type()
)
jnxMbgPgwPPV0GlbCrAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbCrAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbCrAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrAAPdpCxtRspRx = _JnxMbgPgwPPV0GlbCrAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 316),
    _JnxMbgPgwPPV0GlbCrAAPdpCxtRspRx_Type()
)
jnxMbgPgwPPV0GlbCrAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbCrAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbCrAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbCrAAPdpCxtRspTx = _JnxMbgPgwPPV0GlbCrAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 317),
    _JnxMbgPgwPPV0GlbCrAAPdpCxtRspTx_Type()
)
jnxMbgPgwPPV0GlbCrAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbCrAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbDlAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbDlAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDlAAPdpCxtReqRx = _JnxMbgPgwPPV0GlbDlAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 318),
    _JnxMbgPgwPPV0GlbDlAAPdpCxtReqRx_Type()
)
jnxMbgPgwPPV0GlbDlAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDlAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbDlAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbDlAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDlAAPdpCxtReqTx = _JnxMbgPgwPPV0GlbDlAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 319),
    _JnxMbgPgwPPV0GlbDlAAPdpCxtReqTx_Type()
)
jnxMbgPgwPPV0GlbDlAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDlAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbDlAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbDlAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDlAAPdpCxtRspRx = _JnxMbgPgwPPV0GlbDlAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 320),
    _JnxMbgPgwPPV0GlbDlAAPdpCxtRspRx_Type()
)
jnxMbgPgwPPV0GlbDlAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDlAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbDlAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbDlAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbDlAAPdpCxtRspTx = _JnxMbgPgwPPV0GlbDlAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 321),
    _JnxMbgPgwPPV0GlbDlAAPdpCxtRspTx_Type()
)
jnxMbgPgwPPV0GlbDlAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbDlAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbErrorIndRx_Type = Counter64
_JnxMbgPgwPPV0GlbErrorIndRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbErrorIndRx = _JnxMbgPgwPPV0GlbErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 322),
    _JnxMbgPgwPPV0GlbErrorIndRx_Type()
)
jnxMbgPgwPPV0GlbErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbErrorIndRx.setStatus("current")
_JnxMbgPgwPPV0GlbErrorIndTx_Type = Counter64
_JnxMbgPgwPPV0GlbErrorIndTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbErrorIndTx = _JnxMbgPgwPPV0GlbErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 323),
    _JnxMbgPgwPPV0GlbErrorIndTx_Type()
)
jnxMbgPgwPPV0GlbErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbErrorIndTx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifReqRx = _JnxMbgPgwPPV0GlbNotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 324),
    _JnxMbgPgwPPV0GlbNotifReqRx_Type()
)
jnxMbgPgwPPV0GlbNotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifReqTx = _JnxMbgPgwPPV0GlbNotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 325),
    _JnxMbgPgwPPV0GlbNotifReqTx_Type()
)
jnxMbgPgwPPV0GlbNotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifRspRx = _JnxMbgPgwPPV0GlbNotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 326),
    _JnxMbgPgwPPV0GlbNotifRspRx_Type()
)
jnxMbgPgwPPV0GlbNotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifRspTx = _JnxMbgPgwPPV0GlbNotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 327),
    _JnxMbgPgwPPV0GlbNotifRspTx_Type()
)
jnxMbgPgwPPV0GlbNotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifRejReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifRejReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifRejReqRx = _JnxMbgPgwPPV0GlbNotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 328),
    _JnxMbgPgwPPV0GlbNotifRejReqRx_Type()
)
jnxMbgPgwPPV0GlbNotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifRejReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifRejReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifRejReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifRejReqTx = _JnxMbgPgwPPV0GlbNotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 329),
    _JnxMbgPgwPPV0GlbNotifRejReqTx_Type()
)
jnxMbgPgwPPV0GlbNotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifRejReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifRejRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifRejRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifRejRspRx = _JnxMbgPgwPPV0GlbNotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 330),
    _JnxMbgPgwPPV0GlbNotifRejRspRx_Type()
)
jnxMbgPgwPPV0GlbNotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifRejRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbNotifRejRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbNotifRejRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotifRejRspTx = _JnxMbgPgwPPV0GlbNotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 331),
    _JnxMbgPgwPPV0GlbNotifRejRspTx_Type()
)
jnxMbgPgwPPV0GlbNotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotifRejRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbRtInfReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbRtInfReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbRtInfReqRx = _JnxMbgPgwPPV0GlbRtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 332),
    _JnxMbgPgwPPV0GlbRtInfReqRx_Type()
)
jnxMbgPgwPPV0GlbRtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbRtInfReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbRtInfReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbRtInfReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbRtInfReqTx = _JnxMbgPgwPPV0GlbRtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 333),
    _JnxMbgPgwPPV0GlbRtInfReqTx_Type()
)
jnxMbgPgwPPV0GlbRtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbRtInfReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbRtInfRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbRtInfRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbRtInfRspRx = _JnxMbgPgwPPV0GlbRtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 334),
    _JnxMbgPgwPPV0GlbRtInfRspRx_Type()
)
jnxMbgPgwPPV0GlbRtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbRtInfRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbRtInfRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbRtInfRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbRtInfRspTx = _JnxMbgPgwPPV0GlbRtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 335),
    _JnxMbgPgwPPV0GlbRtInfRspTx_Type()
)
jnxMbgPgwPPV0GlbRtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbRtInfRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbFailRptReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbFailRptReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbFailRptReqRx = _JnxMbgPgwPPV0GlbFailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 336),
    _JnxMbgPgwPPV0GlbFailRptReqRx_Type()
)
jnxMbgPgwPPV0GlbFailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbFailRptReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbFailRptReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbFailRptReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbFailRptReqTx = _JnxMbgPgwPPV0GlbFailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 337),
    _JnxMbgPgwPPV0GlbFailRptReqTx_Type()
)
jnxMbgPgwPPV0GlbFailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbFailRptReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbFailRptRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbFailRptRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbFailRptRspRx = _JnxMbgPgwPPV0GlbFailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 338),
    _JnxMbgPgwPPV0GlbFailRptRspRx_Type()
)
jnxMbgPgwPPV0GlbFailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbFailRptRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbFailRptRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbFailRptRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbFailRptRspTx = _JnxMbgPgwPPV0GlbFailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 339),
    _JnxMbgPgwPPV0GlbFailRptRspTx_Type()
)
jnxMbgPgwPPV0GlbFailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbFailRptRspTx.setStatus("current")
_JnxMbgPgwPPV0GlbNotMSPresReqRx_Type = Counter64
_JnxMbgPgwPPV0GlbNotMSPresReqRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotMSPresReqRx = _JnxMbgPgwPPV0GlbNotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 340),
    _JnxMbgPgwPPV0GlbNotMSPresReqRx_Type()
)
jnxMbgPgwPPV0GlbNotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotMSPresReqRx.setStatus("current")
_JnxMbgPgwPPV0GlbNotMSPresReqTx_Type = Counter64
_JnxMbgPgwPPV0GlbNotMSPresReqTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotMSPresReqTx = _JnxMbgPgwPPV0GlbNotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 341),
    _JnxMbgPgwPPV0GlbNotMSPresReqTx_Type()
)
jnxMbgPgwPPV0GlbNotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotMSPresReqTx.setStatus("current")
_JnxMbgPgwPPV0GlbNotMSPresRspRx_Type = Counter64
_JnxMbgPgwPPV0GlbNotMSPresRspRx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotMSPresRspRx = _JnxMbgPgwPPV0GlbNotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 342),
    _JnxMbgPgwPPV0GlbNotMSPresRspRx_Type()
)
jnxMbgPgwPPV0GlbNotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotMSPresRspRx.setStatus("current")
_JnxMbgPgwPPV0GlbNotMSPresRspTx_Type = Counter64
_JnxMbgPgwPPV0GlbNotMSPresRspTx_Object = MibTableColumn
jnxMbgPgwPPV0GlbNotMSPresRspTx = _JnxMbgPgwPPV0GlbNotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 343),
    _JnxMbgPgwPPV0GlbNotMSPresRspTx_Type()
)
jnxMbgPgwPPV0GlbNotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0GlbNotMSPresRspTx.setStatus("current")
_JnxMbgPgwPPV0ICsReqAcceptedRx_Type = Counter64
_JnxMbgPgwPPV0ICsReqAcceptedRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsReqAcceptedRx = _JnxMbgPgwPPV0ICsReqAcceptedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 344),
    _JnxMbgPgwPPV0ICsReqAcceptedRx_Type()
)
jnxMbgPgwPPV0ICsReqAcceptedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsReqAcceptedRx.setStatus("current")
_JnxMbgPgwPPV0ICsReqAcceptedTx_Type = Counter64
_JnxMbgPgwPPV0ICsReqAcceptedTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsReqAcceptedTx = _JnxMbgPgwPPV0ICsReqAcceptedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 345),
    _JnxMbgPgwPPV0ICsReqAcceptedTx_Type()
)
jnxMbgPgwPPV0ICsReqAcceptedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsReqAcceptedTx.setStatus("current")
_JnxMbgPgwPPV0ICsNonExistRx_Type = Counter64
_JnxMbgPgwPPV0ICsNonExistRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsNonExistRx = _JnxMbgPgwPPV0ICsNonExistRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 346),
    _JnxMbgPgwPPV0ICsNonExistRx_Type()
)
jnxMbgPgwPPV0ICsNonExistRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsNonExistRx.setStatus("current")
_JnxMbgPgwPPV0ICsNonExistTx_Type = Counter64
_JnxMbgPgwPPV0ICsNonExistTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsNonExistTx = _JnxMbgPgwPPV0ICsNonExistTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 347),
    _JnxMbgPgwPPV0ICsNonExistTx_Type()
)
jnxMbgPgwPPV0ICsNonExistTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsNonExistTx.setStatus("current")
_JnxMbgPgwPPV0ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwPPV0ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsInvMsgFmtRx = _JnxMbgPgwPPV0ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 348),
    _JnxMbgPgwPPV0ICsInvMsgFmtRx_Type()
)
jnxMbgPgwPPV0ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwPPV0ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwPPV0ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsInvMsgFmtTx = _JnxMbgPgwPPV0ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 349),
    _JnxMbgPgwPPV0ICsInvMsgFmtTx_Type()
)
jnxMbgPgwPPV0ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwPPV0ICsIMSINotKnownRx_Type = Counter64
_JnxMbgPgwPPV0ICsIMSINotKnownRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsIMSINotKnownRx = _JnxMbgPgwPPV0ICsIMSINotKnownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 350),
    _JnxMbgPgwPPV0ICsIMSINotKnownRx_Type()
)
jnxMbgPgwPPV0ICsIMSINotKnownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsIMSINotKnownRx.setStatus("current")
_JnxMbgPgwPPV0ICsIMSINotKnownTx_Type = Counter64
_JnxMbgPgwPPV0ICsIMSINotKnownTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsIMSINotKnownTx = _JnxMbgPgwPPV0ICsIMSINotKnownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 351),
    _JnxMbgPgwPPV0ICsIMSINotKnownTx_Type()
)
jnxMbgPgwPPV0ICsIMSINotKnownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsIMSINotKnownTx.setStatus("current")
_JnxMbgPgwPPV0ICsMSGRPSDetachRx_Type = Counter64
_JnxMbgPgwPPV0ICsMSGRPSDetachRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsMSGRPSDetachRx = _JnxMbgPgwPPV0ICsMSGRPSDetachRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 352),
    _JnxMbgPgwPPV0ICsMSGRPSDetachRx_Type()
)
jnxMbgPgwPPV0ICsMSGRPSDetachRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsMSGRPSDetachRx.setStatus("current")
_JnxMbgPgwPPV0ICsMSGRPSDetachTx_Type = Counter64
_JnxMbgPgwPPV0ICsMSGRPSDetachTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsMSGRPSDetachTx = _JnxMbgPgwPPV0ICsMSGRPSDetachTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 353),
    _JnxMbgPgwPPV0ICsMSGRPSDetachTx_Type()
)
jnxMbgPgwPPV0ICsMSGRPSDetachTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsMSGRPSDetachTx.setStatus("current")
_JnxMbgPgwPPV0ICsMSNotGRPSRespRx_Type = Counter64
_JnxMbgPgwPPV0ICsMSNotGRPSRespRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsMSNotGRPSRespRx = _JnxMbgPgwPPV0ICsMSNotGRPSRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 354),
    _JnxMbgPgwPPV0ICsMSNotGRPSRespRx_Type()
)
jnxMbgPgwPPV0ICsMSNotGRPSRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsMSNotGRPSRespRx.setStatus("current")
_JnxMbgPgwPPV0ICsMSNotGRPSRespTx_Type = Counter64
_JnxMbgPgwPPV0ICsMSNotGRPSRespTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsMSNotGRPSRespTx = _JnxMbgPgwPPV0ICsMSNotGRPSRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 355),
    _JnxMbgPgwPPV0ICsMSNotGRPSRespTx_Type()
)
jnxMbgPgwPPV0ICsMSNotGRPSRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsMSNotGRPSRespTx.setStatus("current")
_JnxMbgPgwPPV0ICsMSRefusesRx_Type = Counter64
_JnxMbgPgwPPV0ICsMSRefusesRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsMSRefusesRx = _JnxMbgPgwPPV0ICsMSRefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 356),
    _JnxMbgPgwPPV0ICsMSRefusesRx_Type()
)
jnxMbgPgwPPV0ICsMSRefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsMSRefusesRx.setStatus("current")
_JnxMbgPgwPPV0ICsMSRefusesTx_Type = Counter64
_JnxMbgPgwPPV0ICsMSRefusesTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsMSRefusesTx = _JnxMbgPgwPPV0ICsMSRefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 357),
    _JnxMbgPgwPPV0ICsMSRefusesTx_Type()
)
jnxMbgPgwPPV0ICsMSRefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsMSRefusesTx.setStatus("current")
_JnxMbgPgwPPV0ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwPPV0ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsVerNotSuppRx = _JnxMbgPgwPPV0ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 358),
    _JnxMbgPgwPPV0ICsVerNotSuppRx_Type()
)
jnxMbgPgwPPV0ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwPPV0ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwPPV0ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsVerNotSuppTx = _JnxMbgPgwPPV0ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 359),
    _JnxMbgPgwPPV0ICsVerNotSuppTx_Type()
)
jnxMbgPgwPPV0ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwPPV0ICsNoResRx_Type = Counter64
_JnxMbgPgwPPV0ICsNoResRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsNoResRx = _JnxMbgPgwPPV0ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 360),
    _JnxMbgPgwPPV0ICsNoResRx_Type()
)
jnxMbgPgwPPV0ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsNoResRx.setStatus("current")
_JnxMbgPgwPPV0ICsNoResTx_Type = Counter64
_JnxMbgPgwPPV0ICsNoResTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsNoResTx = _JnxMbgPgwPPV0ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 361),
    _JnxMbgPgwPPV0ICsNoResTx_Type()
)
jnxMbgPgwPPV0ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsNoResTx.setStatus("current")
_JnxMbgPgwPPV0ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwPPV0ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsServNotSuppRx = _JnxMbgPgwPPV0ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 362),
    _JnxMbgPgwPPV0ICsServNotSuppRx_Type()
)
jnxMbgPgwPPV0ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwPPV0ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwPPV0ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsServNotSuppTx = _JnxMbgPgwPPV0ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 363),
    _JnxMbgPgwPPV0ICsServNotSuppTx_Type()
)
jnxMbgPgwPPV0ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwPPV0ICsManIEIncrtRx_Type = Counter64
_JnxMbgPgwPPV0ICsManIEIncrtRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsManIEIncrtRx = _JnxMbgPgwPPV0ICsManIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 364),
    _JnxMbgPgwPPV0ICsManIEIncrtRx_Type()
)
jnxMbgPgwPPV0ICsManIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsManIEIncrtRx.setStatus("current")
_JnxMbgPgwPPV0ICsManIEIncrtTx_Type = Counter64
_JnxMbgPgwPPV0ICsManIEIncrtTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsManIEIncrtTx = _JnxMbgPgwPPV0ICsManIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 365),
    _JnxMbgPgwPPV0ICsManIEIncrtTx_Type()
)
jnxMbgPgwPPV0ICsManIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsManIEIncrtTx.setStatus("current")
_JnxMbgPgwPPV0ICsManIEMissRx_Type = Counter64
_JnxMbgPgwPPV0ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsManIEMissRx = _JnxMbgPgwPPV0ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 366),
    _JnxMbgPgwPPV0ICsManIEMissRx_Type()
)
jnxMbgPgwPPV0ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsManIEMissRx.setStatus("current")
_JnxMbgPgwPPV0ICsManIEMissTx_Type = Counter64
_JnxMbgPgwPPV0ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsManIEMissTx = _JnxMbgPgwPPV0ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 367),
    _JnxMbgPgwPPV0ICsManIEMissTx_Type()
)
jnxMbgPgwPPV0ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsManIEMissTx.setStatus("current")
_JnxMbgPgwPPV0ICsOptIEIncrtRx_Type = Counter64
_JnxMbgPgwPPV0ICsOptIEIncrtRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsOptIEIncrtRx = _JnxMbgPgwPPV0ICsOptIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 368),
    _JnxMbgPgwPPV0ICsOptIEIncrtRx_Type()
)
jnxMbgPgwPPV0ICsOptIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsOptIEIncrtRx.setStatus("current")
_JnxMbgPgwPPV0ICsOptIEIncrtTx_Type = Counter64
_JnxMbgPgwPPV0ICsOptIEIncrtTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsOptIEIncrtTx = _JnxMbgPgwPPV0ICsOptIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 369),
    _JnxMbgPgwPPV0ICsOptIEIncrtTx_Type()
)
jnxMbgPgwPPV0ICsOptIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsOptIEIncrtTx.setStatus("current")
_JnxMbgPgwPPV0ICsSysFailRx_Type = Counter64
_JnxMbgPgwPPV0ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsSysFailRx = _JnxMbgPgwPPV0ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 370),
    _JnxMbgPgwPPV0ICsSysFailRx_Type()
)
jnxMbgPgwPPV0ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsSysFailRx.setStatus("current")
_JnxMbgPgwPPV0ICsSysFailTx_Type = Counter64
_JnxMbgPgwPPV0ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsSysFailTx = _JnxMbgPgwPPV0ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 371),
    _JnxMbgPgwPPV0ICsSysFailTx_Type()
)
jnxMbgPgwPPV0ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsSysFailTx.setStatus("current")
_JnxMbgPgwPPV0ICsRoamRestrictRx_Type = Counter64
_JnxMbgPgwPPV0ICsRoamRestrictRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsRoamRestrictRx = _JnxMbgPgwPPV0ICsRoamRestrictRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 372),
    _JnxMbgPgwPPV0ICsRoamRestrictRx_Type()
)
jnxMbgPgwPPV0ICsRoamRestrictRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsRoamRestrictRx.setStatus("current")
_JnxMbgPgwPPV0ICsRoamRestrictTx_Type = Counter64
_JnxMbgPgwPPV0ICsRoamRestrictTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsRoamRestrictTx = _JnxMbgPgwPPV0ICsRoamRestrictTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 373),
    _JnxMbgPgwPPV0ICsRoamRestrictTx_Type()
)
jnxMbgPgwPPV0ICsRoamRestrictTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsRoamRestrictTx.setStatus("current")
_JnxMbgPgwPPV0ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwPPV0ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsPTMSISigMMRx = _JnxMbgPgwPPV0ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 374),
    _JnxMbgPgwPPV0ICsPTMSISigMMRx_Type()
)
jnxMbgPgwPPV0ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwPPV0ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwPPV0ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsPTMSISigMMTx = _JnxMbgPgwPPV0ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 375),
    _JnxMbgPgwPPV0ICsPTMSISigMMTx_Type()
)
jnxMbgPgwPPV0ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwPPV0ICsGPRSConnSuppRx_Type = Counter64
_JnxMbgPgwPPV0ICsGPRSConnSuppRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsGPRSConnSuppRx = _JnxMbgPgwPPV0ICsGPRSConnSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 376),
    _JnxMbgPgwPPV0ICsGPRSConnSuppRx_Type()
)
jnxMbgPgwPPV0ICsGPRSConnSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsGPRSConnSuppRx.setStatus("current")
_JnxMbgPgwPPV0ICsGPRSConnSuppTx_Type = Counter64
_JnxMbgPgwPPV0ICsGPRSConnSuppTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsGPRSConnSuppTx = _JnxMbgPgwPPV0ICsGPRSConnSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 377),
    _JnxMbgPgwPPV0ICsGPRSConnSuppTx_Type()
)
jnxMbgPgwPPV0ICsGPRSConnSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsGPRSConnSuppTx.setStatus("current")
_JnxMbgPgwPPV0ICsAuthFailRx_Type = Counter64
_JnxMbgPgwPPV0ICsAuthFailRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsAuthFailRx = _JnxMbgPgwPPV0ICsAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 378),
    _JnxMbgPgwPPV0ICsAuthFailRx_Type()
)
jnxMbgPgwPPV0ICsAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsAuthFailRx.setStatus("current")
_JnxMbgPgwPPV0ICsAuthFailTx_Type = Counter64
_JnxMbgPgwPPV0ICsAuthFailTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsAuthFailTx = _JnxMbgPgwPPV0ICsAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 379),
    _JnxMbgPgwPPV0ICsAuthFailTx_Type()
)
jnxMbgPgwPPV0ICsAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsAuthFailTx.setStatus("current")
_JnxMbgPgwPPV0ICsUserAuthFailRx_Type = Counter64
_JnxMbgPgwPPV0ICsUserAuthFailRx_Object = MibTableColumn
jnxMbgPgwPPV0ICsUserAuthFailRx = _JnxMbgPgwPPV0ICsUserAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 380),
    _JnxMbgPgwPPV0ICsUserAuthFailRx_Type()
)
jnxMbgPgwPPV0ICsUserAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsUserAuthFailRx.setStatus("current")
_JnxMbgPgwPPV0ICsUserAuthFailTx_Type = Counter64
_JnxMbgPgwPPV0ICsUserAuthFailTx_Object = MibTableColumn
jnxMbgPgwPPV0ICsUserAuthFailTx = _JnxMbgPgwPPV0ICsUserAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 381),
    _JnxMbgPgwPPV0ICsUserAuthFailTx_Type()
)
jnxMbgPgwPPV0ICsUserAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV0ICsUserAuthFailTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsLclDetRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsLclDetRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsLclDetRx = _JnxMbgPgwPPGtpV2ICsLclDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 382),
    _JnxMbgPgwPPGtpV2ICsLclDetRx_Type()
)
jnxMbgPgwPPGtpV2ICsLclDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsLclDetRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsLclDetTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsLclDetTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsLclDetTx = _JnxMbgPgwPPGtpV2ICsLclDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 383),
    _JnxMbgPgwPPGtpV2ICsLclDetTx_Type()
)
jnxMbgPgwPPGtpV2ICsLclDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsLclDetTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsCmpDetRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsCmpDetRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsCmpDetRx = _JnxMbgPgwPPGtpV2ICsCmpDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 384),
    _JnxMbgPgwPPGtpV2ICsCmpDetRx_Type()
)
jnxMbgPgwPPGtpV2ICsCmpDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsCmpDetRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsCmpDetTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsCmpDetTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsCmpDetTx = _JnxMbgPgwPPGtpV2ICsCmpDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 385),
    _JnxMbgPgwPPGtpV2ICsCmpDetTx_Type()
)
jnxMbgPgwPPGtpV2ICsCmpDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsCmpDetTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsRATChgRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsRATChgRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsRATChgRx = _JnxMbgPgwPPGtpV2ICsRATChgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 386),
    _JnxMbgPgwPPGtpV2ICsRATChgRx_Type()
)
jnxMbgPgwPPGtpV2ICsRATChgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsRATChgRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsRATChgTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsRATChgTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsRATChgTx = _JnxMbgPgwPPGtpV2ICsRATChgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 387),
    _JnxMbgPgwPPGtpV2ICsRATChgTx_Type()
)
jnxMbgPgwPPGtpV2ICsRATChgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsRATChgTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsISRDeactRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsISRDeactRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsISRDeactRx = _JnxMbgPgwPPGtpV2ICsISRDeactRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 388),
    _JnxMbgPgwPPGtpV2ICsISRDeactRx_Type()
)
jnxMbgPgwPPGtpV2ICsISRDeactRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsISRDeactRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsISRDeactTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsISRDeactTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsISRDeactTx = _JnxMbgPgwPPGtpV2ICsISRDeactTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 389),
    _JnxMbgPgwPPGtpV2ICsISRDeactTx_Type()
)
jnxMbgPgwPPGtpV2ICsISRDeactTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsISRDeactTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsEIFRNCEnRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsEIFRNCEnRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsEIFRNCEnRx = _JnxMbgPgwPPGtpV2ICsEIFRNCEnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 390),
    _JnxMbgPgwPPGtpV2ICsEIFRNCEnRx_Type()
)
jnxMbgPgwPPGtpV2ICsEIFRNCEnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsEIFRNCEnRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsEIFRNCEnTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsEIFRNCEnTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsEIFRNCEnTx = _JnxMbgPgwPPGtpV2ICsEIFRNCEnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 391),
    _JnxMbgPgwPPGtpV2ICsEIFRNCEnTx_Type()
)
jnxMbgPgwPPGtpV2ICsEIFRNCEnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsEIFRNCEnTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsSemErTADRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsSemErTADRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsSemErTADRx = _JnxMbgPgwPPGtpV2ICsSemErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 392),
    _JnxMbgPgwPPGtpV2ICsSemErTADRx_Type()
)
jnxMbgPgwPPGtpV2ICsSemErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsSemErTADRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsSemErTADTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsSemErTADTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsSemErTADTx = _JnxMbgPgwPPGtpV2ICsSemErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 393),
    _JnxMbgPgwPPGtpV2ICsSemErTADTx_Type()
)
jnxMbgPgwPPGtpV2ICsSemErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsSemErTADTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsSynErTADRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsSynErTADRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsSynErTADRx = _JnxMbgPgwPPGtpV2ICsSynErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 394),
    _JnxMbgPgwPPGtpV2ICsSynErTADRx_Type()
)
jnxMbgPgwPPGtpV2ICsSynErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsSynErTADRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsSynErTADTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsSynErTADTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsSynErTADTx = _JnxMbgPgwPPGtpV2ICsSynErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 395),
    _JnxMbgPgwPPGtpV2ICsSynErTADTx_Type()
)
jnxMbgPgwPPGtpV2ICsSynErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsSynErTADTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsRMValRcvRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsRMValRcvRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsRMValRcvRx = _JnxMbgPgwPPGtpV2ICsRMValRcvRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 396),
    _JnxMbgPgwPPGtpV2ICsRMValRcvRx_Type()
)
jnxMbgPgwPPGtpV2ICsRMValRcvRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsRMValRcvRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsRMValRcvTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsRMValRcvTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsRMValRcvTx = _JnxMbgPgwPPGtpV2ICsRMValRcvTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 397),
    _JnxMbgPgwPPGtpV2ICsRMValRcvTx_Type()
)
jnxMbgPgwPPGtpV2ICsRMValRcvTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsRMValRcvTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsRPrNtRspRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsRPrNtRspRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsRPrNtRspRx = _JnxMbgPgwPPGtpV2ICsRPrNtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 398),
    _JnxMbgPgwPPGtpV2ICsRPrNtRspRx_Type()
)
jnxMbgPgwPPGtpV2ICsRPrNtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsRPrNtRspRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsRPrNtRspTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsRPrNtRspTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsRPrNtRspTx = _JnxMbgPgwPPGtpV2ICsRPrNtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 399),
    _JnxMbgPgwPPGtpV2ICsRPrNtRspTx_Type()
)
jnxMbgPgwPPGtpV2ICsRPrNtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsRPrNtRspTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsColNWReqRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsColNWReqRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsColNWReqRx = _JnxMbgPgwPPGtpV2ICsColNWReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 400),
    _JnxMbgPgwPPGtpV2ICsColNWReqRx_Type()
)
jnxMbgPgwPPGtpV2ICsColNWReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsColNWReqRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsColNWReqTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsColNWReqTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsColNWReqTx = _JnxMbgPgwPPGtpV2ICsColNWReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 401),
    _JnxMbgPgwPPGtpV2ICsColNWReqTx_Type()
)
jnxMbgPgwPPGtpV2ICsColNWReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsColNWReqTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsUnPgUESusRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsUnPgUESusRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsUnPgUESusRx = _JnxMbgPgwPPGtpV2ICsUnPgUESusRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 402),
    _JnxMbgPgwPPGtpV2ICsUnPgUESusRx_Type()
)
jnxMbgPgwPPGtpV2ICsUnPgUESusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsUnPgUESusRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsUnPgUESusTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsUnPgUESusTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsUnPgUESusTx = _JnxMbgPgwPPGtpV2ICsUnPgUESusTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 403),
    _JnxMbgPgwPPGtpV2ICsUnPgUESusTx_Type()
)
jnxMbgPgwPPGtpV2ICsUnPgUESusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsUnPgUESusTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsInvTotLenRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsInvTotLenRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsInvTotLenRx = _JnxMbgPgwPPGtpV2ICsInvTotLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 404),
    _JnxMbgPgwPPGtpV2ICsInvTotLenRx_Type()
)
jnxMbgPgwPPGtpV2ICsInvTotLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsInvTotLenRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsInvTotLenTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsInvTotLenTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsInvTotLenTx = _JnxMbgPgwPPGtpV2ICsInvTotLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 405),
    _JnxMbgPgwPPGtpV2ICsInvTotLenTx_Type()
)
jnxMbgPgwPPGtpV2ICsInvTotLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsInvTotLenTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsDtForNtSupRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsDtForNtSupRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsDtForNtSupRx = _JnxMbgPgwPPGtpV2ICsDtForNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 406),
    _JnxMbgPgwPPGtpV2ICsDtForNtSupRx_Type()
)
jnxMbgPgwPPGtpV2ICsDtForNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsDtForNtSupRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsDtForNtSupTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsDtForNtSupTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsDtForNtSupTx = _JnxMbgPgwPPGtpV2ICsDtForNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 407),
    _JnxMbgPgwPPGtpV2ICsDtForNtSupTx_Type()
)
jnxMbgPgwPPGtpV2ICsDtForNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsDtForNtSupTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsInReFRePrRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsInReFRePrRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsInReFRePrRx = _JnxMbgPgwPPGtpV2ICsInReFRePrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 408),
    _JnxMbgPgwPPGtpV2ICsInReFRePrRx_Type()
)
jnxMbgPgwPPGtpV2ICsInReFRePrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsInReFRePrRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsInReFRePrTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsInReFRePrTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsInReFRePrTx = _JnxMbgPgwPPGtpV2ICsInReFRePrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 409),
    _JnxMbgPgwPPGtpV2ICsInReFRePrTx_Type()
)
jnxMbgPgwPPGtpV2ICsInReFRePrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsInReFRePrTx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsInvPrRx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsInvPrRx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsInvPrRx = _JnxMbgPgwPPGtpV2ICsInvPrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 410),
    _JnxMbgPgwPPGtpV2ICsInvPrRx_Type()
)
jnxMbgPgwPPGtpV2ICsInvPrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsInvPrRx.setStatus("current")
_JnxMbgPgwPPGtpV2ICsInvPrTx_Type = Counter64
_JnxMbgPgwPPGtpV2ICsInvPrTx_Object = MibTableColumn
jnxMbgPgwPPGtpV2ICsInvPrTx = _JnxMbgPgwPPGtpV2ICsInvPrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 411),
    _JnxMbgPgwPPGtpV2ICsInvPrTx_Type()
)
jnxMbgPgwPPGtpV2ICsInvPrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPGtpV2ICsInvPrTx.setStatus("current")
_JnxMbgPgwPPV1InitPdpCxtReqRx_Type = Counter64
_JnxMbgPgwPPV1InitPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwPPV1InitPdpCxtReqRx = _JnxMbgPgwPPV1InitPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 412),
    _JnxMbgPgwPPV1InitPdpCxtReqRx_Type()
)
jnxMbgPgwPPV1InitPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1InitPdpCxtReqRx.setStatus("current")
_JnxMbgPgwPPV1InitPdpCxtReqTx_Type = Counter64
_JnxMbgPgwPPV1InitPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwPPV1InitPdpCxtReqTx = _JnxMbgPgwPPV1InitPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 413),
    _JnxMbgPgwPPV1InitPdpCxtReqTx_Type()
)
jnxMbgPgwPPV1InitPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1InitPdpCxtReqTx.setStatus("current")
_JnxMbgPgwPPV1InitPdpCxtRspRx_Type = Counter64
_JnxMbgPgwPPV1InitPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwPPV1InitPdpCxtRspRx = _JnxMbgPgwPPV1InitPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 414),
    _JnxMbgPgwPPV1InitPdpCxtRspRx_Type()
)
jnxMbgPgwPPV1InitPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1InitPdpCxtRspRx.setStatus("current")
_JnxMbgPgwPPV1InitPdpCxtRspTx_Type = Counter64
_JnxMbgPgwPPV1InitPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwPPV1InitPdpCxtRspTx = _JnxMbgPgwPPV1InitPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 415),
    _JnxMbgPgwPPV1InitPdpCxtRspTx_Type()
)
jnxMbgPgwPPV1InitPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV1InitPdpCxtRspTx.setStatus("current")
_JnxMbgPgwPPV2SuspNotifRx_Type = Counter64
_JnxMbgPgwPPV2SuspNotifRx_Object = MibTableColumn
jnxMbgPgwPPV2SuspNotifRx = _JnxMbgPgwPPV2SuspNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 416),
    _JnxMbgPgwPPV2SuspNotifRx_Type()
)
jnxMbgPgwPPV2SuspNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2SuspNotifRx.setStatus("current")
_JnxMbgPgwPPV2SuspNotifTx_Type = Counter64
_JnxMbgPgwPPV2SuspNotifTx_Object = MibTableColumn
jnxMbgPgwPPV2SuspNotifTx = _JnxMbgPgwPPV2SuspNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 417),
    _JnxMbgPgwPPV2SuspNotifTx_Type()
)
jnxMbgPgwPPV2SuspNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2SuspNotifTx.setStatus("current")
_JnxMbgPgwPPV2SuspAckRx_Type = Counter64
_JnxMbgPgwPPV2SuspAckRx_Object = MibTableColumn
jnxMbgPgwPPV2SuspAckRx = _JnxMbgPgwPPV2SuspAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 418),
    _JnxMbgPgwPPV2SuspAckRx_Type()
)
jnxMbgPgwPPV2SuspAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2SuspAckRx.setStatus("current")
_JnxMbgPgwPPV2SuspAckTx_Type = Counter64
_JnxMbgPgwPPV2SuspAckTx_Object = MibTableColumn
jnxMbgPgwPPV2SuspAckTx = _JnxMbgPgwPPV2SuspAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 419),
    _JnxMbgPgwPPV2SuspAckTx_Type()
)
jnxMbgPgwPPV2SuspAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2SuspAckTx.setStatus("current")
_JnxMbgPgwPPV2ResumeNotifRx_Type = Counter64
_JnxMbgPgwPPV2ResumeNotifRx_Object = MibTableColumn
jnxMbgPgwPPV2ResumeNotifRx = _JnxMbgPgwPPV2ResumeNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 420),
    _JnxMbgPgwPPV2ResumeNotifRx_Type()
)
jnxMbgPgwPPV2ResumeNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ResumeNotifRx.setStatus("current")
_JnxMbgPgwPPV2ResumeNotifTx_Type = Counter64
_JnxMbgPgwPPV2ResumeNotifTx_Object = MibTableColumn
jnxMbgPgwPPV2ResumeNotifTx = _JnxMbgPgwPPV2ResumeNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 421),
    _JnxMbgPgwPPV2ResumeNotifTx_Type()
)
jnxMbgPgwPPV2ResumeNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ResumeNotifTx.setStatus("current")
_JnxMbgPgwPPV2ResumeAckRx_Type = Counter64
_JnxMbgPgwPPV2ResumeAckRx_Object = MibTableColumn
jnxMbgPgwPPV2ResumeAckRx = _JnxMbgPgwPPV2ResumeAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 422),
    _JnxMbgPgwPPV2ResumeAckRx_Type()
)
jnxMbgPgwPPV2ResumeAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ResumeAckRx.setStatus("current")
_JnxMbgPgwPPV2ResumeAckTx_Type = Counter64
_JnxMbgPgwPPV2ResumeAckTx_Object = MibTableColumn
jnxMbgPgwPPV2ResumeAckTx = _JnxMbgPgwPPV2ResumeAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 423),
    _JnxMbgPgwPPV2ResumeAckTx_Type()
)
jnxMbgPgwPPV2ResumeAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2ResumeAckTx.setStatus("current")
_JnxMbgPgwPPV2PiggybackMsgRx_Type = Counter64
_JnxMbgPgwPPV2PiggybackMsgRx_Object = MibTableColumn
jnxMbgPgwPPV2PiggybackMsgRx = _JnxMbgPgwPPV2PiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 424),
    _JnxMbgPgwPPV2PiggybackMsgRx_Type()
)
jnxMbgPgwPPV2PiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2PiggybackMsgRx.setStatus("current")
_JnxMbgPgwPPV2PiggybackMsgTx_Type = Counter64
_JnxMbgPgwPPV2PiggybackMsgTx_Object = MibTableColumn
jnxMbgPgwPPV2PiggybackMsgTx = _JnxMbgPgwPPV2PiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 9, 1, 425),
    _JnxMbgPgwPPV2PiggybackMsgTx_Type()
)
jnxMbgPgwPPV2PiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPPV2PiggybackMsgTx.setStatus("current")
_JnxMbgPgwGtpCGlbStatsTable_Object = MibTable
jnxMbgPgwGtpCGlbStatsTable = _JnxMbgPgwGtpCGlbStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10)
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpCGlbStatsTable.setStatus("current")
_JnxMbgPgwGtpGlbStatsEntry_Object = MibTableRow
jnxMbgPgwGtpGlbStatsEntry = _JnxMbgPgwGtpGlbStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1)
)
jnxMbgPgwGtpGlbStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpGlbStatsEntry.setStatus("current")
_JnxMbgPgwRxPacketsDropped_Type = Counter64
_JnxMbgPgwRxPacketsDropped_Object = MibTableColumn
jnxMbgPgwRxPacketsDropped = _JnxMbgPgwRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 1),
    _JnxMbgPgwRxPacketsDropped_Type()
)
jnxMbgPgwRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwRxPacketsDropped.setStatus("current")
_JnxMbgPgwPacketAllocFail_Type = Counter64
_JnxMbgPgwPacketAllocFail_Object = MibTableColumn
jnxMbgPgwPacketAllocFail = _JnxMbgPgwPacketAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 2),
    _JnxMbgPgwPacketAllocFail_Type()
)
jnxMbgPgwPacketAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPacketAllocFail.setStatus("current")
_JnxMbgPgwPacketSendFail_Type = Counter64
_JnxMbgPgwPacketSendFail_Object = MibTableColumn
jnxMbgPgwPacketSendFail = _JnxMbgPgwPacketSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 3),
    _JnxMbgPgwPacketSendFail_Type()
)
jnxMbgPgwPacketSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPacketSendFail.setStatus("current")
_JnxMbgPgwIPVerErrRx_Type = Counter64
_JnxMbgPgwIPVerErrRx_Object = MibTableColumn
jnxMbgPgwIPVerErrRx = _JnxMbgPgwIPVerErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 4),
    _JnxMbgPgwIPVerErrRx_Type()
)
jnxMbgPgwIPVerErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIPVerErrRx.setStatus("current")
_JnxMbgPgwIPProtoErrRx_Type = Counter64
_JnxMbgPgwIPProtoErrRx_Object = MibTableColumn
jnxMbgPgwIPProtoErrRx = _JnxMbgPgwIPProtoErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 5),
    _JnxMbgPgwIPProtoErrRx_Type()
)
jnxMbgPgwIPProtoErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIPProtoErrRx.setStatus("current")
_JnxMbgPgwGTPPortErrRx_Type = Counter64
_JnxMbgPgwGTPPortErrRx_Object = MibTableColumn
jnxMbgPgwGTPPortErrRx = _JnxMbgPgwGTPPortErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 6),
    _JnxMbgPgwGTPPortErrRx_Type()
)
jnxMbgPgwGTPPortErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPPortErrRx.setStatus("current")
_JnxMbgPgwGTPUnknVerRx_Type = Counter64
_JnxMbgPgwGTPUnknVerRx_Object = MibTableColumn
jnxMbgPgwGTPUnknVerRx = _JnxMbgPgwGTPUnknVerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 7),
    _JnxMbgPgwGTPUnknVerRx_Type()
)
jnxMbgPgwGTPUnknVerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGTPUnknVerRx.setStatus("current")
_JnxMbgPgwPcktLenErrRx_Type = Counter64
_JnxMbgPgwPcktLenErrRx_Object = MibTableColumn
jnxMbgPgwPcktLenErrRx = _JnxMbgPgwPcktLenErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 8),
    _JnxMbgPgwPcktLenErrRx_Type()
)
jnxMbgPgwPcktLenErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwPcktLenErrRx.setStatus("current")
_JnxMbgPgwUnknMsgRx_Type = Counter64
_JnxMbgPgwUnknMsgRx_Object = MibTableColumn
jnxMbgPgwUnknMsgRx = _JnxMbgPgwUnknMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 9),
    _JnxMbgPgwUnknMsgRx_Type()
)
jnxMbgPgwUnknMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwUnknMsgRx.setStatus("current")
_JnxMbgPgwV2ProtocolErrRx_Type = Counter64
_JnxMbgPgwV2ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwV2ProtocolErrRx = _JnxMbgPgwV2ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 10),
    _JnxMbgPgwV2ProtocolErrRx_Type()
)
jnxMbgPgwV2ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ProtocolErrRx.setStatus("current")
_JnxMbgPgwV2UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwV2UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwV2UnSupportedMsgRx = _JnxMbgPgwV2UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 11),
    _JnxMbgPgwV2UnSupportedMsgRx_Type()
)
jnxMbgPgwV2UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwV2T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwV2T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwV2T3RespTmrExpRx = _JnxMbgPgwV2T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 12),
    _JnxMbgPgwV2T3RespTmrExpRx_Type()
)
jnxMbgPgwV2T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwV2GlbNumMsgRx_Type = Counter64
_JnxMbgPgwV2GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwV2GlbNumMsgRx = _JnxMbgPgwV2GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 13),
    _JnxMbgPgwV2GlbNumMsgRx_Type()
)
jnxMbgPgwV2GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbNumMsgRx.setStatus("current")
_JnxMbgPgwV2GlbNumMsgTx_Type = Counter64
_JnxMbgPgwV2GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwV2GlbNumMsgTx = _JnxMbgPgwV2GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 14),
    _JnxMbgPgwV2GlbNumMsgTx_Type()
)
jnxMbgPgwV2GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbNumMsgTx.setStatus("current")
_JnxMbgPgwV2GlbNumBytesRx_Type = Counter64
_JnxMbgPgwV2GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwV2GlbNumBytesRx = _JnxMbgPgwV2GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 15),
    _JnxMbgPgwV2GlbNumBytesRx_Type()
)
jnxMbgPgwV2GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbNumBytesRx.setStatus("current")
_JnxMbgPgwV2GlbNumBytesTx_Type = Counter64
_JnxMbgPgwV2GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwV2GlbNumBytesTx = _JnxMbgPgwV2GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 16),
    _JnxMbgPgwV2GlbNumBytesTx_Type()
)
jnxMbgPgwV2GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbNumBytesTx.setStatus("current")
_JnxMbgPgwV2GlbEchoReqRx_Type = Counter64
_JnxMbgPgwV2GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwV2GlbEchoReqRx = _JnxMbgPgwV2GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 19),
    _JnxMbgPgwV2GlbEchoReqRx_Type()
)
jnxMbgPgwV2GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbEchoReqRx.setStatus("current")
_JnxMbgPgwV2GlbEchoReqTx_Type = Counter64
_JnxMbgPgwV2GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwV2GlbEchoReqTx = _JnxMbgPgwV2GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 20),
    _JnxMbgPgwV2GlbEchoReqTx_Type()
)
jnxMbgPgwV2GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbEchoReqTx.setStatus("current")
_JnxMbgPgwV2GlbEchoRespRx_Type = Counter64
_JnxMbgPgwV2GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwV2GlbEchoRespRx = _JnxMbgPgwV2GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 21),
    _JnxMbgPgwV2GlbEchoRespRx_Type()
)
jnxMbgPgwV2GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbEchoRespRx.setStatus("current")
_JnxMbgPgwV2GlbEchoRespTx_Type = Counter64
_JnxMbgPgwV2GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwV2GlbEchoRespTx = _JnxMbgPgwV2GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 22),
    _JnxMbgPgwV2GlbEchoRespTx_Type()
)
jnxMbgPgwV2GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2GlbEchoRespTx.setStatus("current")
_JnxMbgPgwV2VerNotSupRx_Type = Counter64
_JnxMbgPgwV2VerNotSupRx_Object = MibTableColumn
jnxMbgPgwV2VerNotSupRx = _JnxMbgPgwV2VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 23),
    _JnxMbgPgwV2VerNotSupRx_Type()
)
jnxMbgPgwV2VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2VerNotSupRx.setStatus("current")
_JnxMbgPgwV2VerNotSupTx_Type = Counter64
_JnxMbgPgwV2VerNotSupTx_Object = MibTableColumn
jnxMbgPgwV2VerNotSupTx = _JnxMbgPgwV2VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 24),
    _JnxMbgPgwV2VerNotSupTx_Type()
)
jnxMbgPgwV2VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2VerNotSupTx.setStatus("current")
_JnxMbgPgwV2CreateSessReqRx_Type = Counter64
_JnxMbgPgwV2CreateSessReqRx_Object = MibTableColumn
jnxMbgPgwV2CreateSessReqRx = _JnxMbgPgwV2CreateSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 25),
    _JnxMbgPgwV2CreateSessReqRx_Type()
)
jnxMbgPgwV2CreateSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CreateSessReqRx.setStatus("current")
_JnxMbgPgwV2CreateSessReqTx_Type = Counter64
_JnxMbgPgwV2CreateSessReqTx_Object = MibTableColumn
jnxMbgPgwV2CreateSessReqTx = _JnxMbgPgwV2CreateSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 26),
    _JnxMbgPgwV2CreateSessReqTx_Type()
)
jnxMbgPgwV2CreateSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CreateSessReqTx.setStatus("current")
_JnxMbgPgwV2CreateSessRspRx_Type = Counter64
_JnxMbgPgwV2CreateSessRspRx_Object = MibTableColumn
jnxMbgPgwV2CreateSessRspRx = _JnxMbgPgwV2CreateSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 27),
    _JnxMbgPgwV2CreateSessRspRx_Type()
)
jnxMbgPgwV2CreateSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CreateSessRspRx.setStatus("current")
_JnxMbgPgwV2CreateSessRspTx_Type = Counter64
_JnxMbgPgwV2CreateSessRspTx_Object = MibTableColumn
jnxMbgPgwV2CreateSessRspTx = _JnxMbgPgwV2CreateSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 28),
    _JnxMbgPgwV2CreateSessRspTx_Type()
)
jnxMbgPgwV2CreateSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CreateSessRspTx.setStatus("current")
_JnxMbgPgwV2ModBrReqRx_Type = Counter64
_JnxMbgPgwV2ModBrReqRx_Object = MibTableColumn
jnxMbgPgwV2ModBrReqRx = _JnxMbgPgwV2ModBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 29),
    _JnxMbgPgwV2ModBrReqRx_Type()
)
jnxMbgPgwV2ModBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrReqRx.setStatus("current")
_JnxMbgPgwV2ModBrReqTx_Type = Counter64
_JnxMbgPgwV2ModBrReqTx_Object = MibTableColumn
jnxMbgPgwV2ModBrReqTx = _JnxMbgPgwV2ModBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 30),
    _JnxMbgPgwV2ModBrReqTx_Type()
)
jnxMbgPgwV2ModBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrReqTx.setStatus("current")
_JnxMbgPgwV2ModBrRspRx_Type = Counter64
_JnxMbgPgwV2ModBrRspRx_Object = MibTableColumn
jnxMbgPgwV2ModBrRspRx = _JnxMbgPgwV2ModBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 31),
    _JnxMbgPgwV2ModBrRspRx_Type()
)
jnxMbgPgwV2ModBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrRspRx.setStatus("current")
_JnxMbgPgwV2ModBrRspTx_Type = Counter64
_JnxMbgPgwV2ModBrRspTx_Object = MibTableColumn
jnxMbgPgwV2ModBrRspTx = _JnxMbgPgwV2ModBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 32),
    _JnxMbgPgwV2ModBrRspTx_Type()
)
jnxMbgPgwV2ModBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrRspTx.setStatus("current")
_JnxMbgPgwV2DelSessReqRx_Type = Counter64
_JnxMbgPgwV2DelSessReqRx_Object = MibTableColumn
jnxMbgPgwV2DelSessReqRx = _JnxMbgPgwV2DelSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 33),
    _JnxMbgPgwV2DelSessReqRx_Type()
)
jnxMbgPgwV2DelSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelSessReqRx.setStatus("current")
_JnxMbgPgwV2DelSessReqTx_Type = Counter64
_JnxMbgPgwV2DelSessReqTx_Object = MibTableColumn
jnxMbgPgwV2DelSessReqTx = _JnxMbgPgwV2DelSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 34),
    _JnxMbgPgwV2DelSessReqTx_Type()
)
jnxMbgPgwV2DelSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelSessReqTx.setStatus("current")
_JnxMbgPgwV2DelSessRspRx_Type = Counter64
_JnxMbgPgwV2DelSessRspRx_Object = MibTableColumn
jnxMbgPgwV2DelSessRspRx = _JnxMbgPgwV2DelSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 35),
    _JnxMbgPgwV2DelSessRspRx_Type()
)
jnxMbgPgwV2DelSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelSessRspRx.setStatus("current")
_JnxMbgPgwV2DelSessRspTx_Type = Counter64
_JnxMbgPgwV2DelSessRspTx_Object = MibTableColumn
jnxMbgPgwV2DelSessRspTx = _JnxMbgPgwV2DelSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 36),
    _JnxMbgPgwV2DelSessRspTx_Type()
)
jnxMbgPgwV2DelSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelSessRspTx.setStatus("current")
_JnxMbgPgwV2CrtBrReqRx_Type = Counter64
_JnxMbgPgwV2CrtBrReqRx_Object = MibTableColumn
jnxMbgPgwV2CrtBrReqRx = _JnxMbgPgwV2CrtBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 37),
    _JnxMbgPgwV2CrtBrReqRx_Type()
)
jnxMbgPgwV2CrtBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrtBrReqRx.setStatus("current")
_JnxMbgPgwV2CrtBrReqTx_Type = Counter64
_JnxMbgPgwV2CrtBrReqTx_Object = MibTableColumn
jnxMbgPgwV2CrtBrReqTx = _JnxMbgPgwV2CrtBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 38),
    _JnxMbgPgwV2CrtBrReqTx_Type()
)
jnxMbgPgwV2CrtBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrtBrReqTx.setStatus("current")
_JnxMbgPgwV2CrtBrRspRx_Type = Counter64
_JnxMbgPgwV2CrtBrRspRx_Object = MibTableColumn
jnxMbgPgwV2CrtBrRspRx = _JnxMbgPgwV2CrtBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 39),
    _JnxMbgPgwV2CrtBrRspRx_Type()
)
jnxMbgPgwV2CrtBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrtBrRspRx.setStatus("current")
_JnxMbgPgwV2CrtBrRspTx_Type = Counter64
_JnxMbgPgwV2CrtBrRspTx_Object = MibTableColumn
jnxMbgPgwV2CrtBrRspTx = _JnxMbgPgwV2CrtBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 40),
    _JnxMbgPgwV2CrtBrRspTx_Type()
)
jnxMbgPgwV2CrtBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrtBrRspTx.setStatus("current")
_JnxMbgPgwV2UpdBrReqRx_Type = Counter64
_JnxMbgPgwV2UpdBrReqRx_Object = MibTableColumn
jnxMbgPgwV2UpdBrReqRx = _JnxMbgPgwV2UpdBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 41),
    _JnxMbgPgwV2UpdBrReqRx_Type()
)
jnxMbgPgwV2UpdBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdBrReqRx.setStatus("current")
_JnxMbgPgwV2UpdBrReqTx_Type = Counter64
_JnxMbgPgwV2UpdBrReqTx_Object = MibTableColumn
jnxMbgPgwV2UpdBrReqTx = _JnxMbgPgwV2UpdBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 42),
    _JnxMbgPgwV2UpdBrReqTx_Type()
)
jnxMbgPgwV2UpdBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdBrReqTx.setStatus("current")
_JnxMbgPgwV2UpdBrRspRx_Type = Counter64
_JnxMbgPgwV2UpdBrRspRx_Object = MibTableColumn
jnxMbgPgwV2UpdBrRspRx = _JnxMbgPgwV2UpdBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 43),
    _JnxMbgPgwV2UpdBrRspRx_Type()
)
jnxMbgPgwV2UpdBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdBrRspRx.setStatus("current")
_JnxMbgPgwV2UpdBrRspTx_Type = Counter64
_JnxMbgPgwV2UpdBrRspTx_Object = MibTableColumn
jnxMbgPgwV2UpdBrRspTx = _JnxMbgPgwV2UpdBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 44),
    _JnxMbgPgwV2UpdBrRspTx_Type()
)
jnxMbgPgwV2UpdBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdBrRspTx.setStatus("current")
_JnxMbgPgwV2DelBrReqRx_Type = Counter64
_JnxMbgPgwV2DelBrReqRx_Object = MibTableColumn
jnxMbgPgwV2DelBrReqRx = _JnxMbgPgwV2DelBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 45),
    _JnxMbgPgwV2DelBrReqRx_Type()
)
jnxMbgPgwV2DelBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrReqRx.setStatus("current")
_JnxMbgPgwV2DelBrReqTx_Type = Counter64
_JnxMbgPgwV2DelBrReqTx_Object = MibTableColumn
jnxMbgPgwV2DelBrReqTx = _JnxMbgPgwV2DelBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 46),
    _JnxMbgPgwV2DelBrReqTx_Type()
)
jnxMbgPgwV2DelBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrReqTx.setStatus("current")
_JnxMbgPgwV2DelBrRspRx_Type = Counter64
_JnxMbgPgwV2DelBrRspRx_Object = MibTableColumn
jnxMbgPgwV2DelBrRspRx = _JnxMbgPgwV2DelBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 47),
    _JnxMbgPgwV2DelBrRspRx_Type()
)
jnxMbgPgwV2DelBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrRspRx.setStatus("current")
_JnxMbgPgwV2DelBrRspTx_Type = Counter64
_JnxMbgPgwV2DelBrRspTx_Object = MibTableColumn
jnxMbgPgwV2DelBrRspTx = _JnxMbgPgwV2DelBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 48),
    _JnxMbgPgwV2DelBrRspTx_Type()
)
jnxMbgPgwV2DelBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrRspTx.setStatus("current")
_JnxMbgPgwV2DelConnSetReqRx_Type = Counter64
_JnxMbgPgwV2DelConnSetReqRx_Object = MibTableColumn
jnxMbgPgwV2DelConnSetReqRx = _JnxMbgPgwV2DelConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 49),
    _JnxMbgPgwV2DelConnSetReqRx_Type()
)
jnxMbgPgwV2DelConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelConnSetReqRx.setStatus("current")
_JnxMbgPgwV2DelConnSetReqTx_Type = Counter64
_JnxMbgPgwV2DelConnSetReqTx_Object = MibTableColumn
jnxMbgPgwV2DelConnSetReqTx = _JnxMbgPgwV2DelConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 50),
    _JnxMbgPgwV2DelConnSetReqTx_Type()
)
jnxMbgPgwV2DelConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelConnSetReqTx.setStatus("current")
_JnxMbgPgwV2DelConnSetRspRx_Type = Counter64
_JnxMbgPgwV2DelConnSetRspRx_Object = MibTableColumn
jnxMbgPgwV2DelConnSetRspRx = _JnxMbgPgwV2DelConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 51),
    _JnxMbgPgwV2DelConnSetRspRx_Type()
)
jnxMbgPgwV2DelConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelConnSetRspRx.setStatus("current")
_JnxMbgPgwV2DelConnSetRspTx_Type = Counter64
_JnxMbgPgwV2DelConnSetRspTx_Object = MibTableColumn
jnxMbgPgwV2DelConnSetRspTx = _JnxMbgPgwV2DelConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 52),
    _JnxMbgPgwV2DelConnSetRspTx_Type()
)
jnxMbgPgwV2DelConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelConnSetRspTx.setStatus("current")
_JnxMbgPgwV2UpdConnSetReqRx_Type = Counter64
_JnxMbgPgwV2UpdConnSetReqRx_Object = MibTableColumn
jnxMbgPgwV2UpdConnSetReqRx = _JnxMbgPgwV2UpdConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 53),
    _JnxMbgPgwV2UpdConnSetReqRx_Type()
)
jnxMbgPgwV2UpdConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdConnSetReqRx.setStatus("current")
_JnxMbgPgwV2UpdConnSetReqTx_Type = Counter64
_JnxMbgPgwV2UpdConnSetReqTx_Object = MibTableColumn
jnxMbgPgwV2UpdConnSetReqTx = _JnxMbgPgwV2UpdConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 54),
    _JnxMbgPgwV2UpdConnSetReqTx_Type()
)
jnxMbgPgwV2UpdConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdConnSetReqTx.setStatus("current")
_JnxMbgPgwV2UpdConnSetRspRx_Type = Counter64
_JnxMbgPgwV2UpdConnSetRspRx_Object = MibTableColumn
jnxMbgPgwV2UpdConnSetRspRx = _JnxMbgPgwV2UpdConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 55),
    _JnxMbgPgwV2UpdConnSetRspRx_Type()
)
jnxMbgPgwV2UpdConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdConnSetRspRx.setStatus("current")
_JnxMbgPgwV2UpdConnSetRspTx_Type = Counter64
_JnxMbgPgwV2UpdConnSetRspTx_Object = MibTableColumn
jnxMbgPgwV2UpdConnSetRspTx = _JnxMbgPgwV2UpdConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 56),
    _JnxMbgPgwV2UpdConnSetRspTx_Type()
)
jnxMbgPgwV2UpdConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2UpdConnSetRspTx.setStatus("current")
_JnxMbgPgwV2ModBrCmdRx_Type = Counter64
_JnxMbgPgwV2ModBrCmdRx_Object = MibTableColumn
jnxMbgPgwV2ModBrCmdRx = _JnxMbgPgwV2ModBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 57),
    _JnxMbgPgwV2ModBrCmdRx_Type()
)
jnxMbgPgwV2ModBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrCmdRx.setStatus("current")
_JnxMbgPgwV2ModBrCmdTx_Type = Counter64
_JnxMbgPgwV2ModBrCmdTx_Object = MibTableColumn
jnxMbgPgwV2ModBrCmdTx = _JnxMbgPgwV2ModBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 58),
    _JnxMbgPgwV2ModBrCmdTx_Type()
)
jnxMbgPgwV2ModBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrCmdTx.setStatus("current")
_JnxMbgPgwV2ModBrFlrIndRx_Type = Counter64
_JnxMbgPgwV2ModBrFlrIndRx_Object = MibTableColumn
jnxMbgPgwV2ModBrFlrIndRx = _JnxMbgPgwV2ModBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 59),
    _JnxMbgPgwV2ModBrFlrIndRx_Type()
)
jnxMbgPgwV2ModBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrFlrIndRx.setStatus("current")
_JnxMbgPgwV2ModBrFlrIndTx_Type = Counter64
_JnxMbgPgwV2ModBrFlrIndTx_Object = MibTableColumn
jnxMbgPgwV2ModBrFlrIndTx = _JnxMbgPgwV2ModBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 60),
    _JnxMbgPgwV2ModBrFlrIndTx_Type()
)
jnxMbgPgwV2ModBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ModBrFlrIndTx.setStatus("current")
_JnxMbgPgwV2DelBrCmdRx_Type = Counter64
_JnxMbgPgwV2DelBrCmdRx_Object = MibTableColumn
jnxMbgPgwV2DelBrCmdRx = _JnxMbgPgwV2DelBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 61),
    _JnxMbgPgwV2DelBrCmdRx_Type()
)
jnxMbgPgwV2DelBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrCmdRx.setStatus("current")
_JnxMbgPgwV2DelBrCmdTx_Type = Counter64
_JnxMbgPgwV2DelBrCmdTx_Object = MibTableColumn
jnxMbgPgwV2DelBrCmdTx = _JnxMbgPgwV2DelBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 62),
    _JnxMbgPgwV2DelBrCmdTx_Type()
)
jnxMbgPgwV2DelBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrCmdTx.setStatus("current")
_JnxMbgPgwV2DelBrFlrIndRx_Type = Counter64
_JnxMbgPgwV2DelBrFlrIndRx_Object = MibTableColumn
jnxMbgPgwV2DelBrFlrIndRx = _JnxMbgPgwV2DelBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 63),
    _JnxMbgPgwV2DelBrFlrIndRx_Type()
)
jnxMbgPgwV2DelBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrFlrIndRx.setStatus("current")
_JnxMbgPgwV2DelBrFlrIndTx_Type = Counter64
_JnxMbgPgwV2DelBrFlrIndTx_Object = MibTableColumn
jnxMbgPgwV2DelBrFlrIndTx = _JnxMbgPgwV2DelBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 64),
    _JnxMbgPgwV2DelBrFlrIndTx_Type()
)
jnxMbgPgwV2DelBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelBrFlrIndTx.setStatus("current")
_JnxMbgPgwV2BrResCmdRx_Type = Counter64
_JnxMbgPgwV2BrResCmdRx_Object = MibTableColumn
jnxMbgPgwV2BrResCmdRx = _JnxMbgPgwV2BrResCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 65),
    _JnxMbgPgwV2BrResCmdRx_Type()
)
jnxMbgPgwV2BrResCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2BrResCmdRx.setStatus("current")
_JnxMbgPgwV2BrResCmdTx_Type = Counter64
_JnxMbgPgwV2BrResCmdTx_Object = MibTableColumn
jnxMbgPgwV2BrResCmdTx = _JnxMbgPgwV2BrResCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 66),
    _JnxMbgPgwV2BrResCmdTx_Type()
)
jnxMbgPgwV2BrResCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2BrResCmdTx.setStatus("current")
_JnxMbgPgwV2BrResFlrIndRx_Type = Counter64
_JnxMbgPgwV2BrResFlrIndRx_Object = MibTableColumn
jnxMbgPgwV2BrResFlrIndRx = _JnxMbgPgwV2BrResFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 67),
    _JnxMbgPgwV2BrResFlrIndRx_Type()
)
jnxMbgPgwV2BrResFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2BrResFlrIndRx.setStatus("current")
_JnxMbgPgwV2BrResFlrIndTx_Type = Counter64
_JnxMbgPgwV2BrResFlrIndTx_Object = MibTableColumn
jnxMbgPgwV2BrResFlrIndTx = _JnxMbgPgwV2BrResFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 68),
    _JnxMbgPgwV2BrResFlrIndTx_Type()
)
jnxMbgPgwV2BrResFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2BrResFlrIndTx.setStatus("current")
_JnxMbgPgwV2RelAcsBrReqRx_Type = Counter64
_JnxMbgPgwV2RelAcsBrReqRx_Object = MibTableColumn
jnxMbgPgwV2RelAcsBrReqRx = _JnxMbgPgwV2RelAcsBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 69),
    _JnxMbgPgwV2RelAcsBrReqRx_Type()
)
jnxMbgPgwV2RelAcsBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2RelAcsBrReqRx.setStatus("obsolete")
_JnxMbgPgwV2RelAcsBrReqTx_Type = Counter64
_JnxMbgPgwV2RelAcsBrReqTx_Object = MibTableColumn
jnxMbgPgwV2RelAcsBrReqTx = _JnxMbgPgwV2RelAcsBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 70),
    _JnxMbgPgwV2RelAcsBrReqTx_Type()
)
jnxMbgPgwV2RelAcsBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2RelAcsBrReqTx.setStatus("obsolete")
_JnxMbgPgwV2RelAcsBrRespRx_Type = Counter64
_JnxMbgPgwV2RelAcsBrRespRx_Object = MibTableColumn
jnxMbgPgwV2RelAcsBrRespRx = _JnxMbgPgwV2RelAcsBrRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 71),
    _JnxMbgPgwV2RelAcsBrRespRx_Type()
)
jnxMbgPgwV2RelAcsBrRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2RelAcsBrRespRx.setStatus("obsolete")
_JnxMbgPgwV2RelAcsBrRespTx_Type = Counter64
_JnxMbgPgwV2RelAcsBrRespTx_Object = MibTableColumn
jnxMbgPgwV2RelAcsBrRespTx = _JnxMbgPgwV2RelAcsBrRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 72),
    _JnxMbgPgwV2RelAcsBrRespTx_Type()
)
jnxMbgPgwV2RelAcsBrRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2RelAcsBrRespTx.setStatus("obsolete")
_JnxMbgPgwV2CrIndTunReqRx_Type = Counter64
_JnxMbgPgwV2CrIndTunReqRx_Object = MibTableColumn
jnxMbgPgwV2CrIndTunReqRx = _JnxMbgPgwV2CrIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 73),
    _JnxMbgPgwV2CrIndTunReqRx_Type()
)
jnxMbgPgwV2CrIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrIndTunReqRx.setStatus("obsolete")
_JnxMbgPgwV2CrIndTunReqTx_Type = Counter64
_JnxMbgPgwV2CrIndTunReqTx_Object = MibTableColumn
jnxMbgPgwV2CrIndTunReqTx = _JnxMbgPgwV2CrIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 74),
    _JnxMbgPgwV2CrIndTunReqTx_Type()
)
jnxMbgPgwV2CrIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrIndTunReqTx.setStatus("obsolete")
_JnxMbgPgwV2CrIndTunRespRx_Type = Counter64
_JnxMbgPgwV2CrIndTunRespRx_Object = MibTableColumn
jnxMbgPgwV2CrIndTunRespRx = _JnxMbgPgwV2CrIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 75),
    _JnxMbgPgwV2CrIndTunRespRx_Type()
)
jnxMbgPgwV2CrIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrIndTunRespRx.setStatus("obsolete")
_JnxMbgPgwV2CrIndTunRespTx_Type = Counter64
_JnxMbgPgwV2CrIndTunRespTx_Object = MibTableColumn
jnxMbgPgwV2CrIndTunRespTx = _JnxMbgPgwV2CrIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 76),
    _JnxMbgPgwV2CrIndTunRespTx_Type()
)
jnxMbgPgwV2CrIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2CrIndTunRespTx.setStatus("obsolete")
_JnxMbgPgwV2DelIndTunReqRx_Type = Counter64
_JnxMbgPgwV2DelIndTunReqRx_Object = MibTableColumn
jnxMbgPgwV2DelIndTunReqRx = _JnxMbgPgwV2DelIndTunReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 77),
    _JnxMbgPgwV2DelIndTunReqRx_Type()
)
jnxMbgPgwV2DelIndTunReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelIndTunReqRx.setStatus("obsolete")
_JnxMbgPgwV2DelIndTunReqTx_Type = Counter64
_JnxMbgPgwV2DelIndTunReqTx_Object = MibTableColumn
jnxMbgPgwV2DelIndTunReqTx = _JnxMbgPgwV2DelIndTunReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 78),
    _JnxMbgPgwV2DelIndTunReqTx_Type()
)
jnxMbgPgwV2DelIndTunReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelIndTunReqTx.setStatus("obsolete")
_JnxMbgPgwV2DelIndTunRespRx_Type = Counter64
_JnxMbgPgwV2DelIndTunRespRx_Object = MibTableColumn
jnxMbgPgwV2DelIndTunRespRx = _JnxMbgPgwV2DelIndTunRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 79),
    _JnxMbgPgwV2DelIndTunRespRx_Type()
)
jnxMbgPgwV2DelIndTunRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelIndTunRespRx.setStatus("obsolete")
_JnxMbgPgwV2DelIndTunRespTx_Type = Counter64
_JnxMbgPgwV2DelIndTunRespTx_Object = MibTableColumn
jnxMbgPgwV2DelIndTunRespTx = _JnxMbgPgwV2DelIndTunRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 80),
    _JnxMbgPgwV2DelIndTunRespTx_Type()
)
jnxMbgPgwV2DelIndTunRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DelIndTunRespTx.setStatus("obsolete")
_JnxMbgPgwV2DlDataNotifRx_Type = Counter64
_JnxMbgPgwV2DlDataNotifRx_Object = MibTableColumn
jnxMbgPgwV2DlDataNotifRx = _JnxMbgPgwV2DlDataNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 81),
    _JnxMbgPgwV2DlDataNotifRx_Type()
)
jnxMbgPgwV2DlDataNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DlDataNotifRx.setStatus("obsolete")
_JnxMbgPgwV2DlDataNotifTx_Type = Counter64
_JnxMbgPgwV2DlDataNotifTx_Object = MibTableColumn
jnxMbgPgwV2DlDataNotifTx = _JnxMbgPgwV2DlDataNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 82),
    _JnxMbgPgwV2DlDataNotifTx_Type()
)
jnxMbgPgwV2DlDataNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DlDataNotifTx.setStatus("obsolete")
_JnxMbgPgwV2DlDataAckRx_Type = Counter64
_JnxMbgPgwV2DlDataAckRx_Object = MibTableColumn
jnxMbgPgwV2DlDataAckRx = _JnxMbgPgwV2DlDataAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 83),
    _JnxMbgPgwV2DlDataAckRx_Type()
)
jnxMbgPgwV2DlDataAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DlDataAckRx.setStatus("obsolete")
_JnxMbgPgwV2DlDataAckTx_Type = Counter64
_JnxMbgPgwV2DlDataAckTx_Object = MibTableColumn
jnxMbgPgwV2DlDataAckTx = _JnxMbgPgwV2DlDataAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 84),
    _JnxMbgPgwV2DlDataAckTx_Type()
)
jnxMbgPgwV2DlDataAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DlDataAckTx.setStatus("obsolete")
_JnxMbgPgwV2DlDataNotiFlrIndRx_Type = Counter64
_JnxMbgPgwV2DlDataNotiFlrIndRx_Object = MibTableColumn
jnxMbgPgwV2DlDataNotiFlrIndRx = _JnxMbgPgwV2DlDataNotiFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 85),
    _JnxMbgPgwV2DlDataNotiFlrIndRx_Type()
)
jnxMbgPgwV2DlDataNotiFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DlDataNotiFlrIndRx.setStatus("obsolete")
_JnxMbgPgwV2DlDataNotiFlrIndTx_Type = Counter64
_JnxMbgPgwV2DlDataNotiFlrIndTx_Object = MibTableColumn
jnxMbgPgwV2DlDataNotiFlrIndTx = _JnxMbgPgwV2DlDataNotiFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 86),
    _JnxMbgPgwV2DlDataNotiFlrIndTx_Type()
)
jnxMbgPgwV2DlDataNotiFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2DlDataNotiFlrIndTx.setStatus("obsolete")
_JnxMbgPgwV2StopPagingIndRx_Type = Counter64
_JnxMbgPgwV2StopPagingIndRx_Object = MibTableColumn
jnxMbgPgwV2StopPagingIndRx = _JnxMbgPgwV2StopPagingIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 87),
    _JnxMbgPgwV2StopPagingIndRx_Type()
)
jnxMbgPgwV2StopPagingIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2StopPagingIndRx.setStatus("obsolete")
_JnxMbgPgwV2StopPagingIndTx_Type = Counter64
_JnxMbgPgwV2StopPagingIndTx_Object = MibTableColumn
jnxMbgPgwV2StopPagingIndTx = _JnxMbgPgwV2StopPagingIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 88),
    _JnxMbgPgwV2StopPagingIndTx_Type()
)
jnxMbgPgwV2StopPagingIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2StopPagingIndTx.setStatus("obsolete")
_JnxMbgPgwV2ICsPageRx_Type = Counter64
_JnxMbgPgwV2ICsPageRx_Object = MibTableColumn
jnxMbgPgwV2ICsPageRx = _JnxMbgPgwV2ICsPageRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 89),
    _JnxMbgPgwV2ICsPageRx_Type()
)
jnxMbgPgwV2ICsPageRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPageRx.setStatus("obsolete")
_JnxMbgPgwV2ICsPageTx_Type = Counter64
_JnxMbgPgwV2ICsPageTx_Object = MibTableColumn
jnxMbgPgwV2ICsPageTx = _JnxMbgPgwV2ICsPageTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 90),
    _JnxMbgPgwV2ICsPageTx_Type()
)
jnxMbgPgwV2ICsPageTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPageTx.setStatus("obsolete")
_JnxMbgPgwV2ICsReqAcceptRx_Type = Counter64
_JnxMbgPgwV2ICsReqAcceptRx_Object = MibTableColumn
jnxMbgPgwV2ICsReqAcceptRx = _JnxMbgPgwV2ICsReqAcceptRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 91),
    _JnxMbgPgwV2ICsReqAcceptRx_Type()
)
jnxMbgPgwV2ICsReqAcceptRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsReqAcceptRx.setStatus("current")
_JnxMbgPgwV2ICsReqAcceptTx_Type = Counter64
_JnxMbgPgwV2ICsReqAcceptTx_Object = MibTableColumn
jnxMbgPgwV2ICsReqAcceptTx = _JnxMbgPgwV2ICsReqAcceptTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 92),
    _JnxMbgPgwV2ICsReqAcceptTx_Type()
)
jnxMbgPgwV2ICsReqAcceptTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsReqAcceptTx.setStatus("current")
_JnxMbgPgwV2ICsAcceptPartRx_Type = Counter64
_JnxMbgPgwV2ICsAcceptPartRx_Object = MibTableColumn
jnxMbgPgwV2ICsAcceptPartRx = _JnxMbgPgwV2ICsAcceptPartRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 93),
    _JnxMbgPgwV2ICsAcceptPartRx_Type()
)
jnxMbgPgwV2ICsAcceptPartRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAcceptPartRx.setStatus("current")
_JnxMbgPgwV2ICsAcceptPartTx_Type = Counter64
_JnxMbgPgwV2ICsAcceptPartTx_Object = MibTableColumn
jnxMbgPgwV2ICsAcceptPartTx = _JnxMbgPgwV2ICsAcceptPartTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 94),
    _JnxMbgPgwV2ICsAcceptPartTx_Type()
)
jnxMbgPgwV2ICsAcceptPartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAcceptPartTx.setStatus("current")
_JnxMbgPgwV2ICsNewPTNPrefRx_Type = Counter64
_JnxMbgPgwV2ICsNewPTNPrefRx_Object = MibTableColumn
jnxMbgPgwV2ICsNewPTNPrefRx = _JnxMbgPgwV2ICsNewPTNPrefRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 95),
    _JnxMbgPgwV2ICsNewPTNPrefRx_Type()
)
jnxMbgPgwV2ICsNewPTNPrefRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNewPTNPrefRx.setStatus("current")
_JnxMbgPgwV2ICsNewPTNPrefTx_Type = Counter64
_JnxMbgPgwV2ICsNewPTNPrefTx_Object = MibTableColumn
jnxMbgPgwV2ICsNewPTNPrefTx = _JnxMbgPgwV2ICsNewPTNPrefTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 96),
    _JnxMbgPgwV2ICsNewPTNPrefTx_Type()
)
jnxMbgPgwV2ICsNewPTNPrefTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNewPTNPrefTx.setStatus("current")
_JnxMbgPgwV2ICsNewPTSIAdbrRx_Type = Counter64
_JnxMbgPgwV2ICsNewPTSIAdbrRx_Object = MibTableColumn
jnxMbgPgwV2ICsNewPTSIAdbrRx = _JnxMbgPgwV2ICsNewPTSIAdbrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 97),
    _JnxMbgPgwV2ICsNewPTSIAdbrRx_Type()
)
jnxMbgPgwV2ICsNewPTSIAdbrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNewPTSIAdbrRx.setStatus("current")
_JnxMbgPgwV2ICsNewPTSIAdbrTx_Type = Counter64
_JnxMbgPgwV2ICsNewPTSIAdbrTx_Object = MibTableColumn
jnxMbgPgwV2ICsNewPTSIAdbrTx = _JnxMbgPgwV2ICsNewPTSIAdbrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 98),
    _JnxMbgPgwV2ICsNewPTSIAdbrTx_Type()
)
jnxMbgPgwV2ICsNewPTSIAdbrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNewPTSIAdbrTx.setStatus("current")
_JnxMbgPgwV2ICsCtxNotFndRx_Type = Counter64
_JnxMbgPgwV2ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgPgwV2ICsCtxNotFndRx = _JnxMbgPgwV2ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 99),
    _JnxMbgPgwV2ICsCtxNotFndRx_Type()
)
jnxMbgPgwV2ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsCtxNotFndRx.setStatus("current")
_JnxMbgPgwV2ICsCtxNotFndTx_Type = Counter64
_JnxMbgPgwV2ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgPgwV2ICsCtxNotFndTx = _JnxMbgPgwV2ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 100),
    _JnxMbgPgwV2ICsCtxNotFndTx_Type()
)
jnxMbgPgwV2ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsCtxNotFndTx.setStatus("current")
_JnxMbgPgwV2ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwV2ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwV2ICsInvMsgFmtRx = _JnxMbgPgwV2ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 101),
    _JnxMbgPgwV2ICsInvMsgFmtRx_Type()
)
jnxMbgPgwV2ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwV2ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwV2ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwV2ICsInvMsgFmtTx = _JnxMbgPgwV2ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 102),
    _JnxMbgPgwV2ICsInvMsgFmtTx_Type()
)
jnxMbgPgwV2ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwV2ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwV2ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwV2ICsVerNotSuppRx = _JnxMbgPgwV2ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 103),
    _JnxMbgPgwV2ICsVerNotSuppRx_Type()
)
jnxMbgPgwV2ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwV2ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwV2ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwV2ICsVerNotSuppTx = _JnxMbgPgwV2ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 104),
    _JnxMbgPgwV2ICsVerNotSuppTx_Type()
)
jnxMbgPgwV2ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwV2ICsInvLenRx_Type = Counter64
_JnxMbgPgwV2ICsInvLenRx_Object = MibTableColumn
jnxMbgPgwV2ICsInvLenRx = _JnxMbgPgwV2ICsInvLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 105),
    _JnxMbgPgwV2ICsInvLenRx_Type()
)
jnxMbgPgwV2ICsInvLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsInvLenRx.setStatus("current")
_JnxMbgPgwV2ICsInvLenTx_Type = Counter64
_JnxMbgPgwV2ICsInvLenTx_Object = MibTableColumn
jnxMbgPgwV2ICsInvLenTx = _JnxMbgPgwV2ICsInvLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 106),
    _JnxMbgPgwV2ICsInvLenTx_Type()
)
jnxMbgPgwV2ICsInvLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsInvLenTx.setStatus("current")
_JnxMbgPgwV2ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwV2ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwV2ICsServNotSuppRx = _JnxMbgPgwV2ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 107),
    _JnxMbgPgwV2ICsServNotSuppRx_Type()
)
jnxMbgPgwV2ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwV2ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwV2ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwV2ICsServNotSuppTx = _JnxMbgPgwV2ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 108),
    _JnxMbgPgwV2ICsServNotSuppTx_Type()
)
jnxMbgPgwV2ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwV2ICsManIEIncorrRx_Type = Counter64
_JnxMbgPgwV2ICsManIEIncorrRx_Object = MibTableColumn
jnxMbgPgwV2ICsManIEIncorrRx = _JnxMbgPgwV2ICsManIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 109),
    _JnxMbgPgwV2ICsManIEIncorrRx_Type()
)
jnxMbgPgwV2ICsManIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsManIEIncorrRx.setStatus("current")
_JnxMbgPgwV2ICsManIEIncorrTx_Type = Counter64
_JnxMbgPgwV2ICsManIEIncorrTx_Object = MibTableColumn
jnxMbgPgwV2ICsManIEIncorrTx = _JnxMbgPgwV2ICsManIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 110),
    _JnxMbgPgwV2ICsManIEIncorrTx_Type()
)
jnxMbgPgwV2ICsManIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsManIEIncorrTx.setStatus("current")
_JnxMbgPgwV2ICsManIEMissRx_Type = Counter64
_JnxMbgPgwV2ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwV2ICsManIEMissRx = _JnxMbgPgwV2ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 111),
    _JnxMbgPgwV2ICsManIEMissRx_Type()
)
jnxMbgPgwV2ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsManIEMissRx.setStatus("current")
_JnxMbgPgwV2ICsManIEMissTx_Type = Counter64
_JnxMbgPgwV2ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwV2ICsManIEMissTx = _JnxMbgPgwV2ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 112),
    _JnxMbgPgwV2ICsManIEMissTx_Type()
)
jnxMbgPgwV2ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsManIEMissTx.setStatus("current")
_JnxMbgPgwV2ICsOptIEIncorrRx_Type = Counter64
_JnxMbgPgwV2ICsOptIEIncorrRx_Object = MibTableColumn
jnxMbgPgwV2ICsOptIEIncorrRx = _JnxMbgPgwV2ICsOptIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 113),
    _JnxMbgPgwV2ICsOptIEIncorrRx_Type()
)
jnxMbgPgwV2ICsOptIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsOptIEIncorrRx.setStatus("current")
_JnxMbgPgwV2ICsOptIEIncorrTx_Type = Counter64
_JnxMbgPgwV2ICsOptIEIncorrTx_Object = MibTableColumn
jnxMbgPgwV2ICsOptIEIncorrTx = _JnxMbgPgwV2ICsOptIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 114),
    _JnxMbgPgwV2ICsOptIEIncorrTx_Type()
)
jnxMbgPgwV2ICsOptIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsOptIEIncorrTx.setStatus("current")
_JnxMbgPgwV2ICsSysFailRx_Type = Counter64
_JnxMbgPgwV2ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwV2ICsSysFailRx = _JnxMbgPgwV2ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 115),
    _JnxMbgPgwV2ICsSysFailRx_Type()
)
jnxMbgPgwV2ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsSysFailRx.setStatus("current")
_JnxMbgPgwV2ICsSysFailTx_Type = Counter64
_JnxMbgPgwV2ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwV2ICsSysFailTx = _JnxMbgPgwV2ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 116),
    _JnxMbgPgwV2ICsSysFailTx_Type()
)
jnxMbgPgwV2ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsSysFailTx.setStatus("current")
_JnxMbgPgwV2ICsNoResRx_Type = Counter64
_JnxMbgPgwV2ICsNoResRx_Object = MibTableColumn
jnxMbgPgwV2ICsNoResRx = _JnxMbgPgwV2ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 117),
    _JnxMbgPgwV2ICsNoResRx_Type()
)
jnxMbgPgwV2ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNoResRx.setStatus("current")
_JnxMbgPgwV2ICsNoResTx_Type = Counter64
_JnxMbgPgwV2ICsNoResTx_Object = MibTableColumn
jnxMbgPgwV2ICsNoResTx = _JnxMbgPgwV2ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 118),
    _JnxMbgPgwV2ICsNoResTx_Type()
)
jnxMbgPgwV2ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNoResTx.setStatus("current")
_JnxMbgPgwV2ICsTFTSMANTErRx_Type = Counter64
_JnxMbgPgwV2ICsTFTSMANTErRx_Object = MibTableColumn
jnxMbgPgwV2ICsTFTSMANTErRx = _JnxMbgPgwV2ICsTFTSMANTErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 119),
    _JnxMbgPgwV2ICsTFTSMANTErRx_Type()
)
jnxMbgPgwV2ICsTFTSMANTErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsTFTSMANTErRx.setStatus("current")
_JnxMbgPgwV2ICsTFTSMANTErTx_Type = Counter64
_JnxMbgPgwV2ICsTFTSMANTErTx_Object = MibTableColumn
jnxMbgPgwV2ICsTFTSMANTErTx = _JnxMbgPgwV2ICsTFTSMANTErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 120),
    _JnxMbgPgwV2ICsTFTSMANTErTx_Type()
)
jnxMbgPgwV2ICsTFTSMANTErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsTFTSMANTErTx.setStatus("current")
_JnxMbgPgwV2ICsTFTSysErrRx_Type = Counter64
_JnxMbgPgwV2ICsTFTSysErrRx_Object = MibTableColumn
jnxMbgPgwV2ICsTFTSysErrRx = _JnxMbgPgwV2ICsTFTSysErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 121),
    _JnxMbgPgwV2ICsTFTSysErrRx_Type()
)
jnxMbgPgwV2ICsTFTSysErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsTFTSysErrRx.setStatus("current")
_JnxMbgPgwV2ICsTFTSysErrTx_Type = Counter64
_JnxMbgPgwV2ICsTFTSysErrTx_Object = MibTableColumn
jnxMbgPgwV2ICsTFTSysErrTx = _JnxMbgPgwV2ICsTFTSysErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 122),
    _JnxMbgPgwV2ICsTFTSysErrTx_Type()
)
jnxMbgPgwV2ICsTFTSysErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsTFTSysErrTx.setStatus("current")
_JnxMbgPgwV2ICsPkFltManErrRx_Type = Counter64
_JnxMbgPgwV2ICsPkFltManErrRx_Object = MibTableColumn
jnxMbgPgwV2ICsPkFltManErrRx = _JnxMbgPgwV2ICsPkFltManErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 123),
    _JnxMbgPgwV2ICsPkFltManErrRx_Type()
)
jnxMbgPgwV2ICsPkFltManErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPkFltManErrRx.setStatus("current")
_JnxMbgPgwV2ICsPkFltManErrTx_Type = Counter64
_JnxMbgPgwV2ICsPkFltManErrTx_Object = MibTableColumn
jnxMbgPgwV2ICsPkFltManErrTx = _JnxMbgPgwV2ICsPkFltManErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 124),
    _JnxMbgPgwV2ICsPkFltManErrTx_Type()
)
jnxMbgPgwV2ICsPkFltManErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPkFltManErrTx.setStatus("current")
_JnxMbgPgwV2ICsPkFltSynErrRx_Type = Counter64
_JnxMbgPgwV2ICsPkFltSynErrRx_Object = MibTableColumn
jnxMbgPgwV2ICsPkFltSynErrRx = _JnxMbgPgwV2ICsPkFltSynErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 125),
    _JnxMbgPgwV2ICsPkFltSynErrRx_Type()
)
jnxMbgPgwV2ICsPkFltSynErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPkFltSynErrRx.setStatus("current")
_JnxMbgPgwV2ICsPkFltSynErrTx_Type = Counter64
_JnxMbgPgwV2ICsPkFltSynErrTx_Object = MibTableColumn
jnxMbgPgwV2ICsPkFltSynErrTx = _JnxMbgPgwV2ICsPkFltSynErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 126),
    _JnxMbgPgwV2ICsPkFltSynErrTx_Type()
)
jnxMbgPgwV2ICsPkFltSynErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPkFltSynErrTx.setStatus("current")
_JnxMbgPgwV2ICsMisUnknAPNRx_Type = Counter64
_JnxMbgPgwV2ICsMisUnknAPNRx_Object = MibTableColumn
jnxMbgPgwV2ICsMisUnknAPNRx = _JnxMbgPgwV2ICsMisUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 127),
    _JnxMbgPgwV2ICsMisUnknAPNRx_Type()
)
jnxMbgPgwV2ICsMisUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsMisUnknAPNRx.setStatus("current")
_JnxMbgPgwV2ICsMisUnknAPNTx_Type = Counter64
_JnxMbgPgwV2ICsMisUnknAPNTx_Object = MibTableColumn
jnxMbgPgwV2ICsMisUnknAPNTx = _JnxMbgPgwV2ICsMisUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 128),
    _JnxMbgPgwV2ICsMisUnknAPNTx_Type()
)
jnxMbgPgwV2ICsMisUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsMisUnknAPNTx.setStatus("current")
_JnxMbgPgwV2ICsUnexpRptIERx_Type = Counter64
_JnxMbgPgwV2ICsUnexpRptIERx_Object = MibTableColumn
jnxMbgPgwV2ICsUnexpRptIERx = _JnxMbgPgwV2ICsUnexpRptIERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 129),
    _JnxMbgPgwV2ICsUnexpRptIERx_Type()
)
jnxMbgPgwV2ICsUnexpRptIERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUnexpRptIERx.setStatus("current")
_JnxMbgPgwV2ICsUnexpRptIETx_Type = Counter64
_JnxMbgPgwV2ICsUnexpRptIETx_Object = MibTableColumn
jnxMbgPgwV2ICsUnexpRptIETx = _JnxMbgPgwV2ICsUnexpRptIETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 130),
    _JnxMbgPgwV2ICsUnexpRptIETx_Type()
)
jnxMbgPgwV2ICsUnexpRptIETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUnexpRptIETx.setStatus("current")
_JnxMbgPgwV2ICsGREKeyNtFdRx_Type = Counter64
_JnxMbgPgwV2ICsGREKeyNtFdRx_Object = MibTableColumn
jnxMbgPgwV2ICsGREKeyNtFdRx = _JnxMbgPgwV2ICsGREKeyNtFdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 131),
    _JnxMbgPgwV2ICsGREKeyNtFdRx_Type()
)
jnxMbgPgwV2ICsGREKeyNtFdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsGREKeyNtFdRx.setStatus("current")
_JnxMbgPgwV2ICsGREKeyNtFdTx_Type = Counter64
_JnxMbgPgwV2ICsGREKeyNtFdTx_Object = MibTableColumn
jnxMbgPgwV2ICsGREKeyNtFdTx = _JnxMbgPgwV2ICsGREKeyNtFdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 132),
    _JnxMbgPgwV2ICsGREKeyNtFdTx_Type()
)
jnxMbgPgwV2ICsGREKeyNtFdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsGREKeyNtFdTx.setStatus("current")
_JnxMbgPgwV2ICsRelocFailRx_Type = Counter64
_JnxMbgPgwV2ICsRelocFailRx_Object = MibTableColumn
jnxMbgPgwV2ICsRelocFailRx = _JnxMbgPgwV2ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 133),
    _JnxMbgPgwV2ICsRelocFailRx_Type()
)
jnxMbgPgwV2ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsRelocFailRx.setStatus("current")
_JnxMbgPgwV2ICsRelocFailTx_Type = Counter64
_JnxMbgPgwV2ICsRelocFailTx_Object = MibTableColumn
jnxMbgPgwV2ICsRelocFailTx = _JnxMbgPgwV2ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 134),
    _JnxMbgPgwV2ICsRelocFailTx_Type()
)
jnxMbgPgwV2ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsRelocFailTx.setStatus("current")
_JnxMbgPgwV2ICsDeniedINRatRx_Type = Counter64
_JnxMbgPgwV2ICsDeniedINRatRx_Object = MibTableColumn
jnxMbgPgwV2ICsDeniedINRatRx = _JnxMbgPgwV2ICsDeniedINRatRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 135),
    _JnxMbgPgwV2ICsDeniedINRatRx_Type()
)
jnxMbgPgwV2ICsDeniedINRatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsDeniedINRatRx.setStatus("current")
_JnxMbgPgwV2ICsDeniedINRatTx_Type = Counter64
_JnxMbgPgwV2ICsDeniedINRatTx_Object = MibTableColumn
jnxMbgPgwV2ICsDeniedINRatTx = _JnxMbgPgwV2ICsDeniedINRatTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 136),
    _JnxMbgPgwV2ICsDeniedINRatTx_Type()
)
jnxMbgPgwV2ICsDeniedINRatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsDeniedINRatTx.setStatus("current")
_JnxMbgPgwV2ICsPTNotSuppRx_Type = Counter64
_JnxMbgPgwV2ICsPTNotSuppRx_Object = MibTableColumn
jnxMbgPgwV2ICsPTNotSuppRx = _JnxMbgPgwV2ICsPTNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 137),
    _JnxMbgPgwV2ICsPTNotSuppRx_Type()
)
jnxMbgPgwV2ICsPTNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPTNotSuppRx.setStatus("current")
_JnxMbgPgwV2ICsPTNotSuppTx_Type = Counter64
_JnxMbgPgwV2ICsPTNotSuppTx_Object = MibTableColumn
jnxMbgPgwV2ICsPTNotSuppTx = _JnxMbgPgwV2ICsPTNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 138),
    _JnxMbgPgwV2ICsPTNotSuppTx_Type()
)
jnxMbgPgwV2ICsPTNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPTNotSuppTx.setStatus("current")
_JnxMbgPgwV2ICsAllDynAdOccRx_Type = Counter64
_JnxMbgPgwV2ICsAllDynAdOccRx_Object = MibTableColumn
jnxMbgPgwV2ICsAllDynAdOccRx = _JnxMbgPgwV2ICsAllDynAdOccRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 139),
    _JnxMbgPgwV2ICsAllDynAdOccRx_Type()
)
jnxMbgPgwV2ICsAllDynAdOccRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAllDynAdOccRx.setStatus("current")
_JnxMbgPgwV2ICsAllDynAdOccTx_Type = Counter64
_JnxMbgPgwV2ICsAllDynAdOccTx_Object = MibTableColumn
jnxMbgPgwV2ICsAllDynAdOccTx = _JnxMbgPgwV2ICsAllDynAdOccTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 140),
    _JnxMbgPgwV2ICsAllDynAdOccTx_Type()
)
jnxMbgPgwV2ICsAllDynAdOccTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAllDynAdOccTx.setStatus("current")
_JnxMbgPgwV2ICsNOTFTUECTXRx_Type = Counter64
_JnxMbgPgwV2ICsNOTFTUECTXRx_Object = MibTableColumn
jnxMbgPgwV2ICsNOTFTUECTXRx = _JnxMbgPgwV2ICsNOTFTUECTXRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 141),
    _JnxMbgPgwV2ICsNOTFTUECTXRx_Type()
)
jnxMbgPgwV2ICsNOTFTUECTXRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNOTFTUECTXRx.setStatus("current")
_JnxMbgPgwV2ICsNOTFTUECTXTx_Type = Counter64
_JnxMbgPgwV2ICsNOTFTUECTXTx_Object = MibTableColumn
jnxMbgPgwV2ICsNOTFTUECTXTx = _JnxMbgPgwV2ICsNOTFTUECTXTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 142),
    _JnxMbgPgwV2ICsNOTFTUECTXTx_Type()
)
jnxMbgPgwV2ICsNOTFTUECTXTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNOTFTUECTXTx.setStatus("current")
_JnxMbgPgwV2ICsProtoNtSupRx_Type = Counter64
_JnxMbgPgwV2ICsProtoNtSupRx_Object = MibTableColumn
jnxMbgPgwV2ICsProtoNtSupRx = _JnxMbgPgwV2ICsProtoNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 143),
    _JnxMbgPgwV2ICsProtoNtSupRx_Type()
)
jnxMbgPgwV2ICsProtoNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsProtoNtSupRx.setStatus("current")
_JnxMbgPgwV2ICsProtoNtSupTx_Type = Counter64
_JnxMbgPgwV2ICsProtoNtSupTx_Object = MibTableColumn
jnxMbgPgwV2ICsProtoNtSupTx = _JnxMbgPgwV2ICsProtoNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 144),
    _JnxMbgPgwV2ICsProtoNtSupTx_Type()
)
jnxMbgPgwV2ICsProtoNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsProtoNtSupTx.setStatus("current")
_JnxMbgPgwV2ICsUENotRespRx_Type = Counter64
_JnxMbgPgwV2ICsUENotRespRx_Object = MibTableColumn
jnxMbgPgwV2ICsUENotRespRx = _JnxMbgPgwV2ICsUENotRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 145),
    _JnxMbgPgwV2ICsUENotRespRx_Type()
)
jnxMbgPgwV2ICsUENotRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUENotRespRx.setStatus("current")
_JnxMbgPgwV2ICsUENotRespTx_Type = Counter64
_JnxMbgPgwV2ICsUENotRespTx_Object = MibTableColumn
jnxMbgPgwV2ICsUENotRespTx = _JnxMbgPgwV2ICsUENotRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 146),
    _JnxMbgPgwV2ICsUENotRespTx_Type()
)
jnxMbgPgwV2ICsUENotRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUENotRespTx.setStatus("current")
_JnxMbgPgwV2ICsUERefusesRx_Type = Counter64
_JnxMbgPgwV2ICsUERefusesRx_Object = MibTableColumn
jnxMbgPgwV2ICsUERefusesRx = _JnxMbgPgwV2ICsUERefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 147),
    _JnxMbgPgwV2ICsUERefusesRx_Type()
)
jnxMbgPgwV2ICsUERefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUERefusesRx.setStatus("current")
_JnxMbgPgwV2ICsUERefusesTx_Type = Counter64
_JnxMbgPgwV2ICsUERefusesTx_Object = MibTableColumn
jnxMbgPgwV2ICsUERefusesTx = _JnxMbgPgwV2ICsUERefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 148),
    _JnxMbgPgwV2ICsUERefusesTx_Type()
)
jnxMbgPgwV2ICsUERefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUERefusesTx.setStatus("current")
_JnxMbgPgwV2ICsServDeniedRx_Type = Counter64
_JnxMbgPgwV2ICsServDeniedRx_Object = MibTableColumn
jnxMbgPgwV2ICsServDeniedRx = _JnxMbgPgwV2ICsServDeniedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 149),
    _JnxMbgPgwV2ICsServDeniedRx_Type()
)
jnxMbgPgwV2ICsServDeniedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsServDeniedRx.setStatus("current")
_JnxMbgPgwV2ICsServDeniedTx_Type = Counter64
_JnxMbgPgwV2ICsServDeniedTx_Object = MibTableColumn
jnxMbgPgwV2ICsServDeniedTx = _JnxMbgPgwV2ICsServDeniedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 150),
    _JnxMbgPgwV2ICsServDeniedTx_Type()
)
jnxMbgPgwV2ICsServDeniedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsServDeniedTx.setStatus("current")
_JnxMbgPgwV2ICsUnabPageUERx_Type = Counter64
_JnxMbgPgwV2ICsUnabPageUERx_Object = MibTableColumn
jnxMbgPgwV2ICsUnabPageUERx = _JnxMbgPgwV2ICsUnabPageUERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 151),
    _JnxMbgPgwV2ICsUnabPageUERx_Type()
)
jnxMbgPgwV2ICsUnabPageUERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUnabPageUERx.setStatus("current")
_JnxMbgPgwV2ICsUnabPageUETx_Type = Counter64
_JnxMbgPgwV2ICsUnabPageUETx_Object = MibTableColumn
jnxMbgPgwV2ICsUnabPageUETx = _JnxMbgPgwV2ICsUnabPageUETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 152),
    _JnxMbgPgwV2ICsUnabPageUETx_Type()
)
jnxMbgPgwV2ICsUnabPageUETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUnabPageUETx.setStatus("current")
_JnxMbgPgwV2ICsNoMemRx_Type = Counter64
_JnxMbgPgwV2ICsNoMemRx_Object = MibTableColumn
jnxMbgPgwV2ICsNoMemRx = _JnxMbgPgwV2ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 153),
    _JnxMbgPgwV2ICsNoMemRx_Type()
)
jnxMbgPgwV2ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNoMemRx.setStatus("current")
_JnxMbgPgwV2ICsNoMemTx_Type = Counter64
_JnxMbgPgwV2ICsNoMemTx_Object = MibTableColumn
jnxMbgPgwV2ICsNoMemTx = _JnxMbgPgwV2ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 154),
    _JnxMbgPgwV2ICsNoMemTx_Type()
)
jnxMbgPgwV2ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsNoMemTx.setStatus("current")
_JnxMbgPgwV2ICsUserAUTHFlRx_Type = Counter64
_JnxMbgPgwV2ICsUserAUTHFlRx_Object = MibTableColumn
jnxMbgPgwV2ICsUserAUTHFlRx = _JnxMbgPgwV2ICsUserAUTHFlRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 155),
    _JnxMbgPgwV2ICsUserAUTHFlRx_Type()
)
jnxMbgPgwV2ICsUserAUTHFlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUserAUTHFlRx.setStatus("current")
_JnxMbgPgwV2ICsUserAUTHFlTx_Type = Counter64
_JnxMbgPgwV2ICsUserAUTHFlTx_Object = MibTableColumn
jnxMbgPgwV2ICsUserAUTHFlTx = _JnxMbgPgwV2ICsUserAUTHFlTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 156),
    _JnxMbgPgwV2ICsUserAUTHFlTx_Type()
)
jnxMbgPgwV2ICsUserAUTHFlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUserAUTHFlTx.setStatus("current")
_JnxMbgPgwV2ICsAPNAcsDenRx_Type = Counter64
_JnxMbgPgwV2ICsAPNAcsDenRx_Object = MibTableColumn
jnxMbgPgwV2ICsAPNAcsDenRx = _JnxMbgPgwV2ICsAPNAcsDenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 157),
    _JnxMbgPgwV2ICsAPNAcsDenRx_Type()
)
jnxMbgPgwV2ICsAPNAcsDenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAPNAcsDenRx.setStatus("current")
_JnxMbgPgwV2ICsAPNAcsDenTx_Type = Counter64
_JnxMbgPgwV2ICsAPNAcsDenTx_Object = MibTableColumn
jnxMbgPgwV2ICsAPNAcsDenTx = _JnxMbgPgwV2ICsAPNAcsDenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 158),
    _JnxMbgPgwV2ICsAPNAcsDenTx_Type()
)
jnxMbgPgwV2ICsAPNAcsDenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAPNAcsDenTx.setStatus("current")
_JnxMbgPgwV2ICsReqRejRx_Type = Counter64
_JnxMbgPgwV2ICsReqRejRx_Object = MibTableColumn
jnxMbgPgwV2ICsReqRejRx = _JnxMbgPgwV2ICsReqRejRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 159),
    _JnxMbgPgwV2ICsReqRejRx_Type()
)
jnxMbgPgwV2ICsReqRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsReqRejRx.setStatus("current")
_JnxMbgPgwV2ICsReqRejTx_Type = Counter64
_JnxMbgPgwV2ICsReqRejTx_Object = MibTableColumn
jnxMbgPgwV2ICsReqRejTx = _JnxMbgPgwV2ICsReqRejTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 160),
    _JnxMbgPgwV2ICsReqRejTx_Type()
)
jnxMbgPgwV2ICsReqRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsReqRejTx.setStatus("current")
_JnxMbgPgwV2ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwV2ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwV2ICsPTMSISigMMRx = _JnxMbgPgwV2ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 161),
    _JnxMbgPgwV2ICsPTMSISigMMRx_Type()
)
jnxMbgPgwV2ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwV2ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwV2ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwV2ICsPTMSISigMMTx = _JnxMbgPgwV2ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 162),
    _JnxMbgPgwV2ICsPTMSISigMMTx_Type()
)
jnxMbgPgwV2ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwV2ICsIMSINotKnRx_Type = Counter64
_JnxMbgPgwV2ICsIMSINotKnRx_Object = MibTableColumn
jnxMbgPgwV2ICsIMSINotKnRx = _JnxMbgPgwV2ICsIMSINotKnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 163),
    _JnxMbgPgwV2ICsIMSINotKnRx_Type()
)
jnxMbgPgwV2ICsIMSINotKnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsIMSINotKnRx.setStatus("current")
_JnxMbgPgwV2ICsIMSINotKnTx_Type = Counter64
_JnxMbgPgwV2ICsIMSINotKnTx_Object = MibTableColumn
jnxMbgPgwV2ICsIMSINotKnTx = _JnxMbgPgwV2ICsIMSINotKnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 164),
    _JnxMbgPgwV2ICsIMSINotKnTx_Type()
)
jnxMbgPgwV2ICsIMSINotKnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsIMSINotKnTx.setStatus("current")
_JnxMbgPgwV2ICsCondIEMsRx_Type = Counter64
_JnxMbgPgwV2ICsCondIEMsRx_Object = MibTableColumn
jnxMbgPgwV2ICsCondIEMsRx = _JnxMbgPgwV2ICsCondIEMsRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 165),
    _JnxMbgPgwV2ICsCondIEMsRx_Type()
)
jnxMbgPgwV2ICsCondIEMsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsCondIEMsRx.setStatus("current")
_JnxMbgPgwV2ICsCondIEMsTx_Type = Counter64
_JnxMbgPgwV2ICsCondIEMsTx_Object = MibTableColumn
jnxMbgPgwV2ICsCondIEMsTx = _JnxMbgPgwV2ICsCondIEMsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 166),
    _JnxMbgPgwV2ICsCondIEMsTx_Type()
)
jnxMbgPgwV2ICsCondIEMsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsCondIEMsTx.setStatus("current")
_JnxMbgPgwV2ICsAPNResTIncRx_Type = Counter64
_JnxMbgPgwV2ICsAPNResTIncRx_Object = MibTableColumn
jnxMbgPgwV2ICsAPNResTIncRx = _JnxMbgPgwV2ICsAPNResTIncRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 167),
    _JnxMbgPgwV2ICsAPNResTIncRx_Type()
)
jnxMbgPgwV2ICsAPNResTIncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAPNResTIncRx.setStatus("current")
_JnxMbgPgwV2ICsAPNResTIncTx_Type = Counter64
_JnxMbgPgwV2ICsAPNResTIncTx_Object = MibTableColumn
jnxMbgPgwV2ICsAPNResTIncTx = _JnxMbgPgwV2ICsAPNResTIncTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 168),
    _JnxMbgPgwV2ICsAPNResTIncTx_Type()
)
jnxMbgPgwV2ICsAPNResTIncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsAPNResTIncTx.setStatus("current")
_JnxMbgPgwV2ICsUnknownRx_Type = Counter64
_JnxMbgPgwV2ICsUnknownRx_Object = MibTableColumn
jnxMbgPgwV2ICsUnknownRx = _JnxMbgPgwV2ICsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 169),
    _JnxMbgPgwV2ICsUnknownRx_Type()
)
jnxMbgPgwV2ICsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUnknownRx.setStatus("current")
_JnxMbgPgwV2ICsUnknownTx_Type = Counter64
_JnxMbgPgwV2ICsUnknownTx_Object = MibTableColumn
jnxMbgPgwV2ICsUnknownTx = _JnxMbgPgwV2ICsUnknownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 170),
    _JnxMbgPgwV2ICsUnknownTx_Type()
)
jnxMbgPgwV2ICsUnknownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ICsUnknownTx.setStatus("current")
_JnxMbgPgwV1ProtocolErrRx_Type = Counter64
_JnxMbgPgwV1ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwV1ProtocolErrRx = _JnxMbgPgwV1ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 171),
    _JnxMbgPgwV1ProtocolErrRx_Type()
)
jnxMbgPgwV1ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ProtocolErrRx.setStatus("current")
_JnxMbgPgwV1UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwV1UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwV1UnSupportedMsgRx = _JnxMbgPgwV1UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 172),
    _JnxMbgPgwV1UnSupportedMsgRx_Type()
)
jnxMbgPgwV1UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwV1T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwV1T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwV1T3RespTmrExpRx = _JnxMbgPgwV1T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 173),
    _JnxMbgPgwV1T3RespTmrExpRx_Type()
)
jnxMbgPgwV1T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwV1GlbNumMsgRx_Type = Counter64
_JnxMbgPgwV1GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwV1GlbNumMsgRx = _JnxMbgPgwV1GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 174),
    _JnxMbgPgwV1GlbNumMsgRx_Type()
)
jnxMbgPgwV1GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbNumMsgRx.setStatus("current")
_JnxMbgPgwV1GlbNumMsgTx_Type = Counter64
_JnxMbgPgwV1GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwV1GlbNumMsgTx = _JnxMbgPgwV1GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 175),
    _JnxMbgPgwV1GlbNumMsgTx_Type()
)
jnxMbgPgwV1GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbNumMsgTx.setStatus("current")
_JnxMbgPgwV1GlbNumBytesRx_Type = Counter64
_JnxMbgPgwV1GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwV1GlbNumBytesRx = _JnxMbgPgwV1GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 176),
    _JnxMbgPgwV1GlbNumBytesRx_Type()
)
jnxMbgPgwV1GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbNumBytesRx.setStatus("current")
_JnxMbgPgwV1GlbNumBytesTx_Type = Counter64
_JnxMbgPgwV1GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwV1GlbNumBytesTx = _JnxMbgPgwV1GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 177),
    _JnxMbgPgwV1GlbNumBytesTx_Type()
)
jnxMbgPgwV1GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbNumBytesTx.setStatus("current")
_JnxMbgPgwV1GlbEchoReqRx_Type = Counter64
_JnxMbgPgwV1GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwV1GlbEchoReqRx = _JnxMbgPgwV1GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 178),
    _JnxMbgPgwV1GlbEchoReqRx_Type()
)
jnxMbgPgwV1GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbEchoReqRx.setStatus("current")
_JnxMbgPgwV1GlbEchoReqTx_Type = Counter64
_JnxMbgPgwV1GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwV1GlbEchoReqTx = _JnxMbgPgwV1GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 179),
    _JnxMbgPgwV1GlbEchoReqTx_Type()
)
jnxMbgPgwV1GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbEchoReqTx.setStatus("current")
_JnxMbgPgwV1GlbEchoRespRx_Type = Counter64
_JnxMbgPgwV1GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwV1GlbEchoRespRx = _JnxMbgPgwV1GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 180),
    _JnxMbgPgwV1GlbEchoRespRx_Type()
)
jnxMbgPgwV1GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbEchoRespRx.setStatus("current")
_JnxMbgPgwV1GlbEchoRespTx_Type = Counter64
_JnxMbgPgwV1GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwV1GlbEchoRespTx = _JnxMbgPgwV1GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 181),
    _JnxMbgPgwV1GlbEchoRespTx_Type()
)
jnxMbgPgwV1GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1GlbEchoRespTx.setStatus("current")
_JnxMbgPgwV1VerNotSupRx_Type = Counter64
_JnxMbgPgwV1VerNotSupRx_Object = MibTableColumn
jnxMbgPgwV1VerNotSupRx = _JnxMbgPgwV1VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 182),
    _JnxMbgPgwV1VerNotSupRx_Type()
)
jnxMbgPgwV1VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1VerNotSupRx.setStatus("current")
_JnxMbgPgwV1VerNotSupTx_Type = Counter64
_JnxMbgPgwV1VerNotSupTx_Object = MibTableColumn
jnxMbgPgwV1VerNotSupTx = _JnxMbgPgwV1VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 183),
    _JnxMbgPgwV1VerNotSupTx_Type()
)
jnxMbgPgwV1VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1VerNotSupTx.setStatus("current")
_JnxMbgPgwV1CrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV1CrtPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV1CrtPdpCxtReqRx = _JnxMbgPgwV1CrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 184),
    _JnxMbgPgwV1CrtPdpCxtReqRx_Type()
)
jnxMbgPgwV1CrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV1CrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV1CrtPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV1CrtPdpCxtReqTx = _JnxMbgPgwV1CrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 185),
    _JnxMbgPgwV1CrtPdpCxtReqTx_Type()
)
jnxMbgPgwV1CrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV1CrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV1CrtPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV1CrtPdpCxtRspRx = _JnxMbgPgwV1CrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 186),
    _JnxMbgPgwV1CrtPdpCxtRspRx_Type()
)
jnxMbgPgwV1CrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV1CrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV1CrtPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV1CrtPdpCxtRspTx = _JnxMbgPgwV1CrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 187),
    _JnxMbgPgwV1CrtPdpCxtRspTx_Type()
)
jnxMbgPgwV1CrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV1UpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV1UpdPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV1UpdPdpCxtReqRx = _JnxMbgPgwV1UpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 188),
    _JnxMbgPgwV1UpdPdpCxtReqRx_Type()
)
jnxMbgPgwV1UpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1UpdPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV1UpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV1UpdPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV1UpdPdpCxtReqTx = _JnxMbgPgwV1UpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 189),
    _JnxMbgPgwV1UpdPdpCxtReqTx_Type()
)
jnxMbgPgwV1UpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1UpdPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV1UpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV1UpdPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV1UpdPdpCxtRspRx = _JnxMbgPgwV1UpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 190),
    _JnxMbgPgwV1UpdPdpCxtRspRx_Type()
)
jnxMbgPgwV1UpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1UpdPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV1UpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV1UpdPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV1UpdPdpCxtRspTx = _JnxMbgPgwV1UpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 191),
    _JnxMbgPgwV1UpdPdpCxtRspTx_Type()
)
jnxMbgPgwV1UpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1UpdPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV1DelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV1DelPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV1DelPdpCxtReqRx = _JnxMbgPgwV1DelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 192),
    _JnxMbgPgwV1DelPdpCxtReqRx_Type()
)
jnxMbgPgwV1DelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV1DelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV1DelPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV1DelPdpCxtReqTx = _JnxMbgPgwV1DelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 193),
    _JnxMbgPgwV1DelPdpCxtReqTx_Type()
)
jnxMbgPgwV1DelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV1DelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV1DelPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV1DelPdpCxtRspRx = _JnxMbgPgwV1DelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 194),
    _JnxMbgPgwV1DelPdpCxtRspRx_Type()
)
jnxMbgPgwV1DelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV1DelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV1DelPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV1DelPdpCxtRspTx = _JnxMbgPgwV1DelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 195),
    _JnxMbgPgwV1DelPdpCxtRspTx_Type()
)
jnxMbgPgwV1DelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV1CrtAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV1CrtAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV1CrtAAPdpCxtReqRx = _JnxMbgPgwV1CrtAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 196),
    _JnxMbgPgwV1CrtAAPdpCxtReqRx_Type()
)
jnxMbgPgwV1CrtAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV1CrtAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV1CrtAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV1CrtAAPdpCxtReqTx = _JnxMbgPgwV1CrtAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 197),
    _JnxMbgPgwV1CrtAAPdpCxtReqTx_Type()
)
jnxMbgPgwV1CrtAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV1CrtAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV1CrtAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV1CrtAAPdpCxtRspRx = _JnxMbgPgwV1CrtAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 198),
    _JnxMbgPgwV1CrtAAPdpCxtRspRx_Type()
)
jnxMbgPgwV1CrtAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV1CrtAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV1CrtAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV1CrtAAPdpCxtRspTx = _JnxMbgPgwV1CrtAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 199),
    _JnxMbgPgwV1CrtAAPdpCxtRspTx_Type()
)
jnxMbgPgwV1CrtAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1CrtAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV1DelAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV1DelAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV1DelAAPdpCxtReqRx = _JnxMbgPgwV1DelAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 200),
    _JnxMbgPgwV1DelAAPdpCxtReqRx_Type()
)
jnxMbgPgwV1DelAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV1DelAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV1DelAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV1DelAAPdpCxtReqTx = _JnxMbgPgwV1DelAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 201),
    _JnxMbgPgwV1DelAAPdpCxtReqTx_Type()
)
jnxMbgPgwV1DelAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV1DelAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV1DelAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV1DelAAPdpCxtRspRx = _JnxMbgPgwV1DelAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 202),
    _JnxMbgPgwV1DelAAPdpCxtRspRx_Type()
)
jnxMbgPgwV1DelAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV1DelAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV1DelAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV1DelAAPdpCxtRspTx = _JnxMbgPgwV1DelAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 203),
    _JnxMbgPgwV1DelAAPdpCxtRspTx_Type()
)
jnxMbgPgwV1DelAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1DelAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV1ErrorIndRx_Type = Counter64
_JnxMbgPgwV1ErrorIndRx_Object = MibTableColumn
jnxMbgPgwV1ErrorIndRx = _JnxMbgPgwV1ErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 204),
    _JnxMbgPgwV1ErrorIndRx_Type()
)
jnxMbgPgwV1ErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ErrorIndRx.setStatus("current")
_JnxMbgPgwV1ErrorIndTx_Type = Counter64
_JnxMbgPgwV1ErrorIndTx_Object = MibTableColumn
jnxMbgPgwV1ErrorIndTx = _JnxMbgPgwV1ErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 205),
    _JnxMbgPgwV1ErrorIndTx_Type()
)
jnxMbgPgwV1ErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ErrorIndTx.setStatus("current")
_JnxMbgPgwV1NotifReqRx_Type = Counter64
_JnxMbgPgwV1NotifReqRx_Object = MibTableColumn
jnxMbgPgwV1NotifReqRx = _JnxMbgPgwV1NotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 206),
    _JnxMbgPgwV1NotifReqRx_Type()
)
jnxMbgPgwV1NotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifReqRx.setStatus("current")
_JnxMbgPgwV1NotifReqTx_Type = Counter64
_JnxMbgPgwV1NotifReqTx_Object = MibTableColumn
jnxMbgPgwV1NotifReqTx = _JnxMbgPgwV1NotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 207),
    _JnxMbgPgwV1NotifReqTx_Type()
)
jnxMbgPgwV1NotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifReqTx.setStatus("current")
_JnxMbgPgwV1NotifRspRx_Type = Counter64
_JnxMbgPgwV1NotifRspRx_Object = MibTableColumn
jnxMbgPgwV1NotifRspRx = _JnxMbgPgwV1NotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 208),
    _JnxMbgPgwV1NotifRspRx_Type()
)
jnxMbgPgwV1NotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifRspRx.setStatus("current")
_JnxMbgPgwV1NotifRspTx_Type = Counter64
_JnxMbgPgwV1NotifRspTx_Object = MibTableColumn
jnxMbgPgwV1NotifRspTx = _JnxMbgPgwV1NotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 209),
    _JnxMbgPgwV1NotifRspTx_Type()
)
jnxMbgPgwV1NotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifRspTx.setStatus("current")
_JnxMbgPgwV1NotifRejReqRx_Type = Counter64
_JnxMbgPgwV1NotifRejReqRx_Object = MibTableColumn
jnxMbgPgwV1NotifRejReqRx = _JnxMbgPgwV1NotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 210),
    _JnxMbgPgwV1NotifRejReqRx_Type()
)
jnxMbgPgwV1NotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifRejReqRx.setStatus("current")
_JnxMbgPgwV1NotifRejReqTx_Type = Counter64
_JnxMbgPgwV1NotifRejReqTx_Object = MibTableColumn
jnxMbgPgwV1NotifRejReqTx = _JnxMbgPgwV1NotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 211),
    _JnxMbgPgwV1NotifRejReqTx_Type()
)
jnxMbgPgwV1NotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifRejReqTx.setStatus("current")
_JnxMbgPgwV1NotifRejRspRx_Type = Counter64
_JnxMbgPgwV1NotifRejRspRx_Object = MibTableColumn
jnxMbgPgwV1NotifRejRspRx = _JnxMbgPgwV1NotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 212),
    _JnxMbgPgwV1NotifRejRspRx_Type()
)
jnxMbgPgwV1NotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifRejRspRx.setStatus("current")
_JnxMbgPgwV1NotifRejRspTx_Type = Counter64
_JnxMbgPgwV1NotifRejRspTx_Object = MibTableColumn
jnxMbgPgwV1NotifRejRspTx = _JnxMbgPgwV1NotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 213),
    _JnxMbgPgwV1NotifRejRspTx_Type()
)
jnxMbgPgwV1NotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotifRejRspTx.setStatus("current")
_JnxMbgPgwV1RtInfReqRx_Type = Counter64
_JnxMbgPgwV1RtInfReqRx_Object = MibTableColumn
jnxMbgPgwV1RtInfReqRx = _JnxMbgPgwV1RtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 214),
    _JnxMbgPgwV1RtInfReqRx_Type()
)
jnxMbgPgwV1RtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1RtInfReqRx.setStatus("current")
_JnxMbgPgwV1RtInfReqTx_Type = Counter64
_JnxMbgPgwV1RtInfReqTx_Object = MibTableColumn
jnxMbgPgwV1RtInfReqTx = _JnxMbgPgwV1RtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 215),
    _JnxMbgPgwV1RtInfReqTx_Type()
)
jnxMbgPgwV1RtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1RtInfReqTx.setStatus("current")
_JnxMbgPgwV1RtInfRspRx_Type = Counter64
_JnxMbgPgwV1RtInfRspRx_Object = MibTableColumn
jnxMbgPgwV1RtInfRspRx = _JnxMbgPgwV1RtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 216),
    _JnxMbgPgwV1RtInfRspRx_Type()
)
jnxMbgPgwV1RtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1RtInfRspRx.setStatus("current")
_JnxMbgPgwV1RtInfRspTx_Type = Counter64
_JnxMbgPgwV1RtInfRspTx_Object = MibTableColumn
jnxMbgPgwV1RtInfRspTx = _JnxMbgPgwV1RtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 217),
    _JnxMbgPgwV1RtInfRspTx_Type()
)
jnxMbgPgwV1RtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1RtInfRspTx.setStatus("current")
_JnxMbgPgwV1FailRptReqRx_Type = Counter64
_JnxMbgPgwV1FailRptReqRx_Object = MibTableColumn
jnxMbgPgwV1FailRptReqRx = _JnxMbgPgwV1FailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 218),
    _JnxMbgPgwV1FailRptReqRx_Type()
)
jnxMbgPgwV1FailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1FailRptReqRx.setStatus("current")
_JnxMbgPgwV1FailRptReqTx_Type = Counter64
_JnxMbgPgwV1FailRptReqTx_Object = MibTableColumn
jnxMbgPgwV1FailRptReqTx = _JnxMbgPgwV1FailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 219),
    _JnxMbgPgwV1FailRptReqTx_Type()
)
jnxMbgPgwV1FailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1FailRptReqTx.setStatus("current")
_JnxMbgPgwV1FailRptRspRx_Type = Counter64
_JnxMbgPgwV1FailRptRspRx_Object = MibTableColumn
jnxMbgPgwV1FailRptRspRx = _JnxMbgPgwV1FailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 220),
    _JnxMbgPgwV1FailRptRspRx_Type()
)
jnxMbgPgwV1FailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1FailRptRspRx.setStatus("current")
_JnxMbgPgwV1FailRptRspTx_Type = Counter64
_JnxMbgPgwV1FailRptRspTx_Object = MibTableColumn
jnxMbgPgwV1FailRptRspTx = _JnxMbgPgwV1FailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 221),
    _JnxMbgPgwV1FailRptRspTx_Type()
)
jnxMbgPgwV1FailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1FailRptRspTx.setStatus("current")
_JnxMbgPgwV1NotMSPresReqRx_Type = Counter64
_JnxMbgPgwV1NotMSPresReqRx_Object = MibTableColumn
jnxMbgPgwV1NotMSPresReqRx = _JnxMbgPgwV1NotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 222),
    _JnxMbgPgwV1NotMSPresReqRx_Type()
)
jnxMbgPgwV1NotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotMSPresReqRx.setStatus("current")
_JnxMbgPgwV1NotMSPresReqTx_Type = Counter64
_JnxMbgPgwV1NotMSPresReqTx_Object = MibTableColumn
jnxMbgPgwV1NotMSPresReqTx = _JnxMbgPgwV1NotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 223),
    _JnxMbgPgwV1NotMSPresReqTx_Type()
)
jnxMbgPgwV1NotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotMSPresReqTx.setStatus("current")
_JnxMbgPgwV1NotMSPresRspRx_Type = Counter64
_JnxMbgPgwV1NotMSPresRspRx_Object = MibTableColumn
jnxMbgPgwV1NotMSPresRspRx = _JnxMbgPgwV1NotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 224),
    _JnxMbgPgwV1NotMSPresRspRx_Type()
)
jnxMbgPgwV1NotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotMSPresRspRx.setStatus("current")
_JnxMbgPgwV1NotMSPresRspTx_Type = Counter64
_JnxMbgPgwV1NotMSPresRspTx_Object = MibTableColumn
jnxMbgPgwV1NotMSPresRspTx = _JnxMbgPgwV1NotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 225),
    _JnxMbgPgwV1NotMSPresRspTx_Type()
)
jnxMbgPgwV1NotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1NotMSPresRspTx.setStatus("current")
_JnxMbgPgwV1ICsReqAcceptedRx_Type = Counter64
_JnxMbgPgwV1ICsReqAcceptedRx_Object = MibTableColumn
jnxMbgPgwV1ICsReqAcceptedRx = _JnxMbgPgwV1ICsReqAcceptedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 226),
    _JnxMbgPgwV1ICsReqAcceptedRx_Type()
)
jnxMbgPgwV1ICsReqAcceptedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsReqAcceptedRx.setStatus("current")
_JnxMbgPgwV1ICsReqAcceptedTx_Type = Counter64
_JnxMbgPgwV1ICsReqAcceptedTx_Object = MibTableColumn
jnxMbgPgwV1ICsReqAcceptedTx = _JnxMbgPgwV1ICsReqAcceptedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 227),
    _JnxMbgPgwV1ICsReqAcceptedTx_Type()
)
jnxMbgPgwV1ICsReqAcceptedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsReqAcceptedTx.setStatus("current")
_JnxMbgPgwV1ICsNonExistRx_Type = Counter64
_JnxMbgPgwV1ICsNonExistRx_Object = MibTableColumn
jnxMbgPgwV1ICsNonExistRx = _JnxMbgPgwV1ICsNonExistRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 228),
    _JnxMbgPgwV1ICsNonExistRx_Type()
)
jnxMbgPgwV1ICsNonExistRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNonExistRx.setStatus("current")
_JnxMbgPgwV1ICsNonExistTx_Type = Counter64
_JnxMbgPgwV1ICsNonExistTx_Object = MibTableColumn
jnxMbgPgwV1ICsNonExistTx = _JnxMbgPgwV1ICsNonExistTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 229),
    _JnxMbgPgwV1ICsNonExistTx_Type()
)
jnxMbgPgwV1ICsNonExistTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNonExistTx.setStatus("current")
_JnxMbgPgwV1ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwV1ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwV1ICsInvMsgFmtRx = _JnxMbgPgwV1ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 230),
    _JnxMbgPgwV1ICsInvMsgFmtRx_Type()
)
jnxMbgPgwV1ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwV1ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwV1ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwV1ICsInvMsgFmtTx = _JnxMbgPgwV1ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 231),
    _JnxMbgPgwV1ICsInvMsgFmtTx_Type()
)
jnxMbgPgwV1ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwV1ICsIMSINotKnownRx_Type = Counter64
_JnxMbgPgwV1ICsIMSINotKnownRx_Object = MibTableColumn
jnxMbgPgwV1ICsIMSINotKnownRx = _JnxMbgPgwV1ICsIMSINotKnownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 232),
    _JnxMbgPgwV1ICsIMSINotKnownRx_Type()
)
jnxMbgPgwV1ICsIMSINotKnownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsIMSINotKnownRx.setStatus("current")
_JnxMbgPgwV1ICsIMSINotKnownTx_Type = Counter64
_JnxMbgPgwV1ICsIMSINotKnownTx_Object = MibTableColumn
jnxMbgPgwV1ICsIMSINotKnownTx = _JnxMbgPgwV1ICsIMSINotKnownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 233),
    _JnxMbgPgwV1ICsIMSINotKnownTx_Type()
)
jnxMbgPgwV1ICsIMSINotKnownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsIMSINotKnownTx.setStatus("current")
_JnxMbgPgwV1ICsMSGRPSDetachRx_Type = Counter64
_JnxMbgPgwV1ICsMSGRPSDetachRx_Object = MibTableColumn
jnxMbgPgwV1ICsMSGRPSDetachRx = _JnxMbgPgwV1ICsMSGRPSDetachRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 234),
    _JnxMbgPgwV1ICsMSGRPSDetachRx_Type()
)
jnxMbgPgwV1ICsMSGRPSDetachRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMSGRPSDetachRx.setStatus("current")
_JnxMbgPgwV1ICsMSGRPSDetachTx_Type = Counter64
_JnxMbgPgwV1ICsMSGRPSDetachTx_Object = MibTableColumn
jnxMbgPgwV1ICsMSGRPSDetachTx = _JnxMbgPgwV1ICsMSGRPSDetachTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 235),
    _JnxMbgPgwV1ICsMSGRPSDetachTx_Type()
)
jnxMbgPgwV1ICsMSGRPSDetachTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMSGRPSDetachTx.setStatus("current")
_JnxMbgPgwV1ICsMSNotGRPSRespRx_Type = Counter64
_JnxMbgPgwV1ICsMSNotGRPSRespRx_Object = MibTableColumn
jnxMbgPgwV1ICsMSNotGRPSRespRx = _JnxMbgPgwV1ICsMSNotGRPSRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 236),
    _JnxMbgPgwV1ICsMSNotGRPSRespRx_Type()
)
jnxMbgPgwV1ICsMSNotGRPSRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMSNotGRPSRespRx.setStatus("current")
_JnxMbgPgwV1ICsMSNotGRPSRespTx_Type = Counter64
_JnxMbgPgwV1ICsMSNotGRPSRespTx_Object = MibTableColumn
jnxMbgPgwV1ICsMSNotGRPSRespTx = _JnxMbgPgwV1ICsMSNotGRPSRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 237),
    _JnxMbgPgwV1ICsMSNotGRPSRespTx_Type()
)
jnxMbgPgwV1ICsMSNotGRPSRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMSNotGRPSRespTx.setStatus("current")
_JnxMbgPgwV1ICsMSRefusesRx_Type = Counter64
_JnxMbgPgwV1ICsMSRefusesRx_Object = MibTableColumn
jnxMbgPgwV1ICsMSRefusesRx = _JnxMbgPgwV1ICsMSRefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 238),
    _JnxMbgPgwV1ICsMSRefusesRx_Type()
)
jnxMbgPgwV1ICsMSRefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMSRefusesRx.setStatus("current")
_JnxMbgPgwV1ICsMSRefusesTx_Type = Counter64
_JnxMbgPgwV1ICsMSRefusesTx_Object = MibTableColumn
jnxMbgPgwV1ICsMSRefusesTx = _JnxMbgPgwV1ICsMSRefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 239),
    _JnxMbgPgwV1ICsMSRefusesTx_Type()
)
jnxMbgPgwV1ICsMSRefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMSRefusesTx.setStatus("current")
_JnxMbgPgwV1ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwV1ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwV1ICsVerNotSuppRx = _JnxMbgPgwV1ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 240),
    _JnxMbgPgwV1ICsVerNotSuppRx_Type()
)
jnxMbgPgwV1ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwV1ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwV1ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwV1ICsVerNotSuppTx = _JnxMbgPgwV1ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 241),
    _JnxMbgPgwV1ICsVerNotSuppTx_Type()
)
jnxMbgPgwV1ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwV1ICsNoResRx_Type = Counter64
_JnxMbgPgwV1ICsNoResRx_Object = MibTableColumn
jnxMbgPgwV1ICsNoResRx = _JnxMbgPgwV1ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 242),
    _JnxMbgPgwV1ICsNoResRx_Type()
)
jnxMbgPgwV1ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNoResRx.setStatus("current")
_JnxMbgPgwV1ICsNoResTx_Type = Counter64
_JnxMbgPgwV1ICsNoResTx_Object = MibTableColumn
jnxMbgPgwV1ICsNoResTx = _JnxMbgPgwV1ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 243),
    _JnxMbgPgwV1ICsNoResTx_Type()
)
jnxMbgPgwV1ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNoResTx.setStatus("current")
_JnxMbgPgwV1ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwV1ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwV1ICsServNotSuppRx = _JnxMbgPgwV1ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 244),
    _JnxMbgPgwV1ICsServNotSuppRx_Type()
)
jnxMbgPgwV1ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwV1ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwV1ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwV1ICsServNotSuppTx = _JnxMbgPgwV1ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 245),
    _JnxMbgPgwV1ICsServNotSuppTx_Type()
)
jnxMbgPgwV1ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwV1ICsManIEIncrtRx_Type = Counter64
_JnxMbgPgwV1ICsManIEIncrtRx_Object = MibTableColumn
jnxMbgPgwV1ICsManIEIncrtRx = _JnxMbgPgwV1ICsManIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 246),
    _JnxMbgPgwV1ICsManIEIncrtRx_Type()
)
jnxMbgPgwV1ICsManIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsManIEIncrtRx.setStatus("current")
_JnxMbgPgwV1ICsManIEIncrtTx_Type = Counter64
_JnxMbgPgwV1ICsManIEIncrtTx_Object = MibTableColumn
jnxMbgPgwV1ICsManIEIncrtTx = _JnxMbgPgwV1ICsManIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 247),
    _JnxMbgPgwV1ICsManIEIncrtTx_Type()
)
jnxMbgPgwV1ICsManIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsManIEIncrtTx.setStatus("current")
_JnxMbgPgwV1ICsManIEMissRx_Type = Counter64
_JnxMbgPgwV1ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwV1ICsManIEMissRx = _JnxMbgPgwV1ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 248),
    _JnxMbgPgwV1ICsManIEMissRx_Type()
)
jnxMbgPgwV1ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsManIEMissRx.setStatus("current")
_JnxMbgPgwV1ICsManIEMissTx_Type = Counter64
_JnxMbgPgwV1ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwV1ICsManIEMissTx = _JnxMbgPgwV1ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 249),
    _JnxMbgPgwV1ICsManIEMissTx_Type()
)
jnxMbgPgwV1ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsManIEMissTx.setStatus("current")
_JnxMbgPgwV1ICsOptIEIncrtRx_Type = Counter64
_JnxMbgPgwV1ICsOptIEIncrtRx_Object = MibTableColumn
jnxMbgPgwV1ICsOptIEIncrtRx = _JnxMbgPgwV1ICsOptIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 250),
    _JnxMbgPgwV1ICsOptIEIncrtRx_Type()
)
jnxMbgPgwV1ICsOptIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsOptIEIncrtRx.setStatus("current")
_JnxMbgPgwV1ICsOptIEIncrtTx_Type = Counter64
_JnxMbgPgwV1ICsOptIEIncrtTx_Object = MibTableColumn
jnxMbgPgwV1ICsOptIEIncrtTx = _JnxMbgPgwV1ICsOptIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 251),
    _JnxMbgPgwV1ICsOptIEIncrtTx_Type()
)
jnxMbgPgwV1ICsOptIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsOptIEIncrtTx.setStatus("current")
_JnxMbgPgwV1ICsSysFailRx_Type = Counter64
_JnxMbgPgwV1ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwV1ICsSysFailRx = _JnxMbgPgwV1ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 252),
    _JnxMbgPgwV1ICsSysFailRx_Type()
)
jnxMbgPgwV1ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSysFailRx.setStatus("current")
_JnxMbgPgwV1ICsSysFailTx_Type = Counter64
_JnxMbgPgwV1ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwV1ICsSysFailTx = _JnxMbgPgwV1ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 253),
    _JnxMbgPgwV1ICsSysFailTx_Type()
)
jnxMbgPgwV1ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSysFailTx.setStatus("current")
_JnxMbgPgwV1ICsRoamRestrictRx_Type = Counter64
_JnxMbgPgwV1ICsRoamRestrictRx_Object = MibTableColumn
jnxMbgPgwV1ICsRoamRestrictRx = _JnxMbgPgwV1ICsRoamRestrictRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 254),
    _JnxMbgPgwV1ICsRoamRestrictRx_Type()
)
jnxMbgPgwV1ICsRoamRestrictRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsRoamRestrictRx.setStatus("current")
_JnxMbgPgwV1ICsRoamRestrictTx_Type = Counter64
_JnxMbgPgwV1ICsRoamRestrictTx_Object = MibTableColumn
jnxMbgPgwV1ICsRoamRestrictTx = _JnxMbgPgwV1ICsRoamRestrictTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 255),
    _JnxMbgPgwV1ICsRoamRestrictTx_Type()
)
jnxMbgPgwV1ICsRoamRestrictTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsRoamRestrictTx.setStatus("current")
_JnxMbgPgwV1ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwV1ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwV1ICsPTMSISigMMRx = _JnxMbgPgwV1ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 256),
    _JnxMbgPgwV1ICsPTMSISigMMRx_Type()
)
jnxMbgPgwV1ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwV1ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwV1ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwV1ICsPTMSISigMMTx = _JnxMbgPgwV1ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 257),
    _JnxMbgPgwV1ICsPTMSISigMMTx_Type()
)
jnxMbgPgwV1ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwV1ICsGPRSConnSuppRx_Type = Counter64
_JnxMbgPgwV1ICsGPRSConnSuppRx_Object = MibTableColumn
jnxMbgPgwV1ICsGPRSConnSuppRx = _JnxMbgPgwV1ICsGPRSConnSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 258),
    _JnxMbgPgwV1ICsGPRSConnSuppRx_Type()
)
jnxMbgPgwV1ICsGPRSConnSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsGPRSConnSuppRx.setStatus("current")
_JnxMbgPgwV1ICsGPRSConnSuppTx_Type = Counter64
_JnxMbgPgwV1ICsGPRSConnSuppTx_Object = MibTableColumn
jnxMbgPgwV1ICsGPRSConnSuppTx = _JnxMbgPgwV1ICsGPRSConnSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 259),
    _JnxMbgPgwV1ICsGPRSConnSuppTx_Type()
)
jnxMbgPgwV1ICsGPRSConnSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsGPRSConnSuppTx.setStatus("current")
_JnxMbgPgwV1ICsAuthFailRx_Type = Counter64
_JnxMbgPgwV1ICsAuthFailRx_Object = MibTableColumn
jnxMbgPgwV1ICsAuthFailRx = _JnxMbgPgwV1ICsAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 260),
    _JnxMbgPgwV1ICsAuthFailRx_Type()
)
jnxMbgPgwV1ICsAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsAuthFailRx.setStatus("current")
_JnxMbgPgwV1ICsAuthFailTx_Type = Counter64
_JnxMbgPgwV1ICsAuthFailTx_Object = MibTableColumn
jnxMbgPgwV1ICsAuthFailTx = _JnxMbgPgwV1ICsAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 261),
    _JnxMbgPgwV1ICsAuthFailTx_Type()
)
jnxMbgPgwV1ICsAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsAuthFailTx.setStatus("current")
_JnxMbgPgwV1ICsUserAuthFailRx_Type = Counter64
_JnxMbgPgwV1ICsUserAuthFailRx_Object = MibTableColumn
jnxMbgPgwV1ICsUserAuthFailRx = _JnxMbgPgwV1ICsUserAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 262),
    _JnxMbgPgwV1ICsUserAuthFailRx_Type()
)
jnxMbgPgwV1ICsUserAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsUserAuthFailRx.setStatus("current")
_JnxMbgPgwV1ICsUserAuthFailTx_Type = Counter64
_JnxMbgPgwV1ICsUserAuthFailTx_Object = MibTableColumn
jnxMbgPgwV1ICsUserAuthFailTx = _JnxMbgPgwV1ICsUserAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 263),
    _JnxMbgPgwV1ICsUserAuthFailTx_Type()
)
jnxMbgPgwV1ICsUserAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsUserAuthFailTx.setStatus("current")
_JnxMbgPgwV1ICsCtxNotFndRx_Type = Counter64
_JnxMbgPgwV1ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgPgwV1ICsCtxNotFndRx = _JnxMbgPgwV1ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 264),
    _JnxMbgPgwV1ICsCtxNotFndRx_Type()
)
jnxMbgPgwV1ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsCtxNotFndRx.setStatus("current")
_JnxMbgPgwV1ICsCtxNotFndTx_Type = Counter64
_JnxMbgPgwV1ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgPgwV1ICsCtxNotFndTx = _JnxMbgPgwV1ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 265),
    _JnxMbgPgwV1ICsCtxNotFndTx_Type()
)
jnxMbgPgwV1ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsCtxNotFndTx.setStatus("current")
_JnxMbgPgwV1ICsAllDynPDPAdRx_Type = Counter64
_JnxMbgPgwV1ICsAllDynPDPAdRx_Object = MibTableColumn
jnxMbgPgwV1ICsAllDynPDPAdRx = _JnxMbgPgwV1ICsAllDynPDPAdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 266),
    _JnxMbgPgwV1ICsAllDynPDPAdRx_Type()
)
jnxMbgPgwV1ICsAllDynPDPAdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsAllDynPDPAdRx.setStatus("current")
_JnxMbgPgwV1ICsAllDynPDPAdTx_Type = Counter64
_JnxMbgPgwV1ICsAllDynPDPAdTx_Object = MibTableColumn
jnxMbgPgwV1ICsAllDynPDPAdTx = _JnxMbgPgwV1ICsAllDynPDPAdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 267),
    _JnxMbgPgwV1ICsAllDynPDPAdTx_Type()
)
jnxMbgPgwV1ICsAllDynPDPAdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsAllDynPDPAdTx.setStatus("current")
_JnxMbgPgwV1ICsNoMemRx_Type = Counter64
_JnxMbgPgwV1ICsNoMemRx_Object = MibTableColumn
jnxMbgPgwV1ICsNoMemRx = _JnxMbgPgwV1ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 268),
    _JnxMbgPgwV1ICsNoMemRx_Type()
)
jnxMbgPgwV1ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNoMemRx.setStatus("current")
_JnxMbgPgwV1ICsNoMemTx_Type = Counter64
_JnxMbgPgwV1ICsNoMemTx_Object = MibTableColumn
jnxMbgPgwV1ICsNoMemTx = _JnxMbgPgwV1ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 269),
    _JnxMbgPgwV1ICsNoMemTx_Type()
)
jnxMbgPgwV1ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNoMemTx.setStatus("current")
_JnxMbgPgwV1ICsRelocFailRx_Type = Counter64
_JnxMbgPgwV1ICsRelocFailRx_Object = MibTableColumn
jnxMbgPgwV1ICsRelocFailRx = _JnxMbgPgwV1ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 270),
    _JnxMbgPgwV1ICsRelocFailRx_Type()
)
jnxMbgPgwV1ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsRelocFailRx.setStatus("current")
_JnxMbgPgwV1ICsRelocFailTx_Type = Counter64
_JnxMbgPgwV1ICsRelocFailTx_Object = MibTableColumn
jnxMbgPgwV1ICsRelocFailTx = _JnxMbgPgwV1ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 271),
    _JnxMbgPgwV1ICsRelocFailTx_Type()
)
jnxMbgPgwV1ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsRelocFailTx.setStatus("current")
_JnxMbgPgwV1ICsUnkManExhdrRx_Type = Counter64
_JnxMbgPgwV1ICsUnkManExhdrRx_Object = MibTableColumn
jnxMbgPgwV1ICsUnkManExhdrRx = _JnxMbgPgwV1ICsUnkManExhdrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 272),
    _JnxMbgPgwV1ICsUnkManExhdrRx_Type()
)
jnxMbgPgwV1ICsUnkManExhdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsUnkManExhdrRx.setStatus("current")
_JnxMbgPgwV1ICsUnkManExhdrTx_Type = Counter64
_JnxMbgPgwV1ICsUnkManExhdrTx_Object = MibTableColumn
jnxMbgPgwV1ICsUnkManExhdrTx = _JnxMbgPgwV1ICsUnkManExhdrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 273),
    _JnxMbgPgwV1ICsUnkManExhdrTx_Type()
)
jnxMbgPgwV1ICsUnkManExhdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsUnkManExhdrTx.setStatus("current")
_JnxMbgPgwV1ICsSMANTTFTEr1Rx_Type = Counter64
_JnxMbgPgwV1ICsSMANTTFTEr1Rx_Object = MibTableColumn
jnxMbgPgwV1ICsSMANTTFTEr1Rx = _JnxMbgPgwV1ICsSMANTTFTEr1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 274),
    _JnxMbgPgwV1ICsSMANTTFTEr1Rx_Type()
)
jnxMbgPgwV1ICsSMANTTFTEr1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSMANTTFTEr1Rx.setStatus("current")
_JnxMbgPgwV1ICsSMANTTFTEr1Tx_Type = Counter64
_JnxMbgPgwV1ICsSMANTTFTEr1Tx_Object = MibTableColumn
jnxMbgPgwV1ICsSMANTTFTEr1Tx = _JnxMbgPgwV1ICsSMANTTFTEr1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 275),
    _JnxMbgPgwV1ICsSMANTTFTEr1Tx_Type()
)
jnxMbgPgwV1ICsSMANTTFTEr1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSMANTTFTEr1Tx.setStatus("current")
_JnxMbgPgwV1ICsSYNTFTErr2Rx_Type = Counter64
_JnxMbgPgwV1ICsSYNTFTErr2Rx_Object = MibTableColumn
jnxMbgPgwV1ICsSYNTFTErr2Rx = _JnxMbgPgwV1ICsSYNTFTErr2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 276),
    _JnxMbgPgwV1ICsSYNTFTErr2Rx_Type()
)
jnxMbgPgwV1ICsSYNTFTErr2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSYNTFTErr2Rx.setStatus("current")
_JnxMbgPgwV1ICsSYNTFTErr2Tx_Type = Counter64
_JnxMbgPgwV1ICsSYNTFTErr2Tx_Object = MibTableColumn
jnxMbgPgwV1ICsSYNTFTErr2Tx = _JnxMbgPgwV1ICsSYNTFTErr2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 277),
    _JnxMbgPgwV1ICsSYNTFTErr2Tx_Type()
)
jnxMbgPgwV1ICsSYNTFTErr2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSYNTFTErr2Tx.setStatus("current")
_JnxMbgPgwV1ICsSMNTPkFlEr1Rx_Type = Counter64
_JnxMbgPgwV1ICsSMNTPkFlEr1Rx_Object = MibTableColumn
jnxMbgPgwV1ICsSMNTPkFlEr1Rx = _JnxMbgPgwV1ICsSMNTPkFlEr1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 278),
    _JnxMbgPgwV1ICsSMNTPkFlEr1Rx_Type()
)
jnxMbgPgwV1ICsSMNTPkFlEr1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSMNTPkFlEr1Rx.setStatus("current")
_JnxMbgPgwV1ICsSMNTPkFlEr1Tx_Type = Counter64
_JnxMbgPgwV1ICsSMNTPkFlEr1Tx_Object = MibTableColumn
jnxMbgPgwV1ICsSMNTPkFlEr1Tx = _JnxMbgPgwV1ICsSMNTPkFlEr1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 279),
    _JnxMbgPgwV1ICsSMNTPkFlEr1Tx_Type()
)
jnxMbgPgwV1ICsSMNTPkFlEr1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSMNTPkFlEr1Tx.setStatus("current")
_JnxMbgPgwV1ICsSYNPkFlErr2Rx_Type = Counter64
_JnxMbgPgwV1ICsSYNPkFlErr2Rx_Object = MibTableColumn
jnxMbgPgwV1ICsSYNPkFlErr2Rx = _JnxMbgPgwV1ICsSYNPkFlErr2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 280),
    _JnxMbgPgwV1ICsSYNPkFlErr2Rx_Type()
)
jnxMbgPgwV1ICsSYNPkFlErr2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSYNPkFlErr2Rx.setStatus("current")
_JnxMbgPgwV1ICsSYNPkFlErr2Tx_Type = Counter64
_JnxMbgPgwV1ICsSYNPkFlErr2Tx_Object = MibTableColumn
jnxMbgPgwV1ICsSYNPkFlErr2Tx = _JnxMbgPgwV1ICsSYNPkFlErr2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 281),
    _JnxMbgPgwV1ICsSYNPkFlErr2Tx_Type()
)
jnxMbgPgwV1ICsSYNPkFlErr2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsSYNPkFlErr2Tx.setStatus("current")
_JnxMbgPgwV1ICsMissUnknAPNRx_Type = Counter64
_JnxMbgPgwV1ICsMissUnknAPNRx_Object = MibTableColumn
jnxMbgPgwV1ICsMissUnknAPNRx = _JnxMbgPgwV1ICsMissUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 282),
    _JnxMbgPgwV1ICsMissUnknAPNRx_Type()
)
jnxMbgPgwV1ICsMissUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMissUnknAPNRx.setStatus("current")
_JnxMbgPgwV1ICsMissUnknAPNTx_Type = Counter64
_JnxMbgPgwV1ICsMissUnknAPNTx_Object = MibTableColumn
jnxMbgPgwV1ICsMissUnknAPNTx = _JnxMbgPgwV1ICsMissUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 283),
    _JnxMbgPgwV1ICsMissUnknAPNTx_Type()
)
jnxMbgPgwV1ICsMissUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsMissUnknAPNTx.setStatus("current")
_JnxMbgPgwV1ICsUnknPDPAdRx_Type = Counter64
_JnxMbgPgwV1ICsUnknPDPAdRx_Object = MibTableColumn
jnxMbgPgwV1ICsUnknPDPAdRx = _JnxMbgPgwV1ICsUnknPDPAdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 284),
    _JnxMbgPgwV1ICsUnknPDPAdRx_Type()
)
jnxMbgPgwV1ICsUnknPDPAdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsUnknPDPAdRx.setStatus("current")
_JnxMbgPgwV1ICsUnknPDPAdTx_Type = Counter64
_JnxMbgPgwV1ICsUnknPDPAdTx_Object = MibTableColumn
jnxMbgPgwV1ICsUnknPDPAdTx = _JnxMbgPgwV1ICsUnknPDPAdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 285),
    _JnxMbgPgwV1ICsUnknPDPAdTx_Type()
)
jnxMbgPgwV1ICsUnknPDPAdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsUnknPDPAdTx.setStatus("current")
_JnxMbgPgwV1ICsNoTFTCtxExRx_Type = Counter64
_JnxMbgPgwV1ICsNoTFTCtxExRx_Object = MibTableColumn
jnxMbgPgwV1ICsNoTFTCtxExRx = _JnxMbgPgwV1ICsNoTFTCtxExRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 286),
    _JnxMbgPgwV1ICsNoTFTCtxExRx_Type()
)
jnxMbgPgwV1ICsNoTFTCtxExRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNoTFTCtxExRx.setStatus("current")
_JnxMbgPgwV1ICsNoTFTCtxExTx_Type = Counter64
_JnxMbgPgwV1ICsNoTFTCtxExTx_Object = MibTableColumn
jnxMbgPgwV1ICsNoTFTCtxExTx = _JnxMbgPgwV1ICsNoTFTCtxExTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 287),
    _JnxMbgPgwV1ICsNoTFTCtxExTx_Type()
)
jnxMbgPgwV1ICsNoTFTCtxExTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1ICsNoTFTCtxExTx.setStatus("current")
_JnxMbgPgwV0ProtocolErrRx_Type = Counter64
_JnxMbgPgwV0ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwV0ProtocolErrRx = _JnxMbgPgwV0ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 288),
    _JnxMbgPgwV0ProtocolErrRx_Type()
)
jnxMbgPgwV0ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ProtocolErrRx.setStatus("current")
_JnxMbgPgwV0UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwV0UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwV0UnSupportedMsgRx = _JnxMbgPgwV0UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 289),
    _JnxMbgPgwV0UnSupportedMsgRx_Type()
)
jnxMbgPgwV0UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwV0T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwV0T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwV0T3RespTmrExpRx = _JnxMbgPgwV0T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 290),
    _JnxMbgPgwV0T3RespTmrExpRx_Type()
)
jnxMbgPgwV0T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwV0GlbNumMsgRx_Type = Counter64
_JnxMbgPgwV0GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwV0GlbNumMsgRx = _JnxMbgPgwV0GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 291),
    _JnxMbgPgwV0GlbNumMsgRx_Type()
)
jnxMbgPgwV0GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNumMsgRx.setStatus("current")
_JnxMbgPgwV0GlbNumMsgTx_Type = Counter64
_JnxMbgPgwV0GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwV0GlbNumMsgTx = _JnxMbgPgwV0GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 292),
    _JnxMbgPgwV0GlbNumMsgTx_Type()
)
jnxMbgPgwV0GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNumMsgTx.setStatus("current")
_JnxMbgPgwV0GlbNumBytesRx_Type = Counter64
_JnxMbgPgwV0GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwV0GlbNumBytesRx = _JnxMbgPgwV0GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 293),
    _JnxMbgPgwV0GlbNumBytesRx_Type()
)
jnxMbgPgwV0GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNumBytesRx.setStatus("current")
_JnxMbgPgwV0GlbNumBytesTx_Type = Counter64
_JnxMbgPgwV0GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwV0GlbNumBytesTx = _JnxMbgPgwV0GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 294),
    _JnxMbgPgwV0GlbNumBytesTx_Type()
)
jnxMbgPgwV0GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNumBytesTx.setStatus("current")
_JnxMbgPgwV0GlbEchoReqRx_Type = Counter64
_JnxMbgPgwV0GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbEchoReqRx = _JnxMbgPgwV0GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 295),
    _JnxMbgPgwV0GlbEchoReqRx_Type()
)
jnxMbgPgwV0GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbEchoReqRx.setStatus("current")
_JnxMbgPgwV0GlbEchoReqTx_Type = Counter64
_JnxMbgPgwV0GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbEchoReqTx = _JnxMbgPgwV0GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 296),
    _JnxMbgPgwV0GlbEchoReqTx_Type()
)
jnxMbgPgwV0GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbEchoReqTx.setStatus("current")
_JnxMbgPgwV0GlbEchoRespRx_Type = Counter64
_JnxMbgPgwV0GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwV0GlbEchoRespRx = _JnxMbgPgwV0GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 297),
    _JnxMbgPgwV0GlbEchoRespRx_Type()
)
jnxMbgPgwV0GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbEchoRespRx.setStatus("current")
_JnxMbgPgwV0GlbEchoRespTx_Type = Counter64
_JnxMbgPgwV0GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwV0GlbEchoRespTx = _JnxMbgPgwV0GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 298),
    _JnxMbgPgwV0GlbEchoRespTx_Type()
)
jnxMbgPgwV0GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbEchoRespTx.setStatus("current")
_JnxMbgPgwV0GlbVerNotSupRx_Type = Counter64
_JnxMbgPgwV0GlbVerNotSupRx_Object = MibTableColumn
jnxMbgPgwV0GlbVerNotSupRx = _JnxMbgPgwV0GlbVerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 299),
    _JnxMbgPgwV0GlbVerNotSupRx_Type()
)
jnxMbgPgwV0GlbVerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbVerNotSupRx.setStatus("current")
_JnxMbgPgwV0GlbVerNotSupTx_Type = Counter64
_JnxMbgPgwV0GlbVerNotSupTx_Object = MibTableColumn
jnxMbgPgwV0GlbVerNotSupTx = _JnxMbgPgwV0GlbVerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 300),
    _JnxMbgPgwV0GlbVerNotSupTx_Type()
)
jnxMbgPgwV0GlbVerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbVerNotSupTx.setStatus("current")
_JnxMbgPgwV0GlbCrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0GlbCrtPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtPdpCxtReqRx = _JnxMbgPgwV0GlbCrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 301),
    _JnxMbgPgwV0GlbCrtPdpCxtReqRx_Type()
)
jnxMbgPgwV0GlbCrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV0GlbCrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0GlbCrtPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtPdpCxtReqTx = _JnxMbgPgwV0GlbCrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 302),
    _JnxMbgPgwV0GlbCrtPdpCxtReqTx_Type()
)
jnxMbgPgwV0GlbCrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV0GlbCrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0GlbCrtPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtPdpCxtRspRx = _JnxMbgPgwV0GlbCrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 303),
    _JnxMbgPgwV0GlbCrtPdpCxtRspRx_Type()
)
jnxMbgPgwV0GlbCrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV0GlbCrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0GlbCrtPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtPdpCxtRspTx = _JnxMbgPgwV0GlbCrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 304),
    _JnxMbgPgwV0GlbCrtPdpCxtRspTx_Type()
)
jnxMbgPgwV0GlbCrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV0GlbUpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0GlbUpdPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbUpdPdpCxtReqRx = _JnxMbgPgwV0GlbUpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 305),
    _JnxMbgPgwV0GlbUpdPdpCxtReqRx_Type()
)
jnxMbgPgwV0GlbUpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbUpdPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV0GlbUpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0GlbUpdPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbUpdPdpCxtReqTx = _JnxMbgPgwV0GlbUpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 306),
    _JnxMbgPgwV0GlbUpdPdpCxtReqTx_Type()
)
jnxMbgPgwV0GlbUpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbUpdPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV0GlbUpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0GlbUpdPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbUpdPdpCxtRspRx = _JnxMbgPgwV0GlbUpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 307),
    _JnxMbgPgwV0GlbUpdPdpCxtRspRx_Type()
)
jnxMbgPgwV0GlbUpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbUpdPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV0GlbUpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0GlbUpdPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbUpdPdpCxtRspTx = _JnxMbgPgwV0GlbUpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 308),
    _JnxMbgPgwV0GlbUpdPdpCxtRspTx_Type()
)
jnxMbgPgwV0GlbUpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbUpdPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV0GlbDelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0GlbDelPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbDelPdpCxtReqRx = _JnxMbgPgwV0GlbDelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 309),
    _JnxMbgPgwV0GlbDelPdpCxtReqRx_Type()
)
jnxMbgPgwV0GlbDelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV0GlbDelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0GlbDelPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbDelPdpCxtReqTx = _JnxMbgPgwV0GlbDelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 310),
    _JnxMbgPgwV0GlbDelPdpCxtReqTx_Type()
)
jnxMbgPgwV0GlbDelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV0GlbDelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0GlbDelPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbDelPdpCxtRspRx = _JnxMbgPgwV0GlbDelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 311),
    _JnxMbgPgwV0GlbDelPdpCxtRspRx_Type()
)
jnxMbgPgwV0GlbDelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV0GlbDelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0GlbDelPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbDelPdpCxtRspTx = _JnxMbgPgwV0GlbDelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 312),
    _JnxMbgPgwV0GlbDelPdpCxtRspTx_Type()
)
jnxMbgPgwV0GlbDelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV0GlbCrtAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0GlbCrtAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtAAPdpCxtReqRx = _JnxMbgPgwV0GlbCrtAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 313),
    _JnxMbgPgwV0GlbCrtAAPdpCxtReqRx_Type()
)
jnxMbgPgwV0GlbCrtAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV0GlbCrtAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0GlbCrtAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtAAPdpCxtReqTx = _JnxMbgPgwV0GlbCrtAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 314),
    _JnxMbgPgwV0GlbCrtAAPdpCxtReqTx_Type()
)
jnxMbgPgwV0GlbCrtAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV0GlbCrtAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0GlbCrtAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtAAPdpCxtRspRx = _JnxMbgPgwV0GlbCrtAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 315),
    _JnxMbgPgwV0GlbCrtAAPdpCxtRspRx_Type()
)
jnxMbgPgwV0GlbCrtAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV0GlbCrtAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0GlbCrtAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbCrtAAPdpCxtRspTx = _JnxMbgPgwV0GlbCrtAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 316),
    _JnxMbgPgwV0GlbCrtAAPdpCxtRspTx_Type()
)
jnxMbgPgwV0GlbCrtAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbCrtAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV0GlbDelAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV0GlbDelAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbDelAAPdpCxtReqRx = _JnxMbgPgwV0GlbDelAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 317),
    _JnxMbgPgwV0GlbDelAAPdpCxtReqRx_Type()
)
jnxMbgPgwV0GlbDelAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV0GlbDelAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV0GlbDelAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbDelAAPdpCxtReqTx = _JnxMbgPgwV0GlbDelAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 318),
    _JnxMbgPgwV0GlbDelAAPdpCxtReqTx_Type()
)
jnxMbgPgwV0GlbDelAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV0GlbDelAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV0GlbDelAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbDelAAPdpCxtRspRx = _JnxMbgPgwV0GlbDelAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 319),
    _JnxMbgPgwV0GlbDelAAPdpCxtRspRx_Type()
)
jnxMbgPgwV0GlbDelAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV0GlbDelAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV0GlbDelAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbDelAAPdpCxtRspTx = _JnxMbgPgwV0GlbDelAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 320),
    _JnxMbgPgwV0GlbDelAAPdpCxtRspTx_Type()
)
jnxMbgPgwV0GlbDelAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbDelAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV0GlbErrorIndRx_Type = Counter64
_JnxMbgPgwV0GlbErrorIndRx_Object = MibTableColumn
jnxMbgPgwV0GlbErrorIndRx = _JnxMbgPgwV0GlbErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 321),
    _JnxMbgPgwV0GlbErrorIndRx_Type()
)
jnxMbgPgwV0GlbErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbErrorIndRx.setStatus("current")
_JnxMbgPgwV0GlbErrorIndTx_Type = Counter64
_JnxMbgPgwV0GlbErrorIndTx_Object = MibTableColumn
jnxMbgPgwV0GlbErrorIndTx = _JnxMbgPgwV0GlbErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 322),
    _JnxMbgPgwV0GlbErrorIndTx_Type()
)
jnxMbgPgwV0GlbErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbErrorIndTx.setStatus("current")
_JnxMbgPgwV0GlbNotifReqRx_Type = Counter64
_JnxMbgPgwV0GlbNotifReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifReqRx = _JnxMbgPgwV0GlbNotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 323),
    _JnxMbgPgwV0GlbNotifReqRx_Type()
)
jnxMbgPgwV0GlbNotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifReqRx.setStatus("current")
_JnxMbgPgwV0GlbNotifReqTx_Type = Counter64
_JnxMbgPgwV0GlbNotifReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifReqTx = _JnxMbgPgwV0GlbNotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 324),
    _JnxMbgPgwV0GlbNotifReqTx_Type()
)
jnxMbgPgwV0GlbNotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifReqTx.setStatus("current")
_JnxMbgPgwV0GlbNotifRspRx_Type = Counter64
_JnxMbgPgwV0GlbNotifRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifRspRx = _JnxMbgPgwV0GlbNotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 325),
    _JnxMbgPgwV0GlbNotifRspRx_Type()
)
jnxMbgPgwV0GlbNotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifRspRx.setStatus("current")
_JnxMbgPgwV0GlbNotifRspTx_Type = Counter64
_JnxMbgPgwV0GlbNotifRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifRspTx = _JnxMbgPgwV0GlbNotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 326),
    _JnxMbgPgwV0GlbNotifRspTx_Type()
)
jnxMbgPgwV0GlbNotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifRspTx.setStatus("current")
_JnxMbgPgwV0GlbNotifRejReqRx_Type = Counter64
_JnxMbgPgwV0GlbNotifRejReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifRejReqRx = _JnxMbgPgwV0GlbNotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 327),
    _JnxMbgPgwV0GlbNotifRejReqRx_Type()
)
jnxMbgPgwV0GlbNotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifRejReqRx.setStatus("current")
_JnxMbgPgwV0GlbNotifRejReqTx_Type = Counter64
_JnxMbgPgwV0GlbNotifRejReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifRejReqTx = _JnxMbgPgwV0GlbNotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 328),
    _JnxMbgPgwV0GlbNotifRejReqTx_Type()
)
jnxMbgPgwV0GlbNotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifRejReqTx.setStatus("current")
_JnxMbgPgwV0GlbNotifRejRspRx_Type = Counter64
_JnxMbgPgwV0GlbNotifRejRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifRejRspRx = _JnxMbgPgwV0GlbNotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 329),
    _JnxMbgPgwV0GlbNotifRejRspRx_Type()
)
jnxMbgPgwV0GlbNotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifRejRspRx.setStatus("current")
_JnxMbgPgwV0GlbNotifRejRspTx_Type = Counter64
_JnxMbgPgwV0GlbNotifRejRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbNotifRejRspTx = _JnxMbgPgwV0GlbNotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 330),
    _JnxMbgPgwV0GlbNotifRejRspTx_Type()
)
jnxMbgPgwV0GlbNotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotifRejRspTx.setStatus("current")
_JnxMbgPgwV0GlbRtInfReqRx_Type = Counter64
_JnxMbgPgwV0GlbRtInfReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbRtInfReqRx = _JnxMbgPgwV0GlbRtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 331),
    _JnxMbgPgwV0GlbRtInfReqRx_Type()
)
jnxMbgPgwV0GlbRtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbRtInfReqRx.setStatus("current")
_JnxMbgPgwV0GlbRtInfReqTx_Type = Counter64
_JnxMbgPgwV0GlbRtInfReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbRtInfReqTx = _JnxMbgPgwV0GlbRtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 332),
    _JnxMbgPgwV0GlbRtInfReqTx_Type()
)
jnxMbgPgwV0GlbRtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbRtInfReqTx.setStatus("current")
_JnxMbgPgwV0GlbRtInfRspRx_Type = Counter64
_JnxMbgPgwV0GlbRtInfRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbRtInfRspRx = _JnxMbgPgwV0GlbRtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 333),
    _JnxMbgPgwV0GlbRtInfRspRx_Type()
)
jnxMbgPgwV0GlbRtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbRtInfRspRx.setStatus("current")
_JnxMbgPgwV0GlbRtInfRspTx_Type = Counter64
_JnxMbgPgwV0GlbRtInfRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbRtInfRspTx = _JnxMbgPgwV0GlbRtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 334),
    _JnxMbgPgwV0GlbRtInfRspTx_Type()
)
jnxMbgPgwV0GlbRtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbRtInfRspTx.setStatus("current")
_JnxMbgPgwV0GlbFailRptReqRx_Type = Counter64
_JnxMbgPgwV0GlbFailRptReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbFailRptReqRx = _JnxMbgPgwV0GlbFailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 335),
    _JnxMbgPgwV0GlbFailRptReqRx_Type()
)
jnxMbgPgwV0GlbFailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbFailRptReqRx.setStatus("current")
_JnxMbgPgwV0GlbFailRptReqTx_Type = Counter64
_JnxMbgPgwV0GlbFailRptReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbFailRptReqTx = _JnxMbgPgwV0GlbFailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 336),
    _JnxMbgPgwV0GlbFailRptReqTx_Type()
)
jnxMbgPgwV0GlbFailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbFailRptReqTx.setStatus("current")
_JnxMbgPgwV0GlbFailRptRspRx_Type = Counter64
_JnxMbgPgwV0GlbFailRptRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbFailRptRspRx = _JnxMbgPgwV0GlbFailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 337),
    _JnxMbgPgwV0GlbFailRptRspRx_Type()
)
jnxMbgPgwV0GlbFailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbFailRptRspRx.setStatus("current")
_JnxMbgPgwV0GlbFailRptRspTx_Type = Counter64
_JnxMbgPgwV0GlbFailRptRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbFailRptRspTx = _JnxMbgPgwV0GlbFailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 338),
    _JnxMbgPgwV0GlbFailRptRspTx_Type()
)
jnxMbgPgwV0GlbFailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbFailRptRspTx.setStatus("current")
_JnxMbgPgwV0GlbNotMSPresReqRx_Type = Counter64
_JnxMbgPgwV0GlbNotMSPresReqRx_Object = MibTableColumn
jnxMbgPgwV0GlbNotMSPresReqRx = _JnxMbgPgwV0GlbNotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 339),
    _JnxMbgPgwV0GlbNotMSPresReqRx_Type()
)
jnxMbgPgwV0GlbNotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotMSPresReqRx.setStatus("current")
_JnxMbgPgwV0GlbNotMSPresReqTx_Type = Counter64
_JnxMbgPgwV0GlbNotMSPresReqTx_Object = MibTableColumn
jnxMbgPgwV0GlbNotMSPresReqTx = _JnxMbgPgwV0GlbNotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 340),
    _JnxMbgPgwV0GlbNotMSPresReqTx_Type()
)
jnxMbgPgwV0GlbNotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotMSPresReqTx.setStatus("current")
_JnxMbgPgwV0GlbNotMSPresRspRx_Type = Counter64
_JnxMbgPgwV0GlbNotMSPresRspRx_Object = MibTableColumn
jnxMbgPgwV0GlbNotMSPresRspRx = _JnxMbgPgwV0GlbNotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 341),
    _JnxMbgPgwV0GlbNotMSPresRspRx_Type()
)
jnxMbgPgwV0GlbNotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotMSPresRspRx.setStatus("current")
_JnxMbgPgwV0GlbNotMSPresRspTx_Type = Counter64
_JnxMbgPgwV0GlbNotMSPresRspTx_Object = MibTableColumn
jnxMbgPgwV0GlbNotMSPresRspTx = _JnxMbgPgwV0GlbNotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 342),
    _JnxMbgPgwV0GlbNotMSPresRspTx_Type()
)
jnxMbgPgwV0GlbNotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0GlbNotMSPresRspTx.setStatus("current")
_JnxMbgPgwV0ICsReqAcceptedRx_Type = Counter64
_JnxMbgPgwV0ICsReqAcceptedRx_Object = MibTableColumn
jnxMbgPgwV0ICsReqAcceptedRx = _JnxMbgPgwV0ICsReqAcceptedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 343),
    _JnxMbgPgwV0ICsReqAcceptedRx_Type()
)
jnxMbgPgwV0ICsReqAcceptedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsReqAcceptedRx.setStatus("current")
_JnxMbgPgwV0ICsReqAcceptedTx_Type = Counter64
_JnxMbgPgwV0ICsReqAcceptedTx_Object = MibTableColumn
jnxMbgPgwV0ICsReqAcceptedTx = _JnxMbgPgwV0ICsReqAcceptedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 344),
    _JnxMbgPgwV0ICsReqAcceptedTx_Type()
)
jnxMbgPgwV0ICsReqAcceptedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsReqAcceptedTx.setStatus("current")
_JnxMbgPgwV0ICsNonExistRx_Type = Counter64
_JnxMbgPgwV0ICsNonExistRx_Object = MibTableColumn
jnxMbgPgwV0ICsNonExistRx = _JnxMbgPgwV0ICsNonExistRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 345),
    _JnxMbgPgwV0ICsNonExistRx_Type()
)
jnxMbgPgwV0ICsNonExistRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsNonExistRx.setStatus("current")
_JnxMbgPgwV0ICsNonExistTx_Type = Counter64
_JnxMbgPgwV0ICsNonExistTx_Object = MibTableColumn
jnxMbgPgwV0ICsNonExistTx = _JnxMbgPgwV0ICsNonExistTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 346),
    _JnxMbgPgwV0ICsNonExistTx_Type()
)
jnxMbgPgwV0ICsNonExistTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsNonExistTx.setStatus("current")
_JnxMbgPgwV0ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwV0ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwV0ICsInvMsgFmtRx = _JnxMbgPgwV0ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 347),
    _JnxMbgPgwV0ICsInvMsgFmtRx_Type()
)
jnxMbgPgwV0ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwV0ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwV0ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwV0ICsInvMsgFmtTx = _JnxMbgPgwV0ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 348),
    _JnxMbgPgwV0ICsInvMsgFmtTx_Type()
)
jnxMbgPgwV0ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwV0ICsIMSINotKnownRx_Type = Counter64
_JnxMbgPgwV0ICsIMSINotKnownRx_Object = MibTableColumn
jnxMbgPgwV0ICsIMSINotKnownRx = _JnxMbgPgwV0ICsIMSINotKnownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 349),
    _JnxMbgPgwV0ICsIMSINotKnownRx_Type()
)
jnxMbgPgwV0ICsIMSINotKnownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsIMSINotKnownRx.setStatus("current")
_JnxMbgPgwV0ICsIMSINotKnownTx_Type = Counter64
_JnxMbgPgwV0ICsIMSINotKnownTx_Object = MibTableColumn
jnxMbgPgwV0ICsIMSINotKnownTx = _JnxMbgPgwV0ICsIMSINotKnownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 350),
    _JnxMbgPgwV0ICsIMSINotKnownTx_Type()
)
jnxMbgPgwV0ICsIMSINotKnownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsIMSINotKnownTx.setStatus("current")
_JnxMbgPgwV0ICsMSGRPSDetachRx_Type = Counter64
_JnxMbgPgwV0ICsMSGRPSDetachRx_Object = MibTableColumn
jnxMbgPgwV0ICsMSGRPSDetachRx = _JnxMbgPgwV0ICsMSGRPSDetachRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 351),
    _JnxMbgPgwV0ICsMSGRPSDetachRx_Type()
)
jnxMbgPgwV0ICsMSGRPSDetachRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsMSGRPSDetachRx.setStatus("current")
_JnxMbgPgwV0ICsMSGRPSDetachTx_Type = Counter64
_JnxMbgPgwV0ICsMSGRPSDetachTx_Object = MibTableColumn
jnxMbgPgwV0ICsMSGRPSDetachTx = _JnxMbgPgwV0ICsMSGRPSDetachTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 352),
    _JnxMbgPgwV0ICsMSGRPSDetachTx_Type()
)
jnxMbgPgwV0ICsMSGRPSDetachTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsMSGRPSDetachTx.setStatus("current")
_JnxMbgPgwV0ICsMSNotGRPSRespRx_Type = Counter64
_JnxMbgPgwV0ICsMSNotGRPSRespRx_Object = MibTableColumn
jnxMbgPgwV0ICsMSNotGRPSRespRx = _JnxMbgPgwV0ICsMSNotGRPSRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 353),
    _JnxMbgPgwV0ICsMSNotGRPSRespRx_Type()
)
jnxMbgPgwV0ICsMSNotGRPSRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsMSNotGRPSRespRx.setStatus("current")
_JnxMbgPgwV0ICsMSNotGRPSRespTx_Type = Counter64
_JnxMbgPgwV0ICsMSNotGRPSRespTx_Object = MibTableColumn
jnxMbgPgwV0ICsMSNotGRPSRespTx = _JnxMbgPgwV0ICsMSNotGRPSRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 354),
    _JnxMbgPgwV0ICsMSNotGRPSRespTx_Type()
)
jnxMbgPgwV0ICsMSNotGRPSRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsMSNotGRPSRespTx.setStatus("current")
_JnxMbgPgwV0ICsMSRefusesRx_Type = Counter64
_JnxMbgPgwV0ICsMSRefusesRx_Object = MibTableColumn
jnxMbgPgwV0ICsMSRefusesRx = _JnxMbgPgwV0ICsMSRefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 355),
    _JnxMbgPgwV0ICsMSRefusesRx_Type()
)
jnxMbgPgwV0ICsMSRefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsMSRefusesRx.setStatus("current")
_JnxMbgPgwV0ICsMSRefusesTx_Type = Counter64
_JnxMbgPgwV0ICsMSRefusesTx_Object = MibTableColumn
jnxMbgPgwV0ICsMSRefusesTx = _JnxMbgPgwV0ICsMSRefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 356),
    _JnxMbgPgwV0ICsMSRefusesTx_Type()
)
jnxMbgPgwV0ICsMSRefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsMSRefusesTx.setStatus("current")
_JnxMbgPgwV0ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwV0ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwV0ICsVerNotSuppRx = _JnxMbgPgwV0ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 357),
    _JnxMbgPgwV0ICsVerNotSuppRx_Type()
)
jnxMbgPgwV0ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwV0ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwV0ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwV0ICsVerNotSuppTx = _JnxMbgPgwV0ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 358),
    _JnxMbgPgwV0ICsVerNotSuppTx_Type()
)
jnxMbgPgwV0ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwV0ICsNoResRx_Type = Counter64
_JnxMbgPgwV0ICsNoResRx_Object = MibTableColumn
jnxMbgPgwV0ICsNoResRx = _JnxMbgPgwV0ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 359),
    _JnxMbgPgwV0ICsNoResRx_Type()
)
jnxMbgPgwV0ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsNoResRx.setStatus("current")
_JnxMbgPgwV0ICsNoResTx_Type = Counter64
_JnxMbgPgwV0ICsNoResTx_Object = MibTableColumn
jnxMbgPgwV0ICsNoResTx = _JnxMbgPgwV0ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 360),
    _JnxMbgPgwV0ICsNoResTx_Type()
)
jnxMbgPgwV0ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsNoResTx.setStatus("current")
_JnxMbgPgwV0ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwV0ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwV0ICsServNotSuppRx = _JnxMbgPgwV0ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 361),
    _JnxMbgPgwV0ICsServNotSuppRx_Type()
)
jnxMbgPgwV0ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwV0ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwV0ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwV0ICsServNotSuppTx = _JnxMbgPgwV0ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 362),
    _JnxMbgPgwV0ICsServNotSuppTx_Type()
)
jnxMbgPgwV0ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwV0ICsManIEIncrtRx_Type = Counter64
_JnxMbgPgwV0ICsManIEIncrtRx_Object = MibTableColumn
jnxMbgPgwV0ICsManIEIncrtRx = _JnxMbgPgwV0ICsManIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 363),
    _JnxMbgPgwV0ICsManIEIncrtRx_Type()
)
jnxMbgPgwV0ICsManIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsManIEIncrtRx.setStatus("current")
_JnxMbgPgwV0ICsManIEIncrtTx_Type = Counter64
_JnxMbgPgwV0ICsManIEIncrtTx_Object = MibTableColumn
jnxMbgPgwV0ICsManIEIncrtTx = _JnxMbgPgwV0ICsManIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 364),
    _JnxMbgPgwV0ICsManIEIncrtTx_Type()
)
jnxMbgPgwV0ICsManIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsManIEIncrtTx.setStatus("current")
_JnxMbgPgwV0ICsManIEMissRx_Type = Counter64
_JnxMbgPgwV0ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwV0ICsManIEMissRx = _JnxMbgPgwV0ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 365),
    _JnxMbgPgwV0ICsManIEMissRx_Type()
)
jnxMbgPgwV0ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsManIEMissRx.setStatus("current")
_JnxMbgPgwV0ICsManIEMissTx_Type = Counter64
_JnxMbgPgwV0ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwV0ICsManIEMissTx = _JnxMbgPgwV0ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 366),
    _JnxMbgPgwV0ICsManIEMissTx_Type()
)
jnxMbgPgwV0ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsManIEMissTx.setStatus("current")
_JnxMbgPgwV0ICsOptIEIncrtRx_Type = Counter64
_JnxMbgPgwV0ICsOptIEIncrtRx_Object = MibTableColumn
jnxMbgPgwV0ICsOptIEIncrtRx = _JnxMbgPgwV0ICsOptIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 367),
    _JnxMbgPgwV0ICsOptIEIncrtRx_Type()
)
jnxMbgPgwV0ICsOptIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsOptIEIncrtRx.setStatus("current")
_JnxMbgPgwV0ICsOptIEIncrtTx_Type = Counter64
_JnxMbgPgwV0ICsOptIEIncrtTx_Object = MibTableColumn
jnxMbgPgwV0ICsOptIEIncrtTx = _JnxMbgPgwV0ICsOptIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 368),
    _JnxMbgPgwV0ICsOptIEIncrtTx_Type()
)
jnxMbgPgwV0ICsOptIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsOptIEIncrtTx.setStatus("current")
_JnxMbgPgwV0ICsSysFailRx_Type = Counter64
_JnxMbgPgwV0ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwV0ICsSysFailRx = _JnxMbgPgwV0ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 369),
    _JnxMbgPgwV0ICsSysFailRx_Type()
)
jnxMbgPgwV0ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsSysFailRx.setStatus("current")
_JnxMbgPgwV0ICsSysFailTx_Type = Counter64
_JnxMbgPgwV0ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwV0ICsSysFailTx = _JnxMbgPgwV0ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 370),
    _JnxMbgPgwV0ICsSysFailTx_Type()
)
jnxMbgPgwV0ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsSysFailTx.setStatus("current")
_JnxMbgPgwV0ICsRoamRestrictRx_Type = Counter64
_JnxMbgPgwV0ICsRoamRestrictRx_Object = MibTableColumn
jnxMbgPgwV0ICsRoamRestrictRx = _JnxMbgPgwV0ICsRoamRestrictRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 371),
    _JnxMbgPgwV0ICsRoamRestrictRx_Type()
)
jnxMbgPgwV0ICsRoamRestrictRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsRoamRestrictRx.setStatus("current")
_JnxMbgPgwV0ICsRoamRestrictTx_Type = Counter64
_JnxMbgPgwV0ICsRoamRestrictTx_Object = MibTableColumn
jnxMbgPgwV0ICsRoamRestrictTx = _JnxMbgPgwV0ICsRoamRestrictTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 372),
    _JnxMbgPgwV0ICsRoamRestrictTx_Type()
)
jnxMbgPgwV0ICsRoamRestrictTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsRoamRestrictTx.setStatus("current")
_JnxMbgPgwV0ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwV0ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwV0ICsPTMSISigMMRx = _JnxMbgPgwV0ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 373),
    _JnxMbgPgwV0ICsPTMSISigMMRx_Type()
)
jnxMbgPgwV0ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwV0ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwV0ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwV0ICsPTMSISigMMTx = _JnxMbgPgwV0ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 374),
    _JnxMbgPgwV0ICsPTMSISigMMTx_Type()
)
jnxMbgPgwV0ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwV0ICsGPRSConnSuppRx_Type = Counter64
_JnxMbgPgwV0ICsGPRSConnSuppRx_Object = MibTableColumn
jnxMbgPgwV0ICsGPRSConnSuppRx = _JnxMbgPgwV0ICsGPRSConnSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 375),
    _JnxMbgPgwV0ICsGPRSConnSuppRx_Type()
)
jnxMbgPgwV0ICsGPRSConnSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsGPRSConnSuppRx.setStatus("current")
_JnxMbgPgwV0ICsGPRSConnSuppTx_Type = Counter64
_JnxMbgPgwV0ICsGPRSConnSuppTx_Object = MibTableColumn
jnxMbgPgwV0ICsGPRSConnSuppTx = _JnxMbgPgwV0ICsGPRSConnSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 376),
    _JnxMbgPgwV0ICsGPRSConnSuppTx_Type()
)
jnxMbgPgwV0ICsGPRSConnSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsGPRSConnSuppTx.setStatus("current")
_JnxMbgPgwV0ICsAuthFailRx_Type = Counter64
_JnxMbgPgwV0ICsAuthFailRx_Object = MibTableColumn
jnxMbgPgwV0ICsAuthFailRx = _JnxMbgPgwV0ICsAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 377),
    _JnxMbgPgwV0ICsAuthFailRx_Type()
)
jnxMbgPgwV0ICsAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsAuthFailRx.setStatus("current")
_JnxMbgPgwV0ICsAuthFailTx_Type = Counter64
_JnxMbgPgwV0ICsAuthFailTx_Object = MibTableColumn
jnxMbgPgwV0ICsAuthFailTx = _JnxMbgPgwV0ICsAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 378),
    _JnxMbgPgwV0ICsAuthFailTx_Type()
)
jnxMbgPgwV0ICsAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsAuthFailTx.setStatus("current")
_JnxMbgPgwV0ICsUserAuthFailRx_Type = Counter64
_JnxMbgPgwV0ICsUserAuthFailRx_Object = MibTableColumn
jnxMbgPgwV0ICsUserAuthFailRx = _JnxMbgPgwV0ICsUserAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 379),
    _JnxMbgPgwV0ICsUserAuthFailRx_Type()
)
jnxMbgPgwV0ICsUserAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsUserAuthFailRx.setStatus("current")
_JnxMbgPgwV0ICsUserAuthFailTx_Type = Counter64
_JnxMbgPgwV0ICsUserAuthFailTx_Object = MibTableColumn
jnxMbgPgwV0ICsUserAuthFailTx = _JnxMbgPgwV0ICsUserAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 380),
    _JnxMbgPgwV0ICsUserAuthFailTx_Type()
)
jnxMbgPgwV0ICsUserAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV0ICsUserAuthFailTx.setStatus("current")
_JnxMbgPgwGtpV2ICsLclDetRx_Type = Counter64
_JnxMbgPgwGtpV2ICsLclDetRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsLclDetRx = _JnxMbgPgwGtpV2ICsLclDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 381),
    _JnxMbgPgwGtpV2ICsLclDetRx_Type()
)
jnxMbgPgwGtpV2ICsLclDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsLclDetRx.setStatus("current")
_JnxMbgPgwGtpV2ICsLclDetTx_Type = Counter64
_JnxMbgPgwGtpV2ICsLclDetTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsLclDetTx = _JnxMbgPgwGtpV2ICsLclDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 382),
    _JnxMbgPgwGtpV2ICsLclDetTx_Type()
)
jnxMbgPgwGtpV2ICsLclDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsLclDetTx.setStatus("current")
_JnxMbgPgwGtpV2ICsCmpDetRx_Type = Counter64
_JnxMbgPgwGtpV2ICsCmpDetRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsCmpDetRx = _JnxMbgPgwGtpV2ICsCmpDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 383),
    _JnxMbgPgwGtpV2ICsCmpDetRx_Type()
)
jnxMbgPgwGtpV2ICsCmpDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsCmpDetRx.setStatus("current")
_JnxMbgPgwGtpV2ICsCmpDetTx_Type = Counter64
_JnxMbgPgwGtpV2ICsCmpDetTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsCmpDetTx = _JnxMbgPgwGtpV2ICsCmpDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 384),
    _JnxMbgPgwGtpV2ICsCmpDetTx_Type()
)
jnxMbgPgwGtpV2ICsCmpDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsCmpDetTx.setStatus("current")
_JnxMbgPgwGtpV2ICsRATChgRx_Type = Counter64
_JnxMbgPgwGtpV2ICsRATChgRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsRATChgRx = _JnxMbgPgwGtpV2ICsRATChgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 385),
    _JnxMbgPgwGtpV2ICsRATChgRx_Type()
)
jnxMbgPgwGtpV2ICsRATChgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsRATChgRx.setStatus("current")
_JnxMbgPgwGtpV2ICsRATChgTx_Type = Counter64
_JnxMbgPgwGtpV2ICsRATChgTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsRATChgTx = _JnxMbgPgwGtpV2ICsRATChgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 386),
    _JnxMbgPgwGtpV2ICsRATChgTx_Type()
)
jnxMbgPgwGtpV2ICsRATChgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsRATChgTx.setStatus("current")
_JnxMbgPgwGtpV2ICsISRDeactRx_Type = Counter64
_JnxMbgPgwGtpV2ICsISRDeactRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsISRDeactRx = _JnxMbgPgwGtpV2ICsISRDeactRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 387),
    _JnxMbgPgwGtpV2ICsISRDeactRx_Type()
)
jnxMbgPgwGtpV2ICsISRDeactRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsISRDeactRx.setStatus("current")
_JnxMbgPgwGtpV2ICsISRDeactTx_Type = Counter64
_JnxMbgPgwGtpV2ICsISRDeactTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsISRDeactTx = _JnxMbgPgwGtpV2ICsISRDeactTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 388),
    _JnxMbgPgwGtpV2ICsISRDeactTx_Type()
)
jnxMbgPgwGtpV2ICsISRDeactTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsISRDeactTx.setStatus("current")
_JnxMbgPgwGtpV2ICsEIFRNCEnRx_Type = Counter64
_JnxMbgPgwGtpV2ICsEIFRNCEnRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsEIFRNCEnRx = _JnxMbgPgwGtpV2ICsEIFRNCEnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 389),
    _JnxMbgPgwGtpV2ICsEIFRNCEnRx_Type()
)
jnxMbgPgwGtpV2ICsEIFRNCEnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsEIFRNCEnRx.setStatus("current")
_JnxMbgPgwGtpV2ICsEIFRNCEnTx_Type = Counter64
_JnxMbgPgwGtpV2ICsEIFRNCEnTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsEIFRNCEnTx = _JnxMbgPgwGtpV2ICsEIFRNCEnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 390),
    _JnxMbgPgwGtpV2ICsEIFRNCEnTx_Type()
)
jnxMbgPgwGtpV2ICsEIFRNCEnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsEIFRNCEnTx.setStatus("current")
_JnxMbgPgwGtpV2ICsSemErTADRx_Type = Counter64
_JnxMbgPgwGtpV2ICsSemErTADRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsSemErTADRx = _JnxMbgPgwGtpV2ICsSemErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 391),
    _JnxMbgPgwGtpV2ICsSemErTADRx_Type()
)
jnxMbgPgwGtpV2ICsSemErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsSemErTADRx.setStatus("current")
_JnxMbgPgwGtpV2ICsSemErTADTx_Type = Counter64
_JnxMbgPgwGtpV2ICsSemErTADTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsSemErTADTx = _JnxMbgPgwGtpV2ICsSemErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 392),
    _JnxMbgPgwGtpV2ICsSemErTADTx_Type()
)
jnxMbgPgwGtpV2ICsSemErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsSemErTADTx.setStatus("current")
_JnxMbgPgwGtpV2ICsSynErTADRx_Type = Counter64
_JnxMbgPgwGtpV2ICsSynErTADRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsSynErTADRx = _JnxMbgPgwGtpV2ICsSynErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 393),
    _JnxMbgPgwGtpV2ICsSynErTADRx_Type()
)
jnxMbgPgwGtpV2ICsSynErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsSynErTADRx.setStatus("current")
_JnxMbgPgwGtpV2ICsSynErTADTx_Type = Counter64
_JnxMbgPgwGtpV2ICsSynErTADTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsSynErTADTx = _JnxMbgPgwGtpV2ICsSynErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 394),
    _JnxMbgPgwGtpV2ICsSynErTADTx_Type()
)
jnxMbgPgwGtpV2ICsSynErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsSynErTADTx.setStatus("current")
_JnxMbgPgwGtpV2ICsRMValRcvRx_Type = Counter64
_JnxMbgPgwGtpV2ICsRMValRcvRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsRMValRcvRx = _JnxMbgPgwGtpV2ICsRMValRcvRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 395),
    _JnxMbgPgwGtpV2ICsRMValRcvRx_Type()
)
jnxMbgPgwGtpV2ICsRMValRcvRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsRMValRcvRx.setStatus("current")
_JnxMbgPgwGtpV2ICsRMValRcvTx_Type = Counter64
_JnxMbgPgwGtpV2ICsRMValRcvTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsRMValRcvTx = _JnxMbgPgwGtpV2ICsRMValRcvTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 396),
    _JnxMbgPgwGtpV2ICsRMValRcvTx_Type()
)
jnxMbgPgwGtpV2ICsRMValRcvTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsRMValRcvTx.setStatus("current")
_JnxMbgPgwGtpV2ICsRPrNtRspRx_Type = Counter64
_JnxMbgPgwGtpV2ICsRPrNtRspRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsRPrNtRspRx = _JnxMbgPgwGtpV2ICsRPrNtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 397),
    _JnxMbgPgwGtpV2ICsRPrNtRspRx_Type()
)
jnxMbgPgwGtpV2ICsRPrNtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsRPrNtRspRx.setStatus("current")
_JnxMbgPgwGtpV2ICsRPrNtRspTx_Type = Counter64
_JnxMbgPgwGtpV2ICsRPrNtRspTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsRPrNtRspTx = _JnxMbgPgwGtpV2ICsRPrNtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 398),
    _JnxMbgPgwGtpV2ICsRPrNtRspTx_Type()
)
jnxMbgPgwGtpV2ICsRPrNtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsRPrNtRspTx.setStatus("current")
_JnxMbgPgwGtpV2ICsColNWReqRx_Type = Counter64
_JnxMbgPgwGtpV2ICsColNWReqRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsColNWReqRx = _JnxMbgPgwGtpV2ICsColNWReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 399),
    _JnxMbgPgwGtpV2ICsColNWReqRx_Type()
)
jnxMbgPgwGtpV2ICsColNWReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsColNWReqRx.setStatus("current")
_JnxMbgPgwGtpV2ICsColNWReqTx_Type = Counter64
_JnxMbgPgwGtpV2ICsColNWReqTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsColNWReqTx = _JnxMbgPgwGtpV2ICsColNWReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 400),
    _JnxMbgPgwGtpV2ICsColNWReqTx_Type()
)
jnxMbgPgwGtpV2ICsColNWReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsColNWReqTx.setStatus("current")
_JnxMbgPgwGtpV2ICsUnPgUESusRx_Type = Counter64
_JnxMbgPgwGtpV2ICsUnPgUESusRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsUnPgUESusRx = _JnxMbgPgwGtpV2ICsUnPgUESusRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 401),
    _JnxMbgPgwGtpV2ICsUnPgUESusRx_Type()
)
jnxMbgPgwGtpV2ICsUnPgUESusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsUnPgUESusRx.setStatus("current")
_JnxMbgPgwGtpV2ICsUnPgUESusTx_Type = Counter64
_JnxMbgPgwGtpV2ICsUnPgUESusTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsUnPgUESusTx = _JnxMbgPgwGtpV2ICsUnPgUESusTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 402),
    _JnxMbgPgwGtpV2ICsUnPgUESusTx_Type()
)
jnxMbgPgwGtpV2ICsUnPgUESusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsUnPgUESusTx.setStatus("current")
_JnxMbgPgwGtpV2ICsInvTotLenRx_Type = Counter64
_JnxMbgPgwGtpV2ICsInvTotLenRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsInvTotLenRx = _JnxMbgPgwGtpV2ICsInvTotLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 403),
    _JnxMbgPgwGtpV2ICsInvTotLenRx_Type()
)
jnxMbgPgwGtpV2ICsInvTotLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInvTotLenRx.setStatus("current")
_JnxMbgPgwGtpV2ICsInvTotLenTx_Type = Counter64
_JnxMbgPgwGtpV2ICsInvTotLenTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsInvTotLenTx = _JnxMbgPgwGtpV2ICsInvTotLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 404),
    _JnxMbgPgwGtpV2ICsInvTotLenTx_Type()
)
jnxMbgPgwGtpV2ICsInvTotLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInvTotLenTx.setStatus("current")
_JnxMbgPgwGtpV2ICsDtForNtSupRx_Type = Counter64
_JnxMbgPgwGtpV2ICsDtForNtSupRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsDtForNtSupRx = _JnxMbgPgwGtpV2ICsDtForNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 405),
    _JnxMbgPgwGtpV2ICsDtForNtSupRx_Type()
)
jnxMbgPgwGtpV2ICsDtForNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsDtForNtSupRx.setStatus("current")
_JnxMbgPgwGtpV2ICsDtForNtSupTx_Type = Counter64
_JnxMbgPgwGtpV2ICsDtForNtSupTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsDtForNtSupTx = _JnxMbgPgwGtpV2ICsDtForNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 406),
    _JnxMbgPgwGtpV2ICsDtForNtSupTx_Type()
)
jnxMbgPgwGtpV2ICsDtForNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsDtForNtSupTx.setStatus("current")
_JnxMbgPgwGtpV2ICsInReFRePrRx_Type = Counter64
_JnxMbgPgwGtpV2ICsInReFRePrRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsInReFRePrRx = _JnxMbgPgwGtpV2ICsInReFRePrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 407),
    _JnxMbgPgwGtpV2ICsInReFRePrRx_Type()
)
jnxMbgPgwGtpV2ICsInReFRePrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInReFRePrRx.setStatus("current")
_JnxMbgPgwGtpV2ICsInReFRePrTx_Type = Counter64
_JnxMbgPgwGtpV2ICsInReFRePrTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsInReFRePrTx = _JnxMbgPgwGtpV2ICsInReFRePrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 408),
    _JnxMbgPgwGtpV2ICsInReFRePrTx_Type()
)
jnxMbgPgwGtpV2ICsInReFRePrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInReFRePrTx.setStatus("current")
_JnxMbgPgwGtpV2ICsInvPrRx_Type = Counter64
_JnxMbgPgwGtpV2ICsInvPrRx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsInvPrRx = _JnxMbgPgwGtpV2ICsInvPrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 409),
    _JnxMbgPgwGtpV2ICsInvPrRx_Type()
)
jnxMbgPgwGtpV2ICsInvPrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInvPrRx.setStatus("current")
_JnxMbgPgwGtpV2ICsInvPrTx_Type = Counter64
_JnxMbgPgwGtpV2ICsInvPrTx_Object = MibTableColumn
jnxMbgPgwGtpV2ICsInvPrTx = _JnxMbgPgwGtpV2ICsInvPrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 410),
    _JnxMbgPgwGtpV2ICsInvPrTx_Type()
)
jnxMbgPgwGtpV2ICsInvPrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwGtpV2ICsInvPrTx.setStatus("current")
_JnxMbgPgwV1InitPdpCxtReqRx_Type = Counter64
_JnxMbgPgwV1InitPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwV1InitPdpCxtReqRx = _JnxMbgPgwV1InitPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 411),
    _JnxMbgPgwV1InitPdpCxtReqRx_Type()
)
jnxMbgPgwV1InitPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1InitPdpCxtReqRx.setStatus("current")
_JnxMbgPgwV1InitPdpCxtReqTx_Type = Counter64
_JnxMbgPgwV1InitPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwV1InitPdpCxtReqTx = _JnxMbgPgwV1InitPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 412),
    _JnxMbgPgwV1InitPdpCxtReqTx_Type()
)
jnxMbgPgwV1InitPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1InitPdpCxtReqTx.setStatus("current")
_JnxMbgPgwV1InitPdpCxtRspRx_Type = Counter64
_JnxMbgPgwV1InitPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwV1InitPdpCxtRspRx = _JnxMbgPgwV1InitPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 413),
    _JnxMbgPgwV1InitPdpCxtRspRx_Type()
)
jnxMbgPgwV1InitPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1InitPdpCxtRspRx.setStatus("current")
_JnxMbgPgwV1InitPdpCxtRspTx_Type = Counter64
_JnxMbgPgwV1InitPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwV1InitPdpCxtRspTx = _JnxMbgPgwV1InitPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 414),
    _JnxMbgPgwV1InitPdpCxtRspTx_Type()
)
jnxMbgPgwV1InitPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV1InitPdpCxtRspTx.setStatus("current")
_JnxMbgPgwV2SuspNotifRx_Type = Counter64
_JnxMbgPgwV2SuspNotifRx_Object = MibTableColumn
jnxMbgPgwV2SuspNotifRx = _JnxMbgPgwV2SuspNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 415),
    _JnxMbgPgwV2SuspNotifRx_Type()
)
jnxMbgPgwV2SuspNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2SuspNotifRx.setStatus("current")
_JnxMbgPgwV2SuspNotifTx_Type = Counter64
_JnxMbgPgwV2SuspNotifTx_Object = MibTableColumn
jnxMbgPgwV2SuspNotifTx = _JnxMbgPgwV2SuspNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 416),
    _JnxMbgPgwV2SuspNotifTx_Type()
)
jnxMbgPgwV2SuspNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2SuspNotifTx.setStatus("current")
_JnxMbgPgwV2SuspAckRx_Type = Counter64
_JnxMbgPgwV2SuspAckRx_Object = MibTableColumn
jnxMbgPgwV2SuspAckRx = _JnxMbgPgwV2SuspAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 417),
    _JnxMbgPgwV2SuspAckRx_Type()
)
jnxMbgPgwV2SuspAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2SuspAckRx.setStatus("current")
_JnxMbgPgwV2SuspAckTx_Type = Counter64
_JnxMbgPgwV2SuspAckTx_Object = MibTableColumn
jnxMbgPgwV2SuspAckTx = _JnxMbgPgwV2SuspAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 418),
    _JnxMbgPgwV2SuspAckTx_Type()
)
jnxMbgPgwV2SuspAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2SuspAckTx.setStatus("current")
_JnxMbgPgwV2ResumeNotifRx_Type = Counter64
_JnxMbgPgwV2ResumeNotifRx_Object = MibTableColumn
jnxMbgPgwV2ResumeNotifRx = _JnxMbgPgwV2ResumeNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 419),
    _JnxMbgPgwV2ResumeNotifRx_Type()
)
jnxMbgPgwV2ResumeNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ResumeNotifRx.setStatus("current")
_JnxMbgPgwV2ResumeNotifTx_Type = Counter64
_JnxMbgPgwV2ResumeNotifTx_Object = MibTableColumn
jnxMbgPgwV2ResumeNotifTx = _JnxMbgPgwV2ResumeNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 420),
    _JnxMbgPgwV2ResumeNotifTx_Type()
)
jnxMbgPgwV2ResumeNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ResumeNotifTx.setStatus("current")
_JnxMbgPgwV2ResumeAckRx_Type = Counter64
_JnxMbgPgwV2ResumeAckRx_Object = MibTableColumn
jnxMbgPgwV2ResumeAckRx = _JnxMbgPgwV2ResumeAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 421),
    _JnxMbgPgwV2ResumeAckRx_Type()
)
jnxMbgPgwV2ResumeAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ResumeAckRx.setStatus("current")
_JnxMbgPgwV2ResumeAckTx_Type = Counter64
_JnxMbgPgwV2ResumeAckTx_Object = MibTableColumn
jnxMbgPgwV2ResumeAckTx = _JnxMbgPgwV2ResumeAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 422),
    _JnxMbgPgwV2ResumeAckTx_Type()
)
jnxMbgPgwV2ResumeAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2ResumeAckTx.setStatus("current")
_JnxMbgPgwV2PiggybackMsgRx_Type = Counter64
_JnxMbgPgwV2PiggybackMsgRx_Object = MibTableColumn
jnxMbgPgwV2PiggybackMsgRx = _JnxMbgPgwV2PiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 423),
    _JnxMbgPgwV2PiggybackMsgRx_Type()
)
jnxMbgPgwV2PiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2PiggybackMsgRx.setStatus("current")
_JnxMbgPgwV2PiggybackMsgTx_Type = Counter64
_JnxMbgPgwV2PiggybackMsgTx_Object = MibTableColumn
jnxMbgPgwV2PiggybackMsgTx = _JnxMbgPgwV2PiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 10, 1, 424),
    _JnxMbgPgwV2PiggybackMsgTx_Type()
)
jnxMbgPgwV2PiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwV2PiggybackMsgTx.setStatus("current")
_JnxMbgPgwGtpIfStatsTable_Object = MibTable
jnxMbgPgwGtpIfStatsTable = _JnxMbgPgwGtpIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11)
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpIfStatsTable.setStatus("current")
_JnxMbgPgwGtpIfStatsEntry_Object = MibTableRow
jnxMbgPgwGtpIfStatsEntry = _JnxMbgPgwGtpIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1)
)
jnxMbgPgwGtpIfStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
    (0, "JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwIfIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpIfStatsEntry.setStatus("current")
_JnxMbgPgwIfIndex_Type = Unsigned32
_JnxMbgPgwIfIndex_Object = MibTableColumn
jnxMbgPgwIfIndex = _JnxMbgPgwIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 1),
    _JnxMbgPgwIfIndex_Type()
)
jnxMbgPgwIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgPgwIfIndex.setStatus("current")
_JnxMbgPgwIfType_Type = DisplayString
_JnxMbgPgwIfType_Object = MibTableColumn
jnxMbgPgwIfType = _JnxMbgPgwIfType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 2),
    _JnxMbgPgwIfType_Type()
)
jnxMbgPgwIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfType.setStatus("current")
_JnxMbgPgwIfRxPacketsDropped_Type = Counter64
_JnxMbgPgwIfRxPacketsDropped_Object = MibTableColumn
jnxMbgPgwIfRxPacketsDropped = _JnxMbgPgwIfRxPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 3),
    _JnxMbgPgwIfRxPacketsDropped_Type()
)
jnxMbgPgwIfRxPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfRxPacketsDropped.setStatus("current")
_JnxMbgPgwIfPacketAllocFail_Type = Counter64
_JnxMbgPgwIfPacketAllocFail_Object = MibTableColumn
jnxMbgPgwIfPacketAllocFail = _JnxMbgPgwIfPacketAllocFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 4),
    _JnxMbgPgwIfPacketAllocFail_Type()
)
jnxMbgPgwIfPacketAllocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfPacketAllocFail.setStatus("current")
_JnxMbgPgwIfPacketSendFail_Type = Counter64
_JnxMbgPgwIfPacketSendFail_Object = MibTableColumn
jnxMbgPgwIfPacketSendFail = _JnxMbgPgwIfPacketSendFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 5),
    _JnxMbgPgwIfPacketSendFail_Type()
)
jnxMbgPgwIfPacketSendFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfPacketSendFail.setStatus("current")
_JnxMbgPgwIfIPVerErrRx_Type = Counter64
_JnxMbgPgwIfIPVerErrRx_Object = MibTableColumn
jnxMbgPgwIfIPVerErrRx = _JnxMbgPgwIfIPVerErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 6),
    _JnxMbgPgwIfIPVerErrRx_Type()
)
jnxMbgPgwIfIPVerErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfIPVerErrRx.setStatus("current")
_JnxMbgPgwIfIPProtoErrRx_Type = Counter64
_JnxMbgPgwIfIPProtoErrRx_Object = MibTableColumn
jnxMbgPgwIfIPProtoErrRx = _JnxMbgPgwIfIPProtoErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 7),
    _JnxMbgPgwIfIPProtoErrRx_Type()
)
jnxMbgPgwIfIPProtoErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfIPProtoErrRx.setStatus("current")
_JnxMbgPgwIfGTPPortErrRx_Type = Counter64
_JnxMbgPgwIfGTPPortErrRx_Object = MibTableColumn
jnxMbgPgwIfGTPPortErrRx = _JnxMbgPgwIfGTPPortErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 8),
    _JnxMbgPgwIfGTPPortErrRx_Type()
)
jnxMbgPgwIfGTPPortErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGTPPortErrRx.setStatus("current")
_JnxMbgPgwIfGTPUnknVerRx_Type = Counter64
_JnxMbgPgwIfGTPUnknVerRx_Object = MibTableColumn
jnxMbgPgwIfGTPUnknVerRx = _JnxMbgPgwIfGTPUnknVerRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 9),
    _JnxMbgPgwIfGTPUnknVerRx_Type()
)
jnxMbgPgwIfGTPUnknVerRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGTPUnknVerRx.setStatus("current")
_JnxMbgPgwIfPcktLenErrRx_Type = Counter64
_JnxMbgPgwIfPcktLenErrRx_Object = MibTableColumn
jnxMbgPgwIfPcktLenErrRx = _JnxMbgPgwIfPcktLenErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 10),
    _JnxMbgPgwIfPcktLenErrRx_Type()
)
jnxMbgPgwIfPcktLenErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfPcktLenErrRx.setStatus("current")
_JnxMbgPgwIfUnknMsgRx_Type = Counter64
_JnxMbgPgwIfUnknMsgRx_Object = MibTableColumn
jnxMbgPgwIfUnknMsgRx = _JnxMbgPgwIfUnknMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 11),
    _JnxMbgPgwIfUnknMsgRx_Type()
)
jnxMbgPgwIfUnknMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfUnknMsgRx.setStatus("current")
_JnxMbgPgwIfV2ProtocolErrRx_Type = Counter64
_JnxMbgPgwIfV2ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwIfV2ProtocolErrRx = _JnxMbgPgwIfV2ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 12),
    _JnxMbgPgwIfV2ProtocolErrRx_Type()
)
jnxMbgPgwIfV2ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ProtocolErrRx.setStatus("current")
_JnxMbgPgwIfV2UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwIfV2UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwIfV2UnSupportedMsgRx = _JnxMbgPgwIfV2UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 13),
    _JnxMbgPgwIfV2UnSupportedMsgRx_Type()
)
jnxMbgPgwIfV2UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwIfV2T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwIfV2T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwIfV2T3RespTmrExpRx = _JnxMbgPgwIfV2T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 14),
    _JnxMbgPgwIfV2T3RespTmrExpRx_Type()
)
jnxMbgPgwIfV2T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwIfV2GlbNumMsgRx_Type = Counter64
_JnxMbgPgwIfV2GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwIfV2GlbNumMsgRx = _JnxMbgPgwIfV2GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 15),
    _JnxMbgPgwIfV2GlbNumMsgRx_Type()
)
jnxMbgPgwIfV2GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbNumMsgRx.setStatus("current")
_JnxMbgPgwIfV2GlbNumMsgTx_Type = Counter64
_JnxMbgPgwIfV2GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwIfV2GlbNumMsgTx = _JnxMbgPgwIfV2GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 16),
    _JnxMbgPgwIfV2GlbNumMsgTx_Type()
)
jnxMbgPgwIfV2GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbNumMsgTx.setStatus("current")
_JnxMbgPgwIfV2GlbNumBytesRx_Type = Counter64
_JnxMbgPgwIfV2GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwIfV2GlbNumBytesRx = _JnxMbgPgwIfV2GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 17),
    _JnxMbgPgwIfV2GlbNumBytesRx_Type()
)
jnxMbgPgwIfV2GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbNumBytesRx.setStatus("current")
_JnxMbgPgwIfV2GlbNumBytesTx_Type = Counter64
_JnxMbgPgwIfV2GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwIfV2GlbNumBytesTx = _JnxMbgPgwIfV2GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 18),
    _JnxMbgPgwIfV2GlbNumBytesTx_Type()
)
jnxMbgPgwIfV2GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbNumBytesTx.setStatus("current")
_JnxMbgPgwIfV2GlbEchoReqRx_Type = Counter64
_JnxMbgPgwIfV2GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwIfV2GlbEchoReqRx = _JnxMbgPgwIfV2GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 19),
    _JnxMbgPgwIfV2GlbEchoReqRx_Type()
)
jnxMbgPgwIfV2GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbEchoReqRx.setStatus("current")
_JnxMbgPgwIfV2GlbEchoReqTx_Type = Counter64
_JnxMbgPgwIfV2GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwIfV2GlbEchoReqTx = _JnxMbgPgwIfV2GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 20),
    _JnxMbgPgwIfV2GlbEchoReqTx_Type()
)
jnxMbgPgwIfV2GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbEchoReqTx.setStatus("current")
_JnxMbgPgwIfV2GlbEchoRespRx_Type = Counter64
_JnxMbgPgwIfV2GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwIfV2GlbEchoRespRx = _JnxMbgPgwIfV2GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 21),
    _JnxMbgPgwIfV2GlbEchoRespRx_Type()
)
jnxMbgPgwIfV2GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbEchoRespRx.setStatus("current")
_JnxMbgPgwIfV2GlbEchoRespTx_Type = Counter64
_JnxMbgPgwIfV2GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwIfV2GlbEchoRespTx = _JnxMbgPgwIfV2GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 22),
    _JnxMbgPgwIfV2GlbEchoRespTx_Type()
)
jnxMbgPgwIfV2GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2GlbEchoRespTx.setStatus("current")
_JnxMbgPgwIfV2VerNotSupRx_Type = Counter64
_JnxMbgPgwIfV2VerNotSupRx_Object = MibTableColumn
jnxMbgPgwIfV2VerNotSupRx = _JnxMbgPgwIfV2VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 23),
    _JnxMbgPgwIfV2VerNotSupRx_Type()
)
jnxMbgPgwIfV2VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2VerNotSupRx.setStatus("current")
_JnxMbgPgwIfV2VerNotSupTx_Type = Counter64
_JnxMbgPgwIfV2VerNotSupTx_Object = MibTableColumn
jnxMbgPgwIfV2VerNotSupTx = _JnxMbgPgwIfV2VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 24),
    _JnxMbgPgwIfV2VerNotSupTx_Type()
)
jnxMbgPgwIfV2VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2VerNotSupTx.setStatus("current")
_JnxMbgPgwIfV2CreateSessReqRx_Type = Counter64
_JnxMbgPgwIfV2CreateSessReqRx_Object = MibTableColumn
jnxMbgPgwIfV2CreateSessReqRx = _JnxMbgPgwIfV2CreateSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 25),
    _JnxMbgPgwIfV2CreateSessReqRx_Type()
)
jnxMbgPgwIfV2CreateSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CreateSessReqRx.setStatus("current")
_JnxMbgPgwIfV2CreateSessReqTx_Type = Counter64
_JnxMbgPgwIfV2CreateSessReqTx_Object = MibTableColumn
jnxMbgPgwIfV2CreateSessReqTx = _JnxMbgPgwIfV2CreateSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 26),
    _JnxMbgPgwIfV2CreateSessReqTx_Type()
)
jnxMbgPgwIfV2CreateSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CreateSessReqTx.setStatus("current")
_JnxMbgPgwIfV2CreateSessRspRx_Type = Counter64
_JnxMbgPgwIfV2CreateSessRspRx_Object = MibTableColumn
jnxMbgPgwIfV2CreateSessRspRx = _JnxMbgPgwIfV2CreateSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 27),
    _JnxMbgPgwIfV2CreateSessRspRx_Type()
)
jnxMbgPgwIfV2CreateSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CreateSessRspRx.setStatus("current")
_JnxMbgPgwIfV2CreateSessRspTx_Type = Counter64
_JnxMbgPgwIfV2CreateSessRspTx_Object = MibTableColumn
jnxMbgPgwIfV2CreateSessRspTx = _JnxMbgPgwIfV2CreateSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 28),
    _JnxMbgPgwIfV2CreateSessRspTx_Type()
)
jnxMbgPgwIfV2CreateSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CreateSessRspTx.setStatus("current")
_JnxMbgPgwIfV2ModBrReqRx_Type = Counter64
_JnxMbgPgwIfV2ModBrReqRx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrReqRx = _JnxMbgPgwIfV2ModBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 29),
    _JnxMbgPgwIfV2ModBrReqRx_Type()
)
jnxMbgPgwIfV2ModBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrReqRx.setStatus("current")
_JnxMbgPgwIfV2ModBrReqTx_Type = Counter64
_JnxMbgPgwIfV2ModBrReqTx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrReqTx = _JnxMbgPgwIfV2ModBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 30),
    _JnxMbgPgwIfV2ModBrReqTx_Type()
)
jnxMbgPgwIfV2ModBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrReqTx.setStatus("current")
_JnxMbgPgwIfV2ModBrRspRx_Type = Counter64
_JnxMbgPgwIfV2ModBrRspRx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrRspRx = _JnxMbgPgwIfV2ModBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 31),
    _JnxMbgPgwIfV2ModBrRspRx_Type()
)
jnxMbgPgwIfV2ModBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrRspRx.setStatus("current")
_JnxMbgPgwIfV2ModBrRspTx_Type = Counter64
_JnxMbgPgwIfV2ModBrRspTx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrRspTx = _JnxMbgPgwIfV2ModBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 32),
    _JnxMbgPgwIfV2ModBrRspTx_Type()
)
jnxMbgPgwIfV2ModBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrRspTx.setStatus("current")
_JnxMbgPgwIfV2DelSessReqRx_Type = Counter64
_JnxMbgPgwIfV2DelSessReqRx_Object = MibTableColumn
jnxMbgPgwIfV2DelSessReqRx = _JnxMbgPgwIfV2DelSessReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 33),
    _JnxMbgPgwIfV2DelSessReqRx_Type()
)
jnxMbgPgwIfV2DelSessReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelSessReqRx.setStatus("current")
_JnxMbgPgwIfV2DelSessReqTx_Type = Counter64
_JnxMbgPgwIfV2DelSessReqTx_Object = MibTableColumn
jnxMbgPgwIfV2DelSessReqTx = _JnxMbgPgwIfV2DelSessReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 34),
    _JnxMbgPgwIfV2DelSessReqTx_Type()
)
jnxMbgPgwIfV2DelSessReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelSessReqTx.setStatus("current")
_JnxMbgPgwIfV2DelSessRspRx_Type = Counter64
_JnxMbgPgwIfV2DelSessRspRx_Object = MibTableColumn
jnxMbgPgwIfV2DelSessRspRx = _JnxMbgPgwIfV2DelSessRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 35),
    _JnxMbgPgwIfV2DelSessRspRx_Type()
)
jnxMbgPgwIfV2DelSessRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelSessRspRx.setStatus("current")
_JnxMbgPgwIfV2DelSessRspTx_Type = Counter64
_JnxMbgPgwIfV2DelSessRspTx_Object = MibTableColumn
jnxMbgPgwIfV2DelSessRspTx = _JnxMbgPgwIfV2DelSessRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 36),
    _JnxMbgPgwIfV2DelSessRspTx_Type()
)
jnxMbgPgwIfV2DelSessRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelSessRspTx.setStatus("current")
_JnxMbgPgwIfV2CrtBrReqRx_Type = Counter64
_JnxMbgPgwIfV2CrtBrReqRx_Object = MibTableColumn
jnxMbgPgwIfV2CrtBrReqRx = _JnxMbgPgwIfV2CrtBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 37),
    _JnxMbgPgwIfV2CrtBrReqRx_Type()
)
jnxMbgPgwIfV2CrtBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CrtBrReqRx.setStatus("current")
_JnxMbgPgwIfV2CrtBrReqTx_Type = Counter64
_JnxMbgPgwIfV2CrtBrReqTx_Object = MibTableColumn
jnxMbgPgwIfV2CrtBrReqTx = _JnxMbgPgwIfV2CrtBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 38),
    _JnxMbgPgwIfV2CrtBrReqTx_Type()
)
jnxMbgPgwIfV2CrtBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CrtBrReqTx.setStatus("current")
_JnxMbgPgwIfV2CrtBrRspRx_Type = Counter64
_JnxMbgPgwIfV2CrtBrRspRx_Object = MibTableColumn
jnxMbgPgwIfV2CrtBrRspRx = _JnxMbgPgwIfV2CrtBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 39),
    _JnxMbgPgwIfV2CrtBrRspRx_Type()
)
jnxMbgPgwIfV2CrtBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CrtBrRspRx.setStatus("current")
_JnxMbgPgwIfV2CrtBrRspTx_Type = Counter64
_JnxMbgPgwIfV2CrtBrRspTx_Object = MibTableColumn
jnxMbgPgwIfV2CrtBrRspTx = _JnxMbgPgwIfV2CrtBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 40),
    _JnxMbgPgwIfV2CrtBrRspTx_Type()
)
jnxMbgPgwIfV2CrtBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2CrtBrRspTx.setStatus("current")
_JnxMbgPgwIfV2UpdBrReqRx_Type = Counter64
_JnxMbgPgwIfV2UpdBrReqRx_Object = MibTableColumn
jnxMbgPgwIfV2UpdBrReqRx = _JnxMbgPgwIfV2UpdBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 41),
    _JnxMbgPgwIfV2UpdBrReqRx_Type()
)
jnxMbgPgwIfV2UpdBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdBrReqRx.setStatus("current")
_JnxMbgPgwIfV2UpdBrReqTx_Type = Counter64
_JnxMbgPgwIfV2UpdBrReqTx_Object = MibTableColumn
jnxMbgPgwIfV2UpdBrReqTx = _JnxMbgPgwIfV2UpdBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 42),
    _JnxMbgPgwIfV2UpdBrReqTx_Type()
)
jnxMbgPgwIfV2UpdBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdBrReqTx.setStatus("current")
_JnxMbgPgwIfV2UpdBrRspRx_Type = Counter64
_JnxMbgPgwIfV2UpdBrRspRx_Object = MibTableColumn
jnxMbgPgwIfV2UpdBrRspRx = _JnxMbgPgwIfV2UpdBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 43),
    _JnxMbgPgwIfV2UpdBrRspRx_Type()
)
jnxMbgPgwIfV2UpdBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdBrRspRx.setStatus("current")
_JnxMbgPgwIfV2UpdBrRspTx_Type = Counter64
_JnxMbgPgwIfV2UpdBrRspTx_Object = MibTableColumn
jnxMbgPgwIfV2UpdBrRspTx = _JnxMbgPgwIfV2UpdBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 44),
    _JnxMbgPgwIfV2UpdBrRspTx_Type()
)
jnxMbgPgwIfV2UpdBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdBrRspTx.setStatus("current")
_JnxMbgPgwIfV2DelBrReqRx_Type = Counter64
_JnxMbgPgwIfV2DelBrReqRx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrReqRx = _JnxMbgPgwIfV2DelBrReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 45),
    _JnxMbgPgwIfV2DelBrReqRx_Type()
)
jnxMbgPgwIfV2DelBrReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrReqRx.setStatus("current")
_JnxMbgPgwIfV2DelBrReqTx_Type = Counter64
_JnxMbgPgwIfV2DelBrReqTx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrReqTx = _JnxMbgPgwIfV2DelBrReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 46),
    _JnxMbgPgwIfV2DelBrReqTx_Type()
)
jnxMbgPgwIfV2DelBrReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrReqTx.setStatus("current")
_JnxMbgPgwIfV2DelBrRspRx_Type = Counter64
_JnxMbgPgwIfV2DelBrRspRx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrRspRx = _JnxMbgPgwIfV2DelBrRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 47),
    _JnxMbgPgwIfV2DelBrRspRx_Type()
)
jnxMbgPgwIfV2DelBrRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrRspRx.setStatus("current")
_JnxMbgPgwIfV2DelBrRspTx_Type = Counter64
_JnxMbgPgwIfV2DelBrRspTx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrRspTx = _JnxMbgPgwIfV2DelBrRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 48),
    _JnxMbgPgwIfV2DelBrRspTx_Type()
)
jnxMbgPgwIfV2DelBrRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrRspTx.setStatus("current")
_JnxMbgPgwIfV2DelConnSetReqRx_Type = Counter64
_JnxMbgPgwIfV2DelConnSetReqRx_Object = MibTableColumn
jnxMbgPgwIfV2DelConnSetReqRx = _JnxMbgPgwIfV2DelConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 49),
    _JnxMbgPgwIfV2DelConnSetReqRx_Type()
)
jnxMbgPgwIfV2DelConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelConnSetReqRx.setStatus("current")
_JnxMbgPgwIfV2DelConnSetReqTx_Type = Counter64
_JnxMbgPgwIfV2DelConnSetReqTx_Object = MibTableColumn
jnxMbgPgwIfV2DelConnSetReqTx = _JnxMbgPgwIfV2DelConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 50),
    _JnxMbgPgwIfV2DelConnSetReqTx_Type()
)
jnxMbgPgwIfV2DelConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelConnSetReqTx.setStatus("current")
_JnxMbgPgwIfV2DelConnSetRspRx_Type = Counter64
_JnxMbgPgwIfV2DelConnSetRspRx_Object = MibTableColumn
jnxMbgPgwIfV2DelConnSetRspRx = _JnxMbgPgwIfV2DelConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 51),
    _JnxMbgPgwIfV2DelConnSetRspRx_Type()
)
jnxMbgPgwIfV2DelConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelConnSetRspRx.setStatus("current")
_JnxMbgPgwIfV2DelConnSetRspTx_Type = Counter64
_JnxMbgPgwIfV2DelConnSetRspTx_Object = MibTableColumn
jnxMbgPgwIfV2DelConnSetRspTx = _JnxMbgPgwIfV2DelConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 52),
    _JnxMbgPgwIfV2DelConnSetRspTx_Type()
)
jnxMbgPgwIfV2DelConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelConnSetRspTx.setStatus("current")
_JnxMbgPgwIfV2UpdConnSetReqRx_Type = Counter64
_JnxMbgPgwIfV2UpdConnSetReqRx_Object = MibTableColumn
jnxMbgPgwIfV2UpdConnSetReqRx = _JnxMbgPgwIfV2UpdConnSetReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 53),
    _JnxMbgPgwIfV2UpdConnSetReqRx_Type()
)
jnxMbgPgwIfV2UpdConnSetReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdConnSetReqRx.setStatus("current")
_JnxMbgPgwIfV2UpdConnSetReqTx_Type = Counter64
_JnxMbgPgwIfV2UpdConnSetReqTx_Object = MibTableColumn
jnxMbgPgwIfV2UpdConnSetReqTx = _JnxMbgPgwIfV2UpdConnSetReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 54),
    _JnxMbgPgwIfV2UpdConnSetReqTx_Type()
)
jnxMbgPgwIfV2UpdConnSetReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdConnSetReqTx.setStatus("current")
_JnxMbgPgwIfV2UpdConnSetRspRx_Type = Counter64
_JnxMbgPgwIfV2UpdConnSetRspRx_Object = MibTableColumn
jnxMbgPgwIfV2UpdConnSetRspRx = _JnxMbgPgwIfV2UpdConnSetRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 55),
    _JnxMbgPgwIfV2UpdConnSetRspRx_Type()
)
jnxMbgPgwIfV2UpdConnSetRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdConnSetRspRx.setStatus("current")
_JnxMbgPgwIfV2UpdConnSetRspTx_Type = Counter64
_JnxMbgPgwIfV2UpdConnSetRspTx_Object = MibTableColumn
jnxMbgPgwIfV2UpdConnSetRspTx = _JnxMbgPgwIfV2UpdConnSetRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 56),
    _JnxMbgPgwIfV2UpdConnSetRspTx_Type()
)
jnxMbgPgwIfV2UpdConnSetRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2UpdConnSetRspTx.setStatus("current")
_JnxMbgPgwIfV2ModBrCmdRx_Type = Counter64
_JnxMbgPgwIfV2ModBrCmdRx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrCmdRx = _JnxMbgPgwIfV2ModBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 57),
    _JnxMbgPgwIfV2ModBrCmdRx_Type()
)
jnxMbgPgwIfV2ModBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrCmdRx.setStatus("current")
_JnxMbgPgwIfV2ModBrCmdTx_Type = Counter64
_JnxMbgPgwIfV2ModBrCmdTx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrCmdTx = _JnxMbgPgwIfV2ModBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 58),
    _JnxMbgPgwIfV2ModBrCmdTx_Type()
)
jnxMbgPgwIfV2ModBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrCmdTx.setStatus("current")
_JnxMbgPgwIfV2ModBrFlrIndRx_Type = Counter64
_JnxMbgPgwIfV2ModBrFlrIndRx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrFlrIndRx = _JnxMbgPgwIfV2ModBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 59),
    _JnxMbgPgwIfV2ModBrFlrIndRx_Type()
)
jnxMbgPgwIfV2ModBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrFlrIndRx.setStatus("current")
_JnxMbgPgwIfV2ModBrFlrIndTx_Type = Counter64
_JnxMbgPgwIfV2ModBrFlrIndTx_Object = MibTableColumn
jnxMbgPgwIfV2ModBrFlrIndTx = _JnxMbgPgwIfV2ModBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 60),
    _JnxMbgPgwIfV2ModBrFlrIndTx_Type()
)
jnxMbgPgwIfV2ModBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ModBrFlrIndTx.setStatus("current")
_JnxMbgPgwIfV2DelBrCmdRx_Type = Counter64
_JnxMbgPgwIfV2DelBrCmdRx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrCmdRx = _JnxMbgPgwIfV2DelBrCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 61),
    _JnxMbgPgwIfV2DelBrCmdRx_Type()
)
jnxMbgPgwIfV2DelBrCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrCmdRx.setStatus("current")
_JnxMbgPgwIfV2DelBrCmdTx_Type = Counter64
_JnxMbgPgwIfV2DelBrCmdTx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrCmdTx = _JnxMbgPgwIfV2DelBrCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 62),
    _JnxMbgPgwIfV2DelBrCmdTx_Type()
)
jnxMbgPgwIfV2DelBrCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrCmdTx.setStatus("current")
_JnxMbgPgwIfV2DelBrFlrIndRx_Type = Counter64
_JnxMbgPgwIfV2DelBrFlrIndRx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrFlrIndRx = _JnxMbgPgwIfV2DelBrFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 63),
    _JnxMbgPgwIfV2DelBrFlrIndRx_Type()
)
jnxMbgPgwIfV2DelBrFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrFlrIndRx.setStatus("current")
_JnxMbgPgwIfV2DelBrFlrIndTx_Type = Counter64
_JnxMbgPgwIfV2DelBrFlrIndTx_Object = MibTableColumn
jnxMbgPgwIfV2DelBrFlrIndTx = _JnxMbgPgwIfV2DelBrFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 64),
    _JnxMbgPgwIfV2DelBrFlrIndTx_Type()
)
jnxMbgPgwIfV2DelBrFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2DelBrFlrIndTx.setStatus("current")
_JnxMbgPgwIfV2BrResCmdRx_Type = Counter64
_JnxMbgPgwIfV2BrResCmdRx_Object = MibTableColumn
jnxMbgPgwIfV2BrResCmdRx = _JnxMbgPgwIfV2BrResCmdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 65),
    _JnxMbgPgwIfV2BrResCmdRx_Type()
)
jnxMbgPgwIfV2BrResCmdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2BrResCmdRx.setStatus("current")
_JnxMbgPgwIfV2BrResCmdTx_Type = Counter64
_JnxMbgPgwIfV2BrResCmdTx_Object = MibTableColumn
jnxMbgPgwIfV2BrResCmdTx = _JnxMbgPgwIfV2BrResCmdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 66),
    _JnxMbgPgwIfV2BrResCmdTx_Type()
)
jnxMbgPgwIfV2BrResCmdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2BrResCmdTx.setStatus("current")
_JnxMbgPgwIfV2BrResFlrIndRx_Type = Counter64
_JnxMbgPgwIfV2BrResFlrIndRx_Object = MibTableColumn
jnxMbgPgwIfV2BrResFlrIndRx = _JnxMbgPgwIfV2BrResFlrIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 67),
    _JnxMbgPgwIfV2BrResFlrIndRx_Type()
)
jnxMbgPgwIfV2BrResFlrIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2BrResFlrIndRx.setStatus("current")
_JnxMbgPgwIfV2BrResFlrIndTx_Type = Counter64
_JnxMbgPgwIfV2BrResFlrIndTx_Object = MibTableColumn
jnxMbgPgwIfV2BrResFlrIndTx = _JnxMbgPgwIfV2BrResFlrIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 68),
    _JnxMbgPgwIfV2BrResFlrIndTx_Type()
)
jnxMbgPgwIfV2BrResFlrIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2BrResFlrIndTx.setStatus("current")
_JnxMbgPgwIfV2ICsReqAcceptRx_Type = Counter64
_JnxMbgPgwIfV2ICsReqAcceptRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsReqAcceptRx = _JnxMbgPgwIfV2ICsReqAcceptRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 69),
    _JnxMbgPgwIfV2ICsReqAcceptRx_Type()
)
jnxMbgPgwIfV2ICsReqAcceptRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsReqAcceptRx.setStatus("current")
_JnxMbgPgwIfV2ICsReqAcceptTx_Type = Counter64
_JnxMbgPgwIfV2ICsReqAcceptTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsReqAcceptTx = _JnxMbgPgwIfV2ICsReqAcceptTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 70),
    _JnxMbgPgwIfV2ICsReqAcceptTx_Type()
)
jnxMbgPgwIfV2ICsReqAcceptTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsReqAcceptTx.setStatus("current")
_JnxMbgPgwIfV2ICsAcceptPartRx_Type = Counter64
_JnxMbgPgwIfV2ICsAcceptPartRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAcceptPartRx = _JnxMbgPgwIfV2ICsAcceptPartRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 71),
    _JnxMbgPgwIfV2ICsAcceptPartRx_Type()
)
jnxMbgPgwIfV2ICsAcceptPartRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAcceptPartRx.setStatus("current")
_JnxMbgPgwIfV2ICsAcceptPartTx_Type = Counter64
_JnxMbgPgwIfV2ICsAcceptPartTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAcceptPartTx = _JnxMbgPgwIfV2ICsAcceptPartTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 72),
    _JnxMbgPgwIfV2ICsAcceptPartTx_Type()
)
jnxMbgPgwIfV2ICsAcceptPartTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAcceptPartTx.setStatus("current")
_JnxMbgPgwIfV2ICsNewPTNPrefRx_Type = Counter64
_JnxMbgPgwIfV2ICsNewPTNPrefRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNewPTNPrefRx = _JnxMbgPgwIfV2ICsNewPTNPrefRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 73),
    _JnxMbgPgwIfV2ICsNewPTNPrefRx_Type()
)
jnxMbgPgwIfV2ICsNewPTNPrefRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNewPTNPrefRx.setStatus("current")
_JnxMbgPgwIfV2ICsNewPTNPrefTx_Type = Counter64
_JnxMbgPgwIfV2ICsNewPTNPrefTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNewPTNPrefTx = _JnxMbgPgwIfV2ICsNewPTNPrefTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 74),
    _JnxMbgPgwIfV2ICsNewPTNPrefTx_Type()
)
jnxMbgPgwIfV2ICsNewPTNPrefTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNewPTNPrefTx.setStatus("current")
_JnxMbgPgwIfV2ICsNewPTSIAdbrRx_Type = Counter64
_JnxMbgPgwIfV2ICsNewPTSIAdbrRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNewPTSIAdbrRx = _JnxMbgPgwIfV2ICsNewPTSIAdbrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 75),
    _JnxMbgPgwIfV2ICsNewPTSIAdbrRx_Type()
)
jnxMbgPgwIfV2ICsNewPTSIAdbrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNewPTSIAdbrRx.setStatus("current")
_JnxMbgPgwIfV2ICsNewPTSIAdbrTx_Type = Counter64
_JnxMbgPgwIfV2ICsNewPTSIAdbrTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNewPTSIAdbrTx = _JnxMbgPgwIfV2ICsNewPTSIAdbrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 76),
    _JnxMbgPgwIfV2ICsNewPTSIAdbrTx_Type()
)
jnxMbgPgwIfV2ICsNewPTSIAdbrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNewPTSIAdbrTx.setStatus("current")
_JnxMbgPgwIfV2ICsCtxNotFndRx_Type = Counter64
_JnxMbgPgwIfV2ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsCtxNotFndRx = _JnxMbgPgwIfV2ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 77),
    _JnxMbgPgwIfV2ICsCtxNotFndRx_Type()
)
jnxMbgPgwIfV2ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsCtxNotFndRx.setStatus("current")
_JnxMbgPgwIfV2ICsCtxNotFndTx_Type = Counter64
_JnxMbgPgwIfV2ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsCtxNotFndTx = _JnxMbgPgwIfV2ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 78),
    _JnxMbgPgwIfV2ICsCtxNotFndTx_Type()
)
jnxMbgPgwIfV2ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsCtxNotFndTx.setStatus("current")
_JnxMbgPgwIfV2ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwIfV2ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsInvMsgFmtRx = _JnxMbgPgwIfV2ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 79),
    _JnxMbgPgwIfV2ICsInvMsgFmtRx_Type()
)
jnxMbgPgwIfV2ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwIfV2ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwIfV2ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsInvMsgFmtTx = _JnxMbgPgwIfV2ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 80),
    _JnxMbgPgwIfV2ICsInvMsgFmtTx_Type()
)
jnxMbgPgwIfV2ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwIfV2ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwIfV2ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsVerNotSuppRx = _JnxMbgPgwIfV2ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 81),
    _JnxMbgPgwIfV2ICsVerNotSuppRx_Type()
)
jnxMbgPgwIfV2ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwIfV2ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwIfV2ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsVerNotSuppTx = _JnxMbgPgwIfV2ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 82),
    _JnxMbgPgwIfV2ICsVerNotSuppTx_Type()
)
jnxMbgPgwIfV2ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwIfV2ICsInvLenRx_Type = Counter64
_JnxMbgPgwIfV2ICsInvLenRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsInvLenRx = _JnxMbgPgwIfV2ICsInvLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 83),
    _JnxMbgPgwIfV2ICsInvLenRx_Type()
)
jnxMbgPgwIfV2ICsInvLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsInvLenRx.setStatus("current")
_JnxMbgPgwIfV2ICsInvLenTx_Type = Counter64
_JnxMbgPgwIfV2ICsInvLenTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsInvLenTx = _JnxMbgPgwIfV2ICsInvLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 84),
    _JnxMbgPgwIfV2ICsInvLenTx_Type()
)
jnxMbgPgwIfV2ICsInvLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsInvLenTx.setStatus("current")
_JnxMbgPgwIfV2ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwIfV2ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsServNotSuppRx = _JnxMbgPgwIfV2ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 85),
    _JnxMbgPgwIfV2ICsServNotSuppRx_Type()
)
jnxMbgPgwIfV2ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwIfV2ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwIfV2ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsServNotSuppTx = _JnxMbgPgwIfV2ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 86),
    _JnxMbgPgwIfV2ICsServNotSuppTx_Type()
)
jnxMbgPgwIfV2ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwIfV2ICsManIEIncorrRx_Type = Counter64
_JnxMbgPgwIfV2ICsManIEIncorrRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsManIEIncorrRx = _JnxMbgPgwIfV2ICsManIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 87),
    _JnxMbgPgwIfV2ICsManIEIncorrRx_Type()
)
jnxMbgPgwIfV2ICsManIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsManIEIncorrRx.setStatus("current")
_JnxMbgPgwIfV2ICsManIEIncorrTx_Type = Counter64
_JnxMbgPgwIfV2ICsManIEIncorrTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsManIEIncorrTx = _JnxMbgPgwIfV2ICsManIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 88),
    _JnxMbgPgwIfV2ICsManIEIncorrTx_Type()
)
jnxMbgPgwIfV2ICsManIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsManIEIncorrTx.setStatus("current")
_JnxMbgPgwIfV2ICsManIEMissRx_Type = Counter64
_JnxMbgPgwIfV2ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsManIEMissRx = _JnxMbgPgwIfV2ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 89),
    _JnxMbgPgwIfV2ICsManIEMissRx_Type()
)
jnxMbgPgwIfV2ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsManIEMissRx.setStatus("current")
_JnxMbgPgwIfV2ICsManIEMissTx_Type = Counter64
_JnxMbgPgwIfV2ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsManIEMissTx = _JnxMbgPgwIfV2ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 90),
    _JnxMbgPgwIfV2ICsManIEMissTx_Type()
)
jnxMbgPgwIfV2ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsManIEMissTx.setStatus("current")
_JnxMbgPgwIfV2ICsOptIEIncorrRx_Type = Counter64
_JnxMbgPgwIfV2ICsOptIEIncorrRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsOptIEIncorrRx = _JnxMbgPgwIfV2ICsOptIEIncorrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 91),
    _JnxMbgPgwIfV2ICsOptIEIncorrRx_Type()
)
jnxMbgPgwIfV2ICsOptIEIncorrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsOptIEIncorrRx.setStatus("current")
_JnxMbgPgwIfV2ICsOptIEIncorrTx_Type = Counter64
_JnxMbgPgwIfV2ICsOptIEIncorrTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsOptIEIncorrTx = _JnxMbgPgwIfV2ICsOptIEIncorrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 92),
    _JnxMbgPgwIfV2ICsOptIEIncorrTx_Type()
)
jnxMbgPgwIfV2ICsOptIEIncorrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsOptIEIncorrTx.setStatus("current")
_JnxMbgPgwIfV2ICsSysFailRx_Type = Counter64
_JnxMbgPgwIfV2ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsSysFailRx = _JnxMbgPgwIfV2ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 93),
    _JnxMbgPgwIfV2ICsSysFailRx_Type()
)
jnxMbgPgwIfV2ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsSysFailRx.setStatus("current")
_JnxMbgPgwIfV2ICsSysFailTx_Type = Counter64
_JnxMbgPgwIfV2ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsSysFailTx = _JnxMbgPgwIfV2ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 94),
    _JnxMbgPgwIfV2ICsSysFailTx_Type()
)
jnxMbgPgwIfV2ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsSysFailTx.setStatus("current")
_JnxMbgPgwIfV2ICsNoResRx_Type = Counter64
_JnxMbgPgwIfV2ICsNoResRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNoResRx = _JnxMbgPgwIfV2ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 95),
    _JnxMbgPgwIfV2ICsNoResRx_Type()
)
jnxMbgPgwIfV2ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNoResRx.setStatus("current")
_JnxMbgPgwIfV2ICsNoResTx_Type = Counter64
_JnxMbgPgwIfV2ICsNoResTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNoResTx = _JnxMbgPgwIfV2ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 96),
    _JnxMbgPgwIfV2ICsNoResTx_Type()
)
jnxMbgPgwIfV2ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNoResTx.setStatus("current")
_JnxMbgPgwIfV2ICsTFTSMANTErRx_Type = Counter64
_JnxMbgPgwIfV2ICsTFTSMANTErRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsTFTSMANTErRx = _JnxMbgPgwIfV2ICsTFTSMANTErRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 97),
    _JnxMbgPgwIfV2ICsTFTSMANTErRx_Type()
)
jnxMbgPgwIfV2ICsTFTSMANTErRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsTFTSMANTErRx.setStatus("current")
_JnxMbgPgwIfV2ICsTFTSMANTErTx_Type = Counter64
_JnxMbgPgwIfV2ICsTFTSMANTErTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsTFTSMANTErTx = _JnxMbgPgwIfV2ICsTFTSMANTErTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 98),
    _JnxMbgPgwIfV2ICsTFTSMANTErTx_Type()
)
jnxMbgPgwIfV2ICsTFTSMANTErTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsTFTSMANTErTx.setStatus("current")
_JnxMbgPgwIfV2ICsTFTSysErrRx_Type = Counter64
_JnxMbgPgwIfV2ICsTFTSysErrRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsTFTSysErrRx = _JnxMbgPgwIfV2ICsTFTSysErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 99),
    _JnxMbgPgwIfV2ICsTFTSysErrRx_Type()
)
jnxMbgPgwIfV2ICsTFTSysErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsTFTSysErrRx.setStatus("current")
_JnxMbgPgwIfV2ICsTFTSysErrTx_Type = Counter64
_JnxMbgPgwIfV2ICsTFTSysErrTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsTFTSysErrTx = _JnxMbgPgwIfV2ICsTFTSysErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 100),
    _JnxMbgPgwIfV2ICsTFTSysErrTx_Type()
)
jnxMbgPgwIfV2ICsTFTSysErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsTFTSysErrTx.setStatus("current")
_JnxMbgPgwIfV2ICsPkFltManErrRx_Type = Counter64
_JnxMbgPgwIfV2ICsPkFltManErrRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPkFltManErrRx = _JnxMbgPgwIfV2ICsPkFltManErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 101),
    _JnxMbgPgwIfV2ICsPkFltManErrRx_Type()
)
jnxMbgPgwIfV2ICsPkFltManErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPkFltManErrRx.setStatus("current")
_JnxMbgPgwIfV2ICsPkFltManErrTx_Type = Counter64
_JnxMbgPgwIfV2ICsPkFltManErrTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPkFltManErrTx = _JnxMbgPgwIfV2ICsPkFltManErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 102),
    _JnxMbgPgwIfV2ICsPkFltManErrTx_Type()
)
jnxMbgPgwIfV2ICsPkFltManErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPkFltManErrTx.setStatus("current")
_JnxMbgPgwIfV2ICsPkFltSynErrRx_Type = Counter64
_JnxMbgPgwIfV2ICsPkFltSynErrRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPkFltSynErrRx = _JnxMbgPgwIfV2ICsPkFltSynErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 103),
    _JnxMbgPgwIfV2ICsPkFltSynErrRx_Type()
)
jnxMbgPgwIfV2ICsPkFltSynErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPkFltSynErrRx.setStatus("current")
_JnxMbgPgwIfV2ICsPkFltSynErrTx_Type = Counter64
_JnxMbgPgwIfV2ICsPkFltSynErrTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPkFltSynErrTx = _JnxMbgPgwIfV2ICsPkFltSynErrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 104),
    _JnxMbgPgwIfV2ICsPkFltSynErrTx_Type()
)
jnxMbgPgwIfV2ICsPkFltSynErrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPkFltSynErrTx.setStatus("current")
_JnxMbgPgwIfV2ICsMisUnknAPNRx_Type = Counter64
_JnxMbgPgwIfV2ICsMisUnknAPNRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsMisUnknAPNRx = _JnxMbgPgwIfV2ICsMisUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 105),
    _JnxMbgPgwIfV2ICsMisUnknAPNRx_Type()
)
jnxMbgPgwIfV2ICsMisUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsMisUnknAPNRx.setStatus("current")
_JnxMbgPgwIfV2ICsMisUnknAPNTx_Type = Counter64
_JnxMbgPgwIfV2ICsMisUnknAPNTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsMisUnknAPNTx = _JnxMbgPgwIfV2ICsMisUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 106),
    _JnxMbgPgwIfV2ICsMisUnknAPNTx_Type()
)
jnxMbgPgwIfV2ICsMisUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsMisUnknAPNTx.setStatus("current")
_JnxMbgPgwIfV2ICsUnexpRptIERx_Type = Counter64
_JnxMbgPgwIfV2ICsUnexpRptIERx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUnexpRptIERx = _JnxMbgPgwIfV2ICsUnexpRptIERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 107),
    _JnxMbgPgwIfV2ICsUnexpRptIERx_Type()
)
jnxMbgPgwIfV2ICsUnexpRptIERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUnexpRptIERx.setStatus("current")
_JnxMbgPgwIfV2ICsUnexpRptIETx_Type = Counter64
_JnxMbgPgwIfV2ICsUnexpRptIETx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUnexpRptIETx = _JnxMbgPgwIfV2ICsUnexpRptIETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 108),
    _JnxMbgPgwIfV2ICsUnexpRptIETx_Type()
)
jnxMbgPgwIfV2ICsUnexpRptIETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUnexpRptIETx.setStatus("current")
_JnxMbgPgwIfV2ICsGREKeyNtFdRx_Type = Counter64
_JnxMbgPgwIfV2ICsGREKeyNtFdRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsGREKeyNtFdRx = _JnxMbgPgwIfV2ICsGREKeyNtFdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 109),
    _JnxMbgPgwIfV2ICsGREKeyNtFdRx_Type()
)
jnxMbgPgwIfV2ICsGREKeyNtFdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsGREKeyNtFdRx.setStatus("current")
_JnxMbgPgwIfV2ICsGREKeyNtFdTx_Type = Counter64
_JnxMbgPgwIfV2ICsGREKeyNtFdTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsGREKeyNtFdTx = _JnxMbgPgwIfV2ICsGREKeyNtFdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 110),
    _JnxMbgPgwIfV2ICsGREKeyNtFdTx_Type()
)
jnxMbgPgwIfV2ICsGREKeyNtFdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsGREKeyNtFdTx.setStatus("current")
_JnxMbgPgwIfV2ICsRelocFailRx_Type = Counter64
_JnxMbgPgwIfV2ICsRelocFailRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsRelocFailRx = _JnxMbgPgwIfV2ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 111),
    _JnxMbgPgwIfV2ICsRelocFailRx_Type()
)
jnxMbgPgwIfV2ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsRelocFailRx.setStatus("current")
_JnxMbgPgwIfV2ICsRelocFailTx_Type = Counter64
_JnxMbgPgwIfV2ICsRelocFailTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsRelocFailTx = _JnxMbgPgwIfV2ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 112),
    _JnxMbgPgwIfV2ICsRelocFailTx_Type()
)
jnxMbgPgwIfV2ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsRelocFailTx.setStatus("current")
_JnxMbgPgwIfV2ICsDeniedINRatRx_Type = Counter64
_JnxMbgPgwIfV2ICsDeniedINRatRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsDeniedINRatRx = _JnxMbgPgwIfV2ICsDeniedINRatRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 113),
    _JnxMbgPgwIfV2ICsDeniedINRatRx_Type()
)
jnxMbgPgwIfV2ICsDeniedINRatRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsDeniedINRatRx.setStatus("current")
_JnxMbgPgwIfV2ICsDeniedINRatTx_Type = Counter64
_JnxMbgPgwIfV2ICsDeniedINRatTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsDeniedINRatTx = _JnxMbgPgwIfV2ICsDeniedINRatTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 114),
    _JnxMbgPgwIfV2ICsDeniedINRatTx_Type()
)
jnxMbgPgwIfV2ICsDeniedINRatTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsDeniedINRatTx.setStatus("current")
_JnxMbgPgwIfV2ICsPTNotSuppRx_Type = Counter64
_JnxMbgPgwIfV2ICsPTNotSuppRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPTNotSuppRx = _JnxMbgPgwIfV2ICsPTNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 115),
    _JnxMbgPgwIfV2ICsPTNotSuppRx_Type()
)
jnxMbgPgwIfV2ICsPTNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPTNotSuppRx.setStatus("current")
_JnxMbgPgwIfV2ICsPTNotSuppTx_Type = Counter64
_JnxMbgPgwIfV2ICsPTNotSuppTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPTNotSuppTx = _JnxMbgPgwIfV2ICsPTNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 116),
    _JnxMbgPgwIfV2ICsPTNotSuppTx_Type()
)
jnxMbgPgwIfV2ICsPTNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPTNotSuppTx.setStatus("current")
_JnxMbgPgwIfV2ICsAllDynAdOccRx_Type = Counter64
_JnxMbgPgwIfV2ICsAllDynAdOccRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAllDynAdOccRx = _JnxMbgPgwIfV2ICsAllDynAdOccRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 117),
    _JnxMbgPgwIfV2ICsAllDynAdOccRx_Type()
)
jnxMbgPgwIfV2ICsAllDynAdOccRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAllDynAdOccRx.setStatus("current")
_JnxMbgPgwIfV2ICsAllDynAdOccTx_Type = Counter64
_JnxMbgPgwIfV2ICsAllDynAdOccTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAllDynAdOccTx = _JnxMbgPgwIfV2ICsAllDynAdOccTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 118),
    _JnxMbgPgwIfV2ICsAllDynAdOccTx_Type()
)
jnxMbgPgwIfV2ICsAllDynAdOccTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAllDynAdOccTx.setStatus("current")
_JnxMbgPgwIfV2ICsNOTFTUECTXRx_Type = Counter64
_JnxMbgPgwIfV2ICsNOTFTUECTXRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNOTFTUECTXRx = _JnxMbgPgwIfV2ICsNOTFTUECTXRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 119),
    _JnxMbgPgwIfV2ICsNOTFTUECTXRx_Type()
)
jnxMbgPgwIfV2ICsNOTFTUECTXRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNOTFTUECTXRx.setStatus("current")
_JnxMbgPgwIfV2ICsNOTFTUECTXTx_Type = Counter64
_JnxMbgPgwIfV2ICsNOTFTUECTXTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNOTFTUECTXTx = _JnxMbgPgwIfV2ICsNOTFTUECTXTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 120),
    _JnxMbgPgwIfV2ICsNOTFTUECTXTx_Type()
)
jnxMbgPgwIfV2ICsNOTFTUECTXTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNOTFTUECTXTx.setStatus("current")
_JnxMbgPgwIfV2ICsProtoNtSupRx_Type = Counter64
_JnxMbgPgwIfV2ICsProtoNtSupRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsProtoNtSupRx = _JnxMbgPgwIfV2ICsProtoNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 121),
    _JnxMbgPgwIfV2ICsProtoNtSupRx_Type()
)
jnxMbgPgwIfV2ICsProtoNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsProtoNtSupRx.setStatus("current")
_JnxMbgPgwIfV2ICsProtoNtSupTx_Type = Counter64
_JnxMbgPgwIfV2ICsProtoNtSupTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsProtoNtSupTx = _JnxMbgPgwIfV2ICsProtoNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 122),
    _JnxMbgPgwIfV2ICsProtoNtSupTx_Type()
)
jnxMbgPgwIfV2ICsProtoNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsProtoNtSupTx.setStatus("current")
_JnxMbgPgwIfV2ICsUENotRespRx_Type = Counter64
_JnxMbgPgwIfV2ICsUENotRespRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUENotRespRx = _JnxMbgPgwIfV2ICsUENotRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 123),
    _JnxMbgPgwIfV2ICsUENotRespRx_Type()
)
jnxMbgPgwIfV2ICsUENotRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUENotRespRx.setStatus("current")
_JnxMbgPgwIfV2ICsUENotRespTx_Type = Counter64
_JnxMbgPgwIfV2ICsUENotRespTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUENotRespTx = _JnxMbgPgwIfV2ICsUENotRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 124),
    _JnxMbgPgwIfV2ICsUENotRespTx_Type()
)
jnxMbgPgwIfV2ICsUENotRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUENotRespTx.setStatus("current")
_JnxMbgPgwIfV2ICsUERefusesRx_Type = Counter64
_JnxMbgPgwIfV2ICsUERefusesRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUERefusesRx = _JnxMbgPgwIfV2ICsUERefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 125),
    _JnxMbgPgwIfV2ICsUERefusesRx_Type()
)
jnxMbgPgwIfV2ICsUERefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUERefusesRx.setStatus("current")
_JnxMbgPgwIfV2ICsUERefusesTx_Type = Counter64
_JnxMbgPgwIfV2ICsUERefusesTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUERefusesTx = _JnxMbgPgwIfV2ICsUERefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 126),
    _JnxMbgPgwIfV2ICsUERefusesTx_Type()
)
jnxMbgPgwIfV2ICsUERefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUERefusesTx.setStatus("current")
_JnxMbgPgwIfV2ICsServDeniedRx_Type = Counter64
_JnxMbgPgwIfV2ICsServDeniedRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsServDeniedRx = _JnxMbgPgwIfV2ICsServDeniedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 127),
    _JnxMbgPgwIfV2ICsServDeniedRx_Type()
)
jnxMbgPgwIfV2ICsServDeniedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsServDeniedRx.setStatus("current")
_JnxMbgPgwIfV2ICsServDeniedTx_Type = Counter64
_JnxMbgPgwIfV2ICsServDeniedTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsServDeniedTx = _JnxMbgPgwIfV2ICsServDeniedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 128),
    _JnxMbgPgwIfV2ICsServDeniedTx_Type()
)
jnxMbgPgwIfV2ICsServDeniedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsServDeniedTx.setStatus("current")
_JnxMbgPgwIfV2ICsUnabPageUERx_Type = Counter64
_JnxMbgPgwIfV2ICsUnabPageUERx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUnabPageUERx = _JnxMbgPgwIfV2ICsUnabPageUERx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 129),
    _JnxMbgPgwIfV2ICsUnabPageUERx_Type()
)
jnxMbgPgwIfV2ICsUnabPageUERx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUnabPageUERx.setStatus("current")
_JnxMbgPgwIfV2ICsUnabPageUETx_Type = Counter64
_JnxMbgPgwIfV2ICsUnabPageUETx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUnabPageUETx = _JnxMbgPgwIfV2ICsUnabPageUETx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 130),
    _JnxMbgPgwIfV2ICsUnabPageUETx_Type()
)
jnxMbgPgwIfV2ICsUnabPageUETx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUnabPageUETx.setStatus("current")
_JnxMbgPgwIfV2ICsNoMemRx_Type = Counter64
_JnxMbgPgwIfV2ICsNoMemRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNoMemRx = _JnxMbgPgwIfV2ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 131),
    _JnxMbgPgwIfV2ICsNoMemRx_Type()
)
jnxMbgPgwIfV2ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNoMemRx.setStatus("current")
_JnxMbgPgwIfV2ICsNoMemTx_Type = Counter64
_JnxMbgPgwIfV2ICsNoMemTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsNoMemTx = _JnxMbgPgwIfV2ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 132),
    _JnxMbgPgwIfV2ICsNoMemTx_Type()
)
jnxMbgPgwIfV2ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsNoMemTx.setStatus("current")
_JnxMbgPgwIfV2ICsUserAUTHFlRx_Type = Counter64
_JnxMbgPgwIfV2ICsUserAUTHFlRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUserAUTHFlRx = _JnxMbgPgwIfV2ICsUserAUTHFlRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 133),
    _JnxMbgPgwIfV2ICsUserAUTHFlRx_Type()
)
jnxMbgPgwIfV2ICsUserAUTHFlRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUserAUTHFlRx.setStatus("current")
_JnxMbgPgwIfV2ICsUserAUTHFlTx_Type = Counter64
_JnxMbgPgwIfV2ICsUserAUTHFlTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUserAUTHFlTx = _JnxMbgPgwIfV2ICsUserAUTHFlTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 134),
    _JnxMbgPgwIfV2ICsUserAUTHFlTx_Type()
)
jnxMbgPgwIfV2ICsUserAUTHFlTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUserAUTHFlTx.setStatus("current")
_JnxMbgPgwIfV2ICsAPNAcsDenRx_Type = Counter64
_JnxMbgPgwIfV2ICsAPNAcsDenRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAPNAcsDenRx = _JnxMbgPgwIfV2ICsAPNAcsDenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 135),
    _JnxMbgPgwIfV2ICsAPNAcsDenRx_Type()
)
jnxMbgPgwIfV2ICsAPNAcsDenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAPNAcsDenRx.setStatus("current")
_JnxMbgPgwIfV2ICsAPNAcsDenTx_Type = Counter64
_JnxMbgPgwIfV2ICsAPNAcsDenTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAPNAcsDenTx = _JnxMbgPgwIfV2ICsAPNAcsDenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 136),
    _JnxMbgPgwIfV2ICsAPNAcsDenTx_Type()
)
jnxMbgPgwIfV2ICsAPNAcsDenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAPNAcsDenTx.setStatus("current")
_JnxMbgPgwIfV2ICsReqRejRx_Type = Counter64
_JnxMbgPgwIfV2ICsReqRejRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsReqRejRx = _JnxMbgPgwIfV2ICsReqRejRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 137),
    _JnxMbgPgwIfV2ICsReqRejRx_Type()
)
jnxMbgPgwIfV2ICsReqRejRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsReqRejRx.setStatus("current")
_JnxMbgPgwIfV2ICsReqRejTx_Type = Counter64
_JnxMbgPgwIfV2ICsReqRejTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsReqRejTx = _JnxMbgPgwIfV2ICsReqRejTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 138),
    _JnxMbgPgwIfV2ICsReqRejTx_Type()
)
jnxMbgPgwIfV2ICsReqRejTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsReqRejTx.setStatus("current")
_JnxMbgPgwIfV2ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwIfV2ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPTMSISigMMRx = _JnxMbgPgwIfV2ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 139),
    _JnxMbgPgwIfV2ICsPTMSISigMMRx_Type()
)
jnxMbgPgwIfV2ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwIfV2ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwIfV2ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsPTMSISigMMTx = _JnxMbgPgwIfV2ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 140),
    _JnxMbgPgwIfV2ICsPTMSISigMMTx_Type()
)
jnxMbgPgwIfV2ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwIfV2ICsIMSINotKnRx_Type = Counter64
_JnxMbgPgwIfV2ICsIMSINotKnRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsIMSINotKnRx = _JnxMbgPgwIfV2ICsIMSINotKnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 141),
    _JnxMbgPgwIfV2ICsIMSINotKnRx_Type()
)
jnxMbgPgwIfV2ICsIMSINotKnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsIMSINotKnRx.setStatus("current")
_JnxMbgPgwIfV2ICsIMSINotKnTx_Type = Counter64
_JnxMbgPgwIfV2ICsIMSINotKnTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsIMSINotKnTx = _JnxMbgPgwIfV2ICsIMSINotKnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 142),
    _JnxMbgPgwIfV2ICsIMSINotKnTx_Type()
)
jnxMbgPgwIfV2ICsIMSINotKnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsIMSINotKnTx.setStatus("current")
_JnxMbgPgwIfV2ICsCondIEMsRx_Type = Counter64
_JnxMbgPgwIfV2ICsCondIEMsRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsCondIEMsRx = _JnxMbgPgwIfV2ICsCondIEMsRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 143),
    _JnxMbgPgwIfV2ICsCondIEMsRx_Type()
)
jnxMbgPgwIfV2ICsCondIEMsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsCondIEMsRx.setStatus("current")
_JnxMbgPgwIfV2ICsCondIEMsTx_Type = Counter64
_JnxMbgPgwIfV2ICsCondIEMsTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsCondIEMsTx = _JnxMbgPgwIfV2ICsCondIEMsTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 144),
    _JnxMbgPgwIfV2ICsCondIEMsTx_Type()
)
jnxMbgPgwIfV2ICsCondIEMsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsCondIEMsTx.setStatus("current")
_JnxMbgPgwIfV2ICsAPNResTIncRx_Type = Counter64
_JnxMbgPgwIfV2ICsAPNResTIncRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAPNResTIncRx = _JnxMbgPgwIfV2ICsAPNResTIncRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 145),
    _JnxMbgPgwIfV2ICsAPNResTIncRx_Type()
)
jnxMbgPgwIfV2ICsAPNResTIncRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAPNResTIncRx.setStatus("current")
_JnxMbgPgwIfV2ICsAPNResTIncTx_Type = Counter64
_JnxMbgPgwIfV2ICsAPNResTIncTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsAPNResTIncTx = _JnxMbgPgwIfV2ICsAPNResTIncTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 146),
    _JnxMbgPgwIfV2ICsAPNResTIncTx_Type()
)
jnxMbgPgwIfV2ICsAPNResTIncTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsAPNResTIncTx.setStatus("current")
_JnxMbgPgwIfV2ICsUnknownRx_Type = Counter64
_JnxMbgPgwIfV2ICsUnknownRx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUnknownRx = _JnxMbgPgwIfV2ICsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 147),
    _JnxMbgPgwIfV2ICsUnknownRx_Type()
)
jnxMbgPgwIfV2ICsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUnknownRx.setStatus("current")
_JnxMbgPgwIfV2ICsUnknownTx_Type = Counter64
_JnxMbgPgwIfV2ICsUnknownTx_Object = MibTableColumn
jnxMbgPgwIfV2ICsUnknownTx = _JnxMbgPgwIfV2ICsUnknownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 148),
    _JnxMbgPgwIfV2ICsUnknownTx_Type()
)
jnxMbgPgwIfV2ICsUnknownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ICsUnknownTx.setStatus("current")
_JnxMbgPgwIfV1ProtocolErrRx_Type = Counter64
_JnxMbgPgwIfV1ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwIfV1ProtocolErrRx = _JnxMbgPgwIfV1ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 149),
    _JnxMbgPgwIfV1ProtocolErrRx_Type()
)
jnxMbgPgwIfV1ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ProtocolErrRx.setStatus("current")
_JnxMbgPgwIfV1UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwIfV1UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwIfV1UnSupportedMsgRx = _JnxMbgPgwIfV1UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 150),
    _JnxMbgPgwIfV1UnSupportedMsgRx_Type()
)
jnxMbgPgwIfV1UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwIfV1T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwIfV1T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwIfV1T3RespTmrExpRx = _JnxMbgPgwIfV1T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 151),
    _JnxMbgPgwIfV1T3RespTmrExpRx_Type()
)
jnxMbgPgwIfV1T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwIfV1GlbNumMsgRx_Type = Counter64
_JnxMbgPgwIfV1GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwIfV1GlbNumMsgRx = _JnxMbgPgwIfV1GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 152),
    _JnxMbgPgwIfV1GlbNumMsgRx_Type()
)
jnxMbgPgwIfV1GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbNumMsgRx.setStatus("current")
_JnxMbgPgwIfV1GlbNumMsgTx_Type = Counter64
_JnxMbgPgwIfV1GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwIfV1GlbNumMsgTx = _JnxMbgPgwIfV1GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 153),
    _JnxMbgPgwIfV1GlbNumMsgTx_Type()
)
jnxMbgPgwIfV1GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbNumMsgTx.setStatus("current")
_JnxMbgPgwIfV1GlbNumBytesRx_Type = Counter64
_JnxMbgPgwIfV1GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwIfV1GlbNumBytesRx = _JnxMbgPgwIfV1GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 154),
    _JnxMbgPgwIfV1GlbNumBytesRx_Type()
)
jnxMbgPgwIfV1GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbNumBytesRx.setStatus("current")
_JnxMbgPgwIfV1GlbNumBytesTx_Type = Counter64
_JnxMbgPgwIfV1GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwIfV1GlbNumBytesTx = _JnxMbgPgwIfV1GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 155),
    _JnxMbgPgwIfV1GlbNumBytesTx_Type()
)
jnxMbgPgwIfV1GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbNumBytesTx.setStatus("current")
_JnxMbgPgwIfV1GlbEchoReqRx_Type = Counter64
_JnxMbgPgwIfV1GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwIfV1GlbEchoReqRx = _JnxMbgPgwIfV1GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 156),
    _JnxMbgPgwIfV1GlbEchoReqRx_Type()
)
jnxMbgPgwIfV1GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbEchoReqRx.setStatus("current")
_JnxMbgPgwIfV1GlbEchoReqTx_Type = Counter64
_JnxMbgPgwIfV1GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwIfV1GlbEchoReqTx = _JnxMbgPgwIfV1GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 157),
    _JnxMbgPgwIfV1GlbEchoReqTx_Type()
)
jnxMbgPgwIfV1GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbEchoReqTx.setStatus("current")
_JnxMbgPgwIfV1GlbEchoRespRx_Type = Counter64
_JnxMbgPgwIfV1GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwIfV1GlbEchoRespRx = _JnxMbgPgwIfV1GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 158),
    _JnxMbgPgwIfV1GlbEchoRespRx_Type()
)
jnxMbgPgwIfV1GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbEchoRespRx.setStatus("current")
_JnxMbgPgwIfV1GlbEchoRespTx_Type = Counter64
_JnxMbgPgwIfV1GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwIfV1GlbEchoRespTx = _JnxMbgPgwIfV1GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 159),
    _JnxMbgPgwIfV1GlbEchoRespTx_Type()
)
jnxMbgPgwIfV1GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1GlbEchoRespTx.setStatus("current")
_JnxMbgPgwIfV1VerNotSupRx_Type = Counter64
_JnxMbgPgwIfV1VerNotSupRx_Object = MibTableColumn
jnxMbgPgwIfV1VerNotSupRx = _JnxMbgPgwIfV1VerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 160),
    _JnxMbgPgwIfV1VerNotSupRx_Type()
)
jnxMbgPgwIfV1VerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1VerNotSupRx.setStatus("current")
_JnxMbgPgwIfV1VerNotSupTx_Type = Counter64
_JnxMbgPgwIfV1VerNotSupTx_Object = MibTableColumn
jnxMbgPgwIfV1VerNotSupTx = _JnxMbgPgwIfV1VerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 161),
    _JnxMbgPgwIfV1VerNotSupTx_Type()
)
jnxMbgPgwIfV1VerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1VerNotSupTx.setStatus("current")
_JnxMbgPgwIfV1CrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV1CrtPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV1CrtPdpCxtReqRx = _JnxMbgPgwIfV1CrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 162),
    _JnxMbgPgwIfV1CrtPdpCxtReqRx_Type()
)
jnxMbgPgwIfV1CrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV1CrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV1CrtPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV1CrtPdpCxtReqTx = _JnxMbgPgwIfV1CrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 163),
    _JnxMbgPgwIfV1CrtPdpCxtReqTx_Type()
)
jnxMbgPgwIfV1CrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV1CrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV1CrtPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV1CrtPdpCxtRspRx = _JnxMbgPgwIfV1CrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 164),
    _JnxMbgPgwIfV1CrtPdpCxtRspRx_Type()
)
jnxMbgPgwIfV1CrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV1CrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV1CrtPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV1CrtPdpCxtRspTx = _JnxMbgPgwIfV1CrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 165),
    _JnxMbgPgwIfV1CrtPdpCxtRspTx_Type()
)
jnxMbgPgwIfV1CrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV1UpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV1UpdPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV1UpdPdpCxtReqRx = _JnxMbgPgwIfV1UpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 166),
    _JnxMbgPgwIfV1UpdPdpCxtReqRx_Type()
)
jnxMbgPgwIfV1UpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1UpdPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV1UpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV1UpdPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV1UpdPdpCxtReqTx = _JnxMbgPgwIfV1UpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 167),
    _JnxMbgPgwIfV1UpdPdpCxtReqTx_Type()
)
jnxMbgPgwIfV1UpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1UpdPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV1UpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV1UpdPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV1UpdPdpCxtRspRx = _JnxMbgPgwIfV1UpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 168),
    _JnxMbgPgwIfV1UpdPdpCxtRspRx_Type()
)
jnxMbgPgwIfV1UpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1UpdPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV1UpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV1UpdPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV1UpdPdpCxtRspTx = _JnxMbgPgwIfV1UpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 169),
    _JnxMbgPgwIfV1UpdPdpCxtRspTx_Type()
)
jnxMbgPgwIfV1UpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1UpdPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV1DelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV1DelPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV1DelPdpCxtReqRx = _JnxMbgPgwIfV1DelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 170),
    _JnxMbgPgwIfV1DelPdpCxtReqRx_Type()
)
jnxMbgPgwIfV1DelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV1DelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV1DelPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV1DelPdpCxtReqTx = _JnxMbgPgwIfV1DelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 171),
    _JnxMbgPgwIfV1DelPdpCxtReqTx_Type()
)
jnxMbgPgwIfV1DelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV1DelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV1DelPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV1DelPdpCxtRspRx = _JnxMbgPgwIfV1DelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 172),
    _JnxMbgPgwIfV1DelPdpCxtRspRx_Type()
)
jnxMbgPgwIfV1DelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV1DelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV1DelPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV1DelPdpCxtRspTx = _JnxMbgPgwIfV1DelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 173),
    _JnxMbgPgwIfV1DelPdpCxtRspTx_Type()
)
jnxMbgPgwIfV1DelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV1CrtAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV1CrtAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV1CrtAAPdpCxtReqRx = _JnxMbgPgwIfV1CrtAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 174),
    _JnxMbgPgwIfV1CrtAAPdpCxtReqRx_Type()
)
jnxMbgPgwIfV1CrtAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV1CrtAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV1CrtAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV1CrtAAPdpCxtReqTx = _JnxMbgPgwIfV1CrtAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 175),
    _JnxMbgPgwIfV1CrtAAPdpCxtReqTx_Type()
)
jnxMbgPgwIfV1CrtAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV1CrtAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV1CrtAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV1CrtAAPdpCxtRspRx = _JnxMbgPgwIfV1CrtAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 176),
    _JnxMbgPgwIfV1CrtAAPdpCxtRspRx_Type()
)
jnxMbgPgwIfV1CrtAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV1CrtAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV1CrtAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV1CrtAAPdpCxtRspTx = _JnxMbgPgwIfV1CrtAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 177),
    _JnxMbgPgwIfV1CrtAAPdpCxtRspTx_Type()
)
jnxMbgPgwIfV1CrtAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1CrtAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV1DelAAPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV1DelAAPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV1DelAAPdpCxtReqRx = _JnxMbgPgwIfV1DelAAPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 178),
    _JnxMbgPgwIfV1DelAAPdpCxtReqRx_Type()
)
jnxMbgPgwIfV1DelAAPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelAAPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV1DelAAPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV1DelAAPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV1DelAAPdpCxtReqTx = _JnxMbgPgwIfV1DelAAPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 179),
    _JnxMbgPgwIfV1DelAAPdpCxtReqTx_Type()
)
jnxMbgPgwIfV1DelAAPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelAAPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV1DelAAPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV1DelAAPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV1DelAAPdpCxtRspRx = _JnxMbgPgwIfV1DelAAPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 180),
    _JnxMbgPgwIfV1DelAAPdpCxtRspRx_Type()
)
jnxMbgPgwIfV1DelAAPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelAAPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV1DelAAPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV1DelAAPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV1DelAAPdpCxtRspTx = _JnxMbgPgwIfV1DelAAPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 181),
    _JnxMbgPgwIfV1DelAAPdpCxtRspTx_Type()
)
jnxMbgPgwIfV1DelAAPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1DelAAPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV1ErrorIndRx_Type = Counter64
_JnxMbgPgwIfV1ErrorIndRx_Object = MibTableColumn
jnxMbgPgwIfV1ErrorIndRx = _JnxMbgPgwIfV1ErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 182),
    _JnxMbgPgwIfV1ErrorIndRx_Type()
)
jnxMbgPgwIfV1ErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ErrorIndRx.setStatus("current")
_JnxMbgPgwIfV1ErrorIndTx_Type = Counter64
_JnxMbgPgwIfV1ErrorIndTx_Object = MibTableColumn
jnxMbgPgwIfV1ErrorIndTx = _JnxMbgPgwIfV1ErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 183),
    _JnxMbgPgwIfV1ErrorIndTx_Type()
)
jnxMbgPgwIfV1ErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ErrorIndTx.setStatus("current")
_JnxMbgPgwIfV1NotifReqRx_Type = Counter64
_JnxMbgPgwIfV1NotifReqRx_Object = MibTableColumn
jnxMbgPgwIfV1NotifReqRx = _JnxMbgPgwIfV1NotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 184),
    _JnxMbgPgwIfV1NotifReqRx_Type()
)
jnxMbgPgwIfV1NotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifReqRx.setStatus("current")
_JnxMbgPgwIfV1NotifReqTx_Type = Counter64
_JnxMbgPgwIfV1NotifReqTx_Object = MibTableColumn
jnxMbgPgwIfV1NotifReqTx = _JnxMbgPgwIfV1NotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 185),
    _JnxMbgPgwIfV1NotifReqTx_Type()
)
jnxMbgPgwIfV1NotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifReqTx.setStatus("current")
_JnxMbgPgwIfV1NotifRspRx_Type = Counter64
_JnxMbgPgwIfV1NotifRspRx_Object = MibTableColumn
jnxMbgPgwIfV1NotifRspRx = _JnxMbgPgwIfV1NotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 186),
    _JnxMbgPgwIfV1NotifRspRx_Type()
)
jnxMbgPgwIfV1NotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifRspRx.setStatus("current")
_JnxMbgPgwIfV1NotifRspTx_Type = Counter64
_JnxMbgPgwIfV1NotifRspTx_Object = MibTableColumn
jnxMbgPgwIfV1NotifRspTx = _JnxMbgPgwIfV1NotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 187),
    _JnxMbgPgwIfV1NotifRspTx_Type()
)
jnxMbgPgwIfV1NotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifRspTx.setStatus("current")
_JnxMbgPgwIfV1NotifRejReqRx_Type = Counter64
_JnxMbgPgwIfV1NotifRejReqRx_Object = MibTableColumn
jnxMbgPgwIfV1NotifRejReqRx = _JnxMbgPgwIfV1NotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 188),
    _JnxMbgPgwIfV1NotifRejReqRx_Type()
)
jnxMbgPgwIfV1NotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifRejReqRx.setStatus("current")
_JnxMbgPgwIfV1NotifRejReqTx_Type = Counter64
_JnxMbgPgwIfV1NotifRejReqTx_Object = MibTableColumn
jnxMbgPgwIfV1NotifRejReqTx = _JnxMbgPgwIfV1NotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 189),
    _JnxMbgPgwIfV1NotifRejReqTx_Type()
)
jnxMbgPgwIfV1NotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifRejReqTx.setStatus("current")
_JnxMbgPgwIfV1NotifRejRspRx_Type = Counter64
_JnxMbgPgwIfV1NotifRejRspRx_Object = MibTableColumn
jnxMbgPgwIfV1NotifRejRspRx = _JnxMbgPgwIfV1NotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 190),
    _JnxMbgPgwIfV1NotifRejRspRx_Type()
)
jnxMbgPgwIfV1NotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifRejRspRx.setStatus("current")
_JnxMbgPgwIfV1NotifRejRspTx_Type = Counter64
_JnxMbgPgwIfV1NotifRejRspTx_Object = MibTableColumn
jnxMbgPgwIfV1NotifRejRspTx = _JnxMbgPgwIfV1NotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 191),
    _JnxMbgPgwIfV1NotifRejRspTx_Type()
)
jnxMbgPgwIfV1NotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotifRejRspTx.setStatus("current")
_JnxMbgPgwIfV1RtInfReqRx_Type = Counter64
_JnxMbgPgwIfV1RtInfReqRx_Object = MibTableColumn
jnxMbgPgwIfV1RtInfReqRx = _JnxMbgPgwIfV1RtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 192),
    _JnxMbgPgwIfV1RtInfReqRx_Type()
)
jnxMbgPgwIfV1RtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1RtInfReqRx.setStatus("current")
_JnxMbgPgwIfV1RtInfReqTx_Type = Counter64
_JnxMbgPgwIfV1RtInfReqTx_Object = MibTableColumn
jnxMbgPgwIfV1RtInfReqTx = _JnxMbgPgwIfV1RtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 193),
    _JnxMbgPgwIfV1RtInfReqTx_Type()
)
jnxMbgPgwIfV1RtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1RtInfReqTx.setStatus("current")
_JnxMbgPgwIfV1RtInfRspRx_Type = Counter64
_JnxMbgPgwIfV1RtInfRspRx_Object = MibTableColumn
jnxMbgPgwIfV1RtInfRspRx = _JnxMbgPgwIfV1RtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 194),
    _JnxMbgPgwIfV1RtInfRspRx_Type()
)
jnxMbgPgwIfV1RtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1RtInfRspRx.setStatus("current")
_JnxMbgPgwIfV1RtInfRspTx_Type = Counter64
_JnxMbgPgwIfV1RtInfRspTx_Object = MibTableColumn
jnxMbgPgwIfV1RtInfRspTx = _JnxMbgPgwIfV1RtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 195),
    _JnxMbgPgwIfV1RtInfRspTx_Type()
)
jnxMbgPgwIfV1RtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1RtInfRspTx.setStatus("current")
_JnxMbgPgwIfV1FailRptReqRx_Type = Counter64
_JnxMbgPgwIfV1FailRptReqRx_Object = MibTableColumn
jnxMbgPgwIfV1FailRptReqRx = _JnxMbgPgwIfV1FailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 196),
    _JnxMbgPgwIfV1FailRptReqRx_Type()
)
jnxMbgPgwIfV1FailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1FailRptReqRx.setStatus("current")
_JnxMbgPgwIfV1FailRptReqTx_Type = Counter64
_JnxMbgPgwIfV1FailRptReqTx_Object = MibTableColumn
jnxMbgPgwIfV1FailRptReqTx = _JnxMbgPgwIfV1FailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 197),
    _JnxMbgPgwIfV1FailRptReqTx_Type()
)
jnxMbgPgwIfV1FailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1FailRptReqTx.setStatus("current")
_JnxMbgPgwIfV1FailRptRspRx_Type = Counter64
_JnxMbgPgwIfV1FailRptRspRx_Object = MibTableColumn
jnxMbgPgwIfV1FailRptRspRx = _JnxMbgPgwIfV1FailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 198),
    _JnxMbgPgwIfV1FailRptRspRx_Type()
)
jnxMbgPgwIfV1FailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1FailRptRspRx.setStatus("current")
_JnxMbgPgwIfV1FailRptRspTx_Type = Counter64
_JnxMbgPgwIfV1FailRptRspTx_Object = MibTableColumn
jnxMbgPgwIfV1FailRptRspTx = _JnxMbgPgwIfV1FailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 199),
    _JnxMbgPgwIfV1FailRptRspTx_Type()
)
jnxMbgPgwIfV1FailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1FailRptRspTx.setStatus("current")
_JnxMbgPgwIfV1NotMSPresReqRx_Type = Counter64
_JnxMbgPgwIfV1NotMSPresReqRx_Object = MibTableColumn
jnxMbgPgwIfV1NotMSPresReqRx = _JnxMbgPgwIfV1NotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 200),
    _JnxMbgPgwIfV1NotMSPresReqRx_Type()
)
jnxMbgPgwIfV1NotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotMSPresReqRx.setStatus("current")
_JnxMbgPgwIfV1NotMSPresReqTx_Type = Counter64
_JnxMbgPgwIfV1NotMSPresReqTx_Object = MibTableColumn
jnxMbgPgwIfV1NotMSPresReqTx = _JnxMbgPgwIfV1NotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 201),
    _JnxMbgPgwIfV1NotMSPresReqTx_Type()
)
jnxMbgPgwIfV1NotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotMSPresReqTx.setStatus("current")
_JnxMbgPgwIfV1NotMSPresRspRx_Type = Counter64
_JnxMbgPgwIfV1NotMSPresRspRx_Object = MibTableColumn
jnxMbgPgwIfV1NotMSPresRspRx = _JnxMbgPgwIfV1NotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 202),
    _JnxMbgPgwIfV1NotMSPresRspRx_Type()
)
jnxMbgPgwIfV1NotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotMSPresRspRx.setStatus("current")
_JnxMbgPgwIfV1NotMSPresRspTx_Type = Counter64
_JnxMbgPgwIfV1NotMSPresRspTx_Object = MibTableColumn
jnxMbgPgwIfV1NotMSPresRspTx = _JnxMbgPgwIfV1NotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 203),
    _JnxMbgPgwIfV1NotMSPresRspTx_Type()
)
jnxMbgPgwIfV1NotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1NotMSPresRspTx.setStatus("current")
_JnxMbgPgwIfV1ICsReqAcceptedRx_Type = Counter64
_JnxMbgPgwIfV1ICsReqAcceptedRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsReqAcceptedRx = _JnxMbgPgwIfV1ICsReqAcceptedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 204),
    _JnxMbgPgwIfV1ICsReqAcceptedRx_Type()
)
jnxMbgPgwIfV1ICsReqAcceptedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsReqAcceptedRx.setStatus("current")
_JnxMbgPgwIfV1ICsReqAcceptedTx_Type = Counter64
_JnxMbgPgwIfV1ICsReqAcceptedTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsReqAcceptedTx = _JnxMbgPgwIfV1ICsReqAcceptedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 205),
    _JnxMbgPgwIfV1ICsReqAcceptedTx_Type()
)
jnxMbgPgwIfV1ICsReqAcceptedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsReqAcceptedTx.setStatus("current")
_JnxMbgPgwIfV1ICsNonExistRx_Type = Counter64
_JnxMbgPgwIfV1ICsNonExistRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNonExistRx = _JnxMbgPgwIfV1ICsNonExistRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 206),
    _JnxMbgPgwIfV1ICsNonExistRx_Type()
)
jnxMbgPgwIfV1ICsNonExistRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNonExistRx.setStatus("current")
_JnxMbgPgwIfV1ICsNonExistTx_Type = Counter64
_JnxMbgPgwIfV1ICsNonExistTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNonExistTx = _JnxMbgPgwIfV1ICsNonExistTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 207),
    _JnxMbgPgwIfV1ICsNonExistTx_Type()
)
jnxMbgPgwIfV1ICsNonExistTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNonExistTx.setStatus("current")
_JnxMbgPgwIfV1ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwIfV1ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsInvMsgFmtRx = _JnxMbgPgwIfV1ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 208),
    _JnxMbgPgwIfV1ICsInvMsgFmtRx_Type()
)
jnxMbgPgwIfV1ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwIfV1ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwIfV1ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsInvMsgFmtTx = _JnxMbgPgwIfV1ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 209),
    _JnxMbgPgwIfV1ICsInvMsgFmtTx_Type()
)
jnxMbgPgwIfV1ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwIfV1ICsIMSINotKnownRx_Type = Counter64
_JnxMbgPgwIfV1ICsIMSINotKnownRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsIMSINotKnownRx = _JnxMbgPgwIfV1ICsIMSINotKnownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 210),
    _JnxMbgPgwIfV1ICsIMSINotKnownRx_Type()
)
jnxMbgPgwIfV1ICsIMSINotKnownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsIMSINotKnownRx.setStatus("current")
_JnxMbgPgwIfV1ICsIMSINotKnownTx_Type = Counter64
_JnxMbgPgwIfV1ICsIMSINotKnownTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsIMSINotKnownTx = _JnxMbgPgwIfV1ICsIMSINotKnownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 211),
    _JnxMbgPgwIfV1ICsIMSINotKnownTx_Type()
)
jnxMbgPgwIfV1ICsIMSINotKnownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsIMSINotKnownTx.setStatus("current")
_JnxMbgPgwIfV1ICsMSGRPSDetachRx_Type = Counter64
_JnxMbgPgwIfV1ICsMSGRPSDetachRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMSGRPSDetachRx = _JnxMbgPgwIfV1ICsMSGRPSDetachRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 212),
    _JnxMbgPgwIfV1ICsMSGRPSDetachRx_Type()
)
jnxMbgPgwIfV1ICsMSGRPSDetachRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMSGRPSDetachRx.setStatus("current")
_JnxMbgPgwIfV1ICsMSGRPSDetachTx_Type = Counter64
_JnxMbgPgwIfV1ICsMSGRPSDetachTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMSGRPSDetachTx = _JnxMbgPgwIfV1ICsMSGRPSDetachTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 213),
    _JnxMbgPgwIfV1ICsMSGRPSDetachTx_Type()
)
jnxMbgPgwIfV1ICsMSGRPSDetachTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMSGRPSDetachTx.setStatus("current")
_JnxMbgPgwIfV1ICsMSNotGRPSRespRx_Type = Counter64
_JnxMbgPgwIfV1ICsMSNotGRPSRespRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMSNotGRPSRespRx = _JnxMbgPgwIfV1ICsMSNotGRPSRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 214),
    _JnxMbgPgwIfV1ICsMSNotGRPSRespRx_Type()
)
jnxMbgPgwIfV1ICsMSNotGRPSRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMSNotGRPSRespRx.setStatus("current")
_JnxMbgPgwIfV1ICsMSNotGRPSRespTx_Type = Counter64
_JnxMbgPgwIfV1ICsMSNotGRPSRespTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMSNotGRPSRespTx = _JnxMbgPgwIfV1ICsMSNotGRPSRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 215),
    _JnxMbgPgwIfV1ICsMSNotGRPSRespTx_Type()
)
jnxMbgPgwIfV1ICsMSNotGRPSRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMSNotGRPSRespTx.setStatus("current")
_JnxMbgPgwIfV1ICsMSRefusesRx_Type = Counter64
_JnxMbgPgwIfV1ICsMSRefusesRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMSRefusesRx = _JnxMbgPgwIfV1ICsMSRefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 216),
    _JnxMbgPgwIfV1ICsMSRefusesRx_Type()
)
jnxMbgPgwIfV1ICsMSRefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMSRefusesRx.setStatus("current")
_JnxMbgPgwIfV1ICsMSRefusesTx_Type = Counter64
_JnxMbgPgwIfV1ICsMSRefusesTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMSRefusesTx = _JnxMbgPgwIfV1ICsMSRefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 217),
    _JnxMbgPgwIfV1ICsMSRefusesTx_Type()
)
jnxMbgPgwIfV1ICsMSRefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMSRefusesTx.setStatus("current")
_JnxMbgPgwIfV1ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwIfV1ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsVerNotSuppRx = _JnxMbgPgwIfV1ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 218),
    _JnxMbgPgwIfV1ICsVerNotSuppRx_Type()
)
jnxMbgPgwIfV1ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwIfV1ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwIfV1ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsVerNotSuppTx = _JnxMbgPgwIfV1ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 219),
    _JnxMbgPgwIfV1ICsVerNotSuppTx_Type()
)
jnxMbgPgwIfV1ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwIfV1ICsNoResRx_Type = Counter64
_JnxMbgPgwIfV1ICsNoResRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNoResRx = _JnxMbgPgwIfV1ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 220),
    _JnxMbgPgwIfV1ICsNoResRx_Type()
)
jnxMbgPgwIfV1ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNoResRx.setStatus("current")
_JnxMbgPgwIfV1ICsNoResTx_Type = Counter64
_JnxMbgPgwIfV1ICsNoResTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNoResTx = _JnxMbgPgwIfV1ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 221),
    _JnxMbgPgwIfV1ICsNoResTx_Type()
)
jnxMbgPgwIfV1ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNoResTx.setStatus("current")
_JnxMbgPgwIfV1ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwIfV1ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsServNotSuppRx = _JnxMbgPgwIfV1ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 222),
    _JnxMbgPgwIfV1ICsServNotSuppRx_Type()
)
jnxMbgPgwIfV1ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwIfV1ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwIfV1ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsServNotSuppTx = _JnxMbgPgwIfV1ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 223),
    _JnxMbgPgwIfV1ICsServNotSuppTx_Type()
)
jnxMbgPgwIfV1ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwIfV1ICsManIEIncrtRx_Type = Counter64
_JnxMbgPgwIfV1ICsManIEIncrtRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsManIEIncrtRx = _JnxMbgPgwIfV1ICsManIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 224),
    _JnxMbgPgwIfV1ICsManIEIncrtRx_Type()
)
jnxMbgPgwIfV1ICsManIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsManIEIncrtRx.setStatus("current")
_JnxMbgPgwIfV1ICsManIEIncrtTx_Type = Counter64
_JnxMbgPgwIfV1ICsManIEIncrtTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsManIEIncrtTx = _JnxMbgPgwIfV1ICsManIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 225),
    _JnxMbgPgwIfV1ICsManIEIncrtTx_Type()
)
jnxMbgPgwIfV1ICsManIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsManIEIncrtTx.setStatus("current")
_JnxMbgPgwIfV1ICsManIEMissRx_Type = Counter64
_JnxMbgPgwIfV1ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsManIEMissRx = _JnxMbgPgwIfV1ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 226),
    _JnxMbgPgwIfV1ICsManIEMissRx_Type()
)
jnxMbgPgwIfV1ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsManIEMissRx.setStatus("current")
_JnxMbgPgwIfV1ICsManIEMissTx_Type = Counter64
_JnxMbgPgwIfV1ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsManIEMissTx = _JnxMbgPgwIfV1ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 227),
    _JnxMbgPgwIfV1ICsManIEMissTx_Type()
)
jnxMbgPgwIfV1ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsManIEMissTx.setStatus("current")
_JnxMbgPgwIfV1ICsOptIEIncrtRx_Type = Counter64
_JnxMbgPgwIfV1ICsOptIEIncrtRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsOptIEIncrtRx = _JnxMbgPgwIfV1ICsOptIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 228),
    _JnxMbgPgwIfV1ICsOptIEIncrtRx_Type()
)
jnxMbgPgwIfV1ICsOptIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsOptIEIncrtRx.setStatus("current")
_JnxMbgPgwIfV1ICsOptIEIncrtTx_Type = Counter64
_JnxMbgPgwIfV1ICsOptIEIncrtTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsOptIEIncrtTx = _JnxMbgPgwIfV1ICsOptIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 229),
    _JnxMbgPgwIfV1ICsOptIEIncrtTx_Type()
)
jnxMbgPgwIfV1ICsOptIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsOptIEIncrtTx.setStatus("current")
_JnxMbgPgwIfV1ICsSysFailRx_Type = Counter64
_JnxMbgPgwIfV1ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSysFailRx = _JnxMbgPgwIfV1ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 230),
    _JnxMbgPgwIfV1ICsSysFailRx_Type()
)
jnxMbgPgwIfV1ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSysFailRx.setStatus("current")
_JnxMbgPgwIfV1ICsSysFailTx_Type = Counter64
_JnxMbgPgwIfV1ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSysFailTx = _JnxMbgPgwIfV1ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 231),
    _JnxMbgPgwIfV1ICsSysFailTx_Type()
)
jnxMbgPgwIfV1ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSysFailTx.setStatus("current")
_JnxMbgPgwIfV1ICsRoamRestrictRx_Type = Counter64
_JnxMbgPgwIfV1ICsRoamRestrictRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsRoamRestrictRx = _JnxMbgPgwIfV1ICsRoamRestrictRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 232),
    _JnxMbgPgwIfV1ICsRoamRestrictRx_Type()
)
jnxMbgPgwIfV1ICsRoamRestrictRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsRoamRestrictRx.setStatus("current")
_JnxMbgPgwIfV1ICsRoamRestrictTx_Type = Counter64
_JnxMbgPgwIfV1ICsRoamRestrictTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsRoamRestrictTx = _JnxMbgPgwIfV1ICsRoamRestrictTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 233),
    _JnxMbgPgwIfV1ICsRoamRestrictTx_Type()
)
jnxMbgPgwIfV1ICsRoamRestrictTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsRoamRestrictTx.setStatus("current")
_JnxMbgPgwIfV1ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwIfV1ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsPTMSISigMMRx = _JnxMbgPgwIfV1ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 234),
    _JnxMbgPgwIfV1ICsPTMSISigMMRx_Type()
)
jnxMbgPgwIfV1ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwIfV1ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwIfV1ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsPTMSISigMMTx = _JnxMbgPgwIfV1ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 235),
    _JnxMbgPgwIfV1ICsPTMSISigMMTx_Type()
)
jnxMbgPgwIfV1ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwIfV1ICsGPRSConnSuppRx_Type = Counter64
_JnxMbgPgwIfV1ICsGPRSConnSuppRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsGPRSConnSuppRx = _JnxMbgPgwIfV1ICsGPRSConnSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 236),
    _JnxMbgPgwIfV1ICsGPRSConnSuppRx_Type()
)
jnxMbgPgwIfV1ICsGPRSConnSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsGPRSConnSuppRx.setStatus("current")
_JnxMbgPgwIfV1ICsGPRSConnSuppTx_Type = Counter64
_JnxMbgPgwIfV1ICsGPRSConnSuppTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsGPRSConnSuppTx = _JnxMbgPgwIfV1ICsGPRSConnSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 237),
    _JnxMbgPgwIfV1ICsGPRSConnSuppTx_Type()
)
jnxMbgPgwIfV1ICsGPRSConnSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsGPRSConnSuppTx.setStatus("current")
_JnxMbgPgwIfV1ICsAuthFailRx_Type = Counter64
_JnxMbgPgwIfV1ICsAuthFailRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsAuthFailRx = _JnxMbgPgwIfV1ICsAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 238),
    _JnxMbgPgwIfV1ICsAuthFailRx_Type()
)
jnxMbgPgwIfV1ICsAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsAuthFailRx.setStatus("current")
_JnxMbgPgwIfV1ICsAuthFailTx_Type = Counter64
_JnxMbgPgwIfV1ICsAuthFailTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsAuthFailTx = _JnxMbgPgwIfV1ICsAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 239),
    _JnxMbgPgwIfV1ICsAuthFailTx_Type()
)
jnxMbgPgwIfV1ICsAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsAuthFailTx.setStatus("current")
_JnxMbgPgwIfV1ICsUserAuthFailRx_Type = Counter64
_JnxMbgPgwIfV1ICsUserAuthFailRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsUserAuthFailRx = _JnxMbgPgwIfV1ICsUserAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 240),
    _JnxMbgPgwIfV1ICsUserAuthFailRx_Type()
)
jnxMbgPgwIfV1ICsUserAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsUserAuthFailRx.setStatus("current")
_JnxMbgPgwIfV1ICsUserAuthFailTx_Type = Counter64
_JnxMbgPgwIfV1ICsUserAuthFailTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsUserAuthFailTx = _JnxMbgPgwIfV1ICsUserAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 241),
    _JnxMbgPgwIfV1ICsUserAuthFailTx_Type()
)
jnxMbgPgwIfV1ICsUserAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsUserAuthFailTx.setStatus("current")
_JnxMbgPgwIfV1ICsCtxNotFndRx_Type = Counter64
_JnxMbgPgwIfV1ICsCtxNotFndRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsCtxNotFndRx = _JnxMbgPgwIfV1ICsCtxNotFndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 242),
    _JnxMbgPgwIfV1ICsCtxNotFndRx_Type()
)
jnxMbgPgwIfV1ICsCtxNotFndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsCtxNotFndRx.setStatus("current")
_JnxMbgPgwIfV1ICsCtxNotFndTx_Type = Counter64
_JnxMbgPgwIfV1ICsCtxNotFndTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsCtxNotFndTx = _JnxMbgPgwIfV1ICsCtxNotFndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 243),
    _JnxMbgPgwIfV1ICsCtxNotFndTx_Type()
)
jnxMbgPgwIfV1ICsCtxNotFndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsCtxNotFndTx.setStatus("current")
_JnxMbgPgwIfV1ICsAllDynPDPAdRx_Type = Counter64
_JnxMbgPgwIfV1ICsAllDynPDPAdRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsAllDynPDPAdRx = _JnxMbgPgwIfV1ICsAllDynPDPAdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 244),
    _JnxMbgPgwIfV1ICsAllDynPDPAdRx_Type()
)
jnxMbgPgwIfV1ICsAllDynPDPAdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsAllDynPDPAdRx.setStatus("current")
_JnxMbgPgwIfV1ICsAllDynPDPAdTx_Type = Counter64
_JnxMbgPgwIfV1ICsAllDynPDPAdTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsAllDynPDPAdTx = _JnxMbgPgwIfV1ICsAllDynPDPAdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 245),
    _JnxMbgPgwIfV1ICsAllDynPDPAdTx_Type()
)
jnxMbgPgwIfV1ICsAllDynPDPAdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsAllDynPDPAdTx.setStatus("current")
_JnxMbgPgwIfV1ICsNoMemRx_Type = Counter64
_JnxMbgPgwIfV1ICsNoMemRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNoMemRx = _JnxMbgPgwIfV1ICsNoMemRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 246),
    _JnxMbgPgwIfV1ICsNoMemRx_Type()
)
jnxMbgPgwIfV1ICsNoMemRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNoMemRx.setStatus("current")
_JnxMbgPgwIfV1ICsNoMemTx_Type = Counter64
_JnxMbgPgwIfV1ICsNoMemTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNoMemTx = _JnxMbgPgwIfV1ICsNoMemTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 247),
    _JnxMbgPgwIfV1ICsNoMemTx_Type()
)
jnxMbgPgwIfV1ICsNoMemTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNoMemTx.setStatus("current")
_JnxMbgPgwIfV1ICsRelocFailRx_Type = Counter64
_JnxMbgPgwIfV1ICsRelocFailRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsRelocFailRx = _JnxMbgPgwIfV1ICsRelocFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 248),
    _JnxMbgPgwIfV1ICsRelocFailRx_Type()
)
jnxMbgPgwIfV1ICsRelocFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsRelocFailRx.setStatus("current")
_JnxMbgPgwIfV1ICsRelocFailTx_Type = Counter64
_JnxMbgPgwIfV1ICsRelocFailTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsRelocFailTx = _JnxMbgPgwIfV1ICsRelocFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 249),
    _JnxMbgPgwIfV1ICsRelocFailTx_Type()
)
jnxMbgPgwIfV1ICsRelocFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsRelocFailTx.setStatus("current")
_JnxMbgPgwIfV1ICsUnkManExhdrRx_Type = Counter64
_JnxMbgPgwIfV1ICsUnkManExhdrRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsUnkManExhdrRx = _JnxMbgPgwIfV1ICsUnkManExhdrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 250),
    _JnxMbgPgwIfV1ICsUnkManExhdrRx_Type()
)
jnxMbgPgwIfV1ICsUnkManExhdrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsUnkManExhdrRx.setStatus("current")
_JnxMbgPgwIfV1ICsUnkManExhdrTx_Type = Counter64
_JnxMbgPgwIfV1ICsUnkManExhdrTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsUnkManExhdrTx = _JnxMbgPgwIfV1ICsUnkManExhdrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 251),
    _JnxMbgPgwIfV1ICsUnkManExhdrTx_Type()
)
jnxMbgPgwIfV1ICsUnkManExhdrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsUnkManExhdrTx.setStatus("current")
_JnxMbgPgwIfV1ICsSMANTTFTEr1Rx_Type = Counter64
_JnxMbgPgwIfV1ICsSMANTTFTEr1Rx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSMANTTFTEr1Rx = _JnxMbgPgwIfV1ICsSMANTTFTEr1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 252),
    _JnxMbgPgwIfV1ICsSMANTTFTEr1Rx_Type()
)
jnxMbgPgwIfV1ICsSMANTTFTEr1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSMANTTFTEr1Rx.setStatus("current")
_JnxMbgPgwIfV1ICsSMANTTFTEr1Tx_Type = Counter64
_JnxMbgPgwIfV1ICsSMANTTFTEr1Tx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSMANTTFTEr1Tx = _JnxMbgPgwIfV1ICsSMANTTFTEr1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 253),
    _JnxMbgPgwIfV1ICsSMANTTFTEr1Tx_Type()
)
jnxMbgPgwIfV1ICsSMANTTFTEr1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSMANTTFTEr1Tx.setStatus("current")
_JnxMbgPgwIfV1ICsSYNTFTErr2Rx_Type = Counter64
_JnxMbgPgwIfV1ICsSYNTFTErr2Rx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSYNTFTErr2Rx = _JnxMbgPgwIfV1ICsSYNTFTErr2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 254),
    _JnxMbgPgwIfV1ICsSYNTFTErr2Rx_Type()
)
jnxMbgPgwIfV1ICsSYNTFTErr2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSYNTFTErr2Rx.setStatus("current")
_JnxMbgPgwIfV1ICsSYNTFTErr2Tx_Type = Counter64
_JnxMbgPgwIfV1ICsSYNTFTErr2Tx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSYNTFTErr2Tx = _JnxMbgPgwIfV1ICsSYNTFTErr2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 255),
    _JnxMbgPgwIfV1ICsSYNTFTErr2Tx_Type()
)
jnxMbgPgwIfV1ICsSYNTFTErr2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSYNTFTErr2Tx.setStatus("current")
_JnxMbgPgwIfV1ICsSMNTPkFlEr1Rx_Type = Counter64
_JnxMbgPgwIfV1ICsSMNTPkFlEr1Rx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSMNTPkFlEr1Rx = _JnxMbgPgwIfV1ICsSMNTPkFlEr1Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 256),
    _JnxMbgPgwIfV1ICsSMNTPkFlEr1Rx_Type()
)
jnxMbgPgwIfV1ICsSMNTPkFlEr1Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSMNTPkFlEr1Rx.setStatus("current")
_JnxMbgPgwIfV1ICsSMNTPkFlEr1Tx_Type = Counter64
_JnxMbgPgwIfV1ICsSMNTPkFlEr1Tx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSMNTPkFlEr1Tx = _JnxMbgPgwIfV1ICsSMNTPkFlEr1Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 257),
    _JnxMbgPgwIfV1ICsSMNTPkFlEr1Tx_Type()
)
jnxMbgPgwIfV1ICsSMNTPkFlEr1Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSMNTPkFlEr1Tx.setStatus("current")
_JnxMbgPgwIfV1ICsSYNPkFlErr2Rx_Type = Counter64
_JnxMbgPgwIfV1ICsSYNPkFlErr2Rx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSYNPkFlErr2Rx = _JnxMbgPgwIfV1ICsSYNPkFlErr2Rx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 258),
    _JnxMbgPgwIfV1ICsSYNPkFlErr2Rx_Type()
)
jnxMbgPgwIfV1ICsSYNPkFlErr2Rx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSYNPkFlErr2Rx.setStatus("current")
_JnxMbgPgwIfV1ICsSYNPkFlErr2Tx_Type = Counter64
_JnxMbgPgwIfV1ICsSYNPkFlErr2Tx_Object = MibTableColumn
jnxMbgPgwIfV1ICsSYNPkFlErr2Tx = _JnxMbgPgwIfV1ICsSYNPkFlErr2Tx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 259),
    _JnxMbgPgwIfV1ICsSYNPkFlErr2Tx_Type()
)
jnxMbgPgwIfV1ICsSYNPkFlErr2Tx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsSYNPkFlErr2Tx.setStatus("current")
_JnxMbgPgwIfV1ICsMissUnknAPNRx_Type = Counter64
_JnxMbgPgwIfV1ICsMissUnknAPNRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMissUnknAPNRx = _JnxMbgPgwIfV1ICsMissUnknAPNRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 260),
    _JnxMbgPgwIfV1ICsMissUnknAPNRx_Type()
)
jnxMbgPgwIfV1ICsMissUnknAPNRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMissUnknAPNRx.setStatus("current")
_JnxMbgPgwIfV1ICsMissUnknAPNTx_Type = Counter64
_JnxMbgPgwIfV1ICsMissUnknAPNTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsMissUnknAPNTx = _JnxMbgPgwIfV1ICsMissUnknAPNTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 261),
    _JnxMbgPgwIfV1ICsMissUnknAPNTx_Type()
)
jnxMbgPgwIfV1ICsMissUnknAPNTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsMissUnknAPNTx.setStatus("current")
_JnxMbgPgwIfV1ICsUnknPDPAdRx_Type = Counter64
_JnxMbgPgwIfV1ICsUnknPDPAdRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsUnknPDPAdRx = _JnxMbgPgwIfV1ICsUnknPDPAdRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 262),
    _JnxMbgPgwIfV1ICsUnknPDPAdRx_Type()
)
jnxMbgPgwIfV1ICsUnknPDPAdRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsUnknPDPAdRx.setStatus("current")
_JnxMbgPgwIfV1ICsUnknPDPAdTx_Type = Counter64
_JnxMbgPgwIfV1ICsUnknPDPAdTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsUnknPDPAdTx = _JnxMbgPgwIfV1ICsUnknPDPAdTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 263),
    _JnxMbgPgwIfV1ICsUnknPDPAdTx_Type()
)
jnxMbgPgwIfV1ICsUnknPDPAdTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsUnknPDPAdTx.setStatus("current")
_JnxMbgPgwIfV1ICsNoTFTCtxExRx_Type = Counter64
_JnxMbgPgwIfV1ICsNoTFTCtxExRx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNoTFTCtxExRx = _JnxMbgPgwIfV1ICsNoTFTCtxExRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 264),
    _JnxMbgPgwIfV1ICsNoTFTCtxExRx_Type()
)
jnxMbgPgwIfV1ICsNoTFTCtxExRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNoTFTCtxExRx.setStatus("current")
_JnxMbgPgwIfV1ICsNoTFTCtxExTx_Type = Counter64
_JnxMbgPgwIfV1ICsNoTFTCtxExTx_Object = MibTableColumn
jnxMbgPgwIfV1ICsNoTFTCtxExTx = _JnxMbgPgwIfV1ICsNoTFTCtxExTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 265),
    _JnxMbgPgwIfV1ICsNoTFTCtxExTx_Type()
)
jnxMbgPgwIfV1ICsNoTFTCtxExTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1ICsNoTFTCtxExTx.setStatus("current")
_JnxMbgPgwIfV0ProtocolErrRx_Type = Counter64
_JnxMbgPgwIfV0ProtocolErrRx_Object = MibTableColumn
jnxMbgPgwIfV0ProtocolErrRx = _JnxMbgPgwIfV0ProtocolErrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 266),
    _JnxMbgPgwIfV0ProtocolErrRx_Type()
)
jnxMbgPgwIfV0ProtocolErrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ProtocolErrRx.setStatus("current")
_JnxMbgPgwIfV0UnSupportedMsgRx_Type = Counter64
_JnxMbgPgwIfV0UnSupportedMsgRx_Object = MibTableColumn
jnxMbgPgwIfV0UnSupportedMsgRx = _JnxMbgPgwIfV0UnSupportedMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 267),
    _JnxMbgPgwIfV0UnSupportedMsgRx_Type()
)
jnxMbgPgwIfV0UnSupportedMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0UnSupportedMsgRx.setStatus("current")
_JnxMbgPgwIfV0T3RespTmrExpRx_Type = Counter64
_JnxMbgPgwIfV0T3RespTmrExpRx_Object = MibTableColumn
jnxMbgPgwIfV0T3RespTmrExpRx = _JnxMbgPgwIfV0T3RespTmrExpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 268),
    _JnxMbgPgwIfV0T3RespTmrExpRx_Type()
)
jnxMbgPgwIfV0T3RespTmrExpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0T3RespTmrExpRx.setStatus("current")
_JnxMbgPgwIfV0GlbNumMsgRx_Type = Counter64
_JnxMbgPgwIfV0GlbNumMsgRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNumMsgRx = _JnxMbgPgwIfV0GlbNumMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 269),
    _JnxMbgPgwIfV0GlbNumMsgRx_Type()
)
jnxMbgPgwIfV0GlbNumMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNumMsgRx.setStatus("current")
_JnxMbgPgwIfV0GlbNumMsgTx_Type = Counter64
_JnxMbgPgwIfV0GlbNumMsgTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNumMsgTx = _JnxMbgPgwIfV0GlbNumMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 270),
    _JnxMbgPgwIfV0GlbNumMsgTx_Type()
)
jnxMbgPgwIfV0GlbNumMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNumMsgTx.setStatus("current")
_JnxMbgPgwIfV0GlbNumBytesRx_Type = Counter64
_JnxMbgPgwIfV0GlbNumBytesRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNumBytesRx = _JnxMbgPgwIfV0GlbNumBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 271),
    _JnxMbgPgwIfV0GlbNumBytesRx_Type()
)
jnxMbgPgwIfV0GlbNumBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNumBytesRx.setStatus("current")
_JnxMbgPgwIfV0GlbNumBytesTx_Type = Counter64
_JnxMbgPgwIfV0GlbNumBytesTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNumBytesTx = _JnxMbgPgwIfV0GlbNumBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 272),
    _JnxMbgPgwIfV0GlbNumBytesTx_Type()
)
jnxMbgPgwIfV0GlbNumBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNumBytesTx.setStatus("current")
_JnxMbgPgwIfV0GlbEchoReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbEchoReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbEchoReqRx = _JnxMbgPgwIfV0GlbEchoReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 273),
    _JnxMbgPgwIfV0GlbEchoReqRx_Type()
)
jnxMbgPgwIfV0GlbEchoReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbEchoReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbEchoReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbEchoReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbEchoReqTx = _JnxMbgPgwIfV0GlbEchoReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 274),
    _JnxMbgPgwIfV0GlbEchoReqTx_Type()
)
jnxMbgPgwIfV0GlbEchoReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbEchoReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbEchoRespRx_Type = Counter64
_JnxMbgPgwIfV0GlbEchoRespRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbEchoRespRx = _JnxMbgPgwIfV0GlbEchoRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 275),
    _JnxMbgPgwIfV0GlbEchoRespRx_Type()
)
jnxMbgPgwIfV0GlbEchoRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbEchoRespRx.setStatus("current")
_JnxMbgPgwIfV0GlbEchoRespTx_Type = Counter64
_JnxMbgPgwIfV0GlbEchoRespTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbEchoRespTx = _JnxMbgPgwIfV0GlbEchoRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 276),
    _JnxMbgPgwIfV0GlbEchoRespTx_Type()
)
jnxMbgPgwIfV0GlbEchoRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbEchoRespTx.setStatus("current")
_JnxMbgPgwIfV0GlbVerNotSupRx_Type = Counter64
_JnxMbgPgwIfV0GlbVerNotSupRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbVerNotSupRx = _JnxMbgPgwIfV0GlbVerNotSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 277),
    _JnxMbgPgwIfV0GlbVerNotSupRx_Type()
)
jnxMbgPgwIfV0GlbVerNotSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbVerNotSupRx.setStatus("current")
_JnxMbgPgwIfV0GlbVerNotSupTx_Type = Counter64
_JnxMbgPgwIfV0GlbVerNotSupTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbVerNotSupTx = _JnxMbgPgwIfV0GlbVerNotSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 278),
    _JnxMbgPgwIfV0GlbVerNotSupTx_Type()
)
jnxMbgPgwIfV0GlbVerNotSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbVerNotSupTx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtPdpCxtReqRx = _JnxMbgPgwIfV0GlbCrtPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 279),
    _JnxMbgPgwIfV0GlbCrtPdpCxtReqRx_Type()
)
jnxMbgPgwIfV0GlbCrtPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtPdpCxtReqTx = _JnxMbgPgwIfV0GlbCrtPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 280),
    _JnxMbgPgwIfV0GlbCrtPdpCxtReqTx_Type()
)
jnxMbgPgwIfV0GlbCrtPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtPdpCxtRspRx = _JnxMbgPgwIfV0GlbCrtPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 281),
    _JnxMbgPgwIfV0GlbCrtPdpCxtRspRx_Type()
)
jnxMbgPgwIfV0GlbCrtPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtPdpCxtRspTx = _JnxMbgPgwIfV0GlbCrtPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 282),
    _JnxMbgPgwIfV0GlbCrtPdpCxtRspTx_Type()
)
jnxMbgPgwIfV0GlbCrtPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV0GlbUpdPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbUpdPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbUpdPdpCxtReqRx = _JnxMbgPgwIfV0GlbUpdPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 283),
    _JnxMbgPgwIfV0GlbUpdPdpCxtReqRx_Type()
)
jnxMbgPgwIfV0GlbUpdPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbUpdPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbUpdPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbUpdPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbUpdPdpCxtReqTx = _JnxMbgPgwIfV0GlbUpdPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 284),
    _JnxMbgPgwIfV0GlbUpdPdpCxtReqTx_Type()
)
jnxMbgPgwIfV0GlbUpdPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbUpdPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbUpdPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbUpdPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbUpdPdpCxtRspRx = _JnxMbgPgwIfV0GlbUpdPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 285),
    _JnxMbgPgwIfV0GlbUpdPdpCxtRspRx_Type()
)
jnxMbgPgwIfV0GlbUpdPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbUpdPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbUpdPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbUpdPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbUpdPdpCxtRspTx = _JnxMbgPgwIfV0GlbUpdPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 286),
    _JnxMbgPgwIfV0GlbUpdPdpCxtRspTx_Type()
)
jnxMbgPgwIfV0GlbUpdPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbUpdPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV0GlbDelPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbDelPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelPdpCxtReqRx = _JnxMbgPgwIfV0GlbDelPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 287),
    _JnxMbgPgwIfV0GlbDelPdpCxtReqRx_Type()
)
jnxMbgPgwIfV0GlbDelPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbDelPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbDelPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelPdpCxtReqTx = _JnxMbgPgwIfV0GlbDelPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 288),
    _JnxMbgPgwIfV0GlbDelPdpCxtReqTx_Type()
)
jnxMbgPgwIfV0GlbDelPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbDelPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbDelPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelPdpCxtRspRx = _JnxMbgPgwIfV0GlbDelPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 289),
    _JnxMbgPgwIfV0GlbDelPdpCxtRspRx_Type()
)
jnxMbgPgwIfV0GlbDelPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbDelPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbDelPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelPdpCxtRspTx = _JnxMbgPgwIfV0GlbDelPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 290),
    _JnxMbgPgwIfV0GlbDelPdpCxtRspTx_Type()
)
jnxMbgPgwIfV0GlbDelPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx = _JnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 291),
    _JnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx_Type()
)
jnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx = _JnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 292),
    _JnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx_Type()
)
jnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx = _JnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 293),
    _JnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx_Type()
)
jnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx.setStatus("current")
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx_Type = Counter64
_JnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx = _JnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 294),
    _JnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx_Type()
)
jnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx.setStatus("current")
_JnxMbgPgwIfV0GlbDelAAPdpCxtRqRx_Type = Counter64
_JnxMbgPgwIfV0GlbDelAAPdpCxtRqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelAAPdpCxtRqRx = _JnxMbgPgwIfV0GlbDelAAPdpCxtRqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 295),
    _JnxMbgPgwIfV0GlbDelAAPdpCxtRqRx_Type()
)
jnxMbgPgwIfV0GlbDelAAPdpCxtRqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelAAPdpCxtRqRx.setStatus("current")
_JnxMbgPgwIfV0GlbDelAAPdpCxtRqTx_Type = Counter64
_JnxMbgPgwIfV0GlbDelAAPdpCxtRqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelAAPdpCxtRqTx = _JnxMbgPgwIfV0GlbDelAAPdpCxtRqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 296),
    _JnxMbgPgwIfV0GlbDelAAPdpCxtRqTx_Type()
)
jnxMbgPgwIfV0GlbDelAAPdpCxtRqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelAAPdpCxtRqTx.setStatus("current")
_JnxMbgPgwIfV0GlbDelAAPdpCxtRpRx_Type = Counter64
_JnxMbgPgwIfV0GlbDelAAPdpCxtRpRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelAAPdpCxtRpRx = _JnxMbgPgwIfV0GlbDelAAPdpCxtRpRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 297),
    _JnxMbgPgwIfV0GlbDelAAPdpCxtRpRx_Type()
)
jnxMbgPgwIfV0GlbDelAAPdpCxtRpRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelAAPdpCxtRpRx.setStatus("current")
_JnxMbgPgwIfV0GlbDelAAPdpCxtRpTx_Type = Counter64
_JnxMbgPgwIfV0GlbDelAAPdpCxtRpTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbDelAAPdpCxtRpTx = _JnxMbgPgwIfV0GlbDelAAPdpCxtRpTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 298),
    _JnxMbgPgwIfV0GlbDelAAPdpCxtRpTx_Type()
)
jnxMbgPgwIfV0GlbDelAAPdpCxtRpTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbDelAAPdpCxtRpTx.setStatus("current")
_JnxMbgPgwIfV0GlbErrorIndRx_Type = Counter64
_JnxMbgPgwIfV0GlbErrorIndRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbErrorIndRx = _JnxMbgPgwIfV0GlbErrorIndRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 299),
    _JnxMbgPgwIfV0GlbErrorIndRx_Type()
)
jnxMbgPgwIfV0GlbErrorIndRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbErrorIndRx.setStatus("current")
_JnxMbgPgwIfV0GlbErrorIndTx_Type = Counter64
_JnxMbgPgwIfV0GlbErrorIndTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbErrorIndTx = _JnxMbgPgwIfV0GlbErrorIndTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 300),
    _JnxMbgPgwIfV0GlbErrorIndTx_Type()
)
jnxMbgPgwIfV0GlbErrorIndTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbErrorIndTx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifReqRx = _JnxMbgPgwIfV0GlbNotifReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 301),
    _JnxMbgPgwIfV0GlbNotifReqRx_Type()
)
jnxMbgPgwIfV0GlbNotifReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifReqTx = _JnxMbgPgwIfV0GlbNotifReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 302),
    _JnxMbgPgwIfV0GlbNotifReqTx_Type()
)
jnxMbgPgwIfV0GlbNotifReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifRspRx = _JnxMbgPgwIfV0GlbNotifRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 303),
    _JnxMbgPgwIfV0GlbNotifRspRx_Type()
)
jnxMbgPgwIfV0GlbNotifRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifRspTx = _JnxMbgPgwIfV0GlbNotifRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 304),
    _JnxMbgPgwIfV0GlbNotifRspTx_Type()
)
jnxMbgPgwIfV0GlbNotifRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifRspTx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifRejReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifRejReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifRejReqRx = _JnxMbgPgwIfV0GlbNotifRejReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 305),
    _JnxMbgPgwIfV0GlbNotifRejReqRx_Type()
)
jnxMbgPgwIfV0GlbNotifRejReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifRejReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifRejReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifRejReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifRejReqTx = _JnxMbgPgwIfV0GlbNotifRejReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 306),
    _JnxMbgPgwIfV0GlbNotifRejReqTx_Type()
)
jnxMbgPgwIfV0GlbNotifRejReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifRejReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifRejRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifRejRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifRejRspRx = _JnxMbgPgwIfV0GlbNotifRejRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 307),
    _JnxMbgPgwIfV0GlbNotifRejRspRx_Type()
)
jnxMbgPgwIfV0GlbNotifRejRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifRejRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbNotifRejRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbNotifRejRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotifRejRspTx = _JnxMbgPgwIfV0GlbNotifRejRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 308),
    _JnxMbgPgwIfV0GlbNotifRejRspTx_Type()
)
jnxMbgPgwIfV0GlbNotifRejRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotifRejRspTx.setStatus("current")
_JnxMbgPgwIfV0GlbRtInfReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbRtInfReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbRtInfReqRx = _JnxMbgPgwIfV0GlbRtInfReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 309),
    _JnxMbgPgwIfV0GlbRtInfReqRx_Type()
)
jnxMbgPgwIfV0GlbRtInfReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbRtInfReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbRtInfReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbRtInfReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbRtInfReqTx = _JnxMbgPgwIfV0GlbRtInfReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 310),
    _JnxMbgPgwIfV0GlbRtInfReqTx_Type()
)
jnxMbgPgwIfV0GlbRtInfReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbRtInfReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbRtInfRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbRtInfRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbRtInfRspRx = _JnxMbgPgwIfV0GlbRtInfRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 311),
    _JnxMbgPgwIfV0GlbRtInfRspRx_Type()
)
jnxMbgPgwIfV0GlbRtInfRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbRtInfRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbRtInfRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbRtInfRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbRtInfRspTx = _JnxMbgPgwIfV0GlbRtInfRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 312),
    _JnxMbgPgwIfV0GlbRtInfRspTx_Type()
)
jnxMbgPgwIfV0GlbRtInfRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbRtInfRspTx.setStatus("current")
_JnxMbgPgwIfV0GlbFailRptReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbFailRptReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbFailRptReqRx = _JnxMbgPgwIfV0GlbFailRptReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 313),
    _JnxMbgPgwIfV0GlbFailRptReqRx_Type()
)
jnxMbgPgwIfV0GlbFailRptReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbFailRptReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbFailRptReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbFailRptReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbFailRptReqTx = _JnxMbgPgwIfV0GlbFailRptReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 314),
    _JnxMbgPgwIfV0GlbFailRptReqTx_Type()
)
jnxMbgPgwIfV0GlbFailRptReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbFailRptReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbFailRptRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbFailRptRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbFailRptRspRx = _JnxMbgPgwIfV0GlbFailRptRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 315),
    _JnxMbgPgwIfV0GlbFailRptRspRx_Type()
)
jnxMbgPgwIfV0GlbFailRptRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbFailRptRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbFailRptRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbFailRptRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbFailRptRspTx = _JnxMbgPgwIfV0GlbFailRptRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 316),
    _JnxMbgPgwIfV0GlbFailRptRspTx_Type()
)
jnxMbgPgwIfV0GlbFailRptRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbFailRptRspTx.setStatus("current")
_JnxMbgPgwIfV0GlbNotMSPresReqRx_Type = Counter64
_JnxMbgPgwIfV0GlbNotMSPresReqRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotMSPresReqRx = _JnxMbgPgwIfV0GlbNotMSPresReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 317),
    _JnxMbgPgwIfV0GlbNotMSPresReqRx_Type()
)
jnxMbgPgwIfV0GlbNotMSPresReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotMSPresReqRx.setStatus("current")
_JnxMbgPgwIfV0GlbNotMSPresReqTx_Type = Counter64
_JnxMbgPgwIfV0GlbNotMSPresReqTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotMSPresReqTx = _JnxMbgPgwIfV0GlbNotMSPresReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 318),
    _JnxMbgPgwIfV0GlbNotMSPresReqTx_Type()
)
jnxMbgPgwIfV0GlbNotMSPresReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotMSPresReqTx.setStatus("current")
_JnxMbgPgwIfV0GlbNotMSPresRspRx_Type = Counter64
_JnxMbgPgwIfV0GlbNotMSPresRspRx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotMSPresRspRx = _JnxMbgPgwIfV0GlbNotMSPresRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 319),
    _JnxMbgPgwIfV0GlbNotMSPresRspRx_Type()
)
jnxMbgPgwIfV0GlbNotMSPresRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotMSPresRspRx.setStatus("current")
_JnxMbgPgwIfV0GlbNotMSPresRspTx_Type = Counter64
_JnxMbgPgwIfV0GlbNotMSPresRspTx_Object = MibTableColumn
jnxMbgPgwIfV0GlbNotMSPresRspTx = _JnxMbgPgwIfV0GlbNotMSPresRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 320),
    _JnxMbgPgwIfV0GlbNotMSPresRspTx_Type()
)
jnxMbgPgwIfV0GlbNotMSPresRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0GlbNotMSPresRspTx.setStatus("current")
_JnxMbgPgwIfV0ICsReqAcceptedRx_Type = Counter64
_JnxMbgPgwIfV0ICsReqAcceptedRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsReqAcceptedRx = _JnxMbgPgwIfV0ICsReqAcceptedRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 321),
    _JnxMbgPgwIfV0ICsReqAcceptedRx_Type()
)
jnxMbgPgwIfV0ICsReqAcceptedRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsReqAcceptedRx.setStatus("current")
_JnxMbgPgwIfV0ICsReqAcceptedTx_Type = Counter64
_JnxMbgPgwIfV0ICsReqAcceptedTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsReqAcceptedTx = _JnxMbgPgwIfV0ICsReqAcceptedTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 322),
    _JnxMbgPgwIfV0ICsReqAcceptedTx_Type()
)
jnxMbgPgwIfV0ICsReqAcceptedTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsReqAcceptedTx.setStatus("current")
_JnxMbgPgwIfV0ICsNonExistRx_Type = Counter64
_JnxMbgPgwIfV0ICsNonExistRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsNonExistRx = _JnxMbgPgwIfV0ICsNonExistRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 323),
    _JnxMbgPgwIfV0ICsNonExistRx_Type()
)
jnxMbgPgwIfV0ICsNonExistRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsNonExistRx.setStatus("current")
_JnxMbgPgwIfV0ICsNonExistTx_Type = Counter64
_JnxMbgPgwIfV0ICsNonExistTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsNonExistTx = _JnxMbgPgwIfV0ICsNonExistTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 324),
    _JnxMbgPgwIfV0ICsNonExistTx_Type()
)
jnxMbgPgwIfV0ICsNonExistTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsNonExistTx.setStatus("current")
_JnxMbgPgwIfV0ICsInvMsgFmtRx_Type = Counter64
_JnxMbgPgwIfV0ICsInvMsgFmtRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsInvMsgFmtRx = _JnxMbgPgwIfV0ICsInvMsgFmtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 325),
    _JnxMbgPgwIfV0ICsInvMsgFmtRx_Type()
)
jnxMbgPgwIfV0ICsInvMsgFmtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsInvMsgFmtRx.setStatus("current")
_JnxMbgPgwIfV0ICsInvMsgFmtTx_Type = Counter64
_JnxMbgPgwIfV0ICsInvMsgFmtTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsInvMsgFmtTx = _JnxMbgPgwIfV0ICsInvMsgFmtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 326),
    _JnxMbgPgwIfV0ICsInvMsgFmtTx_Type()
)
jnxMbgPgwIfV0ICsInvMsgFmtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsInvMsgFmtTx.setStatus("current")
_JnxMbgPgwIfV0ICsIMSINotKnownRx_Type = Counter64
_JnxMbgPgwIfV0ICsIMSINotKnownRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsIMSINotKnownRx = _JnxMbgPgwIfV0ICsIMSINotKnownRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 327),
    _JnxMbgPgwIfV0ICsIMSINotKnownRx_Type()
)
jnxMbgPgwIfV0ICsIMSINotKnownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsIMSINotKnownRx.setStatus("current")
_JnxMbgPgwIfV0ICsIMSINotKnownTx_Type = Counter64
_JnxMbgPgwIfV0ICsIMSINotKnownTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsIMSINotKnownTx = _JnxMbgPgwIfV0ICsIMSINotKnownTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 328),
    _JnxMbgPgwIfV0ICsIMSINotKnownTx_Type()
)
jnxMbgPgwIfV0ICsIMSINotKnownTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsIMSINotKnownTx.setStatus("current")
_JnxMbgPgwIfV0ICsMSGRPSDetachRx_Type = Counter64
_JnxMbgPgwIfV0ICsMSGRPSDetachRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsMSGRPSDetachRx = _JnxMbgPgwIfV0ICsMSGRPSDetachRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 329),
    _JnxMbgPgwIfV0ICsMSGRPSDetachRx_Type()
)
jnxMbgPgwIfV0ICsMSGRPSDetachRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsMSGRPSDetachRx.setStatus("current")
_JnxMbgPgwIfV0ICsMSGRPSDetachTx_Type = Counter64
_JnxMbgPgwIfV0ICsMSGRPSDetachTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsMSGRPSDetachTx = _JnxMbgPgwIfV0ICsMSGRPSDetachTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 330),
    _JnxMbgPgwIfV0ICsMSGRPSDetachTx_Type()
)
jnxMbgPgwIfV0ICsMSGRPSDetachTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsMSGRPSDetachTx.setStatus("current")
_JnxMbgPgwIfV0ICsMSNotGRPSRespRx_Type = Counter64
_JnxMbgPgwIfV0ICsMSNotGRPSRespRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsMSNotGRPSRespRx = _JnxMbgPgwIfV0ICsMSNotGRPSRespRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 331),
    _JnxMbgPgwIfV0ICsMSNotGRPSRespRx_Type()
)
jnxMbgPgwIfV0ICsMSNotGRPSRespRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsMSNotGRPSRespRx.setStatus("current")
_JnxMbgPgwIfV0ICsMSNotGRPSRespTx_Type = Counter64
_JnxMbgPgwIfV0ICsMSNotGRPSRespTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsMSNotGRPSRespTx = _JnxMbgPgwIfV0ICsMSNotGRPSRespTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 332),
    _JnxMbgPgwIfV0ICsMSNotGRPSRespTx_Type()
)
jnxMbgPgwIfV0ICsMSNotGRPSRespTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsMSNotGRPSRespTx.setStatus("current")
_JnxMbgPgwIfV0ICsMSRefusesRx_Type = Counter64
_JnxMbgPgwIfV0ICsMSRefusesRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsMSRefusesRx = _JnxMbgPgwIfV0ICsMSRefusesRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 333),
    _JnxMbgPgwIfV0ICsMSRefusesRx_Type()
)
jnxMbgPgwIfV0ICsMSRefusesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsMSRefusesRx.setStatus("current")
_JnxMbgPgwIfV0ICsMSRefusesTx_Type = Counter64
_JnxMbgPgwIfV0ICsMSRefusesTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsMSRefusesTx = _JnxMbgPgwIfV0ICsMSRefusesTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 334),
    _JnxMbgPgwIfV0ICsMSRefusesTx_Type()
)
jnxMbgPgwIfV0ICsMSRefusesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsMSRefusesTx.setStatus("current")
_JnxMbgPgwIfV0ICsVerNotSuppRx_Type = Counter64
_JnxMbgPgwIfV0ICsVerNotSuppRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsVerNotSuppRx = _JnxMbgPgwIfV0ICsVerNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 335),
    _JnxMbgPgwIfV0ICsVerNotSuppRx_Type()
)
jnxMbgPgwIfV0ICsVerNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsVerNotSuppRx.setStatus("current")
_JnxMbgPgwIfV0ICsVerNotSuppTx_Type = Counter64
_JnxMbgPgwIfV0ICsVerNotSuppTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsVerNotSuppTx = _JnxMbgPgwIfV0ICsVerNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 336),
    _JnxMbgPgwIfV0ICsVerNotSuppTx_Type()
)
jnxMbgPgwIfV0ICsVerNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsVerNotSuppTx.setStatus("current")
_JnxMbgPgwIfV0ICsNoResRx_Type = Counter64
_JnxMbgPgwIfV0ICsNoResRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsNoResRx = _JnxMbgPgwIfV0ICsNoResRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 337),
    _JnxMbgPgwIfV0ICsNoResRx_Type()
)
jnxMbgPgwIfV0ICsNoResRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsNoResRx.setStatus("current")
_JnxMbgPgwIfV0ICsNoResTx_Type = Counter64
_JnxMbgPgwIfV0ICsNoResTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsNoResTx = _JnxMbgPgwIfV0ICsNoResTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 338),
    _JnxMbgPgwIfV0ICsNoResTx_Type()
)
jnxMbgPgwIfV0ICsNoResTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsNoResTx.setStatus("current")
_JnxMbgPgwIfV0ICsServNotSuppRx_Type = Counter64
_JnxMbgPgwIfV0ICsServNotSuppRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsServNotSuppRx = _JnxMbgPgwIfV0ICsServNotSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 339),
    _JnxMbgPgwIfV0ICsServNotSuppRx_Type()
)
jnxMbgPgwIfV0ICsServNotSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsServNotSuppRx.setStatus("current")
_JnxMbgPgwIfV0ICsServNotSuppTx_Type = Counter64
_JnxMbgPgwIfV0ICsServNotSuppTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsServNotSuppTx = _JnxMbgPgwIfV0ICsServNotSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 340),
    _JnxMbgPgwIfV0ICsServNotSuppTx_Type()
)
jnxMbgPgwIfV0ICsServNotSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsServNotSuppTx.setStatus("current")
_JnxMbgPgwIfV0ICsManIEIncrtRx_Type = Counter64
_JnxMbgPgwIfV0ICsManIEIncrtRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsManIEIncrtRx = _JnxMbgPgwIfV0ICsManIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 341),
    _JnxMbgPgwIfV0ICsManIEIncrtRx_Type()
)
jnxMbgPgwIfV0ICsManIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsManIEIncrtRx.setStatus("current")
_JnxMbgPgwIfV0ICsManIEIncrtTx_Type = Counter64
_JnxMbgPgwIfV0ICsManIEIncrtTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsManIEIncrtTx = _JnxMbgPgwIfV0ICsManIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 342),
    _JnxMbgPgwIfV0ICsManIEIncrtTx_Type()
)
jnxMbgPgwIfV0ICsManIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsManIEIncrtTx.setStatus("current")
_JnxMbgPgwIfV0ICsManIEMissRx_Type = Counter64
_JnxMbgPgwIfV0ICsManIEMissRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsManIEMissRx = _JnxMbgPgwIfV0ICsManIEMissRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 343),
    _JnxMbgPgwIfV0ICsManIEMissRx_Type()
)
jnxMbgPgwIfV0ICsManIEMissRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsManIEMissRx.setStatus("current")
_JnxMbgPgwIfV0ICsManIEMissTx_Type = Counter64
_JnxMbgPgwIfV0ICsManIEMissTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsManIEMissTx = _JnxMbgPgwIfV0ICsManIEMissTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 344),
    _JnxMbgPgwIfV0ICsManIEMissTx_Type()
)
jnxMbgPgwIfV0ICsManIEMissTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsManIEMissTx.setStatus("current")
_JnxMbgPgwIfV0ICsOptIEIncrtRx_Type = Counter64
_JnxMbgPgwIfV0ICsOptIEIncrtRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsOptIEIncrtRx = _JnxMbgPgwIfV0ICsOptIEIncrtRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 345),
    _JnxMbgPgwIfV0ICsOptIEIncrtRx_Type()
)
jnxMbgPgwIfV0ICsOptIEIncrtRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsOptIEIncrtRx.setStatus("current")
_JnxMbgPgwIfV0ICsOptIEIncrtTx_Type = Counter64
_JnxMbgPgwIfV0ICsOptIEIncrtTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsOptIEIncrtTx = _JnxMbgPgwIfV0ICsOptIEIncrtTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 346),
    _JnxMbgPgwIfV0ICsOptIEIncrtTx_Type()
)
jnxMbgPgwIfV0ICsOptIEIncrtTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsOptIEIncrtTx.setStatus("current")
_JnxMbgPgwIfV0ICsSysFailRx_Type = Counter64
_JnxMbgPgwIfV0ICsSysFailRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsSysFailRx = _JnxMbgPgwIfV0ICsSysFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 347),
    _JnxMbgPgwIfV0ICsSysFailRx_Type()
)
jnxMbgPgwIfV0ICsSysFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsSysFailRx.setStatus("current")
_JnxMbgPgwIfV0ICsSysFailTx_Type = Counter64
_JnxMbgPgwIfV0ICsSysFailTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsSysFailTx = _JnxMbgPgwIfV0ICsSysFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 348),
    _JnxMbgPgwIfV0ICsSysFailTx_Type()
)
jnxMbgPgwIfV0ICsSysFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsSysFailTx.setStatus("current")
_JnxMbgPgwIfV0ICsRoamRestrictRx_Type = Counter64
_JnxMbgPgwIfV0ICsRoamRestrictRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsRoamRestrictRx = _JnxMbgPgwIfV0ICsRoamRestrictRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 349),
    _JnxMbgPgwIfV0ICsRoamRestrictRx_Type()
)
jnxMbgPgwIfV0ICsRoamRestrictRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsRoamRestrictRx.setStatus("current")
_JnxMbgPgwIfV0ICsRoamRestrictTx_Type = Counter64
_JnxMbgPgwIfV0ICsRoamRestrictTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsRoamRestrictTx = _JnxMbgPgwIfV0ICsRoamRestrictTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 350),
    _JnxMbgPgwIfV0ICsRoamRestrictTx_Type()
)
jnxMbgPgwIfV0ICsRoamRestrictTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsRoamRestrictTx.setStatus("current")
_JnxMbgPgwIfV0ICsPTMSISigMMRx_Type = Counter64
_JnxMbgPgwIfV0ICsPTMSISigMMRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsPTMSISigMMRx = _JnxMbgPgwIfV0ICsPTMSISigMMRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 351),
    _JnxMbgPgwIfV0ICsPTMSISigMMRx_Type()
)
jnxMbgPgwIfV0ICsPTMSISigMMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsPTMSISigMMRx.setStatus("current")
_JnxMbgPgwIfV0ICsPTMSISigMMTx_Type = Counter64
_JnxMbgPgwIfV0ICsPTMSISigMMTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsPTMSISigMMTx = _JnxMbgPgwIfV0ICsPTMSISigMMTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 352),
    _JnxMbgPgwIfV0ICsPTMSISigMMTx_Type()
)
jnxMbgPgwIfV0ICsPTMSISigMMTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsPTMSISigMMTx.setStatus("current")
_JnxMbgPgwIfV0ICsGPRSConnSuppRx_Type = Counter64
_JnxMbgPgwIfV0ICsGPRSConnSuppRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsGPRSConnSuppRx = _JnxMbgPgwIfV0ICsGPRSConnSuppRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 353),
    _JnxMbgPgwIfV0ICsGPRSConnSuppRx_Type()
)
jnxMbgPgwIfV0ICsGPRSConnSuppRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsGPRSConnSuppRx.setStatus("current")
_JnxMbgPgwIfV0ICsGPRSConnSuppTx_Type = Counter64
_JnxMbgPgwIfV0ICsGPRSConnSuppTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsGPRSConnSuppTx = _JnxMbgPgwIfV0ICsGPRSConnSuppTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 354),
    _JnxMbgPgwIfV0ICsGPRSConnSuppTx_Type()
)
jnxMbgPgwIfV0ICsGPRSConnSuppTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsGPRSConnSuppTx.setStatus("current")
_JnxMbgPgwIfV0ICsAuthFailRx_Type = Counter64
_JnxMbgPgwIfV0ICsAuthFailRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsAuthFailRx = _JnxMbgPgwIfV0ICsAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 355),
    _JnxMbgPgwIfV0ICsAuthFailRx_Type()
)
jnxMbgPgwIfV0ICsAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsAuthFailRx.setStatus("current")
_JnxMbgPgwIfV0ICsAuthFailTx_Type = Counter64
_JnxMbgPgwIfV0ICsAuthFailTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsAuthFailTx = _JnxMbgPgwIfV0ICsAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 356),
    _JnxMbgPgwIfV0ICsAuthFailTx_Type()
)
jnxMbgPgwIfV0ICsAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsAuthFailTx.setStatus("current")
_JnxMbgPgwIfV0ICsUserAuthFailRx_Type = Counter64
_JnxMbgPgwIfV0ICsUserAuthFailRx_Object = MibTableColumn
jnxMbgPgwIfV0ICsUserAuthFailRx = _JnxMbgPgwIfV0ICsUserAuthFailRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 357),
    _JnxMbgPgwIfV0ICsUserAuthFailRx_Type()
)
jnxMbgPgwIfV0ICsUserAuthFailRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsUserAuthFailRx.setStatus("current")
_JnxMbgPgwIfV0ICsUserAuthFailTx_Type = Counter64
_JnxMbgPgwIfV0ICsUserAuthFailTx_Object = MibTableColumn
jnxMbgPgwIfV0ICsUserAuthFailTx = _JnxMbgPgwIfV0ICsUserAuthFailTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 358),
    _JnxMbgPgwIfV0ICsUserAuthFailTx_Type()
)
jnxMbgPgwIfV0ICsUserAuthFailTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV0ICsUserAuthFailTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsLclDetRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsLclDetRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsLclDetRx = _JnxMbgPgwIfGtpV2ICsLclDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 359),
    _JnxMbgPgwIfGtpV2ICsLclDetRx_Type()
)
jnxMbgPgwIfGtpV2ICsLclDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsLclDetRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsLclDetTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsLclDetTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsLclDetTx = _JnxMbgPgwIfGtpV2ICsLclDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 360),
    _JnxMbgPgwIfGtpV2ICsLclDetTx_Type()
)
jnxMbgPgwIfGtpV2ICsLclDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsLclDetTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsCmpDetRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsCmpDetRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsCmpDetRx = _JnxMbgPgwIfGtpV2ICsCmpDetRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 361),
    _JnxMbgPgwIfGtpV2ICsCmpDetRx_Type()
)
jnxMbgPgwIfGtpV2ICsCmpDetRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsCmpDetRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsCmpDetTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsCmpDetTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsCmpDetTx = _JnxMbgPgwIfGtpV2ICsCmpDetTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 362),
    _JnxMbgPgwIfGtpV2ICsCmpDetTx_Type()
)
jnxMbgPgwIfGtpV2ICsCmpDetTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsCmpDetTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsRATChgRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsRATChgRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsRATChgRx = _JnxMbgPgwIfGtpV2ICsRATChgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 363),
    _JnxMbgPgwIfGtpV2ICsRATChgRx_Type()
)
jnxMbgPgwIfGtpV2ICsRATChgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsRATChgRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsRATChgTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsRATChgTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsRATChgTx = _JnxMbgPgwIfGtpV2ICsRATChgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 364),
    _JnxMbgPgwIfGtpV2ICsRATChgTx_Type()
)
jnxMbgPgwIfGtpV2ICsRATChgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsRATChgTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsISRDeactRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsISRDeactRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsISRDeactRx = _JnxMbgPgwIfGtpV2ICsISRDeactRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 365),
    _JnxMbgPgwIfGtpV2ICsISRDeactRx_Type()
)
jnxMbgPgwIfGtpV2ICsISRDeactRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsISRDeactRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsISRDeactTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsISRDeactTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsISRDeactTx = _JnxMbgPgwIfGtpV2ICsISRDeactTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 366),
    _JnxMbgPgwIfGtpV2ICsISRDeactTx_Type()
)
jnxMbgPgwIfGtpV2ICsISRDeactTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsISRDeactTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsEIFRNCEnRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsEIFRNCEnRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsEIFRNCEnRx = _JnxMbgPgwIfGtpV2ICsEIFRNCEnRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 367),
    _JnxMbgPgwIfGtpV2ICsEIFRNCEnRx_Type()
)
jnxMbgPgwIfGtpV2ICsEIFRNCEnRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsEIFRNCEnRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsEIFRNCEnTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsEIFRNCEnTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsEIFRNCEnTx = _JnxMbgPgwIfGtpV2ICsEIFRNCEnTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 368),
    _JnxMbgPgwIfGtpV2ICsEIFRNCEnTx_Type()
)
jnxMbgPgwIfGtpV2ICsEIFRNCEnTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsEIFRNCEnTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsSemErTADRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsSemErTADRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsSemErTADRx = _JnxMbgPgwIfGtpV2ICsSemErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 369),
    _JnxMbgPgwIfGtpV2ICsSemErTADRx_Type()
)
jnxMbgPgwIfGtpV2ICsSemErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsSemErTADRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsSemErTADTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsSemErTADTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsSemErTADTx = _JnxMbgPgwIfGtpV2ICsSemErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 370),
    _JnxMbgPgwIfGtpV2ICsSemErTADTx_Type()
)
jnxMbgPgwIfGtpV2ICsSemErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsSemErTADTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsSynErTADRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsSynErTADRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsSynErTADRx = _JnxMbgPgwIfGtpV2ICsSynErTADRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 371),
    _JnxMbgPgwIfGtpV2ICsSynErTADRx_Type()
)
jnxMbgPgwIfGtpV2ICsSynErTADRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsSynErTADRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsSynErTADTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsSynErTADTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsSynErTADTx = _JnxMbgPgwIfGtpV2ICsSynErTADTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 372),
    _JnxMbgPgwIfGtpV2ICsSynErTADTx_Type()
)
jnxMbgPgwIfGtpV2ICsSynErTADTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsSynErTADTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsRMValRcvRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsRMValRcvRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsRMValRcvRx = _JnxMbgPgwIfGtpV2ICsRMValRcvRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 373),
    _JnxMbgPgwIfGtpV2ICsRMValRcvRx_Type()
)
jnxMbgPgwIfGtpV2ICsRMValRcvRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsRMValRcvRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsRMValRcvTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsRMValRcvTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsRMValRcvTx = _JnxMbgPgwIfGtpV2ICsRMValRcvTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 374),
    _JnxMbgPgwIfGtpV2ICsRMValRcvTx_Type()
)
jnxMbgPgwIfGtpV2ICsRMValRcvTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsRMValRcvTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsRPrNtRspRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsRPrNtRspRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsRPrNtRspRx = _JnxMbgPgwIfGtpV2ICsRPrNtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 375),
    _JnxMbgPgwIfGtpV2ICsRPrNtRspRx_Type()
)
jnxMbgPgwIfGtpV2ICsRPrNtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsRPrNtRspRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsRPrNtRspTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsRPrNtRspTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsRPrNtRspTx = _JnxMbgPgwIfGtpV2ICsRPrNtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 376),
    _JnxMbgPgwIfGtpV2ICsRPrNtRspTx_Type()
)
jnxMbgPgwIfGtpV2ICsRPrNtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsRPrNtRspTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsColNWReqRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsColNWReqRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsColNWReqRx = _JnxMbgPgwIfGtpV2ICsColNWReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 377),
    _JnxMbgPgwIfGtpV2ICsColNWReqRx_Type()
)
jnxMbgPgwIfGtpV2ICsColNWReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsColNWReqRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsColNWReqTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsColNWReqTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsColNWReqTx = _JnxMbgPgwIfGtpV2ICsColNWReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 378),
    _JnxMbgPgwIfGtpV2ICsColNWReqTx_Type()
)
jnxMbgPgwIfGtpV2ICsColNWReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsColNWReqTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsUnPgUESusRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsUnPgUESusRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsUnPgUESusRx = _JnxMbgPgwIfGtpV2ICsUnPgUESusRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 379),
    _JnxMbgPgwIfGtpV2ICsUnPgUESusRx_Type()
)
jnxMbgPgwIfGtpV2ICsUnPgUESusRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsUnPgUESusRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsUnPgUESusTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsUnPgUESusTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsUnPgUESusTx = _JnxMbgPgwIfGtpV2ICsUnPgUESusTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 380),
    _JnxMbgPgwIfGtpV2ICsUnPgUESusTx_Type()
)
jnxMbgPgwIfGtpV2ICsUnPgUESusTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsUnPgUESusTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsInvTotLenRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsInvTotLenRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsInvTotLenRx = _JnxMbgPgwIfGtpV2ICsInvTotLenRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 381),
    _JnxMbgPgwIfGtpV2ICsInvTotLenRx_Type()
)
jnxMbgPgwIfGtpV2ICsInvTotLenRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsInvTotLenRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsInvTotLenTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsInvTotLenTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsInvTotLenTx = _JnxMbgPgwIfGtpV2ICsInvTotLenTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 382),
    _JnxMbgPgwIfGtpV2ICsInvTotLenTx_Type()
)
jnxMbgPgwIfGtpV2ICsInvTotLenTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsInvTotLenTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsDtForNtSupRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsDtForNtSupRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsDtForNtSupRx = _JnxMbgPgwIfGtpV2ICsDtForNtSupRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 383),
    _JnxMbgPgwIfGtpV2ICsDtForNtSupRx_Type()
)
jnxMbgPgwIfGtpV2ICsDtForNtSupRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsDtForNtSupRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsDtForNtSupTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsDtForNtSupTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsDtForNtSupTx = _JnxMbgPgwIfGtpV2ICsDtForNtSupTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 384),
    _JnxMbgPgwIfGtpV2ICsDtForNtSupTx_Type()
)
jnxMbgPgwIfGtpV2ICsDtForNtSupTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsDtForNtSupTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsInReFRePrRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsInReFRePrRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsInReFRePrRx = _JnxMbgPgwIfGtpV2ICsInReFRePrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 385),
    _JnxMbgPgwIfGtpV2ICsInReFRePrRx_Type()
)
jnxMbgPgwIfGtpV2ICsInReFRePrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsInReFRePrRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsInReFRePrTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsInReFRePrTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsInReFRePrTx = _JnxMbgPgwIfGtpV2ICsInReFRePrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 386),
    _JnxMbgPgwIfGtpV2ICsInReFRePrTx_Type()
)
jnxMbgPgwIfGtpV2ICsInReFRePrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsInReFRePrTx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsInvPrRx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsInvPrRx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsInvPrRx = _JnxMbgPgwIfGtpV2ICsInvPrRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 387),
    _JnxMbgPgwIfGtpV2ICsInvPrRx_Type()
)
jnxMbgPgwIfGtpV2ICsInvPrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsInvPrRx.setStatus("current")
_JnxMbgPgwIfGtpV2ICsInvPrTx_Type = Counter64
_JnxMbgPgwIfGtpV2ICsInvPrTx_Object = MibTableColumn
jnxMbgPgwIfGtpV2ICsInvPrTx = _JnxMbgPgwIfGtpV2ICsInvPrTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 388),
    _JnxMbgPgwIfGtpV2ICsInvPrTx_Type()
)
jnxMbgPgwIfGtpV2ICsInvPrTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfGtpV2ICsInvPrTx.setStatus("current")
_JnxMbgPgwIfV1InitPdpCxtReqRx_Type = Counter64
_JnxMbgPgwIfV1InitPdpCxtReqRx_Object = MibTableColumn
jnxMbgPgwIfV1InitPdpCxtReqRx = _JnxMbgPgwIfV1InitPdpCxtReqRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 389),
    _JnxMbgPgwIfV1InitPdpCxtReqRx_Type()
)
jnxMbgPgwIfV1InitPdpCxtReqRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1InitPdpCxtReqRx.setStatus("current")
_JnxMbgPgwIfV1InitPdpCxtReqTx_Type = Counter64
_JnxMbgPgwIfV1InitPdpCxtReqTx_Object = MibTableColumn
jnxMbgPgwIfV1InitPdpCxtReqTx = _JnxMbgPgwIfV1InitPdpCxtReqTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 390),
    _JnxMbgPgwIfV1InitPdpCxtReqTx_Type()
)
jnxMbgPgwIfV1InitPdpCxtReqTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1InitPdpCxtReqTx.setStatus("current")
_JnxMbgPgwIfV1InitPdpCxtRspRx_Type = Counter64
_JnxMbgPgwIfV1InitPdpCxtRspRx_Object = MibTableColumn
jnxMbgPgwIfV1InitPdpCxtRspRx = _JnxMbgPgwIfV1InitPdpCxtRspRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 391),
    _JnxMbgPgwIfV1InitPdpCxtRspRx_Type()
)
jnxMbgPgwIfV1InitPdpCxtRspRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1InitPdpCxtRspRx.setStatus("current")
_JnxMbgPgwIfV1InitPdpCxtRspTx_Type = Counter64
_JnxMbgPgwIfV1InitPdpCxtRspTx_Object = MibTableColumn
jnxMbgPgwIfV1InitPdpCxtRspTx = _JnxMbgPgwIfV1InitPdpCxtRspTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 392),
    _JnxMbgPgwIfV1InitPdpCxtRspTx_Type()
)
jnxMbgPgwIfV1InitPdpCxtRspTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV1InitPdpCxtRspTx.setStatus("current")
_JnxMbgPgwIfV2SuspNotifRx_Type = Counter64
_JnxMbgPgwIfV2SuspNotifRx_Object = MibTableColumn
jnxMbgPgwIfV2SuspNotifRx = _JnxMbgPgwIfV2SuspNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 393),
    _JnxMbgPgwIfV2SuspNotifRx_Type()
)
jnxMbgPgwIfV2SuspNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2SuspNotifRx.setStatus("current")
_JnxMbgPgwIfV2SuspNotifTx_Type = Counter64
_JnxMbgPgwIfV2SuspNotifTx_Object = MibTableColumn
jnxMbgPgwIfV2SuspNotifTx = _JnxMbgPgwIfV2SuspNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 394),
    _JnxMbgPgwIfV2SuspNotifTx_Type()
)
jnxMbgPgwIfV2SuspNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2SuspNotifTx.setStatus("current")
_JnxMbgPgwIfV2SuspAckRx_Type = Counter64
_JnxMbgPgwIfV2SuspAckRx_Object = MibTableColumn
jnxMbgPgwIfV2SuspAckRx = _JnxMbgPgwIfV2SuspAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 395),
    _JnxMbgPgwIfV2SuspAckRx_Type()
)
jnxMbgPgwIfV2SuspAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2SuspAckRx.setStatus("current")
_JnxMbgPgwIfV2SuspAckTx_Type = Counter64
_JnxMbgPgwIfV2SuspAckTx_Object = MibTableColumn
jnxMbgPgwIfV2SuspAckTx = _JnxMbgPgwIfV2SuspAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 396),
    _JnxMbgPgwIfV2SuspAckTx_Type()
)
jnxMbgPgwIfV2SuspAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2SuspAckTx.setStatus("current")
_JnxMbgPgwIfV2ResumeNotifRx_Type = Counter64
_JnxMbgPgwIfV2ResumeNotifRx_Object = MibTableColumn
jnxMbgPgwIfV2ResumeNotifRx = _JnxMbgPgwIfV2ResumeNotifRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 397),
    _JnxMbgPgwIfV2ResumeNotifRx_Type()
)
jnxMbgPgwIfV2ResumeNotifRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ResumeNotifRx.setStatus("current")
_JnxMbgPgwIfV2ResumeNotifTx_Type = Counter64
_JnxMbgPgwIfV2ResumeNotifTx_Object = MibTableColumn
jnxMbgPgwIfV2ResumeNotifTx = _JnxMbgPgwIfV2ResumeNotifTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 398),
    _JnxMbgPgwIfV2ResumeNotifTx_Type()
)
jnxMbgPgwIfV2ResumeNotifTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ResumeNotifTx.setStatus("current")
_JnxMbgPgwIfV2ResumeAckRx_Type = Counter64
_JnxMbgPgwIfV2ResumeAckRx_Object = MibTableColumn
jnxMbgPgwIfV2ResumeAckRx = _JnxMbgPgwIfV2ResumeAckRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 399),
    _JnxMbgPgwIfV2ResumeAckRx_Type()
)
jnxMbgPgwIfV2ResumeAckRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ResumeAckRx.setStatus("current")
_JnxMbgPgwIfV2ResumeAckTx_Type = Counter64
_JnxMbgPgwIfV2ResumeAckTx_Object = MibTableColumn
jnxMbgPgwIfV2ResumeAckTx = _JnxMbgPgwIfV2ResumeAckTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 400),
    _JnxMbgPgwIfV2ResumeAckTx_Type()
)
jnxMbgPgwIfV2ResumeAckTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2ResumeAckTx.setStatus("current")
_JnxMbgPgwIfV2PiggybackMsgRx_Type = Counter64
_JnxMbgPgwIfV2PiggybackMsgRx_Object = MibTableColumn
jnxMbgPgwIfV2PiggybackMsgRx = _JnxMbgPgwIfV2PiggybackMsgRx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 401),
    _JnxMbgPgwIfV2PiggybackMsgRx_Type()
)
jnxMbgPgwIfV2PiggybackMsgRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2PiggybackMsgRx.setStatus("current")
_JnxMbgPgwIfV2PiggybackMsgTx_Type = Counter64
_JnxMbgPgwIfV2PiggybackMsgTx_Object = MibTableColumn
jnxMbgPgwIfV2PiggybackMsgTx = _JnxMbgPgwIfV2PiggybackMsgTx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 1, 11, 1, 402),
    _JnxMbgPgwIfV2PiggybackMsgTx_Type()
)
jnxMbgPgwIfV2PiggybackMsgTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgPgwIfV2PiggybackMsgTx.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgPgwGtpPeerGWUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0, 1)
)
jnxMbgPgwGtpPeerGWUpNotif.setObjects(
    ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerName")
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerGWUpNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwGtpPeerDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0, 2)
)
jnxMbgPgwGtpPeerDownNotif.setObjects(
    ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerName")
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerDownNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwGtpPeerDNThresPerPeerNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0, 3)
)
jnxMbgPgwGtpPeerDNThresPerPeerNotif.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerName"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpAlarmState"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpAlarmStatCounter"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerDNThresPerPeerNotif.setStatus(
        "deprecated"
    )

jnxMbgPgwGtpPeerGwUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0, 4)
)
jnxMbgPgwGtpPeerGwUpNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerGwUpNotify.setStatus(
        "current"
    )

jnxMbgPgwGtpPeerGwDnNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0, 5)
)
jnxMbgPgwGtpPeerGwDnNotify.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerName"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPeerGwDnNotify.setStatus(
        "current"
    )

jnxMbgPgwGtpPrDnTPerPrAlrmActv = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0, 6)
)
jnxMbgPgwGtpPrDnTPerPrAlrmActv.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerName"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpAlarmStatCounter"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPrDnTPerPrAlrmActv.setStatus(
        "current"
    )

jnxMbgPgwGtpPrDnTPerPrAlrmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 1, 2, 0, 7)
)
jnxMbgPgwGtpPrDnTPerPrAlrmClr.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpGwName"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpInterfaceType"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpPeerName"),
        ("JUNIPER-MOBILE-GATEWAY-GTP-MIB", "jnxMbgPgwGtpAlarmStatCounter"))
)
if mibBuilder.loadTexts:
    jnxMbgPgwGtpPrDnTPerPrAlrmClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-GTP-MIB",
    **{"jnxMbgPgwGtpMib": jnxMbgPgwGtpMib,
       "jnxMbgPgwGtpNotifications": jnxMbgPgwGtpNotifications,
       "jnxMbgPgwGtpPeerGWUpNotif": jnxMbgPgwGtpPeerGWUpNotif,
       "jnxMbgPgwGtpPeerDownNotif": jnxMbgPgwGtpPeerDownNotif,
       "jnxMbgPgwGtpPeerDNThresPerPeerNotif": jnxMbgPgwGtpPeerDNThresPerPeerNotif,
       "jnxMbgPgwGtpPeerGwUpNotify": jnxMbgPgwGtpPeerGwUpNotify,
       "jnxMbgPgwGtpPeerGwDnNotify": jnxMbgPgwGtpPeerGwDnNotify,
       "jnxMbgPgwGtpPrDnTPerPrAlrmActv": jnxMbgPgwGtpPrDnTPerPrAlrmActv,
       "jnxMbgPgwGtpPrDnTPerPrAlrmClr": jnxMbgPgwGtpPrDnTPerPrAlrmClr,
       "jnxMbgPgwGtpObjects": jnxMbgPgwGtpObjects,
       "jnxMbgPgwGtpCGlblCfgGroup": jnxMbgPgwGtpCGlblCfgGroup,
       "jnxMbgPgwGtpGWName": jnxMbgPgwGtpGWName,
       "jnxMbgPgwGtpPeerHistory": jnxMbgPgwGtpPeerHistory,
       "jnxMbgPgwGtpN3Reqs": jnxMbgPgwGtpN3Reqs,
       "jnxMbgPgwGtpT3Resp": jnxMbgPgwGtpT3Resp,
       "jnxMbgPgwGtpCtrlEchIntr": jnxMbgPgwGtpCtrlEchIntr,
       "jnxMbgPgwGtpCtrlNoPathMgmt": jnxMbgPgwGtpCtrlNoPathMgmt,
       "jnxMbgPgwGtpCtrlIfName": jnxMbgPgwGtpCtrlIfName,
       "jnxMbgPgwGtpCtrlIfRtbId": jnxMbgPgwGtpCtrlIfRtbId,
       "jnxMbgPgwGtpCtrlIPv4Addr": jnxMbgPgwGtpCtrlIPv4Addr,
       "jnxMbgPgwGtpCtrlIPv6Addr": jnxMbgPgwGtpCtrlIPv6Addr,
       "jnxMbgPgwGtpDataN3Reqs": jnxMbgPgwGtpDataN3Reqs,
       "jnxMbgPgwGtpDataT3Resp": jnxMbgPgwGtpDataT3Resp,
       "jnxMbgPgwGtpDataEchIntr": jnxMbgPgwGtpDataEchIntr,
       "jnxMbgPgwGtpDataNoPathMgmt": jnxMbgPgwGtpDataNoPathMgmt,
       "jnxMbgPgwGtpDataIfName": jnxMbgPgwGtpDataIfName,
       "jnxMbgPgwGtpDataIfRtbId": jnxMbgPgwGtpDataIfRtbId,
       "jnxMbgPgwGtpDataIPv4Addr": jnxMbgPgwGtpDataIPv4Addr,
       "jnxMbgPgwGtpDataIPv6Addr": jnxMbgPgwGtpDataIPv6Addr,
       "jnxMbgPgwGtpCGnGpGlblCfgGroup": jnxMbgPgwGtpCGnGpGlblCfgGroup,
       "jnxMbgPgwGtpCGnGpGWName": jnxMbgPgwGtpCGnGpGWName,
       "jnxMbgPgwGtpCGnGpPeerHistory": jnxMbgPgwGtpCGnGpPeerHistory,
       "jnxMbgPgwGtpCGnGpN3Reqs": jnxMbgPgwGtpCGnGpN3Reqs,
       "jnxMbgPgwGtpCGnGpT3Resp": jnxMbgPgwGtpCGnGpT3Resp,
       "jnxMbgPgwGtpCGnGpCtrlEchIntr": jnxMbgPgwGtpCGnGpCtrlEchIntr,
       "jnxMbgPgwGtpCGnGpCtrlNoPathMgmt": jnxMbgPgwGtpCGnGpCtrlNoPathMgmt,
       "jnxMbgPgwGtpCGnGpCtrlIfName": jnxMbgPgwGtpCGnGpCtrlIfName,
       "jnxMbgPgwGtpCGnGpCtrlIfRtbId": jnxMbgPgwGtpCGnGpCtrlIfRtbId,
       "jnxMbgPgwGtpCGnGpCtrlIPv4Addr": jnxMbgPgwGtpCGnGpCtrlIPv4Addr,
       "jnxMbgPgwGtpCGnGpCtrlIPv6Addr": jnxMbgPgwGtpCGnGpCtrlIPv6Addr,
       "jnxMbgPgwGtpCGnGpDataN3Reqs": jnxMbgPgwGtpCGnGpDataN3Reqs,
       "jnxMbgPgwGtpCGnGpDataT3Resp": jnxMbgPgwGtpCGnGpDataT3Resp,
       "jnxMbgPgwGtpCGnGpDataEchIntr": jnxMbgPgwGtpCGnGpDataEchIntr,
       "jnxMbgPgwGtpCGnGpDataNoPathMgmt": jnxMbgPgwGtpCGnGpDataNoPathMgmt,
       "jnxMbgPgwGtpCGnGpDataIfName": jnxMbgPgwGtpCGnGpDataIfName,
       "jnxMbgPgwGtpCGnGpDataIfRtbId": jnxMbgPgwGtpCGnGpDataIfRtbId,
       "jnxMbgPgwGtpCGnGpDataIPv4Addr": jnxMbgPgwGtpCGnGpDataIPv4Addr,
       "jnxMbgPgwGtpCGnGpDataIPv6Addr": jnxMbgPgwGtpCGnGpDataIPv6Addr,
       "jnxMbgPgwGtpCS5S8GlblCfgGroup": jnxMbgPgwGtpCS5S8GlblCfgGroup,
       "jnxMbgPgwGtpCS5S8GWName": jnxMbgPgwGtpCS5S8GWName,
       "jnxMbgPgwGtpCS5S8PeerHistory": jnxMbgPgwGtpCS5S8PeerHistory,
       "jnxMbgPgwGtpCS5S8N3Reqs": jnxMbgPgwGtpCS5S8N3Reqs,
       "jnxMbgPgwGtpCS5S8T3Resp": jnxMbgPgwGtpCS5S8T3Resp,
       "jnxMbgPgwGtpCS5S8CtrlEchIntr": jnxMbgPgwGtpCS5S8CtrlEchIntr,
       "jnxMbgPgwGtpCS5S8CtrlNoPathMgmt": jnxMbgPgwGtpCS5S8CtrlNoPathMgmt,
       "jnxMbgPgwGtpCS5S8CtrlIfName": jnxMbgPgwGtpCS5S8CtrlIfName,
       "jnxMbgPgwGtpCS5S8CtrlIfRtbId": jnxMbgPgwGtpCS5S8CtrlIfRtbId,
       "jnxMbgPgwGtpCS5S8CtrlIPv4Addr": jnxMbgPgwGtpCS5S8CtrlIPv4Addr,
       "jnxMbgPgwGtpCS5S8CtrlIPv6Addr": jnxMbgPgwGtpCS5S8CtrlIPv6Addr,
       "jnxMbgPgwGtpCS5S8DataN3Reqs": jnxMbgPgwGtpCS5S8DataN3Reqs,
       "jnxMbgPgwGtpCS5S8DataT3Resp": jnxMbgPgwGtpCS5S8DataT3Resp,
       "jnxMbgPgwGtpCS5S8DataEchIntr": jnxMbgPgwGtpCS5S8DataEchIntr,
       "jnxMbgPgwGtpCS5S8DataNoPathMgmt": jnxMbgPgwGtpCS5S8DataNoPathMgmt,
       "jnxMbgPgwGtpCS5S8DataIfName": jnxMbgPgwGtpCS5S8DataIfName,
       "jnxMbgPgwGtpCS5S8DataIfRtbId": jnxMbgPgwGtpCS5S8DataIfRtbId,
       "jnxMbgPgwGtpCS5S8DataIPv4Addr": jnxMbgPgwGtpCS5S8DataIPv4Addr,
       "jnxMbgPgwGtpCS5S8DataIPv6Addr": jnxMbgPgwGtpCS5S8DataIPv6Addr,
       "jnxMbgPgwGtpV2Stats": jnxMbgPgwGtpV2Stats,
       "jnxMbgPgwV2NumMsgRx": jnxMbgPgwV2NumMsgRx,
       "jnxMbgPgwV2NumBytesRx": jnxMbgPgwV2NumBytesRx,
       "jnxMbgPgwUnSupportedMsg": jnxMbgPgwUnSupportedMsg,
       "jnxMbgPgwProtocolErr": jnxMbgPgwProtocolErr,
       "jnxMbgPgwT3RespTmrExp": jnxMbgPgwT3RespTmrExp,
       "jnxMbgPgwmsgRedirectRX": jnxMbgPgwmsgRedirectRX,
       "jnxMbgPgwmsgRedirectTX": jnxMbgPgwmsgRedirectTX,
       "jnxMbgPgwCreateSessReqRx": jnxMbgPgwCreateSessReqRx,
       "jnxMbgPgwCreateSessRspRx": jnxMbgPgwCreateSessRspRx,
       "jnxMbgPgwModBrReqRx": jnxMbgPgwModBrReqRx,
       "jnxMbgPgwModBrRspRx": jnxMbgPgwModBrRspRx,
       "jnxMbgPgwDelSessReqRx": jnxMbgPgwDelSessReqRx,
       "jnxMbgPgwDelSessRspRx": jnxMbgPgwDelSessRspRx,
       "jnxMbgPgwCngNotifReqRx": jnxMbgPgwCngNotifReqRx,
       "jnxMbgPgwCngNotifRspRx": jnxMbgPgwCngNotifRspRx,
       "jnxMbgPgwModBrCmdRx": jnxMbgPgwModBrCmdRx,
       "jnxMbgPgwModBrFlrIndRx": jnxMbgPgwModBrFlrIndRx,
       "jnxMbgPgwDelBrCmdRx": jnxMbgPgwDelBrCmdRx,
       "jnxMbgPgwDelBrFlrIndRx": jnxMbgPgwDelBrFlrIndRx,
       "jnxMbgPgwBrResCmdRx": jnxMbgPgwBrResCmdRx,
       "jnxMbgPgwBrResFlrIndRx": jnxMbgPgwBrResFlrIndRx,
       "jnxMbgPgwDlDataNotiFlrIndRx": jnxMbgPgwDlDataNotiFlrIndRx,
       "jnxMbgPgwTraceSessActRx": jnxMbgPgwTraceSessActRx,
       "jnxMbgPgwTraceSessDeactRx": jnxMbgPgwTraceSessDeactRx,
       "jnxMbgPgwCrtBrReqRx": jnxMbgPgwCrtBrReqRx,
       "jnxMbgPgwCrtBrRspRx": jnxMbgPgwCrtBrRspRx,
       "jnxMbgPgwUpdBrReqRx": jnxMbgPgwUpdBrReqRx,
       "jnxMbgPgwUpdBrRspRx": jnxMbgPgwUpdBrRspRx,
       "jnxMbgPgwDelBrReqRx": jnxMbgPgwDelBrReqRx,
       "jnxMbgPgwDelBrRspRx": jnxMbgPgwDelBrRspRx,
       "jnxMbgPgwDelConnSetReqRx": jnxMbgPgwDelConnSetReqRx,
       "jnxMbgPgwDelConnSetRspRx": jnxMbgPgwDelConnSetRspRx,
       "jnxMbgPgwDlDataNotifRx": jnxMbgPgwDlDataNotifRx,
       "jnxMbgPgwDlDataAckRx": jnxMbgPgwDlDataAckRx,
       "jnxMbgPgwUpdConnSetReqRx": jnxMbgPgwUpdConnSetReqRx,
       "jnxMbgPgwUpdConnSetRspRx": jnxMbgPgwUpdConnSetRspRx,
       "jnxMbgPgwV2EchoReqRx": jnxMbgPgwV2EchoReqRx,
       "jnxMbgPgwV2EchoRespRx": jnxMbgPgwV2EchoRespRx,
       "jnxMbgPgwGtpV2ICsPage": jnxMbgPgwGtpV2ICsPage,
       "jnxMbgPgwGtpV2ICsReqAccept": jnxMbgPgwGtpV2ICsReqAccept,
       "jnxMbgPgwGtpV2ICsAcceptPart": jnxMbgPgwGtpV2ICsAcceptPart,
       "jnxMbgPgwGtpV2ICsNewPTSubLT": jnxMbgPgwGtpV2ICsNewPTSubLT,
       "jnxMbgPgwGtpV2ICsNewPTNPref": jnxMbgPgwGtpV2ICsNewPTNPref,
       "jnxMbgPgwGtpV2ICsNewPTSIAddrbr": jnxMbgPgwGtpV2ICsNewPTSIAddrbr,
       "jnxMbgPgwGtpV2ICsCtxNotFnd": jnxMbgPgwGtpV2ICsCtxNotFnd,
       "jnxMbgPgwGtpV2ICsInvMsgFmt": jnxMbgPgwGtpV2ICsInvMsgFmt,
       "jnxMbgPgwGtpV2ICsVerNotSupp": jnxMbgPgwGtpV2ICsVerNotSupp,
       "jnxMbgPgwGtpV2ICsInvLen": jnxMbgPgwGtpV2ICsInvLen,
       "jnxMbgPgwGtpV2ICsServNotSupp": jnxMbgPgwGtpV2ICsServNotSupp,
       "jnxMbgPgwGtpV2ICsManIEIncorr": jnxMbgPgwGtpV2ICsManIEIncorr,
       "jnxMbgPgwGtpV2ICsManIEMiss": jnxMbgPgwGtpV2ICsManIEMiss,
       "jnxMbgPgwGtpV2ICsOptIEIncorr": jnxMbgPgwGtpV2ICsOptIEIncorr,
       "jnxMbgPgwGtpV2ICsSysFail": jnxMbgPgwGtpV2ICsSysFail,
       "jnxMbgPgwGtpV2ICsNoRes": jnxMbgPgwGtpV2ICsNoRes,
       "jnxMbgPgwGtpV2ICsTFTSMANTErr": jnxMbgPgwGtpV2ICsTFTSMANTErr,
       "jnxMbgPgwGtpV2ICsTFTSysErr": jnxMbgPgwGtpV2ICsTFTSysErr,
       "jnxMbgPgwGtpV2ICsPktFltrsMantErr": jnxMbgPgwGtpV2ICsPktFltrsMantErr,
       "jnxMbgPgwGtpV2ICsPktFltrSynErr": jnxMbgPgwGtpV2ICsPktFltrSynErr,
       "jnxMbgPgwGtpV2ICsMissUnkownAPN": jnxMbgPgwGtpV2ICsMissUnkownAPN,
       "jnxMbgPgwGtpV2ICsUnexpRepeatIE": jnxMbgPgwGtpV2ICsUnexpRepeatIE,
       "jnxMbgPgwGtpV2ICsGREKeyNotFnd": jnxMbgPgwGtpV2ICsGREKeyNotFnd,
       "jnxMbgPgwGtpV2ICsRelocFail": jnxMbgPgwGtpV2ICsRelocFail,
       "jnxMbgPgwGtpV2ICsDeniedINRat": jnxMbgPgwGtpV2ICsDeniedINRat,
       "jnxMbgPgwGtpV2ICsPTNotSupp": jnxMbgPgwGtpV2ICsPTNotSupp,
       "jnxMbgPgwGtpV2ICsAllDynAddrOcc": jnxMbgPgwGtpV2ICsAllDynAddrOcc,
       "jnxMbgPgwGtpV2ICsNOTFTUECTXEXIS": jnxMbgPgwGtpV2ICsNOTFTUECTXEXIS,
       "jnxMbgPgwGtpV2ICsProtoNotSupp": jnxMbgPgwGtpV2ICsProtoNotSupp,
       "jnxMbgPgwGtpV2ICsUENotResp": jnxMbgPgwGtpV2ICsUENotResp,
       "jnxMbgPgwGtpV2ICsUERefuses": jnxMbgPgwGtpV2ICsUERefuses,
       "jnxMbgPgwGtpV2ICsServDenied": jnxMbgPgwGtpV2ICsServDenied,
       "jnxMbgPgwGtpV2ICsUnablePageUE": jnxMbgPgwGtpV2ICsUnablePageUE,
       "jnxMbgPgwGtpV2ICsNoMem": jnxMbgPgwGtpV2ICsNoMem,
       "jnxMbgPgwGtpV2ICsUserAUTHFail": jnxMbgPgwGtpV2ICsUserAUTHFail,
       "jnxMbgPgwGtpV2ICsAPNAccessDenied": jnxMbgPgwGtpV2ICsAPNAccessDenied,
       "jnxMbgPgwGtpV2ICsReqRej": jnxMbgPgwGtpV2ICsReqRej,
       "jnxMbgPgwV2NumMsgTx": jnxMbgPgwV2NumMsgTx,
       "jnxMbgPgwV2NumBytesTx": jnxMbgPgwV2NumBytesTx,
       "jnxMbgPgwCreateSessReqTx": jnxMbgPgwCreateSessReqTx,
       "jnxMbgPgwCreateSessRspTx": jnxMbgPgwCreateSessRspTx,
       "jnxMbgPgwModBrReqTx": jnxMbgPgwModBrReqTx,
       "jnxMbgPgwModBrRspTx": jnxMbgPgwModBrRspTx,
       "jnxMbgPgwDelSessReqTx": jnxMbgPgwDelSessReqTx,
       "jnxMbgPgwDelSessRspTx": jnxMbgPgwDelSessRspTx,
       "jnxMbgPgwCngNotifReqTx": jnxMbgPgwCngNotifReqTx,
       "jnxMbgPgwCngNotifRspTx": jnxMbgPgwCngNotifRspTx,
       "jnxMbgPgwModBrCmdTx": jnxMbgPgwModBrCmdTx,
       "jnxMbgPgwModBrFlrIndTx": jnxMbgPgwModBrFlrIndTx,
       "jnxMbgPgwDelBrCmdTx": jnxMbgPgwDelBrCmdTx,
       "jnxMbgPgwDelBrFlrIndTx": jnxMbgPgwDelBrFlrIndTx,
       "jnxMbgPgwBrResCmdTx": jnxMbgPgwBrResCmdTx,
       "jnxMbgPgwBrResFlrIndTx": jnxMbgPgwBrResFlrIndTx,
       "jnxMbgPgwDlDataNotiFlrIndTx": jnxMbgPgwDlDataNotiFlrIndTx,
       "jnxMbgPgwTraceSessActTx": jnxMbgPgwTraceSessActTx,
       "jnxMbgPgwTraceSessDeactTx": jnxMbgPgwTraceSessDeactTx,
       "jnxMbgPgwCrtBrReqTx": jnxMbgPgwCrtBrReqTx,
       "jnxMbgPgwCrtBrRspTx": jnxMbgPgwCrtBrRspTx,
       "jnxMbgPgwUpdBrReqTx": jnxMbgPgwUpdBrReqTx,
       "jnxMbgPgwUpdBrRspTx": jnxMbgPgwUpdBrRspTx,
       "jnxMbgPgwDelBrReqTx": jnxMbgPgwDelBrReqTx,
       "jnxMbgPgwDelBrRspTx": jnxMbgPgwDelBrRspTx,
       "jnxMbgPgwDelConnSetReqTx": jnxMbgPgwDelConnSetReqTx,
       "jnxMbgPgwDelConnSetRspTx": jnxMbgPgwDelConnSetRspTx,
       "jnxMbgPgwDlDataNotifTx": jnxMbgPgwDlDataNotifTx,
       "jnxMbgPgwDlDataAckTx": jnxMbgPgwDlDataAckTx,
       "jnxMbgPgwUpdConnSetReqTx": jnxMbgPgwUpdConnSetReqTx,
       "jnxMbgPgwUpdConnSetRspTx": jnxMbgPgwUpdConnSetRspTx,
       "jnxMbgPgwV2EchoReqTx": jnxMbgPgwV2EchoReqTx,
       "jnxMbgPgwV2EchoRespTx": jnxMbgPgwV2EchoRespTx,
       "jnxMbgPgwGtpV1Stats": jnxMbgPgwGtpV1Stats,
       "jnxMbgPgwV1NumMsgRx": jnxMbgPgwV1NumMsgRx,
       "jnxMbgPgwV1NumBytesRx": jnxMbgPgwV1NumBytesRx,
       "jnxMbgPgwV1UnSupportedMsg": jnxMbgPgwV1UnSupportedMsg,
       "jnxMbgPgwProtErr": jnxMbgPgwProtErr,
       "jnxMbgPgwV1T3RespTmrExp": jnxMbgPgwV1T3RespTmrExp,
       "jnxMbgPgwMsgRedirectRx": jnxMbgPgwMsgRedirectRx,
       "jnxMbgPgwMsgRedirectTx": jnxMbgPgwMsgRedirectTx,
       "jnxMbgPgwSuppExtHdrNot": jnxMbgPgwSuppExtHdrNot,
       "jnxMbgPgwV1EchoReqRx": jnxMbgPgwV1EchoReqRx,
       "jnxMbgPgwV1EchoRespRx": jnxMbgPgwV1EchoRespRx,
       "jnxMbgPgwCrtPdpCxtReqRx": jnxMbgPgwCrtPdpCxtReqRx,
       "jnxMbgPgwCrtPdpCxtRspRx": jnxMbgPgwCrtPdpCxtRspRx,
       "jnxMbgPgwUpdPdpCxtReqRx": jnxMbgPgwUpdPdpCxtReqRx,
       "jnxMbgPgwUpdPdpCxtRspRx": jnxMbgPgwUpdPdpCxtRspRx,
       "jnxMbgPgwDelPdpCxtReqRx": jnxMbgPgwDelPdpCxtReqRx,
       "jnxMbgPgwDelPdpCxtRspRx": jnxMbgPgwDelPdpCxtRspRx,
       "jnxMbgPgwCrtAAPdpCxtReqRx": jnxMbgPgwCrtAAPdpCxtReqRx,
       "jnxMbgPgwCrtAAPdpCxtRspRx": jnxMbgPgwCrtAAPdpCxtRspRx,
       "jnxMbgPgwDelAAPdpCxtReqRx": jnxMbgPgwDelAAPdpCxtReqRx,
       "jnxMbgPgwDelAAPdpCxtRspRx": jnxMbgPgwDelAAPdpCxtRspRx,
       "jnxMbgPgwErrorIndRx": jnxMbgPgwErrorIndRx,
       "jnxMbgPgwNotifReqRx": jnxMbgPgwNotifReqRx,
       "jnxMbgPgwNotifRspRx": jnxMbgPgwNotifRspRx,
       "jnxMbgPgwNotifRejReqRx": jnxMbgPgwNotifRejReqRx,
       "jnxMbgPgwNotifRejRspRx": jnxMbgPgwNotifRejRspRx,
       "jnxMbgPgwRtInfReqRx": jnxMbgPgwRtInfReqRx,
       "jnxMbgPgwRtInfRspRx": jnxMbgPgwRtInfRspRx,
       "jnxMbgPgwFailRptReqRx": jnxMbgPgwFailRptReqRx,
       "jnxMbgPgwFailRptRspRx": jnxMbgPgwFailRptRspRx,
       "jnxMbgPgwNotMSPresReqRx": jnxMbgPgwNotMSPresReqRx,
       "jnxMbgPgwNotMSPresRspRx": jnxMbgPgwNotMSPresRspRx,
       "jnxMbgPgwGTPICsReqAccepted": jnxMbgPgwGTPICsReqAccepted,
       "jnxMbgPgwGTPICsNonExist": jnxMbgPgwGTPICsNonExist,
       "jnxMbgPgwGTPICsInvMsgFmt": jnxMbgPgwGTPICsInvMsgFmt,
       "jnxMbgPgwGTPICsIMSINotKnown": jnxMbgPgwGTPICsIMSINotKnown,
       "jnxMbgPgwGTPICsMSGRPSDetach": jnxMbgPgwGTPICsMSGRPSDetach,
       "jnxMbgPgwGTPICsMSNotGRPSResp": jnxMbgPgwGTPICsMSNotGRPSResp,
       "jnxMbgPgwGTPICsMSRefuses": jnxMbgPgwGTPICsMSRefuses,
       "jnxMbgPgwGTPICsVerNotSupp": jnxMbgPgwGTPICsVerNotSupp,
       "jnxMbgPgwGTPICsNoRes": jnxMbgPgwGTPICsNoRes,
       "jnxMbgPgwGTPICsServNotSupp": jnxMbgPgwGTPICsServNotSupp,
       "jnxMbgPgwGTPICsManIEIncrt": jnxMbgPgwGTPICsManIEIncrt,
       "jnxMbgPgwGTPICsManIEMiss": jnxMbgPgwGTPICsManIEMiss,
       "jnxMbgPgwGTPICsOptIEIncrt": jnxMbgPgwGTPICsOptIEIncrt,
       "jnxMbgPgwGTPICsSysFail": jnxMbgPgwGTPICsSysFail,
       "jnxMbgPgwGTPICsRoamRestrict": jnxMbgPgwGTPICsRoamRestrict,
       "jnxMbgPgwGTPICsPTMSISigMismatch": jnxMbgPgwGTPICsPTMSISigMismatch,
       "jnxMbgPgwGTPICsGPRSConnSupp": jnxMbgPgwGTPICsGPRSConnSupp,
       "jnxMbgPgwGTPICsAuthFail": jnxMbgPgwGTPICsAuthFail,
       "jnxMbgPgwGTPICsUserAuthFail": jnxMbgPgwGTPICsUserAuthFail,
       "jnxMbgPgwGTPV1ICsCtxNotFnd": jnxMbgPgwGTPV1ICsCtxNotFnd,
       "jnxMbgPgwGTPV1ICsAllDynPDPAddr": jnxMbgPgwGTPV1ICsAllDynPDPAddr,
       "jnxMbgPgwGTPV1ICsNoMem": jnxMbgPgwGTPV1ICsNoMem,
       "jnxMbgPgwGTPV1ICsRelocFail": jnxMbgPgwGTPV1ICsRelocFail,
       "jnxMbgPgwGTPV1ICsUnkManExthdr": jnxMbgPgwGTPV1ICsUnkManExthdr,
       "jnxMbgPgwGTPV1ICsSMANTTFTErr1": jnxMbgPgwGTPV1ICsSMANTTFTErr1,
       "jnxMbgPgwGTPV1ICsSYNTFTErr2": jnxMbgPgwGTPV1ICsSYNTFTErr2,
       "jnxMbgPgwGTPV1ICsSMNTPktFltrErr1": jnxMbgPgwGTPV1ICsSMNTPktFltrErr1,
       "jnxMbgPgwGTPV1ICsSYNPktFltrErr2": jnxMbgPgwGTPV1ICsSYNPktFltrErr2,
       "jnxMbgPgwGTPV1ICsMissUnknownAPN": jnxMbgPgwGTPV1ICsMissUnknownAPN,
       "jnxMbgPgwGTPV1ICsUnknownPDPAddr": jnxMbgPgwGTPV1ICsUnknownPDPAddr,
       "jnxMbgPgwGTPV1ICsNoTFTCtxExist": jnxMbgPgwGTPV1ICsNoTFTCtxExist,
       "jnxMbgPgwV1NumMsgTx": jnxMbgPgwV1NumMsgTx,
       "jnxMbgPgwV1NumBytesTx": jnxMbgPgwV1NumBytesTx,
       "jnxMbgPgwV1EchoReqTx": jnxMbgPgwV1EchoReqTx,
       "jnxMbgPgwV1EchoRespTx": jnxMbgPgwV1EchoRespTx,
       "jnxMbgPgwCrtPdpCxtReqTx": jnxMbgPgwCrtPdpCxtReqTx,
       "jnxMbgPgwCrtPdpCxtRspTx": jnxMbgPgwCrtPdpCxtRspTx,
       "jnxMbgPgwUpdPdpCxtReqTx": jnxMbgPgwUpdPdpCxtReqTx,
       "jnxMbgPgwUpdPdpCxtRspTx": jnxMbgPgwUpdPdpCxtRspTx,
       "jnxMbgPgwDelPdpCxtReqTx": jnxMbgPgwDelPdpCxtReqTx,
       "jnxMbgPgwDelPdpCxtRspTx": jnxMbgPgwDelPdpCxtRspTx,
       "jnxMbgPgwCrtAAPdpCxtReqTx": jnxMbgPgwCrtAAPdpCxtReqTx,
       "jnxMbgPgwCrtAAPdpCxtRspTx": jnxMbgPgwCrtAAPdpCxtRspTx,
       "jnxMbgPgwDelAAPdpCxtReqTx": jnxMbgPgwDelAAPdpCxtReqTx,
       "jnxMbgPgwDelAAPdpCxtRspTx": jnxMbgPgwDelAAPdpCxtRspTx,
       "jnxMbgPgwErrorIndTx": jnxMbgPgwErrorIndTx,
       "jnxMbgPgwNotifReqTx": jnxMbgPgwNotifReqTx,
       "jnxMbgPgwNotifRspTx": jnxMbgPgwNotifRspTx,
       "jnxMbgPgwNotifRejReqTx": jnxMbgPgwNotifRejReqTx,
       "jnxMbgPgwNotifRejRspTx": jnxMbgPgwNotifRejRspTx,
       "jnxMbgPgwRtInfReqTx": jnxMbgPgwRtInfReqTx,
       "jnxMbgPgwRtInfRspTx": jnxMbgPgwRtInfRspTx,
       "jnxMbgPgwFailRptReqTx": jnxMbgPgwFailRptReqTx,
       "jnxMbgPgwFailRptRspTx": jnxMbgPgwFailRptRspTx,
       "jnxMbgPgwNotMSPresReqTx": jnxMbgPgwNotMSPresReqTx,
       "jnxMbgPgwNotMSPresRspTx": jnxMbgPgwNotMSPresRspTx,
       "jnxMbgPgwGtpPeerStatsTable": jnxMbgPgwGtpPeerStatsTable,
       "jnxMbgPgwGtpPeerEntry": jnxMbgPgwGtpPeerEntry,
       "jnxMbgPgwGtpPeerRmtAddr": jnxMbgPgwGtpPeerRmtAddr,
       "jnxMbgPgwGtpPeerLclAddr": jnxMbgPgwGtpPeerLclAddr,
       "jnxMbgPgwGtpPeerRtgInst": jnxMbgPgwGtpPeerRtgInst,
       "jnxMbgPgwGtpDropCounter": jnxMbgPgwGtpDropCounter,
       "jnxMbgPgwGtpPktAllocFail": jnxMbgPgwGtpPktAllocFail,
       "jnxMbgPgwGtpPktSendFail": jnxMbgPgwGtpPktSendFail,
       "jnxMbgPgwGtpIPVerErrRx": jnxMbgPgwGtpIPVerErrRx,
       "jnxMbgPgwGtpIPProtoErrRx": jnxMbgPgwGtpIPProtoErrRx,
       "jnxMbgPgwGtpPktLenErrRx": jnxMbgPgwGtpPktLenErrRx,
       "jnxMbgPgwGtpUnkMsgRx": jnxMbgPgwGtpUnkMsgRx,
       "jnxMbgPgwGtpMemAllocFailed": jnxMbgPgwGtpMemAllocFailed,
       "jnxMbgPgwGtpNotificationVars": jnxMbgPgwGtpNotificationVars,
       "jnxMbgPgwGtpPeerName": jnxMbgPgwGtpPeerName,
       "jnxMbgPgwGtpAlarmThrshld": jnxMbgPgwGtpAlarmThrshld,
       "jnxMbgPgwGtpAlarmState": jnxMbgPgwGtpAlarmState,
       "jnxMbgPgwGtpAlarmStatCounter": jnxMbgPgwGtpAlarmStatCounter,
       "jnxMbgPgwGtpInterfaceType": jnxMbgPgwGtpInterfaceType,
       "jnxMbgPgwGtpGwName": jnxMbgPgwGtpGwName,
       "jnxMbgPgwGtpGwIndex": jnxMbgPgwGtpGwIndex,
       "jnxMbgPgwGtpV0Stats": jnxMbgPgwGtpV0Stats,
       "jnxMbgPgwV0NumMsgRx": jnxMbgPgwV0NumMsgRx,
       "jnxMbgPgwV0NumBytesRx": jnxMbgPgwV0NumBytesRx,
       "jnxMbgPgwV0UnSupportedMsg": jnxMbgPgwV0UnSupportedMsg,
       "jnxMbgPgwV0ProtErr": jnxMbgPgwV0ProtErr,
       "jnxMbgPgwV0T3RespTmrExp": jnxMbgPgwV0T3RespTmrExp,
       "jnxMbgPgwV0MsgRedirectRx": jnxMbgPgwV0MsgRedirectRx,
       "jnxMbgPgwV0MsgRedirectTx": jnxMbgPgwV0MsgRedirectTx,
       "jnxMbgPgwV0SuppExtHdrNot": jnxMbgPgwV0SuppExtHdrNot,
       "jnxMbgPgwV0EchoReqRx": jnxMbgPgwV0EchoReqRx,
       "jnxMbgPgwV0EchoRespRx": jnxMbgPgwV0EchoRespRx,
       "jnxMbgPgwV0CrtPdpCxtReqRx": jnxMbgPgwV0CrtPdpCxtReqRx,
       "jnxMbgPgwV0CrtPdpCxtRspRx": jnxMbgPgwV0CrtPdpCxtRspRx,
       "jnxMbgPgwV0UpdPdpCxtReqRx": jnxMbgPgwV0UpdPdpCxtReqRx,
       "jnxMbgPgwV0UpdPdpCxtRspRx": jnxMbgPgwV0UpdPdpCxtRspRx,
       "jnxMbgPgwV0DelPdpCxtReqRx": jnxMbgPgwV0DelPdpCxtReqRx,
       "jnxMbgPgwV0DelPdpCxtRspRx": jnxMbgPgwV0DelPdpCxtRspRx,
       "jnxMbgPgwV0CrtAAPdpCxtReqRx": jnxMbgPgwV0CrtAAPdpCxtReqRx,
       "jnxMbgPgwV0CrtAAPdpCxtRspRx": jnxMbgPgwV0CrtAAPdpCxtRspRx,
       "jnxMbgPgwV0DelAAPdpCxtReqRx": jnxMbgPgwV0DelAAPdpCxtReqRx,
       "jnxMbgPgwV0DelAAPdpCxtRspRx": jnxMbgPgwV0DelAAPdpCxtRspRx,
       "jnxMbgPgwV0ErrorIndRx": jnxMbgPgwV0ErrorIndRx,
       "jnxMbgPgwV0NotifReqRx": jnxMbgPgwV0NotifReqRx,
       "jnxMbgPgwV0NotifRspRx": jnxMbgPgwV0NotifRspRx,
       "jnxMbgPgwV0NotifRejReqRx": jnxMbgPgwV0NotifRejReqRx,
       "jnxMbgPgwV0NotifRejRspRx": jnxMbgPgwV0NotifRejRspRx,
       "jnxMbgPgwV0RtInfReqRx": jnxMbgPgwV0RtInfReqRx,
       "jnxMbgPgwV0RtInfRspRx": jnxMbgPgwV0RtInfRspRx,
       "jnxMbgPgwV0FailRptReqRx": jnxMbgPgwV0FailRptReqRx,
       "jnxMbgPgwV0FailRptRspRx": jnxMbgPgwV0FailRptRspRx,
       "jnxMbgPgwV0NotMSPresReqRx": jnxMbgPgwV0NotMSPresReqRx,
       "jnxMbgPgwV0NotMSPresRspRx": jnxMbgPgwV0NotMSPresRspRx,
       "jnxMbgPgwGTPV0ICsReqAccepted": jnxMbgPgwGTPV0ICsReqAccepted,
       "jnxMbgPgwGTPV0ICsNonExist": jnxMbgPgwGTPV0ICsNonExist,
       "jnxMbgPgwGTPV0ICsInvMsgFmt": jnxMbgPgwGTPV0ICsInvMsgFmt,
       "jnxMbgPgwGTPV0ICsIMSINotKnown": jnxMbgPgwGTPV0ICsIMSINotKnown,
       "jnxMbgPgwGTPV0ICsMSGRPSDetach": jnxMbgPgwGTPV0ICsMSGRPSDetach,
       "jnxMbgPgwGTPV0ICsMSNotGRPSResp": jnxMbgPgwGTPV0ICsMSNotGRPSResp,
       "jnxMbgPgwGTPV0ICsMSRefuses": jnxMbgPgwGTPV0ICsMSRefuses,
       "jnxMbgPgwGTPV0ICsVerNotSupp": jnxMbgPgwGTPV0ICsVerNotSupp,
       "jnxMbgPgwGTPV0ICsNoRes": jnxMbgPgwGTPV0ICsNoRes,
       "jnxMbgPgwGTPV0ICsServNotSupp": jnxMbgPgwGTPV0ICsServNotSupp,
       "jnxMbgPgwGTPV0ICsManIEIncrt": jnxMbgPgwGTPV0ICsManIEIncrt,
       "jnxMbgPgwGTPV0ICsManIEMiss": jnxMbgPgwGTPV0ICsManIEMiss,
       "jnxMbgPgwGTPV0ICsOptIEIncrt": jnxMbgPgwGTPV0ICsOptIEIncrt,
       "jnxMbgPgwGTPV0ICsSysFail": jnxMbgPgwGTPV0ICsSysFail,
       "jnxMbgPgwGTPV0ICsRoamRestrict": jnxMbgPgwGTPV0ICsRoamRestrict,
       "jnxMbgPgwGTPV0ICsPTMSISigMismatch": jnxMbgPgwGTPV0ICsPTMSISigMismatch,
       "jnxMbgPgwGTPV0ICsGPRSConnSupp": jnxMbgPgwGTPV0ICsGPRSConnSupp,
       "jnxMbgPgwGTPV0ICsAuthFail": jnxMbgPgwGTPV0ICsAuthFail,
       "jnxMbgPgwGTPV0ICsUserAuthFail": jnxMbgPgwGTPV0ICsUserAuthFail,
       "jnxMbgPgwV0NumMsgTx": jnxMbgPgwV0NumMsgTx,
       "jnxMbgPgwV0NumBytesTx": jnxMbgPgwV0NumBytesTx,
       "jnxMbgPgwV0EchoReqTx": jnxMbgPgwV0EchoReqTx,
       "jnxMbgPgwV0EchoRespTx": jnxMbgPgwV0EchoRespTx,
       "jnxMbgPgwV0CrtPdpCxtReqTx": jnxMbgPgwV0CrtPdpCxtReqTx,
       "jnxMbgPgwV0CrtPdpCxtRspTx": jnxMbgPgwV0CrtPdpCxtRspTx,
       "jnxMbgPgwV0UpdPdpCxtReqTx": jnxMbgPgwV0UpdPdpCxtReqTx,
       "jnxMbgPgwV0UpdPdpCxtRspTx": jnxMbgPgwV0UpdPdpCxtRspTx,
       "jnxMbgPgwV0DelPdpCxtReqTx": jnxMbgPgwV0DelPdpCxtReqTx,
       "jnxMbgPgwV0DelPdpCxtRspTx": jnxMbgPgwV0DelPdpCxtRspTx,
       "jnxMbgPgwV0CrtAAPdpCxtReqTx": jnxMbgPgwV0CrtAAPdpCxtReqTx,
       "jnxMbgPgwV0CrtAAPdpCxtRspTx": jnxMbgPgwV0CrtAAPdpCxtRspTx,
       "jnxMbgPgwV0DelAAPdpCxtReqTx": jnxMbgPgwV0DelAAPdpCxtReqTx,
       "jnxMbgPgwV0DelAAPdpCxtRspTx": jnxMbgPgwV0DelAAPdpCxtRspTx,
       "jnxMbgPgwV0ErrorIndTx": jnxMbgPgwV0ErrorIndTx,
       "jnxMbgPgwV0NotifReqTx": jnxMbgPgwV0NotifReqTx,
       "jnxMbgPgwV0NotifRspTx": jnxMbgPgwV0NotifRspTx,
       "jnxMbgPgwV0NotifRejReqTx": jnxMbgPgwV0NotifRejReqTx,
       "jnxMbgPgwV0NotifRejRspTx": jnxMbgPgwV0NotifRejRspTx,
       "jnxMbgPgwV0RtInfReqTx": jnxMbgPgwV0RtInfReqTx,
       "jnxMbgPgwV0RtInfRspTx": jnxMbgPgwV0RtInfRspTx,
       "jnxMbgPgwV0FailRptReqTx": jnxMbgPgwV0FailRptReqTx,
       "jnxMbgPgwV0FailRptRspTx": jnxMbgPgwV0FailRptRspTx,
       "jnxMbgPgwV0NotMSPresReqTx": jnxMbgPgwV0NotMSPresReqTx,
       "jnxMbgPgwV0NotMSPresRspTx": jnxMbgPgwV0NotMSPresRspTx,
       "jnxMbgPgwGtpCPerPeerStatsTable": jnxMbgPgwGtpCPerPeerStatsTable,
       "jnxMbgPgwGtpPerPeerStatsEntry": jnxMbgPgwGtpPerPeerStatsEntry,
       "jnxMbgPgwPPGtpRmtAddr": jnxMbgPgwPPGtpRmtAddr,
       "jnxMbgPgwPPGtpLclAddr": jnxMbgPgwPPGtpLclAddr,
       "jnxMbgPgwPPGtpRtgInst": jnxMbgPgwPPGtpRtgInst,
       "jnxMbgPgwPPRxPacketsDropped": jnxMbgPgwPPRxPacketsDropped,
       "jnxMbgPgwPPPacketAllocFail": jnxMbgPgwPPPacketAllocFail,
       "jnxMbgPgwPPPacketSendFail": jnxMbgPgwPPPacketSendFail,
       "jnxMbgPgwPPIPVerErrRx": jnxMbgPgwPPIPVerErrRx,
       "jnxMbgPgwPPIPProtoErrRx": jnxMbgPgwPPIPProtoErrRx,
       "jnxMbgPgwPPGTPPortErrRx": jnxMbgPgwPPGTPPortErrRx,
       "jnxMbgPgwPPGTPUnknVerRx": jnxMbgPgwPPGTPUnknVerRx,
       "jnxMbgPgwPPPcktLenErrRx": jnxMbgPgwPPPcktLenErrRx,
       "jnxMbgPgwPPUnknMsgRx": jnxMbgPgwPPUnknMsgRx,
       "jnxMbgPgwPPProtocolErrRx": jnxMbgPgwPPProtocolErrRx,
       "jnxMbgPgwPPV2UnSupportedMsgRx": jnxMbgPgwPPV2UnSupportedMsgRx,
       "jnxMbgPgwPPV2T3RespTmrExpRx": jnxMbgPgwPPV2T3RespTmrExpRx,
       "jnxMbgPgwPPV2GlbNumMsgRx": jnxMbgPgwPPV2GlbNumMsgRx,
       "jnxMbgPgwPPV2GlbNumMsgTx": jnxMbgPgwPPV2GlbNumMsgTx,
       "jnxMbgPgwPPV2GlbNumBytesRx": jnxMbgPgwPPV2GlbNumBytesRx,
       "jnxMbgPgwPPV2GlbNumBytesTx": jnxMbgPgwPPV2GlbNumBytesTx,
       "jnxMbgPgwPPV2GlbEchoReqRx": jnxMbgPgwPPV2GlbEchoReqRx,
       "jnxMbgPgwPPV2GlbEchoReqTx": jnxMbgPgwPPV2GlbEchoReqTx,
       "jnxMbgPgwPPV2GlbEchoRespRx": jnxMbgPgwPPV2GlbEchoRespRx,
       "jnxMbgPgwPPV2GlbEchoRespTx": jnxMbgPgwPPV2GlbEchoRespTx,
       "jnxMbgPgwPPV2VerNotSupRx": jnxMbgPgwPPV2VerNotSupRx,
       "jnxMbgPgwPPV2VerNotSupTx": jnxMbgPgwPPV2VerNotSupTx,
       "jnxMbgPgwPPV2CreateSessReqRx": jnxMbgPgwPPV2CreateSessReqRx,
       "jnxMbgPgwPPV2CreateSessReqTx": jnxMbgPgwPPV2CreateSessReqTx,
       "jnxMbgPgwPPV2CreateSessRspRx": jnxMbgPgwPPV2CreateSessRspRx,
       "jnxMbgPgwPPV2CreateSessRspTx": jnxMbgPgwPPV2CreateSessRspTx,
       "jnxMbgPgwPPV2ModBrReqRx": jnxMbgPgwPPV2ModBrReqRx,
       "jnxMbgPgwPPV2ModBrReqTx": jnxMbgPgwPPV2ModBrReqTx,
       "jnxMbgPgwPPV2ModBrRspRx": jnxMbgPgwPPV2ModBrRspRx,
       "jnxMbgPgwPPV2ModBrRspTx": jnxMbgPgwPPV2ModBrRspTx,
       "jnxMbgPgwPPV2DelSessReqRx": jnxMbgPgwPPV2DelSessReqRx,
       "jnxMbgPgwPPV2DelSessReqTx": jnxMbgPgwPPV2DelSessReqTx,
       "jnxMbgPgwPPV2DelSessRspRx": jnxMbgPgwPPV2DelSessRspRx,
       "jnxMbgPgwPPV2DelSessRspTx": jnxMbgPgwPPV2DelSessRspTx,
       "jnxMbgPgwPPV2CrtBrReqRx": jnxMbgPgwPPV2CrtBrReqRx,
       "jnxMbgPgwPPV2CrtBrReqTx": jnxMbgPgwPPV2CrtBrReqTx,
       "jnxMbgPgwPPV2CrtBrRspRx": jnxMbgPgwPPV2CrtBrRspRx,
       "jnxMbgPgwPPV2CrtBrRspTx": jnxMbgPgwPPV2CrtBrRspTx,
       "jnxMbgPgwPPV2UpdBrReqRx": jnxMbgPgwPPV2UpdBrReqRx,
       "jnxMbgPgwPPV2UpdBrReqTx": jnxMbgPgwPPV2UpdBrReqTx,
       "jnxMbgPgwPPV2UpdBrRspRx": jnxMbgPgwPPV2UpdBrRspRx,
       "jnxMbgPgwPPV2UpdBrRspTx": jnxMbgPgwPPV2UpdBrRspTx,
       "jnxMbgPgwPPV2DelBrReqRx": jnxMbgPgwPPV2DelBrReqRx,
       "jnxMbgPgwPPV2DelBrReqTx": jnxMbgPgwPPV2DelBrReqTx,
       "jnxMbgPgwPPV2DelBrRspRx": jnxMbgPgwPPV2DelBrRspRx,
       "jnxMbgPgwPPV2DelBrRspTx": jnxMbgPgwPPV2DelBrRspTx,
       "jnxMbgPgwPPV2DelConnSetReqRx": jnxMbgPgwPPV2DelConnSetReqRx,
       "jnxMbgPgwPPV2DelConnSetReqTx": jnxMbgPgwPPV2DelConnSetReqTx,
       "jnxMbgPgwPPV2DelConnSetRspRx": jnxMbgPgwPPV2DelConnSetRspRx,
       "jnxMbgPgwPPV2DelConnSetRspTx": jnxMbgPgwPPV2DelConnSetRspTx,
       "jnxMbgPgwPPV2UpdConnSetReqRx": jnxMbgPgwPPV2UpdConnSetReqRx,
       "jnxMbgPgwPPV2UpdConnSetReqTx": jnxMbgPgwPPV2UpdConnSetReqTx,
       "jnxMbgPgwPPV2UpdConnSetRspRx": jnxMbgPgwPPV2UpdConnSetRspRx,
       "jnxMbgPgwPPV2UpdConnSetRspTx": jnxMbgPgwPPV2UpdConnSetRspTx,
       "jnxMbgPgwPPV2ModBrCmdRx": jnxMbgPgwPPV2ModBrCmdRx,
       "jnxMbgPgwPPV2ModBrCmdTx": jnxMbgPgwPPV2ModBrCmdTx,
       "jnxMbgPgwPPV2ModBrFlrIndRx": jnxMbgPgwPPV2ModBrFlrIndRx,
       "jnxMbgPgwPPV2ModBrFlrIndTx": jnxMbgPgwPPV2ModBrFlrIndTx,
       "jnxMbgPgwPPV2DelBrCmdRx": jnxMbgPgwPPV2DelBrCmdRx,
       "jnxMbgPgwPPV2DelBrCmdTx": jnxMbgPgwPPV2DelBrCmdTx,
       "jnxMbgPgwPPV2DelBrFlrIndRx": jnxMbgPgwPPV2DelBrFlrIndRx,
       "jnxMbgPgwPPV2DelBrFlrIndTx": jnxMbgPgwPPV2DelBrFlrIndTx,
       "jnxMbgPgwPPV2BrResCmdRx": jnxMbgPgwPPV2BrResCmdRx,
       "jnxMbgPgwPPV2BrResCmdTx": jnxMbgPgwPPV2BrResCmdTx,
       "jnxMbgPgwPPV2BrResFlrIndRx": jnxMbgPgwPPV2BrResFlrIndRx,
       "jnxMbgPgwPPV2BrResFlrIndTx": jnxMbgPgwPPV2BrResFlrIndTx,
       "jnxMbgPgwPPV2RelAcsBrReqRx": jnxMbgPgwPPV2RelAcsBrReqRx,
       "jnxMbgPgwPPV2RelAcsBrReqTx": jnxMbgPgwPPV2RelAcsBrReqTx,
       "jnxMbgPgwPPV2RelAcsBrRespRx": jnxMbgPgwPPV2RelAcsBrRespRx,
       "jnxMbgPgwPPV2RelAcsBrRespTx": jnxMbgPgwPPV2RelAcsBrRespTx,
       "jnxMbgPgwPPV2CrIndTunReqRx": jnxMbgPgwPPV2CrIndTunReqRx,
       "jnxMbgPgwPPV2CrIndTunReqTx": jnxMbgPgwPPV2CrIndTunReqTx,
       "jnxMbgPgwPPV2CrIndTunRespRx": jnxMbgPgwPPV2CrIndTunRespRx,
       "jnxMbgPgwPPV2CrIndTunRespTx": jnxMbgPgwPPV2CrIndTunRespTx,
       "jnxMbgPgwPPV2DelIndTunReqRx": jnxMbgPgwPPV2DelIndTunReqRx,
       "jnxMbgPgwPPV2DelIndTunReqTx": jnxMbgPgwPPV2DelIndTunReqTx,
       "jnxMbgPgwPPV2DelIndTunRespRx": jnxMbgPgwPPV2DelIndTunRespRx,
       "jnxMbgPgwPPV2DelIndTunRespTx": jnxMbgPgwPPV2DelIndTunRespTx,
       "jnxMbgPgwPPV2DlDataNotifRx": jnxMbgPgwPPV2DlDataNotifRx,
       "jnxMbgPgwPPV2DlDataNotifTx": jnxMbgPgwPPV2DlDataNotifTx,
       "jnxMbgPgwPPV2DlDataAckRx": jnxMbgPgwPPV2DlDataAckRx,
       "jnxMbgPgwPPV2DlDataAckTx": jnxMbgPgwPPV2DlDataAckTx,
       "jnxMbgPgwPPV2DlDataNotiFlrIndRx": jnxMbgPgwPPV2DlDataNotiFlrIndRx,
       "jnxMbgPgwPPV2DlDataNotiFlrIndTx": jnxMbgPgwPPV2DlDataNotiFlrIndTx,
       "jnxMbgPgwPPV2StopPagingIndRx": jnxMbgPgwPPV2StopPagingIndRx,
       "jnxMbgPgwPPV2StopPagingIndTx": jnxMbgPgwPPV2StopPagingIndTx,
       "jnxMbgPgwPPV2ICsPageRx": jnxMbgPgwPPV2ICsPageRx,
       "jnxMbgPgwPPV2ICsPageTx": jnxMbgPgwPPV2ICsPageTx,
       "jnxMbgPgwPPV2ICsReqAcceptRx": jnxMbgPgwPPV2ICsReqAcceptRx,
       "jnxMbgPgwPPV2ICsReqAcceptTx": jnxMbgPgwPPV2ICsReqAcceptTx,
       "jnxMbgPgwPPV2ICsAcceptPartRx": jnxMbgPgwPPV2ICsAcceptPartRx,
       "jnxMbgPgwPPV2ICsAcceptPartTx": jnxMbgPgwPPV2ICsAcceptPartTx,
       "jnxMbgPgwPPV2ICsNewPTNPrefRx": jnxMbgPgwPPV2ICsNewPTNPrefRx,
       "jnxMbgPgwPPV2ICsNewPTNPrefTx": jnxMbgPgwPPV2ICsNewPTNPrefTx,
       "jnxMbgPgwPPV2ICsNewPTSIAdbrRx": jnxMbgPgwPPV2ICsNewPTSIAdbrRx,
       "jnxMbgPgwPPV2ICsNewPTSIAdbrTx": jnxMbgPgwPPV2ICsNewPTSIAdbrTx,
       "jnxMbgPgwPPV2ICsCtxNotFndRx": jnxMbgPgwPPV2ICsCtxNotFndRx,
       "jnxMbgPgwPPV2ICsCtxNotFndTx": jnxMbgPgwPPV2ICsCtxNotFndTx,
       "jnxMbgPgwPPV2ICsInvMsgFmtRx": jnxMbgPgwPPV2ICsInvMsgFmtRx,
       "jnxMbgPgwPPV2ICsInvMsgFmtTx": jnxMbgPgwPPV2ICsInvMsgFmtTx,
       "jnxMbgPgwPPV2ICsVerNotSuppRx": jnxMbgPgwPPV2ICsVerNotSuppRx,
       "jnxMbgPgwPPV2ICsVerNotSuppTx": jnxMbgPgwPPV2ICsVerNotSuppTx,
       "jnxMbgPgwPPV2ICsInvLenRx": jnxMbgPgwPPV2ICsInvLenRx,
       "jnxMbgPgwPPV2ICsInvLenTx": jnxMbgPgwPPV2ICsInvLenTx,
       "jnxMbgPgwPPV2ICsServNotSuppRx": jnxMbgPgwPPV2ICsServNotSuppRx,
       "jnxMbgPgwPPV2ICsServNotSuppTx": jnxMbgPgwPPV2ICsServNotSuppTx,
       "jnxMbgPgwPPV2ICsManIEIncorrRx": jnxMbgPgwPPV2ICsManIEIncorrRx,
       "jnxMbgPgwPPV2ICsManIEIncorrTx": jnxMbgPgwPPV2ICsManIEIncorrTx,
       "jnxMbgPgwPPV2ICsManIEMissRx": jnxMbgPgwPPV2ICsManIEMissRx,
       "jnxMbgPgwPPV2ICsManIEMissTx": jnxMbgPgwPPV2ICsManIEMissTx,
       "jnxMbgPgwPPV2ICsOptIEIncorrRx": jnxMbgPgwPPV2ICsOptIEIncorrRx,
       "jnxMbgPgwPPV2ICsOptIEIncorrTx": jnxMbgPgwPPV2ICsOptIEIncorrTx,
       "jnxMbgPgwPPV2ICsSysFailRx": jnxMbgPgwPPV2ICsSysFailRx,
       "jnxMbgPgwPPV2ICsSysFailTx": jnxMbgPgwPPV2ICsSysFailTx,
       "jnxMbgPgwPPV2ICsNoResRx": jnxMbgPgwPPV2ICsNoResRx,
       "jnxMbgPgwPPV2ICsNoResTx": jnxMbgPgwPPV2ICsNoResTx,
       "jnxMbgPgwPPV2ICsTFTSMANTErRx": jnxMbgPgwPPV2ICsTFTSMANTErRx,
       "jnxMbgPgwPPV2ICsTFTSMANTErTx": jnxMbgPgwPPV2ICsTFTSMANTErTx,
       "jnxMbgPgwPPV2ICsTFTSysErrRx": jnxMbgPgwPPV2ICsTFTSysErrRx,
       "jnxMbgPgwPPV2ICsTFTSysErrTx": jnxMbgPgwPPV2ICsTFTSysErrTx,
       "jnxMbgPgwPPV2ICsPkFltManErrRx": jnxMbgPgwPPV2ICsPkFltManErrRx,
       "jnxMbgPgwPPV2ICsPkFltManErrTx": jnxMbgPgwPPV2ICsPkFltManErrTx,
       "jnxMbgPgwPPV2ICsPkFltSynErrRx": jnxMbgPgwPPV2ICsPkFltSynErrRx,
       "jnxMbgPgwPPV2ICsPkFltSynErrTx": jnxMbgPgwPPV2ICsPkFltSynErrTx,
       "jnxMbgPgwPPV2ICsMisUnknAPNRx": jnxMbgPgwPPV2ICsMisUnknAPNRx,
       "jnxMbgPgwPPV2ICsMisUnknAPNTx": jnxMbgPgwPPV2ICsMisUnknAPNTx,
       "jnxMbgPgwPPV2ICsUnexpRptIERx": jnxMbgPgwPPV2ICsUnexpRptIERx,
       "jnxMbgPgwPPV2ICsUnexpRptIETx": jnxMbgPgwPPV2ICsUnexpRptIETx,
       "jnxMbgPgwPPV2ICsGREKeyNtFdRx": jnxMbgPgwPPV2ICsGREKeyNtFdRx,
       "jnxMbgPgwPPV2ICsGREKeyNtFdTx": jnxMbgPgwPPV2ICsGREKeyNtFdTx,
       "jnxMbgPgwPPV2ICsRelocFailRx": jnxMbgPgwPPV2ICsRelocFailRx,
       "jnxMbgPgwPPV2ICsRelocFailTx": jnxMbgPgwPPV2ICsRelocFailTx,
       "jnxMbgPgwPPV2ICsDeniedINRatRx": jnxMbgPgwPPV2ICsDeniedINRatRx,
       "jnxMbgPgwPPV2ICsDeniedINRatTx": jnxMbgPgwPPV2ICsDeniedINRatTx,
       "jnxMbgPgwPPV2ICsPTNotSuppRx": jnxMbgPgwPPV2ICsPTNotSuppRx,
       "jnxMbgPgwPPV2ICsPTNotSuppTx": jnxMbgPgwPPV2ICsPTNotSuppTx,
       "jnxMbgPgwPPV2ICsAllDynAdOccRx": jnxMbgPgwPPV2ICsAllDynAdOccRx,
       "jnxMbgPgwPPV2ICsAllDynAdOccTx": jnxMbgPgwPPV2ICsAllDynAdOccTx,
       "jnxMbgPgwPPV2ICsNOTFTUECTXRx": jnxMbgPgwPPV2ICsNOTFTUECTXRx,
       "jnxMbgPgwPPV2ICsNOTFTUECTXTx": jnxMbgPgwPPV2ICsNOTFTUECTXTx,
       "jnxMbgPgwPPV2ICsProtoNtSupRx": jnxMbgPgwPPV2ICsProtoNtSupRx,
       "jnxMbgPgwPPV2ICsProtoNtSupTx": jnxMbgPgwPPV2ICsProtoNtSupTx,
       "jnxMbgPgwPPV2ICsUENotRespRx": jnxMbgPgwPPV2ICsUENotRespRx,
       "jnxMbgPgwPPV2ICsUENotRespTx": jnxMbgPgwPPV2ICsUENotRespTx,
       "jnxMbgPgwPPV2ICsUERefusesRx": jnxMbgPgwPPV2ICsUERefusesRx,
       "jnxMbgPgwPPV2ICsUERefusesTx": jnxMbgPgwPPV2ICsUERefusesTx,
       "jnxMbgPgwPPV2ICsServDeniedRx": jnxMbgPgwPPV2ICsServDeniedRx,
       "jnxMbgPgwPPV2ICsServDeniedTx": jnxMbgPgwPPV2ICsServDeniedTx,
       "jnxMbgPgwPPV2ICsUnabPageUERx": jnxMbgPgwPPV2ICsUnabPageUERx,
       "jnxMbgPgwPPV2ICsUnabPageUETx": jnxMbgPgwPPV2ICsUnabPageUETx,
       "jnxMbgPgwPPV2ICsNoMemRx": jnxMbgPgwPPV2ICsNoMemRx,
       "jnxMbgPgwPPV2ICsNoMemTx": jnxMbgPgwPPV2ICsNoMemTx,
       "jnxMbgPgwPPV2ICsUserAUTHFlRx": jnxMbgPgwPPV2ICsUserAUTHFlRx,
       "jnxMbgPgwPPV2ICsUserAUTHFlTx": jnxMbgPgwPPV2ICsUserAUTHFlTx,
       "jnxMbgPgwPPV2ICsAPNAcsDenRx": jnxMbgPgwPPV2ICsAPNAcsDenRx,
       "jnxMbgPgwPPV2ICsAPNAcsDenTx": jnxMbgPgwPPV2ICsAPNAcsDenTx,
       "jnxMbgPgwPPV2ICsReqRejRx": jnxMbgPgwPPV2ICsReqRejRx,
       "jnxMbgPgwPPV2ICsReqRejTx": jnxMbgPgwPPV2ICsReqRejTx,
       "jnxMbgPgwPPV2ICsPTMSISigMMRx": jnxMbgPgwPPV2ICsPTMSISigMMRx,
       "jnxMbgPgwPPV2ICsPTMSISigMMTx": jnxMbgPgwPPV2ICsPTMSISigMMTx,
       "jnxMbgPgwPPV2ICsIMSINotKnRx": jnxMbgPgwPPV2ICsIMSINotKnRx,
       "jnxMbgPgwPPV2ICsIMSINotKnTx": jnxMbgPgwPPV2ICsIMSINotKnTx,
       "jnxMbgPgwPPV2ICsCondIEMsRx": jnxMbgPgwPPV2ICsCondIEMsRx,
       "jnxMbgPgwPPV2ICsCondIEMsTx": jnxMbgPgwPPV2ICsCondIEMsTx,
       "jnxMbgPgwPPV2ICsAPNResTIncRx": jnxMbgPgwPPV2ICsAPNResTIncRx,
       "jnxMbgPgwPPV2ICsAPNResTIncTx": jnxMbgPgwPPV2ICsAPNResTIncTx,
       "jnxMbgPgwPPV2ICsUnknownRx": jnxMbgPgwPPV2ICsUnknownRx,
       "jnxMbgPgwPPV2ICsUnknownTx": jnxMbgPgwPPV2ICsUnknownTx,
       "jnxMbgPgwPPV1ProtocolErrRx": jnxMbgPgwPPV1ProtocolErrRx,
       "jnxMbgPgwPPV1UnSupportedMsgRx": jnxMbgPgwPPV1UnSupportedMsgRx,
       "jnxMbgPgwPPV1T3RespTmrExpRx": jnxMbgPgwPPV1T3RespTmrExpRx,
       "jnxMbgPgwPPV1GlbNumMsgRx": jnxMbgPgwPPV1GlbNumMsgRx,
       "jnxMbgPgwPPV1GlbNumMsgTx": jnxMbgPgwPPV1GlbNumMsgTx,
       "jnxMbgPgwPPV1GlbNumBytesRx": jnxMbgPgwPPV1GlbNumBytesRx,
       "jnxMbgPgwPPV1GlbNumBytesTx": jnxMbgPgwPPV1GlbNumBytesTx,
       "jnxMbgPgwPPV1GlbEchoReqRx": jnxMbgPgwPPV1GlbEchoReqRx,
       "jnxMbgPgwPPV1GlbEchoReqTx": jnxMbgPgwPPV1GlbEchoReqTx,
       "jnxMbgPgwPPV1GlbEchoRespRx": jnxMbgPgwPPV1GlbEchoRespRx,
       "jnxMbgPgwPPV1GlbEchoRespTx": jnxMbgPgwPPV1GlbEchoRespTx,
       "jnxMbgPgwPPV1VerNotSupRx": jnxMbgPgwPPV1VerNotSupRx,
       "jnxMbgPgwPPV1VerNotSupTx": jnxMbgPgwPPV1VerNotSupTx,
       "jnxMbgPgwPPV1CrtPdpCxtReqRx": jnxMbgPgwPPV1CrtPdpCxtReqRx,
       "jnxMbgPgwPPV1CrtPdpCxtReqTx": jnxMbgPgwPPV1CrtPdpCxtReqTx,
       "jnxMbgPgwPPV1CrtPdpCxtRspRx": jnxMbgPgwPPV1CrtPdpCxtRspRx,
       "jnxMbgPgwPPV1CrtPdpCxtRspTx": jnxMbgPgwPPV1CrtPdpCxtRspTx,
       "jnxMbgPgwPPV1UpdPdpCxtReqRx": jnxMbgPgwPPV1UpdPdpCxtReqRx,
       "jnxMbgPgwPPV1UpdPdpCxtReqTx": jnxMbgPgwPPV1UpdPdpCxtReqTx,
       "jnxMbgPgwPPV1UpdPdpCxtRspRx": jnxMbgPgwPPV1UpdPdpCxtRspRx,
       "jnxMbgPgwPPV1UpdPdpCxtRspTx": jnxMbgPgwPPV1UpdPdpCxtRspTx,
       "jnxMbgPgwPPV1DelPdpCxtReqRx": jnxMbgPgwPPV1DelPdpCxtReqRx,
       "jnxMbgPgwPPV1DelPdpCxtReqTx": jnxMbgPgwPPV1DelPdpCxtReqTx,
       "jnxMbgPgwPPV1DelPdpCxtRspRx": jnxMbgPgwPPV1DelPdpCxtRspRx,
       "jnxMbgPgwPPV1DelPdpCxtRspTx": jnxMbgPgwPPV1DelPdpCxtRspTx,
       "jnxMbgPgwPPV1CrtAAPdpCxtReqRx": jnxMbgPgwPPV1CrtAAPdpCxtReqRx,
       "jnxMbgPgwPPV1CrtAAPdpCxtReqTx": jnxMbgPgwPPV1CrtAAPdpCxtReqTx,
       "jnxMbgPgwPPV1CrtAAPdpCxtRspRx": jnxMbgPgwPPV1CrtAAPdpCxtRspRx,
       "jnxMbgPgwPPV1CrtAAPdpCxtRspTx": jnxMbgPgwPPV1CrtAAPdpCxtRspTx,
       "jnxMbgPgwPPV1DelAAPdpCxtReqRx": jnxMbgPgwPPV1DelAAPdpCxtReqRx,
       "jnxMbgPgwPPV1DelAAPdpCxtReqTx": jnxMbgPgwPPV1DelAAPdpCxtReqTx,
       "jnxMbgPgwPPV1DelAAPdpCxtRspRx": jnxMbgPgwPPV1DelAAPdpCxtRspRx,
       "jnxMbgPgwPPV1DelAAPdpCxtRspTx": jnxMbgPgwPPV1DelAAPdpCxtRspTx,
       "jnxMbgPgwPPV1ErrorIndRx": jnxMbgPgwPPV1ErrorIndRx,
       "jnxMbgPgwPPV1ErrorIndTx": jnxMbgPgwPPV1ErrorIndTx,
       "jnxMbgPgwPPV1NotifReqRx": jnxMbgPgwPPV1NotifReqRx,
       "jnxMbgPgwPPV1NotifReqTx": jnxMbgPgwPPV1NotifReqTx,
       "jnxMbgPgwPPV1NotifRspRx": jnxMbgPgwPPV1NotifRspRx,
       "jnxMbgPgwPPV1NotifRspTx": jnxMbgPgwPPV1NotifRspTx,
       "jnxMbgPgwPPV1NotifRejReqRx": jnxMbgPgwPPV1NotifRejReqRx,
       "jnxMbgPgwPPV1NotifRejReqTx": jnxMbgPgwPPV1NotifRejReqTx,
       "jnxMbgPgwPPV1NotifRejRspRx": jnxMbgPgwPPV1NotifRejRspRx,
       "jnxMbgPgwPPV1NotifRejRspTx": jnxMbgPgwPPV1NotifRejRspTx,
       "jnxMbgPgwPPV1RtInfReqRx": jnxMbgPgwPPV1RtInfReqRx,
       "jnxMbgPgwPPV1RtInfReqTx": jnxMbgPgwPPV1RtInfReqTx,
       "jnxMbgPgwPPV1RtInfRspRx": jnxMbgPgwPPV1RtInfRspRx,
       "jnxMbgPgwPPV1RtInfRspTx": jnxMbgPgwPPV1RtInfRspTx,
       "jnxMbgPgwPPV1FailRptReqRx": jnxMbgPgwPPV1FailRptReqRx,
       "jnxMbgPgwPPV1FailRptReqTx": jnxMbgPgwPPV1FailRptReqTx,
       "jnxMbgPgwPPV1FailRptRspRx": jnxMbgPgwPPV1FailRptRspRx,
       "jnxMbgPgwPPV1FailRptRspTx": jnxMbgPgwPPV1FailRptRspTx,
       "jnxMbgPgwPPV1NotMSPresReqRx": jnxMbgPgwPPV1NotMSPresReqRx,
       "jnxMbgPgwPPV1NotMSPresReqTx": jnxMbgPgwPPV1NotMSPresReqTx,
       "jnxMbgPgwPPV1NotMSPresRspRx": jnxMbgPgwPPV1NotMSPresRspRx,
       "jnxMbgPgwPPV1NotMSPresRspTx": jnxMbgPgwPPV1NotMSPresRspTx,
       "jnxMbgPgwPPV1ICsReqAcceptedRx": jnxMbgPgwPPV1ICsReqAcceptedRx,
       "jnxMbgPgwPPV1ICsReqAcceptedTx": jnxMbgPgwPPV1ICsReqAcceptedTx,
       "jnxMbgPgwPPV1ICsNonExistRx": jnxMbgPgwPPV1ICsNonExistRx,
       "jnxMbgPgwPPV1ICsNonExistTx": jnxMbgPgwPPV1ICsNonExistTx,
       "jnxMbgPgwPPV1ICsInvMsgFmtRx": jnxMbgPgwPPV1ICsInvMsgFmtRx,
       "jnxMbgPgwPPV1ICsInvMsgFmtTx": jnxMbgPgwPPV1ICsInvMsgFmtTx,
       "jnxMbgPgwPPV1ICsIMSINotKnownRx": jnxMbgPgwPPV1ICsIMSINotKnownRx,
       "jnxMbgPgwPPV1ICsIMSINotKnownTx": jnxMbgPgwPPV1ICsIMSINotKnownTx,
       "jnxMbgPgwPPV1ICsMSGRPSDetachRx": jnxMbgPgwPPV1ICsMSGRPSDetachRx,
       "jnxMbgPgwPPV1ICsMSGRPSDetachTx": jnxMbgPgwPPV1ICsMSGRPSDetachTx,
       "jnxMbgPgwPPV1ICsMSNotGRPSRespRx": jnxMbgPgwPPV1ICsMSNotGRPSRespRx,
       "jnxMbgPgwPPV1ICsMSNotGRPSRespTx": jnxMbgPgwPPV1ICsMSNotGRPSRespTx,
       "jnxMbgPgwPPV1ICsMSRefusesRx": jnxMbgPgwPPV1ICsMSRefusesRx,
       "jnxMbgPgwPPV1ICsMSRefusesTx": jnxMbgPgwPPV1ICsMSRefusesTx,
       "jnxMbgPgwPPV1ICsVerNotSuppRx": jnxMbgPgwPPV1ICsVerNotSuppRx,
       "jnxMbgPgwPPV1ICsVerNotSuppTx": jnxMbgPgwPPV1ICsVerNotSuppTx,
       "jnxMbgPgwPPV1ICsNoResRx": jnxMbgPgwPPV1ICsNoResRx,
       "jnxMbgPgwPPV1ICsNoResTx": jnxMbgPgwPPV1ICsNoResTx,
       "jnxMbgPgwPPV1ICsServNotSuppRx": jnxMbgPgwPPV1ICsServNotSuppRx,
       "jnxMbgPgwPPV1ICsServNotSuppTx": jnxMbgPgwPPV1ICsServNotSuppTx,
       "jnxMbgPgwPPV1ICsManIEIncrtRx": jnxMbgPgwPPV1ICsManIEIncrtRx,
       "jnxMbgPgwPPV1ICsManIEIncrtTx": jnxMbgPgwPPV1ICsManIEIncrtTx,
       "jnxMbgPgwPPV1ICsManIEMissRx": jnxMbgPgwPPV1ICsManIEMissRx,
       "jnxMbgPgwPPV1ICsManIEMissTx": jnxMbgPgwPPV1ICsManIEMissTx,
       "jnxMbgPgwPPV1ICsOptIEIncrtRx": jnxMbgPgwPPV1ICsOptIEIncrtRx,
       "jnxMbgPgwPPV1ICsOptIEIncrtTx": jnxMbgPgwPPV1ICsOptIEIncrtTx,
       "jnxMbgPgwPPV1ICsSysFailRx": jnxMbgPgwPPV1ICsSysFailRx,
       "jnxMbgPgwPPV1ICsSysFailTx": jnxMbgPgwPPV1ICsSysFailTx,
       "jnxMbgPgwPPV1ICsRoamRestrictRx": jnxMbgPgwPPV1ICsRoamRestrictRx,
       "jnxMbgPgwPPV1ICsRoamRestrictTx": jnxMbgPgwPPV1ICsRoamRestrictTx,
       "jnxMbgPgwPPV1ICsPTMSISigMMRx": jnxMbgPgwPPV1ICsPTMSISigMMRx,
       "jnxMbgPgwPPV1ICsPTMSISigMMTx": jnxMbgPgwPPV1ICsPTMSISigMMTx,
       "jnxMbgPgwPPV1ICsGPRSConnSuppRx": jnxMbgPgwPPV1ICsGPRSConnSuppRx,
       "jnxMbgPgwPPV1ICsGPRSConnSuppTx": jnxMbgPgwPPV1ICsGPRSConnSuppTx,
       "jnxMbgPgwPPV1ICsAuthFailRx": jnxMbgPgwPPV1ICsAuthFailRx,
       "jnxMbgPgwPPV1ICsAuthFailTx": jnxMbgPgwPPV1ICsAuthFailTx,
       "jnxMbgPgwPPV1ICsUserAuthFailRx": jnxMbgPgwPPV1ICsUserAuthFailRx,
       "jnxMbgPgwPPV1ICsUserAuthFailTx": jnxMbgPgwPPV1ICsUserAuthFailTx,
       "jnxMbgPgwPPV1ICsCtxNotFndRx": jnxMbgPgwPPV1ICsCtxNotFndRx,
       "jnxMbgPgwPPV1ICsCtxNotFndTx": jnxMbgPgwPPV1ICsCtxNotFndTx,
       "jnxMbgPgwPPV1ICsAllDynPDPAdRx": jnxMbgPgwPPV1ICsAllDynPDPAdRx,
       "jnxMbgPgwPPV1ICsAllDynPDPAdTx": jnxMbgPgwPPV1ICsAllDynPDPAdTx,
       "jnxMbgPgwPPV1ICsNoMemRx": jnxMbgPgwPPV1ICsNoMemRx,
       "jnxMbgPgwPPV1ICsNoMemTx": jnxMbgPgwPPV1ICsNoMemTx,
       "jnxMbgPgwPPV1ICsRelocFailRx": jnxMbgPgwPPV1ICsRelocFailRx,
       "jnxMbgPgwPPV1ICsRelocFailTx": jnxMbgPgwPPV1ICsRelocFailTx,
       "jnxMbgPgwPPV1ICsUnkManExhdrRx": jnxMbgPgwPPV1ICsUnkManExhdrRx,
       "jnxMbgPgwPPV1ICsUnkManExhdrTx": jnxMbgPgwPPV1ICsUnkManExhdrTx,
       "jnxMbgPgwPPV1ICsSMANTTFTEr1Rx": jnxMbgPgwPPV1ICsSMANTTFTEr1Rx,
       "jnxMbgPgwPPV1ICsSMANTTFTEr1Tx": jnxMbgPgwPPV1ICsSMANTTFTEr1Tx,
       "jnxMbgPgwPPV1ICsSYNTFTErr2Rx": jnxMbgPgwPPV1ICsSYNTFTErr2Rx,
       "jnxMbgPgwPPV1ICsSYNTFTErr2Tx": jnxMbgPgwPPV1ICsSYNTFTErr2Tx,
       "jnxMbgPgwPPV1ICsSMNTPkFlEr1Rx": jnxMbgPgwPPV1ICsSMNTPkFlEr1Rx,
       "jnxMbgPgwPPV1ICsSMNTPkFlEr1Tx": jnxMbgPgwPPV1ICsSMNTPkFlEr1Tx,
       "jnxMbgPgwPPV1ICsSYNPkFlErr2Rx": jnxMbgPgwPPV1ICsSYNPkFlErr2Rx,
       "jnxMbgPgwPPV1ICsSYNPkFlErr2Tx": jnxMbgPgwPPV1ICsSYNPkFlErr2Tx,
       "jnxMbgPgwPPV1ICsMissUnknAPNRx": jnxMbgPgwPPV1ICsMissUnknAPNRx,
       "jnxMbgPgwPPV1ICsMissUnknAPNTx": jnxMbgPgwPPV1ICsMissUnknAPNTx,
       "jnxMbgPgwPPV1ICsUnknPDPAdRx": jnxMbgPgwPPV1ICsUnknPDPAdRx,
       "jnxMbgPgwPPV1ICsUnknPDPAdTx": jnxMbgPgwPPV1ICsUnknPDPAdTx,
       "jnxMbgPgwPPV1ICsNoTFTCtxExRx": jnxMbgPgwPPV1ICsNoTFTCtxExRx,
       "jnxMbgPgwPPV1ICsNoTFTCtxExTx": jnxMbgPgwPPV1ICsNoTFTCtxExTx,
       "jnxMbgPgwPPV0ProtocolErrRx": jnxMbgPgwPPV0ProtocolErrRx,
       "jnxMbgPgwPPV0UnSupportedMsgRx": jnxMbgPgwPPV0UnSupportedMsgRx,
       "jnxMbgPgwPPV0T3RespTmrExpRx": jnxMbgPgwPPV0T3RespTmrExpRx,
       "jnxMbgPgwPPV0GlbNumMsgRx": jnxMbgPgwPPV0GlbNumMsgRx,
       "jnxMbgPgwPPV0GlbNumMsgTx": jnxMbgPgwPPV0GlbNumMsgTx,
       "jnxMbgPgwPPV0GlbNumBytesRx": jnxMbgPgwPPV0GlbNumBytesRx,
       "jnxMbgPgwPPV0GlbNumBytesTx": jnxMbgPgwPPV0GlbNumBytesTx,
       "jnxMbgPgwPPV0GlbEchoReqRx": jnxMbgPgwPPV0GlbEchoReqRx,
       "jnxMbgPgwPPV0GlbEchoReqTx": jnxMbgPgwPPV0GlbEchoReqTx,
       "jnxMbgPgwPPV0GlbEchoRespRx": jnxMbgPgwPPV0GlbEchoRespRx,
       "jnxMbgPgwPPV0GlbEchoRespTx": jnxMbgPgwPPV0GlbEchoRespTx,
       "jnxMbgPgwPPV0GlbVerNotSupRx": jnxMbgPgwPPV0GlbVerNotSupRx,
       "jnxMbgPgwPPV0GlbVerNotSupTx": jnxMbgPgwPPV0GlbVerNotSupTx,
       "jnxMbgPgwPPV0GlbCrtPdpCxtReqRx": jnxMbgPgwPPV0GlbCrtPdpCxtReqRx,
       "jnxMbgPgwPPV0GlbCrtPdpCxtReqTx": jnxMbgPgwPPV0GlbCrtPdpCxtReqTx,
       "jnxMbgPgwPPV0GlbCrtPdpCxtRspRx": jnxMbgPgwPPV0GlbCrtPdpCxtRspRx,
       "jnxMbgPgwPPV0GlbCrtPdpCxtRspTx": jnxMbgPgwPPV0GlbCrtPdpCxtRspTx,
       "jnxMbgPgwPPV0GlbUpdPdpCxtReqRx": jnxMbgPgwPPV0GlbUpdPdpCxtReqRx,
       "jnxMbgPgwPPV0GlbUpdPdpCxtReqTx": jnxMbgPgwPPV0GlbUpdPdpCxtReqTx,
       "jnxMbgPgwPPV0GlbUpdPdpCxtRspRx": jnxMbgPgwPPV0GlbUpdPdpCxtRspRx,
       "jnxMbgPgwPPV0GlbUpdPdpCxtRspTx": jnxMbgPgwPPV0GlbUpdPdpCxtRspTx,
       "jnxMbgPgwPPV0GlbDelPdpCxtReqRx": jnxMbgPgwPPV0GlbDelPdpCxtReqRx,
       "jnxMbgPgwPPV0GlbDelPdpCxtReqTx": jnxMbgPgwPPV0GlbDelPdpCxtReqTx,
       "jnxMbgPgwPPV0GlbDelPdpCxtRspRx": jnxMbgPgwPPV0GlbDelPdpCxtRspRx,
       "jnxMbgPgwPPV0GlbDelPdpCxtRspTx": jnxMbgPgwPPV0GlbDelPdpCxtRspTx,
       "jnxMbgPgwPPV0GlbCrAAPdpCxtReqRx": jnxMbgPgwPPV0GlbCrAAPdpCxtReqRx,
       "jnxMbgPgwPPV0GlbCrAAPdpCxtReqTx": jnxMbgPgwPPV0GlbCrAAPdpCxtReqTx,
       "jnxMbgPgwPPV0GlbCrAAPdpCxtRspRx": jnxMbgPgwPPV0GlbCrAAPdpCxtRspRx,
       "jnxMbgPgwPPV0GlbCrAAPdpCxtRspTx": jnxMbgPgwPPV0GlbCrAAPdpCxtRspTx,
       "jnxMbgPgwPPV0GlbDlAAPdpCxtReqRx": jnxMbgPgwPPV0GlbDlAAPdpCxtReqRx,
       "jnxMbgPgwPPV0GlbDlAAPdpCxtReqTx": jnxMbgPgwPPV0GlbDlAAPdpCxtReqTx,
       "jnxMbgPgwPPV0GlbDlAAPdpCxtRspRx": jnxMbgPgwPPV0GlbDlAAPdpCxtRspRx,
       "jnxMbgPgwPPV0GlbDlAAPdpCxtRspTx": jnxMbgPgwPPV0GlbDlAAPdpCxtRspTx,
       "jnxMbgPgwPPV0GlbErrorIndRx": jnxMbgPgwPPV0GlbErrorIndRx,
       "jnxMbgPgwPPV0GlbErrorIndTx": jnxMbgPgwPPV0GlbErrorIndTx,
       "jnxMbgPgwPPV0GlbNotifReqRx": jnxMbgPgwPPV0GlbNotifReqRx,
       "jnxMbgPgwPPV0GlbNotifReqTx": jnxMbgPgwPPV0GlbNotifReqTx,
       "jnxMbgPgwPPV0GlbNotifRspRx": jnxMbgPgwPPV0GlbNotifRspRx,
       "jnxMbgPgwPPV0GlbNotifRspTx": jnxMbgPgwPPV0GlbNotifRspTx,
       "jnxMbgPgwPPV0GlbNotifRejReqRx": jnxMbgPgwPPV0GlbNotifRejReqRx,
       "jnxMbgPgwPPV0GlbNotifRejReqTx": jnxMbgPgwPPV0GlbNotifRejReqTx,
       "jnxMbgPgwPPV0GlbNotifRejRspRx": jnxMbgPgwPPV0GlbNotifRejRspRx,
       "jnxMbgPgwPPV0GlbNotifRejRspTx": jnxMbgPgwPPV0GlbNotifRejRspTx,
       "jnxMbgPgwPPV0GlbRtInfReqRx": jnxMbgPgwPPV0GlbRtInfReqRx,
       "jnxMbgPgwPPV0GlbRtInfReqTx": jnxMbgPgwPPV0GlbRtInfReqTx,
       "jnxMbgPgwPPV0GlbRtInfRspRx": jnxMbgPgwPPV0GlbRtInfRspRx,
       "jnxMbgPgwPPV0GlbRtInfRspTx": jnxMbgPgwPPV0GlbRtInfRspTx,
       "jnxMbgPgwPPV0GlbFailRptReqRx": jnxMbgPgwPPV0GlbFailRptReqRx,
       "jnxMbgPgwPPV0GlbFailRptReqTx": jnxMbgPgwPPV0GlbFailRptReqTx,
       "jnxMbgPgwPPV0GlbFailRptRspRx": jnxMbgPgwPPV0GlbFailRptRspRx,
       "jnxMbgPgwPPV0GlbFailRptRspTx": jnxMbgPgwPPV0GlbFailRptRspTx,
       "jnxMbgPgwPPV0GlbNotMSPresReqRx": jnxMbgPgwPPV0GlbNotMSPresReqRx,
       "jnxMbgPgwPPV0GlbNotMSPresReqTx": jnxMbgPgwPPV0GlbNotMSPresReqTx,
       "jnxMbgPgwPPV0GlbNotMSPresRspRx": jnxMbgPgwPPV0GlbNotMSPresRspRx,
       "jnxMbgPgwPPV0GlbNotMSPresRspTx": jnxMbgPgwPPV0GlbNotMSPresRspTx,
       "jnxMbgPgwPPV0ICsReqAcceptedRx": jnxMbgPgwPPV0ICsReqAcceptedRx,
       "jnxMbgPgwPPV0ICsReqAcceptedTx": jnxMbgPgwPPV0ICsReqAcceptedTx,
       "jnxMbgPgwPPV0ICsNonExistRx": jnxMbgPgwPPV0ICsNonExistRx,
       "jnxMbgPgwPPV0ICsNonExistTx": jnxMbgPgwPPV0ICsNonExistTx,
       "jnxMbgPgwPPV0ICsInvMsgFmtRx": jnxMbgPgwPPV0ICsInvMsgFmtRx,
       "jnxMbgPgwPPV0ICsInvMsgFmtTx": jnxMbgPgwPPV0ICsInvMsgFmtTx,
       "jnxMbgPgwPPV0ICsIMSINotKnownRx": jnxMbgPgwPPV0ICsIMSINotKnownRx,
       "jnxMbgPgwPPV0ICsIMSINotKnownTx": jnxMbgPgwPPV0ICsIMSINotKnownTx,
       "jnxMbgPgwPPV0ICsMSGRPSDetachRx": jnxMbgPgwPPV0ICsMSGRPSDetachRx,
       "jnxMbgPgwPPV0ICsMSGRPSDetachTx": jnxMbgPgwPPV0ICsMSGRPSDetachTx,
       "jnxMbgPgwPPV0ICsMSNotGRPSRespRx": jnxMbgPgwPPV0ICsMSNotGRPSRespRx,
       "jnxMbgPgwPPV0ICsMSNotGRPSRespTx": jnxMbgPgwPPV0ICsMSNotGRPSRespTx,
       "jnxMbgPgwPPV0ICsMSRefusesRx": jnxMbgPgwPPV0ICsMSRefusesRx,
       "jnxMbgPgwPPV0ICsMSRefusesTx": jnxMbgPgwPPV0ICsMSRefusesTx,
       "jnxMbgPgwPPV0ICsVerNotSuppRx": jnxMbgPgwPPV0ICsVerNotSuppRx,
       "jnxMbgPgwPPV0ICsVerNotSuppTx": jnxMbgPgwPPV0ICsVerNotSuppTx,
       "jnxMbgPgwPPV0ICsNoResRx": jnxMbgPgwPPV0ICsNoResRx,
       "jnxMbgPgwPPV0ICsNoResTx": jnxMbgPgwPPV0ICsNoResTx,
       "jnxMbgPgwPPV0ICsServNotSuppRx": jnxMbgPgwPPV0ICsServNotSuppRx,
       "jnxMbgPgwPPV0ICsServNotSuppTx": jnxMbgPgwPPV0ICsServNotSuppTx,
       "jnxMbgPgwPPV0ICsManIEIncrtRx": jnxMbgPgwPPV0ICsManIEIncrtRx,
       "jnxMbgPgwPPV0ICsManIEIncrtTx": jnxMbgPgwPPV0ICsManIEIncrtTx,
       "jnxMbgPgwPPV0ICsManIEMissRx": jnxMbgPgwPPV0ICsManIEMissRx,
       "jnxMbgPgwPPV0ICsManIEMissTx": jnxMbgPgwPPV0ICsManIEMissTx,
       "jnxMbgPgwPPV0ICsOptIEIncrtRx": jnxMbgPgwPPV0ICsOptIEIncrtRx,
       "jnxMbgPgwPPV0ICsOptIEIncrtTx": jnxMbgPgwPPV0ICsOptIEIncrtTx,
       "jnxMbgPgwPPV0ICsSysFailRx": jnxMbgPgwPPV0ICsSysFailRx,
       "jnxMbgPgwPPV0ICsSysFailTx": jnxMbgPgwPPV0ICsSysFailTx,
       "jnxMbgPgwPPV0ICsRoamRestrictRx": jnxMbgPgwPPV0ICsRoamRestrictRx,
       "jnxMbgPgwPPV0ICsRoamRestrictTx": jnxMbgPgwPPV0ICsRoamRestrictTx,
       "jnxMbgPgwPPV0ICsPTMSISigMMRx": jnxMbgPgwPPV0ICsPTMSISigMMRx,
       "jnxMbgPgwPPV0ICsPTMSISigMMTx": jnxMbgPgwPPV0ICsPTMSISigMMTx,
       "jnxMbgPgwPPV0ICsGPRSConnSuppRx": jnxMbgPgwPPV0ICsGPRSConnSuppRx,
       "jnxMbgPgwPPV0ICsGPRSConnSuppTx": jnxMbgPgwPPV0ICsGPRSConnSuppTx,
       "jnxMbgPgwPPV0ICsAuthFailRx": jnxMbgPgwPPV0ICsAuthFailRx,
       "jnxMbgPgwPPV0ICsAuthFailTx": jnxMbgPgwPPV0ICsAuthFailTx,
       "jnxMbgPgwPPV0ICsUserAuthFailRx": jnxMbgPgwPPV0ICsUserAuthFailRx,
       "jnxMbgPgwPPV0ICsUserAuthFailTx": jnxMbgPgwPPV0ICsUserAuthFailTx,
       "jnxMbgPgwPPGtpV2ICsLclDetRx": jnxMbgPgwPPGtpV2ICsLclDetRx,
       "jnxMbgPgwPPGtpV2ICsLclDetTx": jnxMbgPgwPPGtpV2ICsLclDetTx,
       "jnxMbgPgwPPGtpV2ICsCmpDetRx": jnxMbgPgwPPGtpV2ICsCmpDetRx,
       "jnxMbgPgwPPGtpV2ICsCmpDetTx": jnxMbgPgwPPGtpV2ICsCmpDetTx,
       "jnxMbgPgwPPGtpV2ICsRATChgRx": jnxMbgPgwPPGtpV2ICsRATChgRx,
       "jnxMbgPgwPPGtpV2ICsRATChgTx": jnxMbgPgwPPGtpV2ICsRATChgTx,
       "jnxMbgPgwPPGtpV2ICsISRDeactRx": jnxMbgPgwPPGtpV2ICsISRDeactRx,
       "jnxMbgPgwPPGtpV2ICsISRDeactTx": jnxMbgPgwPPGtpV2ICsISRDeactTx,
       "jnxMbgPgwPPGtpV2ICsEIFRNCEnRx": jnxMbgPgwPPGtpV2ICsEIFRNCEnRx,
       "jnxMbgPgwPPGtpV2ICsEIFRNCEnTx": jnxMbgPgwPPGtpV2ICsEIFRNCEnTx,
       "jnxMbgPgwPPGtpV2ICsSemErTADRx": jnxMbgPgwPPGtpV2ICsSemErTADRx,
       "jnxMbgPgwPPGtpV2ICsSemErTADTx": jnxMbgPgwPPGtpV2ICsSemErTADTx,
       "jnxMbgPgwPPGtpV2ICsSynErTADRx": jnxMbgPgwPPGtpV2ICsSynErTADRx,
       "jnxMbgPgwPPGtpV2ICsSynErTADTx": jnxMbgPgwPPGtpV2ICsSynErTADTx,
       "jnxMbgPgwPPGtpV2ICsRMValRcvRx": jnxMbgPgwPPGtpV2ICsRMValRcvRx,
       "jnxMbgPgwPPGtpV2ICsRMValRcvTx": jnxMbgPgwPPGtpV2ICsRMValRcvTx,
       "jnxMbgPgwPPGtpV2ICsRPrNtRspRx": jnxMbgPgwPPGtpV2ICsRPrNtRspRx,
       "jnxMbgPgwPPGtpV2ICsRPrNtRspTx": jnxMbgPgwPPGtpV2ICsRPrNtRspTx,
       "jnxMbgPgwPPGtpV2ICsColNWReqRx": jnxMbgPgwPPGtpV2ICsColNWReqRx,
       "jnxMbgPgwPPGtpV2ICsColNWReqTx": jnxMbgPgwPPGtpV2ICsColNWReqTx,
       "jnxMbgPgwPPGtpV2ICsUnPgUESusRx": jnxMbgPgwPPGtpV2ICsUnPgUESusRx,
       "jnxMbgPgwPPGtpV2ICsUnPgUESusTx": jnxMbgPgwPPGtpV2ICsUnPgUESusTx,
       "jnxMbgPgwPPGtpV2ICsInvTotLenRx": jnxMbgPgwPPGtpV2ICsInvTotLenRx,
       "jnxMbgPgwPPGtpV2ICsInvTotLenTx": jnxMbgPgwPPGtpV2ICsInvTotLenTx,
       "jnxMbgPgwPPGtpV2ICsDtForNtSupRx": jnxMbgPgwPPGtpV2ICsDtForNtSupRx,
       "jnxMbgPgwPPGtpV2ICsDtForNtSupTx": jnxMbgPgwPPGtpV2ICsDtForNtSupTx,
       "jnxMbgPgwPPGtpV2ICsInReFRePrRx": jnxMbgPgwPPGtpV2ICsInReFRePrRx,
       "jnxMbgPgwPPGtpV2ICsInReFRePrTx": jnxMbgPgwPPGtpV2ICsInReFRePrTx,
       "jnxMbgPgwPPGtpV2ICsInvPrRx": jnxMbgPgwPPGtpV2ICsInvPrRx,
       "jnxMbgPgwPPGtpV2ICsInvPrTx": jnxMbgPgwPPGtpV2ICsInvPrTx,
       "jnxMbgPgwPPV1InitPdpCxtReqRx": jnxMbgPgwPPV1InitPdpCxtReqRx,
       "jnxMbgPgwPPV1InitPdpCxtReqTx": jnxMbgPgwPPV1InitPdpCxtReqTx,
       "jnxMbgPgwPPV1InitPdpCxtRspRx": jnxMbgPgwPPV1InitPdpCxtRspRx,
       "jnxMbgPgwPPV1InitPdpCxtRspTx": jnxMbgPgwPPV1InitPdpCxtRspTx,
       "jnxMbgPgwPPV2SuspNotifRx": jnxMbgPgwPPV2SuspNotifRx,
       "jnxMbgPgwPPV2SuspNotifTx": jnxMbgPgwPPV2SuspNotifTx,
       "jnxMbgPgwPPV2SuspAckRx": jnxMbgPgwPPV2SuspAckRx,
       "jnxMbgPgwPPV2SuspAckTx": jnxMbgPgwPPV2SuspAckTx,
       "jnxMbgPgwPPV2ResumeNotifRx": jnxMbgPgwPPV2ResumeNotifRx,
       "jnxMbgPgwPPV2ResumeNotifTx": jnxMbgPgwPPV2ResumeNotifTx,
       "jnxMbgPgwPPV2ResumeAckRx": jnxMbgPgwPPV2ResumeAckRx,
       "jnxMbgPgwPPV2ResumeAckTx": jnxMbgPgwPPV2ResumeAckTx,
       "jnxMbgPgwPPV2PiggybackMsgRx": jnxMbgPgwPPV2PiggybackMsgRx,
       "jnxMbgPgwPPV2PiggybackMsgTx": jnxMbgPgwPPV2PiggybackMsgTx,
       "jnxMbgPgwGtpCGlbStatsTable": jnxMbgPgwGtpCGlbStatsTable,
       "jnxMbgPgwGtpGlbStatsEntry": jnxMbgPgwGtpGlbStatsEntry,
       "jnxMbgPgwRxPacketsDropped": jnxMbgPgwRxPacketsDropped,
       "jnxMbgPgwPacketAllocFail": jnxMbgPgwPacketAllocFail,
       "jnxMbgPgwPacketSendFail": jnxMbgPgwPacketSendFail,
       "jnxMbgPgwIPVerErrRx": jnxMbgPgwIPVerErrRx,
       "jnxMbgPgwIPProtoErrRx": jnxMbgPgwIPProtoErrRx,
       "jnxMbgPgwGTPPortErrRx": jnxMbgPgwGTPPortErrRx,
       "jnxMbgPgwGTPUnknVerRx": jnxMbgPgwGTPUnknVerRx,
       "jnxMbgPgwPcktLenErrRx": jnxMbgPgwPcktLenErrRx,
       "jnxMbgPgwUnknMsgRx": jnxMbgPgwUnknMsgRx,
       "jnxMbgPgwV2ProtocolErrRx": jnxMbgPgwV2ProtocolErrRx,
       "jnxMbgPgwV2UnSupportedMsgRx": jnxMbgPgwV2UnSupportedMsgRx,
       "jnxMbgPgwV2T3RespTmrExpRx": jnxMbgPgwV2T3RespTmrExpRx,
       "jnxMbgPgwV2GlbNumMsgRx": jnxMbgPgwV2GlbNumMsgRx,
       "jnxMbgPgwV2GlbNumMsgTx": jnxMbgPgwV2GlbNumMsgTx,
       "jnxMbgPgwV2GlbNumBytesRx": jnxMbgPgwV2GlbNumBytesRx,
       "jnxMbgPgwV2GlbNumBytesTx": jnxMbgPgwV2GlbNumBytesTx,
       "jnxMbgPgwV2GlbEchoReqRx": jnxMbgPgwV2GlbEchoReqRx,
       "jnxMbgPgwV2GlbEchoReqTx": jnxMbgPgwV2GlbEchoReqTx,
       "jnxMbgPgwV2GlbEchoRespRx": jnxMbgPgwV2GlbEchoRespRx,
       "jnxMbgPgwV2GlbEchoRespTx": jnxMbgPgwV2GlbEchoRespTx,
       "jnxMbgPgwV2VerNotSupRx": jnxMbgPgwV2VerNotSupRx,
       "jnxMbgPgwV2VerNotSupTx": jnxMbgPgwV2VerNotSupTx,
       "jnxMbgPgwV2CreateSessReqRx": jnxMbgPgwV2CreateSessReqRx,
       "jnxMbgPgwV2CreateSessReqTx": jnxMbgPgwV2CreateSessReqTx,
       "jnxMbgPgwV2CreateSessRspRx": jnxMbgPgwV2CreateSessRspRx,
       "jnxMbgPgwV2CreateSessRspTx": jnxMbgPgwV2CreateSessRspTx,
       "jnxMbgPgwV2ModBrReqRx": jnxMbgPgwV2ModBrReqRx,
       "jnxMbgPgwV2ModBrReqTx": jnxMbgPgwV2ModBrReqTx,
       "jnxMbgPgwV2ModBrRspRx": jnxMbgPgwV2ModBrRspRx,
       "jnxMbgPgwV2ModBrRspTx": jnxMbgPgwV2ModBrRspTx,
       "jnxMbgPgwV2DelSessReqRx": jnxMbgPgwV2DelSessReqRx,
       "jnxMbgPgwV2DelSessReqTx": jnxMbgPgwV2DelSessReqTx,
       "jnxMbgPgwV2DelSessRspRx": jnxMbgPgwV2DelSessRspRx,
       "jnxMbgPgwV2DelSessRspTx": jnxMbgPgwV2DelSessRspTx,
       "jnxMbgPgwV2CrtBrReqRx": jnxMbgPgwV2CrtBrReqRx,
       "jnxMbgPgwV2CrtBrReqTx": jnxMbgPgwV2CrtBrReqTx,
       "jnxMbgPgwV2CrtBrRspRx": jnxMbgPgwV2CrtBrRspRx,
       "jnxMbgPgwV2CrtBrRspTx": jnxMbgPgwV2CrtBrRspTx,
       "jnxMbgPgwV2UpdBrReqRx": jnxMbgPgwV2UpdBrReqRx,
       "jnxMbgPgwV2UpdBrReqTx": jnxMbgPgwV2UpdBrReqTx,
       "jnxMbgPgwV2UpdBrRspRx": jnxMbgPgwV2UpdBrRspRx,
       "jnxMbgPgwV2UpdBrRspTx": jnxMbgPgwV2UpdBrRspTx,
       "jnxMbgPgwV2DelBrReqRx": jnxMbgPgwV2DelBrReqRx,
       "jnxMbgPgwV2DelBrReqTx": jnxMbgPgwV2DelBrReqTx,
       "jnxMbgPgwV2DelBrRspRx": jnxMbgPgwV2DelBrRspRx,
       "jnxMbgPgwV2DelBrRspTx": jnxMbgPgwV2DelBrRspTx,
       "jnxMbgPgwV2DelConnSetReqRx": jnxMbgPgwV2DelConnSetReqRx,
       "jnxMbgPgwV2DelConnSetReqTx": jnxMbgPgwV2DelConnSetReqTx,
       "jnxMbgPgwV2DelConnSetRspRx": jnxMbgPgwV2DelConnSetRspRx,
       "jnxMbgPgwV2DelConnSetRspTx": jnxMbgPgwV2DelConnSetRspTx,
       "jnxMbgPgwV2UpdConnSetReqRx": jnxMbgPgwV2UpdConnSetReqRx,
       "jnxMbgPgwV2UpdConnSetReqTx": jnxMbgPgwV2UpdConnSetReqTx,
       "jnxMbgPgwV2UpdConnSetRspRx": jnxMbgPgwV2UpdConnSetRspRx,
       "jnxMbgPgwV2UpdConnSetRspTx": jnxMbgPgwV2UpdConnSetRspTx,
       "jnxMbgPgwV2ModBrCmdRx": jnxMbgPgwV2ModBrCmdRx,
       "jnxMbgPgwV2ModBrCmdTx": jnxMbgPgwV2ModBrCmdTx,
       "jnxMbgPgwV2ModBrFlrIndRx": jnxMbgPgwV2ModBrFlrIndRx,
       "jnxMbgPgwV2ModBrFlrIndTx": jnxMbgPgwV2ModBrFlrIndTx,
       "jnxMbgPgwV2DelBrCmdRx": jnxMbgPgwV2DelBrCmdRx,
       "jnxMbgPgwV2DelBrCmdTx": jnxMbgPgwV2DelBrCmdTx,
       "jnxMbgPgwV2DelBrFlrIndRx": jnxMbgPgwV2DelBrFlrIndRx,
       "jnxMbgPgwV2DelBrFlrIndTx": jnxMbgPgwV2DelBrFlrIndTx,
       "jnxMbgPgwV2BrResCmdRx": jnxMbgPgwV2BrResCmdRx,
       "jnxMbgPgwV2BrResCmdTx": jnxMbgPgwV2BrResCmdTx,
       "jnxMbgPgwV2BrResFlrIndRx": jnxMbgPgwV2BrResFlrIndRx,
       "jnxMbgPgwV2BrResFlrIndTx": jnxMbgPgwV2BrResFlrIndTx,
       "jnxMbgPgwV2RelAcsBrReqRx": jnxMbgPgwV2RelAcsBrReqRx,
       "jnxMbgPgwV2RelAcsBrReqTx": jnxMbgPgwV2RelAcsBrReqTx,
       "jnxMbgPgwV2RelAcsBrRespRx": jnxMbgPgwV2RelAcsBrRespRx,
       "jnxMbgPgwV2RelAcsBrRespTx": jnxMbgPgwV2RelAcsBrRespTx,
       "jnxMbgPgwV2CrIndTunReqRx": jnxMbgPgwV2CrIndTunReqRx,
       "jnxMbgPgwV2CrIndTunReqTx": jnxMbgPgwV2CrIndTunReqTx,
       "jnxMbgPgwV2CrIndTunRespRx": jnxMbgPgwV2CrIndTunRespRx,
       "jnxMbgPgwV2CrIndTunRespTx": jnxMbgPgwV2CrIndTunRespTx,
       "jnxMbgPgwV2DelIndTunReqRx": jnxMbgPgwV2DelIndTunReqRx,
       "jnxMbgPgwV2DelIndTunReqTx": jnxMbgPgwV2DelIndTunReqTx,
       "jnxMbgPgwV2DelIndTunRespRx": jnxMbgPgwV2DelIndTunRespRx,
       "jnxMbgPgwV2DelIndTunRespTx": jnxMbgPgwV2DelIndTunRespTx,
       "jnxMbgPgwV2DlDataNotifRx": jnxMbgPgwV2DlDataNotifRx,
       "jnxMbgPgwV2DlDataNotifTx": jnxMbgPgwV2DlDataNotifTx,
       "jnxMbgPgwV2DlDataAckRx": jnxMbgPgwV2DlDataAckRx,
       "jnxMbgPgwV2DlDataAckTx": jnxMbgPgwV2DlDataAckTx,
       "jnxMbgPgwV2DlDataNotiFlrIndRx": jnxMbgPgwV2DlDataNotiFlrIndRx,
       "jnxMbgPgwV2DlDataNotiFlrIndTx": jnxMbgPgwV2DlDataNotiFlrIndTx,
       "jnxMbgPgwV2StopPagingIndRx": jnxMbgPgwV2StopPagingIndRx,
       "jnxMbgPgwV2StopPagingIndTx": jnxMbgPgwV2StopPagingIndTx,
       "jnxMbgPgwV2ICsPageRx": jnxMbgPgwV2ICsPageRx,
       "jnxMbgPgwV2ICsPageTx": jnxMbgPgwV2ICsPageTx,
       "jnxMbgPgwV2ICsReqAcceptRx": jnxMbgPgwV2ICsReqAcceptRx,
       "jnxMbgPgwV2ICsReqAcceptTx": jnxMbgPgwV2ICsReqAcceptTx,
       "jnxMbgPgwV2ICsAcceptPartRx": jnxMbgPgwV2ICsAcceptPartRx,
       "jnxMbgPgwV2ICsAcceptPartTx": jnxMbgPgwV2ICsAcceptPartTx,
       "jnxMbgPgwV2ICsNewPTNPrefRx": jnxMbgPgwV2ICsNewPTNPrefRx,
       "jnxMbgPgwV2ICsNewPTNPrefTx": jnxMbgPgwV2ICsNewPTNPrefTx,
       "jnxMbgPgwV2ICsNewPTSIAdbrRx": jnxMbgPgwV2ICsNewPTSIAdbrRx,
       "jnxMbgPgwV2ICsNewPTSIAdbrTx": jnxMbgPgwV2ICsNewPTSIAdbrTx,
       "jnxMbgPgwV2ICsCtxNotFndRx": jnxMbgPgwV2ICsCtxNotFndRx,
       "jnxMbgPgwV2ICsCtxNotFndTx": jnxMbgPgwV2ICsCtxNotFndTx,
       "jnxMbgPgwV2ICsInvMsgFmtRx": jnxMbgPgwV2ICsInvMsgFmtRx,
       "jnxMbgPgwV2ICsInvMsgFmtTx": jnxMbgPgwV2ICsInvMsgFmtTx,
       "jnxMbgPgwV2ICsVerNotSuppRx": jnxMbgPgwV2ICsVerNotSuppRx,
       "jnxMbgPgwV2ICsVerNotSuppTx": jnxMbgPgwV2ICsVerNotSuppTx,
       "jnxMbgPgwV2ICsInvLenRx": jnxMbgPgwV2ICsInvLenRx,
       "jnxMbgPgwV2ICsInvLenTx": jnxMbgPgwV2ICsInvLenTx,
       "jnxMbgPgwV2ICsServNotSuppRx": jnxMbgPgwV2ICsServNotSuppRx,
       "jnxMbgPgwV2ICsServNotSuppTx": jnxMbgPgwV2ICsServNotSuppTx,
       "jnxMbgPgwV2ICsManIEIncorrRx": jnxMbgPgwV2ICsManIEIncorrRx,
       "jnxMbgPgwV2ICsManIEIncorrTx": jnxMbgPgwV2ICsManIEIncorrTx,
       "jnxMbgPgwV2ICsManIEMissRx": jnxMbgPgwV2ICsManIEMissRx,
       "jnxMbgPgwV2ICsManIEMissTx": jnxMbgPgwV2ICsManIEMissTx,
       "jnxMbgPgwV2ICsOptIEIncorrRx": jnxMbgPgwV2ICsOptIEIncorrRx,
       "jnxMbgPgwV2ICsOptIEIncorrTx": jnxMbgPgwV2ICsOptIEIncorrTx,
       "jnxMbgPgwV2ICsSysFailRx": jnxMbgPgwV2ICsSysFailRx,
       "jnxMbgPgwV2ICsSysFailTx": jnxMbgPgwV2ICsSysFailTx,
       "jnxMbgPgwV2ICsNoResRx": jnxMbgPgwV2ICsNoResRx,
       "jnxMbgPgwV2ICsNoResTx": jnxMbgPgwV2ICsNoResTx,
       "jnxMbgPgwV2ICsTFTSMANTErRx": jnxMbgPgwV2ICsTFTSMANTErRx,
       "jnxMbgPgwV2ICsTFTSMANTErTx": jnxMbgPgwV2ICsTFTSMANTErTx,
       "jnxMbgPgwV2ICsTFTSysErrRx": jnxMbgPgwV2ICsTFTSysErrRx,
       "jnxMbgPgwV2ICsTFTSysErrTx": jnxMbgPgwV2ICsTFTSysErrTx,
       "jnxMbgPgwV2ICsPkFltManErrRx": jnxMbgPgwV2ICsPkFltManErrRx,
       "jnxMbgPgwV2ICsPkFltManErrTx": jnxMbgPgwV2ICsPkFltManErrTx,
       "jnxMbgPgwV2ICsPkFltSynErrRx": jnxMbgPgwV2ICsPkFltSynErrRx,
       "jnxMbgPgwV2ICsPkFltSynErrTx": jnxMbgPgwV2ICsPkFltSynErrTx,
       "jnxMbgPgwV2ICsMisUnknAPNRx": jnxMbgPgwV2ICsMisUnknAPNRx,
       "jnxMbgPgwV2ICsMisUnknAPNTx": jnxMbgPgwV2ICsMisUnknAPNTx,
       "jnxMbgPgwV2ICsUnexpRptIERx": jnxMbgPgwV2ICsUnexpRptIERx,
       "jnxMbgPgwV2ICsUnexpRptIETx": jnxMbgPgwV2ICsUnexpRptIETx,
       "jnxMbgPgwV2ICsGREKeyNtFdRx": jnxMbgPgwV2ICsGREKeyNtFdRx,
       "jnxMbgPgwV2ICsGREKeyNtFdTx": jnxMbgPgwV2ICsGREKeyNtFdTx,
       "jnxMbgPgwV2ICsRelocFailRx": jnxMbgPgwV2ICsRelocFailRx,
       "jnxMbgPgwV2ICsRelocFailTx": jnxMbgPgwV2ICsRelocFailTx,
       "jnxMbgPgwV2ICsDeniedINRatRx": jnxMbgPgwV2ICsDeniedINRatRx,
       "jnxMbgPgwV2ICsDeniedINRatTx": jnxMbgPgwV2ICsDeniedINRatTx,
       "jnxMbgPgwV2ICsPTNotSuppRx": jnxMbgPgwV2ICsPTNotSuppRx,
       "jnxMbgPgwV2ICsPTNotSuppTx": jnxMbgPgwV2ICsPTNotSuppTx,
       "jnxMbgPgwV2ICsAllDynAdOccRx": jnxMbgPgwV2ICsAllDynAdOccRx,
       "jnxMbgPgwV2ICsAllDynAdOccTx": jnxMbgPgwV2ICsAllDynAdOccTx,
       "jnxMbgPgwV2ICsNOTFTUECTXRx": jnxMbgPgwV2ICsNOTFTUECTXRx,
       "jnxMbgPgwV2ICsNOTFTUECTXTx": jnxMbgPgwV2ICsNOTFTUECTXTx,
       "jnxMbgPgwV2ICsProtoNtSupRx": jnxMbgPgwV2ICsProtoNtSupRx,
       "jnxMbgPgwV2ICsProtoNtSupTx": jnxMbgPgwV2ICsProtoNtSupTx,
       "jnxMbgPgwV2ICsUENotRespRx": jnxMbgPgwV2ICsUENotRespRx,
       "jnxMbgPgwV2ICsUENotRespTx": jnxMbgPgwV2ICsUENotRespTx,
       "jnxMbgPgwV2ICsUERefusesRx": jnxMbgPgwV2ICsUERefusesRx,
       "jnxMbgPgwV2ICsUERefusesTx": jnxMbgPgwV2ICsUERefusesTx,
       "jnxMbgPgwV2ICsServDeniedRx": jnxMbgPgwV2ICsServDeniedRx,
       "jnxMbgPgwV2ICsServDeniedTx": jnxMbgPgwV2ICsServDeniedTx,
       "jnxMbgPgwV2ICsUnabPageUERx": jnxMbgPgwV2ICsUnabPageUERx,
       "jnxMbgPgwV2ICsUnabPageUETx": jnxMbgPgwV2ICsUnabPageUETx,
       "jnxMbgPgwV2ICsNoMemRx": jnxMbgPgwV2ICsNoMemRx,
       "jnxMbgPgwV2ICsNoMemTx": jnxMbgPgwV2ICsNoMemTx,
       "jnxMbgPgwV2ICsUserAUTHFlRx": jnxMbgPgwV2ICsUserAUTHFlRx,
       "jnxMbgPgwV2ICsUserAUTHFlTx": jnxMbgPgwV2ICsUserAUTHFlTx,
       "jnxMbgPgwV2ICsAPNAcsDenRx": jnxMbgPgwV2ICsAPNAcsDenRx,
       "jnxMbgPgwV2ICsAPNAcsDenTx": jnxMbgPgwV2ICsAPNAcsDenTx,
       "jnxMbgPgwV2ICsReqRejRx": jnxMbgPgwV2ICsReqRejRx,
       "jnxMbgPgwV2ICsReqRejTx": jnxMbgPgwV2ICsReqRejTx,
       "jnxMbgPgwV2ICsPTMSISigMMRx": jnxMbgPgwV2ICsPTMSISigMMRx,
       "jnxMbgPgwV2ICsPTMSISigMMTx": jnxMbgPgwV2ICsPTMSISigMMTx,
       "jnxMbgPgwV2ICsIMSINotKnRx": jnxMbgPgwV2ICsIMSINotKnRx,
       "jnxMbgPgwV2ICsIMSINotKnTx": jnxMbgPgwV2ICsIMSINotKnTx,
       "jnxMbgPgwV2ICsCondIEMsRx": jnxMbgPgwV2ICsCondIEMsRx,
       "jnxMbgPgwV2ICsCondIEMsTx": jnxMbgPgwV2ICsCondIEMsTx,
       "jnxMbgPgwV2ICsAPNResTIncRx": jnxMbgPgwV2ICsAPNResTIncRx,
       "jnxMbgPgwV2ICsAPNResTIncTx": jnxMbgPgwV2ICsAPNResTIncTx,
       "jnxMbgPgwV2ICsUnknownRx": jnxMbgPgwV2ICsUnknownRx,
       "jnxMbgPgwV2ICsUnknownTx": jnxMbgPgwV2ICsUnknownTx,
       "jnxMbgPgwV1ProtocolErrRx": jnxMbgPgwV1ProtocolErrRx,
       "jnxMbgPgwV1UnSupportedMsgRx": jnxMbgPgwV1UnSupportedMsgRx,
       "jnxMbgPgwV1T3RespTmrExpRx": jnxMbgPgwV1T3RespTmrExpRx,
       "jnxMbgPgwV1GlbNumMsgRx": jnxMbgPgwV1GlbNumMsgRx,
       "jnxMbgPgwV1GlbNumMsgTx": jnxMbgPgwV1GlbNumMsgTx,
       "jnxMbgPgwV1GlbNumBytesRx": jnxMbgPgwV1GlbNumBytesRx,
       "jnxMbgPgwV1GlbNumBytesTx": jnxMbgPgwV1GlbNumBytesTx,
       "jnxMbgPgwV1GlbEchoReqRx": jnxMbgPgwV1GlbEchoReqRx,
       "jnxMbgPgwV1GlbEchoReqTx": jnxMbgPgwV1GlbEchoReqTx,
       "jnxMbgPgwV1GlbEchoRespRx": jnxMbgPgwV1GlbEchoRespRx,
       "jnxMbgPgwV1GlbEchoRespTx": jnxMbgPgwV1GlbEchoRespTx,
       "jnxMbgPgwV1VerNotSupRx": jnxMbgPgwV1VerNotSupRx,
       "jnxMbgPgwV1VerNotSupTx": jnxMbgPgwV1VerNotSupTx,
       "jnxMbgPgwV1CrtPdpCxtReqRx": jnxMbgPgwV1CrtPdpCxtReqRx,
       "jnxMbgPgwV1CrtPdpCxtReqTx": jnxMbgPgwV1CrtPdpCxtReqTx,
       "jnxMbgPgwV1CrtPdpCxtRspRx": jnxMbgPgwV1CrtPdpCxtRspRx,
       "jnxMbgPgwV1CrtPdpCxtRspTx": jnxMbgPgwV1CrtPdpCxtRspTx,
       "jnxMbgPgwV1UpdPdpCxtReqRx": jnxMbgPgwV1UpdPdpCxtReqRx,
       "jnxMbgPgwV1UpdPdpCxtReqTx": jnxMbgPgwV1UpdPdpCxtReqTx,
       "jnxMbgPgwV1UpdPdpCxtRspRx": jnxMbgPgwV1UpdPdpCxtRspRx,
       "jnxMbgPgwV1UpdPdpCxtRspTx": jnxMbgPgwV1UpdPdpCxtRspTx,
       "jnxMbgPgwV1DelPdpCxtReqRx": jnxMbgPgwV1DelPdpCxtReqRx,
       "jnxMbgPgwV1DelPdpCxtReqTx": jnxMbgPgwV1DelPdpCxtReqTx,
       "jnxMbgPgwV1DelPdpCxtRspRx": jnxMbgPgwV1DelPdpCxtRspRx,
       "jnxMbgPgwV1DelPdpCxtRspTx": jnxMbgPgwV1DelPdpCxtRspTx,
       "jnxMbgPgwV1CrtAAPdpCxtReqRx": jnxMbgPgwV1CrtAAPdpCxtReqRx,
       "jnxMbgPgwV1CrtAAPdpCxtReqTx": jnxMbgPgwV1CrtAAPdpCxtReqTx,
       "jnxMbgPgwV1CrtAAPdpCxtRspRx": jnxMbgPgwV1CrtAAPdpCxtRspRx,
       "jnxMbgPgwV1CrtAAPdpCxtRspTx": jnxMbgPgwV1CrtAAPdpCxtRspTx,
       "jnxMbgPgwV1DelAAPdpCxtReqRx": jnxMbgPgwV1DelAAPdpCxtReqRx,
       "jnxMbgPgwV1DelAAPdpCxtReqTx": jnxMbgPgwV1DelAAPdpCxtReqTx,
       "jnxMbgPgwV1DelAAPdpCxtRspRx": jnxMbgPgwV1DelAAPdpCxtRspRx,
       "jnxMbgPgwV1DelAAPdpCxtRspTx": jnxMbgPgwV1DelAAPdpCxtRspTx,
       "jnxMbgPgwV1ErrorIndRx": jnxMbgPgwV1ErrorIndRx,
       "jnxMbgPgwV1ErrorIndTx": jnxMbgPgwV1ErrorIndTx,
       "jnxMbgPgwV1NotifReqRx": jnxMbgPgwV1NotifReqRx,
       "jnxMbgPgwV1NotifReqTx": jnxMbgPgwV1NotifReqTx,
       "jnxMbgPgwV1NotifRspRx": jnxMbgPgwV1NotifRspRx,
       "jnxMbgPgwV1NotifRspTx": jnxMbgPgwV1NotifRspTx,
       "jnxMbgPgwV1NotifRejReqRx": jnxMbgPgwV1NotifRejReqRx,
       "jnxMbgPgwV1NotifRejReqTx": jnxMbgPgwV1NotifRejReqTx,
       "jnxMbgPgwV1NotifRejRspRx": jnxMbgPgwV1NotifRejRspRx,
       "jnxMbgPgwV1NotifRejRspTx": jnxMbgPgwV1NotifRejRspTx,
       "jnxMbgPgwV1RtInfReqRx": jnxMbgPgwV1RtInfReqRx,
       "jnxMbgPgwV1RtInfReqTx": jnxMbgPgwV1RtInfReqTx,
       "jnxMbgPgwV1RtInfRspRx": jnxMbgPgwV1RtInfRspRx,
       "jnxMbgPgwV1RtInfRspTx": jnxMbgPgwV1RtInfRspTx,
       "jnxMbgPgwV1FailRptReqRx": jnxMbgPgwV1FailRptReqRx,
       "jnxMbgPgwV1FailRptReqTx": jnxMbgPgwV1FailRptReqTx,
       "jnxMbgPgwV1FailRptRspRx": jnxMbgPgwV1FailRptRspRx,
       "jnxMbgPgwV1FailRptRspTx": jnxMbgPgwV1FailRptRspTx,
       "jnxMbgPgwV1NotMSPresReqRx": jnxMbgPgwV1NotMSPresReqRx,
       "jnxMbgPgwV1NotMSPresReqTx": jnxMbgPgwV1NotMSPresReqTx,
       "jnxMbgPgwV1NotMSPresRspRx": jnxMbgPgwV1NotMSPresRspRx,
       "jnxMbgPgwV1NotMSPresRspTx": jnxMbgPgwV1NotMSPresRspTx,
       "jnxMbgPgwV1ICsReqAcceptedRx": jnxMbgPgwV1ICsReqAcceptedRx,
       "jnxMbgPgwV1ICsReqAcceptedTx": jnxMbgPgwV1ICsReqAcceptedTx,
       "jnxMbgPgwV1ICsNonExistRx": jnxMbgPgwV1ICsNonExistRx,
       "jnxMbgPgwV1ICsNonExistTx": jnxMbgPgwV1ICsNonExistTx,
       "jnxMbgPgwV1ICsInvMsgFmtRx": jnxMbgPgwV1ICsInvMsgFmtRx,
       "jnxMbgPgwV1ICsInvMsgFmtTx": jnxMbgPgwV1ICsInvMsgFmtTx,
       "jnxMbgPgwV1ICsIMSINotKnownRx": jnxMbgPgwV1ICsIMSINotKnownRx,
       "jnxMbgPgwV1ICsIMSINotKnownTx": jnxMbgPgwV1ICsIMSINotKnownTx,
       "jnxMbgPgwV1ICsMSGRPSDetachRx": jnxMbgPgwV1ICsMSGRPSDetachRx,
       "jnxMbgPgwV1ICsMSGRPSDetachTx": jnxMbgPgwV1ICsMSGRPSDetachTx,
       "jnxMbgPgwV1ICsMSNotGRPSRespRx": jnxMbgPgwV1ICsMSNotGRPSRespRx,
       "jnxMbgPgwV1ICsMSNotGRPSRespTx": jnxMbgPgwV1ICsMSNotGRPSRespTx,
       "jnxMbgPgwV1ICsMSRefusesRx": jnxMbgPgwV1ICsMSRefusesRx,
       "jnxMbgPgwV1ICsMSRefusesTx": jnxMbgPgwV1ICsMSRefusesTx,
       "jnxMbgPgwV1ICsVerNotSuppRx": jnxMbgPgwV1ICsVerNotSuppRx,
       "jnxMbgPgwV1ICsVerNotSuppTx": jnxMbgPgwV1ICsVerNotSuppTx,
       "jnxMbgPgwV1ICsNoResRx": jnxMbgPgwV1ICsNoResRx,
       "jnxMbgPgwV1ICsNoResTx": jnxMbgPgwV1ICsNoResTx,
       "jnxMbgPgwV1ICsServNotSuppRx": jnxMbgPgwV1ICsServNotSuppRx,
       "jnxMbgPgwV1ICsServNotSuppTx": jnxMbgPgwV1ICsServNotSuppTx,
       "jnxMbgPgwV1ICsManIEIncrtRx": jnxMbgPgwV1ICsManIEIncrtRx,
       "jnxMbgPgwV1ICsManIEIncrtTx": jnxMbgPgwV1ICsManIEIncrtTx,
       "jnxMbgPgwV1ICsManIEMissRx": jnxMbgPgwV1ICsManIEMissRx,
       "jnxMbgPgwV1ICsManIEMissTx": jnxMbgPgwV1ICsManIEMissTx,
       "jnxMbgPgwV1ICsOptIEIncrtRx": jnxMbgPgwV1ICsOptIEIncrtRx,
       "jnxMbgPgwV1ICsOptIEIncrtTx": jnxMbgPgwV1ICsOptIEIncrtTx,
       "jnxMbgPgwV1ICsSysFailRx": jnxMbgPgwV1ICsSysFailRx,
       "jnxMbgPgwV1ICsSysFailTx": jnxMbgPgwV1ICsSysFailTx,
       "jnxMbgPgwV1ICsRoamRestrictRx": jnxMbgPgwV1ICsRoamRestrictRx,
       "jnxMbgPgwV1ICsRoamRestrictTx": jnxMbgPgwV1ICsRoamRestrictTx,
       "jnxMbgPgwV1ICsPTMSISigMMRx": jnxMbgPgwV1ICsPTMSISigMMRx,
       "jnxMbgPgwV1ICsPTMSISigMMTx": jnxMbgPgwV1ICsPTMSISigMMTx,
       "jnxMbgPgwV1ICsGPRSConnSuppRx": jnxMbgPgwV1ICsGPRSConnSuppRx,
       "jnxMbgPgwV1ICsGPRSConnSuppTx": jnxMbgPgwV1ICsGPRSConnSuppTx,
       "jnxMbgPgwV1ICsAuthFailRx": jnxMbgPgwV1ICsAuthFailRx,
       "jnxMbgPgwV1ICsAuthFailTx": jnxMbgPgwV1ICsAuthFailTx,
       "jnxMbgPgwV1ICsUserAuthFailRx": jnxMbgPgwV1ICsUserAuthFailRx,
       "jnxMbgPgwV1ICsUserAuthFailTx": jnxMbgPgwV1ICsUserAuthFailTx,
       "jnxMbgPgwV1ICsCtxNotFndRx": jnxMbgPgwV1ICsCtxNotFndRx,
       "jnxMbgPgwV1ICsCtxNotFndTx": jnxMbgPgwV1ICsCtxNotFndTx,
       "jnxMbgPgwV1ICsAllDynPDPAdRx": jnxMbgPgwV1ICsAllDynPDPAdRx,
       "jnxMbgPgwV1ICsAllDynPDPAdTx": jnxMbgPgwV1ICsAllDynPDPAdTx,
       "jnxMbgPgwV1ICsNoMemRx": jnxMbgPgwV1ICsNoMemRx,
       "jnxMbgPgwV1ICsNoMemTx": jnxMbgPgwV1ICsNoMemTx,
       "jnxMbgPgwV1ICsRelocFailRx": jnxMbgPgwV1ICsRelocFailRx,
       "jnxMbgPgwV1ICsRelocFailTx": jnxMbgPgwV1ICsRelocFailTx,
       "jnxMbgPgwV1ICsUnkManExhdrRx": jnxMbgPgwV1ICsUnkManExhdrRx,
       "jnxMbgPgwV1ICsUnkManExhdrTx": jnxMbgPgwV1ICsUnkManExhdrTx,
       "jnxMbgPgwV1ICsSMANTTFTEr1Rx": jnxMbgPgwV1ICsSMANTTFTEr1Rx,
       "jnxMbgPgwV1ICsSMANTTFTEr1Tx": jnxMbgPgwV1ICsSMANTTFTEr1Tx,
       "jnxMbgPgwV1ICsSYNTFTErr2Rx": jnxMbgPgwV1ICsSYNTFTErr2Rx,
       "jnxMbgPgwV1ICsSYNTFTErr2Tx": jnxMbgPgwV1ICsSYNTFTErr2Tx,
       "jnxMbgPgwV1ICsSMNTPkFlEr1Rx": jnxMbgPgwV1ICsSMNTPkFlEr1Rx,
       "jnxMbgPgwV1ICsSMNTPkFlEr1Tx": jnxMbgPgwV1ICsSMNTPkFlEr1Tx,
       "jnxMbgPgwV1ICsSYNPkFlErr2Rx": jnxMbgPgwV1ICsSYNPkFlErr2Rx,
       "jnxMbgPgwV1ICsSYNPkFlErr2Tx": jnxMbgPgwV1ICsSYNPkFlErr2Tx,
       "jnxMbgPgwV1ICsMissUnknAPNRx": jnxMbgPgwV1ICsMissUnknAPNRx,
       "jnxMbgPgwV1ICsMissUnknAPNTx": jnxMbgPgwV1ICsMissUnknAPNTx,
       "jnxMbgPgwV1ICsUnknPDPAdRx": jnxMbgPgwV1ICsUnknPDPAdRx,
       "jnxMbgPgwV1ICsUnknPDPAdTx": jnxMbgPgwV1ICsUnknPDPAdTx,
       "jnxMbgPgwV1ICsNoTFTCtxExRx": jnxMbgPgwV1ICsNoTFTCtxExRx,
       "jnxMbgPgwV1ICsNoTFTCtxExTx": jnxMbgPgwV1ICsNoTFTCtxExTx,
       "jnxMbgPgwV0ProtocolErrRx": jnxMbgPgwV0ProtocolErrRx,
       "jnxMbgPgwV0UnSupportedMsgRx": jnxMbgPgwV0UnSupportedMsgRx,
       "jnxMbgPgwV0T3RespTmrExpRx": jnxMbgPgwV0T3RespTmrExpRx,
       "jnxMbgPgwV0GlbNumMsgRx": jnxMbgPgwV0GlbNumMsgRx,
       "jnxMbgPgwV0GlbNumMsgTx": jnxMbgPgwV0GlbNumMsgTx,
       "jnxMbgPgwV0GlbNumBytesRx": jnxMbgPgwV0GlbNumBytesRx,
       "jnxMbgPgwV0GlbNumBytesTx": jnxMbgPgwV0GlbNumBytesTx,
       "jnxMbgPgwV0GlbEchoReqRx": jnxMbgPgwV0GlbEchoReqRx,
       "jnxMbgPgwV0GlbEchoReqTx": jnxMbgPgwV0GlbEchoReqTx,
       "jnxMbgPgwV0GlbEchoRespRx": jnxMbgPgwV0GlbEchoRespRx,
       "jnxMbgPgwV0GlbEchoRespTx": jnxMbgPgwV0GlbEchoRespTx,
       "jnxMbgPgwV0GlbVerNotSupRx": jnxMbgPgwV0GlbVerNotSupRx,
       "jnxMbgPgwV0GlbVerNotSupTx": jnxMbgPgwV0GlbVerNotSupTx,
       "jnxMbgPgwV0GlbCrtPdpCxtReqRx": jnxMbgPgwV0GlbCrtPdpCxtReqRx,
       "jnxMbgPgwV0GlbCrtPdpCxtReqTx": jnxMbgPgwV0GlbCrtPdpCxtReqTx,
       "jnxMbgPgwV0GlbCrtPdpCxtRspRx": jnxMbgPgwV0GlbCrtPdpCxtRspRx,
       "jnxMbgPgwV0GlbCrtPdpCxtRspTx": jnxMbgPgwV0GlbCrtPdpCxtRspTx,
       "jnxMbgPgwV0GlbUpdPdpCxtReqRx": jnxMbgPgwV0GlbUpdPdpCxtReqRx,
       "jnxMbgPgwV0GlbUpdPdpCxtReqTx": jnxMbgPgwV0GlbUpdPdpCxtReqTx,
       "jnxMbgPgwV0GlbUpdPdpCxtRspRx": jnxMbgPgwV0GlbUpdPdpCxtRspRx,
       "jnxMbgPgwV0GlbUpdPdpCxtRspTx": jnxMbgPgwV0GlbUpdPdpCxtRspTx,
       "jnxMbgPgwV0GlbDelPdpCxtReqRx": jnxMbgPgwV0GlbDelPdpCxtReqRx,
       "jnxMbgPgwV0GlbDelPdpCxtReqTx": jnxMbgPgwV0GlbDelPdpCxtReqTx,
       "jnxMbgPgwV0GlbDelPdpCxtRspRx": jnxMbgPgwV0GlbDelPdpCxtRspRx,
       "jnxMbgPgwV0GlbDelPdpCxtRspTx": jnxMbgPgwV0GlbDelPdpCxtRspTx,
       "jnxMbgPgwV0GlbCrtAAPdpCxtReqRx": jnxMbgPgwV0GlbCrtAAPdpCxtReqRx,
       "jnxMbgPgwV0GlbCrtAAPdpCxtReqTx": jnxMbgPgwV0GlbCrtAAPdpCxtReqTx,
       "jnxMbgPgwV0GlbCrtAAPdpCxtRspRx": jnxMbgPgwV0GlbCrtAAPdpCxtRspRx,
       "jnxMbgPgwV0GlbCrtAAPdpCxtRspTx": jnxMbgPgwV0GlbCrtAAPdpCxtRspTx,
       "jnxMbgPgwV0GlbDelAAPdpCxtReqRx": jnxMbgPgwV0GlbDelAAPdpCxtReqRx,
       "jnxMbgPgwV0GlbDelAAPdpCxtReqTx": jnxMbgPgwV0GlbDelAAPdpCxtReqTx,
       "jnxMbgPgwV0GlbDelAAPdpCxtRspRx": jnxMbgPgwV0GlbDelAAPdpCxtRspRx,
       "jnxMbgPgwV0GlbDelAAPdpCxtRspTx": jnxMbgPgwV0GlbDelAAPdpCxtRspTx,
       "jnxMbgPgwV0GlbErrorIndRx": jnxMbgPgwV0GlbErrorIndRx,
       "jnxMbgPgwV0GlbErrorIndTx": jnxMbgPgwV0GlbErrorIndTx,
       "jnxMbgPgwV0GlbNotifReqRx": jnxMbgPgwV0GlbNotifReqRx,
       "jnxMbgPgwV0GlbNotifReqTx": jnxMbgPgwV0GlbNotifReqTx,
       "jnxMbgPgwV0GlbNotifRspRx": jnxMbgPgwV0GlbNotifRspRx,
       "jnxMbgPgwV0GlbNotifRspTx": jnxMbgPgwV0GlbNotifRspTx,
       "jnxMbgPgwV0GlbNotifRejReqRx": jnxMbgPgwV0GlbNotifRejReqRx,
       "jnxMbgPgwV0GlbNotifRejReqTx": jnxMbgPgwV0GlbNotifRejReqTx,
       "jnxMbgPgwV0GlbNotifRejRspRx": jnxMbgPgwV0GlbNotifRejRspRx,
       "jnxMbgPgwV0GlbNotifRejRspTx": jnxMbgPgwV0GlbNotifRejRspTx,
       "jnxMbgPgwV0GlbRtInfReqRx": jnxMbgPgwV0GlbRtInfReqRx,
       "jnxMbgPgwV0GlbRtInfReqTx": jnxMbgPgwV0GlbRtInfReqTx,
       "jnxMbgPgwV0GlbRtInfRspRx": jnxMbgPgwV0GlbRtInfRspRx,
       "jnxMbgPgwV0GlbRtInfRspTx": jnxMbgPgwV0GlbRtInfRspTx,
       "jnxMbgPgwV0GlbFailRptReqRx": jnxMbgPgwV0GlbFailRptReqRx,
       "jnxMbgPgwV0GlbFailRptReqTx": jnxMbgPgwV0GlbFailRptReqTx,
       "jnxMbgPgwV0GlbFailRptRspRx": jnxMbgPgwV0GlbFailRptRspRx,
       "jnxMbgPgwV0GlbFailRptRspTx": jnxMbgPgwV0GlbFailRptRspTx,
       "jnxMbgPgwV0GlbNotMSPresReqRx": jnxMbgPgwV0GlbNotMSPresReqRx,
       "jnxMbgPgwV0GlbNotMSPresReqTx": jnxMbgPgwV0GlbNotMSPresReqTx,
       "jnxMbgPgwV0GlbNotMSPresRspRx": jnxMbgPgwV0GlbNotMSPresRspRx,
       "jnxMbgPgwV0GlbNotMSPresRspTx": jnxMbgPgwV0GlbNotMSPresRspTx,
       "jnxMbgPgwV0ICsReqAcceptedRx": jnxMbgPgwV0ICsReqAcceptedRx,
       "jnxMbgPgwV0ICsReqAcceptedTx": jnxMbgPgwV0ICsReqAcceptedTx,
       "jnxMbgPgwV0ICsNonExistRx": jnxMbgPgwV0ICsNonExistRx,
       "jnxMbgPgwV0ICsNonExistTx": jnxMbgPgwV0ICsNonExistTx,
       "jnxMbgPgwV0ICsInvMsgFmtRx": jnxMbgPgwV0ICsInvMsgFmtRx,
       "jnxMbgPgwV0ICsInvMsgFmtTx": jnxMbgPgwV0ICsInvMsgFmtTx,
       "jnxMbgPgwV0ICsIMSINotKnownRx": jnxMbgPgwV0ICsIMSINotKnownRx,
       "jnxMbgPgwV0ICsIMSINotKnownTx": jnxMbgPgwV0ICsIMSINotKnownTx,
       "jnxMbgPgwV0ICsMSGRPSDetachRx": jnxMbgPgwV0ICsMSGRPSDetachRx,
       "jnxMbgPgwV0ICsMSGRPSDetachTx": jnxMbgPgwV0ICsMSGRPSDetachTx,
       "jnxMbgPgwV0ICsMSNotGRPSRespRx": jnxMbgPgwV0ICsMSNotGRPSRespRx,
       "jnxMbgPgwV0ICsMSNotGRPSRespTx": jnxMbgPgwV0ICsMSNotGRPSRespTx,
       "jnxMbgPgwV0ICsMSRefusesRx": jnxMbgPgwV0ICsMSRefusesRx,
       "jnxMbgPgwV0ICsMSRefusesTx": jnxMbgPgwV0ICsMSRefusesTx,
       "jnxMbgPgwV0ICsVerNotSuppRx": jnxMbgPgwV0ICsVerNotSuppRx,
       "jnxMbgPgwV0ICsVerNotSuppTx": jnxMbgPgwV0ICsVerNotSuppTx,
       "jnxMbgPgwV0ICsNoResRx": jnxMbgPgwV0ICsNoResRx,
       "jnxMbgPgwV0ICsNoResTx": jnxMbgPgwV0ICsNoResTx,
       "jnxMbgPgwV0ICsServNotSuppRx": jnxMbgPgwV0ICsServNotSuppRx,
       "jnxMbgPgwV0ICsServNotSuppTx": jnxMbgPgwV0ICsServNotSuppTx,
       "jnxMbgPgwV0ICsManIEIncrtRx": jnxMbgPgwV0ICsManIEIncrtRx,
       "jnxMbgPgwV0ICsManIEIncrtTx": jnxMbgPgwV0ICsManIEIncrtTx,
       "jnxMbgPgwV0ICsManIEMissRx": jnxMbgPgwV0ICsManIEMissRx,
       "jnxMbgPgwV0ICsManIEMissTx": jnxMbgPgwV0ICsManIEMissTx,
       "jnxMbgPgwV0ICsOptIEIncrtRx": jnxMbgPgwV0ICsOptIEIncrtRx,
       "jnxMbgPgwV0ICsOptIEIncrtTx": jnxMbgPgwV0ICsOptIEIncrtTx,
       "jnxMbgPgwV0ICsSysFailRx": jnxMbgPgwV0ICsSysFailRx,
       "jnxMbgPgwV0ICsSysFailTx": jnxMbgPgwV0ICsSysFailTx,
       "jnxMbgPgwV0ICsRoamRestrictRx": jnxMbgPgwV0ICsRoamRestrictRx,
       "jnxMbgPgwV0ICsRoamRestrictTx": jnxMbgPgwV0ICsRoamRestrictTx,
       "jnxMbgPgwV0ICsPTMSISigMMRx": jnxMbgPgwV0ICsPTMSISigMMRx,
       "jnxMbgPgwV0ICsPTMSISigMMTx": jnxMbgPgwV0ICsPTMSISigMMTx,
       "jnxMbgPgwV0ICsGPRSConnSuppRx": jnxMbgPgwV0ICsGPRSConnSuppRx,
       "jnxMbgPgwV0ICsGPRSConnSuppTx": jnxMbgPgwV0ICsGPRSConnSuppTx,
       "jnxMbgPgwV0ICsAuthFailRx": jnxMbgPgwV0ICsAuthFailRx,
       "jnxMbgPgwV0ICsAuthFailTx": jnxMbgPgwV0ICsAuthFailTx,
       "jnxMbgPgwV0ICsUserAuthFailRx": jnxMbgPgwV0ICsUserAuthFailRx,
       "jnxMbgPgwV0ICsUserAuthFailTx": jnxMbgPgwV0ICsUserAuthFailTx,
       "jnxMbgPgwGtpV2ICsLclDetRx": jnxMbgPgwGtpV2ICsLclDetRx,
       "jnxMbgPgwGtpV2ICsLclDetTx": jnxMbgPgwGtpV2ICsLclDetTx,
       "jnxMbgPgwGtpV2ICsCmpDetRx": jnxMbgPgwGtpV2ICsCmpDetRx,
       "jnxMbgPgwGtpV2ICsCmpDetTx": jnxMbgPgwGtpV2ICsCmpDetTx,
       "jnxMbgPgwGtpV2ICsRATChgRx": jnxMbgPgwGtpV2ICsRATChgRx,
       "jnxMbgPgwGtpV2ICsRATChgTx": jnxMbgPgwGtpV2ICsRATChgTx,
       "jnxMbgPgwGtpV2ICsISRDeactRx": jnxMbgPgwGtpV2ICsISRDeactRx,
       "jnxMbgPgwGtpV2ICsISRDeactTx": jnxMbgPgwGtpV2ICsISRDeactTx,
       "jnxMbgPgwGtpV2ICsEIFRNCEnRx": jnxMbgPgwGtpV2ICsEIFRNCEnRx,
       "jnxMbgPgwGtpV2ICsEIFRNCEnTx": jnxMbgPgwGtpV2ICsEIFRNCEnTx,
       "jnxMbgPgwGtpV2ICsSemErTADRx": jnxMbgPgwGtpV2ICsSemErTADRx,
       "jnxMbgPgwGtpV2ICsSemErTADTx": jnxMbgPgwGtpV2ICsSemErTADTx,
       "jnxMbgPgwGtpV2ICsSynErTADRx": jnxMbgPgwGtpV2ICsSynErTADRx,
       "jnxMbgPgwGtpV2ICsSynErTADTx": jnxMbgPgwGtpV2ICsSynErTADTx,
       "jnxMbgPgwGtpV2ICsRMValRcvRx": jnxMbgPgwGtpV2ICsRMValRcvRx,
       "jnxMbgPgwGtpV2ICsRMValRcvTx": jnxMbgPgwGtpV2ICsRMValRcvTx,
       "jnxMbgPgwGtpV2ICsRPrNtRspRx": jnxMbgPgwGtpV2ICsRPrNtRspRx,
       "jnxMbgPgwGtpV2ICsRPrNtRspTx": jnxMbgPgwGtpV2ICsRPrNtRspTx,
       "jnxMbgPgwGtpV2ICsColNWReqRx": jnxMbgPgwGtpV2ICsColNWReqRx,
       "jnxMbgPgwGtpV2ICsColNWReqTx": jnxMbgPgwGtpV2ICsColNWReqTx,
       "jnxMbgPgwGtpV2ICsUnPgUESusRx": jnxMbgPgwGtpV2ICsUnPgUESusRx,
       "jnxMbgPgwGtpV2ICsUnPgUESusTx": jnxMbgPgwGtpV2ICsUnPgUESusTx,
       "jnxMbgPgwGtpV2ICsInvTotLenRx": jnxMbgPgwGtpV2ICsInvTotLenRx,
       "jnxMbgPgwGtpV2ICsInvTotLenTx": jnxMbgPgwGtpV2ICsInvTotLenTx,
       "jnxMbgPgwGtpV2ICsDtForNtSupRx": jnxMbgPgwGtpV2ICsDtForNtSupRx,
       "jnxMbgPgwGtpV2ICsDtForNtSupTx": jnxMbgPgwGtpV2ICsDtForNtSupTx,
       "jnxMbgPgwGtpV2ICsInReFRePrRx": jnxMbgPgwGtpV2ICsInReFRePrRx,
       "jnxMbgPgwGtpV2ICsInReFRePrTx": jnxMbgPgwGtpV2ICsInReFRePrTx,
       "jnxMbgPgwGtpV2ICsInvPrRx": jnxMbgPgwGtpV2ICsInvPrRx,
       "jnxMbgPgwGtpV2ICsInvPrTx": jnxMbgPgwGtpV2ICsInvPrTx,
       "jnxMbgPgwV1InitPdpCxtReqRx": jnxMbgPgwV1InitPdpCxtReqRx,
       "jnxMbgPgwV1InitPdpCxtReqTx": jnxMbgPgwV1InitPdpCxtReqTx,
       "jnxMbgPgwV1InitPdpCxtRspRx": jnxMbgPgwV1InitPdpCxtRspRx,
       "jnxMbgPgwV1InitPdpCxtRspTx": jnxMbgPgwV1InitPdpCxtRspTx,
       "jnxMbgPgwV2SuspNotifRx": jnxMbgPgwV2SuspNotifRx,
       "jnxMbgPgwV2SuspNotifTx": jnxMbgPgwV2SuspNotifTx,
       "jnxMbgPgwV2SuspAckRx": jnxMbgPgwV2SuspAckRx,
       "jnxMbgPgwV2SuspAckTx": jnxMbgPgwV2SuspAckTx,
       "jnxMbgPgwV2ResumeNotifRx": jnxMbgPgwV2ResumeNotifRx,
       "jnxMbgPgwV2ResumeNotifTx": jnxMbgPgwV2ResumeNotifTx,
       "jnxMbgPgwV2ResumeAckRx": jnxMbgPgwV2ResumeAckRx,
       "jnxMbgPgwV2ResumeAckTx": jnxMbgPgwV2ResumeAckTx,
       "jnxMbgPgwV2PiggybackMsgRx": jnxMbgPgwV2PiggybackMsgRx,
       "jnxMbgPgwV2PiggybackMsgTx": jnxMbgPgwV2PiggybackMsgTx,
       "jnxMbgPgwGtpIfStatsTable": jnxMbgPgwGtpIfStatsTable,
       "jnxMbgPgwGtpIfStatsEntry": jnxMbgPgwGtpIfStatsEntry,
       "jnxMbgPgwIfIndex": jnxMbgPgwIfIndex,
       "jnxMbgPgwIfType": jnxMbgPgwIfType,
       "jnxMbgPgwIfRxPacketsDropped": jnxMbgPgwIfRxPacketsDropped,
       "jnxMbgPgwIfPacketAllocFail": jnxMbgPgwIfPacketAllocFail,
       "jnxMbgPgwIfPacketSendFail": jnxMbgPgwIfPacketSendFail,
       "jnxMbgPgwIfIPVerErrRx": jnxMbgPgwIfIPVerErrRx,
       "jnxMbgPgwIfIPProtoErrRx": jnxMbgPgwIfIPProtoErrRx,
       "jnxMbgPgwIfGTPPortErrRx": jnxMbgPgwIfGTPPortErrRx,
       "jnxMbgPgwIfGTPUnknVerRx": jnxMbgPgwIfGTPUnknVerRx,
       "jnxMbgPgwIfPcktLenErrRx": jnxMbgPgwIfPcktLenErrRx,
       "jnxMbgPgwIfUnknMsgRx": jnxMbgPgwIfUnknMsgRx,
       "jnxMbgPgwIfV2ProtocolErrRx": jnxMbgPgwIfV2ProtocolErrRx,
       "jnxMbgPgwIfV2UnSupportedMsgRx": jnxMbgPgwIfV2UnSupportedMsgRx,
       "jnxMbgPgwIfV2T3RespTmrExpRx": jnxMbgPgwIfV2T3RespTmrExpRx,
       "jnxMbgPgwIfV2GlbNumMsgRx": jnxMbgPgwIfV2GlbNumMsgRx,
       "jnxMbgPgwIfV2GlbNumMsgTx": jnxMbgPgwIfV2GlbNumMsgTx,
       "jnxMbgPgwIfV2GlbNumBytesRx": jnxMbgPgwIfV2GlbNumBytesRx,
       "jnxMbgPgwIfV2GlbNumBytesTx": jnxMbgPgwIfV2GlbNumBytesTx,
       "jnxMbgPgwIfV2GlbEchoReqRx": jnxMbgPgwIfV2GlbEchoReqRx,
       "jnxMbgPgwIfV2GlbEchoReqTx": jnxMbgPgwIfV2GlbEchoReqTx,
       "jnxMbgPgwIfV2GlbEchoRespRx": jnxMbgPgwIfV2GlbEchoRespRx,
       "jnxMbgPgwIfV2GlbEchoRespTx": jnxMbgPgwIfV2GlbEchoRespTx,
       "jnxMbgPgwIfV2VerNotSupRx": jnxMbgPgwIfV2VerNotSupRx,
       "jnxMbgPgwIfV2VerNotSupTx": jnxMbgPgwIfV2VerNotSupTx,
       "jnxMbgPgwIfV2CreateSessReqRx": jnxMbgPgwIfV2CreateSessReqRx,
       "jnxMbgPgwIfV2CreateSessReqTx": jnxMbgPgwIfV2CreateSessReqTx,
       "jnxMbgPgwIfV2CreateSessRspRx": jnxMbgPgwIfV2CreateSessRspRx,
       "jnxMbgPgwIfV2CreateSessRspTx": jnxMbgPgwIfV2CreateSessRspTx,
       "jnxMbgPgwIfV2ModBrReqRx": jnxMbgPgwIfV2ModBrReqRx,
       "jnxMbgPgwIfV2ModBrReqTx": jnxMbgPgwIfV2ModBrReqTx,
       "jnxMbgPgwIfV2ModBrRspRx": jnxMbgPgwIfV2ModBrRspRx,
       "jnxMbgPgwIfV2ModBrRspTx": jnxMbgPgwIfV2ModBrRspTx,
       "jnxMbgPgwIfV2DelSessReqRx": jnxMbgPgwIfV2DelSessReqRx,
       "jnxMbgPgwIfV2DelSessReqTx": jnxMbgPgwIfV2DelSessReqTx,
       "jnxMbgPgwIfV2DelSessRspRx": jnxMbgPgwIfV2DelSessRspRx,
       "jnxMbgPgwIfV2DelSessRspTx": jnxMbgPgwIfV2DelSessRspTx,
       "jnxMbgPgwIfV2CrtBrReqRx": jnxMbgPgwIfV2CrtBrReqRx,
       "jnxMbgPgwIfV2CrtBrReqTx": jnxMbgPgwIfV2CrtBrReqTx,
       "jnxMbgPgwIfV2CrtBrRspRx": jnxMbgPgwIfV2CrtBrRspRx,
       "jnxMbgPgwIfV2CrtBrRspTx": jnxMbgPgwIfV2CrtBrRspTx,
       "jnxMbgPgwIfV2UpdBrReqRx": jnxMbgPgwIfV2UpdBrReqRx,
       "jnxMbgPgwIfV2UpdBrReqTx": jnxMbgPgwIfV2UpdBrReqTx,
       "jnxMbgPgwIfV2UpdBrRspRx": jnxMbgPgwIfV2UpdBrRspRx,
       "jnxMbgPgwIfV2UpdBrRspTx": jnxMbgPgwIfV2UpdBrRspTx,
       "jnxMbgPgwIfV2DelBrReqRx": jnxMbgPgwIfV2DelBrReqRx,
       "jnxMbgPgwIfV2DelBrReqTx": jnxMbgPgwIfV2DelBrReqTx,
       "jnxMbgPgwIfV2DelBrRspRx": jnxMbgPgwIfV2DelBrRspRx,
       "jnxMbgPgwIfV2DelBrRspTx": jnxMbgPgwIfV2DelBrRspTx,
       "jnxMbgPgwIfV2DelConnSetReqRx": jnxMbgPgwIfV2DelConnSetReqRx,
       "jnxMbgPgwIfV2DelConnSetReqTx": jnxMbgPgwIfV2DelConnSetReqTx,
       "jnxMbgPgwIfV2DelConnSetRspRx": jnxMbgPgwIfV2DelConnSetRspRx,
       "jnxMbgPgwIfV2DelConnSetRspTx": jnxMbgPgwIfV2DelConnSetRspTx,
       "jnxMbgPgwIfV2UpdConnSetReqRx": jnxMbgPgwIfV2UpdConnSetReqRx,
       "jnxMbgPgwIfV2UpdConnSetReqTx": jnxMbgPgwIfV2UpdConnSetReqTx,
       "jnxMbgPgwIfV2UpdConnSetRspRx": jnxMbgPgwIfV2UpdConnSetRspRx,
       "jnxMbgPgwIfV2UpdConnSetRspTx": jnxMbgPgwIfV2UpdConnSetRspTx,
       "jnxMbgPgwIfV2ModBrCmdRx": jnxMbgPgwIfV2ModBrCmdRx,
       "jnxMbgPgwIfV2ModBrCmdTx": jnxMbgPgwIfV2ModBrCmdTx,
       "jnxMbgPgwIfV2ModBrFlrIndRx": jnxMbgPgwIfV2ModBrFlrIndRx,
       "jnxMbgPgwIfV2ModBrFlrIndTx": jnxMbgPgwIfV2ModBrFlrIndTx,
       "jnxMbgPgwIfV2DelBrCmdRx": jnxMbgPgwIfV2DelBrCmdRx,
       "jnxMbgPgwIfV2DelBrCmdTx": jnxMbgPgwIfV2DelBrCmdTx,
       "jnxMbgPgwIfV2DelBrFlrIndRx": jnxMbgPgwIfV2DelBrFlrIndRx,
       "jnxMbgPgwIfV2DelBrFlrIndTx": jnxMbgPgwIfV2DelBrFlrIndTx,
       "jnxMbgPgwIfV2BrResCmdRx": jnxMbgPgwIfV2BrResCmdRx,
       "jnxMbgPgwIfV2BrResCmdTx": jnxMbgPgwIfV2BrResCmdTx,
       "jnxMbgPgwIfV2BrResFlrIndRx": jnxMbgPgwIfV2BrResFlrIndRx,
       "jnxMbgPgwIfV2BrResFlrIndTx": jnxMbgPgwIfV2BrResFlrIndTx,
       "jnxMbgPgwIfV2ICsReqAcceptRx": jnxMbgPgwIfV2ICsReqAcceptRx,
       "jnxMbgPgwIfV2ICsReqAcceptTx": jnxMbgPgwIfV2ICsReqAcceptTx,
       "jnxMbgPgwIfV2ICsAcceptPartRx": jnxMbgPgwIfV2ICsAcceptPartRx,
       "jnxMbgPgwIfV2ICsAcceptPartTx": jnxMbgPgwIfV2ICsAcceptPartTx,
       "jnxMbgPgwIfV2ICsNewPTNPrefRx": jnxMbgPgwIfV2ICsNewPTNPrefRx,
       "jnxMbgPgwIfV2ICsNewPTNPrefTx": jnxMbgPgwIfV2ICsNewPTNPrefTx,
       "jnxMbgPgwIfV2ICsNewPTSIAdbrRx": jnxMbgPgwIfV2ICsNewPTSIAdbrRx,
       "jnxMbgPgwIfV2ICsNewPTSIAdbrTx": jnxMbgPgwIfV2ICsNewPTSIAdbrTx,
       "jnxMbgPgwIfV2ICsCtxNotFndRx": jnxMbgPgwIfV2ICsCtxNotFndRx,
       "jnxMbgPgwIfV2ICsCtxNotFndTx": jnxMbgPgwIfV2ICsCtxNotFndTx,
       "jnxMbgPgwIfV2ICsInvMsgFmtRx": jnxMbgPgwIfV2ICsInvMsgFmtRx,
       "jnxMbgPgwIfV2ICsInvMsgFmtTx": jnxMbgPgwIfV2ICsInvMsgFmtTx,
       "jnxMbgPgwIfV2ICsVerNotSuppRx": jnxMbgPgwIfV2ICsVerNotSuppRx,
       "jnxMbgPgwIfV2ICsVerNotSuppTx": jnxMbgPgwIfV2ICsVerNotSuppTx,
       "jnxMbgPgwIfV2ICsInvLenRx": jnxMbgPgwIfV2ICsInvLenRx,
       "jnxMbgPgwIfV2ICsInvLenTx": jnxMbgPgwIfV2ICsInvLenTx,
       "jnxMbgPgwIfV2ICsServNotSuppRx": jnxMbgPgwIfV2ICsServNotSuppRx,
       "jnxMbgPgwIfV2ICsServNotSuppTx": jnxMbgPgwIfV2ICsServNotSuppTx,
       "jnxMbgPgwIfV2ICsManIEIncorrRx": jnxMbgPgwIfV2ICsManIEIncorrRx,
       "jnxMbgPgwIfV2ICsManIEIncorrTx": jnxMbgPgwIfV2ICsManIEIncorrTx,
       "jnxMbgPgwIfV2ICsManIEMissRx": jnxMbgPgwIfV2ICsManIEMissRx,
       "jnxMbgPgwIfV2ICsManIEMissTx": jnxMbgPgwIfV2ICsManIEMissTx,
       "jnxMbgPgwIfV2ICsOptIEIncorrRx": jnxMbgPgwIfV2ICsOptIEIncorrRx,
       "jnxMbgPgwIfV2ICsOptIEIncorrTx": jnxMbgPgwIfV2ICsOptIEIncorrTx,
       "jnxMbgPgwIfV2ICsSysFailRx": jnxMbgPgwIfV2ICsSysFailRx,
       "jnxMbgPgwIfV2ICsSysFailTx": jnxMbgPgwIfV2ICsSysFailTx,
       "jnxMbgPgwIfV2ICsNoResRx": jnxMbgPgwIfV2ICsNoResRx,
       "jnxMbgPgwIfV2ICsNoResTx": jnxMbgPgwIfV2ICsNoResTx,
       "jnxMbgPgwIfV2ICsTFTSMANTErRx": jnxMbgPgwIfV2ICsTFTSMANTErRx,
       "jnxMbgPgwIfV2ICsTFTSMANTErTx": jnxMbgPgwIfV2ICsTFTSMANTErTx,
       "jnxMbgPgwIfV2ICsTFTSysErrRx": jnxMbgPgwIfV2ICsTFTSysErrRx,
       "jnxMbgPgwIfV2ICsTFTSysErrTx": jnxMbgPgwIfV2ICsTFTSysErrTx,
       "jnxMbgPgwIfV2ICsPkFltManErrRx": jnxMbgPgwIfV2ICsPkFltManErrRx,
       "jnxMbgPgwIfV2ICsPkFltManErrTx": jnxMbgPgwIfV2ICsPkFltManErrTx,
       "jnxMbgPgwIfV2ICsPkFltSynErrRx": jnxMbgPgwIfV2ICsPkFltSynErrRx,
       "jnxMbgPgwIfV2ICsPkFltSynErrTx": jnxMbgPgwIfV2ICsPkFltSynErrTx,
       "jnxMbgPgwIfV2ICsMisUnknAPNRx": jnxMbgPgwIfV2ICsMisUnknAPNRx,
       "jnxMbgPgwIfV2ICsMisUnknAPNTx": jnxMbgPgwIfV2ICsMisUnknAPNTx,
       "jnxMbgPgwIfV2ICsUnexpRptIERx": jnxMbgPgwIfV2ICsUnexpRptIERx,
       "jnxMbgPgwIfV2ICsUnexpRptIETx": jnxMbgPgwIfV2ICsUnexpRptIETx,
       "jnxMbgPgwIfV2ICsGREKeyNtFdRx": jnxMbgPgwIfV2ICsGREKeyNtFdRx,
       "jnxMbgPgwIfV2ICsGREKeyNtFdTx": jnxMbgPgwIfV2ICsGREKeyNtFdTx,
       "jnxMbgPgwIfV2ICsRelocFailRx": jnxMbgPgwIfV2ICsRelocFailRx,
       "jnxMbgPgwIfV2ICsRelocFailTx": jnxMbgPgwIfV2ICsRelocFailTx,
       "jnxMbgPgwIfV2ICsDeniedINRatRx": jnxMbgPgwIfV2ICsDeniedINRatRx,
       "jnxMbgPgwIfV2ICsDeniedINRatTx": jnxMbgPgwIfV2ICsDeniedINRatTx,
       "jnxMbgPgwIfV2ICsPTNotSuppRx": jnxMbgPgwIfV2ICsPTNotSuppRx,
       "jnxMbgPgwIfV2ICsPTNotSuppTx": jnxMbgPgwIfV2ICsPTNotSuppTx,
       "jnxMbgPgwIfV2ICsAllDynAdOccRx": jnxMbgPgwIfV2ICsAllDynAdOccRx,
       "jnxMbgPgwIfV2ICsAllDynAdOccTx": jnxMbgPgwIfV2ICsAllDynAdOccTx,
       "jnxMbgPgwIfV2ICsNOTFTUECTXRx": jnxMbgPgwIfV2ICsNOTFTUECTXRx,
       "jnxMbgPgwIfV2ICsNOTFTUECTXTx": jnxMbgPgwIfV2ICsNOTFTUECTXTx,
       "jnxMbgPgwIfV2ICsProtoNtSupRx": jnxMbgPgwIfV2ICsProtoNtSupRx,
       "jnxMbgPgwIfV2ICsProtoNtSupTx": jnxMbgPgwIfV2ICsProtoNtSupTx,
       "jnxMbgPgwIfV2ICsUENotRespRx": jnxMbgPgwIfV2ICsUENotRespRx,
       "jnxMbgPgwIfV2ICsUENotRespTx": jnxMbgPgwIfV2ICsUENotRespTx,
       "jnxMbgPgwIfV2ICsUERefusesRx": jnxMbgPgwIfV2ICsUERefusesRx,
       "jnxMbgPgwIfV2ICsUERefusesTx": jnxMbgPgwIfV2ICsUERefusesTx,
       "jnxMbgPgwIfV2ICsServDeniedRx": jnxMbgPgwIfV2ICsServDeniedRx,
       "jnxMbgPgwIfV2ICsServDeniedTx": jnxMbgPgwIfV2ICsServDeniedTx,
       "jnxMbgPgwIfV2ICsUnabPageUERx": jnxMbgPgwIfV2ICsUnabPageUERx,
       "jnxMbgPgwIfV2ICsUnabPageUETx": jnxMbgPgwIfV2ICsUnabPageUETx,
       "jnxMbgPgwIfV2ICsNoMemRx": jnxMbgPgwIfV2ICsNoMemRx,
       "jnxMbgPgwIfV2ICsNoMemTx": jnxMbgPgwIfV2ICsNoMemTx,
       "jnxMbgPgwIfV2ICsUserAUTHFlRx": jnxMbgPgwIfV2ICsUserAUTHFlRx,
       "jnxMbgPgwIfV2ICsUserAUTHFlTx": jnxMbgPgwIfV2ICsUserAUTHFlTx,
       "jnxMbgPgwIfV2ICsAPNAcsDenRx": jnxMbgPgwIfV2ICsAPNAcsDenRx,
       "jnxMbgPgwIfV2ICsAPNAcsDenTx": jnxMbgPgwIfV2ICsAPNAcsDenTx,
       "jnxMbgPgwIfV2ICsReqRejRx": jnxMbgPgwIfV2ICsReqRejRx,
       "jnxMbgPgwIfV2ICsReqRejTx": jnxMbgPgwIfV2ICsReqRejTx,
       "jnxMbgPgwIfV2ICsPTMSISigMMRx": jnxMbgPgwIfV2ICsPTMSISigMMRx,
       "jnxMbgPgwIfV2ICsPTMSISigMMTx": jnxMbgPgwIfV2ICsPTMSISigMMTx,
       "jnxMbgPgwIfV2ICsIMSINotKnRx": jnxMbgPgwIfV2ICsIMSINotKnRx,
       "jnxMbgPgwIfV2ICsIMSINotKnTx": jnxMbgPgwIfV2ICsIMSINotKnTx,
       "jnxMbgPgwIfV2ICsCondIEMsRx": jnxMbgPgwIfV2ICsCondIEMsRx,
       "jnxMbgPgwIfV2ICsCondIEMsTx": jnxMbgPgwIfV2ICsCondIEMsTx,
       "jnxMbgPgwIfV2ICsAPNResTIncRx": jnxMbgPgwIfV2ICsAPNResTIncRx,
       "jnxMbgPgwIfV2ICsAPNResTIncTx": jnxMbgPgwIfV2ICsAPNResTIncTx,
       "jnxMbgPgwIfV2ICsUnknownRx": jnxMbgPgwIfV2ICsUnknownRx,
       "jnxMbgPgwIfV2ICsUnknownTx": jnxMbgPgwIfV2ICsUnknownTx,
       "jnxMbgPgwIfV1ProtocolErrRx": jnxMbgPgwIfV1ProtocolErrRx,
       "jnxMbgPgwIfV1UnSupportedMsgRx": jnxMbgPgwIfV1UnSupportedMsgRx,
       "jnxMbgPgwIfV1T3RespTmrExpRx": jnxMbgPgwIfV1T3RespTmrExpRx,
       "jnxMbgPgwIfV1GlbNumMsgRx": jnxMbgPgwIfV1GlbNumMsgRx,
       "jnxMbgPgwIfV1GlbNumMsgTx": jnxMbgPgwIfV1GlbNumMsgTx,
       "jnxMbgPgwIfV1GlbNumBytesRx": jnxMbgPgwIfV1GlbNumBytesRx,
       "jnxMbgPgwIfV1GlbNumBytesTx": jnxMbgPgwIfV1GlbNumBytesTx,
       "jnxMbgPgwIfV1GlbEchoReqRx": jnxMbgPgwIfV1GlbEchoReqRx,
       "jnxMbgPgwIfV1GlbEchoReqTx": jnxMbgPgwIfV1GlbEchoReqTx,
       "jnxMbgPgwIfV1GlbEchoRespRx": jnxMbgPgwIfV1GlbEchoRespRx,
       "jnxMbgPgwIfV1GlbEchoRespTx": jnxMbgPgwIfV1GlbEchoRespTx,
       "jnxMbgPgwIfV1VerNotSupRx": jnxMbgPgwIfV1VerNotSupRx,
       "jnxMbgPgwIfV1VerNotSupTx": jnxMbgPgwIfV1VerNotSupTx,
       "jnxMbgPgwIfV1CrtPdpCxtReqRx": jnxMbgPgwIfV1CrtPdpCxtReqRx,
       "jnxMbgPgwIfV1CrtPdpCxtReqTx": jnxMbgPgwIfV1CrtPdpCxtReqTx,
       "jnxMbgPgwIfV1CrtPdpCxtRspRx": jnxMbgPgwIfV1CrtPdpCxtRspRx,
       "jnxMbgPgwIfV1CrtPdpCxtRspTx": jnxMbgPgwIfV1CrtPdpCxtRspTx,
       "jnxMbgPgwIfV1UpdPdpCxtReqRx": jnxMbgPgwIfV1UpdPdpCxtReqRx,
       "jnxMbgPgwIfV1UpdPdpCxtReqTx": jnxMbgPgwIfV1UpdPdpCxtReqTx,
       "jnxMbgPgwIfV1UpdPdpCxtRspRx": jnxMbgPgwIfV1UpdPdpCxtRspRx,
       "jnxMbgPgwIfV1UpdPdpCxtRspTx": jnxMbgPgwIfV1UpdPdpCxtRspTx,
       "jnxMbgPgwIfV1DelPdpCxtReqRx": jnxMbgPgwIfV1DelPdpCxtReqRx,
       "jnxMbgPgwIfV1DelPdpCxtReqTx": jnxMbgPgwIfV1DelPdpCxtReqTx,
       "jnxMbgPgwIfV1DelPdpCxtRspRx": jnxMbgPgwIfV1DelPdpCxtRspRx,
       "jnxMbgPgwIfV1DelPdpCxtRspTx": jnxMbgPgwIfV1DelPdpCxtRspTx,
       "jnxMbgPgwIfV1CrtAAPdpCxtReqRx": jnxMbgPgwIfV1CrtAAPdpCxtReqRx,
       "jnxMbgPgwIfV1CrtAAPdpCxtReqTx": jnxMbgPgwIfV1CrtAAPdpCxtReqTx,
       "jnxMbgPgwIfV1CrtAAPdpCxtRspRx": jnxMbgPgwIfV1CrtAAPdpCxtRspRx,
       "jnxMbgPgwIfV1CrtAAPdpCxtRspTx": jnxMbgPgwIfV1CrtAAPdpCxtRspTx,
       "jnxMbgPgwIfV1DelAAPdpCxtReqRx": jnxMbgPgwIfV1DelAAPdpCxtReqRx,
       "jnxMbgPgwIfV1DelAAPdpCxtReqTx": jnxMbgPgwIfV1DelAAPdpCxtReqTx,
       "jnxMbgPgwIfV1DelAAPdpCxtRspRx": jnxMbgPgwIfV1DelAAPdpCxtRspRx,
       "jnxMbgPgwIfV1DelAAPdpCxtRspTx": jnxMbgPgwIfV1DelAAPdpCxtRspTx,
       "jnxMbgPgwIfV1ErrorIndRx": jnxMbgPgwIfV1ErrorIndRx,
       "jnxMbgPgwIfV1ErrorIndTx": jnxMbgPgwIfV1ErrorIndTx,
       "jnxMbgPgwIfV1NotifReqRx": jnxMbgPgwIfV1NotifReqRx,
       "jnxMbgPgwIfV1NotifReqTx": jnxMbgPgwIfV1NotifReqTx,
       "jnxMbgPgwIfV1NotifRspRx": jnxMbgPgwIfV1NotifRspRx,
       "jnxMbgPgwIfV1NotifRspTx": jnxMbgPgwIfV1NotifRspTx,
       "jnxMbgPgwIfV1NotifRejReqRx": jnxMbgPgwIfV1NotifRejReqRx,
       "jnxMbgPgwIfV1NotifRejReqTx": jnxMbgPgwIfV1NotifRejReqTx,
       "jnxMbgPgwIfV1NotifRejRspRx": jnxMbgPgwIfV1NotifRejRspRx,
       "jnxMbgPgwIfV1NotifRejRspTx": jnxMbgPgwIfV1NotifRejRspTx,
       "jnxMbgPgwIfV1RtInfReqRx": jnxMbgPgwIfV1RtInfReqRx,
       "jnxMbgPgwIfV1RtInfReqTx": jnxMbgPgwIfV1RtInfReqTx,
       "jnxMbgPgwIfV1RtInfRspRx": jnxMbgPgwIfV1RtInfRspRx,
       "jnxMbgPgwIfV1RtInfRspTx": jnxMbgPgwIfV1RtInfRspTx,
       "jnxMbgPgwIfV1FailRptReqRx": jnxMbgPgwIfV1FailRptReqRx,
       "jnxMbgPgwIfV1FailRptReqTx": jnxMbgPgwIfV1FailRptReqTx,
       "jnxMbgPgwIfV1FailRptRspRx": jnxMbgPgwIfV1FailRptRspRx,
       "jnxMbgPgwIfV1FailRptRspTx": jnxMbgPgwIfV1FailRptRspTx,
       "jnxMbgPgwIfV1NotMSPresReqRx": jnxMbgPgwIfV1NotMSPresReqRx,
       "jnxMbgPgwIfV1NotMSPresReqTx": jnxMbgPgwIfV1NotMSPresReqTx,
       "jnxMbgPgwIfV1NotMSPresRspRx": jnxMbgPgwIfV1NotMSPresRspRx,
       "jnxMbgPgwIfV1NotMSPresRspTx": jnxMbgPgwIfV1NotMSPresRspTx,
       "jnxMbgPgwIfV1ICsReqAcceptedRx": jnxMbgPgwIfV1ICsReqAcceptedRx,
       "jnxMbgPgwIfV1ICsReqAcceptedTx": jnxMbgPgwIfV1ICsReqAcceptedTx,
       "jnxMbgPgwIfV1ICsNonExistRx": jnxMbgPgwIfV1ICsNonExistRx,
       "jnxMbgPgwIfV1ICsNonExistTx": jnxMbgPgwIfV1ICsNonExistTx,
       "jnxMbgPgwIfV1ICsInvMsgFmtRx": jnxMbgPgwIfV1ICsInvMsgFmtRx,
       "jnxMbgPgwIfV1ICsInvMsgFmtTx": jnxMbgPgwIfV1ICsInvMsgFmtTx,
       "jnxMbgPgwIfV1ICsIMSINotKnownRx": jnxMbgPgwIfV1ICsIMSINotKnownRx,
       "jnxMbgPgwIfV1ICsIMSINotKnownTx": jnxMbgPgwIfV1ICsIMSINotKnownTx,
       "jnxMbgPgwIfV1ICsMSGRPSDetachRx": jnxMbgPgwIfV1ICsMSGRPSDetachRx,
       "jnxMbgPgwIfV1ICsMSGRPSDetachTx": jnxMbgPgwIfV1ICsMSGRPSDetachTx,
       "jnxMbgPgwIfV1ICsMSNotGRPSRespRx": jnxMbgPgwIfV1ICsMSNotGRPSRespRx,
       "jnxMbgPgwIfV1ICsMSNotGRPSRespTx": jnxMbgPgwIfV1ICsMSNotGRPSRespTx,
       "jnxMbgPgwIfV1ICsMSRefusesRx": jnxMbgPgwIfV1ICsMSRefusesRx,
       "jnxMbgPgwIfV1ICsMSRefusesTx": jnxMbgPgwIfV1ICsMSRefusesTx,
       "jnxMbgPgwIfV1ICsVerNotSuppRx": jnxMbgPgwIfV1ICsVerNotSuppRx,
       "jnxMbgPgwIfV1ICsVerNotSuppTx": jnxMbgPgwIfV1ICsVerNotSuppTx,
       "jnxMbgPgwIfV1ICsNoResRx": jnxMbgPgwIfV1ICsNoResRx,
       "jnxMbgPgwIfV1ICsNoResTx": jnxMbgPgwIfV1ICsNoResTx,
       "jnxMbgPgwIfV1ICsServNotSuppRx": jnxMbgPgwIfV1ICsServNotSuppRx,
       "jnxMbgPgwIfV1ICsServNotSuppTx": jnxMbgPgwIfV1ICsServNotSuppTx,
       "jnxMbgPgwIfV1ICsManIEIncrtRx": jnxMbgPgwIfV1ICsManIEIncrtRx,
       "jnxMbgPgwIfV1ICsManIEIncrtTx": jnxMbgPgwIfV1ICsManIEIncrtTx,
       "jnxMbgPgwIfV1ICsManIEMissRx": jnxMbgPgwIfV1ICsManIEMissRx,
       "jnxMbgPgwIfV1ICsManIEMissTx": jnxMbgPgwIfV1ICsManIEMissTx,
       "jnxMbgPgwIfV1ICsOptIEIncrtRx": jnxMbgPgwIfV1ICsOptIEIncrtRx,
       "jnxMbgPgwIfV1ICsOptIEIncrtTx": jnxMbgPgwIfV1ICsOptIEIncrtTx,
       "jnxMbgPgwIfV1ICsSysFailRx": jnxMbgPgwIfV1ICsSysFailRx,
       "jnxMbgPgwIfV1ICsSysFailTx": jnxMbgPgwIfV1ICsSysFailTx,
       "jnxMbgPgwIfV1ICsRoamRestrictRx": jnxMbgPgwIfV1ICsRoamRestrictRx,
       "jnxMbgPgwIfV1ICsRoamRestrictTx": jnxMbgPgwIfV1ICsRoamRestrictTx,
       "jnxMbgPgwIfV1ICsPTMSISigMMRx": jnxMbgPgwIfV1ICsPTMSISigMMRx,
       "jnxMbgPgwIfV1ICsPTMSISigMMTx": jnxMbgPgwIfV1ICsPTMSISigMMTx,
       "jnxMbgPgwIfV1ICsGPRSConnSuppRx": jnxMbgPgwIfV1ICsGPRSConnSuppRx,
       "jnxMbgPgwIfV1ICsGPRSConnSuppTx": jnxMbgPgwIfV1ICsGPRSConnSuppTx,
       "jnxMbgPgwIfV1ICsAuthFailRx": jnxMbgPgwIfV1ICsAuthFailRx,
       "jnxMbgPgwIfV1ICsAuthFailTx": jnxMbgPgwIfV1ICsAuthFailTx,
       "jnxMbgPgwIfV1ICsUserAuthFailRx": jnxMbgPgwIfV1ICsUserAuthFailRx,
       "jnxMbgPgwIfV1ICsUserAuthFailTx": jnxMbgPgwIfV1ICsUserAuthFailTx,
       "jnxMbgPgwIfV1ICsCtxNotFndRx": jnxMbgPgwIfV1ICsCtxNotFndRx,
       "jnxMbgPgwIfV1ICsCtxNotFndTx": jnxMbgPgwIfV1ICsCtxNotFndTx,
       "jnxMbgPgwIfV1ICsAllDynPDPAdRx": jnxMbgPgwIfV1ICsAllDynPDPAdRx,
       "jnxMbgPgwIfV1ICsAllDynPDPAdTx": jnxMbgPgwIfV1ICsAllDynPDPAdTx,
       "jnxMbgPgwIfV1ICsNoMemRx": jnxMbgPgwIfV1ICsNoMemRx,
       "jnxMbgPgwIfV1ICsNoMemTx": jnxMbgPgwIfV1ICsNoMemTx,
       "jnxMbgPgwIfV1ICsRelocFailRx": jnxMbgPgwIfV1ICsRelocFailRx,
       "jnxMbgPgwIfV1ICsRelocFailTx": jnxMbgPgwIfV1ICsRelocFailTx,
       "jnxMbgPgwIfV1ICsUnkManExhdrRx": jnxMbgPgwIfV1ICsUnkManExhdrRx,
       "jnxMbgPgwIfV1ICsUnkManExhdrTx": jnxMbgPgwIfV1ICsUnkManExhdrTx,
       "jnxMbgPgwIfV1ICsSMANTTFTEr1Rx": jnxMbgPgwIfV1ICsSMANTTFTEr1Rx,
       "jnxMbgPgwIfV1ICsSMANTTFTEr1Tx": jnxMbgPgwIfV1ICsSMANTTFTEr1Tx,
       "jnxMbgPgwIfV1ICsSYNTFTErr2Rx": jnxMbgPgwIfV1ICsSYNTFTErr2Rx,
       "jnxMbgPgwIfV1ICsSYNTFTErr2Tx": jnxMbgPgwIfV1ICsSYNTFTErr2Tx,
       "jnxMbgPgwIfV1ICsSMNTPkFlEr1Rx": jnxMbgPgwIfV1ICsSMNTPkFlEr1Rx,
       "jnxMbgPgwIfV1ICsSMNTPkFlEr1Tx": jnxMbgPgwIfV1ICsSMNTPkFlEr1Tx,
       "jnxMbgPgwIfV1ICsSYNPkFlErr2Rx": jnxMbgPgwIfV1ICsSYNPkFlErr2Rx,
       "jnxMbgPgwIfV1ICsSYNPkFlErr2Tx": jnxMbgPgwIfV1ICsSYNPkFlErr2Tx,
       "jnxMbgPgwIfV1ICsMissUnknAPNRx": jnxMbgPgwIfV1ICsMissUnknAPNRx,
       "jnxMbgPgwIfV1ICsMissUnknAPNTx": jnxMbgPgwIfV1ICsMissUnknAPNTx,
       "jnxMbgPgwIfV1ICsUnknPDPAdRx": jnxMbgPgwIfV1ICsUnknPDPAdRx,
       "jnxMbgPgwIfV1ICsUnknPDPAdTx": jnxMbgPgwIfV1ICsUnknPDPAdTx,
       "jnxMbgPgwIfV1ICsNoTFTCtxExRx": jnxMbgPgwIfV1ICsNoTFTCtxExRx,
       "jnxMbgPgwIfV1ICsNoTFTCtxExTx": jnxMbgPgwIfV1ICsNoTFTCtxExTx,
       "jnxMbgPgwIfV0ProtocolErrRx": jnxMbgPgwIfV0ProtocolErrRx,
       "jnxMbgPgwIfV0UnSupportedMsgRx": jnxMbgPgwIfV0UnSupportedMsgRx,
       "jnxMbgPgwIfV0T3RespTmrExpRx": jnxMbgPgwIfV0T3RespTmrExpRx,
       "jnxMbgPgwIfV0GlbNumMsgRx": jnxMbgPgwIfV0GlbNumMsgRx,
       "jnxMbgPgwIfV0GlbNumMsgTx": jnxMbgPgwIfV0GlbNumMsgTx,
       "jnxMbgPgwIfV0GlbNumBytesRx": jnxMbgPgwIfV0GlbNumBytesRx,
       "jnxMbgPgwIfV0GlbNumBytesTx": jnxMbgPgwIfV0GlbNumBytesTx,
       "jnxMbgPgwIfV0GlbEchoReqRx": jnxMbgPgwIfV0GlbEchoReqRx,
       "jnxMbgPgwIfV0GlbEchoReqTx": jnxMbgPgwIfV0GlbEchoReqTx,
       "jnxMbgPgwIfV0GlbEchoRespRx": jnxMbgPgwIfV0GlbEchoRespRx,
       "jnxMbgPgwIfV0GlbEchoRespTx": jnxMbgPgwIfV0GlbEchoRespTx,
       "jnxMbgPgwIfV0GlbVerNotSupRx": jnxMbgPgwIfV0GlbVerNotSupRx,
       "jnxMbgPgwIfV0GlbVerNotSupTx": jnxMbgPgwIfV0GlbVerNotSupTx,
       "jnxMbgPgwIfV0GlbCrtPdpCxtReqRx": jnxMbgPgwIfV0GlbCrtPdpCxtReqRx,
       "jnxMbgPgwIfV0GlbCrtPdpCxtReqTx": jnxMbgPgwIfV0GlbCrtPdpCxtReqTx,
       "jnxMbgPgwIfV0GlbCrtPdpCxtRspRx": jnxMbgPgwIfV0GlbCrtPdpCxtRspRx,
       "jnxMbgPgwIfV0GlbCrtPdpCxtRspTx": jnxMbgPgwIfV0GlbCrtPdpCxtRspTx,
       "jnxMbgPgwIfV0GlbUpdPdpCxtReqRx": jnxMbgPgwIfV0GlbUpdPdpCxtReqRx,
       "jnxMbgPgwIfV0GlbUpdPdpCxtReqTx": jnxMbgPgwIfV0GlbUpdPdpCxtReqTx,
       "jnxMbgPgwIfV0GlbUpdPdpCxtRspRx": jnxMbgPgwIfV0GlbUpdPdpCxtRspRx,
       "jnxMbgPgwIfV0GlbUpdPdpCxtRspTx": jnxMbgPgwIfV0GlbUpdPdpCxtRspTx,
       "jnxMbgPgwIfV0GlbDelPdpCxtReqRx": jnxMbgPgwIfV0GlbDelPdpCxtReqRx,
       "jnxMbgPgwIfV0GlbDelPdpCxtReqTx": jnxMbgPgwIfV0GlbDelPdpCxtReqTx,
       "jnxMbgPgwIfV0GlbDelPdpCxtRspRx": jnxMbgPgwIfV0GlbDelPdpCxtRspRx,
       "jnxMbgPgwIfV0GlbDelPdpCxtRspTx": jnxMbgPgwIfV0GlbDelPdpCxtRspTx,
       "jnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx": jnxMbgPgwIfV0GlbCrtAAPdpCxtRqRx,
       "jnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx": jnxMbgPgwIfV0GlbCrtAAPdpCxtRqTx,
       "jnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx": jnxMbgPgwIfV0GlbCrtAAPdpCxtRpRx,
       "jnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx": jnxMbgPgwIfV0GlbCrtAAPdpCxtRpTx,
       "jnxMbgPgwIfV0GlbDelAAPdpCxtRqRx": jnxMbgPgwIfV0GlbDelAAPdpCxtRqRx,
       "jnxMbgPgwIfV0GlbDelAAPdpCxtRqTx": jnxMbgPgwIfV0GlbDelAAPdpCxtRqTx,
       "jnxMbgPgwIfV0GlbDelAAPdpCxtRpRx": jnxMbgPgwIfV0GlbDelAAPdpCxtRpRx,
       "jnxMbgPgwIfV0GlbDelAAPdpCxtRpTx": jnxMbgPgwIfV0GlbDelAAPdpCxtRpTx,
       "jnxMbgPgwIfV0GlbErrorIndRx": jnxMbgPgwIfV0GlbErrorIndRx,
       "jnxMbgPgwIfV0GlbErrorIndTx": jnxMbgPgwIfV0GlbErrorIndTx,
       "jnxMbgPgwIfV0GlbNotifReqRx": jnxMbgPgwIfV0GlbNotifReqRx,
       "jnxMbgPgwIfV0GlbNotifReqTx": jnxMbgPgwIfV0GlbNotifReqTx,
       "jnxMbgPgwIfV0GlbNotifRspRx": jnxMbgPgwIfV0GlbNotifRspRx,
       "jnxMbgPgwIfV0GlbNotifRspTx": jnxMbgPgwIfV0GlbNotifRspTx,
       "jnxMbgPgwIfV0GlbNotifRejReqRx": jnxMbgPgwIfV0GlbNotifRejReqRx,
       "jnxMbgPgwIfV0GlbNotifRejReqTx": jnxMbgPgwIfV0GlbNotifRejReqTx,
       "jnxMbgPgwIfV0GlbNotifRejRspRx": jnxMbgPgwIfV0GlbNotifRejRspRx,
       "jnxMbgPgwIfV0GlbNotifRejRspTx": jnxMbgPgwIfV0GlbNotifRejRspTx,
       "jnxMbgPgwIfV0GlbRtInfReqRx": jnxMbgPgwIfV0GlbRtInfReqRx,
       "jnxMbgPgwIfV0GlbRtInfReqTx": jnxMbgPgwIfV0GlbRtInfReqTx,
       "jnxMbgPgwIfV0GlbRtInfRspRx": jnxMbgPgwIfV0GlbRtInfRspRx,
       "jnxMbgPgwIfV0GlbRtInfRspTx": jnxMbgPgwIfV0GlbRtInfRspTx,
       "jnxMbgPgwIfV0GlbFailRptReqRx": jnxMbgPgwIfV0GlbFailRptReqRx,
       "jnxMbgPgwIfV0GlbFailRptReqTx": jnxMbgPgwIfV0GlbFailRptReqTx,
       "jnxMbgPgwIfV0GlbFailRptRspRx": jnxMbgPgwIfV0GlbFailRptRspRx,
       "jnxMbgPgwIfV0GlbFailRptRspTx": jnxMbgPgwIfV0GlbFailRptRspTx,
       "jnxMbgPgwIfV0GlbNotMSPresReqRx": jnxMbgPgwIfV0GlbNotMSPresReqRx,
       "jnxMbgPgwIfV0GlbNotMSPresReqTx": jnxMbgPgwIfV0GlbNotMSPresReqTx,
       "jnxMbgPgwIfV0GlbNotMSPresRspRx": jnxMbgPgwIfV0GlbNotMSPresRspRx,
       "jnxMbgPgwIfV0GlbNotMSPresRspTx": jnxMbgPgwIfV0GlbNotMSPresRspTx,
       "jnxMbgPgwIfV0ICsReqAcceptedRx": jnxMbgPgwIfV0ICsReqAcceptedRx,
       "jnxMbgPgwIfV0ICsReqAcceptedTx": jnxMbgPgwIfV0ICsReqAcceptedTx,
       "jnxMbgPgwIfV0ICsNonExistRx": jnxMbgPgwIfV0ICsNonExistRx,
       "jnxMbgPgwIfV0ICsNonExistTx": jnxMbgPgwIfV0ICsNonExistTx,
       "jnxMbgPgwIfV0ICsInvMsgFmtRx": jnxMbgPgwIfV0ICsInvMsgFmtRx,
       "jnxMbgPgwIfV0ICsInvMsgFmtTx": jnxMbgPgwIfV0ICsInvMsgFmtTx,
       "jnxMbgPgwIfV0ICsIMSINotKnownRx": jnxMbgPgwIfV0ICsIMSINotKnownRx,
       "jnxMbgPgwIfV0ICsIMSINotKnownTx": jnxMbgPgwIfV0ICsIMSINotKnownTx,
       "jnxMbgPgwIfV0ICsMSGRPSDetachRx": jnxMbgPgwIfV0ICsMSGRPSDetachRx,
       "jnxMbgPgwIfV0ICsMSGRPSDetachTx": jnxMbgPgwIfV0ICsMSGRPSDetachTx,
       "jnxMbgPgwIfV0ICsMSNotGRPSRespRx": jnxMbgPgwIfV0ICsMSNotGRPSRespRx,
       "jnxMbgPgwIfV0ICsMSNotGRPSRespTx": jnxMbgPgwIfV0ICsMSNotGRPSRespTx,
       "jnxMbgPgwIfV0ICsMSRefusesRx": jnxMbgPgwIfV0ICsMSRefusesRx,
       "jnxMbgPgwIfV0ICsMSRefusesTx": jnxMbgPgwIfV0ICsMSRefusesTx,
       "jnxMbgPgwIfV0ICsVerNotSuppRx": jnxMbgPgwIfV0ICsVerNotSuppRx,
       "jnxMbgPgwIfV0ICsVerNotSuppTx": jnxMbgPgwIfV0ICsVerNotSuppTx,
       "jnxMbgPgwIfV0ICsNoResRx": jnxMbgPgwIfV0ICsNoResRx,
       "jnxMbgPgwIfV0ICsNoResTx": jnxMbgPgwIfV0ICsNoResTx,
       "jnxMbgPgwIfV0ICsServNotSuppRx": jnxMbgPgwIfV0ICsServNotSuppRx,
       "jnxMbgPgwIfV0ICsServNotSuppTx": jnxMbgPgwIfV0ICsServNotSuppTx,
       "jnxMbgPgwIfV0ICsManIEIncrtRx": jnxMbgPgwIfV0ICsManIEIncrtRx,
       "jnxMbgPgwIfV0ICsManIEIncrtTx": jnxMbgPgwIfV0ICsManIEIncrtTx,
       "jnxMbgPgwIfV0ICsManIEMissRx": jnxMbgPgwIfV0ICsManIEMissRx,
       "jnxMbgPgwIfV0ICsManIEMissTx": jnxMbgPgwIfV0ICsManIEMissTx,
       "jnxMbgPgwIfV0ICsOptIEIncrtRx": jnxMbgPgwIfV0ICsOptIEIncrtRx,
       "jnxMbgPgwIfV0ICsOptIEIncrtTx": jnxMbgPgwIfV0ICsOptIEIncrtTx,
       "jnxMbgPgwIfV0ICsSysFailRx": jnxMbgPgwIfV0ICsSysFailRx,
       "jnxMbgPgwIfV0ICsSysFailTx": jnxMbgPgwIfV0ICsSysFailTx,
       "jnxMbgPgwIfV0ICsRoamRestrictRx": jnxMbgPgwIfV0ICsRoamRestrictRx,
       "jnxMbgPgwIfV0ICsRoamRestrictTx": jnxMbgPgwIfV0ICsRoamRestrictTx,
       "jnxMbgPgwIfV0ICsPTMSISigMMRx": jnxMbgPgwIfV0ICsPTMSISigMMRx,
       "jnxMbgPgwIfV0ICsPTMSISigMMTx": jnxMbgPgwIfV0ICsPTMSISigMMTx,
       "jnxMbgPgwIfV0ICsGPRSConnSuppRx": jnxMbgPgwIfV0ICsGPRSConnSuppRx,
       "jnxMbgPgwIfV0ICsGPRSConnSuppTx": jnxMbgPgwIfV0ICsGPRSConnSuppTx,
       "jnxMbgPgwIfV0ICsAuthFailRx": jnxMbgPgwIfV0ICsAuthFailRx,
       "jnxMbgPgwIfV0ICsAuthFailTx": jnxMbgPgwIfV0ICsAuthFailTx,
       "jnxMbgPgwIfV0ICsUserAuthFailRx": jnxMbgPgwIfV0ICsUserAuthFailRx,
       "jnxMbgPgwIfV0ICsUserAuthFailTx": jnxMbgPgwIfV0ICsUserAuthFailTx,
       "jnxMbgPgwIfGtpV2ICsLclDetRx": jnxMbgPgwIfGtpV2ICsLclDetRx,
       "jnxMbgPgwIfGtpV2ICsLclDetTx": jnxMbgPgwIfGtpV2ICsLclDetTx,
       "jnxMbgPgwIfGtpV2ICsCmpDetRx": jnxMbgPgwIfGtpV2ICsCmpDetRx,
       "jnxMbgPgwIfGtpV2ICsCmpDetTx": jnxMbgPgwIfGtpV2ICsCmpDetTx,
       "jnxMbgPgwIfGtpV2ICsRATChgRx": jnxMbgPgwIfGtpV2ICsRATChgRx,
       "jnxMbgPgwIfGtpV2ICsRATChgTx": jnxMbgPgwIfGtpV2ICsRATChgTx,
       "jnxMbgPgwIfGtpV2ICsISRDeactRx": jnxMbgPgwIfGtpV2ICsISRDeactRx,
       "jnxMbgPgwIfGtpV2ICsISRDeactTx": jnxMbgPgwIfGtpV2ICsISRDeactTx,
       "jnxMbgPgwIfGtpV2ICsEIFRNCEnRx": jnxMbgPgwIfGtpV2ICsEIFRNCEnRx,
       "jnxMbgPgwIfGtpV2ICsEIFRNCEnTx": jnxMbgPgwIfGtpV2ICsEIFRNCEnTx,
       "jnxMbgPgwIfGtpV2ICsSemErTADRx": jnxMbgPgwIfGtpV2ICsSemErTADRx,
       "jnxMbgPgwIfGtpV2ICsSemErTADTx": jnxMbgPgwIfGtpV2ICsSemErTADTx,
       "jnxMbgPgwIfGtpV2ICsSynErTADRx": jnxMbgPgwIfGtpV2ICsSynErTADRx,
       "jnxMbgPgwIfGtpV2ICsSynErTADTx": jnxMbgPgwIfGtpV2ICsSynErTADTx,
       "jnxMbgPgwIfGtpV2ICsRMValRcvRx": jnxMbgPgwIfGtpV2ICsRMValRcvRx,
       "jnxMbgPgwIfGtpV2ICsRMValRcvTx": jnxMbgPgwIfGtpV2ICsRMValRcvTx,
       "jnxMbgPgwIfGtpV2ICsRPrNtRspRx": jnxMbgPgwIfGtpV2ICsRPrNtRspRx,
       "jnxMbgPgwIfGtpV2ICsRPrNtRspTx": jnxMbgPgwIfGtpV2ICsRPrNtRspTx,
       "jnxMbgPgwIfGtpV2ICsColNWReqRx": jnxMbgPgwIfGtpV2ICsColNWReqRx,
       "jnxMbgPgwIfGtpV2ICsColNWReqTx": jnxMbgPgwIfGtpV2ICsColNWReqTx,
       "jnxMbgPgwIfGtpV2ICsUnPgUESusRx": jnxMbgPgwIfGtpV2ICsUnPgUESusRx,
       "jnxMbgPgwIfGtpV2ICsUnPgUESusTx": jnxMbgPgwIfGtpV2ICsUnPgUESusTx,
       "jnxMbgPgwIfGtpV2ICsInvTotLenRx": jnxMbgPgwIfGtpV2ICsInvTotLenRx,
       "jnxMbgPgwIfGtpV2ICsInvTotLenTx": jnxMbgPgwIfGtpV2ICsInvTotLenTx,
       "jnxMbgPgwIfGtpV2ICsDtForNtSupRx": jnxMbgPgwIfGtpV2ICsDtForNtSupRx,
       "jnxMbgPgwIfGtpV2ICsDtForNtSupTx": jnxMbgPgwIfGtpV2ICsDtForNtSupTx,
       "jnxMbgPgwIfGtpV2ICsInReFRePrRx": jnxMbgPgwIfGtpV2ICsInReFRePrRx,
       "jnxMbgPgwIfGtpV2ICsInReFRePrTx": jnxMbgPgwIfGtpV2ICsInReFRePrTx,
       "jnxMbgPgwIfGtpV2ICsInvPrRx": jnxMbgPgwIfGtpV2ICsInvPrRx,
       "jnxMbgPgwIfGtpV2ICsInvPrTx": jnxMbgPgwIfGtpV2ICsInvPrTx,
       "jnxMbgPgwIfV1InitPdpCxtReqRx": jnxMbgPgwIfV1InitPdpCxtReqRx,
       "jnxMbgPgwIfV1InitPdpCxtReqTx": jnxMbgPgwIfV1InitPdpCxtReqTx,
       "jnxMbgPgwIfV1InitPdpCxtRspRx": jnxMbgPgwIfV1InitPdpCxtRspRx,
       "jnxMbgPgwIfV1InitPdpCxtRspTx": jnxMbgPgwIfV1InitPdpCxtRspTx,
       "jnxMbgPgwIfV2SuspNotifRx": jnxMbgPgwIfV2SuspNotifRx,
       "jnxMbgPgwIfV2SuspNotifTx": jnxMbgPgwIfV2SuspNotifTx,
       "jnxMbgPgwIfV2SuspAckRx": jnxMbgPgwIfV2SuspAckRx,
       "jnxMbgPgwIfV2SuspAckTx": jnxMbgPgwIfV2SuspAckTx,
       "jnxMbgPgwIfV2ResumeNotifRx": jnxMbgPgwIfV2ResumeNotifRx,
       "jnxMbgPgwIfV2ResumeNotifTx": jnxMbgPgwIfV2ResumeNotifTx,
       "jnxMbgPgwIfV2ResumeAckRx": jnxMbgPgwIfV2ResumeAckRx,
       "jnxMbgPgwIfV2ResumeAckTx": jnxMbgPgwIfV2ResumeAckTx,
       "jnxMbgPgwIfV2PiggybackMsgRx": jnxMbgPgwIfV2PiggybackMsgRx,
       "jnxMbgPgwIfV2PiggybackMsgTx": jnxMbgPgwIfV2PiggybackMsgTx}
)
