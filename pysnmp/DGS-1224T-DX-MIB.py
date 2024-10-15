# SNMP MIB module (DGS-1224T-DX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DGS-1224T-DX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:27:02 2024
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
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



class RowStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_D_link_ObjectIdentity = ObjectIdentity
d_link = _D_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_DGS12XXTSeriesProd_ObjectIdentity = ObjectIdentity
dlink_DGS12XXTSeriesProd = _Dlink_DGS12XXTSeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76)
)
_Dgs_1224tdx_ObjectIdentity = ObjectIdentity
dgs_1224tdx = _Dgs_1224tdx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5)
)
_CompanyCommGroup_ObjectIdentity = ObjectIdentity
companyCommGroup = _CompanyCommGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1)
)
_CommSetTable_Object = MibTable
commSetTable = _CommSetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 1)
)
if mibBuilder.loadTexts:
    commSetTable.setStatus("mandatory")
_CommSetEntry_Object = MibTableRow
commSetEntry = _CommSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 1, 1)
)
commSetEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "commSetIndex"),
)
if mibBuilder.loadTexts:
    commSetEntry.setStatus("mandatory")


class _CommSetIndex_Type(Integer32):
    """Custom type commSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CommSetIndex_Type.__name__ = "Integer32"
_CommSetIndex_Object = MibTableColumn
commSetIndex = _CommSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 1, 1, 1),
    _CommSetIndex_Type()
)
commSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commSetIndex.setStatus("mandatory")


class _CommSetName_Type(DisplayString):
    """Custom type commSetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CommSetName_Type.__name__ = "DisplayString"
_CommSetName_Object = MibTableColumn
commSetName = _CommSetName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 1, 1, 2),
    _CommSetName_Type()
)
commSetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSetName.setStatus("mandatory")
_CommSetStatus_Type = RowStatus
_CommSetStatus_Object = MibTableColumn
commSetStatus = _CommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 1, 1, 3),
    _CommSetStatus_Type()
)
commSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSetStatus.setStatus("mandatory")
_CommGetTable_Object = MibTable
commGetTable = _CommGetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 2)
)
if mibBuilder.loadTexts:
    commGetTable.setStatus("mandatory")
_CommGetEntry_Object = MibTableRow
commGetEntry = _CommGetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 2, 1)
)
commGetEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "commGetIndex"),
)
if mibBuilder.loadTexts:
    commGetEntry.setStatus("mandatory")


class _CommGetIndex_Type(Integer32):
    """Custom type commGetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CommGetIndex_Type.__name__ = "Integer32"
_CommGetIndex_Object = MibTableColumn
commGetIndex = _CommGetIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 2, 1, 1),
    _CommGetIndex_Type()
)
commGetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commGetIndex.setStatus("mandatory")


class _CommGetName_Type(DisplayString):
    """Custom type commGetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CommGetName_Type.__name__ = "DisplayString"
_CommGetName_Object = MibTableColumn
commGetName = _CommGetName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 2, 1, 2),
    _CommGetName_Type()
)
commGetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commGetName.setStatus("mandatory")
_CommGetStatus_Type = RowStatus
_CommGetStatus_Object = MibTableColumn
commGetStatus = _CommGetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 2, 1, 3),
    _CommGetStatus_Type()
)
commGetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commGetStatus.setStatus("mandatory")
_CommTrapTable_Object = MibTable
commTrapTable = _CommTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3)
)
if mibBuilder.loadTexts:
    commTrapTable.setStatus("mandatory")
_CommTrapEntry_Object = MibTableRow
commTrapEntry = _CommTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1)
)
commTrapEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "commTrapIndex"),
)
if mibBuilder.loadTexts:
    commTrapEntry.setStatus("mandatory")


class _CommTrapIndex_Type(Integer32):
    """Custom type commTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CommTrapIndex_Type.__name__ = "Integer32"
_CommTrapIndex_Object = MibTableColumn
commTrapIndex = _CommTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 1),
    _CommTrapIndex_Type()
)
commTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commTrapIndex.setStatus("mandatory")


class _CommTrapName_Type(DisplayString):
    """Custom type commTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CommTrapName_Type.__name__ = "DisplayString"
_CommTrapName_Object = MibTableColumn
commTrapName = _CommTrapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 2),
    _CommTrapName_Type()
)
commTrapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapName.setStatus("mandatory")
_CommTrapIpAddress_Type = IpAddress
_CommTrapIpAddress_Object = MibTableColumn
commTrapIpAddress = _CommTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 3),
    _CommTrapIpAddress_Type()
)
commTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapIpAddress.setStatus("mandatory")


class _CommTrapSNMPBootup_Type(Integer32):
    """Custom type commTrapSNMPBootup based on Integer32"""
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


_CommTrapSNMPBootup_Type.__name__ = "Integer32"
_CommTrapSNMPBootup_Object = MibTableColumn
commTrapSNMPBootup = _CommTrapSNMPBootup_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 5),
    _CommTrapSNMPBootup_Type()
)
commTrapSNMPBootup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapSNMPBootup.setStatus("mandatory")


class _CommTrapSNMPTPLinkUpDown_Type(Integer32):
    """Custom type commTrapSNMPTPLinkUpDown based on Integer32"""
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


_CommTrapSNMPTPLinkUpDown_Type.__name__ = "Integer32"
_CommTrapSNMPTPLinkUpDown_Object = MibTableColumn
commTrapSNMPTPLinkUpDown = _CommTrapSNMPTPLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 6),
    _CommTrapSNMPTPLinkUpDown_Type()
)
commTrapSNMPTPLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapSNMPTPLinkUpDown.setStatus("mandatory")


class _CommTrapSNMPFiberLinkUpDown_Type(Integer32):
    """Custom type commTrapSNMPFiberLinkUpDown based on Integer32"""
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


_CommTrapSNMPFiberLinkUpDown_Type.__name__ = "Integer32"
_CommTrapSNMPFiberLinkUpDown_Object = MibTableColumn
commTrapSNMPFiberLinkUpDown = _CommTrapSNMPFiberLinkUpDown_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 7),
    _CommTrapSNMPFiberLinkUpDown_Type()
)
commTrapSNMPFiberLinkUpDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapSNMPFiberLinkUpDown.setStatus("mandatory")


class _CommTrapTrapAbnormalTPRXError_Type(Integer32):
    """Custom type commTrapTrapAbnormalTPRXError based on Integer32"""
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


_CommTrapTrapAbnormalTPRXError_Type.__name__ = "Integer32"
_CommTrapTrapAbnormalTPRXError_Object = MibTableColumn
commTrapTrapAbnormalTPRXError = _CommTrapTrapAbnormalTPRXError_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 9),
    _CommTrapTrapAbnormalTPRXError_Type()
)
commTrapTrapAbnormalTPRXError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapAbnormalTPRXError.setStatus("mandatory")


class _CommTrapTrapAbnormalTPTXError_Type(Integer32):
    """Custom type commTrapTrapAbnormalTPTXError based on Integer32"""
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


_CommTrapTrapAbnormalTPTXError_Type.__name__ = "Integer32"
_CommTrapTrapAbnormalTPTXError_Object = MibTableColumn
commTrapTrapAbnormalTPTXError = _CommTrapTrapAbnormalTPTXError_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 10),
    _CommTrapTrapAbnormalTPTXError_Type()
)
commTrapTrapAbnormalTPTXError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapAbnormalTPTXError.setStatus("mandatory")


class _CommTrapTrapAbnormalFiberRXError_Type(Integer32):
    """Custom type commTrapTrapAbnormalFiberRXError based on Integer32"""
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


_CommTrapTrapAbnormalFiberRXError_Type.__name__ = "Integer32"
_CommTrapTrapAbnormalFiberRXError_Object = MibTableColumn
commTrapTrapAbnormalFiberRXError = _CommTrapTrapAbnormalFiberRXError_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 11),
    _CommTrapTrapAbnormalFiberRXError_Type()
)
commTrapTrapAbnormalFiberRXError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapAbnormalFiberRXError.setStatus("mandatory")


class _CommTrapTrapAbnormalFiberTXError_Type(Integer32):
    """Custom type commTrapTrapAbnormalFiberTXError based on Integer32"""
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


_CommTrapTrapAbnormalFiberTXError_Type.__name__ = "Integer32"
_CommTrapTrapAbnormalFiberTXError_Object = MibTableColumn
commTrapTrapAbnormalFiberTXError = _CommTrapTrapAbnormalFiberTXError_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 12),
    _CommTrapTrapAbnormalFiberTXError_Type()
)
commTrapTrapAbnormalFiberTXError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapAbnormalFiberTXError.setStatus("mandatory")
_CommTrapStatus_Type = RowStatus
_CommTrapStatus_Object = MibTableColumn
commTrapStatus = _CommTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 1, 3, 1, 13),
    _CommTrapStatus_Type()
)
commTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapStatus.setStatus("mandatory")
_CompanyMiscGroup_ObjectIdentity = ObjectIdentity
companyMiscGroup = _CompanyMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 3)
)


