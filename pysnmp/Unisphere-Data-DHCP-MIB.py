# SNMP MIB module (Unisphere-Data-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:30 2024
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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable")


# MODULE-IDENTITY

usdDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22)
)
usdDhcpMIB.setRevisions(
        ("2002-05-10 19:27",
         "2001-03-30 18:09",
         "2000-02-03 19:50",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdDhcpLocalServerPoolName(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class UsdDhcpLocalServerPoolDomainName(OctetString, TextualConvention):
    status = "current"
    displayHint = "64a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class UsdDhcpLocalServerPoolNetBiosNodeType(Integer32, TextualConvention):
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



class UsdDhcpLocalServerModeType(Integer32, TextualConvention):
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



class UsdDhcpLocalServerPhysAddressString(OctetString, TextualConvention):
    status = "current"
    displayHint = "48a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )



# MIB Managed Objects in the order of their OIDs

_UsdDhcpObjects_ObjectIdentity = ObjectIdentity
usdDhcpObjects = _UsdDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1)
)
_UsdDhcpRelay_ObjectIdentity = ObjectIdentity
usdDhcpRelay = _UsdDhcpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1)
)
_UsdDhcpRelayScalars_ObjectIdentity = ObjectIdentity
usdDhcpRelayScalars = _UsdDhcpRelayScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1)
)
_UsdDhcpRelayAgentInfoEnable_Type = UsdEnable
_UsdDhcpRelayAgentInfoEnable_Object = MibScalar
usdDhcpRelayAgentInfoEnable = _UsdDhcpRelayAgentInfoEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 1),
    _UsdDhcpRelayAgentInfoEnable_Type()
)
usdDhcpRelayAgentInfoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdDhcpRelayAgentInfoEnable.setStatus("deprecated")
_UsdDhcpRelayBadMessages_Type = Counter32
_UsdDhcpRelayBadMessages_Object = MibScalar
usdDhcpRelayBadMessages = _UsdDhcpRelayBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 2),
    _UsdDhcpRelayBadMessages_Type()
)
usdDhcpRelayBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpRelayBadMessages.setStatus("current")
_UsdDhcpRelayUnknownMessages_Type = Counter32
_UsdDhcpRelayUnknownMessages_Object = MibScalar
usdDhcpRelayUnknownMessages = _UsdDhcpRelayUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 3),
    _UsdDhcpRelayUnknownMessages_Type()
)
usdDhcpRelayUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpRelayUnknownMessages.setStatus("current")
_UsdDhcpRelayAgentInfoAlreadyPresents_Type = Counter32
_UsdDhcpRelayAgentInfoAlreadyPresents_Object = MibScalar
usdDhcpRelayAgentInfoAlreadyPresents = _UsdDhcpRelayAgentInfoAlreadyPresents_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 4),
    _UsdDhcpRelayAgentInfoAlreadyPresents_Type()
)
usdDhcpRelayAgentInfoAlreadyPresents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpRelayAgentInfoAlreadyPresents.setStatus("current")
_UsdDhcpRelayGatewayAddrSpoofs_Type = Counter32
_UsdDhcpRelayGatewayAddrSpoofs_Object = MibScalar
usdDhcpRelayGatewayAddrSpoofs = _UsdDhcpRelayGatewayAddrSpoofs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 5),
    _UsdDhcpRelayGatewayAddrSpoofs_Type()
)
usdDhcpRelayGatewayAddrSpoofs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpRelayGatewayAddrSpoofs.setStatus("current")
_UsdDhcpRelayAgentCircuitIdEnable_Type = UsdEnable
_UsdDhcpRelayAgentCircuitIdEnable_Object = MibScalar
usdDhcpRelayAgentCircuitIdEnable = _UsdDhcpRelayAgentCircuitIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 6),
    _UsdDhcpRelayAgentCircuitIdEnable_Type()
)
usdDhcpRelayAgentCircuitIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdDhcpRelayAgentCircuitIdEnable.setStatus("current")
_UsdDhcpRelayAgentRemoteIdEnable_Type = UsdEnable
_UsdDhcpRelayAgentRemoteIdEnable_Object = MibScalar
usdDhcpRelayAgentRemoteIdEnable = _UsdDhcpRelayAgentRemoteIdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 1, 7),
    _UsdDhcpRelayAgentRemoteIdEnable_Type()
)
usdDhcpRelayAgentRemoteIdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdDhcpRelayAgentRemoteIdEnable.setStatus("current")
_UsdDhcpRelayServerTable_Object = MibTable
usdDhcpRelayServerTable = _UsdDhcpRelayServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdDhcpRelayServerTable.setStatus("current")
_UsdDhcpRelayServerEntry_Object = MibTableRow
usdDhcpRelayServerEntry = _UsdDhcpRelayServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2, 1)
)
usdDhcpRelayServerEntry.setIndexNames(
    (0, "Unisphere-Data-DHCP-MIB", "usdDhcpRelayServerAddress"),
)
if mibBuilder.loadTexts:
    usdDhcpRelayServerEntry.setStatus("current")
_UsdDhcpRelayServerAddress_Type = IpAddress
_UsdDhcpRelayServerAddress_Object = MibTableColumn
usdDhcpRelayServerAddress = _UsdDhcpRelayServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2, 1, 1),
    _UsdDhcpRelayServerAddress_Type()
)
usdDhcpRelayServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDhcpRelayServerAddress.setStatus("current")
_UsdDhcpRelayServerRowStatus_Type = RowStatus
_UsdDhcpRelayServerRowStatus_Object = MibTableColumn
usdDhcpRelayServerRowStatus = _UsdDhcpRelayServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 1, 2, 1, 2),
    _UsdDhcpRelayServerRowStatus_Type()
)
usdDhcpRelayServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpRelayServerRowStatus.setStatus("current")
_UsdDhcpProxy_ObjectIdentity = ObjectIdentity
usdDhcpProxy = _UsdDhcpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2)
)
_UsdDhcpProxyClient_ObjectIdentity = ObjectIdentity
usdDhcpProxyClient = _UsdDhcpProxyClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1)
)
_UsdDhcpProxyClientScalars_ObjectIdentity = ObjectIdentity
usdDhcpProxyClientScalars = _UsdDhcpProxyClientScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 1)
)
_UsdDhcpProxyClientUnknownServers_Type = Counter32
_UsdDhcpProxyClientUnknownServers_Object = MibScalar
usdDhcpProxyClientUnknownServers = _UsdDhcpProxyClientUnknownServers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 1, 1),
    _UsdDhcpProxyClientUnknownServers_Type()
)
usdDhcpProxyClientUnknownServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientUnknownServers.setStatus("current")
_UsdDhcpProxyClientServerTable_Object = MibTable
usdDhcpProxyClientServerTable = _UsdDhcpProxyClientServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerTable.setStatus("current")
_UsdDhcpProxyClientServerEntry_Object = MibTableRow
usdDhcpProxyClientServerEntry = _UsdDhcpProxyClientServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1)
)
usdDhcpProxyClientServerEntry.setIndexNames(
    (0, "Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerAddress"),
)
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerEntry.setStatus("current")
_UsdDhcpProxyClientServerAddress_Type = IpAddress
_UsdDhcpProxyClientServerAddress_Object = MibTableColumn
usdDhcpProxyClientServerAddress = _UsdDhcpProxyClientServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 1),
    _UsdDhcpProxyClientServerAddress_Type()
)
usdDhcpProxyClientServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerAddress.setStatus("current")
_UsdDhcpProxyClientServerRowStatus_Type = RowStatus
_UsdDhcpProxyClientServerRowStatus_Object = MibTableColumn
usdDhcpProxyClientServerRowStatus = _UsdDhcpProxyClientServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 2),
    _UsdDhcpProxyClientServerRowStatus_Type()
)
usdDhcpProxyClientServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerRowStatus.setStatus("current")


