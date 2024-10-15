# SNMP MIB module (GUARDIAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/GUARDIAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:17 2024
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

_Westek_ObjectIdentity = ObjectIdentity
westek = _Westek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166)
)
_Guardian_ObjectIdentity = ObjectIdentity
guardian = _Guardian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1)
)
_GuardianRev_Type = DisplayString
_GuardianRev_Object = MibScalar
guardianRev = _GuardianRev_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 1),
    _GuardianRev_Type()
)
guardianRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    guardianRev.setStatus("mandatory")
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2)
)
_DevInput_ObjectIdentity = ObjectIdentity
devInput = _DevInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1)
)
_DevInput1_ObjectIdentity = ObjectIdentity
devInput1 = _DevInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1)
)


class _DevInp1Val_Type(Integer32):
    """Custom type devInp1Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp1Val_Type.__name__ = "Integer32"
_DevInp1Val_Object = MibScalar
devInp1Val = _DevInp1Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1, 1),
    _DevInp1Val_Type()
)
devInp1Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp1Val.setStatus("mandatory")


class _DevInp1Pol_Type(Integer32):
    """Custom type devInp1Pol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp1Pol_Type.__name__ = "Integer32"
_DevInp1Pol_Object = MibScalar
devInp1Pol = _DevInp1Pol_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 1, 2),
    _DevInp1Pol_Type()
)
devInp1Pol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp1Pol.setStatus("mandatory")
_DevInput2_ObjectIdentity = ObjectIdentity
devInput2 = _DevInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2)
)


class _DevInp2Val_Type(Integer32):
    """Custom type devInp2Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp2Val_Type.__name__ = "Integer32"
_DevInp2Val_Object = MibScalar
devInp2Val = _DevInp2Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2, 1),
    _DevInp2Val_Type()
)
devInp2Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp2Val.setStatus("mandatory")


class _DevInp2Pol_Type(Integer32):
    """Custom type devInp2Pol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp2Pol_Type.__name__ = "Integer32"
_DevInp2Pol_Object = MibScalar
devInp2Pol = _DevInp2Pol_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 2, 2),
    _DevInp2Pol_Type()
)
devInp2Pol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp2Pol.setStatus("mandatory")
_DevInput3_ObjectIdentity = ObjectIdentity
devInput3 = _DevInput3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3)
)


class _DevInp3Val_Type(Integer32):
    """Custom type devInp3Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp3Val_Type.__name__ = "Integer32"
_DevInp3Val_Object = MibScalar
devInp3Val = _DevInp3Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3, 1),
    _DevInp3Val_Type()
)
devInp3Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp3Val.setStatus("mandatory")


class _DevInp3Pol_Type(Integer32):
    """Custom type devInp3Pol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp3Pol_Type.__name__ = "Integer32"
_DevInp3Pol_Object = MibScalar
devInp3Pol = _DevInp3Pol_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 3, 2),
    _DevInp3Pol_Type()
)
devInp3Pol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp3Pol.setStatus("mandatory")
_DevInput4_ObjectIdentity = ObjectIdentity
devInput4 = _DevInput4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4)
)


class _DevInp4Val_Type(Integer32):
    """Custom type devInp4Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp4Val_Type.__name__ = "Integer32"
_DevInp4Val_Object = MibScalar
devInp4Val = _DevInp4Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4, 1),
    _DevInp4Val_Type()
)
devInp4Val.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp4Val.setStatus("mandatory")


class _DevInp4Pol_Type(Integer32):
    """Custom type devInp4Pol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DevInp4Pol_Type.__name__ = "Integer32"
_DevInp4Pol_Object = MibScalar
devInp4Pol = _DevInp4Pol_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 4, 2),
    _DevInp4Pol_Type()
)
devInp4Pol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInp4Pol.setStatus("mandatory")


class _DevInpStat_Type(Integer32):
    """Custom type devInpStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevInpStat_Type.__name__ = "Integer32"
_DevInpStat_Object = MibScalar
devInpStat = _DevInpStat_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 1, 10),
    _DevInpStat_Type()
)
devInpStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devInpStat.setStatus("mandatory")
_DevFan_ObjectIdentity = ObjectIdentity
devFan = _DevFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2)
)
_DevFan1_ObjectIdentity = ObjectIdentity
devFan1 = _DevFan1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1)
)


class _DevFan1Val_Type(Integer32):
    """Custom type devFan1Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan1Val_Type.__name__ = "Integer32"
_DevFan1Val_Object = MibScalar
devFan1Val = _DevFan1Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 1),
    _DevFan1Val_Type()
)
devFan1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFan1Val.setStatus("mandatory")


