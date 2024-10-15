# SNMP MIB module (NRC-HUB1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NRC-HUB1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:29:10 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Nrc_ObjectIdentity = ObjectIdentity
nrc = _Nrc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 315)
)
_Hub1_ObjectIdentity = ObjectIdentity
hub1 = _Hub1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 315, 1)
)


class _Hub1AutoPartition_Type(Integer32):
    """Custom type hub1AutoPartition based on Integer32"""
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


_Hub1AutoPartition_Type.__name__ = "Integer32"
_Hub1AutoPartition_Object = MibScalar
hub1AutoPartition = _Hub1AutoPartition_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 1),
    _Hub1AutoPartition_Type()
)
hub1AutoPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1AutoPartition.setStatus("mandatory")


class _Hub1ReconnectOnTransmission_Type(Integer32):
    """Custom type hub1ReconnectOnTransmission based on Integer32"""
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


_Hub1ReconnectOnTransmission_Type.__name__ = "Integer32"
_Hub1ReconnectOnTransmission_Object = MibScalar
hub1ReconnectOnTransmission = _Hub1ReconnectOnTransmission_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 2),
    _Hub1ReconnectOnTransmission_Type()
)
hub1ReconnectOnTransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1ReconnectOnTransmission.setStatus("mandatory")


class _Hub1IncludeOutOfWinColl_Type(Integer32):
    """Custom type hub1IncludeOutOfWinColl based on Integer32"""
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


_Hub1IncludeOutOfWinColl_Type.__name__ = "Integer32"
_Hub1IncludeOutOfWinColl_Object = MibScalar
hub1IncludeOutOfWinColl = _Hub1IncludeOutOfWinColl_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 3),
    _Hub1IncludeOutOfWinColl_Type()
)
hub1IncludeOutOfWinColl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1IncludeOutOfWinColl.setStatus("mandatory")


class _Hub1LoopbackPartition_Type(Integer32):
    """Custom type hub1LoopbackPartition based on Integer32"""
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


_Hub1LoopbackPartition_Type.__name__ = "Integer32"
_Hub1LoopbackPartition_Object = MibScalar
hub1LoopbackPartition = _Hub1LoopbackPartition_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 4),
    _Hub1LoopbackPartition_Type()
)
hub1LoopbackPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1LoopbackPartition.setStatus("mandatory")


class _Hub1CollisionLimit_Type(Integer32):
    """Custom type hub1CollisionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(31,
              63)
        )
    )
    namedValues = NamedValues(
        *(("high", 63),
          ("low", 31))
    )


_Hub1CollisionLimit_Type.__name__ = "Integer32"
_Hub1CollisionLimit_Object = MibScalar
hub1CollisionLimit = _Hub1CollisionLimit_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 5),
    _Hub1CollisionLimit_Type()
)
hub1CollisionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1CollisionLimit.setStatus("mandatory")


class _Hub1CarrierRecoverTime_Type(Integer32):
    """Custom type hub1CarrierRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("long", 5),
          ("short", 3))
    )


_Hub1CarrierRecoverTime_Type.__name__ = "Integer32"
_Hub1CarrierRecoverTime_Object = MibScalar
hub1CarrierRecoverTime = _Hub1CarrierRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 6),
    _Hub1CarrierRecoverTime_Type()
)
hub1CarrierRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1CarrierRecoverTime.setStatus("mandatory")


class _Hub1EventCounterFlags_Type(OctetString):
    """Custom type hub1EventCounterFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hub1EventCounterFlags_Type.__name__ = "OctetString"
_Hub1EventCounterFlags_Object = MibScalar
hub1EventCounterFlags = _Hub1EventCounterFlags_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 7),
    _Hub1EventCounterFlags_Type()
)
hub1EventCounterFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1EventCounterFlags.setStatus("mandatory")


class _Hub1EventRecordFlags_Type(OctetString):
    """Custom type hub1EventRecordFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hub1EventRecordFlags_Type.__name__ = "OctetString"
