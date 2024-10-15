# SNMP MIB module (RFC1381-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1381-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:34 2024
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

(PositiveInteger,) = mibBuilder.importSymbols(
    "RFC1253-MIB",
    "PositiveInteger")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lapb_ObjectIdentity = ObjectIdentity
lapb = _Lapb_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 16)
)
_LapbAdmnTable_Object = MibTable
lapbAdmnTable = _LapbAdmnTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1)
)
if mibBuilder.loadTexts:
    lapbAdmnTable.setStatus("mandatory")
_LapbAdmnEntry_Object = MibTableRow
lapbAdmnEntry = _LapbAdmnEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1)
)
lapbAdmnEntry.setIndexNames(
    (0, "RFC1381-MIB", "lapbAdmnIndex"),
)
if mibBuilder.loadTexts:
    lapbAdmnEntry.setStatus("mandatory")
_LapbAdmnIndex_Type = IfIndexType
_LapbAdmnIndex_Object = MibTableColumn
lapbAdmnIndex = _LapbAdmnIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 1),
    _LapbAdmnIndex_Type()
)
lapbAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbAdmnIndex.setStatus("mandatory")


class _LapbAdmnStationType_Type(Integer32):
    """Custom type lapbAdmnStationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("dxe", 3))
    )


_LapbAdmnStationType_Type.__name__ = "Integer32"
_LapbAdmnStationType_Object = MibTableColumn
lapbAdmnStationType = _LapbAdmnStationType_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 2),
    _LapbAdmnStationType_Type()
)
lapbAdmnStationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnStationType.setStatus("mandatory")


class _LapbAdmnControlField_Type(Integer32):
    """Custom type lapbAdmnControlField based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_LapbAdmnControlField_Type.__name__ = "Integer32"
_LapbAdmnControlField_Object = MibTableColumn
lapbAdmnControlField = _LapbAdmnControlField_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 3),
    _LapbAdmnControlField_Type()
)
lapbAdmnControlField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnControlField.setStatus("mandatory")


class _LapbAdmnTransmitN1FrameSize_Type(PositiveInteger):
    """Custom type lapbAdmnTransmitN1FrameSize based on PositiveInteger"""
    defaultValue = 36000


_LapbAdmnTransmitN1FrameSize_Object = MibTableColumn
lapbAdmnTransmitN1FrameSize = _LapbAdmnTransmitN1FrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 4),
    _LapbAdmnTransmitN1FrameSize_Type()
)
lapbAdmnTransmitN1FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnTransmitN1FrameSize.setStatus("mandatory")


class _LapbAdmnReceiveN1FrameSize_Type(PositiveInteger):
    """Custom type lapbAdmnReceiveN1FrameSize based on PositiveInteger"""
    defaultValue = 36000


_LapbAdmnReceiveN1FrameSize_Object = MibTableColumn
lapbAdmnReceiveN1FrameSize = _LapbAdmnReceiveN1FrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 5),
    _LapbAdmnReceiveN1FrameSize_Type()
)
lapbAdmnReceiveN1FrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnReceiveN1FrameSize.setStatus("mandatory")


class _LapbAdmnTransmitKWindowSize_Type(Integer32):
    """Custom type lapbAdmnTransmitKWindowSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbAdmnTransmitKWindowSize_Type.__name__ = "Integer32"
_LapbAdmnTransmitKWindowSize_Object = MibTableColumn
lapbAdmnTransmitKWindowSize = _LapbAdmnTransmitKWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 6),
    _LapbAdmnTransmitKWindowSize_Type()
)
lapbAdmnTransmitKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnTransmitKWindowSize.setStatus("mandatory")


class _LapbAdmnReceiveKWindowSize_Type(Integer32):
    """Custom type lapbAdmnReceiveKWindowSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbAdmnReceiveKWindowSize_Type.__name__ = "Integer32"
_LapbAdmnReceiveKWindowSize_Object = MibTableColumn
lapbAdmnReceiveKWindowSize = _LapbAdmnReceiveKWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 7),
    _LapbAdmnReceiveKWindowSize_Type()
)
lapbAdmnReceiveKWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnReceiveKWindowSize.setStatus("mandatory")