class _DevFan1Min_Type(Integer32):
    """Custom type devFan1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan1Min_Type.__name__ = "Integer32"
_DevFan1Min_Object = MibScalar
devFan1Min = _DevFan1Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 2),
    _DevFan1Min_Type()
)
devFan1Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan1Min.setStatus("mandatory")


class _DevFan1Max_Type(Integer32):
    """Custom type devFan1Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan1Max_Type.__name__ = "Integer32"
_DevFan1Max_Object = MibScalar
devFan1Max = _DevFan1Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 1, 3),
    _DevFan1Max_Type()
)
devFan1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan1Max.setStatus("mandatory")
_DevFan2_ObjectIdentity = ObjectIdentity
devFan2 = _DevFan2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2)
)


class _DevFan2Val_Type(Integer32):
    """Custom type devFan2Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan2Val_Type.__name__ = "Integer32"
_DevFan2Val_Object = MibScalar
devFan2Val = _DevFan2Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 1),
    _DevFan2Val_Type()
)
devFan2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFan2Val.setStatus("mandatory")


class _DevFan2Min_Type(Integer32):
    """Custom type devFan2Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan2Min_Type.__name__ = "Integer32"
_DevFan2Min_Object = MibScalar
devFan2Min = _DevFan2Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 2),
    _DevFan2Min_Type()
)
devFan2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan2Min.setStatus("mandatory")


class _DevFan2Max_Type(Integer32):
    """Custom type devFan2Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan2Max_Type.__name__ = "Integer32"
_DevFan2Max_Object = MibScalar
devFan2Max = _DevFan2Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 2, 3),
    _DevFan2Max_Type()
)
devFan2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan2Max.setStatus("mandatory")
_DevFan3_ObjectIdentity = ObjectIdentity
devFan3 = _DevFan3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3)
)


class _DevFan3Val_Type(Integer32):
    """Custom type devFan3Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan3Val_Type.__name__ = "Integer32"
_DevFan3Val_Object = MibScalar
devFan3Val = _DevFan3Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 1),
    _DevFan3Val_Type()
)
devFan3Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFan3Val.setStatus("mandatory")


class _DevFan3Min_Type(Integer32):
    """Custom type devFan3Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan3Min_Type.__name__ = "Integer32"
_DevFan3Min_Object = MibScalar
devFan3Min = _DevFan3Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 2),
    _DevFan3Min_Type()
)
devFan3Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan3Min.setStatus("mandatory")


class _DevFan3Max_Type(Integer32):
    """Custom type devFan3Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan3Max_Type.__name__ = "Integer32"
_DevFan3Max_Object = MibScalar
devFan3Max = _DevFan3Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 3, 3),
    _DevFan3Max_Type()
)
devFan3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan3Max.setStatus("mandatory")
_DevFan4_ObjectIdentity = ObjectIdentity
devFan4 = _DevFan4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4)
)


class _DevFan4Val_Type(Integer32):
    """Custom type devFan4Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan4Val_Type.__name__ = "Integer32"
_DevFan4Val_Object = MibScalar
devFan4Val = _DevFan4Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 1),
    _DevFan4Val_Type()
)
devFan4Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFan4Val.setStatus("mandatory")


class _DevFan4Min_Type(Integer32):
    """Custom type devFan4Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan4Min_Type.__name__ = "Integer32"
_DevFan4Min_Object = MibScalar
devFan4Min = _DevFan4Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 2),
    _DevFan4Min_Type()
)
devFan4Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan4Min.setStatus("mandatory")


class _DevFan4Max_Type(Integer32):
    """Custom type devFan4Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )


_DevFan4Max_Type.__name__ = "Integer32"
_DevFan4Max_Object = MibScalar
devFan4Max = _DevFan4Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 4, 3),
    _DevFan4Max_Type()
)
devFan4Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFan4Max.setStatus("mandatory")


class _DevFanStat_Type(Integer32):
    """Custom type devFanStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevFanStat_Type.__name__ = "Integer32"
_DevFanStat_Object = MibScalar
devFanStat = _DevFanStat_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 2, 10),
    _DevFanStat_Type()
)
devFanStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devFanStat.setStatus("mandatory")
_DevTemp_ObjectIdentity = ObjectIdentity
devTemp = _DevTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3)
)
_DevTemp1_ObjectIdentity = ObjectIdentity
devTemp1 = _DevTemp1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1)
)


