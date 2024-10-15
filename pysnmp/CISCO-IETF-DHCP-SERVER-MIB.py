# SNMP MIB module (CISCO-IETF-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-DHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:29 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddressIPv4,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressPrefixLength")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIetfDhcpSrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102)
)
ciscoIetfDhcpSrvMIB.setRevisions(
        ("2007-03-27 00:00",
         "2007-02-14 12:00",
         "2004-03-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDhcpv4PhysicalAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1d,1d,1x:1x:1x:1x:1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(18, 18),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIetfDhcpv4SrvMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIetfDhcpv4SrvMIBNotifs = _CiscoIetfDhcpv4SrvMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0)
)
_CDhcpv4ServerNotificationPrefix_ObjectIdentity = ObjectIdentity
cDhcpv4ServerNotificationPrefix = _CDhcpv4ServerNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2)
)
_CDhcpv4ServerNotifications_ObjectIdentity = ObjectIdentity
cDhcpv4ServerNotifications = _CDhcpv4ServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0)
)
_CiscoIetfDhcpv4SrvMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfDhcpv4SrvMIBObjects = _CiscoIetfDhcpv4SrvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1)
)
_CDhcpv4SrvSystem_ObjectIdentity = ObjectIdentity
cDhcpv4SrvSystem = _CDhcpv4SrvSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 1)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvSystem.setStatus("current")


class _CDhcpv4SrvSystemDescr_Type(SnmpAdminString):
    """Custom type cDhcpv4SrvSystemDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CDhcpv4SrvSystemDescr_Type.__name__ = "SnmpAdminString"
_CDhcpv4SrvSystemDescr_Object = MibScalar
cDhcpv4SrvSystemDescr = _CDhcpv4SrvSystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 1, 1),
    _CDhcpv4SrvSystemDescr_Type()
)
cDhcpv4SrvSystemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4SrvSystemDescr.setStatus("current")
_CDhcpv4SrvSystemObjectID_Type = ObjectIdentifier
_CDhcpv4SrvSystemObjectID_Object = MibScalar
cDhcpv4SrvSystemObjectID = _CDhcpv4SrvSystemObjectID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 1, 2),
    _CDhcpv4SrvSystemObjectID_Type()
)
cDhcpv4SrvSystemObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4SrvSystemObjectID.setStatus("current")
_CBootpCounters_ObjectIdentity = ObjectIdentity
cBootpCounters = _CBootpCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2)
)
if mibBuilder.loadTexts:
    cBootpCounters.setStatus("current")
_CBootpCountRequests_Type = Counter32
_CBootpCountRequests_Object = MibScalar
cBootpCountRequests = _CBootpCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 1),
    _CBootpCountRequests_Type()
)
cBootpCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpCountRequests.setStatus("current")
_CBootpCountInvalids_Type = Counter32
_CBootpCountInvalids_Object = MibScalar
cBootpCountInvalids = _CBootpCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 2),
    _CBootpCountInvalids_Type()
)
cBootpCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpCountInvalids.setStatus("current")
_CBootpCountReplies_Type = Counter32
_CBootpCountReplies_Object = MibScalar
cBootpCountReplies = _CBootpCountReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 3),
    _CBootpCountReplies_Type()
)
cBootpCountReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpCountReplies.setStatus("current")
_CBootpCountDropUnknownClients_Type = Counter32
_CBootpCountDropUnknownClients_Object = MibScalar
cBootpCountDropUnknownClients = _CBootpCountDropUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 4),
    _CBootpCountDropUnknownClients_Type()
)
cBootpCountDropUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpCountDropUnknownClients.setStatus("current")
_CBootpCountDropNotServingSubnet_Type = Counter32
_CBootpCountDropNotServingSubnet_Object = MibScalar
cBootpCountDropNotServingSubnet = _CBootpCountDropNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 2, 5),
    _CBootpCountDropNotServingSubnet_Type()
)
cBootpCountDropNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpCountDropNotServingSubnet.setStatus("current")
_CDhcpv4Counters_ObjectIdentity = ObjectIdentity
cDhcpv4Counters = _CDhcpv4Counters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3)
)
if mibBuilder.loadTexts:
    cDhcpv4Counters.setStatus("current")
_CDhcpv4CountDiscovers_Type = Counter32
_CDhcpv4CountDiscovers_Object = MibScalar
cDhcpv4CountDiscovers = _CDhcpv4CountDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 1),
    _CDhcpv4CountDiscovers_Type()
)
cDhcpv4CountDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountDiscovers.setStatus("current")
_CDhcpv4CountOffers_Type = Counter32
_CDhcpv4CountOffers_Object = MibScalar
cDhcpv4CountOffers = _CDhcpv4CountOffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 2),
    _CDhcpv4CountOffers_Type()
)
cDhcpv4CountOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountOffers.setStatus("current")
_CDhcpv4CountRequests_Type = Counter32
_CDhcpv4CountRequests_Object = MibScalar
cDhcpv4CountRequests = _CDhcpv4CountRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 3),
    _CDhcpv4CountRequests_Type()
)
cDhcpv4CountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountRequests.setStatus("current")
_CDhcpv4CountDeclines_Type = Counter32
_CDhcpv4CountDeclines_Object = MibScalar
cDhcpv4CountDeclines = _CDhcpv4CountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 4),
    _CDhcpv4CountDeclines_Type()
)
cDhcpv4CountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountDeclines.setStatus("current")
_CDhcpv4CountAcks_Type = Counter32
_CDhcpv4CountAcks_Object = MibScalar
cDhcpv4CountAcks = _CDhcpv4CountAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 5),
    _CDhcpv4CountAcks_Type()
)
cDhcpv4CountAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountAcks.setStatus("current")
_CDhcpv4CountNaks_Type = Counter32
_CDhcpv4CountNaks_Object = MibScalar
cDhcpv4CountNaks = _CDhcpv4CountNaks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 6),
    _CDhcpv4CountNaks_Type()
)
cDhcpv4CountNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountNaks.setStatus("current")
_CDhcpv4CountReleases_Type = Counter32
_CDhcpv4CountReleases_Object = MibScalar
cDhcpv4CountReleases = _CDhcpv4CountReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 7),
    _CDhcpv4CountReleases_Type()
)
cDhcpv4CountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountReleases.setStatus("current")
_CDhcpv4CountInforms_Type = Counter32
_CDhcpv4CountInforms_Object = MibScalar
cDhcpv4CountInforms = _CDhcpv4CountInforms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 8),
    _CDhcpv4CountInforms_Type()
)
cDhcpv4CountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountInforms.setStatus("current")
_CDhcpv4CountInvalids_Type = Counter32
_CDhcpv4CountInvalids_Object = MibScalar
cDhcpv4CountInvalids = _CDhcpv4CountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 10),
    _CDhcpv4CountInvalids_Type()
)
cDhcpv4CountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountInvalids.setStatus("current")
_CDhcpv4CountDropUnknownClient_Type = Counter32
_CDhcpv4CountDropUnknownClient_Object = MibScalar
cDhcpv4CountDropUnknownClient = _CDhcpv4CountDropUnknownClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 11),
    _CDhcpv4CountDropUnknownClient_Type()
)
cDhcpv4CountDropUnknownClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountDropUnknownClient.setStatus("current")
_CDhcpv4CountDropNotServingSubnet_Type = Counter32
_CDhcpv4CountDropNotServingSubnet_Object = MibScalar
cDhcpv4CountDropNotServingSubnet = _CDhcpv4CountDropNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 3, 12),
    _CDhcpv4CountDropNotServingSubnet_Type()
)
cDhcpv4CountDropNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4CountDropNotServingSubnet.setStatus("current")
_CDhcpv4SrvConfiguration_ObjectIdentity = ObjectIdentity
cDhcpv4SrvConfiguration = _CDhcpv4SrvConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvConfiguration.setStatus("current")
_CDhcpv4ServerSharedNetTable_Object = MibTable
cDhcpv4ServerSharedNetTable = _CDhcpv4ServerSharedNetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetTable.setStatus("current")
_CDhcpv4ServerSharedNetEntry_Object = MibTableRow
cDhcpv4ServerSharedNetEntry = _CDhcpv4ServerSharedNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1)
)
cDhcpv4ServerSharedNetEntry.setIndexNames(
    (0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetName"),
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetEntry.setStatus("current")


class _CDhcpv4ServerSharedNetName_Type(SnmpAdminString):
    """Custom type cDhcpv4ServerSharedNetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CDhcpv4ServerSharedNetName_Type.__name__ = "SnmpAdminString"
