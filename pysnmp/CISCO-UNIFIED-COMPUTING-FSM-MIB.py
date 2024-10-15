# SNMP MIB module (CISCO-UNIFIED-COMPUTING-FSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-FSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:36 2024
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

(CucsFsmFsmStageStatus,) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsFsmFsmStageStatus")

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

cucsFsmObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFsmStatusTable_Object = MibTable
cucsFsmStatusTable = _CucsFsmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1)
)
if mibBuilder.loadTexts:
    cucsFsmStatusTable.setStatus("current")
_CucsFsmStatusEntry_Object = MibTableRow
cucsFsmStatusEntry = _CucsFsmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1)
)
cucsFsmStatusEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FSM-MIB", "cucsFsmStatusInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFsmStatusEntry.setStatus("current")
_CucsFsmStatusInstanceId_Type = CucsManagedObjectId
_CucsFsmStatusInstanceId_Object = MibTableColumn
cucsFsmStatusInstanceId = _CucsFsmStatusInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 1),
    _CucsFsmStatusInstanceId_Type()
)
cucsFsmStatusInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFsmStatusInstanceId.setStatus("current")
_CucsFsmStatusDn_Type = CucsManagedObjectDn
_CucsFsmStatusDn_Object = MibTableColumn
cucsFsmStatusDn = _CucsFsmStatusDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 2),
    _CucsFsmStatusDn_Type()
)
cucsFsmStatusDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusDn.setStatus("current")
_CucsFsmStatusRn_Type = SnmpAdminString
_CucsFsmStatusRn_Object = MibTableColumn
cucsFsmStatusRn = _CucsFsmStatusRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 3),
    _CucsFsmStatusRn_Type()
)
cucsFsmStatusRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusRn.setStatus("current")
_CucsFsmStatusConvertedEpRef_Type = SnmpAdminString
_CucsFsmStatusConvertedEpRef_Object = MibTableColumn
cucsFsmStatusConvertedEpRef = _CucsFsmStatusConvertedEpRef_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 4),
    _CucsFsmStatusConvertedEpRef_Type()
)
cucsFsmStatusConvertedEpRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusConvertedEpRef.setStatus("current")
_CucsFsmStatusDescr_Type = SnmpAdminString
_CucsFsmStatusDescr_Object = MibTableColumn
cucsFsmStatusDescr = _CucsFsmStatusDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 5),
    _CucsFsmStatusDescr_Type()
)
cucsFsmStatusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusDescr.setStatus("current")
_CucsFsmStatusName_Type = SnmpAdminString
_CucsFsmStatusName_Object = MibTableColumn
cucsFsmStatusName = _CucsFsmStatusName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 6),
    _CucsFsmStatusName_Type()
)
cucsFsmStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusName.setStatus("current")
_CucsFsmStatusObjectClassName_Type = SnmpAdminString
_CucsFsmStatusObjectClassName_Object = MibTableColumn
cucsFsmStatusObjectClassName = _CucsFsmStatusObjectClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 7),
    _CucsFsmStatusObjectClassName_Type()
)
cucsFsmStatusObjectClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusObjectClassName.setStatus("current")
_CucsFsmStatusRemoteEpRef_Type = SnmpAdminString
_CucsFsmStatusRemoteEpRef_Object = MibTableColumn
cucsFsmStatusRemoteEpRef = _CucsFsmStatusRemoteEpRef_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 8),
    _CucsFsmStatusRemoteEpRef_Type()
)
cucsFsmStatusRemoteEpRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusRemoteEpRef.setStatus("current")
_CucsFsmStatusState_Type = CucsFsmFsmStageStatus
_CucsFsmStatusState_Object = MibTableColumn
cucsFsmStatusState = _CucsFsmStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 63, 1, 1, 9),
    _CucsFsmStatusState_Type()
)
cucsFsmStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFsmStatusState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-FSM-MIB",
    **{"cucsFsmObjects": cucsFsmObjects,
       "cucsFsmStatusTable": cucsFsmStatusTable,
       "cucsFsmStatusEntry": cucsFsmStatusEntry,
       "cucsFsmStatusInstanceId": cucsFsmStatusInstanceId,
       "cucsFsmStatusDn": cucsFsmStatusDn,
       "cucsFsmStatusRn": cucsFsmStatusRn,
       "cucsFsmStatusConvertedEpRef": cucsFsmStatusConvertedEpRef,
       "cucsFsmStatusDescr": cucsFsmStatusDescr,
       "cucsFsmStatusName": cucsFsmStatusName,
       "cucsFsmStatusObjectClassName": cucsFsmStatusObjectClassName,
       "cucsFsmStatusRemoteEpRef": cucsFsmStatusRemoteEpRef,
       "cucsFsmStatusState": cucsFsmStatusState}
)
