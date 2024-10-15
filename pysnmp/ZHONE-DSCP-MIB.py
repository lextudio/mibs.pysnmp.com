# SNMP MIB module (ZHONE-DSCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-DSCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:28 2024
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
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(zhoneIp,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneIp")


# MODULE-IDENTITY

dscpProfile = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DscpProfileTable_Object = MibTable
dscpProfileTable = _DscpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1)
)
if mibBuilder.loadTexts:
    dscpProfileTable.setStatus("current")
_DscpProfileEntry_Object = MibTableRow
dscpProfileEntry = _DscpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1)
)
dscpProfileEntry.setIndexNames(
    (0, "ZHONE-DSCP-MIB", "dscpIndex"),
)
if mibBuilder.loadTexts:
    dscpProfileEntry.setStatus("current")


class _DscpIndex_Type(Integer32):
    """Custom type dscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DscpIndex_Type.__name__ = "Integer32"
_DscpIndex_Object = MibTableColumn
dscpIndex = _DscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 1),
    _DscpIndex_Type()
)
dscpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dscpIndex.setStatus("current")
_DscpProfileRowStatus_Type = RowStatus
_DscpProfileRowStatus_Object = MibTableColumn
dscpProfileRowStatus = _DscpProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 2),
    _DscpProfileRowStatus_Type()
)
dscpProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpProfileRowStatus.setStatus("current")


class _Dscp00map8021p_Type(Integer32):
    """Custom type dscp00map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp00map8021p_Type.__name__ = "Integer32"
_Dscp00map8021p_Object = MibTableColumn
dscp00map8021p = _Dscp00map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 3),
    _Dscp00map8021p_Type()
)
dscp00map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp00map8021p.setStatus("current")


class _Dscp01map8021p_Type(Integer32):
    """Custom type dscp01map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp01map8021p_Type.__name__ = "Integer32"
_Dscp01map8021p_Object = MibTableColumn
dscp01map8021p = _Dscp01map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 4),
    _Dscp01map8021p_Type()
)
dscp01map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp01map8021p.setStatus("current")


class _Dscp02map8021p_Type(Integer32):
    """Custom type dscp02map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp02map8021p_Type.__name__ = "Integer32"
_Dscp02map8021p_Object = MibTableColumn
dscp02map8021p = _Dscp02map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 5),
    _Dscp02map8021p_Type()
)
dscp02map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp02map8021p.setStatus("current")


class _Dscp03map8021p_Type(Integer32):
    """Custom type dscp03map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp03map8021p_Type.__name__ = "Integer32"
_Dscp03map8021p_Object = MibTableColumn
dscp03map8021p = _Dscp03map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 6),
    _Dscp03map8021p_Type()
)
dscp03map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp03map8021p.setStatus("current")


class _Dscp04map8021p_Type(Integer32):
    """Custom type dscp04map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp04map8021p_Type.__name__ = "Integer32"
_Dscp04map8021p_Object = MibTableColumn
dscp04map8021p = _Dscp04map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 7),
    _Dscp04map8021p_Type()
)
dscp04map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp04map8021p.setStatus("current")


class _Dscp05map8021p_Type(Integer32):
    """Custom type dscp05map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp05map8021p_Type.__name__ = "Integer32"
_Dscp05map8021p_Object = MibTableColumn
dscp05map8021p = _Dscp05map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 8),
    _Dscp05map8021p_Type()
)
dscp05map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp05map8021p.setStatus("current")


class _Dscp06map8021p_Type(Integer32):
    """Custom type dscp06map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp06map8021p_Type.__name__ = "Integer32"
_Dscp06map8021p_Object = MibTableColumn
dscp06map8021p = _Dscp06map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 9),
    _Dscp06map8021p_Type()
)
dscp06map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp06map8021p.setStatus("current")


class _Dscp07map8021p_Type(Integer32):
    """Custom type dscp07map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp07map8021p_Type.__name__ = "Integer32"
_Dscp07map8021p_Object = MibTableColumn
dscp07map8021p = _Dscp07map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 10),
    _Dscp07map8021p_Type()
)
dscp07map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp07map8021p.setStatus("current")


class _Dscp08map8021p_Type(Integer32):
    """Custom type dscp08map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp08map8021p_Type.__name__ = "Integer32"
