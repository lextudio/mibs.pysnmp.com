# SNMP MIB module (WWP-IGMP-SNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-IGMP-SNOOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:42 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpIgmpSnoopMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10)
)
wwpIgmpSnoopMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class VlanId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



# MIB Managed Objects in the order of their OIDs

_WwpIgmpSnoopMIBObjects_ObjectIdentity = ObjectIdentity
wwpIgmpSnoopMIBObjects = _WwpIgmpSnoopMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1)
)
_WwpIgmpSnoop_ObjectIdentity = ObjectIdentity
wwpIgmpSnoop = _WwpIgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1)
)


class _WwpIgmpSnoopActivate_Type(TruthValue):
    """Custom type wwpIgmpSnoopActivate based on TruthValue"""


_WwpIgmpSnoopActivate_Object = MibScalar
wwpIgmpSnoopActivate = _WwpIgmpSnoopActivate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 1),
    _WwpIgmpSnoopActivate_Type()
)
wwpIgmpSnoopActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIgmpSnoopActivate.setStatus("current")
_WwpIgmpSnoopTable_Object = MibTable
wwpIgmpSnoopTable = _WwpIgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wwpIgmpSnoopTable.setStatus("current")
_WwpIgmpSnoopEntry_Object = MibTableRow
wwpIgmpSnoopEntry = _WwpIgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 2, 1)
)
wwpIgmpSnoopEntry.setIndexNames(
    (0, "WWP-IGMP-SNOOP-MIB", "wwpIgmpSnoopVlanId"),
    (0, "WWP-IGMP-SNOOP-MIB", "wwpIgmpSnoopGroupAddress"),
)
if mibBuilder.loadTexts:
    wwpIgmpSnoopEntry.setStatus("current")
_WwpIgmpSnoopVlanId_Type = VlanId
_WwpIgmpSnoopVlanId_Object = MibTableColumn
wwpIgmpSnoopVlanId = _WwpIgmpSnoopVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 2, 1, 1),
    _WwpIgmpSnoopVlanId_Type()
)
wwpIgmpSnoopVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopVlanId.setStatus("current")
_WwpIgmpSnoopGroupAddress_Type = IpAddress
_WwpIgmpSnoopGroupAddress_Object = MibTableColumn
wwpIgmpSnoopGroupAddress = _WwpIgmpSnoopGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 2, 1, 2),
    _WwpIgmpSnoopGroupAddress_Type()
)
wwpIgmpSnoopGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopGroupAddress.setStatus("current")
_WwpIgmpSnoopActivePorts_Type = PortList
_WwpIgmpSnoopActivePorts_Object = MibTableColumn
wwpIgmpSnoopActivePorts = _WwpIgmpSnoopActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 2, 1, 3),
    _WwpIgmpSnoopActivePorts_Type()
)
wwpIgmpSnoopActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopActivePorts.setStatus("current")


class _WwpIgmpSnoopRouterPort_Type(Integer32):
    """Custom type wwpIgmpSnoopRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpIgmpSnoopRouterPort_Type.__name__ = "Integer32"
_WwpIgmpSnoopRouterPort_Object = MibTableColumn
wwpIgmpSnoopRouterPort = _WwpIgmpSnoopRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 2, 1, 4),
    _WwpIgmpSnoopRouterPort_Type()
)
wwpIgmpSnoopRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopRouterPort.setStatus("current")
_WwpIgmpSnoopQueryTime_Type = TimeTicks
_WwpIgmpSnoopQueryTime_Object = MibTableColumn
wwpIgmpSnoopQueryTime = _WwpIgmpSnoopQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 2, 1, 5),
    _WwpIgmpSnoopQueryTime_Type()
)
wwpIgmpSnoopQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopQueryTime.setStatus("current")


class _WwpIgmpSnoopLingerTimeout_Type(Integer32):
    """Custom type wwpIgmpSnoopLingerTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpIgmpSnoopLingerTimeout_Type.__name__ = "Integer32"
_WwpIgmpSnoopLingerTimeout_Object = MibScalar
wwpIgmpSnoopLingerTimeout = _WwpIgmpSnoopLingerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 3),
    _WwpIgmpSnoopLingerTimeout_Type()
)
wwpIgmpSnoopLingerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIgmpSnoopLingerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpIgmpSnoopLingerTimeout.setUnits("seconds")


