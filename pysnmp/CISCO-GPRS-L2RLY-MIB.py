# SNMP MIB module (CISCO-GPRS-L2RLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GPRS-L2RLY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:58 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoGprsL2rlyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGprsL2rlyObjects_ObjectIdentity = ObjectIdentity
ciscoGprsL2rlyObjects = _CiscoGprsL2rlyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1)
)
_CiscoGprsL2rlyConfig_ObjectIdentity = ObjectIdentity
ciscoGprsL2rlyConfig = _CiscoGprsL2rlyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1)
)


class _CgprsL2rlyUid_Type(Integer32):
    """Custom type cgprsL2rlyUid based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CgprsL2rlyUid_Type.__name__ = "Integer32"
_CgprsL2rlyUid_Object = MibScalar
cgprsL2rlyUid = _CgprsL2rlyUid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 1),
    _CgprsL2rlyUid_Type()
)
cgprsL2rlyUid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsL2rlyUid.setStatus("current")


class _CgprsL2rlyUnitType_Type(Integer32):
    """Custom type cgprsL2rlyUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("datacomUnit", 1),
          ("telecomUnit", 2))
    )


_CgprsL2rlyUnitType_Type.__name__ = "Integer32"
_CgprsL2rlyUnitType_Object = MibScalar
cgprsL2rlyUnitType = _CgprsL2rlyUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 2),
    _CgprsL2rlyUnitType_Type()
)
cgprsL2rlyUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsL2rlyUnitType.setStatus("current")


class _CgprsL2rlyEchoTimer_Type(Integer32):
    """Custom type cgprsL2rlyEchoTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CgprsL2rlyEchoTimer_Type.__name__ = "Integer32"
_CgprsL2rlyEchoTimer_Object = MibScalar
cgprsL2rlyEchoTimer = _CgprsL2rlyEchoTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 3),
    _CgprsL2rlyEchoTimer_Type()
)
cgprsL2rlyEchoTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsL2rlyEchoTimer.setStatus("current")
if mibBuilder.loadTexts:
    cgprsL2rlyEchoTimer.setUnits("seconds")
_CgprsL2rlyFlowControlFlag_Type = TruthValue
_CgprsL2rlyFlowControlFlag_Object = MibScalar
cgprsL2rlyFlowControlFlag = _CgprsL2rlyFlowControlFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 4),
    _CgprsL2rlyFlowControlFlag_Type()
)
cgprsL2rlyFlowControlFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsL2rlyFlowControlFlag.setStatus("current")


class _CgprsL2rlyDroppedPktsMonTime_Type(Integer32):
    """Custom type cgprsL2rlyDroppedPktsMonTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsL2rlyDroppedPktsMonTime_Type.__name__ = "Integer32"
_CgprsL2rlyDroppedPktsMonTime_Object = MibScalar
cgprsL2rlyDroppedPktsMonTime = _CgprsL2rlyDroppedPktsMonTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 5),
    _CgprsL2rlyDroppedPktsMonTime_Type()
)
cgprsL2rlyDroppedPktsMonTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsL2rlyDroppedPktsMonTime.setStatus("current")
if mibBuilder.loadTexts:
    cgprsL2rlyDroppedPktsMonTime.setUnits("seconds")


class _CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Type(TruthValue):
    """Custom type cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable based on TruthValue"""


_CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Object = MibScalar
cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable = _CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 6),
    _CgprsL2rlyNoRespToKeepAliveMsgNotificationEnable_Type()
)
cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable.setStatus("current")


class _CgprsL2rlyUnitJoinNotificationEnable_Type(TruthValue):
    """Custom type cgprsL2rlyUnitJoinNotificationEnable based on TruthValue"""


