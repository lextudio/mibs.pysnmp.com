# SNMP MIB module (ASCEND-FLASH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-FLASH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:57 2024
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

(flashGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "flashGroup")

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



class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlashDevice_ObjectIdentity = ObjectIdentity
flashDevice = _FlashDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 22, 1)
)
_FlashDevices_Type = Integer32
_FlashDevices_Object = MibScalar
flashDevices = _FlashDevices_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 1),
    _FlashDevices_Type()
)
flashDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDevices.setStatus("mandatory")
_FlashDeviceTable_Object = MibTable
flashDeviceTable = _FlashDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2)
)
if mibBuilder.loadTexts:
    flashDeviceTable.setStatus("mandatory")
_FlashDeviceEntry_Object = MibTableRow
flashDeviceEntry = _FlashDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1)
)
flashDeviceEntry.setIndexNames(
    (0, "ASCEND-FLASH-MIB", "flashDeviceSocket"),
)
if mibBuilder.loadTexts:
    flashDeviceEntry.setStatus("mandatory")
_FlashDeviceSocket_Type = Integer32
_FlashDeviceSocket_Object = MibTableColumn
flashDeviceSocket = _FlashDeviceSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 1),
    _FlashDeviceSocket_Type()
)
flashDeviceSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceSocket.setStatus("mandatory")
_FlashDeviceController_Type = Integer32
_FlashDeviceController_Object = MibTableColumn
flashDeviceController = _FlashDeviceController_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 2),
    _FlashDeviceController_Type()
)
flashDeviceController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceController.setStatus("mandatory")
_FlashDeviceControllerSocket_Type = Integer32
_FlashDeviceControllerSocket_Object = MibTableColumn
flashDeviceControllerSocket = _FlashDeviceControllerSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 3),
    _FlashDeviceControllerSocket_Type()
)
flashDeviceControllerSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceControllerSocket.setStatus("mandatory")
_FlashDeviceSize_Type = Integer32
_FlashDeviceSize_Object = MibTableColumn
flashDeviceSize = _FlashDeviceSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 4),
    _FlashDeviceSize_Type()
)
flashDeviceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceSize.setStatus("mandatory")
_FlashDeviceUsed_Type = Integer32
_FlashDeviceUsed_Object = MibTableColumn
flashDeviceUsed = _FlashDeviceUsed_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 5),
    _FlashDeviceUsed_Type()
)
flashDeviceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceUsed.setStatus("mandatory")


class _FlashDeviceState_Type(Integer32):
    """Custom type flashDeviceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inserted", 1),
          ("removed", 2))
    )


_FlashDeviceState_Type.__name__ = "Integer32"
_FlashDeviceState_Object = MibTableColumn
flashDeviceState = _FlashDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 6),
    _FlashDeviceState_Type()
)
flashDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceState.setStatus("mandatory")
_FlashDeviceMaster_Type = TruthValue
_FlashDeviceMaster_Object = MibTableColumn
flashDeviceMaster = _FlashDeviceMaster_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 7),
    _FlashDeviceMaster_Type()
)
flashDeviceMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceMaster.setStatus("mandatory")


class _FlashDeviceFormatStatus_Type(Integer32):
    """Custom type flashDeviceFormatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("format-other", 99),
          ("format-v1", 1),
          ("format-v2", 2),
          ("format-v3", 3),
          ("unformatted", 100))
    )


_FlashDeviceFormatStatus_Type.__name__ = "Integer32"
_FlashDeviceFormatStatus_Object = MibTableColumn
flashDeviceFormatStatus = _FlashDeviceFormatStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 8),
    _FlashDeviceFormatStatus_Type()
)
flashDeviceFormatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceFormatStatus.setStatus("mandatory")
_FlashDeviceDescription_Type = DisplayString
_FlashDeviceDescription_Object = MibTableColumn
flashDeviceDescription = _FlashDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 1, 2, 1, 9),
    _FlashDeviceDescription_Type()
)
flashDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDeviceDescription.setStatus("mandatory")
_FlashFileTable_Object = MibTable
flashFileTable = _FlashFileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2)
)
if mibBuilder.loadTexts:
    flashFileTable.setStatus("mandatory")
_FlashFileEntry_Object = MibTableRow
flashFileEntry = _FlashFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1)
)
flashFileEntry.setIndexNames(
    (0, "ASCEND-FLASH-MIB", "flashFileSocket"),
    (0, "ASCEND-FLASH-MIB", "flashFileIndex"),
)
if mibBuilder.loadTexts:
    flashFileEntry.setStatus("mandatory")
