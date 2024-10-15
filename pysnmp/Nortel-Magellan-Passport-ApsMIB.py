# SNMP MIB module (Nortel-Magellan-Passport-ApsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-ApsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:14 2024
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

(Counter32,
 DisplayString,
 Integer32,
 PassportCounter64,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "PassportCounter64",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint1,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint1",
    "Hex",
    "Link",
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

_Aps_ObjectIdentity = ObjectIdentity
aps = _Aps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134)
)
_ApsRowStatusTable_Object = MibTable
apsRowStatusTable = _ApsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1)
)
if mibBuilder.loadTexts:
    apsRowStatusTable.setStatus("mandatory")
_ApsRowStatusEntry_Object = MibTableRow
apsRowStatusEntry = _ApsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1)
)
apsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
)
if mibBuilder.loadTexts:
    apsRowStatusEntry.setStatus("mandatory")
_ApsRowStatus_Type = RowStatus
_ApsRowStatus_Object = MibTableColumn
apsRowStatus = _ApsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 1),
    _ApsRowStatus_Type()
)
apsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsRowStatus.setStatus("mandatory")
_ApsComponentName_Type = DisplayString
_ApsComponentName_Object = MibTableColumn
apsComponentName = _ApsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 2),
    _ApsComponentName_Type()
)
apsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsComponentName.setStatus("mandatory")
_ApsStorageType_Type = StorageType
_ApsStorageType_Object = MibTableColumn
apsStorageType = _ApsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 4),
    _ApsStorageType_Type()
)
apsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStorageType.setStatus("mandatory")


class _ApsIndex_Type(Integer32):
    """Custom type apsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15999),
    )


_ApsIndex_Type.__name__ = "Integer32"
_ApsIndex_Object = MibTableColumn
apsIndex = _ApsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 1, 1, 10),
    _ApsIndex_Type()
)
apsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsIndex.setStatus("mandatory")
_ApsTest_ObjectIdentity = ObjectIdentity
apsTest = _ApsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2)
)
_ApsTestRowStatusTable_Object = MibTable
apsTestRowStatusTable = _ApsTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1)
)
if mibBuilder.loadTexts:
    apsTestRowStatusTable.setStatus("mandatory")
_ApsTestRowStatusEntry_Object = MibTableRow
apsTestRowStatusEntry = _ApsTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1)
)
apsTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"),
)
if mibBuilder.loadTexts:
    apsTestRowStatusEntry.setStatus("mandatory")
_ApsTestRowStatus_Type = RowStatus
_ApsTestRowStatus_Object = MibTableColumn
apsTestRowStatus = _ApsTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 1),
    _ApsTestRowStatus_Type()
)
apsTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestRowStatus.setStatus("mandatory")
_ApsTestComponentName_Type = DisplayString
_ApsTestComponentName_Object = MibTableColumn
apsTestComponentName = _ApsTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 2),
    _ApsTestComponentName_Type()
)
apsTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestComponentName.setStatus("mandatory")
_ApsTestStorageType_Type = StorageType
_ApsTestStorageType_Object = MibTableColumn
apsTestStorageType = _ApsTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 4),
    _ApsTestStorageType_Type()
)
apsTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestStorageType.setStatus("mandatory")
_ApsTestIndex_Type = NonReplicated
_ApsTestIndex_Object = MibTableColumn
apsTestIndex = _ApsTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 1, 1, 10),
    _ApsTestIndex_Type()
)
apsTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apsTestIndex.setStatus("mandatory")
_ApsTestStateTable_Object = MibTable
apsTestStateTable = _ApsTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10)
)
if mibBuilder.loadTexts:
    apsTestStateTable.setStatus("mandatory")
_ApsTestStateEntry_Object = MibTableRow
apsTestStateEntry = _ApsTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1)
)
apsTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"),
)
if mibBuilder.loadTexts:
    apsTestStateEntry.setStatus("mandatory")


class _ApsTestAdminState_Type(Integer32):
    """Custom type apsTestAdminState based on Integer32"""
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


_ApsTestAdminState_Type.__name__ = "Integer32"
_ApsTestAdminState_Object = MibTableColumn
apsTestAdminState = _ApsTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1, 1),
    _ApsTestAdminState_Type()
)
apsTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestAdminState.setStatus("mandatory")


class _ApsTestOperationalState_Type(Integer32):
    """Custom type apsTestOperationalState based on Integer32"""
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


_ApsTestOperationalState_Type.__name__ = "Integer32"
_ApsTestOperationalState_Object = MibTableColumn
apsTestOperationalState = _ApsTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1, 2),
    _ApsTestOperationalState_Type()
)
apsTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestOperationalState.setStatus("mandatory")


class _ApsTestUsageState_Type(Integer32):
    """Custom type apsTestUsageState based on Integer32"""
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


_ApsTestUsageState_Type.__name__ = "Integer32"
_ApsTestUsageState_Object = MibTableColumn
apsTestUsageState = _ApsTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 10, 1, 3),
    _ApsTestUsageState_Type()
)
apsTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestUsageState.setStatus("mandatory")
_ApsTestSetupTable_Object = MibTable
apsTestSetupTable = _ApsTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11)
)
if mibBuilder.loadTexts:
    apsTestSetupTable.setStatus("mandatory")
_ApsTestSetupEntry_Object = MibTableRow
apsTestSetupEntry = _ApsTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1)
)
apsTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"),
)
if mibBuilder.loadTexts:
    apsTestSetupEntry.setStatus("mandatory")


class _ApsTestPurpose_Type(AsciiString):
    """Custom type apsTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ApsTestPurpose_Type.__name__ = "AsciiString"
