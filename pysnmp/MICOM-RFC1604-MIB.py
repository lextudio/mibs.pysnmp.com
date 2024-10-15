# SNMP MIB module (MICOM-RFC1604-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-RFC1604-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:49 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_rfc1604_ObjectIdentity = ObjectIdentity
micom_rfc1604 = _Micom_rfc1604_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8)
)
_Rfc1604_configuration_ObjectIdentity = ObjectIdentity
rfc1604_configuration = _Rfc1604_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1)
)
_McmFrLportTable_Object = MibTable
mcmFrLportTable = _McmFrLportTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 1)
)
if mibBuilder.loadTexts:
    mcmFrLportTable.setStatus("mandatory")
_McmFrLportEntry_Object = MibTableRow
mcmFrLportEntry = _McmFrLportEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 1, 1)
)
mcmFrLportEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "mcmFrLportIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrLportEntry.setStatus("mandatory")


class _McmFrLportIfIndex_Type(Integer32):
    """Custom type mcmFrLportIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrLportIfIndex_Type.__name__ = "Integer32"
_McmFrLportIfIndex_Object = MibTableColumn
mcmFrLportIfIndex = _McmFrLportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 1, 1, 1),
    _McmFrLportIfIndex_Type()
)
mcmFrLportIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLportIfIndex.setStatus("mandatory")


class _McmFrLportNumPlan_Type(Integer32):
    """Custom type mcmFrLportNumPlan based on Integer32"""
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
        *(("e164", 2),
          ("none", 4),
          ("other", 1),
          ("x121", 3))
    )


_McmFrLportNumPlan_Type.__name__ = "Integer32"
_McmFrLportNumPlan_Object = MibTableColumn
mcmFrLportNumPlan = _McmFrLportNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 1, 1, 2),
    _McmFrLportNumPlan_Type()
)
mcmFrLportNumPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLportNumPlan.setStatus("mandatory")


class _McmFrLportType_Type(Integer32):
    """Custom type mcmFrLportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_McmFrLportType_Type.__name__ = "Integer32"
_McmFrLportType_Object = MibTableColumn
mcmFrLportType = _McmFrLportType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 1, 1, 3),
    _McmFrLportType_Type()
)
mcmFrLportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLportType.setStatus("mandatory")


class _McmFrLportAddrDLCILen_Type(Integer32):
    """Custom type mcmFrLportAddrDLCILen based on Integer32"""
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
        *(("fourOctets17Bits", 4),
          ("fourOctets23Bits", 5),
          ("threeOctets10Bits", 2),
          ("threeOctets16Bits", 3),
          ("twoOctets10Bits", 1))
    )


_McmFrLportAddrDLCILen_Type.__name__ = "Integer32"
_McmFrLportAddrDLCILen_Object = MibTableColumn
mcmFrLportAddrDLCILen = _McmFrLportAddrDLCILen_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 1, 1, 4),
    _McmFrLportAddrDLCILen_Type()
)
mcmFrLportAddrDLCILen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLportAddrDLCILen.setStatus("mandatory")


class _McmFrLportVCSigProtocol_Type(Integer32):
    """Custom type mcmFrLportVCSigProtocol based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1617D-1994", 6),
          ("ccittQ933A", 5),
          ("lmi", 2),
          ("none", 1))
    )


_McmFrLportVCSigProtocol_Type.__name__ = "Integer32"
_McmFrLportVCSigProtocol_Object = MibTableColumn
mcmFrLportVCSigProtocol = _McmFrLportVCSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 1, 1, 5),
    _McmFrLportVCSigProtocol_Type()
)
mcmFrLportVCSigProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrLportVCSigProtocol.setStatus("mandatory")
_McmFrMgtVCSigTable_Object = MibTable
mcmFrMgtVCSigTable = _McmFrMgtVCSigTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2)
)
if mibBuilder.loadTexts:
    mcmFrMgtVCSigTable.setStatus("mandatory")
_McmFrMgtVCSigEntry_Object = MibTableRow
mcmFrMgtVCSigEntry = _McmFrMgtVCSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1)
)
mcmFrMgtVCSigEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "mcmFrMgtVCSigIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrMgtVCSigEntry.setStatus("mandatory")


class _McmFrMgtVCSigIfIndex_Type(Integer32):
    """Custom type mcmFrMgtVCSigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrMgtVCSigIfIndex_Type.__name__ = "Integer32"
_McmFrMgtVCSigIfIndex_Object = MibTableColumn
mcmFrMgtVCSigIfIndex = _McmFrMgtVCSigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 1),
    _McmFrMgtVCSigIfIndex_Type()
)
mcmFrMgtVCSigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigIfIndex.setStatus("mandatory")


class _McmFrMgtVCSigProced_Type(Integer32):
    """Custom type mcmFrMgtVCSigProced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirect", 2),
          ("u2nnet", 1))
    )


_McmFrMgtVCSigProced_Type.__name__ = "Integer32"
_McmFrMgtVCSigProced_Object = MibTableColumn
mcmFrMgtVCSigProced = _McmFrMgtVCSigProced_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 2),
    _McmFrMgtVCSigProced_Type()
)
mcmFrMgtVCSigProced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigProced.setStatus("mandatory")


class _McmFrMgtVCSigNetN392_Type(Integer32):
    """Custom type mcmFrMgtVCSigNetN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_McmFrMgtVCSigNetN392_Type.__name__ = "Integer32"
