# SNMP MIB module (Nortel-Magellan-Passport-OamEthernetMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-OamEthernetMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:31:14 2024
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
 Integer32,
 InterfaceIndex,
 MacAddress,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
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

_LpOamEnet_ObjectIdentity = ObjectIdentity
lpOamEnet = _LpOamEnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27)
)
_LpOamEnetRowStatusTable_Object = MibTable
lpOamEnetRowStatusTable = _LpOamEnetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 1)
)
if mibBuilder.loadTexts:
    lpOamEnetRowStatusTable.setStatus("mandatory")
_LpOamEnetRowStatusEntry_Object = MibTableRow
lpOamEnetRowStatusEntry = _LpOamEnetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 1, 1)
)
lpOamEnetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetRowStatusEntry.setStatus("mandatory")
_LpOamEnetRowStatus_Type = RowStatus
_LpOamEnetRowStatus_Object = MibTableColumn
lpOamEnetRowStatus = _LpOamEnetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 1, 1, 1),
    _LpOamEnetRowStatus_Type()
)
lpOamEnetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetRowStatus.setStatus("mandatory")
_LpOamEnetComponentName_Type = DisplayString
_LpOamEnetComponentName_Object = MibTableColumn
lpOamEnetComponentName = _LpOamEnetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 1, 1, 2),
    _LpOamEnetComponentName_Type()
)
lpOamEnetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetComponentName.setStatus("mandatory")
_LpOamEnetStorageType_Type = StorageType
_LpOamEnetStorageType_Object = MibTableColumn
lpOamEnetStorageType = _LpOamEnetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 1, 1, 4),
    _LpOamEnetStorageType_Type()
)
lpOamEnetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetStorageType.setStatus("mandatory")


