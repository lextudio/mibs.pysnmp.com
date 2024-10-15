# SNMP MIB module (XYLAN-IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-IMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:05 2024
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

(xylanPportArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanPportArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanImaMib_ObjectIdentity = ObjectIdentity
xylanImaMib = _XylanImaMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3)
)
_XylanImaLinkTable_Object = MibTable
xylanImaLinkTable = _XylanImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    xylanImaLinkTable.setStatus("mandatory")
_XylanImaLinkEntry_Object = MibTableRow
xylanImaLinkEntry = _XylanImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1)
)
xylanImaLinkEntry.setIndexNames(
    (0, "XYLAN-IMA-MIB", "xylanImaLinkSlotIndex"),
    (0, "XYLAN-IMA-MIB", "xylanImaLinkPortIndex"),
)
if mibBuilder.loadTexts:
    xylanImaLinkEntry.setStatus("mandatory")


class _XylanImaLinkSlotIndex_Type(Integer32):
    """Custom type xylanImaLinkSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylanImaLinkSlotIndex_Type.__name__ = "Integer32"
_XylanImaLinkSlotIndex_Object = MibTableColumn
xylanImaLinkSlotIndex = _XylanImaLinkSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 1),
    _XylanImaLinkSlotIndex_Type()
)
xylanImaLinkSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkSlotIndex.setStatus("mandatory")


class _XylanImaLinkPortIndex_Type(Integer32):
    """Custom type xylanImaLinkPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_XylanImaLinkPortIndex_Type.__name__ = "Integer32"
_XylanImaLinkPortIndex_Object = MibTableColumn
xylanImaLinkPortIndex = _XylanImaLinkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 2),
    _XylanImaLinkPortIndex_Type()
)
xylanImaLinkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkPortIndex.setStatus("mandatory")


class _XylanImaLinkDescription_Type(DisplayString):
    """Custom type xylanImaLinkDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XylanImaLinkDescription_Type.__name__ = "DisplayString"
_XylanImaLinkDescription_Object = MibTableColumn
xylanImaLinkDescription = _XylanImaLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 3),
    _XylanImaLinkDescription_Type()
)
xylanImaLinkDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaLinkDescription.setStatus("mandatory")


class _XylanImaLinkAdminStatus_Type(Integer32):
    """Custom type xylanImaLinkAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XylanImaLinkAdminStatus_Type.__name__ = "Integer32"
