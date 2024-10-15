# SNMP MIB module (RANGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RANGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:30 2024
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


# MODULE-IDENTITY

rangeTestMIB = ModuleIdentity(
    (1, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RangeObj_ObjectIdentity = ObjectIdentity
rangeObj = _RangeObj_ObjectIdentity(
    (1, 1, 2)
)
_Obj01_Type = Integer32
_Obj01_Object = MibScalar
obj01 = _Obj01_Object(
    (1, 1, 2, 1),
    _Obj01_Type()
)
obj01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj01.setStatus("current")


class _Obj02_Type(Integer32):
    """Custom type obj02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Obj02_Type.__name__ = "Integer32"
_Obj02_Object = MibScalar
obj02 = _Obj02_Object(
    (1, 1, 2, 2),
    _Obj02_Type()
)
obj02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj02.setStatus("current")


class _Obj03_Type(Integer32):
    """Custom type obj03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Obj03_Type.__name__ = "Integer32"
_Obj03_Object = MibScalar
obj03 = _Obj03_Object(
    (1, 1, 2, 3),
    _Obj03_Type()
)
obj03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj03.setStatus("current")


class _Obj04_Type(Integer32):
    """Custom type obj04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
    )


_Obj04_Type.__name__ = "Integer32"
_Obj04_Object = MibScalar
obj04 = _Obj04_Object(
    (1, 1, 2, 4),
    _Obj04_Type()
)
obj04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj04.setStatus("current")


class _Obj05_Type(Integer32):
    """Custom type obj05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_Obj05_Type.__name__ = "Integer32"
_Obj05_Object = MibScalar
obj05 = _Obj05_Object(
    (1, 1, 2, 5),
    _Obj05_Type()
)
obj05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj05.setStatus("current")


class _Obj06_Type(Integer32):
    """Custom type obj06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Obj06_Type.__name__ = "Integer32"
_Obj06_Object = MibScalar
obj06 = _Obj06_Object(
    (1, 1, 2, 6),
    _Obj06_Type()
)
obj06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj06.setStatus("current")


class _Obj07_Type(Integer32):
    """Custom type obj07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10),
    )


_Obj07_Type.__name__ = "Integer32"
_Obj07_Object = MibScalar
obj07 = _Obj07_Object(
    (1, 1, 2, 7),
    _Obj07_Type()
)
obj07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj07.setStatus("current")


class _Obj08_Type(Integer32):
    """Custom type obj08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(0, 0),
    )


_Obj08_Type.__name__ = "Integer32"
_Obj08_Object = MibScalar
obj08 = _Obj08_Object(
    (1, 1, 2, 8),
    _Obj08_Type()
)
obj08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj08.setStatus("current")


class _Obj09_Type(Integer32):
    """Custom type obj09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Obj09_Type.__name__ = "Integer32"
_Obj09_Object = MibScalar
obj09 = _Obj09_Object(
    (1, 1, 2, 9),
    _Obj09_Type()
)
obj09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj09.setStatus("current")


class _Obj10_Type(Integer32):
    """Custom type obj10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2147483647, 2147483647),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 10),
    )


_Obj10_Type.__name__ = "Integer32"
_Obj10_Object = MibScalar
obj10 = _Obj10_Object(
    (1, 1, 2, 10),
    _Obj10_Type()
)
obj10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj10.setStatus("current")


class _Obj11_Type(Integer32):
    """Custom type obj11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 10),
    )


_Obj11_Type.__name__ = "Integer32"
_Obj11_Object = MibScalar
obj11 = _Obj11_Object(
    (1, 1, 2, 11),
    _Obj11_Type()
)
obj11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj11.setStatus("current")


class _Obj12_Type(Integer32):
    """Custom type obj12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(-1, -1),
    )


_Obj12_Type.__name__ = "Integer32"
_Obj12_Object = MibScalar
obj12 = _Obj12_Object(
    (1, 1, 2, 12),
    _Obj12_Type()
)
obj12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj12.setStatus("current")


class _Obj13_Type(Integer32):
    """Custom type obj13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-1, -1),
    )


