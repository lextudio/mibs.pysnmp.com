# SNMP MIB module (Unisphere-Data-RADIUS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-RADIUS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:29 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdRadiusClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19)
)
usdRadiusClientMIB.setRevisions(
        ("2002-05-13 17:54",
         "2001-10-16 19:54",
         "2001-09-06 21:08",
         "2001-03-22 15:20",
         "2000-12-19 16:40",
         "2000-05-05 19:44",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdRadiusClientObjects_ObjectIdentity = ObjectIdentity
usdRadiusClientObjects = _UsdRadiusClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1)
)
_UsdRadiusGeneralClient_ObjectIdentity = ObjectIdentity
usdRadiusGeneralClient = _UsdRadiusGeneralClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1)
)
_UsdRadiusClientIdentifier_Type = DisplayString
_UsdRadiusClientIdentifier_Object = MibScalar
usdRadiusClientIdentifier = _UsdRadiusClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 1),
    _UsdRadiusClientIdentifier_Type()
)
usdRadiusClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusClientIdentifier.setStatus("current")


class _UsdRadiusClientAlgorithm_Type(Integer32):
    """Custom type usdRadiusClientAlgorithm based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("roundRobin", 1))
    )


_UsdRadiusClientAlgorithm_Type.__name__ = "Integer32"
_UsdRadiusClientAlgorithm_Object = MibScalar
usdRadiusClientAlgorithm = _UsdRadiusClientAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 2),
    _UsdRadiusClientAlgorithm_Type()
)
usdRadiusClientAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientAlgorithm.setStatus("current")


class _UsdRadiusClientSourceAddress_Type(IpAddress):
    """Custom type usdRadiusClientSourceAddress based on IpAddress"""
    defaultValue = 0


_UsdRadiusClientSourceAddress_Object = MibScalar
usdRadiusClientSourceAddress = _UsdRadiusClientSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 3),
    _UsdRadiusClientSourceAddress_Type()
)
usdRadiusClientSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientSourceAddress.setStatus("current")


class _UsdRadiusClientUdpChecksum_Type(TruthValue):
    """Custom type usdRadiusClientUdpChecksum based on TruthValue"""


_UsdRadiusClientUdpChecksum_Object = MibScalar
usdRadiusClientUdpChecksum = _UsdRadiusClientUdpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 4),
    _UsdRadiusClientUdpChecksum_Type()
)
usdRadiusClientUdpChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientUdpChecksum.setStatus("current")


class _UsdRadiusClientNasIdentifier_Type(DisplayString):
    """Custom type usdRadiusClientNasIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_UsdRadiusClientNasIdentifier_Type.__name__ = "DisplayString"
_UsdRadiusClientNasIdentifier_Object = MibScalar
usdRadiusClientNasIdentifier = _UsdRadiusClientNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 5),
    _UsdRadiusClientNasIdentifier_Type()
)
usdRadiusClientNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientNasIdentifier.setStatus("current")


class _UsdRadiusClientDslPortType_Type(Integer32):
    """Custom type usdRadiusClientDslPortType based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              11,
              12,
              13,
              14,
              16)
        )
    )
    namedValues = NamedValues(
        *(("adsl-cap", 12),
          ("adsl-dmt", 13),
          ("idsl", 14),
          ("sdsl", 11),
          ("virtual", 5),
          ("xdsl", 16))
    )


_UsdRadiusClientDslPortType_Type.__name__ = "Integer32"
_UsdRadiusClientDslPortType_Object = MibScalar
usdRadiusClientDslPortType = _UsdRadiusClientDslPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 6),
    _UsdRadiusClientDslPortType_Type()
)
usdRadiusClientDslPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientDslPortType.setStatus("current")


class _UsdRadiusClientTunnelAccounting_Type(TruthValue):
    """Custom type usdRadiusClientTunnelAccounting based on TruthValue"""


_UsdRadiusClientTunnelAccounting_Object = MibScalar
usdRadiusClientTunnelAccounting = _UsdRadiusClientTunnelAccounting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 7),
    _UsdRadiusClientTunnelAccounting_Type()
)
usdRadiusClientTunnelAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientTunnelAccounting.setStatus("current")


class _UsdRadiusClientAcctSessionIdFormat_Type(Integer32):
    """Custom type usdRadiusClientAcctSessionIdFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("decimal", 0),
          ("description", 1))
    )


_UsdRadiusClientAcctSessionIdFormat_Type.__name__ = "Integer32"
_UsdRadiusClientAcctSessionIdFormat_Object = MibScalar
usdRadiusClientAcctSessionIdFormat = _UsdRadiusClientAcctSessionIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 8),
    _UsdRadiusClientAcctSessionIdFormat_Type()
)
usdRadiusClientAcctSessionIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientAcctSessionIdFormat.setStatus("current")


class _UsdRadiusClientNasPortFormat_Type(Integer32):
    """Custom type usdRadiusClientNasPortFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ssssxppp", 1),
          ("xssssppp", 0))
    )


_UsdRadiusClientNasPortFormat_Type.__name__ = "Integer32"
_UsdRadiusClientNasPortFormat_Object = MibScalar
usdRadiusClientNasPortFormat = _UsdRadiusClientNasPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 9),
    _UsdRadiusClientNasPortFormat_Type()
)
usdRadiusClientNasPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientNasPortFormat.setStatus("current")


class _UsdRadiusClientCallingStationDelimiter_Type(DisplayString):
    """Custom type usdRadiusClientCallingStationDelimiter based on DisplayString"""
    defaultValue = OctetString("#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_UsdRadiusClientCallingStationDelimiter_Type.__name__ = "DisplayString"
_UsdRadiusClientCallingStationDelimiter_Object = MibScalar
usdRadiusClientCallingStationDelimiter = _UsdRadiusClientCallingStationDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 10),
    _UsdRadiusClientCallingStationDelimiter_Type()
)
usdRadiusClientCallingStationDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientCallingStationDelimiter.setStatus("current")


class _UsdRadiusClientEthernetPortType_Type(Integer32):
    """Custom type usdRadiusClientEthernetPortType based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              15)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 15),
          ("virtual", 5))
    )


_UsdRadiusClientEthernetPortType_Type.__name__ = "Integer32"
_UsdRadiusClientEthernetPortType_Object = MibScalar
usdRadiusClientEthernetPortType = _UsdRadiusClientEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 11),
    _UsdRadiusClientEthernetPortType_Type()
)
usdRadiusClientEthernetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientEthernetPortType.setStatus("current")


class _UsdRadiusClientIncludeIpAddrInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeIpAddrInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeIpAddrInAcctStart_Object = MibScalar
usdRadiusClientIncludeIpAddrInAcctStart = _UsdRadiusClientIncludeIpAddrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 12),
    _UsdRadiusClientIncludeIpAddrInAcctStart_Type()
)
usdRadiusClientIncludeIpAddrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeIpAddrInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeAcctSessionIdInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeAcctSessionIdInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeAcctSessionIdInAccessReq_Object = MibScalar
usdRadiusClientIncludeAcctSessionIdInAccessReq = _UsdRadiusClientIncludeAcctSessionIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 13),
    _UsdRadiusClientIncludeAcctSessionIdInAccessReq_Type()
)
usdRadiusClientIncludeAcctSessionIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeAcctSessionIdInAccessReq.setStatus("current")


class _UsdRadiusClientRollover_Type(TruthValue):
    """Custom type usdRadiusClientRollover based on TruthValue"""


_UsdRadiusClientRollover_Object = MibScalar
usdRadiusClientRollover = _UsdRadiusClientRollover_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 14),
    _UsdRadiusClientRollover_Type()
)
usdRadiusClientRollover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientRollover.setStatus("current")


class _UsdRadiusClientCallingStationIdFormat_Type(Integer32):
    """Custom type usdRadiusClientCallingStationIdFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delimited", 0),
          ("fixedFormat", 1))
    )


_UsdRadiusClientCallingStationIdFormat_Type.__name__ = "Integer32"
_UsdRadiusClientCallingStationIdFormat_Object = MibScalar
usdRadiusClientCallingStationIdFormat = _UsdRadiusClientCallingStationIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 15),
    _UsdRadiusClientCallingStationIdFormat_Type()
)
usdRadiusClientCallingStationIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientCallingStationIdFormat.setStatus("current")


class _UsdRadiusClientNasIpAddrUse_Type(Integer32):
    """Custom type usdRadiusClientNasIpAddrUse based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("tunnelClientEndpoint", 1))
    )


_UsdRadiusClientNasIpAddrUse_Type.__name__ = "Integer32"
_UsdRadiusClientNasIpAddrUse_Object = MibScalar
usdRadiusClientNasIpAddrUse = _UsdRadiusClientNasIpAddrUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 16),
    _UsdRadiusClientNasIpAddrUse_Type()
)
usdRadiusClientNasIpAddrUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientNasIpAddrUse.setStatus("current")


class _UsdRadiusClientIncludeAcctTunnelConnectionInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeAcctTunnelConnectionInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeAcctTunnelConnectionInAccessReq_Object = MibScalar
usdRadiusClientIncludeAcctTunnelConnectionInAccessReq = _UsdRadiusClientIncludeAcctTunnelConnectionInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 17),
    _UsdRadiusClientIncludeAcctTunnelConnectionInAccessReq_Type()
)
usdRadiusClientIncludeAcctTunnelConnectionInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeAcctTunnelConnectionInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeCalledStationIdInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeCalledStationIdInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeCalledStationIdInAccessReq_Object = MibScalar
usdRadiusClientIncludeCalledStationIdInAccessReq = _UsdRadiusClientIncludeCalledStationIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 18),
    _UsdRadiusClientIncludeCalledStationIdInAccessReq_Type()
)
usdRadiusClientIncludeCalledStationIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeCalledStationIdInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeCallingStationIdInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeCallingStationIdInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeCallingStationIdInAccessReq_Object = MibScalar
usdRadiusClientIncludeCallingStationIdInAccessReq = _UsdRadiusClientIncludeCallingStationIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 19),
    _UsdRadiusClientIncludeCallingStationIdInAccessReq_Type()
)
usdRadiusClientIncludeCallingStationIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeCallingStationIdInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeConnectInfoInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeConnectInfoInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeConnectInfoInAccessReq_Object = MibScalar
usdRadiusClientIncludeConnectInfoInAccessReq = _UsdRadiusClientIncludeConnectInfoInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 20),
    _UsdRadiusClientIncludeConnectInfoInAccessReq_Type()
)
usdRadiusClientIncludeConnectInfoInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeConnectInfoInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeNasIdentifierInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasIdentifierInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeNasIdentifierInAccessReq_Object = MibScalar
usdRadiusClientIncludeNasIdentifierInAccessReq = _UsdRadiusClientIncludeNasIdentifierInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 21),
    _UsdRadiusClientIncludeNasIdentifierInAccessReq_Type()
)
usdRadiusClientIncludeNasIdentifierInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasIdentifierInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeNasPortInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeNasPortInAccessReq_Object = MibScalar
usdRadiusClientIncludeNasPortInAccessReq = _UsdRadiusClientIncludeNasPortInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 22),
    _UsdRadiusClientIncludeNasPortInAccessReq_Type()
)
usdRadiusClientIncludeNasPortInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeNasPortIdInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortIdInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeNasPortIdInAccessReq_Object = MibScalar
usdRadiusClientIncludeNasPortIdInAccessReq = _UsdRadiusClientIncludeNasPortIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 23),
    _UsdRadiusClientIncludeNasPortIdInAccessReq_Type()
)
usdRadiusClientIncludeNasPortIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortIdInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeNasPortTypeInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortTypeInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeNasPortTypeInAccessReq_Object = MibScalar
usdRadiusClientIncludeNasPortTypeInAccessReq = _UsdRadiusClientIncludeNasPortTypeInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 24),
    _UsdRadiusClientIncludeNasPortTypeInAccessReq_Type()
)
usdRadiusClientIncludeNasPortTypeInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortTypeInAccessReq.setStatus("current")


