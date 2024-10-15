# SNMP MIB module (Unisphere-Data-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:31 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable")


# MODULE-IDENTITY

usdDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47)
)
usdDnsMIB.setRevisions(
        ("2001-03-22 19:29",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdNextServerListIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ServerListIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class UsdNextLocalDomainNameListIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class LocalDomainNameListIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class LocalDomainName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_UsdDnsObjects_ObjectIdentity = ObjectIdentity
usdDnsObjects = _UsdDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1)
)
_UsdDnsGeneral_ObjectIdentity = ObjectIdentity
usdDnsGeneral = _UsdDnsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1)
)
_UsdDnsEnable_Type = UsdEnable
_UsdDnsEnable_Object = MibScalar
usdDnsEnable = _UsdDnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1, 1),
    _UsdDnsEnable_Type()
)
usdDnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdDnsEnable.setStatus("current")
_UsdDnsServerList_ObjectIdentity = ObjectIdentity
usdDnsServerList = _UsdDnsServerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2)
)
_UsdDnsServerListNextIndex_Type = UsdNextServerListIndex
_UsdDnsServerListNextIndex_Object = MibScalar
usdDnsServerListNextIndex = _UsdDnsServerListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 1),
    _UsdDnsServerListNextIndex_Type()
)
usdDnsServerListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDnsServerListNextIndex.setStatus("current")
_UsdDnsServerListTable_Object = MibTable
usdDnsServerListTable = _UsdDnsServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdDnsServerListTable.setStatus("current")
_UsdDnsServerListEntry_Object = MibTableRow
usdDnsServerListEntry = _UsdDnsServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1)
)
usdDnsServerListEntry.setIndexNames(
    (0, "Unisphere-Data-DNS-MIB", "usdDnsServerListIndex"),
)
if mibBuilder.loadTexts:
    usdDnsServerListEntry.setStatus("current")
_UsdDnsServerListIndex_Type = ServerListIndex
_UsdDnsServerListIndex_Object = MibTableColumn
usdDnsServerListIndex = _UsdDnsServerListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 1),
    _UsdDnsServerListIndex_Type()
)
usdDnsServerListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDnsServerListIndex.setStatus("current")
_UsdDnsServerListAddress_Type = IpAddress
_UsdDnsServerListAddress_Object = MibTableColumn
usdDnsServerListAddress = _UsdDnsServerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 2),
    _UsdDnsServerListAddress_Type()
)
usdDnsServerListAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDnsServerListAddress.setStatus("current")
_UsdDnsServerListRowStatus_Type = RowStatus
_UsdDnsServerListRowStatus_Object = MibTableColumn
usdDnsServerListRowStatus = _UsdDnsServerListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 3),
    _UsdDnsServerListRowStatus_Type()
)
usdDnsServerListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDnsServerListRowStatus.setStatus("current")
_UsdDnsLocalDomainNameList_ObjectIdentity = ObjectIdentity
usdDnsLocalDomainNameList = _UsdDnsLocalDomainNameList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3)
)
_UsdDnsLocalDomainNameListNextIndex_Type = UsdNextLocalDomainNameListIndex
_UsdDnsLocalDomainNameListNextIndex_Object = MibScalar
usdDnsLocalDomainNameListNextIndex = _UsdDnsLocalDomainNameListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 1),
    _UsdDnsLocalDomainNameListNextIndex_Type()
)
usdDnsLocalDomainNameListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdDnsLocalDomainNameListNextIndex.setStatus("current")
_UsdDnsLocalDomainNameListTable_Object = MibTable
usdDnsLocalDomainNameListTable = _UsdDnsLocalDomainNameListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdDnsLocalDomainNameListTable.setStatus("current")
_UsdDnsLocalDomainNameListEntry_Object = MibTableRow
usdDnsLocalDomainNameListEntry = _UsdDnsLocalDomainNameListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1)
)
usdDnsLocalDomainNameListEntry.setIndexNames(
    (0, "Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListIndex"),
)
if mibBuilder.loadTexts:
    usdDnsLocalDomainNameListEntry.setStatus("current")
