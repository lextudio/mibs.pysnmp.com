# SNMP MIB module (CISCO-IETF-DHCP-SERVER-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-DHCP-SERVER-EXT-MIB
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

(cDhcpv4ServerClientPhysicalAddress,
 cDhcpv4ServerSubnetEntry,
 cDhcpv4ServerSubnetFreeAddrHighThreshold,
 cDhcpv4ServerSubnetFreeAddrLowThreshold,
 cDhcpv4ServerSubnetFreeAddresses) = mibBuilder.importSymbols(
    "CISCO-IETF-DHCP-SERVER-MIB",
    "cDhcpv4ServerClientPhysicalAddress",
    "cDhcpv4ServerSubnetEntry",
    "cDhcpv4ServerSubnetFreeAddrHighThreshold",
    "cDhcpv4ServerSubnetFreeAddrLowThreshold",
    "cDhcpv4ServerSubnetFreeAddresses")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(InetAddressIPv4,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfDhcpSrvExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122)
)
ciscoIetfDhcpSrvExtMIB.setRevisions(
        ("2007-03-15 12:00",
         "2005-05-04 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIetfDhcpv4SrvExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIetfDhcpv4SrvExtMIBNotifs = _CiscoIetfDhcpv4SrvExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 0)
)
_CDhcpv4SrvExtNotifyPrefix_ObjectIdentity = ObjectIdentity
cDhcpv4SrvExtNotifyPrefix = _CDhcpv4SrvExtNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 0, 2)
)
_CDhcpv4SrvExtNotify_ObjectIdentity = ObjectIdentity
cDhcpv4SrvExtNotify = _CDhcpv4SrvExtNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 0, 2, 0)
)
_CiscoIetfDhcpv4SrvExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfDhcpv4SrvExtMIBObjects = _CiscoIetfDhcpv4SrvExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1)
)
_CDhcpv4SrvExtSystem_ObjectIdentity = ObjectIdentity
cDhcpv4SrvExtSystem = _CDhcpv4SrvExtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 1)
)
_CDhcpv4SrvStartTime_Type = TimeStamp
_CDhcpv4SrvStartTime_Object = MibScalar
cDhcpv4SrvStartTime = _CDhcpv4SrvStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 1, 1),
    _CDhcpv4SrvStartTime_Type()
)
cDhcpv4SrvStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4SrvStartTime.setStatus("current")
_CDhcpv4SrvResetTime_Type = TimeStamp
_CDhcpv4SrvResetTime_Object = MibScalar
cDhcpv4SrvResetTime = _CDhcpv4SrvResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 1, 2),
    _CDhcpv4SrvResetTime_Type()
)
cDhcpv4SrvResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4SrvResetTime.setStatus("current")
_CDhcpv4ExtCounters_ObjectIdentity = ObjectIdentity
cDhcpv4ExtCounters = _CDhcpv4ExtCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 2)
)
_CDhcpv4LeaseQueries_Type = Counter32
_CDhcpv4LeaseQueries_Object = MibScalar
cDhcpv4LeaseQueries = _CDhcpv4LeaseQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 2, 1),
    _CDhcpv4LeaseQueries_Type()
)
cDhcpv4LeaseQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4LeaseQueries.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4LeaseQueries.setUnits("packets")
_CDhcpv4StatisticsResetTime_Type = TimeStamp
_CDhcpv4StatisticsResetTime_Object = MibScalar
cDhcpv4StatisticsResetTime = _CDhcpv4StatisticsResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 2, 2),
    _CDhcpv4StatisticsResetTime_Type()
)
cDhcpv4StatisticsResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4StatisticsResetTime.setStatus("current")
_CDhcpv4IntervalCounters_ObjectIdentity = ObjectIdentity
cDhcpv4IntervalCounters = _CDhcpv4IntervalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3)
)
_CDhcpv4IntDiscovers_Type = Unsigned32
_CDhcpv4IntDiscovers_Object = MibScalar
cDhcpv4IntDiscovers = _CDhcpv4IntDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 1),
    _CDhcpv4IntDiscovers_Type()
)
cDhcpv4IntDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntDiscovers.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntDiscovers.setUnits("packets")
_CDhcpv4IntOffers_Type = Unsigned32
_CDhcpv4IntOffers_Object = MibScalar
cDhcpv4IntOffers = _CDhcpv4IntOffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 2),
    _CDhcpv4IntOffers_Type()
)
cDhcpv4IntOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntOffers.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntOffers.setUnits("packets")
_CDhcpv4IntRequests_Type = Unsigned32
_CDhcpv4IntRequests_Object = MibScalar
cDhcpv4IntRequests = _CDhcpv4IntRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 3),
    _CDhcpv4IntRequests_Type()
)
cDhcpv4IntRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntRequests.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntRequests.setUnits("packets")
_CDhcpv4IntDeclines_Type = Unsigned32
_CDhcpv4IntDeclines_Object = MibScalar
cDhcpv4IntDeclines = _CDhcpv4IntDeclines_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 4),
    _CDhcpv4IntDeclines_Type()
)
cDhcpv4IntDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntDeclines.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntDeclines.setUnits("packets")
_CDhcpv4IntAcks_Type = Unsigned32
_CDhcpv4IntAcks_Object = MibScalar
cDhcpv4IntAcks = _CDhcpv4IntAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 5),
    _CDhcpv4IntAcks_Type()
)
cDhcpv4IntAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntAcks.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntAcks.setUnits("packets")
_CDhcpv4IntNaks_Type = Unsigned32
_CDhcpv4IntNaks_Object = MibScalar
cDhcpv4IntNaks = _CDhcpv4IntNaks_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 6),
    _CDhcpv4IntNaks_Type()
)
cDhcpv4IntNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntNaks.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntNaks.setUnits("packets")
_CDhcpv4IntReleases_Type = Unsigned32
_CDhcpv4IntReleases_Object = MibScalar
cDhcpv4IntReleases = _CDhcpv4IntReleases_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 7),
    _CDhcpv4IntReleases_Type()
)
cDhcpv4IntReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntReleases.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntReleases.setUnits("packets")
_CDhcpv4IntInforms_Type = Unsigned32
_CDhcpv4IntInforms_Object = MibScalar
cDhcpv4IntInforms = _CDhcpv4IntInforms_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 8),
    _CDhcpv4IntInforms_Type()
)
cDhcpv4IntInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntInforms.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntInforms.setUnits("packets")
_CDhcpv4IntLeaseQueries_Type = Unsigned32
_CDhcpv4IntLeaseQueries_Object = MibScalar
cDhcpv4IntLeaseQueries = _CDhcpv4IntLeaseQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 9),
    _CDhcpv4IntLeaseQueries_Type()
)
cDhcpv4IntLeaseQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntLeaseQueries.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntLeaseQueries.setUnits("packets")
_CDhcpv4IntReqBuffersInUse_Type = Gauge32
_CDhcpv4IntReqBuffersInUse_Object = MibScalar
cDhcpv4IntReqBuffersInUse = _CDhcpv4IntReqBuffersInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 10),
    _CDhcpv4IntReqBuffersInUse_Type()
)
cDhcpv4IntReqBuffersInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntReqBuffersInUse.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntReqBuffersInUse.setUnits("buffers")
_CDhcpv4IntRespBuffersInUse_Type = Gauge32
_CDhcpv4IntRespBuffersInUse_Object = MibScalar
cDhcpv4IntRespBuffersInUse = _CDhcpv4IntRespBuffersInUse_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 11),
    _CDhcpv4IntRespBuffersInUse_Type()
)
cDhcpv4IntRespBuffersInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntRespBuffersInUse.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntRespBuffersInUse.setUnits("buffers")
_CDhcpv4IntEndTime_Type = TimeStamp
_CDhcpv4IntEndTime_Object = MibScalar
cDhcpv4IntEndTime = _CDhcpv4IntEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 12),
    _CDhcpv4IntEndTime_Type()
)
cDhcpv4IntEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntEndTime.setStatus("current")
_CDhcpv4IntDeltaTime_Type = TimeInterval
_CDhcpv4IntDeltaTime_Object = MibScalar
cDhcpv4IntDeltaTime = _CDhcpv4IntDeltaTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 3, 13),
    _CDhcpv4IntDeltaTime_Type()
)
cDhcpv4IntDeltaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4IntDeltaTime.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4IntDeltaTime.setUnits("milliseconds")
_CDhcpv4FailoverCounters_ObjectIdentity = ObjectIdentity
cDhcpv4FailoverCounters = _CDhcpv4FailoverCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4)
)
_CDhcpv4FOPacketsRcvd_Type = Counter32
_CDhcpv4FOPacketsRcvd_Object = MibScalar
cDhcpv4FOPacketsRcvd = _CDhcpv4FOPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 1),
    _CDhcpv4FOPacketsRcvd_Type()
)
cDhcpv4FOPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOPacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOPacketsRcvd.setUnits("packets")
_CDhcpv4FOBindingUpdsRcvd_Type = Counter32
_CDhcpv4FOBindingUpdsRcvd_Object = MibScalar
cDhcpv4FOBindingUpdsRcvd = _CDhcpv4FOBindingUpdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 2),
    _CDhcpv4FOBindingUpdsRcvd_Type()
)
cDhcpv4FOBindingUpdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingUpdsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingUpdsRcvd.setUnits("packets")
_CDhcpv4FOBindingAcksRcvd_Type = Counter32
_CDhcpv4FOBindingAcksRcvd_Object = MibScalar
cDhcpv4FOBindingAcksRcvd = _CDhcpv4FOBindingAcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 3),
    _CDhcpv4FOBindingAcksRcvd_Type()
)
cDhcpv4FOBindingAcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingAcksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingAcksRcvd.setUnits("packets")
_CDhcpv4FOBindingNaksRcvd_Type = Counter32
_CDhcpv4FOBindingNaksRcvd_Object = MibScalar
cDhcpv4FOBindingNaksRcvd = _CDhcpv4FOBindingNaksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 4),
    _CDhcpv4FOBindingNaksRcvd_Type()
)
cDhcpv4FOBindingNaksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingNaksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingNaksRcvd.setUnits("packets")
_CDhcpv4FOPoolRequestsRcvd_Type = Counter32
_CDhcpv4FOPoolRequestsRcvd_Object = MibScalar
cDhcpv4FOPoolRequestsRcvd = _CDhcpv4FOPoolRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 5),
    _CDhcpv4FOPoolRequestsRcvd_Type()
)
cDhcpv4FOPoolRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOPoolRequestsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOPoolRequestsRcvd.setUnits("packets")
_CDhcpv4FOPollsRcvd_Type = Counter32
_CDhcpv4FOPollsRcvd_Object = MibScalar
cDhcpv4FOPollsRcvd = _CDhcpv4FOPollsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 6),
    _CDhcpv4FOPollsRcvd_Type()
)
cDhcpv4FOPollsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOPollsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOPollsRcvd.setUnits("packets")
_CDhcpv4FOUpdateRequestsRcvd_Type = Counter32
_CDhcpv4FOUpdateRequestsRcvd_Object = MibScalar
cDhcpv4FOUpdateRequestsRcvd = _CDhcpv4FOUpdateRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 7),
    _CDhcpv4FOUpdateRequestsRcvd_Type()
)
cDhcpv4FOUpdateRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateRequestsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateRequestsRcvd.setUnits("packets")
_CDhcpv4FOUpdateDoneRcvd_Type = Counter32
_CDhcpv4FOUpdateDoneRcvd_Object = MibScalar
cDhcpv4FOUpdateDoneRcvd = _CDhcpv4FOUpdateDoneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 8),
    _CDhcpv4FOUpdateDoneRcvd_Type()
)
cDhcpv4FOUpdateDoneRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateDoneRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateDoneRcvd.setUnits("packets")
_CDhcpv4FOPacketsSent_Type = Counter32
_CDhcpv4FOPacketsSent_Object = MibScalar
cDhcpv4FOPacketsSent = _CDhcpv4FOPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 9),
    _CDhcpv4FOPacketsSent_Type()
)
cDhcpv4FOPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOPacketsSent.setUnits("packets")
_CDhcpv4FOBindingUpdatesSent_Type = Counter32
_CDhcpv4FOBindingUpdatesSent_Object = MibScalar
cDhcpv4FOBindingUpdatesSent = _CDhcpv4FOBindingUpdatesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 10),
    _CDhcpv4FOBindingUpdatesSent_Type()
)
cDhcpv4FOBindingUpdatesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingUpdatesSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingUpdatesSent.setUnits("packets")
_CDhcpv4FOBindingAcksSent_Type = Counter32
_CDhcpv4FOBindingAcksSent_Object = MibScalar
cDhcpv4FOBindingAcksSent = _CDhcpv4FOBindingAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 11),
    _CDhcpv4FOBindingAcksSent_Type()
)
cDhcpv4FOBindingAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingAcksSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingAcksSent.setUnits("packets")
_CDhcpv4FOBindingNaksSent_Type = Counter32
_CDhcpv4FOBindingNaksSent_Object = MibScalar
cDhcpv4FOBindingNaksSent = _CDhcpv4FOBindingNaksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 12),
    _CDhcpv4FOBindingNaksSent_Type()
)
cDhcpv4FOBindingNaksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingNaksSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOBindingNaksSent.setUnits("packets")
_CDhcpv4FOPoolResponsesSent_Type = Counter32
_CDhcpv4FOPoolResponsesSent_Object = MibScalar
cDhcpv4FOPoolResponsesSent = _CDhcpv4FOPoolResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 13),
    _CDhcpv4FOPoolResponsesSent_Type()
)
cDhcpv4FOPoolResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOPoolResponsesSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOPoolResponsesSent.setUnits("packets")
_CDhcpv4FOPollsSent_Type = Counter32
_CDhcpv4FOPollsSent_Object = MibScalar
cDhcpv4FOPollsSent = _CDhcpv4FOPollsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 14),
    _CDhcpv4FOPollsSent_Type()
)
cDhcpv4FOPollsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOPollsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOPollsSent.setUnits("packets")
_CDhcpv4FOUpdateRequestsSent_Type = Counter32
_CDhcpv4FOUpdateRequestsSent_Object = MibScalar
cDhcpv4FOUpdateRequestsSent = _CDhcpv4FOUpdateRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 15),
    _CDhcpv4FOUpdateRequestsSent_Type()
)
cDhcpv4FOUpdateRequestsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateRequestsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateRequestsSent.setUnits("packets")
_CDhcpv4FOUpdateDoneSent_Type = Counter32
_CDhcpv4FOUpdateDoneSent_Object = MibScalar
cDhcpv4FOUpdateDoneSent = _CDhcpv4FOUpdateDoneSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 16),
    _CDhcpv4FOUpdateDoneSent_Type()
)
cDhcpv4FOUpdateDoneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateDoneSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOUpdateDoneSent.setUnits("packets")
_CDhcpv4FOPacketsDropped_Type = Counter32
_CDhcpv4FOPacketsDropped_Object = MibScalar
cDhcpv4FOPacketsDropped = _CDhcpv4FOPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 4, 17),
    _CDhcpv4FOPacketsDropped_Type()
)
cDhcpv4FOPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOPacketsDropped.setUnits("packets")
_CDhcpv4FailoverIntervalCounters_ObjectIdentity = ObjectIdentity
cDhcpv4FailoverIntervalCounters = _CDhcpv4FailoverIntervalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5)
)
_CDhcpv4FOIntPacketsRcvd_Type = Unsigned32
_CDhcpv4FOIntPacketsRcvd_Object = MibScalar
cDhcpv4FOIntPacketsRcvd = _CDhcpv4FOIntPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 1),
    _CDhcpv4FOIntPacketsRcvd_Type()
)
cDhcpv4FOIntPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPacketsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPacketsRcvd.setUnits("packets")
_CDhcpv4FOIntBindingUpdsRcvd_Type = Unsigned32
_CDhcpv4FOIntBindingUpdsRcvd_Object = MibScalar
cDhcpv4FOIntBindingUpdsRcvd = _CDhcpv4FOIntBindingUpdsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 2),
    _CDhcpv4FOIntBindingUpdsRcvd_Type()
)
cDhcpv4FOIntBindingUpdsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingUpdsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingUpdsRcvd.setUnits("packets")
_CDhcpv4FOIntBindingAcksRcvd_Type = Unsigned32
_CDhcpv4FOIntBindingAcksRcvd_Object = MibScalar
cDhcpv4FOIntBindingAcksRcvd = _CDhcpv4FOIntBindingAcksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 3),
    _CDhcpv4FOIntBindingAcksRcvd_Type()
)
cDhcpv4FOIntBindingAcksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingAcksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingAcksRcvd.setUnits("packets")
_CDhcpv4FOIntBindingNaksRcvd_Type = Unsigned32
_CDhcpv4FOIntBindingNaksRcvd_Object = MibScalar
cDhcpv4FOIntBindingNaksRcvd = _CDhcpv4FOIntBindingNaksRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 4),
    _CDhcpv4FOIntBindingNaksRcvd_Type()
)
cDhcpv4FOIntBindingNaksRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingNaksRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingNaksRcvd.setUnits("packets")
_CDhcpv4FOIntPoolRequestsRcvd_Type = Unsigned32
_CDhcpv4FOIntPoolRequestsRcvd_Object = MibScalar
cDhcpv4FOIntPoolRequestsRcvd = _CDhcpv4FOIntPoolRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 5),
    _CDhcpv4FOIntPoolRequestsRcvd_Type()
)
cDhcpv4FOIntPoolRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPoolRequestsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPoolRequestsRcvd.setUnits("packets")
_CDhcpv4FOIntPollsRcvd_Type = Unsigned32
_CDhcpv4FOIntPollsRcvd_Object = MibScalar
cDhcpv4FOIntPollsRcvd = _CDhcpv4FOIntPollsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 6),
    _CDhcpv4FOIntPollsRcvd_Type()
)
cDhcpv4FOIntPollsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPollsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPollsRcvd.setUnits("packets")
_CDhcpv4FOIntUpdateReqsRcvd_Type = Unsigned32
_CDhcpv4FOIntUpdateReqsRcvd_Object = MibScalar
cDhcpv4FOIntUpdateReqsRcvd = _CDhcpv4FOIntUpdateReqsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 7),
    _CDhcpv4FOIntUpdateReqsRcvd_Type()
)
cDhcpv4FOIntUpdateReqsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateReqsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateReqsRcvd.setUnits("packets")
_CDhcpv4FOIntUpdateDoneRcvd_Type = Unsigned32
_CDhcpv4FOIntUpdateDoneRcvd_Object = MibScalar
cDhcpv4FOIntUpdateDoneRcvd = _CDhcpv4FOIntUpdateDoneRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 8),
    _CDhcpv4FOIntUpdateDoneRcvd_Type()
)
cDhcpv4FOIntUpdateDoneRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateDoneRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateDoneRcvd.setUnits("packets")
_CDhcpv4FOIntPacketsSent_Type = Unsigned32
_CDhcpv4FOIntPacketsSent_Object = MibScalar
cDhcpv4FOIntPacketsSent = _CDhcpv4FOIntPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 9),
    _CDhcpv4FOIntPacketsSent_Type()
)
cDhcpv4FOIntPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPacketsSent.setUnits("packets")
_CDhcpv4FOIntBindingUpdsSent_Type = Unsigned32
_CDhcpv4FOIntBindingUpdsSent_Object = MibScalar
cDhcpv4FOIntBindingUpdsSent = _CDhcpv4FOIntBindingUpdsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 10),
    _CDhcpv4FOIntBindingUpdsSent_Type()
)
cDhcpv4FOIntBindingUpdsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingUpdsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingUpdsSent.setUnits("packets")
_CDhcpv4FOIntBindingAcksSent_Type = Unsigned32
_CDhcpv4FOIntBindingAcksSent_Object = MibScalar
cDhcpv4FOIntBindingAcksSent = _CDhcpv4FOIntBindingAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 11),
    _CDhcpv4FOIntBindingAcksSent_Type()
)
cDhcpv4FOIntBindingAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingAcksSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingAcksSent.setUnits("packets")
_CDhcpv4FOIntBindingNaksSent_Type = Unsigned32
_CDhcpv4FOIntBindingNaksSent_Object = MibScalar
cDhcpv4FOIntBindingNaksSent = _CDhcpv4FOIntBindingNaksSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 12),
    _CDhcpv4FOIntBindingNaksSent_Type()
)
cDhcpv4FOIntBindingNaksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingNaksSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntBindingNaksSent.setUnits("packets")
_CDhcpv4FOIntPoolResponsesSent_Type = Unsigned32
_CDhcpv4FOIntPoolResponsesSent_Object = MibScalar
cDhcpv4FOIntPoolResponsesSent = _CDhcpv4FOIntPoolResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 13),
    _CDhcpv4FOIntPoolResponsesSent_Type()
)
cDhcpv4FOIntPoolResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPoolResponsesSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPoolResponsesSent.setUnits("packets")
_CDhcpv4FOIntPollsSent_Type = Unsigned32
_CDhcpv4FOIntPollsSent_Object = MibScalar
cDhcpv4FOIntPollsSent = _CDhcpv4FOIntPollsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 14),
    _CDhcpv4FOIntPollsSent_Type()
)
cDhcpv4FOIntPollsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPollsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPollsSent.setUnits("packets")
_CDhcpv4FOIntUpdateReqsSent_Type = Unsigned32
_CDhcpv4FOIntUpdateReqsSent_Object = MibScalar
cDhcpv4FOIntUpdateReqsSent = _CDhcpv4FOIntUpdateReqsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 15),
    _CDhcpv4FOIntUpdateReqsSent_Type()
)
cDhcpv4FOIntUpdateReqsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateReqsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateReqsSent.setUnits("packets")
_CDhcpv4FOIntUpdateDoneSent_Type = Unsigned32
_CDhcpv4FOIntUpdateDoneSent_Object = MibScalar
cDhcpv4FOIntUpdateDoneSent = _CDhcpv4FOIntUpdateDoneSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 16),
    _CDhcpv4FOIntUpdateDoneSent_Type()
)
cDhcpv4FOIntUpdateDoneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateDoneSent.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntUpdateDoneSent.setUnits("packets")
_CDhcpv4FOIntPacketsDropped_Type = Unsigned32
_CDhcpv4FOIntPacketsDropped_Object = MibScalar
cDhcpv4FOIntPacketsDropped = _CDhcpv4FOIntPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 17),
    _CDhcpv4FOIntPacketsDropped_Type()
)
cDhcpv4FOIntPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntPacketsDropped.setUnits("packets")
_CDhcpv4FOIntEndTime_Type = TimeStamp
_CDhcpv4FOIntEndTime_Object = MibScalar
cDhcpv4FOIntEndTime = _CDhcpv4FOIntEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 18),
    _CDhcpv4FOIntEndTime_Type()
)
cDhcpv4FOIntEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntEndTime.setStatus("current")
_CDhcpv4FOIntDeltaTime_Type = TimeInterval
_CDhcpv4FOIntDeltaTime_Object = MibScalar
cDhcpv4FOIntDeltaTime = _CDhcpv4FOIntDeltaTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 5, 19),
    _CDhcpv4FOIntDeltaTime_Type()
)
cDhcpv4FOIntDeltaTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4FOIntDeltaTime.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4FOIntDeltaTime.setUnits("milliseconds")
_CDhcpv4CfgObjects_ObjectIdentity = ObjectIdentity
cDhcpv4CfgObjects = _CDhcpv4CfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6)
)
_CDhcpv4ConfigIntervalSample_Type = TimeInterval
_CDhcpv4ConfigIntervalSample_Object = MibScalar
cDhcpv4ConfigIntervalSample = _CDhcpv4ConfigIntervalSample_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 1),
    _CDhcpv4ConfigIntervalSample_Type()
)
cDhcpv4ConfigIntervalSample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ConfigIntervalSample.setStatus("current")
if mibBuilder.loadTexts:
    cDhcpv4ConfigIntervalSample.setUnits("milliseconds")