class _MiscReset_Type(Integer32):
    """Custom type miscReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("reset", 1))
    )


_MiscReset_Type.__name__ = "Integer32"
_MiscReset_Object = MibScalar
miscReset = _MiscReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 3, 2),
    _MiscReset_Type()
)
miscReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscReset.setStatus("mandatory")


class _MiscStatisticsReset_Type(Integer32):
    """Custom type miscStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("reset", 1))
    )


_MiscStatisticsReset_Type.__name__ = "Integer32"
_MiscStatisticsReset_Object = MibScalar
miscStatisticsReset = _MiscStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 3, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("mandatory")
_CompanySpanGroup_ObjectIdentity = ObjectIdentity
companySpanGroup = _CompanySpanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 4)
)


class _SpanOnOff_Type(Integer32):
    """Custom type spanOnOff based on Integer32"""
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


_SpanOnOff_Type.__name__ = "Integer32"
_SpanOnOff_Object = MibScalar
spanOnOff = _SpanOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 4, 1),
    _SpanOnOff_Type()
)
spanOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanOnOff.setStatus("mandatory")
_CompanyConfigGroup_ObjectIdentity = ObjectIdentity
companyConfigGroup = _CompanyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11)
)


class _ConfigVerSwPrimary_Type(DisplayString):
    """Custom type configVerSwPrimary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ConfigVerSwPrimary_Type.__name__ = "DisplayString"
_ConfigVerSwPrimary_Object = MibScalar
configVerSwPrimary = _ConfigVerSwPrimary_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 1),
    _ConfigVerSwPrimary_Type()
)
configVerSwPrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVerSwPrimary.setStatus("mandatory")


class _ConfigVerHwChipSet_Type(DisplayString):
    """Custom type configVerHwChipSet based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_ConfigVerHwChipSet_Type.__name__ = "DisplayString"
_ConfigVerHwChipSet_Object = MibScalar
configVerHwChipSet = _ConfigVerHwChipSet_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 2),
    _ConfigVerHwChipSet_Type()
)
configVerHwChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVerHwChipSet.setStatus("mandatory")


class _ConfigBootTftpOperation_Type(Integer32):
    """Custom type configBootTftpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_ConfigBootTftpOperation_Type.__name__ = "Integer32"
_ConfigBootTftpOperation_Object = MibScalar
configBootTftpOperation = _ConfigBootTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 3),
    _ConfigBootTftpOperation_Type()
)
configBootTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBootTftpOperation.setStatus("mandatory")
_ConfigBootTftpServerIp_Type = IpAddress
_ConfigBootTftpServerIp_Object = MibScalar
configBootTftpServerIp = _ConfigBootTftpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 4),
    _ConfigBootTftpServerIp_Type()
)
configBootTftpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBootTftpServerIp.setStatus("mandatory")


class _ConfigBootImageFileName_Type(DisplayString):
    """Custom type configBootImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_ConfigBootImageFileName_Type.__name__ = "DisplayString"
_ConfigBootImageFileName_Object = MibScalar
configBootImageFileName = _ConfigBootImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 5),
    _ConfigBootImageFileName_Type()
)
configBootImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBootImageFileName.setStatus("mandatory")
_ConfigPortTable_Object = MibTable
configPortTable = _ConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 6)
)
if mibBuilder.loadTexts:
    configPortTable.setStatus("mandatory")
_ConfigPortEntry_Object = MibTableRow
configPortEntry = _ConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 6, 1)
)
configPortEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "configPort"),
)
if mibBuilder.loadTexts:
    configPortEntry.setStatus("mandatory")
_ConfigPort_Type = Integer32
_ConfigPort_Object = MibTableColumn
configPort = _ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 6, 1, 1),
    _ConfigPort_Type()
)
configPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPort.setStatus("mandatory")


class _ConfigPortSpeed_Type(Integer32):
    """Custom type configPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("disable", 1),
          ("rate1000M-Full", 7),
          ("rate100M-Full", 6),
          ("rate100M-Half", 5),
          ("rate10M-Full", 4),
          ("rate10M-Half", 3))
    )


_ConfigPortSpeed_Type.__name__ = "Integer32"
_ConfigPortSpeed_Object = MibTableColumn
configPortSpeed = _ConfigPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 6, 1, 2),
    _ConfigPortSpeed_Type()
)
configPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortSpeed.setStatus("mandatory")


class _ConfigPortOperStatus_Type(Integer32):
    """Custom type configPortOperStatus based on Integer32"""
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
        *(("down", 1),
          ("rate1000M-Full", 6),
          ("rate100M-Full", 5),
          ("rate100M-Half", 4),
          ("rate10M-Full", 3),
          ("rate10M-Half", 2))
    )


_ConfigPortOperStatus_Type.__name__ = "Integer32"
_ConfigPortOperStatus_Object = MibTableColumn
configPortOperStatus = _ConfigPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 6, 1, 3),
    _ConfigPortOperStatus_Type()
)
configPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortOperStatus.setStatus("mandatory")


class _ConfigPortFlowControl_Type(Integer32):
    """Custom type configPortFlowControl based on Integer32"""
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


_ConfigPortFlowControl_Type.__name__ = "Integer32"
_ConfigPortFlowControl_Object = MibTableColumn
configPortFlowControl = _ConfigPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 6, 1, 4),
    _ConfigPortFlowControl_Type()
)
configPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortFlowControl.setStatus("mandatory")


class _ConfigPortFlowControlOper_Type(Integer32):
    """Custom type configPortFlowControlOper based on Integer32"""
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


_ConfigPortFlowControlOper_Type.__name__ = "Integer32"
_ConfigPortFlowControlOper_Object = MibTableColumn
configPortFlowControlOper = _ConfigPortFlowControlOper_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 6, 1, 5),
    _ConfigPortFlowControlOper_Type()
)
configPortFlowControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortFlowControlOper.setStatus("mandatory")


class _ConfigVLANMode_Type(Integer32):
    """Custom type configVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("modeTagBased", 1)
    )


_ConfigVLANMode_Type.__name__ = "Integer32"
_ConfigVLANMode_Object = MibScalar
configVLANMode = _ConfigVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 7),
    _ConfigVLANMode_Type()
)
configVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVLANMode.setStatus("mandatory")
_ConfigMirrorTable_Object = MibTable
configMirrorTable = _ConfigMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 8)
)
if mibBuilder.loadTexts:
    configMirrorTable.setStatus("mandatory")
_ConfigMirrorEntry_Object = MibTableRow
configMirrorEntry = _ConfigMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 8, 1)
)
configMirrorEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "configMirrorId"),
)
if mibBuilder.loadTexts:
    configMirrorEntry.setStatus("mandatory")


class _ConfigMirrorId_Type(Integer32):
    """Custom type configMirrorId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_ConfigMirrorId_Type.__name__ = "Integer32"
_ConfigMirrorId_Object = MibTableColumn
configMirrorId = _ConfigMirrorId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 8, 1, 1),
    _ConfigMirrorId_Type()
)
configMirrorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configMirrorId.setStatus("mandatory")
_ConfigMirrorMon_Type = Integer32
_ConfigMirrorMon_Object = MibTableColumn
configMirrorMon = _ConfigMirrorMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 8, 1, 2),
    _ConfigMirrorMon_Type()
)
configMirrorMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorMon.setStatus("mandatory")
_ConfigMirrorTXSrc_Type = PortList
_ConfigMirrorTXSrc_Object = MibTableColumn
configMirrorTXSrc = _ConfigMirrorTXSrc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 8, 1, 3),
    _ConfigMirrorTXSrc_Type()
)
configMirrorTXSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorTXSrc.setStatus("mandatory")
_ConfigMirrorRXSrc_Type = PortList
_ConfigMirrorRXSrc_Object = MibTableColumn
configMirrorRXSrc = _ConfigMirrorRXSrc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 8, 1, 4),
    _ConfigMirrorRXSrc_Type()
)
configMirrorRXSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorRXSrc.setStatus("mandatory")
_ConfigMirrorStatus_Type = RowStatus
_ConfigMirrorStatus_Object = MibTableColumn
configMirrorStatus = _ConfigMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 8, 1, 5),
    _ConfigMirrorStatus_Type()
)
configMirrorStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorStatus.setStatus("mandatory")


class _ConfigSNMPEnable_Type(Integer32):
    """Custom type configSNMPEnable based on Integer32"""
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


_ConfigSNMPEnable_Type.__name__ = "Integer32"
_ConfigSNMPEnable_Object = MibScalar
configSNMPEnable = _ConfigSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 9),
    _ConfigSNMPEnable_Type()
)
configSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSNMPEnable.setStatus("mandatory")


class _ConfigIpAssignmentMode_Type(Integer32):
    """Custom type configIpAssignmentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("manual", 1),
          ("other", 3))
    )