_UsdDnsLocalDomainNameListIndex_Type = LocalDomainNameListIndex
_UsdDnsLocalDomainNameListIndex_Object = MibTableColumn
usdDnsLocalDomainNameListIndex = _UsdDnsLocalDomainNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 1),
    _UsdDnsLocalDomainNameListIndex_Type()
)
usdDnsLocalDomainNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdDnsLocalDomainNameListIndex.setStatus("current")
_UsdDnsLocalDomainNameListName_Type = LocalDomainName
_UsdDnsLocalDomainNameListName_Object = MibTableColumn
usdDnsLocalDomainNameListName = _UsdDnsLocalDomainNameListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 2),
    _UsdDnsLocalDomainNameListName_Type()
)
usdDnsLocalDomainNameListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDnsLocalDomainNameListName.setStatus("current")
_UsdDnsLocalDomainNameListRowStatus_Type = RowStatus
_UsdDnsLocalDomainNameListRowStatus_Object = MibTableColumn
usdDnsLocalDomainNameListRowStatus = _UsdDnsLocalDomainNameListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 3),
    _UsdDnsLocalDomainNameListRowStatus_Type()
)
usdDnsLocalDomainNameListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdDnsLocalDomainNameListRowStatus.setStatus("current")
_UsdDnsConformance_ObjectIdentity = ObjectIdentity
usdDnsConformance = _UsdDnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2)
)
_UsdDnsCompliances_ObjectIdentity = ObjectIdentity
usdDnsCompliances = _UsdDnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1)
)
_UsdDnsGroups_ObjectIdentity = ObjectIdentity
usdDnsGroups = _UsdDnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2)
)

# Managed Objects groups

usdDnsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 1)
)
usdDnsEnableGroup.setObjects(
    ("Unisphere-Data-DNS-MIB", "usdDnsEnable")
)
if mibBuilder.loadTexts:
    usdDnsEnableGroup.setStatus("current")

usdDnsServerListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 2)
)
usdDnsServerListGroup.setObjects(
      *(("Unisphere-Data-DNS-MIB", "usdDnsServerListNextIndex"),
        ("Unisphere-Data-DNS-MIB", "usdDnsServerListAddress"),
        ("Unisphere-Data-DNS-MIB", "usdDnsServerListRowStatus"))
)
if mibBuilder.loadTexts:
    usdDnsServerListGroup.setStatus("current")

usdDnsLocalDomainNameListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 3)
)
usdDnsLocalDomainNameListGroup.setObjects(
      *(("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListNextIndex"),
        ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListName"),
        ("Unisphere-Data-DNS-MIB", "usdDnsLocalDomainNameListRowStatus"))
)
if mibBuilder.loadTexts:
    usdDnsLocalDomainNameListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdDnsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdDnsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-DNS-MIB",
    **{"UsdNextServerListIndex": UsdNextServerListIndex,
       "ServerListIndex": ServerListIndex,
       "UsdNextLocalDomainNameListIndex": UsdNextLocalDomainNameListIndex,
       "LocalDomainNameListIndex": LocalDomainNameListIndex,
       "LocalDomainName": LocalDomainName,
       "usdDnsMIB": usdDnsMIB,
       "usdDnsObjects": usdDnsObjects,
       "usdDnsGeneral": usdDnsGeneral,
       "usdDnsEnable": usdDnsEnable,
       "usdDnsServerList": usdDnsServerList,
       "usdDnsServerListNextIndex": usdDnsServerListNextIndex,
       "usdDnsServerListTable": usdDnsServerListTable,
       "usdDnsServerListEntry": usdDnsServerListEntry,
       "usdDnsServerListIndex": usdDnsServerListIndex,
       "usdDnsServerListAddress": usdDnsServerListAddress,
       "usdDnsServerListRowStatus": usdDnsServerListRowStatus,
       "usdDnsLocalDomainNameList": usdDnsLocalDomainNameList,
       "usdDnsLocalDomainNameListNextIndex": usdDnsLocalDomainNameListNextIndex,
       "usdDnsLocalDomainNameListTable": usdDnsLocalDomainNameListTable,
       "usdDnsLocalDomainNameListEntry": usdDnsLocalDomainNameListEntry,
       "usdDnsLocalDomainNameListIndex": usdDnsLocalDomainNameListIndex,
       "usdDnsLocalDomainNameListName": usdDnsLocalDomainNameListName,
       "usdDnsLocalDomainNameListRowStatus": usdDnsLocalDomainNameListRowStatus,
       "usdDnsConformance": usdDnsConformance,
       "usdDnsCompliances": usdDnsCompliances,
       "usdDnsCompliance": usdDnsCompliance,
       "usdDnsGroups": usdDnsGroups,
       "usdDnsEnableGroup": usdDnsEnableGroup,
       "usdDnsServerListGroup": usdDnsServerListGroup,
       "usdDnsLocalDomainNameListGroup": usdDnsLocalDomainNameListGroup}
)