_XylanImaLinkAdminStatus_Object = MibTableColumn
xylanImaLinkAdminStatus = _XylanImaLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 4),
    _XylanImaLinkAdminStatus_Type()
)
xylanImaLinkAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaLinkAdminStatus.setStatus("mandatory")
_XylanImaLinkIfIndex_Type = Integer32
_XylanImaLinkIfIndex_Object = MibTableColumn
xylanImaLinkIfIndex = _XylanImaLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 5),
    _XylanImaLinkIfIndex_Type()
)
xylanImaLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkIfIndex.setStatus("mandatory")
_XylanImaLinkRxIcpCells_Type = Integer32
_XylanImaLinkRxIcpCells_Object = MibTableColumn
xylanImaLinkRxIcpCells = _XylanImaLinkRxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 6),
    _XylanImaLinkRxIcpCells_Type()
)
xylanImaLinkRxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxIcpCells.setStatus("mandatory")
_XylanImaLinkTxIcpCells_Type = Integer32
_XylanImaLinkTxIcpCells_Object = MibTableColumn
xylanImaLinkTxIcpCells = _XylanImaLinkTxIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 7),
    _XylanImaLinkTxIcpCells_Type()
)
xylanImaLinkTxIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkTxIcpCells.setStatus("mandatory")
_XylanImaLinkRxFillerCells_Type = Integer32
_XylanImaLinkRxFillerCells_Object = MibTableColumn
xylanImaLinkRxFillerCells = _XylanImaLinkRxFillerCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 8),
    _XylanImaLinkRxFillerCells_Type()
)
xylanImaLinkRxFillerCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxFillerCells.setStatus("mandatory")
_XylanImaLinkTxFillerCells_Type = Integer32
_XylanImaLinkTxFillerCells_Object = MibTableColumn
xylanImaLinkTxFillerCells = _XylanImaLinkTxFillerCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 9),
    _XylanImaLinkTxFillerCells_Type()
)
xylanImaLinkTxFillerCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkTxFillerCells.setStatus("mandatory")
_XylanImaLinkRxAtmLayerCells_Type = Integer32
_XylanImaLinkRxAtmLayerCells_Object = MibTableColumn
xylanImaLinkRxAtmLayerCells = _XylanImaLinkRxAtmLayerCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 10),
    _XylanImaLinkRxAtmLayerCells_Type()
)
xylanImaLinkRxAtmLayerCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxAtmLayerCells.setStatus("mandatory")
_XylanImaLinkTxAtmLayerCells_Type = Integer32
_XylanImaLinkTxAtmLayerCells_Object = MibTableColumn
xylanImaLinkTxAtmLayerCells = _XylanImaLinkTxAtmLayerCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 11),
    _XylanImaLinkTxAtmLayerCells_Type()
)
xylanImaLinkTxAtmLayerCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkTxAtmLayerCells.setStatus("mandatory")
_XylanImaLinkRxBadIcpCells_Type = Integer32
_XylanImaLinkRxBadIcpCells_Object = MibTableColumn
xylanImaLinkRxBadIcpCells = _XylanImaLinkRxBadIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 12),
    _XylanImaLinkRxBadIcpCells_Type()
)
xylanImaLinkRxBadIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxBadIcpCells.setStatus("mandatory")
_XylanImaLinkRxBadCrcIcpCells_Type = Integer32
_XylanImaLinkRxBadCrcIcpCells_Object = MibTableColumn
xylanImaLinkRxBadCrcIcpCells = _XylanImaLinkRxBadCrcIcpCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 13),
    _XylanImaLinkRxBadCrcIcpCells_Type()
)
xylanImaLinkRxBadCrcIcpCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxBadCrcIcpCells.setStatus("mandatory")
_XylanImaLinkCellsInRxBuffer_Type = Integer32
_XylanImaLinkCellsInRxBuffer_Object = MibTableColumn
xylanImaLinkCellsInRxBuffer = _XylanImaLinkCellsInRxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 14),
    _XylanImaLinkCellsInRxBuffer_Type()
)
xylanImaLinkCellsInRxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkCellsInRxBuffer.setStatus("mandatory")
_XylanImaLinkRxBufferFlush_Type = Integer32
_XylanImaLinkRxBufferFlush_Object = MibTableColumn
xylanImaLinkRxBufferFlush = _XylanImaLinkRxBufferFlush_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 15),
    _XylanImaLinkRxBufferFlush_Type()
)
xylanImaLinkRxBufferFlush.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxBufferFlush.setStatus("mandatory")
_XylanImaLinkRxBufferOverflow_Type = Integer32
_XylanImaLinkRxBufferOverflow_Object = MibTableColumn
xylanImaLinkRxBufferOverflow = _XylanImaLinkRxBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 16),
    _XylanImaLinkRxBufferOverflow_Type()
)
xylanImaLinkRxBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxBufferOverflow.setStatus("mandatory")
_XylanImaLinkRxCellDiscarded_Type = Integer32
_XylanImaLinkRxCellDiscarded_Object = MibTableColumn
xylanImaLinkRxCellDiscarded = _XylanImaLinkRxCellDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 17),
    _XylanImaLinkRxCellDiscarded_Type()
)
xylanImaLinkRxCellDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxCellDiscarded.setStatus("mandatory")
_XylanImaLinkRxStuffEvents_Type = Integer32
_XylanImaLinkRxStuffEvents_Object = MibTableColumn
xylanImaLinkRxStuffEvents = _XylanImaLinkRxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 18),
    _XylanImaLinkRxStuffEvents_Type()
)
xylanImaLinkRxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkRxStuffEvents.setStatus("mandatory")
_XylanImaLinkTxStuffEvents_Type = Integer32
_XylanImaLinkTxStuffEvents_Object = MibTableColumn
xylanImaLinkTxStuffEvents = _XylanImaLinkTxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 19),
    _XylanImaLinkTxStuffEvents_Type()
)
xylanImaLinkTxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaLinkTxStuffEvents.setStatus("mandatory")


