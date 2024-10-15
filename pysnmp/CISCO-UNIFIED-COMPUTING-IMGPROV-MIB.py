# SNMP MIB module (CISCO-UNIFIED-COMPUTING-IMGPROV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-IMGPROV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:41 2024
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

(CucsPolicyPolicyOwner,) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
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

cucsImgprovObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsImgprovPolicyTable_Object = MibTable
cucsImgprovPolicyTable = _CucsImgprovPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1)
)
if mibBuilder.loadTexts:
    cucsImgprovPolicyTable.setStatus("current")
_CucsImgprovPolicyEntry_Object = MibTableRow
cucsImgprovPolicyEntry = _CucsImgprovPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1)
)
cucsImgprovPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IMGPROV-MIB", "cucsImgprovPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsImgprovPolicyEntry.setStatus("current")
_CucsImgprovPolicyInstanceId_Type = CucsManagedObjectId
_CucsImgprovPolicyInstanceId_Object = MibTableColumn
cucsImgprovPolicyInstanceId = _CucsImgprovPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 1),
    _CucsImgprovPolicyInstanceId_Type()
)
cucsImgprovPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsImgprovPolicyInstanceId.setStatus("current")
_CucsImgprovPolicyDn_Type = CucsManagedObjectDn
_CucsImgprovPolicyDn_Object = MibTableColumn
cucsImgprovPolicyDn = _CucsImgprovPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 2),
    _CucsImgprovPolicyDn_Type()
)
cucsImgprovPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovPolicyDn.setStatus("current")
_CucsImgprovPolicyRn_Type = SnmpAdminString
_CucsImgprovPolicyRn_Object = MibTableColumn
cucsImgprovPolicyRn = _CucsImgprovPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 3),
    _CucsImgprovPolicyRn_Type()
)
cucsImgprovPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovPolicyRn.setStatus("current")
_CucsImgprovPolicyDescr_Type = SnmpAdminString
_CucsImgprovPolicyDescr_Object = MibTableColumn
cucsImgprovPolicyDescr = _CucsImgprovPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 4),
    _CucsImgprovPolicyDescr_Type()
)
cucsImgprovPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovPolicyDescr.setStatus("current")
_CucsImgprovPolicyIntId_Type = SnmpAdminString
_CucsImgprovPolicyIntId_Object = MibTableColumn
cucsImgprovPolicyIntId = _CucsImgprovPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 5),
    _CucsImgprovPolicyIntId_Type()
)
cucsImgprovPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovPolicyIntId.setStatus("current")
_CucsImgprovPolicyName_Type = SnmpAdminString
_CucsImgprovPolicyName_Object = MibTableColumn
cucsImgprovPolicyName = _CucsImgprovPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 6),
    _CucsImgprovPolicyName_Type()
)
cucsImgprovPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovPolicyName.setStatus("current")
_CucsImgprovPolicyPolicyLevel_Type = Gauge32
_CucsImgprovPolicyPolicyLevel_Object = MibTableColumn
cucsImgprovPolicyPolicyLevel = _CucsImgprovPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 7),
    _CucsImgprovPolicyPolicyLevel_Type()
)
cucsImgprovPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovPolicyPolicyLevel.setStatus("current")
_CucsImgprovPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsImgprovPolicyPolicyOwner_Object = MibTableColumn
cucsImgprovPolicyPolicyOwner = _CucsImgprovPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 1, 1, 8),
    _CucsImgprovPolicyPolicyOwner_Type()
)
cucsImgprovPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovPolicyPolicyOwner.setStatus("current")
_CucsImgprovTargetTable_Object = MibTable
cucsImgprovTargetTable = _CucsImgprovTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 2)
)
if mibBuilder.loadTexts:
    cucsImgprovTargetTable.setStatus("current")
_CucsImgprovTargetEntry_Object = MibTableRow
cucsImgprovTargetEntry = _CucsImgprovTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 2, 1)
)
cucsImgprovTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IMGPROV-MIB", "cucsImgprovTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsImgprovTargetEntry.setStatus("current")
_CucsImgprovTargetInstanceId_Type = CucsManagedObjectId
_CucsImgprovTargetInstanceId_Object = MibTableColumn
cucsImgprovTargetInstanceId = _CucsImgprovTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 2, 1, 1),
    _CucsImgprovTargetInstanceId_Type()
)
cucsImgprovTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsImgprovTargetInstanceId.setStatus("current")
_CucsImgprovTargetDn_Type = CucsManagedObjectDn
_CucsImgprovTargetDn_Object = MibTableColumn
cucsImgprovTargetDn = _CucsImgprovTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 2, 1, 2),
    _CucsImgprovTargetDn_Type()
)
cucsImgprovTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovTargetDn.setStatus("current")
_CucsImgprovTargetRn_Type = SnmpAdminString
_CucsImgprovTargetRn_Object = MibTableColumn
cucsImgprovTargetRn = _CucsImgprovTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 2, 1, 3),
    _CucsImgprovTargetRn_Type()
)
cucsImgprovTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovTargetRn.setStatus("current")
_CucsImgprovTargetName_Type = SnmpAdminString
_CucsImgprovTargetName_Object = MibTableColumn
cucsImgprovTargetName = _CucsImgprovTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 55, 2, 1, 4),
    _CucsImgprovTargetName_Type()
)
cucsImgprovTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgprovTargetName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-IMGPROV-MIB",
    **{"cucsImgprovObjects": cucsImgprovObjects,
       "cucsImgprovPolicyTable": cucsImgprovPolicyTable,
       "cucsImgprovPolicyEntry": cucsImgprovPolicyEntry,
       "cucsImgprovPolicyInstanceId": cucsImgprovPolicyInstanceId,
       "cucsImgprovPolicyDn": cucsImgprovPolicyDn,
       "cucsImgprovPolicyRn": cucsImgprovPolicyRn,
       "cucsImgprovPolicyDescr": cucsImgprovPolicyDescr,
       "cucsImgprovPolicyIntId": cucsImgprovPolicyIntId,
       "cucsImgprovPolicyName": cucsImgprovPolicyName,
       "cucsImgprovPolicyPolicyLevel": cucsImgprovPolicyPolicyLevel,
       "cucsImgprovPolicyPolicyOwner": cucsImgprovPolicyPolicyOwner,
       "cucsImgprovTargetTable": cucsImgprovTargetTable,
       "cucsImgprovTargetEntry": cucsImgprovTargetEntry,
       "cucsImgprovTargetInstanceId": cucsImgprovTargetInstanceId,
       "cucsImgprovTargetDn": cucsImgprovTargetDn,
       "cucsImgprovTargetRn": cucsImgprovTargetRn,
       "cucsImgprovTargetName": cucsImgprovTargetName}
)