_CDhcpv4ServerSharedNetName_Object = MibTableColumn
cDhcpv4ServerSharedNetName = _CDhcpv4ServerSharedNetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 1),
    _CDhcpv4ServerSharedNetName_Type()
)
cDhcpv4ServerSharedNetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetName.setStatus("current")
_CDhcpv4ServerSharedNetFreeAddrLowThreshold_Type = Unsigned32
_CDhcpv4ServerSharedNetFreeAddrLowThreshold_Object = MibTableColumn
cDhcpv4ServerSharedNetFreeAddrLowThreshold = _CDhcpv4ServerSharedNetFreeAddrLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 2),
    _CDhcpv4ServerSharedNetFreeAddrLowThreshold_Type()
)
cDhcpv4ServerSharedNetFreeAddrLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetFreeAddrLowThreshold.setStatus("current")
_CDhcpv4ServerSharedNetFreeAddrHighThreshold_Type = Unsigned32
_CDhcpv4ServerSharedNetFreeAddrHighThreshold_Object = MibTableColumn
cDhcpv4ServerSharedNetFreeAddrHighThreshold = _CDhcpv4ServerSharedNetFreeAddrHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 3),
    _CDhcpv4ServerSharedNetFreeAddrHighThreshold_Type()
)
cDhcpv4ServerSharedNetFreeAddrHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetFreeAddrHighThreshold.setStatus("current")
_CDhcpv4ServerSharedNetFreeAddresses_Type = Unsigned32
_CDhcpv4ServerSharedNetFreeAddresses_Object = MibTableColumn
cDhcpv4ServerSharedNetFreeAddresses = _CDhcpv4ServerSharedNetFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 4),
    _CDhcpv4ServerSharedNetFreeAddresses_Type()
)
cDhcpv4ServerSharedNetFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetFreeAddresses.setStatus("current")
_CDhcpv4ServerSharedNetReservedAddresses_Type = Unsigned32
_CDhcpv4ServerSharedNetReservedAddresses_Object = MibTableColumn
cDhcpv4ServerSharedNetReservedAddresses = _CDhcpv4ServerSharedNetReservedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 5),
    _CDhcpv4ServerSharedNetReservedAddresses_Type()
)
cDhcpv4ServerSharedNetReservedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetReservedAddresses.setStatus("current")
_CDhcpv4ServerSharedNetTotalAddresses_Type = Unsigned32
_CDhcpv4ServerSharedNetTotalAddresses_Object = MibTableColumn
cDhcpv4ServerSharedNetTotalAddresses = _CDhcpv4ServerSharedNetTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 1, 1, 6),
    _CDhcpv4ServerSharedNetTotalAddresses_Type()
)
cDhcpv4ServerSharedNetTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetTotalAddresses.setStatus("current")
_CDhcpv4ServerSubnetTable_Object = MibTable
cDhcpv4ServerSubnetTable = _CDhcpv4ServerSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetTable.setStatus("current")
_CDhcpv4ServerSubnetEntry_Object = MibTableRow
cDhcpv4ServerSubnetEntry = _CDhcpv4ServerSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1)
)
cDhcpv4ServerSubnetEntry.setIndexNames(
    (0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetAddress"),
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetEntry.setStatus("current")
_CDhcpv4ServerSubnetAddress_Type = InetAddressIPv4
_CDhcpv4ServerSubnetAddress_Object = MibTableColumn
cDhcpv4ServerSubnetAddress = _CDhcpv4ServerSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 1),
    _CDhcpv4ServerSubnetAddress_Type()
)
cDhcpv4ServerSubnetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetAddress.setStatus("current")
_CDhcpv4ServerSubnetMask_Type = InetAddressPrefixLength
_CDhcpv4ServerSubnetMask_Object = MibTableColumn
cDhcpv4ServerSubnetMask = _CDhcpv4ServerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 2),
    _CDhcpv4ServerSubnetMask_Type()
)
cDhcpv4ServerSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetMask.setStatus("current")


