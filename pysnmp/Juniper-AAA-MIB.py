# SNMP MIB module (Juniper-AAA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-AAA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:35 2024
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

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(juniRouterIndex,) = mibBuilder.importSymbols(
    "Juniper-ROUTER-MIB",
    "juniRouterIndex")

(JuniEnable,
 JuniInterfaceLocationType,
 JuniInterfaceLocationValue,
 JuniName,
 JuniVrfGroupName) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniInterfaceLocationType",
    "JuniInterfaceLocationValue",
    "JuniName",
    "JuniVrfGroupName")

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

juniAaaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20)
)
juniAaaMIB.setRevisions(
        ("2008-10-24 09:16",
         "2008-09-04 10:34",
         "2008-06-11 05:33",
         "2007-12-27 09:44",
         "2007-10-04 01:33",
         "2007-07-31 19:34",
         "2006-08-02 18:34",
         "2006-07-11 13:05",
         "2006-08-02 13:33",
         "2006-02-21 15:54",
         "2005-01-31 22:01",
         "2004-12-03 22:12",
         "2004-05-20 21:33",
         "2004-07-26 17:02",
         "2003-05-07 18:07",
         "2003-05-05 20:25",
         "2003-04-29 14:09",
         "2003-04-25 16:03",
         "2002-08-01 19:50",
         "2001-10-05 13:25",
         "2001-10-03 19:05",
         "2001-03-01 17:03",
         "2001-02-12 19:54",
         "2000-05-18 00:00",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniAaaDomainName(OctetString, TextualConvention):
    status = "current"
    displayHint = "63a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class JuniAaaTunnelGroupName(OctetString, TextualConvention):
    status = "current"
    displayHint = "63a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )



class JuniAaaTunnelSwitchProfileName(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class JuniAaaAuthenticationMethods(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("protocolEnable", 7),
          ("protocolLine", 5),
          ("protocolNone", 4),
          ("protocolRadius", 1),
          ("protocolTacacsPlus", 6))
    )



class JuniAaaAccountingMethods(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("protocolNone", 4),
          ("protocolRadius", 1))
    )



class JuniAddressAssignType(Integer32, TextualConvention):
    status = "current"
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("application", 5),
          ("dhcp", 3),
          ("localAuthenticationServer", 6),
          ("localPool", 2),
          ("none", 0),
          ("notSet", 7),
          ("radius", 1),
          ("user", 4))
    )



class JuniSubscriberState(Bits, TextualConvention):
    status = "current"


class JuniSubscriberClientType(Integer32, TextualConvention):
    status = "current"
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
        *(("config", 3),
          ("ip", 2),
          ("login", 1),
          ("other", 5),
          ("ppp", 0),
          ("tunnel", 4))
    )



class JuniSubscriberLocationType(Integer32, TextualConvention):
    status = "obsolete"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slotPort", 1),
          ("unknown", 0))
    )



class JuniSubscriberLocationValue(OctetString, TextualConvention):
    status = "obsolete"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class JuniSubscriberInterfaceValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )



class JuniAaaAuthenticationSubscriberTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atm1483", 2),
          ("ip", 3),
          ("ipsec", 6),
          ("ppp", 1),
          ("radiusRelay", 5),
          ("tunnel", 4))
    )



class JuniAaaAccountingSubscriberTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("atm1483", 2),
          ("ip", 3),
          ("ipsec", 6),
          ("ppp", 1),
          ("radiusRelay", 5),
          ("tunnel", 4))
    )



# MIB Managed Objects in the order of their OIDs

_JuniAaaObjects_ObjectIdentity = ObjectIdentity
juniAaaObjects = _JuniAaaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1)
)
_JuniAaaAssignment_ObjectIdentity = ObjectIdentity
juniAaaAssignment = _JuniAaaAssignment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1)
)
_JuniAaaAssignGeneral_ObjectIdentity = ObjectIdentity
juniAaaAssignGeneral = _JuniAaaAssignGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1)
)


class _JuniAaaAssignBrasLicense_Type(DisplayString):
    """Custom type juniAaaAssignBrasLicense based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniAaaAssignBrasLicense_Type.__name__ = "DisplayString"
_JuniAaaAssignBrasLicense_Object = MibScalar
juniAaaAssignBrasLicense = _JuniAaaAssignBrasLicense_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 1),
    _JuniAaaAssignBrasLicense_Type()
)
juniAaaAssignBrasLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignBrasLicense.setStatus("current")
_JuniAaaAssignBrasLicensedUsers_Type = Integer32
_JuniAaaAssignBrasLicensedUsers_Object = MibScalar
juniAaaAssignBrasLicensedUsers = _JuniAaaAssignBrasLicensedUsers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 2),
    _JuniAaaAssignBrasLicensedUsers_Type()
)
juniAaaAssignBrasLicensedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAssignBrasLicensedUsers.setStatus("current")


class _JuniAaaAssignDomainDelimiters_Type(DisplayString):
    """Custom type juniAaaAssignDomainDelimiters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_JuniAaaAssignDomainDelimiters_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainDelimiters_Object = MibScalar
juniAaaAssignDomainDelimiters = _JuniAaaAssignDomainDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 3),
    _JuniAaaAssignDomainDelimiters_Type()
)
juniAaaAssignDomainDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignDomainDelimiters.setStatus("current")


class _JuniAaaAssignRealmDelimiters_Type(DisplayString):
    """Custom type juniAaaAssignRealmDelimiters based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_JuniAaaAssignRealmDelimiters_Type.__name__ = "DisplayString"
_JuniAaaAssignRealmDelimiters_Object = MibScalar
juniAaaAssignRealmDelimiters = _JuniAaaAssignRealmDelimiters_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 4),
    _JuniAaaAssignRealmDelimiters_Type()
)
juniAaaAssignRealmDelimiters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignRealmDelimiters.setStatus("current")


class _JuniAaaAssignDomainParseOrder_Type(Integer32):
    """Custom type juniAaaAssignDomainParseOrder based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("domainFirst", 1),
          ("realmFirst", 2))
    )


_JuniAaaAssignDomainParseOrder_Type.__name__ = "Integer32"
_JuniAaaAssignDomainParseOrder_Object = MibScalar
juniAaaAssignDomainParseOrder = _JuniAaaAssignDomainParseOrder_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 5),
    _JuniAaaAssignDomainParseOrder_Type()
)
juniAaaAssignDomainParseOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignDomainParseOrder.setStatus("current")


class _JuniAaaAssignSubscriberLimit_Type(Integer32):
    """Custom type juniAaaAssignSubscriberLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_JuniAaaAssignSubscriberLimit_Type.__name__ = "Integer32"
_JuniAaaAssignSubscriberLimit_Object = MibScalar
juniAaaAssignSubscriberLimit = _JuniAaaAssignSubscriberLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 6),
    _JuniAaaAssignSubscriberLimit_Type()
)
juniAaaAssignSubscriberLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignSubscriberLimit.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaAssignSubscriberLimit.setUnits("users")
_JuniAaaAssignDomainMaxPadnPerDomain_Type = Unsigned32
_JuniAaaAssignDomainMaxPadnPerDomain_Object = MibScalar
juniAaaAssignDomainMaxPadnPerDomain = _JuniAaaAssignDomainMaxPadnPerDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 7),
    _JuniAaaAssignDomainMaxPadnPerDomain_Type()
)
juniAaaAssignDomainMaxPadnPerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAssignDomainMaxPadnPerDomain.setStatus("current")


class _JuniAaaInterfaceIdFormat_Type(Integer32):
    """Custom type juniAaaInterfaceIdFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excludeSubIntf", 2),
          ("includeSubIntf", 1))
    )


_JuniAaaInterfaceIdFormat_Type.__name__ = "Integer32"
_JuniAaaInterfaceIdFormat_Object = MibScalar
juniAaaInterfaceIdFormat = _JuniAaaInterfaceIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 8),
    _JuniAaaInterfaceIdFormat_Type()
)
juniAaaInterfaceIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaInterfaceIdFormat.setStatus("current")


class _JuniAaaAssignTunnelCallingNumberFormat_Type(Integer32):
    """Custom type juniAaaAssignTunnelCallingNumberFormat based on Integer32"""
    defaultValue = 1

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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("agentCircuitId", 6),
          ("agentCircuitIdIncludeAgentRemoteId", 8),
          ("agentRemoteId", 7),
          ("descriptive", 1),
          ("descriptiveIncludeAgentCircuitId", 3),
          ("descriptiveIncludeAgentCircuitIdAndAgentRemoteId", 5),
          ("descriptiveIncludeAgentRemoteId", 4),
          ("fixed", 2),
          ("fixedAdapterEmbedded", 10),
          ("fixedAdapterEmbeddedIncludeSvlanId", 12),
          ("fixedAdapterNewField", 11),
          ("fixedAdapterNewFieldIncludeSvlanId", 13),
          ("fixedIncludeSvlanId", 9))
    )


_JuniAaaAssignTunnelCallingNumberFormat_Type.__name__ = "Integer32"
_JuniAaaAssignTunnelCallingNumberFormat_Object = MibScalar
juniAaaAssignTunnelCallingNumberFormat = _JuniAaaAssignTunnelCallingNumberFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 9),
    _JuniAaaAssignTunnelCallingNumberFormat_Type()
)
juniAaaAssignTunnelCallingNumberFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignTunnelCallingNumberFormat.setStatus("current")


class _JuniAaaAssignDomainParseDirection_Type(Integer32):
    """Custom type juniAaaAssignDomainParseDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leftToRight", 2),
          ("rightToLeft", 1))
    )


_JuniAaaAssignDomainParseDirection_Type.__name__ = "Integer32"
_JuniAaaAssignDomainParseDirection_Object = MibScalar
juniAaaAssignDomainParseDirection = _JuniAaaAssignDomainParseDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 10),
    _JuniAaaAssignDomainParseDirection_Type()
)
juniAaaAssignDomainParseDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignDomainParseDirection.setStatus("current")


class _JuniAaaAssignRealmParseDirection_Type(Integer32):
    """Custom type juniAaaAssignRealmParseDirection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leftToRight", 2),
          ("rightToLeft", 1))
    )


_JuniAaaAssignRealmParseDirection_Type.__name__ = "Integer32"
_JuniAaaAssignRealmParseDirection_Object = MibScalar
juniAaaAssignRealmParseDirection = _JuniAaaAssignRealmParseDirection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 11),
    _JuniAaaAssignRealmParseDirection_Type()
)
juniAaaAssignRealmParseDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignRealmParseDirection.setStatus("current")


class _JuniAaaInterfaceAdapterFormat_Type(Integer32):
    """Custom type juniAaaInterfaceAdapterFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("excludeAdapter", 2),
          ("includeAdapter", 1))
    )


_JuniAaaInterfaceAdapterFormat_Type.__name__ = "Integer32"
_JuniAaaInterfaceAdapterFormat_Object = MibScalar
juniAaaInterfaceAdapterFormat = _JuniAaaInterfaceAdapterFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 12),
    _JuniAaaInterfaceAdapterFormat_Type()
)
juniAaaInterfaceAdapterFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaInterfaceAdapterFormat.setStatus("current")


class _JuniAaaAssignAccountingStatisticsType_Type(Integer32):
    """Custom type juniAaaAssignAccountingStatisticsType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("full", 0),
          ("uptime", 1))
    )


_JuniAaaAssignAccountingStatisticsType_Type.__name__ = "Integer32"
_JuniAaaAssignAccountingStatisticsType_Object = MibScalar
juniAaaAssignAccountingStatisticsType = _JuniAaaAssignAccountingStatisticsType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 13),
    _JuniAaaAssignAccountingStatisticsType_Type()
)
juniAaaAssignAccountingStatisticsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignAccountingStatisticsType.setStatus("current")


class _JuniAaaAssignQosDownstreamRate_Type(JuniEnable):
    """Custom type juniAaaAssignQosDownstreamRate based on JuniEnable"""


_JuniAaaAssignQosDownstreamRate_Object = MibScalar
juniAaaAssignQosDownstreamRate = _JuniAaaAssignQosDownstreamRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 14),
    _JuniAaaAssignQosDownstreamRate_Type()
)
juniAaaAssignQosDownstreamRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignQosDownstreamRate.setStatus("current")


class _JuniAaaAssignTunnelCallingNumberFormatFallback_Type(Integer32):
    """Custom type juniAaaAssignTunnelCallingNumberFormatFallback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("descriptive", 1),
          ("fixed", 2),
          ("fixedAdapterEmbedded", 4),
          ("fixedAdapterEmbeddedIncludeSvlanId", 6),
          ("fixedAdapterNewField", 5),
          ("fixedAdapterNewFieldIncludeSvlanId", 7),
          ("fixedIncludeSvlanId", 3))
    )


_JuniAaaAssignTunnelCallingNumberFormatFallback_Type.__name__ = "Integer32"
_JuniAaaAssignTunnelCallingNumberFormatFallback_Object = MibScalar
juniAaaAssignTunnelCallingNumberFormatFallback = _JuniAaaAssignTunnelCallingNumberFormatFallback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 15),
    _JuniAaaAssignTunnelCallingNumberFormatFallback_Type()
)
juniAaaAssignTunnelCallingNumberFormatFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAssignTunnelCallingNumberFormatFallback.setStatus("current")


class _JuniAaaFramedIpv6PrefixAsIpv6NdRaPrefix_Type(TruthValue):
    """Custom type juniAaaFramedIpv6PrefixAsIpv6NdRaPrefix based on TruthValue"""


_JuniAaaFramedIpv6PrefixAsIpv6NdRaPrefix_Object = MibScalar
juniAaaFramedIpv6PrefixAsIpv6NdRaPrefix = _JuniAaaFramedIpv6PrefixAsIpv6NdRaPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 16),
    _JuniAaaFramedIpv6PrefixAsIpv6NdRaPrefix_Type()
)
juniAaaFramedIpv6PrefixAsIpv6NdRaPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaFramedIpv6PrefixAsIpv6NdRaPrefix.setStatus("current")


class _JuniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix_Type(TruthValue):
    """Custom type juniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix based on TruthValue"""


_JuniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix_Object = MibScalar
juniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix = _JuniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 1, 17),
    _JuniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix_Type()
)
juniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix.setStatus("current")
_JuniAaaAssignDomain_ObjectIdentity = ObjectIdentity
juniAaaAssignDomain = _JuniAaaAssignDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2)
)
_JuniAaaAssignDomainTable_Object = MibTable
juniAaaAssignDomainTable = _JuniAaaAssignDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniAaaAssignDomainTable.setStatus("current")
_JuniAaaAssignDomainEntry_Object = MibTableRow
juniAaaAssignDomainEntry = _JuniAaaAssignDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1)
)
juniAaaAssignDomainEntry.setIndexNames(
    (1, "Juniper-AAA-MIB", "juniAaaAssignDomainName"),
)
if mibBuilder.loadTexts:
    juniAaaAssignDomainEntry.setStatus("current")
_JuniAaaAssignDomainName_Type = JuniAaaDomainName
_JuniAaaAssignDomainName_Object = MibTableColumn
juniAaaAssignDomainName = _JuniAaaAssignDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 1),
    _JuniAaaAssignDomainName_Type()
)
juniAaaAssignDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAssignDomainName.setStatus("current")
_JuniAaaAssignDomainRowStatus_Type = RowStatus
_JuniAaaAssignDomainRowStatus_Object = MibTableColumn
juniAaaAssignDomainRowStatus = _JuniAaaAssignDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 2),
    _JuniAaaAssignDomainRowStatus_Type()
)
juniAaaAssignDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainRowStatus.setStatus("current")
_JuniAaaAssignDomainRouterName_Type = JuniName
_JuniAaaAssignDomainRouterName_Object = MibTableColumn
juniAaaAssignDomainRouterName = _JuniAaaAssignDomainRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 3),
    _JuniAaaAssignDomainRouterName_Type()
)
juniAaaAssignDomainRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAssignDomainRouterName.setStatus("deprecated")


class _JuniAaaAssignDomainLoopback_Type(Integer32):
    """Custom type juniAaaAssignDomainLoopback based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32000),
    )


_JuniAaaAssignDomainLoopback_Type.__name__ = "Integer32"
_JuniAaaAssignDomainLoopback_Object = MibTableColumn
juniAaaAssignDomainLoopback = _JuniAaaAssignDomainLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 4),
    _JuniAaaAssignDomainLoopback_Type()
)
juniAaaAssignDomainLoopback.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainLoopback.setStatus("obsolete")


class _JuniAaaAssignDomainIpHint_Type(TruthValue):
    """Custom type juniAaaAssignDomainIpHint based on TruthValue"""


_JuniAaaAssignDomainIpHint_Object = MibTableColumn
juniAaaAssignDomainIpHint = _JuniAaaAssignDomainIpHint_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 5),
    _JuniAaaAssignDomainIpHint_Type()
)
juniAaaAssignDomainIpHint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainIpHint.setStatus("current")


class _JuniAaaAssignDomainAtmServiceLevel_Type(Integer32):
    """Custom type juniAaaAssignDomainAtmServiceLevel based on Integer32"""
    defaultValue = 0

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
        *(("cbr", 4),
          ("none", 0),
          ("nrtVbr", 3),
          ("rtVbr", 5),
          ("ubr", 1),
          ("ubrPcr", 2))
    )


_JuniAaaAssignDomainAtmServiceLevel_Type.__name__ = "Integer32"
_JuniAaaAssignDomainAtmServiceLevel_Object = MibTableColumn
juniAaaAssignDomainAtmServiceLevel = _JuniAaaAssignDomainAtmServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 6),
    _JuniAaaAssignDomainAtmServiceLevel_Type()
)
juniAaaAssignDomainAtmServiceLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAtmServiceLevel.setStatus("current")


class _JuniAaaAssignDomainAtmPcr_Type(Unsigned32):
    """Custom type juniAaaAssignDomainAtmPcr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_JuniAaaAssignDomainAtmPcr_Type.__name__ = "Unsigned32"
_JuniAaaAssignDomainAtmPcr_Object = MibTableColumn
juniAaaAssignDomainAtmPcr = _JuniAaaAssignDomainAtmPcr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 7),
    _JuniAaaAssignDomainAtmPcr_Type()
)
juniAaaAssignDomainAtmPcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAtmPcr.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAtmPcr.setUnits("kbps")


class _JuniAaaAssignDomainAtmScr_Type(Unsigned32):
    """Custom type juniAaaAssignDomainAtmScr based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_JuniAaaAssignDomainAtmScr_Type.__name__ = "Unsigned32"
_JuniAaaAssignDomainAtmScr_Object = MibTableColumn
juniAaaAssignDomainAtmScr = _JuniAaaAssignDomainAtmScr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 8),
    _JuniAaaAssignDomainAtmScr_Type()
)
juniAaaAssignDomainAtmScr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAtmScr.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAtmScr.setUnits("kbps")


class _JuniAaaAssignDomainAtmMbs_Type(Unsigned32):
    """Custom type juniAaaAssignDomainAtmMbs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_JuniAaaAssignDomainAtmMbs_Type.__name__ = "Unsigned32"
_JuniAaaAssignDomainAtmMbs_Object = MibTableColumn
juniAaaAssignDomainAtmMbs = _JuniAaaAssignDomainAtmMbs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 9),
    _JuniAaaAssignDomainAtmMbs_Type()
)
juniAaaAssignDomainAtmMbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAtmMbs.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAtmMbs.setUnits("cells")


class _JuniAaaAssignDomainOverrideUserName_Type(DisplayString):
    """Custom type juniAaaAssignDomainOverrideUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaAssignDomainOverrideUserName_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainOverrideUserName_Object = MibTableColumn
juniAaaAssignDomainOverrideUserName = _JuniAaaAssignDomainOverrideUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 10),
    _JuniAaaAssignDomainOverrideUserName_Type()
)
juniAaaAssignDomainOverrideUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainOverrideUserName.setStatus("current")


class _JuniAaaAssignDomainOverridePassword_Type(OctetString):
    """Custom type juniAaaAssignDomainOverridePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaAssignDomainOverridePassword_Type.__name__ = "OctetString"
_JuniAaaAssignDomainOverridePassword_Object = MibTableColumn
juniAaaAssignDomainOverridePassword = _JuniAaaAssignDomainOverridePassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 11),
    _JuniAaaAssignDomainOverridePassword_Type()
)
juniAaaAssignDomainOverridePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainOverridePassword.setStatus("current")


class _JuniAaaAssignDomainStripDomain_Type(TruthValue):
    """Custom type juniAaaAssignDomainStripDomain based on TruthValue"""


_JuniAaaAssignDomainStripDomain_Object = MibTableColumn
juniAaaAssignDomainStripDomain = _JuniAaaAssignDomainStripDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 12),
    _JuniAaaAssignDomainStripDomain_Type()
)
juniAaaAssignDomainStripDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainStripDomain.setStatus("current")


class _JuniAaaAssignDomainPoolName_Type(DisplayString):
    """Custom type juniAaaAssignDomainPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniAaaAssignDomainPoolName_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainPoolName_Object = MibTableColumn
