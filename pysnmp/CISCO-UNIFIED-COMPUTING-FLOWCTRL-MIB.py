# SNMP MIB module (CISCO-UNIFIED-COMPUTING-FLOWCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-FLOWCTRL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:35 2024
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

(CucsFlowctrlConfig,
 CucsFlowctrlFlowControl,
 CucsFlowctrlPriorityPause,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsFlowctrlConfig",
    "CucsFlowctrlFlowControl",
    "CucsFlowctrlPriorityPause",
    "CucsPolicyPolicyOwner")

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

cucsFlowctrlObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsFlowctrlDefinitionTable_Object = MibTable
cucsFlowctrlDefinitionTable = _CucsFlowctrlDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1)
)
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionTable.setStatus("current")
_CucsFlowctrlDefinitionEntry_Object = MibTableRow
cucsFlowctrlDefinitionEntry = _CucsFlowctrlDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1)
)
cucsFlowctrlDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FLOWCTRL-MIB", "cucsFlowctrlDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionEntry.setStatus("current")
_CucsFlowctrlDefinitionInstanceId_Type = CucsManagedObjectId
_CucsFlowctrlDefinitionInstanceId_Object = MibTableColumn
cucsFlowctrlDefinitionInstanceId = _CucsFlowctrlDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 1),
    _CucsFlowctrlDefinitionInstanceId_Type()
)
cucsFlowctrlDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionInstanceId.setStatus("current")
_CucsFlowctrlDefinitionDn_Type = CucsManagedObjectDn
_CucsFlowctrlDefinitionDn_Object = MibTableColumn
cucsFlowctrlDefinitionDn = _CucsFlowctrlDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 2),
    _CucsFlowctrlDefinitionDn_Type()
)
cucsFlowctrlDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionDn.setStatus("current")
_CucsFlowctrlDefinitionRn_Type = SnmpAdminString
_CucsFlowctrlDefinitionRn_Object = MibTableColumn
cucsFlowctrlDefinitionRn = _CucsFlowctrlDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 3),
    _CucsFlowctrlDefinitionRn_Type()
)
cucsFlowctrlDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionRn.setStatus("current")
_CucsFlowctrlDefinitionDescr_Type = SnmpAdminString
_CucsFlowctrlDefinitionDescr_Object = MibTableColumn
cucsFlowctrlDefinitionDescr = _CucsFlowctrlDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 4),
    _CucsFlowctrlDefinitionDescr_Type()
)
cucsFlowctrlDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionDescr.setStatus("current")
_CucsFlowctrlDefinitionIntId_Type = SnmpAdminString
_CucsFlowctrlDefinitionIntId_Object = MibTableColumn
cucsFlowctrlDefinitionIntId = _CucsFlowctrlDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 5),
    _CucsFlowctrlDefinitionIntId_Type()
)
cucsFlowctrlDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionIntId.setStatus("current")
_CucsFlowctrlDefinitionName_Type = SnmpAdminString
_CucsFlowctrlDefinitionName_Object = MibTableColumn
cucsFlowctrlDefinitionName = _CucsFlowctrlDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 6),
    _CucsFlowctrlDefinitionName_Type()
)
cucsFlowctrlDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionName.setStatus("current")
_CucsFlowctrlDefinitionPolicyLevel_Type = Gauge32
_CucsFlowctrlDefinitionPolicyLevel_Object = MibTableColumn
cucsFlowctrlDefinitionPolicyLevel = _CucsFlowctrlDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 7),
    _CucsFlowctrlDefinitionPolicyLevel_Type()
)
cucsFlowctrlDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionPolicyLevel.setStatus("current")
_CucsFlowctrlDefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsFlowctrlDefinitionPolicyOwner_Object = MibTableColumn
cucsFlowctrlDefinitionPolicyOwner = _CucsFlowctrlDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 1, 1, 8),
    _CucsFlowctrlDefinitionPolicyOwner_Type()
)
cucsFlowctrlDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlDefinitionPolicyOwner.setStatus("current")
_CucsFlowctrlItemTable_Object = MibTable
cucsFlowctrlItemTable = _CucsFlowctrlItemTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2)
)
if mibBuilder.loadTexts:
    cucsFlowctrlItemTable.setStatus("current")
_CucsFlowctrlItemEntry_Object = MibTableRow
cucsFlowctrlItemEntry = _CucsFlowctrlItemEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1)
)
cucsFlowctrlItemEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-FLOWCTRL-MIB", "cucsFlowctrlItemInstanceId"),
)
if mibBuilder.loadTexts:
    cucsFlowctrlItemEntry.setStatus("current")
