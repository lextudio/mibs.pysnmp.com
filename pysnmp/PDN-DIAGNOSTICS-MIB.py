# SNMP MIB module (PDN-DIAGNOSTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DIAGNOSTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:28 2024
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

(ifIndex,
 ifTestId) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifTestId")

(pdn_diagnostics,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-diagnostics")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(AutonomousType,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DiagTestMIBObjects_ObjectIdentity = ObjectIdentity
diagTestMIBObjects = _DiagTestMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1)
)
_DiagIfTest_ObjectIdentity = ObjectIdentity
diagIfTest = _DiagIfTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1)
)
_IfLoopbackTestTable_Object = MibTable
ifLoopbackTestTable = _IfLoopbackTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ifLoopbackTestTable.setStatus("mandatory")
_IfLoopbackTestEntry_Object = MibTableRow
ifLoopbackTestEntry = _IfLoopbackTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1)
)
ifLoopbackTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifLoopbackTestEntry.setStatus("mandatory")
_LoopbackTestInputNumCycles_Type = Integer32
_LoopbackTestInputNumCycles_Object = MibTableColumn
loopbackTestInputNumCycles = _LoopbackTestInputNumCycles_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 1),
    _LoopbackTestInputNumCycles_Type()
)
loopbackTestInputNumCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopbackTestInputNumCycles.setStatus("mandatory")
_LoopbackTestResultsPktsSent_Type = Integer32
_LoopbackTestResultsPktsSent_Object = MibTableColumn
loopbackTestResultsPktsSent = _LoopbackTestResultsPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 2),
    _LoopbackTestResultsPktsSent_Type()
)
loopbackTestResultsPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsPktsSent.setStatus("mandatory")
_LoopbackTestResultsPktsRcvdOK_Type = Integer32
_LoopbackTestResultsPktsRcvdOK_Object = MibTableColumn
loopbackTestResultsPktsRcvdOK = _LoopbackTestResultsPktsRcvdOK_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 3),
    _LoopbackTestResultsPktsRcvdOK_Type()
)
loopbackTestResultsPktsRcvdOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsPktsRcvdOK.setStatus("mandatory")
_LoopbackTestResultsPktsRcvdErr_Type = Integer32
_LoopbackTestResultsPktsRcvdErr_Object = MibTableColumn
loopbackTestResultsPktsRcvdErr = _LoopbackTestResultsPktsRcvdErr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 4),
    _LoopbackTestResultsPktsRcvdErr_Type()
)
loopbackTestResultsPktsRcvdErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsPktsRcvdErr.setStatus("mandatory")
_LoopbackTestResultsPktsNotRcvd_Type = Integer32
_LoopbackTestResultsPktsNotRcvd_Object = MibTableColumn
loopbackTestResultsPktsNotRcvd = _LoopbackTestResultsPktsNotRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 5),
    _LoopbackTestResultsPktsNotRcvd_Type()
)
loopbackTestResultsPktsNotRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsPktsNotRcvd.setStatus("mandatory")


