# SNMP MIB module (HM2-PLATFORM-MSRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-MSRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:16 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(hm2AgentDot1qMrpMxrp,) = mibBuilder.importSymbols(
    "HM2-PLATFORM-MRP-MIB",
    "hm2AgentDot1qMrpMxrp")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hm2PlatformMSRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3)
)
hm2PlatformMSRP.setRevisions(
        ("2013-04-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hm2AgentDot1qPriorityValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Hm2AgentDot1qMsrpStreamRankValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("nonEmergency", 1))
    )



class Hm2AgentDot1qMsrpStreamIdValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:1x:1x:1x:1x:1x.1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class Hm2AgentDot1qMsrpReservationDirectionValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("listenerRegistrations", 1),
          ("talkerRegistrations", 0))
    )



class Hm2AgentDot1qMsrpReservationDeclarationTypeValue(Integer32, TextualConvention):
    status = "current"
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
        *(("listenerAskingFailed", 2),
          ("listenerReady", 3),
          ("listenerReadyFailed", 4),
          ("talkerAdvertise", 0),
          ("talkerFailed", 1))
    )



class Hm2AgentDot1qMsrpReservationFailureCodeValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("cannotStoreDestinationAddress", 12),
          ("egressPortNotAVBCapable", 8),
          ("firstValueChangedForStreamID", 16),
          ("insufficientBandwidth", 1),
          ("insufficientResources", 2),
          ("insufficientTrafficClassBandwidth", 3),
          ("latencyHasChanged", 7),
          ("maxFanInPortsLimitReached", 15),
          ("maxFrameSizeTooLarge", 14),
          ("noFailure", 0),
          ("outOfMMRPResources", 11),
          ("outOfMSRPResources", 10),
          ("priorityIsNoAnSRCLass", 13),
          ("srClassPriorityMismatch", 19),
          ("streamDestinationAddressInUse", 5),
          ("streamIDInUse", 4),
          ("streamPreemptedByHigherRank", 6),
          ("useDifferentDestinationAddress", 9),
          ("vlanBlockedOnEgress", 17),
          ("vlanTaggingDisabledOnEgress", 18))
    )



class Hm2AgentDot1qFqtssTrafficClassValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class Hm2AgentDot1qFqtssDeltaBandwidthValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000000),
    )



class Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_Hm2AgentDot1qMsrp_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMsrp = _Hm2AgentDot1qMsrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1)
)
_Hm2AgentDot1qPortMsrpTable_Object = MibTable
hm2AgentDot1qPortMsrpTable = _Hm2AgentDot1qPortMsrpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMsrpTable.setStatus("current")
_Hm2AgentDot1qPortMsrpEntry_Object = MibTableRow
hm2AgentDot1qPortMsrpEntry = _Hm2AgentDot1qPortMsrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1)
)
hm2AgentDot1qPortMsrpEntry.setIndexNames(
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMsrpEntry.setStatus("current")


class _Hm2AgentDot1qMsrpPort_Type(Integer32):
    """Custom type hm2AgentDot1qMsrpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentDot1qMsrpPort_Type.__name__ = "Integer32"
_Hm2AgentDot1qMsrpPort_Object = MibTableColumn
hm2AgentDot1qMsrpPort = _Hm2AgentDot1qMsrpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 1),
    _Hm2AgentDot1qMsrpPort_Type()
)
hm2AgentDot1qMsrpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpPort.setStatus("current")


class _Hm2AgentDot1qPortMsrpEnabledStatus_Type(TruthValue):
    """Custom type hm2AgentDot1qPortMsrpEnabledStatus based on TruthValue"""


_Hm2AgentDot1qPortMsrpEnabledStatus_Object = MibTableColumn
hm2AgentDot1qPortMsrpEnabledStatus = _Hm2AgentDot1qPortMsrpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 2),
    _Hm2AgentDot1qPortMsrpEnabledStatus_Type()
)
hm2AgentDot1qPortMsrpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMsrpEnabledStatus.setStatus("current")
_Hm2AgentDot1qPortMsrpFailedRegistrations_Type = Counter64
_Hm2AgentDot1qPortMsrpFailedRegistrations_Object = MibTableColumn
hm2AgentDot1qPortMsrpFailedRegistrations = _Hm2AgentDot1qPortMsrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 3),
    _Hm2AgentDot1qPortMsrpFailedRegistrations_Type()
)
hm2AgentDot1qPortMsrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMsrpFailedRegistrations.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMsrpFailedRegistrations.setUnits("failed MSRP registrations")
_Hm2AgentDot1qPortMsrpLastPduOrigin_Type = MacAddress
_Hm2AgentDot1qPortMsrpLastPduOrigin_Object = MibTableColumn
hm2AgentDot1qPortMsrpLastPduOrigin = _Hm2AgentDot1qPortMsrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 4),
    _Hm2AgentDot1qPortMsrpLastPduOrigin_Type()
)
hm2AgentDot1qPortMsrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMsrpLastPduOrigin.setStatus("current")


class _Hm2AgentDot1qPortMsrpPvid_Type(VlanId):
    """Custom type hm2AgentDot1qPortMsrpPvid based on VlanId"""
    defaultValue = 2


_Hm2AgentDot1qPortMsrpPvid_Object = MibTableColumn
hm2AgentDot1qPortMsrpPvid = _Hm2AgentDot1qPortMsrpPvid_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 5),
    _Hm2AgentDot1qPortMsrpPvid_Type()
)
hm2AgentDot1qPortMsrpPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qPortMsrpPvid.setStatus("current")


class _Hm2AgentDot1qBridgeMsrpEnabledStatus_Type(TruthValue):
    """Custom type hm2AgentDot1qBridgeMsrpEnabledStatus based on TruthValue"""


_Hm2AgentDot1qBridgeMsrpEnabledStatus_Object = MibScalar
hm2AgentDot1qBridgeMsrpEnabledStatus = _Hm2AgentDot1qBridgeMsrpEnabledStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 2),
    _Hm2AgentDot1qBridgeMsrpEnabledStatus_Type()
)
hm2AgentDot1qBridgeMsrpEnabledStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMsrpEnabledStatus.setStatus("current")


class _Hm2AgentDot1qBridgeMsrpTalkerPruning_Type(TruthValue):
    """Custom type hm2AgentDot1qBridgeMsrpTalkerPruning based on TruthValue"""


_Hm2AgentDot1qBridgeMsrpTalkerPruning_Object = MibScalar
hm2AgentDot1qBridgeMsrpTalkerPruning = _Hm2AgentDot1qBridgeMsrpTalkerPruning_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 3),
    _Hm2AgentDot1qBridgeMsrpTalkerPruning_Type()
)
hm2AgentDot1qBridgeMsrpTalkerPruning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMsrpTalkerPruning.setStatus("current")


class _Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Type(Unsigned32):
    """Custom type hm2AgentDot1qBridgeMsrpMaxFanInPorts based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Object = MibScalar
hm2AgentDot1qBridgeMsrpMaxFanInPorts = _Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 4),
    _Hm2AgentDot1qBridgeMsrpMaxFanInPorts_Type()
)
hm2AgentDot1qBridgeMsrpMaxFanInPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMsrpMaxFanInPorts.setStatus("current")