_Dscp08map8021p_Object = MibTableColumn
dscp08map8021p = _Dscp08map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 11),
    _Dscp08map8021p_Type()
)
dscp08map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp08map8021p.setStatus("current")


class _Dscp09map8021p_Type(Integer32):
    """Custom type dscp09map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp09map8021p_Type.__name__ = "Integer32"
_Dscp09map8021p_Object = MibTableColumn
dscp09map8021p = _Dscp09map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 12),
    _Dscp09map8021p_Type()
)
dscp09map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp09map8021p.setStatus("current")


class _Dscp10map8021p_Type(Integer32):
    """Custom type dscp10map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp10map8021p_Type.__name__ = "Integer32"
_Dscp10map8021p_Object = MibTableColumn
dscp10map8021p = _Dscp10map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 13),
    _Dscp10map8021p_Type()
)
dscp10map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp10map8021p.setStatus("current")


class _Dscp11map8021p_Type(Integer32):
    """Custom type dscp11map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp11map8021p_Type.__name__ = "Integer32"
_Dscp11map8021p_Object = MibTableColumn
dscp11map8021p = _Dscp11map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 14),
    _Dscp11map8021p_Type()
)
dscp11map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp11map8021p.setStatus("current")


class _Dscp12map8021p_Type(Integer32):
    """Custom type dscp12map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp12map8021p_Type.__name__ = "Integer32"
_Dscp12map8021p_Object = MibTableColumn
dscp12map8021p = _Dscp12map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 15),
    _Dscp12map8021p_Type()
)
dscp12map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp12map8021p.setStatus("current")


class _Dscp13map8021p_Type(Integer32):
    """Custom type dscp13map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp13map8021p_Type.__name__ = "Integer32"
_Dscp13map8021p_Object = MibTableColumn
dscp13map8021p = _Dscp13map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 16),
    _Dscp13map8021p_Type()
)
dscp13map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp13map8021p.setStatus("current")


class _Dscp14map8021p_Type(Integer32):
    """Custom type dscp14map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp14map8021p_Type.__name__ = "Integer32"
_Dscp14map8021p_Object = MibTableColumn
dscp14map8021p = _Dscp14map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 17),
    _Dscp14map8021p_Type()
)
dscp14map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp14map8021p.setStatus("current")


class _Dscp15map8021p_Type(Integer32):
    """Custom type dscp15map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp15map8021p_Type.__name__ = "Integer32"
_Dscp15map8021p_Object = MibTableColumn
dscp15map8021p = _Dscp15map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 18),
    _Dscp15map8021p_Type()
)
dscp15map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp15map8021p.setStatus("current")


class _Dscp16map8021p_Type(Integer32):
    """Custom type dscp16map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp16map8021p_Type.__name__ = "Integer32"
_Dscp16map8021p_Object = MibTableColumn
dscp16map8021p = _Dscp16map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 19),
    _Dscp16map8021p_Type()
)
dscp16map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp16map8021p.setStatus("current")


class _Dscp17map8021p_Type(Integer32):
    """Custom type dscp17map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp17map8021p_Type.__name__ = "Integer32"
_Dscp17map8021p_Object = MibTableColumn
dscp17map8021p = _Dscp17map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 20),
    _Dscp17map8021p_Type()
)
dscp17map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp17map8021p.setStatus("current")


class _Dscp18map8021p_Type(Integer32):
    """Custom type dscp18map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp18map8021p_Type.__name__ = "Integer32"
_Dscp18map8021p_Object = MibTableColumn
dscp18map8021p = _Dscp18map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 21),
    _Dscp18map8021p_Type()
)
dscp18map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp18map8021p.setStatus("current")


