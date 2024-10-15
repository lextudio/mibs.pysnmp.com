# SNMP MIB module (IDT1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IDT1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:09 2024
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
 experimental,
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
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_Idt1_ObjectIdentity = ObjectIdentity
idt1 = _Idt1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 15)
)
_Idt1Cfg_ObjectIdentity = ObjectIdentity
idt1Cfg = _Idt1Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1)
)
_Idt1CfgTable_Object = MibTable
idt1CfgTable = _Idt1CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    idt1CfgTable.setStatus("mandatory")
_Idt1CfgEntry_Object = MibTableRow
idt1CfgEntry = _Idt1CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1)
)
idt1CfgEntry.setIndexNames(
    (0, "IDT1-MIB", "idt1CfgIndex"),
)
if mibBuilder.loadTexts:
    idt1CfgEntry.setStatus("mandatory")
_Idt1CfgIndex_Type = Integer32
_Idt1CfgIndex_Object = MibTableColumn
idt1CfgIndex = _Idt1CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 1),
    _Idt1CfgIndex_Type()
)
idt1CfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1CfgIndex.setStatus("mandatory")


class _Idt1CfgAssgndISDNGateway_Type(Integer32):
    """Custom type idt1CfgAssgndISDNGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Idt1CfgAssgndISDNGateway_Type.__name__ = "Integer32"
_Idt1CfgAssgndISDNGateway_Object = MibTableColumn
idt1CfgAssgndISDNGateway = _Idt1CfgAssgndISDNGateway_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 2),
    _Idt1CfgAssgndISDNGateway_Type()
)
idt1CfgAssgndISDNGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgAssgndISDNGateway.setStatus("mandatory")


class _Idt1CfgMdmCallsAllowedEna_Type(Integer32):
    """Custom type idt1CfgMdmCallsAllowedEna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Idt1CfgMdmCallsAllowedEna_Type.__name__ = "Integer32"
_Idt1CfgMdmCallsAllowedEna_Object = MibTableColumn
idt1CfgMdmCallsAllowedEna = _Idt1CfgMdmCallsAllowedEna_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 3),
    _Idt1CfgMdmCallsAllowedEna_Type()
)
idt1CfgMdmCallsAllowedEna.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgMdmCallsAllowedEna.setStatus("mandatory")


class _Idt1CfgMdmRoutingMethod_Type(Integer32):
    """Custom type idt1CfgMdmRoutingMethod based on Integer32"""
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
        *(("firstAvailable", 3),
          ("fixedAssignment", 4),
          ("notSupported", 1),
          ("roundRobin", 2))
    )


_Idt1CfgMdmRoutingMethod_Type.__name__ = "Integer32"
_Idt1CfgMdmRoutingMethod_Object = MibTableColumn
idt1CfgMdmRoutingMethod = _Idt1CfgMdmRoutingMethod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 4),
    _Idt1CfgMdmRoutingMethod_Type()
)
idt1CfgMdmRoutingMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgMdmRoutingMethod.setStatus("mandatory")


class _Idt1CfgProjectSelectionR2_Type(Integer32):
    """Custom type idt1CfgProjectSelectionR2 based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 255),
          ("p7", 4),
          ("q421", 1),
          ("r2", 2),
          ("r2Brazil", 6),
          ("r2China", 8),
          ("r2Korea", 3),
          ("r2LME", 9),
          ("r2Malaysia", 5),
          ("r2Mexico", 7),
          ("r2Venezuela", 10))
    )


_Idt1CfgProjectSelectionR2_Type.__name__ = "Integer32"
_Idt1CfgProjectSelectionR2_Object = MibTableColumn
idt1CfgProjectSelectionR2 = _Idt1CfgProjectSelectionR2_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 5),
    _Idt1CfgProjectSelectionR2_Type()
)
idt1CfgProjectSelectionR2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgProjectSelectionR2.setStatus("mandatory")


class _Idt1CfgInfoMsgTimeOut_Type(Integer32):
    """Custom type idt1CfgInfoMsgTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Idt1CfgInfoMsgTimeOut_Type.__name__ = "Integer32"
