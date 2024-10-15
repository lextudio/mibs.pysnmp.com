# SNMP MIB module (CISCO-EPC-GATEWAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-EPC-GATEWAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:49 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoEpcGatewayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731)
)
ciscoEpcGatewayMIB.setRevisions(
        ("2012-02-08 00:00",
         "2011-05-10 00:00",
         "2011-03-04 00:00",
         "2010-06-28 00:00",
         "2010-05-06 00:00",
         "2010-04-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEpcGatewayMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayMIBNotifications = _CiscoEpcGatewayMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 0)
)
_CiscoEpcGatewayMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayMIBObjects = _CiscoEpcGatewayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1)
)
_CiscoEpcGatewayStatistics_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayStatistics = _CiscoEpcGatewayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1)
)
_CegOverloadProtectionStats_ObjectIdentity = ObjectIdentity
cegOverloadProtectionStats = _CegOverloadProtectionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 1)
)
_CegCongestionIncomingReqDrops_Type = Counter32
_CegCongestionIncomingReqDrops_Object = MibScalar
cegCongestionIncomingReqDrops = _CegCongestionIncomingReqDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 1, 1),
    _CegCongestionIncomingReqDrops_Type()
)
cegCongestionIncomingReqDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionIncomingReqDrops.setStatus("current")
_CegCongestionLowThresholdReached_Type = Counter32
_CegCongestionLowThresholdReached_Object = MibScalar
cegCongestionLowThresholdReached = _CegCongestionLowThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 1, 2),
    _CegCongestionLowThresholdReached_Type()
)
cegCongestionLowThresholdReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionLowThresholdReached.setStatus("current")
_CegCongestionHighThresholdReached_Type = Counter32
_CegCongestionHighThresholdReached_Object = MibScalar
cegCongestionHighThresholdReached = _CegCongestionHighThresholdReached_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 1, 3),
    _CegCongestionHighThresholdReached_Type()
)
cegCongestionHighThresholdReached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionHighThresholdReached.setStatus("current")
_CegBufferStats_ObjectIdentity = ObjectIdentity
cegBufferStats = _CegBufferStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2)
)
_CegBuffersCreated_Type = Counter32
_CegBuffersCreated_Object = MibScalar
cegBuffersCreated = _CegBuffersCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 1),
    _CegBuffersCreated_Type()
)
cegBuffersCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBuffersCreated.setStatus("current")
if mibBuilder.loadTexts:
    cegBuffersCreated.setUnits("buffer")
_CegBuffersDeleted_Type = Counter32
_CegBuffersDeleted_Object = MibScalar
cegBuffersDeleted = _CegBuffersDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 2),
    _CegBuffersDeleted_Type()
)
cegBuffersDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBuffersDeleted.setStatus("current")
if mibBuilder.loadTexts:
    cegBuffersDeleted.setUnits("buffer")
_CegBuffersTimedOut_Type = Counter32
_CegBuffersTimedOut_Object = MibScalar
cegBuffersTimedOut = _CegBuffersTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 3),
    _CegBuffersTimedOut_Type()
)
cegBuffersTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBuffersTimedOut.setStatus("current")
_CegBufferPacketsEnqueued_Type = Counter32
_CegBufferPacketsEnqueued_Object = MibScalar
cegBufferPacketsEnqueued = _CegBufferPacketsEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 4),
    _CegBufferPacketsEnqueued_Type()
)
cegBufferPacketsEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBufferPacketsEnqueued.setStatus("current")
if mibBuilder.loadTexts:
    cegBufferPacketsEnqueued.setUnits("packet")
_CegBufferPacketsDequeued_Type = Counter32
_CegBufferPacketsDequeued_Object = MibScalar
cegBufferPacketsDequeued = _CegBufferPacketsDequeued_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 5),
    _CegBufferPacketsDequeued_Type()
)
cegBufferPacketsDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBufferPacketsDequeued.setStatus("current")
if mibBuilder.loadTexts:
    cegBufferPacketsDequeued.setUnits("packet")
_CegBufferBytesEnqueued_Type = Counter32
_CegBufferBytesEnqueued_Object = MibScalar
cegBufferBytesEnqueued = _CegBufferBytesEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 6),
    _CegBufferBytesEnqueued_Type()
)
cegBufferBytesEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBufferBytesEnqueued.setStatus("current")
if mibBuilder.loadTexts:
    cegBufferBytesEnqueued.setUnits("Bytes")
