# SNMP MIB module (ACC-MSP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-MSP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:35 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccMsp_ObjectIdentity = ObjectIdentity
accMsp = _AccMsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76)
)
_AccMspGeneralScalars_ObjectIdentity = ObjectIdentity
accMspGeneralScalars = _AccMspGeneralScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1)
)


class _AccMspAdminState_Type(Integer32):
    """Custom type accMspAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_AccMspAdminState_Type.__name__ = "Integer32"
_AccMspAdminState_Object = MibScalar
accMspAdminState = _AccMspAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 1),
    _AccMspAdminState_Type()
)
accMspAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspAdminState.setStatus("mandatory")


class _AccMspMode_Type(Integer32):
    """Custom type accMspMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 2),
          ("wait", 1))
    )


_AccMspMode_Type.__name__ = "Integer32"
_AccMspMode_Object = MibScalar
accMspMode = _AccMspMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 2),
    _AccMspMode_Type()
)
accMspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspMode.setStatus("mandatory")


class _AccMspDelivery_Type(Integer32):
    """Custom type accMspDelivery based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("limited-broadcast", 2),
          ("multicast", 1))
    )


_AccMspDelivery_Type.__name__ = "Integer32"
_AccMspDelivery_Object = MibScalar
accMspDelivery = _AccMspDelivery_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 3),
    _AccMspDelivery_Type()
)
accMspDelivery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspDelivery.setStatus("mandatory")


class _AccMspGroupId_Type(Integer32):
    """Custom type accMspGroupId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )


_AccMspGroupId_Type.__name__ = "Integer32"
_AccMspGroupId_Object = MibScalar
accMspGroupId = _AccMspGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 4),
    _AccMspGroupId_Type()
)
accMspGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspGroupId.setStatus("mandatory")


class _AccMspInterfaceAddress_Type(IpAddress):
    """Custom type accMspInterfaceAddress based on IpAddress"""
    defaultValue = 0


_AccMspInterfaceAddress_Object = MibScalar
accMspInterfaceAddress = _AccMspInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 5),
    _AccMspInterfaceAddress_Type()
)
accMspInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspInterfaceAddress.setStatus("mandatory")


class _AccMspUdpPort_Type(Integer32):
    """Custom type accMspUdpPort based on Integer32"""
    defaultValue = 2748

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccMspUdpPort_Type.__name__ = "Integer32"
_AccMspUdpPort_Object = MibScalar
accMspUdpPort = _AccMspUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 6),
    _AccMspUdpPort_Type()
)
accMspUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspUdpPort.setStatus("mandatory")


class _AccMspMaximumTimeout_Type(Integer32):
    """Custom type accMspMaximumTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100000),
    )


_AccMspMaximumTimeout_Type.__name__ = "Integer32"
_AccMspMaximumTimeout_Object = MibScalar
accMspMaximumTimeout = _AccMspMaximumTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 7),
    _AccMspMaximumTimeout_Type()
)
accMspMaximumTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspMaximumTimeout.setStatus("mandatory")


class _AccMspMaximumRetransmissions_Type(Integer32):
    """Custom type accMspMaximumRetransmissions based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AccMspMaximumRetransmissions_Type.__name__ = "Integer32"
_AccMspMaximumRetransmissions_Object = MibScalar
accMspMaximumRetransmissions = _AccMspMaximumRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 8),
    _AccMspMaximumRetransmissions_Type()
)
accMspMaximumRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspMaximumRetransmissions.setStatus("mandatory")


class _AccMspMaximumHistorySize_Type(Integer32):
    """Custom type accMspMaximumHistorySize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_AccMspMaximumHistorySize_Type.__name__ = "Integer32"
_AccMspMaximumHistorySize_Object = MibScalar
accMspMaximumHistorySize = _AccMspMaximumHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 9),
    _AccMspMaximumHistorySize_Type()
)
accMspMaximumHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspMaximumHistorySize.setStatus("mandatory")


class _AccMspMessageLevel_Type(Integer32):
    """Custom type accMspMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccMspMessageLevel_Type.__name__ = "Integer32"
_AccMspMessageLevel_Object = MibScalar
accMspMessageLevel = _AccMspMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 10),
    _AccMspMessageLevel_Type()
)
accMspMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspMessageLevel.setStatus("mandatory")