class _LoopbackTestResultsPktErrorRate_Type(DisplayString):
    """Custom type loopbackTestResultsPktErrorRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LoopbackTestResultsPktErrorRate_Type.__name__ = "DisplayString"
_LoopbackTestResultsPktErrorRate_Object = MibTableColumn
loopbackTestResultsPktErrorRate = _LoopbackTestResultsPktErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 6),
    _LoopbackTestResultsPktErrorRate_Type()
)
loopbackTestResultsPktErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsPktErrorRate.setStatus("mandatory")
_LoopbackTestResultsErrSecs_Type = Integer32
_LoopbackTestResultsErrSecs_Object = MibTableColumn
loopbackTestResultsErrSecs = _LoopbackTestResultsErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 7),
    _LoopbackTestResultsErrSecs_Type()
)
loopbackTestResultsErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsErrSecs.setStatus("mandatory")
_LoopbackTestResultsSvrErrSecs_Type = Integer32
_LoopbackTestResultsSvrErrSecs_Object = MibTableColumn
loopbackTestResultsSvrErrSecs = _LoopbackTestResultsSvrErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 8),
    _LoopbackTestResultsSvrErrSecs_Type()
)
loopbackTestResultsSvrErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsSvrErrSecs.setStatus("mandatory")
_LoopbackTestResultsElpTime_Type = Integer32
_LoopbackTestResultsElpTime_Object = MibTableColumn
loopbackTestResultsElpTime = _LoopbackTestResultsElpTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 1, 1, 9),
    _LoopbackTestResultsElpTime_Type()
)
loopbackTestResultsElpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loopbackTestResultsElpTime.setStatus("mandatory")
_IfBERTObjectsTable_Object = MibTable
ifBERTObjectsTable = _IfBERTObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ifBERTObjectsTable.setStatus("mandatory")
_IfBERTObjectsEntry_Object = MibTableRow
ifBERTObjectsEntry = _IfBERTObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1)
)
ifBERTObjectsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ifBERTObjectsEntry.setStatus("mandatory")
_IfBERTTestDuration_Type = Integer32
_IfBERTTestDuration_Object = MibTableColumn
ifBERTTestDuration = _IfBERTTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 1),
    _IfBERTTestDuration_Type()
)
ifBERTTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifBERTTestDuration.setStatus("mandatory")
_IfBERTElapsedTime_Type = Integer32
_IfBERTElapsedTime_Object = MibTableColumn
ifBERTElapsedTime = _IfBERTElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 2),
    _IfBERTElapsedTime_Type()
)
ifBERTElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTElapsedTime.setStatus("mandatory")


class _IfBERTDownSyncUP_Type(Integer32):
    """Custom type ifBERTDownSyncUP based on Integer32"""
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


_IfBERTDownSyncUP_Type.__name__ = "Integer32"
_IfBERTDownSyncUP_Object = MibTableColumn
ifBERTDownSyncUP = _IfBERTDownSyncUP_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 3),
    _IfBERTDownSyncUP_Type()
)
ifBERTDownSyncUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTDownSyncUP.setStatus("mandatory")


class _IfBERTUpSyncUP_Type(Integer32):
    """Custom type ifBERTUpSyncUP based on Integer32"""
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


_IfBERTUpSyncUP_Type.__name__ = "Integer32"
_IfBERTUpSyncUP_Object = MibTableColumn
ifBERTUpSyncUP = _IfBERTUpSyncUP_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 4),
    _IfBERTUpSyncUP_Type()
)
ifBERTUpSyncUP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTUpSyncUP.setStatus("mandatory")
_IfBERTSegmentsSent_Type = Integer32
_IfBERTSegmentsSent_Object = MibTableColumn
ifBERTSegmentsSent = _IfBERTSegmentsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 5),
    _IfBERTSegmentsSent_Type()
)
ifBERTSegmentsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTSegmentsSent.setStatus("mandatory")
_IfBERTDownMBitsRcvd_Type = Integer32
_IfBERTDownMBitsRcvd_Object = MibTableColumn
ifBERTDownMBitsRcvd = _IfBERTDownMBitsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 6),
    _IfBERTDownMBitsRcvd_Type()
)
ifBERTDownMBitsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTDownMBitsRcvd.setStatus("mandatory")
_IfBERTUpMBitsRcvd_Type = Integer32
_IfBERTUpMBitsRcvd_Object = MibTableColumn
ifBERTUpMBitsRcvd = _IfBERTUpMBitsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 7),
    _IfBERTUpMBitsRcvd_Type()
)
ifBERTUpMBitsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTUpMBitsRcvd.setStatus("mandatory")
_IfBERTDownBitErrDetected_Type = Integer32
_IfBERTDownBitErrDetected_Object = MibTableColumn
ifBERTDownBitErrDetected = _IfBERTDownBitErrDetected_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 8),
    _IfBERTDownBitErrDetected_Type()
)
ifBERTDownBitErrDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTDownBitErrDetected.setStatus("mandatory")
_IfBERTUpBitErrDetected_Type = Integer32
_IfBERTUpBitErrDetected_Object = MibTableColumn
ifBERTUpBitErrDetected = _IfBERTUpBitErrDetected_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 9),
    _IfBERTUpBitErrDetected_Type()
)
ifBERTUpBitErrDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTUpBitErrDetected.setStatus("mandatory")


class _IfBERTDownBitErrRate_Type(DisplayString):
    """Custom type ifBERTDownBitErrRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IfBERTDownBitErrRate_Type.__name__ = "DisplayString"