class _LapbAdmnN2RxmitCount_Type(Integer32):
    """Custom type lapbAdmnN2RxmitCount based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LapbAdmnN2RxmitCount_Type.__name__ = "Integer32"
_LapbAdmnN2RxmitCount_Object = MibTableColumn
lapbAdmnN2RxmitCount = _LapbAdmnN2RxmitCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 8),
    _LapbAdmnN2RxmitCount_Type()
)
lapbAdmnN2RxmitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnN2RxmitCount.setStatus("mandatory")


class _LapbAdmnT1AckTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT1AckTimer based on PositiveInteger"""
    defaultValue = 3000


_LapbAdmnT1AckTimer_Object = MibTableColumn
lapbAdmnT1AckTimer = _LapbAdmnT1AckTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 9),
    _LapbAdmnT1AckTimer_Type()
)
lapbAdmnT1AckTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT1AckTimer.setStatus("mandatory")


class _LapbAdmnT2AckDelayTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT2AckDelayTimer based on PositiveInteger"""
    defaultValue = 0


_LapbAdmnT2AckDelayTimer_Object = MibTableColumn
lapbAdmnT2AckDelayTimer = _LapbAdmnT2AckDelayTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 10),
    _LapbAdmnT2AckDelayTimer_Type()
)
lapbAdmnT2AckDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT2AckDelayTimer.setStatus("mandatory")


class _LapbAdmnT3DisconnectTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT3DisconnectTimer based on PositiveInteger"""
    defaultValue = 60000


_LapbAdmnT3DisconnectTimer_Object = MibTableColumn
lapbAdmnT3DisconnectTimer = _LapbAdmnT3DisconnectTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 11),
    _LapbAdmnT3DisconnectTimer_Type()
)
lapbAdmnT3DisconnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT3DisconnectTimer.setStatus("mandatory")


class _LapbAdmnT4IdleTimer_Type(PositiveInteger):
    """Custom type lapbAdmnT4IdleTimer based on PositiveInteger"""
    defaultValue = 2147483647


_LapbAdmnT4IdleTimer_Object = MibTableColumn
lapbAdmnT4IdleTimer = _LapbAdmnT4IdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 12),
    _LapbAdmnT4IdleTimer_Type()
)
lapbAdmnT4IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnT4IdleTimer.setStatus("mandatory")


class _LapbAdmnActionInitiate_Type(Integer32):
    """Custom type lapbAdmnActionInitiate based on Integer32"""
    defaultValue = 1

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
        *(("none", 4),
          ("other", 5),
          ("sendDISC", 2),
          ("sendDM", 3),
          ("sendSABM", 1))
    )


_LapbAdmnActionInitiate_Type.__name__ = "Integer32"
_LapbAdmnActionInitiate_Object = MibTableColumn
lapbAdmnActionInitiate = _LapbAdmnActionInitiate_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 13),
    _LapbAdmnActionInitiate_Type()
)
lapbAdmnActionInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnActionInitiate.setStatus("mandatory")


class _LapbAdmnActionRecvDM_Type(Integer32):
    """Custom type lapbAdmnActionRecvDM based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("sendDISC", 2),
          ("sendSABM", 1))
    )


_LapbAdmnActionRecvDM_Type.__name__ = "Integer32"
_LapbAdmnActionRecvDM_Object = MibTableColumn
lapbAdmnActionRecvDM = _LapbAdmnActionRecvDM_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 1, 1, 14),
    _LapbAdmnActionRecvDM_Type()
)
lapbAdmnActionRecvDM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbAdmnActionRecvDM.setStatus("mandatory")
_LapbOperTable_Object = MibTable
lapbOperTable = _LapbOperTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2)
)
if mibBuilder.loadTexts:
    lapbOperTable.setStatus("mandatory")
_LapbOperEntry_Object = MibTableRow
lapbOperEntry = _LapbOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1)
)
lapbOperEntry.setIndexNames(
    (0, "RFC1381-MIB", "lapbOperIndex"),
)
if mibBuilder.loadTexts:
    lapbOperEntry.setStatus("mandatory")
_LapbOperIndex_Type = IfIndexType
_LapbOperIndex_Object = MibTableColumn
lapbOperIndex = _LapbOperIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 1),
    _LapbOperIndex_Type()
)
lapbOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperIndex.setStatus("mandatory")


class _LapbOperStationType_Type(Integer32):
    """Custom type lapbOperStationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1),
          ("dxe", 3))
    )


