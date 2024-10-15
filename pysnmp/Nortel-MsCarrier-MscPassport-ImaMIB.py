# SNMP MIB module (Nortel-MsCarrier-MscPassport-ImaMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-ImaMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:37 2024
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

(mscLp,
 mscLpDS3,
 mscLpDS3Index,
 mscLpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB",
    "mscLp",
    "mscLpDS3",
    "mscLpDS3Index",
    "mscLpIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Hex,
 Link,
 NonReplicated,
 PassportCounter64) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "Hex",
    "Link",
    "NonReplicated",
    "PassportCounter64")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
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

_MscLpDS3Ima_ObjectIdentity = ObjectIdentity
mscLpDS3Ima = _MscLpDS3Ima_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7)
)
_MscLpDS3ImaRowStatusTable_Object = MibTable
mscLpDS3ImaRowStatusTable = _MscLpDS3ImaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 1)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaRowStatusTable.setStatus("mandatory")
_MscLpDS3ImaRowStatusEntry_Object = MibTableRow
mscLpDS3ImaRowStatusEntry = _MscLpDS3ImaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 1, 1)
)
mscLpDS3ImaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaRowStatusEntry.setStatus("mandatory")
_MscLpDS3ImaRowStatus_Type = RowStatus
_MscLpDS3ImaRowStatus_Object = MibTableColumn
mscLpDS3ImaRowStatus = _MscLpDS3ImaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 1, 1, 1),
    _MscLpDS3ImaRowStatus_Type()
)
mscLpDS3ImaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaRowStatus.setStatus("mandatory")
_MscLpDS3ImaComponentName_Type = DisplayString
_MscLpDS3ImaComponentName_Object = MibTableColumn
mscLpDS3ImaComponentName = _MscLpDS3ImaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 1, 1, 2),
    _MscLpDS3ImaComponentName_Type()
)
mscLpDS3ImaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaComponentName.setStatus("mandatory")
_MscLpDS3ImaStorageType_Type = StorageType
_MscLpDS3ImaStorageType_Object = MibTableColumn
mscLpDS3ImaStorageType = _MscLpDS3ImaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 1, 1, 4),
    _MscLpDS3ImaStorageType_Type()
)
mscLpDS3ImaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaStorageType.setStatus("mandatory")


class _MscLpDS3ImaIndex_Type(Integer32):
    """Custom type mscLpDS3ImaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_MscLpDS3ImaIndex_Type.__name__ = "Integer32"
_MscLpDS3ImaIndex_Object = MibTableColumn
mscLpDS3ImaIndex = _MscLpDS3ImaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 1, 1, 10),
    _MscLpDS3ImaIndex_Type()
)
mscLpDS3ImaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpDS3ImaIndex.setStatus("mandatory")
_MscLpDS3ImaTest_ObjectIdentity = ObjectIdentity
mscLpDS3ImaTest = _MscLpDS3ImaTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2)
)
_MscLpDS3ImaTestRowStatusTable_Object = MibTable
mscLpDS3ImaTestRowStatusTable = _MscLpDS3ImaTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestRowStatusTable.setStatus("mandatory")
_MscLpDS3ImaTestRowStatusEntry_Object = MibTableRow
mscLpDS3ImaTestRowStatusEntry = _MscLpDS3ImaTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 1, 1)
)
mscLpDS3ImaTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestRowStatusEntry.setStatus("mandatory")
_MscLpDS3ImaTestRowStatus_Type = RowStatus
_MscLpDS3ImaTestRowStatus_Object = MibTableColumn
mscLpDS3ImaTestRowStatus = _MscLpDS3ImaTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 1, 1, 1),
    _MscLpDS3ImaTestRowStatus_Type()
)
mscLpDS3ImaTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestRowStatus.setStatus("mandatory")
_MscLpDS3ImaTestComponentName_Type = DisplayString
_MscLpDS3ImaTestComponentName_Object = MibTableColumn
mscLpDS3ImaTestComponentName = _MscLpDS3ImaTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 1, 1, 2),
    _MscLpDS3ImaTestComponentName_Type()
)
mscLpDS3ImaTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestComponentName.setStatus("mandatory")
_MscLpDS3ImaTestStorageType_Type = StorageType
_MscLpDS3ImaTestStorageType_Object = MibTableColumn
mscLpDS3ImaTestStorageType = _MscLpDS3ImaTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 1, 1, 4),
    _MscLpDS3ImaTestStorageType_Type()
)
mscLpDS3ImaTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestStorageType.setStatus("mandatory")
_MscLpDS3ImaTestIndex_Type = NonReplicated
_MscLpDS3ImaTestIndex_Object = MibTableColumn
mscLpDS3ImaTestIndex = _MscLpDS3ImaTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 1, 1, 10),
    _MscLpDS3ImaTestIndex_Type()
)
mscLpDS3ImaTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestIndex.setStatus("mandatory")
_MscLpDS3ImaTestStateTable_Object = MibTable
mscLpDS3ImaTestStateTable = _MscLpDS3ImaTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestStateTable.setStatus("mandatory")
_MscLpDS3ImaTestStateEntry_Object = MibTableRow
mscLpDS3ImaTestStateEntry = _MscLpDS3ImaTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 10, 1)
)
mscLpDS3ImaTestStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestStateEntry.setStatus("mandatory")


class _MscLpDS3ImaTestAdminState_Type(Integer32):
    """Custom type mscLpDS3ImaTestAdminState based on Integer32"""
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


_MscLpDS3ImaTestAdminState_Type.__name__ = "Integer32"
_MscLpDS3ImaTestAdminState_Object = MibTableColumn
mscLpDS3ImaTestAdminState = _MscLpDS3ImaTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 10, 1, 1),
    _MscLpDS3ImaTestAdminState_Type()
)
mscLpDS3ImaTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestAdminState.setStatus("mandatory")


class _MscLpDS3ImaTestOperationalState_Type(Integer32):
    """Custom type mscLpDS3ImaTestOperationalState based on Integer32"""
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


_MscLpDS3ImaTestOperationalState_Type.__name__ = "Integer32"
_MscLpDS3ImaTestOperationalState_Object = MibTableColumn
mscLpDS3ImaTestOperationalState = _MscLpDS3ImaTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 10, 1, 2),
    _MscLpDS3ImaTestOperationalState_Type()
)
mscLpDS3ImaTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestOperationalState.setStatus("mandatory")


class _MscLpDS3ImaTestUsageState_Type(Integer32):
    """Custom type mscLpDS3ImaTestUsageState based on Integer32"""
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


_MscLpDS3ImaTestUsageState_Type.__name__ = "Integer32"
_MscLpDS3ImaTestUsageState_Object = MibTableColumn
mscLpDS3ImaTestUsageState = _MscLpDS3ImaTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 10, 1, 3),
    _MscLpDS3ImaTestUsageState_Type()
)
mscLpDS3ImaTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestUsageState.setStatus("mandatory")
_MscLpDS3ImaTestSetupTable_Object = MibTable
mscLpDS3ImaTestSetupTable = _MscLpDS3ImaTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestSetupTable.setStatus("mandatory")
_MscLpDS3ImaTestSetupEntry_Object = MibTableRow
mscLpDS3ImaTestSetupEntry = _MscLpDS3ImaTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1)
)
mscLpDS3ImaTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestSetupEntry.setStatus("mandatory")


class _MscLpDS3ImaTestPurpose_Type(AsciiString):
    """Custom type mscLpDS3ImaTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscLpDS3ImaTestPurpose_Type.__name__ = "AsciiString"
_MscLpDS3ImaTestPurpose_Object = MibTableColumn
mscLpDS3ImaTestPurpose = _MscLpDS3ImaTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 1),
    _MscLpDS3ImaTestPurpose_Type()
)
mscLpDS3ImaTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestPurpose.setStatus("mandatory")


class _MscLpDS3ImaTestType_Type(Integer32):
    """Custom type mscLpDS3ImaTestType based on Integer32"""
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


_MscLpDS3ImaTestType_Type.__name__ = "Integer32"
_MscLpDS3ImaTestType_Object = MibTableColumn
mscLpDS3ImaTestType = _MscLpDS3ImaTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 2),
    _MscLpDS3ImaTestType_Type()
)
mscLpDS3ImaTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestType.setStatus("mandatory")


class _MscLpDS3ImaTestFrmSize_Type(Unsigned32):
    """Custom type mscLpDS3ImaTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscLpDS3ImaTestFrmSize_Type.__name__ = "Unsigned32"
_MscLpDS3ImaTestFrmSize_Object = MibTableColumn
mscLpDS3ImaTestFrmSize = _MscLpDS3ImaTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 3),
    _MscLpDS3ImaTestFrmSize_Type()
)
mscLpDS3ImaTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestFrmSize.setStatus("mandatory")


class _MscLpDS3ImaTestFrmPatternType_Type(Integer32):
    """Custom type mscLpDS3ImaTestFrmPatternType based on Integer32"""
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


_MscLpDS3ImaTestFrmPatternType_Type.__name__ = "Integer32"
_MscLpDS3ImaTestFrmPatternType_Object = MibTableColumn
mscLpDS3ImaTestFrmPatternType = _MscLpDS3ImaTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 4),
    _MscLpDS3ImaTestFrmPatternType_Type()
)
mscLpDS3ImaTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestFrmPatternType.setStatus("mandatory")


class _MscLpDS3ImaTestCustomizedPattern_Type(Hex):
    """Custom type mscLpDS3ImaTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaTestCustomizedPattern_Type.__name__ = "Hex"
_MscLpDS3ImaTestCustomizedPattern_Object = MibTableColumn
mscLpDS3ImaTestCustomizedPattern = _MscLpDS3ImaTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 5),
    _MscLpDS3ImaTestCustomizedPattern_Type()
)
mscLpDS3ImaTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestCustomizedPattern.setStatus("mandatory")


class _MscLpDS3ImaTestDataStartDelay_Type(Unsigned32):
    """Custom type mscLpDS3ImaTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_MscLpDS3ImaTestDataStartDelay_Type.__name__ = "Unsigned32"
_MscLpDS3ImaTestDataStartDelay_Object = MibTableColumn
mscLpDS3ImaTestDataStartDelay = _MscLpDS3ImaTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 6),
    _MscLpDS3ImaTestDataStartDelay_Type()
)
mscLpDS3ImaTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestDataStartDelay.setStatus("mandatory")


class _MscLpDS3ImaTestDisplayInterval_Type(Unsigned32):
    """Custom type mscLpDS3ImaTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_MscLpDS3ImaTestDisplayInterval_Type.__name__ = "Unsigned32"
_MscLpDS3ImaTestDisplayInterval_Object = MibTableColumn
mscLpDS3ImaTestDisplayInterval = _MscLpDS3ImaTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 7),
    _MscLpDS3ImaTestDisplayInterval_Type()
)
mscLpDS3ImaTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestDisplayInterval.setStatus("mandatory")


class _MscLpDS3ImaTestDuration_Type(Unsigned32):
    """Custom type mscLpDS3ImaTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscLpDS3ImaTestDuration_Type.__name__ = "Unsigned32"
_MscLpDS3ImaTestDuration_Object = MibTableColumn
mscLpDS3ImaTestDuration = _MscLpDS3ImaTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 11, 1, 8),
    _MscLpDS3ImaTestDuration_Type()
)
mscLpDS3ImaTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestDuration.setStatus("mandatory")
_MscLpDS3ImaTestResultsTable_Object = MibTable
mscLpDS3ImaTestResultsTable = _MscLpDS3ImaTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestResultsTable.setStatus("mandatory")
_MscLpDS3ImaTestResultsEntry_Object = MibTableRow
mscLpDS3ImaTestResultsEntry = _MscLpDS3ImaTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1)
)
mscLpDS3ImaTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaTestResultsEntry.setStatus("mandatory")
_MscLpDS3ImaTestElapsedTime_Type = Counter32
_MscLpDS3ImaTestElapsedTime_Object = MibTableColumn
mscLpDS3ImaTestElapsedTime = _MscLpDS3ImaTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 1),
    _MscLpDS3ImaTestElapsedTime_Type()
)
mscLpDS3ImaTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestElapsedTime.setStatus("mandatory")


class _MscLpDS3ImaTestTimeRemaining_Type(Unsigned32):
    """Custom type mscLpDS3ImaTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscLpDS3ImaTestTimeRemaining_Object = MibTableColumn
mscLpDS3ImaTestTimeRemaining = _MscLpDS3ImaTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 2),
    _MscLpDS3ImaTestTimeRemaining_Type()
)
mscLpDS3ImaTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestTimeRemaining.setStatus("mandatory")


class _MscLpDS3ImaTestCauseOfTermination_Type(Integer32):
    """Custom type mscLpDS3ImaTestCauseOfTermination based on Integer32"""
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


_MscLpDS3ImaTestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpDS3ImaTestCauseOfTermination_Object = MibTableColumn
mscLpDS3ImaTestCauseOfTermination = _MscLpDS3ImaTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 3),
    _MscLpDS3ImaTestCauseOfTermination_Type()
)
mscLpDS3ImaTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestCauseOfTermination.setStatus("mandatory")
_MscLpDS3ImaTestBitsTx_Type = PassportCounter64
_MscLpDS3ImaTestBitsTx_Object = MibTableColumn
mscLpDS3ImaTestBitsTx = _MscLpDS3ImaTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 4),
    _MscLpDS3ImaTestBitsTx_Type()
)
mscLpDS3ImaTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestBitsTx.setStatus("mandatory")
_MscLpDS3ImaTestBytesTx_Type = PassportCounter64
_MscLpDS3ImaTestBytesTx_Object = MibTableColumn
mscLpDS3ImaTestBytesTx = _MscLpDS3ImaTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 5),
    _MscLpDS3ImaTestBytesTx_Type()
)
mscLpDS3ImaTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestBytesTx.setStatus("mandatory")
_MscLpDS3ImaTestFrmTx_Type = PassportCounter64
_MscLpDS3ImaTestFrmTx_Object = MibTableColumn
mscLpDS3ImaTestFrmTx = _MscLpDS3ImaTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 6),
    _MscLpDS3ImaTestFrmTx_Type()
)
mscLpDS3ImaTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestFrmTx.setStatus("mandatory")
_MscLpDS3ImaTestBitsRx_Type = PassportCounter64
_MscLpDS3ImaTestBitsRx_Object = MibTableColumn
mscLpDS3ImaTestBitsRx = _MscLpDS3ImaTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 7),
    _MscLpDS3ImaTestBitsRx_Type()
)
mscLpDS3ImaTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestBitsRx.setStatus("mandatory")
_MscLpDS3ImaTestBytesRx_Type = PassportCounter64
_MscLpDS3ImaTestBytesRx_Object = MibTableColumn
mscLpDS3ImaTestBytesRx = _MscLpDS3ImaTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 8),
    _MscLpDS3ImaTestBytesRx_Type()
)
mscLpDS3ImaTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestBytesRx.setStatus("mandatory")
_MscLpDS3ImaTestFrmRx_Type = PassportCounter64
_MscLpDS3ImaTestFrmRx_Object = MibTableColumn
mscLpDS3ImaTestFrmRx = _MscLpDS3ImaTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 9),
    _MscLpDS3ImaTestFrmRx_Type()
)
mscLpDS3ImaTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestFrmRx.setStatus("mandatory")
_MscLpDS3ImaTestErroredFrmRx_Type = PassportCounter64
_MscLpDS3ImaTestErroredFrmRx_Object = MibTableColumn
mscLpDS3ImaTestErroredFrmRx = _MscLpDS3ImaTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 10),
    _MscLpDS3ImaTestErroredFrmRx_Type()
)
mscLpDS3ImaTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestErroredFrmRx.setStatus("mandatory")


