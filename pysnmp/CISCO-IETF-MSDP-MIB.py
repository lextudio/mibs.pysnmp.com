# SNMP MIB module (CISCO-IETF-MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-MSDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:45 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfMsdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 130)
)
ciscoIetfMsdpMIB.setRevisions(
        ("2006-05-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CMsdpMIBobjects_ObjectIdentity = ObjectIdentity
cMsdpMIBobjects = _CMsdpMIBobjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1)
)
_CMsdp_ObjectIdentity = ObjectIdentity
cMsdp = _CMsdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1)
)
_CMsdpTraps_ObjectIdentity = ObjectIdentity
cMsdpTraps = _CMsdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 0)
)
_CMsdpEnabled_Type = TruthValue
_CMsdpEnabled_Object = MibScalar
cMsdpEnabled = _CMsdpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 1),
    _CMsdpEnabled_Type()
)
cMsdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsdpEnabled.setStatus("current")
_CMsdpCacheLifetime_Type = TimeTicks
_CMsdpCacheLifetime_Object = MibScalar
cMsdpCacheLifetime = _CMsdpCacheLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 2),
    _CMsdpCacheLifetime_Type()
)
cMsdpCacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsdpCacheLifetime.setStatus("current")
_CMsdpNumSACacheEntries_Type = Gauge32
_CMsdpNumSACacheEntries_Object = MibScalar
cMsdpNumSACacheEntries = _CMsdpNumSACacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 3),
    _CMsdpNumSACacheEntries_Type()
)
cMsdpNumSACacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpNumSACacheEntries.setStatus("current")
_CMsdpRequestsTable_Object = MibTable
cMsdpRequestsTable = _CMsdpRequestsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cMsdpRequestsTable.setStatus("deprecated")
_CMsdpRequestsEntry_Object = MibTableRow
cMsdpRequestsEntry = _CMsdpRequestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 4, 1)
)
cMsdpRequestsEntry.setIndexNames(
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpRequestsGroupAddress"),
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpRequestsGroupMask"),
)
if mibBuilder.loadTexts:
    cMsdpRequestsEntry.setStatus("deprecated")
_CMsdpRequestsGroupAddress_Type = IpAddress
_CMsdpRequestsGroupAddress_Object = MibTableColumn
cMsdpRequestsGroupAddress = _CMsdpRequestsGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 4, 1, 1),
    _CMsdpRequestsGroupAddress_Type()
)
cMsdpRequestsGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpRequestsGroupAddress.setStatus("deprecated")
_CMsdpRequestsGroupMask_Type = IpAddress
_CMsdpRequestsGroupMask_Object = MibTableColumn
cMsdpRequestsGroupMask = _CMsdpRequestsGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 4, 1, 2),
    _CMsdpRequestsGroupMask_Type()
)
cMsdpRequestsGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpRequestsGroupMask.setStatus("deprecated")
_CMsdpRequestsPeer_Type = IpAddress
_CMsdpRequestsPeer_Object = MibTableColumn
cMsdpRequestsPeer = _CMsdpRequestsPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 4, 1, 3),
    _CMsdpRequestsPeer_Type()
)
cMsdpRequestsPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpRequestsPeer.setStatus("deprecated")
_CMsdpRequestsStatus_Type = RowStatus
_CMsdpRequestsStatus_Object = MibTableColumn
cMsdpRequestsStatus = _CMsdpRequestsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 4, 1, 4),
    _CMsdpRequestsStatus_Type()
)
cMsdpRequestsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpRequestsStatus.setStatus("deprecated")
_CMsdpPeerTable_Object = MibTable
cMsdpPeerTable = _CMsdpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cMsdpPeerTable.setStatus("current")
_CMsdpPeerEntry_Object = MibTableRow
cMsdpPeerEntry = _CMsdpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1)
)
cMsdpPeerEntry.setIndexNames(
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpPeerRemoteAddress"),
)
if mibBuilder.loadTexts:
    cMsdpPeerEntry.setStatus("current")
_CMsdpPeerRemoteAddress_Type = IpAddress
_CMsdpPeerRemoteAddress_Object = MibTableColumn
cMsdpPeerRemoteAddress = _CMsdpPeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 1),
    _CMsdpPeerRemoteAddress_Type()
)
cMsdpPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpPeerRemoteAddress.setStatus("current")