class _XylanImaLinkClearStatistics_Type(Integer32):
    """Custom type xylanImaLinkClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_XylanImaLinkClearStatistics_Type.__name__ = "Integer32"
_XylanImaLinkClearStatistics_Object = MibTableColumn
xylanImaLinkClearStatistics = _XylanImaLinkClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 1, 1, 20),
    _XylanImaLinkClearStatistics_Type()
)
xylanImaLinkClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaLinkClearStatistics.setStatus("mandatory")
_XylanImaGroupTable_Object = MibTable
xylanImaGroupTable = _XylanImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2)
)
if mibBuilder.loadTexts:
    xylanImaGroupTable.setStatus("mandatory")
_XylanImaGroupEntry_Object = MibTableRow
xylanImaGroupEntry = _XylanImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1)
)
xylanImaGroupEntry.setIndexNames(
    (0, "XYLAN-IMA-MIB", "xylanImaGroupIndex"),
)
if mibBuilder.loadTexts:
    xylanImaGroupEntry.setStatus("mandatory")
_XylanImaGroupIndex_Type = Integer32
_XylanImaGroupIndex_Object = MibTableColumn
xylanImaGroupIndex = _XylanImaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 1),
    _XylanImaGroupIndex_Type()
)
xylanImaGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaGroupIndex.setStatus("mandatory")


class _XylanImaGroupDescription_Type(DisplayString):
    """Custom type xylanImaGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_XylanImaGroupDescription_Type.__name__ = "DisplayString"
_XylanImaGroupDescription_Object = MibTableColumn
xylanImaGroupDescription = _XylanImaGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 2),
    _XylanImaGroupDescription_Type()
)
xylanImaGroupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupDescription.setStatus("mandatory")


class _XylanImaGroupAdminStatus_Type(Integer32):
    """Custom type xylanImaGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_XylanImaGroupAdminStatus_Type.__name__ = "Integer32"
_XylanImaGroupAdminStatus_Object = MibTableColumn
xylanImaGroupAdminStatus = _XylanImaGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 3),
    _XylanImaGroupAdminStatus_Type()
)
xylanImaGroupAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupAdminStatus.setStatus("mandatory")


class _XylanImaGroupMaxDelaySlot_Type(Integer32):
    """Custom type xylanImaGroupMaxDelaySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylanImaGroupMaxDelaySlot_Type.__name__ = "Integer32"
_XylanImaGroupMaxDelaySlot_Object = MibTableColumn
xylanImaGroupMaxDelaySlot = _XylanImaGroupMaxDelaySlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 4),
    _XylanImaGroupMaxDelaySlot_Type()
)
xylanImaGroupMaxDelaySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaGroupMaxDelaySlot.setStatus("mandatory")


class _XylanImaGroupMaxDelayPort_Type(Integer32):
    """Custom type xylanImaGroupMaxDelayPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_XylanImaGroupMaxDelayPort_Type.__name__ = "Integer32"
_XylanImaGroupMaxDelayPort_Object = MibTableColumn
xylanImaGroupMaxDelayPort = _XylanImaGroupMaxDelayPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 5),
    _XylanImaGroupMaxDelayPort_Type()
)
xylanImaGroupMaxDelayPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaGroupMaxDelayPort.setStatus("mandatory")


class _XylanImaGroupAtmLayerSlot_Type(Integer32):
    """Custom type xylanImaGroupAtmLayerSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_XylanImaGroupAtmLayerSlot_Type.__name__ = "Integer32"
_XylanImaGroupAtmLayerSlot_Object = MibTableColumn
xylanImaGroupAtmLayerSlot = _XylanImaGroupAtmLayerSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 6),
    _XylanImaGroupAtmLayerSlot_Type()
)
xylanImaGroupAtmLayerSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupAtmLayerSlot.setStatus("mandatory")