class _Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Type(TruthValue):
    """Custom type hm2AgentDot1qBridgeMsrpBoundaryPropagate based on TruthValue"""


_Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Object = MibScalar
hm2AgentDot1qBridgeMsrpBoundaryPropagate = _Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 6),
    _Hm2AgentDot1qBridgeMsrpBoundaryPropagate_Type()
)
hm2AgentDot1qBridgeMsrpBoundaryPropagate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qBridgeMsrpBoundaryPropagate.setStatus("current")
_Hm2AgentDot1qMsrpStreamTable_Object = MibTable
hm2AgentDot1qMsrpStreamTable = _Hm2AgentDot1qMsrpStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamTable.setStatus("current")
_Hm2AgentDot1qMsrpStreamEntry_Object = MibTableRow
hm2AgentDot1qMsrpStreamEntry = _Hm2AgentDot1qMsrpStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1)
)
hm2AgentDot1qMsrpStreamEntry.setIndexNames(
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpStreamIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamEntry.setStatus("current")


class _Hm2AgentDot1qMsrpStreamIndex_Type(Integer32):
    """Custom type hm2AgentDot1qMsrpStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2AgentDot1qMsrpStreamIndex_Type.__name__ = "Integer32"
_Hm2AgentDot1qMsrpStreamIndex_Object = MibTableColumn
hm2AgentDot1qMsrpStreamIndex = _Hm2AgentDot1qMsrpStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 1),
    _Hm2AgentDot1qMsrpStreamIndex_Type()
)
hm2AgentDot1qMsrpStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamIndex.setStatus("current")
_Hm2AgentDot1qMsrpStreamID_Type = Hm2AgentDot1qMsrpStreamIdValue
_Hm2AgentDot1qMsrpStreamID_Object = MibTableColumn
hm2AgentDot1qMsrpStreamID = _Hm2AgentDot1qMsrpStreamID_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 2),
    _Hm2AgentDot1qMsrpStreamID_Type()
)
hm2AgentDot1qMsrpStreamID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamID.setStatus("current")
_Hm2AgentDot1qMsrpStreamDestMacAddr_Type = MacAddress
_Hm2AgentDot1qMsrpStreamDestMacAddr_Object = MibTableColumn
hm2AgentDot1qMsrpStreamDestMacAddr = _Hm2AgentDot1qMsrpStreamDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 3),
    _Hm2AgentDot1qMsrpStreamDestMacAddr_Type()
)
hm2AgentDot1qMsrpStreamDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamDestMacAddr.setStatus("current")
_Hm2AgentDot1qMsrpStreamVlanId_Type = Integer32
_Hm2AgentDot1qMsrpStreamVlanId_Object = MibTableColumn
hm2AgentDot1qMsrpStreamVlanId = _Hm2AgentDot1qMsrpStreamVlanId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 4),
    _Hm2AgentDot1qMsrpStreamVlanId_Type()
)
hm2AgentDot1qMsrpStreamVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamVlanId.setStatus("current")


class _Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Type(Unsigned32):
    """Custom type hm2AgentDot1qMsrpStreamTspecMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Type.__name__ = "Unsigned32"
_Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Object = MibTableColumn
hm2AgentDot1qMsrpStreamTspecMaxFrameSize = _Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 5),
    _Hm2AgentDot1qMsrpStreamTspecMaxFrameSize_Type()
)
hm2AgentDot1qMsrpStreamTspecMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamTspecMaxFrameSize.setStatus("current")


