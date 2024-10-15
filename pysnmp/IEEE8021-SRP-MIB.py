# SNMP MIB module (IEEE8021-SRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-SRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:41 2024
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

(ieee8021BridgeBaseComponentId,
 ieee8021BridgeBaseEntry,
 ieee8021BridgeBasePort,
 ieee8021BridgeBasePortEntry) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId",
    "ieee8021BridgeBaseEntry",
    "ieee8021BridgeBasePort",
    "ieee8021BridgeBasePortEntry")

(IEEE8021FqtssTrafficClassValue,) = mibBuilder.importSymbols(
    "IEEE8021-FQTSS-MIB",
    "IEEE8021FqtssTrafficClassValue")

(IEEE8021PriorityCodePoint,
 IEEE8021VlanIndex,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityCodePoint",
    "IEEE8021VlanIndex",
    "ieee802dot1mibs")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021SrpMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19)
)
ieee8021SrpMib.setRevisions(
        ("2018-10-04 00:00",
         "2018-06-28 00:00",
         "2015-12-02 00:00",
         "2014-12-15 00:00",
         "2011-02-27 00:00",
         "2010-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IEEE8021SrpStreamRankValue(Integer32, TextualConvention):
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



class IEEE8021SrpStreamIdValue(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:1x:1x:1x:1x:1x.1x:1x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class IEEE8021SrpReservationDirectionValue(Integer32, TextualConvention):
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



class IEEE8021SrpReservationDeclarationTypeValue(Integer32, TextualConvention):
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



class IEEE8021SrpReservationFailureCodeValue(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_Ieee8021SrpNotifications_ObjectIdentity = ObjectIdentity
ieee8021SrpNotifications = _Ieee8021SrpNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 0)
)
_Ieee8021SrpObjects_ObjectIdentity = ObjectIdentity
ieee8021SrpObjects = _Ieee8021SrpObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 1)
)
_Ieee8021SrpConfiguration_ObjectIdentity = ObjectIdentity
ieee8021SrpConfiguration = _Ieee8021SrpConfiguration_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1)
)
_Ieee8021SrpBridgeBaseTable_Object = MibTable
ieee8021SrpBridgeBaseTable = _Ieee8021SrpBridgeBaseTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseTable.setStatus("current")
_Ieee8021SrpBridgeBaseEntry_Object = MibTableRow
ieee8021SrpBridgeBaseEntry = _Ieee8021SrpBridgeBaseEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseEntry.setStatus("current")


class _Ieee8021SrpBridgeBaseMsrpEnabledStatus_Type(TruthValue):
    """Custom type ieee8021SrpBridgeBaseMsrpEnabledStatus based on TruthValue"""


_Ieee8021SrpBridgeBaseMsrpEnabledStatus_Object = MibTableColumn
ieee8021SrpBridgeBaseMsrpEnabledStatus = _Ieee8021SrpBridgeBaseMsrpEnabledStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 1),
    _Ieee8021SrpBridgeBaseMsrpEnabledStatus_Type()
)
ieee8021SrpBridgeBaseMsrpEnabledStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseMsrpEnabledStatus.setStatus("current")


class _Ieee8021SrpBridgeBaseMsrpTalkerPruning_Type(TruthValue):
    """Custom type ieee8021SrpBridgeBaseMsrpTalkerPruning based on TruthValue"""


_Ieee8021SrpBridgeBaseMsrpTalkerPruning_Object = MibTableColumn
ieee8021SrpBridgeBaseMsrpTalkerPruning = _Ieee8021SrpBridgeBaseMsrpTalkerPruning_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 2),
    _Ieee8021SrpBridgeBaseMsrpTalkerPruning_Type()
)
ieee8021SrpBridgeBaseMsrpTalkerPruning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseMsrpTalkerPruning.setStatus("current")


class _Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Type(Unsigned32):
    """Custom type ieee8021SrpBridgeBaseMsrpMaxFanInPorts based on Unsigned32"""
    defaultValue = 0


_Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Object = MibTableColumn
ieee8021SrpBridgeBaseMsrpMaxFanInPorts = _Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 3),
    _Ieee8021SrpBridgeBaseMsrpMaxFanInPorts_Type()
)
ieee8021SrpBridgeBaseMsrpMaxFanInPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseMsrpMaxFanInPorts.setStatus("current")


class _Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Type(Unsigned32):
    """Custom type ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize based on Unsigned32"""
    defaultValue = 2000


_Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Object = MibTableColumn
ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize = _Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 4),
    _Ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize_Type()
)
ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize.setStatus("current")


class _Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Type(TruthValue):
    """Custom type ieee8021SrpBridgeBaseMsrpTalkerVlanPruning based on TruthValue"""


_Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Object = MibTableColumn
ieee8021SrpBridgeBaseMsrpTalkerVlanPruning = _Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 5),
    _Ieee8021SrpBridgeBaseMsrpTalkerVlanPruning_Type()
)
ieee8021SrpBridgeBaseMsrpTalkerVlanPruning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseMsrpTalkerVlanPruning.setStatus("current")
_Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Type = Unsigned32
_Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Object = MibTableColumn
ieee8021SrpBridgeBaseMsrpMaxSRClasses = _Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 1, 1, 6),
    _Ieee8021SrpBridgeBaseMsrpMaxSRClasses_Type()
)
ieee8021SrpBridgeBaseMsrpMaxSRClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpBridgeBaseMsrpMaxSRClasses.setStatus("current")
_Ieee8021SrpBridgePortTable_Object = MibTable
ieee8021SrpBridgePortTable = _Ieee8021SrpBridgePortTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortTable.setStatus("current")
_Ieee8021SrpBridgePortEntry_Object = MibTableRow
ieee8021SrpBridgePortEntry = _Ieee8021SrpBridgePortEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortEntry.setStatus("current")


class _Ieee8021SrpBridgePortMsrpEnabledStatus_Type(TruthValue):
    """Custom type ieee8021SrpBridgePortMsrpEnabledStatus based on TruthValue"""


_Ieee8021SrpBridgePortMsrpEnabledStatus_Object = MibTableColumn
ieee8021SrpBridgePortMsrpEnabledStatus = _Ieee8021SrpBridgePortMsrpEnabledStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 1),
    _Ieee8021SrpBridgePortMsrpEnabledStatus_Type()
)
ieee8021SrpBridgePortMsrpEnabledStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortMsrpEnabledStatus.setStatus("current")
_Ieee8021SrpBridgePortMsrpFailedRegistrations_Type = Counter64
_Ieee8021SrpBridgePortMsrpFailedRegistrations_Object = MibTableColumn
ieee8021SrpBridgePortMsrpFailedRegistrations = _Ieee8021SrpBridgePortMsrpFailedRegistrations_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 2),
    _Ieee8021SrpBridgePortMsrpFailedRegistrations_Type()
)
ieee8021SrpBridgePortMsrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortMsrpFailedRegistrations.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortMsrpFailedRegistrations.setUnits("failed MSRP registrations")
_Ieee8021SrpBridgePortMsrpLastPduOrigin_Type = MacAddress
_Ieee8021SrpBridgePortMsrpLastPduOrigin_Object = MibTableColumn
ieee8021SrpBridgePortMsrpLastPduOrigin = _Ieee8021SrpBridgePortMsrpLastPduOrigin_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 3),
    _Ieee8021SrpBridgePortMsrpLastPduOrigin_Type()
)
ieee8021SrpBridgePortMsrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortMsrpLastPduOrigin.setStatus("current")


class _Ieee8021SrpBridgePortSrPvid_Type(IEEE8021VlanIndex):
    """Custom type ieee8021SrpBridgePortSrPvid based on IEEE8021VlanIndex"""
    defaultValue = 2


_Ieee8021SrpBridgePortSrPvid_Object = MibTableColumn
ieee8021SrpBridgePortSrPvid = _Ieee8021SrpBridgePortSrPvid_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 4),
    _Ieee8021SrpBridgePortSrPvid_Type()
)
ieee8021SrpBridgePortSrPvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortSrPvid.setStatus("current")


class _Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Type(TruthValue):
    """Custom type ieee8021SrpBridgePortMsrpTalkerPrunningPerPort based on TruthValue"""


_Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Object = MibTableColumn
ieee8021SrpBridgePortMsrpTalkerPrunningPerPort = _Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 1, 2, 1, 5),
    _Ieee8021SrpBridgePortMsrpTalkerPrunningPerPort_Type()
)
ieee8021SrpBridgePortMsrpTalkerPrunningPerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021SrpBridgePortMsrpTalkerPrunningPerPort.setStatus("current")
_Ieee8021SrpLatency_ObjectIdentity = ObjectIdentity
ieee8021SrpLatency = _Ieee8021SrpLatency_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 2)
)
_Ieee8021SrpLatencyTable_Object = MibTable
ieee8021SrpLatencyTable = _Ieee8021SrpLatencyTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ieee8021SrpLatencyTable.setStatus("current")
_Ieee8021SrpLatencyEntry_Object = MibTableRow
ieee8021SrpLatencyEntry = _Ieee8021SrpLatencyEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1, 1)
)
ieee8021SrpLatencyEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
    (0, "IEEE8021-SRP-MIB", "ieee8021SrpTrafficClass"),
)
if mibBuilder.loadTexts:
    ieee8021SrpLatencyEntry.setStatus("current")
