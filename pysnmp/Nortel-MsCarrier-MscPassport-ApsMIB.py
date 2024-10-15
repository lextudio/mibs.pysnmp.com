# SNMP MIB module (Nortel-MsCarrier-MscPassport-ApsMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ApsMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:46 2024
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
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 FixedPoint1,
 Hex,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "FixedPoint1",
    "Hex",
    "Link",
    "NonReplicated",
    "PassportCounter64")

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

_MscAps_ObjectIdentity = ObjectIdentity
mscAps = _MscAps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134)
)
_MscApsRowStatusTable_Object = MibTable
mscApsRowStatusTable = _MscApsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 1)
)
if mibBuilder.loadTexts:
    mscApsRowStatusTable.setStatus("mandatory")
_MscApsRowStatusEntry_Object = MibTableRow
mscApsRowStatusEntry = _MscApsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 1, 1)
)
mscApsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
)
if mibBuilder.loadTexts:
    mscApsRowStatusEntry.setStatus("mandatory")
_MscApsRowStatus_Type = RowStatus
_MscApsRowStatus_Object = MibTableColumn
mscApsRowStatus = _MscApsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 1, 1, 1),
    _MscApsRowStatus_Type()
)
mscApsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsRowStatus.setStatus("mandatory")
_MscApsComponentName_Type = DisplayString
_MscApsComponentName_Object = MibTableColumn
mscApsComponentName = _MscApsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 1, 1, 2),
    _MscApsComponentName_Type()
)
mscApsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsComponentName.setStatus("mandatory")
_MscApsStorageType_Type = StorageType
_MscApsStorageType_Object = MibTableColumn
mscApsStorageType = _MscApsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 1, 1, 4),
    _MscApsStorageType_Type()
)
mscApsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsStorageType.setStatus("mandatory")


class _MscApsIndex_Type(Integer32):
    """Custom type mscApsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15999),
    )


_MscApsIndex_Type.__name__ = "Integer32"
_MscApsIndex_Object = MibTableColumn
mscApsIndex = _MscApsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 1, 1, 10),
    _MscApsIndex_Type()
)
mscApsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscApsIndex.setStatus("mandatory")
_MscApsTest_ObjectIdentity = ObjectIdentity
mscApsTest = _MscApsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2)
)
_MscApsTestRowStatusTable_Object = MibTable
mscApsTestRowStatusTable = _MscApsTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 1)
)
if mibBuilder.loadTexts:
    mscApsTestRowStatusTable.setStatus("mandatory")
_MscApsTestRowStatusEntry_Object = MibTableRow
mscApsTestRowStatusEntry = _MscApsTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 1, 1)
)
mscApsTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsTestIndex"),
)
if mibBuilder.loadTexts:
    mscApsTestRowStatusEntry.setStatus("mandatory")
_MscApsTestRowStatus_Type = RowStatus
_MscApsTestRowStatus_Object = MibTableColumn
mscApsTestRowStatus = _MscApsTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 1, 1, 1),
    _MscApsTestRowStatus_Type()
)
mscApsTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestRowStatus.setStatus("mandatory")
_MscApsTestComponentName_Type = DisplayString
_MscApsTestComponentName_Object = MibTableColumn
mscApsTestComponentName = _MscApsTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 1, 1, 2),
    _MscApsTestComponentName_Type()
)
mscApsTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestComponentName.setStatus("mandatory")
_MscApsTestStorageType_Type = StorageType
_MscApsTestStorageType_Object = MibTableColumn
mscApsTestStorageType = _MscApsTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 1, 1, 4),
    _MscApsTestStorageType_Type()
)
mscApsTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestStorageType.setStatus("mandatory")
_MscApsTestIndex_Type = NonReplicated
_MscApsTestIndex_Object = MibTableColumn
mscApsTestIndex = _MscApsTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 1, 1, 10),
    _MscApsTestIndex_Type()
)
mscApsTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscApsTestIndex.setStatus("mandatory")
_MscApsTestStateTable_Object = MibTable
mscApsTestStateTable = _MscApsTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 10)
)
if mibBuilder.loadTexts:
    mscApsTestStateTable.setStatus("mandatory")
_MscApsTestStateEntry_Object = MibTableRow
mscApsTestStateEntry = _MscApsTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 10, 1)
)
mscApsTestStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsTestIndex"),
)
if mibBuilder.loadTexts:
    mscApsTestStateEntry.setStatus("mandatory")


class _MscApsTestAdminState_Type(Integer32):
    """Custom type mscApsTestAdminState based on Integer32"""
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


_MscApsTestAdminState_Type.__name__ = "Integer32"
_MscApsTestAdminState_Object = MibTableColumn
mscApsTestAdminState = _MscApsTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 10, 1, 1),
    _MscApsTestAdminState_Type()
)
mscApsTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestAdminState.setStatus("mandatory")


class _MscApsTestOperationalState_Type(Integer32):
    """Custom type mscApsTestOperationalState based on Integer32"""
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


_MscApsTestOperationalState_Type.__name__ = "Integer32"
_MscApsTestOperationalState_Object = MibTableColumn
mscApsTestOperationalState = _MscApsTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 10, 1, 2),
    _MscApsTestOperationalState_Type()
)
mscApsTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestOperationalState.setStatus("mandatory")


class _MscApsTestUsageState_Type(Integer32):
    """Custom type mscApsTestUsageState based on Integer32"""
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


_MscApsTestUsageState_Type.__name__ = "Integer32"
_MscApsTestUsageState_Object = MibTableColumn
mscApsTestUsageState = _MscApsTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 10, 1, 3),
    _MscApsTestUsageState_Type()
)
mscApsTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestUsageState.setStatus("mandatory")
_MscApsTestSetupTable_Object = MibTable
mscApsTestSetupTable = _MscApsTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11)
)
if mibBuilder.loadTexts:
    mscApsTestSetupTable.setStatus("mandatory")
_MscApsTestSetupEntry_Object = MibTableRow
mscApsTestSetupEntry = _MscApsTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1)
)
mscApsTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsTestIndex"),
)
if mibBuilder.loadTexts:
    mscApsTestSetupEntry.setStatus("mandatory")


class _MscApsTestPurpose_Type(AsciiString):
    """Custom type mscApsTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscApsTestPurpose_Type.__name__ = "AsciiString"
