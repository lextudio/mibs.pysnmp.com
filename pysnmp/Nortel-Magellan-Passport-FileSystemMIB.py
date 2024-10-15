# SNMP MIB module (Nortel-Magellan-Passport-FileSystemMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-FileSystemMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:41 2024
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

(DisplayString,
 Gauge32,
 Integer32,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "NonReplicated")

(components,
 passportMIBs) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "components",
    "passportMIBs")

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

_Fs_ObjectIdentity = ObjectIdentity
fs = _Fs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15)
)
_FsRowStatusTable_Object = MibTable
fsRowStatusTable = _FsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1)
)
if mibBuilder.loadTexts:
    fsRowStatusTable.setStatus("mandatory")
_FsRowStatusEntry_Object = MibTableRow
fsRowStatusEntry = _FsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1)
)
fsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
)
if mibBuilder.loadTexts:
    fsRowStatusEntry.setStatus("mandatory")
_FsRowStatus_Type = RowStatus
_FsRowStatus_Object = MibTableColumn
fsRowStatus = _FsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 1),
    _FsRowStatus_Type()
)
fsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRowStatus.setStatus("mandatory")
_FsComponentName_Type = DisplayString
_FsComponentName_Object = MibTableColumn
fsComponentName = _FsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 2),
    _FsComponentName_Type()
)
fsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsComponentName.setStatus("mandatory")
_FsStorageType_Type = StorageType
_FsStorageType_Object = MibTableColumn
fsStorageType = _FsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 4),
    _FsStorageType_Type()
)
fsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStorageType.setStatus("mandatory")
_FsIndex_Type = NonReplicated
_FsIndex_Object = MibTableColumn
fsIndex = _FsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 1, 1, 10),
    _FsIndex_Type()
)
fsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIndex.setStatus("mandatory")
_FsDisk_ObjectIdentity = ObjectIdentity
fsDisk = _FsDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2)
)
_FsDiskRowStatusTable_Object = MibTable
fsDiskRowStatusTable = _FsDiskRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    fsDiskRowStatusTable.setStatus("mandatory")
_FsDiskRowStatusEntry_Object = MibTableRow
fsDiskRowStatusEntry = _FsDiskRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1)
)
fsDiskRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"),
)
if mibBuilder.loadTexts:
    fsDiskRowStatusEntry.setStatus("mandatory")
_FsDiskRowStatus_Type = RowStatus
_FsDiskRowStatus_Object = MibTableColumn
fsDiskRowStatus = _FsDiskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 1),
    _FsDiskRowStatus_Type()
)
fsDiskRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskRowStatus.setStatus("mandatory")
_FsDiskComponentName_Type = DisplayString
_FsDiskComponentName_Object = MibTableColumn
fsDiskComponentName = _FsDiskComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 2),
    _FsDiskComponentName_Type()
)
fsDiskComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskComponentName.setStatus("mandatory")
_FsDiskStorageType_Type = StorageType
_FsDiskStorageType_Object = MibTableColumn
fsDiskStorageType = _FsDiskStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 4),
    _FsDiskStorageType_Type()
)
fsDiskStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskStorageType.setStatus("mandatory")


