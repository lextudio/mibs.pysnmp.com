# SNMP MIB module (Wellfleet-STA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-STA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:09 2024
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
 Opaque,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt,
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
    "Opaque",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfStaGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfStaGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfSta_ObjectIdentity = ObjectIdentity
wfSta = _WfSta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 1)
)


class _WfStaDisable_Type(Integer32):
    """Custom type wfStaDisable based on Integer32"""
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


_WfStaDisable_Type.__name__ = "Integer32"
_WfStaDisable_Object = MibScalar
wfStaDisable = _WfStaDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 1, 1),
    _WfStaDisable_Type()
)
wfStaDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaDisable.setStatus("mandatory")


class _WfStaPollInterval_Type(Integer32):
    """Custom type wfStaPollInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_WfStaPollInterval_Type.__name__ = "Integer32"
_WfStaPollInterval_Object = MibScalar
wfStaPollInterval = _WfStaPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 1, 2),
    _WfStaPollInterval_Type()
)
wfStaPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaPollInterval.setStatus("mandatory")
_WfStaThresholdTable_Object = MibTable
wfStaThresholdTable = _WfStaThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2)
)
if mibBuilder.loadTexts:
    wfStaThresholdTable.setStatus("mandatory")
_WfStaThresholdEntry_Object = MibTableRow
wfStaThresholdEntry = _WfStaThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1)
)
wfStaThresholdEntry.setIndexNames(
    (0, "Wellfleet-STA-MIB", "wfStaThresholdObject"),
)
if mibBuilder.loadTexts:
    wfStaThresholdEntry.setStatus("mandatory")


class _WfStaThresholdDelete_Type(Integer32):
    """Custom type wfStaThresholdDelete based on Integer32"""
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


_WfStaThresholdDelete_Type.__name__ = "Integer32"
_WfStaThresholdDelete_Object = MibTableColumn
wfStaThresholdDelete = _WfStaThresholdDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 1),
    _WfStaThresholdDelete_Type()
)
wfStaThresholdDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdDelete.setStatus("mandatory")


class _WfStaThresholdDisable_Type(Integer32):
    """Custom type wfStaThresholdDisable based on Integer32"""
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


_WfStaThresholdDisable_Type.__name__ = "Integer32"
_WfStaThresholdDisable_Object = MibTableColumn
wfStaThresholdDisable = _WfStaThresholdDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 2),
    _WfStaThresholdDisable_Type()
)
wfStaThresholdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdDisable.setStatus("mandatory")


class _WfStaThresholdState_Type(Integer32):
    """Custom type wfStaThresholdState based on Integer32"""
    defaultValue = 1

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
        *(("held", 3),
          ("ignored", 2),
          ("invalid", 5),
          ("suspended", 4),
          ("valid", 1))
    )


_WfStaThresholdState_Type.__name__ = "Integer32"
_WfStaThresholdState_Object = MibTableColumn
wfStaThresholdState = _WfStaThresholdState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 3),
    _WfStaThresholdState_Type()
)
wfStaThresholdState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdState.setStatus("mandatory")
_WfStaThresholdObject_Type = ObjectIdentifier
_WfStaThresholdObject_Object = MibTableColumn
wfStaThresholdObject = _WfStaThresholdObject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 4),
    _WfStaThresholdObject_Type()
)
wfStaThresholdObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdObject.setStatus("mandatory")
_WfStaThresholdLowValue_Type = Gauge32
_WfStaThresholdLowValue_Object = MibTableColumn
wfStaThresholdLowValue = _WfStaThresholdLowValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 5),
    _WfStaThresholdLowValue_Type()
)
wfStaThresholdLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdLowValue.setStatus("mandatory")


class _WfStaThresholdLowEventLevel_Type(Integer32):
    """Custom type wfStaThresholdLowEventLevel based on Integer32"""
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
        *(("debug", 3),
          ("info", 2),
          ("warning", 1))
    )


_WfStaThresholdLowEventLevel_Type.__name__ = "Integer32"
_WfStaThresholdLowEventLevel_Object = MibTableColumn
wfStaThresholdLowEventLevel = _WfStaThresholdLowEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 6),
    _WfStaThresholdLowEventLevel_Type()
)
wfStaThresholdLowEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdLowEventLevel.setStatus("mandatory")
_WfStaThresholdMediumValue_Type = Gauge32
_WfStaThresholdMediumValue_Object = MibTableColumn
wfStaThresholdMediumValue = _WfStaThresholdMediumValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 7),
    _WfStaThresholdMediumValue_Type()
)
wfStaThresholdMediumValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdMediumValue.setStatus("mandatory")


class _WfStaThresholdMediumEventLevel_Type(Integer32):
    """Custom type wfStaThresholdMediumEventLevel based on Integer32"""
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
        *(("debug", 3),
          ("info", 2),
          ("warning", 1))
    )


_WfStaThresholdMediumEventLevel_Type.__name__ = "Integer32"
_WfStaThresholdMediumEventLevel_Object = MibTableColumn
wfStaThresholdMediumEventLevel = _WfStaThresholdMediumEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 8),
    _WfStaThresholdMediumEventLevel_Type()
)
wfStaThresholdMediumEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdMediumEventLevel.setStatus("mandatory")
_WfStaThresholdHighValue_Type = Gauge32
_WfStaThresholdHighValue_Object = MibTableColumn
wfStaThresholdHighValue = _WfStaThresholdHighValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 9),
    _WfStaThresholdHighValue_Type()
)
wfStaThresholdHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdHighValue.setStatus("mandatory")


class _WfStaThresholdHighEventLevel_Type(Integer32):
    """Custom type wfStaThresholdHighEventLevel based on Integer32"""
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
        *(("debug", 3),
          ("info", 2),
          ("warning", 1))
    )


_WfStaThresholdHighEventLevel_Type.__name__ = "Integer32"
_WfStaThresholdHighEventLevel_Object = MibTableColumn
wfStaThresholdHighEventLevel = _WfStaThresholdHighEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 10),
    _WfStaThresholdHighEventLevel_Type()
)
wfStaThresholdHighEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdHighEventLevel.setStatus("mandatory")
_WfStaThresholdCurrentValue_Type = Gauge32
_WfStaThresholdCurrentValue_Object = MibTableColumn
wfStaThresholdCurrentValue = _WfStaThresholdCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 11),
    _WfStaThresholdCurrentValue_Type()
)
wfStaThresholdCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdCurrentValue.setStatus("mandatory")


class _WfStaThresholdUnits_Type(Integer32):
    """Custom type wfStaThresholdUnits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("persecond", 2))
    )


