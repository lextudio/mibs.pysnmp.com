# SNMP MIB module (PAD-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAD-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:12 2024
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



class Counter16(Integer32):
    """Custom type Counter16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PPCTPadPortTable_Object = MibTable
cdx6500PPCTPadPortTable = _Cdx6500PPCTPadPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTPadPortTable.setStatus("mandatory")
_Cdx6500PPCTPadPortEntry_Object = MibTableRow
cdx6500PPCTPadPortEntry = _Cdx6500PPCTPadPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1)
)
cdx6500PPCTPadPortEntry.setIndexNames(
    (0, "PAD-OPT-MIB", "cdx6500padpCfgPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTPadPortEntry.setStatus("mandatory")


class _Cdx6500padpCfgPortNum_Type(Integer32):
    """Custom type cdx6500padpCfgPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500padpCfgPortNum_Type.__name__ = "Integer32"
_Cdx6500padpCfgPortNum_Object = MibTableColumn
cdx6500padpCfgPortNum = _Cdx6500padpCfgPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 1),
    _Cdx6500padpCfgPortNum_Type()
)
cdx6500padpCfgPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpCfgPortNum.setStatus("mandatory")


class _Cdx6500padpCfgConnectionType_Type(Integer32):
    """Custom type cdx6500padpCfgConnectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              21,
              50)
        )
    )
    namedValues = NamedValues(
        *(("dimo", 5),
          ("dimoa", 6),
          ("dimob", 7),
          ("dtr", 1),
          ("dtrd", 2),
          ("dtrp", 8),
          ("emdc", 4),
          ("emdcio", 21),
          ("emri", 3),
          ("newvalSimp", 50),
          ("simp", 0))
    )


_Cdx6500padpCfgConnectionType_Type.__name__ = "Integer32"
_Cdx6500padpCfgConnectionType_Object = MibTableColumn
cdx6500padpCfgConnectionType = _Cdx6500padpCfgConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 2),
    _Cdx6500padpCfgConnectionType_Type()
)
cdx6500padpCfgConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgConnectionType.setStatus("mandatory")


class _Cdx6500padpCfgPortControl_Type(DisplayString):
    """Custom type cdx6500padpCfgPortControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 4),
    )


_Cdx6500padpCfgPortControl_Type.__name__ = "DisplayString"
_Cdx6500padpCfgPortControl_Object = MibTableColumn
cdx6500padpCfgPortControl = _Cdx6500padpCfgPortControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 3),
    _Cdx6500padpCfgPortControl_Type()
)
cdx6500padpCfgPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgPortControl.setStatus("mandatory")


class _Cdx6500padpCfgPortSpeed_Type(Integer32):
    """Custom type cdx6500padpCfgPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              50,
              98,
              99)
        )
    )
    namedValues = NamedValues(
        *(("newvalSpeed110", 50),
          ("speed100", 9),
          ("speed110", 0),
          ("speed115200", 17),
          ("speed1200", 3),
          ("speed12000", 21),
          ("speed134", 1),
          ("speed14400", 19),
          ("speed150", 6),
          ("speed16800", 22),
          ("speed1800", 7),
          ("speed19200", 15),
          ("speed200", 8),
          ("speed21600", 23),
          ("speed2400", 12),
          ("speed24000", 24),
          ("speed26400", 25),
          ("speed28800", 20),
          ("speed300", 2),
          ("speed33400", 26),
          ("speed38400", 16),
          ("speed4800", 13),
          ("speed50", 10),
          ("speed57600", 18),
          ("speed600", 4),
          ("speed7200", 98),
          ("speed75", 5),
          ("speed75to1200", 11),
          ("speed9600", 14),
          ("speedAuto", 99))
    )


_Cdx6500padpCfgPortSpeed_Type.__name__ = "Integer32"
_Cdx6500padpCfgPortSpeed_Object = MibTableColumn
cdx6500padpCfgPortSpeed = _Cdx6500padpCfgPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 4),
    _Cdx6500padpCfgPortSpeed_Type()
)
cdx6500padpCfgPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgPortSpeed.setStatus("mandatory")


class _Cdx6500padpCfgAutoBaudSeq_Type(Integer32):
    """Custom type cdx6500padpCfgAutoBaudSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              50)
        )
    )
    namedValues = NamedValues(
        *(("crDotCr", 1),
          ("crOnly", 0),
          ("dotDotCr", 4),
          ("newvalCrOnly", 50),
          ("spacePCr", 5),
          ("telenet", 3),
          ("tymnet", 2))
    )


_Cdx6500padpCfgAutoBaudSeq_Type.__name__ = "Integer32"
_Cdx6500padpCfgAutoBaudSeq_Object = MibTableColumn
cdx6500padpCfgAutoBaudSeq = _Cdx6500padpCfgAutoBaudSeq_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 5),
    _Cdx6500padpCfgAutoBaudSeq_Type()
)
cdx6500padpCfgAutoBaudSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgAutoBaudSeq.setStatus("mandatory")


class _Cdx6500padpCfgDataBits_Type(Integer32):
    """Custom type cdx6500padpCfgDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_Cdx6500padpCfgDataBits_Type.__name__ = "Integer32"
_Cdx6500padpCfgDataBits_Object = MibTableColumn
cdx6500padpCfgDataBits = _Cdx6500padpCfgDataBits_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 6),
    _Cdx6500padpCfgDataBits_Type()
)
cdx6500padpCfgDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgDataBits.setStatus("mandatory")


class _Cdx6500padpCfgParity_Type(Integer32):
    """Custom type cdx6500padpCfgParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              50)
        )
    )
    namedValues = NamedValues(
        *(("auto", 5),
          ("autoA", 6),
          ("even", 3),
          ("mark", 2),
          ("newvalNone", 50),
          ("none", 0),
          ("odd", 4),
          ("space", 1))
    )


_Cdx6500padpCfgParity_Type.__name__ = "Integer32"
_Cdx6500padpCfgParity_Object = MibTableColumn
cdx6500padpCfgParity = _Cdx6500padpCfgParity_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 7),
    _Cdx6500padpCfgParity_Type()
)
cdx6500padpCfgParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgParity.setStatus("mandatory")


class _Cdx6500padpCfgStopBits_Type(Integer32):
    """Custom type cdx6500padpCfgStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalStopBit1", 50),
          ("stopBit1", 0),
          ("stopBit1p5", 1),
          ("stopBit2", 2))
    )


_Cdx6500padpCfgStopBits_Type.__name__ = "Integer32"
_Cdx6500padpCfgStopBits_Object = MibTableColumn
cdx6500padpCfgStopBits = _Cdx6500padpCfgStopBits_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 8),
    _Cdx6500padpCfgStopBits_Type()
)
cdx6500padpCfgStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgStopBits.setStatus("mandatory")


class _Cdx6500padpCfgProfileName_Type(DisplayString):
    """Custom type cdx6500padpCfgProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500padpCfgProfileName_Type.__name__ = "DisplayString"
_Cdx6500padpCfgProfileName_Object = MibTableColumn
cdx6500padpCfgProfileName = _Cdx6500padpCfgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 9),
    _Cdx6500padpCfgProfileName_Type()
)
cdx6500padpCfgProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgProfileName.setStatus("mandatory")


class _Cdx6500padpCfgCallControl_Type(DisplayString):
    """Custom type cdx6500padpCfgCallControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 40),
    )


_Cdx6500padpCfgCallControl_Type.__name__ = "DisplayString"
_Cdx6500padpCfgCallControl_Object = MibTableColumn
cdx6500padpCfgCallControl = _Cdx6500padpCfgCallControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 10),
    _Cdx6500padpCfgCallControl_Type()
)
cdx6500padpCfgCallControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgCallControl.setStatus("mandatory")


class _Cdx6500padpCfgTermControl_Type(DisplayString):
    """Custom type cdx6500padpCfgTermControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 60),
    )


_Cdx6500padpCfgTermControl_Type.__name__ = "DisplayString"
_Cdx6500padpCfgTermControl_Object = MibTableColumn
cdx6500padpCfgTermControl = _Cdx6500padpCfgTermControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 11),
    _Cdx6500padpCfgTermControl_Type()
)
cdx6500padpCfgTermControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgTermControl.setStatus("mandatory")


class _Cdx6500padpCfgPadPromptNum_Type(Integer32):
    """Custom type cdx6500padpCfgPadPromptNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_Cdx6500padpCfgPadPromptNum_Type.__name__ = "Integer32"
_Cdx6500padpCfgPadPromptNum_Object = MibTableColumn
cdx6500padpCfgPadPromptNum = _Cdx6500padpCfgPadPromptNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 12),
    _Cdx6500padpCfgPadPromptNum_Type()
)
cdx6500padpCfgPadPromptNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgPadPromptNum.setStatus("mandatory")


class _Cdx6500padpCfgRemoteParamNum_Type(Integer32):
    """Custom type cdx6500padpCfgRemoteParamNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Cdx6500padpCfgRemoteParamNum_Type.__name__ = "Integer32"
_Cdx6500padpCfgRemoteParamNum_Object = MibTableColumn
cdx6500padpCfgRemoteParamNum = _Cdx6500padpCfgRemoteParamNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 13),
    _Cdx6500padpCfgRemoteParamNum_Type()
)
cdx6500padpCfgRemoteParamNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgRemoteParamNum.setStatus("mandatory")


class _Cdx6500padpCfgAutoCallMnem_Type(DisplayString):
    """Custom type cdx6500padpCfgAutoCallMnem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500padpCfgAutoCallMnem_Type.__name__ = "DisplayString"
_Cdx6500padpCfgAutoCallMnem_Object = MibTableColumn
cdx6500padpCfgAutoCallMnem = _Cdx6500padpCfgAutoCallMnem_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 14),
    _Cdx6500padpCfgAutoCallMnem_Type()
)
cdx6500padpCfgAutoCallMnem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgAutoCallMnem.setStatus("mandatory")


class _Cdx6500padpCfgAutoCallTimeout_Type(Integer32):
    """Custom type cdx6500padpCfgAutoCallTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500padpCfgAutoCallTimeout_Type.__name__ = "Integer32"
_Cdx6500padpCfgAutoCallTimeout_Object = MibTableColumn
cdx6500padpCfgAutoCallTimeout = _Cdx6500padpCfgAutoCallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 15),
    _Cdx6500padpCfgAutoCallTimeout_Type()
)
cdx6500padpCfgAutoCallTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgAutoCallTimeout.setStatus("mandatory")


class _Cdx6500padpCfgMaxAutoCall_Type(Integer32):
    """Custom type cdx6500padpCfgMaxAutoCall based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padpCfgMaxAutoCall_Type.__name__ = "Integer32"
_Cdx6500padpCfgMaxAutoCall_Object = MibTableColumn
cdx6500padpCfgMaxAutoCall = _Cdx6500padpCfgMaxAutoCall_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 16),
    _Cdx6500padpCfgMaxAutoCall_Type()
)
cdx6500padpCfgMaxAutoCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgMaxAutoCall.setStatus("mandatory")


class _Cdx6500padpCfgSubAddress_Type(DisplayString):
    """Custom type cdx6500padpCfgSubAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500padpCfgSubAddress_Type.__name__ = "DisplayString"
