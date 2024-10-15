# SNMP MIB module (LanMgr-Alerts-II-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LanMgr-Alerts-II-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:37 2024
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

(lanmanager,) = mibBuilder.importSymbols(
    "LanMgr-Mib-II-MIB",
    "lanmanager")

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

_Alerts_2_ObjectIdentity = ObjectIdentity
alerts_2 = _Alerts_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2)
)
_Alerts_ObjectIdentity = ObjectIdentity
alerts = _Alerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 1)
)
_Alert_conditions_ObjectIdentity = ObjectIdentity
alert_conditions = _Alert_conditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2)
)
_BytesAvailData_ObjectIdentity = ObjectIdentity
bytesAvailData = _BytesAvailData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 1)
)
_NumDiskDrives_Type = Integer32
_NumDiskDrives_Object = MibScalar
numDiskDrives = _NumDiskDrives_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 1, 1),
    _NumDiskDrives_Type()
)
numDiskDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDiskDrives.setStatus("mandatory")
_BytesAvailTable_Object = MibTable
bytesAvailTable = _BytesAvailTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    bytesAvailTable.setStatus("mandatory")
_BytesAvailEntry_Object = MibTableRow
bytesAvailEntry = _BytesAvailEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 1, 2, 1)
)
bytesAvailEntry.setIndexNames(
    (0, "LanMgr-Alerts-II-MIB", "diskDrive"),
)
if mibBuilder.loadTexts:
    bytesAvailEntry.setStatus("mandatory")


class _DiskDrive_Type(DisplayString):
    """Custom type diskDrive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_DiskDrive_Type.__name__ = "DisplayString"
_DiskDrive_Object = MibTableColumn
diskDrive = _DiskDrive_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 1, 2, 1, 1),
    _DiskDrive_Type()
)
diskDrive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDrive.setStatus("mandatory")
_BytesAvail_Type = Gauge32
_BytesAvail_Object = MibTableColumn
bytesAvail = _BytesAvail_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 1, 2, 1, 2),
    _BytesAvail_Type()
)
bytesAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesAvail.setStatus("mandatory")
_DiskAlertLevel_Type = Integer32
_DiskAlertLevel_Object = MibScalar
diskAlertLevel = _DiskAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 1, 3),
    _DiskAlertLevel_Type()
)
diskAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskAlertLevel.setStatus("mandatory")
_NetIOErrorsData_ObjectIdentity = ObjectIdentity
netIOErrorsData = _NetIOErrorsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 2)
)
_NetIOAlertLevel_Type = Integer32
_NetIOAlertLevel_Object = MibScalar
netIOAlertLevel = _NetIOAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 2, 1),
    _NetIOAlertLevel_Type()
)
netIOAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netIOAlertLevel.setStatus("mandatory")
_NumNetIOErrors_Type = Integer32
_NumNetIOErrors_Object = MibScalar
numNetIOErrors = _NumNetIOErrors_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 2, 2),
    _NumNetIOErrors_Type()
)
numNetIOErrors.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numNetIOErrors.setStatus("mandatory")
_NetworkId_Type = Integer32
_NetworkId_Object = MibScalar
networkId = _NetworkId_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 2, 3),
    _NetworkId_Type()
)
networkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkId.setStatus("mandatory")


class _NetIOErrorStatus_Type(Integer32):
    """Custom type netIOErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ioError-Status-Alert", 2),
          ("ioError-Status-OK", 1))
    )


_NetIOErrorStatus_Type.__name__ = "Integer32"
_NetIOErrorStatus_Object = MibScalar
netIOErrorStatus = _NetIOErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 2, 4),
    _NetIOErrorStatus_Type()
)
netIOErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netIOErrorStatus.setStatus("mandatory")
_ServerErrorsData_ObjectIdentity = ObjectIdentity
serverErrorsData = _ServerErrorsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 3)
)
_ServerErrorAlertLevel_Type = Integer32
_ServerErrorAlertLevel_Object = MibScalar
serverErrorAlertLevel = _ServerErrorAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 3, 1),
    _ServerErrorAlertLevel_Type()
)
serverErrorAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverErrorAlertLevel.setStatus("mandatory")
_NumServerErrors_Type = Integer32
_NumServerErrors_Object = MibScalar
numServerErrors = _NumServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 3, 2),
    _NumServerErrors_Type()
)
numServerErrors.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numServerErrors.setStatus("mandatory")


