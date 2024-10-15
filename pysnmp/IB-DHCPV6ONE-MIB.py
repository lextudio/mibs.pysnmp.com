# SNMP MIB module (IB-DHCPV6ONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IB-DHCPV6ONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:15 2024
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

(IbIpv6Addr,
 IbString,
 ibDHCPOne) = mibBuilder.importSymbols(
    "IB-SMI-MIB",
    "IbIpv6Addr",
    "IbString",
    "ibDHCPOne")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ibDhcpv6Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2)
)
ibDhcpv6Module.setRevisions(
        ("2010-12-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbDHCPv6SubnetTable_Object = MibTable
ibDHCPv6SubnetTable = _IbDHCPv6SubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    ibDHCPv6SubnetTable.setStatus("current")
_IbDHCPv6SubnetEntry_Object = MibTableRow
ibDHCPv6SubnetEntry = _IbDHCPv6SubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 1, 1)
)
ibDHCPv6SubnetEntry.setIndexNames(
    (0, "IB-DHCPV6ONE-MIB", "ibDHCPv6SubnetNetworkAddress"),
)
if mibBuilder.loadTexts:
    ibDHCPv6SubnetEntry.setStatus("current")
_IbDHCPv6SubnetNetworkAddress_Type = IbIpv6Addr
_IbDHCPv6SubnetNetworkAddress_Object = MibTableColumn
ibDHCPv6SubnetNetworkAddress = _IbDHCPv6SubnetNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 1, 1, 1),
    _IbDHCPv6SubnetNetworkAddress_Type()
)
ibDHCPv6SubnetNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6SubnetNetworkAddress.setStatus("current")
_IbDHCPv6SubnetNetworkMask_Type = Integer32
_IbDHCPv6SubnetNetworkMask_Object = MibTableColumn
ibDHCPv6SubnetNetworkMask = _IbDHCPv6SubnetNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 1, 1, 2),
    _IbDHCPv6SubnetNetworkMask_Type()
)
ibDHCPv6SubnetNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6SubnetNetworkMask.setStatus("current")
_IbDHCPv6Statistics_ObjectIdentity = ObjectIdentity
ibDHCPv6Statistics = _IbDHCPv6Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3)
)
_IbDhcpv6TotalNoOfSolicits_Type = Counter32
_IbDhcpv6TotalNoOfSolicits_Object = MibScalar
ibDhcpv6TotalNoOfSolicits = _IbDhcpv6TotalNoOfSolicits_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 1),
    _IbDhcpv6TotalNoOfSolicits_Type()
)
ibDhcpv6TotalNoOfSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfSolicits.setStatus("current")
_IbDhcpv6TotalNoOfRequests_Type = Counter32
_IbDhcpv6TotalNoOfRequests_Object = MibScalar
ibDhcpv6TotalNoOfRequests = _IbDhcpv6TotalNoOfRequests_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 2),
    _IbDhcpv6TotalNoOfRequests_Type()
)
ibDhcpv6TotalNoOfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfRequests.setStatus("current")
_IbDhcpv6TotalNoOfReleases_Type = Counter32
_IbDhcpv6TotalNoOfReleases_Object = MibScalar
ibDhcpv6TotalNoOfReleases = _IbDhcpv6TotalNoOfReleases_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 3),
    _IbDhcpv6TotalNoOfReleases_Type()
)
ibDhcpv6TotalNoOfReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfReleases.setStatus("current")
_IbDhcpv6TotalNoOfAdvertises_Type = Counter32
_IbDhcpv6TotalNoOfAdvertises_Object = MibScalar
ibDhcpv6TotalNoOfAdvertises = _IbDhcpv6TotalNoOfAdvertises_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 4),
    _IbDhcpv6TotalNoOfAdvertises_Type()
)
ibDhcpv6TotalNoOfAdvertises.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfAdvertises.setStatus("current")
_IbDhcpv6TotalNoOfReplies_Type = Counter32
_IbDhcpv6TotalNoOfReplies_Object = MibScalar
ibDhcpv6TotalNoOfReplies = _IbDhcpv6TotalNoOfReplies_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 5),
    _IbDhcpv6TotalNoOfReplies_Type()
)
ibDhcpv6TotalNoOfReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfReplies.setStatus("current")
_IbDhcpv6TotalNoOfRenews_Type = Counter32
_IbDhcpv6TotalNoOfRenews_Object = MibScalar
ibDhcpv6TotalNoOfRenews = _IbDhcpv6TotalNoOfRenews_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 6),
    _IbDhcpv6TotalNoOfRenews_Type()
)
ibDhcpv6TotalNoOfRenews.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfRenews.setStatus("current")
_IbDhcpv6TotalNoOfRebinds_Type = Counter32
_IbDhcpv6TotalNoOfRebinds_Object = MibScalar
ibDhcpv6TotalNoOfRebinds = _IbDhcpv6TotalNoOfRebinds_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 7),
    _IbDhcpv6TotalNoOfRebinds_Type()
)
ibDhcpv6TotalNoOfRebinds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfRebinds.setStatus("current")
_IbDhcpv6TotalNoOfDeclines_Type = Counter32
_IbDhcpv6TotalNoOfDeclines_Object = MibScalar
ibDhcpv6TotalNoOfDeclines = _IbDhcpv6TotalNoOfDeclines_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 8),
    _IbDhcpv6TotalNoOfDeclines_Type()
)
ibDhcpv6TotalNoOfDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfDeclines.setStatus("current")
_IbDhcpv6TotalNoOfInformationRequests_Type = Counter32
_IbDhcpv6TotalNoOfInformationRequests_Object = MibScalar
ibDhcpv6TotalNoOfInformationRequests = _IbDhcpv6TotalNoOfInformationRequests_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 9),
    _IbDhcpv6TotalNoOfInformationRequests_Type()
)
ibDhcpv6TotalNoOfInformationRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfInformationRequests.setStatus("current")
_IbDhcpv6TotalNoOfOthers_Type = Counter32
_IbDhcpv6TotalNoOfOthers_Object = MibScalar
ibDhcpv6TotalNoOfOthers = _IbDhcpv6TotalNoOfOthers_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 3, 10),
    _IbDhcpv6TotalNoOfOthers_Type()
)
ibDhcpv6TotalNoOfOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6TotalNoOfOthers.setStatus("current")
_IbDhcpv6DeferredQueueSize_Type = Integer32
_IbDhcpv6DeferredQueueSize_Object = MibScalar
ibDhcpv6DeferredQueueSize = _IbDhcpv6DeferredQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 4),
    _IbDhcpv6DeferredQueueSize_Type()
)
ibDhcpv6DeferredQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpv6DeferredQueueSize.setStatus("current")
_IbDHCPv6DDNSStats_ObjectIdentity = ObjectIdentity
ibDHCPv6DDNSStats = _IbDHCPv6DDNSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5)
)
_IbDHCPv6DDNSAvgLatency5_Type = Counter64
_IbDHCPv6DDNSAvgLatency5_Object = MibScalar
ibDHCPv6DDNSAvgLatency5 = _IbDHCPv6DDNSAvgLatency5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 1),
    _IbDHCPv6DDNSAvgLatency5_Type()
)
ibDHCPv6DDNSAvgLatency5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSAvgLatency5.setStatus("current")
_IbDHCPv6DDNSAvgLatency15_Type = Counter64
_IbDHCPv6DDNSAvgLatency15_Object = MibScalar
ibDHCPv6DDNSAvgLatency15 = _IbDHCPv6DDNSAvgLatency15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 2),
    _IbDHCPv6DDNSAvgLatency15_Type()
)
ibDHCPv6DDNSAvgLatency15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSAvgLatency15.setStatus("current")
_IbDHCPv6DDNSAvgLatency60_Type = Counter64
_IbDHCPv6DDNSAvgLatency60_Object = MibScalar
ibDHCPv6DDNSAvgLatency60 = _IbDHCPv6DDNSAvgLatency60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 3),
    _IbDHCPv6DDNSAvgLatency60_Type()
)
ibDHCPv6DDNSAvgLatency60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSAvgLatency60.setStatus("current")
_IbDHCPv6DDNSAvgLatency1440_Type = Counter64
_IbDHCPv6DDNSAvgLatency1440_Object = MibScalar
ibDHCPv6DDNSAvgLatency1440 = _IbDHCPv6DDNSAvgLatency1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 4),
    _IbDHCPv6DDNSAvgLatency1440_Type()
)
ibDHCPv6DDNSAvgLatency1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSAvgLatency1440.setStatus("current")
_IbDHCPv6DDNSTimeoutCount5_Type = Unsigned32
_IbDHCPv6DDNSTimeoutCount5_Object = MibScalar
ibDHCPv6DDNSTimeoutCount5 = _IbDHCPv6DDNSTimeoutCount5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 5),
    _IbDHCPv6DDNSTimeoutCount5_Type()
)
ibDHCPv6DDNSTimeoutCount5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSTimeoutCount5.setStatus("current")
_IbDHCPv6DDNSTimeoutCount15_Type = Unsigned32
_IbDHCPv6DDNSTimeoutCount15_Object = MibScalar
ibDHCPv6DDNSTimeoutCount15 = _IbDHCPv6DDNSTimeoutCount15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 6),
    _IbDHCPv6DDNSTimeoutCount15_Type()
)
ibDHCPv6DDNSTimeoutCount15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSTimeoutCount15.setStatus("current")
_IbDHCPv6DDNSTimeoutCount60_Type = Unsigned32
_IbDHCPv6DDNSTimeoutCount60_Object = MibScalar
ibDHCPv6DDNSTimeoutCount60 = _IbDHCPv6DDNSTimeoutCount60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 7),
    _IbDHCPv6DDNSTimeoutCount60_Type()
)
ibDHCPv6DDNSTimeoutCount60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSTimeoutCount60.setStatus("current")
_IbDHCPv6DDNSTimeoutCount1440_Type = Unsigned32
_IbDHCPv6DDNSTimeoutCount1440_Object = MibScalar
ibDHCPv6DDNSTimeoutCount1440 = _IbDHCPv6DDNSTimeoutCount1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 2, 5, 8),
    _IbDHCPv6DDNSTimeoutCount1440_Type()
)
ibDHCPv6DDNSTimeoutCount1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPv6DDNSTimeoutCount1440.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-DHCPV6ONE-MIB",
    **{"ibDhcpv6Module": ibDhcpv6Module,
       "ibDHCPv6SubnetTable": ibDHCPv6SubnetTable,
       "ibDHCPv6SubnetEntry": ibDHCPv6SubnetEntry,
       "ibDHCPv6SubnetNetworkAddress": ibDHCPv6SubnetNetworkAddress,
       "ibDHCPv6SubnetNetworkMask": ibDHCPv6SubnetNetworkMask,
       "ibDHCPv6Statistics": ibDHCPv6Statistics,
       "ibDhcpv6TotalNoOfSolicits": ibDhcpv6TotalNoOfSolicits,
       "ibDhcpv6TotalNoOfRequests": ibDhcpv6TotalNoOfRequests,
       "ibDhcpv6TotalNoOfReleases": ibDhcpv6TotalNoOfReleases,
       "ibDhcpv6TotalNoOfAdvertises": ibDhcpv6TotalNoOfAdvertises,
       "ibDhcpv6TotalNoOfReplies": ibDhcpv6TotalNoOfReplies,
       "ibDhcpv6TotalNoOfRenews": ibDhcpv6TotalNoOfRenews,
       "ibDhcpv6TotalNoOfRebinds": ibDhcpv6TotalNoOfRebinds,
       "ibDhcpv6TotalNoOfDeclines": ibDhcpv6TotalNoOfDeclines,
       "ibDhcpv6TotalNoOfInformationRequests": ibDhcpv6TotalNoOfInformationRequests,
       "ibDhcpv6TotalNoOfOthers": ibDhcpv6TotalNoOfOthers,
       "ibDhcpv6DeferredQueueSize": ibDhcpv6DeferredQueueSize,
       "ibDHCPv6DDNSStats": ibDHCPv6DDNSStats,
       "ibDHCPv6DDNSAvgLatency5": ibDHCPv6DDNSAvgLatency5,
       "ibDHCPv6DDNSAvgLatency15": ibDHCPv6DDNSAvgLatency15,
       "ibDHCPv6DDNSAvgLatency60": ibDHCPv6DDNSAvgLatency60,
       "ibDHCPv6DDNSAvgLatency1440": ibDHCPv6DDNSAvgLatency1440,
       "ibDHCPv6DDNSTimeoutCount5": ibDHCPv6DDNSTimeoutCount5,
       "ibDHCPv6DDNSTimeoutCount15": ibDHCPv6DDNSTimeoutCount15,
       "ibDHCPv6DDNSTimeoutCount60": ibDHCPv6DDNSTimeoutCount60,
       "ibDHCPv6DDNSTimeoutCount1440": ibDHCPv6DDNSTimeoutCount1440}
)
