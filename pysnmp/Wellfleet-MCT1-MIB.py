# SNMP MIB module (Wellfleet-MCT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-MCT1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:38 2024
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

(wfMcT1Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfMcT1Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfMcT1ModTable_Object = MibTable
wfMcT1ModTable = _WfMcT1ModTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1)
)
if mibBuilder.loadTexts:
    wfMcT1ModTable.setStatus("mandatory")
_WfMcT1ModEntry_Object = MibTableRow
wfMcT1ModEntry = _WfMcT1ModEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1)
)
wfMcT1ModEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1ModSlot"),
)
if mibBuilder.loadTexts:
    wfMcT1ModEntry.setStatus("mandatory")


class _WfMcT1ModDelete_Type(Integer32):
    """Custom type wfMcT1ModDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfMcT1ModDelete_Type.__name__ = "Integer32"
_WfMcT1ModDelete_Object = MibTableColumn
wfMcT1ModDelete = _WfMcT1ModDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 1),
    _WfMcT1ModDelete_Type()
)
wfMcT1ModDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1ModDelete.setStatus("mandatory")


class _WfMcT1ModDisable_Type(Integer32):
    """Custom type wfMcT1ModDisable based on Integer32"""
    defaultValue = 1

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


_WfMcT1ModDisable_Type.__name__ = "Integer32"
_WfMcT1ModDisable_Object = MibTableColumn
wfMcT1ModDisable = _WfMcT1ModDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 2),
    _WfMcT1ModDisable_Type()
)
wfMcT1ModDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1ModDisable.setStatus("mandatory")


class _WfMcT1ModSlot_Type(Integer32):
    """Custom type wfMcT1ModSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1ModSlot_Type.__name__ = "Integer32"
_WfMcT1ModSlot_Object = MibTableColumn
wfMcT1ModSlot = _WfMcT1ModSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 3),
    _WfMcT1ModSlot_Type()
)
wfMcT1ModSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1ModSlot.setStatus("mandatory")


class _WfMcT1ModPrimaryClock_Type(Integer32):
    """Custom type wfMcT1ModPrimaryClock based on Integer32"""
    defaultValue = 4

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
        *(("external", 1),
          ("int", 4),
          ("loop0", 2),
          ("loop1", 3))
    )


_WfMcT1ModPrimaryClock_Type.__name__ = "Integer32"
_WfMcT1ModPrimaryClock_Object = MibTableColumn
wfMcT1ModPrimaryClock = _WfMcT1ModPrimaryClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 4),
    _WfMcT1ModPrimaryClock_Type()
)
wfMcT1ModPrimaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1ModPrimaryClock.setStatus("mandatory")


class _WfMcT1ModSecondaryClock_Type(Integer32):
    """Custom type wfMcT1ModSecondaryClock based on Integer32"""
    defaultValue = 2

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
        *(("external", 1),
          ("int", 4),
          ("loop0", 2),
          ("loop1", 3))
    )


_WfMcT1ModSecondaryClock_Type.__name__ = "Integer32"
_WfMcT1ModSecondaryClock_Object = MibTableColumn
wfMcT1ModSecondaryClock = _WfMcT1ModSecondaryClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 5),
    _WfMcT1ModSecondaryClock_Type()
)
wfMcT1ModSecondaryClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1ModSecondaryClock.setStatus("mandatory")


class _WfMcT1ModCurrentClock_Type(Integer32):
    """Custom type wfMcT1ModCurrentClock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("int", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_WfMcT1ModCurrentClock_Type.__name__ = "Integer32"
_WfMcT1ModCurrentClock_Object = MibTableColumn
wfMcT1ModCurrentClock = _WfMcT1ModCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 6),
    _WfMcT1ModCurrentClock_Type()
)
wfMcT1ModCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1ModCurrentClock.setStatus("mandatory")


class _WfMcT1ModExtClockOperational_Type(Integer32):
    """Custom type wfMcT1ModExtClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oper", 1),
          ("unoper", 2))
    )


_WfMcT1ModExtClockOperational_Type.__name__ = "Integer32"
_WfMcT1ModExtClockOperational_Object = MibTableColumn
wfMcT1ModExtClockOperational = _WfMcT1ModExtClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 7),
    _WfMcT1ModExtClockOperational_Type()
)
wfMcT1ModExtClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1ModExtClockOperational.setStatus("mandatory")


class _WfMcT1ModLoop0ClockOperational_Type(Integer32):
    """Custom type wfMcT1ModLoop0ClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oper", 1),
          ("unoper", 2))
    )


_WfMcT1ModLoop0ClockOperational_Type.__name__ = "Integer32"
_WfMcT1ModLoop0ClockOperational_Object = MibTableColumn
wfMcT1ModLoop0ClockOperational = _WfMcT1ModLoop0ClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 8),
    _WfMcT1ModLoop0ClockOperational_Type()
)
wfMcT1ModLoop0ClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1ModLoop0ClockOperational.setStatus("mandatory")


class _WfMcT1ModLoop1ClockOperational_Type(Integer32):
    """Custom type wfMcT1ModLoop1ClockOperational based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oper", 1),
          ("unoper", 2))
    )


_WfMcT1ModLoop1ClockOperational_Type.__name__ = "Integer32"
_WfMcT1ModLoop1ClockOperational_Object = MibTableColumn
wfMcT1ModLoop1ClockOperational = _WfMcT1ModLoop1ClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 9),
    _WfMcT1ModLoop1ClockOperational_Type()
)
wfMcT1ModLoop1ClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1ModLoop1ClockOperational.setStatus("mandatory")
_WfMcT1ModRestart_Type = Integer32
_WfMcT1ModRestart_Object = MibTableColumn
wfMcT1ModRestart = _WfMcT1ModRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 1, 1, 10),
    _WfMcT1ModRestart_Type()
)
wfMcT1ModRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1ModRestart.setStatus("mandatory")
_WfMcT1Table_Object = MibTable
wfMcT1Table = _WfMcT1Table_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2)
)
if mibBuilder.loadTexts:
    wfMcT1Table.setStatus("mandatory")
_WfMcT1Entry_Object = MibTableRow
wfMcT1Entry = _WfMcT1Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1)
)
wfMcT1Entry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Slot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Connector"),
)
if mibBuilder.loadTexts:
    wfMcT1Entry.setStatus("mandatory")


class _WfMcT1Delete_Type(Integer32):
    """Custom type wfMcT1Delete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfMcT1Delete_Type.__name__ = "Integer32"
_WfMcT1Delete_Object = MibTableColumn
wfMcT1Delete = _WfMcT1Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 1),
    _WfMcT1Delete_Type()
)
wfMcT1Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Delete.setStatus("mandatory")


class _WfMcT1Disable_Type(Integer32):
    """Custom type wfMcT1Disable based on Integer32"""
    defaultValue = 1

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


_WfMcT1Disable_Type.__name__ = "Integer32"
_WfMcT1Disable_Object = MibTableColumn
wfMcT1Disable = _WfMcT1Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 2),
    _WfMcT1Disable_Type()
)
wfMcT1Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Disable.setStatus("mandatory")


class _WfMcT1State_Type(Integer32):
    """Custom type wfMcT1State based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("bert", 3),
          ("bluealarm", 7),
          ("init", 1),
          ("loopback", 4),
          ("notpresent", 8),
          ("redalarm", 5),
          ("up", 2),
          ("yelalarm", 6))
    )


_WfMcT1State_Type.__name__ = "Integer32"
_WfMcT1State_Object = MibTableColumn
wfMcT1State = _WfMcT1State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 3),
    _WfMcT1State_Type()
)
wfMcT1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1State.setStatus("mandatory")


class _WfMcT1Slot_Type(Integer32):
    """Custom type wfMcT1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1Slot_Type.__name__ = "Integer32"
_WfMcT1Slot_Object = MibTableColumn
wfMcT1Slot = _WfMcT1Slot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 4),
    _WfMcT1Slot_Type()
)
wfMcT1Slot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Slot.setStatus("mandatory")


class _WfMcT1Connector_Type(Integer32):
    """Custom type wfMcT1Connector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1Connector_Type.__name__ = "Integer32"
_WfMcT1Connector_Object = MibTableColumn
wfMcT1Connector = _WfMcT1Connector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 5),
    _WfMcT1Connector_Type()
)
wfMcT1Connector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Connector.setStatus("mandatory")


class _WfMcT1OperationMode_Type(Integer32):
    """Custom type wfMcT1OperationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bert", 2),
          ("default", 1))
    )


_WfMcT1OperationMode_Type.__name__ = "Integer32"
_WfMcT1OperationMode_Object = MibTableColumn
wfMcT1OperationMode = _WfMcT1OperationMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 6),
    _WfMcT1OperationMode_Type()
)
wfMcT1OperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1OperationMode.setStatus("mandatory")


class _WfMcT1Mtu_Type(Integer32):
    """Custom type wfMcT1Mtu based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4608),
    )


_WfMcT1Mtu_Type.__name__ = "Integer32"
_WfMcT1Mtu_Object = MibTableColumn
wfMcT1Mtu = _WfMcT1Mtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 7),
    _WfMcT1Mtu_Type()
)
wfMcT1Mtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Mtu.setStatus("mandatory")


class _WfMcT1MunichVersion_Type(Integer32):
    """Custom type wfMcT1MunichVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_WfMcT1MunichVersion_Type.__name__ = "Integer32"
_WfMcT1MunichVersion_Object = MibTableColumn
wfMcT1MunichVersion = _WfMcT1MunichVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 8),
    _WfMcT1MunichVersion_Type()
)
wfMcT1MunichVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1MunichVersion.setStatus("mandatory")


class _WfMcT1Dsx1LineType_Type(Integer32):
    """Custom type wfMcT1Dsx1LineType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("esf", 2))
    )


_WfMcT1Dsx1LineType_Type.__name__ = "Integer32"
_WfMcT1Dsx1LineType_Object = MibTableColumn
wfMcT1Dsx1LineType = _WfMcT1Dsx1LineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 9),
    _WfMcT1Dsx1LineType_Type()
)
wfMcT1Dsx1LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1LineType.setStatus("mandatory")