_Obj13_Type.__name__ = "Integer32"
_Obj13_Object = MibScalar
obj13 = _Obj13_Object(
    (1, 1, 2, 13),
    _Obj13_Type()
)
obj13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj13.setStatus("current")


class _Obj14_Type(Integer32):
    """Custom type obj14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(-2147483648, -2147483648),
    )


_Obj14_Type.__name__ = "Integer32"
_Obj14_Object = MibScalar
obj14 = _Obj14_Object(
    (1, 1, 2, 14),
    _Obj14_Type()
)
obj14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj14.setStatus("current")


class _Obj15_Type(Integer32):
    """Custom type obj15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -2147483648),
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(10, 10),
        ValueRangeConstraint(0, 0),
    )


_Obj15_Type.__name__ = "Integer32"
_Obj15_Object = MibScalar
obj15 = _Obj15_Object(
    (1, 1, 2, 15),
    _Obj15_Type()
)
obj15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj15.setStatus("current")


class _Obj21_Type(Integer32):
    """Custom type obj21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Obj21_Type.__name__ = "Integer32"
_Obj21_Object = MibScalar
obj21 = _Obj21_Object(
    (1, 1, 2, 21),
    _Obj21_Type()
)
obj21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj21.setStatus("current")


class _Obj22_Type(Integer32):
    """Custom type obj22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Obj22_Type.__name__ = "Integer32"
_Obj22_Object = MibScalar
obj22 = _Obj22_Object(
    (1, 1, 2, 22),
    _Obj22_Type()
)
obj22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj22.setStatus("current")


class _Obj23_Type(Integer32):
    """Custom type obj23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Obj23_Type.__name__ = "Integer32"
_Obj23_Object = MibScalar
obj23 = _Obj23_Object(
    (1, 1, 2, 23),
    _Obj23_Type()
)
obj23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj23.setStatus("current")


class _Obj24_Type(Integer32):
    """Custom type obj24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Obj24_Type.__name__ = "Integer32"
_Obj24_Object = MibScalar
obj24 = _Obj24_Object(
    (1, 1, 2, 24),
    _Obj24_Type()
)
obj24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj24.setStatus("current")


class _Obj25_Type(Integer32):
    """Custom type obj25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -1),
    )


_Obj25_Type.__name__ = "Integer32"
_Obj25_Object = MibScalar
obj25 = _Obj25_Object(
    (1, 1, 2, 25),
    _Obj25_Type()
)
obj25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj25.setStatus("current")


class _Obj26_Type(Integer32):
    """Custom type obj26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 0),
    )


_Obj26_Type.__name__ = "Integer32"
_Obj26_Object = MibScalar
obj26 = _Obj26_Object(
    (1, 1, 2, 26),
    _Obj26_Type()
)
obj26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj26.setStatus("current")


class _Obj27_Type(Integer32):
    """Custom type obj27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_Obj27_Type.__name__ = "Integer32"
_Obj27_Object = MibScalar
obj27 = _Obj27_Object(
    (1, 1, 2, 27),
    _Obj27_Type()
)
obj27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj27.setStatus("current")


class _Obj28_Type(Integer32):
    """Custom type obj28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_Obj28_Type.__name__ = "Integer32"
_Obj28_Object = MibScalar
obj28 = _Obj28_Object(
    (1, 1, 2, 28),
    _Obj28_Type()
)
obj28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj28.setStatus("current")


class _Obj31_Type(Integer32):
    """Custom type obj31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 10),
    )


_Obj31_Type.__name__ = "Integer32"
_Obj31_Object = MibScalar
obj31 = _Obj31_Object(
    (1, 1, 2, 31),
    _Obj31_Type()
)
obj31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj31.setStatus("current")


class _Obj32_Type(Integer32):
    """Custom type obj32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(0, 0),
    )


_Obj32_Type.__name__ = "Integer32"
_Obj32_Object = MibScalar
obj32 = _Obj32_Object(
    (1, 1, 2, 32),
    _Obj32_Type()
)
obj32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj32.setStatus("current")


