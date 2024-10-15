# SNMP MIB module (CISCO-IP-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:38 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoIPIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309)
)
ciscoIPIfMIB.setRevisions(
        ("2008-08-08 00:00",
         "2008-07-28 00:00",
         "2002-10-12 00:00",
         "2002-10-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpAddressCatagory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 2),
          ("secondary", 3),
          ("single", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoIPIfMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIPIfMIBNotifs = _CiscoIPIfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 0)
)
_CiiIPIfNotifications_ObjectIdentity = ObjectIdentity
ciiIPIfNotifications = _CiiIPIfNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 0, 0)
)
_CiscoIPIfMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIPIfMIBObjects = _CiscoIPIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1)
)
_CiiIPAddressConfiguration_ObjectIdentity = ObjectIdentity
ciiIPAddressConfiguration = _CiiIPAddressConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1)
)


class _CiiIPAddressCategoryCap_Type(Bits):
    """Custom type ciiIPAddressCategoryCap based on Bits"""
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2),
          ("single", 0))
    )

_CiiIPAddressCategoryCap_Type.__name__ = "Bits"
_CiiIPAddressCategoryCap_Object = MibScalar
ciiIPAddressCategoryCap = _CiiIPAddressCategoryCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 1),
    _CiiIPAddressCategoryCap_Type()
)
ciiIPAddressCategoryCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciiIPAddressCategoryCap.setStatus("current")
_CiiIPAddressTable_Object = MibTable
ciiIPAddressTable = _CiiIPAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciiIPAddressTable.setStatus("current")
_CiiIPAddressEntry_Object = MibTableRow
ciiIPAddressEntry = _CiiIPAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1)
)
ciiIPAddressEntry.setIndexNames(
    (0, "CISCO-IP-IF-MIB", "ciiIPAddressType"),
    (0, "CISCO-IP-IF-MIB", "ciiIPAddress"),
)
if mibBuilder.loadTexts:
    ciiIPAddressEntry.setStatus("current")
_CiiIPAddressType_Type = InetAddressType
_CiiIPAddressType_Object = MibTableColumn
ciiIPAddressType = _CiiIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1, 1),
    _CiiIPAddressType_Type()
)
ciiIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiIPAddressType.setStatus("current")


class _CiiIPAddress_Type(InetAddress):
    """Custom type ciiIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_CiiIPAddress_Type.__name__ = "InetAddress"
_CiiIPAddress_Object = MibTableColumn
ciiIPAddress = _CiiIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1, 2),
    _CiiIPAddress_Type()
)
ciiIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiIPAddress.setStatus("current")
_CiiIPAddressIfIndex_Type = InterfaceIndex
_CiiIPAddressIfIndex_Object = MibTableColumn
ciiIPAddressIfIndex = _CiiIPAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1, 3),
    _CiiIPAddressIfIndex_Type()
)
ciiIPAddressIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPAddressIfIndex.setStatus("current")
_CiiIPAddressPrefixLength_Type = InetAddressPrefixLength
_CiiIPAddressPrefixLength_Object = MibTableColumn
ciiIPAddressPrefixLength = _CiiIPAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1, 4),
    _CiiIPAddressPrefixLength_Type()
)
ciiIPAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPAddressPrefixLength.setStatus("current")
_CiiIPAddressBroadcast_Type = InetAddress
_CiiIPAddressBroadcast_Object = MibTableColumn
ciiIPAddressBroadcast = _CiiIPAddressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1, 5),
    _CiiIPAddressBroadcast_Type()
)
ciiIPAddressBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPAddressBroadcast.setStatus("current")
_CiiIPAddressCategory_Type = IpAddressCatagory
_CiiIPAddressCategory_Object = MibTableColumn
ciiIPAddressCategory = _CiiIPAddressCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1, 6),
    _CiiIPAddressCategory_Type()
)
ciiIPAddressCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPAddressCategory.setStatus("current")
_CiiIPAddressStatus_Type = RowStatus
_CiiIPAddressStatus_Object = MibTableColumn
ciiIPAddressStatus = _CiiIPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 2, 1, 7),
    _CiiIPAddressStatus_Type()
)
ciiIPAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPAddressStatus.setStatus("current")
_CiiIPIfAddressTable_Object = MibTable
ciiIPIfAddressTable = _CiiIPIfAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciiIPIfAddressTable.setStatus("current")
_CiiIPIfAddressEntry_Object = MibTableRow
ciiIPIfAddressEntry = _CiiIPIfAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 3, 1)
)
ciiIPIfAddressEntry.setIndexNames(
    (0, "CISCO-IP-IF-MIB", "ciiIPAddressIfIndex"),
    (0, "CISCO-IP-IF-MIB", "ciiIPAddressType"),
    (0, "CISCO-IP-IF-MIB", "ciiIPAddress"),
)
if mibBuilder.loadTexts:
    ciiIPIfAddressEntry.setStatus("current")
_CiiIPIfAddressPrefixLength_Type = InetAddressPrefixLength
_CiiIPIfAddressPrefixLength_Object = MibTableColumn
ciiIPIfAddressPrefixLength = _CiiIPIfAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 3, 1, 1),
    _CiiIPIfAddressPrefixLength_Type()
)
ciiIPIfAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPIfAddressPrefixLength.setStatus("current")
_CiiIPIfAddressBroadcast_Type = InetAddress
_CiiIPIfAddressBroadcast_Object = MibTableColumn
ciiIPIfAddressBroadcast = _CiiIPIfAddressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 3, 1, 2),
    _CiiIPIfAddressBroadcast_Type()
)
ciiIPIfAddressBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPIfAddressBroadcast.setStatus("current")
_CiiIPIfAddressCategory_Type = IpAddressCatagory
_CiiIPIfAddressCategory_Object = MibTableColumn
ciiIPIfAddressCategory = _CiiIPIfAddressCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 3, 1, 3),
    _CiiIPIfAddressCategory_Type()
)
ciiIPIfAddressCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPIfAddressCategory.setStatus("current")
_CiiIPIfAddressStatus_Type = RowStatus
_CiiIPIfAddressStatus_Object = MibTableColumn
ciiIPIfAddressStatus = _CiiIPIfAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 1, 3, 1, 4),
    _CiiIPIfAddressStatus_Type()
)
ciiIPIfAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiIPIfAddressStatus.setStatus("current")
_CiiHelperAddressConfiguration_ObjectIdentity = ObjectIdentity
ciiHelperAddressConfiguration = _CiiHelperAddressConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2)
)
_CiiHelperAddressTable_Object = MibTable
ciiHelperAddressTable = _CiiHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciiHelperAddressTable.setStatus("current")
_CiiHelperAddressEntry_Object = MibTableRow
ciiHelperAddressEntry = _CiiHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2, 1, 1)
)
ciiHelperAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-IP-IF-MIB", "ciiHelperAddressVrf"),
    (0, "CISCO-IP-IF-MIB", "ciiHelperAddressType"),
    (0, "CISCO-IP-IF-MIB", "ciiHelperAddress"),
)
if mibBuilder.loadTexts:
    ciiHelperAddressEntry.setStatus("current")


class _CiiHelperAddressVrf_Type(SnmpAdminString):
    """Custom type ciiHelperAddressVrf based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CiiHelperAddressVrf_Type.__name__ = "SnmpAdminString"