_Hub1EventRecordFlags_Object = MibScalar
hub1EventRecordFlags = _Hub1EventRecordFlags_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 8),
    _Hub1EventRecordFlags_Type()
)
hub1EventRecordFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1EventRecordFlags.setStatus("mandatory")


class _Hub1BridgingMode_Type(Integer32):
    """Custom type hub1BridgingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 1),
          ("bypass", 2))
    )


_Hub1BridgingMode_Type.__name__ = "Integer32"
_Hub1BridgingMode_Object = MibScalar
hub1BridgingMode = _Hub1BridgingMode_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 9),
    _Hub1BridgingMode_Type()
)
hub1BridgingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1BridgingMode.setStatus("mandatory")


class _Hub1ProtocolFilterMode_Type(Integer32):
    """Custom type hub1ProtocolFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 2),
          ("off", 1),
          ("pass", 3))
    )


_Hub1ProtocolFilterMode_Type.__name__ = "Integer32"
_Hub1ProtocolFilterMode_Object = MibScalar
hub1ProtocolFilterMode = _Hub1ProtocolFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 10),
    _Hub1ProtocolFilterMode_Type()
)
hub1ProtocolFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1ProtocolFilterMode.setStatus("mandatory")


class _Hub1FilterProtocols_Type(OctetString):
    """Custom type hub1FilterProtocols based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hub1FilterProtocols_Type.__name__ = "OctetString"
_Hub1FilterProtocols_Object = MibScalar
hub1FilterProtocols = _Hub1FilterProtocols_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 11),
    _Hub1FilterProtocols_Type()
)
hub1FilterProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1FilterProtocols.setStatus("mandatory")
_Hub1ConsoleBaudRate_Type = Integer32
_Hub1ConsoleBaudRate_Object = MibScalar
hub1ConsoleBaudRate = _Hub1ConsoleBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 12),
    _Hub1ConsoleBaudRate_Type()
)
hub1ConsoleBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1ConsoleBaudRate.setStatus("mandatory")


class _Hub1Reset_Type(Integer32):
    """Custom type hub1Reset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 1),
          ("reset", 2))
    )


_Hub1Reset_Type.__name__ = "Integer32"
_Hub1Reset_Object = MibScalar
hub1Reset = _Hub1Reset_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 13),
    _Hub1Reset_Type()
)
hub1Reset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1Reset.setStatus("mandatory")


class _Hub1SoftwareVersion_Type(DisplayString):
    """Custom type hub1SoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Hub1SoftwareVersion_Type.__name__ = "DisplayString"
_Hub1SoftwareVersion_Object = MibScalar
hub1SoftwareVersion = _Hub1SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 14),
    _Hub1SoftwareVersion_Type()
)
hub1SoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1SoftwareVersion.setStatus("mandatory")
_Hub1PortTable_Object = MibTable
hub1PortTable = _Hub1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15)
)
if mibBuilder.loadTexts:
    hub1PortTable.setStatus("mandatory")
_Hub1PortEntry_Object = MibTableRow
hub1PortEntry = _Hub1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1)
)
hub1PortEntry.setIndexNames(
    (0, "NRC-HUB1-MIB", "hub1PortIndex"),
)
if mibBuilder.loadTexts:
    hub1PortEntry.setStatus("mandatory")


class _Hub1PortIndex_Type(Integer32):
    """Custom type hub1PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_Hub1PortIndex_Type.__name__ = "Integer32"
_Hub1PortIndex_Object = MibTableColumn
hub1PortIndex = _Hub1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 1),
    _Hub1PortIndex_Type()
)
hub1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1PortIndex.setStatus("mandatory")