class _Dscp19map8021p_Type(Integer32):
    """Custom type dscp19map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp19map8021p_Type.__name__ = "Integer32"
_Dscp19map8021p_Object = MibTableColumn
dscp19map8021p = _Dscp19map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 22),
    _Dscp19map8021p_Type()
)
dscp19map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp19map8021p.setStatus("current")


class _Dscp20map8021p_Type(Integer32):
    """Custom type dscp20map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp20map8021p_Type.__name__ = "Integer32"
_Dscp20map8021p_Object = MibTableColumn
dscp20map8021p = _Dscp20map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 23),
    _Dscp20map8021p_Type()
)
dscp20map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp20map8021p.setStatus("current")


class _Dscp21map8021p_Type(Integer32):
    """Custom type dscp21map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp21map8021p_Type.__name__ = "Integer32"
_Dscp21map8021p_Object = MibTableColumn
dscp21map8021p = _Dscp21map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 24),
    _Dscp21map8021p_Type()
)
dscp21map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp21map8021p.setStatus("current")


class _Dscp22map8021p_Type(Integer32):
    """Custom type dscp22map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp22map8021p_Type.__name__ = "Integer32"
_Dscp22map8021p_Object = MibTableColumn
dscp22map8021p = _Dscp22map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 25),
    _Dscp22map8021p_Type()
)
dscp22map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp22map8021p.setStatus("current")


class _Dscp23map8021p_Type(Integer32):
    """Custom type dscp23map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp23map8021p_Type.__name__ = "Integer32"
_Dscp23map8021p_Object = MibTableColumn
dscp23map8021p = _Dscp23map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 26),
    _Dscp23map8021p_Type()
)
dscp23map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp23map8021p.setStatus("current")


class _Dscp24map8021p_Type(Integer32):
    """Custom type dscp24map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp24map8021p_Type.__name__ = "Integer32"
_Dscp24map8021p_Object = MibTableColumn
dscp24map8021p = _Dscp24map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 27),
    _Dscp24map8021p_Type()
)
dscp24map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp24map8021p.setStatus("current")


class _Dscp25map8021p_Type(Integer32):
    """Custom type dscp25map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp25map8021p_Type.__name__ = "Integer32"
_Dscp25map8021p_Object = MibTableColumn
dscp25map8021p = _Dscp25map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 28),
    _Dscp25map8021p_Type()
)
dscp25map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp25map8021p.setStatus("current")


class _Dscp26map8021p_Type(Integer32):
    """Custom type dscp26map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp26map8021p_Type.__name__ = "Integer32"
_Dscp26map8021p_Object = MibTableColumn
dscp26map8021p = _Dscp26map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 29),
    _Dscp26map8021p_Type()
)
dscp26map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp26map8021p.setStatus("current")


class _Dscp27map8021p_Type(Integer32):
    """Custom type dscp27map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp27map8021p_Type.__name__ = "Integer32"
_Dscp27map8021p_Object = MibTableColumn
dscp27map8021p = _Dscp27map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 30),
    _Dscp27map8021p_Type()
)
dscp27map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp27map8021p.setStatus("current")


class _Dscp28map8021p_Type(Integer32):
    """Custom type dscp28map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp28map8021p_Type.__name__ = "Integer32"
_Dscp28map8021p_Object = MibTableColumn
dscp28map8021p = _Dscp28map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 31),
    _Dscp28map8021p_Type()
)
dscp28map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp28map8021p.setStatus("current")


class _Dscp29map8021p_Type(Integer32):
    """Custom type dscp29map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp29map8021p_Type.__name__ = "Integer32"
_Dscp29map8021p_Object = MibTableColumn
dscp29map8021p = _Dscp29map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 32),
    _Dscp29map8021p_Type()
)
dscp29map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp29map8021p.setStatus("current")


class _Dscp30map8021p_Type(Integer32):
    """Custom type dscp30map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp30map8021p_Type.__name__ = "Integer32"
_Dscp30map8021p_Object = MibTableColumn
dscp30map8021p = _Dscp30map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 33),
    _Dscp30map8021p_Type()
)
dscp30map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp30map8021p.setStatus("current")


