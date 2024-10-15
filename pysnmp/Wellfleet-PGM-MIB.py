# SNMP MIB module (Wellfleet-PGM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-PGM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:53 2024
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

(wfPgmGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfPgmGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfPgm_ObjectIdentity = ObjectIdentity
wfPgm = _WfPgm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1)
)


class _WfPgmCreate_Type(Integer32):
    """Custom type wfPgmCreate based on Integer32"""
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


_WfPgmCreate_Type.__name__ = "Integer32"
_WfPgmCreate_Object = MibScalar
wfPgmCreate = _WfPgmCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 1),
    _WfPgmCreate_Type()
)
wfPgmCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmCreate.setStatus("mandatory")


class _WfPgmEnable_Type(Integer32):
    """Custom type wfPgmEnable based on Integer32"""
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


_WfPgmEnable_Type.__name__ = "Integer32"
_WfPgmEnable_Object = MibScalar
wfPgmEnable = _WfPgmEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 2),
    _WfPgmEnable_Type()
)
wfPgmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmEnable.setStatus("mandatory")


class _WfPgmState_Type(Integer32):
    """Custom type wfPgmState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfPgmState_Type.__name__ = "Integer32"
_WfPgmState_Object = MibScalar
wfPgmState = _WfPgmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 3),
    _WfPgmState_Type()
)
wfPgmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmState.setStatus("mandatory")
_WfPgmDebug_Type = Integer32
_WfPgmDebug_Object = MibScalar
wfPgmDebug = _WfPgmDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 4),
    _WfPgmDebug_Type()
)
wfPgmDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmDebug.setStatus("mandatory")


class _WfPgmSessionLifeTime_Type(Integer32):
    """Custom type wfPgmSessionLifeTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfPgmSessionLifeTime_Type.__name__ = "Integer32"
_WfPgmSessionLifeTime_Object = MibScalar
wfPgmSessionLifeTime = _WfPgmSessionLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 5),
    _WfPgmSessionLifeTime_Type()
)
wfPgmSessionLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmSessionLifeTime.setStatus("mandatory")


class _WfPgmNnakGenerate_Type(Integer32):
    """Custom type wfPgmNnakGenerate based on Integer32"""
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


_WfPgmNnakGenerate_Type.__name__ = "Integer32"
_WfPgmNnakGenerate_Object = MibScalar
wfPgmNnakGenerate = _WfPgmNnakGenerate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 6),
    _WfPgmNnakGenerate_Type()
)
wfPgmNnakGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmNnakGenerate.setStatus("mandatory")


class _WfPgmMaxReXmitStates_Type(Integer32):
    """Custom type wfPgmMaxReXmitStates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfPgmMaxReXmitStates_Type.__name__ = "Integer32"
_WfPgmMaxReXmitStates_Object = MibScalar
wfPgmMaxReXmitStates = _WfPgmMaxReXmitStates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 7),
    _WfPgmMaxReXmitStates_Type()
)
wfPgmMaxReXmitStates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmMaxReXmitStates.setStatus("mandatory")
_WfPgmTotalReXmitStates_Type = Gauge32
_WfPgmTotalReXmitStates_Object = MibScalar
wfPgmTotalReXmitStates = _WfPgmTotalReXmitStates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 8),
    _WfPgmTotalReXmitStates_Type()
)
wfPgmTotalReXmitStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmTotalReXmitStates.setStatus("mandatory")


class _WfPgmMaxSessions_Type(Integer32):
    """Custom type wfPgmMaxSessions based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfPgmMaxSessions_Type.__name__ = "Integer32"
_WfPgmMaxSessions_Object = MibScalar
wfPgmMaxSessions = _WfPgmMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 9),
    _WfPgmMaxSessions_Type()
)
wfPgmMaxSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmMaxSessions.setStatus("mandatory")
_WfPgmTotalSessions_Type = Gauge32
_WfPgmTotalSessions_Object = MibScalar
wfPgmTotalSessions = _WfPgmTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 10),
    _WfPgmTotalSessions_Type()
)
wfPgmTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmTotalSessions.setStatus("mandatory")
_WfPgmTotalReXmitStatesTimedOut_Type = Gauge32
_WfPgmTotalReXmitStatesTimedOut_Object = MibScalar
wfPgmTotalReXmitStatesTimedOut = _WfPgmTotalReXmitStatesTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 11),
    _WfPgmTotalReXmitStatesTimedOut_Type()
)
wfPgmTotalReXmitStatesTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmTotalReXmitStatesTimedOut.setStatus("mandatory")
_WfPgmTotalUniqueNaks_Type = Gauge32
_WfPgmTotalUniqueNaks_Object = MibScalar
wfPgmTotalUniqueNaks = _WfPgmTotalUniqueNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 12),
    _WfPgmTotalUniqueNaks_Type()
)
wfPgmTotalUniqueNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmTotalUniqueNaks.setStatus("mandatory")
_WfPgmTotalUniqueParityNaks_Type = Gauge32
_WfPgmTotalUniqueParityNaks_Object = MibScalar
wfPgmTotalUniqueParityNaks = _WfPgmTotalUniqueParityNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 13),
    _WfPgmTotalUniqueParityNaks_Type()
)
wfPgmTotalUniqueParityNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmTotalUniqueParityNaks.setStatus("mandatory")


class _WfPgmMaxNakRate_Type(Integer32):
    """Custom type wfPgmMaxNakRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfPgmMaxNakRate_Type.__name__ = "Integer32"
_WfPgmMaxNakRate_Object = MibScalar
wfPgmMaxNakRate = _WfPgmMaxNakRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 1, 14),
    _WfPgmMaxNakRate_Type()
)
wfPgmMaxNakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmMaxNakRate.setStatus("mandatory")
_WfPgmIfTable_Object = MibTable
wfPgmIfTable = _WfPgmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2)
)
if mibBuilder.loadTexts:
    wfPgmIfTable.setStatus("mandatory")
_WfPgmIfEntry_Object = MibTableRow
wfPgmIfEntry = _WfPgmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1)
)
wfPgmIfEntry.setIndexNames(
    (0, "Wellfleet-PGM-MIB", "wfPgmIfCct"),
)
if mibBuilder.loadTexts:
    wfPgmIfEntry.setStatus("mandatory")


class _WfPgmIfCreate_Type(Integer32):
    """Custom type wfPgmIfCreate based on Integer32"""
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


_WfPgmIfCreate_Type.__name__ = "Integer32"
_WfPgmIfCreate_Object = MibTableColumn
wfPgmIfCreate = _WfPgmIfCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 1),
    _WfPgmIfCreate_Type()
)
wfPgmIfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmIfCreate.setStatus("mandatory")


class _WfPgmIfEnable_Type(Integer32):
    """Custom type wfPgmIfEnable based on Integer32"""
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


_WfPgmIfEnable_Type.__name__ = "Integer32"
_WfPgmIfEnable_Object = MibTableColumn
wfPgmIfEnable = _WfPgmIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 2),
    _WfPgmIfEnable_Type()
)
wfPgmIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmIfEnable.setStatus("mandatory")


class _WfPgmIfState_Type(Integer32):
    """Custom type wfPgmIfState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("notpres", 4),
          ("up", 1))
    )


