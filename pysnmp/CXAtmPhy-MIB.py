# SNMP MIB module (CXAtmPhy-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXAtmPhy-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:06 2024
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

(cxAtmPhy,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxAtmPhy")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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



class Switch(Integer32):
    """Custom type Switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )





class ErrorState(Integer32):
    """Custom type ErrorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("errorDetected", 2),
          ("errorNotDetected", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AtmPhyMibLevel_Type(Integer32):
    """Custom type atmPhyMibLevel based on Integer32"""
    defaultValue = 0


_AtmPhyMibLevel_Object = MibScalar
atmPhyMibLevel = _AtmPhyMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 1),
    _AtmPhyMibLevel_Type()
)
atmPhyMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyMibLevel.setStatus("mandatory")
_AtmPhyInterfaceConfTable_Object = MibTable
atmPhyInterfaceConfTable = _AtmPhyInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10)
)
if mibBuilder.loadTexts:
    atmPhyInterfaceConfTable.setStatus("mandatory")
_AtmPhyInterfaceConfEntry_Object = MibTableRow
atmPhyInterfaceConfEntry = _AtmPhyInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1)
)
atmPhyInterfaceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmPhyInterfaceConfEntry.setStatus("mandatory")


class _AtmPhyConfTxClocking_Type(Integer32):
    """Custom type atmPhyConfTxClocking based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 1),
          ("unsynchronized", 2))
    )


_AtmPhyConfTxClocking_Type.__name__ = "Integer32"
_AtmPhyConfTxClocking_Object = MibTableColumn
atmPhyConfTxClocking = _AtmPhyConfTxClocking_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 1),
    _AtmPhyConfTxClocking_Type()
)
atmPhyConfTxClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfTxClocking.setStatus("mandatory")


class _AtmPhyConfRxLoopback_Type(Integer32):
    """Custom type atmPhyConfRxLoopback based on Integer32"""
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
        *(("cell", 3),
          ("line", 2),
          ("none", 1))
    )


_AtmPhyConfRxLoopback_Type.__name__ = "Integer32"
_AtmPhyConfRxLoopback_Object = MibTableColumn
atmPhyConfRxLoopback = _AtmPhyConfRxLoopback_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 2),
    _AtmPhyConfRxLoopback_Type()
)
atmPhyConfRxLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfRxLoopback.setStatus("mandatory")


class _AtmPhyConfFrameFormat_Type(Integer32):
    """Custom type atmPhyConfFrameFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("g-804", 1),
          ("plcp", 2))
    )


_AtmPhyConfFrameFormat_Type.__name__ = "Integer32"
_AtmPhyConfFrameFormat_Object = MibTableColumn
atmPhyConfFrameFormat = _AtmPhyConfFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 3),
    _AtmPhyConfFrameFormat_Type()
)
atmPhyConfFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfFrameFormat.setStatus("mandatory")


class _AtmPhyConfPlcpBypass_Type(Switch):
    """Custom type atmPhyConfPlcpBypass based on Switch"""


_AtmPhyConfPlcpBypass_Object = MibTableColumn
atmPhyConfPlcpBypass = _AtmPhyConfPlcpBypass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 4),
    _AtmPhyConfPlcpBypass_Type()
)
atmPhyConfPlcpBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfPlcpBypass.setStatus("mandatory")


class _AtmPhyConfTxCoset_Type(Switch):
    """Custom type atmPhyConfTxCoset based on Switch"""


_AtmPhyConfTxCoset_Object = MibTableColumn
atmPhyConfTxCoset = _AtmPhyConfTxCoset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 5),
    _AtmPhyConfTxCoset_Type()
)
atmPhyConfTxCoset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfTxCoset.setStatus("mandatory")


class _AtmPhyConfRxCoset_Type(Switch):
    """Custom type atmPhyConfRxCoset based on Switch"""


_AtmPhyConfRxCoset_Object = MibTableColumn
atmPhyConfRxCoset = _AtmPhyConfRxCoset_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 6),
    _AtmPhyConfRxCoset_Type()
)
atmPhyConfRxCoset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfRxCoset.setStatus("mandatory")


class _AtmPhyConfCellScrambling_Type(Switch):
    """Custom type atmPhyConfCellScrambling based on Switch"""


_AtmPhyConfCellScrambling_Object = MibTableColumn
atmPhyConfCellScrambling = _AtmPhyConfCellScrambling_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 7),
    _AtmPhyConfCellScrambling_Type()
)
atmPhyConfCellScrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfCellScrambling.setStatus("mandatory")