class _WfMcT1Dsx1ZeroCoding_Type(Integer32):
    """Custom type wfMcT1Dsx1ZeroCoding based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ami", 5),
          ("b8zs", 2))
    )


_WfMcT1Dsx1ZeroCoding_Type.__name__ = "Integer32"
_WfMcT1Dsx1ZeroCoding_Object = MibTableColumn
wfMcT1Dsx1ZeroCoding = _WfMcT1Dsx1ZeroCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 10),
    _WfMcT1Dsx1ZeroCoding_Type()
)
wfMcT1Dsx1ZeroCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1ZeroCoding.setStatus("mandatory")


class _WfMcT1Dsx1LoopbackConfig_Type(Integer32):
    """Custom type wfMcT1Dsx1LoopbackConfig based on Integer32"""
    defaultValue = 1

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
        *(("mgrlineloop", 3),
          ("mgrpayloadloop", 2),
          ("netreqlineloop", 5),
          ("netreqpayloadloop", 4),
          ("noloop", 1),
          ("otherloop", 6))
    )


_WfMcT1Dsx1LoopbackConfig_Type.__name__ = "Integer32"
_WfMcT1Dsx1LoopbackConfig_Object = MibTableColumn
wfMcT1Dsx1LoopbackConfig = _WfMcT1Dsx1LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 11),
    _WfMcT1Dsx1LoopbackConfig_Type()
)
wfMcT1Dsx1LoopbackConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1LoopbackConfig.setStatus("mandatory")


class _WfMcT1Dsx1LineStatus_Type(Integer32):
    """Custom type wfMcT1Dsx1LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("alarmindicationsignal", 4),
          ("farendalarm", 2),
          ("loopbackstate", 32),
          ("lossofframe", 8),
          ("lossofsignal", 16),
          ("noalarm", 1))
    )


_WfMcT1Dsx1LineStatus_Type.__name__ = "Integer32"
_WfMcT1Dsx1LineStatus_Object = MibTableColumn
wfMcT1Dsx1LineStatus = _WfMcT1Dsx1LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 12),
    _WfMcT1Dsx1LineStatus_Type()
)
wfMcT1Dsx1LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1LineStatus.setStatus("mandatory")


class _WfMcT1Dsx1SetupAlarmThreshold_Type(Integer32):
    """Custom type wfMcT1Dsx1SetupAlarmThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("threshold10", 10),
          ("threshold2", 2),
          ("threshold4", 4),
          ("threshold6", 6),
          ("threshold8", 8))
    )


_WfMcT1Dsx1SetupAlarmThreshold_Type.__name__ = "Integer32"
_WfMcT1Dsx1SetupAlarmThreshold_Object = MibTableColumn
wfMcT1Dsx1SetupAlarmThreshold = _WfMcT1Dsx1SetupAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 13),
    _WfMcT1Dsx1SetupAlarmThreshold_Type()
)
wfMcT1Dsx1SetupAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1SetupAlarmThreshold.setStatus("mandatory")


class _WfMcT1Dsx1ClearAlarmThreshold_Type(Integer32):
    """Custom type wfMcT1Dsx1ClearAlarmThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("threshold10", 10),
          ("threshold2", 2),
          ("threshold4", 4),
          ("threshold6", 6),
          ("threshold8", 8))
    )


_WfMcT1Dsx1ClearAlarmThreshold_Type.__name__ = "Integer32"
_WfMcT1Dsx1ClearAlarmThreshold_Object = MibTableColumn
wfMcT1Dsx1ClearAlarmThreshold = _WfMcT1Dsx1ClearAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 14),
    _WfMcT1Dsx1ClearAlarmThreshold_Type()
)
wfMcT1Dsx1ClearAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1ClearAlarmThreshold.setStatus("mandatory")


class _WfMcT1Dsx1SignalLevel_Type(Integer32):
    """Custom type wfMcT1Dsx1SignalLevel based on Integer32"""
    defaultValue = 3

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
        *(("minus0", 3),
          ("minus15", 1),
          ("minus7point5", 2),
          ("plus1point1", 6),
          ("plus1point5", 7),
          ("pluspoint5", 4),
          ("pluspoint8", 5))
    )


_WfMcT1Dsx1SignalLevel_Type.__name__ = "Integer32"
_WfMcT1Dsx1SignalLevel_Object = MibTableColumn
wfMcT1Dsx1SignalLevel = _WfMcT1Dsx1SignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 15),
    _WfMcT1Dsx1SignalLevel_Type()
)
wfMcT1Dsx1SignalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1SignalLevel.setStatus("mandatory")


class _WfMcT1LoopbackDisable_Type(Integer32):
    """Custom type wfMcT1LoopbackDisable based on Integer32"""
    defaultValue = 1

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


_WfMcT1LoopbackDisable_Type.__name__ = "Integer32"
_WfMcT1LoopbackDisable_Object = MibTableColumn
wfMcT1LoopbackDisable = _WfMcT1LoopbackDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 16),
    _WfMcT1LoopbackDisable_Type()
)
wfMcT1LoopbackDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LoopbackDisable.setStatus("mandatory")


class _WfMcT1Dsx1FDLOperationMode_Type(Integer32):
    """Custom type wfMcT1Dsx1FDLOperationMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oper54016", 1),
          ("opert1403", 2))
    )


_WfMcT1Dsx1FDLOperationMode_Type.__name__ = "Integer32"
_WfMcT1Dsx1FDLOperationMode_Object = MibTableColumn
wfMcT1Dsx1FDLOperationMode = _WfMcT1Dsx1FDLOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 17),
    _WfMcT1Dsx1FDLOperationMode_Type()
)
wfMcT1Dsx1FDLOperationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1FDLOperationMode.setStatus("mandatory")


class _WfMcT1BertTxOutputLevel_Type(Integer32):
    """Custom type wfMcT1BertTxOutputLevel based on Integer32"""
    defaultValue = 3

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
        *(("minus0", 3),
          ("minus15", 1),
          ("minus7point5", 2),
          ("plus1point1", 6),
          ("plus1point5", 7),
          ("pluspoint5", 4),
          ("pluspoint8", 5))
    )


_WfMcT1BertTxOutputLevel_Type.__name__ = "Integer32"
_WfMcT1BertTxOutputLevel_Object = MibTableColumn
wfMcT1BertTxOutputLevel = _WfMcT1BertTxOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 18),
    _WfMcT1BertTxOutputLevel_Type()
)
wfMcT1BertTxOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertTxOutputLevel.setStatus("mandatory")


class _WfMcT1BertTestMode_Type(Integer32):
    """Custom type wfMcT1BertTestMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("esf", 3),
          ("sf", 2),
          ("t1", 1))
    )


_WfMcT1BertTestMode_Type.__name__ = "Integer32"
_WfMcT1BertTestMode_Object = MibTableColumn
wfMcT1BertTestMode = _WfMcT1BertTestMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 19),
    _WfMcT1BertTestMode_Type()
)
wfMcT1BertTestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertTestMode.setStatus("mandatory")


class _WfMcT1BertLineCode_Type(Integer32):
    """Custom type wfMcT1BertLineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2))
    )


_WfMcT1BertLineCode_Type.__name__ = "Integer32"
_WfMcT1BertLineCode_Object = MibTableColumn
wfMcT1BertLineCode = _WfMcT1BertLineCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 20),
    _WfMcT1BertLineCode_Type()
)
wfMcT1BertLineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertLineCode.setStatus("mandatory")


class _WfMcT1BertTestPattern_Type(Integer32):
    """Custom type wfMcT1BertTestPattern based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 4),
          ("fifteeninv", 5),
          ("ones", 2),
          ("qrss", 3),
          ("twenty", 6),
          ("twentythree", 7),
          ("twentythreeinv", 8),
          ("zeros", 1))
    )


_WfMcT1BertTestPattern_Type.__name__ = "Integer32"
_WfMcT1BertTestPattern_Object = MibTableColumn
wfMcT1BertTestPattern = _WfMcT1BertTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 21),
    _WfMcT1BertTestPattern_Type()
)
wfMcT1BertTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertTestPattern.setStatus("mandatory")


class _WfMcT1BertSendAlarm_Type(Integer32):
    """Custom type wfMcT1BertSendAlarm based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blue", 1),
          ("disabled", 3),
          ("yellow", 2))
    )


_WfMcT1BertSendAlarm_Type.__name__ = "Integer32"
_WfMcT1BertSendAlarm_Object = MibTableColumn
wfMcT1BertSendAlarm = _WfMcT1BertSendAlarm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 22),
    _WfMcT1BertSendAlarm_Type()
)
wfMcT1BertSendAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertSendAlarm.setStatus("mandatory")
_WfMcT1DS2282Version_Type = Integer32
_WfMcT1DS2282Version_Object = MibTableColumn
wfMcT1DS2282Version = _WfMcT1DS2282Version_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 23),
    _WfMcT1DS2282Version_Type()
)
wfMcT1DS2282Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1DS2282Version.setStatus("mandatory")
_WfMcT1Restart_Type = Integer32
_WfMcT1Restart_Object = MibTableColumn
wfMcT1Restart = _WfMcT1Restart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 24),
    _WfMcT1Restart_Type()
)
wfMcT1Restart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Restart.setStatus("mandatory")


class _WfMcT1Loopback_Type(Integer32):
    """Custom type wfMcT1Loopback based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deactivate", 3),
          ("linelb", 1),
          ("payldlb", 2))
    )


_WfMcT1Loopback_Type.__name__ = "Integer32"
_WfMcT1Loopback_Object = MibTableColumn
wfMcT1Loopback = _WfMcT1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 25),
    _WfMcT1Loopback_Type()
)
wfMcT1Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Loopback.setStatus("mandatory")


class _WfMcT1FDLTargetAddress_Type(Integer32):
    """Custom type wfMcT1FDLTargetAddress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("az", 1),
          ("by", 2))
    )


_WfMcT1FDLTargetAddress_Type.__name__ = "Integer32"
_WfMcT1FDLTargetAddress_Object = MibTableColumn
wfMcT1FDLTargetAddress = _WfMcT1FDLTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 2, 1, 26),
    _WfMcT1FDLTargetAddress_Type()
)
wfMcT1FDLTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1FDLTargetAddress.setStatus("mandatory")
_WfMcT1ConfigTable_Object = MibTable
wfMcT1ConfigTable = _WfMcT1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3)
)
if mibBuilder.loadTexts:
    wfMcT1ConfigTable.setStatus("mandatory")
_WfMcT1ConfigEntry_Object = MibTableRow
wfMcT1ConfigEntry = _WfMcT1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1)
)
wfMcT1ConfigEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1ConfigSlot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1ConfigConnector"),
)
if mibBuilder.loadTexts:
    wfMcT1ConfigEntry.setStatus("mandatory")


class _WfMcT1ConfigSlot_Type(Integer32):
    """Custom type wfMcT1ConfigSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1ConfigSlot_Type.__name__ = "Integer32"
