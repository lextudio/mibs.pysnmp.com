# SNMP MIB module (ASCEND-WATCHDOG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-WATCHDOG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:45 2024
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

(slots,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "slots")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Watchdog_ObjectIdentity = ObjectIdentity
watchdog = _Watchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 2, 7)
)
_WatchdogCount_Type = Integer32
_WatchdogCount_Object = MibScalar
watchdogCount = _WatchdogCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 1),
    _WatchdogCount_Type()
)
watchdogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogCount.setStatus("mandatory")
_WatchdogTable_Object = MibTable
watchdogTable = _WatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2)
)
if mibBuilder.loadTexts:
    watchdogTable.setStatus("mandatory")
_WatchdogEntry_Object = MibTableRow
watchdogEntry = _WatchdogEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1)
)
watchdogEntry.setIndexNames(
    (0, "ASCEND-WATCHDOG-MIB", "watchdogIndex"),
)
if mibBuilder.loadTexts:
    watchdogEntry.setStatus("mandatory")
_WatchdogIndex_Type = Integer32
_WatchdogIndex_Object = MibTableColumn
watchdogIndex = _WatchdogIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 1),
    _WatchdogIndex_Type()
)
watchdogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogIndex.setStatus("mandatory")
_WatchdogName_Type = DisplayString
_WatchdogName_Object = MibTableColumn
watchdogName = _WatchdogName_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 2),
    _WatchdogName_Type()
)
watchdogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogName.setStatus("mandatory")


class _WatchdogID_Type(Integer32):
    """Custom type watchdogID based on Integer32"""
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
        *(("fan", 3),
          ("fantray", 4),
          ("other", 1),
          ("thermal", 2))
    )


_WatchdogID_Type.__name__ = "Integer32"
_WatchdogID_Object = MibTableColumn
watchdogID = _WatchdogID_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 3),
    _WatchdogID_Type()
)
watchdogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogID.setStatus("mandatory")


class _WatchdogState_Type(Integer32):
    """Custom type watchdogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("operational", 2),
          ("other", 1))
    )


_WatchdogState_Type.__name__ = "Integer32"
_WatchdogState_Object = MibTableColumn
watchdogState = _WatchdogState_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 4),
    _WatchdogState_Type()
)
watchdogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogState.setStatus("mandatory")
_WatchdogReading_Type = Integer32
_WatchdogReading_Object = MibTableColumn
watchdogReading = _WatchdogReading_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 5),
    _WatchdogReading_Type()
)
watchdogReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogReading.setStatus("mandatory")
_WatchdogLastViolation_Type = TimeTicks
_WatchdogLastViolation_Object = MibTableColumn
watchdogLastViolation = _WatchdogLastViolation_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 6),
    _WatchdogLastViolation_Type()
)
watchdogLastViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogLastViolation.setStatus("mandatory")
_WatchdogLocation_Type = DisplayString
_WatchdogLocation_Object = MibTableColumn
watchdogLocation = _WatchdogLocation_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 7),
    _WatchdogLocation_Type()
)
watchdogLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogLocation.setStatus("mandatory")
_WatchdogUnit_Type = Integer32
_WatchdogUnit_Object = MibTableColumn
watchdogUnit = _WatchdogUnit_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 8),
    _WatchdogUnit_Type()
)
watchdogUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogUnit.setStatus("mandatory")


class _WatchdogReadingUnits_Type(Integer32):
    """Custom type watchdogReadingUnits based on Integer32"""
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
        *(("celsius", 2),
          ("noReadingSupported", 4),
          ("other", 1),
          ("rpm", 3))
    )


_WatchdogReadingUnits_Type.__name__ = "Integer32"
_WatchdogReadingUnits_Object = MibTableColumn
watchdogReadingUnits = _WatchdogReadingUnits_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 9),
    _WatchdogReadingUnits_Type()
)
watchdogReadingUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogReadingUnits.setStatus("mandatory")
_WatchdogThreshold_Type = Integer32
_WatchdogThreshold_Object = MibTableColumn
watchdogThreshold = _WatchdogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 2, 1, 10),
    _WatchdogThreshold_Type()
)
watchdogThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchdogThreshold.setStatus("mandatory")


class _WatchdogTrapState_Type(Integer32):
    """Custom type watchdogTrapState based on Integer32"""
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


_WatchdogTrapState_Type.__name__ = "Integer32"
_WatchdogTrapState_Object = MibScalar
watchdogTrapState = _WatchdogTrapState_Object(
    (1, 3, 6, 1, 4, 1, 529, 2, 7, 3),
    _WatchdogTrapState_Type()
)
watchdogTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdogTrapState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-WATCHDOG-MIB",
    **{"watchdog": watchdog,
       "watchdogCount": watchdogCount,
       "watchdogTable": watchdogTable,
       "watchdogEntry": watchdogEntry,
       "watchdogIndex": watchdogIndex,
       "watchdogName": watchdogName,
       "watchdogID": watchdogID,
       "watchdogState": watchdogState,
       "watchdogReading": watchdogReading,
       "watchdogLastViolation": watchdogLastViolation,
       "watchdogLocation": watchdogLocation,
       "watchdogUnit": watchdogUnit,
       "watchdogReadingUnits": watchdogReadingUnits,
       "watchdogThreshold": watchdogThreshold,
       "watchdogTrapState": watchdogTrapState}
)
