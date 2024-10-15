# SNMP MIB module (Juniper-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:56 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(juniRouterName,) = mibBuilder.importSymbols(
    "Juniper-ROUTER-MIB",
    "juniRouterName")

(JuniEnable,
 JuniInterfaceLocation,
 JuniLogSeverity) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniInterfaceLocation",
    "JuniLogSeverity")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

juniDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22)
)
juniDhcpMIB.setRevisions(
        ("2007-01-31 20:38",
         "2005-11-04 19:53",
         "2005-09-27 21:25",
         "2005-12-05 21:31",
         "2004-11-08 16:16",
         "2005-10-19 21:47",
         "2004-09-09 20:02",
         "2004-01-03 00:59",
         "2003-09-05 18:59",
         "2002-12-17 16:59",
         "2002-05-10 19:27",
         "2001-03-30 18:09",
         "2000-02-03 19:50",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniDhcpLocalServerPoolName(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class JuniDhcpLocalServerPoolGroupName(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class JuniDhcpLocalServerPoolDomainName(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class JuniDhcpLocalServerPoolNetBiosNodeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("netBiosNodeTypeBroadcast", 2),
          ("netBiosNodeTypeHybrid", 5),
          ("netBiosNodeTypeMixed", 4),
          ("netBiosNodeTypeNone", 1),
          ("netBiosNodeTypePeerToPeer", 3))
    )



class JuniDhcpLocalServerModeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localServerModeTypeEqualAccess", 1),
          ("localServerModeTypeStandalone", 2))
    )



class JuniDhcpLocalServerPhysAddressString(OctetString, TextualConvention):
    status = "current"
    displayHint = "48a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )



# MIB Managed Objects in the order of their OIDs

_JuniDhcpObjects_ObjectIdentity = ObjectIdentity
juniDhcpObjects = _JuniDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1)
)
_JuniDhcpRelay_ObjectIdentity = ObjectIdentity
juniDhcpRelay = _JuniDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1)
)
_JuniDhcpLocalServerRelayTraps_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerRelayTraps = _JuniDhcpLocalServerRelayTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 0)
)
_JuniDhcpRelayScalars_ObjectIdentity = ObjectIdentity
juniDhcpRelayScalars = _JuniDhcpRelayScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1)
)
_JuniDhcpRelayAgentInfoEnable_Type = JuniEnable
_JuniDhcpRelayAgentInfoEnable_Object = MibScalar
juniDhcpRelayAgentInfoEnable = _JuniDhcpRelayAgentInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 1),
    _JuniDhcpRelayAgentInfoEnable_Type()
)
juniDhcpRelayAgentInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentInfoEnable.setStatus("deprecated")
_JuniDhcpRelayBadMessages_Type = Counter32
_JuniDhcpRelayBadMessages_Object = MibScalar
juniDhcpRelayBadMessages = _JuniDhcpRelayBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 2),
    _JuniDhcpRelayBadMessages_Type()
)
juniDhcpRelayBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayBadMessages.setStatus("current")
_JuniDhcpRelayUnknownMessages_Type = Counter32
_JuniDhcpRelayUnknownMessages_Object = MibScalar
juniDhcpRelayUnknownMessages = _JuniDhcpRelayUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 3),
    _JuniDhcpRelayUnknownMessages_Type()
)
juniDhcpRelayUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayUnknownMessages.setStatus("current")
_JuniDhcpRelayAgentInfoAlreadyPresents_Type = Counter32
_JuniDhcpRelayAgentInfoAlreadyPresents_Object = MibScalar
juniDhcpRelayAgentInfoAlreadyPresents = _JuniDhcpRelayAgentInfoAlreadyPresents_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 4),
    _JuniDhcpRelayAgentInfoAlreadyPresents_Type()
)
juniDhcpRelayAgentInfoAlreadyPresents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentInfoAlreadyPresents.setStatus("current")
_JuniDhcpRelayGatewayAddrSpoofs_Type = Counter32
_JuniDhcpRelayGatewayAddrSpoofs_Object = MibScalar
juniDhcpRelayGatewayAddrSpoofs = _JuniDhcpRelayGatewayAddrSpoofs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 5),
    _JuniDhcpRelayGatewayAddrSpoofs_Type()
)
juniDhcpRelayGatewayAddrSpoofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayGatewayAddrSpoofs.setStatus("current")
_JuniDhcpRelayAgentCircuitIdEnable_Type = JuniEnable
_JuniDhcpRelayAgentCircuitIdEnable_Object = MibScalar
juniDhcpRelayAgentCircuitIdEnable = _JuniDhcpRelayAgentCircuitIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 6),
    _JuniDhcpRelayAgentCircuitIdEnable_Type()
)
juniDhcpRelayAgentCircuitIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentCircuitIdEnable.setStatus("current")
_JuniDhcpRelayAgentRemoteIdEnable_Type = JuniEnable
_JuniDhcpRelayAgentRemoteIdEnable_Object = MibScalar
juniDhcpRelayAgentRemoteIdEnable = _JuniDhcpRelayAgentRemoteIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 7),
    _JuniDhcpRelayAgentRemoteIdEnable_Type()
)
juniDhcpRelayAgentRemoteIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentRemoteIdEnable.setStatus("current")
_JuniDhcpRelayAgentHostnameEnable_Type = JuniEnable
_JuniDhcpRelayAgentHostnameEnable_Object = MibScalar
juniDhcpRelayAgentHostnameEnable = _JuniDhcpRelayAgentHostnameEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 8),
    _JuniDhcpRelayAgentHostnameEnable_Type()
)
juniDhcpRelayAgentHostnameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentHostnameEnable.setStatus("current")
_JuniDhcpRelayAgentVrnameEnable_Type = JuniEnable
_JuniDhcpRelayAgentVrnameEnable_Object = MibScalar
juniDhcpRelayAgentVrnameEnable = _JuniDhcpRelayAgentVrnameEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 9),
    _JuniDhcpRelayAgentVrnameEnable_Type()
)
juniDhcpRelayAgentVrnameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentVrnameEnable.setStatus("current")
_JuniDhcpRelayAgentExcludeSubIdEnable_Type = JuniEnable
_JuniDhcpRelayAgentExcludeSubIdEnable_Object = MibScalar
juniDhcpRelayAgentExcludeSubIdEnable = _JuniDhcpRelayAgentExcludeSubIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 10),
    _JuniDhcpRelayAgentExcludeSubIdEnable_Type()
)
juniDhcpRelayAgentExcludeSubIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentExcludeSubIdEnable.setStatus("current")


class _JuniDhcpRelayAgentTrustAllEnable_Type(JuniEnable):
    """Custom type juniDhcpRelayAgentTrustAllEnable based on JuniEnable"""


_JuniDhcpRelayAgentTrustAllEnable_Object = MibScalar
juniDhcpRelayAgentTrustAllEnable = _JuniDhcpRelayAgentTrustAllEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 11),
    _JuniDhcpRelayAgentTrustAllEnable_Type()
)
juniDhcpRelayAgentTrustAllEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentTrustAllEnable.setStatus("current")
_JuniDhcpRelayAgentInfoAlreadyPresentForwards_Type = Counter32
_JuniDhcpRelayAgentInfoAlreadyPresentForwards_Object = MibScalar
juniDhcpRelayAgentInfoAlreadyPresentForwards = _JuniDhcpRelayAgentInfoAlreadyPresentForwards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 12),
    _JuniDhcpRelayAgentInfoAlreadyPresentForwards_Type()
)
juniDhcpRelayAgentInfoAlreadyPresentForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentInfoAlreadyPresentForwards.setStatus("current")
_JuniDhcpRelayAgentGiaddrOverrides_Type = Counter32
_JuniDhcpRelayAgentGiaddrOverrides_Object = MibScalar
juniDhcpRelayAgentGiaddrOverrides = _JuniDhcpRelayAgentGiaddrOverrides_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 13),
    _JuniDhcpRelayAgentGiaddrOverrides_Type()
)
juniDhcpRelayAgentGiaddrOverrides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentGiaddrOverrides.setStatus("current")
_JuniDhcpRelayAgentOptionOverrides_Type = Counter32
_JuniDhcpRelayAgentOptionOverrides_Object = MibScalar
juniDhcpRelayAgentOptionOverrides = _JuniDhcpRelayAgentOptionOverrides_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 14),
    _JuniDhcpRelayAgentOptionOverrides_Type()
)
juniDhcpRelayAgentOptionOverrides.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentOptionOverrides.setStatus("current")
_JuniDhcpRelayDiscoverDiscards_Type = Counter32
_JuniDhcpRelayDiscoverDiscards_Object = MibScalar
juniDhcpRelayDiscoverDiscards = _JuniDhcpRelayDiscoverDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 15),
    _JuniDhcpRelayDiscoverDiscards_Type()
)
juniDhcpRelayDiscoverDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayDiscoverDiscards.setStatus("current")
_JuniDhcpRelayPacketDiscards_Type = Counter32
_JuniDhcpRelayPacketDiscards_Object = MibScalar
juniDhcpRelayPacketDiscards = _JuniDhcpRelayPacketDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 16),
    _JuniDhcpRelayPacketDiscards_Type()
)
juniDhcpRelayPacketDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayPacketDiscards.setStatus("current")
_JuniDhcpRelayUnknownRequestMessages_Type = Counter32
_JuniDhcpRelayUnknownRequestMessages_Object = MibScalar
juniDhcpRelayUnknownRequestMessages = _JuniDhcpRelayUnknownRequestMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 17),
    _JuniDhcpRelayUnknownRequestMessages_Type()
)
juniDhcpRelayUnknownRequestMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayUnknownRequestMessages.setStatus("current")
_JuniDhcpRelayUnknownReplyMessages_Type = Counter32
_JuniDhcpRelayUnknownReplyMessages_Object = MibScalar
juniDhcpRelayUnknownReplyMessages = _JuniDhcpRelayUnknownReplyMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 18),
    _JuniDhcpRelayUnknownReplyMessages_Type()
)
juniDhcpRelayUnknownReplyMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayUnknownReplyMessages.setStatus("current")
_JuniDhcpRelayDuplicateRequestDiscards_Type = Counter32
_JuniDhcpRelayDuplicateRequestDiscards_Object = MibScalar
juniDhcpRelayDuplicateRequestDiscards = _JuniDhcpRelayDuplicateRequestDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 19),
    _JuniDhcpRelayDuplicateRequestDiscards_Type()
)
juniDhcpRelayDuplicateRequestDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayDuplicateRequestDiscards.setStatus("current")
_JuniDhcpRelayPacketsTransmitted_Type = Counter32
_JuniDhcpRelayPacketsTransmitted_Object = MibScalar
juniDhcpRelayPacketsTransmitted = _JuniDhcpRelayPacketsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 20),
    _JuniDhcpRelayPacketsTransmitted_Type()
)
juniDhcpRelayPacketsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayPacketsTransmitted.setStatus("current")
_JuniDhcpRelayPacketsReceived_Type = Counter32
_JuniDhcpRelayPacketsReceived_Object = MibScalar
juniDhcpRelayPacketsReceived = _JuniDhcpRelayPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 21),
    _JuniDhcpRelayPacketsReceived_Type()
)
juniDhcpRelayPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayPacketsReceived.setStatus("current")
_JuniDhcpRelayUnknownXidDiscards_Type = Counter32
_JuniDhcpRelayUnknownXidDiscards_Object = MibScalar
juniDhcpRelayUnknownXidDiscards = _JuniDhcpRelayUnknownXidDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 22),
    _JuniDhcpRelayUnknownXidDiscards_Type()
)
juniDhcpRelayUnknownXidDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayUnknownXidDiscards.setStatus("current")
_JuniDhcpRelayDroppedStaleRequestDiscards_Type = Counter32
_JuniDhcpRelayDroppedStaleRequestDiscards_Object = MibScalar
juniDhcpRelayDroppedStaleRequestDiscards = _JuniDhcpRelayDroppedStaleRequestDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 23),
    _JuniDhcpRelayDroppedStaleRequestDiscards_Type()
)
juniDhcpRelayDroppedStaleRequestDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpRelayDroppedStaleRequestDiscards.setStatus("current")


class _JuniDhcpRelayLayer2UnicastReplies_Type(JuniEnable):
    """Custom type juniDhcpRelayLayer2UnicastReplies based on JuniEnable"""


_JuniDhcpRelayLayer2UnicastReplies_Object = MibScalar
juniDhcpRelayLayer2UnicastReplies = _JuniDhcpRelayLayer2UnicastReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 24),
    _JuniDhcpRelayLayer2UnicastReplies_Type()
)
juniDhcpRelayLayer2UnicastReplies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayLayer2UnicastReplies.setStatus("current")


class _JuniDhcpRelayGiaddrSelectsInterface_Type(JuniEnable):
    """Custom type juniDhcpRelayGiaddrSelectsInterface based on JuniEnable"""


_JuniDhcpRelayGiaddrSelectsInterface_Object = MibScalar
juniDhcpRelayGiaddrSelectsInterface = _JuniDhcpRelayGiaddrSelectsInterface_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 25),
    _JuniDhcpRelayGiaddrSelectsInterface_Type()
)
juniDhcpRelayGiaddrSelectsInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayGiaddrSelectsInterface.setStatus("current")


