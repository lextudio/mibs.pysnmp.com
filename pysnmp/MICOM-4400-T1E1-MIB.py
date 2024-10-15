# SNMP MIB module (MICOM-4400-T1E1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-4400-T1E1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:36 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

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

_Micom_2t1e1_ObjectIdentity = ObjectIdentity
micom_2t1e1 = _Micom_2t1e1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22)
)
_T1e1_r2_configuration_ObjectIdentity = ObjectIdentity
t1e1_r2_configuration = _T1e1_r2_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1)
)
_Mcm4400t1e1LineCfgTable_Object = MibTable
mcm4400t1e1LineCfgTable = _Mcm4400t1e1LineCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 1)
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineCfgTable.setStatus("mandatory")
_Mcm4400t1e1LineCfgEntry_Object = MibTableRow
mcm4400t1e1LineCfgEntry = _Mcm4400t1e1LineCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 1, 1)
)
mcm4400t1e1LineCfgEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1LineCfgLineID"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineCfgEntry.setStatus("mandatory")


class _Mcm4400t1e1LineCfgLineID_Type(Integer32):
    """Custom type mcm4400t1e1LineCfgLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_Mcm4400t1e1LineCfgLineID_Type.__name__ = "Integer32"
_Mcm4400t1e1LineCfgLineID_Object = MibTableColumn
mcm4400t1e1LineCfgLineID = _Mcm4400t1e1LineCfgLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 1, 1, 1),
    _Mcm4400t1e1LineCfgLineID_Type()
)
mcm4400t1e1LineCfgLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineCfgLineID.setStatus("mandatory")


class _Mcm4400t1e1LineCfgProfileNum_Type(Integer32):
    """Custom type mcm4400t1e1LineCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Mcm4400t1e1LineCfgProfileNum_Type.__name__ = "Integer32"
_Mcm4400t1e1LineCfgProfileNum_Object = MibTableColumn
mcm4400t1e1LineCfgProfileNum = _Mcm4400t1e1LineCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 1, 1, 2),
    _Mcm4400t1e1LineCfgProfileNum_Type()
)
mcm4400t1e1LineCfgProfileNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1LineCfgProfileNum.setStatus("mandatory")
_Mcm4400t1e1ProfCfgTable_Object = MibTable
mcm4400t1e1ProfCfgTable = _Mcm4400t1e1ProfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2)
)
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgTable.setStatus("mandatory")
_Mcm4400t1e1ProfCfgEntry_Object = MibTableRow
mcm4400t1e1ProfCfgEntry = _Mcm4400t1e1ProfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1)
)
mcm4400t1e1ProfCfgEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1ProfCfgProfileNum"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgEntry.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgProfileNum_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Mcm4400t1e1ProfCfgProfileNum_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgProfileNum_Object = MibTableColumn
mcm4400t1e1ProfCfgProfileNum = _Mcm4400t1e1ProfCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 1),
    _Mcm4400t1e1ProfCfgProfileNum_Type()
)
mcm4400t1e1ProfCfgProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgProfileNum.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgT1FrameFmt_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgT1FrameFmt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extendedSuperFrame", 2),
          ("superFrame", 1))
    )


_Mcm4400t1e1ProfCfgT1FrameFmt_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgT1FrameFmt_Object = MibTableColumn
mcm4400t1e1ProfCfgT1FrameFmt = _Mcm4400t1e1ProfCfgT1FrameFmt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 2),
    _Mcm4400t1e1ProfCfgT1FrameFmt_Type()
)
mcm4400t1e1ProfCfgT1FrameFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgT1FrameFmt.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgT1LineCode_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgT1LineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 1),
          ("b8ZS", 2))
    )


_Mcm4400t1e1ProfCfgT1LineCode_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgT1LineCode_Object = MibTableColumn
mcm4400t1e1ProfCfgT1LineCode = _Mcm4400t1e1ProfCfgT1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 3),
    _Mcm4400t1e1ProfCfgT1LineCode_Type()
)
mcm4400t1e1ProfCfgT1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgT1LineCode.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgE1LineCode_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgE1LineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 1),
          ("hDB3", 2))
    )


_Mcm4400t1e1ProfCfgE1LineCode_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgE1LineCode_Object = MibTableColumn
mcm4400t1e1ProfCfgE1LineCode = _Mcm4400t1e1ProfCfgE1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 4),
    _Mcm4400t1e1ProfCfgE1LineCode_Type()
)
mcm4400t1e1ProfCfgE1LineCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgE1LineCode.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgIdleCode_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgIdleCode based on Integer32"""
    defaultHexValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Mcm4400t1e1ProfCfgIdleCode_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgIdleCode_Object = MibTableColumn
mcm4400t1e1ProfCfgIdleCode = _Mcm4400t1e1ProfCfgIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 5),
    _Mcm4400t1e1ProfCfgIdleCode_Type()
)
mcm4400t1e1ProfCfgIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgIdleCode.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgT1LineBuildOut_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgT1LineBuildOut based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("externalLBO", 5),
          ("greaterThan665Feet", 6),
          ("lessThan110Feet", 1),
          ("lessThan220Feet", 2),
          ("lessThan330Feet", 3),
          ("lessThan440Feet", 4),
          ("lessThan550Feet", 7),
          ("lessThan660Feet", 8))
    )


_Mcm4400t1e1ProfCfgT1LineBuildOut_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgT1LineBuildOut_Object = MibTableColumn
mcm4400t1e1ProfCfgT1LineBuildOut = _Mcm4400t1e1ProfCfgT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 6),
    _Mcm4400t1e1ProfCfgT1LineBuildOut_Type()
)
mcm4400t1e1ProfCfgT1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgT1LineBuildOut.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgT1Loopback_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgT1Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Mcm4400t1e1ProfCfgT1Loopback_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgT1Loopback_Object = MibTableColumn
mcm4400t1e1ProfCfgT1Loopback = _Mcm4400t1e1ProfCfgT1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 7),
    _Mcm4400t1e1ProfCfgT1Loopback_Type()
)
mcm4400t1e1ProfCfgT1Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgT1Loopback.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgE1CRC4_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgE1CRC4 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Mcm4400t1e1ProfCfgE1CRC4_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgE1CRC4_Object = MibTableColumn
mcm4400t1e1ProfCfgE1CRC4 = _Mcm4400t1e1ProfCfgE1CRC4_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 8),
    _Mcm4400t1e1ProfCfgE1CRC4_Type()
)
mcm4400t1e1ProfCfgE1CRC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgE1CRC4.setStatus("mandatory")


class _Mcm4400t1e1ProfCfgE1TS16Conn_Type(Integer32):
    """Custom type mcm4400t1e1ProfCfgE1TS16Conn based on Integer32"""
    defaultValue = 1

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
        *(("bypass", 3),
          ("idle", 2),
          ("toCAS", 1),
          ("toDataPort1", 4),
          ("toDataPort2", 5))
    )


_Mcm4400t1e1ProfCfgE1TS16Conn_Type.__name__ = "Integer32"
_Mcm4400t1e1ProfCfgE1TS16Conn_Object = MibTableColumn
mcm4400t1e1ProfCfgE1TS16Conn = _Mcm4400t1e1ProfCfgE1TS16Conn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 2, 1, 9),
    _Mcm4400t1e1ProfCfgE1TS16Conn_Type()
)
mcm4400t1e1ProfCfgE1TS16Conn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1ProfCfgE1TS16Conn.setStatus("mandatory")
_Mcm4400t1e1DS0ChConnTable_Object = MibTable
mcm4400t1e1DS0ChConnTable = _Mcm4400t1e1DS0ChConnTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 3)
)
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChConnTable.setStatus("mandatory")
_Mcm4400t1e1DS0ChConnEntry_Object = MibTableRow
mcm4400t1e1DS0ChConnEntry = _Mcm4400t1e1DS0ChConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 3, 1)
)
mcm4400t1e1DS0ChConnEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DS0ChConnLineID"),
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DS0ChConnDS0Index"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChConnEntry.setStatus("mandatory")


class _Mcm4400t1e1DS0ChConnLineID_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChConnLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_Mcm4400t1e1DS0ChConnLineID_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChConnLineID_Object = MibTableColumn
mcm4400t1e1DS0ChConnLineID = _Mcm4400t1e1DS0ChConnLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 3, 1, 1),
    _Mcm4400t1e1DS0ChConnLineID_Type()
)
mcm4400t1e1DS0ChConnLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChConnLineID.setStatus("mandatory")


class _Mcm4400t1e1DS0ChConnDS0Index_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChConnDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Mcm4400t1e1DS0ChConnDS0Index_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChConnDS0Index_Object = MibTableColumn
mcm4400t1e1DS0ChConnDS0Index = _Mcm4400t1e1DS0ChConnDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 3, 1, 2),
    _Mcm4400t1e1DS0ChConnDS0Index_Type()
)
mcm4400t1e1DS0ChConnDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChConnDS0Index.setStatus("mandatory")


class _Mcm4400t1e1DS0ChConnState_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChConnState based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("bypassData", 3),
          ("bypassVoice", 2),
          ("idle", 1),
          ("toDVMChannelB1", 8),
          ("toDVMChannelB2", 9),
          ("toDVMChannelB3", 10),
          ("toDVMChannelB4", 11),
          ("toDVMChannelB5", 12),
          ("toDVMChannelB6", 13),
          ("toDVMChannelC1", 14),
          ("toDVMChannelC10", 23),
          ("toDVMChannelC11", 24),
          ("toDVMChannelC12", 25),
          ("toDVMChannelC2", 15),
          ("toDVMChannelC3", 16),
          ("toDVMChannelC4", 17),
          ("toDVMChannelC5", 18),
          ("toDVMChannelC6", 19),
          ("toDVMChannelC7", 20),
          ("toDVMChannelC8", 21),
          ("toDVMChannelC9", 22),
          ("toDVMChannelD1", 26),
          ("toDVMChannelD10", 35),
          ("toDVMChannelD11", 36),
          ("toDVMChannelD12", 37),
          ("toDVMChannelD2", 27),
          ("toDVMChannelD3", 28),
          ("toDVMChannelD4", 29),
          ("toDVMChannelD5", 30),
          ("toDVMChannelD6", 31),
          ("toDVMChannelD7", 32),
          ("toDVMChannelD8", 33),
          ("toDVMChannelD9", 34),
          ("toDataPort1", 6),
          ("toDataPort2", 7),
          ("toWANPort1", 4),
          ("toWANPort2", 5))
    )


_Mcm4400t1e1DS0ChConnState_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChConnState_Object = MibTableColumn
mcm4400t1e1DS0ChConnState = _Mcm4400t1e1DS0ChConnState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 3, 1, 3),
    _Mcm4400t1e1DS0ChConnState_Type()
)
mcm4400t1e1DS0ChConnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChConnState.setStatus("mandatory")
_Mcm4400t1e1DPCfgTable_Object = MibTable
mcm4400t1e1DPCfgTable = _Mcm4400t1e1DPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 4)
)
if mibBuilder.loadTexts:
    mcm4400t1e1DPCfgTable.setStatus("mandatory")
_Mcm4400t1e1DPCfgEntry_Object = MibTableRow
mcm4400t1e1DPCfgEntry = _Mcm4400t1e1DPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 4, 1)
)
mcm4400t1e1DPCfgEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DPCfgPortNum"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1DPCfgEntry.setStatus("mandatory")


class _Mcm4400t1e1DPCfgPortNum_Type(Integer32):
    """Custom type mcm4400t1e1DPCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2))
    )


