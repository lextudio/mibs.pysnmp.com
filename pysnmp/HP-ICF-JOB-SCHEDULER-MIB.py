# SNMP MIB module (HP-ICF-JOB-SCHEDULER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-JOB-SCHEDULER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:40 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfJobSchedulerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105)
)
hpicfJobSchedulerMIB.setRevisions(
        ("2016-05-04 00:00",
         "2016-04-19 00:00",
         "2015-08-27 00:00",
         "2015-05-13 00:00",
         "2013-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfJobSchedulerObjects_ObjectIdentity = ObjectIdentity
hpicfJobSchedulerObjects = _HpicfJobSchedulerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1)
)
_HpicfJobSchedulerTable_Object = MibTable
hpicfJobSchedulerTable = _HpicfJobSchedulerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerTable.setStatus("current")
_HpicfJobSchedulerEntry_Object = MibTableRow
hpicfJobSchedulerEntry = _HpicfJobSchedulerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1)
)
hpicfJobSchedulerEntry.setIndexNames(
    (0, "HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerName"),
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerEntry.setStatus("current")


class _HpicfJobSchedulerName_Type(DisplayString):
    """Custom type hpicfJobSchedulerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_HpicfJobSchedulerName_Type.__name__ = "DisplayString"
_HpicfJobSchedulerName_Object = MibTableColumn
hpicfJobSchedulerName = _HpicfJobSchedulerName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 1),
    _HpicfJobSchedulerName_Type()
)
hpicfJobSchedulerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfJobSchedulerName.setStatus("current")
_HpicfJobSchedulerRowStatus_Type = RowStatus
_HpicfJobSchedulerRowStatus_Object = MibTableColumn
hpicfJobSchedulerRowStatus = _HpicfJobSchedulerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 2),
    _HpicfJobSchedulerRowStatus_Type()
)
hpicfJobSchedulerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfJobSchedulerRowStatus.setStatus("current")


class _HpicfJobSchedulerCommand_Type(OctetString):
    """Custom type hpicfJobSchedulerCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfJobSchedulerCommand_Type.__name__ = "OctetString"
_HpicfJobSchedulerCommand_Object = MibTableColumn
hpicfJobSchedulerCommand = _HpicfJobSchedulerCommand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 3),
    _HpicfJobSchedulerCommand_Type()
)
hpicfJobSchedulerCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerCommand.setStatus("current")
_HpicfJobSchedulerConfigSave_Type = TruthValue
_HpicfJobSchedulerConfigSave_Object = MibTableColumn
hpicfJobSchedulerConfigSave = _HpicfJobSchedulerConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 4),
    _HpicfJobSchedulerConfigSave_Type()
)
hpicfJobSchedulerConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerConfigSave.setStatus("current")
_HpicfJobSchedulerRunCount_Type = Unsigned32
_HpicfJobSchedulerRunCount_Object = MibTableColumn
hpicfJobSchedulerRunCount = _HpicfJobSchedulerRunCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 5),
    _HpicfJobSchedulerRunCount_Type()
)
hpicfJobSchedulerRunCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfJobSchedulerRunCount.setStatus("current")
_HpicfJobSchedulerErrorCount_Type = Unsigned32
_HpicfJobSchedulerErrorCount_Object = MibTableColumn
hpicfJobSchedulerErrorCount = _HpicfJobSchedulerErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 6),
    _HpicfJobSchedulerErrorCount_Type()
)
hpicfJobSchedulerErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfJobSchedulerErrorCount.setStatus("current")