class _MscLpDS3ImaTestBitErrorRate_Type(AsciiString):
    """Custom type mscLpDS3ImaTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_MscLpDS3ImaTestBitErrorRate_Type.__name__ = "AsciiString"
_MscLpDS3ImaTestBitErrorRate_Object = MibTableColumn
mscLpDS3ImaTestBitErrorRate = _MscLpDS3ImaTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 2, 12, 1, 11),
    _MscLpDS3ImaTestBitErrorRate_Type()
)
mscLpDS3ImaTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTestBitErrorRate.setStatus("mandatory")
_MscLpDS3ImaLk_ObjectIdentity = ObjectIdentity
mscLpDS3ImaLk = _MscLpDS3ImaLk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3)
)
_MscLpDS3ImaLkRowStatusTable_Object = MibTable
mscLpDS3ImaLkRowStatusTable = _MscLpDS3ImaLkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRowStatusTable.setStatus("mandatory")
_MscLpDS3ImaLkRowStatusEntry_Object = MibTableRow
mscLpDS3ImaLkRowStatusEntry = _MscLpDS3ImaLkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 1, 1)
)
mscLpDS3ImaLkRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRowStatusEntry.setStatus("mandatory")
_MscLpDS3ImaLkRowStatus_Type = RowStatus
_MscLpDS3ImaLkRowStatus_Object = MibTableColumn
mscLpDS3ImaLkRowStatus = _MscLpDS3ImaLkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 1, 1, 1),
    _MscLpDS3ImaLkRowStatus_Type()
)
mscLpDS3ImaLkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRowStatus.setStatus("mandatory")
_MscLpDS3ImaLkComponentName_Type = DisplayString
_MscLpDS3ImaLkComponentName_Object = MibTableColumn
mscLpDS3ImaLkComponentName = _MscLpDS3ImaLkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 1, 1, 2),
    _MscLpDS3ImaLkComponentName_Type()
)
mscLpDS3ImaLkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkComponentName.setStatus("mandatory")
_MscLpDS3ImaLkStorageType_Type = StorageType
_MscLpDS3ImaLkStorageType_Object = MibTableColumn
mscLpDS3ImaLkStorageType = _MscLpDS3ImaLkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 1, 1, 4),
    _MscLpDS3ImaLkStorageType_Type()
)
mscLpDS3ImaLkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkStorageType.setStatus("mandatory")


class _MscLpDS3ImaLkIndex_Type(Integer32):
    """Custom type mscLpDS3ImaLkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MscLpDS3ImaLkIndex_Type.__name__ = "Integer32"
_MscLpDS3ImaLkIndex_Object = MibTableColumn
mscLpDS3ImaLkIndex = _MscLpDS3ImaLkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 1, 1, 10),
    _MscLpDS3ImaLkIndex_Type()
)
mscLpDS3ImaLkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkIndex.setStatus("mandatory")
_MscLpDS3ImaLkProvTable_Object = MibTable
mscLpDS3ImaLkProvTable = _MscLpDS3ImaLkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkProvTable.setStatus("mandatory")
_MscLpDS3ImaLkProvEntry_Object = MibTableRow
mscLpDS3ImaLkProvEntry = _MscLpDS3ImaLkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 10, 1)
)
mscLpDS3ImaLkProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkProvEntry.setStatus("mandatory")
_MscLpDS3ImaLkInterfaceName_Type = Link
_MscLpDS3ImaLkInterfaceName_Object = MibTableColumn
mscLpDS3ImaLkInterfaceName = _MscLpDS3ImaLkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 10, 1, 1),
    _MscLpDS3ImaLkInterfaceName_Type()
)
mscLpDS3ImaLkInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkInterfaceName.setStatus("mandatory")
_MscLpDS3ImaLkOperTable_Object = MibTable
mscLpDS3ImaLkOperTable = _MscLpDS3ImaLkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 11)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkOperTable.setStatus("mandatory")
_MscLpDS3ImaLkOperEntry_Object = MibTableRow
mscLpDS3ImaLkOperEntry = _MscLpDS3ImaLkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 11, 1)
)
mscLpDS3ImaLkOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkOperEntry.setStatus("mandatory")


class _MscLpDS3ImaLkFailureCause_Type(Integer32):
    """Custom type mscLpDS3ImaLkFailureCause based on Integer32"""
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


_MscLpDS3ImaLkFailureCause_Type.__name__ = "Integer32"
_MscLpDS3ImaLkFailureCause_Object = MibTableColumn
mscLpDS3ImaLkFailureCause = _MscLpDS3ImaLkFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 11, 1, 1),
    _MscLpDS3ImaLkFailureCause_Type()
)
mscLpDS3ImaLkFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkFailureCause.setStatus("mandatory")


class _MscLpDS3ImaLkRemoteDefect_Type(Integer32):
    """Custom type mscLpDS3ImaLkRemoteDefect based on Integer32"""
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


_MscLpDS3ImaLkRemoteDefect_Type.__name__ = "Integer32"
_MscLpDS3ImaLkRemoteDefect_Object = MibTableColumn
mscLpDS3ImaLkRemoteDefect = _MscLpDS3ImaLkRemoteDefect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 11, 1, 2),
    _MscLpDS3ImaLkRemoteDefect_Type()
)
mscLpDS3ImaLkRemoteDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRemoteDefect.setStatus("mandatory")


class _MscLpDS3ImaLkRemoteLid_Type(Unsigned32):
    """Custom type mscLpDS3ImaLkRemoteLid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MscLpDS3ImaLkRemoteLid_Type.__name__ = "Unsigned32"
_MscLpDS3ImaLkRemoteLid_Object = MibTableColumn
mscLpDS3ImaLkRemoteLid = _MscLpDS3ImaLkRemoteLid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 11, 1, 3),
    _MscLpDS3ImaLkRemoteLid_Type()
)
mscLpDS3ImaLkRemoteLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRemoteLid.setStatus("mandatory")


class _MscLpDS3ImaLkRelativeDelay_Type(Unsigned32):
    """Custom type mscLpDS3ImaLkRelativeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaLkRelativeDelay_Type.__name__ = "Unsigned32"
_MscLpDS3ImaLkRelativeDelay_Object = MibTableColumn
mscLpDS3ImaLkRelativeDelay = _MscLpDS3ImaLkRelativeDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 11, 1, 4),
    _MscLpDS3ImaLkRelativeDelay_Type()
)
mscLpDS3ImaLkRelativeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRelativeDelay.setStatus("mandatory")


class _MscLpDS3ImaLkLastOifCause_Type(Integer32):
    """Custom type mscLpDS3ImaLkLastOifCause based on Integer32"""
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


_MscLpDS3ImaLkLastOifCause_Type.__name__ = "Integer32"
_MscLpDS3ImaLkLastOifCause_Object = MibTableColumn
mscLpDS3ImaLkLastOifCause = _MscLpDS3ImaLkLastOifCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 11, 1, 5),
    _MscLpDS3ImaLkLastOifCause_Type()
)
mscLpDS3ImaLkLastOifCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkLastOifCause.setStatus("mandatory")
_MscLpDS3ImaLkStatsTable_Object = MibTable
mscLpDS3ImaLkStatsTable = _MscLpDS3ImaLkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkStatsTable.setStatus("mandatory")
_MscLpDS3ImaLkStatsEntry_Object = MibTableRow
mscLpDS3ImaLkStatsEntry = _MscLpDS3ImaLkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1)
)
mscLpDS3ImaLkStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkStatsEntry.setStatus("mandatory")


class _MscLpDS3ImaLkRunningTime_Type(Unsigned32):
    """Custom type mscLpDS3ImaLkRunningTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaLkRunningTime_Type.__name__ = "Unsigned32"
_MscLpDS3ImaLkRunningTime_Object = MibTableColumn
mscLpDS3ImaLkRunningTime = _MscLpDS3ImaLkRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 1),
    _MscLpDS3ImaLkRunningTime_Type()
)
mscLpDS3ImaLkRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRunningTime.setStatus("mandatory")


class _MscLpDS3ImaLkUnavailSecs_Type(Unsigned32):
    """Custom type mscLpDS3ImaLkUnavailSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaLkUnavailSecs_Type.__name__ = "Unsigned32"
_MscLpDS3ImaLkUnavailSecs_Object = MibTableColumn
mscLpDS3ImaLkUnavailSecs = _MscLpDS3ImaLkUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 2),
    _MscLpDS3ImaLkUnavailSecs_Type()
)
mscLpDS3ImaLkUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkUnavailSecs.setStatus("mandatory")


class _MscLpDS3ImaLkFailures_Type(Unsigned32):
    """Custom type mscLpDS3ImaLkFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaLkFailures_Type.__name__ = "Unsigned32"
_MscLpDS3ImaLkFailures_Object = MibTableColumn
mscLpDS3ImaLkFailures = _MscLpDS3ImaLkFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 3),
    _MscLpDS3ImaLkFailures_Type()
)
mscLpDS3ImaLkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkFailures.setStatus("mandatory")
_MscLpDS3ImaLkUnusableSec_Type = Counter32
_MscLpDS3ImaLkUnusableSec_Object = MibTableColumn
mscLpDS3ImaLkUnusableSec = _MscLpDS3ImaLkUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 4),
    _MscLpDS3ImaLkUnusableSec_Type()
)
mscLpDS3ImaLkUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkUnusableSec.setStatus("mandatory")
_MscLpDS3ImaLkSevErroredSec_Type = Counter32
_MscLpDS3ImaLkSevErroredSec_Object = MibTableColumn
mscLpDS3ImaLkSevErroredSec = _MscLpDS3ImaLkSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 5),
    _MscLpDS3ImaLkSevErroredSec_Type()
)
mscLpDS3ImaLkSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkSevErroredSec.setStatus("mandatory")
_MscLpDS3ImaLkFarEndUnusableSec_Type = Counter32
_MscLpDS3ImaLkFarEndUnusableSec_Object = MibTableColumn
mscLpDS3ImaLkFarEndUnusableSec = _MscLpDS3ImaLkFarEndUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 6),
    _MscLpDS3ImaLkFarEndUnusableSec_Type()
)
mscLpDS3ImaLkFarEndUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkFarEndUnusableSec.setStatus("mandatory")
_MscLpDS3ImaLkFarEndSevErroredSec_Type = Counter32
_MscLpDS3ImaLkFarEndSevErroredSec_Object = MibTableColumn
mscLpDS3ImaLkFarEndSevErroredSec = _MscLpDS3ImaLkFarEndSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 7),
    _MscLpDS3ImaLkFarEndSevErroredSec_Type()
)
mscLpDS3ImaLkFarEndSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkFarEndSevErroredSec.setStatus("mandatory")
_MscLpDS3ImaLkFarEndUnavailSec_Type = Counter32
_MscLpDS3ImaLkFarEndUnavailSec_Object = MibTableColumn
mscLpDS3ImaLkFarEndUnavailSec = _MscLpDS3ImaLkFarEndUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 8),
    _MscLpDS3ImaLkFarEndUnavailSec_Type()
)
mscLpDS3ImaLkFarEndUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkFarEndUnavailSec.setStatus("mandatory")
_MscLpDS3ImaLkIcpViolations_Type = Counter32
_MscLpDS3ImaLkIcpViolations_Object = MibTableColumn
mscLpDS3ImaLkIcpViolations = _MscLpDS3ImaLkIcpViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 9),
    _MscLpDS3ImaLkIcpViolations_Type()
)
mscLpDS3ImaLkIcpViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkIcpViolations.setStatus("mandatory")
_MscLpDS3ImaLkTxStuffEvents_Type = Counter32
_MscLpDS3ImaLkTxStuffEvents_Object = MibTableColumn
mscLpDS3ImaLkTxStuffEvents = _MscLpDS3ImaLkTxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 10),
    _MscLpDS3ImaLkTxStuffEvents_Type()
)
mscLpDS3ImaLkTxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkTxStuffEvents.setStatus("mandatory")
_MscLpDS3ImaLkRxStuffEvents_Type = Counter32
_MscLpDS3ImaLkRxStuffEvents_Object = MibTableColumn
mscLpDS3ImaLkRxStuffEvents = _MscLpDS3ImaLkRxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 11),
    _MscLpDS3ImaLkRxStuffEvents_Type()
)
mscLpDS3ImaLkRxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkRxStuffEvents.setStatus("mandatory")
_MscLpDS3ImaLkIdleCellSec_Type = Counter32
_MscLpDS3ImaLkIdleCellSec_Object = MibTableColumn
mscLpDS3ImaLkIdleCellSec = _MscLpDS3ImaLkIdleCellSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 12, 1, 12),
    _MscLpDS3ImaLkIdleCellSec_Type()
)
mscLpDS3ImaLkIdleCellSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkIdleCellSec.setStatus("mandatory")
_MscLpDS3ImaLkStateTable_Object = MibTable
mscLpDS3ImaLkStateTable = _MscLpDS3ImaLkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkStateTable.setStatus("mandatory")
_MscLpDS3ImaLkStateEntry_Object = MibTableRow
mscLpDS3ImaLkStateEntry = _MscLpDS3ImaLkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1)
)
mscLpDS3ImaLkStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaLkStateEntry.setStatus("mandatory")


class _MscLpDS3ImaLkAdminState_Type(Integer32):
    """Custom type mscLpDS3ImaLkAdminState based on Integer32"""
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


_MscLpDS3ImaLkAdminState_Type.__name__ = "Integer32"
_MscLpDS3ImaLkAdminState_Object = MibTableColumn
mscLpDS3ImaLkAdminState = _MscLpDS3ImaLkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 1),
    _MscLpDS3ImaLkAdminState_Type()
)
mscLpDS3ImaLkAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkAdminState.setStatus("mandatory")


class _MscLpDS3ImaLkOperationalState_Type(Integer32):
    """Custom type mscLpDS3ImaLkOperationalState based on Integer32"""
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


_MscLpDS3ImaLkOperationalState_Type.__name__ = "Integer32"
_MscLpDS3ImaLkOperationalState_Object = MibTableColumn
mscLpDS3ImaLkOperationalState = _MscLpDS3ImaLkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 2),
    _MscLpDS3ImaLkOperationalState_Type()
)
mscLpDS3ImaLkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkOperationalState.setStatus("mandatory")


class _MscLpDS3ImaLkUsageState_Type(Integer32):
    """Custom type mscLpDS3ImaLkUsageState based on Integer32"""
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


_MscLpDS3ImaLkUsageState_Type.__name__ = "Integer32"
_MscLpDS3ImaLkUsageState_Object = MibTableColumn
mscLpDS3ImaLkUsageState = _MscLpDS3ImaLkUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 3),
    _MscLpDS3ImaLkUsageState_Type()
)
mscLpDS3ImaLkUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkUsageState.setStatus("mandatory")


class _MscLpDS3ImaLkAvailabilityStatus_Type(OctetString):
    """Custom type mscLpDS3ImaLkAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpDS3ImaLkAvailabilityStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaLkAvailabilityStatus_Object = MibTableColumn
