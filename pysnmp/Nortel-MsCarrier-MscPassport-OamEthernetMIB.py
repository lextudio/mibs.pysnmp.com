# SNMP MIB module (Nortel-MsCarrier-MscPassport-OamEthernetMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-OamEthernetMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:54 2024
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
 mscLpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB",
    "mscLp",
    "mscLpIndex")

(Counter32,
 DisplayString,
 Integer32,
 InterfaceIndex,
 MacAddress,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Integer32",
    "InterfaceIndex",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Link,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "Link",
    "NonReplicated")

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

_MscLpOamEnet_ObjectIdentity = ObjectIdentity
mscLpOamEnet = _MscLpOamEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27)
)
_MscLpOamEnetRowStatusTable_Object = MibTable
mscLpOamEnetRowStatusTable = _MscLpOamEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1)
)
if mibBuilder.loadTexts:
    mscLpOamEnetRowStatusTable.setStatus("mandatory")
_MscLpOamEnetRowStatusEntry_Object = MibTableRow
mscLpOamEnetRowStatusEntry = _MscLpOamEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1)
)
mscLpOamEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetRowStatusEntry.setStatus("mandatory")
_MscLpOamEnetRowStatus_Type = RowStatus
_MscLpOamEnetRowStatus_Object = MibTableColumn
mscLpOamEnetRowStatus = _MscLpOamEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 1),
    _MscLpOamEnetRowStatus_Type()
)
mscLpOamEnetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetRowStatus.setStatus("mandatory")
_MscLpOamEnetComponentName_Type = DisplayString
_MscLpOamEnetComponentName_Object = MibTableColumn
mscLpOamEnetComponentName = _MscLpOamEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 2),
    _MscLpOamEnetComponentName_Type()
)
mscLpOamEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetComponentName.setStatus("mandatory")
_MscLpOamEnetStorageType_Type = StorageType
_MscLpOamEnetStorageType_Object = MibTableColumn
mscLpOamEnetStorageType = _MscLpOamEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 4),
    _MscLpOamEnetStorageType_Type()
)
mscLpOamEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetStorageType.setStatus("mandatory")