_McmFrMgtVCSigNetN392_Object = MibTableColumn
mcmFrMgtVCSigNetN392 = _McmFrMgtVCSigNetN392_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 3),
    _McmFrMgtVCSigNetN392_Type()
)
mcmFrMgtVCSigNetN392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigNetN392.setStatus("mandatory")


class _McmFrMgtVCSigNetN393_Type(Integer32):
    """Custom type mcmFrMgtVCSigNetN393 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_McmFrMgtVCSigNetN393_Type.__name__ = "Integer32"
_McmFrMgtVCSigNetN393_Object = MibTableColumn
mcmFrMgtVCSigNetN393 = _McmFrMgtVCSigNetN393_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 4),
    _McmFrMgtVCSigNetN393_Type()
)
mcmFrMgtVCSigNetN393.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigNetN393.setStatus("mandatory")


class _McmFrMgtVCSigNetT392_Type(Integer32):
    """Custom type mcmFrMgtVCSigNetT392 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_McmFrMgtVCSigNetT392_Type.__name__ = "Integer32"
_McmFrMgtVCSigNetT392_Object = MibTableColumn
mcmFrMgtVCSigNetT392 = _McmFrMgtVCSigNetT392_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 5),
    _McmFrMgtVCSigNetT392_Type()
)
mcmFrMgtVCSigNetT392.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigNetT392.setStatus("mandatory")
_McmFrMgtVCSigNetLinkRelErrors_Type = Counter32
_McmFrMgtVCSigNetLinkRelErrors_Object = MibTableColumn
mcmFrMgtVCSigNetLinkRelErrors = _McmFrMgtVCSigNetLinkRelErrors_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 6),
    _McmFrMgtVCSigNetLinkRelErrors_Type()
)
mcmFrMgtVCSigNetLinkRelErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigNetLinkRelErrors.setStatus("mandatory")
_McmFrMgtVCSigNetProtErrors_Type = Counter32
_McmFrMgtVCSigNetProtErrors_Object = MibTableColumn
mcmFrMgtVCSigNetProtErrors = _McmFrMgtVCSigNetProtErrors_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 7),
    _McmFrMgtVCSigNetProtErrors_Type()
)
mcmFrMgtVCSigNetProtErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigNetProtErrors.setStatus("mandatory")
_McmFrMgtVCSigNetChanInactive_Type = Counter32
_McmFrMgtVCSigNetChanInactive_Object = MibTableColumn
mcmFrMgtVCSigNetChanInactive = _McmFrMgtVCSigNetChanInactive_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 2, 1, 8),
    _McmFrMgtVCSigNetChanInactive_Type()
)
mcmFrMgtVCSigNetChanInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigNetChanInactive.setStatus("mandatory")
_McmFrPVCEndptTable_Object = MibTable
mcmFrPVCEndptTable = _McmFrPVCEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3)
)
if mibBuilder.loadTexts:
    mcmFrPVCEndptTable.setStatus("mandatory")
_McmFrPVCEndptEntry_Object = MibTableRow
mcmFrPVCEndptEntry = _McmFrPVCEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1)
)
mcmFrPVCEndptEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "mcmFrPVCEndptIfIndex"),
    (0, "MICOM-RFC1604-MIB", "mcmFrPVCEndptDLCIIndex"),
)
if mibBuilder.loadTexts:
    mcmFrPVCEndptEntry.setStatus("mandatory")


class _McmFrPVCEndptIfIndex_Type(Integer32):
    """Custom type mcmFrPVCEndptIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrPVCEndptIfIndex_Type.__name__ = "Integer32"
_McmFrPVCEndptIfIndex_Object = MibTableColumn
mcmFrPVCEndptIfIndex = _McmFrPVCEndptIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 1),
    _McmFrPVCEndptIfIndex_Type()
)
mcmFrPVCEndptIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptIfIndex.setStatus("mandatory")


class _McmFrPVCEndptDLCIIndex_Type(Integer32):
    """Custom type mcmFrPVCEndptDLCIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_McmFrPVCEndptDLCIIndex_Type.__name__ = "Integer32"
_McmFrPVCEndptDLCIIndex_Object = MibTableColumn
mcmFrPVCEndptDLCIIndex = _McmFrPVCEndptDLCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 2),
    _McmFrPVCEndptDLCIIndex_Type()
)
mcmFrPVCEndptDLCIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptDLCIIndex.setStatus("mandatory")


