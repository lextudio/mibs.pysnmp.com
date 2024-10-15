# SNMP MIB module (TERAWAVE-teraCAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraCAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:14 2024
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
 enterprises,
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
    "enterprises",
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

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraCACGroup_ObjectIdentity = ObjectIdentity
teraCACGroup = _TeraCACGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 19)
)
_TeraCACSystemTablePar_ObjectIdentity = ObjectIdentity
teraCACSystemTablePar = _TeraCACSystemTablePar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 19, 1)
)
_TeraCACSystemTable_ObjectIdentity = ObjectIdentity
teraCACSystemTable = _TeraCACSystemTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 19, 1, 1)
)


class _TeraLevel1UseSlotNumber_Type(Integer32):
    """Custom type teraLevel1UseSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TeraLevel1UseSlotNumber_Type.__name__ = "Integer32"
_TeraLevel1UseSlotNumber_Object = MibScalar
teraLevel1UseSlotNumber = _TeraLevel1UseSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 1, 1, 1),
    _TeraLevel1UseSlotNumber_Type()
)
teraLevel1UseSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UseSlotNumber.setStatus("mandatory")


class _TeraUsePonIndex_Type(Integer32):
    """Custom type teraUsePonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 33),
    )


_TeraUsePonIndex_Type.__name__ = "Integer32"
_TeraUsePonIndex_Object = MibScalar
teraUsePonIndex = _TeraUsePonIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 1, 1, 2),
    _TeraUsePonIndex_Type()
)
teraUsePonIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUsePonIndex.setStatus("mandatory")


class _TeraLevel2UseSlotNumber_Type(Integer32):
    """Custom type teraLevel2UseSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TeraLevel2UseSlotNumber_Type.__name__ = "Integer32"
_TeraLevel2UseSlotNumber_Object = MibScalar
teraLevel2UseSlotNumber = _TeraLevel2UseSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 1, 1, 3),
    _TeraLevel2UseSlotNumber_Type()
)
teraLevel2UseSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UseSlotNumber.setStatus("mandatory")
_TeraCACTablePar_ObjectIdentity = ObjectIdentity
teraCACTablePar = _TeraCACTablePar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2)
)
_TeraCACTable_ObjectIdentity = ObjectIdentity
teraCACTable = _TeraCACTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1)
)


class _TeraCACUpWeightrtVBR_Type(Integer32):
    """Custom type teraCACUpWeightrtVBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightrtVBR_Type.__name__ = "Integer32"
_TeraCACUpWeightrtVBR_Object = MibScalar
teraCACUpWeightrtVBR = _TeraCACUpWeightrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 1),
    _TeraCACUpWeightrtVBR_Type()
)
teraCACUpWeightrtVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightrtVBR.setStatus("mandatory")


class _TeraCACUpWeightrtVBRpeak_Type(Integer32):
    """Custom type teraCACUpWeightrtVBRpeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightrtVBRpeak_Type.__name__ = "Integer32"
_TeraCACUpWeightrtVBRpeak_Object = MibScalar
teraCACUpWeightrtVBRpeak = _TeraCACUpWeightrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 2),
    _TeraCACUpWeightrtVBRpeak_Type()
)
teraCACUpWeightrtVBRpeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightrtVBRpeak.setStatus("mandatory")


class _TeraCACUpWeightnrtVBR_Type(Integer32):
    """Custom type teraCACUpWeightnrtVBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightnrtVBR_Type.__name__ = "Integer32"
_TeraCACUpWeightnrtVBR_Object = MibScalar
teraCACUpWeightnrtVBR = _TeraCACUpWeightnrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 3),
    _TeraCACUpWeightnrtVBR_Type()
)
teraCACUpWeightnrtVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightnrtVBR.setStatus("mandatory")


class _TeraCACUpWeightnrtVBRpeak_Type(Integer32):
    """Custom type teraCACUpWeightnrtVBRpeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightnrtVBRpeak_Type.__name__ = "Integer32"
_TeraCACUpWeightnrtVBRpeak_Object = MibScalar
teraCACUpWeightnrtVBRpeak = _TeraCACUpWeightnrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 4),
    _TeraCACUpWeightnrtVBRpeak_Type()
)
teraCACUpWeightnrtVBRpeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightnrtVBRpeak.setStatus("mandatory")


class _TeraCACUpWeightUBR_Type(Integer32):
    """Custom type teraCACUpWeightUBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightUBR_Type.__name__ = "Integer32"
_TeraCACUpWeightUBR_Object = MibScalar
teraCACUpWeightUBR = _TeraCACUpWeightUBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 5),
    _TeraCACUpWeightUBR_Type()
)
teraCACUpWeightUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightUBR.setStatus("mandatory")


class _TeraCACUpWeightUBRMcr_Type(Integer32):
    """Custom type teraCACUpWeightUBRMcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightUBRMcr_Type.__name__ = "Integer32"
_TeraCACUpWeightUBRMcr_Object = MibScalar
teraCACUpWeightUBRMcr = _TeraCACUpWeightUBRMcr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 6),
    _TeraCACUpWeightUBRMcr_Type()
)
teraCACUpWeightUBRMcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightUBRMcr.setStatus("mandatory")


class _TeraCACUpWeightMeshGuar_Type(Integer32):
    """Custom type teraCACUpWeightMeshGuar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightMeshGuar_Type.__name__ = "Integer32"
_TeraCACUpWeightMeshGuar_Object = MibScalar
teraCACUpWeightMeshGuar = _TeraCACUpWeightMeshGuar_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 7),
    _TeraCACUpWeightMeshGuar_Type()
)
teraCACUpWeightMeshGuar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightMeshGuar.setStatus("mandatory")


class _TeraCACUpWeightMeshMax_Type(Integer32):
    """Custom type teraCACUpWeightMeshMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACUpWeightMeshMax_Type.__name__ = "Integer32"
_TeraCACUpWeightMeshMax_Object = MibScalar
teraCACUpWeightMeshMax = _TeraCACUpWeightMeshMax_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 8),
    _TeraCACUpWeightMeshMax_Type()
)
teraCACUpWeightMeshMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACUpWeightMeshMax.setStatus("mandatory")


class _TeraCACDownWeightrtVBR_Type(Integer32):
    """Custom type teraCACDownWeightrtVBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightrtVBR_Type.__name__ = "Integer32"
_TeraCACDownWeightrtVBR_Object = MibScalar
teraCACDownWeightrtVBR = _TeraCACDownWeightrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 9),
    _TeraCACDownWeightrtVBR_Type()
)
teraCACDownWeightrtVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightrtVBR.setStatus("mandatory")


class _TeraCACDownWeightrtVBRpeak_Type(Integer32):
    """Custom type teraCACDownWeightrtVBRpeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightrtVBRpeak_Type.__name__ = "Integer32"
_TeraCACDownWeightrtVBRpeak_Object = MibScalar
teraCACDownWeightrtVBRpeak = _TeraCACDownWeightrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 10),
    _TeraCACDownWeightrtVBRpeak_Type()
)
teraCACDownWeightrtVBRpeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightrtVBRpeak.setStatus("mandatory")


class _TeraCACDownWeightnrtVBR_Type(Integer32):
    """Custom type teraCACDownWeightnrtVBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightnrtVBR_Type.__name__ = "Integer32"
_TeraCACDownWeightnrtVBR_Object = MibScalar
teraCACDownWeightnrtVBR = _TeraCACDownWeightnrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 11),
    _TeraCACDownWeightnrtVBR_Type()
)
teraCACDownWeightnrtVBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightnrtVBR.setStatus("mandatory")


class _TeraCACDownWeightnrtVBRpeak_Type(Integer32):
    """Custom type teraCACDownWeightnrtVBRpeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightnrtVBRpeak_Type.__name__ = "Integer32"
_TeraCACDownWeightnrtVBRpeak_Object = MibScalar
teraCACDownWeightnrtVBRpeak = _TeraCACDownWeightnrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 12),
    _TeraCACDownWeightnrtVBRpeak_Type()
)
teraCACDownWeightnrtVBRpeak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightnrtVBRpeak.setStatus("mandatory")


class _TeraCACDownWeightUBR_Type(Integer32):
    """Custom type teraCACDownWeightUBR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightUBR_Type.__name__ = "Integer32"
_TeraCACDownWeightUBR_Object = MibScalar
teraCACDownWeightUBR = _TeraCACDownWeightUBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 13),
    _TeraCACDownWeightUBR_Type()
)
teraCACDownWeightUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightUBR.setStatus("mandatory")


