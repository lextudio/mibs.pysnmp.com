# SNMP MIB module (Wellfleet-BB-MIB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-BB-MIB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:50 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
 mib_2) = mibBuilder.importSymbols(
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfGameGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfGameGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBackboneTable_Object = MibTable
wfBackboneTable = _WfBackboneTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4)
)
if mibBuilder.loadTexts:
    wfBackboneTable.setStatus("mandatory")
_WfBackboneEntry_Object = MibTableRow
wfBackboneEntry = _WfBackboneEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1)
)
wfBackboneEntry.setIndexNames(
    (0, "Wellfleet-BB-MIB-MIB", "wfBackboneSlot"),
)
if mibBuilder.loadTexts:
    wfBackboneEntry.setStatus("mandatory")
_WfBackboneSlot_Type = Integer32
_WfBackboneSlot_Object = MibTableColumn
wfBackboneSlot = _WfBackboneSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 1),
    _WfBackboneSlot_Type()
)
wfBackboneSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBackboneSlot.setStatus("mandatory")
_WfTxDropCtrSlotMask0_Type = Counter32
_WfTxDropCtrSlotMask0_Object = MibTableColumn
wfTxDropCtrSlotMask0 = _WfTxDropCtrSlotMask0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 2),
    _WfTxDropCtrSlotMask0_Type()
)
wfTxDropCtrSlotMask0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDropCtrSlotMask0.setStatus("mandatory")
_WfTxDropCtrNoGrant_Type = Counter32
_WfTxDropCtrNoGrant_Object = MibTableColumn
wfTxDropCtrNoGrant = _WfTxDropCtrNoGrant_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 3),
    _WfTxDropCtrNoGrant_Type()
)
wfTxDropCtrNoGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDropCtrNoGrant.setStatus("mandatory")
_WfTxDropCtrFlowCtrl_Type = Counter32
_WfTxDropCtrFlowCtrl_Object = MibTableColumn
wfTxDropCtrFlowCtrl = _WfTxDropCtrFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 4),
    _WfTxDropCtrFlowCtrl_Type()
)
wfTxDropCtrFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDropCtrFlowCtrl.setStatus("mandatory")
_WfTxDied_Type = Counter32
_WfTxDied_Object = MibTableColumn
wfTxDied = _WfTxDied_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 5),
    _WfTxDied_Type()
)
wfTxDied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDied.setStatus("mandatory")
_WfTxDramDied_Type = Counter32
_WfTxDramDied_Object = MibTableColumn
wfTxDramDied = _WfTxDramDied_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 6),
    _WfTxDramDied_Type()
)
wfTxDramDied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDramDied.setStatus("mandatory")
_WfTxIdleErrors_Type = Counter32
_WfTxIdleErrors_Object = MibTableColumn
wfTxIdleErrors = _WfTxIdleErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 7),
    _WfTxIdleErrors_Type()
)
wfTxIdleErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxIdleErrors.setStatus("mandatory")
_WfTxNoSomErrors_Type = Counter32
_WfTxNoSomErrors_Object = MibTableColumn
wfTxNoSomErrors = _WfTxNoSomErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 8),
    _WfTxNoSomErrors_Type()
)
wfTxNoSomErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxNoSomErrors.setStatus("mandatory")
_WfTxPktSomErrors_Type = Counter32
_WfTxPktSomErrors_Object = MibTableColumn
wfTxPktSomErrors = _WfTxPktSomErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 9),
    _WfTxPktSomErrors_Type()
)
wfTxPktSomErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxPktSomErrors.setStatus("mandatory")
_WfTxDropEomErrors_Type = Counter32
_WfTxDropEomErrors_Object = MibTableColumn
wfTxDropEomErrors = _WfTxDropEomErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 10),
    _WfTxDropEomErrors_Type()
)
wfTxDropEomErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDropEomErrors.setStatus("mandatory")
_WfTxOverflowErrors_Type = Counter32
_WfTxOverflowErrors_Object = MibTableColumn
wfTxOverflowErrors = _WfTxOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 11),
    _WfTxOverflowErrors_Type()
)
wfTxOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxOverflowErrors.setStatus("mandatory")
_WfTxSofErrors_Type = Counter32
_WfTxSofErrors_Object = MibTableColumn
wfTxSofErrors = _WfTxSofErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 12),
    _WfTxSofErrors_Type()
)
wfTxSofErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxSofErrors.setStatus("mandatory")
_WfTxDataptrErrors_Type = Counter32
_WfTxDataptrErrors_Object = MibTableColumn
wfTxDataptrErrors = _WfTxDataptrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 13),
    _WfTxDataptrErrors_Type()
)
wfTxDataptrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDataptrErrors.setStatus("mandatory")
_WfTxEndptrErrors_Type = Counter32
_WfTxEndptrErrors_Object = MibTableColumn
wfTxEndptrErrors = _WfTxEndptrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 14),
    _WfTxEndptrErrors_Type()
)
wfTxEndptrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxEndptrErrors.setStatus("mandatory")
_WfTxBoardSpeedMask_Type = Integer32
_WfTxBoardSpeedMask_Object = MibTableColumn
wfTxBoardSpeedMask = _WfTxBoardSpeedMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 15),
    _WfTxBoardSpeedMask_Type()
)
wfTxBoardSpeedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxBoardSpeedMask.setStatus("mandatory")
_WfTxErrorEnableMask_Type = Integer32
_WfTxErrorEnableMask_Object = MibTableColumn
wfTxErrorEnableMask = _WfTxErrorEnableMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 16),
    _WfTxErrorEnableMask_Type()
)
wfTxErrorEnableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxErrorEnableMask.setStatus("mandatory")
_WfTxBusRequestTimeout_Type = Integer32
_WfTxBusRequestTimeout_Object = MibTableColumn
wfTxBusRequestTimeout = _WfTxBusRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 17),
    _WfTxBusRequestTimeout_Type()
)
wfTxBusRequestTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxBusRequestTimeout.setStatus("mandatory")
_WfTxDeadlockTimeout_Type = Integer32
_WfTxDeadlockTimeout_Object = MibTableColumn
wfTxDeadlockTimeout = _WfTxDeadlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 18),
    _WfTxDeadlockTimeout_Type()
)
wfTxDeadlockTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDeadlockTimeout.setStatus("mandatory")
_WfTxIgnoreFlowCtrl_Type = Integer32
_WfTxIgnoreFlowCtrl_Object = MibTableColumn
wfTxIgnoreFlowCtrl = _WfTxIgnoreFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 19),
    _WfTxIgnoreFlowCtrl_Type()
)
wfTxIgnoreFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxIgnoreFlowCtrl.setStatus("mandatory")
_WfTxBackboneSelectMode_Type = Integer32
_WfTxBackboneSelectMode_Object = MibTableColumn
wfTxBackboneSelectMode = _WfTxBackboneSelectMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 20),
    _WfTxBackboneSelectMode_Type()
)
wfTxBackboneSelectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxBackboneSelectMode.setStatus("mandatory")
_WfTxEnableSlotMask0_Type = Integer32
_WfTxEnableSlotMask0_Object = MibTableColumn
wfTxEnableSlotMask0 = _WfTxEnableSlotMask0_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 21),
    _WfTxEnableSlotMask0_Type()
)
wfTxEnableSlotMask0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxEnableSlotMask0.setStatus("mandatory")
_WfTxFifoSize_Type = Integer32
_WfTxFifoSize_Object = MibTableColumn
wfTxFifoSize = _WfTxFifoSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 22),
    _WfTxFifoSize_Type()
)
wfTxFifoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxFifoSize.setStatus("mandatory")
_WfTxVisControl_Type = Integer32
_WfTxVisControl_Object = MibTableColumn
wfTxVisControl = _WfTxVisControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 23),
    _WfTxVisControl_Type()
)
wfTxVisControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxVisControl.setStatus("mandatory")
_WfRxPktNumErrors_Type = Counter32
_WfRxPktNumErrors_Object = MibTableColumn
wfRxPktNumErrors = _WfRxPktNumErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 24),
    _WfRxPktNumErrors_Type()
)
wfRxPktNumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxPktNumErrors.setStatus("mandatory")
_WfRxAddrOvrErrors_Type = Counter32
_WfRxAddrOvrErrors_Object = MibTableColumn
wfRxAddrOvrErrors = _WfRxAddrOvrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 25),
    _WfRxAddrOvrErrors_Type()
)
wfRxAddrOvrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxAddrOvrErrors.setStatus("mandatory")
_WfRxSomErrors_Type = Counter32
_WfRxSomErrors_Object = MibTableColumn
wfRxSomErrors = _WfRxSomErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 26),
    _WfRxSomErrors_Type()
)
wfRxSomErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxSomErrors.setStatus("mandatory")
_WfRxDied_Type = Counter32
_WfRxDied_Object = MibTableColumn
wfRxDied = _WfRxDied_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 27),
    _WfRxDied_Type()
)
wfRxDied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxDied.setStatus("mandatory")
_WfRxUnloadErrors_Type = Counter32
_WfRxUnloadErrors_Object = MibTableColumn
wfRxUnloadErrors = _WfRxUnloadErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 28),
    _WfRxUnloadErrors_Type()
)
wfRxUnloadErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxUnloadErrors.setStatus("mandatory")
_WfRxDropCtr_Type = Counter32
_WfRxDropCtr_Object = MibTableColumn
wfRxDropCtr = _WfRxDropCtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 29),
    _WfRxDropCtr_Type()
)
wfRxDropCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxDropCtr.setStatus("mandatory")
_WfRxSofErrors_Type = Counter32
_WfRxSofErrors_Object = MibTableColumn
wfRxSofErrors = _WfRxSofErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 30),
    _WfRxSofErrors_Type()
)
wfRxSofErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxSofErrors.setStatus("mandatory")
_WfRxCrcErrors_Type = Counter32
_WfRxCrcErrors_Object = MibTableColumn
wfRxCrcErrors = _WfRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 31),
    _WfRxCrcErrors_Type()
)
wfRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxCrcErrors.setStatus("mandatory")
_WfRxOvrErrors_Type = Counter32
_WfRxOvrErrors_Object = MibTableColumn
wfRxOvrErrors = _WfRxOvrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 32),
    _WfRxOvrErrors_Type()
)
wfRxOvrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxOvrErrors.setStatus("mandatory")
_WfRxForceEomErrors_Type = Counter32
_WfRxForceEomErrors_Object = MibTableColumn
wfRxForceEomErrors = _WfRxForceEomErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 33),
    _WfRxForceEomErrors_Type()
)
wfRxForceEomErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxForceEomErrors.setStatus("mandatory")
_WfRxMaxEofErrors_Type = Counter32
_WfRxMaxEofErrors_Object = MibTableColumn
wfRxMaxEofErrors = _WfRxMaxEofErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 34),
    _WfRxMaxEofErrors_Type()
)
wfRxMaxEofErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxMaxEofErrors.setStatus("mandatory")
_WfRxFifoSize_Type = Integer32
_WfRxFifoSize_Object = MibTableColumn
wfRxFifoSize = _WfRxFifoSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 35),
    _WfRxFifoSize_Type()
)
wfRxFifoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxFifoSize.setStatus("mandatory")
_WfRxReceiveMode_Type = Integer32
_WfRxReceiveMode_Object = MibTableColumn
wfRxReceiveMode = _WfRxReceiveMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 36),
    _WfRxReceiveMode_Type()
)
wfRxReceiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRxReceiveMode.setStatus("mandatory")
_WfRxIgnorePktNum_Type = Integer32
_WfRxIgnorePktNum_Object = MibTableColumn
wfRxIgnorePktNum = _WfRxIgnorePktNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 37),
    _WfRxIgnorePktNum_Type()
)
wfRxIgnorePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxIgnorePktNum.setStatus("mandatory")
_WfRxVisControl_Type = Integer32
_WfRxVisControl_Object = MibTableColumn
wfRxVisControl = _WfRxVisControl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 38),
    _WfRxVisControl_Type()
)
wfRxVisControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRxVisControl.setStatus("mandatory")
_WfRxErrorEnableMask_Type = Integer32
_WfRxErrorEnableMask_Object = MibTableColumn
wfRxErrorEnableMask = _WfRxErrorEnableMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 39),
    _WfRxErrorEnableMask_Type()
)
wfRxErrorEnableMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRxErrorEnableMask.setStatus("mandatory")
_WfRxMaxEof_Type = Integer32
_WfRxMaxEof_Object = MibTableColumn
wfRxMaxEof = _WfRxMaxEof_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 40),
    _WfRxMaxEof_Type()
)
wfRxMaxEof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxMaxEof.setStatus("mandatory")
_WfRxParitySense_Type = Integer32
_WfRxParitySense_Object = MibTableColumn
wfRxParitySense = _WfRxParitySense_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 41),
    _WfRxParitySense_Type()
)
wfRxParitySense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxParitySense.setStatus("mandatory")
_WfRxDeadlockTimeout_Type = Integer32
_WfRxDeadlockTimeout_Object = MibTableColumn
wfRxDeadlockTimeout = _WfRxDeadlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 42),
    _WfRxDeadlockTimeout_Type()
)
wfRxDeadlockTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxDeadlockTimeout.setStatus("mandatory")
_WfTxDropWB_Type = Integer32
_WfTxDropWB_Object = MibTableColumn
wfTxDropWB = _WfTxDropWB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 43),
    _WfTxDropWB_Type()
)
wfTxDropWB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDropWB.setStatus("mandatory")
_WfTxDiedNoPg_Type = Integer32
_WfTxDiedNoPg_Object = MibTableColumn
wfTxDiedNoPg = _WfTxDiedNoPg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 44),
    _WfTxDiedNoPg_Type()
)
wfTxDiedNoPg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDiedNoPg.setStatus("mandatory")
_WfTxDtbErrors_Type = Integer32
_WfTxDtbErrors_Object = MibTableColumn
wfTxDtbErrors = _WfTxDtbErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 45),
    _WfTxDtbErrors_Type()
)
wfTxDtbErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxDtbErrors.setStatus("mandatory")
_WfTxPagePtrErrors_Type = Integer32
_WfTxPagePtrErrors_Object = MibTableColumn
wfTxPagePtrErrors = _WfTxPagePtrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 46),
    _WfTxPagePtrErrors_Type()
)
wfTxPagePtrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxPagePtrErrors.setStatus("mandatory")
_WfRxWBCtr_Type = Integer32
_WfRxWBCtr_Object = MibTableColumn
wfRxWBCtr = _WfRxWBCtr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 47),
    _WfRxWBCtr_Type()
)
wfRxWBCtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxWBCtr.setStatus("mandatory")
_WfRxLinkList0Ctr_Type = Integer32
_WfRxLinkList0Ctr_Object = MibTableColumn
wfRxLinkList0Ctr = _WfRxLinkList0Ctr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 48),
    _WfRxLinkList0Ctr_Type()
)
wfRxLinkList0Ctr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxLinkList0Ctr.setStatus("mandatory")
_WfRxArbErrors_Type = Integer32
_WfRxArbErrors_Object = MibTableColumn
wfRxArbErrors = _WfRxArbErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 5, 4, 1, 49),
    _WfRxArbErrors_Type()
)
wfRxArbErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRxArbErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-BB-MIB-MIB",
    **{"wfBackboneTable": wfBackboneTable,
       "wfBackboneEntry": wfBackboneEntry,
       "wfBackboneSlot": wfBackboneSlot,
       "wfTxDropCtrSlotMask0": wfTxDropCtrSlotMask0,
       "wfTxDropCtrNoGrant": wfTxDropCtrNoGrant,
       "wfTxDropCtrFlowCtrl": wfTxDropCtrFlowCtrl,
       "wfTxDied": wfTxDied,
       "wfTxDramDied": wfTxDramDied,
       "wfTxIdleErrors": wfTxIdleErrors,
       "wfTxNoSomErrors": wfTxNoSomErrors,
       "wfTxPktSomErrors": wfTxPktSomErrors,
       "wfTxDropEomErrors": wfTxDropEomErrors,
       "wfTxOverflowErrors": wfTxOverflowErrors,
       "wfTxSofErrors": wfTxSofErrors,
       "wfTxDataptrErrors": wfTxDataptrErrors,
       "wfTxEndptrErrors": wfTxEndptrErrors,
       "wfTxBoardSpeedMask": wfTxBoardSpeedMask,
       "wfTxErrorEnableMask": wfTxErrorEnableMask,
       "wfTxBusRequestTimeout": wfTxBusRequestTimeout,
       "wfTxDeadlockTimeout": wfTxDeadlockTimeout,
       "wfTxIgnoreFlowCtrl": wfTxIgnoreFlowCtrl,
       "wfTxBackboneSelectMode": wfTxBackboneSelectMode,
       "wfTxEnableSlotMask0": wfTxEnableSlotMask0,
       "wfTxFifoSize": wfTxFifoSize,
       "wfTxVisControl": wfTxVisControl,
       "wfRxPktNumErrors": wfRxPktNumErrors,
       "wfRxAddrOvrErrors": wfRxAddrOvrErrors,
       "wfRxSomErrors": wfRxSomErrors,
       "wfRxDied": wfRxDied,
       "wfRxUnloadErrors": wfRxUnloadErrors,
       "wfRxDropCtr": wfRxDropCtr,
       "wfRxSofErrors": wfRxSofErrors,
       "wfRxCrcErrors": wfRxCrcErrors,
       "wfRxOvrErrors": wfRxOvrErrors,
       "wfRxForceEomErrors": wfRxForceEomErrors,
       "wfRxMaxEofErrors": wfRxMaxEofErrors,
       "wfRxFifoSize": wfRxFifoSize,
       "wfRxReceiveMode": wfRxReceiveMode,
       "wfRxIgnorePktNum": wfRxIgnorePktNum,
       "wfRxVisControl": wfRxVisControl,
       "wfRxErrorEnableMask": wfRxErrorEnableMask,
       "wfRxMaxEof": wfRxMaxEof,
       "wfRxParitySense": wfRxParitySense,
       "wfRxDeadlockTimeout": wfRxDeadlockTimeout,
       "wfTxDropWB": wfTxDropWB,
       "wfTxDiedNoPg": wfTxDiedNoPg,
       "wfTxDtbErrors": wfTxDtbErrors,
       "wfTxPagePtrErrors": wfTxPagePtrErrors,
       "wfRxWBCtr": wfRxWBCtr,
       "wfRxLinkList0Ctr": wfRxLinkList0Ctr,
       "wfRxArbErrors": wfRxArbErrors}
)