class _MscLpOamEnetIndex_Type(Integer32):
    """Custom type mscLpOamEnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MscLpOamEnetIndex_Type.__name__ = "Integer32"
_MscLpOamEnetIndex_Object = MibTableColumn
mscLpOamEnetIndex = _MscLpOamEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 1, 1, 10),
    _MscLpOamEnetIndex_Type()
)
mscLpOamEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpOamEnetIndex.setStatus("mandatory")
_MscLpOamEnetTest_ObjectIdentity = ObjectIdentity
mscLpOamEnetTest = _MscLpOamEnetTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2)
)
_MscLpOamEnetTestRowStatusTable_Object = MibTable
mscLpOamEnetTestRowStatusTable = _MscLpOamEnetTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1)
)
if mibBuilder.loadTexts:
    mscLpOamEnetTestRowStatusTable.setStatus("mandatory")
_MscLpOamEnetTestRowStatusEntry_Object = MibTableRow
mscLpOamEnetTestRowStatusEntry = _MscLpOamEnetTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1)
)
mscLpOamEnetTestRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetTestRowStatusEntry.setStatus("mandatory")
_MscLpOamEnetTestRowStatus_Type = RowStatus
_MscLpOamEnetTestRowStatus_Object = MibTableColumn
mscLpOamEnetTestRowStatus = _MscLpOamEnetTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 1),
    _MscLpOamEnetTestRowStatus_Type()
)
mscLpOamEnetTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetTestRowStatus.setStatus("mandatory")
_MscLpOamEnetTestComponentName_Type = DisplayString
_MscLpOamEnetTestComponentName_Object = MibTableColumn
mscLpOamEnetTestComponentName = _MscLpOamEnetTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 2),
    _MscLpOamEnetTestComponentName_Type()
)
mscLpOamEnetTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetTestComponentName.setStatus("mandatory")
_MscLpOamEnetTestStorageType_Type = StorageType
_MscLpOamEnetTestStorageType_Object = MibTableColumn
mscLpOamEnetTestStorageType = _MscLpOamEnetTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 4),
    _MscLpOamEnetTestStorageType_Type()
)
mscLpOamEnetTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetTestStorageType.setStatus("mandatory")
_MscLpOamEnetTestIndex_Type = NonReplicated
_MscLpOamEnetTestIndex_Object = MibTableColumn
mscLpOamEnetTestIndex = _MscLpOamEnetTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 1, 1, 10),
    _MscLpOamEnetTestIndex_Type()
)
mscLpOamEnetTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscLpOamEnetTestIndex.setStatus("mandatory")
_MscLpOamEnetTestOperTable_Object = MibTable
mscLpOamEnetTestOperTable = _MscLpOamEnetTestOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 10)
)
if mibBuilder.loadTexts:
    mscLpOamEnetTestOperTable.setStatus("mandatory")
_MscLpOamEnetTestOperEntry_Object = MibTableRow
mscLpOamEnetTestOperEntry = _MscLpOamEnetTestOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 10, 1)
)
mscLpOamEnetTestOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetTestOperEntry.setStatus("mandatory")


class _MscLpOamEnetTestType_Type(Integer32):
    """Custom type mscLpOamEnetTestType based on Integer32"""
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
        *(("configuration", 1),
          ("hardwareLogic", 0),
          ("memoryMap", 2),
          ("tdr", 3))
    )


_MscLpOamEnetTestType_Type.__name__ = "Integer32"
_MscLpOamEnetTestType_Object = MibTableColumn
mscLpOamEnetTestType = _MscLpOamEnetTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 10, 1, 1),
    _MscLpOamEnetTestType_Type()
)
mscLpOamEnetTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetTestType.setStatus("mandatory")
_MscLpOamEnetTestResultsTable_Object = MibTable
mscLpOamEnetTestResultsTable = _MscLpOamEnetTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11)
)
if mibBuilder.loadTexts:
    mscLpOamEnetTestResultsTable.setStatus("mandatory")
_MscLpOamEnetTestResultsEntry_Object = MibTableRow
mscLpOamEnetTestResultsEntry = _MscLpOamEnetTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11, 1)
)
mscLpOamEnetTestResultsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetTestIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetTestResultsEntry.setStatus("mandatory")


class _MscLpOamEnetTestCauseOfTermination_Type(Integer32):
    """Custom type mscLpOamEnetTestCauseOfTermination based on Integer32"""
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
        *(("neverStarted", 3),
          ("stoppedByOperator", 1),
          ("testComplete", 5),
          ("testRunning", 4),
          ("testTimeExpired", 0),
          ("unknown", 2))
    )


_MscLpOamEnetTestCauseOfTermination_Type.__name__ = "Integer32"
_MscLpOamEnetTestCauseOfTermination_Object = MibTableColumn
mscLpOamEnetTestCauseOfTermination = _MscLpOamEnetTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11, 1, 1),
    _MscLpOamEnetTestCauseOfTermination_Type()
)
mscLpOamEnetTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetTestCauseOfTermination.setStatus("mandatory")


class _MscLpOamEnetTestTestResult_Type(Integer32):
    """Custom type mscLpOamEnetTestTestResult based on Integer32"""
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
        *(("fail", 1),
          ("neverRun", 0),
          ("pass", 2),
          ("running", 3))
    )


_MscLpOamEnetTestTestResult_Type.__name__ = "Integer32"
_MscLpOamEnetTestTestResult_Object = MibTableColumn
mscLpOamEnetTestTestResult = _MscLpOamEnetTestTestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 2, 11, 1, 2),
    _MscLpOamEnetTestTestResult_Type()
)
mscLpOamEnetTestTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetTestTestResult.setStatus("mandatory")
_MscLpOamEnetCidDataTable_Object = MibTable
mscLpOamEnetCidDataTable = _MscLpOamEnetCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 10)
)
if mibBuilder.loadTexts:
    mscLpOamEnetCidDataTable.setStatus("mandatory")
_MscLpOamEnetCidDataEntry_Object = MibTableRow
mscLpOamEnetCidDataEntry = _MscLpOamEnetCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 10, 1)
)
mscLpOamEnetCidDataEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetCidDataEntry.setStatus("mandatory")


class _MscLpOamEnetCustomerIdentifier_Type(Unsigned32):
    """Custom type mscLpOamEnetCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_MscLpOamEnetCustomerIdentifier_Type.__name__ = "Unsigned32"
_MscLpOamEnetCustomerIdentifier_Object = MibTableColumn
mscLpOamEnetCustomerIdentifier = _MscLpOamEnetCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 10, 1, 1),
    _MscLpOamEnetCustomerIdentifier_Type()
)
mscLpOamEnetCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetCustomerIdentifier.setStatus("mandatory")
_MscLpOamEnetIfEntryTable_Object = MibTable
mscLpOamEnetIfEntryTable = _MscLpOamEnetIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11)
)
if mibBuilder.loadTexts:
    mscLpOamEnetIfEntryTable.setStatus("mandatory")
