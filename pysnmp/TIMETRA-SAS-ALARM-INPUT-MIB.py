# SNMP MIB module (TIMETRA-SAS-ALARM-INPUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIMETRA-SAS-ALARM-INPUT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:04:16 2024
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

(timetraSASConfs,
 timetraSASModules,
 timetraSASNotifyPrefix,
 timetraSASObjs) = mibBuilder.importSymbols(
    "TIMETRA-SAS-GLOBAL-MIB",
    "timetraSASConfs",
    "timetraSASModules",
    "timetraSASNotifyPrefix",
    "timetraSASObjs")

(TItemLongDescription,) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TItemLongDescription")


# MODULE-IDENTITY

tmnxSasAlarmInputMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 1, 1, 10)
)
tmnxSasAlarmInputMIBModule.setRevisions(
        ("2010-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmnxSASAlarmInputConformance_ObjectIdentity = ObjectIdentity
tmnxSASAlarmInputConformance = _TmnxSASAlarmInputConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 6)
)
_TmnxSASAlarmInputCompliances_ObjectIdentity = ObjectIdentity
tmnxSASAlarmInputCompliances = _TmnxSASAlarmInputCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 6, 1)
)
_TmnxSASAlarmInputGroups_ObjectIdentity = ObjectIdentity
tmnxSASAlarmInputGroups = _TmnxSASAlarmInputGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 6, 2)
)
_TmnxSasAlarmInputObjs_ObjectIdentity = ObjectIdentity
tmnxSasAlarmInputObjs = _TmnxSasAlarmInputObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9)
)
_TmnxSasAlarmInputInfoTable_Object = MibTable
tmnxSasAlarmInputInfoTable = _TmnxSasAlarmInputInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1)
)
if mibBuilder.loadTexts:
    tmnxSasAlarmInputInfoTable.setStatus("current")
_TmnxSasAlarmInputInfoEntry_Object = MibTableRow
tmnxSasAlarmInputInfoEntry = _TmnxSasAlarmInputInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1)
)
tmnxSasAlarmInputInfoEntry.setIndexNames(
    (0, "TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputId"),
)
if mibBuilder.loadTexts:
    tmnxSasAlarmInputInfoEntry.setStatus("current")


class _TmnxSasAlarmInputId_Type(Integer32):
    """Custom type tmnxSasAlarmInputId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TmnxSasAlarmInputId_Type.__name__ = "Integer32"
_TmnxSasAlarmInputId_Object = MibTableColumn
tmnxSasAlarmInputId = _TmnxSasAlarmInputId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1, 1),
    _TmnxSasAlarmInputId_Type()
)
tmnxSasAlarmInputId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputId.setStatus("current")
_TmnxSasAlarmInputDescription_Type = TItemLongDescription
_TmnxSasAlarmInputDescription_Object = MibTableColumn
tmnxSasAlarmInputDescription = _TmnxSasAlarmInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1, 2),
    _TmnxSasAlarmInputDescription_Type()
)
tmnxSasAlarmInputDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputDescription.setStatus("current")


class _TmnxSasAlarmInputAdminState_Type(Integer32):
    """Custom type tmnxSasAlarmInputAdminState based on Integer32"""
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


_TmnxSasAlarmInputAdminState_Type.__name__ = "Integer32"
_TmnxSasAlarmInputAdminState_Object = MibTableColumn
tmnxSasAlarmInputAdminState = _TmnxSasAlarmInputAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1, 3),
    _TmnxSasAlarmInputAdminState_Type()
)
tmnxSasAlarmInputAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputAdminState.setStatus("current")


class _TmnxSasAlarmInputPolarity_Type(Integer32):
    """Custom type tmnxSasAlarmInputPolarity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normally-closed", 2),
          ("normally-open", 1))
    )


_TmnxSasAlarmInputPolarity_Type.__name__ = "Integer32"
_TmnxSasAlarmInputPolarity_Object = MibTableColumn
tmnxSasAlarmInputPolarity = _TmnxSasAlarmInputPolarity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1, 4),
    _TmnxSasAlarmInputPolarity_Type()
)
tmnxSasAlarmInputPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputPolarity.setStatus("current")


class _TmnxSasAlarmOutputSeverity_Type(Integer32):
    """Custom type tmnxSasAlarmOutputSeverity based on Integer32"""
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("none", 1))
    )


_TmnxSasAlarmOutputSeverity_Type.__name__ = "Integer32"
_TmnxSasAlarmOutputSeverity_Object = MibTableColumn
tmnxSasAlarmOutputSeverity = _TmnxSasAlarmOutputSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1, 5),
    _TmnxSasAlarmOutputSeverity_Type()
)
tmnxSasAlarmOutputSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSasAlarmOutputSeverity.setStatus("current")