class _Dscp31map8021p_Type(Integer32):
    """Custom type dscp31map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp31map8021p_Type.__name__ = "Integer32"
_Dscp31map8021p_Object = MibTableColumn
dscp31map8021p = _Dscp31map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 34),
    _Dscp31map8021p_Type()
)
dscp31map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp31map8021p.setStatus("current")


class _Dscp32map8021p_Type(Integer32):
    """Custom type dscp32map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp32map8021p_Type.__name__ = "Integer32"
_Dscp32map8021p_Object = MibTableColumn
dscp32map8021p = _Dscp32map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 35),
    _Dscp32map8021p_Type()
)
dscp32map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp32map8021p.setStatus("current")


class _Dscp33map8021p_Type(Integer32):
    """Custom type dscp33map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp33map8021p_Type.__name__ = "Integer32"
_Dscp33map8021p_Object = MibTableColumn
dscp33map8021p = _Dscp33map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 36),
    _Dscp33map8021p_Type()
)
dscp33map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp33map8021p.setStatus("current")


class _Dscp34map8021p_Type(Integer32):
    """Custom type dscp34map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp34map8021p_Type.__name__ = "Integer32"
_Dscp34map8021p_Object = MibTableColumn
dscp34map8021p = _Dscp34map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 37),
    _Dscp34map8021p_Type()
)
dscp34map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp34map8021p.setStatus("current")


class _Dscp35map8021p_Type(Integer32):
    """Custom type dscp35map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp35map8021p_Type.__name__ = "Integer32"
_Dscp35map8021p_Object = MibTableColumn
dscp35map8021p = _Dscp35map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 38),
    _Dscp35map8021p_Type()
)
dscp35map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp35map8021p.setStatus("current")


class _Dscp36map8021p_Type(Integer32):
    """Custom type dscp36map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp36map8021p_Type.__name__ = "Integer32"
_Dscp36map8021p_Object = MibTableColumn
dscp36map8021p = _Dscp36map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 39),
    _Dscp36map8021p_Type()
)
dscp36map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp36map8021p.setStatus("current")


class _Dscp37map8021p_Type(Integer32):
    """Custom type dscp37map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp37map8021p_Type.__name__ = "Integer32"
_Dscp37map8021p_Object = MibTableColumn
dscp37map8021p = _Dscp37map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 40),
    _Dscp37map8021p_Type()
)
dscp37map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp37map8021p.setStatus("current")


class _Dscp38map8021p_Type(Integer32):
    """Custom type dscp38map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp38map8021p_Type.__name__ = "Integer32"
_Dscp38map8021p_Object = MibTableColumn
dscp38map8021p = _Dscp38map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 41),
    _Dscp38map8021p_Type()
)
dscp38map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp38map8021p.setStatus("current")


class _Dscp39map8021p_Type(Integer32):
    """Custom type dscp39map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp39map8021p_Type.__name__ = "Integer32"
_Dscp39map8021p_Object = MibTableColumn
dscp39map8021p = _Dscp39map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 42),
    _Dscp39map8021p_Type()
)
dscp39map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp39map8021p.setStatus("current")


class _Dscp40map8021p_Type(Integer32):
    """Custom type dscp40map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp40map8021p_Type.__name__ = "Integer32"
_Dscp40map8021p_Object = MibTableColumn
dscp40map8021p = _Dscp40map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 43),
    _Dscp40map8021p_Type()
)
dscp40map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp40map8021p.setStatus("current")


class _Dscp41map8021p_Type(Integer32):
    """Custom type dscp41map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp41map8021p_Type.__name__ = "Integer32"
_Dscp41map8021p_Object = MibTableColumn
dscp41map8021p = _Dscp41map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 44),
    _Dscp41map8021p_Type()
)
dscp41map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp41map8021p.setStatus("current")


class _Dscp42map8021p_Type(Integer32):
    """Custom type dscp42map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp42map8021p_Type.__name__ = "Integer32"
_Dscp42map8021p_Object = MibTableColumn
dscp42map8021p = _Dscp42map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 45),
    _Dscp42map8021p_Type()
)
dscp42map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp42map8021p.setStatus("current")


