# SNMP MIB module (AVICI-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:45 2024
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

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(aviciSysTrapDescr,) = mibBuilder.importSymbols(
    "AVICI-SYSTEM-MIB",
    "aviciSysTrapDescr")

(AviciBayType,
 AviciHighAvailabilityType,
 AviciSlotType) = mibBuilder.importSymbols(
    "AVICI-TC",
    "AviciBayType",
    "AviciHighAvailabilityType",
    "AviciSlotType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aviciServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9)
)
aviciServerMIB.setRevisions(
        ("0012-07-15 15:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciServerObjects_ObjectIdentity = ObjectIdentity
aviciServerObjects = _AviciServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1)
)
_AviciServerTable_Object = MibTable
aviciServerTable = _AviciServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    aviciServerTable.setStatus("current")
_AviciServerEntry_Object = MibTableRow
aviciServerEntry = _AviciServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1, 1)
)
aviciServerEntry.setIndexNames(
    (0, "AVICI-SERVER-MIB", "aviciServerIndex"),
)
if mibBuilder.loadTexts:
    aviciServerEntry.setStatus("current")


class _AviciServerIndex_Type(Unsigned32):
    """Custom type aviciServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AviciServerIndex_Type.__name__ = "Unsigned32"
_AviciServerIndex_Object = MibTableColumn
aviciServerIndex = _AviciServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1, 1, 1),
    _AviciServerIndex_Type()
)
aviciServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerIndex.setStatus("current")
_AviciServerBay_Type = AviciBayType
_AviciServerBay_Object = MibTableColumn
aviciServerBay = _AviciServerBay_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1, 1, 2),
    _AviciServerBay_Type()
)
aviciServerBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerBay.setStatus("current")
_AviciServerSlot_Type = AviciSlotType
_AviciServerSlot_Object = MibTableColumn
aviciServerSlot = _AviciServerSlot_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1, 1, 3),
    _AviciServerSlot_Type()
)
aviciServerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerSlot.setStatus("current")
_AviciServerState_Type = AviciHighAvailabilityType
_AviciServerState_Object = MibTableColumn
aviciServerState = _AviciServerState_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1, 1, 4),
    _AviciServerState_Type()
)
aviciServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerState.setStatus("current")


class _AviciServerDomain_Type(Integer32):
    """Custom type aviciServerDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("lower", 2),
          ("upper", 1))
    )


_AviciServerDomain_Type.__name__ = "Integer32"
_AviciServerDomain_Object = MibTableColumn
aviciServerDomain = _AviciServerDomain_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1, 1, 5),
    _AviciServerDomain_Type()
)
aviciServerDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerDomain.setStatus("current")