_LapbOperStationType_Type.__name__ = "Integer32"
_LapbOperStationType_Object = MibTableColumn
lapbOperStationType = _LapbOperStationType_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 2),
    _LapbOperStationType_Type()
)
lapbOperStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperStationType.setStatus("mandatory")


class _LapbOperControlField_Type(Integer32):
    """Custom type lapbOperControlField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modulo128", 2),
          ("modulo8", 1))
    )


_LapbOperControlField_Type.__name__ = "Integer32"
_LapbOperControlField_Object = MibTableColumn
lapbOperControlField = _LapbOperControlField_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 3),
    _LapbOperControlField_Type()
)
lapbOperControlField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperControlField.setStatus("mandatory")
_LapbOperTransmitN1FrameSize_Type = PositiveInteger
_LapbOperTransmitN1FrameSize_Object = MibTableColumn
lapbOperTransmitN1FrameSize = _LapbOperTransmitN1FrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 4),
    _LapbOperTransmitN1FrameSize_Type()
)
lapbOperTransmitN1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperTransmitN1FrameSize.setStatus("mandatory")
_LapbOperReceiveN1FrameSize_Type = PositiveInteger
_LapbOperReceiveN1FrameSize_Object = MibTableColumn
lapbOperReceiveN1FrameSize = _LapbOperReceiveN1FrameSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 5),
    _LapbOperReceiveN1FrameSize_Type()
)
lapbOperReceiveN1FrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperReceiveN1FrameSize.setStatus("mandatory")


class _LapbOperTransmitKWindowSize_Type(Integer32):
    """Custom type lapbOperTransmitKWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbOperTransmitKWindowSize_Type.__name__ = "Integer32"
_LapbOperTransmitKWindowSize_Object = MibTableColumn
lapbOperTransmitKWindowSize = _LapbOperTransmitKWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 6),
    _LapbOperTransmitKWindowSize_Type()
)
lapbOperTransmitKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperTransmitKWindowSize.setStatus("mandatory")


class _LapbOperReceiveKWindowSize_Type(Integer32):
    """Custom type lapbOperReceiveKWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_LapbOperReceiveKWindowSize_Type.__name__ = "Integer32"
_LapbOperReceiveKWindowSize_Object = MibTableColumn
lapbOperReceiveKWindowSize = _LapbOperReceiveKWindowSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 7),
    _LapbOperReceiveKWindowSize_Type()
)
lapbOperReceiveKWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperReceiveKWindowSize.setStatus("mandatory")


class _LapbOperN2RxmitCount_Type(Integer32):
    """Custom type lapbOperN2RxmitCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LapbOperN2RxmitCount_Type.__name__ = "Integer32"