_WfPgmIfState_Type.__name__ = "Integer32"
_WfPgmIfState_Object = MibTableColumn
wfPgmIfState = _WfPgmIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 3),
    _WfPgmIfState_Type()
)
wfPgmIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfState.setStatus("mandatory")
_WfPgmIfCct_Type = Integer32
_WfPgmIfCct_Object = MibTableColumn
wfPgmIfCct = _WfPgmIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 4),
    _WfPgmIfCct_Type()
)
wfPgmIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfCct.setStatus("mandatory")


class _WfPgmIfNakReXmitInterval_Type(Integer32):
    """Custom type wfPgmIfNakReXmitInterval based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2147483647),
    )


_WfPgmIfNakReXmitInterval_Type.__name__ = "Integer32"
_WfPgmIfNakReXmitInterval_Object = MibTableColumn
wfPgmIfNakReXmitInterval = _WfPgmIfNakReXmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 5),
    _WfPgmIfNakReXmitInterval_Type()
)
wfPgmIfNakReXmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmIfNakReXmitInterval.setStatus("mandatory")


class _WfPgmIfMaxNakReXmitRate_Type(Integer32):
    """Custom type wfPgmIfMaxNakReXmitRate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfPgmIfMaxNakReXmitRate_Type.__name__ = "Integer32"
_WfPgmIfMaxNakReXmitRate_Object = MibTableColumn
wfPgmIfMaxNakReXmitRate = _WfPgmIfMaxNakReXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 6),
    _WfPgmIfMaxNakReXmitRate_Type()
)
wfPgmIfMaxNakReXmitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmIfMaxNakReXmitRate.setStatus("mandatory")


class _WfPgmIfNakRdataInterval_Type(Integer32):
    """Custom type wfPgmIfNakRdataInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfPgmIfNakRdataInterval_Type.__name__ = "Integer32"
_WfPgmIfNakRdataInterval_Object = MibTableColumn
wfPgmIfNakRdataInterval = _WfPgmIfNakRdataInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 7),
    _WfPgmIfNakRdataInterval_Type()
)
wfPgmIfNakRdataInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmIfNakRdataInterval.setStatus("mandatory")


class _WfPgmIfNakEliminateInterval_Type(Integer32):
    """Custom type wfPgmIfNakEliminateInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfPgmIfNakEliminateInterval_Type.__name__ = "Integer32"