class _UsdRadiusClientIncludePppoeDescriptionInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludePppoeDescriptionInAccessReq based on TruthValue"""


_UsdRadiusClientIncludePppoeDescriptionInAccessReq_Object = MibScalar
usdRadiusClientIncludePppoeDescriptionInAccessReq = _UsdRadiusClientIncludePppoeDescriptionInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 25),
    _UsdRadiusClientIncludePppoeDescriptionInAccessReq_Type()
)
usdRadiusClientIncludePppoeDescriptionInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludePppoeDescriptionInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeTunnelClientAuthIdInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelClientAuthIdInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeTunnelClientAuthIdInAccessReq_Object = MibScalar
usdRadiusClientIncludeTunnelClientAuthIdInAccessReq = _UsdRadiusClientIncludeTunnelClientAuthIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 26),
    _UsdRadiusClientIncludeTunnelClientAuthIdInAccessReq_Type()
)
usdRadiusClientIncludeTunnelClientAuthIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelClientAuthIdInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeTunnelClientEndpointInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelClientEndpointInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeTunnelClientEndpointInAccessReq_Object = MibScalar
usdRadiusClientIncludeTunnelClientEndpointInAccessReq = _UsdRadiusClientIncludeTunnelClientEndpointInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 27),
    _UsdRadiusClientIncludeTunnelClientEndpointInAccessReq_Type()
)
usdRadiusClientIncludeTunnelClientEndpointInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelClientEndpointInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeTunnelMediumTypeInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelMediumTypeInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeTunnelMediumTypeInAccessReq_Object = MibScalar
usdRadiusClientIncludeTunnelMediumTypeInAccessReq = _UsdRadiusClientIncludeTunnelMediumTypeInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 28),
    _UsdRadiusClientIncludeTunnelMediumTypeInAccessReq_Type()
)
usdRadiusClientIncludeTunnelMediumTypeInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelMediumTypeInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerAttributesInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerAttributesInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerAttributesInAccessReq_Object = MibScalar
usdRadiusClientIncludeTunnelServerAttributesInAccessReq = _UsdRadiusClientIncludeTunnelServerAttributesInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 29),
    _UsdRadiusClientIncludeTunnelServerAttributesInAccessReq_Type()
)
usdRadiusClientIncludeTunnelServerAttributesInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerAttributesInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerAuthIdInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerAuthIdInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerAuthIdInAccessReq_Object = MibScalar
usdRadiusClientIncludeTunnelServerAuthIdInAccessReq = _UsdRadiusClientIncludeTunnelServerAuthIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 30),
    _UsdRadiusClientIncludeTunnelServerAuthIdInAccessReq_Type()
)
usdRadiusClientIncludeTunnelServerAuthIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerAuthIdInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerEndpointInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerEndpointInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerEndpointInAccessReq_Object = MibScalar
usdRadiusClientIncludeTunnelServerEndpointInAccessReq = _UsdRadiusClientIncludeTunnelServerEndpointInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 31),
    _UsdRadiusClientIncludeTunnelServerEndpointInAccessReq_Type()
)
usdRadiusClientIncludeTunnelServerEndpointInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerEndpointInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeTunnelTypeInAccessReq_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelTypeInAccessReq based on TruthValue"""


_UsdRadiusClientIncludeTunnelTypeInAccessReq_Object = MibScalar
usdRadiusClientIncludeTunnelTypeInAccessReq = _UsdRadiusClientIncludeTunnelTypeInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 32),
    _UsdRadiusClientIncludeTunnelTypeInAccessReq_Type()
)
usdRadiusClientIncludeTunnelTypeInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelTypeInAccessReq.setStatus("current")


class _UsdRadiusClientIncludeAcctTunnelConnectionInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeAcctTunnelConnectionInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeAcctTunnelConnectionInAcctStart_Object = MibScalar
usdRadiusClientIncludeAcctTunnelConnectionInAcctStart = _UsdRadiusClientIncludeAcctTunnelConnectionInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 33),
    _UsdRadiusClientIncludeAcctTunnelConnectionInAcctStart_Type()
)
usdRadiusClientIncludeAcctTunnelConnectionInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeAcctTunnelConnectionInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeCalledStationIdInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeCalledStationIdInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeCalledStationIdInAcctStart_Object = MibScalar
usdRadiusClientIncludeCalledStationIdInAcctStart = _UsdRadiusClientIncludeCalledStationIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 34),
    _UsdRadiusClientIncludeCalledStationIdInAcctStart_Type()
)
usdRadiusClientIncludeCalledStationIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeCalledStationIdInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeCallingStationIdInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeCallingStationIdInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeCallingStationIdInAcctStart_Object = MibScalar
usdRadiusClientIncludeCallingStationIdInAcctStart = _UsdRadiusClientIncludeCallingStationIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 35),
    _UsdRadiusClientIncludeCallingStationIdInAcctStart_Type()
)
usdRadiusClientIncludeCallingStationIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeCallingStationIdInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeClassInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeClassInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeClassInAcctStart_Object = MibScalar
usdRadiusClientIncludeClassInAcctStart = _UsdRadiusClientIncludeClassInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 36),
    _UsdRadiusClientIncludeClassInAcctStart_Type()
)
usdRadiusClientIncludeClassInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeClassInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeConnectInfoInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeConnectInfoInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeConnectInfoInAcctStart_Object = MibScalar
usdRadiusClientIncludeConnectInfoInAcctStart = _UsdRadiusClientIncludeConnectInfoInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 37),
    _UsdRadiusClientIncludeConnectInfoInAcctStart_Type()
)
usdRadiusClientIncludeConnectInfoInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeConnectInfoInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeEgressPolicyNameInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeEgressPolicyNameInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeEgressPolicyNameInAcctStart_Object = MibScalar
usdRadiusClientIncludeEgressPolicyNameInAcctStart = _UsdRadiusClientIncludeEgressPolicyNameInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 38),
    _UsdRadiusClientIncludeEgressPolicyNameInAcctStart_Type()
)
usdRadiusClientIncludeEgressPolicyNameInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeEgressPolicyNameInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeEventTimestampInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeEventTimestampInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeEventTimestampInAcctStart_Object = MibScalar
usdRadiusClientIncludeEventTimestampInAcctStart = _UsdRadiusClientIncludeEventTimestampInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 39),
    _UsdRadiusClientIncludeEventTimestampInAcctStart_Type()
)
usdRadiusClientIncludeEventTimestampInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeEventTimestampInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeFramedCompressionInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeFramedCompressionInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeFramedCompressionInAcctStart_Object = MibScalar
usdRadiusClientIncludeFramedCompressionInAcctStart = _UsdRadiusClientIncludeFramedCompressionInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 40),
    _UsdRadiusClientIncludeFramedCompressionInAcctStart_Type()
)
usdRadiusClientIncludeFramedCompressionInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeFramedCompressionInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeFramedIpNetmaskInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeFramedIpNetmaskInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeFramedIpNetmaskInAcctStart_Object = MibScalar
usdRadiusClientIncludeFramedIpNetmaskInAcctStart = _UsdRadiusClientIncludeFramedIpNetmaskInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 41),
    _UsdRadiusClientIncludeFramedIpNetmaskInAcctStart_Type()
)
usdRadiusClientIncludeFramedIpNetmaskInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeFramedIpNetmaskInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeIngressPolicyNameInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeIngressPolicyNameInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeIngressPolicyNameInAcctStart_Object = MibScalar
usdRadiusClientIncludeIngressPolicyNameInAcctStart = _UsdRadiusClientIncludeIngressPolicyNameInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 42),
    _UsdRadiusClientIncludeIngressPolicyNameInAcctStart_Type()
)
usdRadiusClientIncludeIngressPolicyNameInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeIngressPolicyNameInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeNasIdentifierInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasIdentifierInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeNasIdentifierInAcctStart_Object = MibScalar
usdRadiusClientIncludeNasIdentifierInAcctStart = _UsdRadiusClientIncludeNasIdentifierInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 43),
    _UsdRadiusClientIncludeNasIdentifierInAcctStart_Type()
)
usdRadiusClientIncludeNasIdentifierInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasIdentifierInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeNasPortInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeNasPortInAcctStart_Object = MibScalar
usdRadiusClientIncludeNasPortInAcctStart = _UsdRadiusClientIncludeNasPortInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 44),
    _UsdRadiusClientIncludeNasPortInAcctStart_Type()
)
usdRadiusClientIncludeNasPortInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeNasPortIdInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortIdInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeNasPortIdInAcctStart_Object = MibScalar
usdRadiusClientIncludeNasPortIdInAcctStart = _UsdRadiusClientIncludeNasPortIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 45),
    _UsdRadiusClientIncludeNasPortIdInAcctStart_Type()
)
usdRadiusClientIncludeNasPortIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortIdInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeNasPortTypeInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortTypeInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeNasPortTypeInAcctStart_Object = MibScalar
usdRadiusClientIncludeNasPortTypeInAcctStart = _UsdRadiusClientIncludeNasPortTypeInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 46),
    _UsdRadiusClientIncludeNasPortTypeInAcctStart_Type()
)
usdRadiusClientIncludeNasPortTypeInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortTypeInAcctStart.setStatus("current")


