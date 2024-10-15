# SNMP MIB module (CISCO-APPLIANCE-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-APPLIANCE-REDUNDANCY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:37 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ciscoApplianceRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CarRedundancyState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("activeLostNetwork", 7),
          ("activeLostStandby", 6),
          ("notConfigured", 1),
          ("preStandby", 4),
          ("standby", 5),
          ("standbyLostNetwork", 8),
          ("starting", 2))
    )



class CarSwitchOverReason(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forcedSwitchOver", 2),
          ("lossConnWithActive", 1),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoApplRedundancyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoApplRedundancyMIBObjects = _CiscoApplRedundancyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1)
)
_CarConfigObjects_ObjectIdentity = ObjectIdentity
carConfigObjects = _CarConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1)
)
_CarRedundancySyncInterval_Type = TimeInterval
_CarRedundancySyncInterval_Object = MibScalar
carRedundancySyncInterval = _CarRedundancySyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 1),
    _CarRedundancySyncInterval_Type()
)
carRedundancySyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRedundancySyncInterval.setStatus("current")
_CarRedundancyCheckInterval_Type = TimeInterval
_CarRedundancyCheckInterval_Object = MibScalar
carRedundancyCheckInterval = _CarRedundancyCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 2),
    _CarRedundancyCheckInterval_Type()
)
carRedundancyCheckInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRedundancyCheckInterval.setStatus("current")


class _CarRedundancyState_Type(CarRedundancyState):
    """Custom type carRedundancyState based on CarRedundancyState"""


_CarRedundancyState_Object = MibScalar
carRedundancyState = _CarRedundancyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 3),
    _CarRedundancyState_Type()
)
carRedundancyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carRedundancyState.setStatus("current")


class _CarNotificationEnabled_Type(TruthValue):
    """Custom type carNotificationEnabled based on TruthValue"""


_CarNotificationEnabled_Object = MibScalar
carNotificationEnabled = _CarNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 4),
    _CarNotificationEnabled_Type()
)
carNotificationEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carNotificationEnabled.setStatus("current")
_CarHAAddressTable_Object = MibTable
carHAAddressTable = _CarHAAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5)
)
if mibBuilder.loadTexts:
    carHAAddressTable.setStatus("current")
_CarHAAddressEntry_Object = MibTableRow
carHAAddressEntry = _CarHAAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1)
)
carHAAddressEntry.setIndexNames(
    (0, "CISCO-APPLIANCE-REDUNDANCY-MIB", "carHAAddrTableIndex"),
)
if mibBuilder.loadTexts:
    carHAAddressEntry.setStatus("current")
_CarHAAddrTableIndex_Type = InterfaceIndexOrZero
_CarHAAddrTableIndex_Object = MibTableColumn
carHAAddrTableIndex = _CarHAAddrTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 1),
    _CarHAAddrTableIndex_Type()
)
carHAAddrTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    carHAAddrTableIndex.setStatus("current")
_CarVirtualAddressType_Type = InetAddressType
_CarVirtualAddressType_Object = MibTableColumn
carVirtualAddressType = _CarVirtualAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 2),
    _CarVirtualAddressType_Type()
)
carVirtualAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carVirtualAddressType.setStatus("current")
_CarVirtualAddress_Type = InetAddress
_CarVirtualAddress_Object = MibTableColumn
carVirtualAddress = _CarVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 3),
    _CarVirtualAddress_Type()
)
carVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carVirtualAddress.setStatus("current")
_CarMyAddressType_Type = InetAddressType
_CarMyAddressType_Object = MibTableColumn
carMyAddressType = _CarMyAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 4),
    _CarMyAddressType_Type()
)
carMyAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carMyAddressType.setStatus("current")
_CarMyAddress_Type = InetAddress
_CarMyAddress_Object = MibTableColumn
carMyAddress = _CarMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 5),
    _CarMyAddress_Type()
)
carMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carMyAddress.setStatus("current")
_CarPeerAddressType_Type = InetAddressType
_CarPeerAddressType_Object = MibTableColumn
carPeerAddressType = _CarPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 6),
    _CarPeerAddressType_Type()
)
carPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carPeerAddressType.setStatus("current")
_CarPeerAddress_Type = InetAddress
_CarPeerAddress_Object = MibTableColumn
carPeerAddress = _CarPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 1, 5, 1, 7),
    _CarPeerAddress_Type()
)
carPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carPeerAddress.setStatus("current")
_CarSwitchOverObjects_ObjectIdentity = ObjectIdentity
carSwitchOverObjects = _CarSwitchOverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2)
)
_CarLastSwitchOverReason_Type = CarSwitchOverReason
_CarLastSwitchOverReason_Object = MibScalar
carLastSwitchOverReason = _CarLastSwitchOverReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 1),
    _CarLastSwitchOverReason_Type()
)
carLastSwitchOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carLastSwitchOverReason.setStatus("current")
_CarLastSwitchOverTime_Type = DateAndTime
_CarLastSwitchOverTime_Object = MibScalar
carLastSwitchOverTime = _CarLastSwitchOverTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 2),
    _CarLastSwitchOverTime_Type()
)
carLastSwitchOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carLastSwitchOverTime.setStatus("current")
_CarTotalSwitchOvers_Type = Counter32
_CarTotalSwitchOvers_Object = MibScalar
carTotalSwitchOvers = _CarTotalSwitchOvers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 3),
    _CarTotalSwitchOvers_Type()
)
carTotalSwitchOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carTotalSwitchOvers.setStatus("current")