_Mcm4400t1e1DPCfgPortNum_Type.__name__ = "Integer32"
_Mcm4400t1e1DPCfgPortNum_Object = MibTableColumn
mcm4400t1e1DPCfgPortNum = _Mcm4400t1e1DPCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 4, 1, 1),
    _Mcm4400t1e1DPCfgPortNum_Type()
)
mcm4400t1e1DPCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPCfgPortNum.setStatus("mandatory")


class _Mcm4400t1e1DPCfgDataRate_Type(Integer32):
    """Custom type mcm4400t1e1DPCfgDataRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56kbps", 2),
          ("rate64kbps", 1))
    )


_Mcm4400t1e1DPCfgDataRate_Type.__name__ = "Integer32"
_Mcm4400t1e1DPCfgDataRate_Object = MibTableColumn
mcm4400t1e1DPCfgDataRate = _Mcm4400t1e1DPCfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 4, 1, 2),
    _Mcm4400t1e1DPCfgDataRate_Type()
)
mcm4400t1e1DPCfgDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1DPCfgDataRate.setStatus("mandatory")


class _Mcm4400t1e1DPCfgClock_Type(Integer32):
    """Custom type mcm4400t1e1DPCfgClock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalClock", 1),
          ("tailCircuit", 2))
    )


_Mcm4400t1e1DPCfgClock_Type.__name__ = "Integer32"
_Mcm4400t1e1DPCfgClock_Object = MibTableColumn
mcm4400t1e1DPCfgClock = _Mcm4400t1e1DPCfgClock_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 4, 1, 3),
    _Mcm4400t1e1DPCfgClock_Type()
)
mcm4400t1e1DPCfgClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1DPCfgClock.setStatus("mandatory")


class _Mcm4400t1e1DPCfgDTRCntl_Type(Integer32):
    """Custom type mcm4400t1e1DPCfgDTRCntl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedOn", 2),
          ("normal", 1))
    )


_Mcm4400t1e1DPCfgDTRCntl_Type.__name__ = "Integer32"
_Mcm4400t1e1DPCfgDTRCntl_Object = MibTableColumn
mcm4400t1e1DPCfgDTRCntl = _Mcm4400t1e1DPCfgDTRCntl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 4, 1, 4),
    _Mcm4400t1e1DPCfgDTRCntl_Type()
)
mcm4400t1e1DPCfgDTRCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1DPCfgDTRCntl.setStatus("mandatory")


class _Mcm4400t1e1DPCfgRTSCntl_Type(Integer32):
    """Custom type mcm4400t1e1DPCfgRTSCntl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedOn", 2),
          ("normal", 1))
    )


_Mcm4400t1e1DPCfgRTSCntl_Type.__name__ = "Integer32"
_Mcm4400t1e1DPCfgRTSCntl_Object = MibTableColumn
mcm4400t1e1DPCfgRTSCntl = _Mcm4400t1e1DPCfgRTSCntl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 4, 1, 5),
    _Mcm4400t1e1DPCfgRTSCntl_Type()
)
mcm4400t1e1DPCfgRTSCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1DPCfgRTSCntl.setStatus("mandatory")


class _Mcm4400t1e1SysCfgClockSource_Type(Integer32):
    """Custom type mcm4400t1e1SysCfgClockSource based on Integer32"""
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
        *(("internal", 3),
          ("localLineExternal", 2),
          ("networkLineExternal", 1))
    )


_Mcm4400t1e1SysCfgClockSource_Type.__name__ = "Integer32"
_Mcm4400t1e1SysCfgClockSource_Object = MibScalar
mcm4400t1e1SysCfgClockSource = _Mcm4400t1e1SysCfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 5),
    _Mcm4400t1e1SysCfgClockSource_Type()
)
mcm4400t1e1SysCfgClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcm4400t1e1SysCfgClockSource.setStatus("mandatory")
_Nvm4400t1e1LineCfgTable_Object = MibTable
nvm4400t1e1LineCfgTable = _Nvm4400t1e1LineCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 6)
)
if mibBuilder.loadTexts:
    nvm4400t1e1LineCfgTable.setStatus("mandatory")
_Nvm4400t1e1LineCfgEntry_Object = MibTableRow
nvm4400t1e1LineCfgEntry = _Nvm4400t1e1LineCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 6, 1)
)
nvm4400t1e1LineCfgEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "nvm4400t1e1LineCfgLineID"),
)
if mibBuilder.loadTexts:
    nvm4400t1e1LineCfgEntry.setStatus("mandatory")


class _Nvm4400t1e1LineCfgLineID_Type(Integer32):
    """Custom type nvm4400t1e1LineCfgLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_Nvm4400t1e1LineCfgLineID_Type.__name__ = "Integer32"
_Nvm4400t1e1LineCfgLineID_Object = MibTableColumn
nvm4400t1e1LineCfgLineID = _Nvm4400t1e1LineCfgLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 6, 1, 1),
    _Nvm4400t1e1LineCfgLineID_Type()
)
nvm4400t1e1LineCfgLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1LineCfgLineID.setStatus("mandatory")


class _Nvm4400t1e1LineCfgProfileNum_Type(Integer32):
    """Custom type nvm4400t1e1LineCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Nvm4400t1e1LineCfgProfileNum_Type.__name__ = "Integer32"
_Nvm4400t1e1LineCfgProfileNum_Object = MibTableColumn
nvm4400t1e1LineCfgProfileNum = _Nvm4400t1e1LineCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 6, 1, 2),
    _Nvm4400t1e1LineCfgProfileNum_Type()
)
nvm4400t1e1LineCfgProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1LineCfgProfileNum.setStatus("mandatory")
_Nvm4400t1e1ProfCfgTable_Object = MibTable
nvm4400t1e1ProfCfgTable = _Nvm4400t1e1ProfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7)
)
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgTable.setStatus("mandatory")
_Nvm4400t1e1ProfCfgEntry_Object = MibTableRow
nvm4400t1e1ProfCfgEntry = _Nvm4400t1e1ProfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1)
)
nvm4400t1e1ProfCfgEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "nvm4400t1e1ProfCfgProfileNum"),
)
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgEntry.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgProfileNum_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Nvm4400t1e1ProfCfgProfileNum_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgProfileNum_Object = MibTableColumn
nvm4400t1e1ProfCfgProfileNum = _Nvm4400t1e1ProfCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 1),
    _Nvm4400t1e1ProfCfgProfileNum_Type()
)
nvm4400t1e1ProfCfgProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgProfileNum.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgT1FrameFmt_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgT1FrameFmt based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extendedSuperFrame", 2),
          ("superFrame", 1))
    )


_Nvm4400t1e1ProfCfgT1FrameFmt_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgT1FrameFmt_Object = MibTableColumn
nvm4400t1e1ProfCfgT1FrameFmt = _Nvm4400t1e1ProfCfgT1FrameFmt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 2),
    _Nvm4400t1e1ProfCfgT1FrameFmt_Type()
)
nvm4400t1e1ProfCfgT1FrameFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgT1FrameFmt.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgT1LineCode_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgT1LineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 1),
          ("b8ZS", 2))
    )


_Nvm4400t1e1ProfCfgT1LineCode_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgT1LineCode_Object = MibTableColumn
nvm4400t1e1ProfCfgT1LineCode = _Nvm4400t1e1ProfCfgT1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 3),
    _Nvm4400t1e1ProfCfgT1LineCode_Type()
)
nvm4400t1e1ProfCfgT1LineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgT1LineCode.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgE1LineCode_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgE1LineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 1),
          ("hDB3", 2))
    )


_Nvm4400t1e1ProfCfgE1LineCode_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgE1LineCode_Object = MibTableColumn
nvm4400t1e1ProfCfgE1LineCode = _Nvm4400t1e1ProfCfgE1LineCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 4),
    _Nvm4400t1e1ProfCfgE1LineCode_Type()
)
nvm4400t1e1ProfCfgE1LineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgE1LineCode.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgIdleCode_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgIdleCode based on Integer32"""
    defaultHexValue = 127

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Nvm4400t1e1ProfCfgIdleCode_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgIdleCode_Object = MibTableColumn
nvm4400t1e1ProfCfgIdleCode = _Nvm4400t1e1ProfCfgIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 5),
    _Nvm4400t1e1ProfCfgIdleCode_Type()
)
nvm4400t1e1ProfCfgIdleCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgIdleCode.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgT1LineBuildOut_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgT1LineBuildOut based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("externalLBO", 5),
          ("greaterThan665Feet", 6),
          ("lessThan110Feet", 1),
          ("lessThan220Feet", 2),
          ("lessThan330Feet", 3),
          ("lessThan440Feet", 4),
          ("lessThan550Feet", 7),
          ("lessThan660Feet", 8))
    )


_Nvm4400t1e1ProfCfgT1LineBuildOut_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgT1LineBuildOut_Object = MibTableColumn
nvm4400t1e1ProfCfgT1LineBuildOut = _Nvm4400t1e1ProfCfgT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 6),
    _Nvm4400t1e1ProfCfgT1LineBuildOut_Type()
)
nvm4400t1e1ProfCfgT1LineBuildOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgT1LineBuildOut.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgT1Loopback_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgT1Loopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Nvm4400t1e1ProfCfgT1Loopback_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgT1Loopback_Object = MibTableColumn
nvm4400t1e1ProfCfgT1Loopback = _Nvm4400t1e1ProfCfgT1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 7),
    _Nvm4400t1e1ProfCfgT1Loopback_Type()
)
nvm4400t1e1ProfCfgT1Loopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgT1Loopback.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgE1CRC4_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgE1CRC4 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Nvm4400t1e1ProfCfgE1CRC4_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgE1CRC4_Object = MibTableColumn
nvm4400t1e1ProfCfgE1CRC4 = _Nvm4400t1e1ProfCfgE1CRC4_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 8),
    _Nvm4400t1e1ProfCfgE1CRC4_Type()
)
nvm4400t1e1ProfCfgE1CRC4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgE1CRC4.setStatus("mandatory")


class _Nvm4400t1e1ProfCfgE1TS16Conn_Type(Integer32):
    """Custom type nvm4400t1e1ProfCfgE1TS16Conn based on Integer32"""
    defaultValue = 1

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
        *(("bypass", 3),
          ("idle", 2),
          ("toCAS", 1),
          ("toDataPort1", 4),
          ("toDataPort2", 5))
    )


_Nvm4400t1e1ProfCfgE1TS16Conn_Type.__name__ = "Integer32"
_Nvm4400t1e1ProfCfgE1TS16Conn_Object = MibTableColumn
nvm4400t1e1ProfCfgE1TS16Conn = _Nvm4400t1e1ProfCfgE1TS16Conn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 7, 1, 9),
    _Nvm4400t1e1ProfCfgE1TS16Conn_Type()
)
nvm4400t1e1ProfCfgE1TS16Conn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1ProfCfgE1TS16Conn.setStatus("mandatory")
_Nvm4400t1e1DS0ChConnTable_Object = MibTable
nvm4400t1e1DS0ChConnTable = _Nvm4400t1e1DS0ChConnTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 8)
)
if mibBuilder.loadTexts:
    nvm4400t1e1DS0ChConnTable.setStatus("mandatory")
_Nvm4400t1e1DS0ChConnEntry_Object = MibTableRow
nvm4400t1e1DS0ChConnEntry = _Nvm4400t1e1DS0ChConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 8, 1)
)
nvm4400t1e1DS0ChConnEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "nvm4400t1e1DS0ChConnLineID"),
    (0, "MICOM-4400-T1E1-MIB", "nvm4400t1e1DS0ChConnDS0Index"),
)
if mibBuilder.loadTexts:
    nvm4400t1e1DS0ChConnEntry.setStatus("mandatory")


class _Nvm4400t1e1DS0ChConnLineID_Type(Integer32):
    """Custom type nvm4400t1e1DS0ChConnLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_Nvm4400t1e1DS0ChConnLineID_Type.__name__ = "Integer32"