_Cdx6500padpCfgSubAddress_Object = MibTableColumn
cdx6500padpCfgSubAddress = _Cdx6500padpCfgSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 17),
    _Cdx6500padpCfgSubAddress_Type()
)
cdx6500padpCfgSubAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgSubAddress.setStatus("mandatory")


class _Cdx6500padpCfgGroupSubaddress_Type(DisplayString):
    """Custom type cdx6500padpCfgGroupSubaddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_Cdx6500padpCfgGroupSubaddress_Type.__name__ = "DisplayString"
_Cdx6500padpCfgGroupSubaddress_Object = MibTableColumn
cdx6500padpCfgGroupSubaddress = _Cdx6500padpCfgGroupSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 18),
    _Cdx6500padpCfgGroupSubaddress_Type()
)
cdx6500padpCfgGroupSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpCfgGroupSubaddress.setStatus("mandatory")


class _Cdx6500padpCfgCugMembership_Type(DisplayString):
    """Custom type cdx6500padpCfgCugMembership based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_Cdx6500padpCfgCugMembership_Type.__name__ = "DisplayString"
_Cdx6500padpCfgCugMembership_Object = MibTableColumn
cdx6500padpCfgCugMembership = _Cdx6500padpCfgCugMembership_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 19),
    _Cdx6500padpCfgCugMembership_Type()
)
cdx6500padpCfgCugMembership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgCugMembership.setStatus("mandatory")


class _Cdx6500padpCfgBillingRecord_Type(Integer32):
    """Custom type cdx6500padpCfgBillingRecord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              50)
        )
    )
    namedValues = NamedValues(
        *(("newvalOff", 50),
          ("off", 0),
          ("on", 1))
    )


_Cdx6500padpCfgBillingRecord_Type.__name__ = "Integer32"
_Cdx6500padpCfgBillingRecord_Object = MibTableColumn
cdx6500padpCfgBillingRecord = _Cdx6500padpCfgBillingRecord_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 20),
    _Cdx6500padpCfgBillingRecord_Type()
)
cdx6500padpCfgBillingRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgBillingRecord.setStatus("mandatory")


class _Cdx6500padpCfgInviteToClr_Type(Integer32):
    """Custom type cdx6500padpCfgInviteToClr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("clrwd", 2),
          ("clrwo", 1),
          ("newvalNone", 50),
          ("none", 0))
    )


_Cdx6500padpCfgInviteToClr_Type.__name__ = "Integer32"
_Cdx6500padpCfgInviteToClr_Object = MibTableColumn
cdx6500padpCfgInviteToClr = _Cdx6500padpCfgInviteToClr_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 21),
    _Cdx6500padpCfgInviteToClr_Type()
)
cdx6500padpCfgInviteToClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgInviteToClr.setStatus("mandatory")


class _Cdx6500padpCfgCallAcceptTime_Type(Integer32):
    """Custom type cdx6500padpCfgCallAcceptTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padpCfgCallAcceptTime_Type.__name__ = "Integer32"
_Cdx6500padpCfgCallAcceptTime_Object = MibTableColumn
cdx6500padpCfgCallAcceptTime = _Cdx6500padpCfgCallAcceptTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 22),
    _Cdx6500padpCfgCallAcceptTime_Type()
)
cdx6500padpCfgCallAcceptTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgCallAcceptTime.setStatus("mandatory")


class _Cdx6500padpCfgProtectionLevel_Type(Integer32):
    """Custom type cdx6500padpCfgProtectionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              50)
        )
    )
    namedValues = NamedValues(
        *(("cpOnly", 1),
          ("fullDcp", 2),
          ("newvalNone", 50),
          ("none", 0))
    )


_Cdx6500padpCfgProtectionLevel_Type.__name__ = "Integer32"
_Cdx6500padpCfgProtectionLevel_Object = MibTableColumn
cdx6500padpCfgProtectionLevel = _Cdx6500padpCfgProtectionLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 23),
    _Cdx6500padpCfgProtectionLevel_Type()
)
cdx6500padpCfgProtectionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgProtectionLevel.setStatus("mandatory")


class _Cdx6500padpCfgReconnectTimeout_Type(Integer32):
    """Custom type cdx6500padpCfgReconnectTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdx6500padpCfgReconnectTimeout_Type.__name__ = "Integer32"
_Cdx6500padpCfgReconnectTimeout_Object = MibTableColumn
cdx6500padpCfgReconnectTimeout = _Cdx6500padpCfgReconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 24),
    _Cdx6500padpCfgReconnectTimeout_Type()
)
cdx6500padpCfgReconnectTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgReconnectTimeout.setStatus("mandatory")


class _Cdx6500padpCfgReconnectTries_Type(Integer32):
    """Custom type cdx6500padpCfgReconnectTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padpCfgReconnectTries_Type.__name__ = "Integer32"
_Cdx6500padpCfgReconnectTries_Object = MibTableColumn
cdx6500padpCfgReconnectTries = _Cdx6500padpCfgReconnectTries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 25),
    _Cdx6500padpCfgReconnectTries_Type()
)
cdx6500padpCfgReconnectTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgReconnectTries.setStatus("mandatory")


class _Cdx6500padpCfgMaxRcvBufLength_Type(Integer32):
    """Custom type cdx6500padpCfgMaxRcvBufLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Cdx6500padpCfgMaxRcvBufLength_Type.__name__ = "Integer32"
_Cdx6500padpCfgMaxRcvBufLength_Object = MibTableColumn
cdx6500padpCfgMaxRcvBufLength = _Cdx6500padpCfgMaxRcvBufLength_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 26),
    _Cdx6500padpCfgMaxRcvBufLength_Type()
)
cdx6500padpCfgMaxRcvBufLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgMaxRcvBufLength.setStatus("mandatory")


class _Cdx6500padpCfgCommandLanguage_Type(Integer32):
    """Custom type cdx6500padpCfgCommandLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ccitt", 1),
          ("dpn", 2),
          ("nc", 100))
    )


_Cdx6500padpCfgCommandLanguage_Type.__name__ = "Integer32"
_Cdx6500padpCfgCommandLanguage_Object = MibTableColumn
cdx6500padpCfgCommandLanguage = _Cdx6500padpCfgCommandLanguage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 27),
    _Cdx6500padpCfgCommandLanguage_Type()
)
cdx6500padpCfgCommandLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgCommandLanguage.setStatus("mandatory")


class _Cdx6500padpCfgNUIFacilityFormat_Type(Integer32):
    """Custom type cdx6500padpCfgNUIFacilityFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("dpn1992", 4),
          ("nc", 100),
          ("ndpn", 3),
          ("odpn", 2))
    )


_Cdx6500padpCfgNUIFacilityFormat_Type.__name__ = "Integer32"
_Cdx6500padpCfgNUIFacilityFormat_Object = MibTableColumn
cdx6500padpCfgNUIFacilityFormat = _Cdx6500padpCfgNUIFacilityFormat_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 28),
    _Cdx6500padpCfgNUIFacilityFormat_Type()
)
cdx6500padpCfgNUIFacilityFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgNUIFacilityFormat.setStatus("mandatory")


class _Cdx6500padpCfgNUIVerifyTimer_Type(Integer32):
    """Custom type cdx6500padpCfgNUIVerifyTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 180),
    )


_Cdx6500padpCfgNUIVerifyTimer_Type.__name__ = "Integer32"
_Cdx6500padpCfgNUIVerifyTimer_Object = MibTableColumn
cdx6500padpCfgNUIVerifyTimer = _Cdx6500padpCfgNUIVerifyTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 29),
    _Cdx6500padpCfgNUIVerifyTimer_Type()
)
cdx6500padpCfgNUIVerifyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgNUIVerifyTimer.setStatus("mandatory")


class _Cdx6500padpCfgMaxNUIViolations_Type(Integer32):
    """Custom type cdx6500padpCfgMaxNUIViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Cdx6500padpCfgMaxNUIViolations_Type.__name__ = "Integer32"
_Cdx6500padpCfgMaxNUIViolations_Object = MibTableColumn
cdx6500padpCfgMaxNUIViolations = _Cdx6500padpCfgMaxNUIViolations_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 30),
    _Cdx6500padpCfgMaxNUIViolations_Type()
)
cdx6500padpCfgMaxNUIViolations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgMaxNUIViolations.setStatus("mandatory")


class _Cdx6500padpCfgActionTypeNUIV_Type(Integer32):
    """Custom type cdx6500padpCfgActionTypeNUIV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("degr", 2),
          ("disc", 4),
          ("lock", 3),
          ("nc", 100),
          ("none", 1))
    )


_Cdx6500padpCfgActionTypeNUIV_Type.__name__ = "Integer32"
_Cdx6500padpCfgActionTypeNUIV_Object = MibTableColumn
cdx6500padpCfgActionTypeNUIV = _Cdx6500padpCfgActionTypeNUIV_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 31),
    _Cdx6500padpCfgActionTypeNUIV_Type()
)
cdx6500padpCfgActionTypeNUIV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgActionTypeNUIV.setStatus("mandatory")


class _Cdx6500padpCfgCalledDTEAddress_Type(DisplayString):
    """Custom type cdx6500padpCfgCalledDTEAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Cdx6500padpCfgCalledDTEAddress_Type.__name__ = "DisplayString"
_Cdx6500padpCfgCalledDTEAddress_Object = MibTableColumn
cdx6500padpCfgCalledDTEAddress = _Cdx6500padpCfgCalledDTEAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 32),
    _Cdx6500padpCfgCalledDTEAddress_Type()
)
cdx6500padpCfgCalledDTEAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgCalledDTEAddress.setStatus("mandatory")


class _Cdx6500padpCfgCallingDTEIdent_Type(DisplayString):
    """Custom type cdx6500padpCfgCallingDTEIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Cdx6500padpCfgCallingDTEIdent_Type.__name__ = "DisplayString"
_Cdx6500padpCfgCallingDTEIdent_Object = MibTableColumn
cdx6500padpCfgCallingDTEIdent = _Cdx6500padpCfgCallingDTEIdent_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 33),
    _Cdx6500padpCfgCallingDTEIdent_Type()
)
cdx6500padpCfgCallingDTEIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgCallingDTEIdent.setStatus("mandatory")


class _Cdx6500padpCfgCallingDTEPasswd_Type(DisplayString):
    """Custom type cdx6500padpCfgCallingDTEPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Cdx6500padpCfgCallingDTEPasswd_Type.__name__ = "DisplayString"
_Cdx6500padpCfgCallingDTEPasswd_Object = MibTableColumn
cdx6500padpCfgCallingDTEPasswd = _Cdx6500padpCfgCallingDTEPasswd_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 34),
    _Cdx6500padpCfgCallingDTEPasswd_Type()
)
cdx6500padpCfgCallingDTEPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgCallingDTEPasswd.setStatus("mandatory")


class _Cdx6500padpCfgX28ResetService_Type(DisplayString):
    """Custom type cdx6500padpCfgX28ResetService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Cdx6500padpCfgX28ResetService_Type.__name__ = "DisplayString"
