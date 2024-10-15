# SNMP MIB module (VERILINK-ENTERPRISE-NCMQUAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VERILINK-ENTERPRISE-NCMQUAD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:19 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Verilink_ObjectIdentity = ObjectIdentity
verilink = _Verilink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321)
)
_As2000_ObjectIdentity = ObjectIdentity
as2000 = _As2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1)
)
_Ncm_quad_ObjectIdentity = ObjectIdentity
ncm_quad = _Ncm_quad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009)
)
_NcmquadConfigTable_Object = MibTable
ncmquadConfigTable = _NcmquadConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000)
)
if mibBuilder.loadTexts:
    ncmquadConfigTable.setStatus("mandatory")
_NcmquadConfigEntry_Object = MibTableRow
ncmquadConfigEntry = _NcmquadConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1)
)
ncmquadConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLineIndex"),
)
if mibBuilder.loadTexts:
    ncmquadConfigEntry.setStatus("mandatory")


class _NcmquadLineIndex_Type(Integer32):
    """Custom type ncmquadLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmquadLineIndex_Type.__name__ = "Integer32"
_NcmquadLineIndex_Object = MibTableColumn
ncmquadLineIndex = _NcmquadLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 1),
    _NcmquadLineIndex_Type()
)
ncmquadLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLineIndex.setStatus("mandatory")


class _NcmquadIfIndex_Type(Integer32):
    """Custom type ncmquadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmquadIfIndex_Type.__name__ = "Integer32"
_NcmquadIfIndex_Object = MibTableColumn
ncmquadIfIndex = _NcmquadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 2),
    _NcmquadIfIndex_Type()
)
ncmquadIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadIfIndex.setStatus("mandatory")


class _NcmquadEndId_Type(Integer32):
    """Custom type ncmquadEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 1),
          ("near-End", 0))
    )


_NcmquadEndId_Type.__name__ = "Integer32"
_NcmquadEndId_Object = MibTableColumn
ncmquadEndId = _NcmquadEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 3),
    _NcmquadEndId_Type()
)
ncmquadEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadEndId.setStatus("mandatory")


class _NcmquadPort_Type(Integer32):
    """Custom type ncmquadPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmquadPort_Type.__name__ = "Integer32"
_NcmquadPort_Object = MibTableColumn
ncmquadPort = _NcmquadPort_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 4),
    _NcmquadPort_Type()
)
ncmquadPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadPort.setStatus("mandatory")


class _NcmquadLineType_Type(Integer32):
    """Custom type ncmquadLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("d4", 3),
          ("eSF", 2),
          ("other", 1))
    )


_NcmquadLineType_Type.__name__ = "Integer32"
_NcmquadLineType_Object = MibTableColumn
ncmquadLineType = _NcmquadLineType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 5),
    _NcmquadLineType_Type()
)
ncmquadLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadLineType.setStatus("mandatory")


class _NcmquadLineCoding_Type(Integer32):
    """Custom type ncmquadLineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aMI", 5),
          ("b8ZS", 2),
          ("other", 6))
    )


_NcmquadLineCoding_Type.__name__ = "Integer32"
_NcmquadLineCoding_Object = MibTableColumn
ncmquadLineCoding = _NcmquadLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 6),
    _NcmquadLineCoding_Type()
)
ncmquadLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadLineCoding.setStatus("mandatory")


class _NcmquadFDL_Type(Integer32):
    """Custom type ncmquadFDL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NcmquadFDL_Type.__name__ = "Integer32"
_NcmquadFDL_Object = MibTableColumn
ncmquadFDL = _NcmquadFDL_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 7),
    _NcmquadFDL_Type()
)
ncmquadFDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadFDL.setStatus("mandatory")


class _NcmquadDensityPattern_Type(Integer32):
    """Custom type ncmquadDensityPattern based on Integer32"""
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
        *(("d12d5c80Zero", 3),
          ("d15Zeros", 2),
          ("d80Zeros", 1),
          ("disabled", 6),
          ("other", 5),
          ("tR-62411", 4))
    )


_NcmquadDensityPattern_Type.__name__ = "Integer32"
_NcmquadDensityPattern_Object = MibTableColumn
ncmquadDensityPattern = _NcmquadDensityPattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 8),
    _NcmquadDensityPattern_Type()
)
ncmquadDensityPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadDensityPattern.setStatus("mandatory")


class _NcmquadNetworkLineBuildOut_Type(Integer32):
    """Custom type ncmquadNetworkLineBuildOut based on Integer32"""
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
        *(("bldLn-0db", 1),
          ("bldLnNeg15db", 3),
          ("bldLnNeg22d5", 4),
          ("bldLnNeg7d5db", 2))
    )


_NcmquadNetworkLineBuildOut_Type.__name__ = "Integer32"
_NcmquadNetworkLineBuildOut_Object = MibTableColumn
ncmquadNetworkLineBuildOut = _NcmquadNetworkLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 9),
    _NcmquadNetworkLineBuildOut_Type()
)
ncmquadNetworkLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadNetworkLineBuildOut.setStatus("mandatory")


class _NcmquadNetworkLoopConfig_Type(Integer32):
    """Custom type ncmquadNetworkLoopConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NcmquadNetworkLoopConfig_Type.__name__ = "Integer32"
_NcmquadNetworkLoopConfig_Object = MibTableColumn
ncmquadNetworkLoopConfig = _NcmquadNetworkLoopConfig_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 10),
    _NcmquadNetworkLoopConfig_Type()
)
ncmquadNetworkLoopConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadNetworkLoopConfig.setStatus("mandatory")


class _NcmquadLineStatus_Type(Integer32):
    """Custom type ncmquadLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarms", 2),
          ("noAlarms", 1))
    )


_NcmquadLineStatus_Type.__name__ = "Integer32"
_NcmquadLineStatus_Object = MibTableColumn
ncmquadLineStatus = _NcmquadLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 11),
    _NcmquadLineStatus_Type()
)
ncmquadLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLineStatus.setStatus("mandatory")


class _NcmquadLoopbackConfig_Type(Integer32):
    """Custom type ncmquadLoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              10,
              11,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("noLoop", 1),
          ("quadActLLBBOP", 7),
          ("quadActLineLoop", 3),
          ("quadActLocalLoopbk", 5),
          ("quadActPLBBOP", 8),
          ("quadActPayloadLoop", 2),
          ("quadDeactLLBBOP", 13),
          ("quadDeactLineLoop", 10),
          ("quadDeactLocalLoopbk", 11),
          ("quadDeactPLBBOP", 14),
          ("quadDeactPayloadLoop", 9))
    )


