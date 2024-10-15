# SNMP MIB module (WWP-LEOS-COMMUNITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-COMMUNITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:48 2024
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosCommunityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22)
)
wwpLeosCommunityMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosCommunityMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosCommunityMIBObjects = _WwpLeosCommunityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1)
)
_WwpLeosCommunity_ObjectIdentity = ObjectIdentity
wwpLeosCommunity = _WwpLeosCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1)
)
_WwpLeosCommunityTable_Object = MibTable
wwpLeosCommunityTable = _WwpLeosCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCommunityTable.setStatus("current")
_WwpLeosCommunityEntry_Object = MibTableRow
wwpLeosCommunityEntry = _WwpLeosCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1, 1)
)
wwpLeosCommunityEntry.setIndexNames(
    (0, "WWP-LEOS-COMMUNITY-MIB", "wwpLeosCommunityIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCommunityEntry.setStatus("current")


class _WwpLeosCommunityIndex_Type(Integer32):
    """Custom type wwpLeosCommunityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosCommunityIndex_Type.__name__ = "Integer32"
_WwpLeosCommunityIndex_Object = MibTableColumn
wwpLeosCommunityIndex = _WwpLeosCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1, 1, 1),
    _WwpLeosCommunityIndex_Type()
)
wwpLeosCommunityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCommunityIndex.setStatus("current")
_WwpLeosCommunityName_Type = DisplayString
_WwpLeosCommunityName_Object = MibTableColumn
wwpLeosCommunityName = _WwpLeosCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1, 1, 2),
    _WwpLeosCommunityName_Type()
)
wwpLeosCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCommunityName.setStatus("current")
_WwpLeosCommunityAddr_Type = DisplayString
_WwpLeosCommunityAddr_Object = MibTableColumn
wwpLeosCommunityAddr = _WwpLeosCommunityAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1, 1, 3),
    _WwpLeosCommunityAddr_Type()
)
wwpLeosCommunityAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCommunityAddr.setStatus("current")
_WwpLeosCommunityResolvedIp_Type = IpAddress
_WwpLeosCommunityResolvedIp_Object = MibTableColumn
wwpLeosCommunityResolvedIp = _WwpLeosCommunityResolvedIp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1, 1, 4),
    _WwpLeosCommunityResolvedIp_Type()
)
wwpLeosCommunityResolvedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCommunityResolvedIp.setStatus("current")


class _WwpLeosCommunityRights_Type(Integer32):
    """Custom type wwpLeosCommunityRights based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_WwpLeosCommunityRights_Type.__name__ = "Integer32"
_WwpLeosCommunityRights_Object = MibTableColumn
wwpLeosCommunityRights = _WwpLeosCommunityRights_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1, 1, 5),
    _WwpLeosCommunityRights_Type()
)
wwpLeosCommunityRights.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCommunityRights.setStatus("current")
_WwpLeosCommunityStatus_Type = RowStatus
_WwpLeosCommunityStatus_Object = MibTableColumn
wwpLeosCommunityStatus = _WwpLeosCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 1, 1, 6),
    _WwpLeosCommunityStatus_Type()
)
wwpLeosCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCommunityStatus.setStatus("current")
_WwpLeosNotifCommunityTable_Object = MibTable
wwpLeosNotifCommunityTable = _WwpLeosNotifCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpLeosNotifCommunityTable.setStatus("current")
_WwpLeosNotifCommunityEntry_Object = MibTableRow
wwpLeosNotifCommunityEntry = _WwpLeosNotifCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 2, 1)
)
wwpLeosNotifCommunityEntry.setIndexNames(
    (0, "WWP-LEOS-COMMUNITY-MIB", "wwpLeosNotifIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosNotifCommunityEntry.setStatus("current")


class _WwpLeosNotifIndex_Type(Integer32):
    """Custom type wwpLeosNotifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosNotifIndex_Type.__name__ = "Integer32"
_WwpLeosNotifIndex_Object = MibTableColumn
wwpLeosNotifIndex = _WwpLeosNotifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 2, 1, 1),
    _WwpLeosNotifIndex_Type()
)
wwpLeosNotifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNotifIndex.setStatus("current")
_WwpLeosNotifCommunityName_Type = DisplayString
_WwpLeosNotifCommunityName_Object = MibTableColumn
wwpLeosNotifCommunityName = _WwpLeosNotifCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 2, 1, 2),
    _WwpLeosNotifCommunityName_Type()
)
wwpLeosNotifCommunityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosNotifCommunityName.setStatus("current")
_WwpLeosNotifCommunityDestAddr_Type = DisplayString
_WwpLeosNotifCommunityDestAddr_Object = MibTableColumn
wwpLeosNotifCommunityDestAddr = _WwpLeosNotifCommunityDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 2, 1, 3),
    _WwpLeosNotifCommunityDestAddr_Type()
)
wwpLeosNotifCommunityDestAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosNotifCommunityDestAddr.setStatus("current")
_WwpLeosNotifCommunityResolvedIpAddr_Type = IpAddress
_WwpLeosNotifCommunityResolvedIpAddr_Object = MibTableColumn
wwpLeosNotifCommunityResolvedIpAddr = _WwpLeosNotifCommunityResolvedIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 2, 1, 4),
    _WwpLeosNotifCommunityResolvedIpAddr_Type()
)
wwpLeosNotifCommunityResolvedIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosNotifCommunityResolvedIpAddr.setStatus("current")
_WwpLeosNotifCommunityStatus_Type = RowStatus
_WwpLeosNotifCommunityStatus_Object = MibTableColumn
wwpLeosNotifCommunityStatus = _WwpLeosNotifCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 1, 1, 2, 1, 5),
    _WwpLeosNotifCommunityStatus_Type()
)
wwpLeosNotifCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosNotifCommunityStatus.setStatus("current")
_WwpLeosCommunityMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosCommunityMIBNotificationPrefix = _WwpLeosCommunityMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 2)
)
_WwpLeosCommunityMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosCommunityMIBNotifications = _WwpLeosCommunityMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 2, 0)
)
_WwpLeosCommunityMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosCommunityMIBConformance = _WwpLeosCommunityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 3)
)
_WwpLeosCommunityMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosCommunityMIBCompliances = _WwpLeosCommunityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 3, 1)
)
_WwpLeosCommunityMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosCommunityMIBGroups = _WwpLeosCommunityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 22, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-COMMUNITY-MIB",
    **{"wwpLeosCommunityMIB": wwpLeosCommunityMIB,
       "wwpLeosCommunityMIBObjects": wwpLeosCommunityMIBObjects,
       "wwpLeosCommunity": wwpLeosCommunity,
       "wwpLeosCommunityTable": wwpLeosCommunityTable,
       "wwpLeosCommunityEntry": wwpLeosCommunityEntry,
       "wwpLeosCommunityIndex": wwpLeosCommunityIndex,
       "wwpLeosCommunityName": wwpLeosCommunityName,
       "wwpLeosCommunityAddr": wwpLeosCommunityAddr,
       "wwpLeosCommunityResolvedIp": wwpLeosCommunityResolvedIp,
       "wwpLeosCommunityRights": wwpLeosCommunityRights,
       "wwpLeosCommunityStatus": wwpLeosCommunityStatus,
       "wwpLeosNotifCommunityTable": wwpLeosNotifCommunityTable,
       "wwpLeosNotifCommunityEntry": wwpLeosNotifCommunityEntry,
       "wwpLeosNotifIndex": wwpLeosNotifIndex,
       "wwpLeosNotifCommunityName": wwpLeosNotifCommunityName,
       "wwpLeosNotifCommunityDestAddr": wwpLeosNotifCommunityDestAddr,
       "wwpLeosNotifCommunityResolvedIpAddr": wwpLeosNotifCommunityResolvedIpAddr,
       "wwpLeosNotifCommunityStatus": wwpLeosNotifCommunityStatus,
       "wwpLeosCommunityMIBNotificationPrefix": wwpLeosCommunityMIBNotificationPrefix,
       "wwpLeosCommunityMIBNotifications": wwpLeosCommunityMIBNotifications,
       "wwpLeosCommunityMIBConformance": wwpLeosCommunityMIBConformance,
       "wwpLeosCommunityMIBCompliances": wwpLeosCommunityMIBCompliances,
       "wwpLeosCommunityMIBGroups": wwpLeosCommunityMIBGroups}
)