_Cdx6500padpCfgX28ResetService_Object = MibTableColumn
cdx6500padpCfgX28ResetService = _Cdx6500padpCfgX28ResetService_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 35),
    _Cdx6500padpCfgX28ResetService_Type()
)
cdx6500padpCfgX28ResetService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgX28ResetService.setStatus("mandatory")


class _Cdx6500padpCfgX28ClearService_Type(DisplayString):
    """Custom type cdx6500padpCfgX28ClearService based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_Cdx6500padpCfgX28ClearService_Type.__name__ = "DisplayString"
_Cdx6500padpCfgX28ClearService_Object = MibTableColumn
cdx6500padpCfgX28ClearService = _Cdx6500padpCfgX28ClearService_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 36),
    _Cdx6500padpCfgX28ClearService_Type()
)
cdx6500padpCfgX28ClearService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgX28ClearService.setStatus("mandatory")


class _Cdx6500padpCfgMAXMNEMFailures_Type(Integer32):
    """Custom type cdx6500padpCfgMAXMNEMFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padpCfgMAXMNEMFailures_Type.__name__ = "Integer32"
_Cdx6500padpCfgMAXMNEMFailures_Object = MibTableColumn
cdx6500padpCfgMAXMNEMFailures = _Cdx6500padpCfgMAXMNEMFailures_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 37),
    _Cdx6500padpCfgMAXMNEMFailures_Type()
)
cdx6500padpCfgMAXMNEMFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgMAXMNEMFailures.setStatus("mandatory")


class _Cdx6500padpCfgActionTypeMNEMFail_Type(Integer32):
    """Custom type cdx6500padpCfgActionTypeMNEMFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("degr", 2),
          ("disc", 4),
          ("lock", 3),
          ("nc", 100),
          ("none", 1))
    )


_Cdx6500padpCfgActionTypeMNEMFail_Type.__name__ = "Integer32"
_Cdx6500padpCfgActionTypeMNEMFail_Object = MibTableColumn
cdx6500padpCfgActionTypeMNEMFail = _Cdx6500padpCfgActionTypeMNEMFail_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 38),
    _Cdx6500padpCfgActionTypeMNEMFail_Type()
)
cdx6500padpCfgActionTypeMNEMFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgActionTypeMNEMFail.setStatus("mandatory")


class _Cdx6500padpCfgActiveLineMessage_Type(DisplayString):
    """Custom type cdx6500padpCfgActiveLineMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Cdx6500padpCfgActiveLineMessage_Type.__name__ = "DisplayString"
_Cdx6500padpCfgActiveLineMessage_Object = MibTableColumn
cdx6500padpCfgActiveLineMessage = _Cdx6500padpCfgActiveLineMessage_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 39),
    _Cdx6500padpCfgActiveLineMessage_Type()
)
cdx6500padpCfgActiveLineMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgActiveLineMessage.setStatus("mandatory")


class _Cdx6500padpCfgDelayActiveLine_Type(Integer32):
    """Custom type cdx6500padpCfgDelayActiveLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Cdx6500padpCfgDelayActiveLine_Type.__name__ = "Integer32"
_Cdx6500padpCfgDelayActiveLine_Object = MibTableColumn
cdx6500padpCfgDelayActiveLine = _Cdx6500padpCfgDelayActiveLine_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 40),
    _Cdx6500padpCfgDelayActiveLine_Type()
)
cdx6500padpCfgDelayActiveLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgDelayActiveLine.setStatus("mandatory")


class _Cdx6500padpCfgInterCharTimer_Type(Integer32):
    """Custom type cdx6500padpCfgInterCharTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Cdx6500padpCfgInterCharTimer_Type.__name__ = "Integer32"
_Cdx6500padpCfgInterCharTimer_Object = MibTableColumn
cdx6500padpCfgInterCharTimer = _Cdx6500padpCfgInterCharTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 41),
    _Cdx6500padpCfgInterCharTimer_Type()
)
cdx6500padpCfgInterCharTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgInterCharTimer.setStatus("mandatory")


class _Cdx6500padpCfgElectricalInterfaceType_Type(Integer32):
    """Custom type cdx6500padpCfgElectricalInterfaceType based on Integer32"""
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
        *(("none", 5),
          ("v24", 1),
          ("v35", 2),
          ("v36", 3),
          ("x21", 4))
    )


_Cdx6500padpCfgElectricalInterfaceType_Type.__name__ = "Integer32"
_Cdx6500padpCfgElectricalInterfaceType_Object = MibTableColumn
cdx6500padpCfgElectricalInterfaceType = _Cdx6500padpCfgElectricalInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 42),
    _Cdx6500padpCfgElectricalInterfaceType_Type()
)
cdx6500padpCfgElectricalInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgElectricalInterfaceType.setStatus("mandatory")


class _Cdx6500padpCfgV24ElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500padpCfgV24ElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ri", 1),
          ("tm", 2))
    )


_Cdx6500padpCfgV24ElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500padpCfgV24ElectricalInterfaceOption_Object = MibTableColumn
cdx6500padpCfgV24ElectricalInterfaceOption = _Cdx6500padpCfgV24ElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 43),
    _Cdx6500padpCfgV24ElectricalInterfaceOption_Type()
)
cdx6500padpCfgV24ElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgV24ElectricalInterfaceOption.setStatus("mandatory")


class _Cdx6500padpCfgHighSpeedElectricalInterfaceOption_Type(Integer32):
    """Custom type cdx6500padpCfgHighSpeedElectricalInterfaceOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xover", 2))
    )


_Cdx6500padpCfgHighSpeedElectricalInterfaceOption_Type.__name__ = "Integer32"
_Cdx6500padpCfgHighSpeedElectricalInterfaceOption_Object = MibTableColumn
cdx6500padpCfgHighSpeedElectricalInterfaceOption = _Cdx6500padpCfgHighSpeedElectricalInterfaceOption_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 1, 1, 44),
    _Cdx6500padpCfgHighSpeedElectricalInterfaceOption_Type()
)
cdx6500padpCfgHighSpeedElectricalInterfaceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdx6500padpCfgHighSpeedElectricalInterfaceOption.setStatus("mandatory")
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500CfgPadPromptTable_Object = MibTable
cdx6500CfgPadPromptTable = _Cdx6500CfgPadPromptTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cdx6500CfgPadPromptTable.setStatus("mandatory")
_Cdx6500CfgPadPromptEntry_Object = MibTableRow
cdx6500CfgPadPromptEntry = _Cdx6500CfgPadPromptEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 4, 1)
)
cdx6500CfgPadPromptEntry.setIndexNames(
    (0, "PAD-OPT-MIB", "cdx6500padpromptEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500CfgPadPromptEntry.setStatus("mandatory")


class _Cdx6500padpromptEntryNum_Type(Integer32):
    """Custom type cdx6500padpromptEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Cdx6500padpromptEntryNum_Type.__name__ = "Integer32"
_Cdx6500padpromptEntryNum_Object = MibTableColumn
cdx6500padpromptEntryNum = _Cdx6500padpromptEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 4, 1, 1),
    _Cdx6500padpromptEntryNum_Type()
)
cdx6500padpromptEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpromptEntryNum.setStatus("mandatory")


class _Cdx6500padpromptPromptText_Type(DisplayString):
    """Custom type cdx6500padpromptPromptText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Cdx6500padpromptPromptText_Type.__name__ = "DisplayString"
_Cdx6500padpromptPromptText_Object = MibTableColumn
cdx6500padpromptPromptText = _Cdx6500padpromptPromptText_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 4, 1, 2),
    _Cdx6500padpromptPromptText_Type()
)
cdx6500padpromptPromptText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpromptPromptText.setStatus("mandatory")
_Cdx6500CfgPadProfileTable_Object = MibTable
cdx6500CfgPadProfileTable = _Cdx6500CfgPadProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    cdx6500CfgPadProfileTable.setStatus("mandatory")
_Cdx6500CfgPadProfileEntry_Object = MibTableRow
cdx6500CfgPadProfileEntry = _Cdx6500CfgPadProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1)
)
cdx6500CfgPadProfileEntry.setIndexNames(
    (0, "PAD-OPT-MIB", "cdx6500padprofProfileNum"),
)
if mibBuilder.loadTexts:
    cdx6500CfgPadProfileEntry.setStatus("mandatory")


class _Cdx6500padprofProfileNum_Type(Integer32):
    """Custom type cdx6500padprofProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Cdx6500padprofProfileNum_Type.__name__ = "Integer32"
_Cdx6500padprofProfileNum_Object = MibTableColumn
cdx6500padprofProfileNum = _Cdx6500padprofProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 1),
    _Cdx6500padprofProfileNum_Type()
)
cdx6500padprofProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofProfileNum.setStatus("mandatory")


class _Cdx6500padprofProfileName_Type(DisplayString):
    """Custom type cdx6500padprofProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500padprofProfileName_Type.__name__ = "DisplayString"
_Cdx6500padprofProfileName_Object = MibTableColumn
cdx6500padprofProfileName = _Cdx6500padprofProfileName_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 2),
    _Cdx6500padprofProfileName_Type()
)
cdx6500padprofProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofProfileName.setStatus("mandatory")


class _Cdx6500padprofPar1_Type(Integer32):
    """Custom type cdx6500padprofPar1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_Cdx6500padprofPar1_Type.__name__ = "Integer32"
_Cdx6500padprofPar1_Object = MibTableColumn
cdx6500padprofPar1 = _Cdx6500padprofPar1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 3),
    _Cdx6500padprofPar1_Type()
)
cdx6500padprofPar1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar1.setStatus("mandatory")


class _Cdx6500padprofPar2_Type(Integer32):
    """Custom type cdx6500padprofPar2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cdx6500padprofPar2_Type.__name__ = "Integer32"
_Cdx6500padprofPar2_Object = MibTableColumn
cdx6500padprofPar2 = _Cdx6500padprofPar2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 4),
    _Cdx6500padprofPar2_Type()
)
cdx6500padprofPar2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar2.setStatus("mandatory")


class _Cdx6500padprofPar3_Type(DisplayString):
    """Custom type cdx6500padprofPar3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 18),
    )


_Cdx6500padprofPar3_Type.__name__ = "DisplayString"
_Cdx6500padprofPar3_Object = MibTableColumn
cdx6500padprofPar3 = _Cdx6500padprofPar3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 5),
    _Cdx6500padprofPar3_Type()
)
cdx6500padprofPar3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar3.setStatus("mandatory")


class _Cdx6500padprofPar4_Type(Integer32):
    """Custom type cdx6500padprofPar4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar4_Type.__name__ = "Integer32"
_Cdx6500padprofPar4_Object = MibTableColumn
cdx6500padprofPar4 = _Cdx6500padprofPar4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 6),
    _Cdx6500padprofPar4_Type()
)
cdx6500padprofPar4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar4.setStatus("mandatory")


class _Cdx6500padprofPar5_Type(Integer32):
    """Custom type cdx6500padprofPar5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Cdx6500padprofPar5_Type.__name__ = "Integer32"
_Cdx6500padprofPar5_Object = MibTableColumn
cdx6500padprofPar5 = _Cdx6500padprofPar5_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 7),
    _Cdx6500padprofPar5_Type()
)
cdx6500padprofPar5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar5.setStatus("mandatory")


