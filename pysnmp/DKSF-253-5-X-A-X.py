# SNMP MIB module (DKSF-253-5-X-A-X) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DKSF-253-5-X-A-X
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:20 2024
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

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

netPing = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 50)
)
netPing.setRevisions(
        ("2014-11-19 00:00",
         "2014-06-12 00:00",
         "2011-02-04 00:00",
         "2010-08-30 00:00",
         "2010-08-20 00:00",
         "2010-08-13 00:00",
         "2010-08-11 00:00",
         "2010-07-08 00:00",
         "2010-04-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lightcom_ObjectIdentity = ObjectIdentity
lightcom = _Lightcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728)
)
_NpReboot_ObjectIdentity = ObjectIdentity
npReboot = _NpReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 911)
)
_NpSoftReboot_Type = Integer32
_NpSoftReboot_Object = MibScalar
npSoftReboot = _NpSoftReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 1),
    _NpSoftReboot_Type()
)
npSoftReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSoftReboot.setStatus("current")
_NpResetStack_Type = Integer32
_NpResetStack_Object = MibScalar
npResetStack = _NpResetStack_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 2),
    _NpResetStack_Type()
)
npResetStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npResetStack.setStatus("current")
_NpForcedReboot_Type = Integer32
_NpForcedReboot_Object = MibScalar
npForcedReboot = _NpForcedReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 3),
    _NpForcedReboot_Type()
)
npForcedReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npForcedReboot.setStatus("current")
_NpIo_ObjectIdentity = ObjectIdentity
npIo = _NpIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900)
)
_NpIoTable_Object = MibTable
npIoTable = _NpIoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1)
)
if mibBuilder.loadTexts:
    npIoTable.setStatus("current")
_NpIoEntry_Object = MibTableRow
npIoEntry = _NpIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1)
)
npIoEntry.setIndexNames(
    (0, "DKSF-253-5-X-A-X", "npIoLineN"),
)
if mibBuilder.loadTexts:
    npIoEntry.setStatus("current")


class _NpIoLineN_Type(Integer32):
    """Custom type npIoLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpIoLineN_Type.__name__ = "Integer32"
_NpIoLineN_Object = MibTableColumn
npIoLineN = _NpIoLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1),
    _NpIoLineN_Type()
)
npIoLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLineN.setStatus("current")


class _NpIoLevelIn_Type(Integer32):
    """Custom type npIoLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoLevelIn_Type.__name__ = "Integer32"
_NpIoLevelIn_Object = MibTableColumn
npIoLevelIn = _NpIoLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2),
    _NpIoLevelIn_Type()
)
npIoLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLevelIn.setStatus("current")


class _NpIoLevelOut_Type(Integer32):
    """Custom type npIoLevelOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoLevelOut_Type.__name__ = "Integer32"
_NpIoLevelOut_Object = MibTableColumn
npIoLevelOut = _NpIoLevelOut_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3),
    _NpIoLevelOut_Type()
)
npIoLevelOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoLevelOut.setStatus("current")
_NpIoMemo_Type = DisplayString
_NpIoMemo_Object = MibTableColumn
npIoMemo = _NpIoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6),
    _NpIoMemo_Type()
)
npIoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoMemo.setStatus("current")
_NpIoPulseCounter_Type = Counter32
_NpIoPulseCounter_Object = MibTableColumn
npIoPulseCounter = _NpIoPulseCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9),
    _NpIoPulseCounter_Type()
)
npIoPulseCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoPulseCounter.setStatus("current")


class _NpIoSinglePulseDuration_Type(Integer32):
    """Custom type npIoSinglePulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 25500),
    )


