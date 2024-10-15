# SNMP MIB module (NORTEL-NMI-INFO-NOTI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NORTEL-NMI-INFO-NOTI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:54 2024
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

nortelNMIinfoNotiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NortelNMIinfoNotiPrefix_ObjectIdentity = ObjectIdentity
nortelNMIinfoNotiPrefix = _NortelNMIinfoNotiPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 0)
)
if mibBuilder.loadTexts:
    nortelNMIinfoNotiPrefix.setStatus("current")
_NortelNMIinfoNotiVarbinds_ObjectIdentity = ObjectIdentity
nortelNMIinfoNotiVarbinds = _NortelNMIinfoNotiVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    nortelNMIinfoNotiVarbinds.setStatus("current")
_NortelNMInotifyLogComponentId_Type = DisplayString
_NortelNMInotifyLogComponentId_Object = MibScalar
nortelNMInotifyLogComponentId = _NortelNMInotifyLogComponentId_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1, 1),
    _NortelNMInotifyLogComponentId_Type()
)
nortelNMInotifyLogComponentId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyLogComponentId.setStatus("current")


class _NortelNMInotifyLogText_Type(DisplayString):
    """Custom type nortelNMInotifyLogText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_NortelNMInotifyLogText_Type.__name__ = "DisplayString"
_NortelNMInotifyLogText_Object = MibScalar
nortelNMInotifyLogText = _NortelNMInotifyLogText_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1, 2),
    _NortelNMInotifyLogText_Type()
)
nortelNMInotifyLogText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyLogText.setStatus("current")
_NortelNMInotifyLogTimeStamp_Type = NortelNMItimeStampDef
_NortelNMInotifyLogTimeStamp_Object = MibScalar
nortelNMInotifyLogTimeStamp = _NortelNMInotifyLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 1, 3),
    _NortelNMInotifyLogTimeStamp_Type()
)
nortelNMInotifyLogTimeStamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nortelNMInotifyLogTimeStamp.setStatus("current")

# Managed Objects groups


# Notification objects

nortelNMIinfoNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 6, 5, 0, 301)
)
nortelNMIinfoNotification.setObjects(
      *(("NORTEL-NMI-NOTIFICATIONS-MIB", "nortelNMIcurrentTxNotificationSequenceNum"),
        ("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMInotifyLogComponentId"),
        ("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMInotifyLogText"),
        ("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMInotifyLogTimeStamp"))
)
if mibBuilder.loadTexts:
    nortelNMIinfoNotification.setStatus(
        "current"
    )


# Notifications groups

nortelNMIneLogNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 29, 1, 2, 1, 2, 5)
)
nortelNMIneLogNotificationsGroup.setObjects(
    ("NORTEL-NMI-INFO-NOTI-MIB", "nortelNMIinfoNotification")
)
if mibBuilder.loadTexts:
    nortelNMIneLogNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-NMI-INFO-NOTI-MIB",
    **{"nortelNMIneLogNotificationsGroup": nortelNMIneLogNotificationsGroup,
       "nortelNMIinfoNotiMIB": nortelNMIinfoNotiMIB,
       "nortelNMIinfoNotiPrefix": nortelNMIinfoNotiPrefix,
       "nortelNMIinfoNotification": nortelNMIinfoNotification,
       "nortelNMIinfoNotiVarbinds": nortelNMIinfoNotiVarbinds,
       "nortelNMInotifyLogComponentId": nortelNMInotifyLogComponentId,
       "nortelNMInotifyLogText": nortelNMInotifyLogText,
       "nortelNMInotifyLogTimeStamp": nortelNMInotifyLogTimeStamp}
)