_WfPgmIfNakEliminateInterval_Object = MibTableColumn
wfPgmIfNakEliminateInterval = _WfPgmIfNakEliminateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 8),
    _WfPgmIfNakEliminateInterval_Type()
)
wfPgmIfNakEliminateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPgmIfNakEliminateInterval.setStatus("mandatory")
_WfPgmIfTotalReXmitStates_Type = Counter32
_WfPgmIfTotalReXmitStates_Object = MibTableColumn
wfPgmIfTotalReXmitStates = _WfPgmIfTotalReXmitStates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 9),
    _WfPgmIfTotalReXmitStates_Type()
)
wfPgmIfTotalReXmitStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfTotalReXmitStates.setStatus("mandatory")
_WfPgmIfTotalReXmitTimedOut_Type = Counter32
_WfPgmIfTotalReXmitTimedOut_Object = MibTableColumn
wfPgmIfTotalReXmitTimedOut = _WfPgmIfTotalReXmitTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 10),
    _WfPgmIfTotalReXmitTimedOut_Type()
)
wfPgmIfTotalReXmitTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfTotalReXmitTimedOut.setStatus("mandatory")
_WfPgmIfInSpms_Type = Counter32
_WfPgmIfInSpms_Object = MibTableColumn
wfPgmIfInSpms = _WfPgmIfInSpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 11),
    _WfPgmIfInSpms_Type()
)
wfPgmIfInSpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInSpms.setStatus("mandatory")
_WfPgmIfOutSpms_Type = Counter32
_WfPgmIfOutSpms_Object = MibTableColumn
wfPgmIfOutSpms = _WfPgmIfOutSpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 12),
    _WfPgmIfOutSpms_Type()
)
wfPgmIfOutSpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutSpms.setStatus("mandatory")
_WfPgmIfInParitySpms_Type = Counter32
_WfPgmIfInParitySpms_Object = MibTableColumn
wfPgmIfInParitySpms = _WfPgmIfInParitySpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 13),
    _WfPgmIfInParitySpms_Type()
)
wfPgmIfInParitySpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInParitySpms.setStatus("mandatory")
_WfPgmIfOutParitySpms_Type = Counter32
_WfPgmIfOutParitySpms_Object = MibTableColumn
wfPgmIfOutParitySpms = _WfPgmIfOutParitySpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 14),
    _WfPgmIfOutParitySpms_Type()
)
wfPgmIfOutParitySpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutParitySpms.setStatus("mandatory")
_WfPgmIfInSpmPortErrors_Type = Counter32
_WfPgmIfInSpmPortErrors_Object = MibTableColumn
wfPgmIfInSpmPortErrors = _WfPgmIfInSpmPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 15),
    _WfPgmIfInSpmPortErrors_Type()
)
wfPgmIfInSpmPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInSpmPortErrors.setStatus("mandatory")
_WfPgmIfInRdata_Type = Counter32
_WfPgmIfInRdata_Object = MibTableColumn
wfPgmIfInRdata = _WfPgmIfInRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 16),
    _WfPgmIfInRdata_Type()
)
wfPgmIfInRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInRdata.setStatus("mandatory")
_WfPgmIfOutRdata_Type = Counter32
_WfPgmIfOutRdata_Object = MibTableColumn
wfPgmIfOutRdata = _WfPgmIfOutRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 17),
    _WfPgmIfOutRdata_Type()
)
wfPgmIfOutRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutRdata.setStatus("mandatory")
_WfPgmIfInParityRdata_Type = Counter32
_WfPgmIfInParityRdata_Object = MibTableColumn
wfPgmIfInParityRdata = _WfPgmIfInParityRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 18),
    _WfPgmIfInParityRdata_Type()
)
wfPgmIfInParityRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInParityRdata.setStatus("mandatory")
_WfPgmIfOutParityRdata_Type = Counter32
_WfPgmIfOutParityRdata_Object = MibTableColumn
wfPgmIfOutParityRdata = _WfPgmIfOutParityRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 19),
    _WfPgmIfOutParityRdata_Type()
)
wfPgmIfOutParityRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutParityRdata.setStatus("mandatory")
_WfPgmIfInRdataPortErrors_Type = Counter32
_WfPgmIfInRdataPortErrors_Object = MibTableColumn
wfPgmIfInRdataPortErrors = _WfPgmIfInRdataPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 20),
    _WfPgmIfInRdataPortErrors_Type()
)
wfPgmIfInRdataPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInRdataPortErrors.setStatus("mandatory")
_WfPgmIfInRdataNoSessionErrors_Type = Counter32
_WfPgmIfInRdataNoSessionErrors_Object = MibTableColumn
wfPgmIfInRdataNoSessionErrors = _WfPgmIfInRdataNoSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 21),
    _WfPgmIfInRdataNoSessionErrors_Type()
)
wfPgmIfInRdataNoSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInRdataNoSessionErrors.setStatus("mandatory")
_WfPgmIfUniqueNaks_Type = Counter32
_WfPgmIfUniqueNaks_Object = MibTableColumn
wfPgmIfUniqueNaks = _WfPgmIfUniqueNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 22),
    _WfPgmIfUniqueNaks_Type()
)
wfPgmIfUniqueNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfUniqueNaks.setStatus("mandatory")
_WfPgmIfInNaks_Type = Counter32
_WfPgmIfInNaks_Object = MibTableColumn
wfPgmIfInNaks = _WfPgmIfInNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 23),
    _WfPgmIfInNaks_Type()
)
wfPgmIfInNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNaks.setStatus("mandatory")
_WfPgmIfOutNaks_Type = Counter32
_WfPgmIfOutNaks_Object = MibTableColumn
wfPgmIfOutNaks = _WfPgmIfOutNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 24),
    _WfPgmIfOutNaks_Type()
)
wfPgmIfOutNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutNaks.setStatus("mandatory")
_WfPgmIfUniqueParityNaks_Type = Counter32
_WfPgmIfUniqueParityNaks_Object = MibTableColumn
wfPgmIfUniqueParityNaks = _WfPgmIfUniqueParityNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 25),
    _WfPgmIfUniqueParityNaks_Type()
)
wfPgmIfUniqueParityNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfUniqueParityNaks.setStatus("mandatory")
_WfPgmIfInParityNaks_Type = Counter32
_WfPgmIfInParityNaks_Object = MibTableColumn
wfPgmIfInParityNaks = _WfPgmIfInParityNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 26),
    _WfPgmIfInParityNaks_Type()
)
wfPgmIfInParityNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInParityNaks.setStatus("mandatory")
_WfPgmIfOutParityNaks_Type = Counter32
_WfPgmIfOutParityNaks_Object = MibTableColumn
wfPgmIfOutParityNaks = _WfPgmIfOutParityNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 27),
    _WfPgmIfOutParityNaks_Type()
)
wfPgmIfOutParityNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutParityNaks.setStatus("mandatory")
_WfPgmIfInNakPortErrors_Type = Counter32
_WfPgmIfInNakPortErrors_Object = MibTableColumn
wfPgmIfInNakPortErrors = _WfPgmIfInNakPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 28),
    _WfPgmIfInNakPortErrors_Type()
)
wfPgmIfInNakPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNakPortErrors.setStatus("mandatory")
_WfPgmIfInNakNoSessionErrors_Type = Counter32
_WfPgmIfInNakNoSessionErrors_Object = MibTableColumn
wfPgmIfInNakNoSessionErrors = _WfPgmIfInNakNoSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 29),
    _WfPgmIfInNakNoSessionErrors_Type()
)
wfPgmIfInNakNoSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNakNoSessionErrors.setStatus("mandatory")
_WfPgmIfInNakSeqErrors_Type = Counter32
_WfPgmIfInNakSeqErrors_Object = MibTableColumn
wfPgmIfInNakSeqErrors = _WfPgmIfInNakSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 30),
    _WfPgmIfInNakSeqErrors_Type()
)
wfPgmIfInNakSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNakSeqErrors.setStatus("mandatory")
_WfPgmIfInParityNakTgErrors_Type = Counter32
_WfPgmIfInParityNakTgErrors_Object = MibTableColumn
wfPgmIfInParityNakTgErrors = _WfPgmIfInParityNakTgErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 31),
    _WfPgmIfInParityNakTgErrors_Type()
)
wfPgmIfInParityNakTgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInParityNakTgErrors.setStatus("mandatory")
_WfPgmIfInNnaks_Type = Counter32
_WfPgmIfInNnaks_Object = MibTableColumn
wfPgmIfInNnaks = _WfPgmIfInNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 32),
    _WfPgmIfInNnaks_Type()
)
wfPgmIfInNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNnaks.setStatus("mandatory")
_WfPgmIfOutNnaks_Type = Counter32
_WfPgmIfOutNnaks_Object = MibTableColumn
wfPgmIfOutNnaks = _WfPgmIfOutNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 33),
    _WfPgmIfOutNnaks_Type()
)
wfPgmIfOutNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutNnaks.setStatus("mandatory")
_WfPgmIfInParityNnaks_Type = Counter32
_WfPgmIfInParityNnaks_Object = MibTableColumn
wfPgmIfInParityNnaks = _WfPgmIfInParityNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 34),
    _WfPgmIfInParityNnaks_Type()
)
wfPgmIfInParityNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInParityNnaks.setStatus("mandatory")
_WfPgmIfOutParityNnaks_Type = Counter32
_WfPgmIfOutParityNnaks_Object = MibTableColumn
wfPgmIfOutParityNnaks = _WfPgmIfOutParityNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 35),
    _WfPgmIfOutParityNnaks_Type()
)
wfPgmIfOutParityNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutParityNnaks.setStatus("mandatory")
_WfPgmIfInNnakPortErrors_Type = Counter32
_WfPgmIfInNnakPortErrors_Object = MibTableColumn
wfPgmIfInNnakPortErrors = _WfPgmIfInNnakPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 36),
    _WfPgmIfInNnakPortErrors_Type()
)
wfPgmIfInNnakPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNnakPortErrors.setStatus("mandatory")
_WfPgmIfInNnakNoSessionErrors_Type = Counter32
_WfPgmIfInNnakNoSessionErrors_Object = MibTableColumn
wfPgmIfInNnakNoSessionErrors = _WfPgmIfInNnakNoSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 37),
    _WfPgmIfInNnakNoSessionErrors_Type()
)
wfPgmIfInNnakNoSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNnakNoSessionErrors.setStatus("mandatory")
_WfPgmIfInNcfs_Type = Counter32
_WfPgmIfInNcfs_Object = MibTableColumn
wfPgmIfInNcfs = _WfPgmIfInNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 38),
    _WfPgmIfInNcfs_Type()
)
wfPgmIfInNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNcfs.setStatus("mandatory")
_WfPgmIfOutNcfs_Type = Counter32
_WfPgmIfOutNcfs_Object = MibTableColumn
wfPgmIfOutNcfs = _WfPgmIfOutNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 39),
    _WfPgmIfOutNcfs_Type()
)
wfPgmIfOutNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutNcfs.setStatus("mandatory")
_WfPgmIfInParityNcfs_Type = Counter32
_WfPgmIfInParityNcfs_Object = MibTableColumn
wfPgmIfInParityNcfs = _WfPgmIfInParityNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 40),
    _WfPgmIfInParityNcfs_Type()
)
wfPgmIfInParityNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInParityNcfs.setStatus("mandatory")
_WfPgmIfOutParityNcfs_Type = Counter32
_WfPgmIfOutParityNcfs_Object = MibTableColumn
wfPgmIfOutParityNcfs = _WfPgmIfOutParityNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 41),
    _WfPgmIfOutParityNcfs_Type()
)
wfPgmIfOutParityNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfOutParityNcfs.setStatus("mandatory")
_WfPgmIfInNcfPortErrors_Type = Counter32
_WfPgmIfInNcfPortErrors_Object = MibTableColumn
wfPgmIfInNcfPortErrors = _WfPgmIfInNcfPortErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 42),
    _WfPgmIfInNcfPortErrors_Type()
)
wfPgmIfInNcfPortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNcfPortErrors.setStatus("mandatory")
_WfPgmIfInNcfNoSessionErrors_Type = Counter32
_WfPgmIfInNcfNoSessionErrors_Object = MibTableColumn
wfPgmIfInNcfNoSessionErrors = _WfPgmIfInNcfNoSessionErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 43),
    _WfPgmIfInNcfNoSessionErrors_Type()
)
wfPgmIfInNcfNoSessionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInNcfNoSessionErrors.setStatus("mandatory")
_WfPgmIfInRedirectNcfs_Type = Counter32
_WfPgmIfInRedirectNcfs_Object = MibTableColumn
wfPgmIfInRedirectNcfs = _WfPgmIfInRedirectNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 2, 1, 44),
    _WfPgmIfInRedirectNcfs_Type()
)
wfPgmIfInRedirectNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmIfInRedirectNcfs.setStatus("mandatory")
_WfPgmSessionTable_Object = MibTable
wfPgmSessionTable = _WfPgmSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3)
)
if mibBuilder.loadTexts:
    wfPgmSessionTable.setStatus("mandatory")
