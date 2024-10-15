# SNMP MIB module (ROOMALERT24E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ROOMALERT24E-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:13 2024
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
 NotificationType,
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
    "NotificationType",
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

_Avtech_ObjectIdentity = ObjectIdentity
avtech = _Avtech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1)
)
_Roomalert24e_ObjectIdentity = ObjectIdentity
roomalert24e = _Roomalert24e_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1)
)


class _Internal_tempf_Type(Integer32):
    """Custom type internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_tempf_Type.__name__ = "Integer32"
_Internal_tempf_Object = MibScalar
internal_tempf = _Internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1, 1),
    _Internal_tempf_Type()
)
internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_tempf.setStatus("mandatory")


class _Internal_tempc_Type(Integer32):
    """Custom type internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_tempc_Type.__name__ = "Integer32"
_Internal_tempc_Object = MibScalar
internal_tempc = _Internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1, 2),
    _Internal_tempc_Type()
)
internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_tempc.setStatus("mandatory")
_Humidity_ObjectIdentity = ObjectIdentity
humidity = _Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 2)
)


class _Internal_humidity_Type(Integer32):
    """Custom type internal_humidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_humidity_Type.__name__ = "Integer32"
_Internal_humidity_Object = MibScalar
internal_humidity = _Internal_humidity_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 2, 1),
    _Internal_humidity_Type()
)
internal_humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_humidity.setStatus("mandatory")
_Heat_index_ObjectIdentity = ObjectIdentity
heat_index = _Heat_index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3)
)


class _Internal_heat_index_Type(Integer32):
    """Custom type internal_heat_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_heat_index_Type.__name__ = "Integer32"
_Internal_heat_index_Object = MibScalar
internal_heat_index = _Internal_heat_index_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3, 1),
    _Internal_heat_index_Type()
)
internal_heat_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_heat_index.setStatus("mandatory")


class _Internal_heat_indexc_Type(Integer32):
    """Custom type internal_heat_indexc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_heat_indexc_Type.__name__ = "Integer32"
_Internal_heat_indexc_Object = MibScalar
internal_heat_indexc = _Internal_heat_indexc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3, 2),
    _Internal_heat_indexc_Type()
)
internal_heat_indexc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_heat_indexc.setStatus("mandatory")
_Digital_ObjectIdentity = ObjectIdentity
digital = _Digital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2)
)
_Digital_sen1_ObjectIdentity = ObjectIdentity
digital_sen1 = _Digital_sen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1)
)


class _Digital_sen1_1_Type(Integer32):
    """Custom type digital_sen1_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_1_Type.__name__ = "Integer32"
_Digital_sen1_1_Object = MibScalar
digital_sen1_1 = _Digital_sen1_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 1),
    _Digital_sen1_1_Type()
)
digital_sen1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_1.setStatus("mandatory")


class _Digital_sen1_2_Type(Integer32):
    """Custom type digital_sen1_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_2_Type.__name__ = "Integer32"
_Digital_sen1_2_Object = MibScalar
digital_sen1_2 = _Digital_sen1_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 2),
    _Digital_sen1_2_Type()
)
digital_sen1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_2.setStatus("mandatory")


class _Digital_sen1_3_Type(Integer32):
    """Custom type digital_sen1_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_3_Type.__name__ = "Integer32"
_Digital_sen1_3_Object = MibScalar
digital_sen1_3 = _Digital_sen1_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 3),
    _Digital_sen1_3_Type()
)
digital_sen1_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_3.setStatus("mandatory")


class _Digital_sen1_4_Type(Integer32):
    """Custom type digital_sen1_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_4_Type.__name__ = "Integer32"
_Digital_sen1_4_Object = MibScalar
digital_sen1_4 = _Digital_sen1_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 4),
    _Digital_sen1_4_Type()
)
digital_sen1_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_4.setStatus("mandatory")


class _Digital_sen1_5_Type(Integer32):
    """Custom type digital_sen1_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_5_Type.__name__ = "Integer32"
_Digital_sen1_5_Object = MibScalar
digital_sen1_5 = _Digital_sen1_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 5),
    _Digital_sen1_5_Type()
)
digital_sen1_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_5.setStatus("mandatory")
_Digital_sen2_ObjectIdentity = ObjectIdentity
digital_sen2 = _Digital_sen2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2)
)