juniAaaAssignDomainPoolName = _JuniAaaAssignDomainPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 13),
    _JuniAaaAssignDomainPoolName_Type()
)
juniAaaAssignDomainPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainPoolName.setStatus("current")


class _JuniAaaAssignDomainLocalInterface_Type(DisplayString):
    """Custom type juniAaaAssignDomainLocalInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniAaaAssignDomainLocalInterface_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainLocalInterface_Object = MibTableColumn
juniAaaAssignDomainLocalInterface = _JuniAaaAssignDomainLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 14),
    _JuniAaaAssignDomainLocalInterface_Type()
)
juniAaaAssignDomainLocalInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainLocalInterface.setStatus("current")
_JuniAaaAssignDomainIpv6RouterName_Type = JuniName
_JuniAaaAssignDomainIpv6RouterName_Object = MibTableColumn
juniAaaAssignDomainIpv6RouterName = _JuniAaaAssignDomainIpv6RouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 15),
    _JuniAaaAssignDomainIpv6RouterName_Type()
)
juniAaaAssignDomainIpv6RouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainIpv6RouterName.setStatus("current")


class _JuniAaaAssignDomainIpv6LocalInterface_Type(DisplayString):
    """Custom type juniAaaAssignDomainIpv6LocalInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniAaaAssignDomainIpv6LocalInterface_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainIpv6LocalInterface_Object = MibTableColumn
juniAaaAssignDomainIpv6LocalInterface = _JuniAaaAssignDomainIpv6LocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 16),
    _JuniAaaAssignDomainIpv6LocalInterface_Type()
)
juniAaaAssignDomainIpv6LocalInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainIpv6LocalInterface.setStatus("current")
_JuniAaaAssignDomainTunnelGroup_Type = JuniAaaTunnelGroupName
_JuniAaaAssignDomainTunnelGroup_Object = MibTableColumn
juniAaaAssignDomainTunnelGroup = _JuniAaaAssignDomainTunnelGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 17),
    _JuniAaaAssignDomainTunnelGroup_Type()
)
juniAaaAssignDomainTunnelGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelGroup.setStatus("current")
_JuniAaaAssignDomainAuthRouterName_Type = JuniName
_JuniAaaAssignDomainAuthRouterName_Object = MibTableColumn
juniAaaAssignDomainAuthRouterName = _JuniAaaAssignDomainAuthRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 18),
    _JuniAaaAssignDomainAuthRouterName_Type()
)
juniAaaAssignDomainAuthRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainAuthRouterName.setStatus("current")
_JuniAaaAssignDomainIpRouterName_Type = JuniName
_JuniAaaAssignDomainIpRouterName_Object = MibTableColumn
juniAaaAssignDomainIpRouterName = _JuniAaaAssignDomainIpRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 19),
    _JuniAaaAssignDomainIpRouterName_Type()
)
juniAaaAssignDomainIpRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainIpRouterName.setStatus("current")


class _JuniAaaAssignDomainTunnelSubscriberAuthentication_Type(TruthValue):
    """Custom type juniAaaAssignDomainTunnelSubscriberAuthentication based on TruthValue"""


_JuniAaaAssignDomainTunnelSubscriberAuthentication_Object = MibTableColumn
juniAaaAssignDomainTunnelSubscriberAuthentication = _JuniAaaAssignDomainTunnelSubscriberAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 20),
    _JuniAaaAssignDomainTunnelSubscriberAuthentication_Type()
)
juniAaaAssignDomainTunnelSubscriberAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelSubscriberAuthentication.setStatus("current")


class _JuniAaaAssignDomainBackupPoolName_Type(DisplayString):
    """Custom type juniAaaAssignDomainBackupPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniAaaAssignDomainBackupPoolName_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainBackupPoolName_Object = MibTableColumn
juniAaaAssignDomainBackupPoolName = _JuniAaaAssignDomainBackupPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 1, 1, 21),
    _JuniAaaAssignDomainBackupPoolName_Type()
)
juniAaaAssignDomainBackupPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainBackupPoolName.setStatus("current")
_JuniAaaAssignDomainTunnelTable_Object = MibTable
juniAaaAssignDomainTunnelTable = _JuniAaaAssignDomainTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelTable.setStatus("current")
_JuniAaaAssignDomainTunnelEntry_Object = MibTableRow
juniAaaAssignDomainTunnelEntry = _JuniAaaAssignDomainTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1)
)
juniAaaAssignDomainTunnelEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaAssignDomainTunnelName"),
    (0, "Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTag"),
)
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelEntry.setStatus("current")
_JuniAaaAssignDomainTunnelName_Type = JuniAaaDomainName
_JuniAaaAssignDomainTunnelName_Object = MibTableColumn
juniAaaAssignDomainTunnelName = _JuniAaaAssignDomainTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 1),
    _JuniAaaAssignDomainTunnelName_Type()
)
juniAaaAssignDomainTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelName.setStatus("current")


class _JuniAaaAssignDomainTunnelTag_Type(Integer32):
    """Custom type juniAaaAssignDomainTunnelTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_JuniAaaAssignDomainTunnelTag_Type.__name__ = "Integer32"
_JuniAaaAssignDomainTunnelTag_Object = MibTableColumn
juniAaaAssignDomainTunnelTag = _JuniAaaAssignDomainTunnelTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 2),
    _JuniAaaAssignDomainTunnelTag_Type()
)
juniAaaAssignDomainTunnelTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelTag.setStatus("current")


class _JuniAaaAssignDomainTunnelPreference_Type(Integer32):
    """Custom type juniAaaAssignDomainTunnelPreference based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_JuniAaaAssignDomainTunnelPreference_Type.__name__ = "Integer32"
_JuniAaaAssignDomainTunnelPreference_Object = MibTableColumn
juniAaaAssignDomainTunnelPreference = _JuniAaaAssignDomainTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 3),
    _JuniAaaAssignDomainTunnelPreference_Type()
)
juniAaaAssignDomainTunnelPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelPreference.setStatus("current")


class _JuniAaaAssignDomainTunnelType_Type(Integer32):
    """Custom type juniAaaAssignDomainTunnelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tunnelL2f", 3),
          ("tunnelL2tp", 1),
          ("tunnelUnknown", 2))
    )


_JuniAaaAssignDomainTunnelType_Type.__name__ = "Integer32"
_JuniAaaAssignDomainTunnelType_Object = MibTableColumn
juniAaaAssignDomainTunnelType = _JuniAaaAssignDomainTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 4),
    _JuniAaaAssignDomainTunnelType_Type()
)
juniAaaAssignDomainTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelType.setStatus("current")


class _JuniAaaAssignDomainTunnelMedium_Type(Integer32):
    """Custom type juniAaaAssignDomainTunnelMedium based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnelMediumIPv4", 1),
          ("tunnelMediumUnknown", 2))
    )


_JuniAaaAssignDomainTunnelMedium_Type.__name__ = "Integer32"
_JuniAaaAssignDomainTunnelMedium_Object = MibTableColumn
juniAaaAssignDomainTunnelMedium = _JuniAaaAssignDomainTunnelMedium_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 5),
    _JuniAaaAssignDomainTunnelMedium_Type()
)
juniAaaAssignDomainTunnelMedium.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelMedium.setStatus("current")


class _JuniAaaAssignDomainTunnelAddress_Type(DisplayString):
    """Custom type juniAaaAssignDomainTunnelAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaAssignDomainTunnelAddress_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainTunnelAddress_Object = MibTableColumn
juniAaaAssignDomainTunnelAddress = _JuniAaaAssignDomainTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 6),
    _JuniAaaAssignDomainTunnelAddress_Type()
)
juniAaaAssignDomainTunnelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelAddress.setStatus("current")


class _JuniAaaAssignDomainTunnelPassword_Type(DisplayString):
    """Custom type juniAaaAssignDomainTunnelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaAssignDomainTunnelPassword_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainTunnelPassword_Object = MibTableColumn
juniAaaAssignDomainTunnelPassword = _JuniAaaAssignDomainTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 7),
    _JuniAaaAssignDomainTunnelPassword_Type()
)
juniAaaAssignDomainTunnelPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelPassword.setStatus("current")


class _JuniAaaAssignDomainTunnelId_Type(DisplayString):
    """Custom type juniAaaAssignDomainTunnelId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaAssignDomainTunnelId_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainTunnelId_Object = MibTableColumn
juniAaaAssignDomainTunnelId = _JuniAaaAssignDomainTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 8),
    _JuniAaaAssignDomainTunnelId_Type()
)
juniAaaAssignDomainTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelId.setStatus("current")


class _JuniAaaAssignDomainTunnelHostName_Type(DisplayString):
    """Custom type juniAaaAssignDomainTunnelHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniAaaAssignDomainTunnelHostName_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainTunnelHostName_Object = MibTableColumn
juniAaaAssignDomainTunnelHostName = _JuniAaaAssignDomainTunnelHostName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 9),
    _JuniAaaAssignDomainTunnelHostName_Type()
)
juniAaaAssignDomainTunnelHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelHostName.setStatus("current")
_JuniAaaAssignDomainTunnelRowStatus_Type = RowStatus
_JuniAaaAssignDomainTunnelRowStatus_Object = MibTableColumn
juniAaaAssignDomainTunnelRowStatus = _JuniAaaAssignDomainTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 10),
    _JuniAaaAssignDomainTunnelRowStatus_Type()
)
juniAaaAssignDomainTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelRowStatus.setStatus("current")


class _JuniAaaAssignDomainTunnelServerName_Type(DisplayString):
    """Custom type juniAaaAssignDomainTunnelServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniAaaAssignDomainTunnelServerName_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainTunnelServerName_Object = MibTableColumn
juniAaaAssignDomainTunnelServerName = _JuniAaaAssignDomainTunnelServerName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 11),
    _JuniAaaAssignDomainTunnelServerName_Type()
)
juniAaaAssignDomainTunnelServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelServerName.setStatus("current")


class _JuniAaaAssignDomainTunnelClientAddress_Type(DisplayString):
    """Custom type juniAaaAssignDomainTunnelClientAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaAssignDomainTunnelClientAddress_Type.__name__ = "DisplayString"
_JuniAaaAssignDomainTunnelClientAddress_Object = MibTableColumn
juniAaaAssignDomainTunnelClientAddress = _JuniAaaAssignDomainTunnelClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 12),
    _JuniAaaAssignDomainTunnelClientAddress_Type()
)
juniAaaAssignDomainTunnelClientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelClientAddress.setStatus("current")


class _JuniAaaAssignDomainTunnelMaxSessions_Type(Unsigned32):
    """Custom type juniAaaAssignDomainTunnelMaxSessions based on Unsigned32"""
    defaultValue = 1000


_JuniAaaAssignDomainTunnelMaxSessions_Object = MibTableColumn
juniAaaAssignDomainTunnelMaxSessions = _JuniAaaAssignDomainTunnelMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 13),
    _JuniAaaAssignDomainTunnelMaxSessions_Type()
)
juniAaaAssignDomainTunnelMaxSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelMaxSessions.setStatus("current")


class _JuniAaaAssignDomainTunnelReceiveWindowSize_Type(Integer32):
    """Custom type juniAaaAssignDomainTunnelReceiveWindowSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 4),
    )


_JuniAaaAssignDomainTunnelReceiveWindowSize_Type.__name__ = "Integer32"
_JuniAaaAssignDomainTunnelReceiveWindowSize_Object = MibTableColumn
juniAaaAssignDomainTunnelReceiveWindowSize = _JuniAaaAssignDomainTunnelReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 14),
    _JuniAaaAssignDomainTunnelReceiveWindowSize_Type()
)
juniAaaAssignDomainTunnelReceiveWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelReceiveWindowSize.setStatus("current")


class _JuniAaaAssignDomainTunnelFailoverResync_Type(Integer32):
    """Custom type juniAaaAssignDomainTunnelFailoverResync based on Integer32"""
    defaultValue = 4

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
        *(("disable", 0),
          ("failoverProtocol", 1),
          ("failoverProtocolFallbackToSilentFailover", 3),
          ("notConfigured", 4),
          ("silentFailover", 2))
    )


_JuniAaaAssignDomainTunnelFailoverResync_Type.__name__ = "Integer32"
_JuniAaaAssignDomainTunnelFailoverResync_Object = MibTableColumn
juniAaaAssignDomainTunnelFailoverResync = _JuniAaaAssignDomainTunnelFailoverResync_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 15),
    _JuniAaaAssignDomainTunnelFailoverResync_Type()
)
juniAaaAssignDomainTunnelFailoverResync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelFailoverResync.setStatus("current")
_JuniAaaAssignDomainTunnelSwitchProfile_Type = JuniAaaTunnelSwitchProfileName
_JuniAaaAssignDomainTunnelSwitchProfile_Object = MibTableColumn
juniAaaAssignDomainTunnelSwitchProfile = _JuniAaaAssignDomainTunnelSwitchProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 16),
    _JuniAaaAssignDomainTunnelSwitchProfile_Type()
)
juniAaaAssignDomainTunnelSwitchProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelSwitchProfile.setStatus("current")


class _JuniAaaAssignDomainTunnelTxConnectSpeedMethod_Type(Integer32):
    """Custom type juniAaaAssignDomainTunnelTxConnectSpeedMethod based on Integer32"""
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
        *(("actual", 4),
          ("dynamicLayer2", 2),
          ("notSet", 0),
          ("qos", 3),
          ("staticLayer2", 1))
    )


_JuniAaaAssignDomainTunnelTxConnectSpeedMethod_Type.__name__ = "Integer32"
_JuniAaaAssignDomainTunnelTxConnectSpeedMethod_Object = MibTableColumn
juniAaaAssignDomainTunnelTxConnectSpeedMethod = _JuniAaaAssignDomainTunnelTxConnectSpeedMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 2, 1, 17),
    _JuniAaaAssignDomainTunnelTxConnectSpeedMethod_Type()
)
juniAaaAssignDomainTunnelTxConnectSpeedMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainTunnelTxConnectSpeedMethod.setStatus("current")
_JuniAaaAssignDomainPadnTable_Object = MibTable
juniAaaAssignDomainPadnTable = _JuniAaaAssignDomainPadnTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    juniAaaAssignDomainPadnTable.setStatus("current")
_JuniAaaAssignDomainPadnEntry_Object = MibTableRow
juniAaaAssignDomainPadnEntry = _JuniAaaAssignDomainPadnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 3, 1)
)
juniAaaAssignDomainPadnEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaAssignDomainName"),
    (0, "Juniper-AAA-MIB", "juniAaaAssignDomainPadnIpAddress"),
    (0, "Juniper-AAA-MIB", "juniAaaAssignDomainPadnIpMask"),
)
if mibBuilder.loadTexts:
    juniAaaAssignDomainPadnEntry.setStatus("current")
_JuniAaaAssignDomainPadnIpAddress_Type = IpAddress
_JuniAaaAssignDomainPadnIpAddress_Object = MibTableColumn
juniAaaAssignDomainPadnIpAddress = _JuniAaaAssignDomainPadnIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 3, 1, 1),
    _JuniAaaAssignDomainPadnIpAddress_Type()
)
juniAaaAssignDomainPadnIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaAssignDomainPadnIpAddress.setStatus("current")
_JuniAaaAssignDomainPadnIpMask_Type = IpAddress
_JuniAaaAssignDomainPadnIpMask_Object = MibTableColumn
juniAaaAssignDomainPadnIpMask = _JuniAaaAssignDomainPadnIpMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 3, 1, 2),
    _JuniAaaAssignDomainPadnIpMask_Type()
)
juniAaaAssignDomainPadnIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaAssignDomainPadnIpMask.setStatus("current")
_JuniAaaAssignDomainPadnRowStatus_Type = RowStatus
_JuniAaaAssignDomainPadnRowStatus_Object = MibTableColumn
juniAaaAssignDomainPadnRowStatus = _JuniAaaAssignDomainPadnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 3, 1, 3),
    _JuniAaaAssignDomainPadnRowStatus_Type()
)
juniAaaAssignDomainPadnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainPadnRowStatus.setStatus("current")


class _JuniAaaAssignDomainPadnDistance_Type(Integer32):
    """Custom type juniAaaAssignDomainPadnDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniAaaAssignDomainPadnDistance_Type.__name__ = "Integer32"
_JuniAaaAssignDomainPadnDistance_Object = MibTableColumn
juniAaaAssignDomainPadnDistance = _JuniAaaAssignDomainPadnDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 1, 2, 3, 1, 4),
    _JuniAaaAssignDomainPadnDistance_Type()
)
juniAaaAssignDomainPadnDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaAssignDomainPadnDistance.setStatus("current")
_JuniAaaAuthentication_ObjectIdentity = ObjectIdentity
juniAaaAuthentication = _JuniAaaAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2)
)
_JuniAaaAuthGeneral_ObjectIdentity = ObjectIdentity
juniAaaAuthGeneral = _JuniAaaAuthGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1)
)


class _JuniAaaAuthMethods_Type(OctetString):
    """Custom type juniAaaAuthMethods based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JuniAaaAuthMethods_Type.__name__ = "OctetString"
_JuniAaaAuthMethods_Object = MibScalar
juniAaaAuthMethods = _JuniAaaAuthMethods_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1, 1),
    _JuniAaaAuthMethods_Type()
)
juniAaaAuthMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAuthMethods.setStatus("obsolete")
_JuniAaaAuthMethodsTable_Object = MibTable
juniAaaAuthMethodsTable = _JuniAaaAuthMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniAaaAuthMethodsTable.setStatus("current")
_JuniAaaAuthMethodsEntry_Object = MibTableRow
juniAaaAuthMethodsEntry = _JuniAaaAuthMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1, 2, 1)
)
juniAaaAuthMethodsEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaAuthMethodsSubscriberType"),
)
if mibBuilder.loadTexts:
    juniAaaAuthMethodsEntry.setStatus("current")
_JuniAaaAuthMethodsSubscriberType_Type = JuniAaaAuthenticationSubscriberTypes
_JuniAaaAuthMethodsSubscriberType_Object = MibTableColumn
juniAaaAuthMethodsSubscriberType = _JuniAaaAuthMethodsSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1, 2, 1, 1),
    _JuniAaaAuthMethodsSubscriberType_Type()
)
juniAaaAuthMethodsSubscriberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAuthMethodsSubscriberType.setStatus("current")


class _JuniAaaAuthMethodsAuthentication_Type(OctetString):
    """Custom type juniAaaAuthMethodsAuthentication based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JuniAaaAuthMethodsAuthentication_Type.__name__ = "OctetString"
_JuniAaaAuthMethodsAuthentication_Object = MibTableColumn
juniAaaAuthMethodsAuthentication = _JuniAaaAuthMethodsAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 1, 2, 1, 2),
    _JuniAaaAuthMethodsAuthentication_Type()
)
juniAaaAuthMethodsAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAuthMethodsAuthentication.setStatus("current")
_JuniAaaLocalAuth_ObjectIdentity = ObjectIdentity
juniAaaLocalAuth = _JuniAaaLocalAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2)
)
_JuniAaaLocalAuthUser_ObjectIdentity = ObjectIdentity
juniAaaLocalAuthUser = _JuniAaaLocalAuthUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1)
)
_JuniAaaLocalAuthUserTable_Object = MibTable
juniAaaLocalAuthUserTable = _JuniAaaLocalAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserTable.setStatus("current")
_JuniAaaLocalAuthUserEntry_Object = MibTableRow
juniAaaLocalAuthUserEntry = _JuniAaaLocalAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1)
)
juniAaaLocalAuthUserEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaLocalAuthUserDbName"),
    (1, "Juniper-AAA-MIB", "juniAaaLocalAuthUserName"),
)
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserEntry.setStatus("current")


class _JuniAaaLocalAuthUserName_Type(DisplayString):
    """Custom type juniAaaLocalAuthUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JuniAaaLocalAuthUserName_Type.__name__ = "DisplayString"
_JuniAaaLocalAuthUserName_Object = MibTableColumn
juniAaaLocalAuthUserName = _JuniAaaLocalAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1, 1),
    _JuniAaaLocalAuthUserName_Type()
)
juniAaaLocalAuthUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserName.setStatus("current")
_JuniAaaLocalAuthUserRowStatus_Type = RowStatus
_JuniAaaLocalAuthUserRowStatus_Object = MibTableColumn
juniAaaLocalAuthUserRowStatus = _JuniAaaLocalAuthUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1, 2),
    _JuniAaaLocalAuthUserRowStatus_Type()
)
juniAaaLocalAuthUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserRowStatus.setStatus("current")


class _JuniAaaLocalAuthUserPassword_Type(OctetString):
    """Custom type juniAaaLocalAuthUserPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaLocalAuthUserPassword_Type.__name__ = "OctetString"
_JuniAaaLocalAuthUserPassword_Object = MibTableColumn
juniAaaLocalAuthUserPassword = _JuniAaaLocalAuthUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1, 3),
    _JuniAaaLocalAuthUserPassword_Type()
)
juniAaaLocalAuthUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserPassword.setStatus("current")


class _JuniAaaLocalAuthUserEncryption_Type(Integer32):
    """Custom type juniAaaLocalAuthUserEncryption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("encryptionNone", 0),
          ("encryptionPassword", 8),
          ("encryptionSecret", 5))
    )