class _TmnxSasAlarmInputStatus_Type(Integer32):
    """Custom type tmnxSasAlarmInputStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("no-alarm", 1))
    )


_TmnxSasAlarmInputStatus_Type.__name__ = "Integer32"
_TmnxSasAlarmInputStatus_Object = MibTableColumn
tmnxSasAlarmInputStatus = _TmnxSasAlarmInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1, 6),
    _TmnxSasAlarmInputStatus_Type()
)
tmnxSasAlarmInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputStatus.setStatus("current")
_TmnxSasAlarmInputLastChange_Type = TimeTicks
_TmnxSasAlarmInputLastChange_Object = MibTableColumn
tmnxSasAlarmInputLastChange = _TmnxSasAlarmInputLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 1, 1, 7),
    _TmnxSasAlarmInputLastChange_Type()
)
tmnxSasAlarmInputLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputLastChange.setStatus("current")
_TmnxSasAlarmInputMessageTable_Object = MibTable
tmnxSasAlarmInputMessageTable = _TmnxSasAlarmInputMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 2)
)
if mibBuilder.loadTexts:
    tmnxSasAlarmInputMessageTable.setStatus("current")
_TmnxSasAlarmInputMessageEntry_Object = MibTableRow
tmnxSasAlarmInputMessageEntry = _TmnxSasAlarmInputMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 2, 1)
)
tmnxSasAlarmInputMessageEntry.setIndexNames(
    (0, "TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputId"),
)
if mibBuilder.loadTexts:
    tmnxSasAlarmInputMessageEntry.setStatus("current")
_TmnxSasAlarmInputTriggerMessage_Type = OctetString
_TmnxSasAlarmInputTriggerMessage_Object = MibTableColumn
tmnxSasAlarmInputTriggerMessage = _TmnxSasAlarmInputTriggerMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 2, 1, 1),
    _TmnxSasAlarmInputTriggerMessage_Type()
)
tmnxSasAlarmInputTriggerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputTriggerMessage.setStatus("current")
_TmnxSasAlarmInputClearMessage_Type = OctetString
_TmnxSasAlarmInputClearMessage_Object = MibTableColumn
tmnxSasAlarmInputClearMessage = _TmnxSasAlarmInputClearMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 2, 1, 2),
    _TmnxSasAlarmInputClearMessage_Type()
)
tmnxSasAlarmInputClearMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputClearMessage.setStatus("current")


class _TmnxSasAlarmInputPowerStatus_Type(Integer32):
    """Custom type tmnxSasAlarmInputPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_TmnxSasAlarmInputPowerStatus_Type.__name__ = "Integer32"
_TmnxSasAlarmInputPowerStatus_Object = MibScalar
tmnxSasAlarmInputPowerStatus = _TmnxSasAlarmInputPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 9, 3),
    _TmnxSasAlarmInputPowerStatus_Type()
)
tmnxSasAlarmInputPowerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputPowerStatus.setStatus("current")
_TmnxSasAlarmInputNotifyObjs_ObjectIdentity = ObjectIdentity
tmnxSasAlarmInputNotifyObjs = _TmnxSasAlarmInputNotifyObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 10)
)
_TmnxSasAlarmInputNotifyId_Type = Integer32
_TmnxSasAlarmInputNotifyId_Object = MibScalar
tmnxSasAlarmInputNotifyId = _TmnxSasAlarmInputNotifyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 10, 1),
    _TmnxSasAlarmInputNotifyId_Type()
)
tmnxSasAlarmInputNotifyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputNotifyId.setStatus("current")
_TmnxSasAlarmInputNotifyMessage_Type = TItemLongDescription
_TmnxSasAlarmInputNotifyMessage_Object = MibScalar
tmnxSasAlarmInputNotifyMessage = _TmnxSasAlarmInputNotifyMessage_Object(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 2, 10, 2),
    _TmnxSasAlarmInputNotifyMessage_Type()
)
tmnxSasAlarmInputNotifyMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    tmnxSasAlarmInputNotifyMessage.setStatus("current")
_TmnxSasAlarmInputNotifications_ObjectIdentity = ObjectIdentity
tmnxSasAlarmInputNotifications = _TmnxSasAlarmInputNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 10)
)

# Managed Objects groups

tmnxSASAlarmInputV2v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 6, 2, 1)
)
tmnxSASAlarmInputV2v0Group.setObjects(
      *(("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputDescription"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputAdminState"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputPolarity"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmOutputSeverity"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputStatus"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputLastChange"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputTriggerMessage"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputClearMessage"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputPowerStatus"))
)
if mibBuilder.loadTexts:
    tmnxSASAlarmInputV2v0Group.setStatus("current")


# Notification objects

