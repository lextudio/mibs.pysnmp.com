# SNMP MIB module (TIARA-HSSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-HSSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:35 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(tiaraInterfaces,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraInterfaces")


# MODULE-IDENTITY

tiaraHssiMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2)
)
tiaraHssiMib.setRevisions(
        ("1900-08-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HssiConfigTable_Object = MibTable
hssiConfigTable = _HssiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1)
)
if mibBuilder.loadTexts:
    hssiConfigTable.setStatus("current")
_HssiConfigTableEntry_Object = MibTableRow
hssiConfigTableEntry = _HssiConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1)
)
hssiConfigTableEntry.setIndexNames(
    (0, "TIARA-HSSI-MIB", "hssiIfIndex"),
)
if mibBuilder.loadTexts:
    hssiConfigTableEntry.setStatus("current")
_HssiIfIndex_Type = Integer32
_HssiIfIndex_Object = MibTableColumn
hssiIfIndex = _HssiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 1),
    _HssiIfIndex_Type()
)
hssiIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hssiIfIndex.setStatus("current")


class _HssiConfigClockRate_Type(Integer32):
    """Custom type hssiConfigClockRate based on Integer32"""
    defaultValue = 52000000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 52000000),
    )


_HssiConfigClockRate_Type.__name__ = "Integer32"
_HssiConfigClockRate_Object = MibTableColumn
hssiConfigClockRate = _HssiConfigClockRate_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 2),
    _HssiConfigClockRate_Type()
)
hssiConfigClockRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigClockRate.setStatus("current")


class _HssiConfigClockSource_Type(Integer32):
    """Custom type hssiConfigClockSource based on Integer32"""
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


_HssiConfigClockSource_Type.__name__ = "Integer32"
_HssiConfigClockSource_Object = MibTableColumn
hssiConfigClockSource = _HssiConfigClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 3),
    _HssiConfigClockSource_Type()
)
hssiConfigClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigClockSource.setStatus("current")


class _HssiConfigTxClockSource_Type(Integer32):
    """Custom type hssiConfigTxClockSource based on Integer32"""
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
        *(("invertedinternal", 3),
          ("invertedterminal", 4),
          ("normalinternal", 1),
          ("normalterminal", 2))
    )


_HssiConfigTxClockSource_Type.__name__ = "Integer32"
_HssiConfigTxClockSource_Object = MibTableColumn
hssiConfigTxClockSource = _HssiConfigTxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 4),
    _HssiConfigTxClockSource_Type()
)
hssiConfigTxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigTxClockSource.setStatus("current")


class _HssiConfigRxClockSource_Type(Integer32):
    """Custom type hssiConfigRxClockSource based on Integer32"""
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
        *(("invertedinternal", 3),
          ("invertedterminal", 4),
          ("normalinternal", 1),
          ("normalterminal", 2))
    )


_HssiConfigRxClockSource_Type.__name__ = "Integer32"
_HssiConfigRxClockSource_Object = MibTableColumn
hssiConfigRxClockSource = _HssiConfigRxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 5),
    _HssiConfigRxClockSource_Type()
)
hssiConfigRxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigRxClockSource.setStatus("current")


class _HssiConfigMode_Type(Integer32):
    """Custom type hssiConfigMode based on Integer32"""
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


_HssiConfigMode_Type.__name__ = "Integer32"
_HssiConfigMode_Object = MibTableColumn
hssiConfigMode = _HssiConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 6),
    _HssiConfigMode_Type()
)
hssiConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigMode.setStatus("current")


class _HssiConfigDataMode_Type(Integer32):
    """Custom type hssiConfigDataMode based on Integer32"""
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


_HssiConfigDataMode_Type.__name__ = "Integer32"
_HssiConfigDataMode_Object = MibTableColumn
hssiConfigDataMode = _HssiConfigDataMode_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 7),
    _HssiConfigDataMode_Type()
)
hssiConfigDataMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigDataMode.setStatus("current")


class _HssiConfigCRC_Type(Integer32):
    """Custom type hssiConfigCRC based on Integer32"""
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