class _DevTemp1Val_Type(Integer32):
    """Custom type devTemp1Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp1Val_Type.__name__ = "Integer32"
_DevTemp1Val_Object = MibScalar
devTemp1Val = _DevTemp1Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 1),
    _DevTemp1Val_Type()
)
devTemp1Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp1Val.setStatus("mandatory")


class _DevTemp1Min_Type(Integer32):
    """Custom type devTemp1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp1Min_Type.__name__ = "Integer32"
_DevTemp1Min_Object = MibScalar
devTemp1Min = _DevTemp1Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 2),
    _DevTemp1Min_Type()
)
devTemp1Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp1Min.setStatus("mandatory")


class _DevTemp1Max_Type(Integer32):
    """Custom type devTemp1Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp1Max_Type.__name__ = "Integer32"
_DevTemp1Max_Object = MibScalar
devTemp1Max = _DevTemp1Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 1, 3),
    _DevTemp1Max_Type()
)
devTemp1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp1Max.setStatus("mandatory")
_DevTemp2_ObjectIdentity = ObjectIdentity
devTemp2 = _DevTemp2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2)
)


class _DevTemp2Val_Type(Integer32):
    """Custom type devTemp2Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp2Val_Type.__name__ = "Integer32"
_DevTemp2Val_Object = MibScalar
devTemp2Val = _DevTemp2Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 1),
    _DevTemp2Val_Type()
)
devTemp2Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp2Val.setStatus("mandatory")


class _DevTemp2Min_Type(Integer32):
    """Custom type devTemp2Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp2Min_Type.__name__ = "Integer32"
_DevTemp2Min_Object = MibScalar
devTemp2Min = _DevTemp2Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 2),
    _DevTemp2Min_Type()
)
devTemp2Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp2Min.setStatus("mandatory")


class _DevTemp2Max_Type(Integer32):
    """Custom type devTemp2Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp2Max_Type.__name__ = "Integer32"
_DevTemp2Max_Object = MibScalar
devTemp2Max = _DevTemp2Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 2, 3),
    _DevTemp2Max_Type()
)
devTemp2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp2Max.setStatus("mandatory")
_DevTemp3_ObjectIdentity = ObjectIdentity
devTemp3 = _DevTemp3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3)
)


class _DevTemp3Val_Type(Integer32):
    """Custom type devTemp3Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp3Val_Type.__name__ = "Integer32"
_DevTemp3Val_Object = MibScalar
devTemp3Val = _DevTemp3Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 1),
    _DevTemp3Val_Type()
)
devTemp3Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp3Val.setStatus("mandatory")


class _DevTemp3Min_Type(Integer32):
    """Custom type devTemp3Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp3Min_Type.__name__ = "Integer32"
_DevTemp3Min_Object = MibScalar
devTemp3Min = _DevTemp3Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 2),
    _DevTemp3Min_Type()
)
devTemp3Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp3Min.setStatus("mandatory")


class _DevTemp3Max_Type(Integer32):
    """Custom type devTemp3Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp3Max_Type.__name__ = "Integer32"
_DevTemp3Max_Object = MibScalar
devTemp3Max = _DevTemp3Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 3, 3),
    _DevTemp3Max_Type()
)
devTemp3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp3Max.setStatus("mandatory")
_DevTemp4_ObjectIdentity = ObjectIdentity
devTemp4 = _DevTemp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4)
)


class _DevTemp4Val_Type(Integer32):
    """Custom type devTemp4Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp4Val_Type.__name__ = "Integer32"
_DevTemp4Val_Object = MibScalar
devTemp4Val = _DevTemp4Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 1),
    _DevTemp4Val_Type()
)
devTemp4Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp4Val.setStatus("mandatory")


class _DevTemp4Min_Type(Integer32):
    """Custom type devTemp4Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp4Min_Type.__name__ = "Integer32"
_DevTemp4Min_Object = MibScalar
devTemp4Min = _DevTemp4Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 2),
    _DevTemp4Min_Type()
)
devTemp4Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp4Min.setStatus("mandatory")


class _DevTemp4Max_Type(Integer32):
    """Custom type devTemp4Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp4Max_Type.__name__ = "Integer32"
_DevTemp4Max_Object = MibScalar
devTemp4Max = _DevTemp4Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 4, 3),
    _DevTemp4Max_Type()
)
devTemp4Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp4Max.setStatus("mandatory")
_DevTemp5_ObjectIdentity = ObjectIdentity
devTemp5 = _DevTemp5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5)
)


class _DevTemp5Val_Type(Integer32):
    """Custom type devTemp5Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp5Val_Type.__name__ = "Integer32"
_DevTemp5Val_Object = MibScalar
devTemp5Val = _DevTemp5Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 1),
    _DevTemp5Val_Type()
)
devTemp5Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp5Val.setStatus("mandatory")


class _DevTemp5Min_Type(Integer32):
    """Custom type devTemp5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp5Min_Type.__name__ = "Integer32"