class _Digital_sen2_1_Type(Integer32):
    """Custom type digital_sen2_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_1_Type.__name__ = "Integer32"
_Digital_sen2_1_Object = MibScalar
digital_sen2_1 = _Digital_sen2_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 1),
    _Digital_sen2_1_Type()
)
digital_sen2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_1.setStatus("mandatory")


class _Digital_sen2_2_Type(Integer32):
    """Custom type digital_sen2_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_2_Type.__name__ = "Integer32"
_Digital_sen2_2_Object = MibScalar
digital_sen2_2 = _Digital_sen2_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 2),
    _Digital_sen2_2_Type()
)
digital_sen2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_2.setStatus("mandatory")


class _Digital_sen2_3_Type(Integer32):
    """Custom type digital_sen2_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_3_Type.__name__ = "Integer32"
_Digital_sen2_3_Object = MibScalar
digital_sen2_3 = _Digital_sen2_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 3),
    _Digital_sen2_3_Type()
)
digital_sen2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_3.setStatus("mandatory")


class _Digital_sen2_4_Type(Integer32):
    """Custom type digital_sen2_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_4_Type.__name__ = "Integer32"
_Digital_sen2_4_Object = MibScalar
digital_sen2_4 = _Digital_sen2_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 4),
    _Digital_sen2_4_Type()
)
digital_sen2_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_4.setStatus("mandatory")


class _Digital_sen2_5_Type(Integer32):
    """Custom type digital_sen2_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_5_Type.__name__ = "Integer32"
_Digital_sen2_5_Object = MibScalar
digital_sen2_5 = _Digital_sen2_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 5),
    _Digital_sen2_5_Type()
)
digital_sen2_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_5.setStatus("mandatory")
_Digital_sen3_ObjectIdentity = ObjectIdentity
digital_sen3 = _Digital_sen3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3)
)


class _Digital_sen3_1_Type(Integer32):
    """Custom type digital_sen3_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_1_Type.__name__ = "Integer32"
_Digital_sen3_1_Object = MibScalar
digital_sen3_1 = _Digital_sen3_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 1),
    _Digital_sen3_1_Type()
)
digital_sen3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_1.setStatus("mandatory")


class _Digital_sen3_2_Type(Integer32):
    """Custom type digital_sen3_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_2_Type.__name__ = "Integer32"
_Digital_sen3_2_Object = MibScalar
digital_sen3_2 = _Digital_sen3_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 2),
    _Digital_sen3_2_Type()
)
digital_sen3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_2.setStatus("mandatory")


class _Digital_sen3_3_Type(Integer32):
    """Custom type digital_sen3_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_3_Type.__name__ = "Integer32"
_Digital_sen3_3_Object = MibScalar
digital_sen3_3 = _Digital_sen3_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 3),
    _Digital_sen3_3_Type()
)
digital_sen3_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_3.setStatus("mandatory")


class _Digital_sen3_4_Type(Integer32):
    """Custom type digital_sen3_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_4_Type.__name__ = "Integer32"
_Digital_sen3_4_Object = MibScalar
digital_sen3_4 = _Digital_sen3_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 4),
    _Digital_sen3_4_Type()
)
digital_sen3_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_4.setStatus("mandatory")


class _Digital_sen3_5_Type(Integer32):
    """Custom type digital_sen3_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_5_Type.__name__ = "Integer32"
_Digital_sen3_5_Object = MibScalar
digital_sen3_5 = _Digital_sen3_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 5),
    _Digital_sen3_5_Type()
)
digital_sen3_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_5.setStatus("mandatory")
_Digital_sen4_ObjectIdentity = ObjectIdentity
digital_sen4 = _Digital_sen4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4)
)


class _Digital_sen4_1_Type(Integer32):
    """Custom type digital_sen4_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_1_Type.__name__ = "Integer32"
_Digital_sen4_1_Object = MibScalar
digital_sen4_1 = _Digital_sen4_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 1),
    _Digital_sen4_1_Type()
)
digital_sen4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_1.setStatus("mandatory")


class _Digital_sen4_2_Type(Integer32):
    """Custom type digital_sen4_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_2_Type.__name__ = "Integer32"
_Digital_sen4_2_Object = MibScalar
digital_sen4_2 = _Digital_sen4_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 2),
    _Digital_sen4_2_Type()
)
digital_sen4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_2.setStatus("mandatory")


