# SNMP MIB module (NORTEL-NMI-FAULT-NOTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-NMI-FAULT-NOTI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:53 2024
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

(NortelNMIalarmProbableCause,
 NortelNMIalarmProblemCategory,
 NortelNMItimeStampDef) = mibBuilder.importSymbols(
    "NORTEL-NMI-TC-MIB",
    "NortelNMIalarmProbableCause",
    "NortelNMIalarmProblemCategory",
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

nortelNMIfaultNotiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4)
)
nortelNMIfaultNotiMIB.setRevisions(
        ("1999-07-19 00:00",
         "1999-06-24 00:00",
         "1999-05-31 00:00",
         "1999-04-12 00:00",
         "1999-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NortelNMIfaultNotiPrefix_ObjectIdentity = ObjectIdentity
nortelNMIfaultNotiPrefix = _NortelNMIfaultNotiPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0)
)
if mibBuilder.loadTexts:
    nortelNMIfaultNotiPrefix.setStatus("current")
_NortelNMIfaultNotiVarbinds_ObjectIdentity = ObjectIdentity
nortelNMIfaultNotiVarbinds = _NortelNMIfaultNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    nortelNMIfaultNotiVarbinds.setStatus("current")
_NortelNMInotifyAlarmComponentId_Type = DisplayString
_NortelNMInotifyAlarmComponentId_Object = MibScalar
nortelNMInotifyAlarmComponentId = _NortelNMInotifyAlarmComponentId_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 1),
    _NortelNMInotifyAlarmComponentId_Type()
)
nortelNMInotifyAlarmComponentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmComponentId.setStatus("current")
_NortelNMInotifyAlarmCategory_Type = NortelNMIalarmProblemCategory
_NortelNMInotifyAlarmCategory_Object = MibScalar
nortelNMInotifyAlarmCategory = _NortelNMInotifyAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 2),
    _NortelNMInotifyAlarmCategory_Type()
)
nortelNMInotifyAlarmCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmCategory.setStatus("current")


class _NortelNMInotifyAlarmNotificationID_Type(Unsigned32):
    """Custom type nortelNMInotifyAlarmNotificationID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1073741824),
    )


_NortelNMInotifyAlarmNotificationID_Type.__name__ = "Unsigned32"
_NortelNMInotifyAlarmNotificationID_Object = MibScalar
nortelNMInotifyAlarmNotificationID = _NortelNMInotifyAlarmNotificationID_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 3),
    _NortelNMInotifyAlarmNotificationID_Type()
)
nortelNMInotifyAlarmNotificationID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmNotificationID.setStatus("current")


class _NortelNMInotifyAlarmDescription_Type(DisplayString):
    """Custom type nortelNMInotifyAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NortelNMInotifyAlarmDescription_Type.__name__ = "DisplayString"
_NortelNMInotifyAlarmDescription_Object = MibScalar
nortelNMInotifyAlarmDescription = _NortelNMInotifyAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 4),
    _NortelNMInotifyAlarmDescription_Type()
)
nortelNMInotifyAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmDescription.setStatus("current")
_NortelNMInotifyAlarmTimeStamp_Type = NortelNMItimeStampDef
_NortelNMInotifyAlarmTimeStamp_Object = MibScalar
nortelNMInotifyAlarmTimeStamp = _NortelNMInotifyAlarmTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 5),
    _NortelNMInotifyAlarmTimeStamp_Type()
)
nortelNMInotifyAlarmTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmTimeStamp.setStatus("current")
_NortelNMInotifyAlarmProbableCause_Type = NortelNMIalarmProbableCause
_NortelNMInotifyAlarmProbableCause_Object = MibScalar
nortelNMInotifyAlarmProbableCause = _NortelNMInotifyAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 6),
    _NortelNMInotifyAlarmProbableCause_Type()
)
nortelNMInotifyAlarmProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmProbableCause.setStatus("current")


