# SNMP MIB module (Juniper-DNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-DNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:00 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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


# MODULE-IDENTITY

juniDnsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47)
)
juniDnsMIB.setRevisions(
        ("2006-09-15 08:32",
         "2003-09-11 15:50",
         "2002-09-16 21:44",
         "2001-03-22 19:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniNextServerListIndex(Integer32, TextualConvention):
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



class JuniNextLocalDomainNameListIndex(Integer32, TextualConvention):
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
    displayHint = "1025a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1025),
    )



# MIB Managed Objects in the order of their OIDs

_JuniDnsObjects_ObjectIdentity = ObjectIdentity
juniDnsObjects = _JuniDnsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1)
)
_JuniDnsGeneral_ObjectIdentity = ObjectIdentity
juniDnsGeneral = _JuniDnsGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1)
)
_JuniDnsEnable_Type = JuniEnable
_JuniDnsEnable_Object = MibScalar
juniDnsEnable = _JuniDnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 1, 1),
    _JuniDnsEnable_Type()
)
juniDnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniDnsEnable.setStatus("current")
_JuniDnsServerList_ObjectIdentity = ObjectIdentity
juniDnsServerList = _JuniDnsServerList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2)
)
_JuniDnsServerListNextIndex_Type = JuniNextServerListIndex
_JuniDnsServerListNextIndex_Object = MibScalar
juniDnsServerListNextIndex = _JuniDnsServerListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 1),
    _JuniDnsServerListNextIndex_Type()
)
juniDnsServerListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDnsServerListNextIndex.setStatus("current")
_JuniDnsServerListTable_Object = MibTable
juniDnsServerListTable = _JuniDnsServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniDnsServerListTable.setStatus("current")
_JuniDnsServerListEntry_Object = MibTableRow
juniDnsServerListEntry = _JuniDnsServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1)
)
juniDnsServerListEntry.setIndexNames(
    (0, "Juniper-DNS-MIB", "juniDnsServerListIndex"),
)
if mibBuilder.loadTexts:
    juniDnsServerListEntry.setStatus("current")
_JuniDnsServerListIndex_Type = ServerListIndex
_JuniDnsServerListIndex_Object = MibTableColumn
juniDnsServerListIndex = _JuniDnsServerListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 1),
    _JuniDnsServerListIndex_Type()
)
juniDnsServerListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDnsServerListIndex.setStatus("current")
_JuniDnsServerListAddress_Type = IpAddress
_JuniDnsServerListAddress_Object = MibTableColumn
juniDnsServerListAddress = _JuniDnsServerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 2),
    _JuniDnsServerListAddress_Type()
)
juniDnsServerListAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDnsServerListAddress.setStatus("obsolete")
_JuniDnsServerListRowStatus_Type = RowStatus
_JuniDnsServerListRowStatus_Object = MibTableColumn
juniDnsServerListRowStatus = _JuniDnsServerListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 3),
    _JuniDnsServerListRowStatus_Type()
)
juniDnsServerListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDnsServerListRowStatus.setStatus("current")
_JuniDnsV4V6ServerListAddressType_Type = InetAddressType
_JuniDnsV4V6ServerListAddressType_Object = MibTableColumn
juniDnsV4V6ServerListAddressType = _JuniDnsV4V6ServerListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 4),
    _JuniDnsV4V6ServerListAddressType_Type()
)
juniDnsV4V6ServerListAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDnsV4V6ServerListAddressType.setStatus("current")
_JuniDnsV4V6ServerListAddress_Type = InetAddress
_JuniDnsV4V6ServerListAddress_Object = MibTableColumn
juniDnsV4V6ServerListAddress = _JuniDnsV4V6ServerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 2, 2, 1, 5),
    _JuniDnsV4V6ServerListAddress_Type()
)
juniDnsV4V6ServerListAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDnsV4V6ServerListAddress.setStatus("current")
_JuniDnsLocalDomainNameList_ObjectIdentity = ObjectIdentity
juniDnsLocalDomainNameList = _JuniDnsLocalDomainNameList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3)
)
_JuniDnsLocalDomainNameListNextIndex_Type = JuniNextLocalDomainNameListIndex
_JuniDnsLocalDomainNameListNextIndex_Object = MibScalar
juniDnsLocalDomainNameListNextIndex = _JuniDnsLocalDomainNameListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 1),
    _JuniDnsLocalDomainNameListNextIndex_Type()
)
juniDnsLocalDomainNameListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniDnsLocalDomainNameListNextIndex.setStatus("current")
_JuniDnsLocalDomainNameListTable_Object = MibTable
juniDnsLocalDomainNameListTable = _JuniDnsLocalDomainNameListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniDnsLocalDomainNameListTable.setStatus("current")
_JuniDnsLocalDomainNameListEntry_Object = MibTableRow
juniDnsLocalDomainNameListEntry = _JuniDnsLocalDomainNameListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1)
)
juniDnsLocalDomainNameListEntry.setIndexNames(
    (0, "Juniper-DNS-MIB", "juniDnsLocalDomainNameListIndex"),
)
if mibBuilder.loadTexts:
    juniDnsLocalDomainNameListEntry.setStatus("current")