_ConfigIpAssignmentMode_Type.__name__ = "Integer32"
_ConfigIpAssignmentMode_Object = MibScalar
configIpAssignmentMode = _ConfigIpAssignmentMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 12),
    _ConfigIpAssignmentMode_Type()
)
configIpAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpAssignmentMode.setStatus("mandatory")
_ConfigPhysAddress_Type = MacAddress
_ConfigPhysAddress_Object = MibScalar
configPhysAddress = _ConfigPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 13),
    _ConfigPhysAddress_Type()
)
configPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPhysAddress.setStatus("mandatory")


class _ConfigPasswordAdmin_Type(DisplayString):
    """Custom type configPasswordAdmin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ConfigPasswordAdmin_Type.__name__ = "DisplayString"
_ConfigPasswordAdmin_Object = MibScalar
configPasswordAdmin = _ConfigPasswordAdmin_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 15),
    _ConfigPasswordAdmin_Type()
)
configPasswordAdmin.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    configPasswordAdmin.setStatus("mandatory")
_ConfigIpAddress_Type = IpAddress
_ConfigIpAddress_Object = MibScalar
configIpAddress = _ConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 16),
    _ConfigIpAddress_Type()
)
configIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpAddress.setStatus("mandatory")
_ConfigNetMask_Type = IpAddress
_ConfigNetMask_Object = MibScalar
configNetMask = _ConfigNetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 17),
    _ConfigNetMask_Type()
)
configNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNetMask.setStatus("mandatory")
_ConfigGateway_Type = IpAddress
_ConfigGateway_Object = MibScalar
configGateway = _ConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 18),
    _ConfigGateway_Type()
)
configGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configGateway.setStatus("mandatory")


class _ConfigSave_Type(Integer32):
    """Custom type configSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("save", 1))
    )


_ConfigSave_Type.__name__ = "Integer32"
_ConfigSave_Object = MibScalar
configSave = _ConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 19),
    _ConfigSave_Type()
)
configSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSave.setStatus("mandatory")


class _ConfigRestoreDefaults_Type(Integer32):
    """Custom type configRestoreDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 2),
          ("restore", 1))
    )


_ConfigRestoreDefaults_Type.__name__ = "Integer32"
_ConfigRestoreDefaults_Object = MibScalar
configRestoreDefaults = _ConfigRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 22),
    _ConfigRestoreDefaults_Type()
)
configRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRestoreDefaults.setStatus("mandatory")
_ConfigTftpServerIpAddress_Type = IpAddress
_ConfigTftpServerIpAddress_Object = MibScalar
configTftpServerIpAddress = _ConfigTftpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 32),
    _ConfigTftpServerIpAddress_Type()
)
configTftpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTftpServerIpAddress.setStatus("mandatory")


class _ConfigTftpServerFileName_Type(DisplayString):
    """Custom type configTftpServerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ConfigTftpServerFileName_Type.__name__ = "DisplayString"
_ConfigTftpServerFileName_Object = MibScalar
configTftpServerFileName = _ConfigTftpServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 33),
    _ConfigTftpServerFileName_Type()
)
configTftpServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTftpServerFileName.setStatus("mandatory")


class _ConfigTftpOperation_Type(Integer32):
    """Custom type configTftpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_ConfigTftpOperation_Type.__name__ = "Integer32"
_ConfigTftpOperation_Object = MibScalar
configTftpOperation = _ConfigTftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 34),
    _ConfigTftpOperation_Type()
)
configTftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTftpOperation.setStatus("mandatory")


class _ConfigJumboEnable_Type(Integer32):
    """Custom type configJumboEnable based on Integer32"""
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


_ConfigJumboEnable_Type.__name__ = "Integer32"
_ConfigJumboEnable_Object = MibScalar
configJumboEnable = _ConfigJumboEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 43),
    _ConfigJumboEnable_Type()
)
configJumboEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configJumboEnable.setStatus("mandatory")


class _ConfigSafeguardEnable_Type(Integer32):
    """Custom type configSafeguardEnable based on Integer32"""
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


_ConfigSafeguardEnable_Type.__name__ = "Integer32"
_ConfigSafeguardEnable_Object = MibScalar
configSafeguardEnable = _ConfigSafeguardEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 44),
    _ConfigSafeguardEnable_Type()
)
configSafeguardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSafeguardEnable.setStatus("mandatory")


class _ConfigPowerSavingEnable_Type(Integer32):
    """Custom type configPowerSavingEnable based on Integer32"""
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


_ConfigPowerSavingEnable_Type.__name__ = "Integer32"
_ConfigPowerSavingEnable_Object = MibScalar
configPowerSavingEnable = _ConfigPowerSavingEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 11, 45),
    _ConfigPowerSavingEnable_Type()
)
configPowerSavingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPowerSavingEnable.setStatus("mandatory")
_CompanyTVlanGroup_ObjectIdentity = ObjectIdentity
companyTVlanGroup = _CompanyTVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13)
)
_TvlanTable_Object = MibTable
tvlanTable = _TvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 1)
)
if mibBuilder.loadTexts:
    tvlanTable.setStatus("mandatory")
_TvlanEntry_Object = MibTableRow
tvlanEntry = _TvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 1, 1)
)
tvlanEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "tvlanId"),
)
if mibBuilder.loadTexts:
    tvlanEntry.setStatus("mandatory")
_TvlanId_Type = Integer32
_TvlanId_Object = MibTableColumn
tvlanId = _TvlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 1, 1, 1),
    _TvlanId_Type()
)
tvlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvlanId.setStatus("mandatory")
_TvlanName_Type = DisplayString
_TvlanName_Object = MibTableColumn
tvlanName = _TvlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 1, 1, 2),
    _TvlanName_Type()
)
tvlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanName.setStatus("mandatory")
_TvlanMember_Type = PortList
_TvlanMember_Object = MibTableColumn
tvlanMember = _TvlanMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 1, 1, 3),
    _TvlanMember_Type()
)
tvlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanMember.setStatus("mandatory")
_TvlanUntaggedPorts_Type = PortList
_TvlanUntaggedPorts_Object = MibTableColumn
tvlanUntaggedPorts = _TvlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 1, 1, 4),
    _TvlanUntaggedPorts_Type()
)
tvlanUntaggedPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanUntaggedPorts.setStatus("mandatory")


class _TvlanStatus_Type(Integer32):
    """Custom type tvlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndwait", 5),
          ("destroy", 6),
          ("notready", 3))
    )


_TvlanStatus_Type.__name__ = "Integer32"
_TvlanStatus_Object = MibTableColumn
tvlanStatus = _TvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 1, 1, 5),
    _TvlanStatus_Type()
)
tvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanStatus.setStatus("mandatory")


class _TvlanManagementOnOff_Type(Integer32):
    """Custom type tvlanManagementOnOff based on Integer32"""
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


_TvlanManagementOnOff_Type.__name__ = "Integer32"
_TvlanManagementOnOff_Object = MibScalar
tvlanManagementOnOff = _TvlanManagementOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 2),
    _TvlanManagementOnOff_Type()
)
tvlanManagementOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanManagementOnOff.setStatus("mandatory")
_TvlanManagementid_Type = Integer32
_TvlanManagementid_Object = MibScalar
tvlanManagementid = _TvlanManagementid_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 3),
    _TvlanManagementid_Type()
)
tvlanManagementid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanManagementid.setStatus("mandatory")
_TvlanPortTable_Object = MibTable
tvlanPortTable = _TvlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 4)
)
if mibBuilder.loadTexts:
    tvlanPortTable.setStatus("mandatory")
_TvlanPortEntry_Object = MibTableRow
tvlanPortEntry = _TvlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 4, 1)
)
tvlanPortEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "tvlanPortPortId"),
)
if mibBuilder.loadTexts:
    tvlanPortEntry.setStatus("mandatory")
