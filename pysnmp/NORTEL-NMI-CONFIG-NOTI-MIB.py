# SNMP MIB module (NORTEL-NMI-CONFIG-NOTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-NMI-CONFIG-NOTI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:51 2024
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

(nortelNMInotificationGroups,) = mibBuilder.importSymbols(
    "NORTEL-NMI-GROUPS-MIB",
    "nortelNMInotificationGroups")

(nortelNMIcurrentTxNotificationSequenceNum,
 nortelNMInotificationsMIB,
 nortelNMInotifyNeAdminState,
 nortelNMInotifyNeName,
 nortelNMInotifyNeOperState,
 nortelNMInotifyNeType,
 nortelNMInotifyNeUnknownStatus) = mibBuilder.importSymbols(
    "NORTEL-NMI-NOTIFICATIONS-MIB",
    "nortelNMIcurrentTxNotificationSequenceNum",
    "nortelNMInotificationsMIB",
    "nortelNMInotifyNeAdminState",
    "nortelNMInotifyNeName",
    "nortelNMInotifyNeOperState",
    "nortelNMInotifyNeType",
    "nortelNMInotifyNeUnknownStatus")

(NortelNMItimeStampDef,) = mibBuilder.importSymbols(
    "NORTEL-NMI-TC-MIB",
    "NortelNMItimeStampDef")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

nortelNMIconfigNotiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3)
)
nortelNMIconfigNotiMIB.setRevisions(
        ("1999-06-24 00:00",
         "1999-05-31 00:00",
         "1999-04-12 00:00",
         "1999-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NortelNMIconfigNotiPrefix_ObjectIdentity = ObjectIdentity
nortelNMIconfigNotiPrefix = _NortelNMIconfigNotiPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 0)
)
if mibBuilder.loadTexts:
    nortelNMIconfigNotiPrefix.setStatus("current")
_NortelNMIconfigNotiVarbinds_ObjectIdentity = ObjectIdentity
nortelNMIconfigNotiVarbinds = _NortelNMIconfigNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    nortelNMIconfigNotiVarbinds.setStatus("current")
_NortelNMInotifyNeDeEnrolTime_Type = NortelNMItimeStampDef
_NortelNMInotifyNeDeEnrolTime_Object = MibScalar
nortelNMInotifyNeDeEnrolTime = _NortelNMInotifyNeDeEnrolTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1, 1),
    _NortelNMInotifyNeDeEnrolTime_Type()
)
nortelNMInotifyNeDeEnrolTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeDeEnrolTime.setStatus("current")
_NortelNMInotifyNeEnrolTime_Type = NortelNMItimeStampDef
_NortelNMInotifyNeEnrolTime_Object = MibScalar
nortelNMInotifyNeEnrolTime = _NortelNMInotifyNeEnrolTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1, 2),
    _NortelNMInotifyNeEnrolTime_Type()
)
nortelNMInotifyNeEnrolTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeEnrolTime.setStatus("current")
_NortelNMInotifyNeIPaddress_Type = IpAddress
_NortelNMInotifyNeIPaddress_Object = MibScalar
nortelNMInotifyNeIPaddress = _NortelNMInotifyNeIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1, 3),
    _NortelNMInotifyNeIPaddress_Type()
)
nortelNMInotifyNeIPaddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeIPaddress.setStatus("current")


class _NortelNMInotifyNeVersionInfo_Type(DisplayString):
    """Custom type nortelNMInotifyNeVersionInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NortelNMInotifyNeVersionInfo_Type.__name__ = "DisplayString"
_NortelNMInotifyNeVersionInfo_Object = MibScalar
nortelNMInotifyNeVersionInfo = _NortelNMInotifyNeVersionInfo_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1, 4),
    _NortelNMInotifyNeVersionInfo_Type()
)
nortelNMInotifyNeVersionInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeVersionInfo.setStatus("current")


class _NortelNMInotifyNeVendorName_Type(DisplayString):
    """Custom type nortelNMInotifyNeVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NortelNMInotifyNeVendorName_Type.__name__ = "DisplayString"
_NortelNMInotifyNeVendorName_Object = MibScalar
nortelNMInotifyNeVendorName = _NortelNMInotifyNeVendorName_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1, 5),
    _NortelNMInotifyNeVendorName_Type()
)
nortelNMInotifyNeVendorName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeVendorName.setStatus("current")


