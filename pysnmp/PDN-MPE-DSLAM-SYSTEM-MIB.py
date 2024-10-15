# SNMP MIB module (PDN-MPE-DSLAM-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-MPE-DSLAM-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:56 2024
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

(entPhysicalEntry,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalEntry",
    "entPhysicalIndex")

(pdn_mpe,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-mpe")

(mpeSysObjectID,) = mibBuilder.importSymbols(
    "PDN-MPE-MIB2-MIB",
    "mpeSysObjectID")

(ContactState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "ContactState")

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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpe_dslam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24)
)
mpe_dslam.setRevisions(
        ("2004-05-13 14:00",
         "2005-04-08 14:00",
         "2003-06-06 00:00",
         "2003-04-25 00:00",
         "2003-04-18 00:00",
         "2003-03-20 15:00",
         "2003-03-07 00:00",
         "2002-10-25 00:00",
         "2002-08-15 00:00",
         "2002-02-21 00:00",
         "2002-01-28 00:00",
         "2000-01-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MpeEntExtAdminStatus(Integer32, TextualConvention):
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
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )



class MpeEntExtOperStatus(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("dormant", 5),
          ("down", 2),
          ("notPresent", 6),
          ("reserved1", 7),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )



# MIB Managed Objects in the order of their OIDs

_MpeSysDevDslamMIBObjects_ObjectIdentity = ObjectIdentity
mpeSysDevDslamMIBObjects = _MpeSysDevDslamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1)
)
_MpeEntExtAlarms_ObjectIdentity = ObjectIdentity
mpeEntExtAlarms = _MpeEntExtAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1)
)
_MpeEntExtAlarmTable_Object = MibTable
mpeEntExtAlarmTable = _MpeEntExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpeEntExtAlarmTable.setStatus("current")
_MpeEntExtAlarmEntry_Object = MibTableRow
mpeEntExtAlarmEntry = _MpeEntExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mpeEntExtAlarmEntry.setStatus("current")
_MpeEntExtAlarm_Type = TruthValue
_MpeEntExtAlarm_Object = MibTableColumn
mpeEntExtAlarm = _MpeEntExtAlarm_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 1, 1, 1, 1),
    _MpeEntExtAlarm_Type()
)
mpeEntExtAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeEntExtAlarm.setStatus("current")
_MpeAlarmRelay_ObjectIdentity = ObjectIdentity
mpeAlarmRelay = _MpeAlarmRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2)
)
_MpeAlarmRelayEquipIndex_Type = Integer32
_MpeAlarmRelayEquipIndex_Object = MibScalar
mpeAlarmRelayEquipIndex = _MpeAlarmRelayEquipIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 1),
    _MpeAlarmRelayEquipIndex_Type()
)
mpeAlarmRelayEquipIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mpeAlarmRelayEquipIndex.setStatus("deprecated")
_MpeAlarmRelayInputContactState_Type = ContactState
_MpeAlarmRelayInputContactState_Object = MibScalar
mpeAlarmRelayInputContactState = _MpeAlarmRelayInputContactState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 2),
    _MpeAlarmRelayInputContactState_Type()
)
mpeAlarmRelayInputContactState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mpeAlarmRelayInputContactState.setStatus("deprecated")
_MpeAlarmRelayTable_Object = MibTable
mpeAlarmRelayTable = _MpeAlarmRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpeAlarmRelayTable.setStatus("current")
_MpeAlarmRelayEntry_Object = MibTableRow
mpeAlarmRelayEntry = _MpeAlarmRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 3, 1)
)
mpeAlarmRelayEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    mpeAlarmRelayEntry.setStatus("current")
_MpeAlarmRelayState_Type = ContactState
_MpeAlarmRelayState_Object = MibTableColumn
mpeAlarmRelayState = _MpeAlarmRelayState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 2, 3, 1, 1),
    _MpeAlarmRelayState_Type()
)
mpeAlarmRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeAlarmRelayState.setStatus("current")
_MpeEntExtMibObjects_ObjectIdentity = ObjectIdentity
mpeEntExtMibObjects = _MpeEntExtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3)
)
_MpeEntPhysicalExtTable_Object = MibTable
mpeEntPhysicalExtTable = _MpeEntPhysicalExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mpeEntPhysicalExtTable.setStatus("current")
_MpeEntPhysicalExtEntry_Object = MibTableRow
mpeEntPhysicalExtEntry = _MpeEntPhysicalExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mpeEntPhysicalExtEntry.setStatus("current")
_MpeEntPhysicalExtUpTime_Type = TimeTicks
_MpeEntPhysicalExtUpTime_Object = MibTableColumn
mpeEntPhysicalExtUpTime = _MpeEntPhysicalExtUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 1),
    _MpeEntPhysicalExtUpTime_Type()
)
mpeEntPhysicalExtUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeEntPhysicalExtUpTime.setStatus("current")
_MpeEntPhysicalExtLocation_Type = SnmpAdminString
_MpeEntPhysicalExtLocation_Object = MibTableColumn
mpeEntPhysicalExtLocation = _MpeEntPhysicalExtLocation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 2),
    _MpeEntPhysicalExtLocation_Type()
)
mpeEntPhysicalExtLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeEntPhysicalExtLocation.setStatus("current")
_MpeEntPhysicalExtAdminStatus_Type = MpeEntExtAdminStatus
_MpeEntPhysicalExtAdminStatus_Object = MibTableColumn
mpeEntPhysicalExtAdminStatus = _MpeEntPhysicalExtAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 3),
    _MpeEntPhysicalExtAdminStatus_Type()
)
mpeEntPhysicalExtAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpeEntPhysicalExtAdminStatus.setStatus("current")
_MpeEntPhysicalExtOperStatus_Type = MpeEntExtOperStatus
_MpeEntPhysicalExtOperStatus_Object = MibTableColumn
mpeEntPhysicalExtOperStatus = _MpeEntPhysicalExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 1, 3, 1, 1, 4),
    _MpeEntPhysicalExtOperStatus_Type()
)
mpeEntPhysicalExtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpeEntPhysicalExtOperStatus.setStatus("current")
_MpeSysDevDslamMIBTraps_ObjectIdentity = ObjectIdentity
mpeSysDevDslamMIBTraps = _MpeSysDevDslamMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2)
)
_MpeSysDevDslamMIBNotifications_ObjectIdentity = ObjectIdentity
mpeSysDevDslamMIBNotifications = _MpeSysDevDslamMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0)
)
_MpeSysDevDslamConformance_ObjectIdentity = ObjectIdentity
mpeSysDevDslamConformance = _MpeSysDevDslamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3)
)
_MpeSysDevDslamGroups_ObjectIdentity = ObjectIdentity
mpeSysDevDslamGroups = _MpeSysDevDslamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1)
)
_MpeSysDevDslamCompliances_ObjectIdentity = ObjectIdentity
mpeSysDevDslamCompliances = _MpeSysDevDslamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 2)
)
_MpeSysDevDslamDeprecatedGroup_ObjectIdentity = ObjectIdentity
mpeSysDevDslamDeprecatedGroup = _MpeSysDevDslamDeprecatedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 3)
)
entPhysicalEntry.registerAugmentions(
    ("PDN-MPE-DSLAM-SYSTEM-MIB",
     "mpeEntExtAlarmEntry")
)
mpeEntExtAlarmEntry.setIndexNames(*entPhysicalEntry.getIndexNames())
entPhysicalEntry.registerAugmentions(
    ("PDN-MPE-DSLAM-SYSTEM-MIB",
     "mpeEntPhysicalExtEntry")
)
mpeEntPhysicalExtEntry.setIndexNames(*entPhysicalEntry.getIndexNames())