class _Cdx6500padprofPar6_Type(Integer32):
    """Custom type cdx6500padprofPar6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13),
    )


_Cdx6500padprofPar6_Type.__name__ = "Integer32"
_Cdx6500padprofPar6_Object = MibTableColumn
cdx6500padprofPar6 = _Cdx6500padprofPar6_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 8),
    _Cdx6500padprofPar6_Type()
)
cdx6500padprofPar6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar6.setStatus("mandatory")


class _Cdx6500padprofPar7_Type(Integer32):
    """Custom type cdx6500padprofPar7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_Cdx6500padprofPar7_Type.__name__ = "Integer32"
_Cdx6500padprofPar7_Object = MibTableColumn
cdx6500padprofPar7 = _Cdx6500padprofPar7_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 9),
    _Cdx6500padprofPar7_Type()
)
cdx6500padprofPar7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar7.setStatus("mandatory")


class _Cdx6500padprofPar9_Type(Integer32):
    """Custom type cdx6500padprofPar9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar9_Type.__name__ = "Integer32"
_Cdx6500padprofPar9_Object = MibTableColumn
cdx6500padprofPar9 = _Cdx6500padprofPar9_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 10),
    _Cdx6500padprofPar9_Type()
)
cdx6500padprofPar9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar9.setStatus("mandatory")


class _Cdx6500padprofPar10_Type(Integer32):
    """Custom type cdx6500padprofPar10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar10_Type.__name__ = "Integer32"
_Cdx6500padprofPar10_Object = MibTableColumn
cdx6500padprofPar10 = _Cdx6500padprofPar10_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 11),
    _Cdx6500padprofPar10_Type()
)
cdx6500padprofPar10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar10.setStatus("mandatory")


class _Cdx6500padprofPar12_Type(Integer32):
    """Custom type cdx6500padprofPar12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cdx6500padprofPar12_Type.__name__ = "Integer32"
_Cdx6500padprofPar12_Object = MibTableColumn
cdx6500padprofPar12 = _Cdx6500padprofPar12_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 12),
    _Cdx6500padprofPar12_Type()
)
cdx6500padprofPar12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar12.setStatus("mandatory")


class _Cdx6500padprofPar13_Type(DisplayString):
    """Custom type cdx6500padprofPar13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 7),
    )


_Cdx6500padprofPar13_Type.__name__ = "DisplayString"
_Cdx6500padprofPar13_Object = MibTableColumn
cdx6500padprofPar13 = _Cdx6500padprofPar13_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 13),
    _Cdx6500padprofPar13_Type()
)
cdx6500padprofPar13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar13.setStatus("mandatory")


class _Cdx6500padprofPar14_Type(Integer32):
    """Custom type cdx6500padprofPar14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar14_Type.__name__ = "Integer32"
_Cdx6500padprofPar14_Object = MibTableColumn
cdx6500padprofPar14 = _Cdx6500padprofPar14_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 14),
    _Cdx6500padprofPar14_Type()
)
cdx6500padprofPar14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar14.setStatus("mandatory")


class _Cdx6500padprofPar15_Type(Integer32):
    """Custom type cdx6500padprofPar15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cdx6500padprofPar15_Type.__name__ = "Integer32"
_Cdx6500padprofPar15_Object = MibTableColumn
cdx6500padprofPar15 = _Cdx6500padprofPar15_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 15),
    _Cdx6500padprofPar15_Type()
)
cdx6500padprofPar15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar15.setStatus("mandatory")


class _Cdx6500padprofPar16_Type(Integer32):
    """Custom type cdx6500padprofPar16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padprofPar16_Type.__name__ = "Integer32"
_Cdx6500padprofPar16_Object = MibTableColumn
cdx6500padprofPar16 = _Cdx6500padprofPar16_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 16),
    _Cdx6500padprofPar16_Type()
)
cdx6500padprofPar16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar16.setStatus("mandatory")


class _Cdx6500padprofPar17_Type(Integer32):
    """Custom type cdx6500padprofPar17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padprofPar17_Type.__name__ = "Integer32"
_Cdx6500padprofPar17_Object = MibTableColumn
cdx6500padprofPar17 = _Cdx6500padprofPar17_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 17),
    _Cdx6500padprofPar17_Type()
)
cdx6500padprofPar17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar17.setStatus("mandatory")


class _Cdx6500padprofPar18_Type(Integer32):
    """Custom type cdx6500padprofPar18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padprofPar18_Type.__name__ = "Integer32"
_Cdx6500padprofPar18_Object = MibTableColumn
cdx6500padprofPar18 = _Cdx6500padprofPar18_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 18),
    _Cdx6500padprofPar18_Type()
)
cdx6500padprofPar18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar18.setStatus("mandatory")


class _Cdx6500padprofPar19_Type(Integer32):
    """Custom type cdx6500padprofPar19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_Cdx6500padprofPar19_Type.__name__ = "Integer32"
_Cdx6500padprofPar19_Object = MibTableColumn
cdx6500padprofPar19 = _Cdx6500padprofPar19_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 19),
    _Cdx6500padprofPar19_Type()
)
cdx6500padprofPar19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar19.setStatus("mandatory")


class _Cdx6500padprofPar20_Type(DisplayString):
    """Custom type cdx6500padprofPar20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 22),
    )


_Cdx6500padprofPar20_Type.__name__ = "DisplayString"
_Cdx6500padprofPar20_Object = MibTableColumn
cdx6500padprofPar20 = _Cdx6500padprofPar20_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 20),
    _Cdx6500padprofPar20_Type()
)
cdx6500padprofPar20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar20.setStatus("mandatory")


class _Cdx6500padprofPar21_Type(Integer32):
    """Custom type cdx6500padprofPar21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Cdx6500padprofPar21_Type.__name__ = "Integer32"
_Cdx6500padprofPar21_Object = MibTableColumn
cdx6500padprofPar21 = _Cdx6500padprofPar21_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 21),
    _Cdx6500padprofPar21_Type()
)
cdx6500padprofPar21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar21.setStatus("mandatory")


class _Cdx6500padprofPar22_Type(Integer32):
    """Custom type cdx6500padprofPar22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar22_Type.__name__ = "Integer32"
_Cdx6500padprofPar22_Object = MibTableColumn
cdx6500padprofPar22 = _Cdx6500padprofPar22_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 22),
    _Cdx6500padprofPar22_Type()
)
cdx6500padprofPar22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar22.setStatus("mandatory")


class _Cdx6500padprofPar100_Type(Integer32):
    """Custom type cdx6500padprofPar100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padprofPar100_Type.__name__ = "Integer32"
_Cdx6500padprofPar100_Object = MibTableColumn
cdx6500padprofPar100 = _Cdx6500padprofPar100_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 23),
    _Cdx6500padprofPar100_Type()
)
cdx6500padprofPar100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar100.setStatus("mandatory")


class _Cdx6500padprofPar101_Type(Integer32):
    """Custom type cdx6500padprofPar101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padprofPar101_Type.__name__ = "Integer32"
_Cdx6500padprofPar101_Object = MibTableColumn
cdx6500padprofPar101 = _Cdx6500padprofPar101_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 24),
    _Cdx6500padprofPar101_Type()
)
cdx6500padprofPar101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar101.setStatus("mandatory")


class _Cdx6500padprofPar102_Type(Integer32):
    """Custom type cdx6500padprofPar102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padprofPar102_Type.__name__ = "Integer32"
_Cdx6500padprofPar102_Object = MibTableColumn
cdx6500padprofPar102 = _Cdx6500padprofPar102_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 25),
    _Cdx6500padprofPar102_Type()
)
cdx6500padprofPar102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar102.setStatus("mandatory")


class _Cdx6500padprofPar103_Type(Integer32):
    """Custom type cdx6500padprofPar103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar103_Type.__name__ = "Integer32"
_Cdx6500padprofPar103_Object = MibTableColumn
cdx6500padprofPar103 = _Cdx6500padprofPar103_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 26),
    _Cdx6500padprofPar103_Type()
)
cdx6500padprofPar103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar103.setStatus("mandatory")


class _Cdx6500padprofPar104_Type(Integer32):
    """Custom type cdx6500padprofPar104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar104_Type.__name__ = "Integer32"
_Cdx6500padprofPar104_Object = MibTableColumn
cdx6500padprofPar104 = _Cdx6500padprofPar104_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 27),
    _Cdx6500padprofPar104_Type()
)
cdx6500padprofPar104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar104.setStatus("mandatory")


class _Cdx6500padprofPar105_Type(DisplayString):
    """Custom type cdx6500padprofPar105 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 5),
    )


_Cdx6500padprofPar105_Type.__name__ = "DisplayString"
_Cdx6500padprofPar105_Object = MibTableColumn
cdx6500padprofPar105 = _Cdx6500padprofPar105_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 28),
    _Cdx6500padprofPar105_Type()
)
cdx6500padprofPar105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar105.setStatus("mandatory")


class _Cdx6500padprofPar106_Type(Integer32):
    """Custom type cdx6500padprofPar106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Cdx6500padprofPar106_Type.__name__ = "Integer32"
_Cdx6500padprofPar106_Object = MibTableColumn
cdx6500padprofPar106 = _Cdx6500padprofPar106_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 29),
    _Cdx6500padprofPar106_Type()
)
cdx6500padprofPar106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar106.setStatus("mandatory")


class _Cdx6500padprofPar107_Type(Integer32):
    """Custom type cdx6500padprofPar107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar107_Type.__name__ = "Integer32"
_Cdx6500padprofPar107_Object = MibTableColumn
cdx6500padprofPar107 = _Cdx6500padprofPar107_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 30),
    _Cdx6500padprofPar107_Type()
)
cdx6500padprofPar107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar107.setStatus("mandatory")


class _Cdx6500padprofPar108_Type(Integer32):
    """Custom type cdx6500padprofPar108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500padprofPar108_Type.__name__ = "Integer32"
_Cdx6500padprofPar108_Object = MibTableColumn
cdx6500padprofPar108 = _Cdx6500padprofPar108_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 31),
    _Cdx6500padprofPar108_Type()
)
cdx6500padprofPar108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar108.setStatus("mandatory")


class _Cdx6500padprofPar109_Type(Integer32):
    """Custom type cdx6500padprofPar109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar109_Type.__name__ = "Integer32"
_Cdx6500padprofPar109_Object = MibTableColumn
cdx6500padprofPar109 = _Cdx6500padprofPar109_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 32),
    _Cdx6500padprofPar109_Type()
)
cdx6500padprofPar109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar109.setStatus("mandatory")


class _Cdx6500padprofPar110_Type(Integer32):
    """Custom type cdx6500padprofPar110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar110_Type.__name__ = "Integer32"
_Cdx6500padprofPar110_Object = MibTableColumn
cdx6500padprofPar110 = _Cdx6500padprofPar110_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 33),
    _Cdx6500padprofPar110_Type()
)
cdx6500padprofPar110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar110.setStatus("mandatory")


