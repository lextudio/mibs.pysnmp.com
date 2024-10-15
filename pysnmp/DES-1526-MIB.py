# SNMP MIB module (DES-1526-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES-1526-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:40 2024
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
_Dlink_DES1526SeriesProd_ObjectIdentity = ObjectIdentity
dlink_DES1526SeriesProd = _Dlink_DES1526SeriesProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 60)
)
_DES_1526_ObjectIdentity = ObjectIdentity
DES_1526 = _DES_1526_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1)
)
_CompanyCommGroup_ObjectIdentity = ObjectIdentity
companyCommGroup = _CompanyCommGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1)
)
_CommSetTable_Object = MibTable
commSetTable = _CommSetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 1)
)
if mibBuilder.loadTexts:
    commSetTable.setStatus("mandatory")
_CommSetEntry_Object = MibTableRow
commSetEntry = _CommSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 1, 1)
)
commSetEntry.setIndexNames(
    (0, "DES-1526-MIB", "commSetIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 1, 1, 2),
    _CommSetName_Type()
)
commSetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSetName.setStatus("mandatory")
_CommSetStatus_Type = RowStatus
_CommSetStatus_Object = MibTableColumn
commSetStatus = _CommSetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 1, 1, 3),
    _CommSetStatus_Type()
)
commSetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commSetStatus.setStatus("mandatory")
_CommGetTable_Object = MibTable
commGetTable = _CommGetTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 2)
)
if mibBuilder.loadTexts:
    commGetTable.setStatus("mandatory")
_CommGetEntry_Object = MibTableRow
commGetEntry = _CommGetEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 2, 1)
)
commGetEntry.setIndexNames(
    (0, "DES-1526-MIB", "commGetIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 2, 1, 2),
    _CommGetName_Type()
)
commGetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commGetName.setStatus("mandatory")
_CommGetStatus_Type = RowStatus
_CommGetStatus_Object = MibTableColumn
commGetStatus = _CommGetStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 2, 1, 3),
    _CommGetStatus_Type()
)
commGetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commGetStatus.setStatus("mandatory")
_CommTrapTable_Object = MibTable
commTrapTable = _CommTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3)
)
if mibBuilder.loadTexts:
    commTrapTable.setStatus("mandatory")
_CommTrapEntry_Object = MibTableRow
commTrapEntry = _CommTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1)
)
commTrapEntry.setIndexNames(
    (0, "DES-1526-MIB", "commTrapIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 2),
    _CommTrapName_Type()
)
commTrapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapName.setStatus("mandatory")
_CommTrapIpAddress_Type = IpAddress
_CommTrapIpAddress_Object = MibTableColumn
commTrapIpAddress = _CommTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 3),
    _CommTrapIpAddress_Type()
)
commTrapIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapIpAddress.setStatus("mandatory")
_CommTrapVlanId_Type = Integer32
_CommTrapVlanId_Object = MibTableColumn
commTrapVlanId = _CommTrapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 4),
    _CommTrapVlanId_Type()
)
commTrapVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapVlanId.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 12),
    _CommTrapTrapAbnormalFiberTXError_Type()
)
commTrapTrapAbnormalFiberTXError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapAbnormalFiberTXError.setStatus("mandatory")


class _CommTrapTrapPOEPowerFail_Type(Integer32):
    """Custom type commTrapTrapPOEPowerFail based on Integer32"""
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


_CommTrapTrapPOEPowerFail_Type.__name__ = "Integer32"
_CommTrapTrapPOEPowerFail_Object = MibTableColumn
commTrapTrapPOEPowerFail = _CommTrapTrapPOEPowerFail_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 13),
    _CommTrapTrapPOEPowerFail_Type()
)
commTrapTrapPOEPowerFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapPOEPowerFail.setStatus("mandatory")


class _CommTrapTrapPOEPortOvercurrent_Type(Integer32):
    """Custom type commTrapTrapPOEPortOvercurrent based on Integer32"""
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