class _McmFrPVCEndptInMaxFrameSize_Type(Integer32):
    """Custom type mcmFrPVCEndptInMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrPVCEndptInMaxFrameSize_Type.__name__ = "Integer32"
_McmFrPVCEndptInMaxFrameSize_Object = MibTableColumn
mcmFrPVCEndptInMaxFrameSize = _McmFrPVCEndptInMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 3),
    _McmFrPVCEndptInMaxFrameSize_Type()
)
mcmFrPVCEndptInMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInMaxFrameSize.setStatus("mandatory")


class _McmFrPVCEndptInBc_Type(Integer32):
    """Custom type mcmFrPVCEndptInBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrPVCEndptInBc_Type.__name__ = "Integer32"
_McmFrPVCEndptInBc_Object = MibTableColumn
mcmFrPVCEndptInBc = _McmFrPVCEndptInBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 4),
    _McmFrPVCEndptInBc_Type()
)
mcmFrPVCEndptInBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInBc.setStatus("mandatory")


class _McmFrPVCEndptInBe_Type(Integer32):
    """Custom type mcmFrPVCEndptInBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrPVCEndptInBe_Type.__name__ = "Integer32"
_McmFrPVCEndptInBe_Object = MibTableColumn
mcmFrPVCEndptInBe = _McmFrPVCEndptInBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 5),
    _McmFrPVCEndptInBe_Type()
)
mcmFrPVCEndptInBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInBe.setStatus("mandatory")


class _McmFrPVCEndptInCIR_Type(Integer32):
    """Custom type mcmFrPVCEndptInCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmFrPVCEndptInCIR_Type.__name__ = "Integer32"
_McmFrPVCEndptInCIR_Object = MibTableColumn
mcmFrPVCEndptInCIR = _McmFrPVCEndptInCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 6),
    _McmFrPVCEndptInCIR_Type()
)
mcmFrPVCEndptInCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInCIR.setStatus("mandatory")


class _McmFrPVCEndptOutMaxFrameSize_Type(Integer32):
    """Custom type mcmFrPVCEndptOutMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_McmFrPVCEndptOutMaxFrameSize_Type.__name__ = "Integer32"
_McmFrPVCEndptOutMaxFrameSize_Object = MibTableColumn
mcmFrPVCEndptOutMaxFrameSize = _McmFrPVCEndptOutMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 7),
    _McmFrPVCEndptOutMaxFrameSize_Type()
)
mcmFrPVCEndptOutMaxFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptOutMaxFrameSize.setStatus("mandatory")


class _McmFrPVCEndptOutBc_Type(Integer32):
    """Custom type mcmFrPVCEndptOutBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrPVCEndptOutBc_Type.__name__ = "Integer32"
_McmFrPVCEndptOutBc_Object = MibTableColumn
mcmFrPVCEndptOutBc = _McmFrPVCEndptOutBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 8),
    _McmFrPVCEndptOutBc_Type()
)
mcmFrPVCEndptOutBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptOutBc.setStatus("mandatory")


class _McmFrPVCEndptOutBe_Type(Integer32):
    """Custom type mcmFrPVCEndptOutBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_McmFrPVCEndptOutBe_Type.__name__ = "Integer32"
_McmFrPVCEndptOutBe_Object = MibTableColumn
mcmFrPVCEndptOutBe = _McmFrPVCEndptOutBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 9),
    _McmFrPVCEndptOutBe_Type()
)
mcmFrPVCEndptOutBe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptOutBe.setStatus("mandatory")


class _McmFrPVCEndptOutCIR_Type(Integer32):
    """Custom type mcmFrPVCEndptOutCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmFrPVCEndptOutCIR_Type.__name__ = "Integer32"