_WfMcT1ConfigSlot_Object = MibTableColumn
wfMcT1ConfigSlot = _WfMcT1ConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 1),
    _WfMcT1ConfigSlot_Type()
)
wfMcT1ConfigSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1ConfigSlot.setStatus("mandatory")


class _WfMcT1ConfigConnector_Type(Integer32):
    """Custom type wfMcT1ConfigConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1ConfigConnector_Type.__name__ = "Integer32"
_WfMcT1ConfigConnector_Object = MibTableColumn
wfMcT1ConfigConnector = _WfMcT1ConfigConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 2),
    _WfMcT1ConfigConnector_Type()
)
wfMcT1ConfigConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1ConfigConnector.setStatus("mandatory")


class _WfMcT1BertRestart_Type(Integer32):
    """Custom type wfMcT1BertRestart based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 10),
          ("restart", 1))
    )


_WfMcT1BertRestart_Type.__name__ = "Integer32"
_WfMcT1BertRestart_Object = MibTableColumn
wfMcT1BertRestart = _WfMcT1BertRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 3),
    _WfMcT1BertRestart_Type()
)
wfMcT1BertRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertRestart.setStatus("mandatory")


class _WfMcT1BertPayldLb_Type(Integer32):
    """Custom type wfMcT1BertPayldLb based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("act", 1),
          ("deact", 2),
          ("noaction", 10))
    )


_WfMcT1BertPayldLb_Type.__name__ = "Integer32"
_WfMcT1BertPayldLb_Object = MibTableColumn
wfMcT1BertPayldLb = _WfMcT1BertPayldLb_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 4),
    _WfMcT1BertPayldLb_Type()
)
wfMcT1BertPayldLb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertPayldLb.setStatus("mandatory")


class _WfMcT1BertLineLb_Type(Integer32):
    """Custom type wfMcT1BertLineLb based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("fdlact", 3),
          ("fdldeact", 4),
          ("lpdn", 2),
          ("lpup", 1),
          ("noaction", 10))
    )


_WfMcT1BertLineLb_Type.__name__ = "Integer32"
_WfMcT1BertLineLb_Object = MibTableColumn
wfMcT1BertLineLb = _WfMcT1BertLineLb_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 5),
    _WfMcT1BertLineLb_Type()
)
wfMcT1BertLineLb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertLineLb.setStatus("mandatory")


class _WfMcT1BertErrorInsert_Type(Integer32):
    """Custom type wfMcT1BertErrorInsert based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("disable", 4),
          ("millionconfig", 3),
          ("noaction", 10),
          ("thousandconfig", 2))
    )


_WfMcT1BertErrorInsert_Type.__name__ = "Integer32"
_WfMcT1BertErrorInsert_Object = MibTableColumn
wfMcT1BertErrorInsert = _WfMcT1BertErrorInsert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 6),
    _WfMcT1BertErrorInsert_Type()
)
wfMcT1BertErrorInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1BertErrorInsert.setStatus("mandatory")


class _WfMcT1Dsx1SendLoopCode_Type(Integer32):
    """Custom type wfMcT1Dsx1SendLoopCode based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("loopdn", 2),
          ("loopup", 1),
          ("noaction", 10))
    )


_WfMcT1Dsx1SendLoopCode_Type.__name__ = "Integer32"
_WfMcT1Dsx1SendLoopCode_Object = MibTableColumn
wfMcT1Dsx1SendLoopCode = _WfMcT1Dsx1SendLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 7),
    _WfMcT1Dsx1SendLoopCode_Type()
)
wfMcT1Dsx1SendLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1SendLoopCode.setStatus("mandatory")


class _WfMcT1Dsx1SendFDLCode_Type(Integer32):
    """Custom type wfMcT1Dsx1SendFDLCode based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("ci", 1),
          ("ia", 3),
          ("ib", 7),
          ("linelbdeact", 4),
          ("noaction", 10),
          ("pyldlbact", 5),
          ("pyldlbdeact", 6),
          ("univlbdeact", 2))
    )


_WfMcT1Dsx1SendFDLCode_Type.__name__ = "Integer32"
_WfMcT1Dsx1SendFDLCode_Object = MibTableColumn
wfMcT1Dsx1SendFDLCode = _WfMcT1Dsx1SendFDLCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 3, 1, 8),
    _WfMcT1Dsx1SendFDLCode_Type()
)
wfMcT1Dsx1SendFDLCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1Dsx1SendFDLCode.setStatus("mandatory")
_WfMcT1LineTable_Object = MibTable
wfMcT1LineTable = _WfMcT1LineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4)
)
if mibBuilder.loadTexts:
    wfMcT1LineTable.setStatus("mandatory")
_WfMcT1LineEntry_Object = MibTableRow
wfMcT1LineEntry = _WfMcT1LineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1)
)
wfMcT1LineEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1LineSlot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1LineConnector"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1LineLine"),
)
if mibBuilder.loadTexts:
    wfMcT1LineEntry.setStatus("mandatory")


class _WfMcT1LineDelete_Type(Integer32):
    """Custom type wfMcT1LineDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfMcT1LineDelete_Type.__name__ = "Integer32"
_WfMcT1LineDelete_Object = MibTableColumn
wfMcT1LineDelete = _WfMcT1LineDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 1),
    _WfMcT1LineDelete_Type()
)
wfMcT1LineDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineDelete.setStatus("mandatory")


class _WfMcT1LineDisable_Type(Integer32):
    """Custom type wfMcT1LineDisable based on Integer32"""
    defaultValue = 1

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


_WfMcT1LineDisable_Type.__name__ = "Integer32"
_WfMcT1LineDisable_Object = MibTableColumn
wfMcT1LineDisable = _WfMcT1LineDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 2),
    _WfMcT1LineDisable_Type()
)
wfMcT1LineDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineDisable.setStatus("mandatory")


class _WfMcT1LineState_Type(Integer32):
    """Custom type wfMcT1LineState based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("channel", 6),
          ("down", 2),
          ("init", 3),
          ("loopback", 4),
          ("notpresent", 8),
          ("stop", 7),
          ("up", 1),
          ("wait", 5))
    )


_WfMcT1LineState_Type.__name__ = "Integer32"
_WfMcT1LineState_Object = MibTableColumn
wfMcT1LineState = _WfMcT1LineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 3),
    _WfMcT1LineState_Type()
)
wfMcT1LineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineState.setStatus("mandatory")


class _WfMcT1LineSlot_Type(Integer32):
    """Custom type wfMcT1LineSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1LineSlot_Type.__name__ = "Integer32"
_WfMcT1LineSlot_Object = MibTableColumn
wfMcT1LineSlot = _WfMcT1LineSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 4),
    _WfMcT1LineSlot_Type()
)
wfMcT1LineSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineSlot.setStatus("mandatory")


class _WfMcT1LineConnector_Type(Integer32):
    """Custom type wfMcT1LineConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1LineConnector_Type.__name__ = "Integer32"
_WfMcT1LineConnector_Object = MibTableColumn
wfMcT1LineConnector = _WfMcT1LineConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 5),
    _WfMcT1LineConnector_Type()
)
wfMcT1LineConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineConnector.setStatus("mandatory")


class _WfMcT1LineLine_Type(Integer32):
    """Custom type wfMcT1LineLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_WfMcT1LineLine_Type.__name__ = "Integer32"
_WfMcT1LineLine_Object = MibTableColumn
wfMcT1LineLine = _WfMcT1LineLine_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 6),
    _WfMcT1LineLine_Type()
)
wfMcT1LineLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineLine.setStatus("mandatory")


class _WfMcT1LineCct_Type(Integer32):
    """Custom type wfMcT1LineCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMcT1LineCct_Type.__name__ = "Integer32"
_WfMcT1LineCct_Object = MibTableColumn
wfMcT1LineCct = _WfMcT1LineCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 7),
    _WfMcT1LineCct_Type()
)
wfMcT1LineCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineCct.setStatus("mandatory")


class _WfMcT1LineBofl_Type(Integer32):
    """Custom type wfMcT1LineBofl based on Integer32"""
    defaultValue = 1

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


_WfMcT1LineBofl_Type.__name__ = "Integer32"
_WfMcT1LineBofl_Object = MibTableColumn
wfMcT1LineBofl = _WfMcT1LineBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 8),
    _WfMcT1LineBofl_Type()
)
wfMcT1LineBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineBofl.setStatus("mandatory")


class _WfMcT1LineBoflTmo_Type(Integer32):
    """Custom type wfMcT1LineBoflTmo based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfMcT1LineBoflTmo_Type.__name__ = "Integer32"
_WfMcT1LineBoflTmo_Object = MibTableColumn
wfMcT1LineBoflTmo = _WfMcT1LineBoflTmo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 9),
    _WfMcT1LineBoflTmo_Type()
)
wfMcT1LineBoflTmo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineBoflTmo.setStatus("mandatory")


class _WfMcT1LineFractionalLpbk_Type(Integer32):
    """Custom type wfMcT1LineFractionalLpbk based on Integer32"""
    defaultValue = 2

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


_WfMcT1LineFractionalLpbk_Type.__name__ = "Integer32"
_WfMcT1LineFractionalLpbk_Object = MibTableColumn
wfMcT1LineFractionalLpbk = _WfMcT1LineFractionalLpbk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 10),
    _WfMcT1LineFractionalLpbk_Type()
)
wfMcT1LineFractionalLpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineFractionalLpbk.setStatus("mandatory")
_WfMcT1LineChannelAssignment_Type = DisplayString
_WfMcT1LineChannelAssignment_Object = MibTableColumn
wfMcT1LineChannelAssignment = _WfMcT1LineChannelAssignment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 11),
    _WfMcT1LineChannelAssignment_Type()
)
wfMcT1LineChannelAssignment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineChannelAssignment.setStatus("mandatory")
_WfMcT1LineMadr_Type = OctetString
_WfMcT1LineMadr_Object = MibTableColumn
wfMcT1LineMadr = _WfMcT1LineMadr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 12),
    _WfMcT1LineMadr_Type()
)
wfMcT1LineMadr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineMadr.setStatus("mandatory")