_LapbOperN2RxmitCount_Object = MibTableColumn
lapbOperN2RxmitCount = _LapbOperN2RxmitCount_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 8),
    _LapbOperN2RxmitCount_Type()
)
lapbOperN2RxmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperN2RxmitCount.setStatus("mandatory")
_LapbOperT1AckTimer_Type = PositiveInteger
_LapbOperT1AckTimer_Object = MibTableColumn
lapbOperT1AckTimer = _LapbOperT1AckTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 9),
    _LapbOperT1AckTimer_Type()
)
lapbOperT1AckTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperT1AckTimer.setStatus("mandatory")
_LapbOperT2AckDelayTimer_Type = PositiveInteger
_LapbOperT2AckDelayTimer_Object = MibTableColumn
lapbOperT2AckDelayTimer = _LapbOperT2AckDelayTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 10),
    _LapbOperT2AckDelayTimer_Type()
)
lapbOperT2AckDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperT2AckDelayTimer.setStatus("mandatory")
_LapbOperT3DisconnectTimer_Type = PositiveInteger
_LapbOperT3DisconnectTimer_Object = MibTableColumn
lapbOperT3DisconnectTimer = _LapbOperT3DisconnectTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 11),
    _LapbOperT3DisconnectTimer_Type()
)
lapbOperT3DisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperT3DisconnectTimer.setStatus("mandatory")
_LapbOperT4IdleTimer_Type = PositiveInteger
_LapbOperT4IdleTimer_Object = MibTableColumn
lapbOperT4IdleTimer = _LapbOperT4IdleTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 12),
    _LapbOperT4IdleTimer_Type()
)
lapbOperT4IdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbOperT4IdleTimer.setStatus("mandatory")
_LapbOperPortId_Type = ObjectIdentifier
_LapbOperPortId_Object = MibTableColumn
lapbOperPortId = _LapbOperPortId_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 13),
    _LapbOperPortId_Type()
)
lapbOperPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperPortId.setStatus("mandatory")
_LapbOperProtocolVersionId_Type = ObjectIdentifier
_LapbOperProtocolVersionId_Object = MibTableColumn
lapbOperProtocolVersionId = _LapbOperProtocolVersionId_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 2, 1, 14),
    _LapbOperProtocolVersionId_Type()
)
lapbOperProtocolVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbOperProtocolVersionId.setStatus("mandatory")
_LapbFlowTable_Object = MibTable
lapbFlowTable = _LapbFlowTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3)
)
if mibBuilder.loadTexts:
    lapbFlowTable.setStatus("mandatory")
_LapbFlowEntry_Object = MibTableRow
lapbFlowEntry = _LapbFlowEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1)
)
lapbFlowEntry.setIndexNames(
    (0, "RFC1381-MIB", "lapbFlowIfIndex"),
)
if mibBuilder.loadTexts:
    lapbFlowEntry.setStatus("mandatory")
_LapbFlowIfIndex_Type = IfIndexType
_LapbFlowIfIndex_Object = MibTableColumn
lapbFlowIfIndex = _LapbFlowIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 1),
    _LapbFlowIfIndex_Type()
)
lapbFlowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowIfIndex.setStatus("mandatory")
_LapbFlowStateChanges_Type = Counter32
_LapbFlowStateChanges_Object = MibTableColumn
lapbFlowStateChanges = _LapbFlowStateChanges_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 2),
    _LapbFlowStateChanges_Type()
)
lapbFlowStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowStateChanges.setStatus("mandatory")


class _LapbFlowChangeReason_Type(Integer32):
    """Custom type lapbFlowChangeReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("abmEntered", 2),
          ("abmReset", 4),
          ("abmeEntered", 3),
          ("abmeReset", 5),
          ("discReceived", 8),
          ("discSent", 9),
          ("dmReceived", 6),
          ("dmSent", 7),
          ("frmrReceived", 10),
          ("frmrSent", 11),
          ("n2Timeout", 12),
          ("notStarted", 1),
          ("other", 13))
    )


_LapbFlowChangeReason_Type.__name__ = "Integer32"
_LapbFlowChangeReason_Object = MibTableColumn
lapbFlowChangeReason = _LapbFlowChangeReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 3),
    _LapbFlowChangeReason_Type()
)
lapbFlowChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowChangeReason.setStatus("mandatory")


class _LapbFlowCurrentMode_Type(Integer32):
    """Custom type lapbFlowCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("bothStationsBusy", 10),
          ("disconnectRequest", 4),
          ("disconnected", 1),
          ("error", 16),
          ("frameReject", 3),
          ("informationTransfer", 5),
          ("linkSetup", 2),
          ("other", 17),
          ("rejFrameSent", 6),
          ("rejFrameSentRemoteBusy", 14),
          ("remoteStationBusy", 9),
          ("stationBusy", 8),
          ("waitingAckBothBusy", 13),
          ("waitingAckRemoteBusy", 12),
          ("waitingAckStationBusy", 11),
          ("waitingAcknowledgement", 7),
          ("xidFrameSent", 15))
    )