class _JuniDhcpRelayAgentVendorSpecificSuboption_Type(Bits):
    """Custom type juniDhcpRelayAgentVendorSpecificSuboption based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniDhcpRelayAgentVendorSpecificLayer2CircuitId", 0),
          ("juniDhcpRelayAgentVendorSpecificUserPacketClass", 1))
    )

_JuniDhcpRelayAgentVendorSpecificSuboption_Type.__name__ = "Bits"
_JuniDhcpRelayAgentVendorSpecificSuboption_Object = MibScalar
juniDhcpRelayAgentVendorSpecificSuboption = _JuniDhcpRelayAgentVendorSpecificSuboption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 26),
    _JuniDhcpRelayAgentVendorSpecificSuboption_Type()
)
juniDhcpRelayAgentVendorSpecificSuboption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayAgentVendorSpecificSuboption.setStatus("current")


class _JuniDhcpRelayBroadcastFlagReplies_Type(JuniEnable):
    """Custom type juniDhcpRelayBroadcastFlagReplies based on JuniEnable"""


_JuniDhcpRelayBroadcastFlagReplies_Object = MibScalar
juniDhcpRelayBroadcastFlagReplies = _JuniDhcpRelayBroadcastFlagReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 27),
    _JuniDhcpRelayBroadcastFlagReplies_Type()
)
juniDhcpRelayBroadcastFlagReplies.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpRelayBroadcastFlagReplies.setStatus("current")
_JuniDhcpRelayServerTable_Object = MibTable
juniDhcpRelayServerTable = _JuniDhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniDhcpRelayServerTable.setStatus("current")
_JuniDhcpRelayServerEntry_Object = MibTableRow
juniDhcpRelayServerEntry = _JuniDhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2, 1)
)
juniDhcpRelayServerEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpRelayServerAddress"),
)
if mibBuilder.loadTexts:
    juniDhcpRelayServerEntry.setStatus("current")
_JuniDhcpRelayServerAddress_Type = IpAddress
_JuniDhcpRelayServerAddress_Object = MibTableColumn
juniDhcpRelayServerAddress = _JuniDhcpRelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2, 1, 1),
    _JuniDhcpRelayServerAddress_Type()
)
juniDhcpRelayServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpRelayServerAddress.setStatus("current")
_JuniDhcpRelayServerRowStatus_Type = RowStatus
_JuniDhcpRelayServerRowStatus_Object = MibTableColumn
juniDhcpRelayServerRowStatus = _JuniDhcpRelayServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2, 1, 2),
    _JuniDhcpRelayServerRowStatus_Type()
)
juniDhcpRelayServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpRelayServerRowStatus.setStatus("current")
_JuniDhcpProxy_ObjectIdentity = ObjectIdentity
juniDhcpProxy = _JuniDhcpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2)
)
_JuniDhcpLocalServerProxyTraps_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerProxyTraps = _JuniDhcpLocalServerProxyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 0)
)
_JuniDhcpProxyClient_ObjectIdentity = ObjectIdentity
juniDhcpProxyClient = _JuniDhcpProxyClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1)
)
_JuniDhcpProxyClientScalars_ObjectIdentity = ObjectIdentity
juniDhcpProxyClientScalars = _JuniDhcpProxyClientScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 1)
)
_JuniDhcpProxyClientUnknownServers_Type = Counter32
_JuniDhcpProxyClientUnknownServers_Object = MibScalar
juniDhcpProxyClientUnknownServers = _JuniDhcpProxyClientUnknownServers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 1, 1),
    _JuniDhcpProxyClientUnknownServers_Type()
)
juniDhcpProxyClientUnknownServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientUnknownServers.setStatus("current")
_JuniDhcpProxyClientServerTable_Object = MibTable
juniDhcpProxyClientServerTable = _JuniDhcpProxyClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerTable.setStatus("current")
_JuniDhcpProxyClientServerEntry_Object = MibTableRow
juniDhcpProxyClientServerEntry = _JuniDhcpProxyClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1)
)
juniDhcpProxyClientServerEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpProxyClientServerAddress"),
)
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerEntry.setStatus("current")
_JuniDhcpProxyClientServerAddress_Type = IpAddress
_JuniDhcpProxyClientServerAddress_Object = MibTableColumn
juniDhcpProxyClientServerAddress = _JuniDhcpProxyClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 1),
    _JuniDhcpProxyClientServerAddress_Type()
)
juniDhcpProxyClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerAddress.setStatus("current")
_JuniDhcpProxyClientServerRowStatus_Type = RowStatus
_JuniDhcpProxyClientServerRowStatus_Object = MibTableColumn
juniDhcpProxyClientServerRowStatus = _JuniDhcpProxyClientServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 2),
    _JuniDhcpProxyClientServerRowStatus_Type()
)
juniDhcpProxyClientServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerRowStatus.setStatus("current")


class _JuniDhcpProxyClientServerAdminStatus_Type(Integer32):
    """Custom type juniDhcpProxyClientServerAdminStatus based on Integer32"""
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
          ("drain", 1),
          ("enable", 2))
    )


_JuniDhcpProxyClientServerAdminStatus_Type.__name__ = "Integer32"
_JuniDhcpProxyClientServerAdminStatus_Object = MibTableColumn
juniDhcpProxyClientServerAdminStatus = _JuniDhcpProxyClientServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 3),
    _JuniDhcpProxyClientServerAdminStatus_Type()
)
juniDhcpProxyClientServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerAdminStatus.setStatus("current")


class _JuniDhcpProxyClientServerOperStatus_Type(Integer32):
    """Custom type juniDhcpProxyClientServerOperStatus based on Integer32"""
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
          ("draining", 1),
          ("enabled", 2))
    )


_JuniDhcpProxyClientServerOperStatus_Type.__name__ = "Integer32"
_JuniDhcpProxyClientServerOperStatus_Object = MibTableColumn
juniDhcpProxyClientServerOperStatus = _JuniDhcpProxyClientServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 4),
    _JuniDhcpProxyClientServerOperStatus_Type()
)
juniDhcpProxyClientServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerOperStatus.setStatus("current")
_JuniDhcpProxyClientServerLeases_Type = Counter32
_JuniDhcpProxyClientServerLeases_Object = MibTableColumn
juniDhcpProxyClientServerLeases = _JuniDhcpProxyClientServerLeases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 5),
    _JuniDhcpProxyClientServerLeases_Type()
)
juniDhcpProxyClientServerLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerLeases.setStatus("current")
_JuniDhcpProxyClientServerDiscovers_Type = Counter32
_JuniDhcpProxyClientServerDiscovers_Object = MibTableColumn
juniDhcpProxyClientServerDiscovers = _JuniDhcpProxyClientServerDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 6),
    _JuniDhcpProxyClientServerDiscovers_Type()
)
juniDhcpProxyClientServerDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerDiscovers.setStatus("current")
_JuniDhcpProxyClientServerOffers_Type = Counter32
_JuniDhcpProxyClientServerOffers_Object = MibTableColumn
juniDhcpProxyClientServerOffers = _JuniDhcpProxyClientServerOffers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 7),
    _JuniDhcpProxyClientServerOffers_Type()
)
juniDhcpProxyClientServerOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerOffers.setStatus("current")
_JuniDhcpProxyClientServerRequests_Type = Counter32
_JuniDhcpProxyClientServerRequests_Object = MibTableColumn
juniDhcpProxyClientServerRequests = _JuniDhcpProxyClientServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 8),
    _JuniDhcpProxyClientServerRequests_Type()
)
juniDhcpProxyClientServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerRequests.setStatus("current")
_JuniDhcpProxyClientServerAcks_Type = Counter32
_JuniDhcpProxyClientServerAcks_Object = MibTableColumn
juniDhcpProxyClientServerAcks = _JuniDhcpProxyClientServerAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 9),
    _JuniDhcpProxyClientServerAcks_Type()
)
juniDhcpProxyClientServerAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerAcks.setStatus("current")
_JuniDhcpProxyClientServerNaks_Type = Counter32
_JuniDhcpProxyClientServerNaks_Object = MibTableColumn
juniDhcpProxyClientServerNaks = _JuniDhcpProxyClientServerNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 10),
    _JuniDhcpProxyClientServerNaks_Type()
)
juniDhcpProxyClientServerNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerNaks.setStatus("current")
_JuniDhcpProxyClientServerDeclines_Type = Counter32
_JuniDhcpProxyClientServerDeclines_Object = MibTableColumn
juniDhcpProxyClientServerDeclines = _JuniDhcpProxyClientServerDeclines_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 11),
    _JuniDhcpProxyClientServerDeclines_Type()
)
juniDhcpProxyClientServerDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerDeclines.setStatus("current")
_JuniDhcpProxyClientServerReleases_Type = Counter32
_JuniDhcpProxyClientServerReleases_Object = MibTableColumn
juniDhcpProxyClientServerReleases = _JuniDhcpProxyClientServerReleases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 12),
    _JuniDhcpProxyClientServerReleases_Type()
)
juniDhcpProxyClientServerReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerReleases.setStatus("current")
_JuniDhcpProxyClientServerInforms_Type = Counter32
_JuniDhcpProxyClientServerInforms_Object = MibTableColumn
juniDhcpProxyClientServerInforms = _JuniDhcpProxyClientServerInforms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 13),
    _JuniDhcpProxyClientServerInforms_Type()
)
juniDhcpProxyClientServerInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerInforms.setStatus("current")
_JuniDhcpProxyClientServerBadMessages_Type = Counter32
_JuniDhcpProxyClientServerBadMessages_Object = MibTableColumn
juniDhcpProxyClientServerBadMessages = _JuniDhcpProxyClientServerBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 14),
    _JuniDhcpProxyClientServerBadMessages_Type()
)
juniDhcpProxyClientServerBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerBadMessages.setStatus("current")
_JuniDhcpProxyClientServerUnknownMessages_Type = Counter32
_JuniDhcpProxyClientServerUnknownMessages_Object = MibTableColumn
juniDhcpProxyClientServerUnknownMessages = _JuniDhcpProxyClientServerUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 15),
    _JuniDhcpProxyClientServerUnknownMessages_Type()
)
juniDhcpProxyClientServerUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpProxyClientServerUnknownMessages.setStatus("current")
_JuniDhcpProxyServer_ObjectIdentity = ObjectIdentity
juniDhcpProxyServer = _JuniDhcpProxyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 2)
)
_JuniDhcpLocalServerObjects_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerObjects = _JuniDhcpLocalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3)
)
_JuniDhcpLocalServerTraps_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerTraps = _JuniDhcpLocalServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0)
)
_JuniDhcpLocalServerStatistics_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerStatistics = _JuniDhcpLocalServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1)
)
_JuniDhcpLocalServerMemUsage_Type = Counter32
_JuniDhcpLocalServerMemUsage_Object = MibScalar
juniDhcpLocalServerMemUsage = _JuniDhcpLocalServerMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 1),
    _JuniDhcpLocalServerMemUsage_Type()
)
juniDhcpLocalServerMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerMemUsage.setStatus("current")
_JuniDhcpLocalServerNumBindings_Type = Counter32
_JuniDhcpLocalServerNumBindings_Object = MibScalar
juniDhcpLocalServerNumBindings = _JuniDhcpLocalServerNumBindings_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 2),
    _JuniDhcpLocalServerNumBindings_Type()
)
juniDhcpLocalServerNumBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerNumBindings.setStatus("current")
_JuniDhcpLocalServerRxDiscovers_Type = Counter32
_JuniDhcpLocalServerRxDiscovers_Object = MibScalar
juniDhcpLocalServerRxDiscovers = _JuniDhcpLocalServerRxDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 3),
    _JuniDhcpLocalServerRxDiscovers_Type()
)
juniDhcpLocalServerRxDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxDiscovers.setStatus("current")
_JuniDhcpLocalServerRxAccepts_Type = Counter32
_JuniDhcpLocalServerRxAccepts_Object = MibScalar
juniDhcpLocalServerRxAccepts = _JuniDhcpLocalServerRxAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 4),
    _JuniDhcpLocalServerRxAccepts_Type()
)
juniDhcpLocalServerRxAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxAccepts.setStatus("current")
_JuniDhcpLocalServerRxRenews_Type = Counter32
_JuniDhcpLocalServerRxRenews_Object = MibScalar
juniDhcpLocalServerRxRenews = _JuniDhcpLocalServerRxRenews_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 5),
    _JuniDhcpLocalServerRxRenews_Type()
)
juniDhcpLocalServerRxRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxRenews.setStatus("current")
_JuniDhcpLocalServerRxDeclines_Type = Counter32
_JuniDhcpLocalServerRxDeclines_Object = MibScalar
juniDhcpLocalServerRxDeclines = _JuniDhcpLocalServerRxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 6),
    _JuniDhcpLocalServerRxDeclines_Type()
)
juniDhcpLocalServerRxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxDeclines.setStatus("current")
_JuniDhcpLocalServerRxReleases_Type = Counter32
_JuniDhcpLocalServerRxReleases_Object = MibScalar
juniDhcpLocalServerRxReleases = _JuniDhcpLocalServerRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 7),
    _JuniDhcpLocalServerRxReleases_Type()
)
juniDhcpLocalServerRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxReleases.setStatus("current")
_JuniDhcpLocalServerRxInforms_Type = Counter32
_JuniDhcpLocalServerRxInforms_Object = MibScalar
juniDhcpLocalServerRxInforms = _JuniDhcpLocalServerRxInforms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 8),
    _JuniDhcpLocalServerRxInforms_Type()
)
juniDhcpLocalServerRxInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxInforms.setStatus("current")
_JuniDhcpLocalServerTxOffers_Type = Counter32
_JuniDhcpLocalServerTxOffers_Object = MibScalar
juniDhcpLocalServerTxOffers = _JuniDhcpLocalServerTxOffers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 9),
    _JuniDhcpLocalServerTxOffers_Type()
)
juniDhcpLocalServerTxOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxOffers.setStatus("current")
_JuniDhcpLocalServerTxAcks_Type = Counter32
_JuniDhcpLocalServerTxAcks_Object = MibScalar
juniDhcpLocalServerTxAcks = _JuniDhcpLocalServerTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 10),
    _JuniDhcpLocalServerTxAcks_Type()
)
juniDhcpLocalServerTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxAcks.setStatus("current")
_JuniDhcpLocalServerTxNaks_Type = Counter32
_JuniDhcpLocalServerTxNaks_Object = MibScalar
juniDhcpLocalServerTxNaks = _JuniDhcpLocalServerTxNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 11),
    _JuniDhcpLocalServerTxNaks_Type()
)
juniDhcpLocalServerTxNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxNaks.setStatus("current")
_JuniDhcpLocalServerUnknownMessages_Type = Counter32
_JuniDhcpLocalServerUnknownMessages_Object = MibScalar
juniDhcpLocalServerUnknownMessages = _JuniDhcpLocalServerUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 12),
    _JuniDhcpLocalServerUnknownMessages_Type()
)
juniDhcpLocalServerUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerUnknownMessages.setStatus("deprecated")
_JuniDhcpLocalServerBadMessages_Type = Counter32
_JuniDhcpLocalServerBadMessages_Object = MibScalar
juniDhcpLocalServerBadMessages = _JuniDhcpLocalServerBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 13),
    _JuniDhcpLocalServerBadMessages_Type()
)
juniDhcpLocalServerBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBadMessages.setStatus("deprecated")
_JuniDhcpLocalServerPacketsIn_Type = Counter32
_JuniDhcpLocalServerPacketsIn_Object = MibScalar
juniDhcpLocalServerPacketsIn = _JuniDhcpLocalServerPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 14),
    _JuniDhcpLocalServerPacketsIn_Type()
)
juniDhcpLocalServerPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPacketsIn.setStatus("current")
_JuniDhcpLocalServerPacketsOut_Type = Counter32
_JuniDhcpLocalServerPacketsOut_Object = MibScalar
juniDhcpLocalServerPacketsOut = _JuniDhcpLocalServerPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 15),
    _JuniDhcpLocalServerPacketsOut_Type()
)
juniDhcpLocalServerPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPacketsOut.setStatus("current")
_JuniDhcpLocalServerRxRebinds_Type = Counter32
_JuniDhcpLocalServerRxRebinds_Object = MibScalar
juniDhcpLocalServerRxRebinds = _JuniDhcpLocalServerRxRebinds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 16),
    _JuniDhcpLocalServerRxRebinds_Type()
)
juniDhcpLocalServerRxRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxRebinds.setStatus("current")
_JuniDhcpLocalServerRxUnknownClients_Type = Counter32
_JuniDhcpLocalServerRxUnknownClients_Object = MibScalar
juniDhcpLocalServerRxUnknownClients = _JuniDhcpLocalServerRxUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 17),
    _JuniDhcpLocalServerRxUnknownClients_Type()
)
juniDhcpLocalServerRxUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxUnknownClients.setStatus("current")
_JuniDhcpLocalServerRxInErrors_Type = Counter32
_JuniDhcpLocalServerRxInErrors_Object = MibScalar
juniDhcpLocalServerRxInErrors = _JuniDhcpLocalServerRxInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 18),
    _JuniDhcpLocalServerRxInErrors_Type()
)
juniDhcpLocalServerRxInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxInErrors.setStatus("current")
_JuniDhcpLocalServerRxInDiscards_Type = Counter32
_JuniDhcpLocalServerRxInDiscards_Object = MibScalar
juniDhcpLocalServerRxInDiscards = _JuniDhcpLocalServerRxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 19),
    _JuniDhcpLocalServerRxInDiscards_Type()
)
juniDhcpLocalServerRxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxInDiscards.setStatus("current")
_JuniDhcpLocalServerTxRenewAcks_Type = Counter32
_JuniDhcpLocalServerTxRenewAcks_Object = MibScalar
juniDhcpLocalServerTxRenewAcks = _JuniDhcpLocalServerTxRenewAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 20),
    _JuniDhcpLocalServerTxRenewAcks_Type()
)
juniDhcpLocalServerTxRenewAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxRenewAcks.setStatus("current")
_JuniDhcpLocalServerTxRebindAcks_Type = Counter32
_JuniDhcpLocalServerTxRebindAcks_Object = MibScalar
juniDhcpLocalServerTxRebindAcks = _JuniDhcpLocalServerTxRebindAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 21),
    _JuniDhcpLocalServerTxRebindAcks_Type()
)
juniDhcpLocalServerTxRebindAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxRebindAcks.setStatus("current")
_JuniDhcpLocalServerTxRenewNaks_Type = Counter32
_JuniDhcpLocalServerTxRenewNaks_Object = MibScalar
juniDhcpLocalServerTxRenewNaks = _JuniDhcpLocalServerTxRenewNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 22),
    _JuniDhcpLocalServerTxRenewNaks_Type()
)
juniDhcpLocalServerTxRenewNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxRenewNaks.setStatus("current")
_JuniDhcpLocalServerTxRebindNaks_Type = Counter32
_JuniDhcpLocalServerTxRebindNaks_Object = MibScalar
juniDhcpLocalServerTxRebindNaks = _JuniDhcpLocalServerTxRebindNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 23),
    _JuniDhcpLocalServerTxRebindNaks_Type()
)
juniDhcpLocalServerTxRebindNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxRebindNaks.setStatus("current")
_JuniDhcpLocalServerTxOutErrors_Type = Counter32
_JuniDhcpLocalServerTxOutErrors_Object = MibScalar
juniDhcpLocalServerTxOutErrors = _JuniDhcpLocalServerTxOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 24),
    _JuniDhcpLocalServerTxOutErrors_Type()
)
juniDhcpLocalServerTxOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxOutErrors.setStatus("current")
_JuniDhcpLocalServerTxOutDiscards_Type = Counter32
_JuniDhcpLocalServerTxOutDiscards_Object = MibScalar
juniDhcpLocalServerTxOutDiscards = _JuniDhcpLocalServerTxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 25),
    _JuniDhcpLocalServerTxOutDiscards_Type()
)
juniDhcpLocalServerTxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerTxOutDiscards.setStatus("current")
_JuniDhcpLocalServerRxOtherRequests_Type = Counter32
_JuniDhcpLocalServerRxOtherRequests_Object = MibScalar
juniDhcpLocalServerRxOtherRequests = _JuniDhcpLocalServerRxOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 26),
    _JuniDhcpLocalServerRxOtherRequests_Type()
)
juniDhcpLocalServerRxOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerRxOtherRequests.setStatus("current")
_JuniDhcpLocalServerSubInterfaceStatisticsTable_Object = MibTable
juniDhcpLocalServerSubInterfaceStatisticsTable = _JuniDhcpLocalServerSubInterfaceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceStatisticsTable.setStatus("current")
_JuniDhcpLocalServerSubInterfaceStatisticsEntry_Object = MibTableRow
juniDhcpLocalServerSubInterfaceStatisticsEntry = _JuniDhcpLocalServerSubInterfaceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1)
)
juniDhcpLocalServerSubInterfaceStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "InterfaceIndex"),
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceStatisticsEntry.setStatus("current")
_JuniDhcpLocalServerSubInterfaceMemUsage_Type = Counter32
_JuniDhcpLocalServerSubInterfaceMemUsage_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceMemUsage = _JuniDhcpLocalServerSubInterfaceMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 1),
    _JuniDhcpLocalServerSubInterfaceMemUsage_Type()
)
juniDhcpLocalServerSubInterfaceMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceMemUsage.setStatus("current")
_JuniDhcpLocalServerSubInterfaceNumBindings_Type = Counter32
_JuniDhcpLocalServerSubInterfaceNumBindings_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceNumBindings = _JuniDhcpLocalServerSubInterfaceNumBindings_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 2),
    _JuniDhcpLocalServerSubInterfaceNumBindings_Type()
)
juniDhcpLocalServerSubInterfaceNumBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceNumBindings.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxDiscovers_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxDiscovers_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxDiscovers = _JuniDhcpLocalServerSubInterfaceRxDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 3),
    _JuniDhcpLocalServerSubInterfaceRxDiscovers_Type()
)
juniDhcpLocalServerSubInterfaceRxDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxDiscovers.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxAccepts_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxAccepts_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxAccepts = _JuniDhcpLocalServerSubInterfaceRxAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 4),
    _JuniDhcpLocalServerSubInterfaceRxAccepts_Type()
)
juniDhcpLocalServerSubInterfaceRxAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxAccepts.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxRenews_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxRenews_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxRenews = _JuniDhcpLocalServerSubInterfaceRxRenews_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 5),
    _JuniDhcpLocalServerSubInterfaceRxRenews_Type()
)
juniDhcpLocalServerSubInterfaceRxRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxRenews.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxDeclines_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxDeclines_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxDeclines = _JuniDhcpLocalServerSubInterfaceRxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 6),
    _JuniDhcpLocalServerSubInterfaceRxDeclines_Type()
)
juniDhcpLocalServerSubInterfaceRxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxDeclines.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxReleases_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxReleases_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxReleases = _JuniDhcpLocalServerSubInterfaceRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 7),
    _JuniDhcpLocalServerSubInterfaceRxReleases_Type()
)
juniDhcpLocalServerSubInterfaceRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxReleases.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxInforms_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxInforms_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxInforms = _JuniDhcpLocalServerSubInterfaceRxInforms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 8),
    _JuniDhcpLocalServerSubInterfaceRxInforms_Type()
)
juniDhcpLocalServerSubInterfaceRxInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxInforms.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxOffers_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxOffers_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxOffers = _JuniDhcpLocalServerSubInterfaceTxOffers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 9),
    _JuniDhcpLocalServerSubInterfaceTxOffers_Type()
)
juniDhcpLocalServerSubInterfaceTxOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxOffers.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxAcks_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxAcks_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxAcks = _JuniDhcpLocalServerSubInterfaceTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 10),
    _JuniDhcpLocalServerSubInterfaceTxAcks_Type()
)
juniDhcpLocalServerSubInterfaceTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxAcks.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxNaks_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxNaks_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxNaks = _JuniDhcpLocalServerSubInterfaceTxNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 11),
    _JuniDhcpLocalServerSubInterfaceTxNaks_Type()
)
juniDhcpLocalServerSubInterfaceTxNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxNaks.setStatus("current")
_JuniDhcpLocalServerSubInterfaceUnknownMessages_Type = Counter32
_JuniDhcpLocalServerSubInterfaceUnknownMessages_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceUnknownMessages = _JuniDhcpLocalServerSubInterfaceUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 12),
    _JuniDhcpLocalServerSubInterfaceUnknownMessages_Type()
)
juniDhcpLocalServerSubInterfaceUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceUnknownMessages.setStatus("deprecated")
_JuniDhcpLocalServerSubInterfaceBadMessages_Type = Counter32
_JuniDhcpLocalServerSubInterfaceBadMessages_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceBadMessages = _JuniDhcpLocalServerSubInterfaceBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 13),
    _JuniDhcpLocalServerSubInterfaceBadMessages_Type()
)
juniDhcpLocalServerSubInterfaceBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceBadMessages.setStatus("deprecated")
_JuniDhcpLocalServerSubInterfacePacketsIn_Type = Counter32
_JuniDhcpLocalServerSubInterfacePacketsIn_Object = MibTableColumn
juniDhcpLocalServerSubInterfacePacketsIn = _JuniDhcpLocalServerSubInterfacePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 14),
    _JuniDhcpLocalServerSubInterfacePacketsIn_Type()
)
juniDhcpLocalServerSubInterfacePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfacePacketsIn.setStatus("current")
_JuniDhcpLocalServerSubInterfacePacketsOut_Type = Counter32
_JuniDhcpLocalServerSubInterfacePacketsOut_Object = MibTableColumn
juniDhcpLocalServerSubInterfacePacketsOut = _JuniDhcpLocalServerSubInterfacePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 15),
    _JuniDhcpLocalServerSubInterfacePacketsOut_Type()
)
juniDhcpLocalServerSubInterfacePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfacePacketsOut.setStatus("current")
_JuniDhcpLocalServerSubInterfaceClientCount_Type = Counter32
_JuniDhcpLocalServerSubInterfaceClientCount_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceClientCount = _JuniDhcpLocalServerSubInterfaceClientCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 16),
    _JuniDhcpLocalServerSubInterfaceClientCount_Type()
)
juniDhcpLocalServerSubInterfaceClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceClientCount.setStatus("current")
_JuniDhcpLocalServerSubInterfaceDeniedLogins_Type = Counter32
_JuniDhcpLocalServerSubInterfaceDeniedLogins_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceDeniedLogins = _JuniDhcpLocalServerSubInterfaceDeniedLogins_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 17),
    _JuniDhcpLocalServerSubInterfaceDeniedLogins_Type()
)
juniDhcpLocalServerSubInterfaceDeniedLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceDeniedLogins.setStatus("current")
_JuniDhcpLocalServerSubInterfaceDeniedTotal_Type = Counter32
_JuniDhcpLocalServerSubInterfaceDeniedTotal_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceDeniedTotal = _JuniDhcpLocalServerSubInterfaceDeniedTotal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 18),
    _JuniDhcpLocalServerSubInterfaceDeniedTotal_Type()
)
juniDhcpLocalServerSubInterfaceDeniedTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceDeniedTotal.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxRebinds_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxRebinds_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxRebinds = _JuniDhcpLocalServerSubInterfaceRxRebinds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 19),
    _JuniDhcpLocalServerSubInterfaceRxRebinds_Type()
)
juniDhcpLocalServerSubInterfaceRxRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxRebinds.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxUnknownClients_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxUnknownClients_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxUnknownClients = _JuniDhcpLocalServerSubInterfaceRxUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 20),
    _JuniDhcpLocalServerSubInterfaceRxUnknownClients_Type()
)
juniDhcpLocalServerSubInterfaceRxUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxUnknownClients.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxInErrors_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxInErrors_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxInErrors = _JuniDhcpLocalServerSubInterfaceRxInErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 21),
    _JuniDhcpLocalServerSubInterfaceRxInErrors_Type()
)
juniDhcpLocalServerSubInterfaceRxInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxInErrors.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxInDiscards_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxInDiscards_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxInDiscards = _JuniDhcpLocalServerSubInterfaceRxInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 22),
    _JuniDhcpLocalServerSubInterfaceRxInDiscards_Type()
)
juniDhcpLocalServerSubInterfaceRxInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxInDiscards.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxRenewAcks_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxRenewAcks_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxRenewAcks = _JuniDhcpLocalServerSubInterfaceTxRenewAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 23),
    _JuniDhcpLocalServerSubInterfaceTxRenewAcks_Type()
)
juniDhcpLocalServerSubInterfaceTxRenewAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxRenewAcks.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxRebindAcks_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxRebindAcks_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxRebindAcks = _JuniDhcpLocalServerSubInterfaceTxRebindAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 24),
    _JuniDhcpLocalServerSubInterfaceTxRebindAcks_Type()
)
juniDhcpLocalServerSubInterfaceTxRebindAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxRebindAcks.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxRenewNaks_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxRenewNaks_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxRenewNaks = _JuniDhcpLocalServerSubInterfaceTxRenewNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 25),
    _JuniDhcpLocalServerSubInterfaceTxRenewNaks_Type()
)
juniDhcpLocalServerSubInterfaceTxRenewNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxRenewNaks.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxRebindNaks_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxRebindNaks_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxRebindNaks = _JuniDhcpLocalServerSubInterfaceTxRebindNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 26),
    _JuniDhcpLocalServerSubInterfaceTxRebindNaks_Type()
)
juniDhcpLocalServerSubInterfaceTxRebindNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxRebindNaks.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxOutErrors_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxOutErrors_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxOutErrors = _JuniDhcpLocalServerSubInterfaceTxOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 27),
    _JuniDhcpLocalServerSubInterfaceTxOutErrors_Type()
)
juniDhcpLocalServerSubInterfaceTxOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxOutErrors.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTxOutDiscards_Type = Counter32
_JuniDhcpLocalServerSubInterfaceTxOutDiscards_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceTxOutDiscards = _JuniDhcpLocalServerSubInterfaceTxOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 28),
    _JuniDhcpLocalServerSubInterfaceTxOutDiscards_Type()
)
juniDhcpLocalServerSubInterfaceTxOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTxOutDiscards.setStatus("current")
_JuniDhcpLocalServerSubInterfaceRxOtherRequests_Type = Counter32
_JuniDhcpLocalServerSubInterfaceRxOtherRequests_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceRxOtherRequests = _JuniDhcpLocalServerSubInterfaceRxOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 30, 1, 29),
    _JuniDhcpLocalServerSubInterfaceRxOtherRequests_Type()
)
juniDhcpLocalServerSubInterfaceRxOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceRxOtherRequests.setStatus("current")
_JuniDhcpLocalServerBindings_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerBindings = _JuniDhcpLocalServerBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2)
)
_JuniDhcpLocalServerBindingsTable_Object = MibTable
juniDhcpLocalServerBindingsTable = _JuniDhcpLocalServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsTable.setStatus("current")
_JuniDhcpLocalServerBindingsEntry_Object = MibTableRow
juniDhcpLocalServerBindingsEntry = _JuniDhcpLocalServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1)
)
juniDhcpLocalServerBindingsEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsIpAddress"),
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsEntry.setStatus("current")
_JuniDhcpLocalServerBindingsIpAddress_Type = IpAddress
_JuniDhcpLocalServerBindingsIpAddress_Object = MibTableColumn
juniDhcpLocalServerBindingsIpAddress = _JuniDhcpLocalServerBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 1),
    _JuniDhcpLocalServerBindingsIpAddress_Type()
)
juniDhcpLocalServerBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsIpAddress.setStatus("current")


class _JuniDhcpLocalServerBindingsPhysAddress_Type(PhysAddress):
    """Custom type juniDhcpLocalServerBindingsPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_JuniDhcpLocalServerBindingsPhysAddress_Type.__name__ = "PhysAddress"