_Nvm4400t1e1DS0ChConnLineID_Object = MibTableColumn
nvm4400t1e1DS0ChConnLineID = _Nvm4400t1e1DS0ChConnLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 8, 1, 1),
    _Nvm4400t1e1DS0ChConnLineID_Type()
)
nvm4400t1e1DS0ChConnLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DS0ChConnLineID.setStatus("mandatory")


class _Nvm4400t1e1DS0ChConnDS0Index_Type(Integer32):
    """Custom type nvm4400t1e1DS0ChConnDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Nvm4400t1e1DS0ChConnDS0Index_Type.__name__ = "Integer32"
_Nvm4400t1e1DS0ChConnDS0Index_Object = MibTableColumn
nvm4400t1e1DS0ChConnDS0Index = _Nvm4400t1e1DS0ChConnDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 8, 1, 2),
    _Nvm4400t1e1DS0ChConnDS0Index_Type()
)
nvm4400t1e1DS0ChConnDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DS0ChConnDS0Index.setStatus("mandatory")


class _Nvm4400t1e1DS0ChConnState_Type(Integer32):
    """Custom type nvm4400t1e1DS0ChConnState based on Integer32"""
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("bypassData", 3),
          ("bypassVoice", 2),
          ("idle", 1),
          ("toDVMChannelB1", 8),
          ("toDVMChannelB2", 9),
          ("toDVMChannelB3", 10),
          ("toDVMChannelB4", 11),
          ("toDVMChannelB5", 12),
          ("toDVMChannelB6", 13),
          ("toDVMChannelC1", 14),
          ("toDVMChannelC10", 23),
          ("toDVMChannelC11", 24),
          ("toDVMChannelC12", 25),
          ("toDVMChannelC2", 15),
          ("toDVMChannelC3", 16),
          ("toDVMChannelC4", 17),
          ("toDVMChannelC5", 18),
          ("toDVMChannelC6", 19),
          ("toDVMChannelC7", 20),
          ("toDVMChannelC8", 21),
          ("toDVMChannelC9", 22),
          ("toDVMChannelD1", 26),
          ("toDVMChannelD10", 35),
          ("toDVMChannelD11", 36),
          ("toDVMChannelD12", 37),
          ("toDVMChannelD2", 27),
          ("toDVMChannelD3", 28),
          ("toDVMChannelD4", 29),
          ("toDVMChannelD5", 30),
          ("toDVMChannelD6", 31),
          ("toDVMChannelD7", 32),
          ("toDVMChannelD8", 33),
          ("toDVMChannelD9", 34),
          ("toDataPort1", 6),
          ("toDataPort2", 7),
          ("toWANPort1", 4),
          ("toWANPort2", 5))
    )


_Nvm4400t1e1DS0ChConnState_Type.__name__ = "Integer32"
_Nvm4400t1e1DS0ChConnState_Object = MibTableColumn
nvm4400t1e1DS0ChConnState = _Nvm4400t1e1DS0ChConnState_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 8, 1, 3),
    _Nvm4400t1e1DS0ChConnState_Type()
)
nvm4400t1e1DS0ChConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DS0ChConnState.setStatus("mandatory")
_Nvm4400t1e1DPCfgTable_Object = MibTable
nvm4400t1e1DPCfgTable = _Nvm4400t1e1DPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 9)
)
if mibBuilder.loadTexts:
    nvm4400t1e1DPCfgTable.setStatus("mandatory")
_Nvm4400t1e1DPCfgEntry_Object = MibTableRow
nvm4400t1e1DPCfgEntry = _Nvm4400t1e1DPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 9, 1)
)
nvm4400t1e1DPCfgEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "nvm4400t1e1DPCfgPortNum"),
)
if mibBuilder.loadTexts:
    nvm4400t1e1DPCfgEntry.setStatus("mandatory")


class _Nvm4400t1e1DPCfgPortNum_Type(Integer32):
    """Custom type nvm4400t1e1DPCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2))
    )


_Nvm4400t1e1DPCfgPortNum_Type.__name__ = "Integer32"
_Nvm4400t1e1DPCfgPortNum_Object = MibTableColumn
nvm4400t1e1DPCfgPortNum = _Nvm4400t1e1DPCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 9, 1, 1),
    _Nvm4400t1e1DPCfgPortNum_Type()
)
nvm4400t1e1DPCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DPCfgPortNum.setStatus("mandatory")


class _Nvm4400t1e1DPCfgDataRate_Type(Integer32):
    """Custom type nvm4400t1e1DPCfgDataRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate56kbps", 2),
          ("rate64kbps", 1))
    )


_Nvm4400t1e1DPCfgDataRate_Type.__name__ = "Integer32"
_Nvm4400t1e1DPCfgDataRate_Object = MibTableColumn
nvm4400t1e1DPCfgDataRate = _Nvm4400t1e1DPCfgDataRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 9, 1, 2),
    _Nvm4400t1e1DPCfgDataRate_Type()
)
nvm4400t1e1DPCfgDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DPCfgDataRate.setStatus("mandatory")


class _Nvm4400t1e1DPCfgClock_Type(Integer32):
    """Custom type nvm4400t1e1DPCfgClock based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalClock", 1),
          ("tailCircuit", 2))
    )


_Nvm4400t1e1DPCfgClock_Type.__name__ = "Integer32"
_Nvm4400t1e1DPCfgClock_Object = MibTableColumn
nvm4400t1e1DPCfgClock = _Nvm4400t1e1DPCfgClock_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 9, 1, 3),
    _Nvm4400t1e1DPCfgClock_Type()
)
nvm4400t1e1DPCfgClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DPCfgClock.setStatus("mandatory")


class _Nvm4400t1e1DPCfgDTRCntl_Type(Integer32):
    """Custom type nvm4400t1e1DPCfgDTRCntl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedOn", 2),
          ("normal", 1))
    )


_Nvm4400t1e1DPCfgDTRCntl_Type.__name__ = "Integer32"
_Nvm4400t1e1DPCfgDTRCntl_Object = MibTableColumn
nvm4400t1e1DPCfgDTRCntl = _Nvm4400t1e1DPCfgDTRCntl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 9, 1, 4),
    _Nvm4400t1e1DPCfgDTRCntl_Type()
)
nvm4400t1e1DPCfgDTRCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DPCfgDTRCntl.setStatus("mandatory")


class _Nvm4400t1e1DPCfgRTSCntl_Type(Integer32):
    """Custom type nvm4400t1e1DPCfgRTSCntl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedOn", 2),
          ("normal", 1))
    )


_Nvm4400t1e1DPCfgRTSCntl_Type.__name__ = "Integer32"
_Nvm4400t1e1DPCfgRTSCntl_Object = MibTableColumn
nvm4400t1e1DPCfgRTSCntl = _Nvm4400t1e1DPCfgRTSCntl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 9, 1, 5),
    _Nvm4400t1e1DPCfgRTSCntl_Type()
)
nvm4400t1e1DPCfgRTSCntl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1DPCfgRTSCntl.setStatus("mandatory")


class _Nvm4400t1e1SysCfgClockSource_Type(Integer32):
    """Custom type nvm4400t1e1SysCfgClockSource based on Integer32"""
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
        *(("internal", 3),
          ("localLineExternal", 2),
          ("networkLineExternal", 1))
    )


_Nvm4400t1e1SysCfgClockSource_Type.__name__ = "Integer32"
_Nvm4400t1e1SysCfgClockSource_Object = MibScalar
nvm4400t1e1SysCfgClockSource = _Nvm4400t1e1SysCfgClockSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 1, 10),
    _Nvm4400t1e1SysCfgClockSource_Type()
)
nvm4400t1e1SysCfgClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvm4400t1e1SysCfgClockSource.setStatus("mandatory")
_T1e1_r2_control_ObjectIdentity = ObjectIdentity
t1e1_r2_control = _T1e1_r2_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2)
)
_Mcm4400t1e1DS0ChTestCmdTable_Object = MibTable
mcm4400t1e1DS0ChTestCmdTable = _Mcm4400t1e1DS0ChTestCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 1)
)
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChTestCmdTable.setStatus("mandatory")
_Mcm4400t1e1DS0ChTestCmdEntry_Object = MibTableRow
mcm4400t1e1DS0ChTestCmdEntry = _Mcm4400t1e1DS0ChTestCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 1, 1)
)
mcm4400t1e1DS0ChTestCmdEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DS0ChTestCmdLineID"),
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DS0ChTestCmdDS0Index"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChTestCmdEntry.setStatus("mandatory")


class _Mcm4400t1e1DS0ChTestCmdLineID_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChTestCmdLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_Mcm4400t1e1DS0ChTestCmdLineID_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChTestCmdLineID_Object = MibTableColumn
mcm4400t1e1DS0ChTestCmdLineID = _Mcm4400t1e1DS0ChTestCmdLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 1, 1, 1),
    _Mcm4400t1e1DS0ChTestCmdLineID_Type()
)
mcm4400t1e1DS0ChTestCmdLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChTestCmdLineID.setStatus("mandatory")


class _Mcm4400t1e1DS0ChTestCmdDS0Index_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChTestCmdDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Mcm4400t1e1DS0ChTestCmdDS0Index_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChTestCmdDS0Index_Object = MibTableColumn
mcm4400t1e1DS0ChTestCmdDS0Index = _Mcm4400t1e1DS0ChTestCmdDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 1, 1, 2),
    _Mcm4400t1e1DS0ChTestCmdDS0Index_Type()
)
mcm4400t1e1DS0ChTestCmdDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChTestCmdDS0Index.setStatus("mandatory")