_WfPgmSessionEntry_Object = MibTableRow
wfPgmSessionEntry = _WfPgmSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1)
)
wfPgmSessionEntry.setIndexNames(
    (0, "Wellfleet-PGM-MIB", "wfPgmSessionSource"),
    (0, "Wellfleet-PGM-MIB", "wfPgmSessionGroup"),
    (0, "Wellfleet-PGM-MIB", "wfPgmSessionSourcePort"),
    (0, "Wellfleet-PGM-MIB", "wfPgmSessionGlobalId"),
)
if mibBuilder.loadTexts:
    wfPgmSessionEntry.setStatus("mandatory")
_WfPgmSessionSource_Type = IpAddress
_WfPgmSessionSource_Object = MibTableColumn
wfPgmSessionSource = _WfPgmSessionSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 1),
    _WfPgmSessionSource_Type()
)
wfPgmSessionSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionSource.setStatus("mandatory")
_WfPgmSessionGroup_Type = IpAddress
_WfPgmSessionGroup_Object = MibTableColumn
wfPgmSessionGroup = _WfPgmSessionGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 2),
    _WfPgmSessionGroup_Type()
)
wfPgmSessionGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionGroup.setStatus("mandatory")
_WfPgmSessionSourcePort_Type = Integer32
_WfPgmSessionSourcePort_Object = MibTableColumn
wfPgmSessionSourcePort = _WfPgmSessionSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 3),
    _WfPgmSessionSourcePort_Type()
)
wfPgmSessionSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionSourcePort.setStatus("mandatory")