_CegBufferBytesDequeued_Type = Counter32
_CegBufferBytesDequeued_Object = MibScalar
cegBufferBytesDequeued = _CegBufferBytesDequeued_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 7),
    _CegBufferBytesDequeued_Type()
)
cegBufferBytesDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBufferBytesDequeued.setStatus("current")
if mibBuilder.loadTexts:
    cegBufferBytesDequeued.setUnits("Bytes")
_CegBufferRejMemUnavailable_Type = Counter32
_CegBufferRejMemUnavailable_Object = MibScalar
cegBufferRejMemUnavailable = _CegBufferRejMemUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 8),
    _CegBufferRejMemUnavailable_Type()
)
cegBufferRejMemUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBufferRejMemUnavailable.setStatus("current")
_CegBufferRejLowMem_Type = Counter32
_CegBufferRejLowMem_Object = MibScalar
cegBufferRejLowMem = _CegBufferRejLowMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 9),
    _CegBufferRejLowMem_Type()
)
cegBufferRejLowMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegBufferRejLowMem.setStatus("current")
_CegPacketDropDueToMaxPacketLimit_Type = Counter32
_CegPacketDropDueToMaxPacketLimit_Object = MibScalar
cegPacketDropDueToMaxPacketLimit = _CegPacketDropDueToMaxPacketLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 10),
    _CegPacketDropDueToMaxPacketLimit_Type()
)
cegPacketDropDueToMaxPacketLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegPacketDropDueToMaxPacketLimit.setStatus("current")
_CegPacketDropDueToMaxBufferLimit_Type = Counter32
_CegPacketDropDueToMaxBufferLimit_Object = MibScalar
cegPacketDropDueToMaxBufferLimit = _CegPacketDropDueToMaxBufferLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 1, 2, 11),
    _CegPacketDropDueToMaxBufferLimit_Type()
)
cegPacketDropDueToMaxBufferLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegPacketDropDueToMaxBufferLimit.setStatus("current")
_CiscoEpcGatewayConfig_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayConfig = _CiscoEpcGatewayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2)
)
_CegOverloadProtectionConfig_ObjectIdentity = ObjectIdentity
cegOverloadProtectionConfig = _CegOverloadProtectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 1)
)


class _CegCongestionLowThreshold_Type(Unsigned32):
    """Custom type cegCongestionLowThreshold based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CegCongestionLowThreshold_Type.__name__ = "Unsigned32"
_CegCongestionLowThreshold_Object = MibScalar
cegCongestionLowThreshold = _CegCongestionLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 1, 1),
    _CegCongestionLowThreshold_Type()
)
cegCongestionLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegCongestionLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cegCongestionLowThreshold.setUnits("percent")


class _CegCongestionHighThreshold_Type(Unsigned32):
    """Custom type cegCongestionHighThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CegCongestionHighThreshold_Type.__name__ = "Unsigned32"
_CegCongestionHighThreshold_Object = MibScalar
cegCongestionHighThreshold = _CegCongestionHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 1, 2),
    _CegCongestionHighThreshold_Type()
)
cegCongestionHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegCongestionHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cegCongestionHighThreshold.setUnits("percent")
_CegBufferingAgentConfig_ObjectIdentity = ObjectIdentity
cegBufferingAgentConfig = _CegBufferingAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 2)
)


class _CegBufferingAgentEnabled_Type(TruthValue):
    """Custom type cegBufferingAgentEnabled based on TruthValue"""


_CegBufferingAgentEnabled_Object = MibScalar
cegBufferingAgentEnabled = _CegBufferingAgentEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 2, 1),
    _CegBufferingAgentEnabled_Type()
)
cegBufferingAgentEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegBufferingAgentEnabled.setStatus("current")


class _CegBufferMaxSize_Type(Unsigned32):
    """Custom type cegBufferMaxSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 12000),
    )


_CegBufferMaxSize_Type.__name__ = "Unsigned32"
_CegBufferMaxSize_Object = MibScalar
cegBufferMaxSize = _CegBufferMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 2, 2),
    _CegBufferMaxSize_Type()
)
cegBufferMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegBufferMaxSize.setStatus("current")
if mibBuilder.loadTexts:
    cegBufferMaxSize.setUnits("Bytes")


class _CegBufferDiscardDataTime_Type(Unsigned32):
    """Custom type cegBufferDiscardDataTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CegBufferDiscardDataTime_Type.__name__ = "Unsigned32"
