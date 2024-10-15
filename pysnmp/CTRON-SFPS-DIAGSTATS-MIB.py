# SNMP MIB module (CTRON-SFPS-DIAGSTATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-DIAGSTATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:21 2024
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

(sfpsFloodCounters,
 sfpsFloodCountersReset,
 sfpsIsolatedSwitch,
 sfpsResetNVRAM) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsFloodCounters",
    "sfpsFloodCountersReset",
    "sfpsIsolatedSwitch",
    "sfpsResetNVRAM")

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


# MODULE-IDENTITY


# Types definitions



class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsFloodCountersTable_Object = MibTable
sfpsFloodCountersTable = _SfpsFloodCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsFloodCountersTable.setStatus("mandatory")
_SfpsFloodCountersEntry_Object = MibTableRow
sfpsFloodCountersEntry = _SfpsFloodCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1)
)
sfpsFloodCountersEntry.setIndexNames(
    (0, "CTRON-SFPS-DIAGSTATS-MIB", "sfpsFloodCountersSource"),
)
if mibBuilder.loadTexts:
    sfpsFloodCountersEntry.setStatus("mandatory")
_SfpsFloodCountersSource_Type = SfpsAddress
_SfpsFloodCountersSource_Object = MibTableColumn
sfpsFloodCountersSource = _SfpsFloodCountersSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 1),
    _SfpsFloodCountersSource_Type()
)
sfpsFloodCountersSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersSource.setStatus("mandatory")
_SfpsFloodCountersNumFloods_Type = Integer32
_SfpsFloodCountersNumFloods_Object = MibTableColumn
sfpsFloodCountersNumFloods = _SfpsFloodCountersNumFloods_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 2),
    _SfpsFloodCountersNumFloods_Type()
)
sfpsFloodCountersNumFloods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersNumFloods.setStatus("mandatory")
_SfpsFloodCountersLastSeqNum_Type = Integer32
_SfpsFloodCountersLastSeqNum_Object = MibTableColumn
sfpsFloodCountersLastSeqNum = _SfpsFloodCountersLastSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 3),
    _SfpsFloodCountersLastSeqNum_Type()
)
sfpsFloodCountersLastSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersLastSeqNum.setStatus("mandatory")
_SfpsFloodCountersNumDrops_Type = Integer32
_SfpsFloodCountersNumDrops_Object = MibTableColumn
sfpsFloodCountersNumDrops = _SfpsFloodCountersNumDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 4),
    _SfpsFloodCountersNumDrops_Type()
)
sfpsFloodCountersNumDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersNumDrops.setStatus("mandatory")
_SfpsFloodCountersLastDropTime_Type = TimeTicks
_SfpsFloodCountersLastDropTime_Object = MibTableColumn
sfpsFloodCountersLastDropTime = _SfpsFloodCountersLastDropTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 5),
    _SfpsFloodCountersLastDropTime_Type()
)
sfpsFloodCountersLastDropTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersLastDropTime.setStatus("mandatory")
_SfpsFloodCountersMaxDrops_Type = Integer32
_SfpsFloodCountersMaxDrops_Object = MibTableColumn
sfpsFloodCountersMaxDrops = _SfpsFloodCountersMaxDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 6),
    _SfpsFloodCountersMaxDrops_Type()
)
sfpsFloodCountersMaxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersMaxDrops.setStatus("mandatory")
_SfpsFloodCountersMaxDropsTime_Type = TimeTicks
_SfpsFloodCountersMaxDropsTime_Object = MibTableColumn
sfpsFloodCountersMaxDropsTime = _SfpsFloodCountersMaxDropsTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 1, 1, 1, 7),
    _SfpsFloodCountersMaxDropsTime_Type()
)
sfpsFloodCountersMaxDropsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersMaxDropsTime.setStatus("mandatory")
_SfpsFloodCountersResetReset_Type = Integer32
_SfpsFloodCountersResetReset_Object = MibScalar
sfpsFloodCountersResetReset = _SfpsFloodCountersResetReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 1),
    _SfpsFloodCountersResetReset_Type()
)
sfpsFloodCountersResetReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsFloodCountersResetReset.setStatus("mandatory")
_SfpsFloodCountersTotalDropped_Type = Integer32
_SfpsFloodCountersTotalDropped_Object = MibScalar
sfpsFloodCountersTotalDropped = _SfpsFloodCountersTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 2),
    _SfpsFloodCountersTotalDropped_Type()
)
sfpsFloodCountersTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersTotalDropped.setStatus("mandatory")
_SfpsFloodCountersTotalRunts_Type = Integer32
_SfpsFloodCountersTotalRunts_Object = MibScalar
sfpsFloodCountersTotalRunts = _SfpsFloodCountersTotalRunts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 3),
    _SfpsFloodCountersTotalRunts_Type()
)
sfpsFloodCountersTotalRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersTotalRunts.setStatus("mandatory")
_SfpsFloodCountersTotalSelfOrig_Type = Integer32
_SfpsFloodCountersTotalSelfOrig_Object = MibScalar
sfpsFloodCountersTotalSelfOrig = _SfpsFloodCountersTotalSelfOrig_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 4),
    _SfpsFloodCountersTotalSelfOrig_Type()
)
sfpsFloodCountersTotalSelfOrig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersTotalSelfOrig.setStatus("mandatory")
_SfpsFloodCountersNonNetPort_Type = Integer32
_SfpsFloodCountersNonNetPort_Object = MibScalar
sfpsFloodCountersNonNetPort = _SfpsFloodCountersNonNetPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 2, 5),
    _SfpsFloodCountersNonNetPort_Type()
)
sfpsFloodCountersNonNetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsFloodCountersNonNetPort.setStatus("mandatory")


