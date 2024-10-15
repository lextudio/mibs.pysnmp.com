# SNMP MIB module (DRAFT-MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DRAFT-MSDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:33:28 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

msdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 92)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MsdpMIBobjects_ObjectIdentity = ObjectIdentity
msdpMIBobjects = _MsdpMIBobjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1)
)
_Msdp_ObjectIdentity = ObjectIdentity
msdp = _Msdp_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 1)
)
_MsdpEnabled_Type = TruthValue
_MsdpEnabled_Object = MibScalar
msdpEnabled = _MsdpEnabled_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 1),
    _MsdpEnabled_Type()
)
msdpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpEnabled.setStatus("current")
_MsdpCacheLifetime_Type = TimeTicks
_MsdpCacheLifetime_Object = MibScalar
msdpCacheLifetime = _MsdpCacheLifetime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 2),
    _MsdpCacheLifetime_Type()
)
msdpCacheLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpCacheLifetime.setStatus("current")
_MsdpNumSACacheEntries_Type = Gauge32
_MsdpNumSACacheEntries_Object = MibScalar
msdpNumSACacheEntries = _MsdpNumSACacheEntries_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 3),
    _MsdpNumSACacheEntries_Type()
)
msdpNumSACacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpNumSACacheEntries.setStatus("current")
_MsdpRequestsTable_Object = MibTable
msdpRequestsTable = _MsdpRequestsTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4)
)
if mibBuilder.loadTexts:
    msdpRequestsTable.setStatus("current")
_MsdpRequestsEntry_Object = MibTableRow
msdpRequestsEntry = _MsdpRequestsEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1)
)
msdpRequestsEntry.setIndexNames(
    (0, "DRAFT-MSDP-MIB", "msdpRequestsGroupAddress"),
    (0, "DRAFT-MSDP-MIB", "msdpRequestsGroupMask"),
)
if mibBuilder.loadTexts:
    msdpRequestsEntry.setStatus("current")
_MsdpRequestsGroupAddress_Type = IpAddress
_MsdpRequestsGroupAddress_Object = MibTableColumn
msdpRequestsGroupAddress = _MsdpRequestsGroupAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 1),
    _MsdpRequestsGroupAddress_Type()
)
msdpRequestsGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsGroupAddress.setStatus("current")
_MsdpRequestsGroupMask_Type = IpAddress
_MsdpRequestsGroupMask_Object = MibTableColumn
msdpRequestsGroupMask = _MsdpRequestsGroupMask_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 2),
    _MsdpRequestsGroupMask_Type()
)
msdpRequestsGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsGroupMask.setStatus("current")
_MsdpRequestsPeer_Type = IpAddress
_MsdpRequestsPeer_Object = MibTableColumn
msdpRequestsPeer = _MsdpRequestsPeer_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 3),
    _MsdpRequestsPeer_Type()
)
msdpRequestsPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpRequestsPeer.setStatus("current")
_MsdpRequestsStatus_Type = RowStatus
_MsdpRequestsStatus_Object = MibTableColumn
msdpRequestsStatus = _MsdpRequestsStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 4),
    _MsdpRequestsStatus_Type()
)
msdpRequestsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpRequestsStatus.setStatus("current")
_MsdpPeerTable_Object = MibTable
msdpPeerTable = _MsdpPeerTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5)
)
if mibBuilder.loadTexts:
    msdpPeerTable.setStatus("current")
_MsdpPeerEntry_Object = MibTableRow
msdpPeerEntry = _MsdpPeerEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1)
)
msdpPeerEntry.setIndexNames(
    (0, "DRAFT-MSDP-MIB", "msdpPeerRemoteAddress"),
)
if mibBuilder.loadTexts:
    msdpPeerEntry.setStatus("current")
_MsdpPeerRemoteAddress_Type = IpAddress
_MsdpPeerRemoteAddress_Object = MibTableColumn
msdpPeerRemoteAddress = _MsdpPeerRemoteAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 1),
    _MsdpPeerRemoteAddress_Type()
)
msdpPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpPeerRemoteAddress.setStatus("current")


class _MsdpPeerState_Type(Integer32):
    """Custom type msdpPeerState based on Integer32"""
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


