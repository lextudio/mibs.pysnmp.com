# SNMP MIB module (ALVARION-DEVICE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-DEVICE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:34 2024
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
    "ALVARION-DEVICE-MIB",
    "coDevDisIndex")

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

alvarionDeviceIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlvarionDeviceIfMIBObjects_ObjectIdentity = ObjectIdentity
alvarionDeviceIfMIBObjects = _AlvarionDeviceIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1)
)
_CoDeviceIfStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceIfStatusGroup = _CoDeviceIfStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1)
)
_CoDeviceIfStatusTable_Object = MibTable
coDeviceIfStatusTable = _CoDeviceIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceIfStatusTable.setStatus("current")
_CoDeviceIfStatusEntry_Object = MibTableRow
coDeviceIfStatusEntry = _CoDeviceIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1)
)
coDeviceIfStatusEntry.setIndexNames(
    (0, "ALVARION-DEVICE-MIB", "coDevDisIndex"),
    (0, "ALVARION-DEVICE-IF-MIB", "coDevIfStaIfIndex"),
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
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 1),
    _CoDevIfStaIfIndex_Type()
)
coDevIfStaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDevIfStaIfIndex.setStatus("current")
_CoDevIfStaFriendlyInterfaceName_Type = DisplayString
_CoDevIfStaFriendlyInterfaceName_Object = MibTableColumn
coDevIfStaFriendlyInterfaceName = _CoDevIfStaFriendlyInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 4),
    _CoDevIfStaVLAN_Type()
)
coDevIfStaVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaVLAN.setStatus("current")
_CoDevIfStaIpAddress_Type = IpAddress
_CoDevIfStaIpAddress_Object = MibTableColumn
coDevIfStaIpAddress = _CoDevIfStaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 5),
    _CoDevIfStaIpAddress_Type()
)
coDevIfStaIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaIpAddress.setStatus("current")
_CoDevIfStaNetworkMask_Type = IpAddress
_CoDevIfStaNetworkMask_Object = MibTableColumn
coDevIfStaNetworkMask = _CoDevIfStaNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 6),
    _CoDevIfStaNetworkMask_Type()
)
coDevIfStaNetworkMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaNetworkMask.setStatus("current")
_CoDevIfStaMACAddress_Type = MacAddress
_CoDevIfStaMACAddress_Object = MibTableColumn
coDevIfStaMACAddress = _CoDevIfStaMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 1, 1, 1, 8),
    _CoDevIfStaState_Type()
)
coDevIfStaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStaState.setStatus("current")
_CoDeviceIfStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceIfStatsGroup = _CoDeviceIfStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2)
)
_CoDeviceIfStatsTable_Object = MibTable
coDeviceIfStatsTable = _CoDeviceIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceIfStatsTable.setStatus("current")
_CoDeviceIfStatsEntry_Object = MibTableRow
coDeviceIfStatsEntry = _CoDeviceIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceIfStatsEntry.setStatus("current")
_CoDevIfStsRxBytes_Type = Counter64
_CoDevIfStsRxBytes_Object = MibTableColumn
coDevIfStsRxBytes = _CoDevIfStsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1, 1, 1),
    _CoDevIfStsRxBytes_Type()
)
coDevIfStsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsRxBytes.setStatus("current")
_CoDevIfStsRxPackets_Type = Counter32
_CoDevIfStsRxPackets_Object = MibTableColumn
coDevIfStsRxPackets = _CoDevIfStsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1, 1, 2),
    _CoDevIfStsRxPackets_Type()
)
coDevIfStsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsRxPackets.setStatus("current")
_CoDevIfStsRxErrors_Type = Counter32
_CoDevIfStsRxErrors_Object = MibTableColumn
coDevIfStsRxErrors = _CoDevIfStsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1, 1, 3),
    _CoDevIfStsRxErrors_Type()
)
coDevIfStsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsRxErrors.setStatus("current")
_CoDevIfStsTxBytes_Type = Counter64
_CoDevIfStsTxBytes_Object = MibTableColumn
coDevIfStsTxBytes = _CoDevIfStsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1, 1, 4),
    _CoDevIfStsTxBytes_Type()
)
coDevIfStsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsTxBytes.setStatus("current")
_CoDevIfStsTxPackets_Type = Counter32
_CoDevIfStsTxPackets_Object = MibTableColumn
coDevIfStsTxPackets = _CoDevIfStsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1, 1, 5),
    _CoDevIfStsTxPackets_Type()
)
coDevIfStsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsTxPackets.setStatus("current")
_CoDevIfStsTxErrors_Type = Counter32
_CoDevIfStsTxErrors_Object = MibTableColumn
coDevIfStsTxErrors = _CoDevIfStsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 1, 2, 1, 1, 6),
    _CoDevIfStsTxErrors_Type()
)
coDevIfStsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDevIfStsTxErrors.setStatus("current")
_AlvarionDeviceIfMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
alvarionDeviceIfMIBNotificationPrefix = _AlvarionDeviceIfMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 2)
)
_AlvarionDeviceIfMIBNotifications_ObjectIdentity = ObjectIdentity
alvarionDeviceIfMIBNotifications = _AlvarionDeviceIfMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 2, 0)
)
_AlvarionDeviceIfMIBConformance_ObjectIdentity = ObjectIdentity
alvarionDeviceIfMIBConformance = _AlvarionDeviceIfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 3)
)
_AlvarionDeviceIfMIBCompliances_ObjectIdentity = ObjectIdentity
alvarionDeviceIfMIBCompliances = _AlvarionDeviceIfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 3, 1)
)
_AlvarionDeviceIfMIBGroups_ObjectIdentity = ObjectIdentity
alvarionDeviceIfMIBGroups = _AlvarionDeviceIfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 3, 2)
)
coDeviceIfStatusEntry.registerAugmentions(
    ("ALVARION-DEVICE-IF-MIB",
     "coDeviceIfStatsEntry")
)
coDeviceIfStatsEntry.setIndexNames(*coDeviceIfStatusEntry.getIndexNames())

