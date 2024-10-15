# SNMP MIB module (NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:39 2024
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

(NoiAdditionalText,
 NoiAlarmTableCount,
 NoiEventTime) = mibBuilder.importSymbols(
    "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-COMMON-DEFINITION",
    "NoiAdditionalText",
    "NoiAlarmTableCount",
    "NoiEventTime")

(NoiMeasurementActivationError,
 NoiMeasurementFileDirectory,
 NoiMeasurementFileName,
 NoiMeasurementFileTransfer,
 NoiMeasurementJobStatus,
 NoiMeasurementResultIdentifier,
 NoiMeasurementResultTransfer) = mibBuilder.importSymbols(
    "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-COMMON-DEFINITION",
    "NoiMeasurementActivationError",
    "NoiMeasurementFileDirectory",
    "NoiMeasurementFileName",
    "NoiMeasurementFileTransfer",
    "NoiMeasurementJobStatus",
    "NoiMeasurementResultIdentifier",
    "NoiMeasurementResultTransfer")

(noiOpenInterfaceModule,
 noiPmCompliance,
 noiPmNotification,
 noiPmTable,
 noiPmVariable) = mibBuilder.importSymbols(
    "NOKIA-NE3S-REGISTRATION-MIB",
    "noiOpenInterfaceModule",
    "noiPmCompliance",
    "noiPmNotification",
    "noiPmTable",
    "noiPmVariable")

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

noiSnmpPmIrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 94, 7, 1, 1, 4)
)
noiSnmpPmIrp.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NoiPmIrpVersion_Type(OctetString):
    """Custom type noiPmIrpVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_NoiPmIrpVersion_Type.__name__ = "OctetString"
_NoiPmIrpVersion_Object = MibScalar
noiPmIrpVersion = _NoiPmIrpVersion_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 1),
    _NoiPmIrpVersion_Type()
)
noiPmIrpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiPmIrpVersion.setStatus("current")
_NoiPmFileTransferProtocol_Type = NoiMeasurementFileTransfer
_NoiPmFileTransferProtocol_Object = MibScalar
noiPmFileTransferProtocol = _NoiPmFileTransferProtocol_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 2),
    _NoiPmFileTransferProtocol_Type()
)
noiPmFileTransferProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiPmFileTransferProtocol.setStatus("current")
_NoiPmResultTransfer_Type = NoiMeasurementResultTransfer
_NoiPmResultTransfer_Object = MibScalar
noiPmResultTransfer = _NoiPmResultTransfer_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 3),
    _NoiPmResultTransfer_Type()
)
noiPmResultTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiPmResultTransfer.setStatus("current")
_NoiMeasurementScheduleFileDirectory_Type = NoiMeasurementFileDirectory
_NoiMeasurementScheduleFileDirectory_Object = MibScalar
noiMeasurementScheduleFileDirectory = _NoiMeasurementScheduleFileDirectory_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 4),
    _NoiMeasurementScheduleFileDirectory_Type()
)
noiMeasurementScheduleFileDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiMeasurementScheduleFileDirectory.setStatus("current")
_NoiMeasurementRepositoryDirectory_Type = NoiMeasurementFileDirectory
_NoiMeasurementRepositoryDirectory_Object = MibScalar
noiMeasurementRepositoryDirectory = _NoiMeasurementRepositoryDirectory_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 5),
    _NoiMeasurementRepositoryDirectory_Type()
)
noiMeasurementRepositoryDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiMeasurementRepositoryDirectory.setStatus("current")
_NoiMeasurementRepositoryFile_Type = NoiMeasurementFileName
_NoiMeasurementRepositoryFile_Object = MibScalar
noiMeasurementRepositoryFile = _NoiMeasurementRepositoryFile_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 6),
    _NoiMeasurementRepositoryFile_Type()
)
noiMeasurementRepositoryFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiMeasurementRepositoryFile.setStatus("current")
_NoiMeasurementJobStatus_Type = NoiMeasurementJobStatus
_NoiMeasurementJobStatus_Object = MibScalar
noiMeasurementJobStatus = _NoiMeasurementJobStatus_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 7),
    _NoiMeasurementJobStatus_Type()
)
noiMeasurementJobStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiMeasurementJobStatus.setStatus("current")
_NoiMeasurementActivationError_Type = NoiMeasurementActivationError
_NoiMeasurementActivationError_Object = MibScalar
noiMeasurementActivationError = _NoiMeasurementActivationError_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 8),
    _NoiMeasurementActivationError_Type()
)
noiMeasurementActivationError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiMeasurementActivationError.setStatus("current")
_NoiPmAdditionalText_Type = NoiAdditionalText
_NoiPmAdditionalText_Object = MibScalar
noiPmAdditionalText = _NoiPmAdditionalText_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 9),
    _NoiPmAdditionalText_Type()
)
noiPmAdditionalText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiPmAdditionalText.setStatus("current")
_NoiPmFileStoringPeriod_Type = Integer32
_NoiPmFileStoringPeriod_Object = MibScalar
noiPmFileStoringPeriod = _NoiPmFileStoringPeriod_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 2, 10),
    _NoiPmFileStoringPeriod_Type()
)
noiPmFileStoringPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    noiPmFileStoringPeriod.setStatus("current")
_NoiMeasurementResultTableCount_Type = NoiAlarmTableCount
_NoiMeasurementResultTableCount_Object = MibScalar
noiMeasurementResultTableCount = _NoiMeasurementResultTableCount_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 1),
    _NoiMeasurementResultTableCount_Type()
)
noiMeasurementResultTableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiMeasurementResultTableCount.setStatus("current")
_NoiMeasurementResultTableMaxCount_Type = NoiAlarmTableCount
_NoiMeasurementResultTableMaxCount_Object = MibScalar
noiMeasurementResultTableMaxCount = _NoiMeasurementResultTableMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 2),
    _NoiMeasurementResultTableMaxCount_Type()
)
noiMeasurementResultTableMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiMeasurementResultTableMaxCount.setStatus("current")
_NoiPmLastMeasurementResultId_Type = NoiMeasurementResultIdentifier
_NoiPmLastMeasurementResultId_Object = MibScalar
noiPmLastMeasurementResultId = _NoiPmLastMeasurementResultId_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 3),
    _NoiPmLastMeasurementResultId_Type()
)
noiPmLastMeasurementResultId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiPmLastMeasurementResultId.setStatus("current")
_NoiMeasurementResultTable_Object = MibTable
noiMeasurementResultTable = _NoiMeasurementResultTable_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4)
)
if mibBuilder.loadTexts:
    noiMeasurementResultTable.setStatus("current")
_NoiMeasurementResultEntry_Object = MibTableRow
noiMeasurementResultEntry = _NoiMeasurementResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1)
)
noiMeasurementResultEntry.setIndexNames(
    (0, "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"),
)
if mibBuilder.loadTexts:
    noiMeasurementResultEntry.setStatus("current")
_NoiMeasurementResultIdentifier_Type = NoiMeasurementResultIdentifier
_NoiMeasurementResultIdentifier_Object = MibTableColumn
noiMeasurementResultIdentifier = _NoiMeasurementResultIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 1),
    _NoiMeasurementResultIdentifier_Type()
)
noiMeasurementResultIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiMeasurementResultIdentifier.setStatus("current")
_NoiMeasurementFileName_Type = NoiMeasurementFileName
_NoiMeasurementFileName_Object = MibTableColumn
noiMeasurementFileName = _NoiMeasurementFileName_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 2),
    _NoiMeasurementFileName_Type()
)
noiMeasurementFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiMeasurementFileName.setStatus("current")
_NoiMeasurementFileDirectory_Type = NoiMeasurementFileDirectory
_NoiMeasurementFileDirectory_Object = MibTableColumn
noiMeasurementFileDirectory = _NoiMeasurementFileDirectory_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 3),
    _NoiMeasurementFileDirectory_Type()
)
noiMeasurementFileDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiMeasurementFileDirectory.setStatus("current")
_NoiPmEventTime_Type = NoiEventTime
_NoiPmEventTime_Object = MibTableColumn
noiPmEventTime = _NoiPmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 4, 4, 1, 4),
    _NoiPmEventTime_Type()
)
noiPmEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noiPmEventTime.setStatus("current")

# Managed Objects groups

noiPmMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 2)
)
noiPmMandatoryGroup.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmIrpVersion"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmLastMeasurementResultId"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementScheduleFileDirectory"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableCount"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableMaxCount"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileDirectory"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileName"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmFileStoringPeriod"))
)
if mibBuilder.loadTexts:
    noiPmMandatoryGroup.setStatus("current")


# Notification objects

noiMeasurementResultReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 3, 0, 1)
)
noiMeasurementResultReady.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultIdentifier"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileDirectory"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementFileName"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"))
)
if mibBuilder.loadTexts:
    noiMeasurementResultReady.setStatus(
        "current"
    )

noiMeasurementResultTableRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 3, 0, 2)
)
noiMeasurementResultTableRebuild.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmAdditionalText"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiPmEventTime"))
)
if mibBuilder.loadTexts:
    noiMeasurementResultTableRebuild.setStatus(
        "current"
    )


# Notifications groups

noiPmNotificationOptionalGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 3)
)
noiPmNotificationOptionalGroup.setObjects(
      *(("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultReady"),
        ("NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP", "noiMeasurementResultTableRebuild"))
)
if mibBuilder.loadTexts:
    noiPmNotificationOptionalGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

noiPmIRPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 94, 7, 3, 6, 1)
)
if mibBuilder.loadTexts:
    noiPmIRPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NOKIA-ENHANCED-SNMP-SOLUTION-SUITE-PM-IRP",
    **{"noiSnmpPmIrp": noiSnmpPmIrp,
       "noiPmIrpVersion": noiPmIrpVersion,
       "noiPmFileTransferProtocol": noiPmFileTransferProtocol,
       "noiPmResultTransfer": noiPmResultTransfer,
       "noiMeasurementScheduleFileDirectory": noiMeasurementScheduleFileDirectory,
       "noiMeasurementRepositoryDirectory": noiMeasurementRepositoryDirectory,
       "noiMeasurementRepositoryFile": noiMeasurementRepositoryFile,
       "noiMeasurementJobStatus": noiMeasurementJobStatus,
       "noiMeasurementActivationError": noiMeasurementActivationError,
       "noiPmAdditionalText": noiPmAdditionalText,
       "noiPmFileStoringPeriod": noiPmFileStoringPeriod,
       "noiMeasurementResultReady": noiMeasurementResultReady,
       "noiMeasurementResultTableRebuild": noiMeasurementResultTableRebuild,
       "noiMeasurementResultTableCount": noiMeasurementResultTableCount,
       "noiMeasurementResultTableMaxCount": noiMeasurementResultTableMaxCount,
       "noiPmLastMeasurementResultId": noiPmLastMeasurementResultId,
       "noiMeasurementResultTable": noiMeasurementResultTable,
       "noiMeasurementResultEntry": noiMeasurementResultEntry,
       "noiMeasurementResultIdentifier": noiMeasurementResultIdentifier,
       "noiMeasurementFileName": noiMeasurementFileName,
       "noiMeasurementFileDirectory": noiMeasurementFileDirectory,
       "noiPmEventTime": noiPmEventTime,
       "noiPmIRPCompliance": noiPmIRPCompliance,
       "noiPmMandatoryGroup": noiPmMandatoryGroup,
       "noiPmNotificationOptionalGroup": noiPmNotificationOptionalGroup}
)