class _Cdx6500padprofPar111_Type(Integer32):
    """Custom type cdx6500padprofPar111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Cdx6500padprofPar111_Type.__name__ = "Integer32"
_Cdx6500padprofPar111_Object = MibTableColumn
cdx6500padprofPar111 = _Cdx6500padprofPar111_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 34),
    _Cdx6500padprofPar111_Type()
)
cdx6500padprofPar111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar111.setStatus("mandatory")


class _Cdx6500padprofPar112_Type(Integer32):
    """Custom type cdx6500padprofPar112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cdx6500padprofPar112_Type.__name__ = "Integer32"
_Cdx6500padprofPar112_Object = MibTableColumn
cdx6500padprofPar112 = _Cdx6500padprofPar112_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 35),
    _Cdx6500padprofPar112_Type()
)
cdx6500padprofPar112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar112.setStatus("mandatory")


class _Cdx6500padprofPar113_Type(Integer32):
    """Custom type cdx6500padprofPar113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Cdx6500padprofPar113_Type.__name__ = "Integer32"
_Cdx6500padprofPar113_Object = MibTableColumn
cdx6500padprofPar113 = _Cdx6500padprofPar113_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 36),
    _Cdx6500padprofPar113_Type()
)
cdx6500padprofPar113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar113.setStatus("mandatory")


class _Cdx6500padprofPar114_Type(Integer32):
    """Custom type cdx6500padprofPar114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Cdx6500padprofPar114_Type.__name__ = "Integer32"
_Cdx6500padprofPar114_Object = MibTableColumn
cdx6500padprofPar114 = _Cdx6500padprofPar114_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 37),
    _Cdx6500padprofPar114_Type()
)
cdx6500padprofPar114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar114.setStatus("mandatory")


class _Cdx6500padprofPar115_Type(Integer32):
    """Custom type cdx6500padprofPar115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Cdx6500padprofPar115_Type.__name__ = "Integer32"
_Cdx6500padprofPar115_Object = MibTableColumn
cdx6500padprofPar115 = _Cdx6500padprofPar115_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 38),
    _Cdx6500padprofPar115_Type()
)
cdx6500padprofPar115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar115.setStatus("mandatory")


class _Cdx6500padprofPar116_Type(Integer32):
    """Custom type cdx6500padprofPar116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar116_Type.__name__ = "Integer32"
_Cdx6500padprofPar116_Object = MibTableColumn
cdx6500padprofPar116 = _Cdx6500padprofPar116_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 39),
    _Cdx6500padprofPar116_Type()
)
cdx6500padprofPar116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar116.setStatus("mandatory")


class _Cdx6500padprofPar117_Type(Integer32):
    """Custom type cdx6500padprofPar117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cdx6500padprofPar117_Type.__name__ = "Integer32"
_Cdx6500padprofPar117_Object = MibTableColumn
cdx6500padprofPar117 = _Cdx6500padprofPar117_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 40),
    _Cdx6500padprofPar117_Type()
)
cdx6500padprofPar117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar117.setStatus("mandatory")


class _Cdx6500padprofPar118_Type(Integer32):
    """Custom type cdx6500padprofPar118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Cdx6500padprofPar118_Type.__name__ = "Integer32"
_Cdx6500padprofPar118_Object = MibTableColumn
cdx6500padprofPar118 = _Cdx6500padprofPar118_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 41),
    _Cdx6500padprofPar118_Type()
)
cdx6500padprofPar118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar118.setStatus("mandatory")


class _Cdx6500padprofPar119_Type(Integer32):
    """Custom type cdx6500padprofPar119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500padprofPar119_Type.__name__ = "Integer32"
_Cdx6500padprofPar119_Object = MibTableColumn
cdx6500padprofPar119 = _Cdx6500padprofPar119_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 8, 1, 42),
    _Cdx6500padprofPar119_Type()
)
cdx6500padprofPar119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padprofPar119.setStatus("mandatory")
_Cdx6500CfgRemotePadTable_Object = MibTable
cdx6500CfgRemotePadTable = _Cdx6500CfgRemotePadTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    cdx6500CfgRemotePadTable.setStatus("mandatory")
_Cdx6500CfgRemotePadEntry_Object = MibTableRow
cdx6500CfgRemotePadEntry = _Cdx6500CfgRemotePadEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1)
)
cdx6500CfgRemotePadEntry.setIndexNames(
    (0, "PAD-OPT-MIB", "cdx6500remotepadEntryNum"),
)
if mibBuilder.loadTexts:
    cdx6500CfgRemotePadEntry.setStatus("mandatory")


class _Cdx6500remotepadEntryNum_Type(Integer32):
    """Custom type cdx6500remotepadEntryNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_Cdx6500remotepadEntryNum_Type.__name__ = "Integer32"
_Cdx6500remotepadEntryNum_Object = MibTableColumn
cdx6500remotepadEntryNum = _Cdx6500remotepadEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 1),
    _Cdx6500remotepadEntryNum_Type()
)
cdx6500remotepadEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadEntryNum.setStatus("mandatory")


class _Cdx6500remotepadParamNum1_Type(Integer32):
    """Custom type cdx6500remotepadParamNum1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum1_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum1_Object = MibTableColumn
cdx6500remotepadParamNum1 = _Cdx6500remotepadParamNum1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 2),
    _Cdx6500remotepadParamNum1_Type()
)
cdx6500remotepadParamNum1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum1.setStatus("mandatory")


class _Cdx6500remotepadParamVal1_Type(Integer32):
    """Custom type cdx6500remotepadParamVal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal1_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal1_Object = MibTableColumn
cdx6500remotepadParamVal1 = _Cdx6500remotepadParamVal1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 3),
    _Cdx6500remotepadParamVal1_Type()
)
cdx6500remotepadParamVal1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal1.setStatus("mandatory")


class _Cdx6500remotepadParamNum2_Type(Integer32):
    """Custom type cdx6500remotepadParamNum2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum2_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum2_Object = MibTableColumn
cdx6500remotepadParamNum2 = _Cdx6500remotepadParamNum2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 4),
    _Cdx6500remotepadParamNum2_Type()
)
cdx6500remotepadParamNum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum2.setStatus("mandatory")


class _Cdx6500remotepadParamVal2_Type(Integer32):
    """Custom type cdx6500remotepadParamVal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal2_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal2_Object = MibTableColumn
cdx6500remotepadParamVal2 = _Cdx6500remotepadParamVal2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 5),
    _Cdx6500remotepadParamVal2_Type()
)
cdx6500remotepadParamVal2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal2.setStatus("mandatory")


class _Cdx6500remotepadParamNum3_Type(Integer32):
    """Custom type cdx6500remotepadParamNum3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum3_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum3_Object = MibTableColumn
cdx6500remotepadParamNum3 = _Cdx6500remotepadParamNum3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 6),
    _Cdx6500remotepadParamNum3_Type()
)
cdx6500remotepadParamNum3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum3.setStatus("mandatory")


class _Cdx6500remotepadParamVal3_Type(Integer32):
    """Custom type cdx6500remotepadParamVal3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal3_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal3_Object = MibTableColumn
cdx6500remotepadParamVal3 = _Cdx6500remotepadParamVal3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 7),
    _Cdx6500remotepadParamVal3_Type()
)
cdx6500remotepadParamVal3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal3.setStatus("mandatory")


class _Cdx6500remotepadParamNum4_Type(Integer32):
    """Custom type cdx6500remotepadParamNum4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum4_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum4_Object = MibTableColumn
cdx6500remotepadParamNum4 = _Cdx6500remotepadParamNum4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 8),
    _Cdx6500remotepadParamNum4_Type()
)
cdx6500remotepadParamNum4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum4.setStatus("mandatory")


class _Cdx6500remotepadParamVal4_Type(Integer32):
    """Custom type cdx6500remotepadParamVal4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal4_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal4_Object = MibTableColumn
cdx6500remotepadParamVal4 = _Cdx6500remotepadParamVal4_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 9),
    _Cdx6500remotepadParamVal4_Type()
)
cdx6500remotepadParamVal4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal4.setStatus("mandatory")


class _Cdx6500remotepadParamNum5_Type(Integer32):
    """Custom type cdx6500remotepadParamNum5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum5_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum5_Object = MibTableColumn
cdx6500remotepadParamNum5 = _Cdx6500remotepadParamNum5_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 10),
    _Cdx6500remotepadParamNum5_Type()
)
cdx6500remotepadParamNum5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum5.setStatus("mandatory")


class _Cdx6500remotepadParamVal5_Type(Integer32):
    """Custom type cdx6500remotepadParamVal5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal5_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal5_Object = MibTableColumn
cdx6500remotepadParamVal5 = _Cdx6500remotepadParamVal5_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 11),
    _Cdx6500remotepadParamVal5_Type()
)
cdx6500remotepadParamVal5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal5.setStatus("mandatory")


class _Cdx6500remotepadParamNum6_Type(Integer32):
    """Custom type cdx6500remotepadParamNum6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum6_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum6_Object = MibTableColumn
cdx6500remotepadParamNum6 = _Cdx6500remotepadParamNum6_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 12),
    _Cdx6500remotepadParamNum6_Type()
)
cdx6500remotepadParamNum6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum6.setStatus("mandatory")


class _Cdx6500remotepadParamVal6_Type(Integer32):
    """Custom type cdx6500remotepadParamVal6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal6_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal6_Object = MibTableColumn
cdx6500remotepadParamVal6 = _Cdx6500remotepadParamVal6_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 13),
    _Cdx6500remotepadParamVal6_Type()
)
cdx6500remotepadParamVal6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal6.setStatus("mandatory")


class _Cdx6500remotepadParamNum7_Type(Integer32):
    """Custom type cdx6500remotepadParamNum7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum7_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum7_Object = MibTableColumn
cdx6500remotepadParamNum7 = _Cdx6500remotepadParamNum7_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 14),
    _Cdx6500remotepadParamNum7_Type()
)
cdx6500remotepadParamNum7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum7.setStatus("mandatory")


class _Cdx6500remotepadParamVal7_Type(Integer32):
    """Custom type cdx6500remotepadParamVal7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal7_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal7_Object = MibTableColumn
cdx6500remotepadParamVal7 = _Cdx6500remotepadParamVal7_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 15),
    _Cdx6500remotepadParamVal7_Type()
)
cdx6500remotepadParamVal7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal7.setStatus("mandatory")


class _Cdx6500remotepadParamNum8_Type(Integer32):
    """Custom type cdx6500remotepadParamNum8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum8_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum8_Object = MibTableColumn
cdx6500remotepadParamNum8 = _Cdx6500remotepadParamNum8_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 16),
    _Cdx6500remotepadParamNum8_Type()
)
cdx6500remotepadParamNum8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum8.setStatus("mandatory")


class _Cdx6500remotepadParamVal8_Type(Integer32):
    """Custom type cdx6500remotepadParamVal8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal8_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal8_Object = MibTableColumn
cdx6500remotepadParamVal8 = _Cdx6500remotepadParamVal8_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 17),
    _Cdx6500remotepadParamVal8_Type()
)
cdx6500remotepadParamVal8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal8.setStatus("mandatory")