_TvlanPortPortId_Type = Integer32
_TvlanPortPortId_Object = MibTableColumn
tvlanPortPortId = _TvlanPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 4, 1, 1),
    _TvlanPortPortId_Type()
)
tvlanPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvlanPortPortId.setStatus("mandatory")
_TvlanPortVlanId_Type = Integer32
_TvlanPortVlanId_Object = MibTableColumn
tvlanPortVlanId = _TvlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 4, 1, 2),
    _TvlanPortVlanId_Type()
)
tvlanPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanPortVlanId.setStatus("mandatory")


class _TvlanAsyOnOff_Type(Integer32):
    """Custom type tvlanAsyOnOff based on Integer32"""
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


_TvlanAsyOnOff_Type.__name__ = "Integer32"
_TvlanAsyOnOff_Object = MibScalar
tvlanAsyOnOff = _TvlanAsyOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 13, 5),
    _TvlanAsyOnOff_Type()
)
tvlanAsyOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanAsyOnOff.setStatus("mandatory")
_CompanyPortTrunkGroup_ObjectIdentity = ObjectIdentity
companyPortTrunkGroup = _CompanyPortTrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 14)
)
_PortTrunkTable_Object = MibTable
portTrunkTable = _PortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 14, 1)
)
if mibBuilder.loadTexts:
    portTrunkTable.setStatus("mandatory")
_PortTrunkEntry_Object = MibTableRow
portTrunkEntry = _PortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 14, 1, 1)
)
portTrunkEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "portTrunkId"),
    (0, "DGS-1224T-DX-MIB", "portTrunkMember"),
)
if mibBuilder.loadTexts:
    portTrunkEntry.setStatus("mandatory")
_PortTrunkId_Type = Integer32
_PortTrunkId_Object = MibTableColumn
portTrunkId = _PortTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 14, 1, 1, 1),
    _PortTrunkId_Type()
)
portTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkId.setStatus("mandatory")
_PortTrunkName_Type = DisplayString
_PortTrunkName_Object = MibTableColumn
portTrunkName = _PortTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 14, 1, 1, 2),
    _PortTrunkName_Type()
)
portTrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkName.setStatus("mandatory")
_PortTrunkMember_Type = PortList
_PortTrunkMember_Object = MibTableColumn
portTrunkMember = _PortTrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 14, 1, 1, 3),
    _PortTrunkMember_Type()
)
portTrunkMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkMember.setStatus("mandatory")
_CompanyStaticGroup_ObjectIdentity = ObjectIdentity
companyStaticGroup = _CompanyStaticGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21)
)


class _StaticOnOff_Type(Integer32):
    """Custom type staticOnOff based on Integer32"""
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


_StaticOnOff_Type.__name__ = "Integer32"
_StaticOnOff_Object = MibScalar
staticOnOff = _StaticOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 1),
    _StaticOnOff_Type()
)
staticOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticOnOff.setStatus("mandatory")
_StaticAutoLearning_Type = PortList
_StaticAutoLearning_Object = MibScalar
staticAutoLearning = _StaticAutoLearning_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 2),
    _StaticAutoLearning_Type()
)
staticAutoLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticAutoLearning.setStatus("mandatory")
_StaticTable_Object = MibTable
staticTable = _StaticTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 3)
)
if mibBuilder.loadTexts:
    staticTable.setStatus("mandatory")
_StaticEntry_Object = MibTableRow
staticEntry = _StaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 3, 1)
)
staticEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "staticId"),
)
if mibBuilder.loadTexts:
    staticEntry.setStatus("mandatory")
_StaticId_Type = Integer32
_StaticId_Object = MibTableColumn
staticId = _StaticId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 3, 1, 1),
    _StaticId_Type()
)
staticId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staticId.setStatus("mandatory")
_StaticMac_Type = MacAddress
_StaticMac_Object = MibTableColumn
staticMac = _StaticMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 3, 1, 2),
    _StaticMac_Type()
)
staticMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMac.setStatus("mandatory")
_StaticPort_Type = Integer32
_StaticPort_Object = MibTableColumn
staticPort = _StaticPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 3, 1, 3),
    _StaticPort_Type()
)
staticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticPort.setStatus("mandatory")
_StaticVlanID_Type = Integer32
_StaticVlanID_Object = MibTableColumn
staticVlanID = _StaticVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 3, 1, 4),
    _StaticVlanID_Type()
)
staticVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticVlanID.setStatus("mandatory")


class _StaticStatus_Type(Integer32):
    """Custom type staticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndwait", 5),
          ("destroy", 6),
          ("notready", 3))
    )


_StaticStatus_Type.__name__ = "Integer32"
_StaticStatus_Object = MibTableColumn
staticStatus = _StaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 21, 3, 1, 5),
    _StaticStatus_Type()
)
staticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticStatus.setStatus("mandatory")
_CompanyIgsGroup_ObjectIdentity = ObjectIdentity
companyIgsGroup = _CompanyIgsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22)
)
_IgsSystem_ObjectIdentity = ObjectIdentity
igsSystem = _IgsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1)
)


class _IgsStatus_Type(Integer32):
    """Custom type igsStatus based on Integer32"""
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


_IgsStatus_Type.__name__ = "Integer32"
_IgsStatus_Object = MibScalar
igsStatus = _IgsStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 2),
    _IgsStatus_Type()
)
igsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsStatus.setStatus("mandatory")


class _Igsv3Processing_Type(Integer32):
    """Custom type igsv3Processing based on Integer32"""
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


_Igsv3Processing_Type.__name__ = "Integer32"
_Igsv3Processing_Object = MibScalar
igsv3Processing = _Igsv3Processing_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 3),
    _Igsv3Processing_Type()
)
igsv3Processing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsv3Processing.setStatus("mandatory")


class _IgsRouterPortPurgeInterval_Type(Integer32):
    """Custom type igsRouterPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_IgsRouterPortPurgeInterval_Type.__name__ = "Integer32"
_IgsRouterPortPurgeInterval_Object = MibScalar
igsRouterPortPurgeInterval = _IgsRouterPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 4),
    _IgsRouterPortPurgeInterval_Type()
)
igsRouterPortPurgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsRouterPortPurgeInterval.setStatus("mandatory")


class _IgsHostPortPurgeInterval_Type(Integer32):
    """Custom type igsHostPortPurgeInterval based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 153025),
    )


_IgsHostPortPurgeInterval_Type.__name__ = "Integer32"
_IgsHostPortPurgeInterval_Object = MibScalar
igsHostPortPurgeInterval = _IgsHostPortPurgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 5),
    _IgsHostPortPurgeInterval_Type()
)
igsHostPortPurgeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsHostPortPurgeInterval.setStatus("mandatory")


class _IgsReportForwardInterval_Type(Integer32):
    """Custom type igsReportForwardInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_IgsReportForwardInterval_Type.__name__ = "Integer32"
_IgsReportForwardInterval_Object = MibScalar
igsReportForwardInterval = _IgsReportForwardInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 6),
    _IgsReportForwardInterval_Type()
)
igsReportForwardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsReportForwardInterval.setStatus("mandatory")


class _IgsLeaveProcessInterval_Type(Integer32):
    """Custom type igsLeaveProcessInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 25),
    )


_IgsLeaveProcessInterval_Type.__name__ = "Integer32"
_IgsLeaveProcessInterval_Object = MibScalar
igsLeaveProcessInterval = _IgsLeaveProcessInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 7),
    _IgsLeaveProcessInterval_Type()
)
igsLeaveProcessInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsLeaveProcessInterval.setStatus("mandatory")


class _IgsMcastEntryAgeingInterval_Type(Integer32):
    """Custom type igsMcastEntryAgeingInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_IgsMcastEntryAgeingInterval_Type.__name__ = "Integer32"
_IgsMcastEntryAgeingInterval_Object = MibScalar
igsMcastEntryAgeingInterval = _IgsMcastEntryAgeingInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 8),
    _IgsMcastEntryAgeingInterval_Type()
)
igsMcastEntryAgeingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsMcastEntryAgeingInterval.setStatus("mandatory")


class _IgsSharedSegmentAggregationInterval_Type(Integer32):
    """Custom type igsSharedSegmentAggregationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IgsSharedSegmentAggregationInterval_Type.__name__ = "Integer32"
_IgsSharedSegmentAggregationInterval_Object = MibScalar
igsSharedSegmentAggregationInterval = _IgsSharedSegmentAggregationInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 9),
    _IgsSharedSegmentAggregationInterval_Type()
)
igsSharedSegmentAggregationInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsSharedSegmentAggregationInterval.setStatus("mandatory")


class _IgsGblReportFwdOnAllPorts_Type(Integer32):
    """Custom type igsGblReportFwdOnAllPorts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allports", 1),
          ("rtrports", 2))
    )


