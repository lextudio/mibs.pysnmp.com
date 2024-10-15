# SNMP MIB module (CISCO-STUN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-STUN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:57 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoStunMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30)
)
ciscoStunMIB.setRevisions(
        ("1995-08-21 00:00",
         "1995-03-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_StunObjects_ObjectIdentity = ObjectIdentity
stunObjects = _StunObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1)
)
_StunGlobal_ObjectIdentity = ObjectIdentity
stunGlobal = _StunGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 1)
)
_StunIPAddr_Type = IpAddress
_StunIPAddr_Object = MibScalar
stunIPAddr = _StunIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 1, 1),
    _StunIPAddr_Type()
)
stunIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunIPAddr.setStatus("current")
_StunGroups_ObjectIdentity = ObjectIdentity
stunGroups = _StunGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2)
)
_StunGroupTable_Object = MibTable
stunGroupTable = _StunGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1)
)
if mibBuilder.loadTexts:
    stunGroupTable.setStatus("current")
_StunGroupEntry_Object = MibTableRow
stunGroupEntry = _StunGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1)
)
stunGroupEntry.setIndexNames(
    (0, "CISCO-STUN-MIB", "stunGroupIndex"),
)
if mibBuilder.loadTexts:
    stunGroupEntry.setStatus("current")


class _StunGroupIndex_Type(Integer32):
    """Custom type stunGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StunGroupIndex_Type.__name__ = "Integer32"
_StunGroupIndex_Object = MibTableColumn
stunGroupIndex = _StunGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1, 1),
    _StunGroupIndex_Type()
)
stunGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stunGroupIndex.setStatus("current")


class _StunProtocolType_Type(Integer32):
    """Custom type stunProtocolType based on Integer32"""
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
        *(("basic", 1),
          ("custom", 4),
          ("sdlc", 2),
          ("sdlctg", 3))
    )


_StunProtocolType_Type.__name__ = "Integer32"
_StunProtocolType_Object = MibTableColumn
stunProtocolType = _StunProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 2, 1, 1, 2),
    _StunProtocolType_Type()
)
stunProtocolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunProtocolType.setStatus("current")
_StunPorts_ObjectIdentity = ObjectIdentity
stunPorts = _StunPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3)
)
_StunPortTable_Object = MibTable
stunPortTable = _StunPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1)
)
if mibBuilder.loadTexts:
    stunPortTable.setStatus("current")
_StunPortEntry_Object = MibTableRow
stunPortEntry = _StunPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1)
)
stunPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    stunPortEntry.setStatus("current")


class _StunPortGroupIndex_Type(Integer32):
    """Custom type stunPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StunPortGroupIndex_Type.__name__ = "Integer32"
_StunPortGroupIndex_Object = MibTableColumn
stunPortGroupIndex = _StunPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 1),
    _StunPortGroupIndex_Type()
)
stunPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunPortGroupIndex.setStatus("current")


class _StunPortDefaultPeerType_Type(Integer32):
    """Custom type stunPortDefaultPeerType based on Integer32"""
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
        *(("direct", 3),
          ("frameRelay", 4),
          ("ip", 2),
          ("other", 1))
    )


_StunPortDefaultPeerType_Type.__name__ = "Integer32"
_StunPortDefaultPeerType_Object = MibTableColumn
stunPortDefaultPeerType = _StunPortDefaultPeerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 2),
    _StunPortDefaultPeerType_Type()
)
stunPortDefaultPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunPortDefaultPeerType.setStatus("current")
_StunPortDefaultPeerIP_Type = IpAddress
_StunPortDefaultPeerIP_Object = MibTableColumn
stunPortDefaultPeerIP = _StunPortDefaultPeerIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 3),
    _StunPortDefaultPeerIP_Type()
)
stunPortDefaultPeerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunPortDefaultPeerIP.setStatus("current")
_StunPortDefaultPeerSerialInterface_Type = InterfaceIndex
_StunPortDefaultPeerSerialInterface_Object = MibTableColumn
stunPortDefaultPeerSerialInterface = _StunPortDefaultPeerSerialInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 3, 1, 1, 4),
    _StunPortDefaultPeerSerialInterface_Type()
)
stunPortDefaultPeerSerialInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunPortDefaultPeerSerialInterface.setStatus("current")
_StunRoutes_ObjectIdentity = ObjectIdentity
stunRoutes = _StunRoutes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4)
)
_StunRouteTable_Object = MibTable
stunRouteTable = _StunRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1)
)
if mibBuilder.loadTexts:
    stunRouteTable.setStatus("current")