_MscApsTestPurpose_Object = MibTableColumn
mscApsTestPurpose = _MscApsTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 1),
    _MscApsTestPurpose_Type()
)
mscApsTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestPurpose.setStatus("mandatory")


class _MscApsTestType_Type(Integer32):
    """Custom type mscApsTestType based on Integer32"""
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


_MscApsTestType_Type.__name__ = "Integer32"
_MscApsTestType_Object = MibTableColumn
mscApsTestType = _MscApsTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 2),
    _MscApsTestType_Type()
)
mscApsTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestType.setStatus("mandatory")


class _MscApsTestFrmSize_Type(Unsigned32):
    """Custom type mscApsTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscApsTestFrmSize_Type.__name__ = "Unsigned32"
_MscApsTestFrmSize_Object = MibTableColumn
mscApsTestFrmSize = _MscApsTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 3),
    _MscApsTestFrmSize_Type()
)
mscApsTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestFrmSize.setStatus("mandatory")


class _MscApsTestFrmPatternType_Type(Integer32):
    """Custom type mscApsTestFrmPatternType based on Integer32"""
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


_MscApsTestFrmPatternType_Type.__name__ = "Integer32"
_MscApsTestFrmPatternType_Object = MibTableColumn
mscApsTestFrmPatternType = _MscApsTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 4),
    _MscApsTestFrmPatternType_Type()
)
mscApsTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestFrmPatternType.setStatus("mandatory")


class _MscApsTestCustomizedPattern_Type(Hex):
    """Custom type mscApsTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscApsTestCustomizedPattern_Type.__name__ = "Hex"
_MscApsTestCustomizedPattern_Object = MibTableColumn
mscApsTestCustomizedPattern = _MscApsTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 5),
    _MscApsTestCustomizedPattern_Type()
)
mscApsTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestCustomizedPattern.setStatus("mandatory")


class _MscApsTestDataStartDelay_Type(Unsigned32):
    """Custom type mscApsTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_MscApsTestDataStartDelay_Type.__name__ = "Unsigned32"
_MscApsTestDataStartDelay_Object = MibTableColumn
mscApsTestDataStartDelay = _MscApsTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 6),
    _MscApsTestDataStartDelay_Type()
)
mscApsTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestDataStartDelay.setStatus("mandatory")


class _MscApsTestDisplayInterval_Type(Unsigned32):
    """Custom type mscApsTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_MscApsTestDisplayInterval_Type.__name__ = "Unsigned32"