_CgprsL2rlyUnitJoinNotificationEnable_Object = MibScalar
cgprsL2rlyUnitJoinNotificationEnable = _CgprsL2rlyUnitJoinNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 7),
    _CgprsL2rlyUnitJoinNotificationEnable_Type()
)
cgprsL2rlyUnitJoinNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgprsL2rlyUnitJoinNotificationEnable.setStatus("current")
_CgprsL2rlyInterfaceTable_Object = MibTable
cgprsL2rlyInterfaceTable = _CgprsL2rlyInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cgprsL2rlyInterfaceTable.setStatus("current")
_CgprsL2rlyInterfaceEntry_Object = MibTableRow
cgprsL2rlyInterfaceEntry = _CgprsL2rlyInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8, 1)
)
cgprsL2rlyInterfaceEntry.setIndexNames(
    (0, "CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInterfaceId"),
)
if mibBuilder.loadTexts:
    cgprsL2rlyInterfaceEntry.setStatus("current")
_CgprsL2rlyInterfaceId_Type = InterfaceIndex
_CgprsL2rlyInterfaceId_Object = MibTableColumn
cgprsL2rlyInterfaceId = _CgprsL2rlyInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8, 1, 1),
    _CgprsL2rlyInterfaceId_Type()
)
cgprsL2rlyInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsL2rlyInterfaceId.setStatus("current")
_CgprsL2rlyInterfaceRowStatus_Type = RowStatus
_CgprsL2rlyInterfaceRowStatus_Object = MibTableColumn
cgprsL2rlyInterfaceRowStatus = _CgprsL2rlyInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 1, 8, 1, 2),
    _CgprsL2rlyInterfaceRowStatus_Type()
)
cgprsL2rlyInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgprsL2rlyInterfaceRowStatus.setStatus("current")
_CiscoGprsL2rlyStats_ObjectIdentity = ObjectIdentity
ciscoGprsL2rlyStats = _CiscoGprsL2rlyStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2)
)
_CgprsL2rlyFlowControlTriggerCount_Type = Counter32
_CgprsL2rlyFlowControlTriggerCount_Object = MibScalar
cgprsL2rlyFlowControlTriggerCount = _CgprsL2rlyFlowControlTriggerCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 1),
    _CgprsL2rlyFlowControlTriggerCount_Type()
)
cgprsL2rlyFlowControlTriggerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsL2rlyFlowControlTriggerCount.setStatus("current")
_CgprsL2rlyInputQLen_Type = Counter32
_CgprsL2rlyInputQLen_Object = MibScalar
cgprsL2rlyInputQLen = _CgprsL2rlyInputQLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 2),
    _CgprsL2rlyInputQLen_Type()
)
cgprsL2rlyInputQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsL2rlyInputQLen.setStatus("current")
if mibBuilder.loadTexts:
    cgprsL2rlyInputQLen.setUnits("packets")
_CgprsL2rlyTotalPacketsDropped_Type = Counter32
_CgprsL2rlyTotalPacketsDropped_Object = MibScalar
cgprsL2rlyTotalPacketsDropped = _CgprsL2rlyTotalPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 3),
    _CgprsL2rlyTotalPacketsDropped_Type()
)
cgprsL2rlyTotalPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsL2rlyTotalPacketsDropped.setStatus("current")
if mibBuilder.loadTexts:
    cgprsL2rlyTotalPacketsDropped.setUnits("packets")


