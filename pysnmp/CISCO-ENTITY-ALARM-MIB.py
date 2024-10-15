# SNMP MIB module (CISCO-ENTITY-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:28 2024
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

(Unsigned32,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned32")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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

(AutonomousType,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class AlarmSeverity(Integer32, TextualConvention):
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
        *(("critical", 1),
          ("info", 4),
          ("major", 2),
          ("minor", 3))
    )



class AlarmSeverityOrZero(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )



class AlarmList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class AlarmFilterProfileType(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoEntityAlarmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityAlarmMIBObjects = _CiscoEntityAlarmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1)
)
_CeAlarmDescription_ObjectIdentity = ObjectIdentity
ceAlarmDescription = _CeAlarmDescription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1)
)
_CeAlarmDescrMapTable_Object = MibTable
ceAlarmDescrMapTable = _CeAlarmDescrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceAlarmDescrMapTable.setStatus("current")
_CeAlarmDescrMapEntry_Object = MibTableRow
ceAlarmDescrMapEntry = _CeAlarmDescrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 1, 1)
)
ceAlarmDescrMapEntry.setIndexNames(
    (0, "CISCO-ENTITY-ALARM-MIB", "ceAlarmDescrIndex"),
)
if mibBuilder.loadTexts:
    ceAlarmDescrMapEntry.setStatus("current")
_CeAlarmDescrIndex_Type = Unsigned32
_CeAlarmDescrIndex_Object = MibTableColumn
ceAlarmDescrIndex = _CeAlarmDescrIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 1, 1, 1),
    _CeAlarmDescrIndex_Type()
)
ceAlarmDescrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceAlarmDescrIndex.setStatus("current")
_CeAlarmDescrVendorType_Type = AutonomousType
_CeAlarmDescrVendorType_Object = MibTableColumn
ceAlarmDescrVendorType = _CeAlarmDescrVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 1, 1, 2),
    _CeAlarmDescrVendorType_Type()
)
ceAlarmDescrVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmDescrVendorType.setStatus("current")
_CeAlarmDescrTable_Object = MibTable
ceAlarmDescrTable = _CeAlarmDescrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ceAlarmDescrTable.setStatus("current")
_CeAlarmDescrEntry_Object = MibTableRow
ceAlarmDescrEntry = _CeAlarmDescrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 2, 1)
)
ceAlarmDescrEntry.setIndexNames(
    (0, "CISCO-ENTITY-ALARM-MIB", "ceAlarmDescrIndex"),
    (0, "CISCO-ENTITY-ALARM-MIB", "ceAlarmDescrAlarmType"),
)
if mibBuilder.loadTexts:
    ceAlarmDescrEntry.setStatus("current")