_CDhcpv4SrvExtSubnetTable_Object = MibTable
cDhcpv4SrvExtSubnetTable = _CDhcpv4SrvExtSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvExtSubnetTable.setStatus("current")
_CDhcpv4SrvExtSubnetEntry_Object = MibTableRow
cDhcpv4SrvExtSubnetEntry = _CDhcpv4SrvExtSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvExtSubnetEntry.setStatus("current")
_CDhcpv4ServerDefaultRouterAddress_Type = InetAddressIPv4
_CDhcpv4ServerDefaultRouterAddress_Object = MibTableColumn
cDhcpv4ServerDefaultRouterAddress = _CDhcpv4ServerDefaultRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 2, 1, 1),
    _CDhcpv4ServerDefaultRouterAddress_Type()
)
cDhcpv4ServerDefaultRouterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerDefaultRouterAddress.setStatus("current")
_CDhcpv4ServerSubnetStartAddress_Type = InetAddressIPv4
_CDhcpv4ServerSubnetStartAddress_Object = MibTableColumn
cDhcpv4ServerSubnetStartAddress = _CDhcpv4ServerSubnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 2, 1, 2),
    _CDhcpv4ServerSubnetStartAddress_Type()
)
cDhcpv4ServerSubnetStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetStartAddress.setStatus("current")
_CDhcpv4ServerSubnetEndAddress_Type = InetAddressIPv4
_CDhcpv4ServerSubnetEndAddress_Object = MibTableColumn
cDhcpv4ServerSubnetEndAddress = _CDhcpv4ServerSubnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 2, 1, 3),
    _CDhcpv4ServerSubnetEndAddress_Type()
)
cDhcpv4ServerSubnetEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetEndAddress.setStatus("current")


