# SNMP MIB module (Nortel-MsCarrier-MscPassport-FileSystemMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-FileSystemMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:21 2024
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
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "NonReplicated")

(mscComponents,
 mscPassportMIBs) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscComponents",
    "mscPassportMIBs")

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

_MscFs_ObjectIdentity = ObjectIdentity
mscFs = _MscFs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15)
)
_MscFsRowStatusTable_Object = MibTable
mscFsRowStatusTable = _MscFsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    mscFsRowStatusTable.setStatus("mandatory")
_MscFsRowStatusEntry_Object = MibTableRow
mscFsRowStatusEntry = _MscFsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1)
)
mscFsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
)
if mibBuilder.loadTexts:
    mscFsRowStatusEntry.setStatus("mandatory")
_MscFsRowStatus_Type = RowStatus
_MscFsRowStatus_Object = MibTableColumn
mscFsRowStatus = _MscFsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 1),
    _MscFsRowStatus_Type()
)
mscFsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsRowStatus.setStatus("mandatory")
_MscFsComponentName_Type = DisplayString
_MscFsComponentName_Object = MibTableColumn
mscFsComponentName = _MscFsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 2),
    _MscFsComponentName_Type()
)
mscFsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsComponentName.setStatus("mandatory")
_MscFsStorageType_Type = StorageType
_MscFsStorageType_Object = MibTableColumn
mscFsStorageType = _MscFsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 4),
    _MscFsStorageType_Type()
)
mscFsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsStorageType.setStatus("mandatory")
_MscFsIndex_Type = NonReplicated
_MscFsIndex_Object = MibTableColumn
mscFsIndex = _MscFsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 1, 1, 10),
    _MscFsIndex_Type()
)
mscFsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFsIndex.setStatus("mandatory")
_MscFsDisk_ObjectIdentity = ObjectIdentity
mscFsDisk = _MscFsDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2)
)
_MscFsDiskRowStatusTable_Object = MibTable
mscFsDiskRowStatusTable = _MscFsDiskRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    mscFsDiskRowStatusTable.setStatus("mandatory")
_MscFsDiskRowStatusEntry_Object = MibTableRow
mscFsDiskRowStatusEntry = _MscFsDiskRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1)
)
mscFsDiskRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"),
)
if mibBuilder.loadTexts:
    mscFsDiskRowStatusEntry.setStatus("mandatory")
_MscFsDiskRowStatus_Type = RowStatus
_MscFsDiskRowStatus_Object = MibTableColumn
mscFsDiskRowStatus = _MscFsDiskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 1),
    _MscFsDiskRowStatus_Type()
)
mscFsDiskRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskRowStatus.setStatus("mandatory")
_MscFsDiskComponentName_Type = DisplayString
_MscFsDiskComponentName_Object = MibTableColumn
mscFsDiskComponentName = _MscFsDiskComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 2),
    _MscFsDiskComponentName_Type()
)
mscFsDiskComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskComponentName.setStatus("mandatory")
_MscFsDiskStorageType_Type = StorageType
_MscFsDiskStorageType_Object = MibTableColumn
mscFsDiskStorageType = _MscFsDiskStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 4),
    _MscFsDiskStorageType_Type()
)
mscFsDiskStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskStorageType.setStatus("mandatory")