_McmFrPVCEndptOutCIR_Object = MibTableColumn
mcmFrPVCEndptOutCIR = _McmFrPVCEndptOutCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 10),
    _McmFrPVCEndptOutCIR_Type()
)
mcmFrPVCEndptOutCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptOutCIR.setStatus("mandatory")
_McmFrPVCEndptInFrames_Type = Counter32
_McmFrPVCEndptInFrames_Object = MibTableColumn
mcmFrPVCEndptInFrames = _McmFrPVCEndptInFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 11),
    _McmFrPVCEndptInFrames_Type()
)
mcmFrPVCEndptInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInFrames.setStatus("mandatory")
_McmFrPVCEndptOutFrames_Type = Counter32
_McmFrPVCEndptOutFrames_Object = MibTableColumn
mcmFrPVCEndptOutFrames = _McmFrPVCEndptOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 12),
    _McmFrPVCEndptOutFrames_Type()
)
mcmFrPVCEndptOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptOutFrames.setStatus("mandatory")
_McmFrPVCEndptInDEFrames_Type = Counter32
_McmFrPVCEndptInDEFrames_Object = MibTableColumn
mcmFrPVCEndptInDEFrames = _McmFrPVCEndptInDEFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 13),
    _McmFrPVCEndptInDEFrames_Type()
)
mcmFrPVCEndptInDEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInDEFrames.setStatus("mandatory")
_McmFrPVCEndptInExcessFrames_Type = Counter32
_McmFrPVCEndptInExcessFrames_Object = MibTableColumn
mcmFrPVCEndptInExcessFrames = _McmFrPVCEndptInExcessFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 14),
    _McmFrPVCEndptInExcessFrames_Type()
)
mcmFrPVCEndptInExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInExcessFrames.setStatus("mandatory")
_McmFrPVCEndptOutExcessFrames_Type = Counter32
_McmFrPVCEndptOutExcessFrames_Object = MibTableColumn
mcmFrPVCEndptOutExcessFrames = _McmFrPVCEndptOutExcessFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 15),
    _McmFrPVCEndptOutExcessFrames_Type()
)
mcmFrPVCEndptOutExcessFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptOutExcessFrames.setStatus("mandatory")
_McmFrPVCEndptInDiscards_Type = Counter32
_McmFrPVCEndptInDiscards_Object = MibTableColumn
mcmFrPVCEndptInDiscards = _McmFrPVCEndptInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 16),
    _McmFrPVCEndptInDiscards_Type()
)
mcmFrPVCEndptInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInDiscards.setStatus("mandatory")
_McmFrPVCEndptInOctets_Type = Counter32
_McmFrPVCEndptInOctets_Object = MibTableColumn
mcmFrPVCEndptInOctets = _McmFrPVCEndptInOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 17),
    _McmFrPVCEndptInOctets_Type()
)
mcmFrPVCEndptInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptInOctets.setStatus("mandatory")
_McmFrPVCEndptOutOctets_Type = Counter32
_McmFrPVCEndptOutOctets_Object = MibTableColumn
mcmFrPVCEndptOutOctets = _McmFrPVCEndptOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 3, 1, 18),
    _McmFrPVCEndptOutOctets_Type()
)
mcmFrPVCEndptOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptOutOctets.setStatus("mandatory")
_NvmFrLportTable_Object = MibTable
nvmFrLportTable = _NvmFrLportTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 4)
)
if mibBuilder.loadTexts:
    nvmFrLportTable.setStatus("mandatory")
_NvmFrLportEntry_Object = MibTableRow
nvmFrLportEntry = _NvmFrLportEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 4, 1)
)
nvmFrLportEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "nvmFrLportIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrLportEntry.setStatus("mandatory")


class _NvmFrLportIfIndex_Type(Integer32):
    """Custom type nvmFrLportIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrLportIfIndex_Type.__name__ = "Integer32"
_NvmFrLportIfIndex_Object = MibTableColumn
nvmFrLportIfIndex = _NvmFrLportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 4, 1, 1),
    _NvmFrLportIfIndex_Type()
)
nvmFrLportIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrLportIfIndex.setStatus("mandatory")


class _NvmFrLportNumPlan_Type(Integer32):
    """Custom type nvmFrLportNumPlan based on Integer32"""
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
        *(("e164", 2),
          ("none", 4),
          ("other", 1),
          ("x121", 3))
    )


_NvmFrLportNumPlan_Type.__name__ = "Integer32"
_NvmFrLportNumPlan_Object = MibTableColumn
nvmFrLportNumPlan = _NvmFrLportNumPlan_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 4, 1, 2),
    _NvmFrLportNumPlan_Type()
)
nvmFrLportNumPlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrLportNumPlan.setStatus("mandatory")


class _NvmFrLportType_Type(Integer32):
    """Custom type nvmFrLportType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nni", 2),
          ("uni", 1))
    )


_NvmFrLportType_Type.__name__ = "Integer32"
_NvmFrLportType_Object = MibTableColumn
nvmFrLportType = _NvmFrLportType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 4, 1, 3),
    _NvmFrLportType_Type()
)
nvmFrLportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrLportType.setStatus("mandatory")


class _NvmFrLportAddrDLCILen_Type(Integer32):
    """Custom type nvmFrLportAddrDLCILen based on Integer32"""
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
        *(("fourOctets17Bits", 4),
          ("fourOctets23Bits", 5),
          ("threeOctets10Bits", 2),
          ("threeOctets16Bits", 3),
          ("twoOctets10Bits", 1))
    )


_NvmFrLportAddrDLCILen_Type.__name__ = "Integer32"
_NvmFrLportAddrDLCILen_Object = MibTableColumn
nvmFrLportAddrDLCILen = _NvmFrLportAddrDLCILen_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 4, 1, 4),
    _NvmFrLportAddrDLCILen_Type()
)
nvmFrLportAddrDLCILen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrLportAddrDLCILen.setStatus("mandatory")