class _AtmPhyConfCellDescrambling_Type(Switch):
    """Custom type atmPhyConfCellDescrambling based on Switch"""


_AtmPhyConfCellDescrambling_Object = MibTableColumn
atmPhyConfCellDescrambling = _AtmPhyConfCellDescrambling_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 8),
    _AtmPhyConfCellDescrambling_Type()
)
atmPhyConfCellDescrambling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfCellDescrambling.setStatus("mandatory")


class _AtmPhyConfTxFifoDepth_Type(Integer32):
    """Custom type atmPhyConfTxFifoDepth based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AtmPhyConfTxFifoDepth_Type.__name__ = "Integer32"
_AtmPhyConfTxFifoDepth_Object = MibTableColumn
atmPhyConfTxFifoDepth = _AtmPhyConfTxFifoDepth_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 9),
    _AtmPhyConfTxFifoDepth_Type()
)
atmPhyConfTxFifoDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfTxFifoDepth.setStatus("mandatory")


class _AtmPhyConfRxUserProgH1Mask_Type(Integer32):
    """Custom type atmPhyConfRxUserProgH1Mask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmPhyConfRxUserProgH1Mask_Type.__name__ = "Integer32"
_AtmPhyConfRxUserProgH1Mask_Object = MibTableColumn
atmPhyConfRxUserProgH1Mask = _AtmPhyConfRxUserProgH1Mask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 20),
    _AtmPhyConfRxUserProgH1Mask_Type()
)
atmPhyConfRxUserProgH1Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfRxUserProgH1Mask.setStatus("mandatory")


class _AtmPhyConfRxUserProgH2Mask_Type(Integer32):
    """Custom type atmPhyConfRxUserProgH2Mask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmPhyConfRxUserProgH2Mask_Type.__name__ = "Integer32"
_AtmPhyConfRxUserProgH2Mask_Object = MibTableColumn
atmPhyConfRxUserProgH2Mask = _AtmPhyConfRxUserProgH2Mask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 21),
    _AtmPhyConfRxUserProgH2Mask_Type()
)
atmPhyConfRxUserProgH2Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfRxUserProgH2Mask.setStatus("mandatory")


class _AtmPhyConfRxUserProgH3Mask_Type(Integer32):
    """Custom type atmPhyConfRxUserProgH3Mask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmPhyConfRxUserProgH3Mask_Type.__name__ = "Integer32"
_AtmPhyConfRxUserProgH3Mask_Object = MibTableColumn
atmPhyConfRxUserProgH3Mask = _AtmPhyConfRxUserProgH3Mask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 22),
    _AtmPhyConfRxUserProgH3Mask_Type()
)
atmPhyConfRxUserProgH3Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfRxUserProgH3Mask.setStatus("mandatory")


class _AtmPhyConfRxUserProgH4Mask_Type(Integer32):
    """Custom type atmPhyConfRxUserProgH4Mask based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmPhyConfRxUserProgH4Mask_Type.__name__ = "Integer32"
_AtmPhyConfRxUserProgH4Mask_Object = MibTableColumn
atmPhyConfRxUserProgH4Mask = _AtmPhyConfRxUserProgH4Mask_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 23),
    _AtmPhyConfRxUserProgH4Mask_Type()
)
atmPhyConfRxUserProgH4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfRxUserProgH4Mask.setStatus("mandatory")


class _AtmPhyConfTxIdleUnassignedCellPayload_Type(Integer32):
    """Custom type atmPhyConfTxIdleUnassignedCellPayload based on Integer32"""
    defaultValue = 106

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmPhyConfTxIdleUnassignedCellPayload_Type.__name__ = "Integer32"
_AtmPhyConfTxIdleUnassignedCellPayload_Object = MibTableColumn
atmPhyConfTxIdleUnassignedCellPayload = _AtmPhyConfTxIdleUnassignedCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 24),
    _AtmPhyConfTxIdleUnassignedCellPayload_Type()
)
atmPhyConfTxIdleUnassignedCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfTxIdleUnassignedCellPayload.setStatus("mandatory")


class _AtmPhyConfPlcpControlTimer_Type(Integer32):
    """Custom type atmPhyConfPlcpControlTimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_AtmPhyConfPlcpControlTimer_Type.__name__ = "Integer32"
_AtmPhyConfPlcpControlTimer_Object = MibTableColumn
atmPhyConfPlcpControlTimer = _AtmPhyConfPlcpControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 25),
    _AtmPhyConfPlcpControlTimer_Type()
)
atmPhyConfPlcpControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfPlcpControlTimer.setStatus("mandatory")