_MscLpOamEnetIfEntryEntry_Object = MibTableRow
mscLpOamEnetIfEntryEntry = _MscLpOamEnetIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11, 1)
)
mscLpOamEnetIfEntryEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetIfEntryEntry.setStatus("mandatory")


class _MscLpOamEnetIfAdminStatus_Type(Integer32):
    """Custom type mscLpOamEnetIfAdminStatus based on Integer32"""
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


_MscLpOamEnetIfAdminStatus_Type.__name__ = "Integer32"
_MscLpOamEnetIfAdminStatus_Object = MibTableColumn
mscLpOamEnetIfAdminStatus = _MscLpOamEnetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11, 1, 1),
    _MscLpOamEnetIfAdminStatus_Type()
)
mscLpOamEnetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetIfAdminStatus.setStatus("mandatory")


class _MscLpOamEnetIfIndex_Type(InterfaceIndex):
    """Custom type mscLpOamEnetIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscLpOamEnetIfIndex_Type.__name__ = "InterfaceIndex"
_MscLpOamEnetIfIndex_Object = MibTableColumn
mscLpOamEnetIfIndex = _MscLpOamEnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 11, 1, 2),
    _MscLpOamEnetIfIndex_Type()
)
mscLpOamEnetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetIfIndex.setStatus("mandatory")
_MscLpOamEnetProvTable_Object = MibTable
mscLpOamEnetProvTable = _MscLpOamEnetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12)
)
if mibBuilder.loadTexts:
    mscLpOamEnetProvTable.setStatus("mandatory")
_MscLpOamEnetProvEntry_Object = MibTableRow
mscLpOamEnetProvEntry = _MscLpOamEnetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1)
)
mscLpOamEnetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetProvEntry.setStatus("mandatory")
_MscLpOamEnetApplicationFramerName_Type = Link
_MscLpOamEnetApplicationFramerName_Object = MibTableColumn
mscLpOamEnetApplicationFramerName = _MscLpOamEnetApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1, 1),
    _MscLpOamEnetApplicationFramerName_Type()
)
mscLpOamEnetApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetApplicationFramerName.setStatus("mandatory")


class _MscLpOamEnetSwitchoverOnFailure_Type(Integer32):
    """Custom type mscLpOamEnetSwitchoverOnFailure based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscLpOamEnetSwitchoverOnFailure_Type.__name__ = "Integer32"
_MscLpOamEnetSwitchoverOnFailure_Object = MibTableColumn
mscLpOamEnetSwitchoverOnFailure = _MscLpOamEnetSwitchoverOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1, 3),
    _MscLpOamEnetSwitchoverOnFailure_Type()
)
mscLpOamEnetSwitchoverOnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetSwitchoverOnFailure.setStatus("mandatory")


class _MscLpOamEnetExtendedStatistics_Type(Integer32):
    """Custom type mscLpOamEnetExtendedStatistics based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscLpOamEnetExtendedStatistics_Type.__name__ = "Integer32"
_MscLpOamEnetExtendedStatistics_Object = MibTableColumn
mscLpOamEnetExtendedStatistics = _MscLpOamEnetExtendedStatistics_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 12, 1, 4),
    _MscLpOamEnetExtendedStatistics_Type()
)
mscLpOamEnetExtendedStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetExtendedStatistics.setStatus("mandatory")
_MscLpOamEnetAdminInfoTable_Object = MibTable
mscLpOamEnetAdminInfoTable = _MscLpOamEnetAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13)
)
if mibBuilder.loadTexts:
    mscLpOamEnetAdminInfoTable.setStatus("mandatory")
_MscLpOamEnetAdminInfoEntry_Object = MibTableRow
mscLpOamEnetAdminInfoEntry = _MscLpOamEnetAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13, 1)
)
mscLpOamEnetAdminInfoEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetAdminInfoEntry.setStatus("mandatory")


class _MscLpOamEnetVendor_Type(AsciiString):
    """Custom type mscLpOamEnetVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_MscLpOamEnetVendor_Type.__name__ = "AsciiString"