_LapbFlowCurrentMode_Type.__name__ = "Integer32"
_LapbFlowCurrentMode_Object = MibTableColumn
lapbFlowCurrentMode = _LapbFlowCurrentMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 4),
    _LapbFlowCurrentMode_Type()
)
lapbFlowCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowCurrentMode.setStatus("mandatory")
_LapbFlowBusyDefers_Type = Counter32
_LapbFlowBusyDefers_Object = MibTableColumn
lapbFlowBusyDefers = _LapbFlowBusyDefers_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 5),
    _LapbFlowBusyDefers_Type()
)
lapbFlowBusyDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowBusyDefers.setStatus("mandatory")
_LapbFlowRejOutPkts_Type = Counter32
_LapbFlowRejOutPkts_Object = MibTableColumn
lapbFlowRejOutPkts = _LapbFlowRejOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 6),
    _LapbFlowRejOutPkts_Type()
)
lapbFlowRejOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowRejOutPkts.setStatus("mandatory")
_LapbFlowRejInPkts_Type = Counter32
_LapbFlowRejInPkts_Object = MibTableColumn
lapbFlowRejInPkts = _LapbFlowRejInPkts_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 7),
    _LapbFlowRejInPkts_Type()
)
lapbFlowRejInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowRejInPkts.setStatus("mandatory")
_LapbFlowT1Timeouts_Type = Counter32
_LapbFlowT1Timeouts_Object = MibTableColumn
lapbFlowT1Timeouts = _LapbFlowT1Timeouts_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 8),
    _LapbFlowT1Timeouts_Type()
)
lapbFlowT1Timeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowT1Timeouts.setStatus("mandatory")


class _LapbFlowFrmrSent_Type(OctetString):
    """Custom type lapbFlowFrmrSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_LapbFlowFrmrSent_Type.__name__ = "OctetString"
_LapbFlowFrmrSent_Object = MibTableColumn
lapbFlowFrmrSent = _LapbFlowFrmrSent_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 9),
    _LapbFlowFrmrSent_Type()
)
lapbFlowFrmrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowFrmrSent.setStatus("mandatory")


class _LapbFlowFrmrReceived_Type(OctetString):
    """Custom type lapbFlowFrmrReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_LapbFlowFrmrReceived_Type.__name__ = "OctetString"
_LapbFlowFrmrReceived_Object = MibTableColumn
lapbFlowFrmrReceived = _LapbFlowFrmrReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 10),
    _LapbFlowFrmrReceived_Type()
)
lapbFlowFrmrReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowFrmrReceived.setStatus("mandatory")


class _LapbFlowXidReceived_Type(OctetString):
    """Custom type lapbFlowXidReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8206),
    )


_LapbFlowXidReceived_Type.__name__ = "OctetString"
_LapbFlowXidReceived_Object = MibTableColumn
lapbFlowXidReceived = _LapbFlowXidReceived_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 3, 1, 11),
    _LapbFlowXidReceived_Type()
)
lapbFlowXidReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbFlowXidReceived.setStatus("mandatory")
_LapbXidTable_Object = MibTable
lapbXidTable = _LapbXidTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4)
)
if mibBuilder.loadTexts:
    lapbXidTable.setStatus("mandatory")
_LapbXidEntry_Object = MibTableRow
lapbXidEntry = _LapbXidEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1)
)
lapbXidEntry.setIndexNames(
    (0, "RFC1381-MIB", "lapbXidIndex"),
)
if mibBuilder.loadTexts:
    lapbXidEntry.setStatus("mandatory")
_LapbXidIndex_Type = IfIndexType
_LapbXidIndex_Object = MibTableColumn
lapbXidIndex = _LapbXidIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 1),
    _LapbXidIndex_Type()
)
lapbXidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbXidIndex.setStatus("mandatory")


class _LapbXidAdRIdentifier_Type(OctetString):
    """Custom type lapbXidAdRIdentifier based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LapbXidAdRIdentifier_Type.__name__ = "OctetString"