_CeAlarmDescrAlarmType_Type = AlarmType
_CeAlarmDescrAlarmType_Object = MibTableColumn
ceAlarmDescrAlarmType = _CeAlarmDescrAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 2, 1, 1),
    _CeAlarmDescrAlarmType_Type()
)
ceAlarmDescrAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceAlarmDescrAlarmType.setStatus("current")
_CeAlarmDescrSeverity_Type = AlarmSeverityOrZero
_CeAlarmDescrSeverity_Object = MibTableColumn
ceAlarmDescrSeverity = _CeAlarmDescrSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 2, 1, 2),
    _CeAlarmDescrSeverity_Type()
)
ceAlarmDescrSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAlarmDescrSeverity.setStatus("current")
_CeAlarmDescrText_Type = SnmpAdminString
_CeAlarmDescrText_Object = MibTableColumn
ceAlarmDescrText = _CeAlarmDescrText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 1, 2, 1, 3),
    _CeAlarmDescrText_Type()
)
ceAlarmDescrText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmDescrText.setStatus("current")
_CeAlarmMonitoring_ObjectIdentity = ObjectIdentity
ceAlarmMonitoring = _CeAlarmMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2)
)
_CeAlarmCriticalCount_Type = Gauge32
_CeAlarmCriticalCount_Object = MibScalar
ceAlarmCriticalCount = _CeAlarmCriticalCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 1),
    _CeAlarmCriticalCount_Type()
)
ceAlarmCriticalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmCriticalCount.setStatus("current")
_CeAlarmMajorCount_Type = Gauge32
_CeAlarmMajorCount_Object = MibScalar
ceAlarmMajorCount = _CeAlarmMajorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 2),
    _CeAlarmMajorCount_Type()
)
ceAlarmMajorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmMajorCount.setStatus("current")
_CeAlarmMinorCount_Type = Gauge32
_CeAlarmMinorCount_Object = MibScalar
ceAlarmMinorCount = _CeAlarmMinorCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 3),
    _CeAlarmMinorCount_Type()
)
ceAlarmMinorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmMinorCount.setStatus("current")
_CeAlarmCutOff_Type = TruthValue
_CeAlarmCutOff_Object = MibScalar
ceAlarmCutOff = _CeAlarmCutOff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 4),
    _CeAlarmCutOff_Type()
)
ceAlarmCutOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAlarmCutOff.setStatus("current")
_CeAlarmTable_Object = MibTable
ceAlarmTable = _CeAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ceAlarmTable.setStatus("current")
_CeAlarmEntry_Object = MibTableRow
ceAlarmEntry = _CeAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 5, 1)
)
ceAlarmEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    ceAlarmEntry.setStatus("current")
_CeAlarmFilterProfile_Type = AlarmFilterProfileType
_CeAlarmFilterProfile_Object = MibTableColumn
ceAlarmFilterProfile = _CeAlarmFilterProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 5, 1, 1),
    _CeAlarmFilterProfile_Type()
)
ceAlarmFilterProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAlarmFilterProfile.setStatus("current")
_CeAlarmSeverity_Type = AlarmSeverityOrZero
_CeAlarmSeverity_Object = MibTableColumn
ceAlarmSeverity = _CeAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 5, 1, 2),
    _CeAlarmSeverity_Type()
)
ceAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmSeverity.setStatus("current")
_CeAlarmList_Type = AlarmList
_CeAlarmList_Object = MibTableColumn
ceAlarmList = _CeAlarmList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 2, 5, 1, 3),
    _CeAlarmList_Type()
)
ceAlarmList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmList.setStatus("current")
_CeAlarmHistory_ObjectIdentity = ObjectIdentity
ceAlarmHistory = _CeAlarmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3)
)


class _CeAlarmHistTableSize_Type(Integer32):
    """Custom type ceAlarmHistTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CeAlarmHistTableSize_Type.__name__ = "Integer32"
_CeAlarmHistTableSize_Object = MibScalar
ceAlarmHistTableSize = _CeAlarmHistTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 1),
    _CeAlarmHistTableSize_Type()
)
ceAlarmHistTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAlarmHistTableSize.setStatus("current")
_CeAlarmHistLastIndex_Type = Unsigned32
_CeAlarmHistLastIndex_Object = MibScalar
ceAlarmHistLastIndex = _CeAlarmHistLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 2),
    _CeAlarmHistLastIndex_Type()
)
ceAlarmHistLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmHistLastIndex.setStatus("current")
_CeAlarmHistTable_Object = MibTable
ceAlarmHistTable = _CeAlarmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ceAlarmHistTable.setStatus("current")
_CeAlarmHistEntry_Object = MibTableRow
ceAlarmHistEntry = _CeAlarmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3, 1)
)
ceAlarmHistEntry.setIndexNames(
    (0, "CISCO-ENTITY-ALARM-MIB", "ceAlarmHistIndex"),
)
if mibBuilder.loadTexts:
    ceAlarmHistEntry.setStatus("current")
_CeAlarmHistIndex_Type = Unsigned32
_CeAlarmHistIndex_Object = MibTableColumn
ceAlarmHistIndex = _CeAlarmHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3, 1, 1),
    _CeAlarmHistIndex_Type()
)
ceAlarmHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceAlarmHistIndex.setStatus("current")


class _CeAlarmHistType_Type(Integer32):
    """Custom type ceAlarmHistType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 1),
          ("cleared", 2))
    )