class _UsdDhcpProxyClientServerAdminStatus_Type(Integer32):
    """Custom type usdDhcpProxyClientServerAdminStatus based on Integer32"""
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


_UsdDhcpProxyClientServerAdminStatus_Type.__name__ = "Integer32"
_UsdDhcpProxyClientServerAdminStatus_Object = MibTableColumn
usdDhcpProxyClientServerAdminStatus = _UsdDhcpProxyClientServerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 3),
    _UsdDhcpProxyClientServerAdminStatus_Type()
)
usdDhcpProxyClientServerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerAdminStatus.setStatus("current")


class _UsdDhcpProxyClientServerOperStatus_Type(Integer32):
    """Custom type usdDhcpProxyClientServerOperStatus based on Integer32"""
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


_UsdDhcpProxyClientServerOperStatus_Type.__name__ = "Integer32"
_UsdDhcpProxyClientServerOperStatus_Object = MibTableColumn
usdDhcpProxyClientServerOperStatus = _UsdDhcpProxyClientServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 4),
    _UsdDhcpProxyClientServerOperStatus_Type()
)
usdDhcpProxyClientServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerOperStatus.setStatus("current")
_UsdDhcpProxyClientServerLeases_Type = Counter32
_UsdDhcpProxyClientServerLeases_Object = MibTableColumn
usdDhcpProxyClientServerLeases = _UsdDhcpProxyClientServerLeases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 5),
    _UsdDhcpProxyClientServerLeases_Type()
)
usdDhcpProxyClientServerLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerLeases.setStatus("current")
_UsdDhcpProxyClientServerDiscovers_Type = Counter32
_UsdDhcpProxyClientServerDiscovers_Object = MibTableColumn
usdDhcpProxyClientServerDiscovers = _UsdDhcpProxyClientServerDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 6),
    _UsdDhcpProxyClientServerDiscovers_Type()
)
usdDhcpProxyClientServerDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerDiscovers.setStatus("current")
_UsdDhcpProxyClientServerOffers_Type = Counter32
_UsdDhcpProxyClientServerOffers_Object = MibTableColumn
usdDhcpProxyClientServerOffers = _UsdDhcpProxyClientServerOffers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 7),
    _UsdDhcpProxyClientServerOffers_Type()
)
usdDhcpProxyClientServerOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerOffers.setStatus("current")
_UsdDhcpProxyClientServerRequests_Type = Counter32
_UsdDhcpProxyClientServerRequests_Object = MibTableColumn
usdDhcpProxyClientServerRequests = _UsdDhcpProxyClientServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 8),
    _UsdDhcpProxyClientServerRequests_Type()
)
usdDhcpProxyClientServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerRequests.setStatus("current")
_UsdDhcpProxyClientServerAcks_Type = Counter32
_UsdDhcpProxyClientServerAcks_Object = MibTableColumn
usdDhcpProxyClientServerAcks = _UsdDhcpProxyClientServerAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 9),
    _UsdDhcpProxyClientServerAcks_Type()
)
usdDhcpProxyClientServerAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerAcks.setStatus("current")
_UsdDhcpProxyClientServerNaks_Type = Counter32
_UsdDhcpProxyClientServerNaks_Object = MibTableColumn
usdDhcpProxyClientServerNaks = _UsdDhcpProxyClientServerNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 10),
    _UsdDhcpProxyClientServerNaks_Type()
)
usdDhcpProxyClientServerNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerNaks.setStatus("current")
_UsdDhcpProxyClientServerDeclines_Type = Counter32
_UsdDhcpProxyClientServerDeclines_Object = MibTableColumn
usdDhcpProxyClientServerDeclines = _UsdDhcpProxyClientServerDeclines_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 11),
    _UsdDhcpProxyClientServerDeclines_Type()
)
usdDhcpProxyClientServerDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerDeclines.setStatus("current")
_UsdDhcpProxyClientServerReleases_Type = Counter32
_UsdDhcpProxyClientServerReleases_Object = MibTableColumn
usdDhcpProxyClientServerReleases = _UsdDhcpProxyClientServerReleases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 12),
    _UsdDhcpProxyClientServerReleases_Type()
)
usdDhcpProxyClientServerReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerReleases.setStatus("current")
_UsdDhcpProxyClientServerInforms_Type = Counter32
_UsdDhcpProxyClientServerInforms_Object = MibTableColumn
usdDhcpProxyClientServerInforms = _UsdDhcpProxyClientServerInforms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 13),
    _UsdDhcpProxyClientServerInforms_Type()
)
usdDhcpProxyClientServerInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerInforms.setStatus("current")
_UsdDhcpProxyClientServerBadMessages_Type = Counter32
_UsdDhcpProxyClientServerBadMessages_Object = MibTableColumn
usdDhcpProxyClientServerBadMessages = _UsdDhcpProxyClientServerBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 14),
    _UsdDhcpProxyClientServerBadMessages_Type()
)
usdDhcpProxyClientServerBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerBadMessages.setStatus("current")
_UsdDhcpProxyClientServerUnknownMessages_Type = Counter32
_UsdDhcpProxyClientServerUnknownMessages_Object = MibTableColumn
usdDhcpProxyClientServerUnknownMessages = _UsdDhcpProxyClientServerUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 1, 2, 1, 15),
    _UsdDhcpProxyClientServerUnknownMessages_Type()
)
usdDhcpProxyClientServerUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpProxyClientServerUnknownMessages.setStatus("current")
_UsdDhcpProxyServer_ObjectIdentity = ObjectIdentity
usdDhcpProxyServer = _UsdDhcpProxyServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 2, 2)
)
_UsdDhcpLocalServerObjects_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerObjects = _UsdDhcpLocalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3)
)
_UsdDhcpLocalServerStatistics_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerStatistics = _UsdDhcpLocalServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1)
)
_UsdDhcpLocalServerMemUsage_Type = Counter32
_UsdDhcpLocalServerMemUsage_Object = MibScalar
usdDhcpLocalServerMemUsage = _UsdDhcpLocalServerMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 1),
    _UsdDhcpLocalServerMemUsage_Type()
)
usdDhcpLocalServerMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerMemUsage.setStatus("current")
_UsdDhcpLocalServerNumBindings_Type = Counter32
_UsdDhcpLocalServerNumBindings_Object = MibScalar
usdDhcpLocalServerNumBindings = _UsdDhcpLocalServerNumBindings_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 2),
    _UsdDhcpLocalServerNumBindings_Type()
)
usdDhcpLocalServerNumBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerNumBindings.setStatus("current")
_UsdDhcpLocalServerRxDiscovers_Type = Counter32
_UsdDhcpLocalServerRxDiscovers_Object = MibScalar
usdDhcpLocalServerRxDiscovers = _UsdDhcpLocalServerRxDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 3),
    _UsdDhcpLocalServerRxDiscovers_Type()
)
usdDhcpLocalServerRxDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerRxDiscovers.setStatus("current")
_UsdDhcpLocalServerRxAccepts_Type = Counter32
_UsdDhcpLocalServerRxAccepts_Object = MibScalar
usdDhcpLocalServerRxAccepts = _UsdDhcpLocalServerRxAccepts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 4),
    _UsdDhcpLocalServerRxAccepts_Type()
)
usdDhcpLocalServerRxAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerRxAccepts.setStatus("current")
_UsdDhcpLocalServerRxRenews_Type = Counter32
_UsdDhcpLocalServerRxRenews_Object = MibScalar
usdDhcpLocalServerRxRenews = _UsdDhcpLocalServerRxRenews_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 5),
    _UsdDhcpLocalServerRxRenews_Type()
)
usdDhcpLocalServerRxRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerRxRenews.setStatus("current")
_UsdDhcpLocalServerRxDeclines_Type = Counter32
_UsdDhcpLocalServerRxDeclines_Object = MibScalar
usdDhcpLocalServerRxDeclines = _UsdDhcpLocalServerRxDeclines_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 6),
    _UsdDhcpLocalServerRxDeclines_Type()
)
usdDhcpLocalServerRxDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerRxDeclines.setStatus("current")
_UsdDhcpLocalServerRxReleases_Type = Counter32
_UsdDhcpLocalServerRxReleases_Object = MibScalar
usdDhcpLocalServerRxReleases = _UsdDhcpLocalServerRxReleases_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 7),
    _UsdDhcpLocalServerRxReleases_Type()
)
usdDhcpLocalServerRxReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerRxReleases.setStatus("current")
_UsdDhcpLocalServerRxInforms_Type = Counter32
_UsdDhcpLocalServerRxInforms_Object = MibScalar
usdDhcpLocalServerRxInforms = _UsdDhcpLocalServerRxInforms_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 8),
    _UsdDhcpLocalServerRxInforms_Type()
)
usdDhcpLocalServerRxInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerRxInforms.setStatus("current")
_UsdDhcpLocalServerTxOffers_Type = Counter32
_UsdDhcpLocalServerTxOffers_Object = MibScalar
usdDhcpLocalServerTxOffers = _UsdDhcpLocalServerTxOffers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 9),
    _UsdDhcpLocalServerTxOffers_Type()
)
usdDhcpLocalServerTxOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerTxOffers.setStatus("current")
_UsdDhcpLocalServerTxAcks_Type = Counter32
_UsdDhcpLocalServerTxAcks_Object = MibScalar
usdDhcpLocalServerTxAcks = _UsdDhcpLocalServerTxAcks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 10),
    _UsdDhcpLocalServerTxAcks_Type()
)
usdDhcpLocalServerTxAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerTxAcks.setStatus("current")
_UsdDhcpLocalServerTxNaks_Type = Counter32
_UsdDhcpLocalServerTxNaks_Object = MibScalar
usdDhcpLocalServerTxNaks = _UsdDhcpLocalServerTxNaks_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 11),
    _UsdDhcpLocalServerTxNaks_Type()
)
usdDhcpLocalServerTxNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerTxNaks.setStatus("current")
_UsdDhcpLocalServerUnknownMessages_Type = Counter32
_UsdDhcpLocalServerUnknownMessages_Object = MibScalar
usdDhcpLocalServerUnknownMessages = _UsdDhcpLocalServerUnknownMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 12),
    _UsdDhcpLocalServerUnknownMessages_Type()
)
usdDhcpLocalServerUnknownMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerUnknownMessages.setStatus("current")
_UsdDhcpLocalServerBadMessages_Type = Counter32
_UsdDhcpLocalServerBadMessages_Object = MibScalar
usdDhcpLocalServerBadMessages = _UsdDhcpLocalServerBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 13),
    _UsdDhcpLocalServerBadMessages_Type()
)
usdDhcpLocalServerBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerBadMessages.setStatus("current")
_UsdDhcpLocalServerPacketsIn_Type = Counter32
_UsdDhcpLocalServerPacketsIn_Object = MibScalar
usdDhcpLocalServerPacketsIn = _UsdDhcpLocalServerPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 14),
    _UsdDhcpLocalServerPacketsIn_Type()
)
usdDhcpLocalServerPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPacketsIn.setStatus("current")
_UsdDhcpLocalServerPacketsOut_Type = Counter32
_UsdDhcpLocalServerPacketsOut_Object = MibScalar
usdDhcpLocalServerPacketsOut = _UsdDhcpLocalServerPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 1, 15),
    _UsdDhcpLocalServerPacketsOut_Type()
)
usdDhcpLocalServerPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPacketsOut.setStatus("current")
_UsdDhcpLocalServerBindings_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerBindings = _UsdDhcpLocalServerBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2)
)
_UsdDhcpLocalServerBindingsTable_Object = MibTable
usdDhcpLocalServerBindingsTable = _UsdDhcpLocalServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerBindingsTable.setStatus("current")
_UsdDhcpLocalServerBindingsEntry_Object = MibTableRow
usdDhcpLocalServerBindingsEntry = _UsdDhcpLocalServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1)
)
usdDhcpLocalServerBindingsEntry.setIndexNames(
    (0, "Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBindingsIpAddress"),
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerBindingsEntry.setStatus("current")
_UsdDhcpLocalServerBindingsIpAddress_Type = IpAddress
_UsdDhcpLocalServerBindingsIpAddress_Object = MibTableColumn
usdDhcpLocalServerBindingsIpAddress = _UsdDhcpLocalServerBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 1),
    _UsdDhcpLocalServerBindingsIpAddress_Type()
)
usdDhcpLocalServerBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDhcpLocalServerBindingsIpAddress.setStatus("current")