class _CDhcpv4ServerSubnetSharedNetworkName_Type(SnmpAdminString):
    """Custom type cDhcpv4ServerSubnetSharedNetworkName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CDhcpv4ServerSubnetSharedNetworkName_Type.__name__ = "SnmpAdminString"
_CDhcpv4ServerSubnetSharedNetworkName_Object = MibTableColumn
cDhcpv4ServerSubnetSharedNetworkName = _CDhcpv4ServerSubnetSharedNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 3),
    _CDhcpv4ServerSubnetSharedNetworkName_Type()
)
cDhcpv4ServerSubnetSharedNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetSharedNetworkName.setStatus("current")
_CDhcpv4ServerSubnetFreeAddrLowThreshold_Type = Unsigned32
_CDhcpv4ServerSubnetFreeAddrLowThreshold_Object = MibTableColumn
cDhcpv4ServerSubnetFreeAddrLowThreshold = _CDhcpv4ServerSubnetFreeAddrLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 4),
    _CDhcpv4ServerSubnetFreeAddrLowThreshold_Type()
)
cDhcpv4ServerSubnetFreeAddrLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetFreeAddrLowThreshold.setStatus("current")
_CDhcpv4ServerSubnetFreeAddrHighThreshold_Type = Unsigned32
_CDhcpv4ServerSubnetFreeAddrHighThreshold_Object = MibTableColumn
cDhcpv4ServerSubnetFreeAddrHighThreshold = _CDhcpv4ServerSubnetFreeAddrHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 5),
    _CDhcpv4ServerSubnetFreeAddrHighThreshold_Type()
)
cDhcpv4ServerSubnetFreeAddrHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetFreeAddrHighThreshold.setStatus("current")
_CDhcpv4ServerSubnetFreeAddresses_Type = Unsigned32
_CDhcpv4ServerSubnetFreeAddresses_Object = MibTableColumn
cDhcpv4ServerSubnetFreeAddresses = _CDhcpv4ServerSubnetFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 2, 1, 6),
    _CDhcpv4ServerSubnetFreeAddresses_Type()
)
cDhcpv4ServerSubnetFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetFreeAddresses.setStatus("current")
_CDhcpv4ServerRangeTable_Object = MibTable
cDhcpv4ServerRangeTable = _CDhcpv4ServerRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeTable.setStatus("current")
_CDhcpv4ServerRangeEntry_Object = MibTableRow
cDhcpv4ServerRangeEntry = _CDhcpv4ServerRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1)
)
cDhcpv4ServerRangeEntry.setIndexNames(
    (0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeStartAddress"),
    (0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeEndAddress"),
)
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeEntry.setStatus("current")
_CDhcpv4ServerRangeStartAddress_Type = InetAddressIPv4
_CDhcpv4ServerRangeStartAddress_Object = MibTableColumn
cDhcpv4ServerRangeStartAddress = _CDhcpv4ServerRangeStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 1),
    _CDhcpv4ServerRangeStartAddress_Type()
)
cDhcpv4ServerRangeStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeStartAddress.setStatus("current")
_CDhcpv4ServerRangeEndAddress_Type = InetAddressIPv4
_CDhcpv4ServerRangeEndAddress_Object = MibTableColumn
cDhcpv4ServerRangeEndAddress = _CDhcpv4ServerRangeEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 2),
    _CDhcpv4ServerRangeEndAddress_Type()
)
cDhcpv4ServerRangeEndAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeEndAddress.setStatus("current")
_CDhcpv4ServerRangeSubnetMask_Type = InetAddressPrefixLength
_CDhcpv4ServerRangeSubnetMask_Object = MibTableColumn
cDhcpv4ServerRangeSubnetMask = _CDhcpv4ServerRangeSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 3),
    _CDhcpv4ServerRangeSubnetMask_Type()
)
cDhcpv4ServerRangeSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeSubnetMask.setStatus("current")
_CDhcpv4ServerRangeInUse_Type = Gauge32
_CDhcpv4ServerRangeInUse_Object = MibTableColumn
cDhcpv4ServerRangeInUse = _CDhcpv4ServerRangeInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 4),
    _CDhcpv4ServerRangeInUse_Type()
)
cDhcpv4ServerRangeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeInUse.setStatus("current")
_CDhcpv4ServerRangeOutstandingOffers_Type = Gauge32
_CDhcpv4ServerRangeOutstandingOffers_Object = MibTableColumn
cDhcpv4ServerRangeOutstandingOffers = _CDhcpv4ServerRangeOutstandingOffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 3, 1, 5),
    _CDhcpv4ServerRangeOutstandingOffers_Type()
)
cDhcpv4ServerRangeOutstandingOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeOutstandingOffers.setStatus("current")
_CDhcpv4ServerClientTable_Object = MibTable
cDhcpv4ServerClientTable = _CDhcpv4ServerClientTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cDhcpv4ServerClientTable.setStatus("current")
_CDhcpv4ServerClientEntry_Object = MibTableRow
cDhcpv4ServerClientEntry = _CDhcpv4ServerClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1)
)
cDhcpv4ServerClientEntry.setIndexNames(
    (0, "CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClient"),
)
if mibBuilder.loadTexts:
    cDhcpv4ServerClientEntry.setStatus("current")
_CDhcpv4ServerClient_Type = InetAddressIPv4
_CDhcpv4ServerClient_Object = MibTableColumn
cDhcpv4ServerClient = _CDhcpv4ServerClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 1),
    _CDhcpv4ServerClient_Type()
)
cDhcpv4ServerClient.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDhcpv4ServerClient.setStatus("current")
_CDhcpv4ServerClientSubnetMask_Type = InetAddressPrefixLength
_CDhcpv4ServerClientSubnetMask_Object = MibTableColumn
cDhcpv4ServerClientSubnetMask = _CDhcpv4ServerClientSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 2),
    _CDhcpv4ServerClientSubnetMask_Type()
)
cDhcpv4ServerClientSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientSubnetMask.setStatus("current")
_CDhcpv4ServerClientRange_Type = InetAddressIPv4
_CDhcpv4ServerClientRange_Object = MibTableColumn
cDhcpv4ServerClientRange = _CDhcpv4ServerClientRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 3),
    _CDhcpv4ServerClientRange_Type()
)
cDhcpv4ServerClientRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientRange.setStatus("current")


class _CDhcpv4ServerClientLeaseType_Type(Integer32):
    """Custom type cDhcpv4ServerClientLeaseType based on Integer32"""
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
        *(("configurationReserved", 4),
          ("dynamic", 2),
          ("expired", 3),
          ("serverReserved", 5),
          ("static", 1))
    )


_CDhcpv4ServerClientLeaseType_Type.__name__ = "Integer32"
_CDhcpv4ServerClientLeaseType_Object = MibTableColumn
cDhcpv4ServerClientLeaseType = _CDhcpv4ServerClientLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 4),
    _CDhcpv4ServerClientLeaseType_Type()
)
cDhcpv4ServerClientLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientLeaseType.setStatus("current")
_CDhcpv4ServerClientTimeRemaining_Type = Unsigned32
_CDhcpv4ServerClientTimeRemaining_Object = MibTableColumn
cDhcpv4ServerClientTimeRemaining = _CDhcpv4ServerClientTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 5),
    _CDhcpv4ServerClientTimeRemaining_Type()
)
cDhcpv4ServerClientTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientTimeRemaining.setStatus("current")


class _CDhcpv4ServerClientAllowedProtocol_Type(Integer32):
    """Custom type cDhcpv4ServerClientAllowedProtocol based on Integer32"""
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
        *(("bootp", 2),
          ("bootpOrDhcp", 4),
          ("dhcp", 3),
          ("none", 1))
    )


_CDhcpv4ServerClientAllowedProtocol_Type.__name__ = "Integer32"
_CDhcpv4ServerClientAllowedProtocol_Object = MibTableColumn
cDhcpv4ServerClientAllowedProtocol = _CDhcpv4ServerClientAllowedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 6),
    _CDhcpv4ServerClientAllowedProtocol_Type()
)
cDhcpv4ServerClientAllowedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientAllowedProtocol.setStatus("current")


class _CDhcpv4ServerClientServedProtocol_Type(Integer32):
    """Custom type cDhcpv4ServerClientServedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_CDhcpv4ServerClientServedProtocol_Type.__name__ = "Integer32"
