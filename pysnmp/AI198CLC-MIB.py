# SNMP MIB module (AI198CLC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AI198CLC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:05 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aiCLC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 539, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Aii_ObjectIdentity = ObjectIdentity
aii = _Aii_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539)
)
_AiSystemOID_ObjectIdentity = ObjectIdentity
aiSystemOID = _AiSystemOID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2)
)
_Ai198_ObjectIdentity = ObjectIdentity
ai198 = _Ai198_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198)
)
_Ai198Ver1_ObjectIdentity = ObjectIdentity
ai198Ver1 = _Ai198Ver1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1)
)
_Ai198Ver10_ObjectIdentity = ObjectIdentity
ai198Ver10 = _Ai198Ver10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0)
)
_Ai198Ver102_ObjectIdentity = ObjectIdentity
ai198Ver102 = _Ai198Ver102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0, 2)
)
_Ai198Ver103_ObjectIdentity = ObjectIdentity
ai198Ver103 = _Ai198Ver103_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0, 3)
)
_Ai198Ver104_ObjectIdentity = ObjectIdentity
ai198Ver104 = _Ai198Ver104_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 0, 4)
)
_Ai198Ver12_ObjectIdentity = ObjectIdentity
ai198Ver12 = _Ai198Ver12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 2)
)
_Ai198Ver120_ObjectIdentity = ObjectIdentity
ai198Ver120 = _Ai198Ver120_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 2, 0)
)
_Ai198Ver13_ObjectIdentity = ObjectIdentity
ai198Ver13 = _Ai198Ver13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 3)
)
_Ai198Ver130_ObjectIdentity = ObjectIdentity
ai198Ver130 = _Ai198Ver130_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 2, 198, 1, 3, 0)
)
_AiCLCSystem_ObjectIdentity = ObjectIdentity
aiCLCSystem = _AiCLCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 539, 9, 1)
)


class _AiCLCBox1DensAdmin_Type(Integer32):
    """Custom type aiCLCBox1DensAdmin based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox1DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox1DensAdmin_Object = MibScalar
aiCLCBox1DensAdmin = _AiCLCBox1DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 1),
    _AiCLCBox1DensAdmin_Type()
)
aiCLCBox1DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox1DensAdmin.setStatus("current")


class _AiCLCBox2DensAdmin_Type(Integer32):
    """Custom type aiCLCBox2DensAdmin based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox2DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox2DensAdmin_Object = MibScalar
aiCLCBox2DensAdmin = _AiCLCBox2DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 2),
    _AiCLCBox2DensAdmin_Type()
)
aiCLCBox2DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox2DensAdmin.setStatus("current")


class _AiCLCBox3DensAdmin_Type(Integer32):
    """Custom type aiCLCBox3DensAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox3DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox3DensAdmin_Object = MibScalar
aiCLCBox3DensAdmin = _AiCLCBox3DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 3),
    _AiCLCBox3DensAdmin_Type()
)
aiCLCBox3DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox3DensAdmin.setStatus("current")


class _AiCLCBox4DensAdmin_Type(Integer32):
    """Custom type aiCLCBox4DensAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox4DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox4DensAdmin_Object = MibScalar
aiCLCBox4DensAdmin = _AiCLCBox4DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 4),
    _AiCLCBox4DensAdmin_Type()
)
aiCLCBox4DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox4DensAdmin.setStatus("current")


class _AiCLCBox5DensAdmin_Type(Integer32):
    """Custom type aiCLCBox5DensAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox5DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox5DensAdmin_Object = MibScalar
aiCLCBox5DensAdmin = _AiCLCBox5DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 5),
    _AiCLCBox5DensAdmin_Type()
)
aiCLCBox5DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox5DensAdmin.setStatus("current")


class _AiCLCBox6DensAdmin_Type(Integer32):
    """Custom type aiCLCBox6DensAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox6DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox6DensAdmin_Object = MibScalar
aiCLCBox6DensAdmin = _AiCLCBox6DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 6),
    _AiCLCBox6DensAdmin_Type()
)
aiCLCBox6DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox6DensAdmin.setStatus("current")


class _AiCLCBox7DensAdmin_Type(Integer32):
    """Custom type aiCLCBox7DensAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox7DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox7DensAdmin_Object = MibScalar
aiCLCBox7DensAdmin = _AiCLCBox7DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 7),
    _AiCLCBox7DensAdmin_Type()
)
aiCLCBox7DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox7DensAdmin.setStatus("current")


class _AiCLCBox8DensAdmin_Type(Integer32):
    """Custom type aiCLCBox8DensAdmin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("eight", 8),
          ("four", 4),
          ("sixteen", 16),
          ("thirtytwo", 32))
    )


_AiCLCBox8DensAdmin_Type.__name__ = "Integer32"
_AiCLCBox8DensAdmin_Object = MibScalar
aiCLCBox8DensAdmin = _AiCLCBox8DensAdmin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 8),
    _AiCLCBox8DensAdmin_Type()
)
aiCLCBox8DensAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBox8DensAdmin.setStatus("current")


class _AiCLCNodeName_Type(DisplayString):
    """Custom type aiCLCNodeName based on DisplayString"""
    defaultValue = OctetString("NODE-XXX")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 29),
    )


_AiCLCNodeName_Type.__name__ = "DisplayString"
_AiCLCNodeName_Object = MibScalar
aiCLCNodeName = _AiCLCNodeName_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 9),
    _AiCLCNodeName_Type()
)
aiCLCNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCNodeName.setStatus("current")


class _AiCLCLogPortEnable_Type(Integer32):
    """Custom type aiCLCLogPortEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCLogPortEnable_Type.__name__ = "Integer32"
_AiCLCLogPortEnable_Object = MibScalar
aiCLCLogPortEnable = _AiCLCLogPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 10),
    _AiCLCLogPortEnable_Type()
)
aiCLCLogPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCLogPortEnable.setStatus("current")


class _AiCLCAlmLogPort_Type(Integer32):
    """Custom type aiCLCAlmLogPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCAlmLogPort_Type.__name__ = "Integer32"
_AiCLCAlmLogPort_Object = MibScalar
aiCLCAlmLogPort = _AiCLCAlmLogPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 11),
    _AiCLCAlmLogPort_Type()
)
aiCLCAlmLogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAlmLogPort.setStatus("current")


class _AiCLCActLogLvl_Type(Integer32):
    """Custom type aiCLCActLogLvl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AiCLCActLogLvl_Type.__name__ = "Integer32"
_AiCLCActLogLvl_Object = MibScalar
aiCLCActLogLvl = _AiCLCActLogLvl_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 12),
    _AiCLCActLogLvl_Type()
)
aiCLCActLogLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCActLogLvl.setStatus("current")


class _AiCLCMinorAlmMin_Type(Integer32):
    """Custom type aiCLCMinorAlmMin based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AiCLCMinorAlmMin_Type.__name__ = "Integer32"
_AiCLCMinorAlmMin_Object = MibScalar
aiCLCMinorAlmMin = _AiCLCMinorAlmMin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 13),
    _AiCLCMinorAlmMin_Type()
)
aiCLCMinorAlmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCMinorAlmMin.setStatus("current")


class _AiCLCMinorAlmMax_Type(Integer32):
    """Custom type aiCLCMinorAlmMax based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AiCLCMinorAlmMax_Type.__name__ = "Integer32"
_AiCLCMinorAlmMax_Object = MibScalar
aiCLCMinorAlmMax = _AiCLCMinorAlmMax_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 14),
    _AiCLCMinorAlmMax_Type()
)
aiCLCMinorAlmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCMinorAlmMax.setStatus("current")


class _AiCLCMajorAlmMin_Type(Integer32):
    """Custom type aiCLCMajorAlmMin based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AiCLCMajorAlmMin_Type.__name__ = "Integer32"
_AiCLCMajorAlmMin_Object = MibScalar
aiCLCMajorAlmMin = _AiCLCMajorAlmMin_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 15),
    _AiCLCMajorAlmMin_Type()
)
aiCLCMajorAlmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCMajorAlmMin.setStatus("current")


class _AiCLCMajorAlmMax_Type(Integer32):
    """Custom type aiCLCMajorAlmMax based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AiCLCMajorAlmMax_Type.__name__ = "Integer32"
_AiCLCMajorAlmMax_Object = MibScalar
aiCLCMajorAlmMax = _AiCLCMajorAlmMax_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 16),
    _AiCLCMajorAlmMax_Type()
)
aiCLCMajorAlmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCMajorAlmMax.setStatus("current")


class _AiCLCCraftLogEcho_Type(Integer32):
    """Custom type aiCLCCraftLogEcho based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCCraftLogEcho_Type.__name__ = "Integer32"
_AiCLCCraftLogEcho_Object = MibScalar
aiCLCCraftLogEcho = _AiCLCCraftLogEcho_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 17),
    _AiCLCCraftLogEcho_Type()
)
aiCLCCraftLogEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCraftLogEcho.setStatus("current")


class _AiCLCCaamlRoute_Type(DisplayString):
    """Custom type aiCLCCaamlRoute based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_AiCLCCaamlRoute_Type.__name__ = "DisplayString"
_AiCLCCaamlRoute_Object = MibScalar
aiCLCCaamlRoute = _AiCLCCaamlRoute_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 18),
    _AiCLCCaamlRoute_Type()
)
aiCLCCaamlRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCaamlRoute.setStatus("current")


class _AiCLCCaamlIdleTmr_Type(Integer32):
    """Custom type aiCLCCaamlIdleTmr based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCCaamlIdleTmr_Type.__name__ = "Integer32"
_AiCLCCaamlIdleTmr_Object = MibScalar
aiCLCCaamlIdleTmr = _AiCLCCaamlIdleTmr_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 19),
    _AiCLCCaamlIdleTmr_Type()
)
aiCLCCaamlIdleTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCaamlIdleTmr.setStatus("current")


class _AiCLCCaamlRetryTmr_Type(Integer32):
    """Custom type aiCLCCaamlRetryTmr based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCCaamlRetryTmr_Type.__name__ = "Integer32"
_AiCLCCaamlRetryTmr_Object = MibScalar
aiCLCCaamlRetryTmr = _AiCLCCaamlRetryTmr_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 20),
    _AiCLCCaamlRetryTmr_Type()
)
aiCLCCaamlRetryTmr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCaamlRetryTmr.setStatus("current")


class _AiCLCConnInfo_Type(Integer32):
    """Custom type aiCLCConnInfo based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCConnInfo_Type.__name__ = "Integer32"
_AiCLCConnInfo_Object = MibScalar
aiCLCConnInfo = _AiCLCConnInfo_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 21),
    _AiCLCConnInfo_Type()
)
aiCLCConnInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCConnInfo.setStatus("current")


class _AiCLCLongBrkLen_Type(Integer32):
    """Custom type aiCLCLongBrkLen based on Integer32"""
    defaultValue = 1875

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1875, 50000),
    )


_AiCLCLongBrkLen_Type.__name__ = "Integer32"
_AiCLCLongBrkLen_Object = MibScalar
aiCLCLongBrkLen = _AiCLCLongBrkLen_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 22),
    _AiCLCLongBrkLen_Type()
)
aiCLCLongBrkLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCLongBrkLen.setStatus("current")


class _AiCLCDestMenu_Type(Integer32):
    """Custom type aiCLCDestMenu based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDestMenu_Type.__name__ = "Integer32"
_AiCLCDestMenu_Object = MibScalar
aiCLCDestMenu = _AiCLCDestMenu_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 23),
    _AiCLCDestMenu_Type()
)
aiCLCDestMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestMenu.setStatus("current")


class _AiCLCDownSpd_Type(Integer32):
    """Custom type aiCLCDownSpd based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDownSpd_Type.__name__ = "Integer32"
_AiCLCDownSpd_Object = MibScalar
aiCLCDownSpd = _AiCLCDownSpd_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 24),
    _AiCLCDownSpd_Type()
)
aiCLCDownSpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDownSpd.setStatus("current")


class _AiCLCFaultSwitch_Type(Integer32):
    """Custom type aiCLCFaultSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCFaultSwitch_Type.__name__ = "Integer32"
_AiCLCFaultSwitch_Object = MibScalar
aiCLCFaultSwitch = _AiCLCFaultSwitch_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 25),
    _AiCLCFaultSwitch_Type()
)
aiCLCFaultSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCFaultSwitch.setStatus("current")


class _AiCLCDestMenuFmt_Type(Integer32):
    """Custom type aiCLCDestMenuFmt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fourCol", 4),
          ("oneCol", 1))
    )