class _ServerErrorStatus_Type(Integer32):
    """Custom type serverErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("svError-Status-Alert", 2),
          ("svError-Status-OK", 1))
    )


_ServerErrorStatus_Type.__name__ = "Integer32"
_ServerErrorStatus_Object = MibScalar
serverErrorStatus = _ServerErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 3, 3),
    _ServerErrorStatus_Type()
)
serverErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverErrorStatus.setStatus("mandatory")
_PwViolationsData_ObjectIdentity = ObjectIdentity
pwViolationsData = _PwViolationsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 4)
)
_PwLogonAlertLevel_Type = Integer32
_PwLogonAlertLevel_Object = MibScalar
pwLogonAlertLevel = _PwLogonAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 4, 1),
    _PwLogonAlertLevel_Type()
)
pwLogonAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pwLogonAlertLevel.setStatus("mandatory")
_NumPWViolations_Type = Integer32
_NumPWViolations_Object = MibScalar
numPWViolations = _NumPWViolations_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 4, 2),
    _NumPWViolations_Type()
)
numPWViolations.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numPWViolations.setStatus("mandatory")


class _PasswordErrorStatus_Type(Integer32):
    """Custom type passwordErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pwError-Status-Alert", 2),
          ("pwError-Status-OK", 1))
    )


_PasswordErrorStatus_Type.__name__ = "Integer32"
_PasswordErrorStatus_Object = MibScalar
passwordErrorStatus = _PasswordErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 4, 3),
    _PasswordErrorStatus_Type()
)
passwordErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passwordErrorStatus.setStatus("mandatory")
_AccessViolatData_ObjectIdentity = ObjectIdentity
accessViolatData = _AccessViolatData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 5)
)
_AccessAlertLevel_Type = Integer32
_AccessAlertLevel_Object = MibScalar
accessAlertLevel = _AccessAlertLevel_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 5, 1),
    _AccessAlertLevel_Type()
)
accessAlertLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accessAlertLevel.setStatus("mandatory")
_NumAccessViolations_Type = Integer32
_NumAccessViolations_Object = MibScalar
numAccessViolations = _NumAccessViolations_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 5, 2),
    _NumAccessViolations_Type()
)
numAccessViolations.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    numAccessViolations.setStatus("mandatory")


class _AccessErrorStatus_Type(Integer32):
    """Custom type accessErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pwError-Status-Alert", 2),
          ("pwError-Status-OK", 1))
    )


_AccessErrorStatus_Type.__name__ = "Integer32"
_AccessErrorStatus_Object = MibScalar
accessErrorStatus = _AccessErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 5, 3),
    _AccessErrorStatus_Type()
)
accessErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessErrorStatus.setStatus("mandatory")
_PdcFailData_ObjectIdentity = ObjectIdentity
pdcFailData = _PdcFailData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 6)
)


class _PrimaryDCName_Type(DisplayString):
    """Custom type primaryDCName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_PrimaryDCName_Type.__name__ = "DisplayString"
_PrimaryDCName_Object = MibScalar
primaryDCName = _PrimaryDCName_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 6, 1),
    _PrimaryDCName_Type()
)
primaryDCName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryDCName.setStatus("mandatory")


class _PrimaryDCFailed_Type(Integer32):
    """Custom type primaryDCFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pdc-Status-Failed", 2),
          ("pdc-Status-OK", 1))
    )


_PrimaryDCFailed_Type.__name__ = "Integer32"
_PrimaryDCFailed_Object = MibScalar
primaryDCFailed = _PrimaryDCFailed_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 6, 2),
    _PrimaryDCFailed_Type()
)
primaryDCFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    primaryDCFailed.setStatus("mandatory")
_RplFailData_ObjectIdentity = ObjectIdentity
rplFailData = _RplFailData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 7)
)


class _ReplMasterName_Type(DisplayString):
    """Custom type replMasterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_ReplMasterName_Type.__name__ = "DisplayString"
_ReplMasterName_Object = MibScalar
replMasterName = _ReplMasterName_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 7, 1),
    _ReplMasterName_Type()
)
replMasterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replMasterName.setStatus("mandatory")


