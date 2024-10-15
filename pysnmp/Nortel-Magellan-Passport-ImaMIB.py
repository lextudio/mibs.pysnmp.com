# SNMP MIB module (Nortel-Magellan-Passport-ImaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ImaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:56 2024
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

(lp,
 lpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-LogicalProcessorMIB",
    "lp",
    "lpIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "Hex",
    "Link",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
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

_LpIma_ObjectIdentity = ObjectIdentity
lpIma = _LpIma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22)
)
_LpImaRowStatusTable_Object = MibTable
lpImaRowStatusTable = _LpImaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 1)
)
if mibBuilder.loadTexts:
    lpImaRowStatusTable.setStatus("mandatory")
_LpImaRowStatusEntry_Object = MibTableRow
lpImaRowStatusEntry = _LpImaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 1, 1)
)
lpImaRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
)
if mibBuilder.loadTexts:
    lpImaRowStatusEntry.setStatus("mandatory")
_LpImaRowStatus_Type = RowStatus
_LpImaRowStatus_Object = MibTableColumn
lpImaRowStatus = _LpImaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 1, 1, 1),
    _LpImaRowStatus_Type()
)
lpImaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaRowStatus.setStatus("mandatory")
_LpImaComponentName_Type = DisplayString
_LpImaComponentName_Object = MibTableColumn
lpImaComponentName = _LpImaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 1, 1, 2),
    _LpImaComponentName_Type()
)
lpImaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaComponentName.setStatus("mandatory")
_LpImaStorageType_Type = StorageType
_LpImaStorageType_Object = MibTableColumn
lpImaStorageType = _LpImaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 1, 1, 4),
    _LpImaStorageType_Type()
)
lpImaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaStorageType.setStatus("mandatory")


class _LpImaIndex_Type(Integer32):
    """Custom type lpImaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LpImaIndex_Type.__name__ = "Integer32"
_LpImaIndex_Object = MibTableColumn
lpImaIndex = _LpImaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 1, 1, 10),
    _LpImaIndex_Type()
)
lpImaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpImaIndex.setStatus("mandatory")
_LpImaTest_ObjectIdentity = ObjectIdentity
lpImaTest = _LpImaTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2)
)
_LpImaTestRowStatusTable_Object = MibTable
lpImaTestRowStatusTable = _LpImaTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 1)
)
if mibBuilder.loadTexts:
    lpImaTestRowStatusTable.setStatus("mandatory")
_LpImaTestRowStatusEntry_Object = MibTableRow
lpImaTestRowStatusEntry = _LpImaTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 1, 1)
)
lpImaTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaTestIndex"),
)
if mibBuilder.loadTexts:
    lpImaTestRowStatusEntry.setStatus("mandatory")
_LpImaTestRowStatus_Type = RowStatus
_LpImaTestRowStatus_Object = MibTableColumn
lpImaTestRowStatus = _LpImaTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 1, 1, 1),
    _LpImaTestRowStatus_Type()
)
lpImaTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestRowStatus.setStatus("mandatory")
_LpImaTestComponentName_Type = DisplayString
_LpImaTestComponentName_Object = MibTableColumn
lpImaTestComponentName = _LpImaTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 1, 1, 2),
    _LpImaTestComponentName_Type()
)
lpImaTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestComponentName.setStatus("mandatory")
_LpImaTestStorageType_Type = StorageType
_LpImaTestStorageType_Object = MibTableColumn
lpImaTestStorageType = _LpImaTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 1, 1, 4),
    _LpImaTestStorageType_Type()
)
lpImaTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestStorageType.setStatus("mandatory")
_LpImaTestIndex_Type = NonReplicated
_LpImaTestIndex_Object = MibTableColumn
lpImaTestIndex = _LpImaTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 1, 1, 10),
    _LpImaTestIndex_Type()
)
lpImaTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpImaTestIndex.setStatus("mandatory")
_LpImaTestStateTable_Object = MibTable
lpImaTestStateTable = _LpImaTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 10)
)
if mibBuilder.loadTexts:
    lpImaTestStateTable.setStatus("mandatory")
_LpImaTestStateEntry_Object = MibTableRow
lpImaTestStateEntry = _LpImaTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 10, 1)
)
lpImaTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaTestIndex"),
)
if mibBuilder.loadTexts:
    lpImaTestStateEntry.setStatus("mandatory")


class _LpImaTestAdminState_Type(Integer32):
    """Custom type lpImaTestAdminState based on Integer32"""
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


_LpImaTestAdminState_Type.__name__ = "Integer32"
_LpImaTestAdminState_Object = MibTableColumn
lpImaTestAdminState = _LpImaTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 10, 1, 1),
    _LpImaTestAdminState_Type()
)
lpImaTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestAdminState.setStatus("mandatory")


class _LpImaTestOperationalState_Type(Integer32):
    """Custom type lpImaTestOperationalState based on Integer32"""
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


_LpImaTestOperationalState_Type.__name__ = "Integer32"
_LpImaTestOperationalState_Object = MibTableColumn
lpImaTestOperationalState = _LpImaTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 10, 1, 2),
    _LpImaTestOperationalState_Type()
)
lpImaTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestOperationalState.setStatus("mandatory")


class _LpImaTestUsageState_Type(Integer32):
    """Custom type lpImaTestUsageState based on Integer32"""
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


_LpImaTestUsageState_Type.__name__ = "Integer32"
_LpImaTestUsageState_Object = MibTableColumn
lpImaTestUsageState = _LpImaTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 10, 1, 3),
    _LpImaTestUsageState_Type()
)
lpImaTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestUsageState.setStatus("mandatory")
_LpImaTestSetupTable_Object = MibTable
lpImaTestSetupTable = _LpImaTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11)
)
if mibBuilder.loadTexts:
    lpImaTestSetupTable.setStatus("mandatory")
_LpImaTestSetupEntry_Object = MibTableRow
lpImaTestSetupEntry = _LpImaTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1)
)
lpImaTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaTestIndex"),
)
if mibBuilder.loadTexts:
    lpImaTestSetupEntry.setStatus("mandatory")


class _LpImaTestPurpose_Type(AsciiString):
    """Custom type lpImaTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpImaTestPurpose_Type.__name__ = "AsciiString"
_LpImaTestPurpose_Object = MibTableColumn
lpImaTestPurpose = _LpImaTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 1),
    _LpImaTestPurpose_Type()
)
lpImaTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestPurpose.setStatus("mandatory")


class _LpImaTestType_Type(Integer32):
    """Custom type lpImaTestType based on Integer32"""
    defaultValue = 0

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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("card", 0),
          ("externalLoop", 4),
          ("localLoop", 2),
          ("manual", 1),
          ("payloadLoop", 5),
          ("pn127RemoteLoop", 8),
          ("remoteLoop", 3),
          ("remoteLoopThisTrib", 6),
          ("v54RemoteLoop", 7))
    )


