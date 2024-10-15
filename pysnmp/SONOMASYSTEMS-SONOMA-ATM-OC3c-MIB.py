# SNMP MIB module (SONOMASYSTEMS-SONOMA-ATM-OC3c-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ATM-OC3c-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:43 2024
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

(sonomaATM,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaATM")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaOC3cATMAdapterGroup_ObjectIdentity = ObjectIdentity
sonomaOC3cATMAdapterGroup = _SonomaOC3cATMAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4)
)
_AtmOC3cConfGroup_ObjectIdentity = ObjectIdentity
atmOC3cConfGroup = _AtmOC3cConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1)
)
_AtmOC3cConfPhyTable_Object = MibTable
atmOC3cConfPhyTable = _AtmOC3cConfPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1)
)
if mibBuilder.loadTexts:
    atmOC3cConfPhyTable.setStatus("mandatory")
_AtmOC3cConfPhyEntry_Object = MibTableRow
atmOC3cConfPhyEntry = _AtmOC3cConfPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1, 1)
)
atmOC3cConfPhyEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-OC3c-MIB", "atmOC3cConfPhysIndex"),
)
if mibBuilder.loadTexts:
    atmOC3cConfPhyEntry.setStatus("mandatory")
_AtmOC3cConfPhysIndex_Type = Integer32
_AtmOC3cConfPhysIndex_Object = MibTableColumn
atmOC3cConfPhysIndex = _AtmOC3cConfPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1, 1, 1),
    _AtmOC3cConfPhysIndex_Type()
)
atmOC3cConfPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cConfPhysIndex.setStatus("mandatory")


class _AtmOC3cConfFraming_Type(Integer32):
    """Custom type atmOC3cConfFraming based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sDH-STM1", 2),
          ("sONET-STS3c", 1))
    )


_AtmOC3cConfFraming_Type.__name__ = "Integer32"
_AtmOC3cConfFraming_Object = MibTableColumn
atmOC3cConfFraming = _AtmOC3cConfFraming_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1, 1, 2),
    _AtmOC3cConfFraming_Type()
)
atmOC3cConfFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOC3cConfFraming.setStatus("mandatory")


class _AtmOC3cConfLoopbackMode_Type(Integer32):
    """Custom type atmOC3cConfLoopbackMode based on Integer32"""
    defaultValue = 1

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
        *(("both", 4),
          ("disabled", 1),
          ("facility", 3),
          ("terminal", 2))
    )


_AtmOC3cConfLoopbackMode_Type.__name__ = "Integer32"
_AtmOC3cConfLoopbackMode_Object = MibTableColumn
atmOC3cConfLoopbackMode = _AtmOC3cConfLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1, 1, 3),
    _AtmOC3cConfLoopbackMode_Type()
)
atmOC3cConfLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOC3cConfLoopbackMode.setStatus("mandatory")


class _AtmOC3cConfFillerCells_Type(Integer32):
    """Custom type atmOC3cConfFillerCells based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("unassigned", 1))
    )


_AtmOC3cConfFillerCells_Type.__name__ = "Integer32"
_AtmOC3cConfFillerCells_Object = MibTableColumn
atmOC3cConfFillerCells = _AtmOC3cConfFillerCells_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1, 1, 4),
    _AtmOC3cConfFillerCells_Type()
)
atmOC3cConfFillerCells.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOC3cConfFillerCells.setStatus("mandatory")


