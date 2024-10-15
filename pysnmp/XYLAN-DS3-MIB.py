# SNMP MIB module (XYLAN-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-DS3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:00 2024
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

(xylanPportArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanPportArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx3Port_ObjectIdentity = ObjectIdentity
dsx3Port = _Dsx3Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2)
)
_Dsx3PortConfigTable_Object = MibTable
dsx3PortConfigTable = _Dsx3PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    dsx3PortConfigTable.setStatus("mandatory")
_Dsx3PortConfigEntry_Object = MibTableRow
dsx3PortConfigEntry = _Dsx3PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1)
)
dsx3PortConfigEntry.setIndexNames(
    (0, "XYLAN-DS3-MIB", "dsx3PortConfigSlotIndex"),
    (0, "XYLAN-DS3-MIB", "dsx3PortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    dsx3PortConfigEntry.setStatus("mandatory")


class _Dsx3PortConfigSlotIndex_Type(Integer32):
    """Custom type dsx3PortConfigSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Dsx3PortConfigSlotIndex_Type.__name__ = "Integer32"
_Dsx3PortConfigSlotIndex_Object = MibTableColumn
dsx3PortConfigSlotIndex = _Dsx3PortConfigSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 1),
    _Dsx3PortConfigSlotIndex_Type()
)
dsx3PortConfigSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigSlotIndex.setStatus("mandatory")


class _Dsx3PortConfigPortIndex_Type(Integer32):
    """Custom type dsx3PortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Dsx3PortConfigPortIndex_Type.__name__ = "Integer32"
_Dsx3PortConfigPortIndex_Object = MibTableColumn
dsx3PortConfigPortIndex = _Dsx3PortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 2),
    _Dsx3PortConfigPortIndex_Type()
)
dsx3PortConfigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigPortIndex.setStatus("mandatory")


class _Dsx3PortConfigIfType_Type(Integer32):
    """Custom type dsx3PortConfigIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ds3", 1),
          ("e3", 2))
    )


_Dsx3PortConfigIfType_Type.__name__ = "Integer32"
_Dsx3PortConfigIfType_Object = MibTableColumn
dsx3PortConfigIfType = _Dsx3PortConfigIfType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 3),
    _Dsx3PortConfigIfType_Type()
)
dsx3PortConfigIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigIfType.setStatus("mandatory")


class _Dsx3PortConfigTcSubLayer_Type(Integer32):
    """Custom type dsx3PortConfigTcSubLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adm", 3),
          ("none", 1),
          ("plcp", 2))
    )


_Dsx3PortConfigTcSubLayer_Type.__name__ = "Integer32"
_Dsx3PortConfigTcSubLayer_Object = MibTableColumn
dsx3PortConfigTcSubLayer = _Dsx3PortConfigTcSubLayer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 4),
    _Dsx3PortConfigTcSubLayer_Type()
)
dsx3PortConfigTcSubLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PortConfigTcSubLayer.setStatus("mandatory")


class _Dsx3PortConfigPlcpStatus_Type(Integer32):
    """Custom type dsx3PortConfigPlcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Dsx3PortConfigPlcpStatus_Type.__name__ = "Integer32"
_Dsx3PortConfigPlcpStatus_Object = MibTableColumn
dsx3PortConfigPlcpStatus = _Dsx3PortConfigPlcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 5),
    _Dsx3PortConfigPlcpStatus_Type()
)
dsx3PortConfigPlcpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigPlcpStatus.setStatus("mandatory")


class _Dsx3PortConfigFEAC_Type(Integer32):
    """Custom type dsx3PortConfigFEAC based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dsx3CommonEquipmentFailure", 8),
          ("dsx3DS1NonServiceAffectingEquipFailure", 11),
          ("dsx3DS1ServiceAffectingEquipmentFailure", 10),
          ("dsx3DS3AISreceived", 5),
          ("dsx3DS3EquipmentFailure", 2),
          ("dsx3DS3IDLEreceived", 6),
          ("dsx3DS3LOS", 3),
          ("dsx3DS3LoopbackReceived", 9),
          ("dsx3DS3NonServiceAffectingEquipFailure", 7),
          ("dsx3DS3OutofFrame", 4),
          ("dsx3MultipleDS1sLOS", 13),
          ("dsx3NoFEAC", 1),
          ("dsx3SingleDS1LOS", 12),
          ("dsx3UnknownCode", 14),
          ("dsx3UnsupportedCode", 15))
    )


_Dsx3PortConfigFEAC_Type.__name__ = "Integer32"
_Dsx3PortConfigFEAC_Object = MibTableColumn
dsx3PortConfigFEAC = _Dsx3PortConfigFEAC_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 6),
    _Dsx3PortConfigFEAC_Type()
)
dsx3PortConfigFEAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigFEAC.setStatus("mandatory")