class _Hub1PortForceReconnect_Type(Integer32):
    """Custom type hub1PortForceReconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("force-reconnect", 2),
          ("idle", 1))
    )


_Hub1PortForceReconnect_Type.__name__ = "Integer32"
_Hub1PortForceReconnect_Object = MibTableColumn
hub1PortForceReconnect = _Hub1PortForceReconnect_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 2),
    _Hub1PortForceReconnect_Type()
)
hub1PortForceReconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1PortForceReconnect.setStatus("mandatory")


class _Hub1PortPartitionReason_Type(Integer32):
    """Custom type hub1PortPartitionReason based on Integer32"""
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
        *(("consecutive-collision-limit", 3),
          ("data-loopback-failure", 5),
          ("excessive-len-of-collision-limit", 4),
          ("not-partitioned", 1),
          ("other", 2),
          ("process-forced-reconnection", 6))
    )


_Hub1PortPartitionReason_Type.__name__ = "Integer32"
_Hub1PortPartitionReason_Object = MibTableColumn
hub1PortPartitionReason = _Hub1PortPartitionReason_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 3),
    _Hub1PortPartitionReason_Type()
)
hub1PortPartitionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1PortPartitionReason.setStatus("mandatory")


class _Hub1PortLinkState_Type(Integer32):
    """Custom type hub1PortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("unknown", 1),
          ("up", 2))
    )


_Hub1PortLinkState_Type.__name__ = "Integer32"
_Hub1PortLinkState_Object = MibTableColumn
hub1PortLinkState = _Hub1PortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 4),
    _Hub1PortLinkState_Type()
)
hub1PortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1PortLinkState.setStatus("mandatory")


class _Hub1PortLinkEnable_Type(Integer32):
    """Custom type hub1PortLinkEnable based on Integer32"""
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


_Hub1PortLinkEnable_Type.__name__ = "Integer32"
_Hub1PortLinkEnable_Object = MibTableColumn
hub1PortLinkEnable = _Hub1PortLinkEnable_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 5),
    _Hub1PortLinkEnable_Type()
)
hub1PortLinkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1PortLinkEnable.setStatus("mandatory")


class _Hub1PortPolarityStatus_Type(Integer32):
    """Custom type hub1PortPolarityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("reversed", 2))
    )


_Hub1PortPolarityStatus_Type.__name__ = "Integer32"
_Hub1PortPolarityStatus_Object = MibTableColumn
hub1PortPolarityStatus = _Hub1PortPolarityStatus_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 6),
    _Hub1PortPolarityStatus_Type()
)
hub1PortPolarityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1PortPolarityStatus.setStatus("mandatory")


class _Hub1PortName_Type(DisplayString):
    """Custom type hub1PortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hub1PortName_Type.__name__ = "DisplayString"
_Hub1PortName_Object = MibTableColumn
hub1PortName = _Hub1PortName_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 7),
    _Hub1PortName_Type()
)
hub1PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hub1PortName.setStatus("mandatory")
_Hub1PortEventCount_Type = Integer32
_Hub1PortEventCount_Object = MibTableColumn
hub1PortEventCount = _Hub1PortEventCount_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 8),
    _Hub1PortEventCount_Type()
)
hub1PortEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1PortEventCount.setStatus("mandatory")


class _Hub1PortRecordValue_Type(OctetString):
    """Custom type hub1PortRecordValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hub1PortRecordValue_Type.__name__ = "OctetString"
_Hub1PortRecordValue_Object = MibScalar
hub1PortRecordValue = _Hub1PortRecordValue_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 9),
    _Hub1PortRecordValue_Type()
)
hub1PortRecordValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1PortRecordValue.setStatus("mandatory")


class _Hub1PortType_Type(Integer32):
    """Custom type hub1PortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fiber-FOIRL", 4),
          ("other", 1),
          ("thinNet-10Base2", 3),
          ("twistedPair-10BaseT", 2))
    )


_Hub1PortType_Type.__name__ = "Integer32"
_Hub1PortType_Object = MibTableColumn
hub1PortType = _Hub1PortType_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 15, 1, 10),
    _Hub1PortType_Type()
)
hub1PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1PortType.setStatus("mandatory")
_Hub1IFTable_Object = MibTable
hub1IFTable = _Hub1IFTable_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16)
)
if mibBuilder.loadTexts:
    hub1IFTable.setStatus("mandatory")
