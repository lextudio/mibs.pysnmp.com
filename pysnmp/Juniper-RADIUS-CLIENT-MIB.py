# SNMP MIB module (Juniper-RADIUS-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-RADIUS-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:09 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniRadiusClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19)
)
juniRadiusClientMIB.setRevisions(
        ("2009-02-26 16:41",
         "2008-06-18 10:10",
         "2008-06-11 06:15",
         "2007-12-14 15:00",
         "2007-09-18 18:22",
         "2007-09-16 22:00",
         "2007-04-10 01:03",
         "2006-02-17 22:00",
         "2006-01-12 22:00",
         "2005-09-30 14:55",
         "2005-01-14 15:15",
         "2004-12-06 02:32",
         "2004-12-03 22:12",
         "2004-09-09 19:45",
         "2003-12-15 16:36",
         "2003-03-10 19:33",
         "2003-01-27 18:33",
         "2002-11-21 19:45",
         "2002-05-13 17:54",
         "2001-10-16 19:54",
         "2001-09-06 21:08",
         "2001-03-22 15:20",
         "2000-12-19 16:40",
         "2000-05-05 19:44",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniRadiusClientRemoterCircuitIdFormatComponents(Integer32, TextualConvention):
    status = "current"
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
        *(("agentCircuitId", 1),
          ("agentRemoteId", 2),
          ("dsl-format-1", 4),
          ("nasIdentifier", 3))
    )



# MIB Managed Objects in the order of their OIDs

_JuniRadiusClientObjects_ObjectIdentity = ObjectIdentity
juniRadiusClientObjects = _JuniRadiusClientObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1)
)
_JuniRadiusGeneralClient_ObjectIdentity = ObjectIdentity
juniRadiusGeneralClient = _JuniRadiusGeneralClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1)
)
_JuniRadiusClientIdentifier_Type = DisplayString
_JuniRadiusClientIdentifier_Object = MibScalar
juniRadiusClientIdentifier = _JuniRadiusClientIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 1),
    _JuniRadiusClientIdentifier_Type()
)
juniRadiusClientIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusClientIdentifier.setStatus("current")


class _JuniRadiusClientAlgorithm_Type(Integer32):
    """Custom type juniRadiusClientAlgorithm based on Integer32"""
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


_JuniRadiusClientAlgorithm_Type.__name__ = "Integer32"
_JuniRadiusClientAlgorithm_Object = MibScalar
juniRadiusClientAlgorithm = _JuniRadiusClientAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 2),
    _JuniRadiusClientAlgorithm_Type()
)
juniRadiusClientAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientAlgorithm.setStatus("current")


class _JuniRadiusClientSourceAddress_Type(IpAddress):
    """Custom type juniRadiusClientSourceAddress based on IpAddress"""
    defaultValue = 0


_JuniRadiusClientSourceAddress_Object = MibScalar
juniRadiusClientSourceAddress = _JuniRadiusClientSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 3),
    _JuniRadiusClientSourceAddress_Type()
)
juniRadiusClientSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientSourceAddress.setStatus("current")


class _JuniRadiusClientUdpChecksum_Type(TruthValue):
    """Custom type juniRadiusClientUdpChecksum based on TruthValue"""


_JuniRadiusClientUdpChecksum_Object = MibScalar
juniRadiusClientUdpChecksum = _JuniRadiusClientUdpChecksum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 4),
    _JuniRadiusClientUdpChecksum_Type()
)
juniRadiusClientUdpChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientUdpChecksum.setStatus("current")


class _JuniRadiusClientNasIdentifier_Type(DisplayString):
    """Custom type juniRadiusClientNasIdentifier based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniRadiusClientNasIdentifier_Type.__name__ = "DisplayString"
_JuniRadiusClientNasIdentifier_Object = MibScalar
juniRadiusClientNasIdentifier = _JuniRadiusClientNasIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 5),
    _JuniRadiusClientNasIdentifier_Type()
)
juniRadiusClientNasIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasIdentifier.setStatus("current")


class _JuniRadiusClientDslPortType_Type(Integer32):
    """Custom type juniRadiusClientDslPortType based on Integer32"""
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


_JuniRadiusClientDslPortType_Type.__name__ = "Integer32"
_JuniRadiusClientDslPortType_Object = MibScalar
juniRadiusClientDslPortType = _JuniRadiusClientDslPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 6),
    _JuniRadiusClientDslPortType_Type()
)
juniRadiusClientDslPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientDslPortType.setStatus("current")


class _JuniRadiusClientTunnelAccounting_Type(TruthValue):
    """Custom type juniRadiusClientTunnelAccounting based on TruthValue"""


_JuniRadiusClientTunnelAccounting_Object = MibScalar
juniRadiusClientTunnelAccounting = _JuniRadiusClientTunnelAccounting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 7),
    _JuniRadiusClientTunnelAccounting_Type()
)
juniRadiusClientTunnelAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientTunnelAccounting.setStatus("current")


class _JuniRadiusClientAcctSessionIdFormat_Type(Integer32):
    """Custom type juniRadiusClientAcctSessionIdFormat based on Integer32"""
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


_JuniRadiusClientAcctSessionIdFormat_Type.__name__ = "Integer32"
_JuniRadiusClientAcctSessionIdFormat_Object = MibScalar
juniRadiusClientAcctSessionIdFormat = _JuniRadiusClientAcctSessionIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 8),
    _JuniRadiusClientAcctSessionIdFormat_Type()
)
juniRadiusClientAcctSessionIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientAcctSessionIdFormat.setStatus("current")


class _JuniRadiusClientNasPortFormat_Type(Integer32):
    """Custom type juniRadiusClientNasPortFormat based on Integer32"""
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


_JuniRadiusClientNasPortFormat_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFormat_Object = MibScalar
juniRadiusClientNasPortFormat = _JuniRadiusClientNasPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 9),
    _JuniRadiusClientNasPortFormat_Type()
)
juniRadiusClientNasPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFormat.setStatus("current")


class _JuniRadiusClientCallingStationDelimiter_Type(DisplayString):
    """Custom type juniRadiusClientCallingStationDelimiter based on DisplayString"""
    defaultValue = OctetString("#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_JuniRadiusClientCallingStationDelimiter_Type.__name__ = "DisplayString"
_JuniRadiusClientCallingStationDelimiter_Object = MibScalar
juniRadiusClientCallingStationDelimiter = _JuniRadiusClientCallingStationDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 10),
    _JuniRadiusClientCallingStationDelimiter_Type()
)
juniRadiusClientCallingStationDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientCallingStationDelimiter.setStatus("current")


class _JuniRadiusClientEthernetPortType_Type(Integer32):
    """Custom type juniRadiusClientEthernetPortType based on Integer32"""
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


_JuniRadiusClientEthernetPortType_Type.__name__ = "Integer32"
_JuniRadiusClientEthernetPortType_Object = MibScalar
juniRadiusClientEthernetPortType = _JuniRadiusClientEthernetPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 11),
    _JuniRadiusClientEthernetPortType_Type()
)
juniRadiusClientEthernetPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientEthernetPortType.setStatus("current")


class _JuniRadiusClientIncludeIpAddrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpAddrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIpAddrInAcctStart_Object = MibScalar
juniRadiusClientIncludeIpAddrInAcctStart = _JuniRadiusClientIncludeIpAddrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 12),
    _JuniRadiusClientIncludeIpAddrInAcctStart_Type()
)
juniRadiusClientIncludeIpAddrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpAddrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeAcctSessionIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctSessionIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeAcctSessionIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeAcctSessionIdInAccessReq = _JuniRadiusClientIncludeAcctSessionIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 13),
    _JuniRadiusClientIncludeAcctSessionIdInAccessReq_Type()
)
juniRadiusClientIncludeAcctSessionIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctSessionIdInAccessReq.setStatus("current")


class _JuniRadiusClientRollover_Type(TruthValue):
    """Custom type juniRadiusClientRollover based on TruthValue"""


_JuniRadiusClientRollover_Object = MibScalar
juniRadiusClientRollover = _JuniRadiusClientRollover_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 14),
    _JuniRadiusClientRollover_Type()
)
juniRadiusClientRollover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientRollover.setStatus("current")


class _JuniRadiusClientCallingStationIdFormat_Type(Integer32):
    """Custom type juniRadiusClientCallingStationIdFormat based on Integer32"""
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
        *(("delimited", 0),
          ("fixedFormat", 1),
          ("fixedFormatAdapterEmbedded", 2),
          ("fixedFormatAdapterEmbeddedStacked", 5),
          ("fixedFormatAdapterNewField", 3),
          ("fixedFormatAdapterNewFieldStacked", 6),
          ("fixedFormatStacked", 4))
    )


_JuniRadiusClientCallingStationIdFormat_Type.__name__ = "Integer32"
_JuniRadiusClientCallingStationIdFormat_Object = MibScalar
juniRadiusClientCallingStationIdFormat = _JuniRadiusClientCallingStationIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 15),
    _JuniRadiusClientCallingStationIdFormat_Type()
)
juniRadiusClientCallingStationIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientCallingStationIdFormat.setStatus("current")


class _JuniRadiusClientNasIpAddrUse_Type(Integer32):
    """Custom type juniRadiusClientNasIpAddrUse based on Integer32"""
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


_JuniRadiusClientNasIpAddrUse_Type.__name__ = "Integer32"
_JuniRadiusClientNasIpAddrUse_Object = MibScalar
juniRadiusClientNasIpAddrUse = _JuniRadiusClientNasIpAddrUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 16),
    _JuniRadiusClientNasIpAddrUse_Type()
)
juniRadiusClientNasIpAddrUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasIpAddrUse.setStatus("current")


class _JuniRadiusClientIncludeAcctTunnelConnectionInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctTunnelConnectionInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeAcctTunnelConnectionInAccessReq_Object = MibScalar
juniRadiusClientIncludeAcctTunnelConnectionInAccessReq = _JuniRadiusClientIncludeAcctTunnelConnectionInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 17),
    _JuniRadiusClientIncludeAcctTunnelConnectionInAccessReq_Type()
)
juniRadiusClientIncludeAcctTunnelConnectionInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctTunnelConnectionInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeCalledStationIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeCalledStationIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeCalledStationIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeCalledStationIdInAccessReq = _JuniRadiusClientIncludeCalledStationIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 18),
    _JuniRadiusClientIncludeCalledStationIdInAccessReq_Type()
)
juniRadiusClientIncludeCalledStationIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeCalledStationIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeCallingStationIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeCallingStationIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeCallingStationIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeCallingStationIdInAccessReq = _JuniRadiusClientIncludeCallingStationIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 19),
    _JuniRadiusClientIncludeCallingStationIdInAccessReq_Type()
)
juniRadiusClientIncludeCallingStationIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeCallingStationIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeConnectInfoInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeConnectInfoInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeConnectInfoInAccessReq_Object = MibScalar
juniRadiusClientIncludeConnectInfoInAccessReq = _JuniRadiusClientIncludeConnectInfoInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 20),
    _JuniRadiusClientIncludeConnectInfoInAccessReq_Type()
)
juniRadiusClientIncludeConnectInfoInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeConnectInfoInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeNasIdentifierInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasIdentifierInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeNasIdentifierInAccessReq_Object = MibScalar
juniRadiusClientIncludeNasIdentifierInAccessReq = _JuniRadiusClientIncludeNasIdentifierInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 21),
    _JuniRadiusClientIncludeNasIdentifierInAccessReq_Type()
)
juniRadiusClientIncludeNasIdentifierInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasIdentifierInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeNasPortInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeNasPortInAccessReq_Object = MibScalar
juniRadiusClientIncludeNasPortInAccessReq = _JuniRadiusClientIncludeNasPortInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 22),
    _JuniRadiusClientIncludeNasPortInAccessReq_Type()
)
juniRadiusClientIncludeNasPortInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeNasPortIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeNasPortIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeNasPortIdInAccessReq = _JuniRadiusClientIncludeNasPortIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 23),
    _JuniRadiusClientIncludeNasPortIdInAccessReq_Type()
)
juniRadiusClientIncludeNasPortIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeNasPortTypeInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortTypeInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeNasPortTypeInAccessReq_Object = MibScalar
juniRadiusClientIncludeNasPortTypeInAccessReq = _JuniRadiusClientIncludeNasPortTypeInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 24),
    _JuniRadiusClientIncludeNasPortTypeInAccessReq_Type()
)
juniRadiusClientIncludeNasPortTypeInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortTypeInAccessReq.setStatus("current")


class _JuniRadiusClientIncludePppoeDescriptionInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludePppoeDescriptionInAccessReq based on TruthValue"""


_JuniRadiusClientIncludePppoeDescriptionInAccessReq_Object = MibScalar
juniRadiusClientIncludePppoeDescriptionInAccessReq = _JuniRadiusClientIncludePppoeDescriptionInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 25),
    _JuniRadiusClientIncludePppoeDescriptionInAccessReq_Type()
)
juniRadiusClientIncludePppoeDescriptionInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludePppoeDescriptionInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelClientAuthIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelClientAuthIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelClientAuthIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelClientAuthIdInAccessReq = _JuniRadiusClientIncludeTunnelClientAuthIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 26),
    _JuniRadiusClientIncludeTunnelClientAuthIdInAccessReq_Type()
)
juniRadiusClientIncludeTunnelClientAuthIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelClientAuthIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelClientEndpointInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelClientEndpointInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelClientEndpointInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelClientEndpointInAccessReq = _JuniRadiusClientIncludeTunnelClientEndpointInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 27),
    _JuniRadiusClientIncludeTunnelClientEndpointInAccessReq_Type()
)
juniRadiusClientIncludeTunnelClientEndpointInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelClientEndpointInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelMediumTypeInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelMediumTypeInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelMediumTypeInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelMediumTypeInAccessReq = _JuniRadiusClientIncludeTunnelMediumTypeInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 28),
    _JuniRadiusClientIncludeTunnelMediumTypeInAccessReq_Type()
)
juniRadiusClientIncludeTunnelMediumTypeInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelMediumTypeInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerAttributesInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerAttributesInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerAttributesInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelServerAttributesInAccessReq = _JuniRadiusClientIncludeTunnelServerAttributesInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 29),
    _JuniRadiusClientIncludeTunnelServerAttributesInAccessReq_Type()
)
juniRadiusClientIncludeTunnelServerAttributesInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerAttributesInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerAuthIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerAuthIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerAuthIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelServerAuthIdInAccessReq = _JuniRadiusClientIncludeTunnelServerAuthIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 30),
    _JuniRadiusClientIncludeTunnelServerAuthIdInAccessReq_Type()
)
juniRadiusClientIncludeTunnelServerAuthIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerAuthIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerEndpointInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerEndpointInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerEndpointInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelServerEndpointInAccessReq = _JuniRadiusClientIncludeTunnelServerEndpointInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 31),
    _JuniRadiusClientIncludeTunnelServerEndpointInAccessReq_Type()
)
juniRadiusClientIncludeTunnelServerEndpointInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerEndpointInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelTypeInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelTypeInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelTypeInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelTypeInAccessReq = _JuniRadiusClientIncludeTunnelTypeInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 32),
    _JuniRadiusClientIncludeTunnelTypeInAccessReq_Type()
)
juniRadiusClientIncludeTunnelTypeInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelTypeInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeAcctTunnelConnectionInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctTunnelConnectionInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeAcctTunnelConnectionInAcctStart_Object = MibScalar
juniRadiusClientIncludeAcctTunnelConnectionInAcctStart = _JuniRadiusClientIncludeAcctTunnelConnectionInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 33),
    _JuniRadiusClientIncludeAcctTunnelConnectionInAcctStart_Type()
)
juniRadiusClientIncludeAcctTunnelConnectionInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctTunnelConnectionInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeCalledStationIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeCalledStationIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeCalledStationIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeCalledStationIdInAcctStart = _JuniRadiusClientIncludeCalledStationIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 34),
    _JuniRadiusClientIncludeCalledStationIdInAcctStart_Type()
)
juniRadiusClientIncludeCalledStationIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeCalledStationIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeCallingStationIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeCallingStationIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeCallingStationIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeCallingStationIdInAcctStart = _JuniRadiusClientIncludeCallingStationIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 35),
    _JuniRadiusClientIncludeCallingStationIdInAcctStart_Type()
)
juniRadiusClientIncludeCallingStationIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeCallingStationIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeClassInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeClassInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeClassInAcctStart_Object = MibScalar
juniRadiusClientIncludeClassInAcctStart = _JuniRadiusClientIncludeClassInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 36),
    _JuniRadiusClientIncludeClassInAcctStart_Type()
)
juniRadiusClientIncludeClassInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeClassInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeConnectInfoInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeConnectInfoInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeConnectInfoInAcctStart_Object = MibScalar
juniRadiusClientIncludeConnectInfoInAcctStart = _JuniRadiusClientIncludeConnectInfoInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 37),
    _JuniRadiusClientIncludeConnectInfoInAcctStart_Type()
)
juniRadiusClientIncludeConnectInfoInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeConnectInfoInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeEgressPolicyNameInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeEgressPolicyNameInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeEgressPolicyNameInAcctStart_Object = MibScalar
juniRadiusClientIncludeEgressPolicyNameInAcctStart = _JuniRadiusClientIncludeEgressPolicyNameInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 38),
    _JuniRadiusClientIncludeEgressPolicyNameInAcctStart_Type()
)
juniRadiusClientIncludeEgressPolicyNameInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeEgressPolicyNameInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeEventTimestampInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeEventTimestampInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeEventTimestampInAcctStart_Object = MibScalar
juniRadiusClientIncludeEventTimestampInAcctStart = _JuniRadiusClientIncludeEventTimestampInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 39),
    _JuniRadiusClientIncludeEventTimestampInAcctStart_Type()
)
juniRadiusClientIncludeEventTimestampInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeEventTimestampInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeFramedCompressionInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedCompressionInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeFramedCompressionInAcctStart_Object = MibScalar
juniRadiusClientIncludeFramedCompressionInAcctStart = _JuniRadiusClientIncludeFramedCompressionInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 40),
    _JuniRadiusClientIncludeFramedCompressionInAcctStart_Type()
)
juniRadiusClientIncludeFramedCompressionInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedCompressionInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeFramedIpNetmaskInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedIpNetmaskInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeFramedIpNetmaskInAcctStart_Object = MibScalar
juniRadiusClientIncludeFramedIpNetmaskInAcctStart = _JuniRadiusClientIncludeFramedIpNetmaskInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 41),
    _JuniRadiusClientIncludeFramedIpNetmaskInAcctStart_Type()
)
juniRadiusClientIncludeFramedIpNetmaskInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedIpNetmaskInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeIngressPolicyNameInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIngressPolicyNameInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIngressPolicyNameInAcctStart_Object = MibScalar
juniRadiusClientIncludeIngressPolicyNameInAcctStart = _JuniRadiusClientIncludeIngressPolicyNameInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 42),
    _JuniRadiusClientIncludeIngressPolicyNameInAcctStart_Type()
)
juniRadiusClientIncludeIngressPolicyNameInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIngressPolicyNameInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeNasIdentifierInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasIdentifierInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeNasIdentifierInAcctStart_Object = MibScalar
juniRadiusClientIncludeNasIdentifierInAcctStart = _JuniRadiusClientIncludeNasIdentifierInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 43),
    _JuniRadiusClientIncludeNasIdentifierInAcctStart_Type()
)
juniRadiusClientIncludeNasIdentifierInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasIdentifierInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeNasPortInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeNasPortInAcctStart_Object = MibScalar
juniRadiusClientIncludeNasPortInAcctStart = _JuniRadiusClientIncludeNasPortInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 44),
    _JuniRadiusClientIncludeNasPortInAcctStart_Type()
)
juniRadiusClientIncludeNasPortInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeNasPortIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeNasPortIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeNasPortIdInAcctStart = _JuniRadiusClientIncludeNasPortIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 45),
    _JuniRadiusClientIncludeNasPortIdInAcctStart_Type()
)
juniRadiusClientIncludeNasPortIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeNasPortTypeInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortTypeInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeNasPortTypeInAcctStart_Object = MibScalar
juniRadiusClientIncludeNasPortTypeInAcctStart = _JuniRadiusClientIncludeNasPortTypeInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 46),
    _JuniRadiusClientIncludeNasPortTypeInAcctStart_Type()
)
juniRadiusClientIncludeNasPortTypeInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortTypeInAcctStart.setStatus("current")