_MscApsTestDisplayInterval_Object = MibTableColumn
mscApsTestDisplayInterval = _MscApsTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 7),
    _MscApsTestDisplayInterval_Type()
)
mscApsTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestDisplayInterval.setStatus("mandatory")


class _MscApsTestDuration_Type(Unsigned32):
    """Custom type mscApsTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscApsTestDuration_Type.__name__ = "Unsigned32"
_MscApsTestDuration_Object = MibTableColumn
mscApsTestDuration = _MscApsTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 11, 1, 8),
    _MscApsTestDuration_Type()
)
mscApsTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsTestDuration.setStatus("mandatory")
_MscApsTestResultsTable_Object = MibTable
mscApsTestResultsTable = _MscApsTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12)
)
if mibBuilder.loadTexts:
    mscApsTestResultsTable.setStatus("mandatory")
_MscApsTestResultsEntry_Object = MibTableRow
mscApsTestResultsEntry = _MscApsTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1)
)
mscApsTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsTestIndex"),
)
if mibBuilder.loadTexts:
    mscApsTestResultsEntry.setStatus("mandatory")
_MscApsTestElapsedTime_Type = Counter32
_MscApsTestElapsedTime_Object = MibTableColumn
mscApsTestElapsedTime = _MscApsTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 1),
    _MscApsTestElapsedTime_Type()
)
mscApsTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestElapsedTime.setStatus("mandatory")


class _MscApsTestTimeRemaining_Type(Unsigned32):
    """Custom type mscApsTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscApsTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscApsTestTimeRemaining_Object = MibTableColumn
mscApsTestTimeRemaining = _MscApsTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 2),
    _MscApsTestTimeRemaining_Type()
)
mscApsTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestTimeRemaining.setStatus("mandatory")


class _MscApsTestCauseOfTermination_Type(Integer32):
    """Custom type mscApsTestCauseOfTermination based on Integer32"""
    defaultValue = 3

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
        *(("hardwareReconfigured", 5),
          ("loopCodeSyncFailed", 6),
          ("neverStarted", 3),
          ("patternSyncFailed", 7),
          ("patternSyncLost", 8),
          ("stoppedByOperator", 1),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_MscApsTestCauseOfTermination_Type.__name__ = "Integer32"
_MscApsTestCauseOfTermination_Object = MibTableColumn
mscApsTestCauseOfTermination = _MscApsTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 3),
    _MscApsTestCauseOfTermination_Type()
)
mscApsTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestCauseOfTermination.setStatus("mandatory")
_MscApsTestBitsTx_Type = PassportCounter64
_MscApsTestBitsTx_Object = MibTableColumn
mscApsTestBitsTx = _MscApsTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 4),
    _MscApsTestBitsTx_Type()
)
mscApsTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestBitsTx.setStatus("mandatory")
_MscApsTestBytesTx_Type = PassportCounter64
_MscApsTestBytesTx_Object = MibTableColumn
mscApsTestBytesTx = _MscApsTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 5),
    _MscApsTestBytesTx_Type()
)
mscApsTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestBytesTx.setStatus("mandatory")
_MscApsTestFrmTx_Type = PassportCounter64
_MscApsTestFrmTx_Object = MibTableColumn
mscApsTestFrmTx = _MscApsTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 6),
    _MscApsTestFrmTx_Type()
)
mscApsTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestFrmTx.setStatus("mandatory")
_MscApsTestBitsRx_Type = PassportCounter64
_MscApsTestBitsRx_Object = MibTableColumn
mscApsTestBitsRx = _MscApsTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 7),
    _MscApsTestBitsRx_Type()
)
mscApsTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestBitsRx.setStatus("mandatory")
_MscApsTestBytesRx_Type = PassportCounter64
_MscApsTestBytesRx_Object = MibTableColumn
mscApsTestBytesRx = _MscApsTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 8),
    _MscApsTestBytesRx_Type()
)
mscApsTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestBytesRx.setStatus("mandatory")
_MscApsTestFrmRx_Type = PassportCounter64
_MscApsTestFrmRx_Object = MibTableColumn
mscApsTestFrmRx = _MscApsTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 9),
    _MscApsTestFrmRx_Type()
)
mscApsTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestFrmRx.setStatus("mandatory")
_MscApsTestErroredFrmRx_Type = PassportCounter64
_MscApsTestErroredFrmRx_Object = MibTableColumn
mscApsTestErroredFrmRx = _MscApsTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 10),
    _MscApsTestErroredFrmRx_Type()
)
mscApsTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestErroredFrmRx.setStatus("mandatory")


