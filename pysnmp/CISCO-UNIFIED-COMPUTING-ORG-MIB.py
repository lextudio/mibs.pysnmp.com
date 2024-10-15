# SNMP MIB module (CISCO-UNIFIED-COMPUTING-ORG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-ORG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:05 2024
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

(CucsOrgLevel,
 CucsOrgSrcMask) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsOrgLevel",
    "CucsOrgSrcMask")

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

cucsOrgObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsOrgOrgTable_Object = MibTable
cucsOrgOrgTable = _CucsOrgOrgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1)
)
if mibBuilder.loadTexts:
    cucsOrgOrgTable.setStatus("current")
_CucsOrgOrgEntry_Object = MibTableRow
cucsOrgOrgEntry = _CucsOrgOrgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1)
)
cucsOrgOrgEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ORG-MIB", "cucsOrgOrgInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOrgOrgEntry.setStatus("current")
_CucsOrgOrgInstanceId_Type = CucsManagedObjectId
_CucsOrgOrgInstanceId_Object = MibTableColumn
cucsOrgOrgInstanceId = _CucsOrgOrgInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 1),
    _CucsOrgOrgInstanceId_Type()
)
cucsOrgOrgInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOrgOrgInstanceId.setStatus("current")
_CucsOrgOrgDn_Type = CucsManagedObjectDn
_CucsOrgOrgDn_Object = MibTableColumn
cucsOrgOrgDn = _CucsOrgOrgDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 2),
    _CucsOrgOrgDn_Type()
)
cucsOrgOrgDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgOrgDn.setStatus("current")
_CucsOrgOrgRn_Type = SnmpAdminString
_CucsOrgOrgRn_Object = MibTableColumn
cucsOrgOrgRn = _CucsOrgOrgRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 3),
    _CucsOrgOrgRn_Type()
)
cucsOrgOrgRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgOrgRn.setStatus("current")
_CucsOrgOrgDescr_Type = SnmpAdminString
_CucsOrgOrgDescr_Object = MibTableColumn
cucsOrgOrgDescr = _CucsOrgOrgDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 4),
    _CucsOrgOrgDescr_Type()
)
cucsOrgOrgDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgOrgDescr.setStatus("current")
_CucsOrgOrgFltAggr_Type = Unsigned64
_CucsOrgOrgFltAggr_Object = MibTableColumn
cucsOrgOrgFltAggr = _CucsOrgOrgFltAggr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 5),
    _CucsOrgOrgFltAggr_Type()
)
cucsOrgOrgFltAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgOrgFltAggr.setStatus("current")
_CucsOrgOrgLevel_Type = CucsOrgLevel
_CucsOrgOrgLevel_Object = MibTableColumn
cucsOrgOrgLevel = _CucsOrgOrgLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 6),
    _CucsOrgOrgLevel_Type()
)
cucsOrgOrgLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgOrgLevel.setStatus("current")
_CucsOrgOrgName_Type = SnmpAdminString
_CucsOrgOrgName_Object = MibTableColumn
cucsOrgOrgName = _CucsOrgOrgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 7),
    _CucsOrgOrgName_Type()
)
cucsOrgOrgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgOrgName.setStatus("current")
_CucsOrgOrgPermAccess_Type = TruthValue
_CucsOrgOrgPermAccess_Object = MibTableColumn
cucsOrgOrgPermAccess = _CucsOrgOrgPermAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 1, 1, 8),
    _CucsOrgOrgPermAccess_Type()
)
cucsOrgOrgPermAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgOrgPermAccess.setStatus("current")
_CucsOrgSourceMaskTable_Object = MibTable
cucsOrgSourceMaskTable = _CucsOrgSourceMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 2)
)
if mibBuilder.loadTexts:
    cucsOrgSourceMaskTable.setStatus("current")
_CucsOrgSourceMaskEntry_Object = MibTableRow
cucsOrgSourceMaskEntry = _CucsOrgSourceMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 2, 1)
)
cucsOrgSourceMaskEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ORG-MIB", "cucsOrgSourceMaskInstanceId"),
)
if mibBuilder.loadTexts:
    cucsOrgSourceMaskEntry.setStatus("current")
_CucsOrgSourceMaskInstanceId_Type = CucsManagedObjectId
_CucsOrgSourceMaskInstanceId_Object = MibTableColumn
cucsOrgSourceMaskInstanceId = _CucsOrgSourceMaskInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 2, 1, 1),
    _CucsOrgSourceMaskInstanceId_Type()
)
cucsOrgSourceMaskInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsOrgSourceMaskInstanceId.setStatus("current")
_CucsOrgSourceMaskDn_Type = CucsManagedObjectDn
_CucsOrgSourceMaskDn_Object = MibTableColumn
cucsOrgSourceMaskDn = _CucsOrgSourceMaskDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 2, 1, 2),
    _CucsOrgSourceMaskDn_Type()
)
cucsOrgSourceMaskDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgSourceMaskDn.setStatus("current")
_CucsOrgSourceMaskRn_Type = SnmpAdminString
_CucsOrgSourceMaskRn_Object = MibTableColumn
cucsOrgSourceMaskRn = _CucsOrgSourceMaskRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 2, 1, 3),
    _CucsOrgSourceMaskRn_Type()
)
cucsOrgSourceMaskRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgSourceMaskRn.setStatus("current")
_CucsOrgSourceMaskMask_Type = CucsOrgSrcMask
_CucsOrgSourceMaskMask_Object = MibTableColumn
cucsOrgSourceMaskMask = _CucsOrgSourceMaskMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 34, 2, 1, 4),
    _CucsOrgSourceMaskMask_Type()
)
cucsOrgSourceMaskMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsOrgSourceMaskMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-ORG-MIB",
    **{"cucsOrgObjects": cucsOrgObjects,
       "cucsOrgOrgTable": cucsOrgOrgTable,
       "cucsOrgOrgEntry": cucsOrgOrgEntry,
       "cucsOrgOrgInstanceId": cucsOrgOrgInstanceId,
       "cucsOrgOrgDn": cucsOrgOrgDn,
       "cucsOrgOrgRn": cucsOrgOrgRn,
       "cucsOrgOrgDescr": cucsOrgOrgDescr,
       "cucsOrgOrgFltAggr": cucsOrgOrgFltAggr,
       "cucsOrgOrgLevel": cucsOrgOrgLevel,
       "cucsOrgOrgName": cucsOrgOrgName,
       "cucsOrgOrgPermAccess": cucsOrgOrgPermAccess,
       "cucsOrgSourceMaskTable": cucsOrgSourceMaskTable,
       "cucsOrgSourceMaskEntry": cucsOrgSourceMaskEntry,
       "cucsOrgSourceMaskInstanceId": cucsOrgSourceMaskInstanceId,
       "cucsOrgSourceMaskDn": cucsOrgSourceMaskDn,
       "cucsOrgSourceMaskRn": cucsOrgSourceMaskRn,
       "cucsOrgSourceMaskMask": cucsOrgSourceMaskMask}
)
