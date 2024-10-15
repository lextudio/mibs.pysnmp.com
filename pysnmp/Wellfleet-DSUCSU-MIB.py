# SNMP MIB module (Wellfleet-DSUCSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DSUCSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:08 2024
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

(wfDsuCsuGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDsuCsuGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDsuCsuIfTable_Object = MibTable
wfDsuCsuIfTable = _WfDsuCsuIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1)
)
if mibBuilder.loadTexts:
    wfDsuCsuIfTable.setStatus("mandatory")
_WfDsuCsuIfEntry_Object = MibTableRow
wfDsuCsuIfEntry = _WfDsuCsuIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1)
)
wfDsuCsuIfEntry.setIndexNames(
    (0, "Wellfleet-DSUCSU-MIB", "wfDsuCsuIfSlot"),
    (0, "Wellfleet-DSUCSU-MIB", "wfDsuCsuIfConnector"),
)
if mibBuilder.loadTexts:
    wfDsuCsuIfEntry.setStatus("mandatory")


class _WfDsuCsuIfDelete_Type(Integer32):
    """Custom type wfDsuCsuIfDelete based on Integer32"""
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


_WfDsuCsuIfDelete_Type.__name__ = "Integer32"
_WfDsuCsuIfDelete_Object = MibTableColumn
wfDsuCsuIfDelete = _WfDsuCsuIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 1),
    _WfDsuCsuIfDelete_Type()
)
wfDsuCsuIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuIfDelete.setStatus("mandatory")
_WfDsuCsuIfSlot_Type = Integer32
_WfDsuCsuIfSlot_Object = MibTableColumn
wfDsuCsuIfSlot = _WfDsuCsuIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 2),
    _WfDsuCsuIfSlot_Type()
)
wfDsuCsuIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuIfSlot.setStatus("mandatory")
_WfDsuCsuIfConnector_Type = Integer32
_WfDsuCsuIfConnector_Object = MibTableColumn
wfDsuCsuIfConnector = _WfDsuCsuIfConnector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 3),
    _WfDsuCsuIfConnector_Type()
)
wfDsuCsuIfConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuIfConnector.setStatus("mandatory")


class _WfDsuCsuSoftRev_Type(DisplayString):
    """Custom type wfDsuCsuSoftRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_WfDsuCsuSoftRev_Type.__name__ = "DisplayString"
_WfDsuCsuSoftRev_Object = MibTableColumn
wfDsuCsuSoftRev = _WfDsuCsuSoftRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 4),
    _WfDsuCsuSoftRev_Type()
)
wfDsuCsuSoftRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuSoftRev.setStatus("mandatory")


class _WfDsuCsuHardRev_Type(DisplayString):
    """Custom type wfDsuCsuHardRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_WfDsuCsuHardRev_Type.__name__ = "DisplayString"
_WfDsuCsuHardRev_Object = MibTableColumn
wfDsuCsuHardRev = _WfDsuCsuHardRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 5),
    _WfDsuCsuHardRev_Type()
)
wfDsuCsuHardRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuHardRev.setStatus("mandatory")


class _WfDsuCsuOpMode_Type(Integer32):
    """Custom type wfDsuCsuOpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cc64kbps", 2),
          ("dds156kbps", 1))
    )


_WfDsuCsuOpMode_Type.__name__ = "Integer32"
_WfDsuCsuOpMode_Object = MibTableColumn
wfDsuCsuOpMode = _WfDsuCsuOpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 6),
    _WfDsuCsuOpMode_Type()
)
wfDsuCsuOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuOpMode.setStatus("mandatory")


class _WfDsuCsuTxClkSelect_Type(Integer32):
    """Custom type wfDsuCsuTxClkSelect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_WfDsuCsuTxClkSelect_Type.__name__ = "Integer32"
_WfDsuCsuTxClkSelect_Object = MibTableColumn
wfDsuCsuTxClkSelect = _WfDsuCsuTxClkSelect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 7),
    _WfDsuCsuTxClkSelect_Type()
)
wfDsuCsuTxClkSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuTxClkSelect.setStatus("mandatory")


