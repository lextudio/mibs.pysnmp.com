# SNMP MIB module (TIARA-V35-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-V35-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:45 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tiaraInterfaces,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraInterfaces")


# MODULE-IDENTITY

tiaraV35Mib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3)
)
tiaraV35Mib.setRevisions(
        ("1900-08-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_V35ConfigTable_Object = MibTable
v35ConfigTable = _V35ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1)
)
if mibBuilder.loadTexts:
    v35ConfigTable.setStatus("current")
_V35ConfigTableEntry_Object = MibTableRow
v35ConfigTableEntry = _V35ConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1)
)
v35ConfigTableEntry.setIndexNames(
    (0, "TIARA-V35-MIB", "v35IfIndex"),
)
if mibBuilder.loadTexts:
    v35ConfigTableEntry.setStatus("current")
_V35IfIndex_Type = Integer32
_V35IfIndex_Object = MibTableColumn
v35IfIndex = _V35IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 1),
    _V35IfIndex_Type()
)
v35IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v35IfIndex.setStatus("current")


class _V35ConfigClockRate_Type(Integer32):
    """Custom type v35ConfigClockRate based on Integer32"""
    defaultValue = 8000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 8000000),
    )


_V35ConfigClockRate_Type.__name__ = "Integer32"
_V35ConfigClockRate_Object = MibTableColumn
v35ConfigClockRate = _V35ConfigClockRate_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 2),
    _V35ConfigClockRate_Type()
)
v35ConfigClockRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v35ConfigClockRate.setStatus("current")


class _V35ConfigClockSource_Type(Integer32):
    """Custom type v35ConfigClockSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("line", 2))
    )


_V35ConfigClockSource_Type.__name__ = "Integer32"
_V35ConfigClockSource_Object = MibTableColumn
v35ConfigClockSource = _V35ConfigClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 3),
    _V35ConfigClockSource_Type()
)
v35ConfigClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v35ConfigClockSource.setStatus("current")


class _V35ConfigMode_Type(Integer32):
    """Custom type v35ConfigMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 2))
    )


_V35ConfigMode_Type.__name__ = "Integer32"
_V35ConfigMode_Object = MibTableColumn
v35ConfigMode = _V35ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 4),
    _V35ConfigMode_Type()
)
v35ConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v35ConfigMode.setStatus("current")


class _V35ConfigCRC_Type(Integer32):
    """Custom type v35ConfigCRC based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 1),
          ("crc32", 2))
    )


_V35ConfigCRC_Type.__name__ = "Integer32"
_V35ConfigCRC_Object = MibTableColumn
v35ConfigCRC = _V35ConfigCRC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 5),
    _V35ConfigCRC_Type()
)
v35ConfigCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v35ConfigCRC.setStatus("current")


class _V35ConfigDataMode_Type(Integer32):
    """Custom type v35ConfigDataMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inverted", 2),
          ("normal", 1))
    )


_V35ConfigDataMode_Type.__name__ = "Integer32"
_V35ConfigDataMode_Object = MibTableColumn
v35ConfigDataMode = _V35ConfigDataMode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 6),
    _V35ConfigDataMode_Type()
)
v35ConfigDataMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v35ConfigDataMode.setStatus("current")


class _V35ConfigFlowControl_Type(Integer32):
    """Custom type v35ConfigFlowControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_V35ConfigFlowControl_Type.__name__ = "Integer32"
_V35ConfigFlowControl_Object = MibTableColumn
v35ConfigFlowControl = _V35ConfigFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 1, 1, 7),
    _V35ConfigFlowControl_Type()
)
v35ConfigFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    v35ConfigFlowControl.setStatus("current")
_V35StatsTable_Object = MibTable
v35StatsTable = _V35StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2)
)
if mibBuilder.loadTexts:
    v35StatsTable.setStatus("current")
_V35StatsTableEntry_Object = MibTableRow
v35StatsTableEntry = _V35StatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1)
)
v35StatsTableEntry.setIndexNames(
    (0, "TIARA-V35-MIB", "v35IfIndex"),
)
if mibBuilder.loadTexts:
    v35StatsTableEntry.setStatus("current")


class _V35StatsAlarmStatus_Type(Bits):
    """Custom type v35StatsAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("v35-alarms-CTS", 4),
          ("v35-alarms-DSR", 2),
          ("v35-alarms-DTR", 1),
          ("v35-alarms-RTS", 5),
          ("v35-alarms-ST", 3),
          ("v35-no-alarms", 0))
    )