_CDhcpv4ServerClientServedProtocol_Object = MibTableColumn
cDhcpv4ServerClientServedProtocol = _CDhcpv4ServerClientServedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 7),
    _CDhcpv4ServerClientServedProtocol_Type()
)
cDhcpv4ServerClientServedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientServedProtocol.setStatus("current")
_CDhcpv4ServerClientPhysicalAddress_Type = CDhcpv4PhysicalAddress
_CDhcpv4ServerClientPhysicalAddress_Object = MibTableColumn
cDhcpv4ServerClientPhysicalAddress = _CDhcpv4ServerClientPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 8),
    _CDhcpv4ServerClientPhysicalAddress_Type()
)
cDhcpv4ServerClientPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientPhysicalAddress.setStatus("current")


class _CDhcpv4ServerClientClientId_Type(OctetString):
    """Custom type cDhcpv4ServerClientClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CDhcpv4ServerClientClientId_Type.__name__ = "OctetString"
_CDhcpv4ServerClientClientId_Object = MibTableColumn
cDhcpv4ServerClientClientId = _CDhcpv4ServerClientClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 9),
    _CDhcpv4ServerClientClientId_Type()
)
cDhcpv4ServerClientClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientClientId.setStatus("current")


class _CDhcpv4ServerClientHostName_Type(SnmpAdminString):
    """Custom type cDhcpv4ServerClientHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CDhcpv4ServerClientHostName_Type.__name__ = "SnmpAdminString"
_CDhcpv4ServerClientHostName_Object = MibTableColumn
cDhcpv4ServerClientHostName = _CDhcpv4ServerClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 10),
    _CDhcpv4ServerClientHostName_Type()
)
cDhcpv4ServerClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientHostName.setStatus("current")


class _CDhcpv4ServerClientDomainName_Type(SnmpAdminString):
    """Custom type cDhcpv4ServerClientDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CDhcpv4ServerClientDomainName_Type.__name__ = "SnmpAdminString"
_CDhcpv4ServerClientDomainName_Object = MibTableColumn
cDhcpv4ServerClientDomainName = _CDhcpv4ServerClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 4, 4, 1, 11),
    _CDhcpv4ServerClientDomainName_Type()
)
cDhcpv4ServerClientDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerClientDomainName.setStatus("current")
_CDhcpv4ServerNotifyObjects_ObjectIdentity = ObjectIdentity
cDhcpv4ServerNotifyObjects = _CDhcpv4ServerNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7)
)
if mibBuilder.loadTexts:
    cDhcpv4ServerNotifyObjects.setStatus("current")
_CDhcpv4ServerNotifyDuplicateIpAddr_Type = InetAddressIPv4
_CDhcpv4ServerNotifyDuplicateIpAddr_Object = MibScalar
cDhcpv4ServerNotifyDuplicateIpAddr = _CDhcpv4ServerNotifyDuplicateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 1),
    _CDhcpv4ServerNotifyDuplicateIpAddr_Type()
)
cDhcpv4ServerNotifyDuplicateIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cDhcpv4ServerNotifyDuplicateIpAddr.setStatus("current")
_CDhcpv4ServerNotifyDuplicateMac_Type = CDhcpv4PhysicalAddress
_CDhcpv4ServerNotifyDuplicateMac_Object = MibScalar
cDhcpv4ServerNotifyDuplicateMac = _CDhcpv4ServerNotifyDuplicateMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 2),
    _CDhcpv4ServerNotifyDuplicateMac_Type()
)
cDhcpv4ServerNotifyDuplicateMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cDhcpv4ServerNotifyDuplicateMac.setStatus("current")


class _CDhcpv4ServerNotifyClientOrServerDetected_Type(Integer32):
    """Custom type cDhcpv4ServerNotifyClientOrServerDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_CDhcpv4ServerNotifyClientOrServerDetected_Type.__name__ = "Integer32"