_AiCLCDestMenuFmt_Type.__name__ = "Integer32"
_AiCLCDestMenuFmt_Object = MibScalar
aiCLCDestMenuFmt = _AiCLCDestMenuFmt_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 26),
    _AiCLCDestMenuFmt_Type()
)
aiCLCDestMenuFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestMenuFmt.setStatus("current")


class _AiCLCAutoCLCUpdate_Type(Integer32):
    """Custom type aiCLCAutoCLCUpdate based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCAutoCLCUpdate_Type.__name__ = "Integer32"
_AiCLCAutoCLCUpdate_Object = MibScalar
aiCLCAutoCLCUpdate = _AiCLCAutoCLCUpdate_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 27),
    _AiCLCAutoCLCUpdate_Type()
)
aiCLCAutoCLCUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAutoCLCUpdate.setStatus("current")


class _AiCLCAlarmLvl_Type(Integer32):
    """Custom type aiCLCAlarmLvl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AiCLCAlarmLvl_Type.__name__ = "Integer32"
_AiCLCAlarmLvl_Object = MibScalar
aiCLCAlarmLvl = _AiCLCAlarmLvl_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 28),
    _AiCLCAlarmLvl_Type()
)
aiCLCAlarmLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAlarmLvl.setStatus("current")
_AiCLCTimeDate_Type = DateAndTime
_AiCLCTimeDate_Object = MibScalar
aiCLCTimeDate = _AiCLCTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 29),
    _AiCLCTimeDate_Type()
)
aiCLCTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTimeDate.setStatus("current")
_AiCLCRstTimeDate_Type = DateAndTime
_AiCLCRstTimeDate_Object = MibScalar
aiCLCRstTimeDate = _AiCLCRstTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 30),
    _AiCLCRstTimeDate_Type()
)
aiCLCRstTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCRstTimeDate.setStatus("current")


class _AiCLCHoldConn_Type(Integer32):
    """Custom type aiCLCHoldConn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCHoldConn_Type.__name__ = "Integer32"
_AiCLCHoldConn_Object = MibScalar
aiCLCHoldConn = _AiCLCHoldConn_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 31),
    _AiCLCHoldConn_Type()
)
aiCLCHoldConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCHoldConn.setStatus("current")


class _AiCLCNumPorts_Type(Integer32):
    """Custom type aiCLCNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AiCLCNumPorts_Type.__name__ = "Integer32"
_AiCLCNumPorts_Object = MibScalar
aiCLCNumPorts = _AiCLCNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 32),
    _AiCLCNumPorts_Type()
)
aiCLCNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCNumPorts.setStatus("current")


class _AiCLCQueuedPorts_Type(Integer32):
    """Custom type aiCLCQueuedPorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCQueuedPorts_Type.__name__ = "Integer32"
_AiCLCQueuedPorts_Object = MibScalar
aiCLCQueuedPorts = _AiCLCQueuedPorts_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 33),
    _AiCLCQueuedPorts_Type()
)
aiCLCQueuedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCQueuedPorts.setStatus("current")


class _AiCLCEEPromFaults_Type(Integer32):
    """Custom type aiCLCEEPromFaults based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCEEPromFaults_Type.__name__ = "Integer32"
_AiCLCEEPromFaults_Object = MibScalar
aiCLCEEPromFaults = _AiCLCEEPromFaults_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 34),
    _AiCLCEEPromFaults_Type()
)
aiCLCEEPromFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCEEPromFaults.setStatus("current")


class _AiCLCFreeEE_Type(Integer32):
    """Custom type aiCLCFreeEE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_AiCLCFreeEE_Type.__name__ = "Integer32"
_AiCLCFreeEE_Object = MibScalar
aiCLCFreeEE = _AiCLCFreeEE_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 35),
    _AiCLCFreeEE_Type()
)
aiCLCFreeEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCFreeEE.setStatus("current")


class _AiCLCBuffers_Type(Integer32):
    """Custom type aiCLCBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCBuffers_Type.__name__ = "Integer32"
_AiCLCBuffers_Object = MibScalar
aiCLCBuffers = _AiCLCBuffers_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 36),
    _AiCLCBuffers_Type()
)
aiCLCBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCBuffers.setStatus("current")


class _AiCLCFreeBuffers_Type(Integer32):
    """Custom type aiCLCFreeBuffers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCFreeBuffers_Type.__name__ = "Integer32"
_AiCLCFreeBuffers_Object = MibScalar
aiCLCFreeBuffers = _AiCLCFreeBuffers_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 37),
    _AiCLCFreeBuffers_Type()
)
aiCLCFreeBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCFreeBuffers.setStatus("current")


class _AiCLCBufAllocErr_Type(Integer32):
    """Custom type aiCLCBufAllocErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCBufAllocErr_Type.__name__ = "Integer32"
_AiCLCBufAllocErr_Object = MibScalar
aiCLCBufAllocErr = _AiCLCBufAllocErr_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 38),
    _AiCLCBufAllocErr_Type()
)
aiCLCBufAllocErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCBufAllocErr.setStatus("current")


class _AiCLCBufAlign_Type(Integer32):
    """Custom type aiCLCBufAlign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCBufAlign_Type.__name__ = "Integer32"
_AiCLCBufAlign_Object = MibScalar
aiCLCBufAlign = _AiCLCBufAlign_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 39),
    _AiCLCBufAlign_Type()
)
aiCLCBufAlign.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCBufAlign.setStatus("current")


class _AiCLCCpuXacts_Type(Integer32):
    """Custom type aiCLCCpuXacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCCpuXacts_Type.__name__ = "Integer32"
_AiCLCCpuXacts_Object = MibScalar
aiCLCCpuXacts = _AiCLCCpuXacts_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 40),
    _AiCLCCpuXacts_Type()
)
aiCLCCpuXacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCpuXacts.setStatus("current")


class _AiCLCSLCXacts_Type(Integer32):
    """Custom type aiCLCSLCXacts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCSLCXacts_Type.__name__ = "Integer32"
_AiCLCSLCXacts_Object = MibScalar
aiCLCSLCXacts = _AiCLCSLCXacts_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 41),
    _AiCLCSLCXacts_Type()
)
aiCLCSLCXacts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCSLCXacts.setStatus("current")


class _AiCLCConnectionsPlaced_Type(Integer32):
    """Custom type aiCLCConnectionsPlaced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCConnectionsPlaced_Type.__name__ = "Integer32"
_AiCLCConnectionsPlaced_Object = MibScalar
aiCLCConnectionsPlaced = _AiCLCConnectionsPlaced_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 42),
    _AiCLCConnectionsPlaced_Type()
)
aiCLCConnectionsPlaced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCConnectionsPlaced.setStatus("current")


class _AiCLCTxTail_Type(Integer32):
    """Custom type aiCLCTxTail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCTxTail_Type.__name__ = "Integer32"
_AiCLCTxTail_Object = MibScalar
aiCLCTxTail = _AiCLCTxTail_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 43),
    _AiCLCTxTail_Type()
)
aiCLCTxTail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCTxTail.setStatus("current")


class _AiCLCEECRC_Type(Integer32):
    """Custom type aiCLCEECRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AiCLCEECRC_Type.__name__ = "Integer32"
_AiCLCEECRC_Object = MibScalar
aiCLCEECRC = _AiCLCEECRC_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 44),
    _AiCLCEECRC_Type()
)
aiCLCEECRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCEECRC.setStatus("current")
_AiCLCVersion_Type = DisplayString
_AiCLCVersion_Object = MibScalar
aiCLCVersion = _AiCLCVersion_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 45),
    _AiCLCVersion_Type()
)
aiCLCVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCVersion.setStatus("current")


class _AiCLCBackupCLC_Type(Integer32):
    """Custom type aiCLCBackupCLC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1))
    )


_AiCLCBackupCLC_Type.__name__ = "Integer32"
_AiCLCBackupCLC_Object = MibScalar
aiCLCBackupCLC = _AiCLCBackupCLC_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 46),
    _AiCLCBackupCLC_Type()
)
aiCLCBackupCLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCBackupCLC.setStatus("current")


class _AiCLCCpu_Type(Integer32):
    """Custom type aiCLCCpu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slotA", 1),
          ("slotB", 2))
    )


_AiCLCCpu_Type.__name__ = "Integer32"
_AiCLCCpu_Object = MibScalar
aiCLCCpu = _AiCLCCpu_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 47),
    _AiCLCCpu_Type()
)
aiCLCCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCpu.setStatus("current")


class _AiCLCCpyConfig_Type(Integer32):
    """Custom type aiCLCCpyConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copy", 2),
          ("none", 1))
    )


_AiCLCCpyConfig_Type.__name__ = "Integer32"
_AiCLCCpyConfig_Object = MibScalar
aiCLCCpyConfig = _AiCLCCpyConfig_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 48),
    _AiCLCCpyConfig_Type()
)
aiCLCCpyConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCpyConfig.setStatus("current")


class _AiCLCDLWinVerbose_Type(Integer32):
    """Custom type aiCLCDLWinVerbose based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDLWinVerbose_Type.__name__ = "Integer32"
_AiCLCDLWinVerbose_Object = MibScalar
aiCLCDLWinVerbose = _AiCLCDLWinVerbose_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 49),
    _AiCLCDLWinVerbose_Type()
)
aiCLCDLWinVerbose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDLWinVerbose.setStatus("current")


class _AiCLCDLWinIn_Type(Integer32):
    """Custom type aiCLCDLWinIn based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDLWinIn_Type.__name__ = "Integer32"
_AiCLCDLWinIn_Object = MibScalar
aiCLCDLWinIn = _AiCLCDLWinIn_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 50),
    _AiCLCDLWinIn_Type()
)
aiCLCDLWinIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDLWinIn.setStatus("current")


class _AiCLCDLWinOut_Type(Integer32):
    """Custom type aiCLCDLWinOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDLWinOut_Type.__name__ = "Integer32"
_AiCLCDLWinOut_Object = MibScalar
aiCLCDLWinOut = _AiCLCDLWinOut_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 51),
    _AiCLCDLWinOut_Type()
)
aiCLCDLWinOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDLWinOut.setStatus("current")


class _AiCLCDLWinUni_Type(Integer32):
    """Custom type aiCLCDLWinUni based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDLWinUni_Type.__name__ = "Integer32"
_AiCLCDLWinUni_Object = MibScalar
aiCLCDLWinUni = _AiCLCDLWinUni_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 52),
    _AiCLCDLWinUni_Type()
)
aiCLCDLWinUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDLWinUni.setStatus("current")


class _AiCLCDLMsgAll_Type(Integer32):
    """Custom type aiCLCDLMsgAll based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDLMsgAll_Type.__name__ = "Integer32"
_AiCLCDLMsgAll_Object = MibScalar
aiCLCDLMsgAll = _AiCLCDLMsgAll_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 53),
    _AiCLCDLMsgAll_Type()
)
aiCLCDLMsgAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDLMsgAll.setStatus("current")


class _AiCLCDLNoBody_Type(Integer32):
    """Custom type aiCLCDLNoBody based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDLNoBody_Type.__name__ = "Integer32"
_AiCLCDLNoBody_Object = MibScalar
aiCLCDLNoBody = _AiCLCDLNoBody_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 54),
    _AiCLCDLNoBody_Type()
)
aiCLCDLNoBody.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDLNoBody.setStatus("current")


class _AiCLCDLAlias_Type(Integer32):
    """Custom type aiCLCDLAlias based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDLAlias_Type.__name__ = "Integer32"
_AiCLCDLAlias_Object = MibScalar
aiCLCDLAlias = _AiCLCDLAlias_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 55),
    _AiCLCDLAlias_Type()
)
aiCLCDLAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDLAlias.setStatus("current")


class _AiCLCDebugVal_Type(Integer32):
    """Custom type aiCLCDebugVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 143),
    )


_AiCLCDebugVal_Type.__name__ = "Integer32"
_AiCLCDebugVal_Object = MibScalar
aiCLCDebugVal = _AiCLCDebugVal_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 56),
    _AiCLCDebugVal_Type()
)
aiCLCDebugVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDebugVal.setStatus("current")


class _AiCLCSwitchRestart_Type(Integer32):
    """Custom type aiCLCSwitchRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("nextCLC", 3),
          ("reset", 4),
          ("resetSLC", 5),
          ("restart", 1),
          ("restartCfg", 2))
    )