class _Dsx3PortConfigNatUse_Type(Integer32):
    """Custom type dsx3PortConfigNatUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("zero", 2))
    )


_Dsx3PortConfigNatUse_Type.__name__ = "Integer32"
_Dsx3PortConfigNatUse_Object = MibTableColumn
dsx3PortConfigNatUse = _Dsx3PortConfigNatUse_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 7),
    _Dsx3PortConfigNatUse_Type()
)
dsx3PortConfigNatUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigNatUse.setStatus("mandatory")


class _Dsx3PortConfigRxPayloadType_Type(Integer32):
    """Custom type dsx3PortConfigRxPayloadType based on Integer32"""
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
        *(("atm", 3),
          ("equipped-non-specific", 4),
          ("sdh-tu-12s", 5),
          ("unequipped", 2),
          ("unknown-or-not-applicable", 1))
    )


_Dsx3PortConfigRxPayloadType_Type.__name__ = "Integer32"
_Dsx3PortConfigRxPayloadType_Object = MibTableColumn
dsx3PortConfigRxPayloadType = _Dsx3PortConfigRxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 8),
    _Dsx3PortConfigRxPayloadType_Type()
)
dsx3PortConfigRxPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigRxPayloadType.setStatus("mandatory")


class _Dsx3PortConfigTimeMarker_Type(Integer32):
    """Custom type dsx3PortConfigTimeMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("zero", 2))
    )


_Dsx3PortConfigTimeMarker_Type.__name__ = "Integer32"
_Dsx3PortConfigTimeMarker_Object = MibTableColumn
dsx3PortConfigTimeMarker = _Dsx3PortConfigTimeMarker_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 9),
    _Dsx3PortConfigTimeMarker_Type()
)
dsx3PortConfigTimeMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigTimeMarker.setStatus("mandatory")


class _Dsx3PortConfigTxPayloadType_Type(Integer32):
    """Custom type dsx3PortConfigTxPayloadType based on Integer32"""
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
        *(("atm", 2),
          ("equipped-non-specific", 3),
          ("sdh-tu-12s", 4),
          ("unequipped", 1))
    )


_Dsx3PortConfigTxPayloadType_Type.__name__ = "Integer32"
_Dsx3PortConfigTxPayloadType_Object = MibTableColumn
dsx3PortConfigTxPayloadType = _Dsx3PortConfigTxPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 10),
    _Dsx3PortConfigTxPayloadType_Type()
)
dsx3PortConfigTxPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PortConfigTxPayloadType.setStatus("mandatory")


class _Dsx3PortConfigExpectedPayloadType_Type(Integer32):
    """Custom type dsx3PortConfigExpectedPayloadType based on Integer32"""
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
        *(("atm", 2),
          ("equipped-non-specific", 3),
          ("sdh-tu-12s", 4),
          ("unequipped", 1))
    )


_Dsx3PortConfigExpectedPayloadType_Type.__name__ = "Integer32"
_Dsx3PortConfigExpectedPayloadType_Object = MibTableColumn
dsx3PortConfigExpectedPayloadType = _Dsx3PortConfigExpectedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 11),
    _Dsx3PortConfigExpectedPayloadType_Type()
)
dsx3PortConfigExpectedPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PortConfigExpectedPayloadType.setStatus("mandatory")


class _Dsx3PortConfigTxTrailTraceID_Type(DisplayString):
    """Custom type dsx3PortConfigTxTrailTraceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Dsx3PortConfigTxTrailTraceID_Type.__name__ = "DisplayString"
_Dsx3PortConfigTxTrailTraceID_Object = MibTableColumn
dsx3PortConfigTxTrailTraceID = _Dsx3PortConfigTxTrailTraceID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 12),
    _Dsx3PortConfigTxTrailTraceID_Type()
)
dsx3PortConfigTxTrailTraceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PortConfigTxTrailTraceID.setStatus("mandatory")


class _Dsx3PortConfigRxTrailTraceID_Type(DisplayString):
    """Custom type dsx3PortConfigRxTrailTraceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Dsx3PortConfigRxTrailTraceID_Type.__name__ = "DisplayString"
_Dsx3PortConfigRxTrailTraceID_Object = MibTableColumn
dsx3PortConfigRxTrailTraceID = _Dsx3PortConfigRxTrailTraceID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 13),
    _Dsx3PortConfigRxTrailTraceID_Type()
)
dsx3PortConfigRxTrailTraceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigRxTrailTraceID.setStatus("mandatory")


class _Dsx3PortConfigExpectedTrailTraceID_Type(DisplayString):
    """Custom type dsx3PortConfigExpectedTrailTraceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Dsx3PortConfigExpectedTrailTraceID_Type.__name__ = "DisplayString"
_Dsx3PortConfigExpectedTrailTraceID_Object = MibTableColumn
dsx3PortConfigExpectedTrailTraceID = _Dsx3PortConfigExpectedTrailTraceID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 14),
    _Dsx3PortConfigExpectedTrailTraceID_Type()
)
dsx3PortConfigExpectedTrailTraceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PortConfigExpectedTrailTraceID.setStatus("mandatory")


class _Dsx3PortConfigLineStatus_Type(Integer32):
    """Custom type dsx3PortConfigLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2097151),
    )


