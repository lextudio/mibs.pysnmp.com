# SNMP MIB module (TEMPAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TEMPAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:08 2024
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
_Tempager_ObjectIdentity = ObjectIdentity
tempager = _Tempager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1)
)


class _Tempreading1c_Type(Integer32):
    """Custom type tempreading1c based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading1c_Type.__name__ = "Integer32"
_Tempreading1c_Object = MibScalar
tempreading1c = _Tempreading1c_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 1),
    _Tempreading1c_Type()
)
tempreading1c.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading1c.setStatus("mandatory")


class _Tempreading2c_Type(Integer32):
    """Custom type tempreading2c based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading2c_Type.__name__ = "Integer32"
_Tempreading2c_Object = MibScalar
tempreading2c = _Tempreading2c_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 2),
    _Tempreading2c_Type()
)
tempreading2c.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading2c.setStatus("mandatory")


class _Tempreading3c_Type(Integer32):
    """Custom type tempreading3c based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading3c_Type.__name__ = "Integer32"
_Tempreading3c_Object = MibScalar
tempreading3c = _Tempreading3c_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 3),
    _Tempreading3c_Type()
)
tempreading3c.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading3c.setStatus("mandatory")


class _Tempreading4c_Type(Integer32):
    """Custom type tempreading4c based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading4c_Type.__name__ = "Integer32"
_Tempreading4c_Object = MibScalar
tempreading4c = _Tempreading4c_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 4),
    _Tempreading4c_Type()
)
tempreading4c.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading4c.setStatus("mandatory")


class _Tempreading1f_Type(Integer32):
    """Custom type tempreading1f based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading1f_Type.__name__ = "Integer32"
_Tempreading1f_Object = MibScalar
tempreading1f = _Tempreading1f_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 5),
    _Tempreading1f_Type()
)
tempreading1f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading1f.setStatus("mandatory")


class _Tempreading2f_Type(Integer32):
    """Custom type tempreading2f based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading2f_Type.__name__ = "Integer32"
_Tempreading2f_Object = MibScalar
tempreading2f = _Tempreading2f_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 6),
    _Tempreading2f_Type()
)
tempreading2f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading2f.setStatus("mandatory")


class _Tempreading3f_Type(Integer32):
    """Custom type tempreading3f based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading3f_Type.__name__ = "Integer32"
_Tempreading3f_Object = MibScalar
tempreading3f = _Tempreading3f_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 7),
    _Tempreading3f_Type()
)
tempreading3f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading3f.setStatus("mandatory")


class _Tempreading4f_Type(Integer32):
    """Custom type tempreading4f based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tempreading4f_Type.__name__ = "Integer32"
_Tempreading4f_Object = MibScalar
tempreading4f = _Tempreading4f_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 1, 1, 8),
    _Tempreading4f_Type()
)
tempreading4f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempreading4f.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 2)
)


class _Alarmtemp1_Type(Integer32):
    """Custom type alarmtemp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Alarmtemp1_Type.__name__ = "Integer32"
_Alarmtemp1_Object = MibScalar
alarmtemp1 = _Alarmtemp1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 1),
    _Alarmtemp1_Type()
)
alarmtemp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmtemp1.setStatus("mandatory")


class _Alarmtemp2_Type(Integer32):
    """Custom type alarmtemp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Alarmtemp2_Type.__name__ = "Integer32"
_Alarmtemp2_Object = MibScalar
alarmtemp2 = _Alarmtemp2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 2),
    _Alarmtemp2_Type()
)
alarmtemp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmtemp2.setStatus("mandatory")


class _Alarmtemp3_Type(Integer32):
    """Custom type alarmtemp3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Alarmtemp3_Type.__name__ = "Integer32"
_Alarmtemp3_Object = MibScalar
alarmtemp3 = _Alarmtemp3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 3),
    _Alarmtemp3_Type()
)
alarmtemp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmtemp3.setStatus("mandatory")


class _Alarmtemp4_Type(Integer32):
    """Custom type alarmtemp4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Alarmtemp4_Type.__name__ = "Integer32"
_Alarmtemp4_Object = MibScalar
alarmtemp4 = _Alarmtemp4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 4),
    _Alarmtemp4_Type()
)
alarmtemp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmtemp4.setStatus("mandatory")
_Alarmmessage_Type = OctetString
_Alarmmessage_Object = MibScalar
alarmmessage = _Alarmmessage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 2, 5),
    _Alarmmessage_Type()
)
alarmmessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmmessage.setStatus("mandatory")
_Thresholds_ObjectIdentity = ObjectIdentity
thresholds = _Thresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3)
)


class _Upperlimit1_Type(Integer32):
    """Custom type upperlimit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Upperlimit1_Type.__name__ = "Integer32"
_Upperlimit1_Object = MibScalar
upperlimit1 = _Upperlimit1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 1),
    _Upperlimit1_Type()
)
upperlimit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upperlimit1.setStatus("mandatory")


class _Lowerlimit1_Type(Integer32):
    """Custom type lowerlimit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Lowerlimit1_Type.__name__ = "Integer32"
_Lowerlimit1_Object = MibScalar
lowerlimit1 = _Lowerlimit1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 2),
    _Lowerlimit1_Type()
)
lowerlimit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowerlimit1.setStatus("mandatory")


class _Upperlimit2_Type(Integer32):
    """Custom type upperlimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Upperlimit2_Type.__name__ = "Integer32"
_Upperlimit2_Object = MibScalar
upperlimit2 = _Upperlimit2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 3),
    _Upperlimit2_Type()
)
upperlimit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upperlimit2.setStatus("mandatory")


class _Lowerlimit2_Type(Integer32):
    """Custom type lowerlimit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Lowerlimit2_Type.__name__ = "Integer32"
