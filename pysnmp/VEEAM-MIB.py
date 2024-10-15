# SNMP MIB module (VEEAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VEEAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:08 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Veeam_ObjectIdentity = ObjectIdentity
veeam = _Veeam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31023)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31023, 1)
)
_Backup_ObjectIdentity = ObjectIdentity
backup = _Backup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1)
)


class _BackupJobId_Type(DisplayString):
    """Custom type backupJobId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BackupJobId_Type.__name__ = "DisplayString"
_BackupJobId_Object = MibScalar
backupJobId = _BackupJobId_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 101),
    _BackupJobId_Type()
)
backupJobId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupJobId.setStatus("mandatory")


class _BackupJobName_Type(DisplayString):
    """Custom type backupJobName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BackupJobName_Type.__name__ = "DisplayString"
_BackupJobName_Object = MibScalar
backupJobName = _BackupJobName_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 102),
    _BackupJobName_Type()
)
backupJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupJobName.setStatus("mandatory")


class _BackupJobResult_Type(DisplayString):
    """Custom type backupJobResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BackupJobResult_Type.__name__ = "DisplayString"
_BackupJobResult_Object = MibScalar
backupJobResult = _BackupJobResult_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 103),
    _BackupJobResult_Type()
)
backupJobResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupJobResult.setStatus("mandatory")


class _BackupJobComment_Type(DisplayString):
    """Custom type backupJobComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BackupJobComment_Type.__name__ = "DisplayString"
_BackupJobComment_Object = MibScalar
backupJobComment = _BackupJobComment_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 104),
    _BackupJobComment_Type()
)
backupJobComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupJobComment.setStatus("mandatory")


class _VmName_Type(DisplayString):
    """Custom type vmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmName_Type.__name__ = "DisplayString"
_VmName_Object = MibScalar
vmName = _VmName_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 105),
    _VmName_Type()
)
vmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmName.setStatus("mandatory")


class _SourceHostName_Type(DisplayString):
    """Custom type sourceHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SourceHostName_Type.__name__ = "DisplayString"
_SourceHostName_Object = MibScalar
sourceHostName = _SourceHostName_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 106),
    _SourceHostName_Type()
)
sourceHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceHostName.setStatus("mandatory")


class _VmBackupResult_Type(DisplayString):
    """Custom type vmBackupResult based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmBackupResult_Type.__name__ = "DisplayString"
_VmBackupResult_Object = MibScalar
vmBackupResult = _VmBackupResult_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 107),
    _VmBackupResult_Type()
)
vmBackupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmBackupResult.setStatus("mandatory")


class _VmBackupComment_Type(DisplayString):
    """Custom type vmBackupComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmBackupComment_Type.__name__ = "DisplayString"
_VmBackupComment_Object = MibScalar
vmBackupComment = _VmBackupComment_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 108),
    _VmBackupComment_Type()
)
vmBackupComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmBackupComment.setStatus("mandatory")


class _SessionId_Type(DisplayString):
    """Custom type sessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SessionId_Type.__name__ = "DisplayString"
_SessionId_Object = MibScalar
sessionId = _SessionId_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 109),
    _SessionId_Type()
)
sessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionId.setStatus("mandatory")


class _InitiatorName_Type(DisplayString):
    """Custom type initiatorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InitiatorName_Type.__name__ = "DisplayString"
_InitiatorName_Object = MibScalar
initiatorName = _InitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 110),
    _InitiatorName_Type()
)
initiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorName.setStatus("mandatory")


class _InitiatorSid_Type(DisplayString):
    """Custom type initiatorSid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InitiatorSid_Type.__name__ = "DisplayString"
_InitiatorSid_Object = MibScalar
initiatorSid = _InitiatorSid_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 111),
    _InitiatorSid_Type()
)
initiatorSid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initiatorSid.setStatus("mandatory")


class _VmRestorePointId_Type(DisplayString):
    """Custom type vmRestorePointId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmRestorePointId_Type.__name__ = "DisplayString"
_VmRestorePointId_Object = MibScalar
vmRestorePointId = _VmRestorePointId_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 112),
    _VmRestorePointId_Type()
)
vmRestorePointId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmRestorePointId.setStatus("mandatory")


class _VmRestorePointCreationTime_Type(DisplayString):
    """Custom type vmRestorePointCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmRestorePointCreationTime_Type.__name__ = "DisplayString"
_VmRestorePointCreationTime_Object = MibScalar
vmRestorePointCreationTime = _VmRestorePointCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 113),
    _VmRestorePointCreationTime_Type()
)
vmRestorePointCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmRestorePointCreationTime.setStatus("mandatory")


class _TargetHost_Type(DisplayString):
    """Custom type targetHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TargetHost_Type.__name__ = "DisplayString"