class _JuniRadiusClientIncludePppoeDescriptionInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludePppoeDescriptionInAcctStart based on TruthValue"""


_JuniRadiusClientIncludePppoeDescriptionInAcctStart_Object = MibScalar
juniRadiusClientIncludePppoeDescriptionInAcctStart = _JuniRadiusClientIncludePppoeDescriptionInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 47),
    _JuniRadiusClientIncludePppoeDescriptionInAcctStart_Type()
)
juniRadiusClientIncludePppoeDescriptionInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludePppoeDescriptionInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelAssignmentIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelAssignmentIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelAssignmentIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelAssignmentIdInAcctStart = _JuniRadiusClientIncludeTunnelAssignmentIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 48),
    _JuniRadiusClientIncludeTunnelAssignmentIdInAcctStart_Type()
)
juniRadiusClientIncludeTunnelAssignmentIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelAssignmentIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelClientAuthIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelClientAuthIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelClientAuthIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelClientAuthIdInAcctStart = _JuniRadiusClientIncludeTunnelClientAuthIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 49),
    _JuniRadiusClientIncludeTunnelClientAuthIdInAcctStart_Type()
)
juniRadiusClientIncludeTunnelClientAuthIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelClientAuthIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelClientEndpointInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelClientEndpointInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelClientEndpointInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelClientEndpointInAcctStart = _JuniRadiusClientIncludeTunnelClientEndpointInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 50),
    _JuniRadiusClientIncludeTunnelClientEndpointInAcctStart_Type()
)
juniRadiusClientIncludeTunnelClientEndpointInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelClientEndpointInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelMediumTypeInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelMediumTypeInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelMediumTypeInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelMediumTypeInAcctStart = _JuniRadiusClientIncludeTunnelMediumTypeInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 51),
    _JuniRadiusClientIncludeTunnelMediumTypeInAcctStart_Type()
)
juniRadiusClientIncludeTunnelMediumTypeInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelMediumTypeInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelPreferenceInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelPreferenceInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelPreferenceInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelPreferenceInAcctStart = _JuniRadiusClientIncludeTunnelPreferenceInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 52),
    _JuniRadiusClientIncludeTunnelPreferenceInAcctStart_Type()
)
juniRadiusClientIncludeTunnelPreferenceInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelPreferenceInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerAttributesInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerAttributesInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerAttributesInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelServerAttributesInAcctStart = _JuniRadiusClientIncludeTunnelServerAttributesInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 53),
    _JuniRadiusClientIncludeTunnelServerAttributesInAcctStart_Type()
)
juniRadiusClientIncludeTunnelServerAttributesInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerAttributesInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerAuthIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerAuthIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerAuthIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelServerAuthIdInAcctStart = _JuniRadiusClientIncludeTunnelServerAuthIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 54),
    _JuniRadiusClientIncludeTunnelServerAuthIdInAcctStart_Type()
)
juniRadiusClientIncludeTunnelServerAuthIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerAuthIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerEndpointInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerEndpointInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerEndpointInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelServerEndpointInAcctStart = _JuniRadiusClientIncludeTunnelServerEndpointInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 55),
    _JuniRadiusClientIncludeTunnelServerEndpointInAcctStart_Type()
)
juniRadiusClientIncludeTunnelServerEndpointInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerEndpointInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelTypeInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelTypeInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelTypeInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelTypeInAcctStart = _JuniRadiusClientIncludeTunnelTypeInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 56),
    _JuniRadiusClientIncludeTunnelTypeInAcctStart_Type()
)
juniRadiusClientIncludeTunnelTypeInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelTypeInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeAcctTunnelConnectionInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctTunnelConnectionInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeAcctTunnelConnectionInAcctStop_Object = MibScalar
juniRadiusClientIncludeAcctTunnelConnectionInAcctStop = _JuniRadiusClientIncludeAcctTunnelConnectionInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 57),
    _JuniRadiusClientIncludeAcctTunnelConnectionInAcctStop_Type()
)
juniRadiusClientIncludeAcctTunnelConnectionInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctTunnelConnectionInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeCalledStationIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeCalledStationIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeCalledStationIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeCalledStationIdInAcctStop = _JuniRadiusClientIncludeCalledStationIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 59),
    _JuniRadiusClientIncludeCalledStationIdInAcctStop_Type()
)
juniRadiusClientIncludeCalledStationIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeCalledStationIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeCallingStationIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeCallingStationIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeCallingStationIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeCallingStationIdInAcctStop = _JuniRadiusClientIncludeCallingStationIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 60),
    _JuniRadiusClientIncludeCallingStationIdInAcctStop_Type()
)
juniRadiusClientIncludeCallingStationIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeCallingStationIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeClassInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeClassInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeClassInAcctStop_Object = MibScalar
juniRadiusClientIncludeClassInAcctStop = _JuniRadiusClientIncludeClassInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 61),
    _JuniRadiusClientIncludeClassInAcctStop_Type()
)
juniRadiusClientIncludeClassInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeClassInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeConnectInfoInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeConnectInfoInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeConnectInfoInAcctStop_Object = MibScalar
juniRadiusClientIncludeConnectInfoInAcctStop = _JuniRadiusClientIncludeConnectInfoInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 62),
    _JuniRadiusClientIncludeConnectInfoInAcctStop_Type()
)
juniRadiusClientIncludeConnectInfoInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeConnectInfoInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeEgressPolicyNameInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeEgressPolicyNameInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeEgressPolicyNameInAcctStop_Object = MibScalar
juniRadiusClientIncludeEgressPolicyNameInAcctStop = _JuniRadiusClientIncludeEgressPolicyNameInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 63),
    _JuniRadiusClientIncludeEgressPolicyNameInAcctStop_Type()
)
juniRadiusClientIncludeEgressPolicyNameInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeEgressPolicyNameInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeEventTimestampInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeEventTimestampInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeEventTimestampInAcctStop_Object = MibScalar
juniRadiusClientIncludeEventTimestampInAcctStop = _JuniRadiusClientIncludeEventTimestampInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 64),
    _JuniRadiusClientIncludeEventTimestampInAcctStop_Type()
)
juniRadiusClientIncludeEventTimestampInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeEventTimestampInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeFramedCompressionInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedCompressionInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeFramedCompressionInAcctStop_Object = MibScalar
juniRadiusClientIncludeFramedCompressionInAcctStop = _JuniRadiusClientIncludeFramedCompressionInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 65),
    _JuniRadiusClientIncludeFramedCompressionInAcctStop_Type()
)
juniRadiusClientIncludeFramedCompressionInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedCompressionInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeFramedIpNetmaskInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedIpNetmaskInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeFramedIpNetmaskInAcctStop_Object = MibScalar
juniRadiusClientIncludeFramedIpNetmaskInAcctStop = _JuniRadiusClientIncludeFramedIpNetmaskInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 66),
    _JuniRadiusClientIncludeFramedIpNetmaskInAcctStop_Type()
)
juniRadiusClientIncludeFramedIpNetmaskInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedIpNetmaskInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIngressPolicyNameInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIngressPolicyNameInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIngressPolicyNameInAcctStop_Object = MibScalar
juniRadiusClientIncludeIngressPolicyNameInAcctStop = _JuniRadiusClientIncludeIngressPolicyNameInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 67),
    _JuniRadiusClientIncludeIngressPolicyNameInAcctStop_Type()
)
juniRadiusClientIncludeIngressPolicyNameInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIngressPolicyNameInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeInputGigawordsInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeInputGigawordsInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeInputGigawordsInAcctStop_Object = MibScalar
juniRadiusClientIncludeInputGigawordsInAcctStop = _JuniRadiusClientIncludeInputGigawordsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 68),
    _JuniRadiusClientIncludeInputGigawordsInAcctStop_Type()
)
juniRadiusClientIncludeInputGigawordsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeInputGigawordsInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeNasIdentifierInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasIdentifierInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeNasIdentifierInAcctStop_Object = MibScalar
juniRadiusClientIncludeNasIdentifierInAcctStop = _JuniRadiusClientIncludeNasIdentifierInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 69),
    _JuniRadiusClientIncludeNasIdentifierInAcctStop_Type()
)
juniRadiusClientIncludeNasIdentifierInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasIdentifierInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeNasPortInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeNasPortInAcctStop_Object = MibScalar
juniRadiusClientIncludeNasPortInAcctStop = _JuniRadiusClientIncludeNasPortInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 70),
    _JuniRadiusClientIncludeNasPortInAcctStop_Type()
)
juniRadiusClientIncludeNasPortInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeNasPortIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeNasPortIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeNasPortIdInAcctStop = _JuniRadiusClientIncludeNasPortIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 71),
    _JuniRadiusClientIncludeNasPortIdInAcctStop_Type()
)
juniRadiusClientIncludeNasPortIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeNasPortTypeInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasPortTypeInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeNasPortTypeInAcctStop_Object = MibScalar
juniRadiusClientIncludeNasPortTypeInAcctStop = _JuniRadiusClientIncludeNasPortTypeInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 72),
    _JuniRadiusClientIncludeNasPortTypeInAcctStop_Type()
)
juniRadiusClientIncludeNasPortTypeInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasPortTypeInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeOutputGigawordsInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeOutputGigawordsInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeOutputGigawordsInAcctStop_Object = MibScalar
juniRadiusClientIncludeOutputGigawordsInAcctStop = _JuniRadiusClientIncludeOutputGigawordsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 73),
    _JuniRadiusClientIncludeOutputGigawordsInAcctStop_Type()
)
juniRadiusClientIncludeOutputGigawordsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeOutputGigawordsInAcctStop.setStatus("current")


class _JuniRadiusClientIncludePppoeDescriptionInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludePppoeDescriptionInAcctStop based on TruthValue"""


_JuniRadiusClientIncludePppoeDescriptionInAcctStop_Object = MibScalar
juniRadiusClientIncludePppoeDescriptionInAcctStop = _JuniRadiusClientIncludePppoeDescriptionInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 74),
    _JuniRadiusClientIncludePppoeDescriptionInAcctStop_Type()
)
juniRadiusClientIncludePppoeDescriptionInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludePppoeDescriptionInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelAssignmentIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelAssignmentIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelAssignmentIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelAssignmentIdInAcctStop = _JuniRadiusClientIncludeTunnelAssignmentIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 75),
    _JuniRadiusClientIncludeTunnelAssignmentIdInAcctStop_Type()
)
juniRadiusClientIncludeTunnelAssignmentIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelAssignmentIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelClientAuthIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelClientAuthIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelClientAuthIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelClientAuthIdInAcctStop = _JuniRadiusClientIncludeTunnelClientAuthIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 76),
    _JuniRadiusClientIncludeTunnelClientAuthIdInAcctStop_Type()
)
juniRadiusClientIncludeTunnelClientAuthIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelClientAuthIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelClientEndpointInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelClientEndpointInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelClientEndpointInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelClientEndpointInAcctStop = _JuniRadiusClientIncludeTunnelClientEndpointInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 77),
    _JuniRadiusClientIncludeTunnelClientEndpointInAcctStop_Type()
)
juniRadiusClientIncludeTunnelClientEndpointInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelClientEndpointInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelMediumTypeInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelMediumTypeInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelMediumTypeInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelMediumTypeInAcctStop = _JuniRadiusClientIncludeTunnelMediumTypeInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 78),
    _JuniRadiusClientIncludeTunnelMediumTypeInAcctStop_Type()
)
juniRadiusClientIncludeTunnelMediumTypeInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelMediumTypeInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelPreferenceInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelPreferenceInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelPreferenceInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelPreferenceInAcctStop = _JuniRadiusClientIncludeTunnelPreferenceInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 79),
    _JuniRadiusClientIncludeTunnelPreferenceInAcctStop_Type()
)
juniRadiusClientIncludeTunnelPreferenceInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelPreferenceInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerAttributesInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerAttributesInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerAttributesInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelServerAttributesInAcctStop = _JuniRadiusClientIncludeTunnelServerAttributesInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 80),
    _JuniRadiusClientIncludeTunnelServerAttributesInAcctStop_Type()
)
juniRadiusClientIncludeTunnelServerAttributesInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerAttributesInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerAuthIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerAuthIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerAuthIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelServerAuthIdInAcctStop = _JuniRadiusClientIncludeTunnelServerAuthIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 81),
    _JuniRadiusClientIncludeTunnelServerAuthIdInAcctStop_Type()
)
juniRadiusClientIncludeTunnelServerAuthIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerAuthIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelServerEndpointInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelServerEndpointInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelServerEndpointInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelServerEndpointInAcctStop = _JuniRadiusClientIncludeTunnelServerEndpointInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 82),
    _JuniRadiusClientIncludeTunnelServerEndpointInAcctStop_Type()
)
juniRadiusClientIncludeTunnelServerEndpointInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelServerEndpointInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeTunnelTypeInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelTypeInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelTypeInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelTypeInAcctStop = _JuniRadiusClientIncludeTunnelTypeInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 83),
    _JuniRadiusClientIncludeTunnelTypeInAcctStop_Type()
)
juniRadiusClientIncludeTunnelTypeInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelTypeInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeInputGigapktsInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeInputGigapktsInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeInputGigapktsInAcctStop_Object = MibScalar
juniRadiusClientIncludeInputGigapktsInAcctStop = _JuniRadiusClientIncludeInputGigapktsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 84),
    _JuniRadiusClientIncludeInputGigapktsInAcctStop_Type()
)
juniRadiusClientIncludeInputGigapktsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeInputGigapktsInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeOutputGigapktsInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeOutputGigapktsInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeOutputGigapktsInAcctStop_Object = MibScalar
juniRadiusClientIncludeOutputGigapktsInAcctStop = _JuniRadiusClientIncludeOutputGigapktsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 85),
    _JuniRadiusClientIncludeOutputGigapktsInAcctStop_Type()
)
juniRadiusClientIncludeOutputGigapktsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeOutputGigapktsInAcctStop.setStatus("current")


class _JuniRadiusClientIgnoreFramedIpNetmask_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreFramedIpNetmask based on TruthValue"""


_JuniRadiusClientIgnoreFramedIpNetmask_Object = MibScalar
juniRadiusClientIgnoreFramedIpNetmask = _JuniRadiusClientIgnoreFramedIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 86),
    _JuniRadiusClientIgnoreFramedIpNetmask_Type()
)
juniRadiusClientIgnoreFramedIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreFramedIpNetmask.setStatus("current")


class _JuniRadiusClientIgnoreAtmCategory_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreAtmCategory based on TruthValue"""


_JuniRadiusClientIgnoreAtmCategory_Object = MibScalar
juniRadiusClientIgnoreAtmCategory = _JuniRadiusClientIgnoreAtmCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 87),
    _JuniRadiusClientIgnoreAtmCategory_Type()
)
juniRadiusClientIgnoreAtmCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreAtmCategory.setStatus("current")


class _JuniRadiusClientIgnoreAtmMbs_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreAtmMbs based on TruthValue"""


_JuniRadiusClientIgnoreAtmMbs_Object = MibScalar
juniRadiusClientIgnoreAtmMbs = _JuniRadiusClientIgnoreAtmMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 88),
    _JuniRadiusClientIgnoreAtmMbs_Type()
)
juniRadiusClientIgnoreAtmMbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreAtmMbs.setStatus("current")


class _JuniRadiusClientIgnoreAtmPcr_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreAtmPcr based on TruthValue"""


_JuniRadiusClientIgnoreAtmPcr_Object = MibScalar
juniRadiusClientIgnoreAtmPcr = _JuniRadiusClientIgnoreAtmPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 89),
    _JuniRadiusClientIgnoreAtmPcr_Type()
)
juniRadiusClientIgnoreAtmPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreAtmPcr.setStatus("current")


class _JuniRadiusClientIgnoreAtmScr_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreAtmScr based on TruthValue"""


_JuniRadiusClientIgnoreAtmScr_Object = MibScalar
juniRadiusClientIgnoreAtmScr = _JuniRadiusClientIgnoreAtmScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 90),
    _JuniRadiusClientIgnoreAtmScr_Type()
)
juniRadiusClientIgnoreAtmScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreAtmScr.setStatus("current")


class _JuniRadiusClientIgnoreEgressPolicyName_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreEgressPolicyName based on TruthValue"""


_JuniRadiusClientIgnoreEgressPolicyName_Object = MibScalar
juniRadiusClientIgnoreEgressPolicyName = _JuniRadiusClientIgnoreEgressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 91),
    _JuniRadiusClientIgnoreEgressPolicyName_Type()
)
juniRadiusClientIgnoreEgressPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreEgressPolicyName.setStatus("current")


class _JuniRadiusClientIgnoreIngressPolicyName_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreIngressPolicyName based on TruthValue"""


_JuniRadiusClientIgnoreIngressPolicyName_Object = MibScalar
juniRadiusClientIgnoreIngressPolicyName = _JuniRadiusClientIgnoreIngressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 92),
    _JuniRadiusClientIgnoreIngressPolicyName_Type()
)
juniRadiusClientIgnoreIngressPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreIngressPolicyName.setStatus("current")


class _JuniRadiusClientIgnoreVirtualRouter_Type(TruthValue):
    """Custom type juniRadiusClientIgnoreVirtualRouter based on TruthValue"""


_JuniRadiusClientIgnoreVirtualRouter_Object = MibScalar
juniRadiusClientIgnoreVirtualRouter = _JuniRadiusClientIgnoreVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 93),
    _JuniRadiusClientIgnoreVirtualRouter_Type()
)
juniRadiusClientIgnoreVirtualRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnoreVirtualRouter.setStatus("current")


class _JuniRadiusClientTrapOnAuthServerUnavailable_Type(TruthValue):
    """Custom type juniRadiusClientTrapOnAuthServerUnavailable based on TruthValue"""


_JuniRadiusClientTrapOnAuthServerUnavailable_Object = MibScalar
juniRadiusClientTrapOnAuthServerUnavailable = _JuniRadiusClientTrapOnAuthServerUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 94),
    _JuniRadiusClientTrapOnAuthServerUnavailable_Type()
)
juniRadiusClientTrapOnAuthServerUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientTrapOnAuthServerUnavailable.setStatus("current")


class _JuniRadiusClientTrapOnAcctServerUnavailable_Type(TruthValue):
    """Custom type juniRadiusClientTrapOnAcctServerUnavailable based on TruthValue"""


_JuniRadiusClientTrapOnAcctServerUnavailable_Object = MibScalar
juniRadiusClientTrapOnAcctServerUnavailable = _JuniRadiusClientTrapOnAcctServerUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 95),
    _JuniRadiusClientTrapOnAcctServerUnavailable_Type()
)
juniRadiusClientTrapOnAcctServerUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientTrapOnAcctServerUnavailable.setStatus("current")


class _JuniRadiusClientTrapOnNoAuthServerAvailable_Type(TruthValue):
    """Custom type juniRadiusClientTrapOnNoAuthServerAvailable based on TruthValue"""


_JuniRadiusClientTrapOnNoAuthServerAvailable_Object = MibScalar
juniRadiusClientTrapOnNoAuthServerAvailable = _JuniRadiusClientTrapOnNoAuthServerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 96),
    _JuniRadiusClientTrapOnNoAuthServerAvailable_Type()
)
juniRadiusClientTrapOnNoAuthServerAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientTrapOnNoAuthServerAvailable.setStatus("current")


class _JuniRadiusClientTrapOnNoAcctServerAvailable_Type(TruthValue):
    """Custom type juniRadiusClientTrapOnNoAcctServerAvailable based on TruthValue"""


_JuniRadiusClientTrapOnNoAcctServerAvailable_Object = MibScalar
juniRadiusClientTrapOnNoAcctServerAvailable = _JuniRadiusClientTrapOnNoAcctServerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 97),
    _JuniRadiusClientTrapOnNoAcctServerAvailable_Type()
)
juniRadiusClientTrapOnNoAcctServerAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientTrapOnNoAcctServerAvailable.setStatus("current")


class _JuniRadiusClientTrapOnAuthServerAvailable_Type(TruthValue):
    """Custom type juniRadiusClientTrapOnAuthServerAvailable based on TruthValue"""


_JuniRadiusClientTrapOnAuthServerAvailable_Object = MibScalar
juniRadiusClientTrapOnAuthServerAvailable = _JuniRadiusClientTrapOnAuthServerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 98),
    _JuniRadiusClientTrapOnAuthServerAvailable_Type()
)
juniRadiusClientTrapOnAuthServerAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientTrapOnAuthServerAvailable.setStatus("current")


class _JuniRadiusClientTrapOnAcctServerAvailable_Type(TruthValue):
    """Custom type juniRadiusClientTrapOnAcctServerAvailable based on TruthValue"""


_JuniRadiusClientTrapOnAcctServerAvailable_Object = MibScalar
juniRadiusClientTrapOnAcctServerAvailable = _JuniRadiusClientTrapOnAcctServerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 99),
    _JuniRadiusClientTrapOnAcctServerAvailable_Type()
)
juniRadiusClientTrapOnAcctServerAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientTrapOnAcctServerAvailable.setStatus("current")


class _JuniRadiusClientPppoeNasPortFormat_Type(Integer32):
    """Custom type juniRadiusClientPppoeNasPortFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("unique", 1))
    )


_JuniRadiusClientPppoeNasPortFormat_Type.__name__ = "Integer32"
_JuniRadiusClientPppoeNasPortFormat_Object = MibScalar
juniRadiusClientPppoeNasPortFormat = _JuniRadiusClientPppoeNasPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 100),
    _JuniRadiusClientPppoeNasPortFormat_Type()
)
juniRadiusClientPppoeNasPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientPppoeNasPortFormat.setStatus("current")


class _JuniRadiusClientIncludeTunnelInterfaceIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelInterfaceIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeTunnelInterfaceIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeTunnelInterfaceIdInAccessReq = _JuniRadiusClientIncludeTunnelInterfaceIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 101),
    _JuniRadiusClientIncludeTunnelInterfaceIdInAccessReq_Type()
)
juniRadiusClientIncludeTunnelInterfaceIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelInterfaceIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeTunnelInterfaceIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelInterfaceIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeTunnelInterfaceIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeTunnelInterfaceIdInAcctStart = _JuniRadiusClientIncludeTunnelInterfaceIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 102),
    _JuniRadiusClientIncludeTunnelInterfaceIdInAcctStart_Type()
)
juniRadiusClientIncludeTunnelInterfaceIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelInterfaceIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeTunnelInterfaceIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeTunnelInterfaceIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeTunnelInterfaceIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeTunnelInterfaceIdInAcctStop = _JuniRadiusClientIncludeTunnelInterfaceIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 103),
    _JuniRadiusClientIncludeTunnelInterfaceIdInAcctStop_Type()
)
juniRadiusClientIncludeTunnelInterfaceIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeTunnelInterfaceIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop = _JuniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 104),
    _JuniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop_Type()
)
juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop.setStatus("current")