_ApsTestPurpose_Object = MibTableColumn
apsTestPurpose = _ApsTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 1),
    _ApsTestPurpose_Type()
)
apsTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestPurpose.setStatus("mandatory")


class _ApsTestType_Type(Integer32):
    """Custom type apsTestType based on Integer32"""
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


_ApsTestType_Type.__name__ = "Integer32"
_ApsTestType_Object = MibTableColumn
apsTestType = _ApsTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 2),
    _ApsTestType_Type()
)
apsTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestType.setStatus("mandatory")


class _ApsTestFrmSize_Type(Unsigned32):
    """Custom type apsTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_ApsTestFrmSize_Type.__name__ = "Unsigned32"
_ApsTestFrmSize_Object = MibTableColumn
apsTestFrmSize = _ApsTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 3),
    _ApsTestFrmSize_Type()
)
apsTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestFrmSize.setStatus("mandatory")


class _ApsTestFrmPatternType_Type(Integer32):
    """Custom type apsTestFrmPatternType based on Integer32"""
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


_ApsTestFrmPatternType_Type.__name__ = "Integer32"
_ApsTestFrmPatternType_Object = MibTableColumn
apsTestFrmPatternType = _ApsTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 4),
    _ApsTestFrmPatternType_Type()
)
apsTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestFrmPatternType.setStatus("mandatory")


class _ApsTestCustomizedPattern_Type(Hex):
    """Custom type apsTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ApsTestCustomizedPattern_Type.__name__ = "Hex"
_ApsTestCustomizedPattern_Object = MibTableColumn
apsTestCustomizedPattern = _ApsTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 5),
    _ApsTestCustomizedPattern_Type()
)
apsTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestCustomizedPattern.setStatus("mandatory")


class _ApsTestDataStartDelay_Type(Unsigned32):
    """Custom type apsTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_ApsTestDataStartDelay_Type.__name__ = "Unsigned32"
_ApsTestDataStartDelay_Object = MibTableColumn
apsTestDataStartDelay = _ApsTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 6),
    _ApsTestDataStartDelay_Type()
)
apsTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestDataStartDelay.setStatus("mandatory")


class _ApsTestDisplayInterval_Type(Unsigned32):
    """Custom type apsTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_ApsTestDisplayInterval_Type.__name__ = "Unsigned32"
