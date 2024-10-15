# SNMP MIB module (DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DHCP-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:00 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dhcpServMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DhcpServTimeInterval(Gauge32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Lucent_ObjectIdentity = ObjectIdentity
lucent = _Lucent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1)
)
_Ipspg_ObjectIdentity = ObjectIdentity
ipspg = _Ipspg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48)
)
_IpspgServices_ObjectIdentity = ObjectIdentity
ipspgServices = _IpspgServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1)
)
_IpspgDHCP_ObjectIdentity = ObjectIdentity
ipspgDHCP = _IpspgDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1)
)
_DhcpServMibTraps_ObjectIdentity = ObjectIdentity
dhcpServMibTraps = _DhcpServMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0)
)
if mibBuilder.loadTexts:
    dhcpServMibTraps.setStatus("current")
_DhcpServMibObjects_ObjectIdentity = ObjectIdentity
dhcpServMibObjects = _DhcpServMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpServMibObjects.setStatus("current")
_DhcpServSystem_ObjectIdentity = ObjectIdentity
dhcpServSystem = _DhcpServSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpServSystem.setStatus("current")


class _DhcpServSystemDescr_Type(DisplayString):
    """Custom type dhcpServSystemDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhcpServSystemDescr_Type.__name__ = "DisplayString"
_DhcpServSystemDescr_Object = MibScalar
dhcpServSystemDescr = _DhcpServSystemDescr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 1),
    _DhcpServSystemDescr_Type()
)
dhcpServSystemDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServSystemDescr.setStatus("current")


class _DhcpServSystemStatus_Type(Integer32):
    """Custom type dhcpServSystemStatus based on Integer32"""
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
        *(("reload", 4),
          ("running", 1),
          ("starting", 0),
          ("stopped", 3),
          ("stopping", 2))
    )


_DhcpServSystemStatus_Type.__name__ = "Integer32"
_DhcpServSystemStatus_Object = MibScalar
dhcpServSystemStatus = _DhcpServSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 2),
    _DhcpServSystemStatus_Type()
)
dhcpServSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServSystemStatus.setStatus("current")
_DhcpServSystemUpTime_Type = Gauge32
_DhcpServSystemUpTime_Object = MibScalar
dhcpServSystemUpTime = _DhcpServSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 3),
    _DhcpServSystemUpTime_Type()
)
dhcpServSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServSystemUpTime.setStatus("current")
_DhcpServSystemResetTime_Type = Gauge32
_DhcpServSystemResetTime_Object = MibScalar
dhcpServSystemResetTime = _DhcpServSystemResetTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 1, 4),
    _DhcpServSystemResetTime_Type()
)
dhcpServSystemResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServSystemResetTime.setStatus("current")
_DhcpServSubnetCounters_ObjectIdentity = ObjectIdentity
dhcpServSubnetCounters = _DhcpServSubnetCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dhcpServSubnetCounters.setStatus("current")
_DhcpServCountUsedSubnets_Type = Integer32
_DhcpServCountUsedSubnets_Object = MibScalar
dhcpServCountUsedSubnets = _DhcpServCountUsedSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2, 1),
    _DhcpServCountUsedSubnets_Type()
)
dhcpServCountUsedSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServCountUsedSubnets.setStatus("current")
_DhcpServCountUnusedSubnets_Type = Integer32
_DhcpServCountUnusedSubnets_Object = MibScalar
dhcpServCountUnusedSubnets = _DhcpServCountUnusedSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2, 2),
    _DhcpServCountUnusedSubnets_Type()
)
dhcpServCountUnusedSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServCountUnusedSubnets.setStatus("current")
_DhcpServCountFullSubnets_Type = Integer32
_DhcpServCountFullSubnets_Object = MibScalar
dhcpServCountFullSubnets = _DhcpServCountFullSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 2, 3),
    _DhcpServCountFullSubnets_Type()
)
dhcpServCountFullSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServCountFullSubnets.setStatus("current")
_DhcpServBootpCounters_ObjectIdentity = ObjectIdentity
dhcpServBootpCounters = _DhcpServBootpCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    dhcpServBootpCounters.setStatus("current")
_DhcpServBootpCountRequests_Type = Counter32
_DhcpServBootpCountRequests_Object = MibScalar
dhcpServBootpCountRequests = _DhcpServBootpCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 1),
    _DhcpServBootpCountRequests_Type()
)
dhcpServBootpCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpCountRequests.setStatus("current")
_DhcpServBootpCountInvalids_Type = Counter32
_DhcpServBootpCountInvalids_Object = MibScalar
dhcpServBootpCountInvalids = _DhcpServBootpCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 2),
    _DhcpServBootpCountInvalids_Type()
)
dhcpServBootpCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpCountInvalids.setStatus("current")
_DhcpServBootpCountReplies_Type = Counter32
_DhcpServBootpCountReplies_Object = MibScalar
dhcpServBootpCountReplies = _DhcpServBootpCountReplies_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 3),
    _DhcpServBootpCountReplies_Type()
)
dhcpServBootpCountReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpCountReplies.setStatus("current")
_DhcpServBootpCountDroppedUnknownClients_Type = Counter32
_DhcpServBootpCountDroppedUnknownClients_Object = MibScalar
dhcpServBootpCountDroppedUnknownClients = _DhcpServBootpCountDroppedUnknownClients_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 4),
    _DhcpServBootpCountDroppedUnknownClients_Type()
)
dhcpServBootpCountDroppedUnknownClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpCountDroppedUnknownClients.setStatus("current")
_DhcpServBootpCountDroppedNotServingSubnet_Type = Counter32
_DhcpServBootpCountDroppedNotServingSubnet_Object = MibScalar
dhcpServBootpCountDroppedNotServingSubnet = _DhcpServBootpCountDroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 3, 5),
    _DhcpServBootpCountDroppedNotServingSubnet_Type()
)
dhcpServBootpCountDroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpCountDroppedNotServingSubnet.setStatus("current")
_DhcpServDhcpCounters_ObjectIdentity = ObjectIdentity
dhcpServDhcpCounters = _DhcpServDhcpCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dhcpServDhcpCounters.setStatus("current")
_DhcpServDhcpCountDiscovers_Type = Counter32
_DhcpServDhcpCountDiscovers_Object = MibScalar
dhcpServDhcpCountDiscovers = _DhcpServDhcpCountDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 1),
    _DhcpServDhcpCountDiscovers_Type()
)
dhcpServDhcpCountDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountDiscovers.setStatus("current")
_DhcpServDhcpCountRequests_Type = Counter32
_DhcpServDhcpCountRequests_Object = MibScalar
dhcpServDhcpCountRequests = _DhcpServDhcpCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 2),
    _DhcpServDhcpCountRequests_Type()
)
dhcpServDhcpCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountRequests.setStatus("current")
_DhcpServDhcpCountReleases_Type = Counter32
_DhcpServDhcpCountReleases_Object = MibScalar
dhcpServDhcpCountReleases = _DhcpServDhcpCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 3),
    _DhcpServDhcpCountReleases_Type()
)
dhcpServDhcpCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountReleases.setStatus("current")
_DhcpServDhcpCountDeclines_Type = Counter32
_DhcpServDhcpCountDeclines_Object = MibScalar
dhcpServDhcpCountDeclines = _DhcpServDhcpCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 4),
    _DhcpServDhcpCountDeclines_Type()
)
dhcpServDhcpCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountDeclines.setStatus("current")
_DhcpServDhcpCountInforms_Type = Counter32
_DhcpServDhcpCountInforms_Object = MibScalar
dhcpServDhcpCountInforms = _DhcpServDhcpCountInforms_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 5),
    _DhcpServDhcpCountInforms_Type()
)
dhcpServDhcpCountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountInforms.setStatus("current")
_DhcpServDhcpCountInvalids_Type = Counter32
_DhcpServDhcpCountInvalids_Object = MibScalar
dhcpServDhcpCountInvalids = _DhcpServDhcpCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 6),
    _DhcpServDhcpCountInvalids_Type()
)
dhcpServDhcpCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountInvalids.setStatus("current")
_DhcpServDhcpCountOffers_Type = Counter32
_DhcpServDhcpCountOffers_Object = MibScalar
dhcpServDhcpCountOffers = _DhcpServDhcpCountOffers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 7),
    _DhcpServDhcpCountOffers_Type()
)
dhcpServDhcpCountOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountOffers.setStatus("current")
_DhcpServDhcpCountAcks_Type = Counter32
_DhcpServDhcpCountAcks_Object = MibScalar
dhcpServDhcpCountAcks = _DhcpServDhcpCountAcks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 8),
    _DhcpServDhcpCountAcks_Type()
)
dhcpServDhcpCountAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountAcks.setStatus("current")
_DhcpServDhcpCountNacks_Type = Counter32
_DhcpServDhcpCountNacks_Object = MibScalar
dhcpServDhcpCountNacks = _DhcpServDhcpCountNacks_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 9),
    _DhcpServDhcpCountNacks_Type()
)
dhcpServDhcpCountNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountNacks.setStatus("current")
_DhcpServDhcpCountDroppedUnknownClient_Type = Counter32
_DhcpServDhcpCountDroppedUnknownClient_Object = MibScalar
dhcpServDhcpCountDroppedUnknownClient = _DhcpServDhcpCountDroppedUnknownClient_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 10),
    _DhcpServDhcpCountDroppedUnknownClient_Type()
)
dhcpServDhcpCountDroppedUnknownClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountDroppedUnknownClient.setStatus("current")
_DhcpServDhcpCountDroppedNotServingSubnet_Type = Counter32
_DhcpServDhcpCountDroppedNotServingSubnet_Object = MibScalar
dhcpServDhcpCountDroppedNotServingSubnet = _DhcpServDhcpCountDroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 4, 11),
    _DhcpServDhcpCountDroppedNotServingSubnet_Type()
)
dhcpServDhcpCountDroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpCountDroppedNotServingSubnet.setStatus("current")
_DhcpServBootpStatistics_ObjectIdentity = ObjectIdentity
dhcpServBootpStatistics = _DhcpServBootpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dhcpServBootpStatistics.setStatus("current")
_DhcpServBootpStatMinArrivalInterval_Type = DhcpServTimeInterval
_DhcpServBootpStatMinArrivalInterval_Object = MibScalar
dhcpServBootpStatMinArrivalInterval = _DhcpServBootpStatMinArrivalInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 1),
    _DhcpServBootpStatMinArrivalInterval_Type()
)
dhcpServBootpStatMinArrivalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpStatMinArrivalInterval.setStatus("current")
_DhcpServBootpStatMaxArrivalInterval_Type = DhcpServTimeInterval
_DhcpServBootpStatMaxArrivalInterval_Object = MibScalar
dhcpServBootpStatMaxArrivalInterval = _DhcpServBootpStatMaxArrivalInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 2),
    _DhcpServBootpStatMaxArrivalInterval_Type()
)
dhcpServBootpStatMaxArrivalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpStatMaxArrivalInterval.setStatus("current")
_DhcpServBootpStatLastArrivalTime_Type = TimeTicks
_DhcpServBootpStatLastArrivalTime_Object = MibScalar
dhcpServBootpStatLastArrivalTime = _DhcpServBootpStatLastArrivalTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 3),
    _DhcpServBootpStatLastArrivalTime_Type()
)
dhcpServBootpStatLastArrivalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpStatLastArrivalTime.setStatus("current")
_DhcpServBootpStatMinResponseTime_Type = DhcpServTimeInterval
_DhcpServBootpStatMinResponseTime_Object = MibScalar
dhcpServBootpStatMinResponseTime = _DhcpServBootpStatMinResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 4),
    _DhcpServBootpStatMinResponseTime_Type()
)
dhcpServBootpStatMinResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpStatMinResponseTime.setStatus("current")
_DhcpServBootpStatMaxResponseTime_Type = DhcpServTimeInterval
_DhcpServBootpStatMaxResponseTime_Object = MibScalar
dhcpServBootpStatMaxResponseTime = _DhcpServBootpStatMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 5),
    _DhcpServBootpStatMaxResponseTime_Type()
)
dhcpServBootpStatMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpStatMaxResponseTime.setStatus("current")
_DhcpServBootpStatSumResponseTime_Type = DhcpServTimeInterval
_DhcpServBootpStatSumResponseTime_Object = MibScalar
dhcpServBootpStatSumResponseTime = _DhcpServBootpStatSumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 5, 6),
    _DhcpServBootpStatSumResponseTime_Type()
)
dhcpServBootpStatSumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServBootpStatSumResponseTime.setStatus("current")
_DhcpServDhcpStatistics_ObjectIdentity = ObjectIdentity
dhcpServDhcpStatistics = _DhcpServDhcpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    dhcpServDhcpStatistics.setStatus("current")
_DhcpServDhcpStatMinArrivalInterval_Type = DhcpServTimeInterval
_DhcpServDhcpStatMinArrivalInterval_Object = MibScalar
dhcpServDhcpStatMinArrivalInterval = _DhcpServDhcpStatMinArrivalInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 1),
    _DhcpServDhcpStatMinArrivalInterval_Type()
)
dhcpServDhcpStatMinArrivalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpStatMinArrivalInterval.setStatus("current")
_DhcpServDhcpStatMaxArrivalInterval_Type = DhcpServTimeInterval
_DhcpServDhcpStatMaxArrivalInterval_Object = MibScalar
dhcpServDhcpStatMaxArrivalInterval = _DhcpServDhcpStatMaxArrivalInterval_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 2),
    _DhcpServDhcpStatMaxArrivalInterval_Type()
)
dhcpServDhcpStatMaxArrivalInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpStatMaxArrivalInterval.setStatus("current")
_DhcpServDhcpStatLastArrivalTime_Type = TimeTicks
_DhcpServDhcpStatLastArrivalTime_Object = MibScalar
dhcpServDhcpStatLastArrivalTime = _DhcpServDhcpStatLastArrivalTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 3),
    _DhcpServDhcpStatLastArrivalTime_Type()
)
dhcpServDhcpStatLastArrivalTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpStatLastArrivalTime.setStatus("current")
_DhcpServDhcpStatMinResponseTime_Type = DhcpServTimeInterval
_DhcpServDhcpStatMinResponseTime_Object = MibScalar
dhcpServDhcpStatMinResponseTime = _DhcpServDhcpStatMinResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 4),
    _DhcpServDhcpStatMinResponseTime_Type()
)
dhcpServDhcpStatMinResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpStatMinResponseTime.setStatus("current")
_DhcpServDhcpStatMaxResponseTime_Type = DhcpServTimeInterval
_DhcpServDhcpStatMaxResponseTime_Object = MibScalar
dhcpServDhcpStatMaxResponseTime = _DhcpServDhcpStatMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 5),
    _DhcpServDhcpStatMaxResponseTime_Type()
)
dhcpServDhcpStatMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpStatMaxResponseTime.setStatus("current")
_DhcpServDhcpStatSumResponseTime_Type = DhcpServTimeInterval
_DhcpServDhcpStatSumResponseTime_Object = MibScalar
dhcpServDhcpStatSumResponseTime = _DhcpServDhcpStatSumResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 6, 6),
    _DhcpServDhcpStatSumResponseTime_Type()
)
dhcpServDhcpStatSumResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServDhcpStatSumResponseTime.setStatus("current")
_DhcpServConfiguration_ObjectIdentity = ObjectIdentity
dhcpServConfiguration = _DhcpServConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    dhcpServConfiguration.setStatus("current")
_DhcpServRangeTable_Object = MibTable
dhcpServRangeTable = _DhcpServRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    dhcpServRangeTable.setStatus("current")
_DhcpServRangeEntry_Object = MibTableRow
dhcpServRangeEntry = _DhcpServRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1)
)
dhcpServRangeEntry.setIndexNames(
    (0, "DHCP-SERVER-MIB", "dhcpServRangeSubnetAddr"),
    (0, "DHCP-SERVER-MIB", "dhcpServRangeStart"),
)
if mibBuilder.loadTexts:
    dhcpServRangeEntry.setStatus("current")
_DhcpServRangeSubnetAddr_Type = IpAddress
_DhcpServRangeSubnetAddr_Object = MibTableColumn
dhcpServRangeSubnetAddr = _DhcpServRangeSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 1),
    _DhcpServRangeSubnetAddr_Type()
)
dhcpServRangeSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeSubnetAddr.setStatus("current")
_DhcpServRangeSubnetMask_Type = IpAddress
_DhcpServRangeSubnetMask_Object = MibTableColumn
dhcpServRangeSubnetMask = _DhcpServRangeSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 2),
    _DhcpServRangeSubnetMask_Type()
)
dhcpServRangeSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeSubnetMask.setStatus("current")
_DhcpServRangeStart_Type = IpAddress
_DhcpServRangeStart_Object = MibTableColumn
dhcpServRangeStart = _DhcpServRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 3),
    _DhcpServRangeStart_Type()
)
dhcpServRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeStart.setStatus("current")
_DhcpServRangeEnd_Type = IpAddress
_DhcpServRangeEnd_Object = MibTableColumn
dhcpServRangeEnd = _DhcpServRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 4),
    _DhcpServRangeEnd_Type()
)
dhcpServRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeEnd.setStatus("current")
_DhcpServRangeInUse_Type = Gauge32
_DhcpServRangeInUse_Object = MibTableColumn
dhcpServRangeInUse = _DhcpServRangeInUse_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 5),
    _DhcpServRangeInUse_Type()
)
dhcpServRangeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeInUse.setStatus("current")
_DhcpServRangeOutstandingOffers_Type = Gauge32
_DhcpServRangeOutstandingOffers_Object = MibTableColumn
dhcpServRangeOutstandingOffers = _DhcpServRangeOutstandingOffers_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 6),
    _DhcpServRangeOutstandingOffers_Type()
)
dhcpServRangeOutstandingOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeOutstandingOffers.setStatus("current")
_DhcpServRangeUnavailable_Type = Gauge32
_DhcpServRangeUnavailable_Object = MibTableColumn
dhcpServRangeUnavailable = _DhcpServRangeUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 7),
    _DhcpServRangeUnavailable_Type()
)
dhcpServRangeUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeUnavailable.setStatus("current")


class _DhcpServRangeType_Type(Integer32):
    """Custom type dhcpServRangeType based on Integer32"""
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
        *(("autoBootp", 2),
          ("autoDhcp", 4),
          ("dynamicDhcp", 5),
          ("manBootp", 1),
          ("manDhcp", 3))
    )


_DhcpServRangeType_Type.__name__ = "Integer32"
_DhcpServRangeType_Object = MibTableColumn
dhcpServRangeType = _DhcpServRangeType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 8),
    _DhcpServRangeType_Type()
)
dhcpServRangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeType.setStatus("current")
_DhcpServRangeUnused_Type = Gauge32
_DhcpServRangeUnused_Object = MibTableColumn
dhcpServRangeUnused = _DhcpServRangeUnused_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 7, 2, 1, 9),
    _DhcpServRangeUnused_Type()
)
dhcpServRangeUnused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServRangeUnused.setStatus("current")
_DhcpServFailover_ObjectIdentity = ObjectIdentity
dhcpServFailover = _DhcpServFailover_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    dhcpServFailover.setStatus("current")
_DhcpServFailoverTable_Object = MibTable
dhcpServFailoverTable = _DhcpServFailoverTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    dhcpServFailoverTable.setStatus("current")
_DhcpServFailoverEntry_Object = MibTableRow
dhcpServFailoverEntry = _DhcpServFailoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1)
)
dhcpServFailoverEntry.setIndexNames(
    (0, "DHCP-SERVER-MIB", "dhcpServFailoverPartnerAddr"),
)
if mibBuilder.loadTexts:
    dhcpServFailoverEntry.setStatus("current")
_DhcpServFailoverPartnerAddr_Type = IpAddress
_DhcpServFailoverPartnerAddr_Object = MibTableColumn
dhcpServFailoverPartnerAddr = _DhcpServFailoverPartnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 1),
    _DhcpServFailoverPartnerAddr_Type()
)
dhcpServFailoverPartnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServFailoverPartnerAddr.setStatus("current")


class _DhcpServFailoverPartnerType_Type(Integer32):
    """Custom type dhcpServFailoverPartnerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failover", 2),
          ("primary", 1),
          ("unconfigured", 3))
    )