class _CMsdpPeerState_Type(Integer32):
    """Custom type cMsdpPeerState based on Integer32"""
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
        *(("connecting", 3),
          ("disabled", 5),
          ("established", 4),
          ("inactive", 1),
          ("listen", 2))
    )


_CMsdpPeerState_Type.__name__ = "Integer32"
_CMsdpPeerState_Object = MibTableColumn
cMsdpPeerState = _CMsdpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 3),
    _CMsdpPeerState_Type()
)
cMsdpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerState.setStatus("current")
_CMsdpPeerRPFFailures_Type = Counter32
_CMsdpPeerRPFFailures_Object = MibTableColumn
cMsdpPeerRPFFailures = _CMsdpPeerRPFFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 4),
    _CMsdpPeerRPFFailures_Type()
)
cMsdpPeerRPFFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerRPFFailures.setStatus("current")
_CMsdpPeerInSAs_Type = Counter32
_CMsdpPeerInSAs_Object = MibTableColumn
cMsdpPeerInSAs = _CMsdpPeerInSAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 5),
    _CMsdpPeerInSAs_Type()
)
cMsdpPeerInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerInSAs.setStatus("current")
_CMsdpPeerOutSAs_Type = Counter32
_CMsdpPeerOutSAs_Object = MibTableColumn
cMsdpPeerOutSAs = _CMsdpPeerOutSAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 6),
    _CMsdpPeerOutSAs_Type()
)
cMsdpPeerOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerOutSAs.setStatus("current")
_CMsdpPeerInSARequests_Type = Counter32
_CMsdpPeerInSARequests_Object = MibTableColumn
cMsdpPeerInSARequests = _CMsdpPeerInSARequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 7),
    _CMsdpPeerInSARequests_Type()
)
cMsdpPeerInSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerInSARequests.setStatus("current")
_CMsdpPeerOutSARequests_Type = Counter32
_CMsdpPeerOutSARequests_Object = MibTableColumn
cMsdpPeerOutSARequests = _CMsdpPeerOutSARequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 8),
    _CMsdpPeerOutSARequests_Type()
)
cMsdpPeerOutSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerOutSARequests.setStatus("current")
_CMsdpPeerInSAResponses_Type = Counter32
_CMsdpPeerInSAResponses_Object = MibTableColumn
cMsdpPeerInSAResponses = _CMsdpPeerInSAResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 9),
    _CMsdpPeerInSAResponses_Type()
)
cMsdpPeerInSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerInSAResponses.setStatus("deprecated")
_CMsdpPeerOutSAResponses_Type = Counter32
_CMsdpPeerOutSAResponses_Object = MibTableColumn
cMsdpPeerOutSAResponses = _CMsdpPeerOutSAResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 10),
    _CMsdpPeerOutSAResponses_Type()
)
cMsdpPeerOutSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerOutSAResponses.setStatus("deprecated")
_CMsdpPeerInControlMessages_Type = Counter32
_CMsdpPeerInControlMessages_Object = MibTableColumn
cMsdpPeerInControlMessages = _CMsdpPeerInControlMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 11),
    _CMsdpPeerInControlMessages_Type()
)
cMsdpPeerInControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerInControlMessages.setStatus("current")
_CMsdpPeerOutControlMessages_Type = Counter32
_CMsdpPeerOutControlMessages_Object = MibTableColumn
cMsdpPeerOutControlMessages = _CMsdpPeerOutControlMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 12),
    _CMsdpPeerOutControlMessages_Type()
)
cMsdpPeerOutControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerOutControlMessages.setStatus("current")
_CMsdpPeerInDataPackets_Type = Counter32
_CMsdpPeerInDataPackets_Object = MibTableColumn
cMsdpPeerInDataPackets = _CMsdpPeerInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 13),
    _CMsdpPeerInDataPackets_Type()
)
cMsdpPeerInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerInDataPackets.setStatus("current")
_CMsdpPeerOutDataPackets_Type = Counter32
_CMsdpPeerOutDataPackets_Object = MibTableColumn
cMsdpPeerOutDataPackets = _CMsdpPeerOutDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 14),
    _CMsdpPeerOutDataPackets_Type()
)
cMsdpPeerOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerOutDataPackets.setStatus("current")
_CMsdpPeerFsmEstablishedTransitions_Type = Counter32
_CMsdpPeerFsmEstablishedTransitions_Object = MibTableColumn
cMsdpPeerFsmEstablishedTransitions = _CMsdpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 15),
    _CMsdpPeerFsmEstablishedTransitions_Type()
)
cMsdpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerFsmEstablishedTransitions.setStatus("current")
_CMsdpPeerFsmEstablishedTime_Type = TimeStamp
_CMsdpPeerFsmEstablishedTime_Object = MibTableColumn
cMsdpPeerFsmEstablishedTime = _CMsdpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 16),
    _CMsdpPeerFsmEstablishedTime_Type()
)
cMsdpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerFsmEstablishedTime.setStatus("current")
_CMsdpPeerInMessageTime_Type = TimeStamp
_CMsdpPeerInMessageTime_Object = MibTableColumn
cMsdpPeerInMessageTime = _CMsdpPeerInMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 17),
    _CMsdpPeerInMessageTime_Type()
)
cMsdpPeerInMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerInMessageTime.setStatus("current")
_CMsdpPeerLocalAddress_Type = IpAddress
_CMsdpPeerLocalAddress_Object = MibTableColumn
cMsdpPeerLocalAddress = _CMsdpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 18),
    _CMsdpPeerLocalAddress_Type()
)
cMsdpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerLocalAddress.setStatus("current")


