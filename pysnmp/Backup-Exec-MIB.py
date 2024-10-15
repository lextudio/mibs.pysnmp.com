# SNMP MIB module (Backup-Exec-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Backup-Exec-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:15 2024
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

_Veritassoftware_ObjectIdentity = ObjectIdentity
veritassoftware = _Veritassoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302)
)
_BackupExecNetWare_ObjectIdentity = ObjectIdentity
backupExecNetWare = _BackupExecNetWare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 1)
)


class _Messageobject_Type(DisplayString):
    """Custom type messageobject based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Messageobject_Type.__name__ = "DisplayString"
_Messageobject_Object = MibScalar
messageobject = _Messageobject_Object(
    (1, 3, 6, 1, 4, 1, 1302, 1, 1),
    _Messageobject_Type()
)
messageobject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageobject.setStatus("mandatory")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3)
)
_Backupexec_ObjectIdentity = ObjectIdentity
backupexec = _Backupexec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1)
)
_Beconfig_ObjectIdentity = ObjectIdentity
beconfig = _Beconfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 1)
)
_BackupExecNTGeneral_ObjectIdentity = ObjectIdentity
backupExecNTGeneral = _BackupExecNTGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9)
)
_Bejobs_ObjectIdentity = ObjectIdentity
bejobs = _Bejobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2)
)
_BackupExecNTJobs_ObjectIdentity = ObjectIdentity
backupExecNTJobs = _BackupExecNTJobs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8)
)
_Beinfo_ObjectIdentity = ObjectIdentity
beinfo = _Beinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 3)
)


class _BeName_Type(DisplayString):
    """Custom type beName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BeName_Type.__name__ = "DisplayString"
_BeName_Object = MibScalar
beName = _BeName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 1),
    _BeName_Type()
)
beName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beName.setStatus("mandatory")


class _RevMajor_Type(Integer32):
    """Custom type revMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RevMajor_Type.__name__ = "Integer32"
_RevMajor_Object = MibScalar
revMajor = _RevMajor_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 2),
    _RevMajor_Type()
)
revMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revMajor.setStatus("mandatory")


class _RevMinor_Type(Integer32):
    """Custom type revMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RevMinor_Type.__name__ = "Integer32"
_RevMinor_Object = MibScalar
revMinor = _RevMinor_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 3),
    _RevMinor_Type()
)
revMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revMinor.setStatus("mandatory")


class _BeBuild_Type(Integer32):
    """Custom type beBuild based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BeBuild_Type.__name__ = "Integer32"
_BeBuild_Object = MibScalar
beBuild = _BeBuild_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 4),
    _BeBuild_Type()
)
beBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beBuild.setStatus("mandatory")


class _BeSerial_Type(DisplayString):
    """Custom type beSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BeSerial_Type.__name__ = "DisplayString"