class _TeraCACDownWeightUBRMcr_Type(Integer32):
    """Custom type teraCACDownWeightUBRMcr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightUBRMcr_Type.__name__ = "Integer32"
_TeraCACDownWeightUBRMcr_Object = MibScalar
teraCACDownWeightUBRMcr = _TeraCACDownWeightUBRMcr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 14),
    _TeraCACDownWeightUBRMcr_Type()
)
teraCACDownWeightUBRMcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightUBRMcr.setStatus("mandatory")


class _TeraCACDownWeightMeshGuar_Type(Integer32):
    """Custom type teraCACDownWeightMeshGuar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightMeshGuar_Type.__name__ = "Integer32"
_TeraCACDownWeightMeshGuar_Object = MibScalar
teraCACDownWeightMeshGuar = _TeraCACDownWeightMeshGuar_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 15),
    _TeraCACDownWeightMeshGuar_Type()
)
teraCACDownWeightMeshGuar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightMeshGuar.setStatus("mandatory")


class _TeraCACDownWeightMeshMax_Type(Integer32):
    """Custom type teraCACDownWeightMeshMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_TeraCACDownWeightMeshMax_Type.__name__ = "Integer32"
_TeraCACDownWeightMeshMax_Object = MibScalar
teraCACDownWeightMeshMax = _TeraCACDownWeightMeshMax_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 2, 1, 16),
    _TeraCACDownWeightMeshMax_Type()
)
teraCACDownWeightMeshMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraCACDownWeightMeshMax.setStatus("mandatory")
_TeraLevel1UseUpStreamTable_Object = MibTable
teraLevel1UseUpStreamTable = _TeraLevel1UseUpStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3)
)
if mibBuilder.loadTexts:
    teraLevel1UseUpStreamTable.setStatus("mandatory")
_TeraLevel1UseUpStreamTableEntry_Object = MibTableRow
teraLevel1UseUpStreamTableEntry = _TeraLevel1UseUpStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1)
)
teraLevel1UseUpStreamTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCAC-MIB", "teraLevel1UseSlotNumber"),
)
if mibBuilder.loadTexts:
    teraLevel1UseUpStreamTableEntry.setStatus("mandatory")
_TeraLevel1UpStreamCBR_Type = Integer32
_TeraLevel1UpStreamCBR_Object = MibTableColumn
teraLevel1UpStreamCBR = _TeraLevel1UpStreamCBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 1),
    _TeraLevel1UpStreamCBR_Type()
)
teraLevel1UpStreamCBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamCBR.setStatus("mandatory")
_TeraLevel1UpStreamrtVBR_Type = Integer32
_TeraLevel1UpStreamrtVBR_Object = MibTableColumn
teraLevel1UpStreamrtVBR = _TeraLevel1UpStreamrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 2),
    _TeraLevel1UpStreamrtVBR_Type()
)
teraLevel1UpStreamrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamrtVBR.setStatus("mandatory")
_TeraLevel1UpStreamrtVBRpeak_Type = Integer32
_TeraLevel1UpStreamrtVBRpeak_Object = MibTableColumn
teraLevel1UpStreamrtVBRpeak = _TeraLevel1UpStreamrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 3),
    _TeraLevel1UpStreamrtVBRpeak_Type()
)
teraLevel1UpStreamrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamrtVBRpeak.setStatus("mandatory")
_TeraLevel1UpStreamnrtVBR_Type = Integer32
_TeraLevel1UpStreamnrtVBR_Object = MibTableColumn
teraLevel1UpStreamnrtVBR = _TeraLevel1UpStreamnrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 4),
    _TeraLevel1UpStreamnrtVBR_Type()
)
teraLevel1UpStreamnrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamnrtVBR.setStatus("mandatory")
_TeraLevel1UpStreamnrtVBRpeak_Type = Integer32
_TeraLevel1UpStreamnrtVBRpeak_Object = MibTableColumn
teraLevel1UpStreamnrtVBRpeak = _TeraLevel1UpStreamnrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 5),
    _TeraLevel1UpStreamnrtVBRpeak_Type()
)
teraLevel1UpStreamnrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamnrtVBRpeak.setStatus("mandatory")
_TeraLevel1UpStreamUBR_Type = Integer32
_TeraLevel1UpStreamUBR_Object = MibTableColumn
teraLevel1UpStreamUBR = _TeraLevel1UpStreamUBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 6),
    _TeraLevel1UpStreamUBR_Type()
)
teraLevel1UpStreamUBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamUBR.setStatus("mandatory")
_TeraLevel1UpStreamUBRMcr_Type = Integer32
_TeraLevel1UpStreamUBRMcr_Object = MibTableColumn
teraLevel1UpStreamUBRMcr = _TeraLevel1UpStreamUBRMcr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 7),
    _TeraLevel1UpStreamUBRMcr_Type()
)
teraLevel1UpStreamUBRMcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamUBRMcr.setStatus("mandatory")
_TeraLevel1UpStreamMeshGuar_Type = Integer32
_TeraLevel1UpStreamMeshGuar_Object = MibTableColumn
teraLevel1UpStreamMeshGuar = _TeraLevel1UpStreamMeshGuar_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 8),
    _TeraLevel1UpStreamMeshGuar_Type()
)
teraLevel1UpStreamMeshGuar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamMeshGuar.setStatus("mandatory")
_TeraLevel1UpStreamMeshMax_Type = Integer32
_TeraLevel1UpStreamMeshMax_Object = MibTableColumn
teraLevel1UpStreamMeshMax = _TeraLevel1UpStreamMeshMax_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 9),
    _TeraLevel1UpStreamMeshMax_Type()
)
teraLevel1UpStreamMeshMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamMeshMax.setStatus("mandatory")
_TeraLevel1UpStreamDSlot_Type = Integer32
_TeraLevel1UpStreamDSlot_Object = MibTableColumn
teraLevel1UpStreamDSlot = _TeraLevel1UpStreamDSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 10),
    _TeraLevel1UpStreamDSlot_Type()
)
teraLevel1UpStreamDSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamDSlot.setStatus("mandatory")
_TeraLevel1UpStreamMChan_Type = Integer32
_TeraLevel1UpStreamMChan_Object = MibTableColumn
teraLevel1UpStreamMChan = _TeraLevel1UpStreamMChan_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 11),
    _TeraLevel1UpStreamMChan_Type()
)
teraLevel1UpStreamMChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamMChan.setStatus("mandatory")
_TeraLevel1UpStreamrtVBRWeighted_Type = Integer32
_TeraLevel1UpStreamrtVBRWeighted_Object = MibTableColumn
teraLevel1UpStreamrtVBRWeighted = _TeraLevel1UpStreamrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 12),
    _TeraLevel1UpStreamrtVBRWeighted_Type()
)
teraLevel1UpStreamrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamrtVBRWeighted.setStatus("mandatory")
_TeraLevel1UpStreamrtVBRpeakWeighted_Type = Integer32
_TeraLevel1UpStreamrtVBRpeakWeighted_Object = MibTableColumn
teraLevel1UpStreamrtVBRpeakWeighted = _TeraLevel1UpStreamrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 13),
    _TeraLevel1UpStreamrtVBRpeakWeighted_Type()
)
teraLevel1UpStreamrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamrtVBRpeakWeighted.setStatus("mandatory")
_TeraLevel1UpStreamnrtVBRWeighted_Type = Integer32
_TeraLevel1UpStreamnrtVBRWeighted_Object = MibTableColumn
teraLevel1UpStreamnrtVBRWeighted = _TeraLevel1UpStreamnrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 14),
    _TeraLevel1UpStreamnrtVBRWeighted_Type()
)
teraLevel1UpStreamnrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamnrtVBRWeighted.setStatus("mandatory")
_TeraLevel1UpStreamnrtVBRpeakWeighted_Type = Integer32
_TeraLevel1UpStreamnrtVBRpeakWeighted_Object = MibTableColumn
teraLevel1UpStreamnrtVBRpeakWeighted = _TeraLevel1UpStreamnrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 15),
    _TeraLevel1UpStreamnrtVBRpeakWeighted_Type()
)
teraLevel1UpStreamnrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamnrtVBRpeakWeighted.setStatus("mandatory")
_TeraLevel1UpStreamUBRWeighted_Type = Integer32
_TeraLevel1UpStreamUBRWeighted_Object = MibTableColumn
teraLevel1UpStreamUBRWeighted = _TeraLevel1UpStreamUBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 16),
    _TeraLevel1UpStreamUBRWeighted_Type()
)
teraLevel1UpStreamUBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamUBRWeighted.setStatus("mandatory")
_TeraLevel1UpStreamUBRMcrWeighted_Type = Integer32
_TeraLevel1UpStreamUBRMcrWeighted_Object = MibTableColumn
teraLevel1UpStreamUBRMcrWeighted = _TeraLevel1UpStreamUBRMcrWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 17),
    _TeraLevel1UpStreamUBRMcrWeighted_Type()
)
teraLevel1UpStreamUBRMcrWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamUBRMcrWeighted.setStatus("mandatory")
_TeraLevel1UpStreamMeshGuarWeighted_Type = Integer32
_TeraLevel1UpStreamMeshGuarWeighted_Object = MibTableColumn
teraLevel1UpStreamMeshGuarWeighted = _TeraLevel1UpStreamMeshGuarWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 18),
    _TeraLevel1UpStreamMeshGuarWeighted_Type()
)
teraLevel1UpStreamMeshGuarWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamMeshGuarWeighted.setStatus("mandatory")
_TeraLevel1UpStreamMeshMaxWeighted_Type = Integer32
_TeraLevel1UpStreamMeshMaxWeighted_Object = MibTableColumn
teraLevel1UpStreamMeshMaxWeighted = _TeraLevel1UpStreamMeshMaxWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 19),
    _TeraLevel1UpStreamMeshMaxWeighted_Type()
)
teraLevel1UpStreamMeshMaxWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamMeshMaxWeighted.setStatus("mandatory")
_TeraLevel1UpStreamCBRReservedBW4Rounding_Type = Integer32
_TeraLevel1UpStreamCBRReservedBW4Rounding_Object = MibTableColumn
teraLevel1UpStreamCBRReservedBW4Rounding = _TeraLevel1UpStreamCBRReservedBW4Rounding_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 20),
    _TeraLevel1UpStreamCBRReservedBW4Rounding_Type()
)
teraLevel1UpStreamCBRReservedBW4Rounding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamCBRReservedBW4Rounding.setStatus("mandatory")
_TeraLevel1UpStreamTotalScrUse_Type = Integer32
_TeraLevel1UpStreamTotalScrUse_Object = MibTableColumn
teraLevel1UpStreamTotalScrUse = _TeraLevel1UpStreamTotalScrUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 21),
    _TeraLevel1UpStreamTotalScrUse_Type()
)
teraLevel1UpStreamTotalScrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamTotalScrUse.setStatus("mandatory")
_TeraLevel1UpStreamTotalUse_Type = Integer32
_TeraLevel1UpStreamTotalUse_Object = MibTableColumn
teraLevel1UpStreamTotalUse = _TeraLevel1UpStreamTotalUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 22),
    _TeraLevel1UpStreamTotalUse_Type()
)
teraLevel1UpStreamTotalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamTotalUse.setStatus("mandatory")
_TeraLevel1UpStreamTotalWeightedUse_Type = Integer32
_TeraLevel1UpStreamTotalWeightedUse_Object = MibTableColumn
teraLevel1UpStreamTotalWeightedUse = _TeraLevel1UpStreamTotalWeightedUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 23),
    _TeraLevel1UpStreamTotalWeightedUse_Type()
)
teraLevel1UpStreamTotalWeightedUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamTotalWeightedUse.setStatus("mandatory")
_TeraLevel1UpStreamTotalBWAvailableForVBROnly_Type = Integer32
_TeraLevel1UpStreamTotalBWAvailableForVBROnly_Object = MibTableColumn
teraLevel1UpStreamTotalBWAvailableForVBROnly = _TeraLevel1UpStreamTotalBWAvailableForVBROnly_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 24),
    _TeraLevel1UpStreamTotalBWAvailableForVBROnly_Type()
)
teraLevel1UpStreamTotalBWAvailableForVBROnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamTotalBWAvailableForVBROnly.setStatus("mandatory")
_TeraLevel1UpStreamTotalBWAvailableForAny_Type = Integer32
_TeraLevel1UpStreamTotalBWAvailableForAny_Object = MibTableColumn
teraLevel1UpStreamTotalBWAvailableForAny = _TeraLevel1UpStreamTotalBWAvailableForAny_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 25),
    _TeraLevel1UpStreamTotalBWAvailableForAny_Type()
)
teraLevel1UpStreamTotalBWAvailableForAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamTotalBWAvailableForAny.setStatus("mandatory")
_TeraLevel1UpStreamTotalBW_Type = Integer32
_TeraLevel1UpStreamTotalBW_Object = MibTableColumn
teraLevel1UpStreamTotalBW = _TeraLevel1UpStreamTotalBW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 3, 1, 26),
    _TeraLevel1UpStreamTotalBW_Type()
)
teraLevel1UpStreamTotalBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1UpStreamTotalBW.setStatus("mandatory")
_TeraLevel1UseDownStreamTable_Object = MibTable
teraLevel1UseDownStreamTable = _TeraLevel1UseDownStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4)
)
if mibBuilder.loadTexts:
    teraLevel1UseDownStreamTable.setStatus("mandatory")
_TeraLevel1UseDownStreamTableEntry_Object = MibTableRow
teraLevel1UseDownStreamTableEntry = _TeraLevel1UseDownStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1)
)
teraLevel1UseDownStreamTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCAC-MIB", "teraLevel1UseSlotNumber"),
)
if mibBuilder.loadTexts:
    teraLevel1UseDownStreamTableEntry.setStatus("mandatory")
_TeraLevel1DownStreamCBR_Type = Integer32
_TeraLevel1DownStreamCBR_Object = MibTableColumn
teraLevel1DownStreamCBR = _TeraLevel1DownStreamCBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 1),
    _TeraLevel1DownStreamCBR_Type()
)
teraLevel1DownStreamCBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamCBR.setStatus("mandatory")
_TeraLevel1DownStreamrtVBR_Type = Integer32
_TeraLevel1DownStreamrtVBR_Object = MibTableColumn
teraLevel1DownStreamrtVBR = _TeraLevel1DownStreamrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 2),
    _TeraLevel1DownStreamrtVBR_Type()
)
teraLevel1DownStreamrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamrtVBR.setStatus("mandatory")
_TeraLevel1DownStreamrtVBRpeak_Type = Integer32
_TeraLevel1DownStreamrtVBRpeak_Object = MibTableColumn
teraLevel1DownStreamrtVBRpeak = _TeraLevel1DownStreamrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 3),
    _TeraLevel1DownStreamrtVBRpeak_Type()
)
teraLevel1DownStreamrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamrtVBRpeak.setStatus("mandatory")
_TeraLevel1DownStreamnrtVBR_Type = Integer32
_TeraLevel1DownStreamnrtVBR_Object = MibTableColumn
teraLevel1DownStreamnrtVBR = _TeraLevel1DownStreamnrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 4),
    _TeraLevel1DownStreamnrtVBR_Type()
)
teraLevel1DownStreamnrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamnrtVBR.setStatus("mandatory")
_TeraLevel1DownStreamnrtVBRpeak_Type = Integer32
_TeraLevel1DownStreamnrtVBRpeak_Object = MibTableColumn
teraLevel1DownStreamnrtVBRpeak = _TeraLevel1DownStreamnrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 5),
    _TeraLevel1DownStreamnrtVBRpeak_Type()
)
teraLevel1DownStreamnrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamnrtVBRpeak.setStatus("mandatory")
_TeraLevel1DownStreamUBR_Type = Integer32
_TeraLevel1DownStreamUBR_Object = MibTableColumn
teraLevel1DownStreamUBR = _TeraLevel1DownStreamUBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 6),
    _TeraLevel1DownStreamUBR_Type()
)
teraLevel1DownStreamUBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamUBR.setStatus("mandatory")
_TeraLevel1DownStreamUBRMcr_Type = Integer32
_TeraLevel1DownStreamUBRMcr_Object = MibTableColumn
teraLevel1DownStreamUBRMcr = _TeraLevel1DownStreamUBRMcr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 7),
    _TeraLevel1DownStreamUBRMcr_Type()
)
teraLevel1DownStreamUBRMcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamUBRMcr.setStatus("mandatory")
_TeraLevel1DownStreamMeshGuar_Type = Integer32
_TeraLevel1DownStreamMeshGuar_Object = MibTableColumn
teraLevel1DownStreamMeshGuar = _TeraLevel1DownStreamMeshGuar_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 8),
    _TeraLevel1DownStreamMeshGuar_Type()
)
teraLevel1DownStreamMeshGuar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamMeshGuar.setStatus("mandatory")
_TeraLevel1DownStreamMeshMax_Type = Integer32
_TeraLevel1DownStreamMeshMax_Object = MibTableColumn
teraLevel1DownStreamMeshMax = _TeraLevel1DownStreamMeshMax_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 9),
    _TeraLevel1DownStreamMeshMax_Type()
)
teraLevel1DownStreamMeshMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamMeshMax.setStatus("mandatory")
_TeraLevel1DownStreamDSlot_Type = Integer32
_TeraLevel1DownStreamDSlot_Object = MibTableColumn
teraLevel1DownStreamDSlot = _TeraLevel1DownStreamDSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 10),
    _TeraLevel1DownStreamDSlot_Type()
)
teraLevel1DownStreamDSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamDSlot.setStatus("mandatory")
_TeraLevel1DownStreamMChan_Type = Integer32
_TeraLevel1DownStreamMChan_Object = MibTableColumn
teraLevel1DownStreamMChan = _TeraLevel1DownStreamMChan_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 11),
    _TeraLevel1DownStreamMChan_Type()
)
teraLevel1DownStreamMChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamMChan.setStatus("mandatory")
_TeraLevel1DownStreamrtVBRWeighted_Type = Integer32
_TeraLevel1DownStreamrtVBRWeighted_Object = MibTableColumn
teraLevel1DownStreamrtVBRWeighted = _TeraLevel1DownStreamrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 12),
    _TeraLevel1DownStreamrtVBRWeighted_Type()
)
teraLevel1DownStreamrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamrtVBRWeighted.setStatus("mandatory")
_TeraLevel1DownStreamrtVBRpeakWeighted_Type = Integer32
_TeraLevel1DownStreamrtVBRpeakWeighted_Object = MibTableColumn
teraLevel1DownStreamrtVBRpeakWeighted = _TeraLevel1DownStreamrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 13),
    _TeraLevel1DownStreamrtVBRpeakWeighted_Type()
)
teraLevel1DownStreamrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamrtVBRpeakWeighted.setStatus("mandatory")
_TeraLevel1DownStreamnrtVBRWeighted_Type = Integer32
_TeraLevel1DownStreamnrtVBRWeighted_Object = MibTableColumn
teraLevel1DownStreamnrtVBRWeighted = _TeraLevel1DownStreamnrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 14),
    _TeraLevel1DownStreamnrtVBRWeighted_Type()
)
teraLevel1DownStreamnrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamnrtVBRWeighted.setStatus("mandatory")
_TeraLevel1DownStreamnrtVBRpeakWeighted_Type = Integer32
_TeraLevel1DownStreamnrtVBRpeakWeighted_Object = MibTableColumn
teraLevel1DownStreamnrtVBRpeakWeighted = _TeraLevel1DownStreamnrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 15),
    _TeraLevel1DownStreamnrtVBRpeakWeighted_Type()
)
teraLevel1DownStreamnrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamnrtVBRpeakWeighted.setStatus("mandatory")
_TeraLevel1DownStreamUBRWeighted_Type = Integer32
_TeraLevel1DownStreamUBRWeighted_Object = MibTableColumn
teraLevel1DownStreamUBRWeighted = _TeraLevel1DownStreamUBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 16),
    _TeraLevel1DownStreamUBRWeighted_Type()
)
teraLevel1DownStreamUBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamUBRWeighted.setStatus("mandatory")
_TeraLevel1DownStreamUBRMcrWeighted_Type = Integer32
_TeraLevel1DownStreamUBRMcrWeighted_Object = MibTableColumn
teraLevel1DownStreamUBRMcrWeighted = _TeraLevel1DownStreamUBRMcrWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 17),
    _TeraLevel1DownStreamUBRMcrWeighted_Type()
)
teraLevel1DownStreamUBRMcrWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamUBRMcrWeighted.setStatus("mandatory")
_TeraLevel1DownStreamMeshGuarWeighted_Type = Integer32
_TeraLevel1DownStreamMeshGuarWeighted_Object = MibTableColumn
teraLevel1DownStreamMeshGuarWeighted = _TeraLevel1DownStreamMeshGuarWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 18),
    _TeraLevel1DownStreamMeshGuarWeighted_Type()
)
teraLevel1DownStreamMeshGuarWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamMeshGuarWeighted.setStatus("mandatory")
_TeraLevel1DownStreamMeshMaxWeighted_Type = Integer32
_TeraLevel1DownStreamMeshMaxWeighted_Object = MibTableColumn
teraLevel1DownStreamMeshMaxWeighted = _TeraLevel1DownStreamMeshMaxWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 19),
    _TeraLevel1DownStreamMeshMaxWeighted_Type()
)
teraLevel1DownStreamMeshMaxWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamMeshMaxWeighted.setStatus("mandatory")
_TeraLevel1DownStreamCBRReservedBW4Rounding_Type = Integer32
_TeraLevel1DownStreamCBRReservedBW4Rounding_Object = MibTableColumn
teraLevel1DownStreamCBRReservedBW4Rounding = _TeraLevel1DownStreamCBRReservedBW4Rounding_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 20),
    _TeraLevel1DownStreamCBRReservedBW4Rounding_Type()
)
teraLevel1DownStreamCBRReservedBW4Rounding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamCBRReservedBW4Rounding.setStatus("mandatory")
_TeraLevel1DownStreamTotalScrUse_Type = Integer32
_TeraLevel1DownStreamTotalScrUse_Object = MibTableColumn
teraLevel1DownStreamTotalScrUse = _TeraLevel1DownStreamTotalScrUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 21),
    _TeraLevel1DownStreamTotalScrUse_Type()
)
teraLevel1DownStreamTotalScrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamTotalScrUse.setStatus("mandatory")
_TeraLevel1DownStreamTotalUse_Type = Integer32
_TeraLevel1DownStreamTotalUse_Object = MibTableColumn
teraLevel1DownStreamTotalUse = _TeraLevel1DownStreamTotalUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 22),
    _TeraLevel1DownStreamTotalUse_Type()
)
teraLevel1DownStreamTotalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamTotalUse.setStatus("mandatory")


class _TeraLevel1DownStreamTotalWeightedUse_Type(Integer32):
    """Custom type teraLevel1DownStreamTotalWeightedUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel1DownStreamTotalWeightedUse_Type.__name__ = "Integer32"
