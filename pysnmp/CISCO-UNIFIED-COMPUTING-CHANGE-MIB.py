# SNMP MIB module (CISCO-UNIFIED-COMPUTING-CHANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-CHANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:07 2024
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

(CucsChangeStatus,
 CucsMoMoClassId) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsChangeStatus",
    "CucsMoMoClassId")

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

cucsChangeObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsChangeChangedObjectRefTable_Object = MibTable
cucsChangeChangedObjectRefTable = _CucsChangeChangedObjectRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1)
)
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefTable.setStatus("current")
_CucsChangeChangedObjectRefEntry_Object = MibTableRow
cucsChangeChangedObjectRefEntry = _CucsChangeChangedObjectRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1)
)
cucsChangeChangedObjectRefEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-CHANGE-MIB", "cucsChangeChangedObjectRefInstanceId"),
)
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefEntry.setStatus("current")
_CucsChangeChangedObjectRefInstanceId_Type = CucsManagedObjectId
_CucsChangeChangedObjectRefInstanceId_Object = MibTableColumn
cucsChangeChangedObjectRefInstanceId = _CucsChangeChangedObjectRefInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 1),
    _CucsChangeChangedObjectRefInstanceId_Type()
)
cucsChangeChangedObjectRefInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefInstanceId.setStatus("current")
_CucsChangeChangedObjectRefDn_Type = CucsManagedObjectDn
_CucsChangeChangedObjectRefDn_Object = MibTableColumn
cucsChangeChangedObjectRefDn = _CucsChangeChangedObjectRefDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 2),
    _CucsChangeChangedObjectRefDn_Type()
)
cucsChangeChangedObjectRefDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefDn.setStatus("current")
_CucsChangeChangedObjectRefRn_Type = SnmpAdminString
_CucsChangeChangedObjectRefRn_Object = MibTableColumn
cucsChangeChangedObjectRefRn = _CucsChangeChangedObjectRefRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 3),
    _CucsChangeChangedObjectRefRn_Type()
)
cucsChangeChangedObjectRefRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefRn.setStatus("current")
_CucsChangeChangedObjectRefCentraleMoDn_Type = SnmpAdminString
_CucsChangeChangedObjectRefCentraleMoDn_Object = MibTableColumn
cucsChangeChangedObjectRefCentraleMoDn = _CucsChangeChangedObjectRefCentraleMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 4),
    _CucsChangeChangedObjectRefCentraleMoDn_Type()
)
cucsChangeChangedObjectRefCentraleMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefCentraleMoDn.setStatus("current")
_CucsChangeChangedObjectRefChangedMoClassId_Type = CucsMoMoClassId
_CucsChangeChangedObjectRefChangedMoClassId_Object = MibTableColumn
cucsChangeChangedObjectRefChangedMoClassId = _CucsChangeChangedObjectRefChangedMoClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 5),
    _CucsChangeChangedObjectRefChangedMoClassId_Type()
)
cucsChangeChangedObjectRefChangedMoClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefChangedMoClassId.setStatus("current")
_CucsChangeChangedObjectRefId_Type = Gauge32
_CucsChangeChangedObjectRefId_Object = MibTableColumn
cucsChangeChangedObjectRefId = _CucsChangeChangedObjectRefId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 6),
    _CucsChangeChangedObjectRefId_Type()
)
cucsChangeChangedObjectRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefId.setStatus("current")
_CucsChangeChangedObjectRefOldCentraleMoDn_Type = SnmpAdminString
_CucsChangeChangedObjectRefOldCentraleMoDn_Object = MibTableColumn
cucsChangeChangedObjectRefOldCentraleMoDn = _CucsChangeChangedObjectRefOldCentraleMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 7),
    _CucsChangeChangedObjectRefOldCentraleMoDn_Type()
)
cucsChangeChangedObjectRefOldCentraleMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefOldCentraleMoDn.setStatus("current")
_CucsChangeChangedObjectRefRefObjStatus_Type = CucsChangeStatus
_CucsChangeChangedObjectRefRefObjStatus_Object = MibTableColumn
cucsChangeChangedObjectRefRefObjStatus = _CucsChangeChangedObjectRefRefObjStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 8),
    _CucsChangeChangedObjectRefRefObjStatus_Type()
)
cucsChangeChangedObjectRefRefObjStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefRefObjStatus.setStatus("current")
_CucsChangeChangedObjectRefUcsmMoDn_Type = SnmpAdminString
_CucsChangeChangedObjectRefUcsmMoDn_Object = MibTableColumn
cucsChangeChangedObjectRefUcsmMoDn = _CucsChangeChangedObjectRefUcsmMoDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 9),
    _CucsChangeChangedObjectRefUcsmMoDn_Type()
)
cucsChangeChangedObjectRefUcsmMoDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefUcsmMoDn.setStatus("current")
_CucsChangeChangedObjectRefGuid_Type = SnmpAdminString
_CucsChangeChangedObjectRefGuid_Object = MibTableColumn
cucsChangeChangedObjectRefGuid = _CucsChangeChangedObjectRefGuid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 71, 1, 1, 10),
    _CucsChangeChangedObjectRefGuid_Type()
)
cucsChangeChangedObjectRefGuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsChangeChangedObjectRefGuid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-CHANGE-MIB",
    **{"cucsChangeObjects": cucsChangeObjects,
       "cucsChangeChangedObjectRefTable": cucsChangeChangedObjectRefTable,
       "cucsChangeChangedObjectRefEntry": cucsChangeChangedObjectRefEntry,
       "cucsChangeChangedObjectRefInstanceId": cucsChangeChangedObjectRefInstanceId,
       "cucsChangeChangedObjectRefDn": cucsChangeChangedObjectRefDn,
       "cucsChangeChangedObjectRefRn": cucsChangeChangedObjectRefRn,
       "cucsChangeChangedObjectRefCentraleMoDn": cucsChangeChangedObjectRefCentraleMoDn,
       "cucsChangeChangedObjectRefChangedMoClassId": cucsChangeChangedObjectRefChangedMoClassId,
       "cucsChangeChangedObjectRefId": cucsChangeChangedObjectRefId,
       "cucsChangeChangedObjectRefOldCentraleMoDn": cucsChangeChangedObjectRefOldCentraleMoDn,
       "cucsChangeChangedObjectRefRefObjStatus": cucsChangeChangedObjectRefRefObjStatus,
       "cucsChangeChangedObjectRefUcsmMoDn": cucsChangeChangedObjectRefUcsmMoDn,
       "cucsChangeChangedObjectRefGuid": cucsChangeChangedObjectRefGuid}
)