class _MscFsDiskIndex_Type(Integer32):
    """Custom type mscFsDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MscFsDiskIndex_Type.__name__ = "Integer32"
_MscFsDiskIndex_Object = MibTableColumn
mscFsDiskIndex = _MscFsDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 1, 1, 10),
    _MscFsDiskIndex_Type()
)
mscFsDiskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFsDiskIndex.setStatus("mandatory")
_MscFsDiskTest_ObjectIdentity = ObjectIdentity
mscFsDiskTest = _MscFsDiskTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2)
)
_MscFsDiskTestRowStatusTable_Object = MibTable
mscFsDiskTestRowStatusTable = _MscFsDiskTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mscFsDiskTestRowStatusTable.setStatus("mandatory")
_MscFsDiskTestRowStatusEntry_Object = MibTableRow
mscFsDiskTestRowStatusEntry = _MscFsDiskTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1)
)
mscFsDiskTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    mscFsDiskTestRowStatusEntry.setStatus("mandatory")
_MscFsDiskTestRowStatus_Type = RowStatus
_MscFsDiskTestRowStatus_Object = MibTableColumn
mscFsDiskTestRowStatus = _MscFsDiskTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 1),
    _MscFsDiskTestRowStatus_Type()
)
mscFsDiskTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestRowStatus.setStatus("mandatory")
_MscFsDiskTestComponentName_Type = DisplayString
_MscFsDiskTestComponentName_Object = MibTableColumn
mscFsDiskTestComponentName = _MscFsDiskTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 2),
    _MscFsDiskTestComponentName_Type()
)
mscFsDiskTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestComponentName.setStatus("mandatory")
_MscFsDiskTestStorageType_Type = StorageType
_MscFsDiskTestStorageType_Object = MibTableColumn
mscFsDiskTestStorageType = _MscFsDiskTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 4),
    _MscFsDiskTestStorageType_Type()
)
mscFsDiskTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestStorageType.setStatus("mandatory")
_MscFsDiskTestIndex_Type = NonReplicated
_MscFsDiskTestIndex_Object = MibTableColumn
mscFsDiskTestIndex = _MscFsDiskTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 1, 1, 10),
    _MscFsDiskTestIndex_Type()
)
mscFsDiskTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscFsDiskTestIndex.setStatus("mandatory")
_MscFsDiskTestStateTable_Object = MibTable
mscFsDiskTestStateTable = _MscFsDiskTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mscFsDiskTestStateTable.setStatus("mandatory")
_MscFsDiskTestStateEntry_Object = MibTableRow
mscFsDiskTestStateEntry = _MscFsDiskTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1)
)
mscFsDiskTestStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    mscFsDiskTestStateEntry.setStatus("mandatory")


class _MscFsDiskTestAdminState_Type(Integer32):
    """Custom type mscFsDiskTestAdminState based on Integer32"""
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


_MscFsDiskTestAdminState_Type.__name__ = "Integer32"
_MscFsDiskTestAdminState_Object = MibTableColumn
mscFsDiskTestAdminState = _MscFsDiskTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1, 1),
    _MscFsDiskTestAdminState_Type()
)
mscFsDiskTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestAdminState.setStatus("mandatory")


class _MscFsDiskTestOperationalState_Type(Integer32):
    """Custom type mscFsDiskTestOperationalState based on Integer32"""
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


_MscFsDiskTestOperationalState_Type.__name__ = "Integer32"
_MscFsDiskTestOperationalState_Object = MibTableColumn
mscFsDiskTestOperationalState = _MscFsDiskTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1, 2),
    _MscFsDiskTestOperationalState_Type()
)
mscFsDiskTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestOperationalState.setStatus("mandatory")


class _MscFsDiskTestUsageState_Type(Integer32):
    """Custom type mscFsDiskTestUsageState based on Integer32"""
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


_MscFsDiskTestUsageState_Type.__name__ = "Integer32"
_MscFsDiskTestUsageState_Object = MibTableColumn
mscFsDiskTestUsageState = _MscFsDiskTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 10, 1, 3),
    _MscFsDiskTestUsageState_Type()
)
mscFsDiskTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestUsageState.setStatus("mandatory")
_MscFsDiskTestSetupTable_Object = MibTable
mscFsDiskTestSetupTable = _MscFsDiskTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11)
)
if mibBuilder.loadTexts:
    mscFsDiskTestSetupTable.setStatus("mandatory")
_MscFsDiskTestSetupEntry_Object = MibTableRow
mscFsDiskTestSetupEntry = _MscFsDiskTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1)
)
mscFsDiskTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    mscFsDiskTestSetupEntry.setStatus("mandatory")


class _MscFsDiskTestTestCount_Type(Unsigned32):
    """Custom type mscFsDiskTestTestCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsDiskTestTestCount_Type.__name__ = "Unsigned32"