class _WfPgmSessionGlobalId_Type(OctetString):
    """Custom type wfPgmSessionGlobalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfPgmSessionGlobalId_Type.__name__ = "OctetString"
_WfPgmSessionGlobalId_Object = MibTableColumn
wfPgmSessionGlobalId = _WfPgmSessionGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 4),
    _WfPgmSessionGlobalId_Type()
)
wfPgmSessionGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionGlobalId.setStatus("mandatory")
_WfPgmSessionUpstreamAddress_Type = IpAddress
_WfPgmSessionUpstreamAddress_Object = MibTableColumn
wfPgmSessionUpstreamAddress = _WfPgmSessionUpstreamAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 5),
    _WfPgmSessionUpstreamAddress_Type()
)
wfPgmSessionUpstreamAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionUpstreamAddress.setStatus("mandatory")
_WfPgmSessionUpstreamIfCct_Type = Integer32
_WfPgmSessionUpstreamIfCct_Object = MibTableColumn
wfPgmSessionUpstreamIfCct = _WfPgmSessionUpstreamIfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 6),
    _WfPgmSessionUpstreamIfCct_Type()
)
wfPgmSessionUpstreamIfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionUpstreamIfCct.setStatus("mandatory")
_WfPgmSessionTrailEdgeSeq_Type = Counter32
_WfPgmSessionTrailEdgeSeq_Object = MibTableColumn
wfPgmSessionTrailEdgeSeq = _WfPgmSessionTrailEdgeSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 7),
    _WfPgmSessionTrailEdgeSeq_Type()
)
wfPgmSessionTrailEdgeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionTrailEdgeSeq.setStatus("mandatory")
_WfPgmSessionIncrSeq_Type = Counter32
_WfPgmSessionIncrSeq_Object = MibTableColumn
wfPgmSessionIncrSeq = _WfPgmSessionIncrSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 8),
    _WfPgmSessionIncrSeq_Type()
)
wfPgmSessionIncrSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionIncrSeq.setStatus("mandatory")
_WfPgmSessionLeadEdgeSeq_Type = Counter32
_WfPgmSessionLeadEdgeSeq_Object = MibTableColumn
wfPgmSessionLeadEdgeSeq = _WfPgmSessionLeadEdgeSeq_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 9),
    _WfPgmSessionLeadEdgeSeq_Type()
)
wfPgmSessionLeadEdgeSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionLeadEdgeSeq.setStatus("mandatory")
_WfPgmSessionInSpms_Type = Counter32
_WfPgmSessionInSpms_Object = MibTableColumn
wfPgmSessionInSpms = _WfPgmSessionInSpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 10),
    _WfPgmSessionInSpms_Type()
)
wfPgmSessionInSpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInSpms.setStatus("mandatory")
_WfPgmSessionOutSpms_Type = Counter32
_WfPgmSessionOutSpms_Object = MibTableColumn
wfPgmSessionOutSpms = _WfPgmSessionOutSpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 11),
    _WfPgmSessionOutSpms_Type()
)
wfPgmSessionOutSpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutSpms.setStatus("mandatory")
_WfPgmSessionInParitySpms_Type = Counter32
_WfPgmSessionInParitySpms_Object = MibTableColumn
wfPgmSessionInParitySpms = _WfPgmSessionInParitySpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 12),
    _WfPgmSessionInParitySpms_Type()
)
wfPgmSessionInParitySpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInParitySpms.setStatus("mandatory")
_WfPgmSessionOutParitySpms_Type = Counter32
_WfPgmSessionOutParitySpms_Object = MibTableColumn
wfPgmSessionOutParitySpms = _WfPgmSessionOutParitySpms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 13),
    _WfPgmSessionOutParitySpms_Type()
)
wfPgmSessionOutParitySpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutParitySpms.setStatus("mandatory")
_WfPgmSessionTotalReXmitStates_Type = Counter32
_WfPgmSessionTotalReXmitStates_Object = MibTableColumn
wfPgmSessionTotalReXmitStates = _WfPgmSessionTotalReXmitStates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 14),
    _WfPgmSessionTotalReXmitStates_Type()
)
wfPgmSessionTotalReXmitStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionTotalReXmitStates.setStatus("mandatory")
_WfPgmSessionTotalReXmitTimedOut_Type = Counter32
_WfPgmSessionTotalReXmitTimedOut_Object = MibTableColumn
wfPgmSessionTotalReXmitTimedOut = _WfPgmSessionTotalReXmitTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 15),
    _WfPgmSessionTotalReXmitTimedOut_Type()
)
wfPgmSessionTotalReXmitTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionTotalReXmitTimedOut.setStatus("mandatory")
_WfPgmSessionInRdata_Type = Counter32
_WfPgmSessionInRdata_Object = MibTableColumn
wfPgmSessionInRdata = _WfPgmSessionInRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 16),
    _WfPgmSessionInRdata_Type()
)
wfPgmSessionInRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInRdata.setStatus("mandatory")
_WfPgmSessionOutRdata_Type = Counter32
_WfPgmSessionOutRdata_Object = MibTableColumn
wfPgmSessionOutRdata = _WfPgmSessionOutRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 17),
    _WfPgmSessionOutRdata_Type()
)
wfPgmSessionOutRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutRdata.setStatus("mandatory")
_WfPgmSessionInParityRdata_Type = Counter32
_WfPgmSessionInParityRdata_Object = MibTableColumn
wfPgmSessionInParityRdata = _WfPgmSessionInParityRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 18),
    _WfPgmSessionInParityRdata_Type()
)
wfPgmSessionInParityRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInParityRdata.setStatus("mandatory")
_WfPgmSessionOutParityRdata_Type = Counter32
_WfPgmSessionOutParityRdata_Object = MibTableColumn
wfPgmSessionOutParityRdata = _WfPgmSessionOutParityRdata_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 19),
    _WfPgmSessionOutParityRdata_Type()
)
wfPgmSessionOutParityRdata.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutParityRdata.setStatus("mandatory")
_WfPgmSessionInRdataNoStateErrors_Type = Counter32
_WfPgmSessionInRdataNoStateErrors_Object = MibTableColumn
wfPgmSessionInRdataNoStateErrors = _WfPgmSessionInRdataNoStateErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 20),
    _WfPgmSessionInRdataNoStateErrors_Type()
)
wfPgmSessionInRdataNoStateErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInRdataNoStateErrors.setStatus("mandatory")
_WfPgmSessionUniqueNaks_Type = Counter32
_WfPgmSessionUniqueNaks_Object = MibTableColumn
wfPgmSessionUniqueNaks = _WfPgmSessionUniqueNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 21),
    _WfPgmSessionUniqueNaks_Type()
)
wfPgmSessionUniqueNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionUniqueNaks.setStatus("mandatory")
_WfPgmSessionInNaks_Type = Counter32
_WfPgmSessionInNaks_Object = MibTableColumn
wfPgmSessionInNaks = _WfPgmSessionInNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 22),
    _WfPgmSessionInNaks_Type()
)
wfPgmSessionInNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInNaks.setStatus("mandatory")
_WfPgmSessionOutNaks_Type = Counter32
_WfPgmSessionOutNaks_Object = MibTableColumn
wfPgmSessionOutNaks = _WfPgmSessionOutNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 23),
    _WfPgmSessionOutNaks_Type()
)
wfPgmSessionOutNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutNaks.setStatus("mandatory")
_WfPgmSessionUniqueParityNaks_Type = Counter32
_WfPgmSessionUniqueParityNaks_Object = MibTableColumn
wfPgmSessionUniqueParityNaks = _WfPgmSessionUniqueParityNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 24),
    _WfPgmSessionUniqueParityNaks_Type()
)
wfPgmSessionUniqueParityNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionUniqueParityNaks.setStatus("mandatory")
_WfPgmSessionInParityNaks_Type = Counter32
_WfPgmSessionInParityNaks_Object = MibTableColumn
wfPgmSessionInParityNaks = _WfPgmSessionInParityNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 25),
    _WfPgmSessionInParityNaks_Type()
)
wfPgmSessionInParityNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInParityNaks.setStatus("mandatory")
_WfPgmSessionOutParityNaks_Type = Counter32
_WfPgmSessionOutParityNaks_Object = MibTableColumn
wfPgmSessionOutParityNaks = _WfPgmSessionOutParityNaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 26),
    _WfPgmSessionOutParityNaks_Type()
)
wfPgmSessionOutParityNaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutParityNaks.setStatus("mandatory")
_WfPgmSessionInNakSeqErrors_Type = Counter32
_WfPgmSessionInNakSeqErrors_Object = MibTableColumn
wfPgmSessionInNakSeqErrors = _WfPgmSessionInNakSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 27),
    _WfPgmSessionInNakSeqErrors_Type()
)
wfPgmSessionInNakSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInNakSeqErrors.setStatus("mandatory")
_WfPgmSessionInNnaks_Type = Counter32
_WfPgmSessionInNnaks_Object = MibTableColumn
wfPgmSessionInNnaks = _WfPgmSessionInNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 28),
    _WfPgmSessionInNnaks_Type()
)
wfPgmSessionInNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInNnaks.setStatus("mandatory")
_WfPgmSessionOutNnaks_Type = Counter32
_WfPgmSessionOutNnaks_Object = MibTableColumn
wfPgmSessionOutNnaks = _WfPgmSessionOutNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 29),
    _WfPgmSessionOutNnaks_Type()
)
wfPgmSessionOutNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutNnaks.setStatus("mandatory")
_WfPgmSessionInParityNnaks_Type = Counter32
_WfPgmSessionInParityNnaks_Object = MibTableColumn
wfPgmSessionInParityNnaks = _WfPgmSessionInParityNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 30),
    _WfPgmSessionInParityNnaks_Type()
)
wfPgmSessionInParityNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInParityNnaks.setStatus("mandatory")
_WfPgmSessionOutParityNnaks_Type = Counter32
_WfPgmSessionOutParityNnaks_Object = MibTableColumn
wfPgmSessionOutParityNnaks = _WfPgmSessionOutParityNnaks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 31),
    _WfPgmSessionOutParityNnaks_Type()
)
wfPgmSessionOutParityNnaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutParityNnaks.setStatus("mandatory")
_WfPgmSessionInNcfs_Type = Counter32
_WfPgmSessionInNcfs_Object = MibTableColumn
wfPgmSessionInNcfs = _WfPgmSessionInNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 32),
    _WfPgmSessionInNcfs_Type()
)
wfPgmSessionInNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInNcfs.setStatus("mandatory")
_WfPgmSessionOutNcfs_Type = Counter32
_WfPgmSessionOutNcfs_Object = MibTableColumn
wfPgmSessionOutNcfs = _WfPgmSessionOutNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 33),
    _WfPgmSessionOutNcfs_Type()
)
wfPgmSessionOutNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutNcfs.setStatus("mandatory")
_WfPgmSessionInParityNcfs_Type = Counter32
_WfPgmSessionInParityNcfs_Object = MibTableColumn
wfPgmSessionInParityNcfs = _WfPgmSessionInParityNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 34),
    _WfPgmSessionInParityNcfs_Type()
)
wfPgmSessionInParityNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInParityNcfs.setStatus("mandatory")
_WfPgmSessionOutParityNcfs_Type = Counter32
_WfPgmSessionOutParityNcfs_Object = MibTableColumn
wfPgmSessionOutParityNcfs = _WfPgmSessionOutParityNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 35),
    _WfPgmSessionOutParityNcfs_Type()
)
wfPgmSessionOutParityNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionOutParityNcfs.setStatus("mandatory")
_WfPgmSessionInRedirectNcfs_Type = Counter32
_WfPgmSessionInRedirectNcfs_Object = MibTableColumn
wfPgmSessionInRedirectNcfs = _WfPgmSessionInRedirectNcfs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 3, 1, 36),
    _WfPgmSessionInRedirectNcfs_Type()
)
wfPgmSessionInRedirectNcfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmSessionInRedirectNcfs.setStatus("mandatory")
_WfPgmReXmitTable_Object = MibTable
wfPgmReXmitTable = _WfPgmReXmitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4)
)
if mibBuilder.loadTexts:
    wfPgmReXmitTable.setStatus("mandatory")
_WfPgmReXmitEntry_Object = MibTableRow
wfPgmReXmitEntry = _WfPgmReXmitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1)
)
wfPgmReXmitEntry.setIndexNames(
    (0, "Wellfleet-PGM-MIB", "wfPgmReXmitSource"),
    (0, "Wellfleet-PGM-MIB", "wfPgmReXmitGroup"),
    (0, "Wellfleet-PGM-MIB", "wfPgmReXmitSourcePort"),
    (0, "Wellfleet-PGM-MIB", "wfPgmReXmitGlobalId"),
    (0, "Wellfleet-PGM-MIB", "wfPgmReXmitSelectiveSeqNum"),
    (0, "Wellfleet-PGM-MIB", "wfPgmReXmitParityTgSeqNum"),
)
if mibBuilder.loadTexts:
    wfPgmReXmitEntry.setStatus("mandatory")
_WfPgmReXmitSource_Type = IpAddress
_WfPgmReXmitSource_Object = MibTableColumn
wfPgmReXmitSource = _WfPgmReXmitSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 1),
    _WfPgmReXmitSource_Type()
)
wfPgmReXmitSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitSource.setStatus("mandatory")
_WfPgmReXmitGroup_Type = IpAddress
_WfPgmReXmitGroup_Object = MibTableColumn
wfPgmReXmitGroup = _WfPgmReXmitGroup_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 2),
    _WfPgmReXmitGroup_Type()
)
wfPgmReXmitGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitGroup.setStatus("mandatory")
_WfPgmReXmitSourcePort_Type = Integer32
_WfPgmReXmitSourcePort_Object = MibTableColumn
wfPgmReXmitSourcePort = _WfPgmReXmitSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 3),
    _WfPgmReXmitSourcePort_Type()
)
wfPgmReXmitSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitSourcePort.setStatus("mandatory")


class _WfPgmReXmitGlobalId_Type(OctetString):
    """Custom type wfPgmReXmitGlobalId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfPgmReXmitGlobalId_Type.__name__ = "OctetString"