class _Digital_sen4_3_Type(Integer32):
    """Custom type digital_sen4_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_3_Type.__name__ = "Integer32"
_Digital_sen4_3_Object = MibScalar
digital_sen4_3 = _Digital_sen4_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 3),
    _Digital_sen4_3_Type()
)
digital_sen4_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_3.setStatus("mandatory")


class _Digital_sen4_4_Type(Integer32):
    """Custom type digital_sen4_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_4_Type.__name__ = "Integer32"
_Digital_sen4_4_Object = MibScalar
digital_sen4_4 = _Digital_sen4_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 4),
    _Digital_sen4_4_Type()
)
digital_sen4_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_4.setStatus("mandatory")


class _Digital_sen4_5_Type(Integer32):
    """Custom type digital_sen4_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_5_Type.__name__ = "Integer32"
_Digital_sen4_5_Object = MibScalar
digital_sen4_5 = _Digital_sen4_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 5),
    _Digital_sen4_5_Type()
)
digital_sen4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_5.setStatus("mandatory")
_Digital_sen5_ObjectIdentity = ObjectIdentity
digital_sen5 = _Digital_sen5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5)
)


class _Digital_sen5_1_Type(Integer32):
    """Custom type digital_sen5_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_1_Type.__name__ = "Integer32"
_Digital_sen5_1_Object = MibScalar
digital_sen5_1 = _Digital_sen5_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 1),
    _Digital_sen5_1_Type()
)
digital_sen5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_1.setStatus("mandatory")


class _Digital_sen5_2_Type(Integer32):
    """Custom type digital_sen5_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_2_Type.__name__ = "Integer32"
_Digital_sen5_2_Object = MibScalar
digital_sen5_2 = _Digital_sen5_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 2),
    _Digital_sen5_2_Type()
)
digital_sen5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_2.setStatus("mandatory")


class _Digital_sen5_3_Type(Integer32):
    """Custom type digital_sen5_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_3_Type.__name__ = "Integer32"
_Digital_sen5_3_Object = MibScalar
digital_sen5_3 = _Digital_sen5_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 3),
    _Digital_sen5_3_Type()
)
digital_sen5_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_3.setStatus("mandatory")


class _Digital_sen5_4_Type(Integer32):
    """Custom type digital_sen5_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_4_Type.__name__ = "Integer32"
_Digital_sen5_4_Object = MibScalar
digital_sen5_4 = _Digital_sen5_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 4),
    _Digital_sen5_4_Type()
)
digital_sen5_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_4.setStatus("mandatory")


class _Digital_sen5_5_Type(Integer32):
    """Custom type digital_sen5_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_5_Type.__name__ = "Integer32"
_Digital_sen5_5_Object = MibScalar
digital_sen5_5 = _Digital_sen5_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 5),
    _Digital_sen5_5_Type()
)
digital_sen5_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_5.setStatus("mandatory")
_Digital_sen6_ObjectIdentity = ObjectIdentity
digital_sen6 = _Digital_sen6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6)
)


class _Digital_sen6_1_Type(Integer32):
    """Custom type digital_sen6_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_1_Type.__name__ = "Integer32"
_Digital_sen6_1_Object = MibScalar
digital_sen6_1 = _Digital_sen6_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 1),
    _Digital_sen6_1_Type()
)
digital_sen6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_1.setStatus("mandatory")


class _Digital_sen6_2_Type(Integer32):
    """Custom type digital_sen6_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_2_Type.__name__ = "Integer32"
_Digital_sen6_2_Object = MibScalar
digital_sen6_2 = _Digital_sen6_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 2),
    _Digital_sen6_2_Type()
)
digital_sen6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_2.setStatus("mandatory")


class _Digital_sen6_3_Type(Integer32):
    """Custom type digital_sen6_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_3_Type.__name__ = "Integer32"
_Digital_sen6_3_Object = MibScalar
digital_sen6_3 = _Digital_sen6_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 3),
    _Digital_sen6_3_Type()
)
digital_sen6_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_3.setStatus("mandatory")


class _Digital_sen6_4_Type(Integer32):
    """Custom type digital_sen6_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_4_Type.__name__ = "Integer32"
_Digital_sen6_4_Object = MibScalar
digital_sen6_4 = _Digital_sen6_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 4),
    _Digital_sen6_4_Type()
)
digital_sen6_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_4.setStatus("mandatory")


