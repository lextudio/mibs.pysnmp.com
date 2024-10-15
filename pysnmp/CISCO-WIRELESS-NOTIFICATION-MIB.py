# SNMP MIB module (CISCO-WIRELESS-NOTIFICATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WIRELESS-NOTIFICATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:37 2024
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

(CiscoAlarmSeverity,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWirelessNotificationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 712)
)
ciscoWirelessNotificationMIB.setRevisions(
        ("2011-06-06 00:00",
         "2010-09-15 00:00",
         "2009-10-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CWirelessNotificationType(Integer32, TextualConvention):
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
        *(("alert", 2),
          ("event", 3),
          ("unknown", 1))
    )



class CWirelessNotificationCategory(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("accessPoints", 2),
          ("adhocRogue", 3),
          ("clients", 4),
          ("contextAwareNotifications", 8),
          ("controllers", 5),
          ("coverageHole", 6),
          ("interference", 7),
          ("meshLinks", 9),
          ("mobilityService", 10),
          ("ncs", 17),
          ("performance", 11),
          ("rogueAP", 12),
          ("rrm", 13),
          ("security", 14),
          ("switch", 16),
          ("unknown", 1),
          ("wcs", 15))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWirelessNotificationMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWirelessNotificationMIBNotifs = _CiscoWirelessNotificationMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 0)
)
_CiscoWirelessNotificationMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWirelessNotificationMIBObjects = _CiscoWirelessNotificationMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1)
)
_CWNotificationData_ObjectIdentity = ObjectIdentity
cWNotificationData = _CWNotificationData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1)
)


class _CwNotificationHistoryTableMaxLength_Type(Unsigned32):
    """Custom type cwNotificationHistoryTableMaxLength based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CwNotificationHistoryTableMaxLength_Type.__name__ = "Unsigned32"
_CwNotificationHistoryTableMaxLength_Object = MibScalar
cwNotificationHistoryTableMaxLength = _CwNotificationHistoryTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 1),
    _CwNotificationHistoryTableMaxLength_Type()
)
cwNotificationHistoryTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwNotificationHistoryTableMaxLength.setStatus("current")
_CwNotificationHistoryTable_Object = MibTable
cwNotificationHistoryTable = _CwNotificationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwNotificationHistoryTable.setStatus("current")
_CwNotificationHistoryEntry_Object = MibTableRow
cwNotificationHistoryEntry = _CwNotificationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1)
)
cwNotificationHistoryEntry.setIndexNames(
    (0, "CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationIndex"),
)
if mibBuilder.loadTexts:
    cwNotificationHistoryEntry.setStatus("current")


class _CWNotificationIndex_Type(Unsigned32):
    """Custom type cWNotificationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CWNotificationIndex_Type.__name__ = "Unsigned32"
_CWNotificationIndex_Object = MibTableColumn
cWNotificationIndex = _CWNotificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 1),
    _CWNotificationIndex_Type()
)
cWNotificationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cWNotificationIndex.setStatus("current")
_CWNotificationTimestamp_Type = DateAndTime
_CWNotificationTimestamp_Object = MibTableColumn
cWNotificationTimestamp = _CWNotificationTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 2),
    _CWNotificationTimestamp_Type()
)
cWNotificationTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationTimestamp.setStatus("current")
_CWNotificationUpdatedTimestamp_Type = DateAndTime
_CWNotificationUpdatedTimestamp_Object = MibTableColumn
cWNotificationUpdatedTimestamp = _CWNotificationUpdatedTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 3),
    _CWNotificationUpdatedTimestamp_Type()
)
cWNotificationUpdatedTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationUpdatedTimestamp.setStatus("current")


class _CWNotificationKey_Type(SnmpAdminString):
    """Custom type cWNotificationKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CWNotificationKey_Type.__name__ = "SnmpAdminString"
_CWNotificationKey_Object = MibTableColumn
cWNotificationKey = _CWNotificationKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 4),
    _CWNotificationKey_Type()
)
cWNotificationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationKey.setStatus("current")
_CWNotificationCategory_Type = CWirelessNotificationCategory
_CWNotificationCategory_Object = MibTableColumn
cWNotificationCategory = _CWNotificationCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 5),
    _CWNotificationCategory_Type()
)
cWNotificationCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationCategory.setStatus("current")


class _CWNotificationSubCategory_Type(OctetString):
    """Custom type cWNotificationSubCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CWNotificationSubCategory_Type.__name__ = "OctetString"
