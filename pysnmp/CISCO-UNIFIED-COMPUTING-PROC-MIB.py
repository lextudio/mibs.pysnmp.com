# SNMP MIB module (CISCO-UNIFIED-COMPUTING-PROC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-PROC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:13 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsProcStatAdminState,) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsProcStatAdminState")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsProcObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsProcDoerTable_Object = MibTable
cucsProcDoerTable = _CucsProcDoerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1)
)
if mibBuilder.loadTexts:
    cucsProcDoerTable.setStatus("current")
_CucsProcDoerEntry_Object = MibTableRow
cucsProcDoerEntry = _CucsProcDoerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1)
)
cucsProcDoerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcDoerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcDoerEntry.setStatus("current")
_CucsProcDoerInstanceId_Type = CucsManagedObjectId
_CucsProcDoerInstanceId_Object = MibTableColumn
cucsProcDoerInstanceId = _CucsProcDoerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 1),
    _CucsProcDoerInstanceId_Type()
)
cucsProcDoerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcDoerInstanceId.setStatus("current")
_CucsProcDoerDn_Type = CucsManagedObjectDn
_CucsProcDoerDn_Object = MibTableColumn
cucsProcDoerDn = _CucsProcDoerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 2),
    _CucsProcDoerDn_Type()
)
cucsProcDoerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcDoerDn.setStatus("current")
_CucsProcDoerRn_Type = SnmpAdminString
_CucsProcDoerRn_Object = MibTableColumn
cucsProcDoerRn = _CucsProcDoerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 3),
    _CucsProcDoerRn_Type()
)
cucsProcDoerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcDoerRn.setStatus("current")
_CucsProcDoerId_Type = Gauge32
_CucsProcDoerId_Object = MibTableColumn
cucsProcDoerId = _CucsProcDoerId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 4),
    _CucsProcDoerId_Type()
)
cucsProcDoerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcDoerId.setStatus("current")
_CucsProcDoerName_Type = SnmpAdminString
_CucsProcDoerName_Object = MibTableColumn
cucsProcDoerName = _CucsProcDoerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 1, 1, 5),
    _CucsProcDoerName_Type()
)
cucsProcDoerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcDoerName.setStatus("current")
_CucsProcManagerTable_Object = MibTable
cucsProcManagerTable = _CucsProcManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2)
)
if mibBuilder.loadTexts:
    cucsProcManagerTable.setStatus("current")
_CucsProcManagerEntry_Object = MibTableRow
cucsProcManagerEntry = _CucsProcManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1)
)
cucsProcManagerEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcManagerInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcManagerEntry.setStatus("current")
_CucsProcManagerInstanceId_Type = CucsManagedObjectId
_CucsProcManagerInstanceId_Object = MibTableColumn
cucsProcManagerInstanceId = _CucsProcManagerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1, 1),
    _CucsProcManagerInstanceId_Type()
)
cucsProcManagerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcManagerInstanceId.setStatus("current")
_CucsProcManagerDn_Type = CucsManagedObjectDn
_CucsProcManagerDn_Object = MibTableColumn
cucsProcManagerDn = _CucsProcManagerDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1, 2),
    _CucsProcManagerDn_Type()
)
cucsProcManagerDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcManagerDn.setStatus("current")
_CucsProcManagerRn_Type = SnmpAdminString
_CucsProcManagerRn_Object = MibTableColumn
cucsProcManagerRn = _CucsProcManagerRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 2, 1, 3),
    _CucsProcManagerRn_Type()
)
cucsProcManagerRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcManagerRn.setStatus("current")
_CucsProcPrtTable_Object = MibTable
cucsProcPrtTable = _CucsProcPrtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3)
)
if mibBuilder.loadTexts:
    cucsProcPrtTable.setStatus("current")