class _JuniRadiusClientVlanNasPortFormat_Type(Integer32):
    """Custom type juniRadiusClientVlanNasPortFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("stacked", 1))
    )


_JuniRadiusClientVlanNasPortFormat_Type.__name__ = "Integer32"
_JuniRadiusClientVlanNasPortFormat_Object = MibScalar
juniRadiusClientVlanNasPortFormat = _JuniRadiusClientVlanNasPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 105),
    _JuniRadiusClientVlanNasPortFormat_Type()
)
juniRadiusClientVlanNasPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientVlanNasPortFormat.setStatus("current")


class _JuniRadiusClientIncludeAcctMultiSessionIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctMultiSessionIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeAcctMultiSessionIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeAcctMultiSessionIdInAccessReq = _JuniRadiusClientIncludeAcctMultiSessionIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 106),
    _JuniRadiusClientIncludeAcctMultiSessionIdInAccessReq_Type()
)
juniRadiusClientIncludeAcctMultiSessionIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctMultiSessionIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeAcctMultiSessionIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctMultiSessionIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeAcctMultiSessionIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeAcctMultiSessionIdInAcctStart = _JuniRadiusClientIncludeAcctMultiSessionIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 107),
    _JuniRadiusClientIncludeAcctMultiSessionIdInAcctStart_Type()
)
juniRadiusClientIncludeAcctMultiSessionIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctMultiSessionIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeAcctMultiSessionIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctMultiSessionIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeAcctMultiSessionIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeAcctMultiSessionIdInAcctStop = _JuniRadiusClientIncludeAcctMultiSessionIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 108),
    _JuniRadiusClientIncludeAcctMultiSessionIdInAcctStop_Type()
)
juniRadiusClientIncludeAcctMultiSessionIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctMultiSessionIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeAscendNumInMultilinkInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAscendNumInMultilinkInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeAscendNumInMultilinkInAccessReq_Object = MibScalar
juniRadiusClientIncludeAscendNumInMultilinkInAccessReq = _JuniRadiusClientIncludeAscendNumInMultilinkInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 109),
    _JuniRadiusClientIncludeAscendNumInMultilinkInAccessReq_Type()
)
juniRadiusClientIncludeAscendNumInMultilinkInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAscendNumInMultilinkInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeAscendNumInMultilinkInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAscendNumInMultilinkInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeAscendNumInMultilinkInAcctStart_Object = MibScalar
juniRadiusClientIncludeAscendNumInMultilinkInAcctStart = _JuniRadiusClientIncludeAscendNumInMultilinkInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 110),
    _JuniRadiusClientIncludeAscendNumInMultilinkInAcctStart_Type()
)
juniRadiusClientIncludeAscendNumInMultilinkInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAscendNumInMultilinkInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeAscendNumInMultilinkInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAscendNumInMultilinkInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeAscendNumInMultilinkInAcctStop_Object = MibScalar
juniRadiusClientIncludeAscendNumInMultilinkInAcctStop = _JuniRadiusClientIncludeAscendNumInMultilinkInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 111),
    _JuniRadiusClientIncludeAscendNumInMultilinkInAcctStop_Type()
)
juniRadiusClientIncludeAscendNumInMultilinkInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAscendNumInMultilinkInAcctStop.setStatus("current")


class _JuniRadiusClientConnectInfoFormat_Type(Integer32):
    """Custom type juniRadiusClientConnectInfoFormat based on Integer32"""
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
        *(("default", 0),
          ("l2tpConnectSpeed", 1),
          ("l2tpConnectSpeedRxWhenEqual", 2))
    )


_JuniRadiusClientConnectInfoFormat_Type.__name__ = "Integer32"
_JuniRadiusClientConnectInfoFormat_Object = MibScalar
juniRadiusClientConnectInfoFormat = _JuniRadiusClientConnectInfoFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 112),
    _JuniRadiusClientConnectInfoFormat_Type()
)
juniRadiusClientConnectInfoFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientConnectInfoFormat.setStatus("current")


class _JuniRadiusClientIncludeProfileServiceDescrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeProfileServiceDescrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeProfileServiceDescrInAccessReq_Object = MibScalar
juniRadiusClientIncludeProfileServiceDescrInAccessReq = _JuniRadiusClientIncludeProfileServiceDescrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 113),
    _JuniRadiusClientIncludeProfileServiceDescrInAccessReq_Type()
)
juniRadiusClientIncludeProfileServiceDescrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeProfileServiceDescrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeProfileServiceDescrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeProfileServiceDescrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeProfileServiceDescrInAcctStart_Object = MibScalar
juniRadiusClientIncludeProfileServiceDescrInAcctStart = _JuniRadiusClientIncludeProfileServiceDescrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 114),
    _JuniRadiusClientIncludeProfileServiceDescrInAcctStart_Type()
)
juniRadiusClientIncludeProfileServiceDescrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeProfileServiceDescrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeProfileServiceDescrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeProfileServiceDescrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeProfileServiceDescrInAcctStop_Object = MibScalar
juniRadiusClientIncludeProfileServiceDescrInAcctStop = _JuniRadiusClientIncludeProfileServiceDescrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 115),
    _JuniRadiusClientIncludeProfileServiceDescrInAcctStop_Type()
)
juniRadiusClientIncludeProfileServiceDescrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeProfileServiceDescrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeAcctAuthenticInAcctOn_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctAuthenticInAcctOn based on TruthValue"""


_JuniRadiusClientIncludeAcctAuthenticInAcctOn_Object = MibScalar
juniRadiusClientIncludeAcctAuthenticInAcctOn = _JuniRadiusClientIncludeAcctAuthenticInAcctOn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 116),
    _JuniRadiusClientIncludeAcctAuthenticInAcctOn_Type()
)
juniRadiusClientIncludeAcctAuthenticInAcctOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctAuthenticInAcctOn.setStatus("current")


class _JuniRadiusClientIncludeAcctDelayTimeInAcctOn_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctDelayTimeInAcctOn based on TruthValue"""


_JuniRadiusClientIncludeAcctDelayTimeInAcctOn_Object = MibScalar
juniRadiusClientIncludeAcctDelayTimeInAcctOn = _JuniRadiusClientIncludeAcctDelayTimeInAcctOn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 117),
    _JuniRadiusClientIncludeAcctDelayTimeInAcctOn_Type()
)
juniRadiusClientIncludeAcctDelayTimeInAcctOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctDelayTimeInAcctOn.setStatus("current")


class _JuniRadiusClientIncludeAcctSessionIdInAcctOn_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctSessionIdInAcctOn based on TruthValue"""


_JuniRadiusClientIncludeAcctSessionIdInAcctOn_Object = MibScalar
juniRadiusClientIncludeAcctSessionIdInAcctOn = _JuniRadiusClientIncludeAcctSessionIdInAcctOn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 118),
    _JuniRadiusClientIncludeAcctSessionIdInAcctOn_Type()
)
juniRadiusClientIncludeAcctSessionIdInAcctOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctSessionIdInAcctOn.setStatus("current")


class _JuniRadiusClientIncludeNasIdentifierInAcctOn_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasIdentifierInAcctOn based on TruthValue"""


_JuniRadiusClientIncludeNasIdentifierInAcctOn_Object = MibScalar
juniRadiusClientIncludeNasIdentifierInAcctOn = _JuniRadiusClientIncludeNasIdentifierInAcctOn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 119),
    _JuniRadiusClientIncludeNasIdentifierInAcctOn_Type()
)
juniRadiusClientIncludeNasIdentifierInAcctOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasIdentifierInAcctOn.setStatus("current")


class _JuniRadiusClientIncludeEventTimestampInAcctOn_Type(TruthValue):
    """Custom type juniRadiusClientIncludeEventTimestampInAcctOn based on TruthValue"""


_JuniRadiusClientIncludeEventTimestampInAcctOn_Object = MibScalar
juniRadiusClientIncludeEventTimestampInAcctOn = _JuniRadiusClientIncludeEventTimestampInAcctOn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 120),
    _JuniRadiusClientIncludeEventTimestampInAcctOn_Type()
)
juniRadiusClientIncludeEventTimestampInAcctOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeEventTimestampInAcctOn.setStatus("current")


class _JuniRadiusClientIncludeAcctAuthenticInAcctOff_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctAuthenticInAcctOff based on TruthValue"""


_JuniRadiusClientIncludeAcctAuthenticInAcctOff_Object = MibScalar
juniRadiusClientIncludeAcctAuthenticInAcctOff = _JuniRadiusClientIncludeAcctAuthenticInAcctOff_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 121),
    _JuniRadiusClientIncludeAcctAuthenticInAcctOff_Type()
)
juniRadiusClientIncludeAcctAuthenticInAcctOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctAuthenticInAcctOff.setStatus("current")


class _JuniRadiusClientIncludeAcctDelayTimeInAcctOff_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctDelayTimeInAcctOff based on TruthValue"""


_JuniRadiusClientIncludeAcctDelayTimeInAcctOff_Object = MibScalar
juniRadiusClientIncludeAcctDelayTimeInAcctOff = _JuniRadiusClientIncludeAcctDelayTimeInAcctOff_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 122),
    _JuniRadiusClientIncludeAcctDelayTimeInAcctOff_Type()
)
juniRadiusClientIncludeAcctDelayTimeInAcctOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctDelayTimeInAcctOff.setStatus("current")


class _JuniRadiusClientIncludeAcctSessionIdInAcctOff_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctSessionIdInAcctOff based on TruthValue"""


_JuniRadiusClientIncludeAcctSessionIdInAcctOff_Object = MibScalar
juniRadiusClientIncludeAcctSessionIdInAcctOff = _JuniRadiusClientIncludeAcctSessionIdInAcctOff_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 123),
    _JuniRadiusClientIncludeAcctSessionIdInAcctOff_Type()
)
juniRadiusClientIncludeAcctSessionIdInAcctOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctSessionIdInAcctOff.setStatus("current")


class _JuniRadiusClientIncludeAcctTerminateCauseInAcctOff_Type(TruthValue):
    """Custom type juniRadiusClientIncludeAcctTerminateCauseInAcctOff based on TruthValue"""


_JuniRadiusClientIncludeAcctTerminateCauseInAcctOff_Object = MibScalar
juniRadiusClientIncludeAcctTerminateCauseInAcctOff = _JuniRadiusClientIncludeAcctTerminateCauseInAcctOff_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 124),
    _JuniRadiusClientIncludeAcctTerminateCauseInAcctOff_Type()
)
juniRadiusClientIncludeAcctTerminateCauseInAcctOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeAcctTerminateCauseInAcctOff.setStatus("current")


class _JuniRadiusClientIncludeNasIdentifierInAcctOff_Type(TruthValue):
    """Custom type juniRadiusClientIncludeNasIdentifierInAcctOff based on TruthValue"""


_JuniRadiusClientIncludeNasIdentifierInAcctOff_Object = MibScalar
juniRadiusClientIncludeNasIdentifierInAcctOff = _JuniRadiusClientIncludeNasIdentifierInAcctOff_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 125),
    _JuniRadiusClientIncludeNasIdentifierInAcctOff_Type()
)
juniRadiusClientIncludeNasIdentifierInAcctOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeNasIdentifierInAcctOff.setStatus("current")


class _JuniRadiusClientIncludeEventTimestampInAcctOff_Type(TruthValue):
    """Custom type juniRadiusClientIncludeEventTimestampInAcctOff based on TruthValue"""


_JuniRadiusClientIncludeEventTimestampInAcctOff_Object = MibScalar
juniRadiusClientIncludeEventTimestampInAcctOff = _JuniRadiusClientIncludeEventTimestampInAcctOff_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 126),
    _JuniRadiusClientIncludeEventTimestampInAcctOff_Type()
)
juniRadiusClientIncludeEventTimestampInAcctOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeEventTimestampInAcctOff.setStatus("current")


class _JuniRadiusClientIncludeDhcpOptionsInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpOptionsInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeDhcpOptionsInAccessReq_Object = MibScalar
juniRadiusClientIncludeDhcpOptionsInAccessReq = _JuniRadiusClientIncludeDhcpOptionsInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 127),
    _JuniRadiusClientIncludeDhcpOptionsInAccessReq_Type()
)
juniRadiusClientIncludeDhcpOptionsInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpOptionsInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeDhcpMacAddressInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpMacAddressInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeDhcpMacAddressInAccessReq_Object = MibScalar
juniRadiusClientIncludeDhcpMacAddressInAccessReq = _JuniRadiusClientIncludeDhcpMacAddressInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 128),
    _JuniRadiusClientIncludeDhcpMacAddressInAccessReq_Type()
)
juniRadiusClientIncludeDhcpMacAddressInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpMacAddressInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeDhcpGiAddressInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpGiAddressInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeDhcpGiAddressInAccessReq_Object = MibScalar
juniRadiusClientIncludeDhcpGiAddressInAccessReq = _JuniRadiusClientIncludeDhcpGiAddressInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 129),
    _JuniRadiusClientIncludeDhcpGiAddressInAccessReq_Type()
)
juniRadiusClientIncludeDhcpGiAddressInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpGiAddressInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeDhcpOptionsInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpOptionsInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeDhcpOptionsInAcctStart_Object = MibScalar
juniRadiusClientIncludeDhcpOptionsInAcctStart = _JuniRadiusClientIncludeDhcpOptionsInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 130),
    _JuniRadiusClientIncludeDhcpOptionsInAcctStart_Type()
)
juniRadiusClientIncludeDhcpOptionsInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpOptionsInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeDhcpMacAddressInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpMacAddressInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeDhcpMacAddressInAcctStart_Object = MibScalar
juniRadiusClientIncludeDhcpMacAddressInAcctStart = _JuniRadiusClientIncludeDhcpMacAddressInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 131),
    _JuniRadiusClientIncludeDhcpMacAddressInAcctStart_Type()
)
juniRadiusClientIncludeDhcpMacAddressInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpMacAddressInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeDhcpGiAddressInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpGiAddressInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeDhcpGiAddressInAcctStart_Object = MibScalar
juniRadiusClientIncludeDhcpGiAddressInAcctStart = _JuniRadiusClientIncludeDhcpGiAddressInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 132),
    _JuniRadiusClientIncludeDhcpGiAddressInAcctStart_Type()
)
juniRadiusClientIncludeDhcpGiAddressInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpGiAddressInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeDhcpOptionsInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpOptionsInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeDhcpOptionsInAcctStop_Object = MibScalar
juniRadiusClientIncludeDhcpOptionsInAcctStop = _JuniRadiusClientIncludeDhcpOptionsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 133),
    _JuniRadiusClientIncludeDhcpOptionsInAcctStop_Type()
)
juniRadiusClientIncludeDhcpOptionsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpOptionsInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeDhcpMacAddressInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpMacAddressInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeDhcpMacAddressInAcctStop_Object = MibScalar
juniRadiusClientIncludeDhcpMacAddressInAcctStop = _JuniRadiusClientIncludeDhcpMacAddressInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 134),
    _JuniRadiusClientIncludeDhcpMacAddressInAcctStop_Type()
)
juniRadiusClientIncludeDhcpMacAddressInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpMacAddressInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeDhcpGiAddressInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDhcpGiAddressInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeDhcpGiAddressInAcctStop_Object = MibScalar
juniRadiusClientIncludeDhcpGiAddressInAcctStop = _JuniRadiusClientIncludeDhcpGiAddressInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 135),
    _JuniRadiusClientIncludeDhcpGiAddressInAcctStop_Type()
)
juniRadiusClientIncludeDhcpGiAddressInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDhcpGiAddressInAcctStop.setStatus("current")


class _JuniRadiusClientNasPortIdOverrideRemoteCircuitId_Type(TruthValue):
    """Custom type juniRadiusClientNasPortIdOverrideRemoteCircuitId based on TruthValue"""


_JuniRadiusClientNasPortIdOverrideRemoteCircuitId_Object = MibScalar
juniRadiusClientNasPortIdOverrideRemoteCircuitId = _JuniRadiusClientNasPortIdOverrideRemoteCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 136),
    _JuniRadiusClientNasPortIdOverrideRemoteCircuitId_Type()
)
juniRadiusClientNasPortIdOverrideRemoteCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortIdOverrideRemoteCircuitId.setStatus("current")


class _JuniRadiusClientCallingStationIdOverrideRemoteCircuitId_Type(TruthValue):
    """Custom type juniRadiusClientCallingStationIdOverrideRemoteCircuitId based on TruthValue"""


_JuniRadiusClientCallingStationIdOverrideRemoteCircuitId_Object = MibScalar
juniRadiusClientCallingStationIdOverrideRemoteCircuitId = _JuniRadiusClientCallingStationIdOverrideRemoteCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 137),
    _JuniRadiusClientCallingStationIdOverrideRemoteCircuitId_Type()
)
juniRadiusClientCallingStationIdOverrideRemoteCircuitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientCallingStationIdOverrideRemoteCircuitId.setStatus("current")


class _JuniRadiusClientIncludeMlpppBundleNameInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeMlpppBundleNameInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeMlpppBundleNameInAccessReq_Object = MibScalar
juniRadiusClientIncludeMlpppBundleNameInAccessReq = _JuniRadiusClientIncludeMlpppBundleNameInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 138),
    _JuniRadiusClientIncludeMlpppBundleNameInAccessReq_Type()
)
juniRadiusClientIncludeMlpppBundleNameInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeMlpppBundleNameInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeMlpppBundleNameInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeMlpppBundleNameInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeMlpppBundleNameInAcctStart_Object = MibScalar
juniRadiusClientIncludeMlpppBundleNameInAcctStart = _JuniRadiusClientIncludeMlpppBundleNameInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 139),
    _JuniRadiusClientIncludeMlpppBundleNameInAcctStart_Type()
)
juniRadiusClientIncludeMlpppBundleNameInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeMlpppBundleNameInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeMlpppBundleNameInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeMlpppBundleNameInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeMlpppBundleNameInAcctStop_Object = MibScalar
juniRadiusClientIncludeMlpppBundleNameInAcctStop = _JuniRadiusClientIncludeMlpppBundleNameInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 140),
    _JuniRadiusClientIncludeMlpppBundleNameInAcctStop_Type()
)
juniRadiusClientIncludeMlpppBundleNameInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeMlpppBundleNameInAcctStop.setStatus("current")


class _JuniRadiusClientOverrideNasInfo_Type(TruthValue):
    """Custom type juniRadiusClientOverrideNasInfo based on TruthValue"""


_JuniRadiusClientOverrideNasInfo_Object = MibScalar
juniRadiusClientOverrideNasInfo = _JuniRadiusClientOverrideNasInfo_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 141),
    _JuniRadiusClientOverrideNasInfo_Type()
)
juniRadiusClientOverrideNasInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientOverrideNasInfo.setStatus("current")


class _JuniRadiusClientIncludeInterfaceDescriptionInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeInterfaceDescriptionInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeInterfaceDescriptionInAccessReq_Object = MibScalar
juniRadiusClientIncludeInterfaceDescriptionInAccessReq = _JuniRadiusClientIncludeInterfaceDescriptionInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 142),
    _JuniRadiusClientIncludeInterfaceDescriptionInAccessReq_Type()
)
juniRadiusClientIncludeInterfaceDescriptionInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeInterfaceDescriptionInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeInterfaceDescriptionInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeInterfaceDescriptionInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeInterfaceDescriptionInAcctStart_Object = MibScalar
juniRadiusClientIncludeInterfaceDescriptionInAcctStart = _JuniRadiusClientIncludeInterfaceDescriptionInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 143),
    _JuniRadiusClientIncludeInterfaceDescriptionInAcctStart_Type()
)
juniRadiusClientIncludeInterfaceDescriptionInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeInterfaceDescriptionInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeInterfaceDescriptionInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeInterfaceDescriptionInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeInterfaceDescriptionInAcctStop_Object = MibScalar
juniRadiusClientIncludeInterfaceDescriptionInAcctStop = _JuniRadiusClientIncludeInterfaceDescriptionInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 144),
    _JuniRadiusClientIncludeInterfaceDescriptionInAcctStop_Type()
)
juniRadiusClientIncludeInterfaceDescriptionInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeInterfaceDescriptionInAcctStop.setStatus("current")