class _WwpIgmpSnoopExpiryTimeout_Type(Integer32):
    """Custom type wwpIgmpSnoopExpiryTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpIgmpSnoopExpiryTimeout_Type.__name__ = "Integer32"
_WwpIgmpSnoopExpiryTimeout_Object = MibScalar
wwpIgmpSnoopExpiryTimeout = _WwpIgmpSnoopExpiryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 4),
    _WwpIgmpSnoopExpiryTimeout_Type()
)
wwpIgmpSnoopExpiryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIgmpSnoopExpiryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpIgmpSnoopExpiryTimeout.setUnits("seconds")
_WwpIgmpSnoopQueryMessages_Type = Counter32
_WwpIgmpSnoopQueryMessages_Object = MibScalar
wwpIgmpSnoopQueryMessages = _WwpIgmpSnoopQueryMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 5),
    _WwpIgmpSnoopQueryMessages_Type()
)
wwpIgmpSnoopQueryMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopQueryMessages.setStatus("current")
_WwpIgmpSnoopJoinMessages_Type = Counter32
_WwpIgmpSnoopJoinMessages_Object = MibScalar
wwpIgmpSnoopJoinMessages = _WwpIgmpSnoopJoinMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 6),
    _WwpIgmpSnoopJoinMessages_Type()
)
wwpIgmpSnoopJoinMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopJoinMessages.setStatus("current")
_WwpIgmpSnoopLeaveMessages_Type = Counter32
_WwpIgmpSnoopLeaveMessages_Object = MibScalar
wwpIgmpSnoopLeaveMessages = _WwpIgmpSnoopLeaveMessages_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 7),
    _WwpIgmpSnoopLeaveMessages_Type()
)
wwpIgmpSnoopLeaveMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopLeaveMessages.setStatus("current")
_WwpIgmpSnoopRouterDiscards_Type = Counter32
_WwpIgmpSnoopRouterDiscards_Object = MibScalar
wwpIgmpSnoopRouterDiscards = _WwpIgmpSnoopRouterDiscards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 8),
    _WwpIgmpSnoopRouterDiscards_Type()
)
wwpIgmpSnoopRouterDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopRouterDiscards.setStatus("current")


class _WwpIgmpSnoopMinQueryTimeout_Type(Integer32):
    """Custom type wwpIgmpSnoopMinQueryTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpIgmpSnoopMinQueryTimeout_Type.__name__ = "Integer32"
_WwpIgmpSnoopMinQueryTimeout_Object = MibScalar
wwpIgmpSnoopMinQueryTimeout = _WwpIgmpSnoopMinQueryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 9),
    _WwpIgmpSnoopMinQueryTimeout_Type()
)
wwpIgmpSnoopMinQueryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIgmpSnoopMinQueryTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpIgmpSnoopMinQueryTimeout.setUnits("seconds")


class _WwpIgmpSnoopLeaveMode_Type(Integer32):
    """Custom type wwpIgmpSnoopLeaveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("inquisitive", 2))
    )


_WwpIgmpSnoopLeaveMode_Type.__name__ = "Integer32"
_WwpIgmpSnoopLeaveMode_Object = MibScalar
wwpIgmpSnoopLeaveMode = _WwpIgmpSnoopLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 10),
    _WwpIgmpSnoopLeaveMode_Type()
)
wwpIgmpSnoopLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIgmpSnoopLeaveMode.setStatus("current")


class _WwpIgmpSnoopInqLeaveTimeout_Type(Integer32):
    """Custom type wwpIgmpSnoopInqLeaveTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpIgmpSnoopInqLeaveTimeout_Type.__name__ = "Integer32"
_WwpIgmpSnoopInqLeaveTimeout_Object = MibScalar
wwpIgmpSnoopInqLeaveTimeout = _WwpIgmpSnoopInqLeaveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 11),
    _WwpIgmpSnoopInqLeaveTimeout_Type()
)
wwpIgmpSnoopInqLeaveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIgmpSnoopInqLeaveTimeout.setStatus("current")


class _WwpIgmpSnoopUnresMcastFilterAdminStatus_Type(Integer32):
    """Custom type wwpIgmpSnoopUnresMcastFilterAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpIgmpSnoopUnresMcastFilterAdminStatus_Type.__name__ = "Integer32"
_WwpIgmpSnoopUnresMcastFilterAdminStatus_Object = MibScalar
wwpIgmpSnoopUnresMcastFilterAdminStatus = _WwpIgmpSnoopUnresMcastFilterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 12),
    _WwpIgmpSnoopUnresMcastFilterAdminStatus_Type()
)
wwpIgmpSnoopUnresMcastFilterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpIgmpSnoopUnresMcastFilterAdminStatus.setStatus("current")


class _WwpIgmpSnoopUnresMcastFilterOperStatus_Type(Integer32):
    """Custom type wwpIgmpSnoopUnresMcastFilterOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_WwpIgmpSnoopUnresMcastFilterOperStatus_Type.__name__ = "Integer32"