tmnxSasAlarminput1StateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 10, 1)
)
tmnxSasAlarminput1StateChanged.setObjects(
      *(("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyId"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputDescription"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputStatus"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmOutputSeverity"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyMessage"))
)
if mibBuilder.loadTexts:
    tmnxSasAlarminput1StateChanged.setStatus(
        "current"
    )

tmnxSasAlarminput2StateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 10, 2)
)
tmnxSasAlarminput2StateChanged.setObjects(
      *(("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyId"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputDescription"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputStatus"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmOutputSeverity"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyMessage"))
)
if mibBuilder.loadTexts:
    tmnxSasAlarminput2StateChanged.setStatus(
        "current"
    )

tmnxSasAlarminput3StateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 10, 3)
)
tmnxSasAlarminput3StateChanged.setObjects(
      *(("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyId"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputDescription"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputStatus"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmOutputSeverity"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyMessage"))
)
if mibBuilder.loadTexts:
    tmnxSasAlarminput3StateChanged.setStatus(
        "current"
    )

tmnxSasAlarminput4StateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 3, 10, 4)
)
tmnxSasAlarminput4StateChanged.setObjects(
      *(("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyId"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputDescription"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputStatus"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmOutputSeverity"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarmInputNotifyMessage"))
)
if mibBuilder.loadTexts:
    tmnxSasAlarminput4StateChanged.setStatus(
        "current"
    )


# Notifications groups

tmnxAlarmInputNotificationV2v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 6, 2, 2)
)
tmnxAlarmInputNotificationV2v0Group.setObjects(
      *(("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarminput1StateChanged"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarminput2StateChanged"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarminput3StateChanged"),
        ("TIMETRA-SAS-ALARM-INPUT-MIB", "tmnxSasAlarminput4StateChanged"))
)
if mibBuilder.loadTexts:
    tmnxAlarmInputNotificationV2v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxSASAlarmInputComp7210V2v0 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 6, 2, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    tmnxSASAlarmInputComp7210V2v0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-SAS-ALARM-INPUT-MIB",
    **{"tmnxSasAlarmInputMIBModule": tmnxSasAlarmInputMIBModule,
       "tmnxSASAlarmInputConformance": tmnxSASAlarmInputConformance,
       "tmnxSASAlarmInputCompliances": tmnxSASAlarmInputCompliances,
       "tmnxSASAlarmInputComp7210V2v0": tmnxSASAlarmInputComp7210V2v0,
       "tmnxSASAlarmInputGroups": tmnxSASAlarmInputGroups,
       "tmnxSASAlarmInputV2v0Group": tmnxSASAlarmInputV2v0Group,
       "tmnxAlarmInputNotificationV2v0Group": tmnxAlarmInputNotificationV2v0Group,
       "tmnxSasAlarmInputObjs": tmnxSasAlarmInputObjs,
       "tmnxSasAlarmInputInfoTable": tmnxSasAlarmInputInfoTable,
       "tmnxSasAlarmInputInfoEntry": tmnxSasAlarmInputInfoEntry,
       "tmnxSasAlarmInputId": tmnxSasAlarmInputId,
       "tmnxSasAlarmInputDescription": tmnxSasAlarmInputDescription,
       "tmnxSasAlarmInputAdminState": tmnxSasAlarmInputAdminState,
       "tmnxSasAlarmInputPolarity": tmnxSasAlarmInputPolarity,
       "tmnxSasAlarmOutputSeverity": tmnxSasAlarmOutputSeverity,
       "tmnxSasAlarmInputStatus": tmnxSasAlarmInputStatus,
       "tmnxSasAlarmInputLastChange": tmnxSasAlarmInputLastChange,
       "tmnxSasAlarmInputMessageTable": tmnxSasAlarmInputMessageTable,
       "tmnxSasAlarmInputMessageEntry": tmnxSasAlarmInputMessageEntry,
       "tmnxSasAlarmInputTriggerMessage": tmnxSasAlarmInputTriggerMessage,
       "tmnxSasAlarmInputClearMessage": tmnxSasAlarmInputClearMessage,
       "tmnxSasAlarmInputPowerStatus": tmnxSasAlarmInputPowerStatus,
       "tmnxSasAlarmInputNotifyObjs": tmnxSasAlarmInputNotifyObjs,
       "tmnxSasAlarmInputNotifyId": tmnxSasAlarmInputNotifyId,
       "tmnxSasAlarmInputNotifyMessage": tmnxSasAlarmInputNotifyMessage,
       "tmnxSasAlarmInputNotifications": tmnxSasAlarmInputNotifications,
       "tmnxSasAlarminput1StateChanged": tmnxSasAlarminput1StateChanged,
       "tmnxSasAlarminput2StateChanged": tmnxSasAlarminput2StateChanged,
       "tmnxSasAlarminput3StateChanged": tmnxSasAlarminput3StateChanged,
       "tmnxSasAlarminput4StateChanged": tmnxSasAlarminput4StateChanged}
)