class _Mcm4400t1e1DS0ChTestCmdTstPattern_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChTestCmdTstPattern based on Integer32"""
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
        *(("fixed-E1Only", 4),
          ("loop", 3),
          ("qrss", 1),
          ("tp511", 2))
    )


_Mcm4400t1e1DS0ChTestCmdTstPattern_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChTestCmdTstPattern_Object = MibTableColumn
mcm4400t1e1DS0ChTestCmdTstPattern = _Mcm4400t1e1DS0ChTestCmdTstPattern_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 1, 1, 3),
    _Mcm4400t1e1DS0ChTestCmdTstPattern_Type()
)
mcm4400t1e1DS0ChTestCmdTstPattern.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChTestCmdTstPattern.setStatus("mandatory")
_Mcm4400t1e1LineTestCmdTable_Object = MibTable
mcm4400t1e1LineTestCmdTable = _Mcm4400t1e1LineTestCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 2)
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineTestCmdTable.setStatus("mandatory")
_Mcm4400t1e1LineTestCmdEntry_Object = MibTableRow
mcm4400t1e1LineTestCmdEntry = _Mcm4400t1e1LineTestCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 2, 1)
)
mcm4400t1e1LineTestCmdEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1LineTestCmdLineID"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineTestCmdEntry.setStatus("mandatory")


class _Mcm4400t1e1LineTestCmdLineID_Type(Integer32):
    """Custom type mcm4400t1e1LineTestCmdLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_Mcm4400t1e1LineTestCmdLineID_Type.__name__ = "Integer32"
_Mcm4400t1e1LineTestCmdLineID_Object = MibTableColumn
mcm4400t1e1LineTestCmdLineID = _Mcm4400t1e1LineTestCmdLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 2, 1, 1),
    _Mcm4400t1e1LineTestCmdLineID_Type()
)
mcm4400t1e1LineTestCmdLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineTestCmdLineID.setStatus("mandatory")


class _Mcm4400t1e1LineTestCmdTstPattern_Type(Integer32):
    """Custom type mcm4400t1e1LineTestCmdTstPattern based on Integer32"""
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
        *(("externalDigitalLoopback", 2),
          ("externalLineLoopback", 1),
          ("internalDigitalLoopback", 4),
          ("internalLineLoopback", 3))
    )


_Mcm4400t1e1LineTestCmdTstPattern_Type.__name__ = "Integer32"
_Mcm4400t1e1LineTestCmdTstPattern_Object = MibTableColumn
mcm4400t1e1LineTestCmdTstPattern = _Mcm4400t1e1LineTestCmdTstPattern_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 2, 1, 2),
    _Mcm4400t1e1LineTestCmdTstPattern_Type()
)
mcm4400t1e1LineTestCmdTstPattern.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineTestCmdTstPattern.setStatus("mandatory")
_Mcm4400t1e1DPTestCmdTable_Object = MibTable
mcm4400t1e1DPTestCmdTable = _Mcm4400t1e1DPTestCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 3)
)
if mibBuilder.loadTexts:
    mcm4400t1e1DPTestCmdTable.setStatus("mandatory")
_Mcm4400t1e1DPTestCmdEntry_Object = MibTableRow
mcm4400t1e1DPTestCmdEntry = _Mcm4400t1e1DPTestCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 3, 1)
)
mcm4400t1e1DPTestCmdEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DPTestCmdPortNum"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1DPTestCmdEntry.setStatus("mandatory")


class _Mcm4400t1e1DPTestCmdPortNum_Type(Integer32):
    """Custom type mcm4400t1e1DPTestCmdPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dataPort1", 1),
          ("dataPort2", 2))
    )


_Mcm4400t1e1DPTestCmdPortNum_Type.__name__ = "Integer32"
_Mcm4400t1e1DPTestCmdPortNum_Object = MibTableColumn
mcm4400t1e1DPTestCmdPortNum = _Mcm4400t1e1DPTestCmdPortNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 3, 1, 1),
    _Mcm4400t1e1DPTestCmdPortNum_Type()
)
mcm4400t1e1DPTestCmdPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPTestCmdPortNum.setStatus("mandatory")


class _Mcm4400t1e1DPTestCmdTstPattern_Type(Integer32):
    """Custom type mcm4400t1e1DPTestCmdTstPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalLoopback", 1),
          ("internalLoopback", 2))
    )


_Mcm4400t1e1DPTestCmdTstPattern_Type.__name__ = "Integer32"
_Mcm4400t1e1DPTestCmdTstPattern_Object = MibTableColumn
mcm4400t1e1DPTestCmdTstPattern = _Mcm4400t1e1DPTestCmdTstPattern_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 3, 1, 2),
    _Mcm4400t1e1DPTestCmdTstPattern_Type()
)
mcm4400t1e1DPTestCmdTstPattern.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPTestCmdTstPattern.setStatus("mandatory")


class _Mcm4400t1e1SysControlActionCmd_Type(Integer32):
    """Custom type mcm4400t1e1SysControlActionCmd based on Integer32"""
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
        *(("clearCounter", 3),
          ("download", 4),
          ("resetT1E1", 2),
          ("stopAllTests", 9),
          ("stopChannelTest", 5),
          ("stopLEDTest", 8),
          ("stopLineTest", 6),
          ("stopPortTest", 7),
          ("testLED", 1))
    )


_Mcm4400t1e1SysControlActionCmd_Type.__name__ = "Integer32"
_Mcm4400t1e1SysControlActionCmd_Object = MibScalar
mcm4400t1e1SysControlActionCmd = _Mcm4400t1e1SysControlActionCmd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 2, 4),
    _Mcm4400t1e1SysControlActionCmd_Type()
)
mcm4400t1e1SysControlActionCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysControlActionCmd.setStatus("mandatory")
_T1e1_r2_status_ObjectIdentity = ObjectIdentity
t1e1_r2_status = _T1e1_r2_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3)
)
_Mcm4400t1e1LineStatusTable_Object = MibTable
mcm4400t1e1LineStatusTable = _Mcm4400t1e1LineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1)
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusTable.setStatus("mandatory")
_Mcm4400t1e1LineStatusEntry_Object = MibTableRow
mcm4400t1e1LineStatusEntry = _Mcm4400t1e1LineStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1)
)
mcm4400t1e1LineStatusEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusEntry.setStatus("mandatory")


class _Mcm4400t1e1LineStatusLineIndex_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localLine", 1),
          ("networkLine", 2))
    )


_Mcm4400t1e1LineStatusLineIndex_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusLineIndex_Object = MibTableColumn
mcm4400t1e1LineStatusLineIndex = _Mcm4400t1e1LineStatusLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 1),
    _Mcm4400t1e1LineStatusLineIndex_Type()
)
mcm4400t1e1LineStatusLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusLineIndex.setStatus("mandatory")


class _Mcm4400t1e1LineStatusInterface_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_Mcm4400t1e1LineStatusInterface_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusInterface_Object = MibTableColumn
mcm4400t1e1LineStatusInterface = _Mcm4400t1e1LineStatusInterface_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 2),
    _Mcm4400t1e1LineStatusInterface_Type()
)
mcm4400t1e1LineStatusInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusInterface.setStatus("mandatory")


class _Mcm4400t1e1LineStatusImpedance_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusImpedance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line120ohm", 1),
          ("line75ohm", 2))
    )


_Mcm4400t1e1LineStatusImpedance_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusImpedance_Object = MibTableColumn
mcm4400t1e1LineStatusImpedance = _Mcm4400t1e1LineStatusImpedance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 3),
    _Mcm4400t1e1LineStatusImpedance_Type()
)
mcm4400t1e1LineStatusImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusImpedance.setStatus("mandatory")


class _Mcm4400t1e1LineStatusTestMode_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusTestMode based on Integer32"""
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
        *(("inChannelLoopback", 3),
          ("inChannelPatternTest", 4),
          ("inLineLoopback", 2),
          ("none", 1))
    )


_Mcm4400t1e1LineStatusTestMode_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusTestMode_Object = MibTableColumn
mcm4400t1e1LineStatusTestMode = _Mcm4400t1e1LineStatusTestMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 4),
    _Mcm4400t1e1LineStatusTestMode_Type()
)
mcm4400t1e1LineStatusTestMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusTestMode.setStatus("mandatory")


class _Mcm4400t1e1LineStatusTestingDS0Ch_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusTestingDS0Ch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Mcm4400t1e1LineStatusTestingDS0Ch_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusTestingDS0Ch_Object = MibTableColumn
mcm4400t1e1LineStatusTestingDS0Ch = _Mcm4400t1e1LineStatusTestingDS0Ch_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 5),
    _Mcm4400t1e1LineStatusTestingDS0Ch_Type()
)
mcm4400t1e1LineStatusTestingDS0Ch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusTestingDS0Ch.setStatus("mandatory")


class _Mcm4400t1e1LineStatusAISAlarm_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusAISAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusAISAlarm_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusAISAlarm_Object = MibTableColumn
mcm4400t1e1LineStatusAISAlarm = _Mcm4400t1e1LineStatusAISAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 6),
    _Mcm4400t1e1LineStatusAISAlarm_Type()
)
mcm4400t1e1LineStatusAISAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusAISAlarm.setStatus("mandatory")


class _Mcm4400t1e1LineStatusRedAlarm_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusRedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusRedAlarm_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusRedAlarm_Object = MibTableColumn
mcm4400t1e1LineStatusRedAlarm = _Mcm4400t1e1LineStatusRedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 7),
    _Mcm4400t1e1LineStatusRedAlarm_Type()
)
mcm4400t1e1LineStatusRedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusRedAlarm.setStatus("mandatory")


class _Mcm4400t1e1LineStatusYellowAlarm_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusYellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notApplicable", 3),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusYellowAlarm_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusYellowAlarm_Object = MibTableColumn
mcm4400t1e1LineStatusYellowAlarm = _Mcm4400t1e1LineStatusYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 8),
    _Mcm4400t1e1LineStatusYellowAlarm_Type()
)
mcm4400t1e1LineStatusYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusYellowAlarm.setStatus("mandatory")


class _Mcm4400t1e1LineStatusTS16AIS_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusTS16AIS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notApplicable", 3),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusTS16AIS_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusTS16AIS_Object = MibTableColumn
mcm4400t1e1LineStatusTS16AIS = _Mcm4400t1e1LineStatusTS16AIS_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 9),
    _Mcm4400t1e1LineStatusTS16AIS_Type()
)
mcm4400t1e1LineStatusTS16AIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusTS16AIS.setStatus("mandatory")


class _Mcm4400t1e1LineStatusOOSMFAlarm_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusOOSMFAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notApplicable", 3),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusOOSMFAlarm_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusOOSMFAlarm_Object = MibTableColumn
mcm4400t1e1LineStatusOOSMFAlarm = _Mcm4400t1e1LineStatusOOSMFAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 10),
    _Mcm4400t1e1LineStatusOOSMFAlarm_Type()
)
mcm4400t1e1LineStatusOOSMFAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusOOSMFAlarm.setStatus("mandatory")


class _Mcm4400t1e1LineStatusMFASAlarm_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusMFASAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notApplicable", 3),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusMFASAlarm_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusMFASAlarm_Object = MibTableColumn
mcm4400t1e1LineStatusMFASAlarm = _Mcm4400t1e1LineStatusMFASAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 11),
    _Mcm4400t1e1LineStatusMFASAlarm_Type()
)
mcm4400t1e1LineStatusMFASAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusMFASAlarm.setStatus("mandatory")


class _Mcm4400t1e1LineStatusFASAlarm_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusFASAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notApplicable", 3),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusFASAlarm_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusFASAlarm_Object = MibTableColumn
mcm4400t1e1LineStatusFASAlarm = _Mcm4400t1e1LineStatusFASAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 12),
    _Mcm4400t1e1LineStatusFASAlarm_Type()
)
mcm4400t1e1LineStatusFASAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusFASAlarm.setStatus("mandatory")


class _Mcm4400t1e1LineStatusOOCMFAlarm_Type(Integer32):
    """Custom type mcm4400t1e1LineStatusOOCMFAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("notApplicable", 3),
          ("yes", 2))
    )