class _JuniRadiusClientAtmNasPortFormat_Type(Integer32):
    """Custom type juniRadiusClientAtmNasPortFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extended", 1),
          ("none", 0))
    )


_JuniRadiusClientAtmNasPortFormat_Type.__name__ = "Integer32"
_JuniRadiusClientAtmNasPortFormat_Object = MibScalar
juniRadiusClientAtmNasPortFormat = _JuniRadiusClientAtmNasPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 145),
    _JuniRadiusClientAtmNasPortFormat_Type()
)
juniRadiusClientAtmNasPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientAtmNasPortFormat.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthAtmSlot_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthAtmSlot based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthAtmSlot_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthAtmSlot_Object = MibScalar
juniRadiusClientNasPortFieldWidthAtmSlot = _JuniRadiusClientNasPortFieldWidthAtmSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 146),
    _JuniRadiusClientNasPortFieldWidthAtmSlot_Type()
)
juniRadiusClientNasPortFieldWidthAtmSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthAtmSlot.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthAtmAdapter_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthAtmAdapter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthAtmAdapter_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthAtmAdapter_Object = MibScalar
juniRadiusClientNasPortFieldWidthAtmAdapter = _JuniRadiusClientNasPortFieldWidthAtmAdapter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 147),
    _JuniRadiusClientNasPortFieldWidthAtmAdapter_Type()
)
juniRadiusClientNasPortFieldWidthAtmAdapter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthAtmAdapter.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthAtmPort_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthAtmPort based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthAtmPort_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthAtmPort_Object = MibScalar
juniRadiusClientNasPortFieldWidthAtmPort = _JuniRadiusClientNasPortFieldWidthAtmPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 148),
    _JuniRadiusClientNasPortFieldWidthAtmPort_Type()
)
juniRadiusClientNasPortFieldWidthAtmPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthAtmPort.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthAtmVpi_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthAtmVpi based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthAtmVpi_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthAtmVpi_Object = MibScalar
juniRadiusClientNasPortFieldWidthAtmVpi = _JuniRadiusClientNasPortFieldWidthAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 149),
    _JuniRadiusClientNasPortFieldWidthAtmVpi_Type()
)
juniRadiusClientNasPortFieldWidthAtmVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthAtmVpi.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthAtmVci_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthAtmVci based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthAtmVci_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthAtmVci_Object = MibScalar
juniRadiusClientNasPortFieldWidthAtmVci = _JuniRadiusClientNasPortFieldWidthAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 150),
    _JuniRadiusClientNasPortFieldWidthAtmVci_Type()
)
juniRadiusClientNasPortFieldWidthAtmVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthAtmVci.setStatus("current")


class _JuniRadiusClientEthernetNasPortFormat_Type(Integer32):
    """Custom type juniRadiusClientEthernetNasPortFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("extended", 1),
          ("none", 0))
    )


_JuniRadiusClientEthernetNasPortFormat_Type.__name__ = "Integer32"
_JuniRadiusClientEthernetNasPortFormat_Object = MibScalar
juniRadiusClientEthernetNasPortFormat = _JuniRadiusClientEthernetNasPortFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 151),
    _JuniRadiusClientEthernetNasPortFormat_Type()
)
juniRadiusClientEthernetNasPortFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientEthernetNasPortFormat.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthEthernetSlot_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthEthernetSlot based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthEthernetSlot_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthEthernetSlot_Object = MibScalar
juniRadiusClientNasPortFieldWidthEthernetSlot = _JuniRadiusClientNasPortFieldWidthEthernetSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 152),
    _JuniRadiusClientNasPortFieldWidthEthernetSlot_Type()
)
juniRadiusClientNasPortFieldWidthEthernetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthEthernetSlot.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthEthernetAdapter_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthEthernetAdapter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthEthernetAdapter_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthEthernetAdapter_Object = MibScalar
juniRadiusClientNasPortFieldWidthEthernetAdapter = _JuniRadiusClientNasPortFieldWidthEthernetAdapter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 153),
    _JuniRadiusClientNasPortFieldWidthEthernetAdapter_Type()
)
juniRadiusClientNasPortFieldWidthEthernetAdapter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthEthernetAdapter.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthEthernetPort_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthEthernetPort based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthEthernetPort_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthEthernetPort_Object = MibScalar
juniRadiusClientNasPortFieldWidthEthernetPort = _JuniRadiusClientNasPortFieldWidthEthernetPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 154),
    _JuniRadiusClientNasPortFieldWidthEthernetPort_Type()
)
juniRadiusClientNasPortFieldWidthEthernetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthEthernetPort.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthEthernetSVlan_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthEthernetSVlan based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthEthernetSVlan_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthEthernetSVlan_Object = MibScalar
juniRadiusClientNasPortFieldWidthEthernetSVlan = _JuniRadiusClientNasPortFieldWidthEthernetSVlan_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 155),
    _JuniRadiusClientNasPortFieldWidthEthernetSVlan_Type()
)
juniRadiusClientNasPortFieldWidthEthernetSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthEthernetSVlan.setStatus("current")


class _JuniRadiusClientNasPortFieldWidthEthernetVlan_Type(Integer32):
    """Custom type juniRadiusClientNasPortFieldWidthEthernetVlan based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniRadiusClientNasPortFieldWidthEthernetVlan_Type.__name__ = "Integer32"
_JuniRadiusClientNasPortFieldWidthEthernetVlan_Object = MibScalar
juniRadiusClientNasPortFieldWidthEthernetVlan = _JuniRadiusClientNasPortFieldWidthEthernetVlan_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 156),
    _JuniRadiusClientNasPortFieldWidthEthernetVlan_Type()
)
juniRadiusClientNasPortFieldWidthEthernetVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientNasPortFieldWidthEthernetVlan.setStatus("current")


class _JuniRadiusClientRemoteCircuitIdFormat_Type(OctetString):
    """Custom type juniRadiusClientRemoteCircuitIdFormat based on OctetString"""
    defaultHexValue = "1"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )


_JuniRadiusClientRemoteCircuitIdFormat_Type.__name__ = "OctetString"
_JuniRadiusClientRemoteCircuitIdFormat_Object = MibScalar
juniRadiusClientRemoteCircuitIdFormat = _JuniRadiusClientRemoteCircuitIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 157),
    _JuniRadiusClientRemoteCircuitIdFormat_Type()
)
juniRadiusClientRemoteCircuitIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientRemoteCircuitIdFormat.setStatus("current")


class _JuniRadiusClientRemoteCircuitIdDelimiter_Type(DisplayString):
    """Custom type juniRadiusClientRemoteCircuitIdDelimiter based on DisplayString"""
    defaultValue = OctetString("#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_JuniRadiusClientRemoteCircuitIdDelimiter_Type.__name__ = "DisplayString"
_JuniRadiusClientRemoteCircuitIdDelimiter_Object = MibScalar
juniRadiusClientRemoteCircuitIdDelimiter = _JuniRadiusClientRemoteCircuitIdDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 158),
    _JuniRadiusClientRemoteCircuitIdDelimiter_Type()
)
juniRadiusClientRemoteCircuitIdDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientRemoteCircuitIdDelimiter.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessLoopParametersInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessLoopParametersInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq = _JuniRadiusClientIncludeL2cAccessLoopParametersInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 159),
    _JuniRadiusClientIncludeL2cAccessLoopParametersInAccessReq_Type()
)
juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cDownStreamDataInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDownStreamDataInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cDownStreamDataInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cDownStreamDataInAccessReq = _JuniRadiusClientIncludeL2cDownStreamDataInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 160),
    _JuniRadiusClientIncludeL2cDownStreamDataInAccessReq_Type()
)
juniRadiusClientIncludeL2cDownStreamDataInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDownStreamDataInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cUpStreamDataInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cUpStreamDataInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cUpStreamDataInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cUpStreamDataInAccessReq = _JuniRadiusClientIncludeL2cUpStreamDataInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 161),
    _JuniRadiusClientIncludeL2cUpStreamDataInAccessReq_Type()
)
juniRadiusClientIncludeL2cUpStreamDataInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cUpStreamDataInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cDownStreamDataInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDownStreamDataInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cDownStreamDataInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cDownStreamDataInAcctStart = _JuniRadiusClientIncludeL2cDownStreamDataInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 162),
    _JuniRadiusClientIncludeL2cDownStreamDataInAcctStart_Type()
)
juniRadiusClientIncludeL2cDownStreamDataInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDownStreamDataInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cUpStreamDataInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cUpStreamDataInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cUpStreamDataInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cUpStreamDataInAcctStart = _JuniRadiusClientIncludeL2cUpStreamDataInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 163),
    _JuniRadiusClientIncludeL2cUpStreamDataInAcctStart_Type()
)
juniRadiusClientIncludeL2cUpStreamDataInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cUpStreamDataInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cDownStreamDataInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDownStreamDataInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cDownStreamDataInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cDownStreamDataInAcctStop = _JuniRadiusClientIncludeL2cDownStreamDataInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 164),
    _JuniRadiusClientIncludeL2cDownStreamDataInAcctStop_Type()
)
juniRadiusClientIncludeL2cDownStreamDataInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDownStreamDataInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cUpStreamDataInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cUpStreamDataInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cUpStreamDataInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cUpStreamDataInAcctStop = _JuniRadiusClientIncludeL2cUpStreamDataInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 165),
    _JuniRadiusClientIncludeL2cUpStreamDataInAcctStop_Type()
)
juniRadiusClientIncludeL2cUpStreamDataInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cUpStreamDataInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeDslForumAttributesInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDslForumAttributesInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeDslForumAttributesInAccessReq_Object = MibScalar
juniRadiusClientIncludeDslForumAttributesInAccessReq = _JuniRadiusClientIncludeDslForumAttributesInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 166),
    _JuniRadiusClientIncludeDslForumAttributesInAccessReq_Type()
)
juniRadiusClientIncludeDslForumAttributesInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDslForumAttributesInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeDslForumAttributesInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDslForumAttributesInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeDslForumAttributesInAcctStart_Object = MibScalar
juniRadiusClientIncludeDslForumAttributesInAcctStart = _JuniRadiusClientIncludeDslForumAttributesInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 167),
    _JuniRadiusClientIncludeDslForumAttributesInAcctStart_Type()
)
juniRadiusClientIncludeDslForumAttributesInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDslForumAttributesInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeDslForumAttributesInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDslForumAttributesInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeDslForumAttributesInAcctStop_Object = MibScalar
juniRadiusClientIncludeDslForumAttributesInAcctStop = _JuniRadiusClientIncludeDslForumAttributesInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 168),
    _JuniRadiusClientIncludeDslForumAttributesInAcctStop_Type()
)
juniRadiusClientIncludeDslForumAttributesInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDslForumAttributesInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq = _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 169),
    _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq_Type()
)
juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq = _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 170),
    _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq_Type()
)
juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq = _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 171),
    _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq_Type()
)
juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cActualDataRateUstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cActualDataRateUstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq = _JuniRadiusClientIncludeL2cActualDataRateUstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 172),
    _JuniRadiusClientIncludeL2cActualDataRateUstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cActualDataRateDstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cActualDataRateDstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq = _JuniRadiusClientIncludeL2cActualDataRateDstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 173),
    _JuniRadiusClientIncludeL2cActualDataRateDstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq = _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 174),
    _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq = _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 175),
    _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq = _JuniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 176),
    _JuniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq = _JuniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 177),
    _JuniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq = _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 178),
    _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq = _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 179),
    _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq = _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 180),
    _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq = _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 181),
    _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq = _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 182),
    _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq = _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 183),
    _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq = _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 184),
    _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq = _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 185),
    _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq_Type()
)
juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cDslLineStateInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDslLineStateInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cDslLineStateInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cDslLineStateInAccessReq = _JuniRadiusClientIncludeL2cDslLineStateInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 186),
    _JuniRadiusClientIncludeL2cDslLineStateInAccessReq_Type()
)
juniRadiusClientIncludeL2cDslLineStateInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDslLineStateInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cDslTypeInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDslTypeInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeL2cDslTypeInAccessReq_Object = MibScalar
juniRadiusClientIncludeL2cDslTypeInAccessReq = _JuniRadiusClientIncludeL2cDslTypeInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 187),
    _JuniRadiusClientIncludeL2cDslTypeInAccessReq_Type()
)
juniRadiusClientIncludeL2cDslTypeInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDslTypeInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart = _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 188),
    _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart_Type()
)
juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart = _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 189),
    _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart_Type()
)
juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart = _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 190),
    _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart_Type()
)
juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart = _JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 191),
    _JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart = _JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 192),
    _JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart = _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 193),
    _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart = _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 194),
    _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart = _JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 195),
    _JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart = _JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 196),
    _JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart = _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 197),
    _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart = _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 198),
    _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart = _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 199),
    _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart = _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 200),
    _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart = _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 201),
    _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart = _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 202),
    _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart = _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 203),
    _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart = _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 204),
    _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart_Type()
)
juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cDslLineStateInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDslLineStateInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cDslLineStateInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cDslLineStateInAcctStart = _JuniRadiusClientIncludeL2cDslLineStateInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 205),
    _JuniRadiusClientIncludeL2cDslLineStateInAcctStart_Type()
)
juniRadiusClientIncludeL2cDslLineStateInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDslLineStateInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cDslTypeInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDslTypeInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeL2cDslTypeInAcctStart_Object = MibScalar
juniRadiusClientIncludeL2cDslTypeInAcctStart = _JuniRadiusClientIncludeL2cDslTypeInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 206),
    _JuniRadiusClientIncludeL2cDslTypeInAcctStart_Type()
)
juniRadiusClientIncludeL2cDslTypeInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDslTypeInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop = _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 207),
    _JuniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop_Type()
)
juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop = _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 208),
    _JuniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop_Type()
)
juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop = _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 209),
    _JuniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop_Type()
)
juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop = _JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 210),
    _JuniRadiusClientIncludeL2cActualDataRateUstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop = _JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 211),
    _JuniRadiusClientIncludeL2cActualDataRateDstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop = _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 212),
    _JuniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop = _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 213),
    _JuniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop = _JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 214),
    _JuniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop = _JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 215),
    _JuniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop = _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 216),
    _JuniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop = _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 217),
    _JuniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop = _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 218),
    _JuniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop = _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 219),
    _JuniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop = _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 220),
    _JuniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop = _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 221),
    _JuniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop = _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 222),
    _JuniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop = _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 223),
    _JuniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop_Type()
)
juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cDslLineStateInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDslLineStateInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cDslLineStateInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cDslLineStateInAcctStop = _JuniRadiusClientIncludeL2cDslLineStateInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 224),
    _JuniRadiusClientIncludeL2cDslLineStateInAcctStop_Type()
)
juniRadiusClientIncludeL2cDslLineStateInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDslLineStateInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeL2cDslTypeInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeL2cDslTypeInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeL2cDslTypeInAcctStop_Object = MibScalar
juniRadiusClientIncludeL2cDslTypeInAcctStop = _JuniRadiusClientIncludeL2cDslTypeInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 225),
    _JuniRadiusClientIncludeL2cDslTypeInAcctStop_Type()
)
juniRadiusClientIncludeL2cDslTypeInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeL2cDslTypeInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeInterfaceIdInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeInterfaceIdInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeInterfaceIdInAcctStart_Object = MibScalar
juniRadiusClientIncludeInterfaceIdInAcctStart = _JuniRadiusClientIncludeInterfaceIdInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 226),
    _JuniRadiusClientIncludeInterfaceIdInAcctStart_Type()
)
juniRadiusClientIncludeInterfaceIdInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeInterfaceIdInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeIpv6PrefixInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6PrefixInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIpv6PrefixInAcctStart_Object = MibScalar
juniRadiusClientIncludeIpv6PrefixInAcctStart = _JuniRadiusClientIncludeIpv6PrefixInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 227),
    _JuniRadiusClientIncludeIpv6PrefixInAcctStart_Type()
)
juniRadiusClientIncludeIpv6PrefixInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6PrefixInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeInterfaceIdInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeInterfaceIdInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeInterfaceIdInAcctStop_Object = MibScalar
juniRadiusClientIncludeInterfaceIdInAcctStop = _JuniRadiusClientIncludeInterfaceIdInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 228),
    _JuniRadiusClientIncludeInterfaceIdInAcctStop_Type()
)
juniRadiusClientIncludeInterfaceIdInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeInterfaceIdInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIpAddrInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpAddrInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpAddrInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpAddrInAcctStop = _JuniRadiusClientIncludeIpAddrInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 229),
    _JuniRadiusClientIncludeIpAddrInAcctStop_Type()
)
juniRadiusClientIncludeIpAddrInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpAddrInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIpv6PrefixInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6PrefixInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpv6PrefixInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpv6PrefixInAcctStop = _JuniRadiusClientIncludeIpv6PrefixInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 230),
    _JuniRadiusClientIncludeIpv6PrefixInAcctStop_Type()
)
juniRadiusClientIncludeIpv6PrefixInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6PrefixInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq_Object = MibScalar
juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq = _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 231),
    _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq_Type()
)
juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq_Type(TruthValue):
    """Custom type juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq based on TruthValue"""


_JuniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq_Object = MibScalar
juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq = _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 232),
    _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq_Type()
)
juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq.setStatus("current")


class _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart_Object = MibScalar
juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart = _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 233),
    _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart_Type()
)
juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart_Object = MibScalar
juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart = _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 234),
    _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart_Type()
)
juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop_Object = MibScalar
juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop = _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 235),
    _JuniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop_Type()
)
juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop_Object = MibScalar
juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop = _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 236),
    _JuniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop_Type()
)
juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop.setStatus("current")


class _JuniRadiusClientIgnorePppoeMaxSession_Type(TruthValue):
    """Custom type juniRadiusClientIgnorePppoeMaxSession based on TruthValue"""


_JuniRadiusClientIgnorePppoeMaxSession_Object = MibScalar
juniRadiusClientIgnorePppoeMaxSession = _JuniRadiusClientIgnorePppoeMaxSession_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 237),
    _JuniRadiusClientIgnorePppoeMaxSession_Type()
)
juniRadiusClientIgnorePppoeMaxSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIgnorePppoeMaxSession.setStatus("current")


class _JuniRadiusClientIncludeIpv6AccountingInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6AccountingInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpv6AccountingInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpv6AccountingInAcctStop = _JuniRadiusClientIncludeIpv6AccountingInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 238),
    _JuniRadiusClientIncludeIpv6AccountingInAcctStop_Type()
)
juniRadiusClientIncludeIpv6AccountingInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6AccountingInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart_Object = MibScalar
juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart = _JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 239),
    _JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart_Type()
)
juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop_Object = MibScalar
juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop = _JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 240),
    _JuniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop_Type()
)
juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeFramedIpv6PoolInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedIpv6PoolInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeFramedIpv6PoolInAcctStart_Object = MibScalar
juniRadiusClientIncludeFramedIpv6PoolInAcctStart = _JuniRadiusClientIncludeFramedIpv6PoolInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 241),
    _JuniRadiusClientIncludeFramedIpv6PoolInAcctStart_Type()
)
juniRadiusClientIncludeFramedIpv6PoolInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedIpv6PoolInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeFramedIpv6PoolInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedIpv6PoolInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeFramedIpv6PoolInAcctStop_Object = MibScalar
juniRadiusClientIncludeFramedIpv6PoolInAcctStop = _JuniRadiusClientIncludeFramedIpv6PoolInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 242),
    _JuniRadiusClientIncludeFramedIpv6PoolInAcctStop_Type()
)
juniRadiusClientIncludeFramedIpv6PoolInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedIpv6PoolInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeFramedIpv6RouteInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedIpv6RouteInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeFramedIpv6RouteInAcctStart_Object = MibScalar
juniRadiusClientIncludeFramedIpv6RouteInAcctStart = _JuniRadiusClientIncludeFramedIpv6RouteInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 243),
    _JuniRadiusClientIncludeFramedIpv6RouteInAcctStart_Type()
)
juniRadiusClientIncludeFramedIpv6RouteInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedIpv6RouteInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeFramedIpv6RouteInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeFramedIpv6RouteInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeFramedIpv6RouteInAcctStop_Object = MibScalar
juniRadiusClientIncludeFramedIpv6RouteInAcctStop = _JuniRadiusClientIncludeFramedIpv6RouteInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 244),
    _JuniRadiusClientIncludeFramedIpv6RouteInAcctStop_Type()
)
juniRadiusClientIncludeFramedIpv6RouteInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeFramedIpv6RouteInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6LocalInterfaceInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStart_Object = MibScalar
juniRadiusClientIncludeIpv6LocalInterfaceInAcctStart = _JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 245),
    _JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStart_Type()
)
juniRadiusClientIncludeIpv6LocalInterfaceInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6LocalInterfaceInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6LocalInterfaceInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpv6LocalInterfaceInAcctStop = _JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 246),
    _JuniRadiusClientIncludeIpv6LocalInterfaceInAcctStop_Type()
)
juniRadiusClientIncludeIpv6LocalInterfaceInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6LocalInterfaceInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6NdRaPrefixInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStart_Object = MibScalar
juniRadiusClientIncludeIpv6NdRaPrefixInAcctStart = _JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 247),
    _JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStart_Type()
)
juniRadiusClientIncludeIpv6NdRaPrefixInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6NdRaPrefixInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6NdRaPrefixInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpv6NdRaPrefixInAcctStop = _JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 248),
    _JuniRadiusClientIncludeIpv6NdRaPrefixInAcctStop_Type()
)
juniRadiusClientIncludeIpv6NdRaPrefixInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6NdRaPrefixInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6PrimaryDnsInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStart_Object = MibScalar
juniRadiusClientIncludeIpv6PrimaryDnsInAcctStart = _JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 249),
    _JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStart_Type()
)
juniRadiusClientIncludeIpv6PrimaryDnsInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6PrimaryDnsInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6PrimaryDnsInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpv6PrimaryDnsInAcctStop = _JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 250),
    _JuniRadiusClientIncludeIpv6PrimaryDnsInAcctStop_Type()
)
juniRadiusClientIncludeIpv6PrimaryDnsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6PrimaryDnsInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6SecondaryDnsInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStart_Object = MibScalar
juniRadiusClientIncludeIpv6SecondaryDnsInAcctStart = _JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 251),
    _JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStart_Type()
)
juniRadiusClientIncludeIpv6SecondaryDnsInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6SecondaryDnsInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6SecondaryDnsInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpv6SecondaryDnsInAcctStop = _JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 252),
    _JuniRadiusClientIncludeIpv6SecondaryDnsInAcctStop_Type()
)
juniRadiusClientIncludeIpv6SecondaryDnsInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6SecondaryDnsInAcctStop.setStatus("current")


class _JuniRadiusClientIncludeIpv6VirtualRouterInAcctStart_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6VirtualRouterInAcctStart based on TruthValue"""