class _CDhcpv4ServerIfLeaseLimitEnable_Type(TruthValue):
    """Custom type cDhcpv4ServerIfLeaseLimitEnable based on TruthValue"""


_CDhcpv4ServerIfLeaseLimitEnable_Object = MibScalar
cDhcpv4ServerIfLeaseLimitEnable = _CDhcpv4ServerIfLeaseLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 3),
    _CDhcpv4ServerIfLeaseLimitEnable_Type()
)
cDhcpv4ServerIfLeaseLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerIfLeaseLimitEnable.setStatus("current")


class _CDhcpv4ServerSubnetFreeAddressLowEnable_Type(TruthValue):
    """Custom type cDhcpv4ServerSubnetFreeAddressLowEnable based on TruthValue"""


_CDhcpv4ServerSubnetFreeAddressLowEnable_Object = MibScalar
cDhcpv4ServerSubnetFreeAddressLowEnable = _CDhcpv4ServerSubnetFreeAddressLowEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 4),
    _CDhcpv4ServerSubnetFreeAddressLowEnable_Type()
)
cDhcpv4ServerSubnetFreeAddressLowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetFreeAddressLowEnable.setStatus("current")


class _CDhcpv4ServerSubnetFreeAddressHighEnable_Type(TruthValue):
    """Custom type cDhcpv4ServerSubnetFreeAddressHighEnable based on TruthValue"""