_CWNotificationSubCategory_Object = MibTableColumn
cWNotificationSubCategory = _CWNotificationSubCategory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 6),
    _CWNotificationSubCategory_Type()
)
cWNotificationSubCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationSubCategory.setStatus("current")
_CWNotificationManagedObjectAddressType_Type = InetAddressType
_CWNotificationManagedObjectAddressType_Object = MibTableColumn
cWNotificationManagedObjectAddressType = _CWNotificationManagedObjectAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 7),
    _CWNotificationManagedObjectAddressType_Type()
)
cWNotificationManagedObjectAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationManagedObjectAddressType.setStatus("current")
_CWNotificationManagedObjectAddress_Type = InetAddress
_CWNotificationManagedObjectAddress_Object = MibTableColumn
cWNotificationManagedObjectAddress = _CWNotificationManagedObjectAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 8),
    _CWNotificationManagedObjectAddress_Type()
)
cWNotificationManagedObjectAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationManagedObjectAddress.setStatus("current")


class _CWNotificationSourceDisplayName_Type(OctetString):
    """Custom type cWNotificationSourceDisplayName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_CWNotificationSourceDisplayName_Type.__name__ = "OctetString"
_CWNotificationSourceDisplayName_Object = MibTableColumn
cWNotificationSourceDisplayName = _CWNotificationSourceDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 9),
    _CWNotificationSourceDisplayName_Type()
)
cWNotificationSourceDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationSourceDisplayName.setStatus("current")


class _CWNotificationDescription_Type(OctetString):
    """Custom type cWNotificationDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CWNotificationDescription_Type.__name__ = "OctetString"
_CWNotificationDescription_Object = MibTableColumn
cWNotificationDescription = _CWNotificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 10),
    _CWNotificationDescription_Type()
)
cWNotificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationDescription.setStatus("current")
_CWNotificationSeverity_Type = CiscoAlarmSeverity
_CWNotificationSeverity_Object = MibTableColumn
cWNotificationSeverity = _CWNotificationSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 11),
    _CWNotificationSeverity_Type()
)
cWNotificationSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationSeverity.setStatus("current")


class _CWNotificationSpecialAttributes_Type(OctetString):
    """Custom type cWNotificationSpecialAttributes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CWNotificationSpecialAttributes_Type.__name__ = "OctetString"
_CWNotificationSpecialAttributes_Object = MibTableColumn
cWNotificationSpecialAttributes = _CWNotificationSpecialAttributes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 12),
    _CWNotificationSpecialAttributes_Type()
)
cWNotificationSpecialAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationSpecialAttributes.setStatus("current")
_CWNotificationType_Type = CWirelessNotificationType
_CWNotificationType_Object = MibTableColumn
cWNotificationType = _CWNotificationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 13),
    _CWNotificationType_Type()
)
cWNotificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationType.setStatus("current")


class _CWNotificationVirtualDomains_Type(OctetString):
    """Custom type cWNotificationVirtualDomains based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_CWNotificationVirtualDomains_Type.__name__ = "OctetString"
_CWNotificationVirtualDomains_Object = MibTableColumn
cWNotificationVirtualDomains = _CWNotificationVirtualDomains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 2, 1, 14),
    _CWNotificationVirtualDomains_Type()
)
cWNotificationVirtualDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cWNotificationVirtualDomains.setStatus("current")


class _CwNotificationMOStatusEnable_Type(TruthValue):
    """Custom type cwNotificationMOStatusEnable based on TruthValue"""


_CwNotificationMOStatusEnable_Object = MibScalar
cwNotificationMOStatusEnable = _CwNotificationMOStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 1, 1, 3),
    _CwNotificationMOStatusEnable_Type()
)
cwNotificationMOStatusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwNotificationMOStatusEnable.setStatus("current")
_CiscoWirelessNotificationMIBConform_ObjectIdentity = ObjectIdentity
ciscoWirelessNotificationMIBConform = _CiscoWirelessNotificationMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2)
)
_CiscoWirelessNotificationMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWirelessNotificationMIBCompliances = _CiscoWirelessNotificationMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 1)
)
_CiscoWirelessNotificationMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWirelessNotificationMIBGroups = _CiscoWirelessNotificationMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2)
)

# Managed Objects groups

ciscoWirelessNotificationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 1)
)
ciscoWirelessNotificationConfigGroup.setObjects(
    ("CISCO-WIRELESS-NOTIFICATION-MIB", "cwNotificationHistoryTableMaxLength")
)
if mibBuilder.loadTexts:
    ciscoWirelessNotificationConfigGroup.setStatus("current")

ciscoWirelessNotificationObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 3)
)
ciscoWirelessNotificationObjectsGroup.setObjects(
      *(("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationTimestamp"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationUpdatedTimestamp"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationKey"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationCategory"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSubCategory"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddressType"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddress"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSourceDisplayName"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationDescription"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSeverity"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSpecialAttributes"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationType"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationVirtualDomains"))
)
if mibBuilder.loadTexts:
    ciscoWirelessNotificationObjectsGroup.setStatus("current")

ciscoWirelessNotificationEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 4)
)
ciscoWirelessNotificationEnableGroup.setObjects(
    ("CISCO-WIRELESS-NOTIFICATION-MIB", "cwNotificationMOStatusEnable")
)
if mibBuilder.loadTexts:
    ciscoWirelessNotificationEnableGroup.setStatus("current")


# Notification objects

ciscoWirelessMOStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 0, 1)
)
ciscoWirelessMOStatusNotification.setObjects(
      *(("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationTimestamp"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationUpdatedTimestamp"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationKey"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationCategory"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSubCategory"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddressType"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationManagedObjectAddress"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSourceDisplayName"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationDescription"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSeverity"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationSpecialAttributes"),
        ("CISCO-WIRELESS-NOTIFICATION-MIB", "cWNotificationVirtualDomains"))
)
if mibBuilder.loadTexts:
    ciscoWirelessMOStatusNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoWirelessNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 2, 2)
)
ciscoWirelessNotificationsGroup.setObjects(
    ("CISCO-WIRELESS-NOTIFICATION-MIB", "ciscoWirelessMOStatusNotification")
)
if mibBuilder.loadTexts:
    ciscoWirelessNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoWirelessNotificationMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 712, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWirelessNotificationMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WIRELESS-NOTIFICATION-MIB",
    **{"CWirelessNotificationType": CWirelessNotificationType,
       "CWirelessNotificationCategory": CWirelessNotificationCategory,
       "ciscoWirelessNotificationMIB": ciscoWirelessNotificationMIB,
       "ciscoWirelessNotificationMIBNotifs": ciscoWirelessNotificationMIBNotifs,
       "ciscoWirelessMOStatusNotification": ciscoWirelessMOStatusNotification,
       "ciscoWirelessNotificationMIBObjects": ciscoWirelessNotificationMIBObjects,
       "cWNotificationData": cWNotificationData,
       "cwNotificationHistoryTableMaxLength": cwNotificationHistoryTableMaxLength,
       "cwNotificationHistoryTable": cwNotificationHistoryTable,
       "cwNotificationHistoryEntry": cwNotificationHistoryEntry,
       "cWNotificationIndex": cWNotificationIndex,
       "cWNotificationTimestamp": cWNotificationTimestamp,
       "cWNotificationUpdatedTimestamp": cWNotificationUpdatedTimestamp,
       "cWNotificationKey": cWNotificationKey,
       "cWNotificationCategory": cWNotificationCategory,
       "cWNotificationSubCategory": cWNotificationSubCategory,
       "cWNotificationManagedObjectAddressType": cWNotificationManagedObjectAddressType,
       "cWNotificationManagedObjectAddress": cWNotificationManagedObjectAddress,
       "cWNotificationSourceDisplayName": cWNotificationSourceDisplayName,
       "cWNotificationDescription": cWNotificationDescription,
       "cWNotificationSeverity": cWNotificationSeverity,
       "cWNotificationSpecialAttributes": cWNotificationSpecialAttributes,
       "cWNotificationType": cWNotificationType,
       "cWNotificationVirtualDomains": cWNotificationVirtualDomains,
       "cwNotificationMOStatusEnable": cwNotificationMOStatusEnable,
       "ciscoWirelessNotificationMIBConform": ciscoWirelessNotificationMIBConform,
       "ciscoWirelessNotificationMIBCompliances": ciscoWirelessNotificationMIBCompliances,
       "ciscoWirelessNotificationMIBCompliance": ciscoWirelessNotificationMIBCompliance,
       "ciscoWirelessNotificationMIBGroups": ciscoWirelessNotificationMIBGroups,
       "ciscoWirelessNotificationConfigGroup": ciscoWirelessNotificationConfigGroup,
       "ciscoWirelessNotificationsGroup": ciscoWirelessNotificationsGroup,
       "ciscoWirelessNotificationObjectsGroup": ciscoWirelessNotificationObjectsGroup,
       "ciscoWirelessNotificationEnableGroup": ciscoWirelessNotificationEnableGroup}
)
