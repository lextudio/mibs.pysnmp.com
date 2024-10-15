# SNMP MIB module (CISCO-UNIFIED-COMPUTING-SES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-SES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:18 2024
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

(CucsFsmLifecycle,) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsFsmLifecycle")

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

cucsSesObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsSesDiskSlotEpTable_Object = MibTable
cucsSesDiskSlotEpTable = _CucsSesDiskSlotEpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1)
)
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpTable.setStatus("current")
_CucsSesDiskSlotEpEntry_Object = MibTableRow
cucsSesDiskSlotEpEntry = _CucsSesDiskSlotEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1, 1)
)
cucsSesDiskSlotEpEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SES-MIB", "cucsSesDiskSlotEpInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpEntry.setStatus("current")
_CucsSesDiskSlotEpInstanceId_Type = CucsManagedObjectId
_CucsSesDiskSlotEpInstanceId_Object = MibTableColumn
cucsSesDiskSlotEpInstanceId = _CucsSesDiskSlotEpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1, 1, 1),
    _CucsSesDiskSlotEpInstanceId_Type()
)
cucsSesDiskSlotEpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpInstanceId.setStatus("current")
_CucsSesDiskSlotEpDn_Type = CucsManagedObjectDn
_CucsSesDiskSlotEpDn_Object = MibTableColumn
cucsSesDiskSlotEpDn = _CucsSesDiskSlotEpDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1, 1, 2),
    _CucsSesDiskSlotEpDn_Type()
)
cucsSesDiskSlotEpDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpDn.setStatus("current")
_CucsSesDiskSlotEpRn_Type = SnmpAdminString
_CucsSesDiskSlotEpRn_Object = MibTableColumn
cucsSesDiskSlotEpRn = _CucsSesDiskSlotEpRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1, 1, 3),
    _CucsSesDiskSlotEpRn_Type()
)
cucsSesDiskSlotEpRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpRn.setStatus("current")
_CucsSesDiskSlotEpEncId_Type = Gauge32
_CucsSesDiskSlotEpEncId_Object = MibTableColumn
cucsSesDiskSlotEpEncId = _CucsSesDiskSlotEpEncId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1, 1, 4),
    _CucsSesDiskSlotEpEncId_Type()
)
cucsSesDiskSlotEpEncId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpEncId.setStatus("current")
_CucsSesDiskSlotEpId_Type = Gauge32
_CucsSesDiskSlotEpId_Object = MibTableColumn
cucsSesDiskSlotEpId = _CucsSesDiskSlotEpId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1, 1, 5),
    _CucsSesDiskSlotEpId_Type()
)
cucsSesDiskSlotEpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpId.setStatus("current")
_CucsSesDiskSlotEpSlotDn_Type = SnmpAdminString
_CucsSesDiskSlotEpSlotDn_Object = MibTableColumn
cucsSesDiskSlotEpSlotDn = _CucsSesDiskSlotEpSlotDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 1, 1, 6),
    _CucsSesDiskSlotEpSlotDn_Type()
)
cucsSesDiskSlotEpSlotDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesDiskSlotEpSlotDn.setStatus("current")
_CucsSesEnclosureTable_Object = MibTable
cucsSesEnclosureTable = _CucsSesEnclosureTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2)
)
if mibBuilder.loadTexts:
    cucsSesEnclosureTable.setStatus("current")
_CucsSesEnclosureEntry_Object = MibTableRow
cucsSesEnclosureEntry = _CucsSesEnclosureEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1)
)
cucsSesEnclosureEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SES-MIB", "cucsSesEnclosureInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSesEnclosureEntry.setStatus("current")
_CucsSesEnclosureInstanceId_Type = CucsManagedObjectId
_CucsSesEnclosureInstanceId_Object = MibTableColumn
cucsSesEnclosureInstanceId = _CucsSesEnclosureInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1, 1),
    _CucsSesEnclosureInstanceId_Type()
)
cucsSesEnclosureInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSesEnclosureInstanceId.setStatus("current")
_CucsSesEnclosureDn_Type = CucsManagedObjectDn
_CucsSesEnclosureDn_Object = MibTableColumn
cucsSesEnclosureDn = _CucsSesEnclosureDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1, 2),
    _CucsSesEnclosureDn_Type()
)
cucsSesEnclosureDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesEnclosureDn.setStatus("current")
_CucsSesEnclosureRn_Type = SnmpAdminString
_CucsSesEnclosureRn_Object = MibTableColumn
cucsSesEnclosureRn = _CucsSesEnclosureRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1, 3),
    _CucsSesEnclosureRn_Type()
)
cucsSesEnclosureRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesEnclosureRn.setStatus("current")
_CucsSesEnclosureDescr_Type = SnmpAdminString
_CucsSesEnclosureDescr_Object = MibTableColumn
cucsSesEnclosureDescr = _CucsSesEnclosureDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1, 4),
    _CucsSesEnclosureDescr_Type()
)
cucsSesEnclosureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesEnclosureDescr.setStatus("current")
_CucsSesEnclosureElid_Type = SnmpAdminString
_CucsSesEnclosureElid_Object = MibTableColumn
cucsSesEnclosureElid = _CucsSesEnclosureElid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1, 5),
    _CucsSesEnclosureElid_Type()
)
cucsSesEnclosureElid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesEnclosureElid.setStatus("current")
_CucsSesEnclosureId_Type = Gauge32
_CucsSesEnclosureId_Object = MibTableColumn
cucsSesEnclosureId = _CucsSesEnclosureId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1, 6),
    _CucsSesEnclosureId_Type()
)
cucsSesEnclosureId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesEnclosureId.setStatus("current")
_CucsSesEnclosureLc_Type = CucsFsmLifecycle
_CucsSesEnclosureLc_Object = MibTableColumn
cucsSesEnclosureLc = _CucsSesEnclosureLc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 80, 2, 1, 7),
    _CucsSesEnclosureLc_Type()
)
cucsSesEnclosureLc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSesEnclosureLc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-SES-MIB",
    **{"cucsSesObjects": cucsSesObjects,
       "cucsSesDiskSlotEpTable": cucsSesDiskSlotEpTable,
       "cucsSesDiskSlotEpEntry": cucsSesDiskSlotEpEntry,
       "cucsSesDiskSlotEpInstanceId": cucsSesDiskSlotEpInstanceId,
       "cucsSesDiskSlotEpDn": cucsSesDiskSlotEpDn,
       "cucsSesDiskSlotEpRn": cucsSesDiskSlotEpRn,
       "cucsSesDiskSlotEpEncId": cucsSesDiskSlotEpEncId,
       "cucsSesDiskSlotEpId": cucsSesDiskSlotEpId,
       "cucsSesDiskSlotEpSlotDn": cucsSesDiskSlotEpSlotDn,
       "cucsSesEnclosureTable": cucsSesEnclosureTable,
       "cucsSesEnclosureEntry": cucsSesEnclosureEntry,
       "cucsSesEnclosureInstanceId": cucsSesEnclosureInstanceId,
       "cucsSesEnclosureDn": cucsSesEnclosureDn,
       "cucsSesEnclosureRn": cucsSesEnclosureRn,
       "cucsSesEnclosureDescr": cucsSesEnclosureDescr,
       "cucsSesEnclosureElid": cucsSesEnclosureElid,
       "cucsSesEnclosureId": cucsSesEnclosureId,
       "cucsSesEnclosureLc": cucsSesEnclosureLc}
)