class _WfMcT1LineWanProtocol_Type(Integer32):
    """Custom type wfMcT1LineWanProtocol based on Integer32"""
    defaultValue = 1

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
        *(("framerelay", 4),
          ("ppp", 2),
          ("smds", 3),
          ("standard", 1),
          ("sw", 6),
          ("switch", 5))
    )


_WfMcT1LineWanProtocol_Type.__name__ = "Integer32"
_WfMcT1LineWanProtocol_Object = MibTableColumn
wfMcT1LineWanProtocol = _WfMcT1LineWanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 13),
    _WfMcT1LineWanProtocol_Type()
)
wfMcT1LineWanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineWanProtocol.setStatus("mandatory")


class _WfMcT1LineService_Type(Integer32):
    """Custom type wfMcT1LineService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 1),
          ("llc1", 2))
    )


_WfMcT1LineService_Type.__name__ = "Integer32"
_WfMcT1LineService_Object = MibTableColumn
wfMcT1LineService = _WfMcT1LineService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 14),
    _WfMcT1LineService_Type()
)
wfMcT1LineService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineService.setStatus("mandatory")


class _WfMcT1LineRateAdaption_Type(Integer32):
    """Custom type wfMcT1LineRateAdaption based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adaption64k", 1),
          ("lsb", 3),
          ("msb", 2))
    )


_WfMcT1LineRateAdaption_Type.__name__ = "Integer32"
_WfMcT1LineRateAdaption_Object = MibTableColumn
wfMcT1LineRateAdaption = _WfMcT1LineRateAdaption_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 15),
    _WfMcT1LineRateAdaption_Type()
)
wfMcT1LineRateAdaption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineRateAdaption.setStatus("mandatory")


class _WfMcT1LineIFTF_Type(Integer32):
    """Custom type wfMcT1LineIFTF based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flags", 1),
          ("idles", 2))
    )


_WfMcT1LineIFTF_Type.__name__ = "Integer32"
_WfMcT1LineIFTF_Object = MibTableColumn
wfMcT1LineIFTF = _WfMcT1LineIFTF_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 16),
    _WfMcT1LineIFTF_Type()
)
wfMcT1LineIFTF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineIFTF.setStatus("mandatory")


class _WfMcT1LineCRCSize_Type(Integer32):
    """Custom type wfMcT1LineCRCSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16", 2),
          ("crc32", 1))
    )


_WfMcT1LineCRCSize_Type.__name__ = "Integer32"
_WfMcT1LineCRCSize_Object = MibTableColumn
wfMcT1LineCRCSize = _WfMcT1LineCRCSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 17),
    _WfMcT1LineCRCSize_Type()
)
wfMcT1LineCRCSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineCRCSize.setStatus("mandatory")
_WfMcT1LineRxOctets_Type = Counter32
_WfMcT1LineRxOctets_Object = MibTableColumn
wfMcT1LineRxOctets = _WfMcT1LineRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 18),
    _WfMcT1LineRxOctets_Type()
)
wfMcT1LineRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxOctets.setStatus("mandatory")
_WfMcT1LineRxFrames_Type = Counter32
_WfMcT1LineRxFrames_Object = MibTableColumn
wfMcT1LineRxFrames = _WfMcT1LineRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 19),
    _WfMcT1LineRxFrames_Type()
)
wfMcT1LineRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxFrames.setStatus("mandatory")
_WfMcT1LineTxOctets_Type = Counter32
_WfMcT1LineTxOctets_Object = MibTableColumn
wfMcT1LineTxOctets = _WfMcT1LineTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 20),
    _WfMcT1LineTxOctets_Type()
)
wfMcT1LineTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineTxOctets.setStatus("mandatory")
_WfMcT1LineTxFrames_Type = Counter32
_WfMcT1LineTxFrames_Object = MibTableColumn
wfMcT1LineTxFrames = _WfMcT1LineTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 21),
    _WfMcT1LineTxFrames_Type()
)
wfMcT1LineTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineTxFrames.setStatus("mandatory")
_WfMcT1LineRxErrors_Type = Counter32
_WfMcT1LineRxErrors_Object = MibTableColumn
wfMcT1LineRxErrors = _WfMcT1LineRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 22),
    _WfMcT1LineRxErrors_Type()
)
wfMcT1LineRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxErrors.setStatus("mandatory")
_WfMcT1LineTxErrors_Type = Counter32
_WfMcT1LineTxErrors_Object = MibTableColumn
wfMcT1LineTxErrors = _WfMcT1LineTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 23),
    _WfMcT1LineTxErrors_Type()
)
wfMcT1LineTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineTxErrors.setStatus("mandatory")
_WfMcT1LineLackRxResources_Type = Counter32
_WfMcT1LineLackRxResources_Object = MibTableColumn
wfMcT1LineLackRxResources = _WfMcT1LineLackRxResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 24),
    _WfMcT1LineLackRxResources_Type()
)
wfMcT1LineLackRxResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineLackRxResources.setStatus("mandatory")
_WfMcT1LineLackTxResources_Type = Counter32
_WfMcT1LineLackTxResources_Object = MibTableColumn
wfMcT1LineLackTxResources = _WfMcT1LineLackTxResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 25),
    _WfMcT1LineLackTxResources_Type()
)
wfMcT1LineLackTxResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineLackTxResources.setStatus("mandatory")
_WfMcT1LineTxUnderflows_Type = Counter32
_WfMcT1LineTxUnderflows_Object = MibTableColumn
wfMcT1LineTxUnderflows = _WfMcT1LineTxUnderflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 26),
    _WfMcT1LineTxUnderflows_Type()
)
wfMcT1LineTxUnderflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineTxUnderflows.setStatus("mandatory")
_WfMcT1LineRxOverflows_Type = Counter32
_WfMcT1LineRxOverflows_Object = MibTableColumn
wfMcT1LineRxOverflows = _WfMcT1LineRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 27),
    _WfMcT1LineRxOverflows_Type()
)
wfMcT1LineRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxOverflows.setStatus("mandatory")
_WfMcT1LineRxNullFrames_Type = Counter32
_WfMcT1LineRxNullFrames_Object = MibTableColumn
wfMcT1LineRxNullFrames = _WfMcT1LineRxNullFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 28),
    _WfMcT1LineRxNullFrames_Type()
)
wfMcT1LineRxNullFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxNullFrames.setStatus("mandatory")
_WfMcT1LineRxShortFrames_Type = Counter32
_WfMcT1LineRxShortFrames_Object = MibTableColumn
wfMcT1LineRxShortFrames = _WfMcT1LineRxShortFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 29),
    _WfMcT1LineRxShortFrames_Type()
)
wfMcT1LineRxShortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxShortFrames.setStatus("mandatory")
_WfMcT1LineRxLossSyncs_Type = Counter32
_WfMcT1LineRxLossSyncs_Object = MibTableColumn
wfMcT1LineRxLossSyncs = _WfMcT1LineRxLossSyncs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 30),
    _WfMcT1LineRxLossSyncs_Type()
)
wfMcT1LineRxLossSyncs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxLossSyncs.setStatus("mandatory")
_WfMcT1LineRxCRCErrors_Type = Counter32
_WfMcT1LineRxCRCErrors_Object = MibTableColumn
wfMcT1LineRxCRCErrors = _WfMcT1LineRxCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 31),
    _WfMcT1LineRxCRCErrors_Type()
)
wfMcT1LineRxCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxCRCErrors.setStatus("mandatory")
_WfMcT1LineRxNonOctetBits_Type = Counter32
_WfMcT1LineRxNonOctetBits_Object = MibTableColumn
wfMcT1LineRxNonOctetBits = _WfMcT1LineRxNonOctetBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 32),
    _WfMcT1LineRxNonOctetBits_Type()
)
wfMcT1LineRxNonOctetBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxNonOctetBits.setStatus("mandatory")
_WfMcT1LineRxLongFrames_Type = Counter32
_WfMcT1LineRxLongFrames_Object = MibTableColumn
wfMcT1LineRxLongFrames = _WfMcT1LineRxLongFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 33),
    _WfMcT1LineRxLongFrames_Type()
)
wfMcT1LineRxLongFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxLongFrames.setStatus("mandatory")
_WfMcT1LineRxAbortFrames_Type = Counter32
_WfMcT1LineRxAbortFrames_Object = MibTableColumn
wfMcT1LineRxAbortFrames = _WfMcT1LineRxAbortFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 34),
    _WfMcT1LineRxAbortFrames_Type()
)
wfMcT1LineRxAbortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxAbortFrames.setStatus("mandatory")
_WfMcT1LineRxDescOverflows_Type = Counter32
_WfMcT1LineRxDescOverflows_Object = MibTableColumn
wfMcT1LineRxDescOverflows = _WfMcT1LineRxDescOverflows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 35),
    _WfMcT1LineRxDescOverflows_Type()
)
wfMcT1LineRxDescOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxDescOverflows.setStatus("mandatory")


class _WfMcT1LineTurboBofl_Type(Integer32):
    """Custom type wfMcT1LineTurboBofl based on Integer32"""
    defaultValue = 2

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


_WfMcT1LineTurboBofl_Type.__name__ = "Integer32"
_WfMcT1LineTurboBofl_Object = MibTableColumn
wfMcT1LineTurboBofl = _WfMcT1LineTurboBofl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 36),
    _WfMcT1LineTurboBofl_Type()
)
wfMcT1LineTurboBofl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineTurboBofl.setStatus("mandatory")


class _WfMcT1LineBoflNum_Type(Integer32):
    """Custom type wfMcT1LineBoflNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WfMcT1LineBoflNum_Type.__name__ = "Integer32"
_WfMcT1LineBoflNum_Object = MibTableColumn
wfMcT1LineBoflNum = _WfMcT1LineBoflNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 37),
    _WfMcT1LineBoflNum_Type()
)
wfMcT1LineBoflNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineBoflNum.setStatus("mandatory")


class _WfMcT1LineBoflLen_Type(Integer32):
    """Custom type wfMcT1LineBoflLen based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 4450),
    )


