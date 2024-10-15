# SNMP MIB module (CISCO-UNIFIED-COMPUTING-HOSTIMG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-HOSTIMG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:39 2024
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

(CucsHostimgComposition,
 CucsHostimgDistribution,
 CucsHostimgImgType,
 CucsHostimgType,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsHostimgComposition",
    "CucsHostimgDistribution",
    "CucsHostimgImgType",
    "CucsHostimgType",
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

cucsHostimgObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsHostimgPolicyTable_Object = MibTable
cucsHostimgPolicyTable = _CucsHostimgPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1)
)
if mibBuilder.loadTexts:
    cucsHostimgPolicyTable.setStatus("current")
_CucsHostimgPolicyEntry_Object = MibTableRow
cucsHostimgPolicyEntry = _CucsHostimgPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1)
)
cucsHostimgPolicyEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-HOSTIMG-MIB", "cucsHostimgPolicyInstanceId"),
)
if mibBuilder.loadTexts:
    cucsHostimgPolicyEntry.setStatus("current")
_CucsHostimgPolicyInstanceId_Type = CucsManagedObjectId
_CucsHostimgPolicyInstanceId_Object = MibTableColumn
cucsHostimgPolicyInstanceId = _CucsHostimgPolicyInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 1),
    _CucsHostimgPolicyInstanceId_Type()
)
cucsHostimgPolicyInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsHostimgPolicyInstanceId.setStatus("current")
_CucsHostimgPolicyDn_Type = CucsManagedObjectDn
_CucsHostimgPolicyDn_Object = MibTableColumn
cucsHostimgPolicyDn = _CucsHostimgPolicyDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 2),
    _CucsHostimgPolicyDn_Type()
)
cucsHostimgPolicyDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyDn.setStatus("current")
_CucsHostimgPolicyRn_Type = SnmpAdminString
_CucsHostimgPolicyRn_Object = MibTableColumn
cucsHostimgPolicyRn = _CucsHostimgPolicyRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 3),
    _CucsHostimgPolicyRn_Type()
)
cucsHostimgPolicyRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyRn.setStatus("current")
_CucsHostimgPolicyComp_Type = CucsHostimgComposition
_CucsHostimgPolicyComp_Object = MibTableColumn
cucsHostimgPolicyComp = _CucsHostimgPolicyComp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 4),
    _CucsHostimgPolicyComp_Type()
)
cucsHostimgPolicyComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyComp.setStatus("current")
_CucsHostimgPolicyDescr_Type = SnmpAdminString
_CucsHostimgPolicyDescr_Object = MibTableColumn
cucsHostimgPolicyDescr = _CucsHostimgPolicyDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 5),
    _CucsHostimgPolicyDescr_Type()
)
cucsHostimgPolicyDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyDescr.setStatus("current")
_CucsHostimgPolicyIntId_Type = SnmpAdminString
_CucsHostimgPolicyIntId_Object = MibTableColumn
cucsHostimgPolicyIntId = _CucsHostimgPolicyIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 6),
    _CucsHostimgPolicyIntId_Type()
)
cucsHostimgPolicyIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyIntId.setStatus("current")
_CucsHostimgPolicyName_Type = SnmpAdminString
_CucsHostimgPolicyName_Object = MibTableColumn
cucsHostimgPolicyName = _CucsHostimgPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 7),
    _CucsHostimgPolicyName_Type()
)
cucsHostimgPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyName.setStatus("current")
_CucsHostimgPolicyConf_Type = SnmpAdminString
_CucsHostimgPolicyConf_Object = MibTableColumn
cucsHostimgPolicyConf = _CucsHostimgPolicyConf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 8),
    _CucsHostimgPolicyConf_Type()
)
cucsHostimgPolicyConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyConf.setStatus("current")
_CucsHostimgPolicyDistro_Type = CucsHostimgDistribution
_CucsHostimgPolicyDistro_Object = MibTableColumn
cucsHostimgPolicyDistro = _CucsHostimgPolicyDistro_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 9),
    _CucsHostimgPolicyDistro_Type()
)
cucsHostimgPolicyDistro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyDistro.setStatus("current")
_CucsHostimgPolicyType_Type = CucsHostimgImgType
_CucsHostimgPolicyType_Object = MibTableColumn
cucsHostimgPolicyType = _CucsHostimgPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 10),
    _CucsHostimgPolicyType_Type()
)
cucsHostimgPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyType.setStatus("current")
_CucsHostimgPolicyPolicyLevel_Type = Gauge32
_CucsHostimgPolicyPolicyLevel_Object = MibTableColumn
cucsHostimgPolicyPolicyLevel = _CucsHostimgPolicyPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 11),
    _CucsHostimgPolicyPolicyLevel_Type()
)
cucsHostimgPolicyPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyPolicyLevel.setStatus("current")
_CucsHostimgPolicyPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsHostimgPolicyPolicyOwner_Object = MibTableColumn
cucsHostimgPolicyPolicyOwner = _CucsHostimgPolicyPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 1, 1, 12),
    _CucsHostimgPolicyPolicyOwner_Type()
)
cucsHostimgPolicyPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgPolicyPolicyOwner.setStatus("current")
_CucsHostimgTargetTable_Object = MibTable
cucsHostimgTargetTable = _CucsHostimgTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2)
)
if mibBuilder.loadTexts:
    cucsHostimgTargetTable.setStatus("current")