_TeraLevel1DownStreamTotalWeightedUse_Object = MibTableColumn
teraLevel1DownStreamTotalWeightedUse = _TeraLevel1DownStreamTotalWeightedUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 23),
    _TeraLevel1DownStreamTotalWeightedUse_Type()
)
teraLevel1DownStreamTotalWeightedUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamTotalWeightedUse.setStatus("mandatory")
_TeraLevel1DownStreamTotalBWAvailableForVBROnly_Type = Integer32
_TeraLevel1DownStreamTotalBWAvailableForVBROnly_Object = MibTableColumn
teraLevel1DownStreamTotalBWAvailableForVBROnly = _TeraLevel1DownStreamTotalBWAvailableForVBROnly_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 24),
    _TeraLevel1DownStreamTotalBWAvailableForVBROnly_Type()
)
teraLevel1DownStreamTotalBWAvailableForVBROnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamTotalBWAvailableForVBROnly.setStatus("mandatory")
_TeraLevel1DownStreamTotalBWAvailableForAny_Type = Integer32
_TeraLevel1DownStreamTotalBWAvailableForAny_Object = MibTableColumn
teraLevel1DownStreamTotalBWAvailableForAny = _TeraLevel1DownStreamTotalBWAvailableForAny_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 25),
    _TeraLevel1DownStreamTotalBWAvailableForAny_Type()
)
teraLevel1DownStreamTotalBWAvailableForAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamTotalBWAvailableForAny.setStatus("mandatory")
_TeraLevel1DownStreamTotalBW_Type = Integer32
_TeraLevel1DownStreamTotalBW_Object = MibTableColumn
teraLevel1DownStreamTotalBW = _TeraLevel1DownStreamTotalBW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 4, 1, 26),
    _TeraLevel1DownStreamTotalBW_Type()
)
teraLevel1DownStreamTotalBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel1DownStreamTotalBW.setStatus("mandatory")
_TeraLevel2UseUpStreamTable_Object = MibTable
teraLevel2UseUpStreamTable = _TeraLevel2UseUpStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5)
)
if mibBuilder.loadTexts:
    teraLevel2UseUpStreamTable.setStatus("mandatory")
