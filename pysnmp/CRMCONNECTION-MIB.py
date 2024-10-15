# SNMP MIB module (CRMCONNECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CRMCONNECTION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:51 2024
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

(atmTrafficDescrParamIndex,
 atmVclVci,
 atmVclVpi,
 atmVplVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmTrafficDescrParamIndex",
    "atmVclVci",
    "atmVclVpi",
    "atmVplVpi")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Ntt_ObjectIdentity = ObjectIdentity
ntt = _Ntt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2)
)
_Ba3000_ObjectIdentity = ObjectIdentity
ba3000 = _Ba3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8)
)
_CrmCommon_ObjectIdentity = ObjectIdentity
crmCommon = _CrmCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1)
)
_CrmConnection_ObjectIdentity = ObjectIdentity
crmConnection = _CrmConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1)
)
_CrmTrPrmTable_Object = MibTable
crmTrPrmTable = _CrmTrPrmTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    crmTrPrmTable.setStatus("mandatory")
_CrmTrPrmEntry_Object = MibTableRow
crmTrPrmEntry = _CrmTrPrmEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1)
)
crmTrPrmEntry.setIndexNames(
    (0, "CRMCONNECTION-MIB", "crmTrPrmIndex"),
)
if mibBuilder.loadTexts:
    crmTrPrmEntry.setStatus("mandatory")


class _CrmTrPrmIndex_Type(Integer32):
    """Custom type crmTrPrmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrPrmIndex_Type.__name__ = "Integer32"
_CrmTrPrmIndex_Object = MibTableColumn
crmTrPrmIndex = _CrmTrPrmIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 1),
    _CrmTrPrmIndex_Type()
)
crmTrPrmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    crmTrPrmIndex.setStatus("mandatory")


class _CrmTrPrmCategory_Type(Integer32):
    """Custom type crmTrPrmCategory based on Integer32"""
    defaultValue = 5


_CrmTrPrmCategory_Object = MibTableColumn
crmTrPrmCategory = _CrmTrPrmCategory_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 2),
    _CrmTrPrmCategory_Type()
)
crmTrPrmCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmCategory.setStatus("mandatory")


class _CrmTrPrmCDVT_Type(Integer32):
    """Custom type crmTrPrmCDVT based on Integer32"""
    defaultValue = 720

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrPrmCDVT_Type.__name__ = "Integer32"
_CrmTrPrmCDVT_Object = MibTableColumn
crmTrPrmCDVT = _CrmTrPrmCDVT_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 3),
    _CrmTrPrmCDVT_Type()
)
crmTrPrmCDVT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmCDVT.setStatus("mandatory")


class _CrmTrPrmCellDelayPriority_Type(Integer32):
    """Custom type crmTrPrmCellDelayPriority based on Integer32"""
    defaultValue = 4


_CrmTrPrmCellDelayPriority_Object = MibTableColumn
crmTrPrmCellDelayPriority = _CrmTrPrmCellDelayPriority_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 4),
    _CrmTrPrmCellDelayPriority_Type()
)
crmTrPrmCellDelayPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmCellDelayPriority.setStatus("mandatory")


class _CrmTrPrmCellLossPriority_Type(Integer32):
    """Custom type crmTrPrmCellLossPriority based on Integer32"""
    defaultValue = 1


_CrmTrPrmCellLossPriority_Object = MibTableColumn
crmTrPrmCellLossPriority = _CrmTrPrmCellLossPriority_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 5),
    _CrmTrPrmCellLossPriority_Type()
)
crmTrPrmCellLossPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmCellLossPriority.setStatus("mandatory")


class _CrmTrPrmUPCInfo1_Type(Integer32):
    """Custom type crmTrPrmUPCInfo1 based on Integer32"""
    defaultValue = 1


_CrmTrPrmUPCInfo1_Object = MibTableColumn
crmTrPrmUPCInfo1 = _CrmTrPrmUPCInfo1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 6),
    _CrmTrPrmUPCInfo1_Type()
)
crmTrPrmUPCInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmUPCInfo1.setStatus("mandatory")


class _CrmTrPrmUPCInfo2_Type(Integer32):
    """Custom type crmTrPrmUPCInfo2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrPrmUPCInfo2_Type.__name__ = "Integer32"
_CrmTrPrmUPCInfo2_Object = MibTableColumn
crmTrPrmUPCInfo2 = _CrmTrPrmUPCInfo2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 7),
    _CrmTrPrmUPCInfo2_Type()
)
crmTrPrmUPCInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmUPCInfo2.setStatus("mandatory")