_LpImaTestType_Type.__name__ = "Integer32"
_LpImaTestType_Object = MibTableColumn
lpImaTestType = _LpImaTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 2),
    _LpImaTestType_Type()
)
lpImaTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestType.setStatus("mandatory")


class _LpImaTestFrmSize_Type(Unsigned32):
    """Custom type lpImaTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpImaTestFrmSize_Type.__name__ = "Unsigned32"
_LpImaTestFrmSize_Object = MibTableColumn
lpImaTestFrmSize = _LpImaTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 3),
    _LpImaTestFrmSize_Type()
)
lpImaTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestFrmSize.setStatus("mandatory")


class _LpImaTestFrmPatternType_Type(Integer32):
    """Custom type lpImaTestFrmPatternType based on Integer32"""
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
        *(("ccitt32kBitPattern", 0),
          ("ccitt8MBitPattern", 1),
          ("customizedPattern", 2))
    )


_LpImaTestFrmPatternType_Type.__name__ = "Integer32"
_LpImaTestFrmPatternType_Object = MibTableColumn
lpImaTestFrmPatternType = _LpImaTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 4),
    _LpImaTestFrmPatternType_Type()
)
lpImaTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestFrmPatternType.setStatus("mandatory")


class _LpImaTestCustomizedPattern_Type(Hex):
    """Custom type lpImaTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaTestCustomizedPattern_Type.__name__ = "Hex"
_LpImaTestCustomizedPattern_Object = MibTableColumn
lpImaTestCustomizedPattern = _LpImaTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 5),
    _LpImaTestCustomizedPattern_Type()
)
lpImaTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestCustomizedPattern.setStatus("mandatory")


class _LpImaTestDataStartDelay_Type(Unsigned32):
    """Custom type lpImaTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpImaTestDataStartDelay_Type.__name__ = "Unsigned32"
_LpImaTestDataStartDelay_Object = MibTableColumn
lpImaTestDataStartDelay = _LpImaTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 6),
    _LpImaTestDataStartDelay_Type()
)
lpImaTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestDataStartDelay.setStatus("mandatory")


class _LpImaTestDisplayInterval_Type(Unsigned32):
    """Custom type lpImaTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpImaTestDisplayInterval_Type.__name__ = "Unsigned32"
_LpImaTestDisplayInterval_Object = MibTableColumn
lpImaTestDisplayInterval = _LpImaTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 7),
    _LpImaTestDisplayInterval_Type()
)
lpImaTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestDisplayInterval.setStatus("mandatory")


class _LpImaTestDuration_Type(Unsigned32):
    """Custom type lpImaTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpImaTestDuration_Type.__name__ = "Unsigned32"
_LpImaTestDuration_Object = MibTableColumn
lpImaTestDuration = _LpImaTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 11, 1, 8),
    _LpImaTestDuration_Type()
)
lpImaTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTestDuration.setStatus("mandatory")
_LpImaTestResultsTable_Object = MibTable
lpImaTestResultsTable = _LpImaTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12)
)
if mibBuilder.loadTexts:
    lpImaTestResultsTable.setStatus("mandatory")
_LpImaTestResultsEntry_Object = MibTableRow
lpImaTestResultsEntry = _LpImaTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1)
)
lpImaTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaTestIndex"),
)
if mibBuilder.loadTexts:
    lpImaTestResultsEntry.setStatus("mandatory")
_LpImaTestElapsedTime_Type = Counter32
_LpImaTestElapsedTime_Object = MibTableColumn
lpImaTestElapsedTime = _LpImaTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 1),
    _LpImaTestElapsedTime_Type()
)
lpImaTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestElapsedTime.setStatus("mandatory")


class _LpImaTestTimeRemaining_Type(Unsigned32):
    """Custom type lpImaTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpImaTestTimeRemaining_Object = MibTableColumn
lpImaTestTimeRemaining = _LpImaTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 2),
    _LpImaTestTimeRemaining_Type()
)
lpImaTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestTimeRemaining.setStatus("mandatory")


class _LpImaTestCauseOfTermination_Type(Integer32):
    """Custom type lpImaTestCauseOfTermination based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("hardwareReconfigured", 5),
          ("neverStarted", 3),
          ("stoppedByOperator", 1),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_LpImaTestCauseOfTermination_Type.__name__ = "Integer32"
_LpImaTestCauseOfTermination_Object = MibTableColumn
lpImaTestCauseOfTermination = _LpImaTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 3),
    _LpImaTestCauseOfTermination_Type()
)
lpImaTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestCauseOfTermination.setStatus("mandatory")
_LpImaTestBitsTx_Type = PassportCounter64
_LpImaTestBitsTx_Object = MibTableColumn
lpImaTestBitsTx = _LpImaTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 4),
    _LpImaTestBitsTx_Type()
)
lpImaTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestBitsTx.setStatus("mandatory")
_LpImaTestBytesTx_Type = PassportCounter64
_LpImaTestBytesTx_Object = MibTableColumn
lpImaTestBytesTx = _LpImaTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 5),
    _LpImaTestBytesTx_Type()
)
lpImaTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestBytesTx.setStatus("mandatory")
_LpImaTestFrmTx_Type = PassportCounter64
_LpImaTestFrmTx_Object = MibTableColumn
lpImaTestFrmTx = _LpImaTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 6),
    _LpImaTestFrmTx_Type()
)
lpImaTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestFrmTx.setStatus("mandatory")
_LpImaTestBitsRx_Type = PassportCounter64
_LpImaTestBitsRx_Object = MibTableColumn
lpImaTestBitsRx = _LpImaTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 7),
    _LpImaTestBitsRx_Type()
)
lpImaTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestBitsRx.setStatus("mandatory")
_LpImaTestBytesRx_Type = PassportCounter64
_LpImaTestBytesRx_Object = MibTableColumn
lpImaTestBytesRx = _LpImaTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 8),
    _LpImaTestBytesRx_Type()
)
lpImaTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestBytesRx.setStatus("mandatory")
_LpImaTestFrmRx_Type = PassportCounter64
_LpImaTestFrmRx_Object = MibTableColumn
lpImaTestFrmRx = _LpImaTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 9),
    _LpImaTestFrmRx_Type()
)
lpImaTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestFrmRx.setStatus("mandatory")
_LpImaTestErroredFrmRx_Type = PassportCounter64
_LpImaTestErroredFrmRx_Object = MibTableColumn
lpImaTestErroredFrmRx = _LpImaTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 10),
    _LpImaTestErroredFrmRx_Type()
)
lpImaTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestErroredFrmRx.setStatus("mandatory")


class _LpImaTestBitErrorRate_Type(AsciiString):
    """Custom type lpImaTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpImaTestBitErrorRate_Type.__name__ = "AsciiString"
