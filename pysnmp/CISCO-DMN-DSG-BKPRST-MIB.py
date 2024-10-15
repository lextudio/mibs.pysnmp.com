# SNMP MIB module (CISCO-DMN-DSG-BKPRST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-BKPRST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:16 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGBKPRST = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3)
)
ciscoDSGBKPRST.setRevisions(
        ("2012-03-26 17:00",
         "2010-08-30 05:00",
         "2010-06-17 06:00",
         "2010-03-22 05:00",
         "2010-02-12 15:00",
         "2009-11-22 15:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BackupRestoreInfo_ObjectIdentity = ObjectIdentity
backupRestoreInfo = _BackupRestoreInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1)
)


class _BackupRestoreOperation_Type(Integer32):
    """Custom type backupRestoreOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("restore", 2),
          ("writeOnly", 3))
    )


_BackupRestoreOperation_Type.__name__ = "Integer32"
_BackupRestoreOperation_Object = MibScalar
backupRestoreOperation = _BackupRestoreOperation_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 1),
    _BackupRestoreOperation_Type()
)
backupRestoreOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreOperation.setStatus("current")


class _BackupRestoreType_Type(Integer32):
    """Custom type backupRestoreType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("extended", 2),
          ("full", 3),
          ("standard", 1))
    )


_BackupRestoreType_Type.__name__ = "Integer32"
_BackupRestoreType_Object = MibScalar
backupRestoreType = _BackupRestoreType_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 2),
    _BackupRestoreType_Type()
)
backupRestoreType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreType.setStatus("current")


class _BackupRestoreFileName_Type(DisplayString):
    """Custom type backupRestoreFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_BackupRestoreFileName_Type.__name__ = "DisplayString"
_BackupRestoreFileName_Object = MibScalar
backupRestoreFileName = _BackupRestoreFileName_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 3),
    _BackupRestoreFileName_Type()
)
backupRestoreFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreFileName.setStatus("current")
_BackupRestoreFtpServerIp_Type = IpAddress
_BackupRestoreFtpServerIp_Object = MibScalar
backupRestoreFtpServerIp = _BackupRestoreFtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 4),
    _BackupRestoreFtpServerIp_Type()
)
backupRestoreFtpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreFtpServerIp.setStatus("current")


class _BackupRestoreFtpUsername_Type(DisplayString):
    """Custom type backupRestoreFtpUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BackupRestoreFtpUsername_Type.__name__ = "DisplayString"
_BackupRestoreFtpUsername_Object = MibScalar
backupRestoreFtpUsername = _BackupRestoreFtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 5),
    _BackupRestoreFtpUsername_Type()
)
backupRestoreFtpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreFtpUsername.setStatus("current")


class _BackupRestoreFtpPassword_Type(DisplayString):
    """Custom type backupRestoreFtpPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BackupRestoreFtpPassword_Type.__name__ = "DisplayString"
_BackupRestoreFtpPassword_Object = MibScalar
backupRestoreFtpPassword = _BackupRestoreFtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 6),
    _BackupRestoreFtpPassword_Type()
)
backupRestoreFtpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreFtpPassword.setStatus("current")


class _BackupRestoreFtpPortno_Type(Integer32):
    """Custom type backupRestoreFtpPortno based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BackupRestoreFtpPortno_Type.__name__ = "Integer32"
_BackupRestoreFtpPortno_Object = MibScalar
backupRestoreFtpPortno = _BackupRestoreFtpPortno_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 7),
    _BackupRestoreFtpPortno_Type()
)
backupRestoreFtpPortno.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupRestoreFtpPortno.setStatus("current")


class _BackupRestoreLastBackupFile_Type(DisplayString):
    """Custom type backupRestoreLastBackupFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_BackupRestoreLastBackupFile_Type.__name__ = "DisplayString"
_BackupRestoreLastBackupFile_Object = MibScalar
backupRestoreLastBackupFile = _BackupRestoreLastBackupFile_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 8),
    _BackupRestoreLastBackupFile_Type()
)
backupRestoreLastBackupFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupRestoreLastBackupFile.setStatus("current")


class _BackupRestoreLastBackupTime_Type(DisplayString):
    """Custom type backupRestoreLastBackupTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BackupRestoreLastBackupTime_Type.__name__ = "DisplayString"
_BackupRestoreLastBackupTime_Object = MibScalar
backupRestoreLastBackupTime = _BackupRestoreLastBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 9),
    _BackupRestoreLastBackupTime_Type()
)
backupRestoreLastBackupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupRestoreLastBackupTime.setStatus("current")