_JuniAaaLocalAuthUserEncryption_Type.__name__ = "Integer32"
_JuniAaaLocalAuthUserEncryption_Object = MibTableColumn
juniAaaLocalAuthUserEncryption = _JuniAaaLocalAuthUserEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1, 4),
    _JuniAaaLocalAuthUserEncryption_Type()
)
juniAaaLocalAuthUserEncryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserEncryption.setStatus("current")


class _JuniAaaLocalAuthUserIpAddress_Type(IpAddress):
    """Custom type juniAaaLocalAuthUserIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_JuniAaaLocalAuthUserIpAddress_Object = MibTableColumn
juniAaaLocalAuthUserIpAddress = _JuniAaaLocalAuthUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1, 5),
    _JuniAaaLocalAuthUserIpAddress_Type()
)
juniAaaLocalAuthUserIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserIpAddress.setStatus("current")


class _JuniAaaLocalAuthUserIpAddressPool_Type(DisplayString):
    """Custom type juniAaaLocalAuthUserIpAddressPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniAaaLocalAuthUserIpAddressPool_Type.__name__ = "DisplayString"
_JuniAaaLocalAuthUserIpAddressPool_Object = MibTableColumn
juniAaaLocalAuthUserIpAddressPool = _JuniAaaLocalAuthUserIpAddressPool_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1, 6),
    _JuniAaaLocalAuthUserIpAddressPool_Type()
)
juniAaaLocalAuthUserIpAddressPool.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserIpAddressPool.setStatus("current")
_JuniAaaLocalAuthUserRouterName_Type = JuniName
_JuniAaaLocalAuthUserRouterName_Object = MibTableColumn
juniAaaLocalAuthUserRouterName = _JuniAaaLocalAuthUserRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 1, 1, 1, 7),
    _JuniAaaLocalAuthUserRouterName_Type()
)
juniAaaLocalAuthUserRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserRouterName.setStatus("current")
_JuniAaaLocalAuthUserDb_ObjectIdentity = ObjectIdentity
juniAaaLocalAuthUserDb = _JuniAaaLocalAuthUserDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 2)
)
_JuniAaaLocalAuthUserDbTable_Object = MibTable
juniAaaLocalAuthUserDbTable = _JuniAaaLocalAuthUserDbTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbTable.setStatus("current")
_JuniAaaLocalAuthUserDbEntry_Object = MibTableRow
juniAaaLocalAuthUserDbEntry = _JuniAaaLocalAuthUserDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 2, 1, 1)
)
juniAaaLocalAuthUserDbEntry.setIndexNames(
    (1, "Juniper-AAA-MIB", "juniAaaLocalAuthUserDbName"),
)
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbEntry.setStatus("current")


class _JuniAaaLocalAuthUserDbName_Type(DisplayString):
    """Custom type juniAaaLocalAuthUserDbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniAaaLocalAuthUserDbName_Type.__name__ = "DisplayString"
_JuniAaaLocalAuthUserDbName_Object = MibTableColumn
juniAaaLocalAuthUserDbName = _JuniAaaLocalAuthUserDbName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 2, 1, 1, 1),
    _JuniAaaLocalAuthUserDbName_Type()
)
juniAaaLocalAuthUserDbName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbName.setStatus("current")
_JuniAaaLocalAuthUserDbRowStatus_Type = RowStatus
_JuniAaaLocalAuthUserDbRowStatus_Object = MibTableColumn
juniAaaLocalAuthUserDbRowStatus = _JuniAaaLocalAuthUserDbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 2, 1, 1, 2),
    _JuniAaaLocalAuthUserDbRowStatus_Type()
)
juniAaaLocalAuthUserDbRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbRowStatus.setStatus("current")
_JuniAaaLocalAuthUserDbAssoc_ObjectIdentity = ObjectIdentity
juniAaaLocalAuthUserDbAssoc = _JuniAaaLocalAuthUserDbAssoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 3)
)
_JuniAaaLocalAuthUserDbAssocTable_Object = MibTable
juniAaaLocalAuthUserDbAssocTable = _JuniAaaLocalAuthUserDbAssocTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbAssocTable.setStatus("current")
_JuniAaaLocalAuthUserDbAssocEntry_Object = MibTableRow
juniAaaLocalAuthUserDbAssocEntry = _JuniAaaLocalAuthUserDbAssocEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 3, 1, 1)
)
juniAaaLocalAuthUserDbAssocEntry.setIndexNames(
    (0, "Juniper-ROUTER-MIB", "juniRouterIndex"),
)
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbAssocEntry.setStatus("current")
_JuniAaaLocalAuthUserDbAssocRowStatus_Type = RowStatus
_JuniAaaLocalAuthUserDbAssocRowStatus_Object = MibTableColumn
juniAaaLocalAuthUserDbAssocRowStatus = _JuniAaaLocalAuthUserDbAssocRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 3, 1, 1, 1),
    _JuniAaaLocalAuthUserDbAssocRowStatus_Type()
)
juniAaaLocalAuthUserDbAssocRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbAssocRowStatus.setStatus("current")


class _JuniAaaLocalAuthUserDbAssocDbName_Type(DisplayString):
    """Custom type juniAaaLocalAuthUserDbAssocDbName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_JuniAaaLocalAuthUserDbAssocDbName_Type.__name__ = "DisplayString"
_JuniAaaLocalAuthUserDbAssocDbName_Object = MibTableColumn
juniAaaLocalAuthUserDbAssocDbName = _JuniAaaLocalAuthUserDbAssocDbName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 2, 2, 3, 1, 1, 2),
    _JuniAaaLocalAuthUserDbAssocDbName_Type()
)
juniAaaLocalAuthUserDbAssocDbName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaLocalAuthUserDbAssocDbName.setStatus("current")
_JuniAaaAccounting_ObjectIdentity = ObjectIdentity
juniAaaAccounting = _JuniAaaAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3)
)
_JuniAaaAcctGeneral_ObjectIdentity = ObjectIdentity
juniAaaAcctGeneral = _JuniAaaAcctGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1)
)


class _JuniAaaAcctInterval_Type(Integer32):
    """Custom type juniAaaAcctInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(600, 86400),
    )


_JuniAaaAcctInterval_Type.__name__ = "Integer32"
_JuniAaaAcctInterval_Object = MibScalar
juniAaaAcctInterval = _JuniAaaAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 1),
    _JuniAaaAcctInterval_Type()
)
juniAaaAcctInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaAcctInterval.setUnits("seconds")
_JuniAaaAcctDupServerRouterName_Type = JuniName
_JuniAaaAcctDupServerRouterName_Object = MibScalar
juniAaaAcctDupServerRouterName = _JuniAaaAcctDupServerRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 2),
    _JuniAaaAcctDupServerRouterName_Type()
)
juniAaaAcctDupServerRouterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctDupServerRouterName.setStatus("current")


class _JuniAaaAcctMethods_Type(OctetString):
    """Custom type juniAaaAcctMethods based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JuniAaaAcctMethods_Type.__name__ = "OctetString"
_JuniAaaAcctMethods_Object = MibScalar
juniAaaAcctMethods = _JuniAaaAcctMethods_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 3),
    _JuniAaaAcctMethods_Type()
)
juniAaaAcctMethods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctMethods.setStatus("obsolete")


class _JuniAaaAcctSendStopOnAaaDeny_Type(TruthValue):
    """Custom type juniAaaAcctSendStopOnAaaDeny based on TruthValue"""


_JuniAaaAcctSendStopOnAaaDeny_Object = MibScalar
juniAaaAcctSendStopOnAaaDeny = _JuniAaaAcctSendStopOnAaaDeny_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 4),
    _JuniAaaAcctSendStopOnAaaDeny_Type()
)
juniAaaAcctSendStopOnAaaDeny.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctSendStopOnAaaDeny.setStatus("current")


class _JuniAaaAcctSendStopOnAaaReject_Type(TruthValue):
    """Custom type juniAaaAcctSendStopOnAaaReject based on TruthValue"""


_JuniAaaAcctSendStopOnAaaReject_Object = MibScalar
juniAaaAcctSendStopOnAaaReject = _JuniAaaAcctSendStopOnAaaReject_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 5),
    _JuniAaaAcctSendStopOnAaaReject_Type()
)
juniAaaAcctSendStopOnAaaReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctSendStopOnAaaReject.setStatus("current")


class _JuniAaaAcctSendImmediateAcctUpdate_Type(TruthValue):
    """Custom type juniAaaAcctSendImmediateAcctUpdate based on TruthValue"""


_JuniAaaAcctSendImmediateAcctUpdate_Object = MibScalar
juniAaaAcctSendImmediateAcctUpdate = _JuniAaaAcctSendImmediateAcctUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 6),
    _JuniAaaAcctSendImmediateAcctUpdate_Type()
)
juniAaaAcctSendImmediateAcctUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctSendImmediateAcctUpdate.setStatus("current")
_JuniAaaAcctMethodsTable_Object = MibTable
juniAaaAcctMethodsTable = _JuniAaaAcctMethodsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    juniAaaAcctMethodsTable.setStatus("current")
_JuniAaaAcctMethodsEntry_Object = MibTableRow
juniAaaAcctMethodsEntry = _JuniAaaAcctMethodsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 7, 1)
)
juniAaaAcctMethodsEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaAcctMethodsSubscriberType"),
)
if mibBuilder.loadTexts:
    juniAaaAcctMethodsEntry.setStatus("current")
_JuniAaaAcctMethodsSubscriberType_Type = JuniAaaAccountingSubscriberTypes
_JuniAaaAcctMethodsSubscriberType_Object = MibTableColumn
juniAaaAcctMethodsSubscriberType = _JuniAaaAcctMethodsSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 7, 1, 1),
    _JuniAaaAcctMethodsSubscriberType_Type()
)
juniAaaAcctMethodsSubscriberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAcctMethodsSubscriberType.setStatus("current")


class _JuniAaaAcctMethodsAccounting_Type(OctetString):
    """Custom type juniAaaAcctMethodsAccounting based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_JuniAaaAcctMethodsAccounting_Type.__name__ = "OctetString"
_JuniAaaAcctMethodsAccounting_Object = MibTableColumn
juniAaaAcctMethodsAccounting = _JuniAaaAcctMethodsAccounting_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 7, 1, 2),
    _JuniAaaAcctMethodsAccounting_Type()
)
juniAaaAcctMethodsAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctMethodsAccounting.setStatus("current")
_JuniAaaAcctBcastServerGroupName_Type = JuniVrfGroupName
_JuniAaaAcctBcastServerGroupName_Object = MibScalar
juniAaaAcctBcastServerGroupName = _JuniAaaAcctBcastServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 8),
    _JuniAaaAcctBcastServerGroupName_Type()
)
juniAaaAcctBcastServerGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupName.setStatus("current")


class _JuniAaaUserAcctInterval_Type(Integer32):
    """Custom type juniAaaUserAcctInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(600, 86400),
    )


_JuniAaaUserAcctInterval_Type.__name__ = "Integer32"
_JuniAaaUserAcctInterval_Object = MibScalar
juniAaaUserAcctInterval = _JuniAaaUserAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 9),
    _JuniAaaUserAcctInterval_Type()
)
juniAaaUserAcctInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaUserAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaUserAcctInterval.setUnits("seconds")


class _JuniAaaServiceAcctInterval_Type(Integer32):
    """Custom type juniAaaServiceAcctInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(600, 86400),
    )


_JuniAaaServiceAcctInterval_Type.__name__ = "Integer32"
_JuniAaaServiceAcctInterval_Object = MibScalar
juniAaaServiceAcctInterval = _JuniAaaServiceAcctInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 1, 10),
    _JuniAaaServiceAcctInterval_Type()
)
juniAaaServiceAcctInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaServiceAcctInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaServiceAcctInterval.setUnits("seconds")
_JuniAaaAcctBcastConfig_ObjectIdentity = ObjectIdentity
juniAaaAcctBcastConfig = _JuniAaaAcctBcastConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2)
)
_JuniAaaAcctBcastServerGroupTable_Object = MibTable
juniAaaAcctBcastServerGroupTable = _JuniAaaAcctBcastServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupTable.setStatus("current")
_JuniAaaAcctBcastServerGroupEntry_Object = MibTableRow
juniAaaAcctBcastServerGroupEntry = _JuniAaaAcctBcastServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1, 1)
)
juniAaaAcctBcastServerGroupEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaAcctBcastServerGroup"),
)
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupEntry.setStatus("current")
_JuniAaaAcctBcastServerGroup_Type = JuniVrfGroupName
_JuniAaaAcctBcastServerGroup_Object = MibTableColumn
juniAaaAcctBcastServerGroup = _JuniAaaAcctBcastServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1, 1, 1),
    _JuniAaaAcctBcastServerGroup_Type()
)
juniAaaAcctBcastServerGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroup.setStatus("current")
_JuniAaaAcctBcastServerGroupRouter1_Type = JuniName
_JuniAaaAcctBcastServerGroupRouter1_Object = MibTableColumn
juniAaaAcctBcastServerGroupRouter1 = _JuniAaaAcctBcastServerGroupRouter1_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1, 1, 2),
    _JuniAaaAcctBcastServerGroupRouter1_Type()
)
juniAaaAcctBcastServerGroupRouter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupRouter1.setStatus("current")
_JuniAaaAcctBcastServerGroupRouter2_Type = JuniName
_JuniAaaAcctBcastServerGroupRouter2_Object = MibTableColumn
juniAaaAcctBcastServerGroupRouter2 = _JuniAaaAcctBcastServerGroupRouter2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1, 1, 3),
    _JuniAaaAcctBcastServerGroupRouter2_Type()
)
juniAaaAcctBcastServerGroupRouter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupRouter2.setStatus("current")
_JuniAaaAcctBcastServerGroupRouter3_Type = JuniName
_JuniAaaAcctBcastServerGroupRouter3_Object = MibTableColumn
juniAaaAcctBcastServerGroupRouter3 = _JuniAaaAcctBcastServerGroupRouter3_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1, 1, 4),
    _JuniAaaAcctBcastServerGroupRouter3_Type()
)
juniAaaAcctBcastServerGroupRouter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupRouter3.setStatus("current")
_JuniAaaAcctBcastServerGroupRouter4_Type = JuniName
_JuniAaaAcctBcastServerGroupRouter4_Object = MibTableColumn
juniAaaAcctBcastServerGroupRouter4 = _JuniAaaAcctBcastServerGroupRouter4_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1, 1, 5),
    _JuniAaaAcctBcastServerGroupRouter4_Type()
)
juniAaaAcctBcastServerGroupRouter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupRouter4.setStatus("current")
_JuniAaaAcctBcastServerGroupRowStatus_Type = RowStatus
_JuniAaaAcctBcastServerGroupRowStatus_Object = MibTableColumn
juniAaaAcctBcastServerGroupRowStatus = _JuniAaaAcctBcastServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 3, 2, 1, 1, 6),
    _JuniAaaAcctBcastServerGroupRowStatus_Type()
)
juniAaaAcctBcastServerGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAcctBcastServerGroupRowStatus.setStatus("current")
_JuniAaaAddress_ObjectIdentity = ObjectIdentity
juniAaaAddress = _JuniAaaAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4)
)
_JuniAaaAddrGeneral_ObjectIdentity = ObjectIdentity
juniAaaAddrGeneral = _JuniAaaAddrGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 1)
)


class _JuniAaaAddrPoolDefault_Type(Integer32):
    """Custom type juniAaaAddrPoolDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("local", 1),
          ("none", 0))
    )


_JuniAaaAddrPoolDefault_Type.__name__ = "Integer32"
_JuniAaaAddrPoolDefault_Object = MibScalar
juniAaaAddrPoolDefault = _JuniAaaAddrPoolDefault_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 1, 1),
    _JuniAaaAddrPoolDefault_Type()
)
juniAaaAddrPoolDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAddrPoolDefault.setStatus("current")
_JuniAaaDupAddrCheck_Type = TruthValue
_JuniAaaDupAddrCheck_Object = MibScalar
juniAaaDupAddrCheck = _JuniAaaDupAddrCheck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 1, 2),
    _JuniAaaDupAddrCheck_Type()
)
juniAaaDupAddrCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaDupAddrCheck.setStatus("current")
_JuniAaaAddrNameServer_ObjectIdentity = ObjectIdentity
juniAaaAddrNameServer = _JuniAaaAddrNameServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2)
)
_JuniAaaAddrDns_ObjectIdentity = ObjectIdentity
juniAaaAddrDns = _JuniAaaAddrDns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1)
)
_JuniAaaAddrDnsPrimary_Type = IpAddress
_JuniAaaAddrDnsPrimary_Object = MibScalar
juniAaaAddrDnsPrimary = _JuniAaaAddrDnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1, 1),
    _JuniAaaAddrDnsPrimary_Type()
)
juniAaaAddrDnsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAddrDnsPrimary.setStatus("current")
_JuniAaaAddrDnsSecondary_Type = IpAddress
_JuniAaaAddrDnsSecondary_Object = MibScalar
juniAaaAddrDnsSecondary = _JuniAaaAddrDnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1, 2),
    _JuniAaaAddrDnsSecondary_Type()
)
juniAaaAddrDnsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAddrDnsSecondary.setStatus("current")
_JuniAaaAddrIpv6DnsPrimary_Type = Ipv6Address
_JuniAaaAddrIpv6DnsPrimary_Object = MibScalar
juniAaaAddrIpv6DnsPrimary = _JuniAaaAddrIpv6DnsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1, 3),
    _JuniAaaAddrIpv6DnsPrimary_Type()
)
juniAaaAddrIpv6DnsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAddrIpv6DnsPrimary.setStatus("current")
_JuniAaaAddrIpv6DnsSecondary_Type = Ipv6Address
_JuniAaaAddrIpv6DnsSecondary_Object = MibScalar
juniAaaAddrIpv6DnsSecondary = _JuniAaaAddrIpv6DnsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 1, 4),
    _JuniAaaAddrIpv6DnsSecondary_Type()
)
juniAaaAddrIpv6DnsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAddrIpv6DnsSecondary.setStatus("current")
_JuniAaaAddrWins_ObjectIdentity = ObjectIdentity
juniAaaAddrWins = _JuniAaaAddrWins_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 2)
)
_JuniAaaAddrWinsPrimary_Type = IpAddress
_JuniAaaAddrWinsPrimary_Object = MibScalar
juniAaaAddrWinsPrimary = _JuniAaaAddrWinsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 2, 1),
    _JuniAaaAddrWinsPrimary_Type()
)
juniAaaAddrWinsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAddrWinsPrimary.setStatus("current")
_JuniAaaAddrWinsSecondary_Type = IpAddress
_JuniAaaAddrWinsSecondary_Object = MibScalar
juniAaaAddrWinsSecondary = _JuniAaaAddrWinsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 4, 2, 2, 2),
    _JuniAaaAddrWinsSecondary_Type()
)
juniAaaAddrWinsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaAddrWinsSecondary.setStatus("current")
_JuniAaaStatistics_ObjectIdentity = ObjectIdentity
juniAaaStatistics = _JuniAaaStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5)
)
_JuniAaaIncomingInitiateRequests_Type = Counter32
_JuniAaaIncomingInitiateRequests_Object = MibScalar
juniAaaIncomingInitiateRequests = _JuniAaaIncomingInitiateRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 1),
    _JuniAaaIncomingInitiateRequests_Type()
)
juniAaaIncomingInitiateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingInitiateRequests.setStatus("current")
_JuniAaaIncomingTerminateRequests_Type = Counter32
_JuniAaaIncomingTerminateRequests_Object = MibScalar
juniAaaIncomingTerminateRequests = _JuniAaaIncomingTerminateRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 2),
    _JuniAaaIncomingTerminateRequests_Type()
)
juniAaaIncomingTerminateRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingTerminateRequests.setStatus("current")
_JuniAaaOutgoingTunnelGrantResponses_Type = Counter32
_JuniAaaOutgoingTunnelGrantResponses_Object = MibScalar
juniAaaOutgoingTunnelGrantResponses = _JuniAaaOutgoingTunnelGrantResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 3),
    _JuniAaaOutgoingTunnelGrantResponses_Type()
)
juniAaaOutgoingTunnelGrantResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingTunnelGrantResponses.setStatus("current")
_JuniAaaOutgoingGrantResponses_Type = Counter32
_JuniAaaOutgoingGrantResponses_Object = MibScalar
juniAaaOutgoingGrantResponses = _JuniAaaOutgoingGrantResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 4),
    _JuniAaaOutgoingGrantResponses_Type()
)
juniAaaOutgoingGrantResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingGrantResponses.setStatus("current")
_JuniAaaOutgoingDenyResponses_Type = Counter32
_JuniAaaOutgoingDenyResponses_Object = MibScalar
juniAaaOutgoingDenyResponses = _JuniAaaOutgoingDenyResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 5),
    _JuniAaaOutgoingDenyResponses_Type()
)
juniAaaOutgoingDenyResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingDenyResponses.setStatus("current")
_JuniAaaOutgoingErrorResponses_Type = Counter32
_JuniAaaOutgoingErrorResponses_Object = MibScalar
juniAaaOutgoingErrorResponses = _JuniAaaOutgoingErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 6),
    _JuniAaaOutgoingErrorResponses_Type()
)
juniAaaOutgoingErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingErrorResponses.setStatus("current")
_JuniAaaOutgoingAuthRequests_Type = Counter32
_JuniAaaOutgoingAuthRequests_Object = MibScalar
juniAaaOutgoingAuthRequests = _JuniAaaOutgoingAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 7),
    _JuniAaaOutgoingAuthRequests_Type()
)
juniAaaOutgoingAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingAuthRequests.setStatus("current")
_JuniAaaIncomingAuthResponses_Type = Counter32
_JuniAaaIncomingAuthResponses_Object = MibScalar
juniAaaIncomingAuthResponses = _JuniAaaIncomingAuthResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 8),
    _JuniAaaIncomingAuthResponses_Type()
)
juniAaaIncomingAuthResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingAuthResponses.setStatus("current")
_JuniAaaOutgoingReAuthRequests_Type = Counter32
_JuniAaaOutgoingReAuthRequests_Object = MibScalar
juniAaaOutgoingReAuthRequests = _JuniAaaOutgoingReAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 9),
    _JuniAaaOutgoingReAuthRequests_Type()
)
juniAaaOutgoingReAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingReAuthRequests.setStatus("current")
_JuniAaaIncomingReAuthResponses_Type = Counter32
_JuniAaaIncomingReAuthResponses_Object = MibScalar
juniAaaIncomingReAuthResponses = _JuniAaaIncomingReAuthResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 10),
    _JuniAaaIncomingReAuthResponses_Type()
)
juniAaaIncomingReAuthResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingReAuthResponses.setStatus("current")
_JuniAaaOutgoingAcctRequests_Type = Counter32
_JuniAaaOutgoingAcctRequests_Object = MibScalar
juniAaaOutgoingAcctRequests = _JuniAaaOutgoingAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 11),
    _JuniAaaOutgoingAcctRequests_Type()
)
juniAaaOutgoingAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingAcctRequests.setStatus("current")
_JuniAaaIncomingAcctResponses_Type = Counter32
_JuniAaaIncomingAcctResponses_Object = MibScalar
juniAaaIncomingAcctResponses = _JuniAaaIncomingAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 12),
    _JuniAaaIncomingAcctResponses_Type()
)
juniAaaIncomingAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingAcctResponses.setStatus("current")
_JuniAaaOutgoingDupAcctRequests_Type = Counter32
_JuniAaaOutgoingDupAcctRequests_Object = MibScalar
juniAaaOutgoingDupAcctRequests = _JuniAaaOutgoingDupAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 13),
    _JuniAaaOutgoingDupAcctRequests_Type()
)
juniAaaOutgoingDupAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingDupAcctRequests.setStatus("current")
_JuniAaaIncomingDupAcctResponses_Type = Counter32
_JuniAaaIncomingDupAcctResponses_Object = MibScalar
juniAaaIncomingDupAcctResponses = _JuniAaaIncomingDupAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 14),
    _JuniAaaIncomingDupAcctResponses_Type()
)
juniAaaIncomingDupAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingDupAcctResponses.setStatus("current")
_JuniAaaOutgoingAddrRequests_Type = Counter32
_JuniAaaOutgoingAddrRequests_Object = MibScalar
juniAaaOutgoingAddrRequests = _JuniAaaOutgoingAddrRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 15),
    _JuniAaaOutgoingAddrRequests_Type()
)
juniAaaOutgoingAddrRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingAddrRequests.setStatus("current")
_JuniAaaIncomingAddrResponses_Type = Counter32
_JuniAaaIncomingAddrResponses_Object = MibScalar
juniAaaIncomingAddrResponses = _JuniAaaIncomingAddrResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 16),
    _JuniAaaIncomingAddrResponses_Type()
)
juniAaaIncomingAddrResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingAddrResponses.setStatus("current")
_JuniAaaOutgoingBcastAcctRequests_Type = Counter32
_JuniAaaOutgoingBcastAcctRequests_Object = MibScalar
juniAaaOutgoingBcastAcctRequests = _JuniAaaOutgoingBcastAcctRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 17),
    _JuniAaaOutgoingBcastAcctRequests_Type()
)
juniAaaOutgoingBcastAcctRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaOutgoingBcastAcctRequests.setStatus("current")
_JuniAaaIncomingBcastAcctResponses_Type = Counter32
_JuniAaaIncomingBcastAcctResponses_Object = MibScalar
juniAaaIncomingBcastAcctResponses = _JuniAaaIncomingBcastAcctResponses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 5, 18),
    _JuniAaaIncomingBcastAcctResponses_Type()
)
juniAaaIncomingBcastAcctResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaIncomingBcastAcctResponses.setStatus("current")
_JuniAaaTimeout_ObjectIdentity = ObjectIdentity
juniAaaTimeout = _JuniAaaTimeout_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6)
)
_JuniAaaTimeoutGeneral_ObjectIdentity = ObjectIdentity
juniAaaTimeoutGeneral = _JuniAaaTimeoutGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6, 1)
)