class _FsDiskIndex_Type(Integer32):
    """Custom type fsDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FsDiskIndex_Type.__name__ = "Integer32"
_FsDiskIndex_Object = MibTableColumn
fsDiskIndex = _FsDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 1, 1, 10),
    _FsDiskIndex_Type()
)
fsDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiskIndex.setStatus("mandatory")
_FsDiskTest_ObjectIdentity = ObjectIdentity
fsDiskTest = _FsDiskTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2)
)
_FsDiskTestRowStatusTable_Object = MibTable
fsDiskTestRowStatusTable = _FsDiskTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fsDiskTestRowStatusTable.setStatus("mandatory")
_FsDiskTestRowStatusEntry_Object = MibTableRow
fsDiskTestRowStatusEntry = _FsDiskTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1)
)
fsDiskTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    fsDiskTestRowStatusEntry.setStatus("mandatory")
_FsDiskTestRowStatus_Type = RowStatus
_FsDiskTestRowStatus_Object = MibTableColumn
fsDiskTestRowStatus = _FsDiskTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 1),
    _FsDiskTestRowStatus_Type()
)
fsDiskTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestRowStatus.setStatus("mandatory")
_FsDiskTestComponentName_Type = DisplayString
_FsDiskTestComponentName_Object = MibTableColumn
fsDiskTestComponentName = _FsDiskTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 2),
    _FsDiskTestComponentName_Type()
)
fsDiskTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestComponentName.setStatus("mandatory")
_FsDiskTestStorageType_Type = StorageType
_FsDiskTestStorageType_Object = MibTableColumn
fsDiskTestStorageType = _FsDiskTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 4),
    _FsDiskTestStorageType_Type()
)
fsDiskTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestStorageType.setStatus("mandatory")
_FsDiskTestIndex_Type = NonReplicated
_FsDiskTestIndex_Object = MibTableColumn
fsDiskTestIndex = _FsDiskTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 1, 1, 10),
    _FsDiskTestIndex_Type()
)
fsDiskTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDiskTestIndex.setStatus("mandatory")
_FsDiskTestStateTable_Object = MibTable
fsDiskTestStateTable = _FsDiskTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10)
)
if mibBuilder.loadTexts:
    fsDiskTestStateTable.setStatus("mandatory")
_FsDiskTestStateEntry_Object = MibTableRow
fsDiskTestStateEntry = _FsDiskTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1)
)
fsDiskTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    fsDiskTestStateEntry.setStatus("mandatory")


class _FsDiskTestAdminState_Type(Integer32):
    """Custom type fsDiskTestAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_FsDiskTestAdminState_Type.__name__ = "Integer32"
_FsDiskTestAdminState_Object = MibTableColumn
fsDiskTestAdminState = _FsDiskTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1, 1),
    _FsDiskTestAdminState_Type()
)
fsDiskTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestAdminState.setStatus("mandatory")


class _FsDiskTestOperationalState_Type(Integer32):
    """Custom type fsDiskTestOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsDiskTestOperationalState_Type.__name__ = "Integer32"
_FsDiskTestOperationalState_Object = MibTableColumn
fsDiskTestOperationalState = _FsDiskTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1, 2),
    _FsDiskTestOperationalState_Type()
)
fsDiskTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestOperationalState.setStatus("mandatory")


class _FsDiskTestUsageState_Type(Integer32):
    """Custom type fsDiskTestUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_FsDiskTestUsageState_Type.__name__ = "Integer32"
_FsDiskTestUsageState_Object = MibTableColumn
fsDiskTestUsageState = _FsDiskTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 10, 1, 3),
    _FsDiskTestUsageState_Type()
)
fsDiskTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestUsageState.setStatus("mandatory")
_FsDiskTestSetupTable_Object = MibTable
fsDiskTestSetupTable = _FsDiskTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11)
)
if mibBuilder.loadTexts:
    fsDiskTestSetupTable.setStatus("mandatory")
_FsDiskTestSetupEntry_Object = MibTableRow
fsDiskTestSetupEntry = _FsDiskTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1)
)
fsDiskTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    fsDiskTestSetupEntry.setStatus("mandatory")


class _FsDiskTestTestCount_Type(Unsigned32):
    """Custom type fsDiskTestTestCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsDiskTestTestCount_Type.__name__ = "Unsigned32"
_FsDiskTestTestCount_Object = MibTableColumn
fsDiskTestTestCount = _FsDiskTestTestCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1, 1),
    _FsDiskTestTestCount_Type()
)
fsDiskTestTestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiskTestTestCount.setStatus("mandatory")


class _FsDiskTestDuration_Type(Unsigned32):
    """Custom type fsDiskTestDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35791394),
    )


_FsDiskTestDuration_Type.__name__ = "Unsigned32"
_FsDiskTestDuration_Object = MibTableColumn
fsDiskTestDuration = _FsDiskTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1, 2),
    _FsDiskTestDuration_Type()
)
fsDiskTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiskTestDuration.setStatus("mandatory")