_AiCLCSwitchRestart_Type.__name__ = "Integer32"
_AiCLCSwitchRestart_Object = MibScalar
aiCLCSwitchRestart = _AiCLCSwitchRestart_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 57),
    _AiCLCSwitchRestart_Type()
)
aiCLCSwitchRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCSwitchRestart.setStatus("current")


class _AiCLCInitStrings_Type(Integer32):
    """Custom type aiCLCInitStrings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1))
    )


_AiCLCInitStrings_Type.__name__ = "Integer32"
_AiCLCInitStrings_Object = MibScalar
aiCLCInitStrings = _AiCLCInitStrings_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 58),
    _AiCLCInitStrings_Type()
)
aiCLCInitStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCInitStrings.setStatus("current")


class _AiCLCCopyFlash_Type(Integer32):
    """Custom type aiCLCCopyFlash based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("apas", 3),
          ("apbs", 2),
          ("asap", 5),
          ("asbs", 4),
          ("bpas", 6),
          ("bpbs", 7),
          ("bsas", 9),
          ("bsbp", 8),
          ("none", 1))
    )


_AiCLCCopyFlash_Type.__name__ = "Integer32"
_AiCLCCopyFlash_Object = MibScalar
aiCLCCopyFlash = _AiCLCCopyFlash_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 59),
    _AiCLCCopyFlash_Type()
)
aiCLCCopyFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCopyFlash.setStatus("current")


class _AiCLCCopyFlashToSLC_Type(Integer32):
    """Custom type aiCLCCopyFlashToSLC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AiCLCCopyFlashToSLC_Type.__name__ = "Integer32"
_AiCLCCopyFlashToSLC_Object = MibScalar
aiCLCCopyFlashToSLC = _AiCLCCopyFlashToSLC_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 60),
    _AiCLCCopyFlashToSLC_Type()
)
aiCLCCopyFlashToSLC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCopyFlashToSLC.setStatus("current")


class _AiCLCReadCommunity_Type(DisplayString):
    """Custom type aiCLCReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AiCLCReadCommunity_Type.__name__ = "DisplayString"
_AiCLCReadCommunity_Object = MibScalar
aiCLCReadCommunity = _AiCLCReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 61),
    _AiCLCReadCommunity_Type()
)
aiCLCReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCReadCommunity.setStatus("current")


class _AiCLCWriteCommunity_Type(DisplayString):
    """Custom type aiCLCWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AiCLCWriteCommunity_Type.__name__ = "DisplayString"
_AiCLCWriteCommunity_Object = MibScalar
aiCLCWriteCommunity = _AiCLCWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 62),
    _AiCLCWriteCommunity_Type()
)
aiCLCWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCWriteCommunity.setStatus("current")
_AiCLCIPAdrs_Type = IpAddress
_AiCLCIPAdrs_Object = MibScalar
aiCLCIPAdrs = _AiCLCIPAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 63),
    _AiCLCIPAdrs_Type()
)
aiCLCIPAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCIPAdrs.setStatus("current")
_AiCLCRouterIPAdrs_Type = IpAddress
_AiCLCRouterIPAdrs_Object = MibScalar
aiCLCRouterIPAdrs = _AiCLCRouterIPAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 64),
    _AiCLCRouterIPAdrs_Type()
)
aiCLCRouterIPAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRouterIPAdrs.setStatus("current")
_AiCLCSubnetIPAdrs_Type = IpAddress
_AiCLCSubnetIPAdrs_Object = MibScalar
aiCLCSubnetIPAdrs = _AiCLCSubnetIPAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 65),
    _AiCLCSubnetIPAdrs_Type()
)
aiCLCSubnetIPAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCSubnetIPAdrs.setStatus("current")
_AiCLCTrapTable_Object = MibTable
aiCLCTrapTable = _AiCLCTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 66)
)
if mibBuilder.loadTexts:
    aiCLCTrapTable.setStatus("current")
_AiCLCTrapTableEntry_Object = MibTableRow
aiCLCTrapTableEntry = _AiCLCTrapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 66, 1)
)
aiCLCTrapTableEntry.setIndexNames(
    (0, "AI198CLC-MIB", "aiCLCTrapIPAdrs"),
)
if mibBuilder.loadTexts:
    aiCLCTrapTableEntry.setStatus("current")
_AiCLCTrapIPAdrs_Type = IpAddress
_AiCLCTrapIPAdrs_Object = MibTableColumn
aiCLCTrapIPAdrs = _AiCLCTrapIPAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 66, 1, 1),
    _AiCLCTrapIPAdrs_Type()
)
aiCLCTrapIPAdrs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiCLCTrapIPAdrs.setStatus("current")


class _AiCLCTrapRowStatus_Type(Integer32):
    """Custom type aiCLCTrapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_AiCLCTrapRowStatus_Type.__name__ = "Integer32"
_AiCLCTrapRowStatus_Object = MibTableColumn
aiCLCTrapRowStatus = _AiCLCTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 66, 1, 2),
    _AiCLCTrapRowStatus_Type()
)
aiCLCTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiCLCTrapRowStatus.setStatus("current")


class _AiCLCLastTrapMsgText_Type(DisplayString):
    """Custom type aiCLCLastTrapMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_AiCLCLastTrapMsgText_Type.__name__ = "DisplayString"
_AiCLCLastTrapMsgText_Object = MibScalar
aiCLCLastTrapMsgText = _AiCLCLastTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 67),
    _AiCLCLastTrapMsgText_Type()
)
aiCLCLastTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCLastTrapMsgText.setStatus("current")


class _AiCLCLastTrapMsgNum_Type(Integer32):
    """Custom type aiCLCLastTrapMsgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiCLCLastTrapMsgNum_Type.__name__ = "Integer32"
_AiCLCLastTrapMsgNum_Object = MibScalar
aiCLCLastTrapMsgNum = _AiCLCLastTrapMsgNum_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 68),
    _AiCLCLastTrapMsgNum_Type()
)
aiCLCLastTrapMsgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCLastTrapMsgNum.setStatus("current")


class _AiCLCCrashMsgText_Type(DisplayString):
    """Custom type aiCLCCrashMsgText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_AiCLCCrashMsgText_Type.__name__ = "DisplayString"
_AiCLCCrashMsgText_Object = MibScalar
aiCLCCrashMsgText = _AiCLCCrashMsgText_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 69),
    _AiCLCCrashMsgText_Type()
)
aiCLCCrashMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCrashMsgText.setStatus("current")


class _AiCLCNumEventsSinceLastTrap_Type(Integer32):
    """Custom type aiCLCNumEventsSinceLastTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiCLCNumEventsSinceLastTrap_Type.__name__ = "Integer32"
_AiCLCNumEventsSinceLastTrap_Object = MibScalar
aiCLCNumEventsSinceLastTrap = _AiCLCNumEventsSinceLastTrap_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 70),
    _AiCLCNumEventsSinceLastTrap_Type()
)
aiCLCNumEventsSinceLastTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCNumEventsSinceLastTrap.setStatus("current")


class _AiCLCTrapTimer_Type(Integer32):
    """Custom type aiCLCTrapTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_AiCLCTrapTimer_Type.__name__ = "Integer32"
_AiCLCTrapTimer_Object = MibScalar
aiCLCTrapTimer = _AiCLCTrapTimer_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 71),
    _AiCLCTrapTimer_Type()
)
aiCLCTrapTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTrapTimer.setStatus("current")


class _AiCLCAsyncTrap_Type(Integer32):
    """Custom type aiCLCAsyncTrap based on Integer32"""
    defaultValue = 2

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


_AiCLCAsyncTrap_Type.__name__ = "Integer32"
_AiCLCAsyncTrap_Object = MibScalar
aiCLCAsyncTrap = _AiCLCAsyncTrap_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 72),
    _AiCLCAsyncTrap_Type()
)
aiCLCAsyncTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAsyncTrap.setStatus("current")


class _AiCLCTelnetServerPort_Type(Integer32):
    """Custom type aiCLCTelnetServerPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiCLCTelnetServerPort_Type.__name__ = "Integer32"
_AiCLCTelnetServerPort_Object = MibScalar
aiCLCTelnetServerPort = _AiCLCTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 73),
    _AiCLCTelnetServerPort_Type()
)
aiCLCTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTelnetServerPort.setStatus("current")


class _AiCLCColdStartTrapDelay_Type(Integer32):
    """Custom type aiCLCColdStartTrapDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AiCLCColdStartTrapDelay_Type.__name__ = "Integer32"
_AiCLCColdStartTrapDelay_Object = MibScalar
aiCLCColdStartTrapDelay = _AiCLCColdStartTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 74),
    _AiCLCColdStartTrapDelay_Type()
)
aiCLCColdStartTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCColdStartTrapDelay.setStatus("current")


class _AiCLCFtpCtrlPort_Type(Integer32):
    """Custom type aiCLCFtpCtrlPort based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiCLCFtpCtrlPort_Type.__name__ = "Integer32"
_AiCLCFtpCtrlPort_Object = MibScalar
aiCLCFtpCtrlPort = _AiCLCFtpCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 75),
    _AiCLCFtpCtrlPort_Type()
)
aiCLCFtpCtrlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCFtpCtrlPort.setStatus("current")


class _AiCLCBackupCLCHealth_Type(Integer32):
    """Custom type aiCLCBackupCLCHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 2),
          ("present", 1),
          ("presentFaulted", 3))
    )


_AiCLCBackupCLCHealth_Type.__name__ = "Integer32"
_AiCLCBackupCLCHealth_Object = MibScalar
aiCLCBackupCLCHealth = _AiCLCBackupCLCHealth_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 76),
    _AiCLCBackupCLCHealth_Type()
)
aiCLCBackupCLCHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCBackupCLCHealth.setStatus("current")


class _AiCLCBanner_Type(DisplayString):
    """Custom type aiCLCBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1170),
    )


_AiCLCBanner_Type.__name__ = "DisplayString"
_AiCLCBanner_Object = MibScalar
aiCLCBanner = _AiCLCBanner_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 77),
    _AiCLCBanner_Type()
)
aiCLCBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCBanner.setStatus("current")


class _AiCLCTimeZone_Type(Integer32):
    """Custom type aiCLCTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-720, 720),
    )


_AiCLCTimeZone_Type.__name__ = "Integer32"
_AiCLCTimeZone_Object = MibScalar
aiCLCTimeZone = _AiCLCTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 78),
    _AiCLCTimeZone_Type()
)
aiCLCTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTimeZone.setStatus("current")


class _AiCLCDaylightSavings_Type(Integer32):
    """Custom type aiCLCDaylightSavings based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDaylightSavings_Type.__name__ = "Integer32"
_AiCLCDaylightSavings_Object = MibScalar
aiCLCDaylightSavings = _AiCLCDaylightSavings_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 79),
    _AiCLCDaylightSavings_Type()
)
aiCLCDaylightSavings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDaylightSavings.setStatus("current")


class _AiCLCSNTP_Type(Integer32):
    """Custom type aiCLCSNTP based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCSNTP_Type.__name__ = "Integer32"
_AiCLCSNTP_Object = MibScalar
aiCLCSNTP = _AiCLCSNTP_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 80),
    _AiCLCSNTP_Type()
)
aiCLCSNTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCSNTP.setStatus("current")
_AiCLCSNTPPrimaryServer_Type = IpAddress
_AiCLCSNTPPrimaryServer_Object = MibScalar
aiCLCSNTPPrimaryServer = _AiCLCSNTPPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 81),
    _AiCLCSNTPPrimaryServer_Type()
)
aiCLCSNTPPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCSNTPPrimaryServer.setStatus("current")
_AiCLCSNTPSecondaryServer_Type = IpAddress
_AiCLCSNTPSecondaryServer_Object = MibScalar
aiCLCSNTPSecondaryServer = _AiCLCSNTPSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 82),
    _AiCLCSNTPSecondaryServer_Type()
)
aiCLCSNTPSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCSNTPSecondaryServer.setStatus("current")


class _AiCLCSNTPPollInterval_Type(Integer32):
    """Custom type aiCLCSNTPPollInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiCLCSNTPPollInterval_Type.__name__ = "Integer32"
_AiCLCSNTPPollInterval_Object = MibScalar
aiCLCSNTPPollInterval = _AiCLCSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 83),
    _AiCLCSNTPPollInterval_Type()
)
aiCLCSNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCSNTPPollInterval.setStatus("current")