_WfMcT1LineBoflLen_Type.__name__ = "Integer32"
_WfMcT1LineBoflLen_Object = MibTableColumn
wfMcT1LineBoflLen = _WfMcT1LineBoflLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 38),
    _WfMcT1LineBoflLen_Type()
)
wfMcT1LineBoflLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineBoflLen.setStatus("mandatory")
_WfMcT1LineRxIntProcs_Type = Counter32
_WfMcT1LineRxIntProcs_Object = MibTableColumn
wfMcT1LineRxIntProcs = _WfMcT1LineRxIntProcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 39),
    _WfMcT1LineRxIntProcs_Type()
)
wfMcT1LineRxIntProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxIntProcs.setStatus("mandatory")
_WfMcT1LineTxIntProcs_Type = Counter32
_WfMcT1LineTxIntProcs_Object = MibTableColumn
wfMcT1LineTxIntProcs = _WfMcT1LineTxIntProcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 40),
    _WfMcT1LineTxIntProcs_Type()
)
wfMcT1LineTxIntProcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineTxIntProcs.setStatus("mandatory")
_WfMcT1LineRxPktCorruptions_Type = Counter32
_WfMcT1LineRxPktCorruptions_Object = MibTableColumn
wfMcT1LineRxPktCorruptions = _WfMcT1LineRxPktCorruptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 41),
    _WfMcT1LineRxPktCorruptions_Type()
)
wfMcT1LineRxPktCorruptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxPktCorruptions.setStatus("mandatory")
_WfMcT1LineRxReplenMisses_Type = Counter32
_WfMcT1LineRxReplenMisses_Object = MibTableColumn
wfMcT1LineRxReplenMisses = _WfMcT1LineRxReplenMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 42),
    _WfMcT1LineRxReplenMisses_Type()
)
wfMcT1LineRxReplenMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxReplenMisses.setStatus("mandatory")
_WfMcT1LineRxIFCs_Type = Counter32
_WfMcT1LineRxIFCs_Object = MibTableColumn
wfMcT1LineRxIFCs = _WfMcT1LineRxIFCs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 43),
    _WfMcT1LineRxIFCs_Type()
)
wfMcT1LineRxIFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxIFCs.setStatus("mandatory")


class _WfMcT1LineCfgTxQueueLength_Type(Integer32):
    """Custom type wfMcT1LineCfgTxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 336),
    )


_WfMcT1LineCfgTxQueueLength_Type.__name__ = "Integer32"
_WfMcT1LineCfgTxQueueLength_Object = MibTableColumn
wfMcT1LineCfgTxQueueLength = _WfMcT1LineCfgTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 44),
    _WfMcT1LineCfgTxQueueLength_Type()
)
wfMcT1LineCfgTxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineCfgTxQueueLength.setStatus("mandatory")


class _WfMcT1LineCfgRxQueueLength_Type(Integer32):
    """Custom type wfMcT1LineCfgRxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 336),
    )


_WfMcT1LineCfgRxQueueLength_Type.__name__ = "Integer32"
_WfMcT1LineCfgRxQueueLength_Object = MibTableColumn
wfMcT1LineCfgRxQueueLength = _WfMcT1LineCfgRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 45),
    _WfMcT1LineCfgRxQueueLength_Type()
)
wfMcT1LineCfgRxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineCfgRxQueueLength.setStatus("mandatory")
_WfMcT1LineTxQueueLength_Type = Integer32
_WfMcT1LineTxQueueLength_Object = MibTableColumn
wfMcT1LineTxQueueLength = _WfMcT1LineTxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 46),
    _WfMcT1LineTxQueueLength_Type()
)
wfMcT1LineTxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineTxQueueLength.setStatus("mandatory")
_WfMcT1LineRxQueueLength_Type = Integer32
_WfMcT1LineRxQueueLength_Object = MibTableColumn
wfMcT1LineRxQueueLength = _WfMcT1LineRxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 47),
    _WfMcT1LineRxQueueLength_Type()
)
wfMcT1LineRxQueueLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineRxQueueLength.setStatus("mandatory")
_WfMcT1LineTxQueueEmpty_Type = Integer32
_WfMcT1LineTxQueueEmpty_Object = MibTableColumn
wfMcT1LineTxQueueEmpty = _WfMcT1LineTxQueueEmpty_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 48),
    _WfMcT1LineTxQueueEmpty_Type()
)
wfMcT1LineTxQueueEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineTxQueueEmpty.setStatus("mandatory")
_WfMcT1LineMtu_Type = Integer32
_WfMcT1LineMtu_Object = MibTableColumn
wfMcT1LineMtu = _WfMcT1LineMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 49),
    _WfMcT1LineMtu_Type()
)
wfMcT1LineMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1LineMtu.setStatus("mandatory")
_WfMcT1LineRestart_Type = Integer32
_WfMcT1LineRestart_Object = MibTableColumn
wfMcT1LineRestart = _WfMcT1LineRestart_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 50),
    _WfMcT1LineRestart_Type()
)
wfMcT1LineRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineRestart.setStatus("mandatory")
_WfMcT1LineLineNumber_Type = Integer32
_WfMcT1LineLineNumber_Object = MibTableColumn
wfMcT1LineLineNumber = _WfMcT1LineLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 4, 1, 51),
    _WfMcT1LineLineNumber_Type()
)
wfMcT1LineLineNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMcT1LineLineNumber.setStatus("mandatory")
_WfMcT1Dsx1CurrentTable_Object = MibTable
wfMcT1Dsx1CurrentTable = _WfMcT1Dsx1CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5)
)
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentTable.setStatus("mandatory")
_WfMcT1Dsx1CurrentEntry_Object = MibTableRow
wfMcT1Dsx1CurrentEntry = _WfMcT1Dsx1CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1)
)
wfMcT1Dsx1CurrentEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Dsx1CurrentSlot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Dsx1CurrentConnector"),
)
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentEntry.setStatus("mandatory")


class _WfMcT1Dsx1CurrentSlot_Type(Integer32):
    """Custom type wfMcT1Dsx1CurrentSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1Dsx1CurrentSlot_Type.__name__ = "Integer32"
_WfMcT1Dsx1CurrentSlot_Object = MibTableColumn
wfMcT1Dsx1CurrentSlot = _WfMcT1Dsx1CurrentSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 1),
    _WfMcT1Dsx1CurrentSlot_Type()
)
wfMcT1Dsx1CurrentSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentSlot.setStatus("mandatory")


class _WfMcT1Dsx1CurrentConnector_Type(Integer32):
    """Custom type wfMcT1Dsx1CurrentConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1Dsx1CurrentConnector_Type.__name__ = "Integer32"
_WfMcT1Dsx1CurrentConnector_Object = MibTableColumn
wfMcT1Dsx1CurrentConnector = _WfMcT1Dsx1CurrentConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 2),
    _WfMcT1Dsx1CurrentConnector_Type()
)
wfMcT1Dsx1CurrentConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentConnector.setStatus("mandatory")
_WfMcT1Dsx1CurrentIntervalTimer_Type = Gauge32
_WfMcT1Dsx1CurrentIntervalTimer_Object = MibTableColumn
wfMcT1Dsx1CurrentIntervalTimer = _WfMcT1Dsx1CurrentIntervalTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 3),
    _WfMcT1Dsx1CurrentIntervalTimer_Type()
)
wfMcT1Dsx1CurrentIntervalTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentIntervalTimer.setStatus("mandatory")
_WfMcT1Dsx1CurrentESs_Type = Gauge32
_WfMcT1Dsx1CurrentESs_Object = MibTableColumn
wfMcT1Dsx1CurrentESs = _WfMcT1Dsx1CurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 4),
    _WfMcT1Dsx1CurrentESs_Type()
)
wfMcT1Dsx1CurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentESs.setStatus("mandatory")
_WfMcT1Dsx1CurrentSESs_Type = Gauge32
_WfMcT1Dsx1CurrentSESs_Object = MibTableColumn
wfMcT1Dsx1CurrentSESs = _WfMcT1Dsx1CurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 5),
    _WfMcT1Dsx1CurrentSESs_Type()
)
wfMcT1Dsx1CurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentSESs.setStatus("mandatory")
_WfMcT1Dsx1CurrentBESs_Type = Gauge32
_WfMcT1Dsx1CurrentBESs_Object = MibTableColumn
wfMcT1Dsx1CurrentBESs = _WfMcT1Dsx1CurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 6),
    _WfMcT1Dsx1CurrentBESs_Type()
)
wfMcT1Dsx1CurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentBESs.setStatus("mandatory")
_WfMcT1Dsx1CurrentUASs_Type = Gauge32
_WfMcT1Dsx1CurrentUASs_Object = MibTableColumn
wfMcT1Dsx1CurrentUASs = _WfMcT1Dsx1CurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 7),
    _WfMcT1Dsx1CurrentUASs_Type()
)
wfMcT1Dsx1CurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentUASs.setStatus("mandatory")
_WfMcT1Dsx1CurrentCSSs_Type = Gauge32
_WfMcT1Dsx1CurrentCSSs_Object = MibTableColumn
wfMcT1Dsx1CurrentCSSs = _WfMcT1Dsx1CurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 8),
    _WfMcT1Dsx1CurrentCSSs_Type()
)
wfMcT1Dsx1CurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentCSSs.setStatus("mandatory")
_WfMcT1Dsx1CurrentBPVs_Type = Gauge32
_WfMcT1Dsx1CurrentBPVs_Object = MibTableColumn
wfMcT1Dsx1CurrentBPVs = _WfMcT1Dsx1CurrentBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 5, 1, 9),
    _WfMcT1Dsx1CurrentBPVs_Type()
)
wfMcT1Dsx1CurrentBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1CurrentBPVs.setStatus("mandatory")
_WfMcT1Dsx1IntervalTable_Object = MibTable
wfMcT1Dsx1IntervalTable = _WfMcT1Dsx1IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6)
)
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalTable.setStatus("mandatory")
_WfMcT1Dsx1IntervalEntry_Object = MibTableRow
wfMcT1Dsx1IntervalEntry = _WfMcT1Dsx1IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1)
)
wfMcT1Dsx1IntervalEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Dsx1IntervalSlot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Dsx1IntervalConnector"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Dsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalEntry.setStatus("mandatory")