class _HpicfJobSchedulerLastOutput_Type(OctetString):
    """Custom type hpicfJobSchedulerLastOutput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfJobSchedulerLastOutput_Type.__name__ = "OctetString"
_HpicfJobSchedulerLastOutput_Object = MibTableColumn
hpicfJobSchedulerLastOutput = _HpicfJobSchedulerLastOutput_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 7),
    _HpicfJobSchedulerLastOutput_Type()
)
hpicfJobSchedulerLastOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfJobSchedulerLastOutput.setStatus("current")


class _HpicfJobSchedulerEvent_Type(Bits):
    """Custom type hpicfJobSchedulerEvent based on Bits"""
    namedValues = NamedValues(
        *(("failover", 1),
          ("reboot", 0))
    )

_HpicfJobSchedulerEvent_Type.__name__ = "Bits"
_HpicfJobSchedulerEvent_Object = MibTableColumn
hpicfJobSchedulerEvent = _HpicfJobSchedulerEvent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 8),
    _HpicfJobSchedulerEvent_Type()
)
hpicfJobSchedulerEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerEvent.setStatus("current")


class _HpicfJobSchedulerCalendarMonth_Type(Bits):
    """Custom type hpicfJobSchedulerCalendarMonth based on Bits"""
    namedValues = NamedValues(
        *(("april", 3),
          ("august", 7),
          ("december", 11),
          ("february", 1),
          ("january", 0),
          ("july", 6),
          ("june", 5),
          ("march", 2),
          ("may", 4),
          ("november", 10),
          ("october", 9),
          ("september", 8))
    )

_HpicfJobSchedulerCalendarMonth_Type.__name__ = "Bits"
_HpicfJobSchedulerCalendarMonth_Object = MibTableColumn
hpicfJobSchedulerCalendarMonth = _HpicfJobSchedulerCalendarMonth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 9),
    _HpicfJobSchedulerCalendarMonth_Type()
)
hpicfJobSchedulerCalendarMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerCalendarMonth.setStatus("current")


class _HpicfJobSchedulerCalendarDayOfMonth_Type(Bits):
    """Custom type hpicfJobSchedulerCalendarDayOfMonth based on Bits"""
    namedValues = NamedValues(
        *(("d1", 0),
          ("d10", 9),
          ("d11", 10),
          ("d12", 11),
          ("d13", 12),
          ("d14", 13),
          ("d15", 14),
          ("d16", 15),
          ("d17", 16),
          ("d18", 17),
          ("d19", 18),
          ("d2", 1),
          ("d20", 19),
          ("d21", 20),
          ("d22", 21),
          ("d23", 22),
          ("d24", 23),
          ("d25", 24),
          ("d26", 25),
          ("d27", 26),
          ("d28", 27),
          ("d29", 28),
          ("d3", 2),
          ("d30", 29),
          ("d31", 30),
          ("d4", 3),
          ("d5", 4),
          ("d6", 5),
          ("d7", 6),
          ("d8", 7),
          ("d9", 8),
          ("r1", 31),
          ("r10", 40),
          ("r11", 41),
          ("r12", 42),
          ("r13", 43),
          ("r14", 44),
          ("r15", 45),
          ("r16", 46),
          ("r17", 47),
          ("r18", 48),
          ("r19", 49),
          ("r2", 32),
          ("r20", 50),
          ("r21", 51),
          ("r22", 52),
          ("r23", 53),
          ("r24", 54),
          ("r25", 55),
          ("r26", 56),
          ("r27", 57),
          ("r28", 58),
          ("r29", 59),
          ("r3", 33),
          ("r30", 60),
          ("r31", 61),
          ("r4", 34),
          ("r5", 35),
          ("r6", 36),
          ("r7", 37),
          ("r8", 38),
          ("r9", 39))
    )

_HpicfJobSchedulerCalendarDayOfMonth_Type.__name__ = "Bits"
_HpicfJobSchedulerCalendarDayOfMonth_Object = MibTableColumn
hpicfJobSchedulerCalendarDayOfMonth = _HpicfJobSchedulerCalendarDayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 10),
    _HpicfJobSchedulerCalendarDayOfMonth_Type()
)
hpicfJobSchedulerCalendarDayOfMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerCalendarDayOfMonth.setStatus("current")


class _HpicfJobSchedulerCalendarDayOfWeek_Type(Bits):
    """Custom type hpicfJobSchedulerCalendarDayOfWeek based on Bits"""
    namedValues = NamedValues(
        *(("friday", 5),
          ("monday", 1),
          ("saturday", 6),
          ("sunday", 0),
          ("thursday", 4),
          ("tuesday", 2),
          ("wednesday", 3))
    )

_HpicfJobSchedulerCalendarDayOfWeek_Type.__name__ = "Bits"
_HpicfJobSchedulerCalendarDayOfWeek_Object = MibTableColumn
hpicfJobSchedulerCalendarDayOfWeek = _HpicfJobSchedulerCalendarDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 11),
    _HpicfJobSchedulerCalendarDayOfWeek_Type()
)
hpicfJobSchedulerCalendarDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerCalendarDayOfWeek.setStatus("current")


class _HpicfJobSchedulerCalendarHour_Type(Bits):
    """Custom type hpicfJobSchedulerCalendarHour based on Bits"""
    namedValues = NamedValues(
        *(("h0", 0),
          ("h1", 1),
          ("h10", 10),
          ("h11", 11),
          ("h12", 12),
          ("h13", 13),
          ("h14", 14),
          ("h15", 15),
          ("h16", 16),
          ("h17", 17),
          ("h18", 18),
          ("h19", 19),
          ("h2", 2),
          ("h20", 20),
          ("h21", 21),
          ("h22", 22),
          ("h23", 23),
          ("h3", 3),
          ("h4", 4),
          ("h5", 5),
          ("h6", 6),
          ("h7", 7),
          ("h8", 8),
          ("h9", 9))
    )

_HpicfJobSchedulerCalendarHour_Type.__name__ = "Bits"
_HpicfJobSchedulerCalendarHour_Object = MibTableColumn
hpicfJobSchedulerCalendarHour = _HpicfJobSchedulerCalendarHour_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 12),
    _HpicfJobSchedulerCalendarHour_Type()
)
hpicfJobSchedulerCalendarHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerCalendarHour.setStatus("current")


class _HpicfJobSchedulerCalendarMinute_Type(Bits):
    """Custom type hpicfJobSchedulerCalendarMinute based on Bits"""
    namedValues = NamedValues(
        *(("m0", 0),
          ("m1", 1),
          ("m10", 10),
          ("m11", 11),
          ("m12", 12),
          ("m13", 13),
          ("m14", 14),
          ("m15", 15),
          ("m16", 16),
          ("m17", 17),
          ("m18", 18),
          ("m19", 19),
          ("m2", 2),
          ("m20", 20),
          ("m21", 21),
          ("m22", 22),
          ("m23", 23),
          ("m24", 24),
          ("m25", 25),
          ("m26", 26),
          ("m27", 27),
          ("m28", 28),
          ("m29", 29),
          ("m3", 3),
          ("m30", 30),
          ("m31", 31),
          ("m32", 32),
          ("m33", 33),
          ("m34", 34),
          ("m35", 35),
          ("m36", 36),
          ("m37", 37),
          ("m38", 38),
          ("m39", 39),
          ("m4", 4),
          ("m40", 40),
          ("m41", 41),
          ("m42", 42),
          ("m43", 43),
          ("m44", 44),
          ("m45", 45),
          ("m46", 46),
          ("m47", 47),
          ("m48", 48),
          ("m49", 49),
          ("m5", 5),
          ("m50", 50),
          ("m51", 51),
          ("m52", 52),
          ("m53", 53),
          ("m54", 54),
          ("m55", 55),
          ("m56", 56),
          ("m57", 57),
          ("m58", 58),
          ("m59", 59),
          ("m6", 6),
          ("m7", 7),
          ("m8", 8),
          ("m9", 9))
    )

_HpicfJobSchedulerCalendarMinute_Type.__name__ = "Bits"
_HpicfJobSchedulerCalendarMinute_Object = MibTableColumn
hpicfJobSchedulerCalendarMinute = _HpicfJobSchedulerCalendarMinute_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 13),
    _HpicfJobSchedulerCalendarMinute_Type()
)
hpicfJobSchedulerCalendarMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerCalendarMinute.setStatus("current")


class _HpicfJobSchedulerDelay_Type(Unsigned32):
    """Custom type hpicfJobSchedulerDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 527039),
    )