_ApsTestDisplayInterval_Object = MibTableColumn
apsTestDisplayInterval = _ApsTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 7),
    _ApsTestDisplayInterval_Type()
)
apsTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestDisplayInterval.setStatus("mandatory")


class _ApsTestDuration_Type(Unsigned32):
    """Custom type apsTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_ApsTestDuration_Type.__name__ = "Unsigned32"
_ApsTestDuration_Object = MibTableColumn
apsTestDuration = _ApsTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 11, 1, 8),
    _ApsTestDuration_Type()
)
apsTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsTestDuration.setStatus("mandatory")
_ApsTestResultsTable_Object = MibTable
apsTestResultsTable = _ApsTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12)
)
if mibBuilder.loadTexts:
    apsTestResultsTable.setStatus("mandatory")
_ApsTestResultsEntry_Object = MibTableRow
apsTestResultsEntry = _ApsTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1)
)
apsTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsTestIndex"),
)
if mibBuilder.loadTexts:
    apsTestResultsEntry.setStatus("mandatory")
_ApsTestElapsedTime_Type = Counter32
_ApsTestElapsedTime_Object = MibTableColumn
apsTestElapsedTime = _ApsTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 1),
    _ApsTestElapsedTime_Type()
)
apsTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestElapsedTime.setStatus("mandatory")


class _ApsTestTimeRemaining_Type(Unsigned32):
    """Custom type apsTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ApsTestTimeRemaining_Type.__name__ = "Unsigned32"
_ApsTestTimeRemaining_Object = MibTableColumn
apsTestTimeRemaining = _ApsTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 2),
    _ApsTestTimeRemaining_Type()
)
apsTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestTimeRemaining.setStatus("mandatory")


class _ApsTestCauseOfTermination_Type(Integer32):
    """Custom type apsTestCauseOfTermination based on Integer32"""
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


_ApsTestCauseOfTermination_Type.__name__ = "Integer32"
_ApsTestCauseOfTermination_Object = MibTableColumn
apsTestCauseOfTermination = _ApsTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 3),
    _ApsTestCauseOfTermination_Type()
)
apsTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestCauseOfTermination.setStatus("mandatory")
_ApsTestBitsTx_Type = PassportCounter64
_ApsTestBitsTx_Object = MibTableColumn
apsTestBitsTx = _ApsTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 4),
    _ApsTestBitsTx_Type()
)
apsTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestBitsTx.setStatus("mandatory")
_ApsTestBytesTx_Type = PassportCounter64
_ApsTestBytesTx_Object = MibTableColumn
apsTestBytesTx = _ApsTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 5),
    _ApsTestBytesTx_Type()
)
apsTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestBytesTx.setStatus("mandatory")
_ApsTestFrmTx_Type = PassportCounter64
_ApsTestFrmTx_Object = MibTableColumn
apsTestFrmTx = _ApsTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 6),
    _ApsTestFrmTx_Type()
)
apsTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestFrmTx.setStatus("mandatory")
_ApsTestBitsRx_Type = PassportCounter64
_ApsTestBitsRx_Object = MibTableColumn
apsTestBitsRx = _ApsTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 7),
    _ApsTestBitsRx_Type()
)
apsTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestBitsRx.setStatus("mandatory")
_ApsTestBytesRx_Type = PassportCounter64
_ApsTestBytesRx_Object = MibTableColumn
apsTestBytesRx = _ApsTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 8),
    _ApsTestBytesRx_Type()
)
apsTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestBytesRx.setStatus("mandatory")
_ApsTestFrmRx_Type = PassportCounter64
_ApsTestFrmRx_Object = MibTableColumn
apsTestFrmRx = _ApsTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 9),
    _ApsTestFrmRx_Type()
)
apsTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestFrmRx.setStatus("mandatory")
_ApsTestErroredFrmRx_Type = PassportCounter64
_ApsTestErroredFrmRx_Object = MibTableColumn
apsTestErroredFrmRx = _ApsTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 10),
    _ApsTestErroredFrmRx_Type()
)
apsTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestErroredFrmRx.setStatus("mandatory")