_CommTrapTrapPOEPortOvercurrent_Type.__name__ = "Integer32"
_CommTrapTrapPOEPortOvercurrent_Object = MibTableColumn
commTrapTrapPOEPortOvercurrent = _CommTrapTrapPOEPortOvercurrent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 14),
    _CommTrapTrapPOEPortOvercurrent_Type()
)
commTrapTrapPOEPortOvercurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapPOEPortOvercurrent.setStatus("mandatory")


class _CommTrapTrapPOEPortShort_Type(Integer32):
    """Custom type commTrapTrapPOEPortShort based on Integer32"""
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


_CommTrapTrapPOEPortShort_Type.__name__ = "Integer32"
_CommTrapTrapPOEPortShort_Object = MibTableColumn
commTrapTrapPOEPortShort = _CommTrapTrapPOEPortShort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 15),
    _CommTrapTrapPOEPortShort_Type()
)
commTrapTrapPOEPortShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapTrapPOEPortShort.setStatus("mandatory")
_CommTrapStatus_Type = RowStatus
_CommTrapStatus_Object = MibTableColumn
commTrapStatus = _CommTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 1, 3, 1, 16),
    _CommTrapStatus_Type()
)
commTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTrapStatus.setStatus("mandatory")
_CompanyMiscGroup_ObjectIdentity = ObjectIdentity
companyMiscGroup = _CompanyMiscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 3)
)


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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 3, 3),
    _MiscStatisticsReset_Type()
)
miscStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscStatisticsReset.setStatus("mandatory")
_CompanyConfigGroup_ObjectIdentity = ObjectIdentity
companyConfigGroup = _CompanyConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11)
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 2),
    _ConfigVerHwChipSet_Type()
)
configVerHwChipSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configVerHwChipSet.setStatus("mandatory")
_ConfigPortTable_Object = MibTable
configPortTable = _ConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6)
)
if mibBuilder.loadTexts:
    configPortTable.setStatus("mandatory")
_ConfigPortEntry_Object = MibTableRow
configPortEntry = _ConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6, 1)
)
configPortEntry.setIndexNames(
    (0, "DES-1526-MIB", "configPort"),
)
if mibBuilder.loadTexts:
    configPortEntry.setStatus("mandatory")
_ConfigPort_Type = Integer32
_ConfigPort_Object = MibTableColumn
configPort = _ConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6, 1, 1),
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("disable", 1),
          ("rate100M-Full", 6),
          ("rate100M-Half", 5),
          ("rate10M-Full", 4),
          ("rate10M-Half", 3))
    )


_ConfigPortSpeed_Type.__name__ = "Integer32"
_ConfigPortSpeed_Object = MibTableColumn
configPortSpeed = _ConfigPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6, 1, 2),
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("rate100M-Full", 5),
          ("rate100M-Half", 4),
          ("rate10M-Full", 3),
          ("rate10M-Half", 2),
          ("rate1G-Full", 7),
          ("rate1G-Half", 6))
    )


_ConfigPortOperStatus_Type.__name__ = "Integer32"
_ConfigPortOperStatus_Object = MibTableColumn
configPortOperStatus = _ConfigPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6, 1, 5),
    _ConfigPortFlowControlOper_Type()
)
configPortFlowControlOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configPortFlowControlOper.setStatus("mandatory")