# Managed Objects groups

alvarionDeviceIfStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 3, 2, 1)
)
alvarionDeviceIfStatusMIBGroup.setObjects(
      *(("ALVARION-DEVICE-IF-MIB", "coDevIfStaFriendlyInterfaceName"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStaType"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStaVLAN"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStaIpAddress"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStaNetworkMask"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStaMACAddress"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStaState"))
)
if mibBuilder.loadTexts:
    alvarionDeviceIfStatusMIBGroup.setStatus("current")

alvarionDeviceIfStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 3, 2, 2)
)
alvarionDeviceIfStatsMIBGroup.setObjects(
      *(("ALVARION-DEVICE-IF-MIB", "coDevIfStsRxBytes"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStsRxPackets"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStsRxErrors"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStsTxBytes"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStsTxPackets"),
        ("ALVARION-DEVICE-IF-MIB", "coDevIfStsTxErrors"))
)
if mibBuilder.loadTexts:
    alvarionDeviceIfStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alvarionDeviceIfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 24, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alvarionDeviceIfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-DEVICE-IF-MIB",
    **{"alvarionDeviceIfMIB": alvarionDeviceIfMIB,
       "alvarionDeviceIfMIBObjects": alvarionDeviceIfMIBObjects,
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
       "coDeviceIfStatsGroup": coDeviceIfStatsGroup,
       "coDeviceIfStatsTable": coDeviceIfStatsTable,
       "coDeviceIfStatsEntry": coDeviceIfStatsEntry,
       "coDevIfStsRxBytes": coDevIfStsRxBytes,
       "coDevIfStsRxPackets": coDevIfStsRxPackets,
       "coDevIfStsRxErrors": coDevIfStsRxErrors,
       "coDevIfStsTxBytes": coDevIfStsTxBytes,
       "coDevIfStsTxPackets": coDevIfStsTxPackets,
       "coDevIfStsTxErrors": coDevIfStsTxErrors,
       "alvarionDeviceIfMIBNotificationPrefix": alvarionDeviceIfMIBNotificationPrefix,
       "alvarionDeviceIfMIBNotifications": alvarionDeviceIfMIBNotifications,
       "alvarionDeviceIfMIBConformance": alvarionDeviceIfMIBConformance,
       "alvarionDeviceIfMIBCompliances": alvarionDeviceIfMIBCompliances,
       "alvarionDeviceIfMIBCompliance": alvarionDeviceIfMIBCompliance,
       "alvarionDeviceIfMIBGroups": alvarionDeviceIfMIBGroups,
       "alvarionDeviceIfStatusMIBGroup": alvarionDeviceIfStatusMIBGroup,
       "alvarionDeviceIfStatsMIBGroup": alvarionDeviceIfStatsMIBGroup}
)