class _UsdRadiusClientIncludePppoeDescriptionInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludePppoeDescriptionInAcctStart based on TruthValue"""


_UsdRadiusClientIncludePppoeDescriptionInAcctStart_Object = MibScalar
usdRadiusClientIncludePppoeDescriptionInAcctStart = _UsdRadiusClientIncludePppoeDescriptionInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 47),
    _UsdRadiusClientIncludePppoeDescriptionInAcctStart_Type()
)
usdRadiusClientIncludePppoeDescriptionInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludePppoeDescriptionInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelAssignmentIdInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelAssignmentIdInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelAssignmentIdInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelAssignmentIdInAcctStart = _UsdRadiusClientIncludeTunnelAssignmentIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 48),
    _UsdRadiusClientIncludeTunnelAssignmentIdInAcctStart_Type()
)
usdRadiusClientIncludeTunnelAssignmentIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelAssignmentIdInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelClientAuthIdInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelClientAuthIdInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelClientAuthIdInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelClientAuthIdInAcctStart = _UsdRadiusClientIncludeTunnelClientAuthIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 49),
    _UsdRadiusClientIncludeTunnelClientAuthIdInAcctStart_Type()
)
usdRadiusClientIncludeTunnelClientAuthIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelClientAuthIdInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelClientEndpointInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelClientEndpointInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelClientEndpointInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelClientEndpointInAcctStart = _UsdRadiusClientIncludeTunnelClientEndpointInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 50),
    _UsdRadiusClientIncludeTunnelClientEndpointInAcctStart_Type()
)
usdRadiusClientIncludeTunnelClientEndpointInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelClientEndpointInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelMediumTypeInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelMediumTypeInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelMediumTypeInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelMediumTypeInAcctStart = _UsdRadiusClientIncludeTunnelMediumTypeInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 51),
    _UsdRadiusClientIncludeTunnelMediumTypeInAcctStart_Type()
)
usdRadiusClientIncludeTunnelMediumTypeInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelMediumTypeInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelPreferenceInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelPreferenceInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelPreferenceInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelPreferenceInAcctStart = _UsdRadiusClientIncludeTunnelPreferenceInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 52),
    _UsdRadiusClientIncludeTunnelPreferenceInAcctStart_Type()
)
usdRadiusClientIncludeTunnelPreferenceInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelPreferenceInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerAttributesInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerAttributesInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerAttributesInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelServerAttributesInAcctStart = _UsdRadiusClientIncludeTunnelServerAttributesInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 53),
    _UsdRadiusClientIncludeTunnelServerAttributesInAcctStart_Type()
)
usdRadiusClientIncludeTunnelServerAttributesInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerAttributesInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerAuthIdInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerAuthIdInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerAuthIdInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelServerAuthIdInAcctStart = _UsdRadiusClientIncludeTunnelServerAuthIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 54),
    _UsdRadiusClientIncludeTunnelServerAuthIdInAcctStart_Type()
)
usdRadiusClientIncludeTunnelServerAuthIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerAuthIdInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerEndpointInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerEndpointInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerEndpointInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelServerEndpointInAcctStart = _UsdRadiusClientIncludeTunnelServerEndpointInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 55),
    _UsdRadiusClientIncludeTunnelServerEndpointInAcctStart_Type()
)
usdRadiusClientIncludeTunnelServerEndpointInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerEndpointInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeTunnelTypeInAcctStart_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelTypeInAcctStart based on TruthValue"""


_UsdRadiusClientIncludeTunnelTypeInAcctStart_Object = MibScalar
usdRadiusClientIncludeTunnelTypeInAcctStart = _UsdRadiusClientIncludeTunnelTypeInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 56),
    _UsdRadiusClientIncludeTunnelTypeInAcctStart_Type()
)
usdRadiusClientIncludeTunnelTypeInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelTypeInAcctStart.setStatus("current")


class _UsdRadiusClientIncludeAcctTunnelConnectionInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeAcctTunnelConnectionInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeAcctTunnelConnectionInAcctStop_Object = MibScalar
usdRadiusClientIncludeAcctTunnelConnectionInAcctStop = _UsdRadiusClientIncludeAcctTunnelConnectionInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 57),
    _UsdRadiusClientIncludeAcctTunnelConnectionInAcctStop_Type()
)
usdRadiusClientIncludeAcctTunnelConnectionInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeAcctTunnelConnectionInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeCalledStationIdInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeCalledStationIdInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeCalledStationIdInAcctStop_Object = MibScalar
usdRadiusClientIncludeCalledStationIdInAcctStop = _UsdRadiusClientIncludeCalledStationIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 59),
    _UsdRadiusClientIncludeCalledStationIdInAcctStop_Type()
)
usdRadiusClientIncludeCalledStationIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeCalledStationIdInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeCallingStationIdInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeCallingStationIdInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeCallingStationIdInAcctStop_Object = MibScalar
usdRadiusClientIncludeCallingStationIdInAcctStop = _UsdRadiusClientIncludeCallingStationIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 60),
    _UsdRadiusClientIncludeCallingStationIdInAcctStop_Type()
)
usdRadiusClientIncludeCallingStationIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeCallingStationIdInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeClassInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeClassInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeClassInAcctStop_Object = MibScalar
usdRadiusClientIncludeClassInAcctStop = _UsdRadiusClientIncludeClassInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 61),
    _UsdRadiusClientIncludeClassInAcctStop_Type()
)
usdRadiusClientIncludeClassInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeClassInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeConnectInfoInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeConnectInfoInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeConnectInfoInAcctStop_Object = MibScalar
usdRadiusClientIncludeConnectInfoInAcctStop = _UsdRadiusClientIncludeConnectInfoInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 62),
    _UsdRadiusClientIncludeConnectInfoInAcctStop_Type()
)
usdRadiusClientIncludeConnectInfoInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeConnectInfoInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeEgressPolicyNameInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeEgressPolicyNameInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeEgressPolicyNameInAcctStop_Object = MibScalar
usdRadiusClientIncludeEgressPolicyNameInAcctStop = _UsdRadiusClientIncludeEgressPolicyNameInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 63),
    _UsdRadiusClientIncludeEgressPolicyNameInAcctStop_Type()
)
usdRadiusClientIncludeEgressPolicyNameInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeEgressPolicyNameInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeEventTimestampInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeEventTimestampInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeEventTimestampInAcctStop_Object = MibScalar
usdRadiusClientIncludeEventTimestampInAcctStop = _UsdRadiusClientIncludeEventTimestampInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 64),
    _UsdRadiusClientIncludeEventTimestampInAcctStop_Type()
)
usdRadiusClientIncludeEventTimestampInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeEventTimestampInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeFramedCompressionInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeFramedCompressionInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeFramedCompressionInAcctStop_Object = MibScalar
usdRadiusClientIncludeFramedCompressionInAcctStop = _UsdRadiusClientIncludeFramedCompressionInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 65),
    _UsdRadiusClientIncludeFramedCompressionInAcctStop_Type()
)
usdRadiusClientIncludeFramedCompressionInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeFramedCompressionInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeFramedIpNetmaskInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeFramedIpNetmaskInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeFramedIpNetmaskInAcctStop_Object = MibScalar
usdRadiusClientIncludeFramedIpNetmaskInAcctStop = _UsdRadiusClientIncludeFramedIpNetmaskInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 66),
    _UsdRadiusClientIncludeFramedIpNetmaskInAcctStop_Type()
)
usdRadiusClientIncludeFramedIpNetmaskInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeFramedIpNetmaskInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeIngressPolicyNameInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeIngressPolicyNameInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeIngressPolicyNameInAcctStop_Object = MibScalar
usdRadiusClientIncludeIngressPolicyNameInAcctStop = _UsdRadiusClientIncludeIngressPolicyNameInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 67),
    _UsdRadiusClientIncludeIngressPolicyNameInAcctStop_Type()
)
usdRadiusClientIncludeIngressPolicyNameInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeIngressPolicyNameInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeInputGigawordsInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeInputGigawordsInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeInputGigawordsInAcctStop_Object = MibScalar
usdRadiusClientIncludeInputGigawordsInAcctStop = _UsdRadiusClientIncludeInputGigawordsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 68),
    _UsdRadiusClientIncludeInputGigawordsInAcctStop_Type()
)
usdRadiusClientIncludeInputGigawordsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeInputGigawordsInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeNasIdentifierInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasIdentifierInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeNasIdentifierInAcctStop_Object = MibScalar
usdRadiusClientIncludeNasIdentifierInAcctStop = _UsdRadiusClientIncludeNasIdentifierInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 69),
    _UsdRadiusClientIncludeNasIdentifierInAcctStop_Type()
)
usdRadiusClientIncludeNasIdentifierInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasIdentifierInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeNasPortInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeNasPortInAcctStop_Object = MibScalar
usdRadiusClientIncludeNasPortInAcctStop = _UsdRadiusClientIncludeNasPortInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 70),
    _UsdRadiusClientIncludeNasPortInAcctStop_Type()
)
usdRadiusClientIncludeNasPortInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeNasPortIdInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortIdInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeNasPortIdInAcctStop_Object = MibScalar
usdRadiusClientIncludeNasPortIdInAcctStop = _UsdRadiusClientIncludeNasPortIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 71),
    _UsdRadiusClientIncludeNasPortIdInAcctStop_Type()
)
usdRadiusClientIncludeNasPortIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortIdInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeNasPortTypeInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeNasPortTypeInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeNasPortTypeInAcctStop_Object = MibScalar
usdRadiusClientIncludeNasPortTypeInAcctStop = _UsdRadiusClientIncludeNasPortTypeInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 72),
    _UsdRadiusClientIncludeNasPortTypeInAcctStop_Type()
)
usdRadiusClientIncludeNasPortTypeInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeNasPortTypeInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeOutputGigawordsInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeOutputGigawordsInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeOutputGigawordsInAcctStop_Object = MibScalar
usdRadiusClientIncludeOutputGigawordsInAcctStop = _UsdRadiusClientIncludeOutputGigawordsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 73),
    _UsdRadiusClientIncludeOutputGigawordsInAcctStop_Type()
)
usdRadiusClientIncludeOutputGigawordsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeOutputGigawordsInAcctStop.setStatus("current")


