# SNMP MIB module (MICOM-TRAFFIC-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-TRAFFIC-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:52 2024
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

_Micom_2tm_ObjectIdentity = ObjectIdentity
micom_2tm = _Micom_2tm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27)
)
_Tm2_configuration_ObjectIdentity = ObjectIdentity
tm2_configuration = _Tm2_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1)
)
_McmTMclassParamTable_Object = MibTable
mcmTMclassParamTable = _McmTMclassParamTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1)
)
if mibBuilder.loadTexts:
    mcmTMclassParamTable.setStatus("mandatory")
_McmTMclassParamEntry_Object = MibTableRow
mcmTMclassParamEntry = _McmTMclassParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1)
)
mcmTMclassParamEntry.setIndexNames(
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassParamSccNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassParamFRDlciNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassParamMPANLDlciNum"),
)
if mibBuilder.loadTexts:
    mcmTMclassParamEntry.setStatus("mandatory")


class _McmTMclassParamSccNum_Type(Integer32):
    """Custom type mcmTMclassParamSccNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmTMclassParamSccNum_Type.__name__ = "Integer32"
_McmTMclassParamSccNum_Object = MibTableColumn
mcmTMclassParamSccNum = _McmTMclassParamSccNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 1),
    _McmTMclassParamSccNum_Type()
)
mcmTMclassParamSccNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamSccNum.setStatus("mandatory")


class _McmTMclassParamFRDlciNum_Type(Integer32):
    """Custom type mcmTMclassParamFRDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_McmTMclassParamFRDlciNum_Type.__name__ = "Integer32"
_McmTMclassParamFRDlciNum_Object = MibTableColumn
mcmTMclassParamFRDlciNum = _McmTMclassParamFRDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 2),
    _McmTMclassParamFRDlciNum_Type()
)
mcmTMclassParamFRDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamFRDlciNum.setStatus("mandatory")


class _McmTMclassParamMPANLDlciNum_Type(Integer32):
    """Custom type mcmTMclassParamMPANLDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65535, 65535),
        ValueRangeConstraint(0, 1024),
    )


_McmTMclassParamMPANLDlciNum_Type.__name__ = "Integer32"
_McmTMclassParamMPANLDlciNum_Object = MibTableColumn
mcmTMclassParamMPANLDlciNum = _McmTMclassParamMPANLDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 3),
    _McmTMclassParamMPANLDlciNum_Type()
)
mcmTMclassParamMPANLDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamMPANLDlciNum.setStatus("mandatory")


class _McmTMclassParamPriority_Type(Integer32):
    """Custom type mcmTMclassParamPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_McmTMclassParamPriority_Type.__name__ = "Integer32"
_McmTMclassParamPriority_Object = MibTableColumn
mcmTMclassParamPriority = _McmTMclassParamPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 4),
    _McmTMclassParamPriority_Type()
)
mcmTMclassParamPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamPriority.setStatus("mandatory")
_McmTMclassParamCIR_Type = Integer32
_McmTMclassParamCIR_Object = MibTableColumn
mcmTMclassParamCIR = _McmTMclassParamCIR_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 5),
    _McmTMclassParamCIR_Type()
)
mcmTMclassParamCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamCIR.setStatus("mandatory")
_McmTMclassParamExcessInfoRate_Type = Integer32
_McmTMclassParamExcessInfoRate_Object = MibTableColumn
mcmTMclassParamExcessInfoRate = _McmTMclassParamExcessInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 6),
    _McmTMclassParamExcessInfoRate_Type()
)
mcmTMclassParamExcessInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamExcessInfoRate.setStatus("mandatory")


class _McmTMclassParamMaxBurstBytesSz_Type(Integer32):
    """Custom type mcmTMclassParamMaxBurstBytesSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000000),
    )


_McmTMclassParamMaxBurstBytesSz_Type.__name__ = "Integer32"
_McmTMclassParamMaxBurstBytesSz_Object = MibTableColumn
mcmTMclassParamMaxBurstBytesSz = _McmTMclassParamMaxBurstBytesSz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 7),
    _McmTMclassParamMaxBurstBytesSz_Type()
)
mcmTMclassParamMaxBurstBytesSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamMaxBurstBytesSz.setStatus("mandatory")


class _McmTMclassParamMaxBurstFrmSz_Type(Integer32):
    """Custom type mcmTMclassParamMaxBurstFrmSz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_McmTMclassParamMaxBurstFrmSz_Type.__name__ = "Integer32"