class _ApsTestBitErrorRate_Type(AsciiString):
    """Custom type apsTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_ApsTestBitErrorRate_Type.__name__ = "AsciiString"
_ApsTestBitErrorRate_Object = MibTableColumn
apsTestBitErrorRate = _ApsTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 2, 12, 1, 11),
    _ApsTestBitErrorRate_Type()
)
apsTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTestBitErrorRate.setStatus("mandatory")
_ApsCidDataTable_Object = MibTable
apsCidDataTable = _ApsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 10)
)
if mibBuilder.loadTexts:
    apsCidDataTable.setStatus("mandatory")
_ApsCidDataEntry_Object = MibTableRow
apsCidDataEntry = _ApsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 10, 1)
)
apsCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
)
if mibBuilder.loadTexts:
    apsCidDataEntry.setStatus("mandatory")


class _ApsCustomerIdentifier_Type(Unsigned32):
    """Custom type apsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_ApsCustomerIdentifier_Type.__name__ = "Unsigned32"
_ApsCustomerIdentifier_Object = MibTableColumn
apsCustomerIdentifier = _ApsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 10, 1, 1),
    _ApsCustomerIdentifier_Type()
)
apsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsCustomerIdentifier.setStatus("mandatory")
_ApsProvTable_Object = MibTable
apsProvTable = _ApsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11)
)
if mibBuilder.loadTexts:
    apsProvTable.setStatus("mandatory")
_ApsProvEntry_Object = MibTableRow
apsProvEntry = _ApsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1)
)
apsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
)
if mibBuilder.loadTexts:
    apsProvEntry.setStatus("mandatory")
_ApsApplicationFramerName_Type = Link
_ApsApplicationFramerName_Object = MibTableColumn
apsApplicationFramerName = _ApsApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 1),
    _ApsApplicationFramerName_Type()
)
apsApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsApplicationFramerName.setStatus("mandatory")
_ApsWorkingLine_Type = Link
_ApsWorkingLine_Object = MibTableColumn
apsWorkingLine = _ApsWorkingLine_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 2),
    _ApsWorkingLine_Type()
)
apsWorkingLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsWorkingLine.setStatus("mandatory")
_ApsProtectionLine_Type = Link
_ApsProtectionLine_Object = MibTableColumn
apsProtectionLine = _ApsProtectionLine_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 3),
    _ApsProtectionLine_Type()
)
apsProtectionLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsProtectionLine.setStatus("mandatory")


class _ApsMode_Type(Integer32):
    """Custom type apsMode based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 5),
          ("unidirectional", 4))
    )


_ApsMode_Type.__name__ = "Integer32"
_ApsMode_Object = MibTableColumn
apsMode = _ApsMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 4),
    _ApsMode_Type()
)
apsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsMode.setStatus("mandatory")


class _ApsRevertive_Type(Integer32):
    """Custom type apsRevertive based on Integer32"""
    defaultValue = 0

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


_ApsRevertive_Type.__name__ = "Integer32"
_ApsRevertive_Object = MibTableColumn
apsRevertive = _ApsRevertive_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 5),
    _ApsRevertive_Type()
)
apsRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsRevertive.setStatus("mandatory")


class _ApsHoldOffTime_Type(FixedPoint1):
    """Custom type apsHoldOffTime based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ApsHoldOffTime_Type.__name__ = "FixedPoint1"
_ApsHoldOffTime_Object = MibTableColumn
apsHoldOffTime = _ApsHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 6),
    _ApsHoldOffTime_Type()
)
apsHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsHoldOffTime.setStatus("mandatory")


class _ApsWaitToRestorePeriod_Type(Unsigned32):
    """Custom type apsWaitToRestorePeriod based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_ApsWaitToRestorePeriod_Type.__name__ = "Unsigned32"
_ApsWaitToRestorePeriod_Object = MibTableColumn
apsWaitToRestorePeriod = _ApsWaitToRestorePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 7),
    _ApsWaitToRestorePeriod_Type()
)
apsWaitToRestorePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsWaitToRestorePeriod.setStatus("mandatory")


class _ApsSignalDegradeRatio_Type(Integer32):
    """Custom type apsSignalDegradeRatio based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9, -5),
    )