_MsdpPeerState_Type.__name__ = "Integer32"
_MsdpPeerState_Object = MibTableColumn
msdpPeerState = _MsdpPeerState_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 3),
    _MsdpPeerState_Type()
)
msdpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerState.setStatus("current")
_MsdpPeerRPFFailures_Type = Counter32
_MsdpPeerRPFFailures_Object = MibTableColumn
msdpPeerRPFFailures = _MsdpPeerRPFFailures_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 4),
    _MsdpPeerRPFFailures_Type()
)
msdpPeerRPFFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerRPFFailures.setStatus("current")
_MsdpPeerInSAs_Type = Counter32
_MsdpPeerInSAs_Object = MibTableColumn
msdpPeerInSAs = _MsdpPeerInSAs_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 5),
    _MsdpPeerInSAs_Type()
)
msdpPeerInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInSAs.setStatus("current")
_MsdpPeerOutSAs_Type = Counter32
_MsdpPeerOutSAs_Object = MibTableColumn
msdpPeerOutSAs = _MsdpPeerOutSAs_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 6),
    _MsdpPeerOutSAs_Type()
)
msdpPeerOutSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutSAs.setStatus("current")
_MsdpPeerInSARequests_Type = Counter32
_MsdpPeerInSARequests_Object = MibTableColumn
msdpPeerInSARequests = _MsdpPeerInSARequests_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 7),
    _MsdpPeerInSARequests_Type()
)
msdpPeerInSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInSARequests.setStatus("current")
_MsdpPeerOutSARequests_Type = Counter32
_MsdpPeerOutSARequests_Object = MibTableColumn
msdpPeerOutSARequests = _MsdpPeerOutSARequests_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 8),
    _MsdpPeerOutSARequests_Type()
)
msdpPeerOutSARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutSARequests.setStatus("current")
_MsdpPeerInSAResponses_Type = Counter32
_MsdpPeerInSAResponses_Object = MibTableColumn
msdpPeerInSAResponses = _MsdpPeerInSAResponses_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 9),
    _MsdpPeerInSAResponses_Type()
)
msdpPeerInSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInSAResponses.setStatus("current")
_MsdpPeerOutSAResponses_Type = Counter32
_MsdpPeerOutSAResponses_Object = MibTableColumn
msdpPeerOutSAResponses = _MsdpPeerOutSAResponses_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 10),
    _MsdpPeerOutSAResponses_Type()
)
msdpPeerOutSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutSAResponses.setStatus("current")
_MsdpPeerInControlMessages_Type = Counter32
_MsdpPeerInControlMessages_Object = MibTableColumn
msdpPeerInControlMessages = _MsdpPeerInControlMessages_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 11),
    _MsdpPeerInControlMessages_Type()
)
msdpPeerInControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInControlMessages.setStatus("current")
_MsdpPeerOutControlMessages_Type = Counter32
_MsdpPeerOutControlMessages_Object = MibTableColumn
msdpPeerOutControlMessages = _MsdpPeerOutControlMessages_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 12),
    _MsdpPeerOutControlMessages_Type()
)
msdpPeerOutControlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutControlMessages.setStatus("current")
_MsdpPeerInDataPackets_Type = Counter32
_MsdpPeerInDataPackets_Object = MibTableColumn
msdpPeerInDataPackets = _MsdpPeerInDataPackets_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 13),
    _MsdpPeerInDataPackets_Type()
)
msdpPeerInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInDataPackets.setStatus("current")
_MsdpPeerOutDataPackets_Type = Counter32
_MsdpPeerOutDataPackets_Object = MibTableColumn
msdpPeerOutDataPackets = _MsdpPeerOutDataPackets_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 14),
    _MsdpPeerOutDataPackets_Type()
)
msdpPeerOutDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutDataPackets.setStatus("current")
_MsdpPeerFsmEstablishedTransitions_Type = Counter32
_MsdpPeerFsmEstablishedTransitions_Object = MibTableColumn
msdpPeerFsmEstablishedTransitions = _MsdpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 15),
    _MsdpPeerFsmEstablishedTransitions_Type()
)
msdpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerFsmEstablishedTransitions.setStatus("current")
_MsdpPeerFsmEstablishedTime_Type = Gauge32
_MsdpPeerFsmEstablishedTime_Object = MibTableColumn
msdpPeerFsmEstablishedTime = _MsdpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 16),
    _MsdpPeerFsmEstablishedTime_Type()
)
msdpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerFsmEstablishedTime.setUnits("seconds")
_MsdpPeerInMessageElapsedTime_Type = Gauge32
_MsdpPeerInMessageElapsedTime_Object = MibTableColumn
msdpPeerInMessageElapsedTime = _MsdpPeerInMessageElapsedTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 17),
    _MsdpPeerInMessageElapsedTime_Type()
)
msdpPeerInMessageElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInMessageElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerInMessageElapsedTime.setUnits("seconds")
_MsdpPeerLocalAddress_Type = IpAddress
_MsdpPeerLocalAddress_Object = MibTableColumn
msdpPeerLocalAddress = _MsdpPeerLocalAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 18),
    _MsdpPeerLocalAddress_Type()
)
msdpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerLocalAddress.setStatus("current")


