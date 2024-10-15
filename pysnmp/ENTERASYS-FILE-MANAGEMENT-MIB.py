# SNMP MIB module (ENTERASYS-FILE-MANAGEMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-FILE-MANAGEMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:51 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(hrFSIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrFSIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

etsysFileManagementMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15)
)
etsysFileManagementMIB.setRevisions(
        ("2001-12-03 19:54",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysFileTransfer_ObjectIdentity = ObjectIdentity
etsysFileTransfer = _EtsysFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1)
)


class _EtsysFileTransferRequestLimit_Type(Unsigned32):
    """Custom type etsysFileTransferRequestLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFileTransferRequestLimit_Type.__name__ = "Unsigned32"
_EtsysFileTransferRequestLimit_Object = MibScalar
etsysFileTransferRequestLimit = _EtsysFileTransferRequestLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 1),
    _EtsysFileTransferRequestLimit_Type()
)
etsysFileTransferRequestLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestLimit.setStatus("current")
_EtsysFileTransferRequestsCurrent_Type = Gauge32
_EtsysFileTransferRequestsCurrent_Object = MibScalar
etsysFileTransferRequestsCurrent = _EtsysFileTransferRequestsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 2),
    _EtsysFileTransferRequestsCurrent_Type()
)
etsysFileTransferRequestsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestsCurrent.setStatus("current")
_EtsysFileTransferRequestsCompleted_Type = Counter32
_EtsysFileTransferRequestsCompleted_Object = MibScalar
etsysFileTransferRequestsCompleted = _EtsysFileTransferRequestsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 3),
    _EtsysFileTransferRequestsCompleted_Type()
)
etsysFileTransferRequestsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestsCompleted.setStatus("current")


class _EtsysFileTransferRequestSupportedURLs_Type(Bits):
    """Custom type etsysFileTransferRequestSupportedURLs based on Bits"""
    namedValues = NamedValues(
        *(("etsysFileTransferFile", 4),
          ("etsysFileTransferFtp", 0),
          ("etsysFileTransferHttp", 2),
          ("etsysFileTransferRcp", 1),
          ("etsysFileTransferTftp", 3))
    )

_EtsysFileTransferRequestSupportedURLs_Type.__name__ = "Bits"
_EtsysFileTransferRequestSupportedURLs_Object = MibScalar
etsysFileTransferRequestSupportedURLs = _EtsysFileTransferRequestSupportedURLs_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 4),
    _EtsysFileTransferRequestSupportedURLs_Type()
)
etsysFileTransferRequestSupportedURLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestSupportedURLs.setStatus("current")


class _EtsysFileTransferRequestNextAvailableIndex_Type(Unsigned32):
    """Custom type etsysFileTransferRequestNextAvailableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFileTransferRequestNextAvailableIndex_Type.__name__ = "Unsigned32"
_EtsysFileTransferRequestNextAvailableIndex_Object = MibScalar
etsysFileTransferRequestNextAvailableIndex = _EtsysFileTransferRequestNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 5),
    _EtsysFileTransferRequestNextAvailableIndex_Type()
)
etsysFileTransferRequestNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestNextAvailableIndex.setStatus("current")
_EtsysFileTransferRequestTable_Object = MibTable
etsysFileTransferRequestTable = _EtsysFileTransferRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6)
)
if mibBuilder.loadTexts:
    etsysFileTransferRequestTable.setStatus("current")
_EtsysFileTransferRequestEntry_Object = MibTableRow
etsysFileTransferRequestEntry = _EtsysFileTransferRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1)
)
etsysFileTransferRequestEntry.setIndexNames(
    (0, "ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestIndex"),
)
if mibBuilder.loadTexts:
    etsysFileTransferRequestEntry.setStatus("current")