_NcmquadLoopbackConfig_Type.__name__ = "Integer32"
_NcmquadLoopbackConfig_Object = MibTableColumn
ncmquadLoopbackConfig = _NcmquadLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 12),
    _NcmquadLoopbackConfig_Type()
)
ncmquadLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadLoopbackConfig.setStatus("mandatory")


class _NcmquadSendCode_Type(Integer32):
    """Custom type ncmquadSendCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("noCode", 1),
          ("other", 8),
          ("qRSS", 5),
          ("three-in-24type", 7))
    )


_NcmquadSendCode_Type.__name__ = "Integer32"
_NcmquadSendCode_Object = MibTableColumn
ncmquadSendCode = _NcmquadSendCode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 13),
    _NcmquadSendCode_Type()
)
ncmquadSendCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadSendCode.setStatus("mandatory")


class _NcmquadResetPerfReg_Type(Integer32):
    """Custom type ncmquadResetPerfReg based on Integer32"""
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


_NcmquadResetPerfReg_Type.__name__ = "Integer32"
_NcmquadResetPerfReg_Object = MibTableColumn
ncmquadResetPerfReg = _NcmquadResetPerfReg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 14),
    _NcmquadResetPerfReg_Type()
)
ncmquadResetPerfReg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadResetPerfReg.setStatus("mandatory")


class _NcmquadValidIntervals_Type(Integer32):
    """Custom type ncmquadValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_NcmquadValidIntervals_Type.__name__ = "Integer32"
_NcmquadValidIntervals_Object = MibTableColumn
ncmquadValidIntervals = _NcmquadValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 15),
    _NcmquadValidIntervals_Type()
)
ncmquadValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadValidIntervals.setStatus("mandatory")


class _NcmquadTimeElapsed_Type(Integer32):
    """Custom type ncmquadTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_NcmquadTimeElapsed_Type.__name__ = "Integer32"
_NcmquadTimeElapsed_Object = MibTableColumn
ncmquadTimeElapsed = _NcmquadTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 16),
    _NcmquadTimeElapsed_Type()
)
ncmquadTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadTimeElapsed.setStatus("mandatory")


class _NcmquadResetT1Error_Type(Integer32):
    """Custom type ncmquadResetT1Error based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_NcmquadResetT1Error_Type.__name__ = "Integer32"
_NcmquadResetT1Error_Object = MibTableColumn
ncmquadResetT1Error = _NcmquadResetT1Error_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11000, 1, 17),
    _NcmquadResetT1Error_Type()
)
ncmquadResetT1Error.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadResetT1Error.setStatus("mandatory")
_NcmquadLossCurrentTable_Object = MibTable
ncmquadLossCurrentTable = _NcmquadLossCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001)
)
if mibBuilder.loadTexts:
    ncmquadLossCurrentTable.setStatus("mandatory")
_NcmquadLCurrentEntry_Object = MibTableRow
ncmquadLCurrentEntry = _NcmquadLCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1)
)
ncmquadLCurrentEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLCurrentIndex"),
)
if mibBuilder.loadTexts:
    ncmquadLCurrentEntry.setStatus("mandatory")


class _NcmquadLCurrentIndex_Type(Integer32):
    """Custom type ncmquadLCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmquadLCurrentIndex_Type.__name__ = "Integer32"
_NcmquadLCurrentIndex_Object = MibTableColumn
ncmquadLCurrentIndex = _NcmquadLCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 1),
    _NcmquadLCurrentIndex_Type()
)
ncmquadLCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentIndex.setStatus("mandatory")


class _NcmquadCurrentEndId_Type(Integer32):
    """Custom type ncmquadCurrentEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 1),
          ("near-End", 0))
    )