class _MsdpPeerSAAdvPeriod_Type(Integer32):
    """Custom type msdpPeerSAAdvPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdpPeerSAAdvPeriod_Type.__name__ = "Integer32"
_MsdpPeerSAAdvPeriod_Object = MibTableColumn
msdpPeerSAAdvPeriod = _MsdpPeerSAAdvPeriod_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 19),
    _MsdpPeerSAAdvPeriod_Type()
)
msdpPeerSAAdvPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerSAAdvPeriod.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerSAAdvPeriod.setUnits("seconds")


class _MsdpPeerConnectRetryInterval_Type(Integer32):
    """Custom type msdpPeerConnectRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MsdpPeerConnectRetryInterval_Type.__name__ = "Integer32"
_MsdpPeerConnectRetryInterval_Object = MibTableColumn
msdpPeerConnectRetryInterval = _MsdpPeerConnectRetryInterval_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 20),
    _MsdpPeerConnectRetryInterval_Type()
)
msdpPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerConnectRetryInterval.setUnits("seconds")


class _MsdpPeerHoldTimeConfigured_Type(Integer32):
    """Custom type msdpPeerHoldTimeConfigured based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_MsdpPeerHoldTimeConfigured_Type.__name__ = "Integer32"
_MsdpPeerHoldTimeConfigured_Object = MibTableColumn
msdpPeerHoldTimeConfigured = _MsdpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 21),
    _MsdpPeerHoldTimeConfigured_Type()
)
msdpPeerHoldTimeConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerHoldTimeConfigured.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerHoldTimeConfigured.setUnits("seconds")


class _MsdpPeerKeepAliveConfigured_Type(Integer32):
    """Custom type msdpPeerKeepAliveConfigured based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_MsdpPeerKeepAliveConfigured_Type.__name__ = "Integer32"
_MsdpPeerKeepAliveConfigured_Object = MibTableColumn
msdpPeerKeepAliveConfigured = _MsdpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 22),
    _MsdpPeerKeepAliveConfigured_Type()
)
msdpPeerKeepAliveConfigured.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerKeepAliveConfigured.setStatus("current")
if mibBuilder.loadTexts:
    msdpPeerKeepAliveConfigured.setUnits("seconds")


class _MsdpPeerDataTtl_Type(Integer32):
    """Custom type msdpPeerDataTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsdpPeerDataTtl_Type.__name__ = "Integer32"
_MsdpPeerDataTtl_Object = MibTableColumn
msdpPeerDataTtl = _MsdpPeerDataTtl_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 23),
    _MsdpPeerDataTtl_Type()
)
msdpPeerDataTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerDataTtl.setStatus("current")
_MsdpPeerProcessRequestsFrom_Type = TruthValue
_MsdpPeerProcessRequestsFrom_Object = MibTableColumn
msdpPeerProcessRequestsFrom = _MsdpPeerProcessRequestsFrom_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 24),
    _MsdpPeerProcessRequestsFrom_Type()
)
msdpPeerProcessRequestsFrom.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerProcessRequestsFrom.setStatus("current")
_MsdpPeerStatus_Type = RowStatus
_MsdpPeerStatus_Object = MibTableColumn
msdpPeerStatus = _MsdpPeerStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 25),
    _MsdpPeerStatus_Type()
)
msdpPeerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerStatus.setStatus("current")


class _MsdpPeerRemotePort_Type(Integer32):
    """Custom type msdpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsdpPeerRemotePort_Type.__name__ = "Integer32"
_MsdpPeerRemotePort_Object = MibTableColumn
msdpPeerRemotePort = _MsdpPeerRemotePort_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 26),
    _MsdpPeerRemotePort_Type()
)
msdpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerRemotePort.setStatus("current")


