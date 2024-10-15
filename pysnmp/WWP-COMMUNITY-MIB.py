# SNMP MIB module (WWP-COMMUNITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-COMMUNITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:36 2024
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

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpCommunityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32)
)
wwpCommunityMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpCommunityMIBObjects_ObjectIdentity = ObjectIdentity
wwpCommunityMIBObjects = _WwpCommunityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1)
)
_WwpCommunity_ObjectIdentity = ObjectIdentity
wwpCommunity = _WwpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1)
)
_WwpCommunityTable_Object = MibTable
wwpCommunityTable = _WwpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    wwpCommunityTable.setStatus("current")
_WwpCommunityEntry_Object = MibTableRow
wwpCommunityEntry = _WwpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 1, 1)
)
wwpCommunityEntry.setIndexNames(
    (0, "WWP-COMMUNITY-MIB", "wwpCommunityName"),
    (0, "WWP-COMMUNITY-MIB", "wwpCommunityIpAddress"),
)
if mibBuilder.loadTexts:
    wwpCommunityEntry.setStatus("current")


class _WwpCommunityName_Type(OctetString):
    """Custom type wwpCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpCommunityName_Type.__name__ = "OctetString"
_WwpCommunityName_Object = MibTableColumn
wwpCommunityName = _WwpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 1, 1, 1),
    _WwpCommunityName_Type()
)
wwpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpCommunityName.setStatus("current")
_WwpCommunityIpAddress_Type = IpAddress
_WwpCommunityIpAddress_Object = MibTableColumn
wwpCommunityIpAddress = _WwpCommunityIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 1, 1, 2),
    _WwpCommunityIpAddress_Type()
)
wwpCommunityIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpCommunityIpAddress.setStatus("current")


class _WwpCommunityRights_Type(Integer32):
    """Custom type wwpCommunityRights based on Integer32"""
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


_WwpCommunityRights_Type.__name__ = "Integer32"
_WwpCommunityRights_Object = MibTableColumn
wwpCommunityRights = _WwpCommunityRights_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 1, 1, 3),
    _WwpCommunityRights_Type()
)
wwpCommunityRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpCommunityRights.setStatus("current")
_WwpCommunityStatus_Type = RowStatus
_WwpCommunityStatus_Object = MibTableColumn
wwpCommunityStatus = _WwpCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 1, 1, 4),
    _WwpCommunityStatus_Type()
)
wwpCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpCommunityStatus.setStatus("current")
_WwpNotifCommunityTable_Object = MibTable
wwpNotifCommunityTable = _WwpNotifCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpNotifCommunityTable.setStatus("current")
_WwpNotifCommunityEntry_Object = MibTableRow
wwpNotifCommunityEntry = _WwpNotifCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 2, 1)
)
wwpNotifCommunityEntry.setIndexNames(
    (0, "WWP-COMMUNITY-MIB", "wwpNotifCommunityName"),
    (0, "WWP-COMMUNITY-MIB", "wwpNotifCommunityDestAddr"),
)
if mibBuilder.loadTexts:
    wwpNotifCommunityEntry.setStatus("current")


class _WwpNotifCommunityName_Type(OctetString):
    """Custom type wwpNotifCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WwpNotifCommunityName_Type.__name__ = "OctetString"
_WwpNotifCommunityName_Object = MibTableColumn
wwpNotifCommunityName = _WwpNotifCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 2, 1, 1),
    _WwpNotifCommunityName_Type()
)
wwpNotifCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpNotifCommunityName.setStatus("current")
_WwpNotifCommunityDestAddr_Type = IpAddress
_WwpNotifCommunityDestAddr_Object = MibTableColumn
wwpNotifCommunityDestAddr = _WwpNotifCommunityDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 2, 1, 2),
    _WwpNotifCommunityDestAddr_Type()
)
wwpNotifCommunityDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpNotifCommunityDestAddr.setStatus("current")
_WwpNotifCommunityStatus_Type = RowStatus
_WwpNotifCommunityStatus_Object = MibTableColumn
wwpNotifCommunityStatus = _WwpNotifCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 2, 1, 3),
    _WwpNotifCommunityStatus_Type()
)
wwpNotifCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpNotifCommunityStatus.setStatus("current")


class _WwpCommunityPersist_Type(Integer32):
    """Custom type wwpCommunityPersist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("persist", 1))
    )


_WwpCommunityPersist_Type.__name__ = "Integer32"
_WwpCommunityPersist_Object = MibScalar
wwpCommunityPersist = _WwpCommunityPersist_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 1, 1, 3),
    _WwpCommunityPersist_Type()
)
wwpCommunityPersist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpCommunityPersist.setStatus("current")
_WwpCommunityMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpCommunityMIBNotificationPrefix = _WwpCommunityMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 2)
)
_WwpCommunityMIBNotifications_ObjectIdentity = ObjectIdentity
wwpCommunityMIBNotifications = _WwpCommunityMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 2, 0)
)
_WwpCommunityMIBConformance_ObjectIdentity = ObjectIdentity
wwpCommunityMIBConformance = _WwpCommunityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 3)
)
_WwpCommunityMIBCompliances_ObjectIdentity = ObjectIdentity
wwpCommunityMIBCompliances = _WwpCommunityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 3, 1)
)
_WwpCommunityMIBGroups_ObjectIdentity = ObjectIdentity
wwpCommunityMIBGroups = _WwpCommunityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 32, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-COMMUNITY-MIB",
    **{"wwpCommunityMIB": wwpCommunityMIB,
       "wwpCommunityMIBObjects": wwpCommunityMIBObjects,
       "wwpCommunity": wwpCommunity,
       "wwpCommunityTable": wwpCommunityTable,
       "wwpCommunityEntry": wwpCommunityEntry,
       "wwpCommunityName": wwpCommunityName,
       "wwpCommunityIpAddress": wwpCommunityIpAddress,
       "wwpCommunityRights": wwpCommunityRights,
       "wwpCommunityStatus": wwpCommunityStatus,
       "wwpNotifCommunityTable": wwpNotifCommunityTable,
       "wwpNotifCommunityEntry": wwpNotifCommunityEntry,
       "wwpNotifCommunityName": wwpNotifCommunityName,
       "wwpNotifCommunityDestAddr": wwpNotifCommunityDestAddr,
       "wwpNotifCommunityStatus": wwpNotifCommunityStatus,
       "wwpCommunityPersist": wwpCommunityPersist,
       "wwpCommunityMIBNotificationPrefix": wwpCommunityMIBNotificationPrefix,
       "wwpCommunityMIBNotifications": wwpCommunityMIBNotifications,
       "wwpCommunityMIBConformance": wwpCommunityMIBConformance,
       "wwpCommunityMIBCompliances": wwpCommunityMIBCompliances,
       "wwpCommunityMIBGroups": wwpCommunityMIBGroups}
)