mscLpDS3ImaLkAvailabilityStatus = _MscLpDS3ImaLkAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 4),
    _MscLpDS3ImaLkAvailabilityStatus_Type()
)
mscLpDS3ImaLkAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkAvailabilityStatus.setStatus("mandatory")


class _MscLpDS3ImaLkProceduralStatus_Type(OctetString):
    """Custom type mscLpDS3ImaLkProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpDS3ImaLkProceduralStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaLkProceduralStatus_Object = MibTableColumn
mscLpDS3ImaLkProceduralStatus = _MscLpDS3ImaLkProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 5),
    _MscLpDS3ImaLkProceduralStatus_Type()
)
mscLpDS3ImaLkProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkProceduralStatus.setStatus("mandatory")


class _MscLpDS3ImaLkControlStatus_Type(OctetString):
    """Custom type mscLpDS3ImaLkControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpDS3ImaLkControlStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaLkControlStatus_Object = MibTableColumn
mscLpDS3ImaLkControlStatus = _MscLpDS3ImaLkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 6),
    _MscLpDS3ImaLkControlStatus_Type()
)
mscLpDS3ImaLkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkControlStatus.setStatus("mandatory")


class _MscLpDS3ImaLkAlarmStatus_Type(OctetString):
    """Custom type mscLpDS3ImaLkAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpDS3ImaLkAlarmStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaLkAlarmStatus_Object = MibTableColumn
mscLpDS3ImaLkAlarmStatus = _MscLpDS3ImaLkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 7),
    _MscLpDS3ImaLkAlarmStatus_Type()
)
mscLpDS3ImaLkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkAlarmStatus.setStatus("mandatory")


class _MscLpDS3ImaLkStandbyStatus_Type(Integer32):
    """Custom type mscLpDS3ImaLkStandbyStatus based on Integer32"""
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


_MscLpDS3ImaLkStandbyStatus_Type.__name__ = "Integer32"
_MscLpDS3ImaLkStandbyStatus_Object = MibTableColumn
mscLpDS3ImaLkStandbyStatus = _MscLpDS3ImaLkStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 8),
    _MscLpDS3ImaLkStandbyStatus_Type()
)
mscLpDS3ImaLkStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkStandbyStatus.setStatus("mandatory")


class _MscLpDS3ImaLkUnknownStatus_Type(Integer32):
    """Custom type mscLpDS3ImaLkUnknownStatus based on Integer32"""
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


_MscLpDS3ImaLkUnknownStatus_Type.__name__ = "Integer32"
_MscLpDS3ImaLkUnknownStatus_Object = MibTableColumn
mscLpDS3ImaLkUnknownStatus = _MscLpDS3ImaLkUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 3, 13, 1, 9),
    _MscLpDS3ImaLkUnknownStatus_Type()
)
mscLpDS3ImaLkUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaLkUnknownStatus.setStatus("mandatory")
_MscLpDS3ImaProvTable_Object = MibTable
mscLpDS3ImaProvTable = _MscLpDS3ImaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaProvTable.setStatus("mandatory")
_MscLpDS3ImaProvEntry_Object = MibTableRow
mscLpDS3ImaProvEntry = _MscLpDS3ImaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10, 1)
)
mscLpDS3ImaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaProvEntry.setStatus("mandatory")


class _MscLpDS3ImaLinkSelectionCriterion_Type(Integer32):
    """Custom type mscLpDS3ImaLinkSelectionCriterion based on Integer32"""
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


_MscLpDS3ImaLinkSelectionCriterion_Type.__name__ = "Integer32"
_MscLpDS3ImaLinkSelectionCriterion_Object = MibTableColumn
mscLpDS3ImaLinkSelectionCriterion = _MscLpDS3ImaLinkSelectionCriterion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10, 1, 1),
    _MscLpDS3ImaLinkSelectionCriterion_Type()
)
mscLpDS3ImaLinkSelectionCriterion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaLinkSelectionCriterion.setStatus("mandatory")


class _MscLpDS3ImaMaxDiffDelay_Type(Unsigned32):
    """Custom type mscLpDS3ImaMaxDiffDelay based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscLpDS3ImaMaxDiffDelay_Type.__name__ = "Unsigned32"
_MscLpDS3ImaMaxDiffDelay_Object = MibTableColumn
mscLpDS3ImaMaxDiffDelay = _MscLpDS3ImaMaxDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10, 1, 2),
    _MscLpDS3ImaMaxDiffDelay_Type()
)
mscLpDS3ImaMaxDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaMaxDiffDelay.setStatus("mandatory")


class _MscLpDS3ImaLinkRetryTimeout_Type(Unsigned32):
    """Custom type mscLpDS3ImaLinkRetryTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscLpDS3ImaLinkRetryTimeout_Type.__name__ = "Unsigned32"
_MscLpDS3ImaLinkRetryTimeout_Object = MibTableColumn
mscLpDS3ImaLinkRetryTimeout = _MscLpDS3ImaLinkRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10, 1, 3),
    _MscLpDS3ImaLinkRetryTimeout_Type()
)
mscLpDS3ImaLinkRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaLinkRetryTimeout.setStatus("mandatory")
_MscLpDS3ImaApplicationFramerName_Type = Link
_MscLpDS3ImaApplicationFramerName_Object = MibTableColumn
mscLpDS3ImaApplicationFramerName = _MscLpDS3ImaApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10, 1, 4),
    _MscLpDS3ImaApplicationFramerName_Type()
)
mscLpDS3ImaApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaApplicationFramerName.setStatus("mandatory")


class _MscLpDS3ImaTransmitClockMode_Type(Integer32):
    """Custom type mscLpDS3ImaTransmitClockMode based on Integer32"""
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


_MscLpDS3ImaTransmitClockMode_Type.__name__ = "Integer32"
_MscLpDS3ImaTransmitClockMode_Object = MibTableColumn
mscLpDS3ImaTransmitClockMode = _MscLpDS3ImaTransmitClockMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10, 1, 5),
    _MscLpDS3ImaTransmitClockMode_Type()
)
mscLpDS3ImaTransmitClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaTransmitClockMode.setStatus("mandatory")


class _MscLpDS3ImaProtocol_Type(Integer32):
    """Custom type mscLpDS3ImaProtocol based on Integer32"""
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


_MscLpDS3ImaProtocol_Type.__name__ = "Integer32"
_MscLpDS3ImaProtocol_Object = MibTableColumn
mscLpDS3ImaProtocol = _MscLpDS3ImaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 10, 1, 6),
    _MscLpDS3ImaProtocol_Type()
)
mscLpDS3ImaProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaProtocol.setStatus("mandatory")
_MscLpDS3ImaOperTable_Object = MibTable
mscLpDS3ImaOperTable = _MscLpDS3ImaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaOperTable.setStatus("mandatory")
_MscLpDS3ImaOperEntry_Object = MibTableRow
mscLpDS3ImaOperEntry = _MscLpDS3ImaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1)
)
mscLpDS3ImaOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaOperEntry.setStatus("mandatory")


class _MscLpDS3ImaFailureCause_Type(Integer32):
    """Custom type mscLpDS3ImaFailureCause based on Integer32"""
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


_MscLpDS3ImaFailureCause_Type.__name__ = "Integer32"
_MscLpDS3ImaFailureCause_Object = MibTableColumn
mscLpDS3ImaFailureCause = _MscLpDS3ImaFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1, 1),
    _MscLpDS3ImaFailureCause_Type()
)
mscLpDS3ImaFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaFailureCause.setStatus("mandatory")


class _MscLpDS3ImaRemoteDefect_Type(Integer32):
    """Custom type mscLpDS3ImaRemoteDefect based on Integer32"""
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


_MscLpDS3ImaRemoteDefect_Type.__name__ = "Integer32"
_MscLpDS3ImaRemoteDefect_Object = MibTableColumn
mscLpDS3ImaRemoteDefect = _MscLpDS3ImaRemoteDefect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1, 2),
    _MscLpDS3ImaRemoteDefect_Type()
)
mscLpDS3ImaRemoteDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaRemoteDefect.setStatus("mandatory")


class _MscLpDS3ImaRemoteLidsConfig_Type(OctetString):
    """Custom type mscLpDS3ImaRemoteLidsConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscLpDS3ImaRemoteLidsConfig_Type.__name__ = "OctetString"
_MscLpDS3ImaRemoteLidsConfig_Object = MibTableColumn
mscLpDS3ImaRemoteLidsConfig = _MscLpDS3ImaRemoteLidsConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1, 3),
    _MscLpDS3ImaRemoteLidsConfig_Type()
)
mscLpDS3ImaRemoteLidsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaRemoteLidsConfig.setStatus("mandatory")


class _MscLpDS3ImaRemoteLidsActive_Type(OctetString):
    """Custom type mscLpDS3ImaRemoteLidsActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscLpDS3ImaRemoteLidsActive_Type.__name__ = "OctetString"
_MscLpDS3ImaRemoteLidsActive_Object = MibTableColumn
mscLpDS3ImaRemoteLidsActive = _MscLpDS3ImaRemoteLidsActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1, 4),
    _MscLpDS3ImaRemoteLidsActive_Type()
)
mscLpDS3ImaRemoteLidsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaRemoteLidsActive.setStatus("mandatory")


class _MscLpDS3ImaCellCapacity_Type(Unsigned32):
    """Custom type mscLpDS3ImaCellCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaCellCapacity_Type.__name__ = "Unsigned32"
_MscLpDS3ImaCellCapacity_Object = MibTableColumn
mscLpDS3ImaCellCapacity = _MscLpDS3ImaCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1, 5),
    _MscLpDS3ImaCellCapacity_Type()
)
mscLpDS3ImaCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaCellCapacity.setStatus("mandatory")


class _MscLpDS3ImaRemoteGid_Type(Unsigned32):
    """Custom type mscLpDS3ImaRemoteGid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscLpDS3ImaRemoteGid_Type.__name__ = "Unsigned32"
_MscLpDS3ImaRemoteGid_Object = MibTableColumn
mscLpDS3ImaRemoteGid = _MscLpDS3ImaRemoteGid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1, 6),
    _MscLpDS3ImaRemoteGid_Type()
)
mscLpDS3ImaRemoteGid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaRemoteGid.setStatus("mandatory")


class _MscLpDS3ImaClockingModeMismatch_Type(Integer32):
    """Custom type mscLpDS3ImaClockingModeMismatch based on Integer32"""
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


_MscLpDS3ImaClockingModeMismatch_Type.__name__ = "Integer32"
_MscLpDS3ImaClockingModeMismatch_Object = MibTableColumn
mscLpDS3ImaClockingModeMismatch = _MscLpDS3ImaClockingModeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 11, 1, 7),
    _MscLpDS3ImaClockingModeMismatch_Type()
)
mscLpDS3ImaClockingModeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaClockingModeMismatch.setStatus("mandatory")
_MscLpDS3ImaStatsTable_Object = MibTable
mscLpDS3ImaStatsTable = _MscLpDS3ImaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 12)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaStatsTable.setStatus("mandatory")
_MscLpDS3ImaStatsEntry_Object = MibTableRow
mscLpDS3ImaStatsEntry = _MscLpDS3ImaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 12, 1)
)
mscLpDS3ImaStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaStatsEntry.setStatus("mandatory")


class _MscLpDS3ImaRunningTime_Type(Unsigned32):
    """Custom type mscLpDS3ImaRunningTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaRunningTime_Type.__name__ = "Unsigned32"
_MscLpDS3ImaRunningTime_Object = MibTableColumn
mscLpDS3ImaRunningTime = _MscLpDS3ImaRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 12, 1, 1),
    _MscLpDS3ImaRunningTime_Type()
)
mscLpDS3ImaRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaRunningTime.setStatus("mandatory")


class _MscLpDS3ImaUnavailSecs_Type(Unsigned32):
    """Custom type mscLpDS3ImaUnavailSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaUnavailSecs_Type.__name__ = "Unsigned32"
_MscLpDS3ImaUnavailSecs_Object = MibTableColumn
mscLpDS3ImaUnavailSecs = _MscLpDS3ImaUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 12, 1, 2),
    _MscLpDS3ImaUnavailSecs_Type()
)
mscLpDS3ImaUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaUnavailSecs.setStatus("mandatory")


class _MscLpDS3ImaFailures_Type(Unsigned32):
    """Custom type mscLpDS3ImaFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpDS3ImaFailures_Type.__name__ = "Unsigned32"
_MscLpDS3ImaFailures_Object = MibTableColumn
mscLpDS3ImaFailures = _MscLpDS3ImaFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 12, 1, 3),
    _MscLpDS3ImaFailures_Type()
)
mscLpDS3ImaFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaFailures.setStatus("mandatory")


class _MscLpDS3ImaReceiveCellUtilization_Type(Gauge32):
    """Custom type mscLpDS3ImaReceiveCellUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpDS3ImaReceiveCellUtilization_Type.__name__ = "Gauge32"
_MscLpDS3ImaReceiveCellUtilization_Object = MibTableColumn
mscLpDS3ImaReceiveCellUtilization = _MscLpDS3ImaReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 12, 1, 4),
    _MscLpDS3ImaReceiveCellUtilization_Type()
)
mscLpDS3ImaReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaReceiveCellUtilization.setStatus("mandatory")


class _MscLpDS3ImaTransmitCellUtilization_Type(Gauge32):
    """Custom type mscLpDS3ImaTransmitCellUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpDS3ImaTransmitCellUtilization_Type.__name__ = "Gauge32"