_JuniRadiusClientIncludeIpv6VirtualRouterInAcctStart_Object = MibScalar
juniRadiusClientIncludeIpv6VirtualRouterInAcctStart = _JuniRadiusClientIncludeIpv6VirtualRouterInAcctStart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 253),
    _JuniRadiusClientIncludeIpv6VirtualRouterInAcctStart_Type()
)
juniRadiusClientIncludeIpv6VirtualRouterInAcctStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6VirtualRouterInAcctStart.setStatus("current")


class _JuniRadiusClientIncludeIpv6VirtualRouterInAcctStop_Type(TruthValue):
    """Custom type juniRadiusClientIncludeIpv6VirtualRouterInAcctStop based on TruthValue"""


_JuniRadiusClientIncludeIpv6VirtualRouterInAcctStop_Object = MibScalar
juniRadiusClientIncludeIpv6VirtualRouterInAcctStop = _JuniRadiusClientIncludeIpv6VirtualRouterInAcctStop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 1, 254),
    _JuniRadiusClientIncludeIpv6VirtualRouterInAcctStop_Type()
)
juniRadiusClientIncludeIpv6VirtualRouterInAcctStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRadiusClientIncludeIpv6VirtualRouterInAcctStop.setStatus("current")
_JuniRadiusAuthClient_ObjectIdentity = ObjectIdentity
juniRadiusAuthClient = _JuniRadiusAuthClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2)
)
_JuniRadiusAuthClientInvalidServerAddresses_Type = Counter32
_JuniRadiusAuthClientInvalidServerAddresses_Object = MibScalar
juniRadiusAuthClientInvalidServerAddresses = _JuniRadiusAuthClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 1),
    _JuniRadiusAuthClientInvalidServerAddresses_Type()
)
juniRadiusAuthClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientInvalidServerAddresses.setStatus("current")
_JuniRadiusAuthClientServerTable_Object = MibTable
juniRadiusAuthClientServerTable = _JuniRadiusAuthClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientServerTable.setStatus("current")
_JuniRadiusAuthClientServerEntry_Object = MibTableRow
juniRadiusAuthClientServerEntry = _JuniRadiusAuthClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1)
)
juniRadiusAuthClientServerEntry.setIndexNames(
    (0, "Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientServerAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientServerEntry.setStatus("current")
_JuniRadiusAuthClientServerAddress_Type = IpAddress
_JuniRadiusAuthClientServerAddress_Object = MibTableColumn
juniRadiusAuthClientServerAddress = _JuniRadiusAuthClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 1),
    _JuniRadiusAuthClientServerAddress_Type()
)
juniRadiusAuthClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAuthClientServerAddress.setStatus("current")
_JuniRadiusAuthClientServerPortNumber_Type = Integer32
_JuniRadiusAuthClientServerPortNumber_Object = MibTableColumn
juniRadiusAuthClientServerPortNumber = _JuniRadiusAuthClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 2),
    _JuniRadiusAuthClientServerPortNumber_Type()
)
juniRadiusAuthClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientServerPortNumber.setStatus("current")
_JuniRadiusAuthClientRoundTripTime_Type = TimeTicks
_JuniRadiusAuthClientRoundTripTime_Object = MibTableColumn
juniRadiusAuthClientRoundTripTime = _JuniRadiusAuthClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 3),
    _JuniRadiusAuthClientRoundTripTime_Type()
)
juniRadiusAuthClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientRoundTripTime.setStatus("current")
_JuniRadiusAuthClientAccessRequests_Type = Counter32
_JuniRadiusAuthClientAccessRequests_Object = MibTableColumn
juniRadiusAuthClientAccessRequests = _JuniRadiusAuthClientAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 4),
    _JuniRadiusAuthClientAccessRequests_Type()
)
juniRadiusAuthClientAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientAccessRequests.setStatus("current")
_JuniRadiusAuthClientAccessRetransmissions_Type = Counter32
_JuniRadiusAuthClientAccessRetransmissions_Object = MibTableColumn
juniRadiusAuthClientAccessRetransmissions = _JuniRadiusAuthClientAccessRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 5),
    _JuniRadiusAuthClientAccessRetransmissions_Type()
)
juniRadiusAuthClientAccessRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientAccessRetransmissions.setStatus("current")
_JuniRadiusAuthClientAccessAccepts_Type = Counter32
_JuniRadiusAuthClientAccessAccepts_Object = MibTableColumn
juniRadiusAuthClientAccessAccepts = _JuniRadiusAuthClientAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 6),
    _JuniRadiusAuthClientAccessAccepts_Type()
)
juniRadiusAuthClientAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientAccessAccepts.setStatus("current")
_JuniRadiusAuthClientAccessRejects_Type = Counter32
_JuniRadiusAuthClientAccessRejects_Object = MibTableColumn
juniRadiusAuthClientAccessRejects = _JuniRadiusAuthClientAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 7),
    _JuniRadiusAuthClientAccessRejects_Type()
)
juniRadiusAuthClientAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientAccessRejects.setStatus("current")
_JuniRadiusAuthClientAccessChallenges_Type = Counter32
_JuniRadiusAuthClientAccessChallenges_Object = MibTableColumn
juniRadiusAuthClientAccessChallenges = _JuniRadiusAuthClientAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 8),
    _JuniRadiusAuthClientAccessChallenges_Type()
)
juniRadiusAuthClientAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientAccessChallenges.setStatus("current")
_JuniRadiusAuthClientMalformedAccessResponses_Type = Counter32
_JuniRadiusAuthClientMalformedAccessResponses_Object = MibTableColumn
juniRadiusAuthClientMalformedAccessResponses = _JuniRadiusAuthClientMalformedAccessResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 9),
    _JuniRadiusAuthClientMalformedAccessResponses_Type()
)
juniRadiusAuthClientMalformedAccessResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientMalformedAccessResponses.setStatus("current")
_JuniRadiusAuthClientBadAuthenticators_Type = Counter32
_JuniRadiusAuthClientBadAuthenticators_Object = MibTableColumn
juniRadiusAuthClientBadAuthenticators = _JuniRadiusAuthClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 10),
    _JuniRadiusAuthClientBadAuthenticators_Type()
)
juniRadiusAuthClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientBadAuthenticators.setStatus("current")
_JuniRadiusAuthClientPendingRequests_Type = Gauge32
_JuniRadiusAuthClientPendingRequests_Object = MibTableColumn
juniRadiusAuthClientPendingRequests = _JuniRadiusAuthClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 11),
    _JuniRadiusAuthClientPendingRequests_Type()
)
juniRadiusAuthClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientPendingRequests.setStatus("current")
_JuniRadiusAuthClientTimeouts_Type = Counter32
_JuniRadiusAuthClientTimeouts_Object = MibTableColumn
juniRadiusAuthClientTimeouts = _JuniRadiusAuthClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 12),
    _JuniRadiusAuthClientTimeouts_Type()
)
juniRadiusAuthClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientTimeouts.setStatus("current")
_JuniRadiusAuthClientUnknownTypes_Type = Counter32
_JuniRadiusAuthClientUnknownTypes_Object = MibTableColumn
juniRadiusAuthClientUnknownTypes = _JuniRadiusAuthClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 13),
    _JuniRadiusAuthClientUnknownTypes_Type()
)
juniRadiusAuthClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientUnknownTypes.setStatus("current")
_JuniRadiusAuthClientPacketsDropped_Type = Counter32
_JuniRadiusAuthClientPacketsDropped_Object = MibTableColumn
juniRadiusAuthClientPacketsDropped = _JuniRadiusAuthClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 2, 1, 14),
    _JuniRadiusAuthClientPacketsDropped_Type()
)
juniRadiusAuthClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientPacketsDropped.setStatus("current")
_JuniRadiusAuthClientCfgServerTable_Object = MibTable
juniRadiusAuthClientCfgServerTable = _JuniRadiusAuthClientCfgServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgServerTable.setStatus("current")
_JuniRadiusAuthClientCfgServerEntry_Object = MibTableRow
juniRadiusAuthClientCfgServerEntry = _JuniRadiusAuthClientCfgServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1)
)
juniRadiusAuthClientCfgServerEntry.setIndexNames(
    (0, "Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgServerAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgServerEntry.setStatus("current")
_JuniRadiusAuthClientCfgServerAddress_Type = IpAddress
_JuniRadiusAuthClientCfgServerAddress_Object = MibTableColumn
juniRadiusAuthClientCfgServerAddress = _JuniRadiusAuthClientCfgServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 1),
    _JuniRadiusAuthClientCfgServerAddress_Type()
)
juniRadiusAuthClientCfgServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgServerAddress.setStatus("current")


class _JuniRadiusAuthClientCfgServerPortNumber_Type(Integer32):
    """Custom type juniRadiusAuthClientCfgServerPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniRadiusAuthClientCfgServerPortNumber_Type.__name__ = "Integer32"
_JuniRadiusAuthClientCfgServerPortNumber_Object = MibTableColumn
juniRadiusAuthClientCfgServerPortNumber = _JuniRadiusAuthClientCfgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 2),
    _JuniRadiusAuthClientCfgServerPortNumber_Type()
)
juniRadiusAuthClientCfgServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgServerPortNumber.setStatus("current")


class _JuniRadiusAuthClientCfgKey_Type(DisplayString):
    """Custom type juniRadiusAuthClientCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniRadiusAuthClientCfgKey_Type.__name__ = "DisplayString"
_JuniRadiusAuthClientCfgKey_Object = MibTableColumn
juniRadiusAuthClientCfgKey = _JuniRadiusAuthClientCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 3),
    _JuniRadiusAuthClientCfgKey_Type()
)
juniRadiusAuthClientCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgKey.setStatus("current")


class _JuniRadiusAuthClientCfgTimeoutInterval_Type(Integer32):
    """Custom type juniRadiusAuthClientCfgTimeoutInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JuniRadiusAuthClientCfgTimeoutInterval_Type.__name__ = "Integer32"
_JuniRadiusAuthClientCfgTimeoutInterval_Object = MibTableColumn
juniRadiusAuthClientCfgTimeoutInterval = _JuniRadiusAuthClientCfgTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 4),
    _JuniRadiusAuthClientCfgTimeoutInterval_Type()
)
juniRadiusAuthClientCfgTimeoutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgTimeoutInterval.setUnits("seconds")


class _JuniRadiusAuthClientCfgRetries_Type(Integer32):
    """Custom type juniRadiusAuthClientCfgRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniRadiusAuthClientCfgRetries_Type.__name__ = "Integer32"
_JuniRadiusAuthClientCfgRetries_Object = MibTableColumn
juniRadiusAuthClientCfgRetries = _JuniRadiusAuthClientCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 5),
    _JuniRadiusAuthClientCfgRetries_Type()
)
juniRadiusAuthClientCfgRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgRetries.setStatus("current")


class _JuniRadiusAuthClientCfgMaxPendingRequests_Type(Integer32):
    """Custom type juniRadiusAuthClientCfgMaxPendingRequests based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 32000),
    )


_JuniRadiusAuthClientCfgMaxPendingRequests_Type.__name__ = "Integer32"
_JuniRadiusAuthClientCfgMaxPendingRequests_Object = MibTableColumn
juniRadiusAuthClientCfgMaxPendingRequests = _JuniRadiusAuthClientCfgMaxPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 6),
    _JuniRadiusAuthClientCfgMaxPendingRequests_Type()
)
juniRadiusAuthClientCfgMaxPendingRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgMaxPendingRequests.setStatus("current")
_JuniRadiusAuthClientCfgRowStatus_Type = RowStatus
_JuniRadiusAuthClientCfgRowStatus_Object = MibTableColumn
juniRadiusAuthClientCfgRowStatus = _JuniRadiusAuthClientCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 7),
    _JuniRadiusAuthClientCfgRowStatus_Type()
)
juniRadiusAuthClientCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgRowStatus.setStatus("current")


class _JuniRadiusAuthClientCfgPrecedence_Type(Integer32):
    """Custom type juniRadiusAuthClientCfgPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniRadiusAuthClientCfgPrecedence_Type.__name__ = "Integer32"
_JuniRadiusAuthClientCfgPrecedence_Object = MibTableColumn
juniRadiusAuthClientCfgPrecedence = _JuniRadiusAuthClientCfgPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 8),
    _JuniRadiusAuthClientCfgPrecedence_Type()
)
juniRadiusAuthClientCfgPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgPrecedence.setStatus("current")


class _JuniRadiusAuthClientCfgDeadTime_Type(Integer32):
    """Custom type juniRadiusAuthClientCfgDeadTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_JuniRadiusAuthClientCfgDeadTime_Type.__name__ = "Integer32"
_JuniRadiusAuthClientCfgDeadTime_Object = MibTableColumn
juniRadiusAuthClientCfgDeadTime = _JuniRadiusAuthClientCfgDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 2, 3, 1, 9),
    _JuniRadiusAuthClientCfgDeadTime_Type()
)
juniRadiusAuthClientCfgDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    juniRadiusAuthClientCfgDeadTime.setUnits("minutes")
_JuniRadiusAcctClient_ObjectIdentity = ObjectIdentity
juniRadiusAcctClient = _JuniRadiusAcctClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3)
)
_JuniRadiusAcctClientInvalidServerAddresses_Type = Counter32
_JuniRadiusAcctClientInvalidServerAddresses_Object = MibScalar
juniRadiusAcctClientInvalidServerAddresses = _JuniRadiusAcctClientInvalidServerAddresses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 1),
    _JuniRadiusAcctClientInvalidServerAddresses_Type()
)
juniRadiusAcctClientInvalidServerAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientInvalidServerAddresses.setStatus("current")
_JuniRadiusAcctClientServerTable_Object = MibTable
juniRadiusAcctClientServerTable = _JuniRadiusAcctClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientServerTable.setStatus("current")
_JuniRadiusAcctClientServerEntry_Object = MibTableRow
juniRadiusAcctClientServerEntry = _JuniRadiusAcctClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1)
)
juniRadiusAcctClientServerEntry.setIndexNames(
    (0, "Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientServerEntry.setStatus("current")
_JuniRadiusAcctClientServerAddress_Type = IpAddress
_JuniRadiusAcctClientServerAddress_Object = MibTableColumn
juniRadiusAcctClientServerAddress = _JuniRadiusAcctClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 1),
    _JuniRadiusAcctClientServerAddress_Type()
)
juniRadiusAcctClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAcctClientServerAddress.setStatus("current")
_JuniRadiusAcctClientServerPortNumber_Type = Integer32
_JuniRadiusAcctClientServerPortNumber_Object = MibTableColumn
juniRadiusAcctClientServerPortNumber = _JuniRadiusAcctClientServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 2),
    _JuniRadiusAcctClientServerPortNumber_Type()
)
juniRadiusAcctClientServerPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientServerPortNumber.setStatus("current")
_JuniRadiusAcctClientRoundTripTime_Type = TimeTicks
_JuniRadiusAcctClientRoundTripTime_Object = MibTableColumn
juniRadiusAcctClientRoundTripTime = _JuniRadiusAcctClientRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 3),
    _JuniRadiusAcctClientRoundTripTime_Type()
)
juniRadiusAcctClientRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientRoundTripTime.setStatus("current")
_JuniRadiusAcctClientRequests_Type = Counter32
_JuniRadiusAcctClientRequests_Object = MibTableColumn
juniRadiusAcctClientRequests = _JuniRadiusAcctClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 4),
    _JuniRadiusAcctClientRequests_Type()
)
juniRadiusAcctClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientRequests.setStatus("current")
_JuniRadiusAcctClientRetransmissions_Type = Counter32
_JuniRadiusAcctClientRetransmissions_Object = MibTableColumn
juniRadiusAcctClientRetransmissions = _JuniRadiusAcctClientRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 5),
    _JuniRadiusAcctClientRetransmissions_Type()
)
juniRadiusAcctClientRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientRetransmissions.setStatus("current")
_JuniRadiusAcctClientResponses_Type = Counter32
_JuniRadiusAcctClientResponses_Object = MibTableColumn
juniRadiusAcctClientResponses = _JuniRadiusAcctClientResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 6),
    _JuniRadiusAcctClientResponses_Type()
)
juniRadiusAcctClientResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientResponses.setStatus("current")
_JuniRadiusAcctClientMalformedResponses_Type = Counter32
_JuniRadiusAcctClientMalformedResponses_Object = MibTableColumn
juniRadiusAcctClientMalformedResponses = _JuniRadiusAcctClientMalformedResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 7),
    _JuniRadiusAcctClientMalformedResponses_Type()
)
juniRadiusAcctClientMalformedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientMalformedResponses.setStatus("current")
_JuniRadiusAcctClientBadAuthenticators_Type = Counter32
_JuniRadiusAcctClientBadAuthenticators_Object = MibTableColumn
juniRadiusAcctClientBadAuthenticators = _JuniRadiusAcctClientBadAuthenticators_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 8),
    _JuniRadiusAcctClientBadAuthenticators_Type()
)
juniRadiusAcctClientBadAuthenticators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientBadAuthenticators.setStatus("current")
_JuniRadiusAcctClientPendingRequests_Type = Gauge32
_JuniRadiusAcctClientPendingRequests_Object = MibTableColumn
juniRadiusAcctClientPendingRequests = _JuniRadiusAcctClientPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 9),
    _JuniRadiusAcctClientPendingRequests_Type()
)
juniRadiusAcctClientPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientPendingRequests.setStatus("current")
_JuniRadiusAcctClientTimeouts_Type = Counter32
_JuniRadiusAcctClientTimeouts_Object = MibTableColumn
juniRadiusAcctClientTimeouts = _JuniRadiusAcctClientTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 10),
    _JuniRadiusAcctClientTimeouts_Type()
)
juniRadiusAcctClientTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientTimeouts.setStatus("current")
_JuniRadiusAcctClientUnknownTypes_Type = Counter32
_JuniRadiusAcctClientUnknownTypes_Object = MibTableColumn
juniRadiusAcctClientUnknownTypes = _JuniRadiusAcctClientUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 11),
    _JuniRadiusAcctClientUnknownTypes_Type()
)
juniRadiusAcctClientUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientUnknownTypes.setStatus("current")
_JuniRadiusAcctClientPacketsDropped_Type = Counter32
_JuniRadiusAcctClientPacketsDropped_Object = MibTableColumn
juniRadiusAcctClientPacketsDropped = _JuniRadiusAcctClientPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 12),
    _JuniRadiusAcctClientPacketsDropped_Type()
)
juniRadiusAcctClientPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientPacketsDropped.setStatus("current")
_JuniRadiusAcctClientStartRequests_Type = Counter32
_JuniRadiusAcctClientStartRequests_Object = MibTableColumn
juniRadiusAcctClientStartRequests = _JuniRadiusAcctClientStartRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 13),
    _JuniRadiusAcctClientStartRequests_Type()
)
juniRadiusAcctClientStartRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientStartRequests.setStatus("current")
_JuniRadiusAcctClientInterimRequests_Type = Counter32
_JuniRadiusAcctClientInterimRequests_Object = MibTableColumn
juniRadiusAcctClientInterimRequests = _JuniRadiusAcctClientInterimRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 14),
    _JuniRadiusAcctClientInterimRequests_Type()
)
juniRadiusAcctClientInterimRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientInterimRequests.setStatus("current")
_JuniRadiusAcctClientStopRequests_Type = Counter32
_JuniRadiusAcctClientStopRequests_Object = MibTableColumn
juniRadiusAcctClientStopRequests = _JuniRadiusAcctClientStopRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 15),
    _JuniRadiusAcctClientStopRequests_Type()
)
juniRadiusAcctClientStopRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientStopRequests.setStatus("current")
_JuniRadiusAcctClientStartResponses_Type = Counter32
_JuniRadiusAcctClientStartResponses_Object = MibTableColumn
juniRadiusAcctClientStartResponses = _JuniRadiusAcctClientStartResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 16),
    _JuniRadiusAcctClientStartResponses_Type()
)
juniRadiusAcctClientStartResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientStartResponses.setStatus("current")
_JuniRadiusAcctClientInterimResponses_Type = Counter32
_JuniRadiusAcctClientInterimResponses_Object = MibTableColumn
juniRadiusAcctClientInterimResponses = _JuniRadiusAcctClientInterimResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 17),
    _JuniRadiusAcctClientInterimResponses_Type()
)
juniRadiusAcctClientInterimResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientInterimResponses.setStatus("current")
_JuniRadiusAcctClientStopResponses_Type = Counter32
_JuniRadiusAcctClientStopResponses_Object = MibTableColumn
juniRadiusAcctClientStopResponses = _JuniRadiusAcctClientStopResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 18),
    _JuniRadiusAcctClientStopResponses_Type()
)
juniRadiusAcctClientStopResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientStopResponses.setStatus("current")
_JuniRadiusAcctClientRejectRequests_Type = Counter32
_JuniRadiusAcctClientRejectRequests_Object = MibTableColumn
juniRadiusAcctClientRejectRequests = _JuniRadiusAcctClientRejectRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 19),
    _JuniRadiusAcctClientRejectRequests_Type()
)
juniRadiusAcctClientRejectRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientRejectRequests.setStatus("current")
_JuniRadiusAcctClientRejectResponses_Type = Counter32
_JuniRadiusAcctClientRejectResponses_Object = MibTableColumn
juniRadiusAcctClientRejectResponses = _JuniRadiusAcctClientRejectResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 2, 1, 20),
    _JuniRadiusAcctClientRejectResponses_Type()
)
juniRadiusAcctClientRejectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientRejectResponses.setStatus("current")
_JuniRadiusAcctClientCfgServerTable_Object = MibTable
juniRadiusAcctClientCfgServerTable = _JuniRadiusAcctClientCfgServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgServerTable.setStatus("current")
_JuniRadiusAcctClientCfgServerEntry_Object = MibTableRow
juniRadiusAcctClientCfgServerEntry = _JuniRadiusAcctClientCfgServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1)
)
juniRadiusAcctClientCfgServerEntry.setIndexNames(
    (0, "Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgServerAddress"),
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgServerEntry.setStatus("current")
_JuniRadiusAcctClientCfgServerAddress_Type = IpAddress
_JuniRadiusAcctClientCfgServerAddress_Object = MibTableColumn
juniRadiusAcctClientCfgServerAddress = _JuniRadiusAcctClientCfgServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 1),
    _JuniRadiusAcctClientCfgServerAddress_Type()
)
juniRadiusAcctClientCfgServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgServerAddress.setStatus("current")


class _JuniRadiusAcctClientCfgServerPortNumber_Type(Integer32):
    """Custom type juniRadiusAcctClientCfgServerPortNumber based on Integer32"""
    defaultValue = 1813

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniRadiusAcctClientCfgServerPortNumber_Type.__name__ = "Integer32"
_JuniRadiusAcctClientCfgServerPortNumber_Object = MibTableColumn
juniRadiusAcctClientCfgServerPortNumber = _JuniRadiusAcctClientCfgServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 2),
    _JuniRadiusAcctClientCfgServerPortNumber_Type()
)
juniRadiusAcctClientCfgServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgServerPortNumber.setStatus("current")


class _JuniRadiusAcctClientCfgKey_Type(DisplayString):
    """Custom type juniRadiusAcctClientCfgKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniRadiusAcctClientCfgKey_Type.__name__ = "DisplayString"