_MscFsDiskTestTestCount_Object = MibTableColumn
mscFsDiskTestTestCount = _MscFsDiskTestTestCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1, 1),
    _MscFsDiskTestTestCount_Type()
)
mscFsDiskTestTestCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFsDiskTestTestCount.setStatus("mandatory")


class _MscFsDiskTestDuration_Type(Unsigned32):
    """Custom type mscFsDiskTestDuration based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 35791394),
    )


_MscFsDiskTestDuration_Type.__name__ = "Unsigned32"
_MscFsDiskTestDuration_Object = MibTableColumn
mscFsDiskTestDuration = _MscFsDiskTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1, 2),
    _MscFsDiskTestDuration_Type()
)
mscFsDiskTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFsDiskTestDuration.setStatus("mandatory")


class _MscFsDiskTestType_Type(Integer32):
    """Custom type mscFsDiskTestType based on Integer32"""
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


_MscFsDiskTestType_Type.__name__ = "Integer32"
_MscFsDiskTestType_Object = MibTableColumn
mscFsDiskTestType = _MscFsDiskTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 11, 1, 3),
    _MscFsDiskTestType_Type()
)
mscFsDiskTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFsDiskTestType.setStatus("mandatory")
_MscFsDiskTestResultsTable_Object = MibTable
mscFsDiskTestResultsTable = _MscFsDiskTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12)
)
if mibBuilder.loadTexts:
    mscFsDiskTestResultsTable.setStatus("mandatory")
_MscFsDiskTestResultsEntry_Object = MibTableRow
mscFsDiskTestResultsEntry = _MscFsDiskTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1)
)
mscFsDiskTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskTestIndex"),
)
if mibBuilder.loadTexts:
    mscFsDiskTestResultsEntry.setStatus("mandatory")


class _MscFsDiskTestCauseOfTermination_Type(Integer32):
    """Custom type mscFsDiskTestCauseOfTermination based on Integer32"""
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


_MscFsDiskTestCauseOfTermination_Type.__name__ = "Integer32"
_MscFsDiskTestCauseOfTermination_Object = MibTableColumn
mscFsDiskTestCauseOfTermination = _MscFsDiskTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 1),
    _MscFsDiskTestCauseOfTermination_Type()
)
mscFsDiskTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestCauseOfTermination.setStatus("mandatory")


class _MscFsDiskTestNatureOfError_Type(Integer32):
    """Custom type mscFsDiskTestNatureOfError based on Integer32"""
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


_MscFsDiskTestNatureOfError_Type.__name__ = "Integer32"
_MscFsDiskTestNatureOfError_Object = MibTableColumn
mscFsDiskTestNatureOfError = _MscFsDiskTestNatureOfError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 2),
    _MscFsDiskTestNatureOfError_Type()
)
mscFsDiskTestNatureOfError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestNatureOfError.setStatus("mandatory")


class _MscFsDiskTestSeverity_Type(Integer32):
    """Custom type mscFsDiskTestSeverity based on Integer32"""
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


_MscFsDiskTestSeverity_Type.__name__ = "Integer32"
_MscFsDiskTestSeverity_Object = MibTableColumn
mscFsDiskTestSeverity = _MscFsDiskTestSeverity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 3),
    _MscFsDiskTestSeverity_Type()
)
mscFsDiskTestSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestSeverity.setStatus("mandatory")


class _MscFsDiskTestElapsedTime_Type(Unsigned32):
    """Custom type mscFsDiskTestElapsedTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsDiskTestElapsedTime_Type.__name__ = "Unsigned32"
_MscFsDiskTestElapsedTime_Object = MibTableColumn
mscFsDiskTestElapsedTime = _MscFsDiskTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 4),
    _MscFsDiskTestElapsedTime_Type()
)
mscFsDiskTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestElapsedTime.setStatus("mandatory")