_CucsProcPrtEntry_Object = MibTableRow
cucsProcPrtEntry = _CucsProcPrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1)
)
cucsProcPrtEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcPrtInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcPrtEntry.setStatus("current")
_CucsProcPrtInstanceId_Type = CucsManagedObjectId
_CucsProcPrtInstanceId_Object = MibTableColumn
cucsProcPrtInstanceId = _CucsProcPrtInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 1),
    _CucsProcPrtInstanceId_Type()
)
cucsProcPrtInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcPrtInstanceId.setStatus("current")
_CucsProcPrtDn_Type = CucsManagedObjectDn
_CucsProcPrtDn_Object = MibTableColumn
cucsProcPrtDn = _CucsProcPrtDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 2),
    _CucsProcPrtDn_Type()
)
cucsProcPrtDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtDn.setStatus("current")
_CucsProcPrtRn_Type = SnmpAdminString
_CucsProcPrtRn_Object = MibTableColumn
cucsProcPrtRn = _CucsProcPrtRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 3),
    _CucsProcPrtRn_Type()
)
cucsProcPrtRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtRn.setStatus("current")
_CucsProcPrtId_Type = Gauge32
_CucsProcPrtId_Object = MibTableColumn
cucsProcPrtId = _CucsProcPrtId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 4),
    _CucsProcPrtId_Type()
)
cucsProcPrtId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtId.setStatus("current")
_CucsProcPrtName_Type = SnmpAdminString
_CucsProcPrtName_Object = MibTableColumn
cucsProcPrtName = _CucsProcPrtName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 3, 1, 5),
    _CucsProcPrtName_Type()
)
cucsProcPrtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtName.setStatus("current")
_CucsProcPrtCountsTable_Object = MibTable
cucsProcPrtCountsTable = _CucsProcPrtCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4)
)
if mibBuilder.loadTexts:
    cucsProcPrtCountsTable.setStatus("current")
_CucsProcPrtCountsEntry_Object = MibTableRow
cucsProcPrtCountsEntry = _CucsProcPrtCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1)
)
cucsProcPrtCountsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcPrtCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcPrtCountsEntry.setStatus("current")
_CucsProcPrtCountsInstanceId_Type = CucsManagedObjectId
_CucsProcPrtCountsInstanceId_Object = MibTableColumn
cucsProcPrtCountsInstanceId = _CucsProcPrtCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 1),
    _CucsProcPrtCountsInstanceId_Type()
)
cucsProcPrtCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcPrtCountsInstanceId.setStatus("current")
_CucsProcPrtCountsDn_Type = CucsManagedObjectDn
_CucsProcPrtCountsDn_Object = MibTableColumn
cucsProcPrtCountsDn = _CucsProcPrtCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 2),
    _CucsProcPrtCountsDn_Type()
)
cucsProcPrtCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtCountsDn.setStatus("current")
_CucsProcPrtCountsRn_Type = SnmpAdminString
_CucsProcPrtCountsRn_Object = MibTableColumn
cucsProcPrtCountsRn = _CucsProcPrtCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 3),
    _CucsProcPrtCountsRn_Type()
)
cucsProcPrtCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtCountsRn.setStatus("current")
_CucsProcPrtCountsDbtxs_Type = Gauge32
_CucsProcPrtCountsDbtxs_Object = MibTableColumn
cucsProcPrtCountsDbtxs = _CucsProcPrtCountsDbtxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 4),
    _CucsProcPrtCountsDbtxs_Type()
)
cucsProcPrtCountsDbtxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtCountsDbtxs.setStatus("current")
_CucsProcPrtCountsTotal_Type = Gauge32
_CucsProcPrtCountsTotal_Object = MibTableColumn
cucsProcPrtCountsTotal = _CucsProcPrtCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 5),
    _CucsProcPrtCountsTotal_Type()
)
cucsProcPrtCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtCountsTotal.setStatus("current")
_CucsProcPrtCountsCachenospc_Type = Gauge32
_CucsProcPrtCountsCachenospc_Object = MibTableColumn
cucsProcPrtCountsCachenospc = _CucsProcPrtCountsCachenospc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 6),
    _CucsProcPrtCountsCachenospc_Type()
)
cucsProcPrtCountsCachenospc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtCountsCachenospc.setStatus("current")
_CucsProcPrtCountsLargetxs_Type = Gauge32
_CucsProcPrtCountsLargetxs_Object = MibTableColumn
cucsProcPrtCountsLargetxs = _CucsProcPrtCountsLargetxs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 7),
    _CucsProcPrtCountsLargetxs_Type()
)
cucsProcPrtCountsLargetxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtCountsLargetxs.setStatus("current")
_CucsProcPrtCountsPersistTime_Type = Unsigned64
_CucsProcPrtCountsPersistTime_Object = MibTableColumn
cucsProcPrtCountsPersistTime = _CucsProcPrtCountsPersistTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 4, 1, 8),
    _CucsProcPrtCountsPersistTime_Type()
)
cucsProcPrtCountsPersistTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcPrtCountsPersistTime.setStatus("current")
_CucsProcStimulusCountsTable_Object = MibTable
cucsProcStimulusCountsTable = _CucsProcStimulusCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5)
)
if mibBuilder.loadTexts:
    cucsProcStimulusCountsTable.setStatus("current")
