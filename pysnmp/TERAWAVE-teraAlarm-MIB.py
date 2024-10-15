# SNMP MIB module (TERAWAVE-teraAlarm-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraAlarm-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:12 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_Teratraps_ObjectIdentity = ObjectIdentity
teratraps = _Teratraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 1)
)
_TeraAlarms_ObjectIdentity = ObjectIdentity
teraAlarms = _TeraAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1)
)
_TeraConfig_ObjectIdentity = ObjectIdentity
teraConfig = _TeraConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1)
)
_TeraNextAlarmSequenceTable_Object = MibTable
teraNextAlarmSequenceTable = _TeraNextAlarmSequenceTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    teraNextAlarmSequenceTable.setStatus("mandatory")
_TeraNextAlarmSequenceTableEntry_Object = MibTableRow
teraNextAlarmSequenceTableEntry = _TeraNextAlarmSequenceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 1, 1)
)
teraNextAlarmSequenceTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraActiveAlarmSlot"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraPonIndex"),
)
if mibBuilder.loadTexts:
    teraNextAlarmSequenceTableEntry.setStatus("mandatory")
_TeraNextAlarmSequence_Type = Counter32
_TeraNextAlarmSequence_Object = MibTableColumn
teraNextAlarmSequence = _TeraNextAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 1, 1, 1),
    _TeraNextAlarmSequence_Type()
)
teraNextAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraNextAlarmSequence.setStatus("mandatory")
_TeraLocalNextAlarmSequence_Type = Counter32
_TeraLocalNextAlarmSequence_Object = MibScalar
teraLocalNextAlarmSequence = _TeraLocalNextAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 2),
    _TeraLocalNextAlarmSequence_Type()
)
teraLocalNextAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalNextAlarmSequence.setStatus("mandatory")


class _TeraResetAlarmHistoryTable_Type(Integer32):
    """Custom type teraResetAlarmHistoryTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_TeraResetAlarmHistoryTable_Type.__name__ = "Integer32"
_TeraResetAlarmHistoryTable_Object = MibScalar
teraResetAlarmHistoryTable = _TeraResetAlarmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 3),
    _TeraResetAlarmHistoryTable_Type()
)
teraResetAlarmHistoryTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraResetAlarmHistoryTable.setStatus("mandatory")


class _TeraResetEventTable_Type(Integer32):
    """Custom type teraResetEventTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_TeraResetEventTable_Type.__name__ = "Integer32"
_TeraResetEventTable_Object = MibScalar
teraResetEventTable = _TeraResetEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 4),
    _TeraResetEventTable_Type()
)
teraResetEventTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraResetEventTable.setStatus("mandatory")
_TeraAlarmReportingTable_Object = MibTable
teraAlarmReportingTable = _TeraAlarmReportingTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    teraAlarmReportingTable.setStatus("mandatory")
_TeraAlarmReportingTableEntry_Object = MibTableRow
teraAlarmReportingTableEntry = _TeraAlarmReportingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 5, 1)
)
teraAlarmReportingTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraAlarmReportingTableIndex"),
)
if mibBuilder.loadTexts:
    teraAlarmReportingTableEntry.setStatus("mandatory")


class _TeraAlarmReportingTableIndex_Type(Integer32):
    """Custom type teraAlarmReportingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_TeraAlarmReportingTableIndex_Type.__name__ = "Integer32"
_TeraAlarmReportingTableIndex_Object = MibTableColumn
teraAlarmReportingTableIndex = _TeraAlarmReportingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 5, 1, 1),
    _TeraAlarmReportingTableIndex_Type()
)
teraAlarmReportingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAlarmReportingTableIndex.setStatus("mandatory")
_TeraAlarmReportingIPaddress_Type = OctetString
_TeraAlarmReportingIPaddress_Object = MibTableColumn
teraAlarmReportingIPaddress = _TeraAlarmReportingIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 5, 1, 2),
    _TeraAlarmReportingIPaddress_Type()
)
teraAlarmReportingIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAlarmReportingIPaddress.setStatus("mandatory")
_TeraAlarmReportingCommunity_Type = OctetString
_TeraAlarmReportingCommunity_Object = MibTableColumn
teraAlarmReportingCommunity = _TeraAlarmReportingCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 1, 5, 1, 3),
    _TeraAlarmReportingCommunity_Type()
)
teraAlarmReportingCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAlarmReportingCommunity.setStatus("mandatory")
_TeraActiveAlarmTable_Object = MibTable
teraActiveAlarmTable = _TeraActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2)
)
if mibBuilder.loadTexts:
    teraActiveAlarmTable.setStatus("mandatory")
_TeraActiveAlarmTableEntry_Object = MibTableRow
teraActiveAlarmTableEntry = _TeraActiveAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1)
)
teraActiveAlarmTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraPonIndex"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraActiveAlarmSequence"),
)
if mibBuilder.loadTexts:
    teraActiveAlarmTableEntry.setStatus("mandatory")


class _TeraActiveAlarmSequence_Type(Counter32):
    """Custom type teraActiveAlarmSequence based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraActiveAlarmSequence_Type.__name__ = "Counter32"
_TeraActiveAlarmSequence_Object = MibTableColumn
teraActiveAlarmSequence = _TeraActiveAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 1),
    _TeraActiveAlarmSequence_Type()
)
teraActiveAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmSequence.setStatus("mandatory")
_TeraActiveAlarmPort_Type = Integer32
_TeraActiveAlarmPort_Object = MibTableColumn
teraActiveAlarmPort = _TeraActiveAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 2),
    _TeraActiveAlarmPort_Type()
)
teraActiveAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmPort.setStatus("mandatory")
_TeraActiveAlarmPortType_Type = Integer32
_TeraActiveAlarmPortType_Object = MibTableColumn
teraActiveAlarmPortType = _TeraActiveAlarmPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 3),
    _TeraActiveAlarmPortType_Type()
)
teraActiveAlarmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmPortType.setStatus("mandatory")
_TeraActiveAlarmCardType_Type = Integer32
_TeraActiveAlarmCardType_Object = MibTableColumn
teraActiveAlarmCardType = _TeraActiveAlarmCardType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 4),
    _TeraActiveAlarmCardType_Type()
)
teraActiveAlarmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmCardType.setStatus("mandatory")
_TeraActiveAlarmSlot_Type = Integer32
_TeraActiveAlarmSlot_Object = MibTableColumn
teraActiveAlarmSlot = _TeraActiveAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 5),
    _TeraActiveAlarmSlot_Type()
)
teraActiveAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmSlot.setStatus("mandatory")
_TeraActiveAlarmPhysPort_Type = Integer32
_TeraActiveAlarmPhysPort_Object = MibTableColumn
teraActiveAlarmPhysPort = _TeraActiveAlarmPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 6),
    _TeraActiveAlarmPhysPort_Type()
)
teraActiveAlarmPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmPhysPort.setStatus("mandatory")
_TeraActiveAlarmType_Type = Integer32
_TeraActiveAlarmType_Object = MibTableColumn
teraActiveAlarmType = _TeraActiveAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 7),
    _TeraActiveAlarmType_Type()
)
teraActiveAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmType.setStatus("mandatory")