class _JuniAaaIdleTimeout_Type(Integer32):
    """Custom type juniAaaIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 86400),
    )


_JuniAaaIdleTimeout_Type.__name__ = "Integer32"
_JuniAaaIdleTimeout_Object = MibScalar
juniAaaIdleTimeout = _JuniAaaIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6, 1, 1),
    _JuniAaaIdleTimeout_Type()
)
juniAaaIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaIdleTimeout.setUnits("seconds")


class _JuniAaaSessionTimeout_Type(Integer32):
    """Custom type juniAaaSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 31622400),
    )


_JuniAaaSessionTimeout_Type.__name__ = "Integer32"
_JuniAaaSessionTimeout_Object = MibScalar
juniAaaSessionTimeout = _JuniAaaSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6, 1, 2),
    _JuniAaaSessionTimeout_Type()
)
juniAaaSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniAaaSessionTimeout.setUnits("seconds")


class _JuniAaaMonitorIngressTrafficOnly_Type(JuniEnable):
    """Custom type juniAaaMonitorIngressTrafficOnly based on JuniEnable"""


_JuniAaaMonitorIngressTrafficOnly_Object = MibScalar
juniAaaMonitorIngressTrafficOnly = _JuniAaaMonitorIngressTrafficOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 6, 1, 3),
    _JuniAaaMonitorIngressTrafficOnly_Type()
)
juniAaaMonitorIngressTrafficOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaMonitorIngressTrafficOnly.setStatus("current")
_JuniAaaTunnel_ObjectIdentity = ObjectIdentity
juniAaaTunnel = _JuniAaaTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7)
)
_JuniAaaTunnelGeneral_ObjectIdentity = ObjectIdentity
juniAaaTunnelGeneral = _JuniAaaTunnelGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1)
)


class _JuniAaaTunnelClientName_Type(DisplayString):
    """Custom type juniAaaTunnelClientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniAaaTunnelClientName_Type.__name__ = "DisplayString"
_JuniAaaTunnelClientName_Object = MibScalar
juniAaaTunnelClientName = _JuniAaaTunnelClientName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 1),
    _JuniAaaTunnelClientName_Type()
)
juniAaaTunnelClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelClientName.setStatus("current")


class _JuniAaaTunnelPassword_Type(DisplayString):
    """Custom type juniAaaTunnelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaTunnelPassword_Type.__name__ = "DisplayString"
_JuniAaaTunnelPassword_Object = MibScalar
juniAaaTunnelPassword = _JuniAaaTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 2),
    _JuniAaaTunnelPassword_Type()
)
juniAaaTunnelPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelPassword.setStatus("current")


class _JuniAaaTunnelNasPortMethod_Type(Integer32):
    """Custom type juniAaaTunnelNasPortMethod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ciscoAvp", 1),
          ("none", 0))
    )


_JuniAaaTunnelNasPortMethod_Type.__name__ = "Integer32"
_JuniAaaTunnelNasPortMethod_Object = MibScalar
juniAaaTunnelNasPortMethod = _JuniAaaTunnelNasPortMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 3),
    _JuniAaaTunnelNasPortMethod_Type()
)
juniAaaTunnelNasPortMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelNasPortMethod.setStatus("current")
_JuniAaaTunnelIgnoreNasPort_Type = TruthValue
_JuniAaaTunnelIgnoreNasPort_Object = MibScalar
juniAaaTunnelIgnoreNasPort = _JuniAaaTunnelIgnoreNasPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 4),
    _JuniAaaTunnelIgnoreNasPort_Type()
)
juniAaaTunnelIgnoreNasPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelIgnoreNasPort.setStatus("current")
_JuniAaaTunnelIgnoreNasPortType_Type = TruthValue
_JuniAaaTunnelIgnoreNasPortType_Object = MibScalar
juniAaaTunnelIgnoreNasPortType = _JuniAaaTunnelIgnoreNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 5),
    _JuniAaaTunnelIgnoreNasPortType_Type()
)
juniAaaTunnelIgnoreNasPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelIgnoreNasPortType.setStatus("current")


class _JuniAaaTunnelAssignmentIdFormat_Type(Integer32):
    """Custom type juniAaaTunnelAssignmentIdFormat based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("assignmentId", 0),
          ("clientServerId", 1))
    )


_JuniAaaTunnelAssignmentIdFormat_Type.__name__ = "Integer32"
_JuniAaaTunnelAssignmentIdFormat_Object = MibScalar
juniAaaTunnelAssignmentIdFormat = _JuniAaaTunnelAssignmentIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 6),
    _JuniAaaTunnelAssignmentIdFormat_Type()
)
juniAaaTunnelAssignmentIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelAssignmentIdFormat.setStatus("current")
_JuniAaaTunnelSwitchProfile_Type = JuniAaaTunnelSwitchProfileName
_JuniAaaTunnelSwitchProfile_Object = MibScalar
juniAaaTunnelSwitchProfile = _JuniAaaTunnelSwitchProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 7),
    _JuniAaaTunnelSwitchProfile_Type()
)
juniAaaTunnelSwitchProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelSwitchProfile.setStatus("current")


class _JuniAaaTunnelTxConnectSpeedMethod_Type(Integer32):
    """Custom type juniAaaTunnelTxConnectSpeedMethod based on Integer32"""
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
        *(("actual", 4),
          ("dynamicLayer2", 2),
          ("notSet", 0),
          ("qos", 3),
          ("staticLayer2", 1))
    )


_JuniAaaTunnelTxConnectSpeedMethod_Type.__name__ = "Integer32"
_JuniAaaTunnelTxConnectSpeedMethod_Object = MibScalar
juniAaaTunnelTxConnectSpeedMethod = _JuniAaaTunnelTxConnectSpeedMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 1, 8),
    _JuniAaaTunnelTxConnectSpeedMethod_Type()
)
juniAaaTunnelTxConnectSpeedMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaTunnelTxConnectSpeedMethod.setStatus("current")
_JuniAaaTunnelGroups_ObjectIdentity = ObjectIdentity
juniAaaTunnelGroups = _JuniAaaTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2)
)
_JuniAaaTunnelGroupTable_Object = MibTable
juniAaaTunnelGroupTable = _JuniAaaTunnelGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTable.setStatus("current")
_JuniAaaTunnelGroupEntry_Object = MibTableRow
juniAaaTunnelGroupEntry = _JuniAaaTunnelGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 1, 1)
)
juniAaaTunnelGroupEntry.setIndexNames(
    (1, "Juniper-AAA-MIB", "juniAaaTunnelGroupName"),
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroupEntry.setStatus("current")
_JuniAaaTunnelGroupName_Type = JuniAaaTunnelGroupName
_JuniAaaTunnelGroupName_Object = MibTableColumn
juniAaaTunnelGroupName = _JuniAaaTunnelGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 1, 1, 1),
    _JuniAaaTunnelGroupName_Type()
)
juniAaaTunnelGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupName.setStatus("current")
_JuniAaaTunnelGroupRowStatus_Type = RowStatus
_JuniAaaTunnelGroupRowStatus_Object = MibTableColumn
juniAaaTunnelGroupRowStatus = _JuniAaaTunnelGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 1, 1, 2),
    _JuniAaaTunnelGroupRowStatus_Type()
)
juniAaaTunnelGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupRowStatus.setStatus("current")
_JuniAaaTunnelGroupTunnelTable_Object = MibTable
juniAaaTunnelGroupTunnelTable = _JuniAaaTunnelGroupTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2)
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelTable.setStatus("current")
_JuniAaaTunnelGroupTunnelEntry_Object = MibTableRow
juniAaaTunnelGroupTunnelEntry = _JuniAaaTunnelGroupTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1)
)
juniAaaTunnelGroupTunnelEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelName"),
    (0, "Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelTag"),
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelEntry.setStatus("current")
_JuniAaaTunnelGroupTunnelName_Type = JuniAaaTunnelGroupName
_JuniAaaTunnelGroupTunnelName_Object = MibTableColumn
juniAaaTunnelGroupTunnelName = _JuniAaaTunnelGroupTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 1),
    _JuniAaaTunnelGroupTunnelName_Type()
)
juniAaaTunnelGroupTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelName.setStatus("current")


class _JuniAaaTunnelGroupTunnelTag_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_JuniAaaTunnelGroupTunnelTag_Type.__name__ = "Integer32"
_JuniAaaTunnelGroupTunnelTag_Object = MibTableColumn
juniAaaTunnelGroupTunnelTag = _JuniAaaTunnelGroupTunnelTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 2),
    _JuniAaaTunnelGroupTunnelTag_Type()
)
juniAaaTunnelGroupTunnelTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelTag.setStatus("current")


class _JuniAaaTunnelGroupTunnelPreference_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelPreference based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_JuniAaaTunnelGroupTunnelPreference_Type.__name__ = "Integer32"
_JuniAaaTunnelGroupTunnelPreference_Object = MibTableColumn
juniAaaTunnelGroupTunnelPreference = _JuniAaaTunnelGroupTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 3),
    _JuniAaaTunnelGroupTunnelPreference_Type()
)
juniAaaTunnelGroupTunnelPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelPreference.setStatus("current")


class _JuniAaaTunnelGroupTunnelType_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("tunnelL2tp", 1)
    )


_JuniAaaTunnelGroupTunnelType_Type.__name__ = "Integer32"
_JuniAaaTunnelGroupTunnelType_Object = MibTableColumn
juniAaaTunnelGroupTunnelType = _JuniAaaTunnelGroupTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 4),
    _JuniAaaTunnelGroupTunnelType_Type()
)
juniAaaTunnelGroupTunnelType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelType.setStatus("current")


class _JuniAaaTunnelGroupTunnelMedium_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelMedium based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnelMediumIPv4", 1),
          ("tunnelMediumUnknown", 2))
    )


_JuniAaaTunnelGroupTunnelMedium_Type.__name__ = "Integer32"
_JuniAaaTunnelGroupTunnelMedium_Object = MibTableColumn
juniAaaTunnelGroupTunnelMedium = _JuniAaaTunnelGroupTunnelMedium_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 5),
    _JuniAaaTunnelGroupTunnelMedium_Type()
)
juniAaaTunnelGroupTunnelMedium.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelMedium.setStatus("current")


class _JuniAaaTunnelGroupTunnelAddress_Type(DisplayString):
    """Custom type juniAaaTunnelGroupTunnelAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaTunnelGroupTunnelAddress_Type.__name__ = "DisplayString"
_JuniAaaTunnelGroupTunnelAddress_Object = MibTableColumn
juniAaaTunnelGroupTunnelAddress = _JuniAaaTunnelGroupTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 6),
    _JuniAaaTunnelGroupTunnelAddress_Type()
)
juniAaaTunnelGroupTunnelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelAddress.setStatus("current")


class _JuniAaaTunnelGroupTunnelPassword_Type(DisplayString):
    """Custom type juniAaaTunnelGroupTunnelPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaTunnelGroupTunnelPassword_Type.__name__ = "DisplayString"
_JuniAaaTunnelGroupTunnelPassword_Object = MibTableColumn
juniAaaTunnelGroupTunnelPassword = _JuniAaaTunnelGroupTunnelPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 7),
    _JuniAaaTunnelGroupTunnelPassword_Type()
)
juniAaaTunnelGroupTunnelPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelPassword.setStatus("current")


class _JuniAaaTunnelGroupTunnelId_Type(DisplayString):
    """Custom type juniAaaTunnelGroupTunnelId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaTunnelGroupTunnelId_Type.__name__ = "DisplayString"
_JuniAaaTunnelGroupTunnelId_Object = MibTableColumn
juniAaaTunnelGroupTunnelId = _JuniAaaTunnelGroupTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 8),
    _JuniAaaTunnelGroupTunnelId_Type()
)
juniAaaTunnelGroupTunnelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelId.setStatus("current")


class _JuniAaaTunnelGroupTunnelHostName_Type(DisplayString):
    """Custom type juniAaaTunnelGroupTunnelHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniAaaTunnelGroupTunnelHostName_Type.__name__ = "DisplayString"
_JuniAaaTunnelGroupTunnelHostName_Object = MibTableColumn
juniAaaTunnelGroupTunnelHostName = _JuniAaaTunnelGroupTunnelHostName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 9),
    _JuniAaaTunnelGroupTunnelHostName_Type()
)
juniAaaTunnelGroupTunnelHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelHostName.setStatus("current")
_JuniAaaTunnelGroupTunnelRowStatus_Type = RowStatus
_JuniAaaTunnelGroupTunnelRowStatus_Object = MibTableColumn
juniAaaTunnelGroupTunnelRowStatus = _JuniAaaTunnelGroupTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 10),
    _JuniAaaTunnelGroupTunnelRowStatus_Type()
)
juniAaaTunnelGroupTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelRowStatus.setStatus("current")


class _JuniAaaTunnelGroupTunnelServerName_Type(DisplayString):
    """Custom type juniAaaTunnelGroupTunnelServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniAaaTunnelGroupTunnelServerName_Type.__name__ = "DisplayString"
_JuniAaaTunnelGroupTunnelServerName_Object = MibTableColumn
juniAaaTunnelGroupTunnelServerName = _JuniAaaTunnelGroupTunnelServerName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 11),
    _JuniAaaTunnelGroupTunnelServerName_Type()
)
juniAaaTunnelGroupTunnelServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelServerName.setStatus("current")


class _JuniAaaTunnelGroupTunnelClientAddress_Type(DisplayString):
    """Custom type juniAaaTunnelGroupTunnelClientAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniAaaTunnelGroupTunnelClientAddress_Type.__name__ = "DisplayString"
_JuniAaaTunnelGroupTunnelClientAddress_Object = MibTableColumn
juniAaaTunnelGroupTunnelClientAddress = _JuniAaaTunnelGroupTunnelClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 12),
    _JuniAaaTunnelGroupTunnelClientAddress_Type()
)
juniAaaTunnelGroupTunnelClientAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelClientAddress.setStatus("current")


class _JuniAaaTunnelGroupTunnelMaxSessions_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelMaxSessions based on Integer32"""
    defaultValue = 1000


_JuniAaaTunnelGroupTunnelMaxSessions_Object = MibTableColumn
juniAaaTunnelGroupTunnelMaxSessions = _JuniAaaTunnelGroupTunnelMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 13),
    _JuniAaaTunnelGroupTunnelMaxSessions_Type()
)
juniAaaTunnelGroupTunnelMaxSessions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelMaxSessions.setStatus("current")


class _JuniAaaTunnelGroupTunnelReceiveWindowSize_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelReceiveWindowSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4, 4),
    )


_JuniAaaTunnelGroupTunnelReceiveWindowSize_Type.__name__ = "Integer32"
_JuniAaaTunnelGroupTunnelReceiveWindowSize_Object = MibTableColumn
juniAaaTunnelGroupTunnelReceiveWindowSize = _JuniAaaTunnelGroupTunnelReceiveWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 14),
    _JuniAaaTunnelGroupTunnelReceiveWindowSize_Type()
)
juniAaaTunnelGroupTunnelReceiveWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelReceiveWindowSize.setStatus("current")
_JuniAaaTunnelGroupTunnelRouterName_Type = JuniName
_JuniAaaTunnelGroupTunnelRouterName_Object = MibTableColumn
juniAaaTunnelGroupTunnelRouterName = _JuniAaaTunnelGroupTunnelRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 15),
    _JuniAaaTunnelGroupTunnelRouterName_Type()
)
juniAaaTunnelGroupTunnelRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelRouterName.setStatus("current")


class _JuniAaaTunnelGroupTunnelFailoverResync_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelFailoverResync based on Integer32"""
    defaultValue = 4

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
        *(("disable", 0),
          ("failoverProtocol", 1),
          ("failoverProtocolFallbackToSilentFailover", 3),
          ("notConfigured", 4),
          ("silentFailover", 2))
    )