_CucsProcStimulusCountsEntry_Object = MibTableRow
cucsProcStimulusCountsEntry = _CucsProcStimulusCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1)
)
cucsProcStimulusCountsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcStimulusCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcStimulusCountsEntry.setStatus("current")
_CucsProcStimulusCountsInstanceId_Type = CucsManagedObjectId
_CucsProcStimulusCountsInstanceId_Object = MibTableColumn
cucsProcStimulusCountsInstanceId = _CucsProcStimulusCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 1),
    _CucsProcStimulusCountsInstanceId_Type()
)
cucsProcStimulusCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsInstanceId.setStatus("current")
_CucsProcStimulusCountsDn_Type = CucsManagedObjectDn
_CucsProcStimulusCountsDn_Object = MibTableColumn
cucsProcStimulusCountsDn = _CucsProcStimulusCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 2),
    _CucsProcStimulusCountsDn_Type()
)
cucsProcStimulusCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsDn.setStatus("current")
_CucsProcStimulusCountsRn_Type = SnmpAdminString
_CucsProcStimulusCountsRn_Object = MibTableColumn
cucsProcStimulusCountsRn = _CucsProcStimulusCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 3),
    _CucsProcStimulusCountsRn_Type()
)
cucsProcStimulusCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsRn.setStatus("current")
_CucsProcStimulusCountsBulked_Type = Gauge32
_CucsProcStimulusCountsBulked_Object = MibTableColumn
cucsProcStimulusCountsBulked = _CucsProcStimulusCountsBulked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 4),
    _CucsProcStimulusCountsBulked_Type()
)
cucsProcStimulusCountsBulked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsBulked.setStatus("current")
_CucsProcStimulusCountsFailed_Type = Gauge32
_CucsProcStimulusCountsFailed_Object = MibTableColumn
cucsProcStimulusCountsFailed = _CucsProcStimulusCountsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 5),
    _CucsProcStimulusCountsFailed_Type()
)
cucsProcStimulusCountsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsFailed.setStatus("current")
_CucsProcStimulusCountsRetried_Type = Gauge32
_CucsProcStimulusCountsRetried_Object = MibTableColumn
cucsProcStimulusCountsRetried = _CucsProcStimulusCountsRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 6),
    _CucsProcStimulusCountsRetried_Type()
)
cucsProcStimulusCountsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsRetried.setStatus("current")
_CucsProcStimulusCountsSingleton_Type = Gauge32
_CucsProcStimulusCountsSingleton_Object = MibTableColumn
cucsProcStimulusCountsSingleton = _CucsProcStimulusCountsSingleton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 7),
    _CucsProcStimulusCountsSingleton_Type()
)
cucsProcStimulusCountsSingleton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsSingleton.setStatus("current")
_CucsProcStimulusCountsSuccessfull_Type = Gauge32
_CucsProcStimulusCountsSuccessfull_Object = MibTableColumn
cucsProcStimulusCountsSuccessfull = _CucsProcStimulusCountsSuccessfull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 8),
    _CucsProcStimulusCountsSuccessfull_Type()
)
cucsProcStimulusCountsSuccessfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsSuccessfull.setStatus("current")
_CucsProcStimulusCountsTotal_Type = Gauge32
_CucsProcStimulusCountsTotal_Object = MibTableColumn
cucsProcStimulusCountsTotal = _CucsProcStimulusCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 9),
    _CucsProcStimulusCountsTotal_Type()
)
cucsProcStimulusCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsTotal.setStatus("current")
_CucsProcStimulusCountsAdminState_Type = CucsProcStatAdminState
_CucsProcStimulusCountsAdminState_Object = MibTableColumn
cucsProcStimulusCountsAdminState = _CucsProcStimulusCountsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 5, 1, 10),
    _CucsProcStimulusCountsAdminState_Type()
)
cucsProcStimulusCountsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcStimulusCountsAdminState.setStatus("current")
_CucsProcTxCountsTable_Object = MibTable
cucsProcTxCountsTable = _CucsProcTxCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6)
)
if mibBuilder.loadTexts:
    cucsProcTxCountsTable.setStatus("current")
