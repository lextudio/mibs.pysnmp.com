# SNMP MIB module (CISCO-UNIFIED-COMPUTING-SOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-SOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:19 2024
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

(CucsPolicyPolicyOwner,
 CucsSolAdminState,
 CucsSolSpeed) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsPolicyPolicyOwner",
    "CucsSolAdminState",
    "CucsSolSpeed")

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

cucsSolObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsSolConfigTable_Object = MibTable
cucsSolConfigTable = _CucsSolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1)
)
if mibBuilder.loadTexts:
    cucsSolConfigTable.setStatus("current")
_CucsSolConfigEntry_Object = MibTableRow
cucsSolConfigEntry = _CucsSolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1)
)
cucsSolConfigEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SOL-MIB", "cucsSolConfigInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSolConfigEntry.setStatus("current")
_CucsSolConfigInstanceId_Type = CucsManagedObjectId
_CucsSolConfigInstanceId_Object = MibTableColumn
cucsSolConfigInstanceId = _CucsSolConfigInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 1),
    _CucsSolConfigInstanceId_Type()
)
cucsSolConfigInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSolConfigInstanceId.setStatus("current")
_CucsSolConfigDn_Type = CucsManagedObjectDn
_CucsSolConfigDn_Object = MibTableColumn
cucsSolConfigDn = _CucsSolConfigDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 2),
    _CucsSolConfigDn_Type()
)
cucsSolConfigDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigDn.setStatus("current")
_CucsSolConfigRn_Type = SnmpAdminString
_CucsSolConfigRn_Object = MibTableColumn
cucsSolConfigRn = _CucsSolConfigRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 3),
    _CucsSolConfigRn_Type()
)
cucsSolConfigRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigRn.setStatus("current")
_CucsSolConfigAdminState_Type = CucsSolAdminState
_CucsSolConfigAdminState_Object = MibTableColumn
cucsSolConfigAdminState = _CucsSolConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 4),
    _CucsSolConfigAdminState_Type()
)
cucsSolConfigAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigAdminState.setStatus("current")
_CucsSolConfigDescr_Type = SnmpAdminString
_CucsSolConfigDescr_Object = MibTableColumn
cucsSolConfigDescr = _CucsSolConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 5),
    _CucsSolConfigDescr_Type()
)
cucsSolConfigDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigDescr.setStatus("current")
_CucsSolConfigIntId_Type = SnmpAdminString
_CucsSolConfigIntId_Object = MibTableColumn
cucsSolConfigIntId = _CucsSolConfigIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 6),
    _CucsSolConfigIntId_Type()
)
cucsSolConfigIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigIntId.setStatus("current")
_CucsSolConfigName_Type = SnmpAdminString
_CucsSolConfigName_Object = MibTableColumn
cucsSolConfigName = _CucsSolConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 7),
    _CucsSolConfigName_Type()
)
cucsSolConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigName.setStatus("current")
_CucsSolConfigSpeed_Type = CucsSolSpeed
_CucsSolConfigSpeed_Object = MibTableColumn
cucsSolConfigSpeed = _CucsSolConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 8),
    _CucsSolConfigSpeed_Type()
)
cucsSolConfigSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigSpeed.setStatus("current")
_CucsSolConfigPolicyLevel_Type = Gauge32
_CucsSolConfigPolicyLevel_Object = MibTableColumn
cucsSolConfigPolicyLevel = _CucsSolConfigPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 9),
    _CucsSolConfigPolicyLevel_Type()
)
cucsSolConfigPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigPolicyLevel.setStatus("current")
_CucsSolConfigPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsSolConfigPolicyOwner_Object = MibTableColumn
cucsSolConfigPolicyOwner = _CucsSolConfigPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 1, 1, 10),
    _CucsSolConfigPolicyOwner_Type()
)
cucsSolConfigPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolConfigPolicyOwner.setStatus("current")
_CucsSolIfTable_Object = MibTable
cucsSolIfTable = _CucsSolIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2)
)
if mibBuilder.loadTexts:
    cucsSolIfTable.setStatus("current")