class _AiCLCRadiusEnabled_Type(Integer32):
    """Custom type aiCLCRadiusEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("localFallback", 2))
    )


_AiCLCRadiusEnabled_Type.__name__ = "Integer32"
_AiCLCRadiusEnabled_Object = MibScalar
aiCLCRadiusEnabled = _AiCLCRadiusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 84),
    _AiCLCRadiusEnabled_Type()
)
aiCLCRadiusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRadiusEnabled.setStatus("current")
_AiCLCRadiusAddr1_Type = IpAddress
_AiCLCRadiusAddr1_Object = MibScalar
aiCLCRadiusAddr1 = _AiCLCRadiusAddr1_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 85),
    _AiCLCRadiusAddr1_Type()
)
aiCLCRadiusAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRadiusAddr1.setStatus("current")


class _AiCLCRadiusPort1_Type(Integer32):
    """Custom type aiCLCRadiusPort1 based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiCLCRadiusPort1_Type.__name__ = "Integer32"
_AiCLCRadiusPort1_Object = MibScalar
aiCLCRadiusPort1 = _AiCLCRadiusPort1_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 86),
    _AiCLCRadiusPort1_Type()
)
aiCLCRadiusPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRadiusPort1.setStatus("current")


class _AiCLCRadiusSecret1_Type(DisplayString):
    """Custom type aiCLCRadiusSecret1 based on DisplayString"""
    defaultValue = OctetString("applied")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AiCLCRadiusSecret1_Type.__name__ = "DisplayString"
_AiCLCRadiusSecret1_Object = MibScalar
aiCLCRadiusSecret1 = _AiCLCRadiusSecret1_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 87),
    _AiCLCRadiusSecret1_Type()
)
aiCLCRadiusSecret1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRadiusSecret1.setStatus("current")
_AiCLCRadiusAddr2_Type = IpAddress
_AiCLCRadiusAddr2_Object = MibScalar
aiCLCRadiusAddr2 = _AiCLCRadiusAddr2_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 88),
    _AiCLCRadiusAddr2_Type()
)
aiCLCRadiusAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRadiusAddr2.setStatus("current")


class _AiCLCRadiusPort2_Type(Integer32):
    """Custom type aiCLCRadiusPort2 based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiCLCRadiusPort2_Type.__name__ = "Integer32"
_AiCLCRadiusPort2_Object = MibScalar
aiCLCRadiusPort2 = _AiCLCRadiusPort2_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 89),
    _AiCLCRadiusPort2_Type()
)
aiCLCRadiusPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRadiusPort2.setStatus("current")


class _AiCLCRadiusSecret2_Type(DisplayString):
    """Custom type aiCLCRadiusSecret2 based on DisplayString"""
    defaultValue = OctetString("applied")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AiCLCRadiusSecret2_Type.__name__ = "DisplayString"
_AiCLCRadiusSecret2_Object = MibScalar
aiCLCRadiusSecret2 = _AiCLCRadiusSecret2_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 90),
    _AiCLCRadiusSecret2_Type()
)
aiCLCRadiusSecret2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCRadiusSecret2.setStatus("current")


class _AiCLCTrapInterval_Type(Integer32):
    """Custom type aiCLCTrapInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiCLCTrapInterval_Type.__name__ = "Integer32"
_AiCLCTrapInterval_Object = MibScalar
aiCLCTrapInterval = _AiCLCTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 91),
    _AiCLCTrapInterval_Type()
)
aiCLCTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTrapInterval.setStatus("current")


class _AiCLCTacacsEnabled_Type(Integer32):
    """Custom type aiCLCTacacsEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("localFallback", 2))
    )


_AiCLCTacacsEnabled_Type.__name__ = "Integer32"
_AiCLCTacacsEnabled_Object = MibScalar
aiCLCTacacsEnabled = _AiCLCTacacsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 92),
    _AiCLCTacacsEnabled_Type()
)
aiCLCTacacsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTacacsEnabled.setStatus("current")
_AiCLCTacacsAddr1_Type = IpAddress
_AiCLCTacacsAddr1_Object = MibScalar
aiCLCTacacsAddr1 = _AiCLCTacacsAddr1_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 93),
    _AiCLCTacacsAddr1_Type()
)
aiCLCTacacsAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTacacsAddr1.setStatus("current")


class _AiCLCTacacsPort1_Type(Integer32):
    """Custom type aiCLCTacacsPort1 based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiCLCTacacsPort1_Type.__name__ = "Integer32"
_AiCLCTacacsPort1_Object = MibScalar
aiCLCTacacsPort1 = _AiCLCTacacsPort1_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 94),
    _AiCLCTacacsPort1_Type()
)
aiCLCTacacsPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTacacsPort1.setStatus("current")


class _AiCLCTacacsSecret1_Type(DisplayString):
    """Custom type aiCLCTacacsSecret1 based on DisplayString"""
    defaultValue = OctetString("applied")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AiCLCTacacsSecret1_Type.__name__ = "DisplayString"
_AiCLCTacacsSecret1_Object = MibScalar
aiCLCTacacsSecret1 = _AiCLCTacacsSecret1_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 95),
    _AiCLCTacacsSecret1_Type()
)
aiCLCTacacsSecret1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTacacsSecret1.setStatus("current")
_AiCLCTacacsAddr2_Type = IpAddress
_AiCLCTacacsAddr2_Object = MibScalar
aiCLCTacacsAddr2 = _AiCLCTacacsAddr2_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 96),
    _AiCLCTacacsAddr2_Type()
)
aiCLCTacacsAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTacacsAddr2.setStatus("current")


class _AiCLCTacacsPort2_Type(Integer32):
    """Custom type aiCLCTacacsPort2 based on Integer32"""
    defaultValue = 49

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AiCLCTacacsPort2_Type.__name__ = "Integer32"
_AiCLCTacacsPort2_Object = MibScalar
aiCLCTacacsPort2 = _AiCLCTacacsPort2_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 97),
    _AiCLCTacacsPort2_Type()
)
aiCLCTacacsPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTacacsPort2.setStatus("current")


class _AiCLCTacacsSecret2_Type(DisplayString):
    """Custom type aiCLCTacacsSecret2 based on DisplayString"""
    defaultValue = OctetString("applied")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AiCLCTacacsSecret2_Type.__name__ = "DisplayString"
_AiCLCTacacsSecret2_Object = MibScalar
aiCLCTacacsSecret2 = _AiCLCTacacsSecret2_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 1, 98),
    _AiCLCTacacsSecret2_Type()
)
aiCLCTacacsSecret2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCTacacsSecret2.setStatus("current")
_AiCLCCardTable_Object = MibTable
aiCLCCardTable = _AiCLCCardTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2)
)
if mibBuilder.loadTexts:
    aiCLCCardTable.setStatus("current")
_AiCLCCardTableEntry_Object = MibTableRow
aiCLCCardTableEntry = _AiCLCCardTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1)
)
aiCLCCardTableEntry.setIndexNames(
    (0, "AI198CLC-MIB", "aiCLCCTIndex"),
)
if mibBuilder.loadTexts:
    aiCLCCardTableEntry.setStatus("current")


class _AiCLCCTIndex_Type(Integer32):
    """Custom type aiCLCCTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AiCLCCTIndex_Type.__name__ = "Integer32"
_AiCLCCTIndex_Object = MibTableColumn
aiCLCCTIndex = _AiCLCCTIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 1),
    _AiCLCCTIndex_Type()
)
aiCLCCTIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTIndex.setStatus("current")


class _AiCLCCTAdminStatus_Type(Integer32):
    """Custom type aiCLCCTAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AiCLCCTAdminStatus_Type.__name__ = "Integer32"
_AiCLCCTAdminStatus_Object = MibTableColumn
aiCLCCTAdminStatus = _AiCLCCTAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 2),
    _AiCLCCTAdminStatus_Type()
)
aiCLCCTAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTAdminStatus.setStatus("current")


class _AiCLCCTBasePort_Type(Integer32):
    """Custom type aiCLCCTBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCCTBasePort_Type.__name__ = "Integer32"
_AiCLCCTBasePort_Object = MibTableColumn
aiCLCCTBasePort = _AiCLCCTBasePort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 3),
    _AiCLCCTBasePort_Type()
)
aiCLCCTBasePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTBasePort.setStatus("current")


class _AiCLCCTHighPort_Type(Integer32):
    """Custom type aiCLCCTHighPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCCTHighPort_Type.__name__ = "Integer32"
_AiCLCCTHighPort_Object = MibTableColumn
aiCLCCTHighPort = _AiCLCCTHighPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 4),
    _AiCLCCTHighPort_Type()
)
aiCLCCTHighPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCTHighPort.setStatus("current")
_AiCLCCTRdCommStr_Type = DisplayString
_AiCLCCTRdCommStr_Object = MibTableColumn
aiCLCCTRdCommStr = _AiCLCCTRdCommStr_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 5),
    _AiCLCCTRdCommStr_Type()
)
aiCLCCTRdCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTRdCommStr.setStatus("current")
_AiCLCCTWrCommStr_Type = DisplayString
_AiCLCCTWrCommStr_Object = MibTableColumn
aiCLCCTWrCommStr = _AiCLCCTWrCommStr_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 6),
    _AiCLCCTWrCommStr_Type()
)
aiCLCCTWrCommStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTWrCommStr.setStatus("current")


class _AiCLCCTCardSnmpState_Type(Integer32):
    """Custom type aiCLCCTCardSnmpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nosnmp", 1),
          ("snmpDirect", 3),
          ("snmpProxy", 2))
    )


_AiCLCCTCardSnmpState_Type.__name__ = "Integer32"
_AiCLCCTCardSnmpState_Object = MibTableColumn
aiCLCCTCardSnmpState = _AiCLCCTCardSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 7),
    _AiCLCCTCardSnmpState_Type()
)
aiCLCCTCardSnmpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCTCardSnmpState.setStatus("current")


class _AiCLCCTCardType_Type(Integer32):
    """Custom type aiCLCCTCardType based on Integer32"""
    defaultValue = 1

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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("ai120", 19),
          ("ai196ILEG", 15),
          ("ai196im", 9),
          ("ai232", 14),
          ("ai2524", 7),
          ("ai285", 13),
          ("ai294", 8),
          ("ai296", 12),
          ("aie1", 20),
          ("aiflx", 17),
          ("aifocus", 22),
          ("aimod", 16),
          ("aitc", 21),
          ("aslc", 2),
          ("asp", 5),
          ("asynch", 1),
          ("empty", 18),
          ("ethernet", 3),
          ("islc", 6),
          ("islc1", 11),
          ("wanE1", 23),
          ("wanT1", 24),
          ("x25", 4),
          ("x25m", 10))
    )


_AiCLCCTCardType_Type.__name__ = "Integer32"
_AiCLCCTCardType_Object = MibTableColumn
aiCLCCTCardType = _AiCLCCTCardType_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 8),
    _AiCLCCTCardType_Type()
)
aiCLCCTCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTCardType.setStatus("current")


class _AiCLCCTSlotExp_Type(Integer32):
    """Custom type aiCLCCTSlotExp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AiCLCCTSlotExp_Type.__name__ = "Integer32"
_AiCLCCTSlotExp_Object = MibTableColumn
aiCLCCTSlotExp = _AiCLCCTSlotExp_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 9),
    _AiCLCCTSlotExp_Type()
)
aiCLCCTSlotExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTSlotExp.setStatus("current")
_AiCLCCTIPAdrs_Type = IpAddress
_AiCLCCTIPAdrs_Object = MibTableColumn
aiCLCCTIPAdrs = _AiCLCCTIPAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 10),
    _AiCLCCTIPAdrs_Type()
)
aiCLCCTIPAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTIPAdrs.setStatus("current")
_AiCLCCTRtrIPAdrs_Type = IpAddress
_AiCLCCTRtrIPAdrs_Object = MibTableColumn
aiCLCCTRtrIPAdrs = _AiCLCCTRtrIPAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 11),
    _AiCLCCTRtrIPAdrs_Type()
)
aiCLCCTRtrIPAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTRtrIPAdrs.setStatus("current")
_AiCLCCTSubnetMask_Type = IpAddress
_AiCLCCTSubnetMask_Object = MibTableColumn
aiCLCCTSubnetMask = _AiCLCCTSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 12),
    _AiCLCCTSubnetMask_Type()
)
aiCLCCTSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTSubnetMask.setStatus("current")