class _CMsdpPeerConnectRetryInterval_Type(Integer32):
    """Custom type cMsdpPeerConnectRetryInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CMsdpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_CMsdpPeerConnectRetryInterval_Object = MibTableColumn
cMsdpPeerConnectRetryInterval = _CMsdpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 20),
    _CMsdpPeerConnectRetryInterval_Type()
)
cMsdpPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cMsdpPeerConnectRetryInterval.setUnits("seconds")


class _CMsdpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type cMsdpPeerHoldTimeConfigured based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_CMsdpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_CMsdpPeerHoldTimeConfigured_Object = MibTableColumn
cMsdpPeerHoldTimeConfigured = _CMsdpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 21),
    _CMsdpPeerHoldTimeConfigured_Type()
)
cMsdpPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    cMsdpPeerHoldTimeConfigured.setUnits("seconds")


class _CMsdpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type cMsdpPeerKeepAliveConfigured based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_CMsdpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_CMsdpPeerKeepAliveConfigured_Object = MibTableColumn
cMsdpPeerKeepAliveConfigured = _CMsdpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 22),
    _CMsdpPeerKeepAliveConfigured_Type()
)
cMsdpPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    cMsdpPeerKeepAliveConfigured.setUnits("seconds")


class _CMsdpPeerDataTtl_Type(Integer32):
    """Custom type cMsdpPeerDataTtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CMsdpPeerDataTtl_Type.__name__ = "Integer32"
_CMsdpPeerDataTtl_Object = MibTableColumn
cMsdpPeerDataTtl = _CMsdpPeerDataTtl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 23),
    _CMsdpPeerDataTtl_Type()
)
cMsdpPeerDataTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerDataTtl.setStatus("current")
_CMsdpPeerProcessRequestsFrom_Type = TruthValue
_CMsdpPeerProcessRequestsFrom_Object = MibTableColumn
cMsdpPeerProcessRequestsFrom = _CMsdpPeerProcessRequestsFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 24),
    _CMsdpPeerProcessRequestsFrom_Type()
)
cMsdpPeerProcessRequestsFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerProcessRequestsFrom.setStatus("deprecated")
_CMsdpPeerStatus_Type = RowStatus
_CMsdpPeerStatus_Object = MibTableColumn
cMsdpPeerStatus = _CMsdpPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 25),
    _CMsdpPeerStatus_Type()
)
cMsdpPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerStatus.setStatus("current")


class _CMsdpPeerRemotePort_Type(Integer32):
    """Custom type cMsdpPeerRemotePort based on Integer32"""
    defaultValue = 639

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CMsdpPeerRemotePort_Type.__name__ = "Integer32"
_CMsdpPeerRemotePort_Object = MibTableColumn
cMsdpPeerRemotePort = _CMsdpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 26),
    _CMsdpPeerRemotePort_Type()
)
cMsdpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerRemotePort.setStatus("current")


