# SNMP MIB module (COLUBRIS-DEVICE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-DEVICE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:16 2024
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

(coDevDisIndex,) = mibBuilder.importSymbols(
    "COLUBRIS-DEVICE-MIB",
    "coDevDisIndex")

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

colubrisDeviceIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisDeviceIfMIBObjects_ObjectIdentity = ObjectIdentity
colubrisDeviceIfMIBObjects = _ColubrisDeviceIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1)
)
_CoDeviceIfStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceIfStatusGroup = _CoDeviceIfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1)
)
_CoDeviceIfStatusTable_Object = MibTable
coDeviceIfStatusTable = _CoDeviceIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceIfStatusTable.setStatus("current")
_CoDeviceIfStatusEntry_Object = MibTableRow
coDeviceIfStatusEntry = _CoDeviceIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1)
)
coDeviceIfStatusEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIfIndex"),
)
if mibBuilder.loadTexts:
    coDeviceIfStatusEntry.setStatus("current")


class _CoDevIfStaIfIndex_Type(Integer32):
    """Custom type coDevIfStaIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevIfStaIfIndex_Type.__name__ = "Integer32"
_CoDevIfStaIfIndex_Object = MibTableColumn
coDevIfStaIfIndex = _CoDevIfStaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 1),
    _CoDevIfStaIfIndex_Type()
)
coDevIfStaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevIfStaIfIndex.setStatus("current")
_CoDevIfStaFriendlyInterfaceName_Type = DisplayString
_CoDevIfStaFriendlyInterfaceName_Object = MibTableColumn
coDevIfStaFriendlyInterfaceName = _CoDevIfStaFriendlyInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 2),
    _CoDevIfStaFriendlyInterfaceName_Type()
)
coDevIfStaFriendlyInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaFriendlyInterfaceName.setStatus("current")


class _CoDevIfStaType_Type(Integer32):
    """Custom type coDevIfStaType based on Integer32"""
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
        *(("bridge", 4),
          ("ethernet", 2),
          ("ieee80211", 5),
          ("ieee80211Wds", 6),
          ("l2vlan", 3),
          ("other", 1))
    )


_CoDevIfStaType_Type.__name__ = "Integer32"
_CoDevIfStaType_Object = MibTableColumn
coDevIfStaType = _CoDevIfStaType_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 3),
    _CoDevIfStaType_Type()
)
coDevIfStaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaType.setStatus("current")


class _CoDevIfStaVLAN_Type(Integer32):
    """Custom type coDevIfStaVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CoDevIfStaVLAN_Type.__name__ = "Integer32"
_CoDevIfStaVLAN_Object = MibTableColumn
coDevIfStaVLAN = _CoDevIfStaVLAN_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 4),
    _CoDevIfStaVLAN_Type()
)
coDevIfStaVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaVLAN.setStatus("current")
_CoDevIfStaIpAddress_Type = IpAddress
_CoDevIfStaIpAddress_Object = MibTableColumn
coDevIfStaIpAddress = _CoDevIfStaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 5),
    _CoDevIfStaIpAddress_Type()
)
coDevIfStaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaIpAddress.setStatus("current")
_CoDevIfStaNetworkMask_Type = IpAddress
_CoDevIfStaNetworkMask_Object = MibTableColumn
coDevIfStaNetworkMask = _CoDevIfStaNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 6),
    _CoDevIfStaNetworkMask_Type()
)
coDevIfStaNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaNetworkMask.setStatus("current")
_CoDevIfStaMACAddress_Type = MacAddress
_CoDevIfStaMACAddress_Object = MibTableColumn
coDevIfStaMACAddress = _CoDevIfStaMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 7),
    _CoDevIfStaMACAddress_Type()
)
coDevIfStaMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaMACAddress.setStatus("current")