_MscLpDS3ImaTransmitCellUtilization_Object = MibTableColumn
mscLpDS3ImaTransmitCellUtilization = _MscLpDS3ImaTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 12, 1, 5),
    _MscLpDS3ImaTransmitCellUtilization_Type()
)
mscLpDS3ImaTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaTransmitCellUtilization.setStatus("mandatory")
_MscLpDS3ImaCidDataTable_Object = MibTable
mscLpDS3ImaCidDataTable = _MscLpDS3ImaCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 13)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaCidDataTable.setStatus("mandatory")
_MscLpDS3ImaCidDataEntry_Object = MibTableRow
mscLpDS3ImaCidDataEntry = _MscLpDS3ImaCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 13, 1)
)
mscLpDS3ImaCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaCidDataEntry.setStatus("mandatory")


class _MscLpDS3ImaCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLpDS3ImaCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLpDS3ImaCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLpDS3ImaCustomerIdentifier_Object = MibTableColumn
mscLpDS3ImaCustomerIdentifier = _MscLpDS3ImaCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 13, 1, 1),
    _MscLpDS3ImaCustomerIdentifier_Type()
)
mscLpDS3ImaCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpDS3ImaCustomerIdentifier.setStatus("mandatory")
_MscLpDS3ImaStateTable_Object = MibTable
mscLpDS3ImaStateTable = _MscLpDS3ImaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14)
)
if mibBuilder.loadTexts:
    mscLpDS3ImaStateTable.setStatus("mandatory")
_MscLpDS3ImaStateEntry_Object = MibTableRow
mscLpDS3ImaStateEntry = _MscLpDS3ImaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1)
)
mscLpDS3ImaStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpDS3Index"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpDS3ImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpDS3ImaStateEntry.setStatus("mandatory")


class _MscLpDS3ImaAdminState_Type(Integer32):
    """Custom type mscLpDS3ImaAdminState based on Integer32"""
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


_MscLpDS3ImaAdminState_Type.__name__ = "Integer32"
_MscLpDS3ImaAdminState_Object = MibTableColumn
mscLpDS3ImaAdminState = _MscLpDS3ImaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 1),
    _MscLpDS3ImaAdminState_Type()
)
mscLpDS3ImaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaAdminState.setStatus("mandatory")


class _MscLpDS3ImaOperationalState_Type(Integer32):
    """Custom type mscLpDS3ImaOperationalState based on Integer32"""
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


_MscLpDS3ImaOperationalState_Type.__name__ = "Integer32"
_MscLpDS3ImaOperationalState_Object = MibTableColumn
mscLpDS3ImaOperationalState = _MscLpDS3ImaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 2),
    _MscLpDS3ImaOperationalState_Type()
)
mscLpDS3ImaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaOperationalState.setStatus("mandatory")


class _MscLpDS3ImaUsageState_Type(Integer32):
    """Custom type mscLpDS3ImaUsageState based on Integer32"""
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


_MscLpDS3ImaUsageState_Type.__name__ = "Integer32"
_MscLpDS3ImaUsageState_Object = MibTableColumn
mscLpDS3ImaUsageState = _MscLpDS3ImaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 3),
    _MscLpDS3ImaUsageState_Type()
)
mscLpDS3ImaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaUsageState.setStatus("mandatory")


class _MscLpDS3ImaAvailabilityStatus_Type(OctetString):
    """Custom type mscLpDS3ImaAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpDS3ImaAvailabilityStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaAvailabilityStatus_Object = MibTableColumn
mscLpDS3ImaAvailabilityStatus = _MscLpDS3ImaAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 4),
    _MscLpDS3ImaAvailabilityStatus_Type()
)
mscLpDS3ImaAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaAvailabilityStatus.setStatus("mandatory")


class _MscLpDS3ImaProceduralStatus_Type(OctetString):
    """Custom type mscLpDS3ImaProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpDS3ImaProceduralStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaProceduralStatus_Object = MibTableColumn
mscLpDS3ImaProceduralStatus = _MscLpDS3ImaProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 5),
    _MscLpDS3ImaProceduralStatus_Type()
)
mscLpDS3ImaProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaProceduralStatus.setStatus("mandatory")


class _MscLpDS3ImaControlStatus_Type(OctetString):
    """Custom type mscLpDS3ImaControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpDS3ImaControlStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaControlStatus_Object = MibTableColumn
mscLpDS3ImaControlStatus = _MscLpDS3ImaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 6),
    _MscLpDS3ImaControlStatus_Type()
)
mscLpDS3ImaControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaControlStatus.setStatus("mandatory")


class _MscLpDS3ImaAlarmStatus_Type(OctetString):
    """Custom type mscLpDS3ImaAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpDS3ImaAlarmStatus_Type.__name__ = "OctetString"
_MscLpDS3ImaAlarmStatus_Object = MibTableColumn
mscLpDS3ImaAlarmStatus = _MscLpDS3ImaAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 7),
    _MscLpDS3ImaAlarmStatus_Type()
)
mscLpDS3ImaAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaAlarmStatus.setStatus("mandatory")


class _MscLpDS3ImaStandbyStatus_Type(Integer32):
    """Custom type mscLpDS3ImaStandbyStatus based on Integer32"""
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


_MscLpDS3ImaStandbyStatus_Type.__name__ = "Integer32"
_MscLpDS3ImaStandbyStatus_Object = MibTableColumn
mscLpDS3ImaStandbyStatus = _MscLpDS3ImaStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 8),
    _MscLpDS3ImaStandbyStatus_Type()
)
mscLpDS3ImaStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaStandbyStatus.setStatus("mandatory")


class _MscLpDS3ImaUnknownStatus_Type(Integer32):
    """Custom type mscLpDS3ImaUnknownStatus based on Integer32"""
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


_MscLpDS3ImaUnknownStatus_Type.__name__ = "Integer32"
_MscLpDS3ImaUnknownStatus_Object = MibTableColumn
mscLpDS3ImaUnknownStatus = _MscLpDS3ImaUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 5, 7, 14, 1, 9),
    _MscLpDS3ImaUnknownStatus_Type()
)
mscLpDS3ImaUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpDS3ImaUnknownStatus.setStatus("mandatory")
_MscLpIma_ObjectIdentity = ObjectIdentity
mscLpIma = _MscLpIma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22)
)
_MscLpImaRowStatusTable_Object = MibTable
mscLpImaRowStatusTable = _MscLpImaRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 1)
)
if mibBuilder.loadTexts:
    mscLpImaRowStatusTable.setStatus("mandatory")
_MscLpImaRowStatusEntry_Object = MibTableRow
mscLpImaRowStatusEntry = _MscLpImaRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 1, 1)
)
mscLpImaRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaRowStatusEntry.setStatus("mandatory")
_MscLpImaRowStatus_Type = RowStatus
_MscLpImaRowStatus_Object = MibTableColumn
mscLpImaRowStatus = _MscLpImaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 1, 1, 1),
    _MscLpImaRowStatus_Type()
)
mscLpImaRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaRowStatus.setStatus("mandatory")
_MscLpImaComponentName_Type = DisplayString
_MscLpImaComponentName_Object = MibTableColumn
mscLpImaComponentName = _MscLpImaComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 1, 1, 2),
    _MscLpImaComponentName_Type()
)
mscLpImaComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaComponentName.setStatus("mandatory")
_MscLpImaStorageType_Type = StorageType
_MscLpImaStorageType_Object = MibTableColumn
mscLpImaStorageType = _MscLpImaStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 1, 1, 4),
    _MscLpImaStorageType_Type()
)
mscLpImaStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaStorageType.setStatus("mandatory")


class _MscLpImaIndex_Type(Integer32):
    """Custom type mscLpImaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_MscLpImaIndex_Type.__name__ = "Integer32"
_MscLpImaIndex_Object = MibTableColumn
mscLpImaIndex = _MscLpImaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 1, 1, 10),
    _MscLpImaIndex_Type()
)
mscLpImaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpImaIndex.setStatus("mandatory")
_MscLpImaTest_ObjectIdentity = ObjectIdentity
mscLpImaTest = _MscLpImaTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2)
)
_MscLpImaTestRowStatusTable_Object = MibTable
mscLpImaTestRowStatusTable = _MscLpImaTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpImaTestRowStatusTable.setStatus("mandatory")
_MscLpImaTestRowStatusEntry_Object = MibTableRow
mscLpImaTestRowStatusEntry = _MscLpImaTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 1, 1)
)
mscLpImaTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaTestRowStatusEntry.setStatus("mandatory")
_MscLpImaTestRowStatus_Type = RowStatus
_MscLpImaTestRowStatus_Object = MibTableColumn
mscLpImaTestRowStatus = _MscLpImaTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 1, 1, 1),
    _MscLpImaTestRowStatus_Type()
)
mscLpImaTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestRowStatus.setStatus("mandatory")
_MscLpImaTestComponentName_Type = DisplayString
_MscLpImaTestComponentName_Object = MibTableColumn
mscLpImaTestComponentName = _MscLpImaTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 1, 1, 2),
    _MscLpImaTestComponentName_Type()
)
mscLpImaTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestComponentName.setStatus("mandatory")
_MscLpImaTestStorageType_Type = StorageType
_MscLpImaTestStorageType_Object = MibTableColumn
mscLpImaTestStorageType = _MscLpImaTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 1, 1, 4),
    _MscLpImaTestStorageType_Type()
)
mscLpImaTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestStorageType.setStatus("mandatory")
_MscLpImaTestIndex_Type = NonReplicated
_MscLpImaTestIndex_Object = MibTableColumn
mscLpImaTestIndex = _MscLpImaTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 1, 1, 10),
    _MscLpImaTestIndex_Type()
)
mscLpImaTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpImaTestIndex.setStatus("mandatory")
_MscLpImaTestStateTable_Object = MibTable
mscLpImaTestStateTable = _MscLpImaTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpImaTestStateTable.setStatus("mandatory")
_MscLpImaTestStateEntry_Object = MibTableRow
mscLpImaTestStateEntry = _MscLpImaTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 10, 1)
)
mscLpImaTestStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaTestStateEntry.setStatus("mandatory")


class _MscLpImaTestAdminState_Type(Integer32):
    """Custom type mscLpImaTestAdminState based on Integer32"""
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


_MscLpImaTestAdminState_Type.__name__ = "Integer32"
_MscLpImaTestAdminState_Object = MibTableColumn
mscLpImaTestAdminState = _MscLpImaTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 10, 1, 1),
    _MscLpImaTestAdminState_Type()
)
mscLpImaTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestAdminState.setStatus("mandatory")


class _MscLpImaTestOperationalState_Type(Integer32):
    """Custom type mscLpImaTestOperationalState based on Integer32"""
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


_MscLpImaTestOperationalState_Type.__name__ = "Integer32"
_MscLpImaTestOperationalState_Object = MibTableColumn
mscLpImaTestOperationalState = _MscLpImaTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 10, 1, 2),
    _MscLpImaTestOperationalState_Type()
)
mscLpImaTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestOperationalState.setStatus("mandatory")


class _MscLpImaTestUsageState_Type(Integer32):
    """Custom type mscLpImaTestUsageState based on Integer32"""
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


_MscLpImaTestUsageState_Type.__name__ = "Integer32"
_MscLpImaTestUsageState_Object = MibTableColumn
mscLpImaTestUsageState = _MscLpImaTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 10, 1, 3),
    _MscLpImaTestUsageState_Type()
)
mscLpImaTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestUsageState.setStatus("mandatory")
_MscLpImaTestSetupTable_Object = MibTable
mscLpImaTestSetupTable = _MscLpImaTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11)
)
if mibBuilder.loadTexts:
    mscLpImaTestSetupTable.setStatus("mandatory")
_MscLpImaTestSetupEntry_Object = MibTableRow
mscLpImaTestSetupEntry = _MscLpImaTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1)
)
mscLpImaTestSetupEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaTestSetupEntry.setStatus("mandatory")


class _MscLpImaTestPurpose_Type(AsciiString):
    """Custom type mscLpImaTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MscLpImaTestPurpose_Type.__name__ = "AsciiString"
_MscLpImaTestPurpose_Object = MibTableColumn
mscLpImaTestPurpose = _MscLpImaTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 1),
    _MscLpImaTestPurpose_Type()
)
mscLpImaTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestPurpose.setStatus("mandatory")


class _MscLpImaTestType_Type(Integer32):
    """Custom type mscLpImaTestType based on Integer32"""
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


_MscLpImaTestType_Type.__name__ = "Integer32"
_MscLpImaTestType_Object = MibTableColumn
mscLpImaTestType = _MscLpImaTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 2),
    _MscLpImaTestType_Type()
)
mscLpImaTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestType.setStatus("mandatory")


class _MscLpImaTestFrmSize_Type(Unsigned32):
    """Custom type mscLpImaTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_MscLpImaTestFrmSize_Type.__name__ = "Unsigned32"
_MscLpImaTestFrmSize_Object = MibTableColumn
mscLpImaTestFrmSize = _MscLpImaTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 3),
    _MscLpImaTestFrmSize_Type()
)
mscLpImaTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestFrmSize.setStatus("mandatory")


class _MscLpImaTestFrmPatternType_Type(Integer32):
    """Custom type mscLpImaTestFrmPatternType based on Integer32"""
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


_MscLpImaTestFrmPatternType_Type.__name__ = "Integer32"
_MscLpImaTestFrmPatternType_Object = MibTableColumn
mscLpImaTestFrmPatternType = _MscLpImaTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 4),
    _MscLpImaTestFrmPatternType_Type()
)
mscLpImaTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestFrmPatternType.setStatus("mandatory")


class _MscLpImaTestCustomizedPattern_Type(Hex):
    """Custom type mscLpImaTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaTestCustomizedPattern_Type.__name__ = "Hex"
_MscLpImaTestCustomizedPattern_Object = MibTableColumn
mscLpImaTestCustomizedPattern = _MscLpImaTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 5),
    _MscLpImaTestCustomizedPattern_Type()
)
mscLpImaTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestCustomizedPattern.setStatus("mandatory")