_CeAlarmHistType_Type.__name__ = "Integer32"
_CeAlarmHistType_Object = MibTableColumn
ceAlarmHistType = _CeAlarmHistType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3, 1, 2),
    _CeAlarmHistType_Type()
)
ceAlarmHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmHistType.setStatus("current")
_CeAlarmHistEntPhysicalIndex_Type = PhysicalIndex
_CeAlarmHistEntPhysicalIndex_Object = MibTableColumn
ceAlarmHistEntPhysicalIndex = _CeAlarmHistEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3, 1, 3),
    _CeAlarmHistEntPhysicalIndex_Type()
)
ceAlarmHistEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmHistEntPhysicalIndex.setStatus("current")
_CeAlarmHistAlarmType_Type = AlarmType
_CeAlarmHistAlarmType_Object = MibTableColumn
ceAlarmHistAlarmType = _CeAlarmHistAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3, 1, 4),
    _CeAlarmHistAlarmType_Type()
)
ceAlarmHistAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmHistAlarmType.setStatus("current")
_CeAlarmHistSeverity_Type = AlarmSeverity
_CeAlarmHistSeverity_Object = MibTableColumn
ceAlarmHistSeverity = _CeAlarmHistSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3, 1, 5),
    _CeAlarmHistSeverity_Type()
)
ceAlarmHistSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmHistSeverity.setStatus("current")
_CeAlarmHistTimeStamp_Type = TimeStamp
_CeAlarmHistTimeStamp_Object = MibTableColumn
ceAlarmHistTimeStamp = _CeAlarmHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 3, 3, 1, 6),
    _CeAlarmHistTimeStamp_Type()
)
ceAlarmHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmHistTimeStamp.setStatus("current")
_CeAlarmFiltering_ObjectIdentity = ObjectIdentity
ceAlarmFiltering = _CeAlarmFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4)
)
_CeAlarmNotifiesEnable_Type = AlarmSeverityOrZero
_CeAlarmNotifiesEnable_Object = MibScalar
ceAlarmNotifiesEnable = _CeAlarmNotifiesEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 1),
    _CeAlarmNotifiesEnable_Type()
)
ceAlarmNotifiesEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAlarmNotifiesEnable.setStatus("current")
_CeAlarmSyslogEnable_Type = AlarmSeverityOrZero
_CeAlarmSyslogEnable_Object = MibScalar
ceAlarmSyslogEnable = _CeAlarmSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 2),
    _CeAlarmSyslogEnable_Type()
)
ceAlarmSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceAlarmSyslogEnable.setStatus("current")
_CeAlarmFilterProfileIndexNext_Type = AlarmFilterProfileType
_CeAlarmFilterProfileIndexNext_Object = MibScalar
ceAlarmFilterProfileIndexNext = _CeAlarmFilterProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 3),
    _CeAlarmFilterProfileIndexNext_Type()
)
ceAlarmFilterProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceAlarmFilterProfileIndexNext.setStatus("current")
_CeAlarmFilterProfileTable_Object = MibTable
ceAlarmFilterProfileTable = _CeAlarmFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ceAlarmFilterProfileTable.setStatus("current")
_CeAlarmFilterProfileEntry_Object = MibTableRow
ceAlarmFilterProfileEntry = _CeAlarmFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4, 1)
)
ceAlarmFilterProfileEntry.setIndexNames(
    (0, "CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterIndex"),
)
if mibBuilder.loadTexts:
    ceAlarmFilterProfileEntry.setStatus("current")
