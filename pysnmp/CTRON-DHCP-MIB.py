# SNMP MIB module (CTRON-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:43 2024
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

(nwIpClientServices,
 nwIpComponents,
 nwIpMibs,
 nwIpRouter) = mibBuilder.importSymbols(
    "CTRON-IP-ROUTER-MIB",
    "nwIpClientServices",
    "nwIpComponents",
    "nwIpMibs",
    "nwIpRouter")

(nwRtrProtoSuites,) = mibBuilder.importSymbols(
    "ROUTER-OIDS",
    "nwRtrProtoSuites")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtDhcp_ObjectIdentity = ObjectIdentity
ctDhcp = _CtDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2)
)
_CtDhcpServerStats_ObjectIdentity = ObjectIdentity
ctDhcpServerStats = _CtDhcpServerStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1)
)


class _CtDhcpAdminStatus_Type(Integer32):
    """Custom type ctDhcpAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CtDhcpAdminStatus_Type.__name__ = "Integer32"
_CtDhcpAdminStatus_Object = MibScalar
ctDhcpAdminStatus = _CtDhcpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 1),
    _CtDhcpAdminStatus_Type()
)
ctDhcpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpAdminStatus.setStatus("mandatory")


class _CtDhcpOperStatus_Type(Integer32):
    """Custom type ctDhcpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CtDhcpOperStatus_Type.__name__ = "Integer32"
_CtDhcpOperStatus_Object = MibScalar
ctDhcpOperStatus = _CtDhcpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 2),
    _CtDhcpOperStatus_Type()
)
ctDhcpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpOperStatus.setStatus("mandatory")
_CtDhcpDiscovers_Type = Counter32
_CtDhcpDiscovers_Object = MibScalar
ctDhcpDiscovers = _CtDhcpDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 3),
    _CtDhcpDiscovers_Type()
)
ctDhcpDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpDiscovers.setStatus("mandatory")
_CtDhcpOffers_Type = Counter32
_CtDhcpOffers_Object = MibScalar
ctDhcpOffers = _CtDhcpOffers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 4),
    _CtDhcpOffers_Type()
)
ctDhcpOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpOffers.setStatus("mandatory")
_CtDhcpRequests_Type = Counter32
_CtDhcpRequests_Object = MibScalar
ctDhcpRequests = _CtDhcpRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 5),
    _CtDhcpRequests_Type()
)
ctDhcpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpRequests.setStatus("mandatory")
_CtDhcpDeclines_Type = Counter32
_CtDhcpDeclines_Object = MibScalar
ctDhcpDeclines = _CtDhcpDeclines_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 6),
    _CtDhcpDeclines_Type()
)
ctDhcpDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpDeclines.setStatus("mandatory")
_CtDhcpReleases_Type = Counter32
_CtDhcpReleases_Object = MibScalar
ctDhcpReleases = _CtDhcpReleases_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 7),
    _CtDhcpReleases_Type()
)
ctDhcpReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpReleases.setStatus("mandatory")
_CtDhcpAcks_Type = Counter32
_CtDhcpAcks_Object = MibScalar
ctDhcpAcks = _CtDhcpAcks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 8),
    _CtDhcpAcks_Type()
)
ctDhcpAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpAcks.setStatus("mandatory")
_CtDhcpNaks_Type = Counter32
_CtDhcpNaks_Object = MibScalar
ctDhcpNaks = _CtDhcpNaks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 9),
    _CtDhcpNaks_Type()
)
ctDhcpNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpNaks.setStatus("mandatory")
_CtDhcpOtherServers_Type = Counter32
_CtDhcpOtherServers_Object = MibScalar
ctDhcpOtherServers = _CtDhcpOtherServers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 10),
    _CtDhcpOtherServers_Type()
)
ctDhcpOtherServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpOtherServers.setStatus("mandatory")
_CtDhcpProtocolErrors_Type = Counter32
_CtDhcpProtocolErrors_Object = MibScalar
ctDhcpProtocolErrors = _CtDhcpProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 11),
    _CtDhcpProtocolErrors_Type()
)
ctDhcpProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpProtocolErrors.setStatus("mandatory")
_CtDhcpServerTime_Type = Integer32
_CtDhcpServerTime_Object = MibScalar
ctDhcpServerTime = _CtDhcpServerTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 12),
    _CtDhcpServerTime_Type()
)
ctDhcpServerTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpServerTime.setStatus("mandatory")
_CtDhcpNoOfActiveClients_Type = Integer32
_CtDhcpNoOfActiveClients_Object = MibScalar
ctDhcpNoOfActiveClients = _CtDhcpNoOfActiveClients_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 13),
    _CtDhcpNoOfActiveClients_Type()
)
ctDhcpNoOfActiveClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpNoOfActiveClients.setStatus("mandatory")
_CtDhcpReclaimIP_Type = IpAddress
_CtDhcpReclaimIP_Object = MibScalar
ctDhcpReclaimIP = _CtDhcpReclaimIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 14),
    _CtDhcpReclaimIP_Type()
)
ctDhcpReclaimIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpReclaimIP.setStatus("mandatory")
_CtDhcpInterfaceConfig_ObjectIdentity = ObjectIdentity
ctDhcpInterfaceConfig = _CtDhcpInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2)
)
_CtDhcpServerIfTable_Object = MibTable
ctDhcpServerIfTable = _CtDhcpServerIfTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctDhcpServerIfTable.setStatus("mandatory")
_CtDhcpServerIfEntry_Object = MibTableRow
ctDhcpServerIfEntry = _CtDhcpServerIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1)
)
ctDhcpServerIfEntry.setIndexNames(
    (0, "CTRON-DHCP-MIB", "ctDhcpIfIndex"),
)
if mibBuilder.loadTexts:
    ctDhcpServerIfEntry.setStatus("mandatory")