class _MscLpImaTestDataStartDelay_Type(Unsigned32):
    """Custom type mscLpImaTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_MscLpImaTestDataStartDelay_Type.__name__ = "Unsigned32"
_MscLpImaTestDataStartDelay_Object = MibTableColumn
mscLpImaTestDataStartDelay = _MscLpImaTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 6),
    _MscLpImaTestDataStartDelay_Type()
)
mscLpImaTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestDataStartDelay.setStatus("mandatory")


class _MscLpImaTestDisplayInterval_Type(Unsigned32):
    """Custom type mscLpImaTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_MscLpImaTestDisplayInterval_Type.__name__ = "Unsigned32"
_MscLpImaTestDisplayInterval_Object = MibTableColumn
mscLpImaTestDisplayInterval = _MscLpImaTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 7),
    _MscLpImaTestDisplayInterval_Type()
)
mscLpImaTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestDisplayInterval.setStatus("mandatory")


class _MscLpImaTestDuration_Type(Unsigned32):
    """Custom type mscLpImaTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_MscLpImaTestDuration_Type.__name__ = "Unsigned32"
_MscLpImaTestDuration_Object = MibTableColumn
mscLpImaTestDuration = _MscLpImaTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 11, 1, 8),
    _MscLpImaTestDuration_Type()
)
mscLpImaTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTestDuration.setStatus("mandatory")
_MscLpImaTestResultsTable_Object = MibTable
mscLpImaTestResultsTable = _MscLpImaTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12)
)
if mibBuilder.loadTexts:
    mscLpImaTestResultsTable.setStatus("mandatory")
_MscLpImaTestResultsEntry_Object = MibTableRow
mscLpImaTestResultsEntry = _MscLpImaTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1)
)
mscLpImaTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaTestResultsEntry.setStatus("mandatory")
_MscLpImaTestElapsedTime_Type = Counter32
_MscLpImaTestElapsedTime_Object = MibTableColumn
mscLpImaTestElapsedTime = _MscLpImaTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 1),
    _MscLpImaTestElapsedTime_Type()
)
mscLpImaTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestElapsedTime.setStatus("mandatory")


class _MscLpImaTestTimeRemaining_Type(Unsigned32):
    """Custom type mscLpImaTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaTestTimeRemaining_Type.__name__ = "Unsigned32"
_MscLpImaTestTimeRemaining_Object = MibTableColumn
mscLpImaTestTimeRemaining = _MscLpImaTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 2),
    _MscLpImaTestTimeRemaining_Type()
)
mscLpImaTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestTimeRemaining.setStatus("mandatory")


class _MscLpImaTestCauseOfTermination_Type(Integer32):
    """Custom type mscLpImaTestCauseOfTermination based on Integer32"""
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


_MscLpImaTestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpImaTestCauseOfTermination_Object = MibTableColumn
mscLpImaTestCauseOfTermination = _MscLpImaTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 3),
    _MscLpImaTestCauseOfTermination_Type()
)
mscLpImaTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestCauseOfTermination.setStatus("mandatory")
_MscLpImaTestBitsTx_Type = PassportCounter64
_MscLpImaTestBitsTx_Object = MibTableColumn
mscLpImaTestBitsTx = _MscLpImaTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 4),
    _MscLpImaTestBitsTx_Type()
)
mscLpImaTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestBitsTx.setStatus("mandatory")
_MscLpImaTestBytesTx_Type = PassportCounter64
_MscLpImaTestBytesTx_Object = MibTableColumn
mscLpImaTestBytesTx = _MscLpImaTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 5),
    _MscLpImaTestBytesTx_Type()
)
mscLpImaTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestBytesTx.setStatus("mandatory")
_MscLpImaTestFrmTx_Type = PassportCounter64
_MscLpImaTestFrmTx_Object = MibTableColumn
mscLpImaTestFrmTx = _MscLpImaTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 6),
    _MscLpImaTestFrmTx_Type()
)
mscLpImaTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestFrmTx.setStatus("mandatory")
_MscLpImaTestBitsRx_Type = PassportCounter64
_MscLpImaTestBitsRx_Object = MibTableColumn
mscLpImaTestBitsRx = _MscLpImaTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 7),
    _MscLpImaTestBitsRx_Type()
)
mscLpImaTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestBitsRx.setStatus("mandatory")
_MscLpImaTestBytesRx_Type = PassportCounter64
_MscLpImaTestBytesRx_Object = MibTableColumn
mscLpImaTestBytesRx = _MscLpImaTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 8),
    _MscLpImaTestBytesRx_Type()
)
mscLpImaTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestBytesRx.setStatus("mandatory")
_MscLpImaTestFrmRx_Type = PassportCounter64
_MscLpImaTestFrmRx_Object = MibTableColumn
mscLpImaTestFrmRx = _MscLpImaTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 9),
    _MscLpImaTestFrmRx_Type()
)
mscLpImaTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestFrmRx.setStatus("mandatory")
_MscLpImaTestErroredFrmRx_Type = PassportCounter64
_MscLpImaTestErroredFrmRx_Object = MibTableColumn
mscLpImaTestErroredFrmRx = _MscLpImaTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 10),
    _MscLpImaTestErroredFrmRx_Type()
)
mscLpImaTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestErroredFrmRx.setStatus("mandatory")


class _MscLpImaTestBitErrorRate_Type(AsciiString):
    """Custom type mscLpImaTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_MscLpImaTestBitErrorRate_Type.__name__ = "AsciiString"
_MscLpImaTestBitErrorRate_Object = MibTableColumn
mscLpImaTestBitErrorRate = _MscLpImaTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 2, 12, 1, 11),
    _MscLpImaTestBitErrorRate_Type()
)
mscLpImaTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTestBitErrorRate.setStatus("mandatory")
_MscLpImaLk_ObjectIdentity = ObjectIdentity
mscLpImaLk = _MscLpImaLk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3)
)
_MscLpImaLkRowStatusTable_Object = MibTable
mscLpImaLkRowStatusTable = _MscLpImaLkRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 1)
)
if mibBuilder.loadTexts:
    mscLpImaLkRowStatusTable.setStatus("mandatory")
_MscLpImaLkRowStatusEntry_Object = MibTableRow
mscLpImaLkRowStatusEntry = _MscLpImaLkRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 1, 1)
)
mscLpImaLkRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaLkRowStatusEntry.setStatus("mandatory")
_MscLpImaLkRowStatus_Type = RowStatus
_MscLpImaLkRowStatus_Object = MibTableColumn
mscLpImaLkRowStatus = _MscLpImaLkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 1, 1, 1),
    _MscLpImaLkRowStatus_Type()
)
mscLpImaLkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaLkRowStatus.setStatus("mandatory")
_MscLpImaLkComponentName_Type = DisplayString
_MscLpImaLkComponentName_Object = MibTableColumn
mscLpImaLkComponentName = _MscLpImaLkComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 1, 1, 2),
    _MscLpImaLkComponentName_Type()
)
mscLpImaLkComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkComponentName.setStatus("mandatory")
_MscLpImaLkStorageType_Type = StorageType
_MscLpImaLkStorageType_Object = MibTableColumn
mscLpImaLkStorageType = _MscLpImaLkStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 1, 1, 4),
    _MscLpImaLkStorageType_Type()
)
mscLpImaLkStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkStorageType.setStatus("mandatory")


class _MscLpImaLkIndex_Type(Integer32):
    """Custom type mscLpImaLkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MscLpImaLkIndex_Type.__name__ = "Integer32"
_MscLpImaLkIndex_Object = MibTableColumn
mscLpImaLkIndex = _MscLpImaLkIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 1, 1, 10),
    _MscLpImaLkIndex_Type()
)
mscLpImaLkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpImaLkIndex.setStatus("mandatory")
_MscLpImaLkProvTable_Object = MibTable
mscLpImaLkProvTable = _MscLpImaLkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 10)
)
if mibBuilder.loadTexts:
    mscLpImaLkProvTable.setStatus("mandatory")
_MscLpImaLkProvEntry_Object = MibTableRow
mscLpImaLkProvEntry = _MscLpImaLkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 10, 1)
)
mscLpImaLkProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaLkProvEntry.setStatus("mandatory")
_MscLpImaLkInterfaceName_Type = Link
_MscLpImaLkInterfaceName_Object = MibTableColumn
mscLpImaLkInterfaceName = _MscLpImaLkInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 10, 1, 1),
    _MscLpImaLkInterfaceName_Type()
)
mscLpImaLkInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaLkInterfaceName.setStatus("mandatory")
_MscLpImaLkOperTable_Object = MibTable
mscLpImaLkOperTable = _MscLpImaLkOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 11)
)
if mibBuilder.loadTexts:
    mscLpImaLkOperTable.setStatus("mandatory")
_MscLpImaLkOperEntry_Object = MibTableRow
mscLpImaLkOperEntry = _MscLpImaLkOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 11, 1)
)
mscLpImaLkOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaLkOperEntry.setStatus("mandatory")


class _MscLpImaLkFailureCause_Type(Integer32):
    """Custom type mscLpImaLkFailureCause based on Integer32"""
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


_MscLpImaLkFailureCause_Type.__name__ = "Integer32"
_MscLpImaLkFailureCause_Object = MibTableColumn
mscLpImaLkFailureCause = _MscLpImaLkFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 11, 1, 1),
    _MscLpImaLkFailureCause_Type()
)
mscLpImaLkFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkFailureCause.setStatus("mandatory")


class _MscLpImaLkRemoteDefect_Type(Integer32):
    """Custom type mscLpImaLkRemoteDefect based on Integer32"""
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


_MscLpImaLkRemoteDefect_Type.__name__ = "Integer32"
_MscLpImaLkRemoteDefect_Object = MibTableColumn
mscLpImaLkRemoteDefect = _MscLpImaLkRemoteDefect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 11, 1, 2),
    _MscLpImaLkRemoteDefect_Type()
)
mscLpImaLkRemoteDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkRemoteDefect.setStatus("mandatory")


class _MscLpImaLkRemoteLid_Type(Unsigned32):
    """Custom type mscLpImaLkRemoteLid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_MscLpImaLkRemoteLid_Type.__name__ = "Unsigned32"
_MscLpImaLkRemoteLid_Object = MibTableColumn
mscLpImaLkRemoteLid = _MscLpImaLkRemoteLid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 11, 1, 3),
    _MscLpImaLkRemoteLid_Type()
)
mscLpImaLkRemoteLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkRemoteLid.setStatus("mandatory")


class _MscLpImaLkRelativeDelay_Type(Unsigned32):
    """Custom type mscLpImaLkRelativeDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaLkRelativeDelay_Type.__name__ = "Unsigned32"
_MscLpImaLkRelativeDelay_Object = MibTableColumn
mscLpImaLkRelativeDelay = _MscLpImaLkRelativeDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 11, 1, 4),
    _MscLpImaLkRelativeDelay_Type()
)
mscLpImaLkRelativeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkRelativeDelay.setStatus("mandatory")


class _MscLpImaLkLastOifCause_Type(Integer32):
    """Custom type mscLpImaLkLastOifCause based on Integer32"""
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


_MscLpImaLkLastOifCause_Type.__name__ = "Integer32"
_MscLpImaLkLastOifCause_Object = MibTableColumn
mscLpImaLkLastOifCause = _MscLpImaLkLastOifCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 11, 1, 5),
    _MscLpImaLkLastOifCause_Type()
)
mscLpImaLkLastOifCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkLastOifCause.setStatus("mandatory")
_MscLpImaLkStatsTable_Object = MibTable
mscLpImaLkStatsTable = _MscLpImaLkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12)
)
if mibBuilder.loadTexts:
    mscLpImaLkStatsTable.setStatus("mandatory")
_MscLpImaLkStatsEntry_Object = MibTableRow
mscLpImaLkStatsEntry = _MscLpImaLkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1)
)
mscLpImaLkStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaLkStatsEntry.setStatus("mandatory")


class _MscLpImaLkRunningTime_Type(Unsigned32):
    """Custom type mscLpImaLkRunningTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaLkRunningTime_Type.__name__ = "Unsigned32"
_MscLpImaLkRunningTime_Object = MibTableColumn
mscLpImaLkRunningTime = _MscLpImaLkRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 1),
    _MscLpImaLkRunningTime_Type()
)
mscLpImaLkRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkRunningTime.setStatus("mandatory")


class _MscLpImaLkUnavailSecs_Type(Unsigned32):
    """Custom type mscLpImaLkUnavailSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaLkUnavailSecs_Type.__name__ = "Unsigned32"
_MscLpImaLkUnavailSecs_Object = MibTableColumn
mscLpImaLkUnavailSecs = _MscLpImaLkUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 2),
    _MscLpImaLkUnavailSecs_Type()
)
mscLpImaLkUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkUnavailSecs.setStatus("mandatory")