class _Cdx6500remotepadParamNum9_Type(Integer32):
    """Custom type cdx6500remotepadParamNum9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum9_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum9_Object = MibTableColumn
cdx6500remotepadParamNum9 = _Cdx6500remotepadParamNum9_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 18),
    _Cdx6500remotepadParamNum9_Type()
)
cdx6500remotepadParamNum9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum9.setStatus("mandatory")


class _Cdx6500remotepadParamVal9_Type(Integer32):
    """Custom type cdx6500remotepadParamVal9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal9_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal9_Object = MibTableColumn
cdx6500remotepadParamVal9 = _Cdx6500remotepadParamVal9_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 19),
    _Cdx6500remotepadParamVal9_Type()
)
cdx6500remotepadParamVal9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal9.setStatus("mandatory")


class _Cdx6500remotepadParamNum10_Type(Integer32):
    """Custom type cdx6500remotepadParamNum10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum10_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum10_Object = MibTableColumn
cdx6500remotepadParamNum10 = _Cdx6500remotepadParamNum10_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 20),
    _Cdx6500remotepadParamNum10_Type()
)
cdx6500remotepadParamNum10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum10.setStatus("mandatory")


class _Cdx6500remotepadParamVal10_Type(Integer32):
    """Custom type cdx6500remotepadParamVal10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal10_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal10_Object = MibTableColumn
cdx6500remotepadParamVal10 = _Cdx6500remotepadParamVal10_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 21),
    _Cdx6500remotepadParamVal10_Type()
)
cdx6500remotepadParamVal10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal10.setStatus("mandatory")


class _Cdx6500remotepadParamNum11_Type(Integer32):
    """Custom type cdx6500remotepadParamNum11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum11_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum11_Object = MibTableColumn
cdx6500remotepadParamNum11 = _Cdx6500remotepadParamNum11_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 22),
    _Cdx6500remotepadParamNum11_Type()
)
cdx6500remotepadParamNum11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum11.setStatus("mandatory")


class _Cdx6500remotepadParamVal11_Type(Integer32):
    """Custom type cdx6500remotepadParamVal11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal11_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal11_Object = MibTableColumn
cdx6500remotepadParamVal11 = _Cdx6500remotepadParamVal11_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 23),
    _Cdx6500remotepadParamVal11_Type()
)
cdx6500remotepadParamVal11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal11.setStatus("mandatory")


class _Cdx6500remotepadParamNum12_Type(Integer32):
    """Custom type cdx6500remotepadParamNum12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum12_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum12_Object = MibTableColumn
cdx6500remotepadParamNum12 = _Cdx6500remotepadParamNum12_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 24),
    _Cdx6500remotepadParamNum12_Type()
)
cdx6500remotepadParamNum12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum12.setStatus("mandatory")


class _Cdx6500remotepadParamVal12_Type(Integer32):
    """Custom type cdx6500remotepadParamVal12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal12_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal12_Object = MibTableColumn
cdx6500remotepadParamVal12 = _Cdx6500remotepadParamVal12_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 25),
    _Cdx6500remotepadParamVal12_Type()
)
cdx6500remotepadParamVal12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal12.setStatus("mandatory")


class _Cdx6500remotepadParamNum13_Type(Integer32):
    """Custom type cdx6500remotepadParamNum13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum13_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum13_Object = MibTableColumn
cdx6500remotepadParamNum13 = _Cdx6500remotepadParamNum13_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 26),
    _Cdx6500remotepadParamNum13_Type()
)
cdx6500remotepadParamNum13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum13.setStatus("mandatory")


class _Cdx6500remotepadParamVal13_Type(Integer32):
    """Custom type cdx6500remotepadParamVal13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal13_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal13_Object = MibTableColumn
cdx6500remotepadParamVal13 = _Cdx6500remotepadParamVal13_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 27),
    _Cdx6500remotepadParamVal13_Type()
)
cdx6500remotepadParamVal13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal13.setStatus("mandatory")


class _Cdx6500remotepadParamNum14_Type(Integer32):
    """Custom type cdx6500remotepadParamNum14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum14_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum14_Object = MibTableColumn
cdx6500remotepadParamNum14 = _Cdx6500remotepadParamNum14_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 28),
    _Cdx6500remotepadParamNum14_Type()
)
cdx6500remotepadParamNum14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum14.setStatus("mandatory")


class _Cdx6500remotepadParamVal14_Type(Integer32):
    """Custom type cdx6500remotepadParamVal14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal14_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal14_Object = MibTableColumn
cdx6500remotepadParamVal14 = _Cdx6500remotepadParamVal14_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 29),
    _Cdx6500remotepadParamVal14_Type()
)
cdx6500remotepadParamVal14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal14.setStatus("mandatory")


class _Cdx6500remotepadParamNum15_Type(Integer32):
    """Custom type cdx6500remotepadParamNum15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum15_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum15_Object = MibTableColumn
cdx6500remotepadParamNum15 = _Cdx6500remotepadParamNum15_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 30),
    _Cdx6500remotepadParamNum15_Type()
)
cdx6500remotepadParamNum15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum15.setStatus("mandatory")


class _Cdx6500remotepadParamVal15_Type(Integer32):
    """Custom type cdx6500remotepadParamVal15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal15_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal15_Object = MibTableColumn
cdx6500remotepadParamVal15 = _Cdx6500remotepadParamVal15_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 31),
    _Cdx6500remotepadParamVal15_Type()
)
cdx6500remotepadParamVal15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal15.setStatus("mandatory")


class _Cdx6500remotepadParamNum16_Type(Integer32):
    """Custom type cdx6500remotepadParamNum16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum16_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum16_Object = MibTableColumn
cdx6500remotepadParamNum16 = _Cdx6500remotepadParamNum16_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 32),
    _Cdx6500remotepadParamNum16_Type()
)
cdx6500remotepadParamNum16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum16.setStatus("mandatory")


class _Cdx6500remotepadParamVal16_Type(Integer32):
    """Custom type cdx6500remotepadParamVal16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal16_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal16_Object = MibTableColumn
cdx6500remotepadParamVal16 = _Cdx6500remotepadParamVal16_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 33),
    _Cdx6500remotepadParamVal16_Type()
)
cdx6500remotepadParamVal16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal16.setStatus("mandatory")


class _Cdx6500remotepadParamNum17_Type(Integer32):
    """Custom type cdx6500remotepadParamNum17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum17_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum17_Object = MibTableColumn
cdx6500remotepadParamNum17 = _Cdx6500remotepadParamNum17_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 34),
    _Cdx6500remotepadParamNum17_Type()
)
cdx6500remotepadParamNum17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum17.setStatus("mandatory")


class _Cdx6500remotepadParamVal17_Type(Integer32):
    """Custom type cdx6500remotepadParamVal17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal17_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal17_Object = MibTableColumn
cdx6500remotepadParamVal17 = _Cdx6500remotepadParamVal17_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 35),
    _Cdx6500remotepadParamVal17_Type()
)
cdx6500remotepadParamVal17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal17.setStatus("mandatory")


class _Cdx6500remotepadParamNum18_Type(Integer32):
    """Custom type cdx6500remotepadParamNum18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum18_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum18_Object = MibTableColumn
cdx6500remotepadParamNum18 = _Cdx6500remotepadParamNum18_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 36),
    _Cdx6500remotepadParamNum18_Type()
)
cdx6500remotepadParamNum18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum18.setStatus("mandatory")


class _Cdx6500remotepadParamVal18_Type(Integer32):
    """Custom type cdx6500remotepadParamVal18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal18_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal18_Object = MibTableColumn
cdx6500remotepadParamVal18 = _Cdx6500remotepadParamVal18_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 37),
    _Cdx6500remotepadParamVal18_Type()
)
cdx6500remotepadParamVal18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal18.setStatus("mandatory")


class _Cdx6500remotepadParamNum19_Type(Integer32):
    """Custom type cdx6500remotepadParamNum19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum19_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum19_Object = MibTableColumn
cdx6500remotepadParamNum19 = _Cdx6500remotepadParamNum19_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 38),
    _Cdx6500remotepadParamNum19_Type()
)
cdx6500remotepadParamNum19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum19.setStatus("mandatory")


class _Cdx6500remotepadParamVal19_Type(Integer32):
    """Custom type cdx6500remotepadParamVal19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal19_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal19_Object = MibTableColumn
cdx6500remotepadParamVal19 = _Cdx6500remotepadParamVal19_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 39),
    _Cdx6500remotepadParamVal19_Type()
)
cdx6500remotepadParamVal19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal19.setStatus("mandatory")


class _Cdx6500remotepadParamNum20_Type(Integer32):
    """Custom type cdx6500remotepadParamNum20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum20_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum20_Object = MibTableColumn
cdx6500remotepadParamNum20 = _Cdx6500remotepadParamNum20_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 40),
    _Cdx6500remotepadParamNum20_Type()
)
cdx6500remotepadParamNum20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum20.setStatus("mandatory")


class _Cdx6500remotepadParamVal20_Type(Integer32):
    """Custom type cdx6500remotepadParamVal20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal20_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal20_Object = MibTableColumn
cdx6500remotepadParamVal20 = _Cdx6500remotepadParamVal20_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 41),
    _Cdx6500remotepadParamVal20_Type()
)
cdx6500remotepadParamVal20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal20.setStatus("mandatory")


class _Cdx6500remotepadParamNum21_Type(Integer32):
    """Custom type cdx6500remotepadParamNum21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum21_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum21_Object = MibTableColumn
cdx6500remotepadParamNum21 = _Cdx6500remotepadParamNum21_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 42),
    _Cdx6500remotepadParamNum21_Type()
)
cdx6500remotepadParamNum21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum21.setStatus("mandatory")


class _Cdx6500remotepadParamVal21_Type(Integer32):
    """Custom type cdx6500remotepadParamVal21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal21_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal21_Object = MibTableColumn
cdx6500remotepadParamVal21 = _Cdx6500remotepadParamVal21_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 43),
    _Cdx6500remotepadParamVal21_Type()
)
cdx6500remotepadParamVal21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal21.setStatus("mandatory")


class _Cdx6500remotepadParamNum22_Type(Integer32):
    """Custom type cdx6500remotepadParamNum22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Cdx6500remotepadParamNum22_Type.__name__ = "Integer32"
_Cdx6500remotepadParamNum22_Object = MibTableColumn
cdx6500remotepadParamNum22 = _Cdx6500remotepadParamNum22_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 44),
    _Cdx6500remotepadParamNum22_Type()
)
cdx6500remotepadParamNum22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamNum22.setStatus("mandatory")


class _Cdx6500remotepadParamVal22_Type(Integer32):
    """Custom type cdx6500remotepadParamVal22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500remotepadParamVal22_Type.__name__ = "Integer32"