_McmTMclassParamMaxBurstFrmSz_Object = MibTableColumn
mcmTMclassParamMaxBurstFrmSz = _McmTMclassParamMaxBurstFrmSz_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 8),
    _McmTMclassParamMaxBurstFrmSz_Type()
)
mcmTMclassParamMaxBurstFrmSz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamMaxBurstFrmSz.setStatus("mandatory")


class _McmTMclassParamAvgPacketSize_Type(Integer32):
    """Custom type mcmTMclassParamAvgPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536),
    )


_McmTMclassParamAvgPacketSize_Type.__name__ = "Integer32"
_McmTMclassParamAvgPacketSize_Object = MibTableColumn
mcmTMclassParamAvgPacketSize = _McmTMclassParamAvgPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 9),
    _McmTMclassParamAvgPacketSize_Type()
)
mcmTMclassParamAvgPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamAvgPacketSize.setStatus("mandatory")


class _McmTMclassParamMaxPacketSize_Type(Integer32):
    """Custom type mcmTMclassParamMaxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536),
    )


_McmTMclassParamMaxPacketSize_Type.__name__ = "Integer32"
_McmTMclassParamMaxPacketSize_Object = MibTableColumn
mcmTMclassParamMaxPacketSize = _McmTMclassParamMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 10),
    _McmTMclassParamMaxPacketSize_Type()
)
mcmTMclassParamMaxPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamMaxPacketSize.setStatus("mandatory")


class _McmTMclassParamDelta_Type(Integer32):
    """Custom type mcmTMclassParamDelta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmTMclassParamDelta_Type.__name__ = "Integer32"
_McmTMclassParamDelta_Object = MibTableColumn
mcmTMclassParamDelta = _McmTMclassParamDelta_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 11),
    _McmTMclassParamDelta_Type()
)
mcmTMclassParamDelta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamDelta.setStatus("mandatory")


class _McmTMclassParamSFrames_Type(Integer32):
    """Custom type mcmTMclassParamSFrames based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmTMclassParamSFrames_Type.__name__ = "Integer32"
_McmTMclassParamSFrames_Object = MibTableColumn
mcmTMclassParamSFrames = _McmTMclassParamSFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 1, 1, 12),
    _McmTMclassParamSFrames_Type()
)
mcmTMclassParamSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassParamSFrames.setStatus("mandatory")
_McmTMGlobalParamGroup_ObjectIdentity = ObjectIdentity
mcmTMGlobalParamGroup = _McmTMGlobalParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2)
)


class _McmTmRateEnforcement_Type(Integer32):
    """Custom type mcmTmRateEnforcement based on Integer32"""
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


_McmTmRateEnforcement_Type.__name__ = "Integer32"
_McmTmRateEnforcement_Object = MibScalar
mcmTmRateEnforcement = _McmTmRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2, 1),
    _McmTmRateEnforcement_Type()
)
mcmTmRateEnforcement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTmRateEnforcement.setStatus("mandatory")


class _McmTmLineEfficiency_Type(Integer32):
    """Custom type mcmTmLineEfficiency based on Integer32"""
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


_McmTmLineEfficiency_Type.__name__ = "Integer32"
_McmTmLineEfficiency_Object = MibScalar
mcmTmLineEfficiency = _McmTmLineEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2, 2),
    _McmTmLineEfficiency_Type()
)
mcmTmLineEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTmLineEfficiency.setStatus("mandatory")


class _McmTmWeightedRoundRobin_Type(Integer32):
    """Custom type mcmTmWeightedRoundRobin based on Integer32"""
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


_McmTmWeightedRoundRobin_Type.__name__ = "Integer32"
_McmTmWeightedRoundRobin_Object = MibScalar
mcmTmWeightedRoundRobin = _McmTmWeightedRoundRobin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 2, 3),
    _McmTmWeightedRoundRobin_Type()
)
mcmTmWeightedRoundRobin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTmWeightedRoundRobin.setStatus("mandatory")
_NvmTMGlobalParamGroup_ObjectIdentity = ObjectIdentity
nvmTMGlobalParamGroup = _NvmTMGlobalParamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3)
)


class _NvmTmRateEnforcement_Type(Integer32):
    """Custom type nvmTmRateEnforcement based on Integer32"""
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