class _MscLpImaLkFailures_Type(Unsigned32):
    """Custom type mscLpImaLkFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaLkFailures_Type.__name__ = "Unsigned32"
_MscLpImaLkFailures_Object = MibTableColumn
mscLpImaLkFailures = _MscLpImaLkFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 3),
    _MscLpImaLkFailures_Type()
)
mscLpImaLkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkFailures.setStatus("mandatory")
_MscLpImaLkUnusableSec_Type = Counter32
_MscLpImaLkUnusableSec_Object = MibTableColumn
mscLpImaLkUnusableSec = _MscLpImaLkUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 4),
    _MscLpImaLkUnusableSec_Type()
)
mscLpImaLkUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkUnusableSec.setStatus("mandatory")
_MscLpImaLkSevErroredSec_Type = Counter32
_MscLpImaLkSevErroredSec_Object = MibTableColumn
mscLpImaLkSevErroredSec = _MscLpImaLkSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 5),
    _MscLpImaLkSevErroredSec_Type()
)
mscLpImaLkSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkSevErroredSec.setStatus("mandatory")
_MscLpImaLkFarEndUnusableSec_Type = Counter32
_MscLpImaLkFarEndUnusableSec_Object = MibTableColumn
mscLpImaLkFarEndUnusableSec = _MscLpImaLkFarEndUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 6),
    _MscLpImaLkFarEndUnusableSec_Type()
)
mscLpImaLkFarEndUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkFarEndUnusableSec.setStatus("mandatory")
_MscLpImaLkFarEndSevErroredSec_Type = Counter32
_MscLpImaLkFarEndSevErroredSec_Object = MibTableColumn
mscLpImaLkFarEndSevErroredSec = _MscLpImaLkFarEndSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 7),
    _MscLpImaLkFarEndSevErroredSec_Type()
)
mscLpImaLkFarEndSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkFarEndSevErroredSec.setStatus("mandatory")
_MscLpImaLkFarEndUnavailSec_Type = Counter32
_MscLpImaLkFarEndUnavailSec_Object = MibTableColumn
mscLpImaLkFarEndUnavailSec = _MscLpImaLkFarEndUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 8),
    _MscLpImaLkFarEndUnavailSec_Type()
)
mscLpImaLkFarEndUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkFarEndUnavailSec.setStatus("mandatory")
_MscLpImaLkIcpViolations_Type = Counter32
_MscLpImaLkIcpViolations_Object = MibTableColumn
mscLpImaLkIcpViolations = _MscLpImaLkIcpViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 9),
    _MscLpImaLkIcpViolations_Type()
)
mscLpImaLkIcpViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkIcpViolations.setStatus("mandatory")
_MscLpImaLkTxStuffEvents_Type = Counter32
_MscLpImaLkTxStuffEvents_Object = MibTableColumn
mscLpImaLkTxStuffEvents = _MscLpImaLkTxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 10),
    _MscLpImaLkTxStuffEvents_Type()
)
mscLpImaLkTxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkTxStuffEvents.setStatus("mandatory")
_MscLpImaLkRxStuffEvents_Type = Counter32
_MscLpImaLkRxStuffEvents_Object = MibTableColumn
mscLpImaLkRxStuffEvents = _MscLpImaLkRxStuffEvents_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 11),
    _MscLpImaLkRxStuffEvents_Type()
)
mscLpImaLkRxStuffEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkRxStuffEvents.setStatus("mandatory")
_MscLpImaLkIdleCellSec_Type = Counter32
_MscLpImaLkIdleCellSec_Object = MibTableColumn
mscLpImaLkIdleCellSec = _MscLpImaLkIdleCellSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 12, 1, 12),
    _MscLpImaLkIdleCellSec_Type()
)
mscLpImaLkIdleCellSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkIdleCellSec.setStatus("mandatory")
_MscLpImaLkStateTable_Object = MibTable
mscLpImaLkStateTable = _MscLpImaLkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13)
)
if mibBuilder.loadTexts:
    mscLpImaLkStateTable.setStatus("mandatory")
_MscLpImaLkStateEntry_Object = MibTableRow
mscLpImaLkStateEntry = _MscLpImaLkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1)
)
mscLpImaLkStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaLkIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaLkStateEntry.setStatus("mandatory")


class _MscLpImaLkAdminState_Type(Integer32):
    """Custom type mscLpImaLkAdminState based on Integer32"""
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


_MscLpImaLkAdminState_Type.__name__ = "Integer32"
_MscLpImaLkAdminState_Object = MibTableColumn
mscLpImaLkAdminState = _MscLpImaLkAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 1),
    _MscLpImaLkAdminState_Type()
)
mscLpImaLkAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkAdminState.setStatus("mandatory")


class _MscLpImaLkOperationalState_Type(Integer32):
    """Custom type mscLpImaLkOperationalState based on Integer32"""
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


_MscLpImaLkOperationalState_Type.__name__ = "Integer32"
_MscLpImaLkOperationalState_Object = MibTableColumn
mscLpImaLkOperationalState = _MscLpImaLkOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 2),
    _MscLpImaLkOperationalState_Type()
)
mscLpImaLkOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkOperationalState.setStatus("mandatory")


class _MscLpImaLkUsageState_Type(Integer32):
    """Custom type mscLpImaLkUsageState based on Integer32"""
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


_MscLpImaLkUsageState_Type.__name__ = "Integer32"
_MscLpImaLkUsageState_Object = MibTableColumn
mscLpImaLkUsageState = _MscLpImaLkUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 3),
    _MscLpImaLkUsageState_Type()
)
mscLpImaLkUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkUsageState.setStatus("mandatory")


class _MscLpImaLkAvailabilityStatus_Type(OctetString):
    """Custom type mscLpImaLkAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpImaLkAvailabilityStatus_Type.__name__ = "OctetString"
_MscLpImaLkAvailabilityStatus_Object = MibTableColumn
mscLpImaLkAvailabilityStatus = _MscLpImaLkAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 4),
    _MscLpImaLkAvailabilityStatus_Type()
)
mscLpImaLkAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkAvailabilityStatus.setStatus("mandatory")


class _MscLpImaLkProceduralStatus_Type(OctetString):
    """Custom type mscLpImaLkProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpImaLkProceduralStatus_Type.__name__ = "OctetString"
_MscLpImaLkProceduralStatus_Object = MibTableColumn
mscLpImaLkProceduralStatus = _MscLpImaLkProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 5),
    _MscLpImaLkProceduralStatus_Type()
)
mscLpImaLkProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkProceduralStatus.setStatus("mandatory")


class _MscLpImaLkControlStatus_Type(OctetString):
    """Custom type mscLpImaLkControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpImaLkControlStatus_Type.__name__ = "OctetString"
_MscLpImaLkControlStatus_Object = MibTableColumn
mscLpImaLkControlStatus = _MscLpImaLkControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 6),
    _MscLpImaLkControlStatus_Type()
)
mscLpImaLkControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkControlStatus.setStatus("mandatory")


class _MscLpImaLkAlarmStatus_Type(OctetString):
    """Custom type mscLpImaLkAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpImaLkAlarmStatus_Type.__name__ = "OctetString"
_MscLpImaLkAlarmStatus_Object = MibTableColumn
mscLpImaLkAlarmStatus = _MscLpImaLkAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 7),
    _MscLpImaLkAlarmStatus_Type()
)
mscLpImaLkAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkAlarmStatus.setStatus("mandatory")


class _MscLpImaLkStandbyStatus_Type(Integer32):
    """Custom type mscLpImaLkStandbyStatus based on Integer32"""
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


_MscLpImaLkStandbyStatus_Type.__name__ = "Integer32"
_MscLpImaLkStandbyStatus_Object = MibTableColumn
mscLpImaLkStandbyStatus = _MscLpImaLkStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 8),
    _MscLpImaLkStandbyStatus_Type()
)
mscLpImaLkStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkStandbyStatus.setStatus("mandatory")


class _MscLpImaLkUnknownStatus_Type(Integer32):
    """Custom type mscLpImaLkUnknownStatus based on Integer32"""
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


_MscLpImaLkUnknownStatus_Type.__name__ = "Integer32"
_MscLpImaLkUnknownStatus_Object = MibTableColumn
mscLpImaLkUnknownStatus = _MscLpImaLkUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 3, 13, 1, 9),
    _MscLpImaLkUnknownStatus_Type()
)
mscLpImaLkUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaLkUnknownStatus.setStatus("mandatory")
_MscLpImaProvTable_Object = MibTable
mscLpImaProvTable = _MscLpImaProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10)
)
if mibBuilder.loadTexts:
    mscLpImaProvTable.setStatus("mandatory")
_MscLpImaProvEntry_Object = MibTableRow
mscLpImaProvEntry = _MscLpImaProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10, 1)
)
mscLpImaProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaProvEntry.setStatus("mandatory")


class _MscLpImaLinkSelectionCriterion_Type(Integer32):
    """Custom type mscLpImaLinkSelectionCriterion based on Integer32"""
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


_MscLpImaLinkSelectionCriterion_Type.__name__ = "Integer32"
_MscLpImaLinkSelectionCriterion_Object = MibTableColumn
mscLpImaLinkSelectionCriterion = _MscLpImaLinkSelectionCriterion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10, 1, 1),
    _MscLpImaLinkSelectionCriterion_Type()
)
mscLpImaLinkSelectionCriterion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaLinkSelectionCriterion.setStatus("mandatory")


class _MscLpImaMaxDiffDelay_Type(Unsigned32):
    """Custom type mscLpImaMaxDiffDelay based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MscLpImaMaxDiffDelay_Type.__name__ = "Unsigned32"
_MscLpImaMaxDiffDelay_Object = MibTableColumn
mscLpImaMaxDiffDelay = _MscLpImaMaxDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10, 1, 2),
    _MscLpImaMaxDiffDelay_Type()
)
mscLpImaMaxDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaMaxDiffDelay.setStatus("mandatory")


class _MscLpImaLinkRetryTimeout_Type(Unsigned32):
    """Custom type mscLpImaLinkRetryTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_MscLpImaLinkRetryTimeout_Type.__name__ = "Unsigned32"
_MscLpImaLinkRetryTimeout_Object = MibTableColumn
mscLpImaLinkRetryTimeout = _MscLpImaLinkRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10, 1, 3),
    _MscLpImaLinkRetryTimeout_Type()
)
mscLpImaLinkRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaLinkRetryTimeout.setStatus("mandatory")
_MscLpImaApplicationFramerName_Type = Link
_MscLpImaApplicationFramerName_Object = MibTableColumn
mscLpImaApplicationFramerName = _MscLpImaApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10, 1, 4),
    _MscLpImaApplicationFramerName_Type()
)
mscLpImaApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaApplicationFramerName.setStatus("mandatory")


class _MscLpImaTransmitClockMode_Type(Integer32):
    """Custom type mscLpImaTransmitClockMode based on Integer32"""
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


_MscLpImaTransmitClockMode_Type.__name__ = "Integer32"
_MscLpImaTransmitClockMode_Object = MibTableColumn
mscLpImaTransmitClockMode = _MscLpImaTransmitClockMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10, 1, 5),
    _MscLpImaTransmitClockMode_Type()
)
mscLpImaTransmitClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaTransmitClockMode.setStatus("mandatory")


class _MscLpImaProtocol_Type(Integer32):
    """Custom type mscLpImaProtocol based on Integer32"""
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


_MscLpImaProtocol_Type.__name__ = "Integer32"
_MscLpImaProtocol_Object = MibTableColumn
mscLpImaProtocol = _MscLpImaProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 10, 1, 6),
    _MscLpImaProtocol_Type()
)
mscLpImaProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaProtocol.setStatus("mandatory")
_MscLpImaOperTable_Object = MibTable
mscLpImaOperTable = _MscLpImaOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11)
)
if mibBuilder.loadTexts:
    mscLpImaOperTable.setStatus("mandatory")
_MscLpImaOperEntry_Object = MibTableRow
mscLpImaOperEntry = _MscLpImaOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1)
)
mscLpImaOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaOperEntry.setStatus("mandatory")


class _MscLpImaFailureCause_Type(Integer32):
    """Custom type mscLpImaFailureCause based on Integer32"""
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


_MscLpImaFailureCause_Type.__name__ = "Integer32"
_MscLpImaFailureCause_Object = MibTableColumn
mscLpImaFailureCause = _MscLpImaFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1, 1),
    _MscLpImaFailureCause_Type()
)
mscLpImaFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaFailureCause.setStatus("mandatory")


class _MscLpImaRemoteDefect_Type(Integer32):
    """Custom type mscLpImaRemoteDefect based on Integer32"""
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


_MscLpImaRemoteDefect_Type.__name__ = "Integer32"
_MscLpImaRemoteDefect_Object = MibTableColumn
mscLpImaRemoteDefect = _MscLpImaRemoteDefect_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1, 2),
    _MscLpImaRemoteDefect_Type()
)
mscLpImaRemoteDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaRemoteDefect.setStatus("mandatory")


class _MscLpImaRemoteLidsConfig_Type(OctetString):
    """Custom type mscLpImaRemoteLidsConfig based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscLpImaRemoteLidsConfig_Type.__name__ = "OctetString"
_MscLpImaRemoteLidsConfig_Object = MibTableColumn
mscLpImaRemoteLidsConfig = _MscLpImaRemoteLidsConfig_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1, 3),
    _MscLpImaRemoteLidsConfig_Type()
)
mscLpImaRemoteLidsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaRemoteLidsConfig.setStatus("mandatory")


class _MscLpImaRemoteLidsActive_Type(OctetString):
    """Custom type mscLpImaRemoteLidsActive based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_MscLpImaRemoteLidsActive_Type.__name__ = "OctetString"
_MscLpImaRemoteLidsActive_Object = MibTableColumn
mscLpImaRemoteLidsActive = _MscLpImaRemoteLidsActive_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1, 4),
    _MscLpImaRemoteLidsActive_Type()
)
mscLpImaRemoteLidsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaRemoteLidsActive.setStatus("mandatory")


class _MscLpImaCellCapacity_Type(Unsigned32):
    """Custom type mscLpImaCellCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaCellCapacity_Type.__name__ = "Unsigned32"
_MscLpImaCellCapacity_Object = MibTableColumn
mscLpImaCellCapacity = _MscLpImaCellCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1, 5),
    _MscLpImaCellCapacity_Type()
)
mscLpImaCellCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaCellCapacity.setStatus("mandatory")


class _MscLpImaRemoteGid_Type(Unsigned32):
    """Custom type mscLpImaRemoteGid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscLpImaRemoteGid_Type.__name__ = "Unsigned32"
_MscLpImaRemoteGid_Object = MibTableColumn
mscLpImaRemoteGid = _MscLpImaRemoteGid_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1, 6),
    _MscLpImaRemoteGid_Type()
)
mscLpImaRemoteGid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaRemoteGid.setStatus("mandatory")


class _MscLpImaClockingModeMismatch_Type(Integer32):
    """Custom type mscLpImaClockingModeMismatch based on Integer32"""
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


_MscLpImaClockingModeMismatch_Type.__name__ = "Integer32"
_MscLpImaClockingModeMismatch_Object = MibTableColumn
mscLpImaClockingModeMismatch = _MscLpImaClockingModeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 11, 1, 7),
    _MscLpImaClockingModeMismatch_Type()
)
mscLpImaClockingModeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaClockingModeMismatch.setStatus("mandatory")
_MscLpImaStatsTable_Object = MibTable
mscLpImaStatsTable = _MscLpImaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 12)
)
if mibBuilder.loadTexts:
    mscLpImaStatsTable.setStatus("mandatory")
_MscLpImaStatsEntry_Object = MibTableRow
mscLpImaStatsEntry = _MscLpImaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 12, 1)
)
mscLpImaStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaStatsEntry.setStatus("mandatory")


class _MscLpImaRunningTime_Type(Unsigned32):
    """Custom type mscLpImaRunningTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaRunningTime_Type.__name__ = "Unsigned32"
_MscLpImaRunningTime_Object = MibTableColumn
mscLpImaRunningTime = _MscLpImaRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 12, 1, 1),
    _MscLpImaRunningTime_Type()
)
mscLpImaRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaRunningTime.setStatus("mandatory")


class _MscLpImaUnavailSecs_Type(Unsigned32):
    """Custom type mscLpImaUnavailSecs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaUnavailSecs_Type.__name__ = "Unsigned32"
_MscLpImaUnavailSecs_Object = MibTableColumn
mscLpImaUnavailSecs = _MscLpImaUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 12, 1, 2),
    _MscLpImaUnavailSecs_Type()
)
mscLpImaUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaUnavailSecs.setStatus("mandatory")


class _MscLpImaFailures_Type(Unsigned32):
    """Custom type mscLpImaFailures based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscLpImaFailures_Type.__name__ = "Unsigned32"