_ApsSignalDegradeRatio_Type.__name__ = "Integer32"
_ApsSignalDegradeRatio_Object = MibTableColumn
apsSignalDegradeRatio = _ApsSignalDegradeRatio_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 11, 1, 8),
    _ApsSignalDegradeRatio_Type()
)
apsSignalDegradeRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apsSignalDegradeRatio.setStatus("mandatory")
_ApsStateTable_Object = MibTable
apsStateTable = _ApsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12)
)
if mibBuilder.loadTexts:
    apsStateTable.setStatus("mandatory")
_ApsStateEntry_Object = MibTableRow
apsStateEntry = _ApsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1)
)
apsStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
)
if mibBuilder.loadTexts:
    apsStateEntry.setStatus("mandatory")


class _ApsAdminState_Type(Integer32):
    """Custom type apsAdminState based on Integer32"""
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


_ApsAdminState_Type.__name__ = "Integer32"
_ApsAdminState_Object = MibTableColumn
apsAdminState = _ApsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 1),
    _ApsAdminState_Type()
)
apsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsAdminState.setStatus("mandatory")


class _ApsOperationalState_Type(Integer32):
    """Custom type apsOperationalState based on Integer32"""
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


_ApsOperationalState_Type.__name__ = "Integer32"
_ApsOperationalState_Object = MibTableColumn
apsOperationalState = _ApsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 2),
    _ApsOperationalState_Type()
)
apsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsOperationalState.setStatus("mandatory")


class _ApsUsageState_Type(Integer32):
    """Custom type apsUsageState based on Integer32"""
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


_ApsUsageState_Type.__name__ = "Integer32"
_ApsUsageState_Object = MibTableColumn
apsUsageState = _ApsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 3),
    _ApsUsageState_Type()
)
apsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsUsageState.setStatus("mandatory")


class _ApsAvailabilityStatus_Type(OctetString):
    """Custom type apsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ApsAvailabilityStatus_Type.__name__ = "OctetString"
_ApsAvailabilityStatus_Object = MibTableColumn
apsAvailabilityStatus = _ApsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 4),
    _ApsAvailabilityStatus_Type()
)
apsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsAvailabilityStatus.setStatus("mandatory")


class _ApsProceduralStatus_Type(OctetString):
    """Custom type apsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ApsProceduralStatus_Type.__name__ = "OctetString"
_ApsProceduralStatus_Object = MibTableColumn
apsProceduralStatus = _ApsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 5),
    _ApsProceduralStatus_Type()
)
apsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsProceduralStatus.setStatus("mandatory")


class _ApsControlStatus_Type(OctetString):
    """Custom type apsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ApsControlStatus_Type.__name__ = "OctetString"
_ApsControlStatus_Object = MibTableColumn
apsControlStatus = _ApsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 6),
    _ApsControlStatus_Type()
)
apsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsControlStatus.setStatus("mandatory")


class _ApsAlarmStatus_Type(OctetString):
    """Custom type apsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ApsAlarmStatus_Type.__name__ = "OctetString"
_ApsAlarmStatus_Object = MibTableColumn
apsAlarmStatus = _ApsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 7),
    _ApsAlarmStatus_Type()
)
apsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsAlarmStatus.setStatus("mandatory")


class _ApsStandbyStatus_Type(Integer32):
    """Custom type apsStandbyStatus based on Integer32"""
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


_ApsStandbyStatus_Type.__name__ = "Integer32"
_ApsStandbyStatus_Object = MibTableColumn
apsStandbyStatus = _ApsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 8),
    _ApsStandbyStatus_Type()
)
apsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsStandbyStatus.setStatus("mandatory")


class _ApsUnknownStatus_Type(Integer32):
    """Custom type apsUnknownStatus based on Integer32"""
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