class _NvmFrLportVCSigProtocol_Type(Integer32):
    """Custom type nvmFrLportVCSigProtocol based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ansiT1617D-1994", 6),
          ("ccittQ933A", 5),
          ("lmi", 2),
          ("none", 1))
    )


_NvmFrLportVCSigProtocol_Type.__name__ = "Integer32"
_NvmFrLportVCSigProtocol_Object = MibTableColumn
nvmFrLportVCSigProtocol = _NvmFrLportVCSigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 4, 1, 5),
    _NvmFrLportVCSigProtocol_Type()
)
nvmFrLportVCSigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrLportVCSigProtocol.setStatus("mandatory")
_NvmFrMgtVCSigTable_Object = MibTable
nvmFrMgtVCSigTable = _NvmFrMgtVCSigTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 5)
)
if mibBuilder.loadTexts:
    nvmFrMgtVCSigTable.setStatus("mandatory")
_NvmFrMgtVCSigEntry_Object = MibTableRow
nvmFrMgtVCSigEntry = _NvmFrMgtVCSigEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 5, 1)
)
nvmFrMgtVCSigEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "nvmFrMgtVCSigIfIndex"),
)
if mibBuilder.loadTexts:
    nvmFrMgtVCSigEntry.setStatus("mandatory")


class _NvmFrMgtVCSigIfIndex_Type(Integer32):
    """Custom type nvmFrMgtVCSigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrMgtVCSigIfIndex_Type.__name__ = "Integer32"
_NvmFrMgtVCSigIfIndex_Object = MibTableColumn
nvmFrMgtVCSigIfIndex = _NvmFrMgtVCSigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 5, 1, 1),
    _NvmFrMgtVCSigIfIndex_Type()
)
nvmFrMgtVCSigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrMgtVCSigIfIndex.setStatus("mandatory")


class _NvmFrMgtVCSigProced_Type(Integer32):
    """Custom type nvmFrMgtVCSigProced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bidirect", 2),
          ("u2nnet", 1))
    )


_NvmFrMgtVCSigProced_Type.__name__ = "Integer32"
_NvmFrMgtVCSigProced_Object = MibTableColumn
nvmFrMgtVCSigProced = _NvmFrMgtVCSigProced_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 5, 1, 2),
    _NvmFrMgtVCSigProced_Type()
)
nvmFrMgtVCSigProced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrMgtVCSigProced.setStatus("mandatory")


class _NvmFrMgtVCSigNetN392_Type(Integer32):
    """Custom type nvmFrMgtVCSigNetN392 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NvmFrMgtVCSigNetN392_Type.__name__ = "Integer32"
_NvmFrMgtVCSigNetN392_Object = MibTableColumn
nvmFrMgtVCSigNetN392 = _NvmFrMgtVCSigNetN392_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 5, 1, 3),
    _NvmFrMgtVCSigNetN392_Type()
)
nvmFrMgtVCSigNetN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrMgtVCSigNetN392.setStatus("mandatory")


class _NvmFrMgtVCSigNetN393_Type(Integer32):
    """Custom type nvmFrMgtVCSigNetN393 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NvmFrMgtVCSigNetN393_Type.__name__ = "Integer32"
_NvmFrMgtVCSigNetN393_Object = MibTableColumn
nvmFrMgtVCSigNetN393 = _NvmFrMgtVCSigNetN393_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 5, 1, 4),
    _NvmFrMgtVCSigNetN393_Type()
)
nvmFrMgtVCSigNetN393.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrMgtVCSigNetN393.setStatus("mandatory")


class _NvmFrMgtVCSigNetT392_Type(Integer32):
    """Custom type nvmFrMgtVCSigNetT392 based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_NvmFrMgtVCSigNetT392_Type.__name__ = "Integer32"
_NvmFrMgtVCSigNetT392_Object = MibTableColumn
nvmFrMgtVCSigNetT392 = _NvmFrMgtVCSigNetT392_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 5, 1, 5),
    _NvmFrMgtVCSigNetT392_Type()
)
nvmFrMgtVCSigNetT392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrMgtVCSigNetT392.setStatus("mandatory")
_NvmFrPVCEndptTable_Object = MibTable
nvmFrPVCEndptTable = _NvmFrPVCEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6)
)
if mibBuilder.loadTexts:
    nvmFrPVCEndptTable.setStatus("mandatory")
_NvmFrPVCEndptEntry_Object = MibTableRow
nvmFrPVCEndptEntry = _NvmFrPVCEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1)
)
nvmFrPVCEndptEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "nvmFrPVCEndptIfIndex"),
    (0, "MICOM-RFC1604-MIB", "nvmFrPVCEndptDLCIIndex"),
)
if mibBuilder.loadTexts:
    nvmFrPVCEndptEntry.setStatus("mandatory")


class _NvmFrPVCEndptIfIndex_Type(Integer32):
    """Custom type nvmFrPVCEndptIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NvmFrPVCEndptIfIndex_Type.__name__ = "Integer32"
_NvmFrPVCEndptIfIndex_Object = MibTableColumn
nvmFrPVCEndptIfIndex = _NvmFrPVCEndptIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 1),
    _NvmFrPVCEndptIfIndex_Type()
)
nvmFrPVCEndptIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrPVCEndptIfIndex.setStatus("mandatory")


class _NvmFrPVCEndptDLCIIndex_Type(Integer32):
    """Custom type nvmFrPVCEndptDLCIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NvmFrPVCEndptDLCIIndex_Type.__name__ = "Integer32"
_NvmFrPVCEndptDLCIIndex_Object = MibTableColumn
nvmFrPVCEndptDLCIIndex = _NvmFrPVCEndptDLCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 2),
    _NvmFrPVCEndptDLCIIndex_Type()
)
nvmFrPVCEndptDLCIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrPVCEndptDLCIIndex.setStatus("mandatory")