_NvmTmRateEnforcement_Type.__name__ = "Integer32"
_NvmTmRateEnforcement_Object = MibScalar
nvmTmRateEnforcement = _NvmTmRateEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3, 1),
    _NvmTmRateEnforcement_Type()
)
nvmTmRateEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmTmRateEnforcement.setStatus("mandatory")


class _NvmTmLineEfficiency_Type(Integer32):
    """Custom type nvmTmLineEfficiency based on Integer32"""
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


_NvmTmLineEfficiency_Type.__name__ = "Integer32"
_NvmTmLineEfficiency_Object = MibScalar
nvmTmLineEfficiency = _NvmTmLineEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3, 2),
    _NvmTmLineEfficiency_Type()
)
nvmTmLineEfficiency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmTmLineEfficiency.setStatus("mandatory")


class _NvmTmWeightedRoundRobin_Type(Integer32):
    """Custom type nvmTmWeightedRoundRobin based on Integer32"""
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


_NvmTmWeightedRoundRobin_Type.__name__ = "Integer32"
_NvmTmWeightedRoundRobin_Object = MibScalar
nvmTmWeightedRoundRobin = _NvmTmWeightedRoundRobin_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 1, 3, 3),
    _NvmTmWeightedRoundRobin_Type()
)
nvmTmWeightedRoundRobin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nvmTmWeightedRoundRobin.setStatus("mandatory")
_Tm2_status_ObjectIdentity = ObjectIdentity
tm2_status = _Tm2_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2)
)
_McmTMclassStateTable_Object = MibTable
mcmTMclassStateTable = _McmTMclassStateTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1)
)
if mibBuilder.loadTexts:
    mcmTMclassStateTable.setStatus("mandatory")
_McmTMclassStateEntry_Object = MibTableRow
mcmTMclassStateEntry = _McmTMclassStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1)
)
mcmTMclassStateEntry.setIndexNames(
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStateSccNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStateFRDlciNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStateMPANLDlciNum"),
)
if mibBuilder.loadTexts:
    mcmTMclassStateEntry.setStatus("mandatory")


class _McmTMclassStateSccNum_Type(Integer32):
    """Custom type mcmTMclassStateSccNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmTMclassStateSccNum_Type.__name__ = "Integer32"
_McmTMclassStateSccNum_Object = MibTableColumn
mcmTMclassStateSccNum = _McmTMclassStateSccNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 1),
    _McmTMclassStateSccNum_Type()
)
mcmTMclassStateSccNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateSccNum.setStatus("mandatory")


class _McmTMclassStateFRDlciNum_Type(Integer32):
    """Custom type mcmTMclassStateFRDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_McmTMclassStateFRDlciNum_Type.__name__ = "Integer32"
_McmTMclassStateFRDlciNum_Object = MibTableColumn
mcmTMclassStateFRDlciNum = _McmTMclassStateFRDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 2),
    _McmTMclassStateFRDlciNum_Type()
)
mcmTMclassStateFRDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateFRDlciNum.setStatus("mandatory")