_LpImaTestBitErrorRate_Object = MibTableColumn
lpImaTestBitErrorRate = _LpImaTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 2, 12, 1, 11),
    _LpImaTestBitErrorRate_Type()
)
lpImaTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTestBitErrorRate.setStatus("mandatory")
_LpImaLk_ObjectIdentity = ObjectIdentity
lpImaLk = _LpImaLk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3)
)
_LpImaLkRowStatusTable_Object = MibTable
lpImaLkRowStatusTable = _LpImaLkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 1)
)
if mibBuilder.loadTexts:
    lpImaLkRowStatusTable.setStatus("mandatory")
_LpImaLkRowStatusEntry_Object = MibTableRow
lpImaLkRowStatusEntry = _LpImaLkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 1, 1)
)
lpImaLkRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaLkIndex"),
)
if mibBuilder.loadTexts:
    lpImaLkRowStatusEntry.setStatus("mandatory")
_LpImaLkRowStatus_Type = RowStatus
_LpImaLkRowStatus_Object = MibTableColumn
lpImaLkRowStatus = _LpImaLkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 1, 1, 1),
    _LpImaLkRowStatus_Type()
)
lpImaLkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaLkRowStatus.setStatus("mandatory")
_LpImaLkComponentName_Type = DisplayString
_LpImaLkComponentName_Object = MibTableColumn
lpImaLkComponentName = _LpImaLkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 1, 1, 2),
    _LpImaLkComponentName_Type()
)
lpImaLkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkComponentName.setStatus("mandatory")
_LpImaLkStorageType_Type = StorageType
_LpImaLkStorageType_Object = MibTableColumn
lpImaLkStorageType = _LpImaLkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 1, 1, 4),
    _LpImaLkStorageType_Type()
)
lpImaLkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkStorageType.setStatus("mandatory")


class _LpImaLkIndex_Type(Integer32):
    """Custom type lpImaLkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LpImaLkIndex_Type.__name__ = "Integer32"
_LpImaLkIndex_Object = MibTableColumn
lpImaLkIndex = _LpImaLkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 1, 1, 10),
    _LpImaLkIndex_Type()
)
lpImaLkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpImaLkIndex.setStatus("mandatory")
_LpImaLkProvTable_Object = MibTable
lpImaLkProvTable = _LpImaLkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 10)
)
if mibBuilder.loadTexts:
    lpImaLkProvTable.setStatus("mandatory")
_LpImaLkProvEntry_Object = MibTableRow
lpImaLkProvEntry = _LpImaLkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 10, 1)
)
lpImaLkProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaLkIndex"),
)
if mibBuilder.loadTexts:
    lpImaLkProvEntry.setStatus("mandatory")
_LpImaLkInterfaceName_Type = Link
_LpImaLkInterfaceName_Object = MibTableColumn
lpImaLkInterfaceName = _LpImaLkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 10, 1, 1),
    _LpImaLkInterfaceName_Type()
)
lpImaLkInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaLkInterfaceName.setStatus("mandatory")
_LpImaLkOperTable_Object = MibTable
lpImaLkOperTable = _LpImaLkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 11)
)
if mibBuilder.loadTexts:
    lpImaLkOperTable.setStatus("mandatory")
_LpImaLkOperEntry_Object = MibTableRow
lpImaLkOperEntry = _LpImaLkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 11, 1)
)
lpImaLkOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaLkIndex"),
)
if mibBuilder.loadTexts:
    lpImaLkOperEntry.setStatus("mandatory")


class _LpImaLkFailureCause_Type(Integer32):
    """Custom type lpImaLkFailureCause based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDown", 1),
          ("lif", 2),
          ("lods", 3),
          ("misconnected", 6),
          ("noFailure", 0),
          ("noIcp", 9),
          ("protocolError", 4),
          ("remoteFailure", 5),
          ("unsupportedFrameLength", 7),
          ("unsupportedSymmetry", 8))
    )


_LpImaLkFailureCause_Type.__name__ = "Integer32"
_LpImaLkFailureCause_Object = MibTableColumn
lpImaLkFailureCause = _LpImaLkFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 11, 1, 1),
    _LpImaLkFailureCause_Type()
)
lpImaLkFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkFailureCause.setStatus("mandatory")


class _LpImaLkRemoteDefect_Type(Integer32):
    """Custom type lpImaLkRemoteDefect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDown", 4),
          ("lif", 2),
          ("lods", 3),
          ("noDefect", 0),
          ("physicalLayerDefect", 1))
    )


_LpImaLkRemoteDefect_Type.__name__ = "Integer32"
_LpImaLkRemoteDefect_Object = MibTableColumn
lpImaLkRemoteDefect = _LpImaLkRemoteDefect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 11, 1, 2),
    _LpImaLkRemoteDefect_Type()
)
lpImaLkRemoteDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkRemoteDefect.setStatus("mandatory")


class _LpImaLkRemoteLid_Type(Unsigned32):
    """Custom type lpImaLkRemoteLid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LpImaLkRemoteLid_Type.__name__ = "Unsigned32"
_LpImaLkRemoteLid_Object = MibTableColumn
lpImaLkRemoteLid = _LpImaLkRemoteLid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 11, 1, 3),
    _LpImaLkRemoteLid_Type()
)
lpImaLkRemoteLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkRemoteLid.setStatus("mandatory")


class _LpImaLkRelativeDelay_Type(Unsigned32):
    """Custom type lpImaLkRelativeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaLkRelativeDelay_Type.__name__ = "Unsigned32"
_LpImaLkRelativeDelay_Object = MibTableColumn
lpImaLkRelativeDelay = _LpImaLkRelativeDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 11, 1, 4),
    _LpImaLkRelativeDelay_Type()
)
lpImaLkRelativeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkRelativeDelay.setStatus("mandatory")


class _LpImaLkLastOifCause_Type(Integer32):
    """Custom type lpImaLkLastOifCause based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("badFrameLength", 1),
          ("badGid", 2),
          ("badLid", 3),
          ("badOffset", 4),
          ("badSequenceNumber", 5),
          ("erroredIcp", 9),
          ("idleCell", 11),
          ("missingIcp", 7),
          ("noCells", 10),
          ("noOif", 0),
          ("stuffError", 6),
          ("unexpectedIcp", 8))
    )


_LpImaLkLastOifCause_Type.__name__ = "Integer32"
_LpImaLkLastOifCause_Object = MibTableColumn
lpImaLkLastOifCause = _LpImaLkLastOifCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 11, 1, 5),
    _LpImaLkLastOifCause_Type()
)
lpImaLkLastOifCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkLastOifCause.setStatus("mandatory")
_LpImaLkStatsTable_Object = MibTable
lpImaLkStatsTable = _LpImaLkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12)
)
if mibBuilder.loadTexts:
    lpImaLkStatsTable.setStatus("mandatory")