_HpicfJobSchedulerDelay_Type.__name__ = "Unsigned32"
_HpicfJobSchedulerDelay_Object = MibTableColumn
hpicfJobSchedulerDelay = _HpicfJobSchedulerDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 14),
    _HpicfJobSchedulerDelay_Type()
)
hpicfJobSchedulerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpicfJobSchedulerDelay.setUnits("minutes")


class _HpicfJobSchedulerCount_Type(Unsigned32):
    """Custom type hpicfJobSchedulerCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HpicfJobSchedulerCount_Type.__name__ = "Unsigned32"
_HpicfJobSchedulerCount_Object = MibTableColumn
hpicfJobSchedulerCount = _HpicfJobSchedulerCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 15),
    _HpicfJobSchedulerCount_Type()
)
hpicfJobSchedulerCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerCount.setStatus("current")
_HpicfJobSchedulerStatus_Type = TruthValue
_HpicfJobSchedulerStatus_Object = MibTableColumn
hpicfJobSchedulerStatus = _HpicfJobSchedulerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 16),
    _HpicfJobSchedulerStatus_Type()
)
hpicfJobSchedulerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfJobSchedulerStatus.setStatus("current")


class _HpicfJobSchedulerRunningStatus_Type(Integer32):
    """Custom type hpicfJobSchedulerRunningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("expired", 3),
          ("inactive", 2))
    )