class _MsdpPeerLocalPort_Type(Integer32):
    """Custom type msdpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsdpPeerLocalPort_Type.__name__ = "Integer32"
_MsdpPeerLocalPort_Object = MibTableColumn
msdpPeerLocalPort = _MsdpPeerLocalPort_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 27),
    _MsdpPeerLocalPort_Type()
)
msdpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerLocalPort.setStatus("current")


class _MsdpPeerEncapsulationState_Type(Integer32):
    """Custom type msdpPeerEncapsulationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("advertising", 3),
          ("agreed", 5),
          ("default", 1),
          ("failed", 6),
          ("received", 2),
          ("sent", 4))
    )


_MsdpPeerEncapsulationState_Type.__name__ = "Integer32"
_MsdpPeerEncapsulationState_Object = MibTableColumn
msdpPeerEncapsulationState = _MsdpPeerEncapsulationState_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 28),
    _MsdpPeerEncapsulationState_Type()
)
msdpPeerEncapsulationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerEncapsulationState.setStatus("current")


class _MsdpPeerEncapsulationType_Type(Integer32):
    """Custom type msdpPeerEncapsulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gre", 3),
          ("tcp", 1),
          ("udp", 2))
    )


_MsdpPeerEncapsulationType_Type.__name__ = "Integer32"
_MsdpPeerEncapsulationType_Object = MibTableColumn
msdpPeerEncapsulationType = _MsdpPeerEncapsulationType_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 29),
    _MsdpPeerEncapsulationType_Type()
)
msdpPeerEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerEncapsulationType.setStatus("current")
_MsdpPeerConnectionAttempts_Type = Counter32
_MsdpPeerConnectionAttempts_Object = MibTableColumn
msdpPeerConnectionAttempts = _MsdpPeerConnectionAttempts_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 30),
    _MsdpPeerConnectionAttempts_Type()
)
msdpPeerConnectionAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerConnectionAttempts.setStatus("current")
_MsdpPeerInNotifications_Type = Counter32
_MsdpPeerInNotifications_Object = MibTableColumn
msdpPeerInNotifications = _MsdpPeerInNotifications_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 31),
    _MsdpPeerInNotifications_Type()
)
msdpPeerInNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInNotifications.setStatus("current")
_MsdpPeerOutNotifications_Type = Counter32
_MsdpPeerOutNotifications_Object = MibTableColumn
msdpPeerOutNotifications = _MsdpPeerOutNotifications_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 32),
    _MsdpPeerOutNotifications_Type()
)
msdpPeerOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutNotifications.setStatus("current")


class _MsdpPeerLastError_Type(OctetString):
    """Custom type msdpPeerLastError based on OctetString"""
    defaultHexValue = "0000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MsdpPeerLastError_Type.__name__ = "OctetString"
_MsdpPeerLastError_Object = MibTableColumn
msdpPeerLastError = _MsdpPeerLastError_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 33),
    _MsdpPeerLastError_Type()
)
msdpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerLastError.setStatus("current")
_MsdpSACacheTable_Object = MibTable
msdpSACacheTable = _MsdpSACacheTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6)
)
if mibBuilder.loadTexts:
    msdpSACacheTable.setStatus("current")
_MsdpSACacheEntry_Object = MibTableRow
msdpSACacheEntry = _MsdpSACacheEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1)
)
msdpSACacheEntry.setIndexNames(
    (0, "DRAFT-MSDP-MIB", "msdpSACacheGroupAddr"),
    (0, "DRAFT-MSDP-MIB", "msdpSACacheSourceAddr"),
    (0, "DRAFT-MSDP-MIB", "msdpSACacheOriginRP"),
)
if mibBuilder.loadTexts:
    msdpSACacheEntry.setStatus("current")
_MsdpSACacheGroupAddr_Type = IpAddress
_MsdpSACacheGroupAddr_Object = MibTableColumn
msdpSACacheGroupAddr = _MsdpSACacheGroupAddr_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 1),
    _MsdpSACacheGroupAddr_Type()
)
msdpSACacheGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheGroupAddr.setStatus("current")
_MsdpSACacheSourceAddr_Type = IpAddress
_MsdpSACacheSourceAddr_Object = MibTableColumn
msdpSACacheSourceAddr = _MsdpSACacheSourceAddr_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 2),
    _MsdpSACacheSourceAddr_Type()
)
msdpSACacheSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheSourceAddr.setStatus("current")
_MsdpSACacheOriginRP_Type = IpAddress
_MsdpSACacheOriginRP_Object = MibTableColumn
msdpSACacheOriginRP = _MsdpSACacheOriginRP_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 3),
    _MsdpSACacheOriginRP_Type()
)
msdpSACacheOriginRP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpSACacheOriginRP.setStatus("current")
_MsdpSACachePeerLearnedFrom_Type = IpAddress
_MsdpSACachePeerLearnedFrom_Object = MibTableColumn
msdpSACachePeerLearnedFrom = _MsdpSACachePeerLearnedFrom_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 4),
    _MsdpSACachePeerLearnedFrom_Type()
)
msdpSACachePeerLearnedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACachePeerLearnedFrom.setStatus("current")
_MsdpSACacheRPFPeer_Type = IpAddress
_MsdpSACacheRPFPeer_Object = MibTableColumn
msdpSACacheRPFPeer = _MsdpSACacheRPFPeer_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 5),
    _MsdpSACacheRPFPeer_Type()
)
msdpSACacheRPFPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheRPFPeer.setStatus("current")
_MsdpSACacheInSAs_Type = Counter32
_MsdpSACacheInSAs_Object = MibTableColumn
msdpSACacheInSAs = _MsdpSACacheInSAs_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 6),
    _MsdpSACacheInSAs_Type()
)
msdpSACacheInSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheInSAs.setStatus("current")
_MsdpSACacheInDataPackets_Type = Counter32
_MsdpSACacheInDataPackets_Object = MibTableColumn
msdpSACacheInDataPackets = _MsdpSACacheInDataPackets_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 7),
    _MsdpSACacheInDataPackets_Type()
)
msdpSACacheInDataPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheInDataPackets.setStatus("current")
_MsdpSACacheUpTime_Type = TimeTicks
_MsdpSACacheUpTime_Object = MibTableColumn
msdpSACacheUpTime = _MsdpSACacheUpTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 8),
    _MsdpSACacheUpTime_Type()
)
msdpSACacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheUpTime.setStatus("current")
_MsdpSACacheExpiryTime_Type = TimeTicks
_MsdpSACacheExpiryTime_Object = MibTableColumn
msdpSACacheExpiryTime = _MsdpSACacheExpiryTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 9),
    _MsdpSACacheExpiryTime_Type()
)
msdpSACacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSACacheExpiryTime.setStatus("current")
_MsdpSACacheStatus_Type = RowStatus
_MsdpSACacheStatus_Object = MibTableColumn
msdpSACacheStatus = _MsdpSACacheStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 10),
    _MsdpSACacheStatus_Type()
)
msdpSACacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpSACacheStatus.setStatus("current")
_MsdpTraps_ObjectIdentity = ObjectIdentity
msdpTraps = _MsdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 1, 7)
)
_MsdpMIBConformance_ObjectIdentity = ObjectIdentity
msdpMIBConformance = _MsdpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 1, 8)
)
_MsdpMIBCompliances_ObjectIdentity = ObjectIdentity
msdpMIBCompliances = _MsdpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 1)
)
_MsdpMIBGroups_ObjectIdentity = ObjectIdentity
msdpMIBGroups = _MsdpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2)
)


class _MsdpSAHoldDownPeriod_Type(Integer32):
    """Custom type msdpSAHoldDownPeriod based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MsdpSAHoldDownPeriod_Type.__name__ = "Integer32"
