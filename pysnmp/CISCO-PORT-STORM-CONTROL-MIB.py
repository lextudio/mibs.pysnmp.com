# SNMP MIB module (CISCO-PORT-STORM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PORT-STORM-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:59 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoPortStormControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362)
)
ciscoPortStormControlMIB.setRevisions(
        ("2007-10-19 00:00",
         "2003-07-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CPortStormControlTrafficType(Integer32, TextualConvention):
    status = "current"
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
        *(("all", 4),
          ("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )



class CPortStormControlActionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("shutdown", 2))
    )



class CPortStormControlStatusType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("allTrafficFiltered", 4),
          ("forwarding", 2),
          ("inactive", 1),
          ("shutdown", 5),
          ("trafficTypeFiltered", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoPortStormControlMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoPortStormControlMIBNotifs = _CiscoPortStormControlMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 0)
)
_CpscNotificationsPrefix_ObjectIdentity = ObjectIdentity
cpscNotificationsPrefix = _CpscNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 1)
)
_CiscoPortStormControlMIBObjects_ObjectIdentity = ObjectIdentity
ciscoPortStormControlMIBObjects = _CiscoPortStormControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1)
)
_CpscConfigObjects_ObjectIdentity = ObjectIdentity
cpscConfigObjects = _CpscConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1)
)
_CpscThresholdTable_Object = MibTable
cpscThresholdTable = _CpscThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpscThresholdTable.setStatus("current")
_CpscThresholdEntry_Object = MibTableRow
cpscThresholdEntry = _CpscThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1)
)
cpscThresholdEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscTrafficType"),
)
if mibBuilder.loadTexts:
    cpscThresholdEntry.setStatus("current")
_CpscTrafficType_Type = CPortStormControlTrafficType
_CpscTrafficType_Object = MibTableColumn
cpscTrafficType = _CpscTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 1),
    _CpscTrafficType_Type()
)
cpscTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpscTrafficType.setStatus("current")


class _CpscUpperThreshold_Type(Integer32):
    """Custom type cpscUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CpscUpperThreshold_Type.__name__ = "Integer32"
_CpscUpperThreshold_Object = MibTableColumn
cpscUpperThreshold = _CpscUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 2),
    _CpscUpperThreshold_Type()
)
cpscUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpscUpperThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpscUpperThreshold.setUnits("0.01 Percentage")


class _CpscLowerThreshold_Type(Integer32):
    """Custom type cpscLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CpscLowerThreshold_Type.__name__ = "Integer32"
_CpscLowerThreshold_Object = MibTableColumn
cpscLowerThreshold = _CpscLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 1, 1, 3),
    _CpscLowerThreshold_Type()
)
cpscLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpscLowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpscLowerThreshold.setUnits("0.01 Percentage")
_CpscActionTable_Object = MibTable
cpscActionTable = _CpscActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpscActionTable.setStatus("current")
_CpscActionEntry_Object = MibTableRow
cpscActionEntry = _CpscActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1)
)
cpscActionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cpscActionEntry.setStatus("current")
_CpscAction_Type = CPortStormControlActionType
_CpscAction_Object = MibTableColumn
cpscAction = _CpscAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1, 1),
    _CpscAction_Type()
)
cpscAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpscAction.setStatus("current")


class _CpscNotificationControl_Type(Integer32):
    """Custom type cpscNotificationControl based on Integer32"""
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
        *(("both", 4),
          ("none", 1),
          ("stormCleared", 3),
          ("stormOccurred", 2))
    )


_CpscNotificationControl_Type.__name__ = "Integer32"
_CpscNotificationControl_Object = MibTableColumn
cpscNotificationControl = _CpscNotificationControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 2, 1, 2),
    _CpscNotificationControl_Type()
)
cpscNotificationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpscNotificationControl.setStatus("current")


class _CpscNotificationThreshold_Type(Integer32):
    """Custom type cpscNotificationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CpscNotificationThreshold_Type.__name__ = "Integer32"
_CpscNotificationThreshold_Object = MibScalar
cpscNotificationThreshold = _CpscNotificationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 1, 3),
    _CpscNotificationThreshold_Type()
)
cpscNotificationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpscNotificationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpscNotificationThreshold.setUnits("Notifications per Minute")
_CpscStatusObjects_ObjectIdentity = ObjectIdentity
cpscStatusObjects = _CpscStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2)
)
_CpscStatusTable_Object = MibTable
cpscStatusTable = _CpscStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpscStatusTable.setStatus("current")
_CpscStatusEntry_Object = MibTableRow
cpscStatusEntry = _CpscStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1)
)
cpscStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscTrafficType"),
)
if mibBuilder.loadTexts:
    cpscStatusEntry.setStatus("current")
_CpscStatus_Type = CPortStormControlStatusType
_CpscStatus_Object = MibTableColumn
cpscStatus = _CpscStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 1),
    _CpscStatus_Type()
)
cpscStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpscStatus.setStatus("current")


class _CpscCurrentLevel_Type(Integer32):
    """Custom type cpscCurrentLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CpscCurrentLevel_Type.__name__ = "Integer32"
