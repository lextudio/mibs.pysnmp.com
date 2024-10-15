# SNMP MIB module (DDM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DDM-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:28 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

swDdmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDdmCtrl_ObjectIdentity = ObjectIdentity
swDdmCtrl = _SwDdmCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 1)
)


class _SwDdmTrapState_Type(Integer32):
    """Custom type swDdmTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDdmTrapState_Type.__name__ = "Integer32"
_SwDdmTrapState_Object = MibScalar
swDdmTrapState = _SwDdmTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 1, 1),
    _SwDdmTrapState_Type()
)
swDdmTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmTrapState.setStatus("current")


class _SwDdmLogState_Type(Integer32):
    """Custom type swDdmLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDdmLogState_Type.__name__ = "Integer32"
_SwDdmLogState_Object = MibScalar
swDdmLogState = _SwDdmLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 1, 2),
    _SwDdmLogState_Type()
)
swDdmLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmLogState.setStatus("current")
_SwDdmInfo_ObjectIdentity = ObjectIdentity
swDdmInfo = _SwDdmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2)
)
_SwDdmStatus_ObjectIdentity = ObjectIdentity
swDdmStatus = _SwDdmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1)
)
_SwDdmStatusTable_Object = MibTable
swDdmStatusTable = _SwDdmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1)
)
if mibBuilder.loadTexts:
    swDdmStatusTable.setStatus("current")
_SwDdmStatusEntry_Object = MibTableRow
swDdmStatusEntry = _SwDdmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1)
)
swDdmStatusEntry.setIndexNames(
    (0, "DDM-MGMT-MIB", "swDdmPort"),
)
if mibBuilder.loadTexts:
    swDdmStatusEntry.setStatus("current")


class _SwDdmPort_Type(Integer32):
    """Custom type swDdmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwDdmPort_Type.__name__ = "Integer32"
_SwDdmPort_Object = MibTableColumn
swDdmPort = _SwDdmPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 1),
    _SwDdmPort_Type()
)
swDdmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmPort.setStatus("current")
_SwDdmTemperature_Type = DisplayString
_SwDdmTemperature_Object = MibTableColumn
swDdmTemperature = _SwDdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 2),
    _SwDdmTemperature_Type()
)
swDdmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmTemperature.setStatus("current")
_SwDdmVoltage_Type = DisplayString
_SwDdmVoltage_Object = MibTableColumn
swDdmVoltage = _SwDdmVoltage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 3),
    _SwDdmVoltage_Type()
)
swDdmVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmVoltage.setStatus("current")
_SwDdmBiasCurrent_Type = DisplayString
_SwDdmBiasCurrent_Object = MibTableColumn
swDdmBiasCurrent = _SwDdmBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 4),
    _SwDdmBiasCurrent_Type()
)
swDdmBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmBiasCurrent.setStatus("current")
_SwDdmTxPower_Type = DisplayString
_SwDdmTxPower_Object = MibTableColumn
swDdmTxPower = _SwDdmTxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 5),
    _SwDdmTxPower_Type()
)
swDdmTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmTxPower.setStatus("current")
_SwDdmRxPower_Type = DisplayString
_SwDdmRxPower_Object = MibTableColumn
swDdmRxPower = _SwDdmRxPower_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 2, 1, 1, 1, 6),
    _SwDdmRxPower_Type()
)
swDdmRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmRxPower.setStatus("current")
_SwDdmMgmt_ObjectIdentity = ObjectIdentity
swDdmMgmt = _SwDdmMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3)
)
_SwDdmThresholdMgmt_ObjectIdentity = ObjectIdentity
swDdmThresholdMgmt = _SwDdmThresholdMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1)
)
_SwDdmThresholdMgmtTable_Object = MibTable
swDdmThresholdMgmtTable = _SwDdmThresholdMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1)
)
if mibBuilder.loadTexts:
    swDdmThresholdMgmtTable.setStatus("current")
_SwDdmThresholdMgmtEntry_Object = MibTableRow
swDdmThresholdMgmtEntry = _SwDdmThresholdMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1)
)
swDdmThresholdMgmtEntry.setIndexNames(
    (0, "DDM-MGMT-MIB", "swDdmPort"),
    (0, "DDM-MGMT-MIB", "swDdmThresholdType"),
)
if mibBuilder.loadTexts:
    swDdmThresholdMgmtEntry.setStatus("current")


class _SwDdmThresholdType_Type(Integer32):
    """Custom type swDdmThresholdType based on Integer32"""
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
        *(("bias", 3),
          ("rxPower", 5),
          ("temperature", 1),
          ("txPower", 4),
          ("voltage", 2))
    )


_SwDdmThresholdType_Type.__name__ = "Integer32"
_SwDdmThresholdType_Object = MibTableColumn
swDdmThresholdType = _SwDdmThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 1),
    _SwDdmThresholdType_Type()
)
swDdmThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmThresholdType.setStatus("current")
_SwDdmHighAlarm_Type = DisplayString
_SwDdmHighAlarm_Object = MibTableColumn
swDdmHighAlarm = _SwDdmHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 2),
    _SwDdmHighAlarm_Type()
)
swDdmHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmHighAlarm.setStatus("current")
_SwDdmLowAlarm_Type = DisplayString
_SwDdmLowAlarm_Object = MibTableColumn
swDdmLowAlarm = _SwDdmLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 3),
    _SwDdmLowAlarm_Type()
)
swDdmLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmLowAlarm.setStatus("current")
_SwDdmHighWarning_Type = DisplayString
_SwDdmHighWarning_Object = MibTableColumn
swDdmHighWarning = _SwDdmHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 4),
    _SwDdmHighWarning_Type()
)
swDdmHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmHighWarning.setStatus("current")
_SwDdmLowWarning_Type = DisplayString
_SwDdmLowWarning_Object = MibTableColumn
swDdmLowWarning = _SwDdmLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 1, 1, 1, 5),
    _SwDdmLowWarning_Type()
)
swDdmLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmLowWarning.setStatus("current")
_SwDdmActionMgmt_ObjectIdentity = ObjectIdentity
swDdmActionMgmt = _SwDdmActionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2)
)
_SwDdmActionMgmtTable_Object = MibTable
swDdmActionMgmtTable = _SwDdmActionMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1)
)
if mibBuilder.loadTexts:
    swDdmActionMgmtTable.setStatus("obsolete")
_SwDdmActionMgmtEntry_Object = MibTableRow
swDdmActionMgmtEntry = _SwDdmActionMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1)
)
swDdmActionMgmtEntry.setIndexNames(
    (0, "DDM-MGMT-MIB", "swDdmPort"),
    (0, "DDM-MGMT-MIB", "swDdmActionType"),
)
if mibBuilder.loadTexts:
    swDdmActionMgmtEntry.setStatus("obsolete")


class _SwDdmActionType_Type(Integer32):
    """Custom type swDdmActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("warning", 2))
    )