class _TeraActiveAlarmSeverity_Type(Integer32):
    """Custom type teraActiveAlarmSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraActiveAlarmSeverity_Type.__name__ = "Integer32"
_TeraActiveAlarmSeverity_Object = MibTableColumn
teraActiveAlarmSeverity = _TeraActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 8),
    _TeraActiveAlarmSeverity_Type()
)
teraActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmSeverity.setStatus("mandatory")
_TeraActiveAlarmTime_Type = OctetString
_TeraActiveAlarmTime_Object = MibTableColumn
teraActiveAlarmTime = _TeraActiveAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 9),
    _TeraActiveAlarmTime_Type()
)
teraActiveAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmTime.setStatus("mandatory")
_TeraActiveAlarmMessage_Type = OctetString
_TeraActiveAlarmMessage_Object = MibTableColumn
teraActiveAlarmMessage = _TeraActiveAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 10),
    _TeraActiveAlarmMessage_Type()
)
teraActiveAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmMessage.setStatus("mandatory")
_TeraActiveAlarmTimeInSecs_Type = Integer32
_TeraActiveAlarmTimeInSecs_Object = MibTableColumn
teraActiveAlarmTimeInSecs = _TeraActiveAlarmTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 11),
    _TeraActiveAlarmTimeInSecs_Type()
)
teraActiveAlarmTimeInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmTimeInSecs.setStatus("mandatory")
_TeraActiveAlarmNEClli_Type = OctetString
_TeraActiveAlarmNEClli_Object = MibTableColumn
teraActiveAlarmNEClli = _TeraActiveAlarmNEClli_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 2, 1, 12),
    _TeraActiveAlarmNEClli_Type()
)
teraActiveAlarmNEClli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraActiveAlarmNEClli.setStatus("mandatory")
_TeraHistoryAlarmTable_Object = MibTable
teraHistoryAlarmTable = _TeraHistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3)
)
if mibBuilder.loadTexts:
    teraHistoryAlarmTable.setStatus("mandatory")
_TeraHistoryAlarmTableEntry_Object = MibTableRow
teraHistoryAlarmTableEntry = _TeraHistoryAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1)
)
teraHistoryAlarmTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraPonIndex"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraHistoryAlarmSequence"),
)
if mibBuilder.loadTexts:
    teraHistoryAlarmTableEntry.setStatus("mandatory")


class _TeraHistoryAlarmSequence_Type(Counter32):
    """Custom type teraHistoryAlarmSequence based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraHistoryAlarmSequence_Type.__name__ = "Counter32"
_TeraHistoryAlarmSequence_Object = MibTableColumn
teraHistoryAlarmSequence = _TeraHistoryAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 1),
    _TeraHistoryAlarmSequence_Type()
)
teraHistoryAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmSequence.setStatus("mandatory")
_TeraHistoryAlarmPort_Type = Integer32
_TeraHistoryAlarmPort_Object = MibTableColumn
teraHistoryAlarmPort = _TeraHistoryAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 2),
    _TeraHistoryAlarmPort_Type()
)
teraHistoryAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmPort.setStatus("mandatory")
_TeraHistoryAlarmPortType_Type = Integer32
_TeraHistoryAlarmPortType_Object = MibTableColumn
teraHistoryAlarmPortType = _TeraHistoryAlarmPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 3),
    _TeraHistoryAlarmPortType_Type()
)
teraHistoryAlarmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmPortType.setStatus("mandatory")
_TeraHistoryAlarmCardType_Type = Integer32
_TeraHistoryAlarmCardType_Object = MibTableColumn
teraHistoryAlarmCardType = _TeraHistoryAlarmCardType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 4),
    _TeraHistoryAlarmCardType_Type()
)
teraHistoryAlarmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmCardType.setStatus("mandatory")
_TeraHistoryAlarmSlot_Type = Integer32
_TeraHistoryAlarmSlot_Object = MibTableColumn
teraHistoryAlarmSlot = _TeraHistoryAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 5),
    _TeraHistoryAlarmSlot_Type()
)
teraHistoryAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmSlot.setStatus("mandatory")
_TeraHistoryAlarmPhysPort_Type = Integer32
_TeraHistoryAlarmPhysPort_Object = MibTableColumn
teraHistoryAlarmPhysPort = _TeraHistoryAlarmPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 6),
    _TeraHistoryAlarmPhysPort_Type()
)
teraHistoryAlarmPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmPhysPort.setStatus("mandatory")
_TeraHistoryAlarmType_Type = Integer32
_TeraHistoryAlarmType_Object = MibTableColumn
teraHistoryAlarmType = _TeraHistoryAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 7),
    _TeraHistoryAlarmType_Type()
)
teraHistoryAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmType.setStatus("mandatory")


class _TeraHistoryAlarmSeverity_Type(Integer32):
    """Custom type teraHistoryAlarmSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraHistoryAlarmSeverity_Type.__name__ = "Integer32"
_TeraHistoryAlarmSeverity_Object = MibTableColumn
teraHistoryAlarmSeverity = _TeraHistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 8),
    _TeraHistoryAlarmSeverity_Type()
)
teraHistoryAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmSeverity.setStatus("mandatory")
_TeraHistoryAlarmStart_Type = OctetString
_TeraHistoryAlarmStart_Object = MibTableColumn
teraHistoryAlarmStart = _TeraHistoryAlarmStart_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 9),
    _TeraHistoryAlarmStart_Type()
)
teraHistoryAlarmStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmStart.setStatus("mandatory")
_TeraHistoryAlarmStop_Type = OctetString
_TeraHistoryAlarmStop_Object = MibTableColumn
teraHistoryAlarmStop = _TeraHistoryAlarmStop_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 10),
    _TeraHistoryAlarmStop_Type()
)
teraHistoryAlarmStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmStop.setStatus("mandatory")


class _TeraHistoryActiveAlarmSequence_Type(Counter32):
    """Custom type teraHistoryActiveAlarmSequence based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraHistoryActiveAlarmSequence_Type.__name__ = "Counter32"