_DevTemp5Min_Object = MibScalar
devTemp5Min = _DevTemp5Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 2),
    _DevTemp5Min_Type()
)
devTemp5Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp5Min.setStatus("mandatory")


class _DevTemp5Max_Type(Integer32):
    """Custom type devTemp5Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp5Max_Type.__name__ = "Integer32"
_DevTemp5Max_Object = MibScalar
devTemp5Max = _DevTemp5Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 5, 3),
    _DevTemp5Max_Type()
)
devTemp5Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp5Max.setStatus("mandatory")
_DevTemp6_ObjectIdentity = ObjectIdentity
devTemp6 = _DevTemp6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6)
)


class _DevTemp6Val_Type(Integer32):
    """Custom type devTemp6Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp6Val_Type.__name__ = "Integer32"
_DevTemp6Val_Object = MibScalar
devTemp6Val = _DevTemp6Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 1),
    _DevTemp6Val_Type()
)
devTemp6Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp6Val.setStatus("mandatory")


class _DevTemp6Min_Type(Integer32):
    """Custom type devTemp6Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp6Min_Type.__name__ = "Integer32"
_DevTemp6Min_Object = MibScalar
devTemp6Min = _DevTemp6Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 2),
    _DevTemp6Min_Type()
)
devTemp6Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp6Min.setStatus("mandatory")


class _DevTemp6Max_Type(Integer32):
    """Custom type devTemp6Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp6Max_Type.__name__ = "Integer32"
_DevTemp6Max_Object = MibScalar
devTemp6Max = _DevTemp6Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 6, 3),
    _DevTemp6Max_Type()
)
devTemp6Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp6Max.setStatus("mandatory")
_DevTemp7_ObjectIdentity = ObjectIdentity
devTemp7 = _DevTemp7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7)
)


class _DevTemp7Val_Type(Integer32):
    """Custom type devTemp7Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp7Val_Type.__name__ = "Integer32"
_DevTemp7Val_Object = MibScalar
devTemp7Val = _DevTemp7Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 1),
    _DevTemp7Val_Type()
)
devTemp7Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp7Val.setStatus("mandatory")


class _DevTemp7Min_Type(Integer32):
    """Custom type devTemp7Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp7Min_Type.__name__ = "Integer32"
_DevTemp7Min_Object = MibScalar
devTemp7Min = _DevTemp7Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 2),
    _DevTemp7Min_Type()
)
devTemp7Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp7Min.setStatus("mandatory")


class _DevTemp7Max_Type(Integer32):
    """Custom type devTemp7Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp7Max_Type.__name__ = "Integer32"
_DevTemp7Max_Object = MibScalar
devTemp7Max = _DevTemp7Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 7, 3),
    _DevTemp7Max_Type()
)
devTemp7Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp7Max.setStatus("mandatory")
_DevTemp8_ObjectIdentity = ObjectIdentity
devTemp8 = _DevTemp8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8)
)


class _DevTemp8Val_Type(Integer32):
    """Custom type devTemp8Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp8Val_Type.__name__ = "Integer32"
_DevTemp8Val_Object = MibScalar
devTemp8Val = _DevTemp8Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 1),
    _DevTemp8Val_Type()
)
devTemp8Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devTemp8Val.setStatus("mandatory")


class _DevTemp8Min_Type(Integer32):
    """Custom type devTemp8Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp8Min_Type.__name__ = "Integer32"
_DevTemp8Min_Object = MibScalar
devTemp8Min = _DevTemp8Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 2),
    _DevTemp8Min_Type()
)
devTemp8Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp8Min.setStatus("mandatory")


class _DevTemp8Max_Type(Integer32):
    """Custom type devTemp8Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 100),
    )


_DevTemp8Max_Type.__name__ = "Integer32"
_DevTemp8Max_Object = MibScalar
devTemp8Max = _DevTemp8Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 8, 3),
    _DevTemp8Max_Type()
)
devTemp8Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTemp8Max.setStatus("mandatory")


class _DevTempStat_Type(Integer32):
    """Custom type devTempStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevTempStat_Type.__name__ = "Integer32"
_DevTempStat_Object = MibScalar
devTempStat = _DevTempStat_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 3, 10),
    _DevTempStat_Type()
)
devTempStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devTempStat.setStatus("mandatory")
_DevISA_ObjectIdentity = ObjectIdentity
devISA = _DevISA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4)
)
_DevISAP12_ObjectIdentity = ObjectIdentity
devISAP12 = _DevISAP12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1)
)


class _DevISAP12Val_Type(Integer32):
    """Custom type devISAP12Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevISAP12Val_Type.__name__ = "Integer32"
