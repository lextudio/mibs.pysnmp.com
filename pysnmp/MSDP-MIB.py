# SNMP MIB module (MSDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:54 2024
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

msdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 92)
)
msdpMIB.setRevisions(
        ("2006-08-01 00:00",)
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
_MsdpTraps_ObjectIdentity = ObjectIdentity
msdpTraps = _MsdpTraps_ObjectIdentity(
    (1, 3, 6, 1, 3, 92, 1, 1, 0)
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
    msdpRequestsTable.setStatus("deprecated")
_MsdpRequestsEntry_Object = MibTableRow
msdpRequestsEntry = _MsdpRequestsEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1)
)
msdpRequestsEntry.setIndexNames(
    (0, "MSDP-MIB", "msdpRequestsGroupAddress"),
    (0, "MSDP-MIB", "msdpRequestsGroupMask"),
)
if mibBuilder.loadTexts:
    msdpRequestsEntry.setStatus("deprecated")
_MsdpRequestsGroupAddress_Type = IpAddress
_MsdpRequestsGroupAddress_Object = MibTableColumn
msdpRequestsGroupAddress = _MsdpRequestsGroupAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 1),
    _MsdpRequestsGroupAddress_Type()
)
msdpRequestsGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsGroupAddress.setStatus("deprecated")
_MsdpRequestsGroupMask_Type = IpAddress
_MsdpRequestsGroupMask_Object = MibTableColumn
msdpRequestsGroupMask = _MsdpRequestsGroupMask_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 2),
    _MsdpRequestsGroupMask_Type()
)
msdpRequestsGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpRequestsGroupMask.setStatus("deprecated")
_MsdpRequestsPeer_Type = IpAddress
_MsdpRequestsPeer_Object = MibTableColumn
msdpRequestsPeer = _MsdpRequestsPeer_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 3),
    _MsdpRequestsPeer_Type()
)
msdpRequestsPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpRequestsPeer.setStatus("deprecated")
_MsdpRequestsStatus_Type = RowStatus
_MsdpRequestsStatus_Object = MibTableColumn
msdpRequestsStatus = _MsdpRequestsStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 4, 1, 4),
    _MsdpRequestsStatus_Type()
)
msdpRequestsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpRequestsStatus.setStatus("deprecated")
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
    (0, "MSDP-MIB", "msdpPeerRemoteAddress"),
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
    msdpPeerInSAResponses.setStatus("deprecated")
_MsdpPeerOutSAResponses_Type = Counter32
_MsdpPeerOutSAResponses_Object = MibTableColumn
msdpPeerOutSAResponses = _MsdpPeerOutSAResponses_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 10),
    _MsdpPeerOutSAResponses_Type()
)
msdpPeerOutSAResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutSAResponses.setStatus("deprecated")
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
_MsdpPeerFsmEstablishedTime_Type = TimeStamp
_MsdpPeerFsmEstablishedTime_Object = MibTableColumn
msdpPeerFsmEstablishedTime = _MsdpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 16),
    _MsdpPeerFsmEstablishedTime_Type()
)
msdpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerFsmEstablishedTime.setStatus("current")
_MsdpPeerInMessageTime_Type = TimeStamp
_MsdpPeerInMessageTime_Object = MibTableColumn
msdpPeerInMessageTime = _MsdpPeerInMessageTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 17),
    _MsdpPeerInMessageTime_Type()
)
msdpPeerInMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerInMessageTime.setStatus("current")
_MsdpPeerLocalAddress_Type = IpAddress
_MsdpPeerLocalAddress_Object = MibTableColumn
msdpPeerLocalAddress = _MsdpPeerLocalAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 18),
    _MsdpPeerLocalAddress_Type()
)
msdpPeerLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpPeerLocalAddress.setStatus("current")


class _MsdpPeerConnectRetryInterval_Type(Integer32):
    """Custom type msdpPeerConnectRetryInterval based on Integer32"""
    defaultValue = 30

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
    defaultValue = 75

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
    defaultValue = 60

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
    defaultValue = 1

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
    msdpPeerProcessRequestsFrom.setStatus("deprecated")
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
    defaultValue = 639

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
    defaultValue = 639

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


class _MsdpPeerEncapsulationType_Type(Integer32):
    """Custom type msdpPeerEncapsulationType based on Integer32"""
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


_MsdpPeerEncapsulationType_Type.__name__ = "Integer32"
_MsdpPeerEncapsulationType_Object = MibTableColumn
msdpPeerEncapsulationType = _MsdpPeerEncapsulationType_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 29),
    _MsdpPeerEncapsulationType_Type()
)
msdpPeerEncapsulationType.setMaxAccess("read-create")
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
    msdpPeerInNotifications.setStatus("deprecated")
