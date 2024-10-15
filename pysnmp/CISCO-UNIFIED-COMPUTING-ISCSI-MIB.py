# SNMP MIB module (CISCO-UNIFIED-COMPUTING-ISCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-ISCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:48 2024
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

cucsIscsiObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsIscsiAuthProfileTable_Object = MibTable
cucsIscsiAuthProfileTable = _CucsIscsiAuthProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1)
)
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileTable.setStatus("current")
_CucsIscsiAuthProfileEntry_Object = MibTableRow
cucsIscsiAuthProfileEntry = _CucsIscsiAuthProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1)
)
cucsIscsiAuthProfileEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-ISCSI-MIB", "cucsIscsiAuthProfileInstanceId"),
)
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileEntry.setStatus("current")
_CucsIscsiAuthProfileInstanceId_Type = CucsManagedObjectId
_CucsIscsiAuthProfileInstanceId_Object = MibTableColumn
cucsIscsiAuthProfileInstanceId = _CucsIscsiAuthProfileInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 1),
    _CucsIscsiAuthProfileInstanceId_Type()
)
cucsIscsiAuthProfileInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileInstanceId.setStatus("current")
_CucsIscsiAuthProfileDn_Type = CucsManagedObjectDn
_CucsIscsiAuthProfileDn_Object = MibTableColumn
cucsIscsiAuthProfileDn = _CucsIscsiAuthProfileDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 2),
    _CucsIscsiAuthProfileDn_Type()
)
cucsIscsiAuthProfileDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileDn.setStatus("current")
_CucsIscsiAuthProfileRn_Type = SnmpAdminString
_CucsIscsiAuthProfileRn_Object = MibTableColumn
cucsIscsiAuthProfileRn = _CucsIscsiAuthProfileRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 3),
    _CucsIscsiAuthProfileRn_Type()
)
cucsIscsiAuthProfileRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileRn.setStatus("current")
_CucsIscsiAuthProfileDescr_Type = SnmpAdminString
_CucsIscsiAuthProfileDescr_Object = MibTableColumn
cucsIscsiAuthProfileDescr = _CucsIscsiAuthProfileDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 4),
    _CucsIscsiAuthProfileDescr_Type()
)
cucsIscsiAuthProfileDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileDescr.setStatus("current")
_CucsIscsiAuthProfileIntId_Type = SnmpAdminString
_CucsIscsiAuthProfileIntId_Object = MibTableColumn
cucsIscsiAuthProfileIntId = _CucsIscsiAuthProfileIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 5),
    _CucsIscsiAuthProfileIntId_Type()
)
cucsIscsiAuthProfileIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileIntId.setStatus("current")
_CucsIscsiAuthProfileName_Type = SnmpAdminString
_CucsIscsiAuthProfileName_Object = MibTableColumn
cucsIscsiAuthProfileName = _CucsIscsiAuthProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 6),
    _CucsIscsiAuthProfileName_Type()
)
cucsIscsiAuthProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileName.setStatus("current")
_CucsIscsiAuthProfilePassword_Type = SnmpAdminString
_CucsIscsiAuthProfilePassword_Object = MibTableColumn
cucsIscsiAuthProfilePassword = _CucsIscsiAuthProfilePassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 7),
    _CucsIscsiAuthProfilePassword_Type()
)
cucsIscsiAuthProfilePassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfilePassword.setStatus("current")
_CucsIscsiAuthProfileUserId_Type = SnmpAdminString
_CucsIscsiAuthProfileUserId_Object = MibTableColumn
cucsIscsiAuthProfileUserId = _CucsIscsiAuthProfileUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 8),
    _CucsIscsiAuthProfileUserId_Type()
)
cucsIscsiAuthProfileUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileUserId.setStatus("current")
_CucsIscsiAuthProfileCtpassword_Type = SnmpAdminString
_CucsIscsiAuthProfileCtpassword_Object = MibTableColumn
cucsIscsiAuthProfileCtpassword = _CucsIscsiAuthProfileCtpassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 9),
    _CucsIscsiAuthProfileCtpassword_Type()
)
cucsIscsiAuthProfileCtpassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfileCtpassword.setStatus("current")
_CucsIscsiAuthProfilePolicyLevel_Type = Gauge32
_CucsIscsiAuthProfilePolicyLevel_Object = MibTableColumn
cucsIscsiAuthProfilePolicyLevel = _CucsIscsiAuthProfilePolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 10),
    _CucsIscsiAuthProfilePolicyLevel_Type()
)
cucsIscsiAuthProfilePolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfilePolicyLevel.setStatus("current")
_CucsIscsiAuthProfilePolicyOwner_Type = CucsPolicyPolicyOwner
_CucsIscsiAuthProfilePolicyOwner_Object = MibTableColumn
cucsIscsiAuthProfilePolicyOwner = _CucsIscsiAuthProfilePolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 60, 1, 1, 11),
    _CucsIscsiAuthProfilePolicyOwner_Type()
)
cucsIscsiAuthProfilePolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsIscsiAuthProfilePolicyOwner.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-ISCSI-MIB",
    **{"cucsIscsiObjects": cucsIscsiObjects,
       "cucsIscsiAuthProfileTable": cucsIscsiAuthProfileTable,
       "cucsIscsiAuthProfileEntry": cucsIscsiAuthProfileEntry,
       "cucsIscsiAuthProfileInstanceId": cucsIscsiAuthProfileInstanceId,
       "cucsIscsiAuthProfileDn": cucsIscsiAuthProfileDn,
       "cucsIscsiAuthProfileRn": cucsIscsiAuthProfileRn,
       "cucsIscsiAuthProfileDescr": cucsIscsiAuthProfileDescr,
       "cucsIscsiAuthProfileIntId": cucsIscsiAuthProfileIntId,
       "cucsIscsiAuthProfileName": cucsIscsiAuthProfileName,
       "cucsIscsiAuthProfilePassword": cucsIscsiAuthProfilePassword,
       "cucsIscsiAuthProfileUserId": cucsIscsiAuthProfileUserId,
       "cucsIscsiAuthProfileCtpassword": cucsIscsiAuthProfileCtpassword,
       "cucsIscsiAuthProfilePolicyLevel": cucsIscsiAuthProfilePolicyLevel,
       "cucsIscsiAuthProfilePolicyOwner": cucsIscsiAuthProfilePolicyOwner}
)