# Managed Objects groups

mpeSysDevDslamAlarmStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 1)
)
mpeSysDevDslamAlarmStateGroup.setObjects(
    ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntExtAlarm")
)
if mibBuilder.loadTexts:
    mpeSysDevDslamAlarmStateGroup.setStatus("current")

mpeSysDevDslamAlarmRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 3)
)
mpeSysDevDslamAlarmRelayGroup.setObjects(
    ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayState")
)
if mibBuilder.loadTexts:
    mpeSysDevDslamAlarmRelayGroup.setStatus("current")

mpeEntPhysicalExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 4)
)
mpeEntPhysicalExtGroup.setObjects(
      *(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtUpTime"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtLocation"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtAdminStatus"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtOperStatus"))
)
if mibBuilder.loadTexts:
    mpeEntPhysicalExtGroup.setStatus("current")

mpeEntPhysicalExtNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 5)
)
mpeEntPhysicalExtNotificationObjectGroup.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeEntPhysicalExtNotificationObjectGroup.setStatus("current")

mpeDslamDeprecatedObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 3, 1)
)
mpeDslamDeprecatedObjectsGroup.setObjects(
      *(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayEquipIndex"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputContactState"))
)
if mibBuilder.loadTexts:
    mpeDslamDeprecatedObjectsGroup.setStatus("deprecated")


# Notification objects

mpeAlarmRelayInputStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 26)
)
mpeAlarmRelayInputStateChanged.setObjects(
    ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayState")
)
if mibBuilder.loadTexts:
    mpeAlarmRelayInputStateChanged.setStatus(
        "current"
    )

mpeFanEntityModuleFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 27)
)
mpeFanEntityModuleFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeFanEntityModuleFailure.setStatus(
        "current"
    )

mpeFanEntityModuleOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 28)
)
mpeFanEntityModuleOperational.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeFanEntityModuleOperational.setStatus(
        "current"
    )

mpePowerSourceAFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 29)
)
mpePowerSourceAFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpePowerSourceAFailure.setStatus(
        "current"
    )

mpePowerSourceBFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 30)
)
mpePowerSourceBFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpePowerSourceBFailure.setStatus(
        "current"
    )

mpePowerSourceAOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 31)
)
mpePowerSourceAOperational.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpePowerSourceAOperational.setStatus(
        "current"
    )

mpePowerSourceBOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 0, 32)
)
mpePowerSourceBOperational.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpePowerSourceBOperational.setStatus(
        "current"
    )

mpeCcn = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 7)
)
mpeCcn.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeCcn.setStatus(
        "current"
    )

mpeDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 15)
)
mpeDeviceFailure.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeDeviceFailure.setStatus(
        "current"
    )

mpeDeviceFailureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 16)
)
mpeDeviceFailureCleared.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeDeviceFailureCleared.setStatus(
        "current"
    )

mpeNonSupportedMCC = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 20)
)
mpeNonSupportedMCC.setObjects(
    ("PDN-MPE-MIB2-MIB", "mpeSysObjectID")
)
if mibBuilder.loadTexts:
    mpeNonSupportedMCC.setStatus(
        "current"
    )

mpeNonSupportedChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 21)
)
mpeNonSupportedChassis.setObjects(
    ("PDN-MPE-MIB2-MIB", "mpeSysObjectID")
)
if mibBuilder.loadTexts:
    mpeNonSupportedChassis.setStatus(
        "current"
    )

mpeAlarmRelayInputContactStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 22)
)
mpeAlarmRelayInputContactStateChanged.setObjects(
      *(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayEquipIndex"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputContactState"))
)
if mibBuilder.loadTexts:
    mpeAlarmRelayInputContactStateChanged.setStatus(
        "deprecated"
    )

mpeEntPhysicalExtEntityCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 23)
)
mpeEntPhysicalExtEntityCreated.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeEntPhysicalExtEntityCreated.setStatus(
        "current"
    )

mpeEntPhysicalExtEntityDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 24)
)
mpeEntPhysicalExtEntityDeleted.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeEntPhysicalExtEntityDeleted.setStatus(
        "current"
    )

mpeEntPhysicalExtEntityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 2, 25)
)
mpeEntPhysicalExtEntityChanged.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    mpeEntPhysicalExtEntityChanged.setStatus(
        "current"
    )


# Notifications groups

mpeEntityExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 2)
)
mpeEntityExtNotificationGroup.setObjects(
      *(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeCcn"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeDeviceFailure"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeDeviceFailureCleared"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeNonSupportedMCC"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeNonSupportedChassis"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtEntityCreated"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtEntityDeleted"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeEntPhysicalExtEntityChanged"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputStateChanged"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeFanEntityModuleFailure"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeFanEntityModuleOperational"))
)
if mibBuilder.loadTexts:
    mpeEntityExtNotificationGroup.setStatus(
        "current"
    )

mpeEntityExtPowerFailureNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 1, 6)
)
mpeEntityExtPowerFailureNotificationGroup.setObjects(
      *(("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceAFailure"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceBFailure"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceAOperational"),
        ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpePowerSourceBOperational"))
)
if mibBuilder.loadTexts:
    mpeEntityExtPowerFailureNotificationGroup.setStatus(
        "current"
    )

mpeDslamDeprecatedNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 3, 2)
)
mpeDslamDeprecatedNotificationsGroup.setObjects(
    ("PDN-MPE-DSLAM-SYSTEM-MIB", "mpeAlarmRelayInputContactStateChanged")
)
if mibBuilder.loadTexts:
    mpeDslamDeprecatedNotificationsGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

mpeSysDevDslamAlarmCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mpeSysDevDslamAlarmCompliances.setStatus(
        "current"
    )

mpeSysDevDslamAlarmDeprecatedCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 12, 24, 3, 2, 2)
)
if mibBuilder.loadTexts:
    mpeSysDevDslamAlarmDeprecatedCompliances.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-MPE-DSLAM-SYSTEM-MIB",
    **{"MpeEntExtAdminStatus": MpeEntExtAdminStatus,
       "MpeEntExtOperStatus": MpeEntExtOperStatus,
       "mpe-dslam": mpe_dslam,
       "mpeSysDevDslamMIBObjects": mpeSysDevDslamMIBObjects,
       "mpeEntExtAlarms": mpeEntExtAlarms,
       "mpeEntExtAlarmTable": mpeEntExtAlarmTable,
       "mpeEntExtAlarmEntry": mpeEntExtAlarmEntry,
       "mpeEntExtAlarm": mpeEntExtAlarm,
       "mpeAlarmRelay": mpeAlarmRelay,
       "mpeAlarmRelayEquipIndex": mpeAlarmRelayEquipIndex,
       "mpeAlarmRelayInputContactState": mpeAlarmRelayInputContactState,
       "mpeAlarmRelayTable": mpeAlarmRelayTable,
       "mpeAlarmRelayEntry": mpeAlarmRelayEntry,
       "mpeAlarmRelayState": mpeAlarmRelayState,
       "mpeEntExtMibObjects": mpeEntExtMibObjects,
       "mpeEntPhysicalExtTable": mpeEntPhysicalExtTable,
       "mpeEntPhysicalExtEntry": mpeEntPhysicalExtEntry,
       "mpeEntPhysicalExtUpTime": mpeEntPhysicalExtUpTime,
       "mpeEntPhysicalExtLocation": mpeEntPhysicalExtLocation,
       "mpeEntPhysicalExtAdminStatus": mpeEntPhysicalExtAdminStatus,
       "mpeEntPhysicalExtOperStatus": mpeEntPhysicalExtOperStatus,
       "mpeSysDevDslamMIBTraps": mpeSysDevDslamMIBTraps,
       "mpeSysDevDslamMIBNotifications": mpeSysDevDslamMIBNotifications,
       "mpeAlarmRelayInputStateChanged": mpeAlarmRelayInputStateChanged,
       "mpeFanEntityModuleFailure": mpeFanEntityModuleFailure,
       "mpeFanEntityModuleOperational": mpeFanEntityModuleOperational,
       "mpePowerSourceAFailure": mpePowerSourceAFailure,
       "mpePowerSourceBFailure": mpePowerSourceBFailure,
       "mpePowerSourceAOperational": mpePowerSourceAOperational,
       "mpePowerSourceBOperational": mpePowerSourceBOperational,
       "mpeCcn": mpeCcn,
       "mpeDeviceFailure": mpeDeviceFailure,
       "mpeDeviceFailureCleared": mpeDeviceFailureCleared,
       "mpeNonSupportedMCC": mpeNonSupportedMCC,
       "mpeNonSupportedChassis": mpeNonSupportedChassis,
       "mpeAlarmRelayInputContactStateChanged": mpeAlarmRelayInputContactStateChanged,
       "mpeEntPhysicalExtEntityCreated": mpeEntPhysicalExtEntityCreated,
       "mpeEntPhysicalExtEntityDeleted": mpeEntPhysicalExtEntityDeleted,
       "mpeEntPhysicalExtEntityChanged": mpeEntPhysicalExtEntityChanged,
       "mpeSysDevDslamConformance": mpeSysDevDslamConformance,
       "mpeSysDevDslamGroups": mpeSysDevDslamGroups,
       "mpeSysDevDslamAlarmStateGroup": mpeSysDevDslamAlarmStateGroup,
       "mpeEntityExtNotificationGroup": mpeEntityExtNotificationGroup,
       "mpeSysDevDslamAlarmRelayGroup": mpeSysDevDslamAlarmRelayGroup,
       "mpeEntPhysicalExtGroup": mpeEntPhysicalExtGroup,
       "mpeEntPhysicalExtNotificationObjectGroup": mpeEntPhysicalExtNotificationObjectGroup,
       "mpeEntityExtPowerFailureNotificationGroup": mpeEntityExtPowerFailureNotificationGroup,
       "mpeSysDevDslamCompliances": mpeSysDevDslamCompliances,
       "mpeSysDevDslamAlarmCompliances": mpeSysDevDslamAlarmCompliances,
       "mpeSysDevDslamAlarmDeprecatedCompliances": mpeSysDevDslamAlarmDeprecatedCompliances,
       "mpeSysDevDslamDeprecatedGroup": mpeSysDevDslamDeprecatedGroup,
       "mpeDslamDeprecatedObjectsGroup": mpeDslamDeprecatedObjectsGroup,
       "mpeDslamDeprecatedNotificationsGroup": mpeDslamDeprecatedNotificationsGroup}
)