_IgsGblReportFwdOnAllPorts_Type.__name__ = "Integer32"
_IgsGblReportFwdOnAllPorts_Object = MibScalar
igsGblReportFwdOnAllPorts = _IgsGblReportFwdOnAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 10),
    _IgsGblReportFwdOnAllPorts_Type()
)
igsGblReportFwdOnAllPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsGblReportFwdOnAllPorts.setStatus("mandatory")


class _IgsNextMcastFwdMode_Type(Integer32):
    """Custom type igsNextMcastFwdMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipbased", 1),
          ("macbased", 2))
    )


_IgsNextMcastFwdMode_Type.__name__ = "Integer32"
_IgsNextMcastFwdMode_Object = MibScalar
igsNextMcastFwdMode = _IgsNextMcastFwdMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 13),
    _IgsNextMcastFwdMode_Type()
)
igsNextMcastFwdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsNextMcastFwdMode.setStatus("mandatory")


class _IgsQueryInterval_Type(Integer32):
    """Custom type igsQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 600),
    )


_IgsQueryInterval_Type.__name__ = "Integer32"
_IgsQueryInterval_Object = MibScalar
igsQueryInterval = _IgsQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 14),
    _IgsQueryInterval_Type()
)
igsQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsQueryInterval.setStatus("mandatory")


class _IgsQueryMaxResponseTime_Type(Integer32):
    """Custom type igsQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 25),
    )


_IgsQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgsQueryMaxResponseTime_Object = MibScalar
igsQueryMaxResponseTime = _IgsQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 15),
    _IgsQueryMaxResponseTime_Type()
)
igsQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsQueryMaxResponseTime.setStatus("mandatory")


class _IgsRobustnessValue_Type(Integer32):
    """Custom type igsRobustnessValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 255),
    )


_IgsRobustnessValue_Type.__name__ = "Integer32"
_IgsRobustnessValue_Object = MibScalar
igsRobustnessValue = _IgsRobustnessValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 16),
    _IgsRobustnessValue_Type()
)
igsRobustnessValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsRobustnessValue.setStatus("mandatory")


class _IgsLastMembQueryInterval_Type(Integer32):
    """Custom type igsLastMembQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_IgsLastMembQueryInterval_Type.__name__ = "Integer32"
_IgsLastMembQueryInterval_Object = MibScalar
igsLastMembQueryInterval = _IgsLastMembQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 17),
    _IgsLastMembQueryInterval_Type()
)
igsLastMembQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsLastMembQueryInterval.setStatus("mandatory")


class _IgsQuerierStateOnOff_Type(Integer32):
    """Custom type igsQuerierStateOnOff based on Integer32"""
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


_IgsQuerierStateOnOff_Type.__name__ = "Integer32"
_IgsQuerierStateOnOff_Object = MibScalar
igsQuerierStateOnOff = _IgsQuerierStateOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 1, 18),
    _IgsQuerierStateOnOff_Type()
)
igsQuerierStateOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsQuerierStateOnOff.setStatus("mandatory")
_IgsVlan_ObjectIdentity = ObjectIdentity
igsVlan = _IgsVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3)
)
_IgsVlanMcastFwdTable_Object = MibTable
igsVlanMcastFwdTable = _IgsVlanMcastFwdTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 1)
)
if mibBuilder.loadTexts:
    igsVlanMcastFwdTable.setStatus("mandatory")
_IgsVlanMcastFwdEntry_Object = MibTableRow
igsVlanMcastFwdEntry = _IgsVlanMcastFwdEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 1, 1)
)
igsVlanMcastFwdEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "igsVlanMcastFwdVlanIdMac"),
    (0, "DGS-1224T-DX-MIB", "igsVlanMcastFwdGroupAddress"),
)
if mibBuilder.loadTexts:
    igsVlanMcastFwdEntry.setStatus("mandatory")


class _IgsVlanMcastFwdVlanIdMac_Type(Integer32):
    """Custom type igsVlanMcastFwdVlanIdMac based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanMcastFwdVlanIdMac_Type.__name__ = "Integer32"
_IgsVlanMcastFwdVlanIdMac_Object = MibTableColumn
igsVlanMcastFwdVlanIdMac = _IgsVlanMcastFwdVlanIdMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 1, 1, 1),
    _IgsVlanMcastFwdVlanIdMac_Type()
)
igsVlanMcastFwdVlanIdMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igsVlanMcastFwdVlanIdMac.setStatus("mandatory")
_IgsVlanMcastFwdGroupAddress_Type = MacAddress
_IgsVlanMcastFwdGroupAddress_Object = MibTableColumn
igsVlanMcastFwdGroupAddress = _IgsVlanMcastFwdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 1, 1, 2),
    _IgsVlanMcastFwdGroupAddress_Type()
)
igsVlanMcastFwdGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igsVlanMcastFwdGroupAddress.setStatus("mandatory")
_IgsVlanMcastFwdPortListMac_Type = PortList
_IgsVlanMcastFwdPortListMac_Object = MibTableColumn
igsVlanMcastFwdPortListMac = _IgsVlanMcastFwdPortListMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 1, 1, 3),
    _IgsVlanMcastFwdPortListMac_Type()
)
igsVlanMcastFwdPortListMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanMcastFwdPortListMac.setStatus("mandatory")
_IgsVlanRouterPortListTable_Object = MibTable
igsVlanRouterPortListTable = _IgsVlanRouterPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 3)
)
if mibBuilder.loadTexts:
    igsVlanRouterPortListTable.setStatus("mandatory")
_IgsVlanRouterPortListEntry_Object = MibTableRow
igsVlanRouterPortListEntry = _IgsVlanRouterPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 3, 1)
)
igsVlanRouterPortListEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "igsVlanRouterPortListVlanId"),
)
if mibBuilder.loadTexts:
    igsVlanRouterPortListEntry.setStatus("mandatory")


class _IgsVlanRouterPortListVlanId_Type(Integer32):
    """Custom type igsVlanRouterPortListVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanRouterPortListVlanId_Type.__name__ = "Integer32"
_IgsVlanRouterPortListVlanId_Object = MibTableColumn
igsVlanRouterPortListVlanId = _IgsVlanRouterPortListVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 3, 1, 1),
    _IgsVlanRouterPortListVlanId_Type()
)
igsVlanRouterPortListVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igsVlanRouterPortListVlanId.setStatus("mandatory")
_IgsVlanRouterPortList_Type = PortList
_IgsVlanRouterPortList_Object = MibTableColumn
igsVlanRouterPortList = _IgsVlanRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 3, 1, 2),
    _IgsVlanRouterPortList_Type()
)
igsVlanRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igsVlanRouterPortList.setStatus("mandatory")
_IgsVlanFilterTable_Object = MibTable
igsVlanFilterTable = _IgsVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 4)
)
if mibBuilder.loadTexts:
    igsVlanFilterTable.setStatus("mandatory")
_IgsVlanFilterEntry_Object = MibTableRow
igsVlanFilterEntry = _IgsVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 4, 1)
)
igsVlanFilterEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "igsVlanId"),
)
if mibBuilder.loadTexts:
    igsVlanFilterEntry.setStatus("mandatory")


class _IgsVlanId_Type(Integer32):
    """Custom type igsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_IgsVlanId_Type.__name__ = "Integer32"
_IgsVlanId_Object = MibTableColumn
igsVlanId = _IgsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 4, 1, 1),
    _IgsVlanId_Type()
)
igsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igsVlanId.setStatus("mandatory")


class _IgsVlanFilterStatus_Type(Integer32):
    """Custom type igsVlanFilterStatus based on Integer32"""
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


_IgsVlanFilterStatus_Type.__name__ = "Integer32"
_IgsVlanFilterStatus_Object = MibTableColumn
igsVlanFilterStatus = _IgsVlanFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 22, 3, 4, 1, 2),
    _IgsVlanFilterStatus_Type()
)
igsVlanFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igsVlanFilterStatus.setStatus("mandatory")
_CompanyDot1xGroup_ObjectIdentity = ObjectIdentity
companyDot1xGroup = _CompanyDot1xGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23)
)
_Radius_ObjectIdentity = ObjectIdentity
radius = _Radius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 1)
)
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibScalar
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 1, 1),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("mandatory")