class _CrmTrPrmUPCInfo3_Type(Integer32):
    """Custom type crmTrPrmUPCInfo3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrPrmUPCInfo3_Type.__name__ = "Integer32"
_CrmTrPrmUPCInfo3_Object = MibTableColumn
crmTrPrmUPCInfo3 = _CrmTrPrmUPCInfo3_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 8),
    _CrmTrPrmUPCInfo3_Type()
)
crmTrPrmUPCInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmUPCInfo3.setStatus("mandatory")


class _CrmTrPrmUPCInfo4_Type(Integer32):
    """Custom type crmTrPrmUPCInfo4 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrPrmUPCInfo4_Type.__name__ = "Integer32"
_CrmTrPrmUPCInfo4_Object = MibTableColumn
crmTrPrmUPCInfo4 = _CrmTrPrmUPCInfo4_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 9),
    _CrmTrPrmUPCInfo4_Type()
)
crmTrPrmUPCInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmUPCInfo4.setStatus("mandatory")


class _CrmTrPrmShapingInfo1_Type(Integer32):
    """Custom type crmTrPrmShapingInfo1 based on Integer32"""
    defaultValue = 1


_CrmTrPrmShapingInfo1_Object = MibTableColumn
crmTrPrmShapingInfo1 = _CrmTrPrmShapingInfo1_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 10),
    _CrmTrPrmShapingInfo1_Type()
)
crmTrPrmShapingInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmShapingInfo1.setStatus("mandatory")


class _CrmTrPrmShapingInfo2_Type(Integer32):
    """Custom type crmTrPrmShapingInfo2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrPrmShapingInfo2_Type.__name__ = "Integer32"
_CrmTrPrmShapingInfo2_Object = MibTableColumn
crmTrPrmShapingInfo2 = _CrmTrPrmShapingInfo2_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 11),
    _CrmTrPrmShapingInfo2_Type()
)
crmTrPrmShapingInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmShapingInfo2.setStatus("mandatory")


class _CrmTrPrmRowStatus_Type(Integer32):
    """Custom type crmTrPrmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmTrPrmRowStatus_Type.__name__ = "Integer32"
_CrmTrPrmRowStatus_Object = MibTableColumn
crmTrPrmRowStatus = _CrmTrPrmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 12),
    _CrmTrPrmRowStatus_Type()
)
crmTrPrmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmRowStatus.setStatus("mandatory")


class _CrmTrPrmEpdPpd_Type(Integer32):
    """Custom type crmTrPrmEpdPpd based on Integer32"""
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
        *(("epdppdoff", 1),
          ("epdppdon", 3),
          ("ppdon", 2))
    )


_CrmTrPrmEpdPpd_Type.__name__ = "Integer32"
_CrmTrPrmEpdPpd_Object = MibTableColumn
crmTrPrmEpdPpd = _CrmTrPrmEpdPpd_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 13),
    _CrmTrPrmEpdPpd_Type()
)
crmTrPrmEpdPpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmEpdPpd.setStatus("mandatory")


class _CrmTrPrmHeavyCongestionTh_Type(Integer32):
    """Custom type crmTrPrmHeavyCongestionTh based on Integer32"""
    defaultValue = 80


_CrmTrPrmHeavyCongestionTh_Object = MibTableColumn
crmTrPrmHeavyCongestionTh = _CrmTrPrmHeavyCongestionTh_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 14),
    _CrmTrPrmHeavyCongestionTh_Type()
)
crmTrPrmHeavyCongestionTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmHeavyCongestionTh.setStatus("mandatory")


class _CrmTrPrmLightCongestionTh_Type(Integer32):
    """Custom type crmTrPrmLightCongestionTh based on Integer32"""
    defaultValue = 60


_CrmTrPrmLightCongestionTh_Object = MibTableColumn
crmTrPrmLightCongestionTh = _CrmTrPrmLightCongestionTh_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 15),
    _CrmTrPrmLightCongestionTh_Type()
)
crmTrPrmLightCongestionTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmLightCongestionTh.setStatus("mandatory")


class _CrmTrPrmEFCIMarking_Type(Integer32):
    """Custom type crmTrPrmEFCIMarking based on Integer32"""
    defaultValue = 1

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


_CrmTrPrmEFCIMarking_Type.__name__ = "Integer32"
_CrmTrPrmEFCIMarking_Object = MibTableColumn
crmTrPrmEFCIMarking = _CrmTrPrmEFCIMarking_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 16),
    _CrmTrPrmEFCIMarking_Type()
)
crmTrPrmEFCIMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmEFCIMarking.setStatus("mandatory")


class _CrmTrPrmNICIMarking_Type(Integer32):
    """Custom type crmTrPrmNICIMarking based on Integer32"""
    defaultValue = 1

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