class _Dscp43map8021p_Type(Integer32):
    """Custom type dscp43map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp43map8021p_Type.__name__ = "Integer32"
_Dscp43map8021p_Object = MibTableColumn
dscp43map8021p = _Dscp43map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 46),
    _Dscp43map8021p_Type()
)
dscp43map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp43map8021p.setStatus("current")


class _Dscp44map8021p_Type(Integer32):
    """Custom type dscp44map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp44map8021p_Type.__name__ = "Integer32"
_Dscp44map8021p_Object = MibTableColumn
dscp44map8021p = _Dscp44map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 47),
    _Dscp44map8021p_Type()
)
dscp44map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp44map8021p.setStatus("current")


class _Dscp45map8021p_Type(Integer32):
    """Custom type dscp45map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp45map8021p_Type.__name__ = "Integer32"
_Dscp45map8021p_Object = MibTableColumn
dscp45map8021p = _Dscp45map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 48),
    _Dscp45map8021p_Type()
)
dscp45map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp45map8021p.setStatus("current")


class _Dscp46map8021p_Type(Integer32):
    """Custom type dscp46map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp46map8021p_Type.__name__ = "Integer32"
_Dscp46map8021p_Object = MibTableColumn
dscp46map8021p = _Dscp46map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 49),
    _Dscp46map8021p_Type()
)
dscp46map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp46map8021p.setStatus("current")


class _Dscp47map8021p_Type(Integer32):
    """Custom type dscp47map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp47map8021p_Type.__name__ = "Integer32"
_Dscp47map8021p_Object = MibTableColumn
dscp47map8021p = _Dscp47map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 50),
    _Dscp47map8021p_Type()
)
dscp47map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp47map8021p.setStatus("current")


class _Dscp48map8021p_Type(Integer32):
    """Custom type dscp48map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp48map8021p_Type.__name__ = "Integer32"
_Dscp48map8021p_Object = MibTableColumn
dscp48map8021p = _Dscp48map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 51),
    _Dscp48map8021p_Type()
)
dscp48map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp48map8021p.setStatus("current")


class _Dscp49map8021p_Type(Integer32):
    """Custom type dscp49map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp49map8021p_Type.__name__ = "Integer32"
_Dscp49map8021p_Object = MibTableColumn
dscp49map8021p = _Dscp49map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 52),
    _Dscp49map8021p_Type()
)
dscp49map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp49map8021p.setStatus("current")


class _Dscp50map8021p_Type(Integer32):
    """Custom type dscp50map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp50map8021p_Type.__name__ = "Integer32"
_Dscp50map8021p_Object = MibTableColumn
dscp50map8021p = _Dscp50map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 53),
    _Dscp50map8021p_Type()
)
dscp50map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp50map8021p.setStatus("current")


class _Dscp51map8021p_Type(Integer32):
    """Custom type dscp51map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp51map8021p_Type.__name__ = "Integer32"
_Dscp51map8021p_Object = MibTableColumn
dscp51map8021p = _Dscp51map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 54),
    _Dscp51map8021p_Type()
)
dscp51map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp51map8021p.setStatus("current")


class _Dscp52map8021p_Type(Integer32):
    """Custom type dscp52map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp52map8021p_Type.__name__ = "Integer32"
_Dscp52map8021p_Object = MibTableColumn
dscp52map8021p = _Dscp52map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 55),
    _Dscp52map8021p_Type()
)
dscp52map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp52map8021p.setStatus("current")


class _Dscp53map8021p_Type(Integer32):
    """Custom type dscp53map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp53map8021p_Type.__name__ = "Integer32"
_Dscp53map8021p_Object = MibTableColumn
dscp53map8021p = _Dscp53map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 56),
    _Dscp53map8021p_Type()
)
dscp53map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp53map8021p.setStatus("current")


class _Dscp54map8021p_Type(Integer32):
    """Custom type dscp54map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp54map8021p_Type.__name__ = "Integer32"
_Dscp54map8021p_Object = MibTableColumn
dscp54map8021p = _Dscp54map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 57),
    _Dscp54map8021p_Type()
)
dscp54map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp54map8021p.setStatus("current")