_Dsx3PortConfigLineStatus_Type.__name__ = "Integer32"
_Dsx3PortConfigLineStatus_Object = MibTableColumn
dsx3PortConfigLineStatus = _Dsx3PortConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 15),
    _Dsx3PortConfigLineStatus_Type()
)
dsx3PortConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortConfigLineStatus.setStatus("mandatory")


class _Dsx3PortConfigPlScramble_Type(Integer32):
    """Custom type dsx3PortConfigPlScramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_Dsx3PortConfigPlScramble_Type.__name__ = "Integer32"
_Dsx3PortConfigPlScramble_Object = MibTableColumn
dsx3PortConfigPlScramble = _Dsx3PortConfigPlScramble_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 1, 1, 16),
    _Dsx3PortConfigPlScramble_Type()
)
dsx3PortConfigPlScramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PortConfigPlScramble.setStatus("mandatory")
_Dsx3PortStatsTable_Object = MibTable
dsx3PortStatsTable = _Dsx3PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2)
)
if mibBuilder.loadTexts:
    dsx3PortStatsTable.setStatus("mandatory")
_Dsx3PortStatsEntry_Object = MibTableRow
dsx3PortStatsEntry = _Dsx3PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1)
)
dsx3PortStatsEntry.setIndexNames(
    (0, "XYLAN-DS3-MIB", "dsx3PortStatsSlotIndex"),
    (0, "XYLAN-DS3-MIB", "dsx3PortStatsPortIndex"),
)
if mibBuilder.loadTexts:
    dsx3PortStatsEntry.setStatus("mandatory")


class _Dsx3PortStatsSlotIndex_Type(Integer32):
    """Custom type dsx3PortStatsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Dsx3PortStatsSlotIndex_Type.__name__ = "Integer32"
_Dsx3PortStatsSlotIndex_Object = MibTableColumn
dsx3PortStatsSlotIndex = _Dsx3PortStatsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 1),
    _Dsx3PortStatsSlotIndex_Type()
)
dsx3PortStatsSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsSlotIndex.setStatus("mandatory")