_Idt1CfgInfoMsgTimeOut_Object = MibTableColumn
idt1CfgInfoMsgTimeOut = _Idt1CfgInfoMsgTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 6),
    _Idt1CfgInfoMsgTimeOut_Type()
)
idt1CfgInfoMsgTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgInfoMsgTimeOut.setStatus("mandatory")


class _Idt1CfgInbDNISLength_Type(Integer32):
    """Custom type idt1CfgInbDNISLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Idt1CfgInbDNISLength_Type.__name__ = "Integer32"
_Idt1CfgInbDNISLength_Object = MibTableColumn
idt1CfgInbDNISLength = _Idt1CfgInbDNISLength_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 7),
    _Idt1CfgInbDNISLength_Type()
)
idt1CfgInbDNISLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgInbDNISLength.setStatus("mandatory")


class _Idt1CfgSelectCompanding_Type(Integer32):
    """Custom type idt1CfgSelectCompanding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 1),
          ("ulaw", 2),
          ("useCountryCode", 3))
    )


_Idt1CfgSelectCompanding_Type.__name__ = "Integer32"
_Idt1CfgSelectCompanding_Object = MibTableColumn
idt1CfgSelectCompanding = _Idt1CfgSelectCompanding_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 8),
    _Idt1CfgSelectCompanding_Type()
)
idt1CfgSelectCompanding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgSelectCompanding.setStatus("mandatory")


class _Idt1CfgAniNumberEnable_Type(Integer32):
    """Custom type idt1CfgAniNumberEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_Idt1CfgAniNumberEnable_Type.__name__ = "Integer32"
_Idt1CfgAniNumberEnable_Object = MibTableColumn
idt1CfgAniNumberEnable = _Idt1CfgAniNumberEnable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 9),
    _Idt1CfgAniNumberEnable_Type()
)
idt1CfgAniNumberEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgAniNumberEnable.setStatus("mandatory")


class _Idt1CfgNoBptyMethod_Type(Integer32):
    """Custom type idt1CfgNoBptyMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 1),
          ("digital", 2),
          ("unAllocatedNum", 3))
    )


_Idt1CfgNoBptyMethod_Type.__name__ = "Integer32"
_Idt1CfgNoBptyMethod_Object = MibTableColumn
idt1CfgNoBptyMethod = _Idt1CfgNoBptyMethod_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 10),
    _Idt1CfgNoBptyMethod_Type()
)
idt1CfgNoBptyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgNoBptyMethod.setStatus("mandatory")


class _Idt1CfgMaxISDNGwyCalls_Type(Integer32):
    """Custom type idt1CfgMaxISDNGwyCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Idt1CfgMaxISDNGwyCalls_Type.__name__ = "Integer32"
_Idt1CfgMaxISDNGwyCalls_Object = MibTableColumn
idt1CfgMaxISDNGwyCalls = _Idt1CfgMaxISDNGwyCalls_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 1, 1, 1, 11),
    _Idt1CfgMaxISDNGwyCalls_Type()
)
idt1CfgMaxISDNGwyCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CfgMaxISDNGwyCalls.setStatus("mandatory")
_Idt1Cr_ObjectIdentity = ObjectIdentity
idt1Cr = _Idt1Cr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 2)
)
_Idt1CrTable_Object = MibTable
idt1CrTable = _Idt1CrTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1)
)
if mibBuilder.loadTexts:
    idt1CrTable.setStatus("mandatory")
_Idt1CrEntry_Object = MibTableRow
idt1CrEntry = _Idt1CrEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1)
)
idt1CrEntry.setIndexNames(
    (0, "IDT1-MIB", "idt1CrIndex"),
    (0, "IDT1-MIB", "idt1CrPhNumIndex"),
)
if mibBuilder.loadTexts:
    idt1CrEntry.setStatus("mandatory")
_Idt1CrIndex_Type = Integer32
_Idt1CrIndex_Object = MibTableColumn
idt1CrIndex = _Idt1CrIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 1),
    _Idt1CrIndex_Type()
)
idt1CrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1CrIndex.setStatus("mandatory")
_Idt1CrPhNumIndex_Type = Integer32
_Idt1CrPhNumIndex_Object = MibTableColumn
idt1CrPhNumIndex = _Idt1CrPhNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 2),
    _Idt1CrPhNumIndex_Type()
)
idt1CrPhNumIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1CrPhNumIndex.setStatus("mandatory")


class _Idt1CrInboundPhNum_Type(DisplayString):
    """Custom type idt1CrInboundPhNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_Idt1CrInboundPhNum_Type.__name__ = "DisplayString"