_NcmquadCurrentEndId_Type.__name__ = "Integer32"
_NcmquadCurrentEndId_Object = MibTableColumn
ncmquadCurrentEndId = _NcmquadCurrentEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 2),
    _NcmquadCurrentEndId_Type()
)
ncmquadCurrentEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadCurrentEndId.setStatus("mandatory")
_NcmquadLCurrentASs_Type = Gauge32
_NcmquadLCurrentASs_Object = MibTableColumn
ncmquadLCurrentASs = _NcmquadLCurrentASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 3),
    _NcmquadLCurrentASs_Type()
)
ncmquadLCurrentASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentASs.setStatus("mandatory")
_NcmquadLCurrentLOSs_Type = Gauge32
_NcmquadLCurrentLOSs_Object = MibTableColumn
ncmquadLCurrentLOSs = _NcmquadLCurrentLOSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 4),
    _NcmquadLCurrentLOSs_Type()
)
ncmquadLCurrentLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentLOSs.setStatus("mandatory")
_NcmquadLCurrentAISs_Type = Gauge32
_NcmquadLCurrentAISs_Object = MibTableColumn
ncmquadLCurrentAISs = _NcmquadLCurrentAISs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 5),
    _NcmquadLCurrentAISs_Type()
)
ncmquadLCurrentAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentAISs.setStatus("mandatory")
_NcmquadLCurrentLOFs_Type = Gauge32
_NcmquadLCurrentLOFs_Object = MibTableColumn
ncmquadLCurrentLOFs = _NcmquadLCurrentLOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 6),
    _NcmquadLCurrentLOFs_Type()
)
ncmquadLCurrentLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentLOFs.setStatus("mandatory")
_NcmquadLCurrentOFs_Type = Gauge32
_NcmquadLCurrentOFs_Object = MibTableColumn
ncmquadLCurrentOFs = _NcmquadLCurrentOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 7),
    _NcmquadLCurrentOFs_Type()
)
ncmquadLCurrentOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentOFs.setStatus("mandatory")
_NcmquadLCurrentESs_Type = Gauge32
_NcmquadLCurrentESs_Object = MibTableColumn
ncmquadLCurrentESs = _NcmquadLCurrentESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 8),
    _NcmquadLCurrentESs_Type()
)
ncmquadLCurrentESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentESs.setStatus("mandatory")
_NcmquadLCurrentSESs_Type = Gauge32
_NcmquadLCurrentSESs_Object = MibTableColumn
ncmquadLCurrentSESs = _NcmquadLCurrentSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 9),
    _NcmquadLCurrentSESs_Type()
)
ncmquadLCurrentSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentSESs.setStatus("mandatory")
_NcmquadLCurrentSEFs_Type = Gauge32
_NcmquadLCurrentSEFs_Object = MibTableColumn
ncmquadLCurrentSEFs = _NcmquadLCurrentSEFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 10),
    _NcmquadLCurrentSEFs_Type()
)
ncmquadLCurrentSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentSEFs.setStatus("mandatory")
_NcmquadLCurrentUASs_Type = Gauge32
_NcmquadLCurrentUASs_Object = MibTableColumn
ncmquadLCurrentUASs = _NcmquadLCurrentUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 11),
    _NcmquadLCurrentUASs_Type()
)
ncmquadLCurrentUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentUASs.setStatus("mandatory")
_NcmquadLCurrentBESs_Type = Gauge32
_NcmquadLCurrentBESs_Object = MibTableColumn
ncmquadLCurrentBESs = _NcmquadLCurrentBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 12),
    _NcmquadLCurrentBESs_Type()
)
ncmquadLCurrentBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentBESs.setStatus("mandatory")
_NcmquadLCurrentESAs_Type = Gauge32
_NcmquadLCurrentESAs_Object = MibTableColumn
ncmquadLCurrentESAs = _NcmquadLCurrentESAs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 13),
    _NcmquadLCurrentESAs_Type()
)
ncmquadLCurrentESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentESAs.setStatus("mandatory")
_NcmquadLCurrentSASs_Type = Gauge32
_NcmquadLCurrentSASs_Object = MibTableColumn
ncmquadLCurrentSASs = _NcmquadLCurrentSASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 14),
    _NcmquadLCurrentSASs_Type()
)
ncmquadLCurrentSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentSASs.setStatus("mandatory")
_NcmquadLCurrentCSSs_Type = Gauge32
_NcmquadLCurrentCSSs_Object = MibTableColumn
ncmquadLCurrentCSSs = _NcmquadLCurrentCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 15),
    _NcmquadLCurrentCSSs_Type()
)
ncmquadLCurrentCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentCSSs.setStatus("mandatory")
_NcmquadLCurrentLOFCs_Type = Gauge32
_NcmquadLCurrentLOFCs_Object = MibTableColumn
ncmquadLCurrentLOFCs = _NcmquadLCurrentLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11001, 1, 16),
    _NcmquadLCurrentLOFCs_Type()
)
ncmquadLCurrentLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLCurrentLOFCs.setStatus("mandatory")
_NcmquadLossIntervalTable_Object = MibTable
ncmquadLossIntervalTable = _NcmquadLossIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002)
)
if mibBuilder.loadTexts:
    ncmquadLossIntervalTable.setStatus("mandatory")
_NcmquadLIntervalEntry_Object = MibTableRow
ncmquadLIntervalEntry = _NcmquadLIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1)
)
ncmquadLIntervalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLIntervalIndex"),
)
if mibBuilder.loadTexts:
    ncmquadLIntervalEntry.setStatus("mandatory")


class _NcmquadLIntervalIndex_Type(Integer32):
    """Custom type ncmquadLIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmquadLIntervalIndex_Type.__name__ = "Integer32"
_NcmquadLIntervalIndex_Object = MibTableColumn
ncmquadLIntervalIndex = _NcmquadLIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 1),
    _NcmquadLIntervalIndex_Type()
)
ncmquadLIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalIndex.setStatus("mandatory")


class _NcmquadLIntervalEndId_Type(Integer32):
    """Custom type ncmquadLIntervalEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 1),
          ("near-End", 0))
    )


_NcmquadLIntervalEndId_Type.__name__ = "Integer32"
_NcmquadLIntervalEndId_Object = MibTableColumn
ncmquadLIntervalEndId = _NcmquadLIntervalEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 2),
    _NcmquadLIntervalEndId_Type()
)
ncmquadLIntervalEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalEndId.setStatus("mandatory")