_Ieee8021SrpTrafficClass_Type = IEEE8021FqtssTrafficClassValue
_Ieee8021SrpTrafficClass_Object = MibTableColumn
ieee8021SrpTrafficClass = _Ieee8021SrpTrafficClass_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1, 1, 1),
    _Ieee8021SrpTrafficClass_Type()
)
ieee8021SrpTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SrpTrafficClass.setStatus("current")
_Ieee8021SrpPortTcLatency_Type = Unsigned32
_Ieee8021SrpPortTcLatency_Object = MibTableColumn
ieee8021SrpPortTcLatency = _Ieee8021SrpPortTcLatency_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 2, 1, 1, 2),
    _Ieee8021SrpPortTcLatency_Type()
)
ieee8021SrpPortTcLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpPortTcLatency.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SrpPortTcLatency.setUnits("nano-seconds")
_Ieee8021SrpStreams_ObjectIdentity = ObjectIdentity
ieee8021SrpStreams = _Ieee8021SrpStreams_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3)
)
_Ieee8021SrpStreamTable_Object = MibTable
ieee8021SrpStreamTable = _Ieee8021SrpStreamTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ieee8021SrpStreamTable.setStatus("current")
_Ieee8021SrpStreamEntry_Object = MibTableRow
ieee8021SrpStreamEntry = _Ieee8021SrpStreamEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1)
)
ieee8021SrpStreamEntry.setIndexNames(
    (0, "IEEE8021-SRP-MIB", "ieee8021SrpStreamId"),
)
if mibBuilder.loadTexts:
    ieee8021SrpStreamEntry.setStatus("current")
_Ieee8021SrpStreamId_Type = IEEE8021SrpStreamIdValue
_Ieee8021SrpStreamId_Object = MibTableColumn
ieee8021SrpStreamId = _Ieee8021SrpStreamId_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 1),
    _Ieee8021SrpStreamId_Type()
)
ieee8021SrpStreamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SrpStreamId.setStatus("current")
_Ieee8021SrpStreamDestinationAddress_Type = MacAddress
_Ieee8021SrpStreamDestinationAddress_Object = MibTableColumn
ieee8021SrpStreamDestinationAddress = _Ieee8021SrpStreamDestinationAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 2),
    _Ieee8021SrpStreamDestinationAddress_Type()
)
ieee8021SrpStreamDestinationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpStreamDestinationAddress.setStatus("current")
_Ieee8021SrpStreamVlanId_Type = IEEE8021VlanIndex
_Ieee8021SrpStreamVlanId_Object = MibTableColumn
ieee8021SrpStreamVlanId = _Ieee8021SrpStreamVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 3),
    _Ieee8021SrpStreamVlanId_Type()
)
ieee8021SrpStreamVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpStreamVlanId.setStatus("current")


class _Ieee8021SrpStreamTspecMaxFrameSize_Type(Unsigned32):
    """Custom type ieee8021SrpStreamTspecMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021SrpStreamTspecMaxFrameSize_Type.__name__ = "Unsigned32"
_Ieee8021SrpStreamTspecMaxFrameSize_Object = MibTableColumn
ieee8021SrpStreamTspecMaxFrameSize = _Ieee8021SrpStreamTspecMaxFrameSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 4),
    _Ieee8021SrpStreamTspecMaxFrameSize_Type()
)
ieee8021SrpStreamTspecMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpStreamTspecMaxFrameSize.setStatus("current")


class _Ieee8021SrpStreamTspecMaxIntervalFrames_Type(Unsigned32):
    """Custom type ieee8021SrpStreamTspecMaxIntervalFrames based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021SrpStreamTspecMaxIntervalFrames_Type.__name__ = "Unsigned32"