_NpIoSinglePulseDuration_Type.__name__ = "Integer32"
_NpIoSinglePulseDuration_Object = MibTableColumn
npIoSinglePulseDuration = _NpIoSinglePulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12),
    _NpIoSinglePulseDuration_Type()
)
npIoSinglePulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseDuration.setStatus("current")
_NpIoSinglePulseStart_Type = Integer32
_NpIoSinglePulseStart_Object = MibTableColumn
npIoSinglePulseStart = _NpIoSinglePulseStart_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13),
    _NpIoSinglePulseStart_Type()
)
npIoSinglePulseStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseStart.setStatus("current")
_NpIoTraps_ObjectIdentity = ObjectIdentity
npIoTraps = _NpIoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2)
)
_NpIoTrapPrefix_ObjectIdentity = ObjectIdentity
npIoTrapPrefix = _NpIoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0)
)


class _NpIoTrapLineN_Type(Integer32):
    """Custom type npIoTrapLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpIoTrapLineN_Type.__name__ = "Integer32"
_NpIoTrapLineN_Object = MibScalar
npIoTrapLineN = _NpIoTrapLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1),
    _NpIoTrapLineN_Type()
)
npIoTrapLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLineN.setStatus("current")


class _NpIoTrapLevelIn_Type(Integer32):
    """Custom type npIoTrapLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn_Type.__name__ = "Integer32"
_NpIoTrapLevelIn_Object = MibScalar
npIoTrapLevelIn = _NpIoTrapLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2),
    _NpIoTrapLevelIn_Type()
)
npIoTrapLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn.setStatus("current")
_NpIoTrapMemo_Type = DisplayString
_NpIoTrapMemo_Object = MibScalar
npIoTrapMemo = _NpIoTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6),
    _NpIoTrapMemo_Type()
)
npIoTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapMemo.setStatus("current")


class _NpIoTrapLevelIn1_Type(Integer32):
    """Custom type npIoTrapLevelIn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn1_Type.__name__ = "Integer32"
_NpIoTrapLevelIn1_Object = MibScalar
npIoTrapLevelIn1 = _NpIoTrapLevelIn1_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 21),
    _NpIoTrapLevelIn1_Type()
)
npIoTrapLevelIn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn1.setStatus("current")


class _NpIoTrapLevelIn2_Type(Integer32):
    """Custom type npIoTrapLevelIn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn2_Type.__name__ = "Integer32"
_NpIoTrapLevelIn2_Object = MibScalar
npIoTrapLevelIn2 = _NpIoTrapLevelIn2_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 22),
    _NpIoTrapLevelIn2_Type()
)
npIoTrapLevelIn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn2.setStatus("current")


class _NpIoTrapLevelIn3_Type(Integer32):
    """Custom type npIoTrapLevelIn3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn3_Type.__name__ = "Integer32"
_NpIoTrapLevelIn3_Object = MibScalar
npIoTrapLevelIn3 = _NpIoTrapLevelIn3_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 23),
    _NpIoTrapLevelIn3_Type()
)
npIoTrapLevelIn3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn3.setStatus("current")


class _NpIoTrapLevelIn4_Type(Integer32):
    """Custom type npIoTrapLevelIn4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn4_Type.__name__ = "Integer32"
_NpIoTrapLevelIn4_Object = MibScalar
npIoTrapLevelIn4 = _NpIoTrapLevelIn4_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 24),
    _NpIoTrapLevelIn4_Type()
)
npIoTrapLevelIn4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn4.setStatus("current")
_NpElecMeter_ObjectIdentity = ObjectIdentity
npElecMeter = _NpElecMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 9700)
)
_NpElecTable_Object = MibTable
npElecTable = _NpElecTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9700, 1)
)
if mibBuilder.loadTexts:
    npElecTable.setStatus("current")
_NpElecEntry_Object = MibTableRow
npElecEntry = _NpElecEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1)
)
npElecEntry.setIndexNames(
    (0, "DKSF-253-5-X-A-X", "npElecIndex"),
)
if mibBuilder.loadTexts:
    npElecEntry.setStatus("current")