class _LpOamEnetIndex_Type(Integer32):
    """Custom type lpOamEnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LpOamEnetIndex_Type.__name__ = "Integer32"
_LpOamEnetIndex_Object = MibTableColumn
lpOamEnetIndex = _LpOamEnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 1, 1, 10),
    _LpOamEnetIndex_Type()
)
lpOamEnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpOamEnetIndex.setStatus("mandatory")
_LpOamEnetTest_ObjectIdentity = ObjectIdentity
lpOamEnetTest = _LpOamEnetTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2)
)
_LpOamEnetTestRowStatusTable_Object = MibTable
lpOamEnetTestRowStatusTable = _LpOamEnetTestRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 1)
)
if mibBuilder.loadTexts:
    lpOamEnetTestRowStatusTable.setStatus("mandatory")
_LpOamEnetTestRowStatusEntry_Object = MibTableRow
lpOamEnetTestRowStatusEntry = _LpOamEnetTestRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 1, 1)
)
lpOamEnetTestRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetTestIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetTestRowStatusEntry.setStatus("mandatory")
_LpOamEnetTestRowStatus_Type = RowStatus
_LpOamEnetTestRowStatus_Object = MibTableColumn
lpOamEnetTestRowStatus = _LpOamEnetTestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 1, 1, 1),
    _LpOamEnetTestRowStatus_Type()
)
lpOamEnetTestRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetTestRowStatus.setStatus("mandatory")
_LpOamEnetTestComponentName_Type = DisplayString
_LpOamEnetTestComponentName_Object = MibTableColumn
lpOamEnetTestComponentName = _LpOamEnetTestComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 1, 1, 2),
    _LpOamEnetTestComponentName_Type()
)
lpOamEnetTestComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetTestComponentName.setStatus("mandatory")
_LpOamEnetTestStorageType_Type = StorageType
_LpOamEnetTestStorageType_Object = MibTableColumn
lpOamEnetTestStorageType = _LpOamEnetTestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 1, 1, 4),
    _LpOamEnetTestStorageType_Type()
)
lpOamEnetTestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetTestStorageType.setStatus("mandatory")
_LpOamEnetTestIndex_Type = NonReplicated
_LpOamEnetTestIndex_Object = MibTableColumn
lpOamEnetTestIndex = _LpOamEnetTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 1, 1, 10),
    _LpOamEnetTestIndex_Type()
)
lpOamEnetTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lpOamEnetTestIndex.setStatus("mandatory")
_LpOamEnetTestOperTable_Object = MibTable
lpOamEnetTestOperTable = _LpOamEnetTestOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 10)
)
if mibBuilder.loadTexts:
    lpOamEnetTestOperTable.setStatus("mandatory")
_LpOamEnetTestOperEntry_Object = MibTableRow
lpOamEnetTestOperEntry = _LpOamEnetTestOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 10, 1)
)
lpOamEnetTestOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetTestIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetTestOperEntry.setStatus("mandatory")


class _LpOamEnetTestType_Type(Integer32):
    """Custom type lpOamEnetTestType based on Integer32"""
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


_LpOamEnetTestType_Type.__name__ = "Integer32"
_LpOamEnetTestType_Object = MibTableColumn
lpOamEnetTestType = _LpOamEnetTestType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 10, 1, 1),
    _LpOamEnetTestType_Type()
)
lpOamEnetTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetTestType.setStatus("mandatory")
_LpOamEnetTestResultsTable_Object = MibTable
lpOamEnetTestResultsTable = _LpOamEnetTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 11)
)
if mibBuilder.loadTexts:
    lpOamEnetTestResultsTable.setStatus("mandatory")
_LpOamEnetTestResultsEntry_Object = MibTableRow
lpOamEnetTestResultsEntry = _LpOamEnetTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 11, 1)
)
lpOamEnetTestResultsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetTestIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetTestResultsEntry.setStatus("mandatory")


class _LpOamEnetTestCauseOfTermination_Type(Integer32):
    """Custom type lpOamEnetTestCauseOfTermination based on Integer32"""
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


_LpOamEnetTestCauseOfTermination_Type.__name__ = "Integer32"
_LpOamEnetTestCauseOfTermination_Object = MibTableColumn
lpOamEnetTestCauseOfTermination = _LpOamEnetTestCauseOfTermination_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 11, 1, 1),
    _LpOamEnetTestCauseOfTermination_Type()
)
lpOamEnetTestCauseOfTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetTestCauseOfTermination.setStatus("mandatory")


class _LpOamEnetTestTestResult_Type(Integer32):
    """Custom type lpOamEnetTestTestResult based on Integer32"""
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


_LpOamEnetTestTestResult_Type.__name__ = "Integer32"
_LpOamEnetTestTestResult_Object = MibTableColumn
lpOamEnetTestTestResult = _LpOamEnetTestTestResult_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 2, 11, 1, 2),
    _LpOamEnetTestTestResult_Type()
)
lpOamEnetTestTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetTestTestResult.setStatus("mandatory")
_LpOamEnetCidDataTable_Object = MibTable
lpOamEnetCidDataTable = _LpOamEnetCidDataTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 10)
)
if mibBuilder.loadTexts:
    lpOamEnetCidDataTable.setStatus("mandatory")
_LpOamEnetCidDataEntry_Object = MibTableRow
lpOamEnetCidDataEntry = _LpOamEnetCidDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 10, 1)
)
lpOamEnetCidDataEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetCidDataEntry.setStatus("mandatory")


class _LpOamEnetCustomerIdentifier_Type(Unsigned32):
    """Custom type lpOamEnetCustomerIdentifier based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8191),
    )


_LpOamEnetCustomerIdentifier_Type.__name__ = "Unsigned32"
_LpOamEnetCustomerIdentifier_Object = MibTableColumn
lpOamEnetCustomerIdentifier = _LpOamEnetCustomerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 10, 1, 1),
    _LpOamEnetCustomerIdentifier_Type()
)
lpOamEnetCustomerIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetCustomerIdentifier.setStatus("mandatory")
_LpOamEnetIfEntryTable_Object = MibTable
lpOamEnetIfEntryTable = _LpOamEnetIfEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 11)
)
if mibBuilder.loadTexts:
    lpOamEnetIfEntryTable.setStatus("mandatory")
_LpOamEnetIfEntryEntry_Object = MibTableRow
lpOamEnetIfEntryEntry = _LpOamEnetIfEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 11, 1)
)
lpOamEnetIfEntryEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetIfEntryEntry.setStatus("mandatory")