_IfBERTDownBitErrRate_Object = MibTableColumn
ifBERTDownBitErrRate = _IfBERTDownBitErrRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 10),
    _IfBERTDownBitErrRate_Type()
)
ifBERTDownBitErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTDownBitErrRate.setStatus("mandatory")


class _IfBERTUpBitErrRate_Type(DisplayString):
    """Custom type ifBERTUpBitErrRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_IfBERTUpBitErrRate_Type.__name__ = "DisplayString"
_IfBERTUpBitErrRate_Object = MibTableColumn
ifBERTUpBitErrRate = _IfBERTUpBitErrRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 11),
    _IfBERTUpBitErrRate_Type()
)
ifBERTUpBitErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTUpBitErrRate.setStatus("mandatory")
_IfBERTDownErroredSecs_Type = Integer32
_IfBERTDownErroredSecs_Object = MibTableColumn
ifBERTDownErroredSecs = _IfBERTDownErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 12),
    _IfBERTDownErroredSecs_Type()
)
ifBERTDownErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTDownErroredSecs.setStatus("mandatory")
_IfBERTUpErroredSecs_Type = Integer32
_IfBERTUpErroredSecs_Object = MibTableColumn
ifBERTUpErroredSecs = _IfBERTUpErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 13),
    _IfBERTUpErroredSecs_Type()
)
ifBERTUpErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTUpErroredSecs.setStatus("mandatory")
_IfBERTDownLineRate_Type = Integer32
_IfBERTDownLineRate_Object = MibTableColumn
ifBERTDownLineRate = _IfBERTDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 14),
    _IfBERTDownLineRate_Type()
)
ifBERTDownLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTDownLineRate.setStatus("mandatory")
_IfBERTUpLineRate_Type = Integer32
_IfBERTUpLineRate_Object = MibTableColumn
ifBERTUpLineRate = _IfBERTUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 15),
    _IfBERTUpLineRate_Type()
)
ifBERTUpLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTUpLineRate.setStatus("mandatory")
_IfBERTDownMargin_Type = Integer32
_IfBERTDownMargin_Object = MibTableColumn
ifBERTDownMargin = _IfBERTDownMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 16),
    _IfBERTDownMargin_Type()
)
ifBERTDownMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTDownMargin.setStatus("mandatory")
_IfBERTUpMargin_Type = Integer32
_IfBERTUpMargin_Object = MibTableColumn
ifBERTUpMargin = _IfBERTUpMargin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 1, 2, 1, 17),
    _IfBERTUpMargin_Type()
)
ifBERTUpMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifBERTUpMargin.setStatus("mandatory")
_DiagApplTest_ObjectIdentity = ObjectIdentity
diagApplTest = _DiagApplTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2)
)
_ApplMaxNumberOfTests_Type = Integer32
_ApplMaxNumberOfTests_Object = MibScalar
applMaxNumberOfTests = _ApplMaxNumberOfTests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 1),
    _ApplMaxNumberOfTests_Type()
)
applMaxNumberOfTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applMaxNumberOfTests.setStatus("mandatory")
_ApplCurrentNumberOfTests_Type = Integer32
_ApplCurrentNumberOfTests_Object = MibScalar
applCurrentNumberOfTests = _ApplCurrentNumberOfTests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 2),
    _ApplCurrentNumberOfTests_Type()
)
applCurrentNumberOfTests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applCurrentNumberOfTests.setStatus("mandatory")


class _ApplStopAllTests_Type(Integer32):
    """Custom type applStopAllTests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("stop", 2),
          ("stopAndClear", 3))
    )


_ApplStopAllTests_Type.__name__ = "Integer32"
_ApplStopAllTests_Object = MibScalar
applStopAllTests = _ApplStopAllTests_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 3),
    _ApplStopAllTests_Type()
)
applStopAllTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applStopAllTests.setStatus("mandatory")
_ApplNewTestId_Type = Integer32
_ApplNewTestId_Object = MibScalar
applNewTestId = _ApplNewTestId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 4),
    _ApplNewTestId_Type()
)
applNewTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applNewTestId.setStatus("mandatory")
_ApplTestStatusTable_Object = MibTable
applTestStatusTable = _ApplTestStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5)
)
if mibBuilder.loadTexts:
    applTestStatusTable.setStatus("mandatory")