_CeAlarmFilterIndex_Type = AlarmFilterProfileType
_CeAlarmFilterIndex_Object = MibTableColumn
ceAlarmFilterIndex = _CeAlarmFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4, 1, 1),
    _CeAlarmFilterIndex_Type()
)
ceAlarmFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceAlarmFilterIndex.setStatus("current")
_CeAlarmFilterStatus_Type = RowStatus
_CeAlarmFilterStatus_Object = MibTableColumn
ceAlarmFilterStatus = _CeAlarmFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4, 1, 2),
    _CeAlarmFilterStatus_Type()
)
ceAlarmFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceAlarmFilterStatus.setStatus("current")
_CeAlarmFilterAlias_Type = DisplayString
_CeAlarmFilterAlias_Object = MibTableColumn
ceAlarmFilterAlias = _CeAlarmFilterAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4, 1, 3),
    _CeAlarmFilterAlias_Type()
)
ceAlarmFilterAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceAlarmFilterAlias.setStatus("current")
_CeAlarmFilterAlarmsEnabled_Type = AlarmList
_CeAlarmFilterAlarmsEnabled_Object = MibTableColumn
ceAlarmFilterAlarmsEnabled = _CeAlarmFilterAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4, 1, 4),
    _CeAlarmFilterAlarmsEnabled_Type()
)
ceAlarmFilterAlarmsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceAlarmFilterAlarmsEnabled.setStatus("current")
_CeAlarmFilterNotifiesEnabled_Type = AlarmList
_CeAlarmFilterNotifiesEnabled_Object = MibTableColumn
ceAlarmFilterNotifiesEnabled = _CeAlarmFilterNotifiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4, 1, 5),
    _CeAlarmFilterNotifiesEnabled_Type()
)
ceAlarmFilterNotifiesEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceAlarmFilterNotifiesEnabled.setStatus("current")
_CeAlarmFilterSyslogEnabled_Type = AlarmList
_CeAlarmFilterSyslogEnabled_Object = MibTableColumn
ceAlarmFilterSyslogEnabled = _CeAlarmFilterSyslogEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 1, 4, 4, 1, 6),
    _CeAlarmFilterSyslogEnabled_Type()
)
ceAlarmFilterSyslogEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceAlarmFilterSyslogEnabled.setStatus("current")
_CiscoEntityAlarmMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoEntityAlarmMIBNotificationsPrefix = _CiscoEntityAlarmMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 2)
)
_CiscoEntityAlarmMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoEntityAlarmMIBNotifications = _CiscoEntityAlarmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 2, 0)
)
_CiscoEntityAlarmMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEntityAlarmMIBConformance = _CiscoEntityAlarmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3)
)
_CiscoEntityAlarmMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEntityAlarmMIBCompliances = _CiscoEntityAlarmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 1)
)
_CiscoEntityAlarmMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEntityAlarmMIBGroups = _CiscoEntityAlarmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 2)
)

# Managed Objects groups

ceAlarmDescriptionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 2, 1)
)
ceAlarmDescriptionGroup.setObjects(
      *(("CISCO-ENTITY-ALARM-MIB", "ceAlarmDescrVendorType"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmDescrSeverity"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmDescrText"))
)
if mibBuilder.loadTexts:
    ceAlarmDescriptionGroup.setStatus("current")

ceAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 2, 2)
)
ceAlarmGroup.setObjects(
      *(("CISCO-ENTITY-ALARM-MIB", "ceAlarmCriticalCount"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmMajorCount"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmMinorCount"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmCutOff"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterProfile"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmSeverity"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmList"))
)
if mibBuilder.loadTexts:
    ceAlarmGroup.setStatus("current")

ceAlarmHistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 2, 3)
)
ceAlarmHistGroup.setObjects(
      *(("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistTableSize"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistLastIndex"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistType"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistEntPhysicalIndex"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistAlarmType"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistSeverity"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    ceAlarmHistGroup.setStatus("current")

ceAlarmFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 2, 4)
)
ceAlarmFilterGroup.setObjects(
      *(("CISCO-ENTITY-ALARM-MIB", "ceAlarmNotifiesEnable"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmSyslogEnable"))
)
if mibBuilder.loadTexts:
    ceAlarmFilterGroup.setStatus("current")

ceAlarmFilterProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 2, 5)
)
ceAlarmFilterProfileGroup.setObjects(
      *(("CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterProfileIndexNext"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterStatus"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterAlias"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterAlarmsEnabled"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterNotifiesEnabled"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmFilterSyslogEnabled"))
)
if mibBuilder.loadTexts:
    ceAlarmFilterProfileGroup.setStatus("current")


# Notification objects

ceAlarmAsserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 2, 0, 1)
)
ceAlarmAsserted.setObjects(
      *(("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistEntPhysicalIndex"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistAlarmType"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistSeverity"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    ceAlarmAsserted.setStatus(
        "current"
    )

ceAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 2, 0, 2)
)
ceAlarmCleared.setObjects(
      *(("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistEntPhysicalIndex"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistAlarmType"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistSeverity"),
        ("CISCO-ENTITY-ALARM-MIB", "ceAlarmHistTimeStamp"))
)
if mibBuilder.loadTexts:
    ceAlarmCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ceAlarmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 138, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ceAlarmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-ALARM-MIB",
    **{"AlarmType": AlarmType,
       "AlarmSeverity": AlarmSeverity,
       "AlarmSeverityOrZero": AlarmSeverityOrZero,
       "AlarmList": AlarmList,
       "AlarmFilterProfileType": AlarmFilterProfileType,
       "ciscoEntityAlarmMIB": ciscoEntityAlarmMIB,
       "ciscoEntityAlarmMIBObjects": ciscoEntityAlarmMIBObjects,
       "ceAlarmDescription": ceAlarmDescription,
       "ceAlarmDescrMapTable": ceAlarmDescrMapTable,
       "ceAlarmDescrMapEntry": ceAlarmDescrMapEntry,
       "ceAlarmDescrIndex": ceAlarmDescrIndex,
       "ceAlarmDescrVendorType": ceAlarmDescrVendorType,
       "ceAlarmDescrTable": ceAlarmDescrTable,
       "ceAlarmDescrEntry": ceAlarmDescrEntry,
       "ceAlarmDescrAlarmType": ceAlarmDescrAlarmType,
       "ceAlarmDescrSeverity": ceAlarmDescrSeverity,
       "ceAlarmDescrText": ceAlarmDescrText,
       "ceAlarmMonitoring": ceAlarmMonitoring,
       "ceAlarmCriticalCount": ceAlarmCriticalCount,
       "ceAlarmMajorCount": ceAlarmMajorCount,
       "ceAlarmMinorCount": ceAlarmMinorCount,
       "ceAlarmCutOff": ceAlarmCutOff,
       "ceAlarmTable": ceAlarmTable,
       "ceAlarmEntry": ceAlarmEntry,
       "ceAlarmFilterProfile": ceAlarmFilterProfile,
       "ceAlarmSeverity": ceAlarmSeverity,
       "ceAlarmList": ceAlarmList,
       "ceAlarmHistory": ceAlarmHistory,
       "ceAlarmHistTableSize": ceAlarmHistTableSize,
       "ceAlarmHistLastIndex": ceAlarmHistLastIndex,
       "ceAlarmHistTable": ceAlarmHistTable,
       "ceAlarmHistEntry": ceAlarmHistEntry,
       "ceAlarmHistIndex": ceAlarmHistIndex,
       "ceAlarmHistType": ceAlarmHistType,
       "ceAlarmHistEntPhysicalIndex": ceAlarmHistEntPhysicalIndex,
       "ceAlarmHistAlarmType": ceAlarmHistAlarmType,
       "ceAlarmHistSeverity": ceAlarmHistSeverity,
       "ceAlarmHistTimeStamp": ceAlarmHistTimeStamp,
       "ceAlarmFiltering": ceAlarmFiltering,
       "ceAlarmNotifiesEnable": ceAlarmNotifiesEnable,
       "ceAlarmSyslogEnable": ceAlarmSyslogEnable,
       "ceAlarmFilterProfileIndexNext": ceAlarmFilterProfileIndexNext,
       "ceAlarmFilterProfileTable": ceAlarmFilterProfileTable,
       "ceAlarmFilterProfileEntry": ceAlarmFilterProfileEntry,
       "ceAlarmFilterIndex": ceAlarmFilterIndex,
       "ceAlarmFilterStatus": ceAlarmFilterStatus,
       "ceAlarmFilterAlias": ceAlarmFilterAlias,
       "ceAlarmFilterAlarmsEnabled": ceAlarmFilterAlarmsEnabled,
       "ceAlarmFilterNotifiesEnabled": ceAlarmFilterNotifiesEnabled,
       "ceAlarmFilterSyslogEnabled": ceAlarmFilterSyslogEnabled,
       "ciscoEntityAlarmMIBNotificationsPrefix": ciscoEntityAlarmMIBNotificationsPrefix,
       "ciscoEntityAlarmMIBNotifications": ciscoEntityAlarmMIBNotifications,
       "ceAlarmAsserted": ceAlarmAsserted,
       "ceAlarmCleared": ceAlarmCleared,
       "ciscoEntityAlarmMIBConformance": ciscoEntityAlarmMIBConformance,
       "ciscoEntityAlarmMIBCompliances": ciscoEntityAlarmMIBCompliances,
       "ceAlarmMIBCompliance": ceAlarmMIBCompliance,
       "ciscoEntityAlarmMIBGroups": ciscoEntityAlarmMIBGroups,
       "ceAlarmDescriptionGroup": ceAlarmDescriptionGroup,
       "ceAlarmGroup": ceAlarmGroup,
       "ceAlarmHistGroup": ceAlarmHistGroup,
       "ceAlarmFilterGroup": ceAlarmFilterGroup,
       "ceAlarmFilterProfileGroup": ceAlarmFilterProfileGroup}
)