_CDhcpv4ServerNotifyClientOrServerDetected_Object = MibScalar
cDhcpv4ServerNotifyClientOrServerDetected = _CDhcpv4ServerNotifyClientOrServerDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 3),
    _CDhcpv4ServerNotifyClientOrServerDetected_Type()
)
cDhcpv4ServerNotifyClientOrServerDetected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cDhcpv4ServerNotifyClientOrServerDetected.setStatus("current")
_CDhcpv4ServerNotifyServerStart_Type = DateAndTime
_CDhcpv4ServerNotifyServerStart_Object = MibScalar
cDhcpv4ServerNotifyServerStart = _CDhcpv4ServerNotifyServerStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 4),
    _CDhcpv4ServerNotifyServerStart_Type()
)
cDhcpv4ServerNotifyServerStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cDhcpv4ServerNotifyServerStart.setStatus("current")
_CDhcpv4ServerNotifyServerStop_Type = DateAndTime
_CDhcpv4ServerNotifyServerStop_Object = MibScalar
cDhcpv4ServerNotifyServerStop = _CDhcpv4ServerNotifyServerStop_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 7, 5),
    _CDhcpv4ServerNotifyServerStop_Type()
)
cDhcpv4ServerNotifyServerStop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cDhcpv4ServerNotifyServerStop.setStatus("current")
_CBootpHCCounters_ObjectIdentity = ObjectIdentity
cBootpHCCounters = _CBootpHCCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8)
)
if mibBuilder.loadTexts:
    cBootpHCCounters.setStatus("current")
_CBootpHCCountRequests_Type = Counter64
_CBootpHCCountRequests_Object = MibScalar
cBootpHCCountRequests = _CBootpHCCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 1),
    _CBootpHCCountRequests_Type()
)
cBootpHCCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpHCCountRequests.setStatus("current")
_CBootpHCCountInvalids_Type = Counter64
_CBootpHCCountInvalids_Object = MibScalar
cBootpHCCountInvalids = _CBootpHCCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 2),
    _CBootpHCCountInvalids_Type()
)
cBootpHCCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpHCCountInvalids.setStatus("current")
_CBootpHCCountReplies_Type = Counter64
_CBootpHCCountReplies_Object = MibScalar
cBootpHCCountReplies = _CBootpHCCountReplies_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 3),
    _CBootpHCCountReplies_Type()
)
cBootpHCCountReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpHCCountReplies.setStatus("current")
_CBootpHCCountDropUnknownClients_Type = Counter64
_CBootpHCCountDropUnknownClients_Object = MibScalar
cBootpHCCountDropUnknownClients = _CBootpHCCountDropUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 4),
    _CBootpHCCountDropUnknownClients_Type()
)
cBootpHCCountDropUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpHCCountDropUnknownClients.setStatus("current")
_CBootpHCCountDropNotServingSubnet_Type = Counter64
_CBootpHCCountDropNotServingSubnet_Object = MibScalar
cBootpHCCountDropNotServingSubnet = _CBootpHCCountDropNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 8, 5),
    _CBootpHCCountDropNotServingSubnet_Type()
)
cBootpHCCountDropNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cBootpHCCountDropNotServingSubnet.setStatus("current")
_CDhcpv4HCCounters_ObjectIdentity = ObjectIdentity
cDhcpv4HCCounters = _CDhcpv4HCCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9)
)
if mibBuilder.loadTexts:
    cDhcpv4HCCounters.setStatus("current")