_LpImaLkStatsEntry_Object = MibTableRow
lpImaLkStatsEntry = _LpImaLkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1)
)
lpImaLkStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaLkIndex"),
)
if mibBuilder.loadTexts:
    lpImaLkStatsEntry.setStatus("mandatory")


class _LpImaLkRunningTime_Type(Unsigned32):
    """Custom type lpImaLkRunningTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaLkRunningTime_Type.__name__ = "Unsigned32"
_LpImaLkRunningTime_Object = MibTableColumn
lpImaLkRunningTime = _LpImaLkRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 1),
    _LpImaLkRunningTime_Type()
)
lpImaLkRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkRunningTime.setStatus("mandatory")


class _LpImaLkUnavailSecs_Type(Unsigned32):
    """Custom type lpImaLkUnavailSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaLkUnavailSecs_Type.__name__ = "Unsigned32"
_LpImaLkUnavailSecs_Object = MibTableColumn
lpImaLkUnavailSecs = _LpImaLkUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 2),
    _LpImaLkUnavailSecs_Type()
)
lpImaLkUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkUnavailSecs.setStatus("mandatory")


class _LpImaLkFailures_Type(Unsigned32):
    """Custom type lpImaLkFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaLkFailures_Type.__name__ = "Unsigned32"
_LpImaLkFailures_Object = MibTableColumn
lpImaLkFailures = _LpImaLkFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 3),
    _LpImaLkFailures_Type()
)
lpImaLkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkFailures.setStatus("mandatory")
_LpImaLkUnusableSec_Type = Counter32
_LpImaLkUnusableSec_Object = MibTableColumn
lpImaLkUnusableSec = _LpImaLkUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 4),
    _LpImaLkUnusableSec_Type()
)
lpImaLkUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkUnusableSec.setStatus("mandatory")
_LpImaLkSevErroredSec_Type = Counter32
_LpImaLkSevErroredSec_Object = MibTableColumn
lpImaLkSevErroredSec = _LpImaLkSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 5),
    _LpImaLkSevErroredSec_Type()
)
lpImaLkSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkSevErroredSec.setStatus("mandatory")
_LpImaLkFarEndUnusableSec_Type = Counter32
_LpImaLkFarEndUnusableSec_Object = MibTableColumn
lpImaLkFarEndUnusableSec = _LpImaLkFarEndUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 6),
    _LpImaLkFarEndUnusableSec_Type()
)
lpImaLkFarEndUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkFarEndUnusableSec.setStatus("mandatory")
_LpImaLkFarEndSevErroredSec_Type = Counter32
_LpImaLkFarEndSevErroredSec_Object = MibTableColumn
lpImaLkFarEndSevErroredSec = _LpImaLkFarEndSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 7),
    _LpImaLkFarEndSevErroredSec_Type()
)
lpImaLkFarEndSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkFarEndSevErroredSec.setStatus("mandatory")
_LpImaLkFarEndUnavailSec_Type = Counter32
_LpImaLkFarEndUnavailSec_Object = MibTableColumn
lpImaLkFarEndUnavailSec = _LpImaLkFarEndUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 8),
    _LpImaLkFarEndUnavailSec_Type()
)
lpImaLkFarEndUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkFarEndUnavailSec.setStatus("mandatory")
_LpImaLkIcpViolations_Type = Counter32
_LpImaLkIcpViolations_Object = MibTableColumn
lpImaLkIcpViolations = _LpImaLkIcpViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 9),
    _LpImaLkIcpViolations_Type()
)
lpImaLkIcpViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkIcpViolations.setStatus("mandatory")
_LpImaLkTxStuffEvents_Type = Counter32
_LpImaLkTxStuffEvents_Object = MibTableColumn
lpImaLkTxStuffEvents = _LpImaLkTxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 10),
    _LpImaLkTxStuffEvents_Type()
)
lpImaLkTxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkTxStuffEvents.setStatus("mandatory")
_LpImaLkRxStuffEvents_Type = Counter32
_LpImaLkRxStuffEvents_Object = MibTableColumn
lpImaLkRxStuffEvents = _LpImaLkRxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 11),
    _LpImaLkRxStuffEvents_Type()
)
lpImaLkRxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkRxStuffEvents.setStatus("mandatory")
_LpImaLkIdleCellSec_Type = Counter32
_LpImaLkIdleCellSec_Object = MibTableColumn
lpImaLkIdleCellSec = _LpImaLkIdleCellSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 12, 1, 12),
    _LpImaLkIdleCellSec_Type()
)
lpImaLkIdleCellSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkIdleCellSec.setStatus("mandatory")
_LpImaLkStateTable_Object = MibTable
lpImaLkStateTable = _LpImaLkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13)
)
if mibBuilder.loadTexts:
    lpImaLkStateTable.setStatus("mandatory")
_LpImaLkStateEntry_Object = MibTableRow
lpImaLkStateEntry = _LpImaLkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1)
)
lpImaLkStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaLkIndex"),
)
if mibBuilder.loadTexts:
    lpImaLkStateEntry.setStatus("mandatory")


class _LpImaLkAdminState_Type(Integer32):
    """Custom type lpImaLkAdminState based on Integer32"""
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


_LpImaLkAdminState_Type.__name__ = "Integer32"
_LpImaLkAdminState_Object = MibTableColumn
lpImaLkAdminState = _LpImaLkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 1),
    _LpImaLkAdminState_Type()
)
lpImaLkAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkAdminState.setStatus("mandatory")


class _LpImaLkOperationalState_Type(Integer32):
    """Custom type lpImaLkOperationalState based on Integer32"""
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


_LpImaLkOperationalState_Type.__name__ = "Integer32"
_LpImaLkOperationalState_Object = MibTableColumn
lpImaLkOperationalState = _LpImaLkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 2),
    _LpImaLkOperationalState_Type()
)
lpImaLkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkOperationalState.setStatus("mandatory")


class _LpImaLkUsageState_Type(Integer32):
    """Custom type lpImaLkUsageState based on Integer32"""
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


_LpImaLkUsageState_Type.__name__ = "Integer32"
_LpImaLkUsageState_Object = MibTableColumn
lpImaLkUsageState = _LpImaLkUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 3),
    _LpImaLkUsageState_Type()
)
lpImaLkUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkUsageState.setStatus("mandatory")


class _LpImaLkAvailabilityStatus_Type(OctetString):
    """Custom type lpImaLkAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpImaLkAvailabilityStatus_Type.__name__ = "OctetString"
_LpImaLkAvailabilityStatus_Object = MibTableColumn
lpImaLkAvailabilityStatus = _LpImaLkAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 4),
    _LpImaLkAvailabilityStatus_Type()
)
lpImaLkAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkAvailabilityStatus.setStatus("mandatory")