class _Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Type(Unsigned32):
    """Custom type hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Type.__name__ = "Unsigned32"
_Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Object = MibTableColumn
hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames = _Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 6),
    _Hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames_Type()
)
hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames.setStatus("current")
_Hm2AgentDot1qMsrpStreamDataFramePriority_Type = Hm2AgentDot1qPriorityValue
_Hm2AgentDot1qMsrpStreamDataFramePriority_Object = MibTableColumn
hm2AgentDot1qMsrpStreamDataFramePriority = _Hm2AgentDot1qMsrpStreamDataFramePriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 7),
    _Hm2AgentDot1qMsrpStreamDataFramePriority_Type()
)
hm2AgentDot1qMsrpStreamDataFramePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamDataFramePriority.setStatus("current")
_Hm2AgentDot1qMsrpStreamRank_Type = Hm2AgentDot1qMsrpStreamRankValue
_Hm2AgentDot1qMsrpStreamRank_Object = MibTableColumn
hm2AgentDot1qMsrpStreamRank = _Hm2AgentDot1qMsrpStreamRank_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 8),
    _Hm2AgentDot1qMsrpStreamRank_Type()
)
hm2AgentDot1qMsrpStreamRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpStreamRank.setStatus("current")
_Hm2AgentDot1qMsrpReservationTable_Object = MibTable
hm2AgentDot1qMsrpReservationTable = _Hm2AgentDot1qMsrpReservationTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationTable.setStatus("current")
_Hm2AgentDot1qMsrpReservationEntry_Object = MibTableRow
hm2AgentDot1qMsrpReservationEntry = _Hm2AgentDot1qMsrpReservationEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1)
)
hm2AgentDot1qMsrpReservationEntry.setIndexNames(
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpReservationStreamId"),
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpReservationDirection"),
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationEntry.setStatus("current")
_Hm2AgentDot1qMsrpReservationStreamId_Type = Hm2AgentDot1qMsrpStreamIdValue
_Hm2AgentDot1qMsrpReservationStreamId_Object = MibTableColumn
hm2AgentDot1qMsrpReservationStreamId = _Hm2AgentDot1qMsrpReservationStreamId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 1),
    _Hm2AgentDot1qMsrpReservationStreamId_Type()
)
hm2AgentDot1qMsrpReservationStreamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationStreamId.setStatus("current")
_Hm2AgentDot1qMsrpReservationDirection_Type = Hm2AgentDot1qMsrpReservationDirectionValue
_Hm2AgentDot1qMsrpReservationDirection_Object = MibTableColumn
hm2AgentDot1qMsrpReservationDirection = _Hm2AgentDot1qMsrpReservationDirection_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 2),
    _Hm2AgentDot1qMsrpReservationDirection_Type()
)
hm2AgentDot1qMsrpReservationDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationDirection.setStatus("current")
_Hm2AgentDot1qMsrpReservationDeclarationType_Type = Hm2AgentDot1qMsrpReservationDeclarationTypeValue
_Hm2AgentDot1qMsrpReservationDeclarationType_Object = MibTableColumn
hm2AgentDot1qMsrpReservationDeclarationType = _Hm2AgentDot1qMsrpReservationDeclarationType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 3),
    _Hm2AgentDot1qMsrpReservationDeclarationType_Type()
)
hm2AgentDot1qMsrpReservationDeclarationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationDeclarationType.setStatus("current")
_Hm2AgentDot1qMsrpReservationAccumulatedLatency_Type = Unsigned32
_Hm2AgentDot1qMsrpReservationAccumulatedLatency_Object = MibTableColumn
hm2AgentDot1qMsrpReservationAccumulatedLatency = _Hm2AgentDot1qMsrpReservationAccumulatedLatency_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 4),
    _Hm2AgentDot1qMsrpReservationAccumulatedLatency_Type()
)
hm2AgentDot1qMsrpReservationAccumulatedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationAccumulatedLatency.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationAccumulatedLatency.setUnits("nano-seconds")
_Hm2AgentDot1qMsrpReservationFailureBridgeId_Type = BridgeId
_Hm2AgentDot1qMsrpReservationFailureBridgeId_Object = MibTableColumn
hm2AgentDot1qMsrpReservationFailureBridgeId = _Hm2AgentDot1qMsrpReservationFailureBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 5),
    _Hm2AgentDot1qMsrpReservationFailureBridgeId_Type()
)
hm2AgentDot1qMsrpReservationFailureBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationFailureBridgeId.setStatus("current")
_Hm2AgentDot1qMsrpReservationFailureCode_Type = Hm2AgentDot1qMsrpReservationFailureCodeValue
_Hm2AgentDot1qMsrpReservationFailureCode_Object = MibTableColumn
hm2AgentDot1qMsrpReservationFailureCode = _Hm2AgentDot1qMsrpReservationFailureCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 6),
    _Hm2AgentDot1qMsrpReservationFailureCode_Type()
)
hm2AgentDot1qMsrpReservationFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationFailureCode.setStatus("current")
_Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Type = Counter64
_Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Object = MibTableColumn
hm2AgentDot1qMsrpReservationDroppedStreamFrames = _Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 7),
    _Hm2AgentDot1qMsrpReservationDroppedStreamFrames_Type()
)
hm2AgentDot1qMsrpReservationDroppedStreamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationDroppedStreamFrames.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationDroppedStreamFrames.setUnits("frames")
_Hm2AgentDot1qMsrpReservationStreamAge_Type = Unsigned32
_Hm2AgentDot1qMsrpReservationStreamAge_Object = MibTableColumn
hm2AgentDot1qMsrpReservationStreamAge = _Hm2AgentDot1qMsrpReservationStreamAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 8),
    _Hm2AgentDot1qMsrpReservationStreamAge_Type()
)
hm2AgentDot1qMsrpReservationStreamAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationStreamAge.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qMsrpReservationStreamAge.setUnits("seconds")
_Hm2AgentDot1qMrpMsrpStats_ObjectIdentity = ObjectIdentity
hm2AgentDot1qMrpMsrpStats = _Hm2AgentDot1qMrpMsrpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2)
)
_Hm2AgentDot1qMrpMsrpPktTx_Type = Counter32
_Hm2AgentDot1qMrpMsrpPktTx_Object = MibScalar
hm2AgentDot1qMrpMsrpPktTx = _Hm2AgentDot1qMrpMsrpPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 1),
    _Hm2AgentDot1qMrpMsrpPktTx_Type()
)
hm2AgentDot1qMrpMsrpPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPktTx.setStatus("current")
_Hm2AgentDot1qMrpMsrpPktRx_Type = Counter32
_Hm2AgentDot1qMrpMsrpPktRx_Object = MibScalar
hm2AgentDot1qMrpMsrpPktRx = _Hm2AgentDot1qMrpMsrpPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 2),
    _Hm2AgentDot1qMrpMsrpPktRx_Type()
)
hm2AgentDot1qMrpMsrpPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPktRx.setStatus("current")
_Hm2AgentDot1qMrpMsrpPktRxBadHeader_Type = Counter32
_Hm2AgentDot1qMrpMsrpPktRxBadHeader_Object = MibScalar
hm2AgentDot1qMrpMsrpPktRxBadHeader = _Hm2AgentDot1qMrpMsrpPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 3),
    _Hm2AgentDot1qMrpMsrpPktRxBadHeader_Type()
)
hm2AgentDot1qMrpMsrpPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPktRxBadHeader.setStatus("current")
_Hm2AgentDot1qMrpMsrpPktRxBadFormat_Type = Counter32
_Hm2AgentDot1qMrpMsrpPktRxBadFormat_Object = MibScalar
hm2AgentDot1qMrpMsrpPktRxBadFormat = _Hm2AgentDot1qMrpMsrpPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 4),
    _Hm2AgentDot1qMrpMsrpPktRxBadFormat_Type()
)
hm2AgentDot1qMrpMsrpPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPktRxBadFormat.setStatus("current")
_Hm2AgentDot1qMrpMsrpPktTxFailure_Type = Counter32
_Hm2AgentDot1qMrpMsrpPktTxFailure_Object = MibScalar
hm2AgentDot1qMrpMsrpPktTxFailure = _Hm2AgentDot1qMrpMsrpPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 5),
    _Hm2AgentDot1qMrpMsrpPktTxFailure_Type()
)
hm2AgentDot1qMrpMsrpPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPktTxFailure.setStatus("current")
_Hm2AgentDot1qMrpMsrpStatsTable_Object = MibTable
hm2AgentDot1qMrpMsrpStatsTable = _Hm2AgentDot1qMrpMsrpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpStatsTable.setStatus("current")
_Hm2AgentDot1qMrpMsrpStatsEntry_Object = MibTableRow
hm2AgentDot1qMrpMsrpStatsEntry = _Hm2AgentDot1qMrpMsrpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1)
)
hm2AgentDot1qMrpMsrpStatsEntry.setIndexNames(
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMrpMsrpIntf"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpStatsEntry.setStatus("current")


class _Hm2AgentDot1qMrpMsrpIntf_Type(Integer32):
    """Custom type hm2AgentDot1qMrpMsrpIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hm2AgentDot1qMrpMsrpIntf_Type.__name__ = "Integer32"