_CucsFlowctrlItemInstanceId_Type = CucsManagedObjectId
_CucsFlowctrlItemInstanceId_Object = MibTableColumn
cucsFlowctrlItemInstanceId = _CucsFlowctrlItemInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 1),
    _CucsFlowctrlItemInstanceId_Type()
)
cucsFlowctrlItemInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsFlowctrlItemInstanceId.setStatus("current")
_CucsFlowctrlItemDn_Type = CucsManagedObjectDn
_CucsFlowctrlItemDn_Object = MibTableColumn
cucsFlowctrlItemDn = _CucsFlowctrlItemDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 2),
    _CucsFlowctrlItemDn_Type()
)
cucsFlowctrlItemDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlItemDn.setStatus("current")
_CucsFlowctrlItemRn_Type = SnmpAdminString
_CucsFlowctrlItemRn_Object = MibTableColumn
cucsFlowctrlItemRn = _CucsFlowctrlItemRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 3),
    _CucsFlowctrlItemRn_Type()
)
cucsFlowctrlItemRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlItemRn.setStatus("current")
_CucsFlowctrlItemName_Type = SnmpAdminString
_CucsFlowctrlItemName_Object = MibTableColumn
cucsFlowctrlItemName = _CucsFlowctrlItemName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 4),
    _CucsFlowctrlItemName_Type()
)
cucsFlowctrlItemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlItemName.setStatus("current")
_CucsFlowctrlItemPrio_Type = CucsFlowctrlPriorityPause
_CucsFlowctrlItemPrio_Object = MibTableColumn
cucsFlowctrlItemPrio = _CucsFlowctrlItemPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 5),
    _CucsFlowctrlItemPrio_Type()
)
cucsFlowctrlItemPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlItemPrio.setStatus("current")
_CucsFlowctrlItemRcv_Type = CucsFlowctrlFlowControl
_CucsFlowctrlItemRcv_Object = MibTableColumn
cucsFlowctrlItemRcv = _CucsFlowctrlItemRcv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 6),
    _CucsFlowctrlItemRcv_Type()
)
cucsFlowctrlItemRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlItemRcv.setStatus("current")
_CucsFlowctrlItemSnd_Type = CucsFlowctrlFlowControl
_CucsFlowctrlItemSnd_Object = MibTableColumn
cucsFlowctrlItemSnd = _CucsFlowctrlItemSnd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 7),
    _CucsFlowctrlItemSnd_Type()
)
cucsFlowctrlItemSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlItemSnd.setStatus("current")
_CucsFlowctrlItemConfig_Type = CucsFlowctrlConfig
_CucsFlowctrlItemConfig_Object = MibTableColumn
cucsFlowctrlItemConfig = _CucsFlowctrlItemConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 23, 2, 1, 8),
    _CucsFlowctrlItemConfig_Type()
)
cucsFlowctrlItemConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsFlowctrlItemConfig.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-FLOWCTRL-MIB",
    **{"cucsFlowctrlObjects": cucsFlowctrlObjects,
       "cucsFlowctrlDefinitionTable": cucsFlowctrlDefinitionTable,
       "cucsFlowctrlDefinitionEntry": cucsFlowctrlDefinitionEntry,
       "cucsFlowctrlDefinitionInstanceId": cucsFlowctrlDefinitionInstanceId,
       "cucsFlowctrlDefinitionDn": cucsFlowctrlDefinitionDn,
       "cucsFlowctrlDefinitionRn": cucsFlowctrlDefinitionRn,
       "cucsFlowctrlDefinitionDescr": cucsFlowctrlDefinitionDescr,
       "cucsFlowctrlDefinitionIntId": cucsFlowctrlDefinitionIntId,
       "cucsFlowctrlDefinitionName": cucsFlowctrlDefinitionName,
       "cucsFlowctrlDefinitionPolicyLevel": cucsFlowctrlDefinitionPolicyLevel,
       "cucsFlowctrlDefinitionPolicyOwner": cucsFlowctrlDefinitionPolicyOwner,
       "cucsFlowctrlItemTable": cucsFlowctrlItemTable,
       "cucsFlowctrlItemEntry": cucsFlowctrlItemEntry,
       "cucsFlowctrlItemInstanceId": cucsFlowctrlItemInstanceId,
       "cucsFlowctrlItemDn": cucsFlowctrlItemDn,
       "cucsFlowctrlItemRn": cucsFlowctrlItemRn,
       "cucsFlowctrlItemName": cucsFlowctrlItemName,
       "cucsFlowctrlItemPrio": cucsFlowctrlItemPrio,
       "cucsFlowctrlItemRcv": cucsFlowctrlItemRcv,
       "cucsFlowctrlItemSnd": cucsFlowctrlItemSnd,
       "cucsFlowctrlItemConfig": cucsFlowctrlItemConfig}
)