_LapbXidAdRIdentifier_Object = MibTableColumn
lapbXidAdRIdentifier = _LapbXidAdRIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 2),
    _LapbXidAdRIdentifier_Type()
)
lapbXidAdRIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbXidAdRIdentifier.setStatus("mandatory")


class _LapbXidAdRAddress_Type(OctetString):
    """Custom type lapbXidAdRAddress based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LapbXidAdRAddress_Type.__name__ = "OctetString"
_LapbXidAdRAddress_Object = MibTableColumn
lapbXidAdRAddress = _LapbXidAdRAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 3),
    _LapbXidAdRAddress_Type()
)
lapbXidAdRAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbXidAdRAddress.setStatus("mandatory")


class _LapbXidParameterUniqueIdentifier_Type(OctetString):
    """Custom type lapbXidParameterUniqueIdentifier based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LapbXidParameterUniqueIdentifier_Type.__name__ = "OctetString"
_LapbXidParameterUniqueIdentifier_Object = MibTableColumn
lapbXidParameterUniqueIdentifier = _LapbXidParameterUniqueIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 4),
    _LapbXidParameterUniqueIdentifier_Type()
)
lapbXidParameterUniqueIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbXidParameterUniqueIdentifier.setStatus("mandatory")


class _LapbXidGroupAddress_Type(OctetString):
    """Custom type lapbXidGroupAddress based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LapbXidGroupAddress_Type.__name__ = "OctetString"
_LapbXidGroupAddress_Object = MibTableColumn
lapbXidGroupAddress = _LapbXidGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 5),
    _LapbXidGroupAddress_Type()
)
lapbXidGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbXidGroupAddress.setStatus("mandatory")


class _LapbXidPortNumber_Type(OctetString):
    """Custom type lapbXidPortNumber based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LapbXidPortNumber_Type.__name__ = "OctetString"
_LapbXidPortNumber_Object = MibTableColumn
lapbXidPortNumber = _LapbXidPortNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 6),
    _LapbXidPortNumber_Type()
)
lapbXidPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbXidPortNumber.setStatus("mandatory")


