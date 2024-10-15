# SNMP MIB module (CISCO-WDS-IDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WDS-IDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:32 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 MacAddress,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoWdsIdsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 457)
)
ciscoWdsIdsMIB.setRevisions(
        ("2004-10-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWdsIdsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWdsIdsMIBObjects = _CiscoWdsIdsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1)
)
_CiscoWdsIdsMacSpoofing_ObjectIdentity = ObjectIdentity
ciscoWdsIdsMacSpoofing = _CiscoWdsIdsMacSpoofing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1)
)


class _CiscoWdsIdsMaxMacAddresses_Type(Integer32):
    """Custom type ciscoWdsIdsMaxMacAddresses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoWdsIdsMaxMacAddresses_Type.__name__ = "Integer32"
_CiscoWdsIdsMaxMacAddresses_Object = MibScalar
ciscoWdsIdsMaxMacAddresses = _CiscoWdsIdsMaxMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 1),
    _CiscoWdsIdsMaxMacAddresses_Type()
)
ciscoWdsIdsMaxMacAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoWdsIdsMaxMacAddresses.setStatus("current")


class _CiscoWdsIdsMaxEntriesPerMac_Type(Integer32):
    """Custom type ciscoWdsIdsMaxEntriesPerMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoWdsIdsMaxEntriesPerMac_Type.__name__ = "Integer32"
_CiscoWdsIdsMaxEntriesPerMac_Object = MibScalar
ciscoWdsIdsMaxEntriesPerMac = _CiscoWdsIdsMaxEntriesPerMac_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 2),
    _CiscoWdsIdsMaxEntriesPerMac_Type()
)
ciscoWdsIdsMaxEntriesPerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoWdsIdsMaxEntriesPerMac.setStatus("current")
_CiscoWdsIdsMacSpoofTable_Object = MibTable
ciscoWdsIdsMacSpoofTable = _CiscoWdsIdsMacSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofTable.setStatus("current")
_CiscoWdsIdsMacSpoofEntry_Object = MibTableRow
ciscoWdsIdsMacSpoofEntry = _CiscoWdsIdsMacSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 3, 1)
)
ciscoWdsIdsMacSpoofEntry.setIndexNames(
    (0, "CISCO-WDS-IDS-MIB", "ciscoWdsIdsMacSpoofStaMacAddress"),
    (0, "CISCO-WDS-IDS-MIB", "ciscoWdsIdsMacSpoofIndex"),
)
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofEntry.setStatus("current")
_CiscoWdsIdsMacSpoofStaMacAddress_Type = MacAddress
_CiscoWdsIdsMacSpoofStaMacAddress_Object = MibTableColumn
ciscoWdsIdsMacSpoofStaMacAddress = _CiscoWdsIdsMacSpoofStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 3, 1, 1),
    _CiscoWdsIdsMacSpoofStaMacAddress_Type()
)
ciscoWdsIdsMacSpoofStaMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofStaMacAddress.setStatus("current")
_CiscoWdsIdsMacSpoofIndex_Type = Unsigned32
_CiscoWdsIdsMacSpoofIndex_Object = MibTableColumn
ciscoWdsIdsMacSpoofIndex = _CiscoWdsIdsMacSpoofIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 3, 1, 2),
    _CiscoWdsIdsMacSpoofIndex_Type()
)
ciscoWdsIdsMacSpoofIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofIndex.setStatus("current")
_CiscoWdsIdsMacSpoofClient_Type = MacAddress
_CiscoWdsIdsMacSpoofClient_Object = MibTableColumn
ciscoWdsIdsMacSpoofClient = _CiscoWdsIdsMacSpoofClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 3, 1, 3),
    _CiscoWdsIdsMacSpoofClient_Type()
)
ciscoWdsIdsMacSpoofClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofClient.setStatus("current")