class _RadiusServerPort_Type(Integer32):
    """Custom type radiusServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerPort_Type.__name__ = "Integer32"
_RadiusServerPort_Object = MibScalar
radiusServerPort = _RadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 1, 2),
    _RadiusServerPort_Type()
)
radiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPort.setStatus("mandatory")
_RadiusServerSharedSecret_Type = DisplayString
_RadiusServerSharedSecret_Object = MibScalar
radiusServerSharedSecret = _RadiusServerSharedSecret_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 1, 3),
    _RadiusServerSharedSecret_Type()
)
radiusServerSharedSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerSharedSecret.setStatus("mandatory")
_Dot1xAuth_ObjectIdentity = ObjectIdentity
dot1xAuth = _Dot1xAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2)
)


class _Dot1xAuthSystemControl_Type(Integer32):
    """Custom type dot1xAuthSystemControl based on Integer32"""
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


_Dot1xAuthSystemControl_Type.__name__ = "Integer32"
_Dot1xAuthSystemControl_Object = MibScalar
dot1xAuthSystemControl = _Dot1xAuthSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 1),
    _Dot1xAuthSystemControl_Type()
)
dot1xAuthSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthSystemControl.setStatus("mandatory")


class _Dot1xAuthQuietPeriod_Type(Integer32):
    """Custom type dot1xAuthQuietPeriod based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1xAuthQuietPeriod_Type.__name__ = "Integer32"
_Dot1xAuthQuietPeriod_Object = MibScalar
dot1xAuthQuietPeriod = _Dot1xAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 2),
    _Dot1xAuthQuietPeriod_Type()
)
dot1xAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthQuietPeriod.setStatus("mandatory")


class _Dot1xAuthTxPeriod_Type(Integer32):
    """Custom type dot1xAuthTxPeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xAuthTxPeriod_Type.__name__ = "Integer32"
_Dot1xAuthTxPeriod_Object = MibScalar
dot1xAuthTxPeriod = _Dot1xAuthTxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 3),
    _Dot1xAuthTxPeriod_Type()
)
dot1xAuthTxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthTxPeriod.setStatus("mandatory")


class _Dot1xAuthSuppTimeout_Type(Integer32):
    """Custom type dot1xAuthSuppTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xAuthSuppTimeout_Type.__name__ = "Integer32"
_Dot1xAuthSuppTimeout_Object = MibScalar
dot1xAuthSuppTimeout = _Dot1xAuthSuppTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 4),
    _Dot1xAuthSuppTimeout_Type()
)
dot1xAuthSuppTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthSuppTimeout.setStatus("mandatory")


class _Dot1xAuthServerTimeout_Type(Integer32):
    """Custom type dot1xAuthServerTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1xAuthServerTimeout_Type.__name__ = "Integer32"
_Dot1xAuthServerTimeout_Object = MibScalar
dot1xAuthServerTimeout = _Dot1xAuthServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 5),
    _Dot1xAuthServerTimeout_Type()
)
dot1xAuthServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthServerTimeout.setStatus("mandatory")


class _Dot1xAuthMaxReq_Type(Integer32):
    """Custom type dot1xAuthMaxReq based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Dot1xAuthMaxReq_Type.__name__ = "Integer32"
_Dot1xAuthMaxReq_Object = MibScalar
dot1xAuthMaxReq = _Dot1xAuthMaxReq_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 6),
    _Dot1xAuthMaxReq_Type()
)
dot1xAuthMaxReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthMaxReq.setStatus("mandatory")


class _Dot1xAuthReAuthPeriod_Type(Unsigned32):
    """Custom type dot1xAuthReAuthPeriod based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Dot1xAuthReAuthPeriod_Type.__name__ = "Unsigned32"
_Dot1xAuthReAuthPeriod_Object = MibScalar
dot1xAuthReAuthPeriod = _Dot1xAuthReAuthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 7),
    _Dot1xAuthReAuthPeriod_Type()
)
dot1xAuthReAuthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthReAuthPeriod.setStatus("mandatory")


class _Dot1xAuthReAuthEnabled_Type(Integer32):
    """Custom type dot1xAuthReAuthEnabled based on Integer32"""
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


_Dot1xAuthReAuthEnabled_Type.__name__ = "Integer32"
_Dot1xAuthReAuthEnabled_Object = MibScalar
dot1xAuthReAuthEnabled = _Dot1xAuthReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 8),
    _Dot1xAuthReAuthEnabled_Type()
)
dot1xAuthReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthReAuthEnabled.setStatus("mandatory")
_Dot1xAuthConfigPortTable_Object = MibTable
dot1xAuthConfigPortTable = _Dot1xAuthConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 9)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigPortTable.setStatus("mandatory")
_Dot1xAuthConfigPortEntry_Object = MibTableRow
dot1xAuthConfigPortEntry = _Dot1xAuthConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 9, 1)
)
dot1xAuthConfigPortEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "dot1xAuthConfigPortNumber"),
)
if mibBuilder.loadTexts:
    dot1xAuthConfigPortEntry.setStatus("mandatory")
_Dot1xAuthConfigPortNumber_Type = Integer32
_Dot1xAuthConfigPortNumber_Object = MibTableColumn
dot1xAuthConfigPortNumber = _Dot1xAuthConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 9, 1, 1),
    _Dot1xAuthConfigPortNumber_Type()
)
dot1xAuthConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortNumber.setStatus("mandatory")


class _Dot1xAuthConfigPortControl_Type(Integer32):
    """Custom type dot1xAuthConfigPortControl based on Integer32"""
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


_Dot1xAuthConfigPortControl_Type.__name__ = "Integer32"
_Dot1xAuthConfigPortControl_Object = MibTableColumn
dot1xAuthConfigPortControl = _Dot1xAuthConfigPortControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 9, 1, 2),
    _Dot1xAuthConfigPortControl_Type()
)
dot1xAuthConfigPortControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortControl.setStatus("mandatory")


class _Dot1xAuthConfigPortStatus_Type(Integer32):
    """Custom type dot1xAuthConfigPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authnull", 0),
          ("authorized", 1),
          ("unauthorized", 2))
    )


_Dot1xAuthConfigPortStatus_Type.__name__ = "Integer32"
_Dot1xAuthConfigPortStatus_Object = MibTableColumn
dot1xAuthConfigPortStatus = _Dot1xAuthConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 9, 1, 3),
    _Dot1xAuthConfigPortStatus_Type()
)
dot1xAuthConfigPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortStatus.setStatus("mandatory")
_Dot1xAuthConfigPortSessionTime_Type = TimeTicks
_Dot1xAuthConfigPortSessionTime_Object = MibTableColumn
dot1xAuthConfigPortSessionTime = _Dot1xAuthConfigPortSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 9, 1, 4),
    _Dot1xAuthConfigPortSessionTime_Type()
)
dot1xAuthConfigPortSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortSessionTime.setStatus("mandatory")
_Dot1xAuthConfigPortSessionUserName_Type = DisplayString
_Dot1xAuthConfigPortSessionUserName_Object = MibTableColumn
dot1xAuthConfigPortSessionUserName = _Dot1xAuthConfigPortSessionUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 23, 2, 9, 1, 5),
    _Dot1xAuthConfigPortSessionUserName_Type()
)
dot1xAuthConfigPortSessionUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xAuthConfigPortSessionUserName.setStatus("mandatory")
_CompanyQoSGroup_ObjectIdentity = ObjectIdentity
companyQoSGroup = _CompanyQoSGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26)
)


class _QosMode_Type(Integer32):
    """Custom type qosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1p", 1),
          ("dscp", 2))
    )


_QosMode_Type.__name__ = "Integer32"
_QosMode_Object = MibScalar
qosMode = _QosMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 1),
    _QosMode_Type()
)
qosMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMode.setStatus("mandatory")


class _QueuingMechanism_Type(Integer32):
    """Custom type queuingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictPriority", 1),
          ("wrr", 2))
    )


_QueuingMechanism_Type.__name__ = "Integer32"
_QueuingMechanism_Object = MibScalar
queuingMechanism = _QueuingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 2),
    _QueuingMechanism_Type()
)
queuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMechanism.setStatus("mandatory")
_Dot1pPortTable_Object = MibTable
dot1pPortTable = _Dot1pPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 3)
)
if mibBuilder.loadTexts:
    dot1pPortTable.setStatus("mandatory")
_Dot1pPortEntry_Object = MibTableRow
dot1pPortEntry = _Dot1pPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 3, 1)
)
dot1pPortEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "dot1pPortIndex"),
)
if mibBuilder.loadTexts:
    dot1pPortEntry.setStatus("mandatory")
_Dot1pPortIndex_Type = Integer32
_Dot1pPortIndex_Object = MibTableColumn
dot1pPortIndex = _Dot1pPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 3, 1, 1),
    _Dot1pPortIndex_Type()
)
dot1pPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1pPortIndex.setStatus("mandatory")