_CrmTrPrmNICIMarking_Type.__name__ = "Integer32"
_CrmTrPrmNICIMarking_Object = MibTableColumn
crmTrPrmNICIMarking = _CrmTrPrmNICIMarking_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 17),
    _CrmTrPrmNICIMarking_Type()
)
crmTrPrmNICIMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmNICIMarking.setStatus("mandatory")


class _CrmTrPrmERMarking_Type(Integer32):
    """Custom type crmTrPrmERMarking based on Integer32"""
    defaultValue = 1

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


_CrmTrPrmERMarking_Type.__name__ = "Integer32"
_CrmTrPrmERMarking_Object = MibTableColumn
crmTrPrmERMarking = _CrmTrPrmERMarking_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 18),
    _CrmTrPrmERMarking_Type()
)
crmTrPrmERMarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmERMarking.setStatus("mandatory")


class _CrmTrPrmBECNCellSending_Type(Integer32):
    """Custom type crmTrPrmBECNCellSending based on Integer32"""
    defaultValue = 1

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


_CrmTrPrmBECNCellSending_Type.__name__ = "Integer32"
_CrmTrPrmBECNCellSending_Object = MibTableColumn
crmTrPrmBECNCellSending = _CrmTrPrmBECNCellSending_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 19),
    _CrmTrPrmBECNCellSending_Type()
)
crmTrPrmBECNCellSending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmBECNCellSending.setStatus("mandatory")


class _CrmTrPrmVSVD_Type(Integer32):
    """Custom type crmTrPrmVSVD based on Integer32"""
    defaultValue = 1

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


_CrmTrPrmVSVD_Type.__name__ = "Integer32"
_CrmTrPrmVSVD_Object = MibTableColumn
crmTrPrmVSVD = _CrmTrPrmVSVD_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 20),
    _CrmTrPrmVSVD_Type()
)
crmTrPrmVSVD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmVSVD.setStatus("mandatory")


class _CrmTrPrmRDF_Type(Integer32):
    """Custom type crmTrPrmRDF based on Integer32"""
    defaultValue = 4


_CrmTrPrmRDF_Object = MibTableColumn
crmTrPrmRDF = _CrmTrPrmRDF_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 21),
    _CrmTrPrmRDF_Type()
)
crmTrPrmRDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmRDF.setStatus("mandatory")


class _CrmTrPrmRIF_Type(Integer32):
    """Custom type crmTrPrmRIF based on Integer32"""
    defaultValue = 4


_CrmTrPrmRIF_Object = MibTableColumn
crmTrPrmRIF = _CrmTrPrmRIF_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 22),
    _CrmTrPrmRIF_Type()
)
crmTrPrmRIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmRIF.setStatus("mandatory")


class _CrmTrPrmCDF_Type(Integer32):
    """Custom type crmTrPrmCDF based on Integer32"""
    defaultValue = 4


_CrmTrPrmCDF_Object = MibTableColumn
crmTrPrmCDF = _CrmTrPrmCDF_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 1, 1, 23),
    _CrmTrPrmCDF_Type()
)
crmTrPrmCDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmTrPrmCDF.setStatus("mandatory")
_CrmVplXtndTable_Object = MibTable
crmVplXtndTable = _CrmVplXtndTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    crmVplXtndTable.setStatus("mandatory")
_CrmVplXtndEntry_Object = MibTableRow
crmVplXtndEntry = _CrmVplXtndEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1)
)
crmVplXtndEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVplVpi"),
)
if mibBuilder.loadTexts:
    crmVplXtndEntry.setStatus("mandatory")


class _CrmVplGenCastType_Type(Integer32):
    """Custom type crmVplGenCastType based on Integer32"""
    defaultValue = 1


_CrmVplGenCastType_Object = MibTableColumn
crmVplGenCastType = _CrmVplGenCastType_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 1),
    _CrmVplGenCastType_Type()
)
crmVplGenCastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmVplGenCastType.setStatus("mandatory")


class _CrmVplLogicalPortDef_Type(Integer32):
    """Custom type crmVplLogicalPortDef based on Integer32"""
    defaultValue = 1


_CrmVplLogicalPortDef_Object = MibTableColumn
crmVplLogicalPortDef = _CrmVplLogicalPortDef_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 2),
    _CrmVplLogicalPortDef_Type()
)
crmVplLogicalPortDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmVplLogicalPortDef.setStatus("mandatory")
_CrmVplLogicalPortIndex_Type = InterfaceIndex
_CrmVplLogicalPortIndex_Object = MibTableColumn
crmVplLogicalPortIndex = _CrmVplLogicalPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 3),
    _CrmVplLogicalPortIndex_Type()
)
crmVplLogicalPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crmVplLogicalPortIndex.setStatus("mandatory")