_WfStaThresholdUnits_Type.__name__ = "Integer32"
_WfStaThresholdUnits_Object = MibTableColumn
wfStaThresholdUnits = _WfStaThresholdUnits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 12),
    _WfStaThresholdUnits_Type()
)
wfStaThresholdUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdUnits.setStatus("mandatory")


class _WfStaThresholdAction_Type(Integer32):
    """Custom type wfStaThresholdAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("greaterthan", 1),
          ("lessthan", 2))
    )


_WfStaThresholdAction_Type.__name__ = "Integer32"
_WfStaThresholdAction_Object = MibTableColumn
wfStaThresholdAction = _WfStaThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 13),
    _WfStaThresholdAction_Type()
)
wfStaThresholdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdAction.setStatus("mandatory")


class _WfStaThresholdMaxSuccessiveAlarms_Type(Integer32):
    """Custom type wfStaThresholdMaxSuccessiveAlarms based on Integer32"""
    defaultValue = 5


_WfStaThresholdMaxSuccessiveAlarms_Object = MibTableColumn
wfStaThresholdMaxSuccessiveAlarms = _WfStaThresholdMaxSuccessiveAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 14),
    _WfStaThresholdMaxSuccessiveAlarms_Type()
)
wfStaThresholdMaxSuccessiveAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdMaxSuccessiveAlarms.setStatus("mandatory")


class _WfStaThresholdHoldDownIntervals_Type(Integer32):
    """Custom type wfStaThresholdHoldDownIntervals based on Integer32"""
    defaultValue = 1


_WfStaThresholdHoldDownIntervals_Object = MibTableColumn
wfStaThresholdHoldDownIntervals = _WfStaThresholdHoldDownIntervals_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 15),
    _WfStaThresholdHoldDownIntervals_Type()
)
wfStaThresholdHoldDownIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdHoldDownIntervals.setStatus("mandatory")
_WfStaThresholdLowExceptions_Type = Counter32
_WfStaThresholdLowExceptions_Object = MibTableColumn
wfStaThresholdLowExceptions = _WfStaThresholdLowExceptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 16),
    _WfStaThresholdLowExceptions_Type()
)
wfStaThresholdLowExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdLowExceptions.setStatus("mandatory")
_WfStaThresholdLowAlarms_Type = Counter32
_WfStaThresholdLowAlarms_Object = MibTableColumn
wfStaThresholdLowAlarms = _WfStaThresholdLowAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 17),
    _WfStaThresholdLowAlarms_Type()
)
wfStaThresholdLowAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdLowAlarms.setStatus("mandatory")
_WfStaThresholdMediumExceptions_Type = Counter32
_WfStaThresholdMediumExceptions_Object = MibTableColumn
wfStaThresholdMediumExceptions = _WfStaThresholdMediumExceptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 18),
    _WfStaThresholdMediumExceptions_Type()
)
wfStaThresholdMediumExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdMediumExceptions.setStatus("mandatory")
_WfStaThresholdMediumAlarms_Type = Counter32
_WfStaThresholdMediumAlarms_Object = MibTableColumn
wfStaThresholdMediumAlarms = _WfStaThresholdMediumAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 19),
    _WfStaThresholdMediumAlarms_Type()
)
wfStaThresholdMediumAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdMediumAlarms.setStatus("mandatory")
_WfStaThresholdHighExceptions_Type = Counter32
_WfStaThresholdHighExceptions_Object = MibTableColumn
wfStaThresholdHighExceptions = _WfStaThresholdHighExceptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 20),
    _WfStaThresholdHighExceptions_Type()
)
wfStaThresholdHighExceptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdHighExceptions.setStatus("mandatory")
_WfStaThresholdHighAlarms_Type = Counter32
_WfStaThresholdHighAlarms_Object = MibTableColumn
wfStaThresholdHighAlarms = _WfStaThresholdHighAlarms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 21),
    _WfStaThresholdHighAlarms_Type()
)
wfStaThresholdHighAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfStaThresholdHighAlarms.setStatus("mandatory")
_WfStaThresholdLabel_Type = DisplayString
_WfStaThresholdLabel_Object = MibTableColumn
wfStaThresholdLabel = _WfStaThresholdLabel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 6, 2, 1, 22),
    _WfStaThresholdLabel_Type()
)
wfStaThresholdLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStaThresholdLabel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-STA-MIB",
    **{"wfSta": wfSta,
       "wfStaDisable": wfStaDisable,
       "wfStaPollInterval": wfStaPollInterval,
       "wfStaThresholdTable": wfStaThresholdTable,
       "wfStaThresholdEntry": wfStaThresholdEntry,
       "wfStaThresholdDelete": wfStaThresholdDelete,
       "wfStaThresholdDisable": wfStaThresholdDisable,
       "wfStaThresholdState": wfStaThresholdState,
       "wfStaThresholdObject": wfStaThresholdObject,
       "wfStaThresholdLowValue": wfStaThresholdLowValue,
       "wfStaThresholdLowEventLevel": wfStaThresholdLowEventLevel,
       "wfStaThresholdMediumValue": wfStaThresholdMediumValue,
       "wfStaThresholdMediumEventLevel": wfStaThresholdMediumEventLevel,
       "wfStaThresholdHighValue": wfStaThresholdHighValue,
       "wfStaThresholdHighEventLevel": wfStaThresholdHighEventLevel,
       "wfStaThresholdCurrentValue": wfStaThresholdCurrentValue,
       "wfStaThresholdUnits": wfStaThresholdUnits,
       "wfStaThresholdAction": wfStaThresholdAction,
       "wfStaThresholdMaxSuccessiveAlarms": wfStaThresholdMaxSuccessiveAlarms,
       "wfStaThresholdHoldDownIntervals": wfStaThresholdHoldDownIntervals,
       "wfStaThresholdLowExceptions": wfStaThresholdLowExceptions,
       "wfStaThresholdLowAlarms": wfStaThresholdLowAlarms,
       "wfStaThresholdMediumExceptions": wfStaThresholdMediumExceptions,
       "wfStaThresholdMediumAlarms": wfStaThresholdMediumAlarms,
       "wfStaThresholdHighExceptions": wfStaThresholdHighExceptions,
       "wfStaThresholdHighAlarms": wfStaThresholdHighAlarms,
       "wfStaThresholdLabel": wfStaThresholdLabel}
)