class _Dscp55map8021p_Type(Integer32):
    """Custom type dscp55map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp55map8021p_Type.__name__ = "Integer32"
_Dscp55map8021p_Object = MibTableColumn
dscp55map8021p = _Dscp55map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 58),
    _Dscp55map8021p_Type()
)
dscp55map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp55map8021p.setStatus("current")


class _Dscp56map8021p_Type(Integer32):
    """Custom type dscp56map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp56map8021p_Type.__name__ = "Integer32"
_Dscp56map8021p_Object = MibTableColumn
dscp56map8021p = _Dscp56map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 59),
    _Dscp56map8021p_Type()
)
dscp56map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp56map8021p.setStatus("current")


class _Dscp57map8021p_Type(Integer32):
    """Custom type dscp57map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp57map8021p_Type.__name__ = "Integer32"
_Dscp57map8021p_Object = MibTableColumn
dscp57map8021p = _Dscp57map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 60),
    _Dscp57map8021p_Type()
)
dscp57map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp57map8021p.setStatus("current")


class _Dscp58map8021p_Type(Integer32):
    """Custom type dscp58map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp58map8021p_Type.__name__ = "Integer32"
_Dscp58map8021p_Object = MibTableColumn
dscp58map8021p = _Dscp58map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 61),
    _Dscp58map8021p_Type()
)
dscp58map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp58map8021p.setStatus("current")


class _Dscp59map8021p_Type(Integer32):
    """Custom type dscp59map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp59map8021p_Type.__name__ = "Integer32"
_Dscp59map8021p_Object = MibTableColumn
dscp59map8021p = _Dscp59map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 62),
    _Dscp59map8021p_Type()
)
dscp59map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp59map8021p.setStatus("current")


class _Dscp60map8021p_Type(Integer32):
    """Custom type dscp60map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp60map8021p_Type.__name__ = "Integer32"
_Dscp60map8021p_Object = MibTableColumn
dscp60map8021p = _Dscp60map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 63),
    _Dscp60map8021p_Type()
)
dscp60map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp60map8021p.setStatus("current")


class _Dscp61map8021p_Type(Integer32):
    """Custom type dscp61map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp61map8021p_Type.__name__ = "Integer32"
_Dscp61map8021p_Object = MibTableColumn
dscp61map8021p = _Dscp61map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 64),
    _Dscp61map8021p_Type()
)
dscp61map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp61map8021p.setStatus("current")


class _Dscp62map8021p_Type(Integer32):
    """Custom type dscp62map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp62map8021p_Type.__name__ = "Integer32"
_Dscp62map8021p_Object = MibTableColumn
dscp62map8021p = _Dscp62map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 65),
    _Dscp62map8021p_Type()
)
dscp62map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp62map8021p.setStatus("current")