_TeraHistoryActiveAlarmSequence_Object = MibTableColumn
teraHistoryActiveAlarmSequence = _TeraHistoryActiveAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 11),
    _TeraHistoryActiveAlarmSequence_Type()
)
teraHistoryActiveAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryActiveAlarmSequence.setStatus("mandatory")
_TeraHistoryAlarmMessage_Type = OctetString
_TeraHistoryAlarmMessage_Object = MibTableColumn
teraHistoryAlarmMessage = _TeraHistoryAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 12),
    _TeraHistoryAlarmMessage_Type()
)
teraHistoryAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmMessage.setStatus("mandatory")
_TeraHistoryAlarmStartInSecs_Type = Integer32
_TeraHistoryAlarmStartInSecs_Object = MibTableColumn
teraHistoryAlarmStartInSecs = _TeraHistoryAlarmStartInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 13),
    _TeraHistoryAlarmStartInSecs_Type()
)
teraHistoryAlarmStartInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmStartInSecs.setStatus("mandatory")
_TeraHistoryAlarmStopInSecs_Type = Integer32
_TeraHistoryAlarmStopInSecs_Object = MibTableColumn
teraHistoryAlarmStopInSecs = _TeraHistoryAlarmStopInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 14),
    _TeraHistoryAlarmStopInSecs_Type()
)
teraHistoryAlarmStopInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmStopInSecs.setStatus("mandatory")
_TeraHistoryAlarmNEClli_Type = OctetString
_TeraHistoryAlarmNEClli_Object = MibTableColumn
teraHistoryAlarmNEClli = _TeraHistoryAlarmNEClli_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 3, 1, 15),
    _TeraHistoryAlarmNEClli_Type()
)
teraHistoryAlarmNEClli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraHistoryAlarmNEClli.setStatus("mandatory")
_TeraEventTable_Object = MibTable
teraEventTable = _TeraEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4)
)
if mibBuilder.loadTexts:
    teraEventTable.setStatus("mandatory")
_TeraEventTableEntry_Object = MibTableRow
teraEventTableEntry = _TeraEventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1)
)
teraEventTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraInstallSlotNumber"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraPonIndex"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraEventIndex"),
)
if mibBuilder.loadTexts:
    teraEventTableEntry.setStatus("mandatory")


class _TeraEventIndex_Type(Counter32):
    """Custom type teraEventIndex based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraEventIndex_Type.__name__ = "Counter32"
_TeraEventIndex_Object = MibTableColumn
teraEventIndex = _TeraEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 1),
    _TeraEventIndex_Type()
)
teraEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventIndex.setStatus("mandatory")
_TeraEventPort_Type = Integer32
_TeraEventPort_Object = MibTableColumn
teraEventPort = _TeraEventPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 2),
    _TeraEventPort_Type()
)
teraEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventPort.setStatus("mandatory")
_TeraEventPortType_Type = Integer32
_TeraEventPortType_Object = MibTableColumn
teraEventPortType = _TeraEventPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 3),
    _TeraEventPortType_Type()
)
teraEventPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventPortType.setStatus("mandatory")
_TeraEventCardType_Type = Integer32
_TeraEventCardType_Object = MibTableColumn
teraEventCardType = _TeraEventCardType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 4),
    _TeraEventCardType_Type()
)
teraEventCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventCardType.setStatus("mandatory")
_TeraEventSlot_Type = Integer32
_TeraEventSlot_Object = MibTableColumn
teraEventSlot = _TeraEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 5),
    _TeraEventSlot_Type()
)
teraEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventSlot.setStatus("mandatory")
_TeraEventPhysPort_Type = Integer32
_TeraEventPhysPort_Object = MibTableColumn
teraEventPhysPort = _TeraEventPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 6),
    _TeraEventPhysPort_Type()
)
teraEventPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventPhysPort.setStatus("mandatory")
_TeraEventType_Type = Integer32
_TeraEventType_Object = MibTableColumn
teraEventType = _TeraEventType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 7),
    _TeraEventType_Type()
)
teraEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventType.setStatus("mandatory")


class _TeraEventSeverity_Type(Integer32):
    """Custom type teraEventSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraEventSeverity_Type.__name__ = "Integer32"
_TeraEventSeverity_Object = MibTableColumn
teraEventSeverity = _TeraEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 8),
    _TeraEventSeverity_Type()
)
teraEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventSeverity.setStatus("mandatory")
_TeraEventTime_Type = OctetString
_TeraEventTime_Object = MibTableColumn
teraEventTime = _TeraEventTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 9),
    _TeraEventTime_Type()
)
teraEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventTime.setStatus("mandatory")
_TeraEventMessage_Type = OctetString
_TeraEventMessage_Object = MibTableColumn
teraEventMessage = _TeraEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 10),
    _TeraEventMessage_Type()
)
teraEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventMessage.setStatus("mandatory")
_TeraEventTimeInSecs_Type = Integer32
_TeraEventTimeInSecs_Object = MibTableColumn
teraEventTimeInSecs = _TeraEventTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 11),
    _TeraEventTimeInSecs_Type()
)
teraEventTimeInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventTimeInSecs.setStatus("mandatory")
_TeraEventNEClli_Type = OctetString
_TeraEventNEClli_Object = MibTableColumn
teraEventNEClli = _TeraEventNEClli_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 4, 1, 12),
    _TeraEventNEClli_Type()
)
teraEventNEClli.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraEventNEClli.setStatus("mandatory")
_TeraAlarmConfigTable_Object = MibTable
teraAlarmConfigTable = _TeraAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 5)
)
if mibBuilder.loadTexts:
    teraAlarmConfigTable.setStatus("mandatory")