_Hm2AgentDot1qMrpMsrpIntf_Object = MibTableColumn
hm2AgentDot1qMrpMsrpIntf = _Hm2AgentDot1qMrpMsrpIntf_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 1),
    _Hm2AgentDot1qMrpMsrpIntf_Type()
)
hm2AgentDot1qMrpMsrpIntf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpIntf.setStatus("current")
_Hm2AgentDot1qMrpMsrpPortPktTx_Type = Counter32
_Hm2AgentDot1qMrpMsrpPortPktTx_Object = MibTableColumn
hm2AgentDot1qMrpMsrpPortPktTx = _Hm2AgentDot1qMrpMsrpPortPktTx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 2),
    _Hm2AgentDot1qMrpMsrpPortPktTx_Type()
)
hm2AgentDot1qMrpMsrpPortPktTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPortPktTx.setStatus("current")
_Hm2AgentDot1qMrpMsrpPortPktRx_Type = Counter32
_Hm2AgentDot1qMrpMsrpPortPktRx_Object = MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRx = _Hm2AgentDot1qMrpMsrpPortPktRx_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 3),
    _Hm2AgentDot1qMrpMsrpPortPktRx_Type()
)
hm2AgentDot1qMrpMsrpPortPktRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPortPktRx.setStatus("current")
_Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Type = Counter32
_Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Object = MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRxBadHeader = _Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 4),
    _Hm2AgentDot1qMrpMsrpPortPktRxBadHeader_Type()
)
hm2AgentDot1qMrpMsrpPortPktRxBadHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPortPktRxBadHeader.setStatus("current")
_Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Type = Counter32
_Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Object = MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRxBadFormat = _Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 5),
    _Hm2AgentDot1qMrpMsrpPortPktRxBadFormat_Type()
)
hm2AgentDot1qMrpMsrpPortPktRxBadFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPortPktRxBadFormat.setStatus("current")
_Hm2AgentDot1qMrpMsrpPortPktTxFailure_Type = Counter32
_Hm2AgentDot1qMrpMsrpPortPktTxFailure_Object = MibTableColumn
hm2AgentDot1qMrpMsrpPortPktTxFailure = _Hm2AgentDot1qMrpMsrpPortPktTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 6),
    _Hm2AgentDot1qMrpMsrpPortPktTxFailure_Type()
)
hm2AgentDot1qMrpMsrpPortPktTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPortPktTxFailure.setStatus("current")
_Hm2AgentDot1qMrpMsrpPortPktRegFailure_Type = Counter32
_Hm2AgentDot1qMrpMsrpPortPktRegFailure_Object = MibTableColumn
hm2AgentDot1qMrpMsrpPortPktRegFailure = _Hm2AgentDot1qMrpMsrpPortPktRegFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 7),
    _Hm2AgentDot1qMrpMsrpPortPktRegFailure_Type()
)
hm2AgentDot1qMrpMsrpPortPktRegFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPortPktRegFailure.setStatus("current")
_Hm2AgentDot1qMrpMsrpPktMessageFailure_Type = Counter32
_Hm2AgentDot1qMrpMsrpPktMessageFailure_Object = MibScalar
hm2AgentDot1qMrpMsrpPktMessageFailure = _Hm2AgentDot1qMrpMsrpPktMessageFailure_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 7),
    _Hm2AgentDot1qMrpMsrpPktMessageFailure_Type()
)
hm2AgentDot1qMrpMsrpPktMessageFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qMrpMsrpPktMessageFailure.setStatus("current")
_Hm2AgentDot1qFqtss_ObjectIdentity = ObjectIdentity
hm2AgentDot1qFqtss = _Hm2AgentDot1qFqtss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3)
)
_Hm2AgentDot1qFqtssNotifications_ObjectIdentity = ObjectIdentity
hm2AgentDot1qFqtssNotifications = _Hm2AgentDot1qFqtssNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 0)
)
_Hm2AgentDot1qFqtssObjects_ObjectIdentity = ObjectIdentity
hm2AgentDot1qFqtssObjects = _Hm2AgentDot1qFqtssObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 1)
)
_Hm2AgentDot1qFqtssConformance_ObjectIdentity = ObjectIdentity
hm2AgentDot1qFqtssConformance = _Hm2AgentDot1qFqtssConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 2)
)
_Hm2AgentDot1qFqtssBap_ObjectIdentity = ObjectIdentity
hm2AgentDot1qFqtssBap = _Hm2AgentDot1qFqtssBap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3)
)
_Hm2AgentDot1qFqtssBapTable_Object = MibTable
hm2AgentDot1qFqtssBapTable = _Hm2AgentDot1qFqtssBapTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssBapTable.setStatus("current")
_Hm2AgentDot1qFqtssBapEntry_Object = MibTableRow
hm2AgentDot1qFqtssBapEntry = _Hm2AgentDot1qFqtssBapEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1)
)
hm2AgentDot1qFqtssBapEntry.setIndexNames(
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"),
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qFqtssTrafficClass"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssBapEntry.setStatus("current")
_Hm2AgentDot1qFqtssTrafficClass_Type = Hm2AgentDot1qFqtssTrafficClassValue
_Hm2AgentDot1qFqtssTrafficClass_Object = MibTableColumn
hm2AgentDot1qFqtssTrafficClass = _Hm2AgentDot1qFqtssTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 1),
    _Hm2AgentDot1qFqtssTrafficClass_Type()
)
hm2AgentDot1qFqtssTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssTrafficClass.setStatus("current")
_Hm2AgentDot1qFqtssDeltaBandwidth_Type = Hm2AgentDot1qFqtssDeltaBandwidthValue
_Hm2AgentDot1qFqtssDeltaBandwidth_Object = MibTableColumn
hm2AgentDot1qFqtssDeltaBandwidth = _Hm2AgentDot1qFqtssDeltaBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 2),
    _Hm2AgentDot1qFqtssDeltaBandwidth_Type()
)
hm2AgentDot1qFqtssDeltaBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssDeltaBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssDeltaBandwidth.setUnits("percent")
_Hm2AgentDot1qFqtssOperIdleSlopeMs_Type = Unsigned32
_Hm2AgentDot1qFqtssOperIdleSlopeMs_Object = MibTableColumn
hm2AgentDot1qFqtssOperIdleSlopeMs = _Hm2AgentDot1qFqtssOperIdleSlopeMs_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 3),
    _Hm2AgentDot1qFqtssOperIdleSlopeMs_Type()
)
hm2AgentDot1qFqtssOperIdleSlopeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssOperIdleSlopeMs.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssOperIdleSlopeMs.setUnits("bits per second")
_Hm2AgentDot1qFqtssOperIdleSlopeLs_Type = Unsigned32
_Hm2AgentDot1qFqtssOperIdleSlopeLs_Object = MibTableColumn
hm2AgentDot1qFqtssOperIdleSlopeLs = _Hm2AgentDot1qFqtssOperIdleSlopeLs_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 4),
    _Hm2AgentDot1qFqtssOperIdleSlopeLs_Type()
)
hm2AgentDot1qFqtssOperIdleSlopeLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssOperIdleSlopeLs.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssOperIdleSlopeLs.setUnits("bits per second")