class _McmTMclassStateMPANLDlciNum_Type(Integer32):
    """Custom type mcmTMclassStateMPANLDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65535, 65535),
        ValueRangeConstraint(0, 1024),
    )


_McmTMclassStateMPANLDlciNum_Type.__name__ = "Integer32"
_McmTMclassStateMPANLDlciNum_Object = MibTableColumn
mcmTMclassStateMPANLDlciNum = _McmTMclassStateMPANLDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 3),
    _McmTMclassStateMPANLDlciNum_Type()
)
mcmTMclassStateMPANLDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateMPANLDlciNum.setStatus("mandatory")
_McmTMclassStateCurrentInfoRate_Type = Integer32
_McmTMclassStateCurrentInfoRate_Object = MibTableColumn
mcmTMclassStateCurrentInfoRate = _McmTMclassStateCurrentInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 4),
    _McmTMclassStateCurrentInfoRate_Type()
)
mcmTMclassStateCurrentInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateCurrentInfoRate.setStatus("mandatory")
_McmTMclassStateMinInfoRate_Type = Integer32
_McmTMclassStateMinInfoRate_Object = MibTableColumn
mcmTMclassStateMinInfoRate = _McmTMclassStateMinInfoRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 5),
    _McmTMclassStateMinInfoRate_Type()
)
mcmTMclassStateMinInfoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateMinInfoRate.setStatus("mandatory")
_McmTMclassStateAvgTxRate_Type = Integer32
_McmTMclassStateAvgTxRate_Object = MibTableColumn
mcmTMclassStateAvgTxRate = _McmTMclassStateAvgTxRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 6),
    _McmTMclassStateAvgTxRate_Type()
)
mcmTMclassStateAvgTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateAvgTxRate.setStatus("mandatory")
_McmTMclassStateBytesQueued_Type = Counter32
_McmTMclassStateBytesQueued_Object = MibTableColumn
mcmTMclassStateBytesQueued = _McmTMclassStateBytesQueued_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 7),
    _McmTMclassStateBytesQueued_Type()
)
mcmTMclassStateBytesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateBytesQueued.setStatus("mandatory")
_McmTMclassStateFramesQueued_Type = Counter32
_McmTMclassStateFramesQueued_Object = MibTableColumn
mcmTMclassStateFramesQueued = _McmTMclassStateFramesQueued_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 2, 1, 1, 8),
    _McmTMclassStateFramesQueued_Type()
)
mcmTMclassStateFramesQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStateFramesQueued.setStatus("mandatory")
_Tm2_statistics_ObjectIdentity = ObjectIdentity
tm2_statistics = _Tm2_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3)
)
_McmTMclassStatsTable_Object = MibTable
mcmTMclassStatsTable = _McmTMclassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1)
)
if mibBuilder.loadTexts:
    mcmTMclassStatsTable.setStatus("mandatory")
_McmTMclassStatsEntry_Object = MibTableRow
mcmTMclassStatsEntry = _McmTMclassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1)
)
mcmTMclassStatsEntry.setIndexNames(
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStatsSccNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStatsFRDlciNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMclassStatsMPANLDlciNum"),
)
if mibBuilder.loadTexts:
    mcmTMclassStatsEntry.setStatus("mandatory")


class _McmTMclassStatsSccNum_Type(Integer32):
    """Custom type mcmTMclassStatsSccNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmTMclassStatsSccNum_Type.__name__ = "Integer32"
_McmTMclassStatsSccNum_Object = MibTableColumn
mcmTMclassStatsSccNum = _McmTMclassStatsSccNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 1),
    _McmTMclassStatsSccNum_Type()
)
mcmTMclassStatsSccNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsSccNum.setStatus("mandatory")


class _McmTMclassStatsFRDlciNum_Type(Integer32):
    """Custom type mcmTMclassStatsFRDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_McmTMclassStatsFRDlciNum_Type.__name__ = "Integer32"
_McmTMclassStatsFRDlciNum_Object = MibTableColumn
mcmTMclassStatsFRDlciNum = _McmTMclassStatsFRDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 2),
    _McmTMclassStatsFRDlciNum_Type()
)
mcmTMclassStatsFRDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsFRDlciNum.setStatus("mandatory")


class _McmTMclassStatsMPANLDlciNum_Type(Integer32):
    """Custom type mcmTMclassStatsMPANLDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65535, 65535),
        ValueRangeConstraint(0, 1024),
    )