class _FsDiskTestType_Type(Integer32):
    """Custom type fsDiskTestType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diskRead", 1),
          ("filesystemCheck", 0),
          ("flakyBitDetection", 2),
          ("surfaceAnalysis", 3))
    )


_FsDiskTestType_Type.__name__ = "Integer32"
_FsDiskTestType_Object = MibTableColumn
fsDiskTestType = _FsDiskTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 11, 1, 3),
    _FsDiskTestType_Type()
)
fsDiskTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiskTestType.setStatus("mandatory")
_FsDiskTestResultsTable_Object = MibTable
fsDiskTestResultsTable = _FsDiskTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12)
)
if mibBuilder.loadTexts:
    fsDiskTestResultsTable.setStatus("mandatory")
_FsDiskTestResultsEntry_Object = MibTableRow
fsDiskTestResultsEntry = _FsDiskTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1)
)
fsDiskTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    fsDiskTestResultsEntry.setStatus("mandatory")


class _FsDiskTestCauseOfTermination_Type(Integer32):
    """Custom type fsDiskTestCauseOfTermination based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("error", 5),
          ("internalError", 6),
          ("neverStarted", 3),
          ("stoppedByOperator", 2),
          ("testCountReached", 0),
          ("testRunning", 4),
          ("testTimeExpired", 1),
          ("unknown", 7))
    )


_FsDiskTestCauseOfTermination_Type.__name__ = "Integer32"
_FsDiskTestCauseOfTermination_Object = MibTableColumn
fsDiskTestCauseOfTermination = _FsDiskTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 1),
    _FsDiskTestCauseOfTermination_Type()
)
fsDiskTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestCauseOfTermination.setStatus("mandatory")


class _FsDiskTestNatureOfError_Type(Integer32):
    """Custom type fsDiskTestNatureOfError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failedToComplete", 3),
          ("logical", 0),
          ("media", 1),
          ("noErrorDetected", 2))
    )


_FsDiskTestNatureOfError_Type.__name__ = "Integer32"
_FsDiskTestNatureOfError_Object = MibTableColumn
fsDiskTestNatureOfError = _FsDiskTestNatureOfError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 2),
    _FsDiskTestNatureOfError_Type()
)
fsDiskTestNatureOfError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestNatureOfError.setStatus("mandatory")


class _FsDiskTestSeverity_Type(Integer32):
    """Custom type fsDiskTestSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dataLost", 1),
          ("hardwareProblem", 2),
          ("noDataLost", 0),
          ("noError", 3))
    )


_FsDiskTestSeverity_Type.__name__ = "Integer32"
_FsDiskTestSeverity_Object = MibTableColumn
fsDiskTestSeverity = _FsDiskTestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 3),
    _FsDiskTestSeverity_Type()
)
fsDiskTestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestSeverity.setStatus("mandatory")


class _FsDiskTestElapsedTime_Type(Unsigned32):
    """Custom type fsDiskTestElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsDiskTestElapsedTime_Type.__name__ = "Unsigned32"
_FsDiskTestElapsedTime_Object = MibTableColumn
fsDiskTestElapsedTime = _FsDiskTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 4),
    _FsDiskTestElapsedTime_Type()
)
fsDiskTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestElapsedTime.setStatus("mandatory")


class _FsDiskTestTestExecutionCount_Type(Unsigned32):
    """Custom type fsDiskTestTestExecutionCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsDiskTestTestExecutionCount_Type.__name__ = "Unsigned32"
_FsDiskTestTestExecutionCount_Object = MibTableColumn
fsDiskTestTestExecutionCount = _FsDiskTestTestExecutionCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 2, 12, 1, 5),
    _FsDiskTestTestExecutionCount_Type()
)
fsDiskTestTestExecutionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskTestTestExecutionCount.setStatus("mandatory")
_FsDiskStateTable_Object = MibTable
fsDiskStateTable = _FsDiskStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10)
)
if mibBuilder.loadTexts:
    fsDiskStateTable.setStatus("mandatory")
_FsDiskStateEntry_Object = MibTableRow
fsDiskStateEntry = _FsDiskStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1)
)
fsDiskStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"),
)
if mibBuilder.loadTexts:
    fsDiskStateEntry.setStatus("mandatory")


class _FsDiskAdminState_Type(Integer32):
    """Custom type fsDiskAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_FsDiskAdminState_Type.__name__ = "Integer32"
_FsDiskAdminState_Object = MibTableColumn
fsDiskAdminState = _FsDiskAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1, 1),
    _FsDiskAdminState_Type()
)
fsDiskAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskAdminState.setStatus("mandatory")


class _FsDiskOperationalState_Type(Integer32):
    """Custom type fsDiskOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsDiskOperationalState_Type.__name__ = "Integer32"
_FsDiskOperationalState_Object = MibTableColumn
fsDiskOperationalState = _FsDiskOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1, 2),
    _FsDiskOperationalState_Type()
)
fsDiskOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskOperationalState.setStatus("mandatory")