class _LpOamEnetIfAdminStatus_Type(Integer32):
    """Custom type lpOamEnetIfAdminStatus based on Integer32"""
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


_LpOamEnetIfAdminStatus_Type.__name__ = "Integer32"
_LpOamEnetIfAdminStatus_Object = MibTableColumn
lpOamEnetIfAdminStatus = _LpOamEnetIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 11, 1, 1),
    _LpOamEnetIfAdminStatus_Type()
)
lpOamEnetIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetIfAdminStatus.setStatus("mandatory")


class _LpOamEnetIfIndex_Type(InterfaceIndex):
    """Custom type lpOamEnetIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LpOamEnetIfIndex_Type.__name__ = "InterfaceIndex"
_LpOamEnetIfIndex_Object = MibTableColumn
lpOamEnetIfIndex = _LpOamEnetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 11, 1, 2),
    _LpOamEnetIfIndex_Type()
)
lpOamEnetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetIfIndex.setStatus("mandatory")
_LpOamEnetProvTable_Object = MibTable
lpOamEnetProvTable = _LpOamEnetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 12)
)
if mibBuilder.loadTexts:
    lpOamEnetProvTable.setStatus("mandatory")
_LpOamEnetProvEntry_Object = MibTableRow
lpOamEnetProvEntry = _LpOamEnetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 12, 1)
)
lpOamEnetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetProvEntry.setStatus("mandatory")
_LpOamEnetApplicationFramerName_Type = Link
_LpOamEnetApplicationFramerName_Object = MibTableColumn
lpOamEnetApplicationFramerName = _LpOamEnetApplicationFramerName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 12, 1, 1),
    _LpOamEnetApplicationFramerName_Type()
)
lpOamEnetApplicationFramerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetApplicationFramerName.setStatus("mandatory")


class _LpOamEnetSwitchoverOnFailure_Type(Integer32):
    """Custom type lpOamEnetSwitchoverOnFailure based on Integer32"""
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


_LpOamEnetSwitchoverOnFailure_Type.__name__ = "Integer32"
_LpOamEnetSwitchoverOnFailure_Object = MibTableColumn
lpOamEnetSwitchoverOnFailure = _LpOamEnetSwitchoverOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 12, 1, 3),
    _LpOamEnetSwitchoverOnFailure_Type()
)
lpOamEnetSwitchoverOnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetSwitchoverOnFailure.setStatus("mandatory")


class _LpOamEnetExtendedStatistics_Type(Integer32):
    """Custom type lpOamEnetExtendedStatistics based on Integer32"""
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


_LpOamEnetExtendedStatistics_Type.__name__ = "Integer32"
_LpOamEnetExtendedStatistics_Object = MibTableColumn
lpOamEnetExtendedStatistics = _LpOamEnetExtendedStatistics_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 12, 1, 4),
    _LpOamEnetExtendedStatistics_Type()
)
lpOamEnetExtendedStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetExtendedStatistics.setStatus("mandatory")
_LpOamEnetAdminInfoTable_Object = MibTable
lpOamEnetAdminInfoTable = _LpOamEnetAdminInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 13)
)
if mibBuilder.loadTexts:
    lpOamEnetAdminInfoTable.setStatus("mandatory")
_LpOamEnetAdminInfoEntry_Object = MibTableRow
lpOamEnetAdminInfoEntry = _LpOamEnetAdminInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 13, 1)
)
lpOamEnetAdminInfoEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetAdminInfoEntry.setStatus("mandatory")


class _LpOamEnetVendor_Type(AsciiString):
    """Custom type lpOamEnetVendor based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_LpOamEnetVendor_Type.__name__ = "AsciiString"
_LpOamEnetVendor_Object = MibTableColumn
lpOamEnetVendor = _LpOamEnetVendor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 13, 1, 1),
    _LpOamEnetVendor_Type()
)
lpOamEnetVendor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetVendor.setStatus("mandatory")