class _LpImaLkProceduralStatus_Type(OctetString):
    """Custom type lpImaLkProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpImaLkProceduralStatus_Type.__name__ = "OctetString"
_LpImaLkProceduralStatus_Object = MibTableColumn
lpImaLkProceduralStatus = _LpImaLkProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 5),
    _LpImaLkProceduralStatus_Type()
)
lpImaLkProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkProceduralStatus.setStatus("mandatory")


class _LpImaLkControlStatus_Type(OctetString):
    """Custom type lpImaLkControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpImaLkControlStatus_Type.__name__ = "OctetString"
_LpImaLkControlStatus_Object = MibTableColumn
lpImaLkControlStatus = _LpImaLkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 6),
    _LpImaLkControlStatus_Type()
)
lpImaLkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkControlStatus.setStatus("mandatory")


class _LpImaLkAlarmStatus_Type(OctetString):
    """Custom type lpImaLkAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpImaLkAlarmStatus_Type.__name__ = "OctetString"
_LpImaLkAlarmStatus_Object = MibTableColumn
lpImaLkAlarmStatus = _LpImaLkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 7),
    _LpImaLkAlarmStatus_Type()
)
lpImaLkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkAlarmStatus.setStatus("mandatory")


class _LpImaLkStandbyStatus_Type(Integer32):
    """Custom type lpImaLkStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_LpImaLkStandbyStatus_Type.__name__ = "Integer32"
_LpImaLkStandbyStatus_Object = MibTableColumn
lpImaLkStandbyStatus = _LpImaLkStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 8),
    _LpImaLkStandbyStatus_Type()
)
lpImaLkStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkStandbyStatus.setStatus("mandatory")


class _LpImaLkUnknownStatus_Type(Integer32):
    """Custom type lpImaLkUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_LpImaLkUnknownStatus_Type.__name__ = "Integer32"
_LpImaLkUnknownStatus_Object = MibTableColumn
lpImaLkUnknownStatus = _LpImaLkUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 3, 13, 1, 9),
    _LpImaLkUnknownStatus_Type()
)
lpImaLkUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaLkUnknownStatus.setStatus("mandatory")
_LpImaProvTable_Object = MibTable
lpImaProvTable = _LpImaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10)
)
if mibBuilder.loadTexts:
    lpImaProvTable.setStatus("mandatory")
_LpImaProvEntry_Object = MibTableRow
lpImaProvEntry = _LpImaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10, 1)
)
lpImaProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
)
if mibBuilder.loadTexts:
    lpImaProvEntry.setStatus("mandatory")


class _LpImaLinkSelectionCriterion_Type(Integer32):
    """Custom type lpImaLinkSelectionCriterion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("leastDelay", 0),
          ("maxBandwidth", 1))
    )


_LpImaLinkSelectionCriterion_Type.__name__ = "Integer32"
_LpImaLinkSelectionCriterion_Object = MibTableColumn
lpImaLinkSelectionCriterion = _LpImaLinkSelectionCriterion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10, 1, 1),
    _LpImaLinkSelectionCriterion_Type()
)
lpImaLinkSelectionCriterion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaLinkSelectionCriterion.setStatus("mandatory")


class _LpImaMaxDiffDelay_Type(Unsigned32):
    """Custom type lpImaMaxDiffDelay based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_LpImaMaxDiffDelay_Type.__name__ = "Unsigned32"
_LpImaMaxDiffDelay_Object = MibTableColumn
lpImaMaxDiffDelay = _LpImaMaxDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10, 1, 2),
    _LpImaMaxDiffDelay_Type()
)
lpImaMaxDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaMaxDiffDelay.setStatus("mandatory")


class _LpImaLinkRetryTimeout_Type(Unsigned32):
    """Custom type lpImaLinkRetryTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_LpImaLinkRetryTimeout_Type.__name__ = "Unsigned32"
_LpImaLinkRetryTimeout_Object = MibTableColumn
lpImaLinkRetryTimeout = _LpImaLinkRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10, 1, 3),
    _LpImaLinkRetryTimeout_Type()
)
lpImaLinkRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaLinkRetryTimeout.setStatus("mandatory")
_LpImaApplicationFramerName_Type = Link
_LpImaApplicationFramerName_Object = MibTableColumn
lpImaApplicationFramerName = _LpImaApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10, 1, 4),
    _LpImaApplicationFramerName_Type()
)
lpImaApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaApplicationFramerName.setStatus("mandatory")


class _LpImaTransmitClockMode_Type(Integer32):
    """Custom type lpImaTransmitClockMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 0))
    )


_LpImaTransmitClockMode_Type.__name__ = "Integer32"
_LpImaTransmitClockMode_Object = MibTableColumn
lpImaTransmitClockMode = _LpImaTransmitClockMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10, 1, 5),
    _LpImaTransmitClockMode_Type()
)
lpImaTransmitClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaTransmitClockMode.setStatus("mandatory")


class _LpImaProtocol_Type(Integer32):
    """Custom type lpImaProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("atmForum10", 0),
          ("proprietary", 1))
    )


_LpImaProtocol_Type.__name__ = "Integer32"
_LpImaProtocol_Object = MibTableColumn
lpImaProtocol = _LpImaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 10, 1, 6),
    _LpImaProtocol_Type()
)
lpImaProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaProtocol.setStatus("mandatory")
_LpImaOperTable_Object = MibTable
lpImaOperTable = _LpImaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11)
)
if mibBuilder.loadTexts:
    lpImaOperTable.setStatus("mandatory")
_LpImaOperEntry_Object = MibTableRow
lpImaOperEntry = _LpImaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1)
)
lpImaOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
)
if mibBuilder.loadTexts:
    lpImaOperEntry.setStatus("mandatory")


class _LpImaFailureCause_Type(Integer32):
    """Custom type lpImaFailureCause based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("badGidInStartup", 2),
          ("badLidInStartup", 3),
          ("noFailure", 0),
          ("noGoodLinks", 6),
          ("noGoodLinksInStartup", 1),
          ("remoteFailure", 7),
          ("timeoutInStartup", 5),
          ("unsupportedFrameLengthInStartup", 4),
          ("unsupportedSymmetryInStartup", 8))
    )


_LpImaFailureCause_Type.__name__ = "Integer32"
_LpImaFailureCause_Object = MibTableColumn
lpImaFailureCause = _LpImaFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1, 1),
    _LpImaFailureCause_Type()
)
lpImaFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaFailureCause.setStatus("mandatory")


class _LpImaRemoteDefect_Type(Integer32):
    """Custom type lpImaRemoteDefect based on Integer32"""
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("badGidInStartup", 2),
          ("badLidInStartup", 3),
          ("blocked", 11),
          ("insufficientLinks", 10),
          ("locked", 7),
          ("noDefect", 0),
          ("noGoodLinks", 6),
          ("noGoodLinksInStartup", 1),
          ("otherAbortStartup", 9),
          ("timeoutInStartup", 5),
          ("unsupportedFrameLengthInStartup", 4),
          ("unsupportedSymmetryInStartup", 8))
    )


_LpImaRemoteDefect_Type.__name__ = "Integer32"
_LpImaRemoteDefect_Object = MibTableColumn
lpImaRemoteDefect = _LpImaRemoteDefect_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1, 2),
    _LpImaRemoteDefect_Type()
)
lpImaRemoteDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaRemoteDefect.setStatus("mandatory")


class _LpImaRemoteLidsConfig_Type(OctetString):
    """Custom type lpImaRemoteLidsConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpImaRemoteLidsConfig_Type.__name__ = "OctetString"