class _NortelNMInotifyAlarmSpecificProblem_Type(DisplayString):
    """Custom type nortelNMInotifyAlarmSpecificProblem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NortelNMInotifyAlarmSpecificProblem_Type.__name__ = "DisplayString"
_NortelNMInotifyAlarmSpecificProblem_Object = MibScalar
nortelNMInotifyAlarmSpecificProblem = _NortelNMInotifyAlarmSpecificProblem_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 7),
    _NortelNMInotifyAlarmSpecificProblem_Type()
)
nortelNMInotifyAlarmSpecificProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmSpecificProblem.setStatus("current")
_NortelNMInotifyAlarmCorrelationIdList_Type = DisplayString
_NortelNMInotifyAlarmCorrelationIdList_Object = MibScalar
nortelNMInotifyAlarmCorrelationIdList = _NortelNMInotifyAlarmCorrelationIdList_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 8),
    _NortelNMInotifyAlarmCorrelationIdList_Type()
)
nortelNMInotifyAlarmCorrelationIdList.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyAlarmCorrelationIdList.setStatus("current")
_NortelNMInotifyNeStateChangeTime_Type = NortelNMItimeStampDef
_NortelNMInotifyNeStateChangeTime_Object = MibScalar
nortelNMInotifyNeStateChangeTime = _NortelNMInotifyNeStateChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 1, 9),
    _NortelNMInotifyNeStateChangeTime_Type()
)
nortelNMInotifyNeStateChangeTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyNeStateChangeTime.setStatus("current")

# Managed Objects groups


# Notification objects

nortelNMIneOSIstateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 101)
)
nortelNMIneOSIstateChangeNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeType"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeName"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyNeStateChangeTime"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeAdminState"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeOperState"),
        ("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMInotifyNeUnknownStatus"))
)
if mibBuilder.loadTexts:
    nortelNMIneOSIstateChangeNotification.setStatus(
        "current"
    )

nortelNMIalarmClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 201)
)
nortelNMIalarmClearNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
)
if mibBuilder.loadTexts:
    nortelNMIalarmClearNotification.setStatus(
        "current"
    )

nortelNMIwarningAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 202)
)
nortelNMIwarningAlarmNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
)
if mibBuilder.loadTexts:
    nortelNMIwarningAlarmNotification.setStatus(
        "current"
    )

nortelNMIminorAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 203)
)
nortelNMIminorAlarmNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
)
if mibBuilder.loadTexts:
    nortelNMIminorAlarmNotification.setStatus(
        "current"
    )

nortelNMImajorAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 204)
)
nortelNMImajorAlarmNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
)
if mibBuilder.loadTexts:
    nortelNMImajorAlarmNotification.setStatus(
        "current"
    )

nortelNMIcriticalAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 4, 0, 205)
)
nortelNMIcriticalAlarmNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmComponentId"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCategory"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmNotificationID"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmDescription"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmTimeStamp"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmProbableCause"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmSpecificProblem"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMInotifyAlarmCorrelationIdList"))
)
if mibBuilder.loadTexts:
    nortelNMIcriticalAlarmNotification.setStatus(
        "current"
    )


# Notifications groups

nortelNMIneStateChangeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 3)
)
nortelNMIneStateChangeNotificationGroup.setObjects(
    ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIneOSIstateChangeNotification")
)
if mibBuilder.loadTexts:
    nortelNMIneStateChangeNotificationGroup.setStatus(
        "current"
    )

nortelNMIneAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 4)
)
nortelNMIneAlarmNotificationsGroup.setObjects(
      *(("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIalarmClearNotification"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIwarningAlarmNotification"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIminorAlarmNotification"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMImajorAlarmNotification"),
        ("NORTEL-NMI-FAULT-NOTI-MIB", "nortelNMIcriticalAlarmNotification"))
)
if mibBuilder.loadTexts:
    nortelNMIneAlarmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-NMI-FAULT-NOTI-MIB",
    **{"nortelNMIneStateChangeNotificationGroup": nortelNMIneStateChangeNotificationGroup,
       "nortelNMIneAlarmNotificationsGroup": nortelNMIneAlarmNotificationsGroup,
       "nortelNMIfaultNotiMIB": nortelNMIfaultNotiMIB,
       "nortelNMIfaultNotiPrefix": nortelNMIfaultNotiPrefix,
       "nortelNMIneOSIstateChangeNotification": nortelNMIneOSIstateChangeNotification,
       "nortelNMIalarmClearNotification": nortelNMIalarmClearNotification,
       "nortelNMIwarningAlarmNotification": nortelNMIwarningAlarmNotification,
       "nortelNMIminorAlarmNotification": nortelNMIminorAlarmNotification,
       "nortelNMImajorAlarmNotification": nortelNMImajorAlarmNotification,
       "nortelNMIcriticalAlarmNotification": nortelNMIcriticalAlarmNotification,
       "nortelNMIfaultNotiVarbinds": nortelNMIfaultNotiVarbinds,
       "nortelNMInotifyAlarmComponentId": nortelNMInotifyAlarmComponentId,
       "nortelNMInotifyAlarmCategory": nortelNMInotifyAlarmCategory,
       "nortelNMInotifyAlarmNotificationID": nortelNMInotifyAlarmNotificationID,
       "nortelNMInotifyAlarmDescription": nortelNMInotifyAlarmDescription,
       "nortelNMInotifyAlarmTimeStamp": nortelNMInotifyAlarmTimeStamp,
       "nortelNMInotifyAlarmProbableCause": nortelNMInotifyAlarmProbableCause,
       "nortelNMInotifyAlarmSpecificProblem": nortelNMInotifyAlarmSpecificProblem,
       "nortelNMInotifyAlarmCorrelationIdList": nortelNMInotifyAlarmCorrelationIdList,
       "nortelNMInotifyNeStateChangeTime": nortelNMInotifyNeStateChangeTime}
)