class _WfMcT1Dsx1IntervalSlot_Type(Integer32):
    """Custom type wfMcT1Dsx1IntervalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1Dsx1IntervalSlot_Type.__name__ = "Integer32"
_WfMcT1Dsx1IntervalSlot_Object = MibTableColumn
wfMcT1Dsx1IntervalSlot = _WfMcT1Dsx1IntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 1),
    _WfMcT1Dsx1IntervalSlot_Type()
)
wfMcT1Dsx1IntervalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalSlot.setStatus("mandatory")


class _WfMcT1Dsx1IntervalConnector_Type(Integer32):
    """Custom type wfMcT1Dsx1IntervalConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1Dsx1IntervalConnector_Type.__name__ = "Integer32"
_WfMcT1Dsx1IntervalConnector_Object = MibTableColumn
wfMcT1Dsx1IntervalConnector = _WfMcT1Dsx1IntervalConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 2),
    _WfMcT1Dsx1IntervalConnector_Type()
)
wfMcT1Dsx1IntervalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalConnector.setStatus("mandatory")


class _WfMcT1Dsx1IntervalNumber_Type(Integer32):
    """Custom type wfMcT1Dsx1IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WfMcT1Dsx1IntervalNumber_Type.__name__ = "Integer32"
_WfMcT1Dsx1IntervalNumber_Object = MibTableColumn
wfMcT1Dsx1IntervalNumber = _WfMcT1Dsx1IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 3),
    _WfMcT1Dsx1IntervalNumber_Type()
)
wfMcT1Dsx1IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalNumber.setStatus("mandatory")
_WfMcT1Dsx1IntervalESs_Type = Gauge32
_WfMcT1Dsx1IntervalESs_Object = MibTableColumn
wfMcT1Dsx1IntervalESs = _WfMcT1Dsx1IntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 4),
    _WfMcT1Dsx1IntervalESs_Type()
)
wfMcT1Dsx1IntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalESs.setStatus("mandatory")
_WfMcT1Dsx1IntervalSESs_Type = Gauge32
_WfMcT1Dsx1IntervalSESs_Object = MibTableColumn
wfMcT1Dsx1IntervalSESs = _WfMcT1Dsx1IntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 5),
    _WfMcT1Dsx1IntervalSESs_Type()
)
wfMcT1Dsx1IntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalSESs.setStatus("mandatory")
_WfMcT1Dsx1IntervalBESs_Type = Gauge32
_WfMcT1Dsx1IntervalBESs_Object = MibTableColumn
wfMcT1Dsx1IntervalBESs = _WfMcT1Dsx1IntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 6),
    _WfMcT1Dsx1IntervalBESs_Type()
)
wfMcT1Dsx1IntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalBESs.setStatus("mandatory")
_WfMcT1Dsx1IntervalUASs_Type = Gauge32
_WfMcT1Dsx1IntervalUASs_Object = MibTableColumn
wfMcT1Dsx1IntervalUASs = _WfMcT1Dsx1IntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 7),
    _WfMcT1Dsx1IntervalUASs_Type()
)
wfMcT1Dsx1IntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalUASs.setStatus("mandatory")
_WfMcT1Dsx1IntervalCSSs_Type = Gauge32
_WfMcT1Dsx1IntervalCSSs_Object = MibTableColumn
wfMcT1Dsx1IntervalCSSs = _WfMcT1Dsx1IntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 8),
    _WfMcT1Dsx1IntervalCSSs_Type()
)
wfMcT1Dsx1IntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalCSSs.setStatus("mandatory")
_WfMcT1Dsx1IntervalBPVs_Type = Gauge32
_WfMcT1Dsx1IntervalBPVs_Object = MibTableColumn
wfMcT1Dsx1IntervalBPVs = _WfMcT1Dsx1IntervalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 6, 1, 9),
    _WfMcT1Dsx1IntervalBPVs_Type()
)
wfMcT1Dsx1IntervalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1IntervalBPVs.setStatus("mandatory")
_WfMcT1Dsx1TotalTable_Object = MibTable
wfMcT1Dsx1TotalTable = _WfMcT1Dsx1TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7)
)
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalTable.setStatus("mandatory")
_WfMcT1Dsx1TotalEntry_Object = MibTableRow
wfMcT1Dsx1TotalEntry = _WfMcT1Dsx1TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1)
)
wfMcT1Dsx1TotalEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Dsx1TotalSlot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1Dsx1TotalConnector"),
)
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalEntry.setStatus("mandatory")


class _WfMcT1Dsx1TotalSlot_Type(Integer32):
    """Custom type wfMcT1Dsx1TotalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1Dsx1TotalSlot_Type.__name__ = "Integer32"
_WfMcT1Dsx1TotalSlot_Object = MibTableColumn
wfMcT1Dsx1TotalSlot = _WfMcT1Dsx1TotalSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 1),
    _WfMcT1Dsx1TotalSlot_Type()
)
wfMcT1Dsx1TotalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalSlot.setStatus("mandatory")


class _WfMcT1Dsx1TotalConnector_Type(Integer32):
    """Custom type wfMcT1Dsx1TotalConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1Dsx1TotalConnector_Type.__name__ = "Integer32"
_WfMcT1Dsx1TotalConnector_Object = MibTableColumn
wfMcT1Dsx1TotalConnector = _WfMcT1Dsx1TotalConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 2),
    _WfMcT1Dsx1TotalConnector_Type()
)
wfMcT1Dsx1TotalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalConnector.setStatus("mandatory")
_WfMcT1Dsx1TotalVITR_Type = Gauge32
_WfMcT1Dsx1TotalVITR_Object = MibTableColumn
wfMcT1Dsx1TotalVITR = _WfMcT1Dsx1TotalVITR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 3),
    _WfMcT1Dsx1TotalVITR_Type()
)
wfMcT1Dsx1TotalVITR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalVITR.setStatus("mandatory")
_WfMcT1Dsx1TotalESs_Type = Gauge32
_WfMcT1Dsx1TotalESs_Object = MibTableColumn
wfMcT1Dsx1TotalESs = _WfMcT1Dsx1TotalESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 4),
    _WfMcT1Dsx1TotalESs_Type()
)
wfMcT1Dsx1TotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalESs.setStatus("mandatory")
_WfMcT1Dsx1TotalSESs_Type = Gauge32
_WfMcT1Dsx1TotalSESs_Object = MibTableColumn
wfMcT1Dsx1TotalSESs = _WfMcT1Dsx1TotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 5),
    _WfMcT1Dsx1TotalSESs_Type()
)
wfMcT1Dsx1TotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalSESs.setStatus("mandatory")
_WfMcT1Dsx1TotalBESs_Type = Gauge32
_WfMcT1Dsx1TotalBESs_Object = MibTableColumn
wfMcT1Dsx1TotalBESs = _WfMcT1Dsx1TotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 6),
    _WfMcT1Dsx1TotalBESs_Type()
)
wfMcT1Dsx1TotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalBESs.setStatus("mandatory")
_WfMcT1Dsx1TotalUASs_Type = Gauge32
_WfMcT1Dsx1TotalUASs_Object = MibTableColumn
wfMcT1Dsx1TotalUASs = _WfMcT1Dsx1TotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 7),
    _WfMcT1Dsx1TotalUASs_Type()
)
wfMcT1Dsx1TotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalUASs.setStatus("mandatory")
_WfMcT1Dsx1TotalCSSs_Type = Gauge32
_WfMcT1Dsx1TotalCSSs_Object = MibTableColumn
wfMcT1Dsx1TotalCSSs = _WfMcT1Dsx1TotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 8),
    _WfMcT1Dsx1TotalCSSs_Type()
)
wfMcT1Dsx1TotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalCSSs.setStatus("mandatory")
_WfMcT1Dsx1TotalBPVs_Type = Gauge32
_WfMcT1Dsx1TotalBPVs_Object = MibTableColumn
wfMcT1Dsx1TotalBPVs = _WfMcT1Dsx1TotalBPVs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 7, 1, 9),
    _WfMcT1Dsx1TotalBPVs_Type()
)
wfMcT1Dsx1TotalBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1Dsx1TotalBPVs.setStatus("mandatory")
_WfMcT1AnsiTable_Object = MibTable
wfMcT1AnsiTable = _WfMcT1AnsiTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8)
)
if mibBuilder.loadTexts:
    wfMcT1AnsiTable.setStatus("mandatory")
_WfMcT1AnsiEntry_Object = MibTableRow
wfMcT1AnsiEntry = _WfMcT1AnsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1)
)
wfMcT1AnsiEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1AnsiSlot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1AnsiConnector"),
)
if mibBuilder.loadTexts:
    wfMcT1AnsiEntry.setStatus("mandatory")


class _WfMcT1AnsiSlot_Type(Integer32):
    """Custom type wfMcT1AnsiSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1AnsiSlot_Type.__name__ = "Integer32"
_WfMcT1AnsiSlot_Object = MibTableColumn
wfMcT1AnsiSlot = _WfMcT1AnsiSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 1),
    _WfMcT1AnsiSlot_Type()
)
wfMcT1AnsiSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiSlot.setStatus("mandatory")