_Mcm4400t1e1LineStatusOOCMFAlarm_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatusOOCMFAlarm_Object = MibTableColumn
mcm4400t1e1LineStatusOOCMFAlarm = _Mcm4400t1e1LineStatusOOCMFAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 1, 1, 13),
    _Mcm4400t1e1LineStatusOOCMFAlarm_Type()
)
mcm4400t1e1LineStatusOOCMFAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatusOOCMFAlarm.setStatus("mandatory")
_Mcm4400t1e1SysStatusGroup_ObjectIdentity = ObjectIdentity
mcm4400t1e1SysStatusGroup = _Mcm4400t1e1SysStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2)
)


class _Mcm4400t1e1SysStatusCardType_Type(Integer32):
    """Custom type mcm4400t1e1SysStatusCardType based on Integer32"""
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
        *(("e1DualLineAccessModule", 4),
          ("e1SingleLineAccessModule", 3),
          ("t1DualLineAccessModule", 2),
          ("t1SingleLineAccessModule", 1))
    )


_Mcm4400t1e1SysStatusCardType_Type.__name__ = "Integer32"
_Mcm4400t1e1SysStatusCardType_Object = MibScalar
mcm4400t1e1SysStatusCardType = _Mcm4400t1e1SysStatusCardType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2, 1),
    _Mcm4400t1e1SysStatusCardType_Type()
)
mcm4400t1e1SysStatusCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysStatusCardType.setStatus("mandatory")


class _Mcm4400t1e1SysStatusOperStatus_Type(Integer32):
    """Custom type mcm4400t1e1SysStatusOperStatus based on Integer32"""
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
        *(("aliveButNotReady", 2),
          ("dead", 1),
          ("downloadFail", 3),
          ("downloadInProgress", 4),
          ("normal", 5))
    )


_Mcm4400t1e1SysStatusOperStatus_Type.__name__ = "Integer32"
_Mcm4400t1e1SysStatusOperStatus_Object = MibScalar
mcm4400t1e1SysStatusOperStatus = _Mcm4400t1e1SysStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2, 2),
    _Mcm4400t1e1SysStatusOperStatus_Type()
)
mcm4400t1e1SysStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysStatusOperStatus.setStatus("mandatory")


class _Mcm4400t1e1SysStatusLEDTest_Type(Integer32):
    """Custom type mcm4400t1e1SysStatusLEDTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_Mcm4400t1e1SysStatusLEDTest_Type.__name__ = "Integer32"
_Mcm4400t1e1SysStatusLEDTest_Object = MibScalar
mcm4400t1e1SysStatusLEDTest = _Mcm4400t1e1SysStatusLEDTest_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2, 3),
    _Mcm4400t1e1SysStatusLEDTest_Type()
)
mcm4400t1e1SysStatusLEDTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysStatusLEDTest.setStatus("mandatory")


class _Mcm4400t1e1SysStatusSelfTestResults_Type(Integer32):
    """Custom type mcm4400t1e1SysStatusSelfTestResults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 2),
          ("testPassed", 1))
    )


_Mcm4400t1e1SysStatusSelfTestResults_Type.__name__ = "Integer32"
_Mcm4400t1e1SysStatusSelfTestResults_Object = MibScalar
mcm4400t1e1SysStatusSelfTestResults = _Mcm4400t1e1SysStatusSelfTestResults_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2, 4),
    _Mcm4400t1e1SysStatusSelfTestResults_Type()
)
mcm4400t1e1SysStatusSelfTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysStatusSelfTestResults.setStatus("mandatory")


class _Mcm4400t1e1SysStatusFlashEPROMSt_Type(Integer32):
    """Custom type mcm4400t1e1SysStatusFlashEPROMSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("erased", 2),
          ("invalidChecksum", 3),
          ("valid", 1))
    )


_Mcm4400t1e1SysStatusFlashEPROMSt_Type.__name__ = "Integer32"
_Mcm4400t1e1SysStatusFlashEPROMSt_Object = MibScalar
mcm4400t1e1SysStatusFlashEPROMSt = _Mcm4400t1e1SysStatusFlashEPROMSt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2, 5),
    _Mcm4400t1e1SysStatusFlashEPROMSt_Type()
)
mcm4400t1e1SysStatusFlashEPROMSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysStatusFlashEPROMSt.setStatus("mandatory")


class _Mcm4400t1e1SysStatusApplSwID_Type(DisplayString):
    """Custom type mcm4400t1e1SysStatusApplSwID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Mcm4400t1e1SysStatusApplSwID_Type.__name__ = "DisplayString"
_Mcm4400t1e1SysStatusApplSwID_Object = MibScalar
mcm4400t1e1SysStatusApplSwID = _Mcm4400t1e1SysStatusApplSwID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2, 6),
    _Mcm4400t1e1SysStatusApplSwID_Type()
)
mcm4400t1e1SysStatusApplSwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysStatusApplSwID.setStatus("mandatory")


class _Mcm4400t1e1SysStatusBootSwVer_Type(DisplayString):
    """Custom type mcm4400t1e1SysStatusBootSwVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Mcm4400t1e1SysStatusBootSwVer_Type.__name__ = "DisplayString"
_Mcm4400t1e1SysStatusBootSwVer_Object = MibScalar
mcm4400t1e1SysStatusBootSwVer = _Mcm4400t1e1SysStatusBootSwVer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 2, 7),
    _Mcm4400t1e1SysStatusBootSwVer_Type()
)
mcm4400t1e1SysStatusBootSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1SysStatusBootSwVer.setStatus("mandatory")
_Mcm4400t1e1DPStatusTable_Object = MibTable
mcm4400t1e1DPStatusTable = _Mcm4400t1e1DPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3)
)
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusTable.setStatus("mandatory")
_Mcm4400t1e1DPStatusEntry_Object = MibTableRow
mcm4400t1e1DPStatusEntry = _Mcm4400t1e1DPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3, 1)
)
mcm4400t1e1DPStatusEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DPStatusPortNumber"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusEntry.setStatus("mandatory")


class _Mcm4400t1e1DPStatusPortNumber_Type(Integer32):
    """Custom type mcm4400t1e1DPStatusPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port1", 1),
          ("port2", 2))
    )


_Mcm4400t1e1DPStatusPortNumber_Type.__name__ = "Integer32"
_Mcm4400t1e1DPStatusPortNumber_Object = MibTableColumn
mcm4400t1e1DPStatusPortNumber = _Mcm4400t1e1DPStatusPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3, 1, 1),
    _Mcm4400t1e1DPStatusPortNumber_Type()
)
mcm4400t1e1DPStatusPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusPortNumber.setStatus("mandatory")


class _Mcm4400t1e1DPStatusDTRInputSt_Type(Integer32):
    """Custom type mcm4400t1e1DPStatusDTRInputSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Mcm4400t1e1DPStatusDTRInputSt_Type.__name__ = "Integer32"
_Mcm4400t1e1DPStatusDTRInputSt_Object = MibTableColumn
mcm4400t1e1DPStatusDTRInputSt = _Mcm4400t1e1DPStatusDTRInputSt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3, 1, 2),
    _Mcm4400t1e1DPStatusDTRInputSt_Type()
)
mcm4400t1e1DPStatusDTRInputSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusDTRInputSt.setStatus("mandatory")


class _Mcm4400t1e1DPStatusRTSInputSt_Type(Integer32):
    """Custom type mcm4400t1e1DPStatusRTSInputSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Mcm4400t1e1DPStatusRTSInputSt_Type.__name__ = "Integer32"
_Mcm4400t1e1DPStatusRTSInputSt_Object = MibTableColumn
mcm4400t1e1DPStatusRTSInputSt = _Mcm4400t1e1DPStatusRTSInputSt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3, 1, 3),
    _Mcm4400t1e1DPStatusRTSInputSt_Type()
)
mcm4400t1e1DPStatusRTSInputSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusRTSInputSt.setStatus("mandatory")


class _Mcm4400t1e1DPStatusDSROutputSt_Type(Integer32):
    """Custom type mcm4400t1e1DPStatusDSROutputSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Mcm4400t1e1DPStatusDSROutputSt_Type.__name__ = "Integer32"
_Mcm4400t1e1DPStatusDSROutputSt_Object = MibTableColumn
mcm4400t1e1DPStatusDSROutputSt = _Mcm4400t1e1DPStatusDSROutputSt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3, 1, 4),
    _Mcm4400t1e1DPStatusDSROutputSt_Type()
)
mcm4400t1e1DPStatusDSROutputSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusDSROutputSt.setStatus("mandatory")


class _Mcm4400t1e1DPStatusDCDOutputSt_Type(Integer32):
    """Custom type mcm4400t1e1DPStatusDCDOutputSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Mcm4400t1e1DPStatusDCDOutputSt_Type.__name__ = "Integer32"
_Mcm4400t1e1DPStatusDCDOutputSt_Object = MibTableColumn
mcm4400t1e1DPStatusDCDOutputSt = _Mcm4400t1e1DPStatusDCDOutputSt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3, 1, 5),
    _Mcm4400t1e1DPStatusDCDOutputSt_Type()
)
mcm4400t1e1DPStatusDCDOutputSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusDCDOutputSt.setStatus("mandatory")