class _FsDiskUsageState_Type(Integer32):
    """Custom type fsDiskUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_FsDiskUsageState_Type.__name__ = "Integer32"
_FsDiskUsageState_Object = MibTableColumn
fsDiskUsageState = _FsDiskUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 10, 1, 3),
    _FsDiskUsageState_Type()
)
fsDiskUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskUsageState.setStatus("mandatory")
_FsDiskOperTable_Object = MibTable
fsDiskOperTable = _FsDiskOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11)
)
if mibBuilder.loadTexts:
    fsDiskOperTable.setStatus("mandatory")
_FsDiskOperEntry_Object = MibTableRow
fsDiskOperEntry = _FsDiskOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1)
)
fsDiskOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsDiskIndex"),
)
if mibBuilder.loadTexts:
    fsDiskOperEntry.setStatus("mandatory")


class _FsDiskVolumeName_Type(AsciiString):
    """Custom type fsDiskVolumeName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_FsDiskVolumeName_Type.__name__ = "AsciiString"
_FsDiskVolumeName_Object = MibTableColumn
fsDiskVolumeName = _FsDiskVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 1),
    _FsDiskVolumeName_Type()
)
fsDiskVolumeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiskVolumeName.setStatus("mandatory")


class _FsDiskCapacity_Type(Unsigned32):
    """Custom type fsDiskCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsDiskCapacity_Type.__name__ = "Unsigned32"
_FsDiskCapacity_Object = MibTableColumn
fsDiskCapacity = _FsDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 2),
    _FsDiskCapacity_Type()
)
fsDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskCapacity.setStatus("mandatory")


class _FsDiskFreeSpace_Type(Unsigned32):
    """Custom type fsDiskFreeSpace based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsDiskFreeSpace_Type.__name__ = "Unsigned32"
_FsDiskFreeSpace_Object = MibTableColumn
fsDiskFreeSpace = _FsDiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 3),
    _FsDiskFreeSpace_Type()
)
fsDiskFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskFreeSpace.setStatus("mandatory")


class _FsDiskBadBlocksPercentage_Type(Gauge32):
    """Custom type fsDiskBadBlocksPercentage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsDiskBadBlocksPercentage_Type.__name__ = "Gauge32"
_FsDiskBadBlocksPercentage_Object = MibTableColumn
fsDiskBadBlocksPercentage = _FsDiskBadBlocksPercentage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 4),
    _FsDiskBadBlocksPercentage_Type()
)
fsDiskBadBlocksPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskBadBlocksPercentage.setStatus("mandatory")


class _FsDiskUnformattedCapacity_Type(Unsigned32):
    """Custom type fsDiskUnformattedCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsDiskUnformattedCapacity_Type.__name__ = "Unsigned32"
_FsDiskUnformattedCapacity_Object = MibTableColumn
fsDiskUnformattedCapacity = _FsDiskUnformattedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 2, 11, 1, 5),
    _FsDiskUnformattedCapacity_Type()
)
fsDiskUnformattedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiskUnformattedCapacity.setStatus("mandatory")
_FsStateTable_Object = MibTable
fsStateTable = _FsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10)
)
if mibBuilder.loadTexts:
    fsStateTable.setStatus("mandatory")
_FsStateEntry_Object = MibTableRow
fsStateEntry = _FsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1)
)
fsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
)
if mibBuilder.loadTexts:
    fsStateEntry.setStatus("mandatory")


class _FsAdminState_Type(Integer32):
    """Custom type fsAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_FsAdminState_Type.__name__ = "Integer32"
_FsAdminState_Object = MibTableColumn
fsAdminState = _FsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1, 1),
    _FsAdminState_Type()
)
fsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAdminState.setStatus("mandatory")


class _FsOperationalState_Type(Integer32):
    """Custom type fsOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_FsOperationalState_Type.__name__ = "Integer32"
_FsOperationalState_Object = MibTableColumn
fsOperationalState = _FsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1, 2),
    _FsOperationalState_Type()
)
fsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOperationalState.setStatus("mandatory")