_TeraLevel2UseUpStreamTableEntry_Object = MibTableRow
teraLevel2UseUpStreamTableEntry = _TeraLevel2UseUpStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1)
)
teraLevel2UseUpStreamTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCAC-MIB", "teraLevel1UseSlotNumber"),
    (0, "TERAWAVE-teraCAC-MIB", "teraUsePonIndex"),
    (0, "TERAWAVE-teraCAC-MIB", "teraLevel2UseSlotNumber"),
)
if mibBuilder.loadTexts:
    teraLevel2UseUpStreamTableEntry.setStatus("mandatory")
_TeraLevel2UpStreamCBR_Type = Integer32
_TeraLevel2UpStreamCBR_Object = MibTableColumn
teraLevel2UpStreamCBR = _TeraLevel2UpStreamCBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 1),
    _TeraLevel2UpStreamCBR_Type()
)
teraLevel2UpStreamCBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamCBR.setStatus("mandatory")
_TeraLevel2UpStreamrtVBR_Type = Integer32
_TeraLevel2UpStreamrtVBR_Object = MibTableColumn
teraLevel2UpStreamrtVBR = _TeraLevel2UpStreamrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 2),
    _TeraLevel2UpStreamrtVBR_Type()
)
teraLevel2UpStreamrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamrtVBR.setStatus("mandatory")
_TeraLevel2UpStreamrtVBRpeak_Type = Integer32
_TeraLevel2UpStreamrtVBRpeak_Object = MibTableColumn
teraLevel2UpStreamrtVBRpeak = _TeraLevel2UpStreamrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 3),
    _TeraLevel2UpStreamrtVBRpeak_Type()
)
teraLevel2UpStreamrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamrtVBRpeak.setStatus("mandatory")
_TeraLevel2UpStreamnrtVBR_Type = Integer32
_TeraLevel2UpStreamnrtVBR_Object = MibTableColumn
teraLevel2UpStreamnrtVBR = _TeraLevel2UpStreamnrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 4),
    _TeraLevel2UpStreamnrtVBR_Type()
)
teraLevel2UpStreamnrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamnrtVBR.setStatus("mandatory")
_TeraLevel2UpStreamnrtVBRpeak_Type = Integer32
_TeraLevel2UpStreamnrtVBRpeak_Object = MibTableColumn
teraLevel2UpStreamnrtVBRpeak = _TeraLevel2UpStreamnrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 5),
    _TeraLevel2UpStreamnrtVBRpeak_Type()
)
teraLevel2UpStreamnrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamnrtVBRpeak.setStatus("mandatory")
_TeraLevel2UpStreamUBR_Type = Integer32
_TeraLevel2UpStreamUBR_Object = MibTableColumn
teraLevel2UpStreamUBR = _TeraLevel2UpStreamUBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 6),
    _TeraLevel2UpStreamUBR_Type()
)
teraLevel2UpStreamUBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamUBR.setStatus("mandatory")
_TeraLevel2UpStreamUBRMcr_Type = Integer32
_TeraLevel2UpStreamUBRMcr_Object = MibTableColumn
teraLevel2UpStreamUBRMcr = _TeraLevel2UpStreamUBRMcr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 7),
    _TeraLevel2UpStreamUBRMcr_Type()
)
teraLevel2UpStreamUBRMcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamUBRMcr.setStatus("mandatory")
_TeraLevel2UpStreamMeshGuar_Type = Integer32
_TeraLevel2UpStreamMeshGuar_Object = MibTableColumn
teraLevel2UpStreamMeshGuar = _TeraLevel2UpStreamMeshGuar_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 8),
    _TeraLevel2UpStreamMeshGuar_Type()
)
teraLevel2UpStreamMeshGuar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamMeshGuar.setStatus("mandatory")
_TeraLevel2UpStreamMeshMax_Type = Integer32
_TeraLevel2UpStreamMeshMax_Object = MibTableColumn
teraLevel2UpStreamMeshMax = _TeraLevel2UpStreamMeshMax_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 9),
    _TeraLevel2UpStreamMeshMax_Type()
)
teraLevel2UpStreamMeshMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamMeshMax.setStatus("mandatory")
_TeraLevel2UpStreamDSlot_Type = Integer32
_TeraLevel2UpStreamDSlot_Object = MibTableColumn
teraLevel2UpStreamDSlot = _TeraLevel2UpStreamDSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 10),
    _TeraLevel2UpStreamDSlot_Type()
)
teraLevel2UpStreamDSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamDSlot.setStatus("mandatory")
_TeraLevel2UpStreamMChan_Type = Integer32
_TeraLevel2UpStreamMChan_Object = MibTableColumn
teraLevel2UpStreamMChan = _TeraLevel2UpStreamMChan_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 11),
    _TeraLevel2UpStreamMChan_Type()
)
teraLevel2UpStreamMChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamMChan.setStatus("mandatory")