class _BackupRestoreLastRestoreFile_Type(DisplayString):
    """Custom type backupRestoreLastRestoreFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 119),
    )


_BackupRestoreLastRestoreFile_Type.__name__ = "DisplayString"
_BackupRestoreLastRestoreFile_Object = MibScalar
backupRestoreLastRestoreFile = _BackupRestoreLastRestoreFile_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 10),
    _BackupRestoreLastRestoreFile_Type()
)
backupRestoreLastRestoreFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupRestoreLastRestoreFile.setStatus("current")


class _BackupRestoreLastRestoreTime_Type(DisplayString):
    """Custom type backupRestoreLastRestoreTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BackupRestoreLastRestoreTime_Type.__name__ = "DisplayString"
_BackupRestoreLastRestoreTime_Object = MibScalar
backupRestoreLastRestoreTime = _BackupRestoreLastRestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 11),
    _BackupRestoreLastRestoreTime_Type()
)
backupRestoreLastRestoreTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupRestoreLastRestoreTime.setStatus("current")


class _BackupRestoreOperationStatus_Type(Integer32):
    """Custom type backupRestoreOperationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("inprogress", 1),
          ("pass", 2))
    )


_BackupRestoreOperationStatus_Type.__name__ = "Integer32"
_BackupRestoreOperationStatus_Object = MibScalar
backupRestoreOperationStatus = _BackupRestoreOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 12),
    _BackupRestoreOperationStatus_Type()
)
backupRestoreOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupRestoreOperationStatus.setStatus("current")


class _BackupRestoreDetailedStatus_Type(Integer32):
    """Custom type backupRestoreDetailedStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("backupConnecting", 3),
          ("backupDone", 5),
          ("backupFailed", 6),
          ("backupProcessing", 2),
          ("backupSendingFile", 4),
          ("ftpFileTransferError", 13),
          ("idle", 1),
          ("restoreConnecting", 7),
          ("restoreDone", 11),
          ("restoreFailed", 12),
          ("restoreFileCorrupted", 14),
          ("restoreFileDesignationCodeMismatch", 15),
          ("restoreFileMissingContents", 20),
          ("restoreFileMissingDesignation", 19),
          ("restoreFileMissingFileInformation", 17),
          ("restoreFileMissingPlatformType", 18),
          ("restoreFileMissingRoot", 21),
          ("restoreFilePlatformTypeMismatch", 16),
          ("restoreProcessing", 10),
          ("restoreReceivingFile", 9),
          ("restoreWaitingFile", 8))
    )


_BackupRestoreDetailedStatus_Type.__name__ = "Integer32"
_BackupRestoreDetailedStatus_Object = MibScalar
backupRestoreDetailedStatus = _BackupRestoreDetailedStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 13),
    _BackupRestoreDetailedStatus_Type()
)
backupRestoreDetailedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupRestoreDetailedStatus.setStatus("current")


class _BackupRestorePercentageComp_Type(DisplayString):
    """Custom type backupRestorePercentageComp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BackupRestorePercentageComp_Type.__name__ = "DisplayString"
_BackupRestorePercentageComp_Object = MibScalar
backupRestorePercentageComp = _BackupRestorePercentageComp_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 3, 1, 14),
    _BackupRestorePercentageComp_Type()
)
backupRestorePercentageComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupRestorePercentageComp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-BKPRST-MIB",
    **{"ciscoDSGBKPRST": ciscoDSGBKPRST,
       "backupRestoreInfo": backupRestoreInfo,
       "backupRestoreOperation": backupRestoreOperation,
       "backupRestoreType": backupRestoreType,
       "backupRestoreFileName": backupRestoreFileName,
       "backupRestoreFtpServerIp": backupRestoreFtpServerIp,
       "backupRestoreFtpUsername": backupRestoreFtpUsername,
       "backupRestoreFtpPassword": backupRestoreFtpPassword,
       "backupRestoreFtpPortno": backupRestoreFtpPortno,
       "backupRestoreLastBackupFile": backupRestoreLastBackupFile,
       "backupRestoreLastBackupTime": backupRestoreLastBackupTime,
       "backupRestoreLastRestoreFile": backupRestoreLastRestoreFile,
       "backupRestoreLastRestoreTime": backupRestoreLastRestoreTime,
       "backupRestoreOperationStatus": backupRestoreOperationStatus,
       "backupRestoreDetailedStatus": backupRestoreDetailedStatus,
       "backupRestorePercentageComp": backupRestorePercentageComp}
)
