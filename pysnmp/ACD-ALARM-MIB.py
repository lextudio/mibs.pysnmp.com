# SNMP MIB module (ACD-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-ALARM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:16 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acdAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1)
)
acdAlarm.setRevisions(
        ("2011-10-10 01:00",
         "2010-11-10 01:00",
         "2009-02-04 01:00",
         "2008-02-01 01:00",
         "2007-05-22 01:00",
         "2006-12-19 01:00",
         "2006-08-06 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AcdAlarmGenThreshOn_Type(Unsigned32):
    """Custom type acdAlarmGenThreshOn based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 50000),
    )


_AcdAlarmGenThreshOn_Type.__name__ = "Unsigned32"
_AcdAlarmGenThreshOn_Object = MibScalar
acdAlarmGenThreshOn = _AcdAlarmGenThreshOn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 1),
    _AcdAlarmGenThreshOn_Type()
)
acdAlarmGenThreshOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmGenThreshOn.setStatus("current")
if mibBuilder.loadTexts:
    acdAlarmGenThreshOn.setUnits("milliseconds")


class _AcdAlarmGenThreshOff_Type(Unsigned32):
    """Custom type acdAlarmGenThreshOff based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 50000),
    )


_AcdAlarmGenThreshOff_Type.__name__ = "Unsigned32"
_AcdAlarmGenThreshOff_Object = MibScalar
acdAlarmGenThreshOff = _AcdAlarmGenThreshOff_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 2),
    _AcdAlarmGenThreshOff_Type()
)
acdAlarmGenThreshOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmGenThreshOff.setStatus("current")
if mibBuilder.loadTexts:
    acdAlarmGenThreshOff.setUnits("milliseconds")
_AcdAlarmGenLedEnable_Type = TruthValue
_AcdAlarmGenLedEnable_Object = MibScalar
acdAlarmGenLedEnable = _AcdAlarmGenLedEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 3),
    _AcdAlarmGenLedEnable_Type()
)
acdAlarmGenLedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmGenLedEnable.setStatus("current")
_AcdAlarmGenSyslogEnable_Type = TruthValue
_AcdAlarmGenSyslogEnable_Object = MibScalar
acdAlarmGenSyslogEnable = _AcdAlarmGenSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 4),
    _AcdAlarmGenSyslogEnable_Type()
)
acdAlarmGenSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmGenSyslogEnable.setStatus("current")
_AcdAlarmGenSNMPEnable_Type = TruthValue
_AcdAlarmGenSNMPEnable_Object = MibScalar
acdAlarmGenSNMPEnable = _AcdAlarmGenSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 5),
    _AcdAlarmGenSNMPEnable_Type()
)
acdAlarmGenSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmGenSNMPEnable.setStatus("current")
_AcdAlarmGen8023AHEnable_Type = TruthValue
_AcdAlarmGen8023AHEnable_Object = MibScalar
acdAlarmGen8023AHEnable = _AcdAlarmGen8023AHEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 6),
    _AcdAlarmGen8023AHEnable_Type()
)
acdAlarmGen8023AHEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmGen8023AHEnable.setStatus("current")
_AcdAlarmCfgTable_Object = MibTable
acdAlarmCfgTable = _AcdAlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10)
)
if mibBuilder.loadTexts:
    acdAlarmCfgTable.setStatus("current")
_AcdAlarmCfgEntry_Object = MibTableRow
acdAlarmCfgEntry = _AcdAlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1)
)
acdAlarmCfgEntry.setIndexNames(
    (0, "ACD-ALARM-MIB", "acdAlarmCfgID"),
)
if mibBuilder.loadTexts:
    acdAlarmCfgEntry.setStatus("current")