_MsdpPeerOutNotifications_Type = Counter32
_MsdpPeerOutNotifications_Object = MibTableColumn
msdpPeerOutNotifications = _MsdpPeerOutNotifications_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 32),
    _MsdpPeerOutNotifications_Type()
)
msdpPeerOutNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerOutNotifications.setStatus("deprecated")


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
    msdpPeerLastError.setStatus("deprecated")
_MsdpPeerDiscontinuityTime_Type = TimeStamp
_MsdpPeerDiscontinuityTime_Object = MibTableColumn
msdpPeerDiscontinuityTime = _MsdpPeerDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 5, 1, 34),
    _MsdpPeerDiscontinuityTime_Type()
)
msdpPeerDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msdpPeerDiscontinuityTime.setStatus("current")
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
    (0, "MSDP-MIB", "msdpSACacheGroupAddr"),
    (0, "MSDP-MIB", "msdpSACacheSourceAddr"),
    (0, "MSDP-MIB", "msdpSACacheOriginRP"),
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


class _MsdpSACacheStatus_Type(RowStatus):
    """Custom type msdpSACacheStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("destroy", 6))
    )


_MsdpSACacheStatus_Type.__name__ = "RowStatus"
_MsdpSACacheStatus_Object = MibTableColumn
msdpSACacheStatus = _MsdpSACacheStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 6, 1, 10),
    _MsdpSACacheStatus_Type()
)
msdpSACacheStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpSACacheStatus.setStatus("current")
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
_MsdpRPAddress_Type = IpAddress
_MsdpRPAddress_Object = MibScalar
msdpRPAddress = _MsdpRPAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 11),
    _MsdpRPAddress_Type()
)
msdpRPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msdpRPAddress.setStatus("current")
_MsdpMeshGroupTable_Object = MibTable
msdpMeshGroupTable = _MsdpMeshGroupTable_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 12)
)
if mibBuilder.loadTexts:
    msdpMeshGroupTable.setStatus("current")
_MsdpMeshGroupEntry_Object = MibTableRow
msdpMeshGroupEntry = _MsdpMeshGroupEntry_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 12, 1)
)
msdpMeshGroupEntry.setIndexNames(
    (0, "MSDP-MIB", "msdpMeshGroupName"),
    (0, "MSDP-MIB", "msdpMeshGroupPeerAddress"),
)
if mibBuilder.loadTexts:
    msdpMeshGroupEntry.setStatus("current")


class _MsdpMeshGroupName_Type(DisplayString):
    """Custom type msdpMeshGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_MsdpMeshGroupName_Type.__name__ = "DisplayString"
_MsdpMeshGroupName_Object = MibTableColumn
msdpMeshGroupName = _MsdpMeshGroupName_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 12, 1, 1),
    _MsdpMeshGroupName_Type()
)
msdpMeshGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpMeshGroupName.setStatus("current")
_MsdpMeshGroupPeerAddress_Type = IpAddress
_MsdpMeshGroupPeerAddress_Object = MibTableColumn
msdpMeshGroupPeerAddress = _MsdpMeshGroupPeerAddress_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 12, 1, 2),
    _MsdpMeshGroupPeerAddress_Type()
)
msdpMeshGroupPeerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msdpMeshGroupPeerAddress.setStatus("current")
_MsdpMeshGroupStatus_Type = RowStatus
_MsdpMeshGroupStatus_Object = MibTableColumn
msdpMeshGroupStatus = _MsdpMeshGroupStatus_Object(
    (1, 3, 6, 1, 3, 92, 1, 1, 12, 1, 3),
    _MsdpMeshGroupStatus_Type()
)
msdpMeshGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msdpMeshGroupStatus.setStatus("current")

# Managed Objects groups

msdpMIBGlobalsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 1)
)
msdpMIBGlobalsGroup.setObjects(
    ("MSDP-MIB", "msdpEnabled")
)
if mibBuilder.loadTexts:
    msdpMIBGlobalsGroup.setStatus("current")

msdpMIBPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 2)
)
msdpMIBPeerGroup.setObjects(
      *(("MSDP-MIB", "msdpPeerRPFFailures"),
        ("MSDP-MIB", "msdpPeerState"),
        ("MSDP-MIB", "msdpPeerInSAs"),
        ("MSDP-MIB", "msdpPeerOutSAs"),
        ("MSDP-MIB", "msdpPeerInSARequests"),
        ("MSDP-MIB", "msdpPeerOutSARequests"),
        ("MSDP-MIB", "msdpPeerInSAResponses"),
        ("MSDP-MIB", "msdpPeerOutSAResponses"),
        ("MSDP-MIB", "msdpPeerInNotifications"),
        ("MSDP-MIB", "msdpPeerOutNotifications"),
        ("MSDP-MIB", "msdpPeerInControlMessages"),
        ("MSDP-MIB", "msdpPeerOutControlMessages"),
        ("MSDP-MIB", "msdpPeerFsmEstablishedTransitions"),
        ("MSDP-MIB", "msdpPeerFsmEstablishedTime"),
        ("MSDP-MIB", "msdpPeerLocalAddress"),
        ("MSDP-MIB", "msdpPeerRemotePort"),
        ("MSDP-MIB", "msdpPeerLocalPort"),
        ("MSDP-MIB", "msdpPeerConnectRetryInterval"),
        ("MSDP-MIB", "msdpPeerHoldTimeConfigured"),
        ("MSDP-MIB", "msdpPeerKeepAliveConfigured"),
        ("MSDP-MIB", "msdpPeerInMessageTime"),
        ("MSDP-MIB", "msdpPeerProcessRequestsFrom"),
        ("MSDP-MIB", "msdpPeerConnectionAttempts"),
        ("MSDP-MIB", "msdpPeerLastError"),
        ("MSDP-MIB", "msdpPeerStatus"),
        ("MSDP-MIB", "msdpPeerDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    msdpMIBPeerGroup.setStatus("deprecated")

msdpMIBEncapsulationGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 3)
)
msdpMIBEncapsulationGroup.setObjects(
      *(("MSDP-MIB", "msdpPeerInDataPackets"),
        ("MSDP-MIB", "msdpPeerOutDataPackets"),
        ("MSDP-MIB", "msdpPeerDataTtl"),
        ("MSDP-MIB", "msdpPeerEncapsulationType"))
)
if mibBuilder.loadTexts:
    msdpMIBEncapsulationGroup.setStatus("current")

msdpMIBSACacheGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 4)
)
msdpMIBSACacheGroup.setObjects(
      *(("MSDP-MIB", "msdpCacheLifetime"),
        ("MSDP-MIB", "msdpNumSACacheEntries"),
        ("MSDP-MIB", "msdpSACachePeerLearnedFrom"),
        ("MSDP-MIB", "msdpSACacheRPFPeer"),
        ("MSDP-MIB", "msdpSACacheInSAs"),
        ("MSDP-MIB", "msdpSACacheInDataPackets"),
        ("MSDP-MIB", "msdpSACacheUpTime"),
        ("MSDP-MIB", "msdpSACacheExpiryTime"),
        ("MSDP-MIB", "msdpSACacheStatus"))
)
if mibBuilder.loadTexts:
    msdpMIBSACacheGroup.setStatus("current")

msdpMIBRequestsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 6)
)
msdpMIBRequestsGroup.setObjects(
      *(("MSDP-MIB", "msdpRequestsPeer"),
        ("MSDP-MIB", "msdpRequestsStatus"))
)
if mibBuilder.loadTexts:
    msdpMIBRequestsGroup.setStatus("deprecated")

msdpMIBRPGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 7)
)
msdpMIBRPGroup.setObjects(
    ("MSDP-MIB", "msdpRPAddress")
)
if mibBuilder.loadTexts:
    msdpMIBRPGroup.setStatus("current")

msdpMIBMeshGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 8)
)
msdpMIBMeshGroupGroup.setObjects(
    ("MSDP-MIB", "msdpMeshGroupStatus")
)
if mibBuilder.loadTexts:
    msdpMIBMeshGroupGroup.setStatus("current")

msdpMIBPeerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 9)
)
msdpMIBPeerGroup2.setObjects(
      *(("MSDP-MIB", "msdpPeerRPFFailures"),
        ("MSDP-MIB", "msdpPeerState"),
        ("MSDP-MIB", "msdpPeerInSAs"),
        ("MSDP-MIB", "msdpPeerOutSAs"),
        ("MSDP-MIB", "msdpPeerInSARequests"),
        ("MSDP-MIB", "msdpPeerOutSARequests"),
        ("MSDP-MIB", "msdpPeerInControlMessages"),
        ("MSDP-MIB", "msdpPeerOutControlMessages"),
        ("MSDP-MIB", "msdpPeerFsmEstablishedTransitions"),
        ("MSDP-MIB", "msdpPeerFsmEstablishedTime"),
        ("MSDP-MIB", "msdpPeerLocalAddress"),
        ("MSDP-MIB", "msdpPeerRemotePort"),
        ("MSDP-MIB", "msdpPeerLocalPort"),
        ("MSDP-MIB", "msdpPeerConnectRetryInterval"),
        ("MSDP-MIB", "msdpPeerHoldTimeConfigured"),
        ("MSDP-MIB", "msdpPeerKeepAliveConfigured"),
        ("MSDP-MIB", "msdpPeerInMessageTime"),
        ("MSDP-MIB", "msdpPeerConnectionAttempts"),
        ("MSDP-MIB", "msdpPeerStatus"),
        ("MSDP-MIB", "msdpPeerDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    msdpMIBPeerGroup2.setStatus("current")


# Notification objects

msdpEstablished = NotificationType(
    (1, 3, 6, 1, 3, 92, 1, 1, 0, 1)
)
msdpEstablished.setObjects(
    ("MSDP-MIB", "msdpPeerFsmEstablishedTransitions")
)
if mibBuilder.loadTexts:
    msdpEstablished.setStatus(
        "current"
    )

msdpBackwardTransition = NotificationType(
    (1, 3, 6, 1, 3, 92, 1, 1, 0, 2)
)
msdpBackwardTransition.setObjects(
    ("MSDP-MIB", "msdpPeerState")
)
if mibBuilder.loadTexts:
    msdpBackwardTransition.setStatus(
        "current"
    )


# Notifications groups

msdpMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 2, 5)
)
msdpMIBNotificationGroup.setObjects(
      *(("MSDP-MIB", "msdpEstablished"),
        ("MSDP-MIB", "msdpBackwardTransition"))
)
if mibBuilder.loadTexts:
    msdpMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

msdpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    msdpMIBCompliance.setStatus(
        "deprecated"
    )

msdpMIBFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 1, 2)
)
if mibBuilder.loadTexts:
    msdpMIBFullCompliance.setStatus(
        "current"
    )

msdpMIBReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 92, 1, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    msdpMIBReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSDP-MIB",
    **{"msdpMIB": msdpMIB,
       "msdpMIBobjects": msdpMIBobjects,
       "msdp": msdp,
       "msdpTraps": msdpTraps,
       "msdpEstablished": msdpEstablished,
       "msdpBackwardTransition": msdpBackwardTransition,
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
       "msdpPeerInMessageTime": msdpPeerInMessageTime,
       "msdpPeerLocalAddress": msdpPeerLocalAddress,
       "msdpPeerConnectRetryInterval": msdpPeerConnectRetryInterval,
       "msdpPeerHoldTimeConfigured": msdpPeerHoldTimeConfigured,
       "msdpPeerKeepAliveConfigured": msdpPeerKeepAliveConfigured,
       "msdpPeerDataTtl": msdpPeerDataTtl,
       "msdpPeerProcessRequestsFrom": msdpPeerProcessRequestsFrom,
       "msdpPeerStatus": msdpPeerStatus,
       "msdpPeerRemotePort": msdpPeerRemotePort,
       "msdpPeerLocalPort": msdpPeerLocalPort,
       "msdpPeerEncapsulationType": msdpPeerEncapsulationType,
       "msdpPeerConnectionAttempts": msdpPeerConnectionAttempts,
       "msdpPeerInNotifications": msdpPeerInNotifications,
       "msdpPeerOutNotifications": msdpPeerOutNotifications,
       "msdpPeerLastError": msdpPeerLastError,
       "msdpPeerDiscontinuityTime": msdpPeerDiscontinuityTime,
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
       "msdpMIBConformance": msdpMIBConformance,
       "msdpMIBCompliances": msdpMIBCompliances,
       "msdpMIBCompliance": msdpMIBCompliance,
       "msdpMIBFullCompliance": msdpMIBFullCompliance,
       "msdpMIBReadOnlyCompliance": msdpMIBReadOnlyCompliance,
       "msdpMIBGroups": msdpMIBGroups,
       "msdpMIBGlobalsGroup": msdpMIBGlobalsGroup,
       "msdpMIBPeerGroup": msdpMIBPeerGroup,
       "msdpMIBEncapsulationGroup": msdpMIBEncapsulationGroup,
       "msdpMIBSACacheGroup": msdpMIBSACacheGroup,
       "msdpMIBNotificationGroup": msdpMIBNotificationGroup,
       "msdpMIBRequestsGroup": msdpMIBRequestsGroup,
       "msdpMIBRPGroup": msdpMIBRPGroup,
       "msdpMIBMeshGroupGroup": msdpMIBMeshGroupGroup,
       "msdpMIBPeerGroup2": msdpMIBPeerGroup2,
       "msdpRPAddress": msdpRPAddress,
       "msdpMeshGroupTable": msdpMeshGroupTable,
       "msdpMeshGroupEntry": msdpMeshGroupEntry,
       "msdpMeshGroupName": msdpMeshGroupName,
       "msdpMeshGroupPeerAddress": msdpMeshGroupPeerAddress,
       "msdpMeshGroupStatus": msdpMeshGroupStatus}
)
