# SNMP MIB module (CXTRDIo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXTRDIo-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:54 2024
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

(Alias,
 cxTrdIo) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxTrdIo")

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

_TrdSapOprTable_Object = MibTable
trdSapOprTable = _TrdSapOprTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1)
)
if mibBuilder.loadTexts:
    trdSapOprTable.setStatus("mandatory")
_TrdSapOprEntry_Object = MibTableRow
trdSapOprEntry = _TrdSapOprEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1)
)
trdSapOprEntry.setIndexNames(
    (0, "CXTRDIo-MIB", "trdSapOprNumber"),
)
if mibBuilder.loadTexts:
    trdSapOprEntry.setStatus("mandatory")
_TrdSapOprNumber_Type = Integer32
_TrdSapOprNumber_Object = MibTableColumn
trdSapOprNumber = _TrdSapOprNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 1),
    _TrdSapOprNumber_Type()
)
trdSapOprNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdSapOprNumber.setStatus("mandatory")
_TrdSapOprAlias_Type = Alias
_TrdSapOprAlias_Object = MibTableColumn
trdSapOprAlias = _TrdSapOprAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 2),
    _TrdSapOprAlias_Type()
)
trdSapOprAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdSapOprAlias.setStatus("mandatory")


class _TrdSapOprPortSpeed_Type(Integer32):
    """Custom type trdSapOprPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-16-mbps", 2),
          ("speed-4-mbps", 1))
    )


_TrdSapOprPortSpeed_Type.__name__ = "Integer32"
_TrdSapOprPortSpeed_Object = MibTableColumn
trdSapOprPortSpeed = _TrdSapOprPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 3),
    _TrdSapOprPortSpeed_Type()
)
trdSapOprPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdSapOprPortSpeed.setStatus("mandatory")


class _TrdSapOprTxBufferQueue_Type(Integer32):
    """Custom type trdSapOprTxBufferQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 240),
    )


_TrdSapOprTxBufferQueue_Type.__name__ = "Integer32"
_TrdSapOprTxBufferQueue_Object = MibTableColumn
trdSapOprTxBufferQueue = _TrdSapOprTxBufferQueue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 4),
    _TrdSapOprTxBufferQueue_Type()
)
trdSapOprTxBufferQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdSapOprTxBufferQueue.setStatus("mandatory")


class _TrdSapOprRxBufferQueue_Type(Integer32):
    """Custom type trdSapOprRxBufferQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 240),
    )


_TrdSapOprRxBufferQueue_Type.__name__ = "Integer32"
_TrdSapOprRxBufferQueue_Object = MibTableColumn
trdSapOprRxBufferQueue = _TrdSapOprRxBufferQueue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 5),
    _TrdSapOprRxBufferQueue_Type()
)
trdSapOprRxBufferQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdSapOprRxBufferQueue.setStatus("mandatory")


class _TrdSapOprDataGenerator_Type(Integer32):
    """Custom type trdSapOprDataGenerator based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-verify", 3),
          ("retrigger", 4))
    )


_TrdSapOprDataGenerator_Type.__name__ = "Integer32"
_TrdSapOprDataGenerator_Object = MibTableColumn
trdSapOprDataGenerator = _TrdSapOprDataGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 8),
    _TrdSapOprDataGenerator_Type()
)
trdSapOprDataGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapOprDataGenerator.setStatus("mandatory")
_TrdSapOprGenFrames_Type = Integer32
_TrdSapOprGenFrames_Object = MibTableColumn
trdSapOprGenFrames = _TrdSapOprGenFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 9),
    _TrdSapOprGenFrames_Type()
)
trdSapOprGenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapOprGenFrames.setStatus("mandatory")
_TrdSapOprGenFrameSize_Type = Integer32
_TrdSapOprGenFrameSize_Object = MibTableColumn
trdSapOprGenFrameSize = _TrdSapOprGenFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 10),
    _TrdSapOprGenFrameSize_Type()
)
trdSapOprGenFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapOprGenFrameSize.setStatus("mandatory")


class _TrdOprControlStats_Type(Integer32):
    """Custom type trdOprControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearSapStats", 1)
    )


_TrdOprControlStats_Type.__name__ = "Integer32"
_TrdOprControlStats_Object = MibTableColumn
trdOprControlStats = _TrdOprControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 15),
    _TrdOprControlStats_Type()
)
trdOprControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    trdOprControlStats.setStatus("mandatory")
_TrdStatOprRxGenErrors_Type = Counter32
_TrdStatOprRxGenErrors_Object = MibTableColumn
trdStatOprRxGenErrors = _TrdStatOprRxGenErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 17),
    _TrdStatOprRxGenErrors_Type()
)
trdStatOprRxGenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdStatOprRxGenErrors.setStatus("mandatory")
_TrdSapAdmTable_Object = MibTable
trdSapAdmTable = _TrdSapAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2)
)
if mibBuilder.loadTexts:
    trdSapAdmTable.setStatus("mandatory")
_TrdSapAdmEntry_Object = MibTableRow
trdSapAdmEntry = _TrdSapAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1)
)
trdSapAdmEntry.setIndexNames(
    (0, "CXTRDIo-MIB", "trdSapAdmNumber"),
)
if mibBuilder.loadTexts:
    trdSapAdmEntry.setStatus("mandatory")
_TrdSapAdmNumber_Type = Integer32
_TrdSapAdmNumber_Object = MibTableColumn
trdSapAdmNumber = _TrdSapAdmNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 1),
    _TrdSapAdmNumber_Type()
)
trdSapAdmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trdSapAdmNumber.setStatus("mandatory")
_TrdSapAdmAlias_Type = Alias
_TrdSapAdmAlias_Object = MibTableColumn
trdSapAdmAlias = _TrdSapAdmAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 2),
    _TrdSapAdmAlias_Type()
)
trdSapAdmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapAdmAlias.setStatus("mandatory")


class _TrdSapAdmPortSpeed_Type(Integer32):
    """Custom type trdSapAdmPortSpeed based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-16-mbps", 2),
          ("speed-4-mbps", 1))
    )