_TargetHost_Object = MibScalar
targetHost = _TargetHost_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 114),
    _TargetHost_Type()
)
targetHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetHost.setStatus("mandatory")


class _TargetDir_Type(DisplayString):
    """Custom type targetDir based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TargetDir_Type.__name__ = "DisplayString"
_TargetDir_Object = MibScalar
targetDir = _TargetDir_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 115),
    _TargetDir_Type()
)
targetDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetDir.setStatus("mandatory")


class _TransferStatus_Type(DisplayString):
    """Custom type transferStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransferStatus_Type.__name__ = "DisplayString"
_TransferStatus_Object = MibScalar
transferStatus = _TransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 116),
    _TransferStatus_Type()
)
transferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferStatus.setStatus("mandatory")


class _TransferTime_Type(DisplayString):
    """Custom type transferTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransferTime_Type.__name__ = "DisplayString"
_TransferTime_Object = MibScalar
transferTime = _TransferTime_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 117),
    _TransferTime_Type()
)
transferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferTime.setStatus("mandatory")


class _TransferFileList_Type(DisplayString):
    """Custom type transferFileList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransferFileList_Type.__name__ = "DisplayString"
_TransferFileList_Object = MibScalar
transferFileList = _TransferFileList_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 118),
    _TransferFileList_Type()
)
transferFileList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transferFileList.setStatus("mandatory")


class _NotTransferFileList_Type(DisplayString):
    """Custom type notTransferFileList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NotTransferFileList_Type.__name__ = "DisplayString"
_NotTransferFileList_Object = MibScalar
notTransferFileList = _NotTransferFileList_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 119),
    _NotTransferFileList_Type()
)
notTransferFileList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    notTransferFileList.setStatus("mandatory")


class _MountServerName_Type(DisplayString):
    """Custom type mountServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MountServerName_Type.__name__ = "DisplayString"
_MountServerName_Object = MibScalar
mountServerName = _MountServerName_Object(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 120),
    _MountServerName_Type()
)
mountServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mountServerName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

onBackupJobCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 1)
)
onBackupJobCompleted.setObjects(
      *(("VEEAM-MIB", "backupJobId"),
        ("VEEAM-MIB", "backupJobName"),
        ("VEEAM-MIB", "backupJobResult"),
        ("VEEAM-MIB", "backupJobComment"))
)
if mibBuilder.loadTexts:
    onBackupJobCompleted.setStatus(
        ""
    )

onVmBackupCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 2)
)
onVmBackupCompleted.setObjects(
      *(("VEEAM-MIB", "backupJobName"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "sourceHostName"),
        ("VEEAM-MIB", "vmBackupResult"),
        ("VEEAM-MIB", "vmBackupComment"))
)
if mibBuilder.loadTexts:
    onVmBackupCompleted.setStatus(
        ""
    )

onLinuxFLRMountStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 3)
)
onLinuxFLRMountStarted.setObjects(
      *(("VEEAM-MIB", "sessionId"),
        ("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"))
)
if mibBuilder.loadTexts:
    onLinuxFLRMountStarted.setStatus(
        ""
    )

onLinuxFLRCopyToStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 4)
)
onLinuxFLRCopyToStarted.setObjects(
      *(("VEEAM-MIB", "sessionId"),
        ("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "targetHost"),
        ("VEEAM-MIB", "targetDir"))
)
if mibBuilder.loadTexts:
    onLinuxFLRCopyToStarted.setStatus(
        ""
    )

onLinuxFLRToOriginalStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 5)
)
onLinuxFLRToOriginalStarted.setObjects(
      *(("VEEAM-MIB", "sessionId"),
        ("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"))
)
if mibBuilder.loadTexts:
    onLinuxFLRToOriginalStarted.setStatus(
        ""
    )

onLinuxFLRCopyToFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 6)
)
onLinuxFLRCopyToFinished.setObjects(
      *(("VEEAM-MIB", "sessionId"),
        ("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "transferStatus"),
        ("VEEAM-MIB", "transferTime"),
        ("VEEAM-MIB", "transferFileList"),
        ("VEEAM-MIB", "notTransferFileList"),
        ("VEEAM-MIB", "targetHost"),
        ("VEEAM-MIB", "targetDir"))
)
if mibBuilder.loadTexts:
    onLinuxFLRCopyToFinished.setStatus(
        ""
    )

onLinuxFLRToOriginalFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 7)
)
onLinuxFLRToOriginalFinished.setObjects(
      *(("VEEAM-MIB", "sessionId"),
        ("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "transferStatus"),
        ("VEEAM-MIB", "transferTime"),
        ("VEEAM-MIB", "transferFileList"),
        ("VEEAM-MIB", "notTransferFileList"))
)
if mibBuilder.loadTexts:
    onLinuxFLRToOriginalFinished.setStatus(
        ""
    )

onWinFLRMountStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 8)
)
onWinFLRMountStarted.setObjects(
      *(("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "mountServerName"))
)
if mibBuilder.loadTexts:
    onWinFLRMountStarted.setStatus(
        ""
    )

onWinFLRToOriginalStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 9)
)
onWinFLRToOriginalStarted.setObjects(
      *(("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"))
)
if mibBuilder.loadTexts:
    onWinFLRToOriginalStarted.setStatus(
        ""
    )

onWinFLRCopyToStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 10)
)
onWinFLRCopyToStarted.setObjects(
      *(("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "targetDir"))
)
if mibBuilder.loadTexts:
    onWinFLRCopyToStarted.setStatus(
        ""
    )

onWinFLRToOriginalFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 11)
)
onWinFLRToOriginalFinished.setObjects(
      *(("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "transferStatus"),
        ("VEEAM-MIB", "transferFileList"),
        ("VEEAM-MIB", "notTransferFileList"))
)
if mibBuilder.loadTexts:
    onWinFLRToOriginalFinished.setStatus(
        ""
    )

onWinFLRCopyToFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 12)
)
onWinFLRCopyToFinished.setObjects(
      *(("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "transferStatus"),
        ("VEEAM-MIB", "transferFileList"),
        ("VEEAM-MIB", "notTransferFileList"),
        ("VEEAM-MIB", "targetDir"))
)
if mibBuilder.loadTexts:
    onWinFLRCopyToFinished.setStatus(
        ""
    )

onWebDownloadStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 13)
)
onWebDownloadStart.setObjects(
      *(("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"))
)
if mibBuilder.loadTexts:
    onWebDownloadStart.setStatus(
        ""
    )

onWebDownloadFinished = NotificationType(
    (1, 3, 6, 1, 4, 1, 31023, 1, 1, 1, 0, 14)
)
onWebDownloadFinished.setObjects(
      *(("VEEAM-MIB", "initiatorName"),
        ("VEEAM-MIB", "initiatorSid"),
        ("VEEAM-MIB", "vmRestorePointId"),
        ("VEEAM-MIB", "vmName"),
        ("VEEAM-MIB", "vmRestorePointCreationTime"),
        ("VEEAM-MIB", "transferStatus"),
        ("VEEAM-MIB", "transferFileList"),
        ("VEEAM-MIB", "notTransferFileList"))
)
if mibBuilder.loadTexts:
    onWebDownloadFinished.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VEEAM-MIB",
    **{"veeam": veeam,
       "products": products,
       "backup": backup,
       "traps": traps,
       "onBackupJobCompleted": onBackupJobCompleted,
       "onVmBackupCompleted": onVmBackupCompleted,
       "onLinuxFLRMountStarted": onLinuxFLRMountStarted,
       "onLinuxFLRCopyToStarted": onLinuxFLRCopyToStarted,
       "onLinuxFLRToOriginalStarted": onLinuxFLRToOriginalStarted,
       "onLinuxFLRCopyToFinished": onLinuxFLRCopyToFinished,
       "onLinuxFLRToOriginalFinished": onLinuxFLRToOriginalFinished,
       "onWinFLRMountStarted": onWinFLRMountStarted,
       "onWinFLRToOriginalStarted": onWinFLRToOriginalStarted,
       "onWinFLRCopyToStarted": onWinFLRCopyToStarted,
       "onWinFLRToOriginalFinished": onWinFLRToOriginalFinished,
       "onWinFLRCopyToFinished": onWinFLRCopyToFinished,
       "onWebDownloadStart": onWebDownloadStart,
       "onWebDownloadFinished": onWebDownloadFinished,
       "backupJobId": backupJobId,
       "backupJobName": backupJobName,
       "backupJobResult": backupJobResult,
       "backupJobComment": backupJobComment,
       "vmName": vmName,
       "sourceHostName": sourceHostName,
       "vmBackupResult": vmBackupResult,
       "vmBackupComment": vmBackupComment,
       "sessionId": sessionId,
       "initiatorName": initiatorName,
       "initiatorSid": initiatorSid,
       "vmRestorePointId": vmRestorePointId,
       "vmRestorePointCreationTime": vmRestorePointCreationTime,
       "targetHost": targetHost,
       "targetDir": targetDir,
       "transferStatus": transferStatus,
       "transferTime": transferTime,
       "transferFileList": transferFileList,
       "notTransferFileList": notTransferFileList,
       "mountServerName": mountServerName}
)