class _AiCLCCTAutoIdIndex_Type(Integer32):
    """Custom type aiCLCCTAutoIdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AiCLCCTAutoIdIndex_Type.__name__ = "Integer32"
_AiCLCCTAutoIdIndex_Object = MibTableColumn
aiCLCCTAutoIdIndex = _AiCLCCTAutoIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 13),
    _AiCLCCTAutoIdIndex_Type()
)
aiCLCCTAutoIdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCTAutoIdIndex.setStatus("current")
_AiCLCCTSysOID_Type = ObjectIdentifier
_AiCLCCTSysOID_Object = MibTableColumn
aiCLCCTSysOID = _AiCLCCTSysOID_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 14),
    _AiCLCCTSysOID_Type()
)
aiCLCCTSysOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCTSysOID.setStatus("current")


class _AiCLCCTRealCardType_Type(Integer32):
    """Custom type aiCLCCTRealCardType based on Integer32"""
    defaultValue = 1

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
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("ai120", 19),
          ("ai196ILEG", 15),
          ("ai196im", 9),
          ("ai232", 14),
          ("ai2524", 7),
          ("ai285", 13),
          ("ai294", 8),
          ("ai296", 12),
          ("aie1", 20),
          ("aiflx", 17),
          ("aifocus", 22),
          ("aimod", 16),
          ("aitc", 21),
          ("aslc", 2),
          ("asp", 5),
          ("asynch", 1),
          ("empty", 18),
          ("ethernet", 3),
          ("islc", 6),
          ("islc1", 11),
          ("wanE1", 23),
          ("wanT1", 24),
          ("x25", 4),
          ("x25m", 10))
    )


_AiCLCCTRealCardType_Type.__name__ = "Integer32"
_AiCLCCTRealCardType_Object = MibTableColumn
aiCLCCTRealCardType = _AiCLCCTRealCardType_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 15),
    _AiCLCCTRealCardType_Type()
)
aiCLCCTRealCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCTRealCardType.setStatus("current")


class _AiCLCCTIPRange_Type(Integer32):
    """Custom type aiCLCCTIPRange based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AiCLCCTIPRange_Type.__name__ = "Integer32"
_AiCLCCTIPRange_Object = MibTableColumn
aiCLCCTIPRange = _AiCLCCTIPRange_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 16),
    _AiCLCCTIPRange_Type()
)
aiCLCCTIPRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTIPRange.setStatus("current")


class _AiCLCCTTelnetPort_Type(Integer32):
    """Custom type aiCLCCTTelnetPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_AiCLCCTTelnetPort_Type.__name__ = "Integer32"
_AiCLCCTTelnetPort_Object = MibTableColumn
aiCLCCTTelnetPort = _AiCLCCTTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 17),
    _AiCLCCTTelnetPort_Type()
)
aiCLCCTTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTTelnetPort.setStatus("current")


class _AiCLCCTCardReset_Type(Integer32):
    """Custom type aiCLCCTCardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na", 3),
          ("off", 2),
          ("on", 1))
    )


_AiCLCCTCardReset_Type.__name__ = "Integer32"
_AiCLCCTCardReset_Object = MibTableColumn
aiCLCCTCardReset = _AiCLCCTCardReset_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 18),
    _AiCLCCTCardReset_Type()
)
aiCLCCTCardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTCardReset.setStatus("current")


class _AiCLCCTLastSequenceNumber_Type(Counter32):
    """Custom type aiCLCCTLastSequenceNumber based on Counter32"""
    defaultValue = 0


_AiCLCCTLastSequenceNumber_Object = MibTableColumn
aiCLCCTLastSequenceNumber = _AiCLCCTLastSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 19),
    _AiCLCCTLastSequenceNumber_Type()
)
aiCLCCTLastSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCCTLastSequenceNumber.setStatus("current")
_AiCLCCTRtr2IPAdrs_Type = IpAddress
_AiCLCCTRtr2IPAdrs_Object = MibTableColumn
aiCLCCTRtr2IPAdrs = _AiCLCCTRtr2IPAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 2, 1, 20),
    _AiCLCCTRtr2IPAdrs_Type()
)
aiCLCCTRtr2IPAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCTRtr2IPAdrs.setStatus("current")
_AiCLCPortTable_Object = MibTable
aiCLCPortTable = _AiCLCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3)
)
if mibBuilder.loadTexts:
    aiCLCPortTable.setStatus("current")
_AiCLCPortTableEntry_Object = MibTableRow
aiCLCPortTableEntry = _AiCLCPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1)
)
aiCLCPortTableEntry.setIndexNames(
    (0, "AI198CLC-MIB", "aiCLCPortNumber"),
)
if mibBuilder.loadTexts:
    aiCLCPortTableEntry.setStatus("current")


class _AiCLCPortNumber_Type(Integer32):
    """Custom type aiCLCPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCPortNumber_Type.__name__ = "Integer32"
_AiCLCPortNumber_Object = MibTableColumn
aiCLCPortNumber = _AiCLCPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 1),
    _AiCLCPortNumber_Type()
)
aiCLCPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCPortNumber.setStatus("current")


class _AiCLCPortType_Type(Integer32):
    """Custom type aiCLCPortType based on Integer32"""
    defaultValue = 1

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
        *(("actConn", 3),
          ("dedicated", 4),
          ("destination", 2),
          ("user", 1))
    )


_AiCLCPortType_Type.__name__ = "Integer32"
_AiCLCPortType_Object = MibTableColumn
aiCLCPortType = _AiCLCPortType_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 2),
    _AiCLCPortType_Type()
)
aiCLCPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortType.setStatus("current")


class _AiCLCPortDedicated_Type(Integer32):
    """Custom type aiCLCPortDedicated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCPortDedicated_Type.__name__ = "Integer32"
_AiCLCPortDedicated_Object = MibTableColumn
aiCLCPortDedicated = _AiCLCPortDedicated_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 3),
    _AiCLCPortDedicated_Type()
)
aiCLCPortDedicated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortDedicated.setStatus("current")


class _AiCLCPortDestName_Type(DisplayString):
    """Custom type aiCLCPortDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AiCLCPortDestName_Type.__name__ = "DisplayString"
_AiCLCPortDestName_Object = MibTableColumn
aiCLCPortDestName = _AiCLCPortDestName_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 4),
    _AiCLCPortDestName_Type()
)
aiCLCPortDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortDestName.setStatus("current")


class _AiCLCPortEcho_Type(Integer32):
    """Custom type aiCLCPortEcho based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCPortEcho_Type.__name__ = "Integer32"
_AiCLCPortEcho_Object = MibTableColumn
aiCLCPortEcho = _AiCLCPortEcho_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 5),
    _AiCLCPortEcho_Type()
)
aiCLCPortEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortEcho.setStatus("current")


class _AiCLCPortDestMenu_Type(Integer32):
    """Custom type aiCLCPortDestMenu based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCPortDestMenu_Type.__name__ = "Integer32"
_AiCLCPortDestMenu_Object = MibTableColumn
aiCLCPortDestMenu = _AiCLCPortDestMenu_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 6),
    _AiCLCPortDestMenu_Type()
)
aiCLCPortDestMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortDestMenu.setStatus("current")


class _AiCLCPortQueue_Type(Integer32):
    """Custom type aiCLCPortQueue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCPortQueue_Type.__name__ = "Integer32"
_AiCLCPortQueue_Object = MibTableColumn
aiCLCPortQueue = _AiCLCPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 7),
    _AiCLCPortQueue_Type()
)
aiCLCPortQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortQueue.setStatus("current")


class _AiCLCSLCProtocolCode_Type(Integer32):
    """Custom type aiCLCSLCProtocolCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCSLCProtocolCode_Type.__name__ = "Integer32"
_AiCLCSLCProtocolCode_Object = MibTableColumn
aiCLCSLCProtocolCode = _AiCLCSLCProtocolCode_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 8),
    _AiCLCSLCProtocolCode_Type()
)
aiCLCSLCProtocolCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCSLCProtocolCode.setStatus("current")


class _AiCLCPortState_Type(Integer32):
    """Custom type aiCLCPortState based on Integer32"""
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


_AiCLCPortState_Type.__name__ = "Integer32"
_AiCLCPortState_Object = MibTableColumn
aiCLCPortState = _AiCLCPortState_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 9),
    _AiCLCPortState_Type()
)
aiCLCPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCPortState.setStatus("current")


class _AiCLCPortStatus_Type(Integer32):
    """Custom type aiCLCPortStatus based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ai", 10),
          ("conn", 11),
          ("dna", 5),
          ("file", 16),
          ("hold", 14),
          ("holdq", 8),
          ("idle", 1),
          ("inact", 17),
          ("netconn", 15),
          ("preconn", 12),
          ("predisc", 13),
          ("pswd", 3),
          ("queue", 7),
          ("selcos", 2),
          ("swdwn", 18),
          ("tcp", 6),
          ("telnetClient", 19),
          ("uname", 4),
          ("unknown", 20),
          ("waitq", 9))
    )


_AiCLCPortStatus_Type.__name__ = "Integer32"
_AiCLCPortStatus_Object = MibTableColumn
aiCLCPortStatus = _AiCLCPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 10),
    _AiCLCPortStatus_Type()
)
aiCLCPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCPortStatus.setStatus("current")


class _AiCLCPortAlm_Type(Integer32):
    """Custom type aiCLCPortAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AiCLCPortAlm_Type.__name__ = "Integer32"
_AiCLCPortAlm_Object = MibTableColumn
aiCLCPortAlm = _AiCLCPortAlm_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 11),
    _AiCLCPortAlm_Type()
)
aiCLCPortAlm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCPortAlm.setStatus("current")


class _AiCLCPortDesc_Type(DisplayString):
    """Custom type aiCLCPortDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 29),
    )


_AiCLCPortDesc_Type.__name__ = "DisplayString"
_AiCLCPortDesc_Object = MibTableColumn
aiCLCPortDesc = _AiCLCPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 12),
    _AiCLCPortDesc_Type()
)
aiCLCPortDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortDesc.setStatus("current")


class _AiCLCPortReset_Type(Integer32):
    """Custom type aiCLCPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCPortReset_Type.__name__ = "Integer32"
_AiCLCPortReset_Object = MibTableColumn
aiCLCPortReset = _AiCLCPortReset_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 3, 1, 13),
    _AiCLCPortReset_Type()
)
aiCLCPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCPortReset.setStatus("current")
_AiCLCAliasTable_Object = MibTable
aiCLCAliasTable = _AiCLCAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4)
)
if mibBuilder.loadTexts:
    aiCLCAliasTable.setStatus("current")
_AiCLCAliasTableEntry_Object = MibTableRow
aiCLCAliasTableEntry = _AiCLCAliasTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1)
)
aiCLCAliasTableEntry.setIndexNames(
    (1, "AI198CLC-MIB", "aiCLCAliasIndex"),
)
if mibBuilder.loadTexts:
    aiCLCAliasTableEntry.setStatus("current")


class _AiCLCAliasIndex_Type(DisplayString):
    """Custom type aiCLCAliasIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_AiCLCAliasIndex_Type.__name__ = "DisplayString"
_AiCLCAliasIndex_Object = MibTableColumn
aiCLCAliasIndex = _AiCLCAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 1),
    _AiCLCAliasIndex_Type()
)
aiCLCAliasIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiCLCAliasIndex.setStatus("current")


class _AiCLCAliasRowStatus_Type(Integer32):
    """Custom type aiCLCAliasRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_AiCLCAliasRowStatus_Type.__name__ = "Integer32"
_AiCLCAliasRowStatus_Object = MibTableColumn
aiCLCAliasRowStatus = _AiCLCAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 2),
    _AiCLCAliasRowStatus_Type()
)
aiCLCAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiCLCAliasRowStatus.setStatus("current")


class _AiCLCXlatType_Type(Integer32):
    """Custom type aiCLCXlatType based on Integer32"""
    defaultValue = 1

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
        *(("muxconn", 2),
          ("muxxlat", 3),
          ("simple", 1),
          ("slcroute", 4))
    )


_AiCLCXlatType_Type.__name__ = "Integer32"
_AiCLCXlatType_Object = MibTableColumn
aiCLCXlatType = _AiCLCXlatType_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 3),
    _AiCLCXlatType_Type()
)
aiCLCXlatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCXlatType.setStatus("current")
_AiCLCAliasDestName_Type = DisplayString
_AiCLCAliasDestName_Object = MibTableColumn
aiCLCAliasDestName = _AiCLCAliasDestName_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 4),
    _AiCLCAliasDestName_Type()
)
aiCLCAliasDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAliasDestName.setStatus("current")
_AiCLCCalledAdrs_Type = DisplayString
_AiCLCCalledAdrs_Object = MibTableColumn
aiCLCCalledAdrs = _AiCLCCalledAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 5),
    _AiCLCCalledAdrs_Type()
)
aiCLCCalledAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCalledAdrs.setStatus("current")


class _AiCLCAliasDestMenu_Type(Integer32):
    """Custom type aiCLCAliasDestMenu based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCAliasDestMenu_Type.__name__ = "Integer32"