class _MscApsTestBitErrorRate_Type(AsciiString):
    """Custom type mscApsTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_MscApsTestBitErrorRate_Type.__name__ = "AsciiString"
_MscApsTestBitErrorRate_Object = MibTableColumn
mscApsTestBitErrorRate = _MscApsTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 2, 12, 1, 11),
    _MscApsTestBitErrorRate_Type()
)
mscApsTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTestBitErrorRate.setStatus("mandatory")
_MscApsCidDataTable_Object = MibTable
mscApsCidDataTable = _MscApsCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 10)
)
if mibBuilder.loadTexts:
    mscApsCidDataTable.setStatus("mandatory")
_MscApsCidDataEntry_Object = MibTableRow
mscApsCidDataEntry = _MscApsCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 10, 1)
)
mscApsCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
)
if mibBuilder.loadTexts:
    mscApsCidDataEntry.setStatus("mandatory")


class _MscApsCustomerIdentifier_Type(Unsigned32):
    """Custom type mscApsCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscApsCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscApsCustomerIdentifier_Object = MibTableColumn
mscApsCustomerIdentifier = _MscApsCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 10, 1, 1),
    _MscApsCustomerIdentifier_Type()
)
mscApsCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsCustomerIdentifier.setStatus("mandatory")
_MscApsProvTable_Object = MibTable
mscApsProvTable = _MscApsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11)
)
if mibBuilder.loadTexts:
    mscApsProvTable.setStatus("mandatory")
_MscApsProvEntry_Object = MibTableRow
mscApsProvEntry = _MscApsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1)
)
mscApsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
)
if mibBuilder.loadTexts:
    mscApsProvEntry.setStatus("mandatory")
_MscApsApplicationFramerName_Type = Link
_MscApsApplicationFramerName_Object = MibTableColumn
mscApsApplicationFramerName = _MscApsApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 1),
    _MscApsApplicationFramerName_Type()
)
mscApsApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsApplicationFramerName.setStatus("mandatory")
_MscApsWorkingLine_Type = Link
_MscApsWorkingLine_Object = MibTableColumn
mscApsWorkingLine = _MscApsWorkingLine_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 2),
    _MscApsWorkingLine_Type()
)
mscApsWorkingLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsWorkingLine.setStatus("mandatory")
_MscApsProtectionLine_Type = Link
_MscApsProtectionLine_Object = MibTableColumn
mscApsProtectionLine = _MscApsProtectionLine_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 3),
    _MscApsProtectionLine_Type()
)
mscApsProtectionLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsProtectionLine.setStatus("mandatory")


class _MscApsMode_Type(Integer32):
    """Custom type mscApsMode based on Integer32"""
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


_MscApsMode_Type.__name__ = "Integer32"
_MscApsMode_Object = MibTableColumn
mscApsMode = _MscApsMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 4),
    _MscApsMode_Type()
)
mscApsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsMode.setStatus("mandatory")


class _MscApsRevertive_Type(Integer32):
    """Custom type mscApsRevertive based on Integer32"""
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


_MscApsRevertive_Type.__name__ = "Integer32"
_MscApsRevertive_Object = MibTableColumn
mscApsRevertive = _MscApsRevertive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 5),
    _MscApsRevertive_Type()
)
mscApsRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsRevertive.setStatus("mandatory")


class _MscApsHoldOffTime_Type(FixedPoint1):
    """Custom type mscApsHoldOffTime based on FixedPoint1"""
    defaultValue = 0

    subtypeSpec = FixedPoint1.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscApsHoldOffTime_Type.__name__ = "FixedPoint1"
_MscApsHoldOffTime_Object = MibTableColumn
mscApsHoldOffTime = _MscApsHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 6),
    _MscApsHoldOffTime_Type()
)
mscApsHoldOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsHoldOffTime.setStatus("mandatory")