_CDhcpv4HCCountDiscovers_Type = Counter64
_CDhcpv4HCCountDiscovers_Object = MibScalar
cDhcpv4HCCountDiscovers = _CDhcpv4HCCountDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 1),
    _CDhcpv4HCCountDiscovers_Type()
)
cDhcpv4HCCountDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountDiscovers.setStatus("current")
_CDhcpv4HCCountOffers_Type = Counter64
_CDhcpv4HCCountOffers_Object = MibScalar
cDhcpv4HCCountOffers = _CDhcpv4HCCountOffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 2),
    _CDhcpv4HCCountOffers_Type()
)
cDhcpv4HCCountOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountOffers.setStatus("current")
_CDhcpv4HCCountRequests_Type = Counter64
_CDhcpv4HCCountRequests_Object = MibScalar
cDhcpv4HCCountRequests = _CDhcpv4HCCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 3),
    _CDhcpv4HCCountRequests_Type()
)
cDhcpv4HCCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountRequests.setStatus("current")
_CDhcpv4HCCountDeclines_Type = Counter64
_CDhcpv4HCCountDeclines_Object = MibScalar
cDhcpv4HCCountDeclines = _CDhcpv4HCCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 4),
    _CDhcpv4HCCountDeclines_Type()
)
cDhcpv4HCCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountDeclines.setStatus("current")
_CDhcpv4HCCountAcks_Type = Counter64
_CDhcpv4HCCountAcks_Object = MibScalar
cDhcpv4HCCountAcks = _CDhcpv4HCCountAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 5),
    _CDhcpv4HCCountAcks_Type()
)
cDhcpv4HCCountAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountAcks.setStatus("current")
_CDhcpv4HCCountNaks_Type = Counter64
_CDhcpv4HCCountNaks_Object = MibScalar
cDhcpv4HCCountNaks = _CDhcpv4HCCountNaks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 6),
    _CDhcpv4HCCountNaks_Type()
)
cDhcpv4HCCountNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountNaks.setStatus("current")
_CDhcpv4HCCountReleases_Type = Counter64
_CDhcpv4HCCountReleases_Object = MibScalar
cDhcpv4HCCountReleases = _CDhcpv4HCCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 7),
    _CDhcpv4HCCountReleases_Type()
)
cDhcpv4HCCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountReleases.setStatus("current")
_CDhcpv4HCCountInforms_Type = Counter64
_CDhcpv4HCCountInforms_Object = MibScalar
cDhcpv4HCCountInforms = _CDhcpv4HCCountInforms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 8),
    _CDhcpv4HCCountInforms_Type()
)
cDhcpv4HCCountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountInforms.setStatus("current")
_CDhcpv4HCCountForcedRenews_Type = Counter64
_CDhcpv4HCCountForcedRenews_Object = MibScalar
cDhcpv4HCCountForcedRenews = _CDhcpv4HCCountForcedRenews_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 9),
    _CDhcpv4HCCountForcedRenews_Type()
)
cDhcpv4HCCountForcedRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountForcedRenews.setStatus("current")
_CDhcpv4HCCountInvalids_Type = Counter64
_CDhcpv4HCCountInvalids_Object = MibScalar
cDhcpv4HCCountInvalids = _CDhcpv4HCCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 10),
    _CDhcpv4HCCountInvalids_Type()
)
cDhcpv4HCCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountInvalids.setStatus("current")
_CDhcpv4HCCountDropUnknownClient_Type = Counter64
_CDhcpv4HCCountDropUnknownClient_Object = MibScalar
cDhcpv4HCCountDropUnknownClient = _CDhcpv4HCCountDropUnknownClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 11),
    _CDhcpv4HCCountDropUnknownClient_Type()
)
cDhcpv4HCCountDropUnknownClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountDropUnknownClient.setStatus("current")
_CDhcpv4HCCountDropNotServingSubnet_Type = Counter64
_CDhcpv4HCCountDropNotServingSubnet_Object = MibScalar
cDhcpv4HCCountDropNotServingSubnet = _CDhcpv4HCCountDropNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 1, 9, 12),
    _CDhcpv4HCCountDropNotServingSubnet_Type()
)
cDhcpv4HCCountDropNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4HCCountDropNotServingSubnet.setStatus("current")
_CiscoIetfDhcpv4SrvMIBConform_ObjectIdentity = ObjectIdentity
ciscoIetfDhcpv4SrvMIBConform = _CiscoIetfDhcpv4SrvMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2)
)
_CDhcpv4SrvCompliances_ObjectIdentity = ObjectIdentity
cDhcpv4SrvCompliances = _CDhcpv4SrvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 1)
)
_CDhcpv4SrvGroups_ObjectIdentity = ObjectIdentity
cDhcpv4SrvGroups = _CDhcpv4SrvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2)
)

# Managed Objects groups

cDhcpv4SrvSystemObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 1)
)
cDhcpv4SrvSystemObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4SrvSystemDescr"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4SrvSystemObjectID"))
)
if mibBuilder.loadTexts:
    cDhcpv4SrvSystemObjects.setStatus("current")

cBootpCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 2)
)
cBootpCountersGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountRequests"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountInvalids"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountReplies"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountDropUnknownClients"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpCountDropNotServingSubnet"))
)
if mibBuilder.loadTexts:
    cBootpCountersGroup.setStatus("current")

cDhcpv4CounterObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 3)
)
cDhcpv4CounterObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDiscovers"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountOffers"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountRequests"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDeclines"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountAcks"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountNaks"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountReleases"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountInforms"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountInvalids"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDropUnknownClient"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4CountDropNotServingSubnet"))
)
if mibBuilder.loadTexts:
    cDhcpv4CounterObjects.setStatus("current")

cBootpHCCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 4)
)
cBootpHCCountersGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountRequests"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountInvalids"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountReplies"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountDropUnknownClients"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cBootpHCCountDropNotServingSubnet"))
)
if mibBuilder.loadTexts:
    cBootpHCCountersGroup.setStatus("current")

cDhcpv4HCCounterObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 5)
)
cDhcpv4HCCounterObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDiscovers"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountOffers"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountRequests"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDeclines"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountAcks"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountNaks"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountReleases"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountInforms"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountForcedRenews"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountInvalids"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDropUnknownClient"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4HCCountDropNotServingSubnet"))
)
if mibBuilder.loadTexts:
    cDhcpv4HCCounterObjects.setStatus("current")

cDhcpv4ServerSharedNetObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 6)
)
cDhcpv4ServerSharedNetObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrLowThreshold"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrHighThreshold"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddresses"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetReservedAddresses"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetTotalAddresses"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSharedNetObjects.setStatus("current")

cDhcpv4ServerSubnetObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 7)
)
cDhcpv4ServerSubnetObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetMask"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetSharedNetworkName"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddrLowThreshold"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddrHighThreshold"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddresses"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetObjects.setStatus("current")

cDhcpv4ServerRangeObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 8)
)
cDhcpv4ServerRangeObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeSubnetMask"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeInUse"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerRangeOutstandingOffers"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerRangeObjects.setStatus("current")

cDhcpv4ServerClientObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 9)
)
cDhcpv4ServerClientObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientSubnetMask"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientRange"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientLeaseType"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientTimeRemaining"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientAllowedProtocol"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientServedProtocol"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientPhysicalAddress"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientClientId"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientHostName"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientDomainName"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerClientObjects.setStatus("current")

cDhcpv4ServerNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 10)
)
cDhcpv4ServerNotifyObjectsGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateIpAddr"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateMac"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyClientOrServerDetected"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStart"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStop"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerNotifyObjectsGroup.setStatus("current")