_CiiHelperAddressVrf_Object = MibTableColumn
ciiHelperAddressVrf = _CiiHelperAddressVrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2, 1, 1, 1),
    _CiiHelperAddressVrf_Type()
)
ciiHelperAddressVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiHelperAddressVrf.setStatus("current")
_CiiHelperAddressType_Type = InetAddressType
_CiiHelperAddressType_Object = MibTableColumn
ciiHelperAddressType = _CiiHelperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2, 1, 1, 2),
    _CiiHelperAddressType_Type()
)
ciiHelperAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiHelperAddressType.setStatus("current")
_CiiHelperAddress_Type = InetAddress
_CiiHelperAddress_Object = MibTableColumn
ciiHelperAddress = _CiiHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2, 1, 1, 3),
    _CiiHelperAddress_Type()
)
ciiHelperAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciiHelperAddress.setStatus("current")
_CiiHelperAddressStatus_Type = RowStatus
_CiiHelperAddressStatus_Object = MibTableColumn
ciiHelperAddressStatus = _CiiHelperAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2, 1, 1, 4),
    _CiiHelperAddressStatus_Type()
)
ciiHelperAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiHelperAddressStatus.setStatus("current")


class _CiiHelperAddressStorage_Type(StorageType):
    """Custom type ciiHelperAddressStorage based on StorageType"""


_CiiHelperAddressStorage_Object = MibTableColumn
ciiHelperAddressStorage = _CiiHelperAddressStorage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 1, 2, 1, 1, 5),
    _CiiHelperAddressStorage_Type()
)
ciiHelperAddressStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciiHelperAddressStorage.setStatus("current")
_CiscoIPIfMIBConform_ObjectIdentity = ObjectIdentity
ciscoIPIfMIBConform = _CiscoIPIfMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2)
)
_CiscoIPIfMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIPIfMIBCompliances = _CiscoIPIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 1)
)
_CiscoIPIfMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIPIfMIBGroups = _CiscoIPIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 2)
)

# Managed Objects groups

ciscoIPIfAddressConfigurationGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 2, 1)
)
ciscoIPIfAddressConfigurationGroup1.setObjects(
      *(("CISCO-IP-IF-MIB", "ciiIPAddressCategoryCap"),
        ("CISCO-IP-IF-MIB", "ciiIPAddressIfIndex"),
        ("CISCO-IP-IF-MIB", "ciiIPAddressPrefixLength"),
        ("CISCO-IP-IF-MIB", "ciiIPAddressCategory"),
        ("CISCO-IP-IF-MIB", "ciiIPAddressStatus"))
)
if mibBuilder.loadTexts:
    ciscoIPIfAddressConfigurationGroup1.setStatus("current")

ciscoIPIfAddressConfigurationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 2, 2)
)
ciscoIPIfAddressConfigurationGroup2.setObjects(
    ("CISCO-IP-IF-MIB", "ciiIPAddressBroadcast")
)
if mibBuilder.loadTexts:
    ciscoIPIfAddressConfigurationGroup2.setStatus("current")

ciscoIPIfAddressConfigurationGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 2, 3)
)
ciscoIPIfAddressConfigurationGroup3.setObjects(
      *(("CISCO-IP-IF-MIB", "ciiIPAddressCategoryCap"),
        ("CISCO-IP-IF-MIB", "ciiIPIfAddressPrefixLength"),
        ("CISCO-IP-IF-MIB", "ciiIPIfAddressCategory"),
        ("CISCO-IP-IF-MIB", "ciiIPIfAddressStatus"))
)
if mibBuilder.loadTexts:
    ciscoIPIfAddressConfigurationGroup3.setStatus("current")

ciscoIPIfAddressConfigurationGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 2, 4)
)
ciscoIPIfAddressConfigurationGroup4.setObjects(
    ("CISCO-IP-IF-MIB", "ciiIPIfAddressBroadcast")
)
if mibBuilder.loadTexts:
    ciscoIPIfAddressConfigurationGroup4.setStatus("current")

ciiHelperAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 2, 5)
)
ciiHelperAddressGroup.setObjects(
      *(("CISCO-IP-IF-MIB", "ciiHelperAddressStatus"),
        ("CISCO-IP-IF-MIB", "ciiHelperAddressStorage"))
)
if mibBuilder.loadTexts:
    ciiHelperAddressGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIPIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIPIfMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIPIfMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIPIfMIBCompliance1.setStatus(
        "deprecated"
    )

ciscoIPIfMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 309, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIPIfMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-IF-MIB",
    **{"IpAddressCatagory": IpAddressCatagory,
       "ciscoIPIfMIB": ciscoIPIfMIB,
       "ciscoIPIfMIBNotifs": ciscoIPIfMIBNotifs,
       "ciiIPIfNotifications": ciiIPIfNotifications,
       "ciscoIPIfMIBObjects": ciscoIPIfMIBObjects,
       "ciiIPAddressConfiguration": ciiIPAddressConfiguration,
       "ciiIPAddressCategoryCap": ciiIPAddressCategoryCap,
       "ciiIPAddressTable": ciiIPAddressTable,
       "ciiIPAddressEntry": ciiIPAddressEntry,
       "ciiIPAddressType": ciiIPAddressType,
       "ciiIPAddress": ciiIPAddress,
       "ciiIPAddressIfIndex": ciiIPAddressIfIndex,
       "ciiIPAddressPrefixLength": ciiIPAddressPrefixLength,
       "ciiIPAddressBroadcast": ciiIPAddressBroadcast,
       "ciiIPAddressCategory": ciiIPAddressCategory,
       "ciiIPAddressStatus": ciiIPAddressStatus,
       "ciiIPIfAddressTable": ciiIPIfAddressTable,
       "ciiIPIfAddressEntry": ciiIPIfAddressEntry,
       "ciiIPIfAddressPrefixLength": ciiIPIfAddressPrefixLength,
       "ciiIPIfAddressBroadcast": ciiIPIfAddressBroadcast,
       "ciiIPIfAddressCategory": ciiIPIfAddressCategory,
       "ciiIPIfAddressStatus": ciiIPIfAddressStatus,
       "ciiHelperAddressConfiguration": ciiHelperAddressConfiguration,
       "ciiHelperAddressTable": ciiHelperAddressTable,
       "ciiHelperAddressEntry": ciiHelperAddressEntry,
       "ciiHelperAddressVrf": ciiHelperAddressVrf,
       "ciiHelperAddressType": ciiHelperAddressType,
       "ciiHelperAddress": ciiHelperAddress,
       "ciiHelperAddressStatus": ciiHelperAddressStatus,
       "ciiHelperAddressStorage": ciiHelperAddressStorage,
       "ciscoIPIfMIBConform": ciscoIPIfMIBConform,
       "ciscoIPIfMIBCompliances": ciscoIPIfMIBCompliances,
       "ciscoIPIfMIBCompliance": ciscoIPIfMIBCompliance,
       "ciscoIPIfMIBCompliance1": ciscoIPIfMIBCompliance1,
       "ciscoIPIfMIBCompliance2": ciscoIPIfMIBCompliance2,
       "ciscoIPIfMIBGroups": ciscoIPIfMIBGroups,
       "ciscoIPIfAddressConfigurationGroup1": ciscoIPIfAddressConfigurationGroup1,
       "ciscoIPIfAddressConfigurationGroup2": ciscoIPIfAddressConfigurationGroup2,
       "ciscoIPIfAddressConfigurationGroup3": ciscoIPIfAddressConfigurationGroup3,
       "ciscoIPIfAddressConfigurationGroup4": ciscoIPIfAddressConfigurationGroup4,
       "ciiHelperAddressGroup": ciiHelperAddressGroup}
)