_CDhcpv4ServerSubnetFreeAddressHighEnable_Object = MibScalar
cDhcpv4ServerSubnetFreeAddressHighEnable = _CDhcpv4ServerSubnetFreeAddressHighEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 5),
    _CDhcpv4ServerSubnetFreeAddressHighEnable_Type()
)
cDhcpv4ServerSubnetFreeAddressHighEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetFreeAddressHighEnable.setStatus("current")


class _CDhcpv4ServerIfLeaseLimitDefault_Type(Unsigned32):
    """Custom type cDhcpv4ServerIfLeaseLimitDefault based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CDhcpv4ServerIfLeaseLimitDefault_Type.__name__ = "Unsigned32"
_CDhcpv4ServerIfLeaseLimitDefault_Object = MibScalar
cDhcpv4ServerIfLeaseLimitDefault = _CDhcpv4ServerIfLeaseLimitDefault_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 6),
    _CDhcpv4ServerIfLeaseLimitDefault_Type()
)
cDhcpv4ServerIfLeaseLimitDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerIfLeaseLimitDefault.setStatus("current")
_CDhcpv4SrvIfCfgTable_Object = MibTable
cDhcpv4SrvIfCfgTable = _CDhcpv4SrvIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 7)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvIfCfgTable.setStatus("current")
_CDhcpv4SrvIfCfgEntry_Object = MibTableRow
cDhcpv4SrvIfCfgEntry = _CDhcpv4SrvIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 7, 1)
)
cDhcpv4SrvIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cDhcpv4SrvIfCfgEntry.setStatus("current")


class _CDhcpv4ServerIfLeaseLimit_Type(Unsigned32):
    """Custom type cDhcpv4ServerIfLeaseLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CDhcpv4ServerIfLeaseLimit_Type.__name__ = "Unsigned32"