_Idt1CrInboundPhNum_Object = MibTableColumn
idt1CrInboundPhNum = _Idt1CrInboundPhNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 3),
    _Idt1CrInboundPhNum_Type()
)
idt1CrInboundPhNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CrInboundPhNum.setStatus("mandatory")


class _Idt1CrInboundCallType_Type(Integer32):
    """Custom type idt1CrInboundCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analog", 1),
          ("digital", 2))
    )


_Idt1CrInboundCallType_Type.__name__ = "Integer32"
_Idt1CrInboundCallType_Object = MibTableColumn
idt1CrInboundCallType = _Idt1CrInboundCallType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 2, 1, 1, 4),
    _Idt1CrInboundCallType_Type()
)
idt1CrInboundCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1CrInboundCallType.setStatus("mandatory")
_Idt1Pl_ObjectIdentity = ObjectIdentity
idt1Pl = _Idt1Pl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 3)
)
_Idt1PlTable_Object = MibTable
idt1PlTable = _Idt1PlTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1)
)
if mibBuilder.loadTexts:
    idt1PlTable.setStatus("mandatory")
_Idt1PlEntry_Object = MibTableRow
idt1PlEntry = _Idt1PlEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1)
)
idt1PlEntry.setIndexNames(
    (0, "IDT1-MIB", "idt1PlIndex"),
    (0, "IDT1-MIB", "idt1PlIDIndex"),
)
if mibBuilder.loadTexts:
    idt1PlEntry.setStatus("mandatory")
_Idt1PlIndex_Type = Integer32
_Idt1PlIndex_Object = MibTableColumn
idt1PlIndex = _Idt1PlIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 1),
    _Idt1PlIndex_Type()
)
idt1PlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1PlIndex.setStatus("mandatory")
_Idt1PlIDIndex_Type = Integer32
_Idt1PlIDIndex_Object = MibTableColumn
idt1PlIDIndex = _Idt1PlIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 2),
    _Idt1PlIDIndex_Type()
)
idt1PlIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1PlIDIndex.setStatus("mandatory")


class _Idt1PlDNIS_Type(DisplayString):
    """Custom type idt1PlDNIS based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_Idt1PlDNIS_Type.__name__ = "DisplayString"
_Idt1PlDNIS_Object = MibTableColumn
idt1PlDNIS = _Idt1PlDNIS_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 3),
    _Idt1PlDNIS_Type()
)
idt1PlDNIS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1PlDNIS.setStatus("mandatory")


class _Idt1PlType_Type(Integer32):
    """Custom type idt1PlType based on Integer32"""
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
        *(("analog", 2),
          ("both", 4),
          ("digital", 3),
          ("none", 1))
    )


_Idt1PlType_Type.__name__ = "Integer32"
_Idt1PlType_Object = MibTableColumn
idt1PlType = _Idt1PlType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 3, 1, 1, 4),
    _Idt1PlType_Type()
)
idt1PlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1PlType.setStatus("mandatory")
_Idt1MdmRPA_ObjectIdentity = ObjectIdentity
idt1MdmRPA = _Idt1MdmRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4)
)
_Idt1MdmRPATable_Object = MibTable
idt1MdmRPATable = _Idt1MdmRPATable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1)
)
if mibBuilder.loadTexts:
    idt1MdmRPATable.setStatus("mandatory")