_CegBufferDiscardDataTime_Object = MibScalar
cegBufferDiscardDataTime = _CegBufferDiscardDataTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 2, 3),
    _CegBufferDiscardDataTime_Type()
)
cegBufferDiscardDataTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegBufferDiscardDataTime.setStatus("current")
if mibBuilder.loadTexts:
    cegBufferDiscardDataTime.setUnits("second")


class _CegBufferMaxPacketsPerBuffer_Type(Unsigned32):
    """Custom type cegBufferMaxPacketsPerBuffer based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_CegBufferMaxPacketsPerBuffer_Type.__name__ = "Unsigned32"
_CegBufferMaxPacketsPerBuffer_Object = MibScalar
cegBufferMaxPacketsPerBuffer = _CegBufferMaxPacketsPerBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 2, 2, 4),
    _CegBufferMaxPacketsPerBuffer_Type()
)
cegBufferMaxPacketsPerBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegBufferMaxPacketsPerBuffer.setStatus("current")
if mibBuilder.loadTexts:
    cegBufferMaxPacketsPerBuffer.setUnits("packet")
_CiscoEpcGatewayStatus_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayStatus = _CiscoEpcGatewayStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3)
)


class _CegVersion_Type(SnmpAdminString):
    """Custom type cegVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CegVersion_Type.__name__ = "SnmpAdminString"
_CegVersion_Object = MibScalar
cegVersion = _CegVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 1),
    _CegVersion_Type()
)
cegVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegVersion.setStatus("current")
_CegActivatedIpv4Bearers_Type = Gauge32
_CegActivatedIpv4Bearers_Object = MibScalar
cegActivatedIpv4Bearers = _CegActivatedIpv4Bearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 2),
    _CegActivatedIpv4Bearers_Type()
)
cegActivatedIpv4Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedIpv4Bearers.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedIpv4Bearers.setUnits("bearer")
_CegActivatedIpv6Bearers_Type = Gauge32
_CegActivatedIpv6Bearers_Object = MibScalar
cegActivatedIpv6Bearers = _CegActivatedIpv6Bearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 3),
    _CegActivatedIpv6Bearers_Type()
)
cegActivatedIpv6Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedIpv6Bearers.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedIpv6Bearers.setUnits("bearer")
_CegTotalUsers_Type = Gauge32
_CegTotalUsers_Object = MibScalar
cegTotalUsers = _CegTotalUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 4),
    _CegTotalUsers_Type()
)
cegTotalUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalUsers.setStatus("current")
_CegTotalIdleUsers_Type = Gauge32
_CegTotalIdleUsers_Object = MibScalar
cegTotalIdleUsers = _CegTotalIdleUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 5),
    _CegTotalIdleUsers_Type()
)
cegTotalIdleUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalIdleUsers.setStatus("current")
if mibBuilder.loadTexts:
    cegTotalIdleUsers.setUnits("Users")
_CegTotalSuspendedUsers_Type = Gauge32
_CegTotalSuspendedUsers_Object = MibScalar
cegTotalSuspendedUsers = _CegTotalSuspendedUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 6),
    _CegTotalSuspendedUsers_Type()
)
cegTotalSuspendedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalSuspendedUsers.setStatus("current")
_CegActivatedIpv4v6Sessions_Type = Gauge32
_CegActivatedIpv4v6Sessions_Object = MibScalar
cegActivatedIpv4v6Sessions = _CegActivatedIpv4v6Sessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 7),
    _CegActivatedIpv4v6Sessions_Type()
)
cegActivatedIpv4v6Sessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedIpv4v6Sessions.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedIpv4v6Sessions.setUnits("sessions")
_CegOverloadProtectionStatus_ObjectIdentity = ObjectIdentity
cegOverloadProtectionStatus = _CegOverloadProtectionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 8)
)


class _CegCongestionDfpWeight_Type(Unsigned32):
    """Custom type cegCongestionDfpWeight based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CegCongestionDfpWeight_Type.__name__ = "Unsigned32"
_CegCongestionDfpWeight_Object = MibScalar
cegCongestionDfpWeight = _CegCongestionDfpWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 8, 1),
    _CegCongestionDfpWeight_Type()
)
cegCongestionDfpWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionDfpWeight.setStatus("current")


class _CegCongestionStatus_Type(Integer32):
    """Custom type cegCongestionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("normal", 1))
    )