class _MscApsWaitToRestorePeriod_Type(Unsigned32):
    """Custom type mscApsWaitToRestorePeriod based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_MscApsWaitToRestorePeriod_Type.__name__ = "Unsigned32"
_MscApsWaitToRestorePeriod_Object = MibTableColumn
mscApsWaitToRestorePeriod = _MscApsWaitToRestorePeriod_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 7),
    _MscApsWaitToRestorePeriod_Type()
)
mscApsWaitToRestorePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsWaitToRestorePeriod.setStatus("mandatory")


class _MscApsSignalDegradeRatio_Type(Integer32):
    """Custom type mscApsSignalDegradeRatio based on Integer32"""
    defaultValue = -5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-9, -5),
    )


_MscApsSignalDegradeRatio_Type.__name__ = "Integer32"
_MscApsSignalDegradeRatio_Object = MibTableColumn
mscApsSignalDegradeRatio = _MscApsSignalDegradeRatio_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 11, 1, 8),
    _MscApsSignalDegradeRatio_Type()
)
mscApsSignalDegradeRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscApsSignalDegradeRatio.setStatus("mandatory")
_MscApsStateTable_Object = MibTable
mscApsStateTable = _MscApsStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12)
)
if mibBuilder.loadTexts:
    mscApsStateTable.setStatus("mandatory")
_MscApsStateEntry_Object = MibTableRow
mscApsStateEntry = _MscApsStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1)
)
mscApsStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
)
if mibBuilder.loadTexts:
    mscApsStateEntry.setStatus("mandatory")


class _MscApsAdminState_Type(Integer32):
    """Custom type mscApsAdminState based on Integer32"""
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


_MscApsAdminState_Type.__name__ = "Integer32"
_MscApsAdminState_Object = MibTableColumn
mscApsAdminState = _MscApsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 1),
    _MscApsAdminState_Type()
)
mscApsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsAdminState.setStatus("mandatory")


class _MscApsOperationalState_Type(Integer32):
    """Custom type mscApsOperationalState based on Integer32"""
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


_MscApsOperationalState_Type.__name__ = "Integer32"
_MscApsOperationalState_Object = MibTableColumn
mscApsOperationalState = _MscApsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 2),
    _MscApsOperationalState_Type()
)
mscApsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsOperationalState.setStatus("mandatory")


class _MscApsUsageState_Type(Integer32):
    """Custom type mscApsUsageState based on Integer32"""
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


_MscApsUsageState_Type.__name__ = "Integer32"
_MscApsUsageState_Object = MibTableColumn
mscApsUsageState = _MscApsUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 3),
    _MscApsUsageState_Type()
)
mscApsUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsUsageState.setStatus("mandatory")


class _MscApsAvailabilityStatus_Type(OctetString):
    """Custom type mscApsAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscApsAvailabilityStatus_Type.__name__ = "OctetString"
_MscApsAvailabilityStatus_Object = MibTableColumn
mscApsAvailabilityStatus = _MscApsAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 4),
    _MscApsAvailabilityStatus_Type()
)
mscApsAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsAvailabilityStatus.setStatus("mandatory")


class _MscApsProceduralStatus_Type(OctetString):
    """Custom type mscApsProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscApsProceduralStatus_Type.__name__ = "OctetString"
_MscApsProceduralStatus_Object = MibTableColumn
mscApsProceduralStatus = _MscApsProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 5),
    _MscApsProceduralStatus_Type()
)
mscApsProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsProceduralStatus.setStatus("mandatory")


class _MscApsControlStatus_Type(OctetString):
    """Custom type mscApsControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscApsControlStatus_Type.__name__ = "OctetString"
_MscApsControlStatus_Object = MibTableColumn
mscApsControlStatus = _MscApsControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 6),
    _MscApsControlStatus_Type()
)
mscApsControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsControlStatus.setStatus("mandatory")