class _Dscp63map8021p_Type(Integer32):
    """Custom type dscp63map8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Dscp63map8021p_Type.__name__ = "Integer32"
_Dscp63map8021p_Object = MibTableColumn
dscp63map8021p = _Dscp63map8021p_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 1, 1, 66),
    _Dscp63map8021p_Type()
)
dscp63map8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscp63map8021p.setStatus("current")

# Managed Objects groups

dscpProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 2)
)
dscpProfileGroup.setObjects(
    ("ZHONE-DSCP-MIB", "dscpProfileRowStatus")
)
if mibBuilder.loadTexts:
    dscpProfileGroup.setStatus("current")

dscpProfileGroupObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 1, 22, 3)
)
dscpProfileGroupObjectGroup.setObjects(
      *(("ZHONE-DSCP-MIB", "dscp00map8021p"),
        ("ZHONE-DSCP-MIB", "dscp01map8021p"),
        ("ZHONE-DSCP-MIB", "dscp02map8021p"),
        ("ZHONE-DSCP-MIB", "dscp03map8021p"),
        ("ZHONE-DSCP-MIB", "dscp04map8021p"),
        ("ZHONE-DSCP-MIB", "dscp05map8021p"),
        ("ZHONE-DSCP-MIB", "dscp06map8021p"),
        ("ZHONE-DSCP-MIB", "dscp07map8021p"),
        ("ZHONE-DSCP-MIB", "dscp08map8021p"),
        ("ZHONE-DSCP-MIB", "dscp09map8021p"),
        ("ZHONE-DSCP-MIB", "dscp10map8021p"),
        ("ZHONE-DSCP-MIB", "dscp11map8021p"),
        ("ZHONE-DSCP-MIB", "dscp12map8021p"),
        ("ZHONE-DSCP-MIB", "dscp13map8021p"),
        ("ZHONE-DSCP-MIB", "dscp14map8021p"),
        ("ZHONE-DSCP-MIB", "dscp15map8021p"),
        ("ZHONE-DSCP-MIB", "dscp16map8021p"),
        ("ZHONE-DSCP-MIB", "dscp17map8021p"),
        ("ZHONE-DSCP-MIB", "dscp18map8021p"),
        ("ZHONE-DSCP-MIB", "dscp19map8021p"),
        ("ZHONE-DSCP-MIB", "dscp20map8021p"),
        ("ZHONE-DSCP-MIB", "dscp21map8021p"),
        ("ZHONE-DSCP-MIB", "dscp22map8021p"),
        ("ZHONE-DSCP-MIB", "dscp23map8021p"),
        ("ZHONE-DSCP-MIB", "dscp24map8021p"),
        ("ZHONE-DSCP-MIB", "dscp25map8021p"),
        ("ZHONE-DSCP-MIB", "dscp26map8021p"),
        ("ZHONE-DSCP-MIB", "dscp27map8021p"),
        ("ZHONE-DSCP-MIB", "dscp28map8021p"),
        ("ZHONE-DSCP-MIB", "dscp29map8021p"),
        ("ZHONE-DSCP-MIB", "dscp30map8021p"),
        ("ZHONE-DSCP-MIB", "dscp31map8021p"),
        ("ZHONE-DSCP-MIB", "dscp32map8021p"),
        ("ZHONE-DSCP-MIB", "dscp33map8021p"),
        ("ZHONE-DSCP-MIB", "dscp34map8021p"),
        ("ZHONE-DSCP-MIB", "dscp35map8021p"),
        ("ZHONE-DSCP-MIB", "dscp36map8021p"),
        ("ZHONE-DSCP-MIB", "dscp37map8021p"),
        ("ZHONE-DSCP-MIB", "dscp38map8021p"),
        ("ZHONE-DSCP-MIB", "dscp39map8021p"),
        ("ZHONE-DSCP-MIB", "dscp40map8021p"),
        ("ZHONE-DSCP-MIB", "dscp41map8021p"),
        ("ZHONE-DSCP-MIB", "dscp42map8021p"),
        ("ZHONE-DSCP-MIB", "dscp43map8021p"),
        ("ZHONE-DSCP-MIB", "dscp44map8021p"),
        ("ZHONE-DSCP-MIB", "dscp45map8021p"),
        ("ZHONE-DSCP-MIB", "dscp46map8021p"),
        ("ZHONE-DSCP-MIB", "dscp47map8021p"),
        ("ZHONE-DSCP-MIB", "dscp48map8021p"),
        ("ZHONE-DSCP-MIB", "dscp49map8021p"),
        ("ZHONE-DSCP-MIB", "dscp50map8021p"),
        ("ZHONE-DSCP-MIB", "dscp51map8021p"),
        ("ZHONE-DSCP-MIB", "dscp52map8021p"),
        ("ZHONE-DSCP-MIB", "dscp53map8021p"),
        ("ZHONE-DSCP-MIB", "dscp54map8021p"),
        ("ZHONE-DSCP-MIB", "dscp55map8021p"),
        ("ZHONE-DSCP-MIB", "dscp56map8021p"),
        ("ZHONE-DSCP-MIB", "dscp57map8021p"),
        ("ZHONE-DSCP-MIB", "dscp58map8021p"),
        ("ZHONE-DSCP-MIB", "dscp59map8021p"),
        ("ZHONE-DSCP-MIB", "dscp60map8021p"),
        ("ZHONE-DSCP-MIB", "dscp61map8021p"),
        ("ZHONE-DSCP-MIB", "dscp62map8021p"),
        ("ZHONE-DSCP-MIB", "dscp63map8021p"))
)
if mibBuilder.loadTexts:
    dscpProfileGroupObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-DSCP-MIB",
    **{"dscpProfile": dscpProfile,
       "dscpProfileTable": dscpProfileTable,
       "dscpProfileEntry": dscpProfileEntry,
       "dscpIndex": dscpIndex,
       "dscpProfileRowStatus": dscpProfileRowStatus,
       "dscp00map8021p": dscp00map8021p,
       "dscp01map8021p": dscp01map8021p,
       "dscp02map8021p": dscp02map8021p,
       "dscp03map8021p": dscp03map8021p,
       "dscp04map8021p": dscp04map8021p,
       "dscp05map8021p": dscp05map8021p,
       "dscp06map8021p": dscp06map8021p,
       "dscp07map8021p": dscp07map8021p,
       "dscp08map8021p": dscp08map8021p,
       "dscp09map8021p": dscp09map8021p,
       "dscp10map8021p": dscp10map8021p,
       "dscp11map8021p": dscp11map8021p,
       "dscp12map8021p": dscp12map8021p,
       "dscp13map8021p": dscp13map8021p,
       "dscp14map8021p": dscp14map8021p,
       "dscp15map8021p": dscp15map8021p,
       "dscp16map8021p": dscp16map8021p,
       "dscp17map8021p": dscp17map8021p,
       "dscp18map8021p": dscp18map8021p,
       "dscp19map8021p": dscp19map8021p,
       "dscp20map8021p": dscp20map8021p,
       "dscp21map8021p": dscp21map8021p,
       "dscp22map8021p": dscp22map8021p,
       "dscp23map8021p": dscp23map8021p,
       "dscp24map8021p": dscp24map8021p,
       "dscp25map8021p": dscp25map8021p,
       "dscp26map8021p": dscp26map8021p,
       "dscp27map8021p": dscp27map8021p,
       "dscp28map8021p": dscp28map8021p,
       "dscp29map8021p": dscp29map8021p,
       "dscp30map8021p": dscp30map8021p,
       "dscp31map8021p": dscp31map8021p,
       "dscp32map8021p": dscp32map8021p,
       "dscp33map8021p": dscp33map8021p,
       "dscp34map8021p": dscp34map8021p,
       "dscp35map8021p": dscp35map8021p,
       "dscp36map8021p": dscp36map8021p,
       "dscp37map8021p": dscp37map8021p,
       "dscp38map8021p": dscp38map8021p,
       "dscp39map8021p": dscp39map8021p,
       "dscp40map8021p": dscp40map8021p,
       "dscp41map8021p": dscp41map8021p,
       "dscp42map8021p": dscp42map8021p,
       "dscp43map8021p": dscp43map8021p,
       "dscp44map8021p": dscp44map8021p,
       "dscp45map8021p": dscp45map8021p,
       "dscp46map8021p": dscp46map8021p,
       "dscp47map8021p": dscp47map8021p,
       "dscp48map8021p": dscp48map8021p,
       "dscp49map8021p": dscp49map8021p,
       "dscp50map8021p": dscp50map8021p,
       "dscp51map8021p": dscp51map8021p,
       "dscp52map8021p": dscp52map8021p,
       "dscp53map8021p": dscp53map8021p,
       "dscp54map8021p": dscp54map8021p,
       "dscp55map8021p": dscp55map8021p,
       "dscp56map8021p": dscp56map8021p,
       "dscp57map8021p": dscp57map8021p,
       "dscp58map8021p": dscp58map8021p,
       "dscp59map8021p": dscp59map8021p,
       "dscp60map8021p": dscp60map8021p,
       "dscp61map8021p": dscp61map8021p,
       "dscp62map8021p": dscp62map8021p,
       "dscp63map8021p": dscp63map8021p,
       "dscpProfileGroup": dscpProfileGroup,
       "dscpProfileGroupObjectGroup": dscpProfileGroupObjectGroup}
)