class _Digital_sen6_5_Type(Integer32):
    """Custom type digital_sen6_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_5_Type.__name__ = "Integer32"
_Digital_sen6_5_Object = MibScalar
digital_sen6_5 = _Digital_sen6_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 5),
    _Digital_sen6_5_Type()
)
digital_sen6_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_5.setStatus("mandatory")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3)
)


class _Switch_sen1_Type(Integer32):
    """Custom type switch_sen1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen1_Type.__name__ = "Integer32"
_Switch_sen1_Object = MibScalar
switch_sen1 = _Switch_sen1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 1),
    _Switch_sen1_Type()
)
switch_sen1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen1.setStatus("mandatory")


class _Switch_sen2_Type(Integer32):
    """Custom type switch_sen2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen2_Type.__name__ = "Integer32"
_Switch_sen2_Object = MibScalar
switch_sen2 = _Switch_sen2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 2),
    _Switch_sen2_Type()
)
switch_sen2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen2.setStatus("mandatory")


class _Switch_sen3_Type(Integer32):
    """Custom type switch_sen3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen3_Type.__name__ = "Integer32"
_Switch_sen3_Object = MibScalar
switch_sen3 = _Switch_sen3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 3),
    _Switch_sen3_Type()
)
switch_sen3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen3.setStatus("mandatory")


class _Switch_sen4_Type(Integer32):
    """Custom type switch_sen4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen4_Type.__name__ = "Integer32"
_Switch_sen4_Object = MibScalar
switch_sen4 = _Switch_sen4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 4),
    _Switch_sen4_Type()
)
switch_sen4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen4.setStatus("mandatory")


class _Switch_sen5_Type(Integer32):
    """Custom type switch_sen5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen5_Type.__name__ = "Integer32"
_Switch_sen5_Object = MibScalar
switch_sen5 = _Switch_sen5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 5),
    _Switch_sen5_Type()
)
switch_sen5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen5.setStatus("mandatory")


class _Switch_sen6_Type(Integer32):
    """Custom type switch_sen6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen6_Type.__name__ = "Integer32"
_Switch_sen6_Object = MibScalar
switch_sen6 = _Switch_sen6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 6),
    _Switch_sen6_Type()
)
switch_sen6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen6.setStatus("mandatory")


class _Switch_sen7_Type(Integer32):
    """Custom type switch_sen7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen7_Type.__name__ = "Integer32"
_Switch_sen7_Object = MibScalar
switch_sen7 = _Switch_sen7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 7),
    _Switch_sen7_Type()
)
switch_sen7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen7.setStatus("mandatory")


class _Switch_sen8_Type(Integer32):
    """Custom type switch_sen8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen8_Type.__name__ = "Integer32"
_Switch_sen8_Object = MibScalar
switch_sen8 = _Switch_sen8_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 8),
    _Switch_sen8_Type()
)
switch_sen8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen8.setStatus("mandatory")


class _Switch_sen9_Type(Integer32):
    """Custom type switch_sen9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen9_Type.__name__ = "Integer32"
_Switch_sen9_Object = MibScalar
switch_sen9 = _Switch_sen9_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 9),
    _Switch_sen9_Type()
)
switch_sen9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen9.setStatus("mandatory")


class _Switch_sen10_Type(Integer32):
    """Custom type switch_sen10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen10_Type.__name__ = "Integer32"
_Switch_sen10_Object = MibScalar
switch_sen10 = _Switch_sen10_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 10),
    _Switch_sen10_Type()
)
switch_sen10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen10.setStatus("mandatory")


class _Switch_sen11_Type(Integer32):
    """Custom type switch_sen11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen11_Type.__name__ = "Integer32"
_Switch_sen11_Object = MibScalar
switch_sen11 = _Switch_sen11_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 11),
    _Switch_sen11_Type()
)
switch_sen11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen11.setStatus("mandatory")


class _Switch_sen12_Type(Integer32):
    """Custom type switch_sen12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen12_Type.__name__ = "Integer32"
_Switch_sen12_Object = MibScalar
switch_sen12 = _Switch_sen12_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 12),
    _Switch_sen12_Type()
)
switch_sen12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen12.setStatus("mandatory")


class _Switch_sen13_Type(Integer32):
    """Custom type switch_sen13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen13_Type.__name__ = "Integer32"
_Switch_sen13_Object = MibScalar
switch_sen13 = _Switch_sen13_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 13),
    _Switch_sen13_Type()
)
switch_sen13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen13.setStatus("mandatory")