_CegCongestionStatus_Type.__name__ = "Integer32"
_CegCongestionStatus_Object = MibScalar
cegCongestionStatus = _CegCongestionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 8, 2),
    _CegCongestionStatus_Type()
)
cegCongestionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionStatus.setStatus("current")
_CegCongestionLowLastOccurTime_Type = TimeStamp
_CegCongestionLowLastOccurTime_Object = MibScalar
cegCongestionLowLastOccurTime = _CegCongestionLowLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 8, 3),
    _CegCongestionLowLastOccurTime_Type()
)
cegCongestionLowLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionLowLastOccurTime.setStatus("current")
_CegCongestionLowLastDuration_Type = TimeInterval
_CegCongestionLowLastDuration_Object = MibScalar
cegCongestionLowLastDuration = _CegCongestionLowLastDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 8, 4),
    _CegCongestionLowLastDuration_Type()
)
cegCongestionLowLastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionLowLastDuration.setStatus("current")
_CegCongestionHighLastOccurTime_Type = TimeStamp
_CegCongestionHighLastOccurTime_Object = MibScalar
cegCongestionHighLastOccurTime = _CegCongestionHighLastOccurTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 8, 5),
    _CegCongestionHighLastOccurTime_Type()
)
cegCongestionHighLastOccurTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionHighLastOccurTime.setStatus("current")
_CegCongestionHighLastDuration_Type = TimeInterval
_CegCongestionHighLastDuration_Object = MibScalar
cegCongestionHighLastDuration = _CegCongestionHighLastDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 8, 6),
    _CegCongestionHighLastDuration_Type()
)
cegCongestionHighLastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegCongestionHighLastDuration.setStatus("current")
_CegBufferStatus_ObjectIdentity = ObjectIdentity
cegBufferStatus = _CegBufferStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 9)
)
_CegTotalInUseBuffers_Type = Gauge32
_CegTotalInUseBuffers_Object = MibScalar
cegTotalInUseBuffers = _CegTotalInUseBuffers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 9, 1),
    _CegTotalInUseBuffers_Type()
)
cegTotalInUseBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalInUseBuffers.setStatus("current")
if mibBuilder.loadTexts:
    cegTotalInUseBuffers.setUnits("buffer")
_CegTotalBufferedPackets_Type = Gauge32
_CegTotalBufferedPackets_Object = MibScalar
cegTotalBufferedPackets = _CegTotalBufferedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 9, 2),
    _CegTotalBufferedPackets_Type()
)
cegTotalBufferedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalBufferedPackets.setStatus("current")
if mibBuilder.loadTexts:
    cegTotalBufferedPackets.setUnits("packet")
_CegTotalBufferedBytes_Type = Gauge32
_CegTotalBufferedBytes_Object = MibScalar
cegTotalBufferedBytes = _CegTotalBufferedBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 9, 3),
    _CegTotalBufferedBytes_Type()
)
cegTotalBufferedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalBufferedBytes.setStatus("current")
if mibBuilder.loadTexts:
    cegTotalBufferedBytes.setUnits("Bytes")
_CegTotalBufferAvailable_Type = Gauge32
_CegTotalBufferAvailable_Object = MibScalar
cegTotalBufferAvailable = _CegTotalBufferAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 9, 4),
    _CegTotalBufferAvailable_Type()
)
cegTotalBufferAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalBufferAvailable.setStatus("current")
if mibBuilder.loadTexts:
    cegTotalBufferAvailable.setUnits("Bytes")
