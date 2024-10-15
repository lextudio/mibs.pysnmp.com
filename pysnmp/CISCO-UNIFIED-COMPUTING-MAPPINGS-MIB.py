# SNMP MIB module (CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:56 2024
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
 ciscoUnifiedComputingMIB) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIB")

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

cucsMappingsObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsMappingsMoContainmentTable_Object = MibTable
cucsMappingsMoContainmentTable = _CucsMappingsMoContainmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 1)
)
if mibBuilder.loadTexts:
    cucsMappingsMoContainmentTable.setStatus("current")
_CucsMappingsMoContainmentEntry_Object = MibTableRow
cucsMappingsMoContainmentEntry = _CucsMappingsMoContainmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 1, 1)
)
cucsMappingsMoContainmentEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB", "cucsMappingsMoContainmentParentInstanceId"),
    (0, "CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB", "cucsMappingsMoContainmentChildInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMappingsMoContainmentEntry.setStatus("current")
_CucsMappingsMoContainmentParentInstanceId_Type = CucsManagedObjectId
_CucsMappingsMoContainmentParentInstanceId_Object = MibTableColumn
cucsMappingsMoContainmentParentInstanceId = _CucsMappingsMoContainmentParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 1, 1, 1),
    _CucsMappingsMoContainmentParentInstanceId_Type()
)
cucsMappingsMoContainmentParentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMappingsMoContainmentParentInstanceId.setStatus("current")
_CucsMappingsMoContainmentChildInstanceId_Type = CucsManagedObjectId
_CucsMappingsMoContainmentChildInstanceId_Object = MibTableColumn
cucsMappingsMoContainmentChildInstanceId = _CucsMappingsMoContainmentChildInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 1, 1, 2),
    _CucsMappingsMoContainmentChildInstanceId_Type()
)
cucsMappingsMoContainmentChildInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMappingsMoContainmentChildInstanceId.setStatus("current")
_CucsMappingsMoContainmentParentDn_Type = CucsManagedObjectDn
_CucsMappingsMoContainmentParentDn_Object = MibTableColumn
cucsMappingsMoContainmentParentDn = _CucsMappingsMoContainmentParentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 1, 1, 3),
    _CucsMappingsMoContainmentParentDn_Type()
)
cucsMappingsMoContainmentParentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMappingsMoContainmentParentDn.setStatus("current")
_CucsMappingsMoContainmentChildDn_Type = CucsManagedObjectDn
_CucsMappingsMoContainmentChildDn_Object = MibTableColumn
cucsMappingsMoContainmentChildDn = _CucsMappingsMoContainmentChildDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 1, 1, 4),
    _CucsMappingsMoContainmentChildDn_Type()
)
cucsMappingsMoContainmentChildDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMappingsMoContainmentChildDn.setStatus("current")
_CucsMappingsMoInverseContainmentTable_Object = MibTable
cucsMappingsMoInverseContainmentTable = _CucsMappingsMoInverseContainmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 2)
)
if mibBuilder.loadTexts:
    cucsMappingsMoInverseContainmentTable.setStatus("current")
_CucsMappingsMoInverseContainmentEntry_Object = MibTableRow
cucsMappingsMoInverseContainmentEntry = _CucsMappingsMoInverseContainmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 2, 1)
)
cucsMappingsMoInverseContainmentEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB", "cucsMappingsMoInverseContainmentChildInstanceId"),
    (0, "CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB", "cucsMappingsMoInverseContainmentParentInstanceId"),
)
if mibBuilder.loadTexts:
    cucsMappingsMoInverseContainmentEntry.setStatus("current")