class _LapbXidUserDataSubfield_Type(OctetString):
    """Custom type lapbXidUserDataSubfield based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8206),
    )


_LapbXidUserDataSubfield_Type.__name__ = "OctetString"
_LapbXidUserDataSubfield_Object = MibTableColumn
lapbXidUserDataSubfield = _LapbXidUserDataSubfield_Object(
    (1, 3, 6, 1, 2, 1, 10, 16, 4, 1, 7),
    _LapbXidUserDataSubfield_Type()
)
lapbXidUserDataSubfield.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbXidUserDataSubfield.setStatus("mandatory")
_LapbProtocolVersion_ObjectIdentity = ObjectIdentity
lapbProtocolVersion = _LapbProtocolVersion_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 16, 5)
)
_LapbProtocolIso7776v1986_ObjectIdentity = ObjectIdentity
lapbProtocolIso7776v1986 = _LapbProtocolIso7776v1986_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 16, 5, 1)
)
_LapbProtocolCcittV1980_ObjectIdentity = ObjectIdentity
lapbProtocolCcittV1980 = _LapbProtocolCcittV1980_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 16, 5, 2)
)
_LapbProtocolCcittV1984_ObjectIdentity = ObjectIdentity
lapbProtocolCcittV1984 = _LapbProtocolCcittV1984_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 16, 5, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1381-MIB",
    **{"IfIndexType": IfIndexType,
       "lapb": lapb,
       "lapbAdmnTable": lapbAdmnTable,
       "lapbAdmnEntry": lapbAdmnEntry,
       "lapbAdmnIndex": lapbAdmnIndex,
       "lapbAdmnStationType": lapbAdmnStationType,
       "lapbAdmnControlField": lapbAdmnControlField,
       "lapbAdmnTransmitN1FrameSize": lapbAdmnTransmitN1FrameSize,
       "lapbAdmnReceiveN1FrameSize": lapbAdmnReceiveN1FrameSize,
       "lapbAdmnTransmitKWindowSize": lapbAdmnTransmitKWindowSize,
       "lapbAdmnReceiveKWindowSize": lapbAdmnReceiveKWindowSize,
       "lapbAdmnN2RxmitCount": lapbAdmnN2RxmitCount,
       "lapbAdmnT1AckTimer": lapbAdmnT1AckTimer,
       "lapbAdmnT2AckDelayTimer": lapbAdmnT2AckDelayTimer,
       "lapbAdmnT3DisconnectTimer": lapbAdmnT3DisconnectTimer,
       "lapbAdmnT4IdleTimer": lapbAdmnT4IdleTimer,
       "lapbAdmnActionInitiate": lapbAdmnActionInitiate,
       "lapbAdmnActionRecvDM": lapbAdmnActionRecvDM,
       "lapbOperTable": lapbOperTable,
       "lapbOperEntry": lapbOperEntry,
       "lapbOperIndex": lapbOperIndex,
       "lapbOperStationType": lapbOperStationType,
       "lapbOperControlField": lapbOperControlField,
       "lapbOperTransmitN1FrameSize": lapbOperTransmitN1FrameSize,
       "lapbOperReceiveN1FrameSize": lapbOperReceiveN1FrameSize,
       "lapbOperTransmitKWindowSize": lapbOperTransmitKWindowSize,
       "lapbOperReceiveKWindowSize": lapbOperReceiveKWindowSize,
       "lapbOperN2RxmitCount": lapbOperN2RxmitCount,
       "lapbOperT1AckTimer": lapbOperT1AckTimer,
       "lapbOperT2AckDelayTimer": lapbOperT2AckDelayTimer,
       "lapbOperT3DisconnectTimer": lapbOperT3DisconnectTimer,
       "lapbOperT4IdleTimer": lapbOperT4IdleTimer,
       "lapbOperPortId": lapbOperPortId,
       "lapbOperProtocolVersionId": lapbOperProtocolVersionId,
       "lapbFlowTable": lapbFlowTable,
       "lapbFlowEntry": lapbFlowEntry,
       "lapbFlowIfIndex": lapbFlowIfIndex,
       "lapbFlowStateChanges": lapbFlowStateChanges,
       "lapbFlowChangeReason": lapbFlowChangeReason,
       "lapbFlowCurrentMode": lapbFlowCurrentMode,
       "lapbFlowBusyDefers": lapbFlowBusyDefers,
       "lapbFlowRejOutPkts": lapbFlowRejOutPkts,
       "lapbFlowRejInPkts": lapbFlowRejInPkts,
       "lapbFlowT1Timeouts": lapbFlowT1Timeouts,
       "lapbFlowFrmrSent": lapbFlowFrmrSent,
       "lapbFlowFrmrReceived": lapbFlowFrmrReceived,
       "lapbFlowXidReceived": lapbFlowXidReceived,
       "lapbXidTable": lapbXidTable,
       "lapbXidEntry": lapbXidEntry,
       "lapbXidIndex": lapbXidIndex,
       "lapbXidAdRIdentifier": lapbXidAdRIdentifier,
       "lapbXidAdRAddress": lapbXidAdRAddress,
       "lapbXidParameterUniqueIdentifier": lapbXidParameterUniqueIdentifier,
       "lapbXidGroupAddress": lapbXidGroupAddress,
       "lapbXidPortNumber": lapbXidPortNumber,
       "lapbXidUserDataSubfield": lapbXidUserDataSubfield,
       "lapbProtocolVersion": lapbProtocolVersion,
       "lapbProtocolIso7776v1986": lapbProtocolIso7776v1986,
       "lapbProtocolCcittV1980": lapbProtocolCcittV1980,
       "lapbProtocolCcittV1984": lapbProtocolCcittV1984}
)