_MscLpImaFailures_Object = MibTableColumn
mscLpImaFailures = _MscLpImaFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 12, 1, 3),
    _MscLpImaFailures_Type()
)
mscLpImaFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaFailures.setStatus("mandatory")


class _MscLpImaReceiveCellUtilization_Type(Gauge32):
    """Custom type mscLpImaReceiveCellUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpImaReceiveCellUtilization_Type.__name__ = "Gauge32"
_MscLpImaReceiveCellUtilization_Object = MibTableColumn
mscLpImaReceiveCellUtilization = _MscLpImaReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 12, 1, 4),
    _MscLpImaReceiveCellUtilization_Type()
)
mscLpImaReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaReceiveCellUtilization.setStatus("mandatory")


class _MscLpImaTransmitCellUtilization_Type(Gauge32):
    """Custom type mscLpImaTransmitCellUtilization based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_MscLpImaTransmitCellUtilization_Type.__name__ = "Gauge32"
_MscLpImaTransmitCellUtilization_Object = MibTableColumn
mscLpImaTransmitCellUtilization = _MscLpImaTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 12, 1, 5),
    _MscLpImaTransmitCellUtilization_Type()
)
mscLpImaTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaTransmitCellUtilization.setStatus("mandatory")
_MscLpImaCidDataTable_Object = MibTable
mscLpImaCidDataTable = _MscLpImaCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 13)
)
if mibBuilder.loadTexts:
    mscLpImaCidDataTable.setStatus("mandatory")
_MscLpImaCidDataEntry_Object = MibTableRow
mscLpImaCidDataEntry = _MscLpImaCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 13, 1)
)
mscLpImaCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaCidDataEntry.setStatus("mandatory")


class _MscLpImaCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLpImaCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLpImaCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLpImaCustomerIdentifier_Object = MibTableColumn
mscLpImaCustomerIdentifier = _MscLpImaCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 13, 1, 1),
    _MscLpImaCustomerIdentifier_Type()
)
mscLpImaCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpImaCustomerIdentifier.setStatus("mandatory")
_MscLpImaStateTable_Object = MibTable
mscLpImaStateTable = _MscLpImaStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14)
)
if mibBuilder.loadTexts:
    mscLpImaStateTable.setStatus("mandatory")
_MscLpImaStateEntry_Object = MibTableRow
mscLpImaStateEntry = _MscLpImaStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1)
)
mscLpImaStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-ImaMIB", "mscLpImaIndex"),
)
if mibBuilder.loadTexts:
    mscLpImaStateEntry.setStatus("mandatory")


class _MscLpImaAdminState_Type(Integer32):
    """Custom type mscLpImaAdminState based on Integer32"""
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


_MscLpImaAdminState_Type.__name__ = "Integer32"
_MscLpImaAdminState_Object = MibTableColumn
mscLpImaAdminState = _MscLpImaAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 1),
    _MscLpImaAdminState_Type()
)
mscLpImaAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaAdminState.setStatus("mandatory")


class _MscLpImaOperationalState_Type(Integer32):
    """Custom type mscLpImaOperationalState based on Integer32"""
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


_MscLpImaOperationalState_Type.__name__ = "Integer32"
_MscLpImaOperationalState_Object = MibTableColumn
mscLpImaOperationalState = _MscLpImaOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 2),
    _MscLpImaOperationalState_Type()
)
mscLpImaOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaOperationalState.setStatus("mandatory")


class _MscLpImaUsageState_Type(Integer32):
    """Custom type mscLpImaUsageState based on Integer32"""
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


_MscLpImaUsageState_Type.__name__ = "Integer32"
_MscLpImaUsageState_Object = MibTableColumn
mscLpImaUsageState = _MscLpImaUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 3),
    _MscLpImaUsageState_Type()
)
mscLpImaUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaUsageState.setStatus("mandatory")


class _MscLpImaAvailabilityStatus_Type(OctetString):
    """Custom type mscLpImaAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscLpImaAvailabilityStatus_Type.__name__ = "OctetString"
_MscLpImaAvailabilityStatus_Object = MibTableColumn
mscLpImaAvailabilityStatus = _MscLpImaAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 4),
    _MscLpImaAvailabilityStatus_Type()
)
mscLpImaAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaAvailabilityStatus.setStatus("mandatory")


class _MscLpImaProceduralStatus_Type(OctetString):
    """Custom type mscLpImaProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpImaProceduralStatus_Type.__name__ = "OctetString"
_MscLpImaProceduralStatus_Object = MibTableColumn
mscLpImaProceduralStatus = _MscLpImaProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 5),
    _MscLpImaProceduralStatus_Type()
)
mscLpImaProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaProceduralStatus.setStatus("mandatory")


class _MscLpImaControlStatus_Type(OctetString):
    """Custom type mscLpImaControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpImaControlStatus_Type.__name__ = "OctetString"
_MscLpImaControlStatus_Object = MibTableColumn
mscLpImaControlStatus = _MscLpImaControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 6),
    _MscLpImaControlStatus_Type()
)
mscLpImaControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaControlStatus.setStatus("mandatory")


class _MscLpImaAlarmStatus_Type(OctetString):
    """Custom type mscLpImaAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_MscLpImaAlarmStatus_Type.__name__ = "OctetString"
_MscLpImaAlarmStatus_Object = MibTableColumn
mscLpImaAlarmStatus = _MscLpImaAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 7),
    _MscLpImaAlarmStatus_Type()
)
mscLpImaAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaAlarmStatus.setStatus("mandatory")


class _MscLpImaStandbyStatus_Type(Integer32):
    """Custom type mscLpImaStandbyStatus based on Integer32"""
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


_MscLpImaStandbyStatus_Type.__name__ = "Integer32"
_MscLpImaStandbyStatus_Object = MibTableColumn
mscLpImaStandbyStatus = _MscLpImaStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 8),
    _MscLpImaStandbyStatus_Type()
)
mscLpImaStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaStandbyStatus.setStatus("mandatory")


class _MscLpImaUnknownStatus_Type(Integer32):
    """Custom type mscLpImaUnknownStatus based on Integer32"""
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


