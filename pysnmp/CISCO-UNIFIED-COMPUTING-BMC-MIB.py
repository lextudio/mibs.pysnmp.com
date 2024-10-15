# SNMP MIB module (CISCO-UNIFIED-COMPUTING-BMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-BMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:04 2024
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

(CucsBmcSELCntEqptClassId,
 CucsBmcSELCntEqptInstIdPropId,
 CucsBmcSELCntStatsClassId) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsBmcSELCntEqptClassId",
    "CucsBmcSELCntEqptInstIdPropId",
    "CucsBmcSELCntStatsClassId")

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

cucsBmcObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsBmcSELCounterTable_Object = MibTable
cucsBmcSELCounterTable = _CucsBmcSELCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cucsBmcSELCounterTable.setStatus("current")
_CucsBmcSELCounterEntry_Object = MibTableRow
cucsBmcSELCounterEntry = _CucsBmcSELCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1)
)
cucsBmcSELCounterEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-BMC-MIB", "cucsBmcSELCounterInstanceId"),
)
if mibBuilder.loadTexts:
    cucsBmcSELCounterEntry.setStatus("current")
_CucsBmcSELCounterInstanceId_Type = CucsManagedObjectId
_CucsBmcSELCounterInstanceId_Object = MibTableColumn
cucsBmcSELCounterInstanceId = _CucsBmcSELCounterInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 1),
    _CucsBmcSELCounterInstanceId_Type()
)
cucsBmcSELCounterInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsBmcSELCounterInstanceId.setStatus("current")
_CucsBmcSELCounterDn_Type = CucsManagedObjectDn
_CucsBmcSELCounterDn_Object = MibTableColumn
cucsBmcSELCounterDn = _CucsBmcSELCounterDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 2),
    _CucsBmcSELCounterDn_Type()
)
cucsBmcSELCounterDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterDn.setStatus("current")
_CucsBmcSELCounterRn_Type = SnmpAdminString
_CucsBmcSELCounterRn_Object = MibTableColumn
cucsBmcSELCounterRn = _CucsBmcSELCounterRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 3),
    _CucsBmcSELCounterRn_Type()
)
cucsBmcSELCounterRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterRn.setStatus("current")
_CucsBmcSELCounterBitmask_Type = SnmpAdminString
_CucsBmcSELCounterBitmask_Object = MibTableColumn
cucsBmcSELCounterBitmask = _CucsBmcSELCounterBitmask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 4),
    _CucsBmcSELCounterBitmask_Type()
)
cucsBmcSELCounterBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterBitmask.setStatus("current")
_CucsBmcSELCounterCollInterval_Type = Gauge32
_CucsBmcSELCounterCollInterval_Object = MibTableColumn
cucsBmcSELCounterCollInterval = _CucsBmcSELCounterCollInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 5),
    _CucsBmcSELCounterCollInterval_Type()
)
cucsBmcSELCounterCollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterCollInterval.setStatus("current")
_CucsBmcSELCounterContClassId_Type = CucsBmcSELCntEqptClassId
_CucsBmcSELCounterContClassId_Object = MibTableColumn
cucsBmcSELCounterContClassId = _CucsBmcSELCounterContClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 6),
    _CucsBmcSELCounterContClassId_Type()
)
cucsBmcSELCounterContClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterContClassId.setStatus("current")
_CucsBmcSELCounterContInstId_Type = SnmpAdminString
_CucsBmcSELCounterContInstId_Object = MibTableColumn
cucsBmcSELCounterContInstId = _CucsBmcSELCounterContInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 7),
    _CucsBmcSELCounterContInstId_Type()
)
cucsBmcSELCounterContInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterContInstId.setStatus("current")
_CucsBmcSELCounterContInstIdPropId_Type = CucsBmcSELCntEqptInstIdPropId
_CucsBmcSELCounterContInstIdPropId_Object = MibTableColumn
cucsBmcSELCounterContInstIdPropId = _CucsBmcSELCounterContInstIdPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 8),
    _CucsBmcSELCounterContInstIdPropId_Type()
)
cucsBmcSELCounterContInstIdPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterContInstIdPropId.setStatus("current")
_CucsBmcSELCounterEqptClassId_Type = CucsBmcSELCntEqptClassId
_CucsBmcSELCounterEqptClassId_Object = MibTableColumn
cucsBmcSELCounterEqptClassId = _CucsBmcSELCounterEqptClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 9),
    _CucsBmcSELCounterEqptClassId_Type()
)
cucsBmcSELCounterEqptClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterEqptClassId.setStatus("current")
_CucsBmcSELCounterEqptInstId_Type = SnmpAdminString
_CucsBmcSELCounterEqptInstId_Object = MibTableColumn
cucsBmcSELCounterEqptInstId = _CucsBmcSELCounterEqptInstId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 10),
    _CucsBmcSELCounterEqptInstId_Type()
)
cucsBmcSELCounterEqptInstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterEqptInstId.setStatus("current")
_CucsBmcSELCounterEqptInstIdPropId_Type = CucsBmcSELCntEqptInstIdPropId
_CucsBmcSELCounterEqptInstIdPropId_Object = MibTableColumn
cucsBmcSELCounterEqptInstIdPropId = _CucsBmcSELCounterEqptInstIdPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 11),
    _CucsBmcSELCounterEqptInstIdPropId_Type()
)
cucsBmcSELCounterEqptInstIdPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterEqptInstIdPropId.setStatus("current")
_CucsBmcSELCounterGlobalId_Type = SnmpAdminString
_CucsBmcSELCounterGlobalId_Object = MibTableColumn
cucsBmcSELCounterGlobalId = _CucsBmcSELCounterGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 12),
    _CucsBmcSELCounterGlobalId_Type()
)
cucsBmcSELCounterGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterGlobalId.setStatus("current")
_CucsBmcSELCounterLocalId_Type = SnmpAdminString
_CucsBmcSELCounterLocalId_Object = MibTableColumn
cucsBmcSELCounterLocalId = _CucsBmcSELCounterLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 13),
    _CucsBmcSELCounterLocalId_Type()
)
cucsBmcSELCounterLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterLocalId.setStatus("current")
_CucsBmcSELCounterPcGlobalId_Type = SnmpAdminString
_CucsBmcSELCounterPcGlobalId_Object = MibTableColumn
cucsBmcSELCounterPcGlobalId = _CucsBmcSELCounterPcGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 14),
    _CucsBmcSELCounterPcGlobalId_Type()
)
cucsBmcSELCounterPcGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterPcGlobalId.setStatus("current")
_CucsBmcSELCounterPcLocalId_Type = SnmpAdminString
_CucsBmcSELCounterPcLocalId_Object = MibTableColumn
cucsBmcSELCounterPcLocalId = _CucsBmcSELCounterPcLocalId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 15),
    _CucsBmcSELCounterPcLocalId_Type()
)
cucsBmcSELCounterPcLocalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterPcLocalId.setStatus("current")
_CucsBmcSELCounterStatsClassId_Type = CucsBmcSELCntStatsClassId
_CucsBmcSELCounterStatsClassId_Object = MibTableColumn
cucsBmcSELCounterStatsClassId = _CucsBmcSELCounterStatsClassId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 16),
    _CucsBmcSELCounterStatsClassId_Type()
)
cucsBmcSELCounterStatsClassId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterStatsClassId.setStatus("current")
_CucsBmcSELCounterStatsPropId_Type = Integer32
_CucsBmcSELCounterStatsPropId_Object = MibTableColumn
cucsBmcSELCounterStatsPropId = _CucsBmcSELCounterStatsPropId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 17),
    _CucsBmcSELCounterStatsPropId_Type()
)
cucsBmcSELCounterStatsPropId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterStatsPropId.setStatus("current")
_CucsBmcSELCounterThreshold_Type = Gauge32
_CucsBmcSELCounterThreshold_Object = MibTableColumn
cucsBmcSELCounterThreshold = _CucsBmcSELCounterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 18),
    _CucsBmcSELCounterThreshold_Type()
)
cucsBmcSELCounterThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterThreshold.setStatus("current")
_CucsBmcSELCounterValue_Type = SnmpAdminString
_CucsBmcSELCounterValue_Object = MibTableColumn
cucsBmcSELCounterValue = _CucsBmcSELCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 5, 1, 1, 19),
    _CucsBmcSELCounterValue_Type()
)
cucsBmcSELCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsBmcSELCounterValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-BMC-MIB",
    **{"cucsBmcObjects": cucsBmcObjects,
       "cucsBmcSELCounterTable": cucsBmcSELCounterTable,
       "cucsBmcSELCounterEntry": cucsBmcSELCounterEntry,
       "cucsBmcSELCounterInstanceId": cucsBmcSELCounterInstanceId,
       "cucsBmcSELCounterDn": cucsBmcSELCounterDn,
       "cucsBmcSELCounterRn": cucsBmcSELCounterRn,
       "cucsBmcSELCounterBitmask": cucsBmcSELCounterBitmask,
       "cucsBmcSELCounterCollInterval": cucsBmcSELCounterCollInterval,
       "cucsBmcSELCounterContClassId": cucsBmcSELCounterContClassId,
       "cucsBmcSELCounterContInstId": cucsBmcSELCounterContInstId,
       "cucsBmcSELCounterContInstIdPropId": cucsBmcSELCounterContInstIdPropId,
       "cucsBmcSELCounterEqptClassId": cucsBmcSELCounterEqptClassId,
       "cucsBmcSELCounterEqptInstId": cucsBmcSELCounterEqptInstId,
       "cucsBmcSELCounterEqptInstIdPropId": cucsBmcSELCounterEqptInstIdPropId,
       "cucsBmcSELCounterGlobalId": cucsBmcSELCounterGlobalId,
       "cucsBmcSELCounterLocalId": cucsBmcSELCounterLocalId,
       "cucsBmcSELCounterPcGlobalId": cucsBmcSELCounterPcGlobalId,
       "cucsBmcSELCounterPcLocalId": cucsBmcSELCounterPcLocalId,
       "cucsBmcSELCounterStatsClassId": cucsBmcSELCounterStatsClassId,
       "cucsBmcSELCounterStatsPropId": cucsBmcSELCounterStatsPropId,
       "cucsBmcSELCounterThreshold": cucsBmcSELCounterThreshold,
       "cucsBmcSELCounterValue": cucsBmcSELCounterValue}
)