class _FsUsageState_Type(Integer32):
    """Custom type fsUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_FsUsageState_Type.__name__ = "Integer32"
_FsUsageState_Object = MibTableColumn
fsUsageState = _FsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 10, 1, 3),
    _FsUsageState_Type()
)
fsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUsageState.setStatus("mandatory")
_FsOperTable_Object = MibTable
fsOperTable = _FsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11)
)
if mibBuilder.loadTexts:
    fsOperTable.setStatus("mandatory")
_FsOperEntry_Object = MibTableRow
fsOperEntry = _FsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1)
)
fsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-FileSystemMIB", "fsIndex"),
)
if mibBuilder.loadTexts:
    fsOperEntry.setStatus("mandatory")


class _FsVolumeName_Type(AsciiString):
    """Custom type fsVolumeName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_FsVolumeName_Type.__name__ = "AsciiString"
_FsVolumeName_Object = MibTableColumn
fsVolumeName = _FsVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 1),
    _FsVolumeName_Type()
)
fsVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVolumeName.setStatus("mandatory")
_FsActiveDisk_Type = RowPointer
_FsActiveDisk_Object = MibTableColumn
fsActiveDisk = _FsActiveDisk_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 2),
    _FsActiveDisk_Type()
)
fsActiveDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsActiveDisk.setStatus("mandatory")


class _FsSyncStatus_Type(Integer32):
    """Custom type fsSyncStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("synchronized", 0),
          ("synchronizing", 2),
          ("unSynchronized", 1))
    )


_FsSyncStatus_Type.__name__ = "Integer32"
_FsSyncStatus_Object = MibTableColumn
fsSyncStatus = _FsSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 3),
    _FsSyncStatus_Type()
)
fsSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncStatus.setStatus("mandatory")


class _FsSyncProgress_Type(Gauge32):
    """Custom type fsSyncProgress based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsSyncProgress_Type.__name__ = "Gauge32"
_FsSyncProgress_Object = MibTableColumn
fsSyncProgress = _FsSyncProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 4),
    _FsSyncProgress_Type()
)
fsSyncProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSyncProgress.setStatus("mandatory")


class _FsCapacity_Type(Unsigned32):
    """Custom type fsCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsCapacity_Type.__name__ = "Unsigned32"
_FsCapacity_Object = MibTableColumn
fsCapacity = _FsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 5),
    _FsCapacity_Type()
)
fsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCapacity.setStatus("mandatory")


class _FsFreeSpace_Type(Unsigned32):
    """Custom type fsFreeSpace based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsFreeSpace_Type.__name__ = "Unsigned32"
_FsFreeSpace_Object = MibTableColumn
fsFreeSpace = _FsFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 6),
    _FsFreeSpace_Type()
)
fsFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFreeSpace.setStatus("mandatory")