_CucsHostimgTargetEntry_Object = MibTableRow
cucsHostimgTargetEntry = _CucsHostimgTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1)
)
cucsHostimgTargetEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-HOSTIMG-MIB", "cucsHostimgTargetInstanceId"),
)
if mibBuilder.loadTexts:
    cucsHostimgTargetEntry.setStatus("current")
_CucsHostimgTargetInstanceId_Type = CucsManagedObjectId
_CucsHostimgTargetInstanceId_Object = MibTableColumn
cucsHostimgTargetInstanceId = _CucsHostimgTargetInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1, 1),
    _CucsHostimgTargetInstanceId_Type()
)
cucsHostimgTargetInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsHostimgTargetInstanceId.setStatus("current")
_CucsHostimgTargetDn_Type = CucsManagedObjectDn
_CucsHostimgTargetDn_Object = MibTableColumn
cucsHostimgTargetDn = _CucsHostimgTargetDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1, 2),
    _CucsHostimgTargetDn_Type()
)
cucsHostimgTargetDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgTargetDn.setStatus("current")
_CucsHostimgTargetRn_Type = SnmpAdminString
_CucsHostimgTargetRn_Object = MibTableColumn
cucsHostimgTargetRn = _CucsHostimgTargetRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1, 3),
    _CucsHostimgTargetRn_Type()
)
cucsHostimgTargetRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgTargetRn.setStatus("current")
_CucsHostimgTargetName_Type = SnmpAdminString
_CucsHostimgTargetName_Object = MibTableColumn
cucsHostimgTargetName = _CucsHostimgTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1, 4),
    _CucsHostimgTargetName_Type()
)
cucsHostimgTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgTargetName.setStatus("current")
_CucsHostimgTargetType_Type = CucsHostimgType
_CucsHostimgTargetType_Object = MibTableColumn
cucsHostimgTargetType = _CucsHostimgTargetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1, 5),
    _CucsHostimgTargetType_Type()
)
cucsHostimgTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgTargetType.setStatus("current")
_CucsHostimgTargetUri_Type = SnmpAdminString
_CucsHostimgTargetUri_Object = MibTableColumn
cucsHostimgTargetUri = _CucsHostimgTargetUri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1, 6),
    _CucsHostimgTargetUri_Type()
)
cucsHostimgTargetUri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgTargetUri.setStatus("current")
_CucsHostimgTargetOrder_Type = Gauge32
_CucsHostimgTargetOrder_Object = MibTableColumn
cucsHostimgTargetOrder = _CucsHostimgTargetOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 54, 2, 1, 7),
    _CucsHostimgTargetOrder_Type()
)
cucsHostimgTargetOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsHostimgTargetOrder.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-HOSTIMG-MIB",
    **{"cucsHostimgObjects": cucsHostimgObjects,
       "cucsHostimgPolicyTable": cucsHostimgPolicyTable,
       "cucsHostimgPolicyEntry": cucsHostimgPolicyEntry,
       "cucsHostimgPolicyInstanceId": cucsHostimgPolicyInstanceId,
       "cucsHostimgPolicyDn": cucsHostimgPolicyDn,
       "cucsHostimgPolicyRn": cucsHostimgPolicyRn,
       "cucsHostimgPolicyComp": cucsHostimgPolicyComp,
       "cucsHostimgPolicyDescr": cucsHostimgPolicyDescr,
       "cucsHostimgPolicyIntId": cucsHostimgPolicyIntId,
       "cucsHostimgPolicyName": cucsHostimgPolicyName,
       "cucsHostimgPolicyConf": cucsHostimgPolicyConf,
       "cucsHostimgPolicyDistro": cucsHostimgPolicyDistro,
       "cucsHostimgPolicyType": cucsHostimgPolicyType,
       "cucsHostimgPolicyPolicyLevel": cucsHostimgPolicyPolicyLevel,
       "cucsHostimgPolicyPolicyOwner": cucsHostimgPolicyPolicyOwner,
       "cucsHostimgTargetTable": cucsHostimgTargetTable,
       "cucsHostimgTargetEntry": cucsHostimgTargetEntry,
       "cucsHostimgTargetInstanceId": cucsHostimgTargetInstanceId,
       "cucsHostimgTargetDn": cucsHostimgTargetDn,
       "cucsHostimgTargetRn": cucsHostimgTargetRn,
       "cucsHostimgTargetName": cucsHostimgTargetName,
       "cucsHostimgTargetType": cucsHostimgTargetType,
       "cucsHostimgTargetUri": cucsHostimgTargetUri,
       "cucsHostimgTargetOrder": cucsHostimgTargetOrder}
)