class _NvmFrPVCEndptInMaxFrameSize_Type(Integer32):
    """Custom type nvmFrPVCEndptInMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrPVCEndptInMaxFrameSize_Type.__name__ = "Integer32"
_NvmFrPVCEndptInMaxFrameSize_Object = MibTableColumn
nvmFrPVCEndptInMaxFrameSize = _NvmFrPVCEndptInMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 3),
    _NvmFrPVCEndptInMaxFrameSize_Type()
)
nvmFrPVCEndptInMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCEndptInMaxFrameSize.setStatus("mandatory")


class _NvmFrPVCEndptInBc_Type(Integer32):
    """Custom type nvmFrPVCEndptInBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPVCEndptInBc_Type.__name__ = "Integer32"
_NvmFrPVCEndptInBc_Object = MibTableColumn
nvmFrPVCEndptInBc = _NvmFrPVCEndptInBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 4),
    _NvmFrPVCEndptInBc_Type()
)
nvmFrPVCEndptInBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrPVCEndptInBc.setStatus("mandatory")


class _NvmFrPVCEndptInBe_Type(Integer32):
    """Custom type nvmFrPVCEndptInBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPVCEndptInBe_Type.__name__ = "Integer32"
_NvmFrPVCEndptInBe_Object = MibTableColumn
nvmFrPVCEndptInBe = _NvmFrPVCEndptInBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 5),
    _NvmFrPVCEndptInBe_Type()
)
nvmFrPVCEndptInBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCEndptInBe.setStatus("mandatory")


class _NvmFrPVCEndptInCIR_Type(Integer32):
    """Custom type nvmFrPVCEndptInCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPVCEndptInCIR_Type.__name__ = "Integer32"
_NvmFrPVCEndptInCIR_Object = MibTableColumn
nvmFrPVCEndptInCIR = _NvmFrPVCEndptInCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 6),
    _NvmFrPVCEndptInCIR_Type()
)
nvmFrPVCEndptInCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCEndptInCIR.setStatus("mandatory")


class _NvmFrPVCEndptOutMaxFrameSize_Type(Integer32):
    """Custom type nvmFrPVCEndptOutMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_NvmFrPVCEndptOutMaxFrameSize_Type.__name__ = "Integer32"
_NvmFrPVCEndptOutMaxFrameSize_Object = MibTableColumn
nvmFrPVCEndptOutMaxFrameSize = _NvmFrPVCEndptOutMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 7),
    _NvmFrPVCEndptOutMaxFrameSize_Type()
)
nvmFrPVCEndptOutMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCEndptOutMaxFrameSize.setStatus("mandatory")


class _NvmFrPVCEndptOutBc_Type(Integer32):
    """Custom type nvmFrPVCEndptOutBc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPVCEndptOutBc_Type.__name__ = "Integer32"
_NvmFrPVCEndptOutBc_Object = MibTableColumn
nvmFrPVCEndptOutBc = _NvmFrPVCEndptOutBc_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 8),
    _NvmFrPVCEndptOutBc_Type()
)
nvmFrPVCEndptOutBc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmFrPVCEndptOutBc.setStatus("mandatory")


class _NvmFrPVCEndptOutBe_Type(Integer32):
    """Custom type nvmFrPVCEndptOutBe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPVCEndptOutBe_Type.__name__ = "Integer32"
_NvmFrPVCEndptOutBe_Object = MibTableColumn
nvmFrPVCEndptOutBe = _NvmFrPVCEndptOutBe_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 9),
    _NvmFrPVCEndptOutBe_Type()
)
nvmFrPVCEndptOutBe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCEndptOutBe.setStatus("mandatory")


class _NvmFrPVCEndptOutCIR_Type(Integer32):
    """Custom type nvmFrPVCEndptOutCIR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2560000),
    )


_NvmFrPVCEndptOutCIR_Type.__name__ = "Integer32"
_NvmFrPVCEndptOutCIR_Object = MibTableColumn
nvmFrPVCEndptOutCIR = _NvmFrPVCEndptOutCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 1, 6, 1, 10),
    _NvmFrPVCEndptOutCIR_Type()
)
nvmFrPVCEndptOutCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmFrPVCEndptOutCIR.setStatus("mandatory")
_Rfc1604_control_ObjectIdentity = ObjectIdentity
rfc1604_control = _Rfc1604_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2)
)
_McmFrMgtVCSigCntrTable_Object = MibTable
mcmFrMgtVCSigCntrTable = _McmFrMgtVCSigCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 1)
)
if mibBuilder.loadTexts:
    mcmFrMgtVCSigCntrTable.setStatus("obsolete")
_McmFrMgtVCSigCntrEntry_Object = MibTableRow
mcmFrMgtVCSigCntrEntry = _McmFrMgtVCSigCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 1, 1)
)
mcmFrMgtVCSigCntrEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "mcmFrMgtVCSigCntrIfIndex"),
)
if mibBuilder.loadTexts:
    mcmFrMgtVCSigCntrEntry.setStatus("obsolete")


