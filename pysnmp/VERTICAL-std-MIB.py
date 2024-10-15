# SNMP MIB module (VERTICAL-std-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERTICAL-std-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:25 2024
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

_Vertical_ObjectIdentity = ObjectIdentity
vertical = _Vertical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338)
)
_SelfTestDaemon_ObjectIdentity = ObjectIdentity
selfTestDaemon = _SelfTestDaemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 8)
)
_StdSystemGroup_ObjectIdentity = ObjectIdentity
stdSystemGroup = _StdSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 8, 1)
)


class _SysOperStatus_Type(Integer32):
    """Custom type sysOperStatus based on Integer32"""
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
        *(("error", 5),
          ("restoreInProgress", 4),
          ("running", 1),
          ("startUpInProgress", 2),
          ("upgradeInProgress", 3))
    )


_SysOperStatus_Type.__name__ = "Integer32"
_SysOperStatus_Object = MibScalar
sysOperStatus = _SysOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 1, 1),
    _SysOperStatus_Type()
)
sysOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysOperStatus.setStatus("mandatory")


class _SysCurrentVersion_Type(DisplayString):
    """Custom type sysCurrentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SysCurrentVersion_Type.__name__ = "DisplayString"
_SysCurrentVersion_Object = MibScalar
sysCurrentVersion = _SysCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 1, 2),
    _SysCurrentVersion_Type()
)
sysCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCurrentVersion.setStatus("mandatory")
_StdComponentGroup_ObjectIdentity = ObjectIdentity
stdComponentGroup = _StdComponentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2)
)
_StdComponentTable_Object = MibTable
stdComponentTable = _StdComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1)
)
if mibBuilder.loadTexts:
    stdComponentTable.setStatus("mandatory")
_StdComponentEntry_Object = MibTableRow
stdComponentEntry = _StdComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1)
)
stdComponentEntry.setIndexNames(
    (0, "VERTICAL-std-MIB", "compIndex"),
)
if mibBuilder.loadTexts:
    stdComponentEntry.setStatus("mandatory")
_CompIndex_Type = Integer32
_CompIndex_Object = MibTableColumn
compIndex = _CompIndex_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1, 1),
    _CompIndex_Type()
)
compIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compIndex.setStatus("mandatory")


class _CompName_Type(DisplayString):
    """Custom type compName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CompName_Type.__name__ = "DisplayString"
_CompName_Object = MibTableColumn
compName = _CompName_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1, 2),
    _CompName_Type()
)
compName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compName.setStatus("mandatory")


class _CompType_Type(Integer32):
    """Custom type compType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              2000,
              2001,
              2002,
              2003)
        )
    )
    namedValues = NamedValues(
        *(("type-driver", 1),
          ("type-executable", 2000),
          ("type-non-vni-driver", 2001),
          ("type-non-vni-executable", 2003),
          ("type-non-vni-service", 2002),
          ("type-service", 16))
    )


_CompType_Type.__name__ = "Integer32"
_CompType_Object = MibTableColumn
compType = _CompType_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1, 3),
    _CompType_Type()
)
compType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compType.setStatus("mandatory")


class _CompInstallStatus_Type(Integer32):
    """Custom type compInstallStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("uninstalled", 100))
    )


_CompInstallStatus_Type.__name__ = "Integer32"
_CompInstallStatus_Object = MibTableColumn
compInstallStatus = _CompInstallStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1, 4),
    _CompInstallStatus_Type()
)
compInstallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compInstallStatus.setStatus("mandatory")


class _CompOperStatus_Type(Integer32):
    """Custom type compOperStatus based on Integer32"""
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
              1025)
        )
    )
    namedValues = NamedValues(
        *(("continue-pending", 5),
          ("disabled", 1025),
          ("pause-pending", 6),
          ("paused", 7),
          ("running", 4),
          ("start-pending", 2),
          ("stop-pending", 3),
          ("stopped", 1),
          ("unknown", 8))
    )


_CompOperStatus_Type.__name__ = "Integer32"
_CompOperStatus_Object = MibTableColumn
compOperStatus = _CompOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1, 5),
    _CompOperStatus_Type()
)
compOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compOperStatus.setStatus("mandatory")


class _CompEnabled_Type(Integer32):
    """Custom type compEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 100))
    )


_CompEnabled_Type.__name__ = "Integer32"
_CompEnabled_Object = MibTableColumn
compEnabled = _CompEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1, 6),
    _CompEnabled_Type()
)
compEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compEnabled.setStatus("mandatory")


class _CompLastStart_Type(DisplayString):
    """Custom type compLastStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CompLastStart_Type.__name__ = "DisplayString"
_CompLastStart_Object = MibTableColumn
compLastStart = _CompLastStart_Object(
    (1, 3, 6, 1, 4, 1, 2338, 8, 2, 1, 1, 7),
    _CompLastStart_Type()
)
compLastStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compLastStart.setStatus("mandatory")

# Managed Objects groups


# Notification objects

stdCompFailedToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 26)
)
stdCompFailedToStart.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdCompFailedToStart.setStatus(
        ""
    )

stdCompAttemptRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 27)
)
stdCompAttemptRestart.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdCompAttemptRestart.setStatus(
        ""
    )

stdCompFailedToReStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 28)
)
stdCompFailedToReStart.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdCompFailedToReStart.setStatus(
        ""
    )

stdCompRestartComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 29)
)
stdCompRestartComplete.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdCompRestartComplete.setStatus(
        ""
    )

stdUpgradeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 30)
)
stdUpgradeStarted.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdUpgradeStarted.setStatus(
        ""
    )

stdUnpackingFiles = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 31)
)
stdUnpackingFiles.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdUnpackingFiles.setStatus(
        ""
    )

stdUnpackingComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 32)
)
stdUnpackingComplete.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdUnpackingComplete.setStatus(
        ""
    )

stdUpgradeBeingApplied = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 33)
)
stdUpgradeBeingApplied.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdUpgradeBeingApplied.setStatus(
        ""
    )

stdUpgradeInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 34)
)
stdUpgradeInProgress.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdUpgradeInProgress.setStatus(
        ""
    )

stdUpgradeComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 35)
)
stdUpgradeComplete.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdUpgradeComplete.setStatus(
        ""
    )

stdUpgradeError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 36)
)
stdUpgradeError.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdUpgradeError.setStatus(
        ""
    )

stdRestoreStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 37)
)
stdRestoreStarted.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdRestoreStarted.setStatus(
        ""
    )

stdRestoreInProgress = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 38)
)
stdRestoreInProgress.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdRestoreInProgress.setStatus(
        ""
    )

stdRestoreComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 39)
)
stdRestoreComplete.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdRestoreComplete.setStatus(
        ""
    )

stdRestoreError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 40)
)
stdRestoreError.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdRestoreError.setStatus(
        ""
    )

stdRebootingMachine = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 41)
)
stdRebootingMachine.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdRebootingMachine.setStatus(
        ""
    )

stdVerifyingSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 42)
)
stdVerifyingSystem.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdVerifyingSystem.setStatus(
        ""
    )

stdIOUptoDate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 50)
)
stdIOUptoDate.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdIOUptoDate.setStatus(
        ""
    )

stdBadCABFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 51)
)
stdBadCABFile.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdBadCABFile.setStatus(
        ""
    )

stdNotEnoughDiskSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 52)
)
stdNotEnoughDiskSpace.setObjects(
    ("VERTICAL-std-MIB", "sysCurrentVersion")
)
if mibBuilder.loadTexts:
    stdNotEnoughDiskSpace.setStatus(
        ""
    )

stdIoNotOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 63)
)
stdIoNotOperational.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdIoNotOperational.setStatus(
        ""
    )

stdPrerequisiteMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 67)
)
stdPrerequisiteMissing.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdPrerequisiteMissing.setStatus(
        ""
    )

stdPLDFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 70)
)
stdPLDFailed.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdPLDFailed.setStatus(
        ""
    )

stdUnsupportedConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 71)
)
stdUnsupportedConfiguration.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdUnsupportedConfiguration.setStatus(
        ""
    )

stdInvalidConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 2338, 0, 72)
)
stdInvalidConfiguration.setObjects(
      *(("VERTICAL-std-MIB", "sysCurrentVersion"),
        ("VERTICAL-std-MIB", "compName"))
)
if mibBuilder.loadTexts:
    stdInvalidConfiguration.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERTICAL-std-MIB",
    **{"vertical": vertical,
       "stdCompFailedToStart": stdCompFailedToStart,
       "stdCompAttemptRestart": stdCompAttemptRestart,
       "stdCompFailedToReStart": stdCompFailedToReStart,
       "stdCompRestartComplete": stdCompRestartComplete,
       "stdUpgradeStarted": stdUpgradeStarted,
       "stdUnpackingFiles": stdUnpackingFiles,
       "stdUnpackingComplete": stdUnpackingComplete,
       "stdUpgradeBeingApplied": stdUpgradeBeingApplied,
       "stdUpgradeInProgress": stdUpgradeInProgress,
       "stdUpgradeComplete": stdUpgradeComplete,
       "stdUpgradeError": stdUpgradeError,
       "stdRestoreStarted": stdRestoreStarted,
       "stdRestoreInProgress": stdRestoreInProgress,
       "stdRestoreComplete": stdRestoreComplete,
       "stdRestoreError": stdRestoreError,
       "stdRebootingMachine": stdRebootingMachine,
       "stdVerifyingSystem": stdVerifyingSystem,
       "stdIOUptoDate": stdIOUptoDate,
       "stdBadCABFile": stdBadCABFile,
       "stdNotEnoughDiskSpace": stdNotEnoughDiskSpace,
       "stdIoNotOperational": stdIoNotOperational,
       "stdPrerequisiteMissing": stdPrerequisiteMissing,
       "stdPLDFailed": stdPLDFailed,
       "stdUnsupportedConfiguration": stdUnsupportedConfiguration,
       "stdInvalidConfiguration": stdInvalidConfiguration,
       "selfTestDaemon": selfTestDaemon,
       "stdSystemGroup": stdSystemGroup,
       "sysOperStatus": sysOperStatus,
       "sysCurrentVersion": sysCurrentVersion,
       "stdComponentGroup": stdComponentGroup,
       "stdComponentTable": stdComponentTable,
       "stdComponentEntry": stdComponentEntry,
       "compIndex": compIndex,
       "compName": compName,
       "compType": compType,
       "compInstallStatus": compInstallStatus,
       "compOperStatus": compOperStatus,
       "compEnabled": compEnabled,
       "compLastStart": compLastStart}
)