_CpscCurrentLevel_Object = MibTableColumn
cpscCurrentLevel = _CpscCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 2),
    _CpscCurrentLevel_Type()
)
cpscCurrentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpscCurrentLevel.setStatus("current")
if mibBuilder.loadTexts:
    cpscCurrentLevel.setUnits("0.01 Percentage")
_CpscSuppressedPacket_Type = Counter64
_CpscSuppressedPacket_Object = MibTableColumn
cpscSuppressedPacket = _CpscSuppressedPacket_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 1, 1, 3),
    _CpscSuppressedPacket_Type()
)
cpscSuppressedPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpscSuppressedPacket.setStatus("current")
_CpscHistoryTable_Object = MibTable
cpscHistoryTable = _CpscHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cpscHistoryTable.setStatus("current")
_CpscHistoryEntry_Object = MibTableRow
cpscHistoryEntry = _CpscHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1)
)
cpscHistoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryTrafficType"),
    (0, "CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryIndex"),
)
if mibBuilder.loadTexts:
    cpscHistoryEntry.setStatus("current")
_CpscHistoryTrafficType_Type = CPortStormControlTrafficType
_CpscHistoryTrafficType_Object = MibTableColumn
cpscHistoryTrafficType = _CpscHistoryTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 1),
    _CpscHistoryTrafficType_Type()
)
cpscHistoryTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpscHistoryTrafficType.setStatus("current")