_JuniAaaTunnelGroupTunnelFailoverResync_Type.__name__ = "Integer32"
_JuniAaaTunnelGroupTunnelFailoverResync_Object = MibTableColumn
juniAaaTunnelGroupTunnelFailoverResync = _JuniAaaTunnelGroupTunnelFailoverResync_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 16),
    _JuniAaaTunnelGroupTunnelFailoverResync_Type()
)
juniAaaTunnelGroupTunnelFailoverResync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelFailoverResync.setStatus("current")
_JuniAaaTunnelGroupTunnelSwitchProfile_Type = JuniAaaTunnelSwitchProfileName
_JuniAaaTunnelGroupTunnelSwitchProfile_Object = MibTableColumn
juniAaaTunnelGroupTunnelSwitchProfile = _JuniAaaTunnelGroupTunnelSwitchProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 17),
    _JuniAaaTunnelGroupTunnelSwitchProfile_Type()
)
juniAaaTunnelGroupTunnelSwitchProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelSwitchProfile.setStatus("current")


class _JuniAaaTunnelGroupTunnelTxConnectSpeedMethod_Type(Integer32):
    """Custom type juniAaaTunnelGroupTunnelTxConnectSpeedMethod based on Integer32"""
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
        *(("actual", 4),
          ("dynamicLayer2", 2),
          ("notSet", 0),
          ("qos", 3),
          ("staticLayer2", 1))
    )


_JuniAaaTunnelGroupTunnelTxConnectSpeedMethod_Type.__name__ = "Integer32"
_JuniAaaTunnelGroupTunnelTxConnectSpeedMethod_Object = MibTableColumn
juniAaaTunnelGroupTunnelTxConnectSpeedMethod = _JuniAaaTunnelGroupTunnelTxConnectSpeedMethod_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 7, 2, 2, 1, 18),
    _JuniAaaTunnelGroupTunnelTxConnectSpeedMethod_Type()
)
juniAaaTunnelGroupTunnelTxConnectSpeedMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniAaaTunnelGroupTunnelTxConnectSpeedMethod.setStatus("current")
_JuniAaaSubscribers_ObjectIdentity = ObjectIdentity
juniAaaSubscribers = _JuniAaaSubscribers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8)
)
_JuniAaaSubscriberMaxCount_Type = Integer32
_JuniAaaSubscriberMaxCount_Object = MibScalar
juniAaaSubscriberMaxCount = _JuniAaaSubscriberMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 1),
    _JuniAaaSubscriberMaxCount_Type()
)
juniAaaSubscriberMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberMaxCount.setStatus("current")
_JuniAaaSubscriberPeakCount_Type = Gauge32
_JuniAaaSubscriberPeakCount_Object = MibScalar
juniAaaSubscriberPeakCount = _JuniAaaSubscriberPeakCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 2),
    _JuniAaaSubscriberPeakCount_Type()
)
juniAaaSubscriberPeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberPeakCount.setStatus("current")
_JuniAaaSubscriberCount_Type = Gauge32
_JuniAaaSubscriberCount_Object = MibScalar
juniAaaSubscriberCount = _JuniAaaSubscriberCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 3),
    _JuniAaaSubscriberCount_Type()
)
juniAaaSubscriberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberCount.setStatus("current")
_JuniAaaSubscriberTable_Object = MibTable
juniAaaSubscriberTable = _JuniAaaSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberTable.setStatus("current")
_JuniAaaSubscriberEntry_Object = MibTableRow
juniAaaSubscriberEntry = _JuniAaaSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1)
)
juniAaaSubscriberEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberHandle"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberEntry.setStatus("current")
_JuniAaaSubscriberHandle_Type = Unsigned32
_JuniAaaSubscriberHandle_Object = MibTableColumn
juniAaaSubscriberHandle = _JuniAaaSubscriberHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 1),
    _JuniAaaSubscriberHandle_Type()
)
juniAaaSubscriberHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberHandle.setStatus("current")
_JuniAaaSubscriberUserName_Type = DisplayString
_JuniAaaSubscriberUserName_Object = MibTableColumn
juniAaaSubscriberUserName = _JuniAaaSubscriberUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 2),
    _JuniAaaSubscriberUserName_Type()
)
juniAaaSubscriberUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberUserName.setStatus("current")
_JuniAaaSubscriberRouterName_Type = JuniName
_JuniAaaSubscriberRouterName_Object = MibTableColumn
juniAaaSubscriberRouterName = _JuniAaaSubscriberRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 3),
    _JuniAaaSubscriberRouterName_Type()
)
juniAaaSubscriberRouterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterName.setStatus("current")
_JuniAaaSubscriberRouterIndex_Type = Unsigned32
_JuniAaaSubscriberRouterIndex_Object = MibTableColumn
juniAaaSubscriberRouterIndex = _JuniAaaSubscriberRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 4),
    _JuniAaaSubscriberRouterIndex_Type()
)
juniAaaSubscriberRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterIndex.setStatus("current")
_JuniAaaSubscriberLoginTime_Type = DisplayString
_JuniAaaSubscriberLoginTime_Object = MibTableColumn
juniAaaSubscriberLoginTime = _JuniAaaSubscriberLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 5),
    _JuniAaaSubscriberLoginTime_Type()
)
juniAaaSubscriberLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberLoginTime.setStatus("current")
_JuniAaaSubscriberIpAddress_Type = IpAddress
_JuniAaaSubscriberIpAddress_Object = MibTableColumn
juniAaaSubscriberIpAddress = _JuniAaaSubscriberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 6),
    _JuniAaaSubscriberIpAddress_Type()
)
juniAaaSubscriberIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberIpAddress.setStatus("current")
_JuniAaaSubscriberIpAddressMask_Type = IpAddress
_JuniAaaSubscriberIpAddressMask_Object = MibTableColumn
juniAaaSubscriberIpAddressMask = _JuniAaaSubscriberIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 7),
    _JuniAaaSubscriberIpAddressMask_Type()
)
juniAaaSubscriberIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberIpAddressMask.setStatus("current")
_JuniAaaSubscriberAddrAssignType_Type = JuniAddressAssignType
_JuniAaaSubscriberAddrAssignType_Object = MibTableColumn
juniAaaSubscriberAddrAssignType = _JuniAaaSubscriberAddrAssignType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 8),
    _JuniAaaSubscriberAddrAssignType_Type()
)
juniAaaSubscriberAddrAssignType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberAddrAssignType.setStatus("current")
_JuniAaaSubscriberInterfaceId_Type = DisplayString
_JuniAaaSubscriberInterfaceId_Object = MibTableColumn
juniAaaSubscriberInterfaceId = _JuniAaaSubscriberInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 9),
    _JuniAaaSubscriberInterfaceId_Type()
)
juniAaaSubscriberInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceId.setStatus("current")
_JuniAaaSubscriberState_Type = JuniSubscriberState
_JuniAaaSubscriberState_Object = MibTableColumn
juniAaaSubscriberState = _JuniAaaSubscriberState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 10),
    _JuniAaaSubscriberState_Type()
)
juniAaaSubscriberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberState.setStatus("current")
_JuniAaaSubscriberClientType_Type = JuniSubscriberClientType
_JuniAaaSubscriberClientType_Object = MibTableColumn
juniAaaSubscriberClientType = _JuniAaaSubscriberClientType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 11),
    _JuniAaaSubscriberClientType_Type()
)
juniAaaSubscriberClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberClientType.setStatus("current")
_JuniAaaSubscriberIngressPolicyName_Type = DisplayString
_JuniAaaSubscriberIngressPolicyName_Object = MibTableColumn
juniAaaSubscriberIngressPolicyName = _JuniAaaSubscriberIngressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 12),
    _JuniAaaSubscriberIngressPolicyName_Type()
)
juniAaaSubscriberIngressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberIngressPolicyName.setStatus("current")
_JuniAaaSubscriberEgressPolicyName_Type = DisplayString
_JuniAaaSubscriberEgressPolicyName_Object = MibTableColumn
juniAaaSubscriberEgressPolicyName = _JuniAaaSubscriberEgressPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 13),
    _JuniAaaSubscriberEgressPolicyName_Type()
)
juniAaaSubscriberEgressPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberEgressPolicyName.setStatus("current")
_JuniAaaSubscriberQosProfileName_Type = DisplayString
_JuniAaaSubscriberQosProfileName_Object = MibTableColumn
juniAaaSubscriberQosProfileName = _JuniAaaSubscriberQosProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 14),
    _JuniAaaSubscriberQosProfileName_Type()
)
juniAaaSubscriberQosProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberQosProfileName.setStatus("current")
_JuniAaaSubscriberRowStatus_Type = RowStatus
_JuniAaaSubscriberRowStatus_Object = MibTableColumn
juniAaaSubscriberRowStatus = _JuniAaaSubscriberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 15),
    _JuniAaaSubscriberRowStatus_Type()
)
juniAaaSubscriberRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniAaaSubscriberRowStatus.setStatus("current")
_JuniAaaSubscriberIpv6RouterIndex_Type = Unsigned32
_JuniAaaSubscriberIpv6RouterIndex_Object = MibTableColumn
juniAaaSubscriberIpv6RouterIndex = _JuniAaaSubscriberIpv6RouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 16),
    _JuniAaaSubscriberIpv6RouterIndex_Type()
)
juniAaaSubscriberIpv6RouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberIpv6RouterIndex.setStatus("current")
_JuniAaaSubscriberIpv6AddrIfIdentifier_Type = Ipv6AddressIfIdentifier
_JuniAaaSubscriberIpv6AddrIfIdentifier_Object = MibTableColumn
juniAaaSubscriberIpv6AddrIfIdentifier = _JuniAaaSubscriberIpv6AddrIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 4, 1, 17),
    _JuniAaaSubscriberIpv6AddrIfIdentifier_Type()
)
juniAaaSubscriberIpv6AddrIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberIpv6AddrIfIdentifier.setStatus("current")
_JuniAaaSubscriberRouterSummaryTable_Object = MibTable
juniAaaSubscriberRouterSummaryTable = _JuniAaaSubscriberRouterSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterSummaryTable.setStatus("current")
_JuniAaaSubscriberRouterSummaryEntry_Object = MibTableRow
juniAaaSubscriberRouterSummaryEntry = _JuniAaaSubscriberRouterSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5, 1)
)
juniAaaSubscriberRouterSummaryEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberRouterSummaryRouterIndex"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterSummaryEntry.setStatus("current")
_JuniAaaSubscriberRouterSummaryRouterIndex_Type = Unsigned32
_JuniAaaSubscriberRouterSummaryRouterIndex_Object = MibTableColumn
juniAaaSubscriberRouterSummaryRouterIndex = _JuniAaaSubscriberRouterSummaryRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5, 1, 1),
    _JuniAaaSubscriberRouterSummaryRouterIndex_Type()
)
juniAaaSubscriberRouterSummaryRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterSummaryRouterIndex.setStatus("current")
_JuniAaaSubscriberRouterSummaryCount_Type = Gauge32
_JuniAaaSubscriberRouterSummaryCount_Object = MibTableColumn
juniAaaSubscriberRouterSummaryCount = _JuniAaaSubscriberRouterSummaryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 5, 1, 2),
    _JuniAaaSubscriberRouterSummaryCount_Type()
)
juniAaaSubscriberRouterSummaryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterSummaryCount.setStatus("current")
_JuniAaaSubscriberRouterTable_Object = MibTable
juniAaaSubscriberRouterTable = _JuniAaaSubscriberRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterTable.setStatus("current")
_JuniAaaSubscriberRouterEntry_Object = MibTableRow
juniAaaSubscriberRouterEntry = _JuniAaaSubscriberRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1)
)
juniAaaSubscriberRouterEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberRouterRouterIndex"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberRouterHandle"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterEntry.setStatus("current")
_JuniAaaSubscriberRouterRouterIndex_Type = Unsigned32
_JuniAaaSubscriberRouterRouterIndex_Object = MibTableColumn
juniAaaSubscriberRouterRouterIndex = _JuniAaaSubscriberRouterRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1, 1),
    _JuniAaaSubscriberRouterRouterIndex_Type()
)
juniAaaSubscriberRouterRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterRouterIndex.setStatus("current")
_JuniAaaSubscriberRouterHandle_Type = Unsigned32
_JuniAaaSubscriberRouterHandle_Object = MibTableColumn
juniAaaSubscriberRouterHandle = _JuniAaaSubscriberRouterHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1, 2),
    _JuniAaaSubscriberRouterHandle_Type()
)
juniAaaSubscriberRouterHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterHandle.setStatus("current")
_JuniAaaSubscriberRouterRowStatus_Type = RowStatus
_JuniAaaSubscriberRouterRowStatus_Object = MibTableColumn
juniAaaSubscriberRouterRowStatus = _JuniAaaSubscriberRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 6, 1, 3),
    _JuniAaaSubscriberRouterRowStatus_Type()
)
juniAaaSubscriberRouterRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberRouterRowStatus.setStatus("current")
_JuniAaaSubscriberLocationType_Type = JuniInterfaceLocationType
_JuniAaaSubscriberLocationType_Object = MibScalar
juniAaaSubscriberLocationType = _JuniAaaSubscriberLocationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 7),
    _JuniAaaSubscriberLocationType_Type()
)
juniAaaSubscriberLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationType.setStatus("current")
_JuniAaaSubscriberLocationSummaryTable_Object = MibTable
juniAaaSubscriberLocationSummaryTable = _JuniAaaSubscriberLocationSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationSummaryTable.setStatus("current")
_JuniAaaSubscriberLocationSummaryEntry_Object = MibTableRow
juniAaaSubscriberLocationSummaryEntry = _JuniAaaSubscriberLocationSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8, 1)
)
juniAaaSubscriberLocationSummaryEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberLocationSummaryLocationIndex"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationSummaryEntry.setStatus("current")
_JuniAaaSubscriberLocationSummaryLocationIndex_Type = JuniInterfaceLocationValue
_JuniAaaSubscriberLocationSummaryLocationIndex_Object = MibTableColumn
juniAaaSubscriberLocationSummaryLocationIndex = _JuniAaaSubscriberLocationSummaryLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8, 1, 1),
    _JuniAaaSubscriberLocationSummaryLocationIndex_Type()
)
juniAaaSubscriberLocationSummaryLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationSummaryLocationIndex.setStatus("current")
_JuniAaaSubscriberLocationSummaryCount_Type = Gauge32
_JuniAaaSubscriberLocationSummaryCount_Object = MibTableColumn
juniAaaSubscriberLocationSummaryCount = _JuniAaaSubscriberLocationSummaryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 8, 1, 2),
    _JuniAaaSubscriberLocationSummaryCount_Type()
)
juniAaaSubscriberLocationSummaryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationSummaryCount.setStatus("current")
_JuniAaaSubscriberLocationTable_Object = MibTable
juniAaaSubscriberLocationTable = _JuniAaaSubscriberLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationTable.setStatus("current")
_JuniAaaSubscriberLocationEntry_Object = MibTableRow
juniAaaSubscriberLocationEntry = _JuniAaaSubscriberLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1)
)
juniAaaSubscriberLocationEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberLocationLocationIndex"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberLocationHandle"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationEntry.setStatus("current")
_JuniAaaSubscriberLocationLocationIndex_Type = JuniInterfaceLocationValue
_JuniAaaSubscriberLocationLocationIndex_Object = MibTableColumn
juniAaaSubscriberLocationLocationIndex = _JuniAaaSubscriberLocationLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1, 1),
    _JuniAaaSubscriberLocationLocationIndex_Type()
)
juniAaaSubscriberLocationLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationLocationIndex.setStatus("current")
_JuniAaaSubscriberLocationHandle_Type = Unsigned32
_JuniAaaSubscriberLocationHandle_Object = MibTableColumn
juniAaaSubscriberLocationHandle = _JuniAaaSubscriberLocationHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1, 2),
    _JuniAaaSubscriberLocationHandle_Type()
)
juniAaaSubscriberLocationHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationHandle.setStatus("current")
_JuniAaaSubscriberLocationRowStatus_Type = RowStatus
_JuniAaaSubscriberLocationRowStatus_Object = MibTableColumn
juniAaaSubscriberLocationRowStatus = _JuniAaaSubscriberLocationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 9, 1, 3),
    _JuniAaaSubscriberLocationRowStatus_Type()
)
juniAaaSubscriberLocationRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberLocationRowStatus.setStatus("current")
_JuniAaaSubscriberPseudoPeakCount_Type = Gauge32
_JuniAaaSubscriberPseudoPeakCount_Object = MibScalar
juniAaaSubscriberPseudoPeakCount = _JuniAaaSubscriberPseudoPeakCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 10),
    _JuniAaaSubscriberPseudoPeakCount_Type()
)
juniAaaSubscriberPseudoPeakCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberPseudoPeakCount.setStatus("current")
_JuniAaaSubscriberPseudoCount_Type = Gauge32
_JuniAaaSubscriberPseudoCount_Object = MibScalar
juniAaaSubscriberPseudoCount = _JuniAaaSubscriberPseudoCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 11),
    _JuniAaaSubscriberPseudoCount_Type()
)
juniAaaSubscriberPseudoCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberPseudoCount.setStatus("current")
_JuniAaaSubscriberIpv6AddrPrefixTable_Object = MibTable
juniAaaSubscriberIpv6AddrPrefixTable = _JuniAaaSubscriberIpv6AddrPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 12)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberIpv6AddrPrefixTable.setStatus("current")
_JuniAaaSubscriberIpv6AddrPrefixEntry_Object = MibTableRow
juniAaaSubscriberIpv6AddrPrefixEntry = _JuniAaaSubscriberIpv6AddrPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 12, 1)
)
juniAaaSubscriberIpv6AddrPrefixEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberHandle"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrPrefix"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrPrefixSize"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberIpv6AddrPrefixEntry.setStatus("current")
_JuniAaaSubscriberIpv6AddrPrefix_Type = Ipv6AddressPrefix
_JuniAaaSubscriberIpv6AddrPrefix_Object = MibTableColumn
juniAaaSubscriberIpv6AddrPrefix = _JuniAaaSubscriberIpv6AddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 12, 1, 1),
    _JuniAaaSubscriberIpv6AddrPrefix_Type()
)
juniAaaSubscriberIpv6AddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberIpv6AddrPrefix.setStatus("current")


class _JuniAaaSubscriberIpv6AddrPrefixSize_Type(Integer32):
    """Custom type juniAaaSubscriberIpv6AddrPrefixSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_JuniAaaSubscriberIpv6AddrPrefixSize_Type.__name__ = "Integer32"
_JuniAaaSubscriberIpv6AddrPrefixSize_Object = MibTableColumn
juniAaaSubscriberIpv6AddrPrefixSize = _JuniAaaSubscriberIpv6AddrPrefixSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 12, 1, 2),
    _JuniAaaSubscriberIpv6AddrPrefixSize_Type()
)
juniAaaSubscriberIpv6AddrPrefixSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberIpv6AddrPrefixSize.setStatus("current")
_JuniAaaSubscriberExtTable_Object = MibTable
juniAaaSubscriberExtTable = _JuniAaaSubscriberExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberExtTable.setStatus("current")
_JuniAaaSubscriberExtEntry_Object = MibTableRow
juniAaaSubscriberExtEntry = _JuniAaaSubscriberExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1)
)
juniAaaSubscriberExtEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberHandle"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberExtEntry.setStatus("current")
_JuniAaaSubscriberExtUserName_Type = DisplayString
_JuniAaaSubscriberExtUserName_Object = MibTableColumn
juniAaaSubscriberExtUserName = _JuniAaaSubscriberExtUserName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 1),
    _JuniAaaSubscriberExtUserName_Type()
)
juniAaaSubscriberExtUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtUserName.setStatus("current")
_JuniAaaSubscriberExtLoginTime_Type = DisplayString
_JuniAaaSubscriberExtLoginTime_Object = MibTableColumn
juniAaaSubscriberExtLoginTime = _JuniAaaSubscriberExtLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 2),
    _JuniAaaSubscriberExtLoginTime_Type()
)
juniAaaSubscriberExtLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtLoginTime.setStatus("current")
_JuniAaaSubscriberExtIpAddress_Type = IpAddress
_JuniAaaSubscriberExtIpAddress_Object = MibTableColumn
juniAaaSubscriberExtIpAddress = _JuniAaaSubscriberExtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 3),
    _JuniAaaSubscriberExtIpAddress_Type()
)
juniAaaSubscriberExtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtIpAddress.setStatus("current")
_JuniAaaSubscriberExtIpAddressMask_Type = IpAddress
_JuniAaaSubscriberExtIpAddressMask_Object = MibTableColumn
juniAaaSubscriberExtIpAddressMask = _JuniAaaSubscriberExtIpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 4),
    _JuniAaaSubscriberExtIpAddressMask_Type()
)
juniAaaSubscriberExtIpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtIpAddressMask.setStatus("current")
_JuniAaaSubscriberExtAddrAssignType_Type = JuniAddressAssignType
_JuniAaaSubscriberExtAddrAssignType_Object = MibTableColumn
juniAaaSubscriberExtAddrAssignType = _JuniAaaSubscriberExtAddrAssignType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 5),
    _JuniAaaSubscriberExtAddrAssignType_Type()
)
juniAaaSubscriberExtAddrAssignType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtAddrAssignType.setStatus("current")
_JuniAaaSubscriberExtState_Type = JuniSubscriberState
_JuniAaaSubscriberExtState_Object = MibTableColumn
juniAaaSubscriberExtState = _JuniAaaSubscriberExtState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 6),
    _JuniAaaSubscriberExtState_Type()
)
juniAaaSubscriberExtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtState.setStatus("current")
_JuniAaaSubscriberExtClientType_Type = JuniSubscriberClientType
_JuniAaaSubscriberExtClientType_Object = MibTableColumn
juniAaaSubscriberExtClientType = _JuniAaaSubscriberExtClientType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 7),
    _JuniAaaSubscriberExtClientType_Type()
)
juniAaaSubscriberExtClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtClientType.setStatus("current")
_JuniAaaSubscriberExtAcctSessionId_Type = DisplayString
_JuniAaaSubscriberExtAcctSessionId_Object = MibTableColumn
juniAaaSubscriberExtAcctSessionId = _JuniAaaSubscriberExtAcctSessionId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 8),
    _JuniAaaSubscriberExtAcctSessionId_Type()
)
juniAaaSubscriberExtAcctSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtAcctSessionId.setStatus("current")
_JuniAaaSubscriberExtClass_Type = DisplayString
_JuniAaaSubscriberExtClass_Object = MibTableColumn
juniAaaSubscriberExtClass = _JuniAaaSubscriberExtClass_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 9),
    _JuniAaaSubscriberExtClass_Type()
)
juniAaaSubscriberExtClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtClass.setStatus("current")
_JuniAaaSubscriberExtNasPort_Type = Unsigned32
_JuniAaaSubscriberExtNasPort_Object = MibTableColumn
juniAaaSubscriberExtNasPort = _JuniAaaSubscriberExtNasPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 10),
    _JuniAaaSubscriberExtNasPort_Type()
)
juniAaaSubscriberExtNasPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtNasPort.setStatus("current")
_JuniAaaSubscriberExtNasPortType_Type = Unsigned32
_JuniAaaSubscriberExtNasPortType_Object = MibTableColumn
juniAaaSubscriberExtNasPortType = _JuniAaaSubscriberExtNasPortType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 11),
    _JuniAaaSubscriberExtNasPortType_Type()
)
juniAaaSubscriberExtNasPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtNasPortType.setStatus("current")


class _JuniAaaSubscriberExtCalledStationId_Type(OctetString):
    """Custom type juniAaaSubscriberExtCalledStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniAaaSubscriberExtCalledStationId_Type.__name__ = "OctetString"
