# SNMP MIB module (Unisphere-Data-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:16 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27)
)
usdPolicyMIB.setRevisions(
        ("2002-03-28 14:53",
         "2001-09-07 14:48",
         "2001-04-17 12:10",
         "2001-01-23 21:30",
         "2000-11-29 20:30",
         "2000-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdClaclPortOperator(Integer32, TextualConvention):
    status = "current"
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
        *(("eq", 3),
          ("gt", 2),
          ("lt", 1),
          ("ne", 4),
          ("noOperator", 0),
          ("range", 5))
    )



class UsdPolicyAttachmentType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inputPolicy", 1),
          ("localInputPolicy", 3),
          ("outputPolicy", 2))
    )



class UsdPolicyForwardingType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbfForwarding", 2),
          ("ipForwarding", 1))
    )



class UsdPolicyIpFragValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("equalToOne", 1),
          ("equalToZero", 0),
          ("greaterThenOne", 3),
          ("notSpecified", 4),
          ("reserved1", 2))
    )



class UsdRateLimitProfileType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneRate", 1),
          ("twoRate", 2))
    )



# MIB Managed Objects in the order of their OIDs

_UsdPolicyObjects_ObjectIdentity = ObjectIdentity
usdPolicyObjects = _UsdPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1)
)
_UsdClassifierControlList_ObjectIdentity = ObjectIdentity
usdClassifierControlList = _UsdClassifierControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1)
)


class _UsdClassifierControlListNextIndex_Type(Integer32):
    """Custom type usdClassifierControlListNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdClassifierControlListNextIndex_Type.__name__ = "Integer32"
_UsdClassifierControlListNextIndex_Object = MibScalar
usdClassifierControlListNextIndex = _UsdClassifierControlListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 1),
    _UsdClassifierControlListNextIndex_Type()
)
usdClassifierControlListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdClassifierControlListNextIndex.setStatus("current")
_UsdClassifierControlListTable_Object = MibTable
usdClassifierControlListTable = _UsdClassifierControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdClassifierControlListTable.setStatus("current")
_UsdClassifierControlListEntry_Object = MibTableRow
usdClassifierControlListEntry = _UsdClassifierControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1)
)
usdClassifierControlListEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdClassifierControlListId"),
)
if mibBuilder.loadTexts:
    usdClassifierControlListEntry.setStatus("current")


class _UsdClassifierControlListId_Type(Integer32):
    """Custom type usdClassifierControlListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdClassifierControlListId_Type.__name__ = "Integer32"
_UsdClassifierControlListId_Object = MibTableColumn
usdClassifierControlListId = _UsdClassifierControlListId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 1),
    _UsdClassifierControlListId_Type()
)
usdClassifierControlListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdClassifierControlListId.setStatus("current")
_UsdClassifierControlListRowStatus_Type = RowStatus
_UsdClassifierControlListRowStatus_Object = MibTableColumn
usdClassifierControlListRowStatus = _UsdClassifierControlListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 3),
    _UsdClassifierControlListRowStatus_Type()
)
usdClassifierControlListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListRowStatus.setStatus("current")


class _UsdClassifierControlListName_Type(DisplayString):
    """Custom type usdClassifierControlListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_UsdClassifierControlListName_Type.__name__ = "DisplayString"
_UsdClassifierControlListName_Object = MibTableColumn
usdClassifierControlListName = _UsdClassifierControlListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 4),
    _UsdClassifierControlListName_Type()
)
usdClassifierControlListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListName.setStatus("current")
_UsdClassifierControlListReferenceCount_Type = Counter32
_UsdClassifierControlListReferenceCount_Object = MibTableColumn
usdClassifierControlListReferenceCount = _UsdClassifierControlListReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 5),
    _UsdClassifierControlListReferenceCount_Type()
)
usdClassifierControlListReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdClassifierControlListReferenceCount.setStatus("current")


class _UsdClassifierControlListNextElementIndex_Type(Integer32):
    """Custom type usdClassifierControlListNextElementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdClassifierControlListNextElementIndex_Type.__name__ = "Integer32"
_UsdClassifierControlListNextElementIndex_Object = MibTableColumn
usdClassifierControlListNextElementIndex = _UsdClassifierControlListNextElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 6),
    _UsdClassifierControlListNextElementIndex_Type()
)
usdClassifierControlListNextElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdClassifierControlListNextElementIndex.setStatus("current")
_UsdClassifierControlListElementTable_Object = MibTable
usdClassifierControlListElementTable = _UsdClassifierControlListElementTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    usdClassifierControlListElementTable.setStatus("current")
_UsdClassifierControlListElementEntry_Object = MibTableRow
usdClassifierControlListElementEntry = _UsdClassifierControlListElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1)
)
usdClassifierControlListElementEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdClassifierControlListId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdClassifierControlListElemId"),
)
if mibBuilder.loadTexts:
    usdClassifierControlListElementEntry.setStatus("current")


class _UsdClassifierControlListElemId_Type(Integer32):
    """Custom type usdClassifierControlListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdClassifierControlListElemId_Type.__name__ = "Integer32"
_UsdClassifierControlListElemId_Object = MibTableColumn
usdClassifierControlListElemId = _UsdClassifierControlListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 1),
    _UsdClassifierControlListElemId_Type()
)
usdClassifierControlListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdClassifierControlListElemId.setStatus("current")
_UsdClassifierControlListElemRowStatus_Type = RowStatus
_UsdClassifierControlListElemRowStatus_Object = MibTableColumn
usdClassifierControlListElemRowStatus = _UsdClassifierControlListElemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 2),
    _UsdClassifierControlListElemRowStatus_Type()
)
usdClassifierControlListElemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListElemRowStatus.setStatus("current")


class _UsdClassifierControlListNotSrc_Type(TruthValue):
    """Custom type usdClassifierControlListNotSrc based on TruthValue"""


_UsdClassifierControlListNotSrc_Object = MibTableColumn
usdClassifierControlListNotSrc = _UsdClassifierControlListNotSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 3),
    _UsdClassifierControlListNotSrc_Type()
)
usdClassifierControlListNotSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListNotSrc.setStatus("current")


class _UsdClassifierControlListSrc_Type(IpAddress):
    """Custom type usdClassifierControlListSrc based on IpAddress"""
    defaultHexValue = "00000000"


_UsdClassifierControlListSrc_Object = MibTableColumn
usdClassifierControlListSrc = _UsdClassifierControlListSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 4),
    _UsdClassifierControlListSrc_Type()
)
usdClassifierControlListSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListSrc.setStatus("current")


class _UsdClassifierControlListSrcMask_Type(IpAddress):
    """Custom type usdClassifierControlListSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_UsdClassifierControlListSrcMask_Object = MibTableColumn
usdClassifierControlListSrcMask = _UsdClassifierControlListSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 5),
    _UsdClassifierControlListSrcMask_Type()
)
usdClassifierControlListSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListSrcMask.setStatus("current")


class _UsdClassifierControlListNotDst_Type(TruthValue):
    """Custom type usdClassifierControlListNotDst based on TruthValue"""


_UsdClassifierControlListNotDst_Object = MibTableColumn
usdClassifierControlListNotDst = _UsdClassifierControlListNotDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 6),
    _UsdClassifierControlListNotDst_Type()
)
usdClassifierControlListNotDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListNotDst.setStatus("current")


class _UsdClassifierControlListDst_Type(IpAddress):
    """Custom type usdClassifierControlListDst based on IpAddress"""
    defaultHexValue = "00000000"


_UsdClassifierControlListDst_Object = MibTableColumn
usdClassifierControlListDst = _UsdClassifierControlListDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 7),
    _UsdClassifierControlListDst_Type()
)
usdClassifierControlListDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListDst.setStatus("current")


class _UsdClassifierControlListDstMask_Type(IpAddress):
    """Custom type usdClassifierControlListDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_UsdClassifierControlListDstMask_Object = MibTableColumn
usdClassifierControlListDstMask = _UsdClassifierControlListDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 8),
    _UsdClassifierControlListDstMask_Type()
)
usdClassifierControlListDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListDstMask.setStatus("current")


class _UsdClassifierControlListNotProtocol_Type(TruthValue):
    """Custom type usdClassifierControlListNotProtocol based on TruthValue"""


_UsdClassifierControlListNotProtocol_Object = MibTableColumn
usdClassifierControlListNotProtocol = _UsdClassifierControlListNotProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 9),
    _UsdClassifierControlListNotProtocol_Type()
)
usdClassifierControlListNotProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListNotProtocol.setStatus("current")


class _UsdClassifierControlListProtocol_Type(Integer32):
    """Custom type usdClassifierControlListProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdClassifierControlListProtocol_Type.__name__ = "Integer32"
_UsdClassifierControlListProtocol_Object = MibTableColumn
usdClassifierControlListProtocol = _UsdClassifierControlListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 10),
    _UsdClassifierControlListProtocol_Type()
)
usdClassifierControlListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListProtocol.setStatus("current")


class _UsdClassifierControlListTosByte_Type(Integer32):
    """Custom type usdClassifierControlListTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdClassifierControlListTosByte_Type.__name__ = "Integer32"
_UsdClassifierControlListTosByte_Object = MibTableColumn
usdClassifierControlListTosByte = _UsdClassifierControlListTosByte_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 11),
    _UsdClassifierControlListTosByte_Type()
)
usdClassifierControlListTosByte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListTosByte.setStatus("current")


class _UsdClassifierControlListMask_Type(Integer32):
    """Custom type usdClassifierControlListMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdClassifierControlListMask_Type.__name__ = "Integer32"
_UsdClassifierControlListMask_Object = MibTableColumn
usdClassifierControlListMask = _UsdClassifierControlListMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 12),
    _UsdClassifierControlListMask_Type()
)
usdClassifierControlListMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListMask.setStatus("current")


class _UsdClassifierControlListSrcOperator_Type(UsdClaclPortOperator):
    """Custom type usdClassifierControlListSrcOperator based on UsdClaclPortOperator"""


_UsdClassifierControlListSrcOperator_Object = MibTableColumn
usdClassifierControlListSrcOperator = _UsdClassifierControlListSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 13),
    _UsdClassifierControlListSrcOperator_Type()
)
usdClassifierControlListSrcOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListSrcOperator.setStatus("current")


class _UsdClassifierControlListSrcFromPort_Type(Integer32):
    """Custom type usdClassifierControlListSrcFromPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdClassifierControlListSrcFromPort_Type.__name__ = "Integer32"
_UsdClassifierControlListSrcFromPort_Object = MibTableColumn
usdClassifierControlListSrcFromPort = _UsdClassifierControlListSrcFromPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 14),
    _UsdClassifierControlListSrcFromPort_Type()
)
usdClassifierControlListSrcFromPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListSrcFromPort.setStatus("current")


class _UsdClassifierControlListSrcToPort_Type(Integer32):
    """Custom type usdClassifierControlListSrcToPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdClassifierControlListSrcToPort_Type.__name__ = "Integer32"
_UsdClassifierControlListSrcToPort_Object = MibTableColumn
usdClassifierControlListSrcToPort = _UsdClassifierControlListSrcToPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 15),
    _UsdClassifierControlListSrcToPort_Type()
)
usdClassifierControlListSrcToPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListSrcToPort.setStatus("current")


class _UsdClassifierControlListDestOperator_Type(UsdClaclPortOperator):
    """Custom type usdClassifierControlListDestOperator based on UsdClaclPortOperator"""


_UsdClassifierControlListDestOperator_Object = MibTableColumn
usdClassifierControlListDestOperator = _UsdClassifierControlListDestOperator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 16),
    _UsdClassifierControlListDestOperator_Type()
)
usdClassifierControlListDestOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListDestOperator.setStatus("current")


class _UsdClassifierControlListDestFromPort_Type(Integer32):
    """Custom type usdClassifierControlListDestFromPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdClassifierControlListDestFromPort_Type.__name__ = "Integer32"
_UsdClassifierControlListDestFromPort_Object = MibTableColumn
usdClassifierControlListDestFromPort = _UsdClassifierControlListDestFromPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 17),
    _UsdClassifierControlListDestFromPort_Type()
)
usdClassifierControlListDestFromPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListDestFromPort.setStatus("current")


class _UsdClassifierControlListDestToPort_Type(Integer32):
    """Custom type usdClassifierControlListDestToPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdClassifierControlListDestToPort_Type.__name__ = "Integer32"
_UsdClassifierControlListDestToPort_Object = MibTableColumn
usdClassifierControlListDestToPort = _UsdClassifierControlListDestToPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 18),
    _UsdClassifierControlListDestToPort_Type()
)
usdClassifierControlListDestToPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListDestToPort.setStatus("current")


class _UsdClassifierControlListICMPType_Type(Integer32):
    """Custom type usdClassifierControlListICMPType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdClassifierControlListICMPType_Type.__name__ = "Integer32"
_UsdClassifierControlListICMPType_Object = MibTableColumn
usdClassifierControlListICMPType = _UsdClassifierControlListICMPType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 19),
    _UsdClassifierControlListICMPType_Type()
)
usdClassifierControlListICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListICMPType.setStatus("current")


class _UsdClassifierControlListICMPCode_Type(Integer32):
    """Custom type usdClassifierControlListICMPCode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdClassifierControlListICMPCode_Type.__name__ = "Integer32"