class _CiscoWdsIdsMacSpoofUserId_Type(SnmpAdminString):
    """Custom type ciscoWdsIdsMacSpoofUserId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 253),
    )


_CiscoWdsIdsMacSpoofUserId_Type.__name__ = "SnmpAdminString"
_CiscoWdsIdsMacSpoofUserId_Object = MibTableColumn
ciscoWdsIdsMacSpoofUserId = _CiscoWdsIdsMacSpoofUserId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 3, 1, 4),
    _CiscoWdsIdsMacSpoofUserId_Type()
)
ciscoWdsIdsMacSpoofUserId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofUserId.setStatus("current")
_CiscoWdsIdsMacSpoofDetectTime_Type = TimeStamp
_CiscoWdsIdsMacSpoofDetectTime_Object = MibTableColumn
ciscoWdsIdsMacSpoofDetectTime = _CiscoWdsIdsMacSpoofDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 1, 1, 3, 1, 5),
    _CiscoWdsIdsMacSpoofDetectTime_Type()
)
ciscoWdsIdsMacSpoofDetectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofDetectTime.setStatus("current")
_CiscoWdsIdsMIBConform_ObjectIdentity = ObjectIdentity
ciscoWdsIdsMIBConform = _CiscoWdsIdsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 2)
)
_CiscoWdsIdsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWdsIdsMIBCompliances = _CiscoWdsIdsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 2, 1)
)
_CiscoWdsIdsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWdsIdsMIBGroups = _CiscoWdsIdsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 2, 2)
)

# Managed Objects groups

ciscoWdsIdsMacSpoofingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 2, 2, 1)
)
ciscoWdsIdsMacSpoofingGroup.setObjects(
      *(("CISCO-WDS-IDS-MIB", "ciscoWdsIdsMaxMacAddresses"),
        ("CISCO-WDS-IDS-MIB", "ciscoWdsIdsMaxEntriesPerMac"),
        ("CISCO-WDS-IDS-MIB", "ciscoWdsIdsMacSpoofClient"),
        ("CISCO-WDS-IDS-MIB", "ciscoWdsIdsMacSpoofUserId"),
        ("CISCO-WDS-IDS-MIB", "ciscoWdsIdsMacSpoofDetectTime"))
)
if mibBuilder.loadTexts:
    ciscoWdsIdsMacSpoofingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWdsIdsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 457, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWdsIdsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WDS-IDS-MIB",
    **{"ciscoWdsIdsMIB": ciscoWdsIdsMIB,
       "ciscoWdsIdsMIBObjects": ciscoWdsIdsMIBObjects,
       "ciscoWdsIdsMacSpoofing": ciscoWdsIdsMacSpoofing,
       "ciscoWdsIdsMaxMacAddresses": ciscoWdsIdsMaxMacAddresses,
       "ciscoWdsIdsMaxEntriesPerMac": ciscoWdsIdsMaxEntriesPerMac,
       "ciscoWdsIdsMacSpoofTable": ciscoWdsIdsMacSpoofTable,
       "ciscoWdsIdsMacSpoofEntry": ciscoWdsIdsMacSpoofEntry,
       "ciscoWdsIdsMacSpoofStaMacAddress": ciscoWdsIdsMacSpoofStaMacAddress,
       "ciscoWdsIdsMacSpoofIndex": ciscoWdsIdsMacSpoofIndex,
       "ciscoWdsIdsMacSpoofClient": ciscoWdsIdsMacSpoofClient,
       "ciscoWdsIdsMacSpoofUserId": ciscoWdsIdsMacSpoofUserId,
       "ciscoWdsIdsMacSpoofDetectTime": ciscoWdsIdsMacSpoofDetectTime,
       "ciscoWdsIdsMIBConform": ciscoWdsIdsMIBConform,
       "ciscoWdsIdsMIBCompliances": ciscoWdsIdsMIBCompliances,
       "ciscoWdsIdsMIBCompliance": ciscoWdsIdsMIBCompliance,
       "ciscoWdsIdsMIBGroups": ciscoWdsIdsMIBGroups,
       "ciscoWdsIdsMacSpoofingGroup": ciscoWdsIdsMacSpoofingGroup}
)