class _CpscHistoryIndex_Type(Integer32):
    """Custom type cpscHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CpscHistoryIndex_Type.__name__ = "Integer32"
_CpscHistoryIndex_Object = MibTableColumn
cpscHistoryIndex = _CpscHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 2),
    _CpscHistoryIndex_Type()
)
cpscHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpscHistoryIndex.setStatus("current")
_CpscHistoryStartTime_Type = TimeStamp
_CpscHistoryStartTime_Object = MibTableColumn
cpscHistoryStartTime = _CpscHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 3),
    _CpscHistoryStartTime_Type()
)
cpscHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpscHistoryStartTime.setStatus("current")
_CpscHistoryEndTime_Type = TimeStamp
_CpscHistoryEndTime_Object = MibTableColumn
cpscHistoryEndTime = _CpscHistoryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 1, 2, 2, 1, 4),
    _CpscHistoryEndTime_Type()
)
cpscHistoryEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpscHistoryEndTime.setStatus("current")
_CiscoPortStormControlMIBConform_ObjectIdentity = ObjectIdentity
ciscoPortStormControlMIBConform = _CiscoPortStormControlMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2)
)
_CiscoPortStormControlMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoPortStormControlMIBCompliances = _CiscoPortStormControlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1)
)
_CiscoPortStormControlMIBGroups_ObjectIdentity = ObjectIdentity
ciscoPortStormControlMIBGroups = _CiscoPortStormControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2)
)

# Managed Objects groups

cpscConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 1)
)
cpscConfigurationGroup.setObjects(
      *(("CISCO-PORT-STORM-CONTROL-MIB", "cpscUpperThreshold"),
        ("CISCO-PORT-STORM-CONTROL-MIB", "cpscLowerThreshold"),
        ("CISCO-PORT-STORM-CONTROL-MIB", "cpscAction"))
)
if mibBuilder.loadTexts:
    cpscConfigurationGroup.setStatus("current")

cpscStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 2)
)
cpscStatusGroup.setObjects(
      *(("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus"),
        ("CISCO-PORT-STORM-CONTROL-MIB", "cpscCurrentLevel"))
)
if mibBuilder.loadTexts:
    cpscStatusGroup.setStatus("current")

cpscNotifConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 4)
)
cpscNotifConfigurationGroup.setObjects(
      *(("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationControl"),
        ("CISCO-PORT-STORM-CONTROL-MIB", "cpscNotificationThreshold"))
)
if mibBuilder.loadTexts:
    cpscNotifConfigurationGroup.setStatus("current")

cpscStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 5)
)
cpscStatisticsGroup.setObjects(
    ("CISCO-PORT-STORM-CONTROL-MIB", "cpscSuppressedPacket")
)
if mibBuilder.loadTexts:
    cpscStatisticsGroup.setStatus("current")

cpscHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 6)
)
cpscHistoryGroup.setObjects(
      *(("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryStartTime"),
        ("CISCO-PORT-STORM-CONTROL-MIB", "cpscHistoryEndTime"))
)
if mibBuilder.loadTexts:
    cpscHistoryGroup.setStatus("current")


# Notification objects

cpscEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 1, 1)
)
cpscEvent.setObjects(
    ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus")
)
if mibBuilder.loadTexts:
    cpscEvent.setStatus(
        "deprecated"
    )

cpscEventRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 0, 2)
)
cpscEventRev1.setObjects(
    ("CISCO-PORT-STORM-CONTROL-MIB", "cpscStatus")
)
if mibBuilder.loadTexts:
    cpscEventRev1.setStatus(
        "current"
    )


# Notifications groups

cpscNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 3)
)
cpscNotificationGroup.setObjects(
    ("CISCO-PORT-STORM-CONTROL-MIB", "cpscEvent")
)
if mibBuilder.loadTexts:
    cpscNotificationGroup.setStatus(
        "deprecated"
    )

cpscNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 2, 7)
)
cpscNotificationGroupRev1.setObjects(
    ("CISCO-PORT-STORM-CONTROL-MIB", "cpscEventRev1")
)
if mibBuilder.loadTexts:
    cpscNotificationGroupRev1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoPortStormControlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoPortStormControlMIBCompliance.setStatus(
        "deprecated"
    )

ciscoPortStormControlMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 362, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoPortStormControlMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PORT-STORM-CONTROL-MIB",
    **{"CPortStormControlTrafficType": CPortStormControlTrafficType,
       "CPortStormControlActionType": CPortStormControlActionType,
       "CPortStormControlStatusType": CPortStormControlStatusType,
       "ciscoPortStormControlMIB": ciscoPortStormControlMIB,
       "ciscoPortStormControlMIBNotifs": ciscoPortStormControlMIBNotifs,
       "cpscNotificationsPrefix": cpscNotificationsPrefix,
       "cpscEvent": cpscEvent,
       "cpscEventRev1": cpscEventRev1,
       "ciscoPortStormControlMIBObjects": ciscoPortStormControlMIBObjects,
       "cpscConfigObjects": cpscConfigObjects,
       "cpscThresholdTable": cpscThresholdTable,
       "cpscThresholdEntry": cpscThresholdEntry,
       "cpscTrafficType": cpscTrafficType,
       "cpscUpperThreshold": cpscUpperThreshold,
       "cpscLowerThreshold": cpscLowerThreshold,
       "cpscActionTable": cpscActionTable,
       "cpscActionEntry": cpscActionEntry,
       "cpscAction": cpscAction,
       "cpscNotificationControl": cpscNotificationControl,
       "cpscNotificationThreshold": cpscNotificationThreshold,
       "cpscStatusObjects": cpscStatusObjects,
       "cpscStatusTable": cpscStatusTable,
       "cpscStatusEntry": cpscStatusEntry,
       "cpscStatus": cpscStatus,
       "cpscCurrentLevel": cpscCurrentLevel,
       "cpscSuppressedPacket": cpscSuppressedPacket,
       "cpscHistoryTable": cpscHistoryTable,
       "cpscHistoryEntry": cpscHistoryEntry,
       "cpscHistoryTrafficType": cpscHistoryTrafficType,
       "cpscHistoryIndex": cpscHistoryIndex,
       "cpscHistoryStartTime": cpscHistoryStartTime,
       "cpscHistoryEndTime": cpscHistoryEndTime,
       "ciscoPortStormControlMIBConform": ciscoPortStormControlMIBConform,
       "ciscoPortStormControlMIBCompliances": ciscoPortStormControlMIBCompliances,
       "ciscoPortStormControlMIBCompliance": ciscoPortStormControlMIBCompliance,
       "ciscoPortStormControlMIBComplianceRev1": ciscoPortStormControlMIBComplianceRev1,
       "ciscoPortStormControlMIBGroups": ciscoPortStormControlMIBGroups,
       "cpscConfigurationGroup": cpscConfigurationGroup,
       "cpscStatusGroup": cpscStatusGroup,
       "cpscNotificationGroup": cpscNotificationGroup,
       "cpscNotifConfigurationGroup": cpscNotifConfigurationGroup,
       "cpscStatisticsGroup": cpscStatisticsGroup,
       "cpscHistoryGroup": cpscHistoryGroup,
       "cpscNotificationGroupRev1": cpscNotificationGroupRev1}
)