class _TeraLevel2UpStreamrtVBRWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamrtVBRWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamrtVBRWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamrtVBRWeighted_Object = MibTableColumn
teraLevel2UpStreamrtVBRWeighted = _TeraLevel2UpStreamrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 12),
    _TeraLevel2UpStreamrtVBRWeighted_Type()
)
teraLevel2UpStreamrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamrtVBRWeighted.setStatus("mandatory")


class _TeraLevel2UpStreamrtVBRpeakWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamrtVBRpeakWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamrtVBRpeakWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamrtVBRpeakWeighted_Object = MibTableColumn
teraLevel2UpStreamrtVBRpeakWeighted = _TeraLevel2UpStreamrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 13),
    _TeraLevel2UpStreamrtVBRpeakWeighted_Type()
)
teraLevel2UpStreamrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamrtVBRpeakWeighted.setStatus("mandatory")


class _TeraLevel2UpStreamnrtVBRWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamnrtVBRWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamnrtVBRWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamnrtVBRWeighted_Object = MibTableColumn
teraLevel2UpStreamnrtVBRWeighted = _TeraLevel2UpStreamnrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 14),
    _TeraLevel2UpStreamnrtVBRWeighted_Type()
)
teraLevel2UpStreamnrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamnrtVBRWeighted.setStatus("mandatory")


class _TeraLevel2UpStreamnrtVBRpeakWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamnrtVBRpeakWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamnrtVBRpeakWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamnrtVBRpeakWeighted_Object = MibTableColumn
teraLevel2UpStreamnrtVBRpeakWeighted = _TeraLevel2UpStreamnrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 15),
    _TeraLevel2UpStreamnrtVBRpeakWeighted_Type()
)
teraLevel2UpStreamnrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamnrtVBRpeakWeighted.setStatus("mandatory")


class _TeraLevel2UpStreamUBRWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamUBRWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamUBRWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamUBRWeighted_Object = MibTableColumn
teraLevel2UpStreamUBRWeighted = _TeraLevel2UpStreamUBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 16),
    _TeraLevel2UpStreamUBRWeighted_Type()
)
teraLevel2UpStreamUBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamUBRWeighted.setStatus("mandatory")


class _TeraLevel2UpStreamUBRMcrWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamUBRMcrWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamUBRMcrWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamUBRMcrWeighted_Object = MibTableColumn
teraLevel2UpStreamUBRMcrWeighted = _TeraLevel2UpStreamUBRMcrWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 17),
    _TeraLevel2UpStreamUBRMcrWeighted_Type()
)
teraLevel2UpStreamUBRMcrWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamUBRMcrWeighted.setStatus("mandatory")


class _TeraLevel2UpStreamMeshGuarWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamMeshGuarWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamMeshGuarWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamMeshGuarWeighted_Object = MibTableColumn
teraLevel2UpStreamMeshGuarWeighted = _TeraLevel2UpStreamMeshGuarWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 18),
    _TeraLevel2UpStreamMeshGuarWeighted_Type()
)
teraLevel2UpStreamMeshGuarWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamMeshGuarWeighted.setStatus("mandatory")