_ApplTestStatusEntry_Object = MibTableRow
applTestStatusEntry = _ApplTestStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5, 1)
)
applTestStatusEntry.setIndexNames(
    (0, "PDN-DIAGNOSTICS-MIB", "applTestId"),
)
if mibBuilder.loadTexts:
    applTestStatusEntry.setStatus("mandatory")
_ApplTestId_Type = Integer32
_ApplTestId_Object = MibTableColumn
applTestId = _ApplTestId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5, 1, 1),
    _ApplTestId_Type()
)
applTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTestId.setStatus("mandatory")
_ApplTestType_Type = AutonomousType
_ApplTestType_Object = MibTableColumn
applTestType = _ApplTestType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5, 1, 2),
    _ApplTestType_Type()
)
applTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTestType.setStatus("mandatory")


class _ApplTestStatus_Type(Integer32):
    """Custom type applTestStatus based on Integer32"""
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
        *(("abort", 5),
          ("failed", 4),
          ("inProgress", 2),
          ("none", 1),
          ("success", 3))
    )


_ApplTestStatus_Type.__name__ = "Integer32"
_ApplTestStatus_Object = MibTableColumn
applTestStatus = _ApplTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5, 1, 3),
    _ApplTestStatus_Type()
)
applTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTestStatus.setStatus("mandatory")


class _ApplTestErrorCode_Type(Integer32):
    """Custom type applTestErrorCode based on Integer32"""
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
        *(("icmpError", 3),
          ("none", 1),
          ("systemError", 4),
          ("timeout", 2))
    )


_ApplTestErrorCode_Type.__name__ = "Integer32"
_ApplTestErrorCode_Object = MibTableColumn
applTestErrorCode = _ApplTestErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5, 1, 4),
    _ApplTestErrorCode_Type()
)
applTestErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTestErrorCode.setStatus("mandatory")


