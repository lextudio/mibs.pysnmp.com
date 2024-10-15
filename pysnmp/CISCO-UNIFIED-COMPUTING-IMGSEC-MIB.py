# SNMP MIB module (CISCO-UNIFIED-COMPUTING-IMGSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-IMGSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:42 2024
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

(CucsImgsecKeyType,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsImgsecKeyType",
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

cucsImgsecObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsImgsecKeyTable_Object = MibTable
cucsImgsecKeyTable = _CucsImgsecKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1)
)
if mibBuilder.loadTexts:
    cucsImgsecKeyTable.setStatus("current")
_CucsImgsecKeyEntry_Object = MibTableRow
cucsImgsecKeyEntry = _CucsImgsecKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1)
)
cucsImgsecKeyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IMGSEC-MIB", "cucsImgsecKeyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsImgsecKeyEntry.setStatus("current")
_CucsImgsecKeyInstanceId_Type = CucsManagedObjectId
_CucsImgsecKeyInstanceId_Object = MibTableColumn
cucsImgsecKeyInstanceId = _CucsImgsecKeyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 1),
    _CucsImgsecKeyInstanceId_Type()
)
cucsImgsecKeyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsImgsecKeyInstanceId.setStatus("current")
_CucsImgsecKeyDn_Type = CucsManagedObjectDn
_CucsImgsecKeyDn_Object = MibTableColumn
cucsImgsecKeyDn = _CucsImgsecKeyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 2),
    _CucsImgsecKeyDn_Type()
)
cucsImgsecKeyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecKeyDn.setStatus("current")
_CucsImgsecKeyRn_Type = SnmpAdminString
_CucsImgsecKeyRn_Object = MibTableColumn
cucsImgsecKeyRn = _CucsImgsecKeyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 3),
    _CucsImgsecKeyRn_Type()
)
cucsImgsecKeyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecKeyRn.setStatus("current")
_CucsImgsecKeyType_Type = CucsImgsecKeyType
_CucsImgsecKeyType_Object = MibTableColumn
cucsImgsecKeyType = _CucsImgsecKeyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 4),
    _CucsImgsecKeyType_Type()
)
cucsImgsecKeyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecKeyType.setStatus("current")
_CucsImgsecKeyValue_Type = SnmpAdminString
_CucsImgsecKeyValue_Object = MibTableColumn
cucsImgsecKeyValue = _CucsImgsecKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 1, 1, 5),
    _CucsImgsecKeyValue_Type()
)
cucsImgsecKeyValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecKeyValue.setStatus("current")
_CucsImgsecPolicyTable_Object = MibTable
cucsImgsecPolicyTable = _CucsImgsecPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2)
)
if mibBuilder.loadTexts:
    cucsImgsecPolicyTable.setStatus("current")
_CucsImgsecPolicyEntry_Object = MibTableRow
cucsImgsecPolicyEntry = _CucsImgsecPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1)
)
cucsImgsecPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-IMGSEC-MIB", "cucsImgsecPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsImgsecPolicyEntry.setStatus("current")
_CucsImgsecPolicyInstanceId_Type = CucsManagedObjectId
_CucsImgsecPolicyInstanceId_Object = MibTableColumn
cucsImgsecPolicyInstanceId = _CucsImgsecPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 1),
    _CucsImgsecPolicyInstanceId_Type()
)
cucsImgsecPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsImgsecPolicyInstanceId.setStatus("current")
_CucsImgsecPolicyDn_Type = CucsManagedObjectDn
_CucsImgsecPolicyDn_Object = MibTableColumn
cucsImgsecPolicyDn = _CucsImgsecPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 2),
    _CucsImgsecPolicyDn_Type()
)
cucsImgsecPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecPolicyDn.setStatus("current")
_CucsImgsecPolicyRn_Type = SnmpAdminString
_CucsImgsecPolicyRn_Object = MibTableColumn
cucsImgsecPolicyRn = _CucsImgsecPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 3),
    _CucsImgsecPolicyRn_Type()
)
cucsImgsecPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecPolicyRn.setStatus("current")
_CucsImgsecPolicyDescr_Type = SnmpAdminString
_CucsImgsecPolicyDescr_Object = MibTableColumn
cucsImgsecPolicyDescr = _CucsImgsecPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 4),
    _CucsImgsecPolicyDescr_Type()
)
cucsImgsecPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecPolicyDescr.setStatus("current")
_CucsImgsecPolicyIntId_Type = SnmpAdminString
_CucsImgsecPolicyIntId_Object = MibTableColumn
cucsImgsecPolicyIntId = _CucsImgsecPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 5),
    _CucsImgsecPolicyIntId_Type()
)
cucsImgsecPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecPolicyIntId.setStatus("current")
_CucsImgsecPolicyName_Type = SnmpAdminString
_CucsImgsecPolicyName_Object = MibTableColumn
cucsImgsecPolicyName = _CucsImgsecPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 6),
    _CucsImgsecPolicyName_Type()
)
cucsImgsecPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecPolicyName.setStatus("current")
_CucsImgsecPolicyPolicyLevel_Type = Gauge32
_CucsImgsecPolicyPolicyLevel_Object = MibTableColumn
cucsImgsecPolicyPolicyLevel = _CucsImgsecPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 7),
    _CucsImgsecPolicyPolicyLevel_Type()
)
cucsImgsecPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecPolicyPolicyLevel.setStatus("current")
_CucsImgsecPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsImgsecPolicyPolicyOwner_Object = MibTableColumn
cucsImgsecPolicyPolicyOwner = _CucsImgsecPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 56, 2, 1, 8),
    _CucsImgsecPolicyPolicyOwner_Type()
)
cucsImgsecPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsImgsecPolicyPolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-IMGSEC-MIB",
    **{"cucsImgsecObjects": cucsImgsecObjects,
       "cucsImgsecKeyTable": cucsImgsecKeyTable,
       "cucsImgsecKeyEntry": cucsImgsecKeyEntry,
       "cucsImgsecKeyInstanceId": cucsImgsecKeyInstanceId,
       "cucsImgsecKeyDn": cucsImgsecKeyDn,
       "cucsImgsecKeyRn": cucsImgsecKeyRn,
       "cucsImgsecKeyType": cucsImgsecKeyType,
       "cucsImgsecKeyValue": cucsImgsecKeyValue,
       "cucsImgsecPolicyTable": cucsImgsecPolicyTable,
       "cucsImgsecPolicyEntry": cucsImgsecPolicyEntry,
       "cucsImgsecPolicyInstanceId": cucsImgsecPolicyInstanceId,
       "cucsImgsecPolicyDn": cucsImgsecPolicyDn,
       "cucsImgsecPolicyRn": cucsImgsecPolicyRn,
       "cucsImgsecPolicyDescr": cucsImgsecPolicyDescr,
       "cucsImgsecPolicyIntId": cucsImgsecPolicyIntId,
       "cucsImgsecPolicyName": cucsImgsecPolicyName,
       "cucsImgsecPolicyPolicyLevel": cucsImgsecPolicyPolicyLevel,
       "cucsImgsecPolicyPolicyOwner": cucsImgsecPolicyPolicyOwner}
)