_SwDdmActionType_Type.__name__ = "Integer32"
_SwDdmActionType_Object = MibTableColumn
swDdmActionType = _SwDdmActionType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1, 1),
    _SwDdmActionType_Type()
)
swDdmActionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDdmActionType.setStatus("obsolete")


class _SwDdmShutdown_Type(Integer32):
    """Custom type swDdmShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("other", 3))
    )


_SwDdmShutdown_Type.__name__ = "Integer32"
_SwDdmShutdown_Object = MibTableColumn
swDdmShutdown = _SwDdmShutdown_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1, 2),
    _SwDdmShutdown_Type()
)
swDdmShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmShutdown.setStatus("obsolete")


class _SwDdmTrapAndLog_Type(Integer32):
    """Custom type swDdmTrapAndLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("other", 3))
    )


_SwDdmTrapAndLog_Type.__name__ = "Integer32"
_SwDdmTrapAndLog_Object = MibTableColumn
swDdmTrapAndLog = _SwDdmTrapAndLog_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 1, 1, 3),
    _SwDdmTrapAndLog_Type()
)
swDdmTrapAndLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmTrapAndLog.setStatus("obsolete")
_SwDdmPortMgmtTable_Object = MibTable
swDdmPortMgmtTable = _SwDdmPortMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2)
)
if mibBuilder.loadTexts:
    swDdmPortMgmtTable.setStatus("current")
_SwDdmPortMgmtEntry_Object = MibTableRow
swDdmPortMgmtEntry = _SwDdmPortMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2, 1)
)
swDdmPortMgmtEntry.setIndexNames(
    (0, "DDM-MGMT-MIB", "swDdmPort"),
)
if mibBuilder.loadTexts:
    swDdmPortMgmtEntry.setStatus("current")


class _SwDdmPortState_Type(Integer32):
    """Custom type swDdmPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDdmPortState_Type.__name__ = "Integer32"
_SwDdmPortState_Object = MibTableColumn
swDdmPortState = _SwDdmPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2, 1, 1),
    _SwDdmPortState_Type()
)
swDdmPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmPortState.setStatus("current")


class _SwDdmPortShutdown_Type(Integer32):
    """Custom type swDdmPortShutdown based on Integer32"""
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
        *(("alarm", 1),
          ("none", 3),
          ("other", 4),
          ("warning", 2))
    )


_SwDdmPortShutdown_Type.__name__ = "Integer32"
_SwDdmPortShutdown_Object = MibTableColumn
swDdmPortShutdown = _SwDdmPortShutdown_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 3, 2, 2, 1, 2),
    _SwDdmPortShutdown_Type()
)
swDdmPortShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDdmPortShutdown.setStatus("current")
_SwDdmNotify_ObjectIdentity = ObjectIdentity
swDdmNotify = _SwDdmNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 4)
)
_SwDdmNotifyPrefix_ObjectIdentity = ObjectIdentity
swDdmNotifyPrefix = _SwDdmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 0)
)
_SwDdmNotificationBinding_ObjectIdentity = ObjectIdentity
swDdmNotificationBinding = _SwDdmNotificationBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 1)
)


class _SwDdmThresholdExceedType_Type(Integer32):
    """Custom type swDdmThresholdExceedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_SwDdmThresholdExceedType_Type.__name__ = "Integer32"