# Notification objects

cDhcpv4ServerFreeAddressLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 1)
)
cDhcpv4ServerFreeAddressLow.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrLowThreshold"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddresses"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerFreeAddressLow.setStatus(
        "current"
    )

cDhcpv4ServerFreeAddressHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 2)
)
cDhcpv4ServerFreeAddressHigh.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddrHighThreshold"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSharedNetFreeAddresses"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerFreeAddressHigh.setStatus(
        "current"
    )

cDhcpv4ServerStartTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 3)
)
cDhcpv4ServerStartTime.setObjects(
    ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStart")
)
if mibBuilder.loadTexts:
    cDhcpv4ServerStartTime.setStatus(
        "current"
    )

cDhcpv4ServerStopTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 4)
)
cDhcpv4ServerStopTime.setObjects(
    ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyServerStop")
)
if mibBuilder.loadTexts:
    cDhcpv4ServerStopTime.setStatus(
        "current"
    )

cDhcpv4ServerDuplicateAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 0, 2, 0, 5)
)
cDhcpv4ServerDuplicateAddress.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateIpAddr"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyDuplicateMac"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerNotifyClientOrServerDetected"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerDuplicateAddress.setStatus(
        "current"
    )


# Notifications groups

cDhcpv4ServerNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 2, 11)
)
cDhcpv4ServerNotificationsGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerFreeAddressLow"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerFreeAddressHigh"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerStartTime"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerStopTime"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerDuplicateAddress"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cDhcpv4SrvCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvCompliance.setStatus(
        "deprecated"
    )