_CtDhcpIfIndex_Type = Integer32
_CtDhcpIfIndex_Object = MibTableColumn
ctDhcpIfIndex = _CtDhcpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 1),
    _CtDhcpIfIndex_Type()
)
ctDhcpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpIfIndex.setStatus("mandatory")


class _CtDhcpIfAdminStatus_Type(Integer32):
    """Custom type ctDhcpIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_CtDhcpIfAdminStatus_Type.__name__ = "Integer32"
_CtDhcpIfAdminStatus_Object = MibTableColumn
ctDhcpIfAdminStatus = _CtDhcpIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 2),
    _CtDhcpIfAdminStatus_Type()
)
ctDhcpIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfAdminStatus.setStatus("mandatory")


class _CtDhcpIfOperStatus_Type(Integer32):
    """Custom type ctDhcpIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("invalid-config", 3))
    )


_CtDhcpIfOperStatus_Type.__name__ = "Integer32"
_CtDhcpIfOperStatus_Object = MibTableColumn
ctDhcpIfOperStatus = _CtDhcpIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 3),
    _CtDhcpIfOperStatus_Type()
)
ctDhcpIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpIfOperStatus.setStatus("mandatory")
_CtDhcpIfServerAddress_Type = IpAddress
_CtDhcpIfServerAddress_Object = MibTableColumn
ctDhcpIfServerAddress = _CtDhcpIfServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 4),
    _CtDhcpIfServerAddress_Type()
)
ctDhcpIfServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpIfServerAddress.setStatus("mandatory")
_CtDhcpIfNetworkAddress_Type = IpAddress
_CtDhcpIfNetworkAddress_Object = MibTableColumn
ctDhcpIfNetworkAddress = _CtDhcpIfNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 5),
    _CtDhcpIfNetworkAddress_Type()
)
ctDhcpIfNetworkAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfNetworkAddress.setStatus("mandatory")
_CtDhcpIfSubnetMask_Type = IpAddress
_CtDhcpIfSubnetMask_Object = MibTableColumn
ctDhcpIfSubnetMask = _CtDhcpIfSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 6),
    _CtDhcpIfSubnetMask_Type()
)
ctDhcpIfSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfSubnetMask.setStatus("mandatory")
_CtDhcpIfLowestaddress_Type = IpAddress
_CtDhcpIfLowestaddress_Object = MibTableColumn
ctDhcpIfLowestaddress = _CtDhcpIfLowestaddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 7),
    _CtDhcpIfLowestaddress_Type()
)
ctDhcpIfLowestaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfLowestaddress.setStatus("mandatory")
_CtDhcpIfHighestAddress_Type = IpAddress
_CtDhcpIfHighestAddress_Object = MibTableColumn
ctDhcpIfHighestAddress = _CtDhcpIfHighestAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 8),
    _CtDhcpIfHighestAddress_Type()
)
ctDhcpIfHighestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfHighestAddress.setStatus("mandatory")
_CtDhcpIfAddressesUsed_Type = Integer32
_CtDhcpIfAddressesUsed_Object = MibTableColumn
ctDhcpIfAddressesUsed = _CtDhcpIfAddressesUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 9),
    _CtDhcpIfAddressesUsed_Type()
)
ctDhcpIfAddressesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpIfAddressesUsed.setStatus("mandatory")
_CtDhcpIfAddressesFree_Type = Integer32
_CtDhcpIfAddressesFree_Object = MibTableColumn
ctDhcpIfAddressesFree = _CtDhcpIfAddressesFree_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 10),
    _CtDhcpIfAddressesFree_Type()
)
ctDhcpIfAddressesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpIfAddressesFree.setStatus("mandatory")
_CtDhcpIfLeasePeriod_Type = Integer32
_CtDhcpIfLeasePeriod_Object = MibTableColumn
ctDhcpIfLeasePeriod = _CtDhcpIfLeasePeriod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 11),
    _CtDhcpIfLeasePeriod_Type()
)
ctDhcpIfLeasePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfLeasePeriod.setStatus("mandatory")
_CtDhcpIfDefaultGateway_Type = IpAddress
_CtDhcpIfDefaultGateway_Object = MibTableColumn
ctDhcpIfDefaultGateway = _CtDhcpIfDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 12),
    _CtDhcpIfDefaultGateway_Type()
)
ctDhcpIfDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfDefaultGateway.setStatus("mandatory")
_CtDhcpIfDomainNameServer_Type = IpAddress
_CtDhcpIfDomainNameServer_Object = MibTableColumn
ctDhcpIfDomainNameServer = _CtDhcpIfDomainNameServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 13),
    _CtDhcpIfDomainNameServer_Type()
)
ctDhcpIfDomainNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfDomainNameServer.setStatus("mandatory")
_CtDhcpIfDomainName_Type = OctetString
_CtDhcpIfDomainName_Object = MibTableColumn
ctDhcpIfDomainName = _CtDhcpIfDomainName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 14),
    _CtDhcpIfDomainName_Type()
)
ctDhcpIfDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfDomainName.setStatus("mandatory")
_CtDhcpIfWINServer_Type = IpAddress
_CtDhcpIfWINServer_Object = MibTableColumn
ctDhcpIfWINServer = _CtDhcpIfWINServer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 15),
    _CtDhcpIfWINServer_Type()
)
ctDhcpIfWINServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDhcpIfWINServer.setStatus("mandatory")
_CtDhcpClientStatusTable_ObjectIdentity = ObjectIdentity
ctDhcpClientStatusTable = _CtDhcpClientStatusTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3)
)
_CtDhcpClientStatsTable_Object = MibTable
ctDhcpClientStatsTable = _CtDhcpClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ctDhcpClientStatsTable.setStatus("mandatory")
_CtDhcpClientStatsEntry_Object = MibTableRow
ctDhcpClientStatsEntry = _CtDhcpClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1)
)
ctDhcpClientStatsEntry.setIndexNames(
    (0, "CTRON-DHCP-MIB", "ctDhcpClientStatsID"),
)
if mibBuilder.loadTexts:
    ctDhcpClientStatsEntry.setStatus("mandatory")