_Cdx6500remotepadParamVal22_Object = MibTableColumn
cdx6500remotepadParamVal22 = _Cdx6500remotepadParamVal22_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 9, 1, 45),
    _Cdx6500remotepadParamVal22_Type()
)
cdx6500remotepadParamVal22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500remotepadParamVal22.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PPSTPadPortTable_Object = MibTable
cdx6500PPSTPadPortTable = _Cdx6500PPSTPadPortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPSTPadPortTable.setStatus("mandatory")
_Cdx6500PPSTPadPortEntry_Object = MibTableRow
cdx6500PPSTPadPortEntry = _Cdx6500PPSTPadPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1)
)
cdx6500PPSTPadPortEntry.setIndexNames(
    (0, "PAD-OPT-MIB", "cdx6500padpStatPortNum"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTPadPortEntry.setStatus("mandatory")


class _Cdx6500padpStatPortNum_Type(Integer32):
    """Custom type cdx6500padpStatPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )


_Cdx6500padpStatPortNum_Type.__name__ = "Integer32"
_Cdx6500padpStatPortNum_Object = MibTableColumn
cdx6500padpStatPortNum = _Cdx6500padpStatPortNum_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 1),
    _Cdx6500padpStatPortNum_Type()
)
cdx6500padpStatPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPortNum.setStatus("mandatory")


class _Cdx6500padpStatPortStatus_Type(Integer32):
    """Custom type cdx6500padpStatPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              50)
        )
    )
    namedValues = NamedValues(
        *(("busyout", 2),
          ("disabled", 0),
          ("newvalDisabled", 50),
          ("up", 3))
    )


_Cdx6500padpStatPortStatus_Type.__name__ = "Integer32"
_Cdx6500padpStatPortStatus_Object = MibTableColumn
cdx6500padpStatPortStatus = _Cdx6500padpStatPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 2),
    _Cdx6500padpStatPortStatus_Type()
)
cdx6500padpStatPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPortStatus.setStatus("mandatory")


class _Cdx6500padpStatUtilizationIn_Type(Integer32):
    """Custom type cdx6500padpStatUtilizationIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500padpStatUtilizationIn_Type.__name__ = "Integer32"
_Cdx6500padpStatUtilizationIn_Object = MibTableColumn
cdx6500padpStatUtilizationIn = _Cdx6500padpStatUtilizationIn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 3),
    _Cdx6500padpStatUtilizationIn_Type()
)
cdx6500padpStatUtilizationIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatUtilizationIn.setStatus("mandatory")


class _Cdx6500padpStatUtilizationOut_Type(Integer32):
    """Custom type cdx6500padpStatUtilizationOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500padpStatUtilizationOut_Type.__name__ = "Integer32"
_Cdx6500padpStatUtilizationOut_Object = MibTableColumn
cdx6500padpStatUtilizationOut = _Cdx6500padpStatUtilizationOut_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 4),
    _Cdx6500padpStatUtilizationOut_Type()
)
cdx6500padpStatUtilizationOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatUtilizationOut.setStatus("mandatory")
_Cdx6500padpStatPortSpeed_Type = Integer32
_Cdx6500padpStatPortSpeed_Object = MibTableColumn
cdx6500padpStatPortSpeed = _Cdx6500padpStatPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 5),
    _Cdx6500padpStatPortSpeed_Type()
)
cdx6500padpStatPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPortSpeed.setStatus("mandatory")
_Cdx6500padpStatCharInTotal_Type = Counter32
_Cdx6500padpStatCharInTotal_Object = MibTableColumn
cdx6500padpStatCharInTotal = _Cdx6500padpStatCharInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 6),
    _Cdx6500padpStatCharInTotal_Type()
)
cdx6500padpStatCharInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatCharInTotal.setStatus("mandatory")
_Cdx6500padpStatCharOutTotal_Type = Counter32
_Cdx6500padpStatCharOutTotal_Object = MibTableColumn
cdx6500padpStatCharOutTotal = _Cdx6500padpStatCharOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 7),
    _Cdx6500padpStatCharOutTotal_Type()
)
cdx6500padpStatCharOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatCharOutTotal.setStatus("mandatory")
_Cdx6500padpStatCharsInPerSec_Type = Integer32
_Cdx6500padpStatCharsInPerSec_Object = MibTableColumn
cdx6500padpStatCharsInPerSec = _Cdx6500padpStatCharsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 8),
    _Cdx6500padpStatCharsInPerSec_Type()
)
cdx6500padpStatCharsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatCharsInPerSec.setStatus("mandatory")
_Cdx6500padpStatCharsOutPerSec_Type = Integer32
_Cdx6500padpStatCharsOutPerSec_Object = MibTableColumn
cdx6500padpStatCharsOutPerSec = _Cdx6500padpStatCharsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 9),
    _Cdx6500padpStatCharsOutPerSec_Type()
)
cdx6500padpStatCharsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatCharsOutPerSec.setStatus("mandatory")
_Cdx6500padpStatPktInTotal_Type = Counter32
_Cdx6500padpStatPktInTotal_Object = MibTableColumn
cdx6500padpStatPktInTotal = _Cdx6500padpStatPktInTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 10),
    _Cdx6500padpStatPktInTotal_Type()
)
cdx6500padpStatPktInTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPktInTotal.setStatus("mandatory")
_Cdx6500padpStatPktOutTotal_Type = Counter32
_Cdx6500padpStatPktOutTotal_Object = MibTableColumn
cdx6500padpStatPktOutTotal = _Cdx6500padpStatPktOutTotal_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 11),
    _Cdx6500padpStatPktOutTotal_Type()
)
cdx6500padpStatPktOutTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPktOutTotal.setStatus("mandatory")
_Cdx6500padpStatPktsInPerSec_Type = Integer32
_Cdx6500padpStatPktsInPerSec_Object = MibTableColumn
cdx6500padpStatPktsInPerSec = _Cdx6500padpStatPktsInPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 12),
    _Cdx6500padpStatPktsInPerSec_Type()
)
cdx6500padpStatPktsInPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPktsInPerSec.setStatus("mandatory")
_Cdx6500padpStatPktsOutPerSec_Type = Integer32
_Cdx6500padpStatPktsOutPerSec_Object = MibTableColumn
cdx6500padpStatPktsOutPerSec = _Cdx6500padpStatPktsOutPerSec_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 13),
    _Cdx6500padpStatPktsOutPerSec_Type()
)
cdx6500padpStatPktsOutPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPktsOutPerSec.setStatus("mandatory")
_Cdx6500padpStatPktsQueued_Type = Integer32
_Cdx6500padpStatPktsQueued_Object = MibTableColumn
cdx6500padpStatPktsQueued = _Cdx6500padpStatPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 14),
    _Cdx6500padpStatPktsQueued_Type()
)
cdx6500padpStatPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPktsQueued.setStatus("mandatory")
_Cdx6500padpStatOverrunErrors_Type = Counter16
_Cdx6500padpStatOverrunErrors_Object = MibTableColumn
cdx6500padpStatOverrunErrors = _Cdx6500padpStatOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 15),
    _Cdx6500padpStatOverrunErrors_Type()
)
cdx6500padpStatOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatOverrunErrors.setStatus("mandatory")
_Cdx6500padpStatParityErrors_Type = Counter16
_Cdx6500padpStatParityErrors_Object = MibTableColumn
cdx6500padpStatParityErrors = _Cdx6500padpStatParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 16),
    _Cdx6500padpStatParityErrors_Type()
)
cdx6500padpStatParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatParityErrors.setStatus("mandatory")
_Cdx6500padpStatFramingErrors_Type = Counter16
_Cdx6500padpStatFramingErrors_Object = MibTableColumn
cdx6500padpStatFramingErrors = _Cdx6500padpStatFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 17),
    _Cdx6500padpStatFramingErrors_Type()
)
cdx6500padpStatFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatFramingErrors.setStatus("mandatory")


class _Cdx6500padpStatCurrentStatus_Type(DisplayString):
    """Custom type cdx6500padpStatCurrentStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 10),
    )


_Cdx6500padpStatCurrentStatus_Type.__name__ = "DisplayString"
_Cdx6500padpStatCurrentStatus_Object = MibTableColumn
cdx6500padpStatCurrentStatus = _Cdx6500padpStatCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 18),
    _Cdx6500padpStatCurrentStatus_Type()
)
cdx6500padpStatCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatCurrentStatus.setStatus("mandatory")


class _Cdx6500padpStatPortState_Type(Integer32):
    """Custom type cdx6500padpStatPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              50,
              100)
        )
    )
    namedValues = NamedValues(
        *(("account", 3),
          ("na", 100),
          ("newvalPad", 50),
          ("pad", 0),
          ("password", 5),
          ("x28", 1))
    )