class _AtmOC3cConfOpticalDataLink_Type(Integer32):
    """Custom type atmOC3cConfOpticalDataLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("multiMode", 1),
          ("singleModeIntermedReach", 2),
          ("singleModeLongReach", 3))
    )


_AtmOC3cConfOpticalDataLink_Type.__name__ = "Integer32"
_AtmOC3cConfOpticalDataLink_Object = MibTableColumn
atmOC3cConfOpticalDataLink = _AtmOC3cConfOpticalDataLink_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1, 1, 5),
    _AtmOC3cConfOpticalDataLink_Type()
)
atmOC3cConfOpticalDataLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cConfOpticalDataLink.setStatus("mandatory")


class _AtmOC3cConfReceiveClockLooping_Type(Integer32):
    """Custom type atmOC3cConfReceiveClockLooping based on Integer32"""
    defaultValue = 1

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


_AtmOC3cConfReceiveClockLooping_Type.__name__ = "Integer32"
_AtmOC3cConfReceiveClockLooping_Object = MibTableColumn
atmOC3cConfReceiveClockLooping = _AtmOC3cConfReceiveClockLooping_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 1, 1, 1, 6),
    _AtmOC3cConfReceiveClockLooping_Type()
)
atmOC3cConfReceiveClockLooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOC3cConfReceiveClockLooping.setStatus("mandatory")
_AtmOC3cStatsGroup_ObjectIdentity = ObjectIdentity
atmOC3cStatsGroup = _AtmOC3cStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2)
)
_AtmOC3cStatsTable_Object = MibTable
atmOC3cStatsTable = _AtmOC3cStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1)
)
if mibBuilder.loadTexts:
    atmOC3cStatsTable.setStatus("mandatory")
_AtmOC3cStatsEntry_Object = MibTableRow
atmOC3cStatsEntry = _AtmOC3cStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1)
)
atmOC3cStatsEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-OC3c-MIB", "atmOC3cStatsPhysIndex"),
)
if mibBuilder.loadTexts:
    atmOC3cStatsEntry.setStatus("mandatory")
_AtmOC3cStatsPhysIndex_Type = Integer32
_AtmOC3cStatsPhysIndex_Object = MibTableColumn
atmOC3cStatsPhysIndex = _AtmOC3cStatsPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 1),
    _AtmOC3cStatsPhysIndex_Type()
)
atmOC3cStatsPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsPhysIndex.setStatus("mandatory")
_AtmOC3cStatsNoSignals_Type = Counter32
_AtmOC3cStatsNoSignals_Object = MibTableColumn
atmOC3cStatsNoSignals = _AtmOC3cStatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 2),
    _AtmOC3cStatsNoSignals_Type()
)
atmOC3cStatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsNoSignals.setStatus("mandatory")
_AtmOC3cStatsNoOC3cFrames_Type = Counter32
_AtmOC3cStatsNoOC3cFrames_Object = MibTableColumn
atmOC3cStatsNoOC3cFrames = _AtmOC3cStatsNoOC3cFrames_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 3),
    _AtmOC3cStatsNoOC3cFrames_Type()
)
atmOC3cStatsNoOC3cFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsNoOC3cFrames.setStatus("mandatory")
_AtmOC3cStatsFrameErrors_Type = Counter32
_AtmOC3cStatsFrameErrors_Object = MibTableColumn
atmOC3cStatsFrameErrors = _AtmOC3cStatsFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 4),
    _AtmOC3cStatsFrameErrors_Type()
)
atmOC3cStatsFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsFrameErrors.setStatus("mandatory")
_AtmOC3cStatsB1ParityErrors_Type = Counter32
_AtmOC3cStatsB1ParityErrors_Object = MibTableColumn
atmOC3cStatsB1ParityErrors = _AtmOC3cStatsB1ParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 5),
    _AtmOC3cStatsB1ParityErrors_Type()
)
atmOC3cStatsB1ParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB1ParityErrors.setStatus("mandatory")
_AtmOC3cStatsB2ParityErrors_Type = Counter32
_AtmOC3cStatsB2ParityErrors_Object = MibTableColumn
atmOC3cStatsB2ParityErrors = _AtmOC3cStatsB2ParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 6),
    _AtmOC3cStatsB2ParityErrors_Type()
)
atmOC3cStatsB2ParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB2ParityErrors.setStatus("mandatory")
_AtmOC3cStatsB3ParityErrors_Type = Counter32
_AtmOC3cStatsB3ParityErrors_Object = MibTableColumn
atmOC3cStatsB3ParityErrors = _AtmOC3cStatsB3ParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 7),
    _AtmOC3cStatsB3ParityErrors_Type()
)
atmOC3cStatsB3ParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB3ParityErrors.setStatus("mandatory")
_AtmOC3cStatsB1BlockErrors_Type = Counter32
_AtmOC3cStatsB1BlockErrors_Object = MibTableColumn
atmOC3cStatsB1BlockErrors = _AtmOC3cStatsB1BlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 8),
    _AtmOC3cStatsB1BlockErrors_Type()
)
atmOC3cStatsB1BlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB1BlockErrors.setStatus("mandatory")
_AtmOC3cStatsB2BlockErrors_Type = Counter32
_AtmOC3cStatsB2BlockErrors_Object = MibTableColumn
atmOC3cStatsB2BlockErrors = _AtmOC3cStatsB2BlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 9),
    _AtmOC3cStatsB2BlockErrors_Type()
)
atmOC3cStatsB2BlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB2BlockErrors.setStatus("mandatory")
_AtmOC3cStatsB3BlockErrors_Type = Counter32
_AtmOC3cStatsB3BlockErrors_Object = MibTableColumn
atmOC3cStatsB3BlockErrors = _AtmOC3cStatsB3BlockErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 10),
    _AtmOC3cStatsB3BlockErrors_Type()
)
atmOC3cStatsB3BlockErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB3BlockErrors.setStatus("mandatory")
_AtmOC3cStatsB1CodeViolations_Type = Counter32
_AtmOC3cStatsB1CodeViolations_Object = MibTableColumn
atmOC3cStatsB1CodeViolations = _AtmOC3cStatsB1CodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 11),
    _AtmOC3cStatsB1CodeViolations_Type()
)
atmOC3cStatsB1CodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB1CodeViolations.setStatus("mandatory")
_AtmOC3cStatsB2CodeViolations_Type = Counter32
_AtmOC3cStatsB2CodeViolations_Object = MibTableColumn
atmOC3cStatsB2CodeViolations = _AtmOC3cStatsB2CodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 12),
    _AtmOC3cStatsB2CodeViolations_Type()
)
atmOC3cStatsB2CodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB2CodeViolations.setStatus("mandatory")
_AtmOC3cStatsB3CodeViolations_Type = Counter32
_AtmOC3cStatsB3CodeViolations_Object = MibTableColumn
atmOC3cStatsB3CodeViolations = _AtmOC3cStatsB3CodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 13),
    _AtmOC3cStatsB3CodeViolations_Type()
)
atmOC3cStatsB3CodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsB3CodeViolations.setStatus("mandatory")
_AtmOC3cStatsLineFERFDetects_Type = Counter32
_AtmOC3cStatsLineFERFDetects_Object = MibTableColumn
atmOC3cStatsLineFERFDetects = _AtmOC3cStatsLineFERFDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 14),
    _AtmOC3cStatsLineFERFDetects_Type()
)
atmOC3cStatsLineFERFDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsLineFERFDetects.setStatus("mandatory")
_AtmOC3cStatsPathFERFDetects_Type = Counter32
_AtmOC3cStatsPathFERFDetects_Object = MibTableColumn
atmOC3cStatsPathFERFDetects = _AtmOC3cStatsPathFERFDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 15),
    _AtmOC3cStatsPathFERFDetects_Type()
)
atmOC3cStatsPathFERFDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsPathFERFDetects.setStatus("mandatory")
_AtmOC3cStatsLineAISDetects_Type = Counter32
_AtmOC3cStatsLineAISDetects_Object = MibTableColumn
atmOC3cStatsLineAISDetects = _AtmOC3cStatsLineAISDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 16),
    _AtmOC3cStatsLineAISDetects_Type()
)
atmOC3cStatsLineAISDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsLineAISDetects.setStatus("mandatory")
_AtmOC3cStatsPathAISDetects_Type = Counter32
_AtmOC3cStatsPathAISDetects_Object = MibTableColumn
atmOC3cStatsPathAISDetects = _AtmOC3cStatsPathAISDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 17),
    _AtmOC3cStatsPathAISDetects_Type()
)
atmOC3cStatsPathAISDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsPathAISDetects.setStatus("mandatory")
_AtmOC3cStatsRDIDefects_Type = Counter32
_AtmOC3cStatsRDIDefects_Object = MibTableColumn
atmOC3cStatsRDIDefects = _AtmOC3cStatsRDIDefects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 18),
    _AtmOC3cStatsRDIDefects_Type()
)
atmOC3cStatsRDIDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsRDIDefects.setStatus("mandatory")


class _AtmOC3cStatsSignalLoss_Type(Integer32):
    """Custom type atmOC3cStatsSignalLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsSignalLoss_Type.__name__ = "Integer32"