_TeraAlarmConfigTableEntry_Object = MibTableRow
teraAlarmConfigTableEntry = _TeraAlarmConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 5, 1)
)
teraAlarmConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraActiveAlarmType"),
)
if mibBuilder.loadTexts:
    teraAlarmConfigTableEntry.setStatus("mandatory")


class _TeraAlarmConfigFilter_Type(Integer32):
    """Custom type teraAlarmConfigFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("log", 2),
          ("report", 3))
    )


_TeraAlarmConfigFilter_Type.__name__ = "Integer32"
_TeraAlarmConfigFilter_Object = MibTableColumn
teraAlarmConfigFilter = _TeraAlarmConfigFilter_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 5, 1, 1),
    _TeraAlarmConfigFilter_Type()
)
teraAlarmConfigFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAlarmConfigFilter.setStatus("mandatory")


class _TeraAlarmConfigSeverity_Type(Integer32):
    """Custom type teraAlarmConfigSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraAlarmConfigSeverity_Type.__name__ = "Integer32"
_TeraAlarmConfigSeverity_Object = MibTableColumn
teraAlarmConfigSeverity = _TeraAlarmConfigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 5, 1, 2),
    _TeraAlarmConfigSeverity_Type()
)
teraAlarmConfigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAlarmConfigSeverity.setStatus("mandatory")
_TeraEventConfigTable_Object = MibTable
teraEventConfigTable = _TeraEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 6)
)
if mibBuilder.loadTexts:
    teraEventConfigTable.setStatus("mandatory")
_TeraEventConfigTableEntry_Object = MibTableRow
teraEventConfigTableEntry = _TeraEventConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 6, 1)
)
teraEventConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraEventType"),
)
if mibBuilder.loadTexts:
    teraEventConfigTableEntry.setStatus("mandatory")


class _TeraEventConfigFilter_Type(Integer32):
    """Custom type teraEventConfigFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("log", 2),
          ("report", 3))
    )


_TeraEventConfigFilter_Type.__name__ = "Integer32"
_TeraEventConfigFilter_Object = MibTableColumn
teraEventConfigFilter = _TeraEventConfigFilter_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 6, 1, 1),
    _TeraEventConfigFilter_Type()
)
teraEventConfigFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEventConfigFilter.setStatus("mandatory")


class _TeraEventConfigSeverity_Type(Integer32):
    """Custom type teraEventConfigSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraEventConfigSeverity_Type.__name__ = "Integer32"
_TeraEventConfigSeverity_Object = MibTableColumn
teraEventConfigSeverity = _TeraEventConfigSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 6, 1, 2),
    _TeraEventConfigSeverity_Type()
)
teraEventConfigSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEventConfigSeverity.setStatus("mandatory")
_TeraAllActiveAlarmTable_Object = MibTable
teraAllActiveAlarmTable = _TeraAllActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7)
)
if mibBuilder.loadTexts:
    teraAllActiveAlarmTable.setStatus("mandatory")
_TeraAllActiveAlarmTableEntry_Object = MibTableRow
teraAllActiveAlarmTableEntry = _TeraAllActiveAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1)
)
teraAllActiveAlarmTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraAllActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    teraAllActiveAlarmTableEntry.setStatus("mandatory")
_TeraAllActiveAlarmIndex_Type = Counter32
_TeraAllActiveAlarmIndex_Object = MibTableColumn
teraAllActiveAlarmIndex = _TeraAllActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 1),
    _TeraAllActiveAlarmIndex_Type()
)
teraAllActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmIndex.setStatus("mandatory")
_TeraAllActiveAlarmPort_Type = Integer32
_TeraAllActiveAlarmPort_Object = MibTableColumn
teraAllActiveAlarmPort = _TeraAllActiveAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 2),
    _TeraAllActiveAlarmPort_Type()
)
teraAllActiveAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmPort.setStatus("mandatory")
_TeraAllActiveAlarmPortType_Type = Integer32
_TeraAllActiveAlarmPortType_Object = MibTableColumn
teraAllActiveAlarmPortType = _TeraAllActiveAlarmPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 3),
    _TeraAllActiveAlarmPortType_Type()
)
teraAllActiveAlarmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmPortType.setStatus("mandatory")
_TeraAllActiveAlarmCardType_Type = Integer32
_TeraAllActiveAlarmCardType_Object = MibTableColumn
teraAllActiveAlarmCardType = _TeraAllActiveAlarmCardType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 4),
    _TeraAllActiveAlarmCardType_Type()
)
teraAllActiveAlarmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmCardType.setStatus("mandatory")
_TeraAllActiveAlarmSlot_Type = Integer32
_TeraAllActiveAlarmSlot_Object = MibTableColumn
teraAllActiveAlarmSlot = _TeraAllActiveAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 5),
    _TeraAllActiveAlarmSlot_Type()
)
teraAllActiveAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmSlot.setStatus("mandatory")
_TeraAllActiveAlarmPhysPort_Type = Integer32
_TeraAllActiveAlarmPhysPort_Object = MibTableColumn
teraAllActiveAlarmPhysPort = _TeraAllActiveAlarmPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 6),
    _TeraAllActiveAlarmPhysPort_Type()
)
teraAllActiveAlarmPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmPhysPort.setStatus("mandatory")
_TeraAllActiveAlarmType_Type = Integer32
_TeraAllActiveAlarmType_Object = MibTableColumn
teraAllActiveAlarmType = _TeraAllActiveAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 7),
    _TeraAllActiveAlarmType_Type()
)
teraAllActiveAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmType.setStatus("mandatory")


