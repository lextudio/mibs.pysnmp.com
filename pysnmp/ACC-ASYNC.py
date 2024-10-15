# SNMP MIB module (ACC-ASYNC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-ASYNC
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:47 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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

_AccAsync_ObjectIdentity = ObjectIdentity
accAsync = _AccAsync_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68)
)
_AccAsyncPortTable_Object = MibTable
accAsyncPortTable = _AccAsyncPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1)
)
if mibBuilder.loadTexts:
    accAsyncPortTable.setStatus("mandatory")
_AccAsyncPortEntry_Object = MibTableRow
accAsyncPortEntry = _AccAsyncPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1)
)
accAsyncPortEntry.setIndexNames(
    (0, "ACC-ASYNC", "accAsyncIndex"),
)
if mibBuilder.loadTexts:
    accAsyncPortEntry.setStatus("mandatory")
_AccAsyncIndex_Type = Integer32
_AccAsyncIndex_Object = MibTableColumn
accAsyncIndex = _AccAsyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1, 1),
    _AccAsyncIndex_Type()
)
accAsyncIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAsyncIndex.setStatus("mandatory")


class _AccAsyncState_Type(Integer32):
    """Custom type accAsyncState based on Integer32"""
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


_AccAsyncState_Type.__name__ = "Integer32"
_AccAsyncState_Object = MibTableColumn
accAsyncState = _AccAsyncState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1, 2),
    _AccAsyncState_Type()
)
accAsyncState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAsyncState.setStatus("mandatory")
_AccAsyncDataBits_Type = Integer32
_AccAsyncDataBits_Object = MibTableColumn
accAsyncDataBits = _AccAsyncDataBits_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1, 3),
    _AccAsyncDataBits_Type()
)
accAsyncDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAsyncDataBits.setStatus("mandatory")


class _AccAsyncParity_Type(Integer32):
    """Custom type accAsyncParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 1),
          ("none", 3),
          ("odd", 2))
    )


_AccAsyncParity_Type.__name__ = "Integer32"
_AccAsyncParity_Object = MibTableColumn
accAsyncParity = _AccAsyncParity_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1, 4),
    _AccAsyncParity_Type()
)
accAsyncParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAsyncParity.setStatus("mandatory")
_AccAsyncStopBits_Type = Integer32
_AccAsyncStopBits_Object = MibTableColumn
accAsyncStopBits = _AccAsyncStopBits_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1, 5),
    _AccAsyncStopBits_Type()
)
accAsyncStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAsyncStopBits.setStatus("mandatory")
_AccAsyncMinChar_Type = Integer32
_AccAsyncMinChar_Object = MibTableColumn
accAsyncMinChar = _AccAsyncMinChar_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1, 6),
    _AccAsyncMinChar_Type()
)
accAsyncMinChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAsyncMinChar.setStatus("mandatory")
_AccAsyncMaxIdle_Type = Integer32
_AccAsyncMaxIdle_Object = MibTableColumn
accAsyncMaxIdle = _AccAsyncMaxIdle_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 1, 1, 7),
    _AccAsyncMaxIdle_Type()
)
accAsyncMaxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accAsyncMaxIdle.setStatus("mandatory")
_AccAsyncStatTable_Object = MibTable
accAsyncStatTable = _AccAsyncStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2)
)
if mibBuilder.loadTexts:
    accAsyncStatTable.setStatus("mandatory")
_AccAsyncStatEntry_Object = MibTableRow
accAsyncStatEntry = _AccAsyncStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2, 1)
)
accAsyncStatEntry.setIndexNames(
    (0, "ACC-ASYNC", "accAsyncIndex"),
)
if mibBuilder.loadTexts:
    accAsyncStatEntry.setStatus("mandatory")
_AccAsyncUnderruns_Type = Counter32
_AccAsyncUnderruns_Object = MibTableColumn
accAsyncUnderruns = _AccAsyncUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2, 1, 1),
    _AccAsyncUnderruns_Type()
)
accAsyncUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAsyncUnderruns.setStatus("mandatory")
_AccAsyncOverruns_Type = Counter32
_AccAsyncOverruns_Object = MibTableColumn
accAsyncOverruns = _AccAsyncOverruns_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2, 1, 2),
    _AccAsyncOverruns_Type()
)
accAsyncOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAsyncOverruns.setStatus("mandatory")
_AccAsyncFrmErrs_Type = Counter32
_AccAsyncFrmErrs_Object = MibTableColumn
accAsyncFrmErrs = _AccAsyncFrmErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2, 1, 3),
    _AccAsyncFrmErrs_Type()
)
accAsyncFrmErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAsyncFrmErrs.setStatus("mandatory")
_AccAsyncParErrs_Type = Counter32
_AccAsyncParErrs_Object = MibTableColumn
accAsyncParErrs = _AccAsyncParErrs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2, 1, 4),
    _AccAsyncParErrs_Type()
)
accAsyncParErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAsyncParErrs.setStatus("mandatory")
_AccAsyncCarrierLosts_Type = Counter32
_AccAsyncCarrierLosts_Object = MibTableColumn
accAsyncCarrierLosts = _AccAsyncCarrierLosts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2, 1, 5),
    _AccAsyncCarrierLosts_Type()
)
accAsyncCarrierLosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAsyncCarrierLosts.setStatus("mandatory")
_AccAsyncBreaks_Type = Counter32
_AccAsyncBreaks_Object = MibTableColumn
accAsyncBreaks = _AccAsyncBreaks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 68, 2, 1, 6),
    _AccAsyncBreaks_Type()
)
accAsyncBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accAsyncBreaks.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-ASYNC",
    **{"accAsync": accAsync,
       "accAsyncPortTable": accAsyncPortTable,
       "accAsyncPortEntry": accAsyncPortEntry,
       "accAsyncIndex": accAsyncIndex,
       "accAsyncState": accAsyncState,
       "accAsyncDataBits": accAsyncDataBits,
       "accAsyncParity": accAsyncParity,
       "accAsyncStopBits": accAsyncStopBits,
       "accAsyncMinChar": accAsyncMinChar,
       "accAsyncMaxIdle": accAsyncMaxIdle,
       "accAsyncStatTable": accAsyncStatTable,
       "accAsyncStatEntry": accAsyncStatEntry,
       "accAsyncUnderruns": accAsyncUnderruns,
       "accAsyncOverruns": accAsyncOverruns,
       "accAsyncFrmErrs": accAsyncFrmErrs,
       "accAsyncParErrs": accAsyncParErrs,
       "accAsyncCarrierLosts": accAsyncCarrierLosts,
       "accAsyncBreaks": accAsyncBreaks}
)