class _CMsdpPeerLocalPort_Type(Integer32):
    """Custom type cMsdpPeerLocalPort based on Integer32"""
    defaultValue = 639

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CMsdpPeerLocalPort_Type.__name__ = "Integer32"
_CMsdpPeerLocalPort_Object = MibTableColumn
cMsdpPeerLocalPort = _CMsdpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 27),
    _CMsdpPeerLocalPort_Type()
)
cMsdpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerLocalPort.setStatus("current")


class _CMsdpPeerEncapsulationType_Type(Integer32):
    """Custom type cMsdpPeerEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tcp", 1))
    )


_CMsdpPeerEncapsulationType_Type.__name__ = "Integer32"
_CMsdpPeerEncapsulationType_Object = MibTableColumn
cMsdpPeerEncapsulationType = _CMsdpPeerEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 29),
    _CMsdpPeerEncapsulationType_Type()
)
cMsdpPeerEncapsulationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpPeerEncapsulationType.setStatus("current")
_CMsdpPeerConnectionAttempts_Type = Counter32
_CMsdpPeerConnectionAttempts_Object = MibTableColumn
cMsdpPeerConnectionAttempts = _CMsdpPeerConnectionAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 30),
    _CMsdpPeerConnectionAttempts_Type()
)
cMsdpPeerConnectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerConnectionAttempts.setStatus("current")
_CMsdpPeerInNotifications_Type = Counter32
_CMsdpPeerInNotifications_Object = MibTableColumn
cMsdpPeerInNotifications = _CMsdpPeerInNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 31),
    _CMsdpPeerInNotifications_Type()
)
cMsdpPeerInNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerInNotifications.setStatus("deprecated")
_CMsdpPeerOutNotifications_Type = Counter32
_CMsdpPeerOutNotifications_Object = MibTableColumn
cMsdpPeerOutNotifications = _CMsdpPeerOutNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 32),
    _CMsdpPeerOutNotifications_Type()
)
cMsdpPeerOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerOutNotifications.setStatus("deprecated")


class _CMsdpPeerLastError_Type(OctetString):
    """Custom type cMsdpPeerLastError based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_CMsdpPeerLastError_Type.__name__ = "OctetString"
_CMsdpPeerLastError_Object = MibTableColumn
cMsdpPeerLastError = _CMsdpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 33),
    _CMsdpPeerLastError_Type()
)
cMsdpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerLastError.setStatus("deprecated")
_CMsdpPeerDiscontinuityTime_Type = TimeStamp
_CMsdpPeerDiscontinuityTime_Object = MibTableColumn
cMsdpPeerDiscontinuityTime = _CMsdpPeerDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 5, 1, 34),
    _CMsdpPeerDiscontinuityTime_Type()
)
cMsdpPeerDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpPeerDiscontinuityTime.setStatus("current")
_CMsdpSACacheTable_Object = MibTable
cMsdpSACacheTable = _CMsdpSACacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cMsdpSACacheTable.setStatus("current")
_CMsdpSACacheEntry_Object = MibTableRow
cMsdpSACacheEntry = _CMsdpSACacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1)
)
cMsdpSACacheEntry.setIndexNames(
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpSACacheGroupAddr"),
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpSACacheSourceAddr"),
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpSACacheOriginRP"),
)
if mibBuilder.loadTexts:
    cMsdpSACacheEntry.setStatus("current")