_ApsUnknownStatus_Type.__name__ = "Integer32"
_ApsUnknownStatus_Object = MibTableColumn
apsUnknownStatus = _ApsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 12, 1, 9),
    _ApsUnknownStatus_Type()
)
apsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsUnknownStatus.setStatus("mandatory")
_ApsOperTable_Object = MibTable
apsOperTable = _ApsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13)
)
if mibBuilder.loadTexts:
    apsOperTable.setStatus("mandatory")
_ApsOperEntry_Object = MibTableRow
apsOperEntry = _ApsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1)
)
apsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-ApsMIB", "apsIndex"),
)
if mibBuilder.loadTexts:
    apsOperEntry.setStatus("mandatory")


class _ApsNearEndRxActiveLine_Type(Integer32):
    """Custom type apsNearEndRxActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protection", 0),
          ("working", 1))
    )


_ApsNearEndRxActiveLine_Type.__name__ = "Integer32"
_ApsNearEndRxActiveLine_Object = MibTableColumn
apsNearEndRxActiveLine = _ApsNearEndRxActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 1),
    _ApsNearEndRxActiveLine_Type()
)
apsNearEndRxActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsNearEndRxActiveLine.setStatus("mandatory")


class _ApsNearEndRequest_Type(Integer32):
    """Custom type apsNearEndRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              8,
              10,
              12,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("doNotRevert", 1),
          ("forcedSwitch", 14),
          ("lockoutOfProtection", 15),
          ("manualSwitch", 8),
          ("noRequest", 0),
          ("reverseRequest", 2),
          ("signalDegrade", 10),
          ("signalFail", 12),
          ("waitToRestore", 6))
    )


_ApsNearEndRequest_Type.__name__ = "Integer32"
_ApsNearEndRequest_Object = MibTableColumn
apsNearEndRequest = _ApsNearEndRequest_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 2),
    _ApsNearEndRequest_Type()
)
apsNearEndRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsNearEndRequest.setStatus("mandatory")


class _ApsNearEndRequestChannel_Type(Integer32):
    """Custom type apsNearEndRequestChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protection", 0),
          ("working", 1))
    )


_ApsNearEndRequestChannel_Type.__name__ = "Integer32"
_ApsNearEndRequestChannel_Object = MibTableColumn
apsNearEndRequestChannel = _ApsNearEndRequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 3),
    _ApsNearEndRequestChannel_Type()
)
apsNearEndRequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsNearEndRequestChannel.setStatus("mandatory")


class _ApsFarEndRequest_Type(Integer32):
    """Custom type apsFarEndRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              8,
              10,
              12,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("doNotRevert", 1),
          ("forcedSwitch", 14),
          ("lockoutOfProtection", 15),
          ("manualSwitch", 8),
          ("noRequest", 0),
          ("reverseRequest", 2),
          ("signalDegrade", 10),
          ("signalFail", 12),
          ("waitToRestore", 6))
    )


_ApsFarEndRequest_Type.__name__ = "Integer32"
_ApsFarEndRequest_Object = MibTableColumn
apsFarEndRequest = _ApsFarEndRequest_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 4),
    _ApsFarEndRequest_Type()
)
apsFarEndRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsFarEndRequest.setStatus("mandatory")


class _ApsFarEndRequestChannel_Type(Integer32):
    """Custom type apsFarEndRequestChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("protection", 0),
          ("working", 1))
    )


_ApsFarEndRequestChannel_Type.__name__ = "Integer32"
_ApsFarEndRequestChannel_Object = MibTableColumn
apsFarEndRequestChannel = _ApsFarEndRequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 5),
    _ApsFarEndRequestChannel_Type()
)
apsFarEndRequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsFarEndRequestChannel.setStatus("mandatory")


class _ApsSdOnLines_Type(OctetString):
    """Custom type apsSdOnLines based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ApsSdOnLines_Type.__name__ = "OctetString"