_CDhcpv4ServerIfLeaseLimit_Object = MibTableColumn
cDhcpv4ServerIfLeaseLimit = _CDhcpv4ServerIfLeaseLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 1, 6, 7, 1, 1),
    _CDhcpv4ServerIfLeaseLimit_Type()
)
cDhcpv4ServerIfLeaseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDhcpv4ServerIfLeaseLimit.setStatus("current")
_CiscoIetfDhcpv4SrvExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoIetfDhcpv4SrvExtMIBConform = _CiscoIetfDhcpv4SrvExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2)
)
_CDhcpv4SrvExtCompliances_ObjectIdentity = ObjectIdentity
cDhcpv4SrvExtCompliances = _CDhcpv4SrvExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 1)
)
_CDhcpv4SrvExtGroups_ObjectIdentity = ObjectIdentity
cDhcpv4SrvExtGroups = _CDhcpv4SrvExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2)
)
cDhcpv4ServerSubnetEntry.registerAugmentions(
    ("CISCO-IETF-DHCP-SERVER-EXT-MIB",
     "cDhcpv4SrvExtSubnetEntry")
)
cDhcpv4SrvExtSubnetEntry.setIndexNames(*cDhcpv4ServerSubnetEntry.getIndexNames())

# Managed Objects groups