_MscLpOamEnetVendor_Object = MibTableColumn
mscLpOamEnetVendor = _MscLpOamEnetVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13, 1, 1),
    _MscLpOamEnetVendor_Type()
)
mscLpOamEnetVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetVendor.setStatus("mandatory")


class _MscLpOamEnetCommentText_Type(AsciiString):
    """Custom type mscLpOamEnetCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_MscLpOamEnetCommentText_Type.__name__ = "AsciiString"
_MscLpOamEnetCommentText_Object = MibTableColumn
mscLpOamEnetCommentText = _MscLpOamEnetCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 13, 1, 2),
    _MscLpOamEnetCommentText_Type()
)
mscLpOamEnetCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscLpOamEnetCommentText.setStatus("mandatory")
_MscLpOamEnetStateTable_Object = MibTable
mscLpOamEnetStateTable = _MscLpOamEnetStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15)
)
if mibBuilder.loadTexts:
    mscLpOamEnetStateTable.setStatus("mandatory")
_MscLpOamEnetStateEntry_Object = MibTableRow
mscLpOamEnetStateEntry = _MscLpOamEnetStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1)
)
mscLpOamEnetStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetStateEntry.setStatus("mandatory")


class _MscLpOamEnetAdminState_Type(Integer32):
    """Custom type mscLpOamEnetAdminState based on Integer32"""
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


_MscLpOamEnetAdminState_Type.__name__ = "Integer32"
_MscLpOamEnetAdminState_Object = MibTableColumn
mscLpOamEnetAdminState = _MscLpOamEnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1, 1),
    _MscLpOamEnetAdminState_Type()
)
mscLpOamEnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetAdminState.setStatus("mandatory")


class _MscLpOamEnetOperationalState_Type(Integer32):
    """Custom type mscLpOamEnetOperationalState based on Integer32"""
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


_MscLpOamEnetOperationalState_Type.__name__ = "Integer32"
_MscLpOamEnetOperationalState_Object = MibTableColumn
mscLpOamEnetOperationalState = _MscLpOamEnetOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1, 2),
    _MscLpOamEnetOperationalState_Type()
)
mscLpOamEnetOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetOperationalState.setStatus("mandatory")


class _MscLpOamEnetUsageState_Type(Integer32):
    """Custom type mscLpOamEnetUsageState based on Integer32"""
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


_MscLpOamEnetUsageState_Type.__name__ = "Integer32"
_MscLpOamEnetUsageState_Object = MibTableColumn
mscLpOamEnetUsageState = _MscLpOamEnetUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 15, 1, 3),
    _MscLpOamEnetUsageState_Type()
)
mscLpOamEnetUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetUsageState.setStatus("mandatory")
_MscLpOamEnetOperStatusTable_Object = MibTable
mscLpOamEnetOperStatusTable = _MscLpOamEnetOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 16)
)
if mibBuilder.loadTexts:
    mscLpOamEnetOperStatusTable.setStatus("mandatory")
_MscLpOamEnetOperStatusEntry_Object = MibTableRow
mscLpOamEnetOperStatusEntry = _MscLpOamEnetOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 16, 1)
)
mscLpOamEnetOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetOperStatusEntry.setStatus("mandatory")


class _MscLpOamEnetSnmpOperStatus_Type(Integer32):
    """Custom type mscLpOamEnetSnmpOperStatus based on Integer32"""
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


_MscLpOamEnetSnmpOperStatus_Type.__name__ = "Integer32"
_MscLpOamEnetSnmpOperStatus_Object = MibTableColumn
mscLpOamEnetSnmpOperStatus = _MscLpOamEnetSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 16, 1, 1),
    _MscLpOamEnetSnmpOperStatus_Type()
)
mscLpOamEnetSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetSnmpOperStatus.setStatus("mandatory")
_MscLpOamEnetOperTable_Object = MibTable
mscLpOamEnetOperTable = _MscLpOamEnetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17)
)
if mibBuilder.loadTexts:
    mscLpOamEnetOperTable.setStatus("mandatory")
_MscLpOamEnetOperEntry_Object = MibTableRow
mscLpOamEnetOperEntry = _MscLpOamEnetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1)
)
mscLpOamEnetOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetOperEntry.setStatus("mandatory")


class _MscLpOamEnetMacAddress_Type(MacAddress):
    """Custom type mscLpOamEnetMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MscLpOamEnetMacAddress_Type.__name__ = "MacAddress"
