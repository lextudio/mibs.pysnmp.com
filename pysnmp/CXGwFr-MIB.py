# SNMP MIB module (CXGwFr-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXGwFr-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:30 2024
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
 SapIndex,
 cxGwFr) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxGwFr")

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

_GffSapTable_Object = MibTable
gffSapTable = _GffSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1)
)
if mibBuilder.loadTexts:
    gffSapTable.setStatus("mandatory")
_GffSapEntry_Object = MibTableRow
gffSapEntry = _GffSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1)
)
gffSapEntry.setIndexNames(
    (0, "CXGwFr-MIB", "gffSapId"),
)
if mibBuilder.loadTexts:
    gffSapEntry.setStatus("mandatory")
_GffSapId_Type = SapIndex
_GffSapId_Object = MibTableColumn
gffSapId = _GffSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 1),
    _GffSapId_Type()
)
gffSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gffSapId.setStatus("mandatory")


class _GffSapRowStatus_Type(Integer32):
    """Custom type gffSapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_GffSapRowStatus_Type.__name__ = "Integer32"
_GffSapRowStatus_Object = MibTableColumn
gffSapRowStatus = _GffSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 2),
    _GffSapRowStatus_Type()
)
gffSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapRowStatus.setStatus("mandatory")


class _GffSapType_Type(Integer32):
    """Custom type gffSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lower", 1),
          ("upper", 2))
    )


_GffSapType_Type.__name__ = "Integer32"
_GffSapType_Object = MibTableColumn
gffSapType = _GffSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 3),
    _GffSapType_Type()
)
gffSapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapType.setStatus("mandatory")
_GffSapAlias_Type = Alias
_GffSapAlias_Object = MibTableColumn
gffSapAlias = _GffSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 4),
    _GffSapAlias_Type()
)
gffSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapAlias.setStatus("mandatory")
_GffSapCompanionAlias_Type = Alias
_GffSapCompanionAlias_Object = MibTableColumn
gffSapCompanionAlias = _GffSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 5),
    _GffSapCompanionAlias_Type()
)
gffSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapCompanionAlias.setStatus("mandatory")


class _GffSapAssociatedSlotNo_Type(Integer32):
    """Custom type gffSapAssociatedSlotNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_GffSapAssociatedSlotNo_Type.__name__ = "Integer32"
_GffSapAssociatedSlotNo_Object = MibTableColumn
gffSapAssociatedSlotNo = _GffSapAssociatedSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 6),
    _GffSapAssociatedSlotNo_Type()
)
gffSapAssociatedSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapAssociatedSlotNo.setStatus("mandatory")


class _GffSapWindowWidth_Type(Integer32):
    """Custom type gffSapWindowWidth based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 100),
    )


_GffSapWindowWidth_Type.__name__ = "Integer32"
_GffSapWindowWidth_Object = MibTableColumn
gffSapWindowWidth = _GffSapWindowWidth_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 7),
    _GffSapWindowWidth_Type()
)
gffSapWindowWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapWindowWidth.setStatus("mandatory")


class _GffSapTrafficPriority_Type(Integer32):
    """Custom type gffSapTrafficPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_GffSapTrafficPriority_Type.__name__ = "Integer32"
_GffSapTrafficPriority_Object = MibTableColumn
gffSapTrafficPriority = _GffSapTrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 8),
    _GffSapTrafficPriority_Type()
)
gffSapTrafficPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapTrafficPriority.setStatus("mandatory")


class _GffSapMaxFrameSize_Type(Integer32):
    """Custom type gffSapMaxFrameSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8192),
    )


_GffSapMaxFrameSize_Type.__name__ = "Integer32"
_GffSapMaxFrameSize_Object = MibTableColumn
gffSapMaxFrameSize = _GffSapMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 18, 1, 1, 9),
    _GffSapMaxFrameSize_Type()
)
gffSapMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gffSapMaxFrameSize.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXGwFr-MIB",
    **{"gffSapTable": gffSapTable,
       "gffSapEntry": gffSapEntry,
       "gffSapId": gffSapId,
       "gffSapRowStatus": gffSapRowStatus,
       "gffSapType": gffSapType,
       "gffSapAlias": gffSapAlias,
       "gffSapCompanionAlias": gffSapCompanionAlias,
       "gffSapAssociatedSlotNo": gffSapAssociatedSlotNo,
       "gffSapWindowWidth": gffSapWindowWidth,
       "gffSapTrafficPriority": gffSapTrafficPriority,
       "gffSapMaxFrameSize": gffSapMaxFrameSize}
)