_JuniDhcpLocalServerBindingsPhysAddress_Object = MibTableColumn
juniDhcpLocalServerBindingsPhysAddress = _JuniDhcpLocalServerBindingsPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 2),
    _JuniDhcpLocalServerBindingsPhysAddress_Type()
)
juniDhcpLocalServerBindingsPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsPhysAddress.setStatus("current")
_JuniDhcpLocalServerBindingsInfinite_Type = TruthValue
_JuniDhcpLocalServerBindingsInfinite_Object = MibTableColumn
juniDhcpLocalServerBindingsInfinite = _JuniDhcpLocalServerBindingsInfinite_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 3),
    _JuniDhcpLocalServerBindingsInfinite_Type()
)
juniDhcpLocalServerBindingsInfinite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsInfinite.setStatus("current")
_JuniDhcpLocalServerBindingsExpireTime_Type = Unsigned32
_JuniDhcpLocalServerBindingsExpireTime_Object = MibTableColumn
juniDhcpLocalServerBindingsExpireTime = _JuniDhcpLocalServerBindingsExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 4),
    _JuniDhcpLocalServerBindingsExpireTime_Type()
)
juniDhcpLocalServerBindingsExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsExpireTime.setStatus("current")
_JuniDhcpLocalServerBindingsRowStatus_Type = RowStatus
_JuniDhcpLocalServerBindingsRowStatus_Object = MibTableColumn
juniDhcpLocalServerBindingsRowStatus = _JuniDhcpLocalServerBindingsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 5),
    _JuniDhcpLocalServerBindingsRowStatus_Type()
)
juniDhcpLocalServerBindingsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsRowStatus.setStatus("current")
_JuniDhcpLocalServerBindingsLeaseInterval_Type = Unsigned32
_JuniDhcpLocalServerBindingsLeaseInterval_Object = MibTableColumn
juniDhcpLocalServerBindingsLeaseInterval = _JuniDhcpLocalServerBindingsLeaseInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 6),
    _JuniDhcpLocalServerBindingsLeaseInterval_Type()
)
juniDhcpLocalServerBindingsLeaseInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsLeaseInterval.setStatus("current")