_UsdClassifierControlListICMPCode_Object = MibTableColumn
usdClassifierControlListICMPCode = _UsdClassifierControlListICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 20),
    _UsdClassifierControlListICMPCode_Type()
)
usdClassifierControlListICMPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListICMPCode.setStatus("current")


class _UsdClassifierControlListIGMPType_Type(Integer32):
    """Custom type usdClassifierControlListIGMPType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdClassifierControlListIGMPType_Type.__name__ = "Integer32"
_UsdClassifierControlListIGMPType_Object = MibTableColumn
usdClassifierControlListIGMPType = _UsdClassifierControlListIGMPType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 21),
    _UsdClassifierControlListIGMPType_Type()
)
usdClassifierControlListIGMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListIGMPType.setStatus("current")


class _UsdClassifierControlListTcpFlagsValue_Type(Integer32):
    """Custom type usdClassifierControlListTcpFlagsValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_UsdClassifierControlListTcpFlagsValue_Type.__name__ = "Integer32"
_UsdClassifierControlListTcpFlagsValue_Object = MibTableColumn
usdClassifierControlListTcpFlagsValue = _UsdClassifierControlListTcpFlagsValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 22),
    _UsdClassifierControlListTcpFlagsValue_Type()
)
usdClassifierControlListTcpFlagsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListTcpFlagsValue.setStatus("current")


class _UsdClassifierControlListTcpFlagsMask_Type(Integer32):
    """Custom type usdClassifierControlListTcpFlagsMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_UsdClassifierControlListTcpFlagsMask_Type.__name__ = "Integer32"
_UsdClassifierControlListTcpFlagsMask_Object = MibTableColumn
usdClassifierControlListTcpFlagsMask = _UsdClassifierControlListTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 23),
    _UsdClassifierControlListTcpFlagsMask_Type()
)
usdClassifierControlListTcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListTcpFlagsMask.setStatus("current")


class _UsdClassifierControlListIpFlagsValue_Type(Integer32):
    """Custom type usdClassifierControlListIpFlagsValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UsdClassifierControlListIpFlagsValue_Type.__name__ = "Integer32"
_UsdClassifierControlListIpFlagsValue_Object = MibTableColumn
usdClassifierControlListIpFlagsValue = _UsdClassifierControlListIpFlagsValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 24),
    _UsdClassifierControlListIpFlagsValue_Type()
)
usdClassifierControlListIpFlagsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListIpFlagsValue.setStatus("current")


class _UsdClassifierControlListIpFlagsMask_Type(Integer32):
    """Custom type usdClassifierControlListIpFlagsMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UsdClassifierControlListIpFlagsMask_Type.__name__ = "Integer32"
_UsdClassifierControlListIpFlagsMask_Object = MibTableColumn
usdClassifierControlListIpFlagsMask = _UsdClassifierControlListIpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 25),
    _UsdClassifierControlListIpFlagsMask_Type()
)
usdClassifierControlListIpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListIpFlagsMask.setStatus("current")


class _UsdClassifierControlListIpFragValue_Type(UsdPolicyIpFragValue):
    """Custom type usdClassifierControlListIpFragValue based on UsdPolicyIpFragValue"""


_UsdClassifierControlListIpFragValue_Object = MibTableColumn
usdClassifierControlListIpFragValue = _UsdClassifierControlListIpFragValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 26),
    _UsdClassifierControlListIpFragValue_Type()
)
usdClassifierControlListIpFragValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdClassifierControlListIpFragValue.setStatus("current")
_UsdRateLimitControlList_ObjectIdentity = ObjectIdentity
usdRateLimitControlList = _UsdRateLimitControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2)
)


class _UsdRateLimitProfileNextIndex_Type(Integer32):
    """Custom type usdRateLimitProfileNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdRateLimitProfileNextIndex_Type.__name__ = "Integer32"
_UsdRateLimitProfileNextIndex_Object = MibScalar
usdRateLimitProfileNextIndex = _UsdRateLimitProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 1),
    _UsdRateLimitProfileNextIndex_Type()
)
usdRateLimitProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRateLimitProfileNextIndex.setStatus("current")
_UsdRateLimitProfileTable_Object = MibTable
usdRateLimitProfileTable = _UsdRateLimitProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    usdRateLimitProfileTable.setStatus("current")
_UsdRateLimitProfileEntry_Object = MibTableRow
usdRateLimitProfileEntry = _UsdRateLimitProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1)
)
usdRateLimitProfileEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdRateLimitProfileId"),
)
if mibBuilder.loadTexts:
    usdRateLimitProfileEntry.setStatus("current")


class _UsdRateLimitProfileId_Type(Integer32):
    """Custom type usdRateLimitProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdRateLimitProfileId_Type.__name__ = "Integer32"
_UsdRateLimitProfileId_Object = MibTableColumn
usdRateLimitProfileId = _UsdRateLimitProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 1),
    _UsdRateLimitProfileId_Type()
)
usdRateLimitProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRateLimitProfileId.setStatus("current")
_UsdRateLimitProfileRowStatus_Type = RowStatus
_UsdRateLimitProfileRowStatus_Object = MibTableColumn
usdRateLimitProfileRowStatus = _UsdRateLimitProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 2),
    _UsdRateLimitProfileRowStatus_Type()
)
usdRateLimitProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitProfileRowStatus.setStatus("current")


class _UsdRateLimitProfileName_Type(DisplayString):
    """Custom type usdRateLimitProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_UsdRateLimitProfileName_Type.__name__ = "DisplayString"
_UsdRateLimitProfileName_Object = MibTableColumn
usdRateLimitProfileName = _UsdRateLimitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 3),
    _UsdRateLimitProfileName_Type()
)
usdRateLimitProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitProfileName.setStatus("current")
_UsdRateLimitReferenceCount_Type = Counter32
_UsdRateLimitReferenceCount_Object = MibTableColumn
usdRateLimitReferenceCount = _UsdRateLimitReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 4),
    _UsdRateLimitReferenceCount_Type()
)
usdRateLimitReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRateLimitReferenceCount.setStatus("current")


class _UsdRateLimitCommittedBps_Type(Unsigned32):
    """Custom type usdRateLimitCommittedBps based on Unsigned32"""
    defaultValue = 0


_UsdRateLimitCommittedBps_Object = MibTableColumn
usdRateLimitCommittedBps = _UsdRateLimitCommittedBps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 5),
    _UsdRateLimitCommittedBps_Type()
)
usdRateLimitCommittedBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitCommittedBps.setStatus("current")
if mibBuilder.loadTexts:
    usdRateLimitCommittedBps.setUnits("bits per second")


class _UsdRateLimitCommittedBurst_Type(Unsigned32):
    """Custom type usdRateLimitCommittedBurst based on Unsigned32"""
    defaultValue = 8192


_UsdRateLimitCommittedBurst_Object = MibTableColumn
usdRateLimitCommittedBurst = _UsdRateLimitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 6),
    _UsdRateLimitCommittedBurst_Type()
)
usdRateLimitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitCommittedBurst.setStatus("current")
if mibBuilder.loadTexts:
    usdRateLimitCommittedBurst.setUnits("bytes")


class _UsdRateLimitExceedBps_Type(Unsigned32):
    """Custom type usdRateLimitExceedBps based on Unsigned32"""
    defaultValue = 0


_UsdRateLimitExceedBps_Object = MibTableColumn
usdRateLimitExceedBps = _UsdRateLimitExceedBps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 7),
    _UsdRateLimitExceedBps_Type()
)
usdRateLimitExceedBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitExceedBps.setStatus("current")
if mibBuilder.loadTexts:
    usdRateLimitExceedBps.setUnits("bits per second")


class _UsdRateLimitExceedBurst_Type(Unsigned32):
    """Custom type usdRateLimitExceedBurst based on Unsigned32"""
    defaultValue = 8192


_UsdRateLimitExceedBurst_Object = MibTableColumn
usdRateLimitExceedBurst = _UsdRateLimitExceedBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 8),
    _UsdRateLimitExceedBurst_Type()
)
usdRateLimitExceedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitExceedBurst.setStatus("current")
if mibBuilder.loadTexts:
    usdRateLimitExceedBurst.setUnits("bytes")


class _UsdRateLimitCommittedAction_Type(Integer32):
    """Custom type usdRateLimitCommittedAction based on Integer32"""
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
        *(("drop", 1),
          ("mark", 2),
          ("transmit", 0))
    )


_UsdRateLimitCommittedAction_Type.__name__ = "Integer32"
_UsdRateLimitCommittedAction_Object = MibTableColumn
usdRateLimitCommittedAction = _UsdRateLimitCommittedAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 9),
    _UsdRateLimitCommittedAction_Type()
)
usdRateLimitCommittedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitCommittedAction.setStatus("current")


class _UsdRateLimitConformedAction_Type(Integer32):
    """Custom type usdRateLimitConformedAction based on Integer32"""
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
        *(("drop", 1),
          ("mark", 2),
          ("transmit", 0))
    )


_UsdRateLimitConformedAction_Type.__name__ = "Integer32"
_UsdRateLimitConformedAction_Object = MibTableColumn
usdRateLimitConformedAction = _UsdRateLimitConformedAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 10),
    _UsdRateLimitConformedAction_Type()
)
usdRateLimitConformedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitConformedAction.setStatus("current")


class _UsdRateLimitExceededAction_Type(Integer32):
    """Custom type usdRateLimitExceededAction based on Integer32"""
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
        *(("drop", 1),
          ("mark", 2),
          ("transmit", 0))
    )


_UsdRateLimitExceededAction_Type.__name__ = "Integer32"
_UsdRateLimitExceededAction_Object = MibTableColumn
usdRateLimitExceededAction = _UsdRateLimitExceededAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 11),
    _UsdRateLimitExceededAction_Type()
)
usdRateLimitExceededAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitExceededAction.setStatus("current")


class _UsdRateLimitCommittedMarkVal_Type(Integer32):
    """Custom type usdRateLimitCommittedMarkVal based on Integer32"""
    defaultValue = 0


_UsdRateLimitCommittedMarkVal_Object = MibTableColumn
usdRateLimitCommittedMarkVal = _UsdRateLimitCommittedMarkVal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 12),
    _UsdRateLimitCommittedMarkVal_Type()
)
usdRateLimitCommittedMarkVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitCommittedMarkVal.setStatus("current")


class _UsdRateLimitConformedMarkVal_Type(Integer32):
    """Custom type usdRateLimitConformedMarkVal based on Integer32"""
    defaultValue = 0


_UsdRateLimitConformedMarkVal_Object = MibTableColumn
usdRateLimitConformedMarkVal = _UsdRateLimitConformedMarkVal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 13),
    _UsdRateLimitConformedMarkVal_Type()
)
usdRateLimitConformedMarkVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitConformedMarkVal.setStatus("current")


class _UsdRateLimitExceededMarkVal_Type(Integer32):
    """Custom type usdRateLimitExceededMarkVal based on Integer32"""
    defaultValue = 0


_UsdRateLimitExceededMarkVal_Object = MibTableColumn
usdRateLimitExceededMarkVal = _UsdRateLimitExceededMarkVal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 14),
    _UsdRateLimitExceededMarkVal_Type()
)
usdRateLimitExceededMarkVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitExceededMarkVal.setStatus("current")


class _UsdRateLimitMask_Type(Unsigned32):
    """Custom type usdRateLimitMask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdRateLimitMask_Type.__name__ = "Unsigned32"
_UsdRateLimitMask_Object = MibTableColumn
usdRateLimitMask = _UsdRateLimitMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 15),
    _UsdRateLimitMask_Type()
)
usdRateLimitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitMask.setStatus("current")


class _UsdRateLimitProfileType_Type(UsdRateLimitProfileType):
    """Custom type usdRateLimitProfileType based on UsdRateLimitProfileType"""


_UsdRateLimitProfileType_Object = MibTableColumn
usdRateLimitProfileType = _UsdRateLimitProfileType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 16),
    _UsdRateLimitProfileType_Type()
)
usdRateLimitProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitProfileType.setStatus("current")


class _UsdRateLimitExcessBurst_Type(Unsigned32):
    """Custom type usdRateLimitExcessBurst based on Unsigned32"""
    defaultValue = 0


_UsdRateLimitExcessBurst_Object = MibTableColumn
usdRateLimitExcessBurst = _UsdRateLimitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 17),
    _UsdRateLimitExcessBurst_Type()
)
usdRateLimitExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRateLimitExcessBurst.setStatus("current")
if mibBuilder.loadTexts:
    usdRateLimitExcessBurst.setUnits("bytes")
_UsdPolicy_ObjectIdentity = ObjectIdentity
usdPolicy = _UsdPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3)
)


class _UsdPolicyNextIndex_Type(Integer32):
    """Custom type usdPolicyNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyNextIndex_Type.__name__ = "Integer32"