class _LpOamEnetCommentText_Type(AsciiString):
    """Custom type lpOamEnetCommentText based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_LpOamEnetCommentText_Type.__name__ = "AsciiString"
_LpOamEnetCommentText_Object = MibTableColumn
lpOamEnetCommentText = _LpOamEnetCommentText_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 13, 1, 2),
    _LpOamEnetCommentText_Type()
)
lpOamEnetCommentText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lpOamEnetCommentText.setStatus("mandatory")
_LpOamEnetStateTable_Object = MibTable
lpOamEnetStateTable = _LpOamEnetStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 15)
)
if mibBuilder.loadTexts:
    lpOamEnetStateTable.setStatus("mandatory")
_LpOamEnetStateEntry_Object = MibTableRow
lpOamEnetStateEntry = _LpOamEnetStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 15, 1)
)
lpOamEnetStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetStateEntry.setStatus("mandatory")


class _LpOamEnetAdminState_Type(Integer32):
    """Custom type lpOamEnetAdminState based on Integer32"""
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


_LpOamEnetAdminState_Type.__name__ = "Integer32"
_LpOamEnetAdminState_Object = MibTableColumn
lpOamEnetAdminState = _LpOamEnetAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 15, 1, 1),
    _LpOamEnetAdminState_Type()
)
lpOamEnetAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetAdminState.setStatus("mandatory")


class _LpOamEnetOperationalState_Type(Integer32):
    """Custom type lpOamEnetOperationalState based on Integer32"""
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


_LpOamEnetOperationalState_Type.__name__ = "Integer32"
_LpOamEnetOperationalState_Object = MibTableColumn
lpOamEnetOperationalState = _LpOamEnetOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 15, 1, 2),
    _LpOamEnetOperationalState_Type()
)
lpOamEnetOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetOperationalState.setStatus("mandatory")


class _LpOamEnetUsageState_Type(Integer32):
    """Custom type lpOamEnetUsageState based on Integer32"""
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


_LpOamEnetUsageState_Type.__name__ = "Integer32"
_LpOamEnetUsageState_Object = MibTableColumn
lpOamEnetUsageState = _LpOamEnetUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 15, 1, 3),
    _LpOamEnetUsageState_Type()
)
lpOamEnetUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetUsageState.setStatus("mandatory")
_LpOamEnetOperStatusTable_Object = MibTable
lpOamEnetOperStatusTable = _LpOamEnetOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 16)
)
if mibBuilder.loadTexts:
    lpOamEnetOperStatusTable.setStatus("mandatory")
_LpOamEnetOperStatusEntry_Object = MibTableRow
lpOamEnetOperStatusEntry = _LpOamEnetOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 16, 1)
)
lpOamEnetOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetOperStatusEntry.setStatus("mandatory")


class _LpOamEnetSnmpOperStatus_Type(Integer32):
    """Custom type lpOamEnetSnmpOperStatus based on Integer32"""
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


_LpOamEnetSnmpOperStatus_Type.__name__ = "Integer32"
_LpOamEnetSnmpOperStatus_Object = MibTableColumn
lpOamEnetSnmpOperStatus = _LpOamEnetSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 16, 1, 1),
    _LpOamEnetSnmpOperStatus_Type()
)
lpOamEnetSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetSnmpOperStatus.setStatus("mandatory")
_LpOamEnetOperTable_Object = MibTable
lpOamEnetOperTable = _LpOamEnetOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 17)
)
if mibBuilder.loadTexts:
    lpOamEnetOperTable.setStatus("mandatory")
_LpOamEnetOperEntry_Object = MibTableRow
lpOamEnetOperEntry = _LpOamEnetOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 17, 1)
)
lpOamEnetOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetOperEntry.setStatus("mandatory")


class _LpOamEnetMacAddress_Type(MacAddress):
    """Custom type lpOamEnetMacAddress based on MacAddress"""
    subtypeSpec = MacAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LpOamEnetMacAddress_Type.__name__ = "MacAddress"
_LpOamEnetMacAddress_Object = MibTableColumn
lpOamEnetMacAddress = _LpOamEnetMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 17, 1, 1),
    _LpOamEnetMacAddress_Type()
)
lpOamEnetMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetMacAddress.setStatus("mandatory")


class _LpOamEnetActiveStatus_Type(Integer32):
    """Custom type lpOamEnetActiveStatus based on Integer32"""
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


_LpOamEnetActiveStatus_Type.__name__ = "Integer32"
_LpOamEnetActiveStatus_Object = MibTableColumn
lpOamEnetActiveStatus = _LpOamEnetActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 17, 1, 2),
    _LpOamEnetActiveStatus_Type()
)
lpOamEnetActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetActiveStatus.setStatus("mandatory")


class _LpOamEnetStandbyStatus_Type(Integer32):
    """Custom type lpOamEnetStandbyStatus based on Integer32"""
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


_LpOamEnetStandbyStatus_Type.__name__ = "Integer32"
_LpOamEnetStandbyStatus_Object = MibTableColumn
lpOamEnetStandbyStatus = _LpOamEnetStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 17, 1, 3),
    _LpOamEnetStandbyStatus_Type()
)
lpOamEnetStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetStandbyStatus.setStatus("mandatory")
_LpOamEnetOamEnetStatsTable_Object = MibTable
lpOamEnetOamEnetStatsTable = _LpOamEnetOamEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 18)
)
if mibBuilder.loadTexts:
    lpOamEnetOamEnetStatsTable.setStatus("mandatory")
_LpOamEnetOamEnetStatsEntry_Object = MibTableRow
lpOamEnetOamEnetStatsEntry = _LpOamEnetOamEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 18, 1)
)
lpOamEnetOamEnetStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetOamEnetStatsEntry.setStatus("mandatory")
_LpOamEnetClearToSendSignalLoss_Type = Counter32
_LpOamEnetClearToSendSignalLoss_Object = MibTableColumn
lpOamEnetClearToSendSignalLoss = _LpOamEnetClearToSendSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 18, 1, 14),
    _LpOamEnetClearToSendSignalLoss_Type()
)
lpOamEnetClearToSendSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetClearToSendSignalLoss.setStatus("mandatory")
_LpOamEnetFrameTooShort_Type = Counter32
_LpOamEnetFrameTooShort_Object = MibTableColumn
lpOamEnetFrameTooShort = _LpOamEnetFrameTooShort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 18, 1, 15),
    _LpOamEnetFrameTooShort_Type()
)
lpOamEnetFrameTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetFrameTooShort.setStatus("mandatory")
_LpOamEnetNumberOfRxCollisions_Type = Counter32
_LpOamEnetNumberOfRxCollisions_Object = MibTableColumn
lpOamEnetNumberOfRxCollisions = _LpOamEnetNumberOfRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 18, 1, 17),
    _LpOamEnetNumberOfRxCollisions_Type()
)
lpOamEnetNumberOfRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetNumberOfRxCollisions.setStatus("mandatory")
_LpOamEnetLackOfResourcesDiscards_Type = Counter32
_LpOamEnetLackOfResourcesDiscards_Object = MibTableColumn
lpOamEnetLackOfResourcesDiscards = _LpOamEnetLackOfResourcesDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 18, 1, 18),
    _LpOamEnetLackOfResourcesDiscards_Type()
)
lpOamEnetLackOfResourcesDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetLackOfResourcesDiscards.setStatus("mandatory")
_LpOamEnetOverrunErrors_Type = Counter32
_LpOamEnetOverrunErrors_Object = MibTableColumn
lpOamEnetOverrunErrors = _LpOamEnetOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 18, 1, 19),
    _LpOamEnetOverrunErrors_Type()
)
lpOamEnetOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetOverrunErrors.setStatus("mandatory")
_LpOamEnetStatsTable_Object = MibTable
lpOamEnetStatsTable = _LpOamEnetStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19)
)
if mibBuilder.loadTexts:
    lpOamEnetStatsTable.setStatus("mandatory")
_LpOamEnetStatsEntry_Object = MibTableRow
lpOamEnetStatsEntry = _LpOamEnetStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1)
)
lpOamEnetStatsEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-LogicalProcessorMIB", "lpIndex"),
    (0, "Nortel-Magellan-Passport-OamEthernetMIB", "lpOamEnetIndex"),
)
if mibBuilder.loadTexts:
    lpOamEnetStatsEntry.setStatus("mandatory")
_LpOamEnetAlignmentErrors_Type = Counter32
_LpOamEnetAlignmentErrors_Object = MibTableColumn
lpOamEnetAlignmentErrors = _LpOamEnetAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 2),
    _LpOamEnetAlignmentErrors_Type()
)
lpOamEnetAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetAlignmentErrors.setStatus("mandatory")
_LpOamEnetFcsErrors_Type = Counter32
_LpOamEnetFcsErrors_Object = MibTableColumn
lpOamEnetFcsErrors = _LpOamEnetFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 3),
    _LpOamEnetFcsErrors_Type()
)
lpOamEnetFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetFcsErrors.setStatus("mandatory")
_LpOamEnetSingleCollisionFrames_Type = Counter32
_LpOamEnetSingleCollisionFrames_Object = MibTableColumn
lpOamEnetSingleCollisionFrames = _LpOamEnetSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 4),
    _LpOamEnetSingleCollisionFrames_Type()
)
lpOamEnetSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetSingleCollisionFrames.setStatus("mandatory")
_LpOamEnetMultipleCollisionFrames_Type = Counter32
_LpOamEnetMultipleCollisionFrames_Object = MibTableColumn
lpOamEnetMultipleCollisionFrames = _LpOamEnetMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 5),
    _LpOamEnetMultipleCollisionFrames_Type()
)
lpOamEnetMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetMultipleCollisionFrames.setStatus("mandatory")
_LpOamEnetSqeTestErrors_Type = Counter32
_LpOamEnetSqeTestErrors_Object = MibTableColumn
lpOamEnetSqeTestErrors = _LpOamEnetSqeTestErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 6),
    _LpOamEnetSqeTestErrors_Type()
)
lpOamEnetSqeTestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetSqeTestErrors.setStatus("mandatory")
_LpOamEnetDeferredTransmissions_Type = Counter32
_LpOamEnetDeferredTransmissions_Object = MibTableColumn
lpOamEnetDeferredTransmissions = _LpOamEnetDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 7),
    _LpOamEnetDeferredTransmissions_Type()
)
lpOamEnetDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetDeferredTransmissions.setStatus("mandatory")
_LpOamEnetLateCollisions_Type = Counter32
_LpOamEnetLateCollisions_Object = MibTableColumn
lpOamEnetLateCollisions = _LpOamEnetLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 8),
    _LpOamEnetLateCollisions_Type()
)
lpOamEnetLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetLateCollisions.setStatus("mandatory")
_LpOamEnetExcessiveCollisions_Type = Counter32
_LpOamEnetExcessiveCollisions_Object = MibTableColumn
lpOamEnetExcessiveCollisions = _LpOamEnetExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 9),
    _LpOamEnetExcessiveCollisions_Type()
)
lpOamEnetExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetExcessiveCollisions.setStatus("mandatory")
_LpOamEnetMacTransmitErrors_Type = Counter32
_LpOamEnetMacTransmitErrors_Object = MibTableColumn
lpOamEnetMacTransmitErrors = _LpOamEnetMacTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 10),
    _LpOamEnetMacTransmitErrors_Type()
)
lpOamEnetMacTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetMacTransmitErrors.setStatus("mandatory")
_LpOamEnetCarrierSenseErrors_Type = Counter32
_LpOamEnetCarrierSenseErrors_Object = MibTableColumn
lpOamEnetCarrierSenseErrors = _LpOamEnetCarrierSenseErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 11),
    _LpOamEnetCarrierSenseErrors_Type()
)
lpOamEnetCarrierSenseErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetCarrierSenseErrors.setStatus("mandatory")
_LpOamEnetFrameTooLongs_Type = Counter32
_LpOamEnetFrameTooLongs_Object = MibTableColumn
lpOamEnetFrameTooLongs = _LpOamEnetFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 12),
    _LpOamEnetFrameTooLongs_Type()
)
lpOamEnetFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetFrameTooLongs.setStatus("mandatory")
_LpOamEnetMacReceiveErrors_Type = Counter32
_LpOamEnetMacReceiveErrors_Object = MibTableColumn
lpOamEnetMacReceiveErrors = _LpOamEnetMacReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 12, 27, 19, 1, 13),
    _LpOamEnetMacReceiveErrors_Type()
)
lpOamEnetMacReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lpOamEnetMacReceiveErrors.setStatus("mandatory")
_OamEthernetMIB_ObjectIdentity = ObjectIdentity
oamEthernetMIB = _OamEthernetMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79)
)
_OamEthernetGroup_ObjectIdentity = ObjectIdentity
oamEthernetGroup = _OamEthernetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 1)
)
_OamEthernetGroupCA_ObjectIdentity = ObjectIdentity
oamEthernetGroupCA = _OamEthernetGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 1, 27)
)
_OamEthernetGroupCA01_ObjectIdentity = ObjectIdentity
oamEthernetGroupCA01 = _OamEthernetGroupCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 1, 27, 2)
)
_OamEthernetGroupCA01A_ObjectIdentity = ObjectIdentity
oamEthernetGroupCA01A = _OamEthernetGroupCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 1, 27, 2, 2)
)
_OamEthernetCapabilities_ObjectIdentity = ObjectIdentity
oamEthernetCapabilities = _OamEthernetCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 3)
)
_OamEthernetCapabilitiesCA_ObjectIdentity = ObjectIdentity
oamEthernetCapabilitiesCA = _OamEthernetCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 3, 27)
)
_OamEthernetCapabilitiesCA01_ObjectIdentity = ObjectIdentity
oamEthernetCapabilitiesCA01 = _OamEthernetCapabilitiesCA01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 3, 27, 2)
)
_OamEthernetCapabilitiesCA01A_ObjectIdentity = ObjectIdentity
oamEthernetCapabilitiesCA01A = _OamEthernetCapabilitiesCA01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 79, 3, 27, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-OamEthernetMIB",
    **{"lpOamEnet": lpOamEnet,
       "lpOamEnetRowStatusTable": lpOamEnetRowStatusTable,
       "lpOamEnetRowStatusEntry": lpOamEnetRowStatusEntry,
       "lpOamEnetRowStatus": lpOamEnetRowStatus,
       "lpOamEnetComponentName": lpOamEnetComponentName,
       "lpOamEnetStorageType": lpOamEnetStorageType,
       "lpOamEnetIndex": lpOamEnetIndex,
       "lpOamEnetTest": lpOamEnetTest,
       "lpOamEnetTestRowStatusTable": lpOamEnetTestRowStatusTable,
       "lpOamEnetTestRowStatusEntry": lpOamEnetTestRowStatusEntry,
       "lpOamEnetTestRowStatus": lpOamEnetTestRowStatus,
       "lpOamEnetTestComponentName": lpOamEnetTestComponentName,
       "lpOamEnetTestStorageType": lpOamEnetTestStorageType,
       "lpOamEnetTestIndex": lpOamEnetTestIndex,
       "lpOamEnetTestOperTable": lpOamEnetTestOperTable,
       "lpOamEnetTestOperEntry": lpOamEnetTestOperEntry,
       "lpOamEnetTestType": lpOamEnetTestType,
       "lpOamEnetTestResultsTable": lpOamEnetTestResultsTable,
       "lpOamEnetTestResultsEntry": lpOamEnetTestResultsEntry,
       "lpOamEnetTestCauseOfTermination": lpOamEnetTestCauseOfTermination,
       "lpOamEnetTestTestResult": lpOamEnetTestTestResult,
       "lpOamEnetCidDataTable": lpOamEnetCidDataTable,
       "lpOamEnetCidDataEntry": lpOamEnetCidDataEntry,
       "lpOamEnetCustomerIdentifier": lpOamEnetCustomerIdentifier,
       "lpOamEnetIfEntryTable": lpOamEnetIfEntryTable,
       "lpOamEnetIfEntryEntry": lpOamEnetIfEntryEntry,
       "lpOamEnetIfAdminStatus": lpOamEnetIfAdminStatus,
       "lpOamEnetIfIndex": lpOamEnetIfIndex,
       "lpOamEnetProvTable": lpOamEnetProvTable,
       "lpOamEnetProvEntry": lpOamEnetProvEntry,
       "lpOamEnetApplicationFramerName": lpOamEnetApplicationFramerName,
       "lpOamEnetSwitchoverOnFailure": lpOamEnetSwitchoverOnFailure,
       "lpOamEnetExtendedStatistics": lpOamEnetExtendedStatistics,
       "lpOamEnetAdminInfoTable": lpOamEnetAdminInfoTable,
       "lpOamEnetAdminInfoEntry": lpOamEnetAdminInfoEntry,
       "lpOamEnetVendor": lpOamEnetVendor,
       "lpOamEnetCommentText": lpOamEnetCommentText,
       "lpOamEnetStateTable": lpOamEnetStateTable,
       "lpOamEnetStateEntry": lpOamEnetStateEntry,
       "lpOamEnetAdminState": lpOamEnetAdminState,
       "lpOamEnetOperationalState": lpOamEnetOperationalState,
       "lpOamEnetUsageState": lpOamEnetUsageState,
       "lpOamEnetOperStatusTable": lpOamEnetOperStatusTable,
       "lpOamEnetOperStatusEntry": lpOamEnetOperStatusEntry,
       "lpOamEnetSnmpOperStatus": lpOamEnetSnmpOperStatus,
       "lpOamEnetOperTable": lpOamEnetOperTable,
       "lpOamEnetOperEntry": lpOamEnetOperEntry,
       "lpOamEnetMacAddress": lpOamEnetMacAddress,
       "lpOamEnetActiveStatus": lpOamEnetActiveStatus,
       "lpOamEnetStandbyStatus": lpOamEnetStandbyStatus,
       "lpOamEnetOamEnetStatsTable": lpOamEnetOamEnetStatsTable,
       "lpOamEnetOamEnetStatsEntry": lpOamEnetOamEnetStatsEntry,
       "lpOamEnetClearToSendSignalLoss": lpOamEnetClearToSendSignalLoss,
       "lpOamEnetFrameTooShort": lpOamEnetFrameTooShort,
       "lpOamEnetNumberOfRxCollisions": lpOamEnetNumberOfRxCollisions,
       "lpOamEnetLackOfResourcesDiscards": lpOamEnetLackOfResourcesDiscards,
       "lpOamEnetOverrunErrors": lpOamEnetOverrunErrors,
       "lpOamEnetStatsTable": lpOamEnetStatsTable,
       "lpOamEnetStatsEntry": lpOamEnetStatsEntry,
       "lpOamEnetAlignmentErrors": lpOamEnetAlignmentErrors,
       "lpOamEnetFcsErrors": lpOamEnetFcsErrors,
       "lpOamEnetSingleCollisionFrames": lpOamEnetSingleCollisionFrames,
       "lpOamEnetMultipleCollisionFrames": lpOamEnetMultipleCollisionFrames,
       "lpOamEnetSqeTestErrors": lpOamEnetSqeTestErrors,
       "lpOamEnetDeferredTransmissions": lpOamEnetDeferredTransmissions,
       "lpOamEnetLateCollisions": lpOamEnetLateCollisions,
       "lpOamEnetExcessiveCollisions": lpOamEnetExcessiveCollisions,
       "lpOamEnetMacTransmitErrors": lpOamEnetMacTransmitErrors,
       "lpOamEnetCarrierSenseErrors": lpOamEnetCarrierSenseErrors,
       "lpOamEnetFrameTooLongs": lpOamEnetFrameTooLongs,
       "lpOamEnetMacReceiveErrors": lpOamEnetMacReceiveErrors,
       "oamEthernetMIB": oamEthernetMIB,
       "oamEthernetGroup": oamEthernetGroup,
       "oamEthernetGroupCA": oamEthernetGroupCA,
       "oamEthernetGroupCA01": oamEthernetGroupCA01,
       "oamEthernetGroupCA01A": oamEthernetGroupCA01A,
       "oamEthernetCapabilities": oamEthernetCapabilities,
       "oamEthernetCapabilitiesCA": oamEthernetCapabilitiesCA,
       "oamEthernetCapabilitiesCA01": oamEthernetCapabilitiesCA01,
       "oamEthernetCapabilitiesCA01A": oamEthernetCapabilitiesCA01A}
)