_DevISAP12Val_Object = MibScalar
devISAP12Val = _DevISAP12Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 1),
    _DevISAP12Val_Type()
)
devISAP12Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devISAP12Val.setStatus("mandatory")


class _DevISAP12Min_Type(Integer32):
    """Custom type devISAP12Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevISAP12Min_Type.__name__ = "Integer32"
_DevISAP12Min_Object = MibScalar
devISAP12Min = _DevISAP12Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 2),
    _DevISAP12Min_Type()
)
devISAP12Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAP12Min.setStatus("mandatory")


class _DevISAP12Max_Type(Integer32):
    """Custom type devISAP12Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevISAP12Max_Type.__name__ = "Integer32"
_DevISAP12Max_Object = MibScalar
devISAP12Max = _DevISAP12Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 1, 3),
    _DevISAP12Max_Type()
)
devISAP12Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAP12Max.setStatus("mandatory")
_DevISAP5_ObjectIdentity = ObjectIdentity
devISAP5 = _DevISAP5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2)
)


class _DevISAP5Val_Type(Integer32):
    """Custom type devISAP5Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevISAP5Val_Type.__name__ = "Integer32"
_DevISAP5Val_Object = MibScalar
devISAP5Val = _DevISAP5Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 1),
    _DevISAP5Val_Type()
)
devISAP5Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devISAP5Val.setStatus("mandatory")


class _DevISAP5Min_Type(Integer32):
    """Custom type devISAP5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevISAP5Min_Type.__name__ = "Integer32"
_DevISAP5Min_Object = MibScalar
devISAP5Min = _DevISAP5Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 2),
    _DevISAP5Min_Type()
)
devISAP5Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAP5Min.setStatus("mandatory")


class _DevISAP5Max_Type(Integer32):
    """Custom type devISAP5Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevISAP5Max_Type.__name__ = "Integer32"
_DevISAP5Max_Object = MibScalar
devISAP5Max = _DevISAP5Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 2, 3),
    _DevISAP5Max_Type()
)
devISAP5Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAP5Max.setStatus("mandatory")
_DevISAN5_ObjectIdentity = ObjectIdentity
devISAN5 = _DevISAN5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3)
)


class _DevISAN5Val_Type(Integer32):
    """Custom type devISAN5Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevISAN5Val_Type.__name__ = "Integer32"
_DevISAN5Val_Object = MibScalar
devISAN5Val = _DevISAN5Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 1),
    _DevISAN5Val_Type()
)
devISAN5Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devISAN5Val.setStatus("mandatory")


class _DevISAN5Min_Type(Integer32):
    """Custom type devISAN5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevISAN5Min_Type.__name__ = "Integer32"
_DevISAN5Min_Object = MibScalar
devISAN5Min = _DevISAN5Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 2),
    _DevISAN5Min_Type()
)
devISAN5Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAN5Min.setStatus("mandatory")


class _DevISAN5Max_Type(Integer32):
    """Custom type devISAN5Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevISAN5Max_Type.__name__ = "Integer32"
_DevISAN5Max_Object = MibScalar
devISAN5Max = _DevISAN5Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 3, 3),
    _DevISAN5Max_Type()
)
devISAN5Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAN5Max.setStatus("mandatory")
_DevISAN12_ObjectIdentity = ObjectIdentity
devISAN12 = _DevISAN12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4)
)


class _DevISAN12Val_Type(Integer32):
    """Custom type devISAN12Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevISAN12Val_Type.__name__ = "Integer32"
_DevISAN12Val_Object = MibScalar
devISAN12Val = _DevISAN12Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 1),
    _DevISAN12Val_Type()
)
devISAN12Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devISAN12Val.setStatus("mandatory")


class _DevISAN12Min_Type(Integer32):
    """Custom type devISAN12Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevISAN12Min_Type.__name__ = "Integer32"
_DevISAN12Min_Object = MibScalar
devISAN12Min = _DevISAN12Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 2),
    _DevISAN12Min_Type()
)
devISAN12Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAN12Min.setStatus("mandatory")


class _DevISAN12Max_Type(Integer32):
    """Custom type devISAN12Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevISAN12Max_Type.__name__ = "Integer32"
_DevISAN12Max_Object = MibScalar
devISAN12Max = _DevISAN12Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 4, 3),
    _DevISAN12Max_Type()
)
devISAN12Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAN12Max.setStatus("mandatory")


class _DevISAStat_Type(Integer32):
    """Custom type devISAStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevISAStat_Type.__name__ = "Integer32"