class _WfMcT1AnsiConnector_Type(Integer32):
    """Custom type wfMcT1AnsiConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1AnsiConnector_Type.__name__ = "Integer32"
_WfMcT1AnsiConnector_Object = MibTableColumn
wfMcT1AnsiConnector = _WfMcT1AnsiConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 2),
    _WfMcT1AnsiConnector_Type()
)
wfMcT1AnsiConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiConnector.setStatus("mandatory")
_WfMcT1AnsiCRCCounts_Type = Counter32
_WfMcT1AnsiCRCCounts_Object = MibTableColumn
wfMcT1AnsiCRCCounts = _WfMcT1AnsiCRCCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 3),
    _WfMcT1AnsiCRCCounts_Type()
)
wfMcT1AnsiCRCCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiCRCCounts.setStatus("mandatory")
_WfMcT1AnsiBPVCounts_Type = Counter32
_WfMcT1AnsiBPVCounts_Object = MibTableColumn
wfMcT1AnsiBPVCounts = _WfMcT1AnsiBPVCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 4),
    _WfMcT1AnsiBPVCounts_Type()
)
wfMcT1AnsiBPVCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiBPVCounts.setStatus("mandatory")
_WfMcT1AnsiOOFCounts_Type = Counter32
_WfMcT1AnsiOOFCounts_Object = MibTableColumn
wfMcT1AnsiOOFCounts = _WfMcT1AnsiOOFCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 5),
    _WfMcT1AnsiOOFCounts_Type()
)
wfMcT1AnsiOOFCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiOOFCounts.setStatus("mandatory")
_WfMcT1AnsiFECounts_Type = Counter32
_WfMcT1AnsiFECounts_Object = MibTableColumn
wfMcT1AnsiFECounts = _WfMcT1AnsiFECounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 6),
    _WfMcT1AnsiFECounts_Type()
)
wfMcT1AnsiFECounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiFECounts.setStatus("mandatory")
_WfMcT1AnsiESCounts_Type = Counter32
_WfMcT1AnsiESCounts_Object = MibTableColumn
wfMcT1AnsiESCounts = _WfMcT1AnsiESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 7),
    _WfMcT1AnsiESCounts_Type()
)
wfMcT1AnsiESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiESCounts.setStatus("mandatory")
_WfMcT1AnsiSESCounts_Type = Counter32
_WfMcT1AnsiSESCounts_Object = MibTableColumn
wfMcT1AnsiSESCounts = _WfMcT1AnsiSESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 8),
    _WfMcT1AnsiSESCounts_Type()
)
wfMcT1AnsiSESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiSESCounts.setStatus("mandatory")
_WfMcT1AnsiUASCounts_Type = Counter32
_WfMcT1AnsiUASCounts_Object = MibTableColumn
wfMcT1AnsiUASCounts = _WfMcT1AnsiUASCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 9),
    _WfMcT1AnsiUASCounts_Type()
)
wfMcT1AnsiUASCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiUASCounts.setStatus("mandatory")
_WfMcT1AnsiPRMR0Counts_Type = Counter32
_WfMcT1AnsiPRMR0Counts_Object = MibTableColumn
wfMcT1AnsiPRMR0Counts = _WfMcT1AnsiPRMR0Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 10),
    _WfMcT1AnsiPRMR0Counts_Type()
)
wfMcT1AnsiPRMR0Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiPRMR0Counts.setStatus("mandatory")
_WfMcT1AnsiPRMR1Counts_Type = Counter32
_WfMcT1AnsiPRMR1Counts_Object = MibTableColumn
wfMcT1AnsiPRMR1Counts = _WfMcT1AnsiPRMR1Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 11),
    _WfMcT1AnsiPRMR1Counts_Type()
)
wfMcT1AnsiPRMR1Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiPRMR1Counts.setStatus("mandatory")
_WfMcT1AnsiPRMR2Counts_Type = Counter32
_WfMcT1AnsiPRMR2Counts_Object = MibTableColumn
wfMcT1AnsiPRMR2Counts = _WfMcT1AnsiPRMR2Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 12),
    _WfMcT1AnsiPRMR2Counts_Type()
)
wfMcT1AnsiPRMR2Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiPRMR2Counts.setStatus("mandatory")
_WfMcT1AnsiPRMR3Counts_Type = Counter32
_WfMcT1AnsiPRMR3Counts_Object = MibTableColumn
wfMcT1AnsiPRMR3Counts = _WfMcT1AnsiPRMR3Counts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 13),
    _WfMcT1AnsiPRMR3Counts_Type()
)
wfMcT1AnsiPRMR3Counts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiPRMR3Counts.setStatus("mandatory")
_WfMcT1AnsiPRMESCounts_Type = Counter32
_WfMcT1AnsiPRMESCounts_Object = MibTableColumn
wfMcT1AnsiPRMESCounts = _WfMcT1AnsiPRMESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 14),
    _WfMcT1AnsiPRMESCounts_Type()
)
wfMcT1AnsiPRMESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiPRMESCounts.setStatus("mandatory")
_WfMcT1AnsiPRMSESCounts_Type = Counter32
_WfMcT1AnsiPRMSESCounts_Object = MibTableColumn
wfMcT1AnsiPRMSESCounts = _WfMcT1AnsiPRMSESCounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 15),
    _WfMcT1AnsiPRMSESCounts_Type()
)
wfMcT1AnsiPRMSESCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiPRMSESCounts.setStatus("mandatory")
_WfMcT1AnsiPRMECounts_Type = Counter32
_WfMcT1AnsiPRMECounts_Object = MibTableColumn
wfMcT1AnsiPRMECounts = _WfMcT1AnsiPRMECounts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 8, 1, 16),
    _WfMcT1AnsiPRMECounts_Type()
)
wfMcT1AnsiPRMECounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1AnsiPRMECounts.setStatus("mandatory")
_WfMcT1BertStatsTable_Object = MibTable
wfMcT1BertStatsTable = _WfMcT1BertStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 9)
)
if mibBuilder.loadTexts:
    wfMcT1BertStatsTable.setStatus("mandatory")
_WfMcT1BertStatsEntry_Object = MibTableRow
wfMcT1BertStatsEntry = _WfMcT1BertStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 9, 1)
)
wfMcT1BertStatsEntry.setIndexNames(
    (0, "Wellfleet-MCT1-MIB", "wfMcT1BertStatsSlot"),
    (0, "Wellfleet-MCT1-MIB", "wfMcT1BertStatsConnector"),
)
if mibBuilder.loadTexts:
    wfMcT1BertStatsEntry.setStatus("mandatory")


class _WfMcT1BertStatsSlot_Type(Integer32):
    """Custom type wfMcT1BertStatsSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfMcT1BertStatsSlot_Type.__name__ = "Integer32"
_WfMcT1BertStatsSlot_Object = MibTableColumn
wfMcT1BertStatsSlot = _WfMcT1BertStatsSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 9, 1, 1),
    _WfMcT1BertStatsSlot_Type()
)
wfMcT1BertStatsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1BertStatsSlot.setStatus("mandatory")