_UsdPolicyNextIndex_Object = MibScalar
usdPolicyNextIndex = _UsdPolicyNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 1),
    _UsdPolicyNextIndex_Type()
)
usdPolicyNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyNextIndex.setStatus("current")
_UsdPolicyTable_Object = MibTable
usdPolicyTable = _UsdPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdPolicyTable.setStatus("current")
_UsdPolicyEntry_Object = MibTableRow
usdPolicyEntry = _UsdPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1)
)
usdPolicyEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyId"),
)
if mibBuilder.loadTexts:
    usdPolicyEntry.setStatus("current")


class _UsdPolicyId_Type(Integer32):
    """Custom type usdPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyId_Type.__name__ = "Integer32"
_UsdPolicyId_Object = MibTableColumn
usdPolicyId = _UsdPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 1),
    _UsdPolicyId_Type()
)
usdPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyId.setStatus("current")
_UsdPolicyRowStatus_Type = RowStatus
_UsdPolicyRowStatus_Object = MibTableColumn
usdPolicyRowStatus = _UsdPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 2),
    _UsdPolicyRowStatus_Type()
)
usdPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyRowStatus.setStatus("current")


class _UsdPolicyAdminState_Type(Integer32):
    """Custom type usdPolicyAdminState based on Integer32"""
    defaultValue = 0

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


_UsdPolicyAdminState_Type.__name__ = "Integer32"
_UsdPolicyAdminState_Object = MibTableColumn
usdPolicyAdminState = _UsdPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 3),
    _UsdPolicyAdminState_Type()
)
usdPolicyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyAdminState.setStatus("current")


class _UsdPolicyOperStatus_Type(Integer32):
    """Custom type usdPolicyOperStatus based on Integer32"""
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
          ("enabled", 2),
          ("invalid", 1))
    )


_UsdPolicyOperStatus_Type.__name__ = "Integer32"
_UsdPolicyOperStatus_Object = MibTableColumn
usdPolicyOperStatus = _UsdPolicyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 4),
    _UsdPolicyOperStatus_Type()
)
usdPolicyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyOperStatus.setStatus("current")
_UsdPolicyErrorValue_Type = Integer32
_UsdPolicyErrorValue_Object = MibTableColumn
usdPolicyErrorValue = _UsdPolicyErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 5),
    _UsdPolicyErrorValue_Type()
)
usdPolicyErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyErrorValue.setStatus("current")


class _UsdPolicyName_Type(DisplayString):
    """Custom type usdPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_UsdPolicyName_Type.__name__ = "DisplayString"
_UsdPolicyName_Object = MibTableColumn
usdPolicyName = _UsdPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 6),
    _UsdPolicyName_Type()
)
usdPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyName.setStatus("current")
_UsdPolicyReferenceCount_Type = Counter32
_UsdPolicyReferenceCount_Object = MibTableColumn
usdPolicyReferenceCount = _UsdPolicyReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 7),
    _UsdPolicyReferenceCount_Type()
)
usdPolicyReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyReferenceCount.setStatus("current")


class _UsdPolicyRuleNextIndex_Type(Integer32):
    """Custom type usdPolicyRuleNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyRuleNextIndex_Type.__name__ = "Integer32"
_UsdPolicyRuleNextIndex_Object = MibTableColumn
usdPolicyRuleNextIndex = _UsdPolicyRuleNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 8),
    _UsdPolicyRuleNextIndex_Type()
)
usdPolicyRuleNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyRuleNextIndex.setStatus("current")
_UsdPolicyRuleTable_Object = MibTable
usdPolicyRuleTable = _UsdPolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3)
)
if mibBuilder.loadTexts:
    usdPolicyRuleTable.setStatus("current")
_UsdPolicyRuleEntry_Object = MibTableRow
usdPolicyRuleEntry = _UsdPolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1)
)
usdPolicyRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdPolicyRuleEntry.setStatus("current")


class _UsdPolicyRulePolicyId_Type(Integer32):
    """Custom type usdPolicyRulePolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyRulePolicyId_Type.__name__ = "Integer32"
_UsdPolicyRulePolicyId_Object = MibTableColumn
usdPolicyRulePolicyId = _UsdPolicyRulePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 1),
    _UsdPolicyRulePolicyId_Type()
)
usdPolicyRulePolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyRulePolicyId.setStatus("current")


class _UsdPolicyRulePrec_Type(Integer32):
    """Custom type usdPolicyRulePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyRulePrec_Type.__name__ = "Integer32"
_UsdPolicyRulePrec_Object = MibTableColumn
usdPolicyRulePrec = _UsdPolicyRulePrec_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 2),
    _UsdPolicyRulePrec_Type()
)
usdPolicyRulePrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyRulePrec.setStatus("current")


class _UsdPolicyRuleId_Type(Integer32):
    """Custom type usdPolicyRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyRuleId_Type.__name__ = "Integer32"
_UsdPolicyRuleId_Object = MibTableColumn
usdPolicyRuleId = _UsdPolicyRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 3),
    _UsdPolicyRuleId_Type()
)
usdPolicyRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyRuleId.setStatus("current")


class _UsdPolicyRuleType_Type(Integer32):
    """Custom type usdPolicyRuleType based on Integer32"""
    defaultValue = 0

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("colorRule", 10),
          ("filterRule", 2),
          ("forwardRule", 7),
          ("logRule", 8),
          ("markingRule", 5),
          ("nextHopRule", 1),
          ("nextInterfaceRule", 3),
          ("noRule", 0),
          ("rateLimitRule", 4),
          ("trafficClassRule", 6))
    )


_UsdPolicyRuleType_Type.__name__ = "Integer32"
_UsdPolicyRuleType_Object = MibTableColumn
usdPolicyRuleType = _UsdPolicyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 4),
    _UsdPolicyRuleType_Type()
)
usdPolicyRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyRuleType.setStatus("current")


class _UsdPolicySuspend_Type(TruthValue):
    """Custom type usdPolicySuspend based on TruthValue"""


_UsdPolicySuspend_Object = MibTableColumn
usdPolicySuspend = _UsdPolicySuspend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 5),
    _UsdPolicySuspend_Type()
)
usdPolicySuspend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPolicySuspend.setStatus("current")
_UsdPolicyEclipsed_Type = TruthValue
_UsdPolicyEclipsed_Object = MibTableColumn
usdPolicyEclipsed = _UsdPolicyEclipsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 6),
    _UsdPolicyEclipsed_Type()
)
usdPolicyEclipsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyEclipsed.setStatus("current")
_UsdNextHopRuleTable_Object = MibTable
usdNextHopRuleTable = _UsdNextHopRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4)
)
if mibBuilder.loadTexts:
    usdNextHopRuleTable.setStatus("current")
_UsdNextHopRuleEntry_Object = MibTableRow
usdNextHopRuleEntry = _UsdNextHopRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1)
)
usdNextHopRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdNextHopRuleEntry.setStatus("current")
_UsdNextHopRowStatus_Type = RowStatus
_UsdNextHopRowStatus_Object = MibTableColumn
usdNextHopRowStatus = _UsdNextHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1, 1),
    _UsdNextHopRowStatus_Type()
)
usdNextHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNextHopRowStatus.setStatus("current")


class _UsdNextHopIpAddress_Type(IpAddress):
    """Custom type usdNextHopIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_UsdNextHopIpAddress_Object = MibTableColumn
usdNextHopIpAddress = _UsdNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1, 2),
    _UsdNextHopIpAddress_Type()
)
usdNextHopIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNextHopIpAddress.setStatus("current")


class _UsdNextHopClaclId_Type(Integer32):
    """Custom type usdNextHopClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdNextHopClaclId_Type.__name__ = "Integer32"
_UsdNextHopClaclId_Object = MibTableColumn
usdNextHopClaclId = _UsdNextHopClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1, 3),
    _UsdNextHopClaclId_Type()
)
usdNextHopClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNextHopClaclId.setStatus("current")
_UsdFilterRuleTable_Object = MibTable
usdFilterRuleTable = _UsdFilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5)
)
if mibBuilder.loadTexts:
    usdFilterRuleTable.setStatus("current")
_UsdFilterRuleEntry_Object = MibTableRow
usdFilterRuleEntry = _UsdFilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5, 1)
)
usdFilterRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdFilterRuleEntry.setStatus("current")
_UsdFilterRowStatus_Type = RowStatus
_UsdFilterRowStatus_Object = MibTableColumn
usdFilterRowStatus = _UsdFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5, 1, 1),
    _UsdFilterRowStatus_Type()
)
usdFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFilterRowStatus.setStatus("current")


class _UsdFilterClaclId_Type(Integer32):
    """Custom type usdFilterClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdFilterClaclId_Type.__name__ = "Integer32"
_UsdFilterClaclId_Object = MibTableColumn
usdFilterClaclId = _UsdFilterClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5, 1, 2),
    _UsdFilterClaclId_Type()
)
usdFilterClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdFilterClaclId.setStatus("current")
_UsdNextInterfaceRuleTable_Object = MibTable
usdNextInterfaceRuleTable = _UsdNextInterfaceRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6)
)
if mibBuilder.loadTexts:
    usdNextInterfaceRuleTable.setStatus("current")
_UsdNextInterfaceRuleEntry_Object = MibTableRow
usdNextInterfaceRuleEntry = _UsdNextInterfaceRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1)
)
usdNextInterfaceRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdNextInterfaceRuleEntry.setStatus("current")
_UsdNextInterfaceRowStatus_Type = RowStatus
_UsdNextInterfaceRowStatus_Object = MibTableColumn
usdNextInterfaceRowStatus = _UsdNextInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 1),
    _UsdNextInterfaceRowStatus_Type()
)
usdNextInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNextInterfaceRowStatus.setStatus("current")
_UsdNextInterfaceId_Type = InterfaceIndex
_UsdNextInterfaceId_Object = MibTableColumn
usdNextInterfaceId = _UsdNextInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 2),
    _UsdNextInterfaceId_Type()
)
usdNextInterfaceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNextInterfaceId.setStatus("current")


class _UsdNextInterfaceClaclId_Type(Integer32):
    """Custom type usdNextInterfaceClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdNextInterfaceClaclId_Type.__name__ = "Integer32"
_UsdNextInterfaceClaclId_Object = MibTableColumn
usdNextInterfaceClaclId = _UsdNextInterfaceClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 3),
    _UsdNextInterfaceClaclId_Type()
)
usdNextInterfaceClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNextInterfaceClaclId.setStatus("current")


class _UsdNextInterfaceNextHop_Type(IpAddress):
    """Custom type usdNextInterfaceNextHop based on IpAddress"""
    defaultHexValue = "00000000"


_UsdNextInterfaceNextHop_Object = MibTableColumn
usdNextInterfaceNextHop = _UsdNextInterfaceNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 4),
    _UsdNextInterfaceNextHop_Type()
)
usdNextInterfaceNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdNextInterfaceNextHop.setStatus("current")
_UsdRateLimitRuleTable_Object = MibTable
usdRateLimitRuleTable = _UsdRateLimitRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7)
)
if mibBuilder.loadTexts:
    usdRateLimitRuleTable.setStatus("current")
_UsdRateLimitRuleEntry_Object = MibTableRow
usdRateLimitRuleEntry = _UsdRateLimitRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1)
)
usdRateLimitRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdRateLimitRuleEntry.setStatus("current")
_UsdRateLimitRowStatus_Type = RowStatus
_UsdRateLimitRowStatus_Object = MibTableColumn
usdRateLimitRowStatus = _UsdRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1, 1),
    _UsdRateLimitRowStatus_Type()
)
usdRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRateLimitRowStatus.setStatus("current")


class _UsdRateLimitId_Type(Integer32):
    """Custom type usdRateLimitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdRateLimitId_Type.__name__ = "Integer32"
_UsdRateLimitId_Object = MibTableColumn
usdRateLimitId = _UsdRateLimitId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1, 2),
    _UsdRateLimitId_Type()
)
usdRateLimitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRateLimitId.setStatus("current")


class _UsdRateLimitClaclId_Type(Integer32):
    """Custom type usdRateLimitClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdRateLimitClaclId_Type.__name__ = "Integer32"
_UsdRateLimitClaclId_Object = MibTableColumn
usdRateLimitClaclId = _UsdRateLimitClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1, 3),
    _UsdRateLimitClaclId_Type()
)
usdRateLimitClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRateLimitClaclId.setStatus("current")
_UsdMarkingRuleTable_Object = MibTable
usdMarkingRuleTable = _UsdMarkingRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8)
)
if mibBuilder.loadTexts:
    usdMarkingRuleTable.setStatus("current")
_UsdMarkingRuleEntry_Object = MibTableRow
usdMarkingRuleEntry = _UsdMarkingRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1)
)
usdMarkingRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdMarkingRuleEntry.setStatus("current")
_UsdMarkingRowStatus_Type = RowStatus
_UsdMarkingRowStatus_Object = MibTableColumn
usdMarkingRowStatus = _UsdMarkingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 1),
    _UsdMarkingRowStatus_Type()
)
usdMarkingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMarkingRowStatus.setStatus("current")


