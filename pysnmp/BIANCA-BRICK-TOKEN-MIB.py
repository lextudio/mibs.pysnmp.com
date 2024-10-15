# SNMP MIB module (BIANCA-BRICK-TOKEN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-TOKEN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:49 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class Date(Integer32):
    """Custom type Date based on Integer32"""




class HexValue(Integer32):
    """Custom type HexValue based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Tokenring_ObjectIdentity = ObjectIdentity
tokenring = _Tokenring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 11)
)
_TokenringIfTable_Object = MibTable
tokenringIfTable = _TokenringIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1)
)
if mibBuilder.loadTexts:
    tokenringIfTable.setStatus("mandatory")
_TokenringIfEntry_Object = MibTableRow
tokenringIfEntry = _TokenringIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1)
)
tokenringIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-TOKEN-MIB", "tokenringIfSlot"),
)
if mibBuilder.loadTexts:
    tokenringIfEntry.setStatus("mandatory")
_TokenringIfSlot_Type = Integer32
_TokenringIfSlot_Object = MibTableColumn
tokenringIfSlot = _TokenringIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 1),
    _TokenringIfSlot_Type()
)
tokenringIfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfSlot.setStatus("mandatory")


class _TokenringIfState_Type(Integer32):
    """Custom type tokenringIfState based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("bud", 5),
          ("close", 14),
          ("delay1", 10),
          ("done", 13),
          ("down", 1),
          ("download", 3),
          ("error", 15),
          ("open", 8),
          ("receive", 11),
          ("reset", 4),
          ("start", 2),
          ("tferipb", 6),
          ("wait1", 7),
          ("wait2", 9),
          ("wait3", 12))
    )


_TokenringIfState_Type.__name__ = "Integer32"
_TokenringIfState_Object = MibScalar
tokenringIfState = _TokenringIfState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 2),
    _TokenringIfState_Type()
)
tokenringIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfState.setStatus("mandatory")


class _TokenringIfRingRate_Type(Integer32):
    """Custom type tokenringIfRingRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tr-16Mbit", 2),
          ("tr-4Mbit", 1))
    )


_TokenringIfRingRate_Type.__name__ = "Integer32"
_TokenringIfRingRate_Object = MibTableColumn
tokenringIfRingRate = _TokenringIfRingRate_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 3),
    _TokenringIfRingRate_Type()
)
tokenringIfRingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenringIfRingRate.setStatus("mandatory")


class _TokenringIfEarlyTokenRelease_Type(Integer32):
    """Custom type tokenringIfEarlyTokenRelease based on Integer32"""
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


_TokenringIfEarlyTokenRelease_Type.__name__ = "Integer32"
_TokenringIfEarlyTokenRelease_Object = MibTableColumn
tokenringIfEarlyTokenRelease = _TokenringIfEarlyTokenRelease_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 4),
    _TokenringIfEarlyTokenRelease_Type()
)
tokenringIfEarlyTokenRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenringIfEarlyTokenRelease.setStatus("mandatory")


class _TokenringIfWrapInterface_Type(Integer32):
    """Custom type tokenringIfWrapInterface based on Integer32"""
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


_TokenringIfWrapInterface_Type.__name__ = "Integer32"
_TokenringIfWrapInterface_Object = MibTableColumn
tokenringIfWrapInterface = _TokenringIfWrapInterface_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 5),
    _TokenringIfWrapInterface_Type()
)
tokenringIfWrapInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenringIfWrapInterface.setStatus("mandatory")


class _TokenringIfMtu_Type(Integer32):
    """Custom type tokenringIfMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 17800),
    )