_LpImaRemoteLidsConfig_Object = MibTableColumn
lpImaRemoteLidsConfig = _LpImaRemoteLidsConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1, 3),
    _LpImaRemoteLidsConfig_Type()
)
lpImaRemoteLidsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaRemoteLidsConfig.setStatus("mandatory")


class _LpImaRemoteLidsActive_Type(OctetString):
    """Custom type lpImaRemoteLidsActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpImaRemoteLidsActive_Type.__name__ = "OctetString"
_LpImaRemoteLidsActive_Object = MibTableColumn
lpImaRemoteLidsActive = _LpImaRemoteLidsActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1, 4),
    _LpImaRemoteLidsActive_Type()
)
lpImaRemoteLidsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaRemoteLidsActive.setStatus("mandatory")


class _LpImaCellCapacity_Type(Unsigned32):
    """Custom type lpImaCellCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaCellCapacity_Type.__name__ = "Unsigned32"
_LpImaCellCapacity_Object = MibTableColumn
lpImaCellCapacity = _LpImaCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1, 5),
    _LpImaCellCapacity_Type()
)
lpImaCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaCellCapacity.setStatus("mandatory")


class _LpImaRemoteGid_Type(Unsigned32):
    """Custom type lpImaRemoteGid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LpImaRemoteGid_Type.__name__ = "Unsigned32"
_LpImaRemoteGid_Object = MibTableColumn
lpImaRemoteGid = _LpImaRemoteGid_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1, 6),
    _LpImaRemoteGid_Type()
)
lpImaRemoteGid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaRemoteGid.setStatus("mandatory")


class _LpImaClockingModeMismatch_Type(Integer32):
    """Custom type lpImaClockingModeMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_LpImaClockingModeMismatch_Type.__name__ = "Integer32"
_LpImaClockingModeMismatch_Object = MibTableColumn
lpImaClockingModeMismatch = _LpImaClockingModeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 11, 1, 7),
    _LpImaClockingModeMismatch_Type()
)
lpImaClockingModeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaClockingModeMismatch.setStatus("mandatory")
_LpImaStatsTable_Object = MibTable
lpImaStatsTable = _LpImaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 12)
)
if mibBuilder.loadTexts:
    lpImaStatsTable.setStatus("mandatory")
_LpImaStatsEntry_Object = MibTableRow
lpImaStatsEntry = _LpImaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 12, 1)
)
lpImaStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
)
if mibBuilder.loadTexts:
    lpImaStatsEntry.setStatus("mandatory")


class _LpImaRunningTime_Type(Unsigned32):
    """Custom type lpImaRunningTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaRunningTime_Type.__name__ = "Unsigned32"
_LpImaRunningTime_Object = MibTableColumn
lpImaRunningTime = _LpImaRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 12, 1, 1),
    _LpImaRunningTime_Type()
)
lpImaRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaRunningTime.setStatus("mandatory")


class _LpImaUnavailSecs_Type(Unsigned32):
    """Custom type lpImaUnavailSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaUnavailSecs_Type.__name__ = "Unsigned32"
_LpImaUnavailSecs_Object = MibTableColumn
lpImaUnavailSecs = _LpImaUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 12, 1, 2),
    _LpImaUnavailSecs_Type()
)
lpImaUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaUnavailSecs.setStatus("mandatory")


class _LpImaFailures_Type(Unsigned32):
    """Custom type lpImaFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpImaFailures_Type.__name__ = "Unsigned32"
_LpImaFailures_Object = MibTableColumn
lpImaFailures = _LpImaFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 12, 1, 3),
    _LpImaFailures_Type()
)
lpImaFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaFailures.setStatus("mandatory")


class _LpImaReceiveCellUtilization_Type(Gauge32):
    """Custom type lpImaReceiveCellUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpImaReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpImaReceiveCellUtilization_Object = MibTableColumn
lpImaReceiveCellUtilization = _LpImaReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 12, 1, 4),
    _LpImaReceiveCellUtilization_Type()
)
lpImaReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaReceiveCellUtilization.setStatus("mandatory")


class _LpImaTransmitCellUtilization_Type(Gauge32):
    """Custom type lpImaTransmitCellUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpImaTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpImaTransmitCellUtilization_Object = MibTableColumn
lpImaTransmitCellUtilization = _LpImaTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 12, 1, 5),
    _LpImaTransmitCellUtilization_Type()
)
lpImaTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaTransmitCellUtilization.setStatus("mandatory")
_LpImaCidDataTable_Object = MibTable
lpImaCidDataTable = _LpImaCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 13)
)
if mibBuilder.loadTexts:
    lpImaCidDataTable.setStatus("mandatory")
_LpImaCidDataEntry_Object = MibTableRow
lpImaCidDataEntry = _LpImaCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 13, 1)
)
lpImaCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
)
if mibBuilder.loadTexts:
    lpImaCidDataEntry.setStatus("mandatory")


class _LpImaCustomerIdentifier_Type(Unsigned32):
    """Custom type lpImaCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpImaCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpImaCustomerIdentifier_Object = MibTableColumn
lpImaCustomerIdentifier = _LpImaCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 13, 1, 1),
    _LpImaCustomerIdentifier_Type()
)
lpImaCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpImaCustomerIdentifier.setStatus("mandatory")
_LpImaStateTable_Object = MibTable
lpImaStateTable = _LpImaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14)
)
if mibBuilder.loadTexts:
    lpImaStateTable.setStatus("mandatory")
_LpImaStateEntry_Object = MibTableRow
lpImaStateEntry = _LpImaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1)
)
lpImaStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-ImaMIB", "lpImaIndex"),
)
if mibBuilder.loadTexts:
    lpImaStateEntry.setStatus("mandatory")


class _LpImaAdminState_Type(Integer32):
    """Custom type lpImaAdminState based on Integer32"""
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