_Hub1IFEntry_Object = MibTableRow
hub1IFEntry = _Hub1IFEntry_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1)
)
hub1IFEntry.setIndexNames(
    (0, "NRC-HUB1-MIB", "hub1IFIndex"),
)
if mibBuilder.loadTexts:
    hub1IFEntry.setStatus("mandatory")
_Hub1IFIndex_Type = Integer32
_Hub1IFIndex_Object = MibTableColumn
hub1IFIndex = _Hub1IFIndex_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 1),
    _Hub1IFIndex_Type()
)
hub1IFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFIndex.setStatus("mandatory")
_Hub1IFInAlignmentErrors_Type = Counter32
_Hub1IFInAlignmentErrors_Object = MibTableColumn
hub1IFInAlignmentErrors = _Hub1IFInAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 2),
    _Hub1IFInAlignmentErrors_Type()
)
hub1IFInAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFInAlignmentErrors.setStatus("mandatory")
_Hub1IFInCrcErrors_Type = Counter32
_Hub1IFInCrcErrors_Object = MibTableColumn
hub1IFInCrcErrors = _Hub1IFInCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 3),
    _Hub1IFInCrcErrors_Type()
)
hub1IFInCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFInCrcErrors.setStatus("mandatory")
_Hub1IFInCollisions_Type = Counter32
_Hub1IFInCollisions_Object = MibTableColumn
hub1IFInCollisions = _Hub1IFInCollisions_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 4),
    _Hub1IFInCollisions_Type()
)
hub1IFInCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFInCollisions.setStatus("mandatory")
_Hub1IFInMtuExceededDiscards_Type = Counter32
_Hub1IFInMtuExceededDiscards_Object = MibTableColumn
hub1IFInMtuExceededDiscards = _Hub1IFInMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 5),
    _Hub1IFInMtuExceededDiscards_Type()
)
hub1IFInMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFInMtuExceededDiscards.setStatus("mandatory")
_Hub1IFInShortErrors_Type = Counter32
_Hub1IFInShortErrors_Object = MibTableColumn
hub1IFInShortErrors = _Hub1IFInShortErrors_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 6),
    _Hub1IFInShortErrors_Type()
)
hub1IFInShortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFInShortErrors.setStatus("mandatory")
_Hub1IFInOverrunDiscards_Type = Counter32
_Hub1IFInOverrunDiscards_Object = MibTableColumn
hub1IFInOverrunDiscards = _Hub1IFInOverrunDiscards_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 7),
    _Hub1IFInOverrunDiscards_Type()
)
hub1IFInOverrunDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFInOverrunDiscards.setStatus("mandatory")
_Hub1IFOutUnderruns_Type = Counter32
_Hub1IFOutUnderruns_Object = MibTableColumn
hub1IFOutUnderruns = _Hub1IFOutUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 8),
    _Hub1IFOutUnderruns_Type()
)
hub1IFOutUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFOutUnderruns.setStatus("mandatory")
_Hub1IFOutLostCts_Type = Counter32
_Hub1IFOutLostCts_Object = MibTableColumn
hub1IFOutLostCts = _Hub1IFOutLostCts_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 9),
    _Hub1IFOutLostCts_Type()
)
hub1IFOutLostCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFOutLostCts.setStatus("mandatory")
_Hub1IFOutLostCrs_Type = Counter32
_Hub1IFOutLostCrs_Object = MibTableColumn
hub1IFOutLostCrs = _Hub1IFOutLostCrs_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 10),
    _Hub1IFOutLostCrs_Type()
)
hub1IFOutLostCrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFOutLostCrs.setStatus("mandatory")
_Hub1IFOutMtuExceededDiscards_Type = Counter32
_Hub1IFOutMtuExceededDiscards_Object = MibTableColumn
hub1IFOutMtuExceededDiscards = _Hub1IFOutMtuExceededDiscards_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 11),
    _Hub1IFOutMtuExceededDiscards_Type()
)
hub1IFOutMtuExceededDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFOutMtuExceededDiscards.setStatus("mandatory")
_Hub1IFOutCollisions_Type = Counter32
_Hub1IFOutCollisions_Object = MibTableColumn
hub1IFOutCollisions = _Hub1IFOutCollisions_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 12),
    _Hub1IFOutCollisions_Type()
)
hub1IFOutCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFOutCollisions.setStatus("mandatory")