class _NcmquadLIntervalNumber_Type(Integer32):
    """Custom type ncmquadLIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_NcmquadLIntervalNumber_Type.__name__ = "Integer32"
_NcmquadLIntervalNumber_Object = MibTableColumn
ncmquadLIntervalNumber = _NcmquadLIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 3),
    _NcmquadLIntervalNumber_Type()
)
ncmquadLIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalNumber.setStatus("mandatory")
_NcmquadLIntervalASs_Type = Gauge32
_NcmquadLIntervalASs_Object = MibTableColumn
ncmquadLIntervalASs = _NcmquadLIntervalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 4),
    _NcmquadLIntervalASs_Type()
)
ncmquadLIntervalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalASs.setStatus("mandatory")
_NcmquadLIntervalLOSs_Type = Gauge32
_NcmquadLIntervalLOSs_Object = MibTableColumn
ncmquadLIntervalLOSs = _NcmquadLIntervalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 5),
    _NcmquadLIntervalLOSs_Type()
)
ncmquadLIntervalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalLOSs.setStatus("mandatory")
_NcmquadLIntervalAISs_Type = Gauge32
_NcmquadLIntervalAISs_Object = MibTableColumn
ncmquadLIntervalAISs = _NcmquadLIntervalAISs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 6),
    _NcmquadLIntervalAISs_Type()
)
ncmquadLIntervalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalAISs.setStatus("mandatory")
_NcmquadLIntervalLOFs_Type = Gauge32
_NcmquadLIntervalLOFs_Object = MibTableColumn
ncmquadLIntervalLOFs = _NcmquadLIntervalLOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 7),
    _NcmquadLIntervalLOFs_Type()
)
ncmquadLIntervalLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalLOFs.setStatus("mandatory")
_NcmquadLIntervalOFs_Type = Gauge32
_NcmquadLIntervalOFs_Object = MibTableColumn
ncmquadLIntervalOFs = _NcmquadLIntervalOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 8),
    _NcmquadLIntervalOFs_Type()
)
ncmquadLIntervalOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalOFs.setStatus("mandatory")
_NcmquadLIntervalESs_Type = Gauge32
_NcmquadLIntervalESs_Object = MibTableColumn
ncmquadLIntervalESs = _NcmquadLIntervalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 9),
    _NcmquadLIntervalESs_Type()
)
ncmquadLIntervalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalESs.setStatus("mandatory")
_NcmquadLIntervalSESs_Type = Gauge32
_NcmquadLIntervalSESs_Object = MibTableColumn
ncmquadLIntervalSESs = _NcmquadLIntervalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 10),
    _NcmquadLIntervalSESs_Type()
)
ncmquadLIntervalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalSESs.setStatus("mandatory")
_NcmquadLIntervalSEFs_Type = Gauge32
_NcmquadLIntervalSEFs_Object = MibTableColumn
ncmquadLIntervalSEFs = _NcmquadLIntervalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 11),
    _NcmquadLIntervalSEFs_Type()
)
ncmquadLIntervalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalSEFs.setStatus("mandatory")
_NcmquadLIntervalUASs_Type = Gauge32
_NcmquadLIntervalUASs_Object = MibTableColumn
ncmquadLIntervalUASs = _NcmquadLIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 12),
    _NcmquadLIntervalUASs_Type()
)
ncmquadLIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalUASs.setStatus("mandatory")
_NcmquadLIntervalBESs_Type = Gauge32
_NcmquadLIntervalBESs_Object = MibTableColumn
ncmquadLIntervalBESs = _NcmquadLIntervalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 13),
    _NcmquadLIntervalBESs_Type()
)
ncmquadLIntervalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalBESs.setStatus("mandatory")
_NcmquadLIntervalESAs_Type = Gauge32
_NcmquadLIntervalESAs_Object = MibTableColumn
ncmquadLIntervalESAs = _NcmquadLIntervalESAs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 14),
    _NcmquadLIntervalESAs_Type()
)
ncmquadLIntervalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalESAs.setStatus("mandatory")
_NcmquadLIntervalSASs_Type = Gauge32
_NcmquadLIntervalSASs_Object = MibTableColumn
ncmquadLIntervalSASs = _NcmquadLIntervalSASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 15),
    _NcmquadLIntervalSASs_Type()
)
ncmquadLIntervalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalSASs.setStatus("mandatory")
_NcmquadLIntervalCSSs_Type = Gauge32
_NcmquadLIntervalCSSs_Object = MibTableColumn
ncmquadLIntervalCSSs = _NcmquadLIntervalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 16),
    _NcmquadLIntervalCSSs_Type()
)
ncmquadLIntervalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalCSSs.setStatus("mandatory")
_NcmquadLIntervalLOFCs_Type = Gauge32
_NcmquadLIntervalLOFCs_Object = MibTableColumn
ncmquadLIntervalLOFCs = _NcmquadLIntervalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11002, 1, 17),
    _NcmquadLIntervalLOFCs_Type()
)
ncmquadLIntervalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLIntervalLOFCs.setStatus("mandatory")
_NcmquadLossTotalTable_Object = MibTable
ncmquadLossTotalTable = _NcmquadLossTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003)
)
if mibBuilder.loadTexts:
    ncmquadLossTotalTable.setStatus("mandatory")
_NcmquadLTotalEntry_Object = MibTableRow
ncmquadLTotalEntry = _NcmquadLTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1)
)
ncmquadLTotalEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLTotalIndex"),
)
if mibBuilder.loadTexts:
    ncmquadLTotalEntry.setStatus("mandatory")


class _NcmquadLTotalIndex_Type(Integer32):
    """Custom type ncmquadLTotalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmquadLTotalIndex_Type.__name__ = "Integer32"
_NcmquadLTotalIndex_Object = MibTableColumn
ncmquadLTotalIndex = _NcmquadLTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 1),
    _NcmquadLTotalIndex_Type()
)
ncmquadLTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalIndex.setStatus("mandatory")