_ApsSdOnLines_Object = MibTableColumn
apsSdOnLines = _ApsSdOnLines_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 6),
    _ApsSdOnLines_Type()
)
apsSdOnLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsSdOnLines.setStatus("mandatory")
_ApsSwitchovers_Type = Counter32
_ApsSwitchovers_Object = MibTableColumn
apsSwitchovers = _ApsSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 7),
    _ApsSwitchovers_Type()
)
apsSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsSwitchovers.setStatus("mandatory")


class _ApsTimeUntilRestore_Type(Unsigned32):
    """Custom type apsTimeUntilRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ApsTimeUntilRestore_Type.__name__ = "Unsigned32"
_ApsTimeUntilRestore_Object = MibTableColumn
apsTimeUntilRestore = _ApsTimeUntilRestore_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 8),
    _ApsTimeUntilRestore_Type()
)
apsTimeUntilRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsTimeUntilRestore.setStatus("mandatory")


class _ApsProtocolFailureAlarm_Type(Integer32):
    """Custom type apsProtocolFailureAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_ApsProtocolFailureAlarm_Type.__name__ = "Integer32"
_ApsProtocolFailureAlarm_Object = MibTableColumn
apsProtocolFailureAlarm = _ApsProtocolFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 9),
    _ApsProtocolFailureAlarm_Type()
)
apsProtocolFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsProtocolFailureAlarm.setStatus("mandatory")