class _UsdRadiusClientIncludePppoeDescriptionInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludePppoeDescriptionInAcctStop based on TruthValue"""


_UsdRadiusClientIncludePppoeDescriptionInAcctStop_Object = MibScalar
usdRadiusClientIncludePppoeDescriptionInAcctStop = _UsdRadiusClientIncludePppoeDescriptionInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 74),
    _UsdRadiusClientIncludePppoeDescriptionInAcctStop_Type()
)
usdRadiusClientIncludePppoeDescriptionInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludePppoeDescriptionInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelAssignmentIdInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelAssignmentIdInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelAssignmentIdInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelAssignmentIdInAcctStop = _UsdRadiusClientIncludeTunnelAssignmentIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 75),
    _UsdRadiusClientIncludeTunnelAssignmentIdInAcctStop_Type()
)
usdRadiusClientIncludeTunnelAssignmentIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelAssignmentIdInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelClientAuthIdInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelClientAuthIdInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelClientAuthIdInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelClientAuthIdInAcctStop = _UsdRadiusClientIncludeTunnelClientAuthIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 76),
    _UsdRadiusClientIncludeTunnelClientAuthIdInAcctStop_Type()
)
usdRadiusClientIncludeTunnelClientAuthIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelClientAuthIdInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelClientEndpointInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelClientEndpointInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelClientEndpointInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelClientEndpointInAcctStop = _UsdRadiusClientIncludeTunnelClientEndpointInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 77),
    _UsdRadiusClientIncludeTunnelClientEndpointInAcctStop_Type()
)
usdRadiusClientIncludeTunnelClientEndpointInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelClientEndpointInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelMediumTypeInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelMediumTypeInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelMediumTypeInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelMediumTypeInAcctStop = _UsdRadiusClientIncludeTunnelMediumTypeInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 78),
    _UsdRadiusClientIncludeTunnelMediumTypeInAcctStop_Type()
)
usdRadiusClientIncludeTunnelMediumTypeInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelMediumTypeInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelPreferenceInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelPreferenceInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelPreferenceInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelPreferenceInAcctStop = _UsdRadiusClientIncludeTunnelPreferenceInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 79),
    _UsdRadiusClientIncludeTunnelPreferenceInAcctStop_Type()
)
usdRadiusClientIncludeTunnelPreferenceInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelPreferenceInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerAttributesInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerAttributesInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerAttributesInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelServerAttributesInAcctStop = _UsdRadiusClientIncludeTunnelServerAttributesInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 80),
    _UsdRadiusClientIncludeTunnelServerAttributesInAcctStop_Type()
)
usdRadiusClientIncludeTunnelServerAttributesInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerAttributesInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerAuthIdInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerAuthIdInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerAuthIdInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelServerAuthIdInAcctStop = _UsdRadiusClientIncludeTunnelServerAuthIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 81),
    _UsdRadiusClientIncludeTunnelServerAuthIdInAcctStop_Type()
)
usdRadiusClientIncludeTunnelServerAuthIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerAuthIdInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelServerEndpointInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelServerEndpointInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelServerEndpointInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelServerEndpointInAcctStop = _UsdRadiusClientIncludeTunnelServerEndpointInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 82),
    _UsdRadiusClientIncludeTunnelServerEndpointInAcctStop_Type()
)
usdRadiusClientIncludeTunnelServerEndpointInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelServerEndpointInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeTunnelTypeInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeTunnelTypeInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeTunnelTypeInAcctStop_Object = MibScalar
usdRadiusClientIncludeTunnelTypeInAcctStop = _UsdRadiusClientIncludeTunnelTypeInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 83),
    _UsdRadiusClientIncludeTunnelTypeInAcctStop_Type()
)
usdRadiusClientIncludeTunnelTypeInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeTunnelTypeInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeInputGigapktsInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeInputGigapktsInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeInputGigapktsInAcctStop_Object = MibScalar
usdRadiusClientIncludeInputGigapktsInAcctStop = _UsdRadiusClientIncludeInputGigapktsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 84),
    _UsdRadiusClientIncludeInputGigapktsInAcctStop_Type()
)
usdRadiusClientIncludeInputGigapktsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeInputGigapktsInAcctStop.setStatus("current")


class _UsdRadiusClientIncludeOutputGigapktsInAcctStop_Type(TruthValue):
    """Custom type usdRadiusClientIncludeOutputGigapktsInAcctStop based on TruthValue"""


_UsdRadiusClientIncludeOutputGigapktsInAcctStop_Object = MibScalar
usdRadiusClientIncludeOutputGigapktsInAcctStop = _UsdRadiusClientIncludeOutputGigapktsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 85),
    _UsdRadiusClientIncludeOutputGigapktsInAcctStop_Type()
)
usdRadiusClientIncludeOutputGigapktsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIncludeOutputGigapktsInAcctStop.setStatus("current")


class _UsdRadiusClientIgnoreFramedIpNetmask_Type(TruthValue):
    """Custom type usdRadiusClientIgnoreFramedIpNetmask based on TruthValue"""


_UsdRadiusClientIgnoreFramedIpNetmask_Object = MibScalar
usdRadiusClientIgnoreFramedIpNetmask = _UsdRadiusClientIgnoreFramedIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 86),
    _UsdRadiusClientIgnoreFramedIpNetmask_Type()
)
usdRadiusClientIgnoreFramedIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRadiusClientIgnoreFramedIpNetmask.setStatus("current")
_UsdRadiusAuthClient_ObjectIdentity = ObjectIdentity
usdRadiusAuthClient = _UsdRadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2)
)
_UsdRadiusAuthClientInvalidServerAddresses_Type = Counter32
_UsdRadiusAuthClientInvalidServerAddresses_Object = MibScalar
usdRadiusAuthClientInvalidServerAddresses = _UsdRadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 1),
    _UsdRadiusAuthClientInvalidServerAddresses_Type()
)
usdRadiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientInvalidServerAddresses.setStatus("current")
_UsdRadiusAuthClientServerTable_Object = MibTable
usdRadiusAuthClientServerTable = _UsdRadiusAuthClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdRadiusAuthClientServerTable.setStatus("current")
_UsdRadiusAuthClientServerEntry_Object = MibTableRow
usdRadiusAuthClientServerEntry = _UsdRadiusAuthClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1)
)
usdRadiusAuthClientServerEntry.setIndexNames(
    (0, "Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientServerAddress"),
)
if mibBuilder.loadTexts:
    usdRadiusAuthClientServerEntry.setStatus("current")
_UsdRadiusAuthClientServerAddress_Type = IpAddress
_UsdRadiusAuthClientServerAddress_Object = MibTableColumn
usdRadiusAuthClientServerAddress = _UsdRadiusAuthClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 1),
    _UsdRadiusAuthClientServerAddress_Type()
)
usdRadiusAuthClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRadiusAuthClientServerAddress.setStatus("current")
_UsdRadiusAuthClientServerPortNumber_Type = Integer32
_UsdRadiusAuthClientServerPortNumber_Object = MibTableColumn
usdRadiusAuthClientServerPortNumber = _UsdRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 2),
    _UsdRadiusAuthClientServerPortNumber_Type()
)
usdRadiusAuthClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientServerPortNumber.setStatus("current")
_UsdRadiusAuthClientRoundTripTime_Type = TimeTicks
_UsdRadiusAuthClientRoundTripTime_Object = MibTableColumn
usdRadiusAuthClientRoundTripTime = _UsdRadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 3),
    _UsdRadiusAuthClientRoundTripTime_Type()
)
usdRadiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientRoundTripTime.setStatus("current")
_UsdRadiusAuthClientAccessRequests_Type = Counter32
_UsdRadiusAuthClientAccessRequests_Object = MibTableColumn
usdRadiusAuthClientAccessRequests = _UsdRadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 4),
    _UsdRadiusAuthClientAccessRequests_Type()
)
usdRadiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientAccessRequests.setStatus("current")
_UsdRadiusAuthClientAccessRetransmissions_Type = Counter32
_UsdRadiusAuthClientAccessRetransmissions_Object = MibTableColumn
usdRadiusAuthClientAccessRetransmissions = _UsdRadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 5),
    _UsdRadiusAuthClientAccessRetransmissions_Type()
)
usdRadiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientAccessRetransmissions.setStatus("current")
_UsdRadiusAuthClientAccessAccepts_Type = Counter32
_UsdRadiusAuthClientAccessAccepts_Object = MibTableColumn
usdRadiusAuthClientAccessAccepts = _UsdRadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 6),
    _UsdRadiusAuthClientAccessAccepts_Type()
)
usdRadiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientAccessAccepts.setStatus("current")
_UsdRadiusAuthClientAccessRejects_Type = Counter32
_UsdRadiusAuthClientAccessRejects_Object = MibTableColumn
usdRadiusAuthClientAccessRejects = _UsdRadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 7),
    _UsdRadiusAuthClientAccessRejects_Type()
)
usdRadiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientAccessRejects.setStatus("current")
_UsdRadiusAuthClientAccessChallenges_Type = Counter32
_UsdRadiusAuthClientAccessChallenges_Object = MibTableColumn
usdRadiusAuthClientAccessChallenges = _UsdRadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 8),
    _UsdRadiusAuthClientAccessChallenges_Type()
)
usdRadiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientAccessChallenges.setStatus("current")
_UsdRadiusAuthClientMalformedAccessResponses_Type = Counter32
_UsdRadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
usdRadiusAuthClientMalformedAccessResponses = _UsdRadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 9),
    _UsdRadiusAuthClientMalformedAccessResponses_Type()
)
usdRadiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientMalformedAccessResponses.setStatus("current")
_UsdRadiusAuthClientBadAuthenticators_Type = Counter32
_UsdRadiusAuthClientBadAuthenticators_Object = MibTableColumn
usdRadiusAuthClientBadAuthenticators = _UsdRadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 10),
    _UsdRadiusAuthClientBadAuthenticators_Type()
)
usdRadiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientBadAuthenticators.setStatus("current")
_UsdRadiusAuthClientPendingRequests_Type = Gauge32
_UsdRadiusAuthClientPendingRequests_Object = MibTableColumn
usdRadiusAuthClientPendingRequests = _UsdRadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 11),
    _UsdRadiusAuthClientPendingRequests_Type()
)
usdRadiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientPendingRequests.setStatus("current")
_UsdRadiusAuthClientTimeouts_Type = Counter32
_UsdRadiusAuthClientTimeouts_Object = MibTableColumn
usdRadiusAuthClientTimeouts = _UsdRadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 12),
    _UsdRadiusAuthClientTimeouts_Type()
)
usdRadiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientTimeouts.setStatus("current")
_UsdRadiusAuthClientUnknownTypes_Type = Counter32
_UsdRadiusAuthClientUnknownTypes_Object = MibTableColumn
usdRadiusAuthClientUnknownTypes = _UsdRadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 13),
    _UsdRadiusAuthClientUnknownTypes_Type()
)
usdRadiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientUnknownTypes.setStatus("current")
_UsdRadiusAuthClientPacketsDropped_Type = Counter32
_UsdRadiusAuthClientPacketsDropped_Object = MibTableColumn
usdRadiusAuthClientPacketsDropped = _UsdRadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 14),
    _UsdRadiusAuthClientPacketsDropped_Type()
)
usdRadiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientPacketsDropped.setStatus("current")
_UsdRadiusAuthClientCfgServerTable_Object = MibTable
usdRadiusAuthClientCfgServerTable = _UsdRadiusAuthClientCfgServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3)
)
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgServerTable.setStatus("current")
_UsdRadiusAuthClientCfgServerEntry_Object = MibTableRow
usdRadiusAuthClientCfgServerEntry = _UsdRadiusAuthClientCfgServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1)
)
usdRadiusAuthClientCfgServerEntry.setIndexNames(
    (0, "Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgServerAddress"),
)
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgServerEntry.setStatus("current")
_UsdRadiusAuthClientCfgServerAddress_Type = IpAddress
_UsdRadiusAuthClientCfgServerAddress_Object = MibTableColumn
usdRadiusAuthClientCfgServerAddress = _UsdRadiusAuthClientCfgServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 1),
    _UsdRadiusAuthClientCfgServerAddress_Type()
)
usdRadiusAuthClientCfgServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgServerAddress.setStatus("current")


class _UsdRadiusAuthClientCfgServerPortNumber_Type(Integer32):
    """Custom type usdRadiusAuthClientCfgServerPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdRadiusAuthClientCfgServerPortNumber_Type.__name__ = "Integer32"