_CucsSolIfEntry_Object = MibTableRow
cucsSolIfEntry = _CucsSolIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1)
)
cucsSolIfEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SOL-MIB", "cucsSolIfInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSolIfEntry.setStatus("current")
_CucsSolIfInstanceId_Type = CucsManagedObjectId
_CucsSolIfInstanceId_Object = MibTableColumn
cucsSolIfInstanceId = _CucsSolIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 1),
    _CucsSolIfInstanceId_Type()
)
cucsSolIfInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSolIfInstanceId.setStatus("current")
_CucsSolIfDn_Type = CucsManagedObjectDn
_CucsSolIfDn_Object = MibTableColumn
cucsSolIfDn = _CucsSolIfDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 2),
    _CucsSolIfDn_Type()
)
cucsSolIfDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfDn.setStatus("current")
_CucsSolIfRn_Type = SnmpAdminString
_CucsSolIfRn_Object = MibTableColumn
cucsSolIfRn = _CucsSolIfRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 3),
    _CucsSolIfRn_Type()
)
cucsSolIfRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfRn.setStatus("current")
_CucsSolIfAdminState_Type = CucsSolAdminState
_CucsSolIfAdminState_Object = MibTableColumn
cucsSolIfAdminState = _CucsSolIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 4),
    _CucsSolIfAdminState_Type()
)
cucsSolIfAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfAdminState.setStatus("current")
_CucsSolIfDescr_Type = SnmpAdminString
_CucsSolIfDescr_Object = MibTableColumn
cucsSolIfDescr = _CucsSolIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 5),
    _CucsSolIfDescr_Type()
)
cucsSolIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfDescr.setStatus("current")
_CucsSolIfIntId_Type = SnmpAdminString
_CucsSolIfIntId_Object = MibTableColumn
cucsSolIfIntId = _CucsSolIfIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 6),
    _CucsSolIfIntId_Type()
)
cucsSolIfIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfIntId.setStatus("current")
_CucsSolIfName_Type = SnmpAdminString
_CucsSolIfName_Object = MibTableColumn
cucsSolIfName = _CucsSolIfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 7),
    _CucsSolIfName_Type()
)
cucsSolIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfName.setStatus("current")
_CucsSolIfSpeed_Type = CucsSolSpeed
_CucsSolIfSpeed_Object = MibTableColumn
cucsSolIfSpeed = _CucsSolIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 8),
    _CucsSolIfSpeed_Type()
)
cucsSolIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfSpeed.setStatus("current")
_CucsSolIfPolicyLevel_Type = Gauge32
_CucsSolIfPolicyLevel_Object = MibTableColumn
cucsSolIfPolicyLevel = _CucsSolIfPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 9),
    _CucsSolIfPolicyLevel_Type()
)
cucsSolIfPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfPolicyLevel.setStatus("current")
_CucsSolIfPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsSolIfPolicyOwner_Object = MibTableColumn
cucsSolIfPolicyOwner = _CucsSolIfPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 2, 1, 10),
    _CucsSolIfPolicyOwner_Type()
)
cucsSolIfPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolIfPolicyOwner.setStatus("current")
_CucsSolPolicyTable_Object = MibTable
cucsSolPolicyTable = _CucsSolPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3)
)
if mibBuilder.loadTexts:
    cucsSolPolicyTable.setStatus("current")