class _JuniDhcpLocalServerBindingsLeaseStartTime_Type(DateAndTime):
    """Custom type juniDhcpLocalServerBindingsLeaseStartTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniDhcpLocalServerBindingsLeaseStartTime_Type.__name__ = "DateAndTime"
_JuniDhcpLocalServerBindingsLeaseStartTime_Object = MibTableColumn
juniDhcpLocalServerBindingsLeaseStartTime = _JuniDhcpLocalServerBindingsLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 7),
    _JuniDhcpLocalServerBindingsLeaseStartTime_Type()
)
juniDhcpLocalServerBindingsLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsLeaseStartTime.setStatus("current")


class _JuniDhcpLocalServerBindingsInitialLeaseStartTime_Type(DateAndTime):
    """Custom type juniDhcpLocalServerBindingsInitialLeaseStartTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniDhcpLocalServerBindingsInitialLeaseStartTime_Type.__name__ = "DateAndTime"
_JuniDhcpLocalServerBindingsInitialLeaseStartTime_Object = MibTableColumn
juniDhcpLocalServerBindingsInitialLeaseStartTime = _JuniDhcpLocalServerBindingsInitialLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 8),
    _JuniDhcpLocalServerBindingsInitialLeaseStartTime_Type()
)
juniDhcpLocalServerBindingsInitialLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerBindingsInitialLeaseStartTime.setStatus("current")
_JuniDhcpLocalServerPool_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerPool = _JuniDhcpLocalServerPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3)
)
_JuniDhcpLocalServerPoolTable_Object = MibTable
juniDhcpLocalServerPoolTable = _JuniDhcpLocalServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolTable.setStatus("current")
_JuniDhcpLocalServerPoolEntry_Object = MibTableRow
juniDhcpLocalServerPoolEntry = _JuniDhcpLocalServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1)
)
juniDhcpLocalServerPoolEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpLocalServerPoolName"),
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolEntry.setStatus("current")
_JuniDhcpLocalServerPoolName_Type = JuniDhcpLocalServerPoolName
_JuniDhcpLocalServerPoolName_Object = MibTableColumn
juniDhcpLocalServerPoolName = _JuniDhcpLocalServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 1),
    _JuniDhcpLocalServerPoolName_Type()
)
juniDhcpLocalServerPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolName.setStatus("current")
_JuniDhcpLocalServerPoolDomainName_Type = JuniDhcpLocalServerPoolDomainName
_JuniDhcpLocalServerPoolDomainName_Object = MibTableColumn
juniDhcpLocalServerPoolDomainName = _JuniDhcpLocalServerPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 2),
    _JuniDhcpLocalServerPoolDomainName_Type()
)
juniDhcpLocalServerPoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolDomainName.setStatus("current")


class _JuniDhcpLocalServerPoolNetworkIpAddress_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolNetworkIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolNetworkIpAddress_Object = MibTableColumn
juniDhcpLocalServerPoolNetworkIpAddress = _JuniDhcpLocalServerPoolNetworkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 3),
    _JuniDhcpLocalServerPoolNetworkIpAddress_Type()
)
juniDhcpLocalServerPoolNetworkIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolNetworkIpAddress.setStatus("current")


class _JuniDhcpLocalServerPoolNetworkMask_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolNetworkMask based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolNetworkMask_Object = MibTableColumn
juniDhcpLocalServerPoolNetworkMask = _JuniDhcpLocalServerPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 4),
    _JuniDhcpLocalServerPoolNetworkMask_Type()
)
juniDhcpLocalServerPoolNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolNetworkMask.setStatus("current")


class _JuniDhcpLocalServerPoolNetBiosNodeType_Type(JuniDhcpLocalServerPoolNetBiosNodeType):
    """Custom type juniDhcpLocalServerPoolNetBiosNodeType based on JuniDhcpLocalServerPoolNetBiosNodeType"""


_JuniDhcpLocalServerPoolNetBiosNodeType_Object = MibTableColumn
juniDhcpLocalServerPoolNetBiosNodeType = _JuniDhcpLocalServerPoolNetBiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 5),
    _JuniDhcpLocalServerPoolNetBiosNodeType_Type()
)
juniDhcpLocalServerPoolNetBiosNodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolNetBiosNodeType.setStatus("current")
_JuniDhcpLocalServerPoolLeaseTime_Type = TimeInterval
_JuniDhcpLocalServerPoolLeaseTime_Object = MibTableColumn
juniDhcpLocalServerPoolLeaseTime = _JuniDhcpLocalServerPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 6),
    _JuniDhcpLocalServerPoolLeaseTime_Type()
)
juniDhcpLocalServerPoolLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolLeaseTime.setStatus("current")


class _JuniDhcpLocalServerPoolPrimaryDnsServer_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolPrimaryDnsServer based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolPrimaryDnsServer_Object = MibTableColumn
juniDhcpLocalServerPoolPrimaryDnsServer = _JuniDhcpLocalServerPoolPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 7),
    _JuniDhcpLocalServerPoolPrimaryDnsServer_Type()
)
juniDhcpLocalServerPoolPrimaryDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolPrimaryDnsServer.setStatus("current")


class _JuniDhcpLocalServerPoolSecondaryDnsServer_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolSecondaryDnsServer based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolSecondaryDnsServer_Object = MibTableColumn
juniDhcpLocalServerPoolSecondaryDnsServer = _JuniDhcpLocalServerPoolSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 8),
    _JuniDhcpLocalServerPoolSecondaryDnsServer_Type()
)
juniDhcpLocalServerPoolSecondaryDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolSecondaryDnsServer.setStatus("current")


class _JuniDhcpLocalServerPoolPrimaryNetBiosNameServer_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolPrimaryNetBiosNameServer based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolPrimaryNetBiosNameServer_Object = MibTableColumn
juniDhcpLocalServerPoolPrimaryNetBiosNameServer = _JuniDhcpLocalServerPoolPrimaryNetBiosNameServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 9),
    _JuniDhcpLocalServerPoolPrimaryNetBiosNameServer_Type()
)
juniDhcpLocalServerPoolPrimaryNetBiosNameServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolPrimaryNetBiosNameServer.setStatus("current")


class _JuniDhcpLocalServerPoolSecondaryNetBiosNameServer_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolSecondaryNetBiosNameServer based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolSecondaryNetBiosNameServer_Object = MibTableColumn
juniDhcpLocalServerPoolSecondaryNetBiosNameServer = _JuniDhcpLocalServerPoolSecondaryNetBiosNameServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 10),
    _JuniDhcpLocalServerPoolSecondaryNetBiosNameServer_Type()
)
juniDhcpLocalServerPoolSecondaryNetBiosNameServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolSecondaryNetBiosNameServer.setStatus("current")


class _JuniDhcpLocalServerPoolPrimaryDefaultRouter_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolPrimaryDefaultRouter based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolPrimaryDefaultRouter_Object = MibTableColumn
juniDhcpLocalServerPoolPrimaryDefaultRouter = _JuniDhcpLocalServerPoolPrimaryDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 11),
    _JuniDhcpLocalServerPoolPrimaryDefaultRouter_Type()
)
juniDhcpLocalServerPoolPrimaryDefaultRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolPrimaryDefaultRouter.setStatus("current")


class _JuniDhcpLocalServerPoolSecondaryDefaultRouter_Type(IpAddress):
    """Custom type juniDhcpLocalServerPoolSecondaryDefaultRouter based on IpAddress"""
    defaultHexValue = "00000000"


_JuniDhcpLocalServerPoolSecondaryDefaultRouter_Object = MibTableColumn
juniDhcpLocalServerPoolSecondaryDefaultRouter = _JuniDhcpLocalServerPoolSecondaryDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 12),
    _JuniDhcpLocalServerPoolSecondaryDefaultRouter_Type()
)
juniDhcpLocalServerPoolSecondaryDefaultRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolSecondaryDefaultRouter.setStatus("current")
_JuniDhcpLocalServerPoolRowStatus_Type = RowStatus
_JuniDhcpLocalServerPoolRowStatus_Object = MibTableColumn
juniDhcpLocalServerPoolRowStatus = _JuniDhcpLocalServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 13),
    _JuniDhcpLocalServerPoolRowStatus_Type()
)
juniDhcpLocalServerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolRowStatus.setStatus("current")
_JuniDhcpLocalServerPoolLinkName_Type = JuniDhcpLocalServerPoolName
_JuniDhcpLocalServerPoolLinkName_Object = MibTableColumn
juniDhcpLocalServerPoolLinkName = _JuniDhcpLocalServerPoolLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 14),
    _JuniDhcpLocalServerPoolLinkName_Type()
)
juniDhcpLocalServerPoolLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolLinkName.setStatus("current")


class _JuniDhcpLocalServerPoolHighUtilThreshold_Type(Integer32):
    """Custom type juniDhcpLocalServerPoolHighUtilThreshold based on Integer32"""
    defaultValue = 85

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JuniDhcpLocalServerPoolHighUtilThreshold_Type.__name__ = "Integer32"
_JuniDhcpLocalServerPoolHighUtilThreshold_Object = MibTableColumn
juniDhcpLocalServerPoolHighUtilThreshold = _JuniDhcpLocalServerPoolHighUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 15),
    _JuniDhcpLocalServerPoolHighUtilThreshold_Type()
)
juniDhcpLocalServerPoolHighUtilThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolHighUtilThreshold.setStatus("current")


class _JuniDhcpLocalServerPoolAbatedUtilThreshold_Type(Integer32):
    """Custom type juniDhcpLocalServerPoolAbatedUtilThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_JuniDhcpLocalServerPoolAbatedUtilThreshold_Type.__name__ = "Integer32"
_JuniDhcpLocalServerPoolAbatedUtilThreshold_Object = MibTableColumn
juniDhcpLocalServerPoolAbatedUtilThreshold = _JuniDhcpLocalServerPoolAbatedUtilThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 16),
    _JuniDhcpLocalServerPoolAbatedUtilThreshold_Type()
)
juniDhcpLocalServerPoolAbatedUtilThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolAbatedUtilThreshold.setStatus("current")


class _JuniDhcpLocalServerPoolUtilPct_Type(Integer32):
    """Custom type juniDhcpLocalServerPoolUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniDhcpLocalServerPoolUtilPct_Type.__name__ = "Integer32"
_JuniDhcpLocalServerPoolUtilPct_Object = MibTableColumn
juniDhcpLocalServerPoolUtilPct = _JuniDhcpLocalServerPoolUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 17),
    _JuniDhcpLocalServerPoolUtilPct_Type()
)
juniDhcpLocalServerPoolUtilPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolUtilPct.setStatus("current")


class _JuniDhcpLocalServerPoolTrapEnable_Type(TruthValue):
    """Custom type juniDhcpLocalServerPoolTrapEnable based on TruthValue"""


