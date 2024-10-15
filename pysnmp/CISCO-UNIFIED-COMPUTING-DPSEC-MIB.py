# SNMP MIB module (CISCO-UNIFIED-COMPUTING-DPSEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-DPSEC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:10:18 2024
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

(CucsDpsecForgedTransmit,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsDpsecForgedTransmit",
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

cucsDpsecObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsDpsecMacTable_Object = MibTable
cucsDpsecMacTable = _CucsDpsecMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cucsDpsecMacTable.setStatus("current")
_CucsDpsecMacEntry_Object = MibTableRow
cucsDpsecMacEntry = _CucsDpsecMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1)
)
cucsDpsecMacEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-DPSEC-MIB", "cucsDpsecMacInstanceId"),
)
if mibBuilder.loadTexts:
    cucsDpsecMacEntry.setStatus("current")
_CucsDpsecMacInstanceId_Type = CucsManagedObjectId
_CucsDpsecMacInstanceId_Object = MibTableColumn
cucsDpsecMacInstanceId = _CucsDpsecMacInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 1),
    _CucsDpsecMacInstanceId_Type()
)
cucsDpsecMacInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsDpsecMacInstanceId.setStatus("current")
_CucsDpsecMacDn_Type = CucsManagedObjectDn
_CucsDpsecMacDn_Object = MibTableColumn
cucsDpsecMacDn = _CucsDpsecMacDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 2),
    _CucsDpsecMacDn_Type()
)
cucsDpsecMacDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacDn.setStatus("current")
_CucsDpsecMacRn_Type = SnmpAdminString
_CucsDpsecMacRn_Object = MibTableColumn
cucsDpsecMacRn = _CucsDpsecMacRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 3),
    _CucsDpsecMacRn_Type()
)
cucsDpsecMacRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacRn.setStatus("current")
_CucsDpsecMacDescr_Type = SnmpAdminString
_CucsDpsecMacDescr_Object = MibTableColumn
cucsDpsecMacDescr = _CucsDpsecMacDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 4),
    _CucsDpsecMacDescr_Type()
)
cucsDpsecMacDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacDescr.setStatus("current")
_CucsDpsecMacForge_Type = CucsDpsecForgedTransmit
_CucsDpsecMacForge_Object = MibTableColumn
cucsDpsecMacForge = _CucsDpsecMacForge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 5),
    _CucsDpsecMacForge_Type()
)
cucsDpsecMacForge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacForge.setStatus("current")
_CucsDpsecMacIntId_Type = SnmpAdminString
_CucsDpsecMacIntId_Object = MibTableColumn
cucsDpsecMacIntId = _CucsDpsecMacIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 6),
    _CucsDpsecMacIntId_Type()
)
cucsDpsecMacIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacIntId.setStatus("current")
_CucsDpsecMacName_Type = SnmpAdminString
_CucsDpsecMacName_Object = MibTableColumn
cucsDpsecMacName = _CucsDpsecMacName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 7),
    _CucsDpsecMacName_Type()
)
cucsDpsecMacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacName.setStatus("current")
_CucsDpsecMacPolicyLevel_Type = Gauge32
_CucsDpsecMacPolicyLevel_Object = MibTableColumn
cucsDpsecMacPolicyLevel = _CucsDpsecMacPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 8),
    _CucsDpsecMacPolicyLevel_Type()
)
cucsDpsecMacPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacPolicyLevel.setStatus("current")
_CucsDpsecMacPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsDpsecMacPolicyOwner_Object = MibTableColumn
cucsDpsecMacPolicyOwner = _CucsDpsecMacPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 9),
    _CucsDpsecMacPolicyOwner_Type()
)
cucsDpsecMacPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacPolicyOwner.setStatus("current")
_CucsDpsecMacPropAcl_Type = Unsigned64
_CucsDpsecMacPropAcl_Object = MibTableColumn
cucsDpsecMacPropAcl = _CucsDpsecMacPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 13, 1, 1, 10),
    _CucsDpsecMacPropAcl_Type()
)
cucsDpsecMacPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsDpsecMacPropAcl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-DPSEC-MIB",
    **{"cucsDpsecObjects": cucsDpsecObjects,
       "cucsDpsecMacTable": cucsDpsecMacTable,
       "cucsDpsecMacEntry": cucsDpsecMacEntry,
       "cucsDpsecMacInstanceId": cucsDpsecMacInstanceId,
       "cucsDpsecMacDn": cucsDpsecMacDn,
       "cucsDpsecMacRn": cucsDpsecMacRn,
       "cucsDpsecMacDescr": cucsDpsecMacDescr,
       "cucsDpsecMacForge": cucsDpsecMacForge,
       "cucsDpsecMacIntId": cucsDpsecMacIntId,
       "cucsDpsecMacName": cucsDpsecMacName,
       "cucsDpsecMacPolicyLevel": cucsDpsecMacPolicyLevel,
       "cucsDpsecMacPolicyOwner": cucsDpsecMacPolicyOwner,
       "cucsDpsecMacPropAcl": cucsDpsecMacPropAcl}
)