_WwpIgmpSnoopUnresMcastFilterOperStatus_Object = MibScalar
wwpIgmpSnoopUnresMcastFilterOperStatus = _WwpIgmpSnoopUnresMcastFilterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 1, 1, 13),
    _WwpIgmpSnoopUnresMcastFilterOperStatus_Type()
)
wwpIgmpSnoopUnresMcastFilterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpIgmpSnoopUnresMcastFilterOperStatus.setStatus("current")
_WwpIgmpSnoopMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpIgmpSnoopMIBNotificationPrefix = _WwpIgmpSnoopMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 2)
)
_WwpIgmpSnoopMIBNotifications_ObjectIdentity = ObjectIdentity
wwpIgmpSnoopMIBNotifications = _WwpIgmpSnoopMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 2, 0)
)
_WwpIgmpSnoopMIBConformance_ObjectIdentity = ObjectIdentity
wwpIgmpSnoopMIBConformance = _WwpIgmpSnoopMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 3)
)
_WwpIgmpSnoopMIBCompliances_ObjectIdentity = ObjectIdentity
wwpIgmpSnoopMIBCompliances = _WwpIgmpSnoopMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 3, 1)
)
_WwpIgmpSnoopMIBGroups_ObjectIdentity = ObjectIdentity
wwpIgmpSnoopMIBGroups = _WwpIgmpSnoopMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 10, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-IGMP-SNOOP-MIB",
    **{"PortList": PortList,
       "VlanId": VlanId,
       "wwpIgmpSnoopMIB": wwpIgmpSnoopMIB,
       "wwpIgmpSnoopMIBObjects": wwpIgmpSnoopMIBObjects,
       "wwpIgmpSnoop": wwpIgmpSnoop,
       "wwpIgmpSnoopActivate": wwpIgmpSnoopActivate,
       "wwpIgmpSnoopTable": wwpIgmpSnoopTable,
       "wwpIgmpSnoopEntry": wwpIgmpSnoopEntry,
       "wwpIgmpSnoopVlanId": wwpIgmpSnoopVlanId,
       "wwpIgmpSnoopGroupAddress": wwpIgmpSnoopGroupAddress,
       "wwpIgmpSnoopActivePorts": wwpIgmpSnoopActivePorts,
       "wwpIgmpSnoopRouterPort": wwpIgmpSnoopRouterPort,
       "wwpIgmpSnoopQueryTime": wwpIgmpSnoopQueryTime,
       "wwpIgmpSnoopLingerTimeout": wwpIgmpSnoopLingerTimeout,
       "wwpIgmpSnoopExpiryTimeout": wwpIgmpSnoopExpiryTimeout,
       "wwpIgmpSnoopQueryMessages": wwpIgmpSnoopQueryMessages,
       "wwpIgmpSnoopJoinMessages": wwpIgmpSnoopJoinMessages,
       "wwpIgmpSnoopLeaveMessages": wwpIgmpSnoopLeaveMessages,
       "wwpIgmpSnoopRouterDiscards": wwpIgmpSnoopRouterDiscards,
       "wwpIgmpSnoopMinQueryTimeout": wwpIgmpSnoopMinQueryTimeout,
       "wwpIgmpSnoopLeaveMode": wwpIgmpSnoopLeaveMode,
       "wwpIgmpSnoopInqLeaveTimeout": wwpIgmpSnoopInqLeaveTimeout,
       "wwpIgmpSnoopUnresMcastFilterAdminStatus": wwpIgmpSnoopUnresMcastFilterAdminStatus,
       "wwpIgmpSnoopUnresMcastFilterOperStatus": wwpIgmpSnoopUnresMcastFilterOperStatus,
       "wwpIgmpSnoopMIBNotificationPrefix": wwpIgmpSnoopMIBNotificationPrefix,
       "wwpIgmpSnoopMIBNotifications": wwpIgmpSnoopMIBNotifications,
       "wwpIgmpSnoopMIBConformance": wwpIgmpSnoopMIBConformance,
       "wwpIgmpSnoopMIBCompliances": wwpIgmpSnoopMIBCompliances,
       "wwpIgmpSnoopMIBGroups": wwpIgmpSnoopMIBGroups}
)