_MscLpImaUnknownStatus_Type.__name__ = "Integer32"
_MscLpImaUnknownStatus_Object = MibTableColumn
mscLpImaUnknownStatus = _MscLpImaUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 22, 14, 1, 9),
    _MscLpImaUnknownStatus_Type()
)
mscLpImaUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpImaUnknownStatus.setStatus("mandatory")
_ImaMIB_ObjectIdentity = ObjectIdentity
imaMIB = _ImaMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115)
)
_ImaGroup_ObjectIdentity = ObjectIdentity
imaGroup = _ImaGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 1)
)
_ImaGroupCA_ObjectIdentity = ObjectIdentity
imaGroupCA = _ImaGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 1, 1)
)
_ImaGroupCA02_ObjectIdentity = ObjectIdentity
imaGroupCA02 = _ImaGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 1, 1, 3)
)
_ImaGroupCA02A_ObjectIdentity = ObjectIdentity
imaGroupCA02A = _ImaGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 1, 1, 3, 2)
)
_ImaCapabilities_ObjectIdentity = ObjectIdentity
imaCapabilities = _ImaCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 3)
)
_ImaCapabilitiesCA_ObjectIdentity = ObjectIdentity
imaCapabilitiesCA = _ImaCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 3, 1)
)
_ImaCapabilitiesCA02_ObjectIdentity = ObjectIdentity
imaCapabilitiesCA02 = _ImaCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 3, 1, 3)
)
_ImaCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
imaCapabilitiesCA02A = _ImaCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 115, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-ImaMIB",
    **{"mscLpDS3Ima": mscLpDS3Ima,
       "mscLpDS3ImaRowStatusTable": mscLpDS3ImaRowStatusTable,
       "mscLpDS3ImaRowStatusEntry": mscLpDS3ImaRowStatusEntry,
       "mscLpDS3ImaRowStatus": mscLpDS3ImaRowStatus,
       "mscLpDS3ImaComponentName": mscLpDS3ImaComponentName,
       "mscLpDS3ImaStorageType": mscLpDS3ImaStorageType,
       "mscLpDS3ImaIndex": mscLpDS3ImaIndex,
       "mscLpDS3ImaTest": mscLpDS3ImaTest,
       "mscLpDS3ImaTestRowStatusTable": mscLpDS3ImaTestRowStatusTable,
       "mscLpDS3ImaTestRowStatusEntry": mscLpDS3ImaTestRowStatusEntry,
       "mscLpDS3ImaTestRowStatus": mscLpDS3ImaTestRowStatus,
       "mscLpDS3ImaTestComponentName": mscLpDS3ImaTestComponentName,
       "mscLpDS3ImaTestStorageType": mscLpDS3ImaTestStorageType,
       "mscLpDS3ImaTestIndex": mscLpDS3ImaTestIndex,
       "mscLpDS3ImaTestStateTable": mscLpDS3ImaTestStateTable,
       "mscLpDS3ImaTestStateEntry": mscLpDS3ImaTestStateEntry,
       "mscLpDS3ImaTestAdminState": mscLpDS3ImaTestAdminState,
       "mscLpDS3ImaTestOperationalState": mscLpDS3ImaTestOperationalState,
       "mscLpDS3ImaTestUsageState": mscLpDS3ImaTestUsageState,
       "mscLpDS3ImaTestSetupTable": mscLpDS3ImaTestSetupTable,
       "mscLpDS3ImaTestSetupEntry": mscLpDS3ImaTestSetupEntry,
       "mscLpDS3ImaTestPurpose": mscLpDS3ImaTestPurpose,
       "mscLpDS3ImaTestType": mscLpDS3ImaTestType,
       "mscLpDS3ImaTestFrmSize": mscLpDS3ImaTestFrmSize,
       "mscLpDS3ImaTestFrmPatternType": mscLpDS3ImaTestFrmPatternType,
       "mscLpDS3ImaTestCustomizedPattern": mscLpDS3ImaTestCustomizedPattern,
       "mscLpDS3ImaTestDataStartDelay": mscLpDS3ImaTestDataStartDelay,
       "mscLpDS3ImaTestDisplayInterval": mscLpDS3ImaTestDisplayInterval,
       "mscLpDS3ImaTestDuration": mscLpDS3ImaTestDuration,
       "mscLpDS3ImaTestResultsTable": mscLpDS3ImaTestResultsTable,
       "mscLpDS3ImaTestResultsEntry": mscLpDS3ImaTestResultsEntry,
       "mscLpDS3ImaTestElapsedTime": mscLpDS3ImaTestElapsedTime,
       "mscLpDS3ImaTestTimeRemaining": mscLpDS3ImaTestTimeRemaining,
       "mscLpDS3ImaTestCauseOfTermination": mscLpDS3ImaTestCauseOfTermination,
       "mscLpDS3ImaTestBitsTx": mscLpDS3ImaTestBitsTx,
       "mscLpDS3ImaTestBytesTx": mscLpDS3ImaTestBytesTx,
       "mscLpDS3ImaTestFrmTx": mscLpDS3ImaTestFrmTx,
       "mscLpDS3ImaTestBitsRx": mscLpDS3ImaTestBitsRx,
       "mscLpDS3ImaTestBytesRx": mscLpDS3ImaTestBytesRx,
       "mscLpDS3ImaTestFrmRx": mscLpDS3ImaTestFrmRx,
       "mscLpDS3ImaTestErroredFrmRx": mscLpDS3ImaTestErroredFrmRx,
       "mscLpDS3ImaTestBitErrorRate": mscLpDS3ImaTestBitErrorRate,
       "mscLpDS3ImaLk": mscLpDS3ImaLk,
       "mscLpDS3ImaLkRowStatusTable": mscLpDS3ImaLkRowStatusTable,
       "mscLpDS3ImaLkRowStatusEntry": mscLpDS3ImaLkRowStatusEntry,
       "mscLpDS3ImaLkRowStatus": mscLpDS3ImaLkRowStatus,
       "mscLpDS3ImaLkComponentName": mscLpDS3ImaLkComponentName,
       "mscLpDS3ImaLkStorageType": mscLpDS3ImaLkStorageType,
       "mscLpDS3ImaLkIndex": mscLpDS3ImaLkIndex,
       "mscLpDS3ImaLkProvTable": mscLpDS3ImaLkProvTable,
       "mscLpDS3ImaLkProvEntry": mscLpDS3ImaLkProvEntry,
       "mscLpDS3ImaLkInterfaceName": mscLpDS3ImaLkInterfaceName,
       "mscLpDS3ImaLkOperTable": mscLpDS3ImaLkOperTable,
       "mscLpDS3ImaLkOperEntry": mscLpDS3ImaLkOperEntry,
       "mscLpDS3ImaLkFailureCause": mscLpDS3ImaLkFailureCause,
       "mscLpDS3ImaLkRemoteDefect": mscLpDS3ImaLkRemoteDefect,
       "mscLpDS3ImaLkRemoteLid": mscLpDS3ImaLkRemoteLid,
       "mscLpDS3ImaLkRelativeDelay": mscLpDS3ImaLkRelativeDelay,
       "mscLpDS3ImaLkLastOifCause": mscLpDS3ImaLkLastOifCause,
       "mscLpDS3ImaLkStatsTable": mscLpDS3ImaLkStatsTable,
       "mscLpDS3ImaLkStatsEntry": mscLpDS3ImaLkStatsEntry,
       "mscLpDS3ImaLkRunningTime": mscLpDS3ImaLkRunningTime,
       "mscLpDS3ImaLkUnavailSecs": mscLpDS3ImaLkUnavailSecs,
       "mscLpDS3ImaLkFailures": mscLpDS3ImaLkFailures,
       "mscLpDS3ImaLkUnusableSec": mscLpDS3ImaLkUnusableSec,
       "mscLpDS3ImaLkSevErroredSec": mscLpDS3ImaLkSevErroredSec,
       "mscLpDS3ImaLkFarEndUnusableSec": mscLpDS3ImaLkFarEndUnusableSec,
       "mscLpDS3ImaLkFarEndSevErroredSec": mscLpDS3ImaLkFarEndSevErroredSec,
       "mscLpDS3ImaLkFarEndUnavailSec": mscLpDS3ImaLkFarEndUnavailSec,
       "mscLpDS3ImaLkIcpViolations": mscLpDS3ImaLkIcpViolations,
       "mscLpDS3ImaLkTxStuffEvents": mscLpDS3ImaLkTxStuffEvents,
       "mscLpDS3ImaLkRxStuffEvents": mscLpDS3ImaLkRxStuffEvents,
       "mscLpDS3ImaLkIdleCellSec": mscLpDS3ImaLkIdleCellSec,
       "mscLpDS3ImaLkStateTable": mscLpDS3ImaLkStateTable,
       "mscLpDS3ImaLkStateEntry": mscLpDS3ImaLkStateEntry,
       "mscLpDS3ImaLkAdminState": mscLpDS3ImaLkAdminState,
       "mscLpDS3ImaLkOperationalState": mscLpDS3ImaLkOperationalState,
       "mscLpDS3ImaLkUsageState": mscLpDS3ImaLkUsageState,
       "mscLpDS3ImaLkAvailabilityStatus": mscLpDS3ImaLkAvailabilityStatus,
       "mscLpDS3ImaLkProceduralStatus": mscLpDS3ImaLkProceduralStatus,
       "mscLpDS3ImaLkControlStatus": mscLpDS3ImaLkControlStatus,
       "mscLpDS3ImaLkAlarmStatus": mscLpDS3ImaLkAlarmStatus,
       "mscLpDS3ImaLkStandbyStatus": mscLpDS3ImaLkStandbyStatus,
       "mscLpDS3ImaLkUnknownStatus": mscLpDS3ImaLkUnknownStatus,
       "mscLpDS3ImaProvTable": mscLpDS3ImaProvTable,
       "mscLpDS3ImaProvEntry": mscLpDS3ImaProvEntry,
       "mscLpDS3ImaLinkSelectionCriterion": mscLpDS3ImaLinkSelectionCriterion,
       "mscLpDS3ImaMaxDiffDelay": mscLpDS3ImaMaxDiffDelay,
       "mscLpDS3ImaLinkRetryTimeout": mscLpDS3ImaLinkRetryTimeout,
       "mscLpDS3ImaApplicationFramerName": mscLpDS3ImaApplicationFramerName,
       "mscLpDS3ImaTransmitClockMode": mscLpDS3ImaTransmitClockMode,
       "mscLpDS3ImaProtocol": mscLpDS3ImaProtocol,
       "mscLpDS3ImaOperTable": mscLpDS3ImaOperTable,
       "mscLpDS3ImaOperEntry": mscLpDS3ImaOperEntry,
       "mscLpDS3ImaFailureCause": mscLpDS3ImaFailureCause,
       "mscLpDS3ImaRemoteDefect": mscLpDS3ImaRemoteDefect,
       "mscLpDS3ImaRemoteLidsConfig": mscLpDS3ImaRemoteLidsConfig,
       "mscLpDS3ImaRemoteLidsActive": mscLpDS3ImaRemoteLidsActive,
       "mscLpDS3ImaCellCapacity": mscLpDS3ImaCellCapacity,
       "mscLpDS3ImaRemoteGid": mscLpDS3ImaRemoteGid,
       "mscLpDS3ImaClockingModeMismatch": mscLpDS3ImaClockingModeMismatch,
       "mscLpDS3ImaStatsTable": mscLpDS3ImaStatsTable,
       "mscLpDS3ImaStatsEntry": mscLpDS3ImaStatsEntry,
       "mscLpDS3ImaRunningTime": mscLpDS3ImaRunningTime,
       "mscLpDS3ImaUnavailSecs": mscLpDS3ImaUnavailSecs,
       "mscLpDS3ImaFailures": mscLpDS3ImaFailures,
       "mscLpDS3ImaReceiveCellUtilization": mscLpDS3ImaReceiveCellUtilization,
       "mscLpDS3ImaTransmitCellUtilization": mscLpDS3ImaTransmitCellUtilization,
       "mscLpDS3ImaCidDataTable": mscLpDS3ImaCidDataTable,
       "mscLpDS3ImaCidDataEntry": mscLpDS3ImaCidDataEntry,
       "mscLpDS3ImaCustomerIdentifier": mscLpDS3ImaCustomerIdentifier,
       "mscLpDS3ImaStateTable": mscLpDS3ImaStateTable,
       "mscLpDS3ImaStateEntry": mscLpDS3ImaStateEntry,
       "mscLpDS3ImaAdminState": mscLpDS3ImaAdminState,
       "mscLpDS3ImaOperationalState": mscLpDS3ImaOperationalState,
       "mscLpDS3ImaUsageState": mscLpDS3ImaUsageState,
       "mscLpDS3ImaAvailabilityStatus": mscLpDS3ImaAvailabilityStatus,
       "mscLpDS3ImaProceduralStatus": mscLpDS3ImaProceduralStatus,
       "mscLpDS3ImaControlStatus": mscLpDS3ImaControlStatus,
       "mscLpDS3ImaAlarmStatus": mscLpDS3ImaAlarmStatus,
       "mscLpDS3ImaStandbyStatus": mscLpDS3ImaStandbyStatus,
       "mscLpDS3ImaUnknownStatus": mscLpDS3ImaUnknownStatus,
       "mscLpIma": mscLpIma,
       "mscLpImaRowStatusTable": mscLpImaRowStatusTable,
       "mscLpImaRowStatusEntry": mscLpImaRowStatusEntry,
       "mscLpImaRowStatus": mscLpImaRowStatus,
       "mscLpImaComponentName": mscLpImaComponentName,
       "mscLpImaStorageType": mscLpImaStorageType,
       "mscLpImaIndex": mscLpImaIndex,
       "mscLpImaTest": mscLpImaTest,
       "mscLpImaTestRowStatusTable": mscLpImaTestRowStatusTable,
       "mscLpImaTestRowStatusEntry": mscLpImaTestRowStatusEntry,
       "mscLpImaTestRowStatus": mscLpImaTestRowStatus,
       "mscLpImaTestComponentName": mscLpImaTestComponentName,
       "mscLpImaTestStorageType": mscLpImaTestStorageType,
       "mscLpImaTestIndex": mscLpImaTestIndex,
       "mscLpImaTestStateTable": mscLpImaTestStateTable,
       "mscLpImaTestStateEntry": mscLpImaTestStateEntry,
       "mscLpImaTestAdminState": mscLpImaTestAdminState,
       "mscLpImaTestOperationalState": mscLpImaTestOperationalState,
       "mscLpImaTestUsageState": mscLpImaTestUsageState,
       "mscLpImaTestSetupTable": mscLpImaTestSetupTable,
       "mscLpImaTestSetupEntry": mscLpImaTestSetupEntry,
       "mscLpImaTestPurpose": mscLpImaTestPurpose,
       "mscLpImaTestType": mscLpImaTestType,
       "mscLpImaTestFrmSize": mscLpImaTestFrmSize,
       "mscLpImaTestFrmPatternType": mscLpImaTestFrmPatternType,
       "mscLpImaTestCustomizedPattern": mscLpImaTestCustomizedPattern,
       "mscLpImaTestDataStartDelay": mscLpImaTestDataStartDelay,
       "mscLpImaTestDisplayInterval": mscLpImaTestDisplayInterval,
       "mscLpImaTestDuration": mscLpImaTestDuration,
       "mscLpImaTestResultsTable": mscLpImaTestResultsTable,
       "mscLpImaTestResultsEntry": mscLpImaTestResultsEntry,
       "mscLpImaTestElapsedTime": mscLpImaTestElapsedTime,
       "mscLpImaTestTimeRemaining": mscLpImaTestTimeRemaining,
       "mscLpImaTestCauseOfTermination": mscLpImaTestCauseOfTermination,
       "mscLpImaTestBitsTx": mscLpImaTestBitsTx,
       "mscLpImaTestBytesTx": mscLpImaTestBytesTx,
       "mscLpImaTestFrmTx": mscLpImaTestFrmTx,
       "mscLpImaTestBitsRx": mscLpImaTestBitsRx,
       "mscLpImaTestBytesRx": mscLpImaTestBytesRx,
       "mscLpImaTestFrmRx": mscLpImaTestFrmRx,
       "mscLpImaTestErroredFrmRx": mscLpImaTestErroredFrmRx,
       "mscLpImaTestBitErrorRate": mscLpImaTestBitErrorRate,
       "mscLpImaLk": mscLpImaLk,
       "mscLpImaLkRowStatusTable": mscLpImaLkRowStatusTable,
       "mscLpImaLkRowStatusEntry": mscLpImaLkRowStatusEntry,
       "mscLpImaLkRowStatus": mscLpImaLkRowStatus,
       "mscLpImaLkComponentName": mscLpImaLkComponentName,
       "mscLpImaLkStorageType": mscLpImaLkStorageType,
       "mscLpImaLkIndex": mscLpImaLkIndex,
       "mscLpImaLkProvTable": mscLpImaLkProvTable,
       "mscLpImaLkProvEntry": mscLpImaLkProvEntry,
       "mscLpImaLkInterfaceName": mscLpImaLkInterfaceName,
       "mscLpImaLkOperTable": mscLpImaLkOperTable,
       "mscLpImaLkOperEntry": mscLpImaLkOperEntry,
       "mscLpImaLkFailureCause": mscLpImaLkFailureCause,
       "mscLpImaLkRemoteDefect": mscLpImaLkRemoteDefect,
       "mscLpImaLkRemoteLid": mscLpImaLkRemoteLid,
       "mscLpImaLkRelativeDelay": mscLpImaLkRelativeDelay,
       "mscLpImaLkLastOifCause": mscLpImaLkLastOifCause,
       "mscLpImaLkStatsTable": mscLpImaLkStatsTable,
       "mscLpImaLkStatsEntry": mscLpImaLkStatsEntry,
       "mscLpImaLkRunningTime": mscLpImaLkRunningTime,
       "mscLpImaLkUnavailSecs": mscLpImaLkUnavailSecs,
       "mscLpImaLkFailures": mscLpImaLkFailures,
       "mscLpImaLkUnusableSec": mscLpImaLkUnusableSec,
       "mscLpImaLkSevErroredSec": mscLpImaLkSevErroredSec,
       "mscLpImaLkFarEndUnusableSec": mscLpImaLkFarEndUnusableSec,
       "mscLpImaLkFarEndSevErroredSec": mscLpImaLkFarEndSevErroredSec,
       "mscLpImaLkFarEndUnavailSec": mscLpImaLkFarEndUnavailSec,
       "mscLpImaLkIcpViolations": mscLpImaLkIcpViolations,
       "mscLpImaLkTxStuffEvents": mscLpImaLkTxStuffEvents,
       "mscLpImaLkRxStuffEvents": mscLpImaLkRxStuffEvents,
       "mscLpImaLkIdleCellSec": mscLpImaLkIdleCellSec,
       "mscLpImaLkStateTable": mscLpImaLkStateTable,
       "mscLpImaLkStateEntry": mscLpImaLkStateEntry,
       "mscLpImaLkAdminState": mscLpImaLkAdminState,
       "mscLpImaLkOperationalState": mscLpImaLkOperationalState,
       "mscLpImaLkUsageState": mscLpImaLkUsageState,
       "mscLpImaLkAvailabilityStatus": mscLpImaLkAvailabilityStatus,
       "mscLpImaLkProceduralStatus": mscLpImaLkProceduralStatus,
       "mscLpImaLkControlStatus": mscLpImaLkControlStatus,
       "mscLpImaLkAlarmStatus": mscLpImaLkAlarmStatus,
       "mscLpImaLkStandbyStatus": mscLpImaLkStandbyStatus,
       "mscLpImaLkUnknownStatus": mscLpImaLkUnknownStatus,
       "mscLpImaProvTable": mscLpImaProvTable,
       "mscLpImaProvEntry": mscLpImaProvEntry,
       "mscLpImaLinkSelectionCriterion": mscLpImaLinkSelectionCriterion,
       "mscLpImaMaxDiffDelay": mscLpImaMaxDiffDelay,
       "mscLpImaLinkRetryTimeout": mscLpImaLinkRetryTimeout,
       "mscLpImaApplicationFramerName": mscLpImaApplicationFramerName,
       "mscLpImaTransmitClockMode": mscLpImaTransmitClockMode,
       "mscLpImaProtocol": mscLpImaProtocol,
       "mscLpImaOperTable": mscLpImaOperTable,
       "mscLpImaOperEntry": mscLpImaOperEntry,
       "mscLpImaFailureCause": mscLpImaFailureCause,
       "mscLpImaRemoteDefect": mscLpImaRemoteDefect,
       "mscLpImaRemoteLidsConfig": mscLpImaRemoteLidsConfig,
       "mscLpImaRemoteLidsActive": mscLpImaRemoteLidsActive,
       "mscLpImaCellCapacity": mscLpImaCellCapacity,
       "mscLpImaRemoteGid": mscLpImaRemoteGid,
       "mscLpImaClockingModeMismatch": mscLpImaClockingModeMismatch,
       "mscLpImaStatsTable": mscLpImaStatsTable,
       "mscLpImaStatsEntry": mscLpImaStatsEntry,
       "mscLpImaRunningTime": mscLpImaRunningTime,
       "mscLpImaUnavailSecs": mscLpImaUnavailSecs,
       "mscLpImaFailures": mscLpImaFailures,
       "mscLpImaReceiveCellUtilization": mscLpImaReceiveCellUtilization,
       "mscLpImaTransmitCellUtilization": mscLpImaTransmitCellUtilization,
       "mscLpImaCidDataTable": mscLpImaCidDataTable,
       "mscLpImaCidDataEntry": mscLpImaCidDataEntry,
       "mscLpImaCustomerIdentifier": mscLpImaCustomerIdentifier,
       "mscLpImaStateTable": mscLpImaStateTable,
       "mscLpImaStateEntry": mscLpImaStateEntry,
       "mscLpImaAdminState": mscLpImaAdminState,
       "mscLpImaOperationalState": mscLpImaOperationalState,
       "mscLpImaUsageState": mscLpImaUsageState,
       "mscLpImaAvailabilityStatus": mscLpImaAvailabilityStatus,
       "mscLpImaProceduralStatus": mscLpImaProceduralStatus,
       "mscLpImaControlStatus": mscLpImaControlStatus,
       "mscLpImaAlarmStatus": mscLpImaAlarmStatus,
       "mscLpImaStandbyStatus": mscLpImaStandbyStatus,
       "mscLpImaUnknownStatus": mscLpImaUnknownStatus,
       "imaMIB": imaMIB,
       "imaGroup": imaGroup,
       "imaGroupCA": imaGroupCA,
       "imaGroupCA02": imaGroupCA02,
       "imaGroupCA02A": imaGroupCA02A,
       "imaCapabilities": imaCapabilities,
       "imaCapabilitiesCA": imaCapabilitiesCA,
       "imaCapabilitiesCA02": imaCapabilitiesCA02,
       "imaCapabilitiesCA02A": imaCapabilitiesCA02A}
)