class _AccMspDebugMask_Type(Integer32):
    """Custom type accMspDebugMask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccMspDebugMask_Type.__name__ = "Integer32"
_AccMspDebugMask_Object = MibScalar
accMspDebugMask = _AccMspDebugMask_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 11),
    _AccMspDebugMask_Type()
)
accMspDebugMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMspDebugMask.setStatus("mandatory")
_AccMspStatInPackets_Type = Counter32
_AccMspStatInPackets_Object = MibScalar
accMspStatInPackets = _AccMspStatInPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 12),
    _AccMspStatInPackets_Type()
)
accMspStatInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatInPackets.setStatus("mandatory")
_AccMspStatOutPackets_Type = Counter32
_AccMspStatOutPackets_Object = MibScalar
accMspStatOutPackets = _AccMspStatOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 13),
    _AccMspStatOutPackets_Type()
)
accMspStatOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatOutPackets.setStatus("mandatory")
_AccMspStatInQueries_Type = Counter32
_AccMspStatInQueries_Object = MibScalar
accMspStatInQueries = _AccMspStatInQueries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 14),
    _AccMspStatInQueries_Type()
)
accMspStatInQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatInQueries.setStatus("mandatory")
_AccMspStatOutQueries_Type = Counter32
_AccMspStatOutQueries_Object = MibScalar
accMspStatOutQueries = _AccMspStatOutQueries_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 15),
    _AccMspStatOutQueries_Type()
)
accMspStatOutQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatOutQueries.setStatus("mandatory")
_AccMspStatInAcks_Type = Counter32
_AccMspStatInAcks_Object = MibScalar
accMspStatInAcks = _AccMspStatInAcks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 16),
    _AccMspStatInAcks_Type()
)
accMspStatInAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatInAcks.setStatus("mandatory")
_AccMspStatOutAcks_Type = Counter32
_AccMspStatOutAcks_Object = MibScalar
accMspStatOutAcks = _AccMspStatOutAcks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 17),
    _AccMspStatOutAcks_Type()
)
accMspStatOutAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatOutAcks.setStatus("mandatory")
_AccMspStatInRequests_Type = Counter32
_AccMspStatInRequests_Object = MibScalar
accMspStatInRequests = _AccMspStatInRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 18),
    _AccMspStatInRequests_Type()
)
accMspStatInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatInRequests.setStatus("mandatory")
_AccMspStatOutRequests_Type = Counter32
_AccMspStatOutRequests_Object = MibScalar
accMspStatOutRequests = _AccMspStatOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 19),
    _AccMspStatOutRequests_Type()
)
accMspStatOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatOutRequests.setStatus("mandatory")
_AccMspStatInDiscards_Type = Counter32
_AccMspStatInDiscards_Object = MibScalar
accMspStatInDiscards = _AccMspStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 20),
    _AccMspStatInDiscards_Type()
)
accMspStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatInDiscards.setStatus("mandatory")
_AccMspStatProcessingErrors_Type = Counter32
_AccMspStatProcessingErrors_Object = MibScalar
accMspStatProcessingErrors = _AccMspStatProcessingErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 21),
    _AccMspStatProcessingErrors_Type()
)
accMspStatProcessingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatProcessingErrors.setStatus("mandatory")
_AccMspStatNotForMes_Type = Counter32
_AccMspStatNotForMes_Object = MibScalar
accMspStatNotForMes = _AccMspStatNotForMes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 22),
    _AccMspStatNotForMes_Type()
)
accMspStatNotForMes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatNotForMes.setStatus("mandatory")
_AccMspStatProtocolErrors_Type = Counter32
_AccMspStatProtocolErrors_Object = MibScalar
accMspStatProtocolErrors = _AccMspStatProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 23),
    _AccMspStatProtocolErrors_Type()
)
accMspStatProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatProtocolErrors.setStatus("mandatory")
_AccMspStatInQueryPiggys_Type = Counter32
_AccMspStatInQueryPiggys_Object = MibScalar
accMspStatInQueryPiggys = _AccMspStatInQueryPiggys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 24),
    _AccMspStatInQueryPiggys_Type()
)
accMspStatInQueryPiggys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatInQueryPiggys.setStatus("mandatory")
_AccMspStatOutQueryPiggys_Type = Counter32
_AccMspStatOutQueryPiggys_Object = MibScalar
accMspStatOutQueryPiggys = _AccMspStatOutQueryPiggys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 25),
    _AccMspStatOutQueryPiggys_Type()
)
accMspStatOutQueryPiggys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatOutQueryPiggys.setStatus("mandatory")
_AccMspStatInAckPiggys_Type = Counter32
_AccMspStatInAckPiggys_Object = MibScalar
accMspStatInAckPiggys = _AccMspStatInAckPiggys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 26),
    _AccMspStatInAckPiggys_Type()
)
accMspStatInAckPiggys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatInAckPiggys.setStatus("mandatory")
_AccMspStatOutAckPiggys_Type = Counter32
_AccMspStatOutAckPiggys_Object = MibScalar
accMspStatOutAckPiggys = _AccMspStatOutAckPiggys_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 27),
    _AccMspStatOutAckPiggys_Type()
)
accMspStatOutAckPiggys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatOutAckPiggys.setStatus("mandatory")
_AccMspStatQueryTimeouts_Type = Counter32
_AccMspStatQueryTimeouts_Object = MibScalar
accMspStatQueryTimeouts = _AccMspStatQueryTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 28),
    _AccMspStatQueryTimeouts_Type()
)
accMspStatQueryTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatQueryTimeouts.setStatus("mandatory")
_AccMspStatMemoryFails_Type = Counter32
_AccMspStatMemoryFails_Object = MibScalar
accMspStatMemoryFails = _AccMspStatMemoryFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 29),
    _AccMspStatMemoryFails_Type()
)
accMspStatMemoryFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatMemoryFails.setStatus("mandatory")
_AccMspStatAverageQueryClosure_Type = Gauge32
_AccMspStatAverageQueryClosure_Object = MibScalar
accMspStatAverageQueryClosure = _AccMspStatAverageQueryClosure_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 30),
    _AccMspStatAverageQueryClosure_Type()
)
accMspStatAverageQueryClosure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatAverageQueryClosure.setStatus("mandatory")
_AccMspStatCurrentTimeout_Type = Gauge32
_AccMspStatCurrentTimeout_Object = MibScalar
accMspStatCurrentTimeout = _AccMspStatCurrentTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 1, 31),
    _AccMspStatCurrentTimeout_Type()
)
accMspStatCurrentTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspStatCurrentTimeout.setStatus("mandatory")
_AccMspNeighbor_ObjectIdentity = ObjectIdentity
accMspNeighbor = _AccMspNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2)
)
_AccMspNeighborTable_Object = MibTable
accMspNeighborTable = _AccMspNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1)
)
if mibBuilder.loadTexts:
    accMspNeighborTable.setStatus("mandatory")
_AccMspNeighborEntry_Object = MibTableRow
accMspNeighborEntry = _AccMspNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1, 1)
)
accMspNeighborEntry.setIndexNames(
    (0, "ACC-MSP", "accMspNeighborAddress"),
)
if mibBuilder.loadTexts:
    accMspNeighborEntry.setStatus("mandatory")
_AccMspNeighborAddress_Type = IpAddress
_AccMspNeighborAddress_Object = MibTableColumn
accMspNeighborAddress = _AccMspNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1, 1, 1),
    _AccMspNeighborAddress_Type()
)
accMspNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspNeighborAddress.setStatus("mandatory")
_AccMspNeighborIDs_Type = Counter32
_AccMspNeighborIDs_Object = MibTableColumn
accMspNeighborIDs = _AccMspNeighborIDs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1, 1, 2),
    _AccMspNeighborIDs_Type()
)
accMspNeighborIDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspNeighborIDs.setStatus("mandatory")
_AccMspNeighborVersions_Type = Counter32
_AccMspNeighborVersions_Object = MibTableColumn
accMspNeighborVersions = _AccMspNeighborVersions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1, 1, 3),
    _AccMspNeighborVersions_Type()
)
accMspNeighborVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspNeighborVersions.setStatus("mandatory")
_AccMspNeighborStates_Type = Counter32
_AccMspNeighborStates_Object = MibTableColumn
accMspNeighborStates = _AccMspNeighborStates_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1, 1, 4),
    _AccMspNeighborStates_Type()
)
accMspNeighborStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspNeighborStates.setStatus("mandatory")
_AccMspNeighborAckTimeOuts_Type = Counter32
_AccMspNeighborAckTimeOuts_Object = MibTableColumn
accMspNeighborAckTimeOuts = _AccMspNeighborAckTimeOuts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1, 1, 5),
    _AccMspNeighborAckTimeOuts_Type()
)
accMspNeighborAckTimeOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspNeighborAckTimeOuts.setStatus("mandatory")
_AccMspNeighborRetransmissions_Type = Counter32
_AccMspNeighborRetransmissions_Object = MibTableColumn
accMspNeighborRetransmissions = _AccMspNeighborRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 2, 1, 1, 6),
    _AccMspNeighborRetransmissions_Type()
)
accMspNeighborRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspNeighborRetransmissions.setStatus("mandatory")
_AccMspTraps_ObjectIdentity = ObjectIdentity
accMspTraps = _AccMspTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 3)
)
_AccMspTrapMsg_Type = DisplayString
_AccMspTrapMsg_Object = MibScalar
accMspTrapMsg = _AccMspTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 3, 1),
    _AccMspTrapMsg_Type()
)
accMspTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMspTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accMspIpBindTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 3, 0, 1)
)
accMspIpBindTrap.setObjects(
      *(("ACC-MSP", "accMspTrapMsg"),
        ("ACC-MSP", "accMspInterfaceAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accMspIpBindTrap.setStatus(
        ""
    )

accMspInvIntfAddrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 3, 0, 2)
)
accMspInvIntfAddrTrap.setObjects(
      *(("ACC-MSP", "accMspTrapMsg"),
        ("ACC-MSP", "accMspInterfaceAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accMspInvIntfAddrTrap.setStatus(
        ""
    )

accMspShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 76, 3, 0, 3)
)
accMspShutdownTrap.setObjects(
      *(("ACC-MSP", "accMspTrapMsg"),
        ("ACC-MSP", "accMspNeighborAddress"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accMspShutdownTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-MSP",
    **{"accMsp": accMsp,
       "accMspGeneralScalars": accMspGeneralScalars,
       "accMspAdminState": accMspAdminState,
       "accMspMode": accMspMode,
       "accMspDelivery": accMspDelivery,
       "accMspGroupId": accMspGroupId,
       "accMspInterfaceAddress": accMspInterfaceAddress,
       "accMspUdpPort": accMspUdpPort,
       "accMspMaximumTimeout": accMspMaximumTimeout,
       "accMspMaximumRetransmissions": accMspMaximumRetransmissions,
       "accMspMaximumHistorySize": accMspMaximumHistorySize,
       "accMspMessageLevel": accMspMessageLevel,
       "accMspDebugMask": accMspDebugMask,
       "accMspStatInPackets": accMspStatInPackets,
       "accMspStatOutPackets": accMspStatOutPackets,
       "accMspStatInQueries": accMspStatInQueries,
       "accMspStatOutQueries": accMspStatOutQueries,
       "accMspStatInAcks": accMspStatInAcks,
       "accMspStatOutAcks": accMspStatOutAcks,
       "accMspStatInRequests": accMspStatInRequests,
       "accMspStatOutRequests": accMspStatOutRequests,
       "accMspStatInDiscards": accMspStatInDiscards,
       "accMspStatProcessingErrors": accMspStatProcessingErrors,
       "accMspStatNotForMes": accMspStatNotForMes,
       "accMspStatProtocolErrors": accMspStatProtocolErrors,
       "accMspStatInQueryPiggys": accMspStatInQueryPiggys,
       "accMspStatOutQueryPiggys": accMspStatOutQueryPiggys,
       "accMspStatInAckPiggys": accMspStatInAckPiggys,
       "accMspStatOutAckPiggys": accMspStatOutAckPiggys,
       "accMspStatQueryTimeouts": accMspStatQueryTimeouts,
       "accMspStatMemoryFails": accMspStatMemoryFails,
       "accMspStatAverageQueryClosure": accMspStatAverageQueryClosure,
       "accMspStatCurrentTimeout": accMspStatCurrentTimeout,
       "accMspNeighbor": accMspNeighbor,
       "accMspNeighborTable": accMspNeighborTable,
       "accMspNeighborEntry": accMspNeighborEntry,
       "accMspNeighborAddress": accMspNeighborAddress,
       "accMspNeighborIDs": accMspNeighborIDs,
       "accMspNeighborVersions": accMspNeighborVersions,
       "accMspNeighborStates": accMspNeighborStates,
       "accMspNeighborAckTimeOuts": accMspNeighborAckTimeOuts,
       "accMspNeighborRetransmissions": accMspNeighborRetransmissions,
       "accMspTraps": accMspTraps,
       "accMspIpBindTrap": accMspIpBindTrap,
       "accMspInvIntfAddrTrap": accMspInvIntfAddrTrap,
       "accMspShutdownTrap": accMspShutdownTrap,
       "accMspTrapMsg": accMspTrapMsg}
)