class _CgprsL2rlyDroppedPktsTimeFrame_Type(Integer32):
    """Custom type cgprsL2rlyDroppedPktsTimeFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgprsL2rlyDroppedPktsTimeFrame_Type.__name__ = "Integer32"
_CgprsL2rlyDroppedPktsTimeFrame_Object = MibScalar
cgprsL2rlyDroppedPktsTimeFrame = _CgprsL2rlyDroppedPktsTimeFrame_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 4),
    _CgprsL2rlyDroppedPktsTimeFrame_Type()
)
cgprsL2rlyDroppedPktsTimeFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsL2rlyDroppedPktsTimeFrame.setStatus("current")
if mibBuilder.loadTexts:
    cgprsL2rlyDroppedPktsTimeFrame.setUnits("seconds")
_CgprsL2rlyDroppedPktsCount_Type = Counter32
_CgprsL2rlyDroppedPktsCount_Object = MibScalar
cgprsL2rlyDroppedPktsCount = _CgprsL2rlyDroppedPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 5),
    _CgprsL2rlyDroppedPktsCount_Type()
)
cgprsL2rlyDroppedPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsL2rlyDroppedPktsCount.setStatus("current")
if mibBuilder.loadTexts:
    cgprsL2rlyDroppedPktsCount.setUnits("packets")
_CgprsL2rlyPeerTable_Object = MibTable
cgprsL2rlyPeerTable = _CgprsL2rlyPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cgprsL2rlyPeerTable.setStatus("current")
_CgprsL2rlyPeerEntry_Object = MibTableRow
cgprsL2rlyPeerEntry = _CgprsL2rlyPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6, 1)
)
cgprsL2rlyPeerEntry.setIndexNames(
    (0, "CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyPeerUid"),
    (0, "CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInterfaceId"),
)
if mibBuilder.loadTexts:
    cgprsL2rlyPeerEntry.setStatus("current")


class _CgprsL2rlyPeerUid_Type(Integer32):
    """Custom type cgprsL2rlyPeerUid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CgprsL2rlyPeerUid_Type.__name__ = "Integer32"
_CgprsL2rlyPeerUid_Object = MibTableColumn
cgprsL2rlyPeerUid = _CgprsL2rlyPeerUid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6, 1, 1),
    _CgprsL2rlyPeerUid_Type()
)
cgprsL2rlyPeerUid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgprsL2rlyPeerUid.setStatus("current")