class _ApsModeMismatchAlarm_Type(Integer32):
    """Custom type apsModeMismatchAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0))
    )


_ApsModeMismatchAlarm_Type.__name__ = "Integer32"
_ApsModeMismatchAlarm_Object = MibTableColumn
apsModeMismatchAlarm = _ApsModeMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 134, 13, 1, 10),
    _ApsModeMismatchAlarm_Type()
)
apsModeMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apsModeMismatchAlarm.setStatus("mandatory")
_ApsMIB_ObjectIdentity = ObjectIdentity
apsMIB = _ApsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136)
)
_ApsGroup_ObjectIdentity = ObjectIdentity
apsGroup = _ApsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1)
)
_ApsGroupBF_ObjectIdentity = ObjectIdentity
apsGroupBF = _ApsGroupBF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1, 6)
)
_ApsGroupBF00_ObjectIdentity = ObjectIdentity
apsGroupBF00 = _ApsGroupBF00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1, 6, 1)
)
_ApsGroupBF00A_ObjectIdentity = ObjectIdentity
apsGroupBF00A = _ApsGroupBF00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 1, 6, 1, 2)
)
_ApsCapabilities_ObjectIdentity = ObjectIdentity
apsCapabilities = _ApsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3)
)
_ApsCapabilitiesBF_ObjectIdentity = ObjectIdentity
apsCapabilitiesBF = _ApsCapabilitiesBF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3, 6)
)
_ApsCapabilitiesBF00_ObjectIdentity = ObjectIdentity
apsCapabilitiesBF00 = _ApsCapabilitiesBF00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3, 6, 1)
)
_ApsCapabilitiesBF00A_ObjectIdentity = ObjectIdentity
apsCapabilitiesBF00A = _ApsCapabilitiesBF00A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 136, 3, 6, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-ApsMIB",
    **{"aps": aps,
       "apsRowStatusTable": apsRowStatusTable,
       "apsRowStatusEntry": apsRowStatusEntry,
       "apsRowStatus": apsRowStatus,
       "apsComponentName": apsComponentName,
       "apsStorageType": apsStorageType,
       "apsIndex": apsIndex,
       "apsTest": apsTest,
       "apsTestRowStatusTable": apsTestRowStatusTable,
       "apsTestRowStatusEntry": apsTestRowStatusEntry,
       "apsTestRowStatus": apsTestRowStatus,
       "apsTestComponentName": apsTestComponentName,
       "apsTestStorageType": apsTestStorageType,
       "apsTestIndex": apsTestIndex,
       "apsTestStateTable": apsTestStateTable,
       "apsTestStateEntry": apsTestStateEntry,
       "apsTestAdminState": apsTestAdminState,
       "apsTestOperationalState": apsTestOperationalState,
       "apsTestUsageState": apsTestUsageState,
       "apsTestSetupTable": apsTestSetupTable,
       "apsTestSetupEntry": apsTestSetupEntry,
       "apsTestPurpose": apsTestPurpose,
       "apsTestType": apsTestType,
       "apsTestFrmSize": apsTestFrmSize,
       "apsTestFrmPatternType": apsTestFrmPatternType,
       "apsTestCustomizedPattern": apsTestCustomizedPattern,
       "apsTestDataStartDelay": apsTestDataStartDelay,
       "apsTestDisplayInterval": apsTestDisplayInterval,
       "apsTestDuration": apsTestDuration,
       "apsTestResultsTable": apsTestResultsTable,
       "apsTestResultsEntry": apsTestResultsEntry,
       "apsTestElapsedTime": apsTestElapsedTime,
       "apsTestTimeRemaining": apsTestTimeRemaining,
       "apsTestCauseOfTermination": apsTestCauseOfTermination,
       "apsTestBitsTx": apsTestBitsTx,
       "apsTestBytesTx": apsTestBytesTx,
       "apsTestFrmTx": apsTestFrmTx,
       "apsTestBitsRx": apsTestBitsRx,
       "apsTestBytesRx": apsTestBytesRx,
       "apsTestFrmRx": apsTestFrmRx,
       "apsTestErroredFrmRx": apsTestErroredFrmRx,
       "apsTestBitErrorRate": apsTestBitErrorRate,
       "apsCidDataTable": apsCidDataTable,
       "apsCidDataEntry": apsCidDataEntry,
       "apsCustomerIdentifier": apsCustomerIdentifier,
       "apsProvTable": apsProvTable,
       "apsProvEntry": apsProvEntry,
       "apsApplicationFramerName": apsApplicationFramerName,
       "apsWorkingLine": apsWorkingLine,
       "apsProtectionLine": apsProtectionLine,
       "apsMode": apsMode,
       "apsRevertive": apsRevertive,
       "apsHoldOffTime": apsHoldOffTime,
       "apsWaitToRestorePeriod": apsWaitToRestorePeriod,
       "apsSignalDegradeRatio": apsSignalDegradeRatio,
       "apsStateTable": apsStateTable,
       "apsStateEntry": apsStateEntry,
       "apsAdminState": apsAdminState,
       "apsOperationalState": apsOperationalState,
       "apsUsageState": apsUsageState,
       "apsAvailabilityStatus": apsAvailabilityStatus,
       "apsProceduralStatus": apsProceduralStatus,
       "apsControlStatus": apsControlStatus,
       "apsAlarmStatus": apsAlarmStatus,
       "apsStandbyStatus": apsStandbyStatus,
       "apsUnknownStatus": apsUnknownStatus,
       "apsOperTable": apsOperTable,
       "apsOperEntry": apsOperEntry,
       "apsNearEndRxActiveLine": apsNearEndRxActiveLine,
       "apsNearEndRequest": apsNearEndRequest,
       "apsNearEndRequestChannel": apsNearEndRequestChannel,
       "apsFarEndRequest": apsFarEndRequest,
       "apsFarEndRequestChannel": apsFarEndRequestChannel,
       "apsSdOnLines": apsSdOnLines,
       "apsSwitchovers": apsSwitchovers,
       "apsTimeUntilRestore": apsTimeUntilRestore,
       "apsProtocolFailureAlarm": apsProtocolFailureAlarm,
       "apsModeMismatchAlarm": apsModeMismatchAlarm,
       "apsMIB": apsMIB,
       "apsGroup": apsGroup,
       "apsGroupBF": apsGroupBF,
       "apsGroupBF00": apsGroupBF00,
       "apsGroupBF00A": apsGroupBF00A,
       "apsCapabilities": apsCapabilities,
       "apsCapabilitiesBF": apsCapabilitiesBF,
       "apsCapabilitiesBF00": apsCapabilitiesBF00,
       "apsCapabilitiesBF00A": apsCapabilitiesBF00A}
)