_SwDdmThresholdExceedType_Object = MibScalar
swDdmThresholdExceedType = _SwDdmThresholdExceedType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 1, 1),
    _SwDdmThresholdExceedType_Type()
)
swDdmThresholdExceedType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swDdmThresholdExceedType.setStatus("current")


class _SwDdmThresholdExceedOrRecover_Type(Integer32):
    """Custom type swDdmThresholdExceedOrRecover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exceed", 1),
          ("recover", 2))
    )


_SwDdmThresholdExceedOrRecover_Type.__name__ = "Integer32"
_SwDdmThresholdExceedOrRecover_Object = MibScalar
swDdmThresholdExceedOrRecover = _SwDdmThresholdExceedOrRecover_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 1, 2),
    _SwDdmThresholdExceedOrRecover_Type()
)
swDdmThresholdExceedOrRecover.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swDdmThresholdExceedOrRecover.setStatus("current")

# Managed Objects groups


# Notification objects

swDdmAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 0, 1)
)
swDdmAlarmTrap.setObjects(
      *(("DDM-MGMT-MIB", "swDdmPort"),
        ("DDM-MGMT-MIB", "swDdmThresholdType"),
        ("DDM-MGMT-MIB", "swDdmThresholdExceedType"),
        ("DDM-MGMT-MIB", "swDdmThresholdExceedOrRecover"))
)
if mibBuilder.loadTexts:
    swDdmAlarmTrap.setStatus(
        "current"
    )

swDdmWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 72, 4, 0, 2)
)
swDdmWarningTrap.setObjects(
      *(("DDM-MGMT-MIB", "swDdmPort"),
        ("DDM-MGMT-MIB", "swDdmThresholdType"),
        ("DDM-MGMT-MIB", "swDdmThresholdExceedType"),
        ("DDM-MGMT-MIB", "swDdmThresholdExceedOrRecover"))
)
if mibBuilder.loadTexts:
    swDdmWarningTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DDM-MGMT-MIB",
    **{"swDdmMIB": swDdmMIB,
       "swDdmCtrl": swDdmCtrl,
       "swDdmTrapState": swDdmTrapState,
       "swDdmLogState": swDdmLogState,
       "swDdmInfo": swDdmInfo,
       "swDdmStatus": swDdmStatus,
       "swDdmStatusTable": swDdmStatusTable,
       "swDdmStatusEntry": swDdmStatusEntry,
       "swDdmPort": swDdmPort,
       "swDdmTemperature": swDdmTemperature,
       "swDdmVoltage": swDdmVoltage,
       "swDdmBiasCurrent": swDdmBiasCurrent,
       "swDdmTxPower": swDdmTxPower,
       "swDdmRxPower": swDdmRxPower,
       "swDdmMgmt": swDdmMgmt,
       "swDdmThresholdMgmt": swDdmThresholdMgmt,
       "swDdmThresholdMgmtTable": swDdmThresholdMgmtTable,
       "swDdmThresholdMgmtEntry": swDdmThresholdMgmtEntry,
       "swDdmThresholdType": swDdmThresholdType,
       "swDdmHighAlarm": swDdmHighAlarm,
       "swDdmLowAlarm": swDdmLowAlarm,
       "swDdmHighWarning": swDdmHighWarning,
       "swDdmLowWarning": swDdmLowWarning,
       "swDdmActionMgmt": swDdmActionMgmt,
       "swDdmActionMgmtTable": swDdmActionMgmtTable,
       "swDdmActionMgmtEntry": swDdmActionMgmtEntry,
       "swDdmActionType": swDdmActionType,
       "swDdmShutdown": swDdmShutdown,
       "swDdmTrapAndLog": swDdmTrapAndLog,
       "swDdmPortMgmtTable": swDdmPortMgmtTable,
       "swDdmPortMgmtEntry": swDdmPortMgmtEntry,
       "swDdmPortState": swDdmPortState,
       "swDdmPortShutdown": swDdmPortShutdown,
       "swDdmNotify": swDdmNotify,
       "swDdmNotifyPrefix": swDdmNotifyPrefix,
       "swDdmAlarmTrap": swDdmAlarmTrap,
       "swDdmWarningTrap": swDdmWarningTrap,
       "swDdmNotificationBinding": swDdmNotificationBinding,
       "swDdmThresholdExceedType": swDdmThresholdExceedType,
       "swDdmThresholdExceedOrRecover": swDdmThresholdExceedOrRecover}
)