_MscLpOamEnetMacAddress_Object = MibTableColumn
mscLpOamEnetMacAddress = _MscLpOamEnetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1, 1),
    _MscLpOamEnetMacAddress_Type()
)
mscLpOamEnetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetMacAddress.setStatus("mandatory")


class _MscLpOamEnetActiveStatus_Type(Integer32):
    """Custom type mscLpOamEnetActiveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_MscLpOamEnetActiveStatus_Type.__name__ = "Integer32"
_MscLpOamEnetActiveStatus_Object = MibTableColumn
mscLpOamEnetActiveStatus = _MscLpOamEnetActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1, 2),
    _MscLpOamEnetActiveStatus_Type()
)
mscLpOamEnetActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetActiveStatus.setStatus("mandatory")


class _MscLpOamEnetStandbyStatus_Type(Integer32):
    """Custom type mscLpOamEnetStandbyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_MscLpOamEnetStandbyStatus_Type.__name__ = "Integer32"
_MscLpOamEnetStandbyStatus_Object = MibTableColumn
mscLpOamEnetStandbyStatus = _MscLpOamEnetStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 17, 1, 3),
    _MscLpOamEnetStandbyStatus_Type()
)
mscLpOamEnetStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetStandbyStatus.setStatus("mandatory")
_MscLpOamEnetOamEnetStatsTable_Object = MibTable
mscLpOamEnetOamEnetStatsTable = _MscLpOamEnetOamEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18)
)
if mibBuilder.loadTexts:
    mscLpOamEnetOamEnetStatsTable.setStatus("mandatory")
_MscLpOamEnetOamEnetStatsEntry_Object = MibTableRow
mscLpOamEnetOamEnetStatsEntry = _MscLpOamEnetOamEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1)
)
mscLpOamEnetOamEnetStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetOamEnetStatsEntry.setStatus("mandatory")
_MscLpOamEnetClearToSendSignalLoss_Type = Counter32
_MscLpOamEnetClearToSendSignalLoss_Object = MibTableColumn
mscLpOamEnetClearToSendSignalLoss = _MscLpOamEnetClearToSendSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 14),
    _MscLpOamEnetClearToSendSignalLoss_Type()
)
mscLpOamEnetClearToSendSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetClearToSendSignalLoss.setStatus("mandatory")
_MscLpOamEnetFrameTooShort_Type = Counter32
_MscLpOamEnetFrameTooShort_Object = MibTableColumn
mscLpOamEnetFrameTooShort = _MscLpOamEnetFrameTooShort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 15),
    _MscLpOamEnetFrameTooShort_Type()
)
mscLpOamEnetFrameTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetFrameTooShort.setStatus("mandatory")
_MscLpOamEnetNumberOfRxCollisions_Type = Counter32
_MscLpOamEnetNumberOfRxCollisions_Object = MibTableColumn
mscLpOamEnetNumberOfRxCollisions = _MscLpOamEnetNumberOfRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 17),
    _MscLpOamEnetNumberOfRxCollisions_Type()
)
mscLpOamEnetNumberOfRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetNumberOfRxCollisions.setStatus("mandatory")
_MscLpOamEnetLackOfResourcesDiscards_Type = Counter32
_MscLpOamEnetLackOfResourcesDiscards_Object = MibTableColumn
mscLpOamEnetLackOfResourcesDiscards = _MscLpOamEnetLackOfResourcesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 18),
    _MscLpOamEnetLackOfResourcesDiscards_Type()
)
mscLpOamEnetLackOfResourcesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetLackOfResourcesDiscards.setStatus("mandatory")
_MscLpOamEnetOverrunErrors_Type = Counter32
_MscLpOamEnetOverrunErrors_Object = MibTableColumn
mscLpOamEnetOverrunErrors = _MscLpOamEnetOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 18, 1, 19),
    _MscLpOamEnetOverrunErrors_Type()
)
mscLpOamEnetOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetOverrunErrors.setStatus("mandatory")
_MscLpOamEnetStatsTable_Object = MibTable
mscLpOamEnetStatsTable = _MscLpOamEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19)
)
if mibBuilder.loadTexts:
    mscLpOamEnetStatsTable.setStatus("mandatory")
