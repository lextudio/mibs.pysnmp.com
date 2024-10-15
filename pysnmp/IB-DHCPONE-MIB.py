# SNMP MIB module (IB-DHCPONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IB-DHCPONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:14 2024
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

(IbIpAddr,
 IbString,
 ibDHCPOne) = mibBuilder.importSymbols(
    "IB-SMI-MIB",
    "IbIpAddr",
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

ibDhcpModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1)
)
ibDhcpModule.setRevisions(
        ("2010-03-23 00:00",
         "2008-02-14 00:00",
         "2005-01-10 00:00",
         "2004-05-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbDHCPSubnetTable_Object = MibTable
ibDHCPSubnetTable = _IbDHCPSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ibDHCPSubnetTable.setStatus("current")
_IbDHCPSubnetEntry_Object = MibTableRow
ibDHCPSubnetEntry = _IbDHCPSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1)
)
ibDHCPSubnetEntry.setIndexNames(
    (0, "IB-DHCPONE-MIB", "ibDHCPSubnetNetworkAddress"),
)
if mibBuilder.loadTexts:
    ibDHCPSubnetEntry.setStatus("current")
_IbDHCPSubnetNetworkAddress_Type = IbIpAddr
_IbDHCPSubnetNetworkAddress_Object = MibTableColumn
ibDHCPSubnetNetworkAddress = _IbDHCPSubnetNetworkAddress_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 1),
    _IbDHCPSubnetNetworkAddress_Type()
)
ibDHCPSubnetNetworkAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPSubnetNetworkAddress.setStatus("current")
_IbDHCPSubnetNetworkMask_Type = IbIpAddr
_IbDHCPSubnetNetworkMask_Object = MibTableColumn
ibDHCPSubnetNetworkMask = _IbDHCPSubnetNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 2),
    _IbDHCPSubnetNetworkMask_Type()
)
ibDHCPSubnetNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPSubnetNetworkMask.setStatus("current")
_IbDHCPSubnetPercentUsed_Type = Integer32
_IbDHCPSubnetPercentUsed_Object = MibTableColumn
ibDHCPSubnetPercentUsed = _IbDHCPSubnetPercentUsed_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 3),
    _IbDHCPSubnetPercentUsed_Type()
)
ibDHCPSubnetPercentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPSubnetPercentUsed.setStatus("current")
_IbDHCPStatistics_ObjectIdentity = ObjectIdentity
ibDHCPStatistics = _IbDHCPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3)
)
_IbDhcpTotalNoOfDiscovers_Type = Counter32
_IbDhcpTotalNoOfDiscovers_Object = MibScalar
ibDhcpTotalNoOfDiscovers = _IbDhcpTotalNoOfDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 1),
    _IbDhcpTotalNoOfDiscovers_Type()
)
ibDhcpTotalNoOfDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfDiscovers.setStatus("current")
_IbDhcpTotalNoOfRequests_Type = Counter32
_IbDhcpTotalNoOfRequests_Object = MibScalar
ibDhcpTotalNoOfRequests = _IbDhcpTotalNoOfRequests_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 2),
    _IbDhcpTotalNoOfRequests_Type()
)
ibDhcpTotalNoOfRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfRequests.setStatus("current")
_IbDhcpTotalNoOfReleases_Type = Counter32
_IbDhcpTotalNoOfReleases_Object = MibScalar
ibDhcpTotalNoOfReleases = _IbDhcpTotalNoOfReleases_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 3),
    _IbDhcpTotalNoOfReleases_Type()
)
ibDhcpTotalNoOfReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfReleases.setStatus("current")
_IbDhcpTotalNoOfOffers_Type = Counter32
_IbDhcpTotalNoOfOffers_Object = MibScalar
ibDhcpTotalNoOfOffers = _IbDhcpTotalNoOfOffers_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 4),
    _IbDhcpTotalNoOfOffers_Type()
)
ibDhcpTotalNoOfOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfOffers.setStatus("current")
_IbDhcpTotalNoOfAcks_Type = Counter32
_IbDhcpTotalNoOfAcks_Object = MibScalar
ibDhcpTotalNoOfAcks = _IbDhcpTotalNoOfAcks_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 5),
    _IbDhcpTotalNoOfAcks_Type()
)
ibDhcpTotalNoOfAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfAcks.setStatus("current")
_IbDhcpTotalNoOfNacks_Type = Counter32
_IbDhcpTotalNoOfNacks_Object = MibScalar
ibDhcpTotalNoOfNacks = _IbDhcpTotalNoOfNacks_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 6),
    _IbDhcpTotalNoOfNacks_Type()
)
ibDhcpTotalNoOfNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfNacks.setStatus("current")
_IbDhcpTotalNoOfDeclines_Type = Counter32
_IbDhcpTotalNoOfDeclines_Object = MibScalar
ibDhcpTotalNoOfDeclines = _IbDhcpTotalNoOfDeclines_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 7),
    _IbDhcpTotalNoOfDeclines_Type()
)
ibDhcpTotalNoOfDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfDeclines.setStatus("current")
_IbDhcpTotalNoOfInforms_Type = Counter32
_IbDhcpTotalNoOfInforms_Object = MibScalar
ibDhcpTotalNoOfInforms = _IbDhcpTotalNoOfInforms_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 8),
    _IbDhcpTotalNoOfInforms_Type()
)
ibDhcpTotalNoOfInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfInforms.setStatus("current")
_IbDhcpTotalNoOfOthers_Type = Counter32
_IbDhcpTotalNoOfOthers_Object = MibScalar
ibDhcpTotalNoOfOthers = _IbDhcpTotalNoOfOthers_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 9),
    _IbDhcpTotalNoOfOthers_Type()
)
ibDhcpTotalNoOfOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpTotalNoOfOthers.setStatus("current")
_IbDhcpDeferredQueueSize_Type = Integer32
_IbDhcpDeferredQueueSize_Object = MibScalar
ibDhcpDeferredQueueSize = _IbDhcpDeferredQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 4),
    _IbDhcpDeferredQueueSize_Type()
)
ibDhcpDeferredQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDhcpDeferredQueueSize.setStatus("current")
_IbDHCPDDNSStats_ObjectIdentity = ObjectIdentity
ibDHCPDDNSStats = _IbDHCPDDNSStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5)
)
_IbDHCPDDNSAvgLatency5_Type = Counter64
_IbDHCPDDNSAvgLatency5_Object = MibScalar
ibDHCPDDNSAvgLatency5 = _IbDHCPDDNSAvgLatency5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 1),
    _IbDHCPDDNSAvgLatency5_Type()
)
ibDHCPDDNSAvgLatency5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSAvgLatency5.setStatus("current")
_IbDHCPDDNSAvgLatency15_Type = Counter64
_IbDHCPDDNSAvgLatency15_Object = MibScalar
ibDHCPDDNSAvgLatency15 = _IbDHCPDDNSAvgLatency15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 2),
    _IbDHCPDDNSAvgLatency15_Type()
)
ibDHCPDDNSAvgLatency15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSAvgLatency15.setStatus("current")
_IbDHCPDDNSAvgLatency60_Type = Counter64
_IbDHCPDDNSAvgLatency60_Object = MibScalar
ibDHCPDDNSAvgLatency60 = _IbDHCPDDNSAvgLatency60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 3),
    _IbDHCPDDNSAvgLatency60_Type()
)
ibDHCPDDNSAvgLatency60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSAvgLatency60.setStatus("current")
_IbDHCPDDNSAvgLatency1440_Type = Counter64
_IbDHCPDDNSAvgLatency1440_Object = MibScalar
ibDHCPDDNSAvgLatency1440 = _IbDHCPDDNSAvgLatency1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 4),
    _IbDHCPDDNSAvgLatency1440_Type()
)
ibDHCPDDNSAvgLatency1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSAvgLatency1440.setStatus("current")
_IbDHCPDDNSTimeoutCount5_Type = Unsigned32
_IbDHCPDDNSTimeoutCount5_Object = MibScalar
ibDHCPDDNSTimeoutCount5 = _IbDHCPDDNSTimeoutCount5_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 5),
    _IbDHCPDDNSTimeoutCount5_Type()
)
ibDHCPDDNSTimeoutCount5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSTimeoutCount5.setStatus("current")
_IbDHCPDDNSTimeoutCount15_Type = Unsigned32
_IbDHCPDDNSTimeoutCount15_Object = MibScalar
ibDHCPDDNSTimeoutCount15 = _IbDHCPDDNSTimeoutCount15_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 6),
    _IbDHCPDDNSTimeoutCount15_Type()
)
ibDHCPDDNSTimeoutCount15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSTimeoutCount15.setStatus("current")
_IbDHCPDDNSTimeoutCount60_Type = Unsigned32
_IbDHCPDDNSTimeoutCount60_Object = MibScalar
ibDHCPDDNSTimeoutCount60 = _IbDHCPDDNSTimeoutCount60_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 7),
    _IbDHCPDDNSTimeoutCount60_Type()
)
ibDHCPDDNSTimeoutCount60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSTimeoutCount60.setStatus("current")
_IbDHCPDDNSTimeoutCount1440_Type = Unsigned32
_IbDHCPDDNSTimeoutCount1440_Object = MibScalar
ibDHCPDDNSTimeoutCount1440 = _IbDHCPDDNSTimeoutCount1440_Object(
    (1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 8),
    _IbDHCPDDNSTimeoutCount1440_Type()
)
ibDHCPDDNSTimeoutCount1440.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibDHCPDDNSTimeoutCount1440.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IB-DHCPONE-MIB",
    **{"ibDhcpModule": ibDhcpModule,
       "ibDHCPSubnetTable": ibDHCPSubnetTable,
       "ibDHCPSubnetEntry": ibDHCPSubnetEntry,
       "ibDHCPSubnetNetworkAddress": ibDHCPSubnetNetworkAddress,
       "ibDHCPSubnetNetworkMask": ibDHCPSubnetNetworkMask,
       "ibDHCPSubnetPercentUsed": ibDHCPSubnetPercentUsed,
       "ibDHCPStatistics": ibDHCPStatistics,
       "ibDhcpTotalNoOfDiscovers": ibDhcpTotalNoOfDiscovers,
       "ibDhcpTotalNoOfRequests": ibDhcpTotalNoOfRequests,
       "ibDhcpTotalNoOfReleases": ibDhcpTotalNoOfReleases,
       "ibDhcpTotalNoOfOffers": ibDhcpTotalNoOfOffers,
       "ibDhcpTotalNoOfAcks": ibDhcpTotalNoOfAcks,
       "ibDhcpTotalNoOfNacks": ibDhcpTotalNoOfNacks,
       "ibDhcpTotalNoOfDeclines": ibDhcpTotalNoOfDeclines,
       "ibDhcpTotalNoOfInforms": ibDhcpTotalNoOfInforms,
       "ibDhcpTotalNoOfOthers": ibDhcpTotalNoOfOthers,
       "ibDhcpDeferredQueueSize": ibDhcpDeferredQueueSize,
       "ibDHCPDDNSStats": ibDHCPDDNSStats,
       "ibDHCPDDNSAvgLatency5": ibDHCPDDNSAvgLatency5,
       "ibDHCPDDNSAvgLatency15": ibDHCPDDNSAvgLatency15,
       "ibDHCPDDNSAvgLatency60": ibDHCPDDNSAvgLatency60,
       "ibDHCPDDNSAvgLatency1440": ibDHCPDDNSAvgLatency1440,
       "ibDHCPDDNSTimeoutCount5": ibDHCPDDNSTimeoutCount5,
       "ibDHCPDDNSTimeoutCount15": ibDHCPDDNSTimeoutCount15,
       "ibDHCPDDNSTimeoutCount60": ibDHCPDDNSTimeoutCount60,
       "ibDHCPDDNSTimeoutCount1440": ibDHCPDDNSTimeoutCount1440}
)