_UsdRadiusAuthClientCfgServerPortNumber_Object = MibTableColumn
usdRadiusAuthClientCfgServerPortNumber = _UsdRadiusAuthClientCfgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 2),
    _UsdRadiusAuthClientCfgServerPortNumber_Type()
)
usdRadiusAuthClientCfgServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgServerPortNumber.setStatus("current")


class _UsdRadiusAuthClientCfgKey_Type(DisplayString):
    """Custom type usdRadiusAuthClientCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdRadiusAuthClientCfgKey_Type.__name__ = "DisplayString"
_UsdRadiusAuthClientCfgKey_Object = MibTableColumn
usdRadiusAuthClientCfgKey = _UsdRadiusAuthClientCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 3),
    _UsdRadiusAuthClientCfgKey_Type()
)
usdRadiusAuthClientCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgKey.setStatus("current")


class _UsdRadiusAuthClientCfgTimeoutInterval_Type(Integer32):
    """Custom type usdRadiusAuthClientCfgTimeoutInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_UsdRadiusAuthClientCfgTimeoutInterval_Type.__name__ = "Integer32"
_UsdRadiusAuthClientCfgTimeoutInterval_Object = MibTableColumn
usdRadiusAuthClientCfgTimeoutInterval = _UsdRadiusAuthClientCfgTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 4),
    _UsdRadiusAuthClientCfgTimeoutInterval_Type()
)
usdRadiusAuthClientCfgTimeoutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgTimeoutInterval.setUnits("seconds")


class _UsdRadiusAuthClientCfgRetries_Type(Integer32):
    """Custom type usdRadiusAuthClientCfgRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_UsdRadiusAuthClientCfgRetries_Type.__name__ = "Integer32"
_UsdRadiusAuthClientCfgRetries_Object = MibTableColumn
usdRadiusAuthClientCfgRetries = _UsdRadiusAuthClientCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 5),
    _UsdRadiusAuthClientCfgRetries_Type()
)
usdRadiusAuthClientCfgRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgRetries.setStatus("current")


class _UsdRadiusAuthClientCfgMaxPendingRequests_Type(Integer32):
    """Custom type usdRadiusAuthClientCfgMaxPendingRequests based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4000),
    )


_UsdRadiusAuthClientCfgMaxPendingRequests_Type.__name__ = "Integer32"
_UsdRadiusAuthClientCfgMaxPendingRequests_Object = MibTableColumn
usdRadiusAuthClientCfgMaxPendingRequests = _UsdRadiusAuthClientCfgMaxPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 6),
    _UsdRadiusAuthClientCfgMaxPendingRequests_Type()
)
usdRadiusAuthClientCfgMaxPendingRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgMaxPendingRequests.setStatus("current")
_UsdRadiusAuthClientCfgRowStatus_Type = RowStatus
_UsdRadiusAuthClientCfgRowStatus_Object = MibTableColumn
usdRadiusAuthClientCfgRowStatus = _UsdRadiusAuthClientCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 7),
    _UsdRadiusAuthClientCfgRowStatus_Type()
)
usdRadiusAuthClientCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgRowStatus.setStatus("current")


class _UsdRadiusAuthClientCfgPrecedence_Type(Integer32):
    """Custom type usdRadiusAuthClientCfgPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdRadiusAuthClientCfgPrecedence_Type.__name__ = "Integer32"
_UsdRadiusAuthClientCfgPrecedence_Object = MibTableColumn
usdRadiusAuthClientCfgPrecedence = _UsdRadiusAuthClientCfgPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 8),
    _UsdRadiusAuthClientCfgPrecedence_Type()
)
usdRadiusAuthClientCfgPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgPrecedence.setStatus("current")


class _UsdRadiusAuthClientCfgDeadTime_Type(Integer32):
    """Custom type usdRadiusAuthClientCfgDeadTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_UsdRadiusAuthClientCfgDeadTime_Type.__name__ = "Integer32"
_UsdRadiusAuthClientCfgDeadTime_Object = MibTableColumn
usdRadiusAuthClientCfgDeadTime = _UsdRadiusAuthClientCfgDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 9),
    _UsdRadiusAuthClientCfgDeadTime_Type()
)
usdRadiusAuthClientCfgDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    usdRadiusAuthClientCfgDeadTime.setUnits("minutes")
_UsdRadiusAcctClient_ObjectIdentity = ObjectIdentity
usdRadiusAcctClient = _UsdRadiusAcctClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3)
)
_UsdRadiusAcctClientInvalidServerAddresses_Type = Counter32
_UsdRadiusAcctClientInvalidServerAddresses_Object = MibScalar
usdRadiusAcctClientInvalidServerAddresses = _UsdRadiusAcctClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 1),
    _UsdRadiusAcctClientInvalidServerAddresses_Type()
)
usdRadiusAcctClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientInvalidServerAddresses.setStatus("current")
_UsdRadiusAcctClientServerTable_Object = MibTable
usdRadiusAcctClientServerTable = _UsdRadiusAcctClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdRadiusAcctClientServerTable.setStatus("current")
_UsdRadiusAcctClientServerEntry_Object = MibTableRow
usdRadiusAcctClientServerEntry = _UsdRadiusAcctClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1)
)
usdRadiusAcctClientServerEntry.setIndexNames(
    (0, "Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientServerAddress"),
)
if mibBuilder.loadTexts:
    usdRadiusAcctClientServerEntry.setStatus("current")
_UsdRadiusAcctClientServerAddress_Type = IpAddress
_UsdRadiusAcctClientServerAddress_Object = MibTableColumn
usdRadiusAcctClientServerAddress = _UsdRadiusAcctClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 1),
    _UsdRadiusAcctClientServerAddress_Type()
)
usdRadiusAcctClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRadiusAcctClientServerAddress.setStatus("current")
_UsdRadiusAcctClientServerPortNumber_Type = Integer32
_UsdRadiusAcctClientServerPortNumber_Object = MibTableColumn
usdRadiusAcctClientServerPortNumber = _UsdRadiusAcctClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 2),
    _UsdRadiusAcctClientServerPortNumber_Type()
)
usdRadiusAcctClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientServerPortNumber.setStatus("current")
_UsdRadiusAcctClientRoundTripTime_Type = TimeTicks
_UsdRadiusAcctClientRoundTripTime_Object = MibTableColumn
usdRadiusAcctClientRoundTripTime = _UsdRadiusAcctClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 3),
    _UsdRadiusAcctClientRoundTripTime_Type()
)
usdRadiusAcctClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientRoundTripTime.setStatus("current")
_UsdRadiusAcctClientRequests_Type = Counter32
_UsdRadiusAcctClientRequests_Object = MibTableColumn
usdRadiusAcctClientRequests = _UsdRadiusAcctClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 4),
    _UsdRadiusAcctClientRequests_Type()
)
usdRadiusAcctClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientRequests.setStatus("current")
_UsdRadiusAcctClientRetransmissions_Type = Counter32
_UsdRadiusAcctClientRetransmissions_Object = MibTableColumn
usdRadiusAcctClientRetransmissions = _UsdRadiusAcctClientRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 5),
    _UsdRadiusAcctClientRetransmissions_Type()
)
usdRadiusAcctClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientRetransmissions.setStatus("current")
_UsdRadiusAcctClientResponses_Type = Counter32
_UsdRadiusAcctClientResponses_Object = MibTableColumn
usdRadiusAcctClientResponses = _UsdRadiusAcctClientResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 6),
    _UsdRadiusAcctClientResponses_Type()
)
usdRadiusAcctClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientResponses.setStatus("current")
_UsdRadiusAcctClientMalformedResponses_Type = Counter32
_UsdRadiusAcctClientMalformedResponses_Object = MibTableColumn
usdRadiusAcctClientMalformedResponses = _UsdRadiusAcctClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 7),
    _UsdRadiusAcctClientMalformedResponses_Type()
)
usdRadiusAcctClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientMalformedResponses.setStatus("current")
_UsdRadiusAcctClientBadAuthenticators_Type = Counter32
_UsdRadiusAcctClientBadAuthenticators_Object = MibTableColumn
usdRadiusAcctClientBadAuthenticators = _UsdRadiusAcctClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 8),
    _UsdRadiusAcctClientBadAuthenticators_Type()
)
usdRadiusAcctClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientBadAuthenticators.setStatus("current")
_UsdRadiusAcctClientPendingRequests_Type = Gauge32
_UsdRadiusAcctClientPendingRequests_Object = MibTableColumn
usdRadiusAcctClientPendingRequests = _UsdRadiusAcctClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 9),
    _UsdRadiusAcctClientPendingRequests_Type()
)
usdRadiusAcctClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientPendingRequests.setStatus("current")
_UsdRadiusAcctClientTimeouts_Type = Counter32
_UsdRadiusAcctClientTimeouts_Object = MibTableColumn
usdRadiusAcctClientTimeouts = _UsdRadiusAcctClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 10),
    _UsdRadiusAcctClientTimeouts_Type()
)
usdRadiusAcctClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientTimeouts.setStatus("current")
_UsdRadiusAcctClientUnknownTypes_Type = Counter32
_UsdRadiusAcctClientUnknownTypes_Object = MibTableColumn
usdRadiusAcctClientUnknownTypes = _UsdRadiusAcctClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 11),
    _UsdRadiusAcctClientUnknownTypes_Type()
)
usdRadiusAcctClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientUnknownTypes.setStatus("current")
_UsdRadiusAcctClientPacketsDropped_Type = Counter32
_UsdRadiusAcctClientPacketsDropped_Object = MibTableColumn
usdRadiusAcctClientPacketsDropped = _UsdRadiusAcctClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 12),
    _UsdRadiusAcctClientPacketsDropped_Type()
)
usdRadiusAcctClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientPacketsDropped.setStatus("current")
_UsdRadiusAcctClientCfgServerTable_Object = MibTable
usdRadiusAcctClientCfgServerTable = _UsdRadiusAcctClientCfgServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3)
)
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgServerTable.setStatus("current")
_UsdRadiusAcctClientCfgServerEntry_Object = MibTableRow
usdRadiusAcctClientCfgServerEntry = _UsdRadiusAcctClientCfgServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1)
)
usdRadiusAcctClientCfgServerEntry.setIndexNames(
    (0, "Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgServerAddress"),
)
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgServerEntry.setStatus("current")
_UsdRadiusAcctClientCfgServerAddress_Type = IpAddress
_UsdRadiusAcctClientCfgServerAddress_Object = MibTableColumn
usdRadiusAcctClientCfgServerAddress = _UsdRadiusAcctClientCfgServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 1),
    _UsdRadiusAcctClientCfgServerAddress_Type()
)
usdRadiusAcctClientCfgServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgServerAddress.setStatus("current")