_HssiConfigCRC_Type.__name__ = "Integer32"
_HssiConfigCRC_Object = MibTableColumn
hssiConfigCRC = _HssiConfigCRC_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 8),
    _HssiConfigCRC_Type()
)
hssiConfigCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigCRC.setStatus("current")


class _HssiConfigProcessCtrlSignal_Type(Integer32):
    """Custom type hssiConfigProcessCtrlSignal based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("process", 2))
    )


_HssiConfigProcessCtrlSignal_Type.__name__ = "Integer32"
_HssiConfigProcessCtrlSignal_Object = MibTableColumn
hssiConfigProcessCtrlSignal = _HssiConfigProcessCtrlSignal_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 9),
    _HssiConfigProcessCtrlSignal_Type()
)
hssiConfigProcessCtrlSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiConfigProcessCtrlSignal.setStatus("current")
_HssiDteLoopback_Type = TruthValue
_HssiDteLoopback_Object = MibTableColumn
hssiDteLoopback = _HssiDteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 10),
    _HssiDteLoopback_Type()
)
hssiDteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiDteLoopback.setStatus("current")


class _HssiDceLoopbackTest_Type(Integer32):
    """Custom type hssiDceLoopbackTest based on Integer32"""
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
        *(("cable", 3),
          ("line", 2),
          ("noTest", 1),
          ("remote", 4))
    )


_HssiDceLoopbackTest_Type.__name__ = "Integer32"
_HssiDceLoopbackTest_Object = MibTableColumn
hssiDceLoopbackTest = _HssiDceLoopbackTest_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 1, 1, 11),
    _HssiDceLoopbackTest_Type()
)
hssiDceLoopbackTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hssiDceLoopbackTest.setStatus("current")
_HssiTraps_ObjectIdentity = ObjectIdentity
hssiTraps = _HssiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2)
)
_HssiTrapVariables_ObjectIdentity = ObjectIdentity
hssiTrapVariables = _HssiTrapVariables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2, 1)
)


class _HssiAlarmType_Type(Integer32):
    """Custom type hssiAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("hssi-alarm-CA", 1),
          ("hssi-alarm-LALB", 6),
          ("hssi-alarm-LC", 4),
          ("hssi-alarm-ST", 2),
          ("hssi-alarm-TA", 5),
          ("hssi-alarm-TM", 3))
    )


_HssiAlarmType_Type.__name__ = "Integer32"
_HssiAlarmType_Object = MibScalar
hssiAlarmType = _HssiAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2, 1, 1),
    _HssiAlarmType_Type()
)
hssiAlarmType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hssiAlarmType.setStatus("current")
_HssiStatsTable_Object = MibTable
hssiStatsTable = _HssiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3)
)
if mibBuilder.loadTexts:
    hssiStatsTable.setStatus("current")
_HssiStatsTableEntry_Object = MibTableRow
hssiStatsTableEntry = _HssiStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1)
)
hssiStatsTableEntry.setIndexNames(
    (0, "TIARA-HSSI-MIB", "hssiIfIndex"),
)
if mibBuilder.loadTexts:
    hssiStatsTableEntry.setStatus("current")