_AiCLCAliasDestMenu_Object = MibTableColumn
aiCLCAliasDestMenu = _AiCLCAliasDestMenu_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 6),
    _AiCLCAliasDestMenu_Type()
)
aiCLCAliasDestMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAliasDestMenu.setStatus("current")
_AiCLCLinkNum_Type = DisplayString
_AiCLCLinkNum_Object = MibTableColumn
aiCLCLinkNum = _AiCLCLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 7),
    _AiCLCLinkNum_Type()
)
aiCLCLinkNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCLinkNum.setStatus("current")
_AiCLCCallerAdrs_Type = DisplayString
_AiCLCCallerAdrs_Object = MibTableColumn
aiCLCCallerAdrs = _AiCLCCallerAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 8),
    _AiCLCCallerAdrs_Type()
)
aiCLCCallerAdrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCallerAdrs.setStatus("current")
_AiCLCCallData_Type = DisplayString
_AiCLCCallData_Object = MibTableColumn
aiCLCCallData = _AiCLCCallData_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 9),
    _AiCLCCallData_Type()
)
aiCLCCallData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCallData.setStatus("current")
_AiCLCApplicString_Type = DisplayString
_AiCLCApplicString_Object = MibTableColumn
aiCLCApplicString = _AiCLCApplicString_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 10),
    _AiCLCApplicString_Type()
)
aiCLCApplicString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCApplicString.setStatus("current")
_AiCLCCalledProtoStr_Type = DisplayString
_AiCLCCalledProtoStr_Object = MibTableColumn
aiCLCCalledProtoStr = _AiCLCCalledProtoStr_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 11),
    _AiCLCCalledProtoStr_Type()
)
aiCLCCalledProtoStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCalledProtoStr.setStatus("current")
_AiCLCCallerProtoStr_Type = DisplayString
_AiCLCCallerProtoStr_Object = MibTableColumn
aiCLCCallerProtoStr = _AiCLCCallerProtoStr_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 12),
    _AiCLCCallerProtoStr_Type()
)
aiCLCCallerProtoStr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCCallerProtoStr.setStatus("current")
_AiCLCAlternRoute_Type = DisplayString
_AiCLCAlternRoute_Object = MibTableColumn
aiCLCAlternRoute = _AiCLCAlternRoute_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 13),
    _AiCLCAlternRoute_Type()
)
aiCLCAlternRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAlternRoute.setStatus("current")


class _AiCLCAliasPosition_Type(DisplayString):
    """Custom type aiCLCAliasPosition based on DisplayString"""
    defaultValue = 1

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_AiCLCAliasPosition_Type.__name__ = "DisplayString"
_AiCLCAliasPosition_Object = MibTableColumn
aiCLCAliasPosition = _AiCLCAliasPosition_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 4, 1, 14),
    _AiCLCAliasPosition_Type()
)
aiCLCAliasPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAliasPosition.setStatus("current")
_AiCLCDestTable_Object = MibTable
aiCLCDestTable = _AiCLCDestTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5)
)
if mibBuilder.loadTexts:
    aiCLCDestTable.setStatus("current")
_AiCLCDestTableEntry_Object = MibTableRow
aiCLCDestTableEntry = _AiCLCDestTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1)
)
aiCLCDestTableEntry.setIndexNames(
    (1, "AI198CLC-MIB", "aiCLCDestName"),
)
if mibBuilder.loadTexts:
    aiCLCDestTableEntry.setStatus("current")


class _AiCLCDestName_Type(DisplayString):
    """Custom type aiCLCDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AiCLCDestName_Type.__name__ = "DisplayString"
_AiCLCDestName_Object = MibTableColumn
aiCLCDestName = _AiCLCDestName_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 1),
    _AiCLCDestName_Type()
)
aiCLCDestName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiCLCDestName.setStatus("current")


class _AiCLCDestRowStatus_Type(Integer32):
    """Custom type aiCLCDestRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_AiCLCDestRowStatus_Type.__name__ = "Integer32"
_AiCLCDestRowStatus_Object = MibTableColumn
aiCLCDestRowStatus = _AiCLCDestRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 2),
    _AiCLCDestRowStatus_Type()
)
aiCLCDestRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aiCLCDestRowStatus.setStatus("current")


class _AiCLCDestCallInit_Type(Integer32):
    """Custom type aiCLCDestCallInit based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDestCallInit_Type.__name__ = "Integer32"
_AiCLCDestCallInit_Object = MibTableColumn
aiCLCDestCallInit = _AiCLCDestCallInit_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 3),
    _AiCLCDestCallInit_Type()
)
aiCLCDestCallInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestCallInit.setStatus("current")


class _AiCLCDestDisc_Type(Integer32):
    """Custom type aiCLCDestDisc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDestDisc_Type.__name__ = "Integer32"
_AiCLCDestDisc_Object = MibTableColumn
aiCLCDestDisc = _AiCLCDestDisc_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 4),
    _AiCLCDestDisc_Type()
)
aiCLCDestDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestDisc.setStatus("current")


class _AiCLCDestDispMenu_Type(Integer32):
    """Custom type aiCLCDestDispMenu based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDestDispMenu_Type.__name__ = "Integer32"
_AiCLCDestDispMenu_Object = MibTableColumn
aiCLCDestDispMenu = _AiCLCDestDispMenu_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 5),
    _AiCLCDestDispMenu_Type()
)
aiCLCDestDispMenu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestDispMenu.setStatus("current")


class _AiCLCDestBaud_Type(Integer32):
    """Custom type aiCLCDestBaud based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDestBaud_Type.__name__ = "Integer32"
_AiCLCDestBaud_Object = MibTableColumn
aiCLCDestBaud = _AiCLCDestBaud_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 6),
    _AiCLCDestBaud_Type()
)
aiCLCDestBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestBaud.setStatus("current")


class _AiCLCDestIsSwitch_Type(Integer32):
    """Custom type aiCLCDestIsSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_AiCLCDestIsSwitch_Type.__name__ = "Integer32"
_AiCLCDestIsSwitch_Object = MibTableColumn
aiCLCDestIsSwitch = _AiCLCDestIsSwitch_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 7),
    _AiCLCDestIsSwitch_Type()
)
aiCLCDestIsSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestIsSwitch.setStatus("current")


class _AiCLCDestTmrType_Type(Integer32):
    """Custom type aiCLCDestTmrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("actTmr", 1),
          ("sessTmr", 2))
    )


_AiCLCDestTmrType_Type.__name__ = "Integer32"
_AiCLCDestTmrType_Object = MibTableColumn
aiCLCDestTmrType = _AiCLCDestTmrType_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 8),
    _AiCLCDestTmrType_Type()
)
aiCLCDestTmrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestTmrType.setStatus("current")


class _AiCLCDestTmrVal_Type(Integer32):
    """Custom type aiCLCDestTmrVal based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4368000),
    )


_AiCLCDestTmrVal_Type.__name__ = "Integer32"
_AiCLCDestTmrVal_Object = MibTableColumn
aiCLCDestTmrVal = _AiCLCDestTmrVal_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 9),
    _AiCLCDestTmrVal_Type()
)
aiCLCDestTmrVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestTmrVal.setStatus("current")


class _AiCLCDestTmrDelay_Type(Integer32):
    """Custom type aiCLCDestTmrDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4368000),
    )


_AiCLCDestTmrDelay_Type.__name__ = "Integer32"
_AiCLCDestTmrDelay_Object = MibTableColumn
aiCLCDestTmrDelay = _AiCLCDestTmrDelay_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 10),
    _AiCLCDestTmrDelay_Type()
)
aiCLCDestTmrDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestTmrDelay.setStatus("current")


class _AiCLCDestPswd_Type(DisplayString):
    """Custom type aiCLCDestPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AiCLCDestPswd_Type.__name__ = "DisplayString"
_AiCLCDestPswd_Object = MibTableColumn
aiCLCDestPswd = _AiCLCDestPswd_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 11),
    _AiCLCDestPswd_Type()
)
aiCLCDestPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestPswd.setStatus("current")


class _AiCLCDestQPswd_Type(DisplayString):
    """Custom type aiCLCDestQPswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AiCLCDestQPswd_Type.__name__ = "DisplayString"
_AiCLCDestQPswd_Object = MibTableColumn
aiCLCDestQPswd = _AiCLCDestQPswd_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 12),
    _AiCLCDestQPswd_Type()
)
aiCLCDestQPswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestQPswd.setStatus("current")
_AiCLCDestMenuMsg_Type = DisplayString
_AiCLCDestMenuMsg_Object = MibTableColumn
aiCLCDestMenuMsg = _AiCLCDestMenuMsg_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 13),
    _AiCLCDestMenuMsg_Type()
)
aiCLCDestMenuMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestMenuMsg.setStatus("current")
_AiCLCDestConnMsg_Type = DisplayString
_AiCLCDestConnMsg_Object = MibTableColumn
aiCLCDestConnMsg = _AiCLCDestConnMsg_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 14),
    _AiCLCDestConnMsg_Type()
)
aiCLCDestConnMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestConnMsg.setStatus("current")
_AiCLCDestDiscMsg_Type = DisplayString
_AiCLCDestDiscMsg_Object = MibTableColumn
aiCLCDestDiscMsg = _AiCLCDestDiscMsg_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 15),
    _AiCLCDestDiscMsg_Type()
)
aiCLCDestDiscMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestDiscMsg.setStatus("current")


class _AiCLCDestState_Type(Integer32):
    """Custom type aiCLCDestState based on Integer32"""
    defaultValue = 1

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


_AiCLCDestState_Type.__name__ = "Integer32"
_AiCLCDestState_Object = MibTableColumn
aiCLCDestState = _AiCLCDestState_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 16),
    _AiCLCDestState_Type()
)
aiCLCDestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestState.setStatus("current")


class _AiCLCDestNumPorts_Type(Integer32):
    """Custom type aiCLCDestNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AiCLCDestNumPorts_Type.__name__ = "Integer32"
_AiCLCDestNumPorts_Object = MibTableColumn
aiCLCDestNumPorts = _AiCLCDestNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 17),
    _AiCLCDestNumPorts_Type()
)
aiCLCDestNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCDestNumPorts.setStatus("current")


class _AiCLCDestNumUsed_Type(Integer32):
    """Custom type aiCLCDestNumUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AiCLCDestNumUsed_Type.__name__ = "Integer32"
_AiCLCDestNumUsed_Object = MibTableColumn
aiCLCDestNumUsed = _AiCLCDestNumUsed_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 18),
    _AiCLCDestNumUsed_Type()
)
aiCLCDestNumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCDestNumUsed.setStatus("current")


class _AiCLCDestNumFree_Type(Integer32):
    """Custom type aiCLCDestNumFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AiCLCDestNumFree_Type.__name__ = "Integer32"
_AiCLCDestNumFree_Object = MibTableColumn
aiCLCDestNumFree = _AiCLCDestNumFree_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 19),
    _AiCLCDestNumFree_Type()
)
aiCLCDestNumFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCDestNumFree.setStatus("current")


class _AiCLCDestQHigh_Type(Integer32):
    """Custom type aiCLCDestQHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AiCLCDestQHigh_Type.__name__ = "Integer32"
_AiCLCDestQHigh_Object = MibTableColumn
aiCLCDestQHigh = _AiCLCDestQHigh_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 20),
    _AiCLCDestQHigh_Type()
)
aiCLCDestQHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCDestQHigh.setStatus("current")
_AiCLCDestPortList_Type = DisplayString
_AiCLCDestPortList_Object = MibTableColumn
aiCLCDestPortList = _AiCLCDestPortList_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 21),
    _AiCLCDestPortList_Type()
)
aiCLCDestPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCDestPortList.setStatus("current")