_JuniDnsLocalDomainNameListIndex_Type = LocalDomainNameListIndex
_JuniDnsLocalDomainNameListIndex_Object = MibTableColumn
juniDnsLocalDomainNameListIndex = _JuniDnsLocalDomainNameListIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 1),
    _JuniDnsLocalDomainNameListIndex_Type()
)
juniDnsLocalDomainNameListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniDnsLocalDomainNameListIndex.setStatus("current")
_JuniDnsLocalDomainNameListName_Type = LocalDomainName
_JuniDnsLocalDomainNameListName_Object = MibTableColumn
juniDnsLocalDomainNameListName = _JuniDnsLocalDomainNameListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 2),
    _JuniDnsLocalDomainNameListName_Type()
)
juniDnsLocalDomainNameListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDnsLocalDomainNameListName.setStatus("current")
_JuniDnsLocalDomainNameListRowStatus_Type = RowStatus
_JuniDnsLocalDomainNameListRowStatus_Object = MibTableColumn
juniDnsLocalDomainNameListRowStatus = _JuniDnsLocalDomainNameListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 1, 3, 2, 1, 3),
    _JuniDnsLocalDomainNameListRowStatus_Type()
)
juniDnsLocalDomainNameListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniDnsLocalDomainNameListRowStatus.setStatus("current")
_JuniDnsConformance_ObjectIdentity = ObjectIdentity
juniDnsConformance = _JuniDnsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2)
)
_JuniDnsCompliances_ObjectIdentity = ObjectIdentity
juniDnsCompliances = _JuniDnsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1)
)
_JuniDnsGroups_ObjectIdentity = ObjectIdentity
juniDnsGroups = _JuniDnsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2)
)

# Managed Objects groups

juniDnsEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 1)
)
juniDnsEnableGroup.setObjects(
    ("Juniper-DNS-MIB", "juniDnsEnable")
)
if mibBuilder.loadTexts:
    juniDnsEnableGroup.setStatus("current")

juniDnsServerListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 2)
)
juniDnsServerListGroup.setObjects(
      *(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"),
        ("Juniper-DNS-MIB", "juniDnsServerListAddress"),
        ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"))
)
if mibBuilder.loadTexts:
    juniDnsServerListGroup.setStatus("obsolete")

juniDnsLocalDomainNameListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 3)
)
juniDnsLocalDomainNameListGroup.setObjects(
      *(("Juniper-DNS-MIB", "juniDnsLocalDomainNameListNextIndex"),
        ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListName"),
        ("Juniper-DNS-MIB", "juniDnsLocalDomainNameListRowStatus"))
)
if mibBuilder.loadTexts:
    juniDnsLocalDomainNameListGroup.setStatus("current")

juniDnsV4V6ServerListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 2, 4)
)
juniDnsV4V6ServerListGroup.setObjects(
      *(("Juniper-DNS-MIB", "juniDnsServerListNextIndex"),
        ("Juniper-DNS-MIB", "juniDnsServerListRowStatus"),
        ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddress"),
        ("Juniper-DNS-MIB", "juniDnsV4V6ServerListAddressType"))
)
if mibBuilder.loadTexts:
    juniDnsV4V6ServerListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniDnsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 47, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniDnsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-DNS-MIB",
    **{"JuniNextServerListIndex": JuniNextServerListIndex,
       "ServerListIndex": ServerListIndex,
       "JuniNextLocalDomainNameListIndex": JuniNextLocalDomainNameListIndex,
       "LocalDomainNameListIndex": LocalDomainNameListIndex,
       "LocalDomainName": LocalDomainName,
       "juniDnsMIB": juniDnsMIB,
       "juniDnsObjects": juniDnsObjects,
       "juniDnsGeneral": juniDnsGeneral,
       "juniDnsEnable": juniDnsEnable,
       "juniDnsServerList": juniDnsServerList,
       "juniDnsServerListNextIndex": juniDnsServerListNextIndex,
       "juniDnsServerListTable": juniDnsServerListTable,
       "juniDnsServerListEntry": juniDnsServerListEntry,
       "juniDnsServerListIndex": juniDnsServerListIndex,
       "juniDnsServerListAddress": juniDnsServerListAddress,
       "juniDnsServerListRowStatus": juniDnsServerListRowStatus,
       "juniDnsV4V6ServerListAddressType": juniDnsV4V6ServerListAddressType,
       "juniDnsV4V6ServerListAddress": juniDnsV4V6ServerListAddress,
       "juniDnsLocalDomainNameList": juniDnsLocalDomainNameList,
       "juniDnsLocalDomainNameListNextIndex": juniDnsLocalDomainNameListNextIndex,
       "juniDnsLocalDomainNameListTable": juniDnsLocalDomainNameListTable,
       "juniDnsLocalDomainNameListEntry": juniDnsLocalDomainNameListEntry,
       "juniDnsLocalDomainNameListIndex": juniDnsLocalDomainNameListIndex,
       "juniDnsLocalDomainNameListName": juniDnsLocalDomainNameListName,
       "juniDnsLocalDomainNameListRowStatus": juniDnsLocalDomainNameListRowStatus,
       "juniDnsConformance": juniDnsConformance,
       "juniDnsCompliances": juniDnsCompliances,
       "juniDnsCompliance": juniDnsCompliance,
       "juniDnsGroups": juniDnsGroups,
       "juniDnsEnableGroup": juniDnsEnableGroup,
       "juniDnsServerListGroup": juniDnsServerListGroup,
       "juniDnsLocalDomainNameListGroup": juniDnsLocalDomainNameListGroup,
       "juniDnsV4V6ServerListGroup": juniDnsV4V6ServerListGroup}
)