class _MscApsAlarmStatus_Type(OctetString):
    """Custom type mscApsAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscApsAlarmStatus_Type.__name__ = "OctetString"
_MscApsAlarmStatus_Object = MibTableColumn
mscApsAlarmStatus = _MscApsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 7),
    _MscApsAlarmStatus_Type()
)
mscApsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsAlarmStatus.setStatus("mandatory")


class _MscApsStandbyStatus_Type(Integer32):
    """Custom type mscApsStandbyStatus based on Integer32"""
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


_MscApsStandbyStatus_Type.__name__ = "Integer32"
_MscApsStandbyStatus_Object = MibTableColumn
mscApsStandbyStatus = _MscApsStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 8),
    _MscApsStandbyStatus_Type()
)
mscApsStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsStandbyStatus.setStatus("mandatory")


class _MscApsUnknownStatus_Type(Integer32):
    """Custom type mscApsUnknownStatus based on Integer32"""
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


_MscApsUnknownStatus_Type.__name__ = "Integer32"
_MscApsUnknownStatus_Object = MibTableColumn
mscApsUnknownStatus = _MscApsUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 12, 1, 9),
    _MscApsUnknownStatus_Type()
)
mscApsUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsUnknownStatus.setStatus("mandatory")
_MscApsOperTable_Object = MibTable
mscApsOperTable = _MscApsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13)
)
if mibBuilder.loadTexts:
    mscApsOperTable.setStatus("mandatory")
_MscApsOperEntry_Object = MibTableRow
mscApsOperEntry = _MscApsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1)
)
mscApsOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-ApsMIB", "mscApsIndex"),
)
if mibBuilder.loadTexts:
    mscApsOperEntry.setStatus("mandatory")


class _MscApsNearEndRxActiveLine_Type(Integer32):
    """Custom type mscApsNearEndRxActiveLine based on Integer32"""
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


_MscApsNearEndRxActiveLine_Type.__name__ = "Integer32"
_MscApsNearEndRxActiveLine_Object = MibTableColumn
mscApsNearEndRxActiveLine = _MscApsNearEndRxActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 1),
    _MscApsNearEndRxActiveLine_Type()
)
mscApsNearEndRxActiveLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsNearEndRxActiveLine.setStatus("mandatory")


class _MscApsNearEndRequest_Type(Integer32):
    """Custom type mscApsNearEndRequest based on Integer32"""
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


_MscApsNearEndRequest_Type.__name__ = "Integer32"
_MscApsNearEndRequest_Object = MibTableColumn
mscApsNearEndRequest = _MscApsNearEndRequest_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 2),
    _MscApsNearEndRequest_Type()
)
mscApsNearEndRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsNearEndRequest.setStatus("mandatory")


class _MscApsNearEndRequestChannel_Type(Integer32):
    """Custom type mscApsNearEndRequestChannel based on Integer32"""
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


_MscApsNearEndRequestChannel_Type.__name__ = "Integer32"
_MscApsNearEndRequestChannel_Object = MibTableColumn
mscApsNearEndRequestChannel = _MscApsNearEndRequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 3),
    _MscApsNearEndRequestChannel_Type()
)
mscApsNearEndRequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsNearEndRequestChannel.setStatus("mandatory")


class _MscApsFarEndRequest_Type(Integer32):
    """Custom type mscApsFarEndRequest based on Integer32"""
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


_MscApsFarEndRequest_Type.__name__ = "Integer32"
_MscApsFarEndRequest_Object = MibTableColumn
mscApsFarEndRequest = _MscApsFarEndRequest_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 4),
    _MscApsFarEndRequest_Type()
)
mscApsFarEndRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsFarEndRequest.setStatus("mandatory")


class _MscApsFarEndRequestChannel_Type(Integer32):
    """Custom type mscApsFarEndRequestChannel based on Integer32"""
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


_MscApsFarEndRequestChannel_Type.__name__ = "Integer32"
_MscApsFarEndRequestChannel_Object = MibTableColumn
mscApsFarEndRequestChannel = _MscApsFarEndRequestChannel_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 5),
    _MscApsFarEndRequestChannel_Type()
)
mscApsFarEndRequestChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsFarEndRequestChannel.setStatus("mandatory")


class _MscApsSdOnLines_Type(OctetString):
    """Custom type mscApsSdOnLines based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscApsSdOnLines_Type.__name__ = "OctetString"
_MscApsSdOnLines_Object = MibTableColumn
mscApsSdOnLines = _MscApsSdOnLines_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 6),
    _MscApsSdOnLines_Type()
)
mscApsSdOnLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsSdOnLines.setStatus("mandatory")
_MscApsSwitchovers_Type = Counter32
_MscApsSwitchovers_Object = MibTableColumn
mscApsSwitchovers = _MscApsSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 7),
    _MscApsSwitchovers_Type()
)
mscApsSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsSwitchovers.setStatus("mandatory")