class _MscFsDiskTestTestExecutionCount_Type(Unsigned32):
    """Custom type mscFsDiskTestTestExecutionCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsDiskTestTestExecutionCount_Type.__name__ = "Unsigned32"
_MscFsDiskTestTestExecutionCount_Object = MibTableColumn
mscFsDiskTestTestExecutionCount = _MscFsDiskTestTestExecutionCount_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 2, 12, 1, 5),
    _MscFsDiskTestTestExecutionCount_Type()
)
mscFsDiskTestTestExecutionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskTestTestExecutionCount.setStatus("mandatory")
_MscFsDiskStateTable_Object = MibTable
mscFsDiskStateTable = _MscFsDiskStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10)
)
if mibBuilder.loadTexts:
    mscFsDiskStateTable.setStatus("mandatory")
_MscFsDiskStateEntry_Object = MibTableRow
mscFsDiskStateEntry = _MscFsDiskStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1)
)
mscFsDiskStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"),
)
if mibBuilder.loadTexts:
    mscFsDiskStateEntry.setStatus("mandatory")


class _MscFsDiskAdminState_Type(Integer32):
    """Custom type mscFsDiskAdminState based on Integer32"""
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


_MscFsDiskAdminState_Type.__name__ = "Integer32"
_MscFsDiskAdminState_Object = MibTableColumn
mscFsDiskAdminState = _MscFsDiskAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1, 1),
    _MscFsDiskAdminState_Type()
)
mscFsDiskAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskAdminState.setStatus("mandatory")


class _MscFsDiskOperationalState_Type(Integer32):
    """Custom type mscFsDiskOperationalState based on Integer32"""
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


_MscFsDiskOperationalState_Type.__name__ = "Integer32"
_MscFsDiskOperationalState_Object = MibTableColumn
mscFsDiskOperationalState = _MscFsDiskOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1, 2),
    _MscFsDiskOperationalState_Type()
)
mscFsDiskOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskOperationalState.setStatus("mandatory")


class _MscFsDiskUsageState_Type(Integer32):
    """Custom type mscFsDiskUsageState based on Integer32"""
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


_MscFsDiskUsageState_Type.__name__ = "Integer32"
_MscFsDiskUsageState_Object = MibTableColumn
mscFsDiskUsageState = _MscFsDiskUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 10, 1, 3),
    _MscFsDiskUsageState_Type()
)
mscFsDiskUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskUsageState.setStatus("mandatory")
_MscFsDiskOperTable_Object = MibTable
mscFsDiskOperTable = _MscFsDiskOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11)
)
if mibBuilder.loadTexts:
    mscFsDiskOperTable.setStatus("mandatory")
_MscFsDiskOperEntry_Object = MibTableRow
mscFsDiskOperEntry = _MscFsDiskOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1)
)
mscFsDiskOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsDiskIndex"),
)
if mibBuilder.loadTexts:
    mscFsDiskOperEntry.setStatus("mandatory")


class _MscFsDiskVolumeName_Type(AsciiString):
    """Custom type mscFsDiskVolumeName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_MscFsDiskVolumeName_Type.__name__ = "AsciiString"
_MscFsDiskVolumeName_Object = MibTableColumn
mscFsDiskVolumeName = _MscFsDiskVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 1),
    _MscFsDiskVolumeName_Type()
)
mscFsDiskVolumeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscFsDiskVolumeName.setStatus("mandatory")


class _MscFsDiskCapacity_Type(Unsigned32):
    """Custom type mscFsDiskCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsDiskCapacity_Type.__name__ = "Unsigned32"
_MscFsDiskCapacity_Object = MibTableColumn
mscFsDiskCapacity = _MscFsDiskCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 2),
    _MscFsDiskCapacity_Type()
)
mscFsDiskCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskCapacity.setStatus("mandatory")


class _MscFsDiskFreeSpace_Type(Unsigned32):
    """Custom type mscFsDiskFreeSpace based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsDiskFreeSpace_Type.__name__ = "Unsigned32"
_MscFsDiskFreeSpace_Object = MibTableColumn
mscFsDiskFreeSpace = _MscFsDiskFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 3),
    _MscFsDiskFreeSpace_Type()
)
mscFsDiskFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskFreeSpace.setStatus("mandatory")