_JuniDhcpLocalServerPoolTrapEnable_Object = MibTableColumn
juniDhcpLocalServerPoolTrapEnable = _JuniDhcpLocalServerPoolTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 18),
    _JuniDhcpLocalServerPoolTrapEnable_Type()
)
juniDhcpLocalServerPoolTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolTrapEnable.setStatus("current")


class _JuniDhcpLocalServerPoolInUse_Type(Integer32):
    """Custom type juniDhcpLocalServerPoolInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniDhcpLocalServerPoolInUse_Type.__name__ = "Integer32"
_JuniDhcpLocalServerPoolInUse_Object = MibTableColumn
juniDhcpLocalServerPoolInUse = _JuniDhcpLocalServerPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 19),
    _JuniDhcpLocalServerPoolInUse_Type()
)
juniDhcpLocalServerPoolInUse.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolInUse.setStatus("current")


class _JuniDhcpLocalServerPoolSize_Type(Integer32):
    """Custom type juniDhcpLocalServerPoolSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniDhcpLocalServerPoolSize_Type.__name__ = "Integer32"
_JuniDhcpLocalServerPoolSize_Object = MibTableColumn
juniDhcpLocalServerPoolSize = _JuniDhcpLocalServerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 20),
    _JuniDhcpLocalServerPoolSize_Type()
)
juniDhcpLocalServerPoolSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolSize.setStatus("current")
_JuniDhcpLocalServerPoolSharedInUse_Type = Integer32
_JuniDhcpLocalServerPoolSharedInUse_Object = MibTableColumn
juniDhcpLocalServerPoolSharedInUse = _JuniDhcpLocalServerPoolSharedInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 21),
    _JuniDhcpLocalServerPoolSharedInUse_Type()
)
juniDhcpLocalServerPoolSharedInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolSharedInUse.setStatus("current")
_JuniDhcpLocalServerAttributes_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerAttributes = _JuniDhcpLocalServerAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4)
)
_JuniDhcpLocalServerAttributesMode_Type = JuniDhcpLocalServerModeType
_JuniDhcpLocalServerAttributesMode_Object = MibScalar
juniDhcpLocalServerAttributesMode = _JuniDhcpLocalServerAttributesMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 1),
    _JuniDhcpLocalServerAttributesMode_Type()
)
juniDhcpLocalServerAttributesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerAttributesMode.setStatus("current")
_JuniDhcpLocalServerSubInterfaceTable_Object = MibTable
juniDhcpLocalServerSubInterfaceTable = _JuniDhcpLocalServerSubInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceTable.setStatus("current")
_JuniDhcpLocalServerSubInterfaceEntry_Object = MibTableRow
juniDhcpLocalServerSubInterfaceEntry = _JuniDhcpLocalServerSubInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 2, 1)
)
juniDhcpLocalServerSubInterfaceEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceIndex"),
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceEntry.setStatus("current")
_JuniDhcpLocalServerSubInterfaceIndex_Type = InterfaceIndex
_JuniDhcpLocalServerSubInterfaceIndex_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceIndex = _JuniDhcpLocalServerSubInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 2, 1, 1),
    _JuniDhcpLocalServerSubInterfaceIndex_Type()
)
juniDhcpLocalServerSubInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceIndex.setStatus("current")


class _JuniDhcpLocalServerSubInterfaceName_Type(DisplayString):
    """Custom type juniDhcpLocalServerSubInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_JuniDhcpLocalServerSubInterfaceName_Type.__name__ = "DisplayString"
_JuniDhcpLocalServerSubInterfaceName_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceName = _JuniDhcpLocalServerSubInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 2, 1, 2),
    _JuniDhcpLocalServerSubInterfaceName_Type()
)
juniDhcpLocalServerSubInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceName.setStatus("current")
_JuniDhcpLocalServerSubInterfaceLimit_Type = Integer32
_JuniDhcpLocalServerSubInterfaceLimit_Object = MibTableColumn
juniDhcpLocalServerSubInterfaceLimit = _JuniDhcpLocalServerSubInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 2, 1, 3),
    _JuniDhcpLocalServerSubInterfaceLimit_Type()
)
juniDhcpLocalServerSubInterfaceLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSubInterfaceLimit.setStatus("current")


class _JuniDhcpLocalServerSnmpTrap_Type(JuniEnable):
    """Custom type juniDhcpLocalServerSnmpTrap based on JuniEnable"""


_JuniDhcpLocalServerSnmpTrap_Object = MibScalar
juniDhcpLocalServerSnmpTrap = _JuniDhcpLocalServerSnmpTrap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 3),
    _JuniDhcpLocalServerSnmpTrap_Type()
)
juniDhcpLocalServerSnmpTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpLocalServerSnmpTrap.setStatus("current")


class _JuniDhcpLocalServerInhibitRoaming_Type(JuniEnable):
    """Custom type juniDhcpLocalServerInhibitRoaming based on JuniEnable"""


_JuniDhcpLocalServerInhibitRoaming_Object = MibScalar
juniDhcpLocalServerInhibitRoaming = _JuniDhcpLocalServerInhibitRoaming_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 4),
    _JuniDhcpLocalServerInhibitRoaming_Type()
)
juniDhcpLocalServerInhibitRoaming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpLocalServerInhibitRoaming.setStatus("obsolete")


class _JuniDhcpLocalServerUniqueClientIds_Type(JuniEnable):
    """Custom type juniDhcpLocalServerUniqueClientIds based on JuniEnable"""


_JuniDhcpLocalServerUniqueClientIds_Object = MibScalar
juniDhcpLocalServerUniqueClientIds = _JuniDhcpLocalServerUniqueClientIds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 5),
    _JuniDhcpLocalServerUniqueClientIds_Type()
)
juniDhcpLocalServerUniqueClientIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDhcpLocalServerUniqueClientIds.setStatus("current")
_JuniDhcpLocalServerReserves_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerReserves = _JuniDhcpLocalServerReserves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5)
)
_JuniDhcpLocalServerReservesTable_Object = MibTable
juniDhcpLocalServerReservesTable = _JuniDhcpLocalServerReservesTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerReservesTable.setStatus("current")
_JuniDhcpLocalServerReservesEntry_Object = MibTableRow
juniDhcpLocalServerReservesEntry = _JuniDhcpLocalServerReservesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1)
)
juniDhcpLocalServerReservesEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryIpAddress"),
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerReservesEntry.setStatus("current")
_JuniDhcpLocalServerReservesEntryIpAddress_Type = IpAddress
_JuniDhcpLocalServerReservesEntryIpAddress_Object = MibTableColumn
juniDhcpLocalServerReservesEntryIpAddress = _JuniDhcpLocalServerReservesEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 1),
    _JuniDhcpLocalServerReservesEntryIpAddress_Type()
)
juniDhcpLocalServerReservesEntryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpLocalServerReservesEntryIpAddress.setStatus("current")
_JuniDhcpLocalServerReservesEntryPoolName_Type = JuniDhcpLocalServerPoolName
_JuniDhcpLocalServerReservesEntryPoolName_Object = MibTableColumn
juniDhcpLocalServerReservesEntryPoolName = _JuniDhcpLocalServerReservesEntryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 2),
    _JuniDhcpLocalServerReservesEntryPoolName_Type()
)
juniDhcpLocalServerReservesEntryPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerReservesEntryPoolName.setStatus("current")
_JuniDhcpLocalServerReservesEntryPhysAddress_Type = JuniDhcpLocalServerPhysAddressString
_JuniDhcpLocalServerReservesEntryPhysAddress_Object = MibTableColumn
juniDhcpLocalServerReservesEntryPhysAddress = _JuniDhcpLocalServerReservesEntryPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 3),
    _JuniDhcpLocalServerReservesEntryPhysAddress_Type()
)
juniDhcpLocalServerReservesEntryPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerReservesEntryPhysAddress.setStatus("current")
_JuniDhcpLocalServerReservesEntryRowStatus_Type = RowStatus
_JuniDhcpLocalServerReservesEntryRowStatus_Object = MibTableColumn
juniDhcpLocalServerReservesEntryRowStatus = _JuniDhcpLocalServerReservesEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 4),
    _JuniDhcpLocalServerReservesEntryRowStatus_Type()
)
juniDhcpLocalServerReservesEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerReservesEntryRowStatus.setStatus("current")
_JuniDhcpLocalServerCableModemServers_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerCableModemServers = _JuniDhcpLocalServerCableModemServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6)
)
_JuniDhcpLocalServerCableModemServerTable_Object = MibTable
juniDhcpLocalServerCableModemServerTable = _JuniDhcpLocalServerCableModemServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemServerTable.setStatus("obsolete")
_JuniDhcpLocalServerCableModemServerEntry_Object = MibTableRow
juniDhcpLocalServerCableModemServerEntry = _JuniDhcpLocalServerCableModemServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1, 1)
)
juniDhcpLocalServerCableModemServerEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemServerEntryAddress"),
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemServerEntry.setStatus("obsolete")
_JuniDhcpLocalServerCableModemServerEntryAddress_Type = IpAddress
_JuniDhcpLocalServerCableModemServerEntryAddress_Object = MibTableColumn
juniDhcpLocalServerCableModemServerEntryAddress = _JuniDhcpLocalServerCableModemServerEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1, 1, 1),
    _JuniDhcpLocalServerCableModemServerEntryAddress_Type()
)
juniDhcpLocalServerCableModemServerEntryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemServerEntryAddress.setStatus("obsolete")
_JuniDhcpLocalServerCableModemServerEntryRowStatus_Type = RowStatus
_JuniDhcpLocalServerCableModemServerEntryRowStatus_Object = MibTableColumn
juniDhcpLocalServerCableModemServerEntryRowStatus = _JuniDhcpLocalServerCableModemServerEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1, 1, 2),
    _JuniDhcpLocalServerCableModemServerEntryRowStatus_Type()
)
juniDhcpLocalServerCableModemServerEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemServerEntryRowStatus.setStatus("obsolete")
_JuniDhcpLocalServerCableModemStatistics_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerCableModemStatistics = _JuniDhcpLocalServerCableModemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7)
)
_JuniDhcpLocalServerCableModemRequestIn_Type = Counter32
_JuniDhcpLocalServerCableModemRequestIn_Object = MibScalar
juniDhcpLocalServerCableModemRequestIn = _JuniDhcpLocalServerCableModemRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 1),
    _JuniDhcpLocalServerCableModemRequestIn_Type()
)
juniDhcpLocalServerCableModemRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemRequestIn.setStatus("obsolete")
_JuniDhcpLocalServerCableModemResponseIn_Type = Counter32
_JuniDhcpLocalServerCableModemResponseIn_Object = MibScalar
juniDhcpLocalServerCableModemResponseIn = _JuniDhcpLocalServerCableModemResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 2),
    _JuniDhcpLocalServerCableModemResponseIn_Type()
)
juniDhcpLocalServerCableModemResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemResponseIn.setStatus("obsolete")
_JuniDhcpLocalServerCableModemRequestOut_Type = Counter32
_JuniDhcpLocalServerCableModemRequestOut_Object = MibScalar
juniDhcpLocalServerCableModemRequestOut = _JuniDhcpLocalServerCableModemRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 3),
    _JuniDhcpLocalServerCableModemRequestOut_Type()
)
juniDhcpLocalServerCableModemRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemRequestOut.setStatus("obsolete")
_JuniDhcpLocalServerCableModemResponseOut_Type = Counter32
_JuniDhcpLocalServerCableModemResponseOut_Object = MibScalar
juniDhcpLocalServerCableModemResponseOut = _JuniDhcpLocalServerCableModemResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 4),
    _JuniDhcpLocalServerCableModemResponseOut_Type()
)
juniDhcpLocalServerCableModemResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemResponseOut.setStatus("obsolete")
_JuniDhcpLocalServerCableModemRequestDropped_Type = Counter32
_JuniDhcpLocalServerCableModemRequestDropped_Object = MibScalar
juniDhcpLocalServerCableModemRequestDropped = _JuniDhcpLocalServerCableModemRequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 5),
    _JuniDhcpLocalServerCableModemRequestDropped_Type()
)
juniDhcpLocalServerCableModemRequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemRequestDropped.setStatus("obsolete")
_JuniDhcpLocalServerCableModemResponseDropped_Type = Counter32
_JuniDhcpLocalServerCableModemResponseDropped_Object = MibScalar
juniDhcpLocalServerCableModemResponseDropped = _JuniDhcpLocalServerCableModemResponseDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 6),
    _JuniDhcpLocalServerCableModemResponseDropped_Type()
)
juniDhcpLocalServerCableModemResponseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemResponseDropped.setStatus("obsolete")
_JuniDhcpLocalServerCableModemRequestBad_Type = Counter32
_JuniDhcpLocalServerCableModemRequestBad_Object = MibScalar
juniDhcpLocalServerCableModemRequestBad = _JuniDhcpLocalServerCableModemRequestBad_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 7),
    _JuniDhcpLocalServerCableModemRequestBad_Type()
)
juniDhcpLocalServerCableModemRequestBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemRequestBad.setStatus("obsolete")
_JuniDhcpLocalServerCableModemResponseBad_Type = Counter32
_JuniDhcpLocalServerCableModemResponseBad_Object = MibScalar
juniDhcpLocalServerCableModemResponseBad = _JuniDhcpLocalServerCableModemResponseBad_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 8),
    _JuniDhcpLocalServerCableModemResponseBad_Type()
)
juniDhcpLocalServerCableModemResponseBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemResponseBad.setStatus("obsolete")
_JuniDhcpLocalServerCableModemRequestDeleted_Type = Counter32
_JuniDhcpLocalServerCableModemRequestDeleted_Object = MibScalar
juniDhcpLocalServerCableModemRequestDeleted = _JuniDhcpLocalServerCableModemRequestDeleted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 9),
    _JuniDhcpLocalServerCableModemRequestDeleted_Type()
)
juniDhcpLocalServerCableModemRequestDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemRequestDeleted.setStatus("obsolete")
_JuniDhcpLocalServerCableModemPacketsIn_Type = Counter32
_JuniDhcpLocalServerCableModemPacketsIn_Object = MibScalar
juniDhcpLocalServerCableModemPacketsIn = _JuniDhcpLocalServerCableModemPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 10),
    _JuniDhcpLocalServerCableModemPacketsIn_Type()
)
juniDhcpLocalServerCableModemPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemPacketsIn.setStatus("obsolete")
_JuniDhcpLocalServerCableModemPacketsOut_Type = Counter32
_JuniDhcpLocalServerCableModemPacketsOut_Object = MibScalar
juniDhcpLocalServerCableModemPacketsOut = _JuniDhcpLocalServerCableModemPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 11),
    _JuniDhcpLocalServerCableModemPacketsOut_Type()
)
juniDhcpLocalServerCableModemPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemPacketsOut.setStatus("obsolete")
_JuniDhcpLocalServerCableModemPacketsDropped_Type = Counter32
_JuniDhcpLocalServerCableModemPacketsDropped_Object = MibScalar
juniDhcpLocalServerCableModemPacketsDropped = _JuniDhcpLocalServerCableModemPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 12),
    _JuniDhcpLocalServerCableModemPacketsDropped_Type()
)
juniDhcpLocalServerCableModemPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDhcpLocalServerCableModemPacketsDropped.setStatus("obsolete")
_JuniDhcpLocalServerPoolGroup_ObjectIdentity = ObjectIdentity
juniDhcpLocalServerPoolGroup = _JuniDhcpLocalServerPoolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 8)
)
_JuniDhcpLocalServerPoolGroupTable_Object = MibTable
juniDhcpLocalServerPoolGroupTable = _JuniDhcpLocalServerPoolGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 8, 1)
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupTable.setStatus("current")
_JuniDhcpLocalServerPoolGroupEntry_Object = MibTableRow
juniDhcpLocalServerPoolGroupEntry = _JuniDhcpLocalServerPoolGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 8, 1, 1)
)
juniDhcpLocalServerPoolGroupEntry.setIndexNames(
    (0, "Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupName"),
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupEntry.setStatus("current")
_JuniDhcpLocalServerPoolGroupName_Type = JuniDhcpLocalServerPoolGroupName
_JuniDhcpLocalServerPoolGroupName_Object = MibTableColumn
juniDhcpLocalServerPoolGroupName = _JuniDhcpLocalServerPoolGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 8, 1, 1, 1),
    _JuniDhcpLocalServerPoolGroupName_Type()
)
juniDhcpLocalServerPoolGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupName.setStatus("current")
_JuniDhcpLocalServerPoolGroupSize_Type = Integer32
_JuniDhcpLocalServerPoolGroupSize_Object = MibTableColumn
juniDhcpLocalServerPoolGroupSize = _JuniDhcpLocalServerPoolGroupSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 8, 1, 1, 2),
    _JuniDhcpLocalServerPoolGroupSize_Type()
)
juniDhcpLocalServerPoolGroupSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupSize.setStatus("current")
_JuniDhcpLocalServerPoolGroupInUse_Type = Integer32
_JuniDhcpLocalServerPoolGroupInUse_Object = MibTableColumn
juniDhcpLocalServerPoolGroupInUse = _JuniDhcpLocalServerPoolGroupInUse_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 8, 1, 1, 3),
    _JuniDhcpLocalServerPoolGroupInUse_Type()
)
juniDhcpLocalServerPoolGroupInUse.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupInUse.setStatus("current")


class _JuniDhcpLocalServerPoolGroupUtilPct_Type(Integer32):
    """Custom type juniDhcpLocalServerPoolGroupUtilPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_JuniDhcpLocalServerPoolGroupUtilPct_Type.__name__ = "Integer32"