cDhcpv4SrvExtSystemObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2, 1)
)
cDhcpv4SrvExtSystemObjects.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4SrvStartTime"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4SrvResetTime"))
)
if mibBuilder.loadTexts:
    cDhcpv4SrvExtSystemObjects.setStatus("current")

cDhcpv4ExtCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2, 2)
)
cDhcpv4ExtCountersGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4LeaseQueries"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4StatisticsResetTime"))
)
if mibBuilder.loadTexts:
    cDhcpv4ExtCountersGroup.setStatus("current")

cDhcpv4CountersIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2, 3)
)
cDhcpv4CountersIntervalGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntDiscovers"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntOffers"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntRequests"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntDeclines"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntAcks"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntNaks"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntInforms"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntLeaseQueries"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntReleases"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntRespBuffersInUse"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntReqBuffersInUse"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntEndTime"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4IntDeltaTime"))
)
if mibBuilder.loadTexts:
    cDhcpv4CountersIntervalGroup.setStatus("current")

cDhcpv4FOCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2, 4)
)
cDhcpv4FOCountersGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOPacketsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOBindingUpdsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOBindingAcksRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOBindingNaksRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOPoolRequestsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOPollsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOUpdateRequestsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOUpdateDoneRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOPacketsSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOBindingUpdatesSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOBindingAcksSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOBindingNaksSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOPoolResponsesSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOPollsSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOUpdateRequestsSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOUpdateDoneSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOPacketsDropped"))
)
if mibBuilder.loadTexts:
    cDhcpv4FOCountersGroup.setStatus("current")

cDhcpv4FOCountersIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2, 5)
)
cDhcpv4FOCountersIntervalGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntPacketsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntBindingUpdsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntBindingAcksRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntBindingNaksRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntPoolRequestsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntPollsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntUpdateReqsRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntUpdateDoneRcvd"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntPacketsSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntBindingUpdsSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntBindingAcksSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntBindingNaksSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntPoolResponsesSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntPollsSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntUpdateReqsSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntUpdateDoneSent"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntPacketsDropped"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntEndTime"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4FOIntDeltaTime"))
)
if mibBuilder.loadTexts:
    cDhcpv4FOCountersIntervalGroup.setStatus("current")

cDhcpv4CfgObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2, 6)
)
cDhcpv4CfgObjectsGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ConfigIntervalSample"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerDefaultRouterAddress"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerSubnetStartAddress"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerSubnetEndAddress"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerIfLeaseLimitEnable"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerSubnetFreeAddressLowEnable"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerSubnetFreeAddressHighEnable"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerIfLeaseLimitDefault"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerIfLeaseLimit"))
)
if mibBuilder.loadTexts:
    cDhcpv4CfgObjectsGroup.setStatus("current")