class _Dsx3PortStatsPortIndex_Type(Integer32):
    """Custom type dsx3PortStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Dsx3PortStatsPortIndex_Type.__name__ = "Integer32"
_Dsx3PortStatsPortIndex_Object = MibTableColumn
dsx3PortStatsPortIndex = _Dsx3PortStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 2),
    _Dsx3PortStatsPortIndex_Type()
)
dsx3PortStatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPortIndex.setStatus("mandatory")
_Dsx3PortStatsLossOfSignal_Type = Counter32
_Dsx3PortStatsLossOfSignal_Object = MibTableColumn
dsx3PortStatsLossOfSignal = _Dsx3PortStatsLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 3),
    _Dsx3PortStatsLossOfSignal_Type()
)
dsx3PortStatsLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsLossOfSignal.setStatus("mandatory")
_Dsx3PortStatsOutOfFrame_Type = Counter32
_Dsx3PortStatsOutOfFrame_Object = MibTableColumn
dsx3PortStatsOutOfFrame = _Dsx3PortStatsOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 4),
    _Dsx3PortStatsOutOfFrame_Type()
)
dsx3PortStatsOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsOutOfFrame.setStatus("mandatory")
_Dsx3PortStatsAISEvent_Type = Counter32
_Dsx3PortStatsAISEvent_Object = MibTableColumn
dsx3PortStatsAISEvent = _Dsx3PortStatsAISEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 5),
    _Dsx3PortStatsAISEvent_Type()
)
dsx3PortStatsAISEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsAISEvent.setStatus("mandatory")
_Dsx3PortStatsRedAlarmEvent_Type = Counter32
_Dsx3PortStatsRedAlarmEvent_Object = MibTableColumn
dsx3PortStatsRedAlarmEvent = _Dsx3PortStatsRedAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 6),
    _Dsx3PortStatsRedAlarmEvent_Type()
)
dsx3PortStatsRedAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsRedAlarmEvent.setStatus("mandatory")
_Dsx3PortStatsFarEndReceiveError_Type = Counter32
_Dsx3PortStatsFarEndReceiveError_Object = MibTableColumn
dsx3PortStatsFarEndReceiveError = _Dsx3PortStatsFarEndReceiveError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 7),
    _Dsx3PortStatsFarEndReceiveError_Type()
)
dsx3PortStatsFarEndReceiveError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsFarEndReceiveError.setStatus("mandatory")
_Dsx3PortStatsFarEndBlkError_Type = Counter32
_Dsx3PortStatsFarEndBlkError_Object = MibTableColumn
dsx3PortStatsFarEndBlkError = _Dsx3PortStatsFarEndBlkError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 8),
    _Dsx3PortStatsFarEndBlkError_Type()
)
dsx3PortStatsFarEndBlkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsFarEndBlkError.setStatus("mandatory")
_Dsx3PortStatsLineCodeVioEvent_Type = Counter32
_Dsx3PortStatsLineCodeVioEvent_Object = MibTableColumn
dsx3PortStatsLineCodeVioEvent = _Dsx3PortStatsLineCodeVioEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 9),
    _Dsx3PortStatsLineCodeVioEvent_Type()
)
dsx3PortStatsLineCodeVioEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsLineCodeVioEvent.setStatus("mandatory")
_Dsx3PortStatsFramingBitError_Type = Counter32
_Dsx3PortStatsFramingBitError_Object = MibTableColumn
dsx3PortStatsFramingBitError = _Dsx3PortStatsFramingBitError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 10),
    _Dsx3PortStatsFramingBitError_Type()
)
dsx3PortStatsFramingBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsFramingBitError.setStatus("mandatory")
_Dsx3PortStatsChangeOfFrameAlign_Type = Counter32
_Dsx3PortStatsChangeOfFrameAlign_Object = MibTableColumn
dsx3PortStatsChangeOfFrameAlign = _Dsx3PortStatsChangeOfFrameAlign_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 11),
    _Dsx3PortStatsChangeOfFrameAlign_Type()
)
dsx3PortStatsChangeOfFrameAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsChangeOfFrameAlign.setStatus("mandatory")
_Dsx3PortStatsParityBitError_Type = Counter32
_Dsx3PortStatsParityBitError_Object = MibTableColumn
dsx3PortStatsParityBitError = _Dsx3PortStatsParityBitError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 12),
    _Dsx3PortStatsParityBitError_Type()
)
dsx3PortStatsParityBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsParityBitError.setStatus("mandatory")
_Dsx3PortStatsPathParityBitError_Type = Counter32
_Dsx3PortStatsPathParityBitError_Object = MibTableColumn
dsx3PortStatsPathParityBitError = _Dsx3PortStatsPathParityBitError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 13),
    _Dsx3PortStatsPathParityBitError_Type()
)
dsx3PortStatsPathParityBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPathParityBitError.setStatus("mandatory")
_Dsx3PortStatsPlcpLossOfFrame_Type = Counter32
_Dsx3PortStatsPlcpLossOfFrame_Object = MibTableColumn
dsx3PortStatsPlcpLossOfFrame = _Dsx3PortStatsPlcpLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 14),
    _Dsx3PortStatsPlcpLossOfFrame_Type()
)
dsx3PortStatsPlcpLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPlcpLossOfFrame.setStatus("mandatory")
_Dsx3PortStatsPlcpOutOfFrame_Type = Counter32
_Dsx3PortStatsPlcpOutOfFrame_Object = MibTableColumn
dsx3PortStatsPlcpOutOfFrame = _Dsx3PortStatsPlcpOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 15),
    _Dsx3PortStatsPlcpOutOfFrame_Type()
)
dsx3PortStatsPlcpOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPlcpOutOfFrame.setStatus("mandatory")
_Dsx3PortStatsPlcpYellowAlarm_Type = Counter32
_Dsx3PortStatsPlcpYellowAlarm_Object = MibTableColumn
dsx3PortStatsPlcpYellowAlarm = _Dsx3PortStatsPlcpYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 16),
    _Dsx3PortStatsPlcpYellowAlarm_Type()
)
dsx3PortStatsPlcpYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPlcpYellowAlarm.setStatus("mandatory")
_Dsx3PortStatsPlcpFarEndBlkError_Type = Counter32
_Dsx3PortStatsPlcpFarEndBlkError_Object = MibTableColumn
dsx3PortStatsPlcpFarEndBlkError = _Dsx3PortStatsPlcpFarEndBlkError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 17),
    _Dsx3PortStatsPlcpFarEndBlkError_Type()
)
dsx3PortStatsPlcpFarEndBlkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPlcpFarEndBlkError.setStatus("mandatory")
_Dsx3PortStatsPlcpFramingError_Type = Counter32
_Dsx3PortStatsPlcpFramingError_Object = MibTableColumn
dsx3PortStatsPlcpFramingError = _Dsx3PortStatsPlcpFramingError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 18),
    _Dsx3PortStatsPlcpFramingError_Type()
)
dsx3PortStatsPlcpFramingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPlcpFramingError.setStatus("mandatory")
_Dsx3PortStatsPlcpBIPError_Type = Counter32
_Dsx3PortStatsPlcpBIPError_Object = MibTableColumn
dsx3PortStatsPlcpBIPError = _Dsx3PortStatsPlcpBIPError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 19),
    _Dsx3PortStatsPlcpBIPError_Type()
)
dsx3PortStatsPlcpBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPlcpBIPError.setStatus("mandatory")
_Dsx3PortStatsPayloadTypeMismatchError_Type = Counter32
_Dsx3PortStatsPayloadTypeMismatchError_Object = MibTableColumn
dsx3PortStatsPayloadTypeMismatchError = _Dsx3PortStatsPayloadTypeMismatchError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 20),
    _Dsx3PortStatsPayloadTypeMismatchError_Type()
)
dsx3PortStatsPayloadTypeMismatchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsPayloadTypeMismatchError.setStatus("mandatory")
_Dsx3PortStatsUnequippedError_Type = Counter32
_Dsx3PortStatsUnequippedError_Object = MibTableColumn
dsx3PortStatsUnequippedError = _Dsx3PortStatsUnequippedError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 21),
    _Dsx3PortStatsUnequippedError_Type()
)
dsx3PortStatsUnequippedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsUnequippedError.setStatus("mandatory")
_Dsx3PortStatsTrailTraceIDMismatchError_Type = Counter32
_Dsx3PortStatsTrailTraceIDMismatchError_Object = MibTableColumn
dsx3PortStatsTrailTraceIDMismatchError = _Dsx3PortStatsTrailTraceIDMismatchError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 2, 1, 22),
    _Dsx3PortStatsTrailTraceIDMismatchError_Type()
)
dsx3PortStatsTrailTraceIDMismatchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortStatsTrailTraceIDMismatchError.setStatus("mandatory")
_Dsx3PortIntervalTable_Object = MibTable
dsx3PortIntervalTable = _Dsx3PortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3)
)
if mibBuilder.loadTexts:
    dsx3PortIntervalTable.setStatus("mandatory")
_Dsx3PortIntervalEntry_Object = MibTableRow
dsx3PortIntervalEntry = _Dsx3PortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1)
)
dsx3PortIntervalEntry.setIndexNames(
    (0, "XYLAN-DS3-MIB", "dsx3PortIntervalSlotIndex"),
    (0, "XYLAN-DS3-MIB", "dsx3PortIntervalPortIndex"),
)
if mibBuilder.loadTexts:
    dsx3PortIntervalEntry.setStatus("mandatory")


class _Dsx3PortIntervalSlotIndex_Type(Integer32):
    """Custom type dsx3PortIntervalSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Dsx3PortIntervalSlotIndex_Type.__name__ = "Integer32"