_TrdSapAdmPortSpeed_Type.__name__ = "Integer32"
_TrdSapAdmPortSpeed_Object = MibTableColumn
trdSapAdmPortSpeed = _TrdSapAdmPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 3),
    _TrdSapAdmPortSpeed_Type()
)
trdSapAdmPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapAdmPortSpeed.setStatus("mandatory")


class _TrdSapAdmTxBufferQueue_Type(Integer32):
    """Custom type trdSapAdmTxBufferQueue based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 240),
    )


_TrdSapAdmTxBufferQueue_Type.__name__ = "Integer32"
_TrdSapAdmTxBufferQueue_Object = MibTableColumn
trdSapAdmTxBufferQueue = _TrdSapAdmTxBufferQueue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 4),
    _TrdSapAdmTxBufferQueue_Type()
)
trdSapAdmTxBufferQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapAdmTxBufferQueue.setStatus("mandatory")


class _TrdSapAdmRxBufferQueue_Type(Integer32):
    """Custom type trdSapAdmRxBufferQueue based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 240),
    )


_TrdSapAdmRxBufferQueue_Type.__name__ = "Integer32"
_TrdSapAdmRxBufferQueue_Object = MibTableColumn
trdSapAdmRxBufferQueue = _TrdSapAdmRxBufferQueue_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 5),
    _TrdSapAdmRxBufferQueue_Type()
)
trdSapAdmRxBufferQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapAdmRxBufferQueue.setStatus("mandatory")


class _TrdSapAdmDataGenerator_Type(Integer32):
    """Custom type trdSapAdmDataGenerator based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabled-verify", 3))
    )


_TrdSapAdmDataGenerator_Type.__name__ = "Integer32"
_TrdSapAdmDataGenerator_Object = MibTableColumn
trdSapAdmDataGenerator = _TrdSapAdmDataGenerator_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 8),
    _TrdSapAdmDataGenerator_Type()
)
trdSapAdmDataGenerator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapAdmDataGenerator.setStatus("mandatory")


class _TrdSapAdmGenFrames_Type(Integer32):
    """Custom type trdSapAdmGenFrames based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TrdSapAdmGenFrames_Type.__name__ = "Integer32"
_TrdSapAdmGenFrames_Object = MibTableColumn
trdSapAdmGenFrames = _TrdSapAdmGenFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 9),
    _TrdSapAdmGenFrames_Type()
)
trdSapAdmGenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapAdmGenFrames.setStatus("mandatory")


class _TrdSapAdmGenFrameSize_Type(Integer32):
    """Custom type trdSapAdmGenFrameSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 2100),
    )


_TrdSapAdmGenFrameSize_Type.__name__ = "Integer32"
_TrdSapAdmGenFrameSize_Object = MibTableColumn
trdSapAdmGenFrameSize = _TrdSapAdmGenFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 10),
    _TrdSapAdmGenFrameSize_Type()
)
trdSapAdmGenFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trdSapAdmGenFrameSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXTRDIo-MIB",
    **{"trdSapOprTable": trdSapOprTable,
       "trdSapOprEntry": trdSapOprEntry,
       "trdSapOprNumber": trdSapOprNumber,
       "trdSapOprAlias": trdSapOprAlias,
       "trdSapOprPortSpeed": trdSapOprPortSpeed,
       "trdSapOprTxBufferQueue": trdSapOprTxBufferQueue,
       "trdSapOprRxBufferQueue": trdSapOprRxBufferQueue,
       "trdSapOprDataGenerator": trdSapOprDataGenerator,
       "trdSapOprGenFrames": trdSapOprGenFrames,
       "trdSapOprGenFrameSize": trdSapOprGenFrameSize,
       "trdOprControlStats": trdOprControlStats,
       "trdStatOprRxGenErrors": trdStatOprRxGenErrors,
       "trdSapAdmTable": trdSapAdmTable,
       "trdSapAdmEntry": trdSapAdmEntry,
       "trdSapAdmNumber": trdSapAdmNumber,
       "trdSapAdmAlias": trdSapAdmAlias,
       "trdSapAdmPortSpeed": trdSapAdmPortSpeed,
       "trdSapAdmTxBufferQueue": trdSapAdmTxBufferQueue,
       "trdSapAdmRxBufferQueue": trdSapAdmRxBufferQueue,
       "trdSapAdmDataGenerator": trdSapAdmDataGenerator,
       "trdSapAdmGenFrames": trdSapAdmGenFrames,
       "trdSapAdmGenFrameSize": trdSapAdmGenFrameSize}
)