_Cdx6500padpStatPortState_Type.__name__ = "Integer32"
_Cdx6500padpStatPortState_Object = MibTableColumn
cdx6500padpStatPortState = _Cdx6500padpStatPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 1, 1, 19),
    _Cdx6500padpStatPortState_Type()
)
cdx6500padpStatPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500padpStatPortState.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAD-OPT-MIB",
    **{"Counter16": Counter16,
       "DisplayString": DisplayString,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PPCTPadPortTable": cdx6500PPCTPadPortTable,
       "cdx6500PPCTPadPortEntry": cdx6500PPCTPadPortEntry,
       "cdx6500padpCfgPortNum": cdx6500padpCfgPortNum,
       "cdx6500padpCfgConnectionType": cdx6500padpCfgConnectionType,
       "cdx6500padpCfgPortControl": cdx6500padpCfgPortControl,
       "cdx6500padpCfgPortSpeed": cdx6500padpCfgPortSpeed,
       "cdx6500padpCfgAutoBaudSeq": cdx6500padpCfgAutoBaudSeq,
       "cdx6500padpCfgDataBits": cdx6500padpCfgDataBits,
       "cdx6500padpCfgParity": cdx6500padpCfgParity,
       "cdx6500padpCfgStopBits": cdx6500padpCfgStopBits,
       "cdx6500padpCfgProfileName": cdx6500padpCfgProfileName,
       "cdx6500padpCfgCallControl": cdx6500padpCfgCallControl,
       "cdx6500padpCfgTermControl": cdx6500padpCfgTermControl,
       "cdx6500padpCfgPadPromptNum": cdx6500padpCfgPadPromptNum,
       "cdx6500padpCfgRemoteParamNum": cdx6500padpCfgRemoteParamNum,
       "cdx6500padpCfgAutoCallMnem": cdx6500padpCfgAutoCallMnem,
       "cdx6500padpCfgAutoCallTimeout": cdx6500padpCfgAutoCallTimeout,
       "cdx6500padpCfgMaxAutoCall": cdx6500padpCfgMaxAutoCall,
       "cdx6500padpCfgSubAddress": cdx6500padpCfgSubAddress,
       "cdx6500padpCfgGroupSubaddress": cdx6500padpCfgGroupSubaddress,
       "cdx6500padpCfgCugMembership": cdx6500padpCfgCugMembership,
       "cdx6500padpCfgBillingRecord": cdx6500padpCfgBillingRecord,
       "cdx6500padpCfgInviteToClr": cdx6500padpCfgInviteToClr,
       "cdx6500padpCfgCallAcceptTime": cdx6500padpCfgCallAcceptTime,
       "cdx6500padpCfgProtectionLevel": cdx6500padpCfgProtectionLevel,
       "cdx6500padpCfgReconnectTimeout": cdx6500padpCfgReconnectTimeout,
       "cdx6500padpCfgReconnectTries": cdx6500padpCfgReconnectTries,
       "cdx6500padpCfgMaxRcvBufLength": cdx6500padpCfgMaxRcvBufLength,
       "cdx6500padpCfgCommandLanguage": cdx6500padpCfgCommandLanguage,
       "cdx6500padpCfgNUIFacilityFormat": cdx6500padpCfgNUIFacilityFormat,
       "cdx6500padpCfgNUIVerifyTimer": cdx6500padpCfgNUIVerifyTimer,
       "cdx6500padpCfgMaxNUIViolations": cdx6500padpCfgMaxNUIViolations,
       "cdx6500padpCfgActionTypeNUIV": cdx6500padpCfgActionTypeNUIV,
       "cdx6500padpCfgCalledDTEAddress": cdx6500padpCfgCalledDTEAddress,
       "cdx6500padpCfgCallingDTEIdent": cdx6500padpCfgCallingDTEIdent,
       "cdx6500padpCfgCallingDTEPasswd": cdx6500padpCfgCallingDTEPasswd,
       "cdx6500padpCfgX28ResetService": cdx6500padpCfgX28ResetService,
       "cdx6500padpCfgX28ClearService": cdx6500padpCfgX28ClearService,
       "cdx6500padpCfgMAXMNEMFailures": cdx6500padpCfgMAXMNEMFailures,
       "cdx6500padpCfgActionTypeMNEMFail": cdx6500padpCfgActionTypeMNEMFail,
       "cdx6500padpCfgActiveLineMessage": cdx6500padpCfgActiveLineMessage,
       "cdx6500padpCfgDelayActiveLine": cdx6500padpCfgDelayActiveLine,
       "cdx6500padpCfgInterCharTimer": cdx6500padpCfgInterCharTimer,
       "cdx6500padpCfgElectricalInterfaceType": cdx6500padpCfgElectricalInterfaceType,
       "cdx6500padpCfgV24ElectricalInterfaceOption": cdx6500padpCfgV24ElectricalInterfaceOption,
       "cdx6500padpCfgHighSpeedElectricalInterfaceOption": cdx6500padpCfgHighSpeedElectricalInterfaceOption,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500CfgPadPromptTable": cdx6500CfgPadPromptTable,
       "cdx6500CfgPadPromptEntry": cdx6500CfgPadPromptEntry,
       "cdx6500padpromptEntryNum": cdx6500padpromptEntryNum,
       "cdx6500padpromptPromptText": cdx6500padpromptPromptText,
       "cdx6500CfgPadProfileTable": cdx6500CfgPadProfileTable,
       "cdx6500CfgPadProfileEntry": cdx6500CfgPadProfileEntry,
       "cdx6500padprofProfileNum": cdx6500padprofProfileNum,
       "cdx6500padprofProfileName": cdx6500padprofProfileName,
       "cdx6500padprofPar1": cdx6500padprofPar1,
       "cdx6500padprofPar2": cdx6500padprofPar2,
       "cdx6500padprofPar3": cdx6500padprofPar3,
       "cdx6500padprofPar4": cdx6500padprofPar4,
       "cdx6500padprofPar5": cdx6500padprofPar5,
       "cdx6500padprofPar6": cdx6500padprofPar6,
       "cdx6500padprofPar7": cdx6500padprofPar7,
       "cdx6500padprofPar9": cdx6500padprofPar9,
       "cdx6500padprofPar10": cdx6500padprofPar10,
       "cdx6500padprofPar12": cdx6500padprofPar12,
       "cdx6500padprofPar13": cdx6500padprofPar13,
       "cdx6500padprofPar14": cdx6500padprofPar14,
       "cdx6500padprofPar15": cdx6500padprofPar15,
       "cdx6500padprofPar16": cdx6500padprofPar16,
       "cdx6500padprofPar17": cdx6500padprofPar17,
       "cdx6500padprofPar18": cdx6500padprofPar18,
       "cdx6500padprofPar19": cdx6500padprofPar19,
       "cdx6500padprofPar20": cdx6500padprofPar20,
       "cdx6500padprofPar21": cdx6500padprofPar21,
       "cdx6500padprofPar22": cdx6500padprofPar22,
       "cdx6500padprofPar100": cdx6500padprofPar100,
       "cdx6500padprofPar101": cdx6500padprofPar101,
       "cdx6500padprofPar102": cdx6500padprofPar102,
       "cdx6500padprofPar103": cdx6500padprofPar103,
       "cdx6500padprofPar104": cdx6500padprofPar104,
       "cdx6500padprofPar105": cdx6500padprofPar105,
       "cdx6500padprofPar106": cdx6500padprofPar106,
       "cdx6500padprofPar107": cdx6500padprofPar107,
       "cdx6500padprofPar108": cdx6500padprofPar108,
       "cdx6500padprofPar109": cdx6500padprofPar109,
       "cdx6500padprofPar110": cdx6500padprofPar110,
       "cdx6500padprofPar111": cdx6500padprofPar111,
       "cdx6500padprofPar112": cdx6500padprofPar112,
       "cdx6500padprofPar113": cdx6500padprofPar113,
       "cdx6500padprofPar114": cdx6500padprofPar114,
       "cdx6500padprofPar115": cdx6500padprofPar115,
       "cdx6500padprofPar116": cdx6500padprofPar116,
       "cdx6500padprofPar117": cdx6500padprofPar117,
       "cdx6500padprofPar118": cdx6500padprofPar118,
       "cdx6500padprofPar119": cdx6500padprofPar119,
       "cdx6500CfgRemotePadTable": cdx6500CfgRemotePadTable,
       "cdx6500CfgRemotePadEntry": cdx6500CfgRemotePadEntry,
       "cdx6500remotepadEntryNum": cdx6500remotepadEntryNum,
       "cdx6500remotepadParamNum1": cdx6500remotepadParamNum1,
       "cdx6500remotepadParamVal1": cdx6500remotepadParamVal1,
       "cdx6500remotepadParamNum2": cdx6500remotepadParamNum2,
       "cdx6500remotepadParamVal2": cdx6500remotepadParamVal2,
       "cdx6500remotepadParamNum3": cdx6500remotepadParamNum3,
       "cdx6500remotepadParamVal3": cdx6500remotepadParamVal3,
       "cdx6500remotepadParamNum4": cdx6500remotepadParamNum4,
       "cdx6500remotepadParamVal4": cdx6500remotepadParamVal4,
       "cdx6500remotepadParamNum5": cdx6500remotepadParamNum5,
       "cdx6500remotepadParamVal5": cdx6500remotepadParamVal5,
       "cdx6500remotepadParamNum6": cdx6500remotepadParamNum6,
       "cdx6500remotepadParamVal6": cdx6500remotepadParamVal6,
       "cdx6500remotepadParamNum7": cdx6500remotepadParamNum7,
       "cdx6500remotepadParamVal7": cdx6500remotepadParamVal7,
       "cdx6500remotepadParamNum8": cdx6500remotepadParamNum8,
       "cdx6500remotepadParamVal8": cdx6500remotepadParamVal8,
       "cdx6500remotepadParamNum9": cdx6500remotepadParamNum9,
       "cdx6500remotepadParamVal9": cdx6500remotepadParamVal9,
       "cdx6500remotepadParamNum10": cdx6500remotepadParamNum10,
       "cdx6500remotepadParamVal10": cdx6500remotepadParamVal10,
       "cdx6500remotepadParamNum11": cdx6500remotepadParamNum11,
       "cdx6500remotepadParamVal11": cdx6500remotepadParamVal11,
       "cdx6500remotepadParamNum12": cdx6500remotepadParamNum12,
       "cdx6500remotepadParamVal12": cdx6500remotepadParamVal12,
       "cdx6500remotepadParamNum13": cdx6500remotepadParamNum13,
       "cdx6500remotepadParamVal13": cdx6500remotepadParamVal13,
       "cdx6500remotepadParamNum14": cdx6500remotepadParamNum14,
       "cdx6500remotepadParamVal14": cdx6500remotepadParamVal14,
       "cdx6500remotepadParamNum15": cdx6500remotepadParamNum15,
       "cdx6500remotepadParamVal15": cdx6500remotepadParamVal15,
       "cdx6500remotepadParamNum16": cdx6500remotepadParamNum16,
       "cdx6500remotepadParamVal16": cdx6500remotepadParamVal16,
       "cdx6500remotepadParamNum17": cdx6500remotepadParamNum17,
       "cdx6500remotepadParamVal17": cdx6500remotepadParamVal17,
       "cdx6500remotepadParamNum18": cdx6500remotepadParamNum18,
       "cdx6500remotepadParamVal18": cdx6500remotepadParamVal18,
       "cdx6500remotepadParamNum19": cdx6500remotepadParamNum19,
       "cdx6500remotepadParamVal19": cdx6500remotepadParamVal19,
       "cdx6500remotepadParamNum20": cdx6500remotepadParamNum20,
       "cdx6500remotepadParamVal20": cdx6500remotepadParamVal20,
       "cdx6500remotepadParamNum21": cdx6500remotepadParamNum21,
       "cdx6500remotepadParamVal21": cdx6500remotepadParamVal21,
       "cdx6500remotepadParamNum22": cdx6500remotepadParamNum22,
       "cdx6500remotepadParamVal22": cdx6500remotepadParamVal22,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PPSTPadPortTable": cdx6500PPSTPadPortTable,
       "cdx6500PPSTPadPortEntry": cdx6500PPSTPadPortEntry,
       "cdx6500padpStatPortNum": cdx6500padpStatPortNum,
       "cdx6500padpStatPortStatus": cdx6500padpStatPortStatus,
       "cdx6500padpStatUtilizationIn": cdx6500padpStatUtilizationIn,
       "cdx6500padpStatUtilizationOut": cdx6500padpStatUtilizationOut,
       "cdx6500padpStatPortSpeed": cdx6500padpStatPortSpeed,
       "cdx6500padpStatCharInTotal": cdx6500padpStatCharInTotal,
       "cdx6500padpStatCharOutTotal": cdx6500padpStatCharOutTotal,
       "cdx6500padpStatCharsInPerSec": cdx6500padpStatCharsInPerSec,
       "cdx6500padpStatCharsOutPerSec": cdx6500padpStatCharsOutPerSec,
       "cdx6500padpStatPktInTotal": cdx6500padpStatPktInTotal,
       "cdx6500padpStatPktOutTotal": cdx6500padpStatPktOutTotal,
       "cdx6500padpStatPktsInPerSec": cdx6500padpStatPktsInPerSec,
       "cdx6500padpStatPktsOutPerSec": cdx6500padpStatPktsOutPerSec,
       "cdx6500padpStatPktsQueued": cdx6500padpStatPktsQueued,
       "cdx6500padpStatOverrunErrors": cdx6500padpStatOverrunErrors,
       "cdx6500padpStatParityErrors": cdx6500padpStatParityErrors,
       "cdx6500padpStatFramingErrors": cdx6500padpStatFramingErrors,
       "cdx6500padpStatCurrentStatus": cdx6500padpStatCurrentStatus,
       "cdx6500padpStatPortState": cdx6500padpStatPortState,
       "cdx6500Controls": cdx6500Controls}
)