class _Mcm4400t1e1DPStatusCTSOutputSt_Type(Integer32):
    """Custom type mcm4400t1e1DPStatusCTSOutputSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Mcm4400t1e1DPStatusCTSOutputSt_Type.__name__ = "Integer32"
_Mcm4400t1e1DPStatusCTSOutputSt_Object = MibTableColumn
mcm4400t1e1DPStatusCTSOutputSt = _Mcm4400t1e1DPStatusCTSOutputSt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 3, 1, 6),
    _Mcm4400t1e1DPStatusCTSOutputSt_Type()
)
mcm4400t1e1DPStatusCTSOutputSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DPStatusCTSOutputSt.setStatus("mandatory")
_Mcm4400t1e1DS0ChSigTable_Object = MibTable
mcm4400t1e1DS0ChSigTable = _Mcm4400t1e1DS0ChSigTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 4)
)
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChSigTable.setStatus("mandatory")
_Mcm4400t1e1DS0ChSigEntry_Object = MibTableRow
mcm4400t1e1DS0ChSigEntry = _Mcm4400t1e1DS0ChSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 4, 1)
)
mcm4400t1e1DS0ChSigEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DS0ChSigLineID"),
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1DS0ChSigDS0Index"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChSigEntry.setStatus("mandatory")


class _Mcm4400t1e1DS0ChSigLineID_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChSigLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2))
    )


_Mcm4400t1e1DS0ChSigLineID_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChSigLineID_Object = MibTableColumn
mcm4400t1e1DS0ChSigLineID = _Mcm4400t1e1DS0ChSigLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 4, 1, 1),
    _Mcm4400t1e1DS0ChSigLineID_Type()
)
mcm4400t1e1DS0ChSigLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChSigLineID.setStatus("mandatory")


class _Mcm4400t1e1DS0ChSigDS0Index_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChSigDS0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Mcm4400t1e1DS0ChSigDS0Index_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChSigDS0Index_Object = MibTableColumn
mcm4400t1e1DS0ChSigDS0Index = _Mcm4400t1e1DS0ChSigDS0Index_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 4, 1, 2),
    _Mcm4400t1e1DS0ChSigDS0Index_Type()
)
mcm4400t1e1DS0ChSigDS0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChSigDS0Index.setStatus("mandatory")


class _Mcm4400t1e1DS0ChSigInABCDBits_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChSigInABCDBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mcm4400t1e1DS0ChSigInABCDBits_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChSigInABCDBits_Object = MibTableColumn
mcm4400t1e1DS0ChSigInABCDBits = _Mcm4400t1e1DS0ChSigInABCDBits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 4, 1, 3),
    _Mcm4400t1e1DS0ChSigInABCDBits_Type()
)
mcm4400t1e1DS0ChSigInABCDBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChSigInABCDBits.setStatus("mandatory")


class _Mcm4400t1e1DS0ChSigOutABCDBits_Type(Integer32):
    """Custom type mcm4400t1e1DS0ChSigOutABCDBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Mcm4400t1e1DS0ChSigOutABCDBits_Type.__name__ = "Integer32"
_Mcm4400t1e1DS0ChSigOutABCDBits_Object = MibTableColumn
mcm4400t1e1DS0ChSigOutABCDBits = _Mcm4400t1e1DS0ChSigOutABCDBits_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 4, 1, 4),
    _Mcm4400t1e1DS0ChSigOutABCDBits_Type()
)
mcm4400t1e1DS0ChSigOutABCDBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1DS0ChSigOutABCDBits.setStatus("mandatory")
_Mcm4400t1e1ChTestResultsGroup_ObjectIdentity = ObjectIdentity
mcm4400t1e1ChTestResultsGroup = _Mcm4400t1e1ChTestResultsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 5)
)


class _Mcm4400t1e1ChTestResultsLineID_Type(Integer32):
    """Custom type mcm4400t1e1ChTestResultsLineID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("network", 2),
          ("none", 3))
    )


_Mcm4400t1e1ChTestResultsLineID_Type.__name__ = "Integer32"
_Mcm4400t1e1ChTestResultsLineID_Object = MibScalar
mcm4400t1e1ChTestResultsLineID = _Mcm4400t1e1ChTestResultsLineID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 5, 1),
    _Mcm4400t1e1ChTestResultsLineID_Type()
)
mcm4400t1e1ChTestResultsLineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1ChTestResultsLineID.setStatus("mandatory")


class _Mcm4400t1e1ChTestResultsDS0Ch_Type(Integer32):
    """Custom type mcm4400t1e1ChTestResultsDS0Ch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Mcm4400t1e1ChTestResultsDS0Ch_Type.__name__ = "Integer32"
_Mcm4400t1e1ChTestResultsDS0Ch_Object = MibScalar
mcm4400t1e1ChTestResultsDS0Ch = _Mcm4400t1e1ChTestResultsDS0Ch_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 5, 2),
    _Mcm4400t1e1ChTestResultsDS0Ch_Type()
)
mcm4400t1e1ChTestResultsDS0Ch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1ChTestResultsDS0Ch.setStatus("mandatory")
_Mcm4400t1e1ChTestResultsErrorCnt_Type = Counter32
_Mcm4400t1e1ChTestResultsErrorCnt_Object = MibScalar
mcm4400t1e1ChTestResultsErrorCnt = _Mcm4400t1e1ChTestResultsErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 3, 5, 3),
    _Mcm4400t1e1ChTestResultsErrorCnt_Type()
)
mcm4400t1e1ChTestResultsErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1ChTestResultsErrorCnt.setStatus("mandatory")
_T1e1_r2_statistics_ObjectIdentity = ObjectIdentity
t1e1_r2_statistics = _T1e1_r2_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4)
)
_Mcm4400t1e1LineStatsTable_Object = MibTable
mcm4400t1e1LineStatsTable = _Mcm4400t1e1LineStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1)
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsTable.setStatus("mandatory")
_Mcm4400t1e1LineStatsEntry_Object = MibTableRow
mcm4400t1e1LineStatsEntry = _Mcm4400t1e1LineStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1)
)
mcm4400t1e1LineStatsEntry.setIndexNames(
    (0, "MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatsLineIndex"),
)
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsEntry.setStatus("mandatory")


class _Mcm4400t1e1LineStatsLineIndex_Type(Integer32):
    """Custom type mcm4400t1e1LineStatsLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localLine", 1),
          ("networkLine", 2))
    )


_Mcm4400t1e1LineStatsLineIndex_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatsLineIndex_Object = MibTableColumn
mcm4400t1e1LineStatsLineIndex = _Mcm4400t1e1LineStatsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 1),
    _Mcm4400t1e1LineStatsLineIndex_Type()
)
mcm4400t1e1LineStatsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsLineIndex.setStatus("mandatory")


class _Mcm4400t1e1LineStatsInterface_Type(Integer32):
    """Custom type mcm4400t1e1LineStatsInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_Mcm4400t1e1LineStatsInterface_Type.__name__ = "Integer32"
_Mcm4400t1e1LineStatsInterface_Object = MibTableColumn
mcm4400t1e1LineStatsInterface = _Mcm4400t1e1LineStatsInterface_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 2),
    _Mcm4400t1e1LineStatsInterface_Type()
)
mcm4400t1e1LineStatsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsInterface.setStatus("mandatory")
_Mcm4400t1e1LineStatsFramingBitError_Type = Counter32
_Mcm4400t1e1LineStatsFramingBitError_Object = MibTableColumn
mcm4400t1e1LineStatsFramingBitError = _Mcm4400t1e1LineStatsFramingBitError_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 3),
    _Mcm4400t1e1LineStatsFramingBitError_Type()
)
mcm4400t1e1LineStatsFramingBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsFramingBitError.setStatus("mandatory")
_Mcm4400t1e1LineStatsLineCdViolation_Type = Counter32
_Mcm4400t1e1LineStatsLineCdViolation_Object = MibTableColumn
mcm4400t1e1LineStatsLineCdViolation = _Mcm4400t1e1LineStatsLineCdViolation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 4),
    _Mcm4400t1e1LineStatsLineCdViolation_Type()
)
mcm4400t1e1LineStatsLineCdViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsLineCdViolation.setStatus("mandatory")
_Mcm4400t1e1LineStatsFarEndBlkError_Type = Counter32
_Mcm4400t1e1LineStatsFarEndBlkError_Object = MibTableColumn
mcm4400t1e1LineStatsFarEndBlkError = _Mcm4400t1e1LineStatsFarEndBlkError_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 5),
    _Mcm4400t1e1LineStatsFarEndBlkError_Type()
)
mcm4400t1e1LineStatsFarEndBlkError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsFarEndBlkError.setStatus("mandatory")
_Mcm4400t1e1LineStatsCRCError_Type = Counter32
_Mcm4400t1e1LineStatsCRCError_Object = MibTableColumn
mcm4400t1e1LineStatsCRCError = _Mcm4400t1e1LineStatsCRCError_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 6),
    _Mcm4400t1e1LineStatsCRCError_Type()
)
mcm4400t1e1LineStatsCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsCRCError.setStatus("mandatory")
_Mcm4400t1e1LineStatsBufferOverrun_Type = Counter32
_Mcm4400t1e1LineStatsBufferOverrun_Object = MibTableColumn
mcm4400t1e1LineStatsBufferOverrun = _Mcm4400t1e1LineStatsBufferOverrun_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 7),
    _Mcm4400t1e1LineStatsBufferOverrun_Type()
)
mcm4400t1e1LineStatsBufferOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsBufferOverrun.setStatus("mandatory")
_Mcm4400t1e1LineStatsBufferUnderrun_Type = Counter32
_Mcm4400t1e1LineStatsBufferUnderrun_Object = MibTableColumn
mcm4400t1e1LineStatsBufferUnderrun = _Mcm4400t1e1LineStatsBufferUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 8),
    _Mcm4400t1e1LineStatsBufferUnderrun_Type()
)
mcm4400t1e1LineStatsBufferUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsBufferUnderrun.setStatus("mandatory")
_Mcm4400t1e1LineStatsFrmSyncBitError_Type = Counter32
_Mcm4400t1e1LineStatsFrmSyncBitError_Object = MibTableColumn
mcm4400t1e1LineStatsFrmSyncBitError = _Mcm4400t1e1LineStatsFrmSyncBitError_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 9),
    _Mcm4400t1e1LineStatsFrmSyncBitError_Type()
)
mcm4400t1e1LineStatsFrmSyncBitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsFrmSyncBitError.setStatus("mandatory")
_Mcm4400t1e1LineStatsOutOfFrame_Type = Counter32
_Mcm4400t1e1LineStatsOutOfFrame_Object = MibTableColumn
mcm4400t1e1LineStatsOutOfFrame = _Mcm4400t1e1LineStatsOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 10),
    _Mcm4400t1e1LineStatsOutOfFrame_Type()
)
mcm4400t1e1LineStatsOutOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsOutOfFrame.setStatus("mandatory")
_Mcm4400t1e1LineStatsTotalFrameSlip_Type = Counter32
_Mcm4400t1e1LineStatsTotalFrameSlip_Object = MibTableColumn
mcm4400t1e1LineStatsTotalFrameSlip = _Mcm4400t1e1LineStatsTotalFrameSlip_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 4, 1, 1, 11),
    _Mcm4400t1e1LineStatsTotalFrameSlip_Type()
)
mcm4400t1e1LineStatsTotalFrameSlip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcm4400t1e1LineStatsTotalFrameSlip.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcm4400T1NoCodeImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 1)
)
mcm4400T1NoCodeImage.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400T1NoCodeImage.setStatus(
        ""
    )