_CMsdpSACacheGroupAddr_Type = IpAddress
_CMsdpSACacheGroupAddr_Object = MibTableColumn
cMsdpSACacheGroupAddr = _CMsdpSACacheGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 1),
    _CMsdpSACacheGroupAddr_Type()
)
cMsdpSACacheGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpSACacheGroupAddr.setStatus("current")
_CMsdpSACacheSourceAddr_Type = IpAddress
_CMsdpSACacheSourceAddr_Object = MibTableColumn
cMsdpSACacheSourceAddr = _CMsdpSACacheSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 2),
    _CMsdpSACacheSourceAddr_Type()
)
cMsdpSACacheSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpSACacheSourceAddr.setStatus("current")
_CMsdpSACacheOriginRP_Type = IpAddress
_CMsdpSACacheOriginRP_Object = MibTableColumn
cMsdpSACacheOriginRP = _CMsdpSACacheOriginRP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 3),
    _CMsdpSACacheOriginRP_Type()
)
cMsdpSACacheOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpSACacheOriginRP.setStatus("current")
_CMsdpSACachePeerLearnedFrom_Type = IpAddress
_CMsdpSACachePeerLearnedFrom_Object = MibTableColumn
cMsdpSACachePeerLearnedFrom = _CMsdpSACachePeerLearnedFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 4),
    _CMsdpSACachePeerLearnedFrom_Type()
)
cMsdpSACachePeerLearnedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpSACachePeerLearnedFrom.setStatus("current")
_CMsdpSACacheRPFPeer_Type = IpAddress
_CMsdpSACacheRPFPeer_Object = MibTableColumn
cMsdpSACacheRPFPeer = _CMsdpSACacheRPFPeer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 5),
    _CMsdpSACacheRPFPeer_Type()
)
cMsdpSACacheRPFPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpSACacheRPFPeer.setStatus("current")
_CMsdpSACacheInSAs_Type = Counter32
_CMsdpSACacheInSAs_Object = MibTableColumn
cMsdpSACacheInSAs = _CMsdpSACacheInSAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 6),
    _CMsdpSACacheInSAs_Type()
)
cMsdpSACacheInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpSACacheInSAs.setStatus("current")
_CMsdpSACacheInDataPackets_Type = Counter32
_CMsdpSACacheInDataPackets_Object = MibTableColumn
cMsdpSACacheInDataPackets = _CMsdpSACacheInDataPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 7),
    _CMsdpSACacheInDataPackets_Type()
)
cMsdpSACacheInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpSACacheInDataPackets.setStatus("current")
_CMsdpSACacheUpTime_Type = TimeTicks
_CMsdpSACacheUpTime_Object = MibTableColumn
cMsdpSACacheUpTime = _CMsdpSACacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 8),
    _CMsdpSACacheUpTime_Type()
)
cMsdpSACacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpSACacheUpTime.setStatus("current")
_CMsdpSACacheExpiryTime_Type = TimeTicks
_CMsdpSACacheExpiryTime_Object = MibTableColumn
cMsdpSACacheExpiryTime = _CMsdpSACacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 9),
    _CMsdpSACacheExpiryTime_Type()
)
cMsdpSACacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cMsdpSACacheExpiryTime.setStatus("current")
_CMsdpSACacheStatus_Type = RowStatus
_CMsdpSACacheStatus_Object = MibTableColumn
cMsdpSACacheStatus = _CMsdpSACacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 6, 1, 10),
    _CMsdpSACacheStatus_Type()
)
cMsdpSACacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsdpSACacheStatus.setStatus("current")
_CMsdpMIBConformance_ObjectIdentity = ObjectIdentity
cMsdpMIBConformance = _CMsdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8)
)
_CMsdpMIBCompliances_ObjectIdentity = ObjectIdentity
cMsdpMIBCompliances = _CMsdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 1)
)
_CMsdpMIBGroups_ObjectIdentity = ObjectIdentity
cMsdpMIBGroups = _CMsdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2)
)
_CMsdpRPAddress_Type = IpAddress
_CMsdpRPAddress_Object = MibScalar
cMsdpRPAddress = _CMsdpRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 11),
    _CMsdpRPAddress_Type()
)
cMsdpRPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cMsdpRPAddress.setStatus("current")
_CMsdpMeshGroupTable_Object = MibTable
cMsdpMeshGroupTable = _CMsdpMeshGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cMsdpMeshGroupTable.setStatus("current")
_CMsdpMeshGroupEntry_Object = MibTableRow
cMsdpMeshGroupEntry = _CMsdpMeshGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 12, 1)
)
cMsdpMeshGroupEntry.setIndexNames(
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpMeshGroupName"),
    (0, "CISCO-IETF-MSDP-MIB", "cMsdpMeshGroupPeerAddress"),
)
if mibBuilder.loadTexts:
    cMsdpMeshGroupEntry.setStatus("current")


