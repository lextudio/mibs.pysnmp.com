# SNMP MIB module (EATON-GENESIS-II-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EATON-GENESIS-II-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:22 2024
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

_Eaton_ObjectIdentity = ObjectIdentity
eaton = _Eaton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17373)
)
_Genesis2_ObjectIdentity = ObjectIdentity
genesis2 = _Genesis2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17373, 3)
)
_ProductInfo_ObjectIdentity = ObjectIdentity
productInfo = _ProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17373, 3, 1)
)
_ProductTitle_Type = DisplayString
_ProductTitle_Object = MibScalar
productTitle = _ProductTitle_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 1, 1),
    _ProductTitle_Type()
)
productTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productTitle.setStatus("mandatory")
_ProductVersion_Type = DisplayString
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 1, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("mandatory")
_ProductName_Type = DisplayString
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 1, 3),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("mandatory")
_ProductMAC_Type = DisplayString
_ProductMAC_Object = MibScalar
productMAC = _ProductMAC_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 1, 4),
    _ProductMAC_Type()
)
productMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productMAC.setStatus("mandatory")
_ProductIP_Type = DisplayString
_ProductIP_Object = MibScalar
productIP = _ProductIP_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 1, 5),
    _ProductIP_Type()
)
productIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productIP.setStatus("mandatory")
_SensorData_ObjectIdentity = ObjectIdentity
sensorData = _SensorData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2)
)


class _IntDeciAmpsCT1_Type(Integer32):
    """Custom type intDeciAmpsCT1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT1_Type.__name__ = "Integer32"
_IntDeciAmpsCT1_Object = MibScalar
intDeciAmpsCT1 = _IntDeciAmpsCT1_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 1),
    _IntDeciAmpsCT1_Type()
)
intDeciAmpsCT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT1.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT1.setUnits("0.1 Amps")


class _IntDeciAmpsCT2_Type(Integer32):
    """Custom type intDeciAmpsCT2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT2_Type.__name__ = "Integer32"
_IntDeciAmpsCT2_Object = MibScalar
intDeciAmpsCT2 = _IntDeciAmpsCT2_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 2),
    _IntDeciAmpsCT2_Type()
)
intDeciAmpsCT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT2.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT2.setUnits("0.1 Amps")


class _IntDeciAmpsCT3_Type(Integer32):
    """Custom type intDeciAmpsCT3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT3_Type.__name__ = "Integer32"
_IntDeciAmpsCT3_Object = MibScalar
intDeciAmpsCT3 = _IntDeciAmpsCT3_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 3),
    _IntDeciAmpsCT3_Type()
)
intDeciAmpsCT3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT3.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT3.setUnits("0.1 Amps")


class _IntDeciAmpsCT4_Type(Integer32):
    """Custom type intDeciAmpsCT4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT4_Type.__name__ = "Integer32"
_IntDeciAmpsCT4_Object = MibScalar
intDeciAmpsCT4 = _IntDeciAmpsCT4_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 4),
    _IntDeciAmpsCT4_Type()
)
intDeciAmpsCT4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT4.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT4.setUnits("0.1 Amps")


class _IntDeciAmpsCT5_Type(Integer32):
    """Custom type intDeciAmpsCT5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT5_Type.__name__ = "Integer32"
_IntDeciAmpsCT5_Object = MibScalar
intDeciAmpsCT5 = _IntDeciAmpsCT5_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 5),
    _IntDeciAmpsCT5_Type()
)
intDeciAmpsCT5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT5.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT5.setUnits("0.1 Amps")


class _IntDeciAmpsCT6_Type(Integer32):
    """Custom type intDeciAmpsCT6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT6_Type.__name__ = "Integer32"
_IntDeciAmpsCT6_Object = MibScalar
intDeciAmpsCT6 = _IntDeciAmpsCT6_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 6),
    _IntDeciAmpsCT6_Type()
)
intDeciAmpsCT6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT6.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT6.setUnits("0.1 Amps")