_Idt1MdmRPAEntry_Object = MibTableRow
idt1MdmRPAEntry = _Idt1MdmRPAEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1)
)
idt1MdmRPAEntry.setIndexNames(
    (0, "IDT1-MIB", "idt1MdmRPAIndex"),
    (0, "IDT1-MIB", "idt1MdmRPAIDIndex"),
)
if mibBuilder.loadTexts:
    idt1MdmRPAEntry.setStatus("mandatory")
_Idt1MdmRPAIndex_Type = Integer32
_Idt1MdmRPAIndex_Object = MibTableColumn
idt1MdmRPAIndex = _Idt1MdmRPAIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 1),
    _Idt1MdmRPAIndex_Type()
)
idt1MdmRPAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1MdmRPAIndex.setStatus("mandatory")
_Idt1MdmRPAIDIndex_Type = Integer32
_Idt1MdmRPAIDIndex_Object = MibTableColumn
idt1MdmRPAIDIndex = _Idt1MdmRPAIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 2),
    _Idt1MdmRPAIDIndex_Type()
)
idt1MdmRPAIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1MdmRPAIDIndex.setStatus("mandatory")


class _Idt1MdmRPASlot_Type(Integer32):
    """Custom type idt1MdmRPASlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Idt1MdmRPASlot_Type.__name__ = "Integer32"
_Idt1MdmRPASlot_Object = MibTableColumn
idt1MdmRPASlot = _Idt1MdmRPASlot_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 3),
    _Idt1MdmRPASlot_Type()
)
idt1MdmRPASlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1MdmRPASlot.setStatus("mandatory")


class _Idt1MdmRPAChan_Type(Integer32):
    """Custom type idt1MdmRPAChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Idt1MdmRPAChan_Type.__name__ = "Integer32"
_Idt1MdmRPAChan_Object = MibTableColumn
idt1MdmRPAChan = _Idt1MdmRPAChan_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 4),
    _Idt1MdmRPAChan_Type()
)
idt1MdmRPAChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1MdmRPAChan.setStatus("mandatory")


class _Idt1MdmRPAPoolID_Type(Integer32):
    """Custom type idt1MdmRPAPoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Idt1MdmRPAPoolID_Type.__name__ = "Integer32"
_Idt1MdmRPAPoolID_Object = MibTableColumn
idt1MdmRPAPoolID = _Idt1MdmRPAPoolID_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 4, 1, 1, 5),
    _Idt1MdmRPAPoolID_Type()
)
idt1MdmRPAPoolID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1MdmRPAPoolID.setStatus("mandatory")
_Idt1GwyRPA_ObjectIdentity = ObjectIdentity
idt1GwyRPA = _Idt1GwyRPA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 5)
)
_Idt1GwyRPATable_Object = MibTable
idt1GwyRPATable = _Idt1GwyRPATable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1)
)
if mibBuilder.loadTexts:
    idt1GwyRPATable.setStatus("mandatory")
_Idt1GwyRPAEntry_Object = MibTableRow
idt1GwyRPAEntry = _Idt1GwyRPAEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1)
)
idt1GwyRPAEntry.setIndexNames(
    (0, "IDT1-MIB", "idt1GwyRPAIndex"),
    (0, "IDT1-MIB", "idt1GwyRPASlotIndex"),
)
if mibBuilder.loadTexts:
    idt1GwyRPAEntry.setStatus("mandatory")
_Idt1GwyRPAIndex_Type = Integer32
_Idt1GwyRPAIndex_Object = MibTableColumn
idt1GwyRPAIndex = _Idt1GwyRPAIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1, 1),
    _Idt1GwyRPAIndex_Type()
)
idt1GwyRPAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1GwyRPAIndex.setStatus("mandatory")
_Idt1GwyRPASlotIndex_Type = Integer32
_Idt1GwyRPASlotIndex_Object = MibTableColumn
idt1GwyRPASlotIndex = _Idt1GwyRPASlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1, 2),
    _Idt1GwyRPASlotIndex_Type()
)
idt1GwyRPASlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idt1GwyRPASlotIndex.setStatus("mandatory")


class _Idt1GwyRPAPoolID_Type(Integer32):
    """Custom type idt1GwyRPAPoolID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_Idt1GwyRPAPoolID_Type.__name__ = "Integer32"
