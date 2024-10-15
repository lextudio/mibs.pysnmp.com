# SNMP MIB module (ATROPOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATROPOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:14 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

atroposMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 75, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LP_ObjectIdentity = ObjectIdentity
lP = _LP_ObjectIdentity(
    (1, 3, 6, 1, 3, 75, 4, 1)
)
_LPTable_Object = MibTable
lPTable = _LPTable_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1)
)
if mibBuilder.loadTexts:
    lPTable.setStatus("current")
_LPEntry_Object = MibTableRow
lPEntry = _LPEntry_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1)
)
lPEntry.setIndexNames(
    (0, "ATROPOS-MIB", "lPIndex"),
)
if mibBuilder.loadTexts:
    lPEntry.setStatus("current")


class _LPIndex_Type(Integer32):
    """Custom type lPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPIndex_Type.__name__ = "Integer32"
_LPIndex_Object = MibTableColumn
lPIndex = _LPIndex_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 1),
    _LPIndex_Type()
)
lPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lPIndex.setStatus("current")
_LPID_Type = DisplayString
_LPID_Object = MibTableColumn
lPID = _LPID_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 2),
    _LPID_Type()
)
lPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPID.setStatus("current")


class _LPLVT_Type(Integer32):
    """Custom type lPLVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPLVT_Type.__name__ = "Integer32"
_LPLVT_Object = MibTableColumn
lPLVT = _LPLVT_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 3),
    _LPLVT_Type()
)
lPLVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPLVT.setStatus("current")


class _LPQRSize_Type(Integer32):
    """Custom type lPQRSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPQRSize_Type.__name__ = "Integer32"
_LPQRSize_Object = MibTableColumn
lPQRSize = _LPQRSize_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 4),
    _LPQRSize_Type()
)
lPQRSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPQRSize.setStatus("current")


class _LPQSSize_Type(Integer32):
    """Custom type lPQSSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPQSSize_Type.__name__ = "Integer32"
_LPQSSize_Object = MibTableColumn
lPQSSize = _LPQSSize_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 5),
    _LPQSSize_Type()
)
lPQSSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPQSSize.setStatus("current")


class _LPCausalityRollbacks_Type(Integer32):
    """Custom type lPCausalityRollbacks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPCausalityRollbacks_Type.__name__ = "Integer32"
_LPCausalityRollbacks_Object = MibTableColumn
lPCausalityRollbacks = _LPCausalityRollbacks_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 6),
    _LPCausalityRollbacks_Type()
)
lPCausalityRollbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPCausalityRollbacks.setStatus("current")


class _LPToleranceRollbacks_Type(Integer32):
    """Custom type lPToleranceRollbacks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPToleranceRollbacks_Type.__name__ = "Integer32"
_LPToleranceRollbacks_Object = MibTableColumn
lPToleranceRollbacks = _LPToleranceRollbacks_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 7),
    _LPToleranceRollbacks_Type()
)
lPToleranceRollbacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPToleranceRollbacks.setStatus("current")


class _LPSQSize_Type(Integer32):
    """Custom type lPSQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPSQSize_Type.__name__ = "Integer32"
_LPSQSize_Object = MibTableColumn
lPSQSize = _LPSQSize_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 8),
    _LPSQSize_Type()
)
lPSQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPSQSize.setStatus("current")


class _LPTolerance_Type(Integer32):
    """Custom type lPTolerance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPTolerance_Type.__name__ = "Integer32"
_LPTolerance_Object = MibTableColumn
lPTolerance = _LPTolerance_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 9),
    _LPTolerance_Type()
)
lPTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPTolerance.setStatus("current")


class _LPGVT_Type(Integer32):
    """Custom type lPGVT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPGVT_Type.__name__ = "Integer32"
_LPGVT_Object = MibTableColumn
lPGVT = _LPGVT_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 10),
    _LPGVT_Type()
)
lPGVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPGVT.setStatus("current")


class _LPLookAhead_Type(Integer32):
    """Custom type lPLookAhead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPLookAhead_Type.__name__ = "Integer32"
_LPLookAhead_Object = MibTableColumn
lPLookAhead = _LPLookAhead_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 11),
    _LPLookAhead_Type()
)
lPLookAhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPLookAhead.setStatus("current")


class _LPGvtUpdate_Type(Integer32):
    """Custom type lPGvtUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPGvtUpdate_Type.__name__ = "Integer32"
_LPGvtUpdate_Object = MibTableColumn
lPGvtUpdate = _LPGvtUpdate_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 12),
    _LPGvtUpdate_Type()
)
lPGvtUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPGvtUpdate.setStatus("current")


class _LPStepSize_Type(Integer32):
    """Custom type lPStepSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPStepSize_Type.__name__ = "Integer32"
_LPStepSize_Object = MibTableColumn
lPStepSize = _LPStepSize_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 13),
    _LPStepSize_Type()
)
lPStepSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPStepSize.setStatus("current")


class _LPReal_Type(Integer32):
    """Custom type lPReal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPReal_Type.__name__ = "Integer32"
_LPReal_Object = MibTableColumn
lPReal = _LPReal_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 14),
    _LPReal_Type()
)
lPReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPReal.setStatus("current")


class _LPVirtual_Type(Integer32):
    """Custom type lPVirtual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPVirtual_Type.__name__ = "Integer32"
_LPVirtual_Object = MibTableColumn
lPVirtual = _LPVirtual_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 15),
    _LPVirtual_Type()
)
lPVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPVirtual.setStatus("current")