class _CarMaxSwitchOverHistoryRecords_Type(Unsigned32):
    """Custom type carMaxSwitchOverHistoryRecords based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CarMaxSwitchOverHistoryRecords_Type.__name__ = "Unsigned32"
_CarMaxSwitchOverHistoryRecords_Object = MibScalar
carMaxSwitchOverHistoryRecords = _CarMaxSwitchOverHistoryRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 4),
    _CarMaxSwitchOverHistoryRecords_Type()
)
carMaxSwitchOverHistoryRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carMaxSwitchOverHistoryRecords.setStatus("current")
_CarSwitchOverHistoryTable_Object = MibTable
carSwitchOverHistoryTable = _CarSwitchOverHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5)
)
if mibBuilder.loadTexts:
    carSwitchOverHistoryTable.setStatus("current")
_CarSwitchOverHistEntry_Object = MibTableRow
carSwitchOverHistEntry = _CarSwitchOverHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1)
)
carSwitchOverHistEntry.setIndexNames(
    (0, "CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistTableIndex"),
)
if mibBuilder.loadTexts:
    carSwitchOverHistEntry.setStatus("current")


class _CarSWHistTableIndex_Type(Unsigned32):
    """Custom type carSWHistTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CarSWHistTableIndex_Type.__name__ = "Unsigned32"
_CarSWHistTableIndex_Object = MibTableColumn
carSWHistTableIndex = _CarSWHistTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 1),
    _CarSWHistTableIndex_Type()
)
carSWHistTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    carSWHistTableIndex.setStatus("current")
_CarSWHistActiveNodeAddressType_Type = InetAddressType
_CarSWHistActiveNodeAddressType_Object = MibTableColumn
carSWHistActiveNodeAddressType = _CarSWHistActiveNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 2),
    _CarSWHistActiveNodeAddressType_Type()
)
carSWHistActiveNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carSWHistActiveNodeAddressType.setStatus("current")
_CarSWHistActiveNodeAddress_Type = InetAddress
_CarSWHistActiveNodeAddress_Object = MibTableColumn
carSWHistActiveNodeAddress = _CarSWHistActiveNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 3),
    _CarSWHistActiveNodeAddress_Type()
)
carSWHistActiveNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carSWHistActiveNodeAddress.setStatus("current")
_CarSWHistStandbyNodeAddressType_Type = InetAddressType
_CarSWHistStandbyNodeAddressType_Object = MibTableColumn
carSWHistStandbyNodeAddressType = _CarSWHistStandbyNodeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 4),
    _CarSWHistStandbyNodeAddressType_Type()
)
carSWHistStandbyNodeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carSWHistStandbyNodeAddressType.setStatus("current")
_CarSWHistStandbyNodeAddress_Type = InetAddress
_CarSWHistStandbyNodeAddress_Object = MibTableColumn
carSWHistStandbyNodeAddress = _CarSWHistStandbyNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 5),
    _CarSWHistStandbyNodeAddress_Type()
)
carSWHistStandbyNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carSWHistStandbyNodeAddress.setStatus("current")
_CarSWHistEventTime_Type = DateAndTime
_CarSWHistEventTime_Object = MibTableColumn
carSWHistEventTime = _CarSWHistEventTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 6),
    _CarSWHistEventTime_Type()
)
carSWHistEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carSWHistEventTime.setStatus("current")
_CarSWHistEventReason_Type = CarSwitchOverReason
_CarSWHistEventReason_Object = MibTableColumn
carSWHistEventReason = _CarSWHistEventReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 1, 2, 5, 1, 7),
    _CarSWHistEventReason_Type()
)
carSWHistEventReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    carSWHistEventReason.setStatus("current")
_CarHAMIBNotifPrefix_ObjectIdentity = ObjectIdentity
carHAMIBNotifPrefix = _CarHAMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 2)
)
_CarHAMIBNotifications_ObjectIdentity = ObjectIdentity
carHAMIBNotifications = _CarHAMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 2, 0)
)
_CiscoHAMIBConformance_ObjectIdentity = ObjectIdentity
ciscoHAMIBConformance = _CiscoHAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 3)
)
_CiscoHAMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoHAMIBCompliances = _CiscoHAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 1)
)
_CiscoHAMIBGroups_ObjectIdentity = ObjectIdentity
ciscoHAMIBGroups = _CiscoHAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2)
)