class _UsdDhcpLocalServerBindingsPhysAddress_Type(PhysAddress):
    """Custom type usdDhcpLocalServerBindingsPhysAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_UsdDhcpLocalServerBindingsPhysAddress_Type.__name__ = "PhysAddress"
_UsdDhcpLocalServerBindingsPhysAddress_Object = MibTableColumn
usdDhcpLocalServerBindingsPhysAddress = _UsdDhcpLocalServerBindingsPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 2),
    _UsdDhcpLocalServerBindingsPhysAddress_Type()
)
usdDhcpLocalServerBindingsPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerBindingsPhysAddress.setStatus("current")
_UsdDhcpLocalServerBindingsInfinite_Type = TruthValue
_UsdDhcpLocalServerBindingsInfinite_Object = MibTableColumn
usdDhcpLocalServerBindingsInfinite = _UsdDhcpLocalServerBindingsInfinite_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 3),
    _UsdDhcpLocalServerBindingsInfinite_Type()
)
usdDhcpLocalServerBindingsInfinite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerBindingsInfinite.setStatus("current")
_UsdDhcpLocalServerBindingsExpireTime_Type = TimeInterval
_UsdDhcpLocalServerBindingsExpireTime_Object = MibTableColumn
usdDhcpLocalServerBindingsExpireTime = _UsdDhcpLocalServerBindingsExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 2, 1, 1, 4),
    _UsdDhcpLocalServerBindingsExpireTime_Type()
)
usdDhcpLocalServerBindingsExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerBindingsExpireTime.setStatus("current")
_UsdDhcpLocalServerPool_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerPool = _UsdDhcpLocalServerPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3)
)
_UsdDhcpLocalServerPoolTable_Object = MibTable
usdDhcpLocalServerPoolTable = _UsdDhcpLocalServerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolTable.setStatus("current")
_UsdDhcpLocalServerPoolEntry_Object = MibTableRow
usdDhcpLocalServerPoolEntry = _UsdDhcpLocalServerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1)
)
usdDhcpLocalServerPoolEntry.setIndexNames(
    (0, "Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolName"),
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolEntry.setStatus("current")
_UsdDhcpLocalServerPoolName_Type = UsdDhcpLocalServerPoolName
_UsdDhcpLocalServerPoolName_Object = MibTableColumn
usdDhcpLocalServerPoolName = _UsdDhcpLocalServerPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 1),
    _UsdDhcpLocalServerPoolName_Type()
)
usdDhcpLocalServerPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolName.setStatus("current")
_UsdDhcpLocalServerPoolDomainName_Type = UsdDhcpLocalServerPoolDomainName
_UsdDhcpLocalServerPoolDomainName_Object = MibTableColumn
usdDhcpLocalServerPoolDomainName = _UsdDhcpLocalServerPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 2),
    _UsdDhcpLocalServerPoolDomainName_Type()
)
usdDhcpLocalServerPoolDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolDomainName.setStatus("current")


class _UsdDhcpLocalServerPoolNetworkIpAddress_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolNetworkIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolNetworkIpAddress_Object = MibTableColumn
usdDhcpLocalServerPoolNetworkIpAddress = _UsdDhcpLocalServerPoolNetworkIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 3),
    _UsdDhcpLocalServerPoolNetworkIpAddress_Type()
)
usdDhcpLocalServerPoolNetworkIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolNetworkIpAddress.setStatus("current")


class _UsdDhcpLocalServerPoolNetworkMask_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolNetworkMask based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolNetworkMask_Object = MibTableColumn
usdDhcpLocalServerPoolNetworkMask = _UsdDhcpLocalServerPoolNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 4),
    _UsdDhcpLocalServerPoolNetworkMask_Type()
)
usdDhcpLocalServerPoolNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolNetworkMask.setStatus("current")


class _UsdDhcpLocalServerPoolNetBiosNodeType_Type(UsdDhcpLocalServerPoolNetBiosNodeType):
    """Custom type usdDhcpLocalServerPoolNetBiosNodeType based on UsdDhcpLocalServerPoolNetBiosNodeType"""


_UsdDhcpLocalServerPoolNetBiosNodeType_Object = MibTableColumn
usdDhcpLocalServerPoolNetBiosNodeType = _UsdDhcpLocalServerPoolNetBiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 5),
    _UsdDhcpLocalServerPoolNetBiosNodeType_Type()
)
usdDhcpLocalServerPoolNetBiosNodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolNetBiosNodeType.setStatus("current")
_UsdDhcpLocalServerPoolLeaseTime_Type = TimeInterval
_UsdDhcpLocalServerPoolLeaseTime_Object = MibTableColumn
usdDhcpLocalServerPoolLeaseTime = _UsdDhcpLocalServerPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 6),
    _UsdDhcpLocalServerPoolLeaseTime_Type()
)
usdDhcpLocalServerPoolLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolLeaseTime.setStatus("current")


class _UsdDhcpLocalServerPoolPrimaryDnsServer_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolPrimaryDnsServer based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolPrimaryDnsServer_Object = MibTableColumn
usdDhcpLocalServerPoolPrimaryDnsServer = _UsdDhcpLocalServerPoolPrimaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 7),
    _UsdDhcpLocalServerPoolPrimaryDnsServer_Type()
)
usdDhcpLocalServerPoolPrimaryDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolPrimaryDnsServer.setStatus("current")


class _UsdDhcpLocalServerPoolSecondaryDnsServer_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolSecondaryDnsServer based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolSecondaryDnsServer_Object = MibTableColumn
usdDhcpLocalServerPoolSecondaryDnsServer = _UsdDhcpLocalServerPoolSecondaryDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 8),
    _UsdDhcpLocalServerPoolSecondaryDnsServer_Type()
)
usdDhcpLocalServerPoolSecondaryDnsServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolSecondaryDnsServer.setStatus("current")


class _UsdDhcpLocalServerPoolPrimaryNetBiosNameServer_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolPrimaryNetBiosNameServer based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolPrimaryNetBiosNameServer_Object = MibTableColumn
usdDhcpLocalServerPoolPrimaryNetBiosNameServer = _UsdDhcpLocalServerPoolPrimaryNetBiosNameServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 9),
    _UsdDhcpLocalServerPoolPrimaryNetBiosNameServer_Type()
)
usdDhcpLocalServerPoolPrimaryNetBiosNameServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolPrimaryNetBiosNameServer.setStatus("current")


class _UsdDhcpLocalServerPoolSecondaryNetBiosNameServer_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolSecondaryNetBiosNameServer based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolSecondaryNetBiosNameServer_Object = MibTableColumn
usdDhcpLocalServerPoolSecondaryNetBiosNameServer = _UsdDhcpLocalServerPoolSecondaryNetBiosNameServer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 10),
    _UsdDhcpLocalServerPoolSecondaryNetBiosNameServer_Type()
)
usdDhcpLocalServerPoolSecondaryNetBiosNameServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolSecondaryNetBiosNameServer.setStatus("current")


class _UsdDhcpLocalServerPoolPrimaryDefaultRouter_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolPrimaryDefaultRouter based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolPrimaryDefaultRouter_Object = MibTableColumn
usdDhcpLocalServerPoolPrimaryDefaultRouter = _UsdDhcpLocalServerPoolPrimaryDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 11),
    _UsdDhcpLocalServerPoolPrimaryDefaultRouter_Type()
)
usdDhcpLocalServerPoolPrimaryDefaultRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolPrimaryDefaultRouter.setStatus("current")


class _UsdDhcpLocalServerPoolSecondaryDefaultRouter_Type(IpAddress):
    """Custom type usdDhcpLocalServerPoolSecondaryDefaultRouter based on IpAddress"""
    defaultHexValue = "00000000"


_UsdDhcpLocalServerPoolSecondaryDefaultRouter_Object = MibTableColumn
usdDhcpLocalServerPoolSecondaryDefaultRouter = _UsdDhcpLocalServerPoolSecondaryDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 12),
    _UsdDhcpLocalServerPoolSecondaryDefaultRouter_Type()
)
usdDhcpLocalServerPoolSecondaryDefaultRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolSecondaryDefaultRouter.setStatus("current")
_UsdDhcpLocalServerPoolRowStatus_Type = RowStatus
_UsdDhcpLocalServerPoolRowStatus_Object = MibTableColumn
usdDhcpLocalServerPoolRowStatus = _UsdDhcpLocalServerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 13),
    _UsdDhcpLocalServerPoolRowStatus_Type()
)
usdDhcpLocalServerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolRowStatus.setStatus("current")
_UsdDhcpLocalServerPoolLinkName_Type = UsdDhcpLocalServerPoolName
_UsdDhcpLocalServerPoolLinkName_Object = MibTableColumn
usdDhcpLocalServerPoolLinkName = _UsdDhcpLocalServerPoolLinkName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 3, 1, 1, 14),
    _UsdDhcpLocalServerPoolLinkName_Type()
)
usdDhcpLocalServerPoolLinkName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerPoolLinkName.setStatus("current")
_UsdDhcpLocalServerAttributes_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerAttributes = _UsdDhcpLocalServerAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4)
)
_UsdDhcpLocalServerAttributesMode_Type = UsdDhcpLocalServerModeType
_UsdDhcpLocalServerAttributesMode_Object = MibScalar
usdDhcpLocalServerAttributesMode = _UsdDhcpLocalServerAttributesMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 4, 1),
    _UsdDhcpLocalServerAttributesMode_Type()
)
usdDhcpLocalServerAttributesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerAttributesMode.setStatus("current")
_UsdDhcpLocalServerReserves_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerReserves = _UsdDhcpLocalServerReserves_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5)
)
_UsdDhcpLocalServerReservesTable_Object = MibTable
usdDhcpLocalServerReservesTable = _UsdDhcpLocalServerReservesTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerReservesTable.setStatus("current")
_UsdDhcpLocalServerReservesEntry_Object = MibTableRow
usdDhcpLocalServerReservesEntry = _UsdDhcpLocalServerReservesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1)
)
usdDhcpLocalServerReservesEntry.setIndexNames(
    (0, "Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerReservesEntryIpAddress"),
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerReservesEntry.setStatus("current")
_UsdDhcpLocalServerReservesEntryIpAddress_Type = IpAddress
_UsdDhcpLocalServerReservesEntryIpAddress_Object = MibTableColumn
usdDhcpLocalServerReservesEntryIpAddress = _UsdDhcpLocalServerReservesEntryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 1),
    _UsdDhcpLocalServerReservesEntryIpAddress_Type()
)
usdDhcpLocalServerReservesEntryIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDhcpLocalServerReservesEntryIpAddress.setStatus("current")
_UsdDhcpLocalServerReservesEntryPoolName_Type = UsdDhcpLocalServerPoolName
_UsdDhcpLocalServerReservesEntryPoolName_Object = MibTableColumn
usdDhcpLocalServerReservesEntryPoolName = _UsdDhcpLocalServerReservesEntryPoolName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 2),
    _UsdDhcpLocalServerReservesEntryPoolName_Type()
)
usdDhcpLocalServerReservesEntryPoolName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerReservesEntryPoolName.setStatus("current")
_UsdDhcpLocalServerReservesEntryPhysAddress_Type = UsdDhcpLocalServerPhysAddressString
_UsdDhcpLocalServerReservesEntryPhysAddress_Object = MibTableColumn
usdDhcpLocalServerReservesEntryPhysAddress = _UsdDhcpLocalServerReservesEntryPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 3),
    _UsdDhcpLocalServerReservesEntryPhysAddress_Type()
)
usdDhcpLocalServerReservesEntryPhysAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerReservesEntryPhysAddress.setStatus("current")
_UsdDhcpLocalServerReservesEntryRowStatus_Type = RowStatus
_UsdDhcpLocalServerReservesEntryRowStatus_Object = MibTableColumn
usdDhcpLocalServerReservesEntryRowStatus = _UsdDhcpLocalServerReservesEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 5, 1, 1, 4),
    _UsdDhcpLocalServerReservesEntryRowStatus_Type()
)
usdDhcpLocalServerReservesEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerReservesEntryRowStatus.setStatus("current")
_UsdDhcpLocalServerCableModemServers_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerCableModemServers = _UsdDhcpLocalServerCableModemServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6)
)
_UsdDhcpLocalServerCableModemServerTable_Object = MibTable
usdDhcpLocalServerCableModemServerTable = _UsdDhcpLocalServerCableModemServerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1)
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemServerTable.setStatus("current")
_UsdDhcpLocalServerCableModemServerEntry_Object = MibTableRow
usdDhcpLocalServerCableModemServerEntry = _UsdDhcpLocalServerCableModemServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1, 1)
)
usdDhcpLocalServerCableModemServerEntry.setIndexNames(
    (0, "Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemServerEntryAddress"),
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemServerEntry.setStatus("current")
_UsdDhcpLocalServerCableModemServerEntryAddress_Type = IpAddress
_UsdDhcpLocalServerCableModemServerEntryAddress_Object = MibTableColumn
usdDhcpLocalServerCableModemServerEntryAddress = _UsdDhcpLocalServerCableModemServerEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1, 1, 1),
    _UsdDhcpLocalServerCableModemServerEntryAddress_Type()
)
usdDhcpLocalServerCableModemServerEntryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemServerEntryAddress.setStatus("current")
_UsdDhcpLocalServerCableModemServerEntryRowStatus_Type = RowStatus
_UsdDhcpLocalServerCableModemServerEntryRowStatus_Object = MibTableColumn
usdDhcpLocalServerCableModemServerEntryRowStatus = _UsdDhcpLocalServerCableModemServerEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 6, 1, 1, 2),
    _UsdDhcpLocalServerCableModemServerEntryRowStatus_Type()
)
usdDhcpLocalServerCableModemServerEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemServerEntryRowStatus.setStatus("current")
_UsdDhcpLocalServerCableModemStatistics_ObjectIdentity = ObjectIdentity
usdDhcpLocalServerCableModemStatistics = _UsdDhcpLocalServerCableModemStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7)
)
_UsdDhcpLocalServerCableModemRequestIn_Type = Counter32
_UsdDhcpLocalServerCableModemRequestIn_Object = MibScalar
usdDhcpLocalServerCableModemRequestIn = _UsdDhcpLocalServerCableModemRequestIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 1),
    _UsdDhcpLocalServerCableModemRequestIn_Type()
)
usdDhcpLocalServerCableModemRequestIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemRequestIn.setStatus("current")
_UsdDhcpLocalServerCableModemResponseIn_Type = Counter32
_UsdDhcpLocalServerCableModemResponseIn_Object = MibScalar
usdDhcpLocalServerCableModemResponseIn = _UsdDhcpLocalServerCableModemResponseIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 2),
    _UsdDhcpLocalServerCableModemResponseIn_Type()
)
usdDhcpLocalServerCableModemResponseIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemResponseIn.setStatus("current")
_UsdDhcpLocalServerCableModemRequestOut_Type = Counter32
_UsdDhcpLocalServerCableModemRequestOut_Object = MibScalar
usdDhcpLocalServerCableModemRequestOut = _UsdDhcpLocalServerCableModemRequestOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 3),
    _UsdDhcpLocalServerCableModemRequestOut_Type()
)
usdDhcpLocalServerCableModemRequestOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemRequestOut.setStatus("current")
_UsdDhcpLocalServerCableModemResponseOut_Type = Counter32
_UsdDhcpLocalServerCableModemResponseOut_Object = MibScalar
usdDhcpLocalServerCableModemResponseOut = _UsdDhcpLocalServerCableModemResponseOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 4),
    _UsdDhcpLocalServerCableModemResponseOut_Type()
)
usdDhcpLocalServerCableModemResponseOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemResponseOut.setStatus("current")
_UsdDhcpLocalServerCableModemRequestDropped_Type = Counter32
_UsdDhcpLocalServerCableModemRequestDropped_Object = MibScalar
usdDhcpLocalServerCableModemRequestDropped = _UsdDhcpLocalServerCableModemRequestDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 5),
    _UsdDhcpLocalServerCableModemRequestDropped_Type()
)
usdDhcpLocalServerCableModemRequestDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemRequestDropped.setStatus("current")
_UsdDhcpLocalServerCableModemResponseDropped_Type = Counter32
_UsdDhcpLocalServerCableModemResponseDropped_Object = MibScalar
usdDhcpLocalServerCableModemResponseDropped = _UsdDhcpLocalServerCableModemResponseDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 6),
    _UsdDhcpLocalServerCableModemResponseDropped_Type()
)
usdDhcpLocalServerCableModemResponseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemResponseDropped.setStatus("current")
_UsdDhcpLocalServerCableModemRequestBad_Type = Counter32
_UsdDhcpLocalServerCableModemRequestBad_Object = MibScalar
usdDhcpLocalServerCableModemRequestBad = _UsdDhcpLocalServerCableModemRequestBad_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 7),
    _UsdDhcpLocalServerCableModemRequestBad_Type()
)
usdDhcpLocalServerCableModemRequestBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemRequestBad.setStatus("current")
_UsdDhcpLocalServerCableModemResponseBad_Type = Counter32
_UsdDhcpLocalServerCableModemResponseBad_Object = MibScalar
usdDhcpLocalServerCableModemResponseBad = _UsdDhcpLocalServerCableModemResponseBad_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 8),
    _UsdDhcpLocalServerCableModemResponseBad_Type()
)
usdDhcpLocalServerCableModemResponseBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemResponseBad.setStatus("current")
_UsdDhcpLocalServerCableModemRequestDeleted_Type = Counter32
_UsdDhcpLocalServerCableModemRequestDeleted_Object = MibScalar
usdDhcpLocalServerCableModemRequestDeleted = _UsdDhcpLocalServerCableModemRequestDeleted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 9),
    _UsdDhcpLocalServerCableModemRequestDeleted_Type()
)
usdDhcpLocalServerCableModemRequestDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemRequestDeleted.setStatus("current")
_UsdDhcpLocalServerCableModemPacketsIn_Type = Counter32
_UsdDhcpLocalServerCableModemPacketsIn_Object = MibScalar
usdDhcpLocalServerCableModemPacketsIn = _UsdDhcpLocalServerCableModemPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 10),
    _UsdDhcpLocalServerCableModemPacketsIn_Type()
)
usdDhcpLocalServerCableModemPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemPacketsIn.setStatus("current")
_UsdDhcpLocalServerCableModemPacketsOut_Type = Counter32
_UsdDhcpLocalServerCableModemPacketsOut_Object = MibScalar
usdDhcpLocalServerCableModemPacketsOut = _UsdDhcpLocalServerCableModemPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 11),
    _UsdDhcpLocalServerCableModemPacketsOut_Type()
)
usdDhcpLocalServerCableModemPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemPacketsOut.setStatus("current")
_UsdDhcpLocalServerCableModemPacketsDropped_Type = Counter32
_UsdDhcpLocalServerCableModemPacketsDropped_Object = MibScalar
usdDhcpLocalServerCableModemPacketsDropped = _UsdDhcpLocalServerCableModemPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 1, 3, 7, 12),
    _UsdDhcpLocalServerCableModemPacketsDropped_Type()
)
usdDhcpLocalServerCableModemPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDhcpLocalServerCableModemPacketsDropped.setStatus("current")
_UsdDhcpMIBConformance_ObjectIdentity = ObjectIdentity
usdDhcpMIBConformance = _UsdDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4)
)
_UsdDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
usdDhcpMIBCompliances = _UsdDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1)
)
_UsdDhcpMIBGroups_ObjectIdentity = ObjectIdentity
usdDhcpMIBGroups = _UsdDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2)
)

# Managed Objects groups

usdDhcpRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 1)
)
usdDhcpRelayGroup.setObjects(
      *(("Unisphere-Data-DHCP-MIB", "usdDhcpRelayAgentInfoEnable"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayBadMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayUnknownMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayAgentInfoAlreadyPresents"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayGatewayAddrSpoofs"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    usdDhcpRelayGroup.setStatus("deprecated")

usdDhcpProxyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 2)
)
usdDhcpProxyGroup.setObjects(
      *(("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientUnknownServers"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerRowStatus"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerAdminStatus"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerOperStatus"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerLeases"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerDiscovers"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerOffers"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerRequests"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerAcks"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerNaks"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerDeclines"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerReleases"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerInforms"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerBadMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpProxyClientServerUnknownMessages"))
)
if mibBuilder.loadTexts:
    usdDhcpProxyGroup.setStatus("current")

usdDhcpLocalServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 3)
)
usdDhcpLocalServerGroup.setObjects(
      *(("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerMemUsage"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerNumBindings"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxDiscovers"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxAccepts"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxRenews"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxDeclines"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxReleases"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxInforms"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerTxOffers"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerTxAcks"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerTxNaks"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerUnknownMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBadMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPacketsIn"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPacketsOut"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBindingsPhysAddress"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBindingsInfinite"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBindingsExpireTime"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolDomainName"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolNetworkIpAddress"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolNetworkMask"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolNetBiosNodeType"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolLeaseTime"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolPrimaryDnsServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolSecondaryDnsServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolRowStatus"))
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerGroup.setStatus("obsolete")

usdDhcpLocalServerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 4)
)
usdDhcpLocalServerGroup2.setObjects(
      *(("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerMemUsage"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerNumBindings"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxDiscovers"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxAccepts"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxRenews"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxDeclines"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxReleases"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerRxInforms"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerTxOffers"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerTxAcks"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerTxNaks"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerUnknownMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBadMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPacketsIn"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPacketsOut"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBindingsPhysAddress"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBindingsInfinite"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerBindingsExpireTime"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolDomainName"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolNetworkIpAddress"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolNetworkMask"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolNetBiosNodeType"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolLeaseTime"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolPrimaryDnsServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolSecondaryDnsServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolPrimaryNetBiosNameServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolSecondaryNetBiosNameServer"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolPrimaryDefaultRouter"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolSecondaryDefaultRouter"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolRowStatus"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerPoolLinkName"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerAttributesMode"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerReservesEntryPoolName"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerReservesEntryPhysAddress"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerReservesEntryRowStatus"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemServerEntryRowStatus"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemRequestIn"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemResponseIn"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemRequestOut"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemResponseOut"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemRequestDropped"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemResponseDropped"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemRequestBad"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemResponseBad"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemRequestDeleted"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemPacketsIn"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemPacketsOut"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpLocalServerCableModemPacketsDropped"))
)
if mibBuilder.loadTexts:
    usdDhcpLocalServerGroup2.setStatus("current")

usdDhcpRelayGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 2, 5)
)
usdDhcpRelayGroup2.setObjects(
      *(("Unisphere-Data-DHCP-MIB", "usdDhcpRelayBadMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayUnknownMessages"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayAgentInfoAlreadyPresents"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayGatewayAddrSpoofs"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayAgentCircuitIdEnable"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayAgentRemoteIdEnable"),
        ("Unisphere-Data-DHCP-MIB", "usdDhcpRelayServerRowStatus"))
)
if mibBuilder.loadTexts:
    usdDhcpRelayGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdDhcpRelayCompliance.setStatus(
        "obsolete"
    )

usdDhcpProxyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdDhcpProxyCompliance.setStatus(
        "obsolete"
    )

usdDhcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdDhcpCompliance.setStatus(
        "obsolete"
    )

usdDhcpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 22, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdDhcpCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DHCP-MIB",
    **{"UsdDhcpLocalServerPoolName": UsdDhcpLocalServerPoolName,
       "UsdDhcpLocalServerPoolDomainName": UsdDhcpLocalServerPoolDomainName,
       "UsdDhcpLocalServerPoolNetBiosNodeType": UsdDhcpLocalServerPoolNetBiosNodeType,
       "UsdDhcpLocalServerModeType": UsdDhcpLocalServerModeType,
       "UsdDhcpLocalServerPhysAddressString": UsdDhcpLocalServerPhysAddressString,
       "usdDhcpMIB": usdDhcpMIB,
       "usdDhcpObjects": usdDhcpObjects,
       "usdDhcpRelay": usdDhcpRelay,
       "usdDhcpRelayScalars": usdDhcpRelayScalars,
       "usdDhcpRelayAgentInfoEnable": usdDhcpRelayAgentInfoEnable,
       "usdDhcpRelayBadMessages": usdDhcpRelayBadMessages,
       "usdDhcpRelayUnknownMessages": usdDhcpRelayUnknownMessages,
       "usdDhcpRelayAgentInfoAlreadyPresents": usdDhcpRelayAgentInfoAlreadyPresents,
       "usdDhcpRelayGatewayAddrSpoofs": usdDhcpRelayGatewayAddrSpoofs,
       "usdDhcpRelayAgentCircuitIdEnable": usdDhcpRelayAgentCircuitIdEnable,
       "usdDhcpRelayAgentRemoteIdEnable": usdDhcpRelayAgentRemoteIdEnable,
       "usdDhcpRelayServerTable": usdDhcpRelayServerTable,
       "usdDhcpRelayServerEntry": usdDhcpRelayServerEntry,
       "usdDhcpRelayServerAddress": usdDhcpRelayServerAddress,
       "usdDhcpRelayServerRowStatus": usdDhcpRelayServerRowStatus,
       "usdDhcpProxy": usdDhcpProxy,
       "usdDhcpProxyClient": usdDhcpProxyClient,
       "usdDhcpProxyClientScalars": usdDhcpProxyClientScalars,
       "usdDhcpProxyClientUnknownServers": usdDhcpProxyClientUnknownServers,
       "usdDhcpProxyClientServerTable": usdDhcpProxyClientServerTable,
       "usdDhcpProxyClientServerEntry": usdDhcpProxyClientServerEntry,
       "usdDhcpProxyClientServerAddress": usdDhcpProxyClientServerAddress,
       "usdDhcpProxyClientServerRowStatus": usdDhcpProxyClientServerRowStatus,
       "usdDhcpProxyClientServerAdminStatus": usdDhcpProxyClientServerAdminStatus,
       "usdDhcpProxyClientServerOperStatus": usdDhcpProxyClientServerOperStatus,
       "usdDhcpProxyClientServerLeases": usdDhcpProxyClientServerLeases,
       "usdDhcpProxyClientServerDiscovers": usdDhcpProxyClientServerDiscovers,
       "usdDhcpProxyClientServerOffers": usdDhcpProxyClientServerOffers,
       "usdDhcpProxyClientServerRequests": usdDhcpProxyClientServerRequests,
       "usdDhcpProxyClientServerAcks": usdDhcpProxyClientServerAcks,
       "usdDhcpProxyClientServerNaks": usdDhcpProxyClientServerNaks,
       "usdDhcpProxyClientServerDeclines": usdDhcpProxyClientServerDeclines,
       "usdDhcpProxyClientServerReleases": usdDhcpProxyClientServerReleases,
       "usdDhcpProxyClientServerInforms": usdDhcpProxyClientServerInforms,
       "usdDhcpProxyClientServerBadMessages": usdDhcpProxyClientServerBadMessages,
       "usdDhcpProxyClientServerUnknownMessages": usdDhcpProxyClientServerUnknownMessages,
       "usdDhcpProxyServer": usdDhcpProxyServer,
       "usdDhcpLocalServerObjects": usdDhcpLocalServerObjects,
       "usdDhcpLocalServerStatistics": usdDhcpLocalServerStatistics,
       "usdDhcpLocalServerMemUsage": usdDhcpLocalServerMemUsage,
       "usdDhcpLocalServerNumBindings": usdDhcpLocalServerNumBindings,
       "usdDhcpLocalServerRxDiscovers": usdDhcpLocalServerRxDiscovers,
       "usdDhcpLocalServerRxAccepts": usdDhcpLocalServerRxAccepts,
       "usdDhcpLocalServerRxRenews": usdDhcpLocalServerRxRenews,
       "usdDhcpLocalServerRxDeclines": usdDhcpLocalServerRxDeclines,
       "usdDhcpLocalServerRxReleases": usdDhcpLocalServerRxReleases,
       "usdDhcpLocalServerRxInforms": usdDhcpLocalServerRxInforms,
       "usdDhcpLocalServerTxOffers": usdDhcpLocalServerTxOffers,
       "usdDhcpLocalServerTxAcks": usdDhcpLocalServerTxAcks,
       "usdDhcpLocalServerTxNaks": usdDhcpLocalServerTxNaks,
       "usdDhcpLocalServerUnknownMessages": usdDhcpLocalServerUnknownMessages,
       "usdDhcpLocalServerBadMessages": usdDhcpLocalServerBadMessages,
       "usdDhcpLocalServerPacketsIn": usdDhcpLocalServerPacketsIn,
       "usdDhcpLocalServerPacketsOut": usdDhcpLocalServerPacketsOut,
       "usdDhcpLocalServerBindings": usdDhcpLocalServerBindings,
       "usdDhcpLocalServerBindingsTable": usdDhcpLocalServerBindingsTable,
       "usdDhcpLocalServerBindingsEntry": usdDhcpLocalServerBindingsEntry,
       "usdDhcpLocalServerBindingsIpAddress": usdDhcpLocalServerBindingsIpAddress,
       "usdDhcpLocalServerBindingsPhysAddress": usdDhcpLocalServerBindingsPhysAddress,
       "usdDhcpLocalServerBindingsInfinite": usdDhcpLocalServerBindingsInfinite,
       "usdDhcpLocalServerBindingsExpireTime": usdDhcpLocalServerBindingsExpireTime,
       "usdDhcpLocalServerPool": usdDhcpLocalServerPool,
       "usdDhcpLocalServerPoolTable": usdDhcpLocalServerPoolTable,
       "usdDhcpLocalServerPoolEntry": usdDhcpLocalServerPoolEntry,
       "usdDhcpLocalServerPoolName": usdDhcpLocalServerPoolName,
       "usdDhcpLocalServerPoolDomainName": usdDhcpLocalServerPoolDomainName,
       "usdDhcpLocalServerPoolNetworkIpAddress": usdDhcpLocalServerPoolNetworkIpAddress,
       "usdDhcpLocalServerPoolNetworkMask": usdDhcpLocalServerPoolNetworkMask,
       "usdDhcpLocalServerPoolNetBiosNodeType": usdDhcpLocalServerPoolNetBiosNodeType,
       "usdDhcpLocalServerPoolLeaseTime": usdDhcpLocalServerPoolLeaseTime,
       "usdDhcpLocalServerPoolPrimaryDnsServer": usdDhcpLocalServerPoolPrimaryDnsServer,
       "usdDhcpLocalServerPoolSecondaryDnsServer": usdDhcpLocalServerPoolSecondaryDnsServer,
       "usdDhcpLocalServerPoolPrimaryNetBiosNameServer": usdDhcpLocalServerPoolPrimaryNetBiosNameServer,
       "usdDhcpLocalServerPoolSecondaryNetBiosNameServer": usdDhcpLocalServerPoolSecondaryNetBiosNameServer,
       "usdDhcpLocalServerPoolPrimaryDefaultRouter": usdDhcpLocalServerPoolPrimaryDefaultRouter,
       "usdDhcpLocalServerPoolSecondaryDefaultRouter": usdDhcpLocalServerPoolSecondaryDefaultRouter,
       "usdDhcpLocalServerPoolRowStatus": usdDhcpLocalServerPoolRowStatus,
       "usdDhcpLocalServerPoolLinkName": usdDhcpLocalServerPoolLinkName,
       "usdDhcpLocalServerAttributes": usdDhcpLocalServerAttributes,
       "usdDhcpLocalServerAttributesMode": usdDhcpLocalServerAttributesMode,
       "usdDhcpLocalServerReserves": usdDhcpLocalServerReserves,
       "usdDhcpLocalServerReservesTable": usdDhcpLocalServerReservesTable,
       "usdDhcpLocalServerReservesEntry": usdDhcpLocalServerReservesEntry,
       "usdDhcpLocalServerReservesEntryIpAddress": usdDhcpLocalServerReservesEntryIpAddress,
       "usdDhcpLocalServerReservesEntryPoolName": usdDhcpLocalServerReservesEntryPoolName,
       "usdDhcpLocalServerReservesEntryPhysAddress": usdDhcpLocalServerReservesEntryPhysAddress,
       "usdDhcpLocalServerReservesEntryRowStatus": usdDhcpLocalServerReservesEntryRowStatus,
       "usdDhcpLocalServerCableModemServers": usdDhcpLocalServerCableModemServers,
       "usdDhcpLocalServerCableModemServerTable": usdDhcpLocalServerCableModemServerTable,
       "usdDhcpLocalServerCableModemServerEntry": usdDhcpLocalServerCableModemServerEntry,
       "usdDhcpLocalServerCableModemServerEntryAddress": usdDhcpLocalServerCableModemServerEntryAddress,
       "usdDhcpLocalServerCableModemServerEntryRowStatus": usdDhcpLocalServerCableModemServerEntryRowStatus,
       "usdDhcpLocalServerCableModemStatistics": usdDhcpLocalServerCableModemStatistics,
       "usdDhcpLocalServerCableModemRequestIn": usdDhcpLocalServerCableModemRequestIn,
       "usdDhcpLocalServerCableModemResponseIn": usdDhcpLocalServerCableModemResponseIn,
       "usdDhcpLocalServerCableModemRequestOut": usdDhcpLocalServerCableModemRequestOut,
       "usdDhcpLocalServerCableModemResponseOut": usdDhcpLocalServerCableModemResponseOut,
       "usdDhcpLocalServerCableModemRequestDropped": usdDhcpLocalServerCableModemRequestDropped,
       "usdDhcpLocalServerCableModemResponseDropped": usdDhcpLocalServerCableModemResponseDropped,
       "usdDhcpLocalServerCableModemRequestBad": usdDhcpLocalServerCableModemRequestBad,
       "usdDhcpLocalServerCableModemResponseBad": usdDhcpLocalServerCableModemResponseBad,
       "usdDhcpLocalServerCableModemRequestDeleted": usdDhcpLocalServerCableModemRequestDeleted,
       "usdDhcpLocalServerCableModemPacketsIn": usdDhcpLocalServerCableModemPacketsIn,
       "usdDhcpLocalServerCableModemPacketsOut": usdDhcpLocalServerCableModemPacketsOut,
       "usdDhcpLocalServerCableModemPacketsDropped": usdDhcpLocalServerCableModemPacketsDropped,
       "usdDhcpMIBConformance": usdDhcpMIBConformance,
       "usdDhcpMIBCompliances": usdDhcpMIBCompliances,
       "usdDhcpRelayCompliance": usdDhcpRelayCompliance,
       "usdDhcpProxyCompliance": usdDhcpProxyCompliance,
       "usdDhcpCompliance": usdDhcpCompliance,
       "usdDhcpCompliance2": usdDhcpCompliance2,
       "usdDhcpMIBGroups": usdDhcpMIBGroups,
       "usdDhcpRelayGroup": usdDhcpRelayGroup,
       "usdDhcpProxyGroup": usdDhcpProxyGroup,
       "usdDhcpLocalServerGroup": usdDhcpLocalServerGroup,
       "usdDhcpLocalServerGroup2": usdDhcpLocalServerGroup2,
       "usdDhcpRelayGroup2": usdDhcpRelayGroup2}
)