_DhcpServFailoverPartnerType_Type.__name__ = "Integer32"
_DhcpServFailoverPartnerType_Object = MibTableColumn
dhcpServFailoverPartnerType = _DhcpServFailoverPartnerType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 2),
    _DhcpServFailoverPartnerType_Type()
)
dhcpServFailoverPartnerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServFailoverPartnerType.setStatus("current")


class _DhcpServFailoverPartnerStatus_Type(Integer32):
    """Custom type dhcpServFailoverPartnerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("syncing", 1),
          ("unknown", 0))
    )


_DhcpServFailoverPartnerStatus_Type.__name__ = "Integer32"
_DhcpServFailoverPartnerStatus_Object = MibTableColumn
dhcpServFailoverPartnerStatus = _DhcpServFailoverPartnerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 3),
    _DhcpServFailoverPartnerStatus_Type()
)
dhcpServFailoverPartnerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServFailoverPartnerStatus.setStatus("current")
_DhcpServFailoverPartnerPolltime_Type = Counter32
_DhcpServFailoverPartnerPolltime_Object = MibTableColumn
dhcpServFailoverPartnerPolltime = _DhcpServFailoverPartnerPolltime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 1, 8, 1, 1, 4),
    _DhcpServFailoverPartnerPolltime_Type()
)
dhcpServFailoverPartnerPolltime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServFailoverPartnerPolltime.setStatus("current")
_IpspgDNS_ObjectIdentity = ObjectIdentity
ipspgDNS = _IpspgDNS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 2)
)
_IpspgTrap_ObjectIdentity = ObjectIdentity
ipspgTrap = _IpspgTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2)
)
_IpspgDhcpTrapTable_Object = MibTable
ipspgDhcpTrapTable = _IpspgDhcpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1)
)
if mibBuilder.loadTexts:
    ipspgDhcpTrapTable.setStatus("current")
_IpspgDhcpTrapEntry_Object = MibTableRow
ipspgDhcpTrapEntry = _IpspgDhcpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1)
)
ipspgDhcpTrapEntry.setIndexNames(
    (0, "DHCP-SERVER-MIB", "ipspgDhcpTrIndex"),
)
if mibBuilder.loadTexts:
    ipspgDhcpTrapEntry.setStatus("current")


class _IpspgDhcpTrIndex_Type(Integer32):
    """Custom type ipspgDhcpTrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_IpspgDhcpTrIndex_Type.__name__ = "Integer32"