class _ApplTestOwner_Type(DisplayString):
    """Custom type applTestOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_ApplTestOwner_Type.__name__ = "DisplayString"
_ApplTestOwner_Object = MibTableColumn
applTestOwner = _ApplTestOwner_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5, 1, 5),
    _ApplTestOwner_Type()
)
applTestOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTestOwner.setStatus("mandatory")
_ApplTestRowStatus_Type = RowStatus
_ApplTestRowStatus_Object = MibTableColumn
applTestRowStatus = _ApplTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 5, 1, 6),
    _ApplTestRowStatus_Type()
)
applTestRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTestRowStatus.setStatus("mandatory")
_ApplPingTestTable_Object = MibTable
applPingTestTable = _ApplPingTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6)
)
if mibBuilder.loadTexts:
    applPingTestTable.setStatus("mandatory")
_ApplPingTestEntry_Object = MibTableRow
applPingTestEntry = _ApplPingTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1)
)
applPingTestEntry.setIndexNames(
    (0, "PDN-DIAGNOSTICS-MIB", "applPingTestId"),
)
if mibBuilder.loadTexts:
    applPingTestEntry.setStatus("mandatory")
_ApplPingTestId_Type = Integer32
_ApplPingTestId_Object = MibTableColumn
applPingTestId = _ApplPingTestId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 1),
    _ApplPingTestId_Type()
)
applPingTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPingTestId.setStatus("mandatory")
_ApplPingTestIpAddress_Type = IpAddress
_ApplPingTestIpAddress_Object = MibTableColumn
applPingTestIpAddress = _ApplPingTestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 2),
    _ApplPingTestIpAddress_Type()
)
applPingTestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPingTestIpAddress.setStatus("mandatory")
_ApplPingTestSourceIpAddr_Type = IpAddress
_ApplPingTestSourceIpAddr_Object = MibTableColumn
applPingTestSourceIpAddr = _ApplPingTestSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 3),
    _ApplPingTestSourceIpAddr_Type()
)
applPingTestSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPingTestSourceIpAddr.setStatus("mandatory")
_ApplPingTestPacketSize_Type = Integer32
_ApplPingTestPacketSize_Object = MibTableColumn
applPingTestPacketSize = _ApplPingTestPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 4),
    _ApplPingTestPacketSize_Type()
)
applPingTestPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPingTestPacketSize.setStatus("mandatory")
_ApplPingTestTimeout_Type = Integer32
_ApplPingTestTimeout_Object = MibTableColumn
applPingTestTimeout = _ApplPingTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 5),
    _ApplPingTestTimeout_Type()
)
applPingTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPingTestTimeout.setStatus("mandatory")
_ApplPingTestMaxPings_Type = Integer32
_ApplPingTestMaxPings_Object = MibTableColumn
applPingTestMaxPings = _ApplPingTestMaxPings_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 6),
    _ApplPingTestMaxPings_Type()
)
applPingTestMaxPings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPingTestMaxPings.setStatus("mandatory")
_ApplPingTestPktsSent_Type = Integer32
_ApplPingTestPktsSent_Object = MibTableColumn
applPingTestPktsSent = _ApplPingTestPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 7),
    _ApplPingTestPktsSent_Type()
)
applPingTestPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPingTestPktsSent.setStatus("mandatory")
_ApplPingTestPktsRecv_Type = Integer32
_ApplPingTestPktsRecv_Object = MibTableColumn
applPingTestPktsRecv = _ApplPingTestPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 8),
    _ApplPingTestPktsRecv_Type()
)
applPingTestPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPingTestPktsRecv.setStatus("mandatory")
_ApplPingTestMinTime_Type = Integer32
_ApplPingTestMinTime_Object = MibTableColumn
applPingTestMinTime = _ApplPingTestMinTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 9),
    _ApplPingTestMinTime_Type()
)
applPingTestMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPingTestMinTime.setStatus("mandatory")
_ApplPingTestMaxTime_Type = Integer32
_ApplPingTestMaxTime_Object = MibTableColumn
applPingTestMaxTime = _ApplPingTestMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 10),
    _ApplPingTestMaxTime_Type()
)
applPingTestMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPingTestMaxTime.setStatus("mandatory")
_ApplPingTestAvgTime_Type = Integer32
_ApplPingTestAvgTime_Object = MibTableColumn
applPingTestAvgTime = _ApplPingTestAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 11),
    _ApplPingTestAvgTime_Type()
)
applPingTestAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applPingTestAvgTime.setStatus("mandatory")


class _ApplPingTestDomain_Type(Integer32):
    """Custom type applPingTestDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgmt", 2),
          ("noop", 1),
          ("service", 3))
    )


_ApplPingTestDomain_Type.__name__ = "Integer32"
_ApplPingTestDomain_Object = MibTableColumn
applPingTestDomain = _ApplPingTestDomain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 12),
    _ApplPingTestDomain_Type()
)
applPingTestDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPingTestDomain.setStatus("mandatory")
_ApplPingTestIfIndex_Type = Integer32
_ApplPingTestIfIndex_Object = MibTableColumn
applPingTestIfIndex = _ApplPingTestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 6, 1, 13),
    _ApplPingTestIfIndex_Type()
)
applPingTestIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applPingTestIfIndex.setStatus("mandatory")
_ApplTracerouteConfigTable_Object = MibTable
applTracerouteConfigTable = _ApplTracerouteConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7)
)
if mibBuilder.loadTexts:
    applTracerouteConfigTable.setStatus("mandatory")
_ApplTracerouteConfigEntry_Object = MibTableRow
applTracerouteConfigEntry = _ApplTracerouteConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1)
)
applTracerouteConfigEntry.setIndexNames(
    (0, "PDN-DIAGNOSTICS-MIB", "applTracerouteTestId"),
)
if mibBuilder.loadTexts:
    applTracerouteConfigEntry.setStatus("mandatory")