_CegActivatedIpv4v6Bearers_Type = Gauge32
_CegActivatedIpv4v6Bearers_Object = MibScalar
cegActivatedIpv4v6Bearers = _CegActivatedIpv4v6Bearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 10),
    _CegActivatedIpv4v6Bearers_Type()
)
cegActivatedIpv4v6Bearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedIpv4v6Bearers.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedIpv4v6Bearers.setUnits("bearers")
_CegActivatedGtpv2SgwSessions_Type = Gauge32
_CegActivatedGtpv2SgwSessions_Object = MibScalar
cegActivatedGtpv2SgwSessions = _CegActivatedGtpv2SgwSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 11),
    _CegActivatedGtpv2SgwSessions_Type()
)
cegActivatedGtpv2SgwSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedGtpv2SgwSessions.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedGtpv2SgwSessions.setUnits("sessions")
_CegActivatedGtpv2PgwSessions_Type = Gauge32
_CegActivatedGtpv2PgwSessions_Object = MibScalar
cegActivatedGtpv2PgwSessions = _CegActivatedGtpv2PgwSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 12),
    _CegActivatedGtpv2PgwSessions_Type()
)
cegActivatedGtpv2PgwSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedGtpv2PgwSessions.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedGtpv2PgwSessions.setUnits("sessions")
_CegActivatedGtpv2SPgwSessions_Type = Gauge32
_CegActivatedGtpv2SPgwSessions_Object = MibScalar
cegActivatedGtpv2SPgwSessions = _CegActivatedGtpv2SPgwSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 13),
    _CegActivatedGtpv2SPgwSessions_Type()
)
cegActivatedGtpv2SPgwSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedGtpv2SPgwSessions.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedGtpv2SPgwSessions.setUnits("sessions")
_CegActivatedBearers_Type = Gauge32
_CegActivatedBearers_Object = MibScalar
cegActivatedBearers = _CegActivatedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 14),
    _CegActivatedBearers_Type()
)
cegActivatedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedBearers.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedBearers.setUnits("Bearers")
_CegActivatedDedicatedBearers_Type = Gauge32
_CegActivatedDedicatedBearers_Object = MibScalar
cegActivatedDedicatedBearers = _CegActivatedDedicatedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 15),
    _CegActivatedDedicatedBearers_Type()
)
cegActivatedDedicatedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedDedicatedBearers.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedDedicatedBearers.setUnits("Bearers")
_CegActivatedIpv4DedicatedBearers_Type = Gauge32
_CegActivatedIpv4DedicatedBearers_Object = MibScalar
cegActivatedIpv4DedicatedBearers = _CegActivatedIpv4DedicatedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 16),
    _CegActivatedIpv4DedicatedBearers_Type()
)
cegActivatedIpv4DedicatedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedIpv4DedicatedBearers.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedIpv4DedicatedBearers.setUnits("Bearers")
_CegActivatedIpv6DedicatedBearers_Type = Gauge32
_CegActivatedIpv6DedicatedBearers_Object = MibScalar
cegActivatedIpv6DedicatedBearers = _CegActivatedIpv6DedicatedBearers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 17),
    _CegActivatedIpv6DedicatedBearers_Type()
)
cegActivatedIpv6DedicatedBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegActivatedIpv6DedicatedBearers.setStatus("current")
if mibBuilder.loadTexts:
    cegActivatedIpv6DedicatedBearers.setUnits("Bearers")
_CegTotalIdleSessions_Type = Gauge32
_CegTotalIdleSessions_Object = MibScalar
cegTotalIdleSessions = _CegTotalIdleSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 3, 18),
    _CegTotalIdleSessions_Type()
)
cegTotalIdleSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cegTotalIdleSessions.setStatus("current")
if mibBuilder.loadTexts:
    cegTotalIdleSessions.setUnits("Sessions")
_CiscoEpcGatewayNotifMgmt_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayNotifMgmt = _CiscoEpcGatewayNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 4)
)


class _CegCongestionHighNotifEnable_Type(TruthValue):
    """Custom type cegCongestionHighNotifEnable based on TruthValue"""


_CegCongestionHighNotifEnable_Object = MibScalar
cegCongestionHighNotifEnable = _CegCongestionHighNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 4, 1),
    _CegCongestionHighNotifEnable_Type()
)
cegCongestionHighNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegCongestionHighNotifEnable.setStatus("current")


class _CegCongestionLowNotifEnable_Type(TruthValue):
    """Custom type cegCongestionLowNotifEnable based on TruthValue"""


_CegCongestionLowNotifEnable_Object = MibScalar
cegCongestionLowNotifEnable = _CegCongestionLowNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 4, 2),
    _CegCongestionLowNotifEnable_Type()
)
cegCongestionLowNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegCongestionLowNotifEnable.setStatus("current")


class _CegCongestionClearNotifEnable_Type(TruthValue):
    """Custom type cegCongestionClearNotifEnable based on TruthValue"""


_CegCongestionClearNotifEnable_Object = MibScalar
cegCongestionClearNotifEnable = _CegCongestionClearNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 1, 4, 3),
    _CegCongestionClearNotifEnable_Type()
)
cegCongestionClearNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cegCongestionClearNotifEnable.setStatus("current")
_CiscoEpcGatewayMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayMIBConformance = _CiscoEpcGatewayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3)
)
_CiscoEpcGatewayMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayMIBCompliances = _CiscoEpcGatewayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 1)
)
_CiscoEpcGatewayMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEpcGatewayMIBGroups = _CiscoEpcGatewayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2)
)