class _ConfigPortPriority_Type(Integer32):
    """Custom type configPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_ConfigPortPriority_Type.__name__ = "Integer32"
_ConfigPortPriority_Object = MibTableColumn
configPortPriority = _ConfigPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 6, 1, 6),
    _ConfigPortPriority_Type()
)
configPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configPortPriority.setStatus("mandatory")
_ConfigMirrorTable_Object = MibTable
configMirrorTable = _ConfigMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 8)
)
if mibBuilder.loadTexts:
    configMirrorTable.setStatus("mandatory")
_ConfigMirrorEntry_Object = MibTableRow
configMirrorEntry = _ConfigMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 8, 1)
)
configMirrorEntry.setIndexNames(
    (0, "DES-1526-MIB", "configMirrorId"),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 8, 1, 1),
    _ConfigMirrorId_Type()
)
configMirrorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configMirrorId.setStatus("mandatory")


class _ConfigMirrorMode_Type(Integer32):
    """Custom type configMirrorMode based on Integer32"""
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
        *(("Rx", 1),
          ("Tx", 2),
          ("both", 3),
          ("disabled", 0))
    )


_ConfigMirrorMode_Type.__name__ = "Integer32"
_ConfigMirrorMode_Object = MibTableColumn
configMirrorMode = _ConfigMirrorMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 8, 1, 2),
    _ConfigMirrorMode_Type()
)
configMirrorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorMode.setStatus("mandatory")
_ConfigMirrorMon_Type = Integer32
_ConfigMirrorMon_Object = MibTableColumn
configMirrorMon = _ConfigMirrorMon_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 8, 1, 3),
    _ConfigMirrorMon_Type()
)
configMirrorMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorMon.setStatus("mandatory")
_ConfigMirrorSrc_Type = PortList
_ConfigMirrorSrc_Object = MibTableColumn
configMirrorSrc = _ConfigMirrorSrc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 8, 1, 4),
    _ConfigMirrorSrc_Type()
)
configMirrorSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMirrorSrc.setStatus("mandatory")
_ConfigMirrorStatus_Type = RowStatus
_ConfigMirrorStatus_Object = MibTableColumn
configMirrorStatus = _ConfigMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 8, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 9),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 12),
    _ConfigIpAssignmentMode_Type()
)
configIpAssignmentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpAssignmentMode.setStatus("mandatory")
_ConfigPhysAddress_Type = MacAddress
_ConfigPhysAddress_Object = MibScalar
configPhysAddress = _ConfigPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 13),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 15),
    _ConfigPasswordAdmin_Type()
)
configPasswordAdmin.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    configPasswordAdmin.setStatus("mandatory")
_ConfigIpAddress_Type = IpAddress
_ConfigIpAddress_Object = MibScalar
configIpAddress = _ConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 16),
    _ConfigIpAddress_Type()
)
configIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configIpAddress.setStatus("mandatory")
_ConfigNetMask_Type = IpAddress
_ConfigNetMask_Object = MibScalar
configNetMask = _ConfigNetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 17),
    _ConfigNetMask_Type()
)
configNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNetMask.setStatus("mandatory")
_ConfigGateway_Type = IpAddress
_ConfigGateway_Object = MibScalar
configGateway = _ConfigGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 18),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 19),
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
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 11, 22),
    _ConfigRestoreDefaults_Type()
)
configRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRestoreDefaults.setStatus("mandatory")
_CompanyTVlanGroup_ObjectIdentity = ObjectIdentity
companyTVlanGroup = _CompanyTVlanGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13)
)
_TvlanTable_Object = MibTable
tvlanTable = _TvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 1)
)
if mibBuilder.loadTexts:
    tvlanTable.setStatus("mandatory")
_TvlanEntry_Object = MibTableRow
tvlanEntry = _TvlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 1, 1)
)
tvlanEntry.setIndexNames(
    (0, "DES-1526-MIB", "tvlanId"),
)
if mibBuilder.loadTexts:
    tvlanEntry.setStatus("mandatory")
_TvlanId_Type = Integer32
_TvlanId_Object = MibTableColumn
tvlanId = _TvlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 1, 1, 1),
    _TvlanId_Type()
)
tvlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvlanId.setStatus("mandatory")
_TvlanMember_Type = PortList
_TvlanMember_Object = MibTableColumn
tvlanMember = _TvlanMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 1, 1, 3),
    _TvlanMember_Type()
)
tvlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanMember.setStatus("mandatory")
_TvlanUntaggedPorts_Type = PortList
_TvlanUntaggedPorts_Object = MibTableColumn
tvlanUntaggedPorts = _TvlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 1, 1, 4),
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
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("destroy", 6))
    )


_TvlanStatus_Type.__name__ = "Integer32"
_TvlanStatus_Object = MibTableColumn
tvlanStatus = _TvlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 1, 1, 5),
    _TvlanStatus_Type()
)
tvlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanStatus.setStatus("mandatory")
_TvlanPortTable_Object = MibTable
tvlanPortTable = _TvlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 2)
)
if mibBuilder.loadTexts:
    tvlanPortTable.setStatus("mandatory")
_TvlanPortEntry_Object = MibTableRow
tvlanPortEntry = _TvlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 2, 1)
)
tvlanPortEntry.setIndexNames(
    (0, "DES-1526-MIB", "tvlanPortPortId"),
)
if mibBuilder.loadTexts:
    tvlanPortEntry.setStatus("mandatory")
_TvlanPortPortId_Type = Integer32
_TvlanPortPortId_Object = MibTableColumn
tvlanPortPortId = _TvlanPortPortId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 2, 1, 1),
    _TvlanPortPortId_Type()
)
tvlanPortPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tvlanPortPortId.setStatus("mandatory")
_TvlanPortVlanId_Type = Integer32
_TvlanPortVlanId_Object = MibTableColumn
tvlanPortVlanId = _TvlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 13, 2, 1, 2),
    _TvlanPortVlanId_Type()
)
tvlanPortVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tvlanPortVlanId.setStatus("mandatory")
_CompanyPortTrunkGroup_ObjectIdentity = ObjectIdentity
companyPortTrunkGroup = _CompanyPortTrunkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 14)
)
_PortTrunkTable_Object = MibTable
portTrunkTable = _PortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 14, 1)
)
if mibBuilder.loadTexts:
    portTrunkTable.setStatus("mandatory")
_PortTrunkEntry_Object = MibTableRow
portTrunkEntry = _PortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 14, 1, 1)
)
portTrunkEntry.setIndexNames(
    (0, "DES-1526-MIB", "portTrunkId"),
    (0, "DES-1526-MIB", "portTrunkMember"),
)
if mibBuilder.loadTexts:
    portTrunkEntry.setStatus("mandatory")
_PortTrunkId_Type = Integer32
_PortTrunkId_Object = MibTableColumn
portTrunkId = _PortTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 14, 1, 1, 1),
    _PortTrunkId_Type()
)
portTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkId.setStatus("mandatory")
_PortTrunkMember_Type = PortList
_PortTrunkMember_Object = MibTableColumn
portTrunkMember = _PortTrunkMember_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 14, 1, 1, 2),
    _PortTrunkMember_Type()
)
portTrunkMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkMember.setStatus("mandatory")
_PortTrunkMemberValue_Type = PortList
_PortTrunkMemberValue_Object = MibTableColumn
portTrunkMemberValue = _PortTrunkMemberValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 14, 1, 1, 3),
    _PortTrunkMemberValue_Type()
)
portTrunkMemberValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkMemberValue.setStatus("mandatory")


class _PortTrunkEnable_Type(Integer32):
    """Custom type portTrunkEnable based on Integer32"""
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


_PortTrunkEnable_Type.__name__ = "Integer32"
_PortTrunkEnable_Object = MibTableColumn
portTrunkEnable = _PortTrunkEnable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 14, 1, 1, 4),
    _PortTrunkEnable_Type()
)
portTrunkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portTrunkEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects

swFiberInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 0, 1)
)
if mibBuilder.loadTexts:
    swFiberInsert.setStatus(
        ""
    )

swFiberRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 0, 2)
)
if mibBuilder.loadTexts:
    swFiberRemove.setStatus(
        ""
    )

swFiberAbnormalRXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 0, 3)
)
if mibBuilder.loadTexts:
    swFiberAbnormalRXError.setStatus(
        ""
    )

swFiberAbnormalTXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 0, 4)
)
if mibBuilder.loadTexts:
    swFiberAbnormalTXError.setStatus(
        ""
    )

swTPAbnormalRXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 0, 5)
)
if mibBuilder.loadTexts:
    swTPAbnormalRXError.setStatus(
        ""
    )

swTPAbnormalTXError = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 60, 1, 0, 6)
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
    "DES-1526-MIB",
    **{"OwnerString": OwnerString,
       "MacAddress": MacAddress,
       "PortList": PortList,
       "RowStatus": RowStatus,
       "d-link": d_link,
       "dlink-products": dlink_products,
       "dlink-DES1526SeriesProd": dlink_DES1526SeriesProd,
       "DES-1526": DES_1526,
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
       "commTrapVlanId": commTrapVlanId,
       "commTrapSNMPBootup": commTrapSNMPBootup,
       "commTrapSNMPTPLinkUpDown": commTrapSNMPTPLinkUpDown,
       "commTrapSNMPFiberLinkUpDown": commTrapSNMPFiberLinkUpDown,
       "commTrapTrapAbnormalTPRXError": commTrapTrapAbnormalTPRXError,
       "commTrapTrapAbnormalTPTXError": commTrapTrapAbnormalTPTXError,
       "commTrapTrapAbnormalFiberRXError": commTrapTrapAbnormalFiberRXError,
       "commTrapTrapAbnormalFiberTXError": commTrapTrapAbnormalFiberTXError,
       "commTrapTrapPOEPowerFail": commTrapTrapPOEPowerFail,
       "commTrapTrapPOEPortOvercurrent": commTrapTrapPOEPortOvercurrent,
       "commTrapTrapPOEPortShort": commTrapTrapPOEPortShort,
       "commTrapStatus": commTrapStatus,
       "companyMiscGroup": companyMiscGroup,
       "miscStatisticsReset": miscStatisticsReset,
       "companyConfigGroup": companyConfigGroup,
       "configVerSwPrimary": configVerSwPrimary,
       "configVerHwChipSet": configVerHwChipSet,
       "configPortTable": configPortTable,
       "configPortEntry": configPortEntry,
       "configPort": configPort,
       "configPortSpeed": configPortSpeed,
       "configPortOperStatus": configPortOperStatus,
       "configPortFlowControl": configPortFlowControl,
       "configPortFlowControlOper": configPortFlowControlOper,
       "configPortPriority": configPortPriority,
       "configMirrorTable": configMirrorTable,
       "configMirrorEntry": configMirrorEntry,
       "configMirrorId": configMirrorId,
       "configMirrorMode": configMirrorMode,
       "configMirrorMon": configMirrorMon,
       "configMirrorSrc": configMirrorSrc,
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
       "companyTVlanGroup": companyTVlanGroup,
       "tvlanTable": tvlanTable,
       "tvlanEntry": tvlanEntry,
       "tvlanId": tvlanId,
       "tvlanMember": tvlanMember,
       "tvlanUntaggedPorts": tvlanUntaggedPorts,
       "tvlanStatus": tvlanStatus,
       "tvlanPortTable": tvlanPortTable,
       "tvlanPortEntry": tvlanPortEntry,
       "tvlanPortPortId": tvlanPortPortId,
       "tvlanPortVlanId": tvlanPortVlanId,
       "companyPortTrunkGroup": companyPortTrunkGroup,
       "portTrunkTable": portTrunkTable,
       "portTrunkEntry": portTrunkEntry,
       "portTrunkId": portTrunkId,
       "portTrunkMember": portTrunkMember,
       "portTrunkMemberValue": portTrunkMemberValue,
       "portTrunkEnable": portTrunkEnable}
)