class _Dot1pPortPriority_Type(Integer32):
    """Custom type dot1pPortPriority based on Integer32"""
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
        *(("high", 3),
          ("highest", 4),
          ("low", 1),
          ("middle", 2))
    )


_Dot1pPortPriority_Type.__name__ = "Integer32"
_Dot1pPortPriority_Object = MibTableColumn
dot1pPortPriority = _Dot1pPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 3, 1, 2),
    _Dot1pPortPriority_Type()
)
dot1pPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1pPortPriority.setStatus("mandatory")
_DscpTable_Object = MibTable
dscpTable = _DscpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 4)
)
if mibBuilder.loadTexts:
    dscpTable.setStatus("mandatory")
_DscpEntry_Object = MibTableRow
dscpEntry = _DscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 4, 1)
)
dscpEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "dscpIndex"),
)
if mibBuilder.loadTexts:
    dscpEntry.setStatus("mandatory")


class _DscpIndex_Type(Integer32):
    """Custom type dscpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DscpIndex_Type.__name__ = "Integer32"
_DscpIndex_Object = MibTableColumn
dscpIndex = _DscpIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 4, 1, 1),
    _DscpIndex_Type()
)
dscpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dscpIndex.setStatus("mandatory")


class _DscpPriority_Type(Integer32):
    """Custom type dscpPriority based on Integer32"""
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
        *(("high", 3),
          ("highest", 4),
          ("low", 1),
          ("middle", 2))
    )


_DscpPriority_Type.__name__ = "Integer32"
_DscpPriority_Object = MibTableColumn
dscpPriority = _DscpPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 26, 4, 1, 2),
    _DscpPriority_Type()
)
dscpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dscpPriority.setStatus("mandatory")
_CompanyTrafficMgmt_ObjectIdentity = ObjectIdentity
companyTrafficMgmt = _CompanyTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 27)
)
_BroadcastStormCtrlSettings_ObjectIdentity = ObjectIdentity
broadcastStormCtrlSettings = _BroadcastStormCtrlSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 27, 3)
)


class _BroadcastStormCtrlGlobalOnOff_Type(Integer32):
    """Custom type broadcastStormCtrlGlobalOnOff based on Integer32"""
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


_BroadcastStormCtrlGlobalOnOff_Type.__name__ = "Integer32"
_BroadcastStormCtrlGlobalOnOff_Object = MibScalar
broadcastStormCtrlGlobalOnOff = _BroadcastStormCtrlGlobalOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 27, 3, 1),
    _BroadcastStormCtrlGlobalOnOff_Type()
)
broadcastStormCtrlGlobalOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormCtrlGlobalOnOff.setStatus("mandatory")


class _BroadcastStormGlobalThreshold_Type(Integer32):
    """Custom type broadcastStormGlobalThreshold based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("kBps-1024", 9),
          ("kBps-128", 6),
          ("kBps-16", 3),
          ("kBps-2048", 10),
          ("kBps-256", 7),
          ("kBps-32", 4),
          ("kBps-4096", 11),
          ("kBps-512", 8),
          ("kBps-64", 5),
          ("kBps-8", 2))
    )


_BroadcastStormGlobalThreshold_Type.__name__ = "Integer32"
_BroadcastStormGlobalThreshold_Object = MibScalar
broadcastStormGlobalThreshold = _BroadcastStormGlobalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 27, 3, 2),
    _BroadcastStormGlobalThreshold_Type()
)
broadcastStormGlobalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    broadcastStormGlobalThreshold.setStatus("mandatory")
_CompanySecurity_ObjectIdentity = ObjectIdentity
companySecurity = _CompanySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28)
)
_TrustedHostSettings_ObjectIdentity = ObjectIdentity
trustedHostSettings = _TrustedHostSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1)
)


class _TrustedHostOnOff_Type(Integer32):
    """Custom type trustedHostOnOff based on Integer32"""
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


_TrustedHostOnOff_Type.__name__ = "Integer32"
_TrustedHostOnOff_Object = MibScalar
trustedHostOnOff = _TrustedHostOnOff_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1, 1),
    _TrustedHostOnOff_Type()
)
trustedHostOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostOnOff.setStatus("mandatory")
_TrustedHostTable_Object = MibTable
trustedHostTable = _TrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1, 2)
)
if mibBuilder.loadTexts:
    trustedHostTable.setStatus("mandatory")
_TrustedHostEntry_Object = MibTableRow
trustedHostEntry = _TrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1, 2, 1)
)
trustedHostEntry.setIndexNames(
    (0, "DGS-1224T-DX-MIB", "trustedHostID"),
)
if mibBuilder.loadTexts:
    trustedHostEntry.setStatus("mandatory")
_TrustedHostID_Type = Integer32
_TrustedHostID_Object = MibTableColumn
trustedHostID = _TrustedHostID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1, 2, 1, 1),
    _TrustedHostID_Type()
)
trustedHostID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trustedHostID.setStatus("mandatory")
_TrustedHostIpAddress_Type = IpAddress
_TrustedHostIpAddress_Object = MibTableColumn
trustedHostIpAddress = _TrustedHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1, 2, 1, 2),
    _TrustedHostIpAddress_Type()
)
trustedHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostIpAddress.setStatus("mandatory")
_TrustedHostIpMask_Type = IpAddress
_TrustedHostIpMask_Object = MibTableColumn
trustedHostIpMask = _TrustedHostIpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1, 2, 1, 3),
    _TrustedHostIpMask_Type()
)
trustedHostIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostIpMask.setStatus("mandatory")