_Lowerlimit2_Object = MibScalar
lowerlimit2 = _Lowerlimit2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 4),
    _Lowerlimit2_Type()
)
lowerlimit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowerlimit2.setStatus("mandatory")


class _Upperlimit3_Type(Integer32):
    """Custom type upperlimit3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Upperlimit3_Type.__name__ = "Integer32"
_Upperlimit3_Object = MibScalar
upperlimit3 = _Upperlimit3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 5),
    _Upperlimit3_Type()
)
upperlimit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upperlimit3.setStatus("mandatory")


class _Lowerlimit3_Type(Integer32):
    """Custom type lowerlimit3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Lowerlimit3_Type.__name__ = "Integer32"
_Lowerlimit3_Object = MibScalar
lowerlimit3 = _Lowerlimit3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 6),
    _Lowerlimit3_Type()
)
lowerlimit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowerlimit3.setStatus("mandatory")


class _Upperlimit4_Type(Integer32):
    """Custom type upperlimit4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Upperlimit4_Type.__name__ = "Integer32"
_Upperlimit4_Object = MibScalar
upperlimit4 = _Upperlimit4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 7),
    _Upperlimit4_Type()
)
upperlimit4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upperlimit4.setStatus("mandatory")


class _Lowerlimit4_Type(Integer32):
    """Custom type lowerlimit4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_Lowerlimit4_Type.__name__ = "Integer32"
_Lowerlimit4_Object = MibScalar
lowerlimit4 = _Lowerlimit4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 3, 8),
    _Lowerlimit4_Type()
)
lowerlimit4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowerlimit4.setStatus("mandatory")

# Managed Objects groups


# Notification objects

alarmstart1_t4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 1)
)
alarmstart1_t4.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading1c"),
        ("TEMPAGER-MIB", "tempreading1f"))
)
if mibBuilder.loadTexts:
    alarmstart1_t4.setStatus(
        ""
    )

tempager_snmp_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 2)
)
tempager_snmp_trap.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading1c"),
        ("TEMPAGER-MIB", "tempreading1f"),
        ("TEMPAGER-MIB", "tempreading2c"),
        ("TEMPAGER-MIB", "tempreading2f"),
        ("TEMPAGER-MIB", "tempreading3c"),
        ("TEMPAGER-MIB", "tempreading3f"),
        ("TEMPAGER-MIB", "tempreading4c"),
        ("TEMPAGER-MIB", "tempreading4f"))
)
if mibBuilder.loadTexts:
    tempager_snmp_trap.setStatus(
        ""
    )

alarmstart2_t4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 3)
)
alarmstart2_t4.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading2c"),
        ("TEMPAGER-MIB", "tempreading2f"))
)
if mibBuilder.loadTexts:
    alarmstart2_t4.setStatus(
        ""
    )

alarmclear2_t4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 4)
)
alarmclear2_t4.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading2c"),
        ("TEMPAGER-MIB", "tempreading2f"))
)
if mibBuilder.loadTexts:
    alarmclear2_t4.setStatus(
        ""
    )

alarmstart3_t4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 5)
)
alarmstart3_t4.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading3c"),
        ("TEMPAGER-MIB", "tempreading3f"))
)
if mibBuilder.loadTexts:
    alarmstart3_t4.setStatus(
        ""
    )

alarmclear3_t4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 6)
)
alarmclear3_t4.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading3c"),
        ("TEMPAGER-MIB", "tempreading3f"))
)
if mibBuilder.loadTexts:
    alarmclear3_t4.setStatus(
        ""
    )

alarmstart4_t4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 7)
)
alarmstart4_t4.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading4c"),
        ("TEMPAGER-MIB", "tempreading4f"))
)
if mibBuilder.loadTexts:
    alarmstart4_t4.setStatus(
        ""
    )

alarmclear4_t4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 1, 0, 8)
)
alarmclear4_t4.setObjects(
      *(("TEMPAGER-MIB", "alarmmessage"),
        ("TEMPAGER-MIB", "tempreading4c"),
        ("TEMPAGER-MIB", "tempreading4f"))
)
if mibBuilder.loadTexts:
    alarmclear4_t4.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TEMPAGER-MIB",
    **{"avtech": avtech,
       "products": products,
       "tempager": tempager,
       "alarmstart1-t4": alarmstart1_t4,
       "tempager-snmp-trap": tempager_snmp_trap,
       "alarmstart2-t4": alarmstart2_t4,
       "alarmclear2-t4": alarmclear2_t4,
       "alarmstart3-t4": alarmstart3_t4,
       "alarmclear3-t4": alarmclear3_t4,
       "alarmstart4-t4": alarmstart4_t4,
       "alarmclear4-t4": alarmclear4_t4,
       "sensors": sensors,
       "temperature": temperature,
       "tempreading1c": tempreading1c,
       "tempreading2c": tempreading2c,
       "tempreading3c": tempreading3c,
       "tempreading4c": tempreading4c,
       "tempreading1f": tempreading1f,
       "tempreading2f": tempreading2f,
       "tempreading3f": tempreading3f,
       "tempreading4f": tempreading4f,
       "traps": traps,
       "alarmtemp1": alarmtemp1,
       "alarmtemp2": alarmtemp2,
       "alarmtemp3": alarmtemp3,
       "alarmtemp4": alarmtemp4,
       "alarmmessage": alarmmessage,
       "thresholds": thresholds,
       "upperlimit1": upperlimit1,
       "lowerlimit1": lowerlimit1,
       "upperlimit2": upperlimit2,
       "lowerlimit2": lowerlimit2,
       "upperlimit3": upperlimit3,
       "lowerlimit3": lowerlimit3,
       "upperlimit4": upperlimit4,
       "lowerlimit4": lowerlimit4}
)