_DevISAStat_Object = MibScalar
devISAStat = _DevISAStat_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 4, 10),
    _DevISAStat_Type()
)
devISAStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devISAStat.setStatus("mandatory")
_DevDC_ObjectIdentity = ObjectIdentity
devDC = _DevDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5)
)
_DevDCP12_ObjectIdentity = ObjectIdentity
devDCP12 = _DevDCP12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1)
)


class _DevDCP12Val_Type(Integer32):
    """Custom type devDCP12Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevDCP12Val_Type.__name__ = "Integer32"
_DevDCP12Val_Object = MibScalar
devDCP12Val = _DevDCP12Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 1),
    _DevDCP12Val_Type()
)
devDCP12Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDCP12Val.setStatus("mandatory")


class _DevDCP12Min_Type(Integer32):
    """Custom type devDCP12Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevDCP12Min_Type.__name__ = "Integer32"
_DevDCP12Min_Object = MibScalar
devDCP12Min = _DevDCP12Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 2),
    _DevDCP12Min_Type()
)
devDCP12Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDCP12Min.setStatus("mandatory")


class _DevDCP12Max_Type(Integer32):
    """Custom type devDCP12Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DevDCP12Max_Type.__name__ = "Integer32"
_DevDCP12Max_Object = MibScalar
devDCP12Max = _DevDCP12Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 1, 3),
    _DevDCP12Max_Type()
)
devDCP12Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDCP12Max.setStatus("mandatory")
_DevDCP5_ObjectIdentity = ObjectIdentity
devDCP5 = _DevDCP5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2)
)


class _DevDCP5Val_Type(Integer32):
    """Custom type devDCP5Val based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevDCP5Val_Type.__name__ = "Integer32"
_DevDCP5Val_Object = MibScalar
devDCP5Val = _DevDCP5Val_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 1),
    _DevDCP5Val_Type()
)
devDCP5Val.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devDCP5Val.setStatus("mandatory")


class _DevDCP5Min_Type(Integer32):
    """Custom type devDCP5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevDCP5Min_Type.__name__ = "Integer32"
_DevDCP5Min_Object = MibScalar
devDCP5Min = _DevDCP5Min_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 2),
    _DevDCP5Min_Type()
)
devDCP5Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDCP5Min.setStatus("mandatory")


class _DevDCP5Max_Type(Integer32):
    """Custom type devDCP5Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 700),
    )


_DevDCP5Max_Type.__name__ = "Integer32"
_DevDCP5Max_Object = MibScalar
devDCP5Max = _DevDCP5Max_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 2, 3),
    _DevDCP5Max_Type()
)
devDCP5Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDCP5Max.setStatus("mandatory")


class _DevDCStat_Type(Integer32):
    """Custom type devDCStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevDCStat_Type.__name__ = "Integer32"
_DevDCStat_Object = MibScalar
devDCStat = _DevDCStat_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 2, 5, 10),
    _DevDCStat_Type()
)
devDCStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devDCStat.setStatus("mandatory")


class _Control_Type(Integer32):
    """Custom type control based on Integer32"""
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
        *(("reset", 1),
          ("reset2fac", 4),
          ("reset2nvr", 3),
          ("updatenvr", 2))
    )


_Control_Type.__name__ = "Integer32"
_Control_Object = MibScalar
control = _Control_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 3),
    _Control_Type()
)
control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    control.setStatus("mandatory")
_Masks_ObjectIdentity = ObjectIdentity
masks = _Masks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4)
)


class _FanErrors_Type(Integer32):
    """Custom type fanErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FanErrors_Type.__name__ = "Integer32"
_FanErrors_Object = MibScalar
fanErrors = _FanErrors_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 1),
    _FanErrors_Type()
)
fanErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fanErrors.setStatus("mandatory")


class _TempErrors_Type(Integer32):
    """Custom type tempErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TempErrors_Type.__name__ = "Integer32"
_TempErrors_Object = MibScalar
tempErrors = _TempErrors_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 2),
    _TempErrors_Type()
)
tempErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempErrors.setStatus("mandatory")


class _IsaErrors_Type(Integer32):
    """Custom type isaErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IsaErrors_Type.__name__ = "Integer32"
_IsaErrors_Object = MibScalar
isaErrors = _IsaErrors_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 3),
    _IsaErrors_Type()
)
isaErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isaErrors.setStatus("mandatory")