_CucsProcTxCountsEntry_Object = MibTableRow
cucsProcTxCountsEntry = _CucsProcTxCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1)
)
cucsProcTxCountsEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcTxCountsInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcTxCountsEntry.setStatus("current")
_CucsProcTxCountsInstanceId_Type = CucsManagedObjectId
_CucsProcTxCountsInstanceId_Object = MibTableColumn
cucsProcTxCountsInstanceId = _CucsProcTxCountsInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 1),
    _CucsProcTxCountsInstanceId_Type()
)
cucsProcTxCountsInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcTxCountsInstanceId.setStatus("current")
_CucsProcTxCountsDn_Type = CucsManagedObjectDn
_CucsProcTxCountsDn_Object = MibTableColumn
cucsProcTxCountsDn = _CucsProcTxCountsDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 2),
    _CucsProcTxCountsDn_Type()
)
cucsProcTxCountsDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsDn.setStatus("current")
_CucsProcTxCountsRn_Type = SnmpAdminString
_CucsProcTxCountsRn_Object = MibTableColumn
cucsProcTxCountsRn = _CucsProcTxCountsRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 3),
    _CucsProcTxCountsRn_Type()
)
cucsProcTxCountsRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsRn.setStatus("current")
_CucsProcTxCountsBulked_Type = Gauge32
_CucsProcTxCountsBulked_Object = MibTableColumn
cucsProcTxCountsBulked = _CucsProcTxCountsBulked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 4),
    _CucsProcTxCountsBulked_Type()
)
cucsProcTxCountsBulked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsBulked.setStatus("current")
_CucsProcTxCountsFailed_Type = Gauge32
_CucsProcTxCountsFailed_Object = MibTableColumn
cucsProcTxCountsFailed = _CucsProcTxCountsFailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 5),
    _CucsProcTxCountsFailed_Type()
)
cucsProcTxCountsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsFailed.setStatus("current")
_CucsProcTxCountsRetried_Type = Gauge32
_CucsProcTxCountsRetried_Object = MibTableColumn
cucsProcTxCountsRetried = _CucsProcTxCountsRetried_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 6),
    _CucsProcTxCountsRetried_Type()
)
cucsProcTxCountsRetried.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsRetried.setStatus("current")
_CucsProcTxCountsSingleton_Type = Gauge32
_CucsProcTxCountsSingleton_Object = MibTableColumn
cucsProcTxCountsSingleton = _CucsProcTxCountsSingleton_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 7),
    _CucsProcTxCountsSingleton_Type()
)
cucsProcTxCountsSingleton.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsSingleton.setStatus("current")
_CucsProcTxCountsSuccessfull_Type = Gauge32
_CucsProcTxCountsSuccessfull_Object = MibTableColumn
cucsProcTxCountsSuccessfull = _CucsProcTxCountsSuccessfull_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 8),
    _CucsProcTxCountsSuccessfull_Type()
)
cucsProcTxCountsSuccessfull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsSuccessfull.setStatus("current")
_CucsProcTxCountsTotal_Type = Gauge32
_CucsProcTxCountsTotal_Object = MibTableColumn
cucsProcTxCountsTotal = _CucsProcTxCountsTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 9),
    _CucsProcTxCountsTotal_Type()
)
cucsProcTxCountsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsTotal.setStatus("current")
_CucsProcTxCountsAdminState_Type = CucsProcStatAdminState
_CucsProcTxCountsAdminState_Object = MibTableColumn
cucsProcTxCountsAdminState = _CucsProcTxCountsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 6, 1, 10),
    _CucsProcTxCountsAdminState_Type()
)
cucsProcTxCountsAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcTxCountsAdminState.setStatus("current")
_CucsProcSvcTable_Object = MibTable
cucsProcSvcTable = _CucsProcSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7)
)
if mibBuilder.loadTexts:
    cucsProcSvcTable.setStatus("current")