class _WfDsuCsuUnitReset_Type(Integer32):
    """Custom type wfDsuCsuUnitReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetUnit", 1)
    )


_WfDsuCsuUnitReset_Type.__name__ = "Integer32"
_WfDsuCsuUnitReset_Object = MibTableColumn
wfDsuCsuUnitReset = _WfDsuCsuUnitReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 8),
    _WfDsuCsuUnitReset_Type()
)
wfDsuCsuUnitReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuUnitReset.setStatus("mandatory")


class _WfDsuCsu64KTxMonitor_Type(Integer32):
    """Custom type wfDsuCsu64KTxMonitor based on Integer32"""
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


_WfDsuCsu64KTxMonitor_Type.__name__ = "Integer32"
_WfDsuCsu64KTxMonitor_Object = MibTableColumn
wfDsuCsu64KTxMonitor = _WfDsuCsu64KTxMonitor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 9),
    _WfDsuCsu64KTxMonitor_Type()
)
wfDsuCsu64KTxMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsu64KTxMonitor.setStatus("mandatory")


class _WfDsuCsuOpState_Type(Integer32):
    """Custom type wfDsuCsuOpState based on Integer32"""
    defaultValue = 1

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
        *(("digitalLpbk", 3),
          ("localAnlgLpbkWPattern", 7),
          ("localLpbk", 2),
          ("normal", 1),
          ("pattern2047Gen", 8),
          ("remDigLpbkWPattern", 6),
          ("remDigitalLpbk", 4),
          ("telcoLpbk", 5))
    )


_WfDsuCsuOpState_Type.__name__ = "Integer32"
_WfDsuCsuOpState_Object = MibTableColumn
wfDsuCsuOpState = _WfDsuCsuOpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 10),
    _WfDsuCsuOpState_Type()
)
wfDsuCsuOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuOpState.setStatus("mandatory")


class _WfDsuCsuServiceStatus_Type(Integer32):
    """Custom type wfDsuCsuServiceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("frameError", 3),
          ("inService", 1),
          ("lossOfLine", 5),
          ("outOfService", 2),
          ("telcoLpbk", 6))
    )


_WfDsuCsuServiceStatus_Type.__name__ = "Integer32"
_WfDsuCsuServiceStatus_Object = MibTableColumn
wfDsuCsuServiceStatus = _WfDsuCsuServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 11),
    _WfDsuCsuServiceStatus_Type()
)
wfDsuCsuServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuServiceStatus.setStatus("mandatory")


class _WfDsuCsuV54Lpbk_Type(Integer32):
    """Custom type wfDsuCsuV54Lpbk based on Integer32"""
    defaultValue = 1

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
        *(("localAnlgLpbk", 2),
          ("localAnlgLpbkWPattern", 6),
          ("localDigLpbk", 3),
          ("noLoop", 1),
          ("pattern2047Gen", 7),
          ("remDigLpbk", 4),
          ("remDigLpbkWPattern", 5))
    )


_WfDsuCsuV54Lpbk_Type.__name__ = "Integer32"
_WfDsuCsuV54Lpbk_Object = MibTableColumn
wfDsuCsuV54Lpbk = _WfDsuCsuV54Lpbk_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 12),
    _WfDsuCsuV54Lpbk_Type()
)
wfDsuCsuV54Lpbk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuV54Lpbk.setStatus("mandatory")


class _WfDsuCsuV54Timer_Type(Integer32):
    """Custom type wfDsuCsuV54Timer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfDsuCsuV54Timer_Type.__name__ = "Integer32"
_WfDsuCsuV54Timer_Object = MibTableColumn
wfDsuCsuV54Timer = _WfDsuCsuV54Timer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 13),
    _WfDsuCsuV54Timer_Type()
)
wfDsuCsuV54Timer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuV54Timer.setStatus("mandatory")
_WfDsuCsuV54Errors_Type = Counter32
_WfDsuCsuV54Errors_Object = MibTableColumn
wfDsuCsuV54Errors = _WfDsuCsuV54Errors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 14),
    _WfDsuCsuV54Errors_Type()
)
wfDsuCsuV54Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuV54Errors.setStatus("mandatory")


class _WfDsuCsuCqmsLaWindow_Type(Integer32):
    """Custom type wfDsuCsuCqmsLaWindow based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfDsuCsuCqmsLaWindow_Type.__name__ = "Integer32"
_WfDsuCsuCqmsLaWindow_Object = MibTableColumn
wfDsuCsuCqmsLaWindow = _WfDsuCsuCqmsLaWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 15),
    _WfDsuCsuCqmsLaWindow_Type()
)
wfDsuCsuCqmsLaWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuCqmsLaWindow.setStatus("mandatory")
_WfDsuCsuCqmsLaErrors_Type = Counter32
_WfDsuCsuCqmsLaErrors_Object = MibTableColumn
wfDsuCsuCqmsLaErrors = _WfDsuCsuCqmsLaErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 16),
    _WfDsuCsuCqmsLaErrors_Type()
)
wfDsuCsuCqmsLaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuCqmsLaErrors.setStatus("mandatory")