class _LPNumPkts_Type(Integer32):
    """Custom type lPNumPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPNumPkts_Type.__name__ = "Integer32"
_LPNumPkts_Object = MibTableColumn
lPNumPkts = _LPNumPkts_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 16),
    _LPNumPkts_Type()
)
lPNumPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPNumPkts.setStatus("current")


class _LPNumAnti_Type(Integer32):
    """Custom type lPNumAnti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPNumAnti_Type.__name__ = "Integer32"
_LPNumAnti_Object = MibTableColumn
lPNumAnti = _LPNumAnti_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 17),
    _LPNumAnti_Type()
)
lPNumAnti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPNumAnti.setStatus("current")
_LPPredAcc_Type = DisplayString
_LPPredAcc_Object = MibTableColumn
lPPredAcc = _LPPredAcc_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 18),
    _LPPredAcc_Type()
)
lPPredAcc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPPredAcc.setStatus("current")
_LPPropX_Type = DisplayString
_LPPropX_Object = MibTableColumn
lPPropX = _LPPropX_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 19),
    _LPPropX_Type()
)
lPPropX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPPropX.setStatus("current")
_LPPropY_Type = DisplayString
_LPPropY_Object = MibTableColumn
lPPropY = _LPPropY_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 20),
    _LPPropY_Type()
)
lPPropY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPPropY.setStatus("current")
_LPETask_Type = DisplayString
_LPETask_Object = MibTableColumn
lPETask = _LPETask_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 21),
    _LPETask_Type()
)
lPETask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPETask.setStatus("current")
_LPETrb_Type = DisplayString
_LPETrb_Object = MibTableColumn
lPETrb = _LPETrb_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 22),
    _LPETrb_Type()
)
lPETrb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPETrb.setStatus("current")
_LPVmRate_Type = DisplayString
_LPVmRate_Object = MibTableColumn
lPVmRate = _LPVmRate_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 23),
    _LPVmRate_Type()
)
lPVmRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPVmRate.setStatus("current")
_LPReRate_Type = DisplayString
_LPReRate_Object = MibTableColumn
lPReRate = _LPReRate_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 24),
    _LPReRate_Type()
)
lPReRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPReRate.setStatus("current")
_LPSpeedup_Type = DisplayString
_LPSpeedup_Object = MibTableColumn
lPSpeedup = _LPSpeedup_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 25),
    _LPSpeedup_Type()
)
lPSpeedup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPSpeedup.setStatus("current")
_LPLookahead_Type = DisplayString
_LPLookahead_Object = MibTableColumn
lPLookahead = _LPLookahead_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 26),
    _LPLookahead_Type()
)
lPLookahead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPLookahead.setStatus("current")


class _LPNumNoState_Type(Integer32):
    """Custom type lPNumNoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPNumNoState_Type.__name__ = "Integer32"
_LPNumNoState_Object = MibTableColumn
lPNumNoState = _LPNumNoState_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 27),
    _LPNumNoState_Type()
)
lPNumNoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPNumNoState.setStatus("current")
_LPStatePred_Type = DisplayString
_LPStatePred_Object = MibTableColumn
lPStatePred = _LPStatePred_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 28),
    _LPStatePred_Type()
)
lPStatePred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPStatePred.setStatus("current")
_LPPktPred_Type = DisplayString
_LPPktPred_Object = MibTableColumn
lPPktPred = _LPPktPred_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 29),
    _LPPktPred_Type()
)
lPPktPred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPPktPred.setStatus("current")
_LPTdiff_Type = DisplayString
_LPTdiff_Object = MibTableColumn
lPTdiff = _LPTdiff_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 30),
    _LPTdiff_Type()
)
lPTdiff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPTdiff.setStatus("current")
_LPStateError_Type = DisplayString
_LPStateError_Object = MibTableColumn
lPStateError = _LPStateError_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 31),
    _LPStateError_Type()
)
lPStateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPStateError.setStatus("current")


class _LPUptime_Type(Integer32):
    """Custom type lPUptime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LPUptime_Type.__name__ = "Integer32"
_LPUptime_Object = MibTableColumn
lPUptime = _LPUptime_Object(
    (1, 3, 6, 1, 3, 75, 4, 1, 1, 1, 32),
    _LPUptime_Type()
)
lPUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lPUptime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATROPOS-MIB",
    **{"atroposMIB": atroposMIB,
       "lP": lP,
       "lPTable": lPTable,
       "lPEntry": lPEntry,
       "lPIndex": lPIndex,
       "lPID": lPID,
       "lPLVT": lPLVT,
       "lPQRSize": lPQRSize,
       "lPQSSize": lPQSSize,
       "lPCausalityRollbacks": lPCausalityRollbacks,
       "lPToleranceRollbacks": lPToleranceRollbacks,
       "lPSQSize": lPSQSize,
       "lPTolerance": lPTolerance,
       "lPGVT": lPGVT,
       "lPLookAhead": lPLookAhead,
       "lPGvtUpdate": lPGvtUpdate,
       "lPStepSize": lPStepSize,
       "lPReal": lPReal,
       "lPVirtual": lPVirtual,
       "lPNumPkts": lPNumPkts,
       "lPNumAnti": lPNumAnti,
       "lPPredAcc": lPPredAcc,
       "lPPropX": lPPropX,
       "lPPropY": lPPropY,
       "lPETask": lPETask,
       "lPETrb": lPETrb,
       "lPVmRate": lPVmRate,
       "lPReRate": lPReRate,
       "lPSpeedup": lPSpeedup,
       "lPLookahead": lPLookahead,
       "lPNumNoState": lPNumNoState,
       "lPStatePred": lPStatePred,
       "lPPktPred": lPPktPred,
       "lPTdiff": lPTdiff,
       "lPStateError": lPStateError,
       "lPUptime": lPUptime}
)