_JuniRadiusAcctClientCfgKey_Object = MibTableColumn
juniRadiusAcctClientCfgKey = _JuniRadiusAcctClientCfgKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 3),
    _JuniRadiusAcctClientCfgKey_Type()
)
juniRadiusAcctClientCfgKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgKey.setStatus("current")


class _JuniRadiusAcctClientCfgTimeoutInterval_Type(Integer32):
    """Custom type juniRadiusAcctClientCfgTimeoutInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JuniRadiusAcctClientCfgTimeoutInterval_Type.__name__ = "Integer32"
_JuniRadiusAcctClientCfgTimeoutInterval_Object = MibTableColumn
juniRadiusAcctClientCfgTimeoutInterval = _JuniRadiusAcctClientCfgTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 4),
    _JuniRadiusAcctClientCfgTimeoutInterval_Type()
)
juniRadiusAcctClientCfgTimeoutInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgTimeoutInterval.setUnits("seconds")


class _JuniRadiusAcctClientCfgRetries_Type(Integer32):
    """Custom type juniRadiusAcctClientCfgRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniRadiusAcctClientCfgRetries_Type.__name__ = "Integer32"
_JuniRadiusAcctClientCfgRetries_Object = MibTableColumn
juniRadiusAcctClientCfgRetries = _JuniRadiusAcctClientCfgRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 5),
    _JuniRadiusAcctClientCfgRetries_Type()
)
juniRadiusAcctClientCfgRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgRetries.setStatus("current")


class _JuniRadiusAcctClientCfgMaxPendingRequests_Type(Integer32):
    """Custom type juniRadiusAcctClientCfgMaxPendingRequests based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 96000),
    )


_JuniRadiusAcctClientCfgMaxPendingRequests_Type.__name__ = "Integer32"
_JuniRadiusAcctClientCfgMaxPendingRequests_Object = MibTableColumn
juniRadiusAcctClientCfgMaxPendingRequests = _JuniRadiusAcctClientCfgMaxPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 6),
    _JuniRadiusAcctClientCfgMaxPendingRequests_Type()
)
juniRadiusAcctClientCfgMaxPendingRequests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgMaxPendingRequests.setStatus("current")
_JuniRadiusAcctClientCfgRowStatus_Type = RowStatus
_JuniRadiusAcctClientCfgRowStatus_Object = MibTableColumn
juniRadiusAcctClientCfgRowStatus = _JuniRadiusAcctClientCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 7),
    _JuniRadiusAcctClientCfgRowStatus_Type()
)
juniRadiusAcctClientCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgRowStatus.setStatus("current")


class _JuniRadiusAcctClientCfgPrecedence_Type(Integer32):
    """Custom type juniRadiusAcctClientCfgPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniRadiusAcctClientCfgPrecedence_Type.__name__ = "Integer32"
_JuniRadiusAcctClientCfgPrecedence_Object = MibTableColumn
juniRadiusAcctClientCfgPrecedence = _JuniRadiusAcctClientCfgPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 8),
    _JuniRadiusAcctClientCfgPrecedence_Type()
)
juniRadiusAcctClientCfgPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgPrecedence.setStatus("current")