_V35StatsAlarmStatus_Type.__name__ = "Bits"
_V35StatsAlarmStatus_Object = MibTableColumn
v35StatsAlarmStatus = _V35StatsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 1),
    _V35StatsAlarmStatus_Type()
)
v35StatsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v35StatsAlarmStatus.setStatus("current")
_V35StatsFramesIn_Type = Counter32
_V35StatsFramesIn_Object = MibTableColumn
v35StatsFramesIn = _V35StatsFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 2),
    _V35StatsFramesIn_Type()
)
v35StatsFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v35StatsFramesIn.setStatus("current")
_V35StatsFramesOut_Type = Counter32
_V35StatsFramesOut_Object = MibTableColumn
v35StatsFramesOut = _V35StatsFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 3),
    _V35StatsFramesOut_Type()
)
v35StatsFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v35StatsFramesOut.setStatus("current")
_V35StatsOctetsIn_Type = Counter32
_V35StatsOctetsIn_Object = MibTableColumn
v35StatsOctetsIn = _V35StatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 4),
    _V35StatsOctetsIn_Type()
)
v35StatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v35StatsOctetsIn.setStatus("current")
_V35StatsOctetsOut_Type = Counter32
_V35StatsOctetsOut_Object = MibTableColumn
v35StatsOctetsOut = _V35StatsOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 5),
    _V35StatsOctetsOut_Type()
)
v35StatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v35StatsOctetsOut.setStatus("current")
_V35StatsCRCErrors_Type = Counter32
_V35StatsCRCErrors_Object = MibTableColumn
v35StatsCRCErrors = _V35StatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 2, 1, 6),
    _V35StatsCRCErrors_Type()
)
v35StatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v35StatsCRCErrors.setStatus("current")
_V35Traps_ObjectIdentity = ObjectIdentity
v35Traps = _V35Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3)
)
_V35TrapVariables_ObjectIdentity = ObjectIdentity
v35TrapVariables = _V35TrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 1)
)
_V35SlotNumber_Type = Integer32
_V35SlotNumber_Object = MibScalar
v35SlotNumber = _V35SlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 1, 1),
    _V35SlotNumber_Type()
)
v35SlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v35SlotNumber.setStatus("current")


class _V35AlarmType_Type(Integer32):
    """Custom type v35AlarmType based on Integer32"""
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
        *(("v35-alarm-CTS", 4),
          ("v35-alarm-DSR", 2),
          ("v35-alarm-DTR", 1),
          ("v35-alarm-RTS", 5),
          ("v35-alarm-ST", 3))
    )


_V35AlarmType_Type.__name__ = "Integer32"
_V35AlarmType_Object = MibScalar
v35AlarmType = _V35AlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 1, 2),
    _V35AlarmType_Type()
)
v35AlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    v35AlarmType.setStatus("current")

# Managed Objects groups


# Notification objects

v35AlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 0, 1)
)
v35AlarmOnTrap.setObjects(
      *(("TIARA-V35-MIB", "v35IfIndex"),
        ("TIARA-V35-MIB", "v35AlarmType"))
)
if mibBuilder.loadTexts:
    v35AlarmOnTrap.setStatus(
        ""
    )

v35AlarmOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 3, 3, 0, 2)
)
v35AlarmOffTrap.setObjects(
      *(("TIARA-V35-MIB", "v35IfIndex"),
        ("TIARA-V35-MIB", "v35AlarmType"))
)
if mibBuilder.loadTexts:
    v35AlarmOffTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-V35-MIB",
    **{"tiaraV35Mib": tiaraV35Mib,
       "v35ConfigTable": v35ConfigTable,
       "v35ConfigTableEntry": v35ConfigTableEntry,
       "v35IfIndex": v35IfIndex,
       "v35ConfigClockRate": v35ConfigClockRate,
       "v35ConfigClockSource": v35ConfigClockSource,
       "v35ConfigMode": v35ConfigMode,
       "v35ConfigCRC": v35ConfigCRC,
       "v35ConfigDataMode": v35ConfigDataMode,
       "v35ConfigFlowControl": v35ConfigFlowControl,
       "v35StatsTable": v35StatsTable,
       "v35StatsTableEntry": v35StatsTableEntry,
       "v35StatsAlarmStatus": v35StatsAlarmStatus,
       "v35StatsFramesIn": v35StatsFramesIn,
       "v35StatsFramesOut": v35StatsFramesOut,
       "v35StatsOctetsIn": v35StatsOctetsIn,
       "v35StatsOctetsOut": v35StatsOctetsOut,
       "v35StatsCRCErrors": v35StatsCRCErrors,
       "v35Traps": v35Traps,
       "v35AlarmOnTrap": v35AlarmOnTrap,
       "v35AlarmOffTrap": v35AlarmOffTrap,
       "v35TrapVariables": v35TrapVariables,
       "v35SlotNumber": v35SlotNumber,
       "v35AlarmType": v35AlarmType}
)