class _TeraLevel2UpStreamMeshMaxWeighted_Type(Integer32):
    """Custom type teraLevel2UpStreamMeshMaxWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamMeshMaxWeighted_Type.__name__ = "Integer32"
_TeraLevel2UpStreamMeshMaxWeighted_Object = MibTableColumn
teraLevel2UpStreamMeshMaxWeighted = _TeraLevel2UpStreamMeshMaxWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 19),
    _TeraLevel2UpStreamMeshMaxWeighted_Type()
)
teraLevel2UpStreamMeshMaxWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamMeshMaxWeighted.setStatus("mandatory")
_TeraLevel2UpStreamTotalScrUse_Type = Integer32
_TeraLevel2UpStreamTotalScrUse_Object = MibTableColumn
teraLevel2UpStreamTotalScrUse = _TeraLevel2UpStreamTotalScrUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 20),
    _TeraLevel2UpStreamTotalScrUse_Type()
)
teraLevel2UpStreamTotalScrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamTotalScrUse.setStatus("mandatory")
_TeraLevel2UpStreamTotalUse_Type = Integer32
_TeraLevel2UpStreamTotalUse_Object = MibTableColumn
teraLevel2UpStreamTotalUse = _TeraLevel2UpStreamTotalUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 21),
    _TeraLevel2UpStreamTotalUse_Type()
)
teraLevel2UpStreamTotalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamTotalUse.setStatus("mandatory")


class _TeraLevel2UpStreamTotalWeightedUse_Type(Integer32):
    """Custom type teraLevel2UpStreamTotalWeightedUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2UpStreamTotalWeightedUse_Type.__name__ = "Integer32"
_TeraLevel2UpStreamTotalWeightedUse_Object = MibTableColumn
teraLevel2UpStreamTotalWeightedUse = _TeraLevel2UpStreamTotalWeightedUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 22),
    _TeraLevel2UpStreamTotalWeightedUse_Type()
)
teraLevel2UpStreamTotalWeightedUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamTotalWeightedUse.setStatus("mandatory")
_TeraLevel2UpStreamTotalBW_Type = Integer32
_TeraLevel2UpStreamTotalBW_Object = MibTableColumn
teraLevel2UpStreamTotalBW = _TeraLevel2UpStreamTotalBW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 5, 1, 23),
    _TeraLevel2UpStreamTotalBW_Type()
)
teraLevel2UpStreamTotalBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2UpStreamTotalBW.setStatus("mandatory")
_TeraLevel2UseDownStreamTable_Object = MibTable
teraLevel2UseDownStreamTable = _TeraLevel2UseDownStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6)
)
if mibBuilder.loadTexts:
    teraLevel2UseDownStreamTable.setStatus("mandatory")
_TeraLevel2UseDownStreamTableEntry_Object = MibTableRow
teraLevel2UseDownStreamTableEntry = _TeraLevel2UseDownStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1)
)
teraLevel2UseDownStreamTableEntry.setIndexNames(
    (0, "TERAWAVE-teraCAC-MIB", "teraLevel1UseSlotNumber"),
    (0, "TERAWAVE-teraCAC-MIB", "teraUsePonIndex"),
    (0, "TERAWAVE-teraCAC-MIB", "teraLevel2UseSlotNumber"),
)
if mibBuilder.loadTexts:
    teraLevel2UseDownStreamTableEntry.setStatus("mandatory")
_TeraLevel2DownStreamCBR_Type = Integer32
_TeraLevel2DownStreamCBR_Object = MibTableColumn
teraLevel2DownStreamCBR = _TeraLevel2DownStreamCBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 1),
    _TeraLevel2DownStreamCBR_Type()
)
teraLevel2DownStreamCBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamCBR.setStatus("mandatory")
_TeraLevel2DownStreamrtVBR_Type = Integer32
_TeraLevel2DownStreamrtVBR_Object = MibTableColumn
teraLevel2DownStreamrtVBR = _TeraLevel2DownStreamrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 2),
    _TeraLevel2DownStreamrtVBR_Type()
)
teraLevel2DownStreamrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamrtVBR.setStatus("mandatory")
_TeraLevel2DownStreamrtVBRpeak_Type = Integer32
_TeraLevel2DownStreamrtVBRpeak_Object = MibTableColumn
teraLevel2DownStreamrtVBRpeak = _TeraLevel2DownStreamrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 3),
    _TeraLevel2DownStreamrtVBRpeak_Type()
)
teraLevel2DownStreamrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamrtVBRpeak.setStatus("mandatory")
_TeraLevel2DownStreamnrtVBR_Type = Integer32
_TeraLevel2DownStreamnrtVBR_Object = MibTableColumn
teraLevel2DownStreamnrtVBR = _TeraLevel2DownStreamnrtVBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 4),
    _TeraLevel2DownStreamnrtVBR_Type()
)
teraLevel2DownStreamnrtVBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamnrtVBR.setStatus("mandatory")
_TeraLevel2DownStreamnrtVBRpeak_Type = Integer32
_TeraLevel2DownStreamnrtVBRpeak_Object = MibTableColumn
teraLevel2DownStreamnrtVBRpeak = _TeraLevel2DownStreamnrtVBRpeak_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 5),
    _TeraLevel2DownStreamnrtVBRpeak_Type()
)
teraLevel2DownStreamnrtVBRpeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamnrtVBRpeak.setStatus("mandatory")
_TeraLevel2DownStreamUBR_Type = Integer32
_TeraLevel2DownStreamUBR_Object = MibTableColumn
teraLevel2DownStreamUBR = _TeraLevel2DownStreamUBR_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 6),
    _TeraLevel2DownStreamUBR_Type()
)
teraLevel2DownStreamUBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamUBR.setStatus("mandatory")
_TeraLevel2DownStreamUBRMcr_Type = Integer32
_TeraLevel2DownStreamUBRMcr_Object = MibTableColumn
teraLevel2DownStreamUBRMcr = _TeraLevel2DownStreamUBRMcr_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 7),
    _TeraLevel2DownStreamUBRMcr_Type()
)
teraLevel2DownStreamUBRMcr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamUBRMcr.setStatus("mandatory")
_TeraLevel2DownStreamMeshGuar_Type = Integer32
_TeraLevel2DownStreamMeshGuar_Object = MibTableColumn
teraLevel2DownStreamMeshGuar = _TeraLevel2DownStreamMeshGuar_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 8),
    _TeraLevel2DownStreamMeshGuar_Type()
)
teraLevel2DownStreamMeshGuar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamMeshGuar.setStatus("mandatory")
_TeraLevel2DownStreamMeshMax_Type = Integer32
_TeraLevel2DownStreamMeshMax_Object = MibTableColumn
teraLevel2DownStreamMeshMax = _TeraLevel2DownStreamMeshMax_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 9),
    _TeraLevel2DownStreamMeshMax_Type()
)
teraLevel2DownStreamMeshMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamMeshMax.setStatus("mandatory")
_TeraLevel2DownStreamDSlot_Type = Integer32
_TeraLevel2DownStreamDSlot_Object = MibTableColumn
teraLevel2DownStreamDSlot = _TeraLevel2DownStreamDSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 10),
    _TeraLevel2DownStreamDSlot_Type()
)
teraLevel2DownStreamDSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamDSlot.setStatus("mandatory")
_TeraLevel2DownStreamMChan_Type = Integer32
_TeraLevel2DownStreamMChan_Object = MibTableColumn
teraLevel2DownStreamMChan = _TeraLevel2DownStreamMChan_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 11),
    _TeraLevel2DownStreamMChan_Type()
)
teraLevel2DownStreamMChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamMChan.setStatus("mandatory")


class _TeraLevel2DownStreamrtVBRWeighted_Type(Integer32):
    """Custom type teraLevel2DownStreamrtVBRWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2DownStreamrtVBRWeighted_Type.__name__ = "Integer32"
_TeraLevel2DownStreamrtVBRWeighted_Object = MibTableColumn
teraLevel2DownStreamrtVBRWeighted = _TeraLevel2DownStreamrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 12),
    _TeraLevel2DownStreamrtVBRWeighted_Type()
)
teraLevel2DownStreamrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamrtVBRWeighted.setStatus("mandatory")


class _TeraLevel2DownStreamrtVBRpeakWeighted_Type(Integer32):
    """Custom type teraLevel2DownStreamrtVBRpeakWeighted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_TeraLevel2DownStreamrtVBRpeakWeighted_Type.__name__ = "Integer32"