_Dsx3PortIntervalSlotIndex_Object = MibTableColumn
dsx3PortIntervalSlotIndex = _Dsx3PortIntervalSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 1),
    _Dsx3PortIntervalSlotIndex_Type()
)
dsx3PortIntervalSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalSlotIndex.setStatus("mandatory")


class _Dsx3PortIntervalPortIndex_Type(Integer32):
    """Custom type dsx3PortIntervalPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Dsx3PortIntervalPortIndex_Type.__name__ = "Integer32"
_Dsx3PortIntervalPortIndex_Object = MibTableColumn
dsx3PortIntervalPortIndex = _Dsx3PortIntervalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 2),
    _Dsx3PortIntervalPortIndex_Type()
)
dsx3PortIntervalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPortIndex.setStatus("mandatory")


class _Dsx3PortIntervalClear_Type(Integer32):
    """Custom type dsx3PortIntervalClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearRequest", 2),
          ("noAction", 1))
    )


_Dsx3PortIntervalClear_Type.__name__ = "Integer32"
_Dsx3PortIntervalClear_Object = MibTableColumn
dsx3PortIntervalClear = _Dsx3PortIntervalClear_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 3),
    _Dsx3PortIntervalClear_Type()
)
dsx3PortIntervalClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3PortIntervalClear.setStatus("mandatory")
_Dsx3PortIntervalLastClear_Type = TimeTicks
_Dsx3PortIntervalLastClear_Object = MibTableColumn
dsx3PortIntervalLastClear = _Dsx3PortIntervalLastClear_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 4),
    _Dsx3PortIntervalLastClear_Type()
)
dsx3PortIntervalLastClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalLastClear.setStatus("mandatory")
_Dsx3PortIntervalLossOfSignal_Type = Counter32
_Dsx3PortIntervalLossOfSignal_Object = MibTableColumn
dsx3PortIntervalLossOfSignal = _Dsx3PortIntervalLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 5),
    _Dsx3PortIntervalLossOfSignal_Type()
)
dsx3PortIntervalLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalLossOfSignal.setStatus("mandatory")
_Dsx3PortIntervalOutOfFrame_Type = Counter32
_Dsx3PortIntervalOutOfFrame_Object = MibTableColumn
dsx3PortIntervalOutOfFrame = _Dsx3PortIntervalOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 6),
    _Dsx3PortIntervalOutOfFrame_Type()
)
dsx3PortIntervalOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalOutOfFrame.setStatus("mandatory")
_Dsx3PortIntervalAISEvent_Type = Counter32
_Dsx3PortIntervalAISEvent_Object = MibTableColumn
dsx3PortIntervalAISEvent = _Dsx3PortIntervalAISEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 7),
    _Dsx3PortIntervalAISEvent_Type()
)
dsx3PortIntervalAISEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalAISEvent.setStatus("mandatory")
_Dsx3PortIntervalRedAlarmEvent_Type = Counter32
_Dsx3PortIntervalRedAlarmEvent_Object = MibTableColumn
dsx3PortIntervalRedAlarmEvent = _Dsx3PortIntervalRedAlarmEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 8),
    _Dsx3PortIntervalRedAlarmEvent_Type()
)
dsx3PortIntervalRedAlarmEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalRedAlarmEvent.setStatus("mandatory")
_Dsx3PortIntervalFarEndReceiveError_Type = Counter32
_Dsx3PortIntervalFarEndReceiveError_Object = MibTableColumn
dsx3PortIntervalFarEndReceiveError = _Dsx3PortIntervalFarEndReceiveError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 9),
    _Dsx3PortIntervalFarEndReceiveError_Type()
)
dsx3PortIntervalFarEndReceiveError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalFarEndReceiveError.setStatus("mandatory")
_Dsx3PortIntervalFarEndBlkError_Type = Counter32
_Dsx3PortIntervalFarEndBlkError_Object = MibTableColumn
dsx3PortIntervalFarEndBlkError = _Dsx3PortIntervalFarEndBlkError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 10),
    _Dsx3PortIntervalFarEndBlkError_Type()
)
dsx3PortIntervalFarEndBlkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalFarEndBlkError.setStatus("mandatory")
_Dsx3PortIntervalLineCodeVioEvent_Type = Counter32
_Dsx3PortIntervalLineCodeVioEvent_Object = MibTableColumn
dsx3PortIntervalLineCodeVioEvent = _Dsx3PortIntervalLineCodeVioEvent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 11),
    _Dsx3PortIntervalLineCodeVioEvent_Type()
)
dsx3PortIntervalLineCodeVioEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalLineCodeVioEvent.setStatus("mandatory")
_Dsx3PortIntervalFramingBitError_Type = Counter32
_Dsx3PortIntervalFramingBitError_Object = MibTableColumn
dsx3PortIntervalFramingBitError = _Dsx3PortIntervalFramingBitError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 12),
    _Dsx3PortIntervalFramingBitError_Type()
)
dsx3PortIntervalFramingBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalFramingBitError.setStatus("mandatory")
_Dsx3PortIntervalChangeOfFrameAlign_Type = Counter32
_Dsx3PortIntervalChangeOfFrameAlign_Object = MibTableColumn
dsx3PortIntervalChangeOfFrameAlign = _Dsx3PortIntervalChangeOfFrameAlign_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 13),
    _Dsx3PortIntervalChangeOfFrameAlign_Type()
)
dsx3PortIntervalChangeOfFrameAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalChangeOfFrameAlign.setStatus("mandatory")
_Dsx3PortIntervalParityBitError_Type = Counter32
_Dsx3PortIntervalParityBitError_Object = MibTableColumn
dsx3PortIntervalParityBitError = _Dsx3PortIntervalParityBitError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 14),
    _Dsx3PortIntervalParityBitError_Type()
)
dsx3PortIntervalParityBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalParityBitError.setStatus("mandatory")
_Dsx3PortIntervalPathParityBitError_Type = Counter32
_Dsx3PortIntervalPathParityBitError_Object = MibTableColumn
dsx3PortIntervalPathParityBitError = _Dsx3PortIntervalPathParityBitError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 15),
    _Dsx3PortIntervalPathParityBitError_Type()
)
dsx3PortIntervalPathParityBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPathParityBitError.setStatus("mandatory")
_Dsx3PortIntervalPlcpLossOfFrame_Type = Counter32
_Dsx3PortIntervalPlcpLossOfFrame_Object = MibTableColumn
dsx3PortIntervalPlcpLossOfFrame = _Dsx3PortIntervalPlcpLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 16),
    _Dsx3PortIntervalPlcpLossOfFrame_Type()
)
dsx3PortIntervalPlcpLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPlcpLossOfFrame.setStatus("mandatory")
_Dsx3PortIntervalPlcpOutOfFrame_Type = Counter32
_Dsx3PortIntervalPlcpOutOfFrame_Object = MibTableColumn
dsx3PortIntervalPlcpOutOfFrame = _Dsx3PortIntervalPlcpOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 17),
    _Dsx3PortIntervalPlcpOutOfFrame_Type()
)
dsx3PortIntervalPlcpOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPlcpOutOfFrame.setStatus("mandatory")
_Dsx3PortIntervalPlcpYellowAlarm_Type = Counter32
_Dsx3PortIntervalPlcpYellowAlarm_Object = MibTableColumn
dsx3PortIntervalPlcpYellowAlarm = _Dsx3PortIntervalPlcpYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 18),
    _Dsx3PortIntervalPlcpYellowAlarm_Type()
)
dsx3PortIntervalPlcpYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPlcpYellowAlarm.setStatus("mandatory")
_Dsx3PortIntervalPlcpFarEndBlkError_Type = Counter32
_Dsx3PortIntervalPlcpFarEndBlkError_Object = MibTableColumn
dsx3PortIntervalPlcpFarEndBlkError = _Dsx3PortIntervalPlcpFarEndBlkError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 19),
    _Dsx3PortIntervalPlcpFarEndBlkError_Type()
)
dsx3PortIntervalPlcpFarEndBlkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPlcpFarEndBlkError.setStatus("mandatory")
_Dsx3PortIntervalPlcpFramingError_Type = Counter32
_Dsx3PortIntervalPlcpFramingError_Object = MibTableColumn
dsx3PortIntervalPlcpFramingError = _Dsx3PortIntervalPlcpFramingError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 20),
    _Dsx3PortIntervalPlcpFramingError_Type()
)
dsx3PortIntervalPlcpFramingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPlcpFramingError.setStatus("mandatory")
_Dsx3PortIntervalPlcpBIPError_Type = Counter32
_Dsx3PortIntervalPlcpBIPError_Object = MibTableColumn
dsx3PortIntervalPlcpBIPError = _Dsx3PortIntervalPlcpBIPError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 21),
    _Dsx3PortIntervalPlcpBIPError_Type()
)
dsx3PortIntervalPlcpBIPError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPlcpBIPError.setStatus("mandatory")
_Dsx3PortIntervalPayloadTypeMismatchError_Type = Counter32
_Dsx3PortIntervalPayloadTypeMismatchError_Object = MibTableColumn
dsx3PortIntervalPayloadTypeMismatchError = _Dsx3PortIntervalPayloadTypeMismatchError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 22),
    _Dsx3PortIntervalPayloadTypeMismatchError_Type()
)
dsx3PortIntervalPayloadTypeMismatchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalPayloadTypeMismatchError.setStatus("mandatory")
_Dsx3PortIntervalUnequippedError_Type = Counter32
_Dsx3PortIntervalUnequippedError_Object = MibTableColumn
dsx3PortIntervalUnequippedError = _Dsx3PortIntervalUnequippedError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 23),
    _Dsx3PortIntervalUnequippedError_Type()
)
dsx3PortIntervalUnequippedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalUnequippedError.setStatus("mandatory")
_Dsx3PortIntervalTrailTraceIDMismatchError_Type = Counter32
_Dsx3PortIntervalTrailTraceIDMismatchError_Object = MibTableColumn
dsx3PortIntervalTrailTraceIDMismatchError = _Dsx3PortIntervalTrailTraceIDMismatchError_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 2, 3, 1, 24),
    _Dsx3PortIntervalTrailTraceIDMismatchError_Type()
)
dsx3PortIntervalTrailTraceIDMismatchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx3PortIntervalTrailTraceIDMismatchError.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-DS3-MIB",
    **{"dsx3Port": dsx3Port,
       "dsx3PortConfigTable": dsx3PortConfigTable,
       "dsx3PortConfigEntry": dsx3PortConfigEntry,
       "dsx3PortConfigSlotIndex": dsx3PortConfigSlotIndex,
       "dsx3PortConfigPortIndex": dsx3PortConfigPortIndex,
       "dsx3PortConfigIfType": dsx3PortConfigIfType,
       "dsx3PortConfigTcSubLayer": dsx3PortConfigTcSubLayer,
       "dsx3PortConfigPlcpStatus": dsx3PortConfigPlcpStatus,
       "dsx3PortConfigFEAC": dsx3PortConfigFEAC,
       "dsx3PortConfigNatUse": dsx3PortConfigNatUse,
       "dsx3PortConfigRxPayloadType": dsx3PortConfigRxPayloadType,
       "dsx3PortConfigTimeMarker": dsx3PortConfigTimeMarker,
       "dsx3PortConfigTxPayloadType": dsx3PortConfigTxPayloadType,
       "dsx3PortConfigExpectedPayloadType": dsx3PortConfigExpectedPayloadType,
       "dsx3PortConfigTxTrailTraceID": dsx3PortConfigTxTrailTraceID,
       "dsx3PortConfigRxTrailTraceID": dsx3PortConfigRxTrailTraceID,
       "dsx3PortConfigExpectedTrailTraceID": dsx3PortConfigExpectedTrailTraceID,
       "dsx3PortConfigLineStatus": dsx3PortConfigLineStatus,
       "dsx3PortConfigPlScramble": dsx3PortConfigPlScramble,
       "dsx3PortStatsTable": dsx3PortStatsTable,
       "dsx3PortStatsEntry": dsx3PortStatsEntry,
       "dsx3PortStatsSlotIndex": dsx3PortStatsSlotIndex,
       "dsx3PortStatsPortIndex": dsx3PortStatsPortIndex,
       "dsx3PortStatsLossOfSignal": dsx3PortStatsLossOfSignal,
       "dsx3PortStatsOutOfFrame": dsx3PortStatsOutOfFrame,
       "dsx3PortStatsAISEvent": dsx3PortStatsAISEvent,
       "dsx3PortStatsRedAlarmEvent": dsx3PortStatsRedAlarmEvent,
       "dsx3PortStatsFarEndReceiveError": dsx3PortStatsFarEndReceiveError,
       "dsx3PortStatsFarEndBlkError": dsx3PortStatsFarEndBlkError,
       "dsx3PortStatsLineCodeVioEvent": dsx3PortStatsLineCodeVioEvent,
       "dsx3PortStatsFramingBitError": dsx3PortStatsFramingBitError,
       "dsx3PortStatsChangeOfFrameAlign": dsx3PortStatsChangeOfFrameAlign,
       "dsx3PortStatsParityBitError": dsx3PortStatsParityBitError,
       "dsx3PortStatsPathParityBitError": dsx3PortStatsPathParityBitError,
       "dsx3PortStatsPlcpLossOfFrame": dsx3PortStatsPlcpLossOfFrame,
       "dsx3PortStatsPlcpOutOfFrame": dsx3PortStatsPlcpOutOfFrame,
       "dsx3PortStatsPlcpYellowAlarm": dsx3PortStatsPlcpYellowAlarm,
       "dsx3PortStatsPlcpFarEndBlkError": dsx3PortStatsPlcpFarEndBlkError,
       "dsx3PortStatsPlcpFramingError": dsx3PortStatsPlcpFramingError,
       "dsx3PortStatsPlcpBIPError": dsx3PortStatsPlcpBIPError,
       "dsx3PortStatsPayloadTypeMismatchError": dsx3PortStatsPayloadTypeMismatchError,
       "dsx3PortStatsUnequippedError": dsx3PortStatsUnequippedError,
       "dsx3PortStatsTrailTraceIDMismatchError": dsx3PortStatsTrailTraceIDMismatchError,
       "dsx3PortIntervalTable": dsx3PortIntervalTable,
       "dsx3PortIntervalEntry": dsx3PortIntervalEntry,
       "dsx3PortIntervalSlotIndex": dsx3PortIntervalSlotIndex,
       "dsx3PortIntervalPortIndex": dsx3PortIntervalPortIndex,
       "dsx3PortIntervalClear": dsx3PortIntervalClear,
       "dsx3PortIntervalLastClear": dsx3PortIntervalLastClear,
       "dsx3PortIntervalLossOfSignal": dsx3PortIntervalLossOfSignal,
       "dsx3PortIntervalOutOfFrame": dsx3PortIntervalOutOfFrame,
       "dsx3PortIntervalAISEvent": dsx3PortIntervalAISEvent,
       "dsx3PortIntervalRedAlarmEvent": dsx3PortIntervalRedAlarmEvent,
       "dsx3PortIntervalFarEndReceiveError": dsx3PortIntervalFarEndReceiveError,
       "dsx3PortIntervalFarEndBlkError": dsx3PortIntervalFarEndBlkError,
       "dsx3PortIntervalLineCodeVioEvent": dsx3PortIntervalLineCodeVioEvent,
       "dsx3PortIntervalFramingBitError": dsx3PortIntervalFramingBitError,
       "dsx3PortIntervalChangeOfFrameAlign": dsx3PortIntervalChangeOfFrameAlign,
       "dsx3PortIntervalParityBitError": dsx3PortIntervalParityBitError,
       "dsx3PortIntervalPathParityBitError": dsx3PortIntervalPathParityBitError,
       "dsx3PortIntervalPlcpLossOfFrame": dsx3PortIntervalPlcpLossOfFrame,
       "dsx3PortIntervalPlcpOutOfFrame": dsx3PortIntervalPlcpOutOfFrame,
       "dsx3PortIntervalPlcpYellowAlarm": dsx3PortIntervalPlcpYellowAlarm,
       "dsx3PortIntervalPlcpFarEndBlkError": dsx3PortIntervalPlcpFarEndBlkError,
       "dsx3PortIntervalPlcpFramingError": dsx3PortIntervalPlcpFramingError,
       "dsx3PortIntervalPlcpBIPError": dsx3PortIntervalPlcpBIPError,
       "dsx3PortIntervalPayloadTypeMismatchError": dsx3PortIntervalPayloadTypeMismatchError,
       "dsx3PortIntervalUnequippedError": dsx3PortIntervalUnequippedError,
       "dsx3PortIntervalTrailTraceIDMismatchError": dsx3PortIntervalTrailTraceIDMismatchError}
)