class _Switch_sen14_Type(Integer32):
    """Custom type switch_sen14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen14_Type.__name__ = "Integer32"
_Switch_sen14_Object = MibScalar
switch_sen14 = _Switch_sen14_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 14),
    _Switch_sen14_Type()
)
switch_sen14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen14.setStatus("mandatory")


class _Switch_sen15_Type(Integer32):
    """Custom type switch_sen15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen15_Type.__name__ = "Integer32"
_Switch_sen15_Object = MibScalar
switch_sen15 = _Switch_sen15_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 15),
    _Switch_sen15_Type()
)
switch_sen15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen15.setStatus("mandatory")


class _Switch_sen16_Type(Integer32):
    """Custom type switch_sen16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen16_Type.__name__ = "Integer32"
_Switch_sen16_Object = MibScalar
switch_sen16 = _Switch_sen16_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 16),
    _Switch_sen16_Type()
)
switch_sen16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen16.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 2)
)
_Alarmmessage_Type = OctetString
_Alarmmessage_Object = MibScalar
alarmmessage = _Alarmmessage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 2, 1),
    _Alarmmessage_Type()
)
alarmmessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmmessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tempalarm1_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 1)
)
tempalarm1_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm1_24e.setStatus(
        ""
    )

room_alert_24e_snmp_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 2)
)
room_alert_24e_snmp_trap.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    room_alert_24e_snmp_trap.setStatus(
        ""
    )

tempalarm2_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 3)
)
tempalarm2_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm2_24e.setStatus(
        ""
    )

tempclear2_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 4)
)
tempclear2_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempclear2_24e.setStatus(
        ""
    )

tempalarm3_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 5)
)
tempalarm3_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm3_24e.setStatus(
        ""
    )

tempclear3_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 6)
)
tempclear3_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempclear3_24e.setStatus(
        ""
    )

humidityalarm1_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 7)
)
humidityalarm1_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm1_24e.setStatus(
        ""
    )

humidityclear1_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 8)
)
humidityclear1_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear1_24e.setStatus(
        ""
    )

humidityalarm2_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 9)
)
humidityalarm2_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm2_24e.setStatus(
        ""
    )

humidityclear2_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 10)
)
humidityclear2_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear2_24e.setStatus(
        ""
    )

humidityalarm3_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 11)
)
humidityalarm3_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm3_24e.setStatus(
        ""
    )

humidityclear3_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 12)
)
humidityclear3_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear3_24e.setStatus(
        ""
    )

switchalarm1_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 13)
)
switchalarm1_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm1_24e.setStatus(
        ""
    )

switchclear1_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 14)
)
switchclear1_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear1_24e.setStatus(
        ""
    )

switchalarm2_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 15)
)
switchalarm2_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm2_24e.setStatus(
        ""
    )

switchclear2_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 16)
)
switchclear2_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear2_24e.setStatus(
        ""
    )

switchalarm3_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 17)
)
switchalarm3_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm3_24e.setStatus(
        ""
    )

switchclear3_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 18)
)
switchclear3_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear3_24e.setStatus(
        ""
    )

switchalarm4_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 19)
)
switchalarm4_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm4_24e.setStatus(
        ""
    )

switchclear4_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 20)
)
switchclear4_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear4_24e.setStatus(
        ""
    )

switchalarm5_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 21)
)
switchalarm5_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm5_24e.setStatus(
        ""
    )

switchclear5_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 22)
)
switchclear5_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear5_24e.setStatus(
        ""
    )

switchalarm6_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 23)
)
switchalarm6_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm6_24e.setStatus(
        ""
    )

switchclear6_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 24)
)
switchclear6_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear6_24e.setStatus(
        ""
    )

switchalarm7_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 25)
)
switchalarm7_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm7_24e.setStatus(
        ""
    )

switchclear7_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 26)
)
switchclear7_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear7_24e.setStatus(
        ""
    )

switchalarm8_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 27)
)
switchalarm8_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm8_24e.setStatus(
        ""
    )

switchclear8_24e = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 5, 0, 28)
)
switchclear8_24e.setObjects(
    ("ROOMALERT24E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear8_24e.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROOMALERT24E-MIB",
    **{"avtech": avtech,
       "products": products,
       "roomalert24e": roomalert24e,
       "tempalarm1-24e": tempalarm1_24e,
       "room-alert-24e-snmp-trap": room_alert_24e_snmp_trap,
       "tempalarm2-24e": tempalarm2_24e,
       "tempclear2-24e": tempclear2_24e,
       "tempalarm3-24e": tempalarm3_24e,
       "tempclear3-24e": tempclear3_24e,
       "humidityalarm1-24e": humidityalarm1_24e,
       "humidityclear1-24e": humidityclear1_24e,
       "humidityalarm2-24e": humidityalarm2_24e,
       "humidityclear2-24e": humidityclear2_24e,
       "humidityalarm3-24e": humidityalarm3_24e,
       "humidityclear3-24e": humidityclear3_24e,
       "switchalarm1-24e": switchalarm1_24e,
       "switchclear1-24e": switchclear1_24e,
       "switchalarm2-24e": switchalarm2_24e,
       "switchclear2-24e": switchclear2_24e,
       "switchalarm3-24e": switchalarm3_24e,
       "switchclear3-24e": switchclear3_24e,
       "switchalarm4-24e": switchalarm4_24e,
       "switchclear4-24e": switchclear4_24e,
       "switchalarm5-24e": switchalarm5_24e,
       "switchclear5-24e": switchclear5_24e,
       "switchalarm6-24e": switchalarm6_24e,
       "switchclear6-24e": switchclear6_24e,
       "switchalarm7-24e": switchalarm7_24e,
       "switchclear7-24e": switchclear7_24e,
       "switchalarm8-24e": switchalarm8_24e,
       "switchclear8-24e": switchclear8_24e,
       "sensors": sensors,
       "internal": internal,
       "temperature": temperature,
       "internal-tempf": internal_tempf,
       "internal-tempc": internal_tempc,
       "humidity": humidity,
       "internal-humidity": internal_humidity,
       "heat-index": heat_index,
       "internal-heat-index": internal_heat_index,
       "internal-heat-indexc": internal_heat_indexc,
       "digital": digital,
       "digital-sen1": digital_sen1,
       "digital-sen1-1": digital_sen1_1,
       "digital-sen1-2": digital_sen1_2,
       "digital-sen1-3": digital_sen1_3,
       "digital-sen1-4": digital_sen1_4,
       "digital-sen1-5": digital_sen1_5,
       "digital-sen2": digital_sen2,
       "digital-sen2-1": digital_sen2_1,
       "digital-sen2-2": digital_sen2_2,
       "digital-sen2-3": digital_sen2_3,
       "digital-sen2-4": digital_sen2_4,
       "digital-sen2-5": digital_sen2_5,
       "digital-sen3": digital_sen3,
       "digital-sen3-1": digital_sen3_1,
       "digital-sen3-2": digital_sen3_2,
       "digital-sen3-3": digital_sen3_3,
       "digital-sen3-4": digital_sen3_4,
       "digital-sen3-5": digital_sen3_5,
       "digital-sen4": digital_sen4,
       "digital-sen4-1": digital_sen4_1,
       "digital-sen4-2": digital_sen4_2,
       "digital-sen4-3": digital_sen4_3,
       "digital-sen4-4": digital_sen4_4,
       "digital-sen4-5": digital_sen4_5,
       "digital-sen5": digital_sen5,
       "digital-sen5-1": digital_sen5_1,
       "digital-sen5-2": digital_sen5_2,
       "digital-sen5-3": digital_sen5_3,
       "digital-sen5-4": digital_sen5_4,
       "digital-sen5-5": digital_sen5_5,
       "digital-sen6": digital_sen6,
       "digital-sen6-1": digital_sen6_1,
       "digital-sen6-2": digital_sen6_2,
       "digital-sen6-3": digital_sen6_3,
       "digital-sen6-4": digital_sen6_4,
       "digital-sen6-5": digital_sen6_5,
       "switch": switch,
       "switch-sen1": switch_sen1,
       "switch-sen2": switch_sen2,
       "switch-sen3": switch_sen3,
       "switch-sen4": switch_sen4,
       "switch-sen5": switch_sen5,
       "switch-sen6": switch_sen6,
       "switch-sen7": switch_sen7,
       "switch-sen8": switch_sen8,
       "switch-sen9": switch_sen9,
       "switch-sen10": switch_sen10,
       "switch-sen11": switch_sen11,
       "switch-sen12": switch_sen12,
       "switch-sen13": switch_sen13,
       "switch-sen14": switch_sen14,
       "switch-sen15": switch_sen15,
       "switch-sen16": switch_sen16,
       "traps": traps,
       "alarmmessage": alarmmessage}
)