_CtDhcpClientStatsID_Type = Integer32
_CtDhcpClientStatsID_Object = MibTableColumn
ctDhcpClientStatsID = _CtDhcpClientStatsID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 1),
    _CtDhcpClientStatsID_Type()
)
ctDhcpClientStatsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpClientStatsID.setStatus("mandatory")
_CtDhcpClientName_Type = OctetString
_CtDhcpClientName_Object = MibTableColumn
ctDhcpClientName = _CtDhcpClientName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 2),
    _CtDhcpClientName_Type()
)
ctDhcpClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpClientName.setStatus("mandatory")
_CtDhcpClientIP_Type = IpAddress
_CtDhcpClientIP_Object = MibTableColumn
ctDhcpClientIP = _CtDhcpClientIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 3),
    _CtDhcpClientIP_Type()
)
ctDhcpClientIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpClientIP.setStatus("mandatory")
_CtDhcpClientID_Type = OctetString
_CtDhcpClientID_Object = MibTableColumn
ctDhcpClientID = _CtDhcpClientID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 4),
    _CtDhcpClientID_Type()
)
ctDhcpClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpClientID.setStatus("mandatory")
_CtDhcpEndOfLease_Type = Integer32
_CtDhcpEndOfLease_Object = MibTableColumn
ctDhcpEndOfLease = _CtDhcpEndOfLease_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 5),
    _CtDhcpEndOfLease_Type()
)
ctDhcpEndOfLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDhcpEndOfLease.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-DHCP-MIB",
    **{"ctDhcp": ctDhcp,
       "ctDhcpServerStats": ctDhcpServerStats,
       "ctDhcpAdminStatus": ctDhcpAdminStatus,
       "ctDhcpOperStatus": ctDhcpOperStatus,
       "ctDhcpDiscovers": ctDhcpDiscovers,
       "ctDhcpOffers": ctDhcpOffers,
       "ctDhcpRequests": ctDhcpRequests,
       "ctDhcpDeclines": ctDhcpDeclines,
       "ctDhcpReleases": ctDhcpReleases,
       "ctDhcpAcks": ctDhcpAcks,
       "ctDhcpNaks": ctDhcpNaks,
       "ctDhcpOtherServers": ctDhcpOtherServers,
       "ctDhcpProtocolErrors": ctDhcpProtocolErrors,
       "ctDhcpServerTime": ctDhcpServerTime,
       "ctDhcpNoOfActiveClients": ctDhcpNoOfActiveClients,
       "ctDhcpReclaimIP": ctDhcpReclaimIP,
       "ctDhcpInterfaceConfig": ctDhcpInterfaceConfig,
       "ctDhcpServerIfTable": ctDhcpServerIfTable,
       "ctDhcpServerIfEntry": ctDhcpServerIfEntry,
       "ctDhcpIfIndex": ctDhcpIfIndex,
       "ctDhcpIfAdminStatus": ctDhcpIfAdminStatus,
       "ctDhcpIfOperStatus": ctDhcpIfOperStatus,
       "ctDhcpIfServerAddress": ctDhcpIfServerAddress,
       "ctDhcpIfNetworkAddress": ctDhcpIfNetworkAddress,
       "ctDhcpIfSubnetMask": ctDhcpIfSubnetMask,
       "ctDhcpIfLowestaddress": ctDhcpIfLowestaddress,
       "ctDhcpIfHighestAddress": ctDhcpIfHighestAddress,
       "ctDhcpIfAddressesUsed": ctDhcpIfAddressesUsed,
       "ctDhcpIfAddressesFree": ctDhcpIfAddressesFree,
       "ctDhcpIfLeasePeriod": ctDhcpIfLeasePeriod,
       "ctDhcpIfDefaultGateway": ctDhcpIfDefaultGateway,
       "ctDhcpIfDomainNameServer": ctDhcpIfDomainNameServer,
       "ctDhcpIfDomainName": ctDhcpIfDomainName,
       "ctDhcpIfWINServer": ctDhcpIfWINServer,
       "ctDhcpClientStatusTable": ctDhcpClientStatusTable,
       "ctDhcpClientStatsTable": ctDhcpClientStatsTable,
       "ctDhcpClientStatsEntry": ctDhcpClientStatsEntry,
       "ctDhcpClientStatsID": ctDhcpClientStatsID,
       "ctDhcpClientName": ctDhcpClientName,
       "ctDhcpClientIP": ctDhcpClientIP,
       "ctDhcpClientID": ctDhcpClientID,
       "ctDhcpEndOfLease": ctDhcpEndOfLease}
)