# Managed Objects groups

cegSystemStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 1)
)
cegSystemStatusGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegVersion"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedIpv4Bearers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedIpv6Bearers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegTotalUsers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegTotalSuspendedUsers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedIpv4v6Sessions"),
        ("CISCO-EPC-GATEWAY-MIB", "cegTotalIdleUsers"))
)
if mibBuilder.loadTexts:
    cegSystemStatusGrp.setStatus("current")

cegOverloadProtectionStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 2)
)
cegOverloadProtectionStatsGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegCongestionIncomingReqDrops"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighThresholdReached"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowThresholdReached"))
)
if mibBuilder.loadTexts:
    cegOverloadProtectionStatsGrp.setStatus("current")

cegBufferingAgentStatsGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 3)
)
cegBufferingAgentStatsGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegBuffersCreated"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferPacketsEnqueued"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferBytesEnqueued"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferPacketsDequeued"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferBytesDequeued"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBuffersDeleted"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBuffersTimedOut"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferRejMemUnavailable"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferRejLowMem"))
)
if mibBuilder.loadTexts:
    cegBufferingAgentStatsGrp.setStatus("current")

cegOverloadProtectionConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 4)
)
cegOverloadProtectionConfigGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowThreshold"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighThreshold"))
)
if mibBuilder.loadTexts:
    cegOverloadProtectionConfigGrp.setStatus("current")

cegBufferingAgentConfigGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 5)
)
cegBufferingAgentConfigGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegBufferingAgentEnabled"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferMaxSize"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferDiscardDataTime"),
        ("CISCO-EPC-GATEWAY-MIB", "cegBufferMaxPacketsPerBuffer"))
)
if mibBuilder.loadTexts:
    cegBufferingAgentConfigGrp.setStatus("current")

cegBufferingAgentStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 6)
)
cegBufferingAgentStatusGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegTotalInUseBuffers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegTotalBufferedPackets"),
        ("CISCO-EPC-GATEWAY-MIB", "cegTotalBufferedBytes"),
        ("CISCO-EPC-GATEWAY-MIB", "cegTotalBufferAvailable"))
)
if mibBuilder.loadTexts:
    cegBufferingAgentStatusGrp.setStatus("current")

cegOverloadProtectionStatusGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 7)
)
cegOverloadProtectionStatusGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegCongestionDfpWeight"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionStatus"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowLastOccurTime"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowLastDuration"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighLastOccurTime"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighLastDuration"))
)
if mibBuilder.loadTexts:
    cegOverloadProtectionStatusGrp.setStatus("current")

cegOverloadProtectionNotifMgmtGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 8)
)
cegOverloadProtectionNotifMgmtGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighNotifEnable"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowNotifEnable"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionClearNotifEnable"))
)
if mibBuilder.loadTexts:
    cegOverloadProtectionNotifMgmtGrp.setStatus("current")

cegSystemStatusGrpSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 10)
)
cegSystemStatusGrpSup1.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegActivatedIpv4v6Bearers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedGtpv2SgwSessions"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedGtpv2PgwSessions"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedGtpv2SPgwSessions"))
)
if mibBuilder.loadTexts:
    cegSystemStatusGrpSup1.setStatus("current")

cegSystemStatusGrpSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 11)
)
cegSystemStatusGrpSup2.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegActivatedBearers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedDedicatedBearers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedIpv4DedicatedBearers"),
        ("CISCO-EPC-GATEWAY-MIB", "cegActivatedIpv6DedicatedBearers"))
)
if mibBuilder.loadTexts:
    cegSystemStatusGrpSup2.setStatus("current")

cegSystemStatusGrpSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 12)
)
cegSystemStatusGrpSup3.setObjects(
    ("CISCO-EPC-GATEWAY-MIB", "cegTotalIdleSessions")
)
if mibBuilder.loadTexts:
    cegSystemStatusGrpSup3.setStatus("current")

cegBufferingAgentStatsGrpSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 13)
)
cegBufferingAgentStatsGrpSup1.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegPacketDropDueToMaxPacketLimit"),
        ("CISCO-EPC-GATEWAY-MIB", "cegPacketDropDueToMaxBufferLimit"))
)
if mibBuilder.loadTexts:
    cegBufferingAgentStatsGrpSup1.setStatus("current")