_McmTMclassStatsMPANLDlciNum_Type.__name__ = "Integer32"
_McmTMclassStatsMPANLDlciNum_Object = MibTableColumn
mcmTMclassStatsMPANLDlciNum = _McmTMclassStatsMPANLDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 3),
    _McmTMclassStatsMPANLDlciNum_Type()
)
mcmTMclassStatsMPANLDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsMPANLDlciNum.setStatus("mandatory")
_McmTMclassStatsTotalBytesTx_Type = Counter32
_McmTMclassStatsTotalBytesTx_Object = MibTableColumn
mcmTMclassStatsTotalBytesTx = _McmTMclassStatsTotalBytesTx_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 4),
    _McmTMclassStatsTotalBytesTx_Type()
)
mcmTMclassStatsTotalBytesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalBytesTx.setStatus("mandatory")
_McmTMclassStatsTotalFramesTx_Type = Counter32
_McmTMclassStatsTotalFramesTx_Object = MibTableColumn
mcmTMclassStatsTotalFramesTx = _McmTMclassStatsTotalFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 5),
    _McmTMclassStatsTotalFramesTx_Type()
)
mcmTMclassStatsTotalFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalFramesTx.setStatus("mandatory")
_McmTMclassStatsTotalFragsTx_Type = Counter32
_McmTMclassStatsTotalFragsTx_Object = MibTableColumn
mcmTMclassStatsTotalFragsTx = _McmTMclassStatsTotalFragsTx_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 6),
    _McmTMclassStatsTotalFragsTx_Type()
)
mcmTMclassStatsTotalFragsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalFragsTx.setStatus("mandatory")
_McmTMclassStatsTotalBytesRx_Type = Counter32
_McmTMclassStatsTotalBytesRx_Object = MibTableColumn
mcmTMclassStatsTotalBytesRx = _McmTMclassStatsTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 7),
    _McmTMclassStatsTotalBytesRx_Type()
)
mcmTMclassStatsTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalBytesRx.setStatus("mandatory")
_McmTMclassStatsTotalFramesRx_Type = Counter32
_McmTMclassStatsTotalFramesRx_Object = MibTableColumn
mcmTMclassStatsTotalFramesRx = _McmTMclassStatsTotalFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 8),
    _McmTMclassStatsTotalFramesRx_Type()
)
mcmTMclassStatsTotalFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalFramesRx.setStatus("mandatory")
_McmTMclassStatsTotalFragsRx_Type = Counter32
_McmTMclassStatsTotalFragsRx_Object = MibTableColumn
mcmTMclassStatsTotalFragsRx = _McmTMclassStatsTotalFragsRx_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 9),
    _McmTMclassStatsTotalFragsRx_Type()
)
mcmTMclassStatsTotalFragsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalFragsRx.setStatus("mandatory")
_McmTMclassStatsPktsDiscQueFull_Type = Counter32
_McmTMclassStatsPktsDiscQueFull_Object = MibTableColumn
mcmTMclassStatsPktsDiscQueFull = _McmTMclassStatsPktsDiscQueFull_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 10),
    _McmTMclassStatsPktsDiscQueFull_Type()
)
mcmTMclassStatsPktsDiscQueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsPktsDiscQueFull.setStatus("mandatory")
_McmTMclassStatsPktsDiscQueOverflow_Type = Counter32
_McmTMclassStatsPktsDiscQueOverflow_Object = MibTableColumn
mcmTMclassStatsPktsDiscQueOverflow = _McmTMclassStatsPktsDiscQueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 11),
    _McmTMclassStatsPktsDiscQueOverflow_Type()
)
mcmTMclassStatsPktsDiscQueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsPktsDiscQueOverflow.setStatus("mandatory")
_McmTMclassStatsPktsDiscEmitFail_Type = Counter32
_McmTMclassStatsPktsDiscEmitFail_Object = MibTableColumn
mcmTMclassStatsPktsDiscEmitFail = _McmTMclassStatsPktsDiscEmitFail_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 12),
    _McmTMclassStatsPktsDiscEmitFail_Type()
)
mcmTMclassStatsPktsDiscEmitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsPktsDiscEmitFail.setStatus("mandatory")
_McmTMclassStatsPktsDiscEmitQueFull_Type = Counter32
_McmTMclassStatsPktsDiscEmitQueFull_Object = MibTableColumn
mcmTMclassStatsPktsDiscEmitQueFull = _McmTMclassStatsPktsDiscEmitQueFull_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 13),
    _McmTMclassStatsPktsDiscEmitQueFull_Type()
)
mcmTMclassStatsPktsDiscEmitQueFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsPktsDiscEmitQueFull.setStatus("mandatory")
_McmTMclassStatsTotalFecnClearRcvd_Type = Counter32
_McmTMclassStatsTotalFecnClearRcvd_Object = MibTableColumn
mcmTMclassStatsTotalFecnClearRcvd = _McmTMclassStatsTotalFecnClearRcvd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 14),
    _McmTMclassStatsTotalFecnClearRcvd_Type()
)
mcmTMclassStatsTotalFecnClearRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalFecnClearRcvd.setStatus("mandatory")
_McmTMclassStatsTotalFecnSetRcvd_Type = Counter32
_McmTMclassStatsTotalFecnSetRcvd_Object = MibTableColumn
mcmTMclassStatsTotalFecnSetRcvd = _McmTMclassStatsTotalFecnSetRcvd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 15),
    _McmTMclassStatsTotalFecnSetRcvd_Type()
)
mcmTMclassStatsTotalFecnSetRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalFecnSetRcvd.setStatus("mandatory")
_McmTMclassStatsTotalBecnRcvd_Type = Counter32
_McmTMclassStatsTotalBecnRcvd_Object = MibTableColumn
mcmTMclassStatsTotalBecnRcvd = _McmTMclassStatsTotalBecnRcvd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 3, 1, 1, 16),
    _McmTMclassStatsTotalBecnRcvd_Type()
)
mcmTMclassStatsTotalBecnRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMclassStatsTotalBecnRcvd.setStatus("mandatory")
_Tm2_control_ObjectIdentity = ObjectIdentity
tm2_control = _Tm2_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4)
)
_McmTMcntlCounterTable_Object = MibTable
mcmTMcntlCounterTable = _McmTMcntlCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1)
)
if mibBuilder.loadTexts:
    mcmTMcntlCounterTable.setStatus("obsolete")