# Managed Objects groups

ciscoHAConfigDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2, 1)
)
ciscoHAConfigDataGroup.setObjects(
      *(("CISCO-APPLIANCE-REDUNDANCY-MIB", "carVirtualAddressType"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carVirtualAddress"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carMyAddressType"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carMyAddress"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carPeerAddressType"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carPeerAddress"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carRedundancySyncInterval"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carRedundancyCheckInterval"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carRedundancyState"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carNotificationEnabled"))
)
if mibBuilder.loadTexts:
    ciscoHAConfigDataGroup.setStatus("current")

ciscoHASwitchOverDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2, 2)
)
ciscoHASwitchOverDataGroup.setObjects(
      *(("CISCO-APPLIANCE-REDUNDANCY-MIB", "carLastSwitchOverReason"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carLastSwitchOverTime"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carTotalSwitchOvers"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carMaxSwitchOverHistoryRecords"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddressType"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddress"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddressType"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddress"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventTime"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventReason"))
)
if mibBuilder.loadTexts:
    ciscoHASwitchOverDataGroup.setStatus("current")


# Notification objects

carSwitchOverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 2, 0, 1)
)
carSwitchOverNotification.setObjects(
      *(("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventTime"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistEventReason"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddressType"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistActiveNodeAddress"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddressType"),
        ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSWHistStandbyNodeAddress"))
)
if mibBuilder.loadTexts:
    carSwitchOverNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoHAExceptionNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 2, 3)
)
ciscoHAExceptionNotifGroup.setObjects(
    ("CISCO-APPLIANCE-REDUNDANCY-MIB", "carSwitchOverNotification")
)
if mibBuilder.loadTexts:
    ciscoHAExceptionNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoHAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 458, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoHAMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-APPLIANCE-REDUNDANCY-MIB",
    **{"CarRedundancyState": CarRedundancyState,
       "CarSwitchOverReason": CarSwitchOverReason,
       "ciscoApplianceRedundancyMIB": ciscoApplianceRedundancyMIB,
       "ciscoApplRedundancyMIBObjects": ciscoApplRedundancyMIBObjects,
       "carConfigObjects": carConfigObjects,
       "carRedundancySyncInterval": carRedundancySyncInterval,
       "carRedundancyCheckInterval": carRedundancyCheckInterval,
       "carRedundancyState": carRedundancyState,
       "carNotificationEnabled": carNotificationEnabled,
       "carHAAddressTable": carHAAddressTable,
       "carHAAddressEntry": carHAAddressEntry,
       "carHAAddrTableIndex": carHAAddrTableIndex,
       "carVirtualAddressType": carVirtualAddressType,
       "carVirtualAddress": carVirtualAddress,
       "carMyAddressType": carMyAddressType,
       "carMyAddress": carMyAddress,
       "carPeerAddressType": carPeerAddressType,
       "carPeerAddress": carPeerAddress,
       "carSwitchOverObjects": carSwitchOverObjects,
       "carLastSwitchOverReason": carLastSwitchOverReason,
       "carLastSwitchOverTime": carLastSwitchOverTime,
       "carTotalSwitchOvers": carTotalSwitchOvers,
       "carMaxSwitchOverHistoryRecords": carMaxSwitchOverHistoryRecords,
       "carSwitchOverHistoryTable": carSwitchOverHistoryTable,
       "carSwitchOverHistEntry": carSwitchOverHistEntry,
       "carSWHistTableIndex": carSWHistTableIndex,
       "carSWHistActiveNodeAddressType": carSWHistActiveNodeAddressType,
       "carSWHistActiveNodeAddress": carSWHistActiveNodeAddress,
       "carSWHistStandbyNodeAddressType": carSWHistStandbyNodeAddressType,
       "carSWHistStandbyNodeAddress": carSWHistStandbyNodeAddress,
       "carSWHistEventTime": carSWHistEventTime,
       "carSWHistEventReason": carSWHistEventReason,
       "carHAMIBNotifPrefix": carHAMIBNotifPrefix,
       "carHAMIBNotifications": carHAMIBNotifications,
       "carSwitchOverNotification": carSwitchOverNotification,
       "ciscoHAMIBConformance": ciscoHAMIBConformance,
       "ciscoHAMIBCompliances": ciscoHAMIBCompliances,
       "ciscoHAMIBCompliance": ciscoHAMIBCompliance,
       "ciscoHAMIBGroups": ciscoHAMIBGroups,
       "ciscoHAConfigDataGroup": ciscoHAConfigDataGroup,
       "ciscoHASwitchOverDataGroup": ciscoHASwitchOverDataGroup,
       "ciscoHAExceptionNotifGroup": ciscoHAExceptionNotifGroup}
)