class _AiCLCDestWaitForPort_Type(Integer32):
    """Custom type aiCLCDestWaitForPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCDestWaitForPort_Type.__name__ = "Integer32"
_AiCLCDestWaitForPort_Object = MibTableColumn
aiCLCDestWaitForPort = _AiCLCDestWaitForPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 5, 1, 22),
    _AiCLCDestWaitForPort_Type()
)
aiCLCDestWaitForPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCDestWaitForPort.setStatus("current")
_AiCLCAsyncTable_Object = MibTable
aiCLCAsyncTable = _AiCLCAsyncTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6)
)
if mibBuilder.loadTexts:
    aiCLCAsyncTable.setStatus("current")
_AiCLCAsyncTableEntry_Object = MibTableRow
aiCLCAsyncTableEntry = _AiCLCAsyncTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1)
)
aiCLCAsyncTableEntry.setIndexNames(
    (0, "AI198CLC-MIB", "aiCLCAsyncifIndex"),
)
if mibBuilder.loadTexts:
    aiCLCAsyncTableEntry.setStatus("current")
_AiCLCAsyncifIndex_Type = Integer32
_AiCLCAsyncifIndex_Object = MibTableColumn
aiCLCAsyncifIndex = _AiCLCAsyncifIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 1),
    _AiCLCAsyncifIndex_Type()
)
aiCLCAsyncifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAsyncifIndex.setStatus("current")


class _AiCLCAsyncPort_Type(Integer32):
    """Custom type aiCLCAsyncPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCAsyncPort_Type.__name__ = "Integer32"
_AiCLCAsyncPort_Object = MibTableColumn
aiCLCAsyncPort = _AiCLCAsyncPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 2),
    _AiCLCAsyncPort_Type()
)
aiCLCAsyncPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAsyncPort.setStatus("current")


class _AiCLCAsyncAdminStatus_Type(Integer32):
    """Custom type aiCLCAsyncAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AiCLCAsyncAdminStatus_Type.__name__ = "Integer32"
_AiCLCAsyncAdminStatus_Object = MibTableColumn
aiCLCAsyncAdminStatus = _AiCLCAsyncAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 3),
    _AiCLCAsyncAdminStatus_Type()
)
aiCLCAsyncAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAsyncAdminStatus.setStatus("current")


class _AiCLCAsyncDiscType_Type(Integer32):
    """Custom type aiCLCAsyncDiscType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("brkdisc", 2),
          ("longbrkdisc", 3),
          ("nobrkdisc", 1))
    )


_AiCLCAsyncDiscType_Type.__name__ = "Integer32"
_AiCLCAsyncDiscType_Object = MibTableColumn
aiCLCAsyncDiscType = _AiCLCAsyncDiscType_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 4),
    _AiCLCAsyncDiscType_Type()
)
aiCLCAsyncDiscType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCAsyncDiscType.setStatus("current")


class _AiCLCEIASignals_Type(Integer32):
    """Custom type aiCLCEIASignals based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dcdOffDisc", 5),
          ("dcdOnOffDisc", 6),
          ("dsrOffDisc", 3),
          ("dsrOnOffDisc", 4),
          ("dsrRtsPass", 2),
          ("eiaDisabled", 1))
    )


_AiCLCEIASignals_Type.__name__ = "Integer32"
_AiCLCEIASignals_Object = MibTableColumn
aiCLCEIASignals = _AiCLCEIASignals_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 5),
    _AiCLCEIASignals_Type()
)
aiCLCEIASignals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCEIASignals.setStatus("current")


class _AiCLCEIARtsDisc_Type(Integer32):
    """Custom type aiCLCEIARtsDisc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCEIARtsDisc_Type.__name__ = "Integer32"
_AiCLCEIARtsDisc_Object = MibTableColumn
aiCLCEIARtsDisc = _AiCLCEIARtsDisc_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 6),
    _AiCLCEIARtsDisc_Type()
)
aiCLCEIARtsDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCEIARtsDisc.setStatus("current")


class _AiCLCEIADtrDisc_Type(Integer32):
    """Custom type aiCLCEIADtrDisc based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCEIADtrDisc_Type.__name__ = "Integer32"
_AiCLCEIADtrDisc_Object = MibTableColumn
aiCLCEIADtrDisc = _AiCLCEIADtrDisc_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 7),
    _AiCLCEIADtrDisc_Type()
)
aiCLCEIADtrDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCEIADtrDisc.setStatus("current")


class _AiCLCEIARtsConn_Type(Integer32):
    """Custom type aiCLCEIARtsConn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCEIARtsConn_Type.__name__ = "Integer32"
_AiCLCEIARtsConn_Object = MibTableColumn
aiCLCEIARtsConn = _AiCLCEIARtsConn_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 8),
    _AiCLCEIARtsConn_Type()
)
aiCLCEIARtsConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCEIARtsConn.setStatus("current")


class _AiCLCEIADtrConn_Type(Integer32):
    """Custom type aiCLCEIADtrConn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCEIADtrConn_Type.__name__ = "Integer32"
_AiCLCEIADtrConn_Object = MibTableColumn
aiCLCEIADtrConn = _AiCLCEIADtrConn_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 9),
    _AiCLCEIADtrConn_Type()
)
aiCLCEIADtrConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCEIADtrConn.setStatus("current")


class _AiCLCEIARtsToggle_Type(Integer32):
    """Custom type aiCLCEIARtsToggle based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCEIARtsToggle_Type.__name__ = "Integer32"
_AiCLCEIARtsToggle_Object = MibTableColumn
aiCLCEIARtsToggle = _AiCLCEIARtsToggle_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 10),
    _AiCLCEIARtsToggle_Type()
)
aiCLCEIARtsToggle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCEIARtsToggle.setStatus("current")


class _AiCLCEIADtrToggle_Type(Integer32):
    """Custom type aiCLCEIADtrToggle based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AiCLCEIADtrToggle_Type.__name__ = "Integer32"
_AiCLCEIADtrToggle_Object = MibTableColumn
aiCLCEIADtrToggle = _AiCLCEIADtrToggle_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 6, 1, 11),
    _AiCLCEIADtrToggle_Type()
)
aiCLCEIADtrToggle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiCLCEIADtrToggle.setStatus("current")
_AiCLCAutoIDTable_Object = MibTable
aiCLCAutoIDTable = _AiCLCAutoIDTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7)
)
if mibBuilder.loadTexts:
    aiCLCAutoIDTable.setStatus("current")
_AiCLCAutoIDTableEntry_Object = MibTableRow
aiCLCAutoIDTableEntry = _AiCLCAutoIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7, 1)
)
aiCLCAutoIDTableEntry.setIndexNames(
    (0, "AI198CLC-MIB", "aiCLCAIDIndex"),
)
if mibBuilder.loadTexts:
    aiCLCAutoIDTableEntry.setStatus("current")


class _AiCLCAIDIndex_Type(Integer32):
    """Custom type aiCLCAIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AiCLCAIDIndex_Type.__name__ = "Integer32"
_AiCLCAIDIndex_Object = MibTableColumn
aiCLCAIDIndex = _AiCLCAIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7, 1, 1),
    _AiCLCAIDIndex_Type()
)
aiCLCAIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAIDIndex.setStatus("current")


class _AiCLCAIDPort_Type(Integer32):
    """Custom type aiCLCAIDPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AiCLCAIDPort_Type.__name__ = "Integer32"
_AiCLCAIDPort_Object = MibTableColumn
aiCLCAIDPort = _AiCLCAIDPort_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7, 1, 2),
    _AiCLCAIDPort_Type()
)
aiCLCAIDPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAIDPort.setStatus("current")
_AiCLCAIDProduct_Type = DisplayString
_AiCLCAIDProduct_Object = MibTableColumn
aiCLCAIDProduct = _AiCLCAIDProduct_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7, 1, 3),
    _AiCLCAIDProduct_Type()
)
aiCLCAIDProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAIDProduct.setStatus("current")
_AiCLCAIDSerialNumber_Type = DisplayString
_AiCLCAIDSerialNumber_Object = MibTableColumn
aiCLCAIDSerialNumber = _AiCLCAIDSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7, 1, 4),
    _AiCLCAIDSerialNumber_Type()
)
aiCLCAIDSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAIDSerialNumber.setStatus("current")
_AiCLCAIDManufDate_Type = DisplayString
_AiCLCAIDManufDate_Object = MibTableColumn
aiCLCAIDManufDate = _AiCLCAIDManufDate_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7, 1, 5),
    _AiCLCAIDManufDate_Type()
)
aiCLCAIDManufDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAIDManufDate.setStatus("current")
_AiCLCAIDMACAdrs_Type = DisplayString
_AiCLCAIDMACAdrs_Object = MibTableColumn
aiCLCAIDMACAdrs = _AiCLCAIDMACAdrs_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 7, 1, 6),
    _AiCLCAIDMACAdrs_Type()
)
aiCLCAIDMACAdrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAIDMACAdrs.setStatus("current")
_AiCLCAI2524LinkTable_Object = MibTable
aiCLCAI2524LinkTable = _AiCLCAI2524LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 8)
)
if mibBuilder.loadTexts:
    aiCLCAI2524LinkTable.setStatus("current")
_AiCLCAI2524LinkTableEntry_Object = MibTableRow
aiCLCAI2524LinkTableEntry = _AiCLCAI2524LinkTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 8, 1)
)
aiCLCAI2524LinkTableEntry.setIndexNames(
    (0, "AI198CLC-MIB", "aiCLCAI2524Port"),
)
if mibBuilder.loadTexts:
    aiCLCAI2524LinkTableEntry.setStatus("current")


class _AiCLCAI2524Port_Type(Integer32):
    """Custom type aiCLCAI2524Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AiCLCAI2524Port_Type.__name__ = "Integer32"
_AiCLCAI2524Port_Object = MibTableColumn
aiCLCAI2524Port = _AiCLCAI2524Port_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 8, 1, 1),
    _AiCLCAI2524Port_Type()
)
aiCLCAI2524Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAI2524Port.setStatus("current")