class _XylanImaGroupAtmLayerPort_Type(Integer32):
    """Custom type xylanImaGroupAtmLayerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_XylanImaGroupAtmLayerPort_Type.__name__ = "Integer32"
_XylanImaGroupAtmLayerPort_Object = MibTableColumn
xylanImaGroupAtmLayerPort = _XylanImaGroupAtmLayerPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 7),
    _XylanImaGroupAtmLayerPort_Type()
)
xylanImaGroupAtmLayerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupAtmLayerPort.setStatus("mandatory")
_XylanImaGroupRxAtmLayerCells_Type = Integer32
_XylanImaGroupRxAtmLayerCells_Object = MibTableColumn
xylanImaGroupRxAtmLayerCells = _XylanImaGroupRxAtmLayerCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 8),
    _XylanImaGroupRxAtmLayerCells_Type()
)
xylanImaGroupRxAtmLayerCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaGroupRxAtmLayerCells.setStatus("mandatory")
_XylanImaGroupTxAtmLayerCells_Type = Integer32
_XylanImaGroupTxAtmLayerCells_Object = MibTableColumn
xylanImaGroupTxAtmLayerCells = _XylanImaGroupTxAtmLayerCells_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 9),
    _XylanImaGroupTxAtmLayerCells_Type()
)
xylanImaGroupTxAtmLayerCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanImaGroupTxAtmLayerCells.setStatus("mandatory")


class _XylanImaGroupPhyFrameFormat_Type(Integer32):
    """Custom type xylanImaGroupPhyFrameFormat based on Integer32"""
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
        *(("e1", 4),
          ("e1-crc", 5),
          ("esf", 2),
          ("other", 1),
          ("sf", 3))
    )


_XylanImaGroupPhyFrameFormat_Type.__name__ = "Integer32"
_XylanImaGroupPhyFrameFormat_Object = MibTableColumn
xylanImaGroupPhyFrameFormat = _XylanImaGroupPhyFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 10),
    _XylanImaGroupPhyFrameFormat_Type()
)
xylanImaGroupPhyFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupPhyFrameFormat.setStatus("mandatory")


class _XylanImaGroupPhyLoopbackMode_Type(Integer32):
    """Custom type xylanImaGroupPhyLoopbackMode based on Integer32"""
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
        *(("inward", 5),
          ("line", 3),
          ("none", 1),
          ("other", 4),
          ("payloop", 2))
    )


_XylanImaGroupPhyLoopbackMode_Type.__name__ = "Integer32"
_XylanImaGroupPhyLoopbackMode_Object = MibTableColumn
xylanImaGroupPhyLoopbackMode = _XylanImaGroupPhyLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 11),
    _XylanImaGroupPhyLoopbackMode_Type()
)
xylanImaGroupPhyLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupPhyLoopbackMode.setStatus("mandatory")


class _XylanImaGroupPhyLineLength_Type(Integer32):
    """Custom type xylanImaGroupPhyLineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_XylanImaGroupPhyLineLength_Type.__name__ = "Integer32"
_XylanImaGroupPhyLineLength_Object = MibTableColumn
xylanImaGroupPhyLineLength = _XylanImaGroupPhyLineLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 12),
    _XylanImaGroupPhyLineLength_Type()
)
xylanImaGroupPhyLineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupPhyLineLength.setStatus("mandatory")


class _XylanImaGroupPhyTxClkSource_Type(Integer32):
    """Custom type xylanImaGroupPhyTxClkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1))
    )


_XylanImaGroupPhyTxClkSource_Type.__name__ = "Integer32"
_XylanImaGroupPhyTxClkSource_Object = MibTableColumn
xylanImaGroupPhyTxClkSource = _XylanImaGroupPhyTxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 13),
    _XylanImaGroupPhyTxClkSource_Type()
)
xylanImaGroupPhyTxClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupPhyTxClkSource.setStatus("mandatory")


class _XylanImaGroupClearStatistics_Type(Integer32):
    """Custom type xylanImaGroupClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noAction", 1))
    )


_XylanImaGroupClearStatistics_Type.__name__ = "Integer32"
_XylanImaGroupClearStatistics_Object = MibTableColumn
xylanImaGroupClearStatistics = _XylanImaGroupClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 14),
    _XylanImaGroupClearStatistics_Type()
)
xylanImaGroupClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupClearStatistics.setStatus("mandatory")