class _MscFsDiskBadBlocksPercentage_Type(Gauge32):
    """Custom type mscFsDiskBadBlocksPercentage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFsDiskBadBlocksPercentage_Type.__name__ = "Gauge32"
_MscFsDiskBadBlocksPercentage_Object = MibTableColumn
mscFsDiskBadBlocksPercentage = _MscFsDiskBadBlocksPercentage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 4),
    _MscFsDiskBadBlocksPercentage_Type()
)
mscFsDiskBadBlocksPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskBadBlocksPercentage.setStatus("mandatory")


class _MscFsDiskUnformattedCapacity_Type(Unsigned32):
    """Custom type mscFsDiskUnformattedCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsDiskUnformattedCapacity_Type.__name__ = "Unsigned32"
_MscFsDiskUnformattedCapacity_Object = MibTableColumn
mscFsDiskUnformattedCapacity = _MscFsDiskUnformattedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 2, 11, 1, 5),
    _MscFsDiskUnformattedCapacity_Type()
)
mscFsDiskUnformattedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsDiskUnformattedCapacity.setStatus("mandatory")
_MscFsStateTable_Object = MibTable
mscFsStateTable = _MscFsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10)
)
if mibBuilder.loadTexts:
    mscFsStateTable.setStatus("mandatory")
_MscFsStateEntry_Object = MibTableRow
mscFsStateEntry = _MscFsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1)
)
mscFsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
)
if mibBuilder.loadTexts:
    mscFsStateEntry.setStatus("mandatory")


class _MscFsAdminState_Type(Integer32):
    """Custom type mscFsAdminState based on Integer32"""
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


_MscFsAdminState_Type.__name__ = "Integer32"
_MscFsAdminState_Object = MibTableColumn
mscFsAdminState = _MscFsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1, 1),
    _MscFsAdminState_Type()
)
mscFsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsAdminState.setStatus("mandatory")


class _MscFsOperationalState_Type(Integer32):
    """Custom type mscFsOperationalState based on Integer32"""
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


_MscFsOperationalState_Type.__name__ = "Integer32"
_MscFsOperationalState_Object = MibTableColumn
mscFsOperationalState = _MscFsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1, 2),
    _MscFsOperationalState_Type()
)
mscFsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsOperationalState.setStatus("mandatory")


class _MscFsUsageState_Type(Integer32):
    """Custom type mscFsUsageState based on Integer32"""
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


_MscFsUsageState_Type.__name__ = "Integer32"
_MscFsUsageState_Object = MibTableColumn
mscFsUsageState = _MscFsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 10, 1, 3),
    _MscFsUsageState_Type()
)
mscFsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsUsageState.setStatus("mandatory")
_MscFsOperTable_Object = MibTable
mscFsOperTable = _MscFsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11)
)
if mibBuilder.loadTexts:
    mscFsOperTable.setStatus("mandatory")
_MscFsOperEntry_Object = MibTableRow
mscFsOperEntry = _MscFsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1)
)
mscFsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-FileSystemMIB", "mscFsIndex"),
)
if mibBuilder.loadTexts:
    mscFsOperEntry.setStatus("mandatory")


class _MscFsVolumeName_Type(AsciiString):
    """Custom type mscFsVolumeName based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_MscFsVolumeName_Type.__name__ = "AsciiString"
_MscFsVolumeName_Object = MibTableColumn
mscFsVolumeName = _MscFsVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 1),
    _MscFsVolumeName_Type()
)
mscFsVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsVolumeName.setStatus("mandatory")
_MscFsActiveDisk_Type = RowPointer
_MscFsActiveDisk_Object = MibTableColumn
mscFsActiveDisk = _MscFsActiveDisk_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 2),
    _MscFsActiveDisk_Type()
)
mscFsActiveDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsActiveDisk.setStatus("mandatory")


class _MscFsSyncStatus_Type(Integer32):
    """Custom type mscFsSyncStatus based on Integer32"""
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


_MscFsSyncStatus_Type.__name__ = "Integer32"
_MscFsSyncStatus_Object = MibTableColumn
mscFsSyncStatus = _MscFsSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 3),
    _MscFsSyncStatus_Type()
)
mscFsSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsSyncStatus.setStatus("mandatory")


class _MscFsSyncProgress_Type(Gauge32):
    """Custom type mscFsSyncProgress based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFsSyncProgress_Type.__name__ = "Gauge32"