class _AviciServerOperStatus_Type(Integer32):
    """Custom type aviciServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("misconfigured", 4),
          ("unknown", 3),
          ("up", 1))
    )


_AviciServerOperStatus_Type.__name__ = "Integer32"
_AviciServerOperStatus_Object = MibTableColumn
aviciServerOperStatus = _AviciServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 1, 1, 1, 6),
    _AviciServerOperStatus_Type()
)
aviciServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciServerOperStatus.setStatus("current")
_AviciServerGroup_ObjectIdentity = ObjectIdentity
aviciServerGroup = _AviciServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 2)
)
_AviciServerHeartbeatType_Type = AviciHighAvailabilityType
_AviciServerHeartbeatType_Object = MibScalar
aviciServerHeartbeatType = _AviciServerHeartbeatType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 2, 1),
    _AviciServerHeartbeatType_Type()
)
aviciServerHeartbeatType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    aviciServerHeartbeatType.setStatus("current")
_AviciServerNotifications_ObjectIdentity = ObjectIdentity
aviciServerNotifications = _AviciServerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 3)
)
_AviciServerNotificationPrefix_ObjectIdentity = ObjectIdentity
aviciServerNotificationPrefix = _AviciServerNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 3, 0)
)
_AviciServerMIBConformance_ObjectIdentity = ObjectIdentity
aviciServerMIBConformance = _AviciServerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 4)
)
_AviciServerMIBCompliances_ObjectIdentity = ObjectIdentity
aviciServerMIBCompliances = _AviciServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 4, 1)
)
_AviciServerMIBGroups_ObjectIdentity = ObjectIdentity
aviciServerMIBGroups = _AviciServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 4, 2)
)

# Managed Objects groups

aviciServerGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 4, 2, 1)
)
aviciServerGeneralGroup.setObjects(
      *(("AVICI-SERVER-MIB", "aviciServerHeartbeatType"),
        ("AVICI-SERVER-MIB", "aviciServerIndex"),
        ("AVICI-SERVER-MIB", "aviciServerBay"),
        ("AVICI-SERVER-MIB", "aviciServerSlot"),
        ("AVICI-SERVER-MIB", "aviciServerState"),
        ("AVICI-SERVER-MIB", "aviciServerDomain"),
        ("AVICI-SERVER-MIB", "aviciServerOperStatus"))
)
if mibBuilder.loadTexts:
    aviciServerGeneralGroup.setStatus("current")


# Notification objects

aviciServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 3, 0, 1)
)
aviciServerUp.setObjects(
      *(("AVICI-SERVER-MIB", "aviciServerIndex"),
        ("AVICI-SERVER-MIB", "aviciServerBay"),
        ("AVICI-SERVER-MIB", "aviciServerSlot"),
        ("AVICI-SERVER-MIB", "aviciServerState"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciServerUp.setStatus(
        "current"
    )

aviciServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 3, 0, 2)
)
aviciServerDown.setObjects(
      *(("AVICI-SERVER-MIB", "aviciServerIndex"),
        ("AVICI-SERVER-MIB", "aviciServerBay"),
        ("AVICI-SERVER-MIB", "aviciServerSlot"),
        ("AVICI-SERVER-MIB", "aviciServerState"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciServerDown.setStatus(
        "current"
    )

aviciServerHeartbeatUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 3, 0, 3)
)
aviciServerHeartbeatUp.setObjects(
      *(("AVICI-SERVER-MIB", "aviciServerIndex"),
        ("AVICI-SERVER-MIB", "aviciServerBay"),
        ("AVICI-SERVER-MIB", "aviciServerSlot"),
        ("AVICI-SERVER-MIB", "aviciServerHeartbeatType"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciServerHeartbeatUp.setStatus(
        "current"
    )

aviciServerHeartbeatDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 3, 0, 4)
)
aviciServerHeartbeatDown.setObjects(
      *(("AVICI-SERVER-MIB", "aviciServerIndex"),
        ("AVICI-SERVER-MIB", "aviciServerBay"),
        ("AVICI-SERVER-MIB", "aviciServerSlot"),
        ("AVICI-SERVER-MIB", "aviciServerHeartbeatType"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciServerHeartbeatDown.setStatus(
        "current"
    )

aviciServerMisconfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 3, 0, 5)
)
aviciServerMisconfigured.setObjects(
      *(("AVICI-SERVER-MIB", "aviciServerIndex"),
        ("AVICI-SERVER-MIB", "aviciServerBay"),
        ("AVICI-SERVER-MIB", "aviciServerSlot"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciServerMisconfigured.setStatus(
        "current"
    )


# Notifications groups

aviciServerNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 4, 2, 2)
)
aviciServerNotificationGroup.setObjects(
      *(("AVICI-SERVER-MIB", "aviciServerUp"),
        ("AVICI-SERVER-MIB", "aviciServerDown"),
        ("AVICI-SERVER-MIB", "aviciServerHeartbeatUp"),
        ("AVICI-SERVER-MIB", "aviciServerHeartbeatDown"),
        ("AVICI-SERVER-MIB", "aviciServerMisconfigured"))
)
if mibBuilder.loadTexts:
    aviciServerNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aviciServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 9, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aviciServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-SERVER-MIB",
    **{"aviciServerMIB": aviciServerMIB,
       "aviciServerObjects": aviciServerObjects,
       "aviciServerTable": aviciServerTable,
       "aviciServerEntry": aviciServerEntry,
       "aviciServerIndex": aviciServerIndex,
       "aviciServerBay": aviciServerBay,
       "aviciServerSlot": aviciServerSlot,
       "aviciServerState": aviciServerState,
       "aviciServerDomain": aviciServerDomain,
       "aviciServerOperStatus": aviciServerOperStatus,
       "aviciServerGroup": aviciServerGroup,
       "aviciServerHeartbeatType": aviciServerHeartbeatType,
       "aviciServerNotifications": aviciServerNotifications,
       "aviciServerNotificationPrefix": aviciServerNotificationPrefix,
       "aviciServerUp": aviciServerUp,
       "aviciServerDown": aviciServerDown,
       "aviciServerHeartbeatUp": aviciServerHeartbeatUp,
       "aviciServerHeartbeatDown": aviciServerHeartbeatDown,
       "aviciServerMisconfigured": aviciServerMisconfigured,
       "aviciServerMIBConformance": aviciServerMIBConformance,
       "aviciServerMIBCompliances": aviciServerMIBCompliances,
       "aviciServerMIBCompliance": aviciServerMIBCompliance,
       "aviciServerMIBGroups": aviciServerMIBGroups,
       "aviciServerGeneralGroup": aviciServerGeneralGroup,
       "aviciServerNotificationGroup": aviciServerNotificationGroup}
)