_JuniDhcpLocalServerPoolGroupUtilPct_Object = MibTableColumn
juniDhcpLocalServerPoolGroupUtilPct = _JuniDhcpLocalServerPoolGroupUtilPct_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 8, 1, 1, 4),
    _JuniDhcpLocalServerPoolGroupUtilPct_Type()
)
juniDhcpLocalServerPoolGroupUtilPct.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupUtilPct.setStatus("current")
_JuniDhcpTrapControl_ObjectIdentity = ObjectIdentity
juniDhcpTrapControl = _JuniDhcpTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 2)
)
_JuniDhcpLocalServerEventSeverity_Type = JuniLogSeverity
_JuniDhcpLocalServerEventSeverity_Object = MibScalar
juniDhcpLocalServerEventSeverity = _JuniDhcpLocalServerEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 2, 1),
    _JuniDhcpLocalServerEventSeverity_Type()
)
juniDhcpLocalServerEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerEventSeverity.setStatus("current")
_JuniDhcpLocalServerEventString_Type = DisplayString
_JuniDhcpLocalServerEventString_Object = MibScalar
juniDhcpLocalServerEventString = _JuniDhcpLocalServerEventString_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 2, 2),
    _JuniDhcpLocalServerEventString_Type()
)
juniDhcpLocalServerEventString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerEventString.setStatus("current")
_JuniDhcpLocalServerMacAddress_Type = JuniDhcpLocalServerPhysAddressString
_JuniDhcpLocalServerMacAddress_Object = MibScalar
juniDhcpLocalServerMacAddress = _JuniDhcpLocalServerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 2, 3),
    _JuniDhcpLocalServerMacAddress_Type()
)
juniDhcpLocalServerMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerMacAddress.setStatus("current")
_JuniDhcpLocalServerInterfaceString_Type = DisplayString
_JuniDhcpLocalServerInterfaceString_Object = MibScalar
juniDhcpLocalServerInterfaceString = _JuniDhcpLocalServerInterfaceString_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 2, 4),
    _JuniDhcpLocalServerInterfaceString_Type()
)
juniDhcpLocalServerInterfaceString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerInterfaceString.setStatus("current")
_JuniDhcpLocalServerLastDetected_Type = DisplayString
_JuniDhcpLocalServerLastDetected_Object = MibScalar
juniDhcpLocalServerLastDetected = _JuniDhcpLocalServerLastDetected_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 2, 5),
    _JuniDhcpLocalServerLastDetected_Type()
)
juniDhcpLocalServerLastDetected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniDhcpLocalServerLastDetected.setStatus("current")
_JuniDhcpMIBConformance_ObjectIdentity = ObjectIdentity
juniDhcpMIBConformance = _JuniDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4)
)
_JuniDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
juniDhcpMIBCompliances = _JuniDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1)
)
_JuniDhcpMIBGroups_ObjectIdentity = ObjectIdentity
juniDhcpMIBGroups = _JuniDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2)
)

# Managed Objects groups

juniDhcpRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 1)
)
juniDhcpRelayGroup.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup.setStatus("obsolete")

juniDhcpProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 2)
)
juniDhcpProxyGroup.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpProxyClientUnknownServers"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerAdminStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerOperStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerLeases"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerRequests"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpProxyClientServerUnknownMessages"))
)
if mibBuilder.loadTexts:
    juniDhcpProxyGroup.setStatus("current")

juniDhcpLocalServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 3)
)
juniDhcpLocalServerGroup.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup.setStatus("obsolete")

juniDhcpLocalServerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 4)
)
juniDhcpLocalServerGroup2.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLinkName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerAttributesMode"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPoolName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemServerEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDeleted"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsDropped"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup2.setStatus("obsolete")

juniDhcpRelayGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 5)
)
juniDhcpRelayGroup2.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup2.setStatus("obsolete")

juniDhcpRelayGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 6)
)
juniDhcpRelayGroup3.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup3.setStatus("obsolete")

juniDhcpRelayGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 7)
)
juniDhcpRelayGroup4.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentExcludeSubIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup4.setStatus("obsolete")

juniDhcpRelayDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 8)
)
juniDhcpRelayDeprecatedGroup.setObjects(
    ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoEnable")
)
if mibBuilder.loadTexts:
    juniDhcpRelayDeprecatedGroup.setStatus("deprecated")

juniDhcpLocalServerGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 9)
)
juniDhcpLocalServerGroup3.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLinkName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolTrapEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerAttributesMode"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPoolName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemServerEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDeleted"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsDropped"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup3.setStatus("obsolete")

juniDhcpLocalServerGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 11)
)
juniDhcpLocalServerGroup4.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLinkName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolTrapEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerAttributesMode"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPoolName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemServerEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDeleted"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup4.setStatus("obsolete")

juniDhcpRelayGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 12)
)
juniDhcpRelayGroup5.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentExcludeSubIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentTrustAllEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresentForwards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup5.setStatus("obsolete")

juniDhcpLocalServerGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 13)
)
juniDhcpLocalServerGroup5.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseInterval"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInitialLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLinkName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolTrapEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSharedInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerAttributesMode"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSnmpTrap"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInhibitRoaming"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPoolName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemServerEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDeleted"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup5.setStatus("obsolete")

juniDhcpLocalServerGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 14)
)
juniDhcpLocalServerGroup6.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRebinds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxUnknownClients"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRenewAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRebindAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRenewNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRebindNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOutErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOutDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxOtherRequests"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseInterval"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInitialLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLinkName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolTrapEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSharedInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerAttributesMode"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSnmpTrap"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInhibitRoaming"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPoolName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemServerEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDeleted"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceLimit"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceClientCount"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceDeniedLogins"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceDeniedTotal"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRebinds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxUnknownClients"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRenewAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRebindAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRenewNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRebindNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOutErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOutDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxOtherRequests"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup6.setStatus("obsolete")

juniDhcpRelayGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 17)
)
juniDhcpRelayGroup6.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentExcludeSubIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentTrustAllEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresentForwards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentGiaddrOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentOptionOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDiscoverDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownRequestMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownReplyMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDuplicateRequestDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsTransmitted"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsReceived"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownXidDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDroppedStaleRequestDiscards"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup6.setStatus("obsolete")

juniDhcpRelayGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 18)
)
juniDhcpRelayGroup7.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentExcludeSubIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentTrustAllEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresentForwards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayLayer2UnicastReplies"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup7.setStatus("obsolete")

juniDhcpRelayGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 19)
)
juniDhcpRelayGroup8.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentExcludeSubIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentTrustAllEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresentForwards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentGiaddrOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentOptionOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDiscoverDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownRequestMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownReplyMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDuplicateRequestDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsTransmitted"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsReceived"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownXidDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDroppedStaleRequestDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayLayer2UnicastReplies"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup8.setStatus("obsolete")

juniDhcpRelayGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 20)
)
juniDhcpRelayGroup9.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentExcludeSubIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentTrustAllEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresentForwards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentGiaddrOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentOptionOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDiscoverDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownRequestMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownReplyMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDuplicateRequestDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsTransmitted"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsReceived"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownXidDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDroppedStaleRequestDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayLayer2UnicastReplies"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGiaddrSelectsInterface"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVendorSpecificSuboption"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup9.setStatus("obsolete")

juniDhcpLocalServerGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 21)
)
juniDhcpLocalServerGroup7.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRebinds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxUnknownClients"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRenewAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRebindAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRenewNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRebindNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOutErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOutDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxOtherRequests"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseInterval"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInitialLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLinkName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolTrapEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSharedInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerAttributesMode"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSnmpTrap"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInhibitRoaming"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUniqueClientIds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPoolName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemServerEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemResponseBad"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemRequestDeleted"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerCableModemPacketsDropped"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceLimit"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceClientCount"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceDeniedLogins"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceDeniedTotal"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRebinds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxUnknownClients"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRenewAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRebindAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRenewNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRebindNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOutErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOutDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxOtherRequests"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup7.setStatus("obsolete")

juniDhcpRelayGroup10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 22)
)
juniDhcpRelayGroup10.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpRelayBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresents"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGatewayAddrSpoofs"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentCircuitIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentRemoteIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentHostnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVrnameEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentExcludeSubIdEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentTrustAllEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentInfoAlreadyPresentForwards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayServerRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentGiaddrOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentOptionOverrides"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDiscoverDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownRequestMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownReplyMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDuplicateRequestDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsTransmitted"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayPacketsReceived"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayUnknownXidDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayDroppedStaleRequestDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayLayer2UnicastReplies"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayGiaddrSelectsInterface"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayAgentVendorSpecificSuboption"),
        ("Juniper-DHCP-MIB", "juniDhcpRelayBroadcastFlagReplies"))
)
if mibBuilder.loadTexts:
    juniDhcpRelayGroup10.setStatus("current")

juniDhcpLocalServerGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 23)
)
juniDhcpLocalServerGroup8.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxAccepts"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxRebinds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxUnknownClients"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxInDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRenewAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRebindAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRenewNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxRebindNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOutErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerTxOutDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerRxOtherRequests"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInfinite"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsExpireTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseInterval"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerBindingsInitialLeaseStartTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolDomainName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkIpAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetworkMask"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNetBiosNodeType"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLeaseTime"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDnsServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolLinkName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedUtilThreshold"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolTrapEnable"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSharedInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerAttributesMode"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSnmpTrap"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInhibitRoaming"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerUniqueClientIds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPoolName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryPhysAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerReservesEntryRowStatus"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceMemUsage"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceNumBindings"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDiscovers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRenews"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxDeclines"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxReleases"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInforms"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOffers"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceUnknownMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceBadMessages"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsIn"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceLimit"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceClientCount"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceDeniedLogins"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceDeniedTotal"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfacePacketsOut"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxRebinds"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxUnknownClients"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxInDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRenewAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRebindAcks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRenewNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxRebindNaks"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOutErrors"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceTxOutDiscards"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceRxOtherRequests"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerGroup8.setStatus("current")


# Notification objects

juniDhcpLocalServerPoolHighAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 1)
)
juniDhcpLocalServerPoolHighAddrUtil.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolHighAddrUtil.setStatus(
        "current"
    )

juniDhcpLocalServerPoolAbatedAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 2)
)
juniDhcpLocalServerPoolAbatedAddrUtil.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolUtilPct"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolAbatedAddrUtil.setStatus(
        "current"
    )

juniDhcpLocalServerPoolNoAddresses = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 3)
)
juniDhcpLocalServerPoolNoAddresses.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolSize"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolNoAddresses.setStatus(
        "current"
    )

juniDhcpLocalServerHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 4)
)
juniDhcpLocalServerHealth.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerEventSeverity"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerEventString"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerHealth.setStatus(
        "current"
    )

juniDhcpLocalServerPoolGroupHighAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 5)
)
juniDhcpLocalServerPoolGroupHighAddrUtil.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupUtilPct"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupHighAddrUtil.setStatus(
        "current"
    )

juniDhcpLocalServerPoolGroupAbatedAddrUtil = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 6)
)
juniDhcpLocalServerPoolGroupAbatedAddrUtil.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupSize"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupInUse"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupUtilPct"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupAbatedAddrUtil.setStatus(
        "current"
    )

juniDhcpLocalServerPoolGroupNoAddresses = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 7)
)
juniDhcpLocalServerPoolGroupNoAddresses.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupSize"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolGroupNoAddresses.setStatus(
        "current"
    )

juniDhcpLocalServerInterfaceLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 8)
)
juniDhcpLocalServerInterfaceLimitExceeded.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceLimit"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerInterfaceLimitExceeded.setStatus(
        "current"
    )

juniDhcpLocalServerInterfaceLimitAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 9)
)
juniDhcpLocalServerInterfaceLimitAbated.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerSubInterfaceLimit"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerInterfaceLimitAbated.setStatus(
        "current"
    )

juniDhcpLocalServerDuplicateClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 0, 10)
)
juniDhcpLocalServerDuplicateClient.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerMacAddress"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInterfaceString"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerLastDetected"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerDuplicateClient.setStatus(
        "current"
    )


# Notifications groups

juniDhcpLocalServerPoolTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 10)
)
juniDhcpLocalServerPoolTrapGroup.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNoAddresses"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerHealth"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolTrapGroup.setStatus(
        "obsolete"
    )

juniDhcpLocalServerPoolTrapGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 15)
)
juniDhcpLocalServerPoolTrapGroup2.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNoAddresses"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerHealth"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupHighAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupAbatedAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupNoAddresses"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInterfaceLimitExceeded"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInterfaceLimitAbated"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerDuplicateClient"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerPoolTrapGroup2.setStatus(
        "obsolete"
    )

juniDhcpLocalServerTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 16)
)
juniDhcpLocalServerTrapGroup.setObjects(
      *(("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolHighAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolAbatedAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolNoAddresses"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerHealth"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupHighAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupAbatedAddrUtil"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerPoolGroupNoAddresses"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInterfaceLimitExceeded"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerInterfaceLimitAbated"),
        ("Juniper-DHCP-MIB", "juniDhcpLocalServerDuplicateClient"))
)
if mibBuilder.loadTexts:
    juniDhcpLocalServerTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniDhcpRelayCompliance.setStatus(
        "obsolete"
    )

juniDhcpProxyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniDhcpProxyCompliance.setStatus(
        "obsolete"
    )

juniDhcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance.setStatus(
        "obsolete"
    )

juniDhcpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance2.setStatus(
        "obsolete"
    )

juniDhcpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance3.setStatus(
        "obsolete"
    )

juniDhcpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance4.setStatus(
        "obsolete"
    )

juniDhcpCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance5.setStatus(
        "obsolete"
    )

juniDhcpCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance6.setStatus(
        "obsolete"
    )

juniDhcpCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 9)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance7.setStatus(
        "obsolete"
    )

juniDhcpCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 10)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance8.setStatus(
        "obsolete"
    )

juniDhcpCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 11)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance9.setStatus(
        "obsolete"
    )

juniDhcpCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 12)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance10.setStatus(
        "obsolete"
    )

juniDhcpCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 13)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance11.setStatus(
        "obsolete"
    )

juniDhcpCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 14)
)
if mibBuilder.loadTexts:
    juniDhcpCompliance12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DHCP-MIB",
    **{"JuniDhcpLocalServerPoolName": JuniDhcpLocalServerPoolName,
       "JuniDhcpLocalServerPoolGroupName": JuniDhcpLocalServerPoolGroupName,
       "JuniDhcpLocalServerPoolDomainName": JuniDhcpLocalServerPoolDomainName,
       "JuniDhcpLocalServerPoolNetBiosNodeType": JuniDhcpLocalServerPoolNetBiosNodeType,
       "JuniDhcpLocalServerModeType": JuniDhcpLocalServerModeType,
       "JuniDhcpLocalServerPhysAddressString": JuniDhcpLocalServerPhysAddressString,
       "juniDhcpMIB": juniDhcpMIB,
       "juniDhcpObjects": juniDhcpObjects,
       "juniDhcpRelay": juniDhcpRelay,
       "juniDhcpLocalServerRelayTraps": juniDhcpLocalServerRelayTraps,
       "juniDhcpRelayScalars": juniDhcpRelayScalars,
       "juniDhcpRelayAgentInfoEnable": juniDhcpRelayAgentInfoEnable,
       "juniDhcpRelayBadMessages": juniDhcpRelayBadMessages,
       "juniDhcpRelayUnknownMessages": juniDhcpRelayUnknownMessages,
       "juniDhcpRelayAgentInfoAlreadyPresents": juniDhcpRelayAgentInfoAlreadyPresents,
       "juniDhcpRelayGatewayAddrSpoofs": juniDhcpRelayGatewayAddrSpoofs,
       "juniDhcpRelayAgentCircuitIdEnable": juniDhcpRelayAgentCircuitIdEnable,
       "juniDhcpRelayAgentRemoteIdEnable": juniDhcpRelayAgentRemoteIdEnable,
       "juniDhcpRelayAgentHostnameEnable": juniDhcpRelayAgentHostnameEnable,
       "juniDhcpRelayAgentVrnameEnable": juniDhcpRelayAgentVrnameEnable,
       "juniDhcpRelayAgentExcludeSubIdEnable": juniDhcpRelayAgentExcludeSubIdEnable,
       "juniDhcpRelayAgentTrustAllEnable": juniDhcpRelayAgentTrustAllEnable,
       "juniDhcpRelayAgentInfoAlreadyPresentForwards": juniDhcpRelayAgentInfoAlreadyPresentForwards,
       "juniDhcpRelayAgentGiaddrOverrides": juniDhcpRelayAgentGiaddrOverrides,
       "juniDhcpRelayAgentOptionOverrides": juniDhcpRelayAgentOptionOverrides,
       "juniDhcpRelayDiscoverDiscards": juniDhcpRelayDiscoverDiscards,
       "juniDhcpRelayPacketDiscards": juniDhcpRelayPacketDiscards,
       "juniDhcpRelayUnknownRequestMessages": juniDhcpRelayUnknownRequestMessages,
       "juniDhcpRelayUnknownReplyMessages": juniDhcpRelayUnknownReplyMessages,
       "juniDhcpRelayDuplicateRequestDiscards": juniDhcpRelayDuplicateRequestDiscards,
       "juniDhcpRelayPacketsTransmitted": juniDhcpRelayPacketsTransmitted,
       "juniDhcpRelayPacketsReceived": juniDhcpRelayPacketsReceived,
       "juniDhcpRelayUnknownXidDiscards": juniDhcpRelayUnknownXidDiscards,
       "juniDhcpRelayDroppedStaleRequestDiscards": juniDhcpRelayDroppedStaleRequestDiscards,
       "juniDhcpRelayLayer2UnicastReplies": juniDhcpRelayLayer2UnicastReplies,
       "juniDhcpRelayGiaddrSelectsInterface": juniDhcpRelayGiaddrSelectsInterface,
       "juniDhcpRelayAgentVendorSpecificSuboption": juniDhcpRelayAgentVendorSpecificSuboption,
       "juniDhcpRelayBroadcastFlagReplies": juniDhcpRelayBroadcastFlagReplies,
       "juniDhcpRelayServerTable": juniDhcpRelayServerTable,
       "juniDhcpRelayServerEntry": juniDhcpRelayServerEntry,
       "juniDhcpRelayServerAddress": juniDhcpRelayServerAddress,
       "juniDhcpRelayServerRowStatus": juniDhcpRelayServerRowStatus,
       "juniDhcpProxy": juniDhcpProxy,
       "juniDhcpLocalServerProxyTraps": juniDhcpLocalServerProxyTraps,
       "juniDhcpProxyClient": juniDhcpProxyClient,
       "juniDhcpProxyClientScalars": juniDhcpProxyClientScalars,
       "juniDhcpProxyClientUnknownServers": juniDhcpProxyClientUnknownServers,
       "juniDhcpProxyClientServerTable": juniDhcpProxyClientServerTable,
       "juniDhcpProxyClientServerEntry": juniDhcpProxyClientServerEntry,
       "juniDhcpProxyClientServerAddress": juniDhcpProxyClientServerAddress,
       "juniDhcpProxyClientServerRowStatus": juniDhcpProxyClientServerRowStatus,
       "juniDhcpProxyClientServerAdminStatus": juniDhcpProxyClientServerAdminStatus,
       "juniDhcpProxyClientServerOperStatus": juniDhcpProxyClientServerOperStatus,
       "juniDhcpProxyClientServerLeases": juniDhcpProxyClientServerLeases,
       "juniDhcpProxyClientServerDiscovers": juniDhcpProxyClientServerDiscovers,
       "juniDhcpProxyClientServerOffers": juniDhcpProxyClientServerOffers,
       "juniDhcpProxyClientServerRequests": juniDhcpProxyClientServerRequests,
       "juniDhcpProxyClientServerAcks": juniDhcpProxyClientServerAcks,
       "juniDhcpProxyClientServerNaks": juniDhcpProxyClientServerNaks,
       "juniDhcpProxyClientServerDeclines": juniDhcpProxyClientServerDeclines,
       "juniDhcpProxyClientServerReleases": juniDhcpProxyClientServerReleases,
       "juniDhcpProxyClientServerInforms": juniDhcpProxyClientServerInforms,
       "juniDhcpProxyClientServerBadMessages": juniDhcpProxyClientServerBadMessages,
       "juniDhcpProxyClientServerUnknownMessages": juniDhcpProxyClientServerUnknownMessages,
       "juniDhcpProxyServer": juniDhcpProxyServer,
       "juniDhcpLocalServerObjects": juniDhcpLocalServerObjects,
       "juniDhcpLocalServerTraps": juniDhcpLocalServerTraps,
       "juniDhcpLocalServerPoolHighAddrUtil": juniDhcpLocalServerPoolHighAddrUtil,
       "juniDhcpLocalServerPoolAbatedAddrUtil": juniDhcpLocalServerPoolAbatedAddrUtil,
       "juniDhcpLocalServerPoolNoAddresses": juniDhcpLocalServerPoolNoAddresses,
       "juniDhcpLocalServerHealth": juniDhcpLocalServerHealth,
       "juniDhcpLocalServerPoolGroupHighAddrUtil": juniDhcpLocalServerPoolGroupHighAddrUtil,
       "juniDhcpLocalServerPoolGroupAbatedAddrUtil": juniDhcpLocalServerPoolGroupAbatedAddrUtil,
       "juniDhcpLocalServerPoolGroupNoAddresses": juniDhcpLocalServerPoolGroupNoAddresses,
       "juniDhcpLocalServerInterfaceLimitExceeded": juniDhcpLocalServerInterfaceLimitExceeded,
       "juniDhcpLocalServerInterfaceLimitAbated": juniDhcpLocalServerInterfaceLimitAbated,
       "juniDhcpLocalServerDuplicateClient": juniDhcpLocalServerDuplicateClient,
       "juniDhcpLocalServerStatistics": juniDhcpLocalServerStatistics,
       "juniDhcpLocalServerMemUsage": juniDhcpLocalServerMemUsage,
       "juniDhcpLocalServerNumBindings": juniDhcpLocalServerNumBindings,
       "juniDhcpLocalServerRxDiscovers": juniDhcpLocalServerRxDiscovers,
       "juniDhcpLocalServerRxAccepts": juniDhcpLocalServerRxAccepts,
       "juniDhcpLocalServerRxRenews": juniDhcpLocalServerRxRenews,
       "juniDhcpLocalServerRxDeclines": juniDhcpLocalServerRxDeclines,
       "juniDhcpLocalServerRxReleases": juniDhcpLocalServerRxReleases,
       "juniDhcpLocalServerRxInforms": juniDhcpLocalServerRxInforms,
       "juniDhcpLocalServerTxOffers": juniDhcpLocalServerTxOffers,
       "juniDhcpLocalServerTxAcks": juniDhcpLocalServerTxAcks,
       "juniDhcpLocalServerTxNaks": juniDhcpLocalServerTxNaks,
       "juniDhcpLocalServerUnknownMessages": juniDhcpLocalServerUnknownMessages,
       "juniDhcpLocalServerBadMessages": juniDhcpLocalServerBadMessages,
       "juniDhcpLocalServerPacketsIn": juniDhcpLocalServerPacketsIn,
       "juniDhcpLocalServerPacketsOut": juniDhcpLocalServerPacketsOut,
       "juniDhcpLocalServerRxRebinds": juniDhcpLocalServerRxRebinds,
       "juniDhcpLocalServerRxUnknownClients": juniDhcpLocalServerRxUnknownClients,
       "juniDhcpLocalServerRxInErrors": juniDhcpLocalServerRxInErrors,
       "juniDhcpLocalServerRxInDiscards": juniDhcpLocalServerRxInDiscards,
       "juniDhcpLocalServerTxRenewAcks": juniDhcpLocalServerTxRenewAcks,
       "juniDhcpLocalServerTxRebindAcks": juniDhcpLocalServerTxRebindAcks,
       "juniDhcpLocalServerTxRenewNaks": juniDhcpLocalServerTxRenewNaks,
       "juniDhcpLocalServerTxRebindNaks": juniDhcpLocalServerTxRebindNaks,
       "juniDhcpLocalServerTxOutErrors": juniDhcpLocalServerTxOutErrors,
       "juniDhcpLocalServerTxOutDiscards": juniDhcpLocalServerTxOutDiscards,
       "juniDhcpLocalServerRxOtherRequests": juniDhcpLocalServerRxOtherRequests,
       "juniDhcpLocalServerSubInterfaceStatisticsTable": juniDhcpLocalServerSubInterfaceStatisticsTable,
       "juniDhcpLocalServerSubInterfaceStatisticsEntry": juniDhcpLocalServerSubInterfaceStatisticsEntry,
       "juniDhcpLocalServerSubInterfaceMemUsage": juniDhcpLocalServerSubInterfaceMemUsage,
       "juniDhcpLocalServerSubInterfaceNumBindings": juniDhcpLocalServerSubInterfaceNumBindings,
       "juniDhcpLocalServerSubInterfaceRxDiscovers": juniDhcpLocalServerSubInterfaceRxDiscovers,
       "juniDhcpLocalServerSubInterfaceRxAccepts": juniDhcpLocalServerSubInterfaceRxAccepts,
       "juniDhcpLocalServerSubInterfaceRxRenews": juniDhcpLocalServerSubInterfaceRxRenews,
       "juniDhcpLocalServerSubInterfaceRxDeclines": juniDhcpLocalServerSubInterfaceRxDeclines,
       "juniDhcpLocalServerSubInterfaceRxReleases": juniDhcpLocalServerSubInterfaceRxReleases,
       "juniDhcpLocalServerSubInterfaceRxInforms": juniDhcpLocalServerSubInterfaceRxInforms,
       "juniDhcpLocalServerSubInterfaceTxOffers": juniDhcpLocalServerSubInterfaceTxOffers,
       "juniDhcpLocalServerSubInterfaceTxAcks": juniDhcpLocalServerSubInterfaceTxAcks,
       "juniDhcpLocalServerSubInterfaceTxNaks": juniDhcpLocalServerSubInterfaceTxNaks,
       "juniDhcpLocalServerSubInterfaceUnknownMessages": juniDhcpLocalServerSubInterfaceUnknownMessages,
       "juniDhcpLocalServerSubInterfaceBadMessages": juniDhcpLocalServerSubInterfaceBadMessages,
       "juniDhcpLocalServerSubInterfacePacketsIn": juniDhcpLocalServerSubInterfacePacketsIn,
       "juniDhcpLocalServerSubInterfacePacketsOut": juniDhcpLocalServerSubInterfacePacketsOut,
       "juniDhcpLocalServerSubInterfaceClientCount": juniDhcpLocalServerSubInterfaceClientCount,
       "juniDhcpLocalServerSubInterfaceDeniedLogins": juniDhcpLocalServerSubInterfaceDeniedLogins,
       "juniDhcpLocalServerSubInterfaceDeniedTotal": juniDhcpLocalServerSubInterfaceDeniedTotal,
       "juniDhcpLocalServerSubInterfaceRxRebinds": juniDhcpLocalServerSubInterfaceRxRebinds,
       "juniDhcpLocalServerSubInterfaceRxUnknownClients": juniDhcpLocalServerSubInterfaceRxUnknownClients,
       "juniDhcpLocalServerSubInterfaceRxInErrors": juniDhcpLocalServerSubInterfaceRxInErrors,
       "juniDhcpLocalServerSubInterfaceRxInDiscards": juniDhcpLocalServerSubInterfaceRxInDiscards,
       "juniDhcpLocalServerSubInterfaceTxRenewAcks": juniDhcpLocalServerSubInterfaceTxRenewAcks,
       "juniDhcpLocalServerSubInterfaceTxRebindAcks": juniDhcpLocalServerSubInterfaceTxRebindAcks,
       "juniDhcpLocalServerSubInterfaceTxRenewNaks": juniDhcpLocalServerSubInterfaceTxRenewNaks,
       "juniDhcpLocalServerSubInterfaceTxRebindNaks": juniDhcpLocalServerSubInterfaceTxRebindNaks,
       "juniDhcpLocalServerSubInterfaceTxOutErrors": juniDhcpLocalServerSubInterfaceTxOutErrors,
       "juniDhcpLocalServerSubInterfaceTxOutDiscards": juniDhcpLocalServerSubInterfaceTxOutDiscards,
       "juniDhcpLocalServerSubInterfaceRxOtherRequests": juniDhcpLocalServerSubInterfaceRxOtherRequests,
       "juniDhcpLocalServerBindings": juniDhcpLocalServerBindings,
       "juniDhcpLocalServerBindingsTable": juniDhcpLocalServerBindingsTable,
       "juniDhcpLocalServerBindingsEntry": juniDhcpLocalServerBindingsEntry,
       "juniDhcpLocalServerBindingsIpAddress": juniDhcpLocalServerBindingsIpAddress,
       "juniDhcpLocalServerBindingsPhysAddress": juniDhcpLocalServerBindingsPhysAddress,
       "juniDhcpLocalServerBindingsInfinite": juniDhcpLocalServerBindingsInfinite,
       "juniDhcpLocalServerBindingsExpireTime": juniDhcpLocalServerBindingsExpireTime,
       "juniDhcpLocalServerBindingsRowStatus": juniDhcpLocalServerBindingsRowStatus,
       "juniDhcpLocalServerBindingsLeaseInterval": juniDhcpLocalServerBindingsLeaseInterval,
       "juniDhcpLocalServerBindingsLeaseStartTime": juniDhcpLocalServerBindingsLeaseStartTime,
       "juniDhcpLocalServerBindingsInitialLeaseStartTime": juniDhcpLocalServerBindingsInitialLeaseStartTime,
       "juniDhcpLocalServerPool": juniDhcpLocalServerPool,
       "juniDhcpLocalServerPoolTable": juniDhcpLocalServerPoolTable,
       "juniDhcpLocalServerPoolEntry": juniDhcpLocalServerPoolEntry,
       "juniDhcpLocalServerPoolName": juniDhcpLocalServerPoolName,
       "juniDhcpLocalServerPoolDomainName": juniDhcpLocalServerPoolDomainName,
       "juniDhcpLocalServerPoolNetworkIpAddress": juniDhcpLocalServerPoolNetworkIpAddress,
       "juniDhcpLocalServerPoolNetworkMask": juniDhcpLocalServerPoolNetworkMask,
       "juniDhcpLocalServerPoolNetBiosNodeType": juniDhcpLocalServerPoolNetBiosNodeType,
       "juniDhcpLocalServerPoolLeaseTime": juniDhcpLocalServerPoolLeaseTime,
       "juniDhcpLocalServerPoolPrimaryDnsServer": juniDhcpLocalServerPoolPrimaryDnsServer,
       "juniDhcpLocalServerPoolSecondaryDnsServer": juniDhcpLocalServerPoolSecondaryDnsServer,
       "juniDhcpLocalServerPoolPrimaryNetBiosNameServer": juniDhcpLocalServerPoolPrimaryNetBiosNameServer,
       "juniDhcpLocalServerPoolSecondaryNetBiosNameServer": juniDhcpLocalServerPoolSecondaryNetBiosNameServer,
       "juniDhcpLocalServerPoolPrimaryDefaultRouter": juniDhcpLocalServerPoolPrimaryDefaultRouter,
       "juniDhcpLocalServerPoolSecondaryDefaultRouter": juniDhcpLocalServerPoolSecondaryDefaultRouter,
       "juniDhcpLocalServerPoolRowStatus": juniDhcpLocalServerPoolRowStatus,
       "juniDhcpLocalServerPoolLinkName": juniDhcpLocalServerPoolLinkName,
       "juniDhcpLocalServerPoolHighUtilThreshold": juniDhcpLocalServerPoolHighUtilThreshold,
       "juniDhcpLocalServerPoolAbatedUtilThreshold": juniDhcpLocalServerPoolAbatedUtilThreshold,
       "juniDhcpLocalServerPoolUtilPct": juniDhcpLocalServerPoolUtilPct,
       "juniDhcpLocalServerPoolTrapEnable": juniDhcpLocalServerPoolTrapEnable,
       "juniDhcpLocalServerPoolInUse": juniDhcpLocalServerPoolInUse,
       "juniDhcpLocalServerPoolSize": juniDhcpLocalServerPoolSize,
       "juniDhcpLocalServerPoolSharedInUse": juniDhcpLocalServerPoolSharedInUse,
       "juniDhcpLocalServerAttributes": juniDhcpLocalServerAttributes,
       "juniDhcpLocalServerAttributesMode": juniDhcpLocalServerAttributesMode,
       "juniDhcpLocalServerSubInterfaceTable": juniDhcpLocalServerSubInterfaceTable,
       "juniDhcpLocalServerSubInterfaceEntry": juniDhcpLocalServerSubInterfaceEntry,
       "juniDhcpLocalServerSubInterfaceIndex": juniDhcpLocalServerSubInterfaceIndex,
       "juniDhcpLocalServerSubInterfaceName": juniDhcpLocalServerSubInterfaceName,
       "juniDhcpLocalServerSubInterfaceLimit": juniDhcpLocalServerSubInterfaceLimit,
       "juniDhcpLocalServerSnmpTrap": juniDhcpLocalServerSnmpTrap,
       "juniDhcpLocalServerInhibitRoaming": juniDhcpLocalServerInhibitRoaming,
       "juniDhcpLocalServerUniqueClientIds": juniDhcpLocalServerUniqueClientIds,
       "juniDhcpLocalServerReserves": juniDhcpLocalServerReserves,
       "juniDhcpLocalServerReservesTable": juniDhcpLocalServerReservesTable,
       "juniDhcpLocalServerReservesEntry": juniDhcpLocalServerReservesEntry,
       "juniDhcpLocalServerReservesEntryIpAddress": juniDhcpLocalServerReservesEntryIpAddress,
       "juniDhcpLocalServerReservesEntryPoolName": juniDhcpLocalServerReservesEntryPoolName,
       "juniDhcpLocalServerReservesEntryPhysAddress": juniDhcpLocalServerReservesEntryPhysAddress,
       "juniDhcpLocalServerReservesEntryRowStatus": juniDhcpLocalServerReservesEntryRowStatus,
       "juniDhcpLocalServerCableModemServers": juniDhcpLocalServerCableModemServers,
       "juniDhcpLocalServerCableModemServerTable": juniDhcpLocalServerCableModemServerTable,
       "juniDhcpLocalServerCableModemServerEntry": juniDhcpLocalServerCableModemServerEntry,
       "juniDhcpLocalServerCableModemServerEntryAddress": juniDhcpLocalServerCableModemServerEntryAddress,
       "juniDhcpLocalServerCableModemServerEntryRowStatus": juniDhcpLocalServerCableModemServerEntryRowStatus,
       "juniDhcpLocalServerCableModemStatistics": juniDhcpLocalServerCableModemStatistics,
       "juniDhcpLocalServerCableModemRequestIn": juniDhcpLocalServerCableModemRequestIn,
       "juniDhcpLocalServerCableModemResponseIn": juniDhcpLocalServerCableModemResponseIn,
       "juniDhcpLocalServerCableModemRequestOut": juniDhcpLocalServerCableModemRequestOut,
       "juniDhcpLocalServerCableModemResponseOut": juniDhcpLocalServerCableModemResponseOut,
       "juniDhcpLocalServerCableModemRequestDropped": juniDhcpLocalServerCableModemRequestDropped,
       "juniDhcpLocalServerCableModemResponseDropped": juniDhcpLocalServerCableModemResponseDropped,
       "juniDhcpLocalServerCableModemRequestBad": juniDhcpLocalServerCableModemRequestBad,
       "juniDhcpLocalServerCableModemResponseBad": juniDhcpLocalServerCableModemResponseBad,
       "juniDhcpLocalServerCableModemRequestDeleted": juniDhcpLocalServerCableModemRequestDeleted,
       "juniDhcpLocalServerCableModemPacketsIn": juniDhcpLocalServerCableModemPacketsIn,
       "juniDhcpLocalServerCableModemPacketsOut": juniDhcpLocalServerCableModemPacketsOut,
       "juniDhcpLocalServerCableModemPacketsDropped": juniDhcpLocalServerCableModemPacketsDropped,
       "juniDhcpLocalServerPoolGroup": juniDhcpLocalServerPoolGroup,
       "juniDhcpLocalServerPoolGroupTable": juniDhcpLocalServerPoolGroupTable,
       "juniDhcpLocalServerPoolGroupEntry": juniDhcpLocalServerPoolGroupEntry,
       "juniDhcpLocalServerPoolGroupName": juniDhcpLocalServerPoolGroupName,
       "juniDhcpLocalServerPoolGroupSize": juniDhcpLocalServerPoolGroupSize,
       "juniDhcpLocalServerPoolGroupInUse": juniDhcpLocalServerPoolGroupInUse,
       "juniDhcpLocalServerPoolGroupUtilPct": juniDhcpLocalServerPoolGroupUtilPct,
       "juniDhcpTrapControl": juniDhcpTrapControl,
       "juniDhcpLocalServerEventSeverity": juniDhcpLocalServerEventSeverity,
       "juniDhcpLocalServerEventString": juniDhcpLocalServerEventString,
       "juniDhcpLocalServerMacAddress": juniDhcpLocalServerMacAddress,
       "juniDhcpLocalServerInterfaceString": juniDhcpLocalServerInterfaceString,
       "juniDhcpLocalServerLastDetected": juniDhcpLocalServerLastDetected,
       "juniDhcpMIBConformance": juniDhcpMIBConformance,
       "juniDhcpMIBCompliances": juniDhcpMIBCompliances,
       "juniDhcpRelayCompliance": juniDhcpRelayCompliance,
       "juniDhcpProxyCompliance": juniDhcpProxyCompliance,
       "juniDhcpCompliance": juniDhcpCompliance,
       "juniDhcpCompliance2": juniDhcpCompliance2,
       "juniDhcpCompliance3": juniDhcpCompliance3,
       "juniDhcpCompliance4": juniDhcpCompliance4,
       "juniDhcpCompliance5": juniDhcpCompliance5,
       "juniDhcpCompliance6": juniDhcpCompliance6,
       "juniDhcpCompliance7": juniDhcpCompliance7,
       "juniDhcpCompliance8": juniDhcpCompliance8,
       "juniDhcpCompliance9": juniDhcpCompliance9,
       "juniDhcpCompliance10": juniDhcpCompliance10,
       "juniDhcpCompliance11": juniDhcpCompliance11,
       "juniDhcpCompliance12": juniDhcpCompliance12,
       "juniDhcpMIBGroups": juniDhcpMIBGroups,
       "juniDhcpRelayGroup": juniDhcpRelayGroup,
       "juniDhcpProxyGroup": juniDhcpProxyGroup,
       "juniDhcpLocalServerGroup": juniDhcpLocalServerGroup,
       "juniDhcpLocalServerGroup2": juniDhcpLocalServerGroup2,
       "juniDhcpRelayGroup2": juniDhcpRelayGroup2,
       "juniDhcpRelayGroup3": juniDhcpRelayGroup3,
       "juniDhcpRelayGroup4": juniDhcpRelayGroup4,
       "juniDhcpRelayDeprecatedGroup": juniDhcpRelayDeprecatedGroup,
       "juniDhcpLocalServerGroup3": juniDhcpLocalServerGroup3,
       "juniDhcpLocalServerPoolTrapGroup": juniDhcpLocalServerPoolTrapGroup,
       "juniDhcpLocalServerGroup4": juniDhcpLocalServerGroup4,
       "juniDhcpRelayGroup5": juniDhcpRelayGroup5,
       "juniDhcpLocalServerGroup5": juniDhcpLocalServerGroup5,
       "juniDhcpLocalServerGroup6": juniDhcpLocalServerGroup6,
       "juniDhcpLocalServerPoolTrapGroup2": juniDhcpLocalServerPoolTrapGroup2,
       "juniDhcpLocalServerTrapGroup": juniDhcpLocalServerTrapGroup,
       "juniDhcpRelayGroup6": juniDhcpRelayGroup6,
       "juniDhcpRelayGroup7": juniDhcpRelayGroup7,
       "juniDhcpRelayGroup8": juniDhcpRelayGroup8,
       "juniDhcpRelayGroup9": juniDhcpRelayGroup9,
       "juniDhcpLocalServerGroup7": juniDhcpLocalServerGroup7,
       "juniDhcpRelayGroup10": juniDhcpRelayGroup10,
       "juniDhcpLocalServerGroup8": juniDhcpLocalServerGroup8}
)