_MscFsSyncProgress_Object = MibTableColumn
mscFsSyncProgress = _MscFsSyncProgress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 4),
    _MscFsSyncProgress_Type()
)
mscFsSyncProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsSyncProgress.setStatus("mandatory")


class _MscFsCapacity_Type(Unsigned32):
    """Custom type mscFsCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsCapacity_Type.__name__ = "Unsigned32"
_MscFsCapacity_Object = MibTableColumn
mscFsCapacity = _MscFsCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 5),
    _MscFsCapacity_Type()
)
mscFsCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsCapacity.setStatus("mandatory")


class _MscFsFreeSpace_Type(Unsigned32):
    """Custom type mscFsFreeSpace based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscFsFreeSpace_Type.__name__ = "Unsigned32"
_MscFsFreeSpace_Object = MibTableColumn
mscFsFreeSpace = _MscFsFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 6),
    _MscFsFreeSpace_Type()
)
mscFsFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsFreeSpace.setStatus("mandatory")


class _MscFsUsage_Type(Gauge32):
    """Custom type mscFsUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscFsUsage_Type.__name__ = "Gauge32"
_MscFsUsage_Object = MibTableColumn
mscFsUsage = _MscFsUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 15, 11, 1, 7),
    _MscFsUsage_Type()
)
mscFsUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscFsUsage.setStatus("mandatory")
_FileSystemMIB_ObjectIdentity = ObjectIdentity
fileSystemMIB = _FileSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16)
)
_FileSystemGroup_ObjectIdentity = ObjectIdentity
fileSystemGroup = _FileSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1)
)
_FileSystemGroupCA_ObjectIdentity = ObjectIdentity
fileSystemGroupCA = _FileSystemGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1, 1)
)
_FileSystemGroupCA02_ObjectIdentity = ObjectIdentity
fileSystemGroupCA02 = _FileSystemGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1, 1, 3)
)
_FileSystemGroupCA02A_ObjectIdentity = ObjectIdentity
fileSystemGroupCA02A = _FileSystemGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 1, 1, 3, 2)
)
_FileSystemCapabilities_ObjectIdentity = ObjectIdentity
fileSystemCapabilities = _FileSystemCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3)
)
_FileSystemCapabilitiesCA_ObjectIdentity = ObjectIdentity
fileSystemCapabilitiesCA = _FileSystemCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3, 1)
)
_FileSystemCapabilitiesCA02_ObjectIdentity = ObjectIdentity
fileSystemCapabilitiesCA02 = _FileSystemCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3, 1, 3)
)
_FileSystemCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
fileSystemCapabilitiesCA02A = _FileSystemCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 16, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-FileSystemMIB",
    **{"mscFs": mscFs,
       "mscFsRowStatusTable": mscFsRowStatusTable,
       "mscFsRowStatusEntry": mscFsRowStatusEntry,
       "mscFsRowStatus": mscFsRowStatus,
       "mscFsComponentName": mscFsComponentName,
       "mscFsStorageType": mscFsStorageType,
       "mscFsIndex": mscFsIndex,
       "mscFsDisk": mscFsDisk,
       "mscFsDiskRowStatusTable": mscFsDiskRowStatusTable,
       "mscFsDiskRowStatusEntry": mscFsDiskRowStatusEntry,
       "mscFsDiskRowStatus": mscFsDiskRowStatus,
       "mscFsDiskComponentName": mscFsDiskComponentName,
       "mscFsDiskStorageType": mscFsDiskStorageType,
       "mscFsDiskIndex": mscFsDiskIndex,
       "mscFsDiskTest": mscFsDiskTest,
       "mscFsDiskTestRowStatusTable": mscFsDiskTestRowStatusTable,
       "mscFsDiskTestRowStatusEntry": mscFsDiskTestRowStatusEntry,
       "mscFsDiskTestRowStatus": mscFsDiskTestRowStatus,
       "mscFsDiskTestComponentName": mscFsDiskTestComponentName,
       "mscFsDiskTestStorageType": mscFsDiskTestStorageType,
       "mscFsDiskTestIndex": mscFsDiskTestIndex,
       "mscFsDiskTestStateTable": mscFsDiskTestStateTable,
       "mscFsDiskTestStateEntry": mscFsDiskTestStateEntry,
       "mscFsDiskTestAdminState": mscFsDiskTestAdminState,
       "mscFsDiskTestOperationalState": mscFsDiskTestOperationalState,
       "mscFsDiskTestUsageState": mscFsDiskTestUsageState,
       "mscFsDiskTestSetupTable": mscFsDiskTestSetupTable,
       "mscFsDiskTestSetupEntry": mscFsDiskTestSetupEntry,
       "mscFsDiskTestTestCount": mscFsDiskTestTestCount,
       "mscFsDiskTestDuration": mscFsDiskTestDuration,
       "mscFsDiskTestType": mscFsDiskTestType,
       "mscFsDiskTestResultsTable": mscFsDiskTestResultsTable,
       "mscFsDiskTestResultsEntry": mscFsDiskTestResultsEntry,
       "mscFsDiskTestCauseOfTermination": mscFsDiskTestCauseOfTermination,
       "mscFsDiskTestNatureOfError": mscFsDiskTestNatureOfError,
       "mscFsDiskTestSeverity": mscFsDiskTestSeverity,
       "mscFsDiskTestElapsedTime": mscFsDiskTestElapsedTime,
       "mscFsDiskTestTestExecutionCount": mscFsDiskTestTestExecutionCount,
       "mscFsDiskStateTable": mscFsDiskStateTable,
       "mscFsDiskStateEntry": mscFsDiskStateEntry,
       "mscFsDiskAdminState": mscFsDiskAdminState,
       "mscFsDiskOperationalState": mscFsDiskOperationalState,
       "mscFsDiskUsageState": mscFsDiskUsageState,
       "mscFsDiskOperTable": mscFsDiskOperTable,
       "mscFsDiskOperEntry": mscFsDiskOperEntry,
       "mscFsDiskVolumeName": mscFsDiskVolumeName,
       "mscFsDiskCapacity": mscFsDiskCapacity,
       "mscFsDiskFreeSpace": mscFsDiskFreeSpace,
       "mscFsDiskBadBlocksPercentage": mscFsDiskBadBlocksPercentage,
       "mscFsDiskUnformattedCapacity": mscFsDiskUnformattedCapacity,
       "mscFsStateTable": mscFsStateTable,
       "mscFsStateEntry": mscFsStateEntry,
       "mscFsAdminState": mscFsAdminState,
       "mscFsOperationalState": mscFsOperationalState,
       "mscFsUsageState": mscFsUsageState,
       "mscFsOperTable": mscFsOperTable,
       "mscFsOperEntry": mscFsOperEntry,
       "mscFsVolumeName": mscFsVolumeName,
       "mscFsActiveDisk": mscFsActiveDisk,
       "mscFsSyncStatus": mscFsSyncStatus,
       "mscFsSyncProgress": mscFsSyncProgress,
       "mscFsCapacity": mscFsCapacity,
       "mscFsFreeSpace": mscFsFreeSpace,
       "mscFsUsage": mscFsUsage,
       "fileSystemMIB": fileSystemMIB,
       "fileSystemGroup": fileSystemGroup,
       "fileSystemGroupCA": fileSystemGroupCA,
       "fileSystemGroupCA02": fileSystemGroupCA02,
       "fileSystemGroupCA02A": fileSystemGroupCA02A,
       "fileSystemCapabilities": fileSystemCapabilities,
       "fileSystemCapabilitiesCA": fileSystemCapabilitiesCA,
       "fileSystemCapabilitiesCA02": fileSystemCapabilitiesCA02,
       "fileSystemCapabilitiesCA02A": fileSystemCapabilitiesCA02A}
)