class _MscApsTimeUntilRestore_Type(Unsigned32):
    """Custom type mscApsTimeUntilRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_MscApsTimeUntilRestore_Type.__name__ = "Unsigned32"
_MscApsTimeUntilRestore_Object = MibTableColumn
mscApsTimeUntilRestore = _MscApsTimeUntilRestore_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 8),
    _MscApsTimeUntilRestore_Type()
)
mscApsTimeUntilRestore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsTimeUntilRestore.setStatus("mandatory")


class _MscApsProtocolFailureAlarm_Type(Integer32):
    """Custom type mscApsProtocolFailureAlarm based on Integer32"""
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


_MscApsProtocolFailureAlarm_Type.__name__ = "Integer32"
_MscApsProtocolFailureAlarm_Object = MibTableColumn
mscApsProtocolFailureAlarm = _MscApsProtocolFailureAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 9),
    _MscApsProtocolFailureAlarm_Type()
)
mscApsProtocolFailureAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsProtocolFailureAlarm.setStatus("mandatory")


class _MscApsModeMismatchAlarm_Type(Integer32):
    """Custom type mscApsModeMismatchAlarm based on Integer32"""
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


_MscApsModeMismatchAlarm_Type.__name__ = "Integer32"
_MscApsModeMismatchAlarm_Object = MibTableColumn
mscApsModeMismatchAlarm = _MscApsModeMismatchAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 134, 13, 1, 10),
    _MscApsModeMismatchAlarm_Type()
)
mscApsModeMismatchAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscApsModeMismatchAlarm.setStatus("mandatory")
_ApsMIB_ObjectIdentity = ObjectIdentity
apsMIB = _ApsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136)
)
_ApsGroup_ObjectIdentity = ObjectIdentity
apsGroup = _ApsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 1)
)
_ApsGroupCA_ObjectIdentity = ObjectIdentity
apsGroupCA = _ApsGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 1, 1)
)
_ApsGroupCA02_ObjectIdentity = ObjectIdentity
apsGroupCA02 = _ApsGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 1, 1, 3)
)
_ApsGroupCA02A_ObjectIdentity = ObjectIdentity
apsGroupCA02A = _ApsGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 1, 1, 3, 2)
)
_ApsCapabilities_ObjectIdentity = ObjectIdentity
apsCapabilities = _ApsCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 3)
)
_ApsCapabilitiesCA_ObjectIdentity = ObjectIdentity
apsCapabilitiesCA = _ApsCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 3, 1)
)
_ApsCapabilitiesCA02_ObjectIdentity = ObjectIdentity
apsCapabilitiesCA02 = _ApsCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 3, 1, 3)
)
_ApsCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
apsCapabilitiesCA02A = _ApsCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 136, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ApsMIB",
    **{"mscAps": mscAps,
       "mscApsRowStatusTable": mscApsRowStatusTable,
       "mscApsRowStatusEntry": mscApsRowStatusEntry,
       "mscApsRowStatus": mscApsRowStatus,
       "mscApsComponentName": mscApsComponentName,
       "mscApsStorageType": mscApsStorageType,
       "mscApsIndex": mscApsIndex,
       "mscApsTest": mscApsTest,
       "mscApsTestRowStatusTable": mscApsTestRowStatusTable,
       "mscApsTestRowStatusEntry": mscApsTestRowStatusEntry,
       "mscApsTestRowStatus": mscApsTestRowStatus,
       "mscApsTestComponentName": mscApsTestComponentName,
       "mscApsTestStorageType": mscApsTestStorageType,
       "mscApsTestIndex": mscApsTestIndex,
       "mscApsTestStateTable": mscApsTestStateTable,
       "mscApsTestStateEntry": mscApsTestStateEntry,
       "mscApsTestAdminState": mscApsTestAdminState,
       "mscApsTestOperationalState": mscApsTestOperationalState,
       "mscApsTestUsageState": mscApsTestUsageState,
       "mscApsTestSetupTable": mscApsTestSetupTable,
       "mscApsTestSetupEntry": mscApsTestSetupEntry,
       "mscApsTestPurpose": mscApsTestPurpose,
       "mscApsTestType": mscApsTestType,
       "mscApsTestFrmSize": mscApsTestFrmSize,
       "mscApsTestFrmPatternType": mscApsTestFrmPatternType,
       "mscApsTestCustomizedPattern": mscApsTestCustomizedPattern,
       "mscApsTestDataStartDelay": mscApsTestDataStartDelay,
       "mscApsTestDisplayInterval": mscApsTestDisplayInterval,
       "mscApsTestDuration": mscApsTestDuration,
       "mscApsTestResultsTable": mscApsTestResultsTable,
       "mscApsTestResultsEntry": mscApsTestResultsEntry,
       "mscApsTestElapsedTime": mscApsTestElapsedTime,
       "mscApsTestTimeRemaining": mscApsTestTimeRemaining,
       "mscApsTestCauseOfTermination": mscApsTestCauseOfTermination,
       "mscApsTestBitsTx": mscApsTestBitsTx,
       "mscApsTestBytesTx": mscApsTestBytesTx,
       "mscApsTestFrmTx": mscApsTestFrmTx,
       "mscApsTestBitsRx": mscApsTestBitsRx,
       "mscApsTestBytesRx": mscApsTestBytesRx,
       "mscApsTestFrmRx": mscApsTestFrmRx,
       "mscApsTestErroredFrmRx": mscApsTestErroredFrmRx,
       "mscApsTestBitErrorRate": mscApsTestBitErrorRate,
       "mscApsCidDataTable": mscApsCidDataTable,
       "mscApsCidDataEntry": mscApsCidDataEntry,
       "mscApsCustomerIdentifier": mscApsCustomerIdentifier,
       "mscApsProvTable": mscApsProvTable,
       "mscApsProvEntry": mscApsProvEntry,
       "mscApsApplicationFramerName": mscApsApplicationFramerName,
       "mscApsWorkingLine": mscApsWorkingLine,
       "mscApsProtectionLine": mscApsProtectionLine,
       "mscApsMode": mscApsMode,
       "mscApsRevertive": mscApsRevertive,
       "mscApsHoldOffTime": mscApsHoldOffTime,
       "mscApsWaitToRestorePeriod": mscApsWaitToRestorePeriod,
       "mscApsSignalDegradeRatio": mscApsSignalDegradeRatio,
       "mscApsStateTable": mscApsStateTable,
       "mscApsStateEntry": mscApsStateEntry,
       "mscApsAdminState": mscApsAdminState,
       "mscApsOperationalState": mscApsOperationalState,
       "mscApsUsageState": mscApsUsageState,
       "mscApsAvailabilityStatus": mscApsAvailabilityStatus,
       "mscApsProceduralStatus": mscApsProceduralStatus,
       "mscApsControlStatus": mscApsControlStatus,
       "mscApsAlarmStatus": mscApsAlarmStatus,
       "mscApsStandbyStatus": mscApsStandbyStatus,
       "mscApsUnknownStatus": mscApsUnknownStatus,
       "mscApsOperTable": mscApsOperTable,
       "mscApsOperEntry": mscApsOperEntry,
       "mscApsNearEndRxActiveLine": mscApsNearEndRxActiveLine,
       "mscApsNearEndRequest": mscApsNearEndRequest,
       "mscApsNearEndRequestChannel": mscApsNearEndRequestChannel,
       "mscApsFarEndRequest": mscApsFarEndRequest,
       "mscApsFarEndRequestChannel": mscApsFarEndRequestChannel,
       "mscApsSdOnLines": mscApsSdOnLines,
       "mscApsSwitchovers": mscApsSwitchovers,
       "mscApsTimeUntilRestore": mscApsTimeUntilRestore,
       "mscApsProtocolFailureAlarm": mscApsProtocolFailureAlarm,
       "mscApsModeMismatchAlarm": mscApsModeMismatchAlarm,
       "apsMIB": apsMIB,
       "apsGroup": apsGroup,
       "apsGroupCA": apsGroupCA,
       "apsGroupCA02": apsGroupCA02,
       "apsGroupCA02A": apsGroupCA02A,
       "apsCapabilities": apsCapabilities,
       "apsCapabilitiesCA": apsCapabilitiesCA,
       "apsCapabilitiesCA02": apsCapabilitiesCA02,
       "apsCapabilitiesCA02A": apsCapabilitiesCA02A}
)