_StunRouteEntry_Object = MibTableRow
stunRouteEntry = _StunRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1)
)
stunRouteEntry.setIndexNames(
    (0, "CISCO-STUN-MIB", "stunGroupIndex"),
    (0, "CISCO-STUN-MIB", "stunRouteStationAddress"),
)
if mibBuilder.loadTexts:
    stunRouteEntry.setStatus("current")


class _StunRouteStationAddress_Type(Integer32):
    """Custom type stunRouteStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_StunRouteStationAddress_Type.__name__ = "Integer32"
_StunRouteStationAddress_Object = MibTableColumn
stunRouteStationAddress = _StunRouteStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 1),
    _StunRouteStationAddress_Type()
)
stunRouteStationAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stunRouteStationAddress.setStatus("current")


class _StunRouteType_Type(Integer32):
    """Custom type stunRouteType based on Integer32"""
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
        *(("direct", 3),
          ("frameRelay", 4),
          ("ip", 2),
          ("other", 1))
    )


_StunRouteType_Type.__name__ = "Integer32"
_StunRouteType_Object = MibTableColumn
stunRouteType = _StunRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 2),
    _StunRouteType_Type()
)
stunRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteType.setStatus("current")
_StunRouteRemoteIP_Type = IpAddress
_StunRouteRemoteIP_Object = MibTableColumn
stunRouteRemoteIP = _StunRouteRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 3),
    _StunRouteRemoteIP_Type()
)
stunRouteRemoteIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteRemoteIP.setStatus("current")
_StunRouteSerialInterface_Type = InterfaceIndex
_StunRouteSerialInterface_Object = MibTableColumn
stunRouteSerialInterface = _StunRouteSerialInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 4),
    _StunRouteSerialInterface_Type()
)
stunRouteSerialInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteSerialInterface.setStatus("current")


class _StunRoutePriority_Type(Integer32):
    """Custom type stunRoutePriority based on Integer32"""
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
        *(("high", 4),
          ("low", 1),
          ("medium", 3),
          ("normal", 2))
    )


_StunRoutePriority_Type.__name__ = "Integer32"
_StunRoutePriority_Object = MibTableColumn
stunRoutePriority = _StunRoutePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 5),
    _StunRoutePriority_Type()
)
stunRoutePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRoutePriority.setStatus("current")


class _StunRoutePeerState_Type(Integer32):
    """Custom type stunRoutePeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("connected", 5),
          ("dead", 1),
          ("direct", 6),
          ("openWait", 4),
          ("opening", 3))
    )


_StunRoutePeerState_Type.__name__ = "Integer32"
_StunRoutePeerState_Object = MibTableColumn
stunRoutePeerState = _StunRoutePeerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 6),
    _StunRoutePeerState_Type()
)
stunRoutePeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRoutePeerState.setStatus("current")
_StunRouteLocalAck_Type = TruthValue
_StunRouteLocalAck_Object = MibTableColumn
stunRouteLocalAck = _StunRouteLocalAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 7),
    _StunRouteLocalAck_Type()
)
stunRouteLocalAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteLocalAck.setStatus("current")
_StunRouteRxPackets_Type = Counter32
_StunRouteRxPackets_Object = MibTableColumn
stunRouteRxPackets = _StunRouteRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 8),
    _StunRouteRxPackets_Type()
)
stunRouteRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteRxPackets.setStatus("current")
_StunRouteTxPackets_Type = Counter32
_StunRouteTxPackets_Object = MibTableColumn
stunRouteTxPackets = _StunRouteTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 9),
    _StunRouteTxPackets_Type()
)
stunRouteTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteTxPackets.setStatus("current")
_StunRouteRxBytes_Type = Counter32
_StunRouteRxBytes_Object = MibTableColumn
stunRouteRxBytes = _StunRouteRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 10),
    _StunRouteRxBytes_Type()
)
stunRouteRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteRxBytes.setStatus("current")
_StunRouteTxBytes_Type = Counter32
_StunRouteTxBytes_Object = MibTableColumn
stunRouteTxBytes = _StunRouteTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 1, 4, 1, 1, 11),
    _StunRouteTxBytes_Type()
)
stunRouteTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stunRouteTxBytes.setStatus("current")
_StunNotificationPrefix_ObjectIdentity = ObjectIdentity
stunNotificationPrefix = _StunNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 2)
)
_StunNotifications_ObjectIdentity = ObjectIdentity
stunNotifications = _StunNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 2, 0)
)
_StunMibConformance_ObjectIdentity = ObjectIdentity
stunMibConformance = _StunMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3)
)
_StunMibCompliances_ObjectIdentity = ObjectIdentity
stunMibCompliances = _StunMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 1)
)
_StunMibGroups_ObjectIdentity = ObjectIdentity
stunMibGroups = _StunMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2)
)