class _NcmquadTotalEndId_Type(Integer32):
    """Custom type ncmquadTotalEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 1),
          ("near-End", 0))
    )


_NcmquadTotalEndId_Type.__name__ = "Integer32"
_NcmquadTotalEndId_Object = MibTableColumn
ncmquadTotalEndId = _NcmquadTotalEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 2),
    _NcmquadTotalEndId_Type()
)
ncmquadTotalEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadTotalEndId.setStatus("mandatory")
_NcmquadLTotalASs_Type = Gauge32
_NcmquadLTotalASs_Object = MibTableColumn
ncmquadLTotalASs = _NcmquadLTotalASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 3),
    _NcmquadLTotalASs_Type()
)
ncmquadLTotalASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalASs.setStatus("mandatory")
_NcmquadLTotalLOSs_Type = Gauge32
_NcmquadLTotalLOSs_Object = MibTableColumn
ncmquadLTotalLOSs = _NcmquadLTotalLOSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 4),
    _NcmquadLTotalLOSs_Type()
)
ncmquadLTotalLOSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalLOSs.setStatus("mandatory")
_NcmquadLTotalAISs_Type = Gauge32
_NcmquadLTotalAISs_Object = MibTableColumn
ncmquadLTotalAISs = _NcmquadLTotalAISs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 5),
    _NcmquadLTotalAISs_Type()
)
ncmquadLTotalAISs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalAISs.setStatus("mandatory")
_NcmquadLTotalLOFs_Type = Gauge32
_NcmquadLTotalLOFs_Object = MibTableColumn
ncmquadLTotalLOFs = _NcmquadLTotalLOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 6),
    _NcmquadLTotalLOFs_Type()
)
ncmquadLTotalLOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalLOFs.setStatus("mandatory")
_NcmquadLTotalOFs_Type = Gauge32
_NcmquadLTotalOFs_Object = MibTableColumn
ncmquadLTotalOFs = _NcmquadLTotalOFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 7),
    _NcmquadLTotalOFs_Type()
)
ncmquadLTotalOFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalOFs.setStatus("mandatory")
_NcmquadLTotalESs_Type = Gauge32
_NcmquadLTotalESs_Object = MibTableColumn
ncmquadLTotalESs = _NcmquadLTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 8),
    _NcmquadLTotalESs_Type()
)
ncmquadLTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalESs.setStatus("mandatory")
_NcmquadLTotalSESs_Type = Gauge32
_NcmquadLTotalSESs_Object = MibTableColumn
ncmquadLTotalSESs = _NcmquadLTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 9),
    _NcmquadLTotalSESs_Type()
)
ncmquadLTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalSESs.setStatus("mandatory")
_NcmquadLTotalSEFs_Type = Gauge32
_NcmquadLTotalSEFs_Object = MibTableColumn
ncmquadLTotalSEFs = _NcmquadLTotalSEFs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 10),
    _NcmquadLTotalSEFs_Type()
)
ncmquadLTotalSEFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalSEFs.setStatus("mandatory")
_NcmquadLTotalUASs_Type = Gauge32
_NcmquadLTotalUASs_Object = MibTableColumn
ncmquadLTotalUASs = _NcmquadLTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 11),
    _NcmquadLTotalUASs_Type()
)
ncmquadLTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalUASs.setStatus("mandatory")
_NcmquadLTotalBESs_Type = Gauge32
_NcmquadLTotalBESs_Object = MibTableColumn
ncmquadLTotalBESs = _NcmquadLTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 12),
    _NcmquadLTotalBESs_Type()
)
ncmquadLTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalBESs.setStatus("mandatory")
_NcmquadLTotalESAs_Type = Gauge32
_NcmquadLTotalESAs_Object = MibTableColumn
ncmquadLTotalESAs = _NcmquadLTotalESAs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 13),
    _NcmquadLTotalESAs_Type()
)
ncmquadLTotalESAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalESAs.setStatus("mandatory")
_NcmquadLTotalSASs_Type = Gauge32
_NcmquadLTotalSASs_Object = MibTableColumn
ncmquadLTotalSASs = _NcmquadLTotalSASs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 14),
    _NcmquadLTotalSASs_Type()
)
ncmquadLTotalSASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalSASs.setStatus("mandatory")
_NcmquadLTotalCSSs_Type = Gauge32
_NcmquadLTotalCSSs_Object = MibTableColumn
ncmquadLTotalCSSs = _NcmquadLTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 15),
    _NcmquadLTotalCSSs_Type()
)
ncmquadLTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalCSSs.setStatus("mandatory")
_NcmquadLTotalLOFCs_Type = Gauge32
_NcmquadLTotalLOFCs_Object = MibTableColumn
ncmquadLTotalLOFCs = _NcmquadLTotalLOFCs_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11003, 1, 16),
    _NcmquadLTotalLOFCs_Type()
)
ncmquadLTotalLOFCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadLTotalLOFCs.setStatus("mandatory")
_NcmadvancedT1ConfigTable_Object = MibTable
ncmadvancedT1ConfigTable = _NcmadvancedT1ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004)
)
if mibBuilder.loadTexts:
    ncmadvancedT1ConfigTable.setStatus("mandatory")
_NcmadvancedT1ConfigEntry_Object = MibTableRow
ncmadvancedT1ConfigEntry = _NcmadvancedT1ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1)
)
ncmadvancedT1ConfigEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmadvancedT1LineIndex"),
)
if mibBuilder.loadTexts:
    ncmadvancedT1ConfigEntry.setStatus("mandatory")


class _NcmadvancedT1LineIndex_Type(Integer32):
    """Custom type ncmadvancedT1LineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmadvancedT1LineIndex_Type.__name__ = "Integer32"
_NcmadvancedT1LineIndex_Object = MibTableColumn
ncmadvancedT1LineIndex = _NcmadvancedT1LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 1),
    _NcmadvancedT1LineIndex_Type()
)
ncmadvancedT1LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmadvancedT1LineIndex.setStatus("mandatory")


class _NcmportIdentifier_Type(Integer32):
    """Custom type ncmportIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("port-1", 0),
          ("port-2", 1),
          ("port-3", 2),
          ("port-4", 3))
    )


_NcmportIdentifier_Type.__name__ = "Integer32"
_NcmportIdentifier_Object = MibTableColumn
ncmportIdentifier = _NcmportIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 2),
    _NcmportIdentifier_Type()
)
ncmportIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmportIdentifier.setStatus("mandatory")


class _NcmfdlMode_Type(Integer32):
    """Custom type ncmfdlMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("terminated", 0))
    )


_NcmfdlMode_Type.__name__ = "Integer32"
_NcmfdlMode_Object = MibTableColumn
ncmfdlMode = _NcmfdlMode_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 3),
    _NcmfdlMode_Type()
)
ncmfdlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlMode.setStatus("mandatory")


class _NcmfdlStandard_Type(Integer32):
    """Custom type ncmfdlStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8,
              12)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 0),
          ("type-54016", 4),
          ("type-T1-403", 8),
          ("type-both", 12))
    )


_NcmfdlStandard_Type.__name__ = "Integer32"
_NcmfdlStandard_Object = MibTableColumn
ncmfdlStandard = _NcmfdlStandard_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 4),
    _NcmfdlStandard_Type()
)
ncmfdlStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlStandard.setStatus("mandatory")


class _NcmfdlPerformanceReport_Type(Integer32):
    """Custom type ncmfdlPerformanceReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("telco", 64),
          ("user", 32))
    )


_NcmfdlPerformanceReport_Type.__name__ = "Integer32"
_NcmfdlPerformanceReport_Object = MibTableColumn
ncmfdlPerformanceReport = _NcmfdlPerformanceReport_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 5),
    _NcmfdlPerformanceReport_Type()
)
ncmfdlPerformanceReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlPerformanceReport.setStatus("mandatory")