class _UsdMarkingTOSByte_Type(Integer32):
    """Custom type usdMarkingTOSByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdMarkingTOSByte_Type.__name__ = "Integer32"
_UsdMarkingTOSByte_Object = MibTableColumn
usdMarkingTOSByte = _UsdMarkingTOSByte_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 2),
    _UsdMarkingTOSByte_Type()
)
usdMarkingTOSByte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMarkingTOSByte.setStatus("current")


class _UsdMarkingMask_Type(Integer32):
    """Custom type usdMarkingMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UsdMarkingMask_Type.__name__ = "Integer32"
_UsdMarkingMask_Object = MibTableColumn
usdMarkingMask = _UsdMarkingMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 3),
    _UsdMarkingMask_Type()
)
usdMarkingMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMarkingMask.setStatus("current")


class _UsdMarkingClaclId_Type(Integer32):
    """Custom type usdMarkingClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdMarkingClaclId_Type.__name__ = "Integer32"
_UsdMarkingClaclId_Object = MibTableColumn
usdMarkingClaclId = _UsdMarkingClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 4),
    _UsdMarkingClaclId_Type()
)
usdMarkingClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdMarkingClaclId.setStatus("current")
_UsdForwardRuleTable_Object = MibTable
usdForwardRuleTable = _UsdForwardRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9)
)
if mibBuilder.loadTexts:
    usdForwardRuleTable.setStatus("current")
_UsdForwardRuleEntry_Object = MibTableRow
usdForwardRuleEntry = _UsdForwardRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1)
)
usdForwardRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdForwardRuleEntry.setStatus("current")
_UsdForwardRowStatus_Type = RowStatus
_UsdForwardRowStatus_Object = MibTableColumn
usdForwardRowStatus = _UsdForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 1),
    _UsdForwardRowStatus_Type()
)
usdForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdForwardRowStatus.setStatus("current")


class _UsdForwardClaclId_Type(Integer32):
    """Custom type usdForwardClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdForwardClaclId_Type.__name__ = "Integer32"
_UsdForwardClaclId_Object = MibTableColumn
usdForwardClaclId = _UsdForwardClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 2),
    _UsdForwardClaclId_Type()
)
usdForwardClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdForwardClaclId.setStatus("current")
_UsdTrafficShapeRuleTable_Object = MibTable
usdTrafficShapeRuleTable = _UsdTrafficShapeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10)
)
if mibBuilder.loadTexts:
    usdTrafficShapeRuleTable.setStatus("obsolete")
_UsdTrafficShapeRuleEntry_Object = MibTableRow
usdTrafficShapeRuleEntry = _UsdTrafficShapeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10, 1)
)
usdTrafficShapeRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdTrafficShapeRuleEntry.setStatus("obsolete")
_UsdTrafficShapeRowStatus_Type = RowStatus
_UsdTrafficShapeRowStatus_Object = MibTableColumn
usdTrafficShapeRowStatus = _UsdTrafficShapeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10, 1, 1),
    _UsdTrafficShapeRowStatus_Type()
)
usdTrafficShapeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficShapeRowStatus.setStatus("obsolete")


class _UsdTrafficShapeId_Type(Integer32):
    """Custom type usdTrafficShapeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdTrafficShapeId_Type.__name__ = "Integer32"
_UsdTrafficShapeId_Object = MibTableColumn
usdTrafficShapeId = _UsdTrafficShapeId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10, 1, 2),
    _UsdTrafficShapeId_Type()
)
usdTrafficShapeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficShapeId.setStatus("obsolete")
_UsdColorRuleTable_Object = MibTable
usdColorRuleTable = _UsdColorRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11)
)
if mibBuilder.loadTexts:
    usdColorRuleTable.setStatus("current")
_UsdColorRuleEntry_Object = MibTableRow
usdColorRuleEntry = _UsdColorRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1)
)
usdColorRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdColorRuleEntry.setStatus("current")
_UsdColorRowStatus_Type = RowStatus
_UsdColorRowStatus_Object = MibTableColumn
usdColorRowStatus = _UsdColorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1, 1),
    _UsdColorRowStatus_Type()
)
usdColorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdColorRowStatus.setStatus("current")


class _UsdColor_Type(Integer32):
    """Custom type usdColor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 3),
          ("red", 1),
          ("yellow", 2))
    )


_UsdColor_Type.__name__ = "Integer32"
_UsdColor_Object = MibTableColumn
usdColor = _UsdColor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1, 2),
    _UsdColor_Type()
)
usdColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdColor.setStatus("current")


class _UsdColorClaclId_Type(Integer32):
    """Custom type usdColorClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdColorClaclId_Type.__name__ = "Integer32"
_UsdColorClaclId_Object = MibTableColumn
usdColorClaclId = _UsdColorClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1, 3),
    _UsdColorClaclId_Type()
)
usdColorClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdColorClaclId.setStatus("current")
_UsdLogRuleTable_Object = MibTable
usdLogRuleTable = _UsdLogRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12)
)
if mibBuilder.loadTexts:
    usdLogRuleTable.setStatus("current")
_UsdLogRuleEntry_Object = MibTableRow
usdLogRuleEntry = _UsdLogRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12, 1)
)
usdLogRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdLogRuleEntry.setStatus("current")
_UsdLogRowStatus_Type = RowStatus
_UsdLogRowStatus_Object = MibTableColumn
usdLogRowStatus = _UsdLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12, 1, 1),
    _UsdLogRowStatus_Type()
)
usdLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdLogRowStatus.setStatus("current")


class _UsdLogClaclId_Type(Integer32):
    """Custom type usdLogClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdLogClaclId_Type.__name__ = "Integer32"
_UsdLogClaclId_Object = MibTableColumn
usdLogClaclId = _UsdLogClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12, 1, 2),
    _UsdLogClaclId_Type()
)
usdLogClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdLogClaclId.setStatus("current")
_UsdTrafficClassRuleTable_Object = MibTable
usdTrafficClassRuleTable = _UsdTrafficClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13)
)
if mibBuilder.loadTexts:
    usdTrafficClassRuleTable.setStatus("current")
_UsdTrafficClassRuleEntry_Object = MibTableRow
usdTrafficClassRuleEntry = _UsdTrafficClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1)
)
usdTrafficClassRuleEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyRuleId"),
)
if mibBuilder.loadTexts:
    usdTrafficClassRuleEntry.setStatus("current")
_UsdTrafficClassRowStatus_Type = RowStatus
_UsdTrafficClassRowStatus_Object = MibTableColumn
usdTrafficClassRowStatus = _UsdTrafficClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1, 1),
    _UsdTrafficClassRowStatus_Type()
)
usdTrafficClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficClassRowStatus.setStatus("current")


class _UsdTrafficClassId_Type(Integer32):
    """Custom type usdTrafficClassId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdTrafficClassId_Type.__name__ = "Integer32"
_UsdTrafficClassId_Object = MibTableColumn
usdTrafficClassId = _UsdTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1, 2),
    _UsdTrafficClassId_Type()
)
usdTrafficClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficClassId.setStatus("current")


class _UsdTrafficClassClaclId_Type(Integer32):
    """Custom type usdTrafficClassClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdTrafficClassClaclId_Type.__name__ = "Integer32"
_UsdTrafficClassClaclId_Object = MibTableColumn
usdTrafficClassClaclId = _UsdTrafficClassClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1, 3),
    _UsdTrafficClassClaclId_Type()
)
usdTrafficClassClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficClassClaclId.setStatus("current")
_UsdPolicyIf_ObjectIdentity = ObjectIdentity
usdPolicyIf = _UsdPolicyIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4)
)
_UsdPolicyIfTable_Object = MibTable
usdPolicyIfTable = _UsdPolicyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1)
)
if mibBuilder.loadTexts:
    usdPolicyIfTable.setStatus("obsolete")
_UsdPolicyIfEntry_Object = MibTableRow
usdPolicyIfEntry = _UsdPolicyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1)
)
usdPolicyIfEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfInterfaceId"),
)
if mibBuilder.loadTexts:
    usdPolicyIfEntry.setStatus("obsolete")
_UsdPolicyIfInterfaceId_Type = Unsigned32
_UsdPolicyIfInterfaceId_Object = MibTableColumn
usdPolicyIfInterfaceId = _UsdPolicyIfInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 1),
    _UsdPolicyIfInterfaceId_Type()
)
usdPolicyIfInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfInterfaceId.setStatus("obsolete")
_UsdPolicyIfRowStatus_Type = RowStatus
_UsdPolicyIfRowStatus_Object = MibTableColumn
usdPolicyIfRowStatus = _UsdPolicyIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 2),
    _UsdPolicyIfRowStatus_Type()
)
usdPolicyIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfRowStatus.setStatus("obsolete")


class _UsdPolicyIfInputPolicyId_Type(Integer32):
    """Custom type usdPolicyIfInputPolicyId based on Integer32"""
    defaultValue = 0


_UsdPolicyIfInputPolicyId_Object = MibTableColumn
usdPolicyIfInputPolicyId = _UsdPolicyIfInputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 3),
    _UsdPolicyIfInputPolicyId_Type()
)
usdPolicyIfInputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfInputPolicyId.setStatus("obsolete")


class _UsdPolicyIfOutputPolicyId_Type(Integer32):
    """Custom type usdPolicyIfOutputPolicyId based on Integer32"""
    defaultValue = 0


_UsdPolicyIfOutputPolicyId_Object = MibTableColumn
usdPolicyIfOutputPolicyId = _UsdPolicyIfOutputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 4),
    _UsdPolicyIfOutputPolicyId_Type()
)
usdPolicyIfOutputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfOutputPolicyId.setStatus("obsolete")


class _UsdPolicyIfInputStatsEnable_Type(TruthValue):
    """Custom type usdPolicyIfInputStatsEnable based on TruthValue"""


_UsdPolicyIfInputStatsEnable_Object = MibTableColumn
usdPolicyIfInputStatsEnable = _UsdPolicyIfInputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 5),
    _UsdPolicyIfInputStatsEnable_Type()
)
usdPolicyIfInputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfInputStatsEnable.setStatus("obsolete")


class _UsdPolicyIfOutputStatsEnable_Type(TruthValue):
    """Custom type usdPolicyIfOutputStatsEnable based on TruthValue"""


_UsdPolicyIfOutputStatsEnable_Object = MibTableColumn
usdPolicyIfOutputStatsEnable = _UsdPolicyIfOutputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 6),
    _UsdPolicyIfOutputStatsEnable_Type()
)
usdPolicyIfOutputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfOutputStatsEnable.setStatus("obsolete")
_UsdPolicyIfAttachTable_Object = MibTable
usdPolicyIfAttachTable = _UsdPolicyIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2)
)
if mibBuilder.loadTexts:
    usdPolicyIfAttachTable.setStatus("current")
_UsdPolicyIfAttachEntry_Object = MibTableRow
usdPolicyIfAttachEntry = _UsdPolicyIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1)
)
usdPolicyIfAttachEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachInterfaceId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachForwardingType"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachPolicyType"),
)
if mibBuilder.loadTexts:
    usdPolicyIfAttachEntry.setStatus("current")
_UsdPolicyIfAttachInterfaceId_Type = InterfaceIndex
_UsdPolicyIfAttachInterfaceId_Object = MibTableColumn
usdPolicyIfAttachInterfaceId = _UsdPolicyIfAttachInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 1),
    _UsdPolicyIfAttachInterfaceId_Type()
)
usdPolicyIfAttachInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachInterfaceId.setStatus("current")
_UsdPolicyIfAttachForwardingType_Type = UsdPolicyForwardingType
_UsdPolicyIfAttachForwardingType_Object = MibTableColumn
usdPolicyIfAttachForwardingType = _UsdPolicyIfAttachForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 2),
    _UsdPolicyIfAttachForwardingType_Type()
)
usdPolicyIfAttachForwardingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachForwardingType.setStatus("current")
_UsdPolicyIfAttachPolicyType_Type = UsdPolicyAttachmentType
_UsdPolicyIfAttachPolicyType_Object = MibTableColumn
usdPolicyIfAttachPolicyType = _UsdPolicyIfAttachPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 3),
    _UsdPolicyIfAttachPolicyType_Type()
)
usdPolicyIfAttachPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachPolicyType.setStatus("current")
_UsdPolicyIfAttachRowStatus_Type = RowStatus
_UsdPolicyIfAttachRowStatus_Object = MibTableColumn
usdPolicyIfAttachRowStatus = _UsdPolicyIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 4),
    _UsdPolicyIfAttachRowStatus_Type()
)
usdPolicyIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfAttachRowStatus.setStatus("current")


