# SNMP MIB module (RBN-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:14 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPort,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPort",
    "RbnSlot")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rbnMcLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102)
)
rbnMcLagMIB.setRevisions(
        ("2012-06-01 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnMcLagNotifications_ObjectIdentity = ObjectIdentity
rbnMcLagNotifications = _RbnMcLagNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 0)
)
_RbnMcLagObjects_ObjectIdentity = ObjectIdentity
rbnMcLagObjects = _RbnMcLagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1)
)
_RbnMcLagTable_Object = MibTable
rbnMcLagTable = _RbnMcLagTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1)
)
if mibBuilder.loadTexts:
    rbnMcLagTable.setStatus("current")
_RbnMcLagEntry_Object = MibTableRow
rbnMcLagEntry = _RbnMcLagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1)
)
rbnMcLagEntry.setIndexNames(
    (0, "RBN-LAG-MIB", "rbnMcLagName"),
)
if mibBuilder.loadTexts:
    rbnMcLagEntry.setStatus("current")


class _RbnMcLagName_Type(SnmpAdminString):
    """Custom type rbnMcLagName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RbnMcLagName_Type.__name__ = "SnmpAdminString"
_RbnMcLagName_Object = MibTableColumn
rbnMcLagName = _RbnMcLagName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 1),
    _RbnMcLagName_Type()
)
rbnMcLagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMcLagName.setStatus("current")
_RbnMcLagId_Type = Integer32
_RbnMcLagId_Object = MibTableColumn
rbnMcLagId = _RbnMcLagId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 2),
    _RbnMcLagId_Type()
)
rbnMcLagId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagId.setStatus("current")
_RbnMcLagSystemPriority_Type = Integer32
_RbnMcLagSystemPriority_Object = MibTableColumn
rbnMcLagSystemPriority = _RbnMcLagSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 3),
    _RbnMcLagSystemPriority_Type()
)
rbnMcLagSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagSystemPriority.setStatus("current")
_RbnMcLagSystemMacAddress_Type = MacAddress
_RbnMcLagSystemMacAddress_Object = MibTableColumn
rbnMcLagSystemMacAddress = _RbnMcLagSystemMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 4),
    _RbnMcLagSystemMacAddress_Type()
)
rbnMcLagSystemMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagSystemMacAddress.setStatus("current")
_RbnMcLagRevertiveMode_Type = TruthValue
_RbnMcLagRevertiveMode_Object = MibTableColumn
rbnMcLagRevertiveMode = _RbnMcLagRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 5),
    _RbnMcLagRevertiveMode_Type()
)
rbnMcLagRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagRevertiveMode.setStatus("current")
_RbnMcLagRevertiveHoldTimer_Type = Integer32
_RbnMcLagRevertiveHoldTimer_Object = MibTableColumn
rbnMcLagRevertiveHoldTimer = _RbnMcLagRevertiveHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 6),
    _RbnMcLagRevertiveHoldTimer_Type()
)
rbnMcLagRevertiveHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagRevertiveHoldTimer.setStatus("current")
if mibBuilder.loadTexts:
    rbnMcLagRevertiveHoldTimer.setUnits("seconds")


class _RbnMcLagOperState_Type(Integer32):
    """Custom type rbnMcLagOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("standby", 3),
          ("up", 1))
    )


_RbnMcLagOperState_Type.__name__ = "Integer32"
_RbnMcLagOperState_Object = MibTableColumn
rbnMcLagOperState = _RbnMcLagOperState_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 7),
    _RbnMcLagOperState_Type()
)
rbnMcLagOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagOperState.setStatus("current")


