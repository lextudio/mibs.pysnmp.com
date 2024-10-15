# SNMP MIB module (NCR-CORESSTSYSTEMLOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NCR-CORESSTSYSTEMLOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:15 2024
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
_SstDeviceLogTable_Object = MibTable
sstDeviceLogTable = _SstDeviceLogTable_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7)
)
if mibBuilder.loadTexts:
    sstDeviceLogTable.setStatus("mandatory")
_SstLogEntry_Object = MibTableRow
sstLogEntry = _SstLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1)
)
sstLogEntry.setIndexNames(
    (0, "NCR-CORESSTSYSTEMLOG-MIB", "sstLogIndex"),
)
if mibBuilder.loadTexts:
    sstLogEntry.setStatus("mandatory")
_SstLogIndex_Type = Integer32
_SstLogIndex_Object = MibTableColumn
sstLogIndex = _SstLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1, 1),
    _SstLogIndex_Type()
)
sstLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLogIndex.setStatus("mandatory")
_SstLogDeviceName_Type = DisplayString
_SstLogDeviceName_Object = MibTableColumn
sstLogDeviceName = _SstLogDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1, 2),
    _SstLogDeviceName_Type()
)
sstLogDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLogDeviceName.setStatus("mandatory")
_SstLogServiceName_Type = DisplayString
_SstLogServiceName_Object = MibTableColumn
sstLogServiceName = _SstLogServiceName_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1, 3),
    _SstLogServiceName_Type()
)
sstLogServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLogServiceName.setStatus("mandatory")
_SstLogTCode_Type = OctetString
_SstLogTCode_Object = MibTableColumn
sstLogTCode = _SstLogTCode_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1, 4),
    _SstLogTCode_Type()
)
sstLogTCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLogTCode.setStatus("mandatory")
_SstLogSData_Type = OctetString
_SstLogSData_Object = MibTableColumn
sstLogSData = _SstLogSData_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1, 5),
    _SstLogSData_Type()
)
sstLogSData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLogSData.setStatus("mandatory")
_SstLogMData_Type = OctetString
_SstLogMData_Object = MibTableColumn
sstLogMData = _SstLogMData_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1, 6),
    _SstLogMData_Type()
)
sstLogMData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLogMData.setStatus("mandatory")
_SstLogDescription_Type = OctetString
_SstLogDescription_Object = MibTableColumn
sstLogDescription = _SstLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 191, 39, 13, 2, 4, 7, 1, 7),
    _SstLogDescription_Type()
)
sstLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstLogDescription.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NCR-CORESSTSYSTEMLOG-MIB",
    **{"ncr": ncr,
       "sst": sst,
       "sstCore": sstCore,
       "sstProduct": sstProduct,
       "sstObjs": sstObjs,
       "sstGeneral": sstGeneral,
       "sstDevice": sstDevice,
       "sstApplic": sstApplic,
       "sstLogs": sstLogs,
       "sstDeviceLogTable": sstDeviceLogTable,
       "sstLogEntry": sstLogEntry,
       "sstLogIndex": sstLogIndex,
       "sstLogDeviceName": sstLogDeviceName,
       "sstLogServiceName": sstLogServiceName,
       "sstLogTCode": sstLogTCode,
       "sstLogSData": sstLogSData,
       "sstLogMData": sstLogMData,
       "sstLogDescription": sstLogDescription}
)