class _UsdPolicyIfAttachPolicyId_Type(Integer32):
    """Custom type usdPolicyIfAttachPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfAttachPolicyId_Type.__name__ = "Integer32"
_UsdPolicyIfAttachPolicyId_Object = MibTableColumn
usdPolicyIfAttachPolicyId = _UsdPolicyIfAttachPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 5),
    _UsdPolicyIfAttachPolicyId_Type()
)
usdPolicyIfAttachPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfAttachPolicyId.setStatus("current")


class _UsdPolicyIfAttachStatsEnable_Type(TruthValue):
    """Custom type usdPolicyIfAttachStatsEnable based on TruthValue"""


_UsdPolicyIfAttachStatsEnable_Object = MibTableColumn
usdPolicyIfAttachStatsEnable = _UsdPolicyIfAttachStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 6),
    _UsdPolicyIfAttachStatsEnable_Type()
)
usdPolicyIfAttachStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsEnable.setStatus("current")
_UsdPolicyProfile_ObjectIdentity = ObjectIdentity
usdPolicyProfile = _UsdPolicyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5)
)
_UsdPolicyProfileTable_Object = MibTable
usdPolicyProfileTable = _UsdPolicyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1)
)
if mibBuilder.loadTexts:
    usdPolicyProfileTable.setStatus("obsolete")
_UsdPolicyProfileEntry_Object = MibTableRow
usdPolicyProfileEntry = _UsdPolicyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1)
)
usdPolicyProfileEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyProfileId"),
)
if mibBuilder.loadTexts:
    usdPolicyProfileEntry.setStatus("obsolete")
_UsdPolicyProfileId_Type = Unsigned32
_UsdPolicyProfileId_Object = MibTableColumn
usdPolicyProfileId = _UsdPolicyProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 1),
    _UsdPolicyProfileId_Type()
)
usdPolicyProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyProfileId.setStatus("obsolete")
_UsdPolicyProfileRowStatus_Type = RowStatus
_UsdPolicyProfileRowStatus_Object = MibTableColumn
usdPolicyProfileRowStatus = _UsdPolicyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 2),
    _UsdPolicyProfileRowStatus_Type()
)
usdPolicyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyProfileRowStatus.setStatus("obsolete")


class _UsdPolicyProfileInputPolicyId_Type(Integer32):
    """Custom type usdPolicyProfileInputPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyProfileInputPolicyId_Type.__name__ = "Integer32"
_UsdPolicyProfileInputPolicyId_Object = MibTableColumn
usdPolicyProfileInputPolicyId = _UsdPolicyProfileInputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 3),
    _UsdPolicyProfileInputPolicyId_Type()
)
usdPolicyProfileInputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyProfileInputPolicyId.setStatus("obsolete")


class _UsdPolicyProfileOutputPolicyId_Type(Integer32):
    """Custom type usdPolicyProfileOutputPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyProfileOutputPolicyId_Type.__name__ = "Integer32"
_UsdPolicyProfileOutputPolicyId_Object = MibTableColumn
usdPolicyProfileOutputPolicyId = _UsdPolicyProfileOutputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 4),
    _UsdPolicyProfileOutputPolicyId_Type()
)
usdPolicyProfileOutputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyProfileOutputPolicyId.setStatus("obsolete")


class _UsdPolicyProfileInputStatsEnable_Type(TruthValue):
    """Custom type usdPolicyProfileInputStatsEnable based on TruthValue"""


_UsdPolicyProfileInputStatsEnable_Object = MibTableColumn
usdPolicyProfileInputStatsEnable = _UsdPolicyProfileInputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 5),
    _UsdPolicyProfileInputStatsEnable_Type()
)
usdPolicyProfileInputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyProfileInputStatsEnable.setStatus("obsolete")


class _UsdPolicyProfileOutputStatsEnable_Type(TruthValue):
    """Custom type usdPolicyProfileOutputStatsEnable based on TruthValue"""


_UsdPolicyProfileOutputStatsEnable_Object = MibTableColumn
usdPolicyProfileOutputStatsEnable = _UsdPolicyProfileOutputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 6),
    _UsdPolicyProfileOutputStatsEnable_Type()
)
usdPolicyProfileOutputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyProfileOutputStatsEnable.setStatus("obsolete")


class _UsdPolicyProfileLocalInputPolicyId_Type(Integer32):
    """Custom type usdPolicyProfileLocalInputPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyProfileLocalInputPolicyId_Type.__name__ = "Integer32"
_UsdPolicyProfileLocalInputPolicyId_Object = MibTableColumn
usdPolicyProfileLocalInputPolicyId = _UsdPolicyProfileLocalInputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 7),
    _UsdPolicyProfileLocalInputPolicyId_Type()
)
usdPolicyProfileLocalInputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyProfileLocalInputPolicyId.setStatus("obsolete")


class _UsdPolicyProfileLocalInputStatsEnable_Type(TruthValue):
    """Custom type usdPolicyProfileLocalInputStatsEnable based on TruthValue"""


_UsdPolicyProfileLocalInputStatsEnable_Object = MibTableColumn
usdPolicyProfileLocalInputStatsEnable = _UsdPolicyProfileLocalInputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 8),
    _UsdPolicyProfileLocalInputStatsEnable_Type()
)
usdPolicyProfileLocalInputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyProfileLocalInputStatsEnable.setStatus("obsolete")
_UsdPolicyAttachProfileTable_Object = MibTable
usdPolicyAttachProfileTable = _UsdPolicyAttachProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2)
)
if mibBuilder.loadTexts:
    usdPolicyAttachProfileTable.setStatus("current")
_UsdPolicyAttachProfileEntry_Object = MibTableRow
usdPolicyAttachProfileEntry = _UsdPolicyAttachProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1)
)
usdPolicyAttachProfileEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyAttachProfileId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyAttachProfileForwardingType"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyAttachProfilePolicyType"),
)
if mibBuilder.loadTexts:
    usdPolicyAttachProfileEntry.setStatus("current")
_UsdPolicyAttachProfileId_Type = Unsigned32
_UsdPolicyAttachProfileId_Object = MibTableColumn
usdPolicyAttachProfileId = _UsdPolicyAttachProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 1),
    _UsdPolicyAttachProfileId_Type()
)
usdPolicyAttachProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyAttachProfileId.setStatus("current")
_UsdPolicyAttachProfileForwardingType_Type = UsdPolicyForwardingType
_UsdPolicyAttachProfileForwardingType_Object = MibTableColumn
usdPolicyAttachProfileForwardingType = _UsdPolicyAttachProfileForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 2),
    _UsdPolicyAttachProfileForwardingType_Type()
)
usdPolicyAttachProfileForwardingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyAttachProfileForwardingType.setStatus("current")
_UsdPolicyAttachProfilePolicyType_Type = UsdPolicyAttachmentType
_UsdPolicyAttachProfilePolicyType_Object = MibTableColumn
usdPolicyAttachProfilePolicyType = _UsdPolicyAttachProfilePolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 3),
    _UsdPolicyAttachProfilePolicyType_Type()
)
usdPolicyAttachProfilePolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyAttachProfilePolicyType.setStatus("current")
_UsdPolicyAttachProfileRowStatus_Type = RowStatus
_UsdPolicyAttachProfileRowStatus_Object = MibTableColumn
usdPolicyAttachProfileRowStatus = _UsdPolicyAttachProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 4),
    _UsdPolicyAttachProfileRowStatus_Type()
)
usdPolicyAttachProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyAttachProfileRowStatus.setStatus("current")


class _UsdPolicyAttachProfilePolicyId_Type(Integer32):
    """Custom type usdPolicyAttachProfilePolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyAttachProfilePolicyId_Type.__name__ = "Integer32"
_UsdPolicyAttachProfilePolicyId_Object = MibTableColumn
usdPolicyAttachProfilePolicyId = _UsdPolicyAttachProfilePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 5),
    _UsdPolicyAttachProfilePolicyId_Type()
)
usdPolicyAttachProfilePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyAttachProfilePolicyId.setStatus("current")


class _UsdPolicyAttachProfileStatsEnable_Type(TruthValue):
    """Custom type usdPolicyAttachProfileStatsEnable based on TruthValue"""


_UsdPolicyAttachProfileStatsEnable_Object = MibTableColumn
usdPolicyAttachProfileStatsEnable = _UsdPolicyAttachProfileStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 6),
    _UsdPolicyAttachProfileStatsEnable_Type()
)
usdPolicyAttachProfileStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPolicyAttachProfileStatsEnable.setStatus("current")
_UsdPolicyStatistics_ObjectIdentity = ObjectIdentity
usdPolicyStatistics = _UsdPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6)
)
_UsdPolicyIfStatsTable_Object = MibTable
usdPolicyIfStatsTable = _UsdPolicyIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1)
)
if mibBuilder.loadTexts:
    usdPolicyIfStatsTable.setStatus("obsolete")
_UsdPolicyIfStatsEntry_Object = MibTableRow
usdPolicyIfStatsEntry = _UsdPolicyIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1)
)
usdPolicyIfStatsEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsIfId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsPolicyType"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsPolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsRuleId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsClaclEntryNumber"),
)
if mibBuilder.loadTexts:
    usdPolicyIfStatsEntry.setStatus("obsolete")
_UsdPolicyIfStatsIfId_Type = InterfaceIndex
_UsdPolicyIfStatsIfId_Object = MibTableColumn
usdPolicyIfStatsIfId = _UsdPolicyIfStatsIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 1),
    _UsdPolicyIfStatsIfId_Type()
)
usdPolicyIfStatsIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfStatsIfId.setStatus("obsolete")
_UsdPolicyIfStatsPolicyType_Type = UsdPolicyAttachmentType
_UsdPolicyIfStatsPolicyType_Object = MibTableColumn
usdPolicyIfStatsPolicyType = _UsdPolicyIfStatsPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 2),
    _UsdPolicyIfStatsPolicyType_Type()
)
usdPolicyIfStatsPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfStatsPolicyType.setStatus("obsolete")


class _UsdPolicyIfStatsPolicyId_Type(Integer32):
    """Custom type usdPolicyIfStatsPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfStatsPolicyId_Type.__name__ = "Integer32"
_UsdPolicyIfStatsPolicyId_Object = MibTableColumn
usdPolicyIfStatsPolicyId = _UsdPolicyIfStatsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 3),
    _UsdPolicyIfStatsPolicyId_Type()
)
usdPolicyIfStatsPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfStatsPolicyId.setStatus("obsolete")


class _UsdPolicyIfStatsRulePrec_Type(Integer32):
    """Custom type usdPolicyIfStatsRulePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfStatsRulePrec_Type.__name__ = "Integer32"
_UsdPolicyIfStatsRulePrec_Object = MibTableColumn
usdPolicyIfStatsRulePrec = _UsdPolicyIfStatsRulePrec_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 4),
    _UsdPolicyIfStatsRulePrec_Type()
)
usdPolicyIfStatsRulePrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfStatsRulePrec.setStatus("obsolete")


class _UsdPolicyIfStatsRuleId_Type(Integer32):
    """Custom type usdPolicyIfStatsRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfStatsRuleId_Type.__name__ = "Integer32"
_UsdPolicyIfStatsRuleId_Object = MibTableColumn
usdPolicyIfStatsRuleId = _UsdPolicyIfStatsRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 5),
    _UsdPolicyIfStatsRuleId_Type()
)
usdPolicyIfStatsRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfStatsRuleId.setStatus("obsolete")