_AcdAlarmCfgID_Type = Unsigned32
_AcdAlarmCfgID_Object = MibTableColumn
acdAlarmCfgID = _AcdAlarmCfgID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 1),
    _AcdAlarmCfgID_Type()
)
acdAlarmCfgID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmCfgID.setStatus("current")
_AcdAlarmCfgNumber_Type = Unsigned32
_AcdAlarmCfgNumber_Object = MibTableColumn
acdAlarmCfgNumber = _AcdAlarmCfgNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 2),
    _AcdAlarmCfgNumber_Type()
)
acdAlarmCfgNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmCfgNumber.setStatus("current")


class _AcdAlarmCfgDesc_Type(DisplayString):
    """Custom type acdAlarmCfgDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdAlarmCfgDesc_Type.__name__ = "DisplayString"
_AcdAlarmCfgDesc_Object = MibTableColumn
acdAlarmCfgDesc = _AcdAlarmCfgDesc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 3),
    _AcdAlarmCfgDesc_Type()
)
acdAlarmCfgDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmCfgDesc.setStatus("current")
_AcdAlarmCfgEnable_Type = TruthValue
_AcdAlarmCfgEnable_Object = MibTableColumn
acdAlarmCfgEnable = _AcdAlarmCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 4),
    _AcdAlarmCfgEnable_Type()
)
acdAlarmCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmCfgEnable.setStatus("current")


class _AcdAlarmCfgSeverity_Type(Integer32):
    """Custom type acdAlarmCfgSeverity based on Integer32"""
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
        *(("critical", 3),
          ("info", 0),
          ("major", 2),
          ("minor", 1))
    )


_AcdAlarmCfgSeverity_Type.__name__ = "Integer32"
_AcdAlarmCfgSeverity_Object = MibTableColumn
acdAlarmCfgSeverity = _AcdAlarmCfgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 5),
    _AcdAlarmCfgSeverity_Type()
)
acdAlarmCfgSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmCfgSeverity.setStatus("current")
_AcdAlarmCfgServiceAffecting_Type = TruthValue
_AcdAlarmCfgServiceAffecting_Object = MibTableColumn
acdAlarmCfgServiceAffecting = _AcdAlarmCfgServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 6),
    _AcdAlarmCfgServiceAffecting_Type()
)
acdAlarmCfgServiceAffecting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdAlarmCfgServiceAffecting.setStatus("current")


class _AcdAlarmCfgExtNumber_Type(DisplayString):
    """Custom type acdAlarmCfgExtNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcdAlarmCfgExtNumber_Type.__name__ = "DisplayString"
_AcdAlarmCfgExtNumber_Object = MibTableColumn
acdAlarmCfgExtNumber = _AcdAlarmCfgExtNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 7),
    _AcdAlarmCfgExtNumber_Type()
)
acdAlarmCfgExtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmCfgExtNumber.setStatus("current")


class _AcdAlarmCfgConditionType_Type(DisplayString):
    """Custom type acdAlarmCfgConditionType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdAlarmCfgConditionType_Type.__name__ = "DisplayString"
_AcdAlarmCfgConditionType_Object = MibTableColumn
acdAlarmCfgConditionType = _AcdAlarmCfgConditionType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 8),
    _AcdAlarmCfgConditionType_Type()
)
acdAlarmCfgConditionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmCfgConditionType.setStatus("current")


class _AcdAlarmCfgAMOType_Type(DisplayString):
    """Custom type acdAlarmCfgAMOType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AcdAlarmCfgAMOType_Type.__name__ = "DisplayString"
_AcdAlarmCfgAMOType_Object = MibTableColumn
acdAlarmCfgAMOType = _AcdAlarmCfgAMOType_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 10, 1, 9),
    _AcdAlarmCfgAMOType_Type()
)
acdAlarmCfgAMOType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmCfgAMOType.setStatus("current")
_AcdAlarmStatusTable_Object = MibTable
acdAlarmStatusTable = _AcdAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 11)
)
if mibBuilder.loadTexts:
    acdAlarmStatusTable.setStatus("current")
_AcdAlarmStatusEntry_Object = MibTableRow
acdAlarmStatusEntry = _AcdAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1)
)
acdAlarmStatusEntry.setIndexNames(
    (0, "ACD-ALARM-MIB", "acdAlarmStatusID"),
)
if mibBuilder.loadTexts:
    acdAlarmStatusEntry.setStatus("current")