class _NcmfdlLBEnableDisable_Type(Integer32):
    """Custom type ncmfdlLBEnableDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_NcmfdlLBEnableDisable_Type.__name__ = "Integer32"
_NcmfdlLBEnableDisable_Object = MibTableColumn
ncmfdlLBEnableDisable = _NcmfdlLBEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 6),
    _NcmfdlLBEnableDisable_Type()
)
ncmfdlLBEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlLBEnableDisable.setStatus("mandatory")


class _NcmfdlLLBT1BOPMsg_Type(Integer32):
    """Custom type ncmfdlLLBT1BOPMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 2))
    )


_NcmfdlLLBT1BOPMsg_Type.__name__ = "Integer32"
_NcmfdlLLBT1BOPMsg_Object = MibTableColumn
ncmfdlLLBT1BOPMsg = _NcmfdlLLBT1BOPMsg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 7),
    _NcmfdlLLBT1BOPMsg_Type()
)
ncmfdlLLBT1BOPMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlLLBT1BOPMsg.setStatus("mandatory")


class _NcmfdlPLBT1BOPMsg_Type(Integer32):
    """Custom type ncmfdlPLBT1BOPMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 4))
    )


_NcmfdlPLBT1BOPMsg_Type.__name__ = "Integer32"
_NcmfdlPLBT1BOPMsg_Object = MibTableColumn
ncmfdlPLBT1BOPMsg = _NcmfdlPLBT1BOPMsg_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 8),
    _NcmfdlPLBT1BOPMsg_Type()
)
ncmfdlPLBT1BOPMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlPLBT1BOPMsg.setStatus("mandatory")


class _NcmfdlIdlePattern_Type(Integer32):
    """Custom type ncmfdlIdlePattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("all-ones", 0),
          ("flags", 1))
    )


_NcmfdlIdlePattern_Type.__name__ = "Integer32"
_NcmfdlIdlePattern_Object = MibTableColumn
ncmfdlIdlePattern = _NcmfdlIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 9),
    _NcmfdlIdlePattern_Type()
)
ncmfdlIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlIdlePattern.setStatus("mandatory")


class _NcmfdlMonitoringCsuType_Type(Integer32):
    """Custom type ncmfdlMonitoringCsuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("no-polling", 4),
          ("polling", 0),
          ("unsolicited-messages", 8))
    )


_NcmfdlMonitoringCsuType_Type.__name__ = "Integer32"
_NcmfdlMonitoringCsuType_Object = MibTableColumn
ncmfdlMonitoringCsuType = _NcmfdlMonitoringCsuType_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11004, 1, 10),
    _NcmfdlMonitoringCsuType_Type()
)
ncmfdlMonitoringCsuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmfdlMonitoringCsuType.setStatus("mandatory")
_NcmquadSyncTable_Object = MibTable
ncmquadSyncTable = _NcmquadSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005)
)
if mibBuilder.loadTexts:
    ncmquadSyncTable.setStatus("mandatory")
_NcmquadSyncEntry_Object = MibTableRow
ncmquadSyncEntry = _NcmquadSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1)
)
ncmquadSyncEntry.setIndexNames(
    (0, "VERILINK-ENTERPRISE-NCMQUAD-MIB", "ncmquadLineIndex"),
)
if mibBuilder.loadTexts:
    ncmquadSyncEntry.setStatus("mandatory")


class _NcmquadSyncIndex_Type(Integer32):
    """Custom type ncmquadSyncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_NcmquadSyncIndex_Type.__name__ = "Integer32"
_NcmquadSyncIndex_Object = MibTableColumn
ncmquadSyncIndex = _NcmquadSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 1),
    _NcmquadSyncIndex_Type()
)
ncmquadSyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadSyncIndex.setStatus("mandatory")


class _NcmquadSyncEndId_Type(Integer32):
    """Custom type ncmquadSyncEndId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("far-End", 1),
          ("near-End", 0))
    )


_NcmquadSyncEndId_Type.__name__ = "Integer32"
_NcmquadSyncEndId_Object = MibTableColumn
ncmquadSyncEndId = _NcmquadSyncEndId_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 2),
    _NcmquadSyncEndId_Type()
)
ncmquadSyncEndId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadSyncEndId.setStatus("mandatory")


class _NcmquadClkSyncSource_Type(Integer32):
    """Custom type ncmquadClkSyncSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alt-1", 1),
          ("alt-2", 2),
          ("primary", 0))
    )


_NcmquadClkSyncSource_Type.__name__ = "Integer32"
_NcmquadClkSyncSource_Object = MibTableColumn
ncmquadClkSyncSource = _NcmquadClkSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 3),
    _NcmquadClkSyncSource_Type()
)
ncmquadClkSyncSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ncmquadClkSyncSource.setStatus("mandatory")


class _NcmquadClkCardPrim_Type(Integer32):
    """Custom type ncmquadClkCardPrim based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("c-1", 0),
          ("c-10", 9),
          ("c-11", 10),
          ("c-12", 11),
          ("c-13", 12),
          ("c-2", 1),
          ("c-3", 2),
          ("c-4", 3),
          ("c-5", 4),
          ("c-6", 5),
          ("c-7", 6),
          ("c-8", 7),
          ("c-9", 8))
    )


_NcmquadClkCardPrim_Type.__name__ = "Integer32"
_NcmquadClkCardPrim_Object = MibTableColumn
ncmquadClkCardPrim = _NcmquadClkCardPrim_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 4),
    _NcmquadClkCardPrim_Type()
)
ncmquadClkCardPrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadClkCardPrim.setStatus("mandatory")


class _NcmquadClkSyncPrimary_Type(Integer32):
    """Custom type ncmquadClkSyncPrimary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 0),
          ("masterNet1", 2),
          ("masterNet2", 3),
          ("masterNet3", 4),
          ("masterNet4", 5))
    )


_NcmquadClkSyncPrimary_Type.__name__ = "Integer32"
_NcmquadClkSyncPrimary_Object = MibTableColumn
ncmquadClkSyncPrimary = _NcmquadClkSyncPrimary_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 5),
    _NcmquadClkSyncPrimary_Type()
)
ncmquadClkSyncPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadClkSyncPrimary.setStatus("mandatory")


