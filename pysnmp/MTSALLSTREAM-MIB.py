# SNMP MIB module (MTSALLSTREAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MTSALLSTREAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:04 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

mtsallstream = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 23398)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AllstreamObjects_ObjectIdentity = ObjectIdentity
allstreamObjects = _AllstreamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23398, 1)
)
_AllstreamCICEventEntities_ObjectIdentity = ObjectIdentity
allstreamCICEventEntities = _AllstreamCICEventEntities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23398, 1, 1)
)


class _CicEventID_Type(Unsigned32):
    """Custom type cicEventID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CicEventID_Type.__name__ = "Unsigned32"
_CicEventID_Object = MibScalar
cicEventID = _CicEventID_Object(
    (1, 3, 6, 1, 4, 1, 23398, 1, 1, 1),
    _CicEventID_Type()
)
cicEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicEventID.setStatus("current")
_CicNode_Type = DisplayString
_CicNode_Object = MibScalar
cicNode = _CicNode_Object(
    (1, 3, 6, 1, 4, 1, 23398, 1, 1, 2),
    _CicNode_Type()
)
cicNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicNode.setStatus("current")
_CicEventMessage_Type = DisplayString
_CicEventMessage_Object = MibScalar
cicEventMessage = _CicEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 23398, 1, 1, 3),
    _CicEventMessage_Type()
)
cicEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicEventMessage.setStatus("current")
_CicEventSeverity_Type = Unsigned32
_CicEventSeverity_Object = MibScalar
cicEventSeverity = _CicEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 23398, 1, 1, 4),
    _CicEventSeverity_Type()
)
cicEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicEventSeverity.setStatus("current")
_CicEventTrapReason_Type = DisplayString
_CicEventTrapReason_Object = MibScalar
cicEventTrapReason = _CicEventTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 23398, 1, 1, 5),
    _CicEventTrapReason_Type()
)
cicEventTrapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cicEventTrapReason.setStatus("current")
_AllstreamNotifications_ObjectIdentity = ObjectIdentity
allstreamNotifications = _AllstreamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23398, 1, 20)
)
_AllstreamMIBConformance_ObjectIdentity = ObjectIdentity
allstreamMIBConformance = _AllstreamMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23398, 2)
)
_AllstreamCompliances_ObjectIdentity = ObjectIdentity
allstreamCompliances = _AllstreamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23398, 2, 1)
)
_AllstreamGroups_ObjectIdentity = ObjectIdentity
allstreamGroups = _AllstreamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23398, 2, 2)
)

# Managed Objects groups

allstreamObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 23398, 2, 2, 2)
)
allstreamObjectGroup.setObjects(
      *(("MTSALLSTREAM-MIB", "cicEventID"),
        ("MTSALLSTREAM-MIB", "cicNode"),
        ("MTSALLSTREAM-MIB", "cicEventMessage"),
        ("MTSALLSTREAM-MIB", "cicEventSeverity"),
        ("MTSALLSTREAM-MIB", "cicEventTrapReason"))
)
if mibBuilder.loadTexts:
    allstreamObjectGroup.setStatus("current")


# Notification objects

allstreamForwardCICEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 23398, 1, 20, 1)
)
allstreamForwardCICEventTrap.setObjects(
      *(("MTSALLSTREAM-MIB", "cicEventID"),
        ("MTSALLSTREAM-MIB", "cicNode"),
        ("MTSALLSTREAM-MIB", "cicEventMessage"),
        ("MTSALLSTREAM-MIB", "cicEventSeverity"),
        ("MTSALLSTREAM-MIB", "cicEventTrapReason"))
)
if mibBuilder.loadTexts:
    allstreamForwardCICEventTrap.setStatus(
        "current"
    )


# Notifications groups

allstreamNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 23398, 2, 2, 1)
)
allstreamNotificationsGroup.setObjects(
    ("MTSALLSTREAM-MIB", "allstreamForwardCICEventTrap")
)
if mibBuilder.loadTexts:
    allstreamNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

allstreamBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 23398, 2, 1, 1)
)
if mibBuilder.loadTexts:
    allstreamBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MTSALLSTREAM-MIB",
    **{"mtsallstream": mtsallstream,
       "allstreamObjects": allstreamObjects,
       "allstreamCICEventEntities": allstreamCICEventEntities,
       "cicEventID": cicEventID,
       "cicNode": cicNode,
       "cicEventMessage": cicEventMessage,
       "cicEventSeverity": cicEventSeverity,
       "cicEventTrapReason": cicEventTrapReason,
       "allstreamNotifications": allstreamNotifications,
       "allstreamForwardCICEventTrap": allstreamForwardCICEventTrap,
       "allstreamMIBConformance": allstreamMIBConformance,
       "allstreamCompliances": allstreamCompliances,
       "allstreamBasicCompliance": allstreamBasicCompliance,
       "allstreamGroups": allstreamGroups,
       "allstreamNotificationsGroup": allstreamNotificationsGroup,
       "allstreamObjectGroup": allstreamObjectGroup}
)