_CucsProcSvcEntry_Object = MibTableRow
cucsProcSvcEntry = _CucsProcSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1)
)
cucsProcSvcEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-PROC-MIB", "cucsProcSvcInstanceId"),
)
if mibBuilder.loadTexts:
    cucsProcSvcEntry.setStatus("current")
_CucsProcSvcInstanceId_Type = CucsManagedObjectId
_CucsProcSvcInstanceId_Object = MibTableColumn
cucsProcSvcInstanceId = _CucsProcSvcInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 1),
    _CucsProcSvcInstanceId_Type()
)
cucsProcSvcInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsProcSvcInstanceId.setStatus("current")
_CucsProcSvcDn_Type = CucsManagedObjectDn
_CucsProcSvcDn_Object = MibTableColumn
cucsProcSvcDn = _CucsProcSvcDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 2),
    _CucsProcSvcDn_Type()
)
cucsProcSvcDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcSvcDn.setStatus("current")
_CucsProcSvcRn_Type = SnmpAdminString
_CucsProcSvcRn_Object = MibTableColumn
cucsProcSvcRn = _CucsProcSvcRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 3),
    _CucsProcSvcRn_Type()
)
cucsProcSvcRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcSvcRn.setStatus("current")
_CucsProcSvcId_Type = Gauge32
_CucsProcSvcId_Object = MibTableColumn
cucsProcSvcId = _CucsProcSvcId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 4),
    _CucsProcSvcId_Type()
)
cucsProcSvcId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcSvcId.setStatus("current")
_CucsProcSvcName_Type = SnmpAdminString
_CucsProcSvcName_Object = MibTableColumn
cucsProcSvcName = _CucsProcSvcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 40, 7, 1, 5),
    _CucsProcSvcName_Type()
)
cucsProcSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsProcSvcName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-PROC-MIB",
    **{"cucsProcObjects": cucsProcObjects,
       "cucsProcDoerTable": cucsProcDoerTable,
       "cucsProcDoerEntry": cucsProcDoerEntry,
       "cucsProcDoerInstanceId": cucsProcDoerInstanceId,
       "cucsProcDoerDn": cucsProcDoerDn,
       "cucsProcDoerRn": cucsProcDoerRn,
       "cucsProcDoerId": cucsProcDoerId,
       "cucsProcDoerName": cucsProcDoerName,
       "cucsProcManagerTable": cucsProcManagerTable,
       "cucsProcManagerEntry": cucsProcManagerEntry,
       "cucsProcManagerInstanceId": cucsProcManagerInstanceId,
       "cucsProcManagerDn": cucsProcManagerDn,
       "cucsProcManagerRn": cucsProcManagerRn,
       "cucsProcPrtTable": cucsProcPrtTable,
       "cucsProcPrtEntry": cucsProcPrtEntry,
       "cucsProcPrtInstanceId": cucsProcPrtInstanceId,
       "cucsProcPrtDn": cucsProcPrtDn,
       "cucsProcPrtRn": cucsProcPrtRn,
       "cucsProcPrtId": cucsProcPrtId,
       "cucsProcPrtName": cucsProcPrtName,
       "cucsProcPrtCountsTable": cucsProcPrtCountsTable,
       "cucsProcPrtCountsEntry": cucsProcPrtCountsEntry,
       "cucsProcPrtCountsInstanceId": cucsProcPrtCountsInstanceId,
       "cucsProcPrtCountsDn": cucsProcPrtCountsDn,
       "cucsProcPrtCountsRn": cucsProcPrtCountsRn,
       "cucsProcPrtCountsDbtxs": cucsProcPrtCountsDbtxs,
       "cucsProcPrtCountsTotal": cucsProcPrtCountsTotal,
       "cucsProcPrtCountsCachenospc": cucsProcPrtCountsCachenospc,
       "cucsProcPrtCountsLargetxs": cucsProcPrtCountsLargetxs,
       "cucsProcPrtCountsPersistTime": cucsProcPrtCountsPersistTime,
       "cucsProcStimulusCountsTable": cucsProcStimulusCountsTable,
       "cucsProcStimulusCountsEntry": cucsProcStimulusCountsEntry,
       "cucsProcStimulusCountsInstanceId": cucsProcStimulusCountsInstanceId,
       "cucsProcStimulusCountsDn": cucsProcStimulusCountsDn,
       "cucsProcStimulusCountsRn": cucsProcStimulusCountsRn,
       "cucsProcStimulusCountsBulked": cucsProcStimulusCountsBulked,
       "cucsProcStimulusCountsFailed": cucsProcStimulusCountsFailed,
       "cucsProcStimulusCountsRetried": cucsProcStimulusCountsRetried,
       "cucsProcStimulusCountsSingleton": cucsProcStimulusCountsSingleton,
       "cucsProcStimulusCountsSuccessfull": cucsProcStimulusCountsSuccessfull,
       "cucsProcStimulusCountsTotal": cucsProcStimulusCountsTotal,
       "cucsProcStimulusCountsAdminState": cucsProcStimulusCountsAdminState,
       "cucsProcTxCountsTable": cucsProcTxCountsTable,
       "cucsProcTxCountsEntry": cucsProcTxCountsEntry,
       "cucsProcTxCountsInstanceId": cucsProcTxCountsInstanceId,
       "cucsProcTxCountsDn": cucsProcTxCountsDn,
       "cucsProcTxCountsRn": cucsProcTxCountsRn,
       "cucsProcTxCountsBulked": cucsProcTxCountsBulked,
       "cucsProcTxCountsFailed": cucsProcTxCountsFailed,
       "cucsProcTxCountsRetried": cucsProcTxCountsRetried,
       "cucsProcTxCountsSingleton": cucsProcTxCountsSingleton,
       "cucsProcTxCountsSuccessfull": cucsProcTxCountsSuccessfull,
       "cucsProcTxCountsTotal": cucsProcTxCountsTotal,
       "cucsProcTxCountsAdminState": cucsProcTxCountsAdminState,
       "cucsProcSvcTable": cucsProcSvcTable,
       "cucsProcSvcEntry": cucsProcSvcEntry,
       "cucsProcSvcInstanceId": cucsProcSvcInstanceId,
       "cucsProcSvcDn": cucsProcSvcDn,
       "cucsProcSvcRn": cucsProcSvcRn,
       "cucsProcSvcId": cucsProcSvcId,
       "cucsProcSvcName": cucsProcSvcName}
)