# Notification objects

cegCongestionHighThresholdNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 0, 1)
)
cegCongestionHighThresholdNotif.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegVersion"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionDfpWeight"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionStatus"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighThreshold"))
)
if mibBuilder.loadTexts:
    cegCongestionHighThresholdNotif.setStatus(
        "current"
    )

cegCongestionLowThresholdNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 0, 2)
)
cegCongestionLowThresholdNotif.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegVersion"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionDfpWeight"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionStatus"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowThreshold"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighThreshold"))
)
if mibBuilder.loadTexts:
    cegCongestionLowThresholdNotif.setStatus(
        "current"
    )

cegCongestionClearedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 0, 3)
)
cegCongestionClearedNotif.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegVersion"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionDfpWeight"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionStatus"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowThreshold"))
)
if mibBuilder.loadTexts:
    cegCongestionClearedNotif.setStatus(
        "current"
    )


# Notifications groups

cegOverloadProtectionNotifGrp = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 2, 9)
)
cegOverloadProtectionNotifGrp.setObjects(
      *(("CISCO-EPC-GATEWAY-MIB", "cegCongestionHighThresholdNotif"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionLowThresholdNotif"),
        ("CISCO-EPC-GATEWAY-MIB", "cegCongestionClearedNotif"))
)
if mibBuilder.loadTexts:
    cegOverloadProtectionNotifGrp.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoEpcGatewayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEpcGatewayMIBCompliance.setStatus(
        "deprecated"
    )

ciscoEpcGatewayMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoEpcGatewayMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoEPCGatewayMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoEPCGatewayMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoEpcGatewayMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 731, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoEpcGatewayMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-EPC-GATEWAY-MIB",
    **{"ciscoEpcGatewayMIB": ciscoEpcGatewayMIB,
       "ciscoEpcGatewayMIBNotifications": ciscoEpcGatewayMIBNotifications,
       "cegCongestionHighThresholdNotif": cegCongestionHighThresholdNotif,
       "cegCongestionLowThresholdNotif": cegCongestionLowThresholdNotif,
       "cegCongestionClearedNotif": cegCongestionClearedNotif,
       "ciscoEpcGatewayMIBObjects": ciscoEpcGatewayMIBObjects,
       "ciscoEpcGatewayStatistics": ciscoEpcGatewayStatistics,
       "cegOverloadProtectionStats": cegOverloadProtectionStats,
       "cegCongestionIncomingReqDrops": cegCongestionIncomingReqDrops,
       "cegCongestionLowThresholdReached": cegCongestionLowThresholdReached,
       "cegCongestionHighThresholdReached": cegCongestionHighThresholdReached,
       "cegBufferStats": cegBufferStats,
       "cegBuffersCreated": cegBuffersCreated,
       "cegBuffersDeleted": cegBuffersDeleted,
       "cegBuffersTimedOut": cegBuffersTimedOut,
       "cegBufferPacketsEnqueued": cegBufferPacketsEnqueued,
       "cegBufferPacketsDequeued": cegBufferPacketsDequeued,
       "cegBufferBytesEnqueued": cegBufferBytesEnqueued,
       "cegBufferBytesDequeued": cegBufferBytesDequeued,
       "cegBufferRejMemUnavailable": cegBufferRejMemUnavailable,
       "cegBufferRejLowMem": cegBufferRejLowMem,
       "cegPacketDropDueToMaxPacketLimit": cegPacketDropDueToMaxPacketLimit,
       "cegPacketDropDueToMaxBufferLimit": cegPacketDropDueToMaxBufferLimit,
       "ciscoEpcGatewayConfig": ciscoEpcGatewayConfig,
       "cegOverloadProtectionConfig": cegOverloadProtectionConfig,
       "cegCongestionLowThreshold": cegCongestionLowThreshold,
       "cegCongestionHighThreshold": cegCongestionHighThreshold,
       "cegBufferingAgentConfig": cegBufferingAgentConfig,
       "cegBufferingAgentEnabled": cegBufferingAgentEnabled,
       "cegBufferMaxSize": cegBufferMaxSize,
       "cegBufferDiscardDataTime": cegBufferDiscardDataTime,
       "cegBufferMaxPacketsPerBuffer": cegBufferMaxPacketsPerBuffer,
       "ciscoEpcGatewayStatus": ciscoEpcGatewayStatus,
       "cegVersion": cegVersion,
       "cegActivatedIpv4Bearers": cegActivatedIpv4Bearers,
       "cegActivatedIpv6Bearers": cegActivatedIpv6Bearers,
       "cegTotalUsers": cegTotalUsers,
       "cegTotalIdleUsers": cegTotalIdleUsers,
       "cegTotalSuspendedUsers": cegTotalSuspendedUsers,
       "cegActivatedIpv4v6Sessions": cegActivatedIpv4v6Sessions,
       "cegOverloadProtectionStatus": cegOverloadProtectionStatus,
       "cegCongestionDfpWeight": cegCongestionDfpWeight,
       "cegCongestionStatus": cegCongestionStatus,
       "cegCongestionLowLastOccurTime": cegCongestionLowLastOccurTime,
       "cegCongestionLowLastDuration": cegCongestionLowLastDuration,
       "cegCongestionHighLastOccurTime": cegCongestionHighLastOccurTime,
       "cegCongestionHighLastDuration": cegCongestionHighLastDuration,
       "cegBufferStatus": cegBufferStatus,
       "cegTotalInUseBuffers": cegTotalInUseBuffers,
       "cegTotalBufferedPackets": cegTotalBufferedPackets,
       "cegTotalBufferedBytes": cegTotalBufferedBytes,
       "cegTotalBufferAvailable": cegTotalBufferAvailable,
       "cegActivatedIpv4v6Bearers": cegActivatedIpv4v6Bearers,
       "cegActivatedGtpv2SgwSessions": cegActivatedGtpv2SgwSessions,
       "cegActivatedGtpv2PgwSessions": cegActivatedGtpv2PgwSessions,
       "cegActivatedGtpv2SPgwSessions": cegActivatedGtpv2SPgwSessions,
       "cegActivatedBearers": cegActivatedBearers,
       "cegActivatedDedicatedBearers": cegActivatedDedicatedBearers,
       "cegActivatedIpv4DedicatedBearers": cegActivatedIpv4DedicatedBearers,
       "cegActivatedIpv6DedicatedBearers": cegActivatedIpv6DedicatedBearers,
       "cegTotalIdleSessions": cegTotalIdleSessions,
       "ciscoEpcGatewayNotifMgmt": ciscoEpcGatewayNotifMgmt,
       "cegCongestionHighNotifEnable": cegCongestionHighNotifEnable,
       "cegCongestionLowNotifEnable": cegCongestionLowNotifEnable,
       "cegCongestionClearNotifEnable": cegCongestionClearNotifEnable,
       "ciscoEpcGatewayMIBConformance": ciscoEpcGatewayMIBConformance,
       "ciscoEpcGatewayMIBCompliances": ciscoEpcGatewayMIBCompliances,
       "ciscoEpcGatewayMIBCompliance": ciscoEpcGatewayMIBCompliance,
       "ciscoEpcGatewayMIBComplianceRev1": ciscoEpcGatewayMIBComplianceRev1,
       "ciscoEPCGatewayMIBComplianceRev2": ciscoEPCGatewayMIBComplianceRev2,
       "ciscoEpcGatewayMIBComplianceRev3": ciscoEpcGatewayMIBComplianceRev3,
       "ciscoEpcGatewayMIBGroups": ciscoEpcGatewayMIBGroups,
       "cegSystemStatusGrp": cegSystemStatusGrp,
       "cegOverloadProtectionStatsGrp": cegOverloadProtectionStatsGrp,
       "cegBufferingAgentStatsGrp": cegBufferingAgentStatsGrp,
       "cegOverloadProtectionConfigGrp": cegOverloadProtectionConfigGrp,
       "cegBufferingAgentConfigGrp": cegBufferingAgentConfigGrp,
       "cegBufferingAgentStatusGrp": cegBufferingAgentStatusGrp,
       "cegOverloadProtectionStatusGrp": cegOverloadProtectionStatusGrp,
       "cegOverloadProtectionNotifMgmtGrp": cegOverloadProtectionNotifMgmtGrp,
       "cegOverloadProtectionNotifGrp": cegOverloadProtectionNotifGrp,
       "cegSystemStatusGrpSup1": cegSystemStatusGrpSup1,
       "cegSystemStatusGrpSup2": cegSystemStatusGrpSup2,
       "cegSystemStatusGrpSup3": cegSystemStatusGrpSup3,
       "cegBufferingAgentStatsGrpSup1": cegBufferingAgentStatsGrpSup1}
)