class _TrustedHostStatus_Type(Integer32):
    """Custom type trustedHostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndwait", 5),
          ("destroy", 6),
          ("notready", 3))
    )


_TrustedHostStatus_Type.__name__ = "Integer32"
_TrustedHostStatus_Object = MibTableColumn
trustedHostStatus = _TrustedHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 28, 1, 2, 1, 4),
    _TrustedHostStatus_Type()
)
trustedHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trustedHostStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

swFiberInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 0, 1)
)
if mibBuilder.loadTexts:
    swFiberInsert.setStatus(
        ""
    )

swFiberRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 0, 2)
)
if mibBuilder.loadTexts:
    swFiberRemove.setStatus(
        ""
    )

swFiberAbnormalRXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 0, 3)
)
if mibBuilder.loadTexts:
    swFiberAbnormalRXError.setStatus(
        ""
    )

swFiberAbnormalTXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 0, 4)
)
if mibBuilder.loadTexts:
    swFiberAbnormalTXError.setStatus(
        ""
    )

swTPAbnormalRXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 0, 5)
)
if mibBuilder.loadTexts:
    swTPAbnormalRXError.setStatus(
        ""
    )

swTPAbnormalTXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 76, 5, 0, 6)
)
if mibBuilder.loadTexts:
    swTPAbnormalTXError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DGS-1224T-DX-MIB",
    **{"OwnerString": OwnerString,
       "MacAddress": MacAddress,
       "PortList": PortList,
       "RowStatus": RowStatus,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DGS12XXTSeriesProd": dlink_DGS12XXTSeriesProd,
       "dgs-1224tdx": dgs_1224tdx,
       "swFiberInsert": swFiberInsert,
       "swFiberRemove": swFiberRemove,
       "swFiberAbnormalRXError": swFiberAbnormalRXError,
       "swFiberAbnormalTXError": swFiberAbnormalTXError,
       "swTPAbnormalRXError": swTPAbnormalRXError,
       "swTPAbnormalTXError": swTPAbnormalTXError,
       "companyCommGroup": companyCommGroup,
       "commSetTable": commSetTable,
       "commSetEntry": commSetEntry,
       "commSetIndex": commSetIndex,
       "commSetName": commSetName,
       "commSetStatus": commSetStatus,
       "commGetTable": commGetTable,
       "commGetEntry": commGetEntry,
       "commGetIndex": commGetIndex,
       "commGetName": commGetName,
       "commGetStatus": commGetStatus,
       "commTrapTable": commTrapTable,
       "commTrapEntry": commTrapEntry,
       "commTrapIndex": commTrapIndex,
       "commTrapName": commTrapName,
       "commTrapIpAddress": commTrapIpAddress,
       "commTrapSNMPBootup": commTrapSNMPBootup,
       "commTrapSNMPTPLinkUpDown": commTrapSNMPTPLinkUpDown,
       "commTrapSNMPFiberLinkUpDown": commTrapSNMPFiberLinkUpDown,
       "commTrapTrapAbnormalTPRXError": commTrapTrapAbnormalTPRXError,
       "commTrapTrapAbnormalTPTXError": commTrapTrapAbnormalTPTXError,
       "commTrapTrapAbnormalFiberRXError": commTrapTrapAbnormalFiberRXError,
       "commTrapTrapAbnormalFiberTXError": commTrapTrapAbnormalFiberTXError,
       "commTrapStatus": commTrapStatus,
       "companyMiscGroup": companyMiscGroup,
       "miscReset": miscReset,
       "miscStatisticsReset": miscStatisticsReset,
       "companySpanGroup": companySpanGroup,
       "spanOnOff": spanOnOff,
       "companyConfigGroup": companyConfigGroup,
       "configVerSwPrimary": configVerSwPrimary,
       "configVerHwChipSet": configVerHwChipSet,
       "configBootTftpOperation": configBootTftpOperation,
       "configBootTftpServerIp": configBootTftpServerIp,
       "configBootImageFileName": configBootImageFileName,
       "configPortTable": configPortTable,
       "configPortEntry": configPortEntry,
       "configPort": configPort,
       "configPortSpeed": configPortSpeed,
       "configPortOperStatus": configPortOperStatus,
       "configPortFlowControl": configPortFlowControl,
       "configPortFlowControlOper": configPortFlowControlOper,
       "configVLANMode": configVLANMode,
       "configMirrorTable": configMirrorTable,
       "configMirrorEntry": configMirrorEntry,
       "configMirrorId": configMirrorId,
       "configMirrorMon": configMirrorMon,
       "configMirrorTXSrc": configMirrorTXSrc,
       "configMirrorRXSrc": configMirrorRXSrc,
       "configMirrorStatus": configMirrorStatus,
       "configSNMPEnable": configSNMPEnable,
       "configIpAssignmentMode": configIpAssignmentMode,
       "configPhysAddress": configPhysAddress,
       "configPasswordAdmin": configPasswordAdmin,
       "configIpAddress": configIpAddress,
       "configNetMask": configNetMask,
       "configGateway": configGateway,
       "configSave": configSave,
       "configRestoreDefaults": configRestoreDefaults,
       "configTftpServerIpAddress": configTftpServerIpAddress,
       "configTftpServerFileName": configTftpServerFileName,
       "configTftpOperation": configTftpOperation,
       "configJumboEnable": configJumboEnable,
       "configSafeguardEnable": configSafeguardEnable,
       "configPowerSavingEnable": configPowerSavingEnable,
       "companyTVlanGroup": companyTVlanGroup,
       "tvlanTable": tvlanTable,
       "tvlanEntry": tvlanEntry,
       "tvlanId": tvlanId,
       "tvlanName": tvlanName,
       "tvlanMember": tvlanMember,
       "tvlanUntaggedPorts": tvlanUntaggedPorts,
       "tvlanStatus": tvlanStatus,
       "tvlanManagementOnOff": tvlanManagementOnOff,
       "tvlanManagementid": tvlanManagementid,
       "tvlanPortTable": tvlanPortTable,
       "tvlanPortEntry": tvlanPortEntry,
       "tvlanPortPortId": tvlanPortPortId,
       "tvlanPortVlanId": tvlanPortVlanId,
       "tvlanAsyOnOff": tvlanAsyOnOff,
       "companyPortTrunkGroup": companyPortTrunkGroup,
       "portTrunkTable": portTrunkTable,
       "portTrunkEntry": portTrunkEntry,
       "portTrunkId": portTrunkId,
       "portTrunkName": portTrunkName,
       "portTrunkMember": portTrunkMember,
       "companyStaticGroup": companyStaticGroup,
       "staticOnOff": staticOnOff,
       "staticAutoLearning": staticAutoLearning,
       "staticTable": staticTable,
       "staticEntry": staticEntry,
       "staticId": staticId,
       "staticMac": staticMac,
       "staticPort": staticPort,
       "staticVlanID": staticVlanID,
       "staticStatus": staticStatus,
       "companyIgsGroup": companyIgsGroup,
       "igsSystem": igsSystem,
       "igsStatus": igsStatus,
       "igsv3Processing": igsv3Processing,
       "igsRouterPortPurgeInterval": igsRouterPortPurgeInterval,
       "igsHostPortPurgeInterval": igsHostPortPurgeInterval,
       "igsReportForwardInterval": igsReportForwardInterval,
       "igsLeaveProcessInterval": igsLeaveProcessInterval,
       "igsMcastEntryAgeingInterval": igsMcastEntryAgeingInterval,
       "igsSharedSegmentAggregationInterval": igsSharedSegmentAggregationInterval,
       "igsGblReportFwdOnAllPorts": igsGblReportFwdOnAllPorts,
       "igsNextMcastFwdMode": igsNextMcastFwdMode,
       "igsQueryInterval": igsQueryInterval,
       "igsQueryMaxResponseTime": igsQueryMaxResponseTime,
       "igsRobustnessValue": igsRobustnessValue,
       "igsLastMembQueryInterval": igsLastMembQueryInterval,
       "igsQuerierStateOnOff": igsQuerierStateOnOff,
       "igsVlan": igsVlan,
       "igsVlanMcastFwdTable": igsVlanMcastFwdTable,
       "igsVlanMcastFwdEntry": igsVlanMcastFwdEntry,
       "igsVlanMcastFwdVlanIdMac": igsVlanMcastFwdVlanIdMac,
       "igsVlanMcastFwdGroupAddress": igsVlanMcastFwdGroupAddress,
       "igsVlanMcastFwdPortListMac": igsVlanMcastFwdPortListMac,
       "igsVlanRouterPortListTable": igsVlanRouterPortListTable,
       "igsVlanRouterPortListEntry": igsVlanRouterPortListEntry,
       "igsVlanRouterPortListVlanId": igsVlanRouterPortListVlanId,
       "igsVlanRouterPortList": igsVlanRouterPortList,
       "igsVlanFilterTable": igsVlanFilterTable,
       "igsVlanFilterEntry": igsVlanFilterEntry,
       "igsVlanId": igsVlanId,
       "igsVlanFilterStatus": igsVlanFilterStatus,
       "companyDot1xGroup": companyDot1xGroup,
       "radius": radius,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerPort": radiusServerPort,
       "radiusServerSharedSecret": radiusServerSharedSecret,
       "dot1xAuth": dot1xAuth,
       "dot1xAuthSystemControl": dot1xAuthSystemControl,
       "dot1xAuthQuietPeriod": dot1xAuthQuietPeriod,
       "dot1xAuthTxPeriod": dot1xAuthTxPeriod,
       "dot1xAuthSuppTimeout": dot1xAuthSuppTimeout,
       "dot1xAuthServerTimeout": dot1xAuthServerTimeout,
       "dot1xAuthMaxReq": dot1xAuthMaxReq,
       "dot1xAuthReAuthPeriod": dot1xAuthReAuthPeriod,
       "dot1xAuthReAuthEnabled": dot1xAuthReAuthEnabled,
       "dot1xAuthConfigPortTable": dot1xAuthConfigPortTable,
       "dot1xAuthConfigPortEntry": dot1xAuthConfigPortEntry,
       "dot1xAuthConfigPortNumber": dot1xAuthConfigPortNumber,
       "dot1xAuthConfigPortControl": dot1xAuthConfigPortControl,
       "dot1xAuthConfigPortStatus": dot1xAuthConfigPortStatus,
       "dot1xAuthConfigPortSessionTime": dot1xAuthConfigPortSessionTime,
       "dot1xAuthConfigPortSessionUserName": dot1xAuthConfigPortSessionUserName,
       "companyQoSGroup": companyQoSGroup,
       "qosMode": qosMode,
       "queuingMechanism": queuingMechanism,
       "dot1pPortTable": dot1pPortTable,
       "dot1pPortEntry": dot1pPortEntry,
       "dot1pPortIndex": dot1pPortIndex,
       "dot1pPortPriority": dot1pPortPriority,
       "dscpTable": dscpTable,
       "dscpEntry": dscpEntry,
       "dscpIndex": dscpIndex,
       "dscpPriority": dscpPriority,
       "companyTrafficMgmt": companyTrafficMgmt,
       "broadcastStormCtrlSettings": broadcastStormCtrlSettings,
       "broadcastStormCtrlGlobalOnOff": broadcastStormCtrlGlobalOnOff,
       "broadcastStormGlobalThreshold": broadcastStormGlobalThreshold,
       "companySecurity": companySecurity,
       "trustedHostSettings": trustedHostSettings,
       "trustedHostOnOff": trustedHostOnOff,
       "trustedHostTable": trustedHostTable,
       "trustedHostEntry": trustedHostEntry,
       "trustedHostID": trustedHostID,
       "trustedHostIpAddress": trustedHostIpAddress,
       "trustedHostIpMask": trustedHostIpMask,
       "trustedHostStatus": trustedHostStatus}
)