cDhcpv4SrvComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 102, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-DHCP-SERVER-MIB",
    **{"CDhcpv4PhysicalAddress": CDhcpv4PhysicalAddress,
       "ciscoIetfDhcpSrvMIB": ciscoIetfDhcpSrvMIB,
       "ciscoIetfDhcpv4SrvMIBNotifs": ciscoIetfDhcpv4SrvMIBNotifs,
       "cDhcpv4ServerNotificationPrefix": cDhcpv4ServerNotificationPrefix,
       "cDhcpv4ServerNotifications": cDhcpv4ServerNotifications,
       "cDhcpv4ServerFreeAddressLow": cDhcpv4ServerFreeAddressLow,
       "cDhcpv4ServerFreeAddressHigh": cDhcpv4ServerFreeAddressHigh,
       "cDhcpv4ServerStartTime": cDhcpv4ServerStartTime,
       "cDhcpv4ServerStopTime": cDhcpv4ServerStopTime,
       "cDhcpv4ServerDuplicateAddress": cDhcpv4ServerDuplicateAddress,
       "ciscoIetfDhcpv4SrvMIBObjects": ciscoIetfDhcpv4SrvMIBObjects,
       "cDhcpv4SrvSystem": cDhcpv4SrvSystem,
       "cDhcpv4SrvSystemDescr": cDhcpv4SrvSystemDescr,
       "cDhcpv4SrvSystemObjectID": cDhcpv4SrvSystemObjectID,
       "cBootpCounters": cBootpCounters,
       "cBootpCountRequests": cBootpCountRequests,
       "cBootpCountInvalids": cBootpCountInvalids,
       "cBootpCountReplies": cBootpCountReplies,
       "cBootpCountDropUnknownClients": cBootpCountDropUnknownClients,
       "cBootpCountDropNotServingSubnet": cBootpCountDropNotServingSubnet,
       "cDhcpv4Counters": cDhcpv4Counters,
       "cDhcpv4CountDiscovers": cDhcpv4CountDiscovers,
       "cDhcpv4CountOffers": cDhcpv4CountOffers,
       "cDhcpv4CountRequests": cDhcpv4CountRequests,
       "cDhcpv4CountDeclines": cDhcpv4CountDeclines,
       "cDhcpv4CountAcks": cDhcpv4CountAcks,
       "cDhcpv4CountNaks": cDhcpv4CountNaks,
       "cDhcpv4CountReleases": cDhcpv4CountReleases,
       "cDhcpv4CountInforms": cDhcpv4CountInforms,
       "cDhcpv4CountInvalids": cDhcpv4CountInvalids,
       "cDhcpv4CountDropUnknownClient": cDhcpv4CountDropUnknownClient,
       "cDhcpv4CountDropNotServingSubnet": cDhcpv4CountDropNotServingSubnet,
       "cDhcpv4SrvConfiguration": cDhcpv4SrvConfiguration,
       "cDhcpv4ServerSharedNetTable": cDhcpv4ServerSharedNetTable,
       "cDhcpv4ServerSharedNetEntry": cDhcpv4ServerSharedNetEntry,
       "cDhcpv4ServerSharedNetName": cDhcpv4ServerSharedNetName,
       "cDhcpv4ServerSharedNetFreeAddrLowThreshold": cDhcpv4ServerSharedNetFreeAddrLowThreshold,
       "cDhcpv4ServerSharedNetFreeAddrHighThreshold": cDhcpv4ServerSharedNetFreeAddrHighThreshold,
       "cDhcpv4ServerSharedNetFreeAddresses": cDhcpv4ServerSharedNetFreeAddresses,
       "cDhcpv4ServerSharedNetReservedAddresses": cDhcpv4ServerSharedNetReservedAddresses,
       "cDhcpv4ServerSharedNetTotalAddresses": cDhcpv4ServerSharedNetTotalAddresses,
       "cDhcpv4ServerSubnetTable": cDhcpv4ServerSubnetTable,
       "cDhcpv4ServerSubnetEntry": cDhcpv4ServerSubnetEntry,
       "cDhcpv4ServerSubnetAddress": cDhcpv4ServerSubnetAddress,
       "cDhcpv4ServerSubnetMask": cDhcpv4ServerSubnetMask,
       "cDhcpv4ServerSubnetSharedNetworkName": cDhcpv4ServerSubnetSharedNetworkName,
       "cDhcpv4ServerSubnetFreeAddrLowThreshold": cDhcpv4ServerSubnetFreeAddrLowThreshold,
       "cDhcpv4ServerSubnetFreeAddrHighThreshold": cDhcpv4ServerSubnetFreeAddrHighThreshold,
       "cDhcpv4ServerSubnetFreeAddresses": cDhcpv4ServerSubnetFreeAddresses,
       "cDhcpv4ServerRangeTable": cDhcpv4ServerRangeTable,
       "cDhcpv4ServerRangeEntry": cDhcpv4ServerRangeEntry,
       "cDhcpv4ServerRangeStartAddress": cDhcpv4ServerRangeStartAddress,
       "cDhcpv4ServerRangeEndAddress": cDhcpv4ServerRangeEndAddress,
       "cDhcpv4ServerRangeSubnetMask": cDhcpv4ServerRangeSubnetMask,
       "cDhcpv4ServerRangeInUse": cDhcpv4ServerRangeInUse,
       "cDhcpv4ServerRangeOutstandingOffers": cDhcpv4ServerRangeOutstandingOffers,
       "cDhcpv4ServerClientTable": cDhcpv4ServerClientTable,
       "cDhcpv4ServerClientEntry": cDhcpv4ServerClientEntry,
       "cDhcpv4ServerClient": cDhcpv4ServerClient,
       "cDhcpv4ServerClientSubnetMask": cDhcpv4ServerClientSubnetMask,
       "cDhcpv4ServerClientRange": cDhcpv4ServerClientRange,
       "cDhcpv4ServerClientLeaseType": cDhcpv4ServerClientLeaseType,
       "cDhcpv4ServerClientTimeRemaining": cDhcpv4ServerClientTimeRemaining,
       "cDhcpv4ServerClientAllowedProtocol": cDhcpv4ServerClientAllowedProtocol,
       "cDhcpv4ServerClientServedProtocol": cDhcpv4ServerClientServedProtocol,
       "cDhcpv4ServerClientPhysicalAddress": cDhcpv4ServerClientPhysicalAddress,
       "cDhcpv4ServerClientClientId": cDhcpv4ServerClientClientId,
       "cDhcpv4ServerClientHostName": cDhcpv4ServerClientHostName,
       "cDhcpv4ServerClientDomainName": cDhcpv4ServerClientDomainName,
       "cDhcpv4ServerNotifyObjects": cDhcpv4ServerNotifyObjects,
       "cDhcpv4ServerNotifyDuplicateIpAddr": cDhcpv4ServerNotifyDuplicateIpAddr,
       "cDhcpv4ServerNotifyDuplicateMac": cDhcpv4ServerNotifyDuplicateMac,
       "cDhcpv4ServerNotifyClientOrServerDetected": cDhcpv4ServerNotifyClientOrServerDetected,
       "cDhcpv4ServerNotifyServerStart": cDhcpv4ServerNotifyServerStart,
       "cDhcpv4ServerNotifyServerStop": cDhcpv4ServerNotifyServerStop,
       "cBootpHCCounters": cBootpHCCounters,
       "cBootpHCCountRequests": cBootpHCCountRequests,
       "cBootpHCCountInvalids": cBootpHCCountInvalids,
       "cBootpHCCountReplies": cBootpHCCountReplies,
       "cBootpHCCountDropUnknownClients": cBootpHCCountDropUnknownClients,
       "cBootpHCCountDropNotServingSubnet": cBootpHCCountDropNotServingSubnet,
       "cDhcpv4HCCounters": cDhcpv4HCCounters,
       "cDhcpv4HCCountDiscovers": cDhcpv4HCCountDiscovers,
       "cDhcpv4HCCountOffers": cDhcpv4HCCountOffers,
       "cDhcpv4HCCountRequests": cDhcpv4HCCountRequests,
       "cDhcpv4HCCountDeclines": cDhcpv4HCCountDeclines,
       "cDhcpv4HCCountAcks": cDhcpv4HCCountAcks,
       "cDhcpv4HCCountNaks": cDhcpv4HCCountNaks,
       "cDhcpv4HCCountReleases": cDhcpv4HCCountReleases,
       "cDhcpv4HCCountInforms": cDhcpv4HCCountInforms,
       "cDhcpv4HCCountForcedRenews": cDhcpv4HCCountForcedRenews,
       "cDhcpv4HCCountInvalids": cDhcpv4HCCountInvalids,
       "cDhcpv4HCCountDropUnknownClient": cDhcpv4HCCountDropUnknownClient,
       "cDhcpv4HCCountDropNotServingSubnet": cDhcpv4HCCountDropNotServingSubnet,
       "ciscoIetfDhcpv4SrvMIBConform": ciscoIetfDhcpv4SrvMIBConform,
       "cDhcpv4SrvCompliances": cDhcpv4SrvCompliances,
       "cDhcpv4SrvCompliance": cDhcpv4SrvCompliance,
       "cDhcpv4SrvComplianceRev1": cDhcpv4SrvComplianceRev1,
       "cDhcpv4SrvGroups": cDhcpv4SrvGroups,
       "cDhcpv4SrvSystemObjects": cDhcpv4SrvSystemObjects,
       "cBootpCountersGroup": cBootpCountersGroup,
       "cDhcpv4CounterObjects": cDhcpv4CounterObjects,
       "cBootpHCCountersGroup": cBootpHCCountersGroup,
       "cDhcpv4HCCounterObjects": cDhcpv4HCCounterObjects,
       "cDhcpv4ServerSharedNetObjects": cDhcpv4ServerSharedNetObjects,
       "cDhcpv4ServerSubnetObjects": cDhcpv4ServerSubnetObjects,
       "cDhcpv4ServerRangeObjects": cDhcpv4ServerRangeObjects,
       "cDhcpv4ServerClientObjects": cDhcpv4ServerClientObjects,
       "cDhcpv4ServerNotifyObjectsGroup": cDhcpv4ServerNotifyObjectsGroup,
       "cDhcpv4ServerNotificationsGroup": cDhcpv4ServerNotificationsGroup}
)