_TeraLevel2DownStreamrtVBRpeakWeighted_Object = MibTableColumn
teraLevel2DownStreamrtVBRpeakWeighted = _TeraLevel2DownStreamrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 13),
    _TeraLevel2DownStreamrtVBRpeakWeighted_Type()
)
teraLevel2DownStreamrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamrtVBRpeakWeighted.setStatus("mandatory")
_TeraLevel2DownStreamnrtVBRWeighted_Type = Integer32
_TeraLevel2DownStreamnrtVBRWeighted_Object = MibTableColumn
teraLevel2DownStreamnrtVBRWeighted = _TeraLevel2DownStreamnrtVBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 14),
    _TeraLevel2DownStreamnrtVBRWeighted_Type()
)
teraLevel2DownStreamnrtVBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamnrtVBRWeighted.setStatus("mandatory")
_TeraLevel2DownStreamnrtVBRpeakWeighted_Type = Integer32
_TeraLevel2DownStreamnrtVBRpeakWeighted_Object = MibTableColumn
teraLevel2DownStreamnrtVBRpeakWeighted = _TeraLevel2DownStreamnrtVBRpeakWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 15),
    _TeraLevel2DownStreamnrtVBRpeakWeighted_Type()
)
teraLevel2DownStreamnrtVBRpeakWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamnrtVBRpeakWeighted.setStatus("mandatory")
_TeraLevel2DownStreamUBRWeighted_Type = Integer32
_TeraLevel2DownStreamUBRWeighted_Object = MibTableColumn
teraLevel2DownStreamUBRWeighted = _TeraLevel2DownStreamUBRWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 16),
    _TeraLevel2DownStreamUBRWeighted_Type()
)
teraLevel2DownStreamUBRWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamUBRWeighted.setStatus("mandatory")
_TeraLevel2DownStreamUBRMcrWeighted_Type = Integer32
_TeraLevel2DownStreamUBRMcrWeighted_Object = MibTableColumn
teraLevel2DownStreamUBRMcrWeighted = _TeraLevel2DownStreamUBRMcrWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 17),
    _TeraLevel2DownStreamUBRMcrWeighted_Type()
)
teraLevel2DownStreamUBRMcrWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamUBRMcrWeighted.setStatus("mandatory")
_TeraLevel2DownStreamMeshGuarWeighted_Type = Integer32
_TeraLevel2DownStreamMeshGuarWeighted_Object = MibTableColumn
teraLevel2DownStreamMeshGuarWeighted = _TeraLevel2DownStreamMeshGuarWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 18),
    _TeraLevel2DownStreamMeshGuarWeighted_Type()
)
teraLevel2DownStreamMeshGuarWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamMeshGuarWeighted.setStatus("mandatory")
_TeraLevel2DownStreamMeshMaxWeighted_Type = Integer32
_TeraLevel2DownStreamMeshMaxWeighted_Object = MibTableColumn
teraLevel2DownStreamMeshMaxWeighted = _TeraLevel2DownStreamMeshMaxWeighted_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 19),
    _TeraLevel2DownStreamMeshMaxWeighted_Type()
)
teraLevel2DownStreamMeshMaxWeighted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamMeshMaxWeighted.setStatus("mandatory")
_TeraLevel2DownStreamTotalScrUse_Type = Integer32
_TeraLevel2DownStreamTotalScrUse_Object = MibTableColumn
teraLevel2DownStreamTotalScrUse = _TeraLevel2DownStreamTotalScrUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 20),
    _TeraLevel2DownStreamTotalScrUse_Type()
)
teraLevel2DownStreamTotalScrUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamTotalScrUse.setStatus("mandatory")
_TeraLevel2DownStreamTotalUse_Type = Integer32
_TeraLevel2DownStreamTotalUse_Object = MibTableColumn
teraLevel2DownStreamTotalUse = _TeraLevel2DownStreamTotalUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 21),
    _TeraLevel2DownStreamTotalUse_Type()
)
teraLevel2DownStreamTotalUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamTotalUse.setStatus("mandatory")
_TeraLevel2DownStreamTotalWeightedUse_Type = Integer32
_TeraLevel2DownStreamTotalWeightedUse_Object = MibTableColumn
teraLevel2DownStreamTotalWeightedUse = _TeraLevel2DownStreamTotalWeightedUse_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 22),
    _TeraLevel2DownStreamTotalWeightedUse_Type()
)
teraLevel2DownStreamTotalWeightedUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamTotalWeightedUse.setStatus("mandatory")
_TeraLevel2DownStreamTotalBW_Type = Integer32
_TeraLevel2DownStreamTotalBW_Object = MibTableColumn
teraLevel2DownStreamTotalBW = _TeraLevel2DownStreamTotalBW_Object(
    (1, 3, 6, 1, 4, 1, 4513, 19, 6, 1, 23),
    _TeraLevel2DownStreamTotalBW_Type()
)
teraLevel2DownStreamTotalBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLevel2DownStreamTotalBW.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraCAC-MIB",
    **{"terawave": terawave,
       "teraCACGroup": teraCACGroup,
       "teraCACSystemTablePar": teraCACSystemTablePar,
       "teraCACSystemTable": teraCACSystemTable,
       "teraLevel1UseSlotNumber": teraLevel1UseSlotNumber,
       "teraUsePonIndex": teraUsePonIndex,
       "teraLevel2UseSlotNumber": teraLevel2UseSlotNumber,
       "teraCACTablePar": teraCACTablePar,
       "teraCACTable": teraCACTable,
       "teraCACUpWeightrtVBR": teraCACUpWeightrtVBR,
       "teraCACUpWeightrtVBRpeak": teraCACUpWeightrtVBRpeak,
       "teraCACUpWeightnrtVBR": teraCACUpWeightnrtVBR,
       "teraCACUpWeightnrtVBRpeak": teraCACUpWeightnrtVBRpeak,
       "teraCACUpWeightUBR": teraCACUpWeightUBR,
       "teraCACUpWeightUBRMcr": teraCACUpWeightUBRMcr,
       "teraCACUpWeightMeshGuar": teraCACUpWeightMeshGuar,
       "teraCACUpWeightMeshMax": teraCACUpWeightMeshMax,
       "teraCACDownWeightrtVBR": teraCACDownWeightrtVBR,
       "teraCACDownWeightrtVBRpeak": teraCACDownWeightrtVBRpeak,
       "teraCACDownWeightnrtVBR": teraCACDownWeightnrtVBR,
       "teraCACDownWeightnrtVBRpeak": teraCACDownWeightnrtVBRpeak,
       "teraCACDownWeightUBR": teraCACDownWeightUBR,
       "teraCACDownWeightUBRMcr": teraCACDownWeightUBRMcr,
       "teraCACDownWeightMeshGuar": teraCACDownWeightMeshGuar,
       "teraCACDownWeightMeshMax": teraCACDownWeightMeshMax,
       "teraLevel1UseUpStreamTable": teraLevel1UseUpStreamTable,
       "teraLevel1UseUpStreamTableEntry": teraLevel1UseUpStreamTableEntry,
       "teraLevel1UpStreamCBR": teraLevel1UpStreamCBR,
       "teraLevel1UpStreamrtVBR": teraLevel1UpStreamrtVBR,
       "teraLevel1UpStreamrtVBRpeak": teraLevel1UpStreamrtVBRpeak,
       "teraLevel1UpStreamnrtVBR": teraLevel1UpStreamnrtVBR,
       "teraLevel1UpStreamnrtVBRpeak": teraLevel1UpStreamnrtVBRpeak,
       "teraLevel1UpStreamUBR": teraLevel1UpStreamUBR,
       "teraLevel1UpStreamUBRMcr": teraLevel1UpStreamUBRMcr,
       "teraLevel1UpStreamMeshGuar": teraLevel1UpStreamMeshGuar,
       "teraLevel1UpStreamMeshMax": teraLevel1UpStreamMeshMax,
       "teraLevel1UpStreamDSlot": teraLevel1UpStreamDSlot,
       "teraLevel1UpStreamMChan": teraLevel1UpStreamMChan,
       "teraLevel1UpStreamrtVBRWeighted": teraLevel1UpStreamrtVBRWeighted,
       "teraLevel1UpStreamrtVBRpeakWeighted": teraLevel1UpStreamrtVBRpeakWeighted,
       "teraLevel1UpStreamnrtVBRWeighted": teraLevel1UpStreamnrtVBRWeighted,
       "teraLevel1UpStreamnrtVBRpeakWeighted": teraLevel1UpStreamnrtVBRpeakWeighted,
       "teraLevel1UpStreamUBRWeighted": teraLevel1UpStreamUBRWeighted,
       "teraLevel1UpStreamUBRMcrWeighted": teraLevel1UpStreamUBRMcrWeighted,
       "teraLevel1UpStreamMeshGuarWeighted": teraLevel1UpStreamMeshGuarWeighted,
       "teraLevel1UpStreamMeshMaxWeighted": teraLevel1UpStreamMeshMaxWeighted,
       "teraLevel1UpStreamCBRReservedBW4Rounding": teraLevel1UpStreamCBRReservedBW4Rounding,
       "teraLevel1UpStreamTotalScrUse": teraLevel1UpStreamTotalScrUse,
       "teraLevel1UpStreamTotalUse": teraLevel1UpStreamTotalUse,
       "teraLevel1UpStreamTotalWeightedUse": teraLevel1UpStreamTotalWeightedUse,
       "teraLevel1UpStreamTotalBWAvailableForVBROnly": teraLevel1UpStreamTotalBWAvailableForVBROnly,
       "teraLevel1UpStreamTotalBWAvailableForAny": teraLevel1UpStreamTotalBWAvailableForAny,
       "teraLevel1UpStreamTotalBW": teraLevel1UpStreamTotalBW,
       "teraLevel1UseDownStreamTable": teraLevel1UseDownStreamTable,
       "teraLevel1UseDownStreamTableEntry": teraLevel1UseDownStreamTableEntry,
       "teraLevel1DownStreamCBR": teraLevel1DownStreamCBR,
       "teraLevel1DownStreamrtVBR": teraLevel1DownStreamrtVBR,
       "teraLevel1DownStreamrtVBRpeak": teraLevel1DownStreamrtVBRpeak,
       "teraLevel1DownStreamnrtVBR": teraLevel1DownStreamnrtVBR,
       "teraLevel1DownStreamnrtVBRpeak": teraLevel1DownStreamnrtVBRpeak,
       "teraLevel1DownStreamUBR": teraLevel1DownStreamUBR,
       "teraLevel1DownStreamUBRMcr": teraLevel1DownStreamUBRMcr,
       "teraLevel1DownStreamMeshGuar": teraLevel1DownStreamMeshGuar,
       "teraLevel1DownStreamMeshMax": teraLevel1DownStreamMeshMax,
       "teraLevel1DownStreamDSlot": teraLevel1DownStreamDSlot,
       "teraLevel1DownStreamMChan": teraLevel1DownStreamMChan,
       "teraLevel1DownStreamrtVBRWeighted": teraLevel1DownStreamrtVBRWeighted,
       "teraLevel1DownStreamrtVBRpeakWeighted": teraLevel1DownStreamrtVBRpeakWeighted,
       "teraLevel1DownStreamnrtVBRWeighted": teraLevel1DownStreamnrtVBRWeighted,
       "teraLevel1DownStreamnrtVBRpeakWeighted": teraLevel1DownStreamnrtVBRpeakWeighted,
       "teraLevel1DownStreamUBRWeighted": teraLevel1DownStreamUBRWeighted,
       "teraLevel1DownStreamUBRMcrWeighted": teraLevel1DownStreamUBRMcrWeighted,
       "teraLevel1DownStreamMeshGuarWeighted": teraLevel1DownStreamMeshGuarWeighted,
       "teraLevel1DownStreamMeshMaxWeighted": teraLevel1DownStreamMeshMaxWeighted,
       "teraLevel1DownStreamCBRReservedBW4Rounding": teraLevel1DownStreamCBRReservedBW4Rounding,
       "teraLevel1DownStreamTotalScrUse": teraLevel1DownStreamTotalScrUse,
       "teraLevel1DownStreamTotalUse": teraLevel1DownStreamTotalUse,
       "teraLevel1DownStreamTotalWeightedUse": teraLevel1DownStreamTotalWeightedUse,
       "teraLevel1DownStreamTotalBWAvailableForVBROnly": teraLevel1DownStreamTotalBWAvailableForVBROnly,
       "teraLevel1DownStreamTotalBWAvailableForAny": teraLevel1DownStreamTotalBWAvailableForAny,
       "teraLevel1DownStreamTotalBW": teraLevel1DownStreamTotalBW,
       "teraLevel2UseUpStreamTable": teraLevel2UseUpStreamTable,
       "teraLevel2UseUpStreamTableEntry": teraLevel2UseUpStreamTableEntry,
       "teraLevel2UpStreamCBR": teraLevel2UpStreamCBR,
       "teraLevel2UpStreamrtVBR": teraLevel2UpStreamrtVBR,
       "teraLevel2UpStreamrtVBRpeak": teraLevel2UpStreamrtVBRpeak,
       "teraLevel2UpStreamnrtVBR": teraLevel2UpStreamnrtVBR,
       "teraLevel2UpStreamnrtVBRpeak": teraLevel2UpStreamnrtVBRpeak,
       "teraLevel2UpStreamUBR": teraLevel2UpStreamUBR,
       "teraLevel2UpStreamUBRMcr": teraLevel2UpStreamUBRMcr,
       "teraLevel2UpStreamMeshGuar": teraLevel2UpStreamMeshGuar,
       "teraLevel2UpStreamMeshMax": teraLevel2UpStreamMeshMax,
       "teraLevel2UpStreamDSlot": teraLevel2UpStreamDSlot,
       "teraLevel2UpStreamMChan": teraLevel2UpStreamMChan,
       "teraLevel2UpStreamrtVBRWeighted": teraLevel2UpStreamrtVBRWeighted,
       "teraLevel2UpStreamrtVBRpeakWeighted": teraLevel2UpStreamrtVBRpeakWeighted,
       "teraLevel2UpStreamnrtVBRWeighted": teraLevel2UpStreamnrtVBRWeighted,
       "teraLevel2UpStreamnrtVBRpeakWeighted": teraLevel2UpStreamnrtVBRpeakWeighted,
       "teraLevel2UpStreamUBRWeighted": teraLevel2UpStreamUBRWeighted,
       "teraLevel2UpStreamUBRMcrWeighted": teraLevel2UpStreamUBRMcrWeighted,
       "teraLevel2UpStreamMeshGuarWeighted": teraLevel2UpStreamMeshGuarWeighted,
       "teraLevel2UpStreamMeshMaxWeighted": teraLevel2UpStreamMeshMaxWeighted,
       "teraLevel2UpStreamTotalScrUse": teraLevel2UpStreamTotalScrUse,
       "teraLevel2UpStreamTotalUse": teraLevel2UpStreamTotalUse,
       "teraLevel2UpStreamTotalWeightedUse": teraLevel2UpStreamTotalWeightedUse,
       "teraLevel2UpStreamTotalBW": teraLevel2UpStreamTotalBW,
       "teraLevel2UseDownStreamTable": teraLevel2UseDownStreamTable,
       "teraLevel2UseDownStreamTableEntry": teraLevel2UseDownStreamTableEntry,
       "teraLevel2DownStreamCBR": teraLevel2DownStreamCBR,
       "teraLevel2DownStreamrtVBR": teraLevel2DownStreamrtVBR,
       "teraLevel2DownStreamrtVBRpeak": teraLevel2DownStreamrtVBRpeak,
       "teraLevel2DownStreamnrtVBR": teraLevel2DownStreamnrtVBR,
       "teraLevel2DownStreamnrtVBRpeak": teraLevel2DownStreamnrtVBRpeak,
       "teraLevel2DownStreamUBR": teraLevel2DownStreamUBR,
       "teraLevel2DownStreamUBRMcr": teraLevel2DownStreamUBRMcr,
       "teraLevel2DownStreamMeshGuar": teraLevel2DownStreamMeshGuar,
       "teraLevel2DownStreamMeshMax": teraLevel2DownStreamMeshMax,
       "teraLevel2DownStreamDSlot": teraLevel2DownStreamDSlot,
       "teraLevel2DownStreamMChan": teraLevel2DownStreamMChan,
       "teraLevel2DownStreamrtVBRWeighted": teraLevel2DownStreamrtVBRWeighted,
       "teraLevel2DownStreamrtVBRpeakWeighted": teraLevel2DownStreamrtVBRpeakWeighted,
       "teraLevel2DownStreamnrtVBRWeighted": teraLevel2DownStreamnrtVBRWeighted,
       "teraLevel2DownStreamnrtVBRpeakWeighted": teraLevel2DownStreamnrtVBRpeakWeighted,
       "teraLevel2DownStreamUBRWeighted": teraLevel2DownStreamUBRWeighted,
       "teraLevel2DownStreamUBRMcrWeighted": teraLevel2DownStreamUBRMcrWeighted,
       "teraLevel2DownStreamMeshGuarWeighted": teraLevel2DownStreamMeshGuarWeighted,
       "teraLevel2DownStreamMeshMaxWeighted": teraLevel2DownStreamMeshMaxWeighted,
       "teraLevel2DownStreamTotalScrUse": teraLevel2DownStreamTotalScrUse,
       "teraLevel2DownStreamTotalUse": teraLevel2DownStreamTotalUse,
       "teraLevel2DownStreamTotalWeightedUse": teraLevel2DownStreamTotalWeightedUse,
       "teraLevel2DownStreamTotalBW": teraLevel2DownStreamTotalBW}
)