_BeSerial_Object = MibScalar
beSerial = _BeSerial_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 3, 5),
    _BeSerial_Type()
)
beSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    beSerial.setStatus("mandatory")
_Bemodules_ObjectIdentity = ObjectIdentity
bemodules = _Bemodules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4)
)
_Labs_ObjectIdentity = ObjectIdentity
labs = _Labs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1)
)
_BackupExecOptLABS_ObjectIdentity = ObjectIdentity
backupExecOptLABS = _BackupExecOptLABS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1, 1)
)
_Disasterrecovery_ObjectIdentity = ObjectIdentity
disasterrecovery = _Disasterrecovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2)
)
_BackupExecOptIDR_ObjectIdentity = ObjectIdentity
backupExecOptIDR = _BackupExecOptIDR_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2, 1)
)
_Openfileoption_ObjectIdentity = ObjectIdentity
openfileoption = _Openfileoption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3)
)
_BackupExecOptOFO_ObjectIdentity = ObjectIdentity
backupExecOptOFO = _BackupExecOptOFO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3, 1)
)
_Nonspecifictraps_ObjectIdentity = ObjectIdentity
nonspecifictraps = _Nonspecifictraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5)
)
_Pvldevice_ObjectIdentity = ObjectIdentity
pvldevice = _Pvldevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1)
)
_BackupExecPVLDevice_ObjectIdentity = ObjectIdentity
backupExecPVLDevice = _BackupExecPVLDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1)
)
_Pvlmedia_ObjectIdentity = ObjectIdentity
pvlmedia = _Pvlmedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2)
)
_BackupExecPVLMedia_ObjectIdentity = ObjectIdentity
backupExecPVLMedia = _BackupExecPVLMedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1)
)
_Catalog_ObjectIdentity = ObjectIdentity
catalog = _Catalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 3)
)
_BackupExecCatalog_ObjectIdentity = ObjectIdentity
backupExecCatalog = _BackupExecCatalog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 3, 1)
)
_Tapealert_ObjectIdentity = ObjectIdentity
tapealert = _Tapealert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4)
)
_BackupExecTapeAlert_ObjectIdentity = ObjectIdentity
backupExecTapeAlert = _BackupExecTapeAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1)
)
_Databasemaint_ObjectIdentity = ObjectIdentity
databasemaint = _Databasemaint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5)
)
_BackupExecDatabaseMaintenance_ObjectIdentity = ObjectIdentity
backupExecDatabaseMaintenance = _BackupExecDatabaseMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5, 1)
)
_Softwareupdate_ObjectIdentity = ObjectIdentity
softwareupdate = _Softwareupdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6)
)
_BackupExecSoftwareUpdate_ObjectIdentity = ObjectIdentity
backupExecSoftwareUpdate = _BackupExecSoftwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1)
)
_Install_ObjectIdentity = ObjectIdentity
install = _Install_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7)
)
_BackupExecInstall_ObjectIdentity = ObjectIdentity
backupExecInstall = _BackupExecInstall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7, 1)
)
_Devices_ObjectIdentity = ObjectIdentity
devices = _Devices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 2)
)
_Loader_ObjectIdentity = ObjectIdentity
loader = _Loader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 2, 4)
)
_BackupExecNTLoader_ObjectIdentity = ObjectIdentity
backupExecNTLoader = _BackupExecNTLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 2, 4, 3)
)
_Tape_ObjectIdentity = ObjectIdentity
tape = _Tape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 2, 5)
)
_BackupExecNTTapeDrive_ObjectIdentity = ObjectIdentity
backupExecNTTapeDrive = _BackupExecNTTapeDrive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 2, 5, 3)
)
_Trapvars_ObjectIdentity = ObjectIdentity
trapvars = _Trapvars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1302, 3, 3)
)
_ServerName_Type = DisplayString
_ServerName_Object = MibScalar
serverName = _ServerName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 3, 1),
    _ServerName_Type()
)
serverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverName.setStatus("mandatory")
_AppInfo_Type = DisplayString
_AppInfo_Object = MibScalar
appInfo = _AppInfo_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 3, 2),
    _AppInfo_Type()
)
appInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appInfo.setStatus("mandatory")
_JobName_Type = DisplayString
_JobName_Object = MibScalar
jobName = _JobName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 3, 3),
    _JobName_Type()
)
jobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jobName.setStatus("mandatory")
_OperatorName_Type = DisplayString
_OperatorName_Object = MibScalar
operatorName = _OperatorName_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 3, 4),
    _OperatorName_Type()
)
operatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operatorName.setStatus("mandatory")
_MessageText_Type = DisplayString
_MessageText_Object = MibScalar
messageText = _MessageText_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 3, 5),
    _MessageText_Type()
)
messageText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    messageText.setStatus("mandatory")
_AdditionalText_Type = DisplayString
_AdditionalText_Object = MibScalar
additionalText = _AdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 1302, 3, 3, 6),
    _AdditionalText_Type()
)
additionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    additionalText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

blockingerrormsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 1, 0, 1)
)
blockingerrormsg.setObjects(
    ("Backup-Exec-MIB", "messageobject")
)
if mibBuilder.loadTexts:
    blockingerrormsg.setStatus(
        ""
    )

errormessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 1, 0, 2)
)
errormessage.setObjects(
    ("Backup-Exec-MIB", "messageobject")
)
if mibBuilder.loadTexts:
    errormessage.setStatus(
        ""
    )

blockingmessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 1, 0, 3)
)
blockingmessage.setObjects(
    ("Backup-Exec-MIB", "messageobject")
)
if mibBuilder.loadTexts:
    blockingmessage.setStatus(
        ""
    )

warningmessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 1, 0, 4)
)
warningmessage.setObjects(
    ("Backup-Exec-MIB", "messageobject")
)
if mibBuilder.loadTexts:
    warningmessage.setStatus(
        ""
    )

informationmessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 1, 0, 5)
)
informationmessage.setObjects(
    ("Backup-Exec-MIB", "messageobject")
)
if mibBuilder.loadTexts:
    informationmessage.setStatus(
        ""
    )

beNTLoaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9, 0, 1)
)
beNTLoaded.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "appInfo"))
)
if mibBuilder.loadTexts:
    beNTLoaded.setStatus(
        ""
    )

beNTUnloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9, 0, 2)
)
beNTUnloaded.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "appInfo"))
)
if mibBuilder.loadTexts:
    beNTUnloaded.setStatus(
        ""
    )

beNTSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9, 0, 3)
)
beNTSystemError.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    beNTSystemError.setStatus(
        ""
    )

beNTGeneralInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 1, 9, 0, 4)
)
beNTGeneralInfo.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    beNTGeneralInfo.setStatus(
        ""
    )

jobFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8, 0, 1)
)
jobFailure.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    jobFailure.setStatus(
        ""
    )

jobAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8, 0, 2)
)
jobAborted.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "operatorName"))
)
if mibBuilder.loadTexts:
    jobAborted.setStatus(
        ""
    )

jobSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8, 0, 3)
)
jobSuccess.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    jobSuccess.setStatus(
        ""
    )

jobSuccessExcept = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8, 0, 4)
)
jobSuccessExcept.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    jobSuccessExcept.setStatus(
        ""
    )

jobStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8, 0, 5)
)
jobStarted.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    jobStarted.setStatus(
        ""
    )

jobNoData = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8, 0, 6)
)
jobNoData.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    jobNoData.setStatus(
        ""
    )

jobWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 2, 8, 0, 7)
)
jobWarning.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    jobWarning.setStatus(
        ""
    )

multipleTapesNeeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1, 1, 0, 1)
)
multipleTapesNeeded.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    multipleTapesNeeded.setStatus(
        ""
    )

retriedAutomatically = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 1, 1, 0, 2)
)
retriedAutomatically.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    retriedAutomatically.setStatus(
        ""
    )

copyDRFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2, 1, 0, 1)
)
copyDRFile.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    copyDRFile.setStatus(
        ""
    )

fullBackupComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 2, 1, 0, 2)
)
fullBackupComplete.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    fullBackupComplete.setStatus(
        ""
    )

ofoFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3, 1, 0, 1)
)
ofoFailed.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    ofoFailed.setStatus(
        ""
    )

ofoCouldNotInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 4, 3, 1, 0, 2)
)
ofoCouldNotInit.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    ofoCouldNotInit.setStatus(
        ""
    )

pvlDeviceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1, 0, 1)
)
pvlDeviceError.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlDeviceError.setStatus(
        ""
    )

pvlDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1, 0, 2)
)
pvlDeviceWarning.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlDeviceWarning.setStatus(
        ""
    )

pvlDeviceInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1, 0, 3)
)
pvlDeviceInfo.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlDeviceInfo.setStatus(
        ""
    )

pvlDeviceAttn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 1, 1, 0, 4)
)
pvlDeviceAttn.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlDeviceAttn.setStatus(
        ""
    )

pvlMediaError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1, 0, 1)
)
pvlMediaError.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlMediaError.setStatus(
        ""
    )

pvlMediaWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1, 0, 2)
)
pvlMediaWarning.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlMediaWarning.setStatus(
        ""
    )

pvlMediaInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1, 0, 3)
)
pvlMediaInfo.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlMediaInfo.setStatus(
        ""
    )

pvlMediaAttn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 2, 1, 0, 4)
)
pvlMediaAttn.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    pvlMediaAttn.setStatus(
        ""
    )

catalogFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 3, 1, 0, 1)
)
catalogFailed.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    catalogFailed.setStatus(
        ""
    )

tapeAlertError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1, 0, 1)
)
tapeAlertError.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    tapeAlertError.setStatus(
        ""
    )

tapeAlertWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1, 0, 2)
)
tapeAlertWarning.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    tapeAlertWarning.setStatus(
        ""
    )

tapeAlertInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 4, 1, 0, 3)
)
tapeAlertInfo.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    tapeAlertInfo.setStatus(
        ""
    )

databaseMaintenanceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5, 1, 0, 1)
)
databaseMaintenanceError.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    databaseMaintenanceError.setStatus(
        ""
    )

databaseMaintenanceInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 5, 1, 0, 2)
)
databaseMaintenanceInfo.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    databaseMaintenanceInfo.setStatus(
        ""
    )

softwareUpdateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1, 0, 1)
)
softwareUpdateError.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    softwareUpdateError.setStatus(
        ""
    )

softwareUpdateWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1, 0, 2)
)
softwareUpdateWarning.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    softwareUpdateWarning.setStatus(
        ""
    )

softwareUpdateInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 6, 1, 0, 3)
)
softwareUpdateInfo.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    softwareUpdateInfo.setStatus(
        ""
    )

installWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7, 1, 0, 1)
)
installWarning.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    installWarning.setStatus(
        ""
    )

installInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 1, 5, 7, 1, 0, 2)
)
installInfo.setObjects(
    ("Backup-Exec-MIB", "messageText")
)
if mibBuilder.loadTexts:
    installInfo.setStatus(
        ""
    )

loaderNeedsAttention = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 2, 4, 3, 0, 3)
)
loaderNeedsAttention.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    loaderNeedsAttention.setStatus(
        ""
    )