_AcdAlarmStatusID_Type = Unsigned32
_AcdAlarmStatusID_Object = MibTableColumn
acdAlarmStatusID = _AcdAlarmStatusID_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 1),
    _AcdAlarmStatusID_Type()
)
acdAlarmStatusID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmStatusID.setStatus("current")
_AcdAlarmStatusNumber_Type = Unsigned32
_AcdAlarmStatusNumber_Object = MibTableColumn
acdAlarmStatusNumber = _AcdAlarmStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 2),
    _AcdAlarmStatusNumber_Type()
)
acdAlarmStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmStatusNumber.setStatus("current")
_AcdAlarmStatusOn_Type = TruthValue
_AcdAlarmStatusOn_Object = MibTableColumn
acdAlarmStatusOn = _AcdAlarmStatusOn_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 3),
    _AcdAlarmStatusOn_Type()
)
acdAlarmStatusOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmStatusOn.setStatus("current")
_AcdAlarmStatusLastChange_Type = DateAndTime
_AcdAlarmStatusLastChange_Object = MibTableColumn
acdAlarmStatusLastChange = _AcdAlarmStatusLastChange_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 4),
    _AcdAlarmStatusLastChange_Type()
)
acdAlarmStatusLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmStatusLastChange.setStatus("current")