class _NcmquadAutoRestorePrim_Type(Integer32):
    """Custom type ncmquadAutoRestorePrim based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NcmquadAutoRestorePrim_Type.__name__ = "Integer32"
_NcmquadAutoRestorePrim_Object = MibTableColumn
ncmquadAutoRestorePrim = _NcmquadAutoRestorePrim_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 6),
    _NcmquadAutoRestorePrim_Type()
)
ncmquadAutoRestorePrim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadAutoRestorePrim.setStatus("mandatory")


class _NcmquadClkCardAlt1_Type(Integer32):
    """Custom type ncmquadClkCardAlt1 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("c-1", 0),
          ("c-10", 9),
          ("c-11", 10),
          ("c-12", 11),
          ("c-13", 12),
          ("c-2", 1),
          ("c-3", 2),
          ("c-4", 3),
          ("c-5", 4),
          ("c-6", 5),
          ("c-7", 6),
          ("c-8", 7),
          ("c-9", 8))
    )


_NcmquadClkCardAlt1_Type.__name__ = "Integer32"
_NcmquadClkCardAlt1_Object = MibTableColumn
ncmquadClkCardAlt1 = _NcmquadClkCardAlt1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 7),
    _NcmquadClkCardAlt1_Type()
)
ncmquadClkCardAlt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadClkCardAlt1.setStatus("mandatory")


class _NcmquadClkSyncAlt1_Type(Integer32):
    """Custom type ncmquadClkSyncAlt1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 0),
          ("masterNet1", 2),
          ("masterNet2", 3),
          ("masterNet3", 4),
          ("masterNet4", 5))
    )


_NcmquadClkSyncAlt1_Type.__name__ = "Integer32"
_NcmquadClkSyncAlt1_Object = MibTableColumn
ncmquadClkSyncAlt1 = _NcmquadClkSyncAlt1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 8),
    _NcmquadClkSyncAlt1_Type()
)
ncmquadClkSyncAlt1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadClkSyncAlt1.setStatus("mandatory")


class _NcmquadAutoRestore1_Type(Integer32):
    """Custom type ncmquadAutoRestore1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NcmquadAutoRestore1_Type.__name__ = "Integer32"
_NcmquadAutoRestore1_Object = MibTableColumn
ncmquadAutoRestore1 = _NcmquadAutoRestore1_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 9),
    _NcmquadAutoRestore1_Type()
)
ncmquadAutoRestore1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadAutoRestore1.setStatus("mandatory")


class _NcmquadClkCardAlt2_Type(Integer32):
    """Custom type ncmquadClkCardAlt2 based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("c-1", 0),
          ("c-10", 9),
          ("c-11", 10),
          ("c-12", 11),
          ("c-13", 12),
          ("c-2", 1),
          ("c-3", 2),
          ("c-4", 3),
          ("c-5", 4),
          ("c-6", 5),
          ("c-7", 6),
          ("c-8", 7),
          ("c-9", 8))
    )


_NcmquadClkCardAlt2_Type.__name__ = "Integer32"
_NcmquadClkCardAlt2_Object = MibTableColumn
ncmquadClkCardAlt2 = _NcmquadClkCardAlt2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 10),
    _NcmquadClkCardAlt2_Type()
)
ncmquadClkCardAlt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadClkCardAlt2.setStatus("mandatory")


class _NcmquadClkSyncAlt2_Type(Integer32):
    """Custom type ncmquadClkSyncAlt2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("internal", 0),
          ("masterNet1", 2),
          ("masterNet2", 3),
          ("masterNet3", 4),
          ("masterNet4", 5))
    )


_NcmquadClkSyncAlt2_Type.__name__ = "Integer32"
_NcmquadClkSyncAlt2_Object = MibTableColumn
ncmquadClkSyncAlt2 = _NcmquadClkSyncAlt2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 11),
    _NcmquadClkSyncAlt2_Type()
)
ncmquadClkSyncAlt2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadClkSyncAlt2.setStatus("mandatory")