_AtmOC3cStatsSignalLoss_Object = MibTableColumn
atmOC3cStatsSignalLoss = _AtmOC3cStatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 19),
    _AtmOC3cStatsSignalLoss_Type()
)
atmOC3cStatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsSignalLoss.setStatus("mandatory")


class _AtmOC3cStatsOpticalCarrierLoss_Type(Integer32):
    """Custom type atmOC3cStatsOpticalCarrierLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsOpticalCarrierLoss_Type.__name__ = "Integer32"
_AtmOC3cStatsOpticalCarrierLoss_Object = MibTableColumn
atmOC3cStatsOpticalCarrierLoss = _AtmOC3cStatsOpticalCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 20),
    _AtmOC3cStatsOpticalCarrierLoss_Type()
)
atmOC3cStatsOpticalCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsOpticalCarrierLoss.setStatus("mandatory")


class _AtmOC3cStatsFrameLoss_Type(Integer32):
    """Custom type atmOC3cStatsFrameLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsFrameLoss_Type.__name__ = "Integer32"
_AtmOC3cStatsFrameLoss_Object = MibTableColumn
atmOC3cStatsFrameLoss = _AtmOC3cStatsFrameLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 21),
    _AtmOC3cStatsFrameLoss_Type()
)
atmOC3cStatsFrameLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsFrameLoss.setStatus("mandatory")