class _UsdPolicyIfStatsClaclEntryNumber_Type(Integer32):
    """Custom type usdPolicyIfStatsClaclEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfStatsClaclEntryNumber_Type.__name__ = "Integer32"
_UsdPolicyIfStatsClaclEntryNumber_Object = MibTableColumn
usdPolicyIfStatsClaclEntryNumber = _UsdPolicyIfStatsClaclEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 6),
    _UsdPolicyIfStatsClaclEntryNumber_Type()
)
usdPolicyIfStatsClaclEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfStatsClaclEntryNumber.setStatus("obsolete")
_UsdPolicyIfStatsGreenPackets_Type = Counter64
_UsdPolicyIfStatsGreenPackets_Object = MibTableColumn
usdPolicyIfStatsGreenPackets = _UsdPolicyIfStatsGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 7),
    _UsdPolicyIfStatsGreenPackets_Type()
)
usdPolicyIfStatsGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfStatsGreenPackets.setStatus("obsolete")
_UsdPolicyIfStatsYellowPackets_Type = Counter64
_UsdPolicyIfStatsYellowPackets_Object = MibTableColumn
usdPolicyIfStatsYellowPackets = _UsdPolicyIfStatsYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 8),
    _UsdPolicyIfStatsYellowPackets_Type()
)
usdPolicyIfStatsYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfStatsYellowPackets.setStatus("obsolete")
_UsdPolicyIfStatsRedPackets_Type = Counter64
_UsdPolicyIfStatsRedPackets_Object = MibTableColumn
usdPolicyIfStatsRedPackets = _UsdPolicyIfStatsRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 9),
    _UsdPolicyIfStatsRedPackets_Type()
)
usdPolicyIfStatsRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfStatsRedPackets.setStatus("obsolete")
_UsdPolicyIfStatsGreenBytes_Type = Counter64
_UsdPolicyIfStatsGreenBytes_Object = MibTableColumn
usdPolicyIfStatsGreenBytes = _UsdPolicyIfStatsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 10),
    _UsdPolicyIfStatsGreenBytes_Type()
)
usdPolicyIfStatsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfStatsGreenBytes.setStatus("obsolete")
_UsdPolicyIfStatsYellowBytes_Type = Counter64
_UsdPolicyIfStatsYellowBytes_Object = MibTableColumn
usdPolicyIfStatsYellowBytes = _UsdPolicyIfStatsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 11),
    _UsdPolicyIfStatsYellowBytes_Type()
)
usdPolicyIfStatsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfStatsYellowBytes.setStatus("obsolete")
_UsdPolicyIfStatsRedBytes_Type = Counter64
_UsdPolicyIfStatsRedBytes_Object = MibTableColumn
usdPolicyIfStatsRedBytes = _UsdPolicyIfStatsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 12),
    _UsdPolicyIfStatsRedBytes_Type()
)
usdPolicyIfStatsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfStatsRedBytes.setStatus("obsolete")
_UsdPolicyIfAttachStatsTable_Object = MibTable
usdPolicyIfAttachStatsTable = _UsdPolicyIfAttachStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2)
)
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsTable.setStatus("current")
_UsdPolicyIfAttachStatsEntry_Object = MibTableRow
usdPolicyIfAttachStatsEntry = _UsdPolicyIfAttachStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1)
)
usdPolicyIfAttachStatsEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsIfId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsForwardingType"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsPolicyType"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsPolicyId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsRulePrec"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsRuleId"),
    (0, "Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsClaclEntryNumber"),
)
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsEntry.setStatus("current")
_UsdPolicyIfAttachStatsIfId_Type = InterfaceIndex
_UsdPolicyIfAttachStatsIfId_Object = MibTableColumn
usdPolicyIfAttachStatsIfId = _UsdPolicyIfAttachStatsIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 1),
    _UsdPolicyIfAttachStatsIfId_Type()
)
usdPolicyIfAttachStatsIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsIfId.setStatus("current")
_UsdPolicyIfAttachStatsForwardingType_Type = UsdPolicyForwardingType
_UsdPolicyIfAttachStatsForwardingType_Object = MibTableColumn
usdPolicyIfAttachStatsForwardingType = _UsdPolicyIfAttachStatsForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 2),
    _UsdPolicyIfAttachStatsForwardingType_Type()
)
usdPolicyIfAttachStatsForwardingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsForwardingType.setStatus("current")
_UsdPolicyIfAttachStatsPolicyType_Type = UsdPolicyAttachmentType
_UsdPolicyIfAttachStatsPolicyType_Object = MibTableColumn
usdPolicyIfAttachStatsPolicyType = _UsdPolicyIfAttachStatsPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 3),
    _UsdPolicyIfAttachStatsPolicyType_Type()
)
usdPolicyIfAttachStatsPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsPolicyType.setStatus("current")


class _UsdPolicyIfAttachStatsPolicyId_Type(Integer32):
    """Custom type usdPolicyIfAttachStatsPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfAttachStatsPolicyId_Type.__name__ = "Integer32"
_UsdPolicyIfAttachStatsPolicyId_Object = MibTableColumn
usdPolicyIfAttachStatsPolicyId = _UsdPolicyIfAttachStatsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 4),
    _UsdPolicyIfAttachStatsPolicyId_Type()
)
usdPolicyIfAttachStatsPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsPolicyId.setStatus("current")


class _UsdPolicyIfAttachStatsRulePrec_Type(Integer32):
    """Custom type usdPolicyIfAttachStatsRulePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfAttachStatsRulePrec_Type.__name__ = "Integer32"
_UsdPolicyIfAttachStatsRulePrec_Object = MibTableColumn
usdPolicyIfAttachStatsRulePrec = _UsdPolicyIfAttachStatsRulePrec_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 5),
    _UsdPolicyIfAttachStatsRulePrec_Type()
)
usdPolicyIfAttachStatsRulePrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsRulePrec.setStatus("current")


class _UsdPolicyIfAttachStatsRuleId_Type(Integer32):
    """Custom type usdPolicyIfAttachStatsRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfAttachStatsRuleId_Type.__name__ = "Integer32"
_UsdPolicyIfAttachStatsRuleId_Object = MibTableColumn
usdPolicyIfAttachStatsRuleId = _UsdPolicyIfAttachStatsRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 6),
    _UsdPolicyIfAttachStatsRuleId_Type()
)
usdPolicyIfAttachStatsRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsRuleId.setStatus("current")


class _UsdPolicyIfAttachStatsClaclEntryNumber_Type(Integer32):
    """Custom type usdPolicyIfAttachStatsClaclEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPolicyIfAttachStatsClaclEntryNumber_Type.__name__ = "Integer32"
_UsdPolicyIfAttachStatsClaclEntryNumber_Object = MibTableColumn
usdPolicyIfAttachStatsClaclEntryNumber = _UsdPolicyIfAttachStatsClaclEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 7),
    _UsdPolicyIfAttachStatsClaclEntryNumber_Type()
)
usdPolicyIfAttachStatsClaclEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsClaclEntryNumber.setStatus("current")
_UsdPolicyIfAttachStatsGreenPackets_Type = Counter64
_UsdPolicyIfAttachStatsGreenPackets_Object = MibTableColumn
usdPolicyIfAttachStatsGreenPackets = _UsdPolicyIfAttachStatsGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 8),
    _UsdPolicyIfAttachStatsGreenPackets_Type()
)
usdPolicyIfAttachStatsGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsGreenPackets.setStatus("current")
_UsdPolicyIfAttachStatsYellowPackets_Type = Counter64
_UsdPolicyIfAttachStatsYellowPackets_Object = MibTableColumn
usdPolicyIfAttachStatsYellowPackets = _UsdPolicyIfAttachStatsYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 9),
    _UsdPolicyIfAttachStatsYellowPackets_Type()
)
usdPolicyIfAttachStatsYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsYellowPackets.setStatus("current")
_UsdPolicyIfAttachStatsRedPackets_Type = Counter64
_UsdPolicyIfAttachStatsRedPackets_Object = MibTableColumn
usdPolicyIfAttachStatsRedPackets = _UsdPolicyIfAttachStatsRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 10),
    _UsdPolicyIfAttachStatsRedPackets_Type()
)
usdPolicyIfAttachStatsRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsRedPackets.setStatus("current")
_UsdPolicyIfAttachStatsGreenBytes_Type = Counter64
_UsdPolicyIfAttachStatsGreenBytes_Object = MibTableColumn
usdPolicyIfAttachStatsGreenBytes = _UsdPolicyIfAttachStatsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 11),
    _UsdPolicyIfAttachStatsGreenBytes_Type()
)
usdPolicyIfAttachStatsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsGreenBytes.setStatus("current")
_UsdPolicyIfAttachStatsYellowBytes_Type = Counter64
_UsdPolicyIfAttachStatsYellowBytes_Object = MibTableColumn
usdPolicyIfAttachStatsYellowBytes = _UsdPolicyIfAttachStatsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 12),
    _UsdPolicyIfAttachStatsYellowBytes_Type()
)
usdPolicyIfAttachStatsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsYellowBytes.setStatus("current")
_UsdPolicyIfAttachStatsRedBytes_Type = Counter64
_UsdPolicyIfAttachStatsRedBytes_Object = MibTableColumn
usdPolicyIfAttachStatsRedBytes = _UsdPolicyIfAttachStatsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 13),
    _UsdPolicyIfAttachStatsRedBytes_Type()
)
usdPolicyIfAttachStatsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPolicyIfAttachStatsRedBytes.setStatus("current")
_UsdTrafficShapeControlList_ObjectIdentity = ObjectIdentity
usdTrafficShapeControlList = _UsdTrafficShapeControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7)
)


class _UsdTrafficShapeProfileNextIndex_Type(Integer32):
    """Custom type usdTrafficShapeProfileNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdTrafficShapeProfileNextIndex_Type.__name__ = "Integer32"
_UsdTrafficShapeProfileNextIndex_Object = MibScalar
usdTrafficShapeProfileNextIndex = _UsdTrafficShapeProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 1),
    _UsdTrafficShapeProfileNextIndex_Type()
)
usdTrafficShapeProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdTrafficShapeProfileNextIndex.setStatus("obsolete")
_UsdTrafficShapeProfileTable_Object = MibTable
usdTrafficShapeProfileTable = _UsdTrafficShapeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2)
)
if mibBuilder.loadTexts:
    usdTrafficShapeProfileTable.setStatus("obsolete")
_UsdTrafficShapeProfileEntry_Object = MibTableRow
usdTrafficShapeProfileEntry = _UsdTrafficShapeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1)
)
usdTrafficShapeProfileEntry.setIndexNames(
    (0, "Unisphere-Data-POLICY-MIB", "usdTrafficShapeProfileId"),
)
if mibBuilder.loadTexts:
    usdTrafficShapeProfileEntry.setStatus("obsolete")


class _UsdTrafficShapeProfileId_Type(Integer32):
    """Custom type usdTrafficShapeProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdTrafficShapeProfileId_Type.__name__ = "Integer32"
_UsdTrafficShapeProfileId_Object = MibTableColumn
usdTrafficShapeProfileId = _UsdTrafficShapeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 1),
    _UsdTrafficShapeProfileId_Type()
)
usdTrafficShapeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdTrafficShapeProfileId.setStatus("obsolete")
_UsdTrafficShapeProfileRowStatus_Type = RowStatus
_UsdTrafficShapeProfileRowStatus_Object = MibTableColumn
usdTrafficShapeProfileRowStatus = _UsdTrafficShapeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 2),
    _UsdTrafficShapeProfileRowStatus_Type()
)
usdTrafficShapeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficShapeProfileRowStatus.setStatus("obsolete")


class _UsdTrafficShapeProfileName_Type(DisplayString):
    """Custom type usdTrafficShapeProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_UsdTrafficShapeProfileName_Type.__name__ = "DisplayString"
_UsdTrafficShapeProfileName_Object = MibTableColumn
usdTrafficShapeProfileName = _UsdTrafficShapeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 3),
    _UsdTrafficShapeProfileName_Type()
)
usdTrafficShapeProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficShapeProfileName.setStatus("obsolete")
_UsdTrafficShapeReferenceCount_Type = Counter32
_UsdTrafficShapeReferenceCount_Object = MibTableColumn
usdTrafficShapeReferenceCount = _UsdTrafficShapeReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 4),
    _UsdTrafficShapeReferenceCount_Type()
)
usdTrafficShapeReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdTrafficShapeReferenceCount.setStatus("obsolete")


class _UsdTrafficShapeRate_Type(Integer32):
    """Custom type usdTrafficShapeRate based on Integer32"""
    defaultValue = 0


_UsdTrafficShapeRate_Object = MibTableColumn
usdTrafficShapeRate = _UsdTrafficShapeRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 5),
    _UsdTrafficShapeRate_Type()
)
usdTrafficShapeRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficShapeRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    usdTrafficShapeRate.setUnits("bits per second")


class _UsdTrafficShapeBurst_Type(Integer32):
    """Custom type usdTrafficShapeBurst based on Integer32"""
    defaultValue = 0


_UsdTrafficShapeBurst_Object = MibTableColumn
usdTrafficShapeBurst = _UsdTrafficShapeBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 6),
    _UsdTrafficShapeBurst_Type()
)
usdTrafficShapeBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdTrafficShapeBurst.setStatus("obsolete")
if mibBuilder.loadTexts:
    usdTrafficShapeBurst.setUnits("bytes")
_UsdPolicyConformance_ObjectIdentity = ObjectIdentity
usdPolicyConformance = _UsdPolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2)
)
_UsdPolicyCompliances_ObjectIdentity = ObjectIdentity
usdPolicyCompliances = _UsdPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1)
)
_UsdPolicyGroups_ObjectIdentity = ObjectIdentity
usdPolicyGroups = _UsdPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2)
)

# Managed Objects groups

usdPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 1)
)
usdPolicyGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyAdminState"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyOperStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyErrorValue"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyName"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRuleNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRuleType"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicySuspend"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyEclipsed"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopIpAddress"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdFilterRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdFilterClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceNextHop"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitId"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingTOSByte"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingMask"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdForwardRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdForwardClaclId"))
)
if mibBuilder.loadTexts:
    usdPolicyGroup.setStatus("obsolete")

usdRateLimitControlListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 2)
)
usdRateLimitControlListGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileName"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedBps"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedBurst"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceedBps"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceedBurst"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitConformedAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceededAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitConformedMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceededMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitMask"))
)
if mibBuilder.loadTexts:
    usdRateLimitControlListGroup.setStatus("obsolete")

usdClassifierControlListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 3)
)
usdClassifierControlListGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListName"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNextElementIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListElemRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNotSrc"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrc"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNotDst"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDst"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDstMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNotProtocol"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListProtocol"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListTosByte"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcOperator"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcFromPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcToPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDestOperator"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDestFromPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDestToPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListICMPType"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListICMPCode"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListIGMPType"))
)
if mibBuilder.loadTexts:
    usdClassifierControlListGroup.setStatus("obsolete")

usdPolicyIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 4)
)
usdPolicyIfGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyIfRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfInputPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfOutputPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfInputStatsEnable"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfOutputStatsEnable"))
)
if mibBuilder.loadTexts:
    usdPolicyIfGroup.setStatus("obsolete")

usdPolicyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 5)
)
usdPolicyProfileGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileInputPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileOutputPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileInputStatsEnable"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileOutputStatsEnable"))
)
if mibBuilder.loadTexts:
    usdPolicyProfileGroup.setStatus("obsolete")

usdPolicyStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 6)
)
usdPolicyStatisticsGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsGreenPackets"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsYellowPackets"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsRedPackets"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsGreenBytes"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsYellowBytes"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfStatsRedBytes"))
)
if mibBuilder.loadTexts:
    usdPolicyStatisticsGroup.setStatus("obsolete")

usdPolicyGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 7)
)
usdPolicyGroup2.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyAdminState"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyOperStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyErrorValue"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyName"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRuleNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRuleType"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicySuspend"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyEclipsed"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopIpAddress"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdFilterRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdFilterClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceNextHop"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitId"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingTOSByte"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingMask"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdForwardRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdForwardClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeId"),
        ("Unisphere-Data-POLICY-MIB", "usdColorRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdColor"),
        ("Unisphere-Data-POLICY-MIB", "usdColorClaclId"))
)
if mibBuilder.loadTexts:
    usdPolicyGroup2.setStatus("obsolete")

usdTrafficShapeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 8)
)
usdTrafficShapeProfileGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdTrafficShapeProfileNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeProfileName"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeRate"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeBurst"))
)
if mibBuilder.loadTexts:
    usdTrafficShapeProfileGroup.setStatus("obsolete")

usdLogRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 9)
)
usdLogRuleGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdLogRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdLogClaclId"))
)
if mibBuilder.loadTexts:
    usdLogRuleGroup.setStatus("current")

usdPolicyIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 10)
)
usdPolicyIfAttachGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsEnable"))
)
if mibBuilder.loadTexts:
    usdPolicyIfAttachGroup.setStatus("current")

usdPolicyProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 11)
)
usdPolicyProfileGroup2.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileInputPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileOutputPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileInputStatsEnable"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileOutputStatsEnable"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileLocalInputPolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyProfileLocalInputStatsEnable"))
)
if mibBuilder.loadTexts:
    usdPolicyProfileGroup2.setStatus("obsolete")

usdPolicyAttachStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 12)
)
usdPolicyAttachStatisticsGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsGreenPackets"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsYellowPackets"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsRedPackets"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsGreenBytes"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsYellowBytes"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyIfAttachStatsRedBytes"))
)
if mibBuilder.loadTexts:
    usdPolicyAttachStatisticsGroup.setStatus("current")

usdClassifierControlListGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 13)
)
usdClassifierControlListGroup2.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListName"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNextElementIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListElemRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNotSrc"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrc"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNotDst"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDst"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDstMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListNotProtocol"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListProtocol"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListTosByte"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcOperator"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcFromPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListSrcToPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDestOperator"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDestFromPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListDestToPort"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListICMPType"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListICMPCode"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListIGMPType"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListTcpFlagsValue"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListTcpFlagsMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListIpFlagsValue"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListIpFlagsMask"),
        ("Unisphere-Data-POLICY-MIB", "usdClassifierControlListIpFragValue"))
)
if mibBuilder.loadTexts:
    usdClassifierControlListGroup2.setStatus("current")

usdPolicyAttachProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 14)
)
usdPolicyAttachProfileGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyAttachProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyAttachProfilePolicyId"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyAttachProfileStatsEnable"))
)
if mibBuilder.loadTexts:
    usdPolicyAttachProfileGroup.setStatus("current")

usdPolicyBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 15)
)
usdPolicyBaseGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdPolicyNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyAdminState"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyOperStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyErrorValue"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyName"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRuleNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyRuleType"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicySuspend"),
        ("Unisphere-Data-POLICY-MIB", "usdPolicyEclipsed"))
)
if mibBuilder.loadTexts:
    usdPolicyBaseGroup.setStatus("current")

usdNextHopRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 16)
)
usdNextHopRulesGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdNextHopRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopIpAddress"),
        ("Unisphere-Data-POLICY-MIB", "usdNextHopClaclId"))
)
if mibBuilder.loadTexts:
    usdNextHopRulesGroup.setStatus("current")

usdFilterRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 17)
)
usdFilterRulesGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdFilterRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdFilterClaclId"))
)
if mibBuilder.loadTexts:
    usdFilterRulesGroup.setStatus("current")

usdNextInterfaceRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 18)
)
usdNextInterfaceRulesGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdNextInterfaceRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdNextInterfaceNextHop"))
)
if mibBuilder.loadTexts:
    usdNextInterfaceRulesGroup.setStatus("current")

usdRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 19)
)
usdRateLimitGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdRateLimitRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitId"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileName"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedBps"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedBurst"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceedBps"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceedBurst"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitConformedAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceededAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitConformedMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceededMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitMask"))
)
if mibBuilder.loadTexts:
    usdRateLimitGroup.setStatus("obsolete")

usdMarkingRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 20)
)
usdMarkingRulesGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdMarkingRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingTOSByte"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingMask"),
        ("Unisphere-Data-POLICY-MIB", "usdMarkingClaclId"))
)
if mibBuilder.loadTexts:
    usdMarkingRulesGroup.setStatus("current")

usdForwardRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 21)
)
usdForwardRulesGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdForwardRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdForwardClaclId"))
)
if mibBuilder.loadTexts:
    usdForwardRulesGroup.setStatus("current")

usdTrafficShapeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 22)
)
usdTrafficShapeGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdTrafficShapeRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeId"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeProfileNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeProfileName"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeRate"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficShapeBurst"))
)
if mibBuilder.loadTexts:
    usdTrafficShapeGroup.setStatus("obsolete")

usdColorRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 23)
)
usdColorRulesGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdColorRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdColor"),
        ("Unisphere-Data-POLICY-MIB", "usdColorClaclId"))
)
if mibBuilder.loadTexts:
    usdColorRulesGroup.setStatus("current")

usdTrafficClassRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 24)
)
usdTrafficClassRulesGroup.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdTrafficClassRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficClassId"),
        ("Unisphere-Data-POLICY-MIB", "usdTrafficClassClaclId"))
)
if mibBuilder.loadTexts:
    usdTrafficClassRulesGroup.setStatus("current")

usdRateLimitGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 25)
)
usdRateLimitGroup2.setObjects(
      *(("Unisphere-Data-POLICY-MIB", "usdRateLimitRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitId"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitClaclId"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileNextIndex"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileRowStatus"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileName"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitProfileType"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitReferenceCount"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedBps"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedBurst"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceedBps"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceedBurst"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExcessBurst"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitConformedAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceededAction"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitCommittedMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitConformedMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitExceededMarkVal"),
        ("Unisphere-Data-POLICY-MIB", "usdRateLimitMask"))
)
if mibBuilder.loadTexts:
    usdRateLimitGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdPolicyCompliance.setStatus(
        "obsolete"
    )

usdPolicyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdPolicyCompliance2.setStatus(
        "obsolete"
    )

usdPolicyCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 3)
)
if mibBuilder.loadTexts:
    usdPolicyCompliance3.setStatus(
        "obsolete"
    )

usdPolicyCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 4)
)
if mibBuilder.loadTexts:
    usdPolicyCompliance4.setStatus(
        "obsolete"
    )

usdPolicyCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 5)
)
if mibBuilder.loadTexts:
    usdPolicyCompliance5.setStatus(
        "obsolete"
    )

usdPolicyCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 6)
)
if mibBuilder.loadTexts:
    usdPolicyCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-POLICY-MIB",
    **{"UsdClaclPortOperator": UsdClaclPortOperator,
       "UsdPolicyAttachmentType": UsdPolicyAttachmentType,
       "UsdPolicyForwardingType": UsdPolicyForwardingType,
       "UsdPolicyIpFragValue": UsdPolicyIpFragValue,
       "UsdRateLimitProfileType": UsdRateLimitProfileType,
       "usdPolicyMIB": usdPolicyMIB,
       "usdPolicyObjects": usdPolicyObjects,
       "usdClassifierControlList": usdClassifierControlList,
       "usdClassifierControlListNextIndex": usdClassifierControlListNextIndex,
       "usdClassifierControlListTable": usdClassifierControlListTable,
       "usdClassifierControlListEntry": usdClassifierControlListEntry,
       "usdClassifierControlListId": usdClassifierControlListId,
       "usdClassifierControlListRowStatus": usdClassifierControlListRowStatus,
       "usdClassifierControlListName": usdClassifierControlListName,
       "usdClassifierControlListReferenceCount": usdClassifierControlListReferenceCount,
       "usdClassifierControlListNextElementIndex": usdClassifierControlListNextElementIndex,
       "usdClassifierControlListElementTable": usdClassifierControlListElementTable,
       "usdClassifierControlListElementEntry": usdClassifierControlListElementEntry,
       "usdClassifierControlListElemId": usdClassifierControlListElemId,
       "usdClassifierControlListElemRowStatus": usdClassifierControlListElemRowStatus,
       "usdClassifierControlListNotSrc": usdClassifierControlListNotSrc,
       "usdClassifierControlListSrc": usdClassifierControlListSrc,
       "usdClassifierControlListSrcMask": usdClassifierControlListSrcMask,
       "usdClassifierControlListNotDst": usdClassifierControlListNotDst,
       "usdClassifierControlListDst": usdClassifierControlListDst,
       "usdClassifierControlListDstMask": usdClassifierControlListDstMask,
       "usdClassifierControlListNotProtocol": usdClassifierControlListNotProtocol,
       "usdClassifierControlListProtocol": usdClassifierControlListProtocol,
       "usdClassifierControlListTosByte": usdClassifierControlListTosByte,
       "usdClassifierControlListMask": usdClassifierControlListMask,
       "usdClassifierControlListSrcOperator": usdClassifierControlListSrcOperator,
       "usdClassifierControlListSrcFromPort": usdClassifierControlListSrcFromPort,
       "usdClassifierControlListSrcToPort": usdClassifierControlListSrcToPort,
       "usdClassifierControlListDestOperator": usdClassifierControlListDestOperator,
       "usdClassifierControlListDestFromPort": usdClassifierControlListDestFromPort,
       "usdClassifierControlListDestToPort": usdClassifierControlListDestToPort,
       "usdClassifierControlListICMPType": usdClassifierControlListICMPType,
       "usdClassifierControlListICMPCode": usdClassifierControlListICMPCode,
       "usdClassifierControlListIGMPType": usdClassifierControlListIGMPType,
       "usdClassifierControlListTcpFlagsValue": usdClassifierControlListTcpFlagsValue,
       "usdClassifierControlListTcpFlagsMask": usdClassifierControlListTcpFlagsMask,
       "usdClassifierControlListIpFlagsValue": usdClassifierControlListIpFlagsValue,
       "usdClassifierControlListIpFlagsMask": usdClassifierControlListIpFlagsMask,
       "usdClassifierControlListIpFragValue": usdClassifierControlListIpFragValue,
       "usdRateLimitControlList": usdRateLimitControlList,
       "usdRateLimitProfileNextIndex": usdRateLimitProfileNextIndex,
       "usdRateLimitProfileTable": usdRateLimitProfileTable,
       "usdRateLimitProfileEntry": usdRateLimitProfileEntry,
       "usdRateLimitProfileId": usdRateLimitProfileId,
       "usdRateLimitProfileRowStatus": usdRateLimitProfileRowStatus,
       "usdRateLimitProfileName": usdRateLimitProfileName,
       "usdRateLimitReferenceCount": usdRateLimitReferenceCount,
       "usdRateLimitCommittedBps": usdRateLimitCommittedBps,
       "usdRateLimitCommittedBurst": usdRateLimitCommittedBurst,
       "usdRateLimitExceedBps": usdRateLimitExceedBps,
       "usdRateLimitExceedBurst": usdRateLimitExceedBurst,
       "usdRateLimitCommittedAction": usdRateLimitCommittedAction,
       "usdRateLimitConformedAction": usdRateLimitConformedAction,
       "usdRateLimitExceededAction": usdRateLimitExceededAction,
       "usdRateLimitCommittedMarkVal": usdRateLimitCommittedMarkVal,
       "usdRateLimitConformedMarkVal": usdRateLimitConformedMarkVal,
       "usdRateLimitExceededMarkVal": usdRateLimitExceededMarkVal,
       "usdRateLimitMask": usdRateLimitMask,
       "usdRateLimitProfileType": usdRateLimitProfileType,
       "usdRateLimitExcessBurst": usdRateLimitExcessBurst,
       "usdPolicy": usdPolicy,
       "usdPolicyNextIndex": usdPolicyNextIndex,
       "usdPolicyTable": usdPolicyTable,
       "usdPolicyEntry": usdPolicyEntry,
       "usdPolicyId": usdPolicyId,
       "usdPolicyRowStatus": usdPolicyRowStatus,
       "usdPolicyAdminState": usdPolicyAdminState,
       "usdPolicyOperStatus": usdPolicyOperStatus,
       "usdPolicyErrorValue": usdPolicyErrorValue,
       "usdPolicyName": usdPolicyName,
       "usdPolicyReferenceCount": usdPolicyReferenceCount,
       "usdPolicyRuleNextIndex": usdPolicyRuleNextIndex,
       "usdPolicyRuleTable": usdPolicyRuleTable,
       "usdPolicyRuleEntry": usdPolicyRuleEntry,
       "usdPolicyRulePolicyId": usdPolicyRulePolicyId,
       "usdPolicyRulePrec": usdPolicyRulePrec,
       "usdPolicyRuleId": usdPolicyRuleId,
       "usdPolicyRuleType": usdPolicyRuleType,
       "usdPolicySuspend": usdPolicySuspend,
       "usdPolicyEclipsed": usdPolicyEclipsed,
       "usdNextHopRuleTable": usdNextHopRuleTable,
       "usdNextHopRuleEntry": usdNextHopRuleEntry,
       "usdNextHopRowStatus": usdNextHopRowStatus,
       "usdNextHopIpAddress": usdNextHopIpAddress,
       "usdNextHopClaclId": usdNextHopClaclId,
       "usdFilterRuleTable": usdFilterRuleTable,
       "usdFilterRuleEntry": usdFilterRuleEntry,
       "usdFilterRowStatus": usdFilterRowStatus,
       "usdFilterClaclId": usdFilterClaclId,
       "usdNextInterfaceRuleTable": usdNextInterfaceRuleTable,
       "usdNextInterfaceRuleEntry": usdNextInterfaceRuleEntry,
       "usdNextInterfaceRowStatus": usdNextInterfaceRowStatus,
       "usdNextInterfaceId": usdNextInterfaceId,
       "usdNextInterfaceClaclId": usdNextInterfaceClaclId,
       "usdNextInterfaceNextHop": usdNextInterfaceNextHop,
       "usdRateLimitRuleTable": usdRateLimitRuleTable,
       "usdRateLimitRuleEntry": usdRateLimitRuleEntry,
       "usdRateLimitRowStatus": usdRateLimitRowStatus,
       "usdRateLimitId": usdRateLimitId,
       "usdRateLimitClaclId": usdRateLimitClaclId,
       "usdMarkingRuleTable": usdMarkingRuleTable,
       "usdMarkingRuleEntry": usdMarkingRuleEntry,
       "usdMarkingRowStatus": usdMarkingRowStatus,
       "usdMarkingTOSByte": usdMarkingTOSByte,
       "usdMarkingMask": usdMarkingMask,
       "usdMarkingClaclId": usdMarkingClaclId,
       "usdForwardRuleTable": usdForwardRuleTable,
       "usdForwardRuleEntry": usdForwardRuleEntry,
       "usdForwardRowStatus": usdForwardRowStatus,
       "usdForwardClaclId": usdForwardClaclId,
       "usdTrafficShapeRuleTable": usdTrafficShapeRuleTable,
       "usdTrafficShapeRuleEntry": usdTrafficShapeRuleEntry,
       "usdTrafficShapeRowStatus": usdTrafficShapeRowStatus,
       "usdTrafficShapeId": usdTrafficShapeId,
       "usdColorRuleTable": usdColorRuleTable,
       "usdColorRuleEntry": usdColorRuleEntry,
       "usdColorRowStatus": usdColorRowStatus,
       "usdColor": usdColor,
       "usdColorClaclId": usdColorClaclId,
       "usdLogRuleTable": usdLogRuleTable,
       "usdLogRuleEntry": usdLogRuleEntry,
       "usdLogRowStatus": usdLogRowStatus,
       "usdLogClaclId": usdLogClaclId,
       "usdTrafficClassRuleTable": usdTrafficClassRuleTable,
       "usdTrafficClassRuleEntry": usdTrafficClassRuleEntry,
       "usdTrafficClassRowStatus": usdTrafficClassRowStatus,
       "usdTrafficClassId": usdTrafficClassId,
       "usdTrafficClassClaclId": usdTrafficClassClaclId,
       "usdPolicyIf": usdPolicyIf,
       "usdPolicyIfTable": usdPolicyIfTable,
       "usdPolicyIfEntry": usdPolicyIfEntry,
       "usdPolicyIfInterfaceId": usdPolicyIfInterfaceId,
       "usdPolicyIfRowStatus": usdPolicyIfRowStatus,
       "usdPolicyIfInputPolicyId": usdPolicyIfInputPolicyId,
       "usdPolicyIfOutputPolicyId": usdPolicyIfOutputPolicyId,
       "usdPolicyIfInputStatsEnable": usdPolicyIfInputStatsEnable,
       "usdPolicyIfOutputStatsEnable": usdPolicyIfOutputStatsEnable,
       "usdPolicyIfAttachTable": usdPolicyIfAttachTable,
       "usdPolicyIfAttachEntry": usdPolicyIfAttachEntry,
       "usdPolicyIfAttachInterfaceId": usdPolicyIfAttachInterfaceId,
       "usdPolicyIfAttachForwardingType": usdPolicyIfAttachForwardingType,
       "usdPolicyIfAttachPolicyType": usdPolicyIfAttachPolicyType,
       "usdPolicyIfAttachRowStatus": usdPolicyIfAttachRowStatus,
       "usdPolicyIfAttachPolicyId": usdPolicyIfAttachPolicyId,
       "usdPolicyIfAttachStatsEnable": usdPolicyIfAttachStatsEnable,
       "usdPolicyProfile": usdPolicyProfile,
       "usdPolicyProfileTable": usdPolicyProfileTable,
       "usdPolicyProfileEntry": usdPolicyProfileEntry,
       "usdPolicyProfileId": usdPolicyProfileId,
       "usdPolicyProfileRowStatus": usdPolicyProfileRowStatus,
       "usdPolicyProfileInputPolicyId": usdPolicyProfileInputPolicyId,
       "usdPolicyProfileOutputPolicyId": usdPolicyProfileOutputPolicyId,
       "usdPolicyProfileInputStatsEnable": usdPolicyProfileInputStatsEnable,
       "usdPolicyProfileOutputStatsEnable": usdPolicyProfileOutputStatsEnable,
       "usdPolicyProfileLocalInputPolicyId": usdPolicyProfileLocalInputPolicyId,
       "usdPolicyProfileLocalInputStatsEnable": usdPolicyProfileLocalInputStatsEnable,
       "usdPolicyAttachProfileTable": usdPolicyAttachProfileTable,
       "usdPolicyAttachProfileEntry": usdPolicyAttachProfileEntry,
       "usdPolicyAttachProfileId": usdPolicyAttachProfileId,
       "usdPolicyAttachProfileForwardingType": usdPolicyAttachProfileForwardingType,
       "usdPolicyAttachProfilePolicyType": usdPolicyAttachProfilePolicyType,
       "usdPolicyAttachProfileRowStatus": usdPolicyAttachProfileRowStatus,
       "usdPolicyAttachProfilePolicyId": usdPolicyAttachProfilePolicyId,
       "usdPolicyAttachProfileStatsEnable": usdPolicyAttachProfileStatsEnable,
       "usdPolicyStatistics": usdPolicyStatistics,
       "usdPolicyIfStatsTable": usdPolicyIfStatsTable,
       "usdPolicyIfStatsEntry": usdPolicyIfStatsEntry,
       "usdPolicyIfStatsIfId": usdPolicyIfStatsIfId,
       "usdPolicyIfStatsPolicyType": usdPolicyIfStatsPolicyType,
       "usdPolicyIfStatsPolicyId": usdPolicyIfStatsPolicyId,
       "usdPolicyIfStatsRulePrec": usdPolicyIfStatsRulePrec,
       "usdPolicyIfStatsRuleId": usdPolicyIfStatsRuleId,
       "usdPolicyIfStatsClaclEntryNumber": usdPolicyIfStatsClaclEntryNumber,
       "usdPolicyIfStatsGreenPackets": usdPolicyIfStatsGreenPackets,
       "usdPolicyIfStatsYellowPackets": usdPolicyIfStatsYellowPackets,
       "usdPolicyIfStatsRedPackets": usdPolicyIfStatsRedPackets,
       "usdPolicyIfStatsGreenBytes": usdPolicyIfStatsGreenBytes,
       "usdPolicyIfStatsYellowBytes": usdPolicyIfStatsYellowBytes,
       "usdPolicyIfStatsRedBytes": usdPolicyIfStatsRedBytes,
       "usdPolicyIfAttachStatsTable": usdPolicyIfAttachStatsTable,
       "usdPolicyIfAttachStatsEntry": usdPolicyIfAttachStatsEntry,
       "usdPolicyIfAttachStatsIfId": usdPolicyIfAttachStatsIfId,
       "usdPolicyIfAttachStatsForwardingType": usdPolicyIfAttachStatsForwardingType,
       "usdPolicyIfAttachStatsPolicyType": usdPolicyIfAttachStatsPolicyType,
       "usdPolicyIfAttachStatsPolicyId": usdPolicyIfAttachStatsPolicyId,
       "usdPolicyIfAttachStatsRulePrec": usdPolicyIfAttachStatsRulePrec,
       "usdPolicyIfAttachStatsRuleId": usdPolicyIfAttachStatsRuleId,
       "usdPolicyIfAttachStatsClaclEntryNumber": usdPolicyIfAttachStatsClaclEntryNumber,
       "usdPolicyIfAttachStatsGreenPackets": usdPolicyIfAttachStatsGreenPackets,
       "usdPolicyIfAttachStatsYellowPackets": usdPolicyIfAttachStatsYellowPackets,
       "usdPolicyIfAttachStatsRedPackets": usdPolicyIfAttachStatsRedPackets,
       "usdPolicyIfAttachStatsGreenBytes": usdPolicyIfAttachStatsGreenBytes,
       "usdPolicyIfAttachStatsYellowBytes": usdPolicyIfAttachStatsYellowBytes,
       "usdPolicyIfAttachStatsRedBytes": usdPolicyIfAttachStatsRedBytes,
       "usdTrafficShapeControlList": usdTrafficShapeControlList,
       "usdTrafficShapeProfileNextIndex": usdTrafficShapeProfileNextIndex,
       "usdTrafficShapeProfileTable": usdTrafficShapeProfileTable,
       "usdTrafficShapeProfileEntry": usdTrafficShapeProfileEntry,
       "usdTrafficShapeProfileId": usdTrafficShapeProfileId,
       "usdTrafficShapeProfileRowStatus": usdTrafficShapeProfileRowStatus,
       "usdTrafficShapeProfileName": usdTrafficShapeProfileName,
       "usdTrafficShapeReferenceCount": usdTrafficShapeReferenceCount,
       "usdTrafficShapeRate": usdTrafficShapeRate,
       "usdTrafficShapeBurst": usdTrafficShapeBurst,
       "usdPolicyConformance": usdPolicyConformance,
       "usdPolicyCompliances": usdPolicyCompliances,
       "usdPolicyCompliance": usdPolicyCompliance,
       "usdPolicyCompliance2": usdPolicyCompliance2,
       "usdPolicyCompliance3": usdPolicyCompliance3,
       "usdPolicyCompliance4": usdPolicyCompliance4,
       "usdPolicyCompliance5": usdPolicyCompliance5,
       "usdPolicyCompliance6": usdPolicyCompliance6,
       "usdPolicyGroups": usdPolicyGroups,
       "usdPolicyGroup": usdPolicyGroup,
       "usdRateLimitControlListGroup": usdRateLimitControlListGroup,
       "usdClassifierControlListGroup": usdClassifierControlListGroup,
       "usdPolicyIfGroup": usdPolicyIfGroup,
       "usdPolicyProfileGroup": usdPolicyProfileGroup,
       "usdPolicyStatisticsGroup": usdPolicyStatisticsGroup,
       "usdPolicyGroup2": usdPolicyGroup2,
       "usdTrafficShapeProfileGroup": usdTrafficShapeProfileGroup,
       "usdLogRuleGroup": usdLogRuleGroup,
       "usdPolicyIfAttachGroup": usdPolicyIfAttachGroup,
       "usdPolicyProfileGroup2": usdPolicyProfileGroup2,
       "usdPolicyAttachStatisticsGroup": usdPolicyAttachStatisticsGroup,
       "usdClassifierControlListGroup2": usdClassifierControlListGroup2,
       "usdPolicyAttachProfileGroup": usdPolicyAttachProfileGroup,
       "usdPolicyBaseGroup": usdPolicyBaseGroup,
       "usdNextHopRulesGroup": usdNextHopRulesGroup,
       "usdFilterRulesGroup": usdFilterRulesGroup,
       "usdNextInterfaceRulesGroup": usdNextInterfaceRulesGroup,
       "usdRateLimitGroup": usdRateLimitGroup,
       "usdMarkingRulesGroup": usdMarkingRulesGroup,
       "usdForwardRulesGroup": usdForwardRulesGroup,
       "usdTrafficShapeGroup": usdTrafficShapeGroup,
       "usdColorRulesGroup": usdColorRulesGroup,
       "usdTrafficClassRulesGroup": usdTrafficClassRulesGroup,
       "usdRateLimitGroup2": usdRateLimitGroup2}
)