_LpImaAdminState_Type.__name__ = "Integer32"
_LpImaAdminState_Object = MibTableColumn
lpImaAdminState = _LpImaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 1),
    _LpImaAdminState_Type()
)
lpImaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaAdminState.setStatus("mandatory")


class _LpImaOperationalState_Type(Integer32):
    """Custom type lpImaOperationalState based on Integer32"""
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


_LpImaOperationalState_Type.__name__ = "Integer32"
_LpImaOperationalState_Object = MibTableColumn
lpImaOperationalState = _LpImaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 2),
    _LpImaOperationalState_Type()
)
lpImaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaOperationalState.setStatus("mandatory")


class _LpImaUsageState_Type(Integer32):
    """Custom type lpImaUsageState based on Integer32"""
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


_LpImaUsageState_Type.__name__ = "Integer32"
_LpImaUsageState_Object = MibTableColumn
lpImaUsageState = _LpImaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 3),
    _LpImaUsageState_Type()
)
lpImaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaUsageState.setStatus("mandatory")


class _LpImaAvailabilityStatus_Type(OctetString):
    """Custom type lpImaAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpImaAvailabilityStatus_Type.__name__ = "OctetString"
_LpImaAvailabilityStatus_Object = MibTableColumn
lpImaAvailabilityStatus = _LpImaAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 4),
    _LpImaAvailabilityStatus_Type()
)
lpImaAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaAvailabilityStatus.setStatus("mandatory")


class _LpImaProceduralStatus_Type(OctetString):
    """Custom type lpImaProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpImaProceduralStatus_Type.__name__ = "OctetString"
_LpImaProceduralStatus_Object = MibTableColumn
lpImaProceduralStatus = _LpImaProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 5),
    _LpImaProceduralStatus_Type()
)
lpImaProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaProceduralStatus.setStatus("mandatory")


class _LpImaControlStatus_Type(OctetString):
    """Custom type lpImaControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpImaControlStatus_Type.__name__ = "OctetString"
_LpImaControlStatus_Object = MibTableColumn
lpImaControlStatus = _LpImaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 6),
    _LpImaControlStatus_Type()
)
lpImaControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaControlStatus.setStatus("mandatory")


class _LpImaAlarmStatus_Type(OctetString):
    """Custom type lpImaAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpImaAlarmStatus_Type.__name__ = "OctetString"
_LpImaAlarmStatus_Object = MibTableColumn
lpImaAlarmStatus = _LpImaAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 7),
    _LpImaAlarmStatus_Type()
)
lpImaAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaAlarmStatus.setStatus("mandatory")


class _LpImaStandbyStatus_Type(Integer32):
    """Custom type lpImaStandbyStatus based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              15)
        )
    )
    namedValues = NamedValues(
        *(("coldStandby", 1),
          ("hotStandby", 0),
          ("notSet", 15),
          ("providingService", 2))
    )


_LpImaStandbyStatus_Type.__name__ = "Integer32"
_LpImaStandbyStatus_Object = MibTableColumn
lpImaStandbyStatus = _LpImaStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 8),
    _LpImaStandbyStatus_Type()
)
lpImaStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaStandbyStatus.setStatus("mandatory")


class _LpImaUnknownStatus_Type(Integer32):
    """Custom type lpImaUnknownStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_LpImaUnknownStatus_Type.__name__ = "Integer32"