_Ieee8021SrpStreamTspecMaxIntervalFrames_Object = MibTableColumn
ieee8021SrpStreamTspecMaxIntervalFrames = _Ieee8021SrpStreamTspecMaxIntervalFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 5),
    _Ieee8021SrpStreamTspecMaxIntervalFrames_Type()
)
ieee8021SrpStreamTspecMaxIntervalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpStreamTspecMaxIntervalFrames.setStatus("current")
_Ieee8021SrpStreamDataFramePriority_Type = IEEE8021PriorityCodePoint
_Ieee8021SrpStreamDataFramePriority_Object = MibTableColumn
ieee8021SrpStreamDataFramePriority = _Ieee8021SrpStreamDataFramePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 6),
    _Ieee8021SrpStreamDataFramePriority_Type()
)
ieee8021SrpStreamDataFramePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpStreamDataFramePriority.setStatus("current")
_Ieee8021SrpStreamRank_Type = IEEE8021SrpStreamRankValue
_Ieee8021SrpStreamRank_Object = MibTableColumn
ieee8021SrpStreamRank = _Ieee8021SrpStreamRank_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 1, 1, 7),
    _Ieee8021SrpStreamRank_Type()
)
ieee8021SrpStreamRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpStreamRank.setStatus("current")
_Ieee8021SrpStreamPreloadTable_Object = MibTable
ieee8021SrpStreamPreloadTable = _Ieee8021SrpStreamPreloadTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadTable.setStatus("current")
_Ieee8021SrpStreamPreloadEntry_Object = MibTableRow
ieee8021SrpStreamPreloadEntry = _Ieee8021SrpStreamPreloadEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1)
)
ieee8021SrpStreamPreloadEntry.setIndexNames(
    (0, "IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadId"),
)
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadEntry.setStatus("current")
_Ieee8021SrpStreamPreloadId_Type = IEEE8021SrpStreamIdValue
_Ieee8021SrpStreamPreloadId_Object = MibTableColumn
ieee8021SrpStreamPreloadId = _Ieee8021SrpStreamPreloadId_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 1),
    _Ieee8021SrpStreamPreloadId_Type()
)
ieee8021SrpStreamPreloadId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadId.setStatus("current")
_Ieee8021SrpStreamPreloadDestinationAddress_Type = MacAddress
_Ieee8021SrpStreamPreloadDestinationAddress_Object = MibTableColumn
ieee8021SrpStreamPreloadDestinationAddress = _Ieee8021SrpStreamPreloadDestinationAddress_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 2),
    _Ieee8021SrpStreamPreloadDestinationAddress_Type()
)
ieee8021SrpStreamPreloadDestinationAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadDestinationAddress.setStatus("current")
_Ieee8021SrpStreamPreloadVlanId_Type = IEEE8021VlanIndex
_Ieee8021SrpStreamPreloadVlanId_Object = MibTableColumn
ieee8021SrpStreamPreloadVlanId = _Ieee8021SrpStreamPreloadVlanId_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 3),
    _Ieee8021SrpStreamPreloadVlanId_Type()
)
ieee8021SrpStreamPreloadVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadVlanId.setStatus("current")


class _Ieee8021SrpStreamPreloadTspecMaxFrameSize_Type(Unsigned32):
    """Custom type ieee8021SrpStreamPreloadTspecMaxFrameSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021SrpStreamPreloadTspecMaxFrameSize_Type.__name__ = "Unsigned32"
_Ieee8021SrpStreamPreloadTspecMaxFrameSize_Object = MibTableColumn
ieee8021SrpStreamPreloadTspecMaxFrameSize = _Ieee8021SrpStreamPreloadTspecMaxFrameSize_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 4),
    _Ieee8021SrpStreamPreloadTspecMaxFrameSize_Type()
)
ieee8021SrpStreamPreloadTspecMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadTspecMaxFrameSize.setStatus("current")


class _Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Type(Unsigned32):
    """Custom type ieee8021SrpStreamPreloadTspecMaxIntervalFrames based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Type.__name__ = "Unsigned32"
_Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Object = MibTableColumn
ieee8021SrpStreamPreloadTspecMaxIntervalFrames = _Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 5),
    _Ieee8021SrpStreamPreloadTspecMaxIntervalFrames_Type()
)
ieee8021SrpStreamPreloadTspecMaxIntervalFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadTspecMaxIntervalFrames.setStatus("current")
_Ieee8021SrpStreamPreloadDataFramePriority_Type = IEEE8021PriorityCodePoint
_Ieee8021SrpStreamPreloadDataFramePriority_Object = MibTableColumn
ieee8021SrpStreamPreloadDataFramePriority = _Ieee8021SrpStreamPreloadDataFramePriority_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 6),
    _Ieee8021SrpStreamPreloadDataFramePriority_Type()
)
ieee8021SrpStreamPreloadDataFramePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadDataFramePriority.setStatus("current")
_Ieee8021SrpStreamPreloadRank_Type = IEEE8021SrpStreamRankValue
_Ieee8021SrpStreamPreloadRank_Object = MibTableColumn
ieee8021SrpStreamPreloadRank = _Ieee8021SrpStreamPreloadRank_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 3, 2, 1, 7),
    _Ieee8021SrpStreamPreloadRank_Type()
)
ieee8021SrpStreamPreloadRank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpStreamPreloadRank.setStatus("current")
_Ieee8021SrpReservations_ObjectIdentity = ObjectIdentity
ieee8021SrpReservations = _Ieee8021SrpReservations_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4)
)
_Ieee8021SrpReservationsTable_Object = MibTable
ieee8021SrpReservationsTable = _Ieee8021SrpReservationsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ieee8021SrpReservationsTable.setStatus("current")
_Ieee8021SrpReservationsEntry_Object = MibTableRow
ieee8021SrpReservationsEntry = _Ieee8021SrpReservationsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1)
)
ieee8021SrpReservationsEntry.setIndexNames(
    (0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationStreamId"),
    (0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationDirection"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021SrpReservationsEntry.setStatus("current")
_Ieee8021SrpReservationStreamId_Type = IEEE8021SrpStreamIdValue
_Ieee8021SrpReservationStreamId_Object = MibTableColumn
ieee8021SrpReservationStreamId = _Ieee8021SrpReservationStreamId_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 1),
    _Ieee8021SrpReservationStreamId_Type()
)
ieee8021SrpReservationStreamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SrpReservationStreamId.setStatus("current")
_Ieee8021SrpReservationDirection_Type = IEEE8021SrpReservationDirectionValue
_Ieee8021SrpReservationDirection_Object = MibTableColumn
ieee8021SrpReservationDirection = _Ieee8021SrpReservationDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 2),
    _Ieee8021SrpReservationDirection_Type()
)
ieee8021SrpReservationDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SrpReservationDirection.setStatus("current")
_Ieee8021SrpReservationDeclarationType_Type = IEEE8021SrpReservationDeclarationTypeValue
_Ieee8021SrpReservationDeclarationType_Object = MibTableColumn
ieee8021SrpReservationDeclarationType = _Ieee8021SrpReservationDeclarationType_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 3),
    _Ieee8021SrpReservationDeclarationType_Type()
)
ieee8021SrpReservationDeclarationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpReservationDeclarationType.setStatus("current")
_Ieee8021SrpReservationAccumulatedLatency_Type = Unsigned32
_Ieee8021SrpReservationAccumulatedLatency_Object = MibTableColumn
ieee8021SrpReservationAccumulatedLatency = _Ieee8021SrpReservationAccumulatedLatency_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 4),
    _Ieee8021SrpReservationAccumulatedLatency_Type()
)
ieee8021SrpReservationAccumulatedLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpReservationAccumulatedLatency.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SrpReservationAccumulatedLatency.setUnits("nano-seconds")