class _WfDsuCsuCqmsLaPollRate_Type(Integer32):
    """Custom type wfDsuCsuCqmsLaPollRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfDsuCsuCqmsLaPollRate_Type.__name__ = "Integer32"
_WfDsuCsuCqmsLaPollRate_Object = MibTableColumn
wfDsuCsuCqmsLaPollRate = _WfDsuCsuCqmsLaPollRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 17),
    _WfDsuCsuCqmsLaPollRate_Type()
)
wfDsuCsuCqmsLaPollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuCqmsLaPollRate.setStatus("mandatory")


class _WfDsuCsuCqmsReset_Type(Integer32):
    """Custom type wfDsuCsuCqmsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCqms", 1)
    )


_WfDsuCsuCqmsReset_Type.__name__ = "Integer32"
_WfDsuCsuCqmsReset_Object = MibTableColumn
wfDsuCsuCqmsReset = _WfDsuCsuCqmsReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 18),
    _WfDsuCsuCqmsReset_Type()
)
wfDsuCsuCqmsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDsuCsuCqmsReset.setStatus("mandatory")
_WfDsuCsuOOSErrors_Type = Counter32
_WfDsuCsuOOSErrors_Object = MibTableColumn
wfDsuCsuOOSErrors = _WfDsuCsuOOSErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 19),
    _WfDsuCsuOOSErrors_Type()
)
wfDsuCsuOOSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuOOSErrors.setStatus("mandatory")
_WfDsuCsuFrameErrors_Type = Counter32
_WfDsuCsuFrameErrors_Object = MibTableColumn
wfDsuCsuFrameErrors = _WfDsuCsuFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 20),
    _WfDsuCsuFrameErrors_Type()
)
wfDsuCsuFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuFrameErrors.setStatus("mandatory")
_WfDsuCsuLOLErrors_Type = Counter32
_WfDsuCsuLOLErrors_Object = MibTableColumn
wfDsuCsuLOLErrors = _WfDsuCsuLOLErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 21),
    _WfDsuCsuLOLErrors_Type()
)
wfDsuCsuLOLErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuLOLErrors.setStatus("mandatory")


class _WfDsuCsuInitState_Type(Integer32):
    """Custom type wfDsuCsuInitState based on Integer32"""
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
        *(("init", 2),
          ("loopback", 4),
          ("monitor", 3),
          ("startup", 1))
    )


_WfDsuCsuInitState_Type.__name__ = "Integer32"
_WfDsuCsuInitState_Object = MibTableColumn
wfDsuCsuInitState = _WfDsuCsuInitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 1, 1, 22),
    _WfDsuCsuInitState_Type()
)
wfDsuCsuInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDsuCsuInitState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

wfDsuCsuIfTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 30, 0, 1)
)
wfDsuCsuIfTrap.setObjects(
    ("Wellfleet-DSUCSU-MIB", "wfDsuCsuServiceStatus")
)
if mibBuilder.loadTexts:
    wfDsuCsuIfTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DSUCSU-MIB",
    **{"wfDsuCsuIfTrap": wfDsuCsuIfTrap,
       "wfDsuCsuIfTable": wfDsuCsuIfTable,
       "wfDsuCsuIfEntry": wfDsuCsuIfEntry,
       "wfDsuCsuIfDelete": wfDsuCsuIfDelete,
       "wfDsuCsuIfSlot": wfDsuCsuIfSlot,
       "wfDsuCsuIfConnector": wfDsuCsuIfConnector,
       "wfDsuCsuSoftRev": wfDsuCsuSoftRev,
       "wfDsuCsuHardRev": wfDsuCsuHardRev,
       "wfDsuCsuOpMode": wfDsuCsuOpMode,
       "wfDsuCsuTxClkSelect": wfDsuCsuTxClkSelect,
       "wfDsuCsuUnitReset": wfDsuCsuUnitReset,
       "wfDsuCsu64KTxMonitor": wfDsuCsu64KTxMonitor,
       "wfDsuCsuOpState": wfDsuCsuOpState,
       "wfDsuCsuServiceStatus": wfDsuCsuServiceStatus,
       "wfDsuCsuV54Lpbk": wfDsuCsuV54Lpbk,
       "wfDsuCsuV54Timer": wfDsuCsuV54Timer,
       "wfDsuCsuV54Errors": wfDsuCsuV54Errors,
       "wfDsuCsuCqmsLaWindow": wfDsuCsuCqmsLaWindow,
       "wfDsuCsuCqmsLaErrors": wfDsuCsuCqmsLaErrors,
       "wfDsuCsuCqmsLaPollRate": wfDsuCsuCqmsLaPollRate,
       "wfDsuCsuCqmsReset": wfDsuCsuCqmsReset,
       "wfDsuCsuOOSErrors": wfDsuCsuOOSErrors,
       "wfDsuCsuFrameErrors": wfDsuCsuFrameErrors,
       "wfDsuCsuLOLErrors": wfDsuCsuLOLErrors,
       "wfDsuCsuInitState": wfDsuCsuInitState}
)