_IpspgDhcpTrIndex_Object = MibTableColumn
ipspgDhcpTrIndex = _IpspgDhcpTrIndex_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 1),
    _IpspgDhcpTrIndex_Type()
)
ipspgDhcpTrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrIndex.setStatus("current")
_IpspgDhcpTrSequence_Type = Counter32
_IpspgDhcpTrSequence_Object = MibTableColumn
ipspgDhcpTrSequence = _IpspgDhcpTrSequence_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 2),
    _IpspgDhcpTrSequence_Type()
)
ipspgDhcpTrSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrSequence.setStatus("current")


class _IpspgDhcpTrId_Type(Integer32):
    """Custom type ipspgDhcpTrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analyzer", 3),
          ("monitor", 1))
    )


_IpspgDhcpTrId_Type.__name__ = "Integer32"
_IpspgDhcpTrId_Object = MibTableColumn
ipspgDhcpTrId = _IpspgDhcpTrId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 3),
    _IpspgDhcpTrId_Type()
)
ipspgDhcpTrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrId.setStatus("current")


class _IpspgDhcpTrText_Type(DisplayString):
    """Custom type ipspgDhcpTrText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_IpspgDhcpTrText_Type.__name__ = "DisplayString"
_IpspgDhcpTrText_Object = MibTableColumn
ipspgDhcpTrText = _IpspgDhcpTrText_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 4),
    _IpspgDhcpTrText_Type()
)
ipspgDhcpTrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrText.setStatus("current")