mcm4400T1DownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 2)
)
mcm4400T1DownloadFail.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400T1DownloadFail.setStatus(
        ""
    )

mcm4400T1OutOfOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 3)
)
mcm4400T1OutOfOrder.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400T1OutOfOrder.setStatus(
        ""
    )

mcm4400T1OutOfOrderRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 4)
)
mcm4400T1OutOfOrderRecovered.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400T1OutOfOrderRecovered.setStatus(
        ""
    )

mcm4400T1FailToSyncUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 5)
)
mcm4400T1FailToSyncUp.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400T1FailToSyncUp.setStatus(
        ""
    )

mcm4400T1FailToSyncUpRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 6)
)
mcm4400T1FailToSyncUpRecovered.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400T1FailToSyncUpRecovered.setStatus(
        ""
    )

mcm4400T1AISAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 7)
)
mcm4400T1AISAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400T1AISAlarmSet.setStatus(
        ""
    )

mcm4400T1AISAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 8)
)
mcm4400T1AISAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400T1AISAlarmClear.setStatus(
        ""
    )

mcm4400T1RedAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 9)
)
mcm4400T1RedAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400T1RedAlarmSet.setStatus(
        ""
    )

mcm4400T1RedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 10)
)
mcm4400T1RedAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400T1RedAlarmClear.setStatus(
        ""
    )

mcm4400T1YellowAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 11)
)
mcm4400T1YellowAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400T1YellowAlarmSet.setStatus(
        ""
    )

mcm4400T1YellowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 12)
)
mcm4400T1YellowAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400T1YellowAlarmClear.setStatus(
        ""
    )

mcm4400E1NoCodeImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 13)
)
mcm4400E1NoCodeImage.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400E1NoCodeImage.setStatus(
        ""
    )

mcm4400E1DownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 14)
)
mcm4400E1DownloadFail.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400E1DownloadFail.setStatus(
        ""
    )

mcm4400E1OutOfOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 15)
)
mcm4400E1OutOfOrder.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400E1OutOfOrder.setStatus(
        ""
    )

mcm4400E1OutOfOrderRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 16)
)
mcm4400E1OutOfOrderRecovered.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400E1OutOfOrderRecovered.setStatus(
        ""
    )

mcm4400E1FailToSyncUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 17)
)
mcm4400E1FailToSyncUp.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400E1FailToSyncUp.setStatus(
        ""
    )

mcm4400E1FailToSyncUpRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 18)
)
mcm4400E1FailToSyncUpRecovered.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcm4400E1FailToSyncUpRecovered.setStatus(
        ""
    )

mcm4400E1AISAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 19)
)
mcm4400E1AISAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1AISAlarmSet.setStatus(
        ""
    )

mcm4400E1AISAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 20)
)
mcm4400E1AISAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1AISAlarmClear.setStatus(
        ""
    )

mcm4400E1RedAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 21)
)
mcm4400E1RedAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1RedAlarmSet.setStatus(
        ""
    )

mcm4400E1RedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 22)
)
mcm4400E1RedAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1RedAlarmClear.setStatus(
        ""
    )

mcm4400E1TS16AISAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 23)
)
mcm4400E1TS16AISAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1TS16AISAlarmSet.setStatus(
        ""
    )

mcm4400E1TS16AISAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 24)
)
mcm4400E1TS16AISAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1TS16AISAlarmClear.setStatus(
        ""
    )

mcm4400E1OOSMFAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 25)
)
mcm4400E1OOSMFAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1OOSMFAlarmSet.setStatus(
        ""
    )

mcm4400E1OOSMFAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 26)
)
mcm4400E1OOSMFAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1OOSMFAlarmClear.setStatus(
        ""
    )

mcm4400E1RemoteYBitAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 27)
)
mcm4400E1RemoteYBitAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1RemoteYBitAlarmSet.setStatus(
        ""
    )

mcm4400E1RemoteYBitAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 28)
)
mcm4400E1RemoteYBitAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1RemoteYBitAlarmClear.setStatus(
        ""
    )

mcm4400E1RemoteABitAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 29)
)
mcm4400E1RemoteABitAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1RemoteABitAlarmSet.setStatus(
        ""
    )

mcm4400E1RemoteABitAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 30)
)
mcm4400E1RemoteABitAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1RemoteABitAlarmClear.setStatus(
        ""
    )

mcm4400E1OOCMFAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 31)
)
mcm4400E1OOCMFAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1OOCMFAlarmSet.setStatus(
        ""
    )

