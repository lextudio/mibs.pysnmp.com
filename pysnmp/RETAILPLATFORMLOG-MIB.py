# SNMP MIB module (RETAILPLATFORMLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RETAILPLATFORMLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:56 2024
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



class NTSeverity(Integer32):
    """Custom type NTSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("auditFailure", 16),
          ("auditSuccess", 8),
          ("error", 1),
          ("information", 4),
          ("warning", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ncr_ObjectIdentity = ObjectIdentity
ncr = _Ncr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191)
)
_Ncr_products_ObjectIdentity = ObjectIdentity
ncr_products = _Ncr_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 1)
)
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 1, 33)
)
_LogSysLog_ObjectIdentity = ObjectIdentity
logSysLog = _LogSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1)
)
_LogSysLogTable_Object = MibTable
logSysLogTable = _LogSysLogTable_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1)
)
if mibBuilder.loadTexts:
    logSysLogTable.setStatus("mandatory")
_LogSysLogEntry_Object = MibTableRow
logSysLogEntry = _LogSysLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1)
)
logSysLogEntry.setIndexNames(
    (0, "RETAILPLATFORMLOG-MIB", "logSysLogIndex"),
)
if mibBuilder.loadTexts:
    logSysLogEntry.setStatus("mandatory")
_LogSysLogIndex_Type = Integer32
_LogSysLogIndex_Object = MibTableColumn
logSysLogIndex = _LogSysLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 1),
    _LogSysLogIndex_Type()
)
logSysLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogIndex.setStatus("mandatory")
_LogSysLogDate_Type = OctetString
_LogSysLogDate_Object = MibTableColumn
logSysLogDate = _LogSysLogDate_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 2),
    _LogSysLogDate_Type()
)
logSysLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogDate.setStatus("mandatory")
_LogSysLogTime_Type = OctetString
_LogSysLogTime_Object = MibTableColumn
logSysLogTime = _LogSysLogTime_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 3),
    _LogSysLogTime_Type()
)
logSysLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogTime.setStatus("mandatory")
_LogSysLogUser_Type = OctetString
_LogSysLogUser_Object = MibTableColumn
logSysLogUser = _LogSysLogUser_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 4),
    _LogSysLogUser_Type()
)
logSysLogUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogUser.setStatus("mandatory")
_LogSysLogComputer_Type = OctetString
_LogSysLogComputer_Object = MibTableColumn
logSysLogComputer = _LogSysLogComputer_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 5),
    _LogSysLogComputer_Type()
)
logSysLogComputer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogComputer.setStatus("mandatory")
_LogSysLogEventID_Type = Integer32
_LogSysLogEventID_Object = MibTableColumn
logSysLogEventID = _LogSysLogEventID_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 6),
    _LogSysLogEventID_Type()
)
logSysLogEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogEventID.setStatus("mandatory")
_LogSysLogSource_Type = OctetString
_LogSysLogSource_Object = MibTableColumn
logSysLogSource = _LogSysLogSource_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 7),
    _LogSysLogSource_Type()
)
logSysLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogSource.setStatus("mandatory")
_LogSysLogType_Type = NTSeverity
_LogSysLogType_Object = MibTableColumn
logSysLogType = _LogSysLogType_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 8),
    _LogSysLogType_Type()
)
logSysLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogType.setStatus("mandatory")
_LogSysLogCategory_Type = OctetString
_LogSysLogCategory_Object = MibTableColumn
logSysLogCategory = _LogSysLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 9),
    _LogSysLogCategory_Type()
)
logSysLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogCategory.setStatus("mandatory")
_LogSysLogDescription_Type = OctetString
_LogSysLogDescription_Object = MibTableColumn
logSysLogDescription = _LogSysLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 10),
    _LogSysLogDescription_Type()
)
logSysLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogDescription.setStatus("mandatory")
_LogSysLogData_Type = OctetString
_LogSysLogData_Object = MibTableColumn
logSysLogData = _LogSysLogData_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 1, 1, 11),
    _LogSysLogData_Type()
)
logSysLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogData.setStatus("mandatory")
_LogSysLogSize_Type = Integer32
_LogSysLogSize_Object = MibScalar
logSysLogSize = _LogSysLogSize_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 2),
    _LogSysLogSize_Type()
)
logSysLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSysLogSize.setStatus("mandatory")
_LogSysLogReqSize_Type = Integer32
_LogSysLogReqSize_Object = MibScalar
logSysLogReqSize = _LogSysLogReqSize_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 1, 3),
    _LogSysLogReqSize_Type()
)
logSysLogReqSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSysLogReqSize.setStatus("mandatory")
_LogSecLog_ObjectIdentity = ObjectIdentity
logSecLog = _LogSecLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2)
)
_LogSecLogTable_Object = MibTable
logSecLogTable = _LogSecLogTable_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1)
)
if mibBuilder.loadTexts:
    logSecLogTable.setStatus("mandatory")
_LogSecLogEntry_Object = MibTableRow
logSecLogEntry = _LogSecLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1)
)
logSecLogEntry.setIndexNames(
    (0, "RETAILPLATFORMLOG-MIB", "logSecLogIndex"),
)
if mibBuilder.loadTexts:
    logSecLogEntry.setStatus("mandatory")
_LogSecLogIndex_Type = Integer32
_LogSecLogIndex_Object = MibTableColumn
logSecLogIndex = _LogSecLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 1),
    _LogSecLogIndex_Type()
)
logSecLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogIndex.setStatus("mandatory")
_LogSecLogDate_Type = OctetString
_LogSecLogDate_Object = MibTableColumn
logSecLogDate = _LogSecLogDate_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 2),
    _LogSecLogDate_Type()
)
logSecLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogDate.setStatus("mandatory")
_LogSecLogTime_Type = OctetString
_LogSecLogTime_Object = MibTableColumn
logSecLogTime = _LogSecLogTime_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 3),
    _LogSecLogTime_Type()
)
logSecLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogTime.setStatus("mandatory")
_LogSecLogUser_Type = OctetString
_LogSecLogUser_Object = MibTableColumn
logSecLogUser = _LogSecLogUser_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 4),
    _LogSecLogUser_Type()
)
logSecLogUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogUser.setStatus("mandatory")
_LogSecLogComputer_Type = OctetString
_LogSecLogComputer_Object = MibTableColumn
logSecLogComputer = _LogSecLogComputer_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 5),
    _LogSecLogComputer_Type()
)
logSecLogComputer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogComputer.setStatus("mandatory")
_LogSecLogEventID_Type = Integer32
_LogSecLogEventID_Object = MibTableColumn
logSecLogEventID = _LogSecLogEventID_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 6),
    _LogSecLogEventID_Type()
)
logSecLogEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogEventID.setStatus("mandatory")
_LogSecLogSource_Type = OctetString
_LogSecLogSource_Object = MibTableColumn
logSecLogSource = _LogSecLogSource_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 7),
    _LogSecLogSource_Type()
)
logSecLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogSource.setStatus("mandatory")
_LogSecLogType_Type = NTSeverity
_LogSecLogType_Object = MibTableColumn
logSecLogType = _LogSecLogType_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 8),
    _LogSecLogType_Type()
)
logSecLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogType.setStatus("mandatory")
_LogSecLogCategory_Type = OctetString
_LogSecLogCategory_Object = MibTableColumn
logSecLogCategory = _LogSecLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 9),
    _LogSecLogCategory_Type()
)
logSecLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogCategory.setStatus("mandatory")
_LogSecLogDescription_Type = OctetString
_LogSecLogDescription_Object = MibTableColumn
logSecLogDescription = _LogSecLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 10),
    _LogSecLogDescription_Type()
)
logSecLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogDescription.setStatus("mandatory")
_LogSecLogData_Type = OctetString
_LogSecLogData_Object = MibTableColumn
logSecLogData = _LogSecLogData_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 1, 1, 11),
    _LogSecLogData_Type()
)
logSecLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogData.setStatus("mandatory")
_LogSecLogSize_Type = Integer32
_LogSecLogSize_Object = MibScalar
logSecLogSize = _LogSecLogSize_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 2),
    _LogSecLogSize_Type()
)
logSecLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logSecLogSize.setStatus("mandatory")
_LogSecLogReqSize_Type = Integer32
_LogSecLogReqSize_Object = MibScalar
logSecLogReqSize = _LogSecLogReqSize_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 2, 3),
    _LogSecLogReqSize_Type()
)
logSecLogReqSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logSecLogReqSize.setStatus("mandatory")
_LogAppLog_ObjectIdentity = ObjectIdentity
logAppLog = _LogAppLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3)
)
_LogAppLogTable_Object = MibTable
logAppLogTable = _LogAppLogTable_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1)
)
if mibBuilder.loadTexts:
    logAppLogTable.setStatus("mandatory")
_LogAppLogEntry_Object = MibTableRow
logAppLogEntry = _LogAppLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1)
)
logAppLogEntry.setIndexNames(
    (0, "RETAILPLATFORMLOG-MIB", "logAppLogIndex"),
)
if mibBuilder.loadTexts:
    logAppLogEntry.setStatus("mandatory")
_LogAppLogIndex_Type = Integer32
_LogAppLogIndex_Object = MibTableColumn
logAppLogIndex = _LogAppLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 1),
    _LogAppLogIndex_Type()
)
logAppLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogIndex.setStatus("mandatory")
_LogAppLogDate_Type = OctetString
_LogAppLogDate_Object = MibTableColumn
logAppLogDate = _LogAppLogDate_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 2),
    _LogAppLogDate_Type()
)
logAppLogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogDate.setStatus("mandatory")
_LogAppLogTime_Type = OctetString
_LogAppLogTime_Object = MibTableColumn
logAppLogTime = _LogAppLogTime_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 3),
    _LogAppLogTime_Type()
)
logAppLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogTime.setStatus("mandatory")
_LogAppLogUser_Type = OctetString
_LogAppLogUser_Object = MibTableColumn
logAppLogUser = _LogAppLogUser_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 4),
    _LogAppLogUser_Type()
)
logAppLogUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogUser.setStatus("mandatory")
_LogAppLogComputer_Type = OctetString
_LogAppLogComputer_Object = MibTableColumn
logAppLogComputer = _LogAppLogComputer_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 5),
    _LogAppLogComputer_Type()
)
logAppLogComputer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogComputer.setStatus("mandatory")
_LogAppLogEventID_Type = Integer32
_LogAppLogEventID_Object = MibTableColumn
logAppLogEventID = _LogAppLogEventID_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 6),
    _LogAppLogEventID_Type()
)
logAppLogEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogEventID.setStatus("mandatory")
_LogAppLogSource_Type = OctetString
_LogAppLogSource_Object = MibTableColumn
logAppLogSource = _LogAppLogSource_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 7),
    _LogAppLogSource_Type()
)
logAppLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogSource.setStatus("mandatory")
_LogAppLogType_Type = NTSeverity
_LogAppLogType_Object = MibTableColumn
logAppLogType = _LogAppLogType_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 8),
    _LogAppLogType_Type()
)
logAppLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogType.setStatus("mandatory")
_LogAppLogCategory_Type = OctetString
_LogAppLogCategory_Object = MibTableColumn
logAppLogCategory = _LogAppLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 9),
    _LogAppLogCategory_Type()
)
logAppLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogCategory.setStatus("mandatory")
_LogAppLogDescription_Type = OctetString
_LogAppLogDescription_Object = MibTableColumn
logAppLogDescription = _LogAppLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 10),
    _LogAppLogDescription_Type()
)
logAppLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogDescription.setStatus("mandatory")
_LogAppLogData_Type = OctetString
_LogAppLogData_Object = MibTableColumn
logAppLogData = _LogAppLogData_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 1, 1, 11),
    _LogAppLogData_Type()
)
logAppLogData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogData.setStatus("mandatory")
_LogAppLogSize_Type = Integer32
_LogAppLogSize_Object = MibScalar
logAppLogSize = _LogAppLogSize_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 2),
    _LogAppLogSize_Type()
)
logAppLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAppLogSize.setStatus("mandatory")
_LogAppLogReqSize_Type = Integer32
_LogAppLogReqSize_Object = MibScalar
logAppLogReqSize = _LogAppLogReqSize_Object(
    (1, 3, 6, 1, 4, 1, 191, 1, 33, 3, 3),
    _LogAppLogReqSize_Type()
)
logAppLogReqSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logAppLogReqSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RETAILPLATFORMLOG-MIB",
    **{"NTSeverity": NTSeverity,
       "ncr": ncr,
       "ncr-products": ncr_products,
       "log": log,
       "logSysLog": logSysLog,
       "logSysLogTable": logSysLogTable,
       "logSysLogEntry": logSysLogEntry,
       "logSysLogIndex": logSysLogIndex,
       "logSysLogDate": logSysLogDate,
       "logSysLogTime": logSysLogTime,
       "logSysLogUser": logSysLogUser,
       "logSysLogComputer": logSysLogComputer,
       "logSysLogEventID": logSysLogEventID,
       "logSysLogSource": logSysLogSource,
       "logSysLogType": logSysLogType,
       "logSysLogCategory": logSysLogCategory,
       "logSysLogDescription": logSysLogDescription,
       "logSysLogData": logSysLogData,
       "logSysLogSize": logSysLogSize,
       "logSysLogReqSize": logSysLogReqSize,
       "logSecLog": logSecLog,
       "logSecLogTable": logSecLogTable,
       "logSecLogEntry": logSecLogEntry,
       "logSecLogIndex": logSecLogIndex,
       "logSecLogDate": logSecLogDate,
       "logSecLogTime": logSecLogTime,
       "logSecLogUser": logSecLogUser,
       "logSecLogComputer": logSecLogComputer,
       "logSecLogEventID": logSecLogEventID,
       "logSecLogSource": logSecLogSource,
       "logSecLogType": logSecLogType,
       "logSecLogCategory": logSecLogCategory,
       "logSecLogDescription": logSecLogDescription,
       "logSecLogData": logSecLogData,
       "logSecLogSize": logSecLogSize,
       "logSecLogReqSize": logSecLogReqSize,
       "logAppLog": logAppLog,
       "logAppLogTable": logAppLogTable,
       "logAppLogEntry": logAppLogEntry,
       "logAppLogIndex": logAppLogIndex,
       "logAppLogDate": logAppLogDate,
       "logAppLogTime": logAppLogTime,
       "logAppLogUser": logAppLogUser,
       "logAppLogComputer": logAppLogComputer,
       "logAppLogEventID": logAppLogEventID,
       "logAppLogSource": logAppLogSource,
       "logAppLogType": logAppLogType,
       "logAppLogCategory": logAppLogCategory,
       "logAppLogDescription": logAppLogDescription,
       "logAppLogData": logAppLogData,
       "logAppLogSize": logAppLogSize,
       "logAppLogReqSize": logAppLogReqSize}
)