class _McmFrMgtVCSigCntrIfIndex_Type(Integer32):
    """Custom type mcmFrMgtVCSigCntrIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmFrMgtVCSigCntrIfIndex_Type.__name__ = "Integer32"
_McmFrMgtVCSigCntrIfIndex_Object = MibTableColumn
mcmFrMgtVCSigCntrIfIndex = _McmFrMgtVCSigCntrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 1, 1, 1),
    _McmFrMgtVCSigCntrIfIndex_Type()
)
mcmFrMgtVCSigCntrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigCntrIfIndex.setStatus("obsolete")


class _McmFrMgtVCSigCntrAction_Type(Integer32):
    """Custom type mcmFrMgtVCSigCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmFrMgtVCSigCntrAction_Type.__name__ = "Integer32"
_McmFrMgtVCSigCntrAction_Object = MibTableColumn
mcmFrMgtVCSigCntrAction = _McmFrMgtVCSigCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 1, 1, 2),
    _McmFrMgtVCSigCntrAction_Type()
)
mcmFrMgtVCSigCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmFrMgtVCSigCntrAction.setStatus("obsolete")
_McmFrPVCEndptCntrTable_Object = MibTable
mcmFrPVCEndptCntrTable = _McmFrPVCEndptCntrTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 2)
)
if mibBuilder.loadTexts:
    mcmFrPVCEndptCntrTable.setStatus("obsolete")
_McmFrPVCEndptCntrEntry_Object = MibTableRow
mcmFrPVCEndptCntrEntry = _McmFrPVCEndptCntrEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 2, 1)
)
mcmFrPVCEndptCntrEntry.setIndexNames(
    (0, "MICOM-RFC1604-MIB", "mcmFrPVCEndptCntrIfIndex"),
    (0, "MICOM-RFC1604-MIB", "mcmFrPVCEndptCntrDLCIIndex"),
)
if mibBuilder.loadTexts:
    mcmFrPVCEndptCntrEntry.setStatus("obsolete")
_McmFrPVCEndptCntrIfIndex_Type = Integer32
_McmFrPVCEndptCntrIfIndex_Object = MibTableColumn
mcmFrPVCEndptCntrIfIndex = _McmFrPVCEndptCntrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 2, 1, 1),
    _McmFrPVCEndptCntrIfIndex_Type()
)
mcmFrPVCEndptCntrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptCntrIfIndex.setStatus("obsolete")
_McmFrPVCEndptCntrDLCIIndex_Type = Integer32
_McmFrPVCEndptCntrDLCIIndex_Object = MibTableColumn
mcmFrPVCEndptCntrDLCIIndex = _McmFrPVCEndptCntrDLCIIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 2, 1, 2),
    _McmFrPVCEndptCntrDLCIIndex_Type()
)
mcmFrPVCEndptCntrDLCIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptCntrDLCIIndex.setStatus("obsolete")


