# SNMP MIB module (FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:54 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraFileMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FileTable_Object = MibTable
fileTable = _FileTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1)
)
if mibBuilder.loadTexts:
    fileTable.setStatus("current")
_FileTableEntry_Object = MibTableRow
fileTableEntry = _FileTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1)
)
fileTableEntry.setIndexNames(
    (0, "FILE-MIB", "fileOwnerString"),
    (0, "FILE-MIB", "fileSequenceNumber"),
)
if mibBuilder.loadTexts:
    fileTableEntry.setStatus("current")
_FileOwnerString_Type = DisplayString
_FileOwnerString_Object = MibTableColumn
fileOwnerString = _FileOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 1),
    _FileOwnerString_Type()
)
fileOwnerString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileOwnerString.setStatus("current")
_FileSequenceNumber_Type = Integer32
_FileSequenceNumber_Object = MibTableColumn
fileSequenceNumber = _FileSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 2),
    _FileSequenceNumber_Type()
)
fileSequenceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSequenceNumber.setStatus("current")
_FileSrcFile_Type = DisplayString
_FileSrcFile_Object = MibTableColumn
fileSrcFile = _FileSrcFile_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 3),
    _FileSrcFile_Type()
)
fileSrcFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSrcFile.setStatus("current")
_FileDestFile_Type = DisplayString
_FileDestFile_Object = MibTableColumn
fileDestFile = _FileDestFile_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 4),
    _FileDestFile_Type()
)
fileDestFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileDestFile.setStatus("current")
_FileHostIpAddr_Type = IpAddress
_FileHostIpAddr_Object = MibTableColumn
fileHostIpAddr = _FileHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 5),
    _FileHostIpAddr_Type()
)
fileHostIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileHostIpAddr.setStatus("current")


class _FileLocationOfFile_Type(Integer32):
    """Custom type fileLocationOfFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ic", 1),
          ("ncm", 2),
          ("none", 3))
    )


_FileLocationOfFile_Type.__name__ = "Integer32"
_FileLocationOfFile_Object = MibTableColumn
fileLocationOfFile = _FileLocationOfFile_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 6),
    _FileLocationOfFile_Type()
)
fileLocationOfFile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileLocationOfFile.setStatus("current")
_FileSlotNumber_Type = Integer32
_FileSlotNumber_Object = MibTableColumn
fileSlotNumber = _FileSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 7),
    _FileSlotNumber_Type()
)
fileSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSlotNumber.setStatus("current")


class _FileUploadFileType_Type(Integer32):
    """Custom type fileUploadFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eventlog", 1),
          ("flashfile", 2),
          ("none", 3))
    )


_FileUploadFileType_Type.__name__ = "Integer32"
_FileUploadFileType_Object = MibTableColumn
fileUploadFileType = _FileUploadFileType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 8),
    _FileUploadFileType_Type()
)
fileUploadFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileUploadFileType.setStatus("current")


class _FilePerformAction_Type(Integer32):
    """Custom type filePerformAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("copy", 1),
          ("download", 2),
          ("format", 3),
          ("list", 4),
          ("remove", 5),
          ("upload", 6))
    )


_FilePerformAction_Type.__name__ = "Integer32"
_FilePerformAction_Object = MibTableColumn
filePerformAction = _FilePerformAction_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 9),
    _FilePerformAction_Type()
)
filePerformAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filePerformAction.setStatus("current")


class _FileActionStatus_Type(Integer32):
    """Custom type fileActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("inProgress", 3),
          ("success", 1))
    )


_FileActionStatus_Type.__name__ = "Integer32"
_FileActionStatus_Object = MibTableColumn
fileActionStatus = _FileActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 10),
    _FileActionStatus_Type()
)
fileActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileActionStatus.setStatus("current")
_FileListData_Type = DisplayString
_FileListData_Object = MibTableColumn
fileListData = _FileListData_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 11),
    _FileListData_Type()
)
fileListData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileListData.setStatus("current")
_FileRowStatus_Type = RowStatus
_FileRowStatus_Object = MibTableColumn
fileRowStatus = _FileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 120, 1, 1, 12),
    _FileRowStatus_Type()
)
fileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FILE-MIB",
    **{"tiaraFileMib": tiaraFileMib,
       "fileTable": fileTable,
       "fileTableEntry": fileTableEntry,
       "fileOwnerString": fileOwnerString,
       "fileSequenceNumber": fileSequenceNumber,
       "fileSrcFile": fileSrcFile,
       "fileDestFile": fileDestFile,
       "fileHostIpAddr": fileHostIpAddr,
       "fileLocationOfFile": fileLocationOfFile,
       "fileSlotNumber": fileSlotNumber,
       "fileUploadFileType": fileUploadFileType,
       "filePerformAction": filePerformAction,
       "fileActionStatus": fileActionStatus,
       "fileListData": fileListData,
       "fileRowStatus": fileRowStatus}
)
