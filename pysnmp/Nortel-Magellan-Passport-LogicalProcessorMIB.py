# SNMP MIB module (Nortel-Magellan-Passport-LogicalProcessorMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-LogicalProcessorMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:15 2024
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
 Gauge32,
 Integer32,
 InterfaceIndex,
 PassportCounter64,
 RowPointer,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "InterfaceIndex",
    "PassportCounter64",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 EnterpriseDateAndTime,
 Hex,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "EnterpriseDateAndTime",
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

_Lp_ObjectIdentity = ObjectIdentity
lp = _Lp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12)
)
_LpRowStatusTable_Object = MibTable
lpRowStatusTable = _LpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 1)
)
if mibBuilder.loadTexts:
    lpRowStatusTable.setStatus("mandatory")
_LpRowStatusEntry_Object = MibTableRow
lpRowStatusEntry = _LpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 1, 1)
)
lpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
)
if mibBuilder.loadTexts:
    lpRowStatusEntry.setStatus("mandatory")
_LpRowStatus_Type = RowStatus
_LpRowStatus_Object = MibTableColumn
lpRowStatus = _LpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 1, 1, 1),
    _LpRowStatus_Type()
)
lpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpRowStatus.setStatus("mandatory")
_LpComponentName_Type = DisplayString
_LpComponentName_Object = MibTableColumn
lpComponentName = _LpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 1, 1, 2),
    _LpComponentName_Type()
)
lpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpComponentName.setStatus("mandatory")
_LpStorageType_Type = StorageType
_LpStorageType_Object = MibTableColumn
lpStorageType = _LpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 1, 1, 4),
    _LpStorageType_Type()
)
lpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpStorageType.setStatus("mandatory")


class _LpIndex_Type(Integer32):
    """Custom type lpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LpIndex_Type.__name__ = "Integer32"
_LpIndex_Object = MibTableColumn
lpIndex = _LpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 1, 1, 10),
    _LpIndex_Type()
)
lpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpIndex.setStatus("mandatory")
_LpDS3_ObjectIdentity = ObjectIdentity
lpDS3 = _LpDS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5)
)
_LpDS3RowStatusTable_Object = MibTable
lpDS3RowStatusTable = _LpDS3RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 1)
)
if mibBuilder.loadTexts:
    lpDS3RowStatusTable.setStatus("mandatory")
_LpDS3RowStatusEntry_Object = MibTableRow
lpDS3RowStatusEntry = _LpDS3RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 1, 1)
)
lpDS3RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3RowStatusEntry.setStatus("mandatory")
_LpDS3RowStatus_Type = RowStatus
_LpDS3RowStatus_Object = MibTableColumn
lpDS3RowStatus = _LpDS3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 1, 1, 1),
    _LpDS3RowStatus_Type()
)
lpDS3RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3RowStatus.setStatus("mandatory")
_LpDS3ComponentName_Type = DisplayString
_LpDS3ComponentName_Object = MibTableColumn
lpDS3ComponentName = _LpDS3ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 1, 1, 2),
    _LpDS3ComponentName_Type()
)
lpDS3ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3ComponentName.setStatus("mandatory")
_LpDS3StorageType_Type = StorageType
_LpDS3StorageType_Object = MibTableColumn
lpDS3StorageType = _LpDS3StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 1, 1, 4),
    _LpDS3StorageType_Type()
)
lpDS3StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3StorageType.setStatus("mandatory")


class _LpDS3Index_Type(Integer32):
    """Custom type lpDS3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LpDS3Index_Type.__name__ = "Integer32"
_LpDS3Index_Object = MibTableColumn
lpDS3Index = _LpDS3Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 1, 1, 10),
    _LpDS3Index_Type()
)
lpDS3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3Index.setStatus("mandatory")
_LpDS3Test_ObjectIdentity = ObjectIdentity
lpDS3Test = _LpDS3Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2)
)
_LpDS3TestRowStatusTable_Object = MibTable
lpDS3TestRowStatusTable = _LpDS3TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lpDS3TestRowStatusTable.setStatus("mandatory")
_LpDS3TestRowStatusEntry_Object = MibTableRow
lpDS3TestRowStatusEntry = _LpDS3TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 1, 1)
)
lpDS3TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3TestRowStatusEntry.setStatus("mandatory")
_LpDS3TestRowStatus_Type = RowStatus
_LpDS3TestRowStatus_Object = MibTableColumn
lpDS3TestRowStatus = _LpDS3TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 1, 1, 1),
    _LpDS3TestRowStatus_Type()
)
lpDS3TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestRowStatus.setStatus("mandatory")
_LpDS3TestComponentName_Type = DisplayString
_LpDS3TestComponentName_Object = MibTableColumn
lpDS3TestComponentName = _LpDS3TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 1, 1, 2),
    _LpDS3TestComponentName_Type()
)
lpDS3TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestComponentName.setStatus("mandatory")
_LpDS3TestStorageType_Type = StorageType
_LpDS3TestStorageType_Object = MibTableColumn
lpDS3TestStorageType = _LpDS3TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 1, 1, 4),
    _LpDS3TestStorageType_Type()
)
lpDS3TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestStorageType.setStatus("mandatory")
_LpDS3TestIndex_Type = NonReplicated
_LpDS3TestIndex_Object = MibTableColumn
lpDS3TestIndex = _LpDS3TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 1, 1, 10),
    _LpDS3TestIndex_Type()
)
lpDS3TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3TestIndex.setStatus("mandatory")
_LpDS3TestStateTable_Object = MibTable
lpDS3TestStateTable = _LpDS3TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 10)
)
if mibBuilder.loadTexts:
    lpDS3TestStateTable.setStatus("mandatory")
_LpDS3TestStateEntry_Object = MibTableRow
lpDS3TestStateEntry = _LpDS3TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 10, 1)
)
lpDS3TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3TestStateEntry.setStatus("mandatory")


class _LpDS3TestAdminState_Type(Integer32):
    """Custom type lpDS3TestAdminState based on Integer32"""
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


_LpDS3TestAdminState_Type.__name__ = "Integer32"
_LpDS3TestAdminState_Object = MibTableColumn
lpDS3TestAdminState = _LpDS3TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 10, 1, 1),
    _LpDS3TestAdminState_Type()
)
lpDS3TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestAdminState.setStatus("mandatory")


class _LpDS3TestOperationalState_Type(Integer32):
    """Custom type lpDS3TestOperationalState based on Integer32"""
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


_LpDS3TestOperationalState_Type.__name__ = "Integer32"
_LpDS3TestOperationalState_Object = MibTableColumn
lpDS3TestOperationalState = _LpDS3TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 10, 1, 2),
    _LpDS3TestOperationalState_Type()
)
lpDS3TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestOperationalState.setStatus("mandatory")


class _LpDS3TestUsageState_Type(Integer32):
    """Custom type lpDS3TestUsageState based on Integer32"""
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


_LpDS3TestUsageState_Type.__name__ = "Integer32"
_LpDS3TestUsageState_Object = MibTableColumn
lpDS3TestUsageState = _LpDS3TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 10, 1, 3),
    _LpDS3TestUsageState_Type()
)
lpDS3TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestUsageState.setStatus("mandatory")
_LpDS3TestSetupTable_Object = MibTable
lpDS3TestSetupTable = _LpDS3TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11)
)
if mibBuilder.loadTexts:
    lpDS3TestSetupTable.setStatus("mandatory")
_LpDS3TestSetupEntry_Object = MibTableRow
lpDS3TestSetupEntry = _LpDS3TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1)
)
lpDS3TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3TestSetupEntry.setStatus("mandatory")


class _LpDS3TestPurpose_Type(AsciiString):
    """Custom type lpDS3TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpDS3TestPurpose_Type.__name__ = "AsciiString"
_LpDS3TestPurpose_Object = MibTableColumn
lpDS3TestPurpose = _LpDS3TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 1),
    _LpDS3TestPurpose_Type()
)
lpDS3TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestPurpose.setStatus("mandatory")


class _LpDS3TestType_Type(Integer32):
    """Custom type lpDS3TestType based on Integer32"""
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


_LpDS3TestType_Type.__name__ = "Integer32"
_LpDS3TestType_Object = MibTableColumn
lpDS3TestType = _LpDS3TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 2),
    _LpDS3TestType_Type()
)
lpDS3TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestType.setStatus("mandatory")


class _LpDS3TestFrmSize_Type(Unsigned32):
    """Custom type lpDS3TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpDS3TestFrmSize_Type.__name__ = "Unsigned32"
_LpDS3TestFrmSize_Object = MibTableColumn
lpDS3TestFrmSize = _LpDS3TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 3),
    _LpDS3TestFrmSize_Type()
)
lpDS3TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestFrmSize.setStatus("mandatory")


class _LpDS3TestFrmPatternType_Type(Integer32):
    """Custom type lpDS3TestFrmPatternType based on Integer32"""
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


_LpDS3TestFrmPatternType_Type.__name__ = "Integer32"
_LpDS3TestFrmPatternType_Object = MibTableColumn
lpDS3TestFrmPatternType = _LpDS3TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 4),
    _LpDS3TestFrmPatternType_Type()
)
lpDS3TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestFrmPatternType.setStatus("mandatory")


class _LpDS3TestCustomizedPattern_Type(Hex):
    """Custom type lpDS3TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS3TestCustomizedPattern_Type.__name__ = "Hex"
_LpDS3TestCustomizedPattern_Object = MibTableColumn
lpDS3TestCustomizedPattern = _LpDS3TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 5),
    _LpDS3TestCustomizedPattern_Type()
)
lpDS3TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestCustomizedPattern.setStatus("mandatory")


class _LpDS3TestDataStartDelay_Type(Unsigned32):
    """Custom type lpDS3TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpDS3TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpDS3TestDataStartDelay_Object = MibTableColumn
lpDS3TestDataStartDelay = _LpDS3TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 6),
    _LpDS3TestDataStartDelay_Type()
)
lpDS3TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestDataStartDelay.setStatus("mandatory")


class _LpDS3TestDisplayInterval_Type(Unsigned32):
    """Custom type lpDS3TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpDS3TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpDS3TestDisplayInterval_Object = MibTableColumn
lpDS3TestDisplayInterval = _LpDS3TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 7),
    _LpDS3TestDisplayInterval_Type()
)
lpDS3TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestDisplayInterval.setStatus("mandatory")


class _LpDS3TestDuration_Type(Unsigned32):
    """Custom type lpDS3TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpDS3TestDuration_Type.__name__ = "Unsigned32"
_LpDS3TestDuration_Object = MibTableColumn
lpDS3TestDuration = _LpDS3TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 11, 1, 8),
    _LpDS3TestDuration_Type()
)
lpDS3TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3TestDuration.setStatus("mandatory")
_LpDS3TestResultsTable_Object = MibTable
lpDS3TestResultsTable = _LpDS3TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12)
)
if mibBuilder.loadTexts:
    lpDS3TestResultsTable.setStatus("mandatory")
_LpDS3TestResultsEntry_Object = MibTableRow
lpDS3TestResultsEntry = _LpDS3TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1)
)
lpDS3TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3TestResultsEntry.setStatus("mandatory")
_LpDS3TestElapsedTime_Type = Counter32
_LpDS3TestElapsedTime_Object = MibTableColumn
lpDS3TestElapsedTime = _LpDS3TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 1),
    _LpDS3TestElapsedTime_Type()
)
lpDS3TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestElapsedTime.setStatus("mandatory")


class _LpDS3TestTimeRemaining_Type(Unsigned32):
    """Custom type lpDS3TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS3TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpDS3TestTimeRemaining_Object = MibTableColumn
lpDS3TestTimeRemaining = _LpDS3TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 2),
    _LpDS3TestTimeRemaining_Type()
)
lpDS3TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestTimeRemaining.setStatus("mandatory")


class _LpDS3TestCauseOfTermination_Type(Integer32):
    """Custom type lpDS3TestCauseOfTermination based on Integer32"""
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


_LpDS3TestCauseOfTermination_Type.__name__ = "Integer32"
_LpDS3TestCauseOfTermination_Object = MibTableColumn
lpDS3TestCauseOfTermination = _LpDS3TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 3),
    _LpDS3TestCauseOfTermination_Type()
)
lpDS3TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestCauseOfTermination.setStatus("mandatory")
_LpDS3TestBitsTx_Type = PassportCounter64
_LpDS3TestBitsTx_Object = MibTableColumn
lpDS3TestBitsTx = _LpDS3TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 4),
    _LpDS3TestBitsTx_Type()
)
lpDS3TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestBitsTx.setStatus("mandatory")
_LpDS3TestBytesTx_Type = PassportCounter64
_LpDS3TestBytesTx_Object = MibTableColumn
lpDS3TestBytesTx = _LpDS3TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 5),
    _LpDS3TestBytesTx_Type()
)
lpDS3TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestBytesTx.setStatus("mandatory")
_LpDS3TestFrmTx_Type = PassportCounter64
_LpDS3TestFrmTx_Object = MibTableColumn
lpDS3TestFrmTx = _LpDS3TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 6),
    _LpDS3TestFrmTx_Type()
)
lpDS3TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestFrmTx.setStatus("mandatory")
_LpDS3TestBitsRx_Type = PassportCounter64
_LpDS3TestBitsRx_Object = MibTableColumn
lpDS3TestBitsRx = _LpDS3TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 7),
    _LpDS3TestBitsRx_Type()
)
lpDS3TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestBitsRx.setStatus("mandatory")
_LpDS3TestBytesRx_Type = PassportCounter64
_LpDS3TestBytesRx_Object = MibTableColumn
lpDS3TestBytesRx = _LpDS3TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 8),
    _LpDS3TestBytesRx_Type()
)
lpDS3TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestBytesRx.setStatus("mandatory")
_LpDS3TestFrmRx_Type = PassportCounter64
_LpDS3TestFrmRx_Object = MibTableColumn
lpDS3TestFrmRx = _LpDS3TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 9),
    _LpDS3TestFrmRx_Type()
)
lpDS3TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestFrmRx.setStatus("mandatory")
_LpDS3TestErroredFrmRx_Type = PassportCounter64
_LpDS3TestErroredFrmRx_Object = MibTableColumn
lpDS3TestErroredFrmRx = _LpDS3TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 10),
    _LpDS3TestErroredFrmRx_Type()
)
lpDS3TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestErroredFrmRx.setStatus("mandatory")


class _LpDS3TestBitErrorRate_Type(AsciiString):
    """Custom type lpDS3TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpDS3TestBitErrorRate_Type.__name__ = "AsciiString"
_LpDS3TestBitErrorRate_Object = MibTableColumn
lpDS3TestBitErrorRate = _LpDS3TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 2, 12, 1, 11),
    _LpDS3TestBitErrorRate_Type()
)
lpDS3TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TestBitErrorRate.setStatus("mandatory")
_LpDS3CBit_ObjectIdentity = ObjectIdentity
lpDS3CBit = _LpDS3CBit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3)
)
_LpDS3CBitRowStatusTable_Object = MibTable
lpDS3CBitRowStatusTable = _LpDS3CBitRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lpDS3CBitRowStatusTable.setStatus("mandatory")
_LpDS3CBitRowStatusEntry_Object = MibTableRow
lpDS3CBitRowStatusEntry = _LpDS3CBitRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 1, 1)
)
lpDS3CBitRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3CBitIndex"),
)
if mibBuilder.loadTexts:
    lpDS3CBitRowStatusEntry.setStatus("mandatory")
_LpDS3CBitRowStatus_Type = RowStatus
_LpDS3CBitRowStatus_Object = MibTableColumn
lpDS3CBitRowStatus = _LpDS3CBitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 1, 1, 1),
    _LpDS3CBitRowStatus_Type()
)
lpDS3CBitRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitRowStatus.setStatus("mandatory")
_LpDS3CBitComponentName_Type = DisplayString
_LpDS3CBitComponentName_Object = MibTableColumn
lpDS3CBitComponentName = _LpDS3CBitComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 1, 1, 2),
    _LpDS3CBitComponentName_Type()
)
lpDS3CBitComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitComponentName.setStatus("mandatory")
_LpDS3CBitStorageType_Type = StorageType
_LpDS3CBitStorageType_Object = MibTableColumn
lpDS3CBitStorageType = _LpDS3CBitStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 1, 1, 4),
    _LpDS3CBitStorageType_Type()
)
lpDS3CBitStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitStorageType.setStatus("mandatory")
_LpDS3CBitIndex_Type = NonReplicated
_LpDS3CBitIndex_Object = MibTableColumn
lpDS3CBitIndex = _LpDS3CBitIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 1, 1, 10),
    _LpDS3CBitIndex_Type()
)
lpDS3CBitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3CBitIndex.setStatus("mandatory")
_LpDS3CBitOperationalTable_Object = MibTable
lpDS3CBitOperationalTable = _LpDS3CBitOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 10)
)
if mibBuilder.loadTexts:
    lpDS3CBitOperationalTable.setStatus("mandatory")
_LpDS3CBitOperationalEntry_Object = MibTableRow
lpDS3CBitOperationalEntry = _LpDS3CBitOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 10, 1)
)
lpDS3CBitOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3CBitIndex"),
)
if mibBuilder.loadTexts:
    lpDS3CBitOperationalEntry.setStatus("mandatory")


class _LpDS3CBitFarEndAlarm_Type(Integer32):
    """Custom type lpDS3CBitFarEndAlarm based on Integer32"""
    defaultValue = 5

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
        *(("ais", 3),
          ("equipmentFailure", 0),
          ("idle", 4),
          ("los", 1),
          ("none", 5),
          ("sef", 2))
    )


_LpDS3CBitFarEndAlarm_Type.__name__ = "Integer32"
_LpDS3CBitFarEndAlarm_Object = MibTableColumn
lpDS3CBitFarEndAlarm = _LpDS3CBitFarEndAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 10, 1, 1),
    _LpDS3CBitFarEndAlarm_Type()
)
lpDS3CBitFarEndAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndAlarm.setStatus("mandatory")


class _LpDS3CBitLoopedbackToFarEnd_Type(OctetString):
    """Custom type lpDS3CBitLoopedbackToFarEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpDS3CBitLoopedbackToFarEnd_Type.__name__ = "OctetString"
_LpDS3CBitLoopedbackToFarEnd_Object = MibTableColumn
lpDS3CBitLoopedbackToFarEnd = _LpDS3CBitLoopedbackToFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 10, 1, 2),
    _LpDS3CBitLoopedbackToFarEnd_Type()
)
lpDS3CBitLoopedbackToFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitLoopedbackToFarEnd.setStatus("mandatory")


class _LpDS3CBitLoopbackAtFarEndRequested_Type(OctetString):
    """Custom type lpDS3CBitLoopbackAtFarEndRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpDS3CBitLoopbackAtFarEndRequested_Type.__name__ = "OctetString"
_LpDS3CBitLoopbackAtFarEndRequested_Object = MibTableColumn
lpDS3CBitLoopbackAtFarEndRequested = _LpDS3CBitLoopbackAtFarEndRequested_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 10, 1, 3),
    _LpDS3CBitLoopbackAtFarEndRequested_Type()
)
lpDS3CBitLoopbackAtFarEndRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitLoopbackAtFarEndRequested.setStatus("mandatory")
_LpDS3CBitStatsTable_Object = MibTable
lpDS3CBitStatsTable = _LpDS3CBitStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11)
)
if mibBuilder.loadTexts:
    lpDS3CBitStatsTable.setStatus("mandatory")
_LpDS3CBitStatsEntry_Object = MibTableRow
lpDS3CBitStatsEntry = _LpDS3CBitStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1)
)
lpDS3CBitStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3CBitIndex"),
)
if mibBuilder.loadTexts:
    lpDS3CBitStatsEntry.setStatus("mandatory")
_LpDS3CBitCbitErrorFreeSec_Type = Counter32
_LpDS3CBitCbitErrorFreeSec_Object = MibTableColumn
lpDS3CBitCbitErrorFreeSec = _LpDS3CBitCbitErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 1),
    _LpDS3CBitCbitErrorFreeSec_Type()
)
lpDS3CBitCbitErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitCbitErrorFreeSec.setStatus("mandatory")
_LpDS3CBitCbitCodeViolations_Type = Counter32
_LpDS3CBitCbitCodeViolations_Object = MibTableColumn
lpDS3CBitCbitCodeViolations = _LpDS3CBitCbitCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 2),
    _LpDS3CBitCbitCodeViolations_Type()
)
lpDS3CBitCbitCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitCbitCodeViolations.setStatus("mandatory")
_LpDS3CBitCbitErroredSec_Type = Counter32
_LpDS3CBitCbitErroredSec_Object = MibTableColumn
lpDS3CBitCbitErroredSec = _LpDS3CBitCbitErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 3),
    _LpDS3CBitCbitErroredSec_Type()
)
lpDS3CBitCbitErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitCbitErroredSec.setStatus("mandatory")
_LpDS3CBitCbitSevErroredSec_Type = Counter32
_LpDS3CBitCbitSevErroredSec_Object = MibTableColumn
lpDS3CBitCbitSevErroredSec = _LpDS3CBitCbitSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 4),
    _LpDS3CBitCbitSevErroredSec_Type()
)
lpDS3CBitCbitSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitCbitSevErroredSec.setStatus("mandatory")
_LpDS3CBitCbitUnavailSec_Type = Counter32
_LpDS3CBitCbitUnavailSec_Object = MibTableColumn
lpDS3CBitCbitUnavailSec = _LpDS3CBitCbitUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 5),
    _LpDS3CBitCbitUnavailSec_Type()
)
lpDS3CBitCbitUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitCbitUnavailSec.setStatus("mandatory")
_LpDS3CBitFarEndErrorFreeSec_Type = Counter32
_LpDS3CBitFarEndErrorFreeSec_Object = MibTableColumn
lpDS3CBitFarEndErrorFreeSec = _LpDS3CBitFarEndErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 6),
    _LpDS3CBitFarEndErrorFreeSec_Type()
)
lpDS3CBitFarEndErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndErrorFreeSec.setStatus("mandatory")
_LpDS3CBitFarEndCodeViolations_Type = Counter32
_LpDS3CBitFarEndCodeViolations_Object = MibTableColumn
lpDS3CBitFarEndCodeViolations = _LpDS3CBitFarEndCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 7),
    _LpDS3CBitFarEndCodeViolations_Type()
)
lpDS3CBitFarEndCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndCodeViolations.setStatus("mandatory")
_LpDS3CBitFarEndErroredSec_Type = Counter32
_LpDS3CBitFarEndErroredSec_Object = MibTableColumn
lpDS3CBitFarEndErroredSec = _LpDS3CBitFarEndErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 8),
    _LpDS3CBitFarEndErroredSec_Type()
)
lpDS3CBitFarEndErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndErroredSec.setStatus("mandatory")
_LpDS3CBitFarEndSevErroredSec_Type = Counter32
_LpDS3CBitFarEndSevErroredSec_Object = MibTableColumn
lpDS3CBitFarEndSevErroredSec = _LpDS3CBitFarEndSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 9),
    _LpDS3CBitFarEndSevErroredSec_Type()
)
lpDS3CBitFarEndSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndSevErroredSec.setStatus("mandatory")
_LpDS3CBitFarEndSefAisSec_Type = Counter32
_LpDS3CBitFarEndSefAisSec_Object = MibTableColumn
lpDS3CBitFarEndSefAisSec = _LpDS3CBitFarEndSefAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 10),
    _LpDS3CBitFarEndSefAisSec_Type()
)
lpDS3CBitFarEndSefAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndSefAisSec.setStatus("mandatory")
_LpDS3CBitFarEndUnavailSec_Type = Counter32
_LpDS3CBitFarEndUnavailSec_Object = MibTableColumn
lpDS3CBitFarEndUnavailSec = _LpDS3CBitFarEndUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 11),
    _LpDS3CBitFarEndUnavailSec_Type()
)
lpDS3CBitFarEndUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndUnavailSec.setStatus("mandatory")
_LpDS3CBitFarEndFailures_Type = Counter32
_LpDS3CBitFarEndFailures_Object = MibTableColumn
lpDS3CBitFarEndFailures = _LpDS3CBitFarEndFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 3, 11, 1, 12),
    _LpDS3CBitFarEndFailures_Type()
)
lpDS3CBitFarEndFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CBitFarEndFailures.setStatus("mandatory")
_LpDS3Plcp_ObjectIdentity = ObjectIdentity
lpDS3Plcp = _LpDS3Plcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4)
)
_LpDS3PlcpRowStatusTable_Object = MibTable
lpDS3PlcpRowStatusTable = _LpDS3PlcpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 1)
)
if mibBuilder.loadTexts:
    lpDS3PlcpRowStatusTable.setStatus("mandatory")
_LpDS3PlcpRowStatusEntry_Object = MibTableRow
lpDS3PlcpRowStatusEntry = _LpDS3PlcpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 1, 1)
)
lpDS3PlcpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3PlcpIndex"),
)
if mibBuilder.loadTexts:
    lpDS3PlcpRowStatusEntry.setStatus("mandatory")
_LpDS3PlcpRowStatus_Type = RowStatus
_LpDS3PlcpRowStatus_Object = MibTableColumn
lpDS3PlcpRowStatus = _LpDS3PlcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 1, 1, 1),
    _LpDS3PlcpRowStatus_Type()
)
lpDS3PlcpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpRowStatus.setStatus("mandatory")
_LpDS3PlcpComponentName_Type = DisplayString
_LpDS3PlcpComponentName_Object = MibTableColumn
lpDS3PlcpComponentName = _LpDS3PlcpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 1, 1, 2),
    _LpDS3PlcpComponentName_Type()
)
lpDS3PlcpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpComponentName.setStatus("mandatory")
_LpDS3PlcpStorageType_Type = StorageType
_LpDS3PlcpStorageType_Object = MibTableColumn
lpDS3PlcpStorageType = _LpDS3PlcpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 1, 1, 4),
    _LpDS3PlcpStorageType_Type()
)
lpDS3PlcpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpStorageType.setStatus("mandatory")
_LpDS3PlcpIndex_Type = NonReplicated
_LpDS3PlcpIndex_Object = MibTableColumn
lpDS3PlcpIndex = _LpDS3PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 1, 1, 10),
    _LpDS3PlcpIndex_Type()
)
lpDS3PlcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3PlcpIndex.setStatus("mandatory")
_LpDS3PlcpOperationalTable_Object = MibTable
lpDS3PlcpOperationalTable = _LpDS3PlcpOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 10)
)
if mibBuilder.loadTexts:
    lpDS3PlcpOperationalTable.setStatus("mandatory")
_LpDS3PlcpOperationalEntry_Object = MibTableRow
lpDS3PlcpOperationalEntry = _LpDS3PlcpOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 10, 1)
)
lpDS3PlcpOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3PlcpIndex"),
)
if mibBuilder.loadTexts:
    lpDS3PlcpOperationalEntry.setStatus("mandatory")


class _LpDS3PlcpLofAlarm_Type(Integer32):
    """Custom type lpDS3PlcpLofAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3PlcpLofAlarm_Type.__name__ = "Integer32"
_LpDS3PlcpLofAlarm_Object = MibTableColumn
lpDS3PlcpLofAlarm = _LpDS3PlcpLofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 10, 1, 1),
    _LpDS3PlcpLofAlarm_Type()
)
lpDS3PlcpLofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpLofAlarm.setStatus("mandatory")


class _LpDS3PlcpRxRaiAlarm_Type(Integer32):
    """Custom type lpDS3PlcpRxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3PlcpRxRaiAlarm_Type.__name__ = "Integer32"
_LpDS3PlcpRxRaiAlarm_Object = MibTableColumn
lpDS3PlcpRxRaiAlarm = _LpDS3PlcpRxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 10, 1, 2),
    _LpDS3PlcpRxRaiAlarm_Type()
)
lpDS3PlcpRxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpRxRaiAlarm.setStatus("mandatory")
_LpDS3PlcpStatsTable_Object = MibTable
lpDS3PlcpStatsTable = _LpDS3PlcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11)
)
if mibBuilder.loadTexts:
    lpDS3PlcpStatsTable.setStatus("mandatory")
_LpDS3PlcpStatsEntry_Object = MibTableRow
lpDS3PlcpStatsEntry = _LpDS3PlcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1)
)
lpDS3PlcpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3PlcpIndex"),
)
if mibBuilder.loadTexts:
    lpDS3PlcpStatsEntry.setStatus("mandatory")
_LpDS3PlcpErrorFreeSec_Type = Counter32
_LpDS3PlcpErrorFreeSec_Object = MibTableColumn
lpDS3PlcpErrorFreeSec = _LpDS3PlcpErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 1),
    _LpDS3PlcpErrorFreeSec_Type()
)
lpDS3PlcpErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpErrorFreeSec.setStatus("mandatory")
_LpDS3PlcpCodingViolations_Type = Counter32
_LpDS3PlcpCodingViolations_Object = MibTableColumn
lpDS3PlcpCodingViolations = _LpDS3PlcpCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 2),
    _LpDS3PlcpCodingViolations_Type()
)
lpDS3PlcpCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpCodingViolations.setStatus("mandatory")
_LpDS3PlcpErroredSec_Type = Counter32
_LpDS3PlcpErroredSec_Object = MibTableColumn
lpDS3PlcpErroredSec = _LpDS3PlcpErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 3),
    _LpDS3PlcpErroredSec_Type()
)
lpDS3PlcpErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpErroredSec.setStatus("mandatory")
_LpDS3PlcpSevErroredSec_Type = Counter32
_LpDS3PlcpSevErroredSec_Object = MibTableColumn
lpDS3PlcpSevErroredSec = _LpDS3PlcpSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 4),
    _LpDS3PlcpSevErroredSec_Type()
)
lpDS3PlcpSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpSevErroredSec.setStatus("mandatory")
_LpDS3PlcpSevErroredFramingSec_Type = Counter32
_LpDS3PlcpSevErroredFramingSec_Object = MibTableColumn
lpDS3PlcpSevErroredFramingSec = _LpDS3PlcpSevErroredFramingSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 5),
    _LpDS3PlcpSevErroredFramingSec_Type()
)
lpDS3PlcpSevErroredFramingSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpSevErroredFramingSec.setStatus("mandatory")
_LpDS3PlcpUnavailSec_Type = Counter32
_LpDS3PlcpUnavailSec_Object = MibTableColumn
lpDS3PlcpUnavailSec = _LpDS3PlcpUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 6),
    _LpDS3PlcpUnavailSec_Type()
)
lpDS3PlcpUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpUnavailSec.setStatus("mandatory")
_LpDS3PlcpFarEndErrorFreeSec_Type = Counter32
_LpDS3PlcpFarEndErrorFreeSec_Object = MibTableColumn
lpDS3PlcpFarEndErrorFreeSec = _LpDS3PlcpFarEndErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 7),
    _LpDS3PlcpFarEndErrorFreeSec_Type()
)
lpDS3PlcpFarEndErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpFarEndErrorFreeSec.setStatus("mandatory")
_LpDS3PlcpFarEndCodingViolations_Type = Counter32
_LpDS3PlcpFarEndCodingViolations_Object = MibTableColumn
lpDS3PlcpFarEndCodingViolations = _LpDS3PlcpFarEndCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 8),
    _LpDS3PlcpFarEndCodingViolations_Type()
)
lpDS3PlcpFarEndCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpFarEndCodingViolations.setStatus("mandatory")
_LpDS3PlcpFarEndErroredSec_Type = Counter32
_LpDS3PlcpFarEndErroredSec_Object = MibTableColumn
lpDS3PlcpFarEndErroredSec = _LpDS3PlcpFarEndErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 9),
    _LpDS3PlcpFarEndErroredSec_Type()
)
lpDS3PlcpFarEndErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpFarEndErroredSec.setStatus("mandatory")
_LpDS3PlcpFarEndSevErroredSec_Type = Counter32
_LpDS3PlcpFarEndSevErroredSec_Object = MibTableColumn
lpDS3PlcpFarEndSevErroredSec = _LpDS3PlcpFarEndSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 10),
    _LpDS3PlcpFarEndSevErroredSec_Type()
)
lpDS3PlcpFarEndSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpFarEndSevErroredSec.setStatus("mandatory")
_LpDS3PlcpFarEndUnavailableSec_Type = Counter32
_LpDS3PlcpFarEndUnavailableSec_Object = MibTableColumn
lpDS3PlcpFarEndUnavailableSec = _LpDS3PlcpFarEndUnavailableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 4, 11, 1, 11),
    _LpDS3PlcpFarEndUnavailableSec_Type()
)
lpDS3PlcpFarEndUnavailableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PlcpFarEndUnavailableSec.setStatus("mandatory")
_LpDS3Cell_ObjectIdentity = ObjectIdentity
lpDS3Cell = _LpDS3Cell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5)
)
_LpDS3CellRowStatusTable_Object = MibTable
lpDS3CellRowStatusTable = _LpDS3CellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 1)
)
if mibBuilder.loadTexts:
    lpDS3CellRowStatusTable.setStatus("mandatory")
_LpDS3CellRowStatusEntry_Object = MibTableRow
lpDS3CellRowStatusEntry = _LpDS3CellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 1, 1)
)
lpDS3CellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3CellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3CellRowStatusEntry.setStatus("mandatory")
_LpDS3CellRowStatus_Type = RowStatus
_LpDS3CellRowStatus_Object = MibTableColumn
lpDS3CellRowStatus = _LpDS3CellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 1, 1, 1),
    _LpDS3CellRowStatus_Type()
)
lpDS3CellRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3CellRowStatus.setStatus("mandatory")
_LpDS3CellComponentName_Type = DisplayString
_LpDS3CellComponentName_Object = MibTableColumn
lpDS3CellComponentName = _LpDS3CellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 1, 1, 2),
    _LpDS3CellComponentName_Type()
)
lpDS3CellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellComponentName.setStatus("mandatory")
_LpDS3CellStorageType_Type = StorageType
_LpDS3CellStorageType_Object = MibTableColumn
lpDS3CellStorageType = _LpDS3CellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 1, 1, 4),
    _LpDS3CellStorageType_Type()
)
lpDS3CellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellStorageType.setStatus("mandatory")
_LpDS3CellIndex_Type = NonReplicated
_LpDS3CellIndex_Object = MibTableColumn
lpDS3CellIndex = _LpDS3CellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 1, 1, 10),
    _LpDS3CellIndex_Type()
)
lpDS3CellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3CellIndex.setStatus("mandatory")
_LpDS3CellProvTable_Object = MibTable
lpDS3CellProvTable = _LpDS3CellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 10)
)
if mibBuilder.loadTexts:
    lpDS3CellProvTable.setStatus("mandatory")
_LpDS3CellProvEntry_Object = MibTableRow
lpDS3CellProvEntry = _LpDS3CellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 10, 1)
)
lpDS3CellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3CellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3CellProvEntry.setStatus("mandatory")


class _LpDS3CellAlarmActDelay_Type(Unsigned32):
    """Custom type lpDS3CellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpDS3CellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpDS3CellAlarmActDelay_Object = MibTableColumn
lpDS3CellAlarmActDelay = _LpDS3CellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 10, 1, 1),
    _LpDS3CellAlarmActDelay_Type()
)
lpDS3CellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3CellAlarmActDelay.setStatus("mandatory")


class _LpDS3CellScrambleCellPayload_Type(Integer32):
    """Custom type lpDS3CellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS3CellScrambleCellPayload_Type.__name__ = "Integer32"
_LpDS3CellScrambleCellPayload_Object = MibTableColumn
lpDS3CellScrambleCellPayload = _LpDS3CellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 10, 1, 2),
    _LpDS3CellScrambleCellPayload_Type()
)
lpDS3CellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3CellScrambleCellPayload.setStatus("mandatory")


class _LpDS3CellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpDS3CellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS3CellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpDS3CellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpDS3CellCorrectSingleBitHeaderErrors = _LpDS3CellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 10, 1, 3),
    _LpDS3CellCorrectSingleBitHeaderErrors_Type()
)
lpDS3CellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3CellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpDS3CellOperTable_Object = MibTable
lpDS3CellOperTable = _LpDS3CellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 11)
)
if mibBuilder.loadTexts:
    lpDS3CellOperTable.setStatus("mandatory")
_LpDS3CellOperEntry_Object = MibTableRow
lpDS3CellOperEntry = _LpDS3CellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 11, 1)
)
lpDS3CellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3CellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3CellOperEntry.setStatus("mandatory")


class _LpDS3CellLcdAlarm_Type(Integer32):
    """Custom type lpDS3CellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3CellLcdAlarm_Type.__name__ = "Integer32"
_LpDS3CellLcdAlarm_Object = MibTableColumn
lpDS3CellLcdAlarm = _LpDS3CellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 11, 1, 1),
    _LpDS3CellLcdAlarm_Type()
)
lpDS3CellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellLcdAlarm.setStatus("mandatory")
_LpDS3CellStatsTable_Object = MibTable
lpDS3CellStatsTable = _LpDS3CellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 12)
)
if mibBuilder.loadTexts:
    lpDS3CellStatsTable.setStatus("mandatory")
_LpDS3CellStatsEntry_Object = MibTableRow
lpDS3CellStatsEntry = _LpDS3CellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 12, 1)
)
lpDS3CellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3CellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3CellStatsEntry.setStatus("mandatory")
_LpDS3CellUncorrectableHecErrors_Type = Counter32
_LpDS3CellUncorrectableHecErrors_Object = MibTableColumn
lpDS3CellUncorrectableHecErrors = _LpDS3CellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 12, 1, 1),
    _LpDS3CellUncorrectableHecErrors_Type()
)
lpDS3CellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellUncorrectableHecErrors.setStatus("mandatory")
_LpDS3CellSevErroredSec_Type = Counter32
_LpDS3CellSevErroredSec_Object = MibTableColumn
lpDS3CellSevErroredSec = _LpDS3CellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 12, 1, 2),
    _LpDS3CellSevErroredSec_Type()
)
lpDS3CellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellSevErroredSec.setStatus("mandatory")


class _LpDS3CellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpDS3CellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpDS3CellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpDS3CellReceiveCellUtilization_Object = MibTableColumn
lpDS3CellReceiveCellUtilization = _LpDS3CellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 12, 1, 3),
    _LpDS3CellReceiveCellUtilization_Type()
)
lpDS3CellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellReceiveCellUtilization.setStatus("mandatory")


class _LpDS3CellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpDS3CellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpDS3CellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpDS3CellTransmitCellUtilization_Object = MibTableColumn
lpDS3CellTransmitCellUtilization = _LpDS3CellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 12, 1, 4),
    _LpDS3CellTransmitCellUtilization_Type()
)
lpDS3CellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellTransmitCellUtilization.setStatus("mandatory")
_LpDS3CellCorrectableHeaderErrors_Type = Counter32
_LpDS3CellCorrectableHeaderErrors_Object = MibTableColumn
lpDS3CellCorrectableHeaderErrors = _LpDS3CellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 5, 12, 1, 5),
    _LpDS3CellCorrectableHeaderErrors_Type()
)
lpDS3CellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3CellCorrectableHeaderErrors.setStatus("mandatory")
_LpDS3DS1_ObjectIdentity = ObjectIdentity
lpDS3DS1 = _LpDS3DS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6)
)
_LpDS3DS1RowStatusTable_Object = MibTable
lpDS3DS1RowStatusTable = _LpDS3DS1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 1)
)
if mibBuilder.loadTexts:
    lpDS3DS1RowStatusTable.setStatus("mandatory")
_LpDS3DS1RowStatusEntry_Object = MibTableRow
lpDS3DS1RowStatusEntry = _LpDS3DS1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 1, 1)
)
lpDS3DS1RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1RowStatusEntry.setStatus("mandatory")
_LpDS3DS1RowStatus_Type = RowStatus
_LpDS3DS1RowStatus_Object = MibTableColumn
lpDS3DS1RowStatus = _LpDS3DS1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 1, 1, 1),
    _LpDS3DS1RowStatus_Type()
)
lpDS3DS1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1RowStatus.setStatus("mandatory")
_LpDS3DS1ComponentName_Type = DisplayString
_LpDS3DS1ComponentName_Object = MibTableColumn
lpDS3DS1ComponentName = _LpDS3DS1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 1, 1, 2),
    _LpDS3DS1ComponentName_Type()
)
lpDS3DS1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ComponentName.setStatus("mandatory")
_LpDS3DS1StorageType_Type = StorageType
_LpDS3DS1StorageType_Object = MibTableColumn
lpDS3DS1StorageType = _LpDS3DS1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 1, 1, 4),
    _LpDS3DS1StorageType_Type()
)
lpDS3DS1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1StorageType.setStatus("mandatory")


class _LpDS3DS1Index_Type(Integer32):
    """Custom type lpDS3DS1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_LpDS3DS1Index_Type.__name__ = "Integer32"
_LpDS3DS1Index_Object = MibTableColumn
lpDS3DS1Index = _LpDS3DS1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 1, 1, 10),
    _LpDS3DS1Index_Type()
)
lpDS3DS1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1Index.setStatus("mandatory")
_LpDS3DS1Chan_ObjectIdentity = ObjectIdentity
lpDS3DS1Chan = _LpDS3DS1Chan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2)
)
_LpDS3DS1ChanRowStatusTable_Object = MibTable
lpDS3DS1ChanRowStatusTable = _LpDS3DS1ChanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 1)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanRowStatusTable.setStatus("mandatory")
_LpDS3DS1ChanRowStatusEntry_Object = MibTableRow
lpDS3DS1ChanRowStatusEntry = _LpDS3DS1ChanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 1, 1)
)
lpDS3DS1ChanRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanRowStatusEntry.setStatus("mandatory")
_LpDS3DS1ChanRowStatus_Type = RowStatus
_LpDS3DS1ChanRowStatus_Object = MibTableColumn
lpDS3DS1ChanRowStatus = _LpDS3DS1ChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 1, 1, 1),
    _LpDS3DS1ChanRowStatus_Type()
)
lpDS3DS1ChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanRowStatus.setStatus("mandatory")
_LpDS3DS1ChanComponentName_Type = DisplayString
_LpDS3DS1ChanComponentName_Object = MibTableColumn
lpDS3DS1ChanComponentName = _LpDS3DS1ChanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 1, 1, 2),
    _LpDS3DS1ChanComponentName_Type()
)
lpDS3DS1ChanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanComponentName.setStatus("mandatory")
_LpDS3DS1ChanStorageType_Type = StorageType
_LpDS3DS1ChanStorageType_Object = MibTableColumn
lpDS3DS1ChanStorageType = _LpDS3DS1ChanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 1, 1, 4),
    _LpDS3DS1ChanStorageType_Type()
)
lpDS3DS1ChanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanStorageType.setStatus("mandatory")


class _LpDS3DS1ChanIndex_Type(Integer32):
    """Custom type lpDS3DS1ChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LpDS3DS1ChanIndex_Type.__name__ = "Integer32"
_LpDS3DS1ChanIndex_Object = MibTableColumn
lpDS3DS1ChanIndex = _LpDS3DS1ChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 1, 1, 10),
    _LpDS3DS1ChanIndex_Type()
)
lpDS3DS1ChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1ChanIndex.setStatus("mandatory")
_LpDS3DS1ChanTest_ObjectIdentity = ObjectIdentity
lpDS3DS1ChanTest = _LpDS3DS1ChanTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2)
)
_LpDS3DS1ChanTestRowStatusTable_Object = MibTable
lpDS3DS1ChanTestRowStatusTable = _LpDS3DS1ChanTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestRowStatusTable.setStatus("mandatory")
_LpDS3DS1ChanTestRowStatusEntry_Object = MibTableRow
lpDS3DS1ChanTestRowStatusEntry = _LpDS3DS1ChanTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 1, 1)
)
lpDS3DS1ChanTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestRowStatusEntry.setStatus("mandatory")
_LpDS3DS1ChanTestRowStatus_Type = RowStatus
_LpDS3DS1ChanTestRowStatus_Object = MibTableColumn
lpDS3DS1ChanTestRowStatus = _LpDS3DS1ChanTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 1, 1, 1),
    _LpDS3DS1ChanTestRowStatus_Type()
)
lpDS3DS1ChanTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestRowStatus.setStatus("mandatory")
_LpDS3DS1ChanTestComponentName_Type = DisplayString
_LpDS3DS1ChanTestComponentName_Object = MibTableColumn
lpDS3DS1ChanTestComponentName = _LpDS3DS1ChanTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 1, 1, 2),
    _LpDS3DS1ChanTestComponentName_Type()
)
lpDS3DS1ChanTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestComponentName.setStatus("mandatory")
_LpDS3DS1ChanTestStorageType_Type = StorageType
_LpDS3DS1ChanTestStorageType_Object = MibTableColumn
lpDS3DS1ChanTestStorageType = _LpDS3DS1ChanTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 1, 1, 4),
    _LpDS3DS1ChanTestStorageType_Type()
)
lpDS3DS1ChanTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestStorageType.setStatus("mandatory")
_LpDS3DS1ChanTestIndex_Type = NonReplicated
_LpDS3DS1ChanTestIndex_Object = MibTableColumn
lpDS3DS1ChanTestIndex = _LpDS3DS1ChanTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 1, 1, 10),
    _LpDS3DS1ChanTestIndex_Type()
)
lpDS3DS1ChanTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestIndex.setStatus("mandatory")
_LpDS3DS1ChanTestStateTable_Object = MibTable
lpDS3DS1ChanTestStateTable = _LpDS3DS1ChanTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestStateTable.setStatus("mandatory")
_LpDS3DS1ChanTestStateEntry_Object = MibTableRow
lpDS3DS1ChanTestStateEntry = _LpDS3DS1ChanTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 10, 1)
)
lpDS3DS1ChanTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestStateEntry.setStatus("mandatory")


class _LpDS3DS1ChanTestAdminState_Type(Integer32):
    """Custom type lpDS3DS1ChanTestAdminState based on Integer32"""
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


_LpDS3DS1ChanTestAdminState_Type.__name__ = "Integer32"
_LpDS3DS1ChanTestAdminState_Object = MibTableColumn
lpDS3DS1ChanTestAdminState = _LpDS3DS1ChanTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 10, 1, 1),
    _LpDS3DS1ChanTestAdminState_Type()
)
lpDS3DS1ChanTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestAdminState.setStatus("mandatory")


class _LpDS3DS1ChanTestOperationalState_Type(Integer32):
    """Custom type lpDS3DS1ChanTestOperationalState based on Integer32"""
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


_LpDS3DS1ChanTestOperationalState_Type.__name__ = "Integer32"
_LpDS3DS1ChanTestOperationalState_Object = MibTableColumn
lpDS3DS1ChanTestOperationalState = _LpDS3DS1ChanTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 10, 1, 2),
    _LpDS3DS1ChanTestOperationalState_Type()
)
lpDS3DS1ChanTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestOperationalState.setStatus("mandatory")


class _LpDS3DS1ChanTestUsageState_Type(Integer32):
    """Custom type lpDS3DS1ChanTestUsageState based on Integer32"""
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


_LpDS3DS1ChanTestUsageState_Type.__name__ = "Integer32"
_LpDS3DS1ChanTestUsageState_Object = MibTableColumn
lpDS3DS1ChanTestUsageState = _LpDS3DS1ChanTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 10, 1, 3),
    _LpDS3DS1ChanTestUsageState_Type()
)
lpDS3DS1ChanTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestUsageState.setStatus("mandatory")
_LpDS3DS1ChanTestSetupTable_Object = MibTable
lpDS3DS1ChanTestSetupTable = _LpDS3DS1ChanTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestSetupTable.setStatus("mandatory")
_LpDS3DS1ChanTestSetupEntry_Object = MibTableRow
lpDS3DS1ChanTestSetupEntry = _LpDS3DS1ChanTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1)
)
lpDS3DS1ChanTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestSetupEntry.setStatus("mandatory")


class _LpDS3DS1ChanTestPurpose_Type(AsciiString):
    """Custom type lpDS3DS1ChanTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpDS3DS1ChanTestPurpose_Type.__name__ = "AsciiString"
_LpDS3DS1ChanTestPurpose_Object = MibTableColumn
lpDS3DS1ChanTestPurpose = _LpDS3DS1ChanTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 1),
    _LpDS3DS1ChanTestPurpose_Type()
)
lpDS3DS1ChanTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestPurpose.setStatus("mandatory")


class _LpDS3DS1ChanTestType_Type(Integer32):
    """Custom type lpDS3DS1ChanTestType based on Integer32"""
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


_LpDS3DS1ChanTestType_Type.__name__ = "Integer32"
_LpDS3DS1ChanTestType_Object = MibTableColumn
lpDS3DS1ChanTestType = _LpDS3DS1ChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 2),
    _LpDS3DS1ChanTestType_Type()
)
lpDS3DS1ChanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestType.setStatus("mandatory")


class _LpDS3DS1ChanTestFrmSize_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpDS3DS1ChanTestFrmSize_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTestFrmSize_Object = MibTableColumn
lpDS3DS1ChanTestFrmSize = _LpDS3DS1ChanTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 3),
    _LpDS3DS1ChanTestFrmSize_Type()
)
lpDS3DS1ChanTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestFrmSize.setStatus("mandatory")


class _LpDS3DS1ChanTestFrmPatternType_Type(Integer32):
    """Custom type lpDS3DS1ChanTestFrmPatternType based on Integer32"""
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


_LpDS3DS1ChanTestFrmPatternType_Type.__name__ = "Integer32"
_LpDS3DS1ChanTestFrmPatternType_Object = MibTableColumn
lpDS3DS1ChanTestFrmPatternType = _LpDS3DS1ChanTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 4),
    _LpDS3DS1ChanTestFrmPatternType_Type()
)
lpDS3DS1ChanTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestFrmPatternType.setStatus("mandatory")


class _LpDS3DS1ChanTestCustomizedPattern_Type(Hex):
    """Custom type lpDS3DS1ChanTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS3DS1ChanTestCustomizedPattern_Type.__name__ = "Hex"
_LpDS3DS1ChanTestCustomizedPattern_Object = MibTableColumn
lpDS3DS1ChanTestCustomizedPattern = _LpDS3DS1ChanTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 5),
    _LpDS3DS1ChanTestCustomizedPattern_Type()
)
lpDS3DS1ChanTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestCustomizedPattern.setStatus("mandatory")


class _LpDS3DS1ChanTestDataStartDelay_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpDS3DS1ChanTestDataStartDelay_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTestDataStartDelay_Object = MibTableColumn
lpDS3DS1ChanTestDataStartDelay = _LpDS3DS1ChanTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 6),
    _LpDS3DS1ChanTestDataStartDelay_Type()
)
lpDS3DS1ChanTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestDataStartDelay.setStatus("mandatory")


class _LpDS3DS1ChanTestDisplayInterval_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpDS3DS1ChanTestDisplayInterval_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTestDisplayInterval_Object = MibTableColumn
lpDS3DS1ChanTestDisplayInterval = _LpDS3DS1ChanTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 7),
    _LpDS3DS1ChanTestDisplayInterval_Type()
)
lpDS3DS1ChanTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestDisplayInterval.setStatus("mandatory")


class _LpDS3DS1ChanTestDuration_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpDS3DS1ChanTestDuration_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTestDuration_Object = MibTableColumn
lpDS3DS1ChanTestDuration = _LpDS3DS1ChanTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 11, 1, 8),
    _LpDS3DS1ChanTestDuration_Type()
)
lpDS3DS1ChanTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestDuration.setStatus("mandatory")
_LpDS3DS1ChanTestResultsTable_Object = MibTable
lpDS3DS1ChanTestResultsTable = _LpDS3DS1ChanTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestResultsTable.setStatus("mandatory")
_LpDS3DS1ChanTestResultsEntry_Object = MibTableRow
lpDS3DS1ChanTestResultsEntry = _LpDS3DS1ChanTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1)
)
lpDS3DS1ChanTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestResultsEntry.setStatus("mandatory")
_LpDS3DS1ChanTestElapsedTime_Type = Counter32
_LpDS3DS1ChanTestElapsedTime_Object = MibTableColumn
lpDS3DS1ChanTestElapsedTime = _LpDS3DS1ChanTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 1),
    _LpDS3DS1ChanTestElapsedTime_Type()
)
lpDS3DS1ChanTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestElapsedTime.setStatus("mandatory")


class _LpDS3DS1ChanTestTimeRemaining_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS3DS1ChanTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTestTimeRemaining_Object = MibTableColumn
lpDS3DS1ChanTestTimeRemaining = _LpDS3DS1ChanTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 2),
    _LpDS3DS1ChanTestTimeRemaining_Type()
)
lpDS3DS1ChanTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestTimeRemaining.setStatus("mandatory")


class _LpDS3DS1ChanTestCauseOfTermination_Type(Integer32):
    """Custom type lpDS3DS1ChanTestCauseOfTermination based on Integer32"""
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


_LpDS3DS1ChanTestCauseOfTermination_Type.__name__ = "Integer32"
_LpDS3DS1ChanTestCauseOfTermination_Object = MibTableColumn
lpDS3DS1ChanTestCauseOfTermination = _LpDS3DS1ChanTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 3),
    _LpDS3DS1ChanTestCauseOfTermination_Type()
)
lpDS3DS1ChanTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestCauseOfTermination.setStatus("mandatory")
_LpDS3DS1ChanTestBitsTx_Type = PassportCounter64
_LpDS3DS1ChanTestBitsTx_Object = MibTableColumn
lpDS3DS1ChanTestBitsTx = _LpDS3DS1ChanTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 4),
    _LpDS3DS1ChanTestBitsTx_Type()
)
lpDS3DS1ChanTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestBitsTx.setStatus("mandatory")
_LpDS3DS1ChanTestBytesTx_Type = PassportCounter64
_LpDS3DS1ChanTestBytesTx_Object = MibTableColumn
lpDS3DS1ChanTestBytesTx = _LpDS3DS1ChanTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 5),
    _LpDS3DS1ChanTestBytesTx_Type()
)
lpDS3DS1ChanTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestBytesTx.setStatus("mandatory")
_LpDS3DS1ChanTestFrmTx_Type = PassportCounter64
_LpDS3DS1ChanTestFrmTx_Object = MibTableColumn
lpDS3DS1ChanTestFrmTx = _LpDS3DS1ChanTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 6),
    _LpDS3DS1ChanTestFrmTx_Type()
)
lpDS3DS1ChanTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestFrmTx.setStatus("mandatory")
_LpDS3DS1ChanTestBitsRx_Type = PassportCounter64
_LpDS3DS1ChanTestBitsRx_Object = MibTableColumn
lpDS3DS1ChanTestBitsRx = _LpDS3DS1ChanTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 7),
    _LpDS3DS1ChanTestBitsRx_Type()
)
lpDS3DS1ChanTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestBitsRx.setStatus("mandatory")
_LpDS3DS1ChanTestBytesRx_Type = PassportCounter64
_LpDS3DS1ChanTestBytesRx_Object = MibTableColumn
lpDS3DS1ChanTestBytesRx = _LpDS3DS1ChanTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 8),
    _LpDS3DS1ChanTestBytesRx_Type()
)
lpDS3DS1ChanTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestBytesRx.setStatus("mandatory")
_LpDS3DS1ChanTestFrmRx_Type = PassportCounter64
_LpDS3DS1ChanTestFrmRx_Object = MibTableColumn
lpDS3DS1ChanTestFrmRx = _LpDS3DS1ChanTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 9),
    _LpDS3DS1ChanTestFrmRx_Type()
)
lpDS3DS1ChanTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestFrmRx.setStatus("mandatory")
_LpDS3DS1ChanTestErroredFrmRx_Type = PassportCounter64
_LpDS3DS1ChanTestErroredFrmRx_Object = MibTableColumn
lpDS3DS1ChanTestErroredFrmRx = _LpDS3DS1ChanTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 10),
    _LpDS3DS1ChanTestErroredFrmRx_Type()
)
lpDS3DS1ChanTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestErroredFrmRx.setStatus("mandatory")


class _LpDS3DS1ChanTestBitErrorRate_Type(AsciiString):
    """Custom type lpDS3DS1ChanTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpDS3DS1ChanTestBitErrorRate_Type.__name__ = "AsciiString"
_LpDS3DS1ChanTestBitErrorRate_Object = MibTableColumn
lpDS3DS1ChanTestBitErrorRate = _LpDS3DS1ChanTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 2, 12, 1, 11),
    _LpDS3DS1ChanTestBitErrorRate_Type()
)
lpDS3DS1ChanTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTestBitErrorRate.setStatus("mandatory")
_LpDS3DS1ChanCell_ObjectIdentity = ObjectIdentity
lpDS3DS1ChanCell = _LpDS3DS1ChanCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3)
)
_LpDS3DS1ChanCellRowStatusTable_Object = MibTable
lpDS3DS1ChanCellRowStatusTable = _LpDS3DS1ChanCellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellRowStatusTable.setStatus("mandatory")
_LpDS3DS1ChanCellRowStatusEntry_Object = MibTableRow
lpDS3DS1ChanCellRowStatusEntry = _LpDS3DS1ChanCellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 1, 1)
)
lpDS3DS1ChanCellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellRowStatusEntry.setStatus("mandatory")
_LpDS3DS1ChanCellRowStatus_Type = RowStatus
_LpDS3DS1ChanCellRowStatus_Object = MibTableColumn
lpDS3DS1ChanCellRowStatus = _LpDS3DS1ChanCellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 1, 1, 1),
    _LpDS3DS1ChanCellRowStatus_Type()
)
lpDS3DS1ChanCellRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellRowStatus.setStatus("mandatory")
_LpDS3DS1ChanCellComponentName_Type = DisplayString
_LpDS3DS1ChanCellComponentName_Object = MibTableColumn
lpDS3DS1ChanCellComponentName = _LpDS3DS1ChanCellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 1, 1, 2),
    _LpDS3DS1ChanCellComponentName_Type()
)
lpDS3DS1ChanCellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellComponentName.setStatus("mandatory")
_LpDS3DS1ChanCellStorageType_Type = StorageType
_LpDS3DS1ChanCellStorageType_Object = MibTableColumn
lpDS3DS1ChanCellStorageType = _LpDS3DS1ChanCellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 1, 1, 4),
    _LpDS3DS1ChanCellStorageType_Type()
)
lpDS3DS1ChanCellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellStorageType.setStatus("mandatory")
_LpDS3DS1ChanCellIndex_Type = NonReplicated
_LpDS3DS1ChanCellIndex_Object = MibTableColumn
lpDS3DS1ChanCellIndex = _LpDS3DS1ChanCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 1, 1, 10),
    _LpDS3DS1ChanCellIndex_Type()
)
lpDS3DS1ChanCellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellIndex.setStatus("mandatory")
_LpDS3DS1ChanCellProvTable_Object = MibTable
lpDS3DS1ChanCellProvTable = _LpDS3DS1ChanCellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellProvTable.setStatus("mandatory")
_LpDS3DS1ChanCellProvEntry_Object = MibTableRow
lpDS3DS1ChanCellProvEntry = _LpDS3DS1ChanCellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 10, 1)
)
lpDS3DS1ChanCellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellProvEntry.setStatus("mandatory")


class _LpDS3DS1ChanCellAlarmActDelay_Type(Unsigned32):
    """Custom type lpDS3DS1ChanCellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpDS3DS1ChanCellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanCellAlarmActDelay_Object = MibTableColumn
lpDS3DS1ChanCellAlarmActDelay = _LpDS3DS1ChanCellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 10, 1, 1),
    _LpDS3DS1ChanCellAlarmActDelay_Type()
)
lpDS3DS1ChanCellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellAlarmActDelay.setStatus("mandatory")


class _LpDS3DS1ChanCellScrambleCellPayload_Type(Integer32):
    """Custom type lpDS3DS1ChanCellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS3DS1ChanCellScrambleCellPayload_Type.__name__ = "Integer32"
_LpDS3DS1ChanCellScrambleCellPayload_Object = MibTableColumn
lpDS3DS1ChanCellScrambleCellPayload = _LpDS3DS1ChanCellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 10, 1, 2),
    _LpDS3DS1ChanCellScrambleCellPayload_Type()
)
lpDS3DS1ChanCellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellScrambleCellPayload.setStatus("mandatory")


class _LpDS3DS1ChanCellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpDS3DS1ChanCellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS3DS1ChanCellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpDS3DS1ChanCellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpDS3DS1ChanCellCorrectSingleBitHeaderErrors = _LpDS3DS1ChanCellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 10, 1, 3),
    _LpDS3DS1ChanCellCorrectSingleBitHeaderErrors_Type()
)
lpDS3DS1ChanCellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpDS3DS1ChanCellOperTable_Object = MibTable
lpDS3DS1ChanCellOperTable = _LpDS3DS1ChanCellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 11)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellOperTable.setStatus("mandatory")
_LpDS3DS1ChanCellOperEntry_Object = MibTableRow
lpDS3DS1ChanCellOperEntry = _LpDS3DS1ChanCellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 11, 1)
)
lpDS3DS1ChanCellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellOperEntry.setStatus("mandatory")


class _LpDS3DS1ChanCellLcdAlarm_Type(Integer32):
    """Custom type lpDS3DS1ChanCellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3DS1ChanCellLcdAlarm_Type.__name__ = "Integer32"
_LpDS3DS1ChanCellLcdAlarm_Object = MibTableColumn
lpDS3DS1ChanCellLcdAlarm = _LpDS3DS1ChanCellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 11, 1, 1),
    _LpDS3DS1ChanCellLcdAlarm_Type()
)
lpDS3DS1ChanCellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellLcdAlarm.setStatus("mandatory")
_LpDS3DS1ChanCellStatsTable_Object = MibTable
lpDS3DS1ChanCellStatsTable = _LpDS3DS1ChanCellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 12)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellStatsTable.setStatus("mandatory")
_LpDS3DS1ChanCellStatsEntry_Object = MibTableRow
lpDS3DS1ChanCellStatsEntry = _LpDS3DS1ChanCellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 12, 1)
)
lpDS3DS1ChanCellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellStatsEntry.setStatus("mandatory")
_LpDS3DS1ChanCellUncorrectableHecErrors_Type = Counter32
_LpDS3DS1ChanCellUncorrectableHecErrors_Object = MibTableColumn
lpDS3DS1ChanCellUncorrectableHecErrors = _LpDS3DS1ChanCellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 12, 1, 1),
    _LpDS3DS1ChanCellUncorrectableHecErrors_Type()
)
lpDS3DS1ChanCellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellUncorrectableHecErrors.setStatus("mandatory")
_LpDS3DS1ChanCellSevErroredSec_Type = Counter32
_LpDS3DS1ChanCellSevErroredSec_Object = MibTableColumn
lpDS3DS1ChanCellSevErroredSec = _LpDS3DS1ChanCellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 12, 1, 2),
    _LpDS3DS1ChanCellSevErroredSec_Type()
)
lpDS3DS1ChanCellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellSevErroredSec.setStatus("mandatory")


class _LpDS3DS1ChanCellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpDS3DS1ChanCellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpDS3DS1ChanCellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpDS3DS1ChanCellReceiveCellUtilization_Object = MibTableColumn
lpDS3DS1ChanCellReceiveCellUtilization = _LpDS3DS1ChanCellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 12, 1, 3),
    _LpDS3DS1ChanCellReceiveCellUtilization_Type()
)
lpDS3DS1ChanCellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellReceiveCellUtilization.setStatus("mandatory")


class _LpDS3DS1ChanCellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpDS3DS1ChanCellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpDS3DS1ChanCellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpDS3DS1ChanCellTransmitCellUtilization_Object = MibTableColumn
lpDS3DS1ChanCellTransmitCellUtilization = _LpDS3DS1ChanCellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 12, 1, 4),
    _LpDS3DS1ChanCellTransmitCellUtilization_Type()
)
lpDS3DS1ChanCellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellTransmitCellUtilization.setStatus("mandatory")
_LpDS3DS1ChanCellCorrectableHeaderErrors_Type = Counter32
_LpDS3DS1ChanCellCorrectableHeaderErrors_Object = MibTableColumn
lpDS3DS1ChanCellCorrectableHeaderErrors = _LpDS3DS1ChanCellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 3, 12, 1, 5),
    _LpDS3DS1ChanCellCorrectableHeaderErrors_Type()
)
lpDS3DS1ChanCellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCellCorrectableHeaderErrors.setStatus("mandatory")
_LpDS3DS1ChanTc_ObjectIdentity = ObjectIdentity
lpDS3DS1ChanTc = _LpDS3DS1ChanTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4)
)
_LpDS3DS1ChanTcRowStatusTable_Object = MibTable
lpDS3DS1ChanTcRowStatusTable = _LpDS3DS1ChanTcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcRowStatusTable.setStatus("mandatory")
_LpDS3DS1ChanTcRowStatusEntry_Object = MibTableRow
lpDS3DS1ChanTcRowStatusEntry = _LpDS3DS1ChanTcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 1, 1)
)
lpDS3DS1ChanTcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcRowStatusEntry.setStatus("mandatory")
_LpDS3DS1ChanTcRowStatus_Type = RowStatus
_LpDS3DS1ChanTcRowStatus_Object = MibTableColumn
lpDS3DS1ChanTcRowStatus = _LpDS3DS1ChanTcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 1, 1, 1),
    _LpDS3DS1ChanTcRowStatus_Type()
)
lpDS3DS1ChanTcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcRowStatus.setStatus("mandatory")
_LpDS3DS1ChanTcComponentName_Type = DisplayString
_LpDS3DS1ChanTcComponentName_Object = MibTableColumn
lpDS3DS1ChanTcComponentName = _LpDS3DS1ChanTcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 1, 1, 2),
    _LpDS3DS1ChanTcComponentName_Type()
)
lpDS3DS1ChanTcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcComponentName.setStatus("mandatory")
_LpDS3DS1ChanTcStorageType_Type = StorageType
_LpDS3DS1ChanTcStorageType_Object = MibTableColumn
lpDS3DS1ChanTcStorageType = _LpDS3DS1ChanTcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 1, 1, 4),
    _LpDS3DS1ChanTcStorageType_Type()
)
lpDS3DS1ChanTcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcStorageType.setStatus("mandatory")
_LpDS3DS1ChanTcIndex_Type = NonReplicated
_LpDS3DS1ChanTcIndex_Object = MibTableColumn
lpDS3DS1ChanTcIndex = _LpDS3DS1ChanTcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 1, 1, 10),
    _LpDS3DS1ChanTcIndex_Type()
)
lpDS3DS1ChanTcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcIndex.setStatus("mandatory")
_LpDS3DS1ChanTcProvTable_Object = MibTable
lpDS3DS1ChanTcProvTable = _LpDS3DS1ChanTcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcProvTable.setStatus("mandatory")
_LpDS3DS1ChanTcProvEntry_Object = MibTableRow
lpDS3DS1ChanTcProvEntry = _LpDS3DS1ChanTcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 10, 1)
)
lpDS3DS1ChanTcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcProvEntry.setStatus("mandatory")


class _LpDS3DS1ChanTcReplacementData_Type(Hex):
    """Custom type lpDS3DS1ChanTcReplacementData based on Hex"""
    defaultValue = 255

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LpDS3DS1ChanTcReplacementData_Type.__name__ = "Hex"
_LpDS3DS1ChanTcReplacementData_Object = MibTableColumn
lpDS3DS1ChanTcReplacementData = _LpDS3DS1ChanTcReplacementData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 10, 1, 1),
    _LpDS3DS1ChanTcReplacementData_Type()
)
lpDS3DS1ChanTcReplacementData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcReplacementData.setStatus("mandatory")


class _LpDS3DS1ChanTcSignalOneDuration_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTcSignalOneDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_LpDS3DS1ChanTcSignalOneDuration_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTcSignalOneDuration_Object = MibTableColumn
lpDS3DS1ChanTcSignalOneDuration = _LpDS3DS1ChanTcSignalOneDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 10, 1, 2),
    _LpDS3DS1ChanTcSignalOneDuration_Type()
)
lpDS3DS1ChanTcSignalOneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSignalOneDuration.setStatus("mandatory")
_LpDS3DS1ChanTcOpTable_Object = MibTable
lpDS3DS1ChanTcOpTable = _LpDS3DS1ChanTcOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 11)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcOpTable.setStatus("mandatory")
_LpDS3DS1ChanTcOpEntry_Object = MibTableRow
lpDS3DS1ChanTcOpEntry = _LpDS3DS1ChanTcOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 11, 1)
)
lpDS3DS1ChanTcOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcOpEntry.setStatus("mandatory")


class _LpDS3DS1ChanTcIngressConditioning_Type(Integer32):
    """Custom type lpDS3DS1ChanTcIngressConditioning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS3DS1ChanTcIngressConditioning_Type.__name__ = "Integer32"
_LpDS3DS1ChanTcIngressConditioning_Object = MibTableColumn
lpDS3DS1ChanTcIngressConditioning = _LpDS3DS1ChanTcIngressConditioning_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 11, 1, 1),
    _LpDS3DS1ChanTcIngressConditioning_Type()
)
lpDS3DS1ChanTcIngressConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcIngressConditioning.setStatus("mandatory")


class _LpDS3DS1ChanTcEgressConditioning_Type(Integer32):
    """Custom type lpDS3DS1ChanTcEgressConditioning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS3DS1ChanTcEgressConditioning_Type.__name__ = "Integer32"
_LpDS3DS1ChanTcEgressConditioning_Object = MibTableColumn
lpDS3DS1ChanTcEgressConditioning = _LpDS3DS1ChanTcEgressConditioning_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 11, 1, 2),
    _LpDS3DS1ChanTcEgressConditioning_Type()
)
lpDS3DS1ChanTcEgressConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcEgressConditioning.setStatus("mandatory")
_LpDS3DS1ChanTcSigOneTable_Object = MibTable
lpDS3DS1ChanTcSigOneTable = _LpDS3DS1ChanTcSigOneTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 398)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigOneTable.setStatus("mandatory")
_LpDS3DS1ChanTcSigOneEntry_Object = MibTableRow
lpDS3DS1ChanTcSigOneEntry = _LpDS3DS1ChanTcSigOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 398, 1)
)
lpDS3DS1ChanTcSigOneEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTcIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTcSigOneIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigOneEntry.setStatus("mandatory")


class _LpDS3DS1ChanTcSigOneIndex_Type(Integer32):
    """Custom type lpDS3DS1ChanTcSigOneIndex based on Integer32"""
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
        *(("a", 3),
          ("b", 2),
          ("c", 1),
          ("d", 0))
    )


_LpDS3DS1ChanTcSigOneIndex_Type.__name__ = "Integer32"
_LpDS3DS1ChanTcSigOneIndex_Object = MibTableColumn
lpDS3DS1ChanTcSigOneIndex = _LpDS3DS1ChanTcSigOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 398, 1, 1),
    _LpDS3DS1ChanTcSigOneIndex_Type()
)
lpDS3DS1ChanTcSigOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigOneIndex.setStatus("mandatory")


class _LpDS3DS1ChanTcSigOneValue_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTcSigOneValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpDS3DS1ChanTcSigOneValue_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTcSigOneValue_Object = MibTableColumn
lpDS3DS1ChanTcSigOneValue = _LpDS3DS1ChanTcSigOneValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 398, 1, 2),
    _LpDS3DS1ChanTcSigOneValue_Type()
)
lpDS3DS1ChanTcSigOneValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigOneValue.setStatus("mandatory")
_LpDS3DS1ChanTcSigTwoTable_Object = MibTable
lpDS3DS1ChanTcSigTwoTable = _LpDS3DS1ChanTcSigTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 399)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigTwoTable.setStatus("mandatory")
_LpDS3DS1ChanTcSigTwoEntry_Object = MibTableRow
lpDS3DS1ChanTcSigTwoEntry = _LpDS3DS1ChanTcSigTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 399, 1)
)
lpDS3DS1ChanTcSigTwoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTcIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanTcSigTwoIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigTwoEntry.setStatus("mandatory")


class _LpDS3DS1ChanTcSigTwoIndex_Type(Integer32):
    """Custom type lpDS3DS1ChanTcSigTwoIndex based on Integer32"""
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
        *(("a", 3),
          ("b", 2),
          ("c", 1),
          ("d", 0))
    )


_LpDS3DS1ChanTcSigTwoIndex_Type.__name__ = "Integer32"
_LpDS3DS1ChanTcSigTwoIndex_Object = MibTableColumn
lpDS3DS1ChanTcSigTwoIndex = _LpDS3DS1ChanTcSigTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 399, 1, 1),
    _LpDS3DS1ChanTcSigTwoIndex_Type()
)
lpDS3DS1ChanTcSigTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigTwoIndex.setStatus("mandatory")


class _LpDS3DS1ChanTcSigTwoValue_Type(Unsigned32):
    """Custom type lpDS3DS1ChanTcSigTwoValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpDS3DS1ChanTcSigTwoValue_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanTcSigTwoValue_Object = MibTableColumn
lpDS3DS1ChanTcSigTwoValue = _LpDS3DS1ChanTcSigTwoValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 4, 399, 1, 2),
    _LpDS3DS1ChanTcSigTwoValue_Type()
)
lpDS3DS1ChanTcSigTwoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTcSigTwoValue.setStatus("mandatory")
_LpDS3DS1ChanProvTable_Object = MibTable
lpDS3DS1ChanProvTable = _LpDS3DS1ChanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 10)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanProvTable.setStatus("mandatory")
_LpDS3DS1ChanProvEntry_Object = MibTableRow
lpDS3DS1ChanProvEntry = _LpDS3DS1ChanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 10, 1)
)
lpDS3DS1ChanProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanProvEntry.setStatus("mandatory")


class _LpDS3DS1ChanTimeslots_Type(OctetString):
    """Custom type lpDS3DS1ChanTimeslots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpDS3DS1ChanTimeslots_Type.__name__ = "OctetString"
_LpDS3DS1ChanTimeslots_Object = MibTableColumn
lpDS3DS1ChanTimeslots = _LpDS3DS1ChanTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 10, 1, 1),
    _LpDS3DS1ChanTimeslots_Type()
)
lpDS3DS1ChanTimeslots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTimeslots.setStatus("mandatory")


class _LpDS3DS1ChanTimeslotDataRate_Type(Integer32):
    """Custom type lpDS3DS1ChanTimeslotDataRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNotOverride", 1),
          ("n56k", 0))
    )


_LpDS3DS1ChanTimeslotDataRate_Type.__name__ = "Integer32"
_LpDS3DS1ChanTimeslotDataRate_Object = MibTableColumn
lpDS3DS1ChanTimeslotDataRate = _LpDS3DS1ChanTimeslotDataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 10, 1, 2),
    _LpDS3DS1ChanTimeslotDataRate_Type()
)
lpDS3DS1ChanTimeslotDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanTimeslotDataRate.setStatus("mandatory")
_LpDS3DS1ChanApplicationFramerName_Type = Link
_LpDS3DS1ChanApplicationFramerName_Object = MibTableColumn
lpDS3DS1ChanApplicationFramerName = _LpDS3DS1ChanApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 10, 1, 3),
    _LpDS3DS1ChanApplicationFramerName_Type()
)
lpDS3DS1ChanApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanApplicationFramerName.setStatus("mandatory")
_LpDS3DS1ChanCidDataTable_Object = MibTable
lpDS3DS1ChanCidDataTable = _LpDS3DS1ChanCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 11)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCidDataTable.setStatus("mandatory")
_LpDS3DS1ChanCidDataEntry_Object = MibTableRow
lpDS3DS1ChanCidDataEntry = _LpDS3DS1ChanCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 11, 1)
)
lpDS3DS1ChanCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanCidDataEntry.setStatus("mandatory")


class _LpDS3DS1ChanCustomerIdentifier_Type(Unsigned32):
    """Custom type lpDS3DS1ChanCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpDS3DS1ChanCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpDS3DS1ChanCustomerIdentifier_Object = MibTableColumn
lpDS3DS1ChanCustomerIdentifier = _LpDS3DS1ChanCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 11, 1, 1),
    _LpDS3DS1ChanCustomerIdentifier_Type()
)
lpDS3DS1ChanCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCustomerIdentifier.setStatus("mandatory")
_LpDS3DS1ChanIfEntryTable_Object = MibTable
lpDS3DS1ChanIfEntryTable = _LpDS3DS1ChanIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 12)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanIfEntryTable.setStatus("mandatory")
_LpDS3DS1ChanIfEntryEntry_Object = MibTableRow
lpDS3DS1ChanIfEntryEntry = _LpDS3DS1ChanIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 12, 1)
)
lpDS3DS1ChanIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanIfEntryEntry.setStatus("mandatory")


class _LpDS3DS1ChanIfAdminStatus_Type(Integer32):
    """Custom type lpDS3DS1ChanIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS3DS1ChanIfAdminStatus_Type.__name__ = "Integer32"
_LpDS3DS1ChanIfAdminStatus_Object = MibTableColumn
lpDS3DS1ChanIfAdminStatus = _LpDS3DS1ChanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 12, 1, 1),
    _LpDS3DS1ChanIfAdminStatus_Type()
)
lpDS3DS1ChanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanIfAdminStatus.setStatus("mandatory")


class _LpDS3DS1ChanIfIndex_Type(InterfaceIndex):
    """Custom type lpDS3DS1ChanIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpDS3DS1ChanIfIndex_Type.__name__ = "InterfaceIndex"
_LpDS3DS1ChanIfIndex_Object = MibTableColumn
lpDS3DS1ChanIfIndex = _LpDS3DS1ChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 12, 1, 2),
    _LpDS3DS1ChanIfIndex_Type()
)
lpDS3DS1ChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanIfIndex.setStatus("mandatory")
_LpDS3DS1ChanOperStatusTable_Object = MibTable
lpDS3DS1ChanOperStatusTable = _LpDS3DS1ChanOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 13)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanOperStatusTable.setStatus("mandatory")
_LpDS3DS1ChanOperStatusEntry_Object = MibTableRow
lpDS3DS1ChanOperStatusEntry = _LpDS3DS1ChanOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 13, 1)
)
lpDS3DS1ChanOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanOperStatusEntry.setStatus("mandatory")


class _LpDS3DS1ChanSnmpOperStatus_Type(Integer32):
    """Custom type lpDS3DS1ChanSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS3DS1ChanSnmpOperStatus_Type.__name__ = "Integer32"
_LpDS3DS1ChanSnmpOperStatus_Object = MibTableColumn
lpDS3DS1ChanSnmpOperStatus = _LpDS3DS1ChanSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 13, 1, 1),
    _LpDS3DS1ChanSnmpOperStatus_Type()
)
lpDS3DS1ChanSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanSnmpOperStatus.setStatus("mandatory")
_LpDS3DS1ChanStateTable_Object = MibTable
lpDS3DS1ChanStateTable = _LpDS3DS1ChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanStateTable.setStatus("mandatory")
_LpDS3DS1ChanStateEntry_Object = MibTableRow
lpDS3DS1ChanStateEntry = _LpDS3DS1ChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1)
)
lpDS3DS1ChanStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanStateEntry.setStatus("mandatory")


class _LpDS3DS1ChanAdminState_Type(Integer32):
    """Custom type lpDS3DS1ChanAdminState based on Integer32"""
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


_LpDS3DS1ChanAdminState_Type.__name__ = "Integer32"
_LpDS3DS1ChanAdminState_Object = MibTableColumn
lpDS3DS1ChanAdminState = _LpDS3DS1ChanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 1),
    _LpDS3DS1ChanAdminState_Type()
)
lpDS3DS1ChanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanAdminState.setStatus("mandatory")


class _LpDS3DS1ChanOperationalState_Type(Integer32):
    """Custom type lpDS3DS1ChanOperationalState based on Integer32"""
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


_LpDS3DS1ChanOperationalState_Type.__name__ = "Integer32"
_LpDS3DS1ChanOperationalState_Object = MibTableColumn
lpDS3DS1ChanOperationalState = _LpDS3DS1ChanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 2),
    _LpDS3DS1ChanOperationalState_Type()
)
lpDS3DS1ChanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanOperationalState.setStatus("mandatory")


class _LpDS3DS1ChanUsageState_Type(Integer32):
    """Custom type lpDS3DS1ChanUsageState based on Integer32"""
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


_LpDS3DS1ChanUsageState_Type.__name__ = "Integer32"
_LpDS3DS1ChanUsageState_Object = MibTableColumn
lpDS3DS1ChanUsageState = _LpDS3DS1ChanUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 3),
    _LpDS3DS1ChanUsageState_Type()
)
lpDS3DS1ChanUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanUsageState.setStatus("mandatory")


class _LpDS3DS1ChanAvailabilityStatus_Type(OctetString):
    """Custom type lpDS3DS1ChanAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpDS3DS1ChanAvailabilityStatus_Type.__name__ = "OctetString"
_LpDS3DS1ChanAvailabilityStatus_Object = MibTableColumn
lpDS3DS1ChanAvailabilityStatus = _LpDS3DS1ChanAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 4),
    _LpDS3DS1ChanAvailabilityStatus_Type()
)
lpDS3DS1ChanAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanAvailabilityStatus.setStatus("mandatory")


class _LpDS3DS1ChanProceduralStatus_Type(OctetString):
    """Custom type lpDS3DS1ChanProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3DS1ChanProceduralStatus_Type.__name__ = "OctetString"
_LpDS3DS1ChanProceduralStatus_Object = MibTableColumn
lpDS3DS1ChanProceduralStatus = _LpDS3DS1ChanProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 5),
    _LpDS3DS1ChanProceduralStatus_Type()
)
lpDS3DS1ChanProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanProceduralStatus.setStatus("mandatory")


class _LpDS3DS1ChanControlStatus_Type(OctetString):
    """Custom type lpDS3DS1ChanControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3DS1ChanControlStatus_Type.__name__ = "OctetString"
_LpDS3DS1ChanControlStatus_Object = MibTableColumn
lpDS3DS1ChanControlStatus = _LpDS3DS1ChanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 6),
    _LpDS3DS1ChanControlStatus_Type()
)
lpDS3DS1ChanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanControlStatus.setStatus("mandatory")


class _LpDS3DS1ChanAlarmStatus_Type(OctetString):
    """Custom type lpDS3DS1ChanAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3DS1ChanAlarmStatus_Type.__name__ = "OctetString"
_LpDS3DS1ChanAlarmStatus_Object = MibTableColumn
lpDS3DS1ChanAlarmStatus = _LpDS3DS1ChanAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 7),
    _LpDS3DS1ChanAlarmStatus_Type()
)
lpDS3DS1ChanAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanAlarmStatus.setStatus("mandatory")


class _LpDS3DS1ChanStandbyStatus_Type(Integer32):
    """Custom type lpDS3DS1ChanStandbyStatus based on Integer32"""
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


_LpDS3DS1ChanStandbyStatus_Type.__name__ = "Integer32"
_LpDS3DS1ChanStandbyStatus_Object = MibTableColumn
lpDS3DS1ChanStandbyStatus = _LpDS3DS1ChanStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 8),
    _LpDS3DS1ChanStandbyStatus_Type()
)
lpDS3DS1ChanStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanStandbyStatus.setStatus("mandatory")


class _LpDS3DS1ChanUnknownStatus_Type(Integer32):
    """Custom type lpDS3DS1ChanUnknownStatus based on Integer32"""
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


_LpDS3DS1ChanUnknownStatus_Type.__name__ = "Integer32"
_LpDS3DS1ChanUnknownStatus_Object = MibTableColumn
lpDS3DS1ChanUnknownStatus = _LpDS3DS1ChanUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 14, 1, 9),
    _LpDS3DS1ChanUnknownStatus_Type()
)
lpDS3DS1ChanUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanUnknownStatus.setStatus("mandatory")
_LpDS3DS1ChanOperTable_Object = MibTable
lpDS3DS1ChanOperTable = _LpDS3DS1ChanOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 15)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanOperTable.setStatus("mandatory")
_LpDS3DS1ChanOperEntry_Object = MibTableRow
lpDS3DS1ChanOperEntry = _LpDS3DS1ChanOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 15, 1)
)
lpDS3DS1ChanOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanOperEntry.setStatus("mandatory")


class _LpDS3DS1ChanActualChannelSpeed_Type(Gauge32):
    """Custom type lpDS3DS1ChanActualChannelSpeed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS3DS1ChanActualChannelSpeed_Type.__name__ = "Gauge32"
_LpDS3DS1ChanActualChannelSpeed_Object = MibTableColumn
lpDS3DS1ChanActualChannelSpeed = _LpDS3DS1ChanActualChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 15, 1, 1),
    _LpDS3DS1ChanActualChannelSpeed_Type()
)
lpDS3DS1ChanActualChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ChanActualChannelSpeed.setStatus("mandatory")
_LpDS3DS1ChanAdminInfoTable_Object = MibTable
lpDS3DS1ChanAdminInfoTable = _LpDS3DS1ChanAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 16)
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanAdminInfoTable.setStatus("mandatory")
_LpDS3DS1ChanAdminInfoEntry_Object = MibTableRow
lpDS3DS1ChanAdminInfoEntry = _LpDS3DS1ChanAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 16, 1)
)
lpDS3DS1ChanAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ChanAdminInfoEntry.setStatus("mandatory")


class _LpDS3DS1ChanVendor_Type(AsciiString):
    """Custom type lpDS3DS1ChanVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpDS3DS1ChanVendor_Type.__name__ = "AsciiString"
_LpDS3DS1ChanVendor_Object = MibTableColumn
lpDS3DS1ChanVendor = _LpDS3DS1ChanVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 16, 1, 1),
    _LpDS3DS1ChanVendor_Type()
)
lpDS3DS1ChanVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanVendor.setStatus("mandatory")


class _LpDS3DS1ChanCommentText_Type(AsciiString):
    """Custom type lpDS3DS1ChanCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpDS3DS1ChanCommentText_Type.__name__ = "AsciiString"
_LpDS3DS1ChanCommentText_Object = MibTableColumn
lpDS3DS1ChanCommentText = _LpDS3DS1ChanCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 2, 16, 1, 2),
    _LpDS3DS1ChanCommentText_Type()
)
lpDS3DS1ChanCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ChanCommentText.setStatus("mandatory")
_LpDS3DS1Test_ObjectIdentity = ObjectIdentity
lpDS3DS1Test = _LpDS3DS1Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3)
)
_LpDS3DS1TestRowStatusTable_Object = MibTable
lpDS3DS1TestRowStatusTable = _LpDS3DS1TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 1)
)
if mibBuilder.loadTexts:
    lpDS3DS1TestRowStatusTable.setStatus("mandatory")
_LpDS3DS1TestRowStatusEntry_Object = MibTableRow
lpDS3DS1TestRowStatusEntry = _LpDS3DS1TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 1, 1)
)
lpDS3DS1TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1TestRowStatusEntry.setStatus("mandatory")
_LpDS3DS1TestRowStatus_Type = RowStatus
_LpDS3DS1TestRowStatus_Object = MibTableColumn
lpDS3DS1TestRowStatus = _LpDS3DS1TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 1, 1, 1),
    _LpDS3DS1TestRowStatus_Type()
)
lpDS3DS1TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestRowStatus.setStatus("mandatory")
_LpDS3DS1TestComponentName_Type = DisplayString
_LpDS3DS1TestComponentName_Object = MibTableColumn
lpDS3DS1TestComponentName = _LpDS3DS1TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 1, 1, 2),
    _LpDS3DS1TestComponentName_Type()
)
lpDS3DS1TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestComponentName.setStatus("mandatory")
_LpDS3DS1TestStorageType_Type = StorageType
_LpDS3DS1TestStorageType_Object = MibTableColumn
lpDS3DS1TestStorageType = _LpDS3DS1TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 1, 1, 4),
    _LpDS3DS1TestStorageType_Type()
)
lpDS3DS1TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestStorageType.setStatus("mandatory")
_LpDS3DS1TestIndex_Type = NonReplicated
_LpDS3DS1TestIndex_Object = MibTableColumn
lpDS3DS1TestIndex = _LpDS3DS1TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 1, 1, 10),
    _LpDS3DS1TestIndex_Type()
)
lpDS3DS1TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS3DS1TestIndex.setStatus("mandatory")
_LpDS3DS1TestStateTable_Object = MibTable
lpDS3DS1TestStateTable = _LpDS3DS1TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 10)
)
if mibBuilder.loadTexts:
    lpDS3DS1TestStateTable.setStatus("mandatory")
_LpDS3DS1TestStateEntry_Object = MibTableRow
lpDS3DS1TestStateEntry = _LpDS3DS1TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 10, 1)
)
lpDS3DS1TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1TestStateEntry.setStatus("mandatory")


class _LpDS3DS1TestAdminState_Type(Integer32):
    """Custom type lpDS3DS1TestAdminState based on Integer32"""
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


_LpDS3DS1TestAdminState_Type.__name__ = "Integer32"
_LpDS3DS1TestAdminState_Object = MibTableColumn
lpDS3DS1TestAdminState = _LpDS3DS1TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 10, 1, 1),
    _LpDS3DS1TestAdminState_Type()
)
lpDS3DS1TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestAdminState.setStatus("mandatory")


class _LpDS3DS1TestOperationalState_Type(Integer32):
    """Custom type lpDS3DS1TestOperationalState based on Integer32"""
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


_LpDS3DS1TestOperationalState_Type.__name__ = "Integer32"
_LpDS3DS1TestOperationalState_Object = MibTableColumn
lpDS3DS1TestOperationalState = _LpDS3DS1TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 10, 1, 2),
    _LpDS3DS1TestOperationalState_Type()
)
lpDS3DS1TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestOperationalState.setStatus("mandatory")


class _LpDS3DS1TestUsageState_Type(Integer32):
    """Custom type lpDS3DS1TestUsageState based on Integer32"""
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


_LpDS3DS1TestUsageState_Type.__name__ = "Integer32"
_LpDS3DS1TestUsageState_Object = MibTableColumn
lpDS3DS1TestUsageState = _LpDS3DS1TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 10, 1, 3),
    _LpDS3DS1TestUsageState_Type()
)
lpDS3DS1TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestUsageState.setStatus("mandatory")
_LpDS3DS1TestSetupTable_Object = MibTable
lpDS3DS1TestSetupTable = _LpDS3DS1TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11)
)
if mibBuilder.loadTexts:
    lpDS3DS1TestSetupTable.setStatus("mandatory")
_LpDS3DS1TestSetupEntry_Object = MibTableRow
lpDS3DS1TestSetupEntry = _LpDS3DS1TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1)
)
lpDS3DS1TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1TestSetupEntry.setStatus("mandatory")


class _LpDS3DS1TestPurpose_Type(AsciiString):
    """Custom type lpDS3DS1TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpDS3DS1TestPurpose_Type.__name__ = "AsciiString"
_LpDS3DS1TestPurpose_Object = MibTableColumn
lpDS3DS1TestPurpose = _LpDS3DS1TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 1),
    _LpDS3DS1TestPurpose_Type()
)
lpDS3DS1TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestPurpose.setStatus("mandatory")


class _LpDS3DS1TestType_Type(Integer32):
    """Custom type lpDS3DS1TestType based on Integer32"""
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


_LpDS3DS1TestType_Type.__name__ = "Integer32"
_LpDS3DS1TestType_Object = MibTableColumn
lpDS3DS1TestType = _LpDS3DS1TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 2),
    _LpDS3DS1TestType_Type()
)
lpDS3DS1TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestType.setStatus("mandatory")


class _LpDS3DS1TestFrmSize_Type(Unsigned32):
    """Custom type lpDS3DS1TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpDS3DS1TestFrmSize_Type.__name__ = "Unsigned32"
_LpDS3DS1TestFrmSize_Object = MibTableColumn
lpDS3DS1TestFrmSize = _LpDS3DS1TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 3),
    _LpDS3DS1TestFrmSize_Type()
)
lpDS3DS1TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestFrmSize.setStatus("mandatory")


class _LpDS3DS1TestFrmPatternType_Type(Integer32):
    """Custom type lpDS3DS1TestFrmPatternType based on Integer32"""
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


_LpDS3DS1TestFrmPatternType_Type.__name__ = "Integer32"
_LpDS3DS1TestFrmPatternType_Object = MibTableColumn
lpDS3DS1TestFrmPatternType = _LpDS3DS1TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 4),
    _LpDS3DS1TestFrmPatternType_Type()
)
lpDS3DS1TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestFrmPatternType.setStatus("mandatory")


class _LpDS3DS1TestCustomizedPattern_Type(Hex):
    """Custom type lpDS3DS1TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS3DS1TestCustomizedPattern_Type.__name__ = "Hex"
_LpDS3DS1TestCustomizedPattern_Object = MibTableColumn
lpDS3DS1TestCustomizedPattern = _LpDS3DS1TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 5),
    _LpDS3DS1TestCustomizedPattern_Type()
)
lpDS3DS1TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestCustomizedPattern.setStatus("mandatory")


class _LpDS3DS1TestDataStartDelay_Type(Unsigned32):
    """Custom type lpDS3DS1TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpDS3DS1TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpDS3DS1TestDataStartDelay_Object = MibTableColumn
lpDS3DS1TestDataStartDelay = _LpDS3DS1TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 6),
    _LpDS3DS1TestDataStartDelay_Type()
)
lpDS3DS1TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestDataStartDelay.setStatus("mandatory")


class _LpDS3DS1TestDisplayInterval_Type(Unsigned32):
    """Custom type lpDS3DS1TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpDS3DS1TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpDS3DS1TestDisplayInterval_Object = MibTableColumn
lpDS3DS1TestDisplayInterval = _LpDS3DS1TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 7),
    _LpDS3DS1TestDisplayInterval_Type()
)
lpDS3DS1TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestDisplayInterval.setStatus("mandatory")


class _LpDS3DS1TestDuration_Type(Unsigned32):
    """Custom type lpDS3DS1TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpDS3DS1TestDuration_Type.__name__ = "Unsigned32"
_LpDS3DS1TestDuration_Object = MibTableColumn
lpDS3DS1TestDuration = _LpDS3DS1TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 11, 1, 8),
    _LpDS3DS1TestDuration_Type()
)
lpDS3DS1TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1TestDuration.setStatus("mandatory")
_LpDS3DS1TestResultsTable_Object = MibTable
lpDS3DS1TestResultsTable = _LpDS3DS1TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12)
)
if mibBuilder.loadTexts:
    lpDS3DS1TestResultsTable.setStatus("mandatory")
_LpDS3DS1TestResultsEntry_Object = MibTableRow
lpDS3DS1TestResultsEntry = _LpDS3DS1TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1)
)
lpDS3DS1TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS3DS1TestResultsEntry.setStatus("mandatory")
_LpDS3DS1TestElapsedTime_Type = Counter32
_LpDS3DS1TestElapsedTime_Object = MibTableColumn
lpDS3DS1TestElapsedTime = _LpDS3DS1TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 1),
    _LpDS3DS1TestElapsedTime_Type()
)
lpDS3DS1TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestElapsedTime.setStatus("mandatory")


class _LpDS3DS1TestTimeRemaining_Type(Unsigned32):
    """Custom type lpDS3DS1TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS3DS1TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpDS3DS1TestTimeRemaining_Object = MibTableColumn
lpDS3DS1TestTimeRemaining = _LpDS3DS1TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 2),
    _LpDS3DS1TestTimeRemaining_Type()
)
lpDS3DS1TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestTimeRemaining.setStatus("mandatory")


class _LpDS3DS1TestCauseOfTermination_Type(Integer32):
    """Custom type lpDS3DS1TestCauseOfTermination based on Integer32"""
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


_LpDS3DS1TestCauseOfTermination_Type.__name__ = "Integer32"
_LpDS3DS1TestCauseOfTermination_Object = MibTableColumn
lpDS3DS1TestCauseOfTermination = _LpDS3DS1TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 3),
    _LpDS3DS1TestCauseOfTermination_Type()
)
lpDS3DS1TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestCauseOfTermination.setStatus("mandatory")
_LpDS3DS1TestBitsTx_Type = PassportCounter64
_LpDS3DS1TestBitsTx_Object = MibTableColumn
lpDS3DS1TestBitsTx = _LpDS3DS1TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 4),
    _LpDS3DS1TestBitsTx_Type()
)
lpDS3DS1TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestBitsTx.setStatus("mandatory")
_LpDS3DS1TestBytesTx_Type = PassportCounter64
_LpDS3DS1TestBytesTx_Object = MibTableColumn
lpDS3DS1TestBytesTx = _LpDS3DS1TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 5),
    _LpDS3DS1TestBytesTx_Type()
)
lpDS3DS1TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestBytesTx.setStatus("mandatory")
_LpDS3DS1TestFrmTx_Type = PassportCounter64
_LpDS3DS1TestFrmTx_Object = MibTableColumn
lpDS3DS1TestFrmTx = _LpDS3DS1TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 6),
    _LpDS3DS1TestFrmTx_Type()
)
lpDS3DS1TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestFrmTx.setStatus("mandatory")
_LpDS3DS1TestBitsRx_Type = PassportCounter64
_LpDS3DS1TestBitsRx_Object = MibTableColumn
lpDS3DS1TestBitsRx = _LpDS3DS1TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 7),
    _LpDS3DS1TestBitsRx_Type()
)
lpDS3DS1TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestBitsRx.setStatus("mandatory")
_LpDS3DS1TestBytesRx_Type = PassportCounter64
_LpDS3DS1TestBytesRx_Object = MibTableColumn
lpDS3DS1TestBytesRx = _LpDS3DS1TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 8),
    _LpDS3DS1TestBytesRx_Type()
)
lpDS3DS1TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestBytesRx.setStatus("mandatory")
_LpDS3DS1TestFrmRx_Type = PassportCounter64
_LpDS3DS1TestFrmRx_Object = MibTableColumn
lpDS3DS1TestFrmRx = _LpDS3DS1TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 9),
    _LpDS3DS1TestFrmRx_Type()
)
lpDS3DS1TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestFrmRx.setStatus("mandatory")
_LpDS3DS1TestErroredFrmRx_Type = PassportCounter64
_LpDS3DS1TestErroredFrmRx_Object = MibTableColumn
lpDS3DS1TestErroredFrmRx = _LpDS3DS1TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 10),
    _LpDS3DS1TestErroredFrmRx_Type()
)
lpDS3DS1TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestErroredFrmRx.setStatus("mandatory")


class _LpDS3DS1TestBitErrorRate_Type(AsciiString):
    """Custom type lpDS3DS1TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpDS3DS1TestBitErrorRate_Type.__name__ = "AsciiString"
_LpDS3DS1TestBitErrorRate_Object = MibTableColumn
lpDS3DS1TestBitErrorRate = _LpDS3DS1TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 3, 12, 1, 11),
    _LpDS3DS1TestBitErrorRate_Type()
)
lpDS3DS1TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TestBitErrorRate.setStatus("mandatory")
_LpDS3DS1ProvTable_Object = MibTable
lpDS3DS1ProvTable = _LpDS3DS1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 10)
)
if mibBuilder.loadTexts:
    lpDS3DS1ProvTable.setStatus("mandatory")
_LpDS3DS1ProvEntry_Object = MibTableRow
lpDS3DS1ProvEntry = _LpDS3DS1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 10, 1)
)
lpDS3DS1ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1ProvEntry.setStatus("mandatory")


class _LpDS3DS1LineType_Type(Integer32):
    """Custom type lpDS3DS1LineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("d4", 0),
          ("d4Cas", 4),
          ("esf", 1),
          ("esfCas", 5))
    )


_LpDS3DS1LineType_Type.__name__ = "Integer32"
_LpDS3DS1LineType_Object = MibTableColumn
lpDS3DS1LineType = _LpDS3DS1LineType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 10, 1, 1),
    _LpDS3DS1LineType_Type()
)
lpDS3DS1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1LineType.setStatus("mandatory")


class _LpDS3DS1ZeroCoding_Type(Integer32):
    """Custom type lpDS3DS1ZeroCoding based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bit7Stuffing", 0),
          ("none", 3))
    )


_LpDS3DS1ZeroCoding_Type.__name__ = "Integer32"
_LpDS3DS1ZeroCoding_Object = MibTableColumn
lpDS3DS1ZeroCoding = _LpDS3DS1ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 10, 1, 2),
    _LpDS3DS1ZeroCoding_Type()
)
lpDS3DS1ZeroCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ZeroCoding.setStatus("mandatory")


class _LpDS3DS1ClockingSource_Type(Integer32):
    """Custom type lpDS3DS1ClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("local", 0),
          ("module", 2))
    )


_LpDS3DS1ClockingSource_Type.__name__ = "Integer32"
_LpDS3DS1ClockingSource_Object = MibTableColumn
lpDS3DS1ClockingSource = _LpDS3DS1ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 10, 1, 3),
    _LpDS3DS1ClockingSource_Type()
)
lpDS3DS1ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1ClockingSource.setStatus("mandatory")
_LpDS3DS1CidDataTable_Object = MibTable
lpDS3DS1CidDataTable = _LpDS3DS1CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 11)
)
if mibBuilder.loadTexts:
    lpDS3DS1CidDataTable.setStatus("mandatory")
_LpDS3DS1CidDataEntry_Object = MibTableRow
lpDS3DS1CidDataEntry = _LpDS3DS1CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 11, 1)
)
lpDS3DS1CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1CidDataEntry.setStatus("mandatory")


class _LpDS3DS1CustomerIdentifier_Type(Unsigned32):
    """Custom type lpDS3DS1CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpDS3DS1CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpDS3DS1CustomerIdentifier_Object = MibTableColumn
lpDS3DS1CustomerIdentifier = _LpDS3DS1CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 11, 1, 1),
    _LpDS3DS1CustomerIdentifier_Type()
)
lpDS3DS1CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1CustomerIdentifier.setStatus("mandatory")
_LpDS3DS1AdminInfoTable_Object = MibTable
lpDS3DS1AdminInfoTable = _LpDS3DS1AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 12)
)
if mibBuilder.loadTexts:
    lpDS3DS1AdminInfoTable.setStatus("mandatory")
_LpDS3DS1AdminInfoEntry_Object = MibTableRow
lpDS3DS1AdminInfoEntry = _LpDS3DS1AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 12, 1)
)
lpDS3DS1AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1AdminInfoEntry.setStatus("mandatory")


class _LpDS3DS1Vendor_Type(AsciiString):
    """Custom type lpDS3DS1Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpDS3DS1Vendor_Type.__name__ = "AsciiString"
_LpDS3DS1Vendor_Object = MibTableColumn
lpDS3DS1Vendor = _LpDS3DS1Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 12, 1, 1),
    _LpDS3DS1Vendor_Type()
)
lpDS3DS1Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1Vendor.setStatus("mandatory")


class _LpDS3DS1CommentText_Type(AsciiString):
    """Custom type lpDS3DS1CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpDS3DS1CommentText_Type.__name__ = "AsciiString"
_LpDS3DS1CommentText_Object = MibTableColumn
lpDS3DS1CommentText = _LpDS3DS1CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 12, 1, 2),
    _LpDS3DS1CommentText_Type()
)
lpDS3DS1CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1CommentText.setStatus("mandatory")
_LpDS3DS1IfEntryTable_Object = MibTable
lpDS3DS1IfEntryTable = _LpDS3DS1IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 13)
)
if mibBuilder.loadTexts:
    lpDS3DS1IfEntryTable.setStatus("mandatory")
_LpDS3DS1IfEntryEntry_Object = MibTableRow
lpDS3DS1IfEntryEntry = _LpDS3DS1IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 13, 1)
)
lpDS3DS1IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1IfEntryEntry.setStatus("mandatory")


class _LpDS3DS1IfAdminStatus_Type(Integer32):
    """Custom type lpDS3DS1IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS3DS1IfAdminStatus_Type.__name__ = "Integer32"
_LpDS3DS1IfAdminStatus_Object = MibTableColumn
lpDS3DS1IfAdminStatus = _LpDS3DS1IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 13, 1, 1),
    _LpDS3DS1IfAdminStatus_Type()
)
lpDS3DS1IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3DS1IfAdminStatus.setStatus("mandatory")


class _LpDS3DS1IfIndex_Type(InterfaceIndex):
    """Custom type lpDS3DS1IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpDS3DS1IfIndex_Type.__name__ = "InterfaceIndex"
_LpDS3DS1IfIndex_Object = MibTableColumn
lpDS3DS1IfIndex = _LpDS3DS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 13, 1, 2),
    _LpDS3DS1IfIndex_Type()
)
lpDS3DS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1IfIndex.setStatus("mandatory")
_LpDS3DS1OperStatusTable_Object = MibTable
lpDS3DS1OperStatusTable = _LpDS3DS1OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 14)
)
if mibBuilder.loadTexts:
    lpDS3DS1OperStatusTable.setStatus("mandatory")
_LpDS3DS1OperStatusEntry_Object = MibTableRow
lpDS3DS1OperStatusEntry = _LpDS3DS1OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 14, 1)
)
lpDS3DS1OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1OperStatusEntry.setStatus("mandatory")


class _LpDS3DS1SnmpOperStatus_Type(Integer32):
    """Custom type lpDS3DS1SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS3DS1SnmpOperStatus_Type.__name__ = "Integer32"
_LpDS3DS1SnmpOperStatus_Object = MibTableColumn
lpDS3DS1SnmpOperStatus = _LpDS3DS1SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 14, 1, 1),
    _LpDS3DS1SnmpOperStatus_Type()
)
lpDS3DS1SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1SnmpOperStatus.setStatus("mandatory")
_LpDS3DS1StateTable_Object = MibTable
lpDS3DS1StateTable = _LpDS3DS1StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15)
)
if mibBuilder.loadTexts:
    lpDS3DS1StateTable.setStatus("mandatory")
_LpDS3DS1StateEntry_Object = MibTableRow
lpDS3DS1StateEntry = _LpDS3DS1StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1)
)
lpDS3DS1StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1StateEntry.setStatus("mandatory")


class _LpDS3DS1AdminState_Type(Integer32):
    """Custom type lpDS3DS1AdminState based on Integer32"""
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


_LpDS3DS1AdminState_Type.__name__ = "Integer32"
_LpDS3DS1AdminState_Object = MibTableColumn
lpDS3DS1AdminState = _LpDS3DS1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 1),
    _LpDS3DS1AdminState_Type()
)
lpDS3DS1AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1AdminState.setStatus("mandatory")


class _LpDS3DS1OperationalState_Type(Integer32):
    """Custom type lpDS3DS1OperationalState based on Integer32"""
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


_LpDS3DS1OperationalState_Type.__name__ = "Integer32"
_LpDS3DS1OperationalState_Object = MibTableColumn
lpDS3DS1OperationalState = _LpDS3DS1OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 2),
    _LpDS3DS1OperationalState_Type()
)
lpDS3DS1OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1OperationalState.setStatus("mandatory")


class _LpDS3DS1UsageState_Type(Integer32):
    """Custom type lpDS3DS1UsageState based on Integer32"""
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


_LpDS3DS1UsageState_Type.__name__ = "Integer32"
_LpDS3DS1UsageState_Object = MibTableColumn
lpDS3DS1UsageState = _LpDS3DS1UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 3),
    _LpDS3DS1UsageState_Type()
)
lpDS3DS1UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1UsageState.setStatus("mandatory")


class _LpDS3DS1AvailabilityStatus_Type(OctetString):
    """Custom type lpDS3DS1AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpDS3DS1AvailabilityStatus_Type.__name__ = "OctetString"
_LpDS3DS1AvailabilityStatus_Object = MibTableColumn
lpDS3DS1AvailabilityStatus = _LpDS3DS1AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 4),
    _LpDS3DS1AvailabilityStatus_Type()
)
lpDS3DS1AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1AvailabilityStatus.setStatus("mandatory")


class _LpDS3DS1ProceduralStatus_Type(OctetString):
    """Custom type lpDS3DS1ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3DS1ProceduralStatus_Type.__name__ = "OctetString"
_LpDS3DS1ProceduralStatus_Object = MibTableColumn
lpDS3DS1ProceduralStatus = _LpDS3DS1ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 5),
    _LpDS3DS1ProceduralStatus_Type()
)
lpDS3DS1ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ProceduralStatus.setStatus("mandatory")


class _LpDS3DS1ControlStatus_Type(OctetString):
    """Custom type lpDS3DS1ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3DS1ControlStatus_Type.__name__ = "OctetString"
_LpDS3DS1ControlStatus_Object = MibTableColumn
lpDS3DS1ControlStatus = _LpDS3DS1ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 6),
    _LpDS3DS1ControlStatus_Type()
)
lpDS3DS1ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ControlStatus.setStatus("mandatory")


class _LpDS3DS1AlarmStatus_Type(OctetString):
    """Custom type lpDS3DS1AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3DS1AlarmStatus_Type.__name__ = "OctetString"
_LpDS3DS1AlarmStatus_Object = MibTableColumn
lpDS3DS1AlarmStatus = _LpDS3DS1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 7),
    _LpDS3DS1AlarmStatus_Type()
)
lpDS3DS1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1AlarmStatus.setStatus("mandatory")


class _LpDS3DS1StandbyStatus_Type(Integer32):
    """Custom type lpDS3DS1StandbyStatus based on Integer32"""
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


_LpDS3DS1StandbyStatus_Type.__name__ = "Integer32"
_LpDS3DS1StandbyStatus_Object = MibTableColumn
lpDS3DS1StandbyStatus = _LpDS3DS1StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 8),
    _LpDS3DS1StandbyStatus_Type()
)
lpDS3DS1StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1StandbyStatus.setStatus("mandatory")


class _LpDS3DS1UnknownStatus_Type(Integer32):
    """Custom type lpDS3DS1UnknownStatus based on Integer32"""
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


_LpDS3DS1UnknownStatus_Type.__name__ = "Integer32"
_LpDS3DS1UnknownStatus_Object = MibTableColumn
lpDS3DS1UnknownStatus = _LpDS3DS1UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 15, 1, 9),
    _LpDS3DS1UnknownStatus_Type()
)
lpDS3DS1UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1UnknownStatus.setStatus("mandatory")
_LpDS3DS1OperTable_Object = MibTable
lpDS3DS1OperTable = _LpDS3DS1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 16)
)
if mibBuilder.loadTexts:
    lpDS3DS1OperTable.setStatus("mandatory")
_LpDS3DS1OperEntry_Object = MibTableRow
lpDS3DS1OperEntry = _LpDS3DS1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 16, 1)
)
lpDS3DS1OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1OperEntry.setStatus("mandatory")


class _LpDS3DS1RxAisAlarm_Type(Integer32):
    """Custom type lpDS3DS1RxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3DS1RxAisAlarm_Type.__name__ = "Integer32"
_LpDS3DS1RxAisAlarm_Object = MibTableColumn
lpDS3DS1RxAisAlarm = _LpDS3DS1RxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 16, 1, 1),
    _LpDS3DS1RxAisAlarm_Type()
)
lpDS3DS1RxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1RxAisAlarm.setStatus("mandatory")


class _LpDS3DS1LofAlarm_Type(Integer32):
    """Custom type lpDS3DS1LofAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3DS1LofAlarm_Type.__name__ = "Integer32"
_LpDS3DS1LofAlarm_Object = MibTableColumn
lpDS3DS1LofAlarm = _LpDS3DS1LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 16, 1, 2),
    _LpDS3DS1LofAlarm_Type()
)
lpDS3DS1LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1LofAlarm.setStatus("mandatory")


class _LpDS3DS1RxRaiAlarm_Type(Integer32):
    """Custom type lpDS3DS1RxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3DS1RxRaiAlarm_Type.__name__ = "Integer32"
_LpDS3DS1RxRaiAlarm_Object = MibTableColumn
lpDS3DS1RxRaiAlarm = _LpDS3DS1RxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 16, 1, 3),
    _LpDS3DS1RxRaiAlarm_Type()
)
lpDS3DS1RxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1RxRaiAlarm.setStatus("mandatory")


class _LpDS3DS1TxAisAlarm_Type(Integer32):
    """Custom type lpDS3DS1TxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3DS1TxAisAlarm_Type.__name__ = "Integer32"
_LpDS3DS1TxAisAlarm_Object = MibTableColumn
lpDS3DS1TxAisAlarm = _LpDS3DS1TxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 16, 1, 4),
    _LpDS3DS1TxAisAlarm_Type()
)
lpDS3DS1TxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TxAisAlarm.setStatus("mandatory")


class _LpDS3DS1TxRaiAlarm_Type(Integer32):
    """Custom type lpDS3DS1TxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3DS1TxRaiAlarm_Type.__name__ = "Integer32"
_LpDS3DS1TxRaiAlarm_Object = MibTableColumn
lpDS3DS1TxRaiAlarm = _LpDS3DS1TxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 16, 1, 5),
    _LpDS3DS1TxRaiAlarm_Type()
)
lpDS3DS1TxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1TxRaiAlarm.setStatus("mandatory")
_LpDS3DS1StatsTable_Object = MibTable
lpDS3DS1StatsTable = _LpDS3DS1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17)
)
if mibBuilder.loadTexts:
    lpDS3DS1StatsTable.setStatus("mandatory")
_LpDS3DS1StatsEntry_Object = MibTableRow
lpDS3DS1StatsEntry = _LpDS3DS1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1)
)
lpDS3DS1StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3DS1Index"),
)
if mibBuilder.loadTexts:
    lpDS3DS1StatsEntry.setStatus("mandatory")
_LpDS3DS1RunningTime_Type = Counter32
_LpDS3DS1RunningTime_Object = MibTableColumn
lpDS3DS1RunningTime = _LpDS3DS1RunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 1),
    _LpDS3DS1RunningTime_Type()
)
lpDS3DS1RunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1RunningTime.setStatus("mandatory")
_LpDS3DS1ErrorFreeSec_Type = Counter32
_LpDS3DS1ErrorFreeSec_Object = MibTableColumn
lpDS3DS1ErrorFreeSec = _LpDS3DS1ErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 2),
    _LpDS3DS1ErrorFreeSec_Type()
)
lpDS3DS1ErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ErrorFreeSec.setStatus("mandatory")
_LpDS3DS1ErroredSec_Type = Counter32
_LpDS3DS1ErroredSec_Object = MibTableColumn
lpDS3DS1ErroredSec = _LpDS3DS1ErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 3),
    _LpDS3DS1ErroredSec_Type()
)
lpDS3DS1ErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1ErroredSec.setStatus("mandatory")
_LpDS3DS1SevErroredSec_Type = Counter32
_LpDS3DS1SevErroredSec_Object = MibTableColumn
lpDS3DS1SevErroredSec = _LpDS3DS1SevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 4),
    _LpDS3DS1SevErroredSec_Type()
)
lpDS3DS1SevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1SevErroredSec.setStatus("mandatory")
_LpDS3DS1SevErroredFrmSec_Type = Counter32
_LpDS3DS1SevErroredFrmSec_Object = MibTableColumn
lpDS3DS1SevErroredFrmSec = _LpDS3DS1SevErroredFrmSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 5),
    _LpDS3DS1SevErroredFrmSec_Type()
)
lpDS3DS1SevErroredFrmSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1SevErroredFrmSec.setStatus("mandatory")
_LpDS3DS1UnavailSec_Type = Counter32
_LpDS3DS1UnavailSec_Object = MibTableColumn
lpDS3DS1UnavailSec = _LpDS3DS1UnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 6),
    _LpDS3DS1UnavailSec_Type()
)
lpDS3DS1UnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1UnavailSec.setStatus("mandatory")
_LpDS3DS1CrcErrors_Type = Counter32
_LpDS3DS1CrcErrors_Object = MibTableColumn
lpDS3DS1CrcErrors = _LpDS3DS1CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 7),
    _LpDS3DS1CrcErrors_Type()
)
lpDS3DS1CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1CrcErrors.setStatus("mandatory")
_LpDS3DS1FrmErrors_Type = Counter32
_LpDS3DS1FrmErrors_Object = MibTableColumn
lpDS3DS1FrmErrors = _LpDS3DS1FrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 8),
    _LpDS3DS1FrmErrors_Type()
)
lpDS3DS1FrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1FrmErrors.setStatus("mandatory")
_LpDS3DS1SlipErrors_Type = Counter32
_LpDS3DS1SlipErrors_Object = MibTableColumn
lpDS3DS1SlipErrors = _LpDS3DS1SlipErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 6, 17, 1, 9),
    _LpDS3DS1SlipErrors_Type()
)
lpDS3DS1SlipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3DS1SlipErrors.setStatus("mandatory")
_LpDS3ProvTable_Object = MibTable
lpDS3ProvTable = _LpDS3ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 10)
)
if mibBuilder.loadTexts:
    lpDS3ProvTable.setStatus("mandatory")
_LpDS3ProvEntry_Object = MibTableRow
lpDS3ProvEntry = _LpDS3ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 10, 1)
)
lpDS3ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3ProvEntry.setStatus("mandatory")


class _LpDS3CbitParity_Type(Integer32):
    """Custom type lpDS3CbitParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS3CbitParity_Type.__name__ = "Integer32"
_LpDS3CbitParity_Object = MibTableColumn
lpDS3CbitParity = _LpDS3CbitParity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 10, 1, 1),
    _LpDS3CbitParity_Type()
)
lpDS3CbitParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3CbitParity.setStatus("mandatory")


class _LpDS3LineLength_Type(Unsigned32):
    """Custom type lpDS3LineLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 450),
    )


_LpDS3LineLength_Type.__name__ = "Unsigned32"
_LpDS3LineLength_Object = MibTableColumn
lpDS3LineLength = _LpDS3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 10, 1, 2),
    _LpDS3LineLength_Type()
)
lpDS3LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3LineLength.setStatus("mandatory")


class _LpDS3ClockingSource_Type(Integer32):
    """Custom type lpDS3ClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("local", 0),
          ("module", 2),
          ("otherPort", 4))
    )


_LpDS3ClockingSource_Type.__name__ = "Integer32"
_LpDS3ClockingSource_Object = MibTableColumn
lpDS3ClockingSource = _LpDS3ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 10, 1, 3),
    _LpDS3ClockingSource_Type()
)
lpDS3ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3ClockingSource.setStatus("mandatory")
_LpDS3ApplicationFramerName_Type = Link
_LpDS3ApplicationFramerName_Object = MibTableColumn
lpDS3ApplicationFramerName = _LpDS3ApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 10, 1, 4),
    _LpDS3ApplicationFramerName_Type()
)
lpDS3ApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3ApplicationFramerName.setStatus("mandatory")


class _LpDS3Mapping_Type(Integer32):
    """Custom type lpDS3Mapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("plcp", 1))
    )


_LpDS3Mapping_Type.__name__ = "Integer32"
_LpDS3Mapping_Object = MibTableColumn
lpDS3Mapping = _LpDS3Mapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 10, 1, 5),
    _LpDS3Mapping_Type()
)
lpDS3Mapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3Mapping.setStatus("mandatory")
_LpDS3CidDataTable_Object = MibTable
lpDS3CidDataTable = _LpDS3CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 11)
)
if mibBuilder.loadTexts:
    lpDS3CidDataTable.setStatus("mandatory")
_LpDS3CidDataEntry_Object = MibTableRow
lpDS3CidDataEntry = _LpDS3CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 11, 1)
)
lpDS3CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3CidDataEntry.setStatus("mandatory")


class _LpDS3CustomerIdentifier_Type(Unsigned32):
    """Custom type lpDS3CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpDS3CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpDS3CustomerIdentifier_Object = MibTableColumn
lpDS3CustomerIdentifier = _LpDS3CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 11, 1, 1),
    _LpDS3CustomerIdentifier_Type()
)
lpDS3CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3CustomerIdentifier.setStatus("mandatory")
_LpDS3AdminInfoTable_Object = MibTable
lpDS3AdminInfoTable = _LpDS3AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 12)
)
if mibBuilder.loadTexts:
    lpDS3AdminInfoTable.setStatus("mandatory")
_LpDS3AdminInfoEntry_Object = MibTableRow
lpDS3AdminInfoEntry = _LpDS3AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 12, 1)
)
lpDS3AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3AdminInfoEntry.setStatus("mandatory")


class _LpDS3Vendor_Type(AsciiString):
    """Custom type lpDS3Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpDS3Vendor_Type.__name__ = "AsciiString"
_LpDS3Vendor_Object = MibTableColumn
lpDS3Vendor = _LpDS3Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 12, 1, 1),
    _LpDS3Vendor_Type()
)
lpDS3Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3Vendor.setStatus("mandatory")


class _LpDS3CommentText_Type(AsciiString):
    """Custom type lpDS3CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpDS3CommentText_Type.__name__ = "AsciiString"
_LpDS3CommentText_Object = MibTableColumn
lpDS3CommentText = _LpDS3CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 12, 1, 2),
    _LpDS3CommentText_Type()
)
lpDS3CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3CommentText.setStatus("mandatory")
_LpDS3IfEntryTable_Object = MibTable
lpDS3IfEntryTable = _LpDS3IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 13)
)
if mibBuilder.loadTexts:
    lpDS3IfEntryTable.setStatus("mandatory")
_LpDS3IfEntryEntry_Object = MibTableRow
lpDS3IfEntryEntry = _LpDS3IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 13, 1)
)
lpDS3IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3IfEntryEntry.setStatus("mandatory")


class _LpDS3IfAdminStatus_Type(Integer32):
    """Custom type lpDS3IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS3IfAdminStatus_Type.__name__ = "Integer32"
_LpDS3IfAdminStatus_Object = MibTableColumn
lpDS3IfAdminStatus = _LpDS3IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 13, 1, 1),
    _LpDS3IfAdminStatus_Type()
)
lpDS3IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS3IfAdminStatus.setStatus("mandatory")


class _LpDS3IfIndex_Type(InterfaceIndex):
    """Custom type lpDS3IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpDS3IfIndex_Type.__name__ = "InterfaceIndex"
_LpDS3IfIndex_Object = MibTableColumn
lpDS3IfIndex = _LpDS3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 13, 1, 2),
    _LpDS3IfIndex_Type()
)
lpDS3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3IfIndex.setStatus("mandatory")
_LpDS3OperStatusTable_Object = MibTable
lpDS3OperStatusTable = _LpDS3OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 14)
)
if mibBuilder.loadTexts:
    lpDS3OperStatusTable.setStatus("mandatory")
_LpDS3OperStatusEntry_Object = MibTableRow
lpDS3OperStatusEntry = _LpDS3OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 14, 1)
)
lpDS3OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3OperStatusEntry.setStatus("mandatory")


class _LpDS3SnmpOperStatus_Type(Integer32):
    """Custom type lpDS3SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS3SnmpOperStatus_Type.__name__ = "Integer32"
_LpDS3SnmpOperStatus_Object = MibTableColumn
lpDS3SnmpOperStatus = _LpDS3SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 14, 1, 1),
    _LpDS3SnmpOperStatus_Type()
)
lpDS3SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3SnmpOperStatus.setStatus("mandatory")
_LpDS3StateTable_Object = MibTable
lpDS3StateTable = _LpDS3StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15)
)
if mibBuilder.loadTexts:
    lpDS3StateTable.setStatus("mandatory")
_LpDS3StateEntry_Object = MibTableRow
lpDS3StateEntry = _LpDS3StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1)
)
lpDS3StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3StateEntry.setStatus("mandatory")


class _LpDS3AdminState_Type(Integer32):
    """Custom type lpDS3AdminState based on Integer32"""
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


_LpDS3AdminState_Type.__name__ = "Integer32"
_LpDS3AdminState_Object = MibTableColumn
lpDS3AdminState = _LpDS3AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 1),
    _LpDS3AdminState_Type()
)
lpDS3AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3AdminState.setStatus("mandatory")


class _LpDS3OperationalState_Type(Integer32):
    """Custom type lpDS3OperationalState based on Integer32"""
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


_LpDS3OperationalState_Type.__name__ = "Integer32"
_LpDS3OperationalState_Object = MibTableColumn
lpDS3OperationalState = _LpDS3OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 2),
    _LpDS3OperationalState_Type()
)
lpDS3OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3OperationalState.setStatus("mandatory")


class _LpDS3UsageState_Type(Integer32):
    """Custom type lpDS3UsageState based on Integer32"""
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


_LpDS3UsageState_Type.__name__ = "Integer32"
_LpDS3UsageState_Object = MibTableColumn
lpDS3UsageState = _LpDS3UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 3),
    _LpDS3UsageState_Type()
)
lpDS3UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3UsageState.setStatus("mandatory")


class _LpDS3AvailabilityStatus_Type(OctetString):
    """Custom type lpDS3AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpDS3AvailabilityStatus_Type.__name__ = "OctetString"
_LpDS3AvailabilityStatus_Object = MibTableColumn
lpDS3AvailabilityStatus = _LpDS3AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 4),
    _LpDS3AvailabilityStatus_Type()
)
lpDS3AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3AvailabilityStatus.setStatus("mandatory")


class _LpDS3ProceduralStatus_Type(OctetString):
    """Custom type lpDS3ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3ProceduralStatus_Type.__name__ = "OctetString"
_LpDS3ProceduralStatus_Object = MibTableColumn
lpDS3ProceduralStatus = _LpDS3ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 5),
    _LpDS3ProceduralStatus_Type()
)
lpDS3ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3ProceduralStatus.setStatus("mandatory")


class _LpDS3ControlStatus_Type(OctetString):
    """Custom type lpDS3ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3ControlStatus_Type.__name__ = "OctetString"
_LpDS3ControlStatus_Object = MibTableColumn
lpDS3ControlStatus = _LpDS3ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 6),
    _LpDS3ControlStatus_Type()
)
lpDS3ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3ControlStatus.setStatus("mandatory")


class _LpDS3AlarmStatus_Type(OctetString):
    """Custom type lpDS3AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS3AlarmStatus_Type.__name__ = "OctetString"
_LpDS3AlarmStatus_Object = MibTableColumn
lpDS3AlarmStatus = _LpDS3AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 7),
    _LpDS3AlarmStatus_Type()
)
lpDS3AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3AlarmStatus.setStatus("mandatory")


class _LpDS3StandbyStatus_Type(Integer32):
    """Custom type lpDS3StandbyStatus based on Integer32"""
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


_LpDS3StandbyStatus_Type.__name__ = "Integer32"
_LpDS3StandbyStatus_Object = MibTableColumn
lpDS3StandbyStatus = _LpDS3StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 8),
    _LpDS3StandbyStatus_Type()
)
lpDS3StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3StandbyStatus.setStatus("mandatory")


class _LpDS3UnknownStatus_Type(Integer32):
    """Custom type lpDS3UnknownStatus based on Integer32"""
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


_LpDS3UnknownStatus_Type.__name__ = "Integer32"
_LpDS3UnknownStatus_Object = MibTableColumn
lpDS3UnknownStatus = _LpDS3UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 15, 1, 9),
    _LpDS3UnknownStatus_Type()
)
lpDS3UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3UnknownStatus.setStatus("mandatory")
_LpDS3OperTable_Object = MibTable
lpDS3OperTable = _LpDS3OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16)
)
if mibBuilder.loadTexts:
    lpDS3OperTable.setStatus("mandatory")
_LpDS3OperEntry_Object = MibTableRow
lpDS3OperEntry = _LpDS3OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1)
)
lpDS3OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3OperEntry.setStatus("mandatory")


class _LpDS3LosAlarm_Type(Integer32):
    """Custom type lpDS3LosAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3LosAlarm_Type.__name__ = "Integer32"
_LpDS3LosAlarm_Object = MibTableColumn
lpDS3LosAlarm = _LpDS3LosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 1),
    _LpDS3LosAlarm_Type()
)
lpDS3LosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3LosAlarm.setStatus("mandatory")


class _LpDS3LofAlarm_Type(Integer32):
    """Custom type lpDS3LofAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3LofAlarm_Type.__name__ = "Integer32"
_LpDS3LofAlarm_Object = MibTableColumn
lpDS3LofAlarm = _LpDS3LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 2),
    _LpDS3LofAlarm_Type()
)
lpDS3LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3LofAlarm.setStatus("mandatory")


class _LpDS3RxAisAlarm_Type(Integer32):
    """Custom type lpDS3RxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3RxAisAlarm_Type.__name__ = "Integer32"
_LpDS3RxAisAlarm_Object = MibTableColumn
lpDS3RxAisAlarm = _LpDS3RxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 3),
    _LpDS3RxAisAlarm_Type()
)
lpDS3RxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3RxAisAlarm.setStatus("mandatory")


class _LpDS3RxRaiAlarm_Type(Integer32):
    """Custom type lpDS3RxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS3RxRaiAlarm_Type.__name__ = "Integer32"
_LpDS3RxRaiAlarm_Object = MibTableColumn
lpDS3RxRaiAlarm = _LpDS3RxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 4),
    _LpDS3RxRaiAlarm_Type()
)
lpDS3RxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3RxRaiAlarm.setStatus("mandatory")


class _LpDS3RxIdle_Type(Integer32):
    """Custom type lpDS3RxIdle based on Integer32"""
    defaultValue = 1

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


_LpDS3RxIdle_Type.__name__ = "Integer32"
_LpDS3RxIdle_Object = MibTableColumn
lpDS3RxIdle = _LpDS3RxIdle_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 5),
    _LpDS3RxIdle_Type()
)
lpDS3RxIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3RxIdle.setStatus("mandatory")


class _LpDS3TxAis_Type(Integer32):
    """Custom type lpDS3TxAis based on Integer32"""
    defaultValue = 1

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


_LpDS3TxAis_Type.__name__ = "Integer32"
_LpDS3TxAis_Object = MibTableColumn
lpDS3TxAis = _LpDS3TxAis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 6),
    _LpDS3TxAis_Type()
)
lpDS3TxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TxAis.setStatus("mandatory")


class _LpDS3TxRai_Type(Integer32):
    """Custom type lpDS3TxRai based on Integer32"""
    defaultValue = 1

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


_LpDS3TxRai_Type.__name__ = "Integer32"
_LpDS3TxRai_Object = MibTableColumn
lpDS3TxRai = _LpDS3TxRai_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 7),
    _LpDS3TxRai_Type()
)
lpDS3TxRai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TxRai.setStatus("mandatory")


class _LpDS3TxIdle_Type(Integer32):
    """Custom type lpDS3TxIdle based on Integer32"""
    defaultValue = 1

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


_LpDS3TxIdle_Type.__name__ = "Integer32"
_LpDS3TxIdle_Object = MibTableColumn
lpDS3TxIdle = _LpDS3TxIdle_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 16, 1, 8),
    _LpDS3TxIdle_Type()
)
lpDS3TxIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3TxIdle.setStatus("mandatory")
_LpDS3StatsTable_Object = MibTable
lpDS3StatsTable = _LpDS3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17)
)
if mibBuilder.loadTexts:
    lpDS3StatsTable.setStatus("mandatory")
_LpDS3StatsEntry_Object = MibTableRow
lpDS3StatsEntry = _LpDS3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1)
)
lpDS3StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS3Index"),
)
if mibBuilder.loadTexts:
    lpDS3StatsEntry.setStatus("mandatory")
_LpDS3RunningTime_Type = Counter32
_LpDS3RunningTime_Object = MibTableColumn
lpDS3RunningTime = _LpDS3RunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 1),
    _LpDS3RunningTime_Type()
)
lpDS3RunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3RunningTime.setStatus("mandatory")
_LpDS3ErrorFreeSec_Type = Counter32
_LpDS3ErrorFreeSec_Object = MibTableColumn
lpDS3ErrorFreeSec = _LpDS3ErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 2),
    _LpDS3ErrorFreeSec_Type()
)
lpDS3ErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3ErrorFreeSec.setStatus("mandatory")
_LpDS3LineCodeViolations_Type = Counter32
_LpDS3LineCodeViolations_Object = MibTableColumn
lpDS3LineCodeViolations = _LpDS3LineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 3),
    _LpDS3LineCodeViolations_Type()
)
lpDS3LineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3LineCodeViolations.setStatus("mandatory")
_LpDS3LineErroredSec_Type = Counter32
_LpDS3LineErroredSec_Object = MibTableColumn
lpDS3LineErroredSec = _LpDS3LineErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 4),
    _LpDS3LineErroredSec_Type()
)
lpDS3LineErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3LineErroredSec.setStatus("mandatory")
_LpDS3LineSevErroredSec_Type = Counter32
_LpDS3LineSevErroredSec_Object = MibTableColumn
lpDS3LineSevErroredSec = _LpDS3LineSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 5),
    _LpDS3LineSevErroredSec_Type()
)
lpDS3LineSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3LineSevErroredSec.setStatus("mandatory")
_LpDS3LineLosSec_Type = Counter32
_LpDS3LineLosSec_Object = MibTableColumn
lpDS3LineLosSec = _LpDS3LineLosSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 6),
    _LpDS3LineLosSec_Type()
)
lpDS3LineLosSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3LineLosSec.setStatus("mandatory")
_LpDS3LineFailures_Type = Counter32
_LpDS3LineFailures_Object = MibTableColumn
lpDS3LineFailures = _LpDS3LineFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 7),
    _LpDS3LineFailures_Type()
)
lpDS3LineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3LineFailures.setStatus("mandatory")
_LpDS3PathCodeViolations_Type = Counter32
_LpDS3PathCodeViolations_Object = MibTableColumn
lpDS3PathCodeViolations = _LpDS3PathCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 8),
    _LpDS3PathCodeViolations_Type()
)
lpDS3PathCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PathCodeViolations.setStatus("mandatory")
_LpDS3PathErroredSec_Type = Counter32
_LpDS3PathErroredSec_Object = MibTableColumn
lpDS3PathErroredSec = _LpDS3PathErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 9),
    _LpDS3PathErroredSec_Type()
)
lpDS3PathErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PathErroredSec.setStatus("mandatory")
_LpDS3PathSevErroredSec_Type = Counter32
_LpDS3PathSevErroredSec_Object = MibTableColumn
lpDS3PathSevErroredSec = _LpDS3PathSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 10),
    _LpDS3PathSevErroredSec_Type()
)
lpDS3PathSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PathSevErroredSec.setStatus("mandatory")
_LpDS3PathSefAisSec_Type = Counter32
_LpDS3PathSefAisSec_Object = MibTableColumn
lpDS3PathSefAisSec = _LpDS3PathSefAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 11),
    _LpDS3PathSefAisSec_Type()
)
lpDS3PathSefAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PathSefAisSec.setStatus("mandatory")
_LpDS3PathUnavailSec_Type = Counter32
_LpDS3PathUnavailSec_Object = MibTableColumn
lpDS3PathUnavailSec = _LpDS3PathUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 12),
    _LpDS3PathUnavailSec_Type()
)
lpDS3PathUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PathUnavailSec.setStatus("mandatory")
_LpDS3PathFailures_Type = Counter32
_LpDS3PathFailures_Object = MibTableColumn
lpDS3PathFailures = _LpDS3PathFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 5, 17, 1, 13),
    _LpDS3PathFailures_Type()
)
lpDS3PathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS3PathFailures.setStatus("mandatory")
_LpE3_ObjectIdentity = ObjectIdentity
lpE3 = _LpE3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6)
)
_LpE3RowStatusTable_Object = MibTable
lpE3RowStatusTable = _LpE3RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 1)
)
if mibBuilder.loadTexts:
    lpE3RowStatusTable.setStatus("mandatory")
_LpE3RowStatusEntry_Object = MibTableRow
lpE3RowStatusEntry = _LpE3RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 1, 1)
)
lpE3RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3RowStatusEntry.setStatus("mandatory")
_LpE3RowStatus_Type = RowStatus
_LpE3RowStatus_Object = MibTableColumn
lpE3RowStatus = _LpE3RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 1, 1, 1),
    _LpE3RowStatus_Type()
)
lpE3RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3RowStatus.setStatus("mandatory")
_LpE3ComponentName_Type = DisplayString
_LpE3ComponentName_Object = MibTableColumn
lpE3ComponentName = _LpE3ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 1, 1, 2),
    _LpE3ComponentName_Type()
)
lpE3ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3ComponentName.setStatus("mandatory")
_LpE3StorageType_Type = StorageType
_LpE3StorageType_Object = MibTableColumn
lpE3StorageType = _LpE3StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 1, 1, 4),
    _LpE3StorageType_Type()
)
lpE3StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3StorageType.setStatus("mandatory")


class _LpE3Index_Type(Integer32):
    """Custom type lpE3Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LpE3Index_Type.__name__ = "Integer32"
_LpE3Index_Object = MibTableColumn
lpE3Index = _LpE3Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 1, 1, 10),
    _LpE3Index_Type()
)
lpE3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE3Index.setStatus("mandatory")
_LpE3Test_ObjectIdentity = ObjectIdentity
lpE3Test = _LpE3Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2)
)
_LpE3TestRowStatusTable_Object = MibTable
lpE3TestRowStatusTable = _LpE3TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 1)
)
if mibBuilder.loadTexts:
    lpE3TestRowStatusTable.setStatus("mandatory")
_LpE3TestRowStatusEntry_Object = MibTableRow
lpE3TestRowStatusEntry = _LpE3TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 1, 1)
)
lpE3TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3TestIndex"),
)
if mibBuilder.loadTexts:
    lpE3TestRowStatusEntry.setStatus("mandatory")
_LpE3TestRowStatus_Type = RowStatus
_LpE3TestRowStatus_Object = MibTableColumn
lpE3TestRowStatus = _LpE3TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 1, 1, 1),
    _LpE3TestRowStatus_Type()
)
lpE3TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestRowStatus.setStatus("mandatory")
_LpE3TestComponentName_Type = DisplayString
_LpE3TestComponentName_Object = MibTableColumn
lpE3TestComponentName = _LpE3TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 1, 1, 2),
    _LpE3TestComponentName_Type()
)
lpE3TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestComponentName.setStatus("mandatory")
_LpE3TestStorageType_Type = StorageType
_LpE3TestStorageType_Object = MibTableColumn
lpE3TestStorageType = _LpE3TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 1, 1, 4),
    _LpE3TestStorageType_Type()
)
lpE3TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestStorageType.setStatus("mandatory")
_LpE3TestIndex_Type = NonReplicated
_LpE3TestIndex_Object = MibTableColumn
lpE3TestIndex = _LpE3TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 1, 1, 10),
    _LpE3TestIndex_Type()
)
lpE3TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE3TestIndex.setStatus("mandatory")
_LpE3TestStateTable_Object = MibTable
lpE3TestStateTable = _LpE3TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 10)
)
if mibBuilder.loadTexts:
    lpE3TestStateTable.setStatus("mandatory")
_LpE3TestStateEntry_Object = MibTableRow
lpE3TestStateEntry = _LpE3TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 10, 1)
)
lpE3TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3TestIndex"),
)
if mibBuilder.loadTexts:
    lpE3TestStateEntry.setStatus("mandatory")


class _LpE3TestAdminState_Type(Integer32):
    """Custom type lpE3TestAdminState based on Integer32"""
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


_LpE3TestAdminState_Type.__name__ = "Integer32"
_LpE3TestAdminState_Object = MibTableColumn
lpE3TestAdminState = _LpE3TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 10, 1, 1),
    _LpE3TestAdminState_Type()
)
lpE3TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestAdminState.setStatus("mandatory")


class _LpE3TestOperationalState_Type(Integer32):
    """Custom type lpE3TestOperationalState based on Integer32"""
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


_LpE3TestOperationalState_Type.__name__ = "Integer32"
_LpE3TestOperationalState_Object = MibTableColumn
lpE3TestOperationalState = _LpE3TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 10, 1, 2),
    _LpE3TestOperationalState_Type()
)
lpE3TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestOperationalState.setStatus("mandatory")


class _LpE3TestUsageState_Type(Integer32):
    """Custom type lpE3TestUsageState based on Integer32"""
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


_LpE3TestUsageState_Type.__name__ = "Integer32"
_LpE3TestUsageState_Object = MibTableColumn
lpE3TestUsageState = _LpE3TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 10, 1, 3),
    _LpE3TestUsageState_Type()
)
lpE3TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestUsageState.setStatus("mandatory")
_LpE3TestSetupTable_Object = MibTable
lpE3TestSetupTable = _LpE3TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11)
)
if mibBuilder.loadTexts:
    lpE3TestSetupTable.setStatus("mandatory")
_LpE3TestSetupEntry_Object = MibTableRow
lpE3TestSetupEntry = _LpE3TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1)
)
lpE3TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3TestIndex"),
)
if mibBuilder.loadTexts:
    lpE3TestSetupEntry.setStatus("mandatory")


class _LpE3TestPurpose_Type(AsciiString):
    """Custom type lpE3TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpE3TestPurpose_Type.__name__ = "AsciiString"
_LpE3TestPurpose_Object = MibTableColumn
lpE3TestPurpose = _LpE3TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 1),
    _LpE3TestPurpose_Type()
)
lpE3TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestPurpose.setStatus("mandatory")


class _LpE3TestType_Type(Integer32):
    """Custom type lpE3TestType based on Integer32"""
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


_LpE3TestType_Type.__name__ = "Integer32"
_LpE3TestType_Object = MibTableColumn
lpE3TestType = _LpE3TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 2),
    _LpE3TestType_Type()
)
lpE3TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestType.setStatus("mandatory")


class _LpE3TestFrmSize_Type(Unsigned32):
    """Custom type lpE3TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpE3TestFrmSize_Type.__name__ = "Unsigned32"
_LpE3TestFrmSize_Object = MibTableColumn
lpE3TestFrmSize = _LpE3TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 3),
    _LpE3TestFrmSize_Type()
)
lpE3TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestFrmSize.setStatus("mandatory")


class _LpE3TestFrmPatternType_Type(Integer32):
    """Custom type lpE3TestFrmPatternType based on Integer32"""
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


_LpE3TestFrmPatternType_Type.__name__ = "Integer32"
_LpE3TestFrmPatternType_Object = MibTableColumn
lpE3TestFrmPatternType = _LpE3TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 4),
    _LpE3TestFrmPatternType_Type()
)
lpE3TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestFrmPatternType.setStatus("mandatory")


class _LpE3TestCustomizedPattern_Type(Hex):
    """Custom type lpE3TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpE3TestCustomizedPattern_Type.__name__ = "Hex"
_LpE3TestCustomizedPattern_Object = MibTableColumn
lpE3TestCustomizedPattern = _LpE3TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 5),
    _LpE3TestCustomizedPattern_Type()
)
lpE3TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestCustomizedPattern.setStatus("mandatory")


class _LpE3TestDataStartDelay_Type(Unsigned32):
    """Custom type lpE3TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpE3TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpE3TestDataStartDelay_Object = MibTableColumn
lpE3TestDataStartDelay = _LpE3TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 6),
    _LpE3TestDataStartDelay_Type()
)
lpE3TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestDataStartDelay.setStatus("mandatory")


class _LpE3TestDisplayInterval_Type(Unsigned32):
    """Custom type lpE3TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpE3TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpE3TestDisplayInterval_Object = MibTableColumn
lpE3TestDisplayInterval = _LpE3TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 7),
    _LpE3TestDisplayInterval_Type()
)
lpE3TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestDisplayInterval.setStatus("mandatory")


class _LpE3TestDuration_Type(Unsigned32):
    """Custom type lpE3TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpE3TestDuration_Type.__name__ = "Unsigned32"
_LpE3TestDuration_Object = MibTableColumn
lpE3TestDuration = _LpE3TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 11, 1, 8),
    _LpE3TestDuration_Type()
)
lpE3TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3TestDuration.setStatus("mandatory")
_LpE3TestResultsTable_Object = MibTable
lpE3TestResultsTable = _LpE3TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12)
)
if mibBuilder.loadTexts:
    lpE3TestResultsTable.setStatus("mandatory")
_LpE3TestResultsEntry_Object = MibTableRow
lpE3TestResultsEntry = _LpE3TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1)
)
lpE3TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3TestIndex"),
)
if mibBuilder.loadTexts:
    lpE3TestResultsEntry.setStatus("mandatory")
_LpE3TestElapsedTime_Type = Counter32
_LpE3TestElapsedTime_Object = MibTableColumn
lpE3TestElapsedTime = _LpE3TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 1),
    _LpE3TestElapsedTime_Type()
)
lpE3TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestElapsedTime.setStatus("mandatory")


class _LpE3TestTimeRemaining_Type(Unsigned32):
    """Custom type lpE3TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpE3TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpE3TestTimeRemaining_Object = MibTableColumn
lpE3TestTimeRemaining = _LpE3TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 2),
    _LpE3TestTimeRemaining_Type()
)
lpE3TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestTimeRemaining.setStatus("mandatory")


class _LpE3TestCauseOfTermination_Type(Integer32):
    """Custom type lpE3TestCauseOfTermination based on Integer32"""
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


_LpE3TestCauseOfTermination_Type.__name__ = "Integer32"
_LpE3TestCauseOfTermination_Object = MibTableColumn
lpE3TestCauseOfTermination = _LpE3TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 3),
    _LpE3TestCauseOfTermination_Type()
)
lpE3TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestCauseOfTermination.setStatus("mandatory")
_LpE3TestBitsTx_Type = PassportCounter64
_LpE3TestBitsTx_Object = MibTableColumn
lpE3TestBitsTx = _LpE3TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 4),
    _LpE3TestBitsTx_Type()
)
lpE3TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestBitsTx.setStatus("mandatory")
_LpE3TestBytesTx_Type = PassportCounter64
_LpE3TestBytesTx_Object = MibTableColumn
lpE3TestBytesTx = _LpE3TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 5),
    _LpE3TestBytesTx_Type()
)
lpE3TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestBytesTx.setStatus("mandatory")
_LpE3TestFrmTx_Type = PassportCounter64
_LpE3TestFrmTx_Object = MibTableColumn
lpE3TestFrmTx = _LpE3TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 6),
    _LpE3TestFrmTx_Type()
)
lpE3TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestFrmTx.setStatus("mandatory")
_LpE3TestBitsRx_Type = PassportCounter64
_LpE3TestBitsRx_Object = MibTableColumn
lpE3TestBitsRx = _LpE3TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 7),
    _LpE3TestBitsRx_Type()
)
lpE3TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestBitsRx.setStatus("mandatory")
_LpE3TestBytesRx_Type = PassportCounter64
_LpE3TestBytesRx_Object = MibTableColumn
lpE3TestBytesRx = _LpE3TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 8),
    _LpE3TestBytesRx_Type()
)
lpE3TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestBytesRx.setStatus("mandatory")
_LpE3TestFrmRx_Type = PassportCounter64
_LpE3TestFrmRx_Object = MibTableColumn
lpE3TestFrmRx = _LpE3TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 9),
    _LpE3TestFrmRx_Type()
)
lpE3TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestFrmRx.setStatus("mandatory")
_LpE3TestErroredFrmRx_Type = PassportCounter64
_LpE3TestErroredFrmRx_Object = MibTableColumn
lpE3TestErroredFrmRx = _LpE3TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 10),
    _LpE3TestErroredFrmRx_Type()
)
lpE3TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestErroredFrmRx.setStatus("mandatory")


class _LpE3TestBitErrorRate_Type(AsciiString):
    """Custom type lpE3TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpE3TestBitErrorRate_Type.__name__ = "AsciiString"
_LpE3TestBitErrorRate_Object = MibTableColumn
lpE3TestBitErrorRate = _LpE3TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 2, 12, 1, 11),
    _LpE3TestBitErrorRate_Type()
)
lpE3TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TestBitErrorRate.setStatus("mandatory")
_LpE3G832_ObjectIdentity = ObjectIdentity
lpE3G832 = _LpE3G832_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3)
)
_LpE3G832RowStatusTable_Object = MibTable
lpE3G832RowStatusTable = _LpE3G832RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 1)
)
if mibBuilder.loadTexts:
    lpE3G832RowStatusTable.setStatus("mandatory")
_LpE3G832RowStatusEntry_Object = MibTableRow
lpE3G832RowStatusEntry = _LpE3G832RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 1, 1)
)
lpE3G832RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3G832Index"),
)
if mibBuilder.loadTexts:
    lpE3G832RowStatusEntry.setStatus("mandatory")
_LpE3G832RowStatus_Type = RowStatus
_LpE3G832RowStatus_Object = MibTableColumn
lpE3G832RowStatus = _LpE3G832RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 1, 1, 1),
    _LpE3G832RowStatus_Type()
)
lpE3G832RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3G832RowStatus.setStatus("mandatory")
_LpE3G832ComponentName_Type = DisplayString
_LpE3G832ComponentName_Object = MibTableColumn
lpE3G832ComponentName = _LpE3G832ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 1, 1, 2),
    _LpE3G832ComponentName_Type()
)
lpE3G832ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832ComponentName.setStatus("mandatory")
_LpE3G832StorageType_Type = StorageType
_LpE3G832StorageType_Object = MibTableColumn
lpE3G832StorageType = _LpE3G832StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 1, 1, 4),
    _LpE3G832StorageType_Type()
)
lpE3G832StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832StorageType.setStatus("mandatory")
_LpE3G832Index_Type = NonReplicated
_LpE3G832Index_Object = MibTableColumn
lpE3G832Index = _LpE3G832Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 1, 1, 10),
    _LpE3G832Index_Type()
)
lpE3G832Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE3G832Index.setStatus("mandatory")
_LpE3G832ProvisionedTable_Object = MibTable
lpE3G832ProvisionedTable = _LpE3G832ProvisionedTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 10)
)
if mibBuilder.loadTexts:
    lpE3G832ProvisionedTable.setStatus("mandatory")
_LpE3G832ProvisionedEntry_Object = MibTableRow
lpE3G832ProvisionedEntry = _LpE3G832ProvisionedEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 10, 1)
)
lpE3G832ProvisionedEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3G832Index"),
)
if mibBuilder.loadTexts:
    lpE3G832ProvisionedEntry.setStatus("mandatory")


class _LpE3G832TrailTraceTransmitted_Type(AsciiString):
    """Custom type lpE3G832TrailTraceTransmitted based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LpE3G832TrailTraceTransmitted_Type.__name__ = "AsciiString"
_LpE3G832TrailTraceTransmitted_Object = MibTableColumn
lpE3G832TrailTraceTransmitted = _LpE3G832TrailTraceTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 10, 1, 1),
    _LpE3G832TrailTraceTransmitted_Type()
)
lpE3G832TrailTraceTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3G832TrailTraceTransmitted.setStatus("mandatory")


class _LpE3G832TrailTraceExpected_Type(AsciiString):
    """Custom type lpE3G832TrailTraceExpected based on AsciiString"""
    defaultHexValue = ""

    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LpE3G832TrailTraceExpected_Type.__name__ = "AsciiString"
_LpE3G832TrailTraceExpected_Object = MibTableColumn
lpE3G832TrailTraceExpected = _LpE3G832TrailTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 10, 1, 2),
    _LpE3G832TrailTraceExpected_Type()
)
lpE3G832TrailTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3G832TrailTraceExpected.setStatus("mandatory")
_LpE3G832OperationalTable_Object = MibTable
lpE3G832OperationalTable = _LpE3G832OperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 11)
)
if mibBuilder.loadTexts:
    lpE3G832OperationalTable.setStatus("mandatory")
_LpE3G832OperationalEntry_Object = MibTableRow
lpE3G832OperationalEntry = _LpE3G832OperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 11, 1)
)
lpE3G832OperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3G832Index"),
)
if mibBuilder.loadTexts:
    lpE3G832OperationalEntry.setStatus("mandatory")


class _LpE3G832UnexpectedPayloadType_Type(Integer32):
    """Custom type lpE3G832UnexpectedPayloadType based on Integer32"""
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


_LpE3G832UnexpectedPayloadType_Type.__name__ = "Integer32"
_LpE3G832UnexpectedPayloadType_Object = MibTableColumn
lpE3G832UnexpectedPayloadType = _LpE3G832UnexpectedPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 11, 1, 1),
    _LpE3G832UnexpectedPayloadType_Type()
)
lpE3G832UnexpectedPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832UnexpectedPayloadType.setStatus("mandatory")


class _LpE3G832TrailTraceMismatch_Type(Integer32):
    """Custom type lpE3G832TrailTraceMismatch based on Integer32"""
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


_LpE3G832TrailTraceMismatch_Type.__name__ = "Integer32"
_LpE3G832TrailTraceMismatch_Object = MibTableColumn
lpE3G832TrailTraceMismatch = _LpE3G832TrailTraceMismatch_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 11, 1, 2),
    _LpE3G832TrailTraceMismatch_Type()
)
lpE3G832TrailTraceMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832TrailTraceMismatch.setStatus("mandatory")


class _LpE3G832TimingMarker_Type(Integer32):
    """Custom type lpE3G832TimingMarker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notTraceable", 0),
          ("traceable", 1))
    )


_LpE3G832TimingMarker_Type.__name__ = "Integer32"
_LpE3G832TimingMarker_Object = MibTableColumn
lpE3G832TimingMarker = _LpE3G832TimingMarker_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 11, 1, 3),
    _LpE3G832TimingMarker_Type()
)
lpE3G832TimingMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832TimingMarker.setStatus("mandatory")


class _LpE3G832TrailTraceReceived_Type(AsciiString):
    """Custom type lpE3G832TrailTraceReceived based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_LpE3G832TrailTraceReceived_Type.__name__ = "AsciiString"
_LpE3G832TrailTraceReceived_Object = MibTableColumn
lpE3G832TrailTraceReceived = _LpE3G832TrailTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 11, 1, 4),
    _LpE3G832TrailTraceReceived_Type()
)
lpE3G832TrailTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832TrailTraceReceived.setStatus("mandatory")
_LpE3G832StatsTable_Object = MibTable
lpE3G832StatsTable = _LpE3G832StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12)
)
if mibBuilder.loadTexts:
    lpE3G832StatsTable.setStatus("mandatory")
_LpE3G832StatsEntry_Object = MibTableRow
lpE3G832StatsEntry = _LpE3G832StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12, 1)
)
lpE3G832StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3G832Index"),
)
if mibBuilder.loadTexts:
    lpE3G832StatsEntry.setStatus("mandatory")
_LpE3G832FarEndErrorFreeSec_Type = Counter32
_LpE3G832FarEndErrorFreeSec_Object = MibTableColumn
lpE3G832FarEndErrorFreeSec = _LpE3G832FarEndErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12, 1, 1),
    _LpE3G832FarEndErrorFreeSec_Type()
)
lpE3G832FarEndErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832FarEndErrorFreeSec.setStatus("mandatory")
_LpE3G832FarEndCodeViolations_Type = Counter32
_LpE3G832FarEndCodeViolations_Object = MibTableColumn
lpE3G832FarEndCodeViolations = _LpE3G832FarEndCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12, 1, 2),
    _LpE3G832FarEndCodeViolations_Type()
)
lpE3G832FarEndCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832FarEndCodeViolations.setStatus("mandatory")
_LpE3G832FarEndErroredSec_Type = Counter32
_LpE3G832FarEndErroredSec_Object = MibTableColumn
lpE3G832FarEndErroredSec = _LpE3G832FarEndErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12, 1, 3),
    _LpE3G832FarEndErroredSec_Type()
)
lpE3G832FarEndErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832FarEndErroredSec.setStatus("mandatory")
_LpE3G832FarEndSevErroredSec_Type = Counter32
_LpE3G832FarEndSevErroredSec_Object = MibTableColumn
lpE3G832FarEndSevErroredSec = _LpE3G832FarEndSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12, 1, 4),
    _LpE3G832FarEndSevErroredSec_Type()
)
lpE3G832FarEndSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832FarEndSevErroredSec.setStatus("mandatory")
_LpE3G832FarEndSefAisSec_Type = Counter32
_LpE3G832FarEndSefAisSec_Object = MibTableColumn
lpE3G832FarEndSefAisSec = _LpE3G832FarEndSefAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12, 1, 5),
    _LpE3G832FarEndSefAisSec_Type()
)
lpE3G832FarEndSefAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832FarEndSefAisSec.setStatus("mandatory")
_LpE3G832FarEndUnavailSec_Type = Counter32
_LpE3G832FarEndUnavailSec_Object = MibTableColumn
lpE3G832FarEndUnavailSec = _LpE3G832FarEndUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 3, 12, 1, 6),
    _LpE3G832FarEndUnavailSec_Type()
)
lpE3G832FarEndUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3G832FarEndUnavailSec.setStatus("mandatory")
_LpE3Plcp_ObjectIdentity = ObjectIdentity
lpE3Plcp = _LpE3Plcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4)
)
_LpE3PlcpRowStatusTable_Object = MibTable
lpE3PlcpRowStatusTable = _LpE3PlcpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 1)
)
if mibBuilder.loadTexts:
    lpE3PlcpRowStatusTable.setStatus("mandatory")
_LpE3PlcpRowStatusEntry_Object = MibTableRow
lpE3PlcpRowStatusEntry = _LpE3PlcpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 1, 1)
)
lpE3PlcpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3PlcpIndex"),
)
if mibBuilder.loadTexts:
    lpE3PlcpRowStatusEntry.setStatus("mandatory")
_LpE3PlcpRowStatus_Type = RowStatus
_LpE3PlcpRowStatus_Object = MibTableColumn
lpE3PlcpRowStatus = _LpE3PlcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 1, 1, 1),
    _LpE3PlcpRowStatus_Type()
)
lpE3PlcpRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpRowStatus.setStatus("mandatory")
_LpE3PlcpComponentName_Type = DisplayString
_LpE3PlcpComponentName_Object = MibTableColumn
lpE3PlcpComponentName = _LpE3PlcpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 1, 1, 2),
    _LpE3PlcpComponentName_Type()
)
lpE3PlcpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpComponentName.setStatus("mandatory")
_LpE3PlcpStorageType_Type = StorageType
_LpE3PlcpStorageType_Object = MibTableColumn
lpE3PlcpStorageType = _LpE3PlcpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 1, 1, 4),
    _LpE3PlcpStorageType_Type()
)
lpE3PlcpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpStorageType.setStatus("mandatory")
_LpE3PlcpIndex_Type = NonReplicated
_LpE3PlcpIndex_Object = MibTableColumn
lpE3PlcpIndex = _LpE3PlcpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 1, 1, 10),
    _LpE3PlcpIndex_Type()
)
lpE3PlcpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE3PlcpIndex.setStatus("mandatory")
_LpE3PlcpOperationalTable_Object = MibTable
lpE3PlcpOperationalTable = _LpE3PlcpOperationalTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 10)
)
if mibBuilder.loadTexts:
    lpE3PlcpOperationalTable.setStatus("mandatory")
_LpE3PlcpOperationalEntry_Object = MibTableRow
lpE3PlcpOperationalEntry = _LpE3PlcpOperationalEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 10, 1)
)
lpE3PlcpOperationalEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3PlcpIndex"),
)
if mibBuilder.loadTexts:
    lpE3PlcpOperationalEntry.setStatus("mandatory")


class _LpE3PlcpLofAlarm_Type(Integer32):
    """Custom type lpE3PlcpLofAlarm based on Integer32"""
    defaultValue = 1

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


_LpE3PlcpLofAlarm_Type.__name__ = "Integer32"
_LpE3PlcpLofAlarm_Object = MibTableColumn
lpE3PlcpLofAlarm = _LpE3PlcpLofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 10, 1, 1),
    _LpE3PlcpLofAlarm_Type()
)
lpE3PlcpLofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpLofAlarm.setStatus("mandatory")


class _LpE3PlcpRxRaiAlarm_Type(Integer32):
    """Custom type lpE3PlcpRxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpE3PlcpRxRaiAlarm_Type.__name__ = "Integer32"
_LpE3PlcpRxRaiAlarm_Object = MibTableColumn
lpE3PlcpRxRaiAlarm = _LpE3PlcpRxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 10, 1, 2),
    _LpE3PlcpRxRaiAlarm_Type()
)
lpE3PlcpRxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpRxRaiAlarm.setStatus("mandatory")
_LpE3PlcpStatsTable_Object = MibTable
lpE3PlcpStatsTable = _LpE3PlcpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11)
)
if mibBuilder.loadTexts:
    lpE3PlcpStatsTable.setStatus("mandatory")
_LpE3PlcpStatsEntry_Object = MibTableRow
lpE3PlcpStatsEntry = _LpE3PlcpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1)
)
lpE3PlcpStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3PlcpIndex"),
)
if mibBuilder.loadTexts:
    lpE3PlcpStatsEntry.setStatus("mandatory")
_LpE3PlcpErrorFreeSec_Type = Counter32
_LpE3PlcpErrorFreeSec_Object = MibTableColumn
lpE3PlcpErrorFreeSec = _LpE3PlcpErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 1),
    _LpE3PlcpErrorFreeSec_Type()
)
lpE3PlcpErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpErrorFreeSec.setStatus("mandatory")
_LpE3PlcpCodingViolations_Type = Counter32
_LpE3PlcpCodingViolations_Object = MibTableColumn
lpE3PlcpCodingViolations = _LpE3PlcpCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 2),
    _LpE3PlcpCodingViolations_Type()
)
lpE3PlcpCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpCodingViolations.setStatus("mandatory")
_LpE3PlcpErroredSec_Type = Counter32
_LpE3PlcpErroredSec_Object = MibTableColumn
lpE3PlcpErroredSec = _LpE3PlcpErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 3),
    _LpE3PlcpErroredSec_Type()
)
lpE3PlcpErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpErroredSec.setStatus("mandatory")
_LpE3PlcpSevErroredSec_Type = Counter32
_LpE3PlcpSevErroredSec_Object = MibTableColumn
lpE3PlcpSevErroredSec = _LpE3PlcpSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 4),
    _LpE3PlcpSevErroredSec_Type()
)
lpE3PlcpSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpSevErroredSec.setStatus("mandatory")
_LpE3PlcpSevErroredFramingSec_Type = Counter32
_LpE3PlcpSevErroredFramingSec_Object = MibTableColumn
lpE3PlcpSevErroredFramingSec = _LpE3PlcpSevErroredFramingSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 5),
    _LpE3PlcpSevErroredFramingSec_Type()
)
lpE3PlcpSevErroredFramingSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpSevErroredFramingSec.setStatus("mandatory")
_LpE3PlcpUnavailSec_Type = Counter32
_LpE3PlcpUnavailSec_Object = MibTableColumn
lpE3PlcpUnavailSec = _LpE3PlcpUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 6),
    _LpE3PlcpUnavailSec_Type()
)
lpE3PlcpUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpUnavailSec.setStatus("mandatory")
_LpE3PlcpFarEndErrorFreeSec_Type = Counter32
_LpE3PlcpFarEndErrorFreeSec_Object = MibTableColumn
lpE3PlcpFarEndErrorFreeSec = _LpE3PlcpFarEndErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 7),
    _LpE3PlcpFarEndErrorFreeSec_Type()
)
lpE3PlcpFarEndErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpFarEndErrorFreeSec.setStatus("mandatory")
_LpE3PlcpFarEndCodingViolations_Type = Counter32
_LpE3PlcpFarEndCodingViolations_Object = MibTableColumn
lpE3PlcpFarEndCodingViolations = _LpE3PlcpFarEndCodingViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 8),
    _LpE3PlcpFarEndCodingViolations_Type()
)
lpE3PlcpFarEndCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpFarEndCodingViolations.setStatus("mandatory")
_LpE3PlcpFarEndErroredSec_Type = Counter32
_LpE3PlcpFarEndErroredSec_Object = MibTableColumn
lpE3PlcpFarEndErroredSec = _LpE3PlcpFarEndErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 9),
    _LpE3PlcpFarEndErroredSec_Type()
)
lpE3PlcpFarEndErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpFarEndErroredSec.setStatus("mandatory")
_LpE3PlcpFarEndSevErroredSec_Type = Counter32
_LpE3PlcpFarEndSevErroredSec_Object = MibTableColumn
lpE3PlcpFarEndSevErroredSec = _LpE3PlcpFarEndSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 10),
    _LpE3PlcpFarEndSevErroredSec_Type()
)
lpE3PlcpFarEndSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpFarEndSevErroredSec.setStatus("mandatory")
_LpE3PlcpFarEndUnavailableSec_Type = Counter32
_LpE3PlcpFarEndUnavailableSec_Object = MibTableColumn
lpE3PlcpFarEndUnavailableSec = _LpE3PlcpFarEndUnavailableSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 4, 11, 1, 11),
    _LpE3PlcpFarEndUnavailableSec_Type()
)
lpE3PlcpFarEndUnavailableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PlcpFarEndUnavailableSec.setStatus("mandatory")
_LpE3Cell_ObjectIdentity = ObjectIdentity
lpE3Cell = _LpE3Cell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5)
)
_LpE3CellRowStatusTable_Object = MibTable
lpE3CellRowStatusTable = _LpE3CellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 1)
)
if mibBuilder.loadTexts:
    lpE3CellRowStatusTable.setStatus("mandatory")
_LpE3CellRowStatusEntry_Object = MibTableRow
lpE3CellRowStatusEntry = _LpE3CellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 1, 1)
)
lpE3CellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3CellIndex"),
)
if mibBuilder.loadTexts:
    lpE3CellRowStatusEntry.setStatus("mandatory")
_LpE3CellRowStatus_Type = RowStatus
_LpE3CellRowStatus_Object = MibTableColumn
lpE3CellRowStatus = _LpE3CellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 1, 1, 1),
    _LpE3CellRowStatus_Type()
)
lpE3CellRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3CellRowStatus.setStatus("mandatory")
_LpE3CellComponentName_Type = DisplayString
_LpE3CellComponentName_Object = MibTableColumn
lpE3CellComponentName = _LpE3CellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 1, 1, 2),
    _LpE3CellComponentName_Type()
)
lpE3CellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellComponentName.setStatus("mandatory")
_LpE3CellStorageType_Type = StorageType
_LpE3CellStorageType_Object = MibTableColumn
lpE3CellStorageType = _LpE3CellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 1, 1, 4),
    _LpE3CellStorageType_Type()
)
lpE3CellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellStorageType.setStatus("mandatory")
_LpE3CellIndex_Type = NonReplicated
_LpE3CellIndex_Object = MibTableColumn
lpE3CellIndex = _LpE3CellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 1, 1, 10),
    _LpE3CellIndex_Type()
)
lpE3CellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE3CellIndex.setStatus("mandatory")
_LpE3CellProvTable_Object = MibTable
lpE3CellProvTable = _LpE3CellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 10)
)
if mibBuilder.loadTexts:
    lpE3CellProvTable.setStatus("mandatory")
_LpE3CellProvEntry_Object = MibTableRow
lpE3CellProvEntry = _LpE3CellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 10, 1)
)
lpE3CellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3CellIndex"),
)
if mibBuilder.loadTexts:
    lpE3CellProvEntry.setStatus("mandatory")


class _LpE3CellAlarmActDelay_Type(Unsigned32):
    """Custom type lpE3CellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpE3CellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpE3CellAlarmActDelay_Object = MibTableColumn
lpE3CellAlarmActDelay = _LpE3CellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 10, 1, 1),
    _LpE3CellAlarmActDelay_Type()
)
lpE3CellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3CellAlarmActDelay.setStatus("mandatory")


class _LpE3CellScrambleCellPayload_Type(Integer32):
    """Custom type lpE3CellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpE3CellScrambleCellPayload_Type.__name__ = "Integer32"
_LpE3CellScrambleCellPayload_Object = MibTableColumn
lpE3CellScrambleCellPayload = _LpE3CellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 10, 1, 2),
    _LpE3CellScrambleCellPayload_Type()
)
lpE3CellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3CellScrambleCellPayload.setStatus("mandatory")


class _LpE3CellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpE3CellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpE3CellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpE3CellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpE3CellCorrectSingleBitHeaderErrors = _LpE3CellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 10, 1, 3),
    _LpE3CellCorrectSingleBitHeaderErrors_Type()
)
lpE3CellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3CellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpE3CellOperTable_Object = MibTable
lpE3CellOperTable = _LpE3CellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 11)
)
if mibBuilder.loadTexts:
    lpE3CellOperTable.setStatus("mandatory")
_LpE3CellOperEntry_Object = MibTableRow
lpE3CellOperEntry = _LpE3CellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 11, 1)
)
lpE3CellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3CellIndex"),
)
if mibBuilder.loadTexts:
    lpE3CellOperEntry.setStatus("mandatory")


class _LpE3CellLcdAlarm_Type(Integer32):
    """Custom type lpE3CellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpE3CellLcdAlarm_Type.__name__ = "Integer32"
_LpE3CellLcdAlarm_Object = MibTableColumn
lpE3CellLcdAlarm = _LpE3CellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 11, 1, 1),
    _LpE3CellLcdAlarm_Type()
)
lpE3CellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellLcdAlarm.setStatus("mandatory")
_LpE3CellStatsTable_Object = MibTable
lpE3CellStatsTable = _LpE3CellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 12)
)
if mibBuilder.loadTexts:
    lpE3CellStatsTable.setStatus("mandatory")
_LpE3CellStatsEntry_Object = MibTableRow
lpE3CellStatsEntry = _LpE3CellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 12, 1)
)
lpE3CellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3CellIndex"),
)
if mibBuilder.loadTexts:
    lpE3CellStatsEntry.setStatus("mandatory")
_LpE3CellUncorrectableHecErrors_Type = Counter32
_LpE3CellUncorrectableHecErrors_Object = MibTableColumn
lpE3CellUncorrectableHecErrors = _LpE3CellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 12, 1, 1),
    _LpE3CellUncorrectableHecErrors_Type()
)
lpE3CellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellUncorrectableHecErrors.setStatus("mandatory")
_LpE3CellSevErroredSec_Type = Counter32
_LpE3CellSevErroredSec_Object = MibTableColumn
lpE3CellSevErroredSec = _LpE3CellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 12, 1, 2),
    _LpE3CellSevErroredSec_Type()
)
lpE3CellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellSevErroredSec.setStatus("mandatory")


class _LpE3CellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpE3CellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpE3CellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpE3CellReceiveCellUtilization_Object = MibTableColumn
lpE3CellReceiveCellUtilization = _LpE3CellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 12, 1, 3),
    _LpE3CellReceiveCellUtilization_Type()
)
lpE3CellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellReceiveCellUtilization.setStatus("mandatory")


class _LpE3CellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpE3CellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpE3CellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpE3CellTransmitCellUtilization_Object = MibTableColumn
lpE3CellTransmitCellUtilization = _LpE3CellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 12, 1, 4),
    _LpE3CellTransmitCellUtilization_Type()
)
lpE3CellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellTransmitCellUtilization.setStatus("mandatory")
_LpE3CellCorrectableHeaderErrors_Type = Counter32
_LpE3CellCorrectableHeaderErrors_Object = MibTableColumn
lpE3CellCorrectableHeaderErrors = _LpE3CellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 5, 12, 1, 5),
    _LpE3CellCorrectableHeaderErrors_Type()
)
lpE3CellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3CellCorrectableHeaderErrors.setStatus("mandatory")
_LpE3ProvTable_Object = MibTable
lpE3ProvTable = _LpE3ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10)
)
if mibBuilder.loadTexts:
    lpE3ProvTable.setStatus("mandatory")
_LpE3ProvEntry_Object = MibTableRow
lpE3ProvEntry = _LpE3ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1)
)
lpE3ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3ProvEntry.setStatus("mandatory")


class _LpE3LineLength_Type(Unsigned32):
    """Custom type lpE3LineLength based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_LpE3LineLength_Type.__name__ = "Unsigned32"
_LpE3LineLength_Object = MibTableColumn
lpE3LineLength = _LpE3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1, 1),
    _LpE3LineLength_Type()
)
lpE3LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3LineLength.setStatus("mandatory")


class _LpE3ClockingSource_Type(Integer32):
    """Custom type lpE3ClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("local", 0),
          ("module", 2),
          ("otherPort", 4))
    )


_LpE3ClockingSource_Type.__name__ = "Integer32"
_LpE3ClockingSource_Object = MibTableColumn
lpE3ClockingSource = _LpE3ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1, 2),
    _LpE3ClockingSource_Type()
)
lpE3ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3ClockingSource.setStatus("mandatory")
_LpE3ApplicationFramerName_Type = Link
_LpE3ApplicationFramerName_Object = MibTableColumn
lpE3ApplicationFramerName = _LpE3ApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1, 3),
    _LpE3ApplicationFramerName_Type()
)
lpE3ApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3ApplicationFramerName.setStatus("mandatory")


class _LpE3Mapping_Type(Integer32):
    """Custom type lpE3Mapping based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("direct", 0),
          ("plcp", 1))
    )


_LpE3Mapping_Type.__name__ = "Integer32"
_LpE3Mapping_Object = MibTableColumn
lpE3Mapping = _LpE3Mapping_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1, 4),
    _LpE3Mapping_Type()
)
lpE3Mapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3Mapping.setStatus("mandatory")


class _LpE3Framing_Type(Integer32):
    """Custom type lpE3Framing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("g751", 0),
          ("g832", 1))
    )


_LpE3Framing_Type.__name__ = "Integer32"
_LpE3Framing_Object = MibTableColumn
lpE3Framing = _LpE3Framing_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1, 5),
    _LpE3Framing_Type()
)
lpE3Framing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3Framing.setStatus("mandatory")


class _LpE3LinkAlarmActivationThreshold_Type(Unsigned32):
    """Custom type lpE3LinkAlarmActivationThreshold based on Unsigned32"""
    defaultValue = 2200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2600),
    )


_LpE3LinkAlarmActivationThreshold_Type.__name__ = "Unsigned32"
_LpE3LinkAlarmActivationThreshold_Object = MibTableColumn
lpE3LinkAlarmActivationThreshold = _LpE3LinkAlarmActivationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1, 6),
    _LpE3LinkAlarmActivationThreshold_Type()
)
lpE3LinkAlarmActivationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3LinkAlarmActivationThreshold.setStatus("mandatory")


class _LpE3LinkAlarmScanInterval_Type(Unsigned32):
    """Custom type lpE3LinkAlarmScanInterval based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 250),
    )


_LpE3LinkAlarmScanInterval_Type.__name__ = "Unsigned32"
_LpE3LinkAlarmScanInterval_Object = MibTableColumn
lpE3LinkAlarmScanInterval = _LpE3LinkAlarmScanInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 10, 1, 7),
    _LpE3LinkAlarmScanInterval_Type()
)
lpE3LinkAlarmScanInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3LinkAlarmScanInterval.setStatus("mandatory")
_LpE3CidDataTable_Object = MibTable
lpE3CidDataTable = _LpE3CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 11)
)
if mibBuilder.loadTexts:
    lpE3CidDataTable.setStatus("mandatory")
_LpE3CidDataEntry_Object = MibTableRow
lpE3CidDataEntry = _LpE3CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 11, 1)
)
lpE3CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3CidDataEntry.setStatus("mandatory")


class _LpE3CustomerIdentifier_Type(Unsigned32):
    """Custom type lpE3CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpE3CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpE3CustomerIdentifier_Object = MibTableColumn
lpE3CustomerIdentifier = _LpE3CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 11, 1, 1),
    _LpE3CustomerIdentifier_Type()
)
lpE3CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3CustomerIdentifier.setStatus("mandatory")
_LpE3AdminInfoTable_Object = MibTable
lpE3AdminInfoTable = _LpE3AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 12)
)
if mibBuilder.loadTexts:
    lpE3AdminInfoTable.setStatus("mandatory")
_LpE3AdminInfoEntry_Object = MibTableRow
lpE3AdminInfoEntry = _LpE3AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 12, 1)
)
lpE3AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3AdminInfoEntry.setStatus("mandatory")


class _LpE3Vendor_Type(AsciiString):
    """Custom type lpE3Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpE3Vendor_Type.__name__ = "AsciiString"
_LpE3Vendor_Object = MibTableColumn
lpE3Vendor = _LpE3Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 12, 1, 1),
    _LpE3Vendor_Type()
)
lpE3Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3Vendor.setStatus("mandatory")


class _LpE3CommentText_Type(AsciiString):
    """Custom type lpE3CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpE3CommentText_Type.__name__ = "AsciiString"
_LpE3CommentText_Object = MibTableColumn
lpE3CommentText = _LpE3CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 12, 1, 2),
    _LpE3CommentText_Type()
)
lpE3CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3CommentText.setStatus("mandatory")
_LpE3IfEntryTable_Object = MibTable
lpE3IfEntryTable = _LpE3IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 13)
)
if mibBuilder.loadTexts:
    lpE3IfEntryTable.setStatus("mandatory")
_LpE3IfEntryEntry_Object = MibTableRow
lpE3IfEntryEntry = _LpE3IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 13, 1)
)
lpE3IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3IfEntryEntry.setStatus("mandatory")


class _LpE3IfAdminStatus_Type(Integer32):
    """Custom type lpE3IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpE3IfAdminStatus_Type.__name__ = "Integer32"
_LpE3IfAdminStatus_Object = MibTableColumn
lpE3IfAdminStatus = _LpE3IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 13, 1, 1),
    _LpE3IfAdminStatus_Type()
)
lpE3IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE3IfAdminStatus.setStatus("mandatory")


class _LpE3IfIndex_Type(InterfaceIndex):
    """Custom type lpE3IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpE3IfIndex_Type.__name__ = "InterfaceIndex"
_LpE3IfIndex_Object = MibTableColumn
lpE3IfIndex = _LpE3IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 13, 1, 2),
    _LpE3IfIndex_Type()
)
lpE3IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3IfIndex.setStatus("mandatory")
_LpE3OperStatusTable_Object = MibTable
lpE3OperStatusTable = _LpE3OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 14)
)
if mibBuilder.loadTexts:
    lpE3OperStatusTable.setStatus("mandatory")
_LpE3OperStatusEntry_Object = MibTableRow
lpE3OperStatusEntry = _LpE3OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 14, 1)
)
lpE3OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3OperStatusEntry.setStatus("mandatory")


class _LpE3SnmpOperStatus_Type(Integer32):
    """Custom type lpE3SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpE3SnmpOperStatus_Type.__name__ = "Integer32"
_LpE3SnmpOperStatus_Object = MibTableColumn
lpE3SnmpOperStatus = _LpE3SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 14, 1, 1),
    _LpE3SnmpOperStatus_Type()
)
lpE3SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3SnmpOperStatus.setStatus("mandatory")
_LpE3StateTable_Object = MibTable
lpE3StateTable = _LpE3StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15)
)
if mibBuilder.loadTexts:
    lpE3StateTable.setStatus("mandatory")
_LpE3StateEntry_Object = MibTableRow
lpE3StateEntry = _LpE3StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1)
)
lpE3StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3StateEntry.setStatus("mandatory")


class _LpE3AdminState_Type(Integer32):
    """Custom type lpE3AdminState based on Integer32"""
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


_LpE3AdminState_Type.__name__ = "Integer32"
_LpE3AdminState_Object = MibTableColumn
lpE3AdminState = _LpE3AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 1),
    _LpE3AdminState_Type()
)
lpE3AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3AdminState.setStatus("mandatory")


class _LpE3OperationalState_Type(Integer32):
    """Custom type lpE3OperationalState based on Integer32"""
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


_LpE3OperationalState_Type.__name__ = "Integer32"
_LpE3OperationalState_Object = MibTableColumn
lpE3OperationalState = _LpE3OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 2),
    _LpE3OperationalState_Type()
)
lpE3OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3OperationalState.setStatus("mandatory")


class _LpE3UsageState_Type(Integer32):
    """Custom type lpE3UsageState based on Integer32"""
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


_LpE3UsageState_Type.__name__ = "Integer32"
_LpE3UsageState_Object = MibTableColumn
lpE3UsageState = _LpE3UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 3),
    _LpE3UsageState_Type()
)
lpE3UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3UsageState.setStatus("mandatory")


class _LpE3AvailabilityStatus_Type(OctetString):
    """Custom type lpE3AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpE3AvailabilityStatus_Type.__name__ = "OctetString"
_LpE3AvailabilityStatus_Object = MibTableColumn
lpE3AvailabilityStatus = _LpE3AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 4),
    _LpE3AvailabilityStatus_Type()
)
lpE3AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3AvailabilityStatus.setStatus("mandatory")


class _LpE3ProceduralStatus_Type(OctetString):
    """Custom type lpE3ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE3ProceduralStatus_Type.__name__ = "OctetString"
_LpE3ProceduralStatus_Object = MibTableColumn
lpE3ProceduralStatus = _LpE3ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 5),
    _LpE3ProceduralStatus_Type()
)
lpE3ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3ProceduralStatus.setStatus("mandatory")


class _LpE3ControlStatus_Type(OctetString):
    """Custom type lpE3ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE3ControlStatus_Type.__name__ = "OctetString"
_LpE3ControlStatus_Object = MibTableColumn
lpE3ControlStatus = _LpE3ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 6),
    _LpE3ControlStatus_Type()
)
lpE3ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3ControlStatus.setStatus("mandatory")


class _LpE3AlarmStatus_Type(OctetString):
    """Custom type lpE3AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE3AlarmStatus_Type.__name__ = "OctetString"
_LpE3AlarmStatus_Object = MibTableColumn
lpE3AlarmStatus = _LpE3AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 7),
    _LpE3AlarmStatus_Type()
)
lpE3AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3AlarmStatus.setStatus("mandatory")


class _LpE3StandbyStatus_Type(Integer32):
    """Custom type lpE3StandbyStatus based on Integer32"""
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


_LpE3StandbyStatus_Type.__name__ = "Integer32"
_LpE3StandbyStatus_Object = MibTableColumn
lpE3StandbyStatus = _LpE3StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 8),
    _LpE3StandbyStatus_Type()
)
lpE3StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3StandbyStatus.setStatus("mandatory")


class _LpE3UnknownStatus_Type(Integer32):
    """Custom type lpE3UnknownStatus based on Integer32"""
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


_LpE3UnknownStatus_Type.__name__ = "Integer32"
_LpE3UnknownStatus_Object = MibTableColumn
lpE3UnknownStatus = _LpE3UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 15, 1, 9),
    _LpE3UnknownStatus_Type()
)
lpE3UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3UnknownStatus.setStatus("mandatory")
_LpE3OperTable_Object = MibTable
lpE3OperTable = _LpE3OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16)
)
if mibBuilder.loadTexts:
    lpE3OperTable.setStatus("mandatory")
_LpE3OperEntry_Object = MibTableRow
lpE3OperEntry = _LpE3OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16, 1)
)
lpE3OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3OperEntry.setStatus("mandatory")


class _LpE3LosAlarm_Type(Integer32):
    """Custom type lpE3LosAlarm based on Integer32"""
    defaultValue = 1

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


_LpE3LosAlarm_Type.__name__ = "Integer32"
_LpE3LosAlarm_Object = MibTableColumn
lpE3LosAlarm = _LpE3LosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16, 1, 1),
    _LpE3LosAlarm_Type()
)
lpE3LosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3LosAlarm.setStatus("mandatory")


class _LpE3LofAlarm_Type(Integer32):
    """Custom type lpE3LofAlarm based on Integer32"""
    defaultValue = 1

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


_LpE3LofAlarm_Type.__name__ = "Integer32"
_LpE3LofAlarm_Object = MibTableColumn
lpE3LofAlarm = _LpE3LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16, 1, 2),
    _LpE3LofAlarm_Type()
)
lpE3LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3LofAlarm.setStatus("mandatory")


class _LpE3RxAisAlarm_Type(Integer32):
    """Custom type lpE3RxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpE3RxAisAlarm_Type.__name__ = "Integer32"
_LpE3RxAisAlarm_Object = MibTableColumn
lpE3RxAisAlarm = _LpE3RxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16, 1, 3),
    _LpE3RxAisAlarm_Type()
)
lpE3RxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3RxAisAlarm.setStatus("mandatory")


class _LpE3RxRaiAlarm_Type(Integer32):
    """Custom type lpE3RxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpE3RxRaiAlarm_Type.__name__ = "Integer32"
_LpE3RxRaiAlarm_Object = MibTableColumn
lpE3RxRaiAlarm = _LpE3RxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16, 1, 4),
    _LpE3RxRaiAlarm_Type()
)
lpE3RxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3RxRaiAlarm.setStatus("mandatory")


class _LpE3TxAis_Type(Integer32):
    """Custom type lpE3TxAis based on Integer32"""
    defaultValue = 1

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


_LpE3TxAis_Type.__name__ = "Integer32"
_LpE3TxAis_Object = MibTableColumn
lpE3TxAis = _LpE3TxAis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16, 1, 5),
    _LpE3TxAis_Type()
)
lpE3TxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TxAis.setStatus("mandatory")


class _LpE3TxRai_Type(Integer32):
    """Custom type lpE3TxRai based on Integer32"""
    defaultValue = 1

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


_LpE3TxRai_Type.__name__ = "Integer32"
_LpE3TxRai_Object = MibTableColumn
lpE3TxRai = _LpE3TxRai_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 16, 1, 6),
    _LpE3TxRai_Type()
)
lpE3TxRai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3TxRai.setStatus("mandatory")
_LpE3StatsTable_Object = MibTable
lpE3StatsTable = _LpE3StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17)
)
if mibBuilder.loadTexts:
    lpE3StatsTable.setStatus("mandatory")
_LpE3StatsEntry_Object = MibTableRow
lpE3StatsEntry = _LpE3StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1)
)
lpE3StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE3Index"),
)
if mibBuilder.loadTexts:
    lpE3StatsEntry.setStatus("mandatory")
_LpE3RunningTime_Type = Counter32
_LpE3RunningTime_Object = MibTableColumn
lpE3RunningTime = _LpE3RunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 1),
    _LpE3RunningTime_Type()
)
lpE3RunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3RunningTime.setStatus("mandatory")
_LpE3ErrorFreeSec_Type = Counter32
_LpE3ErrorFreeSec_Object = MibTableColumn
lpE3ErrorFreeSec = _LpE3ErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 2),
    _LpE3ErrorFreeSec_Type()
)
lpE3ErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3ErrorFreeSec.setStatus("mandatory")
_LpE3LineCodeViolations_Type = Counter32
_LpE3LineCodeViolations_Object = MibTableColumn
lpE3LineCodeViolations = _LpE3LineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 3),
    _LpE3LineCodeViolations_Type()
)
lpE3LineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3LineCodeViolations.setStatus("mandatory")
_LpE3LineErroredSec_Type = Counter32
_LpE3LineErroredSec_Object = MibTableColumn
lpE3LineErroredSec = _LpE3LineErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 4),
    _LpE3LineErroredSec_Type()
)
lpE3LineErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3LineErroredSec.setStatus("mandatory")
_LpE3LineSevErroredSec_Type = Counter32
_LpE3LineSevErroredSec_Object = MibTableColumn
lpE3LineSevErroredSec = _LpE3LineSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 5),
    _LpE3LineSevErroredSec_Type()
)
lpE3LineSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3LineSevErroredSec.setStatus("mandatory")
_LpE3LineLosSec_Type = Counter32
_LpE3LineLosSec_Object = MibTableColumn
lpE3LineLosSec = _LpE3LineLosSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 6),
    _LpE3LineLosSec_Type()
)
lpE3LineLosSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3LineLosSec.setStatus("mandatory")
_LpE3LineFailures_Type = Counter32
_LpE3LineFailures_Object = MibTableColumn
lpE3LineFailures = _LpE3LineFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 7),
    _LpE3LineFailures_Type()
)
lpE3LineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3LineFailures.setStatus("mandatory")
_LpE3PathCodeViolations_Type = Counter32
_LpE3PathCodeViolations_Object = MibTableColumn
lpE3PathCodeViolations = _LpE3PathCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 8),
    _LpE3PathCodeViolations_Type()
)
lpE3PathCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PathCodeViolations.setStatus("mandatory")
_LpE3PathErroredSec_Type = Counter32
_LpE3PathErroredSec_Object = MibTableColumn
lpE3PathErroredSec = _LpE3PathErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 9),
    _LpE3PathErroredSec_Type()
)
lpE3PathErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PathErroredSec.setStatus("mandatory")
_LpE3PathSevErroredSec_Type = Counter32
_LpE3PathSevErroredSec_Object = MibTableColumn
lpE3PathSevErroredSec = _LpE3PathSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 10),
    _LpE3PathSevErroredSec_Type()
)
lpE3PathSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PathSevErroredSec.setStatus("mandatory")
_LpE3PathSefAisSec_Type = Counter32
_LpE3PathSefAisSec_Object = MibTableColumn
lpE3PathSefAisSec = _LpE3PathSefAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 11),
    _LpE3PathSefAisSec_Type()
)
lpE3PathSefAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PathSefAisSec.setStatus("mandatory")
_LpE3PathUnavailSec_Type = Counter32
_LpE3PathUnavailSec_Object = MibTableColumn
lpE3PathUnavailSec = _LpE3PathUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 12),
    _LpE3PathUnavailSec_Type()
)
lpE3PathUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PathUnavailSec.setStatus("mandatory")
_LpE3PathFailures_Type = Counter32
_LpE3PathFailures_Object = MibTableColumn
lpE3PathFailures = _LpE3PathFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 6, 17, 1, 13),
    _LpE3PathFailures_Type()
)
lpE3PathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE3PathFailures.setStatus("mandatory")
_LpDS1_ObjectIdentity = ObjectIdentity
lpDS1 = _LpDS1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7)
)
_LpDS1RowStatusTable_Object = MibTable
lpDS1RowStatusTable = _LpDS1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 1)
)
if mibBuilder.loadTexts:
    lpDS1RowStatusTable.setStatus("mandatory")
_LpDS1RowStatusEntry_Object = MibTableRow
lpDS1RowStatusEntry = _LpDS1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 1, 1)
)
lpDS1RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1RowStatusEntry.setStatus("mandatory")
_LpDS1RowStatus_Type = RowStatus
_LpDS1RowStatus_Object = MibTableColumn
lpDS1RowStatus = _LpDS1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 1, 1, 1),
    _LpDS1RowStatus_Type()
)
lpDS1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1RowStatus.setStatus("mandatory")
_LpDS1ComponentName_Type = DisplayString
_LpDS1ComponentName_Object = MibTableColumn
lpDS1ComponentName = _LpDS1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 1, 1, 2),
    _LpDS1ComponentName_Type()
)
lpDS1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ComponentName.setStatus("mandatory")
_LpDS1StorageType_Type = StorageType
_LpDS1StorageType_Object = MibTableColumn
lpDS1StorageType = _LpDS1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 1, 1, 4),
    _LpDS1StorageType_Type()
)
lpDS1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1StorageType.setStatus("mandatory")


class _LpDS1Index_Type(Integer32):
    """Custom type lpDS1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LpDS1Index_Type.__name__ = "Integer32"
_LpDS1Index_Object = MibTableColumn
lpDS1Index = _LpDS1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 1, 1, 10),
    _LpDS1Index_Type()
)
lpDS1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1Index.setStatus("mandatory")
_LpDS1Chan_ObjectIdentity = ObjectIdentity
lpDS1Chan = _LpDS1Chan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2)
)
_LpDS1ChanRowStatusTable_Object = MibTable
lpDS1ChanRowStatusTable = _LpDS1ChanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 1)
)
if mibBuilder.loadTexts:
    lpDS1ChanRowStatusTable.setStatus("mandatory")
_LpDS1ChanRowStatusEntry_Object = MibTableRow
lpDS1ChanRowStatusEntry = _LpDS1ChanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 1, 1)
)
lpDS1ChanRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanRowStatusEntry.setStatus("mandatory")
_LpDS1ChanRowStatus_Type = RowStatus
_LpDS1ChanRowStatus_Object = MibTableColumn
lpDS1ChanRowStatus = _LpDS1ChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 1, 1, 1),
    _LpDS1ChanRowStatus_Type()
)
lpDS1ChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanRowStatus.setStatus("mandatory")
_LpDS1ChanComponentName_Type = DisplayString
_LpDS1ChanComponentName_Object = MibTableColumn
lpDS1ChanComponentName = _LpDS1ChanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 1, 1, 2),
    _LpDS1ChanComponentName_Type()
)
lpDS1ChanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanComponentName.setStatus("mandatory")
_LpDS1ChanStorageType_Type = StorageType
_LpDS1ChanStorageType_Object = MibTableColumn
lpDS1ChanStorageType = _LpDS1ChanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 1, 1, 4),
    _LpDS1ChanStorageType_Type()
)
lpDS1ChanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanStorageType.setStatus("mandatory")


class _LpDS1ChanIndex_Type(Integer32):
    """Custom type lpDS1ChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_LpDS1ChanIndex_Type.__name__ = "Integer32"
_LpDS1ChanIndex_Object = MibTableColumn
lpDS1ChanIndex = _LpDS1ChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 1, 1, 10),
    _LpDS1ChanIndex_Type()
)
lpDS1ChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1ChanIndex.setStatus("mandatory")
_LpDS1ChanTest_ObjectIdentity = ObjectIdentity
lpDS1ChanTest = _LpDS1ChanTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2)
)
_LpDS1ChanTestRowStatusTable_Object = MibTable
lpDS1ChanTestRowStatusTable = _LpDS1ChanTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpDS1ChanTestRowStatusTable.setStatus("mandatory")
_LpDS1ChanTestRowStatusEntry_Object = MibTableRow
lpDS1ChanTestRowStatusEntry = _LpDS1ChanTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 1, 1)
)
lpDS1ChanTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTestRowStatusEntry.setStatus("mandatory")
_LpDS1ChanTestRowStatus_Type = RowStatus
_LpDS1ChanTestRowStatus_Object = MibTableColumn
lpDS1ChanTestRowStatus = _LpDS1ChanTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 1, 1, 1),
    _LpDS1ChanTestRowStatus_Type()
)
lpDS1ChanTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestRowStatus.setStatus("mandatory")
_LpDS1ChanTestComponentName_Type = DisplayString
_LpDS1ChanTestComponentName_Object = MibTableColumn
lpDS1ChanTestComponentName = _LpDS1ChanTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 1, 1, 2),
    _LpDS1ChanTestComponentName_Type()
)
lpDS1ChanTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestComponentName.setStatus("mandatory")
_LpDS1ChanTestStorageType_Type = StorageType
_LpDS1ChanTestStorageType_Object = MibTableColumn
lpDS1ChanTestStorageType = _LpDS1ChanTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 1, 1, 4),
    _LpDS1ChanTestStorageType_Type()
)
lpDS1ChanTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestStorageType.setStatus("mandatory")
_LpDS1ChanTestIndex_Type = NonReplicated
_LpDS1ChanTestIndex_Object = MibTableColumn
lpDS1ChanTestIndex = _LpDS1ChanTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 1, 1, 10),
    _LpDS1ChanTestIndex_Type()
)
lpDS1ChanTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1ChanTestIndex.setStatus("mandatory")
_LpDS1ChanTestStateTable_Object = MibTable
lpDS1ChanTestStateTable = _LpDS1ChanTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpDS1ChanTestStateTable.setStatus("mandatory")
_LpDS1ChanTestStateEntry_Object = MibTableRow
lpDS1ChanTestStateEntry = _LpDS1ChanTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 10, 1)
)
lpDS1ChanTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTestStateEntry.setStatus("mandatory")


class _LpDS1ChanTestAdminState_Type(Integer32):
    """Custom type lpDS1ChanTestAdminState based on Integer32"""
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


_LpDS1ChanTestAdminState_Type.__name__ = "Integer32"
_LpDS1ChanTestAdminState_Object = MibTableColumn
lpDS1ChanTestAdminState = _LpDS1ChanTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 10, 1, 1),
    _LpDS1ChanTestAdminState_Type()
)
lpDS1ChanTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestAdminState.setStatus("mandatory")


class _LpDS1ChanTestOperationalState_Type(Integer32):
    """Custom type lpDS1ChanTestOperationalState based on Integer32"""
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


_LpDS1ChanTestOperationalState_Type.__name__ = "Integer32"
_LpDS1ChanTestOperationalState_Object = MibTableColumn
lpDS1ChanTestOperationalState = _LpDS1ChanTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 10, 1, 2),
    _LpDS1ChanTestOperationalState_Type()
)
lpDS1ChanTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestOperationalState.setStatus("mandatory")


class _LpDS1ChanTestUsageState_Type(Integer32):
    """Custom type lpDS1ChanTestUsageState based on Integer32"""
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


_LpDS1ChanTestUsageState_Type.__name__ = "Integer32"
_LpDS1ChanTestUsageState_Object = MibTableColumn
lpDS1ChanTestUsageState = _LpDS1ChanTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 10, 1, 3),
    _LpDS1ChanTestUsageState_Type()
)
lpDS1ChanTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestUsageState.setStatus("mandatory")
_LpDS1ChanTestSetupTable_Object = MibTable
lpDS1ChanTestSetupTable = _LpDS1ChanTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11)
)
if mibBuilder.loadTexts:
    lpDS1ChanTestSetupTable.setStatus("mandatory")
_LpDS1ChanTestSetupEntry_Object = MibTableRow
lpDS1ChanTestSetupEntry = _LpDS1ChanTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1)
)
lpDS1ChanTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTestSetupEntry.setStatus("mandatory")


class _LpDS1ChanTestPurpose_Type(AsciiString):
    """Custom type lpDS1ChanTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpDS1ChanTestPurpose_Type.__name__ = "AsciiString"
_LpDS1ChanTestPurpose_Object = MibTableColumn
lpDS1ChanTestPurpose = _LpDS1ChanTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 1),
    _LpDS1ChanTestPurpose_Type()
)
lpDS1ChanTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestPurpose.setStatus("mandatory")


class _LpDS1ChanTestType_Type(Integer32):
    """Custom type lpDS1ChanTestType based on Integer32"""
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


_LpDS1ChanTestType_Type.__name__ = "Integer32"
_LpDS1ChanTestType_Object = MibTableColumn
lpDS1ChanTestType = _LpDS1ChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 2),
    _LpDS1ChanTestType_Type()
)
lpDS1ChanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestType.setStatus("mandatory")


class _LpDS1ChanTestFrmSize_Type(Unsigned32):
    """Custom type lpDS1ChanTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpDS1ChanTestFrmSize_Type.__name__ = "Unsigned32"
_LpDS1ChanTestFrmSize_Object = MibTableColumn
lpDS1ChanTestFrmSize = _LpDS1ChanTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 3),
    _LpDS1ChanTestFrmSize_Type()
)
lpDS1ChanTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestFrmSize.setStatus("mandatory")


class _LpDS1ChanTestFrmPatternType_Type(Integer32):
    """Custom type lpDS1ChanTestFrmPatternType based on Integer32"""
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


_LpDS1ChanTestFrmPatternType_Type.__name__ = "Integer32"
_LpDS1ChanTestFrmPatternType_Object = MibTableColumn
lpDS1ChanTestFrmPatternType = _LpDS1ChanTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 4),
    _LpDS1ChanTestFrmPatternType_Type()
)
lpDS1ChanTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestFrmPatternType.setStatus("mandatory")


class _LpDS1ChanTestCustomizedPattern_Type(Hex):
    """Custom type lpDS1ChanTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS1ChanTestCustomizedPattern_Type.__name__ = "Hex"
_LpDS1ChanTestCustomizedPattern_Object = MibTableColumn
lpDS1ChanTestCustomizedPattern = _LpDS1ChanTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 5),
    _LpDS1ChanTestCustomizedPattern_Type()
)
lpDS1ChanTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestCustomizedPattern.setStatus("mandatory")


class _LpDS1ChanTestDataStartDelay_Type(Unsigned32):
    """Custom type lpDS1ChanTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpDS1ChanTestDataStartDelay_Type.__name__ = "Unsigned32"
_LpDS1ChanTestDataStartDelay_Object = MibTableColumn
lpDS1ChanTestDataStartDelay = _LpDS1ChanTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 6),
    _LpDS1ChanTestDataStartDelay_Type()
)
lpDS1ChanTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestDataStartDelay.setStatus("mandatory")


class _LpDS1ChanTestDisplayInterval_Type(Unsigned32):
    """Custom type lpDS1ChanTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpDS1ChanTestDisplayInterval_Type.__name__ = "Unsigned32"
_LpDS1ChanTestDisplayInterval_Object = MibTableColumn
lpDS1ChanTestDisplayInterval = _LpDS1ChanTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 7),
    _LpDS1ChanTestDisplayInterval_Type()
)
lpDS1ChanTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestDisplayInterval.setStatus("mandatory")


class _LpDS1ChanTestDuration_Type(Unsigned32):
    """Custom type lpDS1ChanTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpDS1ChanTestDuration_Type.__name__ = "Unsigned32"
_LpDS1ChanTestDuration_Object = MibTableColumn
lpDS1ChanTestDuration = _LpDS1ChanTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 11, 1, 8),
    _LpDS1ChanTestDuration_Type()
)
lpDS1ChanTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTestDuration.setStatus("mandatory")
_LpDS1ChanTestResultsTable_Object = MibTable
lpDS1ChanTestResultsTable = _LpDS1ChanTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12)
)
if mibBuilder.loadTexts:
    lpDS1ChanTestResultsTable.setStatus("mandatory")
_LpDS1ChanTestResultsEntry_Object = MibTableRow
lpDS1ChanTestResultsEntry = _LpDS1ChanTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1)
)
lpDS1ChanTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTestResultsEntry.setStatus("mandatory")
_LpDS1ChanTestElapsedTime_Type = Counter32
_LpDS1ChanTestElapsedTime_Object = MibTableColumn
lpDS1ChanTestElapsedTime = _LpDS1ChanTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 1),
    _LpDS1ChanTestElapsedTime_Type()
)
lpDS1ChanTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestElapsedTime.setStatus("mandatory")


class _LpDS1ChanTestTimeRemaining_Type(Unsigned32):
    """Custom type lpDS1ChanTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS1ChanTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpDS1ChanTestTimeRemaining_Object = MibTableColumn
lpDS1ChanTestTimeRemaining = _LpDS1ChanTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 2),
    _LpDS1ChanTestTimeRemaining_Type()
)
lpDS1ChanTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestTimeRemaining.setStatus("mandatory")


class _LpDS1ChanTestCauseOfTermination_Type(Integer32):
    """Custom type lpDS1ChanTestCauseOfTermination based on Integer32"""
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


_LpDS1ChanTestCauseOfTermination_Type.__name__ = "Integer32"
_LpDS1ChanTestCauseOfTermination_Object = MibTableColumn
lpDS1ChanTestCauseOfTermination = _LpDS1ChanTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 3),
    _LpDS1ChanTestCauseOfTermination_Type()
)
lpDS1ChanTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestCauseOfTermination.setStatus("mandatory")
_LpDS1ChanTestBitsTx_Type = PassportCounter64
_LpDS1ChanTestBitsTx_Object = MibTableColumn
lpDS1ChanTestBitsTx = _LpDS1ChanTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 4),
    _LpDS1ChanTestBitsTx_Type()
)
lpDS1ChanTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestBitsTx.setStatus("mandatory")
_LpDS1ChanTestBytesTx_Type = PassportCounter64
_LpDS1ChanTestBytesTx_Object = MibTableColumn
lpDS1ChanTestBytesTx = _LpDS1ChanTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 5),
    _LpDS1ChanTestBytesTx_Type()
)
lpDS1ChanTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestBytesTx.setStatus("mandatory")
_LpDS1ChanTestFrmTx_Type = PassportCounter64
_LpDS1ChanTestFrmTx_Object = MibTableColumn
lpDS1ChanTestFrmTx = _LpDS1ChanTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 6),
    _LpDS1ChanTestFrmTx_Type()
)
lpDS1ChanTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestFrmTx.setStatus("mandatory")
_LpDS1ChanTestBitsRx_Type = PassportCounter64
_LpDS1ChanTestBitsRx_Object = MibTableColumn
lpDS1ChanTestBitsRx = _LpDS1ChanTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 7),
    _LpDS1ChanTestBitsRx_Type()
)
lpDS1ChanTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestBitsRx.setStatus("mandatory")
_LpDS1ChanTestBytesRx_Type = PassportCounter64
_LpDS1ChanTestBytesRx_Object = MibTableColumn
lpDS1ChanTestBytesRx = _LpDS1ChanTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 8),
    _LpDS1ChanTestBytesRx_Type()
)
lpDS1ChanTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestBytesRx.setStatus("mandatory")
_LpDS1ChanTestFrmRx_Type = PassportCounter64
_LpDS1ChanTestFrmRx_Object = MibTableColumn
lpDS1ChanTestFrmRx = _LpDS1ChanTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 9),
    _LpDS1ChanTestFrmRx_Type()
)
lpDS1ChanTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestFrmRx.setStatus("mandatory")
_LpDS1ChanTestErroredFrmRx_Type = PassportCounter64
_LpDS1ChanTestErroredFrmRx_Object = MibTableColumn
lpDS1ChanTestErroredFrmRx = _LpDS1ChanTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 10),
    _LpDS1ChanTestErroredFrmRx_Type()
)
lpDS1ChanTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestErroredFrmRx.setStatus("mandatory")


class _LpDS1ChanTestBitErrorRate_Type(AsciiString):
    """Custom type lpDS1ChanTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpDS1ChanTestBitErrorRate_Type.__name__ = "AsciiString"
_LpDS1ChanTestBitErrorRate_Object = MibTableColumn
lpDS1ChanTestBitErrorRate = _LpDS1ChanTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 2, 12, 1, 11),
    _LpDS1ChanTestBitErrorRate_Type()
)
lpDS1ChanTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTestBitErrorRate.setStatus("mandatory")
_LpDS1ChanCell_ObjectIdentity = ObjectIdentity
lpDS1ChanCell = _LpDS1ChanCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3)
)
_LpDS1ChanCellRowStatusTable_Object = MibTable
lpDS1ChanCellRowStatusTable = _LpDS1ChanCellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpDS1ChanCellRowStatusTable.setStatus("mandatory")
_LpDS1ChanCellRowStatusEntry_Object = MibTableRow
lpDS1ChanCellRowStatusEntry = _LpDS1ChanCellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 1, 1)
)
lpDS1ChanCellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanCellRowStatusEntry.setStatus("mandatory")
_LpDS1ChanCellRowStatus_Type = RowStatus
_LpDS1ChanCellRowStatus_Object = MibTableColumn
lpDS1ChanCellRowStatus = _LpDS1ChanCellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 1, 1, 1),
    _LpDS1ChanCellRowStatus_Type()
)
lpDS1ChanCellRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanCellRowStatus.setStatus("mandatory")
_LpDS1ChanCellComponentName_Type = DisplayString
_LpDS1ChanCellComponentName_Object = MibTableColumn
lpDS1ChanCellComponentName = _LpDS1ChanCellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 1, 1, 2),
    _LpDS1ChanCellComponentName_Type()
)
lpDS1ChanCellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellComponentName.setStatus("mandatory")
_LpDS1ChanCellStorageType_Type = StorageType
_LpDS1ChanCellStorageType_Object = MibTableColumn
lpDS1ChanCellStorageType = _LpDS1ChanCellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 1, 1, 4),
    _LpDS1ChanCellStorageType_Type()
)
lpDS1ChanCellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellStorageType.setStatus("mandatory")
_LpDS1ChanCellIndex_Type = NonReplicated
_LpDS1ChanCellIndex_Object = MibTableColumn
lpDS1ChanCellIndex = _LpDS1ChanCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 1, 1, 10),
    _LpDS1ChanCellIndex_Type()
)
lpDS1ChanCellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1ChanCellIndex.setStatus("mandatory")
_LpDS1ChanCellProvTable_Object = MibTable
lpDS1ChanCellProvTable = _LpDS1ChanCellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpDS1ChanCellProvTable.setStatus("mandatory")
_LpDS1ChanCellProvEntry_Object = MibTableRow
lpDS1ChanCellProvEntry = _LpDS1ChanCellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 10, 1)
)
lpDS1ChanCellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanCellProvEntry.setStatus("mandatory")


class _LpDS1ChanCellAlarmActDelay_Type(Unsigned32):
    """Custom type lpDS1ChanCellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpDS1ChanCellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpDS1ChanCellAlarmActDelay_Object = MibTableColumn
lpDS1ChanCellAlarmActDelay = _LpDS1ChanCellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 10, 1, 1),
    _LpDS1ChanCellAlarmActDelay_Type()
)
lpDS1ChanCellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanCellAlarmActDelay.setStatus("mandatory")


class _LpDS1ChanCellScrambleCellPayload_Type(Integer32):
    """Custom type lpDS1ChanCellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS1ChanCellScrambleCellPayload_Type.__name__ = "Integer32"
_LpDS1ChanCellScrambleCellPayload_Object = MibTableColumn
lpDS1ChanCellScrambleCellPayload = _LpDS1ChanCellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 10, 1, 2),
    _LpDS1ChanCellScrambleCellPayload_Type()
)
lpDS1ChanCellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanCellScrambleCellPayload.setStatus("mandatory")


class _LpDS1ChanCellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpDS1ChanCellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS1ChanCellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpDS1ChanCellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpDS1ChanCellCorrectSingleBitHeaderErrors = _LpDS1ChanCellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 10, 1, 3),
    _LpDS1ChanCellCorrectSingleBitHeaderErrors_Type()
)
lpDS1ChanCellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanCellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpDS1ChanCellOperTable_Object = MibTable
lpDS1ChanCellOperTable = _LpDS1ChanCellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 11)
)
if mibBuilder.loadTexts:
    lpDS1ChanCellOperTable.setStatus("mandatory")
_LpDS1ChanCellOperEntry_Object = MibTableRow
lpDS1ChanCellOperEntry = _LpDS1ChanCellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 11, 1)
)
lpDS1ChanCellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanCellOperEntry.setStatus("mandatory")


class _LpDS1ChanCellLcdAlarm_Type(Integer32):
    """Custom type lpDS1ChanCellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS1ChanCellLcdAlarm_Type.__name__ = "Integer32"
_LpDS1ChanCellLcdAlarm_Object = MibTableColumn
lpDS1ChanCellLcdAlarm = _LpDS1ChanCellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 11, 1, 1),
    _LpDS1ChanCellLcdAlarm_Type()
)
lpDS1ChanCellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellLcdAlarm.setStatus("mandatory")
_LpDS1ChanCellStatsTable_Object = MibTable
lpDS1ChanCellStatsTable = _LpDS1ChanCellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 12)
)
if mibBuilder.loadTexts:
    lpDS1ChanCellStatsTable.setStatus("mandatory")
_LpDS1ChanCellStatsEntry_Object = MibTableRow
lpDS1ChanCellStatsEntry = _LpDS1ChanCellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 12, 1)
)
lpDS1ChanCellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanCellStatsEntry.setStatus("mandatory")
_LpDS1ChanCellUncorrectableHecErrors_Type = Counter32
_LpDS1ChanCellUncorrectableHecErrors_Object = MibTableColumn
lpDS1ChanCellUncorrectableHecErrors = _LpDS1ChanCellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 12, 1, 1),
    _LpDS1ChanCellUncorrectableHecErrors_Type()
)
lpDS1ChanCellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellUncorrectableHecErrors.setStatus("mandatory")
_LpDS1ChanCellSevErroredSec_Type = Counter32
_LpDS1ChanCellSevErroredSec_Object = MibTableColumn
lpDS1ChanCellSevErroredSec = _LpDS1ChanCellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 12, 1, 2),
    _LpDS1ChanCellSevErroredSec_Type()
)
lpDS1ChanCellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellSevErroredSec.setStatus("mandatory")


class _LpDS1ChanCellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpDS1ChanCellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpDS1ChanCellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpDS1ChanCellReceiveCellUtilization_Object = MibTableColumn
lpDS1ChanCellReceiveCellUtilization = _LpDS1ChanCellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 12, 1, 3),
    _LpDS1ChanCellReceiveCellUtilization_Type()
)
lpDS1ChanCellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellReceiveCellUtilization.setStatus("mandatory")


class _LpDS1ChanCellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpDS1ChanCellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpDS1ChanCellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpDS1ChanCellTransmitCellUtilization_Object = MibTableColumn
lpDS1ChanCellTransmitCellUtilization = _LpDS1ChanCellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 12, 1, 4),
    _LpDS1ChanCellTransmitCellUtilization_Type()
)
lpDS1ChanCellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellTransmitCellUtilization.setStatus("mandatory")
_LpDS1ChanCellCorrectableHeaderErrors_Type = Counter32
_LpDS1ChanCellCorrectableHeaderErrors_Object = MibTableColumn
lpDS1ChanCellCorrectableHeaderErrors = _LpDS1ChanCellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 3, 12, 1, 5),
    _LpDS1ChanCellCorrectableHeaderErrors_Type()
)
lpDS1ChanCellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanCellCorrectableHeaderErrors.setStatus("mandatory")
_LpDS1ChanTc_ObjectIdentity = ObjectIdentity
lpDS1ChanTc = _LpDS1ChanTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4)
)
_LpDS1ChanTcRowStatusTable_Object = MibTable
lpDS1ChanTcRowStatusTable = _LpDS1ChanTcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpDS1ChanTcRowStatusTable.setStatus("mandatory")
_LpDS1ChanTcRowStatusEntry_Object = MibTableRow
lpDS1ChanTcRowStatusEntry = _LpDS1ChanTcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 1, 1)
)
lpDS1ChanTcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTcRowStatusEntry.setStatus("mandatory")
_LpDS1ChanTcRowStatus_Type = RowStatus
_LpDS1ChanTcRowStatus_Object = MibTableColumn
lpDS1ChanTcRowStatus = _LpDS1ChanTcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 1, 1, 1),
    _LpDS1ChanTcRowStatus_Type()
)
lpDS1ChanTcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTcRowStatus.setStatus("mandatory")
_LpDS1ChanTcComponentName_Type = DisplayString
_LpDS1ChanTcComponentName_Object = MibTableColumn
lpDS1ChanTcComponentName = _LpDS1ChanTcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 1, 1, 2),
    _LpDS1ChanTcComponentName_Type()
)
lpDS1ChanTcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTcComponentName.setStatus("mandatory")
_LpDS1ChanTcStorageType_Type = StorageType
_LpDS1ChanTcStorageType_Object = MibTableColumn
lpDS1ChanTcStorageType = _LpDS1ChanTcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 1, 1, 4),
    _LpDS1ChanTcStorageType_Type()
)
lpDS1ChanTcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTcStorageType.setStatus("mandatory")
_LpDS1ChanTcIndex_Type = NonReplicated
_LpDS1ChanTcIndex_Object = MibTableColumn
lpDS1ChanTcIndex = _LpDS1ChanTcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 1, 1, 10),
    _LpDS1ChanTcIndex_Type()
)
lpDS1ChanTcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1ChanTcIndex.setStatus("mandatory")
_LpDS1ChanTcProvTable_Object = MibTable
lpDS1ChanTcProvTable = _LpDS1ChanTcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpDS1ChanTcProvTable.setStatus("mandatory")
_LpDS1ChanTcProvEntry_Object = MibTableRow
lpDS1ChanTcProvEntry = _LpDS1ChanTcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 10, 1)
)
lpDS1ChanTcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTcProvEntry.setStatus("mandatory")


class _LpDS1ChanTcReplacementData_Type(Hex):
    """Custom type lpDS1ChanTcReplacementData based on Hex"""
    defaultValue = 255

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LpDS1ChanTcReplacementData_Type.__name__ = "Hex"
_LpDS1ChanTcReplacementData_Object = MibTableColumn
lpDS1ChanTcReplacementData = _LpDS1ChanTcReplacementData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 10, 1, 1),
    _LpDS1ChanTcReplacementData_Type()
)
lpDS1ChanTcReplacementData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTcReplacementData.setStatus("mandatory")


class _LpDS1ChanTcSignalOneDuration_Type(Unsigned32):
    """Custom type lpDS1ChanTcSignalOneDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_LpDS1ChanTcSignalOneDuration_Type.__name__ = "Unsigned32"
_LpDS1ChanTcSignalOneDuration_Object = MibTableColumn
lpDS1ChanTcSignalOneDuration = _LpDS1ChanTcSignalOneDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 10, 1, 2),
    _LpDS1ChanTcSignalOneDuration_Type()
)
lpDS1ChanTcSignalOneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTcSignalOneDuration.setStatus("mandatory")
_LpDS1ChanTcOpTable_Object = MibTable
lpDS1ChanTcOpTable = _LpDS1ChanTcOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 11)
)
if mibBuilder.loadTexts:
    lpDS1ChanTcOpTable.setStatus("mandatory")
_LpDS1ChanTcOpEntry_Object = MibTableRow
lpDS1ChanTcOpEntry = _LpDS1ChanTcOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 11, 1)
)
lpDS1ChanTcOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTcOpEntry.setStatus("mandatory")


class _LpDS1ChanTcIngressConditioning_Type(Integer32):
    """Custom type lpDS1ChanTcIngressConditioning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS1ChanTcIngressConditioning_Type.__name__ = "Integer32"
_LpDS1ChanTcIngressConditioning_Object = MibTableColumn
lpDS1ChanTcIngressConditioning = _LpDS1ChanTcIngressConditioning_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 11, 1, 1),
    _LpDS1ChanTcIngressConditioning_Type()
)
lpDS1ChanTcIngressConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTcIngressConditioning.setStatus("mandatory")


class _LpDS1ChanTcEgressConditioning_Type(Integer32):
    """Custom type lpDS1ChanTcEgressConditioning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpDS1ChanTcEgressConditioning_Type.__name__ = "Integer32"
_LpDS1ChanTcEgressConditioning_Object = MibTableColumn
lpDS1ChanTcEgressConditioning = _LpDS1ChanTcEgressConditioning_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 11, 1, 2),
    _LpDS1ChanTcEgressConditioning_Type()
)
lpDS1ChanTcEgressConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanTcEgressConditioning.setStatus("mandatory")
_LpDS1ChanTcSigOneTable_Object = MibTable
lpDS1ChanTcSigOneTable = _LpDS1ChanTcSigOneTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 398)
)
if mibBuilder.loadTexts:
    lpDS1ChanTcSigOneTable.setStatus("mandatory")
_LpDS1ChanTcSigOneEntry_Object = MibTableRow
lpDS1ChanTcSigOneEntry = _LpDS1ChanTcSigOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 398, 1)
)
lpDS1ChanTcSigOneEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTcIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTcSigOneIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTcSigOneEntry.setStatus("mandatory")


class _LpDS1ChanTcSigOneIndex_Type(Integer32):
    """Custom type lpDS1ChanTcSigOneIndex based on Integer32"""
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
        *(("a", 3),
          ("b", 2),
          ("c", 1),
          ("d", 0))
    )


_LpDS1ChanTcSigOneIndex_Type.__name__ = "Integer32"
_LpDS1ChanTcSigOneIndex_Object = MibTableColumn
lpDS1ChanTcSigOneIndex = _LpDS1ChanTcSigOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 398, 1, 1),
    _LpDS1ChanTcSigOneIndex_Type()
)
lpDS1ChanTcSigOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1ChanTcSigOneIndex.setStatus("mandatory")


class _LpDS1ChanTcSigOneValue_Type(Unsigned32):
    """Custom type lpDS1ChanTcSigOneValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpDS1ChanTcSigOneValue_Type.__name__ = "Unsigned32"
_LpDS1ChanTcSigOneValue_Object = MibTableColumn
lpDS1ChanTcSigOneValue = _LpDS1ChanTcSigOneValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 398, 1, 2),
    _LpDS1ChanTcSigOneValue_Type()
)
lpDS1ChanTcSigOneValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTcSigOneValue.setStatus("mandatory")
_LpDS1ChanTcSigTwoTable_Object = MibTable
lpDS1ChanTcSigTwoTable = _LpDS1ChanTcSigTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 399)
)
if mibBuilder.loadTexts:
    lpDS1ChanTcSigTwoTable.setStatus("mandatory")
_LpDS1ChanTcSigTwoEntry_Object = MibTableRow
lpDS1ChanTcSigTwoEntry = _LpDS1ChanTcSigTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 399, 1)
)
lpDS1ChanTcSigTwoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTcIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanTcSigTwoIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanTcSigTwoEntry.setStatus("mandatory")


class _LpDS1ChanTcSigTwoIndex_Type(Integer32):
    """Custom type lpDS1ChanTcSigTwoIndex based on Integer32"""
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
        *(("a", 3),
          ("b", 2),
          ("c", 1),
          ("d", 0))
    )


_LpDS1ChanTcSigTwoIndex_Type.__name__ = "Integer32"
_LpDS1ChanTcSigTwoIndex_Object = MibTableColumn
lpDS1ChanTcSigTwoIndex = _LpDS1ChanTcSigTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 399, 1, 1),
    _LpDS1ChanTcSigTwoIndex_Type()
)
lpDS1ChanTcSigTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1ChanTcSigTwoIndex.setStatus("mandatory")


class _LpDS1ChanTcSigTwoValue_Type(Unsigned32):
    """Custom type lpDS1ChanTcSigTwoValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpDS1ChanTcSigTwoValue_Type.__name__ = "Unsigned32"
_LpDS1ChanTcSigTwoValue_Object = MibTableColumn
lpDS1ChanTcSigTwoValue = _LpDS1ChanTcSigTwoValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 4, 399, 1, 2),
    _LpDS1ChanTcSigTwoValue_Type()
)
lpDS1ChanTcSigTwoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTcSigTwoValue.setStatus("mandatory")
_LpDS1ChanProvTable_Object = MibTable
lpDS1ChanProvTable = _LpDS1ChanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 10)
)
if mibBuilder.loadTexts:
    lpDS1ChanProvTable.setStatus("mandatory")
_LpDS1ChanProvEntry_Object = MibTableRow
lpDS1ChanProvEntry = _LpDS1ChanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 10, 1)
)
lpDS1ChanProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanProvEntry.setStatus("mandatory")


class _LpDS1ChanTimeslots_Type(OctetString):
    """Custom type lpDS1ChanTimeslots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpDS1ChanTimeslots_Type.__name__ = "OctetString"
_LpDS1ChanTimeslots_Object = MibTableColumn
lpDS1ChanTimeslots = _LpDS1ChanTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 10, 1, 1),
    _LpDS1ChanTimeslots_Type()
)
lpDS1ChanTimeslots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTimeslots.setStatus("mandatory")


class _LpDS1ChanTimeslotDataRate_Type(Integer32):
    """Custom type lpDS1ChanTimeslotDataRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNotOverride", 1),
          ("n56k", 0))
    )


_LpDS1ChanTimeslotDataRate_Type.__name__ = "Integer32"
_LpDS1ChanTimeslotDataRate_Object = MibTableColumn
lpDS1ChanTimeslotDataRate = _LpDS1ChanTimeslotDataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 10, 1, 2),
    _LpDS1ChanTimeslotDataRate_Type()
)
lpDS1ChanTimeslotDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanTimeslotDataRate.setStatus("mandatory")
_LpDS1ChanApplicationFramerName_Type = Link
_LpDS1ChanApplicationFramerName_Object = MibTableColumn
lpDS1ChanApplicationFramerName = _LpDS1ChanApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 10, 1, 3),
    _LpDS1ChanApplicationFramerName_Type()
)
lpDS1ChanApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanApplicationFramerName.setStatus("mandatory")
_LpDS1ChanCidDataTable_Object = MibTable
lpDS1ChanCidDataTable = _LpDS1ChanCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 11)
)
if mibBuilder.loadTexts:
    lpDS1ChanCidDataTable.setStatus("mandatory")
_LpDS1ChanCidDataEntry_Object = MibTableRow
lpDS1ChanCidDataEntry = _LpDS1ChanCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 11, 1)
)
lpDS1ChanCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanCidDataEntry.setStatus("mandatory")


class _LpDS1ChanCustomerIdentifier_Type(Unsigned32):
    """Custom type lpDS1ChanCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpDS1ChanCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpDS1ChanCustomerIdentifier_Object = MibTableColumn
lpDS1ChanCustomerIdentifier = _LpDS1ChanCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 11, 1, 1),
    _LpDS1ChanCustomerIdentifier_Type()
)
lpDS1ChanCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanCustomerIdentifier.setStatus("mandatory")
_LpDS1ChanIfEntryTable_Object = MibTable
lpDS1ChanIfEntryTable = _LpDS1ChanIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 12)
)
if mibBuilder.loadTexts:
    lpDS1ChanIfEntryTable.setStatus("mandatory")
_LpDS1ChanIfEntryEntry_Object = MibTableRow
lpDS1ChanIfEntryEntry = _LpDS1ChanIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 12, 1)
)
lpDS1ChanIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanIfEntryEntry.setStatus("mandatory")


class _LpDS1ChanIfAdminStatus_Type(Integer32):
    """Custom type lpDS1ChanIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS1ChanIfAdminStatus_Type.__name__ = "Integer32"
_LpDS1ChanIfAdminStatus_Object = MibTableColumn
lpDS1ChanIfAdminStatus = _LpDS1ChanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 12, 1, 1),
    _LpDS1ChanIfAdminStatus_Type()
)
lpDS1ChanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanIfAdminStatus.setStatus("mandatory")


class _LpDS1ChanIfIndex_Type(InterfaceIndex):
    """Custom type lpDS1ChanIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpDS1ChanIfIndex_Type.__name__ = "InterfaceIndex"
_LpDS1ChanIfIndex_Object = MibTableColumn
lpDS1ChanIfIndex = _LpDS1ChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 12, 1, 2),
    _LpDS1ChanIfIndex_Type()
)
lpDS1ChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanIfIndex.setStatus("mandatory")
_LpDS1ChanOperStatusTable_Object = MibTable
lpDS1ChanOperStatusTable = _LpDS1ChanOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 13)
)
if mibBuilder.loadTexts:
    lpDS1ChanOperStatusTable.setStatus("mandatory")
_LpDS1ChanOperStatusEntry_Object = MibTableRow
lpDS1ChanOperStatusEntry = _LpDS1ChanOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 13, 1)
)
lpDS1ChanOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanOperStatusEntry.setStatus("mandatory")


class _LpDS1ChanSnmpOperStatus_Type(Integer32):
    """Custom type lpDS1ChanSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS1ChanSnmpOperStatus_Type.__name__ = "Integer32"
_LpDS1ChanSnmpOperStatus_Object = MibTableColumn
lpDS1ChanSnmpOperStatus = _LpDS1ChanSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 13, 1, 1),
    _LpDS1ChanSnmpOperStatus_Type()
)
lpDS1ChanSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanSnmpOperStatus.setStatus("mandatory")
_LpDS1ChanStateTable_Object = MibTable
lpDS1ChanStateTable = _LpDS1ChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14)
)
if mibBuilder.loadTexts:
    lpDS1ChanStateTable.setStatus("mandatory")
_LpDS1ChanStateEntry_Object = MibTableRow
lpDS1ChanStateEntry = _LpDS1ChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1)
)
lpDS1ChanStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanStateEntry.setStatus("mandatory")


class _LpDS1ChanAdminState_Type(Integer32):
    """Custom type lpDS1ChanAdminState based on Integer32"""
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


_LpDS1ChanAdminState_Type.__name__ = "Integer32"
_LpDS1ChanAdminState_Object = MibTableColumn
lpDS1ChanAdminState = _LpDS1ChanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 1),
    _LpDS1ChanAdminState_Type()
)
lpDS1ChanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanAdminState.setStatus("mandatory")


class _LpDS1ChanOperationalState_Type(Integer32):
    """Custom type lpDS1ChanOperationalState based on Integer32"""
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


_LpDS1ChanOperationalState_Type.__name__ = "Integer32"
_LpDS1ChanOperationalState_Object = MibTableColumn
lpDS1ChanOperationalState = _LpDS1ChanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 2),
    _LpDS1ChanOperationalState_Type()
)
lpDS1ChanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanOperationalState.setStatus("mandatory")


class _LpDS1ChanUsageState_Type(Integer32):
    """Custom type lpDS1ChanUsageState based on Integer32"""
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


_LpDS1ChanUsageState_Type.__name__ = "Integer32"
_LpDS1ChanUsageState_Object = MibTableColumn
lpDS1ChanUsageState = _LpDS1ChanUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 3),
    _LpDS1ChanUsageState_Type()
)
lpDS1ChanUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanUsageState.setStatus("mandatory")


class _LpDS1ChanAvailabilityStatus_Type(OctetString):
    """Custom type lpDS1ChanAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpDS1ChanAvailabilityStatus_Type.__name__ = "OctetString"
_LpDS1ChanAvailabilityStatus_Object = MibTableColumn
lpDS1ChanAvailabilityStatus = _LpDS1ChanAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 4),
    _LpDS1ChanAvailabilityStatus_Type()
)
lpDS1ChanAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanAvailabilityStatus.setStatus("mandatory")


class _LpDS1ChanProceduralStatus_Type(OctetString):
    """Custom type lpDS1ChanProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS1ChanProceduralStatus_Type.__name__ = "OctetString"
_LpDS1ChanProceduralStatus_Object = MibTableColumn
lpDS1ChanProceduralStatus = _LpDS1ChanProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 5),
    _LpDS1ChanProceduralStatus_Type()
)
lpDS1ChanProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanProceduralStatus.setStatus("mandatory")


class _LpDS1ChanControlStatus_Type(OctetString):
    """Custom type lpDS1ChanControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS1ChanControlStatus_Type.__name__ = "OctetString"
_LpDS1ChanControlStatus_Object = MibTableColumn
lpDS1ChanControlStatus = _LpDS1ChanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 6),
    _LpDS1ChanControlStatus_Type()
)
lpDS1ChanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanControlStatus.setStatus("mandatory")


class _LpDS1ChanAlarmStatus_Type(OctetString):
    """Custom type lpDS1ChanAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS1ChanAlarmStatus_Type.__name__ = "OctetString"
_LpDS1ChanAlarmStatus_Object = MibTableColumn
lpDS1ChanAlarmStatus = _LpDS1ChanAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 7),
    _LpDS1ChanAlarmStatus_Type()
)
lpDS1ChanAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanAlarmStatus.setStatus("mandatory")


class _LpDS1ChanStandbyStatus_Type(Integer32):
    """Custom type lpDS1ChanStandbyStatus based on Integer32"""
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


_LpDS1ChanStandbyStatus_Type.__name__ = "Integer32"
_LpDS1ChanStandbyStatus_Object = MibTableColumn
lpDS1ChanStandbyStatus = _LpDS1ChanStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 8),
    _LpDS1ChanStandbyStatus_Type()
)
lpDS1ChanStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanStandbyStatus.setStatus("mandatory")


class _LpDS1ChanUnknownStatus_Type(Integer32):
    """Custom type lpDS1ChanUnknownStatus based on Integer32"""
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


_LpDS1ChanUnknownStatus_Type.__name__ = "Integer32"
_LpDS1ChanUnknownStatus_Object = MibTableColumn
lpDS1ChanUnknownStatus = _LpDS1ChanUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 14, 1, 9),
    _LpDS1ChanUnknownStatus_Type()
)
lpDS1ChanUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanUnknownStatus.setStatus("mandatory")
_LpDS1ChanOperTable_Object = MibTable
lpDS1ChanOperTable = _LpDS1ChanOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 15)
)
if mibBuilder.loadTexts:
    lpDS1ChanOperTable.setStatus("mandatory")
_LpDS1ChanOperEntry_Object = MibTableRow
lpDS1ChanOperEntry = _LpDS1ChanOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 15, 1)
)
lpDS1ChanOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanOperEntry.setStatus("mandatory")


class _LpDS1ChanActualChannelSpeed_Type(Gauge32):
    """Custom type lpDS1ChanActualChannelSpeed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS1ChanActualChannelSpeed_Type.__name__ = "Gauge32"
_LpDS1ChanActualChannelSpeed_Object = MibTableColumn
lpDS1ChanActualChannelSpeed = _LpDS1ChanActualChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 15, 1, 1),
    _LpDS1ChanActualChannelSpeed_Type()
)
lpDS1ChanActualChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ChanActualChannelSpeed.setStatus("mandatory")
_LpDS1ChanAdminInfoTable_Object = MibTable
lpDS1ChanAdminInfoTable = _LpDS1ChanAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 16)
)
if mibBuilder.loadTexts:
    lpDS1ChanAdminInfoTable.setStatus("mandatory")
_LpDS1ChanAdminInfoEntry_Object = MibTableRow
lpDS1ChanAdminInfoEntry = _LpDS1ChanAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 16, 1)
)
lpDS1ChanAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpDS1ChanAdminInfoEntry.setStatus("mandatory")


class _LpDS1ChanVendor_Type(AsciiString):
    """Custom type lpDS1ChanVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpDS1ChanVendor_Type.__name__ = "AsciiString"
_LpDS1ChanVendor_Object = MibTableColumn
lpDS1ChanVendor = _LpDS1ChanVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 16, 1, 1),
    _LpDS1ChanVendor_Type()
)
lpDS1ChanVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanVendor.setStatus("mandatory")


class _LpDS1ChanCommentText_Type(AsciiString):
    """Custom type lpDS1ChanCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpDS1ChanCommentText_Type.__name__ = "AsciiString"
_LpDS1ChanCommentText_Object = MibTableColumn
lpDS1ChanCommentText = _LpDS1ChanCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 2, 16, 1, 2),
    _LpDS1ChanCommentText_Type()
)
lpDS1ChanCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ChanCommentText.setStatus("mandatory")
_LpDS1Test_ObjectIdentity = ObjectIdentity
lpDS1Test = _LpDS1Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3)
)
_LpDS1TestRowStatusTable_Object = MibTable
lpDS1TestRowStatusTable = _LpDS1TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 1)
)
if mibBuilder.loadTexts:
    lpDS1TestRowStatusTable.setStatus("mandatory")
_LpDS1TestRowStatusEntry_Object = MibTableRow
lpDS1TestRowStatusEntry = _LpDS1TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 1, 1)
)
lpDS1TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1TestRowStatusEntry.setStatus("mandatory")
_LpDS1TestRowStatus_Type = RowStatus
_LpDS1TestRowStatus_Object = MibTableColumn
lpDS1TestRowStatus = _LpDS1TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 1, 1, 1),
    _LpDS1TestRowStatus_Type()
)
lpDS1TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestRowStatus.setStatus("mandatory")
_LpDS1TestComponentName_Type = DisplayString
_LpDS1TestComponentName_Object = MibTableColumn
lpDS1TestComponentName = _LpDS1TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 1, 1, 2),
    _LpDS1TestComponentName_Type()
)
lpDS1TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestComponentName.setStatus("mandatory")
_LpDS1TestStorageType_Type = StorageType
_LpDS1TestStorageType_Object = MibTableColumn
lpDS1TestStorageType = _LpDS1TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 1, 1, 4),
    _LpDS1TestStorageType_Type()
)
lpDS1TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestStorageType.setStatus("mandatory")
_LpDS1TestIndex_Type = NonReplicated
_LpDS1TestIndex_Object = MibTableColumn
lpDS1TestIndex = _LpDS1TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 1, 1, 10),
    _LpDS1TestIndex_Type()
)
lpDS1TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1TestIndex.setStatus("mandatory")
_LpDS1TestStateTable_Object = MibTable
lpDS1TestStateTable = _LpDS1TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 10)
)
if mibBuilder.loadTexts:
    lpDS1TestStateTable.setStatus("mandatory")
_LpDS1TestStateEntry_Object = MibTableRow
lpDS1TestStateEntry = _LpDS1TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 10, 1)
)
lpDS1TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1TestStateEntry.setStatus("mandatory")


class _LpDS1TestAdminState_Type(Integer32):
    """Custom type lpDS1TestAdminState based on Integer32"""
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


_LpDS1TestAdminState_Type.__name__ = "Integer32"
_LpDS1TestAdminState_Object = MibTableColumn
lpDS1TestAdminState = _LpDS1TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 10, 1, 1),
    _LpDS1TestAdminState_Type()
)
lpDS1TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestAdminState.setStatus("mandatory")


class _LpDS1TestOperationalState_Type(Integer32):
    """Custom type lpDS1TestOperationalState based on Integer32"""
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


_LpDS1TestOperationalState_Type.__name__ = "Integer32"
_LpDS1TestOperationalState_Object = MibTableColumn
lpDS1TestOperationalState = _LpDS1TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 10, 1, 2),
    _LpDS1TestOperationalState_Type()
)
lpDS1TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestOperationalState.setStatus("mandatory")


class _LpDS1TestUsageState_Type(Integer32):
    """Custom type lpDS1TestUsageState based on Integer32"""
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


_LpDS1TestUsageState_Type.__name__ = "Integer32"
_LpDS1TestUsageState_Object = MibTableColumn
lpDS1TestUsageState = _LpDS1TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 10, 1, 3),
    _LpDS1TestUsageState_Type()
)
lpDS1TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestUsageState.setStatus("mandatory")
_LpDS1TestSetupTable_Object = MibTable
lpDS1TestSetupTable = _LpDS1TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11)
)
if mibBuilder.loadTexts:
    lpDS1TestSetupTable.setStatus("mandatory")
_LpDS1TestSetupEntry_Object = MibTableRow
lpDS1TestSetupEntry = _LpDS1TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1)
)
lpDS1TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1TestSetupEntry.setStatus("mandatory")


class _LpDS1TestPurpose_Type(AsciiString):
    """Custom type lpDS1TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpDS1TestPurpose_Type.__name__ = "AsciiString"
_LpDS1TestPurpose_Object = MibTableColumn
lpDS1TestPurpose = _LpDS1TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 1),
    _LpDS1TestPurpose_Type()
)
lpDS1TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestPurpose.setStatus("mandatory")


class _LpDS1TestType_Type(Integer32):
    """Custom type lpDS1TestType based on Integer32"""
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


_LpDS1TestType_Type.__name__ = "Integer32"
_LpDS1TestType_Object = MibTableColumn
lpDS1TestType = _LpDS1TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 2),
    _LpDS1TestType_Type()
)
lpDS1TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestType.setStatus("mandatory")


class _LpDS1TestFrmSize_Type(Unsigned32):
    """Custom type lpDS1TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpDS1TestFrmSize_Type.__name__ = "Unsigned32"
_LpDS1TestFrmSize_Object = MibTableColumn
lpDS1TestFrmSize = _LpDS1TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 3),
    _LpDS1TestFrmSize_Type()
)
lpDS1TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestFrmSize.setStatus("mandatory")


class _LpDS1TestFrmPatternType_Type(Integer32):
    """Custom type lpDS1TestFrmPatternType based on Integer32"""
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


_LpDS1TestFrmPatternType_Type.__name__ = "Integer32"
_LpDS1TestFrmPatternType_Object = MibTableColumn
lpDS1TestFrmPatternType = _LpDS1TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 4),
    _LpDS1TestFrmPatternType_Type()
)
lpDS1TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestFrmPatternType.setStatus("mandatory")


class _LpDS1TestCustomizedPattern_Type(Hex):
    """Custom type lpDS1TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS1TestCustomizedPattern_Type.__name__ = "Hex"
_LpDS1TestCustomizedPattern_Object = MibTableColumn
lpDS1TestCustomizedPattern = _LpDS1TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 5),
    _LpDS1TestCustomizedPattern_Type()
)
lpDS1TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestCustomizedPattern.setStatus("mandatory")


class _LpDS1TestDataStartDelay_Type(Unsigned32):
    """Custom type lpDS1TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpDS1TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpDS1TestDataStartDelay_Object = MibTableColumn
lpDS1TestDataStartDelay = _LpDS1TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 6),
    _LpDS1TestDataStartDelay_Type()
)
lpDS1TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestDataStartDelay.setStatus("mandatory")


class _LpDS1TestDisplayInterval_Type(Unsigned32):
    """Custom type lpDS1TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpDS1TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpDS1TestDisplayInterval_Object = MibTableColumn
lpDS1TestDisplayInterval = _LpDS1TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 7),
    _LpDS1TestDisplayInterval_Type()
)
lpDS1TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestDisplayInterval.setStatus("mandatory")


class _LpDS1TestDuration_Type(Unsigned32):
    """Custom type lpDS1TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpDS1TestDuration_Type.__name__ = "Unsigned32"
_LpDS1TestDuration_Object = MibTableColumn
lpDS1TestDuration = _LpDS1TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 11, 1, 8),
    _LpDS1TestDuration_Type()
)
lpDS1TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1TestDuration.setStatus("mandatory")
_LpDS1TestResultsTable_Object = MibTable
lpDS1TestResultsTable = _LpDS1TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12)
)
if mibBuilder.loadTexts:
    lpDS1TestResultsTable.setStatus("mandatory")
_LpDS1TestResultsEntry_Object = MibTableRow
lpDS1TestResultsEntry = _LpDS1TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1)
)
lpDS1TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1TestIndex"),
)
if mibBuilder.loadTexts:
    lpDS1TestResultsEntry.setStatus("mandatory")
_LpDS1TestElapsedTime_Type = Counter32
_LpDS1TestElapsedTime_Object = MibTableColumn
lpDS1TestElapsedTime = _LpDS1TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 1),
    _LpDS1TestElapsedTime_Type()
)
lpDS1TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestElapsedTime.setStatus("mandatory")


class _LpDS1TestTimeRemaining_Type(Unsigned32):
    """Custom type lpDS1TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpDS1TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpDS1TestTimeRemaining_Object = MibTableColumn
lpDS1TestTimeRemaining = _LpDS1TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 2),
    _LpDS1TestTimeRemaining_Type()
)
lpDS1TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestTimeRemaining.setStatus("mandatory")


class _LpDS1TestCauseOfTermination_Type(Integer32):
    """Custom type lpDS1TestCauseOfTermination based on Integer32"""
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


_LpDS1TestCauseOfTermination_Type.__name__ = "Integer32"
_LpDS1TestCauseOfTermination_Object = MibTableColumn
lpDS1TestCauseOfTermination = _LpDS1TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 3),
    _LpDS1TestCauseOfTermination_Type()
)
lpDS1TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestCauseOfTermination.setStatus("mandatory")
_LpDS1TestBitsTx_Type = PassportCounter64
_LpDS1TestBitsTx_Object = MibTableColumn
lpDS1TestBitsTx = _LpDS1TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 4),
    _LpDS1TestBitsTx_Type()
)
lpDS1TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestBitsTx.setStatus("mandatory")
_LpDS1TestBytesTx_Type = PassportCounter64
_LpDS1TestBytesTx_Object = MibTableColumn
lpDS1TestBytesTx = _LpDS1TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 5),
    _LpDS1TestBytesTx_Type()
)
lpDS1TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestBytesTx.setStatus("mandatory")
_LpDS1TestFrmTx_Type = PassportCounter64
_LpDS1TestFrmTx_Object = MibTableColumn
lpDS1TestFrmTx = _LpDS1TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 6),
    _LpDS1TestFrmTx_Type()
)
lpDS1TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestFrmTx.setStatus("mandatory")
_LpDS1TestBitsRx_Type = PassportCounter64
_LpDS1TestBitsRx_Object = MibTableColumn
lpDS1TestBitsRx = _LpDS1TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 7),
    _LpDS1TestBitsRx_Type()
)
lpDS1TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestBitsRx.setStatus("mandatory")
_LpDS1TestBytesRx_Type = PassportCounter64
_LpDS1TestBytesRx_Object = MibTableColumn
lpDS1TestBytesRx = _LpDS1TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 8),
    _LpDS1TestBytesRx_Type()
)
lpDS1TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestBytesRx.setStatus("mandatory")
_LpDS1TestFrmRx_Type = PassportCounter64
_LpDS1TestFrmRx_Object = MibTableColumn
lpDS1TestFrmRx = _LpDS1TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 9),
    _LpDS1TestFrmRx_Type()
)
lpDS1TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestFrmRx.setStatus("mandatory")
_LpDS1TestErroredFrmRx_Type = PassportCounter64
_LpDS1TestErroredFrmRx_Object = MibTableColumn
lpDS1TestErroredFrmRx = _LpDS1TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 10),
    _LpDS1TestErroredFrmRx_Type()
)
lpDS1TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestErroredFrmRx.setStatus("mandatory")


class _LpDS1TestBitErrorRate_Type(AsciiString):
    """Custom type lpDS1TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpDS1TestBitErrorRate_Type.__name__ = "AsciiString"
_LpDS1TestBitErrorRate_Object = MibTableColumn
lpDS1TestBitErrorRate = _LpDS1TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 3, 12, 1, 11),
    _LpDS1TestBitErrorRate_Type()
)
lpDS1TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TestBitErrorRate.setStatus("mandatory")
_LpDS1Dsp_ObjectIdentity = ObjectIdentity
lpDS1Dsp = _LpDS1Dsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 4)
)
_LpDS1DspRowStatusTable_Object = MibTable
lpDS1DspRowStatusTable = _LpDS1DspRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 4, 1)
)
if mibBuilder.loadTexts:
    lpDS1DspRowStatusTable.setStatus("mandatory")
_LpDS1DspRowStatusEntry_Object = MibTableRow
lpDS1DspRowStatusEntry = _LpDS1DspRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 4, 1, 1)
)
lpDS1DspRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1DspIndex"),
)
if mibBuilder.loadTexts:
    lpDS1DspRowStatusEntry.setStatus("mandatory")
_LpDS1DspRowStatus_Type = RowStatus
_LpDS1DspRowStatus_Object = MibTableColumn
lpDS1DspRowStatus = _LpDS1DspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 4, 1, 1, 1),
    _LpDS1DspRowStatus_Type()
)
lpDS1DspRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1DspRowStatus.setStatus("mandatory")
_LpDS1DspComponentName_Type = DisplayString
_LpDS1DspComponentName_Object = MibTableColumn
lpDS1DspComponentName = _LpDS1DspComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 4, 1, 1, 2),
    _LpDS1DspComponentName_Type()
)
lpDS1DspComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1DspComponentName.setStatus("mandatory")
_LpDS1DspStorageType_Type = StorageType
_LpDS1DspStorageType_Object = MibTableColumn
lpDS1DspStorageType = _LpDS1DspStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 4, 1, 1, 4),
    _LpDS1DspStorageType_Type()
)
lpDS1DspStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1DspStorageType.setStatus("mandatory")
_LpDS1DspIndex_Type = NonReplicated
_LpDS1DspIndex_Object = MibTableColumn
lpDS1DspIndex = _LpDS1DspIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 4, 1, 1, 10),
    _LpDS1DspIndex_Type()
)
lpDS1DspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1DspIndex.setStatus("mandatory")
_LpDS1Audio_ObjectIdentity = ObjectIdentity
lpDS1Audio = _LpDS1Audio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 5)
)
_LpDS1AudioRowStatusTable_Object = MibTable
lpDS1AudioRowStatusTable = _LpDS1AudioRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 5, 1)
)
if mibBuilder.loadTexts:
    lpDS1AudioRowStatusTable.setStatus("mandatory")
_LpDS1AudioRowStatusEntry_Object = MibTableRow
lpDS1AudioRowStatusEntry = _LpDS1AudioRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 5, 1, 1)
)
lpDS1AudioRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1AudioIndex"),
)
if mibBuilder.loadTexts:
    lpDS1AudioRowStatusEntry.setStatus("mandatory")
_LpDS1AudioRowStatus_Type = RowStatus
_LpDS1AudioRowStatus_Object = MibTableColumn
lpDS1AudioRowStatus = _LpDS1AudioRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 5, 1, 1, 1),
    _LpDS1AudioRowStatus_Type()
)
lpDS1AudioRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1AudioRowStatus.setStatus("mandatory")
_LpDS1AudioComponentName_Type = DisplayString
_LpDS1AudioComponentName_Object = MibTableColumn
lpDS1AudioComponentName = _LpDS1AudioComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 5, 1, 1, 2),
    _LpDS1AudioComponentName_Type()
)
lpDS1AudioComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1AudioComponentName.setStatus("mandatory")
_LpDS1AudioStorageType_Type = StorageType
_LpDS1AudioStorageType_Object = MibTableColumn
lpDS1AudioStorageType = _LpDS1AudioStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 5, 1, 1, 4),
    _LpDS1AudioStorageType_Type()
)
lpDS1AudioStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1AudioStorageType.setStatus("mandatory")
_LpDS1AudioIndex_Type = NonReplicated
_LpDS1AudioIndex_Object = MibTableColumn
lpDS1AudioIndex = _LpDS1AudioIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 5, 1, 1, 10),
    _LpDS1AudioIndex_Type()
)
lpDS1AudioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpDS1AudioIndex.setStatus("mandatory")
_LpDS1ProvTable_Object = MibTable
lpDS1ProvTable = _LpDS1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 10)
)
if mibBuilder.loadTexts:
    lpDS1ProvTable.setStatus("mandatory")
_LpDS1ProvEntry_Object = MibTableRow
lpDS1ProvEntry = _LpDS1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 10, 1)
)
lpDS1ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1ProvEntry.setStatus("mandatory")


class _LpDS1LineType_Type(Integer32):
    """Custom type lpDS1LineType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("d4", 0),
          ("d4Cas", 4),
          ("esf", 1),
          ("esfCas", 5),
          ("unframed", 6))
    )


_LpDS1LineType_Type.__name__ = "Integer32"
_LpDS1LineType_Object = MibTableColumn
lpDS1LineType = _LpDS1LineType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 10, 1, 1),
    _LpDS1LineType_Type()
)
lpDS1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1LineType.setStatus("mandatory")


class _LpDS1ZeroCoding_Type(Integer32):
    """Custom type lpDS1ZeroCoding based on Integer32"""
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
        *(("ami", 2),
          ("b8zs", 1),
          ("bit7Stuffing", 0))
    )


_LpDS1ZeroCoding_Type.__name__ = "Integer32"
_LpDS1ZeroCoding_Object = MibTableColumn
lpDS1ZeroCoding = _LpDS1ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 10, 1, 2),
    _LpDS1ZeroCoding_Type()
)
lpDS1ZeroCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ZeroCoding.setStatus("mandatory")


class _LpDS1ClockingSource_Type(Integer32):
    """Custom type lpDS1ClockingSource based on Integer32"""
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
        *(("line", 1),
          ("local", 0),
          ("module", 2),
          ("otherPort", 3),
          ("srtsMode", 4))
    )


_LpDS1ClockingSource_Type.__name__ = "Integer32"
_LpDS1ClockingSource_Object = MibTableColumn
lpDS1ClockingSource = _LpDS1ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 10, 1, 3),
    _LpDS1ClockingSource_Type()
)
lpDS1ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1ClockingSource.setStatus("mandatory")


class _LpDS1RaiAlarmType_Type(Integer32):
    """Custom type lpDS1RaiAlarmType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bit2", 1),
          ("fdl", 2),
          ("sBit", 0))
    )


_LpDS1RaiAlarmType_Type.__name__ = "Integer32"
_LpDS1RaiAlarmType_Object = MibTableColumn
lpDS1RaiAlarmType = _LpDS1RaiAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 10, 1, 4),
    _LpDS1RaiAlarmType_Type()
)
lpDS1RaiAlarmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1RaiAlarmType.setStatus("mandatory")


class _LpDS1LineLength_Type(Unsigned32):
    """Custom type lpDS1LineLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655),
    )


_LpDS1LineLength_Type.__name__ = "Unsigned32"
_LpDS1LineLength_Object = MibTableColumn
lpDS1LineLength = _LpDS1LineLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 10, 1, 5),
    _LpDS1LineLength_Type()
)
lpDS1LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1LineLength.setStatus("mandatory")
_LpDS1CidDataTable_Object = MibTable
lpDS1CidDataTable = _LpDS1CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 11)
)
if mibBuilder.loadTexts:
    lpDS1CidDataTable.setStatus("mandatory")
_LpDS1CidDataEntry_Object = MibTableRow
lpDS1CidDataEntry = _LpDS1CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 11, 1)
)
lpDS1CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1CidDataEntry.setStatus("mandatory")


class _LpDS1CustomerIdentifier_Type(Unsigned32):
    """Custom type lpDS1CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpDS1CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpDS1CustomerIdentifier_Object = MibTableColumn
lpDS1CustomerIdentifier = _LpDS1CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 11, 1, 1),
    _LpDS1CustomerIdentifier_Type()
)
lpDS1CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1CustomerIdentifier.setStatus("mandatory")
_LpDS1AdminInfoTable_Object = MibTable
lpDS1AdminInfoTable = _LpDS1AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 12)
)
if mibBuilder.loadTexts:
    lpDS1AdminInfoTable.setStatus("mandatory")
_LpDS1AdminInfoEntry_Object = MibTableRow
lpDS1AdminInfoEntry = _LpDS1AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 12, 1)
)
lpDS1AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1AdminInfoEntry.setStatus("mandatory")


class _LpDS1Vendor_Type(AsciiString):
    """Custom type lpDS1Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpDS1Vendor_Type.__name__ = "AsciiString"
_LpDS1Vendor_Object = MibTableColumn
lpDS1Vendor = _LpDS1Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 12, 1, 1),
    _LpDS1Vendor_Type()
)
lpDS1Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1Vendor.setStatus("mandatory")


class _LpDS1CommentText_Type(AsciiString):
    """Custom type lpDS1CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpDS1CommentText_Type.__name__ = "AsciiString"
_LpDS1CommentText_Object = MibTableColumn
lpDS1CommentText = _LpDS1CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 12, 1, 2),
    _LpDS1CommentText_Type()
)
lpDS1CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1CommentText.setStatus("mandatory")
_LpDS1IfEntryTable_Object = MibTable
lpDS1IfEntryTable = _LpDS1IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 13)
)
if mibBuilder.loadTexts:
    lpDS1IfEntryTable.setStatus("mandatory")
_LpDS1IfEntryEntry_Object = MibTableRow
lpDS1IfEntryEntry = _LpDS1IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 13, 1)
)
lpDS1IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1IfEntryEntry.setStatus("mandatory")


class _LpDS1IfAdminStatus_Type(Integer32):
    """Custom type lpDS1IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS1IfAdminStatus_Type.__name__ = "Integer32"
_LpDS1IfAdminStatus_Object = MibTableColumn
lpDS1IfAdminStatus = _LpDS1IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 13, 1, 1),
    _LpDS1IfAdminStatus_Type()
)
lpDS1IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpDS1IfAdminStatus.setStatus("mandatory")


class _LpDS1IfIndex_Type(InterfaceIndex):
    """Custom type lpDS1IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpDS1IfIndex_Type.__name__ = "InterfaceIndex"
_LpDS1IfIndex_Object = MibTableColumn
lpDS1IfIndex = _LpDS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 13, 1, 2),
    _LpDS1IfIndex_Type()
)
lpDS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1IfIndex.setStatus("mandatory")
_LpDS1OperStatusTable_Object = MibTable
lpDS1OperStatusTable = _LpDS1OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 14)
)
if mibBuilder.loadTexts:
    lpDS1OperStatusTable.setStatus("mandatory")
_LpDS1OperStatusEntry_Object = MibTableRow
lpDS1OperStatusEntry = _LpDS1OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 14, 1)
)
lpDS1OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1OperStatusEntry.setStatus("mandatory")


class _LpDS1SnmpOperStatus_Type(Integer32):
    """Custom type lpDS1SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpDS1SnmpOperStatus_Type.__name__ = "Integer32"
_LpDS1SnmpOperStatus_Object = MibTableColumn
lpDS1SnmpOperStatus = _LpDS1SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 14, 1, 1),
    _LpDS1SnmpOperStatus_Type()
)
lpDS1SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1SnmpOperStatus.setStatus("mandatory")
_LpDS1StateTable_Object = MibTable
lpDS1StateTable = _LpDS1StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15)
)
if mibBuilder.loadTexts:
    lpDS1StateTable.setStatus("mandatory")
_LpDS1StateEntry_Object = MibTableRow
lpDS1StateEntry = _LpDS1StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1)
)
lpDS1StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1StateEntry.setStatus("mandatory")


class _LpDS1AdminState_Type(Integer32):
    """Custom type lpDS1AdminState based on Integer32"""
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


_LpDS1AdminState_Type.__name__ = "Integer32"
_LpDS1AdminState_Object = MibTableColumn
lpDS1AdminState = _LpDS1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 1),
    _LpDS1AdminState_Type()
)
lpDS1AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1AdminState.setStatus("mandatory")


class _LpDS1OperationalState_Type(Integer32):
    """Custom type lpDS1OperationalState based on Integer32"""
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


_LpDS1OperationalState_Type.__name__ = "Integer32"
_LpDS1OperationalState_Object = MibTableColumn
lpDS1OperationalState = _LpDS1OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 2),
    _LpDS1OperationalState_Type()
)
lpDS1OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1OperationalState.setStatus("mandatory")


class _LpDS1UsageState_Type(Integer32):
    """Custom type lpDS1UsageState based on Integer32"""
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


_LpDS1UsageState_Type.__name__ = "Integer32"
_LpDS1UsageState_Object = MibTableColumn
lpDS1UsageState = _LpDS1UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 3),
    _LpDS1UsageState_Type()
)
lpDS1UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1UsageState.setStatus("mandatory")


class _LpDS1AvailabilityStatus_Type(OctetString):
    """Custom type lpDS1AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpDS1AvailabilityStatus_Type.__name__ = "OctetString"
_LpDS1AvailabilityStatus_Object = MibTableColumn
lpDS1AvailabilityStatus = _LpDS1AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 4),
    _LpDS1AvailabilityStatus_Type()
)
lpDS1AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1AvailabilityStatus.setStatus("mandatory")


class _LpDS1ProceduralStatus_Type(OctetString):
    """Custom type lpDS1ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS1ProceduralStatus_Type.__name__ = "OctetString"
_LpDS1ProceduralStatus_Object = MibTableColumn
lpDS1ProceduralStatus = _LpDS1ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 5),
    _LpDS1ProceduralStatus_Type()
)
lpDS1ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ProceduralStatus.setStatus("mandatory")


class _LpDS1ControlStatus_Type(OctetString):
    """Custom type lpDS1ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS1ControlStatus_Type.__name__ = "OctetString"
_LpDS1ControlStatus_Object = MibTableColumn
lpDS1ControlStatus = _LpDS1ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 6),
    _LpDS1ControlStatus_Type()
)
lpDS1ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ControlStatus.setStatus("mandatory")


class _LpDS1AlarmStatus_Type(OctetString):
    """Custom type lpDS1AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpDS1AlarmStatus_Type.__name__ = "OctetString"
_LpDS1AlarmStatus_Object = MibTableColumn
lpDS1AlarmStatus = _LpDS1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 7),
    _LpDS1AlarmStatus_Type()
)
lpDS1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1AlarmStatus.setStatus("mandatory")


class _LpDS1StandbyStatus_Type(Integer32):
    """Custom type lpDS1StandbyStatus based on Integer32"""
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


_LpDS1StandbyStatus_Type.__name__ = "Integer32"
_LpDS1StandbyStatus_Object = MibTableColumn
lpDS1StandbyStatus = _LpDS1StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 8),
    _LpDS1StandbyStatus_Type()
)
lpDS1StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1StandbyStatus.setStatus("mandatory")


class _LpDS1UnknownStatus_Type(Integer32):
    """Custom type lpDS1UnknownStatus based on Integer32"""
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


_LpDS1UnknownStatus_Type.__name__ = "Integer32"
_LpDS1UnknownStatus_Object = MibTableColumn
lpDS1UnknownStatus = _LpDS1UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 15, 1, 9),
    _LpDS1UnknownStatus_Type()
)
lpDS1UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1UnknownStatus.setStatus("mandatory")
_LpDS1OperTable_Object = MibTable
lpDS1OperTable = _LpDS1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16)
)
if mibBuilder.loadTexts:
    lpDS1OperTable.setStatus("mandatory")
_LpDS1OperEntry_Object = MibTableRow
lpDS1OperEntry = _LpDS1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16, 1)
)
lpDS1OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1OperEntry.setStatus("mandatory")


class _LpDS1LosAlarm_Type(Integer32):
    """Custom type lpDS1LosAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS1LosAlarm_Type.__name__ = "Integer32"
_LpDS1LosAlarm_Object = MibTableColumn
lpDS1LosAlarm = _LpDS1LosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16, 1, 1),
    _LpDS1LosAlarm_Type()
)
lpDS1LosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1LosAlarm.setStatus("mandatory")


class _LpDS1RxAisAlarm_Type(Integer32):
    """Custom type lpDS1RxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS1RxAisAlarm_Type.__name__ = "Integer32"
_LpDS1RxAisAlarm_Object = MibTableColumn
lpDS1RxAisAlarm = _LpDS1RxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16, 1, 2),
    _LpDS1RxAisAlarm_Type()
)
lpDS1RxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1RxAisAlarm.setStatus("mandatory")


class _LpDS1LofAlarm_Type(Integer32):
    """Custom type lpDS1LofAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS1LofAlarm_Type.__name__ = "Integer32"
_LpDS1LofAlarm_Object = MibTableColumn
lpDS1LofAlarm = _LpDS1LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16, 1, 3),
    _LpDS1LofAlarm_Type()
)
lpDS1LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1LofAlarm.setStatus("mandatory")


class _LpDS1RxRaiAlarm_Type(Integer32):
    """Custom type lpDS1RxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS1RxRaiAlarm_Type.__name__ = "Integer32"
_LpDS1RxRaiAlarm_Object = MibTableColumn
lpDS1RxRaiAlarm = _LpDS1RxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16, 1, 4),
    _LpDS1RxRaiAlarm_Type()
)
lpDS1RxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1RxRaiAlarm.setStatus("mandatory")


class _LpDS1TxAisAlarm_Type(Integer32):
    """Custom type lpDS1TxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS1TxAisAlarm_Type.__name__ = "Integer32"
_LpDS1TxAisAlarm_Object = MibTableColumn
lpDS1TxAisAlarm = _LpDS1TxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16, 1, 5),
    _LpDS1TxAisAlarm_Type()
)
lpDS1TxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TxAisAlarm.setStatus("mandatory")


class _LpDS1TxRaiAlarm_Type(Integer32):
    """Custom type lpDS1TxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpDS1TxRaiAlarm_Type.__name__ = "Integer32"
_LpDS1TxRaiAlarm_Object = MibTableColumn
lpDS1TxRaiAlarm = _LpDS1TxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 16, 1, 6),
    _LpDS1TxRaiAlarm_Type()
)
lpDS1TxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1TxRaiAlarm.setStatus("mandatory")
_LpDS1StatsTable_Object = MibTable
lpDS1StatsTable = _LpDS1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17)
)
if mibBuilder.loadTexts:
    lpDS1StatsTable.setStatus("mandatory")
_LpDS1StatsEntry_Object = MibTableRow
lpDS1StatsEntry = _LpDS1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1)
)
lpDS1StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpDS1Index"),
)
if mibBuilder.loadTexts:
    lpDS1StatsEntry.setStatus("mandatory")
_LpDS1RunningTime_Type = Counter32
_LpDS1RunningTime_Object = MibTableColumn
lpDS1RunningTime = _LpDS1RunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 1),
    _LpDS1RunningTime_Type()
)
lpDS1RunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1RunningTime.setStatus("mandatory")
_LpDS1ErrorFreeSec_Type = Counter32
_LpDS1ErrorFreeSec_Object = MibTableColumn
lpDS1ErrorFreeSec = _LpDS1ErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 2),
    _LpDS1ErrorFreeSec_Type()
)
lpDS1ErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ErrorFreeSec.setStatus("mandatory")
_LpDS1ErroredSec_Type = Counter32
_LpDS1ErroredSec_Object = MibTableColumn
lpDS1ErroredSec = _LpDS1ErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 3),
    _LpDS1ErroredSec_Type()
)
lpDS1ErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1ErroredSec.setStatus("mandatory")
_LpDS1SevErroredSec_Type = Counter32
_LpDS1SevErroredSec_Object = MibTableColumn
lpDS1SevErroredSec = _LpDS1SevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 4),
    _LpDS1SevErroredSec_Type()
)
lpDS1SevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1SevErroredSec.setStatus("mandatory")
_LpDS1SevErroredFrmSec_Type = Counter32
_LpDS1SevErroredFrmSec_Object = MibTableColumn
lpDS1SevErroredFrmSec = _LpDS1SevErroredFrmSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 5),
    _LpDS1SevErroredFrmSec_Type()
)
lpDS1SevErroredFrmSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1SevErroredFrmSec.setStatus("mandatory")
_LpDS1UnavailSec_Type = Counter32
_LpDS1UnavailSec_Object = MibTableColumn
lpDS1UnavailSec = _LpDS1UnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 6),
    _LpDS1UnavailSec_Type()
)
lpDS1UnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1UnavailSec.setStatus("mandatory")
_LpDS1BpvErrors_Type = Counter32
_LpDS1BpvErrors_Object = MibTableColumn
lpDS1BpvErrors = _LpDS1BpvErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 7),
    _LpDS1BpvErrors_Type()
)
lpDS1BpvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1BpvErrors.setStatus("mandatory")
_LpDS1CrcErrors_Type = Counter32
_LpDS1CrcErrors_Object = MibTableColumn
lpDS1CrcErrors = _LpDS1CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 8),
    _LpDS1CrcErrors_Type()
)
lpDS1CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1CrcErrors.setStatus("mandatory")
_LpDS1FrmErrors_Type = Counter32
_LpDS1FrmErrors_Object = MibTableColumn
lpDS1FrmErrors = _LpDS1FrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 9),
    _LpDS1FrmErrors_Type()
)
lpDS1FrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1FrmErrors.setStatus("mandatory")
_LpDS1LosStateChanges_Type = Counter32
_LpDS1LosStateChanges_Object = MibTableColumn
lpDS1LosStateChanges = _LpDS1LosStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 10),
    _LpDS1LosStateChanges_Type()
)
lpDS1LosStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1LosStateChanges.setStatus("mandatory")
_LpDS1SlipErrors_Type = Counter32
_LpDS1SlipErrors_Object = MibTableColumn
lpDS1SlipErrors = _LpDS1SlipErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 7, 17, 1, 11),
    _LpDS1SlipErrors_Type()
)
lpDS1SlipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpDS1SlipErrors.setStatus("mandatory")
_LpE1_ObjectIdentity = ObjectIdentity
lpE1 = _LpE1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8)
)
_LpE1RowStatusTable_Object = MibTable
lpE1RowStatusTable = _LpE1RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 1)
)
if mibBuilder.loadTexts:
    lpE1RowStatusTable.setStatus("mandatory")
_LpE1RowStatusEntry_Object = MibTableRow
lpE1RowStatusEntry = _LpE1RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 1, 1)
)
lpE1RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1RowStatusEntry.setStatus("mandatory")
_LpE1RowStatus_Type = RowStatus
_LpE1RowStatus_Object = MibTableColumn
lpE1RowStatus = _LpE1RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 1, 1, 1),
    _LpE1RowStatus_Type()
)
lpE1RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1RowStatus.setStatus("mandatory")
_LpE1ComponentName_Type = DisplayString
_LpE1ComponentName_Object = MibTableColumn
lpE1ComponentName = _LpE1ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 1, 1, 2),
    _LpE1ComponentName_Type()
)
lpE1ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ComponentName.setStatus("mandatory")
_LpE1StorageType_Type = StorageType
_LpE1StorageType_Object = MibTableColumn
lpE1StorageType = _LpE1StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 1, 1, 4),
    _LpE1StorageType_Type()
)
lpE1StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1StorageType.setStatus("mandatory")


class _LpE1Index_Type(Integer32):
    """Custom type lpE1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_LpE1Index_Type.__name__ = "Integer32"
_LpE1Index_Object = MibTableColumn
lpE1Index = _LpE1Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 1, 1, 10),
    _LpE1Index_Type()
)
lpE1Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1Index.setStatus("mandatory")
_LpE1Chan_ObjectIdentity = ObjectIdentity
lpE1Chan = _LpE1Chan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2)
)
_LpE1ChanRowStatusTable_Object = MibTable
lpE1ChanRowStatusTable = _LpE1ChanRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 1)
)
if mibBuilder.loadTexts:
    lpE1ChanRowStatusTable.setStatus("mandatory")
_LpE1ChanRowStatusEntry_Object = MibTableRow
lpE1ChanRowStatusEntry = _LpE1ChanRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 1, 1)
)
lpE1ChanRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanRowStatusEntry.setStatus("mandatory")
_LpE1ChanRowStatus_Type = RowStatus
_LpE1ChanRowStatus_Object = MibTableColumn
lpE1ChanRowStatus = _LpE1ChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 1, 1, 1),
    _LpE1ChanRowStatus_Type()
)
lpE1ChanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanRowStatus.setStatus("mandatory")
_LpE1ChanComponentName_Type = DisplayString
_LpE1ChanComponentName_Object = MibTableColumn
lpE1ChanComponentName = _LpE1ChanComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 1, 1, 2),
    _LpE1ChanComponentName_Type()
)
lpE1ChanComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanComponentName.setStatus("mandatory")
_LpE1ChanStorageType_Type = StorageType
_LpE1ChanStorageType_Object = MibTableColumn
lpE1ChanStorageType = _LpE1ChanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 1, 1, 4),
    _LpE1ChanStorageType_Type()
)
lpE1ChanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanStorageType.setStatus("mandatory")


class _LpE1ChanIndex_Type(Integer32):
    """Custom type lpE1ChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_LpE1ChanIndex_Type.__name__ = "Integer32"
_LpE1ChanIndex_Object = MibTableColumn
lpE1ChanIndex = _LpE1ChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 1, 1, 10),
    _LpE1ChanIndex_Type()
)
lpE1ChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1ChanIndex.setStatus("mandatory")
_LpE1ChanTest_ObjectIdentity = ObjectIdentity
lpE1ChanTest = _LpE1ChanTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2)
)
_LpE1ChanTestRowStatusTable_Object = MibTable
lpE1ChanTestRowStatusTable = _LpE1ChanTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpE1ChanTestRowStatusTable.setStatus("mandatory")
_LpE1ChanTestRowStatusEntry_Object = MibTableRow
lpE1ChanTestRowStatusEntry = _LpE1ChanTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 1, 1)
)
lpE1ChanTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTestRowStatusEntry.setStatus("mandatory")
_LpE1ChanTestRowStatus_Type = RowStatus
_LpE1ChanTestRowStatus_Object = MibTableColumn
lpE1ChanTestRowStatus = _LpE1ChanTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 1, 1, 1),
    _LpE1ChanTestRowStatus_Type()
)
lpE1ChanTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestRowStatus.setStatus("mandatory")
_LpE1ChanTestComponentName_Type = DisplayString
_LpE1ChanTestComponentName_Object = MibTableColumn
lpE1ChanTestComponentName = _LpE1ChanTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 1, 1, 2),
    _LpE1ChanTestComponentName_Type()
)
lpE1ChanTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestComponentName.setStatus("mandatory")
_LpE1ChanTestStorageType_Type = StorageType
_LpE1ChanTestStorageType_Object = MibTableColumn
lpE1ChanTestStorageType = _LpE1ChanTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 1, 1, 4),
    _LpE1ChanTestStorageType_Type()
)
lpE1ChanTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestStorageType.setStatus("mandatory")
_LpE1ChanTestIndex_Type = NonReplicated
_LpE1ChanTestIndex_Object = MibTableColumn
lpE1ChanTestIndex = _LpE1ChanTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 1, 1, 10),
    _LpE1ChanTestIndex_Type()
)
lpE1ChanTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1ChanTestIndex.setStatus("mandatory")
_LpE1ChanTestStateTable_Object = MibTable
lpE1ChanTestStateTable = _LpE1ChanTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpE1ChanTestStateTable.setStatus("mandatory")
_LpE1ChanTestStateEntry_Object = MibTableRow
lpE1ChanTestStateEntry = _LpE1ChanTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 10, 1)
)
lpE1ChanTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTestStateEntry.setStatus("mandatory")


class _LpE1ChanTestAdminState_Type(Integer32):
    """Custom type lpE1ChanTestAdminState based on Integer32"""
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


_LpE1ChanTestAdminState_Type.__name__ = "Integer32"
_LpE1ChanTestAdminState_Object = MibTableColumn
lpE1ChanTestAdminState = _LpE1ChanTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 10, 1, 1),
    _LpE1ChanTestAdminState_Type()
)
lpE1ChanTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestAdminState.setStatus("mandatory")


class _LpE1ChanTestOperationalState_Type(Integer32):
    """Custom type lpE1ChanTestOperationalState based on Integer32"""
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


_LpE1ChanTestOperationalState_Type.__name__ = "Integer32"
_LpE1ChanTestOperationalState_Object = MibTableColumn
lpE1ChanTestOperationalState = _LpE1ChanTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 10, 1, 2),
    _LpE1ChanTestOperationalState_Type()
)
lpE1ChanTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestOperationalState.setStatus("mandatory")


class _LpE1ChanTestUsageState_Type(Integer32):
    """Custom type lpE1ChanTestUsageState based on Integer32"""
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


_LpE1ChanTestUsageState_Type.__name__ = "Integer32"
_LpE1ChanTestUsageState_Object = MibTableColumn
lpE1ChanTestUsageState = _LpE1ChanTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 10, 1, 3),
    _LpE1ChanTestUsageState_Type()
)
lpE1ChanTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestUsageState.setStatus("mandatory")
_LpE1ChanTestSetupTable_Object = MibTable
lpE1ChanTestSetupTable = _LpE1ChanTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11)
)
if mibBuilder.loadTexts:
    lpE1ChanTestSetupTable.setStatus("mandatory")
_LpE1ChanTestSetupEntry_Object = MibTableRow
lpE1ChanTestSetupEntry = _LpE1ChanTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1)
)
lpE1ChanTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTestSetupEntry.setStatus("mandatory")


class _LpE1ChanTestPurpose_Type(AsciiString):
    """Custom type lpE1ChanTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpE1ChanTestPurpose_Type.__name__ = "AsciiString"
_LpE1ChanTestPurpose_Object = MibTableColumn
lpE1ChanTestPurpose = _LpE1ChanTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 1),
    _LpE1ChanTestPurpose_Type()
)
lpE1ChanTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestPurpose.setStatus("mandatory")


class _LpE1ChanTestType_Type(Integer32):
    """Custom type lpE1ChanTestType based on Integer32"""
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


_LpE1ChanTestType_Type.__name__ = "Integer32"
_LpE1ChanTestType_Object = MibTableColumn
lpE1ChanTestType = _LpE1ChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 2),
    _LpE1ChanTestType_Type()
)
lpE1ChanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestType.setStatus("mandatory")


class _LpE1ChanTestFrmSize_Type(Unsigned32):
    """Custom type lpE1ChanTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpE1ChanTestFrmSize_Type.__name__ = "Unsigned32"
_LpE1ChanTestFrmSize_Object = MibTableColumn
lpE1ChanTestFrmSize = _LpE1ChanTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 3),
    _LpE1ChanTestFrmSize_Type()
)
lpE1ChanTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestFrmSize.setStatus("mandatory")


class _LpE1ChanTestFrmPatternType_Type(Integer32):
    """Custom type lpE1ChanTestFrmPatternType based on Integer32"""
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


_LpE1ChanTestFrmPatternType_Type.__name__ = "Integer32"
_LpE1ChanTestFrmPatternType_Object = MibTableColumn
lpE1ChanTestFrmPatternType = _LpE1ChanTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 4),
    _LpE1ChanTestFrmPatternType_Type()
)
lpE1ChanTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestFrmPatternType.setStatus("mandatory")


class _LpE1ChanTestCustomizedPattern_Type(Hex):
    """Custom type lpE1ChanTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpE1ChanTestCustomizedPattern_Type.__name__ = "Hex"
_LpE1ChanTestCustomizedPattern_Object = MibTableColumn
lpE1ChanTestCustomizedPattern = _LpE1ChanTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 5),
    _LpE1ChanTestCustomizedPattern_Type()
)
lpE1ChanTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestCustomizedPattern.setStatus("mandatory")


class _LpE1ChanTestDataStartDelay_Type(Unsigned32):
    """Custom type lpE1ChanTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpE1ChanTestDataStartDelay_Type.__name__ = "Unsigned32"
_LpE1ChanTestDataStartDelay_Object = MibTableColumn
lpE1ChanTestDataStartDelay = _LpE1ChanTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 6),
    _LpE1ChanTestDataStartDelay_Type()
)
lpE1ChanTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestDataStartDelay.setStatus("mandatory")


class _LpE1ChanTestDisplayInterval_Type(Unsigned32):
    """Custom type lpE1ChanTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpE1ChanTestDisplayInterval_Type.__name__ = "Unsigned32"
_LpE1ChanTestDisplayInterval_Object = MibTableColumn
lpE1ChanTestDisplayInterval = _LpE1ChanTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 7),
    _LpE1ChanTestDisplayInterval_Type()
)
lpE1ChanTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestDisplayInterval.setStatus("mandatory")


class _LpE1ChanTestDuration_Type(Unsigned32):
    """Custom type lpE1ChanTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpE1ChanTestDuration_Type.__name__ = "Unsigned32"
_LpE1ChanTestDuration_Object = MibTableColumn
lpE1ChanTestDuration = _LpE1ChanTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 11, 1, 8),
    _LpE1ChanTestDuration_Type()
)
lpE1ChanTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTestDuration.setStatus("mandatory")
_LpE1ChanTestResultsTable_Object = MibTable
lpE1ChanTestResultsTable = _LpE1ChanTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12)
)
if mibBuilder.loadTexts:
    lpE1ChanTestResultsTable.setStatus("mandatory")
_LpE1ChanTestResultsEntry_Object = MibTableRow
lpE1ChanTestResultsEntry = _LpE1ChanTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1)
)
lpE1ChanTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTestIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTestResultsEntry.setStatus("mandatory")
_LpE1ChanTestElapsedTime_Type = Counter32
_LpE1ChanTestElapsedTime_Object = MibTableColumn
lpE1ChanTestElapsedTime = _LpE1ChanTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 1),
    _LpE1ChanTestElapsedTime_Type()
)
lpE1ChanTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestElapsedTime.setStatus("mandatory")


class _LpE1ChanTestTimeRemaining_Type(Unsigned32):
    """Custom type lpE1ChanTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpE1ChanTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpE1ChanTestTimeRemaining_Object = MibTableColumn
lpE1ChanTestTimeRemaining = _LpE1ChanTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 2),
    _LpE1ChanTestTimeRemaining_Type()
)
lpE1ChanTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestTimeRemaining.setStatus("mandatory")


class _LpE1ChanTestCauseOfTermination_Type(Integer32):
    """Custom type lpE1ChanTestCauseOfTermination based on Integer32"""
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


_LpE1ChanTestCauseOfTermination_Type.__name__ = "Integer32"
_LpE1ChanTestCauseOfTermination_Object = MibTableColumn
lpE1ChanTestCauseOfTermination = _LpE1ChanTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 3),
    _LpE1ChanTestCauseOfTermination_Type()
)
lpE1ChanTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestCauseOfTermination.setStatus("mandatory")
_LpE1ChanTestBitsTx_Type = PassportCounter64
_LpE1ChanTestBitsTx_Object = MibTableColumn
lpE1ChanTestBitsTx = _LpE1ChanTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 4),
    _LpE1ChanTestBitsTx_Type()
)
lpE1ChanTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestBitsTx.setStatus("mandatory")
_LpE1ChanTestBytesTx_Type = PassportCounter64
_LpE1ChanTestBytesTx_Object = MibTableColumn
lpE1ChanTestBytesTx = _LpE1ChanTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 5),
    _LpE1ChanTestBytesTx_Type()
)
lpE1ChanTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestBytesTx.setStatus("mandatory")
_LpE1ChanTestFrmTx_Type = PassportCounter64
_LpE1ChanTestFrmTx_Object = MibTableColumn
lpE1ChanTestFrmTx = _LpE1ChanTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 6),
    _LpE1ChanTestFrmTx_Type()
)
lpE1ChanTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestFrmTx.setStatus("mandatory")
_LpE1ChanTestBitsRx_Type = PassportCounter64
_LpE1ChanTestBitsRx_Object = MibTableColumn
lpE1ChanTestBitsRx = _LpE1ChanTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 7),
    _LpE1ChanTestBitsRx_Type()
)
lpE1ChanTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestBitsRx.setStatus("mandatory")
_LpE1ChanTestBytesRx_Type = PassportCounter64
_LpE1ChanTestBytesRx_Object = MibTableColumn
lpE1ChanTestBytesRx = _LpE1ChanTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 8),
    _LpE1ChanTestBytesRx_Type()
)
lpE1ChanTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestBytesRx.setStatus("mandatory")
_LpE1ChanTestFrmRx_Type = PassportCounter64
_LpE1ChanTestFrmRx_Object = MibTableColumn
lpE1ChanTestFrmRx = _LpE1ChanTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 9),
    _LpE1ChanTestFrmRx_Type()
)
lpE1ChanTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestFrmRx.setStatus("mandatory")
_LpE1ChanTestErroredFrmRx_Type = PassportCounter64
_LpE1ChanTestErroredFrmRx_Object = MibTableColumn
lpE1ChanTestErroredFrmRx = _LpE1ChanTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 10),
    _LpE1ChanTestErroredFrmRx_Type()
)
lpE1ChanTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestErroredFrmRx.setStatus("mandatory")


class _LpE1ChanTestBitErrorRate_Type(AsciiString):
    """Custom type lpE1ChanTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpE1ChanTestBitErrorRate_Type.__name__ = "AsciiString"
_LpE1ChanTestBitErrorRate_Object = MibTableColumn
lpE1ChanTestBitErrorRate = _LpE1ChanTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 2, 12, 1, 11),
    _LpE1ChanTestBitErrorRate_Type()
)
lpE1ChanTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTestBitErrorRate.setStatus("mandatory")
_LpE1ChanCell_ObjectIdentity = ObjectIdentity
lpE1ChanCell = _LpE1ChanCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3)
)
_LpE1ChanCellRowStatusTable_Object = MibTable
lpE1ChanCellRowStatusTable = _LpE1ChanCellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    lpE1ChanCellRowStatusTable.setStatus("mandatory")
_LpE1ChanCellRowStatusEntry_Object = MibTableRow
lpE1ChanCellRowStatusEntry = _LpE1ChanCellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 1, 1)
)
lpE1ChanCellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanCellRowStatusEntry.setStatus("mandatory")
_LpE1ChanCellRowStatus_Type = RowStatus
_LpE1ChanCellRowStatus_Object = MibTableColumn
lpE1ChanCellRowStatus = _LpE1ChanCellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 1, 1, 1),
    _LpE1ChanCellRowStatus_Type()
)
lpE1ChanCellRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanCellRowStatus.setStatus("mandatory")
_LpE1ChanCellComponentName_Type = DisplayString
_LpE1ChanCellComponentName_Object = MibTableColumn
lpE1ChanCellComponentName = _LpE1ChanCellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 1, 1, 2),
    _LpE1ChanCellComponentName_Type()
)
lpE1ChanCellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellComponentName.setStatus("mandatory")
_LpE1ChanCellStorageType_Type = StorageType
_LpE1ChanCellStorageType_Object = MibTableColumn
lpE1ChanCellStorageType = _LpE1ChanCellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 1, 1, 4),
    _LpE1ChanCellStorageType_Type()
)
lpE1ChanCellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellStorageType.setStatus("mandatory")
_LpE1ChanCellIndex_Type = NonReplicated
_LpE1ChanCellIndex_Object = MibTableColumn
lpE1ChanCellIndex = _LpE1ChanCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 1, 1, 10),
    _LpE1ChanCellIndex_Type()
)
lpE1ChanCellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1ChanCellIndex.setStatus("mandatory")
_LpE1ChanCellProvTable_Object = MibTable
lpE1ChanCellProvTable = _LpE1ChanCellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 10)
)
if mibBuilder.loadTexts:
    lpE1ChanCellProvTable.setStatus("mandatory")
_LpE1ChanCellProvEntry_Object = MibTableRow
lpE1ChanCellProvEntry = _LpE1ChanCellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 10, 1)
)
lpE1ChanCellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanCellProvEntry.setStatus("mandatory")


class _LpE1ChanCellAlarmActDelay_Type(Unsigned32):
    """Custom type lpE1ChanCellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpE1ChanCellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpE1ChanCellAlarmActDelay_Object = MibTableColumn
lpE1ChanCellAlarmActDelay = _LpE1ChanCellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 10, 1, 1),
    _LpE1ChanCellAlarmActDelay_Type()
)
lpE1ChanCellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanCellAlarmActDelay.setStatus("mandatory")


class _LpE1ChanCellScrambleCellPayload_Type(Integer32):
    """Custom type lpE1ChanCellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpE1ChanCellScrambleCellPayload_Type.__name__ = "Integer32"
_LpE1ChanCellScrambleCellPayload_Object = MibTableColumn
lpE1ChanCellScrambleCellPayload = _LpE1ChanCellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 10, 1, 2),
    _LpE1ChanCellScrambleCellPayload_Type()
)
lpE1ChanCellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanCellScrambleCellPayload.setStatus("mandatory")


class _LpE1ChanCellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpE1ChanCellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpE1ChanCellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpE1ChanCellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpE1ChanCellCorrectSingleBitHeaderErrors = _LpE1ChanCellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 10, 1, 3),
    _LpE1ChanCellCorrectSingleBitHeaderErrors_Type()
)
lpE1ChanCellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanCellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpE1ChanCellOperTable_Object = MibTable
lpE1ChanCellOperTable = _LpE1ChanCellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 11)
)
if mibBuilder.loadTexts:
    lpE1ChanCellOperTable.setStatus("mandatory")
_LpE1ChanCellOperEntry_Object = MibTableRow
lpE1ChanCellOperEntry = _LpE1ChanCellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 11, 1)
)
lpE1ChanCellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanCellOperEntry.setStatus("mandatory")


class _LpE1ChanCellLcdAlarm_Type(Integer32):
    """Custom type lpE1ChanCellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1ChanCellLcdAlarm_Type.__name__ = "Integer32"
_LpE1ChanCellLcdAlarm_Object = MibTableColumn
lpE1ChanCellLcdAlarm = _LpE1ChanCellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 11, 1, 1),
    _LpE1ChanCellLcdAlarm_Type()
)
lpE1ChanCellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellLcdAlarm.setStatus("mandatory")
_LpE1ChanCellStatsTable_Object = MibTable
lpE1ChanCellStatsTable = _LpE1ChanCellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 12)
)
if mibBuilder.loadTexts:
    lpE1ChanCellStatsTable.setStatus("mandatory")
_LpE1ChanCellStatsEntry_Object = MibTableRow
lpE1ChanCellStatsEntry = _LpE1ChanCellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 12, 1)
)
lpE1ChanCellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanCellIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanCellStatsEntry.setStatus("mandatory")
_LpE1ChanCellUncorrectableHecErrors_Type = Counter32
_LpE1ChanCellUncorrectableHecErrors_Object = MibTableColumn
lpE1ChanCellUncorrectableHecErrors = _LpE1ChanCellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 12, 1, 1),
    _LpE1ChanCellUncorrectableHecErrors_Type()
)
lpE1ChanCellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellUncorrectableHecErrors.setStatus("mandatory")
_LpE1ChanCellSevErroredSec_Type = Counter32
_LpE1ChanCellSevErroredSec_Object = MibTableColumn
lpE1ChanCellSevErroredSec = _LpE1ChanCellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 12, 1, 2),
    _LpE1ChanCellSevErroredSec_Type()
)
lpE1ChanCellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellSevErroredSec.setStatus("mandatory")


class _LpE1ChanCellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpE1ChanCellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpE1ChanCellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpE1ChanCellReceiveCellUtilization_Object = MibTableColumn
lpE1ChanCellReceiveCellUtilization = _LpE1ChanCellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 12, 1, 3),
    _LpE1ChanCellReceiveCellUtilization_Type()
)
lpE1ChanCellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellReceiveCellUtilization.setStatus("mandatory")


class _LpE1ChanCellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpE1ChanCellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpE1ChanCellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpE1ChanCellTransmitCellUtilization_Object = MibTableColumn
lpE1ChanCellTransmitCellUtilization = _LpE1ChanCellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 12, 1, 4),
    _LpE1ChanCellTransmitCellUtilization_Type()
)
lpE1ChanCellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellTransmitCellUtilization.setStatus("mandatory")
_LpE1ChanCellCorrectableHeaderErrors_Type = Counter32
_LpE1ChanCellCorrectableHeaderErrors_Object = MibTableColumn
lpE1ChanCellCorrectableHeaderErrors = _LpE1ChanCellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 3, 12, 1, 5),
    _LpE1ChanCellCorrectableHeaderErrors_Type()
)
lpE1ChanCellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanCellCorrectableHeaderErrors.setStatus("mandatory")
_LpE1ChanTc_ObjectIdentity = ObjectIdentity
lpE1ChanTc = _LpE1ChanTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4)
)
_LpE1ChanTcRowStatusTable_Object = MibTable
lpE1ChanTcRowStatusTable = _LpE1ChanTcRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lpE1ChanTcRowStatusTable.setStatus("mandatory")
_LpE1ChanTcRowStatusEntry_Object = MibTableRow
lpE1ChanTcRowStatusEntry = _LpE1ChanTcRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 1, 1)
)
lpE1ChanTcRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTcRowStatusEntry.setStatus("mandatory")
_LpE1ChanTcRowStatus_Type = RowStatus
_LpE1ChanTcRowStatus_Object = MibTableColumn
lpE1ChanTcRowStatus = _LpE1ChanTcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 1, 1, 1),
    _LpE1ChanTcRowStatus_Type()
)
lpE1ChanTcRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTcRowStatus.setStatus("mandatory")
_LpE1ChanTcComponentName_Type = DisplayString
_LpE1ChanTcComponentName_Object = MibTableColumn
lpE1ChanTcComponentName = _LpE1ChanTcComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 1, 1, 2),
    _LpE1ChanTcComponentName_Type()
)
lpE1ChanTcComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTcComponentName.setStatus("mandatory")
_LpE1ChanTcStorageType_Type = StorageType
_LpE1ChanTcStorageType_Object = MibTableColumn
lpE1ChanTcStorageType = _LpE1ChanTcStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 1, 1, 4),
    _LpE1ChanTcStorageType_Type()
)
lpE1ChanTcStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTcStorageType.setStatus("mandatory")
_LpE1ChanTcIndex_Type = NonReplicated
_LpE1ChanTcIndex_Object = MibTableColumn
lpE1ChanTcIndex = _LpE1ChanTcIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 1, 1, 10),
    _LpE1ChanTcIndex_Type()
)
lpE1ChanTcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1ChanTcIndex.setStatus("mandatory")
_LpE1ChanTcProvTable_Object = MibTable
lpE1ChanTcProvTable = _LpE1ChanTcProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 10)
)
if mibBuilder.loadTexts:
    lpE1ChanTcProvTable.setStatus("mandatory")
_LpE1ChanTcProvEntry_Object = MibTableRow
lpE1ChanTcProvEntry = _LpE1ChanTcProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 10, 1)
)
lpE1ChanTcProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTcProvEntry.setStatus("mandatory")


class _LpE1ChanTcReplacementData_Type(Hex):
    """Custom type lpE1ChanTcReplacementData based on Hex"""
    defaultValue = 255

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LpE1ChanTcReplacementData_Type.__name__ = "Hex"
_LpE1ChanTcReplacementData_Object = MibTableColumn
lpE1ChanTcReplacementData = _LpE1ChanTcReplacementData_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 10, 1, 1),
    _LpE1ChanTcReplacementData_Type()
)
lpE1ChanTcReplacementData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTcReplacementData.setStatus("mandatory")


class _LpE1ChanTcSignalOneDuration_Type(Unsigned32):
    """Custom type lpE1ChanTcSignalOneDuration based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_LpE1ChanTcSignalOneDuration_Type.__name__ = "Unsigned32"
_LpE1ChanTcSignalOneDuration_Object = MibTableColumn
lpE1ChanTcSignalOneDuration = _LpE1ChanTcSignalOneDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 10, 1, 2),
    _LpE1ChanTcSignalOneDuration_Type()
)
lpE1ChanTcSignalOneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTcSignalOneDuration.setStatus("mandatory")
_LpE1ChanTcOpTable_Object = MibTable
lpE1ChanTcOpTable = _LpE1ChanTcOpTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 11)
)
if mibBuilder.loadTexts:
    lpE1ChanTcOpTable.setStatus("mandatory")
_LpE1ChanTcOpEntry_Object = MibTableRow
lpE1ChanTcOpEntry = _LpE1ChanTcOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 11, 1)
)
lpE1ChanTcOpEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTcIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTcOpEntry.setStatus("mandatory")


class _LpE1ChanTcIngressConditioning_Type(Integer32):
    """Custom type lpE1ChanTcIngressConditioning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpE1ChanTcIngressConditioning_Type.__name__ = "Integer32"
_LpE1ChanTcIngressConditioning_Object = MibTableColumn
lpE1ChanTcIngressConditioning = _LpE1ChanTcIngressConditioning_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 11, 1, 1),
    _LpE1ChanTcIngressConditioning_Type()
)
lpE1ChanTcIngressConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTcIngressConditioning.setStatus("mandatory")


class _LpE1ChanTcEgressConditioning_Type(Integer32):
    """Custom type lpE1ChanTcEgressConditioning based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpE1ChanTcEgressConditioning_Type.__name__ = "Integer32"
_LpE1ChanTcEgressConditioning_Object = MibTableColumn
lpE1ChanTcEgressConditioning = _LpE1ChanTcEgressConditioning_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 11, 1, 2),
    _LpE1ChanTcEgressConditioning_Type()
)
lpE1ChanTcEgressConditioning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanTcEgressConditioning.setStatus("mandatory")
_LpE1ChanTcSigOneTable_Object = MibTable
lpE1ChanTcSigOneTable = _LpE1ChanTcSigOneTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 398)
)
if mibBuilder.loadTexts:
    lpE1ChanTcSigOneTable.setStatus("mandatory")
_LpE1ChanTcSigOneEntry_Object = MibTableRow
lpE1ChanTcSigOneEntry = _LpE1ChanTcSigOneEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 398, 1)
)
lpE1ChanTcSigOneEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTcIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTcSigOneIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTcSigOneEntry.setStatus("mandatory")


class _LpE1ChanTcSigOneIndex_Type(Integer32):
    """Custom type lpE1ChanTcSigOneIndex based on Integer32"""
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
        *(("a", 3),
          ("b", 2),
          ("c", 1),
          ("d", 0))
    )


_LpE1ChanTcSigOneIndex_Type.__name__ = "Integer32"
_LpE1ChanTcSigOneIndex_Object = MibTableColumn
lpE1ChanTcSigOneIndex = _LpE1ChanTcSigOneIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 398, 1, 1),
    _LpE1ChanTcSigOneIndex_Type()
)
lpE1ChanTcSigOneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1ChanTcSigOneIndex.setStatus("mandatory")


class _LpE1ChanTcSigOneValue_Type(Unsigned32):
    """Custom type lpE1ChanTcSigOneValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpE1ChanTcSigOneValue_Type.__name__ = "Unsigned32"
_LpE1ChanTcSigOneValue_Object = MibTableColumn
lpE1ChanTcSigOneValue = _LpE1ChanTcSigOneValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 398, 1, 2),
    _LpE1ChanTcSigOneValue_Type()
)
lpE1ChanTcSigOneValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTcSigOneValue.setStatus("mandatory")
_LpE1ChanTcSigTwoTable_Object = MibTable
lpE1ChanTcSigTwoTable = _LpE1ChanTcSigTwoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 399)
)
if mibBuilder.loadTexts:
    lpE1ChanTcSigTwoTable.setStatus("mandatory")
_LpE1ChanTcSigTwoEntry_Object = MibTableRow
lpE1ChanTcSigTwoEntry = _LpE1ChanTcSigTwoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 399, 1)
)
lpE1ChanTcSigTwoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTcIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanTcSigTwoIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanTcSigTwoEntry.setStatus("mandatory")


class _LpE1ChanTcSigTwoIndex_Type(Integer32):
    """Custom type lpE1ChanTcSigTwoIndex based on Integer32"""
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
        *(("a", 3),
          ("b", 2),
          ("c", 1),
          ("d", 0))
    )


_LpE1ChanTcSigTwoIndex_Type.__name__ = "Integer32"
_LpE1ChanTcSigTwoIndex_Object = MibTableColumn
lpE1ChanTcSigTwoIndex = _LpE1ChanTcSigTwoIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 399, 1, 1),
    _LpE1ChanTcSigTwoIndex_Type()
)
lpE1ChanTcSigTwoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1ChanTcSigTwoIndex.setStatus("mandatory")


class _LpE1ChanTcSigTwoValue_Type(Unsigned32):
    """Custom type lpE1ChanTcSigTwoValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpE1ChanTcSigTwoValue_Type.__name__ = "Unsigned32"
_LpE1ChanTcSigTwoValue_Object = MibTableColumn
lpE1ChanTcSigTwoValue = _LpE1ChanTcSigTwoValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 4, 399, 1, 2),
    _LpE1ChanTcSigTwoValue_Type()
)
lpE1ChanTcSigTwoValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTcSigTwoValue.setStatus("mandatory")
_LpE1ChanProvTable_Object = MibTable
lpE1ChanProvTable = _LpE1ChanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 10)
)
if mibBuilder.loadTexts:
    lpE1ChanProvTable.setStatus("mandatory")
_LpE1ChanProvEntry_Object = MibTableRow
lpE1ChanProvEntry = _LpE1ChanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 10, 1)
)
lpE1ChanProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanProvEntry.setStatus("mandatory")


class _LpE1ChanTimeslots_Type(OctetString):
    """Custom type lpE1ChanTimeslots based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_LpE1ChanTimeslots_Type.__name__ = "OctetString"
_LpE1ChanTimeslots_Object = MibTableColumn
lpE1ChanTimeslots = _LpE1ChanTimeslots_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 10, 1, 1),
    _LpE1ChanTimeslots_Type()
)
lpE1ChanTimeslots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTimeslots.setStatus("mandatory")


class _LpE1ChanTimeslotDataRate_Type(Integer32):
    """Custom type lpE1ChanTimeslotDataRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("doNotOverride", 1),
          ("n56k", 0))
    )


_LpE1ChanTimeslotDataRate_Type.__name__ = "Integer32"
_LpE1ChanTimeslotDataRate_Object = MibTableColumn
lpE1ChanTimeslotDataRate = _LpE1ChanTimeslotDataRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 10, 1, 2),
    _LpE1ChanTimeslotDataRate_Type()
)
lpE1ChanTimeslotDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanTimeslotDataRate.setStatus("mandatory")
_LpE1ChanApplicationFramerName_Type = Link
_LpE1ChanApplicationFramerName_Object = MibTableColumn
lpE1ChanApplicationFramerName = _LpE1ChanApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 10, 1, 3),
    _LpE1ChanApplicationFramerName_Type()
)
lpE1ChanApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanApplicationFramerName.setStatus("mandatory")
_LpE1ChanCidDataTable_Object = MibTable
lpE1ChanCidDataTable = _LpE1ChanCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 11)
)
if mibBuilder.loadTexts:
    lpE1ChanCidDataTable.setStatus("mandatory")
_LpE1ChanCidDataEntry_Object = MibTableRow
lpE1ChanCidDataEntry = _LpE1ChanCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 11, 1)
)
lpE1ChanCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanCidDataEntry.setStatus("mandatory")


class _LpE1ChanCustomerIdentifier_Type(Unsigned32):
    """Custom type lpE1ChanCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpE1ChanCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpE1ChanCustomerIdentifier_Object = MibTableColumn
lpE1ChanCustomerIdentifier = _LpE1ChanCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 11, 1, 1),
    _LpE1ChanCustomerIdentifier_Type()
)
lpE1ChanCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanCustomerIdentifier.setStatus("mandatory")
_LpE1ChanIfEntryTable_Object = MibTable
lpE1ChanIfEntryTable = _LpE1ChanIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 12)
)
if mibBuilder.loadTexts:
    lpE1ChanIfEntryTable.setStatus("mandatory")
_LpE1ChanIfEntryEntry_Object = MibTableRow
lpE1ChanIfEntryEntry = _LpE1ChanIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 12, 1)
)
lpE1ChanIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanIfEntryEntry.setStatus("mandatory")


class _LpE1ChanIfAdminStatus_Type(Integer32):
    """Custom type lpE1ChanIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpE1ChanIfAdminStatus_Type.__name__ = "Integer32"
_LpE1ChanIfAdminStatus_Object = MibTableColumn
lpE1ChanIfAdminStatus = _LpE1ChanIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 12, 1, 1),
    _LpE1ChanIfAdminStatus_Type()
)
lpE1ChanIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanIfAdminStatus.setStatus("mandatory")


class _LpE1ChanIfIndex_Type(InterfaceIndex):
    """Custom type lpE1ChanIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpE1ChanIfIndex_Type.__name__ = "InterfaceIndex"
_LpE1ChanIfIndex_Object = MibTableColumn
lpE1ChanIfIndex = _LpE1ChanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 12, 1, 2),
    _LpE1ChanIfIndex_Type()
)
lpE1ChanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanIfIndex.setStatus("mandatory")
_LpE1ChanOperStatusTable_Object = MibTable
lpE1ChanOperStatusTable = _LpE1ChanOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 13)
)
if mibBuilder.loadTexts:
    lpE1ChanOperStatusTable.setStatus("mandatory")
_LpE1ChanOperStatusEntry_Object = MibTableRow
lpE1ChanOperStatusEntry = _LpE1ChanOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 13, 1)
)
lpE1ChanOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanOperStatusEntry.setStatus("mandatory")


class _LpE1ChanSnmpOperStatus_Type(Integer32):
    """Custom type lpE1ChanSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpE1ChanSnmpOperStatus_Type.__name__ = "Integer32"
_LpE1ChanSnmpOperStatus_Object = MibTableColumn
lpE1ChanSnmpOperStatus = _LpE1ChanSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 13, 1, 1),
    _LpE1ChanSnmpOperStatus_Type()
)
lpE1ChanSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanSnmpOperStatus.setStatus("mandatory")
_LpE1ChanStateTable_Object = MibTable
lpE1ChanStateTable = _LpE1ChanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14)
)
if mibBuilder.loadTexts:
    lpE1ChanStateTable.setStatus("mandatory")
_LpE1ChanStateEntry_Object = MibTableRow
lpE1ChanStateEntry = _LpE1ChanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1)
)
lpE1ChanStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanStateEntry.setStatus("mandatory")


class _LpE1ChanAdminState_Type(Integer32):
    """Custom type lpE1ChanAdminState based on Integer32"""
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


_LpE1ChanAdminState_Type.__name__ = "Integer32"
_LpE1ChanAdminState_Object = MibTableColumn
lpE1ChanAdminState = _LpE1ChanAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 1),
    _LpE1ChanAdminState_Type()
)
lpE1ChanAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanAdminState.setStatus("mandatory")


class _LpE1ChanOperationalState_Type(Integer32):
    """Custom type lpE1ChanOperationalState based on Integer32"""
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


_LpE1ChanOperationalState_Type.__name__ = "Integer32"
_LpE1ChanOperationalState_Object = MibTableColumn
lpE1ChanOperationalState = _LpE1ChanOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 2),
    _LpE1ChanOperationalState_Type()
)
lpE1ChanOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanOperationalState.setStatus("mandatory")


class _LpE1ChanUsageState_Type(Integer32):
    """Custom type lpE1ChanUsageState based on Integer32"""
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


_LpE1ChanUsageState_Type.__name__ = "Integer32"
_LpE1ChanUsageState_Object = MibTableColumn
lpE1ChanUsageState = _LpE1ChanUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 3),
    _LpE1ChanUsageState_Type()
)
lpE1ChanUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanUsageState.setStatus("mandatory")


class _LpE1ChanAvailabilityStatus_Type(OctetString):
    """Custom type lpE1ChanAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpE1ChanAvailabilityStatus_Type.__name__ = "OctetString"
_LpE1ChanAvailabilityStatus_Object = MibTableColumn
lpE1ChanAvailabilityStatus = _LpE1ChanAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 4),
    _LpE1ChanAvailabilityStatus_Type()
)
lpE1ChanAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanAvailabilityStatus.setStatus("mandatory")


class _LpE1ChanProceduralStatus_Type(OctetString):
    """Custom type lpE1ChanProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE1ChanProceduralStatus_Type.__name__ = "OctetString"
_LpE1ChanProceduralStatus_Object = MibTableColumn
lpE1ChanProceduralStatus = _LpE1ChanProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 5),
    _LpE1ChanProceduralStatus_Type()
)
lpE1ChanProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanProceduralStatus.setStatus("mandatory")


class _LpE1ChanControlStatus_Type(OctetString):
    """Custom type lpE1ChanControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE1ChanControlStatus_Type.__name__ = "OctetString"
_LpE1ChanControlStatus_Object = MibTableColumn
lpE1ChanControlStatus = _LpE1ChanControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 6),
    _LpE1ChanControlStatus_Type()
)
lpE1ChanControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanControlStatus.setStatus("mandatory")


class _LpE1ChanAlarmStatus_Type(OctetString):
    """Custom type lpE1ChanAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE1ChanAlarmStatus_Type.__name__ = "OctetString"
_LpE1ChanAlarmStatus_Object = MibTableColumn
lpE1ChanAlarmStatus = _LpE1ChanAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 7),
    _LpE1ChanAlarmStatus_Type()
)
lpE1ChanAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanAlarmStatus.setStatus("mandatory")


class _LpE1ChanStandbyStatus_Type(Integer32):
    """Custom type lpE1ChanStandbyStatus based on Integer32"""
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


_LpE1ChanStandbyStatus_Type.__name__ = "Integer32"
_LpE1ChanStandbyStatus_Object = MibTableColumn
lpE1ChanStandbyStatus = _LpE1ChanStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 8),
    _LpE1ChanStandbyStatus_Type()
)
lpE1ChanStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanStandbyStatus.setStatus("mandatory")


class _LpE1ChanUnknownStatus_Type(Integer32):
    """Custom type lpE1ChanUnknownStatus based on Integer32"""
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


_LpE1ChanUnknownStatus_Type.__name__ = "Integer32"
_LpE1ChanUnknownStatus_Object = MibTableColumn
lpE1ChanUnknownStatus = _LpE1ChanUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 14, 1, 9),
    _LpE1ChanUnknownStatus_Type()
)
lpE1ChanUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanUnknownStatus.setStatus("mandatory")
_LpE1ChanOperTable_Object = MibTable
lpE1ChanOperTable = _LpE1ChanOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 15)
)
if mibBuilder.loadTexts:
    lpE1ChanOperTable.setStatus("mandatory")
_LpE1ChanOperEntry_Object = MibTableRow
lpE1ChanOperEntry = _LpE1ChanOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 15, 1)
)
lpE1ChanOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanOperEntry.setStatus("mandatory")


class _LpE1ChanActualChannelSpeed_Type(Gauge32):
    """Custom type lpE1ChanActualChannelSpeed based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpE1ChanActualChannelSpeed_Type.__name__ = "Gauge32"
_LpE1ChanActualChannelSpeed_Object = MibTableColumn
lpE1ChanActualChannelSpeed = _LpE1ChanActualChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 15, 1, 1),
    _LpE1ChanActualChannelSpeed_Type()
)
lpE1ChanActualChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ChanActualChannelSpeed.setStatus("mandatory")
_LpE1ChanAdminInfoTable_Object = MibTable
lpE1ChanAdminInfoTable = _LpE1ChanAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 16)
)
if mibBuilder.loadTexts:
    lpE1ChanAdminInfoTable.setStatus("mandatory")
_LpE1ChanAdminInfoEntry_Object = MibTableRow
lpE1ChanAdminInfoEntry = _LpE1ChanAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 16, 1)
)
lpE1ChanAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1ChanIndex"),
)
if mibBuilder.loadTexts:
    lpE1ChanAdminInfoEntry.setStatus("mandatory")


class _LpE1ChanVendor_Type(AsciiString):
    """Custom type lpE1ChanVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpE1ChanVendor_Type.__name__ = "AsciiString"
_LpE1ChanVendor_Object = MibTableColumn
lpE1ChanVendor = _LpE1ChanVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 16, 1, 1),
    _LpE1ChanVendor_Type()
)
lpE1ChanVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanVendor.setStatus("mandatory")


class _LpE1ChanCommentText_Type(AsciiString):
    """Custom type lpE1ChanCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpE1ChanCommentText_Type.__name__ = "AsciiString"
_LpE1ChanCommentText_Object = MibTableColumn
lpE1ChanCommentText = _LpE1ChanCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 2, 16, 1, 2),
    _LpE1ChanCommentText_Type()
)
lpE1ChanCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ChanCommentText.setStatus("mandatory")
_LpE1Test_ObjectIdentity = ObjectIdentity
lpE1Test = _LpE1Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3)
)
_LpE1TestRowStatusTable_Object = MibTable
lpE1TestRowStatusTable = _LpE1TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 1)
)
if mibBuilder.loadTexts:
    lpE1TestRowStatusTable.setStatus("mandatory")
_LpE1TestRowStatusEntry_Object = MibTableRow
lpE1TestRowStatusEntry = _LpE1TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 1, 1)
)
lpE1TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1TestIndex"),
)
if mibBuilder.loadTexts:
    lpE1TestRowStatusEntry.setStatus("mandatory")
_LpE1TestRowStatus_Type = RowStatus
_LpE1TestRowStatus_Object = MibTableColumn
lpE1TestRowStatus = _LpE1TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 1, 1, 1),
    _LpE1TestRowStatus_Type()
)
lpE1TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestRowStatus.setStatus("mandatory")
_LpE1TestComponentName_Type = DisplayString
_LpE1TestComponentName_Object = MibTableColumn
lpE1TestComponentName = _LpE1TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 1, 1, 2),
    _LpE1TestComponentName_Type()
)
lpE1TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestComponentName.setStatus("mandatory")
_LpE1TestStorageType_Type = StorageType
_LpE1TestStorageType_Object = MibTableColumn
lpE1TestStorageType = _LpE1TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 1, 1, 4),
    _LpE1TestStorageType_Type()
)
lpE1TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestStorageType.setStatus("mandatory")
_LpE1TestIndex_Type = NonReplicated
_LpE1TestIndex_Object = MibTableColumn
lpE1TestIndex = _LpE1TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 1, 1, 10),
    _LpE1TestIndex_Type()
)
lpE1TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1TestIndex.setStatus("mandatory")
_LpE1TestStateTable_Object = MibTable
lpE1TestStateTable = _LpE1TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 10)
)
if mibBuilder.loadTexts:
    lpE1TestStateTable.setStatus("mandatory")
_LpE1TestStateEntry_Object = MibTableRow
lpE1TestStateEntry = _LpE1TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 10, 1)
)
lpE1TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1TestIndex"),
)
if mibBuilder.loadTexts:
    lpE1TestStateEntry.setStatus("mandatory")


class _LpE1TestAdminState_Type(Integer32):
    """Custom type lpE1TestAdminState based on Integer32"""
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


_LpE1TestAdminState_Type.__name__ = "Integer32"
_LpE1TestAdminState_Object = MibTableColumn
lpE1TestAdminState = _LpE1TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 10, 1, 1),
    _LpE1TestAdminState_Type()
)
lpE1TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestAdminState.setStatus("mandatory")


class _LpE1TestOperationalState_Type(Integer32):
    """Custom type lpE1TestOperationalState based on Integer32"""
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


_LpE1TestOperationalState_Type.__name__ = "Integer32"
_LpE1TestOperationalState_Object = MibTableColumn
lpE1TestOperationalState = _LpE1TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 10, 1, 2),
    _LpE1TestOperationalState_Type()
)
lpE1TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestOperationalState.setStatus("mandatory")


class _LpE1TestUsageState_Type(Integer32):
    """Custom type lpE1TestUsageState based on Integer32"""
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


_LpE1TestUsageState_Type.__name__ = "Integer32"
_LpE1TestUsageState_Object = MibTableColumn
lpE1TestUsageState = _LpE1TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 10, 1, 3),
    _LpE1TestUsageState_Type()
)
lpE1TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestUsageState.setStatus("mandatory")
_LpE1TestSetupTable_Object = MibTable
lpE1TestSetupTable = _LpE1TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11)
)
if mibBuilder.loadTexts:
    lpE1TestSetupTable.setStatus("mandatory")
_LpE1TestSetupEntry_Object = MibTableRow
lpE1TestSetupEntry = _LpE1TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1)
)
lpE1TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1TestIndex"),
)
if mibBuilder.loadTexts:
    lpE1TestSetupEntry.setStatus("mandatory")


class _LpE1TestPurpose_Type(AsciiString):
    """Custom type lpE1TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpE1TestPurpose_Type.__name__ = "AsciiString"
_LpE1TestPurpose_Object = MibTableColumn
lpE1TestPurpose = _LpE1TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 1),
    _LpE1TestPurpose_Type()
)
lpE1TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestPurpose.setStatus("mandatory")


class _LpE1TestType_Type(Integer32):
    """Custom type lpE1TestType based on Integer32"""
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


_LpE1TestType_Type.__name__ = "Integer32"
_LpE1TestType_Object = MibTableColumn
lpE1TestType = _LpE1TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 2),
    _LpE1TestType_Type()
)
lpE1TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestType.setStatus("mandatory")


class _LpE1TestFrmSize_Type(Unsigned32):
    """Custom type lpE1TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpE1TestFrmSize_Type.__name__ = "Unsigned32"
_LpE1TestFrmSize_Object = MibTableColumn
lpE1TestFrmSize = _LpE1TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 3),
    _LpE1TestFrmSize_Type()
)
lpE1TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestFrmSize.setStatus("mandatory")


class _LpE1TestFrmPatternType_Type(Integer32):
    """Custom type lpE1TestFrmPatternType based on Integer32"""
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


_LpE1TestFrmPatternType_Type.__name__ = "Integer32"
_LpE1TestFrmPatternType_Object = MibTableColumn
lpE1TestFrmPatternType = _LpE1TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 4),
    _LpE1TestFrmPatternType_Type()
)
lpE1TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestFrmPatternType.setStatus("mandatory")


class _LpE1TestCustomizedPattern_Type(Hex):
    """Custom type lpE1TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpE1TestCustomizedPattern_Type.__name__ = "Hex"
_LpE1TestCustomizedPattern_Object = MibTableColumn
lpE1TestCustomizedPattern = _LpE1TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 5),
    _LpE1TestCustomizedPattern_Type()
)
lpE1TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestCustomizedPattern.setStatus("mandatory")


class _LpE1TestDataStartDelay_Type(Unsigned32):
    """Custom type lpE1TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpE1TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpE1TestDataStartDelay_Object = MibTableColumn
lpE1TestDataStartDelay = _LpE1TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 6),
    _LpE1TestDataStartDelay_Type()
)
lpE1TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestDataStartDelay.setStatus("mandatory")


class _LpE1TestDisplayInterval_Type(Unsigned32):
    """Custom type lpE1TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpE1TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpE1TestDisplayInterval_Object = MibTableColumn
lpE1TestDisplayInterval = _LpE1TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 7),
    _LpE1TestDisplayInterval_Type()
)
lpE1TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestDisplayInterval.setStatus("mandatory")


class _LpE1TestDuration_Type(Unsigned32):
    """Custom type lpE1TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpE1TestDuration_Type.__name__ = "Unsigned32"
_LpE1TestDuration_Object = MibTableColumn
lpE1TestDuration = _LpE1TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 11, 1, 8),
    _LpE1TestDuration_Type()
)
lpE1TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1TestDuration.setStatus("mandatory")
_LpE1TestResultsTable_Object = MibTable
lpE1TestResultsTable = _LpE1TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12)
)
if mibBuilder.loadTexts:
    lpE1TestResultsTable.setStatus("mandatory")
_LpE1TestResultsEntry_Object = MibTableRow
lpE1TestResultsEntry = _LpE1TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1)
)
lpE1TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1TestIndex"),
)
if mibBuilder.loadTexts:
    lpE1TestResultsEntry.setStatus("mandatory")
_LpE1TestElapsedTime_Type = Counter32
_LpE1TestElapsedTime_Object = MibTableColumn
lpE1TestElapsedTime = _LpE1TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 1),
    _LpE1TestElapsedTime_Type()
)
lpE1TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestElapsedTime.setStatus("mandatory")


class _LpE1TestTimeRemaining_Type(Unsigned32):
    """Custom type lpE1TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpE1TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpE1TestTimeRemaining_Object = MibTableColumn
lpE1TestTimeRemaining = _LpE1TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 2),
    _LpE1TestTimeRemaining_Type()
)
lpE1TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestTimeRemaining.setStatus("mandatory")


class _LpE1TestCauseOfTermination_Type(Integer32):
    """Custom type lpE1TestCauseOfTermination based on Integer32"""
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


_LpE1TestCauseOfTermination_Type.__name__ = "Integer32"
_LpE1TestCauseOfTermination_Object = MibTableColumn
lpE1TestCauseOfTermination = _LpE1TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 3),
    _LpE1TestCauseOfTermination_Type()
)
lpE1TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestCauseOfTermination.setStatus("mandatory")
_LpE1TestBitsTx_Type = PassportCounter64
_LpE1TestBitsTx_Object = MibTableColumn
lpE1TestBitsTx = _LpE1TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 4),
    _LpE1TestBitsTx_Type()
)
lpE1TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestBitsTx.setStatus("mandatory")
_LpE1TestBytesTx_Type = PassportCounter64
_LpE1TestBytesTx_Object = MibTableColumn
lpE1TestBytesTx = _LpE1TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 5),
    _LpE1TestBytesTx_Type()
)
lpE1TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestBytesTx.setStatus("mandatory")
_LpE1TestFrmTx_Type = PassportCounter64
_LpE1TestFrmTx_Object = MibTableColumn
lpE1TestFrmTx = _LpE1TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 6),
    _LpE1TestFrmTx_Type()
)
lpE1TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestFrmTx.setStatus("mandatory")
_LpE1TestBitsRx_Type = PassportCounter64
_LpE1TestBitsRx_Object = MibTableColumn
lpE1TestBitsRx = _LpE1TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 7),
    _LpE1TestBitsRx_Type()
)
lpE1TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestBitsRx.setStatus("mandatory")
_LpE1TestBytesRx_Type = PassportCounter64
_LpE1TestBytesRx_Object = MibTableColumn
lpE1TestBytesRx = _LpE1TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 8),
    _LpE1TestBytesRx_Type()
)
lpE1TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestBytesRx.setStatus("mandatory")
_LpE1TestFrmRx_Type = PassportCounter64
_LpE1TestFrmRx_Object = MibTableColumn
lpE1TestFrmRx = _LpE1TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 9),
    _LpE1TestFrmRx_Type()
)
lpE1TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestFrmRx.setStatus("mandatory")
_LpE1TestErroredFrmRx_Type = PassportCounter64
_LpE1TestErroredFrmRx_Object = MibTableColumn
lpE1TestErroredFrmRx = _LpE1TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 10),
    _LpE1TestErroredFrmRx_Type()
)
lpE1TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestErroredFrmRx.setStatus("mandatory")


class _LpE1TestBitErrorRate_Type(AsciiString):
    """Custom type lpE1TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpE1TestBitErrorRate_Type.__name__ = "AsciiString"
_LpE1TestBitErrorRate_Object = MibTableColumn
lpE1TestBitErrorRate = _LpE1TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 3, 12, 1, 11),
    _LpE1TestBitErrorRate_Type()
)
lpE1TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TestBitErrorRate.setStatus("mandatory")
_LpE1Dsp_ObjectIdentity = ObjectIdentity
lpE1Dsp = _LpE1Dsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 4)
)
_LpE1DspRowStatusTable_Object = MibTable
lpE1DspRowStatusTable = _LpE1DspRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 4, 1)
)
if mibBuilder.loadTexts:
    lpE1DspRowStatusTable.setStatus("mandatory")
_LpE1DspRowStatusEntry_Object = MibTableRow
lpE1DspRowStatusEntry = _LpE1DspRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 4, 1, 1)
)
lpE1DspRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1DspIndex"),
)
if mibBuilder.loadTexts:
    lpE1DspRowStatusEntry.setStatus("mandatory")
_LpE1DspRowStatus_Type = RowStatus
_LpE1DspRowStatus_Object = MibTableColumn
lpE1DspRowStatus = _LpE1DspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 4, 1, 1, 1),
    _LpE1DspRowStatus_Type()
)
lpE1DspRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1DspRowStatus.setStatus("mandatory")
_LpE1DspComponentName_Type = DisplayString
_LpE1DspComponentName_Object = MibTableColumn
lpE1DspComponentName = _LpE1DspComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 4, 1, 1, 2),
    _LpE1DspComponentName_Type()
)
lpE1DspComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1DspComponentName.setStatus("mandatory")
_LpE1DspStorageType_Type = StorageType
_LpE1DspStorageType_Object = MibTableColumn
lpE1DspStorageType = _LpE1DspStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 4, 1, 1, 4),
    _LpE1DspStorageType_Type()
)
lpE1DspStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1DspStorageType.setStatus("mandatory")
_LpE1DspIndex_Type = NonReplicated
_LpE1DspIndex_Object = MibTableColumn
lpE1DspIndex = _LpE1DspIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 4, 1, 1, 10),
    _LpE1DspIndex_Type()
)
lpE1DspIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1DspIndex.setStatus("mandatory")
_LpE1Audio_ObjectIdentity = ObjectIdentity
lpE1Audio = _LpE1Audio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 5)
)
_LpE1AudioRowStatusTable_Object = MibTable
lpE1AudioRowStatusTable = _LpE1AudioRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 5, 1)
)
if mibBuilder.loadTexts:
    lpE1AudioRowStatusTable.setStatus("mandatory")
_LpE1AudioRowStatusEntry_Object = MibTableRow
lpE1AudioRowStatusEntry = _LpE1AudioRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 5, 1, 1)
)
lpE1AudioRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1AudioIndex"),
)
if mibBuilder.loadTexts:
    lpE1AudioRowStatusEntry.setStatus("mandatory")
_LpE1AudioRowStatus_Type = RowStatus
_LpE1AudioRowStatus_Object = MibTableColumn
lpE1AudioRowStatus = _LpE1AudioRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 5, 1, 1, 1),
    _LpE1AudioRowStatus_Type()
)
lpE1AudioRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1AudioRowStatus.setStatus("mandatory")
_LpE1AudioComponentName_Type = DisplayString
_LpE1AudioComponentName_Object = MibTableColumn
lpE1AudioComponentName = _LpE1AudioComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 5, 1, 1, 2),
    _LpE1AudioComponentName_Type()
)
lpE1AudioComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1AudioComponentName.setStatus("mandatory")
_LpE1AudioStorageType_Type = StorageType
_LpE1AudioStorageType_Object = MibTableColumn
lpE1AudioStorageType = _LpE1AudioStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 5, 1, 1, 4),
    _LpE1AudioStorageType_Type()
)
lpE1AudioStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1AudioStorageType.setStatus("mandatory")
_LpE1AudioIndex_Type = NonReplicated
_LpE1AudioIndex_Object = MibTableColumn
lpE1AudioIndex = _LpE1AudioIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 5, 1, 1, 10),
    _LpE1AudioIndex_Type()
)
lpE1AudioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpE1AudioIndex.setStatus("mandatory")
_LpE1ProvTable_Object = MibTable
lpE1ProvTable = _LpE1ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10)
)
if mibBuilder.loadTexts:
    lpE1ProvTable.setStatus("mandatory")
_LpE1ProvEntry_Object = MibTableRow
lpE1ProvEntry = _LpE1ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10, 1)
)
lpE1ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1ProvEntry.setStatus("mandatory")


class _LpE1LineType_Type(Integer32):
    """Custom type lpE1LineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cas", 3),
          ("ccs", 2),
          ("unframed", 6))
    )


_LpE1LineType_Type.__name__ = "Integer32"
_LpE1LineType_Object = MibTableColumn
lpE1LineType = _LpE1LineType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10, 1, 1),
    _LpE1LineType_Type()
)
lpE1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1LineType.setStatus("mandatory")


class _LpE1ClockingSource_Type(Integer32):
    """Custom type lpE1ClockingSource based on Integer32"""
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
        *(("line", 1),
          ("local", 0),
          ("module", 2),
          ("otherPort", 3),
          ("srtsMode", 4))
    )


_LpE1ClockingSource_Type.__name__ = "Integer32"
_LpE1ClockingSource_Object = MibTableColumn
lpE1ClockingSource = _LpE1ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10, 1, 2),
    _LpE1ClockingSource_Type()
)
lpE1ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1ClockingSource.setStatus("mandatory")


class _LpE1Crc4Mode_Type(Integer32):
    """Custom type lpE1Crc4Mode based on Integer32"""
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


_LpE1Crc4Mode_Type.__name__ = "Integer32"
_LpE1Crc4Mode_Object = MibTableColumn
lpE1Crc4Mode = _LpE1Crc4Mode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10, 1, 3),
    _LpE1Crc4Mode_Type()
)
lpE1Crc4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1Crc4Mode.setStatus("mandatory")


class _LpE1SendRaiOnAis_Type(Integer32):
    """Custom type lpE1SendRaiOnAis based on Integer32"""
    defaultValue = 1

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


_LpE1SendRaiOnAis_Type.__name__ = "Integer32"
_LpE1SendRaiOnAis_Object = MibTableColumn
lpE1SendRaiOnAis = _LpE1SendRaiOnAis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10, 1, 4),
    _LpE1SendRaiOnAis_Type()
)
lpE1SendRaiOnAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1SendRaiOnAis.setStatus("mandatory")


class _LpE1RaiDeclareAlarmTime_Type(Unsigned32):
    """Custom type lpE1RaiDeclareAlarmTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 20000),
    )


_LpE1RaiDeclareAlarmTime_Type.__name__ = "Unsigned32"
_LpE1RaiDeclareAlarmTime_Object = MibTableColumn
lpE1RaiDeclareAlarmTime = _LpE1RaiDeclareAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10, 1, 5),
    _LpE1RaiDeclareAlarmTime_Type()
)
lpE1RaiDeclareAlarmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1RaiDeclareAlarmTime.setStatus("mandatory")


class _LpE1RaiClearAlarmTime_Type(Unsigned32):
    """Custom type lpE1RaiClearAlarmTime based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 20000),
    )


_LpE1RaiClearAlarmTime_Type.__name__ = "Unsigned32"
_LpE1RaiClearAlarmTime_Object = MibTableColumn
lpE1RaiClearAlarmTime = _LpE1RaiClearAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 10, 1, 6),
    _LpE1RaiClearAlarmTime_Type()
)
lpE1RaiClearAlarmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1RaiClearAlarmTime.setStatus("mandatory")
_LpE1CidDataTable_Object = MibTable
lpE1CidDataTable = _LpE1CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 11)
)
if mibBuilder.loadTexts:
    lpE1CidDataTable.setStatus("mandatory")
_LpE1CidDataEntry_Object = MibTableRow
lpE1CidDataEntry = _LpE1CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 11, 1)
)
lpE1CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1CidDataEntry.setStatus("mandatory")


class _LpE1CustomerIdentifier_Type(Unsigned32):
    """Custom type lpE1CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpE1CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpE1CustomerIdentifier_Object = MibTableColumn
lpE1CustomerIdentifier = _LpE1CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 11, 1, 1),
    _LpE1CustomerIdentifier_Type()
)
lpE1CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1CustomerIdentifier.setStatus("mandatory")
_LpE1AdminInfoTable_Object = MibTable
lpE1AdminInfoTable = _LpE1AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 12)
)
if mibBuilder.loadTexts:
    lpE1AdminInfoTable.setStatus("mandatory")
_LpE1AdminInfoEntry_Object = MibTableRow
lpE1AdminInfoEntry = _LpE1AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 12, 1)
)
lpE1AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1AdminInfoEntry.setStatus("mandatory")


class _LpE1Vendor_Type(AsciiString):
    """Custom type lpE1Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpE1Vendor_Type.__name__ = "AsciiString"
_LpE1Vendor_Object = MibTableColumn
lpE1Vendor = _LpE1Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 12, 1, 1),
    _LpE1Vendor_Type()
)
lpE1Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1Vendor.setStatus("mandatory")


class _LpE1CommentText_Type(AsciiString):
    """Custom type lpE1CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpE1CommentText_Type.__name__ = "AsciiString"
_LpE1CommentText_Object = MibTableColumn
lpE1CommentText = _LpE1CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 12, 1, 2),
    _LpE1CommentText_Type()
)
lpE1CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1CommentText.setStatus("mandatory")
_LpE1IfEntryTable_Object = MibTable
lpE1IfEntryTable = _LpE1IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 13)
)
if mibBuilder.loadTexts:
    lpE1IfEntryTable.setStatus("mandatory")
_LpE1IfEntryEntry_Object = MibTableRow
lpE1IfEntryEntry = _LpE1IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 13, 1)
)
lpE1IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1IfEntryEntry.setStatus("mandatory")


class _LpE1IfAdminStatus_Type(Integer32):
    """Custom type lpE1IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpE1IfAdminStatus_Type.__name__ = "Integer32"
_LpE1IfAdminStatus_Object = MibTableColumn
lpE1IfAdminStatus = _LpE1IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 13, 1, 1),
    _LpE1IfAdminStatus_Type()
)
lpE1IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpE1IfAdminStatus.setStatus("mandatory")


class _LpE1IfIndex_Type(InterfaceIndex):
    """Custom type lpE1IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpE1IfIndex_Type.__name__ = "InterfaceIndex"
_LpE1IfIndex_Object = MibTableColumn
lpE1IfIndex = _LpE1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 13, 1, 2),
    _LpE1IfIndex_Type()
)
lpE1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1IfIndex.setStatus("mandatory")
_LpE1OperStatusTable_Object = MibTable
lpE1OperStatusTable = _LpE1OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 14)
)
if mibBuilder.loadTexts:
    lpE1OperStatusTable.setStatus("mandatory")
_LpE1OperStatusEntry_Object = MibTableRow
lpE1OperStatusEntry = _LpE1OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 14, 1)
)
lpE1OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1OperStatusEntry.setStatus("mandatory")


class _LpE1SnmpOperStatus_Type(Integer32):
    """Custom type lpE1SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpE1SnmpOperStatus_Type.__name__ = "Integer32"
_LpE1SnmpOperStatus_Object = MibTableColumn
lpE1SnmpOperStatus = _LpE1SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 14, 1, 1),
    _LpE1SnmpOperStatus_Type()
)
lpE1SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1SnmpOperStatus.setStatus("mandatory")
_LpE1StateTable_Object = MibTable
lpE1StateTable = _LpE1StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15)
)
if mibBuilder.loadTexts:
    lpE1StateTable.setStatus("mandatory")
_LpE1StateEntry_Object = MibTableRow
lpE1StateEntry = _LpE1StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1)
)
lpE1StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1StateEntry.setStatus("mandatory")


class _LpE1AdminState_Type(Integer32):
    """Custom type lpE1AdminState based on Integer32"""
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


_LpE1AdminState_Type.__name__ = "Integer32"
_LpE1AdminState_Object = MibTableColumn
lpE1AdminState = _LpE1AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 1),
    _LpE1AdminState_Type()
)
lpE1AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1AdminState.setStatus("mandatory")


class _LpE1OperationalState_Type(Integer32):
    """Custom type lpE1OperationalState based on Integer32"""
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


_LpE1OperationalState_Type.__name__ = "Integer32"
_LpE1OperationalState_Object = MibTableColumn
lpE1OperationalState = _LpE1OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 2),
    _LpE1OperationalState_Type()
)
lpE1OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1OperationalState.setStatus("mandatory")


class _LpE1UsageState_Type(Integer32):
    """Custom type lpE1UsageState based on Integer32"""
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


_LpE1UsageState_Type.__name__ = "Integer32"
_LpE1UsageState_Object = MibTableColumn
lpE1UsageState = _LpE1UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 3),
    _LpE1UsageState_Type()
)
lpE1UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1UsageState.setStatus("mandatory")


class _LpE1AvailabilityStatus_Type(OctetString):
    """Custom type lpE1AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpE1AvailabilityStatus_Type.__name__ = "OctetString"
_LpE1AvailabilityStatus_Object = MibTableColumn
lpE1AvailabilityStatus = _LpE1AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 4),
    _LpE1AvailabilityStatus_Type()
)
lpE1AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1AvailabilityStatus.setStatus("mandatory")


class _LpE1ProceduralStatus_Type(OctetString):
    """Custom type lpE1ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE1ProceduralStatus_Type.__name__ = "OctetString"
_LpE1ProceduralStatus_Object = MibTableColumn
lpE1ProceduralStatus = _LpE1ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 5),
    _LpE1ProceduralStatus_Type()
)
lpE1ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ProceduralStatus.setStatus("mandatory")


class _LpE1ControlStatus_Type(OctetString):
    """Custom type lpE1ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE1ControlStatus_Type.__name__ = "OctetString"
_LpE1ControlStatus_Object = MibTableColumn
lpE1ControlStatus = _LpE1ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 6),
    _LpE1ControlStatus_Type()
)
lpE1ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ControlStatus.setStatus("mandatory")


class _LpE1AlarmStatus_Type(OctetString):
    """Custom type lpE1AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpE1AlarmStatus_Type.__name__ = "OctetString"
_LpE1AlarmStatus_Object = MibTableColumn
lpE1AlarmStatus = _LpE1AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 7),
    _LpE1AlarmStatus_Type()
)
lpE1AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1AlarmStatus.setStatus("mandatory")


class _LpE1StandbyStatus_Type(Integer32):
    """Custom type lpE1StandbyStatus based on Integer32"""
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


_LpE1StandbyStatus_Type.__name__ = "Integer32"
_LpE1StandbyStatus_Object = MibTableColumn
lpE1StandbyStatus = _LpE1StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 8),
    _LpE1StandbyStatus_Type()
)
lpE1StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1StandbyStatus.setStatus("mandatory")


class _LpE1UnknownStatus_Type(Integer32):
    """Custom type lpE1UnknownStatus based on Integer32"""
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


_LpE1UnknownStatus_Type.__name__ = "Integer32"
_LpE1UnknownStatus_Object = MibTableColumn
lpE1UnknownStatus = _LpE1UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 15, 1, 9),
    _LpE1UnknownStatus_Type()
)
lpE1UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1UnknownStatus.setStatus("mandatory")
_LpE1OperTable_Object = MibTable
lpE1OperTable = _LpE1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16)
)
if mibBuilder.loadTexts:
    lpE1OperTable.setStatus("mandatory")
_LpE1OperEntry_Object = MibTableRow
lpE1OperEntry = _LpE1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16, 1)
)
lpE1OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1OperEntry.setStatus("mandatory")


class _LpE1LosAlarm_Type(Integer32):
    """Custom type lpE1LosAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1LosAlarm_Type.__name__ = "Integer32"
_LpE1LosAlarm_Object = MibTableColumn
lpE1LosAlarm = _LpE1LosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16, 1, 1),
    _LpE1LosAlarm_Type()
)
lpE1LosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1LosAlarm.setStatus("mandatory")


class _LpE1RxAisAlarm_Type(Integer32):
    """Custom type lpE1RxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1RxAisAlarm_Type.__name__ = "Integer32"
_LpE1RxAisAlarm_Object = MibTableColumn
lpE1RxAisAlarm = _LpE1RxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16, 1, 2),
    _LpE1RxAisAlarm_Type()
)
lpE1RxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1RxAisAlarm.setStatus("mandatory")


class _LpE1LofAlarm_Type(Integer32):
    """Custom type lpE1LofAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1LofAlarm_Type.__name__ = "Integer32"
_LpE1LofAlarm_Object = MibTableColumn
lpE1LofAlarm = _LpE1LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16, 1, 3),
    _LpE1LofAlarm_Type()
)
lpE1LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1LofAlarm.setStatus("mandatory")


class _LpE1RxRaiAlarm_Type(Integer32):
    """Custom type lpE1RxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1RxRaiAlarm_Type.__name__ = "Integer32"
_LpE1RxRaiAlarm_Object = MibTableColumn
lpE1RxRaiAlarm = _LpE1RxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16, 1, 4),
    _LpE1RxRaiAlarm_Type()
)
lpE1RxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1RxRaiAlarm.setStatus("mandatory")


class _LpE1TxAisAlarm_Type(Integer32):
    """Custom type lpE1TxAisAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1TxAisAlarm_Type.__name__ = "Integer32"
_LpE1TxAisAlarm_Object = MibTableColumn
lpE1TxAisAlarm = _LpE1TxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16, 1, 5),
    _LpE1TxAisAlarm_Type()
)
lpE1TxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TxAisAlarm.setStatus("mandatory")


class _LpE1TxRaiAlarm_Type(Integer32):
    """Custom type lpE1TxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1TxRaiAlarm_Type.__name__ = "Integer32"
_LpE1TxRaiAlarm_Object = MibTableColumn
lpE1TxRaiAlarm = _LpE1TxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 16, 1, 6),
    _LpE1TxRaiAlarm_Type()
)
lpE1TxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TxRaiAlarm.setStatus("mandatory")
_LpE1E1OperTable_Object = MibTable
lpE1E1OperTable = _LpE1E1OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 17)
)
if mibBuilder.loadTexts:
    lpE1E1OperTable.setStatus("mandatory")
_LpE1E1OperEntry_Object = MibTableRow
lpE1E1OperEntry = _LpE1E1OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 17, 1)
)
lpE1E1OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1E1OperEntry.setStatus("mandatory")


class _LpE1MultifrmLofAlarm_Type(Integer32):
    """Custom type lpE1MultifrmLofAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1MultifrmLofAlarm_Type.__name__ = "Integer32"
_LpE1MultifrmLofAlarm_Object = MibTableColumn
lpE1MultifrmLofAlarm = _LpE1MultifrmLofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 17, 1, 1),
    _LpE1MultifrmLofAlarm_Type()
)
lpE1MultifrmLofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1MultifrmLofAlarm.setStatus("mandatory")


class _LpE1RxMultifrmRaiAlarm_Type(Integer32):
    """Custom type lpE1RxMultifrmRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1RxMultifrmRaiAlarm_Type.__name__ = "Integer32"
_LpE1RxMultifrmRaiAlarm_Object = MibTableColumn
lpE1RxMultifrmRaiAlarm = _LpE1RxMultifrmRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 17, 1, 2),
    _LpE1RxMultifrmRaiAlarm_Type()
)
lpE1RxMultifrmRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1RxMultifrmRaiAlarm.setStatus("mandatory")


class _LpE1TxMultifrmRaiAlarm_Type(Integer32):
    """Custom type lpE1TxMultifrmRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpE1TxMultifrmRaiAlarm_Type.__name__ = "Integer32"
_LpE1TxMultifrmRaiAlarm_Object = MibTableColumn
lpE1TxMultifrmRaiAlarm = _LpE1TxMultifrmRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 17, 1, 3),
    _LpE1TxMultifrmRaiAlarm_Type()
)
lpE1TxMultifrmRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1TxMultifrmRaiAlarm.setStatus("mandatory")
_LpE1StatsTable_Object = MibTable
lpE1StatsTable = _LpE1StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18)
)
if mibBuilder.loadTexts:
    lpE1StatsTable.setStatus("mandatory")
_LpE1StatsEntry_Object = MibTableRow
lpE1StatsEntry = _LpE1StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1)
)
lpE1StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpE1Index"),
)
if mibBuilder.loadTexts:
    lpE1StatsEntry.setStatus("mandatory")
_LpE1RunningTime_Type = Counter32
_LpE1RunningTime_Object = MibTableColumn
lpE1RunningTime = _LpE1RunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 1),
    _LpE1RunningTime_Type()
)
lpE1RunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1RunningTime.setStatus("mandatory")
_LpE1ErrorFreeSec_Type = Counter32
_LpE1ErrorFreeSec_Object = MibTableColumn
lpE1ErrorFreeSec = _LpE1ErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 2),
    _LpE1ErrorFreeSec_Type()
)
lpE1ErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ErrorFreeSec.setStatus("mandatory")
_LpE1ErroredSec_Type = Counter32
_LpE1ErroredSec_Object = MibTableColumn
lpE1ErroredSec = _LpE1ErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 3),
    _LpE1ErroredSec_Type()
)
lpE1ErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1ErroredSec.setStatus("mandatory")
_LpE1SevErroredSec_Type = Counter32
_LpE1SevErroredSec_Object = MibTableColumn
lpE1SevErroredSec = _LpE1SevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 4),
    _LpE1SevErroredSec_Type()
)
lpE1SevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1SevErroredSec.setStatus("mandatory")
_LpE1SevErroredFrmSec_Type = Counter32
_LpE1SevErroredFrmSec_Object = MibTableColumn
lpE1SevErroredFrmSec = _LpE1SevErroredFrmSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 5),
    _LpE1SevErroredFrmSec_Type()
)
lpE1SevErroredFrmSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1SevErroredFrmSec.setStatus("mandatory")
_LpE1UnavailSec_Type = Counter32
_LpE1UnavailSec_Object = MibTableColumn
lpE1UnavailSec = _LpE1UnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 6),
    _LpE1UnavailSec_Type()
)
lpE1UnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1UnavailSec.setStatus("mandatory")
_LpE1BpvErrors_Type = Counter32
_LpE1BpvErrors_Object = MibTableColumn
lpE1BpvErrors = _LpE1BpvErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 7),
    _LpE1BpvErrors_Type()
)
lpE1BpvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1BpvErrors.setStatus("mandatory")
_LpE1CrcErrors_Type = Counter32
_LpE1CrcErrors_Object = MibTableColumn
lpE1CrcErrors = _LpE1CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 8),
    _LpE1CrcErrors_Type()
)
lpE1CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1CrcErrors.setStatus("mandatory")
_LpE1FrmErrors_Type = Counter32
_LpE1FrmErrors_Object = MibTableColumn
lpE1FrmErrors = _LpE1FrmErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 9),
    _LpE1FrmErrors_Type()
)
lpE1FrmErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1FrmErrors.setStatus("mandatory")
_LpE1LosStateChanges_Type = Counter32
_LpE1LosStateChanges_Object = MibTableColumn
lpE1LosStateChanges = _LpE1LosStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 10),
    _LpE1LosStateChanges_Type()
)
lpE1LosStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1LosStateChanges.setStatus("mandatory")
_LpE1SlipErrors_Type = Counter32
_LpE1SlipErrors_Object = MibTableColumn
lpE1SlipErrors = _LpE1SlipErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 8, 18, 1, 11),
    _LpE1SlipErrors_Type()
)
lpE1SlipErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpE1SlipErrors.setStatus("mandatory")
_LpV35_ObjectIdentity = ObjectIdentity
lpV35 = _LpV35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9)
)
_LpV35RowStatusTable_Object = MibTable
lpV35RowStatusTable = _LpV35RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 1)
)
if mibBuilder.loadTexts:
    lpV35RowStatusTable.setStatus("mandatory")
_LpV35RowStatusEntry_Object = MibTableRow
lpV35RowStatusEntry = _LpV35RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 1, 1)
)
lpV35RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35RowStatusEntry.setStatus("mandatory")
_LpV35RowStatus_Type = RowStatus
_LpV35RowStatus_Object = MibTableColumn
lpV35RowStatus = _LpV35RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 1, 1, 1),
    _LpV35RowStatus_Type()
)
lpV35RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35RowStatus.setStatus("mandatory")
_LpV35ComponentName_Type = DisplayString
_LpV35ComponentName_Object = MibTableColumn
lpV35ComponentName = _LpV35ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 1, 1, 2),
    _LpV35ComponentName_Type()
)
lpV35ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35ComponentName.setStatus("mandatory")
_LpV35StorageType_Type = StorageType
_LpV35StorageType_Object = MibTableColumn
lpV35StorageType = _LpV35StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 1, 1, 4),
    _LpV35StorageType_Type()
)
lpV35StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35StorageType.setStatus("mandatory")


class _LpV35Index_Type(Integer32):
    """Custom type lpV35Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LpV35Index_Type.__name__ = "Integer32"
_LpV35Index_Object = MibTableColumn
lpV35Index = _LpV35Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 1, 1, 10),
    _LpV35Index_Type()
)
lpV35Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpV35Index.setStatus("mandatory")
_LpV35Test_ObjectIdentity = ObjectIdentity
lpV35Test = _LpV35Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2)
)
_LpV35TestRowStatusTable_Object = MibTable
lpV35TestRowStatusTable = _LpV35TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 1)
)
if mibBuilder.loadTexts:
    lpV35TestRowStatusTable.setStatus("mandatory")
_LpV35TestRowStatusEntry_Object = MibTableRow
lpV35TestRowStatusEntry = _LpV35TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 1, 1)
)
lpV35TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35TestIndex"),
)
if mibBuilder.loadTexts:
    lpV35TestRowStatusEntry.setStatus("mandatory")
_LpV35TestRowStatus_Type = RowStatus
_LpV35TestRowStatus_Object = MibTableColumn
lpV35TestRowStatus = _LpV35TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 1, 1, 1),
    _LpV35TestRowStatus_Type()
)
lpV35TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestRowStatus.setStatus("mandatory")
_LpV35TestComponentName_Type = DisplayString
_LpV35TestComponentName_Object = MibTableColumn
lpV35TestComponentName = _LpV35TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 1, 1, 2),
    _LpV35TestComponentName_Type()
)
lpV35TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestComponentName.setStatus("mandatory")
_LpV35TestStorageType_Type = StorageType
_LpV35TestStorageType_Object = MibTableColumn
lpV35TestStorageType = _LpV35TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 1, 1, 4),
    _LpV35TestStorageType_Type()
)
lpV35TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestStorageType.setStatus("mandatory")
_LpV35TestIndex_Type = NonReplicated
_LpV35TestIndex_Object = MibTableColumn
lpV35TestIndex = _LpV35TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 1, 1, 10),
    _LpV35TestIndex_Type()
)
lpV35TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpV35TestIndex.setStatus("mandatory")
_LpV35TestStateTable_Object = MibTable
lpV35TestStateTable = _LpV35TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 10)
)
if mibBuilder.loadTexts:
    lpV35TestStateTable.setStatus("mandatory")
_LpV35TestStateEntry_Object = MibTableRow
lpV35TestStateEntry = _LpV35TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 10, 1)
)
lpV35TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35TestIndex"),
)
if mibBuilder.loadTexts:
    lpV35TestStateEntry.setStatus("mandatory")


class _LpV35TestAdminState_Type(Integer32):
    """Custom type lpV35TestAdminState based on Integer32"""
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


_LpV35TestAdminState_Type.__name__ = "Integer32"
_LpV35TestAdminState_Object = MibTableColumn
lpV35TestAdminState = _LpV35TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 10, 1, 1),
    _LpV35TestAdminState_Type()
)
lpV35TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestAdminState.setStatus("mandatory")


class _LpV35TestOperationalState_Type(Integer32):
    """Custom type lpV35TestOperationalState based on Integer32"""
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


_LpV35TestOperationalState_Type.__name__ = "Integer32"
_LpV35TestOperationalState_Object = MibTableColumn
lpV35TestOperationalState = _LpV35TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 10, 1, 2),
    _LpV35TestOperationalState_Type()
)
lpV35TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestOperationalState.setStatus("mandatory")


class _LpV35TestUsageState_Type(Integer32):
    """Custom type lpV35TestUsageState based on Integer32"""
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


_LpV35TestUsageState_Type.__name__ = "Integer32"
_LpV35TestUsageState_Object = MibTableColumn
lpV35TestUsageState = _LpV35TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 10, 1, 3),
    _LpV35TestUsageState_Type()
)
lpV35TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestUsageState.setStatus("mandatory")
_LpV35TestSetupTable_Object = MibTable
lpV35TestSetupTable = _LpV35TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11)
)
if mibBuilder.loadTexts:
    lpV35TestSetupTable.setStatus("mandatory")
_LpV35TestSetupEntry_Object = MibTableRow
lpV35TestSetupEntry = _LpV35TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1)
)
lpV35TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35TestIndex"),
)
if mibBuilder.loadTexts:
    lpV35TestSetupEntry.setStatus("mandatory")


class _LpV35TestPurpose_Type(AsciiString):
    """Custom type lpV35TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpV35TestPurpose_Type.__name__ = "AsciiString"
_LpV35TestPurpose_Object = MibTableColumn
lpV35TestPurpose = _LpV35TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 1),
    _LpV35TestPurpose_Type()
)
lpV35TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestPurpose.setStatus("mandatory")


class _LpV35TestType_Type(Integer32):
    """Custom type lpV35TestType based on Integer32"""
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


_LpV35TestType_Type.__name__ = "Integer32"
_LpV35TestType_Object = MibTableColumn
lpV35TestType = _LpV35TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 2),
    _LpV35TestType_Type()
)
lpV35TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestType.setStatus("mandatory")


class _LpV35TestFrmSize_Type(Unsigned32):
    """Custom type lpV35TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpV35TestFrmSize_Type.__name__ = "Unsigned32"
_LpV35TestFrmSize_Object = MibTableColumn
lpV35TestFrmSize = _LpV35TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 3),
    _LpV35TestFrmSize_Type()
)
lpV35TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestFrmSize.setStatus("mandatory")


class _LpV35TestFrmPatternType_Type(Integer32):
    """Custom type lpV35TestFrmPatternType based on Integer32"""
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


_LpV35TestFrmPatternType_Type.__name__ = "Integer32"
_LpV35TestFrmPatternType_Object = MibTableColumn
lpV35TestFrmPatternType = _LpV35TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 4),
    _LpV35TestFrmPatternType_Type()
)
lpV35TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestFrmPatternType.setStatus("mandatory")


class _LpV35TestCustomizedPattern_Type(Hex):
    """Custom type lpV35TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpV35TestCustomizedPattern_Type.__name__ = "Hex"
_LpV35TestCustomizedPattern_Object = MibTableColumn
lpV35TestCustomizedPattern = _LpV35TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 5),
    _LpV35TestCustomizedPattern_Type()
)
lpV35TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestCustomizedPattern.setStatus("mandatory")


class _LpV35TestDataStartDelay_Type(Unsigned32):
    """Custom type lpV35TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpV35TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpV35TestDataStartDelay_Object = MibTableColumn
lpV35TestDataStartDelay = _LpV35TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 6),
    _LpV35TestDataStartDelay_Type()
)
lpV35TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestDataStartDelay.setStatus("mandatory")


class _LpV35TestDisplayInterval_Type(Unsigned32):
    """Custom type lpV35TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpV35TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpV35TestDisplayInterval_Object = MibTableColumn
lpV35TestDisplayInterval = _LpV35TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 7),
    _LpV35TestDisplayInterval_Type()
)
lpV35TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestDisplayInterval.setStatus("mandatory")


class _LpV35TestDuration_Type(Unsigned32):
    """Custom type lpV35TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpV35TestDuration_Type.__name__ = "Unsigned32"
_LpV35TestDuration_Object = MibTableColumn
lpV35TestDuration = _LpV35TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 11, 1, 8),
    _LpV35TestDuration_Type()
)
lpV35TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35TestDuration.setStatus("mandatory")
_LpV35TestResultsTable_Object = MibTable
lpV35TestResultsTable = _LpV35TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12)
)
if mibBuilder.loadTexts:
    lpV35TestResultsTable.setStatus("mandatory")
_LpV35TestResultsEntry_Object = MibTableRow
lpV35TestResultsEntry = _LpV35TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1)
)
lpV35TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35TestIndex"),
)
if mibBuilder.loadTexts:
    lpV35TestResultsEntry.setStatus("mandatory")
_LpV35TestElapsedTime_Type = Counter32
_LpV35TestElapsedTime_Object = MibTableColumn
lpV35TestElapsedTime = _LpV35TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 1),
    _LpV35TestElapsedTime_Type()
)
lpV35TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestElapsedTime.setStatus("mandatory")


class _LpV35TestTimeRemaining_Type(Unsigned32):
    """Custom type lpV35TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpV35TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpV35TestTimeRemaining_Object = MibTableColumn
lpV35TestTimeRemaining = _LpV35TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 2),
    _LpV35TestTimeRemaining_Type()
)
lpV35TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestTimeRemaining.setStatus("mandatory")


class _LpV35TestCauseOfTermination_Type(Integer32):
    """Custom type lpV35TestCauseOfTermination based on Integer32"""
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


_LpV35TestCauseOfTermination_Type.__name__ = "Integer32"
_LpV35TestCauseOfTermination_Object = MibTableColumn
lpV35TestCauseOfTermination = _LpV35TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 3),
    _LpV35TestCauseOfTermination_Type()
)
lpV35TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestCauseOfTermination.setStatus("mandatory")
_LpV35TestBitsTx_Type = PassportCounter64
_LpV35TestBitsTx_Object = MibTableColumn
lpV35TestBitsTx = _LpV35TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 4),
    _LpV35TestBitsTx_Type()
)
lpV35TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestBitsTx.setStatus("mandatory")
_LpV35TestBytesTx_Type = PassportCounter64
_LpV35TestBytesTx_Object = MibTableColumn
lpV35TestBytesTx = _LpV35TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 5),
    _LpV35TestBytesTx_Type()
)
lpV35TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestBytesTx.setStatus("mandatory")
_LpV35TestFrmTx_Type = PassportCounter64
_LpV35TestFrmTx_Object = MibTableColumn
lpV35TestFrmTx = _LpV35TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 6),
    _LpV35TestFrmTx_Type()
)
lpV35TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestFrmTx.setStatus("mandatory")
_LpV35TestBitsRx_Type = PassportCounter64
_LpV35TestBitsRx_Object = MibTableColumn
lpV35TestBitsRx = _LpV35TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 7),
    _LpV35TestBitsRx_Type()
)
lpV35TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestBitsRx.setStatus("mandatory")
_LpV35TestBytesRx_Type = PassportCounter64
_LpV35TestBytesRx_Object = MibTableColumn
lpV35TestBytesRx = _LpV35TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 8),
    _LpV35TestBytesRx_Type()
)
lpV35TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestBytesRx.setStatus("mandatory")
_LpV35TestFrmRx_Type = PassportCounter64
_LpV35TestFrmRx_Object = MibTableColumn
lpV35TestFrmRx = _LpV35TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 9),
    _LpV35TestFrmRx_Type()
)
lpV35TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestFrmRx.setStatus("mandatory")
_LpV35TestErroredFrmRx_Type = PassportCounter64
_LpV35TestErroredFrmRx_Object = MibTableColumn
lpV35TestErroredFrmRx = _LpV35TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 10),
    _LpV35TestErroredFrmRx_Type()
)
lpV35TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestErroredFrmRx.setStatus("mandatory")


class _LpV35TestBitErrorRate_Type(AsciiString):
    """Custom type lpV35TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpV35TestBitErrorRate_Type.__name__ = "AsciiString"
_LpV35TestBitErrorRate_Object = MibTableColumn
lpV35TestBitErrorRate = _LpV35TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 2, 12, 1, 11),
    _LpV35TestBitErrorRate_Type()
)
lpV35TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35TestBitErrorRate.setStatus("mandatory")
_LpV35ProvTable_Object = MibTable
lpV35ProvTable = _LpV35ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10)
)
if mibBuilder.loadTexts:
    lpV35ProvTable.setStatus("mandatory")
_LpV35ProvEntry_Object = MibTableRow
lpV35ProvEntry = _LpV35ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1)
)
lpV35ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35ProvEntry.setStatus("mandatory")


class _LpV35LinkMode_Type(Integer32):
    """Custom type lpV35LinkMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dce", 128),
          ("dte", 0))
    )


_LpV35LinkMode_Type.__name__ = "Integer32"
_LpV35LinkMode_Object = MibTableColumn
lpV35LinkMode = _LpV35LinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 1),
    _LpV35LinkMode_Type()
)
lpV35LinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35LinkMode.setStatus("mandatory")


class _LpV35ReadyLineState_Type(OctetString):
    """Custom type lpV35ReadyLineState based on OctetString"""
    defaultHexValue = "f0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpV35ReadyLineState_Type.__name__ = "OctetString"
_LpV35ReadyLineState_Object = MibTableColumn
lpV35ReadyLineState = _LpV35ReadyLineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 2),
    _LpV35ReadyLineState_Type()
)
lpV35ReadyLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35ReadyLineState.setStatus("mandatory")


class _LpV35DataTransferLineState_Type(OctetString):
    """Custom type lpV35DataTransferLineState based on OctetString"""
    defaultHexValue = "f0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpV35DataTransferLineState_Type.__name__ = "OctetString"
_LpV35DataTransferLineState_Object = MibTableColumn
lpV35DataTransferLineState = _LpV35DataTransferLineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 3),
    _LpV35DataTransferLineState_Type()
)
lpV35DataTransferLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35DataTransferLineState.setStatus("mandatory")


class _LpV35LineStatusTimeOut_Type(Unsigned32):
    """Custom type lpV35LineStatusTimeOut based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20000),
    )


_LpV35LineStatusTimeOut_Type.__name__ = "Unsigned32"
_LpV35LineStatusTimeOut_Object = MibTableColumn
lpV35LineStatusTimeOut = _LpV35LineStatusTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 4),
    _LpV35LineStatusTimeOut_Type()
)
lpV35LineStatusTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35LineStatusTimeOut.setStatus("mandatory")


class _LpV35LineSpeed_Type(Unsigned32):
    """Custom type lpV35LineSpeed based on Unsigned32"""
    defaultValue = 192000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 3840000),
    )


_LpV35LineSpeed_Type.__name__ = "Unsigned32"
_LpV35LineSpeed_Object = MibTableColumn
lpV35LineSpeed = _LpV35LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 5),
    _LpV35LineSpeed_Type()
)
lpV35LineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35LineSpeed.setStatus("mandatory")


class _LpV35ClockingSource_Type(Integer32):
    """Custom type lpV35ClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("module", 1))
    )


_LpV35ClockingSource_Type.__name__ = "Integer32"
_LpV35ClockingSource_Object = MibTableColumn
lpV35ClockingSource = _LpV35ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 6),
    _LpV35ClockingSource_Type()
)
lpV35ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35ClockingSource.setStatus("mandatory")


class _LpV35DteDataClockSource_Type(Integer32):
    """Custom type lpV35DteDataClockSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromDce", 0),
          ("fromDte", 2))
    )


_LpV35DteDataClockSource_Type.__name__ = "Integer32"
_LpV35DteDataClockSource_Object = MibTableColumn
lpV35DteDataClockSource = _LpV35DteDataClockSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 7),
    _LpV35DteDataClockSource_Type()
)
lpV35DteDataClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35DteDataClockSource.setStatus("mandatory")
_LpV35ApplicationFramerName_Type = Link
_LpV35ApplicationFramerName_Object = MibTableColumn
lpV35ApplicationFramerName = _LpV35ApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 8),
    _LpV35ApplicationFramerName_Type()
)
lpV35ApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35ApplicationFramerName.setStatus("mandatory")


class _LpV35EnableDynamicSpeed_Type(Integer32):
    """Custom type lpV35EnableDynamicSpeed based on Integer32"""
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


_LpV35EnableDynamicSpeed_Type.__name__ = "Integer32"
_LpV35EnableDynamicSpeed_Object = MibTableColumn
lpV35EnableDynamicSpeed = _LpV35EnableDynamicSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 10, 1, 9),
    _LpV35EnableDynamicSpeed_Type()
)
lpV35EnableDynamicSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35EnableDynamicSpeed.setStatus("mandatory")
_LpV35CidDataTable_Object = MibTable
lpV35CidDataTable = _LpV35CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 11)
)
if mibBuilder.loadTexts:
    lpV35CidDataTable.setStatus("mandatory")
_LpV35CidDataEntry_Object = MibTableRow
lpV35CidDataEntry = _LpV35CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 11, 1)
)
lpV35CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35CidDataEntry.setStatus("mandatory")


class _LpV35CustomerIdentifier_Type(Unsigned32):
    """Custom type lpV35CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpV35CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpV35CustomerIdentifier_Object = MibTableColumn
lpV35CustomerIdentifier = _LpV35CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 11, 1, 1),
    _LpV35CustomerIdentifier_Type()
)
lpV35CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35CustomerIdentifier.setStatus("mandatory")
_LpV35AdminInfoTable_Object = MibTable
lpV35AdminInfoTable = _LpV35AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 12)
)
if mibBuilder.loadTexts:
    lpV35AdminInfoTable.setStatus("mandatory")
_LpV35AdminInfoEntry_Object = MibTableRow
lpV35AdminInfoEntry = _LpV35AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 12, 1)
)
lpV35AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35AdminInfoEntry.setStatus("mandatory")


class _LpV35Vendor_Type(AsciiString):
    """Custom type lpV35Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpV35Vendor_Type.__name__ = "AsciiString"
_LpV35Vendor_Object = MibTableColumn
lpV35Vendor = _LpV35Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 12, 1, 1),
    _LpV35Vendor_Type()
)
lpV35Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35Vendor.setStatus("mandatory")


class _LpV35CommentText_Type(AsciiString):
    """Custom type lpV35CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpV35CommentText_Type.__name__ = "AsciiString"
_LpV35CommentText_Object = MibTableColumn
lpV35CommentText = _LpV35CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 12, 1, 2),
    _LpV35CommentText_Type()
)
lpV35CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35CommentText.setStatus("mandatory")
_LpV35IfEntryTable_Object = MibTable
lpV35IfEntryTable = _LpV35IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 13)
)
if mibBuilder.loadTexts:
    lpV35IfEntryTable.setStatus("mandatory")
_LpV35IfEntryEntry_Object = MibTableRow
lpV35IfEntryEntry = _LpV35IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 13, 1)
)
lpV35IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35IfEntryEntry.setStatus("mandatory")


class _LpV35IfAdminStatus_Type(Integer32):
    """Custom type lpV35IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpV35IfAdminStatus_Type.__name__ = "Integer32"
_LpV35IfAdminStatus_Object = MibTableColumn
lpV35IfAdminStatus = _LpV35IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 13, 1, 1),
    _LpV35IfAdminStatus_Type()
)
lpV35IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpV35IfAdminStatus.setStatus("mandatory")


class _LpV35IfIndex_Type(InterfaceIndex):
    """Custom type lpV35IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpV35IfIndex_Type.__name__ = "InterfaceIndex"
_LpV35IfIndex_Object = MibTableColumn
lpV35IfIndex = _LpV35IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 13, 1, 2),
    _LpV35IfIndex_Type()
)
lpV35IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35IfIndex.setStatus("mandatory")
_LpV35OperStatusTable_Object = MibTable
lpV35OperStatusTable = _LpV35OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 14)
)
if mibBuilder.loadTexts:
    lpV35OperStatusTable.setStatus("mandatory")
_LpV35OperStatusEntry_Object = MibTableRow
lpV35OperStatusEntry = _LpV35OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 14, 1)
)
lpV35OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35OperStatusEntry.setStatus("mandatory")


class _LpV35SnmpOperStatus_Type(Integer32):
    """Custom type lpV35SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpV35SnmpOperStatus_Type.__name__ = "Integer32"
_LpV35SnmpOperStatus_Object = MibTableColumn
lpV35SnmpOperStatus = _LpV35SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 14, 1, 1),
    _LpV35SnmpOperStatus_Type()
)
lpV35SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35SnmpOperStatus.setStatus("mandatory")
_LpV35StateTable_Object = MibTable
lpV35StateTable = _LpV35StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15)
)
if mibBuilder.loadTexts:
    lpV35StateTable.setStatus("mandatory")
_LpV35StateEntry_Object = MibTableRow
lpV35StateEntry = _LpV35StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1)
)
lpV35StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35StateEntry.setStatus("mandatory")


class _LpV35AdminState_Type(Integer32):
    """Custom type lpV35AdminState based on Integer32"""
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


_LpV35AdminState_Type.__name__ = "Integer32"
_LpV35AdminState_Object = MibTableColumn
lpV35AdminState = _LpV35AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 1),
    _LpV35AdminState_Type()
)
lpV35AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35AdminState.setStatus("mandatory")


class _LpV35OperationalState_Type(Integer32):
    """Custom type lpV35OperationalState based on Integer32"""
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


_LpV35OperationalState_Type.__name__ = "Integer32"
_LpV35OperationalState_Object = MibTableColumn
lpV35OperationalState = _LpV35OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 2),
    _LpV35OperationalState_Type()
)
lpV35OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35OperationalState.setStatus("mandatory")


class _LpV35UsageState_Type(Integer32):
    """Custom type lpV35UsageState based on Integer32"""
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


_LpV35UsageState_Type.__name__ = "Integer32"
_LpV35UsageState_Object = MibTableColumn
lpV35UsageState = _LpV35UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 3),
    _LpV35UsageState_Type()
)
lpV35UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35UsageState.setStatus("mandatory")


class _LpV35AvailabilityStatus_Type(OctetString):
    """Custom type lpV35AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpV35AvailabilityStatus_Type.__name__ = "OctetString"
_LpV35AvailabilityStatus_Object = MibTableColumn
lpV35AvailabilityStatus = _LpV35AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 4),
    _LpV35AvailabilityStatus_Type()
)
lpV35AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35AvailabilityStatus.setStatus("mandatory")


class _LpV35ProceduralStatus_Type(OctetString):
    """Custom type lpV35ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpV35ProceduralStatus_Type.__name__ = "OctetString"
_LpV35ProceduralStatus_Object = MibTableColumn
lpV35ProceduralStatus = _LpV35ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 5),
    _LpV35ProceduralStatus_Type()
)
lpV35ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35ProceduralStatus.setStatus("mandatory")


class _LpV35ControlStatus_Type(OctetString):
    """Custom type lpV35ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpV35ControlStatus_Type.__name__ = "OctetString"
_LpV35ControlStatus_Object = MibTableColumn
lpV35ControlStatus = _LpV35ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 6),
    _LpV35ControlStatus_Type()
)
lpV35ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35ControlStatus.setStatus("mandatory")


class _LpV35AlarmStatus_Type(OctetString):
    """Custom type lpV35AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpV35AlarmStatus_Type.__name__ = "OctetString"
_LpV35AlarmStatus_Object = MibTableColumn
lpV35AlarmStatus = _LpV35AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 7),
    _LpV35AlarmStatus_Type()
)
lpV35AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35AlarmStatus.setStatus("mandatory")


class _LpV35StandbyStatus_Type(Integer32):
    """Custom type lpV35StandbyStatus based on Integer32"""
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


_LpV35StandbyStatus_Type.__name__ = "Integer32"
_LpV35StandbyStatus_Object = MibTableColumn
lpV35StandbyStatus = _LpV35StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 8),
    _LpV35StandbyStatus_Type()
)
lpV35StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35StandbyStatus.setStatus("mandatory")


class _LpV35UnknownStatus_Type(Integer32):
    """Custom type lpV35UnknownStatus based on Integer32"""
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


_LpV35UnknownStatus_Type.__name__ = "Integer32"
_LpV35UnknownStatus_Object = MibTableColumn
lpV35UnknownStatus = _LpV35UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 15, 1, 9),
    _LpV35UnknownStatus_Type()
)
lpV35UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35UnknownStatus.setStatus("mandatory")
_LpV35OperTable_Object = MibTable
lpV35OperTable = _LpV35OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 16)
)
if mibBuilder.loadTexts:
    lpV35OperTable.setStatus("mandatory")
_LpV35OperEntry_Object = MibTableRow
lpV35OperEntry = _LpV35OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 16, 1)
)
lpV35OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpV35Index"),
)
if mibBuilder.loadTexts:
    lpV35OperEntry.setStatus("mandatory")


class _LpV35ActualLinkMode_Type(Integer32):
    """Custom type lpV35ActualLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dce", 128),
          ("dte", 0))
    )


_LpV35ActualLinkMode_Type.__name__ = "Integer32"
_LpV35ActualLinkMode_Object = MibTableColumn
lpV35ActualLinkMode = _LpV35ActualLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 16, 1, 1),
    _LpV35ActualLinkMode_Type()
)
lpV35ActualLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35ActualLinkMode.setStatus("mandatory")


class _LpV35LineState_Type(OctetString):
    """Custom type lpV35LineState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpV35LineState_Type.__name__ = "OctetString"
_LpV35LineState_Object = MibTableColumn
lpV35LineState = _LpV35LineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 16, 1, 2),
    _LpV35LineState_Type()
)
lpV35LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35LineState.setStatus("mandatory")


class _LpV35ActualTxLineSpeed_Type(Gauge32):
    """Custom type lpV35ActualTxLineSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpV35ActualTxLineSpeed_Type.__name__ = "Gauge32"
_LpV35ActualTxLineSpeed_Object = MibTableColumn
lpV35ActualTxLineSpeed = _LpV35ActualTxLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 16, 1, 3),
    _LpV35ActualTxLineSpeed_Type()
)
lpV35ActualTxLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35ActualTxLineSpeed.setStatus("mandatory")


class _LpV35ActualRxLineSpeed_Type(Gauge32):
    """Custom type lpV35ActualRxLineSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpV35ActualRxLineSpeed_Type.__name__ = "Gauge32"
_LpV35ActualRxLineSpeed_Object = MibTableColumn
lpV35ActualRxLineSpeed = _LpV35ActualRxLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 16, 1, 4),
    _LpV35ActualRxLineSpeed_Type()
)
lpV35ActualRxLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35ActualRxLineSpeed.setStatus("mandatory")
_LpV35DataXferStateChanges_Type = Counter32
_LpV35DataXferStateChanges_Object = MibTableColumn
lpV35DataXferStateChanges = _LpV35DataXferStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 9, 16, 1, 5),
    _LpV35DataXferStateChanges_Type()
)
lpV35DataXferStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpV35DataXferStateChanges.setStatus("mandatory")
_LpX21_ObjectIdentity = ObjectIdentity
lpX21 = _LpX21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10)
)
_LpX21RowStatusTable_Object = MibTable
lpX21RowStatusTable = _LpX21RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 1)
)
if mibBuilder.loadTexts:
    lpX21RowStatusTable.setStatus("mandatory")
_LpX21RowStatusEntry_Object = MibTableRow
lpX21RowStatusEntry = _LpX21RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 1, 1)
)
lpX21RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21RowStatusEntry.setStatus("mandatory")
_LpX21RowStatus_Type = RowStatus
_LpX21RowStatus_Object = MibTableColumn
lpX21RowStatus = _LpX21RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 1, 1, 1),
    _LpX21RowStatus_Type()
)
lpX21RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21RowStatus.setStatus("mandatory")
_LpX21ComponentName_Type = DisplayString
_LpX21ComponentName_Object = MibTableColumn
lpX21ComponentName = _LpX21ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 1, 1, 2),
    _LpX21ComponentName_Type()
)
lpX21ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21ComponentName.setStatus("mandatory")
_LpX21StorageType_Type = StorageType
_LpX21StorageType_Object = MibTableColumn
lpX21StorageType = _LpX21StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 1, 1, 4),
    _LpX21StorageType_Type()
)
lpX21StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21StorageType.setStatus("mandatory")


class _LpX21Index_Type(Integer32):
    """Custom type lpX21Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LpX21Index_Type.__name__ = "Integer32"
_LpX21Index_Object = MibTableColumn
lpX21Index = _LpX21Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 1, 1, 10),
    _LpX21Index_Type()
)
lpX21Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpX21Index.setStatus("mandatory")
_LpX21Test_ObjectIdentity = ObjectIdentity
lpX21Test = _LpX21Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2)
)
_LpX21TestRowStatusTable_Object = MibTable
lpX21TestRowStatusTable = _LpX21TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 1)
)
if mibBuilder.loadTexts:
    lpX21TestRowStatusTable.setStatus("mandatory")
_LpX21TestRowStatusEntry_Object = MibTableRow
lpX21TestRowStatusEntry = _LpX21TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 1, 1)
)
lpX21TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21TestIndex"),
)
if mibBuilder.loadTexts:
    lpX21TestRowStatusEntry.setStatus("mandatory")
_LpX21TestRowStatus_Type = RowStatus
_LpX21TestRowStatus_Object = MibTableColumn
lpX21TestRowStatus = _LpX21TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 1, 1, 1),
    _LpX21TestRowStatus_Type()
)
lpX21TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestRowStatus.setStatus("mandatory")
_LpX21TestComponentName_Type = DisplayString
_LpX21TestComponentName_Object = MibTableColumn
lpX21TestComponentName = _LpX21TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 1, 1, 2),
    _LpX21TestComponentName_Type()
)
lpX21TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestComponentName.setStatus("mandatory")
_LpX21TestStorageType_Type = StorageType
_LpX21TestStorageType_Object = MibTableColumn
lpX21TestStorageType = _LpX21TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 1, 1, 4),
    _LpX21TestStorageType_Type()
)
lpX21TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestStorageType.setStatus("mandatory")
_LpX21TestIndex_Type = NonReplicated
_LpX21TestIndex_Object = MibTableColumn
lpX21TestIndex = _LpX21TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 1, 1, 10),
    _LpX21TestIndex_Type()
)
lpX21TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpX21TestIndex.setStatus("mandatory")
_LpX21TestStateTable_Object = MibTable
lpX21TestStateTable = _LpX21TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 10)
)
if mibBuilder.loadTexts:
    lpX21TestStateTable.setStatus("mandatory")
_LpX21TestStateEntry_Object = MibTableRow
lpX21TestStateEntry = _LpX21TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 10, 1)
)
lpX21TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21TestIndex"),
)
if mibBuilder.loadTexts:
    lpX21TestStateEntry.setStatus("mandatory")


class _LpX21TestAdminState_Type(Integer32):
    """Custom type lpX21TestAdminState based on Integer32"""
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


_LpX21TestAdminState_Type.__name__ = "Integer32"
_LpX21TestAdminState_Object = MibTableColumn
lpX21TestAdminState = _LpX21TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 10, 1, 1),
    _LpX21TestAdminState_Type()
)
lpX21TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestAdminState.setStatus("mandatory")


class _LpX21TestOperationalState_Type(Integer32):
    """Custom type lpX21TestOperationalState based on Integer32"""
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


_LpX21TestOperationalState_Type.__name__ = "Integer32"
_LpX21TestOperationalState_Object = MibTableColumn
lpX21TestOperationalState = _LpX21TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 10, 1, 2),
    _LpX21TestOperationalState_Type()
)
lpX21TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestOperationalState.setStatus("mandatory")


class _LpX21TestUsageState_Type(Integer32):
    """Custom type lpX21TestUsageState based on Integer32"""
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


_LpX21TestUsageState_Type.__name__ = "Integer32"
_LpX21TestUsageState_Object = MibTableColumn
lpX21TestUsageState = _LpX21TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 10, 1, 3),
    _LpX21TestUsageState_Type()
)
lpX21TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestUsageState.setStatus("mandatory")
_LpX21TestSetupTable_Object = MibTable
lpX21TestSetupTable = _LpX21TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11)
)
if mibBuilder.loadTexts:
    lpX21TestSetupTable.setStatus("mandatory")
_LpX21TestSetupEntry_Object = MibTableRow
lpX21TestSetupEntry = _LpX21TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1)
)
lpX21TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21TestIndex"),
)
if mibBuilder.loadTexts:
    lpX21TestSetupEntry.setStatus("mandatory")


class _LpX21TestPurpose_Type(AsciiString):
    """Custom type lpX21TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpX21TestPurpose_Type.__name__ = "AsciiString"
_LpX21TestPurpose_Object = MibTableColumn
lpX21TestPurpose = _LpX21TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 1),
    _LpX21TestPurpose_Type()
)
lpX21TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestPurpose.setStatus("mandatory")


class _LpX21TestType_Type(Integer32):
    """Custom type lpX21TestType based on Integer32"""
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


_LpX21TestType_Type.__name__ = "Integer32"
_LpX21TestType_Object = MibTableColumn
lpX21TestType = _LpX21TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 2),
    _LpX21TestType_Type()
)
lpX21TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestType.setStatus("mandatory")


class _LpX21TestFrmSize_Type(Unsigned32):
    """Custom type lpX21TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpX21TestFrmSize_Type.__name__ = "Unsigned32"
_LpX21TestFrmSize_Object = MibTableColumn
lpX21TestFrmSize = _LpX21TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 3),
    _LpX21TestFrmSize_Type()
)
lpX21TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestFrmSize.setStatus("mandatory")


class _LpX21TestFrmPatternType_Type(Integer32):
    """Custom type lpX21TestFrmPatternType based on Integer32"""
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


_LpX21TestFrmPatternType_Type.__name__ = "Integer32"
_LpX21TestFrmPatternType_Object = MibTableColumn
lpX21TestFrmPatternType = _LpX21TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 4),
    _LpX21TestFrmPatternType_Type()
)
lpX21TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestFrmPatternType.setStatus("mandatory")


class _LpX21TestCustomizedPattern_Type(Hex):
    """Custom type lpX21TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpX21TestCustomizedPattern_Type.__name__ = "Hex"
_LpX21TestCustomizedPattern_Object = MibTableColumn
lpX21TestCustomizedPattern = _LpX21TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 5),
    _LpX21TestCustomizedPattern_Type()
)
lpX21TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestCustomizedPattern.setStatus("mandatory")


class _LpX21TestDataStartDelay_Type(Unsigned32):
    """Custom type lpX21TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpX21TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpX21TestDataStartDelay_Object = MibTableColumn
lpX21TestDataStartDelay = _LpX21TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 6),
    _LpX21TestDataStartDelay_Type()
)
lpX21TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestDataStartDelay.setStatus("mandatory")


class _LpX21TestDisplayInterval_Type(Unsigned32):
    """Custom type lpX21TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpX21TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpX21TestDisplayInterval_Object = MibTableColumn
lpX21TestDisplayInterval = _LpX21TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 7),
    _LpX21TestDisplayInterval_Type()
)
lpX21TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestDisplayInterval.setStatus("mandatory")


class _LpX21TestDuration_Type(Unsigned32):
    """Custom type lpX21TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpX21TestDuration_Type.__name__ = "Unsigned32"
_LpX21TestDuration_Object = MibTableColumn
lpX21TestDuration = _LpX21TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 11, 1, 8),
    _LpX21TestDuration_Type()
)
lpX21TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21TestDuration.setStatus("mandatory")
_LpX21TestResultsTable_Object = MibTable
lpX21TestResultsTable = _LpX21TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12)
)
if mibBuilder.loadTexts:
    lpX21TestResultsTable.setStatus("mandatory")
_LpX21TestResultsEntry_Object = MibTableRow
lpX21TestResultsEntry = _LpX21TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1)
)
lpX21TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21TestIndex"),
)
if mibBuilder.loadTexts:
    lpX21TestResultsEntry.setStatus("mandatory")
_LpX21TestElapsedTime_Type = Counter32
_LpX21TestElapsedTime_Object = MibTableColumn
lpX21TestElapsedTime = _LpX21TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 1),
    _LpX21TestElapsedTime_Type()
)
lpX21TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestElapsedTime.setStatus("mandatory")


class _LpX21TestTimeRemaining_Type(Unsigned32):
    """Custom type lpX21TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpX21TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpX21TestTimeRemaining_Object = MibTableColumn
lpX21TestTimeRemaining = _LpX21TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 2),
    _LpX21TestTimeRemaining_Type()
)
lpX21TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestTimeRemaining.setStatus("mandatory")


class _LpX21TestCauseOfTermination_Type(Integer32):
    """Custom type lpX21TestCauseOfTermination based on Integer32"""
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


_LpX21TestCauseOfTermination_Type.__name__ = "Integer32"
_LpX21TestCauseOfTermination_Object = MibTableColumn
lpX21TestCauseOfTermination = _LpX21TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 3),
    _LpX21TestCauseOfTermination_Type()
)
lpX21TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestCauseOfTermination.setStatus("mandatory")
_LpX21TestBitsTx_Type = PassportCounter64
_LpX21TestBitsTx_Object = MibTableColumn
lpX21TestBitsTx = _LpX21TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 4),
    _LpX21TestBitsTx_Type()
)
lpX21TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestBitsTx.setStatus("mandatory")
_LpX21TestBytesTx_Type = PassportCounter64
_LpX21TestBytesTx_Object = MibTableColumn
lpX21TestBytesTx = _LpX21TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 5),
    _LpX21TestBytesTx_Type()
)
lpX21TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestBytesTx.setStatus("mandatory")
_LpX21TestFrmTx_Type = PassportCounter64
_LpX21TestFrmTx_Object = MibTableColumn
lpX21TestFrmTx = _LpX21TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 6),
    _LpX21TestFrmTx_Type()
)
lpX21TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestFrmTx.setStatus("mandatory")
_LpX21TestBitsRx_Type = PassportCounter64
_LpX21TestBitsRx_Object = MibTableColumn
lpX21TestBitsRx = _LpX21TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 7),
    _LpX21TestBitsRx_Type()
)
lpX21TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestBitsRx.setStatus("mandatory")
_LpX21TestBytesRx_Type = PassportCounter64
_LpX21TestBytesRx_Object = MibTableColumn
lpX21TestBytesRx = _LpX21TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 8),
    _LpX21TestBytesRx_Type()
)
lpX21TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestBytesRx.setStatus("mandatory")
_LpX21TestFrmRx_Type = PassportCounter64
_LpX21TestFrmRx_Object = MibTableColumn
lpX21TestFrmRx = _LpX21TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 9),
    _LpX21TestFrmRx_Type()
)
lpX21TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestFrmRx.setStatus("mandatory")
_LpX21TestErroredFrmRx_Type = PassportCounter64
_LpX21TestErroredFrmRx_Object = MibTableColumn
lpX21TestErroredFrmRx = _LpX21TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 10),
    _LpX21TestErroredFrmRx_Type()
)
lpX21TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestErroredFrmRx.setStatus("mandatory")


class _LpX21TestBitErrorRate_Type(AsciiString):
    """Custom type lpX21TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpX21TestBitErrorRate_Type.__name__ = "AsciiString"
_LpX21TestBitErrorRate_Object = MibTableColumn
lpX21TestBitErrorRate = _LpX21TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 2, 12, 1, 11),
    _LpX21TestBitErrorRate_Type()
)
lpX21TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21TestBitErrorRate.setStatus("mandatory")
_LpX21ProvTable_Object = MibTable
lpX21ProvTable = _LpX21ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10)
)
if mibBuilder.loadTexts:
    lpX21ProvTable.setStatus("mandatory")
_LpX21ProvEntry_Object = MibTableRow
lpX21ProvEntry = _LpX21ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1)
)
lpX21ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21ProvEntry.setStatus("mandatory")


class _LpX21LinkMode_Type(Integer32):
    """Custom type lpX21LinkMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dce", 128),
          ("dte", 0))
    )


_LpX21LinkMode_Type.__name__ = "Integer32"
_LpX21LinkMode_Object = MibTableColumn
lpX21LinkMode = _LpX21LinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 1),
    _LpX21LinkMode_Type()
)
lpX21LinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21LinkMode.setStatus("mandatory")


class _LpX21ReadyLineState_Type(OctetString):
    """Custom type lpX21ReadyLineState based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpX21ReadyLineState_Type.__name__ = "OctetString"
_LpX21ReadyLineState_Object = MibTableColumn
lpX21ReadyLineState = _LpX21ReadyLineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 2),
    _LpX21ReadyLineState_Type()
)
lpX21ReadyLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21ReadyLineState.setStatus("mandatory")


class _LpX21DataTransferLineState_Type(OctetString):
    """Custom type lpX21DataTransferLineState based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpX21DataTransferLineState_Type.__name__ = "OctetString"
_LpX21DataTransferLineState_Object = MibTableColumn
lpX21DataTransferLineState = _LpX21DataTransferLineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 3),
    _LpX21DataTransferLineState_Type()
)
lpX21DataTransferLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21DataTransferLineState.setStatus("mandatory")


class _LpX21LineStatusTimeOut_Type(Unsigned32):
    """Custom type lpX21LineStatusTimeOut based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 20000),
    )


_LpX21LineStatusTimeOut_Type.__name__ = "Unsigned32"
_LpX21LineStatusTimeOut_Object = MibTableColumn
lpX21LineStatusTimeOut = _LpX21LineStatusTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 4),
    _LpX21LineStatusTimeOut_Type()
)
lpX21LineStatusTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21LineStatusTimeOut.setStatus("mandatory")


class _LpX21LineSpeed_Type(Unsigned32):
    """Custom type lpX21LineSpeed based on Unsigned32"""
    defaultValue = 192000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 7680000),
    )


_LpX21LineSpeed_Type.__name__ = "Unsigned32"
_LpX21LineSpeed_Object = MibTableColumn
lpX21LineSpeed = _LpX21LineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 5),
    _LpX21LineSpeed_Type()
)
lpX21LineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21LineSpeed.setStatus("mandatory")


class _LpX21ClockingSource_Type(Integer32):
    """Custom type lpX21ClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("module", 1))
    )


_LpX21ClockingSource_Type.__name__ = "Integer32"
_LpX21ClockingSource_Object = MibTableColumn
lpX21ClockingSource = _LpX21ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 6),
    _LpX21ClockingSource_Type()
)
lpX21ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21ClockingSource.setStatus("mandatory")


class _LpX21DteDataClockSource_Type(Integer32):
    """Custom type lpX21DteDataClockSource based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromDce", 0),
          ("fromDte", 2))
    )


_LpX21DteDataClockSource_Type.__name__ = "Integer32"
_LpX21DteDataClockSource_Object = MibTableColumn
lpX21DteDataClockSource = _LpX21DteDataClockSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 7),
    _LpX21DteDataClockSource_Type()
)
lpX21DteDataClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21DteDataClockSource.setStatus("mandatory")


class _LpX21LineTerminationRequired_Type(Integer32):
    """Custom type lpX21LineTerminationRequired based on Integer32"""
    defaultValue = 1

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


_LpX21LineTerminationRequired_Type.__name__ = "Integer32"
_LpX21LineTerminationRequired_Object = MibTableColumn
lpX21LineTerminationRequired = _LpX21LineTerminationRequired_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 8),
    _LpX21LineTerminationRequired_Type()
)
lpX21LineTerminationRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21LineTerminationRequired.setStatus("mandatory")
_LpX21ApplicationFramerName_Type = Link
_LpX21ApplicationFramerName_Object = MibTableColumn
lpX21ApplicationFramerName = _LpX21ApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 9),
    _LpX21ApplicationFramerName_Type()
)
lpX21ApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21ApplicationFramerName.setStatus("mandatory")


class _LpX21EnableDynamicSpeed_Type(Integer32):
    """Custom type lpX21EnableDynamicSpeed based on Integer32"""
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


_LpX21EnableDynamicSpeed_Type.__name__ = "Integer32"
_LpX21EnableDynamicSpeed_Object = MibTableColumn
lpX21EnableDynamicSpeed = _LpX21EnableDynamicSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 10, 1, 10),
    _LpX21EnableDynamicSpeed_Type()
)
lpX21EnableDynamicSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21EnableDynamicSpeed.setStatus("mandatory")
_LpX21CidDataTable_Object = MibTable
lpX21CidDataTable = _LpX21CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 11)
)
if mibBuilder.loadTexts:
    lpX21CidDataTable.setStatus("mandatory")
_LpX21CidDataEntry_Object = MibTableRow
lpX21CidDataEntry = _LpX21CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 11, 1)
)
lpX21CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21CidDataEntry.setStatus("mandatory")


class _LpX21CustomerIdentifier_Type(Unsigned32):
    """Custom type lpX21CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpX21CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpX21CustomerIdentifier_Object = MibTableColumn
lpX21CustomerIdentifier = _LpX21CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 11, 1, 1),
    _LpX21CustomerIdentifier_Type()
)
lpX21CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21CustomerIdentifier.setStatus("mandatory")
_LpX21AdminInfoTable_Object = MibTable
lpX21AdminInfoTable = _LpX21AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 12)
)
if mibBuilder.loadTexts:
    lpX21AdminInfoTable.setStatus("mandatory")
_LpX21AdminInfoEntry_Object = MibTableRow
lpX21AdminInfoEntry = _LpX21AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 12, 1)
)
lpX21AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21AdminInfoEntry.setStatus("mandatory")


class _LpX21Vendor_Type(AsciiString):
    """Custom type lpX21Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpX21Vendor_Type.__name__ = "AsciiString"
_LpX21Vendor_Object = MibTableColumn
lpX21Vendor = _LpX21Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 12, 1, 1),
    _LpX21Vendor_Type()
)
lpX21Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21Vendor.setStatus("mandatory")


class _LpX21CommentText_Type(AsciiString):
    """Custom type lpX21CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpX21CommentText_Type.__name__ = "AsciiString"
_LpX21CommentText_Object = MibTableColumn
lpX21CommentText = _LpX21CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 12, 1, 2),
    _LpX21CommentText_Type()
)
lpX21CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21CommentText.setStatus("mandatory")
_LpX21IfEntryTable_Object = MibTable
lpX21IfEntryTable = _LpX21IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 13)
)
if mibBuilder.loadTexts:
    lpX21IfEntryTable.setStatus("mandatory")
_LpX21IfEntryEntry_Object = MibTableRow
lpX21IfEntryEntry = _LpX21IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 13, 1)
)
lpX21IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21IfEntryEntry.setStatus("mandatory")


class _LpX21IfAdminStatus_Type(Integer32):
    """Custom type lpX21IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpX21IfAdminStatus_Type.__name__ = "Integer32"
_LpX21IfAdminStatus_Object = MibTableColumn
lpX21IfAdminStatus = _LpX21IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 13, 1, 1),
    _LpX21IfAdminStatus_Type()
)
lpX21IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpX21IfAdminStatus.setStatus("mandatory")


class _LpX21IfIndex_Type(InterfaceIndex):
    """Custom type lpX21IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpX21IfIndex_Type.__name__ = "InterfaceIndex"
_LpX21IfIndex_Object = MibTableColumn
lpX21IfIndex = _LpX21IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 13, 1, 2),
    _LpX21IfIndex_Type()
)
lpX21IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21IfIndex.setStatus("mandatory")
_LpX21OperStatusTable_Object = MibTable
lpX21OperStatusTable = _LpX21OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 14)
)
if mibBuilder.loadTexts:
    lpX21OperStatusTable.setStatus("mandatory")
_LpX21OperStatusEntry_Object = MibTableRow
lpX21OperStatusEntry = _LpX21OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 14, 1)
)
lpX21OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21OperStatusEntry.setStatus("mandatory")


class _LpX21SnmpOperStatus_Type(Integer32):
    """Custom type lpX21SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpX21SnmpOperStatus_Type.__name__ = "Integer32"
_LpX21SnmpOperStatus_Object = MibTableColumn
lpX21SnmpOperStatus = _LpX21SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 14, 1, 1),
    _LpX21SnmpOperStatus_Type()
)
lpX21SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21SnmpOperStatus.setStatus("mandatory")
_LpX21StateTable_Object = MibTable
lpX21StateTable = _LpX21StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15)
)
if mibBuilder.loadTexts:
    lpX21StateTable.setStatus("mandatory")
_LpX21StateEntry_Object = MibTableRow
lpX21StateEntry = _LpX21StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1)
)
lpX21StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21StateEntry.setStatus("mandatory")


class _LpX21AdminState_Type(Integer32):
    """Custom type lpX21AdminState based on Integer32"""
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


_LpX21AdminState_Type.__name__ = "Integer32"
_LpX21AdminState_Object = MibTableColumn
lpX21AdminState = _LpX21AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 1),
    _LpX21AdminState_Type()
)
lpX21AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21AdminState.setStatus("mandatory")


class _LpX21OperationalState_Type(Integer32):
    """Custom type lpX21OperationalState based on Integer32"""
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


_LpX21OperationalState_Type.__name__ = "Integer32"
_LpX21OperationalState_Object = MibTableColumn
lpX21OperationalState = _LpX21OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 2),
    _LpX21OperationalState_Type()
)
lpX21OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21OperationalState.setStatus("mandatory")


class _LpX21UsageState_Type(Integer32):
    """Custom type lpX21UsageState based on Integer32"""
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


_LpX21UsageState_Type.__name__ = "Integer32"
_LpX21UsageState_Object = MibTableColumn
lpX21UsageState = _LpX21UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 3),
    _LpX21UsageState_Type()
)
lpX21UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21UsageState.setStatus("mandatory")


class _LpX21AvailabilityStatus_Type(OctetString):
    """Custom type lpX21AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpX21AvailabilityStatus_Type.__name__ = "OctetString"
_LpX21AvailabilityStatus_Object = MibTableColumn
lpX21AvailabilityStatus = _LpX21AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 4),
    _LpX21AvailabilityStatus_Type()
)
lpX21AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21AvailabilityStatus.setStatus("mandatory")


class _LpX21ProceduralStatus_Type(OctetString):
    """Custom type lpX21ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpX21ProceduralStatus_Type.__name__ = "OctetString"
_LpX21ProceduralStatus_Object = MibTableColumn
lpX21ProceduralStatus = _LpX21ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 5),
    _LpX21ProceduralStatus_Type()
)
lpX21ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21ProceduralStatus.setStatus("mandatory")


class _LpX21ControlStatus_Type(OctetString):
    """Custom type lpX21ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpX21ControlStatus_Type.__name__ = "OctetString"
_LpX21ControlStatus_Object = MibTableColumn
lpX21ControlStatus = _LpX21ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 6),
    _LpX21ControlStatus_Type()
)
lpX21ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21ControlStatus.setStatus("mandatory")


class _LpX21AlarmStatus_Type(OctetString):
    """Custom type lpX21AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpX21AlarmStatus_Type.__name__ = "OctetString"
_LpX21AlarmStatus_Object = MibTableColumn
lpX21AlarmStatus = _LpX21AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 7),
    _LpX21AlarmStatus_Type()
)
lpX21AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21AlarmStatus.setStatus("mandatory")


class _LpX21StandbyStatus_Type(Integer32):
    """Custom type lpX21StandbyStatus based on Integer32"""
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


_LpX21StandbyStatus_Type.__name__ = "Integer32"
_LpX21StandbyStatus_Object = MibTableColumn
lpX21StandbyStatus = _LpX21StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 8),
    _LpX21StandbyStatus_Type()
)
lpX21StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21StandbyStatus.setStatus("mandatory")


class _LpX21UnknownStatus_Type(Integer32):
    """Custom type lpX21UnknownStatus based on Integer32"""
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


_LpX21UnknownStatus_Type.__name__ = "Integer32"
_LpX21UnknownStatus_Object = MibTableColumn
lpX21UnknownStatus = _LpX21UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 15, 1, 9),
    _LpX21UnknownStatus_Type()
)
lpX21UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21UnknownStatus.setStatus("mandatory")
_LpX21OperTable_Object = MibTable
lpX21OperTable = _LpX21OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 16)
)
if mibBuilder.loadTexts:
    lpX21OperTable.setStatus("mandatory")
_LpX21OperEntry_Object = MibTableRow
lpX21OperEntry = _LpX21OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 16, 1)
)
lpX21OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpX21Index"),
)
if mibBuilder.loadTexts:
    lpX21OperEntry.setStatus("mandatory")


class _LpX21ActualLinkMode_Type(Integer32):
    """Custom type lpX21ActualLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dce", 128),
          ("dte", 0))
    )


_LpX21ActualLinkMode_Type.__name__ = "Integer32"
_LpX21ActualLinkMode_Object = MibTableColumn
lpX21ActualLinkMode = _LpX21ActualLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 16, 1, 1),
    _LpX21ActualLinkMode_Type()
)
lpX21ActualLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21ActualLinkMode.setStatus("mandatory")


class _LpX21LineState_Type(OctetString):
    """Custom type lpX21LineState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpX21LineState_Type.__name__ = "OctetString"
_LpX21LineState_Object = MibTableColumn
lpX21LineState = _LpX21LineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 16, 1, 2),
    _LpX21LineState_Type()
)
lpX21LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21LineState.setStatus("mandatory")


class _LpX21ActualTxLineSpeed_Type(Gauge32):
    """Custom type lpX21ActualTxLineSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpX21ActualTxLineSpeed_Type.__name__ = "Gauge32"
_LpX21ActualTxLineSpeed_Object = MibTableColumn
lpX21ActualTxLineSpeed = _LpX21ActualTxLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 16, 1, 3),
    _LpX21ActualTxLineSpeed_Type()
)
lpX21ActualTxLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21ActualTxLineSpeed.setStatus("mandatory")


class _LpX21ActualRxLineSpeed_Type(Gauge32):
    """Custom type lpX21ActualRxLineSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpX21ActualRxLineSpeed_Type.__name__ = "Gauge32"
_LpX21ActualRxLineSpeed_Object = MibTableColumn
lpX21ActualRxLineSpeed = _LpX21ActualRxLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 16, 1, 4),
    _LpX21ActualRxLineSpeed_Type()
)
lpX21ActualRxLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21ActualRxLineSpeed.setStatus("mandatory")
_LpX21DataXferStateChanges_Type = Counter32
_LpX21DataXferStateChanges_Object = MibTableColumn
lpX21DataXferStateChanges = _LpX21DataXferStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 10, 16, 1, 5),
    _LpX21DataXferStateChanges_Type()
)
lpX21DataXferStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpX21DataXferStateChanges.setStatus("mandatory")
_LpSonet_ObjectIdentity = ObjectIdentity
lpSonet = _LpSonet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14)
)
_LpSonetRowStatusTable_Object = MibTable
lpSonetRowStatusTable = _LpSonetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 1)
)
if mibBuilder.loadTexts:
    lpSonetRowStatusTable.setStatus("mandatory")
_LpSonetRowStatusEntry_Object = MibTableRow
lpSonetRowStatusEntry = _LpSonetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 1, 1)
)
lpSonetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetRowStatusEntry.setStatus("mandatory")
_LpSonetRowStatus_Type = RowStatus
_LpSonetRowStatus_Object = MibTableColumn
lpSonetRowStatus = _LpSonetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 1, 1, 1),
    _LpSonetRowStatus_Type()
)
lpSonetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetRowStatus.setStatus("mandatory")
_LpSonetComponentName_Type = DisplayString
_LpSonetComponentName_Object = MibTableColumn
lpSonetComponentName = _LpSonetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 1, 1, 2),
    _LpSonetComponentName_Type()
)
lpSonetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetComponentName.setStatus("mandatory")
_LpSonetStorageType_Type = StorageType
_LpSonetStorageType_Object = MibTableColumn
lpSonetStorageType = _LpSonetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 1, 1, 4),
    _LpSonetStorageType_Type()
)
lpSonetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetStorageType.setStatus("mandatory")


class _LpSonetIndex_Type(Integer32):
    """Custom type lpSonetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LpSonetIndex_Type.__name__ = "Integer32"
_LpSonetIndex_Object = MibTableColumn
lpSonetIndex = _LpSonetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 1, 1, 10),
    _LpSonetIndex_Type()
)
lpSonetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSonetIndex.setStatus("mandatory")
_LpSonetPath_ObjectIdentity = ObjectIdentity
lpSonetPath = _LpSonetPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2)
)
_LpSonetPathRowStatusTable_Object = MibTable
lpSonetPathRowStatusTable = _LpSonetPathRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 1)
)
if mibBuilder.loadTexts:
    lpSonetPathRowStatusTable.setStatus("mandatory")
_LpSonetPathRowStatusEntry_Object = MibTableRow
lpSonetPathRowStatusEntry = _LpSonetPathRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 1, 1)
)
lpSonetPathRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathRowStatusEntry.setStatus("mandatory")
_LpSonetPathRowStatus_Type = RowStatus
_LpSonetPathRowStatus_Object = MibTableColumn
lpSonetPathRowStatus = _LpSonetPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 1, 1, 1),
    _LpSonetPathRowStatus_Type()
)
lpSonetPathRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetPathRowStatus.setStatus("mandatory")
_LpSonetPathComponentName_Type = DisplayString
_LpSonetPathComponentName_Object = MibTableColumn
lpSonetPathComponentName = _LpSonetPathComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 1, 1, 2),
    _LpSonetPathComponentName_Type()
)
lpSonetPathComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathComponentName.setStatus("mandatory")
_LpSonetPathStorageType_Type = StorageType
_LpSonetPathStorageType_Object = MibTableColumn
lpSonetPathStorageType = _LpSonetPathStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 1, 1, 4),
    _LpSonetPathStorageType_Type()
)
lpSonetPathStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathStorageType.setStatus("mandatory")


class _LpSonetPathIndex_Type(Integer32):
    """Custom type lpSonetPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LpSonetPathIndex_Type.__name__ = "Integer32"
_LpSonetPathIndex_Object = MibTableColumn
lpSonetPathIndex = _LpSonetPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 1, 1, 10),
    _LpSonetPathIndex_Type()
)
lpSonetPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSonetPathIndex.setStatus("mandatory")
_LpSonetPathCell_ObjectIdentity = ObjectIdentity
lpSonetPathCell = _LpSonetPathCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2)
)
_LpSonetPathCellRowStatusTable_Object = MibTable
lpSonetPathCellRowStatusTable = _LpSonetPathCellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpSonetPathCellRowStatusTable.setStatus("mandatory")
_LpSonetPathCellRowStatusEntry_Object = MibTableRow
lpSonetPathCellRowStatusEntry = _LpSonetPathCellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 1, 1)
)
lpSonetPathCellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathCellRowStatusEntry.setStatus("mandatory")
_LpSonetPathCellRowStatus_Type = RowStatus
_LpSonetPathCellRowStatus_Object = MibTableColumn
lpSonetPathCellRowStatus = _LpSonetPathCellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 1, 1, 1),
    _LpSonetPathCellRowStatus_Type()
)
lpSonetPathCellRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellRowStatus.setStatus("mandatory")
_LpSonetPathCellComponentName_Type = DisplayString
_LpSonetPathCellComponentName_Object = MibTableColumn
lpSonetPathCellComponentName = _LpSonetPathCellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 1, 1, 2),
    _LpSonetPathCellComponentName_Type()
)
lpSonetPathCellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellComponentName.setStatus("mandatory")
_LpSonetPathCellStorageType_Type = StorageType
_LpSonetPathCellStorageType_Object = MibTableColumn
lpSonetPathCellStorageType = _LpSonetPathCellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 1, 1, 4),
    _LpSonetPathCellStorageType_Type()
)
lpSonetPathCellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellStorageType.setStatus("mandatory")
_LpSonetPathCellIndex_Type = NonReplicated
_LpSonetPathCellIndex_Object = MibTableColumn
lpSonetPathCellIndex = _LpSonetPathCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 1, 1, 10),
    _LpSonetPathCellIndex_Type()
)
lpSonetPathCellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSonetPathCellIndex.setStatus("mandatory")
_LpSonetPathCellProvTable_Object = MibTable
lpSonetPathCellProvTable = _LpSonetPathCellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpSonetPathCellProvTable.setStatus("mandatory")
_LpSonetPathCellProvEntry_Object = MibTableRow
lpSonetPathCellProvEntry = _LpSonetPathCellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 10, 1)
)
lpSonetPathCellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathCellProvEntry.setStatus("mandatory")


class _LpSonetPathCellAlarmActDelay_Type(Unsigned32):
    """Custom type lpSonetPathCellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpSonetPathCellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpSonetPathCellAlarmActDelay_Object = MibTableColumn
lpSonetPathCellAlarmActDelay = _LpSonetPathCellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 10, 1, 1),
    _LpSonetPathCellAlarmActDelay_Type()
)
lpSonetPathCellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetPathCellAlarmActDelay.setStatus("mandatory")


class _LpSonetPathCellScrambleCellPayload_Type(Integer32):
    """Custom type lpSonetPathCellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpSonetPathCellScrambleCellPayload_Type.__name__ = "Integer32"
_LpSonetPathCellScrambleCellPayload_Object = MibTableColumn
lpSonetPathCellScrambleCellPayload = _LpSonetPathCellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 10, 1, 2),
    _LpSonetPathCellScrambleCellPayload_Type()
)
lpSonetPathCellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetPathCellScrambleCellPayload.setStatus("mandatory")


class _LpSonetPathCellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpSonetPathCellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpSonetPathCellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpSonetPathCellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpSonetPathCellCorrectSingleBitHeaderErrors = _LpSonetPathCellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 10, 1, 3),
    _LpSonetPathCellCorrectSingleBitHeaderErrors_Type()
)
lpSonetPathCellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetPathCellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpSonetPathCellOperTable_Object = MibTable
lpSonetPathCellOperTable = _LpSonetPathCellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 11)
)
if mibBuilder.loadTexts:
    lpSonetPathCellOperTable.setStatus("mandatory")
_LpSonetPathCellOperEntry_Object = MibTableRow
lpSonetPathCellOperEntry = _LpSonetPathCellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 11, 1)
)
lpSonetPathCellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathCellOperEntry.setStatus("mandatory")


class _LpSonetPathCellLcdAlarm_Type(Integer32):
    """Custom type lpSonetPathCellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpSonetPathCellLcdAlarm_Type.__name__ = "Integer32"
_LpSonetPathCellLcdAlarm_Object = MibTableColumn
lpSonetPathCellLcdAlarm = _LpSonetPathCellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 11, 1, 1),
    _LpSonetPathCellLcdAlarm_Type()
)
lpSonetPathCellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellLcdAlarm.setStatus("mandatory")
_LpSonetPathCellStatsTable_Object = MibTable
lpSonetPathCellStatsTable = _LpSonetPathCellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 12)
)
if mibBuilder.loadTexts:
    lpSonetPathCellStatsTable.setStatus("mandatory")
_LpSonetPathCellStatsEntry_Object = MibTableRow
lpSonetPathCellStatsEntry = _LpSonetPathCellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 12, 1)
)
lpSonetPathCellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathCellStatsEntry.setStatus("mandatory")
_LpSonetPathCellUncorrectableHecErrors_Type = Counter32
_LpSonetPathCellUncorrectableHecErrors_Object = MibTableColumn
lpSonetPathCellUncorrectableHecErrors = _LpSonetPathCellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 12, 1, 1),
    _LpSonetPathCellUncorrectableHecErrors_Type()
)
lpSonetPathCellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellUncorrectableHecErrors.setStatus("mandatory")
_LpSonetPathCellSevErroredSec_Type = Counter32
_LpSonetPathCellSevErroredSec_Object = MibTableColumn
lpSonetPathCellSevErroredSec = _LpSonetPathCellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 12, 1, 2),
    _LpSonetPathCellSevErroredSec_Type()
)
lpSonetPathCellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellSevErroredSec.setStatus("mandatory")


class _LpSonetPathCellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpSonetPathCellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpSonetPathCellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpSonetPathCellReceiveCellUtilization_Object = MibTableColumn
lpSonetPathCellReceiveCellUtilization = _LpSonetPathCellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 12, 1, 3),
    _LpSonetPathCellReceiveCellUtilization_Type()
)
lpSonetPathCellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellReceiveCellUtilization.setStatus("mandatory")


class _LpSonetPathCellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpSonetPathCellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpSonetPathCellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpSonetPathCellTransmitCellUtilization_Object = MibTableColumn
lpSonetPathCellTransmitCellUtilization = _LpSonetPathCellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 12, 1, 4),
    _LpSonetPathCellTransmitCellUtilization_Type()
)
lpSonetPathCellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellTransmitCellUtilization.setStatus("mandatory")
_LpSonetPathCellCorrectableHeaderErrors_Type = Counter32
_LpSonetPathCellCorrectableHeaderErrors_Object = MibTableColumn
lpSonetPathCellCorrectableHeaderErrors = _LpSonetPathCellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 2, 12, 1, 5),
    _LpSonetPathCellCorrectableHeaderErrors_Type()
)
lpSonetPathCellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathCellCorrectableHeaderErrors.setStatus("mandatory")
_LpSonetPathProvTable_Object = MibTable
lpSonetPathProvTable = _LpSonetPathProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 10)
)
if mibBuilder.loadTexts:
    lpSonetPathProvTable.setStatus("mandatory")
_LpSonetPathProvEntry_Object = MibTableRow
lpSonetPathProvEntry = _LpSonetPathProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 10, 1)
)
lpSonetPathProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathProvEntry.setStatus("mandatory")
_LpSonetPathApplicationFramerName_Type = Link
_LpSonetPathApplicationFramerName_Object = MibTableColumn
lpSonetPathApplicationFramerName = _LpSonetPathApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 10, 1, 1),
    _LpSonetPathApplicationFramerName_Type()
)
lpSonetPathApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetPathApplicationFramerName.setStatus("mandatory")
_LpSonetPathCidDataTable_Object = MibTable
lpSonetPathCidDataTable = _LpSonetPathCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 11)
)
if mibBuilder.loadTexts:
    lpSonetPathCidDataTable.setStatus("mandatory")
_LpSonetPathCidDataEntry_Object = MibTableRow
lpSonetPathCidDataEntry = _LpSonetPathCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 11, 1)
)
lpSonetPathCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathCidDataEntry.setStatus("mandatory")


class _LpSonetPathCustomerIdentifier_Type(Unsigned32):
    """Custom type lpSonetPathCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpSonetPathCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpSonetPathCustomerIdentifier_Object = MibTableColumn
lpSonetPathCustomerIdentifier = _LpSonetPathCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 11, 1, 1),
    _LpSonetPathCustomerIdentifier_Type()
)
lpSonetPathCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetPathCustomerIdentifier.setStatus("mandatory")
_LpSonetPathStateTable_Object = MibTable
lpSonetPathStateTable = _LpSonetPathStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12)
)
if mibBuilder.loadTexts:
    lpSonetPathStateTable.setStatus("mandatory")
_LpSonetPathStateEntry_Object = MibTableRow
lpSonetPathStateEntry = _LpSonetPathStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1)
)
lpSonetPathStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathStateEntry.setStatus("mandatory")


class _LpSonetPathAdminState_Type(Integer32):
    """Custom type lpSonetPathAdminState based on Integer32"""
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


_LpSonetPathAdminState_Type.__name__ = "Integer32"
_LpSonetPathAdminState_Object = MibTableColumn
lpSonetPathAdminState = _LpSonetPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 1),
    _LpSonetPathAdminState_Type()
)
lpSonetPathAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathAdminState.setStatus("mandatory")


class _LpSonetPathOperationalState_Type(Integer32):
    """Custom type lpSonetPathOperationalState based on Integer32"""
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


_LpSonetPathOperationalState_Type.__name__ = "Integer32"
_LpSonetPathOperationalState_Object = MibTableColumn
lpSonetPathOperationalState = _LpSonetPathOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 2),
    _LpSonetPathOperationalState_Type()
)
lpSonetPathOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathOperationalState.setStatus("mandatory")


class _LpSonetPathUsageState_Type(Integer32):
    """Custom type lpSonetPathUsageState based on Integer32"""
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


_LpSonetPathUsageState_Type.__name__ = "Integer32"
_LpSonetPathUsageState_Object = MibTableColumn
lpSonetPathUsageState = _LpSonetPathUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 3),
    _LpSonetPathUsageState_Type()
)
lpSonetPathUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathUsageState.setStatus("mandatory")


class _LpSonetPathAvailabilityStatus_Type(OctetString):
    """Custom type lpSonetPathAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpSonetPathAvailabilityStatus_Type.__name__ = "OctetString"
_LpSonetPathAvailabilityStatus_Object = MibTableColumn
lpSonetPathAvailabilityStatus = _LpSonetPathAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 4),
    _LpSonetPathAvailabilityStatus_Type()
)
lpSonetPathAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathAvailabilityStatus.setStatus("mandatory")


class _LpSonetPathProceduralStatus_Type(OctetString):
    """Custom type lpSonetPathProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSonetPathProceduralStatus_Type.__name__ = "OctetString"
_LpSonetPathProceduralStatus_Object = MibTableColumn
lpSonetPathProceduralStatus = _LpSonetPathProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 5),
    _LpSonetPathProceduralStatus_Type()
)
lpSonetPathProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathProceduralStatus.setStatus("mandatory")


class _LpSonetPathControlStatus_Type(OctetString):
    """Custom type lpSonetPathControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSonetPathControlStatus_Type.__name__ = "OctetString"
_LpSonetPathControlStatus_Object = MibTableColumn
lpSonetPathControlStatus = _LpSonetPathControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 6),
    _LpSonetPathControlStatus_Type()
)
lpSonetPathControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathControlStatus.setStatus("mandatory")


class _LpSonetPathAlarmStatus_Type(OctetString):
    """Custom type lpSonetPathAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSonetPathAlarmStatus_Type.__name__ = "OctetString"
_LpSonetPathAlarmStatus_Object = MibTableColumn
lpSonetPathAlarmStatus = _LpSonetPathAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 7),
    _LpSonetPathAlarmStatus_Type()
)
lpSonetPathAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathAlarmStatus.setStatus("mandatory")


class _LpSonetPathStandbyStatus_Type(Integer32):
    """Custom type lpSonetPathStandbyStatus based on Integer32"""
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


_LpSonetPathStandbyStatus_Type.__name__ = "Integer32"
_LpSonetPathStandbyStatus_Object = MibTableColumn
lpSonetPathStandbyStatus = _LpSonetPathStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 8),
    _LpSonetPathStandbyStatus_Type()
)
lpSonetPathStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathStandbyStatus.setStatus("mandatory")


class _LpSonetPathUnknownStatus_Type(Integer32):
    """Custom type lpSonetPathUnknownStatus based on Integer32"""
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


_LpSonetPathUnknownStatus_Type.__name__ = "Integer32"
_LpSonetPathUnknownStatus_Object = MibTableColumn
lpSonetPathUnknownStatus = _LpSonetPathUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 12, 1, 9),
    _LpSonetPathUnknownStatus_Type()
)
lpSonetPathUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathUnknownStatus.setStatus("mandatory")
_LpSonetPathIfEntryTable_Object = MibTable
lpSonetPathIfEntryTable = _LpSonetPathIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 13)
)
if mibBuilder.loadTexts:
    lpSonetPathIfEntryTable.setStatus("mandatory")
_LpSonetPathIfEntryEntry_Object = MibTableRow
lpSonetPathIfEntryEntry = _LpSonetPathIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 13, 1)
)
lpSonetPathIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathIfEntryEntry.setStatus("mandatory")


class _LpSonetPathIfAdminStatus_Type(Integer32):
    """Custom type lpSonetPathIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSonetPathIfAdminStatus_Type.__name__ = "Integer32"
_LpSonetPathIfAdminStatus_Object = MibTableColumn
lpSonetPathIfAdminStatus = _LpSonetPathIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 13, 1, 1),
    _LpSonetPathIfAdminStatus_Type()
)
lpSonetPathIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetPathIfAdminStatus.setStatus("mandatory")


class _LpSonetPathIfIndex_Type(InterfaceIndex):
    """Custom type lpSonetPathIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpSonetPathIfIndex_Type.__name__ = "InterfaceIndex"
_LpSonetPathIfIndex_Object = MibTableColumn
lpSonetPathIfIndex = _LpSonetPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 13, 1, 2),
    _LpSonetPathIfIndex_Type()
)
lpSonetPathIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathIfIndex.setStatus("mandatory")
_LpSonetPathOperStatusTable_Object = MibTable
lpSonetPathOperStatusTable = _LpSonetPathOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 14)
)
if mibBuilder.loadTexts:
    lpSonetPathOperStatusTable.setStatus("mandatory")
_LpSonetPathOperStatusEntry_Object = MibTableRow
lpSonetPathOperStatusEntry = _LpSonetPathOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 14, 1)
)
lpSonetPathOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathOperStatusEntry.setStatus("mandatory")


class _LpSonetPathSnmpOperStatus_Type(Integer32):
    """Custom type lpSonetPathSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSonetPathSnmpOperStatus_Type.__name__ = "Integer32"
_LpSonetPathSnmpOperStatus_Object = MibTableColumn
lpSonetPathSnmpOperStatus = _LpSonetPathSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 14, 1, 1),
    _LpSonetPathSnmpOperStatus_Type()
)
lpSonetPathSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathSnmpOperStatus.setStatus("mandatory")
_LpSonetPathOperTable_Object = MibTable
lpSonetPathOperTable = _LpSonetPathOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15)
)
if mibBuilder.loadTexts:
    lpSonetPathOperTable.setStatus("mandatory")
_LpSonetPathOperEntry_Object = MibTableRow
lpSonetPathOperEntry = _LpSonetPathOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15, 1)
)
lpSonetPathOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathOperEntry.setStatus("mandatory")


class _LpSonetPathLopAlarm_Type(Integer32):
    """Custom type lpSonetPathLopAlarm based on Integer32"""
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


_LpSonetPathLopAlarm_Type.__name__ = "Integer32"
_LpSonetPathLopAlarm_Object = MibTableColumn
lpSonetPathLopAlarm = _LpSonetPathLopAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15, 1, 1),
    _LpSonetPathLopAlarm_Type()
)
lpSonetPathLopAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathLopAlarm.setStatus("mandatory")


class _LpSonetPathRxAisAlarm_Type(Integer32):
    """Custom type lpSonetPathRxAisAlarm based on Integer32"""
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


_LpSonetPathRxAisAlarm_Type.__name__ = "Integer32"
_LpSonetPathRxAisAlarm_Object = MibTableColumn
lpSonetPathRxAisAlarm = _LpSonetPathRxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15, 1, 2),
    _LpSonetPathRxAisAlarm_Type()
)
lpSonetPathRxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathRxAisAlarm.setStatus("mandatory")


class _LpSonetPathRxRfiAlarm_Type(Integer32):
    """Custom type lpSonetPathRxRfiAlarm based on Integer32"""
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


_LpSonetPathRxRfiAlarm_Type.__name__ = "Integer32"
_LpSonetPathRxRfiAlarm_Object = MibTableColumn
lpSonetPathRxRfiAlarm = _LpSonetPathRxRfiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15, 1, 3),
    _LpSonetPathRxRfiAlarm_Type()
)
lpSonetPathRxRfiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathRxRfiAlarm.setStatus("mandatory")


class _LpSonetPathSignalLabelMismatch_Type(Integer32):
    """Custom type lpSonetPathSignalLabelMismatch based on Integer32"""
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


_LpSonetPathSignalLabelMismatch_Type.__name__ = "Integer32"
_LpSonetPathSignalLabelMismatch_Object = MibTableColumn
lpSonetPathSignalLabelMismatch = _LpSonetPathSignalLabelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15, 1, 4),
    _LpSonetPathSignalLabelMismatch_Type()
)
lpSonetPathSignalLabelMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathSignalLabelMismatch.setStatus("mandatory")


class _LpSonetPathTxAis_Type(Integer32):
    """Custom type lpSonetPathTxAis based on Integer32"""
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


_LpSonetPathTxAis_Type.__name__ = "Integer32"
_LpSonetPathTxAis_Object = MibTableColumn
lpSonetPathTxAis = _LpSonetPathTxAis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15, 1, 5),
    _LpSonetPathTxAis_Type()
)
lpSonetPathTxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathTxAis.setStatus("mandatory")


class _LpSonetPathTxRdi_Type(Integer32):
    """Custom type lpSonetPathTxRdi based on Integer32"""
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


_LpSonetPathTxRdi_Type.__name__ = "Integer32"
_LpSonetPathTxRdi_Object = MibTableColumn
lpSonetPathTxRdi = _LpSonetPathTxRdi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 15, 1, 6),
    _LpSonetPathTxRdi_Type()
)
lpSonetPathTxRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathTxRdi.setStatus("mandatory")
_LpSonetPathStatsTable_Object = MibTable
lpSonetPathStatsTable = _LpSonetPathStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16)
)
if mibBuilder.loadTexts:
    lpSonetPathStatsTable.setStatus("mandatory")
_LpSonetPathStatsEntry_Object = MibTableRow
lpSonetPathStatsEntry = _LpSonetPathStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1)
)
lpSonetPathStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetPathIndex"),
)
if mibBuilder.loadTexts:
    lpSonetPathStatsEntry.setStatus("mandatory")
_LpSonetPathPathErrorFreeSec_Type = Counter32
_LpSonetPathPathErrorFreeSec_Object = MibTableColumn
lpSonetPathPathErrorFreeSec = _LpSonetPathPathErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 1),
    _LpSonetPathPathErrorFreeSec_Type()
)
lpSonetPathPathErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathPathErrorFreeSec.setStatus("mandatory")
_LpSonetPathPathCodeViolations_Type = Counter32
_LpSonetPathPathCodeViolations_Object = MibTableColumn
lpSonetPathPathCodeViolations = _LpSonetPathPathCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 2),
    _LpSonetPathPathCodeViolations_Type()
)
lpSonetPathPathCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathPathCodeViolations.setStatus("mandatory")
_LpSonetPathPathErroredSec_Type = Counter32
_LpSonetPathPathErroredSec_Object = MibTableColumn
lpSonetPathPathErroredSec = _LpSonetPathPathErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 3),
    _LpSonetPathPathErroredSec_Type()
)
lpSonetPathPathErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathPathErroredSec.setStatus("mandatory")
_LpSonetPathPathSevErroredSec_Type = Counter32
_LpSonetPathPathSevErroredSec_Object = MibTableColumn
lpSonetPathPathSevErroredSec = _LpSonetPathPathSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 4),
    _LpSonetPathPathSevErroredSec_Type()
)
lpSonetPathPathSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathPathSevErroredSec.setStatus("mandatory")
_LpSonetPathPathAisLopSec_Type = Counter32
_LpSonetPathPathAisLopSec_Object = MibTableColumn
lpSonetPathPathAisLopSec = _LpSonetPathPathAisLopSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 5),
    _LpSonetPathPathAisLopSec_Type()
)
lpSonetPathPathAisLopSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathPathAisLopSec.setStatus("mandatory")
_LpSonetPathPathUnavailSec_Type = Counter32
_LpSonetPathPathUnavailSec_Object = MibTableColumn
lpSonetPathPathUnavailSec = _LpSonetPathPathUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 6),
    _LpSonetPathPathUnavailSec_Type()
)
lpSonetPathPathUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathPathUnavailSec.setStatus("mandatory")
_LpSonetPathPathFailures_Type = Counter32
_LpSonetPathPathFailures_Object = MibTableColumn
lpSonetPathPathFailures = _LpSonetPathPathFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 7),
    _LpSonetPathPathFailures_Type()
)
lpSonetPathPathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathPathFailures.setStatus("mandatory")
_LpSonetPathFarEndPathErrorFreeSec_Type = Counter32
_LpSonetPathFarEndPathErrorFreeSec_Object = MibTableColumn
lpSonetPathFarEndPathErrorFreeSec = _LpSonetPathFarEndPathErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 8),
    _LpSonetPathFarEndPathErrorFreeSec_Type()
)
lpSonetPathFarEndPathErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathFarEndPathErrorFreeSec.setStatus("mandatory")
_LpSonetPathFarEndPathCodeViolations_Type = Counter32
_LpSonetPathFarEndPathCodeViolations_Object = MibTableColumn
lpSonetPathFarEndPathCodeViolations = _LpSonetPathFarEndPathCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 9),
    _LpSonetPathFarEndPathCodeViolations_Type()
)
lpSonetPathFarEndPathCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathFarEndPathCodeViolations.setStatus("mandatory")
_LpSonetPathFarEndPathErroredSec_Type = Counter32
_LpSonetPathFarEndPathErroredSec_Object = MibTableColumn
lpSonetPathFarEndPathErroredSec = _LpSonetPathFarEndPathErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 10),
    _LpSonetPathFarEndPathErroredSec_Type()
)
lpSonetPathFarEndPathErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathFarEndPathErroredSec.setStatus("mandatory")
_LpSonetPathFarEndPathSevErroredSec_Type = Counter32
_LpSonetPathFarEndPathSevErroredSec_Object = MibTableColumn
lpSonetPathFarEndPathSevErroredSec = _LpSonetPathFarEndPathSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 11),
    _LpSonetPathFarEndPathSevErroredSec_Type()
)
lpSonetPathFarEndPathSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathFarEndPathSevErroredSec.setStatus("mandatory")
_LpSonetPathFarEndPathAisLopSec_Type = Counter32
_LpSonetPathFarEndPathAisLopSec_Object = MibTableColumn
lpSonetPathFarEndPathAisLopSec = _LpSonetPathFarEndPathAisLopSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 12),
    _LpSonetPathFarEndPathAisLopSec_Type()
)
lpSonetPathFarEndPathAisLopSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathFarEndPathAisLopSec.setStatus("mandatory")
_LpSonetPathFarEndPathUnavailSec_Type = Counter32
_LpSonetPathFarEndPathUnavailSec_Object = MibTableColumn
lpSonetPathFarEndPathUnavailSec = _LpSonetPathFarEndPathUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 13),
    _LpSonetPathFarEndPathUnavailSec_Type()
)
lpSonetPathFarEndPathUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathFarEndPathUnavailSec.setStatus("mandatory")
_LpSonetPathFarEndPathFailures_Type = Counter32
_LpSonetPathFarEndPathFailures_Object = MibTableColumn
lpSonetPathFarEndPathFailures = _LpSonetPathFarEndPathFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 2, 16, 1, 14),
    _LpSonetPathFarEndPathFailures_Type()
)
lpSonetPathFarEndPathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetPathFarEndPathFailures.setStatus("mandatory")
_LpSonetTest_ObjectIdentity = ObjectIdentity
lpSonetTest = _LpSonetTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3)
)
_LpSonetTestRowStatusTable_Object = MibTable
lpSonetTestRowStatusTable = _LpSonetTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 1)
)
if mibBuilder.loadTexts:
    lpSonetTestRowStatusTable.setStatus("mandatory")
_LpSonetTestRowStatusEntry_Object = MibTableRow
lpSonetTestRowStatusEntry = _LpSonetTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 1, 1)
)
lpSonetTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetTestIndex"),
)
if mibBuilder.loadTexts:
    lpSonetTestRowStatusEntry.setStatus("mandatory")
_LpSonetTestRowStatus_Type = RowStatus
_LpSonetTestRowStatus_Object = MibTableColumn
lpSonetTestRowStatus = _LpSonetTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 1, 1, 1),
    _LpSonetTestRowStatus_Type()
)
lpSonetTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestRowStatus.setStatus("mandatory")
_LpSonetTestComponentName_Type = DisplayString
_LpSonetTestComponentName_Object = MibTableColumn
lpSonetTestComponentName = _LpSonetTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 1, 1, 2),
    _LpSonetTestComponentName_Type()
)
lpSonetTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestComponentName.setStatus("mandatory")
_LpSonetTestStorageType_Type = StorageType
_LpSonetTestStorageType_Object = MibTableColumn
lpSonetTestStorageType = _LpSonetTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 1, 1, 4),
    _LpSonetTestStorageType_Type()
)
lpSonetTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestStorageType.setStatus("mandatory")
_LpSonetTestIndex_Type = NonReplicated
_LpSonetTestIndex_Object = MibTableColumn
lpSonetTestIndex = _LpSonetTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 1, 1, 10),
    _LpSonetTestIndex_Type()
)
lpSonetTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSonetTestIndex.setStatus("mandatory")
_LpSonetTestStateTable_Object = MibTable
lpSonetTestStateTable = _LpSonetTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 10)
)
if mibBuilder.loadTexts:
    lpSonetTestStateTable.setStatus("mandatory")
_LpSonetTestStateEntry_Object = MibTableRow
lpSonetTestStateEntry = _LpSonetTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 10, 1)
)
lpSonetTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetTestIndex"),
)
if mibBuilder.loadTexts:
    lpSonetTestStateEntry.setStatus("mandatory")


class _LpSonetTestAdminState_Type(Integer32):
    """Custom type lpSonetTestAdminState based on Integer32"""
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


_LpSonetTestAdminState_Type.__name__ = "Integer32"
_LpSonetTestAdminState_Object = MibTableColumn
lpSonetTestAdminState = _LpSonetTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 10, 1, 1),
    _LpSonetTestAdminState_Type()
)
lpSonetTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestAdminState.setStatus("mandatory")


class _LpSonetTestOperationalState_Type(Integer32):
    """Custom type lpSonetTestOperationalState based on Integer32"""
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


_LpSonetTestOperationalState_Type.__name__ = "Integer32"
_LpSonetTestOperationalState_Object = MibTableColumn
lpSonetTestOperationalState = _LpSonetTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 10, 1, 2),
    _LpSonetTestOperationalState_Type()
)
lpSonetTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestOperationalState.setStatus("mandatory")


class _LpSonetTestUsageState_Type(Integer32):
    """Custom type lpSonetTestUsageState based on Integer32"""
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


_LpSonetTestUsageState_Type.__name__ = "Integer32"
_LpSonetTestUsageState_Object = MibTableColumn
lpSonetTestUsageState = _LpSonetTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 10, 1, 3),
    _LpSonetTestUsageState_Type()
)
lpSonetTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestUsageState.setStatus("mandatory")
_LpSonetTestSetupTable_Object = MibTable
lpSonetTestSetupTable = _LpSonetTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11)
)
if mibBuilder.loadTexts:
    lpSonetTestSetupTable.setStatus("mandatory")
_LpSonetTestSetupEntry_Object = MibTableRow
lpSonetTestSetupEntry = _LpSonetTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1)
)
lpSonetTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetTestIndex"),
)
if mibBuilder.loadTexts:
    lpSonetTestSetupEntry.setStatus("mandatory")


class _LpSonetTestPurpose_Type(AsciiString):
    """Custom type lpSonetTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpSonetTestPurpose_Type.__name__ = "AsciiString"
_LpSonetTestPurpose_Object = MibTableColumn
lpSonetTestPurpose = _LpSonetTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 1),
    _LpSonetTestPurpose_Type()
)
lpSonetTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestPurpose.setStatus("mandatory")


class _LpSonetTestType_Type(Integer32):
    """Custom type lpSonetTestType based on Integer32"""
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


_LpSonetTestType_Type.__name__ = "Integer32"
_LpSonetTestType_Object = MibTableColumn
lpSonetTestType = _LpSonetTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 2),
    _LpSonetTestType_Type()
)
lpSonetTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestType.setStatus("mandatory")


class _LpSonetTestFrmSize_Type(Unsigned32):
    """Custom type lpSonetTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpSonetTestFrmSize_Type.__name__ = "Unsigned32"
_LpSonetTestFrmSize_Object = MibTableColumn
lpSonetTestFrmSize = _LpSonetTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 3),
    _LpSonetTestFrmSize_Type()
)
lpSonetTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestFrmSize.setStatus("mandatory")


class _LpSonetTestFrmPatternType_Type(Integer32):
    """Custom type lpSonetTestFrmPatternType based on Integer32"""
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


_LpSonetTestFrmPatternType_Type.__name__ = "Integer32"
_LpSonetTestFrmPatternType_Object = MibTableColumn
lpSonetTestFrmPatternType = _LpSonetTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 4),
    _LpSonetTestFrmPatternType_Type()
)
lpSonetTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestFrmPatternType.setStatus("mandatory")


class _LpSonetTestCustomizedPattern_Type(Hex):
    """Custom type lpSonetTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpSonetTestCustomizedPattern_Type.__name__ = "Hex"
_LpSonetTestCustomizedPattern_Object = MibTableColumn
lpSonetTestCustomizedPattern = _LpSonetTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 5),
    _LpSonetTestCustomizedPattern_Type()
)
lpSonetTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestCustomizedPattern.setStatus("mandatory")


class _LpSonetTestDataStartDelay_Type(Unsigned32):
    """Custom type lpSonetTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpSonetTestDataStartDelay_Type.__name__ = "Unsigned32"
_LpSonetTestDataStartDelay_Object = MibTableColumn
lpSonetTestDataStartDelay = _LpSonetTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 6),
    _LpSonetTestDataStartDelay_Type()
)
lpSonetTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestDataStartDelay.setStatus("mandatory")


class _LpSonetTestDisplayInterval_Type(Unsigned32):
    """Custom type lpSonetTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpSonetTestDisplayInterval_Type.__name__ = "Unsigned32"
_LpSonetTestDisplayInterval_Object = MibTableColumn
lpSonetTestDisplayInterval = _LpSonetTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 7),
    _LpSonetTestDisplayInterval_Type()
)
lpSonetTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestDisplayInterval.setStatus("mandatory")


class _LpSonetTestDuration_Type(Unsigned32):
    """Custom type lpSonetTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpSonetTestDuration_Type.__name__ = "Unsigned32"
_LpSonetTestDuration_Object = MibTableColumn
lpSonetTestDuration = _LpSonetTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 11, 1, 8),
    _LpSonetTestDuration_Type()
)
lpSonetTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetTestDuration.setStatus("mandatory")
_LpSonetTestResultsTable_Object = MibTable
lpSonetTestResultsTable = _LpSonetTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12)
)
if mibBuilder.loadTexts:
    lpSonetTestResultsTable.setStatus("mandatory")
_LpSonetTestResultsEntry_Object = MibTableRow
lpSonetTestResultsEntry = _LpSonetTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1)
)
lpSonetTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetTestIndex"),
)
if mibBuilder.loadTexts:
    lpSonetTestResultsEntry.setStatus("mandatory")
_LpSonetTestElapsedTime_Type = Counter32
_LpSonetTestElapsedTime_Object = MibTableColumn
lpSonetTestElapsedTime = _LpSonetTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 1),
    _LpSonetTestElapsedTime_Type()
)
lpSonetTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestElapsedTime.setStatus("mandatory")


class _LpSonetTestTimeRemaining_Type(Unsigned32):
    """Custom type lpSonetTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpSonetTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpSonetTestTimeRemaining_Object = MibTableColumn
lpSonetTestTimeRemaining = _LpSonetTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 2),
    _LpSonetTestTimeRemaining_Type()
)
lpSonetTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestTimeRemaining.setStatus("mandatory")


class _LpSonetTestCauseOfTermination_Type(Integer32):
    """Custom type lpSonetTestCauseOfTermination based on Integer32"""
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


_LpSonetTestCauseOfTermination_Type.__name__ = "Integer32"
_LpSonetTestCauseOfTermination_Object = MibTableColumn
lpSonetTestCauseOfTermination = _LpSonetTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 3),
    _LpSonetTestCauseOfTermination_Type()
)
lpSonetTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestCauseOfTermination.setStatus("mandatory")
_LpSonetTestBitsTx_Type = PassportCounter64
_LpSonetTestBitsTx_Object = MibTableColumn
lpSonetTestBitsTx = _LpSonetTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 4),
    _LpSonetTestBitsTx_Type()
)
lpSonetTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestBitsTx.setStatus("mandatory")
_LpSonetTestBytesTx_Type = PassportCounter64
_LpSonetTestBytesTx_Object = MibTableColumn
lpSonetTestBytesTx = _LpSonetTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 5),
    _LpSonetTestBytesTx_Type()
)
lpSonetTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestBytesTx.setStatus("mandatory")
_LpSonetTestFrmTx_Type = PassportCounter64
_LpSonetTestFrmTx_Object = MibTableColumn
lpSonetTestFrmTx = _LpSonetTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 6),
    _LpSonetTestFrmTx_Type()
)
lpSonetTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestFrmTx.setStatus("mandatory")
_LpSonetTestBitsRx_Type = PassportCounter64
_LpSonetTestBitsRx_Object = MibTableColumn
lpSonetTestBitsRx = _LpSonetTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 7),
    _LpSonetTestBitsRx_Type()
)
lpSonetTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestBitsRx.setStatus("mandatory")
_LpSonetTestBytesRx_Type = PassportCounter64
_LpSonetTestBytesRx_Object = MibTableColumn
lpSonetTestBytesRx = _LpSonetTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 8),
    _LpSonetTestBytesRx_Type()
)
lpSonetTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestBytesRx.setStatus("mandatory")
_LpSonetTestFrmRx_Type = PassportCounter64
_LpSonetTestFrmRx_Object = MibTableColumn
lpSonetTestFrmRx = _LpSonetTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 9),
    _LpSonetTestFrmRx_Type()
)
lpSonetTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestFrmRx.setStatus("mandatory")
_LpSonetTestErroredFrmRx_Type = PassportCounter64
_LpSonetTestErroredFrmRx_Object = MibTableColumn
lpSonetTestErroredFrmRx = _LpSonetTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 10),
    _LpSonetTestErroredFrmRx_Type()
)
lpSonetTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestErroredFrmRx.setStatus("mandatory")


class _LpSonetTestBitErrorRate_Type(AsciiString):
    """Custom type lpSonetTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpSonetTestBitErrorRate_Type.__name__ = "AsciiString"
_LpSonetTestBitErrorRate_Object = MibTableColumn
lpSonetTestBitErrorRate = _LpSonetTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 3, 12, 1, 11),
    _LpSonetTestBitErrorRate_Type()
)
lpSonetTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTestBitErrorRate.setStatus("mandatory")
_LpSonetProvTable_Object = MibTable
lpSonetProvTable = _LpSonetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 10)
)
if mibBuilder.loadTexts:
    lpSonetProvTable.setStatus("mandatory")
_LpSonetProvEntry_Object = MibTableRow
lpSonetProvEntry = _LpSonetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 10, 1)
)
lpSonetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetProvEntry.setStatus("mandatory")


class _LpSonetClockingSource_Type(Integer32):
    """Custom type lpSonetClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("local", 0),
          ("module", 2))
    )


_LpSonetClockingSource_Type.__name__ = "Integer32"
_LpSonetClockingSource_Object = MibTableColumn
lpSonetClockingSource = _LpSonetClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 10, 1, 1),
    _LpSonetClockingSource_Type()
)
lpSonetClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetClockingSource.setStatus("mandatory")
_LpSonetCidDataTable_Object = MibTable
lpSonetCidDataTable = _LpSonetCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 11)
)
if mibBuilder.loadTexts:
    lpSonetCidDataTable.setStatus("mandatory")
_LpSonetCidDataEntry_Object = MibTableRow
lpSonetCidDataEntry = _LpSonetCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 11, 1)
)
lpSonetCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetCidDataEntry.setStatus("mandatory")


class _LpSonetCustomerIdentifier_Type(Unsigned32):
    """Custom type lpSonetCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpSonetCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpSonetCustomerIdentifier_Object = MibTableColumn
lpSonetCustomerIdentifier = _LpSonetCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 11, 1, 1),
    _LpSonetCustomerIdentifier_Type()
)
lpSonetCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetCustomerIdentifier.setStatus("mandatory")
_LpSonetAdminInfoTable_Object = MibTable
lpSonetAdminInfoTable = _LpSonetAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 12)
)
if mibBuilder.loadTexts:
    lpSonetAdminInfoTable.setStatus("mandatory")
_LpSonetAdminInfoEntry_Object = MibTableRow
lpSonetAdminInfoEntry = _LpSonetAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 12, 1)
)
lpSonetAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetAdminInfoEntry.setStatus("mandatory")


class _LpSonetVendor_Type(AsciiString):
    """Custom type lpSonetVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpSonetVendor_Type.__name__ = "AsciiString"
_LpSonetVendor_Object = MibTableColumn
lpSonetVendor = _LpSonetVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 12, 1, 1),
    _LpSonetVendor_Type()
)
lpSonetVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetVendor.setStatus("mandatory")


class _LpSonetCommentText_Type(AsciiString):
    """Custom type lpSonetCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpSonetCommentText_Type.__name__ = "AsciiString"
_LpSonetCommentText_Object = MibTableColumn
lpSonetCommentText = _LpSonetCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 12, 1, 2),
    _LpSonetCommentText_Type()
)
lpSonetCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetCommentText.setStatus("mandatory")
_LpSonetIfEntryTable_Object = MibTable
lpSonetIfEntryTable = _LpSonetIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 13)
)
if mibBuilder.loadTexts:
    lpSonetIfEntryTable.setStatus("mandatory")
_LpSonetIfEntryEntry_Object = MibTableRow
lpSonetIfEntryEntry = _LpSonetIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 13, 1)
)
lpSonetIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetIfEntryEntry.setStatus("mandatory")


class _LpSonetIfAdminStatus_Type(Integer32):
    """Custom type lpSonetIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSonetIfAdminStatus_Type.__name__ = "Integer32"
_LpSonetIfAdminStatus_Object = MibTableColumn
lpSonetIfAdminStatus = _LpSonetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 13, 1, 1),
    _LpSonetIfAdminStatus_Type()
)
lpSonetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSonetIfAdminStatus.setStatus("mandatory")


class _LpSonetIfIndex_Type(InterfaceIndex):
    """Custom type lpSonetIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpSonetIfIndex_Type.__name__ = "InterfaceIndex"
_LpSonetIfIndex_Object = MibTableColumn
lpSonetIfIndex = _LpSonetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 13, 1, 2),
    _LpSonetIfIndex_Type()
)
lpSonetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetIfIndex.setStatus("mandatory")
_LpSonetOperStatusTable_Object = MibTable
lpSonetOperStatusTable = _LpSonetOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 14)
)
if mibBuilder.loadTexts:
    lpSonetOperStatusTable.setStatus("mandatory")
_LpSonetOperStatusEntry_Object = MibTableRow
lpSonetOperStatusEntry = _LpSonetOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 14, 1)
)
lpSonetOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetOperStatusEntry.setStatus("mandatory")


class _LpSonetSnmpOperStatus_Type(Integer32):
    """Custom type lpSonetSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSonetSnmpOperStatus_Type.__name__ = "Integer32"
_LpSonetSnmpOperStatus_Object = MibTableColumn
lpSonetSnmpOperStatus = _LpSonetSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 14, 1, 1),
    _LpSonetSnmpOperStatus_Type()
)
lpSonetSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetSnmpOperStatus.setStatus("mandatory")
_LpSonetStateTable_Object = MibTable
lpSonetStateTable = _LpSonetStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15)
)
if mibBuilder.loadTexts:
    lpSonetStateTable.setStatus("mandatory")
_LpSonetStateEntry_Object = MibTableRow
lpSonetStateEntry = _LpSonetStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1)
)
lpSonetStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetStateEntry.setStatus("mandatory")


class _LpSonetAdminState_Type(Integer32):
    """Custom type lpSonetAdminState based on Integer32"""
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


_LpSonetAdminState_Type.__name__ = "Integer32"
_LpSonetAdminState_Object = MibTableColumn
lpSonetAdminState = _LpSonetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 1),
    _LpSonetAdminState_Type()
)
lpSonetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetAdminState.setStatus("mandatory")


class _LpSonetOperationalState_Type(Integer32):
    """Custom type lpSonetOperationalState based on Integer32"""
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


_LpSonetOperationalState_Type.__name__ = "Integer32"
_LpSonetOperationalState_Object = MibTableColumn
lpSonetOperationalState = _LpSonetOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 2),
    _LpSonetOperationalState_Type()
)
lpSonetOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetOperationalState.setStatus("mandatory")


class _LpSonetUsageState_Type(Integer32):
    """Custom type lpSonetUsageState based on Integer32"""
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


_LpSonetUsageState_Type.__name__ = "Integer32"
_LpSonetUsageState_Object = MibTableColumn
lpSonetUsageState = _LpSonetUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 3),
    _LpSonetUsageState_Type()
)
lpSonetUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetUsageState.setStatus("mandatory")


class _LpSonetAvailabilityStatus_Type(OctetString):
    """Custom type lpSonetAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpSonetAvailabilityStatus_Type.__name__ = "OctetString"
_LpSonetAvailabilityStatus_Object = MibTableColumn
lpSonetAvailabilityStatus = _LpSonetAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 4),
    _LpSonetAvailabilityStatus_Type()
)
lpSonetAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetAvailabilityStatus.setStatus("mandatory")


class _LpSonetProceduralStatus_Type(OctetString):
    """Custom type lpSonetProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSonetProceduralStatus_Type.__name__ = "OctetString"
_LpSonetProceduralStatus_Object = MibTableColumn
lpSonetProceduralStatus = _LpSonetProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 5),
    _LpSonetProceduralStatus_Type()
)
lpSonetProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetProceduralStatus.setStatus("mandatory")


class _LpSonetControlStatus_Type(OctetString):
    """Custom type lpSonetControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSonetControlStatus_Type.__name__ = "OctetString"
_LpSonetControlStatus_Object = MibTableColumn
lpSonetControlStatus = _LpSonetControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 6),
    _LpSonetControlStatus_Type()
)
lpSonetControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetControlStatus.setStatus("mandatory")


class _LpSonetAlarmStatus_Type(OctetString):
    """Custom type lpSonetAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSonetAlarmStatus_Type.__name__ = "OctetString"
_LpSonetAlarmStatus_Object = MibTableColumn
lpSonetAlarmStatus = _LpSonetAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 7),
    _LpSonetAlarmStatus_Type()
)
lpSonetAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetAlarmStatus.setStatus("mandatory")


class _LpSonetStandbyStatus_Type(Integer32):
    """Custom type lpSonetStandbyStatus based on Integer32"""
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


_LpSonetStandbyStatus_Type.__name__ = "Integer32"
_LpSonetStandbyStatus_Object = MibTableColumn
lpSonetStandbyStatus = _LpSonetStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 8),
    _LpSonetStandbyStatus_Type()
)
lpSonetStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetStandbyStatus.setStatus("mandatory")


class _LpSonetUnknownStatus_Type(Integer32):
    """Custom type lpSonetUnknownStatus based on Integer32"""
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


_LpSonetUnknownStatus_Type.__name__ = "Integer32"
_LpSonetUnknownStatus_Object = MibTableColumn
lpSonetUnknownStatus = _LpSonetUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 15, 1, 9),
    _LpSonetUnknownStatus_Type()
)
lpSonetUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetUnknownStatus.setStatus("mandatory")
_LpSonetOperTable_Object = MibTable
lpSonetOperTable = _LpSonetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16)
)
if mibBuilder.loadTexts:
    lpSonetOperTable.setStatus("mandatory")
_LpSonetOperEntry_Object = MibTableRow
lpSonetOperEntry = _LpSonetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1)
)
lpSonetOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetOperEntry.setStatus("mandatory")


class _LpSonetLosAlarm_Type(Integer32):
    """Custom type lpSonetLosAlarm based on Integer32"""
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


_LpSonetLosAlarm_Type.__name__ = "Integer32"
_LpSonetLosAlarm_Object = MibTableColumn
lpSonetLosAlarm = _LpSonetLosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1, 1),
    _LpSonetLosAlarm_Type()
)
lpSonetLosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLosAlarm.setStatus("mandatory")


class _LpSonetLofAlarm_Type(Integer32):
    """Custom type lpSonetLofAlarm based on Integer32"""
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


_LpSonetLofAlarm_Type.__name__ = "Integer32"
_LpSonetLofAlarm_Object = MibTableColumn
lpSonetLofAlarm = _LpSonetLofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1, 2),
    _LpSonetLofAlarm_Type()
)
lpSonetLofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLofAlarm.setStatus("mandatory")


class _LpSonetRxAisAlarm_Type(Integer32):
    """Custom type lpSonetRxAisAlarm based on Integer32"""
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


_LpSonetRxAisAlarm_Type.__name__ = "Integer32"
_LpSonetRxAisAlarm_Object = MibTableColumn
lpSonetRxAisAlarm = _LpSonetRxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1, 3),
    _LpSonetRxAisAlarm_Type()
)
lpSonetRxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetRxAisAlarm.setStatus("mandatory")


class _LpSonetRxRfiAlarm_Type(Integer32):
    """Custom type lpSonetRxRfiAlarm based on Integer32"""
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


_LpSonetRxRfiAlarm_Type.__name__ = "Integer32"
_LpSonetRxRfiAlarm_Object = MibTableColumn
lpSonetRxRfiAlarm = _LpSonetRxRfiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1, 4),
    _LpSonetRxRfiAlarm_Type()
)
lpSonetRxRfiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetRxRfiAlarm.setStatus("mandatory")


class _LpSonetTxAis_Type(Integer32):
    """Custom type lpSonetTxAis based on Integer32"""
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


_LpSonetTxAis_Type.__name__ = "Integer32"
_LpSonetTxAis_Object = MibTableColumn
lpSonetTxAis = _LpSonetTxAis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1, 5),
    _LpSonetTxAis_Type()
)
lpSonetTxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTxAis.setStatus("mandatory")


class _LpSonetTxRdi_Type(Integer32):
    """Custom type lpSonetTxRdi based on Integer32"""
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


_LpSonetTxRdi_Type.__name__ = "Integer32"
_LpSonetTxRdi_Object = MibTableColumn
lpSonetTxRdi = _LpSonetTxRdi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1, 6),
    _LpSonetTxRdi_Type()
)
lpSonetTxRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetTxRdi.setStatus("mandatory")


class _LpSonetUnusableTxClockRefAlarm_Type(Integer32):
    """Custom type lpSonetUnusableTxClockRefAlarm based on Integer32"""
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


_LpSonetUnusableTxClockRefAlarm_Type.__name__ = "Integer32"
_LpSonetUnusableTxClockRefAlarm_Object = MibTableColumn
lpSonetUnusableTxClockRefAlarm = _LpSonetUnusableTxClockRefAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 16, 1, 7),
    _LpSonetUnusableTxClockRefAlarm_Type()
)
lpSonetUnusableTxClockRefAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetUnusableTxClockRefAlarm.setStatus("mandatory")
_LpSonetStatsTable_Object = MibTable
lpSonetStatsTable = _LpSonetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17)
)
if mibBuilder.loadTexts:
    lpSonetStatsTable.setStatus("mandatory")
_LpSonetStatsEntry_Object = MibTableRow
lpSonetStatsEntry = _LpSonetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1)
)
lpSonetStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSonetIndex"),
)
if mibBuilder.loadTexts:
    lpSonetStatsEntry.setStatus("mandatory")
_LpSonetRunningTime_Type = Counter32
_LpSonetRunningTime_Object = MibTableColumn
lpSonetRunningTime = _LpSonetRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 1),
    _LpSonetRunningTime_Type()
)
lpSonetRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetRunningTime.setStatus("mandatory")
_LpSonetErrorFreeSec_Type = Counter32
_LpSonetErrorFreeSec_Object = MibTableColumn
lpSonetErrorFreeSec = _LpSonetErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 2),
    _LpSonetErrorFreeSec_Type()
)
lpSonetErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetErrorFreeSec.setStatus("mandatory")
_LpSonetSectCodeViolations_Type = Counter32
_LpSonetSectCodeViolations_Object = MibTableColumn
lpSonetSectCodeViolations = _LpSonetSectCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 3),
    _LpSonetSectCodeViolations_Type()
)
lpSonetSectCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetSectCodeViolations.setStatus("mandatory")
_LpSonetSectErroredSec_Type = Counter32
_LpSonetSectErroredSec_Object = MibTableColumn
lpSonetSectErroredSec = _LpSonetSectErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 4),
    _LpSonetSectErroredSec_Type()
)
lpSonetSectErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetSectErroredSec.setStatus("mandatory")
_LpSonetSectSevErroredSec_Type = Counter32
_LpSonetSectSevErroredSec_Object = MibTableColumn
lpSonetSectSevErroredSec = _LpSonetSectSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 5),
    _LpSonetSectSevErroredSec_Type()
)
lpSonetSectSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetSectSevErroredSec.setStatus("mandatory")
_LpSonetSectLosSec_Type = Counter32
_LpSonetSectLosSec_Object = MibTableColumn
lpSonetSectLosSec = _LpSonetSectLosSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 6),
    _LpSonetSectLosSec_Type()
)
lpSonetSectLosSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetSectLosSec.setStatus("mandatory")
_LpSonetSectSevErroredFrmSec_Type = Counter32
_LpSonetSectSevErroredFrmSec_Object = MibTableColumn
lpSonetSectSevErroredFrmSec = _LpSonetSectSevErroredFrmSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 7),
    _LpSonetSectSevErroredFrmSec_Type()
)
lpSonetSectSevErroredFrmSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetSectSevErroredFrmSec.setStatus("mandatory")
_LpSonetSectFailures_Type = Counter32
_LpSonetSectFailures_Object = MibTableColumn
lpSonetSectFailures = _LpSonetSectFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 8),
    _LpSonetSectFailures_Type()
)
lpSonetSectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetSectFailures.setStatus("mandatory")
_LpSonetLineCodeViolations_Type = Counter32
_LpSonetLineCodeViolations_Object = MibTableColumn
lpSonetLineCodeViolations = _LpSonetLineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 9),
    _LpSonetLineCodeViolations_Type()
)
lpSonetLineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLineCodeViolations.setStatus("mandatory")
_LpSonetLineErroredSec_Type = Counter32
_LpSonetLineErroredSec_Object = MibTableColumn
lpSonetLineErroredSec = _LpSonetLineErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 10),
    _LpSonetLineErroredSec_Type()
)
lpSonetLineErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLineErroredSec.setStatus("mandatory")
_LpSonetLineSevErroredSec_Type = Counter32
_LpSonetLineSevErroredSec_Object = MibTableColumn
lpSonetLineSevErroredSec = _LpSonetLineSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 11),
    _LpSonetLineSevErroredSec_Type()
)
lpSonetLineSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLineSevErroredSec.setStatus("mandatory")
_LpSonetLineAisSec_Type = Counter32
_LpSonetLineAisSec_Object = MibTableColumn
lpSonetLineAisSec = _LpSonetLineAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 12),
    _LpSonetLineAisSec_Type()
)
lpSonetLineAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLineAisSec.setStatus("mandatory")
_LpSonetLineUnavailSec_Type = Counter32
_LpSonetLineUnavailSec_Object = MibTableColumn
lpSonetLineUnavailSec = _LpSonetLineUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 13),
    _LpSonetLineUnavailSec_Type()
)
lpSonetLineUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLineUnavailSec.setStatus("mandatory")
_LpSonetLineFailures_Type = Counter32
_LpSonetLineFailures_Object = MibTableColumn
lpSonetLineFailures = _LpSonetLineFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 14),
    _LpSonetLineFailures_Type()
)
lpSonetLineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetLineFailures.setStatus("mandatory")
_LpSonetFarEndLineErrorFreeSec_Type = Counter32
_LpSonetFarEndLineErrorFreeSec_Object = MibTableColumn
lpSonetFarEndLineErrorFreeSec = _LpSonetFarEndLineErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 15),
    _LpSonetFarEndLineErrorFreeSec_Type()
)
lpSonetFarEndLineErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetFarEndLineErrorFreeSec.setStatus("mandatory")
_LpSonetFarEndLineCodeViolations_Type = Counter32
_LpSonetFarEndLineCodeViolations_Object = MibTableColumn
lpSonetFarEndLineCodeViolations = _LpSonetFarEndLineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 16),
    _LpSonetFarEndLineCodeViolations_Type()
)
lpSonetFarEndLineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetFarEndLineCodeViolations.setStatus("mandatory")
_LpSonetFarEndLineErroredSec_Type = Counter32
_LpSonetFarEndLineErroredSec_Object = MibTableColumn
lpSonetFarEndLineErroredSec = _LpSonetFarEndLineErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 17),
    _LpSonetFarEndLineErroredSec_Type()
)
lpSonetFarEndLineErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetFarEndLineErroredSec.setStatus("mandatory")
_LpSonetFarEndLineSevErroredSec_Type = Counter32
_LpSonetFarEndLineSevErroredSec_Object = MibTableColumn
lpSonetFarEndLineSevErroredSec = _LpSonetFarEndLineSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 18),
    _LpSonetFarEndLineSevErroredSec_Type()
)
lpSonetFarEndLineSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetFarEndLineSevErroredSec.setStatus("mandatory")
_LpSonetFarEndLineAisSec_Type = Counter32
_LpSonetFarEndLineAisSec_Object = MibTableColumn
lpSonetFarEndLineAisSec = _LpSonetFarEndLineAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 19),
    _LpSonetFarEndLineAisSec_Type()
)
lpSonetFarEndLineAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetFarEndLineAisSec.setStatus("mandatory")
_LpSonetFarEndLineUnavailSec_Type = Counter32
_LpSonetFarEndLineUnavailSec_Object = MibTableColumn
lpSonetFarEndLineUnavailSec = _LpSonetFarEndLineUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 20),
    _LpSonetFarEndLineUnavailSec_Type()
)
lpSonetFarEndLineUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetFarEndLineUnavailSec.setStatus("mandatory")
_LpSonetFarEndLineFailures_Type = Counter32
_LpSonetFarEndLineFailures_Object = MibTableColumn
lpSonetFarEndLineFailures = _LpSonetFarEndLineFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 14, 17, 1, 21),
    _LpSonetFarEndLineFailures_Type()
)
lpSonetFarEndLineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSonetFarEndLineFailures.setStatus("mandatory")
_LpSdh_ObjectIdentity = ObjectIdentity
lpSdh = _LpSdh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15)
)
_LpSdhRowStatusTable_Object = MibTable
lpSdhRowStatusTable = _LpSdhRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 1)
)
if mibBuilder.loadTexts:
    lpSdhRowStatusTable.setStatus("mandatory")
_LpSdhRowStatusEntry_Object = MibTableRow
lpSdhRowStatusEntry = _LpSdhRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 1, 1)
)
lpSdhRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhRowStatusEntry.setStatus("mandatory")
_LpSdhRowStatus_Type = RowStatus
_LpSdhRowStatus_Object = MibTableColumn
lpSdhRowStatus = _LpSdhRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 1, 1, 1),
    _LpSdhRowStatus_Type()
)
lpSdhRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhRowStatus.setStatus("mandatory")
_LpSdhComponentName_Type = DisplayString
_LpSdhComponentName_Object = MibTableColumn
lpSdhComponentName = _LpSdhComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 1, 1, 2),
    _LpSdhComponentName_Type()
)
lpSdhComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhComponentName.setStatus("mandatory")
_LpSdhStorageType_Type = StorageType
_LpSdhStorageType_Object = MibTableColumn
lpSdhStorageType = _LpSdhStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 1, 1, 4),
    _LpSdhStorageType_Type()
)
lpSdhStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhStorageType.setStatus("mandatory")


class _LpSdhIndex_Type(Integer32):
    """Custom type lpSdhIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_LpSdhIndex_Type.__name__ = "Integer32"
_LpSdhIndex_Object = MibTableColumn
lpSdhIndex = _LpSdhIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 1, 1, 10),
    _LpSdhIndex_Type()
)
lpSdhIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSdhIndex.setStatus("mandatory")
_LpSdhPath_ObjectIdentity = ObjectIdentity
lpSdhPath = _LpSdhPath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2)
)
_LpSdhPathRowStatusTable_Object = MibTable
lpSdhPathRowStatusTable = _LpSdhPathRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 1)
)
if mibBuilder.loadTexts:
    lpSdhPathRowStatusTable.setStatus("mandatory")
_LpSdhPathRowStatusEntry_Object = MibTableRow
lpSdhPathRowStatusEntry = _LpSdhPathRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 1, 1)
)
lpSdhPathRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathRowStatusEntry.setStatus("mandatory")
_LpSdhPathRowStatus_Type = RowStatus
_LpSdhPathRowStatus_Object = MibTableColumn
lpSdhPathRowStatus = _LpSdhPathRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 1, 1, 1),
    _LpSdhPathRowStatus_Type()
)
lpSdhPathRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhPathRowStatus.setStatus("mandatory")
_LpSdhPathComponentName_Type = DisplayString
_LpSdhPathComponentName_Object = MibTableColumn
lpSdhPathComponentName = _LpSdhPathComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 1, 1, 2),
    _LpSdhPathComponentName_Type()
)
lpSdhPathComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathComponentName.setStatus("mandatory")
_LpSdhPathStorageType_Type = StorageType
_LpSdhPathStorageType_Object = MibTableColumn
lpSdhPathStorageType = _LpSdhPathStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 1, 1, 4),
    _LpSdhPathStorageType_Type()
)
lpSdhPathStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathStorageType.setStatus("mandatory")


class _LpSdhPathIndex_Type(Integer32):
    """Custom type lpSdhPathIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LpSdhPathIndex_Type.__name__ = "Integer32"
_LpSdhPathIndex_Object = MibTableColumn
lpSdhPathIndex = _LpSdhPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 1, 1, 10),
    _LpSdhPathIndex_Type()
)
lpSdhPathIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSdhPathIndex.setStatus("mandatory")
_LpSdhPathCell_ObjectIdentity = ObjectIdentity
lpSdhPathCell = _LpSdhPathCell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2)
)
_LpSdhPathCellRowStatusTable_Object = MibTable
lpSdhPathCellRowStatusTable = _LpSdhPathCellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpSdhPathCellRowStatusTable.setStatus("mandatory")
_LpSdhPathCellRowStatusEntry_Object = MibTableRow
lpSdhPathCellRowStatusEntry = _LpSdhPathCellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 1, 1)
)
lpSdhPathCellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathCellRowStatusEntry.setStatus("mandatory")
_LpSdhPathCellRowStatus_Type = RowStatus
_LpSdhPathCellRowStatus_Object = MibTableColumn
lpSdhPathCellRowStatus = _LpSdhPathCellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 1, 1, 1),
    _LpSdhPathCellRowStatus_Type()
)
lpSdhPathCellRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellRowStatus.setStatus("mandatory")
_LpSdhPathCellComponentName_Type = DisplayString
_LpSdhPathCellComponentName_Object = MibTableColumn
lpSdhPathCellComponentName = _LpSdhPathCellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 1, 1, 2),
    _LpSdhPathCellComponentName_Type()
)
lpSdhPathCellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellComponentName.setStatus("mandatory")
_LpSdhPathCellStorageType_Type = StorageType
_LpSdhPathCellStorageType_Object = MibTableColumn
lpSdhPathCellStorageType = _LpSdhPathCellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 1, 1, 4),
    _LpSdhPathCellStorageType_Type()
)
lpSdhPathCellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellStorageType.setStatus("mandatory")
_LpSdhPathCellIndex_Type = NonReplicated
_LpSdhPathCellIndex_Object = MibTableColumn
lpSdhPathCellIndex = _LpSdhPathCellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 1, 1, 10),
    _LpSdhPathCellIndex_Type()
)
lpSdhPathCellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSdhPathCellIndex.setStatus("mandatory")
_LpSdhPathCellProvTable_Object = MibTable
lpSdhPathCellProvTable = _LpSdhPathCellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpSdhPathCellProvTable.setStatus("mandatory")
_LpSdhPathCellProvEntry_Object = MibTableRow
lpSdhPathCellProvEntry = _LpSdhPathCellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 10, 1)
)
lpSdhPathCellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathCellProvEntry.setStatus("mandatory")


class _LpSdhPathCellAlarmActDelay_Type(Unsigned32):
    """Custom type lpSdhPathCellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpSdhPathCellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpSdhPathCellAlarmActDelay_Object = MibTableColumn
lpSdhPathCellAlarmActDelay = _LpSdhPathCellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 10, 1, 1),
    _LpSdhPathCellAlarmActDelay_Type()
)
lpSdhPathCellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhPathCellAlarmActDelay.setStatus("mandatory")


class _LpSdhPathCellScrambleCellPayload_Type(Integer32):
    """Custom type lpSdhPathCellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpSdhPathCellScrambleCellPayload_Type.__name__ = "Integer32"
_LpSdhPathCellScrambleCellPayload_Object = MibTableColumn
lpSdhPathCellScrambleCellPayload = _LpSdhPathCellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 10, 1, 2),
    _LpSdhPathCellScrambleCellPayload_Type()
)
lpSdhPathCellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhPathCellScrambleCellPayload.setStatus("mandatory")


class _LpSdhPathCellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpSdhPathCellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpSdhPathCellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpSdhPathCellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpSdhPathCellCorrectSingleBitHeaderErrors = _LpSdhPathCellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 10, 1, 3),
    _LpSdhPathCellCorrectSingleBitHeaderErrors_Type()
)
lpSdhPathCellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhPathCellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpSdhPathCellOperTable_Object = MibTable
lpSdhPathCellOperTable = _LpSdhPathCellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 11)
)
if mibBuilder.loadTexts:
    lpSdhPathCellOperTable.setStatus("mandatory")
_LpSdhPathCellOperEntry_Object = MibTableRow
lpSdhPathCellOperEntry = _LpSdhPathCellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 11, 1)
)
lpSdhPathCellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathCellOperEntry.setStatus("mandatory")


class _LpSdhPathCellLcdAlarm_Type(Integer32):
    """Custom type lpSdhPathCellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpSdhPathCellLcdAlarm_Type.__name__ = "Integer32"
_LpSdhPathCellLcdAlarm_Object = MibTableColumn
lpSdhPathCellLcdAlarm = _LpSdhPathCellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 11, 1, 1),
    _LpSdhPathCellLcdAlarm_Type()
)
lpSdhPathCellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellLcdAlarm.setStatus("mandatory")
_LpSdhPathCellStatsTable_Object = MibTable
lpSdhPathCellStatsTable = _LpSdhPathCellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 12)
)
if mibBuilder.loadTexts:
    lpSdhPathCellStatsTable.setStatus("mandatory")
_LpSdhPathCellStatsEntry_Object = MibTableRow
lpSdhPathCellStatsEntry = _LpSdhPathCellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 12, 1)
)
lpSdhPathCellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathCellIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathCellStatsEntry.setStatus("mandatory")
_LpSdhPathCellUncorrectableHecErrors_Type = Counter32
_LpSdhPathCellUncorrectableHecErrors_Object = MibTableColumn
lpSdhPathCellUncorrectableHecErrors = _LpSdhPathCellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 12, 1, 1),
    _LpSdhPathCellUncorrectableHecErrors_Type()
)
lpSdhPathCellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellUncorrectableHecErrors.setStatus("mandatory")
_LpSdhPathCellSevErroredSec_Type = Counter32
_LpSdhPathCellSevErroredSec_Object = MibTableColumn
lpSdhPathCellSevErroredSec = _LpSdhPathCellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 12, 1, 2),
    _LpSdhPathCellSevErroredSec_Type()
)
lpSdhPathCellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellSevErroredSec.setStatus("mandatory")


class _LpSdhPathCellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpSdhPathCellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpSdhPathCellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpSdhPathCellReceiveCellUtilization_Object = MibTableColumn
lpSdhPathCellReceiveCellUtilization = _LpSdhPathCellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 12, 1, 3),
    _LpSdhPathCellReceiveCellUtilization_Type()
)
lpSdhPathCellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellReceiveCellUtilization.setStatus("mandatory")


class _LpSdhPathCellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpSdhPathCellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpSdhPathCellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpSdhPathCellTransmitCellUtilization_Object = MibTableColumn
lpSdhPathCellTransmitCellUtilization = _LpSdhPathCellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 12, 1, 4),
    _LpSdhPathCellTransmitCellUtilization_Type()
)
lpSdhPathCellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellTransmitCellUtilization.setStatus("mandatory")
_LpSdhPathCellCorrectableHeaderErrors_Type = Counter32
_LpSdhPathCellCorrectableHeaderErrors_Object = MibTableColumn
lpSdhPathCellCorrectableHeaderErrors = _LpSdhPathCellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 2, 12, 1, 5),
    _LpSdhPathCellCorrectableHeaderErrors_Type()
)
lpSdhPathCellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathCellCorrectableHeaderErrors.setStatus("mandatory")
_LpSdhPathProvTable_Object = MibTable
lpSdhPathProvTable = _LpSdhPathProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 10)
)
if mibBuilder.loadTexts:
    lpSdhPathProvTable.setStatus("mandatory")
_LpSdhPathProvEntry_Object = MibTableRow
lpSdhPathProvEntry = _LpSdhPathProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 10, 1)
)
lpSdhPathProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathProvEntry.setStatus("mandatory")
_LpSdhPathApplicationFramerName_Type = Link
_LpSdhPathApplicationFramerName_Object = MibTableColumn
lpSdhPathApplicationFramerName = _LpSdhPathApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 10, 1, 1),
    _LpSdhPathApplicationFramerName_Type()
)
lpSdhPathApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhPathApplicationFramerName.setStatus("mandatory")
_LpSdhPathCidDataTable_Object = MibTable
lpSdhPathCidDataTable = _LpSdhPathCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 11)
)
if mibBuilder.loadTexts:
    lpSdhPathCidDataTable.setStatus("mandatory")
_LpSdhPathCidDataEntry_Object = MibTableRow
lpSdhPathCidDataEntry = _LpSdhPathCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 11, 1)
)
lpSdhPathCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathCidDataEntry.setStatus("mandatory")


class _LpSdhPathCustomerIdentifier_Type(Unsigned32):
    """Custom type lpSdhPathCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpSdhPathCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpSdhPathCustomerIdentifier_Object = MibTableColumn
lpSdhPathCustomerIdentifier = _LpSdhPathCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 11, 1, 1),
    _LpSdhPathCustomerIdentifier_Type()
)
lpSdhPathCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhPathCustomerIdentifier.setStatus("mandatory")
_LpSdhPathStateTable_Object = MibTable
lpSdhPathStateTable = _LpSdhPathStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12)
)
if mibBuilder.loadTexts:
    lpSdhPathStateTable.setStatus("mandatory")
_LpSdhPathStateEntry_Object = MibTableRow
lpSdhPathStateEntry = _LpSdhPathStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1)
)
lpSdhPathStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathStateEntry.setStatus("mandatory")


class _LpSdhPathAdminState_Type(Integer32):
    """Custom type lpSdhPathAdminState based on Integer32"""
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


_LpSdhPathAdminState_Type.__name__ = "Integer32"
_LpSdhPathAdminState_Object = MibTableColumn
lpSdhPathAdminState = _LpSdhPathAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 1),
    _LpSdhPathAdminState_Type()
)
lpSdhPathAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathAdminState.setStatus("mandatory")


class _LpSdhPathOperationalState_Type(Integer32):
    """Custom type lpSdhPathOperationalState based on Integer32"""
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


_LpSdhPathOperationalState_Type.__name__ = "Integer32"
_LpSdhPathOperationalState_Object = MibTableColumn
lpSdhPathOperationalState = _LpSdhPathOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 2),
    _LpSdhPathOperationalState_Type()
)
lpSdhPathOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathOperationalState.setStatus("mandatory")


class _LpSdhPathUsageState_Type(Integer32):
    """Custom type lpSdhPathUsageState based on Integer32"""
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


_LpSdhPathUsageState_Type.__name__ = "Integer32"
_LpSdhPathUsageState_Object = MibTableColumn
lpSdhPathUsageState = _LpSdhPathUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 3),
    _LpSdhPathUsageState_Type()
)
lpSdhPathUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathUsageState.setStatus("mandatory")


class _LpSdhPathAvailabilityStatus_Type(OctetString):
    """Custom type lpSdhPathAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpSdhPathAvailabilityStatus_Type.__name__ = "OctetString"
_LpSdhPathAvailabilityStatus_Object = MibTableColumn
lpSdhPathAvailabilityStatus = _LpSdhPathAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 4),
    _LpSdhPathAvailabilityStatus_Type()
)
lpSdhPathAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathAvailabilityStatus.setStatus("mandatory")


class _LpSdhPathProceduralStatus_Type(OctetString):
    """Custom type lpSdhPathProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSdhPathProceduralStatus_Type.__name__ = "OctetString"
_LpSdhPathProceduralStatus_Object = MibTableColumn
lpSdhPathProceduralStatus = _LpSdhPathProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 5),
    _LpSdhPathProceduralStatus_Type()
)
lpSdhPathProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathProceduralStatus.setStatus("mandatory")


class _LpSdhPathControlStatus_Type(OctetString):
    """Custom type lpSdhPathControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSdhPathControlStatus_Type.__name__ = "OctetString"
_LpSdhPathControlStatus_Object = MibTableColumn
lpSdhPathControlStatus = _LpSdhPathControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 6),
    _LpSdhPathControlStatus_Type()
)
lpSdhPathControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathControlStatus.setStatus("mandatory")


class _LpSdhPathAlarmStatus_Type(OctetString):
    """Custom type lpSdhPathAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSdhPathAlarmStatus_Type.__name__ = "OctetString"
_LpSdhPathAlarmStatus_Object = MibTableColumn
lpSdhPathAlarmStatus = _LpSdhPathAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 7),
    _LpSdhPathAlarmStatus_Type()
)
lpSdhPathAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathAlarmStatus.setStatus("mandatory")


class _LpSdhPathStandbyStatus_Type(Integer32):
    """Custom type lpSdhPathStandbyStatus based on Integer32"""
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


_LpSdhPathStandbyStatus_Type.__name__ = "Integer32"
_LpSdhPathStandbyStatus_Object = MibTableColumn
lpSdhPathStandbyStatus = _LpSdhPathStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 8),
    _LpSdhPathStandbyStatus_Type()
)
lpSdhPathStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathStandbyStatus.setStatus("mandatory")


class _LpSdhPathUnknownStatus_Type(Integer32):
    """Custom type lpSdhPathUnknownStatus based on Integer32"""
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


_LpSdhPathUnknownStatus_Type.__name__ = "Integer32"
_LpSdhPathUnknownStatus_Object = MibTableColumn
lpSdhPathUnknownStatus = _LpSdhPathUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 12, 1, 9),
    _LpSdhPathUnknownStatus_Type()
)
lpSdhPathUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathUnknownStatus.setStatus("mandatory")
_LpSdhPathIfEntryTable_Object = MibTable
lpSdhPathIfEntryTable = _LpSdhPathIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 13)
)
if mibBuilder.loadTexts:
    lpSdhPathIfEntryTable.setStatus("mandatory")
_LpSdhPathIfEntryEntry_Object = MibTableRow
lpSdhPathIfEntryEntry = _LpSdhPathIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 13, 1)
)
lpSdhPathIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathIfEntryEntry.setStatus("mandatory")


class _LpSdhPathIfAdminStatus_Type(Integer32):
    """Custom type lpSdhPathIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSdhPathIfAdminStatus_Type.__name__ = "Integer32"
_LpSdhPathIfAdminStatus_Object = MibTableColumn
lpSdhPathIfAdminStatus = _LpSdhPathIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 13, 1, 1),
    _LpSdhPathIfAdminStatus_Type()
)
lpSdhPathIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhPathIfAdminStatus.setStatus("mandatory")


class _LpSdhPathIfIndex_Type(InterfaceIndex):
    """Custom type lpSdhPathIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpSdhPathIfIndex_Type.__name__ = "InterfaceIndex"
_LpSdhPathIfIndex_Object = MibTableColumn
lpSdhPathIfIndex = _LpSdhPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 13, 1, 2),
    _LpSdhPathIfIndex_Type()
)
lpSdhPathIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathIfIndex.setStatus("mandatory")
_LpSdhPathOperStatusTable_Object = MibTable
lpSdhPathOperStatusTable = _LpSdhPathOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 14)
)
if mibBuilder.loadTexts:
    lpSdhPathOperStatusTable.setStatus("mandatory")
_LpSdhPathOperStatusEntry_Object = MibTableRow
lpSdhPathOperStatusEntry = _LpSdhPathOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 14, 1)
)
lpSdhPathOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathOperStatusEntry.setStatus("mandatory")


class _LpSdhPathSnmpOperStatus_Type(Integer32):
    """Custom type lpSdhPathSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSdhPathSnmpOperStatus_Type.__name__ = "Integer32"
_LpSdhPathSnmpOperStatus_Object = MibTableColumn
lpSdhPathSnmpOperStatus = _LpSdhPathSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 14, 1, 1),
    _LpSdhPathSnmpOperStatus_Type()
)
lpSdhPathSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathSnmpOperStatus.setStatus("mandatory")
_LpSdhPathOperTable_Object = MibTable
lpSdhPathOperTable = _LpSdhPathOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15)
)
if mibBuilder.loadTexts:
    lpSdhPathOperTable.setStatus("mandatory")
_LpSdhPathOperEntry_Object = MibTableRow
lpSdhPathOperEntry = _LpSdhPathOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15, 1)
)
lpSdhPathOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathOperEntry.setStatus("mandatory")


class _LpSdhPathLopAlarm_Type(Integer32):
    """Custom type lpSdhPathLopAlarm based on Integer32"""
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


_LpSdhPathLopAlarm_Type.__name__ = "Integer32"
_LpSdhPathLopAlarm_Object = MibTableColumn
lpSdhPathLopAlarm = _LpSdhPathLopAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15, 1, 1),
    _LpSdhPathLopAlarm_Type()
)
lpSdhPathLopAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathLopAlarm.setStatus("mandatory")


class _LpSdhPathRxAisAlarm_Type(Integer32):
    """Custom type lpSdhPathRxAisAlarm based on Integer32"""
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


_LpSdhPathRxAisAlarm_Type.__name__ = "Integer32"
_LpSdhPathRxAisAlarm_Object = MibTableColumn
lpSdhPathRxAisAlarm = _LpSdhPathRxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15, 1, 2),
    _LpSdhPathRxAisAlarm_Type()
)
lpSdhPathRxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathRxAisAlarm.setStatus("mandatory")


class _LpSdhPathRxRfiAlarm_Type(Integer32):
    """Custom type lpSdhPathRxRfiAlarm based on Integer32"""
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


_LpSdhPathRxRfiAlarm_Type.__name__ = "Integer32"
_LpSdhPathRxRfiAlarm_Object = MibTableColumn
lpSdhPathRxRfiAlarm = _LpSdhPathRxRfiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15, 1, 3),
    _LpSdhPathRxRfiAlarm_Type()
)
lpSdhPathRxRfiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathRxRfiAlarm.setStatus("mandatory")


class _LpSdhPathSignalLabelMismatch_Type(Integer32):
    """Custom type lpSdhPathSignalLabelMismatch based on Integer32"""
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


_LpSdhPathSignalLabelMismatch_Type.__name__ = "Integer32"
_LpSdhPathSignalLabelMismatch_Object = MibTableColumn
lpSdhPathSignalLabelMismatch = _LpSdhPathSignalLabelMismatch_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15, 1, 4),
    _LpSdhPathSignalLabelMismatch_Type()
)
lpSdhPathSignalLabelMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathSignalLabelMismatch.setStatus("mandatory")


class _LpSdhPathTxAis_Type(Integer32):
    """Custom type lpSdhPathTxAis based on Integer32"""
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


_LpSdhPathTxAis_Type.__name__ = "Integer32"
_LpSdhPathTxAis_Object = MibTableColumn
lpSdhPathTxAis = _LpSdhPathTxAis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15, 1, 5),
    _LpSdhPathTxAis_Type()
)
lpSdhPathTxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathTxAis.setStatus("mandatory")


class _LpSdhPathTxRdi_Type(Integer32):
    """Custom type lpSdhPathTxRdi based on Integer32"""
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


_LpSdhPathTxRdi_Type.__name__ = "Integer32"
_LpSdhPathTxRdi_Object = MibTableColumn
lpSdhPathTxRdi = _LpSdhPathTxRdi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 15, 1, 6),
    _LpSdhPathTxRdi_Type()
)
lpSdhPathTxRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathTxRdi.setStatus("mandatory")
_LpSdhPathStatsTable_Object = MibTable
lpSdhPathStatsTable = _LpSdhPathStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16)
)
if mibBuilder.loadTexts:
    lpSdhPathStatsTable.setStatus("mandatory")
_LpSdhPathStatsEntry_Object = MibTableRow
lpSdhPathStatsEntry = _LpSdhPathStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1)
)
lpSdhPathStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhPathIndex"),
)
if mibBuilder.loadTexts:
    lpSdhPathStatsEntry.setStatus("mandatory")
_LpSdhPathPathErrorFreeSec_Type = Counter32
_LpSdhPathPathErrorFreeSec_Object = MibTableColumn
lpSdhPathPathErrorFreeSec = _LpSdhPathPathErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 1),
    _LpSdhPathPathErrorFreeSec_Type()
)
lpSdhPathPathErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathPathErrorFreeSec.setStatus("mandatory")
_LpSdhPathPathCodeViolations_Type = Counter32
_LpSdhPathPathCodeViolations_Object = MibTableColumn
lpSdhPathPathCodeViolations = _LpSdhPathPathCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 2),
    _LpSdhPathPathCodeViolations_Type()
)
lpSdhPathPathCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathPathCodeViolations.setStatus("mandatory")
_LpSdhPathPathErroredSec_Type = Counter32
_LpSdhPathPathErroredSec_Object = MibTableColumn
lpSdhPathPathErroredSec = _LpSdhPathPathErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 3),
    _LpSdhPathPathErroredSec_Type()
)
lpSdhPathPathErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathPathErroredSec.setStatus("mandatory")
_LpSdhPathPathSevErroredSec_Type = Counter32
_LpSdhPathPathSevErroredSec_Object = MibTableColumn
lpSdhPathPathSevErroredSec = _LpSdhPathPathSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 4),
    _LpSdhPathPathSevErroredSec_Type()
)
lpSdhPathPathSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathPathSevErroredSec.setStatus("mandatory")
_LpSdhPathPathAisLopSec_Type = Counter32
_LpSdhPathPathAisLopSec_Object = MibTableColumn
lpSdhPathPathAisLopSec = _LpSdhPathPathAisLopSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 5),
    _LpSdhPathPathAisLopSec_Type()
)
lpSdhPathPathAisLopSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathPathAisLopSec.setStatus("mandatory")
_LpSdhPathPathUnavailSec_Type = Counter32
_LpSdhPathPathUnavailSec_Object = MibTableColumn
lpSdhPathPathUnavailSec = _LpSdhPathPathUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 6),
    _LpSdhPathPathUnavailSec_Type()
)
lpSdhPathPathUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathPathUnavailSec.setStatus("mandatory")
_LpSdhPathPathFailures_Type = Counter32
_LpSdhPathPathFailures_Object = MibTableColumn
lpSdhPathPathFailures = _LpSdhPathPathFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 7),
    _LpSdhPathPathFailures_Type()
)
lpSdhPathPathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathPathFailures.setStatus("mandatory")
_LpSdhPathFarEndPathErrorFreeSec_Type = Counter32
_LpSdhPathFarEndPathErrorFreeSec_Object = MibTableColumn
lpSdhPathFarEndPathErrorFreeSec = _LpSdhPathFarEndPathErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 8),
    _LpSdhPathFarEndPathErrorFreeSec_Type()
)
lpSdhPathFarEndPathErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathFarEndPathErrorFreeSec.setStatus("mandatory")
_LpSdhPathFarEndPathCodeViolations_Type = Counter32
_LpSdhPathFarEndPathCodeViolations_Object = MibTableColumn
lpSdhPathFarEndPathCodeViolations = _LpSdhPathFarEndPathCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 9),
    _LpSdhPathFarEndPathCodeViolations_Type()
)
lpSdhPathFarEndPathCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathFarEndPathCodeViolations.setStatus("mandatory")
_LpSdhPathFarEndPathErroredSec_Type = Counter32
_LpSdhPathFarEndPathErroredSec_Object = MibTableColumn
lpSdhPathFarEndPathErroredSec = _LpSdhPathFarEndPathErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 10),
    _LpSdhPathFarEndPathErroredSec_Type()
)
lpSdhPathFarEndPathErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathFarEndPathErroredSec.setStatus("mandatory")
_LpSdhPathFarEndPathSevErroredSec_Type = Counter32
_LpSdhPathFarEndPathSevErroredSec_Object = MibTableColumn
lpSdhPathFarEndPathSevErroredSec = _LpSdhPathFarEndPathSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 11),
    _LpSdhPathFarEndPathSevErroredSec_Type()
)
lpSdhPathFarEndPathSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathFarEndPathSevErroredSec.setStatus("mandatory")
_LpSdhPathFarEndPathAisLopSec_Type = Counter32
_LpSdhPathFarEndPathAisLopSec_Object = MibTableColumn
lpSdhPathFarEndPathAisLopSec = _LpSdhPathFarEndPathAisLopSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 12),
    _LpSdhPathFarEndPathAisLopSec_Type()
)
lpSdhPathFarEndPathAisLopSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathFarEndPathAisLopSec.setStatus("mandatory")
_LpSdhPathFarEndPathUnavailSec_Type = Counter32
_LpSdhPathFarEndPathUnavailSec_Object = MibTableColumn
lpSdhPathFarEndPathUnavailSec = _LpSdhPathFarEndPathUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 13),
    _LpSdhPathFarEndPathUnavailSec_Type()
)
lpSdhPathFarEndPathUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathFarEndPathUnavailSec.setStatus("mandatory")
_LpSdhPathFarEndPathFailures_Type = Counter32
_LpSdhPathFarEndPathFailures_Object = MibTableColumn
lpSdhPathFarEndPathFailures = _LpSdhPathFarEndPathFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 2, 16, 1, 14),
    _LpSdhPathFarEndPathFailures_Type()
)
lpSdhPathFarEndPathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhPathFarEndPathFailures.setStatus("mandatory")
_LpSdhTest_ObjectIdentity = ObjectIdentity
lpSdhTest = _LpSdhTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3)
)
_LpSdhTestRowStatusTable_Object = MibTable
lpSdhTestRowStatusTable = _LpSdhTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 1)
)
if mibBuilder.loadTexts:
    lpSdhTestRowStatusTable.setStatus("mandatory")
_LpSdhTestRowStatusEntry_Object = MibTableRow
lpSdhTestRowStatusEntry = _LpSdhTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 1, 1)
)
lpSdhTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhTestIndex"),
)
if mibBuilder.loadTexts:
    lpSdhTestRowStatusEntry.setStatus("mandatory")
_LpSdhTestRowStatus_Type = RowStatus
_LpSdhTestRowStatus_Object = MibTableColumn
lpSdhTestRowStatus = _LpSdhTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 1, 1, 1),
    _LpSdhTestRowStatus_Type()
)
lpSdhTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestRowStatus.setStatus("mandatory")
_LpSdhTestComponentName_Type = DisplayString
_LpSdhTestComponentName_Object = MibTableColumn
lpSdhTestComponentName = _LpSdhTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 1, 1, 2),
    _LpSdhTestComponentName_Type()
)
lpSdhTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestComponentName.setStatus("mandatory")
_LpSdhTestStorageType_Type = StorageType
_LpSdhTestStorageType_Object = MibTableColumn
lpSdhTestStorageType = _LpSdhTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 1, 1, 4),
    _LpSdhTestStorageType_Type()
)
lpSdhTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestStorageType.setStatus("mandatory")
_LpSdhTestIndex_Type = NonReplicated
_LpSdhTestIndex_Object = MibTableColumn
lpSdhTestIndex = _LpSdhTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 1, 1, 10),
    _LpSdhTestIndex_Type()
)
lpSdhTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpSdhTestIndex.setStatus("mandatory")
_LpSdhTestStateTable_Object = MibTable
lpSdhTestStateTable = _LpSdhTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 10)
)
if mibBuilder.loadTexts:
    lpSdhTestStateTable.setStatus("mandatory")
_LpSdhTestStateEntry_Object = MibTableRow
lpSdhTestStateEntry = _LpSdhTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 10, 1)
)
lpSdhTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhTestIndex"),
)
if mibBuilder.loadTexts:
    lpSdhTestStateEntry.setStatus("mandatory")


class _LpSdhTestAdminState_Type(Integer32):
    """Custom type lpSdhTestAdminState based on Integer32"""
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


_LpSdhTestAdminState_Type.__name__ = "Integer32"
_LpSdhTestAdminState_Object = MibTableColumn
lpSdhTestAdminState = _LpSdhTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 10, 1, 1),
    _LpSdhTestAdminState_Type()
)
lpSdhTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestAdminState.setStatus("mandatory")


class _LpSdhTestOperationalState_Type(Integer32):
    """Custom type lpSdhTestOperationalState based on Integer32"""
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


_LpSdhTestOperationalState_Type.__name__ = "Integer32"
_LpSdhTestOperationalState_Object = MibTableColumn
lpSdhTestOperationalState = _LpSdhTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 10, 1, 2),
    _LpSdhTestOperationalState_Type()
)
lpSdhTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestOperationalState.setStatus("mandatory")


class _LpSdhTestUsageState_Type(Integer32):
    """Custom type lpSdhTestUsageState based on Integer32"""
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


_LpSdhTestUsageState_Type.__name__ = "Integer32"
_LpSdhTestUsageState_Object = MibTableColumn
lpSdhTestUsageState = _LpSdhTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 10, 1, 3),
    _LpSdhTestUsageState_Type()
)
lpSdhTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestUsageState.setStatus("mandatory")
_LpSdhTestSetupTable_Object = MibTable
lpSdhTestSetupTable = _LpSdhTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11)
)
if mibBuilder.loadTexts:
    lpSdhTestSetupTable.setStatus("mandatory")
_LpSdhTestSetupEntry_Object = MibTableRow
lpSdhTestSetupEntry = _LpSdhTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1)
)
lpSdhTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhTestIndex"),
)
if mibBuilder.loadTexts:
    lpSdhTestSetupEntry.setStatus("mandatory")


class _LpSdhTestPurpose_Type(AsciiString):
    """Custom type lpSdhTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpSdhTestPurpose_Type.__name__ = "AsciiString"
_LpSdhTestPurpose_Object = MibTableColumn
lpSdhTestPurpose = _LpSdhTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 1),
    _LpSdhTestPurpose_Type()
)
lpSdhTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestPurpose.setStatus("mandatory")


class _LpSdhTestType_Type(Integer32):
    """Custom type lpSdhTestType based on Integer32"""
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


_LpSdhTestType_Type.__name__ = "Integer32"
_LpSdhTestType_Object = MibTableColumn
lpSdhTestType = _LpSdhTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 2),
    _LpSdhTestType_Type()
)
lpSdhTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestType.setStatus("mandatory")


class _LpSdhTestFrmSize_Type(Unsigned32):
    """Custom type lpSdhTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpSdhTestFrmSize_Type.__name__ = "Unsigned32"
_LpSdhTestFrmSize_Object = MibTableColumn
lpSdhTestFrmSize = _LpSdhTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 3),
    _LpSdhTestFrmSize_Type()
)
lpSdhTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestFrmSize.setStatus("mandatory")


class _LpSdhTestFrmPatternType_Type(Integer32):
    """Custom type lpSdhTestFrmPatternType based on Integer32"""
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


_LpSdhTestFrmPatternType_Type.__name__ = "Integer32"
_LpSdhTestFrmPatternType_Object = MibTableColumn
lpSdhTestFrmPatternType = _LpSdhTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 4),
    _LpSdhTestFrmPatternType_Type()
)
lpSdhTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestFrmPatternType.setStatus("mandatory")


class _LpSdhTestCustomizedPattern_Type(Hex):
    """Custom type lpSdhTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpSdhTestCustomizedPattern_Type.__name__ = "Hex"
_LpSdhTestCustomizedPattern_Object = MibTableColumn
lpSdhTestCustomizedPattern = _LpSdhTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 5),
    _LpSdhTestCustomizedPattern_Type()
)
lpSdhTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestCustomizedPattern.setStatus("mandatory")


class _LpSdhTestDataStartDelay_Type(Unsigned32):
    """Custom type lpSdhTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpSdhTestDataStartDelay_Type.__name__ = "Unsigned32"
_LpSdhTestDataStartDelay_Object = MibTableColumn
lpSdhTestDataStartDelay = _LpSdhTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 6),
    _LpSdhTestDataStartDelay_Type()
)
lpSdhTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestDataStartDelay.setStatus("mandatory")


class _LpSdhTestDisplayInterval_Type(Unsigned32):
    """Custom type lpSdhTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpSdhTestDisplayInterval_Type.__name__ = "Unsigned32"
_LpSdhTestDisplayInterval_Object = MibTableColumn
lpSdhTestDisplayInterval = _LpSdhTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 7),
    _LpSdhTestDisplayInterval_Type()
)
lpSdhTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestDisplayInterval.setStatus("mandatory")


class _LpSdhTestDuration_Type(Unsigned32):
    """Custom type lpSdhTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpSdhTestDuration_Type.__name__ = "Unsigned32"
_LpSdhTestDuration_Object = MibTableColumn
lpSdhTestDuration = _LpSdhTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 11, 1, 8),
    _LpSdhTestDuration_Type()
)
lpSdhTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhTestDuration.setStatus("mandatory")
_LpSdhTestResultsTable_Object = MibTable
lpSdhTestResultsTable = _LpSdhTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12)
)
if mibBuilder.loadTexts:
    lpSdhTestResultsTable.setStatus("mandatory")
_LpSdhTestResultsEntry_Object = MibTableRow
lpSdhTestResultsEntry = _LpSdhTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1)
)
lpSdhTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhTestIndex"),
)
if mibBuilder.loadTexts:
    lpSdhTestResultsEntry.setStatus("mandatory")
_LpSdhTestElapsedTime_Type = Counter32
_LpSdhTestElapsedTime_Object = MibTableColumn
lpSdhTestElapsedTime = _LpSdhTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 1),
    _LpSdhTestElapsedTime_Type()
)
lpSdhTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestElapsedTime.setStatus("mandatory")


class _LpSdhTestTimeRemaining_Type(Unsigned32):
    """Custom type lpSdhTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpSdhTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpSdhTestTimeRemaining_Object = MibTableColumn
lpSdhTestTimeRemaining = _LpSdhTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 2),
    _LpSdhTestTimeRemaining_Type()
)
lpSdhTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestTimeRemaining.setStatus("mandatory")


class _LpSdhTestCauseOfTermination_Type(Integer32):
    """Custom type lpSdhTestCauseOfTermination based on Integer32"""
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


_LpSdhTestCauseOfTermination_Type.__name__ = "Integer32"
_LpSdhTestCauseOfTermination_Object = MibTableColumn
lpSdhTestCauseOfTermination = _LpSdhTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 3),
    _LpSdhTestCauseOfTermination_Type()
)
lpSdhTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestCauseOfTermination.setStatus("mandatory")
_LpSdhTestBitsTx_Type = PassportCounter64
_LpSdhTestBitsTx_Object = MibTableColumn
lpSdhTestBitsTx = _LpSdhTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 4),
    _LpSdhTestBitsTx_Type()
)
lpSdhTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestBitsTx.setStatus("mandatory")
_LpSdhTestBytesTx_Type = PassportCounter64
_LpSdhTestBytesTx_Object = MibTableColumn
lpSdhTestBytesTx = _LpSdhTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 5),
    _LpSdhTestBytesTx_Type()
)
lpSdhTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestBytesTx.setStatus("mandatory")
_LpSdhTestFrmTx_Type = PassportCounter64
_LpSdhTestFrmTx_Object = MibTableColumn
lpSdhTestFrmTx = _LpSdhTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 6),
    _LpSdhTestFrmTx_Type()
)
lpSdhTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestFrmTx.setStatus("mandatory")
_LpSdhTestBitsRx_Type = PassportCounter64
_LpSdhTestBitsRx_Object = MibTableColumn
lpSdhTestBitsRx = _LpSdhTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 7),
    _LpSdhTestBitsRx_Type()
)
lpSdhTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestBitsRx.setStatus("mandatory")
_LpSdhTestBytesRx_Type = PassportCounter64
_LpSdhTestBytesRx_Object = MibTableColumn
lpSdhTestBytesRx = _LpSdhTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 8),
    _LpSdhTestBytesRx_Type()
)
lpSdhTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestBytesRx.setStatus("mandatory")
_LpSdhTestFrmRx_Type = PassportCounter64
_LpSdhTestFrmRx_Object = MibTableColumn
lpSdhTestFrmRx = _LpSdhTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 9),
    _LpSdhTestFrmRx_Type()
)
lpSdhTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestFrmRx.setStatus("mandatory")
_LpSdhTestErroredFrmRx_Type = PassportCounter64
_LpSdhTestErroredFrmRx_Object = MibTableColumn
lpSdhTestErroredFrmRx = _LpSdhTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 10),
    _LpSdhTestErroredFrmRx_Type()
)
lpSdhTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestErroredFrmRx.setStatus("mandatory")


class _LpSdhTestBitErrorRate_Type(AsciiString):
    """Custom type lpSdhTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpSdhTestBitErrorRate_Type.__name__ = "AsciiString"
_LpSdhTestBitErrorRate_Object = MibTableColumn
lpSdhTestBitErrorRate = _LpSdhTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 3, 12, 1, 11),
    _LpSdhTestBitErrorRate_Type()
)
lpSdhTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTestBitErrorRate.setStatus("mandatory")
_LpSdhProvTable_Object = MibTable
lpSdhProvTable = _LpSdhProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 10)
)
if mibBuilder.loadTexts:
    lpSdhProvTable.setStatus("mandatory")
_LpSdhProvEntry_Object = MibTableRow
lpSdhProvEntry = _LpSdhProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 10, 1)
)
lpSdhProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhProvEntry.setStatus("mandatory")


class _LpSdhClockingSource_Type(Integer32):
    """Custom type lpSdhClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("local", 0),
          ("module", 2))
    )


_LpSdhClockingSource_Type.__name__ = "Integer32"
_LpSdhClockingSource_Object = MibTableColumn
lpSdhClockingSource = _LpSdhClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 10, 1, 1),
    _LpSdhClockingSource_Type()
)
lpSdhClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhClockingSource.setStatus("mandatory")
_LpSdhCidDataTable_Object = MibTable
lpSdhCidDataTable = _LpSdhCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 11)
)
if mibBuilder.loadTexts:
    lpSdhCidDataTable.setStatus("mandatory")
_LpSdhCidDataEntry_Object = MibTableRow
lpSdhCidDataEntry = _LpSdhCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 11, 1)
)
lpSdhCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhCidDataEntry.setStatus("mandatory")


class _LpSdhCustomerIdentifier_Type(Unsigned32):
    """Custom type lpSdhCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpSdhCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpSdhCustomerIdentifier_Object = MibTableColumn
lpSdhCustomerIdentifier = _LpSdhCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 11, 1, 1),
    _LpSdhCustomerIdentifier_Type()
)
lpSdhCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhCustomerIdentifier.setStatus("mandatory")
_LpSdhAdminInfoTable_Object = MibTable
lpSdhAdminInfoTable = _LpSdhAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 12)
)
if mibBuilder.loadTexts:
    lpSdhAdminInfoTable.setStatus("mandatory")
_LpSdhAdminInfoEntry_Object = MibTableRow
lpSdhAdminInfoEntry = _LpSdhAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 12, 1)
)
lpSdhAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhAdminInfoEntry.setStatus("mandatory")


class _LpSdhVendor_Type(AsciiString):
    """Custom type lpSdhVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpSdhVendor_Type.__name__ = "AsciiString"
_LpSdhVendor_Object = MibTableColumn
lpSdhVendor = _LpSdhVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 12, 1, 1),
    _LpSdhVendor_Type()
)
lpSdhVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhVendor.setStatus("mandatory")


class _LpSdhCommentText_Type(AsciiString):
    """Custom type lpSdhCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpSdhCommentText_Type.__name__ = "AsciiString"
_LpSdhCommentText_Object = MibTableColumn
lpSdhCommentText = _LpSdhCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 12, 1, 2),
    _LpSdhCommentText_Type()
)
lpSdhCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhCommentText.setStatus("mandatory")
_LpSdhIfEntryTable_Object = MibTable
lpSdhIfEntryTable = _LpSdhIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 13)
)
if mibBuilder.loadTexts:
    lpSdhIfEntryTable.setStatus("mandatory")
_LpSdhIfEntryEntry_Object = MibTableRow
lpSdhIfEntryEntry = _LpSdhIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 13, 1)
)
lpSdhIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhIfEntryEntry.setStatus("mandatory")


class _LpSdhIfAdminStatus_Type(Integer32):
    """Custom type lpSdhIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSdhIfAdminStatus_Type.__name__ = "Integer32"
_LpSdhIfAdminStatus_Object = MibTableColumn
lpSdhIfAdminStatus = _LpSdhIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 13, 1, 1),
    _LpSdhIfAdminStatus_Type()
)
lpSdhIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSdhIfAdminStatus.setStatus("mandatory")


class _LpSdhIfIndex_Type(InterfaceIndex):
    """Custom type lpSdhIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpSdhIfIndex_Type.__name__ = "InterfaceIndex"
_LpSdhIfIndex_Object = MibTableColumn
lpSdhIfIndex = _LpSdhIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 13, 1, 2),
    _LpSdhIfIndex_Type()
)
lpSdhIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhIfIndex.setStatus("mandatory")
_LpSdhOperStatusTable_Object = MibTable
lpSdhOperStatusTable = _LpSdhOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 14)
)
if mibBuilder.loadTexts:
    lpSdhOperStatusTable.setStatus("mandatory")
_LpSdhOperStatusEntry_Object = MibTableRow
lpSdhOperStatusEntry = _LpSdhOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 14, 1)
)
lpSdhOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhOperStatusEntry.setStatus("mandatory")


class _LpSdhSnmpOperStatus_Type(Integer32):
    """Custom type lpSdhSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpSdhSnmpOperStatus_Type.__name__ = "Integer32"
_LpSdhSnmpOperStatus_Object = MibTableColumn
lpSdhSnmpOperStatus = _LpSdhSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 14, 1, 1),
    _LpSdhSnmpOperStatus_Type()
)
lpSdhSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhSnmpOperStatus.setStatus("mandatory")
_LpSdhStateTable_Object = MibTable
lpSdhStateTable = _LpSdhStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15)
)
if mibBuilder.loadTexts:
    lpSdhStateTable.setStatus("mandatory")
_LpSdhStateEntry_Object = MibTableRow
lpSdhStateEntry = _LpSdhStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1)
)
lpSdhStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhStateEntry.setStatus("mandatory")


class _LpSdhAdminState_Type(Integer32):
    """Custom type lpSdhAdminState based on Integer32"""
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


_LpSdhAdminState_Type.__name__ = "Integer32"
_LpSdhAdminState_Object = MibTableColumn
lpSdhAdminState = _LpSdhAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 1),
    _LpSdhAdminState_Type()
)
lpSdhAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhAdminState.setStatus("mandatory")


class _LpSdhOperationalState_Type(Integer32):
    """Custom type lpSdhOperationalState based on Integer32"""
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


_LpSdhOperationalState_Type.__name__ = "Integer32"
_LpSdhOperationalState_Object = MibTableColumn
lpSdhOperationalState = _LpSdhOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 2),
    _LpSdhOperationalState_Type()
)
lpSdhOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhOperationalState.setStatus("mandatory")


class _LpSdhUsageState_Type(Integer32):
    """Custom type lpSdhUsageState based on Integer32"""
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


_LpSdhUsageState_Type.__name__ = "Integer32"
_LpSdhUsageState_Object = MibTableColumn
lpSdhUsageState = _LpSdhUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 3),
    _LpSdhUsageState_Type()
)
lpSdhUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhUsageState.setStatus("mandatory")


class _LpSdhAvailabilityStatus_Type(OctetString):
    """Custom type lpSdhAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpSdhAvailabilityStatus_Type.__name__ = "OctetString"
_LpSdhAvailabilityStatus_Object = MibTableColumn
lpSdhAvailabilityStatus = _LpSdhAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 4),
    _LpSdhAvailabilityStatus_Type()
)
lpSdhAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhAvailabilityStatus.setStatus("mandatory")


class _LpSdhProceduralStatus_Type(OctetString):
    """Custom type lpSdhProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSdhProceduralStatus_Type.__name__ = "OctetString"
_LpSdhProceduralStatus_Object = MibTableColumn
lpSdhProceduralStatus = _LpSdhProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 5),
    _LpSdhProceduralStatus_Type()
)
lpSdhProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhProceduralStatus.setStatus("mandatory")


class _LpSdhControlStatus_Type(OctetString):
    """Custom type lpSdhControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSdhControlStatus_Type.__name__ = "OctetString"
_LpSdhControlStatus_Object = MibTableColumn
lpSdhControlStatus = _LpSdhControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 6),
    _LpSdhControlStatus_Type()
)
lpSdhControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhControlStatus.setStatus("mandatory")


class _LpSdhAlarmStatus_Type(OctetString):
    """Custom type lpSdhAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpSdhAlarmStatus_Type.__name__ = "OctetString"
_LpSdhAlarmStatus_Object = MibTableColumn
lpSdhAlarmStatus = _LpSdhAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 7),
    _LpSdhAlarmStatus_Type()
)
lpSdhAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhAlarmStatus.setStatus("mandatory")


class _LpSdhStandbyStatus_Type(Integer32):
    """Custom type lpSdhStandbyStatus based on Integer32"""
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


_LpSdhStandbyStatus_Type.__name__ = "Integer32"
_LpSdhStandbyStatus_Object = MibTableColumn
lpSdhStandbyStatus = _LpSdhStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 8),
    _LpSdhStandbyStatus_Type()
)
lpSdhStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhStandbyStatus.setStatus("mandatory")


class _LpSdhUnknownStatus_Type(Integer32):
    """Custom type lpSdhUnknownStatus based on Integer32"""
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


_LpSdhUnknownStatus_Type.__name__ = "Integer32"
_LpSdhUnknownStatus_Object = MibTableColumn
lpSdhUnknownStatus = _LpSdhUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 15, 1, 9),
    _LpSdhUnknownStatus_Type()
)
lpSdhUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhUnknownStatus.setStatus("mandatory")
_LpSdhOperTable_Object = MibTable
lpSdhOperTable = _LpSdhOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16)
)
if mibBuilder.loadTexts:
    lpSdhOperTable.setStatus("mandatory")
_LpSdhOperEntry_Object = MibTableRow
lpSdhOperEntry = _LpSdhOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1)
)
lpSdhOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhOperEntry.setStatus("mandatory")


class _LpSdhLosAlarm_Type(Integer32):
    """Custom type lpSdhLosAlarm based on Integer32"""
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


_LpSdhLosAlarm_Type.__name__ = "Integer32"
_LpSdhLosAlarm_Object = MibTableColumn
lpSdhLosAlarm = _LpSdhLosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1, 1),
    _LpSdhLosAlarm_Type()
)
lpSdhLosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLosAlarm.setStatus("mandatory")


class _LpSdhLofAlarm_Type(Integer32):
    """Custom type lpSdhLofAlarm based on Integer32"""
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


_LpSdhLofAlarm_Type.__name__ = "Integer32"
_LpSdhLofAlarm_Object = MibTableColumn
lpSdhLofAlarm = _LpSdhLofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1, 2),
    _LpSdhLofAlarm_Type()
)
lpSdhLofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLofAlarm.setStatus("mandatory")


class _LpSdhRxAisAlarm_Type(Integer32):
    """Custom type lpSdhRxAisAlarm based on Integer32"""
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


_LpSdhRxAisAlarm_Type.__name__ = "Integer32"
_LpSdhRxAisAlarm_Object = MibTableColumn
lpSdhRxAisAlarm = _LpSdhRxAisAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1, 3),
    _LpSdhRxAisAlarm_Type()
)
lpSdhRxAisAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhRxAisAlarm.setStatus("mandatory")


class _LpSdhRxRfiAlarm_Type(Integer32):
    """Custom type lpSdhRxRfiAlarm based on Integer32"""
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


_LpSdhRxRfiAlarm_Type.__name__ = "Integer32"
_LpSdhRxRfiAlarm_Object = MibTableColumn
lpSdhRxRfiAlarm = _LpSdhRxRfiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1, 4),
    _LpSdhRxRfiAlarm_Type()
)
lpSdhRxRfiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhRxRfiAlarm.setStatus("mandatory")


class _LpSdhTxAis_Type(Integer32):
    """Custom type lpSdhTxAis based on Integer32"""
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


_LpSdhTxAis_Type.__name__ = "Integer32"
_LpSdhTxAis_Object = MibTableColumn
lpSdhTxAis = _LpSdhTxAis_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1, 5),
    _LpSdhTxAis_Type()
)
lpSdhTxAis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTxAis.setStatus("mandatory")


class _LpSdhTxRdi_Type(Integer32):
    """Custom type lpSdhTxRdi based on Integer32"""
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


_LpSdhTxRdi_Type.__name__ = "Integer32"
_LpSdhTxRdi_Object = MibTableColumn
lpSdhTxRdi = _LpSdhTxRdi_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1, 6),
    _LpSdhTxRdi_Type()
)
lpSdhTxRdi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhTxRdi.setStatus("mandatory")


class _LpSdhUnusableTxClockRefAlarm_Type(Integer32):
    """Custom type lpSdhUnusableTxClockRefAlarm based on Integer32"""
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


_LpSdhUnusableTxClockRefAlarm_Type.__name__ = "Integer32"
_LpSdhUnusableTxClockRefAlarm_Object = MibTableColumn
lpSdhUnusableTxClockRefAlarm = _LpSdhUnusableTxClockRefAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 16, 1, 7),
    _LpSdhUnusableTxClockRefAlarm_Type()
)
lpSdhUnusableTxClockRefAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhUnusableTxClockRefAlarm.setStatus("mandatory")
_LpSdhStatsTable_Object = MibTable
lpSdhStatsTable = _LpSdhStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17)
)
if mibBuilder.loadTexts:
    lpSdhStatsTable.setStatus("mandatory")
_LpSdhStatsEntry_Object = MibTableRow
lpSdhStatsEntry = _LpSdhStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1)
)
lpSdhStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpSdhIndex"),
)
if mibBuilder.loadTexts:
    lpSdhStatsEntry.setStatus("mandatory")
_LpSdhRunningTime_Type = Counter32
_LpSdhRunningTime_Object = MibTableColumn
lpSdhRunningTime = _LpSdhRunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 1),
    _LpSdhRunningTime_Type()
)
lpSdhRunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhRunningTime.setStatus("mandatory")
_LpSdhErrorFreeSec_Type = Counter32
_LpSdhErrorFreeSec_Object = MibTableColumn
lpSdhErrorFreeSec = _LpSdhErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 2),
    _LpSdhErrorFreeSec_Type()
)
lpSdhErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhErrorFreeSec.setStatus("mandatory")
_LpSdhSectCodeViolations_Type = Counter32
_LpSdhSectCodeViolations_Object = MibTableColumn
lpSdhSectCodeViolations = _LpSdhSectCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 3),
    _LpSdhSectCodeViolations_Type()
)
lpSdhSectCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhSectCodeViolations.setStatus("mandatory")
_LpSdhSectErroredSec_Type = Counter32
_LpSdhSectErroredSec_Object = MibTableColumn
lpSdhSectErroredSec = _LpSdhSectErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 4),
    _LpSdhSectErroredSec_Type()
)
lpSdhSectErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhSectErroredSec.setStatus("mandatory")
_LpSdhSectSevErroredSec_Type = Counter32
_LpSdhSectSevErroredSec_Object = MibTableColumn
lpSdhSectSevErroredSec = _LpSdhSectSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 5),
    _LpSdhSectSevErroredSec_Type()
)
lpSdhSectSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhSectSevErroredSec.setStatus("mandatory")
_LpSdhSectLosSec_Type = Counter32
_LpSdhSectLosSec_Object = MibTableColumn
lpSdhSectLosSec = _LpSdhSectLosSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 6),
    _LpSdhSectLosSec_Type()
)
lpSdhSectLosSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhSectLosSec.setStatus("mandatory")
_LpSdhSectSevErroredFrmSec_Type = Counter32
_LpSdhSectSevErroredFrmSec_Object = MibTableColumn
lpSdhSectSevErroredFrmSec = _LpSdhSectSevErroredFrmSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 7),
    _LpSdhSectSevErroredFrmSec_Type()
)
lpSdhSectSevErroredFrmSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhSectSevErroredFrmSec.setStatus("mandatory")
_LpSdhSectFailures_Type = Counter32
_LpSdhSectFailures_Object = MibTableColumn
lpSdhSectFailures = _LpSdhSectFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 8),
    _LpSdhSectFailures_Type()
)
lpSdhSectFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhSectFailures.setStatus("mandatory")
_LpSdhLineCodeViolations_Type = Counter32
_LpSdhLineCodeViolations_Object = MibTableColumn
lpSdhLineCodeViolations = _LpSdhLineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 9),
    _LpSdhLineCodeViolations_Type()
)
lpSdhLineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLineCodeViolations.setStatus("mandatory")
_LpSdhLineErroredSec_Type = Counter32
_LpSdhLineErroredSec_Object = MibTableColumn
lpSdhLineErroredSec = _LpSdhLineErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 10),
    _LpSdhLineErroredSec_Type()
)
lpSdhLineErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLineErroredSec.setStatus("mandatory")
_LpSdhLineSevErroredSec_Type = Counter32
_LpSdhLineSevErroredSec_Object = MibTableColumn
lpSdhLineSevErroredSec = _LpSdhLineSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 11),
    _LpSdhLineSevErroredSec_Type()
)
lpSdhLineSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLineSevErroredSec.setStatus("mandatory")
_LpSdhLineAisSec_Type = Counter32
_LpSdhLineAisSec_Object = MibTableColumn
lpSdhLineAisSec = _LpSdhLineAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 12),
    _LpSdhLineAisSec_Type()
)
lpSdhLineAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLineAisSec.setStatus("mandatory")
_LpSdhLineUnavailSec_Type = Counter32
_LpSdhLineUnavailSec_Object = MibTableColumn
lpSdhLineUnavailSec = _LpSdhLineUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 13),
    _LpSdhLineUnavailSec_Type()
)
lpSdhLineUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLineUnavailSec.setStatus("mandatory")
_LpSdhLineFailures_Type = Counter32
_LpSdhLineFailures_Object = MibTableColumn
lpSdhLineFailures = _LpSdhLineFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 14),
    _LpSdhLineFailures_Type()
)
lpSdhLineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhLineFailures.setStatus("mandatory")
_LpSdhFarEndLineErrorFreeSec_Type = Counter32
_LpSdhFarEndLineErrorFreeSec_Object = MibTableColumn
lpSdhFarEndLineErrorFreeSec = _LpSdhFarEndLineErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 15),
    _LpSdhFarEndLineErrorFreeSec_Type()
)
lpSdhFarEndLineErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhFarEndLineErrorFreeSec.setStatus("mandatory")
_LpSdhFarEndLineCodeViolations_Type = Counter32
_LpSdhFarEndLineCodeViolations_Object = MibTableColumn
lpSdhFarEndLineCodeViolations = _LpSdhFarEndLineCodeViolations_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 16),
    _LpSdhFarEndLineCodeViolations_Type()
)
lpSdhFarEndLineCodeViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhFarEndLineCodeViolations.setStatus("mandatory")
_LpSdhFarEndLineErroredSec_Type = Counter32
_LpSdhFarEndLineErroredSec_Object = MibTableColumn
lpSdhFarEndLineErroredSec = _LpSdhFarEndLineErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 17),
    _LpSdhFarEndLineErroredSec_Type()
)
lpSdhFarEndLineErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhFarEndLineErroredSec.setStatus("mandatory")
_LpSdhFarEndLineSevErroredSec_Type = Counter32
_LpSdhFarEndLineSevErroredSec_Object = MibTableColumn
lpSdhFarEndLineSevErroredSec = _LpSdhFarEndLineSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 18),
    _LpSdhFarEndLineSevErroredSec_Type()
)
lpSdhFarEndLineSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhFarEndLineSevErroredSec.setStatus("mandatory")
_LpSdhFarEndLineAisSec_Type = Counter32
_LpSdhFarEndLineAisSec_Object = MibTableColumn
lpSdhFarEndLineAisSec = _LpSdhFarEndLineAisSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 19),
    _LpSdhFarEndLineAisSec_Type()
)
lpSdhFarEndLineAisSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhFarEndLineAisSec.setStatus("mandatory")
_LpSdhFarEndLineUnavailSec_Type = Counter32
_LpSdhFarEndLineUnavailSec_Object = MibTableColumn
lpSdhFarEndLineUnavailSec = _LpSdhFarEndLineUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 20),
    _LpSdhFarEndLineUnavailSec_Type()
)
lpSdhFarEndLineUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhFarEndLineUnavailSec.setStatus("mandatory")
_LpSdhFarEndLineFailures_Type = Counter32
_LpSdhFarEndLineFailures_Object = MibTableColumn
lpSdhFarEndLineFailures = _LpSdhFarEndLineFailures_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 15, 17, 1, 21),
    _LpSdhFarEndLineFailures_Type()
)
lpSdhFarEndLineFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSdhFarEndLineFailures.setStatus("mandatory")
_LpJT2_ObjectIdentity = ObjectIdentity
lpJT2 = _LpJT2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16)
)
_LpJT2RowStatusTable_Object = MibTable
lpJT2RowStatusTable = _LpJT2RowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 1)
)
if mibBuilder.loadTexts:
    lpJT2RowStatusTable.setStatus("mandatory")
_LpJT2RowStatusEntry_Object = MibTableRow
lpJT2RowStatusEntry = _LpJT2RowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 1, 1)
)
lpJT2RowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2RowStatusEntry.setStatus("mandatory")
_LpJT2RowStatus_Type = RowStatus
_LpJT2RowStatus_Object = MibTableColumn
lpJT2RowStatus = _LpJT2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 1, 1, 1),
    _LpJT2RowStatus_Type()
)
lpJT2RowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2RowStatus.setStatus("mandatory")
_LpJT2ComponentName_Type = DisplayString
_LpJT2ComponentName_Object = MibTableColumn
lpJT2ComponentName = _LpJT2ComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 1, 1, 2),
    _LpJT2ComponentName_Type()
)
lpJT2ComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2ComponentName.setStatus("mandatory")
_LpJT2StorageType_Type = StorageType
_LpJT2StorageType_Object = MibTableColumn
lpJT2StorageType = _LpJT2StorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 1, 1, 4),
    _LpJT2StorageType_Type()
)
lpJT2StorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2StorageType.setStatus("mandatory")


class _LpJT2Index_Type(Integer32):
    """Custom type lpJT2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LpJT2Index_Type.__name__ = "Integer32"
_LpJT2Index_Object = MibTableColumn
lpJT2Index = _LpJT2Index_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 1, 1, 10),
    _LpJT2Index_Type()
)
lpJT2Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpJT2Index.setStatus("mandatory")
_LpJT2Test_ObjectIdentity = ObjectIdentity
lpJT2Test = _LpJT2Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2)
)
_LpJT2TestRowStatusTable_Object = MibTable
lpJT2TestRowStatusTable = _LpJT2TestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 1)
)
if mibBuilder.loadTexts:
    lpJT2TestRowStatusTable.setStatus("mandatory")
_LpJT2TestRowStatusEntry_Object = MibTableRow
lpJT2TestRowStatusEntry = _LpJT2TestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 1, 1)
)
lpJT2TestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2TestIndex"),
)
if mibBuilder.loadTexts:
    lpJT2TestRowStatusEntry.setStatus("mandatory")
_LpJT2TestRowStatus_Type = RowStatus
_LpJT2TestRowStatus_Object = MibTableColumn
lpJT2TestRowStatus = _LpJT2TestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 1, 1, 1),
    _LpJT2TestRowStatus_Type()
)
lpJT2TestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestRowStatus.setStatus("mandatory")
_LpJT2TestComponentName_Type = DisplayString
_LpJT2TestComponentName_Object = MibTableColumn
lpJT2TestComponentName = _LpJT2TestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 1, 1, 2),
    _LpJT2TestComponentName_Type()
)
lpJT2TestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestComponentName.setStatus("mandatory")
_LpJT2TestStorageType_Type = StorageType
_LpJT2TestStorageType_Object = MibTableColumn
lpJT2TestStorageType = _LpJT2TestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 1, 1, 4),
    _LpJT2TestStorageType_Type()
)
lpJT2TestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestStorageType.setStatus("mandatory")
_LpJT2TestIndex_Type = NonReplicated
_LpJT2TestIndex_Object = MibTableColumn
lpJT2TestIndex = _LpJT2TestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 1, 1, 10),
    _LpJT2TestIndex_Type()
)
lpJT2TestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpJT2TestIndex.setStatus("mandatory")
_LpJT2TestStateTable_Object = MibTable
lpJT2TestStateTable = _LpJT2TestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 10)
)
if mibBuilder.loadTexts:
    lpJT2TestStateTable.setStatus("mandatory")
_LpJT2TestStateEntry_Object = MibTableRow
lpJT2TestStateEntry = _LpJT2TestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 10, 1)
)
lpJT2TestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2TestIndex"),
)
if mibBuilder.loadTexts:
    lpJT2TestStateEntry.setStatus("mandatory")


class _LpJT2TestAdminState_Type(Integer32):
    """Custom type lpJT2TestAdminState based on Integer32"""
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


_LpJT2TestAdminState_Type.__name__ = "Integer32"
_LpJT2TestAdminState_Object = MibTableColumn
lpJT2TestAdminState = _LpJT2TestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 10, 1, 1),
    _LpJT2TestAdminState_Type()
)
lpJT2TestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestAdminState.setStatus("mandatory")


class _LpJT2TestOperationalState_Type(Integer32):
    """Custom type lpJT2TestOperationalState based on Integer32"""
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


_LpJT2TestOperationalState_Type.__name__ = "Integer32"
_LpJT2TestOperationalState_Object = MibTableColumn
lpJT2TestOperationalState = _LpJT2TestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 10, 1, 2),
    _LpJT2TestOperationalState_Type()
)
lpJT2TestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestOperationalState.setStatus("mandatory")


class _LpJT2TestUsageState_Type(Integer32):
    """Custom type lpJT2TestUsageState based on Integer32"""
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


_LpJT2TestUsageState_Type.__name__ = "Integer32"
_LpJT2TestUsageState_Object = MibTableColumn
lpJT2TestUsageState = _LpJT2TestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 10, 1, 3),
    _LpJT2TestUsageState_Type()
)
lpJT2TestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestUsageState.setStatus("mandatory")
_LpJT2TestSetupTable_Object = MibTable
lpJT2TestSetupTable = _LpJT2TestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11)
)
if mibBuilder.loadTexts:
    lpJT2TestSetupTable.setStatus("mandatory")
_LpJT2TestSetupEntry_Object = MibTableRow
lpJT2TestSetupEntry = _LpJT2TestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1)
)
lpJT2TestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2TestIndex"),
)
if mibBuilder.loadTexts:
    lpJT2TestSetupEntry.setStatus("mandatory")


class _LpJT2TestPurpose_Type(AsciiString):
    """Custom type lpJT2TestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpJT2TestPurpose_Type.__name__ = "AsciiString"
_LpJT2TestPurpose_Object = MibTableColumn
lpJT2TestPurpose = _LpJT2TestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 1),
    _LpJT2TestPurpose_Type()
)
lpJT2TestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestPurpose.setStatus("mandatory")


class _LpJT2TestType_Type(Integer32):
    """Custom type lpJT2TestType based on Integer32"""
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


_LpJT2TestType_Type.__name__ = "Integer32"
_LpJT2TestType_Object = MibTableColumn
lpJT2TestType = _LpJT2TestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 2),
    _LpJT2TestType_Type()
)
lpJT2TestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestType.setStatus("mandatory")


class _LpJT2TestFrmSize_Type(Unsigned32):
    """Custom type lpJT2TestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpJT2TestFrmSize_Type.__name__ = "Unsigned32"
_LpJT2TestFrmSize_Object = MibTableColumn
lpJT2TestFrmSize = _LpJT2TestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 3),
    _LpJT2TestFrmSize_Type()
)
lpJT2TestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestFrmSize.setStatus("mandatory")


class _LpJT2TestFrmPatternType_Type(Integer32):
    """Custom type lpJT2TestFrmPatternType based on Integer32"""
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


_LpJT2TestFrmPatternType_Type.__name__ = "Integer32"
_LpJT2TestFrmPatternType_Object = MibTableColumn
lpJT2TestFrmPatternType = _LpJT2TestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 4),
    _LpJT2TestFrmPatternType_Type()
)
lpJT2TestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestFrmPatternType.setStatus("mandatory")


class _LpJT2TestCustomizedPattern_Type(Hex):
    """Custom type lpJT2TestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpJT2TestCustomizedPattern_Type.__name__ = "Hex"
_LpJT2TestCustomizedPattern_Object = MibTableColumn
lpJT2TestCustomizedPattern = _LpJT2TestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 5),
    _LpJT2TestCustomizedPattern_Type()
)
lpJT2TestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestCustomizedPattern.setStatus("mandatory")


class _LpJT2TestDataStartDelay_Type(Unsigned32):
    """Custom type lpJT2TestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpJT2TestDataStartDelay_Type.__name__ = "Unsigned32"
_LpJT2TestDataStartDelay_Object = MibTableColumn
lpJT2TestDataStartDelay = _LpJT2TestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 6),
    _LpJT2TestDataStartDelay_Type()
)
lpJT2TestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestDataStartDelay.setStatus("mandatory")


class _LpJT2TestDisplayInterval_Type(Unsigned32):
    """Custom type lpJT2TestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpJT2TestDisplayInterval_Type.__name__ = "Unsigned32"
_LpJT2TestDisplayInterval_Object = MibTableColumn
lpJT2TestDisplayInterval = _LpJT2TestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 7),
    _LpJT2TestDisplayInterval_Type()
)
lpJT2TestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestDisplayInterval.setStatus("mandatory")


class _LpJT2TestDuration_Type(Unsigned32):
    """Custom type lpJT2TestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpJT2TestDuration_Type.__name__ = "Unsigned32"
_LpJT2TestDuration_Object = MibTableColumn
lpJT2TestDuration = _LpJT2TestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 11, 1, 8),
    _LpJT2TestDuration_Type()
)
lpJT2TestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2TestDuration.setStatus("mandatory")
_LpJT2TestResultsTable_Object = MibTable
lpJT2TestResultsTable = _LpJT2TestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12)
)
if mibBuilder.loadTexts:
    lpJT2TestResultsTable.setStatus("mandatory")
_LpJT2TestResultsEntry_Object = MibTableRow
lpJT2TestResultsEntry = _LpJT2TestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1)
)
lpJT2TestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2TestIndex"),
)
if mibBuilder.loadTexts:
    lpJT2TestResultsEntry.setStatus("mandatory")
_LpJT2TestElapsedTime_Type = Counter32
_LpJT2TestElapsedTime_Object = MibTableColumn
lpJT2TestElapsedTime = _LpJT2TestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 1),
    _LpJT2TestElapsedTime_Type()
)
lpJT2TestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestElapsedTime.setStatus("mandatory")


class _LpJT2TestTimeRemaining_Type(Unsigned32):
    """Custom type lpJT2TestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpJT2TestTimeRemaining_Type.__name__ = "Unsigned32"
_LpJT2TestTimeRemaining_Object = MibTableColumn
lpJT2TestTimeRemaining = _LpJT2TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 2),
    _LpJT2TestTimeRemaining_Type()
)
lpJT2TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestTimeRemaining.setStatus("mandatory")


class _LpJT2TestCauseOfTermination_Type(Integer32):
    """Custom type lpJT2TestCauseOfTermination based on Integer32"""
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


_LpJT2TestCauseOfTermination_Type.__name__ = "Integer32"
_LpJT2TestCauseOfTermination_Object = MibTableColumn
lpJT2TestCauseOfTermination = _LpJT2TestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 3),
    _LpJT2TestCauseOfTermination_Type()
)
lpJT2TestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestCauseOfTermination.setStatus("mandatory")
_LpJT2TestBitsTx_Type = PassportCounter64
_LpJT2TestBitsTx_Object = MibTableColumn
lpJT2TestBitsTx = _LpJT2TestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 4),
    _LpJT2TestBitsTx_Type()
)
lpJT2TestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestBitsTx.setStatus("mandatory")
_LpJT2TestBytesTx_Type = PassportCounter64
_LpJT2TestBytesTx_Object = MibTableColumn
lpJT2TestBytesTx = _LpJT2TestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 5),
    _LpJT2TestBytesTx_Type()
)
lpJT2TestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestBytesTx.setStatus("mandatory")
_LpJT2TestFrmTx_Type = PassportCounter64
_LpJT2TestFrmTx_Object = MibTableColumn
lpJT2TestFrmTx = _LpJT2TestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 6),
    _LpJT2TestFrmTx_Type()
)
lpJT2TestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestFrmTx.setStatus("mandatory")
_LpJT2TestBitsRx_Type = PassportCounter64
_LpJT2TestBitsRx_Object = MibTableColumn
lpJT2TestBitsRx = _LpJT2TestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 7),
    _LpJT2TestBitsRx_Type()
)
lpJT2TestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestBitsRx.setStatus("mandatory")
_LpJT2TestBytesRx_Type = PassportCounter64
_LpJT2TestBytesRx_Object = MibTableColumn
lpJT2TestBytesRx = _LpJT2TestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 8),
    _LpJT2TestBytesRx_Type()
)
lpJT2TestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestBytesRx.setStatus("mandatory")
_LpJT2TestFrmRx_Type = PassportCounter64
_LpJT2TestFrmRx_Object = MibTableColumn
lpJT2TestFrmRx = _LpJT2TestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 9),
    _LpJT2TestFrmRx_Type()
)
lpJT2TestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestFrmRx.setStatus("mandatory")
_LpJT2TestErroredFrmRx_Type = PassportCounter64
_LpJT2TestErroredFrmRx_Object = MibTableColumn
lpJT2TestErroredFrmRx = _LpJT2TestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 10),
    _LpJT2TestErroredFrmRx_Type()
)
lpJT2TestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestErroredFrmRx.setStatus("mandatory")


class _LpJT2TestBitErrorRate_Type(AsciiString):
    """Custom type lpJT2TestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpJT2TestBitErrorRate_Type.__name__ = "AsciiString"
_LpJT2TestBitErrorRate_Object = MibTableColumn
lpJT2TestBitErrorRate = _LpJT2TestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 2, 12, 1, 11),
    _LpJT2TestBitErrorRate_Type()
)
lpJT2TestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TestBitErrorRate.setStatus("mandatory")
_LpJT2Cell_ObjectIdentity = ObjectIdentity
lpJT2Cell = _LpJT2Cell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3)
)
_LpJT2CellRowStatusTable_Object = MibTable
lpJT2CellRowStatusTable = _LpJT2CellRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 1)
)
if mibBuilder.loadTexts:
    lpJT2CellRowStatusTable.setStatus("mandatory")
_LpJT2CellRowStatusEntry_Object = MibTableRow
lpJT2CellRowStatusEntry = _LpJT2CellRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 1, 1)
)
lpJT2CellRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2CellIndex"),
)
if mibBuilder.loadTexts:
    lpJT2CellRowStatusEntry.setStatus("mandatory")
_LpJT2CellRowStatus_Type = RowStatus
_LpJT2CellRowStatus_Object = MibTableColumn
lpJT2CellRowStatus = _LpJT2CellRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 1, 1, 1),
    _LpJT2CellRowStatus_Type()
)
lpJT2CellRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellRowStatus.setStatus("mandatory")
_LpJT2CellComponentName_Type = DisplayString
_LpJT2CellComponentName_Object = MibTableColumn
lpJT2CellComponentName = _LpJT2CellComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 1, 1, 2),
    _LpJT2CellComponentName_Type()
)
lpJT2CellComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellComponentName.setStatus("mandatory")
_LpJT2CellStorageType_Type = StorageType
_LpJT2CellStorageType_Object = MibTableColumn
lpJT2CellStorageType = _LpJT2CellStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 1, 1, 4),
    _LpJT2CellStorageType_Type()
)
lpJT2CellStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellStorageType.setStatus("mandatory")
_LpJT2CellIndex_Type = NonReplicated
_LpJT2CellIndex_Object = MibTableColumn
lpJT2CellIndex = _LpJT2CellIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 1, 1, 10),
    _LpJT2CellIndex_Type()
)
lpJT2CellIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpJT2CellIndex.setStatus("mandatory")
_LpJT2CellProvTable_Object = MibTable
lpJT2CellProvTable = _LpJT2CellProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 10)
)
if mibBuilder.loadTexts:
    lpJT2CellProvTable.setStatus("mandatory")
_LpJT2CellProvEntry_Object = MibTableRow
lpJT2CellProvEntry = _LpJT2CellProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 10, 1)
)
lpJT2CellProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2CellIndex"),
)
if mibBuilder.loadTexts:
    lpJT2CellProvEntry.setStatus("mandatory")


class _LpJT2CellAlarmActDelay_Type(Unsigned32):
    """Custom type lpJT2CellAlarmActDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_LpJT2CellAlarmActDelay_Type.__name__ = "Unsigned32"
_LpJT2CellAlarmActDelay_Object = MibTableColumn
lpJT2CellAlarmActDelay = _LpJT2CellAlarmActDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 10, 1, 1),
    _LpJT2CellAlarmActDelay_Type()
)
lpJT2CellAlarmActDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2CellAlarmActDelay.setStatus("mandatory")


class _LpJT2CellScrambleCellPayload_Type(Integer32):
    """Custom type lpJT2CellScrambleCellPayload based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpJT2CellScrambleCellPayload_Type.__name__ = "Integer32"
_LpJT2CellScrambleCellPayload_Object = MibTableColumn
lpJT2CellScrambleCellPayload = _LpJT2CellScrambleCellPayload_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 10, 1, 2),
    _LpJT2CellScrambleCellPayload_Type()
)
lpJT2CellScrambleCellPayload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2CellScrambleCellPayload.setStatus("mandatory")


class _LpJT2CellCorrectSingleBitHeaderErrors_Type(Integer32):
    """Custom type lpJT2CellCorrectSingleBitHeaderErrors based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_LpJT2CellCorrectSingleBitHeaderErrors_Type.__name__ = "Integer32"
_LpJT2CellCorrectSingleBitHeaderErrors_Object = MibTableColumn
lpJT2CellCorrectSingleBitHeaderErrors = _LpJT2CellCorrectSingleBitHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 10, 1, 3),
    _LpJT2CellCorrectSingleBitHeaderErrors_Type()
)
lpJT2CellCorrectSingleBitHeaderErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2CellCorrectSingleBitHeaderErrors.setStatus("mandatory")
_LpJT2CellOperTable_Object = MibTable
lpJT2CellOperTable = _LpJT2CellOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 11)
)
if mibBuilder.loadTexts:
    lpJT2CellOperTable.setStatus("mandatory")
_LpJT2CellOperEntry_Object = MibTableRow
lpJT2CellOperEntry = _LpJT2CellOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 11, 1)
)
lpJT2CellOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2CellIndex"),
)
if mibBuilder.loadTexts:
    lpJT2CellOperEntry.setStatus("mandatory")


class _LpJT2CellLcdAlarm_Type(Integer32):
    """Custom type lpJT2CellLcdAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2CellLcdAlarm_Type.__name__ = "Integer32"
_LpJT2CellLcdAlarm_Object = MibTableColumn
lpJT2CellLcdAlarm = _LpJT2CellLcdAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 11, 1, 1),
    _LpJT2CellLcdAlarm_Type()
)
lpJT2CellLcdAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellLcdAlarm.setStatus("mandatory")
_LpJT2CellStatsTable_Object = MibTable
lpJT2CellStatsTable = _LpJT2CellStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 12)
)
if mibBuilder.loadTexts:
    lpJT2CellStatsTable.setStatus("mandatory")
_LpJT2CellStatsEntry_Object = MibTableRow
lpJT2CellStatsEntry = _LpJT2CellStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 12, 1)
)
lpJT2CellStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2CellIndex"),
)
if mibBuilder.loadTexts:
    lpJT2CellStatsEntry.setStatus("mandatory")
_LpJT2CellUncorrectableHecErrors_Type = Counter32
_LpJT2CellUncorrectableHecErrors_Object = MibTableColumn
lpJT2CellUncorrectableHecErrors = _LpJT2CellUncorrectableHecErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 12, 1, 1),
    _LpJT2CellUncorrectableHecErrors_Type()
)
lpJT2CellUncorrectableHecErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellUncorrectableHecErrors.setStatus("mandatory")
_LpJT2CellSevErroredSec_Type = Counter32
_LpJT2CellSevErroredSec_Object = MibTableColumn
lpJT2CellSevErroredSec = _LpJT2CellSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 12, 1, 2),
    _LpJT2CellSevErroredSec_Type()
)
lpJT2CellSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellSevErroredSec.setStatus("mandatory")


class _LpJT2CellReceiveCellUtilization_Type(Gauge32):
    """Custom type lpJT2CellReceiveCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpJT2CellReceiveCellUtilization_Type.__name__ = "Gauge32"
_LpJT2CellReceiveCellUtilization_Object = MibTableColumn
lpJT2CellReceiveCellUtilization = _LpJT2CellReceiveCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 12, 1, 3),
    _LpJT2CellReceiveCellUtilization_Type()
)
lpJT2CellReceiveCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellReceiveCellUtilization.setStatus("mandatory")


class _LpJT2CellTransmitCellUtilization_Type(Gauge32):
    """Custom type lpJT2CellTransmitCellUtilization based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpJT2CellTransmitCellUtilization_Type.__name__ = "Gauge32"
_LpJT2CellTransmitCellUtilization_Object = MibTableColumn
lpJT2CellTransmitCellUtilization = _LpJT2CellTransmitCellUtilization_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 12, 1, 4),
    _LpJT2CellTransmitCellUtilization_Type()
)
lpJT2CellTransmitCellUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellTransmitCellUtilization.setStatus("mandatory")
_LpJT2CellCorrectableHeaderErrors_Type = Counter32
_LpJT2CellCorrectableHeaderErrors_Object = MibTableColumn
lpJT2CellCorrectableHeaderErrors = _LpJT2CellCorrectableHeaderErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 3, 12, 1, 5),
    _LpJT2CellCorrectableHeaderErrors_Type()
)
lpJT2CellCorrectableHeaderErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CellCorrectableHeaderErrors.setStatus("mandatory")
_LpJT2CidDataTable_Object = MibTable
lpJT2CidDataTable = _LpJT2CidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 10)
)
if mibBuilder.loadTexts:
    lpJT2CidDataTable.setStatus("mandatory")
_LpJT2CidDataEntry_Object = MibTableRow
lpJT2CidDataEntry = _LpJT2CidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 10, 1)
)
lpJT2CidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2CidDataEntry.setStatus("mandatory")


class _LpJT2CustomerIdentifier_Type(Unsigned32):
    """Custom type lpJT2CustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpJT2CustomerIdentifier_Type.__name__ = "Unsigned32"
_LpJT2CustomerIdentifier_Object = MibTableColumn
lpJT2CustomerIdentifier = _LpJT2CustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 10, 1, 1),
    _LpJT2CustomerIdentifier_Type()
)
lpJT2CustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2CustomerIdentifier.setStatus("mandatory")
_LpJT2ProvTable_Object = MibTable
lpJT2ProvTable = _LpJT2ProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 11)
)
if mibBuilder.loadTexts:
    lpJT2ProvTable.setStatus("mandatory")
_LpJT2ProvEntry_Object = MibTableRow
lpJT2ProvEntry = _LpJT2ProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 11, 1)
)
lpJT2ProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2ProvEntry.setStatus("mandatory")


class _LpJT2ClockingSource_Type(Integer32):
    """Custom type lpJT2ClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("local", 0),
          ("module", 2),
          ("otherPort", 4))
    )


_LpJT2ClockingSource_Type.__name__ = "Integer32"
_LpJT2ClockingSource_Object = MibTableColumn
lpJT2ClockingSource = _LpJT2ClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 11, 1, 1),
    _LpJT2ClockingSource_Type()
)
lpJT2ClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2ClockingSource.setStatus("mandatory")


class _LpJT2LineLength_Type(Unsigned32):
    """Custom type lpJT2LineLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 480),
    )


_LpJT2LineLength_Type.__name__ = "Unsigned32"
_LpJT2LineLength_Object = MibTableColumn
lpJT2LineLength = _LpJT2LineLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 11, 1, 2),
    _LpJT2LineLength_Type()
)
lpJT2LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2LineLength.setStatus("mandatory")
_LpJT2ApplicationFramerName_Type = Link
_LpJT2ApplicationFramerName_Object = MibTableColumn
lpJT2ApplicationFramerName = _LpJT2ApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 11, 1, 3),
    _LpJT2ApplicationFramerName_Type()
)
lpJT2ApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2ApplicationFramerName.setStatus("mandatory")
_LpJT2IfEntryTable_Object = MibTable
lpJT2IfEntryTable = _LpJT2IfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 12)
)
if mibBuilder.loadTexts:
    lpJT2IfEntryTable.setStatus("mandatory")
_LpJT2IfEntryEntry_Object = MibTableRow
lpJT2IfEntryEntry = _LpJT2IfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 12, 1)
)
lpJT2IfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2IfEntryEntry.setStatus("mandatory")


class _LpJT2IfAdminStatus_Type(Integer32):
    """Custom type lpJT2IfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpJT2IfAdminStatus_Type.__name__ = "Integer32"
_LpJT2IfAdminStatus_Object = MibTableColumn
lpJT2IfAdminStatus = _LpJT2IfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 12, 1, 1),
    _LpJT2IfAdminStatus_Type()
)
lpJT2IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2IfAdminStatus.setStatus("mandatory")


class _LpJT2IfIndex_Type(InterfaceIndex):
    """Custom type lpJT2IfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpJT2IfIndex_Type.__name__ = "InterfaceIndex"
_LpJT2IfIndex_Object = MibTableColumn
lpJT2IfIndex = _LpJT2IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 12, 1, 2),
    _LpJT2IfIndex_Type()
)
lpJT2IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2IfIndex.setStatus("mandatory")
_LpJT2OperStatusTable_Object = MibTable
lpJT2OperStatusTable = _LpJT2OperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 13)
)
if mibBuilder.loadTexts:
    lpJT2OperStatusTable.setStatus("mandatory")
_LpJT2OperStatusEntry_Object = MibTableRow
lpJT2OperStatusEntry = _LpJT2OperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 13, 1)
)
lpJT2OperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2OperStatusEntry.setStatus("mandatory")


class _LpJT2SnmpOperStatus_Type(Integer32):
    """Custom type lpJT2SnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpJT2SnmpOperStatus_Type.__name__ = "Integer32"
_LpJT2SnmpOperStatus_Object = MibTableColumn
lpJT2SnmpOperStatus = _LpJT2SnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 13, 1, 1),
    _LpJT2SnmpOperStatus_Type()
)
lpJT2SnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2SnmpOperStatus.setStatus("mandatory")
_LpJT2StateTable_Object = MibTable
lpJT2StateTable = _LpJT2StateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14)
)
if mibBuilder.loadTexts:
    lpJT2StateTable.setStatus("mandatory")
_LpJT2StateEntry_Object = MibTableRow
lpJT2StateEntry = _LpJT2StateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1)
)
lpJT2StateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2StateEntry.setStatus("mandatory")


class _LpJT2AdminState_Type(Integer32):
    """Custom type lpJT2AdminState based on Integer32"""
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


_LpJT2AdminState_Type.__name__ = "Integer32"
_LpJT2AdminState_Object = MibTableColumn
lpJT2AdminState = _LpJT2AdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 1),
    _LpJT2AdminState_Type()
)
lpJT2AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2AdminState.setStatus("mandatory")


class _LpJT2OperationalState_Type(Integer32):
    """Custom type lpJT2OperationalState based on Integer32"""
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


_LpJT2OperationalState_Type.__name__ = "Integer32"
_LpJT2OperationalState_Object = MibTableColumn
lpJT2OperationalState = _LpJT2OperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 2),
    _LpJT2OperationalState_Type()
)
lpJT2OperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2OperationalState.setStatus("mandatory")


class _LpJT2UsageState_Type(Integer32):
    """Custom type lpJT2UsageState based on Integer32"""
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


_LpJT2UsageState_Type.__name__ = "Integer32"
_LpJT2UsageState_Object = MibTableColumn
lpJT2UsageState = _LpJT2UsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 3),
    _LpJT2UsageState_Type()
)
lpJT2UsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2UsageState.setStatus("mandatory")


class _LpJT2AvailabilityStatus_Type(OctetString):
    """Custom type lpJT2AvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpJT2AvailabilityStatus_Type.__name__ = "OctetString"
_LpJT2AvailabilityStatus_Object = MibTableColumn
lpJT2AvailabilityStatus = _LpJT2AvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 4),
    _LpJT2AvailabilityStatus_Type()
)
lpJT2AvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2AvailabilityStatus.setStatus("mandatory")


class _LpJT2ProceduralStatus_Type(OctetString):
    """Custom type lpJT2ProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpJT2ProceduralStatus_Type.__name__ = "OctetString"
_LpJT2ProceduralStatus_Object = MibTableColumn
lpJT2ProceduralStatus = _LpJT2ProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 5),
    _LpJT2ProceduralStatus_Type()
)
lpJT2ProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2ProceduralStatus.setStatus("mandatory")


class _LpJT2ControlStatus_Type(OctetString):
    """Custom type lpJT2ControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpJT2ControlStatus_Type.__name__ = "OctetString"
_LpJT2ControlStatus_Object = MibTableColumn
lpJT2ControlStatus = _LpJT2ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 6),
    _LpJT2ControlStatus_Type()
)
lpJT2ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2ControlStatus.setStatus("mandatory")


class _LpJT2AlarmStatus_Type(OctetString):
    """Custom type lpJT2AlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpJT2AlarmStatus_Type.__name__ = "OctetString"
_LpJT2AlarmStatus_Object = MibTableColumn
lpJT2AlarmStatus = _LpJT2AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 7),
    _LpJT2AlarmStatus_Type()
)
lpJT2AlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2AlarmStatus.setStatus("mandatory")


class _LpJT2StandbyStatus_Type(Integer32):
    """Custom type lpJT2StandbyStatus based on Integer32"""
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


_LpJT2StandbyStatus_Type.__name__ = "Integer32"
_LpJT2StandbyStatus_Object = MibTableColumn
lpJT2StandbyStatus = _LpJT2StandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 8),
    _LpJT2StandbyStatus_Type()
)
lpJT2StandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2StandbyStatus.setStatus("mandatory")


class _LpJT2UnknownStatus_Type(Integer32):
    """Custom type lpJT2UnknownStatus based on Integer32"""
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


_LpJT2UnknownStatus_Type.__name__ = "Integer32"
_LpJT2UnknownStatus_Object = MibTableColumn
lpJT2UnknownStatus = _LpJT2UnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 14, 1, 9),
    _LpJT2UnknownStatus_Type()
)
lpJT2UnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2UnknownStatus.setStatus("mandatory")
_LpJT2OperTable_Object = MibTable
lpJT2OperTable = _LpJT2OperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15)
)
if mibBuilder.loadTexts:
    lpJT2OperTable.setStatus("mandatory")
_LpJT2OperEntry_Object = MibTableRow
lpJT2OperEntry = _LpJT2OperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1)
)
lpJT2OperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2OperEntry.setStatus("mandatory")


class _LpJT2LosAlarm_Type(Integer32):
    """Custom type lpJT2LosAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2LosAlarm_Type.__name__ = "Integer32"
_LpJT2LosAlarm_Object = MibTableColumn
lpJT2LosAlarm = _LpJT2LosAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1, 1),
    _LpJT2LosAlarm_Type()
)
lpJT2LosAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2LosAlarm.setStatus("mandatory")


class _LpJT2LofAlarm_Type(Integer32):
    """Custom type lpJT2LofAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2LofAlarm_Type.__name__ = "Integer32"
_LpJT2LofAlarm_Object = MibTableColumn
lpJT2LofAlarm = _LpJT2LofAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1, 2),
    _LpJT2LofAlarm_Type()
)
lpJT2LofAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2LofAlarm.setStatus("mandatory")


class _LpJT2RxAisPhysicalAlarm_Type(Integer32):
    """Custom type lpJT2RxAisPhysicalAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2RxAisPhysicalAlarm_Type.__name__ = "Integer32"
_LpJT2RxAisPhysicalAlarm_Object = MibTableColumn
lpJT2RxAisPhysicalAlarm = _LpJT2RxAisPhysicalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1, 3),
    _LpJT2RxAisPhysicalAlarm_Type()
)
lpJT2RxAisPhysicalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2RxAisPhysicalAlarm.setStatus("mandatory")


class _LpJT2RxAisPayloadAlarm_Type(Integer32):
    """Custom type lpJT2RxAisPayloadAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2RxAisPayloadAlarm_Type.__name__ = "Integer32"
_LpJT2RxAisPayloadAlarm_Object = MibTableColumn
lpJT2RxAisPayloadAlarm = _LpJT2RxAisPayloadAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1, 4),
    _LpJT2RxAisPayloadAlarm_Type()
)
lpJT2RxAisPayloadAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2RxAisPayloadAlarm.setStatus("mandatory")


class _LpJT2RxRaiAlarm_Type(Integer32):
    """Custom type lpJT2RxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2RxRaiAlarm_Type.__name__ = "Integer32"
_LpJT2RxRaiAlarm_Object = MibTableColumn
lpJT2RxRaiAlarm = _LpJT2RxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1, 5),
    _LpJT2RxRaiAlarm_Type()
)
lpJT2RxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2RxRaiAlarm.setStatus("mandatory")


class _LpJT2TxAisPhysicalAlarm_Type(Integer32):
    """Custom type lpJT2TxAisPhysicalAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2TxAisPhysicalAlarm_Type.__name__ = "Integer32"
_LpJT2TxAisPhysicalAlarm_Object = MibTableColumn
lpJT2TxAisPhysicalAlarm = _LpJT2TxAisPhysicalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1, 6),
    _LpJT2TxAisPhysicalAlarm_Type()
)
lpJT2TxAisPhysicalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TxAisPhysicalAlarm.setStatus("mandatory")


class _LpJT2TxRaiAlarm_Type(Integer32):
    """Custom type lpJT2TxRaiAlarm based on Integer32"""
    defaultValue = 1

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


_LpJT2TxRaiAlarm_Type.__name__ = "Integer32"
_LpJT2TxRaiAlarm_Object = MibTableColumn
lpJT2TxRaiAlarm = _LpJT2TxRaiAlarm_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 15, 1, 7),
    _LpJT2TxRaiAlarm_Type()
)
lpJT2TxRaiAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2TxRaiAlarm.setStatus("mandatory")
_LpJT2StatsTable_Object = MibTable
lpJT2StatsTable = _LpJT2StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16)
)
if mibBuilder.loadTexts:
    lpJT2StatsTable.setStatus("mandatory")
_LpJT2StatsEntry_Object = MibTableRow
lpJT2StatsEntry = _LpJT2StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1)
)
lpJT2StatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2StatsEntry.setStatus("mandatory")
_LpJT2RunningTime_Type = Counter32
_LpJT2RunningTime_Object = MibTableColumn
lpJT2RunningTime = _LpJT2RunningTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 1),
    _LpJT2RunningTime_Type()
)
lpJT2RunningTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2RunningTime.setStatus("mandatory")
_LpJT2ErrorFreeSec_Type = Counter32
_LpJT2ErrorFreeSec_Object = MibTableColumn
lpJT2ErrorFreeSec = _LpJT2ErrorFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 2),
    _LpJT2ErrorFreeSec_Type()
)
lpJT2ErrorFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2ErrorFreeSec.setStatus("mandatory")
_LpJT2ErroredSec_Type = Counter32
_LpJT2ErroredSec_Object = MibTableColumn
lpJT2ErroredSec = _LpJT2ErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 3),
    _LpJT2ErroredSec_Type()
)
lpJT2ErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2ErroredSec.setStatus("mandatory")
_LpJT2SevErroredSec_Type = Counter32
_LpJT2SevErroredSec_Object = MibTableColumn
lpJT2SevErroredSec = _LpJT2SevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 4),
    _LpJT2SevErroredSec_Type()
)
lpJT2SevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2SevErroredSec.setStatus("mandatory")
_LpJT2SevErroredFrmSec_Type = Counter32
_LpJT2SevErroredFrmSec_Object = MibTableColumn
lpJT2SevErroredFrmSec = _LpJT2SevErroredFrmSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 5),
    _LpJT2SevErroredFrmSec_Type()
)
lpJT2SevErroredFrmSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2SevErroredFrmSec.setStatus("mandatory")
_LpJT2UnavailSec_Type = Counter32
_LpJT2UnavailSec_Object = MibTableColumn
lpJT2UnavailSec = _LpJT2UnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 6),
    _LpJT2UnavailSec_Type()
)
lpJT2UnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2UnavailSec.setStatus("mandatory")
_LpJT2BpvErrors_Type = Counter32
_LpJT2BpvErrors_Object = MibTableColumn
lpJT2BpvErrors = _LpJT2BpvErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 7),
    _LpJT2BpvErrors_Type()
)
lpJT2BpvErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2BpvErrors.setStatus("mandatory")
_LpJT2CrcErrors_Type = Counter32
_LpJT2CrcErrors_Object = MibTableColumn
lpJT2CrcErrors = _LpJT2CrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 8),
    _LpJT2CrcErrors_Type()
)
lpJT2CrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2CrcErrors.setStatus("mandatory")
_LpJT2FrameErrors_Type = Counter32
_LpJT2FrameErrors_Object = MibTableColumn
lpJT2FrameErrors = _LpJT2FrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 9),
    _LpJT2FrameErrors_Type()
)
lpJT2FrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2FrameErrors.setStatus("mandatory")
_LpJT2LosStateChanges_Type = Counter32
_LpJT2LosStateChanges_Object = MibTableColumn
lpJT2LosStateChanges = _LpJT2LosStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 16, 1, 10),
    _LpJT2LosStateChanges_Type()
)
lpJT2LosStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpJT2LosStateChanges.setStatus("mandatory")
_LpJT2AdminInfoTable_Object = MibTable
lpJT2AdminInfoTable = _LpJT2AdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 17)
)
if mibBuilder.loadTexts:
    lpJT2AdminInfoTable.setStatus("mandatory")
_LpJT2AdminInfoEntry_Object = MibTableRow
lpJT2AdminInfoEntry = _LpJT2AdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 17, 1)
)
lpJT2AdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpJT2Index"),
)
if mibBuilder.loadTexts:
    lpJT2AdminInfoEntry.setStatus("mandatory")


class _LpJT2Vendor_Type(AsciiString):
    """Custom type lpJT2Vendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpJT2Vendor_Type.__name__ = "AsciiString"
_LpJT2Vendor_Object = MibTableColumn
lpJT2Vendor = _LpJT2Vendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 17, 1, 1),
    _LpJT2Vendor_Type()
)
lpJT2Vendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2Vendor.setStatus("mandatory")


class _LpJT2CommentText_Type(AsciiString):
    """Custom type lpJT2CommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpJT2CommentText_Type.__name__ = "AsciiString"
_LpJT2CommentText_Object = MibTableColumn
lpJT2CommentText = _LpJT2CommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 16, 17, 1, 2),
    _LpJT2CommentText_Type()
)
lpJT2CommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpJT2CommentText.setStatus("mandatory")
_LpHssi_ObjectIdentity = ObjectIdentity
lpHssi = _LpHssi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17)
)
_LpHssiRowStatusTable_Object = MibTable
lpHssiRowStatusTable = _LpHssiRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 1)
)
if mibBuilder.loadTexts:
    lpHssiRowStatusTable.setStatus("mandatory")
_LpHssiRowStatusEntry_Object = MibTableRow
lpHssiRowStatusEntry = _LpHssiRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 1, 1)
)
lpHssiRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiRowStatusEntry.setStatus("mandatory")
_LpHssiRowStatus_Type = RowStatus
_LpHssiRowStatus_Object = MibTableColumn
lpHssiRowStatus = _LpHssiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 1, 1, 1),
    _LpHssiRowStatus_Type()
)
lpHssiRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiRowStatus.setStatus("mandatory")
_LpHssiComponentName_Type = DisplayString
_LpHssiComponentName_Object = MibTableColumn
lpHssiComponentName = _LpHssiComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 1, 1, 2),
    _LpHssiComponentName_Type()
)
lpHssiComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiComponentName.setStatus("mandatory")
_LpHssiStorageType_Type = StorageType
_LpHssiStorageType_Object = MibTableColumn
lpHssiStorageType = _LpHssiStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 1, 1, 4),
    _LpHssiStorageType_Type()
)
lpHssiStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiStorageType.setStatus("mandatory")


class _LpHssiIndex_Type(Integer32):
    """Custom type lpHssiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LpHssiIndex_Type.__name__ = "Integer32"
_LpHssiIndex_Object = MibTableColumn
lpHssiIndex = _LpHssiIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 1, 1, 10),
    _LpHssiIndex_Type()
)
lpHssiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpHssiIndex.setStatus("mandatory")
_LpHssiTest_ObjectIdentity = ObjectIdentity
lpHssiTest = _LpHssiTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2)
)
_LpHssiTestRowStatusTable_Object = MibTable
lpHssiTestRowStatusTable = _LpHssiTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 1)
)
if mibBuilder.loadTexts:
    lpHssiTestRowStatusTable.setStatus("mandatory")
_LpHssiTestRowStatusEntry_Object = MibTableRow
lpHssiTestRowStatusEntry = _LpHssiTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 1, 1)
)
lpHssiTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiTestIndex"),
)
if mibBuilder.loadTexts:
    lpHssiTestRowStatusEntry.setStatus("mandatory")
_LpHssiTestRowStatus_Type = RowStatus
_LpHssiTestRowStatus_Object = MibTableColumn
lpHssiTestRowStatus = _LpHssiTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 1, 1, 1),
    _LpHssiTestRowStatus_Type()
)
lpHssiTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestRowStatus.setStatus("mandatory")
_LpHssiTestComponentName_Type = DisplayString
_LpHssiTestComponentName_Object = MibTableColumn
lpHssiTestComponentName = _LpHssiTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 1, 1, 2),
    _LpHssiTestComponentName_Type()
)
lpHssiTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestComponentName.setStatus("mandatory")
_LpHssiTestStorageType_Type = StorageType
_LpHssiTestStorageType_Object = MibTableColumn
lpHssiTestStorageType = _LpHssiTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 1, 1, 4),
    _LpHssiTestStorageType_Type()
)
lpHssiTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestStorageType.setStatus("mandatory")
_LpHssiTestIndex_Type = NonReplicated
_LpHssiTestIndex_Object = MibTableColumn
lpHssiTestIndex = _LpHssiTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 1, 1, 10),
    _LpHssiTestIndex_Type()
)
lpHssiTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpHssiTestIndex.setStatus("mandatory")
_LpHssiTestStateTable_Object = MibTable
lpHssiTestStateTable = _LpHssiTestStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 10)
)
if mibBuilder.loadTexts:
    lpHssiTestStateTable.setStatus("mandatory")
_LpHssiTestStateEntry_Object = MibTableRow
lpHssiTestStateEntry = _LpHssiTestStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 10, 1)
)
lpHssiTestStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiTestIndex"),
)
if mibBuilder.loadTexts:
    lpHssiTestStateEntry.setStatus("mandatory")


class _LpHssiTestAdminState_Type(Integer32):
    """Custom type lpHssiTestAdminState based on Integer32"""
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


_LpHssiTestAdminState_Type.__name__ = "Integer32"
_LpHssiTestAdminState_Object = MibTableColumn
lpHssiTestAdminState = _LpHssiTestAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 10, 1, 1),
    _LpHssiTestAdminState_Type()
)
lpHssiTestAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestAdminState.setStatus("mandatory")


class _LpHssiTestOperationalState_Type(Integer32):
    """Custom type lpHssiTestOperationalState based on Integer32"""
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


_LpHssiTestOperationalState_Type.__name__ = "Integer32"
_LpHssiTestOperationalState_Object = MibTableColumn
lpHssiTestOperationalState = _LpHssiTestOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 10, 1, 2),
    _LpHssiTestOperationalState_Type()
)
lpHssiTestOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestOperationalState.setStatus("mandatory")


class _LpHssiTestUsageState_Type(Integer32):
    """Custom type lpHssiTestUsageState based on Integer32"""
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


_LpHssiTestUsageState_Type.__name__ = "Integer32"
_LpHssiTestUsageState_Object = MibTableColumn
lpHssiTestUsageState = _LpHssiTestUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 10, 1, 3),
    _LpHssiTestUsageState_Type()
)
lpHssiTestUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestUsageState.setStatus("mandatory")
_LpHssiTestSetupTable_Object = MibTable
lpHssiTestSetupTable = _LpHssiTestSetupTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11)
)
if mibBuilder.loadTexts:
    lpHssiTestSetupTable.setStatus("mandatory")
_LpHssiTestSetupEntry_Object = MibTableRow
lpHssiTestSetupEntry = _LpHssiTestSetupEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1)
)
lpHssiTestSetupEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiTestIndex"),
)
if mibBuilder.loadTexts:
    lpHssiTestSetupEntry.setStatus("mandatory")


class _LpHssiTestPurpose_Type(AsciiString):
    """Custom type lpHssiTestPurpose based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_LpHssiTestPurpose_Type.__name__ = "AsciiString"
_LpHssiTestPurpose_Object = MibTableColumn
lpHssiTestPurpose = _LpHssiTestPurpose_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 1),
    _LpHssiTestPurpose_Type()
)
lpHssiTestPurpose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestPurpose.setStatus("mandatory")


class _LpHssiTestType_Type(Integer32):
    """Custom type lpHssiTestType based on Integer32"""
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


_LpHssiTestType_Type.__name__ = "Integer32"
_LpHssiTestType_Object = MibTableColumn
lpHssiTestType = _LpHssiTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 2),
    _LpHssiTestType_Type()
)
lpHssiTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestType.setStatus("mandatory")


class _LpHssiTestFrmSize_Type(Unsigned32):
    """Custom type lpHssiTestFrmSize based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 4096),
    )


_LpHssiTestFrmSize_Type.__name__ = "Unsigned32"
_LpHssiTestFrmSize_Object = MibTableColumn
lpHssiTestFrmSize = _LpHssiTestFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 3),
    _LpHssiTestFrmSize_Type()
)
lpHssiTestFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestFrmSize.setStatus("mandatory")


class _LpHssiTestFrmPatternType_Type(Integer32):
    """Custom type lpHssiTestFrmPatternType based on Integer32"""
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


_LpHssiTestFrmPatternType_Type.__name__ = "Integer32"
_LpHssiTestFrmPatternType_Object = MibTableColumn
lpHssiTestFrmPatternType = _LpHssiTestFrmPatternType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 4),
    _LpHssiTestFrmPatternType_Type()
)
lpHssiTestFrmPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestFrmPatternType.setStatus("mandatory")


class _LpHssiTestCustomizedPattern_Type(Hex):
    """Custom type lpHssiTestCustomizedPattern based on Hex"""
    defaultValue = 1431655765

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpHssiTestCustomizedPattern_Type.__name__ = "Hex"
_LpHssiTestCustomizedPattern_Object = MibTableColumn
lpHssiTestCustomizedPattern = _LpHssiTestCustomizedPattern_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 5),
    _LpHssiTestCustomizedPattern_Type()
)
lpHssiTestCustomizedPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestCustomizedPattern.setStatus("mandatory")


class _LpHssiTestDataStartDelay_Type(Unsigned32):
    """Custom type lpHssiTestDataStartDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1814400),
    )


_LpHssiTestDataStartDelay_Type.__name__ = "Unsigned32"
_LpHssiTestDataStartDelay_Object = MibTableColumn
lpHssiTestDataStartDelay = _LpHssiTestDataStartDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 6),
    _LpHssiTestDataStartDelay_Type()
)
lpHssiTestDataStartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestDataStartDelay.setStatus("mandatory")


class _LpHssiTestDisplayInterval_Type(Unsigned32):
    """Custom type lpHssiTestDisplayInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30240),
    )


_LpHssiTestDisplayInterval_Type.__name__ = "Unsigned32"
_LpHssiTestDisplayInterval_Object = MibTableColumn
lpHssiTestDisplayInterval = _LpHssiTestDisplayInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 7),
    _LpHssiTestDisplayInterval_Type()
)
lpHssiTestDisplayInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestDisplayInterval.setStatus("mandatory")


class _LpHssiTestDuration_Type(Unsigned32):
    """Custom type lpHssiTestDuration based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30240),
    )


_LpHssiTestDuration_Type.__name__ = "Unsigned32"
_LpHssiTestDuration_Object = MibTableColumn
lpHssiTestDuration = _LpHssiTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 11, 1, 8),
    _LpHssiTestDuration_Type()
)
lpHssiTestDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiTestDuration.setStatus("mandatory")
_LpHssiTestResultsTable_Object = MibTable
lpHssiTestResultsTable = _LpHssiTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12)
)
if mibBuilder.loadTexts:
    lpHssiTestResultsTable.setStatus("mandatory")
_LpHssiTestResultsEntry_Object = MibTableRow
lpHssiTestResultsEntry = _LpHssiTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1)
)
lpHssiTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiTestIndex"),
)
if mibBuilder.loadTexts:
    lpHssiTestResultsEntry.setStatus("mandatory")
_LpHssiTestElapsedTime_Type = Counter32
_LpHssiTestElapsedTime_Object = MibTableColumn
lpHssiTestElapsedTime = _LpHssiTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 1),
    _LpHssiTestElapsedTime_Type()
)
lpHssiTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestElapsedTime.setStatus("mandatory")


class _LpHssiTestTimeRemaining_Type(Unsigned32):
    """Custom type lpHssiTestTimeRemaining based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpHssiTestTimeRemaining_Type.__name__ = "Unsigned32"
_LpHssiTestTimeRemaining_Object = MibTableColumn
lpHssiTestTimeRemaining = _LpHssiTestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 2),
    _LpHssiTestTimeRemaining_Type()
)
lpHssiTestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestTimeRemaining.setStatus("mandatory")


class _LpHssiTestCauseOfTermination_Type(Integer32):
    """Custom type lpHssiTestCauseOfTermination based on Integer32"""
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


_LpHssiTestCauseOfTermination_Type.__name__ = "Integer32"
_LpHssiTestCauseOfTermination_Object = MibTableColumn
lpHssiTestCauseOfTermination = _LpHssiTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 3),
    _LpHssiTestCauseOfTermination_Type()
)
lpHssiTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestCauseOfTermination.setStatus("mandatory")
_LpHssiTestBitsTx_Type = PassportCounter64
_LpHssiTestBitsTx_Object = MibTableColumn
lpHssiTestBitsTx = _LpHssiTestBitsTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 4),
    _LpHssiTestBitsTx_Type()
)
lpHssiTestBitsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestBitsTx.setStatus("mandatory")
_LpHssiTestBytesTx_Type = PassportCounter64
_LpHssiTestBytesTx_Object = MibTableColumn
lpHssiTestBytesTx = _LpHssiTestBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 5),
    _LpHssiTestBytesTx_Type()
)
lpHssiTestBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestBytesTx.setStatus("mandatory")
_LpHssiTestFrmTx_Type = PassportCounter64
_LpHssiTestFrmTx_Object = MibTableColumn
lpHssiTestFrmTx = _LpHssiTestFrmTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 6),
    _LpHssiTestFrmTx_Type()
)
lpHssiTestFrmTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestFrmTx.setStatus("mandatory")
_LpHssiTestBitsRx_Type = PassportCounter64
_LpHssiTestBitsRx_Object = MibTableColumn
lpHssiTestBitsRx = _LpHssiTestBitsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 7),
    _LpHssiTestBitsRx_Type()
)
lpHssiTestBitsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestBitsRx.setStatus("mandatory")
_LpHssiTestBytesRx_Type = PassportCounter64
_LpHssiTestBytesRx_Object = MibTableColumn
lpHssiTestBytesRx = _LpHssiTestBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 8),
    _LpHssiTestBytesRx_Type()
)
lpHssiTestBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestBytesRx.setStatus("mandatory")
_LpHssiTestFrmRx_Type = PassportCounter64
_LpHssiTestFrmRx_Object = MibTableColumn
lpHssiTestFrmRx = _LpHssiTestFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 9),
    _LpHssiTestFrmRx_Type()
)
lpHssiTestFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestFrmRx.setStatus("mandatory")
_LpHssiTestErroredFrmRx_Type = PassportCounter64
_LpHssiTestErroredFrmRx_Object = MibTableColumn
lpHssiTestErroredFrmRx = _LpHssiTestErroredFrmRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 10),
    _LpHssiTestErroredFrmRx_Type()
)
lpHssiTestErroredFrmRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestErroredFrmRx.setStatus("mandatory")


class _LpHssiTestBitErrorRate_Type(AsciiString):
    """Custom type lpHssiTestBitErrorRate based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_LpHssiTestBitErrorRate_Type.__name__ = "AsciiString"
_LpHssiTestBitErrorRate_Object = MibTableColumn
lpHssiTestBitErrorRate = _LpHssiTestBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 2, 12, 1, 11),
    _LpHssiTestBitErrorRate_Type()
)
lpHssiTestBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiTestBitErrorRate.setStatus("mandatory")
_LpHssiProvTable_Object = MibTable
lpHssiProvTable = _LpHssiProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 10)
)
if mibBuilder.loadTexts:
    lpHssiProvTable.setStatus("mandatory")
_LpHssiProvEntry_Object = MibTableRow
lpHssiProvEntry = _LpHssiProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 10, 1)
)
lpHssiProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiProvEntry.setStatus("mandatory")


class _LpHssiLinkMode_Type(Integer32):
    """Custom type lpHssiLinkMode based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dce", 128),
          ("dte", 0))
    )


_LpHssiLinkMode_Type.__name__ = "Integer32"
_LpHssiLinkMode_Object = MibTableColumn
lpHssiLinkMode = _LpHssiLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 10, 1, 1),
    _LpHssiLinkMode_Type()
)
lpHssiLinkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiLinkMode.setStatus("mandatory")


class _LpHssiReadyLineState_Type(OctetString):
    """Custom type lpHssiReadyLineState based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpHssiReadyLineState_Type.__name__ = "OctetString"
_LpHssiReadyLineState_Object = MibTableColumn
lpHssiReadyLineState = _LpHssiReadyLineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 10, 1, 2),
    _LpHssiReadyLineState_Type()
)
lpHssiReadyLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiReadyLineState.setStatus("mandatory")


class _LpHssiDataTransferLineState_Type(OctetString):
    """Custom type lpHssiDataTransferLineState based on OctetString"""
    defaultHexValue = "c0"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpHssiDataTransferLineState_Type.__name__ = "OctetString"
_LpHssiDataTransferLineState_Object = MibTableColumn
lpHssiDataTransferLineState = _LpHssiDataTransferLineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 10, 1, 3),
    _LpHssiDataTransferLineState_Type()
)
lpHssiDataTransferLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiDataTransferLineState.setStatus("mandatory")


class _LpHssiLineSpeed_Type(Unsigned32):
    """Custom type lpHssiLineSpeed based on Unsigned32"""
    defaultValue = 45000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 50000000),
    )


_LpHssiLineSpeed_Type.__name__ = "Unsigned32"
_LpHssiLineSpeed_Object = MibTableColumn
lpHssiLineSpeed = _LpHssiLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 10, 1, 5),
    _LpHssiLineSpeed_Type()
)
lpHssiLineSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiLineSpeed.setStatus("mandatory")
_LpHssiApplicationFramerName_Type = Link
_LpHssiApplicationFramerName_Object = MibTableColumn
lpHssiApplicationFramerName = _LpHssiApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 10, 1, 7),
    _LpHssiApplicationFramerName_Type()
)
lpHssiApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiApplicationFramerName.setStatus("mandatory")
_LpHssiCidDataTable_Object = MibTable
lpHssiCidDataTable = _LpHssiCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 11)
)
if mibBuilder.loadTexts:
    lpHssiCidDataTable.setStatus("mandatory")
_LpHssiCidDataEntry_Object = MibTableRow
lpHssiCidDataEntry = _LpHssiCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 11, 1)
)
lpHssiCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiCidDataEntry.setStatus("mandatory")


class _LpHssiCustomerIdentifier_Type(Unsigned32):
    """Custom type lpHssiCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpHssiCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpHssiCustomerIdentifier_Object = MibTableColumn
lpHssiCustomerIdentifier = _LpHssiCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 11, 1, 1),
    _LpHssiCustomerIdentifier_Type()
)
lpHssiCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiCustomerIdentifier.setStatus("mandatory")
_LpHssiAdminInfoTable_Object = MibTable
lpHssiAdminInfoTable = _LpHssiAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 12)
)
if mibBuilder.loadTexts:
    lpHssiAdminInfoTable.setStatus("mandatory")
_LpHssiAdminInfoEntry_Object = MibTableRow
lpHssiAdminInfoEntry = _LpHssiAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 12, 1)
)
lpHssiAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiAdminInfoEntry.setStatus("mandatory")


class _LpHssiVendor_Type(AsciiString):
    """Custom type lpHssiVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpHssiVendor_Type.__name__ = "AsciiString"
_LpHssiVendor_Object = MibTableColumn
lpHssiVendor = _LpHssiVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 12, 1, 1),
    _LpHssiVendor_Type()
)
lpHssiVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiVendor.setStatus("mandatory")


class _LpHssiCommentText_Type(AsciiString):
    """Custom type lpHssiCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpHssiCommentText_Type.__name__ = "AsciiString"
_LpHssiCommentText_Object = MibTableColumn
lpHssiCommentText = _LpHssiCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 12, 1, 2),
    _LpHssiCommentText_Type()
)
lpHssiCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiCommentText.setStatus("mandatory")
_LpHssiIfEntryTable_Object = MibTable
lpHssiIfEntryTable = _LpHssiIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 13)
)
if mibBuilder.loadTexts:
    lpHssiIfEntryTable.setStatus("mandatory")
_LpHssiIfEntryEntry_Object = MibTableRow
lpHssiIfEntryEntry = _LpHssiIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 13, 1)
)
lpHssiIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiIfEntryEntry.setStatus("mandatory")


class _LpHssiIfAdminStatus_Type(Integer32):
    """Custom type lpHssiIfAdminStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpHssiIfAdminStatus_Type.__name__ = "Integer32"
_LpHssiIfAdminStatus_Object = MibTableColumn
lpHssiIfAdminStatus = _LpHssiIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 13, 1, 1),
    _LpHssiIfAdminStatus_Type()
)
lpHssiIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpHssiIfAdminStatus.setStatus("mandatory")


class _LpHssiIfIndex_Type(InterfaceIndex):
    """Custom type lpHssiIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpHssiIfIndex_Type.__name__ = "InterfaceIndex"
_LpHssiIfIndex_Object = MibTableColumn
lpHssiIfIndex = _LpHssiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 13, 1, 2),
    _LpHssiIfIndex_Type()
)
lpHssiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiIfIndex.setStatus("mandatory")
_LpHssiOperStatusTable_Object = MibTable
lpHssiOperStatusTable = _LpHssiOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 14)
)
if mibBuilder.loadTexts:
    lpHssiOperStatusTable.setStatus("mandatory")
_LpHssiOperStatusEntry_Object = MibTableRow
lpHssiOperStatusEntry = _LpHssiOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 14, 1)
)
lpHssiOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiOperStatusEntry.setStatus("mandatory")


class _LpHssiSnmpOperStatus_Type(Integer32):
    """Custom type lpHssiSnmpOperStatus based on Integer32"""
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_LpHssiSnmpOperStatus_Type.__name__ = "Integer32"
_LpHssiSnmpOperStatus_Object = MibTableColumn
lpHssiSnmpOperStatus = _LpHssiSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 14, 1, 1),
    _LpHssiSnmpOperStatus_Type()
)
lpHssiSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiSnmpOperStatus.setStatus("mandatory")
_LpHssiStateTable_Object = MibTable
lpHssiStateTable = _LpHssiStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15)
)
if mibBuilder.loadTexts:
    lpHssiStateTable.setStatus("mandatory")
_LpHssiStateEntry_Object = MibTableRow
lpHssiStateEntry = _LpHssiStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1)
)
lpHssiStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiStateEntry.setStatus("mandatory")


class _LpHssiAdminState_Type(Integer32):
    """Custom type lpHssiAdminState based on Integer32"""
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


_LpHssiAdminState_Type.__name__ = "Integer32"
_LpHssiAdminState_Object = MibTableColumn
lpHssiAdminState = _LpHssiAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 1),
    _LpHssiAdminState_Type()
)
lpHssiAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiAdminState.setStatus("mandatory")


class _LpHssiOperationalState_Type(Integer32):
    """Custom type lpHssiOperationalState based on Integer32"""
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


_LpHssiOperationalState_Type.__name__ = "Integer32"
_LpHssiOperationalState_Object = MibTableColumn
lpHssiOperationalState = _LpHssiOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 2),
    _LpHssiOperationalState_Type()
)
lpHssiOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiOperationalState.setStatus("mandatory")


class _LpHssiUsageState_Type(Integer32):
    """Custom type lpHssiUsageState based on Integer32"""
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


_LpHssiUsageState_Type.__name__ = "Integer32"
_LpHssiUsageState_Object = MibTableColumn
lpHssiUsageState = _LpHssiUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 3),
    _LpHssiUsageState_Type()
)
lpHssiUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiUsageState.setStatus("mandatory")


class _LpHssiAvailabilityStatus_Type(OctetString):
    """Custom type lpHssiAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpHssiAvailabilityStatus_Type.__name__ = "OctetString"
_LpHssiAvailabilityStatus_Object = MibTableColumn
lpHssiAvailabilityStatus = _LpHssiAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 4),
    _LpHssiAvailabilityStatus_Type()
)
lpHssiAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiAvailabilityStatus.setStatus("mandatory")


class _LpHssiProceduralStatus_Type(OctetString):
    """Custom type lpHssiProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpHssiProceduralStatus_Type.__name__ = "OctetString"
_LpHssiProceduralStatus_Object = MibTableColumn
lpHssiProceduralStatus = _LpHssiProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 5),
    _LpHssiProceduralStatus_Type()
)
lpHssiProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiProceduralStatus.setStatus("mandatory")


class _LpHssiControlStatus_Type(OctetString):
    """Custom type lpHssiControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpHssiControlStatus_Type.__name__ = "OctetString"
_LpHssiControlStatus_Object = MibTableColumn
lpHssiControlStatus = _LpHssiControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 6),
    _LpHssiControlStatus_Type()
)
lpHssiControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiControlStatus.setStatus("mandatory")


class _LpHssiAlarmStatus_Type(OctetString):
    """Custom type lpHssiAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpHssiAlarmStatus_Type.__name__ = "OctetString"
_LpHssiAlarmStatus_Object = MibTableColumn
lpHssiAlarmStatus = _LpHssiAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 7),
    _LpHssiAlarmStatus_Type()
)
lpHssiAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiAlarmStatus.setStatus("mandatory")


class _LpHssiStandbyStatus_Type(Integer32):
    """Custom type lpHssiStandbyStatus based on Integer32"""
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


_LpHssiStandbyStatus_Type.__name__ = "Integer32"
_LpHssiStandbyStatus_Object = MibTableColumn
lpHssiStandbyStatus = _LpHssiStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 8),
    _LpHssiStandbyStatus_Type()
)
lpHssiStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiStandbyStatus.setStatus("mandatory")


class _LpHssiUnknownStatus_Type(Integer32):
    """Custom type lpHssiUnknownStatus based on Integer32"""
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


_LpHssiUnknownStatus_Type.__name__ = "Integer32"
_LpHssiUnknownStatus_Object = MibTableColumn
lpHssiUnknownStatus = _LpHssiUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 15, 1, 9),
    _LpHssiUnknownStatus_Type()
)
lpHssiUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiUnknownStatus.setStatus("mandatory")
_LpHssiOperTable_Object = MibTable
lpHssiOperTable = _LpHssiOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 16)
)
if mibBuilder.loadTexts:
    lpHssiOperTable.setStatus("mandatory")
_LpHssiOperEntry_Object = MibTableRow
lpHssiOperEntry = _LpHssiOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 16, 1)
)
lpHssiOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpHssiIndex"),
)
if mibBuilder.loadTexts:
    lpHssiOperEntry.setStatus("mandatory")


class _LpHssiActualLinkMode_Type(Integer32):
    """Custom type lpHssiActualLinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              128)
        )
    )
    namedValues = NamedValues(
        *(("dce", 128),
          ("dte", 0))
    )


_LpHssiActualLinkMode_Type.__name__ = "Integer32"
_LpHssiActualLinkMode_Object = MibTableColumn
lpHssiActualLinkMode = _LpHssiActualLinkMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 16, 1, 1),
    _LpHssiActualLinkMode_Type()
)
lpHssiActualLinkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiActualLinkMode.setStatus("mandatory")


class _LpHssiLineState_Type(OctetString):
    """Custom type lpHssiLineState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpHssiLineState_Type.__name__ = "OctetString"
_LpHssiLineState_Object = MibTableColumn
lpHssiLineState = _LpHssiLineState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 16, 1, 2),
    _LpHssiLineState_Type()
)
lpHssiLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiLineState.setStatus("mandatory")


class _LpHssiActualTxLineSpeed_Type(Gauge32):
    """Custom type lpHssiActualTxLineSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpHssiActualTxLineSpeed_Type.__name__ = "Gauge32"
_LpHssiActualTxLineSpeed_Object = MibTableColumn
lpHssiActualTxLineSpeed = _LpHssiActualTxLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 16, 1, 3),
    _LpHssiActualTxLineSpeed_Type()
)
lpHssiActualTxLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiActualTxLineSpeed.setStatus("mandatory")


class _LpHssiActualRxLineSpeed_Type(Gauge32):
    """Custom type lpHssiActualRxLineSpeed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpHssiActualRxLineSpeed_Type.__name__ = "Gauge32"
_LpHssiActualRxLineSpeed_Object = MibTableColumn
lpHssiActualRxLineSpeed = _LpHssiActualRxLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 16, 1, 4),
    _LpHssiActualRxLineSpeed_Type()
)
lpHssiActualRxLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiActualRxLineSpeed.setStatus("mandatory")
_LpHssiDataXferStateChanges_Type = Counter32
_LpHssiDataXferStateChanges_Object = MibTableColumn
lpHssiDataXferStateChanges = _LpHssiDataXferStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 17, 16, 1, 5),
    _LpHssiDataXferStateChanges_Type()
)
lpHssiDataXferStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpHssiDataXferStateChanges.setStatus("mandatory")
_LpEng_ObjectIdentity = ObjectIdentity
lpEng = _LpEng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23)
)
_LpEngRowStatusTable_Object = MibTable
lpEngRowStatusTable = _LpEngRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 1)
)
if mibBuilder.loadTexts:
    lpEngRowStatusTable.setStatus("mandatory")
_LpEngRowStatusEntry_Object = MibTableRow
lpEngRowStatusEntry = _LpEngRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 1, 1)
)
lpEngRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
)
if mibBuilder.loadTexts:
    lpEngRowStatusEntry.setStatus("mandatory")
_LpEngRowStatus_Type = RowStatus
_LpEngRowStatus_Object = MibTableColumn
lpEngRowStatus = _LpEngRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 1, 1, 1),
    _LpEngRowStatus_Type()
)
lpEngRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngRowStatus.setStatus("mandatory")
_LpEngComponentName_Type = DisplayString
_LpEngComponentName_Object = MibTableColumn
lpEngComponentName = _LpEngComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 1, 1, 2),
    _LpEngComponentName_Type()
)
lpEngComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngComponentName.setStatus("mandatory")
_LpEngStorageType_Type = StorageType
_LpEngStorageType_Object = MibTableColumn
lpEngStorageType = _LpEngStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 1, 1, 4),
    _LpEngStorageType_Type()
)
lpEngStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngStorageType.setStatus("mandatory")
_LpEngIndex_Type = NonReplicated
_LpEngIndex_Object = MibTableColumn
lpEngIndex = _LpEngIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 1, 1, 10),
    _LpEngIndex_Type()
)
lpEngIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngIndex.setStatus("mandatory")
_LpEngDs_ObjectIdentity = ObjectIdentity
lpEngDs = _LpEngDs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2)
)
_LpEngDsRowStatusTable_Object = MibTable
lpEngDsRowStatusTable = _LpEngDsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngDsRowStatusTable.setStatus("mandatory")
_LpEngDsRowStatusEntry_Object = MibTableRow
lpEngDsRowStatusEntry = _LpEngDsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 1, 1)
)
lpEngDsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngDsIndex"),
)
if mibBuilder.loadTexts:
    lpEngDsRowStatusEntry.setStatus("mandatory")
_LpEngDsRowStatus_Type = RowStatus
_LpEngDsRowStatus_Object = MibTableColumn
lpEngDsRowStatus = _LpEngDsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 1, 1, 1),
    _LpEngDsRowStatus_Type()
)
lpEngDsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngDsRowStatus.setStatus("mandatory")
_LpEngDsComponentName_Type = DisplayString
_LpEngDsComponentName_Object = MibTableColumn
lpEngDsComponentName = _LpEngDsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 1, 1, 2),
    _LpEngDsComponentName_Type()
)
lpEngDsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngDsComponentName.setStatus("mandatory")
_LpEngDsStorageType_Type = StorageType
_LpEngDsStorageType_Object = MibTableColumn
lpEngDsStorageType = _LpEngDsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 1, 1, 4),
    _LpEngDsStorageType_Type()
)
lpEngDsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngDsStorageType.setStatus("mandatory")


class _LpEngDsIndex_Type(Integer32):
    """Custom type lpEngDsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 0),
          ("alarm", 1),
          ("debug", 3),
          ("log", 2),
          ("scn", 4),
          ("stats", 6),
          ("trap", 5))
    )


_LpEngDsIndex_Type.__name__ = "Integer32"
_LpEngDsIndex_Object = MibTableColumn
lpEngDsIndex = _LpEngDsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 1, 1, 10),
    _LpEngDsIndex_Type()
)
lpEngDsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngDsIndex.setStatus("mandatory")
_LpEngDsOv_ObjectIdentity = ObjectIdentity
lpEngDsOv = _LpEngDsOv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2)
)
_LpEngDsOvRowStatusTable_Object = MibTable
lpEngDsOvRowStatusTable = _LpEngDsOvRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lpEngDsOvRowStatusTable.setStatus("mandatory")
_LpEngDsOvRowStatusEntry_Object = MibTableRow
lpEngDsOvRowStatusEntry = _LpEngDsOvRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 1, 1)
)
lpEngDsOvRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngDsIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngDsOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngDsOvRowStatusEntry.setStatus("mandatory")
_LpEngDsOvRowStatus_Type = RowStatus
_LpEngDsOvRowStatus_Object = MibTableColumn
lpEngDsOvRowStatus = _LpEngDsOvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 1, 1, 1),
    _LpEngDsOvRowStatus_Type()
)
lpEngDsOvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngDsOvRowStatus.setStatus("mandatory")
_LpEngDsOvComponentName_Type = DisplayString
_LpEngDsOvComponentName_Object = MibTableColumn
lpEngDsOvComponentName = _LpEngDsOvComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 1, 1, 2),
    _LpEngDsOvComponentName_Type()
)
lpEngDsOvComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngDsOvComponentName.setStatus("mandatory")
_LpEngDsOvStorageType_Type = StorageType
_LpEngDsOvStorageType_Object = MibTableColumn
lpEngDsOvStorageType = _LpEngDsOvStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 1, 1, 4),
    _LpEngDsOvStorageType_Type()
)
lpEngDsOvStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngDsOvStorageType.setStatus("mandatory")
_LpEngDsOvIndex_Type = NonReplicated
_LpEngDsOvIndex_Object = MibTableColumn
lpEngDsOvIndex = _LpEngDsOvIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 1, 1, 10),
    _LpEngDsOvIndex_Type()
)
lpEngDsOvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpEngDsOvIndex.setStatus("mandatory")
_LpEngDsOvProvTable_Object = MibTable
lpEngDsOvProvTable = _LpEngDsOvProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngDsOvProvTable.setStatus("mandatory")
_LpEngDsOvProvEntry_Object = MibTableRow
lpEngDsOvProvEntry = _LpEngDsOvProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 10, 1)
)
lpEngDsOvProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngDsIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngDsOvIndex"),
)
if mibBuilder.loadTexts:
    lpEngDsOvProvEntry.setStatus("mandatory")


class _LpEngDsOvAgentQueueSize_Type(Unsigned32):
    """Custom type lpEngDsOvAgentQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpEngDsOvAgentQueueSize_Type.__name__ = "Unsigned32"
_LpEngDsOvAgentQueueSize_Object = MibTableColumn
lpEngDsOvAgentQueueSize = _LpEngDsOvAgentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 2, 10, 1, 1),
    _LpEngDsOvAgentQueueSize_Type()
)
lpEngDsOvAgentQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpEngDsOvAgentQueueSize.setStatus("mandatory")
_LpEngDsOperTable_Object = MibTable
lpEngDsOperTable = _LpEngDsOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 10)
)
if mibBuilder.loadTexts:
    lpEngDsOperTable.setStatus("mandatory")
_LpEngDsOperEntry_Object = MibTableRow
lpEngDsOperEntry = _LpEngDsOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 10, 1)
)
lpEngDsOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpEngDsIndex"),
)
if mibBuilder.loadTexts:
    lpEngDsOperEntry.setStatus("mandatory")


class _LpEngDsAgentQueueSize_Type(Unsigned32):
    """Custom type lpEngDsAgentQueueSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_LpEngDsAgentQueueSize_Type.__name__ = "Unsigned32"
_LpEngDsAgentQueueSize_Object = MibTableColumn
lpEngDsAgentQueueSize = _LpEngDsAgentQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 23, 2, 10, 1, 1),
    _LpEngDsAgentQueueSize_Type()
)
lpEngDsAgentQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpEngDsAgentQueueSize.setStatus("mandatory")
_LpProvTable_Object = MibTable
lpProvTable = _LpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 100)
)
if mibBuilder.loadTexts:
    lpProvTable.setStatus("mandatory")
_LpProvEntry_Object = MibTableRow
lpProvEntry = _LpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 100, 1)
)
lpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
)
if mibBuilder.loadTexts:
    lpProvEntry.setStatus("mandatory")
_LpMainCard_Type = Link
_LpMainCard_Object = MibTableColumn
lpMainCard = _LpMainCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 100, 1, 1),
    _LpMainCard_Type()
)
lpMainCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpMainCard.setStatus("mandatory")
_LpSpareCard_Type = Link
_LpSpareCard_Object = MibTableColumn
lpSpareCard = _LpSpareCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 100, 1, 2),
    _LpSpareCard_Type()
)
lpSpareCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpSpareCard.setStatus("mandatory")
_LpLogicalProcessorType_Type = Link
_LpLogicalProcessorType_Object = MibTableColumn
lpLogicalProcessorType = _LpLogicalProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 100, 1, 3),
    _LpLogicalProcessorType_Type()
)
lpLogicalProcessorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpLogicalProcessorType.setStatus("mandatory")
_LpCidDataTable_Object = MibTable
lpCidDataTable = _LpCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 101)
)
if mibBuilder.loadTexts:
    lpCidDataTable.setStatus("mandatory")
_LpCidDataEntry_Object = MibTableRow
lpCidDataEntry = _LpCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 101, 1)
)
lpCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
)
if mibBuilder.loadTexts:
    lpCidDataEntry.setStatus("mandatory")


class _LpCustomerIdentifier_Type(Unsigned32):
    """Custom type lpCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpCustomerIdentifier_Object = MibTableColumn
lpCustomerIdentifier = _LpCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 101, 1, 1),
    _LpCustomerIdentifier_Type()
)
lpCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpCustomerIdentifier.setStatus("mandatory")
_LpStateTable_Object = MibTable
lpStateTable = _LpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102)
)
if mibBuilder.loadTexts:
    lpStateTable.setStatus("mandatory")
_LpStateEntry_Object = MibTableRow
lpStateEntry = _LpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1)
)
lpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
)
if mibBuilder.loadTexts:
    lpStateEntry.setStatus("mandatory")


class _LpAdminState_Type(Integer32):
    """Custom type lpAdminState based on Integer32"""
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


_LpAdminState_Type.__name__ = "Integer32"
_LpAdminState_Object = MibTableColumn
lpAdminState = _LpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 1),
    _LpAdminState_Type()
)
lpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAdminState.setStatus("mandatory")


class _LpOperationalState_Type(Integer32):
    """Custom type lpOperationalState based on Integer32"""
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


_LpOperationalState_Type.__name__ = "Integer32"
_LpOperationalState_Object = MibTableColumn
lpOperationalState = _LpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 2),
    _LpOperationalState_Type()
)
lpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOperationalState.setStatus("mandatory")


class _LpUsageState_Type(Integer32):
    """Custom type lpUsageState based on Integer32"""
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


_LpUsageState_Type.__name__ = "Integer32"
_LpUsageState_Object = MibTableColumn
lpUsageState = _LpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 3),
    _LpUsageState_Type()
)
lpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpUsageState.setStatus("mandatory")


class _LpAvailabilityStatus_Type(OctetString):
    """Custom type lpAvailabilityStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LpAvailabilityStatus_Type.__name__ = "OctetString"
_LpAvailabilityStatus_Object = MibTableColumn
lpAvailabilityStatus = _LpAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 4),
    _LpAvailabilityStatus_Type()
)
lpAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAvailabilityStatus.setStatus("mandatory")


class _LpProceduralStatus_Type(OctetString):
    """Custom type lpProceduralStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpProceduralStatus_Type.__name__ = "OctetString"
_LpProceduralStatus_Object = MibTableColumn
lpProceduralStatus = _LpProceduralStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 5),
    _LpProceduralStatus_Type()
)
lpProceduralStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpProceduralStatus.setStatus("mandatory")


class _LpControlStatus_Type(OctetString):
    """Custom type lpControlStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpControlStatus_Type.__name__ = "OctetString"
_LpControlStatus_Object = MibTableColumn
lpControlStatus = _LpControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 6),
    _LpControlStatus_Type()
)
lpControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpControlStatus.setStatus("mandatory")


class _LpAlarmStatus_Type(OctetString):
    """Custom type lpAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_LpAlarmStatus_Type.__name__ = "OctetString"
_LpAlarmStatus_Object = MibTableColumn
lpAlarmStatus = _LpAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 7),
    _LpAlarmStatus_Type()
)
lpAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpAlarmStatus.setStatus("mandatory")


class _LpStandbyStatus_Type(Integer32):
    """Custom type lpStandbyStatus based on Integer32"""
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


_LpStandbyStatus_Type.__name__ = "Integer32"
_LpStandbyStatus_Object = MibTableColumn
lpStandbyStatus = _LpStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 8),
    _LpStandbyStatus_Type()
)
lpStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpStandbyStatus.setStatus("mandatory")


class _LpUnknownStatus_Type(Integer32):
    """Custom type lpUnknownStatus based on Integer32"""
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


_LpUnknownStatus_Type.__name__ = "Integer32"
_LpUnknownStatus_Object = MibTableColumn
lpUnknownStatus = _LpUnknownStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 102, 1, 9),
    _LpUnknownStatus_Type()
)
lpUnknownStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpUnknownStatus.setStatus("mandatory")
_LpOperTable_Object = MibTable
lpOperTable = _LpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 103)
)
if mibBuilder.loadTexts:
    lpOperTable.setStatus("mandatory")
_LpOperEntry_Object = MibTableRow
lpOperEntry = _LpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 103, 1)
)
lpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
)
if mibBuilder.loadTexts:
    lpOperEntry.setStatus("mandatory")
_LpActiveCard_Type = RowPointer
_LpActiveCard_Object = MibTableColumn
lpActiveCard = _LpActiveCard_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 103, 1, 1),
    _LpActiveCard_Type()
)
lpActiveCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpActiveCard.setStatus("mandatory")


class _LpMainCardStatus_Type(Integer32):
    """Custom type lpMainCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("available", 3),
          ("notAvailable", 1),
          ("notProvisioned", 0))
    )


_LpMainCardStatus_Type.__name__ = "Integer32"
_LpMainCardStatus_Object = MibTableColumn
lpMainCardStatus = _LpMainCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 103, 1, 2),
    _LpMainCardStatus_Type()
)
lpMainCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMainCardStatus.setStatus("mandatory")


class _LpSpareCardStatus_Type(Integer32):
    """Custom type lpSpareCardStatus based on Integer32"""
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
        *(("active", 4),
          ("alreadyInUse", 2),
          ("available", 3),
          ("notAvailable", 1),
          ("notProvisioned", 0))
    )


_LpSpareCardStatus_Type.__name__ = "Integer32"
_LpSpareCardStatus_Object = MibTableColumn
lpSpareCardStatus = _LpSpareCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 103, 1, 3),
    _LpSpareCardStatus_Type()
)
lpSpareCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpSpareCardStatus.setStatus("mandatory")


class _LpRestartOnCpSwitch_Type(Integer32):
    """Custom type lpRestartOnCpSwitch based on Integer32"""
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


_LpRestartOnCpSwitch_Type.__name__ = "Integer32"
_LpRestartOnCpSwitch_Object = MibTableColumn
lpRestartOnCpSwitch = _LpRestartOnCpSwitch_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 103, 1, 4),
    _LpRestartOnCpSwitch_Type()
)
lpRestartOnCpSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpRestartOnCpSwitch.setStatus("mandatory")


class _LpScheduledSwitchover_Type(EnterpriseDateAndTime):
    """Custom type lpScheduledSwitchover based on EnterpriseDateAndTime"""
    subtypeSpec = EnterpriseDateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
    )


_LpScheduledSwitchover_Type.__name__ = "EnterpriseDateAndTime"
_LpScheduledSwitchover_Object = MibTableColumn
lpScheduledSwitchover = _LpScheduledSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 103, 1, 5),
    _LpScheduledSwitchover_Type()
)
lpScheduledSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpScheduledSwitchover.setStatus("mandatory")
_LpUtilTable_Object = MibTable
lpUtilTable = _LpUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104)
)
if mibBuilder.loadTexts:
    lpUtilTable.setStatus("mandatory")
_LpUtilEntry_Object = MibTableRow
lpUtilEntry = _LpUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1)
)
lpUtilEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
)
if mibBuilder.loadTexts:
    lpUtilEntry.setStatus("mandatory")


class _LpTimeInterval_Type(Unsigned32):
    """Custom type lpTimeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LpTimeInterval_Type.__name__ = "Unsigned32"
_LpTimeInterval_Object = MibTableColumn
lpTimeInterval = _LpTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 1),
    _LpTimeInterval_Type()
)
lpTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpTimeInterval.setStatus("mandatory")


class _LpCpuUtil_Type(Gauge32):
    """Custom type lpCpuUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpCpuUtil_Type.__name__ = "Gauge32"
_LpCpuUtil_Object = MibTableColumn
lpCpuUtil = _LpCpuUtil_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 2),
    _LpCpuUtil_Type()
)
lpCpuUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpCpuUtil.setStatus("mandatory")


class _LpCpuUtilAvg_Type(Gauge32):
    """Custom type lpCpuUtilAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpCpuUtilAvg_Type.__name__ = "Gauge32"
_LpCpuUtilAvg_Object = MibTableColumn
lpCpuUtilAvg = _LpCpuUtilAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 3),
    _LpCpuUtilAvg_Type()
)
lpCpuUtilAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpCpuUtilAvg.setStatus("mandatory")


class _LpCpuUtilAvgMin_Type(Gauge32):
    """Custom type lpCpuUtilAvgMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpCpuUtilAvgMin_Type.__name__ = "Gauge32"
_LpCpuUtilAvgMin_Object = MibTableColumn
lpCpuUtilAvgMin = _LpCpuUtilAvgMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 4),
    _LpCpuUtilAvgMin_Type()
)
lpCpuUtilAvgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpCpuUtilAvgMin.setStatus("mandatory")


class _LpCpuUtilAvgMax_Type(Gauge32):
    """Custom type lpCpuUtilAvgMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LpCpuUtilAvgMax_Type.__name__ = "Gauge32"
_LpCpuUtilAvgMax_Object = MibTableColumn
lpCpuUtilAvgMax = _LpCpuUtilAvgMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 5),
    _LpCpuUtilAvgMax_Type()
)
lpCpuUtilAvgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpCpuUtilAvgMax.setStatus("mandatory")


class _LpMsgBlockUsage_Type(Gauge32):
    """Custom type lpMsgBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMsgBlockUsage_Type.__name__ = "Gauge32"
_LpMsgBlockUsage_Object = MibTableColumn
lpMsgBlockUsage = _LpMsgBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 6),
    _LpMsgBlockUsage_Type()
)
lpMsgBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMsgBlockUsage.setStatus("mandatory")


class _LpMsgBlockUsageAvg_Type(Gauge32):
    """Custom type lpMsgBlockUsageAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMsgBlockUsageAvg_Type.__name__ = "Gauge32"
_LpMsgBlockUsageAvg_Object = MibTableColumn
lpMsgBlockUsageAvg = _LpMsgBlockUsageAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 7),
    _LpMsgBlockUsageAvg_Type()
)
lpMsgBlockUsageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMsgBlockUsageAvg.setStatus("mandatory")


class _LpMsgBlockUsageAvgMin_Type(Gauge32):
    """Custom type lpMsgBlockUsageAvgMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMsgBlockUsageAvgMin_Type.__name__ = "Gauge32"
_LpMsgBlockUsageAvgMin_Object = MibTableColumn
lpMsgBlockUsageAvgMin = _LpMsgBlockUsageAvgMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 8),
    _LpMsgBlockUsageAvgMin_Type()
)
lpMsgBlockUsageAvgMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMsgBlockUsageAvgMin.setStatus("mandatory")


class _LpMsgBlockUsageAvgMax_Type(Gauge32):
    """Custom type lpMsgBlockUsageAvgMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMsgBlockUsageAvgMax_Type.__name__ = "Gauge32"
_LpMsgBlockUsageAvgMax_Object = MibTableColumn
lpMsgBlockUsageAvgMax = _LpMsgBlockUsageAvgMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 9),
    _LpMsgBlockUsageAvgMax_Type()
)
lpMsgBlockUsageAvgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMsgBlockUsageAvgMax.setStatus("mandatory")


class _LpLocalMsgBlockUsage_Type(Gauge32):
    """Custom type lpLocalMsgBlockUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpLocalMsgBlockUsage_Type.__name__ = "Gauge32"
_LpLocalMsgBlockUsage_Object = MibTableColumn
lpLocalMsgBlockUsage = _LpLocalMsgBlockUsage_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 10),
    _LpLocalMsgBlockUsage_Type()
)
lpLocalMsgBlockUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpLocalMsgBlockUsage.setStatus("mandatory")


class _LpLocalMsgBlockUsageAvg_Type(Gauge32):
    """Custom type lpLocalMsgBlockUsageAvg based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpLocalMsgBlockUsageAvg_Type.__name__ = "Gauge32"
_LpLocalMsgBlockUsageAvg_Object = MibTableColumn
lpLocalMsgBlockUsageAvg = _LpLocalMsgBlockUsageAvg_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 11),
    _LpLocalMsgBlockUsageAvg_Type()
)
lpLocalMsgBlockUsageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpLocalMsgBlockUsageAvg.setStatus("mandatory")


class _LpLocalMsgBlockUsageMin_Type(Gauge32):
    """Custom type lpLocalMsgBlockUsageMin based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpLocalMsgBlockUsageMin_Type.__name__ = "Gauge32"
_LpLocalMsgBlockUsageMin_Object = MibTableColumn
lpLocalMsgBlockUsageMin = _LpLocalMsgBlockUsageMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 12),
    _LpLocalMsgBlockUsageMin_Type()
)
lpLocalMsgBlockUsageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpLocalMsgBlockUsageMin.setStatus("mandatory")


class _LpLocalMsgBlockUsageMax_Type(Gauge32):
    """Custom type lpLocalMsgBlockUsageMax based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpLocalMsgBlockUsageMax_Type.__name__ = "Gauge32"
_LpLocalMsgBlockUsageMax_Object = MibTableColumn
lpLocalMsgBlockUsageMax = _LpLocalMsgBlockUsageMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 104, 1, 13),
    _LpLocalMsgBlockUsageMax_Type()
)
lpLocalMsgBlockUsageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpLocalMsgBlockUsageMax.setStatus("mandatory")
_LpCapTable_Object = MibTable
lpCapTable = _LpCapTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 105)
)
if mibBuilder.loadTexts:
    lpCapTable.setStatus("mandatory")
_LpCapEntry_Object = MibTableRow
lpCapEntry = _LpCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 105, 1)
)
lpCapEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
)
if mibBuilder.loadTexts:
    lpCapEntry.setStatus("mandatory")


class _LpMsgBlockCapacity_Type(Unsigned32):
    """Custom type lpMsgBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMsgBlockCapacity_Type.__name__ = "Unsigned32"
_LpMsgBlockCapacity_Object = MibTableColumn
lpMsgBlockCapacity = _LpMsgBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 105, 1, 1),
    _LpMsgBlockCapacity_Type()
)
lpMsgBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMsgBlockCapacity.setStatus("mandatory")


class _LpLocalMsgBlockCapacity_Type(Unsigned32):
    """Custom type lpLocalMsgBlockCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpLocalMsgBlockCapacity_Type.__name__ = "Unsigned32"
_LpLocalMsgBlockCapacity_Object = MibTableColumn
lpLocalMsgBlockCapacity = _LpLocalMsgBlockCapacity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 105, 1, 2),
    _LpLocalMsgBlockCapacity_Type()
)
lpLocalMsgBlockCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpLocalMsgBlockCapacity.setStatus("mandatory")
_LpLinkToApplicationsTable_Object = MibTable
lpLinkToApplicationsTable = _LpLinkToApplicationsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 242)
)
if mibBuilder.loadTexts:
    lpLinkToApplicationsTable.setStatus("mandatory")
_LpLinkToApplicationsEntry_Object = MibTableRow
lpLinkToApplicationsEntry = _LpLinkToApplicationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 242, 1)
)
lpLinkToApplicationsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpLinkToApplicationsValue"),
)
if mibBuilder.loadTexts:
    lpLinkToApplicationsEntry.setStatus("mandatory")
_LpLinkToApplicationsValue_Type = Link
_LpLinkToApplicationsValue_Object = MibTableColumn
lpLinkToApplicationsValue = _LpLinkToApplicationsValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 242, 1, 1),
    _LpLinkToApplicationsValue_Type()
)
lpLinkToApplicationsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpLinkToApplicationsValue.setStatus("mandatory")
_LpMemoryCapacityTable_Object = MibTable
lpMemoryCapacityTable = _LpMemoryCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 244)
)
if mibBuilder.loadTexts:
    lpMemoryCapacityTable.setStatus("mandatory")
_LpMemoryCapacityEntry_Object = MibTableRow
lpMemoryCapacityEntry = _LpMemoryCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 244, 1)
)
lpMemoryCapacityEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpMemoryCapacityIndex"),
)
if mibBuilder.loadTexts:
    lpMemoryCapacityEntry.setStatus("mandatory")


class _LpMemoryCapacityIndex_Type(Integer32):
    """Custom type lpMemoryCapacityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_LpMemoryCapacityIndex_Type.__name__ = "Integer32"
_LpMemoryCapacityIndex_Object = MibTableColumn
lpMemoryCapacityIndex = _LpMemoryCapacityIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 244, 1, 1),
    _LpMemoryCapacityIndex_Type()
)
lpMemoryCapacityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpMemoryCapacityIndex.setStatus("mandatory")


class _LpMemoryCapacityValue_Type(Unsigned32):
    """Custom type lpMemoryCapacityValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMemoryCapacityValue_Type.__name__ = "Unsigned32"
_LpMemoryCapacityValue_Object = MibTableColumn
lpMemoryCapacityValue = _LpMemoryCapacityValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 244, 1, 2),
    _LpMemoryCapacityValue_Type()
)
lpMemoryCapacityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMemoryCapacityValue.setStatus("mandatory")
_LpMemoryUsageTable_Object = MibTable
lpMemoryUsageTable = _LpMemoryUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 245)
)
if mibBuilder.loadTexts:
    lpMemoryUsageTable.setStatus("mandatory")
_LpMemoryUsageEntry_Object = MibTableRow
lpMemoryUsageEntry = _LpMemoryUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 245, 1)
)
lpMemoryUsageEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpMemoryUsageIndex"),
)
if mibBuilder.loadTexts:
    lpMemoryUsageEntry.setStatus("mandatory")


class _LpMemoryUsageIndex_Type(Integer32):
    """Custom type lpMemoryUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_LpMemoryUsageIndex_Type.__name__ = "Integer32"
_LpMemoryUsageIndex_Object = MibTableColumn
lpMemoryUsageIndex = _LpMemoryUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 245, 1, 1),
    _LpMemoryUsageIndex_Type()
)
lpMemoryUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpMemoryUsageIndex.setStatus("mandatory")


class _LpMemoryUsageValue_Type(Gauge32):
    """Custom type lpMemoryUsageValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMemoryUsageValue_Type.__name__ = "Gauge32"
_LpMemoryUsageValue_Object = MibTableColumn
lpMemoryUsageValue = _LpMemoryUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 245, 1, 2),
    _LpMemoryUsageValue_Type()
)
lpMemoryUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMemoryUsageValue.setStatus("mandatory")
_LpMemoryUsageAvgTable_Object = MibTable
lpMemoryUsageAvgTable = _LpMemoryUsageAvgTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 276)
)
if mibBuilder.loadTexts:
    lpMemoryUsageAvgTable.setStatus("mandatory")
_LpMemoryUsageAvgEntry_Object = MibTableRow
lpMemoryUsageAvgEntry = _LpMemoryUsageAvgEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 276, 1)
)
lpMemoryUsageAvgEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpMemoryUsageAvgIndex"),
)
if mibBuilder.loadTexts:
    lpMemoryUsageAvgEntry.setStatus("mandatory")


class _LpMemoryUsageAvgIndex_Type(Integer32):
    """Custom type lpMemoryUsageAvgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_LpMemoryUsageAvgIndex_Type.__name__ = "Integer32"
_LpMemoryUsageAvgIndex_Object = MibTableColumn
lpMemoryUsageAvgIndex = _LpMemoryUsageAvgIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 276, 1, 1),
    _LpMemoryUsageAvgIndex_Type()
)
lpMemoryUsageAvgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpMemoryUsageAvgIndex.setStatus("mandatory")


class _LpMemoryUsageAvgValue_Type(Gauge32):
    """Custom type lpMemoryUsageAvgValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMemoryUsageAvgValue_Type.__name__ = "Gauge32"
_LpMemoryUsageAvgValue_Object = MibTableColumn
lpMemoryUsageAvgValue = _LpMemoryUsageAvgValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 276, 1, 2),
    _LpMemoryUsageAvgValue_Type()
)
lpMemoryUsageAvgValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMemoryUsageAvgValue.setStatus("mandatory")
_LpMemoryUsageAvgMinTable_Object = MibTable
lpMemoryUsageAvgMinTable = _LpMemoryUsageAvgMinTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 277)
)
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMinTable.setStatus("mandatory")
_LpMemoryUsageAvgMinEntry_Object = MibTableRow
lpMemoryUsageAvgMinEntry = _LpMemoryUsageAvgMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 277, 1)
)
lpMemoryUsageAvgMinEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpMemoryUsageAvgMinIndex"),
)
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMinEntry.setStatus("mandatory")


class _LpMemoryUsageAvgMinIndex_Type(Integer32):
    """Custom type lpMemoryUsageAvgMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_LpMemoryUsageAvgMinIndex_Type.__name__ = "Integer32"
_LpMemoryUsageAvgMinIndex_Object = MibTableColumn
lpMemoryUsageAvgMinIndex = _LpMemoryUsageAvgMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 277, 1, 1),
    _LpMemoryUsageAvgMinIndex_Type()
)
lpMemoryUsageAvgMinIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMinIndex.setStatus("mandatory")


class _LpMemoryUsageAvgMinValue_Type(Gauge32):
    """Custom type lpMemoryUsageAvgMinValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMemoryUsageAvgMinValue_Type.__name__ = "Gauge32"
_LpMemoryUsageAvgMinValue_Object = MibTableColumn
lpMemoryUsageAvgMinValue = _LpMemoryUsageAvgMinValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 277, 1, 2),
    _LpMemoryUsageAvgMinValue_Type()
)
lpMemoryUsageAvgMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMinValue.setStatus("mandatory")
_LpMemoryUsageAvgMaxTable_Object = MibTable
lpMemoryUsageAvgMaxTable = _LpMemoryUsageAvgMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 278)
)
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMaxTable.setStatus("mandatory")
_LpMemoryUsageAvgMaxEntry_Object = MibTableRow
lpMemoryUsageAvgMaxEntry = _LpMemoryUsageAvgMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 278, 1)
)
lpMemoryUsageAvgMaxEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpMemoryUsageAvgMaxIndex"),
)
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMaxEntry.setStatus("mandatory")


class _LpMemoryUsageAvgMaxIndex_Type(Integer32):
    """Custom type lpMemoryUsageAvgMaxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fastRam", 0),
          ("normalRam", 1),
          ("sharedRam", 2))
    )


_LpMemoryUsageAvgMaxIndex_Type.__name__ = "Integer32"
_LpMemoryUsageAvgMaxIndex_Object = MibTableColumn
lpMemoryUsageAvgMaxIndex = _LpMemoryUsageAvgMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 278, 1, 1),
    _LpMemoryUsageAvgMaxIndex_Type()
)
lpMemoryUsageAvgMaxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMaxIndex.setStatus("mandatory")


class _LpMemoryUsageAvgMaxValue_Type(Gauge32):
    """Custom type lpMemoryUsageAvgMaxValue based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LpMemoryUsageAvgMaxValue_Type.__name__ = "Gauge32"
_LpMemoryUsageAvgMaxValue_Object = MibTableColumn
lpMemoryUsageAvgMaxValue = _LpMemoryUsageAvgMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 278, 1, 2),
    _LpMemoryUsageAvgMaxValue_Type()
)
lpMemoryUsageAvgMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpMemoryUsageAvgMaxValue.setStatus("mandatory")
_LogicalProcessorMIB_ObjectIdentity = ObjectIdentity
logicalProcessorMIB = _LogicalProcessorMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11)
)
_LogicalProcessorGroup_ObjectIdentity = ObjectIdentity
logicalProcessorGroup = _LogicalProcessorGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 1)
)
_LogicalProcessorGroupBE_ObjectIdentity = ObjectIdentity
logicalProcessorGroupBE = _LogicalProcessorGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 1, 5)
)
_LogicalProcessorGroupBE01_ObjectIdentity = ObjectIdentity
logicalProcessorGroupBE01 = _LogicalProcessorGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 1, 5, 2)
)
_LogicalProcessorGroupBE01A_ObjectIdentity = ObjectIdentity
logicalProcessorGroupBE01A = _LogicalProcessorGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 1, 5, 2, 2)
)
_LogicalProcessorCapabilities_ObjectIdentity = ObjectIdentity
logicalProcessorCapabilities = _LogicalProcessorCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 3)
)
_LogicalProcessorCapabilitiesBE_ObjectIdentity = ObjectIdentity
logicalProcessorCapabilitiesBE = _LogicalProcessorCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 3, 5)
)
_LogicalProcessorCapabilitiesBE01_ObjectIdentity = ObjectIdentity
logicalProcessorCapabilitiesBE01 = _LogicalProcessorCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 3, 5, 2)
)
_LogicalProcessorCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
logicalProcessorCapabilitiesBE01A = _LogicalProcessorCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 11, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-LogicalProcessorMIB",
    **{"lp": lp,
       "lpRowStatusTable": lpRowStatusTable,
       "lpRowStatusEntry": lpRowStatusEntry,
       "lpRowStatus": lpRowStatus,
       "lpComponentName": lpComponentName,
       "lpStorageType": lpStorageType,
       "lpIndex": lpIndex,
       "lpDS3": lpDS3,
       "lpDS3RowStatusTable": lpDS3RowStatusTable,
       "lpDS3RowStatusEntry": lpDS3RowStatusEntry,
       "lpDS3RowStatus": lpDS3RowStatus,
       "lpDS3ComponentName": lpDS3ComponentName,
       "lpDS3StorageType": lpDS3StorageType,
       "lpDS3Index": lpDS3Index,
       "lpDS3Test": lpDS3Test,
       "lpDS3TestRowStatusTable": lpDS3TestRowStatusTable,
       "lpDS3TestRowStatusEntry": lpDS3TestRowStatusEntry,
       "lpDS3TestRowStatus": lpDS3TestRowStatus,
       "lpDS3TestComponentName": lpDS3TestComponentName,
       "lpDS3TestStorageType": lpDS3TestStorageType,
       "lpDS3TestIndex": lpDS3TestIndex,
       "lpDS3TestStateTable": lpDS3TestStateTable,
       "lpDS3TestStateEntry": lpDS3TestStateEntry,
       "lpDS3TestAdminState": lpDS3TestAdminState,
       "lpDS3TestOperationalState": lpDS3TestOperationalState,
       "lpDS3TestUsageState": lpDS3TestUsageState,
       "lpDS3TestSetupTable": lpDS3TestSetupTable,
       "lpDS3TestSetupEntry": lpDS3TestSetupEntry,
       "lpDS3TestPurpose": lpDS3TestPurpose,
       "lpDS3TestType": lpDS3TestType,
       "lpDS3TestFrmSize": lpDS3TestFrmSize,
       "lpDS3TestFrmPatternType": lpDS3TestFrmPatternType,
       "lpDS3TestCustomizedPattern": lpDS3TestCustomizedPattern,
       "lpDS3TestDataStartDelay": lpDS3TestDataStartDelay,
       "lpDS3TestDisplayInterval": lpDS3TestDisplayInterval,
       "lpDS3TestDuration": lpDS3TestDuration,
       "lpDS3TestResultsTable": lpDS3TestResultsTable,
       "lpDS3TestResultsEntry": lpDS3TestResultsEntry,
       "lpDS3TestElapsedTime": lpDS3TestElapsedTime,
       "lpDS3TestTimeRemaining": lpDS3TestTimeRemaining,
       "lpDS3TestCauseOfTermination": lpDS3TestCauseOfTermination,
       "lpDS3TestBitsTx": lpDS3TestBitsTx,
       "lpDS3TestBytesTx": lpDS3TestBytesTx,
       "lpDS3TestFrmTx": lpDS3TestFrmTx,
       "lpDS3TestBitsRx": lpDS3TestBitsRx,
       "lpDS3TestBytesRx": lpDS3TestBytesRx,
       "lpDS3TestFrmRx": lpDS3TestFrmRx,
       "lpDS3TestErroredFrmRx": lpDS3TestErroredFrmRx,
       "lpDS3TestBitErrorRate": lpDS3TestBitErrorRate,
       "lpDS3CBit": lpDS3CBit,
       "lpDS3CBitRowStatusTable": lpDS3CBitRowStatusTable,
       "lpDS3CBitRowStatusEntry": lpDS3CBitRowStatusEntry,
       "lpDS3CBitRowStatus": lpDS3CBitRowStatus,
       "lpDS3CBitComponentName": lpDS3CBitComponentName,
       "lpDS3CBitStorageType": lpDS3CBitStorageType,
       "lpDS3CBitIndex": lpDS3CBitIndex,
       "lpDS3CBitOperationalTable": lpDS3CBitOperationalTable,
       "lpDS3CBitOperationalEntry": lpDS3CBitOperationalEntry,
       "lpDS3CBitFarEndAlarm": lpDS3CBitFarEndAlarm,
       "lpDS3CBitLoopedbackToFarEnd": lpDS3CBitLoopedbackToFarEnd,
       "lpDS3CBitLoopbackAtFarEndRequested": lpDS3CBitLoopbackAtFarEndRequested,
       "lpDS3CBitStatsTable": lpDS3CBitStatsTable,
       "lpDS3CBitStatsEntry": lpDS3CBitStatsEntry,
       "lpDS3CBitCbitErrorFreeSec": lpDS3CBitCbitErrorFreeSec,
       "lpDS3CBitCbitCodeViolations": lpDS3CBitCbitCodeViolations,
       "lpDS3CBitCbitErroredSec": lpDS3CBitCbitErroredSec,
       "lpDS3CBitCbitSevErroredSec": lpDS3CBitCbitSevErroredSec,
       "lpDS3CBitCbitUnavailSec": lpDS3CBitCbitUnavailSec,
       "lpDS3CBitFarEndErrorFreeSec": lpDS3CBitFarEndErrorFreeSec,
       "lpDS3CBitFarEndCodeViolations": lpDS3CBitFarEndCodeViolations,
       "lpDS3CBitFarEndErroredSec": lpDS3CBitFarEndErroredSec,
       "lpDS3CBitFarEndSevErroredSec": lpDS3CBitFarEndSevErroredSec,
       "lpDS3CBitFarEndSefAisSec": lpDS3CBitFarEndSefAisSec,
       "lpDS3CBitFarEndUnavailSec": lpDS3CBitFarEndUnavailSec,
       "lpDS3CBitFarEndFailures": lpDS3CBitFarEndFailures,
       "lpDS3Plcp": lpDS3Plcp,
       "lpDS3PlcpRowStatusTable": lpDS3PlcpRowStatusTable,
       "lpDS3PlcpRowStatusEntry": lpDS3PlcpRowStatusEntry,
       "lpDS3PlcpRowStatus": lpDS3PlcpRowStatus,
       "lpDS3PlcpComponentName": lpDS3PlcpComponentName,
       "lpDS3PlcpStorageType": lpDS3PlcpStorageType,
       "lpDS3PlcpIndex": lpDS3PlcpIndex,
       "lpDS3PlcpOperationalTable": lpDS3PlcpOperationalTable,
       "lpDS3PlcpOperationalEntry": lpDS3PlcpOperationalEntry,
       "lpDS3PlcpLofAlarm": lpDS3PlcpLofAlarm,
       "lpDS3PlcpRxRaiAlarm": lpDS3PlcpRxRaiAlarm,
       "lpDS3PlcpStatsTable": lpDS3PlcpStatsTable,
       "lpDS3PlcpStatsEntry": lpDS3PlcpStatsEntry,
       "lpDS3PlcpErrorFreeSec": lpDS3PlcpErrorFreeSec,
       "lpDS3PlcpCodingViolations": lpDS3PlcpCodingViolations,
       "lpDS3PlcpErroredSec": lpDS3PlcpErroredSec,
       "lpDS3PlcpSevErroredSec": lpDS3PlcpSevErroredSec,
       "lpDS3PlcpSevErroredFramingSec": lpDS3PlcpSevErroredFramingSec,
       "lpDS3PlcpUnavailSec": lpDS3PlcpUnavailSec,
       "lpDS3PlcpFarEndErrorFreeSec": lpDS3PlcpFarEndErrorFreeSec,
       "lpDS3PlcpFarEndCodingViolations": lpDS3PlcpFarEndCodingViolations,
       "lpDS3PlcpFarEndErroredSec": lpDS3PlcpFarEndErroredSec,
       "lpDS3PlcpFarEndSevErroredSec": lpDS3PlcpFarEndSevErroredSec,
       "lpDS3PlcpFarEndUnavailableSec": lpDS3PlcpFarEndUnavailableSec,
       "lpDS3Cell": lpDS3Cell,
       "lpDS3CellRowStatusTable": lpDS3CellRowStatusTable,
       "lpDS3CellRowStatusEntry": lpDS3CellRowStatusEntry,
       "lpDS3CellRowStatus": lpDS3CellRowStatus,
       "lpDS3CellComponentName": lpDS3CellComponentName,
       "lpDS3CellStorageType": lpDS3CellStorageType,
       "lpDS3CellIndex": lpDS3CellIndex,
       "lpDS3CellProvTable": lpDS3CellProvTable,
       "lpDS3CellProvEntry": lpDS3CellProvEntry,
       "lpDS3CellAlarmActDelay": lpDS3CellAlarmActDelay,
       "lpDS3CellScrambleCellPayload": lpDS3CellScrambleCellPayload,
       "lpDS3CellCorrectSingleBitHeaderErrors": lpDS3CellCorrectSingleBitHeaderErrors,
       "lpDS3CellOperTable": lpDS3CellOperTable,
       "lpDS3CellOperEntry": lpDS3CellOperEntry,
       "lpDS3CellLcdAlarm": lpDS3CellLcdAlarm,
       "lpDS3CellStatsTable": lpDS3CellStatsTable,
       "lpDS3CellStatsEntry": lpDS3CellStatsEntry,
       "lpDS3CellUncorrectableHecErrors": lpDS3CellUncorrectableHecErrors,
       "lpDS3CellSevErroredSec": lpDS3CellSevErroredSec,
       "lpDS3CellReceiveCellUtilization": lpDS3CellReceiveCellUtilization,
       "lpDS3CellTransmitCellUtilization": lpDS3CellTransmitCellUtilization,
       "lpDS3CellCorrectableHeaderErrors": lpDS3CellCorrectableHeaderErrors,
       "lpDS3DS1": lpDS3DS1,
       "lpDS3DS1RowStatusTable": lpDS3DS1RowStatusTable,
       "lpDS3DS1RowStatusEntry": lpDS3DS1RowStatusEntry,
       "lpDS3DS1RowStatus": lpDS3DS1RowStatus,
       "lpDS3DS1ComponentName": lpDS3DS1ComponentName,
       "lpDS3DS1StorageType": lpDS3DS1StorageType,
       "lpDS3DS1Index": lpDS3DS1Index,
       "lpDS3DS1Chan": lpDS3DS1Chan,
       "lpDS3DS1ChanRowStatusTable": lpDS3DS1ChanRowStatusTable,
       "lpDS3DS1ChanRowStatusEntry": lpDS3DS1ChanRowStatusEntry,
       "lpDS3DS1ChanRowStatus": lpDS3DS1ChanRowStatus,
       "lpDS3DS1ChanComponentName": lpDS3DS1ChanComponentName,
       "lpDS3DS1ChanStorageType": lpDS3DS1ChanStorageType,
       "lpDS3DS1ChanIndex": lpDS3DS1ChanIndex,
       "lpDS3DS1ChanTest": lpDS3DS1ChanTest,
       "lpDS3DS1ChanTestRowStatusTable": lpDS3DS1ChanTestRowStatusTable,
       "lpDS3DS1ChanTestRowStatusEntry": lpDS3DS1ChanTestRowStatusEntry,
       "lpDS3DS1ChanTestRowStatus": lpDS3DS1ChanTestRowStatus,
       "lpDS3DS1ChanTestComponentName": lpDS3DS1ChanTestComponentName,
       "lpDS3DS1ChanTestStorageType": lpDS3DS1ChanTestStorageType,
       "lpDS3DS1ChanTestIndex": lpDS3DS1ChanTestIndex,
       "lpDS3DS1ChanTestStateTable": lpDS3DS1ChanTestStateTable,
       "lpDS3DS1ChanTestStateEntry": lpDS3DS1ChanTestStateEntry,
       "lpDS3DS1ChanTestAdminState": lpDS3DS1ChanTestAdminState,
       "lpDS3DS1ChanTestOperationalState": lpDS3DS1ChanTestOperationalState,
       "lpDS3DS1ChanTestUsageState": lpDS3DS1ChanTestUsageState,
       "lpDS3DS1ChanTestSetupTable": lpDS3DS1ChanTestSetupTable,
       "lpDS3DS1ChanTestSetupEntry": lpDS3DS1ChanTestSetupEntry,
       "lpDS3DS1ChanTestPurpose": lpDS3DS1ChanTestPurpose,
       "lpDS3DS1ChanTestType": lpDS3DS1ChanTestType,
       "lpDS3DS1ChanTestFrmSize": lpDS3DS1ChanTestFrmSize,
       "lpDS3DS1ChanTestFrmPatternType": lpDS3DS1ChanTestFrmPatternType,
       "lpDS3DS1ChanTestCustomizedPattern": lpDS3DS1ChanTestCustomizedPattern,
       "lpDS3DS1ChanTestDataStartDelay": lpDS3DS1ChanTestDataStartDelay,
       "lpDS3DS1ChanTestDisplayInterval": lpDS3DS1ChanTestDisplayInterval,
       "lpDS3DS1ChanTestDuration": lpDS3DS1ChanTestDuration,
       "lpDS3DS1ChanTestResultsTable": lpDS3DS1ChanTestResultsTable,
       "lpDS3DS1ChanTestResultsEntry": lpDS3DS1ChanTestResultsEntry,
       "lpDS3DS1ChanTestElapsedTime": lpDS3DS1ChanTestElapsedTime,
       "lpDS3DS1ChanTestTimeRemaining": lpDS3DS1ChanTestTimeRemaining,
       "lpDS3DS1ChanTestCauseOfTermination": lpDS3DS1ChanTestCauseOfTermination,
       "lpDS3DS1ChanTestBitsTx": lpDS3DS1ChanTestBitsTx,
       "lpDS3DS1ChanTestBytesTx": lpDS3DS1ChanTestBytesTx,
       "lpDS3DS1ChanTestFrmTx": lpDS3DS1ChanTestFrmTx,
       "lpDS3DS1ChanTestBitsRx": lpDS3DS1ChanTestBitsRx,
       "lpDS3DS1ChanTestBytesRx": lpDS3DS1ChanTestBytesRx,
       "lpDS3DS1ChanTestFrmRx": lpDS3DS1ChanTestFrmRx,
       "lpDS3DS1ChanTestErroredFrmRx": lpDS3DS1ChanTestErroredFrmRx,
       "lpDS3DS1ChanTestBitErrorRate": lpDS3DS1ChanTestBitErrorRate,
       "lpDS3DS1ChanCell": lpDS3DS1ChanCell,
       "lpDS3DS1ChanCellRowStatusTable": lpDS3DS1ChanCellRowStatusTable,
       "lpDS3DS1ChanCellRowStatusEntry": lpDS3DS1ChanCellRowStatusEntry,
       "lpDS3DS1ChanCellRowStatus": lpDS3DS1ChanCellRowStatus,
       "lpDS3DS1ChanCellComponentName": lpDS3DS1ChanCellComponentName,
       "lpDS3DS1ChanCellStorageType": lpDS3DS1ChanCellStorageType,
       "lpDS3DS1ChanCellIndex": lpDS3DS1ChanCellIndex,
       "lpDS3DS1ChanCellProvTable": lpDS3DS1ChanCellProvTable,
       "lpDS3DS1ChanCellProvEntry": lpDS3DS1ChanCellProvEntry,
       "lpDS3DS1ChanCellAlarmActDelay": lpDS3DS1ChanCellAlarmActDelay,
       "lpDS3DS1ChanCellScrambleCellPayload": lpDS3DS1ChanCellScrambleCellPayload,
       "lpDS3DS1ChanCellCorrectSingleBitHeaderErrors": lpDS3DS1ChanCellCorrectSingleBitHeaderErrors,
       "lpDS3DS1ChanCellOperTable": lpDS3DS1ChanCellOperTable,
       "lpDS3DS1ChanCellOperEntry": lpDS3DS1ChanCellOperEntry,
       "lpDS3DS1ChanCellLcdAlarm": lpDS3DS1ChanCellLcdAlarm,
       "lpDS3DS1ChanCellStatsTable": lpDS3DS1ChanCellStatsTable,
       "lpDS3DS1ChanCellStatsEntry": lpDS3DS1ChanCellStatsEntry,
       "lpDS3DS1ChanCellUncorrectableHecErrors": lpDS3DS1ChanCellUncorrectableHecErrors,
       "lpDS3DS1ChanCellSevErroredSec": lpDS3DS1ChanCellSevErroredSec,
       "lpDS3DS1ChanCellReceiveCellUtilization": lpDS3DS1ChanCellReceiveCellUtilization,
       "lpDS3DS1ChanCellTransmitCellUtilization": lpDS3DS1ChanCellTransmitCellUtilization,
       "lpDS3DS1ChanCellCorrectableHeaderErrors": lpDS3DS1ChanCellCorrectableHeaderErrors,
       "lpDS3DS1ChanTc": lpDS3DS1ChanTc,
       "lpDS3DS1ChanTcRowStatusTable": lpDS3DS1ChanTcRowStatusTable,
       "lpDS3DS1ChanTcRowStatusEntry": lpDS3DS1ChanTcRowStatusEntry,
       "lpDS3DS1ChanTcRowStatus": lpDS3DS1ChanTcRowStatus,
       "lpDS3DS1ChanTcComponentName": lpDS3DS1ChanTcComponentName,
       "lpDS3DS1ChanTcStorageType": lpDS3DS1ChanTcStorageType,
       "lpDS3DS1ChanTcIndex": lpDS3DS1ChanTcIndex,
       "lpDS3DS1ChanTcProvTable": lpDS3DS1ChanTcProvTable,
       "lpDS3DS1ChanTcProvEntry": lpDS3DS1ChanTcProvEntry,
       "lpDS3DS1ChanTcReplacementData": lpDS3DS1ChanTcReplacementData,
       "lpDS3DS1ChanTcSignalOneDuration": lpDS3DS1ChanTcSignalOneDuration,
       "lpDS3DS1ChanTcOpTable": lpDS3DS1ChanTcOpTable,
       "lpDS3DS1ChanTcOpEntry": lpDS3DS1ChanTcOpEntry,
       "lpDS3DS1ChanTcIngressConditioning": lpDS3DS1ChanTcIngressConditioning,
       "lpDS3DS1ChanTcEgressConditioning": lpDS3DS1ChanTcEgressConditioning,
       "lpDS3DS1ChanTcSigOneTable": lpDS3DS1ChanTcSigOneTable,
       "lpDS3DS1ChanTcSigOneEntry": lpDS3DS1ChanTcSigOneEntry,
       "lpDS3DS1ChanTcSigOneIndex": lpDS3DS1ChanTcSigOneIndex,
       "lpDS3DS1ChanTcSigOneValue": lpDS3DS1ChanTcSigOneValue,
       "lpDS3DS1ChanTcSigTwoTable": lpDS3DS1ChanTcSigTwoTable,
       "lpDS3DS1ChanTcSigTwoEntry": lpDS3DS1ChanTcSigTwoEntry,
       "lpDS3DS1ChanTcSigTwoIndex": lpDS3DS1ChanTcSigTwoIndex,
       "lpDS3DS1ChanTcSigTwoValue": lpDS3DS1ChanTcSigTwoValue,
       "lpDS3DS1ChanProvTable": lpDS3DS1ChanProvTable,
       "lpDS3DS1ChanProvEntry": lpDS3DS1ChanProvEntry,
       "lpDS3DS1ChanTimeslots": lpDS3DS1ChanTimeslots,
       "lpDS3DS1ChanTimeslotDataRate": lpDS3DS1ChanTimeslotDataRate,
       "lpDS3DS1ChanApplicationFramerName": lpDS3DS1ChanApplicationFramerName,
       "lpDS3DS1ChanCidDataTable": lpDS3DS1ChanCidDataTable,
       "lpDS3DS1ChanCidDataEntry": lpDS3DS1ChanCidDataEntry,
       "lpDS3DS1ChanCustomerIdentifier": lpDS3DS1ChanCustomerIdentifier,
       "lpDS3DS1ChanIfEntryTable": lpDS3DS1ChanIfEntryTable,
       "lpDS3DS1ChanIfEntryEntry": lpDS3DS1ChanIfEntryEntry,
       "lpDS3DS1ChanIfAdminStatus": lpDS3DS1ChanIfAdminStatus,
       "lpDS3DS1ChanIfIndex": lpDS3DS1ChanIfIndex,
       "lpDS3DS1ChanOperStatusTable": lpDS3DS1ChanOperStatusTable,
       "lpDS3DS1ChanOperStatusEntry": lpDS3DS1ChanOperStatusEntry,
       "lpDS3DS1ChanSnmpOperStatus": lpDS3DS1ChanSnmpOperStatus,
       "lpDS3DS1ChanStateTable": lpDS3DS1ChanStateTable,
       "lpDS3DS1ChanStateEntry": lpDS3DS1ChanStateEntry,
       "lpDS3DS1ChanAdminState": lpDS3DS1ChanAdminState,
       "lpDS3DS1ChanOperationalState": lpDS3DS1ChanOperationalState,
       "lpDS3DS1ChanUsageState": lpDS3DS1ChanUsageState,
       "lpDS3DS1ChanAvailabilityStatus": lpDS3DS1ChanAvailabilityStatus,
       "lpDS3DS1ChanProceduralStatus": lpDS3DS1ChanProceduralStatus,
       "lpDS3DS1ChanControlStatus": lpDS3DS1ChanControlStatus,
       "lpDS3DS1ChanAlarmStatus": lpDS3DS1ChanAlarmStatus,
       "lpDS3DS1ChanStandbyStatus": lpDS3DS1ChanStandbyStatus,
       "lpDS3DS1ChanUnknownStatus": lpDS3DS1ChanUnknownStatus,
       "lpDS3DS1ChanOperTable": lpDS3DS1ChanOperTable,
       "lpDS3DS1ChanOperEntry": lpDS3DS1ChanOperEntry,
       "lpDS3DS1ChanActualChannelSpeed": lpDS3DS1ChanActualChannelSpeed,
       "lpDS3DS1ChanAdminInfoTable": lpDS3DS1ChanAdminInfoTable,
       "lpDS3DS1ChanAdminInfoEntry": lpDS3DS1ChanAdminInfoEntry,
       "lpDS3DS1ChanVendor": lpDS3DS1ChanVendor,
       "lpDS3DS1ChanCommentText": lpDS3DS1ChanCommentText,
       "lpDS3DS1Test": lpDS3DS1Test,
       "lpDS3DS1TestRowStatusTable": lpDS3DS1TestRowStatusTable,
       "lpDS3DS1TestRowStatusEntry": lpDS3DS1TestRowStatusEntry,
       "lpDS3DS1TestRowStatus": lpDS3DS1TestRowStatus,
       "lpDS3DS1TestComponentName": lpDS3DS1TestComponentName,
       "lpDS3DS1TestStorageType": lpDS3DS1TestStorageType,
       "lpDS3DS1TestIndex": lpDS3DS1TestIndex,
       "lpDS3DS1TestStateTable": lpDS3DS1TestStateTable,
       "lpDS3DS1TestStateEntry": lpDS3DS1TestStateEntry,
       "lpDS3DS1TestAdminState": lpDS3DS1TestAdminState,
       "lpDS3DS1TestOperationalState": lpDS3DS1TestOperationalState,
       "lpDS3DS1TestUsageState": lpDS3DS1TestUsageState,
       "lpDS3DS1TestSetupTable": lpDS3DS1TestSetupTable,
       "lpDS3DS1TestSetupEntry": lpDS3DS1TestSetupEntry,
       "lpDS3DS1TestPurpose": lpDS3DS1TestPurpose,
       "lpDS3DS1TestType": lpDS3DS1TestType,
       "lpDS3DS1TestFrmSize": lpDS3DS1TestFrmSize,
       "lpDS3DS1TestFrmPatternType": lpDS3DS1TestFrmPatternType,
       "lpDS3DS1TestCustomizedPattern": lpDS3DS1TestCustomizedPattern,
       "lpDS3DS1TestDataStartDelay": lpDS3DS1TestDataStartDelay,
       "lpDS3DS1TestDisplayInterval": lpDS3DS1TestDisplayInterval,
       "lpDS3DS1TestDuration": lpDS3DS1TestDuration,
       "lpDS3DS1TestResultsTable": lpDS3DS1TestResultsTable,
       "lpDS3DS1TestResultsEntry": lpDS3DS1TestResultsEntry,
       "lpDS3DS1TestElapsedTime": lpDS3DS1TestElapsedTime,
       "lpDS3DS1TestTimeRemaining": lpDS3DS1TestTimeRemaining,
       "lpDS3DS1TestCauseOfTermination": lpDS3DS1TestCauseOfTermination,
       "lpDS3DS1TestBitsTx": lpDS3DS1TestBitsTx,
       "lpDS3DS1TestBytesTx": lpDS3DS1TestBytesTx,
       "lpDS3DS1TestFrmTx": lpDS3DS1TestFrmTx,
       "lpDS3DS1TestBitsRx": lpDS3DS1TestBitsRx,
       "lpDS3DS1TestBytesRx": lpDS3DS1TestBytesRx,
       "lpDS3DS1TestFrmRx": lpDS3DS1TestFrmRx,
       "lpDS3DS1TestErroredFrmRx": lpDS3DS1TestErroredFrmRx,
       "lpDS3DS1TestBitErrorRate": lpDS3DS1TestBitErrorRate,
       "lpDS3DS1ProvTable": lpDS3DS1ProvTable,
       "lpDS3DS1ProvEntry": lpDS3DS1ProvEntry,
       "lpDS3DS1LineType": lpDS3DS1LineType,
       "lpDS3DS1ZeroCoding": lpDS3DS1ZeroCoding,
       "lpDS3DS1ClockingSource": lpDS3DS1ClockingSource,
       "lpDS3DS1CidDataTable": lpDS3DS1CidDataTable,
       "lpDS3DS1CidDataEntry": lpDS3DS1CidDataEntry,
       "lpDS3DS1CustomerIdentifier": lpDS3DS1CustomerIdentifier,
       "lpDS3DS1AdminInfoTable": lpDS3DS1AdminInfoTable,
       "lpDS3DS1AdminInfoEntry": lpDS3DS1AdminInfoEntry,
       "lpDS3DS1Vendor": lpDS3DS1Vendor,
       "lpDS3DS1CommentText": lpDS3DS1CommentText,
       "lpDS3DS1IfEntryTable": lpDS3DS1IfEntryTable,
       "lpDS3DS1IfEntryEntry": lpDS3DS1IfEntryEntry,
       "lpDS3DS1IfAdminStatus": lpDS3DS1IfAdminStatus,
       "lpDS3DS1IfIndex": lpDS3DS1IfIndex,
       "lpDS3DS1OperStatusTable": lpDS3DS1OperStatusTable,
       "lpDS3DS1OperStatusEntry": lpDS3DS1OperStatusEntry,
       "lpDS3DS1SnmpOperStatus": lpDS3DS1SnmpOperStatus,
       "lpDS3DS1StateTable": lpDS3DS1StateTable,
       "lpDS3DS1StateEntry": lpDS3DS1StateEntry,
       "lpDS3DS1AdminState": lpDS3DS1AdminState,
       "lpDS3DS1OperationalState": lpDS3DS1OperationalState,
       "lpDS3DS1UsageState": lpDS3DS1UsageState,
       "lpDS3DS1AvailabilityStatus": lpDS3DS1AvailabilityStatus,
       "lpDS3DS1ProceduralStatus": lpDS3DS1ProceduralStatus,
       "lpDS3DS1ControlStatus": lpDS3DS1ControlStatus,
       "lpDS3DS1AlarmStatus": lpDS3DS1AlarmStatus,
       "lpDS3DS1StandbyStatus": lpDS3DS1StandbyStatus,
       "lpDS3DS1UnknownStatus": lpDS3DS1UnknownStatus,
       "lpDS3DS1OperTable": lpDS3DS1OperTable,
       "lpDS3DS1OperEntry": lpDS3DS1OperEntry,
       "lpDS3DS1RxAisAlarm": lpDS3DS1RxAisAlarm,
       "lpDS3DS1LofAlarm": lpDS3DS1LofAlarm,
       "lpDS3DS1RxRaiAlarm": lpDS3DS1RxRaiAlarm,
       "lpDS3DS1TxAisAlarm": lpDS3DS1TxAisAlarm,
       "lpDS3DS1TxRaiAlarm": lpDS3DS1TxRaiAlarm,
       "lpDS3DS1StatsTable": lpDS3DS1StatsTable,
       "lpDS3DS1StatsEntry": lpDS3DS1StatsEntry,
       "lpDS3DS1RunningTime": lpDS3DS1RunningTime,
       "lpDS3DS1ErrorFreeSec": lpDS3DS1ErrorFreeSec,
       "lpDS3DS1ErroredSec": lpDS3DS1ErroredSec,
       "lpDS3DS1SevErroredSec": lpDS3DS1SevErroredSec,
       "lpDS3DS1SevErroredFrmSec": lpDS3DS1SevErroredFrmSec,
       "lpDS3DS1UnavailSec": lpDS3DS1UnavailSec,
       "lpDS3DS1CrcErrors": lpDS3DS1CrcErrors,
       "lpDS3DS1FrmErrors": lpDS3DS1FrmErrors,
       "lpDS3DS1SlipErrors": lpDS3DS1SlipErrors,
       "lpDS3ProvTable": lpDS3ProvTable,
       "lpDS3ProvEntry": lpDS3ProvEntry,
       "lpDS3CbitParity": lpDS3CbitParity,
       "lpDS3LineLength": lpDS3LineLength,
       "lpDS3ClockingSource": lpDS3ClockingSource,
       "lpDS3ApplicationFramerName": lpDS3ApplicationFramerName,
       "lpDS3Mapping": lpDS3Mapping,
       "lpDS3CidDataTable": lpDS3CidDataTable,
       "lpDS3CidDataEntry": lpDS3CidDataEntry,
       "lpDS3CustomerIdentifier": lpDS3CustomerIdentifier,
       "lpDS3AdminInfoTable": lpDS3AdminInfoTable,
       "lpDS3AdminInfoEntry": lpDS3AdminInfoEntry,
       "lpDS3Vendor": lpDS3Vendor,
       "lpDS3CommentText": lpDS3CommentText,
       "lpDS3IfEntryTable": lpDS3IfEntryTable,
       "lpDS3IfEntryEntry": lpDS3IfEntryEntry,
       "lpDS3IfAdminStatus": lpDS3IfAdminStatus,
       "lpDS3IfIndex": lpDS3IfIndex,
       "lpDS3OperStatusTable": lpDS3OperStatusTable,
       "lpDS3OperStatusEntry": lpDS3OperStatusEntry,
       "lpDS3SnmpOperStatus": lpDS3SnmpOperStatus,
       "lpDS3StateTable": lpDS3StateTable,
       "lpDS3StateEntry": lpDS3StateEntry,
       "lpDS3AdminState": lpDS3AdminState,
       "lpDS3OperationalState": lpDS3OperationalState,
       "lpDS3UsageState": lpDS3UsageState,
       "lpDS3AvailabilityStatus": lpDS3AvailabilityStatus,
       "lpDS3ProceduralStatus": lpDS3ProceduralStatus,
       "lpDS3ControlStatus": lpDS3ControlStatus,
       "lpDS3AlarmStatus": lpDS3AlarmStatus,
       "lpDS3StandbyStatus": lpDS3StandbyStatus,
       "lpDS3UnknownStatus": lpDS3UnknownStatus,
       "lpDS3OperTable": lpDS3OperTable,
       "lpDS3OperEntry": lpDS3OperEntry,
       "lpDS3LosAlarm": lpDS3LosAlarm,
       "lpDS3LofAlarm": lpDS3LofAlarm,
       "lpDS3RxAisAlarm": lpDS3RxAisAlarm,
       "lpDS3RxRaiAlarm": lpDS3RxRaiAlarm,
       "lpDS3RxIdle": lpDS3RxIdle,
       "lpDS3TxAis": lpDS3TxAis,
       "lpDS3TxRai": lpDS3TxRai,
       "lpDS3TxIdle": lpDS3TxIdle,
       "lpDS3StatsTable": lpDS3StatsTable,
       "lpDS3StatsEntry": lpDS3StatsEntry,
       "lpDS3RunningTime": lpDS3RunningTime,
       "lpDS3ErrorFreeSec": lpDS3ErrorFreeSec,
       "lpDS3LineCodeViolations": lpDS3LineCodeViolations,
       "lpDS3LineErroredSec": lpDS3LineErroredSec,
       "lpDS3LineSevErroredSec": lpDS3LineSevErroredSec,
       "lpDS3LineLosSec": lpDS3LineLosSec,
       "lpDS3LineFailures": lpDS3LineFailures,
       "lpDS3PathCodeViolations": lpDS3PathCodeViolations,
       "lpDS3PathErroredSec": lpDS3PathErroredSec,
       "lpDS3PathSevErroredSec": lpDS3PathSevErroredSec,
       "lpDS3PathSefAisSec": lpDS3PathSefAisSec,
       "lpDS3PathUnavailSec": lpDS3PathUnavailSec,
       "lpDS3PathFailures": lpDS3PathFailures,
       "lpE3": lpE3,
       "lpE3RowStatusTable": lpE3RowStatusTable,
       "lpE3RowStatusEntry": lpE3RowStatusEntry,
       "lpE3RowStatus": lpE3RowStatus,
       "lpE3ComponentName": lpE3ComponentName,
       "lpE3StorageType": lpE3StorageType,
       "lpE3Index": lpE3Index,
       "lpE3Test": lpE3Test,
       "lpE3TestRowStatusTable": lpE3TestRowStatusTable,
       "lpE3TestRowStatusEntry": lpE3TestRowStatusEntry,
       "lpE3TestRowStatus": lpE3TestRowStatus,
       "lpE3TestComponentName": lpE3TestComponentName,
       "lpE3TestStorageType": lpE3TestStorageType,
       "lpE3TestIndex": lpE3TestIndex,
       "lpE3TestStateTable": lpE3TestStateTable,
       "lpE3TestStateEntry": lpE3TestStateEntry,
       "lpE3TestAdminState": lpE3TestAdminState,
       "lpE3TestOperationalState": lpE3TestOperationalState,
       "lpE3TestUsageState": lpE3TestUsageState,
       "lpE3TestSetupTable": lpE3TestSetupTable,
       "lpE3TestSetupEntry": lpE3TestSetupEntry,
       "lpE3TestPurpose": lpE3TestPurpose,
       "lpE3TestType": lpE3TestType,
       "lpE3TestFrmSize": lpE3TestFrmSize,
       "lpE3TestFrmPatternType": lpE3TestFrmPatternType,
       "lpE3TestCustomizedPattern": lpE3TestCustomizedPattern,
       "lpE3TestDataStartDelay": lpE3TestDataStartDelay,
       "lpE3TestDisplayInterval": lpE3TestDisplayInterval,
       "lpE3TestDuration": lpE3TestDuration,
       "lpE3TestResultsTable": lpE3TestResultsTable,
       "lpE3TestResultsEntry": lpE3TestResultsEntry,
       "lpE3TestElapsedTime": lpE3TestElapsedTime,
       "lpE3TestTimeRemaining": lpE3TestTimeRemaining,
       "lpE3TestCauseOfTermination": lpE3TestCauseOfTermination,
       "lpE3TestBitsTx": lpE3TestBitsTx,
       "lpE3TestBytesTx": lpE3TestBytesTx,
       "lpE3TestFrmTx": lpE3TestFrmTx,
       "lpE3TestBitsRx": lpE3TestBitsRx,
       "lpE3TestBytesRx": lpE3TestBytesRx,
       "lpE3TestFrmRx": lpE3TestFrmRx,
       "lpE3TestErroredFrmRx": lpE3TestErroredFrmRx,
       "lpE3TestBitErrorRate": lpE3TestBitErrorRate,
       "lpE3G832": lpE3G832,
       "lpE3G832RowStatusTable": lpE3G832RowStatusTable,
       "lpE3G832RowStatusEntry": lpE3G832RowStatusEntry,
       "lpE3G832RowStatus": lpE3G832RowStatus,
       "lpE3G832ComponentName": lpE3G832ComponentName,
       "lpE3G832StorageType": lpE3G832StorageType,
       "lpE3G832Index": lpE3G832Index,
       "lpE3G832ProvisionedTable": lpE3G832ProvisionedTable,
       "lpE3G832ProvisionedEntry": lpE3G832ProvisionedEntry,
       "lpE3G832TrailTraceTransmitted": lpE3G832TrailTraceTransmitted,
       "lpE3G832TrailTraceExpected": lpE3G832TrailTraceExpected,
       "lpE3G832OperationalTable": lpE3G832OperationalTable,
       "lpE3G832OperationalEntry": lpE3G832OperationalEntry,
       "lpE3G832UnexpectedPayloadType": lpE3G832UnexpectedPayloadType,
       "lpE3G832TrailTraceMismatch": lpE3G832TrailTraceMismatch,
       "lpE3G832TimingMarker": lpE3G832TimingMarker,
       "lpE3G832TrailTraceReceived": lpE3G832TrailTraceReceived,
       "lpE3G832StatsTable": lpE3G832StatsTable,
       "lpE3G832StatsEntry": lpE3G832StatsEntry,
       "lpE3G832FarEndErrorFreeSec": lpE3G832FarEndErrorFreeSec,
       "lpE3G832FarEndCodeViolations": lpE3G832FarEndCodeViolations,
       "lpE3G832FarEndErroredSec": lpE3G832FarEndErroredSec,
       "lpE3G832FarEndSevErroredSec": lpE3G832FarEndSevErroredSec,
       "lpE3G832FarEndSefAisSec": lpE3G832FarEndSefAisSec,
       "lpE3G832FarEndUnavailSec": lpE3G832FarEndUnavailSec,
       "lpE3Plcp": lpE3Plcp,
       "lpE3PlcpRowStatusTable": lpE3PlcpRowStatusTable,
       "lpE3PlcpRowStatusEntry": lpE3PlcpRowStatusEntry,
       "lpE3PlcpRowStatus": lpE3PlcpRowStatus,
       "lpE3PlcpComponentName": lpE3PlcpComponentName,
       "lpE3PlcpStorageType": lpE3PlcpStorageType,
       "lpE3PlcpIndex": lpE3PlcpIndex,
       "lpE3PlcpOperationalTable": lpE3PlcpOperationalTable,
       "lpE3PlcpOperationalEntry": lpE3PlcpOperationalEntry,
       "lpE3PlcpLofAlarm": lpE3PlcpLofAlarm,
       "lpE3PlcpRxRaiAlarm": lpE3PlcpRxRaiAlarm,
       "lpE3PlcpStatsTable": lpE3PlcpStatsTable,
       "lpE3PlcpStatsEntry": lpE3PlcpStatsEntry,
       "lpE3PlcpErrorFreeSec": lpE3PlcpErrorFreeSec,
       "lpE3PlcpCodingViolations": lpE3PlcpCodingViolations,
       "lpE3PlcpErroredSec": lpE3PlcpErroredSec,
       "lpE3PlcpSevErroredSec": lpE3PlcpSevErroredSec,
       "lpE3PlcpSevErroredFramingSec": lpE3PlcpSevErroredFramingSec,
       "lpE3PlcpUnavailSec": lpE3PlcpUnavailSec,
       "lpE3PlcpFarEndErrorFreeSec": lpE3PlcpFarEndErrorFreeSec,
       "lpE3PlcpFarEndCodingViolations": lpE3PlcpFarEndCodingViolations,
       "lpE3PlcpFarEndErroredSec": lpE3PlcpFarEndErroredSec,
       "lpE3PlcpFarEndSevErroredSec": lpE3PlcpFarEndSevErroredSec,
       "lpE3PlcpFarEndUnavailableSec": lpE3PlcpFarEndUnavailableSec,
       "lpE3Cell": lpE3Cell,
       "lpE3CellRowStatusTable": lpE3CellRowStatusTable,
       "lpE3CellRowStatusEntry": lpE3CellRowStatusEntry,
       "lpE3CellRowStatus": lpE3CellRowStatus,
       "lpE3CellComponentName": lpE3CellComponentName,
       "lpE3CellStorageType": lpE3CellStorageType,
       "lpE3CellIndex": lpE3CellIndex,
       "lpE3CellProvTable": lpE3CellProvTable,
       "lpE3CellProvEntry": lpE3CellProvEntry,
       "lpE3CellAlarmActDelay": lpE3CellAlarmActDelay,
       "lpE3CellScrambleCellPayload": lpE3CellScrambleCellPayload,
       "lpE3CellCorrectSingleBitHeaderErrors": lpE3CellCorrectSingleBitHeaderErrors,
       "lpE3CellOperTable": lpE3CellOperTable,
       "lpE3CellOperEntry": lpE3CellOperEntry,
       "lpE3CellLcdAlarm": lpE3CellLcdAlarm,
       "lpE3CellStatsTable": lpE3CellStatsTable,
       "lpE3CellStatsEntry": lpE3CellStatsEntry,
       "lpE3CellUncorrectableHecErrors": lpE3CellUncorrectableHecErrors,
       "lpE3CellSevErroredSec": lpE3CellSevErroredSec,
       "lpE3CellReceiveCellUtilization": lpE3CellReceiveCellUtilization,
       "lpE3CellTransmitCellUtilization": lpE3CellTransmitCellUtilization,
       "lpE3CellCorrectableHeaderErrors": lpE3CellCorrectableHeaderErrors,
       "lpE3ProvTable": lpE3ProvTable,
       "lpE3ProvEntry": lpE3ProvEntry,
       "lpE3LineLength": lpE3LineLength,
       "lpE3ClockingSource": lpE3ClockingSource,
       "lpE3ApplicationFramerName": lpE3ApplicationFramerName,
       "lpE3Mapping": lpE3Mapping,
       "lpE3Framing": lpE3Framing,
       "lpE3LinkAlarmActivationThreshold": lpE3LinkAlarmActivationThreshold,
       "lpE3LinkAlarmScanInterval": lpE3LinkAlarmScanInterval,
       "lpE3CidDataTable": lpE3CidDataTable,
       "lpE3CidDataEntry": lpE3CidDataEntry,
       "lpE3CustomerIdentifier": lpE3CustomerIdentifier,
       "lpE3AdminInfoTable": lpE3AdminInfoTable,
       "lpE3AdminInfoEntry": lpE3AdminInfoEntry,
       "lpE3Vendor": lpE3Vendor,
       "lpE3CommentText": lpE3CommentText,
       "lpE3IfEntryTable": lpE3IfEntryTable,
       "lpE3IfEntryEntry": lpE3IfEntryEntry,
       "lpE3IfAdminStatus": lpE3IfAdminStatus,
       "lpE3IfIndex": lpE3IfIndex,
       "lpE3OperStatusTable": lpE3OperStatusTable,
       "lpE3OperStatusEntry": lpE3OperStatusEntry,
       "lpE3SnmpOperStatus": lpE3SnmpOperStatus,
       "lpE3StateTable": lpE3StateTable,
       "lpE3StateEntry": lpE3StateEntry,
       "lpE3AdminState": lpE3AdminState,
       "lpE3OperationalState": lpE3OperationalState,
       "lpE3UsageState": lpE3UsageState,
       "lpE3AvailabilityStatus": lpE3AvailabilityStatus,
       "lpE3ProceduralStatus": lpE3ProceduralStatus,
       "lpE3ControlStatus": lpE3ControlStatus,
       "lpE3AlarmStatus": lpE3AlarmStatus,
       "lpE3StandbyStatus": lpE3StandbyStatus,
       "lpE3UnknownStatus": lpE3UnknownStatus,
       "lpE3OperTable": lpE3OperTable,
       "lpE3OperEntry": lpE3OperEntry,
       "lpE3LosAlarm": lpE3LosAlarm,
       "lpE3LofAlarm": lpE3LofAlarm,
       "lpE3RxAisAlarm": lpE3RxAisAlarm,
       "lpE3RxRaiAlarm": lpE3RxRaiAlarm,
       "lpE3TxAis": lpE3TxAis,
       "lpE3TxRai": lpE3TxRai,
       "lpE3StatsTable": lpE3StatsTable,
       "lpE3StatsEntry": lpE3StatsEntry,
       "lpE3RunningTime": lpE3RunningTime,
       "lpE3ErrorFreeSec": lpE3ErrorFreeSec,
       "lpE3LineCodeViolations": lpE3LineCodeViolations,
       "lpE3LineErroredSec": lpE3LineErroredSec,
       "lpE3LineSevErroredSec": lpE3LineSevErroredSec,
       "lpE3LineLosSec": lpE3LineLosSec,
       "lpE3LineFailures": lpE3LineFailures,
       "lpE3PathCodeViolations": lpE3PathCodeViolations,
       "lpE3PathErroredSec": lpE3PathErroredSec,
       "lpE3PathSevErroredSec": lpE3PathSevErroredSec,
       "lpE3PathSefAisSec": lpE3PathSefAisSec,
       "lpE3PathUnavailSec": lpE3PathUnavailSec,
       "lpE3PathFailures": lpE3PathFailures,
       "lpDS1": lpDS1,
       "lpDS1RowStatusTable": lpDS1RowStatusTable,
       "lpDS1RowStatusEntry": lpDS1RowStatusEntry,
       "lpDS1RowStatus": lpDS1RowStatus,
       "lpDS1ComponentName": lpDS1ComponentName,
       "lpDS1StorageType": lpDS1StorageType,
       "lpDS1Index": lpDS1Index,
       "lpDS1Chan": lpDS1Chan,
       "lpDS1ChanRowStatusTable": lpDS1ChanRowStatusTable,
       "lpDS1ChanRowStatusEntry": lpDS1ChanRowStatusEntry,
       "lpDS1ChanRowStatus": lpDS1ChanRowStatus,
       "lpDS1ChanComponentName": lpDS1ChanComponentName,
       "lpDS1ChanStorageType": lpDS1ChanStorageType,
       "lpDS1ChanIndex": lpDS1ChanIndex,
       "lpDS1ChanTest": lpDS1ChanTest,
       "lpDS1ChanTestRowStatusTable": lpDS1ChanTestRowStatusTable,
       "lpDS1ChanTestRowStatusEntry": lpDS1ChanTestRowStatusEntry,
       "lpDS1ChanTestRowStatus": lpDS1ChanTestRowStatus,
       "lpDS1ChanTestComponentName": lpDS1ChanTestComponentName,
       "lpDS1ChanTestStorageType": lpDS1ChanTestStorageType,
       "lpDS1ChanTestIndex": lpDS1ChanTestIndex,
       "lpDS1ChanTestStateTable": lpDS1ChanTestStateTable,
       "lpDS1ChanTestStateEntry": lpDS1ChanTestStateEntry,
       "lpDS1ChanTestAdminState": lpDS1ChanTestAdminState,
       "lpDS1ChanTestOperationalState": lpDS1ChanTestOperationalState,
       "lpDS1ChanTestUsageState": lpDS1ChanTestUsageState,
       "lpDS1ChanTestSetupTable": lpDS1ChanTestSetupTable,
       "lpDS1ChanTestSetupEntry": lpDS1ChanTestSetupEntry,
       "lpDS1ChanTestPurpose": lpDS1ChanTestPurpose,
       "lpDS1ChanTestType": lpDS1ChanTestType,
       "lpDS1ChanTestFrmSize": lpDS1ChanTestFrmSize,
       "lpDS1ChanTestFrmPatternType": lpDS1ChanTestFrmPatternType,
       "lpDS1ChanTestCustomizedPattern": lpDS1ChanTestCustomizedPattern,
       "lpDS1ChanTestDataStartDelay": lpDS1ChanTestDataStartDelay,
       "lpDS1ChanTestDisplayInterval": lpDS1ChanTestDisplayInterval,
       "lpDS1ChanTestDuration": lpDS1ChanTestDuration,
       "lpDS1ChanTestResultsTable": lpDS1ChanTestResultsTable,
       "lpDS1ChanTestResultsEntry": lpDS1ChanTestResultsEntry,
       "lpDS1ChanTestElapsedTime": lpDS1ChanTestElapsedTime,
       "lpDS1ChanTestTimeRemaining": lpDS1ChanTestTimeRemaining,
       "lpDS1ChanTestCauseOfTermination": lpDS1ChanTestCauseOfTermination,
       "lpDS1ChanTestBitsTx": lpDS1ChanTestBitsTx,
       "lpDS1ChanTestBytesTx": lpDS1ChanTestBytesTx,
       "lpDS1ChanTestFrmTx": lpDS1ChanTestFrmTx,
       "lpDS1ChanTestBitsRx": lpDS1ChanTestBitsRx,
       "lpDS1ChanTestBytesRx": lpDS1ChanTestBytesRx,
       "lpDS1ChanTestFrmRx": lpDS1ChanTestFrmRx,
       "lpDS1ChanTestErroredFrmRx": lpDS1ChanTestErroredFrmRx,
       "lpDS1ChanTestBitErrorRate": lpDS1ChanTestBitErrorRate,
       "lpDS1ChanCell": lpDS1ChanCell,
       "lpDS1ChanCellRowStatusTable": lpDS1ChanCellRowStatusTable,
       "lpDS1ChanCellRowStatusEntry": lpDS1ChanCellRowStatusEntry,
       "lpDS1ChanCellRowStatus": lpDS1ChanCellRowStatus,
       "lpDS1ChanCellComponentName": lpDS1ChanCellComponentName,
       "lpDS1ChanCellStorageType": lpDS1ChanCellStorageType,
       "lpDS1ChanCellIndex": lpDS1ChanCellIndex,
       "lpDS1ChanCellProvTable": lpDS1ChanCellProvTable,
       "lpDS1ChanCellProvEntry": lpDS1ChanCellProvEntry,
       "lpDS1ChanCellAlarmActDelay": lpDS1ChanCellAlarmActDelay,
       "lpDS1ChanCellScrambleCellPayload": lpDS1ChanCellScrambleCellPayload,
       "lpDS1ChanCellCorrectSingleBitHeaderErrors": lpDS1ChanCellCorrectSingleBitHeaderErrors,
       "lpDS1ChanCellOperTable": lpDS1ChanCellOperTable,
       "lpDS1ChanCellOperEntry": lpDS1ChanCellOperEntry,
       "lpDS1ChanCellLcdAlarm": lpDS1ChanCellLcdAlarm,
       "lpDS1ChanCellStatsTable": lpDS1ChanCellStatsTable,
       "lpDS1ChanCellStatsEntry": lpDS1ChanCellStatsEntry,
       "lpDS1ChanCellUncorrectableHecErrors": lpDS1ChanCellUncorrectableHecErrors,
       "lpDS1ChanCellSevErroredSec": lpDS1ChanCellSevErroredSec,
       "lpDS1ChanCellReceiveCellUtilization": lpDS1ChanCellReceiveCellUtilization,
       "lpDS1ChanCellTransmitCellUtilization": lpDS1ChanCellTransmitCellUtilization,
       "lpDS1ChanCellCorrectableHeaderErrors": lpDS1ChanCellCorrectableHeaderErrors,
       "lpDS1ChanTc": lpDS1ChanTc,
       "lpDS1ChanTcRowStatusTable": lpDS1ChanTcRowStatusTable,
       "lpDS1ChanTcRowStatusEntry": lpDS1ChanTcRowStatusEntry,
       "lpDS1ChanTcRowStatus": lpDS1ChanTcRowStatus,
       "lpDS1ChanTcComponentName": lpDS1ChanTcComponentName,
       "lpDS1ChanTcStorageType": lpDS1ChanTcStorageType,
       "lpDS1ChanTcIndex": lpDS1ChanTcIndex,
       "lpDS1ChanTcProvTable": lpDS1ChanTcProvTable,
       "lpDS1ChanTcProvEntry": lpDS1ChanTcProvEntry,
       "lpDS1ChanTcReplacementData": lpDS1ChanTcReplacementData,
       "lpDS1ChanTcSignalOneDuration": lpDS1ChanTcSignalOneDuration,
       "lpDS1ChanTcOpTable": lpDS1ChanTcOpTable,
       "lpDS1ChanTcOpEntry": lpDS1ChanTcOpEntry,
       "lpDS1ChanTcIngressConditioning": lpDS1ChanTcIngressConditioning,
       "lpDS1ChanTcEgressConditioning": lpDS1ChanTcEgressConditioning,
       "lpDS1ChanTcSigOneTable": lpDS1ChanTcSigOneTable,
       "lpDS1ChanTcSigOneEntry": lpDS1ChanTcSigOneEntry,
       "lpDS1ChanTcSigOneIndex": lpDS1ChanTcSigOneIndex,
       "lpDS1ChanTcSigOneValue": lpDS1ChanTcSigOneValue,
       "lpDS1ChanTcSigTwoTable": lpDS1ChanTcSigTwoTable,
       "lpDS1ChanTcSigTwoEntry": lpDS1ChanTcSigTwoEntry,
       "lpDS1ChanTcSigTwoIndex": lpDS1ChanTcSigTwoIndex,
       "lpDS1ChanTcSigTwoValue": lpDS1ChanTcSigTwoValue,
       "lpDS1ChanProvTable": lpDS1ChanProvTable,
       "lpDS1ChanProvEntry": lpDS1ChanProvEntry,
       "lpDS1ChanTimeslots": lpDS1ChanTimeslots,
       "lpDS1ChanTimeslotDataRate": lpDS1ChanTimeslotDataRate,
       "lpDS1ChanApplicationFramerName": lpDS1ChanApplicationFramerName,
       "lpDS1ChanCidDataTable": lpDS1ChanCidDataTable,
       "lpDS1ChanCidDataEntry": lpDS1ChanCidDataEntry,
       "lpDS1ChanCustomerIdentifier": lpDS1ChanCustomerIdentifier,
       "lpDS1ChanIfEntryTable": lpDS1ChanIfEntryTable,
       "lpDS1ChanIfEntryEntry": lpDS1ChanIfEntryEntry,
       "lpDS1ChanIfAdminStatus": lpDS1ChanIfAdminStatus,
       "lpDS1ChanIfIndex": lpDS1ChanIfIndex,
       "lpDS1ChanOperStatusTable": lpDS1ChanOperStatusTable,
       "lpDS1ChanOperStatusEntry": lpDS1ChanOperStatusEntry,
       "lpDS1ChanSnmpOperStatus": lpDS1ChanSnmpOperStatus,
       "lpDS1ChanStateTable": lpDS1ChanStateTable,
       "lpDS1ChanStateEntry": lpDS1ChanStateEntry,
       "lpDS1ChanAdminState": lpDS1ChanAdminState,
       "lpDS1ChanOperationalState": lpDS1ChanOperationalState,
       "lpDS1ChanUsageState": lpDS1ChanUsageState,
       "lpDS1ChanAvailabilityStatus": lpDS1ChanAvailabilityStatus,
       "lpDS1ChanProceduralStatus": lpDS1ChanProceduralStatus,
       "lpDS1ChanControlStatus": lpDS1ChanControlStatus,
       "lpDS1ChanAlarmStatus": lpDS1ChanAlarmStatus,
       "lpDS1ChanStandbyStatus": lpDS1ChanStandbyStatus,
       "lpDS1ChanUnknownStatus": lpDS1ChanUnknownStatus,
       "lpDS1ChanOperTable": lpDS1ChanOperTable,
       "lpDS1ChanOperEntry": lpDS1ChanOperEntry,
       "lpDS1ChanActualChannelSpeed": lpDS1ChanActualChannelSpeed,
       "lpDS1ChanAdminInfoTable": lpDS1ChanAdminInfoTable,
       "lpDS1ChanAdminInfoEntry": lpDS1ChanAdminInfoEntry,
       "lpDS1ChanVendor": lpDS1ChanVendor,
       "lpDS1ChanCommentText": lpDS1ChanCommentText,
       "lpDS1Test": lpDS1Test,
       "lpDS1TestRowStatusTable": lpDS1TestRowStatusTable,
       "lpDS1TestRowStatusEntry": lpDS1TestRowStatusEntry,
       "lpDS1TestRowStatus": lpDS1TestRowStatus,
       "lpDS1TestComponentName": lpDS1TestComponentName,
       "lpDS1TestStorageType": lpDS1TestStorageType,
       "lpDS1TestIndex": lpDS1TestIndex,
       "lpDS1TestStateTable": lpDS1TestStateTable,
       "lpDS1TestStateEntry": lpDS1TestStateEntry,
       "lpDS1TestAdminState": lpDS1TestAdminState,
       "lpDS1TestOperationalState": lpDS1TestOperationalState,
       "lpDS1TestUsageState": lpDS1TestUsageState,
       "lpDS1TestSetupTable": lpDS1TestSetupTable,
       "lpDS1TestSetupEntry": lpDS1TestSetupEntry,
       "lpDS1TestPurpose": lpDS1TestPurpose,
       "lpDS1TestType": lpDS1TestType,
       "lpDS1TestFrmSize": lpDS1TestFrmSize,
       "lpDS1TestFrmPatternType": lpDS1TestFrmPatternType,
       "lpDS1TestCustomizedPattern": lpDS1TestCustomizedPattern,
       "lpDS1TestDataStartDelay": lpDS1TestDataStartDelay,
       "lpDS1TestDisplayInterval": lpDS1TestDisplayInterval,
       "lpDS1TestDuration": lpDS1TestDuration,
       "lpDS1TestResultsTable": lpDS1TestResultsTable,
       "lpDS1TestResultsEntry": lpDS1TestResultsEntry,
       "lpDS1TestElapsedTime": lpDS1TestElapsedTime,
       "lpDS1TestTimeRemaining": lpDS1TestTimeRemaining,
       "lpDS1TestCauseOfTermination": lpDS1TestCauseOfTermination,
       "lpDS1TestBitsTx": lpDS1TestBitsTx,
       "lpDS1TestBytesTx": lpDS1TestBytesTx,
       "lpDS1TestFrmTx": lpDS1TestFrmTx,
       "lpDS1TestBitsRx": lpDS1TestBitsRx,
       "lpDS1TestBytesRx": lpDS1TestBytesRx,
       "lpDS1TestFrmRx": lpDS1TestFrmRx,
       "lpDS1TestErroredFrmRx": lpDS1TestErroredFrmRx,
       "lpDS1TestBitErrorRate": lpDS1TestBitErrorRate,
       "lpDS1Dsp": lpDS1Dsp,
       "lpDS1DspRowStatusTable": lpDS1DspRowStatusTable,
       "lpDS1DspRowStatusEntry": lpDS1DspRowStatusEntry,
       "lpDS1DspRowStatus": lpDS1DspRowStatus,
       "lpDS1DspComponentName": lpDS1DspComponentName,
       "lpDS1DspStorageType": lpDS1DspStorageType,
       "lpDS1DspIndex": lpDS1DspIndex,
       "lpDS1Audio": lpDS1Audio,
       "lpDS1AudioRowStatusTable": lpDS1AudioRowStatusTable,
       "lpDS1AudioRowStatusEntry": lpDS1AudioRowStatusEntry,
       "lpDS1AudioRowStatus": lpDS1AudioRowStatus,
       "lpDS1AudioComponentName": lpDS1AudioComponentName,
       "lpDS1AudioStorageType": lpDS1AudioStorageType,
       "lpDS1AudioIndex": lpDS1AudioIndex,
       "lpDS1ProvTable": lpDS1ProvTable,
       "lpDS1ProvEntry": lpDS1ProvEntry,
       "lpDS1LineType": lpDS1LineType,
       "lpDS1ZeroCoding": lpDS1ZeroCoding,
       "lpDS1ClockingSource": lpDS1ClockingSource,
       "lpDS1RaiAlarmType": lpDS1RaiAlarmType,
       "lpDS1LineLength": lpDS1LineLength,
       "lpDS1CidDataTable": lpDS1CidDataTable,
       "lpDS1CidDataEntry": lpDS1CidDataEntry,
       "lpDS1CustomerIdentifier": lpDS1CustomerIdentifier,
       "lpDS1AdminInfoTable": lpDS1AdminInfoTable,
       "lpDS1AdminInfoEntry": lpDS1AdminInfoEntry,
       "lpDS1Vendor": lpDS1Vendor,
       "lpDS1CommentText": lpDS1CommentText,
       "lpDS1IfEntryTable": lpDS1IfEntryTable,
       "lpDS1IfEntryEntry": lpDS1IfEntryEntry,
       "lpDS1IfAdminStatus": lpDS1IfAdminStatus,
       "lpDS1IfIndex": lpDS1IfIndex,
       "lpDS1OperStatusTable": lpDS1OperStatusTable,
       "lpDS1OperStatusEntry": lpDS1OperStatusEntry,
       "lpDS1SnmpOperStatus": lpDS1SnmpOperStatus,
       "lpDS1StateTable": lpDS1StateTable,
       "lpDS1StateEntry": lpDS1StateEntry,
       "lpDS1AdminState": lpDS1AdminState,
       "lpDS1OperationalState": lpDS1OperationalState,
       "lpDS1UsageState": lpDS1UsageState,
       "lpDS1AvailabilityStatus": lpDS1AvailabilityStatus,
       "lpDS1ProceduralStatus": lpDS1ProceduralStatus,
       "lpDS1ControlStatus": lpDS1ControlStatus,
       "lpDS1AlarmStatus": lpDS1AlarmStatus,
       "lpDS1StandbyStatus": lpDS1StandbyStatus,
       "lpDS1UnknownStatus": lpDS1UnknownStatus,
       "lpDS1OperTable": lpDS1OperTable,
       "lpDS1OperEntry": lpDS1OperEntry,
       "lpDS1LosAlarm": lpDS1LosAlarm,
       "lpDS1RxAisAlarm": lpDS1RxAisAlarm,
       "lpDS1LofAlarm": lpDS1LofAlarm,
       "lpDS1RxRaiAlarm": lpDS1RxRaiAlarm,
       "lpDS1TxAisAlarm": lpDS1TxAisAlarm,
       "lpDS1TxRaiAlarm": lpDS1TxRaiAlarm,
       "lpDS1StatsTable": lpDS1StatsTable,
       "lpDS1StatsEntry": lpDS1StatsEntry,
       "lpDS1RunningTime": lpDS1RunningTime,
       "lpDS1ErrorFreeSec": lpDS1ErrorFreeSec,
       "lpDS1ErroredSec": lpDS1ErroredSec,
       "lpDS1SevErroredSec": lpDS1SevErroredSec,
       "lpDS1SevErroredFrmSec": lpDS1SevErroredFrmSec,
       "lpDS1UnavailSec": lpDS1UnavailSec,
       "lpDS1BpvErrors": lpDS1BpvErrors,
       "lpDS1CrcErrors": lpDS1CrcErrors,
       "lpDS1FrmErrors": lpDS1FrmErrors,
       "lpDS1LosStateChanges": lpDS1LosStateChanges,
       "lpDS1SlipErrors": lpDS1SlipErrors,
       "lpE1": lpE1,
       "lpE1RowStatusTable": lpE1RowStatusTable,
       "lpE1RowStatusEntry": lpE1RowStatusEntry,
       "lpE1RowStatus": lpE1RowStatus,
       "lpE1ComponentName": lpE1ComponentName,
       "lpE1StorageType": lpE1StorageType,
       "lpE1Index": lpE1Index,
       "lpE1Chan": lpE1Chan,
       "lpE1ChanRowStatusTable": lpE1ChanRowStatusTable,
       "lpE1ChanRowStatusEntry": lpE1ChanRowStatusEntry,
       "lpE1ChanRowStatus": lpE1ChanRowStatus,
       "lpE1ChanComponentName": lpE1ChanComponentName,
       "lpE1ChanStorageType": lpE1ChanStorageType,
       "lpE1ChanIndex": lpE1ChanIndex,
       "lpE1ChanTest": lpE1ChanTest,
       "lpE1ChanTestRowStatusTable": lpE1ChanTestRowStatusTable,
       "lpE1ChanTestRowStatusEntry": lpE1ChanTestRowStatusEntry,
       "lpE1ChanTestRowStatus": lpE1ChanTestRowStatus,
       "lpE1ChanTestComponentName": lpE1ChanTestComponentName,
       "lpE1ChanTestStorageType": lpE1ChanTestStorageType,
       "lpE1ChanTestIndex": lpE1ChanTestIndex,
       "lpE1ChanTestStateTable": lpE1ChanTestStateTable,
       "lpE1ChanTestStateEntry": lpE1ChanTestStateEntry,
       "lpE1ChanTestAdminState": lpE1ChanTestAdminState,
       "lpE1ChanTestOperationalState": lpE1ChanTestOperationalState,
       "lpE1ChanTestUsageState": lpE1ChanTestUsageState,
       "lpE1ChanTestSetupTable": lpE1ChanTestSetupTable,
       "lpE1ChanTestSetupEntry": lpE1ChanTestSetupEntry,
       "lpE1ChanTestPurpose": lpE1ChanTestPurpose,
       "lpE1ChanTestType": lpE1ChanTestType,
       "lpE1ChanTestFrmSize": lpE1ChanTestFrmSize,
       "lpE1ChanTestFrmPatternType": lpE1ChanTestFrmPatternType,
       "lpE1ChanTestCustomizedPattern": lpE1ChanTestCustomizedPattern,
       "lpE1ChanTestDataStartDelay": lpE1ChanTestDataStartDelay,
       "lpE1ChanTestDisplayInterval": lpE1ChanTestDisplayInterval,
       "lpE1ChanTestDuration": lpE1ChanTestDuration,
       "lpE1ChanTestResultsTable": lpE1ChanTestResultsTable,
       "lpE1ChanTestResultsEntry": lpE1ChanTestResultsEntry,
       "lpE1ChanTestElapsedTime": lpE1ChanTestElapsedTime,
       "lpE1ChanTestTimeRemaining": lpE1ChanTestTimeRemaining,
       "lpE1ChanTestCauseOfTermination": lpE1ChanTestCauseOfTermination,
       "lpE1ChanTestBitsTx": lpE1ChanTestBitsTx,
       "lpE1ChanTestBytesTx": lpE1ChanTestBytesTx,
       "lpE1ChanTestFrmTx": lpE1ChanTestFrmTx,
       "lpE1ChanTestBitsRx": lpE1ChanTestBitsRx,
       "lpE1ChanTestBytesRx": lpE1ChanTestBytesRx,
       "lpE1ChanTestFrmRx": lpE1ChanTestFrmRx,
       "lpE1ChanTestErroredFrmRx": lpE1ChanTestErroredFrmRx,
       "lpE1ChanTestBitErrorRate": lpE1ChanTestBitErrorRate,
       "lpE1ChanCell": lpE1ChanCell,
       "lpE1ChanCellRowStatusTable": lpE1ChanCellRowStatusTable,
       "lpE1ChanCellRowStatusEntry": lpE1ChanCellRowStatusEntry,
       "lpE1ChanCellRowStatus": lpE1ChanCellRowStatus,
       "lpE1ChanCellComponentName": lpE1ChanCellComponentName,
       "lpE1ChanCellStorageType": lpE1ChanCellStorageType,
       "lpE1ChanCellIndex": lpE1ChanCellIndex,
       "lpE1ChanCellProvTable": lpE1ChanCellProvTable,
       "lpE1ChanCellProvEntry": lpE1ChanCellProvEntry,
       "lpE1ChanCellAlarmActDelay": lpE1ChanCellAlarmActDelay,
       "lpE1ChanCellScrambleCellPayload": lpE1ChanCellScrambleCellPayload,
       "lpE1ChanCellCorrectSingleBitHeaderErrors": lpE1ChanCellCorrectSingleBitHeaderErrors,
       "lpE1ChanCellOperTable": lpE1ChanCellOperTable,
       "lpE1ChanCellOperEntry": lpE1ChanCellOperEntry,
       "lpE1ChanCellLcdAlarm": lpE1ChanCellLcdAlarm,
       "lpE1ChanCellStatsTable": lpE1ChanCellStatsTable,
       "lpE1ChanCellStatsEntry": lpE1ChanCellStatsEntry,
       "lpE1ChanCellUncorrectableHecErrors": lpE1ChanCellUncorrectableHecErrors,
       "lpE1ChanCellSevErroredSec": lpE1ChanCellSevErroredSec,
       "lpE1ChanCellReceiveCellUtilization": lpE1ChanCellReceiveCellUtilization,
       "lpE1ChanCellTransmitCellUtilization": lpE1ChanCellTransmitCellUtilization,
       "lpE1ChanCellCorrectableHeaderErrors": lpE1ChanCellCorrectableHeaderErrors,
       "lpE1ChanTc": lpE1ChanTc,
       "lpE1ChanTcRowStatusTable": lpE1ChanTcRowStatusTable,
       "lpE1ChanTcRowStatusEntry": lpE1ChanTcRowStatusEntry,
       "lpE1ChanTcRowStatus": lpE1ChanTcRowStatus,
       "lpE1ChanTcComponentName": lpE1ChanTcComponentName,
       "lpE1ChanTcStorageType": lpE1ChanTcStorageType,
       "lpE1ChanTcIndex": lpE1ChanTcIndex,
       "lpE1ChanTcProvTable": lpE1ChanTcProvTable,
       "lpE1ChanTcProvEntry": lpE1ChanTcProvEntry,
       "lpE1ChanTcReplacementData": lpE1ChanTcReplacementData,
       "lpE1ChanTcSignalOneDuration": lpE1ChanTcSignalOneDuration,
       "lpE1ChanTcOpTable": lpE1ChanTcOpTable,
       "lpE1ChanTcOpEntry": lpE1ChanTcOpEntry,
       "lpE1ChanTcIngressConditioning": lpE1ChanTcIngressConditioning,
       "lpE1ChanTcEgressConditioning": lpE1ChanTcEgressConditioning,
       "lpE1ChanTcSigOneTable": lpE1ChanTcSigOneTable,
       "lpE1ChanTcSigOneEntry": lpE1ChanTcSigOneEntry,
       "lpE1ChanTcSigOneIndex": lpE1ChanTcSigOneIndex,
       "lpE1ChanTcSigOneValue": lpE1ChanTcSigOneValue,
       "lpE1ChanTcSigTwoTable": lpE1ChanTcSigTwoTable,
       "lpE1ChanTcSigTwoEntry": lpE1ChanTcSigTwoEntry,
       "lpE1ChanTcSigTwoIndex": lpE1ChanTcSigTwoIndex,
       "lpE1ChanTcSigTwoValue": lpE1ChanTcSigTwoValue,
       "lpE1ChanProvTable": lpE1ChanProvTable,
       "lpE1ChanProvEntry": lpE1ChanProvEntry,
       "lpE1ChanTimeslots": lpE1ChanTimeslots,
       "lpE1ChanTimeslotDataRate": lpE1ChanTimeslotDataRate,
       "lpE1ChanApplicationFramerName": lpE1ChanApplicationFramerName,
       "lpE1ChanCidDataTable": lpE1ChanCidDataTable,
       "lpE1ChanCidDataEntry": lpE1ChanCidDataEntry,
       "lpE1ChanCustomerIdentifier": lpE1ChanCustomerIdentifier,
       "lpE1ChanIfEntryTable": lpE1ChanIfEntryTable,
       "lpE1ChanIfEntryEntry": lpE1ChanIfEntryEntry,
       "lpE1ChanIfAdminStatus": lpE1ChanIfAdminStatus,
       "lpE1ChanIfIndex": lpE1ChanIfIndex,
       "lpE1ChanOperStatusTable": lpE1ChanOperStatusTable,
       "lpE1ChanOperStatusEntry": lpE1ChanOperStatusEntry,
       "lpE1ChanSnmpOperStatus": lpE1ChanSnmpOperStatus,
       "lpE1ChanStateTable": lpE1ChanStateTable,
       "lpE1ChanStateEntry": lpE1ChanStateEntry,
       "lpE1ChanAdminState": lpE1ChanAdminState,
       "lpE1ChanOperationalState": lpE1ChanOperationalState,
       "lpE1ChanUsageState": lpE1ChanUsageState,
       "lpE1ChanAvailabilityStatus": lpE1ChanAvailabilityStatus,
       "lpE1ChanProceduralStatus": lpE1ChanProceduralStatus,
       "lpE1ChanControlStatus": lpE1ChanControlStatus,
       "lpE1ChanAlarmStatus": lpE1ChanAlarmStatus,
       "lpE1ChanStandbyStatus": lpE1ChanStandbyStatus,
       "lpE1ChanUnknownStatus": lpE1ChanUnknownStatus,
       "lpE1ChanOperTable": lpE1ChanOperTable,
       "lpE1ChanOperEntry": lpE1ChanOperEntry,
       "lpE1ChanActualChannelSpeed": lpE1ChanActualChannelSpeed,
       "lpE1ChanAdminInfoTable": lpE1ChanAdminInfoTable,
       "lpE1ChanAdminInfoEntry": lpE1ChanAdminInfoEntry,
       "lpE1ChanVendor": lpE1ChanVendor,
       "lpE1ChanCommentText": lpE1ChanCommentText,
       "lpE1Test": lpE1Test,
       "lpE1TestRowStatusTable": lpE1TestRowStatusTable,
       "lpE1TestRowStatusEntry": lpE1TestRowStatusEntry,
       "lpE1TestRowStatus": lpE1TestRowStatus,
       "lpE1TestComponentName": lpE1TestComponentName,
       "lpE1TestStorageType": lpE1TestStorageType,
       "lpE1TestIndex": lpE1TestIndex,
       "lpE1TestStateTable": lpE1TestStateTable,
       "lpE1TestStateEntry": lpE1TestStateEntry,
       "lpE1TestAdminState": lpE1TestAdminState,
       "lpE1TestOperationalState": lpE1TestOperationalState,
       "lpE1TestUsageState": lpE1TestUsageState,
       "lpE1TestSetupTable": lpE1TestSetupTable,
       "lpE1TestSetupEntry": lpE1TestSetupEntry,
       "lpE1TestPurpose": lpE1TestPurpose,
       "lpE1TestType": lpE1TestType,
       "lpE1TestFrmSize": lpE1TestFrmSize,
       "lpE1TestFrmPatternType": lpE1TestFrmPatternType,
       "lpE1TestCustomizedPattern": lpE1TestCustomizedPattern,
       "lpE1TestDataStartDelay": lpE1TestDataStartDelay,
       "lpE1TestDisplayInterval": lpE1TestDisplayInterval,
       "lpE1TestDuration": lpE1TestDuration,
       "lpE1TestResultsTable": lpE1TestResultsTable,
       "lpE1TestResultsEntry": lpE1TestResultsEntry,
       "lpE1TestElapsedTime": lpE1TestElapsedTime,
       "lpE1TestTimeRemaining": lpE1TestTimeRemaining,
       "lpE1TestCauseOfTermination": lpE1TestCauseOfTermination,
       "lpE1TestBitsTx": lpE1TestBitsTx,
       "lpE1TestBytesTx": lpE1TestBytesTx,
       "lpE1TestFrmTx": lpE1TestFrmTx,
       "lpE1TestBitsRx": lpE1TestBitsRx,
       "lpE1TestBytesRx": lpE1TestBytesRx,
       "lpE1TestFrmRx": lpE1TestFrmRx,
       "lpE1TestErroredFrmRx": lpE1TestErroredFrmRx,
       "lpE1TestBitErrorRate": lpE1TestBitErrorRate,
       "lpE1Dsp": lpE1Dsp,
       "lpE1DspRowStatusTable": lpE1DspRowStatusTable,
       "lpE1DspRowStatusEntry": lpE1DspRowStatusEntry,
       "lpE1DspRowStatus": lpE1DspRowStatus,
       "lpE1DspComponentName": lpE1DspComponentName,
       "lpE1DspStorageType": lpE1DspStorageType,
       "lpE1DspIndex": lpE1DspIndex,
       "lpE1Audio": lpE1Audio,
       "lpE1AudioRowStatusTable": lpE1AudioRowStatusTable,
       "lpE1AudioRowStatusEntry": lpE1AudioRowStatusEntry,
       "lpE1AudioRowStatus": lpE1AudioRowStatus,
       "lpE1AudioComponentName": lpE1AudioComponentName,
       "lpE1AudioStorageType": lpE1AudioStorageType,
       "lpE1AudioIndex": lpE1AudioIndex,
       "lpE1ProvTable": lpE1ProvTable,
       "lpE1ProvEntry": lpE1ProvEntry,
       "lpE1LineType": lpE1LineType,
       "lpE1ClockingSource": lpE1ClockingSource,
       "lpE1Crc4Mode": lpE1Crc4Mode,
       "lpE1SendRaiOnAis": lpE1SendRaiOnAis,
       "lpE1RaiDeclareAlarmTime": lpE1RaiDeclareAlarmTime,
       "lpE1RaiClearAlarmTime": lpE1RaiClearAlarmTime,
       "lpE1CidDataTable": lpE1CidDataTable,
       "lpE1CidDataEntry": lpE1CidDataEntry,
       "lpE1CustomerIdentifier": lpE1CustomerIdentifier,
       "lpE1AdminInfoTable": lpE1AdminInfoTable,
       "lpE1AdminInfoEntry": lpE1AdminInfoEntry,
       "lpE1Vendor": lpE1Vendor,
       "lpE1CommentText": lpE1CommentText,
       "lpE1IfEntryTable": lpE1IfEntryTable,
       "lpE1IfEntryEntry": lpE1IfEntryEntry,
       "lpE1IfAdminStatus": lpE1IfAdminStatus,
       "lpE1IfIndex": lpE1IfIndex,
       "lpE1OperStatusTable": lpE1OperStatusTable,
       "lpE1OperStatusEntry": lpE1OperStatusEntry,
       "lpE1SnmpOperStatus": lpE1SnmpOperStatus,
       "lpE1StateTable": lpE1StateTable,
       "lpE1StateEntry": lpE1StateEntry,
       "lpE1AdminState": lpE1AdminState,
       "lpE1OperationalState": lpE1OperationalState,
       "lpE1UsageState": lpE1UsageState,
       "lpE1AvailabilityStatus": lpE1AvailabilityStatus,
       "lpE1ProceduralStatus": lpE1ProceduralStatus,
       "lpE1ControlStatus": lpE1ControlStatus,
       "lpE1AlarmStatus": lpE1AlarmStatus,
       "lpE1StandbyStatus": lpE1StandbyStatus,
       "lpE1UnknownStatus": lpE1UnknownStatus,
       "lpE1OperTable": lpE1OperTable,
       "lpE1OperEntry": lpE1OperEntry,
       "lpE1LosAlarm": lpE1LosAlarm,
       "lpE1RxAisAlarm": lpE1RxAisAlarm,
       "lpE1LofAlarm": lpE1LofAlarm,
       "lpE1RxRaiAlarm": lpE1RxRaiAlarm,
       "lpE1TxAisAlarm": lpE1TxAisAlarm,
       "lpE1TxRaiAlarm": lpE1TxRaiAlarm,
       "lpE1E1OperTable": lpE1E1OperTable,
       "lpE1E1OperEntry": lpE1E1OperEntry,
       "lpE1MultifrmLofAlarm": lpE1MultifrmLofAlarm,
       "lpE1RxMultifrmRaiAlarm": lpE1RxMultifrmRaiAlarm,
       "lpE1TxMultifrmRaiAlarm": lpE1TxMultifrmRaiAlarm,
       "lpE1StatsTable": lpE1StatsTable,
       "lpE1StatsEntry": lpE1StatsEntry,
       "lpE1RunningTime": lpE1RunningTime,
       "lpE1ErrorFreeSec": lpE1ErrorFreeSec,
       "lpE1ErroredSec": lpE1ErroredSec,
       "lpE1SevErroredSec": lpE1SevErroredSec,
       "lpE1SevErroredFrmSec": lpE1SevErroredFrmSec,
       "lpE1UnavailSec": lpE1UnavailSec,
       "lpE1BpvErrors": lpE1BpvErrors,
       "lpE1CrcErrors": lpE1CrcErrors,
       "lpE1FrmErrors": lpE1FrmErrors,
       "lpE1LosStateChanges": lpE1LosStateChanges,
       "lpE1SlipErrors": lpE1SlipErrors,
       "lpV35": lpV35,
       "lpV35RowStatusTable": lpV35RowStatusTable,
       "lpV35RowStatusEntry": lpV35RowStatusEntry,
       "lpV35RowStatus": lpV35RowStatus,
       "lpV35ComponentName": lpV35ComponentName,
       "lpV35StorageType": lpV35StorageType,
       "lpV35Index": lpV35Index,
       "lpV35Test": lpV35Test,
       "lpV35TestRowStatusTable": lpV35TestRowStatusTable,
       "lpV35TestRowStatusEntry": lpV35TestRowStatusEntry,
       "lpV35TestRowStatus": lpV35TestRowStatus,
       "lpV35TestComponentName": lpV35TestComponentName,
       "lpV35TestStorageType": lpV35TestStorageType,
       "lpV35TestIndex": lpV35TestIndex,
       "lpV35TestStateTable": lpV35TestStateTable,
       "lpV35TestStateEntry": lpV35TestStateEntry,
       "lpV35TestAdminState": lpV35TestAdminState,
       "lpV35TestOperationalState": lpV35TestOperationalState,
       "lpV35TestUsageState": lpV35TestUsageState,
       "lpV35TestSetupTable": lpV35TestSetupTable,
       "lpV35TestSetupEntry": lpV35TestSetupEntry,
       "lpV35TestPurpose": lpV35TestPurpose,
       "lpV35TestType": lpV35TestType,
       "lpV35TestFrmSize": lpV35TestFrmSize,
       "lpV35TestFrmPatternType": lpV35TestFrmPatternType,
       "lpV35TestCustomizedPattern": lpV35TestCustomizedPattern,
       "lpV35TestDataStartDelay": lpV35TestDataStartDelay,
       "lpV35TestDisplayInterval": lpV35TestDisplayInterval,
       "lpV35TestDuration": lpV35TestDuration,
       "lpV35TestResultsTable": lpV35TestResultsTable,
       "lpV35TestResultsEntry": lpV35TestResultsEntry,
       "lpV35TestElapsedTime": lpV35TestElapsedTime,
       "lpV35TestTimeRemaining": lpV35TestTimeRemaining,
       "lpV35TestCauseOfTermination": lpV35TestCauseOfTermination,
       "lpV35TestBitsTx": lpV35TestBitsTx,
       "lpV35TestBytesTx": lpV35TestBytesTx,
       "lpV35TestFrmTx": lpV35TestFrmTx,
       "lpV35TestBitsRx": lpV35TestBitsRx,
       "lpV35TestBytesRx": lpV35TestBytesRx,
       "lpV35TestFrmRx": lpV35TestFrmRx,
       "lpV35TestErroredFrmRx": lpV35TestErroredFrmRx,
       "lpV35TestBitErrorRate": lpV35TestBitErrorRate,
       "lpV35ProvTable": lpV35ProvTable,
       "lpV35ProvEntry": lpV35ProvEntry,
       "lpV35LinkMode": lpV35LinkMode,
       "lpV35ReadyLineState": lpV35ReadyLineState,
       "lpV35DataTransferLineState": lpV35DataTransferLineState,
       "lpV35LineStatusTimeOut": lpV35LineStatusTimeOut,
       "lpV35LineSpeed": lpV35LineSpeed,
       "lpV35ClockingSource": lpV35ClockingSource,
       "lpV35DteDataClockSource": lpV35DteDataClockSource,
       "lpV35ApplicationFramerName": lpV35ApplicationFramerName,
       "lpV35EnableDynamicSpeed": lpV35EnableDynamicSpeed,
       "lpV35CidDataTable": lpV35CidDataTable,
       "lpV35CidDataEntry": lpV35CidDataEntry,
       "lpV35CustomerIdentifier": lpV35CustomerIdentifier,
       "lpV35AdminInfoTable": lpV35AdminInfoTable,
       "lpV35AdminInfoEntry": lpV35AdminInfoEntry,
       "lpV35Vendor": lpV35Vendor,
       "lpV35CommentText": lpV35CommentText,
       "lpV35IfEntryTable": lpV35IfEntryTable,
       "lpV35IfEntryEntry": lpV35IfEntryEntry,
       "lpV35IfAdminStatus": lpV35IfAdminStatus,
       "lpV35IfIndex": lpV35IfIndex,
       "lpV35OperStatusTable": lpV35OperStatusTable,
       "lpV35OperStatusEntry": lpV35OperStatusEntry,
       "lpV35SnmpOperStatus": lpV35SnmpOperStatus,
       "lpV35StateTable": lpV35StateTable,
       "lpV35StateEntry": lpV35StateEntry,
       "lpV35AdminState": lpV35AdminState,
       "lpV35OperationalState": lpV35OperationalState,
       "lpV35UsageState": lpV35UsageState,
       "lpV35AvailabilityStatus": lpV35AvailabilityStatus,
       "lpV35ProceduralStatus": lpV35ProceduralStatus,
       "lpV35ControlStatus": lpV35ControlStatus,
       "lpV35AlarmStatus": lpV35AlarmStatus,
       "lpV35StandbyStatus": lpV35StandbyStatus,
       "lpV35UnknownStatus": lpV35UnknownStatus,
       "lpV35OperTable": lpV35OperTable,
       "lpV35OperEntry": lpV35OperEntry,
       "lpV35ActualLinkMode": lpV35ActualLinkMode,
       "lpV35LineState": lpV35LineState,
       "lpV35ActualTxLineSpeed": lpV35ActualTxLineSpeed,
       "lpV35ActualRxLineSpeed": lpV35ActualRxLineSpeed,
       "lpV35DataXferStateChanges": lpV35DataXferStateChanges,
       "lpX21": lpX21,
       "lpX21RowStatusTable": lpX21RowStatusTable,
       "lpX21RowStatusEntry": lpX21RowStatusEntry,
       "lpX21RowStatus": lpX21RowStatus,
       "lpX21ComponentName": lpX21ComponentName,
       "lpX21StorageType": lpX21StorageType,
       "lpX21Index": lpX21Index,
       "lpX21Test": lpX21Test,
       "lpX21TestRowStatusTable": lpX21TestRowStatusTable,
       "lpX21TestRowStatusEntry": lpX21TestRowStatusEntry,
       "lpX21TestRowStatus": lpX21TestRowStatus,
       "lpX21TestComponentName": lpX21TestComponentName,
       "lpX21TestStorageType": lpX21TestStorageType,
       "lpX21TestIndex": lpX21TestIndex,
       "lpX21TestStateTable": lpX21TestStateTable,
       "lpX21TestStateEntry": lpX21TestStateEntry,
       "lpX21TestAdminState": lpX21TestAdminState,
       "lpX21TestOperationalState": lpX21TestOperationalState,
       "lpX21TestUsageState": lpX21TestUsageState,
       "lpX21TestSetupTable": lpX21TestSetupTable,
       "lpX21TestSetupEntry": lpX21TestSetupEntry,
       "lpX21TestPurpose": lpX21TestPurpose,
       "lpX21TestType": lpX21TestType,
       "lpX21TestFrmSize": lpX21TestFrmSize,
       "lpX21TestFrmPatternType": lpX21TestFrmPatternType,
       "lpX21TestCustomizedPattern": lpX21TestCustomizedPattern,
       "lpX21TestDataStartDelay": lpX21TestDataStartDelay,
       "lpX21TestDisplayInterval": lpX21TestDisplayInterval,
       "lpX21TestDuration": lpX21TestDuration,
       "lpX21TestResultsTable": lpX21TestResultsTable,
       "lpX21TestResultsEntry": lpX21TestResultsEntry,
       "lpX21TestElapsedTime": lpX21TestElapsedTime,
       "lpX21TestTimeRemaining": lpX21TestTimeRemaining,
       "lpX21TestCauseOfTermination": lpX21TestCauseOfTermination,
       "lpX21TestBitsTx": lpX21TestBitsTx,
       "lpX21TestBytesTx": lpX21TestBytesTx,
       "lpX21TestFrmTx": lpX21TestFrmTx,
       "lpX21TestBitsRx": lpX21TestBitsRx,
       "lpX21TestBytesRx": lpX21TestBytesRx,
       "lpX21TestFrmRx": lpX21TestFrmRx,
       "lpX21TestErroredFrmRx": lpX21TestErroredFrmRx,
       "lpX21TestBitErrorRate": lpX21TestBitErrorRate,
       "lpX21ProvTable": lpX21ProvTable,
       "lpX21ProvEntry": lpX21ProvEntry,
       "lpX21LinkMode": lpX21LinkMode,
       "lpX21ReadyLineState": lpX21ReadyLineState,
       "lpX21DataTransferLineState": lpX21DataTransferLineState,
       "lpX21LineStatusTimeOut": lpX21LineStatusTimeOut,
       "lpX21LineSpeed": lpX21LineSpeed,
       "lpX21ClockingSource": lpX21ClockingSource,
       "lpX21DteDataClockSource": lpX21DteDataClockSource,
       "lpX21LineTerminationRequired": lpX21LineTerminationRequired,
       "lpX21ApplicationFramerName": lpX21ApplicationFramerName,
       "lpX21EnableDynamicSpeed": lpX21EnableDynamicSpeed,
       "lpX21CidDataTable": lpX21CidDataTable,
       "lpX21CidDataEntry": lpX21CidDataEntry,
       "lpX21CustomerIdentifier": lpX21CustomerIdentifier,
       "lpX21AdminInfoTable": lpX21AdminInfoTable,
       "lpX21AdminInfoEntry": lpX21AdminInfoEntry,
       "lpX21Vendor": lpX21Vendor,
       "lpX21CommentText": lpX21CommentText,
       "lpX21IfEntryTable": lpX21IfEntryTable,
       "lpX21IfEntryEntry": lpX21IfEntryEntry,
       "lpX21IfAdminStatus": lpX21IfAdminStatus,
       "lpX21IfIndex": lpX21IfIndex,
       "lpX21OperStatusTable": lpX21OperStatusTable,
       "lpX21OperStatusEntry": lpX21OperStatusEntry,
       "lpX21SnmpOperStatus": lpX21SnmpOperStatus,
       "lpX21StateTable": lpX21StateTable,
       "lpX21StateEntry": lpX21StateEntry,
       "lpX21AdminState": lpX21AdminState,
       "lpX21OperationalState": lpX21OperationalState,
       "lpX21UsageState": lpX21UsageState,
       "lpX21AvailabilityStatus": lpX21AvailabilityStatus,
       "lpX21ProceduralStatus": lpX21ProceduralStatus,
       "lpX21ControlStatus": lpX21ControlStatus,
       "lpX21AlarmStatus": lpX21AlarmStatus,
       "lpX21StandbyStatus": lpX21StandbyStatus,
       "lpX21UnknownStatus": lpX21UnknownStatus,
       "lpX21OperTable": lpX21OperTable,
       "lpX21OperEntry": lpX21OperEntry,
       "lpX21ActualLinkMode": lpX21ActualLinkMode,
       "lpX21LineState": lpX21LineState,
       "lpX21ActualTxLineSpeed": lpX21ActualTxLineSpeed,
       "lpX21ActualRxLineSpeed": lpX21ActualRxLineSpeed,
       "lpX21DataXferStateChanges": lpX21DataXferStateChanges,
       "lpSonet": lpSonet,
       "lpSonetRowStatusTable": lpSonetRowStatusTable,
       "lpSonetRowStatusEntry": lpSonetRowStatusEntry,
       "lpSonetRowStatus": lpSonetRowStatus,
       "lpSonetComponentName": lpSonetComponentName,
       "lpSonetStorageType": lpSonetStorageType,
       "lpSonetIndex": lpSonetIndex,
       "lpSonetPath": lpSonetPath,
       "lpSonetPathRowStatusTable": lpSonetPathRowStatusTable,
       "lpSonetPathRowStatusEntry": lpSonetPathRowStatusEntry,
       "lpSonetPathRowStatus": lpSonetPathRowStatus,
       "lpSonetPathComponentName": lpSonetPathComponentName,
       "lpSonetPathStorageType": lpSonetPathStorageType,
       "lpSonetPathIndex": lpSonetPathIndex,
       "lpSonetPathCell": lpSonetPathCell,
       "lpSonetPathCellRowStatusTable": lpSonetPathCellRowStatusTable,
       "lpSonetPathCellRowStatusEntry": lpSonetPathCellRowStatusEntry,
       "lpSonetPathCellRowStatus": lpSonetPathCellRowStatus,
       "lpSonetPathCellComponentName": lpSonetPathCellComponentName,
       "lpSonetPathCellStorageType": lpSonetPathCellStorageType,
       "lpSonetPathCellIndex": lpSonetPathCellIndex,
       "lpSonetPathCellProvTable": lpSonetPathCellProvTable,
       "lpSonetPathCellProvEntry": lpSonetPathCellProvEntry,
       "lpSonetPathCellAlarmActDelay": lpSonetPathCellAlarmActDelay,
       "lpSonetPathCellScrambleCellPayload": lpSonetPathCellScrambleCellPayload,
       "lpSonetPathCellCorrectSingleBitHeaderErrors": lpSonetPathCellCorrectSingleBitHeaderErrors,
       "lpSonetPathCellOperTable": lpSonetPathCellOperTable,
       "lpSonetPathCellOperEntry": lpSonetPathCellOperEntry,
       "lpSonetPathCellLcdAlarm": lpSonetPathCellLcdAlarm,
       "lpSonetPathCellStatsTable": lpSonetPathCellStatsTable,
       "lpSonetPathCellStatsEntry": lpSonetPathCellStatsEntry,
       "lpSonetPathCellUncorrectableHecErrors": lpSonetPathCellUncorrectableHecErrors,
       "lpSonetPathCellSevErroredSec": lpSonetPathCellSevErroredSec,
       "lpSonetPathCellReceiveCellUtilization": lpSonetPathCellReceiveCellUtilization,
       "lpSonetPathCellTransmitCellUtilization": lpSonetPathCellTransmitCellUtilization,
       "lpSonetPathCellCorrectableHeaderErrors": lpSonetPathCellCorrectableHeaderErrors,
       "lpSonetPathProvTable": lpSonetPathProvTable,
       "lpSonetPathProvEntry": lpSonetPathProvEntry,
       "lpSonetPathApplicationFramerName": lpSonetPathApplicationFramerName,
       "lpSonetPathCidDataTable": lpSonetPathCidDataTable,
       "lpSonetPathCidDataEntry": lpSonetPathCidDataEntry,
       "lpSonetPathCustomerIdentifier": lpSonetPathCustomerIdentifier,
       "lpSonetPathStateTable": lpSonetPathStateTable,
       "lpSonetPathStateEntry": lpSonetPathStateEntry,
       "lpSonetPathAdminState": lpSonetPathAdminState,
       "lpSonetPathOperationalState": lpSonetPathOperationalState,
       "lpSonetPathUsageState": lpSonetPathUsageState,
       "lpSonetPathAvailabilityStatus": lpSonetPathAvailabilityStatus,
       "lpSonetPathProceduralStatus": lpSonetPathProceduralStatus,
       "lpSonetPathControlStatus": lpSonetPathControlStatus,
       "lpSonetPathAlarmStatus": lpSonetPathAlarmStatus,
       "lpSonetPathStandbyStatus": lpSonetPathStandbyStatus,
       "lpSonetPathUnknownStatus": lpSonetPathUnknownStatus,
       "lpSonetPathIfEntryTable": lpSonetPathIfEntryTable,
       "lpSonetPathIfEntryEntry": lpSonetPathIfEntryEntry,
       "lpSonetPathIfAdminStatus": lpSonetPathIfAdminStatus,
       "lpSonetPathIfIndex": lpSonetPathIfIndex,
       "lpSonetPathOperStatusTable": lpSonetPathOperStatusTable,
       "lpSonetPathOperStatusEntry": lpSonetPathOperStatusEntry,
       "lpSonetPathSnmpOperStatus": lpSonetPathSnmpOperStatus,
       "lpSonetPathOperTable": lpSonetPathOperTable,
       "lpSonetPathOperEntry": lpSonetPathOperEntry,
       "lpSonetPathLopAlarm": lpSonetPathLopAlarm,
       "lpSonetPathRxAisAlarm": lpSonetPathRxAisAlarm,
       "lpSonetPathRxRfiAlarm": lpSonetPathRxRfiAlarm,
       "lpSonetPathSignalLabelMismatch": lpSonetPathSignalLabelMismatch,
       "lpSonetPathTxAis": lpSonetPathTxAis,
       "lpSonetPathTxRdi": lpSonetPathTxRdi,
       "lpSonetPathStatsTable": lpSonetPathStatsTable,
       "lpSonetPathStatsEntry": lpSonetPathStatsEntry,
       "lpSonetPathPathErrorFreeSec": lpSonetPathPathErrorFreeSec,
       "lpSonetPathPathCodeViolations": lpSonetPathPathCodeViolations,
       "lpSonetPathPathErroredSec": lpSonetPathPathErroredSec,
       "lpSonetPathPathSevErroredSec": lpSonetPathPathSevErroredSec,
       "lpSonetPathPathAisLopSec": lpSonetPathPathAisLopSec,
       "lpSonetPathPathUnavailSec": lpSonetPathPathUnavailSec,
       "lpSonetPathPathFailures": lpSonetPathPathFailures,
       "lpSonetPathFarEndPathErrorFreeSec": lpSonetPathFarEndPathErrorFreeSec,
       "lpSonetPathFarEndPathCodeViolations": lpSonetPathFarEndPathCodeViolations,
       "lpSonetPathFarEndPathErroredSec": lpSonetPathFarEndPathErroredSec,
       "lpSonetPathFarEndPathSevErroredSec": lpSonetPathFarEndPathSevErroredSec,
       "lpSonetPathFarEndPathAisLopSec": lpSonetPathFarEndPathAisLopSec,
       "lpSonetPathFarEndPathUnavailSec": lpSonetPathFarEndPathUnavailSec,
       "lpSonetPathFarEndPathFailures": lpSonetPathFarEndPathFailures,
       "lpSonetTest": lpSonetTest,
       "lpSonetTestRowStatusTable": lpSonetTestRowStatusTable,
       "lpSonetTestRowStatusEntry": lpSonetTestRowStatusEntry,
       "lpSonetTestRowStatus": lpSonetTestRowStatus,
       "lpSonetTestComponentName": lpSonetTestComponentName,
       "lpSonetTestStorageType": lpSonetTestStorageType,
       "lpSonetTestIndex": lpSonetTestIndex,
       "lpSonetTestStateTable": lpSonetTestStateTable,
       "lpSonetTestStateEntry": lpSonetTestStateEntry,
       "lpSonetTestAdminState": lpSonetTestAdminState,
       "lpSonetTestOperationalState": lpSonetTestOperationalState,
       "lpSonetTestUsageState": lpSonetTestUsageState,
       "lpSonetTestSetupTable": lpSonetTestSetupTable,
       "lpSonetTestSetupEntry": lpSonetTestSetupEntry,
       "lpSonetTestPurpose": lpSonetTestPurpose,
       "lpSonetTestType": lpSonetTestType,
       "lpSonetTestFrmSize": lpSonetTestFrmSize,
       "lpSonetTestFrmPatternType": lpSonetTestFrmPatternType,
       "lpSonetTestCustomizedPattern": lpSonetTestCustomizedPattern,
       "lpSonetTestDataStartDelay": lpSonetTestDataStartDelay,
       "lpSonetTestDisplayInterval": lpSonetTestDisplayInterval,
       "lpSonetTestDuration": lpSonetTestDuration,
       "lpSonetTestResultsTable": lpSonetTestResultsTable,
       "lpSonetTestResultsEntry": lpSonetTestResultsEntry,
       "lpSonetTestElapsedTime": lpSonetTestElapsedTime,
       "lpSonetTestTimeRemaining": lpSonetTestTimeRemaining,
       "lpSonetTestCauseOfTermination": lpSonetTestCauseOfTermination,
       "lpSonetTestBitsTx": lpSonetTestBitsTx,
       "lpSonetTestBytesTx": lpSonetTestBytesTx,
       "lpSonetTestFrmTx": lpSonetTestFrmTx,
       "lpSonetTestBitsRx": lpSonetTestBitsRx,
       "lpSonetTestBytesRx": lpSonetTestBytesRx,
       "lpSonetTestFrmRx": lpSonetTestFrmRx,
       "lpSonetTestErroredFrmRx": lpSonetTestErroredFrmRx,
       "lpSonetTestBitErrorRate": lpSonetTestBitErrorRate,
       "lpSonetProvTable": lpSonetProvTable,
       "lpSonetProvEntry": lpSonetProvEntry,
       "lpSonetClockingSource": lpSonetClockingSource,
       "lpSonetCidDataTable": lpSonetCidDataTable,
       "lpSonetCidDataEntry": lpSonetCidDataEntry,
       "lpSonetCustomerIdentifier": lpSonetCustomerIdentifier,
       "lpSonetAdminInfoTable": lpSonetAdminInfoTable,
       "lpSonetAdminInfoEntry": lpSonetAdminInfoEntry,
       "lpSonetVendor": lpSonetVendor,
       "lpSonetCommentText": lpSonetCommentText,
       "lpSonetIfEntryTable": lpSonetIfEntryTable,
       "lpSonetIfEntryEntry": lpSonetIfEntryEntry,
       "lpSonetIfAdminStatus": lpSonetIfAdminStatus,
       "lpSonetIfIndex": lpSonetIfIndex,
       "lpSonetOperStatusTable": lpSonetOperStatusTable,
       "lpSonetOperStatusEntry": lpSonetOperStatusEntry,
       "lpSonetSnmpOperStatus": lpSonetSnmpOperStatus,
       "lpSonetStateTable": lpSonetStateTable,
       "lpSonetStateEntry": lpSonetStateEntry,
       "lpSonetAdminState": lpSonetAdminState,
       "lpSonetOperationalState": lpSonetOperationalState,
       "lpSonetUsageState": lpSonetUsageState,
       "lpSonetAvailabilityStatus": lpSonetAvailabilityStatus,
       "lpSonetProceduralStatus": lpSonetProceduralStatus,
       "lpSonetControlStatus": lpSonetControlStatus,
       "lpSonetAlarmStatus": lpSonetAlarmStatus,
       "lpSonetStandbyStatus": lpSonetStandbyStatus,
       "lpSonetUnknownStatus": lpSonetUnknownStatus,
       "lpSonetOperTable": lpSonetOperTable,
       "lpSonetOperEntry": lpSonetOperEntry,
       "lpSonetLosAlarm": lpSonetLosAlarm,
       "lpSonetLofAlarm": lpSonetLofAlarm,
       "lpSonetRxAisAlarm": lpSonetRxAisAlarm,
       "lpSonetRxRfiAlarm": lpSonetRxRfiAlarm,
       "lpSonetTxAis": lpSonetTxAis,
       "lpSonetTxRdi": lpSonetTxRdi,
       "lpSonetUnusableTxClockRefAlarm": lpSonetUnusableTxClockRefAlarm,
       "lpSonetStatsTable": lpSonetStatsTable,
       "lpSonetStatsEntry": lpSonetStatsEntry,
       "lpSonetRunningTime": lpSonetRunningTime,
       "lpSonetErrorFreeSec": lpSonetErrorFreeSec,
       "lpSonetSectCodeViolations": lpSonetSectCodeViolations,
       "lpSonetSectErroredSec": lpSonetSectErroredSec,
       "lpSonetSectSevErroredSec": lpSonetSectSevErroredSec,
       "lpSonetSectLosSec": lpSonetSectLosSec,
       "lpSonetSectSevErroredFrmSec": lpSonetSectSevErroredFrmSec,
       "lpSonetSectFailures": lpSonetSectFailures,
       "lpSonetLineCodeViolations": lpSonetLineCodeViolations,
       "lpSonetLineErroredSec": lpSonetLineErroredSec,
       "lpSonetLineSevErroredSec": lpSonetLineSevErroredSec,
       "lpSonetLineAisSec": lpSonetLineAisSec,
       "lpSonetLineUnavailSec": lpSonetLineUnavailSec,
       "lpSonetLineFailures": lpSonetLineFailures,
       "lpSonetFarEndLineErrorFreeSec": lpSonetFarEndLineErrorFreeSec,
       "lpSonetFarEndLineCodeViolations": lpSonetFarEndLineCodeViolations,
       "lpSonetFarEndLineErroredSec": lpSonetFarEndLineErroredSec,
       "lpSonetFarEndLineSevErroredSec": lpSonetFarEndLineSevErroredSec,
       "lpSonetFarEndLineAisSec": lpSonetFarEndLineAisSec,
       "lpSonetFarEndLineUnavailSec": lpSonetFarEndLineUnavailSec,
       "lpSonetFarEndLineFailures": lpSonetFarEndLineFailures,
       "lpSdh": lpSdh,
       "lpSdhRowStatusTable": lpSdhRowStatusTable,
       "lpSdhRowStatusEntry": lpSdhRowStatusEntry,
       "lpSdhRowStatus": lpSdhRowStatus,
       "lpSdhComponentName": lpSdhComponentName,
       "lpSdhStorageType": lpSdhStorageType,
       "lpSdhIndex": lpSdhIndex,
       "lpSdhPath": lpSdhPath,
       "lpSdhPathRowStatusTable": lpSdhPathRowStatusTable,
       "lpSdhPathRowStatusEntry": lpSdhPathRowStatusEntry,
       "lpSdhPathRowStatus": lpSdhPathRowStatus,
       "lpSdhPathComponentName": lpSdhPathComponentName,
       "lpSdhPathStorageType": lpSdhPathStorageType,
       "lpSdhPathIndex": lpSdhPathIndex,
       "lpSdhPathCell": lpSdhPathCell,
       "lpSdhPathCellRowStatusTable": lpSdhPathCellRowStatusTable,
       "lpSdhPathCellRowStatusEntry": lpSdhPathCellRowStatusEntry,
       "lpSdhPathCellRowStatus": lpSdhPathCellRowStatus,
       "lpSdhPathCellComponentName": lpSdhPathCellComponentName,
       "lpSdhPathCellStorageType": lpSdhPathCellStorageType,
       "lpSdhPathCellIndex": lpSdhPathCellIndex,
       "lpSdhPathCellProvTable": lpSdhPathCellProvTable,
       "lpSdhPathCellProvEntry": lpSdhPathCellProvEntry,
       "lpSdhPathCellAlarmActDelay": lpSdhPathCellAlarmActDelay,
       "lpSdhPathCellScrambleCellPayload": lpSdhPathCellScrambleCellPayload,
       "lpSdhPathCellCorrectSingleBitHeaderErrors": lpSdhPathCellCorrectSingleBitHeaderErrors,
       "lpSdhPathCellOperTable": lpSdhPathCellOperTable,
       "lpSdhPathCellOperEntry": lpSdhPathCellOperEntry,
       "lpSdhPathCellLcdAlarm": lpSdhPathCellLcdAlarm,
       "lpSdhPathCellStatsTable": lpSdhPathCellStatsTable,
       "lpSdhPathCellStatsEntry": lpSdhPathCellStatsEntry,
       "lpSdhPathCellUncorrectableHecErrors": lpSdhPathCellUncorrectableHecErrors,
       "lpSdhPathCellSevErroredSec": lpSdhPathCellSevErroredSec,
       "lpSdhPathCellReceiveCellUtilization": lpSdhPathCellReceiveCellUtilization,
       "lpSdhPathCellTransmitCellUtilization": lpSdhPathCellTransmitCellUtilization,
       "lpSdhPathCellCorrectableHeaderErrors": lpSdhPathCellCorrectableHeaderErrors,
       "lpSdhPathProvTable": lpSdhPathProvTable,
       "lpSdhPathProvEntry": lpSdhPathProvEntry,
       "lpSdhPathApplicationFramerName": lpSdhPathApplicationFramerName,
       "lpSdhPathCidDataTable": lpSdhPathCidDataTable,
       "lpSdhPathCidDataEntry": lpSdhPathCidDataEntry,
       "lpSdhPathCustomerIdentifier": lpSdhPathCustomerIdentifier,
       "lpSdhPathStateTable": lpSdhPathStateTable,
       "lpSdhPathStateEntry": lpSdhPathStateEntry,
       "lpSdhPathAdminState": lpSdhPathAdminState,
       "lpSdhPathOperationalState": lpSdhPathOperationalState,
       "lpSdhPathUsageState": lpSdhPathUsageState,
       "lpSdhPathAvailabilityStatus": lpSdhPathAvailabilityStatus,
       "lpSdhPathProceduralStatus": lpSdhPathProceduralStatus,
       "lpSdhPathControlStatus": lpSdhPathControlStatus,
       "lpSdhPathAlarmStatus": lpSdhPathAlarmStatus,
       "lpSdhPathStandbyStatus": lpSdhPathStandbyStatus,
       "lpSdhPathUnknownStatus": lpSdhPathUnknownStatus,
       "lpSdhPathIfEntryTable": lpSdhPathIfEntryTable,
       "lpSdhPathIfEntryEntry": lpSdhPathIfEntryEntry,
       "lpSdhPathIfAdminStatus": lpSdhPathIfAdminStatus,
       "lpSdhPathIfIndex": lpSdhPathIfIndex,
       "lpSdhPathOperStatusTable": lpSdhPathOperStatusTable,
       "lpSdhPathOperStatusEntry": lpSdhPathOperStatusEntry,
       "lpSdhPathSnmpOperStatus": lpSdhPathSnmpOperStatus,
       "lpSdhPathOperTable": lpSdhPathOperTable,
       "lpSdhPathOperEntry": lpSdhPathOperEntry,
       "lpSdhPathLopAlarm": lpSdhPathLopAlarm,
       "lpSdhPathRxAisAlarm": lpSdhPathRxAisAlarm,
       "lpSdhPathRxRfiAlarm": lpSdhPathRxRfiAlarm,
       "lpSdhPathSignalLabelMismatch": lpSdhPathSignalLabelMismatch,
       "lpSdhPathTxAis": lpSdhPathTxAis,
       "lpSdhPathTxRdi": lpSdhPathTxRdi,
       "lpSdhPathStatsTable": lpSdhPathStatsTable,
       "lpSdhPathStatsEntry": lpSdhPathStatsEntry,
       "lpSdhPathPathErrorFreeSec": lpSdhPathPathErrorFreeSec,
       "lpSdhPathPathCodeViolations": lpSdhPathPathCodeViolations,
       "lpSdhPathPathErroredSec": lpSdhPathPathErroredSec,
       "lpSdhPathPathSevErroredSec": lpSdhPathPathSevErroredSec,
       "lpSdhPathPathAisLopSec": lpSdhPathPathAisLopSec,
       "lpSdhPathPathUnavailSec": lpSdhPathPathUnavailSec,
       "lpSdhPathPathFailures": lpSdhPathPathFailures,
       "lpSdhPathFarEndPathErrorFreeSec": lpSdhPathFarEndPathErrorFreeSec,
       "lpSdhPathFarEndPathCodeViolations": lpSdhPathFarEndPathCodeViolations,
       "lpSdhPathFarEndPathErroredSec": lpSdhPathFarEndPathErroredSec,
       "lpSdhPathFarEndPathSevErroredSec": lpSdhPathFarEndPathSevErroredSec,
       "lpSdhPathFarEndPathAisLopSec": lpSdhPathFarEndPathAisLopSec,
       "lpSdhPathFarEndPathUnavailSec": lpSdhPathFarEndPathUnavailSec,
       "lpSdhPathFarEndPathFailures": lpSdhPathFarEndPathFailures,
       "lpSdhTest": lpSdhTest,
       "lpSdhTestRowStatusTable": lpSdhTestRowStatusTable,
       "lpSdhTestRowStatusEntry": lpSdhTestRowStatusEntry,
       "lpSdhTestRowStatus": lpSdhTestRowStatus,
       "lpSdhTestComponentName": lpSdhTestComponentName,
       "lpSdhTestStorageType": lpSdhTestStorageType,
       "lpSdhTestIndex": lpSdhTestIndex,
       "lpSdhTestStateTable": lpSdhTestStateTable,
       "lpSdhTestStateEntry": lpSdhTestStateEntry,
       "lpSdhTestAdminState": lpSdhTestAdminState,
       "lpSdhTestOperationalState": lpSdhTestOperationalState,
       "lpSdhTestUsageState": lpSdhTestUsageState,
       "lpSdhTestSetupTable": lpSdhTestSetupTable,
       "lpSdhTestSetupEntry": lpSdhTestSetupEntry,
       "lpSdhTestPurpose": lpSdhTestPurpose,
       "lpSdhTestType": lpSdhTestType,
       "lpSdhTestFrmSize": lpSdhTestFrmSize,
       "lpSdhTestFrmPatternType": lpSdhTestFrmPatternType,
       "lpSdhTestCustomizedPattern": lpSdhTestCustomizedPattern,
       "lpSdhTestDataStartDelay": lpSdhTestDataStartDelay,
       "lpSdhTestDisplayInterval": lpSdhTestDisplayInterval,
       "lpSdhTestDuration": lpSdhTestDuration,
       "lpSdhTestResultsTable": lpSdhTestResultsTable,
       "lpSdhTestResultsEntry": lpSdhTestResultsEntry,
       "lpSdhTestElapsedTime": lpSdhTestElapsedTime,
       "lpSdhTestTimeRemaining": lpSdhTestTimeRemaining,
       "lpSdhTestCauseOfTermination": lpSdhTestCauseOfTermination,
       "lpSdhTestBitsTx": lpSdhTestBitsTx,
       "lpSdhTestBytesTx": lpSdhTestBytesTx,
       "lpSdhTestFrmTx": lpSdhTestFrmTx,
       "lpSdhTestBitsRx": lpSdhTestBitsRx,
       "lpSdhTestBytesRx": lpSdhTestBytesRx,
       "lpSdhTestFrmRx": lpSdhTestFrmRx,
       "lpSdhTestErroredFrmRx": lpSdhTestErroredFrmRx,
       "lpSdhTestBitErrorRate": lpSdhTestBitErrorRate,
       "lpSdhProvTable": lpSdhProvTable,
       "lpSdhProvEntry": lpSdhProvEntry,
       "lpSdhClockingSource": lpSdhClockingSource,
       "lpSdhCidDataTable": lpSdhCidDataTable,
       "lpSdhCidDataEntry": lpSdhCidDataEntry,
       "lpSdhCustomerIdentifier": lpSdhCustomerIdentifier,
       "lpSdhAdminInfoTable": lpSdhAdminInfoTable,
       "lpSdhAdminInfoEntry": lpSdhAdminInfoEntry,
       "lpSdhVendor": lpSdhVendor,
       "lpSdhCommentText": lpSdhCommentText,
       "lpSdhIfEntryTable": lpSdhIfEntryTable,
       "lpSdhIfEntryEntry": lpSdhIfEntryEntry,
       "lpSdhIfAdminStatus": lpSdhIfAdminStatus,
       "lpSdhIfIndex": lpSdhIfIndex,
       "lpSdhOperStatusTable": lpSdhOperStatusTable,
       "lpSdhOperStatusEntry": lpSdhOperStatusEntry,
       "lpSdhSnmpOperStatus": lpSdhSnmpOperStatus,
       "lpSdhStateTable": lpSdhStateTable,
       "lpSdhStateEntry": lpSdhStateEntry,
       "lpSdhAdminState": lpSdhAdminState,
       "lpSdhOperationalState": lpSdhOperationalState,
       "lpSdhUsageState": lpSdhUsageState,
       "lpSdhAvailabilityStatus": lpSdhAvailabilityStatus,
       "lpSdhProceduralStatus": lpSdhProceduralStatus,
       "lpSdhControlStatus": lpSdhControlStatus,
       "lpSdhAlarmStatus": lpSdhAlarmStatus,
       "lpSdhStandbyStatus": lpSdhStandbyStatus,
       "lpSdhUnknownStatus": lpSdhUnknownStatus,
       "lpSdhOperTable": lpSdhOperTable,
       "lpSdhOperEntry": lpSdhOperEntry,
       "lpSdhLosAlarm": lpSdhLosAlarm,
       "lpSdhLofAlarm": lpSdhLofAlarm,
       "lpSdhRxAisAlarm": lpSdhRxAisAlarm,
       "lpSdhRxRfiAlarm": lpSdhRxRfiAlarm,
       "lpSdhTxAis": lpSdhTxAis,
       "lpSdhTxRdi": lpSdhTxRdi,
       "lpSdhUnusableTxClockRefAlarm": lpSdhUnusableTxClockRefAlarm,
       "lpSdhStatsTable": lpSdhStatsTable,
       "lpSdhStatsEntry": lpSdhStatsEntry,
       "lpSdhRunningTime": lpSdhRunningTime,
       "lpSdhErrorFreeSec": lpSdhErrorFreeSec,
       "lpSdhSectCodeViolations": lpSdhSectCodeViolations,
       "lpSdhSectErroredSec": lpSdhSectErroredSec,
       "lpSdhSectSevErroredSec": lpSdhSectSevErroredSec,
       "lpSdhSectLosSec": lpSdhSectLosSec,
       "lpSdhSectSevErroredFrmSec": lpSdhSectSevErroredFrmSec,
       "lpSdhSectFailures": lpSdhSectFailures,
       "lpSdhLineCodeViolations": lpSdhLineCodeViolations,
       "lpSdhLineErroredSec": lpSdhLineErroredSec,
       "lpSdhLineSevErroredSec": lpSdhLineSevErroredSec,
       "lpSdhLineAisSec": lpSdhLineAisSec,
       "lpSdhLineUnavailSec": lpSdhLineUnavailSec,
       "lpSdhLineFailures": lpSdhLineFailures,
       "lpSdhFarEndLineErrorFreeSec": lpSdhFarEndLineErrorFreeSec,
       "lpSdhFarEndLineCodeViolations": lpSdhFarEndLineCodeViolations,
       "lpSdhFarEndLineErroredSec": lpSdhFarEndLineErroredSec,
       "lpSdhFarEndLineSevErroredSec": lpSdhFarEndLineSevErroredSec,
       "lpSdhFarEndLineAisSec": lpSdhFarEndLineAisSec,
       "lpSdhFarEndLineUnavailSec": lpSdhFarEndLineUnavailSec,
       "lpSdhFarEndLineFailures": lpSdhFarEndLineFailures,
       "lpJT2": lpJT2,
       "lpJT2RowStatusTable": lpJT2RowStatusTable,
       "lpJT2RowStatusEntry": lpJT2RowStatusEntry,
       "lpJT2RowStatus": lpJT2RowStatus,
       "lpJT2ComponentName": lpJT2ComponentName,
       "lpJT2StorageType": lpJT2StorageType,
       "lpJT2Index": lpJT2Index,
       "lpJT2Test": lpJT2Test,
       "lpJT2TestRowStatusTable": lpJT2TestRowStatusTable,
       "lpJT2TestRowStatusEntry": lpJT2TestRowStatusEntry,
       "lpJT2TestRowStatus": lpJT2TestRowStatus,
       "lpJT2TestComponentName": lpJT2TestComponentName,
       "lpJT2TestStorageType": lpJT2TestStorageType,
       "lpJT2TestIndex": lpJT2TestIndex,
       "lpJT2TestStateTable": lpJT2TestStateTable,
       "lpJT2TestStateEntry": lpJT2TestStateEntry,
       "lpJT2TestAdminState": lpJT2TestAdminState,
       "lpJT2TestOperationalState": lpJT2TestOperationalState,
       "lpJT2TestUsageState": lpJT2TestUsageState,
       "lpJT2TestSetupTable": lpJT2TestSetupTable,
       "lpJT2TestSetupEntry": lpJT2TestSetupEntry,
       "lpJT2TestPurpose": lpJT2TestPurpose,
       "lpJT2TestType": lpJT2TestType,
       "lpJT2TestFrmSize": lpJT2TestFrmSize,
       "lpJT2TestFrmPatternType": lpJT2TestFrmPatternType,
       "lpJT2TestCustomizedPattern": lpJT2TestCustomizedPattern,
       "lpJT2TestDataStartDelay": lpJT2TestDataStartDelay,
       "lpJT2TestDisplayInterval": lpJT2TestDisplayInterval,
       "lpJT2TestDuration": lpJT2TestDuration,
       "lpJT2TestResultsTable": lpJT2TestResultsTable,
       "lpJT2TestResultsEntry": lpJT2TestResultsEntry,
       "lpJT2TestElapsedTime": lpJT2TestElapsedTime,
       "lpJT2TestTimeRemaining": lpJT2TestTimeRemaining,
       "lpJT2TestCauseOfTermination": lpJT2TestCauseOfTermination,
       "lpJT2TestBitsTx": lpJT2TestBitsTx,
       "lpJT2TestBytesTx": lpJT2TestBytesTx,
       "lpJT2TestFrmTx": lpJT2TestFrmTx,
       "lpJT2TestBitsRx": lpJT2TestBitsRx,
       "lpJT2TestBytesRx": lpJT2TestBytesRx,
       "lpJT2TestFrmRx": lpJT2TestFrmRx,
       "lpJT2TestErroredFrmRx": lpJT2TestErroredFrmRx,
       "lpJT2TestBitErrorRate": lpJT2TestBitErrorRate,
       "lpJT2Cell": lpJT2Cell,
       "lpJT2CellRowStatusTable": lpJT2CellRowStatusTable,
       "lpJT2CellRowStatusEntry": lpJT2CellRowStatusEntry,
       "lpJT2CellRowStatus": lpJT2CellRowStatus,
       "lpJT2CellComponentName": lpJT2CellComponentName,
       "lpJT2CellStorageType": lpJT2CellStorageType,
       "lpJT2CellIndex": lpJT2CellIndex,
       "lpJT2CellProvTable": lpJT2CellProvTable,
       "lpJT2CellProvEntry": lpJT2CellProvEntry,
       "lpJT2CellAlarmActDelay": lpJT2CellAlarmActDelay,
       "lpJT2CellScrambleCellPayload": lpJT2CellScrambleCellPayload,
       "lpJT2CellCorrectSingleBitHeaderErrors": lpJT2CellCorrectSingleBitHeaderErrors,
       "lpJT2CellOperTable": lpJT2CellOperTable,
       "lpJT2CellOperEntry": lpJT2CellOperEntry,
       "lpJT2CellLcdAlarm": lpJT2CellLcdAlarm,
       "lpJT2CellStatsTable": lpJT2CellStatsTable,
       "lpJT2CellStatsEntry": lpJT2CellStatsEntry,
       "lpJT2CellUncorrectableHecErrors": lpJT2CellUncorrectableHecErrors,
       "lpJT2CellSevErroredSec": lpJT2CellSevErroredSec,
       "lpJT2CellReceiveCellUtilization": lpJT2CellReceiveCellUtilization,
       "lpJT2CellTransmitCellUtilization": lpJT2CellTransmitCellUtilization,
       "lpJT2CellCorrectableHeaderErrors": lpJT2CellCorrectableHeaderErrors,
       "lpJT2CidDataTable": lpJT2CidDataTable,
       "lpJT2CidDataEntry": lpJT2CidDataEntry,
       "lpJT2CustomerIdentifier": lpJT2CustomerIdentifier,
       "lpJT2ProvTable": lpJT2ProvTable,
       "lpJT2ProvEntry": lpJT2ProvEntry,
       "lpJT2ClockingSource": lpJT2ClockingSource,
       "lpJT2LineLength": lpJT2LineLength,
       "lpJT2ApplicationFramerName": lpJT2ApplicationFramerName,
       "lpJT2IfEntryTable": lpJT2IfEntryTable,
       "lpJT2IfEntryEntry": lpJT2IfEntryEntry,
       "lpJT2IfAdminStatus": lpJT2IfAdminStatus,
       "lpJT2IfIndex": lpJT2IfIndex,
       "lpJT2OperStatusTable": lpJT2OperStatusTable,
       "lpJT2OperStatusEntry": lpJT2OperStatusEntry,
       "lpJT2SnmpOperStatus": lpJT2SnmpOperStatus,
       "lpJT2StateTable": lpJT2StateTable,
       "lpJT2StateEntry": lpJT2StateEntry,
       "lpJT2AdminState": lpJT2AdminState,
       "lpJT2OperationalState": lpJT2OperationalState,
       "lpJT2UsageState": lpJT2UsageState,
       "lpJT2AvailabilityStatus": lpJT2AvailabilityStatus,
       "lpJT2ProceduralStatus": lpJT2ProceduralStatus,
       "lpJT2ControlStatus": lpJT2ControlStatus,
       "lpJT2AlarmStatus": lpJT2AlarmStatus,
       "lpJT2StandbyStatus": lpJT2StandbyStatus,
       "lpJT2UnknownStatus": lpJT2UnknownStatus,
       "lpJT2OperTable": lpJT2OperTable,
       "lpJT2OperEntry": lpJT2OperEntry,
       "lpJT2LosAlarm": lpJT2LosAlarm,
       "lpJT2LofAlarm": lpJT2LofAlarm,
       "lpJT2RxAisPhysicalAlarm": lpJT2RxAisPhysicalAlarm,
       "lpJT2RxAisPayloadAlarm": lpJT2RxAisPayloadAlarm,
       "lpJT2RxRaiAlarm": lpJT2RxRaiAlarm,
       "lpJT2TxAisPhysicalAlarm": lpJT2TxAisPhysicalAlarm,
       "lpJT2TxRaiAlarm": lpJT2TxRaiAlarm,
       "lpJT2StatsTable": lpJT2StatsTable,
       "lpJT2StatsEntry": lpJT2StatsEntry,
       "lpJT2RunningTime": lpJT2RunningTime,
       "lpJT2ErrorFreeSec": lpJT2ErrorFreeSec,
       "lpJT2ErroredSec": lpJT2ErroredSec,
       "lpJT2SevErroredSec": lpJT2SevErroredSec,
       "lpJT2SevErroredFrmSec": lpJT2SevErroredFrmSec,
       "lpJT2UnavailSec": lpJT2UnavailSec,
       "lpJT2BpvErrors": lpJT2BpvErrors,
       "lpJT2CrcErrors": lpJT2CrcErrors,
       "lpJT2FrameErrors": lpJT2FrameErrors,
       "lpJT2LosStateChanges": lpJT2LosStateChanges,
       "lpJT2AdminInfoTable": lpJT2AdminInfoTable,
       "lpJT2AdminInfoEntry": lpJT2AdminInfoEntry,
       "lpJT2Vendor": lpJT2Vendor,
       "lpJT2CommentText": lpJT2CommentText,
       "lpHssi": lpHssi,
       "lpHssiRowStatusTable": lpHssiRowStatusTable,
       "lpHssiRowStatusEntry": lpHssiRowStatusEntry,
       "lpHssiRowStatus": lpHssiRowStatus,
       "lpHssiComponentName": lpHssiComponentName,
       "lpHssiStorageType": lpHssiStorageType,
       "lpHssiIndex": lpHssiIndex,
       "lpHssiTest": lpHssiTest,
       "lpHssiTestRowStatusTable": lpHssiTestRowStatusTable,
       "lpHssiTestRowStatusEntry": lpHssiTestRowStatusEntry,
       "lpHssiTestRowStatus": lpHssiTestRowStatus,
       "lpHssiTestComponentName": lpHssiTestComponentName,
       "lpHssiTestStorageType": lpHssiTestStorageType,
       "lpHssiTestIndex": lpHssiTestIndex,
       "lpHssiTestStateTable": lpHssiTestStateTable,
       "lpHssiTestStateEntry": lpHssiTestStateEntry,
       "lpHssiTestAdminState": lpHssiTestAdminState,
       "lpHssiTestOperationalState": lpHssiTestOperationalState,
       "lpHssiTestUsageState": lpHssiTestUsageState,
       "lpHssiTestSetupTable": lpHssiTestSetupTable,
       "lpHssiTestSetupEntry": lpHssiTestSetupEntry,
       "lpHssiTestPurpose": lpHssiTestPurpose,
       "lpHssiTestType": lpHssiTestType,
       "lpHssiTestFrmSize": lpHssiTestFrmSize,
       "lpHssiTestFrmPatternType": lpHssiTestFrmPatternType,
       "lpHssiTestCustomizedPattern": lpHssiTestCustomizedPattern,
       "lpHssiTestDataStartDelay": lpHssiTestDataStartDelay,
       "lpHssiTestDisplayInterval": lpHssiTestDisplayInterval,
       "lpHssiTestDuration": lpHssiTestDuration,
       "lpHssiTestResultsTable": lpHssiTestResultsTable,
       "lpHssiTestResultsEntry": lpHssiTestResultsEntry,
       "lpHssiTestElapsedTime": lpHssiTestElapsedTime,
       "lpHssiTestTimeRemaining": lpHssiTestTimeRemaining,
       "lpHssiTestCauseOfTermination": lpHssiTestCauseOfTermination,
       "lpHssiTestBitsTx": lpHssiTestBitsTx,
       "lpHssiTestBytesTx": lpHssiTestBytesTx,
       "lpHssiTestFrmTx": lpHssiTestFrmTx,
       "lpHssiTestBitsRx": lpHssiTestBitsRx,
       "lpHssiTestBytesRx": lpHssiTestBytesRx,
       "lpHssiTestFrmRx": lpHssiTestFrmRx,
       "lpHssiTestErroredFrmRx": lpHssiTestErroredFrmRx,
       "lpHssiTestBitErrorRate": lpHssiTestBitErrorRate,
       "lpHssiProvTable": lpHssiProvTable,
       "lpHssiProvEntry": lpHssiProvEntry,
       "lpHssiLinkMode": lpHssiLinkMode,
       "lpHssiReadyLineState": lpHssiReadyLineState,
       "lpHssiDataTransferLineState": lpHssiDataTransferLineState,
       "lpHssiLineSpeed": lpHssiLineSpeed,
       "lpHssiApplicationFramerName": lpHssiApplicationFramerName,
       "lpHssiCidDataTable": lpHssiCidDataTable,
       "lpHssiCidDataEntry": lpHssiCidDataEntry,
       "lpHssiCustomerIdentifier": lpHssiCustomerIdentifier,
       "lpHssiAdminInfoTable": lpHssiAdminInfoTable,
       "lpHssiAdminInfoEntry": lpHssiAdminInfoEntry,
       "lpHssiVendor": lpHssiVendor,
       "lpHssiCommentText": lpHssiCommentText,
       "lpHssiIfEntryTable": lpHssiIfEntryTable,
       "lpHssiIfEntryEntry": lpHssiIfEntryEntry,
       "lpHssiIfAdminStatus": lpHssiIfAdminStatus,
       "lpHssiIfIndex": lpHssiIfIndex,
       "lpHssiOperStatusTable": lpHssiOperStatusTable,
       "lpHssiOperStatusEntry": lpHssiOperStatusEntry,
       "lpHssiSnmpOperStatus": lpHssiSnmpOperStatus,
       "lpHssiStateTable": lpHssiStateTable,
       "lpHssiStateEntry": lpHssiStateEntry,
       "lpHssiAdminState": lpHssiAdminState,
       "lpHssiOperationalState": lpHssiOperationalState,
       "lpHssiUsageState": lpHssiUsageState,
       "lpHssiAvailabilityStatus": lpHssiAvailabilityStatus,
       "lpHssiProceduralStatus": lpHssiProceduralStatus,
       "lpHssiControlStatus": lpHssiControlStatus,
       "lpHssiAlarmStatus": lpHssiAlarmStatus,
       "lpHssiStandbyStatus": lpHssiStandbyStatus,
       "lpHssiUnknownStatus": lpHssiUnknownStatus,
       "lpHssiOperTable": lpHssiOperTable,
       "lpHssiOperEntry": lpHssiOperEntry,
       "lpHssiActualLinkMode": lpHssiActualLinkMode,
       "lpHssiLineState": lpHssiLineState,
       "lpHssiActualTxLineSpeed": lpHssiActualTxLineSpeed,
       "lpHssiActualRxLineSpeed": lpHssiActualRxLineSpeed,
       "lpHssiDataXferStateChanges": lpHssiDataXferStateChanges,
       "lpEng": lpEng,
       "lpEngRowStatusTable": lpEngRowStatusTable,
       "lpEngRowStatusEntry": lpEngRowStatusEntry,
       "lpEngRowStatus": lpEngRowStatus,
       "lpEngComponentName": lpEngComponentName,
       "lpEngStorageType": lpEngStorageType,
       "lpEngIndex": lpEngIndex,
       "lpEngDs": lpEngDs,
       "lpEngDsRowStatusTable": lpEngDsRowStatusTable,
       "lpEngDsRowStatusEntry": lpEngDsRowStatusEntry,
       "lpEngDsRowStatus": lpEngDsRowStatus,
       "lpEngDsComponentName": lpEngDsComponentName,
       "lpEngDsStorageType": lpEngDsStorageType,
       "lpEngDsIndex": lpEngDsIndex,
       "lpEngDsOv": lpEngDsOv,
       "lpEngDsOvRowStatusTable": lpEngDsOvRowStatusTable,
       "lpEngDsOvRowStatusEntry": lpEngDsOvRowStatusEntry,
       "lpEngDsOvRowStatus": lpEngDsOvRowStatus,
       "lpEngDsOvComponentName": lpEngDsOvComponentName,
       "lpEngDsOvStorageType": lpEngDsOvStorageType,
       "lpEngDsOvIndex": lpEngDsOvIndex,
       "lpEngDsOvProvTable": lpEngDsOvProvTable,
       "lpEngDsOvProvEntry": lpEngDsOvProvEntry,
       "lpEngDsOvAgentQueueSize": lpEngDsOvAgentQueueSize,
       "lpEngDsOperTable": lpEngDsOperTable,
       "lpEngDsOperEntry": lpEngDsOperEntry,
       "lpEngDsAgentQueueSize": lpEngDsAgentQueueSize,
       "lpProvTable": lpProvTable,
       "lpProvEntry": lpProvEntry,
       "lpMainCard": lpMainCard,
       "lpSpareCard": lpSpareCard,
       "lpLogicalProcessorType": lpLogicalProcessorType,
       "lpCidDataTable": lpCidDataTable,
       "lpCidDataEntry": lpCidDataEntry,
       "lpCustomerIdentifier": lpCustomerIdentifier,
       "lpStateTable": lpStateTable,
       "lpStateEntry": lpStateEntry,
       "lpAdminState": lpAdminState,
       "lpOperationalState": lpOperationalState,
       "lpUsageState": lpUsageState,
       "lpAvailabilityStatus": lpAvailabilityStatus,
       "lpProceduralStatus": lpProceduralStatus,
       "lpControlStatus": lpControlStatus,
       "lpAlarmStatus": lpAlarmStatus,
       "lpStandbyStatus": lpStandbyStatus,
       "lpUnknownStatus": lpUnknownStatus,
       "lpOperTable": lpOperTable,
       "lpOperEntry": lpOperEntry,
       "lpActiveCard": lpActiveCard,
       "lpMainCardStatus": lpMainCardStatus,
       "lpSpareCardStatus": lpSpareCardStatus,
       "lpRestartOnCpSwitch": lpRestartOnCpSwitch,
       "lpScheduledSwitchover": lpScheduledSwitchover,
       "lpUtilTable": lpUtilTable,
       "lpUtilEntry": lpUtilEntry,
       "lpTimeInterval": lpTimeInterval,
       "lpCpuUtil": lpCpuUtil,
       "lpCpuUtilAvg": lpCpuUtilAvg,
       "lpCpuUtilAvgMin": lpCpuUtilAvgMin,
       "lpCpuUtilAvgMax": lpCpuUtilAvgMax,
       "lpMsgBlockUsage": lpMsgBlockUsage,
       "lpMsgBlockUsageAvg": lpMsgBlockUsageAvg,
       "lpMsgBlockUsageAvgMin": lpMsgBlockUsageAvgMin,
       "lpMsgBlockUsageAvgMax": lpMsgBlockUsageAvgMax,
       "lpLocalMsgBlockUsage": lpLocalMsgBlockUsage,
       "lpLocalMsgBlockUsageAvg": lpLocalMsgBlockUsageAvg,
       "lpLocalMsgBlockUsageMin": lpLocalMsgBlockUsageMin,
       "lpLocalMsgBlockUsageMax": lpLocalMsgBlockUsageMax,
       "lpCapTable": lpCapTable,
       "lpCapEntry": lpCapEntry,
       "lpMsgBlockCapacity": lpMsgBlockCapacity,
       "lpLocalMsgBlockCapacity": lpLocalMsgBlockCapacity,
       "lpLinkToApplicationsTable": lpLinkToApplicationsTable,
       "lpLinkToApplicationsEntry": lpLinkToApplicationsEntry,
       "lpLinkToApplicationsValue": lpLinkToApplicationsValue,
       "lpMemoryCapacityTable": lpMemoryCapacityTable,
       "lpMemoryCapacityEntry": lpMemoryCapacityEntry,
       "lpMemoryCapacityIndex": lpMemoryCapacityIndex,
       "lpMemoryCapacityValue": lpMemoryCapacityValue,
       "lpMemoryUsageTable": lpMemoryUsageTable,
       "lpMemoryUsageEntry": lpMemoryUsageEntry,
       "lpMemoryUsageIndex": lpMemoryUsageIndex,
       "lpMemoryUsageValue": lpMemoryUsageValue,
       "lpMemoryUsageAvgTable": lpMemoryUsageAvgTable,
       "lpMemoryUsageAvgEntry": lpMemoryUsageAvgEntry,
       "lpMemoryUsageAvgIndex": lpMemoryUsageAvgIndex,
       "lpMemoryUsageAvgValue": lpMemoryUsageAvgValue,
       "lpMemoryUsageAvgMinTable": lpMemoryUsageAvgMinTable,
       "lpMemoryUsageAvgMinEntry": lpMemoryUsageAvgMinEntry,
       "lpMemoryUsageAvgMinIndex": lpMemoryUsageAvgMinIndex,
       "lpMemoryUsageAvgMinValue": lpMemoryUsageAvgMinValue,
       "lpMemoryUsageAvgMaxTable": lpMemoryUsageAvgMaxTable,
       "lpMemoryUsageAvgMaxEntry": lpMemoryUsageAvgMaxEntry,
       "lpMemoryUsageAvgMaxIndex": lpMemoryUsageAvgMaxIndex,
       "lpMemoryUsageAvgMaxValue": lpMemoryUsageAvgMaxValue,
       "logicalProcessorMIB": logicalProcessorMIB,
       "logicalProcessorGroup": logicalProcessorGroup,
       "logicalProcessorGroupBE": logicalProcessorGroupBE,
       "logicalProcessorGroupBE01": logicalProcessorGroupBE01,
       "logicalProcessorGroupBE01A": logicalProcessorGroupBE01A,
       "logicalProcessorCapabilities": logicalProcessorCapabilities,
       "logicalProcessorCapabilitiesBE": logicalProcessorCapabilitiesBE,
       "logicalProcessorCapabilitiesBE01": logicalProcessorCapabilitiesBE01,
       "logicalProcessorCapabilitiesBE01A": logicalProcessorCapabilitiesBE01A}
)