_MscLpOamEnetStatsEntry_Object = MibTableRow
mscLpOamEnetStatsEntry = _MscLpOamEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1)
)
mscLpOamEnetStatsEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-LogicalProcessorMIB", "mscLpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-OamEthernetMIB", "mscLpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    mscLpOamEnetStatsEntry.setStatus("mandatory")
_MscLpOamEnetAlignmentErrors_Type = Counter32
_MscLpOamEnetAlignmentErrors_Object = MibTableColumn
mscLpOamEnetAlignmentErrors = _MscLpOamEnetAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 2),
    _MscLpOamEnetAlignmentErrors_Type()
)
mscLpOamEnetAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetAlignmentErrors.setStatus("mandatory")
_MscLpOamEnetFcsErrors_Type = Counter32
_MscLpOamEnetFcsErrors_Object = MibTableColumn
mscLpOamEnetFcsErrors = _MscLpOamEnetFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 3),
    _MscLpOamEnetFcsErrors_Type()
)
mscLpOamEnetFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetFcsErrors.setStatus("mandatory")
_MscLpOamEnetSingleCollisionFrames_Type = Counter32
_MscLpOamEnetSingleCollisionFrames_Object = MibTableColumn
mscLpOamEnetSingleCollisionFrames = _MscLpOamEnetSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 4),
    _MscLpOamEnetSingleCollisionFrames_Type()
)
mscLpOamEnetSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetSingleCollisionFrames.setStatus("mandatory")
_MscLpOamEnetMultipleCollisionFrames_Type = Counter32
_MscLpOamEnetMultipleCollisionFrames_Object = MibTableColumn
mscLpOamEnetMultipleCollisionFrames = _MscLpOamEnetMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 5),
    _MscLpOamEnetMultipleCollisionFrames_Type()
)
mscLpOamEnetMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetMultipleCollisionFrames.setStatus("mandatory")
_MscLpOamEnetSqeTestErrors_Type = Counter32
_MscLpOamEnetSqeTestErrors_Object = MibTableColumn
mscLpOamEnetSqeTestErrors = _MscLpOamEnetSqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 6),
    _MscLpOamEnetSqeTestErrors_Type()
)
mscLpOamEnetSqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetSqeTestErrors.setStatus("mandatory")
_MscLpOamEnetDeferredTransmissions_Type = Counter32
_MscLpOamEnetDeferredTransmissions_Object = MibTableColumn
mscLpOamEnetDeferredTransmissions = _MscLpOamEnetDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 7),
    _MscLpOamEnetDeferredTransmissions_Type()
)
mscLpOamEnetDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetDeferredTransmissions.setStatus("mandatory")
_MscLpOamEnetLateCollisions_Type = Counter32
_MscLpOamEnetLateCollisions_Object = MibTableColumn
mscLpOamEnetLateCollisions = _MscLpOamEnetLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 8),
    _MscLpOamEnetLateCollisions_Type()
)
mscLpOamEnetLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetLateCollisions.setStatus("mandatory")
_MscLpOamEnetExcessiveCollisions_Type = Counter32
_MscLpOamEnetExcessiveCollisions_Object = MibTableColumn
mscLpOamEnetExcessiveCollisions = _MscLpOamEnetExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 9),
    _MscLpOamEnetExcessiveCollisions_Type()
)
mscLpOamEnetExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetExcessiveCollisions.setStatus("mandatory")
_MscLpOamEnetMacTransmitErrors_Type = Counter32
_MscLpOamEnetMacTransmitErrors_Object = MibTableColumn
mscLpOamEnetMacTransmitErrors = _MscLpOamEnetMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 10),
    _MscLpOamEnetMacTransmitErrors_Type()
)
mscLpOamEnetMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetMacTransmitErrors.setStatus("mandatory")
_MscLpOamEnetCarrierSenseErrors_Type = Counter32
_MscLpOamEnetCarrierSenseErrors_Object = MibTableColumn
mscLpOamEnetCarrierSenseErrors = _MscLpOamEnetCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 11),
    _MscLpOamEnetCarrierSenseErrors_Type()
)
mscLpOamEnetCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetCarrierSenseErrors.setStatus("mandatory")
_MscLpOamEnetFrameTooLongs_Type = Counter32
_MscLpOamEnetFrameTooLongs_Object = MibTableColumn
mscLpOamEnetFrameTooLongs = _MscLpOamEnetFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 12),
    _MscLpOamEnetFrameTooLongs_Type()
)
mscLpOamEnetFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetFrameTooLongs.setStatus("mandatory")
_MscLpOamEnetMacReceiveErrors_Type = Counter32
_MscLpOamEnetMacReceiveErrors_Object = MibTableColumn
mscLpOamEnetMacReceiveErrors = _MscLpOamEnetMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 12, 27, 19, 1, 13),
    _MscLpOamEnetMacReceiveErrors_Type()
)
mscLpOamEnetMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscLpOamEnetMacReceiveErrors.setStatus("mandatory")
_OamEthernetMIB_ObjectIdentity = ObjectIdentity
oamEthernetMIB = _OamEthernetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79)
)
_OamEthernetGroup_ObjectIdentity = ObjectIdentity
oamEthernetGroup = _OamEthernetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1)
)
_OamEthernetGroupCA_ObjectIdentity = ObjectIdentity
oamEthernetGroupCA = _OamEthernetGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1, 1)
)
_OamEthernetGroupCA02_ObjectIdentity = ObjectIdentity
oamEthernetGroupCA02 = _OamEthernetGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1, 1, 3)
)
_OamEthernetGroupCA02A_ObjectIdentity = ObjectIdentity
oamEthernetGroupCA02A = _OamEthernetGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 1, 1, 3, 2)
)
_OamEthernetCapabilities_ObjectIdentity = ObjectIdentity
oamEthernetCapabilities = _OamEthernetCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3)
)
_OamEthernetCapabilitiesCA_ObjectIdentity = ObjectIdentity
oamEthernetCapabilitiesCA = _OamEthernetCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3, 1)
)
_OamEthernetCapabilitiesCA02_ObjectIdentity = ObjectIdentity
oamEthernetCapabilitiesCA02 = _OamEthernetCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3, 1, 3)
)
_OamEthernetCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
oamEthernetCapabilitiesCA02A = _OamEthernetCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 79, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-OamEthernetMIB",
    **{"mscLpOamEnet": mscLpOamEnet,
       "mscLpOamEnetRowStatusTable": mscLpOamEnetRowStatusTable,
       "mscLpOamEnetRowStatusEntry": mscLpOamEnetRowStatusEntry,
       "mscLpOamEnetRowStatus": mscLpOamEnetRowStatus,
       "mscLpOamEnetComponentName": mscLpOamEnetComponentName,
       "mscLpOamEnetStorageType": mscLpOamEnetStorageType,
       "mscLpOamEnetIndex": mscLpOamEnetIndex,
       "mscLpOamEnetTest": mscLpOamEnetTest,
       "mscLpOamEnetTestRowStatusTable": mscLpOamEnetTestRowStatusTable,
       "mscLpOamEnetTestRowStatusEntry": mscLpOamEnetTestRowStatusEntry,
       "mscLpOamEnetTestRowStatus": mscLpOamEnetTestRowStatus,
       "mscLpOamEnetTestComponentName": mscLpOamEnetTestComponentName,
       "mscLpOamEnetTestStorageType": mscLpOamEnetTestStorageType,
       "mscLpOamEnetTestIndex": mscLpOamEnetTestIndex,
       "mscLpOamEnetTestOperTable": mscLpOamEnetTestOperTable,
       "mscLpOamEnetTestOperEntry": mscLpOamEnetTestOperEntry,
       "mscLpOamEnetTestType": mscLpOamEnetTestType,
       "mscLpOamEnetTestResultsTable": mscLpOamEnetTestResultsTable,
       "mscLpOamEnetTestResultsEntry": mscLpOamEnetTestResultsEntry,
       "mscLpOamEnetTestCauseOfTermination": mscLpOamEnetTestCauseOfTermination,
       "mscLpOamEnetTestTestResult": mscLpOamEnetTestTestResult,
       "mscLpOamEnetCidDataTable": mscLpOamEnetCidDataTable,
       "mscLpOamEnetCidDataEntry": mscLpOamEnetCidDataEntry,
       "mscLpOamEnetCustomerIdentifier": mscLpOamEnetCustomerIdentifier,
       "mscLpOamEnetIfEntryTable": mscLpOamEnetIfEntryTable,
       "mscLpOamEnetIfEntryEntry": mscLpOamEnetIfEntryEntry,
       "mscLpOamEnetIfAdminStatus": mscLpOamEnetIfAdminStatus,
       "mscLpOamEnetIfIndex": mscLpOamEnetIfIndex,
       "mscLpOamEnetProvTable": mscLpOamEnetProvTable,
       "mscLpOamEnetProvEntry": mscLpOamEnetProvEntry,
       "mscLpOamEnetApplicationFramerName": mscLpOamEnetApplicationFramerName,
       "mscLpOamEnetSwitchoverOnFailure": mscLpOamEnetSwitchoverOnFailure,
       "mscLpOamEnetExtendedStatistics": mscLpOamEnetExtendedStatistics,
       "mscLpOamEnetAdminInfoTable": mscLpOamEnetAdminInfoTable,
       "mscLpOamEnetAdminInfoEntry": mscLpOamEnetAdminInfoEntry,
       "mscLpOamEnetVendor": mscLpOamEnetVendor,
       "mscLpOamEnetCommentText": mscLpOamEnetCommentText,
       "mscLpOamEnetStateTable": mscLpOamEnetStateTable,
       "mscLpOamEnetStateEntry": mscLpOamEnetStateEntry,
       "mscLpOamEnetAdminState": mscLpOamEnetAdminState,
       "mscLpOamEnetOperationalState": mscLpOamEnetOperationalState,
       "mscLpOamEnetUsageState": mscLpOamEnetUsageState,
       "mscLpOamEnetOperStatusTable": mscLpOamEnetOperStatusTable,
       "mscLpOamEnetOperStatusEntry": mscLpOamEnetOperStatusEntry,
       "mscLpOamEnetSnmpOperStatus": mscLpOamEnetSnmpOperStatus,
       "mscLpOamEnetOperTable": mscLpOamEnetOperTable,
       "mscLpOamEnetOperEntry": mscLpOamEnetOperEntry,
       "mscLpOamEnetMacAddress": mscLpOamEnetMacAddress,
       "mscLpOamEnetActiveStatus": mscLpOamEnetActiveStatus,
       "mscLpOamEnetStandbyStatus": mscLpOamEnetStandbyStatus,
       "mscLpOamEnetOamEnetStatsTable": mscLpOamEnetOamEnetStatsTable,
       "mscLpOamEnetOamEnetStatsEntry": mscLpOamEnetOamEnetStatsEntry,
       "mscLpOamEnetClearToSendSignalLoss": mscLpOamEnetClearToSendSignalLoss,
       "mscLpOamEnetFrameTooShort": mscLpOamEnetFrameTooShort,
       "mscLpOamEnetNumberOfRxCollisions": mscLpOamEnetNumberOfRxCollisions,
       "mscLpOamEnetLackOfResourcesDiscards": mscLpOamEnetLackOfResourcesDiscards,
       "mscLpOamEnetOverrunErrors": mscLpOamEnetOverrunErrors,
       "mscLpOamEnetStatsTable": mscLpOamEnetStatsTable,
       "mscLpOamEnetStatsEntry": mscLpOamEnetStatsEntry,
       "mscLpOamEnetAlignmentErrors": mscLpOamEnetAlignmentErrors,
       "mscLpOamEnetFcsErrors": mscLpOamEnetFcsErrors,
       "mscLpOamEnetSingleCollisionFrames": mscLpOamEnetSingleCollisionFrames,
       "mscLpOamEnetMultipleCollisionFrames": mscLpOamEnetMultipleCollisionFrames,
       "mscLpOamEnetSqeTestErrors": mscLpOamEnetSqeTestErrors,
       "mscLpOamEnetDeferredTransmissions": mscLpOamEnetDeferredTransmissions,
       "mscLpOamEnetLateCollisions": mscLpOamEnetLateCollisions,
       "mscLpOamEnetExcessiveCollisions": mscLpOamEnetExcessiveCollisions,
       "mscLpOamEnetMacTransmitErrors": mscLpOamEnetMacTransmitErrors,
       "mscLpOamEnetCarrierSenseErrors": mscLpOamEnetCarrierSenseErrors,
       "mscLpOamEnetFrameTooLongs": mscLpOamEnetFrameTooLongs,
       "mscLpOamEnetMacReceiveErrors": mscLpOamEnetMacReceiveErrors,
       "oamEthernetMIB": oamEthernetMIB,
       "oamEthernetGroup": oamEthernetGroup,
       "oamEthernetGroupCA": oamEthernetGroupCA,
       "oamEthernetGroupCA02": oamEthernetGroupCA02,
       "oamEthernetGroupCA02A": oamEthernetGroupCA02A,
       "oamEthernetCapabilities": oamEthernetCapabilities,
       "oamEthernetCapabilitiesCA": oamEthernetCapabilitiesCA,
       "oamEthernetCapabilitiesCA02": oamEthernetCapabilitiesCA02,
       "oamEthernetCapabilitiesCA02A": oamEthernetCapabilitiesCA02A}
)