class _CgprsL2rlyPeerUnitType_Type(Integer32):
    """Custom type cgprsL2rlyPeerUnitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("datacomUnit", 1),
          ("telecomUnit", 2))
    )


_CgprsL2rlyPeerUnitType_Type.__name__ = "Integer32"
_CgprsL2rlyPeerUnitType_Object = MibTableColumn
cgprsL2rlyPeerUnitType = _CgprsL2rlyPeerUnitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 1, 2, 6, 1, 2),
    _CgprsL2rlyPeerUnitType_Type()
)
cgprsL2rlyPeerUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgprsL2rlyPeerUnitType.setStatus("current")
_CiscoGprsL2rlyNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoGprsL2rlyNotificationPrefix = _CiscoGprsL2rlyNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 2)
)
_CiscoGprsL2rlyNotifications_ObjectIdentity = ObjectIdentity
ciscoGprsL2rlyNotifications = _CiscoGprsL2rlyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 2, 0)
)
_CiscoGprsL2rlyConformances_ObjectIdentity = ObjectIdentity
ciscoGprsL2rlyConformances = _CiscoGprsL2rlyConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 3)
)
_CgprsL2rlyCompliances_ObjectIdentity = ObjectIdentity
cgprsL2rlyCompliances = _CgprsL2rlyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 1)
)
_CgprsL2rlyGroups_ObjectIdentity = ObjectIdentity
cgprsL2rlyGroups = _CgprsL2rlyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 2)
)

# Managed Objects groups

cgprsL2rlyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 2, 1)
)
cgprsL2rlyConfigGroup.setObjects(
      *(("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUid"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUnitType"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyEchoTimer"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyFlowControlFlag"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyDroppedPktsMonTime"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUnitJoinNotificationEnable"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    cgprsL2rlyConfigGroup.setStatus("current")

cgprsL2rlyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 2, 2)
)
cgprsL2rlyStatsGroup.setObjects(
      *(("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyFlowControlTriggerCount"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyInputQLen"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyTotalPacketsDropped"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyDroppedPktsTimeFrame"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyDroppedPktsCount"),
        ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyPeerUnitType"))
)
if mibBuilder.loadTexts:
    cgprsL2rlyStatsGroup.setStatus("current")


# Notification objects

cgprsL2rlyUnitJoinNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 2, 0, 1)
)
cgprsL2rlyUnitJoinNotification.setObjects(
    ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUid")
)
if mibBuilder.loadTexts:
    cgprsL2rlyUnitJoinNotification.setStatus(
        "current"
    )

cgprsL2rlyNoRespToKeepAliveMsgNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 2, 0, 2)
)
cgprsL2rlyNoRespToKeepAliveMsgNotification.setObjects(
    ("CISCO-GPRS-L2RLY-MIB", "cgprsL2rlyUid")
)
if mibBuilder.loadTexts:
    cgprsL2rlyNoRespToKeepAliveMsgNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cgprsL2rlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 9993, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cgprsL2rlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GPRS-L2RLY-MIB",
    **{"ciscoGprsL2rlyMIB": ciscoGprsL2rlyMIB,
       "ciscoGprsL2rlyObjects": ciscoGprsL2rlyObjects,
       "ciscoGprsL2rlyConfig": ciscoGprsL2rlyConfig,
       "cgprsL2rlyUid": cgprsL2rlyUid,
       "cgprsL2rlyUnitType": cgprsL2rlyUnitType,
       "cgprsL2rlyEchoTimer": cgprsL2rlyEchoTimer,
       "cgprsL2rlyFlowControlFlag": cgprsL2rlyFlowControlFlag,
       "cgprsL2rlyDroppedPktsMonTime": cgprsL2rlyDroppedPktsMonTime,
       "cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable": cgprsL2rlyNoRespToKeepAliveMsgNotificationEnable,
       "cgprsL2rlyUnitJoinNotificationEnable": cgprsL2rlyUnitJoinNotificationEnable,
       "cgprsL2rlyInterfaceTable": cgprsL2rlyInterfaceTable,
       "cgprsL2rlyInterfaceEntry": cgprsL2rlyInterfaceEntry,
       "cgprsL2rlyInterfaceId": cgprsL2rlyInterfaceId,
       "cgprsL2rlyInterfaceRowStatus": cgprsL2rlyInterfaceRowStatus,
       "ciscoGprsL2rlyStats": ciscoGprsL2rlyStats,
       "cgprsL2rlyFlowControlTriggerCount": cgprsL2rlyFlowControlTriggerCount,
       "cgprsL2rlyInputQLen": cgprsL2rlyInputQLen,
       "cgprsL2rlyTotalPacketsDropped": cgprsL2rlyTotalPacketsDropped,
       "cgprsL2rlyDroppedPktsTimeFrame": cgprsL2rlyDroppedPktsTimeFrame,
       "cgprsL2rlyDroppedPktsCount": cgprsL2rlyDroppedPktsCount,
       "cgprsL2rlyPeerTable": cgprsL2rlyPeerTable,
       "cgprsL2rlyPeerEntry": cgprsL2rlyPeerEntry,
       "cgprsL2rlyPeerUid": cgprsL2rlyPeerUid,
       "cgprsL2rlyPeerUnitType": cgprsL2rlyPeerUnitType,
       "ciscoGprsL2rlyNotificationPrefix": ciscoGprsL2rlyNotificationPrefix,
       "ciscoGprsL2rlyNotifications": ciscoGprsL2rlyNotifications,
       "cgprsL2rlyUnitJoinNotification": cgprsL2rlyUnitJoinNotification,
       "cgprsL2rlyNoRespToKeepAliveMsgNotification": cgprsL2rlyNoRespToKeepAliveMsgNotification,
       "ciscoGprsL2rlyConformances": ciscoGprsL2rlyConformances,
       "cgprsL2rlyCompliances": cgprsL2rlyCompliances,
       "cgprsL2rlyCompliance": cgprsL2rlyCompliance,
       "cgprsL2rlyGroups": cgprsL2rlyGroups,
       "cgprsL2rlyConfigGroup": cgprsL2rlyConfigGroup,
       "cgprsL2rlyStatsGroup": cgprsL2rlyStatsGroup}
)