class _FsUsage_Type(Gauge32):
    """Custom type fsUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsUsage_Type.__name__ = "Gauge32"
_FsUsage_Object = MibTableColumn
fsUsage = _FsUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 15, 11, 1, 7),
    _FsUsage_Type()
)
fsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUsage.setStatus("mandatory")
_FileSystemMIB_ObjectIdentity = ObjectIdentity
fileSystemMIB = _FileSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16)
)
_FileSystemGroup_ObjectIdentity = ObjectIdentity
fileSystemGroup = _FileSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1)
)
_FileSystemGroupBD_ObjectIdentity = ObjectIdentity
fileSystemGroupBD = _FileSystemGroupBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1, 4)
)
_FileSystemGroupBD00_ObjectIdentity = ObjectIdentity
fileSystemGroupBD00 = _FileSystemGroupBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1, 4, 1)
)
_FileSystemGroupBD00A_ObjectIdentity = ObjectIdentity
fileSystemGroupBD00A = _FileSystemGroupBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 1, 4, 1, 2)
)
_FileSystemCapabilities_ObjectIdentity = ObjectIdentity
fileSystemCapabilities = _FileSystemCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3)
)
_FileSystemCapabilitiesBD_ObjectIdentity = ObjectIdentity
fileSystemCapabilitiesBD = _FileSystemCapabilitiesBD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3, 4)
)
_FileSystemCapabilitiesBD00_ObjectIdentity = ObjectIdentity
fileSystemCapabilitiesBD00 = _FileSystemCapabilitiesBD00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3, 4, 1)
)
_FileSystemCapabilitiesBD00A_ObjectIdentity = ObjectIdentity
fileSystemCapabilitiesBD00A = _FileSystemCapabilitiesBD00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 16, 3, 4, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-FileSystemMIB",
    **{"fs": fs,
       "fsRowStatusTable": fsRowStatusTable,
       "fsRowStatusEntry": fsRowStatusEntry,
       "fsRowStatus": fsRowStatus,
       "fsComponentName": fsComponentName,
       "fsStorageType": fsStorageType,
       "fsIndex": fsIndex,
       "fsDisk": fsDisk,
       "fsDiskRowStatusTable": fsDiskRowStatusTable,
       "fsDiskRowStatusEntry": fsDiskRowStatusEntry,
       "fsDiskRowStatus": fsDiskRowStatus,
       "fsDiskComponentName": fsDiskComponentName,
       "fsDiskStorageType": fsDiskStorageType,
       "fsDiskIndex": fsDiskIndex,
       "fsDiskTest": fsDiskTest,
       "fsDiskTestRowStatusTable": fsDiskTestRowStatusTable,
       "fsDiskTestRowStatusEntry": fsDiskTestRowStatusEntry,
       "fsDiskTestRowStatus": fsDiskTestRowStatus,
       "fsDiskTestComponentName": fsDiskTestComponentName,
       "fsDiskTestStorageType": fsDiskTestStorageType,
       "fsDiskTestIndex": fsDiskTestIndex,
       "fsDiskTestStateTable": fsDiskTestStateTable,
       "fsDiskTestStateEntry": fsDiskTestStateEntry,
       "fsDiskTestAdminState": fsDiskTestAdminState,
       "fsDiskTestOperationalState": fsDiskTestOperationalState,
       "fsDiskTestUsageState": fsDiskTestUsageState,
       "fsDiskTestSetupTable": fsDiskTestSetupTable,
       "fsDiskTestSetupEntry": fsDiskTestSetupEntry,
       "fsDiskTestTestCount": fsDiskTestTestCount,
       "fsDiskTestDuration": fsDiskTestDuration,
       "fsDiskTestType": fsDiskTestType,
       "fsDiskTestResultsTable": fsDiskTestResultsTable,
       "fsDiskTestResultsEntry": fsDiskTestResultsEntry,
       "fsDiskTestCauseOfTermination": fsDiskTestCauseOfTermination,
       "fsDiskTestNatureOfError": fsDiskTestNatureOfError,
       "fsDiskTestSeverity": fsDiskTestSeverity,
       "fsDiskTestElapsedTime": fsDiskTestElapsedTime,
       "fsDiskTestTestExecutionCount": fsDiskTestTestExecutionCount,
       "fsDiskStateTable": fsDiskStateTable,
       "fsDiskStateEntry": fsDiskStateEntry,
       "fsDiskAdminState": fsDiskAdminState,
       "fsDiskOperationalState": fsDiskOperationalState,
       "fsDiskUsageState": fsDiskUsageState,
       "fsDiskOperTable": fsDiskOperTable,
       "fsDiskOperEntry": fsDiskOperEntry,
       "fsDiskVolumeName": fsDiskVolumeName,
       "fsDiskCapacity": fsDiskCapacity,
       "fsDiskFreeSpace": fsDiskFreeSpace,
       "fsDiskBadBlocksPercentage": fsDiskBadBlocksPercentage,
       "fsDiskUnformattedCapacity": fsDiskUnformattedCapacity,
       "fsStateTable": fsStateTable,
       "fsStateEntry": fsStateEntry,
       "fsAdminState": fsAdminState,
       "fsOperationalState": fsOperationalState,
       "fsUsageState": fsUsageState,
       "fsOperTable": fsOperTable,
       "fsOperEntry": fsOperEntry,
       "fsVolumeName": fsVolumeName,
       "fsActiveDisk": fsActiveDisk,
       "fsSyncStatus": fsSyncStatus,
       "fsSyncProgress": fsSyncProgress,
       "fsCapacity": fsCapacity,
       "fsFreeSpace": fsFreeSpace,
       "fsUsage": fsUsage,
       "fileSystemMIB": fileSystemMIB,
       "fileSystemGroup": fileSystemGroup,
       "fileSystemGroupBD": fileSystemGroupBD,
       "fileSystemGroupBD00": fileSystemGroupBD00,
       "fileSystemGroupBD00A": fileSystemGroupBD00A,
       "fileSystemCapabilities": fileSystemCapabilities,
       "fileSystemCapabilitiesBD": fileSystemCapabilitiesBD,
       "fileSystemCapabilitiesBD00": fileSystemCapabilitiesBD00,
       "fileSystemCapabilitiesBD00A": fileSystemCapabilitiesBD00A}
)