class _AtmPhyConfControl_Type(Integer32):
    """Custom type atmPhyConfControl based on Integer32"""
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
        *(("clearStats", 2),
          ("disableHCSErrorGeneration", 4),
          ("enableHCSErrorGeneration", 3),
          ("none", 1))
    )


_AtmPhyConfControl_Type.__name__ = "Integer32"
_AtmPhyConfControl_Object = MibTableColumn
atmPhyConfControl = _AtmPhyConfControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 40),
    _AtmPhyConfControl_Type()
)
atmPhyConfControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfControl.setStatus("mandatory")


class _AtmPhyConfPlcpControl_Type(Integer32):
    """Custom type atmPhyConfPlcpControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmPhyConfPlcpControl_Type.__name__ = "Integer32"
_AtmPhyConfPlcpControl_Object = MibTableColumn
atmPhyConfPlcpControl = _AtmPhyConfPlcpControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 10, 1, 45),
    _AtmPhyConfPlcpControl_Type()
)
atmPhyConfPlcpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmPhyConfPlcpControl.setStatus("mandatory")
_AtmPhyOperTable_Object = MibTable
atmPhyOperTable = _AtmPhyOperTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20)
)
if mibBuilder.loadTexts:
    atmPhyOperTable.setStatus("mandatory")
_AtmPhyOperEntry_Object = MibTableRow
atmPhyOperEntry = _AtmPhyOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1)
)
atmPhyOperEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmPhyOperEntry.setStatus("mandatory")
_AtmPhyOperDeviceVersion_Type = Integer32
_AtmPhyOperDeviceVersion_Object = MibTableColumn
atmPhyOperDeviceVersion = _AtmPhyOperDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 10),
    _AtmPhyOperDeviceVersion_Type()
)
atmPhyOperDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperDeviceVersion.setStatus("mandatory")


class _AtmPhyOperFramerDetected_Type(Integer32):
    """Custom type atmPhyOperFramerDetected based on Integer32"""
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
        *(("ds1", 2),
          ("ds3", 4),
          ("e1", 3),
          ("e3", 5),
          ("none", 1))
    )


_AtmPhyOperFramerDetected_Type.__name__ = "Integer32"
_AtmPhyOperFramerDetected_Object = MibTableColumn
atmPhyOperFramerDetected = _AtmPhyOperFramerDetected_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 11),
    _AtmPhyOperFramerDetected_Type()
)
atmPhyOperFramerDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperFramerDetected.setStatus("mandatory")


class _AtmPhyOperState_Type(Integer32):
    """Custom type atmPhyOperState based on Integer32"""
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
        *(("down", 4),
          ("downConfigError", 3),
          ("downNoHwDetected", 2),
          ("offLine", 1),
          ("up", 5))
    )


_AtmPhyOperState_Type.__name__ = "Integer32"
_AtmPhyOperState_Object = MibTableColumn
atmPhyOperState = _AtmPhyOperState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 12),
    _AtmPhyOperState_Type()
)
atmPhyOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperState.setStatus("mandatory")


class _AtmPhyOperLCDState_Type(Integer32):
    """Custom type atmPhyOperLCDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detectedLCD", 1),
          ("noLCD", 2))
    )