_MsdpSAHoldDownPeriod_Object = MibScalar
msdpSAHoldDownPeriod = _MsdpSAHoldDownPeriod_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 9),
    _MsdpSAHoldDownPeriod_Type()
)
msdpSAHoldDownPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpSAHoldDownPeriod.setStatus("current")
if mibBuilder.loadTexts:
    msdpSAHoldDownPeriod.setUnits("seconds")

# Managed Objects groups

msdpMIBGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 1)
)
msdpMIBGlobalsGroup.setObjects(
    ("DRAFT-MSDP-MIB", "msdpEnabled")
)
if mibBuilder.loadTexts:
    msdpMIBGlobalsGroup.setStatus("current")

msdpMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 2)
)
msdpMIBPeerGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpPeerRPFFailures"),
        ("DRAFT-MSDP-MIB", "msdpPeerState"),
        ("DRAFT-MSDP-MIB", "msdpPeerInSAs"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutSAs"),
        ("DRAFT-MSDP-MIB", "msdpPeerInSARequests"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutSARequests"),
        ("DRAFT-MSDP-MIB", "msdpPeerInSAResponses"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutSAResponses"),
        ("DRAFT-MSDP-MIB", "msdpPeerInNotifications"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutNotifications"),
        ("DRAFT-MSDP-MIB", "msdpPeerInControlMessages"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutControlMessages"),
        ("DRAFT-MSDP-MIB", "msdpPeerInDataPackets"),
        ("DRAFT-MSDP-MIB", "msdpPeerOutDataPackets"),
        ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTransitions"),
        ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTime"),
        ("DRAFT-MSDP-MIB", "msdpPeerLocalAddress"),
        ("DRAFT-MSDP-MIB", "msdpPeerRemotePort"),
        ("DRAFT-MSDP-MIB", "msdpPeerLocalPort"),
        ("DRAFT-MSDP-MIB", "msdpPeerSAAdvPeriod"),
        ("DRAFT-MSDP-MIB", "msdpPeerConnectRetryInterval"),
        ("DRAFT-MSDP-MIB", "msdpPeerHoldTimeConfigured"),
        ("DRAFT-MSDP-MIB", "msdpPeerKeepAliveConfigured"),
        ("DRAFT-MSDP-MIB", "msdpPeerInMessageElapsedTime"),
        ("DRAFT-MSDP-MIB", "msdpPeerDataTtl"),
        ("DRAFT-MSDP-MIB", "msdpPeerProcessRequestsFrom"),
        ("DRAFT-MSDP-MIB", "msdpPeerEncapsulationState"),
        ("DRAFT-MSDP-MIB", "msdpPeerEncapsulationType"),
        ("DRAFT-MSDP-MIB", "msdpPeerConnectionAttempts"),
        ("DRAFT-MSDP-MIB", "msdpPeerLastError"),
        ("DRAFT-MSDP-MIB", "msdpPeerStatus"))
)
if mibBuilder.loadTexts:
    msdpMIBPeerGroup.setStatus("current")

msdpSACacheGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 3)
)
msdpSACacheGroup.setObjects(
      *(("DRAFT-MSDP-MIB", "msdpCacheLifetime"),
        ("DRAFT-MSDP-MIB", "msdpNumSACacheEntries"),
        ("DRAFT-MSDP-MIB", "msdpSAHoldDownPeriod"),
        ("DRAFT-MSDP-MIB", "msdpSACachePeerLearnedFrom"),
        ("DRAFT-MSDP-MIB", "msdpSACacheRPFPeer"),
        ("DRAFT-MSDP-MIB", "msdpSACacheInSAs"),
        ("DRAFT-MSDP-MIB", "msdpSACacheInDataPackets"),
        ("DRAFT-MSDP-MIB", "msdpSACacheUpTime"),
        ("DRAFT-MSDP-MIB", "msdpSACacheExpiryTime"),
        ("DRAFT-MSDP-MIB", "msdpSACacheStatus"))
)
if mibBuilder.loadTexts:
    msdpSACacheGroup.setStatus("current")


# Notification objects

msdpEstablished = NotificationType(
    (1, 3, 6, 1, 3, 92, 1, 1, 7, 1)
)
msdpEstablished.setObjects(
    ("DRAFT-MSDP-MIB", "msdpPeerFsmEstablishedTransitions")
)
if mibBuilder.loadTexts:
    msdpEstablished.setStatus(
        "current"
    )

msdpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 3, 92, 1, 1, 7, 2)
)
msdpBackwardTransition.setObjects(
    ("DRAFT-MSDP-MIB", "msdpPeerState")
)
if mibBuilder.loadTexts:
    msdpBackwardTransition.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

msdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    msdpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DRAFT-MSDP-MIB",
    **{"msdpMIB": msdpMIB,
       "msdpMIBobjects": msdpMIBobjects,
       "msdp": msdp,
       "msdpEnabled": msdpEnabled,
       "msdpCacheLifetime": msdpCacheLifetime,
       "msdpNumSACacheEntries": msdpNumSACacheEntries,
       "msdpRequestsTable": msdpRequestsTable,
       "msdpRequestsEntry": msdpRequestsEntry,
       "msdpRequestsGroupAddress": msdpRequestsGroupAddress,
       "msdpRequestsGroupMask": msdpRequestsGroupMask,
       "msdpRequestsPeer": msdpRequestsPeer,
       "msdpRequestsStatus": msdpRequestsStatus,
       "msdpPeerTable": msdpPeerTable,
       "msdpPeerEntry": msdpPeerEntry,
       "msdpPeerRemoteAddress": msdpPeerRemoteAddress,
       "msdpPeerState": msdpPeerState,
       "msdpPeerRPFFailures": msdpPeerRPFFailures,
       "msdpPeerInSAs": msdpPeerInSAs,
       "msdpPeerOutSAs": msdpPeerOutSAs,
       "msdpPeerInSARequests": msdpPeerInSARequests,
       "msdpPeerOutSARequests": msdpPeerOutSARequests,
       "msdpPeerInSAResponses": msdpPeerInSAResponses,
       "msdpPeerOutSAResponses": msdpPeerOutSAResponses,
       "msdpPeerInControlMessages": msdpPeerInControlMessages,
       "msdpPeerOutControlMessages": msdpPeerOutControlMessages,
       "msdpPeerInDataPackets": msdpPeerInDataPackets,
       "msdpPeerOutDataPackets": msdpPeerOutDataPackets,
       "msdpPeerFsmEstablishedTransitions": msdpPeerFsmEstablishedTransitions,
       "msdpPeerFsmEstablishedTime": msdpPeerFsmEstablishedTime,
       "msdpPeerInMessageElapsedTime": msdpPeerInMessageElapsedTime,
       "msdpPeerLocalAddress": msdpPeerLocalAddress,
       "msdpPeerSAAdvPeriod": msdpPeerSAAdvPeriod,
       "msdpPeerConnectRetryInterval": msdpPeerConnectRetryInterval,
       "msdpPeerHoldTimeConfigured": msdpPeerHoldTimeConfigured,
       "msdpPeerKeepAliveConfigured": msdpPeerKeepAliveConfigured,
       "msdpPeerDataTtl": msdpPeerDataTtl,
       "msdpPeerProcessRequestsFrom": msdpPeerProcessRequestsFrom,
       "msdpPeerStatus": msdpPeerStatus,
       "msdpPeerRemotePort": msdpPeerRemotePort,
       "msdpPeerLocalPort": msdpPeerLocalPort,
       "msdpPeerEncapsulationState": msdpPeerEncapsulationState,
       "msdpPeerEncapsulationType": msdpPeerEncapsulationType,
       "msdpPeerConnectionAttempts": msdpPeerConnectionAttempts,
       "msdpPeerInNotifications": msdpPeerInNotifications,
       "msdpPeerOutNotifications": msdpPeerOutNotifications,
       "msdpPeerLastError": msdpPeerLastError,
       "msdpSACacheTable": msdpSACacheTable,
       "msdpSACacheEntry": msdpSACacheEntry,
       "msdpSACacheGroupAddr": msdpSACacheGroupAddr,
       "msdpSACacheSourceAddr": msdpSACacheSourceAddr,
       "msdpSACacheOriginRP": msdpSACacheOriginRP,
       "msdpSACachePeerLearnedFrom": msdpSACachePeerLearnedFrom,
       "msdpSACacheRPFPeer": msdpSACacheRPFPeer,
       "msdpSACacheInSAs": msdpSACacheInSAs,
       "msdpSACacheInDataPackets": msdpSACacheInDataPackets,
       "msdpSACacheUpTime": msdpSACacheUpTime,
       "msdpSACacheExpiryTime": msdpSACacheExpiryTime,
       "msdpSACacheStatus": msdpSACacheStatus,
       "msdpTraps": msdpTraps,
       "msdpEstablished": msdpEstablished,
       "msdpBackwardTransition": msdpBackwardTransition,
       "msdpMIBConformance": msdpMIBConformance,
       "msdpMIBCompliances": msdpMIBCompliances,
       "msdpMIBCompliance": msdpMIBCompliance,
       "msdpMIBGroups": msdpMIBGroups,
       "msdpMIBGlobalsGroup": msdpMIBGlobalsGroup,
       "msdpMIBPeerGroup": msdpMIBPeerGroup,
       "msdpSACacheGroup": msdpSACacheGroup,
       "msdpSAHoldDownPeriod": msdpSAHoldDownPeriod}
)
