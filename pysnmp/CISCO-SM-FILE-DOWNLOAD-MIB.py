# SNMP MIB module (CISCO-SM-FILE-DOWNLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SM-FILE-DOWNLOAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:24 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSmFileDownloadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199)
)
ciscoSmFileDownloadMIB.setRevisions(
        ("2002-05-21 00:00",
         "2001-02-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CsFileMIBObjects_ObjectIdentity = ObjectIdentity
csFileMIBObjects = _CsFileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1)
)
_CsDefineFile_ObjectIdentity = ObjectIdentity
csDefineFile = _CsDefineFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1)
)
_CsDefineFileTable_Object = MibTable
csDefineFileTable = _CsDefineFileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1)
)
if mibBuilder.loadTexts:
    csDefineFileTable.setStatus("current")
_CsDefineFileEntry_Object = MibTableRow
csDefineFileEntry = _CsDefineFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1, 1)
)
csDefineFileEntry.setIndexNames(
    (0, "CISCO-SM-FILE-DOWNLOAD-MIB", "csDefineFileIndex"),
)
if mibBuilder.loadTexts:
    csDefineFileEntry.setStatus("current")


class _CsDefineFileIndex_Type(Unsigned32):
    """Custom type csDefineFileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsDefineFileIndex_Type.__name__ = "Unsigned32"
_CsDefineFileIndex_Object = MibTableColumn
csDefineFileIndex = _CsDefineFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1, 1, 1),
    _CsDefineFileIndex_Type()
)
csDefineFileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csDefineFileIndex.setStatus("current")


class _CsDefineFileName_Type(DisplayString):
    """Custom type csDefineFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CsDefineFileName_Type.__name__ = "DisplayString"
_CsDefineFileName_Object = MibTableColumn
csDefineFileName = _CsDefineFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1, 1, 2),
    _CsDefineFileName_Type()
)
csDefineFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csDefineFileName.setStatus("current")


class _CsDefineSlotNumber_Type(Unsigned32):
    """Custom type csDefineSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(100, 100),
    )


_CsDefineSlotNumber_Type.__name__ = "Unsigned32"
_CsDefineSlotNumber_Object = MibTableColumn
csDefineSlotNumber = _CsDefineSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1, 1, 3),
    _CsDefineSlotNumber_Type()
)
csDefineSlotNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csDefineSlotNumber.setStatus("current")


class _CsDefineFileStatus_Type(Integer32):
    """Custom type csDefineFileStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 8),
          ("dbUpdateFailed", 9),
          ("downloadFailed", 7),
          ("fileNotValid", 6),
          ("fileOpenFailed", 4),
          ("fileReadFailed", 5),
          ("inProgress", 1),
          ("miscError", 10),
          ("noMemory", 3),
          ("success", 2))
    )


_CsDefineFileStatus_Type.__name__ = "Integer32"
_CsDefineFileStatus_Object = MibTableColumn
csDefineFileStatus = _CsDefineFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1, 1, 4),
    _CsDefineFileStatus_Type()
)
csDefineFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csDefineFileStatus.setStatus("current")


class _CsDefineFileOperation_Type(Integer32):
    """Custom type csDefineFileOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sendToSMsOnly", 1),
          ("updateAndSend", 2))
    )


_CsDefineFileOperation_Type.__name__ = "Integer32"
_CsDefineFileOperation_Object = MibTableColumn
csDefineFileOperation = _CsDefineFileOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1, 1, 5),
    _CsDefineFileOperation_Type()
)
csDefineFileOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csDefineFileOperation.setStatus("current")
_CsDefineFileEntryStatus_Type = RowStatus
_CsDefineFileEntryStatus_Object = MibTableColumn
csDefineFileEntryStatus = _CsDefineFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 1, 1, 1, 6),
    _CsDefineFileEntryStatus_Type()
)
csDefineFileEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    csDefineFileEntryStatus.setStatus("current")
_CsFileStatus_ObjectIdentity = ObjectIdentity
csFileStatus = _CsFileStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 2)
)
_CsFileStatusTable_Object = MibTable
csFileStatusTable = _CsFileStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csFileStatusTable.setStatus("current")
_CsFileStatusEntry_Object = MibTableRow
csFileStatusEntry = _CsFileStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 2, 1, 1)
)
csFileStatusEntry.setIndexNames(
    (0, "CISCO-SM-FILE-DOWNLOAD-MIB", "csDefineFileIndex"),
    (0, "CISCO-SM-FILE-DOWNLOAD-MIB", "csFileStatusSlotNumber"),
)
if mibBuilder.loadTexts:
    csFileStatusEntry.setStatus("current")


class _CsFileStatusSlotNumber_Type(Unsigned32):
    """Custom type csFileStatusSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CsFileStatusSlotNumber_Type.__name__ = "Unsigned32"