_AtmPhyOperLCDState_Type.__name__ = "Integer32"
_AtmPhyOperLCDState_Object = MibTableColumn
atmPhyOperLCDState = _AtmPhyOperLCDState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 13),
    _AtmPhyOperLCDState_Type()
)
atmPhyOperLCDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperLCDState.setStatus("mandatory")
_AtmPhyOperRxIdleUnassignedCellsDropped_Type = Counter32
_AtmPhyOperRxIdleUnassignedCellsDropped_Object = MibTableColumn
atmPhyOperRxIdleUnassignedCellsDropped = _AtmPhyOperRxIdleUnassignedCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 20),
    _AtmPhyOperRxIdleUnassignedCellsDropped_Type()
)
atmPhyOperRxIdleUnassignedCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperRxIdleUnassignedCellsDropped.setStatus("mandatory")
_AtmPhyOperHCSErrors_Type = Counter32
_AtmPhyOperHCSErrors_Object = MibTableColumn
atmPhyOperHCSErrors = _AtmPhyOperHCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 21),
    _AtmPhyOperHCSErrors_Type()
)
atmPhyOperHCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperHCSErrors.setStatus("mandatory")
_AtmPhyOperOCDEvents_Type = Counter32
_AtmPhyOperOCDEvents_Object = MibTableColumn
atmPhyOperOCDEvents = _AtmPhyOperOCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 22),
    _AtmPhyOperOCDEvents_Type()
)
atmPhyOperOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperOCDEvents.setStatus("mandatory")
_AtmPhyOperRxFifoOverruns_Type = Counter32
_AtmPhyOperRxFifoOverruns_Object = MibTableColumn
atmPhyOperRxFifoOverruns = _AtmPhyOperRxFifoOverruns_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 23),
    _AtmPhyOperRxFifoOverruns_Type()
)
atmPhyOperRxFifoOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperRxFifoOverruns.setStatus("mandatory")
_AtmPhyOperTxFifoOverruns_Type = Counter32
_AtmPhyOperTxFifoOverruns_Object = MibTableColumn
atmPhyOperTxFifoOverruns = _AtmPhyOperTxFifoOverruns_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 20, 1, 24),
    _AtmPhyOperTxFifoOverruns_Type()
)
atmPhyOperTxFifoOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperTxFifoOverruns.setStatus("mandatory")
_AtmPhyOperPlcpTable_Object = MibTable
atmPhyOperPlcpTable = _AtmPhyOperPlcpTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30)
)
if mibBuilder.loadTexts:
    atmPhyOperPlcpTable.setStatus("mandatory")