_LpImaUnknownStatus_Object = MibTableColumn
lpImaUnknownStatus = _LpImaUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 22, 14, 1, 9),
    _LpImaUnknownStatus_Type()
)
lpImaUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpImaUnknownStatus.setStatus("mandatory")
_ImaMIB_ObjectIdentity = ObjectIdentity
imaMIB = _ImaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115)
)
_ImaGroup_ObjectIdentity = ObjectIdentity
imaGroup = _ImaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 1)
)
_ImaGroupBE_ObjectIdentity = ObjectIdentity
imaGroupBE = _ImaGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 1, 5)
)
_ImaGroupBE00_ObjectIdentity = ObjectIdentity
imaGroupBE00 = _ImaGroupBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 1, 5, 1)
)
_ImaGroupBE00A_ObjectIdentity = ObjectIdentity
imaGroupBE00A = _ImaGroupBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 1, 5, 1, 2)
)
_ImaCapabilities_ObjectIdentity = ObjectIdentity
imaCapabilities = _ImaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 3)
)
_ImaCapabilitiesBE_ObjectIdentity = ObjectIdentity
imaCapabilitiesBE = _ImaCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 3, 5)
)
_ImaCapabilitiesBE00_ObjectIdentity = ObjectIdentity
imaCapabilitiesBE00 = _ImaCapabilitiesBE00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 3, 5, 1)
)
_ImaCapabilitiesBE00A_ObjectIdentity = ObjectIdentity
imaCapabilitiesBE00A = _ImaCapabilitiesBE00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 115, 3, 5, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ImaMIB",
    **{"lpIma": lpIma,
       "lpImaRowStatusTable": lpImaRowStatusTable,
       "lpImaRowStatusEntry": lpImaRowStatusEntry,
       "lpImaRowStatus": lpImaRowStatus,
       "lpImaComponentName": lpImaComponentName,
       "lpImaStorageType": lpImaStorageType,
       "lpImaIndex": lpImaIndex,
       "lpImaTest": lpImaTest,
       "lpImaTestRowStatusTable": lpImaTestRowStatusTable,
       "lpImaTestRowStatusEntry": lpImaTestRowStatusEntry,
       "lpImaTestRowStatus": lpImaTestRowStatus,
       "lpImaTestComponentName": lpImaTestComponentName,
       "lpImaTestStorageType": lpImaTestStorageType,
       "lpImaTestIndex": lpImaTestIndex,
       "lpImaTestStateTable": lpImaTestStateTable,
       "lpImaTestStateEntry": lpImaTestStateEntry,
       "lpImaTestAdminState": lpImaTestAdminState,
       "lpImaTestOperationalState": lpImaTestOperationalState,
       "lpImaTestUsageState": lpImaTestUsageState,
       "lpImaTestSetupTable": lpImaTestSetupTable,
       "lpImaTestSetupEntry": lpImaTestSetupEntry,
       "lpImaTestPurpose": lpImaTestPurpose,
       "lpImaTestType": lpImaTestType,
       "lpImaTestFrmSize": lpImaTestFrmSize,
       "lpImaTestFrmPatternType": lpImaTestFrmPatternType,
       "lpImaTestCustomizedPattern": lpImaTestCustomizedPattern,
       "lpImaTestDataStartDelay": lpImaTestDataStartDelay,
       "lpImaTestDisplayInterval": lpImaTestDisplayInterval,
       "lpImaTestDuration": lpImaTestDuration,
       "lpImaTestResultsTable": lpImaTestResultsTable,
       "lpImaTestResultsEntry": lpImaTestResultsEntry,
       "lpImaTestElapsedTime": lpImaTestElapsedTime,
       "lpImaTestTimeRemaining": lpImaTestTimeRemaining,
       "lpImaTestCauseOfTermination": lpImaTestCauseOfTermination,
       "lpImaTestBitsTx": lpImaTestBitsTx,
       "lpImaTestBytesTx": lpImaTestBytesTx,
       "lpImaTestFrmTx": lpImaTestFrmTx,
       "lpImaTestBitsRx": lpImaTestBitsRx,
       "lpImaTestBytesRx": lpImaTestBytesRx,
       "lpImaTestFrmRx": lpImaTestFrmRx,
       "lpImaTestErroredFrmRx": lpImaTestErroredFrmRx,
       "lpImaTestBitErrorRate": lpImaTestBitErrorRate,
       "lpImaLk": lpImaLk,
       "lpImaLkRowStatusTable": lpImaLkRowStatusTable,
       "lpImaLkRowStatusEntry": lpImaLkRowStatusEntry,
       "lpImaLkRowStatus": lpImaLkRowStatus,
       "lpImaLkComponentName": lpImaLkComponentName,
       "lpImaLkStorageType": lpImaLkStorageType,
       "lpImaLkIndex": lpImaLkIndex,
       "lpImaLkProvTable": lpImaLkProvTable,
       "lpImaLkProvEntry": lpImaLkProvEntry,
       "lpImaLkInterfaceName": lpImaLkInterfaceName,
       "lpImaLkOperTable": lpImaLkOperTable,
       "lpImaLkOperEntry": lpImaLkOperEntry,
       "lpImaLkFailureCause": lpImaLkFailureCause,
       "lpImaLkRemoteDefect": lpImaLkRemoteDefect,
       "lpImaLkRemoteLid": lpImaLkRemoteLid,
       "lpImaLkRelativeDelay": lpImaLkRelativeDelay,
       "lpImaLkLastOifCause": lpImaLkLastOifCause,
       "lpImaLkStatsTable": lpImaLkStatsTable,
       "lpImaLkStatsEntry": lpImaLkStatsEntry,
       "lpImaLkRunningTime": lpImaLkRunningTime,
       "lpImaLkUnavailSecs": lpImaLkUnavailSecs,
       "lpImaLkFailures": lpImaLkFailures,
       "lpImaLkUnusableSec": lpImaLkUnusableSec,
       "lpImaLkSevErroredSec": lpImaLkSevErroredSec,
       "lpImaLkFarEndUnusableSec": lpImaLkFarEndUnusableSec,
       "lpImaLkFarEndSevErroredSec": lpImaLkFarEndSevErroredSec,
       "lpImaLkFarEndUnavailSec": lpImaLkFarEndUnavailSec,
       "lpImaLkIcpViolations": lpImaLkIcpViolations,
       "lpImaLkTxStuffEvents": lpImaLkTxStuffEvents,
       "lpImaLkRxStuffEvents": lpImaLkRxStuffEvents,
       "lpImaLkIdleCellSec": lpImaLkIdleCellSec,
       "lpImaLkStateTable": lpImaLkStateTable,
       "lpImaLkStateEntry": lpImaLkStateEntry,
       "lpImaLkAdminState": lpImaLkAdminState,
       "lpImaLkOperationalState": lpImaLkOperationalState,
       "lpImaLkUsageState": lpImaLkUsageState,
       "lpImaLkAvailabilityStatus": lpImaLkAvailabilityStatus,
       "lpImaLkProceduralStatus": lpImaLkProceduralStatus,
       "lpImaLkControlStatus": lpImaLkControlStatus,
       "lpImaLkAlarmStatus": lpImaLkAlarmStatus,
       "lpImaLkStandbyStatus": lpImaLkStandbyStatus,
       "lpImaLkUnknownStatus": lpImaLkUnknownStatus,
       "lpImaProvTable": lpImaProvTable,
       "lpImaProvEntry": lpImaProvEntry,
       "lpImaLinkSelectionCriterion": lpImaLinkSelectionCriterion,
       "lpImaMaxDiffDelay": lpImaMaxDiffDelay,
       "lpImaLinkRetryTimeout": lpImaLinkRetryTimeout,
       "lpImaApplicationFramerName": lpImaApplicationFramerName,
       "lpImaTransmitClockMode": lpImaTransmitClockMode,
       "lpImaProtocol": lpImaProtocol,
       "lpImaOperTable": lpImaOperTable,
       "lpImaOperEntry": lpImaOperEntry,
       "lpImaFailureCause": lpImaFailureCause,
       "lpImaRemoteDefect": lpImaRemoteDefect,
       "lpImaRemoteLidsConfig": lpImaRemoteLidsConfig,
       "lpImaRemoteLidsActive": lpImaRemoteLidsActive,
       "lpImaCellCapacity": lpImaCellCapacity,
       "lpImaRemoteGid": lpImaRemoteGid,
       "lpImaClockingModeMismatch": lpImaClockingModeMismatch,
       "lpImaStatsTable": lpImaStatsTable,
       "lpImaStatsEntry": lpImaStatsEntry,
       "lpImaRunningTime": lpImaRunningTime,
       "lpImaUnavailSecs": lpImaUnavailSecs,
       "lpImaFailures": lpImaFailures,
       "lpImaReceiveCellUtilization": lpImaReceiveCellUtilization,
       "lpImaTransmitCellUtilization": lpImaTransmitCellUtilization,
       "lpImaCidDataTable": lpImaCidDataTable,
       "lpImaCidDataEntry": lpImaCidDataEntry,
       "lpImaCustomerIdentifier": lpImaCustomerIdentifier,
       "lpImaStateTable": lpImaStateTable,
       "lpImaStateEntry": lpImaStateEntry,
       "lpImaAdminState": lpImaAdminState,
       "lpImaOperationalState": lpImaOperationalState,
       "lpImaUsageState": lpImaUsageState,
       "lpImaAvailabilityStatus": lpImaAvailabilityStatus,
       "lpImaProceduralStatus": lpImaProceduralStatus,
       "lpImaControlStatus": lpImaControlStatus,
       "lpImaAlarmStatus": lpImaAlarmStatus,
       "lpImaStandbyStatus": lpImaStandbyStatus,
       "lpImaUnknownStatus": lpImaUnknownStatus,
       "imaMIB": imaMIB,
       "imaGroup": imaGroup,
       "imaGroupBE": imaGroupBE,
       "imaGroupBE00": imaGroupBE00,
       "imaGroupBE00A": imaGroupBE00A,
       "imaCapabilities": imaCapabilities,
       "imaCapabilitiesBE": imaCapabilitiesBE,
       "imaCapabilitiesBE00": imaCapabilitiesBE00,
       "imaCapabilitiesBE00A": imaCapabilitiesBE00A}
)