class _IpspgDhcpTrPriority_Type(Integer32):
    """Custom type ipspgDhcpTrPriority based on Integer32"""
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
        *(("critical", 5),
          ("inform", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_IpspgDhcpTrPriority_Type.__name__ = "Integer32"
_IpspgDhcpTrPriority_Object = MibTableColumn
ipspgDhcpTrPriority = _IpspgDhcpTrPriority_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 5),
    _IpspgDhcpTrPriority_Type()
)
ipspgDhcpTrPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrPriority.setStatus("current")


class _IpspgDhcpTrClass_Type(Integer32):
    """Custom type ipspgDhcpTrClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpspgDhcpTrClass_Type.__name__ = "Integer32"
_IpspgDhcpTrClass_Object = MibTableColumn
ipspgDhcpTrClass = _IpspgDhcpTrClass_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 6),
    _IpspgDhcpTrClass_Type()
)
ipspgDhcpTrClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrClass.setStatus("current")


class _IpspgDhcpTrType_Type(Integer32):
    """Custom type ipspgDhcpTrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpspgDhcpTrType_Type.__name__ = "Integer32"
_IpspgDhcpTrType_Object = MibTableColumn
ipspgDhcpTrType = _IpspgDhcpTrType_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 7),
    _IpspgDhcpTrType_Type()
)
ipspgDhcpTrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrType.setStatus("current")
_IpspgDhcpTrTime_Type = Counter32
_IpspgDhcpTrTime_Object = MibTableColumn
ipspgDhcpTrTime = _IpspgDhcpTrTime_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 8),
    _IpspgDhcpTrTime_Type()
)
ipspgDhcpTrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrTime.setStatus("current")