class _DcErrors_Type(Integer32):
    """Custom type dcErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DcErrors_Type.__name__ = "Integer32"
_DcErrors_Object = MibScalar
dcErrors = _DcErrors_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 4),
    _DcErrors_Type()
)
dcErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dcErrors.setStatus("mandatory")


class _InputPSU_Type(Integer32):
    """Custom type inputPSU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InputPSU_Type.__name__ = "Integer32"
_InputPSU_Object = MibScalar
inputPSU = _InputPSU_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 7),
    _InputPSU_Type()
)
inputPSU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputPSU.setStatus("mandatory")


class _InputTamper_Type(Integer32):
    """Custom type inputTamper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_InputTamper_Type.__name__ = "Integer32"
_InputTamper_Object = MibScalar
inputTamper = _InputTamper_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 8),
    _InputTamper_Type()
)
inputTamper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inputTamper.setStatus("mandatory")


class _EnOutput0_Type(Integer32):
    """Custom type enOutput0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnOutput0_Type.__name__ = "Integer32"
_EnOutput0_Object = MibScalar
enOutput0 = _EnOutput0_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 9),
    _EnOutput0_Type()
)
enOutput0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enOutput0.setStatus("mandatory")


class _EnOutput1_Type(Integer32):
    """Custom type enOutput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnOutput1_Type.__name__ = "Integer32"
_EnOutput1_Object = MibScalar
enOutput1 = _EnOutput1_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 10),
    _EnOutput1_Type()
)
enOutput1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enOutput1.setStatus("mandatory")


class _EnOutput2_Type(Integer32):
    """Custom type enOutput2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnOutput2_Type.__name__ = "Integer32"
_EnOutput2_Object = MibScalar
enOutput2 = _EnOutput2_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 11),
    _EnOutput2_Type()
)
enOutput2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enOutput2.setStatus("mandatory")


class _EnOutput3_Type(Integer32):
    """Custom type enOutput3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnOutput3_Type.__name__ = "Integer32"
_EnOutput3_Object = MibScalar
enOutput3 = _EnOutput3_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 12),
    _EnOutput3_Type()
)
enOutput3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enOutput3.setStatus("mandatory")


class _EnBeeper_Type(Integer32):
    """Custom type enBeeper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnBeeper_Type.__name__ = "Integer32"
_EnBeeper_Object = MibScalar
enBeeper = _EnBeeper_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 13),
    _EnBeeper_Type()
)
enBeeper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enBeeper.setStatus("mandatory")


class _EnRelay_Type(Integer32):
    """Custom type enRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnRelay_Type.__name__ = "Integer32"
_EnRelay_Object = MibScalar
enRelay = _EnRelay_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 14),
    _EnRelay_Type()
)
enRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enRelay.setStatus("mandatory")


class _EnReset_Type(Integer32):
    """Custom type enReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnReset_Type.__name__ = "Integer32"
_EnReset_Object = MibScalar
enReset = _EnReset_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 4, 15),
    _EnReset_Type()
)
enReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enReset.setStatus("mandatory")
_Special_ObjectIdentity = ObjectIdentity
special = _Special_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3166, 1, 5)
)