# Managed Objects groups

stunGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 1)
)
stunGlobalGroup.setObjects(
    ("CISCO-STUN-MIB", "stunIPAddr")
)
if mibBuilder.loadTexts:
    stunGlobalGroup.setStatus("current")

stunGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 2)
)
stunGroupGroup.setObjects(
    ("CISCO-STUN-MIB", "stunProtocolType")
)
if mibBuilder.loadTexts:
    stunGroupGroup.setStatus("current")

stunPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 3)
)
stunPortGroup.setObjects(
      *(("CISCO-STUN-MIB", "stunPortGroupIndex"),
        ("CISCO-STUN-MIB", "stunPortDefaultPeerType"),
        ("CISCO-STUN-MIB", "stunPortDefaultPeerIP"),
        ("CISCO-STUN-MIB", "stunPortDefaultPeerSerialInterface"))
)
if mibBuilder.loadTexts:
    stunPortGroup.setStatus("current")

stunRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 2, 4)
)
stunRouteGroup.setObjects(
      *(("CISCO-STUN-MIB", "stunRouteType"),
        ("CISCO-STUN-MIB", "stunRouteRemoteIP"),
        ("CISCO-STUN-MIB", "stunRouteSerialInterface"),
        ("CISCO-STUN-MIB", "stunRoutePriority"),
        ("CISCO-STUN-MIB", "stunRoutePeerState"),
        ("CISCO-STUN-MIB", "stunRouteLocalAck"),
        ("CISCO-STUN-MIB", "stunRouteRxPackets"),
        ("CISCO-STUN-MIB", "stunRouteTxPackets"),
        ("CISCO-STUN-MIB", "stunRouteRxBytes"),
        ("CISCO-STUN-MIB", "stunRouteTxBytes"))
)
if mibBuilder.loadTexts:
    stunRouteGroup.setStatus("current")


# Notification objects

stunPeerStateChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 2, 0, 1)
)
stunPeerStateChangeNotification.setObjects(
    ("CISCO-STUN-MIB", "stunRoutePeerState")
)
if mibBuilder.loadTexts:
    stunPeerStateChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

stunMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 30, 3, 1, 1)
)
if mibBuilder.loadTexts:
    stunMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-STUN-MIB",
    **{"ciscoStunMIB": ciscoStunMIB,
       "stunObjects": stunObjects,
       "stunGlobal": stunGlobal,
       "stunIPAddr": stunIPAddr,
       "stunGroups": stunGroups,
       "stunGroupTable": stunGroupTable,
       "stunGroupEntry": stunGroupEntry,
       "stunGroupIndex": stunGroupIndex,
       "stunProtocolType": stunProtocolType,
       "stunPorts": stunPorts,
       "stunPortTable": stunPortTable,
       "stunPortEntry": stunPortEntry,
       "stunPortGroupIndex": stunPortGroupIndex,
       "stunPortDefaultPeerType": stunPortDefaultPeerType,
       "stunPortDefaultPeerIP": stunPortDefaultPeerIP,
       "stunPortDefaultPeerSerialInterface": stunPortDefaultPeerSerialInterface,
       "stunRoutes": stunRoutes,
       "stunRouteTable": stunRouteTable,
       "stunRouteEntry": stunRouteEntry,
       "stunRouteStationAddress": stunRouteStationAddress,
       "stunRouteType": stunRouteType,
       "stunRouteRemoteIP": stunRouteRemoteIP,
       "stunRouteSerialInterface": stunRouteSerialInterface,
       "stunRoutePriority": stunRoutePriority,
       "stunRoutePeerState": stunRoutePeerState,
       "stunRouteLocalAck": stunRouteLocalAck,
       "stunRouteRxPackets": stunRouteRxPackets,
       "stunRouteTxPackets": stunRouteTxPackets,
       "stunRouteRxBytes": stunRouteRxBytes,
       "stunRouteTxBytes": stunRouteTxBytes,
       "stunNotificationPrefix": stunNotificationPrefix,
       "stunNotifications": stunNotifications,
       "stunPeerStateChangeNotification": stunPeerStateChangeNotification,
       "stunMibConformance": stunMibConformance,
       "stunMibCompliances": stunMibCompliances,
       "stunMibCompliance": stunMibCompliance,
       "stunMibGroups": stunMibGroups,
       "stunGlobalGroup": stunGlobalGroup,
       "stunGroupGroup": stunGroupGroup,
       "stunPortGroup": stunPortGroup,
       "stunRouteGroup": stunRouteGroup}
)