class _EtsysFileTransferRequestIndex_Type(Unsigned32):
    """Custom type etsysFileTransferRequestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysFileTransferRequestIndex_Type.__name__ = "Unsigned32"
_EtsysFileTransferRequestIndex_Object = MibTableColumn
etsysFileTransferRequestIndex = _EtsysFileTransferRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 1),
    _EtsysFileTransferRequestIndex_Type()
)
etsysFileTransferRequestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFileTransferRequestIndex.setStatus("current")
_EtsysFileTransferRequestSource_Type = DisplayString
_EtsysFileTransferRequestSource_Object = MibTableColumn
etsysFileTransferRequestSource = _EtsysFileTransferRequestSource_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 2),
    _EtsysFileTransferRequestSource_Type()
)
etsysFileTransferRequestSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFileTransferRequestSource.setStatus("current")
_EtsysFileTransferRequestDestination_Type = DisplayString
_EtsysFileTransferRequestDestination_Object = MibTableColumn
etsysFileTransferRequestDestination = _EtsysFileTransferRequestDestination_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 3),
    _EtsysFileTransferRequestDestination_Type()
)
etsysFileTransferRequestDestination.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFileTransferRequestDestination.setStatus("current")


class _EtsysFileTransferRequestOperStatus_Type(Integer32):
    """Custom type etsysFileTransferRequestOperStatus based on Integer32"""
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
        *(("failure", 5),
          ("inactive", 1),
          ("pending", 2),
          ("running", 3),
          ("success", 4))
    )


_EtsysFileTransferRequestOperStatus_Type.__name__ = "Integer32"
_EtsysFileTransferRequestOperStatus_Object = MibTableColumn
etsysFileTransferRequestOperStatus = _EtsysFileTransferRequestOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 4),
    _EtsysFileTransferRequestOperStatus_Type()
)
etsysFileTransferRequestOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestOperStatus.setStatus("current")


class _EtsysFileTransferRequestEnqueuedTime_Type(DateAndTime):
    """Custom type etsysFileTransferRequestEnqueuedTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_EtsysFileTransferRequestEnqueuedTime_Object = MibTableColumn
etsysFileTransferRequestEnqueuedTime = _EtsysFileTransferRequestEnqueuedTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 5),
    _EtsysFileTransferRequestEnqueuedTime_Type()
)
etsysFileTransferRequestEnqueuedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestEnqueuedTime.setStatus("current")


class _EtsysFileTransferRequestCompletionTime_Type(DateAndTime):
    """Custom type etsysFileTransferRequestCompletionTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_EtsysFileTransferRequestCompletionTime_Object = MibTableColumn
etsysFileTransferRequestCompletionTime = _EtsysFileTransferRequestCompletionTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 6),
    _EtsysFileTransferRequestCompletionTime_Type()
)
etsysFileTransferRequestCompletionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestCompletionTime.setStatus("current")


class _EtsysFileTransferRequestBytesTransferred_Type(Integer32):
    """Custom type etsysFileTransferRequestBytesTransferred based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_EtsysFileTransferRequestBytesTransferred_Type.__name__ = "Integer32"
_EtsysFileTransferRequestBytesTransferred_Object = MibTableColumn
etsysFileTransferRequestBytesTransferred = _EtsysFileTransferRequestBytesTransferred_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 7),
    _EtsysFileTransferRequestBytesTransferred_Type()
)
etsysFileTransferRequestBytesTransferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestBytesTransferred.setStatus("current")


class _EtsysFileTransferRequestErrorDescription_Type(SnmpAdminString):
    """Custom type etsysFileTransferRequestErrorDescription based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysFileTransferRequestErrorDescription_Object = MibTableColumn
etsysFileTransferRequestErrorDescription = _EtsysFileTransferRequestErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 8),
    _EtsysFileTransferRequestErrorDescription_Type()
)
etsysFileTransferRequestErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestErrorDescription.setStatus("current")


class _EtsysFileTransferRequestStorageType_Type(StorageType):
    """Custom type etsysFileTransferRequestStorageType based on StorageType"""


_EtsysFileTransferRequestStorageType_Object = MibTableColumn
etsysFileTransferRequestStorageType = _EtsysFileTransferRequestStorageType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 9),
    _EtsysFileTransferRequestStorageType_Type()
)
etsysFileTransferRequestStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileTransferRequestStorageType.setStatus("current")
_EtsysFileTransferRequestRowStatus_Type = RowStatus
_EtsysFileTransferRequestRowStatus_Object = MibTableColumn
etsysFileTransferRequestRowStatus = _EtsysFileTransferRequestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 1, 6, 1, 10),
    _EtsysFileTransferRequestRowStatus_Type()
)
etsysFileTransferRequestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFileTransferRequestRowStatus.setStatus("current")
_EtsysFileListing_ObjectIdentity = ObjectIdentity
etsysFileListing = _EtsysFileListing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2)
)
_EtsysFileListingTable_Object = MibTable
etsysFileListingTable = _EtsysFileListingTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1)
)
if mibBuilder.loadTexts:
    etsysFileListingTable.setStatus("current")
_EtsysFileListingEntry_Object = MibTableRow
etsysFileListingEntry = _EtsysFileListingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1)
)
etsysFileListingEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrFSIndex"),
    (0, "ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingIndex"),
)
if mibBuilder.loadTexts:
    etsysFileListingEntry.setStatus("current")
_EtsysFileListingIndex_Type = Unsigned32
_EtsysFileListingIndex_Object = MibTableColumn
etsysFileListingIndex = _EtsysFileListingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 1),
    _EtsysFileListingIndex_Type()
)
etsysFileListingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFileListingIndex.setStatus("current")
_EtsysFileListingFileName_Type = DisplayString
_EtsysFileListingFileName_Object = MibTableColumn
etsysFileListingFileName = _EtsysFileListingFileName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 2),
    _EtsysFileListingFileName_Type()
)
etsysFileListingFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileListingFileName.setStatus("current")


class _EtsysFileListingFileSize_Type(Unsigned32):
    """Custom type etsysFileListingFileSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFileListingFileSize_Type.__name__ = "Unsigned32"