_McmTMcntlCounterEntry_Object = MibTableRow
mcmTMcntlCounterEntry = _McmTMcntlCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1)
)
mcmTMcntlCounterEntry.setIndexNames(
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMcntlCounterSccNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMcntlCounterFRDlciNum"),
    (0, "MICOM-TRAFFIC-MGMT-MIB", "mcmTMcntlCounterMPANLDlciNum"),
)
if mibBuilder.loadTexts:
    mcmTMcntlCounterEntry.setStatus("obsolete")


class _McmTMcntlCounterSccNum_Type(Integer32):
    """Custom type mcmTMcntlCounterSccNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McmTMcntlCounterSccNum_Type.__name__ = "Integer32"
_McmTMcntlCounterSccNum_Object = MibTableColumn
mcmTMcntlCounterSccNum = _McmTMcntlCounterSccNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 1),
    _McmTMcntlCounterSccNum_Type()
)
mcmTMcntlCounterSccNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMcntlCounterSccNum.setStatus("obsolete")


class _McmTMcntlCounterFRDlciNum_Type(Integer32):
    """Custom type mcmTMcntlCounterFRDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1007),
    )


_McmTMcntlCounterFRDlciNum_Type.__name__ = "Integer32"
_McmTMcntlCounterFRDlciNum_Object = MibTableColumn
mcmTMcntlCounterFRDlciNum = _McmTMcntlCounterFRDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 2),
    _McmTMcntlCounterFRDlciNum_Type()
)
mcmTMcntlCounterFRDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMcntlCounterFRDlciNum.setStatus("obsolete")


class _McmTMcntlCounterMPANLDlciNum_Type(Integer32):
    """Custom type mcmTMcntlCounterMPANLDlciNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_McmTMcntlCounterMPANLDlciNum_Type.__name__ = "Integer32"
_McmTMcntlCounterMPANLDlciNum_Object = MibTableColumn
mcmTMcntlCounterMPANLDlciNum = _McmTMcntlCounterMPANLDlciNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 3),
    _McmTMcntlCounterMPANLDlciNum_Type()
)
mcmTMcntlCounterMPANLDlciNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmTMcntlCounterMPANLDlciNum.setStatus("obsolete")


class _McmTMcntlCounterClassStatsReset_Type(Integer32):
    """Custom type mcmTMcntlCounterClassStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_McmTMcntlCounterClassStatsReset_Type.__name__ = "Integer32"
