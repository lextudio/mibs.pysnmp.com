# SNMP MIB module (CISCO-BBSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-BBSM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:13 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoBbsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 358)
)
ciscoBbsmMIB.setRevisions(
        ("2004-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoBbsmNotifications_ObjectIdentity = ObjectIdentity
ciscoBbsmNotifications = _CiscoBbsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 0)
)
_CiscoBbsmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoBbsmMIBObjects = _CiscoBbsmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 1)
)
_CiscoBbsmEventInfo_ObjectIdentity = ObjectIdentity
ciscoBbsmEventInfo = _CiscoBbsmEventInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1)
)
_CbbsmEventDescription_Type = OctetString
_CbbsmEventDescription_Object = MibScalar
cbbsmEventDescription = _CbbsmEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 1),
    _CbbsmEventDescription_Type()
)
cbbsmEventDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbbsmEventDescription.setStatus("current")
_CbbsmEventSource_Type = SnmpAdminString
_CbbsmEventSource_Object = MibScalar
cbbsmEventSource = _CbbsmEventSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 2),
    _CbbsmEventSource_Type()
)
cbbsmEventSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbbsmEventSource.setStatus("current")
_CbbsmEventID_Type = Unsigned32
_CbbsmEventID_Object = MibScalar
cbbsmEventID = _CbbsmEventID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 3),
    _CbbsmEventID_Type()
)
cbbsmEventID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbbsmEventID.setStatus("current")


class _CbbsmEventType_Type(Integer32):
    """Custom type cbbsmEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("information", 3),
          ("warning", 2))
    )


_CbbsmEventType_Type.__name__ = "Integer32"
_CbbsmEventType_Object = MibScalar
cbbsmEventType = _CbbsmEventType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 4),
    _CbbsmEventType_Type()
)
cbbsmEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbbsmEventType.setStatus("current")
_CbbsmEventTime_Type = DateAndTime
_CbbsmEventTime_Object = MibScalar
cbbsmEventTime = _CbbsmEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 1, 1, 5),
    _CbbsmEventTime_Type()
)
cbbsmEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cbbsmEventTime.setStatus("current")
_CiscoBbsmMIBConformance_ObjectIdentity = ObjectIdentity
ciscoBbsmMIBConformance = _CiscoBbsmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 2)
)
_CiscoBbsmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoBbsmMIBCompliances = _CiscoBbsmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1)
)
_CiscoBbsmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoBbsmMIBGroups = _CiscoBbsmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2)
)

# Managed Objects groups

ciscoBbsmMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 1)
)
ciscoBbsmMIBGroup.setObjects(
      *(("CISCO-BBSM-MIB", "cbbsmEventDescription"),
        ("CISCO-BBSM-MIB", "cbbsmEventSource"),
        ("CISCO-BBSM-MIB", "cbbsmEventID"),
        ("CISCO-BBSM-MIB", "cbbsmEventType"),
        ("CISCO-BBSM-MIB", "cbbsmEventTime"))
)
if mibBuilder.loadTexts:
    ciscoBbsmMIBGroup.setStatus("current")


# Notification objects

ciscoBbsmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 0, 1)
)
ciscoBbsmEvent.setObjects(
      *(("CISCO-BBSM-MIB", "cbbsmEventDescription"),
        ("CISCO-BBSM-MIB", "cbbsmEventSource"),
        ("CISCO-BBSM-MIB", "cbbsmEventID"),
        ("CISCO-BBSM-MIB", "cbbsmEventType"),
        ("CISCO-BBSM-MIB", "cbbsmEventTime"))
)
if mibBuilder.loadTexts:
    ciscoBbsmEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoBbsmMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 2, 2)
)
ciscoBbsmMIBNotificationGroup.setObjects(
    ("CISCO-BBSM-MIB", "ciscoBbsmEvent")
)
if mibBuilder.loadTexts:
    ciscoBbsmMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoBbsmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 358, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoBbsmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-BBSM-MIB",
    **{"ciscoBbsmMIB": ciscoBbsmMIB,
       "ciscoBbsmNotifications": ciscoBbsmNotifications,
       "ciscoBbsmEvent": ciscoBbsmEvent,
       "ciscoBbsmMIBObjects": ciscoBbsmMIBObjects,
       "ciscoBbsmEventInfo": ciscoBbsmEventInfo,
       "cbbsmEventDescription": cbbsmEventDescription,
       "cbbsmEventSource": cbbsmEventSource,
       "cbbsmEventID": cbbsmEventID,
       "cbbsmEventType": cbbsmEventType,
       "cbbsmEventTime": cbbsmEventTime,
       "ciscoBbsmMIBConformance": ciscoBbsmMIBConformance,
       "ciscoBbsmMIBCompliances": ciscoBbsmMIBCompliances,
       "ciscoBbsmMIBCompliance": ciscoBbsmMIBCompliance,
       "ciscoBbsmMIBGroups": ciscoBbsmMIBGroups,
       "ciscoBbsmMIBGroup": ciscoBbsmMIBGroup,
       "ciscoBbsmMIBNotificationGroup": ciscoBbsmMIBNotificationGroup}
)