class _JuniRadiusAcctClientCfgDeadTime_Type(Integer32):
    """Custom type juniRadiusAcctClientCfgDeadTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_JuniRadiusAcctClientCfgDeadTime_Type.__name__ = "Integer32"
_JuniRadiusAcctClientCfgDeadTime_Object = MibTableColumn
juniRadiusAcctClientCfgDeadTime = _JuniRadiusAcctClientCfgDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 1, 3, 3, 1, 9),
    _JuniRadiusAcctClientCfgDeadTime_Type()
)
juniRadiusAcctClientCfgDeadTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    juniRadiusAcctClientCfgDeadTime.setUnits("minutes")
_JuniRadiusClientMIBConformance_ObjectIdentity = ObjectIdentity
juniRadiusClientMIBConformance = _JuniRadiusClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2)
)
_JuniRadiusClientMIBCompliances_ObjectIdentity = ObjectIdentity
juniRadiusClientMIBCompliances = _JuniRadiusClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1)
)
_JuniRadiusClientMIBGroups_ObjectIdentity = ObjectIdentity
juniRadiusClientMIBGroups = _JuniRadiusClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2)
)
_JuniRadiusClientTraps_ObjectIdentity = ObjectIdentity
juniRadiusClientTraps = _JuniRadiusClientTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3)
)
_JuniRadiusClientTrapPrefix_ObjectIdentity = ObjectIdentity
juniRadiusClientTrapPrefix = _JuniRadiusClientTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3, 0)
)
_JuniRadiusClientTrapControl_ObjectIdentity = ObjectIdentity
juniRadiusClientTrapControl = _JuniRadiusClientTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 4)
)
_JuniRadiusAuthClientUnavailableServer_Type = IpAddress
_JuniRadiusAuthClientUnavailableServer_Object = MibScalar
juniRadiusAuthClientUnavailableServer = _JuniRadiusAuthClientUnavailableServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 4, 1),
    _JuniRadiusAuthClientUnavailableServer_Type()
)
juniRadiusAuthClientUnavailableServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniRadiusAuthClientUnavailableServer.setStatus("current")
_JuniRadiusAuthClientNextAvailableServer_Type = IpAddress
_JuniRadiusAuthClientNextAvailableServer_Object = MibScalar
juniRadiusAuthClientNextAvailableServer = _JuniRadiusAuthClientNextAvailableServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 4, 2),
    _JuniRadiusAuthClientNextAvailableServer_Type()
)
juniRadiusAuthClientNextAvailableServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniRadiusAuthClientNextAvailableServer.setStatus("current")
_JuniRadiusAcctClientUnavailableServer_Type = IpAddress
_JuniRadiusAcctClientUnavailableServer_Object = MibScalar
juniRadiusAcctClientUnavailableServer = _JuniRadiusAcctClientUnavailableServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 4, 3),
    _JuniRadiusAcctClientUnavailableServer_Type()
)
juniRadiusAcctClientUnavailableServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniRadiusAcctClientUnavailableServer.setStatus("current")
_JuniRadiusAcctClientNextAvailableServer_Type = IpAddress
_JuniRadiusAcctClientNextAvailableServer_Object = MibScalar
juniRadiusAcctClientNextAvailableServer = _JuniRadiusAcctClientNextAvailableServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 4, 4),
    _JuniRadiusAcctClientNextAvailableServer_Type()
)
juniRadiusAcctClientNextAvailableServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniRadiusAcctClientNextAvailableServer.setStatus("current")
_JuniRadiusAuthClientAvailableServer_Type = IpAddress
_JuniRadiusAuthClientAvailableServer_Object = MibScalar
juniRadiusAuthClientAvailableServer = _JuniRadiusAuthClientAvailableServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 4, 5),
    _JuniRadiusAuthClientAvailableServer_Type()
)
juniRadiusAuthClientAvailableServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniRadiusAuthClientAvailableServer.setStatus("current")
_JuniRadiusAcctClientAvailableServer_Type = IpAddress
_JuniRadiusAcctClientAvailableServer_Object = MibScalar
juniRadiusAcctClientAvailableServer = _JuniRadiusAcctClientAvailableServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 4, 6),
    _JuniRadiusAcctClientAvailableServer_Type()
)
juniRadiusAcctClientAvailableServer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniRadiusAcctClientAvailableServer.setStatus("current")

# Managed Objects groups

juniRadiusGeneralClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 1)
)
juniRadiusGeneralClientGroup.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIdentifier"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAlgorithm"))
)
if mibBuilder.loadTexts:
    juniRadiusGeneralClientGroup.setStatus("obsolete")

juniRadiusAuthClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 2)
)
juniRadiusAuthClientGroup.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientInvalidServerAddresses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientRoundTripTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRetransmissions"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessAccepts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRejects"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessChallenges"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientMalformedAccessResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientBadAuthenticators"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientTimeouts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientUnknownTypes"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientPacketsDropped"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgKey"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgTimeoutInterval"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgRetries"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgMaxPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgRowStatus"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgPrecedence"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgDeadTime"))
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientGroup.setStatus("obsolete")

juniRadiusAcctClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 3)
)
juniRadiusAcctClientGroup.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInvalidServerAddresses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRoundTripTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRetransmissions"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientMalformedResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientBadAuthenticators"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientTimeouts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnknownTypes"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPacketsDropped"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgKey"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgTimeoutInterval"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRetries"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgMaxPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRowStatus"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgPrecedence"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgDeadTime"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientGroup.setStatus("obsolete")

juniRadiusGeneralClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 4)
)
juniRadiusGeneralClientGroup2.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIdentifier"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAlgorithm"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientSourceAddress"))
)
if mibBuilder.loadTexts:
    juniRadiusGeneralClientGroup2.setStatus("obsolete")

juniRadiusBasicClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 5)
)
juniRadiusBasicClientGroup.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIdentifier"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAlgorithm"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientSourceAddress"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientUdpChecksum"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIdentifier"))
)
if mibBuilder.loadTexts:
    juniRadiusBasicClientGroup.setStatus("obsolete")

juniRadiusBrasClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 6)
)
juniRadiusBrasClientGroup.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup.setStatus("obsolete")

juniRadiusTunnelClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 7)
)
juniRadiusTunnelClientGroup.setObjects(
    ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTunnelAccounting")
)
if mibBuilder.loadTexts:
    juniRadiusTunnelClientGroup.setStatus("current")

juniRadiusBrasClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 8)
)
juniRadiusBrasClientGroup2.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup2.setStatus("obsolete")

juniRadiusBasicClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 9)
)
juniRadiusBasicClientGroup2.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIdentifier"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAlgorithm"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientSourceAddress"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientUdpChecksum"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIdentifier"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRollover"))
)
if mibBuilder.loadTexts:
    juniRadiusBasicClientGroup2.setStatus("current")

juniRadiusBrasClientGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 10)
)
juniRadiusBrasClientGroup3.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup3.setStatus("obsolete")

juniRadiusBrasClientGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 11)
)
juniRadiusBrasClientGroup4.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup4.setStatus("obsolete")

juniRadiusBrasClientGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 12)
)
juniRadiusBrasClientGroup5.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup5.setStatus("obsolete")

juniRadiusAuthClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 13)
)
juniRadiusAuthClientGroup2.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientInvalidServerAddresses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientRoundTripTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRetransmissions"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessAccepts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRejects"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessChallenges"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientMalformedAccessResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientBadAuthenticators"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientTimeouts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientUnknownTypes"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientPacketsDropped"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgKey"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgTimeoutInterval"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgRetries"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgMaxPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgRowStatus"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgPrecedence"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgDeadTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientUnavailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientNextAvailableServer"))
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientGroup2.setStatus("obsolete")

juniRadiusAcctClientGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 14)
)
juniRadiusAcctClientGroup2.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInvalidServerAddresses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRoundTripTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRetransmissions"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientMalformedResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientBadAuthenticators"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientTimeouts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnknownTypes"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPacketsDropped"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgKey"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgTimeoutInterval"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRetries"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgMaxPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRowStatus"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgPrecedence"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgDeadTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnavailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientNextAvailableServer"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientGroup2.setStatus("obsolete")

juniRadiusBrasClientGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 17)
)
juniRadiusBrasClientGroup6.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup6.setStatus("obsolete")

juniRadiusAuthClientGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 18)
)
juniRadiusAuthClientGroup3.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientInvalidServerAddresses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientRoundTripTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRetransmissions"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessAccepts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessRejects"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAccessChallenges"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientMalformedAccessResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientBadAuthenticators"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientTimeouts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientUnknownTypes"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientPacketsDropped"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgKey"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgTimeoutInterval"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgRetries"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgMaxPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgRowStatus"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgPrecedence"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientCfgDeadTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientUnavailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientNextAvailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAvailableServer"))
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientGroup3.setStatus("current")

juniRadiusAcctClientGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 19)
)
juniRadiusAcctClientGroup3.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInvalidServerAddresses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRoundTripTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStartRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInterimRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStopRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRetransmissions"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStartResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInterimResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStopResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientMalformedResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientBadAuthenticators"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientTimeouts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnknownTypes"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPacketsDropped"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgKey"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgTimeoutInterval"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRetries"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgMaxPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRowStatus"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgPrecedence"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgDeadTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnavailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientNextAvailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientAvailableServer"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientGroup3.setStatus("obsolete")

juniRadiusBrasClientGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 22)
)
juniRadiusBrasClientGroup7.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup7.setStatus("obsolete")

juniRadiusAcctClientGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 23)
)
juniRadiusAcctClientGroup4.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInvalidServerAddresses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRoundTripTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStartRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInterimRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStopRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRejectRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRetransmissions"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStartResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientInterimResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientStopResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientRejectResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientMalformedResponses"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientBadAuthenticators"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientTimeouts"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnknownTypes"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientPacketsDropped"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgServerPortNumber"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgKey"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgTimeoutInterval"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRetries"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgMaxPendingRequests"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgRowStatus"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgPrecedence"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientCfgDeadTime"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnavailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientNextAvailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientAvailableServer"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientGroup4.setStatus("current")

juniRadiusBrasClientGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 24)
)
juniRadiusBrasClientGroup8.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup8.setStatus("obsolete")

juniRadiusBrasClientGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 25)
)
juniRadiusBrasClientGroup9.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup9.setStatus("obsolete")

juniRadiusBrasClientGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 26)
)
juniRadiusBrasClientGroup10.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup10.setStatus("obsolete")

juniRadiusBrasClientGroup11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 27)
)
juniRadiusBrasClientGroup11.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup11.setStatus("obsolete")

juniRadiusBrasClientGroup12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 28)
)
juniRadiusBrasClientGroup12.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup12.setStatus("obsolete")

juniRadiusBrasClientGroup13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 29)
)
juniRadiusBrasClientGroup13.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup13.setStatus("obsolete")

juniRadiusBrasClientGroup14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 30)
)
juniRadiusBrasClientGroup14.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup14.setStatus("obsolete")

juniRadiusBrasClientGroup15 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 31)
)
juniRadiusBrasClientGroup15.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup15.setStatus("obsolete")

juniRadiusBrasClientGroup16 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 32)
)
juniRadiusBrasClientGroup16.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup16.setStatus("obsolete")

juniRadiusBrasClientGroup17 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 33)
)
juniRadiusBrasClientGroup17.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup17.setStatus("obsolete")

juniRadiusBrasClientGroup18 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 34)
)
juniRadiusBrasClientGroup18.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnorePppoeMaxSession"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup18.setStatus("obsolete")

juniRadiusBrasClientGroup19 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 35)
)
juniRadiusBrasClientGroup19.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnorePppoeMaxSession"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6AccountingInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup19.setStatus("obsolete")

juniRadiusBrasClientGroup20 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 36)
)
juniRadiusBrasClientGroup20.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientDslPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientAcctSessionIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientEthernetPortType"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasIpAddrUse"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCalledStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeCallingStationIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeClassInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeConnectInfoInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEgressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeEventTimestampInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedCompressionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpNetmaskInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIngressPolicyNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasIdentifierInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeNasPortTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigawordsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludePppoeDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelClientEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelMediumTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelPreferenceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAttributesInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelServerEndpointInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeOutputGigapktsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreFramedIpNetmask"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmCategory"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmMbs"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmPcr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreAtmScr"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreEgressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreIngressPolicyName"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnoreVirtualRouter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnNoAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAuthServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientTrapOnAcctServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientPppoeNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientVlanNasPortFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientConnectInfoFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeProfileServiceDescrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOn"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctAuthenticInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctDelayTimeInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctSessionIdInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeAcctTerminateCauseInAcctOff"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeMlpppBundleNameInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpOptionsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpMacAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDhcpGiAddressInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientOverrideNasInfo"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceDescriptionInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientCallingStationIdOverrideRemoteCircuitId"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVpi"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthAtmVci"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSlot"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetAdapter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetPort"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetSVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientNasPortFieldWidthEthernetVlan"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdFormat"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientRemoteCircuitIdDelimiter"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDownStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cUpStreamDataInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDslForumAttributesInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslLineStateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeL2cDslTypeInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeInterfaceIdInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpAddrInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrefixInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIgnorePppoeMaxSession"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6AccountingInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpv6PoolInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpv6PoolInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpv6RouteInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeFramedIpv6RouteInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6LocalInterfaceInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6LocalInterfaceInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6NdRaPrefixInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6NdRaPrefixInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrimaryDnsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6PrimaryDnsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6SecondaryDnsInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6SecondaryDnsInAcctStop"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6VirtualRouterInAcctStart"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusClientIncludeIpv6VirtualRouterInAcctStop"))
)
if mibBuilder.loadTexts:
    juniRadiusBrasClientGroup20.setStatus("current")


# Notification objects

juniRadiusAuthClientServerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3, 0, 1)
)
juniRadiusAuthClientServerUnavailable.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientUnavailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientNextAvailableServer"))
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientServerUnavailable.setStatus(
        "current"
    )

juniRadiusAuthClientNoServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3, 0, 2)
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientNoServerAvailable.setStatus(
        "current"
    )

juniRadiusAcctClientServerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3, 0, 3)
)
juniRadiusAcctClientServerUnavailable.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientUnavailableServer"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientNextAvailableServer"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientServerUnavailable.setStatus(
        "current"
    )

juniRadiusAcctClientNoServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3, 0, 4)
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientNoServerAvailable.setStatus(
        "current"
    )

juniRadiusAuthClientServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3, 0, 5)
)
juniRadiusAuthClientServerAvailable.setObjects(
    ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientAvailableServer")
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientServerAvailable.setStatus(
        "current"
    )

juniRadiusAcctClientServerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 3, 0, 6)
)
juniRadiusAcctClientServerAvailable.setObjects(
    ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientAvailableServer")
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientServerAvailable.setStatus(
        "current"
    )


# Notifications groups

juniRadiusAuthNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 15)
)
juniRadiusAuthNotificationGroup.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientNoServerAvailable"))
)
if mibBuilder.loadTexts:
    juniRadiusAuthNotificationGroup.setStatus(
        "obsolete"
    )

juniRadiusAcctNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 16)
)
juniRadiusAcctNotificationGroup.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientNoServerAvailable"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctNotificationGroup.setStatus(
        "obsolete"
    )

juniRadiusAuthNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 20)
)
juniRadiusAuthNotificationGroup2.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientNoServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAuthClientServerAvailable"))
)
if mibBuilder.loadTexts:
    juniRadiusAuthNotificationGroup2.setStatus(
        "current"
    )

juniRadiusAcctNotificationGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 2, 21)
)
juniRadiusAcctNotificationGroup2.setObjects(
      *(("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerUnavailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientNoServerAvailable"),
        ("Juniper-RADIUS-CLIENT-MIB", "juniRadiusAcctClientServerAvailable"))
)
if mibBuilder.loadTexts:
    juniRadiusAcctNotificationGroup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniRadiusAuthClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientCompliance.setStatus(
        "obsolete"
    )

juniRadiusAcctClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientCompliance.setStatus(
        "obsolete"
    )

juniRadiusAuthClientCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniRadiusAuthClientCompliance2.setStatus(
        "obsolete"
    )

juniRadiusAcctClientCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniRadiusAcctClientCompliance2.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance2.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 7)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance3.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 8)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance4.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 9)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance5.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 10)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance6.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 11)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance7.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 12)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance8.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 13)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance9.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 14)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance10.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 15)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance11.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 16)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance12.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 17)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance13.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 18)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance14.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 19)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance15.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 20)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance16.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 21)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance17.setStatus(
        "obsolete"
    )

juniRadiusClientCompliance18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 19, 2, 1, 22)
)
if mibBuilder.loadTexts:
    juniRadiusClientCompliance18.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-RADIUS-CLIENT-MIB",
    **{"JuniRadiusClientRemoterCircuitIdFormatComponents": JuniRadiusClientRemoterCircuitIdFormatComponents,
       "juniRadiusClientMIB": juniRadiusClientMIB,
       "juniRadiusClientObjects": juniRadiusClientObjects,
       "juniRadiusGeneralClient": juniRadiusGeneralClient,
       "juniRadiusClientIdentifier": juniRadiusClientIdentifier,
       "juniRadiusClientAlgorithm": juniRadiusClientAlgorithm,
       "juniRadiusClientSourceAddress": juniRadiusClientSourceAddress,
       "juniRadiusClientUdpChecksum": juniRadiusClientUdpChecksum,
       "juniRadiusClientNasIdentifier": juniRadiusClientNasIdentifier,
       "juniRadiusClientDslPortType": juniRadiusClientDslPortType,
       "juniRadiusClientTunnelAccounting": juniRadiusClientTunnelAccounting,
       "juniRadiusClientAcctSessionIdFormat": juniRadiusClientAcctSessionIdFormat,
       "juniRadiusClientNasPortFormat": juniRadiusClientNasPortFormat,
       "juniRadiusClientCallingStationDelimiter": juniRadiusClientCallingStationDelimiter,
       "juniRadiusClientEthernetPortType": juniRadiusClientEthernetPortType,
       "juniRadiusClientIncludeIpAddrInAcctStart": juniRadiusClientIncludeIpAddrInAcctStart,
       "juniRadiusClientIncludeAcctSessionIdInAccessReq": juniRadiusClientIncludeAcctSessionIdInAccessReq,
       "juniRadiusClientRollover": juniRadiusClientRollover,
       "juniRadiusClientCallingStationIdFormat": juniRadiusClientCallingStationIdFormat,
       "juniRadiusClientNasIpAddrUse": juniRadiusClientNasIpAddrUse,
       "juniRadiusClientIncludeAcctTunnelConnectionInAccessReq": juniRadiusClientIncludeAcctTunnelConnectionInAccessReq,
       "juniRadiusClientIncludeCalledStationIdInAccessReq": juniRadiusClientIncludeCalledStationIdInAccessReq,
       "juniRadiusClientIncludeCallingStationIdInAccessReq": juniRadiusClientIncludeCallingStationIdInAccessReq,
       "juniRadiusClientIncludeConnectInfoInAccessReq": juniRadiusClientIncludeConnectInfoInAccessReq,
       "juniRadiusClientIncludeNasIdentifierInAccessReq": juniRadiusClientIncludeNasIdentifierInAccessReq,
       "juniRadiusClientIncludeNasPortInAccessReq": juniRadiusClientIncludeNasPortInAccessReq,
       "juniRadiusClientIncludeNasPortIdInAccessReq": juniRadiusClientIncludeNasPortIdInAccessReq,
       "juniRadiusClientIncludeNasPortTypeInAccessReq": juniRadiusClientIncludeNasPortTypeInAccessReq,
       "juniRadiusClientIncludePppoeDescriptionInAccessReq": juniRadiusClientIncludePppoeDescriptionInAccessReq,
       "juniRadiusClientIncludeTunnelClientAuthIdInAccessReq": juniRadiusClientIncludeTunnelClientAuthIdInAccessReq,
       "juniRadiusClientIncludeTunnelClientEndpointInAccessReq": juniRadiusClientIncludeTunnelClientEndpointInAccessReq,
       "juniRadiusClientIncludeTunnelMediumTypeInAccessReq": juniRadiusClientIncludeTunnelMediumTypeInAccessReq,
       "juniRadiusClientIncludeTunnelServerAttributesInAccessReq": juniRadiusClientIncludeTunnelServerAttributesInAccessReq,
       "juniRadiusClientIncludeTunnelServerAuthIdInAccessReq": juniRadiusClientIncludeTunnelServerAuthIdInAccessReq,
       "juniRadiusClientIncludeTunnelServerEndpointInAccessReq": juniRadiusClientIncludeTunnelServerEndpointInAccessReq,
       "juniRadiusClientIncludeTunnelTypeInAccessReq": juniRadiusClientIncludeTunnelTypeInAccessReq,
       "juniRadiusClientIncludeAcctTunnelConnectionInAcctStart": juniRadiusClientIncludeAcctTunnelConnectionInAcctStart,
       "juniRadiusClientIncludeCalledStationIdInAcctStart": juniRadiusClientIncludeCalledStationIdInAcctStart,
       "juniRadiusClientIncludeCallingStationIdInAcctStart": juniRadiusClientIncludeCallingStationIdInAcctStart,
       "juniRadiusClientIncludeClassInAcctStart": juniRadiusClientIncludeClassInAcctStart,
       "juniRadiusClientIncludeConnectInfoInAcctStart": juniRadiusClientIncludeConnectInfoInAcctStart,
       "juniRadiusClientIncludeEgressPolicyNameInAcctStart": juniRadiusClientIncludeEgressPolicyNameInAcctStart,
       "juniRadiusClientIncludeEventTimestampInAcctStart": juniRadiusClientIncludeEventTimestampInAcctStart,
       "juniRadiusClientIncludeFramedCompressionInAcctStart": juniRadiusClientIncludeFramedCompressionInAcctStart,
       "juniRadiusClientIncludeFramedIpNetmaskInAcctStart": juniRadiusClientIncludeFramedIpNetmaskInAcctStart,
       "juniRadiusClientIncludeIngressPolicyNameInAcctStart": juniRadiusClientIncludeIngressPolicyNameInAcctStart,
       "juniRadiusClientIncludeNasIdentifierInAcctStart": juniRadiusClientIncludeNasIdentifierInAcctStart,
       "juniRadiusClientIncludeNasPortInAcctStart": juniRadiusClientIncludeNasPortInAcctStart,
       "juniRadiusClientIncludeNasPortIdInAcctStart": juniRadiusClientIncludeNasPortIdInAcctStart,
       "juniRadiusClientIncludeNasPortTypeInAcctStart": juniRadiusClientIncludeNasPortTypeInAcctStart,
       "juniRadiusClientIncludePppoeDescriptionInAcctStart": juniRadiusClientIncludePppoeDescriptionInAcctStart,
       "juniRadiusClientIncludeTunnelAssignmentIdInAcctStart": juniRadiusClientIncludeTunnelAssignmentIdInAcctStart,
       "juniRadiusClientIncludeTunnelClientAuthIdInAcctStart": juniRadiusClientIncludeTunnelClientAuthIdInAcctStart,
       "juniRadiusClientIncludeTunnelClientEndpointInAcctStart": juniRadiusClientIncludeTunnelClientEndpointInAcctStart,
       "juniRadiusClientIncludeTunnelMediumTypeInAcctStart": juniRadiusClientIncludeTunnelMediumTypeInAcctStart,
       "juniRadiusClientIncludeTunnelPreferenceInAcctStart": juniRadiusClientIncludeTunnelPreferenceInAcctStart,
       "juniRadiusClientIncludeTunnelServerAttributesInAcctStart": juniRadiusClientIncludeTunnelServerAttributesInAcctStart,
       "juniRadiusClientIncludeTunnelServerAuthIdInAcctStart": juniRadiusClientIncludeTunnelServerAuthIdInAcctStart,
       "juniRadiusClientIncludeTunnelServerEndpointInAcctStart": juniRadiusClientIncludeTunnelServerEndpointInAcctStart,
       "juniRadiusClientIncludeTunnelTypeInAcctStart": juniRadiusClientIncludeTunnelTypeInAcctStart,
       "juniRadiusClientIncludeAcctTunnelConnectionInAcctStop": juniRadiusClientIncludeAcctTunnelConnectionInAcctStop,
       "juniRadiusClientIncludeCalledStationIdInAcctStop": juniRadiusClientIncludeCalledStationIdInAcctStop,
       "juniRadiusClientIncludeCallingStationIdInAcctStop": juniRadiusClientIncludeCallingStationIdInAcctStop,
       "juniRadiusClientIncludeClassInAcctStop": juniRadiusClientIncludeClassInAcctStop,
       "juniRadiusClientIncludeConnectInfoInAcctStop": juniRadiusClientIncludeConnectInfoInAcctStop,
       "juniRadiusClientIncludeEgressPolicyNameInAcctStop": juniRadiusClientIncludeEgressPolicyNameInAcctStop,
       "juniRadiusClientIncludeEventTimestampInAcctStop": juniRadiusClientIncludeEventTimestampInAcctStop,
       "juniRadiusClientIncludeFramedCompressionInAcctStop": juniRadiusClientIncludeFramedCompressionInAcctStop,
       "juniRadiusClientIncludeFramedIpNetmaskInAcctStop": juniRadiusClientIncludeFramedIpNetmaskInAcctStop,
       "juniRadiusClientIncludeIngressPolicyNameInAcctStop": juniRadiusClientIncludeIngressPolicyNameInAcctStop,
       "juniRadiusClientIncludeInputGigawordsInAcctStop": juniRadiusClientIncludeInputGigawordsInAcctStop,
       "juniRadiusClientIncludeNasIdentifierInAcctStop": juniRadiusClientIncludeNasIdentifierInAcctStop,
       "juniRadiusClientIncludeNasPortInAcctStop": juniRadiusClientIncludeNasPortInAcctStop,
       "juniRadiusClientIncludeNasPortIdInAcctStop": juniRadiusClientIncludeNasPortIdInAcctStop,
       "juniRadiusClientIncludeNasPortTypeInAcctStop": juniRadiusClientIncludeNasPortTypeInAcctStop,
       "juniRadiusClientIncludeOutputGigawordsInAcctStop": juniRadiusClientIncludeOutputGigawordsInAcctStop,
       "juniRadiusClientIncludePppoeDescriptionInAcctStop": juniRadiusClientIncludePppoeDescriptionInAcctStop,
       "juniRadiusClientIncludeTunnelAssignmentIdInAcctStop": juniRadiusClientIncludeTunnelAssignmentIdInAcctStop,
       "juniRadiusClientIncludeTunnelClientAuthIdInAcctStop": juniRadiusClientIncludeTunnelClientAuthIdInAcctStop,
       "juniRadiusClientIncludeTunnelClientEndpointInAcctStop": juniRadiusClientIncludeTunnelClientEndpointInAcctStop,
       "juniRadiusClientIncludeTunnelMediumTypeInAcctStop": juniRadiusClientIncludeTunnelMediumTypeInAcctStop,
       "juniRadiusClientIncludeTunnelPreferenceInAcctStop": juniRadiusClientIncludeTunnelPreferenceInAcctStop,
       "juniRadiusClientIncludeTunnelServerAttributesInAcctStop": juniRadiusClientIncludeTunnelServerAttributesInAcctStop,
       "juniRadiusClientIncludeTunnelServerAuthIdInAcctStop": juniRadiusClientIncludeTunnelServerAuthIdInAcctStop,
       "juniRadiusClientIncludeTunnelServerEndpointInAcctStop": juniRadiusClientIncludeTunnelServerEndpointInAcctStop,
       "juniRadiusClientIncludeTunnelTypeInAcctStop": juniRadiusClientIncludeTunnelTypeInAcctStop,
       "juniRadiusClientIncludeInputGigapktsInAcctStop": juniRadiusClientIncludeInputGigapktsInAcctStop,
       "juniRadiusClientIncludeOutputGigapktsInAcctStop": juniRadiusClientIncludeOutputGigapktsInAcctStop,
       "juniRadiusClientIgnoreFramedIpNetmask": juniRadiusClientIgnoreFramedIpNetmask,
       "juniRadiusClientIgnoreAtmCategory": juniRadiusClientIgnoreAtmCategory,
       "juniRadiusClientIgnoreAtmMbs": juniRadiusClientIgnoreAtmMbs,
       "juniRadiusClientIgnoreAtmPcr": juniRadiusClientIgnoreAtmPcr,
       "juniRadiusClientIgnoreAtmScr": juniRadiusClientIgnoreAtmScr,
       "juniRadiusClientIgnoreEgressPolicyName": juniRadiusClientIgnoreEgressPolicyName,
       "juniRadiusClientIgnoreIngressPolicyName": juniRadiusClientIgnoreIngressPolicyName,
       "juniRadiusClientIgnoreVirtualRouter": juniRadiusClientIgnoreVirtualRouter,
       "juniRadiusClientTrapOnAuthServerUnavailable": juniRadiusClientTrapOnAuthServerUnavailable,
       "juniRadiusClientTrapOnAcctServerUnavailable": juniRadiusClientTrapOnAcctServerUnavailable,
       "juniRadiusClientTrapOnNoAuthServerAvailable": juniRadiusClientTrapOnNoAuthServerAvailable,
       "juniRadiusClientTrapOnNoAcctServerAvailable": juniRadiusClientTrapOnNoAcctServerAvailable,
       "juniRadiusClientTrapOnAuthServerAvailable": juniRadiusClientTrapOnAuthServerAvailable,
       "juniRadiusClientTrapOnAcctServerAvailable": juniRadiusClientTrapOnAcctServerAvailable,
       "juniRadiusClientPppoeNasPortFormat": juniRadiusClientPppoeNasPortFormat,
       "juniRadiusClientIncludeTunnelInterfaceIdInAccessReq": juniRadiusClientIncludeTunnelInterfaceIdInAccessReq,
       "juniRadiusClientIncludeTunnelInterfaceIdInAcctStart": juniRadiusClientIncludeTunnelInterfaceIdInAcctStart,
       "juniRadiusClientIncludeTunnelInterfaceIdInAcctStop": juniRadiusClientIncludeTunnelInterfaceIdInAcctStop,
       "juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop": juniRadiusClientIncludeL2tpPppDisconnectCauseInAcctStop,
       "juniRadiusClientVlanNasPortFormat": juniRadiusClientVlanNasPortFormat,
       "juniRadiusClientIncludeAcctMultiSessionIdInAccessReq": juniRadiusClientIncludeAcctMultiSessionIdInAccessReq,
       "juniRadiusClientIncludeAcctMultiSessionIdInAcctStart": juniRadiusClientIncludeAcctMultiSessionIdInAcctStart,
       "juniRadiusClientIncludeAcctMultiSessionIdInAcctStop": juniRadiusClientIncludeAcctMultiSessionIdInAcctStop,
       "juniRadiusClientIncludeAscendNumInMultilinkInAccessReq": juniRadiusClientIncludeAscendNumInMultilinkInAccessReq,
       "juniRadiusClientIncludeAscendNumInMultilinkInAcctStart": juniRadiusClientIncludeAscendNumInMultilinkInAcctStart,
       "juniRadiusClientIncludeAscendNumInMultilinkInAcctStop": juniRadiusClientIncludeAscendNumInMultilinkInAcctStop,
       "juniRadiusClientConnectInfoFormat": juniRadiusClientConnectInfoFormat,
       "juniRadiusClientIncludeProfileServiceDescrInAccessReq": juniRadiusClientIncludeProfileServiceDescrInAccessReq,
       "juniRadiusClientIncludeProfileServiceDescrInAcctStart": juniRadiusClientIncludeProfileServiceDescrInAcctStart,
       "juniRadiusClientIncludeProfileServiceDescrInAcctStop": juniRadiusClientIncludeProfileServiceDescrInAcctStop,
       "juniRadiusClientIncludeAcctAuthenticInAcctOn": juniRadiusClientIncludeAcctAuthenticInAcctOn,
       "juniRadiusClientIncludeAcctDelayTimeInAcctOn": juniRadiusClientIncludeAcctDelayTimeInAcctOn,
       "juniRadiusClientIncludeAcctSessionIdInAcctOn": juniRadiusClientIncludeAcctSessionIdInAcctOn,
       "juniRadiusClientIncludeNasIdentifierInAcctOn": juniRadiusClientIncludeNasIdentifierInAcctOn,
       "juniRadiusClientIncludeEventTimestampInAcctOn": juniRadiusClientIncludeEventTimestampInAcctOn,
       "juniRadiusClientIncludeAcctAuthenticInAcctOff": juniRadiusClientIncludeAcctAuthenticInAcctOff,
       "juniRadiusClientIncludeAcctDelayTimeInAcctOff": juniRadiusClientIncludeAcctDelayTimeInAcctOff,
       "juniRadiusClientIncludeAcctSessionIdInAcctOff": juniRadiusClientIncludeAcctSessionIdInAcctOff,
       "juniRadiusClientIncludeAcctTerminateCauseInAcctOff": juniRadiusClientIncludeAcctTerminateCauseInAcctOff,
       "juniRadiusClientIncludeNasIdentifierInAcctOff": juniRadiusClientIncludeNasIdentifierInAcctOff,
       "juniRadiusClientIncludeEventTimestampInAcctOff": juniRadiusClientIncludeEventTimestampInAcctOff,
       "juniRadiusClientIncludeDhcpOptionsInAccessReq": juniRadiusClientIncludeDhcpOptionsInAccessReq,
       "juniRadiusClientIncludeDhcpMacAddressInAccessReq": juniRadiusClientIncludeDhcpMacAddressInAccessReq,
       "juniRadiusClientIncludeDhcpGiAddressInAccessReq": juniRadiusClientIncludeDhcpGiAddressInAccessReq,
       "juniRadiusClientIncludeDhcpOptionsInAcctStart": juniRadiusClientIncludeDhcpOptionsInAcctStart,
       "juniRadiusClientIncludeDhcpMacAddressInAcctStart": juniRadiusClientIncludeDhcpMacAddressInAcctStart,
       "juniRadiusClientIncludeDhcpGiAddressInAcctStart": juniRadiusClientIncludeDhcpGiAddressInAcctStart,
       "juniRadiusClientIncludeDhcpOptionsInAcctStop": juniRadiusClientIncludeDhcpOptionsInAcctStop,
       "juniRadiusClientIncludeDhcpMacAddressInAcctStop": juniRadiusClientIncludeDhcpMacAddressInAcctStop,
       "juniRadiusClientIncludeDhcpGiAddressInAcctStop": juniRadiusClientIncludeDhcpGiAddressInAcctStop,
       "juniRadiusClientNasPortIdOverrideRemoteCircuitId": juniRadiusClientNasPortIdOverrideRemoteCircuitId,
       "juniRadiusClientCallingStationIdOverrideRemoteCircuitId": juniRadiusClientCallingStationIdOverrideRemoteCircuitId,
       "juniRadiusClientIncludeMlpppBundleNameInAccessReq": juniRadiusClientIncludeMlpppBundleNameInAccessReq,
       "juniRadiusClientIncludeMlpppBundleNameInAcctStart": juniRadiusClientIncludeMlpppBundleNameInAcctStart,
       "juniRadiusClientIncludeMlpppBundleNameInAcctStop": juniRadiusClientIncludeMlpppBundleNameInAcctStop,
       "juniRadiusClientOverrideNasInfo": juniRadiusClientOverrideNasInfo,
       "juniRadiusClientIncludeInterfaceDescriptionInAccessReq": juniRadiusClientIncludeInterfaceDescriptionInAccessReq,
       "juniRadiusClientIncludeInterfaceDescriptionInAcctStart": juniRadiusClientIncludeInterfaceDescriptionInAcctStart,
       "juniRadiusClientIncludeInterfaceDescriptionInAcctStop": juniRadiusClientIncludeInterfaceDescriptionInAcctStop,
       "juniRadiusClientAtmNasPortFormat": juniRadiusClientAtmNasPortFormat,
       "juniRadiusClientNasPortFieldWidthAtmSlot": juniRadiusClientNasPortFieldWidthAtmSlot,
       "juniRadiusClientNasPortFieldWidthAtmAdapter": juniRadiusClientNasPortFieldWidthAtmAdapter,
       "juniRadiusClientNasPortFieldWidthAtmPort": juniRadiusClientNasPortFieldWidthAtmPort,
       "juniRadiusClientNasPortFieldWidthAtmVpi": juniRadiusClientNasPortFieldWidthAtmVpi,
       "juniRadiusClientNasPortFieldWidthAtmVci": juniRadiusClientNasPortFieldWidthAtmVci,
       "juniRadiusClientEthernetNasPortFormat": juniRadiusClientEthernetNasPortFormat,
       "juniRadiusClientNasPortFieldWidthEthernetSlot": juniRadiusClientNasPortFieldWidthEthernetSlot,
       "juniRadiusClientNasPortFieldWidthEthernetAdapter": juniRadiusClientNasPortFieldWidthEthernetAdapter,
       "juniRadiusClientNasPortFieldWidthEthernetPort": juniRadiusClientNasPortFieldWidthEthernetPort,
       "juniRadiusClientNasPortFieldWidthEthernetSVlan": juniRadiusClientNasPortFieldWidthEthernetSVlan,
       "juniRadiusClientNasPortFieldWidthEthernetVlan": juniRadiusClientNasPortFieldWidthEthernetVlan,
       "juniRadiusClientRemoteCircuitIdFormat": juniRadiusClientRemoteCircuitIdFormat,
       "juniRadiusClientRemoteCircuitIdDelimiter": juniRadiusClientRemoteCircuitIdDelimiter,
       "juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq": juniRadiusClientIncludeL2cAccessLoopParametersInAccessReq,
       "juniRadiusClientIncludeL2cDownStreamDataInAccessReq": juniRadiusClientIncludeL2cDownStreamDataInAccessReq,
       "juniRadiusClientIncludeL2cUpStreamDataInAccessReq": juniRadiusClientIncludeL2cUpStreamDataInAccessReq,
       "juniRadiusClientIncludeL2cDownStreamDataInAcctStart": juniRadiusClientIncludeL2cDownStreamDataInAcctStart,
       "juniRadiusClientIncludeL2cUpStreamDataInAcctStart": juniRadiusClientIncludeL2cUpStreamDataInAcctStart,
       "juniRadiusClientIncludeL2cDownStreamDataInAcctStop": juniRadiusClientIncludeL2cDownStreamDataInAcctStop,
       "juniRadiusClientIncludeL2cUpStreamDataInAcctStop": juniRadiusClientIncludeL2cUpStreamDataInAcctStop,
       "juniRadiusClientIncludeDslForumAttributesInAccessReq": juniRadiusClientIncludeDslForumAttributesInAccessReq,
       "juniRadiusClientIncludeDslForumAttributesInAcctStart": juniRadiusClientIncludeDslForumAttributesInAcctStart,
       "juniRadiusClientIncludeDslForumAttributesInAcctStop": juniRadiusClientIncludeDslForumAttributesInAcctStop,
       "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq": juniRadiusClientIncludeL2cAccessLoopCircuitIdInAccessReq,
       "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq": juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAccessReq,
       "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq": juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAccessReq,
       "juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq": juniRadiusClientIncludeL2cActualDataRateUstrInAccessReq,
       "juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq": juniRadiusClientIncludeL2cActualDataRateDstrInAccessReq,
       "juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq": juniRadiusClientIncludeL2cMinimumDataRateUstrInAccessReq,
       "juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq": juniRadiusClientIncludeL2cMinimumDataRateDstrInAccessReq,
       "juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq": juniRadiusClientIncludeL2cAttainDataRateUstrInAccessReq,
       "juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq": juniRadiusClientIncludeL2cAttainDataRateDstrInAccessReq,
       "juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq": juniRadiusClientIncludeL2cMaximumDataRateUstrInAccessReq,
       "juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq": juniRadiusClientIncludeL2cMaximumDataRateDstrInAccessReq,
       "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq": juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAccessReq,
       "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq": juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAccessReq,
       "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq": juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAccessReq,
       "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq": juniRadiusClientIncludeL2cActInterleavingDelayUstrInAccessReq,
       "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq": juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAccessReq,
       "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq": juniRadiusClientIncludeL2cActInterleavingDelayDstrInAccessReq,
       "juniRadiusClientIncludeL2cDslLineStateInAccessReq": juniRadiusClientIncludeL2cDslLineStateInAccessReq,
       "juniRadiusClientIncludeL2cDslTypeInAccessReq": juniRadiusClientIncludeL2cDslTypeInAccessReq,
       "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart": juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStart,
       "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart": juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStart,
       "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart": juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStart,
       "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart": juniRadiusClientIncludeL2cActualDataRateUstrInAcctStart,
       "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart": juniRadiusClientIncludeL2cActualDataRateDstrInAcctStart,
       "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart": juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStart,
       "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart": juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStart,
       "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart": juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStart,
       "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart": juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStart,
       "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart": juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStart,
       "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart": juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStart,
       "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart": juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStart,
       "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart": juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStart,
       "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart": juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStart,
       "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart": juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStart,
       "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart": juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStart,
       "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart": juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStart,
       "juniRadiusClientIncludeL2cDslLineStateInAcctStart": juniRadiusClientIncludeL2cDslLineStateInAcctStart,
       "juniRadiusClientIncludeL2cDslTypeInAcctStart": juniRadiusClientIncludeL2cDslTypeInAcctStart,
       "juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop": juniRadiusClientIncludeL2cAccessLoopCircuitIdInAcctStop,
       "juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop": juniRadiusClientIncludeL2cAccessAggrCircuitIdBinaryInAcctStop,
       "juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop": juniRadiusClientIncludeL2cAccessAggrCircuitIdAsciiInAcctStop,
       "juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop": juniRadiusClientIncludeL2cActualDataRateUstrInAcctStop,
       "juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop": juniRadiusClientIncludeL2cActualDataRateDstrInAcctStop,
       "juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop": juniRadiusClientIncludeL2cMinimumDataRateUstrInAcctStop,
       "juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop": juniRadiusClientIncludeL2cMinimumDataRateDstrInAcctStop,
       "juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop": juniRadiusClientIncludeL2cAttainDataRateUstrInAcctStop,
       "juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop": juniRadiusClientIncludeL2cAttainDataRateDstrInAcctStop,
       "juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop": juniRadiusClientIncludeL2cMaximumDataRateUstrInAcctStop,
       "juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop": juniRadiusClientIncludeL2cMaximumDataRateDstrInAcctStop,
       "juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop": juniRadiusClientIncludeL2cMinLowPowerDataRateUstrInAcctStop,
       "juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop": juniRadiusClientIncludeL2cMinLowPowerDataRateDstrInAcctStop,
       "juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop": juniRadiusClientIncludeL2cMaxInterleavingDelayUstrInAcctStop,
       "juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop": juniRadiusClientIncludeL2cActInterleavingDelayUstrInAcctStop,
       "juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop": juniRadiusClientIncludeL2cMaxInterleavingDelayDstrInAcctStop,
       "juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop": juniRadiusClientIncludeL2cActInterleavingDelayDstrInAcctStop,
       "juniRadiusClientIncludeL2cDslLineStateInAcctStop": juniRadiusClientIncludeL2cDslLineStateInAcctStop,
       "juniRadiusClientIncludeL2cDslTypeInAcctStop": juniRadiusClientIncludeL2cDslTypeInAcctStop,
       "juniRadiusClientIncludeInterfaceIdInAcctStart": juniRadiusClientIncludeInterfaceIdInAcctStart,
       "juniRadiusClientIncludeIpv6PrefixInAcctStart": juniRadiusClientIncludeIpv6PrefixInAcctStart,
       "juniRadiusClientIncludeInterfaceIdInAcctStop": juniRadiusClientIncludeInterfaceIdInAcctStop,
       "juniRadiusClientIncludeIpAddrInAcctStop": juniRadiusClientIncludeIpAddrInAcctStop,
       "juniRadiusClientIncludeIpv6PrefixInAcctStop": juniRadiusClientIncludeIpv6PrefixInAcctStop,
       "juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq": juniRadiusClientIncludeDownStreamCalculatedQosRateInAccessReq,
       "juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq": juniRadiusClientIncludeUpStreamCalculatedQosRateInAccessReq,
       "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart": juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStart,
       "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart": juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStart,
       "juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop": juniRadiusClientIncludeDownStreamCalculatedQosRateInAcctStop,
       "juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop": juniRadiusClientIncludeUpStreamCalculatedQosRateInAcctStop,
       "juniRadiusClientIgnorePppoeMaxSession": juniRadiusClientIgnorePppoeMaxSession,
       "juniRadiusClientIncludeIpv6AccountingInAcctStop": juniRadiusClientIncludeIpv6AccountingInAcctStop,
       "juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart": juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStart,
       "juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop": juniRadiusClientIncludeDelegatedIpv6PrefixInAcctStop,
       "juniRadiusClientIncludeFramedIpv6PoolInAcctStart": juniRadiusClientIncludeFramedIpv6PoolInAcctStart,
       "juniRadiusClientIncludeFramedIpv6PoolInAcctStop": juniRadiusClientIncludeFramedIpv6PoolInAcctStop,
       "juniRadiusClientIncludeFramedIpv6RouteInAcctStart": juniRadiusClientIncludeFramedIpv6RouteInAcctStart,
       "juniRadiusClientIncludeFramedIpv6RouteInAcctStop": juniRadiusClientIncludeFramedIpv6RouteInAcctStop,
       "juniRadiusClientIncludeIpv6LocalInterfaceInAcctStart": juniRadiusClientIncludeIpv6LocalInterfaceInAcctStart,
       "juniRadiusClientIncludeIpv6LocalInterfaceInAcctStop": juniRadiusClientIncludeIpv6LocalInterfaceInAcctStop,
       "juniRadiusClientIncludeIpv6NdRaPrefixInAcctStart": juniRadiusClientIncludeIpv6NdRaPrefixInAcctStart,
       "juniRadiusClientIncludeIpv6NdRaPrefixInAcctStop": juniRadiusClientIncludeIpv6NdRaPrefixInAcctStop,
       "juniRadiusClientIncludeIpv6PrimaryDnsInAcctStart": juniRadiusClientIncludeIpv6PrimaryDnsInAcctStart,
       "juniRadiusClientIncludeIpv6PrimaryDnsInAcctStop": juniRadiusClientIncludeIpv6PrimaryDnsInAcctStop,
       "juniRadiusClientIncludeIpv6SecondaryDnsInAcctStart": juniRadiusClientIncludeIpv6SecondaryDnsInAcctStart,
       "juniRadiusClientIncludeIpv6SecondaryDnsInAcctStop": juniRadiusClientIncludeIpv6SecondaryDnsInAcctStop,
       "juniRadiusClientIncludeIpv6VirtualRouterInAcctStart": juniRadiusClientIncludeIpv6VirtualRouterInAcctStart,
       "juniRadiusClientIncludeIpv6VirtualRouterInAcctStop": juniRadiusClientIncludeIpv6VirtualRouterInAcctStop,
       "juniRadiusAuthClient": juniRadiusAuthClient,
       "juniRadiusAuthClientInvalidServerAddresses": juniRadiusAuthClientInvalidServerAddresses,
       "juniRadiusAuthClientServerTable": juniRadiusAuthClientServerTable,
       "juniRadiusAuthClientServerEntry": juniRadiusAuthClientServerEntry,
       "juniRadiusAuthClientServerAddress": juniRadiusAuthClientServerAddress,
       "juniRadiusAuthClientServerPortNumber": juniRadiusAuthClientServerPortNumber,
       "juniRadiusAuthClientRoundTripTime": juniRadiusAuthClientRoundTripTime,
       "juniRadiusAuthClientAccessRequests": juniRadiusAuthClientAccessRequests,
       "juniRadiusAuthClientAccessRetransmissions": juniRadiusAuthClientAccessRetransmissions,
       "juniRadiusAuthClientAccessAccepts": juniRadiusAuthClientAccessAccepts,
       "juniRadiusAuthClientAccessRejects": juniRadiusAuthClientAccessRejects,
       "juniRadiusAuthClientAccessChallenges": juniRadiusAuthClientAccessChallenges,
       "juniRadiusAuthClientMalformedAccessResponses": juniRadiusAuthClientMalformedAccessResponses,
       "juniRadiusAuthClientBadAuthenticators": juniRadiusAuthClientBadAuthenticators,
       "juniRadiusAuthClientPendingRequests": juniRadiusAuthClientPendingRequests,
       "juniRadiusAuthClientTimeouts": juniRadiusAuthClientTimeouts,
       "juniRadiusAuthClientUnknownTypes": juniRadiusAuthClientUnknownTypes,
       "juniRadiusAuthClientPacketsDropped": juniRadiusAuthClientPacketsDropped,
       "juniRadiusAuthClientCfgServerTable": juniRadiusAuthClientCfgServerTable,
       "juniRadiusAuthClientCfgServerEntry": juniRadiusAuthClientCfgServerEntry,
       "juniRadiusAuthClientCfgServerAddress": juniRadiusAuthClientCfgServerAddress,
       "juniRadiusAuthClientCfgServerPortNumber": juniRadiusAuthClientCfgServerPortNumber,
       "juniRadiusAuthClientCfgKey": juniRadiusAuthClientCfgKey,
       "juniRadiusAuthClientCfgTimeoutInterval": juniRadiusAuthClientCfgTimeoutInterval,
       "juniRadiusAuthClientCfgRetries": juniRadiusAuthClientCfgRetries,
       "juniRadiusAuthClientCfgMaxPendingRequests": juniRadiusAuthClientCfgMaxPendingRequests,
       "juniRadiusAuthClientCfgRowStatus": juniRadiusAuthClientCfgRowStatus,
       "juniRadiusAuthClientCfgPrecedence": juniRadiusAuthClientCfgPrecedence,
       "juniRadiusAuthClientCfgDeadTime": juniRadiusAuthClientCfgDeadTime,
       "juniRadiusAcctClient": juniRadiusAcctClient,
       "juniRadiusAcctClientInvalidServerAddresses": juniRadiusAcctClientInvalidServerAddresses,
       "juniRadiusAcctClientServerTable": juniRadiusAcctClientServerTable,
       "juniRadiusAcctClientServerEntry": juniRadiusAcctClientServerEntry,
       "juniRadiusAcctClientServerAddress": juniRadiusAcctClientServerAddress,
       "juniRadiusAcctClientServerPortNumber": juniRadiusAcctClientServerPortNumber,
       "juniRadiusAcctClientRoundTripTime": juniRadiusAcctClientRoundTripTime,
       "juniRadiusAcctClientRequests": juniRadiusAcctClientRequests,
       "juniRadiusAcctClientRetransmissions": juniRadiusAcctClientRetransmissions,
       "juniRadiusAcctClientResponses": juniRadiusAcctClientResponses,
       "juniRadiusAcctClientMalformedResponses": juniRadiusAcctClientMalformedResponses,
       "juniRadiusAcctClientBadAuthenticators": juniRadiusAcctClientBadAuthenticators,
       "juniRadiusAcctClientPendingRequests": juniRadiusAcctClientPendingRequests,
       "juniRadiusAcctClientTimeouts": juniRadiusAcctClientTimeouts,
       "juniRadiusAcctClientUnknownTypes": juniRadiusAcctClientUnknownTypes,
       "juniRadiusAcctClientPacketsDropped": juniRadiusAcctClientPacketsDropped,
       "juniRadiusAcctClientStartRequests": juniRadiusAcctClientStartRequests,
       "juniRadiusAcctClientInterimRequests": juniRadiusAcctClientInterimRequests,
       "juniRadiusAcctClientStopRequests": juniRadiusAcctClientStopRequests,
       "juniRadiusAcctClientStartResponses": juniRadiusAcctClientStartResponses,
       "juniRadiusAcctClientInterimResponses": juniRadiusAcctClientInterimResponses,
       "juniRadiusAcctClientStopResponses": juniRadiusAcctClientStopResponses,
       "juniRadiusAcctClientRejectRequests": juniRadiusAcctClientRejectRequests,
       "juniRadiusAcctClientRejectResponses": juniRadiusAcctClientRejectResponses,
       "juniRadiusAcctClientCfgServerTable": juniRadiusAcctClientCfgServerTable,
       "juniRadiusAcctClientCfgServerEntry": juniRadiusAcctClientCfgServerEntry,
       "juniRadiusAcctClientCfgServerAddress": juniRadiusAcctClientCfgServerAddress,
       "juniRadiusAcctClientCfgServerPortNumber": juniRadiusAcctClientCfgServerPortNumber,
       "juniRadiusAcctClientCfgKey": juniRadiusAcctClientCfgKey,
       "juniRadiusAcctClientCfgTimeoutInterval": juniRadiusAcctClientCfgTimeoutInterval,
       "juniRadiusAcctClientCfgRetries": juniRadiusAcctClientCfgRetries,
       "juniRadiusAcctClientCfgMaxPendingRequests": juniRadiusAcctClientCfgMaxPendingRequests,
       "juniRadiusAcctClientCfgRowStatus": juniRadiusAcctClientCfgRowStatus,
       "juniRadiusAcctClientCfgPrecedence": juniRadiusAcctClientCfgPrecedence,
       "juniRadiusAcctClientCfgDeadTime": juniRadiusAcctClientCfgDeadTime,
       "juniRadiusClientMIBConformance": juniRadiusClientMIBConformance,
       "juniRadiusClientMIBCompliances": juniRadiusClientMIBCompliances,
       "juniRadiusAuthClientCompliance": juniRadiusAuthClientCompliance,
       "juniRadiusAcctClientCompliance": juniRadiusAcctClientCompliance,
       "juniRadiusAuthClientCompliance2": juniRadiusAuthClientCompliance2,
       "juniRadiusAcctClientCompliance2": juniRadiusAcctClientCompliance2,
       "juniRadiusClientCompliance": juniRadiusClientCompliance,
       "juniRadiusClientCompliance2": juniRadiusClientCompliance2,
       "juniRadiusClientCompliance3": juniRadiusClientCompliance3,
       "juniRadiusClientCompliance4": juniRadiusClientCompliance4,
       "juniRadiusClientCompliance5": juniRadiusClientCompliance5,
       "juniRadiusClientCompliance6": juniRadiusClientCompliance6,
       "juniRadiusClientCompliance7": juniRadiusClientCompliance7,
       "juniRadiusClientCompliance8": juniRadiusClientCompliance8,
       "juniRadiusClientCompliance9": juniRadiusClientCompliance9,
       "juniRadiusClientCompliance10": juniRadiusClientCompliance10,
       "juniRadiusClientCompliance11": juniRadiusClientCompliance11,
       "juniRadiusClientCompliance12": juniRadiusClientCompliance12,
       "juniRadiusClientCompliance13": juniRadiusClientCompliance13,
       "juniRadiusClientCompliance14": juniRadiusClientCompliance14,
       "juniRadiusClientCompliance15": juniRadiusClientCompliance15,
       "juniRadiusClientCompliance16": juniRadiusClientCompliance16,
       "juniRadiusClientCompliance17": juniRadiusClientCompliance17,
       "juniRadiusClientCompliance18": juniRadiusClientCompliance18,
       "juniRadiusClientMIBGroups": juniRadiusClientMIBGroups,
       "juniRadiusGeneralClientGroup": juniRadiusGeneralClientGroup,
       "juniRadiusAuthClientGroup": juniRadiusAuthClientGroup,
       "juniRadiusAcctClientGroup": juniRadiusAcctClientGroup,
       "juniRadiusGeneralClientGroup2": juniRadiusGeneralClientGroup2,
       "juniRadiusBasicClientGroup": juniRadiusBasicClientGroup,
       "juniRadiusBrasClientGroup": juniRadiusBrasClientGroup,
       "juniRadiusTunnelClientGroup": juniRadiusTunnelClientGroup,
       "juniRadiusBrasClientGroup2": juniRadiusBrasClientGroup2,
       "juniRadiusBasicClientGroup2": juniRadiusBasicClientGroup2,
       "juniRadiusBrasClientGroup3": juniRadiusBrasClientGroup3,
       "juniRadiusBrasClientGroup4": juniRadiusBrasClientGroup4,
       "juniRadiusBrasClientGroup5": juniRadiusBrasClientGroup5,
       "juniRadiusAuthClientGroup2": juniRadiusAuthClientGroup2,
       "juniRadiusAcctClientGroup2": juniRadiusAcctClientGroup2,
       "juniRadiusAuthNotificationGroup": juniRadiusAuthNotificationGroup,
       "juniRadiusAcctNotificationGroup": juniRadiusAcctNotificationGroup,
       "juniRadiusBrasClientGroup6": juniRadiusBrasClientGroup6,
       "juniRadiusAuthClientGroup3": juniRadiusAuthClientGroup3,
       "juniRadiusAcctClientGroup3": juniRadiusAcctClientGroup3,
       "juniRadiusAuthNotificationGroup2": juniRadiusAuthNotificationGroup2,
       "juniRadiusAcctNotificationGroup2": juniRadiusAcctNotificationGroup2,
       "juniRadiusBrasClientGroup7": juniRadiusBrasClientGroup7,
       "juniRadiusAcctClientGroup4": juniRadiusAcctClientGroup4,
       "juniRadiusBrasClientGroup8": juniRadiusBrasClientGroup8,
       "juniRadiusBrasClientGroup9": juniRadiusBrasClientGroup9,
       "juniRadiusBrasClientGroup10": juniRadiusBrasClientGroup10,
       "juniRadiusBrasClientGroup11": juniRadiusBrasClientGroup11,
       "juniRadiusBrasClientGroup12": juniRadiusBrasClientGroup12,
       "juniRadiusBrasClientGroup13": juniRadiusBrasClientGroup13,
       "juniRadiusBrasClientGroup14": juniRadiusBrasClientGroup14,
       "juniRadiusBrasClientGroup15": juniRadiusBrasClientGroup15,
       "juniRadiusBrasClientGroup16": juniRadiusBrasClientGroup16,
       "juniRadiusBrasClientGroup17": juniRadiusBrasClientGroup17,
       "juniRadiusBrasClientGroup18": juniRadiusBrasClientGroup18,
       "juniRadiusBrasClientGroup19": juniRadiusBrasClientGroup19,
       "juniRadiusBrasClientGroup20": juniRadiusBrasClientGroup20,
       "juniRadiusClientTraps": juniRadiusClientTraps,
       "juniRadiusClientTrapPrefix": juniRadiusClientTrapPrefix,
       "juniRadiusAuthClientServerUnavailable": juniRadiusAuthClientServerUnavailable,
       "juniRadiusAuthClientNoServerAvailable": juniRadiusAuthClientNoServerAvailable,
       "juniRadiusAcctClientServerUnavailable": juniRadiusAcctClientServerUnavailable,
       "juniRadiusAcctClientNoServerAvailable": juniRadiusAcctClientNoServerAvailable,
       "juniRadiusAuthClientServerAvailable": juniRadiusAuthClientServerAvailable,
       "juniRadiusAcctClientServerAvailable": juniRadiusAcctClientServerAvailable,
       "juniRadiusClientTrapControl": juniRadiusClientTrapControl,
       "juniRadiusAuthClientUnavailableServer": juniRadiusAuthClientUnavailableServer,
       "juniRadiusAuthClientNextAvailableServer": juniRadiusAuthClientNextAvailableServer,
       "juniRadiusAcctClientUnavailableServer": juniRadiusAcctClientUnavailableServer,
       "juniRadiusAcctClientNextAvailableServer": juniRadiusAcctClientNextAvailableServer,
       "juniRadiusAuthClientAvailableServer": juniRadiusAuthClientAvailableServer,
       "juniRadiusAcctClientAvailableServer": juniRadiusAcctClientAvailableServer}
)