_McmTMcntlCounterClassStatsReset_Object = MibTableColumn
mcmTMcntlCounterClassStatsReset = _McmTMcntlCounterClassStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 27, 4, 1, 1, 4),
    _McmTMcntlCounterClassStatsReset_Type()
)
mcmTMcntlCounterClassStatsReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmTMcntlCounterClassStatsReset.setStatus("obsolete")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-TRAFFIC-MGMT-MIB",
    **{"micom-2tm": micom_2tm,
       "tm2-configuration": tm2_configuration,
       "mcmTMclassParamTable": mcmTMclassParamTable,
       "mcmTMclassParamEntry": mcmTMclassParamEntry,
       "mcmTMclassParamSccNum": mcmTMclassParamSccNum,
       "mcmTMclassParamFRDlciNum": mcmTMclassParamFRDlciNum,
       "mcmTMclassParamMPANLDlciNum": mcmTMclassParamMPANLDlciNum,
       "mcmTMclassParamPriority": mcmTMclassParamPriority,
       "mcmTMclassParamCIR": mcmTMclassParamCIR,
       "mcmTMclassParamExcessInfoRate": mcmTMclassParamExcessInfoRate,
       "mcmTMclassParamMaxBurstBytesSz": mcmTMclassParamMaxBurstBytesSz,
       "mcmTMclassParamMaxBurstFrmSz": mcmTMclassParamMaxBurstFrmSz,
       "mcmTMclassParamAvgPacketSize": mcmTMclassParamAvgPacketSize,
       "mcmTMclassParamMaxPacketSize": mcmTMclassParamMaxPacketSize,
       "mcmTMclassParamDelta": mcmTMclassParamDelta,
       "mcmTMclassParamSFrames": mcmTMclassParamSFrames,
       "mcmTMGlobalParamGroup": mcmTMGlobalParamGroup,
       "mcmTmRateEnforcement": mcmTmRateEnforcement,
       "mcmTmLineEfficiency": mcmTmLineEfficiency,
       "mcmTmWeightedRoundRobin": mcmTmWeightedRoundRobin,
       "nvmTMGlobalParamGroup": nvmTMGlobalParamGroup,
       "nvmTmRateEnforcement": nvmTmRateEnforcement,
       "nvmTmLineEfficiency": nvmTmLineEfficiency,
       "nvmTmWeightedRoundRobin": nvmTmWeightedRoundRobin,
       "tm2-status": tm2_status,
       "mcmTMclassStateTable": mcmTMclassStateTable,
       "mcmTMclassStateEntry": mcmTMclassStateEntry,
       "mcmTMclassStateSccNum": mcmTMclassStateSccNum,
       "mcmTMclassStateFRDlciNum": mcmTMclassStateFRDlciNum,
       "mcmTMclassStateMPANLDlciNum": mcmTMclassStateMPANLDlciNum,
       "mcmTMclassStateCurrentInfoRate": mcmTMclassStateCurrentInfoRate,
       "mcmTMclassStateMinInfoRate": mcmTMclassStateMinInfoRate,
       "mcmTMclassStateAvgTxRate": mcmTMclassStateAvgTxRate,
       "mcmTMclassStateBytesQueued": mcmTMclassStateBytesQueued,
       "mcmTMclassStateFramesQueued": mcmTMclassStateFramesQueued,
       "tm2-statistics": tm2_statistics,
       "mcmTMclassStatsTable": mcmTMclassStatsTable,
       "mcmTMclassStatsEntry": mcmTMclassStatsEntry,
       "mcmTMclassStatsSccNum": mcmTMclassStatsSccNum,
       "mcmTMclassStatsFRDlciNum": mcmTMclassStatsFRDlciNum,
       "mcmTMclassStatsMPANLDlciNum": mcmTMclassStatsMPANLDlciNum,
       "mcmTMclassStatsTotalBytesTx": mcmTMclassStatsTotalBytesTx,
       "mcmTMclassStatsTotalFramesTx": mcmTMclassStatsTotalFramesTx,
       "mcmTMclassStatsTotalFragsTx": mcmTMclassStatsTotalFragsTx,
       "mcmTMclassStatsTotalBytesRx": mcmTMclassStatsTotalBytesRx,
       "mcmTMclassStatsTotalFramesRx": mcmTMclassStatsTotalFramesRx,
       "mcmTMclassStatsTotalFragsRx": mcmTMclassStatsTotalFragsRx,
       "mcmTMclassStatsPktsDiscQueFull": mcmTMclassStatsPktsDiscQueFull,
       "mcmTMclassStatsPktsDiscQueOverflow": mcmTMclassStatsPktsDiscQueOverflow,
       "mcmTMclassStatsPktsDiscEmitFail": mcmTMclassStatsPktsDiscEmitFail,
       "mcmTMclassStatsPktsDiscEmitQueFull": mcmTMclassStatsPktsDiscEmitQueFull,
       "mcmTMclassStatsTotalFecnClearRcvd": mcmTMclassStatsTotalFecnClearRcvd,
       "mcmTMclassStatsTotalFecnSetRcvd": mcmTMclassStatsTotalFecnSetRcvd,
       "mcmTMclassStatsTotalBecnRcvd": mcmTMclassStatsTotalBecnRcvd,
       "tm2-control": tm2_control,
       "mcmTMcntlCounterTable": mcmTMcntlCounterTable,
       "mcmTMcntlCounterEntry": mcmTMcntlCounterEntry,
       "mcmTMcntlCounterSccNum": mcmTMcntlCounterSccNum,
       "mcmTMcntlCounterFRDlciNum": mcmTMcntlCounterFRDlciNum,
       "mcmTMcntlCounterMPANLDlciNum": mcmTMcntlCounterMPANLDlciNum,
       "mcmTMcntlCounterClassStatsReset": mcmTMcntlCounterClassStatsReset}
)