class _McmFrPVCEndptCntrAction_Type(Integer32):
    """Custom type mcmFrPVCEndptCntrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmFrPVCEndptCntrAction_Type.__name__ = "Integer32"
_McmFrPVCEndptCntrAction_Object = MibTableColumn
mcmFrPVCEndptCntrAction = _McmFrPVCEndptCntrAction_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 8, 2, 2, 1, 3),
    _McmFrPVCEndptCntrAction_Type()
)
mcmFrPVCEndptCntrAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmFrPVCEndptCntrAction.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-RFC1604-MIB",
    **{"micom-rfc1604": micom_rfc1604,
       "rfc1604-configuration": rfc1604_configuration,
       "mcmFrLportTable": mcmFrLportTable,
       "mcmFrLportEntry": mcmFrLportEntry,
       "mcmFrLportIfIndex": mcmFrLportIfIndex,
       "mcmFrLportNumPlan": mcmFrLportNumPlan,
       "mcmFrLportType": mcmFrLportType,
       "mcmFrLportAddrDLCILen": mcmFrLportAddrDLCILen,
       "mcmFrLportVCSigProtocol": mcmFrLportVCSigProtocol,
       "mcmFrMgtVCSigTable": mcmFrMgtVCSigTable,
       "mcmFrMgtVCSigEntry": mcmFrMgtVCSigEntry,
       "mcmFrMgtVCSigIfIndex": mcmFrMgtVCSigIfIndex,
       "mcmFrMgtVCSigProced": mcmFrMgtVCSigProced,
       "mcmFrMgtVCSigNetN392": mcmFrMgtVCSigNetN392,
       "mcmFrMgtVCSigNetN393": mcmFrMgtVCSigNetN393,
       "mcmFrMgtVCSigNetT392": mcmFrMgtVCSigNetT392,
       "mcmFrMgtVCSigNetLinkRelErrors": mcmFrMgtVCSigNetLinkRelErrors,
       "mcmFrMgtVCSigNetProtErrors": mcmFrMgtVCSigNetProtErrors,
       "mcmFrMgtVCSigNetChanInactive": mcmFrMgtVCSigNetChanInactive,
       "mcmFrPVCEndptTable": mcmFrPVCEndptTable,
       "mcmFrPVCEndptEntry": mcmFrPVCEndptEntry,
       "mcmFrPVCEndptIfIndex": mcmFrPVCEndptIfIndex,
       "mcmFrPVCEndptDLCIIndex": mcmFrPVCEndptDLCIIndex,
       "mcmFrPVCEndptInMaxFrameSize": mcmFrPVCEndptInMaxFrameSize,
       "mcmFrPVCEndptInBc": mcmFrPVCEndptInBc,
       "mcmFrPVCEndptInBe": mcmFrPVCEndptInBe,
       "mcmFrPVCEndptInCIR": mcmFrPVCEndptInCIR,
       "mcmFrPVCEndptOutMaxFrameSize": mcmFrPVCEndptOutMaxFrameSize,
       "mcmFrPVCEndptOutBc": mcmFrPVCEndptOutBc,
       "mcmFrPVCEndptOutBe": mcmFrPVCEndptOutBe,
       "mcmFrPVCEndptOutCIR": mcmFrPVCEndptOutCIR,
       "mcmFrPVCEndptInFrames": mcmFrPVCEndptInFrames,
       "mcmFrPVCEndptOutFrames": mcmFrPVCEndptOutFrames,
       "mcmFrPVCEndptInDEFrames": mcmFrPVCEndptInDEFrames,
       "mcmFrPVCEndptInExcessFrames": mcmFrPVCEndptInExcessFrames,
       "mcmFrPVCEndptOutExcessFrames": mcmFrPVCEndptOutExcessFrames,
       "mcmFrPVCEndptInDiscards": mcmFrPVCEndptInDiscards,
       "mcmFrPVCEndptInOctets": mcmFrPVCEndptInOctets,
       "mcmFrPVCEndptOutOctets": mcmFrPVCEndptOutOctets,
       "nvmFrLportTable": nvmFrLportTable,
       "nvmFrLportEntry": nvmFrLportEntry,
       "nvmFrLportIfIndex": nvmFrLportIfIndex,
       "nvmFrLportNumPlan": nvmFrLportNumPlan,
       "nvmFrLportType": nvmFrLportType,
       "nvmFrLportAddrDLCILen": nvmFrLportAddrDLCILen,
       "nvmFrLportVCSigProtocol": nvmFrLportVCSigProtocol,
       "nvmFrMgtVCSigTable": nvmFrMgtVCSigTable,
       "nvmFrMgtVCSigEntry": nvmFrMgtVCSigEntry,
       "nvmFrMgtVCSigIfIndex": nvmFrMgtVCSigIfIndex,
       "nvmFrMgtVCSigProced": nvmFrMgtVCSigProced,
       "nvmFrMgtVCSigNetN392": nvmFrMgtVCSigNetN392,
       "nvmFrMgtVCSigNetN393": nvmFrMgtVCSigNetN393,
       "nvmFrMgtVCSigNetT392": nvmFrMgtVCSigNetT392,
       "nvmFrPVCEndptTable": nvmFrPVCEndptTable,
       "nvmFrPVCEndptEntry": nvmFrPVCEndptEntry,
       "nvmFrPVCEndptIfIndex": nvmFrPVCEndptIfIndex,
       "nvmFrPVCEndptDLCIIndex": nvmFrPVCEndptDLCIIndex,
       "nvmFrPVCEndptInMaxFrameSize": nvmFrPVCEndptInMaxFrameSize,
       "nvmFrPVCEndptInBc": nvmFrPVCEndptInBc,
       "nvmFrPVCEndptInBe": nvmFrPVCEndptInBe,
       "nvmFrPVCEndptInCIR": nvmFrPVCEndptInCIR,
       "nvmFrPVCEndptOutMaxFrameSize": nvmFrPVCEndptOutMaxFrameSize,
       "nvmFrPVCEndptOutBc": nvmFrPVCEndptOutBc,
       "nvmFrPVCEndptOutBe": nvmFrPVCEndptOutBe,
       "nvmFrPVCEndptOutCIR": nvmFrPVCEndptOutCIR,
       "rfc1604-control": rfc1604_control,
       "mcmFrMgtVCSigCntrTable": mcmFrMgtVCSigCntrTable,
       "mcmFrMgtVCSigCntrEntry": mcmFrMgtVCSigCntrEntry,
       "mcmFrMgtVCSigCntrIfIndex": mcmFrMgtVCSigCntrIfIndex,
       "mcmFrMgtVCSigCntrAction": mcmFrMgtVCSigCntrAction,
       "mcmFrPVCEndptCntrTable": mcmFrPVCEndptCntrTable,
       "mcmFrPVCEndptCntrEntry": mcmFrPVCEndptCntrEntry,
       "mcmFrPVCEndptCntrIfIndex": mcmFrPVCEndptCntrIfIndex,
       "mcmFrPVCEndptCntrDLCIIndex": mcmFrPVCEndptCntrDLCIIndex,
       "mcmFrPVCEndptCntrAction": mcmFrPVCEndptCntrAction}
)