class _AcdAlarmStatusMsg_Type(DisplayString):
    """Custom type acdAlarmStatusMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcdAlarmStatusMsg_Type.__name__ = "DisplayString"
_AcdAlarmStatusMsg_Object = MibTableColumn
acdAlarmStatusMsg = _AcdAlarmStatusMsg_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 11, 1, 5),
    _AcdAlarmStatusMsg_Type()
)
acdAlarmStatusMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmStatusMsg.setStatus("current")
_AcdAlarmV2_ObjectIdentity = ObjectIdentity
acdAlarmV2 = _AcdAlarmV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 12)
)
_AcdAlarmMIBObjects_ObjectIdentity = ObjectIdentity
acdAlarmMIBObjects = _AcdAlarmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15)
)
_AcdAlarmConfig_ObjectIdentity = ObjectIdentity
acdAlarmConfig = _AcdAlarmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 1)
)
_AcdAlarmStatus_ObjectIdentity = ObjectIdentity
acdAlarmStatus = _AcdAlarmStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 2)
)
_AcdAlarmConformance_ObjectIdentity = ObjectIdentity
acdAlarmConformance = _AcdAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3)
)
_AcdAlarmCompliances_ObjectIdentity = ObjectIdentity
acdAlarmCompliances = _AcdAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 1)
)
_AcdAlarmGroups_ObjectIdentity = ObjectIdentity
acdAlarmGroups = _AcdAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2)
)
_AcdAlarmTableTid_ObjectIdentity = ObjectIdentity
acdAlarmTableTid = _AcdAlarmTableTid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 4)
)
_AcdAlarmCfgTableLastChangeTid_Type = Unsigned32
_AcdAlarmCfgTableLastChangeTid_Object = MibScalar
acdAlarmCfgTableLastChangeTid = _AcdAlarmCfgTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 4, 1),
    _AcdAlarmCfgTableLastChangeTid_Type()
)
acdAlarmCfgTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmCfgTableLastChangeTid.setStatus("current")
_AcdAlarmStatusTableLastChangeTid_Type = Unsigned32
_AcdAlarmStatusTableLastChangeTid_Object = MibScalar
acdAlarmStatusTableLastChangeTid = _AcdAlarmStatusTableLastChangeTid_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 4, 2),
    _AcdAlarmStatusTableLastChangeTid_Type()
)
acdAlarmStatusTableLastChangeTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdAlarmStatusTableLastChangeTid.setStatus("current")

# Managed Objects groups

acdAlarmGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 1)
)
acdAlarmGenGroup.setObjects(
      *(("ACD-ALARM-MIB", "acdAlarmGenThreshOn"),
        ("ACD-ALARM-MIB", "acdAlarmGenThreshOff"),
        ("ACD-ALARM-MIB", "acdAlarmGenLedEnable"),
        ("ACD-ALARM-MIB", "acdAlarmGenSyslogEnable"),
        ("ACD-ALARM-MIB", "acdAlarmGenSNMPEnable"),
        ("ACD-ALARM-MIB", "acdAlarmGen8023AHEnable"))
)
if mibBuilder.loadTexts:
    acdAlarmGenGroup.setStatus("current")

acdAlarmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 2)
)
acdAlarmCfgGroup.setObjects(
      *(("ACD-ALARM-MIB", "acdAlarmCfgID"),
        ("ACD-ALARM-MIB", "acdAlarmCfgNumber"),
        ("ACD-ALARM-MIB", "acdAlarmCfgDesc"),
        ("ACD-ALARM-MIB", "acdAlarmCfgEnable"),
        ("ACD-ALARM-MIB", "acdAlarmCfgSeverity"),
        ("ACD-ALARM-MIB", "acdAlarmCfgServiceAffecting"),
        ("ACD-ALARM-MIB", "acdAlarmCfgExtNumber"),
        ("ACD-ALARM-MIB", "acdAlarmCfgConditionType"),
        ("ACD-ALARM-MIB", "acdAlarmCfgAMOType"))
)
if mibBuilder.loadTexts:
    acdAlarmCfgGroup.setStatus("current")

acdAlarmStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 3)
)
acdAlarmStatusGroup.setObjects(
      *(("ACD-ALARM-MIB", "acdAlarmStatusID"),
        ("ACD-ALARM-MIB", "acdAlarmStatusNumber"),
        ("ACD-ALARM-MIB", "acdAlarmStatusOn"),
        ("ACD-ALARM-MIB", "acdAlarmStatusLastChange"),
        ("ACD-ALARM-MIB", "acdAlarmStatusMsg"))
)
if mibBuilder.loadTexts:
    acdAlarmStatusGroup.setStatus("current")

acdAlarmTidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 5)
)
acdAlarmTidGroup.setObjects(
      *(("ACD-ALARM-MIB", "acdAlarmCfgTableLastChangeTid"),
        ("ACD-ALARM-MIB", "acdAlarmStatusTableLastChangeTid"))
)
if mibBuilder.loadTexts:
    acdAlarmTidGroup.setStatus("current")


# Notification objects

acdAlarmActiveState = NotificationType(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 12, 1)
)
acdAlarmActiveState.setObjects(
      *(("ACD-ALARM-MIB", "acdAlarmCfgID"),
        ("ACD-ALARM-MIB", "acdAlarmCfgNumber"),
        ("ACD-ALARM-MIB", "acdAlarmCfgSeverity"),
        ("ACD-ALARM-MIB", "acdAlarmCfgServiceAffecting"),
        ("ACD-ALARM-MIB", "acdAlarmCfgDesc"),
        ("ACD-ALARM-MIB", "acdAlarmStatusLastChange"),
        ("ACD-ALARM-MIB", "acdAlarmCfgExtNumber"),
        ("ACD-ALARM-MIB", "acdAlarmCfgConditionType"),
        ("ACD-ALARM-MIB", "acdAlarmCfgAMOType"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    acdAlarmActiveState.setStatus(
        "current"
    )

acdAlarmClearState = NotificationType(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 12, 2)
)
acdAlarmClearState.setObjects(
      *(("ACD-ALARM-MIB", "acdAlarmCfgID"),
        ("ACD-ALARM-MIB", "acdAlarmCfgNumber"),
        ("ACD-ALARM-MIB", "acdAlarmCfgSeverity"),
        ("ACD-ALARM-MIB", "acdAlarmCfgServiceAffecting"),
        ("ACD-ALARM-MIB", "acdAlarmCfgDesc"),
        ("ACD-ALARM-MIB", "acdAlarmStatusLastChange"),
        ("ACD-ALARM-MIB", "acdAlarmCfgExtNumber"),
        ("ACD-ALARM-MIB", "acdAlarmCfgConditionType"),
        ("ACD-ALARM-MIB", "acdAlarmCfgAMOType"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    acdAlarmClearState.setStatus(
        "current"
    )


# Notifications groups

acdAlarmNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 2, 4)
)
acdAlarmNotificationsGroup.setObjects(
      *(("ACD-ALARM-MIB", "acdAlarmActiveState"),
        ("ACD-ALARM-MIB", "acdAlarmClearState"))
)
if mibBuilder.loadTexts:
    acdAlarmNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

acdAlarmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 1, 15, 3, 1, 1)
)
if mibBuilder.loadTexts:
    acdAlarmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-ALARM-MIB",
    **{"acdAlarm": acdAlarm,
       "acdAlarmGenThreshOn": acdAlarmGenThreshOn,
       "acdAlarmGenThreshOff": acdAlarmGenThreshOff,
       "acdAlarmGenLedEnable": acdAlarmGenLedEnable,
       "acdAlarmGenSyslogEnable": acdAlarmGenSyslogEnable,
       "acdAlarmGenSNMPEnable": acdAlarmGenSNMPEnable,
       "acdAlarmGen8023AHEnable": acdAlarmGen8023AHEnable,
       "acdAlarmCfgTable": acdAlarmCfgTable,
       "acdAlarmCfgEntry": acdAlarmCfgEntry,
       "acdAlarmCfgID": acdAlarmCfgID,
       "acdAlarmCfgNumber": acdAlarmCfgNumber,
       "acdAlarmCfgDesc": acdAlarmCfgDesc,
       "acdAlarmCfgEnable": acdAlarmCfgEnable,
       "acdAlarmCfgSeverity": acdAlarmCfgSeverity,
       "acdAlarmCfgServiceAffecting": acdAlarmCfgServiceAffecting,
       "acdAlarmCfgExtNumber": acdAlarmCfgExtNumber,
       "acdAlarmCfgConditionType": acdAlarmCfgConditionType,
       "acdAlarmCfgAMOType": acdAlarmCfgAMOType,
       "acdAlarmStatusTable": acdAlarmStatusTable,
       "acdAlarmStatusEntry": acdAlarmStatusEntry,
       "acdAlarmStatusID": acdAlarmStatusID,
       "acdAlarmStatusNumber": acdAlarmStatusNumber,
       "acdAlarmStatusOn": acdAlarmStatusOn,
       "acdAlarmStatusLastChange": acdAlarmStatusLastChange,
       "acdAlarmStatusMsg": acdAlarmStatusMsg,
       "acdAlarmV2": acdAlarmV2,
       "acdAlarmActiveState": acdAlarmActiveState,
       "acdAlarmClearState": acdAlarmClearState,
       "acdAlarmMIBObjects": acdAlarmMIBObjects,
       "acdAlarmConfig": acdAlarmConfig,
       "acdAlarmStatus": acdAlarmStatus,
       "acdAlarmConformance": acdAlarmConformance,
       "acdAlarmCompliances": acdAlarmCompliances,
       "acdAlarmCompliance": acdAlarmCompliance,
       "acdAlarmGroups": acdAlarmGroups,
       "acdAlarmGenGroup": acdAlarmGenGroup,
       "acdAlarmCfgGroup": acdAlarmCfgGroup,
       "acdAlarmStatusGroup": acdAlarmStatusGroup,
       "acdAlarmNotificationsGroup": acdAlarmNotificationsGroup,
       "acdAlarmTidGroup": acdAlarmTidGroup,
       "acdAlarmTableTid": acdAlarmTableTid,
       "acdAlarmCfgTableLastChangeTid": acdAlarmCfgTableLastChangeTid,
       "acdAlarmStatusTableLastChangeTid": acdAlarmStatusTableLastChangeTid}
)