class _NortelNMInotifyNeLocationName_Type(DisplayString):
    """Custom type nortelNMInotifyNeLocationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NortelNMInotifyNeLocationName_Type.__name__ = "DisplayString"
_NortelNMInotifyNeLocationName_Object = MibScalar
nortelNMInotifyNeLocationName = _NortelNMInotifyNeLocationName_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1, 6),
    _NortelNMInotifyNeLocationName_Type()
)
nortelNMInotifyNeLocationName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeLocationName.setStatus("current")
_NortelNMInotifyNeDataChangeTime_Type = NortelNMItimeStampDef
_NortelNMInotifyNeDataChangeTime_Object = MibScalar
nortelNMInotifyNeDataChangeTime = _NortelNMInotifyNeDataChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 1, 7),
    _NortelNMInotifyNeDataChangeTime_Type()
)
nortelNMInotifyNeDataChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeDataChangeTime.setStatus("current")

# Managed Objects groups


# Notification objects

nortelNMIneEnrolNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 0, 11)
)
nortelNMIneEnrolNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeType"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeName"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeEnrolTime"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeIPaddress"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeVersionInfo"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeVendorName"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeLocationName"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeAdminState"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeOperState"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeUnknownStatus"))
)
if mibBuilder.loadTexts:
    nortelNMIneEnrolNotification.setStatus(
        "current"
    )

nortelNMIneDeEnrolNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 0, 12)
)
nortelNMIneDeEnrolNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeType"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeName"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeDeEnrolTime"))
)
if mibBuilder.loadTexts:
    nortelNMIneDeEnrolNotification.setStatus(
        "current"
    )

nortelNMIneAttributeChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 3, 0, 13)
)
nortelNMIneAttributeChangeNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeType"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeName"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeDataChangeTime"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeVersionInfo"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeVendorName"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeLocationName"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMInotifyNeIPaddress"))
)
if mibBuilder.loadTexts:
    nortelNMIneAttributeChangeNotification.setStatus(
        "current"
    )


# Notifications groups

nortelNMIneRegistrationNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 1)
)
nortelNMIneRegistrationNotificationGroup.setObjects(
      *(("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMIneEnrolNotification"),
        ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMIneDeEnrolNotification"))
)
if mibBuilder.loadTexts:
    nortelNMIneRegistrationNotificationGroup.setStatus(
        "current"
    )

nortelNMIneAttrChangeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 2)
)
nortelNMIneAttrChangeNotificationGroup.setObjects(
    ("NORTEL-NMI-CONFIG-NOTI-MIB", "nortelNMIneAttributeChangeNotification")
)
if mibBuilder.loadTexts:
    nortelNMIneAttrChangeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-NMI-CONFIG-NOTI-MIB",
    **{"nortelNMIneRegistrationNotificationGroup": nortelNMIneRegistrationNotificationGroup,
       "nortelNMIneAttrChangeNotificationGroup": nortelNMIneAttrChangeNotificationGroup,
       "nortelNMIconfigNotiMIB": nortelNMIconfigNotiMIB,
       "nortelNMIconfigNotiPrefix": nortelNMIconfigNotiPrefix,
       "nortelNMIneEnrolNotification": nortelNMIneEnrolNotification,
       "nortelNMIneDeEnrolNotification": nortelNMIneDeEnrolNotification,
       "nortelNMIneAttributeChangeNotification": nortelNMIneAttributeChangeNotification,
       "nortelNMIconfigNotiVarbinds": nortelNMIconfigNotiVarbinds,
       "nortelNMInotifyNeDeEnrolTime": nortelNMInotifyNeDeEnrolTime,
       "nortelNMInotifyNeEnrolTime": nortelNMInotifyNeEnrolTime,
       "nortelNMInotifyNeIPaddress": nortelNMInotifyNeIPaddress,
       "nortelNMInotifyNeVersionInfo": nortelNMInotifyNeVersionInfo,
       "nortelNMInotifyNeVendorName": nortelNMInotifyNeVendorName,
       "nortelNMInotifyNeLocationName": nortelNMInotifyNeLocationName,
       "nortelNMInotifyNeDataChangeTime": nortelNMInotifyNeDataChangeTime}
)