_CucsSolPolicyEntry_Object = MibTableRow
cucsSolPolicyEntry = _CucsSolPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1)
)
cucsSolPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-SOL-MIB", "cucsSolPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsSolPolicyEntry.setStatus("current")
_CucsSolPolicyInstanceId_Type = CucsManagedObjectId
_CucsSolPolicyInstanceId_Object = MibTableColumn
cucsSolPolicyInstanceId = _CucsSolPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 1),
    _CucsSolPolicyInstanceId_Type()
)
cucsSolPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsSolPolicyInstanceId.setStatus("current")
_CucsSolPolicyDn_Type = CucsManagedObjectDn
_CucsSolPolicyDn_Object = MibTableColumn
cucsSolPolicyDn = _CucsSolPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 2),
    _CucsSolPolicyDn_Type()
)
cucsSolPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyDn.setStatus("current")
_CucsSolPolicyRn_Type = SnmpAdminString
_CucsSolPolicyRn_Object = MibTableColumn
cucsSolPolicyRn = _CucsSolPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 3),
    _CucsSolPolicyRn_Type()
)
cucsSolPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyRn.setStatus("current")
_CucsSolPolicyAdminState_Type = CucsSolAdminState
_CucsSolPolicyAdminState_Object = MibTableColumn
cucsSolPolicyAdminState = _CucsSolPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 4),
    _CucsSolPolicyAdminState_Type()
)
cucsSolPolicyAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyAdminState.setStatus("current")
_CucsSolPolicyDescr_Type = SnmpAdminString
_CucsSolPolicyDescr_Object = MibTableColumn
cucsSolPolicyDescr = _CucsSolPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 5),
    _CucsSolPolicyDescr_Type()
)
cucsSolPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyDescr.setStatus("current")
_CucsSolPolicyIntId_Type = SnmpAdminString
_CucsSolPolicyIntId_Object = MibTableColumn
cucsSolPolicyIntId = _CucsSolPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 6),
    _CucsSolPolicyIntId_Type()
)
cucsSolPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyIntId.setStatus("current")
_CucsSolPolicyName_Type = SnmpAdminString
_CucsSolPolicyName_Object = MibTableColumn
cucsSolPolicyName = _CucsSolPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 7),
    _CucsSolPolicyName_Type()
)
cucsSolPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyName.setStatus("current")
_CucsSolPolicySpeed_Type = CucsSolSpeed
_CucsSolPolicySpeed_Object = MibTableColumn
cucsSolPolicySpeed = _CucsSolPolicySpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 8),
    _CucsSolPolicySpeed_Type()
)
cucsSolPolicySpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicySpeed.setStatus("current")
_CucsSolPolicyPolicyLevel_Type = Gauge32
_CucsSolPolicyPolicyLevel_Object = MibTableColumn
cucsSolPolicyPolicyLevel = _CucsSolPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 9),
    _CucsSolPolicyPolicyLevel_Type()
)
cucsSolPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyPolicyLevel.setStatus("current")
_CucsSolPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsSolPolicyPolicyOwner_Object = MibTableColumn
cucsSolPolicyPolicyOwner = _CucsSolPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 10),
    _CucsSolPolicyPolicyOwner_Type()
)
cucsSolPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyPolicyOwner.setStatus("current")
_CucsSolPolicyPropAcl_Type = Unsigned64
_CucsSolPolicyPropAcl_Object = MibTableColumn
cucsSolPolicyPropAcl = _CucsSolPolicyPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 43, 3, 1, 11),
    _CucsSolPolicyPropAcl_Type()
)
cucsSolPolicyPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsSolPolicyPropAcl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-SOL-MIB",
    **{"cucsSolObjects": cucsSolObjects,
       "cucsSolConfigTable": cucsSolConfigTable,
       "cucsSolConfigEntry": cucsSolConfigEntry,
       "cucsSolConfigInstanceId": cucsSolConfigInstanceId,
       "cucsSolConfigDn": cucsSolConfigDn,
       "cucsSolConfigRn": cucsSolConfigRn,
       "cucsSolConfigAdminState": cucsSolConfigAdminState,
       "cucsSolConfigDescr": cucsSolConfigDescr,
       "cucsSolConfigIntId": cucsSolConfigIntId,
       "cucsSolConfigName": cucsSolConfigName,
       "cucsSolConfigSpeed": cucsSolConfigSpeed,
       "cucsSolConfigPolicyLevel": cucsSolConfigPolicyLevel,
       "cucsSolConfigPolicyOwner": cucsSolConfigPolicyOwner,
       "cucsSolIfTable": cucsSolIfTable,
       "cucsSolIfEntry": cucsSolIfEntry,
       "cucsSolIfInstanceId": cucsSolIfInstanceId,
       "cucsSolIfDn": cucsSolIfDn,
       "cucsSolIfRn": cucsSolIfRn,
       "cucsSolIfAdminState": cucsSolIfAdminState,
       "cucsSolIfDescr": cucsSolIfDescr,
       "cucsSolIfIntId": cucsSolIfIntId,
       "cucsSolIfName": cucsSolIfName,
       "cucsSolIfSpeed": cucsSolIfSpeed,
       "cucsSolIfPolicyLevel": cucsSolIfPolicyLevel,
       "cucsSolIfPolicyOwner": cucsSolIfPolicyOwner,
       "cucsSolPolicyTable": cucsSolPolicyTable,
       "cucsSolPolicyEntry": cucsSolPolicyEntry,
       "cucsSolPolicyInstanceId": cucsSolPolicyInstanceId,
       "cucsSolPolicyDn": cucsSolPolicyDn,
       "cucsSolPolicyRn": cucsSolPolicyRn,
       "cucsSolPolicyAdminState": cucsSolPolicyAdminState,
       "cucsSolPolicyDescr": cucsSolPolicyDescr,
       "cucsSolPolicyIntId": cucsSolPolicyIntId,
       "cucsSolPolicyName": cucsSolPolicyName,
       "cucsSolPolicySpeed": cucsSolPolicySpeed,
       "cucsSolPolicyPolicyLevel": cucsSolPolicyPolicyLevel,
       "cucsSolPolicyPolicyOwner": cucsSolPolicyPolicyOwner,
       "cucsSolPolicyPropAcl": cucsSolPolicyPropAcl}
)