class _TeraAllActiveAlarmSeverity_Type(Integer32):
    """Custom type teraAllActiveAlarmSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraAllActiveAlarmSeverity_Type.__name__ = "Integer32"
_TeraAllActiveAlarmSeverity_Object = MibTableColumn
teraAllActiveAlarmSeverity = _TeraAllActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 8),
    _TeraAllActiveAlarmSeverity_Type()
)
teraAllActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmSeverity.setStatus("mandatory")
_TeraAllActiveAlarmTime_Type = OctetString
_TeraAllActiveAlarmTime_Object = MibTableColumn
teraAllActiveAlarmTime = _TeraAllActiveAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 9),
    _TeraAllActiveAlarmTime_Type()
)
teraAllActiveAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmTime.setStatus("mandatory")
_TeraAllActiveAlarmMessage_Type = OctetString
_TeraAllActiveAlarmMessage_Object = MibTableColumn
teraAllActiveAlarmMessage = _TeraAllActiveAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 10),
    _TeraAllActiveAlarmMessage_Type()
)
teraAllActiveAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmMessage.setStatus("mandatory")
_TeraAllActiveAlarmTimeInSecs_Type = Integer32
_TeraAllActiveAlarmTimeInSecs_Object = MibTableColumn
teraAllActiveAlarmTimeInSecs = _TeraAllActiveAlarmTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 7, 1, 11),
    _TeraAllActiveAlarmTimeInSecs_Type()
)
teraAllActiveAlarmTimeInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAllActiveAlarmTimeInSecs.setStatus("mandatory")
_TeraLocalActiveAlarmTable_Object = MibTable
teraLocalActiveAlarmTable = _TeraLocalActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8)
)
if mibBuilder.loadTexts:
    teraLocalActiveAlarmTable.setStatus("mandatory")
_TeraLocalActiveAlarmTableEntry_Object = MibTableRow
teraLocalActiveAlarmTableEntry = _TeraLocalActiveAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1)
)
teraLocalActiveAlarmTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraLocalActiveAlarmSequence"),
)
if mibBuilder.loadTexts:
    teraLocalActiveAlarmTableEntry.setStatus("mandatory")


class _TeraLocalActiveAlarmSequence_Type(Counter32):
    """Custom type teraLocalActiveAlarmSequence based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLocalActiveAlarmSequence_Type.__name__ = "Counter32"
_TeraLocalActiveAlarmSequence_Object = MibTableColumn
teraLocalActiveAlarmSequence = _TeraLocalActiveAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 1),
    _TeraLocalActiveAlarmSequence_Type()
)
teraLocalActiveAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmSequence.setStatus("mandatory")
_TeraLocalActiveAlarmPort_Type = Integer32
_TeraLocalActiveAlarmPort_Object = MibTableColumn
teraLocalActiveAlarmPort = _TeraLocalActiveAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 2),
    _TeraLocalActiveAlarmPort_Type()
)
teraLocalActiveAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmPort.setStatus("mandatory")
_TeraLocalActiveAlarmPortType_Type = Integer32
_TeraLocalActiveAlarmPortType_Object = MibTableColumn
teraLocalActiveAlarmPortType = _TeraLocalActiveAlarmPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 3),
    _TeraLocalActiveAlarmPortType_Type()
)
teraLocalActiveAlarmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmPortType.setStatus("mandatory")
_TeraLocalActiveAlarmCardType_Type = Integer32
_TeraLocalActiveAlarmCardType_Object = MibTableColumn
teraLocalActiveAlarmCardType = _TeraLocalActiveAlarmCardType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 4),
    _TeraLocalActiveAlarmCardType_Type()
)
teraLocalActiveAlarmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmCardType.setStatus("mandatory")
_TeraLocalActiveAlarmSlot_Type = Integer32
_TeraLocalActiveAlarmSlot_Object = MibTableColumn
teraLocalActiveAlarmSlot = _TeraLocalActiveAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 5),
    _TeraLocalActiveAlarmSlot_Type()
)
teraLocalActiveAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmSlot.setStatus("mandatory")
_TeraLocalActiveAlarmPhysPort_Type = Integer32
_TeraLocalActiveAlarmPhysPort_Object = MibTableColumn
teraLocalActiveAlarmPhysPort = _TeraLocalActiveAlarmPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 6),
    _TeraLocalActiveAlarmPhysPort_Type()
)
teraLocalActiveAlarmPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmPhysPort.setStatus("mandatory")
_TeraLocalActiveAlarmType_Type = Integer32
_TeraLocalActiveAlarmType_Object = MibTableColumn
teraLocalActiveAlarmType = _TeraLocalActiveAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 7),
    _TeraLocalActiveAlarmType_Type()
)
teraLocalActiveAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmType.setStatus("mandatory")


class _TeraLocalActiveAlarmSeverity_Type(Integer32):
    """Custom type teraLocalActiveAlarmSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraLocalActiveAlarmSeverity_Type.__name__ = "Integer32"
_TeraLocalActiveAlarmSeverity_Object = MibTableColumn
teraLocalActiveAlarmSeverity = _TeraLocalActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 8),
    _TeraLocalActiveAlarmSeverity_Type()
)
teraLocalActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmSeverity.setStatus("mandatory")
_TeraLocalActiveAlarmTime_Type = OctetString
_TeraLocalActiveAlarmTime_Object = MibTableColumn
teraLocalActiveAlarmTime = _TeraLocalActiveAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 9),
    _TeraLocalActiveAlarmTime_Type()
)
teraLocalActiveAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmTime.setStatus("mandatory")
_TeraLocalActiveAlarmMessage_Type = OctetString
_TeraLocalActiveAlarmMessage_Object = MibTableColumn
teraLocalActiveAlarmMessage = _TeraLocalActiveAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 10),
    _TeraLocalActiveAlarmMessage_Type()
)
teraLocalActiveAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmMessage.setStatus("mandatory")
_TeraLocalActiveAlarmTimeInSecs_Type = Integer32
_TeraLocalActiveAlarmTimeInSecs_Object = MibTableColumn
teraLocalActiveAlarmTimeInSecs = _TeraLocalActiveAlarmTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 8, 1, 11),
    _TeraLocalActiveAlarmTimeInSecs_Type()
)
teraLocalActiveAlarmTimeInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalActiveAlarmTimeInSecs.setStatus("mandatory")
_TeraLocalHistoryAlarmTable_Object = MibTable
teraLocalHistoryAlarmTable = _TeraLocalHistoryAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9)
)
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmTable.setStatus("mandatory")
_TeraLocalHistoryAlarmTableEntry_Object = MibTableRow
teraLocalHistoryAlarmTableEntry = _TeraLocalHistoryAlarmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1)
)
teraLocalHistoryAlarmTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraLocalHistoryAlarmSequence"),
)
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmTableEntry.setStatus("mandatory")


class _TeraLocalHistoryAlarmSequence_Type(Counter32):
    """Custom type teraLocalHistoryAlarmSequence based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLocalHistoryAlarmSequence_Type.__name__ = "Counter32"