class _RbnMcLagOperErrorCode_Type(Integer32):
    """Custom type rbnMcLagOperErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("configMismatch", 1),
          ("downMinLink", 3),
          ("noError", 0),
          ("priorityError", 2))
    )


_RbnMcLagOperErrorCode_Type.__name__ = "Integer32"
_RbnMcLagOperErrorCode_Object = MibTableColumn
rbnMcLagOperErrorCode = _RbnMcLagOperErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 8),
    _RbnMcLagOperErrorCode_Type()
)
rbnMcLagOperErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagOperErrorCode.setStatus("current")
_RbnMcLagSwitchOverTime_Type = DateAndTime
_RbnMcLagSwitchOverTime_Object = MibTableColumn
rbnMcLagSwitchOverTime = _RbnMcLagSwitchOverTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 9),
    _RbnMcLagSwitchOverTime_Type()
)
rbnMcLagSwitchOverTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagSwitchOverTime.setStatus("current")
_RbnMcLagSwitchOverReason_Type = SnmpAdminString
_RbnMcLagSwitchOverReason_Object = MibTableColumn
rbnMcLagSwitchOverReason = _RbnMcLagSwitchOverReason_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 1, 1, 10),
    _RbnMcLagSwitchOverReason_Type()
)
rbnMcLagSwitchOverReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagSwitchOverReason.setStatus("current")
_RbnMcLagConstituentTable_Object = MibTable
rbnMcLagConstituentTable = _RbnMcLagConstituentTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 2)
)
if mibBuilder.loadTexts:
    rbnMcLagConstituentTable.setStatus("current")
_RbnMcLagConstituentEntry_Object = MibTableRow
rbnMcLagConstituentEntry = _RbnMcLagConstituentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 2, 1)
)
rbnMcLagConstituentEntry.setIndexNames(
    (0, "RBN-LAG-MIB", "rbnMcLagName"),
    (0, "RBN-LAG-MIB", "rbnMcLagConstituentSlot"),
    (0, "RBN-LAG-MIB", "rbnMcLagConstituentPort"),
)
if mibBuilder.loadTexts:
    rbnMcLagConstituentEntry.setStatus("current")
_RbnMcLagConstituentSlot_Type = RbnSlot
_RbnMcLagConstituentSlot_Object = MibTableColumn
rbnMcLagConstituentSlot = _RbnMcLagConstituentSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 2, 1, 1),
    _RbnMcLagConstituentSlot_Type()
)
rbnMcLagConstituentSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMcLagConstituentSlot.setStatus("current")
_RbnMcLagConstituentPort_Type = RbnPort
_RbnMcLagConstituentPort_Object = MibTableColumn
rbnMcLagConstituentPort = _RbnMcLagConstituentPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 2, 1, 2),
    _RbnMcLagConstituentPort_Type()
)
rbnMcLagConstituentPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnMcLagConstituentPort.setStatus("current")
_RbnMcLagConstituentPortPriority_Type = Integer32
_RbnMcLagConstituentPortPriority_Object = MibTableColumn
rbnMcLagConstituentPortPriority = _RbnMcLagConstituentPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 2, 1, 3),
    _RbnMcLagConstituentPortPriority_Type()
)
rbnMcLagConstituentPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagConstituentPortPriority.setStatus("current")
_RbnMcLagConstituentPortIfIndex_Type = InterfaceIndexOrZero
_RbnMcLagConstituentPortIfIndex_Object = MibTableColumn
rbnMcLagConstituentPortIfIndex = _RbnMcLagConstituentPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 1, 2, 1, 4),
    _RbnMcLagConstituentPortIfIndex_Type()
)
rbnMcLagConstituentPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnMcLagConstituentPortIfIndex.setStatus("current")
_RbnMcLagConformance_ObjectIdentity = ObjectIdentity
rbnMcLagConformance = _RbnMcLagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 2)
)
_RbnMcLagGroups_ObjectIdentity = ObjectIdentity
rbnMcLagGroups = _RbnMcLagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 2, 1)
)
_RbnMcLagCompliances_ObjectIdentity = ObjectIdentity
rbnMcLagCompliances = _RbnMcLagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 2, 2)
)

# Managed Objects groups

rbnMcLagObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 2, 1, 1)
)
rbnMcLagObjectGroup.setObjects(
      *(("RBN-LAG-MIB", "rbnMcLagId"),
        ("RBN-LAG-MIB", "rbnMcLagSystemPriority"),
        ("RBN-LAG-MIB", "rbnMcLagSystemMacAddress"),
        ("RBN-LAG-MIB", "rbnMcLagRevertiveMode"),
        ("RBN-LAG-MIB", "rbnMcLagRevertiveHoldTimer"),
        ("RBN-LAG-MIB", "rbnMcLagOperState"),
        ("RBN-LAG-MIB", "rbnMcLagOperErrorCode"),
        ("RBN-LAG-MIB", "rbnMcLagSwitchOverTime"),
        ("RBN-LAG-MIB", "rbnMcLagSwitchOverReason"),
        ("RBN-LAG-MIB", "rbnMcLagConstituentPortPriority"),
        ("RBN-LAG-MIB", "rbnMcLagConstituentPortIfIndex"))
)
if mibBuilder.loadTexts:
    rbnMcLagObjectGroup.setStatus("current")


# Notification objects

rbnMcLagSwitchOverEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 0, 1)
)
rbnMcLagSwitchOverEvent.setObjects(
      *(("RBN-LAG-MIB", "rbnMcLagOperState"),
        ("RBN-LAG-MIB", "rbnMcLagSwitchOverReason"))
)
if mibBuilder.loadTexts:
    rbnMcLagSwitchOverEvent.setStatus(
        "current"
    )

rbnMcLagOperFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 0, 2)
)
rbnMcLagOperFailed.setObjects(
      *(("RBN-LAG-MIB", "rbnMcLagOperState"),
        ("RBN-LAG-MIB", "rbnMcLagOperErrorCode"))
)
if mibBuilder.loadTexts:
    rbnMcLagOperFailed.setStatus(
        "current"
    )

rbnMcLagOperFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 0, 3)
)
rbnMcLagOperFailureCleared.setObjects(
    ("RBN-LAG-MIB", "rbnMcLagOperState")
)
if mibBuilder.loadTexts:
    rbnMcLagOperFailureCleared.setStatus(
        "current"
    )

rbnMcLagConstituentPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 0, 4)
)
rbnMcLagConstituentPortUp.setObjects(
      *(("RBN-LAG-MIB", "rbnMcLagConstituentPortPriority"),
        ("RBN-LAG-MIB", "rbnMcLagConstituentPortIfIndex"))
)
if mibBuilder.loadTexts:
    rbnMcLagConstituentPortUp.setStatus(
        "current"
    )

rbnMcLagConstituentPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 0, 5)
)
rbnMcLagConstituentPortDown.setObjects(
      *(("RBN-LAG-MIB", "rbnMcLagConstituentPortPriority"),
        ("RBN-LAG-MIB", "rbnMcLagConstituentPortIfIndex"))
)
if mibBuilder.loadTexts:
    rbnMcLagConstituentPortDown.setStatus(
        "current"
    )


# Notifications groups

rbnMcLagNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 2, 1, 2)
)
rbnMcLagNotificationGroup.setObjects(
      *(("RBN-LAG-MIB", "rbnMcLagSwitchOverEvent"),
        ("RBN-LAG-MIB", "rbnMcLagOperFailed"),
        ("RBN-LAG-MIB", "rbnMcLagOperFailureCleared"),
        ("RBN-LAG-MIB", "rbnMcLagConstituentPortUp"),
        ("RBN-LAG-MIB", "rbnMcLagConstituentPortDown"))
)
if mibBuilder.loadTexts:
    rbnMcLagNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnMcLagModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 102, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnMcLagModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-LAG-MIB",
    **{"rbnMcLagMIB": rbnMcLagMIB,
       "rbnMcLagNotifications": rbnMcLagNotifications,
       "rbnMcLagSwitchOverEvent": rbnMcLagSwitchOverEvent,
       "rbnMcLagOperFailed": rbnMcLagOperFailed,
       "rbnMcLagOperFailureCleared": rbnMcLagOperFailureCleared,
       "rbnMcLagConstituentPortUp": rbnMcLagConstituentPortUp,
       "rbnMcLagConstituentPortDown": rbnMcLagConstituentPortDown,
       "rbnMcLagObjects": rbnMcLagObjects,
       "rbnMcLagTable": rbnMcLagTable,
       "rbnMcLagEntry": rbnMcLagEntry,
       "rbnMcLagName": rbnMcLagName,
       "rbnMcLagId": rbnMcLagId,
       "rbnMcLagSystemPriority": rbnMcLagSystemPriority,
       "rbnMcLagSystemMacAddress": rbnMcLagSystemMacAddress,
       "rbnMcLagRevertiveMode": rbnMcLagRevertiveMode,
       "rbnMcLagRevertiveHoldTimer": rbnMcLagRevertiveHoldTimer,
       "rbnMcLagOperState": rbnMcLagOperState,
       "rbnMcLagOperErrorCode": rbnMcLagOperErrorCode,
       "rbnMcLagSwitchOverTime": rbnMcLagSwitchOverTime,
       "rbnMcLagSwitchOverReason": rbnMcLagSwitchOverReason,
       "rbnMcLagConstituentTable": rbnMcLagConstituentTable,
       "rbnMcLagConstituentEntry": rbnMcLagConstituentEntry,
       "rbnMcLagConstituentSlot": rbnMcLagConstituentSlot,
       "rbnMcLagConstituentPort": rbnMcLagConstituentPort,
       "rbnMcLagConstituentPortPriority": rbnMcLagConstituentPortPriority,
       "rbnMcLagConstituentPortIfIndex": rbnMcLagConstituentPortIfIndex,
       "rbnMcLagConformance": rbnMcLagConformance,
       "rbnMcLagGroups": rbnMcLagGroups,
       "rbnMcLagObjectGroup": rbnMcLagObjectGroup,
       "rbnMcLagNotificationGroup": rbnMcLagNotificationGroup,
       "rbnMcLagCompliances": rbnMcLagCompliances,
       "rbnMcLagModuleCompliance": rbnMcLagModuleCompliance}
)