class _SfpsIsolatedSwitchIsolatedSwitch_Type(Integer32):
    """Custom type sfpsIsolatedSwitchIsolatedSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_SfpsIsolatedSwitchIsolatedSwitch_Type.__name__ = "Integer32"
_SfpsIsolatedSwitchIsolatedSwitch_Object = MibScalar
sfpsIsolatedSwitchIsolatedSwitch = _SfpsIsolatedSwitchIsolatedSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 1),
    _SfpsIsolatedSwitchIsolatedSwitch_Type()
)
sfpsIsolatedSwitchIsolatedSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIsolatedSwitchIsolatedSwitch.setStatus("mandatory")
_SfpsIsolatedSwitchResetCounters_Type = Integer32
_SfpsIsolatedSwitchResetCounters_Object = MibScalar
sfpsIsolatedSwitchResetCounters = _SfpsIsolatedSwitchResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 2),
    _SfpsIsolatedSwitchResetCounters_Type()
)
sfpsIsolatedSwitchResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsIsolatedSwitchResetCounters.setStatus("mandatory")
_SfpsIsolatedSwitchINBDropped_Type = Integer32
_SfpsIsolatedSwitchINBDropped_Object = MibScalar
sfpsIsolatedSwitchINBDropped = _SfpsIsolatedSwitchINBDropped_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 3),
    _SfpsIsolatedSwitchINBDropped_Type()
)
sfpsIsolatedSwitchINBDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIsolatedSwitchINBDropped.setStatus("mandatory")
_SfpsIsolatedSwitchINBNotSent_Type = Integer32
_SfpsIsolatedSwitchINBNotSent_Object = MibScalar
sfpsIsolatedSwitchINBNotSent = _SfpsIsolatedSwitchINBNotSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 2, 5, 4),
    _SfpsIsolatedSwitchINBNotSent_Type()
)
sfpsIsolatedSwitchINBNotSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsIsolatedSwitchINBNotSent.setStatus("mandatory")
_SfpsResetNVRAMPercentNvramAvailable_Type = Integer32
_SfpsResetNVRAMPercentNvramAvailable_Object = MibScalar
sfpsResetNVRAMPercentNvramAvailable = _SfpsResetNVRAMPercentNvramAvailable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 1),
    _SfpsResetNVRAMPercentNvramAvailable_Type()
)
sfpsResetNVRAMPercentNvramAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResetNVRAMPercentNvramAvailable.setStatus("mandatory")
_SfpsResetNVRAMTotalNVRAM_Type = Integer32
_SfpsResetNVRAMTotalNVRAM_Object = MibScalar
sfpsResetNVRAMTotalNVRAM = _SfpsResetNVRAMTotalNVRAM_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 2),
    _SfpsResetNVRAMTotalNVRAM_Type()
)
sfpsResetNVRAMTotalNVRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsResetNVRAMTotalNVRAM.setStatus("mandatory")
_SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Type = Integer32
_SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Object = MibScalar
sfpsResetNVRAMOnetoResetNvramAndRestoreIP = _SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 3),
    _SfpsResetNVRAMOnetoResetNvramAndRestoreIP_Type()
)
sfpsResetNVRAMOnetoResetNvramAndRestoreIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResetNVRAMOnetoResetNvramAndRestoreIP.setStatus("mandatory")
_SfpsResetNVRAMDelayTimer_Type = Integer32
_SfpsResetNVRAMDelayTimer_Object = MibScalar
sfpsResetNVRAMDelayTimer = _SfpsResetNVRAMDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 3, 4),
    _SfpsResetNVRAMDelayTimer_Type()
)
sfpsResetNVRAMDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsResetNVRAMDelayTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-DIAGSTATS-MIB",
    **{"SfpsAddress": SfpsAddress,
       "sfpsFloodCountersTable": sfpsFloodCountersTable,
       "sfpsFloodCountersEntry": sfpsFloodCountersEntry,
       "sfpsFloodCountersSource": sfpsFloodCountersSource,
       "sfpsFloodCountersNumFloods": sfpsFloodCountersNumFloods,
       "sfpsFloodCountersLastSeqNum": sfpsFloodCountersLastSeqNum,
       "sfpsFloodCountersNumDrops": sfpsFloodCountersNumDrops,
       "sfpsFloodCountersLastDropTime": sfpsFloodCountersLastDropTime,
       "sfpsFloodCountersMaxDrops": sfpsFloodCountersMaxDrops,
       "sfpsFloodCountersMaxDropsTime": sfpsFloodCountersMaxDropsTime,
       "sfpsFloodCountersResetReset": sfpsFloodCountersResetReset,
       "sfpsFloodCountersTotalDropped": sfpsFloodCountersTotalDropped,
       "sfpsFloodCountersTotalRunts": sfpsFloodCountersTotalRunts,
       "sfpsFloodCountersTotalSelfOrig": sfpsFloodCountersTotalSelfOrig,
       "sfpsFloodCountersNonNetPort": sfpsFloodCountersNonNetPort,
       "sfpsIsolatedSwitchIsolatedSwitch": sfpsIsolatedSwitchIsolatedSwitch,
       "sfpsIsolatedSwitchResetCounters": sfpsIsolatedSwitchResetCounters,
       "sfpsIsolatedSwitchINBDropped": sfpsIsolatedSwitchINBDropped,
       "sfpsIsolatedSwitchINBNotSent": sfpsIsolatedSwitchINBNotSent,
       "sfpsResetNVRAMPercentNvramAvailable": sfpsResetNVRAMPercentNvramAvailable,
       "sfpsResetNVRAMTotalNVRAM": sfpsResetNVRAMTotalNVRAM,
       "sfpsResetNVRAMOnetoResetNvramAndRestoreIP": sfpsResetNVRAMOnetoResetNvramAndRestoreIP,
       "sfpsResetNVRAMDelayTimer": sfpsResetNVRAMDelayTimer}
)