_TeraLocalHistoryAlarmSequence_Object = MibTableColumn
teraLocalHistoryAlarmSequence = _TeraLocalHistoryAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 1),
    _TeraLocalHistoryAlarmSequence_Type()
)
teraLocalHistoryAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmSequence.setStatus("mandatory")
_TeraLocalHistoryAlarmPort_Type = Integer32
_TeraLocalHistoryAlarmPort_Object = MibTableColumn
teraLocalHistoryAlarmPort = _TeraLocalHistoryAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 2),
    _TeraLocalHistoryAlarmPort_Type()
)
teraLocalHistoryAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmPort.setStatus("mandatory")
_TeraLocalHistoryAlarmPortType_Type = Integer32
_TeraLocalHistoryAlarmPortType_Object = MibTableColumn
teraLocalHistoryAlarmPortType = _TeraLocalHistoryAlarmPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 3),
    _TeraLocalHistoryAlarmPortType_Type()
)
teraLocalHistoryAlarmPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmPortType.setStatus("mandatory")
_TeraLocalHistoryAlarmCardType_Type = Integer32
_TeraLocalHistoryAlarmCardType_Object = MibTableColumn
teraLocalHistoryAlarmCardType = _TeraLocalHistoryAlarmCardType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 4),
    _TeraLocalHistoryAlarmCardType_Type()
)
teraLocalHistoryAlarmCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmCardType.setStatus("mandatory")
_TeraLocalHistoryAlarmSlot_Type = Integer32
_TeraLocalHistoryAlarmSlot_Object = MibTableColumn
teraLocalHistoryAlarmSlot = _TeraLocalHistoryAlarmSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 5),
    _TeraLocalHistoryAlarmSlot_Type()
)
teraLocalHistoryAlarmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmSlot.setStatus("mandatory")
_TeraLocalHistoryAlarmPhysPort_Type = Integer32
_TeraLocalHistoryAlarmPhysPort_Object = MibTableColumn
teraLocalHistoryAlarmPhysPort = _TeraLocalHistoryAlarmPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 6),
    _TeraLocalHistoryAlarmPhysPort_Type()
)
teraLocalHistoryAlarmPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmPhysPort.setStatus("mandatory")
_TeraLocalHistoryAlarmType_Type = Integer32
_TeraLocalHistoryAlarmType_Object = MibTableColumn
teraLocalHistoryAlarmType = _TeraLocalHistoryAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 7),
    _TeraLocalHistoryAlarmType_Type()
)
teraLocalHistoryAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmType.setStatus("mandatory")


class _TeraLocalHistoryAlarmSeverity_Type(Integer32):
    """Custom type teraLocalHistoryAlarmSeverity based on Integer32"""
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
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraLocalHistoryAlarmSeverity_Type.__name__ = "Integer32"
_TeraLocalHistoryAlarmSeverity_Object = MibTableColumn
teraLocalHistoryAlarmSeverity = _TeraLocalHistoryAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 8),
    _TeraLocalHistoryAlarmSeverity_Type()
)
teraLocalHistoryAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmSeverity.setStatus("mandatory")
_TeraLocalHistoryAlarmStart_Type = OctetString
_TeraLocalHistoryAlarmStart_Object = MibTableColumn
teraLocalHistoryAlarmStart = _TeraLocalHistoryAlarmStart_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 9),
    _TeraLocalHistoryAlarmStart_Type()
)
teraLocalHistoryAlarmStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmStart.setStatus("mandatory")
_TeraLocalHistoryAlarmStop_Type = OctetString
_TeraLocalHistoryAlarmStop_Object = MibTableColumn
teraLocalHistoryAlarmStop = _TeraLocalHistoryAlarmStop_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 10),
    _TeraLocalHistoryAlarmStop_Type()
)
teraLocalHistoryAlarmStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmStop.setStatus("mandatory")


class _TeraLocalHistoryActiveAlarmSequence_Type(Counter32):
    """Custom type teraLocalHistoryActiveAlarmSequence based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLocalHistoryActiveAlarmSequence_Type.__name__ = "Counter32"
_TeraLocalHistoryActiveAlarmSequence_Object = MibTableColumn
teraLocalHistoryActiveAlarmSequence = _TeraLocalHistoryActiveAlarmSequence_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 11),
    _TeraLocalHistoryActiveAlarmSequence_Type()
)
teraLocalHistoryActiveAlarmSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryActiveAlarmSequence.setStatus("mandatory")
_TeraLocalHistoryActiveAlarmMessage_Type = OctetString
_TeraLocalHistoryActiveAlarmMessage_Object = MibTableColumn
teraLocalHistoryActiveAlarmMessage = _TeraLocalHistoryActiveAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 12),
    _TeraLocalHistoryActiveAlarmMessage_Type()
)
teraLocalHistoryActiveAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryActiveAlarmMessage.setStatus("mandatory")
_TeraLocalHistoryAlarmStartInSecs_Type = Integer32
_TeraLocalHistoryAlarmStartInSecs_Object = MibTableColumn
teraLocalHistoryAlarmStartInSecs = _TeraLocalHistoryAlarmStartInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 13),
    _TeraLocalHistoryAlarmStartInSecs_Type()
)
teraLocalHistoryAlarmStartInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmStartInSecs.setStatus("mandatory")
_TeraLocalHistoryAlarmStopInSecs_Type = Integer32
_TeraLocalHistoryAlarmStopInSecs_Object = MibTableColumn
teraLocalHistoryAlarmStopInSecs = _TeraLocalHistoryAlarmStopInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 9, 1, 14),
    _TeraLocalHistoryAlarmStopInSecs_Type()
)
teraLocalHistoryAlarmStopInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalHistoryAlarmStopInSecs.setStatus("mandatory")
_TeraAlarmPortFilterTable_Object = MibTable
teraAlarmPortFilterTable = _TeraAlarmPortFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 10)
)
if mibBuilder.loadTexts:
    teraAlarmPortFilterTable.setStatus("mandatory")
_TeraAlarmPortFilterTableEntry_Object = MibTableRow
teraAlarmPortFilterTableEntry = _TeraAlarmPortFilterTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 10, 1)
)
teraAlarmPortFilterTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraActiveAlarmPort"),
)
if mibBuilder.loadTexts:
    teraAlarmPortFilterTableEntry.setStatus("mandatory")


class _TeraAlarmPortFilter_Type(Integer32):
    """Custom type teraAlarmPortFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TeraAlarmPortFilter_Type.__name__ = "Integer32"