class _CoDevIfStaState_Type(Integer32):
    """Custom type coDevIfStaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CoDevIfStaState_Type.__name__ = "Integer32"
_CoDevIfStaState_Object = MibTableColumn
coDevIfStaState = _CoDevIfStaState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 8),
    _CoDevIfStaState_Type()
)
coDevIfStaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaState.setStatus("current")
_CoDevIfStaPowerForwardingStatus_Type = TruthValue
_CoDevIfStaPowerForwardingStatus_Object = MibTableColumn
coDevIfStaPowerForwardingStatus = _CoDevIfStaPowerForwardingStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 9),
    _CoDevIfStaPowerForwardingStatus_Type()
)
coDevIfStaPowerForwardingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaPowerForwardingStatus.setStatus("current")
_CoDeviceIfStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceIfStatsGroup = _CoDeviceIfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2)
)
_CoDeviceIfStatsTable_Object = MibTable
coDeviceIfStatsTable = _CoDeviceIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceIfStatsTable.setStatus("current")
_CoDeviceIfStatsEntry_Object = MibTableRow
coDeviceIfStatsEntry = _CoDeviceIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceIfStatsEntry.setStatus("current")
_CoDevIfStsRxBytes_Type = Counter64
_CoDevIfStsRxBytes_Object = MibTableColumn
coDevIfStsRxBytes = _CoDevIfStsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 1),
    _CoDevIfStsRxBytes_Type()
)
coDevIfStsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsRxBytes.setStatus("current")
_CoDevIfStsRxPackets_Type = Counter32
_CoDevIfStsRxPackets_Object = MibTableColumn
coDevIfStsRxPackets = _CoDevIfStsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 2),
    _CoDevIfStsRxPackets_Type()
)
coDevIfStsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsRxPackets.setStatus("current")
_CoDevIfStsRxErrors_Type = Counter32
_CoDevIfStsRxErrors_Object = MibTableColumn
coDevIfStsRxErrors = _CoDevIfStsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 3),
    _CoDevIfStsRxErrors_Type()
)
coDevIfStsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsRxErrors.setStatus("current")
_CoDevIfStsTxBytes_Type = Counter64
_CoDevIfStsTxBytes_Object = MibTableColumn
coDevIfStsTxBytes = _CoDevIfStsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 4),
    _CoDevIfStsTxBytes_Type()
)
coDevIfStsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsTxBytes.setStatus("current")
_CoDevIfStsTxPackets_Type = Counter32
_CoDevIfStsTxPackets_Object = MibTableColumn
coDevIfStsTxPackets = _CoDevIfStsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 5),
    _CoDevIfStsTxPackets_Type()
)
coDevIfStsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsTxPackets.setStatus("current")
_CoDevIfStsTxErrors_Type = Counter32
_CoDevIfStsTxErrors_Object = MibTableColumn
coDevIfStsTxErrors = _CoDevIfStsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 6),
    _CoDevIfStsTxErrors_Type()
)
coDevIfStsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsTxErrors.setStatus("current")
_CoDeviceIfFdbGroup_ObjectIdentity = ObjectIdentity
coDeviceIfFdbGroup = _CoDeviceIfFdbGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3)
)
_CoDeviceIfFdbTable_Object = MibTable
coDeviceIfFdbTable = _CoDeviceIfFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceIfFdbTable.setStatus("current")
_CoDeviceIfFdbEntry_Object = MibTableRow
coDeviceIfFdbEntry = _CoDeviceIfFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1)
)
coDeviceIfFdbEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIfIndex"),
    (0, "COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbMacIndex"),
)
if mibBuilder.loadTexts:
    coDeviceIfFdbEntry.setStatus("current")


class _CoDevIfFdbMacIndex_Type(Integer32):
    """Custom type coDevIfFdbMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDevIfFdbMacIndex_Type.__name__ = "Integer32"
_CoDevIfFdbMacIndex_Object = MibTableColumn
coDevIfFdbMacIndex = _CoDevIfFdbMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 1),
    _CoDevIfFdbMacIndex_Type()
)
coDevIfFdbMacIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevIfFdbMacIndex.setStatus("current")
_CoDevIfFdbMACAddress_Type = MacAddress
_CoDevIfFdbMACAddress_Object = MibTableColumn
coDevIfFdbMACAddress = _CoDevIfFdbMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 2),
    _CoDevIfFdbMACAddress_Type()
)
coDevIfFdbMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfFdbMACAddress.setStatus("current")
_CoDevIfFdbAuthorized_Type = TruthValue
_CoDevIfFdbAuthorized_Object = MibTableColumn
coDevIfFdbAuthorized = _CoDevIfFdbAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 3),
    _CoDevIfFdbAuthorized_Type()
)
coDevIfFdbAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfFdbAuthorized.setStatus("current")
_CoDevIfFdbAgeing_Type = Integer32
_CoDevIfFdbAgeing_Object = MibTableColumn
coDevIfFdbAgeing = _CoDevIfFdbAgeing_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 3, 1, 1, 4),
    _CoDevIfFdbAgeing_Type()
)
coDevIfFdbAgeing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfFdbAgeing.setStatus("current")
if mibBuilder.loadTexts:
    coDevIfFdbAgeing.setUnits("msec")
_ColubrisDeviceIfMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisDeviceIfMIBNotificationPrefix = _ColubrisDeviceIfMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 2)
)
_ColubrisDeviceIfMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisDeviceIfMIBNotifications = _ColubrisDeviceIfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 2, 0)
)
_ColubrisDeviceIfMIBConformance_ObjectIdentity = ObjectIdentity
colubrisDeviceIfMIBConformance = _ColubrisDeviceIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 3)
)
_ColubrisDeviceIfMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisDeviceIfMIBCompliances = _ColubrisDeviceIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 1)
)
_ColubrisDeviceIfMIBGroups_ObjectIdentity = ObjectIdentity
colubrisDeviceIfMIBGroups = _ColubrisDeviceIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2)
)
coDeviceIfStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-IF-MIB",
     "coDeviceIfStatsEntry")
)
coDeviceIfStatsEntry.setIndexNames(*coDeviceIfStatusEntry.getIndexNames())

# Managed Objects groups

colubrisDeviceIfStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 1)
)
colubrisDeviceIfStatusMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaFriendlyInterfaceName"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaType"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaVLAN"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIpAddress"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaNetworkMask"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaMACAddress"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaState"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaPowerForwardingStatus"))
)
if mibBuilder.loadTexts:
    colubrisDeviceIfStatusMIBGroup.setStatus("current")

colubrisDeviceIfStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 2)
)
colubrisDeviceIfStatsMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxBytes"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxPackets"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxErrors"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxBytes"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxPackets"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxErrors"))
)
if mibBuilder.loadTexts:
    colubrisDeviceIfStatsMIBGroup.setStatus("current")

colubrisDeviceIfFdbMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 3)
)
colubrisDeviceIfFdbMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbMACAddress"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbAuthorized"),
        ("COLUBRIS-DEVICE-IF-MIB", "coDevIfFdbAgeing"))
)
if mibBuilder.loadTexts:
    colubrisDeviceIfFdbMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisDeviceIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisDeviceIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-DEVICE-IF-MIB",
    **{"colubrisDeviceIfMIB": colubrisDeviceIfMIB,
       "colubrisDeviceIfMIBObjects": colubrisDeviceIfMIBObjects,
       "coDeviceIfStatusGroup": coDeviceIfStatusGroup,
       "coDeviceIfStatusTable": coDeviceIfStatusTable,
       "coDeviceIfStatusEntry": coDeviceIfStatusEntry,
       "coDevIfStaIfIndex": coDevIfStaIfIndex,
       "coDevIfStaFriendlyInterfaceName": coDevIfStaFriendlyInterfaceName,
       "coDevIfStaType": coDevIfStaType,
       "coDevIfStaVLAN": coDevIfStaVLAN,
       "coDevIfStaIpAddress": coDevIfStaIpAddress,
       "coDevIfStaNetworkMask": coDevIfStaNetworkMask,
       "coDevIfStaMACAddress": coDevIfStaMACAddress,
       "coDevIfStaState": coDevIfStaState,
       "coDevIfStaPowerForwardingStatus": coDevIfStaPowerForwardingStatus,
       "coDeviceIfStatsGroup": coDeviceIfStatsGroup,
       "coDeviceIfStatsTable": coDeviceIfStatsTable,
       "coDeviceIfStatsEntry": coDeviceIfStatsEntry,
       "coDevIfStsRxBytes": coDevIfStsRxBytes,
       "coDevIfStsRxPackets": coDevIfStsRxPackets,
       "coDevIfStsRxErrors": coDevIfStsRxErrors,
       "coDevIfStsTxBytes": coDevIfStsTxBytes,
       "coDevIfStsTxPackets": coDevIfStsTxPackets,
       "coDevIfStsTxErrors": coDevIfStsTxErrors,
       "coDeviceIfFdbGroup": coDeviceIfFdbGroup,
       "coDeviceIfFdbTable": coDeviceIfFdbTable,
       "coDeviceIfFdbEntry": coDeviceIfFdbEntry,
       "coDevIfFdbMacIndex": coDevIfFdbMacIndex,
       "coDevIfFdbMACAddress": coDevIfFdbMACAddress,
       "coDevIfFdbAuthorized": coDevIfFdbAuthorized,
       "coDevIfFdbAgeing": coDevIfFdbAgeing,
       "colubrisDeviceIfMIBNotificationPrefix": colubrisDeviceIfMIBNotificationPrefix,
       "colubrisDeviceIfMIBNotifications": colubrisDeviceIfMIBNotifications,
       "colubrisDeviceIfMIBConformance": colubrisDeviceIfMIBConformance,
       "colubrisDeviceIfMIBCompliances": colubrisDeviceIfMIBCompliances,
       "colubrisDeviceIfMIBCompliance": colubrisDeviceIfMIBCompliance,
       "colubrisDeviceIfMIBGroups": colubrisDeviceIfMIBGroups,
       "colubrisDeviceIfStatusMIBGroup": colubrisDeviceIfStatusMIBGroup,
       "colubrisDeviceIfStatsMIBGroup": colubrisDeviceIfStatsMIBGroup,
       "colubrisDeviceIfFdbMIBGroup": colubrisDeviceIfFdbMIBGroup}
)