class _CrmVplRowStatus_Type(Integer32):
    """Custom type crmVplRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmVplRowStatus_Type.__name__ = "Integer32"
_CrmVplRowStatus_Object = MibTableColumn
crmVplRowStatus = _CrmVplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 2, 1, 4),
    _CrmVplRowStatus_Type()
)
crmVplRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmVplRowStatus.setStatus("mandatory")
_CrmVclXtndTable_Object = MibTable
crmVclXtndTable = _CrmVclXtndTable_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    crmVclXtndTable.setStatus("mandatory")
_CrmVclXtndEntry_Object = MibTableRow
crmVclXtndEntry = _CrmVclXtndEntry_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1)
)
crmVclXtndEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ATM-MIB", "atmVclVpi"),
    (0, "ATM-MIB", "atmVclVci"),
)
if mibBuilder.loadTexts:
    crmVclXtndEntry.setStatus("mandatory")


class _CrmVclGenConType_Type(Integer32):
    """Custom type crmVclGenConType based on Integer32"""
    defaultValue = 1


_CrmVclGenConType_Object = MibTableColumn
crmVclGenConType = _CrmVclGenConType_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1, 1),
    _CrmVclGenConType_Type()
)
crmVclGenConType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmVclGenConType.setStatus("mandatory")


class _CrmVclGenCastType_Type(Integer32):
    """Custom type crmVclGenCastType based on Integer32"""
    defaultValue = 1


_CrmVclGenCastType_Object = MibTableColumn
crmVclGenCastType = _CrmVclGenCastType_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1, 2),
    _CrmVclGenCastType_Type()
)
crmVclGenCastType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmVclGenCastType.setStatus("mandatory")


class _CrmVclRowStatus_Type(Integer32):
    """Custom type crmVclRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CrmVclRowStatus_Type.__name__ = "Integer32"
_CrmVclRowStatus_Object = MibTableColumn
crmVclRowStatus = _CrmVclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 210, 2, 8, 1, 1, 3, 1, 3),
    _CrmVclRowStatus_Type()
)
crmVclRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    crmVclRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRMCONNECTION-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "ntt": ntt,
       "mibDoc": mibDoc,
       "ba3000": ba3000,
       "crmCommon": crmCommon,
       "crmConnection": crmConnection,
       "crmTrPrmTable": crmTrPrmTable,
       "crmTrPrmEntry": crmTrPrmEntry,
       "crmTrPrmIndex": crmTrPrmIndex,
       "crmTrPrmCategory": crmTrPrmCategory,
       "crmTrPrmCDVT": crmTrPrmCDVT,
       "crmTrPrmCellDelayPriority": crmTrPrmCellDelayPriority,
       "crmTrPrmCellLossPriority": crmTrPrmCellLossPriority,
       "crmTrPrmUPCInfo1": crmTrPrmUPCInfo1,
       "crmTrPrmUPCInfo2": crmTrPrmUPCInfo2,
       "crmTrPrmUPCInfo3": crmTrPrmUPCInfo3,
       "crmTrPrmUPCInfo4": crmTrPrmUPCInfo4,
       "crmTrPrmShapingInfo1": crmTrPrmShapingInfo1,
       "crmTrPrmShapingInfo2": crmTrPrmShapingInfo2,
       "crmTrPrmRowStatus": crmTrPrmRowStatus,
       "crmTrPrmEpdPpd": crmTrPrmEpdPpd,
       "crmTrPrmHeavyCongestionTh": crmTrPrmHeavyCongestionTh,
       "crmTrPrmLightCongestionTh": crmTrPrmLightCongestionTh,
       "crmTrPrmEFCIMarking": crmTrPrmEFCIMarking,
       "crmTrPrmNICIMarking": crmTrPrmNICIMarking,
       "crmTrPrmERMarking": crmTrPrmERMarking,
       "crmTrPrmBECNCellSending": crmTrPrmBECNCellSending,
       "crmTrPrmVSVD": crmTrPrmVSVD,
       "crmTrPrmRDF": crmTrPrmRDF,
       "crmTrPrmRIF": crmTrPrmRIF,
       "crmTrPrmCDF": crmTrPrmCDF,
       "crmVplXtndTable": crmVplXtndTable,
       "crmVplXtndEntry": crmVplXtndEntry,
       "crmVplGenCastType": crmVplGenCastType,
       "crmVplLogicalPortDef": crmVplLogicalPortDef,
       "crmVplLogicalPortIndex": crmVplLogicalPortIndex,
       "crmVplRowStatus": crmVplRowStatus,
       "crmVclXtndTable": crmVclXtndTable,
       "crmVclXtndEntry": crmVclXtndEntry,
       "crmVclGenConType": crmVclGenConType,
       "crmVclGenCastType": crmVclGenCastType,
       "crmVclRowStatus": crmVclRowStatus}
)