class _AtmOC3cStatsSyncLoss_Type(Integer32):
    """Custom type atmOC3cStatsSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsSyncLoss_Type.__name__ = "Integer32"
_AtmOC3cStatsSyncLoss_Object = MibTableColumn
atmOC3cStatsSyncLoss = _AtmOC3cStatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 22),
    _AtmOC3cStatsSyncLoss_Type()
)
atmOC3cStatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsSyncLoss.setStatus("mandatory")


class _AtmOC3cStatsOutOfCell_Type(Integer32):
    """Custom type atmOC3cStatsOutOfCell based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsOutOfCell_Type.__name__ = "Integer32"
_AtmOC3cStatsOutOfCell_Object = MibTableColumn
atmOC3cStatsOutOfCell = _AtmOC3cStatsOutOfCell_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 23),
    _AtmOC3cStatsOutOfCell_Type()
)
atmOC3cStatsOutOfCell.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsOutOfCell.setStatus("mandatory")


class _AtmOC3cStatsPointerLoss_Type(Integer32):
    """Custom type atmOC3cStatsPointerLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsPointerLoss_Type.__name__ = "Integer32"
_AtmOC3cStatsPointerLoss_Object = MibTableColumn
atmOC3cStatsPointerLoss = _AtmOC3cStatsPointerLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 24),
    _AtmOC3cStatsPointerLoss_Type()
)
atmOC3cStatsPointerLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsPointerLoss.setStatus("mandatory")


class _AtmOC3cStatsFIFOOverflow_Type(Integer32):
    """Custom type atmOC3cStatsFIFOOverflow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsFIFOOverflow_Type.__name__ = "Integer32"
_AtmOC3cStatsFIFOOverflow_Object = MibTableColumn
atmOC3cStatsFIFOOverflow = _AtmOC3cStatsFIFOOverflow_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 25),
    _AtmOC3cStatsFIFOOverflow_Type()
)
atmOC3cStatsFIFOOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsFIFOOverflow.setStatus("mandatory")


class _AtmOC3cStatsLineFERFDetect_Type(Integer32):
    """Custom type atmOC3cStatsLineFERFDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsLineFERFDetect_Type.__name__ = "Integer32"
_AtmOC3cStatsLineFERFDetect_Object = MibTableColumn
atmOC3cStatsLineFERFDetect = _AtmOC3cStatsLineFERFDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 26),
    _AtmOC3cStatsLineFERFDetect_Type()
)
atmOC3cStatsLineFERFDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsLineFERFDetect.setStatus("mandatory")


class _AtmOC3cStatsPathFERFDetect_Type(Integer32):
    """Custom type atmOC3cStatsPathFERFDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsPathFERFDetect_Type.__name__ = "Integer32"
_AtmOC3cStatsPathFERFDetect_Object = MibTableColumn
atmOC3cStatsPathFERFDetect = _AtmOC3cStatsPathFERFDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 27),
    _AtmOC3cStatsPathFERFDetect_Type()
)
atmOC3cStatsPathFERFDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsPathFERFDetect.setStatus("mandatory")


class _AtmOC3cStatsLineAISState_Type(Integer32):
    """Custom type atmOC3cStatsLineAISState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsLineAISState_Type.__name__ = "Integer32"
_AtmOC3cStatsLineAISState_Object = MibTableColumn
atmOC3cStatsLineAISState = _AtmOC3cStatsLineAISState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 28),
    _AtmOC3cStatsLineAISState_Type()
)
atmOC3cStatsLineAISState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsLineAISState.setStatus("mandatory")


class _AtmOC3cStatsPathAISState_Type(Integer32):
    """Custom type atmOC3cStatsPathAISState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsPathAISState_Type.__name__ = "Integer32"
_AtmOC3cStatsPathAISState_Object = MibTableColumn
atmOC3cStatsPathAISState = _AtmOC3cStatsPathAISState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 29),
    _AtmOC3cStatsPathAISState_Type()
)
atmOC3cStatsPathAISState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsPathAISState.setStatus("mandatory")


class _AtmOC3cStatsRDIState_Type(Integer32):
    """Custom type atmOC3cStatsRDIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsRDIState_Type.__name__ = "Integer32"
_AtmOC3cStatsRDIState_Object = MibTableColumn
atmOC3cStatsRDIState = _AtmOC3cStatsRDIState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 30),
    _AtmOC3cStatsRDIState_Type()
)
atmOC3cStatsRDIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmOC3cStatsRDIState.setStatus("mandatory")


class _AtmOC3cStatsClearCounters_Type(Integer32):
    """Custom type atmOC3cStatsClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AtmOC3cStatsClearCounters_Type.__name__ = "Integer32"