class _NpElecIndex_Type(Integer32):
    """Custom type npElecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NpElecIndex_Type.__name__ = "Integer32"
_NpElecIndex_Object = MibTableColumn
npElecIndex = _NpElecIndex_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 1),
    _NpElecIndex_Type()
)
npElecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npElecIndex.setStatus("current")
_NpElecPulsesPerKwh_Type = Integer32
_NpElecPulsesPerKwh_Object = MibTableColumn
npElecPulsesPerKwh = _NpElecPulsesPerKwh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 2),
    _NpElecPulsesPerKwh_Type()
)
npElecPulsesPerKwh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npElecPulsesPerKwh.setStatus("current")
_NpElecPower_Type = Gauge32
_NpElecPower_Object = MibTableColumn
npElecPower = _NpElecPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 3),
    _NpElecPower_Type()
)
npElecPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npElecPower.setStatus("current")
_NpElecEnergy_Type = Counter32
_NpElecEnergy_Object = MibTableColumn
npElecEnergy = _NpElecEnergy_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 4),
    _NpElecEnergy_Type()
)
npElecEnergy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npElecEnergy.setStatus("current")
_NpElecEnergy100_Type = Counter32
_NpElecEnergy100_Object = MibTableColumn
npElecEnergy100 = _NpElecEnergy100_Object(
    (1, 3, 6, 1, 4, 1, 25728, 9700, 1, 1, 5),
    _NpElecEnergy100_Type()
)
npElecEnergy100.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npElecEnergy100.setStatus("current")

# Managed Objects groups


# Notification objects

npIoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)
)
npIoTrap.setObjects(
      *(("DKSF-253-5-X-A-X", "npIoTrapLineN"),
        ("DKSF-253-5-X-A-X", "npIoTrapLevelIn"),
        ("DKSF-253-5-X-A-X", "npIoTrapMemo"),
        ("DKSF-253-5-X-A-X", "npIoTrapLevelIn1"),
        ("DKSF-253-5-X-A-X", "npIoTrapLevelIn2"),
        ("DKSF-253-5-X-A-X", "npIoTrapLevelIn3"),
        ("DKSF-253-5-X-A-X", "npIoTrapLevelIn4"))
)
if mibBuilder.loadTexts:
    npIoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKSF-253-5-X-A-X",
    **{"lightcom": lightcom,
       "netPing": netPing,
       "npReboot": npReboot,
       "npSoftReboot": npSoftReboot,
       "npResetStack": npResetStack,
       "npForcedReboot": npForcedReboot,
       "npIo": npIo,
       "npIoTable": npIoTable,
       "npIoEntry": npIoEntry,
       "npIoLineN": npIoLineN,
       "npIoLevelIn": npIoLevelIn,
       "npIoLevelOut": npIoLevelOut,
       "npIoMemo": npIoMemo,
       "npIoPulseCounter": npIoPulseCounter,
       "npIoSinglePulseDuration": npIoSinglePulseDuration,
       "npIoSinglePulseStart": npIoSinglePulseStart,
       "npIoTraps": npIoTraps,
       "npIoTrapPrefix": npIoTrapPrefix,
       "npIoTrap": npIoTrap,
       "npIoTrapLineN": npIoTrapLineN,
       "npIoTrapLevelIn": npIoTrapLevelIn,
       "npIoTrapMemo": npIoTrapMemo,
       "npIoTrapLevelIn1": npIoTrapLevelIn1,
       "npIoTrapLevelIn2": npIoTrapLevelIn2,
       "npIoTrapLevelIn3": npIoTrapLevelIn3,
       "npIoTrapLevelIn4": npIoTrapLevelIn4,
       "npElecMeter": npElecMeter,
       "npElecTable": npElecTable,
       "npElecEntry": npElecEntry,
       "npElecIndex": npElecIndex,
       "npElecPulsesPerKwh": npElecPulsesPerKwh,
       "npElecPower": npElecPower,
       "npElecEnergy": npElecEnergy,
       "npElecEnergy100": npElecEnergy100}
)