_ApplTracerouteTestId_Type = Integer32
_ApplTracerouteTestId_Object = MibTableColumn
applTracerouteTestId = _ApplTracerouteTestId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 1),
    _ApplTracerouteTestId_Type()
)
applTracerouteTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTracerouteTestId.setStatus("mandatory")
_ApplTracerouteIpAddress_Type = IpAddress
_ApplTracerouteIpAddress_Object = MibTableColumn
applTracerouteIpAddress = _ApplTracerouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 2),
    _ApplTracerouteIpAddress_Type()
)
applTracerouteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTracerouteIpAddress.setStatus("mandatory")
_ApplTracerouteSourceIpAddr_Type = IpAddress
_ApplTracerouteSourceIpAddr_Object = MibTableColumn
applTracerouteSourceIpAddr = _ApplTracerouteSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 3),
    _ApplTracerouteSourceIpAddr_Type()
)
applTracerouteSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTracerouteSourceIpAddr.setStatus("mandatory")
_ApplTraceroutePktsSize_Type = Integer32
_ApplTraceroutePktsSize_Object = MibTableColumn
applTraceroutePktsSize = _ApplTraceroutePktsSize_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 4),
    _ApplTraceroutePktsSize_Type()
)
applTraceroutePktsSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTraceroutePktsSize.setStatus("mandatory")
_ApplTracerouteTimeout_Type = Integer32
_ApplTracerouteTimeout_Object = MibTableColumn
applTracerouteTimeout = _ApplTracerouteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 5),
    _ApplTracerouteTimeout_Type()
)
applTracerouteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTracerouteTimeout.setStatus("mandatory")
_ApplTracerouteMaxHops_Type = Integer32
_ApplTracerouteMaxHops_Object = MibTableColumn
applTracerouteMaxHops = _ApplTracerouteMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 6),
    _ApplTracerouteMaxHops_Type()
)
applTracerouteMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTracerouteMaxHops.setStatus("mandatory")