_EtsysFileListingFileSize_Object = MibTableColumn
etsysFileListingFileSize = _EtsysFileListingFileSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 3),
    _EtsysFileListingFileSize_Type()
)
etsysFileListingFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileListingFileSize.setStatus("current")


class _EtsysFileListingFileType_Type(Integer32):
    """Custom type etsysFileListingFileType based on Integer32"""
    defaultValue = 1

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
        *(("directory", 2),
          ("ordinary-file", 3),
          ("symbolic-link", 4),
          ("unsupported", 1))
    )


_EtsysFileListingFileType_Type.__name__ = "Integer32"
_EtsysFileListingFileType_Object = MibTableColumn
etsysFileListingFileType = _EtsysFileListingFileType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 4),
    _EtsysFileListingFileType_Type()
)
etsysFileListingFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileListingFileType.setStatus("current")


class _EtsysFileListingFileDate_Type(DateAndTime):
    """Custom type etsysFileListingFileDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_EtsysFileListingFileDate_Object = MibTableColumn
etsysFileListingFileDate = _EtsysFileListingFileDate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 5),
    _EtsysFileListingFileDate_Type()
)
etsysFileListingFileDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileListingFileDate.setStatus("current")


class _EtsysFileListingFileOrigin_Type(DisplayString):
    """Custom type etsysFileListingFileOrigin based on DisplayString"""
    defaultHexValue = ""


_EtsysFileListingFileOrigin_Object = MibTableColumn
etsysFileListingFileOrigin = _EtsysFileListingFileOrigin_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 2, 1, 1, 6),
    _EtsysFileListingFileOrigin_Type()
)
etsysFileListingFileOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileListingFileOrigin.setStatus("current")
_EtsysFileOperation_ObjectIdentity = ObjectIdentity
etsysFileOperation = _EtsysFileOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3)
)


class _EtsysFileOperationLimit_Type(Unsigned32):
    """Custom type etsysFileOperationLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFileOperationLimit_Type.__name__ = "Unsigned32"
_EtsysFileOperationLimit_Object = MibScalar
etsysFileOperationLimit = _EtsysFileOperationLimit_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 1),
    _EtsysFileOperationLimit_Type()
)
etsysFileOperationLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileOperationLimit.setStatus("current")
_EtsysFileOperationsCurrent_Type = Gauge32
_EtsysFileOperationsCurrent_Object = MibScalar
etsysFileOperationsCurrent = _EtsysFileOperationsCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 2),
    _EtsysFileOperationsCurrent_Type()
)
etsysFileOperationsCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileOperationsCurrent.setStatus("current")
_EtsysFileOperationsCompleted_Type = Counter32
_EtsysFileOperationsCompleted_Object = MibScalar
etsysFileOperationsCompleted = _EtsysFileOperationsCompleted_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 3),
    _EtsysFileOperationsCompleted_Type()
)
etsysFileOperationsCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileOperationsCompleted.setStatus("current")