_JuniAaaSubscriberExtCalledStationId_Object = MibTableColumn
juniAaaSubscriberExtCalledStationId = _JuniAaaSubscriberExtCalledStationId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 12),
    _JuniAaaSubscriberExtCalledStationId_Type()
)
juniAaaSubscriberExtCalledStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtCalledStationId.setStatus("current")


class _JuniAaaSubscriberExtCallingStationId_Type(OctetString):
    """Custom type juniAaaSubscriberExtCallingStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniAaaSubscriberExtCallingStationId_Type.__name__ = "OctetString"
_JuniAaaSubscriberExtCallingStationId_Object = MibTableColumn
juniAaaSubscriberExtCallingStationId = _JuniAaaSubscriberExtCallingStationId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 13),
    _JuniAaaSubscriberExtCallingStationId_Type()
)
juniAaaSubscriberExtCallingStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtCallingStationId.setStatus("current")


class _JuniAaaSubscriberExtL2tpTunnelId_Type(Integer32):
    """Custom type juniAaaSubscriberExtL2tpTunnelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniAaaSubscriberExtL2tpTunnelId_Type.__name__ = "Integer32"
_JuniAaaSubscriberExtL2tpTunnelId_Object = MibTableColumn
juniAaaSubscriberExtL2tpTunnelId = _JuniAaaSubscriberExtL2tpTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 13, 1, 14),
    _JuniAaaSubscriberExtL2tpTunnelId_Type()
)
juniAaaSubscriberExtL2tpTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberExtL2tpTunnelId.setStatus("current")
_JuniAaaSubscriberInterfaceSummaryTable_Object = MibTable
juniAaaSubscriberInterfaceSummaryTable = _JuniAaaSubscriberInterfaceSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 14)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceSummaryTable.setStatus("current")
_JuniAaaSubscriberInterfaceSummaryEntry_Object = MibTableRow
juniAaaSubscriberInterfaceSummaryEntry = _JuniAaaSubscriberInterfaceSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 14, 1)
)
juniAaaSubscriberInterfaceSummaryEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberInterfaceSummaryIndex"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberSubInterfaceSummaryIndex"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceSummaryEntry.setStatus("current")
_JuniAaaSubscriberInterfaceSummaryIndex_Type = JuniSubscriberInterfaceValue
_JuniAaaSubscriberInterfaceSummaryIndex_Object = MibTableColumn
juniAaaSubscriberInterfaceSummaryIndex = _JuniAaaSubscriberInterfaceSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 14, 1, 1),
    _JuniAaaSubscriberInterfaceSummaryIndex_Type()
)
juniAaaSubscriberInterfaceSummaryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceSummaryIndex.setStatus("current")
_JuniAaaSubscriberSubInterfaceSummaryIndex_Type = Integer32
_JuniAaaSubscriberSubInterfaceSummaryIndex_Object = MibTableColumn
juniAaaSubscriberSubInterfaceSummaryIndex = _JuniAaaSubscriberSubInterfaceSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 14, 1, 2),
    _JuniAaaSubscriberSubInterfaceSummaryIndex_Type()
)
juniAaaSubscriberSubInterfaceSummaryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberSubInterfaceSummaryIndex.setStatus("current")
_JuniAaaSubscriberInterfaceSummaryCount_Type = Gauge32
_JuniAaaSubscriberInterfaceSummaryCount_Object = MibTableColumn
juniAaaSubscriberInterfaceSummaryCount = _JuniAaaSubscriberInterfaceSummaryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 14, 1, 3),
    _JuniAaaSubscriberInterfaceSummaryCount_Type()
)
juniAaaSubscriberInterfaceSummaryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceSummaryCount.setStatus("current")
_JuniAaaSubscriberInterfaceTable_Object = MibTable
juniAaaSubscriberInterfaceTable = _JuniAaaSubscriberInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 15)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceTable.setStatus("current")
_JuniAaaSubscriberInterfaceEntry_Object = MibTableRow
juniAaaSubscriberInterfaceEntry = _JuniAaaSubscriberInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 15, 1)
)
juniAaaSubscriberInterfaceEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberInterfaceIndex"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberSubInterfaceIndex"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberInterfaceHandle"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceEntry.setStatus("current")
_JuniAaaSubscriberInterfaceIndex_Type = JuniSubscriberInterfaceValue
_JuniAaaSubscriberInterfaceIndex_Object = MibTableColumn
juniAaaSubscriberInterfaceIndex = _JuniAaaSubscriberInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 15, 1, 1),
    _JuniAaaSubscriberInterfaceIndex_Type()
)
juniAaaSubscriberInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceIndex.setStatus("current")
_JuniAaaSubscriberSubInterfaceIndex_Type = Integer32
_JuniAaaSubscriberSubInterfaceIndex_Object = MibTableColumn
juniAaaSubscriberSubInterfaceIndex = _JuniAaaSubscriberSubInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 15, 1, 2),
    _JuniAaaSubscriberSubInterfaceIndex_Type()
)
juniAaaSubscriberSubInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberSubInterfaceIndex.setStatus("current")
_JuniAaaSubscriberInterfaceHandle_Type = Unsigned32
_JuniAaaSubscriberInterfaceHandle_Object = MibTableColumn
juniAaaSubscriberInterfaceHandle = _JuniAaaSubscriberInterfaceHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 15, 1, 3),
    _JuniAaaSubscriberInterfaceHandle_Type()
)
juniAaaSubscriberInterfaceHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceHandle.setStatus("current")
_JuniAaaSubscriberInterfaceRowStatus_Type = RowStatus
_JuniAaaSubscriberInterfaceRowStatus_Object = MibTableColumn
juniAaaSubscriberInterfaceRowStatus = _JuniAaaSubscriberInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 15, 1, 4),
    _JuniAaaSubscriberInterfaceRowStatus_Type()
)
juniAaaSubscriberInterfaceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberInterfaceRowStatus.setStatus("current")
_JuniAaaSubscriberSlotSummaryTable_Object = MibTable
juniAaaSubscriberSlotSummaryTable = _JuniAaaSubscriberSlotSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 16)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotSummaryTable.setStatus("current")
_JuniAaaSubscriberSlotSummaryEntry_Object = MibTableRow
juniAaaSubscriberSlotSummaryEntry = _JuniAaaSubscriberSlotSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 16, 1)
)
juniAaaSubscriberSlotSummaryEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberSlotSummarySlotIndex"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotSummaryEntry.setStatus("current")
_JuniAaaSubscriberSlotSummarySlotIndex_Type = Unsigned32
_JuniAaaSubscriberSlotSummarySlotIndex_Object = MibTableColumn
juniAaaSubscriberSlotSummarySlotIndex = _JuniAaaSubscriberSlotSummarySlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 16, 1, 1),
    _JuniAaaSubscriberSlotSummarySlotIndex_Type()
)
juniAaaSubscriberSlotSummarySlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotSummarySlotIndex.setStatus("current")
_JuniAaaSubscriberSlotSummaryCount_Type = Gauge32
_JuniAaaSubscriberSlotSummaryCount_Object = MibTableColumn
juniAaaSubscriberSlotSummaryCount = _JuniAaaSubscriberSlotSummaryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 16, 1, 2),
    _JuniAaaSubscriberSlotSummaryCount_Type()
)
juniAaaSubscriberSlotSummaryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotSummaryCount.setStatus("current")
_JuniAaaSubscriberSlotTable_Object = MibTable
juniAaaSubscriberSlotTable = _JuniAaaSubscriberSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 17)
)
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotTable.setStatus("current")
_JuniAaaSubscriberSlotEntry_Object = MibTableRow
juniAaaSubscriberSlotEntry = _JuniAaaSubscriberSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 17, 1)
)
juniAaaSubscriberSlotEntry.setIndexNames(
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberSlotIndex"),
    (0, "Juniper-AAA-MIB", "juniAaaSubscriberSlotHandle"),
)
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotEntry.setStatus("current")
_JuniAaaSubscriberSlotIndex_Type = Unsigned32
_JuniAaaSubscriberSlotIndex_Object = MibTableColumn
juniAaaSubscriberSlotIndex = _JuniAaaSubscriberSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 17, 1, 1),
    _JuniAaaSubscriberSlotIndex_Type()
)
juniAaaSubscriberSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotIndex.setStatus("current")
_JuniAaaSubscriberSlotHandle_Type = Unsigned32
_JuniAaaSubscriberSlotHandle_Object = MibTableColumn
juniAaaSubscriberSlotHandle = _JuniAaaSubscriberSlotHandle_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 17, 1, 2),
    _JuniAaaSubscriberSlotHandle_Type()
)
juniAaaSubscriberSlotHandle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotHandle.setStatus("current")
_JuniAaaSubscriberSlotRowStatus_Type = RowStatus
_JuniAaaSubscriberSlotRowStatus_Object = MibTableColumn
juniAaaSubscriberSlotRowStatus = _JuniAaaSubscriberSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 8, 17, 1, 3),
    _JuniAaaSubscriberSlotRowStatus_Type()
)
juniAaaSubscriberSlotRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaSubscriberSlotRowStatus.setStatus("current")
_JuniAaaCapabilities_ObjectIdentity = ObjectIdentity
juniAaaCapabilities = _JuniAaaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9)
)
_JuniAaaAccountingCapability_Type = TruthValue
_JuniAaaAccountingCapability_Object = MibScalar
juniAaaAccountingCapability = _JuniAaaAccountingCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 1),
    _JuniAaaAccountingCapability_Type()
)
juniAaaAccountingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAccountingCapability.setStatus("current")
_JuniAaaAddressAssignmentCapability_Type = TruthValue
_JuniAaaAddressAssignmentCapability_Object = MibScalar
juniAaaAddressAssignmentCapability = _JuniAaaAddressAssignmentCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 2),
    _JuniAaaAddressAssignmentCapability_Type()
)
juniAaaAddressAssignmentCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaAddressAssignmentCapability.setStatus("current")
_JuniAaaBrasCapability_Type = TruthValue
_JuniAaaBrasCapability_Object = MibScalar
juniAaaBrasCapability = _JuniAaaBrasCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 3),
    _JuniAaaBrasCapability_Type()
)
juniAaaBrasCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaBrasCapability.setStatus("current")
_JuniAaaTunnelingCapability_Type = TruthValue
_JuniAaaTunnelingCapability_Object = MibScalar
juniAaaTunnelingCapability = _JuniAaaTunnelingCapability_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 1, 9, 4),
    _JuniAaaTunnelingCapability_Type()
)
juniAaaTunnelingCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniAaaTunnelingCapability.setStatus("current")
_JuniAaaMIBConformance_ObjectIdentity = ObjectIdentity
juniAaaMIBConformance = _JuniAaaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4)
)
_JuniAaaMIBCompliances_ObjectIdentity = ObjectIdentity
juniAaaMIBCompliances = _JuniAaaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1)
)
_JuniAaaMIBGroups_ObjectIdentity = ObjectIdentity
juniAaaMIBGroups = _JuniAaaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2)
)

# Managed Objects groups

juniAaaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 1)
)
juniAaaGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLoopback"),
        ("Juniper-AAA-MIB", "juniAaaAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaAcctDupServerRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAddrPoolDefault"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsSecondary"))
)
if mibBuilder.loadTexts:
    juniAaaGroup.setStatus("obsolete")

juniAaaGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 2)
)
juniAaaGroup2.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLoopback"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaAcctDupServerRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAddrPoolDefault"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaIncomingInitiateRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingTerminateRequests"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingTunnelGrantResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingGrantResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDenyResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingErrorResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAuthResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingReAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingReAuthResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDupAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingDupAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAddrRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAddrResponses"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelRowStatus"))
)
if mibBuilder.loadTexts:
    juniAaaGroup2.setStatus("obsolete")

juniAaaBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 3)
)
juniAaaBasicGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaIncomingInitiateRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingTerminateRequests"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingGrantResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDenyResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingErrorResponses"))
)
if mibBuilder.loadTexts:
    juniAaaBasicGroup.setStatus("current")

juniAaaBrasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 4)
)
juniAaaBrasGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLoopback"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup.setStatus("obsolete")

juniAaaTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 5)
)
juniAaaTunnelGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelServerName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelClientAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingTunnelGrantResponses"))
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroup.setStatus("obsolete")

juniAaaAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 6)
)
juniAaaAuthenticationGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAuthMethods"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAuthResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingReAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingReAuthResponses"))
)
if mibBuilder.loadTexts:
    juniAaaAuthenticationGroup.setStatus("obsolete")

juniAaaAccountingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 7)
)
juniAaaAccountingGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaAcctDupServerRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethods"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDupAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingDupAcctResponses"))
)
if mibBuilder.loadTexts:
    juniAaaAccountingGroup.setStatus("obsolete")

juniAaaAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 8)
)
juniAaaAddressGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAddrPoolDefault"),
        ("Juniper-AAA-MIB", "juniAaaDupAddrCheck"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAddrRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAddrResponses"))
)
if mibBuilder.loadTexts:
    juniAaaAddressGroup.setStatus("obsolete")

juniAaaBrasGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 9)
)
juniAaaBrasGroup2.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLoopback"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup2.setStatus("obsolete")

juniAaaBrasGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 10)
)
juniAaaBrasGroup3.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLoopback"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup3.setStatus("obsolete")

juniAaaSubscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 11)
)
juniAaaSubscriberGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaSubscriberMaxCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberUserName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterIndex"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLoginTime"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddress"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddressMask"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberAddrAssignType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberInterfaceId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberState"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberClientType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIngressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberEgressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberQosProfileName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterRowStatus"))
)
if mibBuilder.loadTexts:
    juniAaaSubscriberGroup.setStatus("obsolete")

juniAaaCapabilitiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 12)
)
juniAaaCapabilitiesGroup.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAccountingCapability"),
        ("Juniper-AAA-MIB", "juniAaaAddressAssignmentCapability"),
        ("Juniper-AAA-MIB", "juniAaaBrasCapability"),
        ("Juniper-AAA-MIB", "juniAaaTunnelingCapability"))
)
if mibBuilder.loadTexts:
    juniAaaCapabilitiesGroup.setStatus("current")

juniAaaSubscriberGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 13)
)
juniAaaSubscriberGroup2.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaSubscriberMaxCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberUserName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterIndex"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLoginTime"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddress"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddressMask"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberAddrAssignType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberInterfaceId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberState"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberClientType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIngressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberEgressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberQosProfileName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationRowStatus"))
)
if mibBuilder.loadTexts:
    juniAaaSubscriberGroup2.setStatus("obsolete")

juniAaaAccountingGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 14)
)
juniAaaAccountingGroup2.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaAcctDupServerRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethods"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaDeny"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaReject"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDupAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingDupAcctResponses"))
)
if mibBuilder.loadTexts:
    juniAaaAccountingGroup2.setStatus("obsolete")

juniAaaBrasGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 15)
)
juniAaaBrasGroup4.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLoopback"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup4.setStatus("obsolete")

juniAaaSubscriberGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 16)
)
juniAaaSubscriberGroup3.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaSubscriberMaxCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberUserName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterIndex"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLoginTime"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddress"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddressMask"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberAddrAssignType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberInterfaceId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberState"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberClientType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIngressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberEgressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberQosProfileName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPseudoPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPseudoCount"))
)
if mibBuilder.loadTexts:
    juniAaaSubscriberGroup3.setStatus("obsolete")

juniAaaBrasGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 17)
)
juniAaaBrasGroup5.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLoopback"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup5.setStatus("obsolete")

juniAaaTunnelGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 18)
)
juniAaaTunnelGroup2.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelServerName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelClientAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMaxSessions"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingTunnelGrantResponses"))
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroup2.setStatus("obsolete")

juniAaaBrasGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 19)
)
juniAaaBrasGroup6.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup6.setStatus("obsolete")

juniAaaBrasGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 20)
)
juniAaaBrasGroup7.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup7.setStatus("obsolete")

juniAaaAddressGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 21)
)
juniAaaAddressGroup2.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAddrPoolDefault"),
        ("Juniper-AAA-MIB", "juniAaaDupAddrCheck"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrDnsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrWinsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaAddrIpv6DnsPrimary"),
        ("Juniper-AAA-MIB", "juniAaaAddrIpv6DnsSecondary"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAddrRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAddrResponses"))
)
if mibBuilder.loadTexts:
    juniAaaAddressGroup2.setStatus("current")

juniAaaSubscriberGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 22)
)
juniAaaSubscriberGroup4.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaSubscriberMaxCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberUserName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterIndex"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLoginTime"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddress"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddressMask"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberAddrAssignType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberInterfaceId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberState"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberClientType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIngressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberEgressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberQosProfileName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6RouterIndex"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrIfIdentifier"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrPrefix"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrPrefixSize"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPseudoPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPseudoCount"))
)
if mibBuilder.loadTexts:
    juniAaaSubscriberGroup4.setStatus("obsolete")

juniAaaBrasGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 23)
)
juniAaaBrasGroup8.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup8.setStatus("obsolete")

juniAaaBrasGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 24)
)
juniAaaBrasGroup9.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup9.setStatus("obsolete")

juniAaaTunnelGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 25)
)
juniAaaTunnelGroup3.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelServerName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelClientAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMaxSessions"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelReceiveWindowSize"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingTunnelGrantResponses"))
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroup3.setStatus("obsolete")

juniAaaAccountingGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 26)
)
juniAaaAccountingGroup3.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaAcctDupServerRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaDeny"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaReject"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendImmediateAcctUpdate"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDupAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingDupAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethodsSubscriberType"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethodsAccounting"))
)
if mibBuilder.loadTexts:
    juniAaaAccountingGroup3.setStatus("obsolete")

juniAaaAuthenticationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 27)
)
juniAaaAuthenticationGroup2.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaOutgoingAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAuthResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingReAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingReAuthResponses"),
        ("Juniper-AAA-MIB", "juniAaaAuthMethodsSubscriberType"),
        ("Juniper-AAA-MIB", "juniAaaAuthMethodsAuthentication"))
)
if mibBuilder.loadTexts:
    juniAaaAuthenticationGroup2.setStatus("obsolete")

juniAaaAuthenticationGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 28)
)
juniAaaAuthenticationGroup3.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaOutgoingAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAuthResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingReAuthRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingReAuthResponses"),
        ("Juniper-AAA-MIB", "juniAaaAuthMethodsSubscriberType"),
        ("Juniper-AAA-MIB", "juniAaaAuthMethodsAuthentication"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserPassword"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserEncryption"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserIpAddress"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserIpAddressPool"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserRouterName"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserDbRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserDbAssocRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaLocalAuthUserDbAssocDbName"))
)
if mibBuilder.loadTexts:
    juniAaaAuthenticationGroup3.setStatus("current")

juniAaaAccountingGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 29)
)
juniAaaAccountingGroup4.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaAcctDupServerRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupName"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter1"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter2"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter3"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter4"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaDeny"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaReject"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendImmediateAcctUpdate"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDupAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingDupAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethodsSubscriberType"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethodsAccounting"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingBcastAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingBcastAcctResponses"))
)
if mibBuilder.loadTexts:
    juniAaaAccountingGroup4.setStatus("obsolete")

juniAaaTunnelGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 30)
)
juniAaaTunnelGroup4.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelServerName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelClientAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMaxSessions"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelReceiveWindowSize"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelSwitchProfile"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelGroup"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelServerName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelClientAddress"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelMaxSessions"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelReceiveWindowSize"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelRouterName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelSwitchProfile"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingTunnelGrantResponses"))
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroup4.setStatus("obsolete")

juniAaaSubscriberGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 31)
)
juniAaaSubscriberGroup5.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaSubscriberMaxCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberUserName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterIndex"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLoginTime"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddress"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpAddressMask"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberAddrAssignType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberInterfaceId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberState"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberClientType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIngressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberEgressPolicyName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberQosProfileName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6RouterIndex"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrIfIdentifier"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrPrefix"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberIpv6AddrPrefixSize"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberRouterRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationSummaryCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberLocationRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPseudoPeakCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberPseudoCount"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtUserName"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtLoginTime"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtIpAddress"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtIpAddressMask"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtAddrAssignType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtState"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtClientType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtAcctSessionId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtClass"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtNasPort"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtCalledStationId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtCallingStationId"),
        ("Juniper-AAA-MIB", "juniAaaSubscriberExtL2tpTunnelId"))
)
if mibBuilder.loadTexts:
    juniAaaSubscriberGroup5.setStatus("current")

juniAaaBrasGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 32)
)
juniAaaBrasGroup10.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAuthRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignAccountingStatisticsType"),
        ("Juniper-AAA-MIB", "juniAaaAssignQosDownstreamRate"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup10.setStatus("obsolete")

juniAaaTunnelGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 33)
)
juniAaaTunnelGroup5.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelServerName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelClientAddress"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelMaxSessions"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelReceiveWindowSize"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelFailoverResync"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelSwitchProfile"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelTxConnectSpeedMethod"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelGroup"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelTag"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelPreference"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelMedium"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelAddress"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelId"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelHostName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelServerName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelClientAddress"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelMaxSessions"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelReceiveWindowSize"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelRouterName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelFailoverResync"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelSwitchProfile"),
        ("Juniper-AAA-MIB", "juniAaaTunnelGroupTunnelTxConnectSpeedMethod"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingTunnelGrantResponses"))
)
if mibBuilder.loadTexts:
    juniAaaTunnelGroup5.setStatus("current")

juniAaaBrasGroup11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 34)
)
juniAaaBrasGroup11.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAuthRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignAccountingStatisticsType"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormatFallback"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup11.setStatus("obsolete")

juniAaaAccountingGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 35)
)
juniAaaAccountingGroup5.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaAcctDupServerRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupName"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter1"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter2"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter3"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRouter4"),
        ("Juniper-AAA-MIB", "juniAaaAcctBcastServerGroupRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaDeny"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendStopOnAaaReject"),
        ("Juniper-AAA-MIB", "juniAaaAcctSendImmediateAcctUpdate"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingDupAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingDupAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethodsSubscriberType"),
        ("Juniper-AAA-MIB", "juniAaaAcctMethodsAccounting"),
        ("Juniper-AAA-MIB", "juniAaaOutgoingBcastAcctRequests"),
        ("Juniper-AAA-MIB", "juniAaaIncomingBcastAcctResponses"),
        ("Juniper-AAA-MIB", "juniAaaUserAcctInterval"),
        ("Juniper-AAA-MIB", "juniAaaServiceAcctInterval"))
)
if mibBuilder.loadTexts:
    juniAaaAccountingGroup5.setStatus("current")

juniAaaBrasGroup12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 36)
)
juniAaaBrasGroup12.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAuthRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelSubscriberAuthentication"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignAccountingStatisticsType"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormatFallback"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup12.setStatus("obsolete")

juniAaaBrasGroup13 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 37)
)
juniAaaBrasGroup13.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaMonitorIngressTrafficOnly"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAuthRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelSubscriberAuthentication"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignAccountingStatisticsType"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormatFallback"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup13.setStatus("obsolete")

juniAaaBrasGroup14 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 38)
)
juniAaaBrasGroup14.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaMonitorIngressTrafficOnly"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAuthRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelSubscriberAuthentication"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainBackupPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignAccountingStatisticsType"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormatFallback"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup14.setStatus("obsolete")

juniAaaBrasGroup15 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 2, 39)
)
juniAaaBrasGroup15.setObjects(
      *(("Juniper-AAA-MIB", "juniAaaAssignBrasLicense"),
        ("Juniper-AAA-MIB", "juniAaaAssignBrasLicensedUsers"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmDelimiters"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseOrder"),
        ("Juniper-AAA-MIB", "juniAaaAssignSubscriberLimit"),
        ("Juniper-AAA-MIB", "juniAaaIdleTimeout"),
        ("Juniper-AAA-MIB", "juniAaaSessionTimeout"),
        ("Juniper-AAA-MIB", "juniAaaMonitorIngressTrafficOnly"),
        ("Juniper-AAA-MIB", "juniAaaTunnelClientName"),
        ("Juniper-AAA-MIB", "juniAaaTunnelPassword"),
        ("Juniper-AAA-MIB", "juniAaaTunnelNasPortMethod"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPort"),
        ("Juniper-AAA-MIB", "juniAaaTunnelIgnoreNasPortType"),
        ("Juniper-AAA-MIB", "juniAaaTunnelAssignmentIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpHint"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmServiceLevel"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmPcr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmScr"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAtmMbs"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverrideUserName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainOverridePassword"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainStripDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainLocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6RouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpv6LocalInterface"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainAuthRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainIpRouterName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainTunnelSubscriberAuthentication"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainBackupPoolName"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainMaxPadnPerDomain"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnRowStatus"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainPadnDistance"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceIdFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignDomainParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaAssignRealmParseDirection"),
        ("Juniper-AAA-MIB", "juniAaaInterfaceAdapterFormat"),
        ("Juniper-AAA-MIB", "juniAaaAssignAccountingStatisticsType"),
        ("Juniper-AAA-MIB", "juniAaaAssignTunnelCallingNumberFormatFallback"),
        ("Juniper-AAA-MIB", "juniAaaFramedIpv6PrefixAsIpv6NdRaPrefix"),
        ("Juniper-AAA-MIB", "juniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix"))
)
if mibBuilder.loadTexts:
    juniAaaBrasGroup15.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniAaaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniAaaCompliance.setStatus(
        "obsolete"
    )

juniAaaCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniAaaCompliance2.setStatus(
        "obsolete"
    )

juniAaaCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniAaaCompliance3.setStatus(
        "obsolete"
    )

juniAaaCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniAaaCompliance4.setStatus(
        "obsolete"
    )

juniAaaCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniAaaCompliance5.setStatus(
        "obsolete"
    )

juniAaaCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniAaaCompliance6.setStatus(
        "obsolete"
    )

juniAaaCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniAaaCompliance7.setStatus(
        "obsolete"
    )

juniAaaCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniAaaCompliance8.setStatus(
        "obsolete"
    )

juniAaaCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 9)
)
if mibBuilder.loadTexts:
    juniAaaCompliance9.setStatus(
        "obsolete"
    )

juniAaaCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 10)
)
if mibBuilder.loadTexts:
    juniAaaCompliance10.setStatus(
        "obsolete"
    )

juniAaaCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 11)
)
if mibBuilder.loadTexts:
    juniAaaCompliance11.setStatus(
        "obsolete"
    )

juniAaaCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 12)
)
if mibBuilder.loadTexts:
    juniAaaCompliance12.setStatus(
        "obsolete"
    )

juniAaaCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 13)
)
if mibBuilder.loadTexts:
    juniAaaCompliance13.setStatus(
        "obsolete"
    )

juniAaaCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 14)
)
if mibBuilder.loadTexts:
    juniAaaCompliance14.setStatus(
        "obsolete"
    )

juniAaaCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 15)
)
if mibBuilder.loadTexts:
    juniAaaCompliance15.setStatus(
        "obsolete"
    )

juniAaaCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 16)
)
if mibBuilder.loadTexts:
    juniAaaCompliance16.setStatus(
        "obsolete"
    )

juniAaaCompliance17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 17)
)
if mibBuilder.loadTexts:
    juniAaaCompliance17.setStatus(
        "obsolete"
    )

juniAaaCompliance18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 18)
)
if mibBuilder.loadTexts:
    juniAaaCompliance18.setStatus(
        "obsolete"
    )

juniAaaCompliance19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 19)
)
if mibBuilder.loadTexts:
    juniAaaCompliance19.setStatus(
        "obsolete"
    )

juniAaaCompliance20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 20)
)
if mibBuilder.loadTexts:
    juniAaaCompliance20.setStatus(
        "obsolete"
    )

juniAaaCompliance21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 21)
)
if mibBuilder.loadTexts:
    juniAaaCompliance21.setStatus(
        "obsolete"
    )

juniAaaCompliance22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 22)
)
if mibBuilder.loadTexts:
    juniAaaCompliance22.setStatus(
        "obsolete"
    )

juniAaaCompliance23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 23)
)
if mibBuilder.loadTexts:
    juniAaaCompliance23.setStatus(
        "obsolete"
    )