class _AiCLCAI2524LinkStatus_Type(Integer32):
    """Custom type aiCLCAI2524LinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AiCLCAI2524LinkStatus_Type.__name__ = "Integer32"
_AiCLCAI2524LinkStatus_Object = MibTableColumn
aiCLCAI2524LinkStatus = _AiCLCAI2524LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 539, 9, 8, 1, 2),
    _AiCLCAI2524LinkStatus_Type()
)
aiCLCAI2524LinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiCLCAI2524LinkStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AI198CLC-MIB",
    **{"aii": aii,
       "aiSystemOID": aiSystemOID,
       "ai198": ai198,
       "ai198Ver1": ai198Ver1,
       "ai198Ver10": ai198Ver10,
       "ai198Ver102": ai198Ver102,
       "ai198Ver103": ai198Ver103,
       "ai198Ver104": ai198Ver104,
       "ai198Ver12": ai198Ver12,
       "ai198Ver120": ai198Ver120,
       "ai198Ver13": ai198Ver13,
       "ai198Ver130": ai198Ver130,
       "aiCLC": aiCLC,
       "aiCLCSystem": aiCLCSystem,
       "aiCLCBox1DensAdmin": aiCLCBox1DensAdmin,
       "aiCLCBox2DensAdmin": aiCLCBox2DensAdmin,
       "aiCLCBox3DensAdmin": aiCLCBox3DensAdmin,
       "aiCLCBox4DensAdmin": aiCLCBox4DensAdmin,
       "aiCLCBox5DensAdmin": aiCLCBox5DensAdmin,
       "aiCLCBox6DensAdmin": aiCLCBox6DensAdmin,
       "aiCLCBox7DensAdmin": aiCLCBox7DensAdmin,
       "aiCLCBox8DensAdmin": aiCLCBox8DensAdmin,
       "aiCLCNodeName": aiCLCNodeName,
       "aiCLCLogPortEnable": aiCLCLogPortEnable,
       "aiCLCAlmLogPort": aiCLCAlmLogPort,
       "aiCLCActLogLvl": aiCLCActLogLvl,
       "aiCLCMinorAlmMin": aiCLCMinorAlmMin,
       "aiCLCMinorAlmMax": aiCLCMinorAlmMax,
       "aiCLCMajorAlmMin": aiCLCMajorAlmMin,
       "aiCLCMajorAlmMax": aiCLCMajorAlmMax,
       "aiCLCCraftLogEcho": aiCLCCraftLogEcho,
       "aiCLCCaamlRoute": aiCLCCaamlRoute,
       "aiCLCCaamlIdleTmr": aiCLCCaamlIdleTmr,
       "aiCLCCaamlRetryTmr": aiCLCCaamlRetryTmr,
       "aiCLCConnInfo": aiCLCConnInfo,
       "aiCLCLongBrkLen": aiCLCLongBrkLen,
       "aiCLCDestMenu": aiCLCDestMenu,
       "aiCLCDownSpd": aiCLCDownSpd,
       "aiCLCFaultSwitch": aiCLCFaultSwitch,
       "aiCLCDestMenuFmt": aiCLCDestMenuFmt,
       "aiCLCAutoCLCUpdate": aiCLCAutoCLCUpdate,
       "aiCLCAlarmLvl": aiCLCAlarmLvl,
       "aiCLCTimeDate": aiCLCTimeDate,
       "aiCLCRstTimeDate": aiCLCRstTimeDate,
       "aiCLCHoldConn": aiCLCHoldConn,
       "aiCLCNumPorts": aiCLCNumPorts,
       "aiCLCQueuedPorts": aiCLCQueuedPorts,
       "aiCLCEEPromFaults": aiCLCEEPromFaults,
       "aiCLCFreeEE": aiCLCFreeEE,
       "aiCLCBuffers": aiCLCBuffers,
       "aiCLCFreeBuffers": aiCLCFreeBuffers,
       "aiCLCBufAllocErr": aiCLCBufAllocErr,
       "aiCLCBufAlign": aiCLCBufAlign,
       "aiCLCCpuXacts": aiCLCCpuXacts,
       "aiCLCSLCXacts": aiCLCSLCXacts,
       "aiCLCConnectionsPlaced": aiCLCConnectionsPlaced,
       "aiCLCTxTail": aiCLCTxTail,
       "aiCLCEECRC": aiCLCEECRC,
       "aiCLCVersion": aiCLCVersion,
       "aiCLCBackupCLC": aiCLCBackupCLC,
       "aiCLCCpu": aiCLCCpu,
       "aiCLCCpyConfig": aiCLCCpyConfig,
       "aiCLCDLWinVerbose": aiCLCDLWinVerbose,
       "aiCLCDLWinIn": aiCLCDLWinIn,
       "aiCLCDLWinOut": aiCLCDLWinOut,
       "aiCLCDLWinUni": aiCLCDLWinUni,
       "aiCLCDLMsgAll": aiCLCDLMsgAll,
       "aiCLCDLNoBody": aiCLCDLNoBody,
       "aiCLCDLAlias": aiCLCDLAlias,
       "aiCLCDebugVal": aiCLCDebugVal,
       "aiCLCSwitchRestart": aiCLCSwitchRestart,
       "aiCLCInitStrings": aiCLCInitStrings,
       "aiCLCCopyFlash": aiCLCCopyFlash,
       "aiCLCCopyFlashToSLC": aiCLCCopyFlashToSLC,
       "aiCLCReadCommunity": aiCLCReadCommunity,
       "aiCLCWriteCommunity": aiCLCWriteCommunity,
       "aiCLCIPAdrs": aiCLCIPAdrs,
       "aiCLCRouterIPAdrs": aiCLCRouterIPAdrs,
       "aiCLCSubnetIPAdrs": aiCLCSubnetIPAdrs,
       "aiCLCTrapTable": aiCLCTrapTable,
       "aiCLCTrapTableEntry": aiCLCTrapTableEntry,
       "aiCLCTrapIPAdrs": aiCLCTrapIPAdrs,
       "aiCLCTrapRowStatus": aiCLCTrapRowStatus,
       "aiCLCLastTrapMsgText": aiCLCLastTrapMsgText,
       "aiCLCLastTrapMsgNum": aiCLCLastTrapMsgNum,
       "aiCLCCrashMsgText": aiCLCCrashMsgText,
       "aiCLCNumEventsSinceLastTrap": aiCLCNumEventsSinceLastTrap,
       "aiCLCTrapTimer": aiCLCTrapTimer,
       "aiCLCAsyncTrap": aiCLCAsyncTrap,
       "aiCLCTelnetServerPort": aiCLCTelnetServerPort,
       "aiCLCColdStartTrapDelay": aiCLCColdStartTrapDelay,
       "aiCLCFtpCtrlPort": aiCLCFtpCtrlPort,
       "aiCLCBackupCLCHealth": aiCLCBackupCLCHealth,
       "aiCLCBanner": aiCLCBanner,
       "aiCLCTimeZone": aiCLCTimeZone,
       "aiCLCDaylightSavings": aiCLCDaylightSavings,
       "aiCLCSNTP": aiCLCSNTP,
       "aiCLCSNTPPrimaryServer": aiCLCSNTPPrimaryServer,
       "aiCLCSNTPSecondaryServer": aiCLCSNTPSecondaryServer,
       "aiCLCSNTPPollInterval": aiCLCSNTPPollInterval,
       "aiCLCRadiusEnabled": aiCLCRadiusEnabled,
       "aiCLCRadiusAddr1": aiCLCRadiusAddr1,
       "aiCLCRadiusPort1": aiCLCRadiusPort1,
       "aiCLCRadiusSecret1": aiCLCRadiusSecret1,
       "aiCLCRadiusAddr2": aiCLCRadiusAddr2,
       "aiCLCRadiusPort2": aiCLCRadiusPort2,
       "aiCLCRadiusSecret2": aiCLCRadiusSecret2,
       "aiCLCTrapInterval": aiCLCTrapInterval,
       "aiCLCTacacsEnabled": aiCLCTacacsEnabled,
       "aiCLCTacacsAddr1": aiCLCTacacsAddr1,
       "aiCLCTacacsPort1": aiCLCTacacsPort1,
       "aiCLCTacacsSecret1": aiCLCTacacsSecret1,
       "aiCLCTacacsAddr2": aiCLCTacacsAddr2,
       "aiCLCTacacsPort2": aiCLCTacacsPort2,
       "aiCLCTacacsSecret2": aiCLCTacacsSecret2,
       "aiCLCCardTable": aiCLCCardTable,
       "aiCLCCardTableEntry": aiCLCCardTableEntry,
       "aiCLCCTIndex": aiCLCCTIndex,
       "aiCLCCTAdminStatus": aiCLCCTAdminStatus,
       "aiCLCCTBasePort": aiCLCCTBasePort,
       "aiCLCCTHighPort": aiCLCCTHighPort,
       "aiCLCCTRdCommStr": aiCLCCTRdCommStr,
       "aiCLCCTWrCommStr": aiCLCCTWrCommStr,
       "aiCLCCTCardSnmpState": aiCLCCTCardSnmpState,
       "aiCLCCTCardType": aiCLCCTCardType,
       "aiCLCCTSlotExp": aiCLCCTSlotExp,
       "aiCLCCTIPAdrs": aiCLCCTIPAdrs,
       "aiCLCCTRtrIPAdrs": aiCLCCTRtrIPAdrs,
       "aiCLCCTSubnetMask": aiCLCCTSubnetMask,
       "aiCLCCTAutoIdIndex": aiCLCCTAutoIdIndex,
       "aiCLCCTSysOID": aiCLCCTSysOID,
       "aiCLCCTRealCardType": aiCLCCTRealCardType,
       "aiCLCCTIPRange": aiCLCCTIPRange,
       "aiCLCCTTelnetPort": aiCLCCTTelnetPort,
       "aiCLCCTCardReset": aiCLCCTCardReset,
       "aiCLCCTLastSequenceNumber": aiCLCCTLastSequenceNumber,
       "aiCLCCTRtr2IPAdrs": aiCLCCTRtr2IPAdrs,
       "aiCLCPortTable": aiCLCPortTable,
       "aiCLCPortTableEntry": aiCLCPortTableEntry,
       "aiCLCPortNumber": aiCLCPortNumber,
       "aiCLCPortType": aiCLCPortType,
       "aiCLCPortDedicated": aiCLCPortDedicated,
       "aiCLCPortDestName": aiCLCPortDestName,
       "aiCLCPortEcho": aiCLCPortEcho,
       "aiCLCPortDestMenu": aiCLCPortDestMenu,
       "aiCLCPortQueue": aiCLCPortQueue,
       "aiCLCSLCProtocolCode": aiCLCSLCProtocolCode,
       "aiCLCPortState": aiCLCPortState,
       "aiCLCPortStatus": aiCLCPortStatus,
       "aiCLCPortAlm": aiCLCPortAlm,
       "aiCLCPortDesc": aiCLCPortDesc,
       "aiCLCPortReset": aiCLCPortReset,
       "aiCLCAliasTable": aiCLCAliasTable,
       "aiCLCAliasTableEntry": aiCLCAliasTableEntry,
       "aiCLCAliasIndex": aiCLCAliasIndex,
       "aiCLCAliasRowStatus": aiCLCAliasRowStatus,
       "aiCLCXlatType": aiCLCXlatType,
       "aiCLCAliasDestName": aiCLCAliasDestName,
       "aiCLCCalledAdrs": aiCLCCalledAdrs,
       "aiCLCAliasDestMenu": aiCLCAliasDestMenu,
       "aiCLCLinkNum": aiCLCLinkNum,
       "aiCLCCallerAdrs": aiCLCCallerAdrs,
       "aiCLCCallData": aiCLCCallData,
       "aiCLCApplicString": aiCLCApplicString,
       "aiCLCCalledProtoStr": aiCLCCalledProtoStr,
       "aiCLCCallerProtoStr": aiCLCCallerProtoStr,
       "aiCLCAlternRoute": aiCLCAlternRoute,
       "aiCLCAliasPosition": aiCLCAliasPosition,
       "aiCLCDestTable": aiCLCDestTable,
       "aiCLCDestTableEntry": aiCLCDestTableEntry,
       "aiCLCDestName": aiCLCDestName,
       "aiCLCDestRowStatus": aiCLCDestRowStatus,
       "aiCLCDestCallInit": aiCLCDestCallInit,
       "aiCLCDestDisc": aiCLCDestDisc,
       "aiCLCDestDispMenu": aiCLCDestDispMenu,
       "aiCLCDestBaud": aiCLCDestBaud,
       "aiCLCDestIsSwitch": aiCLCDestIsSwitch,
       "aiCLCDestTmrType": aiCLCDestTmrType,
       "aiCLCDestTmrVal": aiCLCDestTmrVal,
       "aiCLCDestTmrDelay": aiCLCDestTmrDelay,
       "aiCLCDestPswd": aiCLCDestPswd,
       "aiCLCDestQPswd": aiCLCDestQPswd,
       "aiCLCDestMenuMsg": aiCLCDestMenuMsg,
       "aiCLCDestConnMsg": aiCLCDestConnMsg,
       "aiCLCDestDiscMsg": aiCLCDestDiscMsg,
       "aiCLCDestState": aiCLCDestState,
       "aiCLCDestNumPorts": aiCLCDestNumPorts,
       "aiCLCDestNumUsed": aiCLCDestNumUsed,
       "aiCLCDestNumFree": aiCLCDestNumFree,
       "aiCLCDestQHigh": aiCLCDestQHigh,
       "aiCLCDestPortList": aiCLCDestPortList,
       "aiCLCDestWaitForPort": aiCLCDestWaitForPort,
       "aiCLCAsyncTable": aiCLCAsyncTable,
       "aiCLCAsyncTableEntry": aiCLCAsyncTableEntry,
       "aiCLCAsyncifIndex": aiCLCAsyncifIndex,
       "aiCLCAsyncPort": aiCLCAsyncPort,
       "aiCLCAsyncAdminStatus": aiCLCAsyncAdminStatus,
       "aiCLCAsyncDiscType": aiCLCAsyncDiscType,
       "aiCLCEIASignals": aiCLCEIASignals,
       "aiCLCEIARtsDisc": aiCLCEIARtsDisc,
       "aiCLCEIADtrDisc": aiCLCEIADtrDisc,
       "aiCLCEIARtsConn": aiCLCEIARtsConn,
       "aiCLCEIADtrConn": aiCLCEIADtrConn,
       "aiCLCEIARtsToggle": aiCLCEIARtsToggle,
       "aiCLCEIADtrToggle": aiCLCEIADtrToggle,
       "aiCLCAutoIDTable": aiCLCAutoIDTable,
       "aiCLCAutoIDTableEntry": aiCLCAutoIDTableEntry,
       "aiCLCAIDIndex": aiCLCAIDIndex,
       "aiCLCAIDPort": aiCLCAIDPort,
       "aiCLCAIDProduct": aiCLCAIDProduct,
       "aiCLCAIDSerialNumber": aiCLCAIDSerialNumber,
       "aiCLCAIDManufDate": aiCLCAIDManufDate,
       "aiCLCAIDMACAdrs": aiCLCAIDMACAdrs,
       "aiCLCAI2524LinkTable": aiCLCAI2524LinkTable,
       "aiCLCAI2524LinkTableEntry": aiCLCAI2524LinkTableEntry,
       "aiCLCAI2524Port": aiCLCAI2524Port,
       "aiCLCAI2524LinkStatus": aiCLCAI2524LinkStatus}
)