_HpicfJobSchedulerRunningStatus_Type.__name__ = "Integer32"
_HpicfJobSchedulerRunningStatus_Object = MibTableColumn
hpicfJobSchedulerRunningStatus = _HpicfJobSchedulerRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 17),
    _HpicfJobSchedulerRunningStatus_Type()
)
hpicfJobSchedulerRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfJobSchedulerRunningStatus.setStatus("current")
_HpicfJobSchedulerLastRunTime_Type = DateAndTime
_HpicfJobSchedulerLastRunTime_Object = MibTableColumn
hpicfJobSchedulerLastRunTime = _HpicfJobSchedulerLastRunTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 18),
    _HpicfJobSchedulerLastRunTime_Type()
)
hpicfJobSchedulerLastRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfJobSchedulerLastRunTime.setStatus("current")


class _HpicfJobSchedulerSkipCount_Type(Unsigned32):
    """Custom type hpicfJobSchedulerSkipCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_HpicfJobSchedulerSkipCount_Type.__name__ = "Unsigned32"
_HpicfJobSchedulerSkipCount_Object = MibTableColumn
hpicfJobSchedulerSkipCount = _HpicfJobSchedulerSkipCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 1, 1, 1, 19),
    _HpicfJobSchedulerSkipCount_Type()
)
hpicfJobSchedulerSkipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfJobSchedulerSkipCount.setStatus("current")
_HpicfJobSchedulerConformance_ObjectIdentity = ObjectIdentity
hpicfJobSchedulerConformance = _HpicfJobSchedulerConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2)
)
_HpicfJobSchedulerMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfJobSchedulerMIBCompliances = _HpicfJobSchedulerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1)
)
_HpicfJobSchedulerMIBGroups_ObjectIdentity = ObjectIdentity
hpicfJobSchedulerMIBGroups = _HpicfJobSchedulerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2)
)

# Managed Objects groups

hpicfJobSchedulerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 1)
)
hpicfJobSchedulerGroup.setObjects(
      *(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"))
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerGroup.setStatus("deprecated")

hpicfJobSchedulerGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 2)
)
hpicfJobSchedulerGroup1.setObjects(
      *(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerDelay"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerStatus"))
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerGroup1.setStatus("deprecated")

hpicfJobSchedulerGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 3)
)
hpicfJobSchedulerGroup2.setObjects(
      *(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerDelay"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunningStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastRunTime"))
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerGroup2.setStatus("deprecated")

hpicfJobSchedulerGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 2, 4)
)
hpicfJobSchedulerGroup3.setObjects(
      *(("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRowStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCommand"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerConfigSave"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerErrorCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastOutput"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerEvent"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfMonth"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarDayOfWeek"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarHour"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCalendarMinute"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerDelay"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerCount"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerRunningStatus"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerLastRunTime"),
        ("HP-ICF-JOB-SCHEDULER-MIB", "hpicfJobSchedulerSkipCount"))
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfJobSchedulerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerMIBCompliance.setStatus(
        "deprecated"
    )

hpicfJobSchedulerMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerMIBCompliance1.setStatus(
        "deprecated"
    )

hpicfJobSchedulerMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerMIBCompliance2.setStatus(
        "deprecated"
    )

hpicfJobSchedulerMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 105, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfJobSchedulerMIBCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-JOB-SCHEDULER-MIB",
    **{"hpicfJobSchedulerMIB": hpicfJobSchedulerMIB,
       "hpicfJobSchedulerObjects": hpicfJobSchedulerObjects,
       "hpicfJobSchedulerTable": hpicfJobSchedulerTable,
       "hpicfJobSchedulerEntry": hpicfJobSchedulerEntry,
       "hpicfJobSchedulerName": hpicfJobSchedulerName,
       "hpicfJobSchedulerRowStatus": hpicfJobSchedulerRowStatus,
       "hpicfJobSchedulerCommand": hpicfJobSchedulerCommand,
       "hpicfJobSchedulerConfigSave": hpicfJobSchedulerConfigSave,
       "hpicfJobSchedulerRunCount": hpicfJobSchedulerRunCount,
       "hpicfJobSchedulerErrorCount": hpicfJobSchedulerErrorCount,
       "hpicfJobSchedulerLastOutput": hpicfJobSchedulerLastOutput,
       "hpicfJobSchedulerEvent": hpicfJobSchedulerEvent,
       "hpicfJobSchedulerCalendarMonth": hpicfJobSchedulerCalendarMonth,
       "hpicfJobSchedulerCalendarDayOfMonth": hpicfJobSchedulerCalendarDayOfMonth,
       "hpicfJobSchedulerCalendarDayOfWeek": hpicfJobSchedulerCalendarDayOfWeek,
       "hpicfJobSchedulerCalendarHour": hpicfJobSchedulerCalendarHour,
       "hpicfJobSchedulerCalendarMinute": hpicfJobSchedulerCalendarMinute,
       "hpicfJobSchedulerDelay": hpicfJobSchedulerDelay,
       "hpicfJobSchedulerCount": hpicfJobSchedulerCount,
       "hpicfJobSchedulerStatus": hpicfJobSchedulerStatus,
       "hpicfJobSchedulerRunningStatus": hpicfJobSchedulerRunningStatus,
       "hpicfJobSchedulerLastRunTime": hpicfJobSchedulerLastRunTime,
       "hpicfJobSchedulerSkipCount": hpicfJobSchedulerSkipCount,
       "hpicfJobSchedulerConformance": hpicfJobSchedulerConformance,
       "hpicfJobSchedulerMIBCompliances": hpicfJobSchedulerMIBCompliances,
       "hpicfJobSchedulerMIBCompliance": hpicfJobSchedulerMIBCompliance,
       "hpicfJobSchedulerMIBCompliance1": hpicfJobSchedulerMIBCompliance1,
       "hpicfJobSchedulerMIBCompliance2": hpicfJobSchedulerMIBCompliance2,
       "hpicfJobSchedulerMIBCompliance3": hpicfJobSchedulerMIBCompliance3,
       "hpicfJobSchedulerMIBGroups": hpicfJobSchedulerMIBGroups,
       "hpicfJobSchedulerGroup": hpicfJobSchedulerGroup,
       "hpicfJobSchedulerGroup1": hpicfJobSchedulerGroup1,
       "hpicfJobSchedulerGroup2": hpicfJobSchedulerGroup2,
       "hpicfJobSchedulerGroup3": hpicfJobSchedulerGroup3}
)