_TeraAlarmPortFilter_Object = MibTableColumn
teraAlarmPortFilter = _TeraAlarmPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 10, 1, 1),
    _TeraAlarmPortFilter_Type()
)
teraAlarmPortFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAlarmPortFilter.setStatus("mandatory")


class _TeraEventPortFilter_Type(Integer32):
    """Custom type teraEventPortFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_TeraEventPortFilter_Type.__name__ = "Integer32"
_TeraEventPortFilter_Object = MibTableColumn
teraEventPortFilter = _TeraEventPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 10, 1, 2),
    _TeraEventPortFilter_Type()
)
teraEventPortFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraEventPortFilter.setStatus("mandatory")


class _TeraAlarmPortFilterTableStatus_Type(Integer32):
    """Custom type teraAlarmPortFilterTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_TeraAlarmPortFilterTableStatus_Type.__name__ = "Integer32"
_TeraAlarmPortFilterTableStatus_Object = MibTableColumn
teraAlarmPortFilterTableStatus = _TeraAlarmPortFilterTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 10, 1, 3),
    _TeraAlarmPortFilterTableStatus_Type()
)
teraAlarmPortFilterTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAlarmPortFilterTableStatus.setStatus("mandatory")
_TeraAlarmPortMaskTable_Object = MibTable
teraAlarmPortMaskTable = _TeraAlarmPortMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 14)
)
if mibBuilder.loadTexts:
    teraAlarmPortMaskTable.setStatus("mandatory")
_TeraAlarmPortMaskTableEntry_Object = MibTableRow
teraAlarmPortMaskTableEntry = _TeraAlarmPortMaskTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 14, 1)
)
teraAlarmPortMaskTableEntry.setIndexNames(
    (0, "TERAWAVE-teraAlarm-MIB", "teraAlarmPortMaskSlot"),
    (0, "TERAWAVE-teraAlarm-MIB", "teraAlarmPortMaskPort"),
)
if mibBuilder.loadTexts:
    teraAlarmPortMaskTableEntry.setStatus("mandatory")
_TeraAlarmPortMaskSlot_Type = Integer32
_TeraAlarmPortMaskSlot_Object = MibTableColumn
teraAlarmPortMaskSlot = _TeraAlarmPortMaskSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 14, 1, 1),
    _TeraAlarmPortMaskSlot_Type()
)
teraAlarmPortMaskSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAlarmPortMaskSlot.setStatus("mandatory")
_TeraAlarmPortMaskPort_Type = Integer32
_TeraAlarmPortMaskPort_Object = MibTableColumn
teraAlarmPortMaskPort = _TeraAlarmPortMaskPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 14, 1, 2),
    _TeraAlarmPortMaskPort_Type()
)
teraAlarmPortMaskPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraAlarmPortMaskPort.setStatus("mandatory")