_FlashFileIndex_Type = Integer32
_FlashFileIndex_Object = MibTableColumn
flashFileIndex = _FlashFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 1),
    _FlashFileIndex_Type()
)
flashFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileIndex.setStatus("mandatory")
_FlashFileSocket_Type = Integer32
_FlashFileSocket_Object = MibTableColumn
flashFileSocket = _FlashFileSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 3),
    _FlashFileSocket_Type()
)
flashFileSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileSocket.setStatus("mandatory")
_FlashFileSize_Type = Integer32
_FlashFileSize_Object = MibTableColumn
flashFileSize = _FlashFileSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 4),
    _FlashFileSize_Type()
)
flashFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileSize.setStatus("mandatory")


class _FlashFileStatus_Type(Integer32):
    """Custom type flashFileStatus based on Integer32"""
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
        *(("invalid", 2),
          ("open-read", 3),
          ("open-write", 4),
          ("valid", 1))
    )


_FlashFileStatus_Type.__name__ = "Integer32"
_FlashFileStatus_Object = MibTableColumn
flashFileStatus = _FlashFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 5),
    _FlashFileStatus_Type()
)
flashFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileStatus.setStatus("mandatory")
_FlashFileName_Type = DisplayString
_FlashFileName_Object = MibTableColumn
flashFileName = _FlashFileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 6),
    _FlashFileName_Type()
)
flashFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileName.setStatus("mandatory")
_FlashFileChecksum_Type = Integer32
_FlashFileChecksum_Object = MibTableColumn
flashFileChecksum = _FlashFileChecksum_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 7),
    _FlashFileChecksum_Type()
)
flashFileChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileChecksum.setStatus("mandatory")
_FlashFileVersion_Type = DisplayString
_FlashFileVersion_Object = MibTableColumn
flashFileVersion = _FlashFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 8),
    _FlashFileVersion_Type()
)
flashFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileVersion.setStatus("mandatory")


class _FlashFileAccess_Type(Integer32):
    """Custom type flashFileAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_FlashFileAccess_Type.__name__ = "Integer32"
_FlashFileAccess_Object = MibTableColumn
flashFileAccess = _FlashFileAccess_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 9),
    _FlashFileAccess_Type()
)
flashFileAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileAccess.setStatus("mandatory")
_FlashFileDateTimeStamp_Type = DisplayString
_FlashFileDateTimeStamp_Object = MibTableColumn
flashFileDateTimeStamp = _FlashFileDateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 2, 1, 10),
    _FlashFileDateTimeStamp_Type()
)
flashFileDateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFileDateTimeStamp.setStatus("mandatory")
_FlashOperation_ObjectIdentity = ObjectIdentity
flashOperation = _FlashOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 22, 3)
)


class _FlashOperationStatus_Type(Integer32):
    """Custom type flashOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              50,
              51,
              52,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162)
        )
    )
    namedValues = NamedValues(
        *(("activeConfigDownload", 5),
          ("activeConfigUpload", 4),
          ("activeFileUpload", 3),
          ("activeFormating", 2),
          ("activeInProgress", 6),
          ("errorFilenameNotValid", 52),
          ("errorFlashResultAlreadyOpen", 154),
          ("errorFlashResultBadParam", 151),
          ("errorFlashResultInternalError", 162),
          ("errorFlashResultNoCard", 156),
          ("errorFlashResultNoFormat", 157),
          ("errorFlashResultNoSpace", 160),
          ("errorFlashResultNotFound", 152),
          ("errorFlashResultNullFile", 155),
          ("errorFlashResultOldFormat", 158),
          ("errorFlashResultReadOnly", 159),
          ("errorFlashResultTooManyOpen", 153),
          ("errorFlashResultUnavail", 161),
          ("errorGeneric", 51),
          ("errorTftpCreateFile", 114),
          ("errorTftpEaccess", 102),
          ("errorTftpEbadOp", 104),
          ("errorTftpEbadTid", 105),
          ("errorTftpEbusy", 109),
          ("errorTftpEexists", 106),
          ("errorTftpEnoSpace", 103),
          ("errorTftpEnotFound", 101),
          ("errorTftpEnouser", 107),
          ("errorTftpEparm", 108),
          ("errorTftpEresource", 110),
          ("errorTftpEretries", 113),
          ("errorTftpEtimeout", 111),
          ("errorTftpEuerror", 112),
          ("errorTftpOpenFile", 115),
          ("errorTftpReadData", 116),
          ("errorTftpWriteData", 117),
          ("idle", 1),
          ("success", 50))
    )