class _Obj33_Type(Integer32):
    """Custom type obj33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, -1),
        ValueRangeConstraint(1, 2147483647),
    )


_Obj33_Type.__name__ = "Integer32"
_Obj33_Object = MibScalar
obj33 = _Obj33_Object(
    (1, 1, 2, 33),
    _Obj33_Type()
)
obj33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj33.setStatus("current")


class _Obj34_Type(Integer32):
    """Custom type obj34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
        ValueRangeConstraint(-2147483648, -1),
    )


_Obj34_Type.__name__ = "Integer32"
_Obj34_Object = MibScalar
obj34 = _Obj34_Object(
    (1, 1, 2, 34),
    _Obj34_Type()
)
obj34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj34.setStatus("current")


class _Obj35_Type(Integer32):
    """Custom type obj35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, -60),
        ValueRangeConstraint(-40, -5),
        ValueRangeConstraint(-1, 3),
        ValueRangeConstraint(5, 10),
        ValueRangeConstraint(100, 400),
    )


_Obj35_Type.__name__ = "Integer32"
_Obj35_Object = MibScalar
obj35 = _Obj35_Object(
    (1, 1, 2, 35),
    _Obj35_Type()
)
obj35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj35.setStatus("current")


class _Obj36_Type(Integer32):
    """Custom type obj36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, -200),
        ValueRangeConstraint(200, 200),
        ValueRangeConstraint(-199, -199),
        ValueRangeConstraint(199, 199),
        ValueRangeConstraint(-198, -198),
        ValueRangeConstraint(198, 198),
        ValueRangeConstraint(-197, -197),
        ValueRangeConstraint(197, 197),
        ValueRangeConstraint(-196, -196),
        ValueRangeConstraint(196, 196),
        ValueRangeConstraint(-195, -195),
        ValueRangeConstraint(195, 195),
        ValueRangeConstraint(-194, -194),
        ValueRangeConstraint(194, 194),
        ValueRangeConstraint(-193, -193),
        ValueRangeConstraint(193, 193),
        ValueRangeConstraint(-192, -192),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(-191, -191),
        ValueRangeConstraint(191, 191),
        ValueRangeConstraint(-190, -190),
        ValueRangeConstraint(190, 190),
    )


_Obj36_Type.__name__ = "Integer32"
_Obj36_Object = MibScalar
obj36 = _Obj36_Object(
    (1, 1, 2, 36),
    _Obj36_Type()
)
obj36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj36.setStatus("current")


class _Obj37_Type(Integer32):
    """Custom type obj37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, -190),
        ValueRangeConstraint(190, 200),
        ValueRangeConstraint(-170, -160),
        ValueRangeConstraint(160, 170),
        ValueRangeConstraint(-150, -140),
        ValueRangeConstraint(140, 150),
        ValueRangeConstraint(-120, -100),
        ValueRangeConstraint(100, 120),
    )


_Obj37_Type.__name__ = "Integer32"
_Obj37_Object = MibScalar
obj37 = _Obj37_Object(
    (1, 1, 2, 37),
    _Obj37_Type()
)
obj37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    obj37.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RANGE-MIB",
    **{"rangeTestMIB": rangeTestMIB,
       "rangeObj": rangeObj,
       "obj01": obj01,
       "obj02": obj02,
       "obj03": obj03,
       "obj04": obj04,
       "obj05": obj05,
       "obj06": obj06,
       "obj07": obj07,
       "obj08": obj08,
       "obj09": obj09,
       "obj10": obj10,
       "obj11": obj11,
       "obj12": obj12,
       "obj13": obj13,
       "obj14": obj14,
       "obj15": obj15,
       "obj21": obj21,
       "obj22": obj22,
       "obj23": obj23,
       "obj24": obj24,
       "obj25": obj25,
       "obj26": obj26,
       "obj27": obj27,
       "obj28": obj28,
       "obj31": obj31,
       "obj32": obj32,
       "obj33": obj33,
       "obj34": obj34,
       "obj35": obj35,
       "obj36": obj36,
       "obj37": obj37}
)