_TokenringIfMtu_Type.__name__ = "Integer32"
_TokenringIfMtu_Object = MibTableColumn
tokenringIfMtu = _TokenringIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 6),
    _TokenringIfMtu_Type()
)
tokenringIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenringIfMtu.setStatus("mandatory")
_TokenringIfOverwritePhysAddress_Type = PhysAddress
_TokenringIfOverwritePhysAddress_Object = MibTableColumn
tokenringIfOverwritePhysAddress = _TokenringIfOverwritePhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 7),
    _TokenringIfOverwritePhysAddress_Type()
)
tokenringIfOverwritePhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenringIfOverwritePhysAddress.setStatus("mandatory")
_TokenringIfNAUN_Type = PhysAddress
_TokenringIfNAUN_Object = MibTableColumn
tokenringIfNAUN = _TokenringIfNAUN_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 8),
    _TokenringIfNAUN_Type()
)
tokenringIfNAUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfNAUN.setStatus("mandatory")
_TokenringIfLineError_Type = Counter32
_TokenringIfLineError_Object = MibTableColumn
tokenringIfLineError = _TokenringIfLineError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 9),
    _TokenringIfLineError_Type()
)
tokenringIfLineError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfLineError.setStatus("mandatory")
_TokenringIfBurstError_Type = Counter32
_TokenringIfBurstError_Object = MibTableColumn
tokenringIfBurstError = _TokenringIfBurstError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 10),
    _TokenringIfBurstError_Type()
)
tokenringIfBurstError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfBurstError.setStatus("mandatory")
_TokenringIfAriFciError_Type = Counter32
_TokenringIfAriFciError_Object = MibTableColumn
tokenringIfAriFciError = _TokenringIfAriFciError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 11),
    _TokenringIfAriFciError_Type()
)
tokenringIfAriFciError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfAriFciError.setStatus("mandatory")
_TokenringIfLostFrameError_Type = Counter32
_TokenringIfLostFrameError_Object = MibTableColumn
tokenringIfLostFrameError = _TokenringIfLostFrameError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 12),
    _TokenringIfLostFrameError_Type()
)
tokenringIfLostFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfLostFrameError.setStatus("mandatory")
_TokenringIfReceiveCongestionError_Type = Counter32
_TokenringIfReceiveCongestionError_Object = MibTableColumn
tokenringIfReceiveCongestionError = _TokenringIfReceiveCongestionError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 13),
    _TokenringIfReceiveCongestionError_Type()
)
tokenringIfReceiveCongestionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfReceiveCongestionError.setStatus("mandatory")
_TokenringIfFrameCopiedError_Type = Counter32
_TokenringIfFrameCopiedError_Object = MibTableColumn
tokenringIfFrameCopiedError = _TokenringIfFrameCopiedError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 14),
    _TokenringIfFrameCopiedError_Type()
)
tokenringIfFrameCopiedError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfFrameCopiedError.setStatus("mandatory")
_TokenringIfTokenError_Type = Counter32
_TokenringIfTokenError_Object = MibTableColumn
tokenringIfTokenError = _TokenringIfTokenError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 15),
    _TokenringIfTokenError_Type()
)
tokenringIfTokenError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfTokenError.setStatus("mandatory")
_TokenringIfDmaBusError_Type = Counter32
_TokenringIfDmaBusError_Object = MibTableColumn
tokenringIfDmaBusError = _TokenringIfDmaBusError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 16),
    _TokenringIfDmaBusError_Type()
)
tokenringIfDmaBusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfDmaBusError.setStatus("mandatory")
_TokenringIfDmaParityError_Type = Counter32
_TokenringIfDmaParityError_Object = MibTableColumn
tokenringIfDmaParityError = _TokenringIfDmaParityError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 17),
    _TokenringIfDmaParityError_Type()
)
tokenringIfDmaParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfDmaParityError.setStatus("mandatory")
_TokenringIfSoftError_Type = Counter32
_TokenringIfSoftError_Object = MibTableColumn
tokenringIfSoftError = _TokenringIfSoftError_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 18),
    _TokenringIfSoftError_Type()
)
tokenringIfSoftError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenringIfSoftError.setStatus("mandatory")


class _TokenringIfSourceRouting_Type(Integer32):
    """Custom type tokenringIfSourceRouting based on Integer32"""
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


_TokenringIfSourceRouting_Type.__name__ = "Integer32"
_TokenringIfSourceRouting_Object = MibTableColumn
tokenringIfSourceRouting = _TokenringIfSourceRouting_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 11, 1, 1, 19),
    _TokenringIfSourceRouting_Type()
)
tokenringIfSourceRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenringIfSourceRouting.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-TOKEN-MIB",
    **{"Date": Date,
       "HexValue": HexValue,
       "org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "tokenring": tokenring,
       "tokenringIfTable": tokenringIfTable,
       "tokenringIfEntry": tokenringIfEntry,
       "tokenringIfSlot": tokenringIfSlot,
       "tokenringIfState": tokenringIfState,
       "tokenringIfRingRate": tokenringIfRingRate,
       "tokenringIfEarlyTokenRelease": tokenringIfEarlyTokenRelease,
       "tokenringIfWrapInterface": tokenringIfWrapInterface,
       "tokenringIfMtu": tokenringIfMtu,
       "tokenringIfOverwritePhysAddress": tokenringIfOverwritePhysAddress,
       "tokenringIfNAUN": tokenringIfNAUN,
       "tokenringIfLineError": tokenringIfLineError,
       "tokenringIfBurstError": tokenringIfBurstError,
       "tokenringIfAriFciError": tokenringIfAriFciError,
       "tokenringIfLostFrameError": tokenringIfLostFrameError,
       "tokenringIfReceiveCongestionError": tokenringIfReceiveCongestionError,
       "tokenringIfFrameCopiedError": tokenringIfFrameCopiedError,
       "tokenringIfTokenError": tokenringIfTokenError,
       "tokenringIfDmaBusError": tokenringIfDmaBusError,
       "tokenringIfDmaParityError": tokenringIfDmaParityError,
       "tokenringIfSoftError": tokenringIfSoftError,
       "tokenringIfSourceRouting": tokenringIfSourceRouting}
)
