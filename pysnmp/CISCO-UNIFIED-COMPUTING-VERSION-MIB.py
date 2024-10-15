# SNMP MIB module (CISCO-UNIFIED-COMPUTING-VERSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-VERSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:29 2024
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

cucsVersionObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsVersionApplicationTable_Object = MibTable
cucsVersionApplicationTable = _CucsVersionApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1)
)
if mibBuilder.loadTexts:
    cucsVersionApplicationTable.setStatus("current")
_CucsVersionApplicationEntry_Object = MibTableRow
cucsVersionApplicationEntry = _CucsVersionApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1)
)
cucsVersionApplicationEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VERSION-MIB", "cucsVersionApplicationInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVersionApplicationEntry.setStatus("current")
_CucsVersionApplicationInstanceId_Type = CucsManagedObjectId
_CucsVersionApplicationInstanceId_Object = MibTableColumn
cucsVersionApplicationInstanceId = _CucsVersionApplicationInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 1),
    _CucsVersionApplicationInstanceId_Type()
)
cucsVersionApplicationInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVersionApplicationInstanceId.setStatus("current")
_CucsVersionApplicationDn_Type = CucsManagedObjectDn
_CucsVersionApplicationDn_Object = MibTableColumn
cucsVersionApplicationDn = _CucsVersionApplicationDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 2),
    _CucsVersionApplicationDn_Type()
)
cucsVersionApplicationDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVersionApplicationDn.setStatus("current")
_CucsVersionApplicationRn_Type = SnmpAdminString
_CucsVersionApplicationRn_Object = MibTableColumn
cucsVersionApplicationRn = _CucsVersionApplicationRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 3),
    _CucsVersionApplicationRn_Type()
)
cucsVersionApplicationRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVersionApplicationRn.setStatus("current")
_CucsVersionApplicationDetail_Type = SnmpAdminString
_CucsVersionApplicationDetail_Object = MibTableColumn
cucsVersionApplicationDetail = _CucsVersionApplicationDetail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 4),
    _CucsVersionApplicationDetail_Type()
)
cucsVersionApplicationDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVersionApplicationDetail.setStatus("current")
_CucsVersionApplicationTime_Type = SnmpAdminString
_CucsVersionApplicationTime_Object = MibTableColumn
cucsVersionApplicationTime = _CucsVersionApplicationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 5),
    _CucsVersionApplicationTime_Type()
)
cucsVersionApplicationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVersionApplicationTime.setStatus("current")
_CucsVersionApplicationVersion_Type = SnmpAdminString
_CucsVersionApplicationVersion_Object = MibTableColumn
cucsVersionApplicationVersion = _CucsVersionApplicationVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 1, 1, 6),
    _CucsVersionApplicationVersion_Type()
)
cucsVersionApplicationVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVersionApplicationVersion.setStatus("current")
_CucsVersionEpTable_Object = MibTable
cucsVersionEpTable = _CucsVersionEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2)
)
if mibBuilder.loadTexts:
    cucsVersionEpTable.setStatus("current")
_CucsVersionEpEntry_Object = MibTableRow
cucsVersionEpEntry = _CucsVersionEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1)
)
cucsVersionEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-VERSION-MIB", "cucsVersionEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsVersionEpEntry.setStatus("current")
_CucsVersionEpInstanceId_Type = CucsManagedObjectId
_CucsVersionEpInstanceId_Object = MibTableColumn
cucsVersionEpInstanceId = _CucsVersionEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 1),
    _CucsVersionEpInstanceId_Type()
)
cucsVersionEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsVersionEpInstanceId.setStatus("current")
_CucsVersionEpDn_Type = CucsManagedObjectDn
_CucsVersionEpDn_Object = MibTableColumn
cucsVersionEpDn = _CucsVersionEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 2),
    _CucsVersionEpDn_Type()
)
cucsVersionEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVersionEpDn.setStatus("current")
_CucsVersionEpRn_Type = SnmpAdminString
_CucsVersionEpRn_Object = MibTableColumn
cucsVersionEpRn = _CucsVersionEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 70, 2, 1, 3),
    _CucsVersionEpRn_Type()
)
cucsVersionEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsVersionEpRn.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-VERSION-MIB",
    **{"cucsVersionObjects": cucsVersionObjects,
       "cucsVersionApplicationTable": cucsVersionApplicationTable,
       "cucsVersionApplicationEntry": cucsVersionApplicationEntry,
       "cucsVersionApplicationInstanceId": cucsVersionApplicationInstanceId,
       "cucsVersionApplicationDn": cucsVersionApplicationDn,
       "cucsVersionApplicationRn": cucsVersionApplicationRn,
       "cucsVersionApplicationDetail": cucsVersionApplicationDetail,
       "cucsVersionApplicationTime": cucsVersionApplicationTime,
       "cucsVersionApplicationVersion": cucsVersionApplicationVersion,
       "cucsVersionEpTable": cucsVersionEpTable,
       "cucsVersionEpEntry": cucsVersionEpEntry,
       "cucsVersionEpInstanceId": cucsVersionEpInstanceId,
       "cucsVersionEpDn": cucsVersionEpDn,
       "cucsVersionEpRn": cucsVersionEpRn}
)