class _CMsdpMeshGroupName_Type(DisplayString):
    """Custom type cMsdpMeshGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CMsdpMeshGroupName_Type.__name__ = "DisplayString"
_CMsdpMeshGroupName_Object = MibTableColumn
cMsdpMeshGroupName = _CMsdpMeshGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 12, 1, 1),
    _CMsdpMeshGroupName_Type()
)
cMsdpMeshGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpMeshGroupName.setStatus("current")
_CMsdpMeshGroupPeerAddress_Type = IpAddress
_CMsdpMeshGroupPeerAddress_Object = MibTableColumn
cMsdpMeshGroupPeerAddress = _CMsdpMeshGroupPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 12, 1, 2),
    _CMsdpMeshGroupPeerAddress_Type()
)
cMsdpMeshGroupPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cMsdpMeshGroupPeerAddress.setStatus("current")
_CMsdpMeshGroupStatus_Type = RowStatus
_CMsdpMeshGroupStatus_Object = MibTableColumn
cMsdpMeshGroupStatus = _CMsdpMeshGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 12, 1, 3),
    _CMsdpMeshGroupStatus_Type()
)
cMsdpMeshGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cMsdpMeshGroupStatus.setStatus("current")

# Managed Objects groups

cMsdpMIBGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 1)
)
cMsdpMIBGlobalsGroup.setObjects(
    ("CISCO-IETF-MSDP-MIB", "cMsdpEnabled")
)
if mibBuilder.loadTexts:
    cMsdpMIBGlobalsGroup.setStatus("current")

cMsdpMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 2)
)
cMsdpMIBPeerGroup.setObjects(
      *(("CISCO-IETF-MSDP-MIB", "cMsdpPeerRPFFailures"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerState"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInSAs"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutSAs"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInSARequests"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutSARequests"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInSAResponses"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutSAResponses"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInNotifications"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutNotifications"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInControlMessages"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutControlMessages"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerFsmEstablishedTransitions"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerFsmEstablishedTime"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerLocalAddress"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerRemotePort"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerLocalPort"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerConnectRetryInterval"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerHoldTimeConfigured"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerKeepAliveConfigured"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInMessageTime"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerProcessRequestsFrom"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerConnectionAttempts"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerLastError"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerStatus"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    cMsdpMIBPeerGroup.setStatus("deprecated")

cMsdpMIBEncapsulationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 3)
)
cMsdpMIBEncapsulationGroup.setObjects(
      *(("CISCO-IETF-MSDP-MIB", "cMsdpPeerInDataPackets"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutDataPackets"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerDataTtl"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerEncapsulationType"))
)
if mibBuilder.loadTexts:
    cMsdpMIBEncapsulationGroup.setStatus("current")

cMsdpMIBSACacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 4)
)
cMsdpMIBSACacheGroup.setObjects(
      *(("CISCO-IETF-MSDP-MIB", "cMsdpCacheLifetime"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpNumSACacheEntries"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpSACachePeerLearnedFrom"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpSACacheRPFPeer"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpSACacheInSAs"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpSACacheInDataPackets"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpSACacheUpTime"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpSACacheExpiryTime"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpSACacheStatus"))
)
if mibBuilder.loadTexts:
    cMsdpMIBSACacheGroup.setStatus("current")

cMsdpMIBRequestsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 6)
)
cMsdpMIBRequestsGroup.setObjects(
      *(("CISCO-IETF-MSDP-MIB", "cMsdpRequestsPeer"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpRequestsStatus"))
)
if mibBuilder.loadTexts:
    cMsdpMIBRequestsGroup.setStatus("deprecated")

cMsdpMIBRPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 7)
)
cMsdpMIBRPGroup.setObjects(
    ("CISCO-IETF-MSDP-MIB", "cMsdpRPAddress")
)
if mibBuilder.loadTexts:
    cMsdpMIBRPGroup.setStatus("current")

cMsdpMIBMeshGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 8)
)
cMsdpMIBMeshGroupGroup.setObjects(
    ("CISCO-IETF-MSDP-MIB", "cMsdpMeshGroupStatus")
)
if mibBuilder.loadTexts:
    cMsdpMIBMeshGroupGroup.setStatus("current")

cMsdpMIBPeerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 9)
)
cMsdpMIBPeerGroup2.setObjects(
      *(("CISCO-IETF-MSDP-MIB", "cMsdpPeerRPFFailures"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerState"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInSAs"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutSAs"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInSARequests"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutSARequests"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInControlMessages"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerOutControlMessages"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerFsmEstablishedTransitions"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerFsmEstablishedTime"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerLocalAddress"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerRemotePort"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerLocalPort"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerConnectRetryInterval"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerHoldTimeConfigured"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerKeepAliveConfigured"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerInMessageTime"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerConnectionAttempts"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerStatus"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpPeerDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    cMsdpMIBPeerGroup2.setStatus("current")


# Notification objects

cMsdpEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 0, 1)
)
cMsdpEstablished.setObjects(
    ("CISCO-IETF-MSDP-MIB", "cMsdpPeerFsmEstablishedTransitions")
)
if mibBuilder.loadTexts:
    cMsdpEstablished.setStatus(
        "current"
    )

cMsdpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 0, 2)
)
cMsdpBackwardTransition.setObjects(
    ("CISCO-IETF-MSDP-MIB", "cMsdpPeerState")
)
if mibBuilder.loadTexts:
    cMsdpBackwardTransition.setStatus(
        "current"
    )


# Notifications groups

cMsdpMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 2, 5)
)
cMsdpMIBNotificationGroup.setObjects(
      *(("CISCO-IETF-MSDP-MIB", "cMsdpEstablished"),
        ("CISCO-IETF-MSDP-MIB", "cMsdpBackwardTransition"))
)
if mibBuilder.loadTexts:
    cMsdpMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cMsdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    cMsdpMIBCompliance.setStatus(
        "deprecated"
    )

cMsdpMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    cMsdpMIBFullCompliance.setStatus(
        "current"
    )

cMsdpMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 130, 1, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    cMsdpMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-MSDP-MIB",
    **{"ciscoIetfMsdpMIB": ciscoIetfMsdpMIB,
       "cMsdpMIBobjects": cMsdpMIBobjects,
       "cMsdp": cMsdp,
       "cMsdpTraps": cMsdpTraps,
       "cMsdpEstablished": cMsdpEstablished,
       "cMsdpBackwardTransition": cMsdpBackwardTransition,
       "cMsdpEnabled": cMsdpEnabled,
       "cMsdpCacheLifetime": cMsdpCacheLifetime,
       "cMsdpNumSACacheEntries": cMsdpNumSACacheEntries,
       "cMsdpRequestsTable": cMsdpRequestsTable,
       "cMsdpRequestsEntry": cMsdpRequestsEntry,
       "cMsdpRequestsGroupAddress": cMsdpRequestsGroupAddress,
       "cMsdpRequestsGroupMask": cMsdpRequestsGroupMask,
       "cMsdpRequestsPeer": cMsdpRequestsPeer,
       "cMsdpRequestsStatus": cMsdpRequestsStatus,
       "cMsdpPeerTable": cMsdpPeerTable,
       "cMsdpPeerEntry": cMsdpPeerEntry,
       "cMsdpPeerRemoteAddress": cMsdpPeerRemoteAddress,
       "cMsdpPeerState": cMsdpPeerState,
       "cMsdpPeerRPFFailures": cMsdpPeerRPFFailures,
       "cMsdpPeerInSAs": cMsdpPeerInSAs,
       "cMsdpPeerOutSAs": cMsdpPeerOutSAs,
       "cMsdpPeerInSARequests": cMsdpPeerInSARequests,
       "cMsdpPeerOutSARequests": cMsdpPeerOutSARequests,
       "cMsdpPeerInSAResponses": cMsdpPeerInSAResponses,
       "cMsdpPeerOutSAResponses": cMsdpPeerOutSAResponses,
       "cMsdpPeerInControlMessages": cMsdpPeerInControlMessages,
       "cMsdpPeerOutControlMessages": cMsdpPeerOutControlMessages,
       "cMsdpPeerInDataPackets": cMsdpPeerInDataPackets,
       "cMsdpPeerOutDataPackets": cMsdpPeerOutDataPackets,
       "cMsdpPeerFsmEstablishedTransitions": cMsdpPeerFsmEstablishedTransitions,
       "cMsdpPeerFsmEstablishedTime": cMsdpPeerFsmEstablishedTime,
       "cMsdpPeerInMessageTime": cMsdpPeerInMessageTime,
       "cMsdpPeerLocalAddress": cMsdpPeerLocalAddress,
       "cMsdpPeerConnectRetryInterval": cMsdpPeerConnectRetryInterval,
       "cMsdpPeerHoldTimeConfigured": cMsdpPeerHoldTimeConfigured,
       "cMsdpPeerKeepAliveConfigured": cMsdpPeerKeepAliveConfigured,
       "cMsdpPeerDataTtl": cMsdpPeerDataTtl,
       "cMsdpPeerProcessRequestsFrom": cMsdpPeerProcessRequestsFrom,
       "cMsdpPeerStatus": cMsdpPeerStatus,
       "cMsdpPeerRemotePort": cMsdpPeerRemotePort,
       "cMsdpPeerLocalPort": cMsdpPeerLocalPort,
       "cMsdpPeerEncapsulationType": cMsdpPeerEncapsulationType,
       "cMsdpPeerConnectionAttempts": cMsdpPeerConnectionAttempts,
       "cMsdpPeerInNotifications": cMsdpPeerInNotifications,
       "cMsdpPeerOutNotifications": cMsdpPeerOutNotifications,
       "cMsdpPeerLastError": cMsdpPeerLastError,
       "cMsdpPeerDiscontinuityTime": cMsdpPeerDiscontinuityTime,
       "cMsdpSACacheTable": cMsdpSACacheTable,
       "cMsdpSACacheEntry": cMsdpSACacheEntry,
       "cMsdpSACacheGroupAddr": cMsdpSACacheGroupAddr,
       "cMsdpSACacheSourceAddr": cMsdpSACacheSourceAddr,
       "cMsdpSACacheOriginRP": cMsdpSACacheOriginRP,
       "cMsdpSACachePeerLearnedFrom": cMsdpSACachePeerLearnedFrom,
       "cMsdpSACacheRPFPeer": cMsdpSACacheRPFPeer,
       "cMsdpSACacheInSAs": cMsdpSACacheInSAs,
       "cMsdpSACacheInDataPackets": cMsdpSACacheInDataPackets,
       "cMsdpSACacheUpTime": cMsdpSACacheUpTime,
       "cMsdpSACacheExpiryTime": cMsdpSACacheExpiryTime,
       "cMsdpSACacheStatus": cMsdpSACacheStatus,
       "cMsdpMIBConformance": cMsdpMIBConformance,
       "cMsdpMIBCompliances": cMsdpMIBCompliances,
       "cMsdpMIBCompliance": cMsdpMIBCompliance,
       "cMsdpMIBFullCompliance": cMsdpMIBFullCompliance,
       "cMsdpMIBReadOnlyCompliance": cMsdpMIBReadOnlyCompliance,
       "cMsdpMIBGroups": cMsdpMIBGroups,
       "cMsdpMIBGlobalsGroup": cMsdpMIBGlobalsGroup,
       "cMsdpMIBPeerGroup": cMsdpMIBPeerGroup,
       "cMsdpMIBEncapsulationGroup": cMsdpMIBEncapsulationGroup,
       "cMsdpMIBSACacheGroup": cMsdpMIBSACacheGroup,
       "cMsdpMIBNotificationGroup": cMsdpMIBNotificationGroup,
       "cMsdpMIBRequestsGroup": cMsdpMIBRequestsGroup,
       "cMsdpMIBRPGroup": cMsdpMIBRPGroup,
       "cMsdpMIBMeshGroupGroup": cMsdpMIBMeshGroupGroup,
       "cMsdpMIBPeerGroup2": cMsdpMIBPeerGroup2,
       "cMsdpRPAddress": cMsdpRPAddress,
       "cMsdpMeshGroupTable": cMsdpMeshGroupTable,
       "cMsdpMeshGroupEntry": cMsdpMeshGroupEntry,
       "cMsdpMeshGroupName": cMsdpMeshGroupName,
       "cMsdpMeshGroupPeerAddress": cMsdpMeshGroupPeerAddress,
       "cMsdpMeshGroupStatus": cMsdpMeshGroupStatus}
)