class _ApplTracerouteDomain_Type(Integer32):
    """Custom type applTracerouteDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mgmt", 2),
          ("noop", 1),
          ("service", 3))
    )


_ApplTracerouteDomain_Type.__name__ = "Integer32"
_ApplTracerouteDomain_Object = MibTableColumn
applTracerouteDomain = _ApplTracerouteDomain_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 7),
    _ApplTracerouteDomain_Type()
)
applTracerouteDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTracerouteDomain.setStatus("mandatory")
_ApplTracerouteIfIndex_Type = Integer32
_ApplTracerouteIfIndex_Object = MibTableColumn
applTracerouteIfIndex = _ApplTracerouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 7, 1, 8),
    _ApplTracerouteIfIndex_Type()
)
applTracerouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    applTracerouteIfIndex.setStatus("mandatory")
_ApplTracerouteResultTable_Object = MibTable
applTracerouteResultTable = _ApplTracerouteResultTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8)
)
if mibBuilder.loadTexts:
    applTracerouteResultTable.setStatus("mandatory")
_ApplTracerouteResultEntry_Object = MibTableRow
applTracerouteResultEntry = _ApplTracerouteResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1)
)
applTracerouteResultEntry.setIndexNames(
    (0, "PDN-DIAGNOSTICS-MIB", "applTracerouteResultTestId"),
    (0, "PDN-DIAGNOSTICS-MIB", "applTracerouteHopCount"),
)
if mibBuilder.loadTexts:
    applTracerouteResultEntry.setStatus("mandatory")
_ApplTracerouteResultTestId_Type = Integer32
_ApplTracerouteResultTestId_Object = MibTableColumn
applTracerouteResultTestId = _ApplTracerouteResultTestId_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1, 1),
    _ApplTracerouteResultTestId_Type()
)
applTracerouteResultTestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTracerouteResultTestId.setStatus("mandatory")
_ApplTracerouteHopCount_Type = Integer32
_ApplTracerouteHopCount_Object = MibTableColumn
applTracerouteHopCount = _ApplTracerouteHopCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1, 2),
    _ApplTracerouteHopCount_Type()
)
applTracerouteHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTracerouteHopCount.setStatus("mandatory")
_ApplTracerouteIpAddr_Type = IpAddress
_ApplTracerouteIpAddr_Object = MibTableColumn
applTracerouteIpAddr = _ApplTracerouteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1, 3),
    _ApplTracerouteIpAddr_Type()
)
applTracerouteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTracerouteIpAddr.setStatus("mandatory")
_ApplTraceroutePktSize_Type = Integer32
_ApplTraceroutePktSize_Object = MibTableColumn
applTraceroutePktSize = _ApplTraceroutePktSize_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1, 4),
    _ApplTraceroutePktSize_Type()
)
applTraceroutePktSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTraceroutePktSize.setStatus("mandatory")
_ApplTracerouteProbe1RTT_Type = Integer32
_ApplTracerouteProbe1RTT_Object = MibTableColumn
applTracerouteProbe1RTT = _ApplTracerouteProbe1RTT_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1, 5),
    _ApplTracerouteProbe1RTT_Type()
)
applTracerouteProbe1RTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTracerouteProbe1RTT.setStatus("mandatory")
_ApplTracerouteProbe2RTT_Type = Integer32
_ApplTracerouteProbe2RTT_Object = MibTableColumn
applTracerouteProbe2RTT = _ApplTracerouteProbe2RTT_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1, 6),
    _ApplTracerouteProbe2RTT_Type()
)
applTracerouteProbe2RTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTracerouteProbe2RTT.setStatus("mandatory")
_ApplTracerouteProbe3RTT_Type = Integer32
_ApplTracerouteProbe3RTT_Object = MibTableColumn
applTracerouteProbe3RTT = _ApplTracerouteProbe3RTT_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 2, 8, 1, 7),
    _ApplTracerouteProbe3RTT_Type()
)
applTracerouteProbe3RTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    applTracerouteProbe3RTT.setStatus("mandatory")
_DiagTest_ObjectIdentity = ObjectIdentity
diagTest = _DiagTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 3)
)
_DiagTestTrapEnable_Type = Integer32
_DiagTestTrapEnable_Object = MibScalar
diagTestTrapEnable = _DiagTestTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 1, 3, 1),
    _DiagTestTrapEnable_Type()
)
diagTestTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diagTestTrapEnable.setStatus("mandatory")
_DiagTestMIBTraps_ObjectIdentity = ObjectIdentity
diagTestMIBTraps = _DiagTestMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 2)
)

# Managed Objects groups


# Notification objects

diagApplTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 2, 0, 1)
)
diagApplTestStart.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-DIAGNOSTICS-MIB", "applTestId"),
        ("PDN-DIAGNOSTICS-MIB", "applTestType"))
)
if mibBuilder.loadTexts:
    diagApplTestStart.setStatus(
        ""
    )

diagIfTestStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 2, 0, 2)
)
diagIfTestStart.setObjects(
    ("IF-MIB", "ifTestId")
)
if mibBuilder.loadTexts:
    diagIfTestStart.setStatus(
        ""
    )

diagApplTestStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 2, 0, 101)
)
diagApplTestStop.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("PDN-DIAGNOSTICS-MIB", "applTestId"),
        ("PDN-DIAGNOSTICS-MIB", "applTestType"),
        ("PDN-DIAGNOSTICS-MIB", "applTestStatus"))
)
if mibBuilder.loadTexts:
    diagApplTestStop.setStatus(
        ""
    )

diagIfTestOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 16, 2, 0, 102)
)
diagIfTestOver.setObjects(
    ("IF-MIB", "ifTestId")
)
if mibBuilder.loadTexts:
    diagIfTestOver.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DIAGNOSTICS-MIB",
    **{"diagTestMIBObjects": diagTestMIBObjects,
       "diagIfTest": diagIfTest,
       "ifLoopbackTestTable": ifLoopbackTestTable,
       "ifLoopbackTestEntry": ifLoopbackTestEntry,
       "loopbackTestInputNumCycles": loopbackTestInputNumCycles,
       "loopbackTestResultsPktsSent": loopbackTestResultsPktsSent,
       "loopbackTestResultsPktsRcvdOK": loopbackTestResultsPktsRcvdOK,
       "loopbackTestResultsPktsRcvdErr": loopbackTestResultsPktsRcvdErr,
       "loopbackTestResultsPktsNotRcvd": loopbackTestResultsPktsNotRcvd,
       "loopbackTestResultsPktErrorRate": loopbackTestResultsPktErrorRate,
       "loopbackTestResultsErrSecs": loopbackTestResultsErrSecs,
       "loopbackTestResultsSvrErrSecs": loopbackTestResultsSvrErrSecs,
       "loopbackTestResultsElpTime": loopbackTestResultsElpTime,
       "ifBERTObjectsTable": ifBERTObjectsTable,
       "ifBERTObjectsEntry": ifBERTObjectsEntry,
       "ifBERTTestDuration": ifBERTTestDuration,
       "ifBERTElapsedTime": ifBERTElapsedTime,
       "ifBERTDownSyncUP": ifBERTDownSyncUP,
       "ifBERTUpSyncUP": ifBERTUpSyncUP,
       "ifBERTSegmentsSent": ifBERTSegmentsSent,
       "ifBERTDownMBitsRcvd": ifBERTDownMBitsRcvd,
       "ifBERTUpMBitsRcvd": ifBERTUpMBitsRcvd,
       "ifBERTDownBitErrDetected": ifBERTDownBitErrDetected,
       "ifBERTUpBitErrDetected": ifBERTUpBitErrDetected,
       "ifBERTDownBitErrRate": ifBERTDownBitErrRate,
       "ifBERTUpBitErrRate": ifBERTUpBitErrRate,
       "ifBERTDownErroredSecs": ifBERTDownErroredSecs,
       "ifBERTUpErroredSecs": ifBERTUpErroredSecs,
       "ifBERTDownLineRate": ifBERTDownLineRate,
       "ifBERTUpLineRate": ifBERTUpLineRate,
       "ifBERTDownMargin": ifBERTDownMargin,
       "ifBERTUpMargin": ifBERTUpMargin,
       "diagApplTest": diagApplTest,
       "applMaxNumberOfTests": applMaxNumberOfTests,
       "applCurrentNumberOfTests": applCurrentNumberOfTests,
       "applStopAllTests": applStopAllTests,
       "applNewTestId": applNewTestId,
       "applTestStatusTable": applTestStatusTable,
       "applTestStatusEntry": applTestStatusEntry,
       "applTestId": applTestId,
       "applTestType": applTestType,
       "applTestStatus": applTestStatus,
       "applTestErrorCode": applTestErrorCode,
       "applTestOwner": applTestOwner,
       "applTestRowStatus": applTestRowStatus,
       "applPingTestTable": applPingTestTable,
       "applPingTestEntry": applPingTestEntry,
       "applPingTestId": applPingTestId,
       "applPingTestIpAddress": applPingTestIpAddress,
       "applPingTestSourceIpAddr": applPingTestSourceIpAddr,
       "applPingTestPacketSize": applPingTestPacketSize,
       "applPingTestTimeout": applPingTestTimeout,
       "applPingTestMaxPings": applPingTestMaxPings,
       "applPingTestPktsSent": applPingTestPktsSent,
       "applPingTestPktsRecv": applPingTestPktsRecv,
       "applPingTestMinTime": applPingTestMinTime,
       "applPingTestMaxTime": applPingTestMaxTime,
       "applPingTestAvgTime": applPingTestAvgTime,
       "applPingTestDomain": applPingTestDomain,
       "applPingTestIfIndex": applPingTestIfIndex,
       "applTracerouteConfigTable": applTracerouteConfigTable,
       "applTracerouteConfigEntry": applTracerouteConfigEntry,
       "applTracerouteTestId": applTracerouteTestId,
       "applTracerouteIpAddress": applTracerouteIpAddress,
       "applTracerouteSourceIpAddr": applTracerouteSourceIpAddr,
       "applTraceroutePktsSize": applTraceroutePktsSize,
       "applTracerouteTimeout": applTracerouteTimeout,
       "applTracerouteMaxHops": applTracerouteMaxHops,
       "applTracerouteDomain": applTracerouteDomain,
       "applTracerouteIfIndex": applTracerouteIfIndex,
       "applTracerouteResultTable": applTracerouteResultTable,
       "applTracerouteResultEntry": applTracerouteResultEntry,
       "applTracerouteResultTestId": applTracerouteResultTestId,
       "applTracerouteHopCount": applTracerouteHopCount,
       "applTracerouteIpAddr": applTracerouteIpAddr,
       "applTraceroutePktSize": applTraceroutePktSize,
       "applTracerouteProbe1RTT": applTracerouteProbe1RTT,
       "applTracerouteProbe2RTT": applTracerouteProbe2RTT,
       "applTracerouteProbe3RTT": applTracerouteProbe3RTT,
       "diagTest": diagTest,
       "diagTestTrapEnable": diagTestTrapEnable,
       "diagTestMIBTraps": diagTestMIBTraps,
       "diagApplTestStart": diagApplTestStart,
       "diagIfTestStart": diagIfTestStart,
       "diagApplTestStop": diagApplTestStop,
       "diagIfTestOver": diagIfTestOver}
)