class _IntDeciAmpsCT7_Type(Integer32):
    """Custom type intDeciAmpsCT7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT7_Type.__name__ = "Integer32"
_IntDeciAmpsCT7_Object = MibScalar
intDeciAmpsCT7 = _IntDeciAmpsCT7_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 7),
    _IntDeciAmpsCT7_Type()
)
intDeciAmpsCT7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT7.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT7.setUnits("0.1 Amps")


class _IntDeciAmpsCT8_Type(Integer32):
    """Custom type intDeciAmpsCT8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 300),
    )


_IntDeciAmpsCT8_Type.__name__ = "Integer32"
_IntDeciAmpsCT8_Object = MibScalar
intDeciAmpsCT8 = _IntDeciAmpsCT8_Object(
    (1, 3, 6, 1, 4, 1, 17373, 3, 2, 8),
    _IntDeciAmpsCT8_Type()
)
intDeciAmpsCT8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intDeciAmpsCT8.setStatus("mandatory")
if mibBuilder.loadTexts:
    intDeciAmpsCT8.setUnits("0.1 Amps")

# Managed Objects groups


# Notification objects

intDeciAmpsCT1TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 1)
)
intDeciAmpsCT1TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT1")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT1TRAP.setStatus(
        ""
    )

intDeciAmpsCT2TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 2)
)
intDeciAmpsCT2TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT2")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT2TRAP.setStatus(
        ""
    )

intDeciAmpsCT3TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 3)
)
intDeciAmpsCT3TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT3")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT3TRAP.setStatus(
        ""
    )

intDeciAmpsCT4TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 4)
)
intDeciAmpsCT4TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT4")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT4TRAP.setStatus(
        ""
    )

intDeciAmpsCT5TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 5)
)
intDeciAmpsCT5TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT5")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT5TRAP.setStatus(
        ""
    )

intDeciAmpsCT6TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 6)
)
intDeciAmpsCT6TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT6")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT6TRAP.setStatus(
        ""
    )

intDeciAmpsCT7TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 7)
)
intDeciAmpsCT7TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT7")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT7TRAP.setStatus(
        ""
    )

intDeciAmpsCT8TRAP = NotificationType(
    (1, 3, 6, 1, 4, 1, 17373, 0, 8)
)
intDeciAmpsCT8TRAP.setObjects(
    ("EATON-GENESIS-II-MIB", "intDeciAmpsCT8")
)
if mibBuilder.loadTexts:
    intDeciAmpsCT8TRAP.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EATON-GENESIS-II-MIB",
    **{"eaton": eaton,
       "intDeciAmpsCT1TRAP": intDeciAmpsCT1TRAP,
       "intDeciAmpsCT2TRAP": intDeciAmpsCT2TRAP,
       "intDeciAmpsCT3TRAP": intDeciAmpsCT3TRAP,
       "intDeciAmpsCT4TRAP": intDeciAmpsCT4TRAP,
       "intDeciAmpsCT5TRAP": intDeciAmpsCT5TRAP,
       "intDeciAmpsCT6TRAP": intDeciAmpsCT6TRAP,
       "intDeciAmpsCT7TRAP": intDeciAmpsCT7TRAP,
       "intDeciAmpsCT8TRAP": intDeciAmpsCT8TRAP,
       "genesis2": genesis2,
       "productInfo": productInfo,
       "productTitle": productTitle,
       "productVersion": productVersion,
       "productName": productName,
       "productMAC": productMAC,
       "productIP": productIP,
       "sensorData": sensorData,
       "intDeciAmpsCT1": intDeciAmpsCT1,
       "intDeciAmpsCT2": intDeciAmpsCT2,
       "intDeciAmpsCT3": intDeciAmpsCT3,
       "intDeciAmpsCT4": intDeciAmpsCT4,
       "intDeciAmpsCT5": intDeciAmpsCT5,
       "intDeciAmpsCT6": intDeciAmpsCT6,
       "intDeciAmpsCT7": intDeciAmpsCT7,
       "intDeciAmpsCT8": intDeciAmpsCT8}
)