class _UsdRadiusAcctClientCfgServerPortNumber_Type(Integer32):
    """Custom type usdRadiusAcctClientCfgServerPortNumber based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdRadiusAcctClientCfgServerPortNumber_Type.__name__ = "Integer32"
_UsdRadiusAcctClientCfgServerPortNumber_Object = MibTableColumn
usdRadiusAcctClientCfgServerPortNumber = _UsdRadiusAcctClientCfgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 2),
    _UsdRadiusAcctClientCfgServerPortNumber_Type()
)
usdRadiusAcctClientCfgServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgServerPortNumber.setStatus("current")


class _UsdRadiusAcctClientCfgKey_Type(DisplayString):
    """Custom type usdRadiusAcctClientCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdRadiusAcctClientCfgKey_Type.__name__ = "DisplayString"
_UsdRadiusAcctClientCfgKey_Object = MibTableColumn
usdRadiusAcctClientCfgKey = _UsdRadiusAcctClientCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 3),
    _UsdRadiusAcctClientCfgKey_Type()
)
usdRadiusAcctClientCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgKey.setStatus("current")


class _UsdRadiusAcctClientCfgTimeoutInterval_Type(Integer32):
    """Custom type usdRadiusAcctClientCfgTimeoutInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 30),
    )


_UsdRadiusAcctClientCfgTimeoutInterval_Type.__name__ = "Integer32"
_UsdRadiusAcctClientCfgTimeoutInterval_Object = MibTableColumn
usdRadiusAcctClientCfgTimeoutInterval = _UsdRadiusAcctClientCfgTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 4),
    _UsdRadiusAcctClientCfgTimeoutInterval_Type()
)
usdRadiusAcctClientCfgTimeoutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgTimeoutInterval.setUnits("seconds")


class _UsdRadiusAcctClientCfgRetries_Type(Integer32):
    """Custom type usdRadiusAcctClientCfgRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_UsdRadiusAcctClientCfgRetries_Type.__name__ = "Integer32"
_UsdRadiusAcctClientCfgRetries_Object = MibTableColumn
usdRadiusAcctClientCfgRetries = _UsdRadiusAcctClientCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 5),
    _UsdRadiusAcctClientCfgRetries_Type()
)
usdRadiusAcctClientCfgRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgRetries.setStatus("current")


class _UsdRadiusAcctClientCfgMaxPendingRequests_Type(Integer32):
    """Custom type usdRadiusAcctClientCfgMaxPendingRequests based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 4000),
    )


_UsdRadiusAcctClientCfgMaxPendingRequests_Type.__name__ = "Integer32"
_UsdRadiusAcctClientCfgMaxPendingRequests_Object = MibTableColumn
usdRadiusAcctClientCfgMaxPendingRequests = _UsdRadiusAcctClientCfgMaxPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 6),
    _UsdRadiusAcctClientCfgMaxPendingRequests_Type()
)
usdRadiusAcctClientCfgMaxPendingRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgMaxPendingRequests.setStatus("current")
_UsdRadiusAcctClientCfgRowStatus_Type = RowStatus
_UsdRadiusAcctClientCfgRowStatus_Object = MibTableColumn
usdRadiusAcctClientCfgRowStatus = _UsdRadiusAcctClientCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 7),
    _UsdRadiusAcctClientCfgRowStatus_Type()
)
usdRadiusAcctClientCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgRowStatus.setStatus("current")


class _UsdRadiusAcctClientCfgPrecedence_Type(Integer32):
    """Custom type usdRadiusAcctClientCfgPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdRadiusAcctClientCfgPrecedence_Type.__name__ = "Integer32"
_UsdRadiusAcctClientCfgPrecedence_Object = MibTableColumn
usdRadiusAcctClientCfgPrecedence = _UsdRadiusAcctClientCfgPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 8),
    _UsdRadiusAcctClientCfgPrecedence_Type()
)
usdRadiusAcctClientCfgPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgPrecedence.setStatus("current")