class _XylanImaGroupPhyUniqueParameter_Type(Integer32):
    """Custom type xylanImaGroupPhyUniqueParameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_XylanImaGroupPhyUniqueParameter_Type.__name__ = "Integer32"
_XylanImaGroupPhyUniqueParameter_Object = MibTableColumn
xylanImaGroupPhyUniqueParameter = _XylanImaGroupPhyUniqueParameter_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 11, 3, 2, 1, 15),
    _XylanImaGroupPhyUniqueParameter_Type()
)
xylanImaGroupPhyUniqueParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanImaGroupPhyUniqueParameter.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-IMA-MIB",
    **{"xylanImaMib": xylanImaMib,
       "xylanImaLinkTable": xylanImaLinkTable,
       "xylanImaLinkEntry": xylanImaLinkEntry,
       "xylanImaLinkSlotIndex": xylanImaLinkSlotIndex,
       "xylanImaLinkPortIndex": xylanImaLinkPortIndex,
       "xylanImaLinkDescription": xylanImaLinkDescription,
       "xylanImaLinkAdminStatus": xylanImaLinkAdminStatus,
       "xylanImaLinkIfIndex": xylanImaLinkIfIndex,
       "xylanImaLinkRxIcpCells": xylanImaLinkRxIcpCells,
       "xylanImaLinkTxIcpCells": xylanImaLinkTxIcpCells,
       "xylanImaLinkRxFillerCells": xylanImaLinkRxFillerCells,
       "xylanImaLinkTxFillerCells": xylanImaLinkTxFillerCells,
       "xylanImaLinkRxAtmLayerCells": xylanImaLinkRxAtmLayerCells,
       "xylanImaLinkTxAtmLayerCells": xylanImaLinkTxAtmLayerCells,
       "xylanImaLinkRxBadIcpCells": xylanImaLinkRxBadIcpCells,
       "xylanImaLinkRxBadCrcIcpCells": xylanImaLinkRxBadCrcIcpCells,
       "xylanImaLinkCellsInRxBuffer": xylanImaLinkCellsInRxBuffer,
       "xylanImaLinkRxBufferFlush": xylanImaLinkRxBufferFlush,
       "xylanImaLinkRxBufferOverflow": xylanImaLinkRxBufferOverflow,
       "xylanImaLinkRxCellDiscarded": xylanImaLinkRxCellDiscarded,
       "xylanImaLinkRxStuffEvents": xylanImaLinkRxStuffEvents,
       "xylanImaLinkTxStuffEvents": xylanImaLinkTxStuffEvents,
       "xylanImaLinkClearStatistics": xylanImaLinkClearStatistics,
       "xylanImaGroupTable": xylanImaGroupTable,
       "xylanImaGroupEntry": xylanImaGroupEntry,
       "xylanImaGroupIndex": xylanImaGroupIndex,
       "xylanImaGroupDescription": xylanImaGroupDescription,
       "xylanImaGroupAdminStatus": xylanImaGroupAdminStatus,
       "xylanImaGroupMaxDelaySlot": xylanImaGroupMaxDelaySlot,
       "xylanImaGroupMaxDelayPort": xylanImaGroupMaxDelayPort,
       "xylanImaGroupAtmLayerSlot": xylanImaGroupAtmLayerSlot,
       "xylanImaGroupAtmLayerPort": xylanImaGroupAtmLayerPort,
       "xylanImaGroupRxAtmLayerCells": xylanImaGroupRxAtmLayerCells,
       "xylanImaGroupTxAtmLayerCells": xylanImaGroupTxAtmLayerCells,
       "xylanImaGroupPhyFrameFormat": xylanImaGroupPhyFrameFormat,
       "xylanImaGroupPhyLoopbackMode": xylanImaGroupPhyLoopbackMode,
       "xylanImaGroupPhyLineLength": xylanImaGroupPhyLineLength,
       "xylanImaGroupPhyTxClkSource": xylanImaGroupPhyTxClkSource,
       "xylanImaGroupClearStatistics": xylanImaGroupClearStatistics,
       "xylanImaGroupPhyUniqueParameter": xylanImaGroupPhyUniqueParameter}
)