class _WfMcT1BertStatsConnector_Type(Integer32):
    """Custom type wfMcT1BertStatsConnector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_WfMcT1BertStatsConnector_Type.__name__ = "Integer32"
_WfMcT1BertStatsConnector_Object = MibTableColumn
wfMcT1BertStatsConnector = _WfMcT1BertStatsConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 9, 1, 2),
    _WfMcT1BertStatsConnector_Type()
)
wfMcT1BertStatsConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1BertStatsConnector.setStatus("mandatory")
_WfMcT1BertStatsBitErrors_Type = Counter32
_WfMcT1BertStatsBitErrors_Object = MibTableColumn
wfMcT1BertStatsBitErrors = _WfMcT1BertStatsBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 9, 1, 3),
    _WfMcT1BertStatsBitErrors_Type()
)
wfMcT1BertStatsBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1BertStatsBitErrors.setStatus("mandatory")
_WfMcT1BertStatsBits_Type = Counter32
_WfMcT1BertStatsBits_Object = MibTableColumn
wfMcT1BertStatsBits = _WfMcT1BertStatsBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 8, 9, 1, 4),
    _WfMcT1BertStatsBits_Type()
)
wfMcT1BertStatsBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMcT1BertStatsBits.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-MCT1-MIB",
    **{"wfMcT1ModTable": wfMcT1ModTable,
       "wfMcT1ModEntry": wfMcT1ModEntry,
       "wfMcT1ModDelete": wfMcT1ModDelete,
       "wfMcT1ModDisable": wfMcT1ModDisable,
       "wfMcT1ModSlot": wfMcT1ModSlot,
       "wfMcT1ModPrimaryClock": wfMcT1ModPrimaryClock,
       "wfMcT1ModSecondaryClock": wfMcT1ModSecondaryClock,
       "wfMcT1ModCurrentClock": wfMcT1ModCurrentClock,
       "wfMcT1ModExtClockOperational": wfMcT1ModExtClockOperational,
       "wfMcT1ModLoop0ClockOperational": wfMcT1ModLoop0ClockOperational,
       "wfMcT1ModLoop1ClockOperational": wfMcT1ModLoop1ClockOperational,
       "wfMcT1ModRestart": wfMcT1ModRestart,
       "wfMcT1Table": wfMcT1Table,
       "wfMcT1Entry": wfMcT1Entry,
       "wfMcT1Delete": wfMcT1Delete,
       "wfMcT1Disable": wfMcT1Disable,
       "wfMcT1State": wfMcT1State,
       "wfMcT1Slot": wfMcT1Slot,
       "wfMcT1Connector": wfMcT1Connector,
       "wfMcT1OperationMode": wfMcT1OperationMode,
       "wfMcT1Mtu": wfMcT1Mtu,
       "wfMcT1MunichVersion": wfMcT1MunichVersion,
       "wfMcT1Dsx1LineType": wfMcT1Dsx1LineType,
       "wfMcT1Dsx1ZeroCoding": wfMcT1Dsx1ZeroCoding,
       "wfMcT1Dsx1LoopbackConfig": wfMcT1Dsx1LoopbackConfig,
       "wfMcT1Dsx1LineStatus": wfMcT1Dsx1LineStatus,
       "wfMcT1Dsx1SetupAlarmThreshold": wfMcT1Dsx1SetupAlarmThreshold,
       "wfMcT1Dsx1ClearAlarmThreshold": wfMcT1Dsx1ClearAlarmThreshold,
       "wfMcT1Dsx1SignalLevel": wfMcT1Dsx1SignalLevel,
       "wfMcT1LoopbackDisable": wfMcT1LoopbackDisable,
       "wfMcT1Dsx1FDLOperationMode": wfMcT1Dsx1FDLOperationMode,
       "wfMcT1BertTxOutputLevel": wfMcT1BertTxOutputLevel,
       "wfMcT1BertTestMode": wfMcT1BertTestMode,
       "wfMcT1BertLineCode": wfMcT1BertLineCode,
       "wfMcT1BertTestPattern": wfMcT1BertTestPattern,
       "wfMcT1BertSendAlarm": wfMcT1BertSendAlarm,
       "wfMcT1DS2282Version": wfMcT1DS2282Version,
       "wfMcT1Restart": wfMcT1Restart,
       "wfMcT1Loopback": wfMcT1Loopback,
       "wfMcT1FDLTargetAddress": wfMcT1FDLTargetAddress,
       "wfMcT1ConfigTable": wfMcT1ConfigTable,
       "wfMcT1ConfigEntry": wfMcT1ConfigEntry,
       "wfMcT1ConfigSlot": wfMcT1ConfigSlot,
       "wfMcT1ConfigConnector": wfMcT1ConfigConnector,
       "wfMcT1BertRestart": wfMcT1BertRestart,
       "wfMcT1BertPayldLb": wfMcT1BertPayldLb,
       "wfMcT1BertLineLb": wfMcT1BertLineLb,
       "wfMcT1BertErrorInsert": wfMcT1BertErrorInsert,
       "wfMcT1Dsx1SendLoopCode": wfMcT1Dsx1SendLoopCode,
       "wfMcT1Dsx1SendFDLCode": wfMcT1Dsx1SendFDLCode,
       "wfMcT1LineTable": wfMcT1LineTable,
       "wfMcT1LineEntry": wfMcT1LineEntry,
       "wfMcT1LineDelete": wfMcT1LineDelete,
       "wfMcT1LineDisable": wfMcT1LineDisable,
       "wfMcT1LineState": wfMcT1LineState,
       "wfMcT1LineSlot": wfMcT1LineSlot,
       "wfMcT1LineConnector": wfMcT1LineConnector,
       "wfMcT1LineLine": wfMcT1LineLine,
       "wfMcT1LineCct": wfMcT1LineCct,
       "wfMcT1LineBofl": wfMcT1LineBofl,
       "wfMcT1LineBoflTmo": wfMcT1LineBoflTmo,
       "wfMcT1LineFractionalLpbk": wfMcT1LineFractionalLpbk,
       "wfMcT1LineChannelAssignment": wfMcT1LineChannelAssignment,
       "wfMcT1LineMadr": wfMcT1LineMadr,
       "wfMcT1LineWanProtocol": wfMcT1LineWanProtocol,
       "wfMcT1LineService": wfMcT1LineService,
       "wfMcT1LineRateAdaption": wfMcT1LineRateAdaption,
       "wfMcT1LineIFTF": wfMcT1LineIFTF,
       "wfMcT1LineCRCSize": wfMcT1LineCRCSize,
       "wfMcT1LineRxOctets": wfMcT1LineRxOctets,
       "wfMcT1LineRxFrames": wfMcT1LineRxFrames,
       "wfMcT1LineTxOctets": wfMcT1LineTxOctets,
       "wfMcT1LineTxFrames": wfMcT1LineTxFrames,
       "wfMcT1LineRxErrors": wfMcT1LineRxErrors,
       "wfMcT1LineTxErrors": wfMcT1LineTxErrors,
       "wfMcT1LineLackRxResources": wfMcT1LineLackRxResources,
       "wfMcT1LineLackTxResources": wfMcT1LineLackTxResources,
       "wfMcT1LineTxUnderflows": wfMcT1LineTxUnderflows,
       "wfMcT1LineRxOverflows": wfMcT1LineRxOverflows,
       "wfMcT1LineRxNullFrames": wfMcT1LineRxNullFrames,
       "wfMcT1LineRxShortFrames": wfMcT1LineRxShortFrames,
       "wfMcT1LineRxLossSyncs": wfMcT1LineRxLossSyncs,
       "wfMcT1LineRxCRCErrors": wfMcT1LineRxCRCErrors,
       "wfMcT1LineRxNonOctetBits": wfMcT1LineRxNonOctetBits,
       "wfMcT1LineRxLongFrames": wfMcT1LineRxLongFrames,
       "wfMcT1LineRxAbortFrames": wfMcT1LineRxAbortFrames,
       "wfMcT1LineRxDescOverflows": wfMcT1LineRxDescOverflows,
       "wfMcT1LineTurboBofl": wfMcT1LineTurboBofl,
       "wfMcT1LineBoflNum": wfMcT1LineBoflNum,
       "wfMcT1LineBoflLen": wfMcT1LineBoflLen,
       "wfMcT1LineRxIntProcs": wfMcT1LineRxIntProcs,
       "wfMcT1LineTxIntProcs": wfMcT1LineTxIntProcs,
       "wfMcT1LineRxPktCorruptions": wfMcT1LineRxPktCorruptions,
       "wfMcT1LineRxReplenMisses": wfMcT1LineRxReplenMisses,
       "wfMcT1LineRxIFCs": wfMcT1LineRxIFCs,
       "wfMcT1LineCfgTxQueueLength": wfMcT1LineCfgTxQueueLength,
       "wfMcT1LineCfgRxQueueLength": wfMcT1LineCfgRxQueueLength,
       "wfMcT1LineTxQueueLength": wfMcT1LineTxQueueLength,
       "wfMcT1LineRxQueueLength": wfMcT1LineRxQueueLength,
       "wfMcT1LineTxQueueEmpty": wfMcT1LineTxQueueEmpty,
       "wfMcT1LineMtu": wfMcT1LineMtu,
       "wfMcT1LineRestart": wfMcT1LineRestart,
       "wfMcT1LineLineNumber": wfMcT1LineLineNumber,
       "wfMcT1Dsx1CurrentTable": wfMcT1Dsx1CurrentTable,
       "wfMcT1Dsx1CurrentEntry": wfMcT1Dsx1CurrentEntry,
       "wfMcT1Dsx1CurrentSlot": wfMcT1Dsx1CurrentSlot,
       "wfMcT1Dsx1CurrentConnector": wfMcT1Dsx1CurrentConnector,
       "wfMcT1Dsx1CurrentIntervalTimer": wfMcT1Dsx1CurrentIntervalTimer,
       "wfMcT1Dsx1CurrentESs": wfMcT1Dsx1CurrentESs,
       "wfMcT1Dsx1CurrentSESs": wfMcT1Dsx1CurrentSESs,
       "wfMcT1Dsx1CurrentBESs": wfMcT1Dsx1CurrentBESs,
       "wfMcT1Dsx1CurrentUASs": wfMcT1Dsx1CurrentUASs,
       "wfMcT1Dsx1CurrentCSSs": wfMcT1Dsx1CurrentCSSs,
       "wfMcT1Dsx1CurrentBPVs": wfMcT1Dsx1CurrentBPVs,
       "wfMcT1Dsx1IntervalTable": wfMcT1Dsx1IntervalTable,
       "wfMcT1Dsx1IntervalEntry": wfMcT1Dsx1IntervalEntry,
       "wfMcT1Dsx1IntervalSlot": wfMcT1Dsx1IntervalSlot,
       "wfMcT1Dsx1IntervalConnector": wfMcT1Dsx1IntervalConnector,
       "wfMcT1Dsx1IntervalNumber": wfMcT1Dsx1IntervalNumber,
       "wfMcT1Dsx1IntervalESs": wfMcT1Dsx1IntervalESs,
       "wfMcT1Dsx1IntervalSESs": wfMcT1Dsx1IntervalSESs,
       "wfMcT1Dsx1IntervalBESs": wfMcT1Dsx1IntervalBESs,
       "wfMcT1Dsx1IntervalUASs": wfMcT1Dsx1IntervalUASs,
       "wfMcT1Dsx1IntervalCSSs": wfMcT1Dsx1IntervalCSSs,
       "wfMcT1Dsx1IntervalBPVs": wfMcT1Dsx1IntervalBPVs,
       "wfMcT1Dsx1TotalTable": wfMcT1Dsx1TotalTable,
       "wfMcT1Dsx1TotalEntry": wfMcT1Dsx1TotalEntry,
       "wfMcT1Dsx1TotalSlot": wfMcT1Dsx1TotalSlot,
       "wfMcT1Dsx1TotalConnector": wfMcT1Dsx1TotalConnector,
       "wfMcT1Dsx1TotalVITR": wfMcT1Dsx1TotalVITR,
       "wfMcT1Dsx1TotalESs": wfMcT1Dsx1TotalESs,
       "wfMcT1Dsx1TotalSESs": wfMcT1Dsx1TotalSESs,
       "wfMcT1Dsx1TotalBESs": wfMcT1Dsx1TotalBESs,
       "wfMcT1Dsx1TotalUASs": wfMcT1Dsx1TotalUASs,
       "wfMcT1Dsx1TotalCSSs": wfMcT1Dsx1TotalCSSs,
       "wfMcT1Dsx1TotalBPVs": wfMcT1Dsx1TotalBPVs,
       "wfMcT1AnsiTable": wfMcT1AnsiTable,
       "wfMcT1AnsiEntry": wfMcT1AnsiEntry,
       "wfMcT1AnsiSlot": wfMcT1AnsiSlot,
       "wfMcT1AnsiConnector": wfMcT1AnsiConnector,
       "wfMcT1AnsiCRCCounts": wfMcT1AnsiCRCCounts,
       "wfMcT1AnsiBPVCounts": wfMcT1AnsiBPVCounts,
       "wfMcT1AnsiOOFCounts": wfMcT1AnsiOOFCounts,
       "wfMcT1AnsiFECounts": wfMcT1AnsiFECounts,
       "wfMcT1AnsiESCounts": wfMcT1AnsiESCounts,
       "wfMcT1AnsiSESCounts": wfMcT1AnsiSESCounts,
       "wfMcT1AnsiUASCounts": wfMcT1AnsiUASCounts,
       "wfMcT1AnsiPRMR0Counts": wfMcT1AnsiPRMR0Counts,
       "wfMcT1AnsiPRMR1Counts": wfMcT1AnsiPRMR1Counts,
       "wfMcT1AnsiPRMR2Counts": wfMcT1AnsiPRMR2Counts,
       "wfMcT1AnsiPRMR3Counts": wfMcT1AnsiPRMR3Counts,
       "wfMcT1AnsiPRMESCounts": wfMcT1AnsiPRMESCounts,
       "wfMcT1AnsiPRMSESCounts": wfMcT1AnsiPRMSESCounts,
       "wfMcT1AnsiPRMECounts": wfMcT1AnsiPRMECounts,
       "wfMcT1BertStatsTable": wfMcT1BertStatsTable,
       "wfMcT1BertStatsEntry": wfMcT1BertStatsEntry,
       "wfMcT1BertStatsSlot": wfMcT1BertStatsSlot,
       "wfMcT1BertStatsConnector": wfMcT1BertStatsConnector,
       "wfMcT1BertStatsBitErrors": wfMcT1BertStatsBitErrors,
       "wfMcT1BertStatsBits": wfMcT1BertStatsBits}
)