class _Watchdog_Type(Integer32):
    """Custom type watchdog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Watchdog_Type.__name__ = "Integer32"
_Watchdog_Object = MibScalar
watchdog = _Watchdog_Object(
    (1, 3, 6, 1, 4, 1, 3166, 1, 5, 1),
    _Watchdog_Type()
)
watchdog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    watchdog.setStatus("mandatory")

# Managed Objects groups


# Notification objects

inputsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3166, 1, 0, 0)
)
if mibBuilder.loadTexts:
    inputsAlert.setStatus(
        ""
    )

fanAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3166, 1, 0, 1)
)
if mibBuilder.loadTexts:
    fanAlert.setStatus(
        ""
    )

tempAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3166, 1, 0, 2)
)
if mibBuilder.loadTexts:
    tempAlert.setStatus(
        ""
    )

isaAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3166, 1, 0, 3)
)
if mibBuilder.loadTexts:
    isaAlert.setStatus(
        ""
    )

dcAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 3166, 1, 0, 4)
)
if mibBuilder.loadTexts:
    dcAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "GUARDIAN-MIB",
    **{"westek": westek,
       "guardian": guardian,
       "inputsAlert": inputsAlert,
       "fanAlert": fanAlert,
       "tempAlert": tempAlert,
       "isaAlert": isaAlert,
       "dcAlert": dcAlert,
       "guardianRev": guardianRev,
       "device": device,
       "devInput": devInput,
       "devInput1": devInput1,
       "devInp1Val": devInp1Val,
       "devInp1Pol": devInp1Pol,
       "devInput2": devInput2,
       "devInp2Val": devInp2Val,
       "devInp2Pol": devInp2Pol,
       "devInput3": devInput3,
       "devInp3Val": devInp3Val,
       "devInp3Pol": devInp3Pol,
       "devInput4": devInput4,
       "devInp4Val": devInp4Val,
       "devInp4Pol": devInp4Pol,
       "devInpStat": devInpStat,
       "devFan": devFan,
       "devFan1": devFan1,
       "devFan1Val": devFan1Val,
       "devFan1Min": devFan1Min,
       "devFan1Max": devFan1Max,
       "devFan2": devFan2,
       "devFan2Val": devFan2Val,
       "devFan2Min": devFan2Min,
       "devFan2Max": devFan2Max,
       "devFan3": devFan3,
       "devFan3Val": devFan3Val,
       "devFan3Min": devFan3Min,
       "devFan3Max": devFan3Max,
       "devFan4": devFan4,
       "devFan4Val": devFan4Val,
       "devFan4Min": devFan4Min,
       "devFan4Max": devFan4Max,
       "devFanStat": devFanStat,
       "devTemp": devTemp,
       "devTemp1": devTemp1,
       "devTemp1Val": devTemp1Val,
       "devTemp1Min": devTemp1Min,
       "devTemp1Max": devTemp1Max,
       "devTemp2": devTemp2,
       "devTemp2Val": devTemp2Val,
       "devTemp2Min": devTemp2Min,
       "devTemp2Max": devTemp2Max,
       "devTemp3": devTemp3,
       "devTemp3Val": devTemp3Val,
       "devTemp3Min": devTemp3Min,
       "devTemp3Max": devTemp3Max,
       "devTemp4": devTemp4,
       "devTemp4Val": devTemp4Val,
       "devTemp4Min": devTemp4Min,
       "devTemp4Max": devTemp4Max,
       "devTemp5": devTemp5,
       "devTemp5Val": devTemp5Val,
       "devTemp5Min": devTemp5Min,
       "devTemp5Max": devTemp5Max,
       "devTemp6": devTemp6,
       "devTemp6Val": devTemp6Val,
       "devTemp6Min": devTemp6Min,
       "devTemp6Max": devTemp6Max,
       "devTemp7": devTemp7,
       "devTemp7Val": devTemp7Val,
       "devTemp7Min": devTemp7Min,
       "devTemp7Max": devTemp7Max,
       "devTemp8": devTemp8,
       "devTemp8Val": devTemp8Val,
       "devTemp8Min": devTemp8Min,
       "devTemp8Max": devTemp8Max,
       "devTempStat": devTempStat,
       "devISA": devISA,
       "devISAP12": devISAP12,
       "devISAP12Val": devISAP12Val,
       "devISAP12Min": devISAP12Min,
       "devISAP12Max": devISAP12Max,
       "devISAP5": devISAP5,
       "devISAP5Val": devISAP5Val,
       "devISAP5Min": devISAP5Min,
       "devISAP5Max": devISAP5Max,
       "devISAN5": devISAN5,
       "devISAN5Val": devISAN5Val,
       "devISAN5Min": devISAN5Min,
       "devISAN5Max": devISAN5Max,
       "devISAN12": devISAN12,
       "devISAN12Val": devISAN12Val,
       "devISAN12Min": devISAN12Min,
       "devISAN12Max": devISAN12Max,
       "devISAStat": devISAStat,
       "devDC": devDC,
       "devDCP12": devDCP12,
       "devDCP12Val": devDCP12Val,
       "devDCP12Min": devDCP12Min,
       "devDCP12Max": devDCP12Max,
       "devDCP5": devDCP5,
       "devDCP5Val": devDCP5Val,
       "devDCP5Min": devDCP5Min,
       "devDCP5Max": devDCP5Max,
       "devDCStat": devDCStat,
       "control": control,
       "masks": masks,
       "fanErrors": fanErrors,
       "tempErrors": tempErrors,
       "isaErrors": isaErrors,
       "dcErrors": dcErrors,
       "inputPSU": inputPSU,
       "inputTamper": inputTamper,
       "enOutput0": enOutput0,
       "enOutput1": enOutput1,
       "enOutput2": enOutput2,
       "enOutput3": enOutput3,
       "enBeeper": enBeeper,
       "enRelay": enRelay,
       "enReset": enReset,
       "special": special,
       "watchdog": watchdog}
)