class _Hm2AgentDot1qFqtssAdminIdleSlopeMs_Type(Unsigned32):
    """Custom type hm2AgentDot1qFqtssAdminIdleSlopeMs based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDot1qFqtssAdminIdleSlopeMs_Object = MibTableColumn
hm2AgentDot1qFqtssAdminIdleSlopeMs = _Hm2AgentDot1qFqtssAdminIdleSlopeMs_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 5),
    _Hm2AgentDot1qFqtssAdminIdleSlopeMs_Type()
)
hm2AgentDot1qFqtssAdminIdleSlopeMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssAdminIdleSlopeMs.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssAdminIdleSlopeMs.setUnits("bits per second")


class _Hm2AgentDot1qFqtssAdminIdleSlopeLs_Type(Unsigned32):
    """Custom type hm2AgentDot1qFqtssAdminIdleSlopeLs based on Unsigned32"""
    defaultValue = 0


_Hm2AgentDot1qFqtssAdminIdleSlopeLs_Object = MibTableColumn
hm2AgentDot1qFqtssAdminIdleSlopeLs = _Hm2AgentDot1qFqtssAdminIdleSlopeLs_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 6),
    _Hm2AgentDot1qFqtssAdminIdleSlopeLs_Type()
)
hm2AgentDot1qFqtssAdminIdleSlopeLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssAdminIdleSlopeLs.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssAdminIdleSlopeLs.setUnits("bits per second")
_Hm2AgentDot1qFqtssMappings_ObjectIdentity = ObjectIdentity
hm2AgentDot1qFqtssMappings = _Hm2AgentDot1qFqtssMappings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4)
)
_Hm2AgentDot1qFqtssTxSelectionAlgorithmTable_Object = MibTable
hm2AgentDot1qFqtssTxSelectionAlgorithmTable = _Hm2AgentDot1qFqtssTxSelectionAlgorithmTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssTxSelectionAlgorithmTable.setStatus("current")
_Hm2AgentDot1qFqtssTxSelectionAlgorithmEntry_Object = MibTableRow
hm2AgentDot1qFqtssTxSelectionAlgorithmEntry = _Hm2AgentDot1qFqtssTxSelectionAlgorithmEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 1, 1)
)
hm2AgentDot1qFqtssTxSelectionAlgorithmEntry.setIndexNames(
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"),
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qFqtssTrafficClass"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssTxSelectionAlgorithmEntry.setStatus("current")
_Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Type = Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue
_Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Object = MibTableColumn
hm2AgentDot1qFqtssTxSelectionAlgorithmID = _Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 1, 1, 1),
    _Hm2AgentDot1qFqtssTxSelectionAlgorithmID_Type()
)
hm2AgentDot1qFqtssTxSelectionAlgorithmID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssTxSelectionAlgorithmID.setStatus("current")
_Hm2AgentDot1qFqtssSrpRegenOverrideTable_Object = MibTable
hm2AgentDot1qFqtssSrpRegenOverrideTable = _Hm2AgentDot1qFqtssSrpRegenOverrideTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2)
)
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssSrpRegenOverrideTable.setStatus("current")
_Hm2AgentDot1qFqtssSrpRegenOverrideEntry_Object = MibTableRow
hm2AgentDot1qFqtssSrpRegenOverrideEntry = _Hm2AgentDot1qFqtssSrpRegenOverrideEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1)
)
hm2AgentDot1qFqtssSrpRegenOverrideEntry.setIndexNames(
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"),
    (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qFqtssTrafficClass"),
)
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssSrpRegenOverrideEntry.setStatus("current")
_Hm2AgentDot1qFqtssSrClassPriority_Type = Hm2AgentDot1qPriorityValue
_Hm2AgentDot1qFqtssSrClassPriority_Object = MibTableColumn
hm2AgentDot1qFqtssSrClassPriority = _Hm2AgentDot1qFqtssSrClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1, 1),
    _Hm2AgentDot1qFqtssSrClassPriority_Type()
)
hm2AgentDot1qFqtssSrClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssSrClassPriority.setStatus("current")
_Hm2AgentDot1qFqtssPriorityRegenOverride_Type = Hm2AgentDot1qPriorityValue
_Hm2AgentDot1qFqtssPriorityRegenOverride_Object = MibTableColumn
hm2AgentDot1qFqtssPriorityRegenOverride = _Hm2AgentDot1qFqtssPriorityRegenOverride_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1, 2),
    _Hm2AgentDot1qFqtssPriorityRegenOverride_Type()
)
hm2AgentDot1qFqtssPriorityRegenOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssPriorityRegenOverride.setStatus("current")
_Hm2AgentDot1qFqtssSrpBoundaryPort_Type = TruthValue
_Hm2AgentDot1qFqtssSrpBoundaryPort_Object = MibTableColumn
hm2AgentDot1qFqtssSrpBoundaryPort = _Hm2AgentDot1qFqtssSrpBoundaryPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1, 3),
    _Hm2AgentDot1qFqtssSrpBoundaryPort_Type()
)
hm2AgentDot1qFqtssSrpBoundaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentDot1qFqtssSrpBoundaryPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-MSRP-MIB",
    **{"Hm2AgentDot1qPriorityValue": Hm2AgentDot1qPriorityValue,
       "Hm2AgentDot1qMsrpStreamRankValue": Hm2AgentDot1qMsrpStreamRankValue,
       "Hm2AgentDot1qMsrpStreamIdValue": Hm2AgentDot1qMsrpStreamIdValue,
       "Hm2AgentDot1qMsrpReservationDirectionValue": Hm2AgentDot1qMsrpReservationDirectionValue,
       "Hm2AgentDot1qMsrpReservationDeclarationTypeValue": Hm2AgentDot1qMsrpReservationDeclarationTypeValue,
       "Hm2AgentDot1qMsrpReservationFailureCodeValue": Hm2AgentDot1qMsrpReservationFailureCodeValue,
       "Hm2AgentDot1qFqtssTrafficClassValue": Hm2AgentDot1qFqtssTrafficClassValue,
       "Hm2AgentDot1qFqtssDeltaBandwidthValue": Hm2AgentDot1qFqtssDeltaBandwidthValue,
       "Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue": Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue,
       "hm2PlatformMSRP": hm2PlatformMSRP,
       "hm2AgentDot1qMsrp": hm2AgentDot1qMsrp,
       "hm2AgentDot1qPortMsrpTable": hm2AgentDot1qPortMsrpTable,
       "hm2AgentDot1qPortMsrpEntry": hm2AgentDot1qPortMsrpEntry,
       "hm2AgentDot1qMsrpPort": hm2AgentDot1qMsrpPort,
       "hm2AgentDot1qPortMsrpEnabledStatus": hm2AgentDot1qPortMsrpEnabledStatus,
       "hm2AgentDot1qPortMsrpFailedRegistrations": hm2AgentDot1qPortMsrpFailedRegistrations,
       "hm2AgentDot1qPortMsrpLastPduOrigin": hm2AgentDot1qPortMsrpLastPduOrigin,
       "hm2AgentDot1qPortMsrpPvid": hm2AgentDot1qPortMsrpPvid,
       "hm2AgentDot1qBridgeMsrpEnabledStatus": hm2AgentDot1qBridgeMsrpEnabledStatus,
       "hm2AgentDot1qBridgeMsrpTalkerPruning": hm2AgentDot1qBridgeMsrpTalkerPruning,
       "hm2AgentDot1qBridgeMsrpMaxFanInPorts": hm2AgentDot1qBridgeMsrpMaxFanInPorts,
       "hm2AgentDot1qBridgeMsrpBoundaryPropagate": hm2AgentDot1qBridgeMsrpBoundaryPropagate,
       "hm2AgentDot1qMsrpStreamTable": hm2AgentDot1qMsrpStreamTable,
       "hm2AgentDot1qMsrpStreamEntry": hm2AgentDot1qMsrpStreamEntry,
       "hm2AgentDot1qMsrpStreamIndex": hm2AgentDot1qMsrpStreamIndex,
       "hm2AgentDot1qMsrpStreamID": hm2AgentDot1qMsrpStreamID,
       "hm2AgentDot1qMsrpStreamDestMacAddr": hm2AgentDot1qMsrpStreamDestMacAddr,
       "hm2AgentDot1qMsrpStreamVlanId": hm2AgentDot1qMsrpStreamVlanId,
       "hm2AgentDot1qMsrpStreamTspecMaxFrameSize": hm2AgentDot1qMsrpStreamTspecMaxFrameSize,
       "hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames": hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames,
       "hm2AgentDot1qMsrpStreamDataFramePriority": hm2AgentDot1qMsrpStreamDataFramePriority,
       "hm2AgentDot1qMsrpStreamRank": hm2AgentDot1qMsrpStreamRank,
       "hm2AgentDot1qMsrpReservationTable": hm2AgentDot1qMsrpReservationTable,
       "hm2AgentDot1qMsrpReservationEntry": hm2AgentDot1qMsrpReservationEntry,
       "hm2AgentDot1qMsrpReservationStreamId": hm2AgentDot1qMsrpReservationStreamId,
       "hm2AgentDot1qMsrpReservationDirection": hm2AgentDot1qMsrpReservationDirection,
       "hm2AgentDot1qMsrpReservationDeclarationType": hm2AgentDot1qMsrpReservationDeclarationType,
       "hm2AgentDot1qMsrpReservationAccumulatedLatency": hm2AgentDot1qMsrpReservationAccumulatedLatency,
       "hm2AgentDot1qMsrpReservationFailureBridgeId": hm2AgentDot1qMsrpReservationFailureBridgeId,
       "hm2AgentDot1qMsrpReservationFailureCode": hm2AgentDot1qMsrpReservationFailureCode,
       "hm2AgentDot1qMsrpReservationDroppedStreamFrames": hm2AgentDot1qMsrpReservationDroppedStreamFrames,
       "hm2AgentDot1qMsrpReservationStreamAge": hm2AgentDot1qMsrpReservationStreamAge,
       "hm2AgentDot1qMrpMsrpStats": hm2AgentDot1qMrpMsrpStats,
       "hm2AgentDot1qMrpMsrpPktTx": hm2AgentDot1qMrpMsrpPktTx,
       "hm2AgentDot1qMrpMsrpPktRx": hm2AgentDot1qMrpMsrpPktRx,
       "hm2AgentDot1qMrpMsrpPktRxBadHeader": hm2AgentDot1qMrpMsrpPktRxBadHeader,
       "hm2AgentDot1qMrpMsrpPktRxBadFormat": hm2AgentDot1qMrpMsrpPktRxBadFormat,
       "hm2AgentDot1qMrpMsrpPktTxFailure": hm2AgentDot1qMrpMsrpPktTxFailure,
       "hm2AgentDot1qMrpMsrpStatsTable": hm2AgentDot1qMrpMsrpStatsTable,
       "hm2AgentDot1qMrpMsrpStatsEntry": hm2AgentDot1qMrpMsrpStatsEntry,
       "hm2AgentDot1qMrpMsrpIntf": hm2AgentDot1qMrpMsrpIntf,
       "hm2AgentDot1qMrpMsrpPortPktTx": hm2AgentDot1qMrpMsrpPortPktTx,
       "hm2AgentDot1qMrpMsrpPortPktRx": hm2AgentDot1qMrpMsrpPortPktRx,
       "hm2AgentDot1qMrpMsrpPortPktRxBadHeader": hm2AgentDot1qMrpMsrpPortPktRxBadHeader,
       "hm2AgentDot1qMrpMsrpPortPktRxBadFormat": hm2AgentDot1qMrpMsrpPortPktRxBadFormat,
       "hm2AgentDot1qMrpMsrpPortPktTxFailure": hm2AgentDot1qMrpMsrpPortPktTxFailure,
       "hm2AgentDot1qMrpMsrpPortPktRegFailure": hm2AgentDot1qMrpMsrpPortPktRegFailure,
       "hm2AgentDot1qMrpMsrpPktMessageFailure": hm2AgentDot1qMrpMsrpPktMessageFailure,
       "hm2AgentDot1qFqtss": hm2AgentDot1qFqtss,
       "hm2AgentDot1qFqtssNotifications": hm2AgentDot1qFqtssNotifications,
       "hm2AgentDot1qFqtssObjects": hm2AgentDot1qFqtssObjects,
       "hm2AgentDot1qFqtssConformance": hm2AgentDot1qFqtssConformance,
       "hm2AgentDot1qFqtssBap": hm2AgentDot1qFqtssBap,
       "hm2AgentDot1qFqtssBapTable": hm2AgentDot1qFqtssBapTable,
       "hm2AgentDot1qFqtssBapEntry": hm2AgentDot1qFqtssBapEntry,
       "hm2AgentDot1qFqtssTrafficClass": hm2AgentDot1qFqtssTrafficClass,
       "hm2AgentDot1qFqtssDeltaBandwidth": hm2AgentDot1qFqtssDeltaBandwidth,
       "hm2AgentDot1qFqtssOperIdleSlopeMs": hm2AgentDot1qFqtssOperIdleSlopeMs,
       "hm2AgentDot1qFqtssOperIdleSlopeLs": hm2AgentDot1qFqtssOperIdleSlopeLs,
       "hm2AgentDot1qFqtssAdminIdleSlopeMs": hm2AgentDot1qFqtssAdminIdleSlopeMs,
       "hm2AgentDot1qFqtssAdminIdleSlopeLs": hm2AgentDot1qFqtssAdminIdleSlopeLs,
       "hm2AgentDot1qFqtssMappings": hm2AgentDot1qFqtssMappings,
       "hm2AgentDot1qFqtssTxSelectionAlgorithmTable": hm2AgentDot1qFqtssTxSelectionAlgorithmTable,
       "hm2AgentDot1qFqtssTxSelectionAlgorithmEntry": hm2AgentDot1qFqtssTxSelectionAlgorithmEntry,
       "hm2AgentDot1qFqtssTxSelectionAlgorithmID": hm2AgentDot1qFqtssTxSelectionAlgorithmID,
       "hm2AgentDot1qFqtssSrpRegenOverrideTable": hm2AgentDot1qFqtssSrpRegenOverrideTable,
       "hm2AgentDot1qFqtssSrpRegenOverrideEntry": hm2AgentDot1qFqtssSrpRegenOverrideEntry,
       "hm2AgentDot1qFqtssSrClassPriority": hm2AgentDot1qFqtssSrClassPriority,
       "hm2AgentDot1qFqtssPriorityRegenOverride": hm2AgentDot1qFqtssPriorityRegenOverride,
       "hm2AgentDot1qFqtssSrpBoundaryPort": hm2AgentDot1qFqtssSrpBoundaryPort}
)