class _IpspgDhcpTrSuspect_Type(DisplayString):
    """Custom type ipspgDhcpTrSuspect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpspgDhcpTrSuspect_Type.__name__ = "DisplayString"
_IpspgDhcpTrSuspect_Object = MibTableColumn
ipspgDhcpTrSuspect = _IpspgDhcpTrSuspect_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 9),
    _IpspgDhcpTrSuspect_Type()
)
ipspgDhcpTrSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrSuspect.setStatus("current")


class _IpspgDhcpTrDiagId_Type(Integer32):
    """Custom type ipspgDhcpTrDiagId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpspgDhcpTrDiagId_Type.__name__ = "Integer32"
_IpspgDhcpTrDiagId_Object = MibTableColumn
ipspgDhcpTrDiagId = _IpspgDhcpTrDiagId_Object(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 2, 1, 1, 10),
    _IpspgDhcpTrDiagId_Type()
)
ipspgDhcpTrDiagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipspgDhcpTrDiagId.setStatus("current")
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1751, 2)
)

# Managed Objects groups


# Notification objects

dhcpServerStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 1)
)
dhcpServerStarted.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerStarted.setStatus(
        "current"
    )

dhcpServerStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 2)
)
dhcpServerStopped.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerStopped.setStatus(
        "current"
    )