# Notification objects

cDhcpv4ServerIfLeaseLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 0, 2, 0, 1)
)
cDhcpv4ServerIfLeaseLimitExceeded.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerClientPhysicalAddress"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerIfLeaseLimit"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerIfLeaseLimitExceeded.setStatus(
        "current"
    )

cDhcpv4ServerSubnetFreeAddressLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 0, 2, 0, 2)
)
cDhcpv4ServerSubnetFreeAddressLow.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddresses"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddrLowThreshold"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetFreeAddressLow.setStatus(
        "current"
    )

cDhcpv4ServerSubnetFreeAddressHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 0, 2, 0, 3)
)
cDhcpv4ServerSubnetFreeAddressHigh.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddresses"),
        ("CISCO-IETF-DHCP-SERVER-MIB", "cDhcpv4ServerSubnetFreeAddrHighThreshold"))
)
if mibBuilder.loadTexts:
    cDhcpv4ServerSubnetFreeAddressHigh.setStatus(
        "current"
    )


# Notifications groups

cDhcpv4SrvExtNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 2, 7)
)
cDhcpv4SrvExtNotifyGroup.setObjects(
      *(("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerIfLeaseLimitExceeded"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerSubnetFreeAddressLow"),
        ("CISCO-IETF-DHCP-SERVER-EXT-MIB", "cDhcpv4ServerSubnetFreeAddressHigh"))
)
if mibBuilder.loadTexts:
    cDhcpv4SrvExtNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cDhcpv4SrvExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvExtCompliance.setStatus(
        "deprecated"
    )

cDhcpv4SrvExtComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 122, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cDhcpv4SrvExtComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-DHCP-SERVER-EXT-MIB",
    **{"ciscoIetfDhcpSrvExtMIB": ciscoIetfDhcpSrvExtMIB,
       "ciscoIetfDhcpv4SrvExtMIBNotifs": ciscoIetfDhcpv4SrvExtMIBNotifs,
       "cDhcpv4SrvExtNotifyPrefix": cDhcpv4SrvExtNotifyPrefix,
       "cDhcpv4SrvExtNotify": cDhcpv4SrvExtNotify,
       "cDhcpv4ServerIfLeaseLimitExceeded": cDhcpv4ServerIfLeaseLimitExceeded,
       "cDhcpv4ServerSubnetFreeAddressLow": cDhcpv4ServerSubnetFreeAddressLow,
       "cDhcpv4ServerSubnetFreeAddressHigh": cDhcpv4ServerSubnetFreeAddressHigh,
       "ciscoIetfDhcpv4SrvExtMIBObjects": ciscoIetfDhcpv4SrvExtMIBObjects,
       "cDhcpv4SrvExtSystem": cDhcpv4SrvExtSystem,
       "cDhcpv4SrvStartTime": cDhcpv4SrvStartTime,
       "cDhcpv4SrvResetTime": cDhcpv4SrvResetTime,
       "cDhcpv4ExtCounters": cDhcpv4ExtCounters,
       "cDhcpv4LeaseQueries": cDhcpv4LeaseQueries,
       "cDhcpv4StatisticsResetTime": cDhcpv4StatisticsResetTime,
       "cDhcpv4IntervalCounters": cDhcpv4IntervalCounters,
       "cDhcpv4IntDiscovers": cDhcpv4IntDiscovers,
       "cDhcpv4IntOffers": cDhcpv4IntOffers,
       "cDhcpv4IntRequests": cDhcpv4IntRequests,
       "cDhcpv4IntDeclines": cDhcpv4IntDeclines,
       "cDhcpv4IntAcks": cDhcpv4IntAcks,
       "cDhcpv4IntNaks": cDhcpv4IntNaks,
       "cDhcpv4IntReleases": cDhcpv4IntReleases,
       "cDhcpv4IntInforms": cDhcpv4IntInforms,
       "cDhcpv4IntLeaseQueries": cDhcpv4IntLeaseQueries,
       "cDhcpv4IntReqBuffersInUse": cDhcpv4IntReqBuffersInUse,
       "cDhcpv4IntRespBuffersInUse": cDhcpv4IntRespBuffersInUse,
       "cDhcpv4IntEndTime": cDhcpv4IntEndTime,
       "cDhcpv4IntDeltaTime": cDhcpv4IntDeltaTime,
       "cDhcpv4FailoverCounters": cDhcpv4FailoverCounters,
       "cDhcpv4FOPacketsRcvd": cDhcpv4FOPacketsRcvd,
       "cDhcpv4FOBindingUpdsRcvd": cDhcpv4FOBindingUpdsRcvd,
       "cDhcpv4FOBindingAcksRcvd": cDhcpv4FOBindingAcksRcvd,
       "cDhcpv4FOBindingNaksRcvd": cDhcpv4FOBindingNaksRcvd,
       "cDhcpv4FOPoolRequestsRcvd": cDhcpv4FOPoolRequestsRcvd,
       "cDhcpv4FOPollsRcvd": cDhcpv4FOPollsRcvd,
       "cDhcpv4FOUpdateRequestsRcvd": cDhcpv4FOUpdateRequestsRcvd,
       "cDhcpv4FOUpdateDoneRcvd": cDhcpv4FOUpdateDoneRcvd,
       "cDhcpv4FOPacketsSent": cDhcpv4FOPacketsSent,
       "cDhcpv4FOBindingUpdatesSent": cDhcpv4FOBindingUpdatesSent,
       "cDhcpv4FOBindingAcksSent": cDhcpv4FOBindingAcksSent,
       "cDhcpv4FOBindingNaksSent": cDhcpv4FOBindingNaksSent,
       "cDhcpv4FOPoolResponsesSent": cDhcpv4FOPoolResponsesSent,
       "cDhcpv4FOPollsSent": cDhcpv4FOPollsSent,
       "cDhcpv4FOUpdateRequestsSent": cDhcpv4FOUpdateRequestsSent,
       "cDhcpv4FOUpdateDoneSent": cDhcpv4FOUpdateDoneSent,
       "cDhcpv4FOPacketsDropped": cDhcpv4FOPacketsDropped,
       "cDhcpv4FailoverIntervalCounters": cDhcpv4FailoverIntervalCounters,
       "cDhcpv4FOIntPacketsRcvd": cDhcpv4FOIntPacketsRcvd,
       "cDhcpv4FOIntBindingUpdsRcvd": cDhcpv4FOIntBindingUpdsRcvd,
       "cDhcpv4FOIntBindingAcksRcvd": cDhcpv4FOIntBindingAcksRcvd,
       "cDhcpv4FOIntBindingNaksRcvd": cDhcpv4FOIntBindingNaksRcvd,
       "cDhcpv4FOIntPoolRequestsRcvd": cDhcpv4FOIntPoolRequestsRcvd,
       "cDhcpv4FOIntPollsRcvd": cDhcpv4FOIntPollsRcvd,
       "cDhcpv4FOIntUpdateReqsRcvd": cDhcpv4FOIntUpdateReqsRcvd,
       "cDhcpv4FOIntUpdateDoneRcvd": cDhcpv4FOIntUpdateDoneRcvd,
       "cDhcpv4FOIntPacketsSent": cDhcpv4FOIntPacketsSent,
       "cDhcpv4FOIntBindingUpdsSent": cDhcpv4FOIntBindingUpdsSent,
       "cDhcpv4FOIntBindingAcksSent": cDhcpv4FOIntBindingAcksSent,
       "cDhcpv4FOIntBindingNaksSent": cDhcpv4FOIntBindingNaksSent,
       "cDhcpv4FOIntPoolResponsesSent": cDhcpv4FOIntPoolResponsesSent,
       "cDhcpv4FOIntPollsSent": cDhcpv4FOIntPollsSent,
       "cDhcpv4FOIntUpdateReqsSent": cDhcpv4FOIntUpdateReqsSent,
       "cDhcpv4FOIntUpdateDoneSent": cDhcpv4FOIntUpdateDoneSent,
       "cDhcpv4FOIntPacketsDropped": cDhcpv4FOIntPacketsDropped,
       "cDhcpv4FOIntEndTime": cDhcpv4FOIntEndTime,
       "cDhcpv4FOIntDeltaTime": cDhcpv4FOIntDeltaTime,
       "cDhcpv4CfgObjects": cDhcpv4CfgObjects,
       "cDhcpv4ConfigIntervalSample": cDhcpv4ConfigIntervalSample,
       "cDhcpv4SrvExtSubnetTable": cDhcpv4SrvExtSubnetTable,
       "cDhcpv4SrvExtSubnetEntry": cDhcpv4SrvExtSubnetEntry,
       "cDhcpv4ServerDefaultRouterAddress": cDhcpv4ServerDefaultRouterAddress,
       "cDhcpv4ServerSubnetStartAddress": cDhcpv4ServerSubnetStartAddress,
       "cDhcpv4ServerSubnetEndAddress": cDhcpv4ServerSubnetEndAddress,
       "cDhcpv4ServerIfLeaseLimitEnable": cDhcpv4ServerIfLeaseLimitEnable,
       "cDhcpv4ServerSubnetFreeAddressLowEnable": cDhcpv4ServerSubnetFreeAddressLowEnable,
       "cDhcpv4ServerSubnetFreeAddressHighEnable": cDhcpv4ServerSubnetFreeAddressHighEnable,
       "cDhcpv4ServerIfLeaseLimitDefault": cDhcpv4ServerIfLeaseLimitDefault,
       "cDhcpv4SrvIfCfgTable": cDhcpv4SrvIfCfgTable,
       "cDhcpv4SrvIfCfgEntry": cDhcpv4SrvIfCfgEntry,
       "cDhcpv4ServerIfLeaseLimit": cDhcpv4ServerIfLeaseLimit,
       "ciscoIetfDhcpv4SrvExtMIBConform": ciscoIetfDhcpv4SrvExtMIBConform,
       "cDhcpv4SrvExtCompliances": cDhcpv4SrvExtCompliances,
       "cDhcpv4SrvExtCompliance": cDhcpv4SrvExtCompliance,
       "cDhcpv4SrvExtComplianceRev1": cDhcpv4SrvExtComplianceRev1,
       "cDhcpv4SrvExtGroups": cDhcpv4SrvExtGroups,
       "cDhcpv4SrvExtSystemObjects": cDhcpv4SrvExtSystemObjects,
       "cDhcpv4ExtCountersGroup": cDhcpv4ExtCountersGroup,
       "cDhcpv4CountersIntervalGroup": cDhcpv4CountersIntervalGroup,
       "cDhcpv4FOCountersGroup": cDhcpv4FOCountersGroup,
       "cDhcpv4FOCountersIntervalGroup": cDhcpv4FOCountersIntervalGroup,
       "cDhcpv4CfgObjectsGroup": cDhcpv4CfgObjectsGroup,
       "cDhcpv4SrvExtNotifyGroup": cDhcpv4SrvExtNotifyGroup}
)