class _UsdRadiusAcctClientCfgDeadTime_Type(Integer32):
    """Custom type usdRadiusAcctClientCfgDeadTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_UsdRadiusAcctClientCfgDeadTime_Type.__name__ = "Integer32"
_UsdRadiusAcctClientCfgDeadTime_Object = MibTableColumn
usdRadiusAcctClientCfgDeadTime = _UsdRadiusAcctClientCfgDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 9),
    _UsdRadiusAcctClientCfgDeadTime_Type()
)
usdRadiusAcctClientCfgDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    usdRadiusAcctClientCfgDeadTime.setUnits("minutes")
_UsdRadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
usdRadiusClientMIBConformance = _UsdRadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2)
)
_UsdRadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
usdRadiusClientMIBCompliances = _UsdRadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1)
)
_UsdRadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
usdRadiusClientMIBGroups = _UsdRadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2)
)

# Managed Objects groups

usdRadiusGeneralClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 1)
)
usdRadiusGeneralClientGroup.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIdentifier"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAlgorithm"))
)
if mibBuilder.loadTexts:
    usdRadiusGeneralClientGroup.setStatus("obsolete")

usdRadiusAuthClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 2)
)
usdRadiusAuthClientGroup.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientInvalidServerAddresses"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientServerPortNumber"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientRoundTripTime"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientAccessRequests"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientAccessRetransmissions"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientAccessAccepts"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientAccessRejects"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientAccessChallenges"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientMalformedAccessResponses"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientBadAuthenticators"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientPendingRequests"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientTimeouts"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientUnknownTypes"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientPacketsDropped"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgServerPortNumber"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgKey"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgTimeoutInterval"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgRetries"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgMaxPendingRequests"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgRowStatus"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgPrecedence"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAuthClientCfgDeadTime"))
)
if mibBuilder.loadTexts:
    usdRadiusAuthClientGroup.setStatus("current")

usdRadiusAcctClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 3)
)
usdRadiusAcctClientGroup.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientInvalidServerAddresses"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientServerPortNumber"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientRoundTripTime"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientRequests"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientRetransmissions"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientResponses"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientMalformedResponses"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientBadAuthenticators"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientPendingRequests"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientTimeouts"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientUnknownTypes"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientPacketsDropped"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgServerPortNumber"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgKey"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgTimeoutInterval"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgRetries"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgMaxPendingRequests"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgRowStatus"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgPrecedence"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusAcctClientCfgDeadTime"))
)
if mibBuilder.loadTexts:
    usdRadiusAcctClientGroup.setStatus("current")

usdRadiusGeneralClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 4)
)
usdRadiusGeneralClientGroup2.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIdentifier"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAlgorithm"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientSourceAddress"))
)
if mibBuilder.loadTexts:
    usdRadiusGeneralClientGroup2.setStatus("obsolete")

usdRadiusBasicClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 5)
)
usdRadiusBasicClientGroup.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIdentifier"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAlgorithm"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientSourceAddress"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientUdpChecksum"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasIdentifier"))
)
if mibBuilder.loadTexts:
    usdRadiusBasicClientGroup.setStatus("obsolete")

usdRadiusBrasClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 6)
)
usdRadiusBrasClientGroup.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientDslPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAcctSessionIdFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasPortFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationDelimiter"))
)
if mibBuilder.loadTexts:
    usdRadiusBrasClientGroup.setStatus("obsolete")

usdRadiusTunnelClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 7)
)
usdRadiusTunnelClientGroup.setObjects(
    ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientTunnelAccounting")
)
if mibBuilder.loadTexts:
    usdRadiusTunnelClientGroup.setStatus("current")

usdRadiusBrasClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 8)
)
usdRadiusBrasClientGroup2.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientDslPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAcctSessionIdFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasPortFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationDelimiter"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientEthernetPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeIpAddrInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeAcctSessionIdInAccessReq"))
)
if mibBuilder.loadTexts:
    usdRadiusBrasClientGroup2.setStatus("obsolete")

usdRadiusBasicClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 9)
)
usdRadiusBasicClientGroup2.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIdentifier"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAlgorithm"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientSourceAddress"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientUdpChecksum"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasIdentifier"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientRollover"))
)
if mibBuilder.loadTexts:
    usdRadiusBasicClientGroup2.setStatus("current")

usdRadiusBrasClientGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 10)
)
usdRadiusBrasClientGroup3.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientDslPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAcctSessionIdFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasPortFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationDelimiter"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientEthernetPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeIpAddrInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationIdFormat"))
)
if mibBuilder.loadTexts:
    usdRadiusBrasClientGroup3.setStatus("obsolete")

usdRadiusBrasClientGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 11)
)
usdRadiusBrasClientGroup4.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientDslPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAcctSessionIdFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasPortFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationDelimiter"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientEthernetPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeIpAddrInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationIdFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasIpAddrUse"))
)
if mibBuilder.loadTexts:
    usdRadiusBrasClientGroup4.setStatus("obsolete")

usdRadiusBrasClientGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 12)
)
usdRadiusBrasClientGroup5.setObjects(
      *(("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientDslPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientAcctSessionIdFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasPortFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationDelimiter"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientEthernetPortType"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeIpAddrInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientCallingStationIdFormat"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientNasIpAddrUse"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeConnectInfoInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeClassInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeConnectInfoInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeEventTimestampInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortIdInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeClassInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeConnectInfoInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeEventTimestampInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortIdInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Unisphere-Data-RADIUS-CLIENT-MIB", "usdRadiusClientIgnoreFramedIpNetmask"))
)
if mibBuilder.loadTexts:
    usdRadiusBrasClientGroup5.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdRadiusAuthClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdRadiusAuthClientCompliance.setStatus(
        "obsolete"
    )

usdRadiusAcctClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdRadiusAcctClientCompliance.setStatus(
        "obsolete"
    )

usdRadiusAuthClientCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 3)
)
if mibBuilder.loadTexts:
    usdRadiusAuthClientCompliance2.setStatus(
        "obsolete"
    )

usdRadiusAcctClientCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 4)
)
if mibBuilder.loadTexts:
    usdRadiusAcctClientCompliance2.setStatus(
        "obsolete"
    )

usdRadiusClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 5)
)
if mibBuilder.loadTexts:
    usdRadiusClientCompliance.setStatus(
        "obsolete"
    )

usdRadiusClientCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 6)
)
if mibBuilder.loadTexts:
    usdRadiusClientCompliance2.setStatus(
        "obsolete"
    )

usdRadiusClientCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 7)
)
if mibBuilder.loadTexts:
    usdRadiusClientCompliance3.setStatus(
        "obsolete"
    )

usdRadiusClientCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 8)
)
if mibBuilder.loadTexts:
    usdRadiusClientCompliance4.setStatus(
        "obsolete"
    )

usdRadiusClientCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 9)
)
if mibBuilder.loadTexts:
    usdRadiusClientCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-RADIUS-CLIENT-MIB",
    **{"usdRadiusClientMIB": usdRadiusClientMIB,
       "usdRadiusClientObjects": usdRadiusClientObjects,
       "usdRadiusGeneralClient": usdRadiusGeneralClient,
       "usdRadiusClientIdentifier": usdRadiusClientIdentifier,
       "usdRadiusClientAlgorithm": usdRadiusClientAlgorithm,
       "usdRadiusClientSourceAddress": usdRadiusClientSourceAddress,
       "usdRadiusClientUdpChecksum": usdRadiusClientUdpChecksum,
       "usdRadiusClientNasIdentifier": usdRadiusClientNasIdentifier,
       "usdRadiusClientDslPortType": usdRadiusClientDslPortType,
       "usdRadiusClientTunnelAccounting": usdRadiusClientTunnelAccounting,
       "usdRadiusClientAcctSessionIdFormat": usdRadiusClientAcctSessionIdFormat,
       "usdRadiusClientNasPortFormat": usdRadiusClientNasPortFormat,
       "usdRadiusClientCallingStationDelimiter": usdRadiusClientCallingStationDelimiter,
       "usdRadiusClientEthernetPortType": usdRadiusClientEthernetPortType,
       "usdRadiusClientIncludeIpAddrInAcctStart": usdRadiusClientIncludeIpAddrInAcctStart,
       "usdRadiusClientIncludeAcctSessionIdInAccessReq": usdRadiusClientIncludeAcctSessionIdInAccessReq,
       "usdRadiusClientRollover": usdRadiusClientRollover,
       "usdRadiusClientCallingStationIdFormat": usdRadiusClientCallingStationIdFormat,
       "usdRadiusClientNasIpAddrUse": usdRadiusClientNasIpAddrUse,
       "usdRadiusClientIncludeAcctTunnelConnectionInAccessReq": usdRadiusClientIncludeAcctTunnelConnectionInAccessReq,
       "usdRadiusClientIncludeCalledStationIdInAccessReq": usdRadiusClientIncludeCalledStationIdInAccessReq,
       "usdRadiusClientIncludeCallingStationIdInAccessReq": usdRadiusClientIncludeCallingStationIdInAccessReq,
       "usdRadiusClientIncludeConnectInfoInAccessReq": usdRadiusClientIncludeConnectInfoInAccessReq,
       "usdRadiusClientIncludeNasIdentifierInAccessReq": usdRadiusClientIncludeNasIdentifierInAccessReq,
       "usdRadiusClientIncludeNasPortInAccessReq": usdRadiusClientIncludeNasPortInAccessReq,
       "usdRadiusClientIncludeNasPortIdInAccessReq": usdRadiusClientIncludeNasPortIdInAccessReq,
       "usdRadiusClientIncludeNasPortTypeInAccessReq": usdRadiusClientIncludeNasPortTypeInAccessReq,
       "usdRadiusClientIncludePppoeDescriptionInAccessReq": usdRadiusClientIncludePppoeDescriptionInAccessReq,
       "usdRadiusClientIncludeTunnelClientAuthIdInAccessReq": usdRadiusClientIncludeTunnelClientAuthIdInAccessReq,
       "usdRadiusClientIncludeTunnelClientEndpointInAccessReq": usdRadiusClientIncludeTunnelClientEndpointInAccessReq,
       "usdRadiusClientIncludeTunnelMediumTypeInAccessReq": usdRadiusClientIncludeTunnelMediumTypeInAccessReq,
       "usdRadiusClientIncludeTunnelServerAttributesInAccessReq": usdRadiusClientIncludeTunnelServerAttributesInAccessReq,
       "usdRadiusClientIncludeTunnelServerAuthIdInAccessReq": usdRadiusClientIncludeTunnelServerAuthIdInAccessReq,
       "usdRadiusClientIncludeTunnelServerEndpointInAccessReq": usdRadiusClientIncludeTunnelServerEndpointInAccessReq,
       "usdRadiusClientIncludeTunnelTypeInAccessReq": usdRadiusClientIncludeTunnelTypeInAccessReq,
       "usdRadiusClientIncludeAcctTunnelConnectionInAcctStart": usdRadiusClientIncludeAcctTunnelConnectionInAcctStart,
       "usdRadiusClientIncludeCalledStationIdInAcctStart": usdRadiusClientIncludeCalledStationIdInAcctStart,
       "usdRadiusClientIncludeCallingStationIdInAcctStart": usdRadiusClientIncludeCallingStationIdInAcctStart,
       "usdRadiusClientIncludeClassInAcctStart": usdRadiusClientIncludeClassInAcctStart,
       "usdRadiusClientIncludeConnectInfoInAcctStart": usdRadiusClientIncludeConnectInfoInAcctStart,
       "usdRadiusClientIncludeEgressPolicyNameInAcctStart": usdRadiusClientIncludeEgressPolicyNameInAcctStart,
       "usdRadiusClientIncludeEventTimestampInAcctStart": usdRadiusClientIncludeEventTimestampInAcctStart,
       "usdRadiusClientIncludeFramedCompressionInAcctStart": usdRadiusClientIncludeFramedCompressionInAcctStart,
       "usdRadiusClientIncludeFramedIpNetmaskInAcctStart": usdRadiusClientIncludeFramedIpNetmaskInAcctStart,
       "usdRadiusClientIncludeIngressPolicyNameInAcctStart": usdRadiusClientIncludeIngressPolicyNameInAcctStart,
       "usdRadiusClientIncludeNasIdentifierInAcctStart": usdRadiusClientIncludeNasIdentifierInAcctStart,
       "usdRadiusClientIncludeNasPortInAcctStart": usdRadiusClientIncludeNasPortInAcctStart,
       "usdRadiusClientIncludeNasPortIdInAcctStart": usdRadiusClientIncludeNasPortIdInAcctStart,
       "usdRadiusClientIncludeNasPortTypeInAcctStart": usdRadiusClientIncludeNasPortTypeInAcctStart,
       "usdRadiusClientIncludePppoeDescriptionInAcctStart": usdRadiusClientIncludePppoeDescriptionInAcctStart,
       "usdRadiusClientIncludeTunnelAssignmentIdInAcctStart": usdRadiusClientIncludeTunnelAssignmentIdInAcctStart,
       "usdRadiusClientIncludeTunnelClientAuthIdInAcctStart": usdRadiusClientIncludeTunnelClientAuthIdInAcctStart,
       "usdRadiusClientIncludeTunnelClientEndpointInAcctStart": usdRadiusClientIncludeTunnelClientEndpointInAcctStart,
       "usdRadiusClientIncludeTunnelMediumTypeInAcctStart": usdRadiusClientIncludeTunnelMediumTypeInAcctStart,
       "usdRadiusClientIncludeTunnelPreferenceInAcctStart": usdRadiusClientIncludeTunnelPreferenceInAcctStart,
       "usdRadiusClientIncludeTunnelServerAttributesInAcctStart": usdRadiusClientIncludeTunnelServerAttributesInAcctStart,
       "usdRadiusClientIncludeTunnelServerAuthIdInAcctStart": usdRadiusClientIncludeTunnelServerAuthIdInAcctStart,
       "usdRadiusClientIncludeTunnelServerEndpointInAcctStart": usdRadiusClientIncludeTunnelServerEndpointInAcctStart,
       "usdRadiusClientIncludeTunnelTypeInAcctStart": usdRadiusClientIncludeTunnelTypeInAcctStart,
       "usdRadiusClientIncludeAcctTunnelConnectionInAcctStop": usdRadiusClientIncludeAcctTunnelConnectionInAcctStop,
       "usdRadiusClientIncludeCalledStationIdInAcctStop": usdRadiusClientIncludeCalledStationIdInAcctStop,
       "usdRadiusClientIncludeCallingStationIdInAcctStop": usdRadiusClientIncludeCallingStationIdInAcctStop,
       "usdRadiusClientIncludeClassInAcctStop": usdRadiusClientIncludeClassInAcctStop,
       "usdRadiusClientIncludeConnectInfoInAcctStop": usdRadiusClientIncludeConnectInfoInAcctStop,
       "usdRadiusClientIncludeEgressPolicyNameInAcctStop": usdRadiusClientIncludeEgressPolicyNameInAcctStop,
       "usdRadiusClientIncludeEventTimestampInAcctStop": usdRadiusClientIncludeEventTimestampInAcctStop,
       "usdRadiusClientIncludeFramedCompressionInAcctStop": usdRadiusClientIncludeFramedCompressionInAcctStop,
       "usdRadiusClientIncludeFramedIpNetmaskInAcctStop": usdRadiusClientIncludeFramedIpNetmaskInAcctStop,
       "usdRadiusClientIncludeIngressPolicyNameInAcctStop": usdRadiusClientIncludeIngressPolicyNameInAcctStop,
       "usdRadiusClientIncludeInputGigawordsInAcctStop": usdRadiusClientIncludeInputGigawordsInAcctStop,
       "usdRadiusClientIncludeNasIdentifierInAcctStop": usdRadiusClientIncludeNasIdentifierInAcctStop,
       "usdRadiusClientIncludeNasPortInAcctStop": usdRadiusClientIncludeNasPortInAcctStop,
       "usdRadiusClientIncludeNasPortIdInAcctStop": usdRadiusClientIncludeNasPortIdInAcctStop,
       "usdRadiusClientIncludeNasPortTypeInAcctStop": usdRadiusClientIncludeNasPortTypeInAcctStop,
       "usdRadiusClientIncludeOutputGigawordsInAcctStop": usdRadiusClientIncludeOutputGigawordsInAcctStop,
       "usdRadiusClientIncludePppoeDescriptionInAcctStop": usdRadiusClientIncludePppoeDescriptionInAcctStop,
       "usdRadiusClientIncludeTunnelAssignmentIdInAcctStop": usdRadiusClientIncludeTunnelAssignmentIdInAcctStop,
       "usdRadiusClientIncludeTunnelClientAuthIdInAcctStop": usdRadiusClientIncludeTunnelClientAuthIdInAcctStop,
       "usdRadiusClientIncludeTunnelClientEndpointInAcctStop": usdRadiusClientIncludeTunnelClientEndpointInAcctStop,
       "usdRadiusClientIncludeTunnelMediumTypeInAcctStop": usdRadiusClientIncludeTunnelMediumTypeInAcctStop,
       "usdRadiusClientIncludeTunnelPreferenceInAcctStop": usdRadiusClientIncludeTunnelPreferenceInAcctStop,
       "usdRadiusClientIncludeTunnelServerAttributesInAcctStop": usdRadiusClientIncludeTunnelServerAttributesInAcctStop,
       "usdRadiusClientIncludeTunnelServerAuthIdInAcctStop": usdRadiusClientIncludeTunnelServerAuthIdInAcctStop,
       "usdRadiusClientIncludeTunnelServerEndpointInAcctStop": usdRadiusClientIncludeTunnelServerEndpointInAcctStop,
       "usdRadiusClientIncludeTunnelTypeInAcctStop": usdRadiusClientIncludeTunnelTypeInAcctStop,
       "usdRadiusClientIncludeInputGigapktsInAcctStop": usdRadiusClientIncludeInputGigapktsInAcctStop,
       "usdRadiusClientIncludeOutputGigapktsInAcctStop": usdRadiusClientIncludeOutputGigapktsInAcctStop,
       "usdRadiusClientIgnoreFramedIpNetmask": usdRadiusClientIgnoreFramedIpNetmask,
       "usdRadiusAuthClient": usdRadiusAuthClient,
       "usdRadiusAuthClientInvalidServerAddresses": usdRadiusAuthClientInvalidServerAddresses,
       "usdRadiusAuthClientServerTable": usdRadiusAuthClientServerTable,
       "usdRadiusAuthClientServerEntry": usdRadiusAuthClientServerEntry,
       "usdRadiusAuthClientServerAddress": usdRadiusAuthClientServerAddress,
       "usdRadiusAuthClientServerPortNumber": usdRadiusAuthClientServerPortNumber,
       "usdRadiusAuthClientRoundTripTime": usdRadiusAuthClientRoundTripTime,
       "usdRadiusAuthClientAccessRequests": usdRadiusAuthClientAccessRequests,
       "usdRadiusAuthClientAccessRetransmissions": usdRadiusAuthClientAccessRetransmissions,
       "usdRadiusAuthClientAccessAccepts": usdRadiusAuthClientAccessAccepts,
       "usdRadiusAuthClientAccessRejects": usdRadiusAuthClientAccessRejects,
       "usdRadiusAuthClientAccessChallenges": usdRadiusAuthClientAccessChallenges,
       "usdRadiusAuthClientMalformedAccessResponses": usdRadiusAuthClientMalformedAccessResponses,
       "usdRadiusAuthClientBadAuthenticators": usdRadiusAuthClientBadAuthenticators,
       "usdRadiusAuthClientPendingRequests": usdRadiusAuthClientPendingRequests,
       "usdRadiusAuthClientTimeouts": usdRadiusAuthClientTimeouts,
       "usdRadiusAuthClientUnknownTypes": usdRadiusAuthClientUnknownTypes,
       "usdRadiusAuthClientPacketsDropped": usdRadiusAuthClientPacketsDropped,
       "usdRadiusAuthClientCfgServerTable": usdRadiusAuthClientCfgServerTable,
       "usdRadiusAuthClientCfgServerEntry": usdRadiusAuthClientCfgServerEntry,
       "usdRadiusAuthClientCfgServerAddress": usdRadiusAuthClientCfgServerAddress,
       "usdRadiusAuthClientCfgServerPortNumber": usdRadiusAuthClientCfgServerPortNumber,
       "usdRadiusAuthClientCfgKey": usdRadiusAuthClientCfgKey,
       "usdRadiusAuthClientCfgTimeoutInterval": usdRadiusAuthClientCfgTimeoutInterval,
       "usdRadiusAuthClientCfgRetries": usdRadiusAuthClientCfgRetries,
       "usdRadiusAuthClientCfgMaxPendingRequests": usdRadiusAuthClientCfgMaxPendingRequests,
       "usdRadiusAuthClientCfgRowStatus": usdRadiusAuthClientCfgRowStatus,
       "usdRadiusAuthClientCfgPrecedence": usdRadiusAuthClientCfgPrecedence,
       "usdRadiusAuthClientCfgDeadTime": usdRadiusAuthClientCfgDeadTime,
       "usdRadiusAcctClient": usdRadiusAcctClient,
       "usdRadiusAcctClientInvalidServerAddresses": usdRadiusAcctClientInvalidServerAddresses,
       "usdRadiusAcctClientServerTable": usdRadiusAcctClientServerTable,
       "usdRadiusAcctClientServerEntry": usdRadiusAcctClientServerEntry,
       "usdRadiusAcctClientServerAddress": usdRadiusAcctClientServerAddress,
       "usdRadiusAcctClientServerPortNumber": usdRadiusAcctClientServerPortNumber,
       "usdRadiusAcctClientRoundTripTime": usdRadiusAcctClientRoundTripTime,
       "usdRadiusAcctClientRequests": usdRadiusAcctClientRequests,
       "usdRadiusAcctClientRetransmissions": usdRadiusAcctClientRetransmissions,
       "usdRadiusAcctClientResponses": usdRadiusAcctClientResponses,
       "usdRadiusAcctClientMalformedResponses": usdRadiusAcctClientMalformedResponses,
       "usdRadiusAcctClientBadAuthenticators": usdRadiusAcctClientBadAuthenticators,
       "usdRadiusAcctClientPendingRequests": usdRadiusAcctClientPendingRequests,
       "usdRadiusAcctClientTimeouts": usdRadiusAcctClientTimeouts,
       "usdRadiusAcctClientUnknownTypes": usdRadiusAcctClientUnknownTypes,
       "usdRadiusAcctClientPacketsDropped": usdRadiusAcctClientPacketsDropped,
       "usdRadiusAcctClientCfgServerTable": usdRadiusAcctClientCfgServerTable,
       "usdRadiusAcctClientCfgServerEntry": usdRadiusAcctClientCfgServerEntry,
       "usdRadiusAcctClientCfgServerAddress": usdRadiusAcctClientCfgServerAddress,
       "usdRadiusAcctClientCfgServerPortNumber": usdRadiusAcctClientCfgServerPortNumber,
       "usdRadiusAcctClientCfgKey": usdRadiusAcctClientCfgKey,
       "usdRadiusAcctClientCfgTimeoutInterval": usdRadiusAcctClientCfgTimeoutInterval,
       "usdRadiusAcctClientCfgRetries": usdRadiusAcctClientCfgRetries,
       "usdRadiusAcctClientCfgMaxPendingRequests": usdRadiusAcctClientCfgMaxPendingRequests,
       "usdRadiusAcctClientCfgRowStatus": usdRadiusAcctClientCfgRowStatus,
       "usdRadiusAcctClientCfgPrecedence": usdRadiusAcctClientCfgPrecedence,
       "usdRadiusAcctClientCfgDeadTime": usdRadiusAcctClientCfgDeadTime,
       "usdRadiusClientMIBConformance": usdRadiusClientMIBConformance,
       "usdRadiusClientMIBCompliances": usdRadiusClientMIBCompliances,
       "usdRadiusAuthClientCompliance": usdRadiusAuthClientCompliance,
       "usdRadiusAcctClientCompliance": usdRadiusAcctClientCompliance,
       "usdRadiusAuthClientCompliance2": usdRadiusAuthClientCompliance2,
       "usdRadiusAcctClientCompliance2": usdRadiusAcctClientCompliance2,
       "usdRadiusClientCompliance": usdRadiusClientCompliance,
       "usdRadiusClientCompliance2": usdRadiusClientCompliance2,
       "usdRadiusClientCompliance3": usdRadiusClientCompliance3,
       "usdRadiusClientCompliance4": usdRadiusClientCompliance4,
       "usdRadiusClientCompliance5": usdRadiusClientCompliance5,
       "usdRadiusClientMIBGroups": usdRadiusClientMIBGroups,
       "usdRadiusGeneralClientGroup": usdRadiusGeneralClientGroup,
       "usdRadiusAuthClientGroup": usdRadiusAuthClientGroup,
       "usdRadiusAcctClientGroup": usdRadiusAcctClientGroup,
       "usdRadiusGeneralClientGroup2": usdRadiusGeneralClientGroup2,
       "usdRadiusBasicClientGroup": usdRadiusBasicClientGroup,
       "usdRadiusBrasClientGroup": usdRadiusBrasClientGroup,
       "usdRadiusTunnelClientGroup": usdRadiusTunnelClientGroup,
       "usdRadiusBrasClientGroup2": usdRadiusBrasClientGroup2,
       "usdRadiusBasicClientGroup2": usdRadiusBasicClientGroup2,
       "usdRadiusBrasClientGroup3": usdRadiusBrasClientGroup3,
       "usdRadiusBrasClientGroup4": usdRadiusBrasClientGroup4,
       "usdRadiusBrasClientGroup5": usdRadiusBrasClientGroup5}
)