class _HssiStatsAlarmStatus_Type(Bits):
    """Custom type hssiStatsAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("hssi-alarms-CA", 1),
          ("hssi-alarms-LALB", 6),
          ("hssi-alarms-LC", 4),
          ("hssi-alarms-ST", 2),
          ("hssi-alarms-TA", 5),
          ("hssi-alarms-TM", 3),
          ("hssi-no-alarms", 0))
    )

_HssiStatsAlarmStatus_Type.__name__ = "Bits"
_HssiStatsAlarmStatus_Object = MibTableColumn
hssiStatsAlarmStatus = _HssiStatsAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 1),
    _HssiStatsAlarmStatus_Type()
)
hssiStatsAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssiStatsAlarmStatus.setStatus("current")
_HssiStatsFramesIn_Type = Counter32
_HssiStatsFramesIn_Object = MibTableColumn
hssiStatsFramesIn = _HssiStatsFramesIn_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 2),
    _HssiStatsFramesIn_Type()
)
hssiStatsFramesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssiStatsFramesIn.setStatus("current")
_HssiStatsFramesOut_Type = Counter32
_HssiStatsFramesOut_Object = MibTableColumn
hssiStatsFramesOut = _HssiStatsFramesOut_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 3),
    _HssiStatsFramesOut_Type()
)
hssiStatsFramesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssiStatsFramesOut.setStatus("current")
_HssiStatsOctetsIn_Type = Counter32
_HssiStatsOctetsIn_Object = MibTableColumn
hssiStatsOctetsIn = _HssiStatsOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 4),
    _HssiStatsOctetsIn_Type()
)
hssiStatsOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssiStatsOctetsIn.setStatus("current")
_HssiStatsOctetsOut_Type = Counter32
_HssiStatsOctetsOut_Object = MibTableColumn
hssiStatsOctetsOut = _HssiStatsOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 5),
    _HssiStatsOctetsOut_Type()
)
hssiStatsOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssiStatsOctetsOut.setStatus("current")
_HssiStatsCRCErrors_Type = Counter32
_HssiStatsCRCErrors_Object = MibTableColumn
hssiStatsCRCErrors = _HssiStatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 3, 1, 6),
    _HssiStatsCRCErrors_Type()
)
hssiStatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hssiStatsCRCErrors.setStatus("current")

# Managed Objects groups


# Notification objects

hssiAlarmOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2, 0, 1)
)
hssiAlarmOnTrap.setObjects(
      *(("TIARA-HSSI-MIB", "hssiIfIndex"),
        ("TIARA-HSSI-MIB", "hssiAlarmType"))
)
if mibBuilder.loadTexts:
    hssiAlarmOnTrap.setStatus(
        ""
    )

hssiAlarmOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3174, 2, 7, 2, 2, 0, 2)
)
hssiAlarmOffTrap.setObjects(
      *(("TIARA-HSSI-MIB", "hssiIfIndex"),
        ("TIARA-HSSI-MIB", "hssiAlarmType"))
)
if mibBuilder.loadTexts:
    hssiAlarmOffTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-HSSI-MIB",
    **{"tiaraHssiMib": tiaraHssiMib,
       "hssiConfigTable": hssiConfigTable,
       "hssiConfigTableEntry": hssiConfigTableEntry,
       "hssiIfIndex": hssiIfIndex,
       "hssiConfigClockRate": hssiConfigClockRate,
       "hssiConfigClockSource": hssiConfigClockSource,
       "hssiConfigTxClockSource": hssiConfigTxClockSource,
       "hssiConfigRxClockSource": hssiConfigRxClockSource,
       "hssiConfigMode": hssiConfigMode,
       "hssiConfigDataMode": hssiConfigDataMode,
       "hssiConfigCRC": hssiConfigCRC,
       "hssiConfigProcessCtrlSignal": hssiConfigProcessCtrlSignal,
       "hssiDteLoopback": hssiDteLoopback,
       "hssiDceLoopbackTest": hssiDceLoopbackTest,
       "hssiTraps": hssiTraps,
       "hssiAlarmOnTrap": hssiAlarmOnTrap,
       "hssiAlarmOffTrap": hssiAlarmOffTrap,
       "hssiTrapVariables": hssiTrapVariables,
       "hssiAlarmType": hssiAlarmType,
       "hssiStatsTable": hssiStatsTable,
       "hssiStatsTableEntry": hssiStatsTableEntry,
       "hssiStatsAlarmStatus": hssiStatsAlarmStatus,
       "hssiStatsFramesIn": hssiStatsFramesIn,
       "hssiStatsFramesOut": hssiStatsFramesOut,
       "hssiStatsOctetsIn": hssiStatsOctetsIn,
       "hssiStatsOctetsOut": hssiStatsOctetsOut,
       "hssiStatsCRCErrors": hssiStatsCRCErrors}
)