mcm4400E1OOCMFAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 22, 0, 32)
)
mcm4400E1OOCMFAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-T1E1-MIB", "mcm4400t1e1LineStatusLineIndex"))
)
if mibBuilder.loadTexts:
    mcm4400E1OOCMFAlarmClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-4400-T1E1-MIB",
    **{"micom-2t1e1": micom_2t1e1,
       "mcm4400T1NoCodeImage": mcm4400T1NoCodeImage,
       "mcm4400T1DownloadFail": mcm4400T1DownloadFail,
       "mcm4400T1OutOfOrder": mcm4400T1OutOfOrder,
       "mcm4400T1OutOfOrderRecovered": mcm4400T1OutOfOrderRecovered,
       "mcm4400T1FailToSyncUp": mcm4400T1FailToSyncUp,
       "mcm4400T1FailToSyncUpRecovered": mcm4400T1FailToSyncUpRecovered,
       "mcm4400T1AISAlarmSet": mcm4400T1AISAlarmSet,
       "mcm4400T1AISAlarmClear": mcm4400T1AISAlarmClear,
       "mcm4400T1RedAlarmSet": mcm4400T1RedAlarmSet,
       "mcm4400T1RedAlarmClear": mcm4400T1RedAlarmClear,
       "mcm4400T1YellowAlarmSet": mcm4400T1YellowAlarmSet,
       "mcm4400T1YellowAlarmClear": mcm4400T1YellowAlarmClear,
       "mcm4400E1NoCodeImage": mcm4400E1NoCodeImage,
       "mcm4400E1DownloadFail": mcm4400E1DownloadFail,
       "mcm4400E1OutOfOrder": mcm4400E1OutOfOrder,
       "mcm4400E1OutOfOrderRecovered": mcm4400E1OutOfOrderRecovered,
       "mcm4400E1FailToSyncUp": mcm4400E1FailToSyncUp,
       "mcm4400E1FailToSyncUpRecovered": mcm4400E1FailToSyncUpRecovered,
       "mcm4400E1AISAlarmSet": mcm4400E1AISAlarmSet,
       "mcm4400E1AISAlarmClear": mcm4400E1AISAlarmClear,
       "mcm4400E1RedAlarmSet": mcm4400E1RedAlarmSet,
       "mcm4400E1RedAlarmClear": mcm4400E1RedAlarmClear,
       "mcm4400E1TS16AISAlarmSet": mcm4400E1TS16AISAlarmSet,
       "mcm4400E1TS16AISAlarmClear": mcm4400E1TS16AISAlarmClear,
       "mcm4400E1OOSMFAlarmSet": mcm4400E1OOSMFAlarmSet,
       "mcm4400E1OOSMFAlarmClear": mcm4400E1OOSMFAlarmClear,
       "mcm4400E1RemoteYBitAlarmSet": mcm4400E1RemoteYBitAlarmSet,
       "mcm4400E1RemoteYBitAlarmClear": mcm4400E1RemoteYBitAlarmClear,
       "mcm4400E1RemoteABitAlarmSet": mcm4400E1RemoteABitAlarmSet,
       "mcm4400E1RemoteABitAlarmClear": mcm4400E1RemoteABitAlarmClear,
       "mcm4400E1OOCMFAlarmSet": mcm4400E1OOCMFAlarmSet,
       "mcm4400E1OOCMFAlarmClear": mcm4400E1OOCMFAlarmClear,
       "t1e1-r2-configuration": t1e1_r2_configuration,
       "mcm4400t1e1LineCfgTable": mcm4400t1e1LineCfgTable,
       "mcm4400t1e1LineCfgEntry": mcm4400t1e1LineCfgEntry,
       "mcm4400t1e1LineCfgLineID": mcm4400t1e1LineCfgLineID,
       "mcm4400t1e1LineCfgProfileNum": mcm4400t1e1LineCfgProfileNum,
       "mcm4400t1e1ProfCfgTable": mcm4400t1e1ProfCfgTable,
       "mcm4400t1e1ProfCfgEntry": mcm4400t1e1ProfCfgEntry,
       "mcm4400t1e1ProfCfgProfileNum": mcm4400t1e1ProfCfgProfileNum,
       "mcm4400t1e1ProfCfgT1FrameFmt": mcm4400t1e1ProfCfgT1FrameFmt,
       "mcm4400t1e1ProfCfgT1LineCode": mcm4400t1e1ProfCfgT1LineCode,
       "mcm4400t1e1ProfCfgE1LineCode": mcm4400t1e1ProfCfgE1LineCode,
       "mcm4400t1e1ProfCfgIdleCode": mcm4400t1e1ProfCfgIdleCode,
       "mcm4400t1e1ProfCfgT1LineBuildOut": mcm4400t1e1ProfCfgT1LineBuildOut,
       "mcm4400t1e1ProfCfgT1Loopback": mcm4400t1e1ProfCfgT1Loopback,
       "mcm4400t1e1ProfCfgE1CRC4": mcm4400t1e1ProfCfgE1CRC4,
       "mcm4400t1e1ProfCfgE1TS16Conn": mcm4400t1e1ProfCfgE1TS16Conn,
       "mcm4400t1e1DS0ChConnTable": mcm4400t1e1DS0ChConnTable,
       "mcm4400t1e1DS0ChConnEntry": mcm4400t1e1DS0ChConnEntry,
       "mcm4400t1e1DS0ChConnLineID": mcm4400t1e1DS0ChConnLineID,
       "mcm4400t1e1DS0ChConnDS0Index": mcm4400t1e1DS0ChConnDS0Index,
       "mcm4400t1e1DS0ChConnState": mcm4400t1e1DS0ChConnState,
       "mcm4400t1e1DPCfgTable": mcm4400t1e1DPCfgTable,
       "mcm4400t1e1DPCfgEntry": mcm4400t1e1DPCfgEntry,
       "mcm4400t1e1DPCfgPortNum": mcm4400t1e1DPCfgPortNum,
       "mcm4400t1e1DPCfgDataRate": mcm4400t1e1DPCfgDataRate,
       "mcm4400t1e1DPCfgClock": mcm4400t1e1DPCfgClock,
       "mcm4400t1e1DPCfgDTRCntl": mcm4400t1e1DPCfgDTRCntl,
       "mcm4400t1e1DPCfgRTSCntl": mcm4400t1e1DPCfgRTSCntl,
       "mcm4400t1e1SysCfgClockSource": mcm4400t1e1SysCfgClockSource,
       "nvm4400t1e1LineCfgTable": nvm4400t1e1LineCfgTable,
       "nvm4400t1e1LineCfgEntry": nvm4400t1e1LineCfgEntry,
       "nvm4400t1e1LineCfgLineID": nvm4400t1e1LineCfgLineID,
       "nvm4400t1e1LineCfgProfileNum": nvm4400t1e1LineCfgProfileNum,
       "nvm4400t1e1ProfCfgTable": nvm4400t1e1ProfCfgTable,
       "nvm4400t1e1ProfCfgEntry": nvm4400t1e1ProfCfgEntry,
       "nvm4400t1e1ProfCfgProfileNum": nvm4400t1e1ProfCfgProfileNum,
       "nvm4400t1e1ProfCfgT1FrameFmt": nvm4400t1e1ProfCfgT1FrameFmt,
       "nvm4400t1e1ProfCfgT1LineCode": nvm4400t1e1ProfCfgT1LineCode,
       "nvm4400t1e1ProfCfgE1LineCode": nvm4400t1e1ProfCfgE1LineCode,
       "nvm4400t1e1ProfCfgIdleCode": nvm4400t1e1ProfCfgIdleCode,
       "nvm4400t1e1ProfCfgT1LineBuildOut": nvm4400t1e1ProfCfgT1LineBuildOut,
       "nvm4400t1e1ProfCfgT1Loopback": nvm4400t1e1ProfCfgT1Loopback,
       "nvm4400t1e1ProfCfgE1CRC4": nvm4400t1e1ProfCfgE1CRC4,
       "nvm4400t1e1ProfCfgE1TS16Conn": nvm4400t1e1ProfCfgE1TS16Conn,
       "nvm4400t1e1DS0ChConnTable": nvm4400t1e1DS0ChConnTable,
       "nvm4400t1e1DS0ChConnEntry": nvm4400t1e1DS0ChConnEntry,
       "nvm4400t1e1DS0ChConnLineID": nvm4400t1e1DS0ChConnLineID,
       "nvm4400t1e1DS0ChConnDS0Index": nvm4400t1e1DS0ChConnDS0Index,
       "nvm4400t1e1DS0ChConnState": nvm4400t1e1DS0ChConnState,
       "nvm4400t1e1DPCfgTable": nvm4400t1e1DPCfgTable,
       "nvm4400t1e1DPCfgEntry": nvm4400t1e1DPCfgEntry,
       "nvm4400t1e1DPCfgPortNum": nvm4400t1e1DPCfgPortNum,
       "nvm4400t1e1DPCfgDataRate": nvm4400t1e1DPCfgDataRate,
       "nvm4400t1e1DPCfgClock": nvm4400t1e1DPCfgClock,
       "nvm4400t1e1DPCfgDTRCntl": nvm4400t1e1DPCfgDTRCntl,
       "nvm4400t1e1DPCfgRTSCntl": nvm4400t1e1DPCfgRTSCntl,
       "nvm4400t1e1SysCfgClockSource": nvm4400t1e1SysCfgClockSource,
       "t1e1-r2-control": t1e1_r2_control,
       "mcm4400t1e1DS0ChTestCmdTable": mcm4400t1e1DS0ChTestCmdTable,
       "mcm4400t1e1DS0ChTestCmdEntry": mcm4400t1e1DS0ChTestCmdEntry,
       "mcm4400t1e1DS0ChTestCmdLineID": mcm4400t1e1DS0ChTestCmdLineID,
       "mcm4400t1e1DS0ChTestCmdDS0Index": mcm4400t1e1DS0ChTestCmdDS0Index,
       "mcm4400t1e1DS0ChTestCmdTstPattern": mcm4400t1e1DS0ChTestCmdTstPattern,
       "mcm4400t1e1LineTestCmdTable": mcm4400t1e1LineTestCmdTable,
       "mcm4400t1e1LineTestCmdEntry": mcm4400t1e1LineTestCmdEntry,
       "mcm4400t1e1LineTestCmdLineID": mcm4400t1e1LineTestCmdLineID,
       "mcm4400t1e1LineTestCmdTstPattern": mcm4400t1e1LineTestCmdTstPattern,
       "mcm4400t1e1DPTestCmdTable": mcm4400t1e1DPTestCmdTable,
       "mcm4400t1e1DPTestCmdEntry": mcm4400t1e1DPTestCmdEntry,
       "mcm4400t1e1DPTestCmdPortNum": mcm4400t1e1DPTestCmdPortNum,
       "mcm4400t1e1DPTestCmdTstPattern": mcm4400t1e1DPTestCmdTstPattern,
       "mcm4400t1e1SysControlActionCmd": mcm4400t1e1SysControlActionCmd,
       "t1e1-r2-status": t1e1_r2_status,
       "mcm4400t1e1LineStatusTable": mcm4400t1e1LineStatusTable,
       "mcm4400t1e1LineStatusEntry": mcm4400t1e1LineStatusEntry,
       "mcm4400t1e1LineStatusLineIndex": mcm4400t1e1LineStatusLineIndex,
       "mcm4400t1e1LineStatusInterface": mcm4400t1e1LineStatusInterface,
       "mcm4400t1e1LineStatusImpedance": mcm4400t1e1LineStatusImpedance,
       "mcm4400t1e1LineStatusTestMode": mcm4400t1e1LineStatusTestMode,
       "mcm4400t1e1LineStatusTestingDS0Ch": mcm4400t1e1LineStatusTestingDS0Ch,
       "mcm4400t1e1LineStatusAISAlarm": mcm4400t1e1LineStatusAISAlarm,
       "mcm4400t1e1LineStatusRedAlarm": mcm4400t1e1LineStatusRedAlarm,
       "mcm4400t1e1LineStatusYellowAlarm": mcm4400t1e1LineStatusYellowAlarm,
       "mcm4400t1e1LineStatusTS16AIS": mcm4400t1e1LineStatusTS16AIS,
       "mcm4400t1e1LineStatusOOSMFAlarm": mcm4400t1e1LineStatusOOSMFAlarm,
       "mcm4400t1e1LineStatusMFASAlarm": mcm4400t1e1LineStatusMFASAlarm,
       "mcm4400t1e1LineStatusFASAlarm": mcm4400t1e1LineStatusFASAlarm,
       "mcm4400t1e1LineStatusOOCMFAlarm": mcm4400t1e1LineStatusOOCMFAlarm,
       "mcm4400t1e1SysStatusGroup": mcm4400t1e1SysStatusGroup,
       "mcm4400t1e1SysStatusCardType": mcm4400t1e1SysStatusCardType,
       "mcm4400t1e1SysStatusOperStatus": mcm4400t1e1SysStatusOperStatus,
       "mcm4400t1e1SysStatusLEDTest": mcm4400t1e1SysStatusLEDTest,
       "mcm4400t1e1SysStatusSelfTestResults": mcm4400t1e1SysStatusSelfTestResults,
       "mcm4400t1e1SysStatusFlashEPROMSt": mcm4400t1e1SysStatusFlashEPROMSt,
       "mcm4400t1e1SysStatusApplSwID": mcm4400t1e1SysStatusApplSwID,
       "mcm4400t1e1SysStatusBootSwVer": mcm4400t1e1SysStatusBootSwVer,
       "mcm4400t1e1DPStatusTable": mcm4400t1e1DPStatusTable,
       "mcm4400t1e1DPStatusEntry": mcm4400t1e1DPStatusEntry,
       "mcm4400t1e1DPStatusPortNumber": mcm4400t1e1DPStatusPortNumber,
       "mcm4400t1e1DPStatusDTRInputSt": mcm4400t1e1DPStatusDTRInputSt,
       "mcm4400t1e1DPStatusRTSInputSt": mcm4400t1e1DPStatusRTSInputSt,
       "mcm4400t1e1DPStatusDSROutputSt": mcm4400t1e1DPStatusDSROutputSt,
       "mcm4400t1e1DPStatusDCDOutputSt": mcm4400t1e1DPStatusDCDOutputSt,
       "mcm4400t1e1DPStatusCTSOutputSt": mcm4400t1e1DPStatusCTSOutputSt,
       "mcm4400t1e1DS0ChSigTable": mcm4400t1e1DS0ChSigTable,
       "mcm4400t1e1DS0ChSigEntry": mcm4400t1e1DS0ChSigEntry,
       "mcm4400t1e1DS0ChSigLineID": mcm4400t1e1DS0ChSigLineID,
       "mcm4400t1e1DS0ChSigDS0Index": mcm4400t1e1DS0ChSigDS0Index,
       "mcm4400t1e1DS0ChSigInABCDBits": mcm4400t1e1DS0ChSigInABCDBits,
       "mcm4400t1e1DS0ChSigOutABCDBits": mcm4400t1e1DS0ChSigOutABCDBits,
       "mcm4400t1e1ChTestResultsGroup": mcm4400t1e1ChTestResultsGroup,
       "mcm4400t1e1ChTestResultsLineID": mcm4400t1e1ChTestResultsLineID,
       "mcm4400t1e1ChTestResultsDS0Ch": mcm4400t1e1ChTestResultsDS0Ch,
       "mcm4400t1e1ChTestResultsErrorCnt": mcm4400t1e1ChTestResultsErrorCnt,
       "t1e1-r2-statistics": t1e1_r2_statistics,
       "mcm4400t1e1LineStatsTable": mcm4400t1e1LineStatsTable,
       "mcm4400t1e1LineStatsEntry": mcm4400t1e1LineStatsEntry,
       "mcm4400t1e1LineStatsLineIndex": mcm4400t1e1LineStatsLineIndex,
       "mcm4400t1e1LineStatsInterface": mcm4400t1e1LineStatsInterface,
       "mcm4400t1e1LineStatsFramingBitError": mcm4400t1e1LineStatsFramingBitError,
       "mcm4400t1e1LineStatsLineCdViolation": mcm4400t1e1LineStatsLineCdViolation,
       "mcm4400t1e1LineStatsFarEndBlkError": mcm4400t1e1LineStatsFarEndBlkError,
       "mcm4400t1e1LineStatsCRCError": mcm4400t1e1LineStatsCRCError,
       "mcm4400t1e1LineStatsBufferOverrun": mcm4400t1e1LineStatsBufferOverrun,
       "mcm4400t1e1LineStatsBufferUnderrun": mcm4400t1e1LineStatsBufferUnderrun,
       "mcm4400t1e1LineStatsFrmSyncBitError": mcm4400t1e1LineStatsFrmSyncBitError,
       "mcm4400t1e1LineStatsOutOfFrame": mcm4400t1e1LineStatsOutOfFrame,
       "mcm4400t1e1LineStatsTotalFrameSlip": mcm4400t1e1LineStatsTotalFrameSlip}
)