_Idt1GwyRPAPoolID_Object = MibTableColumn
idt1GwyRPAPoolID = _Idt1GwyRPAPoolID_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 15, 5, 1, 1, 3),
    _Idt1GwyRPAPoolID_Type()
)
idt1GwyRPAPoolID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idt1GwyRPAPoolID.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IDT1-MIB",
    **{"usr": usr,
       "nas": nas,
       "idt1": idt1,
       "idt1Cfg": idt1Cfg,
       "idt1CfgTable": idt1CfgTable,
       "idt1CfgEntry": idt1CfgEntry,
       "idt1CfgIndex": idt1CfgIndex,
       "idt1CfgAssgndISDNGateway": idt1CfgAssgndISDNGateway,
       "idt1CfgMdmCallsAllowedEna": idt1CfgMdmCallsAllowedEna,
       "idt1CfgMdmRoutingMethod": idt1CfgMdmRoutingMethod,
       "idt1CfgProjectSelectionR2": idt1CfgProjectSelectionR2,
       "idt1CfgInfoMsgTimeOut": idt1CfgInfoMsgTimeOut,
       "idt1CfgInbDNISLength": idt1CfgInbDNISLength,
       "idt1CfgSelectCompanding": idt1CfgSelectCompanding,
       "idt1CfgAniNumberEnable": idt1CfgAniNumberEnable,
       "idt1CfgNoBptyMethod": idt1CfgNoBptyMethod,
       "idt1CfgMaxISDNGwyCalls": idt1CfgMaxISDNGwyCalls,
       "idt1Cr": idt1Cr,
       "idt1CrTable": idt1CrTable,
       "idt1CrEntry": idt1CrEntry,
       "idt1CrIndex": idt1CrIndex,
       "idt1CrPhNumIndex": idt1CrPhNumIndex,
       "idt1CrInboundPhNum": idt1CrInboundPhNum,
       "idt1CrInboundCallType": idt1CrInboundCallType,
       "idt1Pl": idt1Pl,
       "idt1PlTable": idt1PlTable,
       "idt1PlEntry": idt1PlEntry,
       "idt1PlIndex": idt1PlIndex,
       "idt1PlIDIndex": idt1PlIDIndex,
       "idt1PlDNIS": idt1PlDNIS,
       "idt1PlType": idt1PlType,
       "idt1MdmRPA": idt1MdmRPA,
       "idt1MdmRPATable": idt1MdmRPATable,
       "idt1MdmRPAEntry": idt1MdmRPAEntry,
       "idt1MdmRPAIndex": idt1MdmRPAIndex,
       "idt1MdmRPAIDIndex": idt1MdmRPAIDIndex,
       "idt1MdmRPASlot": idt1MdmRPASlot,
       "idt1MdmRPAChan": idt1MdmRPAChan,
       "idt1MdmRPAPoolID": idt1MdmRPAPoolID,
       "idt1GwyRPA": idt1GwyRPA,
       "idt1GwyRPATable": idt1GwyRPATable,
       "idt1GwyRPAEntry": idt1GwyRPAEntry,
       "idt1GwyRPAIndex": idt1GwyRPAIndex,
       "idt1GwyRPASlotIndex": idt1GwyRPASlotIndex,
       "idt1GwyRPAPoolID": idt1GwyRPAPoolID}
)