driveNeedsAttention = NotificationType(
    (1, 3, 6, 1, 4, 1, 1302, 3, 2, 5, 3, 0, 3)
)
driveNeedsAttention.setObjects(
      *(("Backup-Exec-MIB", "messageText"),
        ("Backup-Exec-MIB", "serverName"),
        ("Backup-Exec-MIB", "jobName"),
        ("Backup-Exec-MIB", "additionalText"))
)
if mibBuilder.loadTexts:
    driveNeedsAttention.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Backup-Exec-MIB",
    **{"veritassoftware": veritassoftware,
       "backupExecNetWare": backupExecNetWare,
       "blockingerrormsg": blockingerrormsg,
       "errormessage": errormessage,
       "blockingmessage": blockingmessage,
       "warningmessage": warningmessage,
       "informationmessage": informationmessage,
       "messageobject": messageobject,
       "products": products,
       "backupexec": backupexec,
       "beconfig": beconfig,
       "backupExecNTGeneral": backupExecNTGeneral,
       "beNTLoaded": beNTLoaded,
       "beNTUnloaded": beNTUnloaded,
       "beNTSystemError": beNTSystemError,
       "beNTGeneralInfo": beNTGeneralInfo,
       "bejobs": bejobs,
       "backupExecNTJobs": backupExecNTJobs,
       "jobFailure": jobFailure,
       "jobAborted": jobAborted,
       "jobSuccess": jobSuccess,
       "jobSuccessExcept": jobSuccessExcept,
       "jobStarted": jobStarted,
       "jobNoData": jobNoData,
       "jobWarning": jobWarning,
       "beinfo": beinfo,
       "beName": beName,
       "revMajor": revMajor,
       "revMinor": revMinor,
       "beBuild": beBuild,
       "beSerial": beSerial,
       "bemodules": bemodules,
       "labs": labs,
       "backupExecOptLABS": backupExecOptLABS,
       "multipleTapesNeeded": multipleTapesNeeded,
       "retriedAutomatically": retriedAutomatically,
       "disasterrecovery": disasterrecovery,
       "backupExecOptIDR": backupExecOptIDR,
       "copyDRFile": copyDRFile,
       "fullBackupComplete": fullBackupComplete,
       "openfileoption": openfileoption,
       "backupExecOptOFO": backupExecOptOFO,
       "ofoFailed": ofoFailed,
       "ofoCouldNotInit": ofoCouldNotInit,
       "nonspecifictraps": nonspecifictraps,
       "pvldevice": pvldevice,
       "backupExecPVLDevice": backupExecPVLDevice,
       "pvlDeviceError": pvlDeviceError,
       "pvlDeviceWarning": pvlDeviceWarning,
       "pvlDeviceInfo": pvlDeviceInfo,
       "pvlDeviceAttn": pvlDeviceAttn,
       "pvlmedia": pvlmedia,
       "backupExecPVLMedia": backupExecPVLMedia,
       "pvlMediaError": pvlMediaError,
       "pvlMediaWarning": pvlMediaWarning,
       "pvlMediaInfo": pvlMediaInfo,
       "pvlMediaAttn": pvlMediaAttn,
       "catalog": catalog,
       "backupExecCatalog": backupExecCatalog,
       "catalogFailed": catalogFailed,
       "tapealert": tapealert,
       "backupExecTapeAlert": backupExecTapeAlert,
       "tapeAlertError": tapeAlertError,
       "tapeAlertWarning": tapeAlertWarning,
       "tapeAlertInfo": tapeAlertInfo,
       "databasemaint": databasemaint,
       "backupExecDatabaseMaintenance": backupExecDatabaseMaintenance,
       "databaseMaintenanceError": databaseMaintenanceError,
       "databaseMaintenanceInfo": databaseMaintenanceInfo,
       "softwareupdate": softwareupdate,
       "backupExecSoftwareUpdate": backupExecSoftwareUpdate,
       "softwareUpdateError": softwareUpdateError,
       "softwareUpdateWarning": softwareUpdateWarning,
       "softwareUpdateInfo": softwareUpdateInfo,
       "install": install,
       "backupExecInstall": backupExecInstall,
       "installWarning": installWarning,
       "installInfo": installInfo,
       "devices": devices,
       "loader": loader,
       "backupExecNTLoader": backupExecNTLoader,
       "loaderNeedsAttention": loaderNeedsAttention,
       "tape": tape,
       "backupExecNTTapeDrive": backupExecNTTapeDrive,
       "driveNeedsAttention": driveNeedsAttention,
       "trapvars": trapvars,
       "serverName": serverName,
       "appInfo": appInfo,
       "jobName": jobName,
       "operatorName": operatorName,
       "messageText": messageText,
       "additionalText": additionalText}
)