class _Hub1IFChannelUtilization_Type(OctetString):
    """Custom type hub1IFChannelUtilization based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(90, 90),
    )


_Hub1IFChannelUtilization_Type.__name__ = "OctetString"
_Hub1IFChannelUtilization_Object = MibTableColumn
hub1IFChannelUtilization = _Hub1IFChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 16, 1, 13),
    _Hub1IFChannelUtilization_Type()
)
hub1IFChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1IFChannelUtilization.setStatus("mandatory")
_Hub1LastFailureReason_Type = Integer32
_Hub1LastFailureReason_Object = MibScalar
hub1LastFailureReason = _Hub1LastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 315, 1, 17),
    _Hub1LastFailureReason_Type()
)
hub1LastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hub1LastFailureReason.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NRC-HUB1-MIB",
    **{"enterprises": enterprises,
       "nrc": nrc,
       "hub1": hub1,
       "hub1AutoPartition": hub1AutoPartition,
       "hub1ReconnectOnTransmission": hub1ReconnectOnTransmission,
       "hub1IncludeOutOfWinColl": hub1IncludeOutOfWinColl,
       "hub1LoopbackPartition": hub1LoopbackPartition,
       "hub1CollisionLimit": hub1CollisionLimit,
       "hub1CarrierRecoverTime": hub1CarrierRecoverTime,
       "hub1EventCounterFlags": hub1EventCounterFlags,
       "hub1EventRecordFlags": hub1EventRecordFlags,
       "hub1BridgingMode": hub1BridgingMode,
       "hub1ProtocolFilterMode": hub1ProtocolFilterMode,
       "hub1FilterProtocols": hub1FilterProtocols,
       "hub1ConsoleBaudRate": hub1ConsoleBaudRate,
       "hub1Reset": hub1Reset,
       "hub1SoftwareVersion": hub1SoftwareVersion,
       "hub1PortTable": hub1PortTable,
       "hub1PortEntry": hub1PortEntry,
       "hub1PortIndex": hub1PortIndex,
       "hub1PortForceReconnect": hub1PortForceReconnect,
       "hub1PortPartitionReason": hub1PortPartitionReason,
       "hub1PortLinkState": hub1PortLinkState,
       "hub1PortLinkEnable": hub1PortLinkEnable,
       "hub1PortPolarityStatus": hub1PortPolarityStatus,
       "hub1PortName": hub1PortName,
       "hub1PortEventCount": hub1PortEventCount,
       "hub1PortRecordValue": hub1PortRecordValue,
       "hub1PortType": hub1PortType,
       "hub1IFTable": hub1IFTable,
       "hub1IFEntry": hub1IFEntry,
       "hub1IFIndex": hub1IFIndex,
       "hub1IFInAlignmentErrors": hub1IFInAlignmentErrors,
       "hub1IFInCrcErrors": hub1IFInCrcErrors,
       "hub1IFInCollisions": hub1IFInCollisions,
       "hub1IFInMtuExceededDiscards": hub1IFInMtuExceededDiscards,
       "hub1IFInShortErrors": hub1IFInShortErrors,
       "hub1IFInOverrunDiscards": hub1IFInOverrunDiscards,
       "hub1IFOutUnderruns": hub1IFOutUnderruns,
       "hub1IFOutLostCts": hub1IFOutLostCts,
       "hub1IFOutLostCrs": hub1IFOutLostCrs,
       "hub1IFOutMtuExceededDiscards": hub1IFOutMtuExceededDiscards,
       "hub1IFOutCollisions": hub1IFOutCollisions,
       "hub1IFChannelUtilization": hub1IFChannelUtilization,
       "hub1LastFailureReason": hub1LastFailureReason}
)