class _Ieee8021SrpReservationFailureSystemId_Type(OctetString):
    """Custom type ieee8021SrpReservationFailureSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Ieee8021SrpReservationFailureSystemId_Type.__name__ = "OctetString"
_Ieee8021SrpReservationFailureSystemId_Object = MibTableColumn
ieee8021SrpReservationFailureSystemId = _Ieee8021SrpReservationFailureSystemId_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 5),
    _Ieee8021SrpReservationFailureSystemId_Type()
)
ieee8021SrpReservationFailureSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpReservationFailureSystemId.setStatus("current")
_Ieee8021SrpReservationFailureCode_Type = IEEE8021SrpReservationFailureCodeValue
_Ieee8021SrpReservationFailureCode_Object = MibTableColumn
ieee8021SrpReservationFailureCode = _Ieee8021SrpReservationFailureCode_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 6),
    _Ieee8021SrpReservationFailureCode_Type()
)
ieee8021SrpReservationFailureCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpReservationFailureCode.setStatus("current")
_Ieee8021SrpReservationDroppedStreamFrames_Type = Counter64
_Ieee8021SrpReservationDroppedStreamFrames_Object = MibTableColumn
ieee8021SrpReservationDroppedStreamFrames = _Ieee8021SrpReservationDroppedStreamFrames_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 7),
    _Ieee8021SrpReservationDroppedStreamFrames_Type()
)
ieee8021SrpReservationDroppedStreamFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpReservationDroppedStreamFrames.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SrpReservationDroppedStreamFrames.setUnits("frames")
_Ieee8021SrpReservationStreamAge_Type = Unsigned32
_Ieee8021SrpReservationStreamAge_Object = MibTableColumn
ieee8021SrpReservationStreamAge = _Ieee8021SrpReservationStreamAge_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 1, 1, 8),
    _Ieee8021SrpReservationStreamAge_Type()
)
ieee8021SrpReservationStreamAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021SrpReservationStreamAge.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SrpReservationStreamAge.setUnits("seconds")
_Ieee8021SrpReservationsPreloadTable_Object = MibTable
ieee8021SrpReservationsPreloadTable = _Ieee8021SrpReservationsPreloadTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ieee8021SrpReservationsPreloadTable.setStatus("current")
_Ieee8021SrpReservationsPreloadEntry_Object = MibTableRow
ieee8021SrpReservationsPreloadEntry = _Ieee8021SrpReservationsPreloadEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1)
)
ieee8021SrpReservationsPreloadEntry.setIndexNames(
    (0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationsPreloadStreamId"),
    (0, "IEEE8021-SRP-MIB", "ieee8021SrpReservationPreloadDirection"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"),
)
if mibBuilder.loadTexts:
    ieee8021SrpReservationsPreloadEntry.setStatus("current")
_Ieee8021SrpReservationsPreloadStreamId_Type = IEEE8021SrpStreamIdValue
_Ieee8021SrpReservationsPreloadStreamId_Object = MibTableColumn
ieee8021SrpReservationsPreloadStreamId = _Ieee8021SrpReservationsPreloadStreamId_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1, 1),
    _Ieee8021SrpReservationsPreloadStreamId_Type()
)
ieee8021SrpReservationsPreloadStreamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021SrpReservationsPreloadStreamId.setStatus("current")
_Ieee8021SrpReservationPreloadDirection_Type = IEEE8021SrpReservationDirectionValue
_Ieee8021SrpReservationPreloadDirection_Object = MibTableColumn
ieee8021SrpReservationPreloadDirection = _Ieee8021SrpReservationPreloadDirection_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1, 2),
    _Ieee8021SrpReservationPreloadDirection_Type()
)
ieee8021SrpReservationPreloadDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpReservationPreloadDirection.setStatus("current")
_Ieee8021SrpReservationPreloadAccumulatedLatency_Type = Unsigned32
_Ieee8021SrpReservationPreloadAccumulatedLatency_Object = MibTableColumn
ieee8021SrpReservationPreloadAccumulatedLatency = _Ieee8021SrpReservationPreloadAccumulatedLatency_Object(
    (1, 3, 111, 2, 802, 1, 1, 19, 1, 4, 2, 1, 3),
    _Ieee8021SrpReservationPreloadAccumulatedLatency_Type()
)
ieee8021SrpReservationPreloadAccumulatedLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ieee8021SrpReservationPreloadAccumulatedLatency.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021SrpReservationPreloadAccumulatedLatency.setUnits("nano-seconds")
_Ieee8021SrpConformance_ObjectIdentity = ObjectIdentity
ieee8021SrpConformance = _Ieee8021SrpConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 2)
)
_Ieee8021SrpCompliances_ObjectIdentity = ObjectIdentity
ieee8021SrpCompliances = _Ieee8021SrpCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 1)
)
_Ieee8021SrpGroups_ObjectIdentity = ObjectIdentity
ieee8021SrpGroups = _Ieee8021SrpGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2)
)
ieee8021BridgeBaseEntry.registerAugmentions(
    ("IEEE8021-SRP-MIB",
     "ieee8021SrpBridgeBaseEntry")
)
ieee8021SrpBridgeBaseEntry.setIndexNames(*ieee8021BridgeBaseEntry.getIndexNames())
ieee8021BridgeBasePortEntry.registerAugmentions(
    ("IEEE8021-SRP-MIB",
     "ieee8021SrpBridgePortEntry")
)
ieee8021SrpBridgePortEntry.setIndexNames(*ieee8021BridgeBasePortEntry.getIndexNames())

# Managed Objects groups

ieee8021SrpConfigurationGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 1)
)
ieee8021SrpConfigurationGroup.setObjects(
      *(("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpEnabledStatus"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpTalkerPruning"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpMaxFanInPorts"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpTalkerVlanPruning"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpMaxSRClasses"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpEnabledStatus"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpFailedRegistrations"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpLastPduOrigin"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortSrPvid"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpTalkerPrunningPerPort"))
)
if mibBuilder.loadTexts:
    ieee8021SrpConfigurationGroup.setStatus("current")

ieee8021SrpLatencyGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 2)
)
ieee8021SrpLatencyGroup.setObjects(
    ("IEEE8021-SRP-MIB", "ieee8021SrpPortTcLatency")
)
if mibBuilder.loadTexts:
    ieee8021SrpLatencyGroup.setStatus("current")

ieee8021SrpStreamsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 3)
)
ieee8021SrpStreamsGroup.setObjects(
      *(("IEEE8021-SRP-MIB", "ieee8021SrpStreamDestinationAddress"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamVlanId"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamTspecMaxFrameSize"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamTspecMaxIntervalFrames"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamDataFramePriority"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamRank"))
)
if mibBuilder.loadTexts:
    ieee8021SrpStreamsGroup.setStatus("current")

ieee8021SrpReservationsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 4)
)
ieee8021SrpReservationsGroup.setObjects(
      *(("IEEE8021-SRP-MIB", "ieee8021SrpReservationDeclarationType"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpReservationAccumulatedLatency"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpReservationFailureSystemId"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpReservationFailureCode"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpReservationDroppedStreamFrames"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpReservationStreamAge"))
)
if mibBuilder.loadTexts:
    ieee8021SrpReservationsGroup.setStatus("current")

ieee8021SrpConfigurationPruningGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 5)
)
ieee8021SrpConfigurationPruningGroup.setObjects(
      *(("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpTalkerVlanPruning"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpBridgePortMsrpTalkerPrunningPerPort"))
)
if mibBuilder.loadTexts:
    ieee8021SrpConfigurationPruningGroup.setStatus("current")

ieee8021SrpMonitoringSRclassesGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 6)
)
ieee8021SrpMonitoringSRclassesGroup.setObjects(
    ("IEEE8021-SRP-MIB", "ieee8021SrpBridgeBaseMsrpMaxSRClasses")
)
if mibBuilder.loadTexts:
    ieee8021SrpMonitoringSRclassesGroup.setStatus("current")

ieee8021SrpStreamsPreloadGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 7)
)
ieee8021SrpStreamsPreloadGroup.setObjects(
      *(("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadId"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadDestinationAddress"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadVlanId"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadTspecMaxFrameSize"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadTspecMaxIntervalFrames"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadDataFramePriority"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpStreamPreloadRank"))
)
if mibBuilder.loadTexts:
    ieee8021SrpStreamsPreloadGroup.setStatus("current")

ieee8021SrpReservationsPreloadGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 2, 8)
)
ieee8021SrpReservationsPreloadGroup.setObjects(
      *(("IEEE8021-SRP-MIB", "ieee8021SrpReservationsPreloadStreamId"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpReservationPreloadDirection"),
        ("IEEE8021-SRP-MIB", "ieee8021SrpReservationPreloadAccumulatedLatency"))
)
if mibBuilder.loadTexts:
    ieee8021SrpReservationsPreloadGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ieee8021SrpCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 19, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021SrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-SRP-MIB",
    **{"IEEE8021SrpStreamRankValue": IEEE8021SrpStreamRankValue,
       "IEEE8021SrpStreamIdValue": IEEE8021SrpStreamIdValue,
       "IEEE8021SrpReservationDirectionValue": IEEE8021SrpReservationDirectionValue,
       "IEEE8021SrpReservationDeclarationTypeValue": IEEE8021SrpReservationDeclarationTypeValue,
       "IEEE8021SrpReservationFailureCodeValue": IEEE8021SrpReservationFailureCodeValue,
       "ieee8021SrpMib": ieee8021SrpMib,
       "ieee8021SrpNotifications": ieee8021SrpNotifications,
       "ieee8021SrpObjects": ieee8021SrpObjects,
       "ieee8021SrpConfiguration": ieee8021SrpConfiguration,
       "ieee8021SrpBridgeBaseTable": ieee8021SrpBridgeBaseTable,
       "ieee8021SrpBridgeBaseEntry": ieee8021SrpBridgeBaseEntry,
       "ieee8021SrpBridgeBaseMsrpEnabledStatus": ieee8021SrpBridgeBaseMsrpEnabledStatus,
       "ieee8021SrpBridgeBaseMsrpTalkerPruning": ieee8021SrpBridgeBaseMsrpTalkerPruning,
       "ieee8021SrpBridgeBaseMsrpMaxFanInPorts": ieee8021SrpBridgeBaseMsrpMaxFanInPorts,
       "ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize": ieee8021SrpBridgeBaseMsrpLatencyMaxFrameSize,
       "ieee8021SrpBridgeBaseMsrpTalkerVlanPruning": ieee8021SrpBridgeBaseMsrpTalkerVlanPruning,
       "ieee8021SrpBridgeBaseMsrpMaxSRClasses": ieee8021SrpBridgeBaseMsrpMaxSRClasses,
       "ieee8021SrpBridgePortTable": ieee8021SrpBridgePortTable,
       "ieee8021SrpBridgePortEntry": ieee8021SrpBridgePortEntry,
       "ieee8021SrpBridgePortMsrpEnabledStatus": ieee8021SrpBridgePortMsrpEnabledStatus,
       "ieee8021SrpBridgePortMsrpFailedRegistrations": ieee8021SrpBridgePortMsrpFailedRegistrations,
       "ieee8021SrpBridgePortMsrpLastPduOrigin": ieee8021SrpBridgePortMsrpLastPduOrigin,
       "ieee8021SrpBridgePortSrPvid": ieee8021SrpBridgePortSrPvid,
       "ieee8021SrpBridgePortMsrpTalkerPrunningPerPort": ieee8021SrpBridgePortMsrpTalkerPrunningPerPort,
       "ieee8021SrpLatency": ieee8021SrpLatency,
       "ieee8021SrpLatencyTable": ieee8021SrpLatencyTable,
       "ieee8021SrpLatencyEntry": ieee8021SrpLatencyEntry,
       "ieee8021SrpTrafficClass": ieee8021SrpTrafficClass,
       "ieee8021SrpPortTcLatency": ieee8021SrpPortTcLatency,
       "ieee8021SrpStreams": ieee8021SrpStreams,
       "ieee8021SrpStreamTable": ieee8021SrpStreamTable,
       "ieee8021SrpStreamEntry": ieee8021SrpStreamEntry,
       "ieee8021SrpStreamId": ieee8021SrpStreamId,
       "ieee8021SrpStreamDestinationAddress": ieee8021SrpStreamDestinationAddress,
       "ieee8021SrpStreamVlanId": ieee8021SrpStreamVlanId,
       "ieee8021SrpStreamTspecMaxFrameSize": ieee8021SrpStreamTspecMaxFrameSize,
       "ieee8021SrpStreamTspecMaxIntervalFrames": ieee8021SrpStreamTspecMaxIntervalFrames,
       "ieee8021SrpStreamDataFramePriority": ieee8021SrpStreamDataFramePriority,
       "ieee8021SrpStreamRank": ieee8021SrpStreamRank,
       "ieee8021SrpStreamPreloadTable": ieee8021SrpStreamPreloadTable,
       "ieee8021SrpStreamPreloadEntry": ieee8021SrpStreamPreloadEntry,
       "ieee8021SrpStreamPreloadId": ieee8021SrpStreamPreloadId,
       "ieee8021SrpStreamPreloadDestinationAddress": ieee8021SrpStreamPreloadDestinationAddress,
       "ieee8021SrpStreamPreloadVlanId": ieee8021SrpStreamPreloadVlanId,
       "ieee8021SrpStreamPreloadTspecMaxFrameSize": ieee8021SrpStreamPreloadTspecMaxFrameSize,
       "ieee8021SrpStreamPreloadTspecMaxIntervalFrames": ieee8021SrpStreamPreloadTspecMaxIntervalFrames,
       "ieee8021SrpStreamPreloadDataFramePriority": ieee8021SrpStreamPreloadDataFramePriority,
       "ieee8021SrpStreamPreloadRank": ieee8021SrpStreamPreloadRank,
       "ieee8021SrpReservations": ieee8021SrpReservations,
       "ieee8021SrpReservationsTable": ieee8021SrpReservationsTable,
       "ieee8021SrpReservationsEntry": ieee8021SrpReservationsEntry,
       "ieee8021SrpReservationStreamId": ieee8021SrpReservationStreamId,
       "ieee8021SrpReservationDirection": ieee8021SrpReservationDirection,
       "ieee8021SrpReservationDeclarationType": ieee8021SrpReservationDeclarationType,
       "ieee8021SrpReservationAccumulatedLatency": ieee8021SrpReservationAccumulatedLatency,
       "ieee8021SrpReservationFailureSystemId": ieee8021SrpReservationFailureSystemId,
       "ieee8021SrpReservationFailureCode": ieee8021SrpReservationFailureCode,
       "ieee8021SrpReservationDroppedStreamFrames": ieee8021SrpReservationDroppedStreamFrames,
       "ieee8021SrpReservationStreamAge": ieee8021SrpReservationStreamAge,
       "ieee8021SrpReservationsPreloadTable": ieee8021SrpReservationsPreloadTable,
       "ieee8021SrpReservationsPreloadEntry": ieee8021SrpReservationsPreloadEntry,
       "ieee8021SrpReservationsPreloadStreamId": ieee8021SrpReservationsPreloadStreamId,
       "ieee8021SrpReservationPreloadDirection": ieee8021SrpReservationPreloadDirection,
       "ieee8021SrpReservationPreloadAccumulatedLatency": ieee8021SrpReservationPreloadAccumulatedLatency,
       "ieee8021SrpConformance": ieee8021SrpConformance,
       "ieee8021SrpCompliances": ieee8021SrpCompliances,
       "ieee8021SrpCompliance": ieee8021SrpCompliance,
       "ieee8021SrpGroups": ieee8021SrpGroups,
       "ieee8021SrpConfigurationGroup": ieee8021SrpConfigurationGroup,
       "ieee8021SrpLatencyGroup": ieee8021SrpLatencyGroup,
       "ieee8021SrpStreamsGroup": ieee8021SrpStreamsGroup,
       "ieee8021SrpReservationsGroup": ieee8021SrpReservationsGroup,
       "ieee8021SrpConfigurationPruningGroup": ieee8021SrpConfigurationPruningGroup,
       "ieee8021SrpMonitoringSRclassesGroup": ieee8021SrpMonitoringSRclassesGroup,
       "ieee8021SrpStreamsPreloadGroup": ieee8021SrpStreamsPreloadGroup,
       "ieee8021SrpReservationsPreloadGroup": ieee8021SrpReservationsPreloadGroup}
)
