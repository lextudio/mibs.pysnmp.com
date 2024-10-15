# SNMP MIB module (NCR-CORESSTSWARELOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NCR-CORESSTCOMMSLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:13 2024
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

(TruthValue,) = mibBuilder.importSymbols(
    "RFC1253-MIB",
    "TruthValue")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ncr_ObjectIdentity = ObjectIdentity
ncr = _Ncr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191)
)
_Sst_ObjectIdentity = ObjectIdentity
sst = _Sst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39)
)
_SstCore_ObjectIdentity = ObjectIdentity
sstCore = _SstCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39, 1)
)
_SstProduct_ObjectIdentity = ObjectIdentity
sstProduct = _SstProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39, 13)
)
_SstObjs_ObjectIdentity = ObjectIdentity
sstObjs = _SstObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2)
)
_SstGeneral_ObjectIdentity = ObjectIdentity
sstGeneral = _SstGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 1)
)
_SstDevice_ObjectIdentity = ObjectIdentity
sstDevice = _SstDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 2)
)
_SstApplic_ObjectIdentity = ObjectIdentity
sstApplic = _SstApplic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 3)
)
_SstLogs_ObjectIdentity = ObjectIdentity
sstLogs = _SstLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4)
)
_SstSWareLogTable_Object = MibTable
sstSWareLogTable = _SstSWareLogTable_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9)
)
if mibBuilder.loadTexts:
    sstSWareLogTable.setStatus("mandatory")
_SstSWareLogEntry_Object = MibTableRow
sstSWareLogEntry = _SstSWareLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1)
)
sstSWareLogEntry.setIndexNames(
    (0, "NCR-CORESSTSWARELOG-MIB", "sstSWareLogIndex"),
)
if mibBuilder.loadTexts:
    sstSWareLogEntry.setStatus("mandatory")
_SstSWareLogIndex_Type = Integer32
_SstSWareLogIndex_Object = MibTableColumn
sstSWareLogIndex = _SstSWareLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 1),
    _SstSWareLogIndex_Type()
)
sstSWareLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogIndex.setStatus("mandatory")
_SstSWareLogLineNumber_Type = Integer32
_SstSWareLogLineNumber_Object = MibTableColumn
sstSWareLogLineNumber = _SstSWareLogLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 2),
    _SstSWareLogLineNumber_Type()
)
sstSWareLogLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogLineNumber.setStatus("mandatory")
_SstSWareLogSourceName_Type = DisplayString
_SstSWareLogSourceName_Object = MibTableColumn
sstSWareLogSourceName = _SstSWareLogSourceName_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 3),
    _SstSWareLogSourceName_Type()
)
sstSWareLogSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogSourceName.setStatus("mandatory")
_SstSWareLogProcName_Type = DisplayString
_SstSWareLogProcName_Object = MibTableColumn
sstSWareLogProcName = _SstSWareLogProcName_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 4),
    _SstSWareLogProcName_Type()
)
sstSWareLogProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogProcName.setStatus("mandatory")
_SstSWareLogThrdName_Type = DisplayString
_SstSWareLogThrdName_Object = MibTableColumn
sstSWareLogThrdName = _SstSWareLogThrdName_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 5),
    _SstSWareLogThrdName_Type()
)
sstSWareLogThrdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogThrdName.setStatus("mandatory")
_SstSWareLogDLLName_Type = DisplayString
_SstSWareLogDLLName_Object = MibTableColumn
sstSWareLogDLLName = _SstSWareLogDLLName_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 6),
    _SstSWareLogDLLName_Type()
)
sstSWareLogDLLName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogDLLName.setStatus("mandatory")
_SstSWareLogEventId_Type = Integer32
_SstSWareLogEventId_Object = MibTableColumn
sstSWareLogEventId = _SstSWareLogEventId_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 7),
    _SstSWareLogEventId_Type()
)
sstSWareLogEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogEventId.setStatus("mandatory")
_SstSWareLogLevel_Type = Integer32
_SstSWareLogLevel_Object = MibTableColumn
sstSWareLogLevel = _SstSWareLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 8),
    _SstSWareLogLevel_Type()
)
sstSWareLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogLevel.setStatus("mandatory")
_SstSWareLogReason_Type = Integer32
_SstSWareLogReason_Object = MibTableColumn
sstSWareLogReason = _SstSWareLogReason_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 9),
    _SstSWareLogReason_Type()
)
sstSWareLogReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogReason.setStatus("mandatory")
_SstSWareLogBinaryType_Type = Integer32
_SstSWareLogBinaryType_Object = MibTableColumn
sstSWareLogBinaryType = _SstSWareLogBinaryType_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 10),
    _SstSWareLogBinaryType_Type()
)
sstSWareLogBinaryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogBinaryType.setStatus("mandatory")
_SstSWareLogBinaryData_Type = OctetString
_SstSWareLogBinaryData_Object = MibTableColumn
sstSWareLogBinaryData = _SstSWareLogBinaryData_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 11),
    _SstSWareLogBinaryData_Type()
)
sstSWareLogBinaryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogBinaryData.setStatus("mandatory")
_SstSWareLogStrData_Type = DisplayString
_SstSWareLogStrData_Object = MibTableColumn
sstSWareLogStrData = _SstSWareLogStrData_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 9, 1, 12),
    _SstSWareLogStrData_Type()
)
sstSWareLogStrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSWareLogStrData.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NCR-CORESSTSWARELOG-MIB",
    **{"ncr": ncr,
       "sst": sst,
       "sstCore": sstCore,
       "sstProduct": sstProduct,
       "sstObjs": sstObjs,
       "sstGeneral": sstGeneral,
       "sstDevice": sstDevice,
       "sstApplic": sstApplic,
       "sstLogs": sstLogs,
       "sstSWareLogTable": sstSWareLogTable,
       "sstSWareLogEntry": sstSWareLogEntry,
       "sstSWareLogIndex": sstSWareLogIndex,
       "sstSWareLogLineNumber": sstSWareLogLineNumber,
       "sstSWareLogSourceName": sstSWareLogSourceName,
       "sstSWareLogProcName": sstSWareLogProcName,
       "sstSWareLogThrdName": sstSWareLogThrdName,
       "sstSWareLogDLLName": sstSWareLogDLLName,
       "sstSWareLogEventId": sstSWareLogEventId,
       "sstSWareLogLevel": sstSWareLogLevel,
       "sstSWareLogReason": sstSWareLogReason,
       "sstSWareLogBinaryType": sstSWareLogBinaryType,
       "sstSWareLogBinaryData": sstSWareLogBinaryData,
       "sstSWareLogStrData": sstSWareLogStrData}
)