class _NcmquadAutoRestore2_Type(Integer32):
    """Custom type ncmquadAutoRestore2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NcmquadAutoRestore2_Type.__name__ = "Integer32"
_NcmquadAutoRestore2_Object = MibTableColumn
ncmquadAutoRestore2 = _NcmquadAutoRestore2_Object(
    (1, 3, 6, 1, 4, 1, 321, 1, 3009, 11005, 1, 12),
    _NcmquadAutoRestore2_Type()
)
ncmquadAutoRestore2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncmquadAutoRestore2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VERILINK-ENTERPRISE-NCMQUAD-MIB",
    **{"verilink": verilink,
       "as2000": as2000,
       "ncm-quad": ncm_quad,
       "ncmquadConfigTable": ncmquadConfigTable,
       "ncmquadConfigEntry": ncmquadConfigEntry,
       "ncmquadLineIndex": ncmquadLineIndex,
       "ncmquadIfIndex": ncmquadIfIndex,
       "ncmquadEndId": ncmquadEndId,
       "ncmquadPort": ncmquadPort,
       "ncmquadLineType": ncmquadLineType,
       "ncmquadLineCoding": ncmquadLineCoding,
       "ncmquadFDL": ncmquadFDL,
       "ncmquadDensityPattern": ncmquadDensityPattern,
       "ncmquadNetworkLineBuildOut": ncmquadNetworkLineBuildOut,
       "ncmquadNetworkLoopConfig": ncmquadNetworkLoopConfig,
       "ncmquadLineStatus": ncmquadLineStatus,
       "ncmquadLoopbackConfig": ncmquadLoopbackConfig,
       "ncmquadSendCode": ncmquadSendCode,
       "ncmquadResetPerfReg": ncmquadResetPerfReg,
       "ncmquadValidIntervals": ncmquadValidIntervals,
       "ncmquadTimeElapsed": ncmquadTimeElapsed,
       "ncmquadResetT1Error": ncmquadResetT1Error,
       "ncmquadLossCurrentTable": ncmquadLossCurrentTable,
       "ncmquadLCurrentEntry": ncmquadLCurrentEntry,
       "ncmquadLCurrentIndex": ncmquadLCurrentIndex,
       "ncmquadCurrentEndId": ncmquadCurrentEndId,
       "ncmquadLCurrentASs": ncmquadLCurrentASs,
       "ncmquadLCurrentLOSs": ncmquadLCurrentLOSs,
       "ncmquadLCurrentAISs": ncmquadLCurrentAISs,
       "ncmquadLCurrentLOFs": ncmquadLCurrentLOFs,
       "ncmquadLCurrentOFs": ncmquadLCurrentOFs,
       "ncmquadLCurrentESs": ncmquadLCurrentESs,
       "ncmquadLCurrentSESs": ncmquadLCurrentSESs,
       "ncmquadLCurrentSEFs": ncmquadLCurrentSEFs,
       "ncmquadLCurrentUASs": ncmquadLCurrentUASs,
       "ncmquadLCurrentBESs": ncmquadLCurrentBESs,
       "ncmquadLCurrentESAs": ncmquadLCurrentESAs,
       "ncmquadLCurrentSASs": ncmquadLCurrentSASs,
       "ncmquadLCurrentCSSs": ncmquadLCurrentCSSs,
       "ncmquadLCurrentLOFCs": ncmquadLCurrentLOFCs,
       "ncmquadLossIntervalTable": ncmquadLossIntervalTable,
       "ncmquadLIntervalEntry": ncmquadLIntervalEntry,
       "ncmquadLIntervalIndex": ncmquadLIntervalIndex,
       "ncmquadLIntervalEndId": ncmquadLIntervalEndId,
       "ncmquadLIntervalNumber": ncmquadLIntervalNumber,
       "ncmquadLIntervalASs": ncmquadLIntervalASs,
       "ncmquadLIntervalLOSs": ncmquadLIntervalLOSs,
       "ncmquadLIntervalAISs": ncmquadLIntervalAISs,
       "ncmquadLIntervalLOFs": ncmquadLIntervalLOFs,
       "ncmquadLIntervalOFs": ncmquadLIntervalOFs,
       "ncmquadLIntervalESs": ncmquadLIntervalESs,
       "ncmquadLIntervalSESs": ncmquadLIntervalSESs,
       "ncmquadLIntervalSEFs": ncmquadLIntervalSEFs,
       "ncmquadLIntervalUASs": ncmquadLIntervalUASs,
       "ncmquadLIntervalBESs": ncmquadLIntervalBESs,
       "ncmquadLIntervalESAs": ncmquadLIntervalESAs,
       "ncmquadLIntervalSASs": ncmquadLIntervalSASs,
       "ncmquadLIntervalCSSs": ncmquadLIntervalCSSs,
       "ncmquadLIntervalLOFCs": ncmquadLIntervalLOFCs,
       "ncmquadLossTotalTable": ncmquadLossTotalTable,
       "ncmquadLTotalEntry": ncmquadLTotalEntry,
       "ncmquadLTotalIndex": ncmquadLTotalIndex,
       "ncmquadTotalEndId": ncmquadTotalEndId,
       "ncmquadLTotalASs": ncmquadLTotalASs,
       "ncmquadLTotalLOSs": ncmquadLTotalLOSs,
       "ncmquadLTotalAISs": ncmquadLTotalAISs,
       "ncmquadLTotalLOFs": ncmquadLTotalLOFs,
       "ncmquadLTotalOFs": ncmquadLTotalOFs,
       "ncmquadLTotalESs": ncmquadLTotalESs,
       "ncmquadLTotalSESs": ncmquadLTotalSESs,
       "ncmquadLTotalSEFs": ncmquadLTotalSEFs,
       "ncmquadLTotalUASs": ncmquadLTotalUASs,
       "ncmquadLTotalBESs": ncmquadLTotalBESs,
       "ncmquadLTotalESAs": ncmquadLTotalESAs,
       "ncmquadLTotalSASs": ncmquadLTotalSASs,
       "ncmquadLTotalCSSs": ncmquadLTotalCSSs,
       "ncmquadLTotalLOFCs": ncmquadLTotalLOFCs,
       "ncmadvancedT1ConfigTable": ncmadvancedT1ConfigTable,
       "ncmadvancedT1ConfigEntry": ncmadvancedT1ConfigEntry,
       "ncmadvancedT1LineIndex": ncmadvancedT1LineIndex,
       "ncmportIdentifier": ncmportIdentifier,
       "ncmfdlMode": ncmfdlMode,
       "ncmfdlStandard": ncmfdlStandard,
       "ncmfdlPerformanceReport": ncmfdlPerformanceReport,
       "ncmfdlLBEnableDisable": ncmfdlLBEnableDisable,
       "ncmfdlLLBT1BOPMsg": ncmfdlLLBT1BOPMsg,
       "ncmfdlPLBT1BOPMsg": ncmfdlPLBT1BOPMsg,
       "ncmfdlIdlePattern": ncmfdlIdlePattern,
       "ncmfdlMonitoringCsuType": ncmfdlMonitoringCsuType,
       "ncmquadSyncTable": ncmquadSyncTable,
       "ncmquadSyncEntry": ncmquadSyncEntry,
       "ncmquadSyncIndex": ncmquadSyncIndex,
       "ncmquadSyncEndId": ncmquadSyncEndId,
       "ncmquadClkSyncSource": ncmquadClkSyncSource,
       "ncmquadClkCardPrim": ncmquadClkCardPrim,
       "ncmquadClkSyncPrimary": ncmquadClkSyncPrimary,
       "ncmquadAutoRestorePrim": ncmquadAutoRestorePrim,
       "ncmquadClkCardAlt1": ncmquadClkCardAlt1,
       "ncmquadClkSyncAlt1": ncmquadClkSyncAlt1,
       "ncmquadAutoRestore1": ncmquadAutoRestore1,
       "ncmquadClkCardAlt2": ncmquadClkCardAlt2,
       "ncmquadClkSyncAlt2": ncmquadClkSyncAlt2,
       "ncmquadAutoRestore2": ncmquadAutoRestore2}
)