_AtmOC3cStatsClearCounters_Object = MibTableColumn
atmOC3cStatsClearCounters = _AtmOC3cStatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 4, 2, 1, 1, 31),
    _AtmOC3cStatsClearCounters_Type()
)
atmOC3cStatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmOC3cStatsClearCounters.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ATM-OC3c-MIB",
    **{"sonomaOC3cATMAdapterGroup": sonomaOC3cATMAdapterGroup,
       "atmOC3cConfGroup": atmOC3cConfGroup,
       "atmOC3cConfPhyTable": atmOC3cConfPhyTable,
       "atmOC3cConfPhyEntry": atmOC3cConfPhyEntry,
       "atmOC3cConfPhysIndex": atmOC3cConfPhysIndex,
       "atmOC3cConfFraming": atmOC3cConfFraming,
       "atmOC3cConfLoopbackMode": atmOC3cConfLoopbackMode,
       "atmOC3cConfFillerCells": atmOC3cConfFillerCells,
       "atmOC3cConfOpticalDataLink": atmOC3cConfOpticalDataLink,
       "atmOC3cConfReceiveClockLooping": atmOC3cConfReceiveClockLooping,
       "atmOC3cStatsGroup": atmOC3cStatsGroup,
       "atmOC3cStatsTable": atmOC3cStatsTable,
       "atmOC3cStatsEntry": atmOC3cStatsEntry,
       "atmOC3cStatsPhysIndex": atmOC3cStatsPhysIndex,
       "atmOC3cStatsNoSignals": atmOC3cStatsNoSignals,
       "atmOC3cStatsNoOC3cFrames": atmOC3cStatsNoOC3cFrames,
       "atmOC3cStatsFrameErrors": atmOC3cStatsFrameErrors,
       "atmOC3cStatsB1ParityErrors": atmOC3cStatsB1ParityErrors,
       "atmOC3cStatsB2ParityErrors": atmOC3cStatsB2ParityErrors,
       "atmOC3cStatsB3ParityErrors": atmOC3cStatsB3ParityErrors,
       "atmOC3cStatsB1BlockErrors": atmOC3cStatsB1BlockErrors,
       "atmOC3cStatsB2BlockErrors": atmOC3cStatsB2BlockErrors,
       "atmOC3cStatsB3BlockErrors": atmOC3cStatsB3BlockErrors,
       "atmOC3cStatsB1CodeViolations": atmOC3cStatsB1CodeViolations,
       "atmOC3cStatsB2CodeViolations": atmOC3cStatsB2CodeViolations,
       "atmOC3cStatsB3CodeViolations": atmOC3cStatsB3CodeViolations,
       "atmOC3cStatsLineFERFDetects": atmOC3cStatsLineFERFDetects,
       "atmOC3cStatsPathFERFDetects": atmOC3cStatsPathFERFDetects,
       "atmOC3cStatsLineAISDetects": atmOC3cStatsLineAISDetects,
       "atmOC3cStatsPathAISDetects": atmOC3cStatsPathAISDetects,
       "atmOC3cStatsRDIDefects": atmOC3cStatsRDIDefects,
       "atmOC3cStatsSignalLoss": atmOC3cStatsSignalLoss,
       "atmOC3cStatsOpticalCarrierLoss": atmOC3cStatsOpticalCarrierLoss,
       "atmOC3cStatsFrameLoss": atmOC3cStatsFrameLoss,
       "atmOC3cStatsSyncLoss": atmOC3cStatsSyncLoss,
       "atmOC3cStatsOutOfCell": atmOC3cStatsOutOfCell,
       "atmOC3cStatsPointerLoss": atmOC3cStatsPointerLoss,
       "atmOC3cStatsFIFOOverflow": atmOC3cStatsFIFOOverflow,
       "atmOC3cStatsLineFERFDetect": atmOC3cStatsLineFERFDetect,
       "atmOC3cStatsPathFERFDetect": atmOC3cStatsPathFERFDetect,
       "atmOC3cStatsLineAISState": atmOC3cStatsLineAISState,
       "atmOC3cStatsPathAISState": atmOC3cStatsPathAISState,
       "atmOC3cStatsRDIState": atmOC3cStatsRDIState,
       "atmOC3cStatsClearCounters": atmOC3cStatsClearCounters}
)