class _ReplMasterFailed_Type(Integer32):
    """Custom type replMasterFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rpl-Status-Failed", 2),
          ("rpl-Status-OK", 1),
          ("rpl-Status-Unknown", 3))
    )


_ReplMasterFailed_Type.__name__ = "Integer32"
_ReplMasterFailed_Object = MibScalar
replMasterFailed = _ReplMasterFailed_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 7, 2),
    _ReplMasterFailed_Type()
)
replMasterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    replMasterFailed.setStatus("mandatory")
_DiskData_ObjectIdentity = ObjectIdentity
diskData = _DiskData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 8)
)
_DiskHotFixes_Type = Counter32
_DiskHotFixes_Object = MibScalar
diskHotFixes = _DiskHotFixes_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 8, 1),
    _DiskHotFixes_Type()
)
diskHotFixes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskHotFixes.setStatus("mandatory")
_DiskHardErrors_Type = Counter32
_DiskHardErrors_Object = MibScalar
diskHardErrors = _DiskHardErrors_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 8, 2),
    _DiskHardErrors_Type()
)
diskHardErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diskHardErrors.setStatus("mandatory")
_AuditLogData_ObjectIdentity = ObjectIdentity
auditLogData = _AuditLogData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 9)
)


class _AuditLogStatus_Type(Integer32):
    """Custom type auditLogStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audit-log-80", 2),
          ("audit-log-Full", 3),
          ("audit-log-OK", 1))
    )


_AuditLogStatus_Type.__name__ = "Integer32"
_AuditLogStatus_Object = MibScalar
auditLogStatus = _AuditLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 9, 1),
    _AuditLogStatus_Type()
)
auditLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStatus.setStatus("mandatory")
_PowerData_ObjectIdentity = ObjectIdentity
powerData = _PowerData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 10)
)


class _PowerStatus_Type(Integer32):
    """Custom type powerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("power-Battery", 2),
          ("power-OK", 1),
          ("power-Shutdown", 3))
    )


_PowerStatus_Type.__name__ = "Integer32"
_PowerStatus_Object = MibScalar
powerStatus = _PowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 2, 10, 1),
    _PowerStatus_Type()
)
powerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStatus.setStatus("mandatory")
_Alert_mgmt_ObjectIdentity = ObjectIdentity
alert_mgmt = _Alert_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 77, 2, 3)
)
_AlertNameNumber_Type = Integer32
_AlertNameNumber_Object = MibScalar
alertNameNumber = _AlertNameNumber_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 3, 1),
    _AlertNameNumber_Type()
)
alertNameNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertNameNumber.setStatus("mandatory")
_AlertNameTable_Object = MibTable
alertNameTable = _AlertNameTable_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 3, 2)
)
if mibBuilder.loadTexts:
    alertNameTable.setStatus("mandatory")
_SvAlertNameEntry_Object = MibTableRow
svAlertNameEntry = _SvAlertNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 3, 2, 1)
)
svAlertNameEntry.setIndexNames(
    (0, "LanMgr-Alerts-II-MIB", "svAlertName"),
)
if mibBuilder.loadTexts:
    svAlertNameEntry.setStatus("mandatory")


class _SvAlertName_Type(DisplayString):
    """Custom type svAlertName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SvAlertName_Type.__name__ = "DisplayString"
_SvAlertName_Object = MibTableColumn
svAlertName = _SvAlertName_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 3, 2, 1, 1),
    _SvAlertName_Type()
)
svAlertName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    svAlertName.setStatus("mandatory")
_AlertSchedule_Type = Integer32
_AlertSchedule_Object = MibScalar
alertSchedule = _AlertSchedule_Object(
    (1, 3, 6, 1, 4, 1, 77, 2, 3, 3),
    _AlertSchedule_Type()
)
alertSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alertSchedule.setStatus("mandatory")

# Managed Objects groups


# Notification objects

bytesAvailAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 1)
)
if mibBuilder.loadTexts:
    bytesAvailAlert.setStatus(
        ""
    )

netIOErrorsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 2)
)
netIOErrorsAlert.setObjects(
      *(("LanMgr-Alerts-II-MIB", "networkId"),
        ("LanMgr-Alerts-II-MIB", "numNetIOErrors"))
)
if mibBuilder.loadTexts:
    netIOErrorsAlert.setStatus(
        ""
    )

serverErrorsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 3)
)
serverErrorsAlert.setObjects(
    ("LanMgr-Alerts-II-MIB", "serverErrorsData")
)
if mibBuilder.loadTexts:
    serverErrorsAlert.setStatus(
        ""
    )

pwViolationsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 4)
)
pwViolationsAlert.setObjects(
    ("LanMgr-Alerts-II-MIB", "numPWViolations")
)
if mibBuilder.loadTexts:
    pwViolationsAlert.setStatus(
        ""
    )

accessViolationsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 5)
)
accessViolationsAlert.setObjects(
    ("LanMgr-Alerts-II-MIB", "numAccessViolations")
)
if mibBuilder.loadTexts:
    accessViolationsAlert.setStatus(
        ""
    )

auditLogFullAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 6)
)
if mibBuilder.loadTexts:
    auditLogFullAlert.setStatus(
        ""
    )

auditLog80Alert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 7)
)
if mibBuilder.loadTexts:
    auditLog80Alert.setStatus(
        ""
    )

upsPowerOutWarnAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 8)
)
if mibBuilder.loadTexts:
    upsPowerOutWarnAlert.setStatus(
        ""
    )

upsPowerOutShutdownAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 9)
)
if mibBuilder.loadTexts:
    upsPowerOutShutdownAlert.setStatus(
        ""
    )

upsPowerRestoredAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 10)
)
if mibBuilder.loadTexts:
    upsPowerRestoredAlert.setStatus(
        ""
    )

logonPrimaryDCFailureAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 11)
)
logonPrimaryDCFailureAlert.setObjects(
    ("LanMgr-Alerts-II-MIB", "primaryDCName")
)
if mibBuilder.loadTexts:
    logonPrimaryDCFailureAlert.setStatus(
        ""
    )

replMasterFailurealert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 12)
)
replMasterFailurealert.setObjects(
    ("LanMgr-Alerts-II-MIB", "replMasterName")
)
if mibBuilder.loadTexts:
    replMasterFailurealert.setStatus(
        ""
    )

diskHotFixAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 13)
)
diskHotFixAlert.setObjects(
    ("LanMgr-Alerts-II-MIB", "diskDrive")
)
if mibBuilder.loadTexts:
    diskHotFixAlert.setStatus(
        ""
    )

diskHardErrorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 77, 2, 1, 0, 14)
)
diskHardErrorAlert.setObjects(
    ("LanMgr-Alerts-II-MIB", "diskDrive")
)
if mibBuilder.loadTexts:
    diskHardErrorAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LanMgr-Alerts-II-MIB",
    **{"alerts-2": alerts_2,
       "alerts": alerts,
       "bytesAvailAlert": bytesAvailAlert,
       "netIOErrorsAlert": netIOErrorsAlert,
       "serverErrorsAlert": serverErrorsAlert,
       "pwViolationsAlert": pwViolationsAlert,
       "accessViolationsAlert": accessViolationsAlert,
       "auditLogFullAlert": auditLogFullAlert,
       "auditLog80Alert": auditLog80Alert,
       "upsPowerOutWarnAlert": upsPowerOutWarnAlert,
       "upsPowerOutShutdownAlert": upsPowerOutShutdownAlert,
       "upsPowerRestoredAlert": upsPowerRestoredAlert,
       "logonPrimaryDCFailureAlert": logonPrimaryDCFailureAlert,
       "replMasterFailurealert": replMasterFailurealert,
       "diskHotFixAlert": diskHotFixAlert,
       "diskHardErrorAlert": diskHardErrorAlert,
       "alert-conditions": alert_conditions,
       "bytesAvailData": bytesAvailData,
       "numDiskDrives": numDiskDrives,
       "bytesAvailTable": bytesAvailTable,
       "bytesAvailEntry": bytesAvailEntry,
       "diskDrive": diskDrive,
       "bytesAvail": bytesAvail,
       "diskAlertLevel": diskAlertLevel,
       "netIOErrorsData": netIOErrorsData,
       "netIOAlertLevel": netIOAlertLevel,
       "numNetIOErrors": numNetIOErrors,
       "networkId": networkId,
       "netIOErrorStatus": netIOErrorStatus,
       "serverErrorsData": serverErrorsData,
       "serverErrorAlertLevel": serverErrorAlertLevel,
       "numServerErrors": numServerErrors,
       "serverErrorStatus": serverErrorStatus,
       "pwViolationsData": pwViolationsData,
       "pwLogonAlertLevel": pwLogonAlertLevel,
       "numPWViolations": numPWViolations,
       "passwordErrorStatus": passwordErrorStatus,
       "accessViolatData": accessViolatData,
       "accessAlertLevel": accessAlertLevel,
       "numAccessViolations": numAccessViolations,
       "accessErrorStatus": accessErrorStatus,
       "pdcFailData": pdcFailData,
       "primaryDCName": primaryDCName,
       "primaryDCFailed": primaryDCFailed,
       "rplFailData": rplFailData,
       "replMasterName": replMasterName,
       "replMasterFailed": replMasterFailed,
       "diskData": diskData,
       "diskHotFixes": diskHotFixes,
       "diskHardErrors": diskHardErrors,
       "auditLogData": auditLogData,
       "auditLogStatus": auditLogStatus,
       "powerData": powerData,
       "powerStatus": powerStatus,
       "alert-mgmt": alert_mgmt,
       "alertNameNumber": alertNameNumber,
       "alertNameTable": alertNameTable,
       "svAlertNameEntry": svAlertNameEntry,
       "svAlertName": svAlertName,
       "alertSchedule": alertSchedule}
)