_AtmPhyOperPlcpEntry_Object = MibTableRow
atmPhyOperPlcpEntry = _AtmPhyOperPlcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1)
)
atmPhyOperPlcpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmPhyOperPlcpEntry.setStatus("mandatory")
_AtmPhyOperPlcpOOFDefectState_Type = ErrorState
_AtmPhyOperPlcpOOFDefectState_Object = MibTableColumn
atmPhyOperPlcpOOFDefectState = _AtmPhyOperPlcpOOFDefectState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 10),
    _AtmPhyOperPlcpOOFDefectState_Type()
)
atmPhyOperPlcpOOFDefectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpOOFDefectState.setStatus("mandatory")
_AtmPhyOperPlcpLOFDefectState_Type = ErrorState
_AtmPhyOperPlcpLOFDefectState_Object = MibTableColumn
atmPhyOperPlcpLOFDefectState = _AtmPhyOperPlcpLOFDefectState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 11),
    _AtmPhyOperPlcpLOFDefectState_Type()
)
atmPhyOperPlcpLOFDefectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpLOFDefectState.setStatus("mandatory")
_AtmPhyOperPlcpYADefectState_Type = ErrorState
_AtmPhyOperPlcpYADefectState_Object = MibTableColumn
atmPhyOperPlcpYADefectState = _AtmPhyOperPlcpYADefectState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 12),
    _AtmPhyOperPlcpYADefectState_Type()
)
atmPhyOperPlcpYADefectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpYADefectState.setStatus("mandatory")
_AtmPhyOperPlcpOOFs_Type = Counter32
_AtmPhyOperPlcpOOFs_Object = MibTableColumn
atmPhyOperPlcpOOFs = _AtmPhyOperPlcpOOFs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 20),
    _AtmPhyOperPlcpOOFs_Type()
)
atmPhyOperPlcpOOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpOOFs.setStatus("mandatory")
_AtmPhyOperPlcpLOFs_Type = Counter32
_AtmPhyOperPlcpLOFs_Object = MibTableColumn
atmPhyOperPlcpLOFs = _AtmPhyOperPlcpLOFs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 21),
    _AtmPhyOperPlcpLOFs_Type()
)
atmPhyOperPlcpLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpLOFs.setStatus("mandatory")
_AtmPhyOperPlcpYAs_Type = Counter32
_AtmPhyOperPlcpYAs_Object = MibTableColumn
atmPhyOperPlcpYAs = _AtmPhyOperPlcpYAs_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 22),
    _AtmPhyOperPlcpYAs_Type()
)
atmPhyOperPlcpYAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpYAs.setStatus("mandatory")
_AtmPhyOperPlcpBIPErrors_Type = Counter32
_AtmPhyOperPlcpBIPErrors_Object = MibTableColumn
atmPhyOperPlcpBIPErrors = _AtmPhyOperPlcpBIPErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 23),
    _AtmPhyOperPlcpBIPErrors_Type()
)
atmPhyOperPlcpBIPErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpBIPErrors.setStatus("mandatory")
_AtmPhyOperPlcpFramingErrors_Type = Counter32
_AtmPhyOperPlcpFramingErrors_Object = MibTableColumn
atmPhyOperPlcpFramingErrors = _AtmPhyOperPlcpFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 24),
    _AtmPhyOperPlcpFramingErrors_Type()
)
atmPhyOperPlcpFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpFramingErrors.setStatus("mandatory")
_AtmPhyOperPlcpFEBEErrors_Type = Counter32
_AtmPhyOperPlcpFEBEErrors_Object = MibTableColumn
atmPhyOperPlcpFEBEErrors = _AtmPhyOperPlcpFEBEErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 61, 30, 1, 25),
    _AtmPhyOperPlcpFEBEErrors_Type()
)
atmPhyOperPlcpFEBEErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmPhyOperPlcpFEBEErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXAtmPhy-MIB",
    **{"Switch": Switch,
       "ErrorState": ErrorState,
       "atmPhyMibLevel": atmPhyMibLevel,
       "atmPhyInterfaceConfTable": atmPhyInterfaceConfTable,
       "atmPhyInterfaceConfEntry": atmPhyInterfaceConfEntry,
       "atmPhyConfTxClocking": atmPhyConfTxClocking,
       "atmPhyConfRxLoopback": atmPhyConfRxLoopback,
       "atmPhyConfFrameFormat": atmPhyConfFrameFormat,
       "atmPhyConfPlcpBypass": atmPhyConfPlcpBypass,
       "atmPhyConfTxCoset": atmPhyConfTxCoset,
       "atmPhyConfRxCoset": atmPhyConfRxCoset,
       "atmPhyConfCellScrambling": atmPhyConfCellScrambling,
       "atmPhyConfCellDescrambling": atmPhyConfCellDescrambling,
       "atmPhyConfTxFifoDepth": atmPhyConfTxFifoDepth,
       "atmPhyConfRxUserProgH1Mask": atmPhyConfRxUserProgH1Mask,
       "atmPhyConfRxUserProgH2Mask": atmPhyConfRxUserProgH2Mask,
       "atmPhyConfRxUserProgH3Mask": atmPhyConfRxUserProgH3Mask,
       "atmPhyConfRxUserProgH4Mask": atmPhyConfRxUserProgH4Mask,
       "atmPhyConfTxIdleUnassignedCellPayload": atmPhyConfTxIdleUnassignedCellPayload,
       "atmPhyConfPlcpControlTimer": atmPhyConfPlcpControlTimer,
       "atmPhyConfControl": atmPhyConfControl,
       "atmPhyConfPlcpControl": atmPhyConfPlcpControl,
       "atmPhyOperTable": atmPhyOperTable,
       "atmPhyOperEntry": atmPhyOperEntry,
       "atmPhyOperDeviceVersion": atmPhyOperDeviceVersion,
       "atmPhyOperFramerDetected": atmPhyOperFramerDetected,
       "atmPhyOperState": atmPhyOperState,
       "atmPhyOperLCDState": atmPhyOperLCDState,
       "atmPhyOperRxIdleUnassignedCellsDropped": atmPhyOperRxIdleUnassignedCellsDropped,
       "atmPhyOperHCSErrors": atmPhyOperHCSErrors,
       "atmPhyOperOCDEvents": atmPhyOperOCDEvents,
       "atmPhyOperRxFifoOverruns": atmPhyOperRxFifoOverruns,
       "atmPhyOperTxFifoOverruns": atmPhyOperTxFifoOverruns,
       "atmPhyOperPlcpTable": atmPhyOperPlcpTable,
       "atmPhyOperPlcpEntry": atmPhyOperPlcpEntry,
       "atmPhyOperPlcpOOFDefectState": atmPhyOperPlcpOOFDefectState,
       "atmPhyOperPlcpLOFDefectState": atmPhyOperPlcpLOFDefectState,
       "atmPhyOperPlcpYADefectState": atmPhyOperPlcpYADefectState,
       "atmPhyOperPlcpOOFs": atmPhyOperPlcpOOFs,
       "atmPhyOperPlcpLOFs": atmPhyOperPlcpLOFs,
       "atmPhyOperPlcpYAs": atmPhyOperPlcpYAs,
       "atmPhyOperPlcpBIPErrors": atmPhyOperPlcpBIPErrors,
       "atmPhyOperPlcpFramingErrors": atmPhyOperPlcpFramingErrors,
       "atmPhyOperPlcpFEBEErrors": atmPhyOperPlcpFEBEErrors}
)