_CucsMappingsMoInverseContainmentChildInstanceId_Type = CucsManagedObjectId
_CucsMappingsMoInverseContainmentChildInstanceId_Object = MibTableColumn
cucsMappingsMoInverseContainmentChildInstanceId = _CucsMappingsMoInverseContainmentChildInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 2, 1, 1),
    _CucsMappingsMoInverseContainmentChildInstanceId_Type()
)
cucsMappingsMoInverseContainmentChildInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMappingsMoInverseContainmentChildInstanceId.setStatus("current")
_CucsMappingsMoInverseContainmentParentInstanceId_Type = CucsManagedObjectId
_CucsMappingsMoInverseContainmentParentInstanceId_Object = MibTableColumn
cucsMappingsMoInverseContainmentParentInstanceId = _CucsMappingsMoInverseContainmentParentInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 2, 1, 2),
    _CucsMappingsMoInverseContainmentParentInstanceId_Type()
)
cucsMappingsMoInverseContainmentParentInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMappingsMoInverseContainmentParentInstanceId.setStatus("current")
_CucsMappingsMoInverseContainmentParentDn_Type = CucsManagedObjectDn
_CucsMappingsMoInverseContainmentParentDn_Object = MibTableColumn
cucsMappingsMoInverseContainmentParentDn = _CucsMappingsMoInverseContainmentParentDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 2, 1, 3),
    _CucsMappingsMoInverseContainmentParentDn_Type()
)
cucsMappingsMoInverseContainmentParentDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMappingsMoInverseContainmentParentDn.setStatus("current")
_CucsMappingsMoInverseContainmentChildDn_Type = CucsManagedObjectDn
_CucsMappingsMoInverseContainmentChildDn_Object = MibTableColumn
cucsMappingsMoInverseContainmentChildDn = _CucsMappingsMoInverseContainmentChildDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 2, 1, 4),
    _CucsMappingsMoInverseContainmentChildDn_Type()
)
cucsMappingsMoInverseContainmentChildDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMappingsMoInverseContainmentChildDn.setStatus("current")
_CucsMappingsDnToOidTable_Object = MibTable
cucsMappingsDnToOidTable = _CucsMappingsDnToOidTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 3)
)
if mibBuilder.loadTexts:
    cucsMappingsDnToOidTable.setStatus("current")
_CucsMappingsDnToOidEntry_Object = MibTableRow
cucsMappingsDnToOidEntry = _CucsMappingsDnToOidEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 3, 1)
)
cucsMappingsDnToOidEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB", "cucsMappingsDnToOidDn"),
)
if mibBuilder.loadTexts:
    cucsMappingsDnToOidEntry.setStatus("current")
_CucsMappingsDnToOidDn_Type = CucsManagedObjectDn
_CucsMappingsDnToOidDn_Object = MibTableColumn
cucsMappingsDnToOidDn = _CucsMappingsDnToOidDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 3, 1, 1),
    _CucsMappingsDnToOidDn_Type()
)
cucsMappingsDnToOidDn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsMappingsDnToOidDn.setStatus("current")
_CucsMappingsDnToOidOid_Type = RowPointer
_CucsMappingsDnToOidOid_Object = MibTableColumn
cucsMappingsDnToOidOid = _CucsMappingsDnToOidOid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 3, 3, 1, 2),
    _CucsMappingsDnToOidOid_Type()
)
cucsMappingsDnToOidOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsMappingsDnToOidOid.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-MAPPINGS-MIB",
    **{"cucsMappingsObjects": cucsMappingsObjects,
       "cucsMappingsMoContainmentTable": cucsMappingsMoContainmentTable,
       "cucsMappingsMoContainmentEntry": cucsMappingsMoContainmentEntry,
       "cucsMappingsMoContainmentParentInstanceId": cucsMappingsMoContainmentParentInstanceId,
       "cucsMappingsMoContainmentChildInstanceId": cucsMappingsMoContainmentChildInstanceId,
       "cucsMappingsMoContainmentParentDn": cucsMappingsMoContainmentParentDn,
       "cucsMappingsMoContainmentChildDn": cucsMappingsMoContainmentChildDn,
       "cucsMappingsMoInverseContainmentTable": cucsMappingsMoInverseContainmentTable,
       "cucsMappingsMoInverseContainmentEntry": cucsMappingsMoInverseContainmentEntry,
       "cucsMappingsMoInverseContainmentChildInstanceId": cucsMappingsMoInverseContainmentChildInstanceId,
       "cucsMappingsMoInverseContainmentParentInstanceId": cucsMappingsMoInverseContainmentParentInstanceId,
       "cucsMappingsMoInverseContainmentParentDn": cucsMappingsMoInverseContainmentParentDn,
       "cucsMappingsMoInverseContainmentChildDn": cucsMappingsMoInverseContainmentChildDn,
       "cucsMappingsDnToOidTable": cucsMappingsDnToOidTable,
       "cucsMappingsDnToOidEntry": cucsMappingsDnToOidEntry,
       "cucsMappingsDnToOidDn": cucsMappingsDnToOidDn,
       "cucsMappingsDnToOidOid": cucsMappingsDnToOidOid}
)