_CsFileStatusSlotNumber_Object = MibTableColumn
csFileStatusSlotNumber = _CsFileStatusSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 2, 1, 1, 1),
    _CsFileStatusSlotNumber_Type()
)
csFileStatusSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csFileStatusSlotNumber.setStatus("current")


class _CsFileSlotState_Type(Integer32):
    """Custom type csFileSlotState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 6),
          ("fileOpenFailed", 4),
          ("fileWriteFailed", 5),
          ("inProgress", 1),
          ("miscFailure", 7),
          ("notProcessed", 2),
          ("success", 3))
    )


_CsFileSlotState_Type.__name__ = "Integer32"
_CsFileSlotState_Object = MibTableColumn
csFileSlotState = _CsFileSlotState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 1, 2, 1, 1, 2),
    _CsFileSlotState_Type()
)
csFileSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csFileSlotState.setStatus("current")
_CsFileMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
csFileMIBNotificationPrefix = _CsFileMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 2)
)
_CsFileMIBNotifications_ObjectIdentity = ObjectIdentity
csFileMIBNotifications = _CsFileMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 2, 0)
)
_CsFileMIBConformance_ObjectIdentity = ObjectIdentity
csFileMIBConformance = _CsFileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 3)
)
_CsFileMIBCompliances_ObjectIdentity = ObjectIdentity
csFileMIBCompliances = _CsFileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 3, 1)
)
_CsFileMIBGroups_ObjectIdentity = ObjectIdentity
csFileMIBGroups = _CsFileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 3, 2)
)

# Managed Objects groups

csDefineFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 3, 2, 1)
)
csDefineFileGroup.setObjects(
      *(("CISCO-SM-FILE-DOWNLOAD-MIB", "csDefineFileName"),
        ("CISCO-SM-FILE-DOWNLOAD-MIB", "csDefineSlotNumber"),
        ("CISCO-SM-FILE-DOWNLOAD-MIB", "csDefineFileStatus"),
        ("CISCO-SM-FILE-DOWNLOAD-MIB", "csDefineFileOperation"),
        ("CISCO-SM-FILE-DOWNLOAD-MIB", "csDefineFileEntryStatus"))
)
if mibBuilder.loadTexts:
    csDefineFileGroup.setStatus("current")

csFileStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 3, 2, 2)
)
csFileStatusGroup.setObjects(
    ("CISCO-SM-FILE-DOWNLOAD-MIB", "csFileSlotState")
)
if mibBuilder.loadTexts:
    csFileStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csFileMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 199, 3, 1, 1)
)
if mibBuilder.loadTexts:
    csFileMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SM-FILE-DOWNLOAD-MIB",
    **{"ciscoSmFileDownloadMIB": ciscoSmFileDownloadMIB,
       "csFileMIBObjects": csFileMIBObjects,
       "csDefineFile": csDefineFile,
       "csDefineFileTable": csDefineFileTable,
       "csDefineFileEntry": csDefineFileEntry,
       "csDefineFileIndex": csDefineFileIndex,
       "csDefineFileName": csDefineFileName,
       "csDefineSlotNumber": csDefineSlotNumber,
       "csDefineFileStatus": csDefineFileStatus,
       "csDefineFileOperation": csDefineFileOperation,
       "csDefineFileEntryStatus": csDefineFileEntryStatus,
       "csFileStatus": csFileStatus,
       "csFileStatusTable": csFileStatusTable,
       "csFileStatusEntry": csFileStatusEntry,
       "csFileStatusSlotNumber": csFileStatusSlotNumber,
       "csFileSlotState": csFileSlotState,
       "csFileMIBNotificationPrefix": csFileMIBNotificationPrefix,
       "csFileMIBNotifications": csFileMIBNotifications,
       "csFileMIBConformance": csFileMIBConformance,
       "csFileMIBCompliances": csFileMIBCompliances,
       "csFileMIBCompliance": csFileMIBCompliance,
       "csFileMIBGroups": csFileMIBGroups,
       "csDefineFileGroup": csDefineFileGroup,
       "csFileStatusGroup": csFileStatusGroup}
)
