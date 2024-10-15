# SNMP MIB module (CXT1E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXT1E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:53 2024
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

(cxT1E1,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxT1E1")

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

_T1e1CfgTable_Object = MibTable
t1e1CfgTable = _T1e1CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10)
)
if mibBuilder.loadTexts:
    t1e1CfgTable.setStatus("mandatory")
_T1e1CfgEntry_Object = MibTableRow
t1e1CfgEntry = _T1e1CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1)
)
t1e1CfgEntry.setIndexNames(
    (0, "CXT1E1-MIB", "t1e1CfgLinkIndex"),
)
if mibBuilder.loadTexts:
    t1e1CfgEntry.setStatus("mandatory")


class _T1e1CfgLinkIndex_Type(Integer32):
    """Custom type t1e1CfgLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_T1e1CfgLinkIndex_Type.__name__ = "Integer32"
_T1e1CfgLinkIndex_Object = MibTableColumn
t1e1CfgLinkIndex = _T1e1CfgLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 1),
    _T1e1CfgLinkIndex_Type()
)
t1e1CfgLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CfgLinkIndex.setStatus("mandatory")


class _T1e1CfgDebounce_Type(Integer32):
    """Custom type t1e1CfgDebounce based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_T1e1CfgDebounce_Type.__name__ = "Integer32"
_T1e1CfgDebounce_Object = MibTableColumn
t1e1CfgDebounce = _T1e1CfgDebounce_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 10),
    _T1e1CfgDebounce_Type()
)
t1e1CfgDebounce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1CfgDebounce.setStatus("mandatory")


class _T1e1CfgJitterAttenuator_Type(Integer32):
    """Custom type t1e1CfgJitterAttenuator based on Integer32"""
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
        *(("t1e1NoJitterAttenuator", 1),
          ("t1e1RxAttenuator128Bits", 3),
          ("t1e1RxAttenuator32Bits", 2),
          ("t1e1TxAttenuator128Bits", 5),
          ("t1e1TxAttenuator32Bits", 4))
    )


_T1e1CfgJitterAttenuator_Type.__name__ = "Integer32"
_T1e1CfgJitterAttenuator_Object = MibTableColumn
t1e1CfgJitterAttenuator = _T1e1CfgJitterAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 11),
    _T1e1CfgJitterAttenuator_Type()
)
t1e1CfgJitterAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1CfgJitterAttenuator.setStatus("mandatory")


class _T1e1CfgSyncCriteria_Type(Integer32):
    """Custom type t1e1CfgSyncCriteria based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_T1e1CfgSyncCriteria_Type.__name__ = "Integer32"
_T1e1CfgSyncCriteria_Object = MibTableColumn
t1e1CfgSyncCriteria = _T1e1CfgSyncCriteria_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 12),
    _T1e1CfgSyncCriteria_Type()
)
t1e1CfgSyncCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1CfgSyncCriteria.setStatus("mandatory")


class _T1e1CfgT1RxEqualizerGainLimit_Type(Integer32):
    """Custom type t1e1CfgT1RxEqualizerGainLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t1e1EGLHigh", 2),
          ("t1e1EGLLow", 1))
    )


_T1e1CfgT1RxEqualizerGainLimit_Type.__name__ = "Integer32"
_T1e1CfgT1RxEqualizerGainLimit_Object = MibTableColumn
t1e1CfgT1RxEqualizerGainLimit = _T1e1CfgT1RxEqualizerGainLimit_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 13),
    _T1e1CfgT1RxEqualizerGainLimit_Type()
)
t1e1CfgT1RxEqualizerGainLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t1e1CfgT1RxEqualizerGainLimit.setStatus("mandatory")


class _T1e1CfgT1RxLevel_Type(Integer32):
    """Custom type t1e1CfgT1RxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_T1e1CfgT1RxLevel_Type.__name__ = "Integer32"
_T1e1CfgT1RxLevel_Object = MibTableColumn
t1e1CfgT1RxLevel = _T1e1CfgT1RxLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 50),
    _T1e1CfgT1RxLevel_Type()
)
t1e1CfgT1RxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CfgT1RxLevel.setStatus("mandatory")
_T1e1CfgT1FrameAlignmentChange_Type = TimeTicks
_T1e1CfgT1FrameAlignmentChange_Object = MibTableColumn
t1e1CfgT1FrameAlignmentChange = _T1e1CfgT1FrameAlignmentChange_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 51),
    _T1e1CfgT1FrameAlignmentChange_Type()
)
t1e1CfgT1FrameAlignmentChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CfgT1FrameAlignmentChange.setStatus("mandatory")
_T1e1CfgT1JitterAttenuatorTrip_Type = TimeTicks
_T1e1CfgT1JitterAttenuatorTrip_Object = MibTableColumn
t1e1CfgT1JitterAttenuatorTrip = _T1e1CfgT1JitterAttenuatorTrip_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 8, 2, 10, 1, 52),
    _T1e1CfgT1JitterAttenuatorTrip_Type()
)
t1e1CfgT1JitterAttenuatorTrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1e1CfgT1JitterAttenuatorTrip.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXT1E1-MIB",
    **{"t1e1CfgTable": t1e1CfgTable,
       "t1e1CfgEntry": t1e1CfgEntry,
       "t1e1CfgLinkIndex": t1e1CfgLinkIndex,
       "t1e1CfgDebounce": t1e1CfgDebounce,
       "t1e1CfgJitterAttenuator": t1e1CfgJitterAttenuator,
       "t1e1CfgSyncCriteria": t1e1CfgSyncCriteria,
       "t1e1CfgT1RxEqualizerGainLimit": t1e1CfgT1RxEqualizerGainLimit,
       "t1e1CfgT1RxLevel": t1e1CfgT1RxLevel,
       "t1e1CfgT1FrameAlignmentChange": t1e1CfgT1FrameAlignmentChange,
       "t1e1CfgT1JitterAttenuatorTrip": t1e1CfgT1JitterAttenuatorTrip}
)