class _EtsysFileOperationNextAvailableIndex_Type(Unsigned32):
    """Custom type etsysFileOperationNextAvailableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFileOperationNextAvailableIndex_Type.__name__ = "Unsigned32"
_EtsysFileOperationNextAvailableIndex_Object = MibScalar
etsysFileOperationNextAvailableIndex = _EtsysFileOperationNextAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 4),
    _EtsysFileOperationNextAvailableIndex_Type()
)
etsysFileOperationNextAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileOperationNextAvailableIndex.setStatus("current")
_EtsysFileOperationTable_Object = MibTable
etsysFileOperationTable = _EtsysFileOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5)
)
if mibBuilder.loadTexts:
    etsysFileOperationTable.setStatus("current")
_EtsysFileOperationEntry_Object = MibTableRow
etsysFileOperationEntry = _EtsysFileOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1)
)
etsysFileOperationEntry.setIndexNames(
    (0, "ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationIndex"),
)
if mibBuilder.loadTexts:
    etsysFileOperationEntry.setStatus("current")


class _EtsysFileOperationIndex_Type(Unsigned32):
    """Custom type etsysFileOperationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysFileOperationIndex_Type.__name__ = "Unsigned32"
_EtsysFileOperationIndex_Object = MibTableColumn
etsysFileOperationIndex = _EtsysFileOperationIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 1),
    _EtsysFileOperationIndex_Type()
)
etsysFileOperationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysFileOperationIndex.setStatus("current")


class _EtsysFileOperationType_Type(Integer32):
    """Custom type etsysFileOperationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("rename", 2))
    )


_EtsysFileOperationType_Type.__name__ = "Integer32"
_EtsysFileOperationType_Object = MibTableColumn
etsysFileOperationType = _EtsysFileOperationType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 2),
    _EtsysFileOperationType_Type()
)
etsysFileOperationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFileOperationType.setStatus("current")


class _EtsysFileOperationFileName_Type(SnmpAdminString):
    """Custom type etsysFileOperationFileName based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysFileOperationFileName_Object = MibTableColumn
etsysFileOperationFileName = _EtsysFileOperationFileName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 3),
    _EtsysFileOperationFileName_Type()
)
etsysFileOperationFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFileOperationFileName.setStatus("current")