dhcpServerReload = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 3)
)
dhcpServerReload.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerReload.setStatus(
        "current"
    )

dhcpServerSubnetDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 4)
)
dhcpServerSubnetDepleted.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerSubnetDepleted.setStatus(
        "current"
    )

dhcpServerBadPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 5)
)
dhcpServerBadPacket.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerBadPacket.setStatus(
        "current"
    )

dhcpServerFailoverActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 6)
)
dhcpServerFailoverActive.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerFailoverActive.setStatus(
        "current"
    )

dhcpServerFailoverReturnedControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 7)
)
dhcpServerFailoverReturnedControl.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerFailoverReturnedControl.setStatus(
        "current"
    )

dhcpServerSubnetThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 8)
)
dhcpServerSubnetThresholdExceeded.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerSubnetThresholdExceeded.setStatus(
        "current"
    )

dhcpServerSubnetThresholdDescent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 9)
)
dhcpServerSubnetThresholdDescent.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerSubnetThresholdDescent.setStatus(
        "current"
    )

dhcpServerDropUnknownClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 10)
)
dhcpServerDropUnknownClient.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerDropUnknownClient.setStatus(
        "current"
    )

dhcpServerPingResponseReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 1751, 1, 48, 1, 1, 1, 0, 11)
)
dhcpServerPingResponseReceived.setObjects(
      *(("DHCP-SERVER-MIB", "ipspgDhcpTrSequence"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrId"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrText"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrPriority"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrClass"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrType"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrTime"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrSuspect"),
        ("DHCP-SERVER-MIB", "ipspgDhcpTrDiagId"))
)
if mibBuilder.loadTexts:
    dhcpServerPingResponseReceived.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-SERVER-MIB",
    **{"DhcpServTimeInterval": DhcpServTimeInterval,
       "lucent": lucent,
       "products": products,
       "ipspg": ipspg,
       "ipspgServices": ipspgServices,
       "ipspgDHCP": ipspgDHCP,
       "dhcpServMib": dhcpServMib,
       "dhcpServMibTraps": dhcpServMibTraps,
       "dhcpServerStarted": dhcpServerStarted,
       "dhcpServerStopped": dhcpServerStopped,
       "dhcpServerReload": dhcpServerReload,
       "dhcpServerSubnetDepleted": dhcpServerSubnetDepleted,
       "dhcpServerBadPacket": dhcpServerBadPacket,
       "dhcpServerFailoverActive": dhcpServerFailoverActive,
       "dhcpServerFailoverReturnedControl": dhcpServerFailoverReturnedControl,
       "dhcpServerSubnetThresholdExceeded": dhcpServerSubnetThresholdExceeded,
       "dhcpServerSubnetThresholdDescent": dhcpServerSubnetThresholdDescent,
       "dhcpServerDropUnknownClient": dhcpServerDropUnknownClient,
       "dhcpServerPingResponseReceived": dhcpServerPingResponseReceived,
       "dhcpServMibObjects": dhcpServMibObjects,
       "dhcpServSystem": dhcpServSystem,
       "dhcpServSystemDescr": dhcpServSystemDescr,
       "dhcpServSystemStatus": dhcpServSystemStatus,
       "dhcpServSystemUpTime": dhcpServSystemUpTime,
       "dhcpServSystemResetTime": dhcpServSystemResetTime,
       "dhcpServSubnetCounters": dhcpServSubnetCounters,
       "dhcpServCountUsedSubnets": dhcpServCountUsedSubnets,
       "dhcpServCountUnusedSubnets": dhcpServCountUnusedSubnets,
       "dhcpServCountFullSubnets": dhcpServCountFullSubnets,
       "dhcpServBootpCounters": dhcpServBootpCounters,
       "dhcpServBootpCountRequests": dhcpServBootpCountRequests,
       "dhcpServBootpCountInvalids": dhcpServBootpCountInvalids,
       "dhcpServBootpCountReplies": dhcpServBootpCountReplies,
       "dhcpServBootpCountDroppedUnknownClients": dhcpServBootpCountDroppedUnknownClients,
       "dhcpServBootpCountDroppedNotServingSubnet": dhcpServBootpCountDroppedNotServingSubnet,
       "dhcpServDhcpCounters": dhcpServDhcpCounters,
       "dhcpServDhcpCountDiscovers": dhcpServDhcpCountDiscovers,
       "dhcpServDhcpCountRequests": dhcpServDhcpCountRequests,
       "dhcpServDhcpCountReleases": dhcpServDhcpCountReleases,
       "dhcpServDhcpCountDeclines": dhcpServDhcpCountDeclines,
       "dhcpServDhcpCountInforms": dhcpServDhcpCountInforms,
       "dhcpServDhcpCountInvalids": dhcpServDhcpCountInvalids,
       "dhcpServDhcpCountOffers": dhcpServDhcpCountOffers,
       "dhcpServDhcpCountAcks": dhcpServDhcpCountAcks,
       "dhcpServDhcpCountNacks": dhcpServDhcpCountNacks,
       "dhcpServDhcpCountDroppedUnknownClient": dhcpServDhcpCountDroppedUnknownClient,
       "dhcpServDhcpCountDroppedNotServingSubnet": dhcpServDhcpCountDroppedNotServingSubnet,
       "dhcpServBootpStatistics": dhcpServBootpStatistics,
       "dhcpServBootpStatMinArrivalInterval": dhcpServBootpStatMinArrivalInterval,
       "dhcpServBootpStatMaxArrivalInterval": dhcpServBootpStatMaxArrivalInterval,
       "dhcpServBootpStatLastArrivalTime": dhcpServBootpStatLastArrivalTime,
       "dhcpServBootpStatMinResponseTime": dhcpServBootpStatMinResponseTime,
       "dhcpServBootpStatMaxResponseTime": dhcpServBootpStatMaxResponseTime,
       "dhcpServBootpStatSumResponseTime": dhcpServBootpStatSumResponseTime,
       "dhcpServDhcpStatistics": dhcpServDhcpStatistics,
       "dhcpServDhcpStatMinArrivalInterval": dhcpServDhcpStatMinArrivalInterval,
       "dhcpServDhcpStatMaxArrivalInterval": dhcpServDhcpStatMaxArrivalInterval,
       "dhcpServDhcpStatLastArrivalTime": dhcpServDhcpStatLastArrivalTime,
       "dhcpServDhcpStatMinResponseTime": dhcpServDhcpStatMinResponseTime,
       "dhcpServDhcpStatMaxResponseTime": dhcpServDhcpStatMaxResponseTime,
       "dhcpServDhcpStatSumResponseTime": dhcpServDhcpStatSumResponseTime,
       "dhcpServConfiguration": dhcpServConfiguration,
       "dhcpServRangeTable": dhcpServRangeTable,
       "dhcpServRangeEntry": dhcpServRangeEntry,
       "dhcpServRangeSubnetAddr": dhcpServRangeSubnetAddr,
       "dhcpServRangeSubnetMask": dhcpServRangeSubnetMask,
       "dhcpServRangeStart": dhcpServRangeStart,
       "dhcpServRangeEnd": dhcpServRangeEnd,
       "dhcpServRangeInUse": dhcpServRangeInUse,
       "dhcpServRangeOutstandingOffers": dhcpServRangeOutstandingOffers,
       "dhcpServRangeUnavailable": dhcpServRangeUnavailable,
       "dhcpServRangeType": dhcpServRangeType,
       "dhcpServRangeUnused": dhcpServRangeUnused,
       "dhcpServFailover": dhcpServFailover,
       "dhcpServFailoverTable": dhcpServFailoverTable,
       "dhcpServFailoverEntry": dhcpServFailoverEntry,
       "dhcpServFailoverPartnerAddr": dhcpServFailoverPartnerAddr,
       "dhcpServFailoverPartnerType": dhcpServFailoverPartnerType,
       "dhcpServFailoverPartnerStatus": dhcpServFailoverPartnerStatus,
       "dhcpServFailoverPartnerPolltime": dhcpServFailoverPartnerPolltime,
       "ipspgDNS": ipspgDNS,
       "ipspgTrap": ipspgTrap,
       "ipspgDhcpTrapTable": ipspgDhcpTrapTable,
       "ipspgDhcpTrapEntry": ipspgDhcpTrapEntry,
       "ipspgDhcpTrIndex": ipspgDhcpTrIndex,
       "ipspgDhcpTrSequence": ipspgDhcpTrSequence,
       "ipspgDhcpTrId": ipspgDhcpTrId,
       "ipspgDhcpTrText": ipspgDhcpTrText,
       "ipspgDhcpTrPriority": ipspgDhcpTrPriority,
       "ipspgDhcpTrClass": ipspgDhcpTrClass,
       "ipspgDhcpTrType": ipspgDhcpTrType,
       "ipspgDhcpTrTime": ipspgDhcpTrTime,
       "ipspgDhcpTrSuspect": ipspgDhcpTrSuspect,
       "ipspgDhcpTrDiagId": ipspgDhcpTrDiagId,
       "mibs": mibs}
)