_WfPgmReXmitGlobalId_Object = MibTableColumn
wfPgmReXmitGlobalId = _WfPgmReXmitGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 4),
    _WfPgmReXmitGlobalId_Type()
)
wfPgmReXmitGlobalId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitGlobalId.setStatus("mandatory")
_WfPgmReXmitSelectiveSeqNum_Type = Integer32
_WfPgmReXmitSelectiveSeqNum_Object = MibTableColumn
wfPgmReXmitSelectiveSeqNum = _WfPgmReXmitSelectiveSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 5),
    _WfPgmReXmitSelectiveSeqNum_Type()
)
wfPgmReXmitSelectiveSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitSelectiveSeqNum.setStatus("mandatory")
_WfPgmReXmitParityTgSeqNum_Type = Integer32
_WfPgmReXmitParityTgSeqNum_Object = MibTableColumn
wfPgmReXmitParityTgSeqNum = _WfPgmReXmitParityTgSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 6),
    _WfPgmReXmitParityTgSeqNum_Type()
)
wfPgmReXmitParityTgSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitParityTgSeqNum.setStatus("mandatory")
_WfPgmReXmitReqParityTgCount_Type = Integer32
_WfPgmReXmitReqParityTgCount_Object = MibTableColumn
wfPgmReXmitReqParityTgCount = _WfPgmReXmitReqParityTgCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 7),
    _WfPgmReXmitReqParityTgCount_Type()
)
wfPgmReXmitReqParityTgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitReqParityTgCount.setStatus("mandatory")
_WfPgmReXmitUpStreamCct_Type = Integer32
_WfPgmReXmitUpStreamCct_Object = MibTableColumn
wfPgmReXmitUpStreamCct = _WfPgmReXmitUpStreamCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 8),
    _WfPgmReXmitUpStreamCct_Type()
)
wfPgmReXmitUpStreamCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitUpStreamCct.setStatus("mandatory")
_WfPgmReXmitDownStream_Type = OctetString
_WfPgmReXmitDownStream_Object = MibTableColumn
wfPgmReXmitDownStream = _WfPgmReXmitDownStream_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 28, 4, 1, 9),
    _WfPgmReXmitDownStream_Type()
)
wfPgmReXmitDownStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfPgmReXmitDownStream.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-PGM-MIB",
    **{"wfPgm": wfPgm,
       "wfPgmCreate": wfPgmCreate,
       "wfPgmEnable": wfPgmEnable,
       "wfPgmState": wfPgmState,
       "wfPgmDebug": wfPgmDebug,
       "wfPgmSessionLifeTime": wfPgmSessionLifeTime,
       "wfPgmNnakGenerate": wfPgmNnakGenerate,
       "wfPgmMaxReXmitStates": wfPgmMaxReXmitStates,
       "wfPgmTotalReXmitStates": wfPgmTotalReXmitStates,
       "wfPgmMaxSessions": wfPgmMaxSessions,
       "wfPgmTotalSessions": wfPgmTotalSessions,
       "wfPgmTotalReXmitStatesTimedOut": wfPgmTotalReXmitStatesTimedOut,
       "wfPgmTotalUniqueNaks": wfPgmTotalUniqueNaks,
       "wfPgmTotalUniqueParityNaks": wfPgmTotalUniqueParityNaks,
       "wfPgmMaxNakRate": wfPgmMaxNakRate,
       "wfPgmIfTable": wfPgmIfTable,
       "wfPgmIfEntry": wfPgmIfEntry,
       "wfPgmIfCreate": wfPgmIfCreate,
       "wfPgmIfEnable": wfPgmIfEnable,
       "wfPgmIfState": wfPgmIfState,
       "wfPgmIfCct": wfPgmIfCct,
       "wfPgmIfNakReXmitInterval": wfPgmIfNakReXmitInterval,
       "wfPgmIfMaxNakReXmitRate": wfPgmIfMaxNakReXmitRate,
       "wfPgmIfNakRdataInterval": wfPgmIfNakRdataInterval,
       "wfPgmIfNakEliminateInterval": wfPgmIfNakEliminateInterval,
       "wfPgmIfTotalReXmitStates": wfPgmIfTotalReXmitStates,
       "wfPgmIfTotalReXmitTimedOut": wfPgmIfTotalReXmitTimedOut,
       "wfPgmIfInSpms": wfPgmIfInSpms,
       "wfPgmIfOutSpms": wfPgmIfOutSpms,
       "wfPgmIfInParitySpms": wfPgmIfInParitySpms,
       "wfPgmIfOutParitySpms": wfPgmIfOutParitySpms,
       "wfPgmIfInSpmPortErrors": wfPgmIfInSpmPortErrors,
       "wfPgmIfInRdata": wfPgmIfInRdata,
       "wfPgmIfOutRdata": wfPgmIfOutRdata,
       "wfPgmIfInParityRdata": wfPgmIfInParityRdata,
       "wfPgmIfOutParityRdata": wfPgmIfOutParityRdata,
       "wfPgmIfInRdataPortErrors": wfPgmIfInRdataPortErrors,
       "wfPgmIfInRdataNoSessionErrors": wfPgmIfInRdataNoSessionErrors,
       "wfPgmIfUniqueNaks": wfPgmIfUniqueNaks,
       "wfPgmIfInNaks": wfPgmIfInNaks,
       "wfPgmIfOutNaks": wfPgmIfOutNaks,
       "wfPgmIfUniqueParityNaks": wfPgmIfUniqueParityNaks,
       "wfPgmIfInParityNaks": wfPgmIfInParityNaks,
       "wfPgmIfOutParityNaks": wfPgmIfOutParityNaks,
       "wfPgmIfInNakPortErrors": wfPgmIfInNakPortErrors,
       "wfPgmIfInNakNoSessionErrors": wfPgmIfInNakNoSessionErrors,
       "wfPgmIfInNakSeqErrors": wfPgmIfInNakSeqErrors,
       "wfPgmIfInParityNakTgErrors": wfPgmIfInParityNakTgErrors,
       "wfPgmIfInNnaks": wfPgmIfInNnaks,
       "wfPgmIfOutNnaks": wfPgmIfOutNnaks,
       "wfPgmIfInParityNnaks": wfPgmIfInParityNnaks,
       "wfPgmIfOutParityNnaks": wfPgmIfOutParityNnaks,
       "wfPgmIfInNnakPortErrors": wfPgmIfInNnakPortErrors,
       "wfPgmIfInNnakNoSessionErrors": wfPgmIfInNnakNoSessionErrors,
       "wfPgmIfInNcfs": wfPgmIfInNcfs,
       "wfPgmIfOutNcfs": wfPgmIfOutNcfs,
       "wfPgmIfInParityNcfs": wfPgmIfInParityNcfs,
       "wfPgmIfOutParityNcfs": wfPgmIfOutParityNcfs,
       "wfPgmIfInNcfPortErrors": wfPgmIfInNcfPortErrors,
       "wfPgmIfInNcfNoSessionErrors": wfPgmIfInNcfNoSessionErrors,
       "wfPgmIfInRedirectNcfs": wfPgmIfInRedirectNcfs,
       "wfPgmSessionTable": wfPgmSessionTable,
       "wfPgmSessionEntry": wfPgmSessionEntry,
       "wfPgmSessionSource": wfPgmSessionSource,
       "wfPgmSessionGroup": wfPgmSessionGroup,
       "wfPgmSessionSourcePort": wfPgmSessionSourcePort,
       "wfPgmSessionGlobalId": wfPgmSessionGlobalId,
       "wfPgmSessionUpstreamAddress": wfPgmSessionUpstreamAddress,
       "wfPgmSessionUpstreamIfCct": wfPgmSessionUpstreamIfCct,
       "wfPgmSessionTrailEdgeSeq": wfPgmSessionTrailEdgeSeq,
       "wfPgmSessionIncrSeq": wfPgmSessionIncrSeq,
       "wfPgmSessionLeadEdgeSeq": wfPgmSessionLeadEdgeSeq,
       "wfPgmSessionInSpms": wfPgmSessionInSpms,
       "wfPgmSessionOutSpms": wfPgmSessionOutSpms,
       "wfPgmSessionInParitySpms": wfPgmSessionInParitySpms,
       "wfPgmSessionOutParitySpms": wfPgmSessionOutParitySpms,
       "wfPgmSessionTotalReXmitStates": wfPgmSessionTotalReXmitStates,
       "wfPgmSessionTotalReXmitTimedOut": wfPgmSessionTotalReXmitTimedOut,
       "wfPgmSessionInRdata": wfPgmSessionInRdata,
       "wfPgmSessionOutRdata": wfPgmSessionOutRdata,
       "wfPgmSessionInParityRdata": wfPgmSessionInParityRdata,
       "wfPgmSessionOutParityRdata": wfPgmSessionOutParityRdata,
       "wfPgmSessionInRdataNoStateErrors": wfPgmSessionInRdataNoStateErrors,
       "wfPgmSessionUniqueNaks": wfPgmSessionUniqueNaks,
       "wfPgmSessionInNaks": wfPgmSessionInNaks,
       "wfPgmSessionOutNaks": wfPgmSessionOutNaks,
       "wfPgmSessionUniqueParityNaks": wfPgmSessionUniqueParityNaks,
       "wfPgmSessionInParityNaks": wfPgmSessionInParityNaks,
       "wfPgmSessionOutParityNaks": wfPgmSessionOutParityNaks,
       "wfPgmSessionInNakSeqErrors": wfPgmSessionInNakSeqErrors,
       "wfPgmSessionInNnaks": wfPgmSessionInNnaks,
       "wfPgmSessionOutNnaks": wfPgmSessionOutNnaks,
       "wfPgmSessionInParityNnaks": wfPgmSessionInParityNnaks,
       "wfPgmSessionOutParityNnaks": wfPgmSessionOutParityNnaks,
       "wfPgmSessionInNcfs": wfPgmSessionInNcfs,
       "wfPgmSessionOutNcfs": wfPgmSessionOutNcfs,
       "wfPgmSessionInParityNcfs": wfPgmSessionInParityNcfs,
       "wfPgmSessionOutParityNcfs": wfPgmSessionOutParityNcfs,
       "wfPgmSessionInRedirectNcfs": wfPgmSessionInRedirectNcfs,
       "wfPgmReXmitTable": wfPgmReXmitTable,
       "wfPgmReXmitEntry": wfPgmReXmitEntry,
       "wfPgmReXmitSource": wfPgmReXmitSource,
       "wfPgmReXmitGroup": wfPgmReXmitGroup,
       "wfPgmReXmitSourcePort": wfPgmReXmitSourcePort,
       "wfPgmReXmitGlobalId": wfPgmReXmitGlobalId,
       "wfPgmReXmitSelectiveSeqNum": wfPgmReXmitSelectiveSeqNum,
       "wfPgmReXmitParityTgSeqNum": wfPgmReXmitParityTgSeqNum,
       "wfPgmReXmitReqParityTgCount": wfPgmReXmitReqParityTgCount,
       "wfPgmReXmitUpStreamCct": wfPgmReXmitUpStreamCct,
       "wfPgmReXmitDownStream": wfPgmReXmitDownStream}
)