class _EtsysFileOperationFileNewName_Type(SnmpAdminString):
    """Custom type etsysFileOperationFileNewName based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysFileOperationFileNewName_Object = MibTableColumn
etsysFileOperationFileNewName = _EtsysFileOperationFileNewName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 4),
    _EtsysFileOperationFileNewName_Type()
)
etsysFileOperationFileNewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFileOperationFileNewName.setStatus("current")


class _EtsysFileOperationErrorDescription_Type(SnmpAdminString):
    """Custom type etsysFileOperationErrorDescription based on SnmpAdminString"""
    defaultHexValue = ""


_EtsysFileOperationErrorDescription_Object = MibTableColumn
etsysFileOperationErrorDescription = _EtsysFileOperationErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 5),
    _EtsysFileOperationErrorDescription_Type()
)
etsysFileOperationErrorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysFileOperationErrorDescription.setStatus("current")
_EtsysFileOperationRowStatus_Type = RowStatus
_EtsysFileOperationRowStatus_Object = MibTableColumn
etsysFileOperationRowStatus = _EtsysFileOperationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 3, 5, 1, 6),
    _EtsysFileOperationRowStatus_Type()
)
etsysFileOperationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysFileOperationRowStatus.setStatus("current")
_EtsysFileConformance_ObjectIdentity = ObjectIdentity
etsysFileConformance = _EtsysFileConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4)
)
_EtsysFileGroups_ObjectIdentity = ObjectIdentity
etsysFileGroups = _EtsysFileGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1)
)
_EtsysFileCompliances_ObjectIdentity = ObjectIdentity
etsysFileCompliances = _EtsysFileCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 2)
)

# Managed Objects groups

etsysFileTransferGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1, 1)
)
etsysFileTransferGroup.setObjects(
      *(("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestLimit"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestsCurrent"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestsCompleted"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestSupportedURLs"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestNextAvailableIndex"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestSource"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestDestination"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestOperStatus"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestEnqueuedTime"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestCompletionTime"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestBytesTransferred"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestErrorDescription"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestStorageType"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileTransferRequestRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFileTransferGroup.setStatus("current")

etsysFileListingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1, 2)
)
etsysFileListingGroup.setObjects(
      *(("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileName"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileSize"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileType"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileDate"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileListingFileOrigin"))
)
if mibBuilder.loadTexts:
    etsysFileListingGroup.setStatus("current")

etsysFileOperationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 1, 3)
)
etsysFileOperationGroup.setObjects(
      *(("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationLimit"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationsCurrent"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationsCompleted"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationNextAvailableIndex"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationType"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationFileName"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationFileNewName"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationErrorDescription"),
        ("ENTERASYS-FILE-MANAGEMENT-MIB", "etsysFileOperationRowStatus"))
)
if mibBuilder.loadTexts:
    etsysFileOperationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysFileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 15, 4, 2, 1)
)
if mibBuilder.loadTexts:
    etsysFileCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-FILE-MANAGEMENT-MIB",
    **{"etsysFileManagementMIB": etsysFileManagementMIB,
       "etsysFileTransfer": etsysFileTransfer,
       "etsysFileTransferRequestLimit": etsysFileTransferRequestLimit,
       "etsysFileTransferRequestsCurrent": etsysFileTransferRequestsCurrent,
       "etsysFileTransferRequestsCompleted": etsysFileTransferRequestsCompleted,
       "etsysFileTransferRequestSupportedURLs": etsysFileTransferRequestSupportedURLs,
       "etsysFileTransferRequestNextAvailableIndex": etsysFileTransferRequestNextAvailableIndex,
       "etsysFileTransferRequestTable": etsysFileTransferRequestTable,
       "etsysFileTransferRequestEntry": etsysFileTransferRequestEntry,
       "etsysFileTransferRequestIndex": etsysFileTransferRequestIndex,
       "etsysFileTransferRequestSource": etsysFileTransferRequestSource,
       "etsysFileTransferRequestDestination": etsysFileTransferRequestDestination,
       "etsysFileTransferRequestOperStatus": etsysFileTransferRequestOperStatus,
       "etsysFileTransferRequestEnqueuedTime": etsysFileTransferRequestEnqueuedTime,
       "etsysFileTransferRequestCompletionTime": etsysFileTransferRequestCompletionTime,
       "etsysFileTransferRequestBytesTransferred": etsysFileTransferRequestBytesTransferred,
       "etsysFileTransferRequestErrorDescription": etsysFileTransferRequestErrorDescription,
       "etsysFileTransferRequestStorageType": etsysFileTransferRequestStorageType,
       "etsysFileTransferRequestRowStatus": etsysFileTransferRequestRowStatus,
       "etsysFileListing": etsysFileListing,
       "etsysFileListingTable": etsysFileListingTable,
       "etsysFileListingEntry": etsysFileListingEntry,
       "etsysFileListingIndex": etsysFileListingIndex,
       "etsysFileListingFileName": etsysFileListingFileName,
       "etsysFileListingFileSize": etsysFileListingFileSize,
       "etsysFileListingFileType": etsysFileListingFileType,
       "etsysFileListingFileDate": etsysFileListingFileDate,
       "etsysFileListingFileOrigin": etsysFileListingFileOrigin,
       "etsysFileOperation": etsysFileOperation,
       "etsysFileOperationLimit": etsysFileOperationLimit,
       "etsysFileOperationsCurrent": etsysFileOperationsCurrent,
       "etsysFileOperationsCompleted": etsysFileOperationsCompleted,
       "etsysFileOperationNextAvailableIndex": etsysFileOperationNextAvailableIndex,
       "etsysFileOperationTable": etsysFileOperationTable,
       "etsysFileOperationEntry": etsysFileOperationEntry,
       "etsysFileOperationIndex": etsysFileOperationIndex,
       "etsysFileOperationType": etsysFileOperationType,
       "etsysFileOperationFileName": etsysFileOperationFileName,
       "etsysFileOperationFileNewName": etsysFileOperationFileNewName,
       "etsysFileOperationErrorDescription": etsysFileOperationErrorDescription,
       "etsysFileOperationRowStatus": etsysFileOperationRowStatus,
       "etsysFileConformance": etsysFileConformance,
       "etsysFileGroups": etsysFileGroups,
       "etsysFileTransferGroup": etsysFileTransferGroup,
       "etsysFileListingGroup": etsysFileListingGroup,
       "etsysFileOperationGroup": etsysFileOperationGroup,
       "etsysFileCompliances": etsysFileCompliances,
       "etsysFileCompliance": etsysFileCompliance}
)