_FlashOperationStatus_Type.__name__ = "Integer32"
_FlashOperationStatus_Object = MibScalar
flashOperationStatus = _FlashOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 3, 1),
    _FlashOperationStatus_Type()
)
flashOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashOperationStatus.setStatus("mandatory")


class _FlashOperationCommand_Type(Integer32):
    """Custom type flashOperationCommand based on Integer32"""
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
        *(("format-card", 1),
          ("load-config", 4),
          ("no-command", 3),
          ("save-config", 5),
          ("tftp-upload", 2))
    )


_FlashOperationCommand_Type.__name__ = "Integer32"
_FlashOperationCommand_Object = MibScalar
flashOperationCommand = _FlashOperationCommand_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 3, 2),
    _FlashOperationCommand_Type()
)
flashOperationCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashOperationCommand.setStatus("mandatory")
_FlashOperationHost_Type = IpAddress
_FlashOperationHost_Object = MibScalar
flashOperationHost = _FlashOperationHost_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 3, 3),
    _FlashOperationHost_Type()
)
flashOperationHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashOperationHost.setStatus("mandatory")
_FlashOperationDestFileName_Type = DisplayString
_FlashOperationDestFileName_Object = MibScalar
flashOperationDestFileName = _FlashOperationDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 3, 4),
    _FlashOperationDestFileName_Type()
)
flashOperationDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashOperationDestFileName.setStatus("mandatory")
_FlashOperationSrcFileName_Type = DisplayString
_FlashOperationSrcFileName_Object = MibScalar
flashOperationSrcFileName = _FlashOperationSrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 3, 5),
    _FlashOperationSrcFileName_Type()
)
flashOperationSrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashOperationSrcFileName.setStatus("mandatory")
_FlashOperationSocket_Type = Integer32
_FlashOperationSocket_Object = MibScalar
flashOperationSocket = _FlashOperationSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 3, 7),
    _FlashOperationSocket_Type()
)
flashOperationSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashOperationSocket.setStatus("mandatory")
_FlashOperationTftpPort_Type = Integer32
_FlashOperationTftpPort_Object = MibScalar
flashOperationTftpPort = _FlashOperationTftpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 22, 3, 8),
    _FlashOperationTftpPort_Type()
)
flashOperationTftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashOperationTftpPort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-FLASH-MIB",
    **{"TruthValue": TruthValue,
       "flashDevice": flashDevice,
       "flashDevices": flashDevices,
       "flashDeviceTable": flashDeviceTable,
       "flashDeviceEntry": flashDeviceEntry,
       "flashDeviceSocket": flashDeviceSocket,
       "flashDeviceController": flashDeviceController,
       "flashDeviceControllerSocket": flashDeviceControllerSocket,
       "flashDeviceSize": flashDeviceSize,
       "flashDeviceUsed": flashDeviceUsed,
       "flashDeviceState": flashDeviceState,
       "flashDeviceMaster": flashDeviceMaster,
       "flashDeviceFormatStatus": flashDeviceFormatStatus,
       "flashDeviceDescription": flashDeviceDescription,
       "flashFileTable": flashFileTable,
       "flashFileEntry": flashFileEntry,
       "flashFileIndex": flashFileIndex,
       "flashFileSocket": flashFileSocket,
       "flashFileSize": flashFileSize,
       "flashFileStatus": flashFileStatus,
       "flashFileName": flashFileName,
       "flashFileChecksum": flashFileChecksum,
       "flashFileVersion": flashFileVersion,
       "flashFileAccess": flashFileAccess,
       "flashFileDateTimeStamp": flashFileDateTimeStamp,
       "flashOperation": flashOperation,
       "flashOperationStatus": flashOperationStatus,
       "flashOperationCommand": flashOperationCommand,
       "flashOperationHost": flashOperationHost,
       "flashOperationDestFileName": flashOperationDestFileName,
       "flashOperationSrcFileName": flashOperationSrcFileName,
       "flashOperationSocket": flashOperationSocket,
       "flashOperationTftpPort": flashOperationTftpPort}
)
