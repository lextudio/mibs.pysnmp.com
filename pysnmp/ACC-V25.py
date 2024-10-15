# SNMP MIB module (ACC-V25) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-V25
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:10 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccV25_ObjectIdentity = ObjectIdentity
accV25 = _AccV25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37)
)
_AccV25StatTable_Object = MibTable
accV25StatTable = _AccV25StatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1)
)
if mibBuilder.loadTexts:
    accV25StatTable.setStatus("mandatory")
_AccV25StatEntry_Object = MibTableRow
accV25StatEntry = _AccV25StatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1)
)
accV25StatEntry.setIndexNames(
    (0, "ACC-V25", "accV25IntIndex"),
)
if mibBuilder.loadTexts:
    accV25StatEntry.setStatus("mandatory")
_AccV25IntIndex_Type = Integer32
_AccV25IntIndex_Object = MibTableColumn
accV25IntIndex = _AccV25IntIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 1),
    _AccV25IntIndex_Type()
)
accV25IntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25IntIndex.setStatus("mandatory")


class _AccV25CurState_Type(Integer32):
    """Custom type accV25CurState based on Integer32"""
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
        *(("call-connected", 5),
          ("clear-by-dte", 7),
          ("data-transfer", 6),
          ("dialogue", 3),
          ("dialogue-pending", 2),
          ("dte-not-ready", 1),
          ("handshaking", 4))
    )


_AccV25CurState_Type.__name__ = "Integer32"
_AccV25CurState_Object = MibTableColumn
accV25CurState = _AccV25CurState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 2),
    _AccV25CurState_Type()
)
accV25CurState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CurState.setStatus("mandatory")


class _AccV25DTRSignal_Type(Integer32):
    """Custom type accV25DTRSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccV25DTRSignal_Type.__name__ = "Integer32"
_AccV25DTRSignal_Object = MibTableColumn
accV25DTRSignal = _AccV25DTRSignal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 3),
    _AccV25DTRSignal_Type()
)
accV25DTRSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25DTRSignal.setStatus("mandatory")


class _AccV25DSRSignal_Type(Integer32):
    """Custom type accV25DSRSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccV25DSRSignal_Type.__name__ = "Integer32"
_AccV25DSRSignal_Object = MibTableColumn
accV25DSRSignal = _AccV25DSRSignal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 4),
    _AccV25DSRSignal_Type()
)
accV25DSRSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25DSRSignal.setStatus("mandatory")


class _AccV25CTSSignal_Type(Integer32):
    """Custom type accV25CTSSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccV25CTSSignal_Type.__name__ = "Integer32"
_AccV25CTSSignal_Object = MibTableColumn
accV25CTSSignal = _AccV25CTSSignal_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 5),
    _AccV25CTSSignal_Type()
)
accV25CTSSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CTSSignal.setStatus("mandatory")
_AccV25CallAttempts_Type = Integer32
_AccV25CallAttempts_Object = MibTableColumn
accV25CallAttempts = _AccV25CallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 6),
    _AccV25CallAttempts_Type()
)
accV25CallAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CallAttempts.setStatus("mandatory")
_AccV25CallSuccess_Type = Integer32
_AccV25CallSuccess_Object = MibTableColumn
accV25CallSuccess = _AccV25CallSuccess_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 37, 1, 1, 7),
    _AccV25CallSuccess_Type()
)
accV25CallSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accV25CallSuccess.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-V25",
    **{"accV25": accV25,
       "accV25StatTable": accV25StatTable,
       "accV25StatEntry": accV25StatEntry,
       "accV25IntIndex": accV25IntIndex,
       "accV25CurState": accV25CurState,
       "accV25DTRSignal": accV25DTRSignal,
       "accV25DSRSignal": accV25DSRSignal,
       "accV25CTSSignal": accV25CTSSignal,
       "accV25CallAttempts": accV25CallAttempts,
       "accV25CallSuccess": accV25CallSuccess}
)