juniAaaCompliance24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 20, 4, 1, 24)
)
if mibBuilder.loadTexts:
    juniAaaCompliance24.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-AAA-MIB",
    **{"JuniAaaDomainName": JuniAaaDomainName,
       "JuniAaaTunnelGroupName": JuniAaaTunnelGroupName,
       "JuniAaaTunnelSwitchProfileName": JuniAaaTunnelSwitchProfileName,
       "JuniAaaAuthenticationMethods": JuniAaaAuthenticationMethods,
       "JuniAaaAccountingMethods": JuniAaaAccountingMethods,
       "JuniAddressAssignType": JuniAddressAssignType,
       "JuniSubscriberState": JuniSubscriberState,
       "JuniSubscriberClientType": JuniSubscriberClientType,
       "JuniSubscriberLocationType": JuniSubscriberLocationType,
       "JuniSubscriberLocationValue": JuniSubscriberLocationValue,
       "JuniSubscriberInterfaceValue": JuniSubscriberInterfaceValue,
       "JuniAaaAuthenticationSubscriberTypes": JuniAaaAuthenticationSubscriberTypes,
       "JuniAaaAccountingSubscriberTypes": JuniAaaAccountingSubscriberTypes,
       "juniAaaMIB": juniAaaMIB,
       "juniAaaObjects": juniAaaObjects,
       "juniAaaAssignment": juniAaaAssignment,
       "juniAaaAssignGeneral": juniAaaAssignGeneral,
       "juniAaaAssignBrasLicense": juniAaaAssignBrasLicense,
       "juniAaaAssignBrasLicensedUsers": juniAaaAssignBrasLicensedUsers,
       "juniAaaAssignDomainDelimiters": juniAaaAssignDomainDelimiters,
       "juniAaaAssignRealmDelimiters": juniAaaAssignRealmDelimiters,
       "juniAaaAssignDomainParseOrder": juniAaaAssignDomainParseOrder,
       "juniAaaAssignSubscriberLimit": juniAaaAssignSubscriberLimit,
       "juniAaaAssignDomainMaxPadnPerDomain": juniAaaAssignDomainMaxPadnPerDomain,
       "juniAaaInterfaceIdFormat": juniAaaInterfaceIdFormat,
       "juniAaaAssignTunnelCallingNumberFormat": juniAaaAssignTunnelCallingNumberFormat,
       "juniAaaAssignDomainParseDirection": juniAaaAssignDomainParseDirection,
       "juniAaaAssignRealmParseDirection": juniAaaAssignRealmParseDirection,
       "juniAaaInterfaceAdapterFormat": juniAaaInterfaceAdapterFormat,
       "juniAaaAssignAccountingStatisticsType": juniAaaAssignAccountingStatisticsType,
       "juniAaaAssignQosDownstreamRate": juniAaaAssignQosDownstreamRate,
       "juniAaaAssignTunnelCallingNumberFormatFallback": juniAaaAssignTunnelCallingNumberFormatFallback,
       "juniAaaFramedIpv6PrefixAsIpv6NdRaPrefix": juniAaaFramedIpv6PrefixAsIpv6NdRaPrefix,
       "juniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix": juniAaaDelegatedIpv6PrefixAsDhcpv6DelegatedPrefix,
       "juniAaaAssignDomain": juniAaaAssignDomain,
       "juniAaaAssignDomainTable": juniAaaAssignDomainTable,
       "juniAaaAssignDomainEntry": juniAaaAssignDomainEntry,
       "juniAaaAssignDomainName": juniAaaAssignDomainName,
       "juniAaaAssignDomainRowStatus": juniAaaAssignDomainRowStatus,
       "juniAaaAssignDomainRouterName": juniAaaAssignDomainRouterName,
       "juniAaaAssignDomainLoopback": juniAaaAssignDomainLoopback,
       "juniAaaAssignDomainIpHint": juniAaaAssignDomainIpHint,
       "juniAaaAssignDomainAtmServiceLevel": juniAaaAssignDomainAtmServiceLevel,
       "juniAaaAssignDomainAtmPcr": juniAaaAssignDomainAtmPcr,
       "juniAaaAssignDomainAtmScr": juniAaaAssignDomainAtmScr,
       "juniAaaAssignDomainAtmMbs": juniAaaAssignDomainAtmMbs,
       "juniAaaAssignDomainOverrideUserName": juniAaaAssignDomainOverrideUserName,
       "juniAaaAssignDomainOverridePassword": juniAaaAssignDomainOverridePassword,
       "juniAaaAssignDomainStripDomain": juniAaaAssignDomainStripDomain,
       "juniAaaAssignDomainPoolName": juniAaaAssignDomainPoolName,
       "juniAaaAssignDomainLocalInterface": juniAaaAssignDomainLocalInterface,
       "juniAaaAssignDomainIpv6RouterName": juniAaaAssignDomainIpv6RouterName,
       "juniAaaAssignDomainIpv6LocalInterface": juniAaaAssignDomainIpv6LocalInterface,
       "juniAaaAssignDomainTunnelGroup": juniAaaAssignDomainTunnelGroup,
       "juniAaaAssignDomainAuthRouterName": juniAaaAssignDomainAuthRouterName,
       "juniAaaAssignDomainIpRouterName": juniAaaAssignDomainIpRouterName,
       "juniAaaAssignDomainTunnelSubscriberAuthentication": juniAaaAssignDomainTunnelSubscriberAuthentication,
       "juniAaaAssignDomainBackupPoolName": juniAaaAssignDomainBackupPoolName,
       "juniAaaAssignDomainTunnelTable": juniAaaAssignDomainTunnelTable,
       "juniAaaAssignDomainTunnelEntry": juniAaaAssignDomainTunnelEntry,
       "juniAaaAssignDomainTunnelName": juniAaaAssignDomainTunnelName,
       "juniAaaAssignDomainTunnelTag": juniAaaAssignDomainTunnelTag,
       "juniAaaAssignDomainTunnelPreference": juniAaaAssignDomainTunnelPreference,
       "juniAaaAssignDomainTunnelType": juniAaaAssignDomainTunnelType,
       "juniAaaAssignDomainTunnelMedium": juniAaaAssignDomainTunnelMedium,
       "juniAaaAssignDomainTunnelAddress": juniAaaAssignDomainTunnelAddress,
       "juniAaaAssignDomainTunnelPassword": juniAaaAssignDomainTunnelPassword,
       "juniAaaAssignDomainTunnelId": juniAaaAssignDomainTunnelId,
       "juniAaaAssignDomainTunnelHostName": juniAaaAssignDomainTunnelHostName,
       "juniAaaAssignDomainTunnelRowStatus": juniAaaAssignDomainTunnelRowStatus,
       "juniAaaAssignDomainTunnelServerName": juniAaaAssignDomainTunnelServerName,
       "juniAaaAssignDomainTunnelClientAddress": juniAaaAssignDomainTunnelClientAddress,
       "juniAaaAssignDomainTunnelMaxSessions": juniAaaAssignDomainTunnelMaxSessions,
       "juniAaaAssignDomainTunnelReceiveWindowSize": juniAaaAssignDomainTunnelReceiveWindowSize,
       "juniAaaAssignDomainTunnelFailoverResync": juniAaaAssignDomainTunnelFailoverResync,
       "juniAaaAssignDomainTunnelSwitchProfile": juniAaaAssignDomainTunnelSwitchProfile,
       "juniAaaAssignDomainTunnelTxConnectSpeedMethod": juniAaaAssignDomainTunnelTxConnectSpeedMethod,
       "juniAaaAssignDomainPadnTable": juniAaaAssignDomainPadnTable,
       "juniAaaAssignDomainPadnEntry": juniAaaAssignDomainPadnEntry,
       "juniAaaAssignDomainPadnIpAddress": juniAaaAssignDomainPadnIpAddress,
       "juniAaaAssignDomainPadnIpMask": juniAaaAssignDomainPadnIpMask,
       "juniAaaAssignDomainPadnRowStatus": juniAaaAssignDomainPadnRowStatus,
       "juniAaaAssignDomainPadnDistance": juniAaaAssignDomainPadnDistance,
       "juniAaaAuthentication": juniAaaAuthentication,
       "juniAaaAuthGeneral": juniAaaAuthGeneral,
       "juniAaaAuthMethods": juniAaaAuthMethods,
       "juniAaaAuthMethodsTable": juniAaaAuthMethodsTable,
       "juniAaaAuthMethodsEntry": juniAaaAuthMethodsEntry,
       "juniAaaAuthMethodsSubscriberType": juniAaaAuthMethodsSubscriberType,
       "juniAaaAuthMethodsAuthentication": juniAaaAuthMethodsAuthentication,
       "juniAaaLocalAuth": juniAaaLocalAuth,
       "juniAaaLocalAuthUser": juniAaaLocalAuthUser,
       "juniAaaLocalAuthUserTable": juniAaaLocalAuthUserTable,
       "juniAaaLocalAuthUserEntry": juniAaaLocalAuthUserEntry,
       "juniAaaLocalAuthUserName": juniAaaLocalAuthUserName,
       "juniAaaLocalAuthUserRowStatus": juniAaaLocalAuthUserRowStatus,
       "juniAaaLocalAuthUserPassword": juniAaaLocalAuthUserPassword,
       "juniAaaLocalAuthUserEncryption": juniAaaLocalAuthUserEncryption,
       "juniAaaLocalAuthUserIpAddress": juniAaaLocalAuthUserIpAddress,
       "juniAaaLocalAuthUserIpAddressPool": juniAaaLocalAuthUserIpAddressPool,
       "juniAaaLocalAuthUserRouterName": juniAaaLocalAuthUserRouterName,
       "juniAaaLocalAuthUserDb": juniAaaLocalAuthUserDb,
       "juniAaaLocalAuthUserDbTable": juniAaaLocalAuthUserDbTable,
       "juniAaaLocalAuthUserDbEntry": juniAaaLocalAuthUserDbEntry,
       "juniAaaLocalAuthUserDbName": juniAaaLocalAuthUserDbName,
       "juniAaaLocalAuthUserDbRowStatus": juniAaaLocalAuthUserDbRowStatus,
       "juniAaaLocalAuthUserDbAssoc": juniAaaLocalAuthUserDbAssoc,
       "juniAaaLocalAuthUserDbAssocTable": juniAaaLocalAuthUserDbAssocTable,
       "juniAaaLocalAuthUserDbAssocEntry": juniAaaLocalAuthUserDbAssocEntry,
       "juniAaaLocalAuthUserDbAssocRowStatus": juniAaaLocalAuthUserDbAssocRowStatus,
       "juniAaaLocalAuthUserDbAssocDbName": juniAaaLocalAuthUserDbAssocDbName,
       "juniAaaAccounting": juniAaaAccounting,
       "juniAaaAcctGeneral": juniAaaAcctGeneral,
       "juniAaaAcctInterval": juniAaaAcctInterval,
       "juniAaaAcctDupServerRouterName": juniAaaAcctDupServerRouterName,
       "juniAaaAcctMethods": juniAaaAcctMethods,
       "juniAaaAcctSendStopOnAaaDeny": juniAaaAcctSendStopOnAaaDeny,
       "juniAaaAcctSendStopOnAaaReject": juniAaaAcctSendStopOnAaaReject,
       "juniAaaAcctSendImmediateAcctUpdate": juniAaaAcctSendImmediateAcctUpdate,
       "juniAaaAcctMethodsTable": juniAaaAcctMethodsTable,
       "juniAaaAcctMethodsEntry": juniAaaAcctMethodsEntry,
       "juniAaaAcctMethodsSubscriberType": juniAaaAcctMethodsSubscriberType,
       "juniAaaAcctMethodsAccounting": juniAaaAcctMethodsAccounting,
       "juniAaaAcctBcastServerGroupName": juniAaaAcctBcastServerGroupName,
       "juniAaaUserAcctInterval": juniAaaUserAcctInterval,
       "juniAaaServiceAcctInterval": juniAaaServiceAcctInterval,
       "juniAaaAcctBcastConfig": juniAaaAcctBcastConfig,
       "juniAaaAcctBcastServerGroupTable": juniAaaAcctBcastServerGroupTable,
       "juniAaaAcctBcastServerGroupEntry": juniAaaAcctBcastServerGroupEntry,
       "juniAaaAcctBcastServerGroup": juniAaaAcctBcastServerGroup,
       "juniAaaAcctBcastServerGroupRouter1": juniAaaAcctBcastServerGroupRouter1,
       "juniAaaAcctBcastServerGroupRouter2": juniAaaAcctBcastServerGroupRouter2,
       "juniAaaAcctBcastServerGroupRouter3": juniAaaAcctBcastServerGroupRouter3,
       "juniAaaAcctBcastServerGroupRouter4": juniAaaAcctBcastServerGroupRouter4,
       "juniAaaAcctBcastServerGroupRowStatus": juniAaaAcctBcastServerGroupRowStatus,
       "juniAaaAddress": juniAaaAddress,
       "juniAaaAddrGeneral": juniAaaAddrGeneral,
       "juniAaaAddrPoolDefault": juniAaaAddrPoolDefault,
       "juniAaaDupAddrCheck": juniAaaDupAddrCheck,
       "juniAaaAddrNameServer": juniAaaAddrNameServer,
       "juniAaaAddrDns": juniAaaAddrDns,
       "juniAaaAddrDnsPrimary": juniAaaAddrDnsPrimary,
       "juniAaaAddrDnsSecondary": juniAaaAddrDnsSecondary,
       "juniAaaAddrIpv6DnsPrimary": juniAaaAddrIpv6DnsPrimary,
       "juniAaaAddrIpv6DnsSecondary": juniAaaAddrIpv6DnsSecondary,
       "juniAaaAddrWins": juniAaaAddrWins,
       "juniAaaAddrWinsPrimary": juniAaaAddrWinsPrimary,
       "juniAaaAddrWinsSecondary": juniAaaAddrWinsSecondary,
       "juniAaaStatistics": juniAaaStatistics,
       "juniAaaIncomingInitiateRequests": juniAaaIncomingInitiateRequests,
       "juniAaaIncomingTerminateRequests": juniAaaIncomingTerminateRequests,
       "juniAaaOutgoingTunnelGrantResponses": juniAaaOutgoingTunnelGrantResponses,
       "juniAaaOutgoingGrantResponses": juniAaaOutgoingGrantResponses,
       "juniAaaOutgoingDenyResponses": juniAaaOutgoingDenyResponses,
       "juniAaaOutgoingErrorResponses": juniAaaOutgoingErrorResponses,
       "juniAaaOutgoingAuthRequests": juniAaaOutgoingAuthRequests,
       "juniAaaIncomingAuthResponses": juniAaaIncomingAuthResponses,
       "juniAaaOutgoingReAuthRequests": juniAaaOutgoingReAuthRequests,
       "juniAaaIncomingReAuthResponses": juniAaaIncomingReAuthResponses,
       "juniAaaOutgoingAcctRequests": juniAaaOutgoingAcctRequests,
       "juniAaaIncomingAcctResponses": juniAaaIncomingAcctResponses,
       "juniAaaOutgoingDupAcctRequests": juniAaaOutgoingDupAcctRequests,
       "juniAaaIncomingDupAcctResponses": juniAaaIncomingDupAcctResponses,
       "juniAaaOutgoingAddrRequests": juniAaaOutgoingAddrRequests,
       "juniAaaIncomingAddrResponses": juniAaaIncomingAddrResponses,
       "juniAaaOutgoingBcastAcctRequests": juniAaaOutgoingBcastAcctRequests,
       "juniAaaIncomingBcastAcctResponses": juniAaaIncomingBcastAcctResponses,
       "juniAaaTimeout": juniAaaTimeout,
       "juniAaaTimeoutGeneral": juniAaaTimeoutGeneral,
       "juniAaaIdleTimeout": juniAaaIdleTimeout,
       "juniAaaSessionTimeout": juniAaaSessionTimeout,
       "juniAaaMonitorIngressTrafficOnly": juniAaaMonitorIngressTrafficOnly,
       "juniAaaTunnel": juniAaaTunnel,
       "juniAaaTunnelGeneral": juniAaaTunnelGeneral,
       "juniAaaTunnelClientName": juniAaaTunnelClientName,
       "juniAaaTunnelPassword": juniAaaTunnelPassword,
       "juniAaaTunnelNasPortMethod": juniAaaTunnelNasPortMethod,
       "juniAaaTunnelIgnoreNasPort": juniAaaTunnelIgnoreNasPort,
       "juniAaaTunnelIgnoreNasPortType": juniAaaTunnelIgnoreNasPortType,
       "juniAaaTunnelAssignmentIdFormat": juniAaaTunnelAssignmentIdFormat,
       "juniAaaTunnelSwitchProfile": juniAaaTunnelSwitchProfile,
       "juniAaaTunnelTxConnectSpeedMethod": juniAaaTunnelTxConnectSpeedMethod,
       "juniAaaTunnelGroups": juniAaaTunnelGroups,
       "juniAaaTunnelGroupTable": juniAaaTunnelGroupTable,
       "juniAaaTunnelGroupEntry": juniAaaTunnelGroupEntry,
       "juniAaaTunnelGroupName": juniAaaTunnelGroupName,
       "juniAaaTunnelGroupRowStatus": juniAaaTunnelGroupRowStatus,
       "juniAaaTunnelGroupTunnelTable": juniAaaTunnelGroupTunnelTable,
       "juniAaaTunnelGroupTunnelEntry": juniAaaTunnelGroupTunnelEntry,
       "juniAaaTunnelGroupTunnelName": juniAaaTunnelGroupTunnelName,
       "juniAaaTunnelGroupTunnelTag": juniAaaTunnelGroupTunnelTag,
       "juniAaaTunnelGroupTunnelPreference": juniAaaTunnelGroupTunnelPreference,
       "juniAaaTunnelGroupTunnelType": juniAaaTunnelGroupTunnelType,
       "juniAaaTunnelGroupTunnelMedium": juniAaaTunnelGroupTunnelMedium,
       "juniAaaTunnelGroupTunnelAddress": juniAaaTunnelGroupTunnelAddress,
       "juniAaaTunnelGroupTunnelPassword": juniAaaTunnelGroupTunnelPassword,
       "juniAaaTunnelGroupTunnelId": juniAaaTunnelGroupTunnelId,
       "juniAaaTunnelGroupTunnelHostName": juniAaaTunnelGroupTunnelHostName,
       "juniAaaTunnelGroupTunnelRowStatus": juniAaaTunnelGroupTunnelRowStatus,
       "juniAaaTunnelGroupTunnelServerName": juniAaaTunnelGroupTunnelServerName,
       "juniAaaTunnelGroupTunnelClientAddress": juniAaaTunnelGroupTunnelClientAddress,
       "juniAaaTunnelGroupTunnelMaxSessions": juniAaaTunnelGroupTunnelMaxSessions,
       "juniAaaTunnelGroupTunnelReceiveWindowSize": juniAaaTunnelGroupTunnelReceiveWindowSize,
       "juniAaaTunnelGroupTunnelRouterName": juniAaaTunnelGroupTunnelRouterName,
       "juniAaaTunnelGroupTunnelFailoverResync": juniAaaTunnelGroupTunnelFailoverResync,
       "juniAaaTunnelGroupTunnelSwitchProfile": juniAaaTunnelGroupTunnelSwitchProfile,
       "juniAaaTunnelGroupTunnelTxConnectSpeedMethod": juniAaaTunnelGroupTunnelTxConnectSpeedMethod,
       "juniAaaSubscribers": juniAaaSubscribers,
       "juniAaaSubscriberMaxCount": juniAaaSubscriberMaxCount,
       "juniAaaSubscriberPeakCount": juniAaaSubscriberPeakCount,
       "juniAaaSubscriberCount": juniAaaSubscriberCount,
       "juniAaaSubscriberTable": juniAaaSubscriberTable,
       "juniAaaSubscriberEntry": juniAaaSubscriberEntry,
       "juniAaaSubscriberHandle": juniAaaSubscriberHandle,
       "juniAaaSubscriberUserName": juniAaaSubscriberUserName,
       "juniAaaSubscriberRouterName": juniAaaSubscriberRouterName,
       "juniAaaSubscriberRouterIndex": juniAaaSubscriberRouterIndex,
       "juniAaaSubscriberLoginTime": juniAaaSubscriberLoginTime,
       "juniAaaSubscriberIpAddress": juniAaaSubscriberIpAddress,
       "juniAaaSubscriberIpAddressMask": juniAaaSubscriberIpAddressMask,
       "juniAaaSubscriberAddrAssignType": juniAaaSubscriberAddrAssignType,
       "juniAaaSubscriberInterfaceId": juniAaaSubscriberInterfaceId,
       "juniAaaSubscriberState": juniAaaSubscriberState,
       "juniAaaSubscriberClientType": juniAaaSubscriberClientType,
       "juniAaaSubscriberIngressPolicyName": juniAaaSubscriberIngressPolicyName,
       "juniAaaSubscriberEgressPolicyName": juniAaaSubscriberEgressPolicyName,
       "juniAaaSubscriberQosProfileName": juniAaaSubscriberQosProfileName,
       "juniAaaSubscriberRowStatus": juniAaaSubscriberRowStatus,
       "juniAaaSubscriberIpv6RouterIndex": juniAaaSubscriberIpv6RouterIndex,
       "juniAaaSubscriberIpv6AddrIfIdentifier": juniAaaSubscriberIpv6AddrIfIdentifier,
       "juniAaaSubscriberRouterSummaryTable": juniAaaSubscriberRouterSummaryTable,
       "juniAaaSubscriberRouterSummaryEntry": juniAaaSubscriberRouterSummaryEntry,
       "juniAaaSubscriberRouterSummaryRouterIndex": juniAaaSubscriberRouterSummaryRouterIndex,
       "juniAaaSubscriberRouterSummaryCount": juniAaaSubscriberRouterSummaryCount,
       "juniAaaSubscriberRouterTable": juniAaaSubscriberRouterTable,
       "juniAaaSubscriberRouterEntry": juniAaaSubscriberRouterEntry,
       "juniAaaSubscriberRouterRouterIndex": juniAaaSubscriberRouterRouterIndex,
       "juniAaaSubscriberRouterHandle": juniAaaSubscriberRouterHandle,
       "juniAaaSubscriberRouterRowStatus": juniAaaSubscriberRouterRowStatus,
       "juniAaaSubscriberLocationType": juniAaaSubscriberLocationType,
       "juniAaaSubscriberLocationSummaryTable": juniAaaSubscriberLocationSummaryTable,
       "juniAaaSubscriberLocationSummaryEntry": juniAaaSubscriberLocationSummaryEntry,
       "juniAaaSubscriberLocationSummaryLocationIndex": juniAaaSubscriberLocationSummaryLocationIndex,
       "juniAaaSubscriberLocationSummaryCount": juniAaaSubscriberLocationSummaryCount,
       "juniAaaSubscriberLocationTable": juniAaaSubscriberLocationTable,
       "juniAaaSubscriberLocationEntry": juniAaaSubscriberLocationEntry,
       "juniAaaSubscriberLocationLocationIndex": juniAaaSubscriberLocationLocationIndex,
       "juniAaaSubscriberLocationHandle": juniAaaSubscriberLocationHandle,
       "juniAaaSubscriberLocationRowStatus": juniAaaSubscriberLocationRowStatus,
       "juniAaaSubscriberPseudoPeakCount": juniAaaSubscriberPseudoPeakCount,
       "juniAaaSubscriberPseudoCount": juniAaaSubscriberPseudoCount,
       "juniAaaSubscriberIpv6AddrPrefixTable": juniAaaSubscriberIpv6AddrPrefixTable,
       "juniAaaSubscriberIpv6AddrPrefixEntry": juniAaaSubscriberIpv6AddrPrefixEntry,
       "juniAaaSubscriberIpv6AddrPrefix": juniAaaSubscriberIpv6AddrPrefix,
       "juniAaaSubscriberIpv6AddrPrefixSize": juniAaaSubscriberIpv6AddrPrefixSize,
       "juniAaaSubscriberExtTable": juniAaaSubscriberExtTable,
       "juniAaaSubscriberExtEntry": juniAaaSubscriberExtEntry,
       "juniAaaSubscriberExtUserName": juniAaaSubscriberExtUserName,
       "juniAaaSubscriberExtLoginTime": juniAaaSubscriberExtLoginTime,
       "juniAaaSubscriberExtIpAddress": juniAaaSubscriberExtIpAddress,
       "juniAaaSubscriberExtIpAddressMask": juniAaaSubscriberExtIpAddressMask,
       "juniAaaSubscriberExtAddrAssignType": juniAaaSubscriberExtAddrAssignType,
       "juniAaaSubscriberExtState": juniAaaSubscriberExtState,
       "juniAaaSubscriberExtClientType": juniAaaSubscriberExtClientType,
       "juniAaaSubscriberExtAcctSessionId": juniAaaSubscriberExtAcctSessionId,
       "juniAaaSubscriberExtClass": juniAaaSubscriberExtClass,
       "juniAaaSubscriberExtNasPort": juniAaaSubscriberExtNasPort,
       "juniAaaSubscriberExtNasPortType": juniAaaSubscriberExtNasPortType,
       "juniAaaSubscriberExtCalledStationId": juniAaaSubscriberExtCalledStationId,
       "juniAaaSubscriberExtCallingStationId": juniAaaSubscriberExtCallingStationId,
       "juniAaaSubscriberExtL2tpTunnelId": juniAaaSubscriberExtL2tpTunnelId,
       "juniAaaSubscriberInterfaceSummaryTable": juniAaaSubscriberInterfaceSummaryTable,
       "juniAaaSubscriberInterfaceSummaryEntry": juniAaaSubscriberInterfaceSummaryEntry,
       "juniAaaSubscriberInterfaceSummaryIndex": juniAaaSubscriberInterfaceSummaryIndex,
       "juniAaaSubscriberSubInterfaceSummaryIndex": juniAaaSubscriberSubInterfaceSummaryIndex,
       "juniAaaSubscriberInterfaceSummaryCount": juniAaaSubscriberInterfaceSummaryCount,
       "juniAaaSubscriberInterfaceTable": juniAaaSubscriberInterfaceTable,
       "juniAaaSubscriberInterfaceEntry": juniAaaSubscriberInterfaceEntry,
       "juniAaaSubscriberInterfaceIndex": juniAaaSubscriberInterfaceIndex,
       "juniAaaSubscriberSubInterfaceIndex": juniAaaSubscriberSubInterfaceIndex,
       "juniAaaSubscriberInterfaceHandle": juniAaaSubscriberInterfaceHandle,
       "juniAaaSubscriberInterfaceRowStatus": juniAaaSubscriberInterfaceRowStatus,
       "juniAaaSubscriberSlotSummaryTable": juniAaaSubscriberSlotSummaryTable,
       "juniAaaSubscriberSlotSummaryEntry": juniAaaSubscriberSlotSummaryEntry,
       "juniAaaSubscriberSlotSummarySlotIndex": juniAaaSubscriberSlotSummarySlotIndex,
       "juniAaaSubscriberSlotSummaryCount": juniAaaSubscriberSlotSummaryCount,
       "juniAaaSubscriberSlotTable": juniAaaSubscriberSlotTable,
       "juniAaaSubscriberSlotEntry": juniAaaSubscriberSlotEntry,
       "juniAaaSubscriberSlotIndex": juniAaaSubscriberSlotIndex,
       "juniAaaSubscriberSlotHandle": juniAaaSubscriberSlotHandle,
       "juniAaaSubscriberSlotRowStatus": juniAaaSubscriberSlotRowStatus,
       "juniAaaCapabilities": juniAaaCapabilities,
       "juniAaaAccountingCapability": juniAaaAccountingCapability,
       "juniAaaAddressAssignmentCapability": juniAaaAddressAssignmentCapability,
       "juniAaaBrasCapability": juniAaaBrasCapability,
       "juniAaaTunnelingCapability": juniAaaTunnelingCapability,
       "juniAaaMIBConformance": juniAaaMIBConformance,
       "juniAaaMIBCompliances": juniAaaMIBCompliances,
       "juniAaaCompliance": juniAaaCompliance,
       "juniAaaCompliance2": juniAaaCompliance2,
       "juniAaaCompliance3": juniAaaCompliance3,
       "juniAaaCompliance4": juniAaaCompliance4,
       "juniAaaCompliance5": juniAaaCompliance5,
       "juniAaaCompliance6": juniAaaCompliance6,
       "juniAaaCompliance7": juniAaaCompliance7,
       "juniAaaCompliance8": juniAaaCompliance8,
       "juniAaaCompliance9": juniAaaCompliance9,
       "juniAaaCompliance10": juniAaaCompliance10,
       "juniAaaCompliance11": juniAaaCompliance11,
       "juniAaaCompliance12": juniAaaCompliance12,
       "juniAaaCompliance13": juniAaaCompliance13,
       "juniAaaCompliance14": juniAaaCompliance14,
       "juniAaaCompliance15": juniAaaCompliance15,
       "juniAaaCompliance16": juniAaaCompliance16,
       "juniAaaCompliance17": juniAaaCompliance17,
       "juniAaaCompliance18": juniAaaCompliance18,
       "juniAaaCompliance19": juniAaaCompliance19,
       "juniAaaCompliance20": juniAaaCompliance20,
       "juniAaaCompliance21": juniAaaCompliance21,
       "juniAaaCompliance22": juniAaaCompliance22,
       "juniAaaCompliance23": juniAaaCompliance23,
       "juniAaaCompliance24": juniAaaCompliance24,
       "juniAaaMIBGroups": juniAaaMIBGroups,
       "juniAaaGroup": juniAaaGroup,
       "juniAaaGroup2": juniAaaGroup2,
       "juniAaaBasicGroup": juniAaaBasicGroup,
       "juniAaaBrasGroup": juniAaaBrasGroup,
       "juniAaaTunnelGroup": juniAaaTunnelGroup,
       "juniAaaAuthenticationGroup": juniAaaAuthenticationGroup,
       "juniAaaAccountingGroup": juniAaaAccountingGroup,
       "juniAaaAddressGroup": juniAaaAddressGroup,
       "juniAaaBrasGroup2": juniAaaBrasGroup2,
       "juniAaaBrasGroup3": juniAaaBrasGroup3,
       "juniAaaSubscriberGroup": juniAaaSubscriberGroup,
       "juniAaaCapabilitiesGroup": juniAaaCapabilitiesGroup,
       "juniAaaSubscriberGroup2": juniAaaSubscriberGroup2,
       "juniAaaAccountingGroup2": juniAaaAccountingGroup2,
       "juniAaaBrasGroup4": juniAaaBrasGroup4,
       "juniAaaSubscriberGroup3": juniAaaSubscriberGroup3,
       "juniAaaBrasGroup5": juniAaaBrasGroup5,
       "juniAaaTunnelGroup2": juniAaaTunnelGroup2,
       "juniAaaBrasGroup6": juniAaaBrasGroup6,
       "juniAaaBrasGroup7": juniAaaBrasGroup7,
       "juniAaaAddressGroup2": juniAaaAddressGroup2,
       "juniAaaSubscriberGroup4": juniAaaSubscriberGroup4,
       "juniAaaBrasGroup8": juniAaaBrasGroup8,
       "juniAaaBrasGroup9": juniAaaBrasGroup9,
       "juniAaaTunnelGroup3": juniAaaTunnelGroup3,
       "juniAaaAccountingGroup3": juniAaaAccountingGroup3,
       "juniAaaAuthenticationGroup2": juniAaaAuthenticationGroup2,
       "juniAaaAuthenticationGroup3": juniAaaAuthenticationGroup3,
       "juniAaaAccountingGroup4": juniAaaAccountingGroup4,
       "juniAaaTunnelGroup4": juniAaaTunnelGroup4,
       "juniAaaSubscriberGroup5": juniAaaSubscriberGroup5,
       "juniAaaBrasGroup10": juniAaaBrasGroup10,
       "juniAaaTunnelGroup5": juniAaaTunnelGroup5,
       "juniAaaBrasGroup11": juniAaaBrasGroup11,
       "juniAaaAccountingGroup5": juniAaaAccountingGroup5,
       "juniAaaBrasGroup12": juniAaaBrasGroup12,
       "juniAaaBrasGroup13": juniAaaBrasGroup13,
       "juniAaaBrasGroup14": juniAaaBrasGroup14,
       "juniAaaBrasGroup15": juniAaaBrasGroup15}
)