class _TeraAlarmPortUnMask_Type(Integer32):
    """Custom type teraAlarmPortUnMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("mask", 1),
          ("unmask", 2))
    )


_TeraAlarmPortUnMask_Type.__name__ = "Integer32"
_TeraAlarmPortUnMask_Object = MibTableColumn
teraAlarmPortUnMask = _TeraAlarmPortUnMask_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 14, 1, 3),
    _TeraAlarmPortUnMask_Type()
)
teraAlarmPortUnMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraAlarmPortUnMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraAlarm-MIB",
    **{"terawave": terawave,
       "teratraps": teratraps,
       "teraAlarms": teraAlarms,
       "teraConfig": teraConfig,
       "teraNextAlarmSequenceTable": teraNextAlarmSequenceTable,
       "teraNextAlarmSequenceTableEntry": teraNextAlarmSequenceTableEntry,
       "teraNextAlarmSequence": teraNextAlarmSequence,
       "teraLocalNextAlarmSequence": teraLocalNextAlarmSequence,
       "teraResetAlarmHistoryTable": teraResetAlarmHistoryTable,
       "teraResetEventTable": teraResetEventTable,
       "teraAlarmReportingTable": teraAlarmReportingTable,
       "teraAlarmReportingTableEntry": teraAlarmReportingTableEntry,
       "teraAlarmReportingTableIndex": teraAlarmReportingTableIndex,
       "teraAlarmReportingIPaddress": teraAlarmReportingIPaddress,
       "teraAlarmReportingCommunity": teraAlarmReportingCommunity,
       "teraActiveAlarmTable": teraActiveAlarmTable,
       "teraActiveAlarmTableEntry": teraActiveAlarmTableEntry,
       "teraActiveAlarmSequence": teraActiveAlarmSequence,
       "teraActiveAlarmPort": teraActiveAlarmPort,
       "teraActiveAlarmPortType": teraActiveAlarmPortType,
       "teraActiveAlarmCardType": teraActiveAlarmCardType,
       "teraActiveAlarmSlot": teraActiveAlarmSlot,
       "teraActiveAlarmPhysPort": teraActiveAlarmPhysPort,
       "teraActiveAlarmType": teraActiveAlarmType,
       "teraActiveAlarmSeverity": teraActiveAlarmSeverity,
       "teraActiveAlarmTime": teraActiveAlarmTime,
       "teraActiveAlarmMessage": teraActiveAlarmMessage,
       "teraActiveAlarmTimeInSecs": teraActiveAlarmTimeInSecs,
       "teraActiveAlarmNEClli": teraActiveAlarmNEClli,
       "teraHistoryAlarmTable": teraHistoryAlarmTable,
       "teraHistoryAlarmTableEntry": teraHistoryAlarmTableEntry,
       "teraHistoryAlarmSequence": teraHistoryAlarmSequence,
       "teraHistoryAlarmPort": teraHistoryAlarmPort,
       "teraHistoryAlarmPortType": teraHistoryAlarmPortType,
       "teraHistoryAlarmCardType": teraHistoryAlarmCardType,
       "teraHistoryAlarmSlot": teraHistoryAlarmSlot,
       "teraHistoryAlarmPhysPort": teraHistoryAlarmPhysPort,
       "teraHistoryAlarmType": teraHistoryAlarmType,
       "teraHistoryAlarmSeverity": teraHistoryAlarmSeverity,
       "teraHistoryAlarmStart": teraHistoryAlarmStart,
       "teraHistoryAlarmStop": teraHistoryAlarmStop,
       "teraHistoryActiveAlarmSequence": teraHistoryActiveAlarmSequence,
       "teraHistoryAlarmMessage": teraHistoryAlarmMessage,
       "teraHistoryAlarmStartInSecs": teraHistoryAlarmStartInSecs,
       "teraHistoryAlarmStopInSecs": teraHistoryAlarmStopInSecs,
       "teraHistoryAlarmNEClli": teraHistoryAlarmNEClli,
       "teraEventTable": teraEventTable,
       "teraEventTableEntry": teraEventTableEntry,
       "teraEventIndex": teraEventIndex,
       "teraEventPort": teraEventPort,
       "teraEventPortType": teraEventPortType,
       "teraEventCardType": teraEventCardType,
       "teraEventSlot": teraEventSlot,
       "teraEventPhysPort": teraEventPhysPort,
       "teraEventType": teraEventType,
       "teraEventSeverity": teraEventSeverity,
       "teraEventTime": teraEventTime,
       "teraEventMessage": teraEventMessage,
       "teraEventTimeInSecs": teraEventTimeInSecs,
       "teraEventNEClli": teraEventNEClli,
       "teraAlarmConfigTable": teraAlarmConfigTable,
       "teraAlarmConfigTableEntry": teraAlarmConfigTableEntry,
       "teraAlarmConfigFilter": teraAlarmConfigFilter,
       "teraAlarmConfigSeverity": teraAlarmConfigSeverity,
       "teraEventConfigTable": teraEventConfigTable,
       "teraEventConfigTableEntry": teraEventConfigTableEntry,
       "teraEventConfigFilter": teraEventConfigFilter,
       "teraEventConfigSeverity": teraEventConfigSeverity,
       "teraAllActiveAlarmTable": teraAllActiveAlarmTable,
       "teraAllActiveAlarmTableEntry": teraAllActiveAlarmTableEntry,
       "teraAllActiveAlarmIndex": teraAllActiveAlarmIndex,
       "teraAllActiveAlarmPort": teraAllActiveAlarmPort,
       "teraAllActiveAlarmPortType": teraAllActiveAlarmPortType,
       "teraAllActiveAlarmCardType": teraAllActiveAlarmCardType,
       "teraAllActiveAlarmSlot": teraAllActiveAlarmSlot,
       "teraAllActiveAlarmPhysPort": teraAllActiveAlarmPhysPort,
       "teraAllActiveAlarmType": teraAllActiveAlarmType,
       "teraAllActiveAlarmSeverity": teraAllActiveAlarmSeverity,
       "teraAllActiveAlarmTime": teraAllActiveAlarmTime,
       "teraAllActiveAlarmMessage": teraAllActiveAlarmMessage,
       "teraAllActiveAlarmTimeInSecs": teraAllActiveAlarmTimeInSecs,
       "teraLocalActiveAlarmTable": teraLocalActiveAlarmTable,
       "teraLocalActiveAlarmTableEntry": teraLocalActiveAlarmTableEntry,
       "teraLocalActiveAlarmSequence": teraLocalActiveAlarmSequence,
       "teraLocalActiveAlarmPort": teraLocalActiveAlarmPort,
       "teraLocalActiveAlarmPortType": teraLocalActiveAlarmPortType,
       "teraLocalActiveAlarmCardType": teraLocalActiveAlarmCardType,
       "teraLocalActiveAlarmSlot": teraLocalActiveAlarmSlot,
       "teraLocalActiveAlarmPhysPort": teraLocalActiveAlarmPhysPort,
       "teraLocalActiveAlarmType": teraLocalActiveAlarmType,
       "teraLocalActiveAlarmSeverity": teraLocalActiveAlarmSeverity,
       "teraLocalActiveAlarmTime": teraLocalActiveAlarmTime,
       "teraLocalActiveAlarmMessage": teraLocalActiveAlarmMessage,
       "teraLocalActiveAlarmTimeInSecs": teraLocalActiveAlarmTimeInSecs,
       "teraLocalHistoryAlarmTable": teraLocalHistoryAlarmTable,
       "teraLocalHistoryAlarmTableEntry": teraLocalHistoryAlarmTableEntry,
       "teraLocalHistoryAlarmSequence": teraLocalHistoryAlarmSequence,
       "teraLocalHistoryAlarmPort": teraLocalHistoryAlarmPort,
       "teraLocalHistoryAlarmPortType": teraLocalHistoryAlarmPortType,
       "teraLocalHistoryAlarmCardType": teraLocalHistoryAlarmCardType,
       "teraLocalHistoryAlarmSlot": teraLocalHistoryAlarmSlot,
       "teraLocalHistoryAlarmPhysPort": teraLocalHistoryAlarmPhysPort,
       "teraLocalHistoryAlarmType": teraLocalHistoryAlarmType,
       "teraLocalHistoryAlarmSeverity": teraLocalHistoryAlarmSeverity,
       "teraLocalHistoryAlarmStart": teraLocalHistoryAlarmStart,
       "teraLocalHistoryAlarmStop": teraLocalHistoryAlarmStop,
       "teraLocalHistoryActiveAlarmSequence": teraLocalHistoryActiveAlarmSequence,
       "teraLocalHistoryActiveAlarmMessage": teraLocalHistoryActiveAlarmMessage,
       "teraLocalHistoryAlarmStartInSecs": teraLocalHistoryAlarmStartInSecs,
       "teraLocalHistoryAlarmStopInSecs": teraLocalHistoryAlarmStopInSecs,
       "teraAlarmPortFilterTable": teraAlarmPortFilterTable,
       "teraAlarmPortFilterTableEntry": teraAlarmPortFilterTableEntry,
       "teraAlarmPortFilter": teraAlarmPortFilter,
       "teraEventPortFilter": teraEventPortFilter,
       "teraAlarmPortFilterTableStatus": teraAlarmPortFilterTableStatus,
       "teraAlarmPortMaskTable": teraAlarmPortMaskTable,
       "teraAlarmPortMaskTableEntry": teraAlarmPortMaskTableEntry,
       "teraAlarmPortMaskSlot": teraAlarmPortMaskSlot,
       "teraAlarmPortMaskPort": teraAlarmPortMaskPort,
       "teraAlarmPortUnMask": teraAlarmPortUnMask}
)
