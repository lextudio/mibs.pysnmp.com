# SNMP MIB module (Juniper-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:37 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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


# MODULE-IDENTITY

juniPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27)
)
juniPolicyMIB.setRevisions(
        ("2005-08-08 18:21",
         "2005-02-01 15:58",
         "2003-10-21 19:05",
         "2003-08-25 21:55",
         "2003-03-13 21:55",
         "2002-09-16 21:44",
         "2002-03-28 14:53",
         "2001-09-07 14:48",
         "2001-04-17 12:10",
         "2001-01-23 21:30",
         "2000-11-29 20:30",
         "2000-05-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniClaclPortOperator(Integer32, TextualConvention):
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



class JuniPolicyAttachmentType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auxiliaryInputPolicy", 7),
          ("inputPolicy", 1),
          ("noPolicy", 0),
          ("outputPolicy", 2),
          ("secondaryInputPolicy", 4))
    )



class JuniPolicyForwardingType(Integer32, TextualConvention):
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



class JuniPolicyIpFragValue(Integer32, TextualConvention):
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



class JuniRateLimitProfileType(Integer32, TextualConvention):
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

_JuniPolicyObjects_ObjectIdentity = ObjectIdentity
juniPolicyObjects = _JuniPolicyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1)
)
_JuniClassifierControlList_ObjectIdentity = ObjectIdentity
juniClassifierControlList = _JuniClassifierControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1)
)


class _JuniClassifierControlListNextIndex_Type(Integer32):
    """Custom type juniClassifierControlListNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniClassifierControlListNextIndex_Type.__name__ = "Integer32"
_JuniClassifierControlListNextIndex_Object = MibScalar
juniClassifierControlListNextIndex = _JuniClassifierControlListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 1),
    _JuniClassifierControlListNextIndex_Type()
)
juniClassifierControlListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniClassifierControlListNextIndex.setStatus("current")
_JuniClassifierControlListTable_Object = MibTable
juniClassifierControlListTable = _JuniClassifierControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniClassifierControlListTable.setStatus("current")
_JuniClassifierControlListEntry_Object = MibTableRow
juniClassifierControlListEntry = _JuniClassifierControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1)
)
juniClassifierControlListEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniClassifierControlListId"),
)
if mibBuilder.loadTexts:
    juniClassifierControlListEntry.setStatus("current")


class _JuniClassifierControlListId_Type(Integer32):
    """Custom type juniClassifierControlListId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniClassifierControlListId_Type.__name__ = "Integer32"
_JuniClassifierControlListId_Object = MibTableColumn
juniClassifierControlListId = _JuniClassifierControlListId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 1),
    _JuniClassifierControlListId_Type()
)
juniClassifierControlListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniClassifierControlListId.setStatus("current")
_JuniClassifierControlListRowStatus_Type = RowStatus
_JuniClassifierControlListRowStatus_Object = MibTableColumn
juniClassifierControlListRowStatus = _JuniClassifierControlListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 3),
    _JuniClassifierControlListRowStatus_Type()
)
juniClassifierControlListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListRowStatus.setStatus("current")


class _JuniClassifierControlListName_Type(DisplayString):
    """Custom type juniClassifierControlListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_JuniClassifierControlListName_Type.__name__ = "DisplayString"
_JuniClassifierControlListName_Object = MibTableColumn
juniClassifierControlListName = _JuniClassifierControlListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 4),
    _JuniClassifierControlListName_Type()
)
juniClassifierControlListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListName.setStatus("current")
_JuniClassifierControlListReferenceCount_Type = Counter32
_JuniClassifierControlListReferenceCount_Object = MibTableColumn
juniClassifierControlListReferenceCount = _JuniClassifierControlListReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 5),
    _JuniClassifierControlListReferenceCount_Type()
)
juniClassifierControlListReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniClassifierControlListReferenceCount.setStatus("current")


class _JuniClassifierControlListNextElementIndex_Type(Integer32):
    """Custom type juniClassifierControlListNextElementIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniClassifierControlListNextElementIndex_Type.__name__ = "Integer32"
_JuniClassifierControlListNextElementIndex_Object = MibTableColumn
juniClassifierControlListNextElementIndex = _JuniClassifierControlListNextElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 2, 1, 6),
    _JuniClassifierControlListNextElementIndex_Type()
)
juniClassifierControlListNextElementIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniClassifierControlListNextElementIndex.setStatus("current")
_JuniClassifierControlListElementTable_Object = MibTable
juniClassifierControlListElementTable = _JuniClassifierControlListElementTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4)
)
if mibBuilder.loadTexts:
    juniClassifierControlListElementTable.setStatus("current")
_JuniClassifierControlListElementEntry_Object = MibTableRow
juniClassifierControlListElementEntry = _JuniClassifierControlListElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1)
)
juniClassifierControlListElementEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniClassifierControlListId"),
    (0, "Juniper-POLICY-MIB", "juniClassifierControlListElemId"),
)
if mibBuilder.loadTexts:
    juniClassifierControlListElementEntry.setStatus("current")


class _JuniClassifierControlListElemId_Type(Integer32):
    """Custom type juniClassifierControlListElemId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniClassifierControlListElemId_Type.__name__ = "Integer32"
_JuniClassifierControlListElemId_Object = MibTableColumn
juniClassifierControlListElemId = _JuniClassifierControlListElemId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 1),
    _JuniClassifierControlListElemId_Type()
)
juniClassifierControlListElemId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniClassifierControlListElemId.setStatus("current")
_JuniClassifierControlListElemRowStatus_Type = RowStatus
_JuniClassifierControlListElemRowStatus_Object = MibTableColumn
juniClassifierControlListElemRowStatus = _JuniClassifierControlListElemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 2),
    _JuniClassifierControlListElemRowStatus_Type()
)
juniClassifierControlListElemRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListElemRowStatus.setStatus("current")


class _JuniClassifierControlListNotSrc_Type(TruthValue):
    """Custom type juniClassifierControlListNotSrc based on TruthValue"""


_JuniClassifierControlListNotSrc_Object = MibTableColumn
juniClassifierControlListNotSrc = _JuniClassifierControlListNotSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 3),
    _JuniClassifierControlListNotSrc_Type()
)
juniClassifierControlListNotSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListNotSrc.setStatus("current")


class _JuniClassifierControlListSrc_Type(IpAddress):
    """Custom type juniClassifierControlListSrc based on IpAddress"""
    defaultHexValue = "00000000"


_JuniClassifierControlListSrc_Object = MibTableColumn
juniClassifierControlListSrc = _JuniClassifierControlListSrc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 4),
    _JuniClassifierControlListSrc_Type()
)
juniClassifierControlListSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListSrc.setStatus("current")


class _JuniClassifierControlListSrcMask_Type(IpAddress):
    """Custom type juniClassifierControlListSrcMask based on IpAddress"""
    defaultHexValue = "00000000"


_JuniClassifierControlListSrcMask_Object = MibTableColumn
juniClassifierControlListSrcMask = _JuniClassifierControlListSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 5),
    _JuniClassifierControlListSrcMask_Type()
)
juniClassifierControlListSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListSrcMask.setStatus("current")


class _JuniClassifierControlListNotDst_Type(TruthValue):
    """Custom type juniClassifierControlListNotDst based on TruthValue"""


_JuniClassifierControlListNotDst_Object = MibTableColumn
juniClassifierControlListNotDst = _JuniClassifierControlListNotDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 6),
    _JuniClassifierControlListNotDst_Type()
)
juniClassifierControlListNotDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListNotDst.setStatus("current")


class _JuniClassifierControlListDst_Type(IpAddress):
    """Custom type juniClassifierControlListDst based on IpAddress"""
    defaultHexValue = "00000000"


_JuniClassifierControlListDst_Object = MibTableColumn
juniClassifierControlListDst = _JuniClassifierControlListDst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 7),
    _JuniClassifierControlListDst_Type()
)
juniClassifierControlListDst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListDst.setStatus("current")


class _JuniClassifierControlListDstMask_Type(IpAddress):
    """Custom type juniClassifierControlListDstMask based on IpAddress"""
    defaultHexValue = "00000000"


_JuniClassifierControlListDstMask_Object = MibTableColumn
juniClassifierControlListDstMask = _JuniClassifierControlListDstMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 8),
    _JuniClassifierControlListDstMask_Type()
)
juniClassifierControlListDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListDstMask.setStatus("current")


class _JuniClassifierControlListNotProtocol_Type(TruthValue):
    """Custom type juniClassifierControlListNotProtocol based on TruthValue"""


_JuniClassifierControlListNotProtocol_Object = MibTableColumn
juniClassifierControlListNotProtocol = _JuniClassifierControlListNotProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 9),
    _JuniClassifierControlListNotProtocol_Type()
)
juniClassifierControlListNotProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListNotProtocol.setStatus("current")


class _JuniClassifierControlListProtocol_Type(Integer32):
    """Custom type juniClassifierControlListProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListProtocol_Type.__name__ = "Integer32"
_JuniClassifierControlListProtocol_Object = MibTableColumn
juniClassifierControlListProtocol = _JuniClassifierControlListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 10),
    _JuniClassifierControlListProtocol_Type()
)
juniClassifierControlListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListProtocol.setStatus("current")


class _JuniClassifierControlListTosByte_Type(Integer32):
    """Custom type juniClassifierControlListTosByte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListTosByte_Type.__name__ = "Integer32"
_JuniClassifierControlListTosByte_Object = MibTableColumn
juniClassifierControlListTosByte = _JuniClassifierControlListTosByte_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 11),
    _JuniClassifierControlListTosByte_Type()
)
juniClassifierControlListTosByte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListTosByte.setStatus("current")


class _JuniClassifierControlListMask_Type(Integer32):
    """Custom type juniClassifierControlListMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListMask_Type.__name__ = "Integer32"
_JuniClassifierControlListMask_Object = MibTableColumn
juniClassifierControlListMask = _JuniClassifierControlListMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 12),
    _JuniClassifierControlListMask_Type()
)
juniClassifierControlListMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListMask.setStatus("current")


class _JuniClassifierControlListSrcOperator_Type(JuniClaclPortOperator):
    """Custom type juniClassifierControlListSrcOperator based on JuniClaclPortOperator"""


_JuniClassifierControlListSrcOperator_Object = MibTableColumn
juniClassifierControlListSrcOperator = _JuniClassifierControlListSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 13),
    _JuniClassifierControlListSrcOperator_Type()
)
juniClassifierControlListSrcOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListSrcOperator.setStatus("current")


class _JuniClassifierControlListSrcFromPort_Type(Integer32):
    """Custom type juniClassifierControlListSrcFromPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniClassifierControlListSrcFromPort_Type.__name__ = "Integer32"
_JuniClassifierControlListSrcFromPort_Object = MibTableColumn
juniClassifierControlListSrcFromPort = _JuniClassifierControlListSrcFromPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 14),
    _JuniClassifierControlListSrcFromPort_Type()
)
juniClassifierControlListSrcFromPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListSrcFromPort.setStatus("current")


class _JuniClassifierControlListSrcToPort_Type(Integer32):
    """Custom type juniClassifierControlListSrcToPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniClassifierControlListSrcToPort_Type.__name__ = "Integer32"
_JuniClassifierControlListSrcToPort_Object = MibTableColumn
juniClassifierControlListSrcToPort = _JuniClassifierControlListSrcToPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 15),
    _JuniClassifierControlListSrcToPort_Type()
)
juniClassifierControlListSrcToPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListSrcToPort.setStatus("current")


class _JuniClassifierControlListDestOperator_Type(JuniClaclPortOperator):
    """Custom type juniClassifierControlListDestOperator based on JuniClaclPortOperator"""


_JuniClassifierControlListDestOperator_Object = MibTableColumn
juniClassifierControlListDestOperator = _JuniClassifierControlListDestOperator_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 16),
    _JuniClassifierControlListDestOperator_Type()
)
juniClassifierControlListDestOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListDestOperator.setStatus("current")


class _JuniClassifierControlListDestFromPort_Type(Integer32):
    """Custom type juniClassifierControlListDestFromPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniClassifierControlListDestFromPort_Type.__name__ = "Integer32"
_JuniClassifierControlListDestFromPort_Object = MibTableColumn
juniClassifierControlListDestFromPort = _JuniClassifierControlListDestFromPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 17),
    _JuniClassifierControlListDestFromPort_Type()
)
juniClassifierControlListDestFromPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListDestFromPort.setStatus("current")


class _JuniClassifierControlListDestToPort_Type(Integer32):
    """Custom type juniClassifierControlListDestToPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniClassifierControlListDestToPort_Type.__name__ = "Integer32"
_JuniClassifierControlListDestToPort_Object = MibTableColumn
juniClassifierControlListDestToPort = _JuniClassifierControlListDestToPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 18),
    _JuniClassifierControlListDestToPort_Type()
)
juniClassifierControlListDestToPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListDestToPort.setStatus("current")


class _JuniClassifierControlListICMPType_Type(Integer32):
    """Custom type juniClassifierControlListICMPType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListICMPType_Type.__name__ = "Integer32"
_JuniClassifierControlListICMPType_Object = MibTableColumn
juniClassifierControlListICMPType = _JuniClassifierControlListICMPType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 19),
    _JuniClassifierControlListICMPType_Type()
)
juniClassifierControlListICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListICMPType.setStatus("current")


class _JuniClassifierControlListICMPCode_Type(Integer32):
    """Custom type juniClassifierControlListICMPCode based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListICMPCode_Type.__name__ = "Integer32"
_JuniClassifierControlListICMPCode_Object = MibTableColumn
juniClassifierControlListICMPCode = _JuniClassifierControlListICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 20),
    _JuniClassifierControlListICMPCode_Type()
)
juniClassifierControlListICMPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListICMPCode.setStatus("current")


class _JuniClassifierControlListIGMPType_Type(Integer32):
    """Custom type juniClassifierControlListIGMPType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListIGMPType_Type.__name__ = "Integer32"
_JuniClassifierControlListIGMPType_Object = MibTableColumn
juniClassifierControlListIGMPType = _JuniClassifierControlListIGMPType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 21),
    _JuniClassifierControlListIGMPType_Type()
)
juniClassifierControlListIGMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListIGMPType.setStatus("current")


class _JuniClassifierControlListTcpFlagsValue_Type(Integer32):
    """Custom type juniClassifierControlListTcpFlagsValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JuniClassifierControlListTcpFlagsValue_Type.__name__ = "Integer32"
_JuniClassifierControlListTcpFlagsValue_Object = MibTableColumn
juniClassifierControlListTcpFlagsValue = _JuniClassifierControlListTcpFlagsValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 22),
    _JuniClassifierControlListTcpFlagsValue_Type()
)
juniClassifierControlListTcpFlagsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListTcpFlagsValue.setStatus("current")


class _JuniClassifierControlListTcpFlagsMask_Type(Integer32):
    """Custom type juniClassifierControlListTcpFlagsMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JuniClassifierControlListTcpFlagsMask_Type.__name__ = "Integer32"
_JuniClassifierControlListTcpFlagsMask_Object = MibTableColumn
juniClassifierControlListTcpFlagsMask = _JuniClassifierControlListTcpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 23),
    _JuniClassifierControlListTcpFlagsMask_Type()
)
juniClassifierControlListTcpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListTcpFlagsMask.setStatus("current")


class _JuniClassifierControlListIpFlagsValue_Type(Integer32):
    """Custom type juniClassifierControlListIpFlagsValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JuniClassifierControlListIpFlagsValue_Type.__name__ = "Integer32"
_JuniClassifierControlListIpFlagsValue_Object = MibTableColumn
juniClassifierControlListIpFlagsValue = _JuniClassifierControlListIpFlagsValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 24),
    _JuniClassifierControlListIpFlagsValue_Type()
)
juniClassifierControlListIpFlagsValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListIpFlagsValue.setStatus("current")


class _JuniClassifierControlListIpFlagsMask_Type(Integer32):
    """Custom type juniClassifierControlListIpFlagsMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JuniClassifierControlListIpFlagsMask_Type.__name__ = "Integer32"
_JuniClassifierControlListIpFlagsMask_Object = MibTableColumn
juniClassifierControlListIpFlagsMask = _JuniClassifierControlListIpFlagsMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 25),
    _JuniClassifierControlListIpFlagsMask_Type()
)
juniClassifierControlListIpFlagsMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListIpFlagsMask.setStatus("current")


class _JuniClassifierControlListIpFragValue_Type(JuniPolicyIpFragValue):
    """Custom type juniClassifierControlListIpFragValue based on JuniPolicyIpFragValue"""


_JuniClassifierControlListIpFragValue_Object = MibTableColumn
juniClassifierControlListIpFragValue = _JuniClassifierControlListIpFragValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 26),
    _JuniClassifierControlListIpFragValue_Type()
)
juniClassifierControlListIpFragValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListIpFragValue.setStatus("current")


class _JuniClassifierControlListLocal_Type(TruthValue):
    """Custom type juniClassifierControlListLocal based on TruthValue"""


_JuniClassifierControlListLocal_Object = MibTableColumn
juniClassifierControlListLocal = _JuniClassifierControlListLocal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 27),
    _JuniClassifierControlListLocal_Type()
)
juniClassifierControlListLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListLocal.setStatus("current")


class _JuniClassifierControlListLocalPresent_Type(TruthValue):
    """Custom type juniClassifierControlListLocalPresent based on TruthValue"""


_JuniClassifierControlListLocalPresent_Object = MibTableColumn
juniClassifierControlListLocalPresent = _JuniClassifierControlListLocalPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 28),
    _JuniClassifierControlListLocalPresent_Type()
)
juniClassifierControlListLocalPresent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListLocalPresent.setStatus("current")


class _JuniClassifierControlListSaRouteClass_Type(Integer32):
    """Custom type juniClassifierControlListSaRouteClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListSaRouteClass_Type.__name__ = "Integer32"
_JuniClassifierControlListSaRouteClass_Object = MibTableColumn
juniClassifierControlListSaRouteClass = _JuniClassifierControlListSaRouteClass_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 29),
    _JuniClassifierControlListSaRouteClass_Type()
)
juniClassifierControlListSaRouteClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListSaRouteClass.setStatus("current")


class _JuniClassifierControlListSaRouteClassPresent_Type(TruthValue):
    """Custom type juniClassifierControlListSaRouteClassPresent based on TruthValue"""


_JuniClassifierControlListSaRouteClassPresent_Object = MibTableColumn
juniClassifierControlListSaRouteClassPresent = _JuniClassifierControlListSaRouteClassPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 30),
    _JuniClassifierControlListSaRouteClassPresent_Type()
)
juniClassifierControlListSaRouteClassPresent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListSaRouteClassPresent.setStatus("current")


class _JuniClassifierControlListDaRouteClass_Type(Integer32):
    """Custom type juniClassifierControlListDaRouteClass based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniClassifierControlListDaRouteClass_Type.__name__ = "Integer32"
_JuniClassifierControlListDaRouteClass_Object = MibTableColumn
juniClassifierControlListDaRouteClass = _JuniClassifierControlListDaRouteClass_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 31),
    _JuniClassifierControlListDaRouteClass_Type()
)
juniClassifierControlListDaRouteClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListDaRouteClass.setStatus("current")


class _JuniClassifierControlListDaRouteClassPresent_Type(TruthValue):
    """Custom type juniClassifierControlListDaRouteClassPresent based on TruthValue"""


_JuniClassifierControlListDaRouteClassPresent_Object = MibTableColumn
juniClassifierControlListDaRouteClassPresent = _JuniClassifierControlListDaRouteClassPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 1, 4, 1, 32),
    _JuniClassifierControlListDaRouteClassPresent_Type()
)
juniClassifierControlListDaRouteClassPresent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniClassifierControlListDaRouteClassPresent.setStatus("current")
_JuniRateLimitControlList_ObjectIdentity = ObjectIdentity
juniRateLimitControlList = _JuniRateLimitControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2)
)


class _JuniRateLimitProfileNextIndex_Type(Integer32):
    """Custom type juniRateLimitProfileNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniRateLimitProfileNextIndex_Type.__name__ = "Integer32"
_JuniRateLimitProfileNextIndex_Object = MibScalar
juniRateLimitProfileNextIndex = _JuniRateLimitProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 1),
    _JuniRateLimitProfileNextIndex_Type()
)
juniRateLimitProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRateLimitProfileNextIndex.setStatus("current")
_JuniRateLimitProfileTable_Object = MibTable
juniRateLimitProfileTable = _JuniRateLimitProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2)
)
if mibBuilder.loadTexts:
    juniRateLimitProfileTable.setStatus("current")
_JuniRateLimitProfileEntry_Object = MibTableRow
juniRateLimitProfileEntry = _JuniRateLimitProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1)
)
juniRateLimitProfileEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniRateLimitProfileId"),
)
if mibBuilder.loadTexts:
    juniRateLimitProfileEntry.setStatus("current")


class _JuniRateLimitProfileId_Type(Integer32):
    """Custom type juniRateLimitProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniRateLimitProfileId_Type.__name__ = "Integer32"
_JuniRateLimitProfileId_Object = MibTableColumn
juniRateLimitProfileId = _JuniRateLimitProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 1),
    _JuniRateLimitProfileId_Type()
)
juniRateLimitProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRateLimitProfileId.setStatus("current")
_JuniRateLimitProfileRowStatus_Type = RowStatus
_JuniRateLimitProfileRowStatus_Object = MibTableColumn
juniRateLimitProfileRowStatus = _JuniRateLimitProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 2),
    _JuniRateLimitProfileRowStatus_Type()
)
juniRateLimitProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitProfileRowStatus.setStatus("current")


class _JuniRateLimitProfileName_Type(DisplayString):
    """Custom type juniRateLimitProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_JuniRateLimitProfileName_Type.__name__ = "DisplayString"
_JuniRateLimitProfileName_Object = MibTableColumn
juniRateLimitProfileName = _JuniRateLimitProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 3),
    _JuniRateLimitProfileName_Type()
)
juniRateLimitProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitProfileName.setStatus("current")
_JuniRateLimitReferenceCount_Type = Counter32
_JuniRateLimitReferenceCount_Object = MibTableColumn
juniRateLimitReferenceCount = _JuniRateLimitReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 4),
    _JuniRateLimitReferenceCount_Type()
)
juniRateLimitReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRateLimitReferenceCount.setStatus("current")


class _JuniRateLimitCommittedBps_Type(Unsigned32):
    """Custom type juniRateLimitCommittedBps based on Unsigned32"""
    defaultValue = 0


_JuniRateLimitCommittedBps_Object = MibTableColumn
juniRateLimitCommittedBps = _JuniRateLimitCommittedBps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 5),
    _JuniRateLimitCommittedBps_Type()
)
juniRateLimitCommittedBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitCommittedBps.setStatus("current")
if mibBuilder.loadTexts:
    juniRateLimitCommittedBps.setUnits("bits per second")


class _JuniRateLimitCommittedBurst_Type(Unsigned32):
    """Custom type juniRateLimitCommittedBurst based on Unsigned32"""
    defaultValue = 8192


_JuniRateLimitCommittedBurst_Object = MibTableColumn
juniRateLimitCommittedBurst = _JuniRateLimitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 6),
    _JuniRateLimitCommittedBurst_Type()
)
juniRateLimitCommittedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitCommittedBurst.setStatus("current")
if mibBuilder.loadTexts:
    juniRateLimitCommittedBurst.setUnits("bytes")


class _JuniRateLimitExceedBps_Type(Unsigned32):
    """Custom type juniRateLimitExceedBps based on Unsigned32"""
    defaultValue = 0


_JuniRateLimitExceedBps_Object = MibTableColumn
juniRateLimitExceedBps = _JuniRateLimitExceedBps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 7),
    _JuniRateLimitExceedBps_Type()
)
juniRateLimitExceedBps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitExceedBps.setStatus("current")
if mibBuilder.loadTexts:
    juniRateLimitExceedBps.setUnits("bits per second")


class _JuniRateLimitExceedBurst_Type(Unsigned32):
    """Custom type juniRateLimitExceedBurst based on Unsigned32"""
    defaultValue = 8192


_JuniRateLimitExceedBurst_Object = MibTableColumn
juniRateLimitExceedBurst = _JuniRateLimitExceedBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 8),
    _JuniRateLimitExceedBurst_Type()
)
juniRateLimitExceedBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitExceedBurst.setStatus("current")
if mibBuilder.loadTexts:
    juniRateLimitExceedBurst.setUnits("bytes")


class _JuniRateLimitCommittedAction_Type(Integer32):
    """Custom type juniRateLimitCommittedAction based on Integer32"""
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


_JuniRateLimitCommittedAction_Type.__name__ = "Integer32"
_JuniRateLimitCommittedAction_Object = MibTableColumn
juniRateLimitCommittedAction = _JuniRateLimitCommittedAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 9),
    _JuniRateLimitCommittedAction_Type()
)
juniRateLimitCommittedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitCommittedAction.setStatus("current")


class _JuniRateLimitConformedAction_Type(Integer32):
    """Custom type juniRateLimitConformedAction based on Integer32"""
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


_JuniRateLimitConformedAction_Type.__name__ = "Integer32"
_JuniRateLimitConformedAction_Object = MibTableColumn
juniRateLimitConformedAction = _JuniRateLimitConformedAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 10),
    _JuniRateLimitConformedAction_Type()
)
juniRateLimitConformedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitConformedAction.setStatus("current")


class _JuniRateLimitExceededAction_Type(Integer32):
    """Custom type juniRateLimitExceededAction based on Integer32"""
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


_JuniRateLimitExceededAction_Type.__name__ = "Integer32"
_JuniRateLimitExceededAction_Object = MibTableColumn
juniRateLimitExceededAction = _JuniRateLimitExceededAction_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 11),
    _JuniRateLimitExceededAction_Type()
)
juniRateLimitExceededAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitExceededAction.setStatus("current")


class _JuniRateLimitCommittedMarkVal_Type(Integer32):
    """Custom type juniRateLimitCommittedMarkVal based on Integer32"""
    defaultValue = 0


_JuniRateLimitCommittedMarkVal_Object = MibTableColumn
juniRateLimitCommittedMarkVal = _JuniRateLimitCommittedMarkVal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 12),
    _JuniRateLimitCommittedMarkVal_Type()
)
juniRateLimitCommittedMarkVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitCommittedMarkVal.setStatus("current")


class _JuniRateLimitConformedMarkVal_Type(Integer32):
    """Custom type juniRateLimitConformedMarkVal based on Integer32"""
    defaultValue = 0


_JuniRateLimitConformedMarkVal_Object = MibTableColumn
juniRateLimitConformedMarkVal = _JuniRateLimitConformedMarkVal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 13),
    _JuniRateLimitConformedMarkVal_Type()
)
juniRateLimitConformedMarkVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitConformedMarkVal.setStatus("current")


class _JuniRateLimitExceededMarkVal_Type(Integer32):
    """Custom type juniRateLimitExceededMarkVal based on Integer32"""
    defaultValue = 0


_JuniRateLimitExceededMarkVal_Object = MibTableColumn
juniRateLimitExceededMarkVal = _JuniRateLimitExceededMarkVal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 14),
    _JuniRateLimitExceededMarkVal_Type()
)
juniRateLimitExceededMarkVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitExceededMarkVal.setStatus("current")


class _JuniRateLimitMask_Type(Unsigned32):
    """Custom type juniRateLimitMask based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniRateLimitMask_Type.__name__ = "Unsigned32"
_JuniRateLimitMask_Object = MibTableColumn
juniRateLimitMask = _JuniRateLimitMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 15),
    _JuniRateLimitMask_Type()
)
juniRateLimitMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitMask.setStatus("current")


class _JuniRateLimitProfileType_Type(JuniRateLimitProfileType):
    """Custom type juniRateLimitProfileType based on JuniRateLimitProfileType"""


_JuniRateLimitProfileType_Object = MibTableColumn
juniRateLimitProfileType = _JuniRateLimitProfileType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 16),
    _JuniRateLimitProfileType_Type()
)
juniRateLimitProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitProfileType.setStatus("current")


class _JuniRateLimitExcessBurst_Type(Unsigned32):
    """Custom type juniRateLimitExcessBurst based on Unsigned32"""
    defaultValue = 0


_JuniRateLimitExcessBurst_Object = MibTableColumn
juniRateLimitExcessBurst = _JuniRateLimitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 2, 2, 1, 17),
    _JuniRateLimitExcessBurst_Type()
)
juniRateLimitExcessBurst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRateLimitExcessBurst.setStatus("current")
if mibBuilder.loadTexts:
    juniRateLimitExcessBurst.setUnits("bytes")
_JuniPolicy_ObjectIdentity = ObjectIdentity
juniPolicy = _JuniPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3)
)


class _JuniPolicyNextIndex_Type(Integer32):
    """Custom type juniPolicyNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyNextIndex_Type.__name__ = "Integer32"
_JuniPolicyNextIndex_Object = MibScalar
juniPolicyNextIndex = _JuniPolicyNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 1),
    _JuniPolicyNextIndex_Type()
)
juniPolicyNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyNextIndex.setStatus("current")
_JuniPolicyTable_Object = MibTable
juniPolicyTable = _JuniPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniPolicyTable.setStatus("current")
_JuniPolicyEntry_Object = MibTableRow
juniPolicyEntry = _JuniPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1)
)
juniPolicyEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyId"),
)
if mibBuilder.loadTexts:
    juniPolicyEntry.setStatus("current")


class _JuniPolicyId_Type(Integer32):
    """Custom type juniPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyId_Type.__name__ = "Integer32"
_JuniPolicyId_Object = MibTableColumn
juniPolicyId = _JuniPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 1),
    _JuniPolicyId_Type()
)
juniPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyId.setStatus("current")
_JuniPolicyRowStatus_Type = RowStatus
_JuniPolicyRowStatus_Object = MibTableColumn
juniPolicyRowStatus = _JuniPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 2),
    _JuniPolicyRowStatus_Type()
)
juniPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyRowStatus.setStatus("current")


class _JuniPolicyAdminState_Type(Integer32):
    """Custom type juniPolicyAdminState based on Integer32"""
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


_JuniPolicyAdminState_Type.__name__ = "Integer32"
_JuniPolicyAdminState_Object = MibTableColumn
juniPolicyAdminState = _JuniPolicyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 3),
    _JuniPolicyAdminState_Type()
)
juniPolicyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyAdminState.setStatus("current")


class _JuniPolicyOperStatus_Type(Integer32):
    """Custom type juniPolicyOperStatus based on Integer32"""
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


_JuniPolicyOperStatus_Type.__name__ = "Integer32"
_JuniPolicyOperStatus_Object = MibTableColumn
juniPolicyOperStatus = _JuniPolicyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 4),
    _JuniPolicyOperStatus_Type()
)
juniPolicyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyOperStatus.setStatus("obsolete")
_JuniPolicyErrorValue_Type = Integer32
_JuniPolicyErrorValue_Object = MibTableColumn
juniPolicyErrorValue = _JuniPolicyErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 5),
    _JuniPolicyErrorValue_Type()
)
juniPolicyErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyErrorValue.setStatus("obsolete")


class _JuniPolicyName_Type(DisplayString):
    """Custom type juniPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_JuniPolicyName_Type.__name__ = "DisplayString"
_JuniPolicyName_Object = MibTableColumn
juniPolicyName = _JuniPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 6),
    _JuniPolicyName_Type()
)
juniPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyName.setStatus("current")
_JuniPolicyReferenceCount_Type = Counter32
_JuniPolicyReferenceCount_Object = MibTableColumn
juniPolicyReferenceCount = _JuniPolicyReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 7),
    _JuniPolicyReferenceCount_Type()
)
juniPolicyReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyReferenceCount.setStatus("current")


class _JuniPolicyRuleNextIndex_Type(Integer32):
    """Custom type juniPolicyRuleNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyRuleNextIndex_Type.__name__ = "Integer32"
_JuniPolicyRuleNextIndex_Object = MibTableColumn
juniPolicyRuleNextIndex = _JuniPolicyRuleNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 8),
    _JuniPolicyRuleNextIndex_Type()
)
juniPolicyRuleNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyRuleNextIndex.setStatus("current")
_JuniPolicyAtmCellModeEnable_Type = TruthValue
_JuniPolicyAtmCellModeEnable_Object = MibTableColumn
juniPolicyAtmCellModeEnable = _JuniPolicyAtmCellModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 2, 1, 9),
    _JuniPolicyAtmCellModeEnable_Type()
)
juniPolicyAtmCellModeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyAtmCellModeEnable.setStatus("current")
_JuniPolicyRuleTable_Object = MibTable
juniPolicyRuleTable = _JuniPolicyRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniPolicyRuleTable.setStatus("deprecated")
_JuniPolicyRuleEntry_Object = MibTableRow
juniPolicyRuleEntry = _JuniPolicyRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1)
)
juniPolicyRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniPolicyRuleEntry.setStatus("deprecated")


class _JuniPolicyRulePolicyId_Type(Integer32):
    """Custom type juniPolicyRulePolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyRulePolicyId_Type.__name__ = "Integer32"
_JuniPolicyRulePolicyId_Object = MibTableColumn
juniPolicyRulePolicyId = _JuniPolicyRulePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 1),
    _JuniPolicyRulePolicyId_Type()
)
juniPolicyRulePolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyRulePolicyId.setStatus("deprecated")


class _JuniPolicyRulePrec_Type(Integer32):
    """Custom type juniPolicyRulePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyRulePrec_Type.__name__ = "Integer32"
_JuniPolicyRulePrec_Object = MibTableColumn
juniPolicyRulePrec = _JuniPolicyRulePrec_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 2),
    _JuniPolicyRulePrec_Type()
)
juniPolicyRulePrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyRulePrec.setStatus("deprecated")


class _JuniPolicyRuleId_Type(Integer32):
    """Custom type juniPolicyRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyRuleId_Type.__name__ = "Integer32"
_JuniPolicyRuleId_Object = MibTableColumn
juniPolicyRuleId = _JuniPolicyRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 3),
    _JuniPolicyRuleId_Type()
)
juniPolicyRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyRuleId.setStatus("deprecated")


class _JuniPolicyRuleType_Type(Integer32):
    """Custom type juniPolicyRuleType based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("colorRule", 10),
          ("exceptionRule", 11),
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


_JuniPolicyRuleType_Type.__name__ = "Integer32"
_JuniPolicyRuleType_Object = MibTableColumn
juniPolicyRuleType = _JuniPolicyRuleType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 4),
    _JuniPolicyRuleType_Type()
)
juniPolicyRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyRuleType.setStatus("deprecated")


class _JuniPolicySuspend_Type(TruthValue):
    """Custom type juniPolicySuspend based on TruthValue"""


_JuniPolicySuspend_Object = MibTableColumn
juniPolicySuspend = _JuniPolicySuspend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 5),
    _JuniPolicySuspend_Type()
)
juniPolicySuspend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPolicySuspend.setStatus("deprecated")
_JuniPolicyEclipsed_Type = TruthValue
_JuniPolicyEclipsed_Object = MibTableColumn
juniPolicyEclipsed = _JuniPolicyEclipsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 3, 1, 6),
    _JuniPolicyEclipsed_Type()
)
juniPolicyEclipsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyEclipsed.setStatus("deprecated")
_JuniNextHopRuleTable_Object = MibTable
juniNextHopRuleTable = _JuniNextHopRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4)
)
if mibBuilder.loadTexts:
    juniNextHopRuleTable.setStatus("deprecated")
_JuniNextHopRuleEntry_Object = MibTableRow
juniNextHopRuleEntry = _JuniNextHopRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1)
)
juniNextHopRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniNextHopRuleEntry.setStatus("deprecated")
_JuniNextHopRowStatus_Type = RowStatus
_JuniNextHopRowStatus_Object = MibTableColumn
juniNextHopRowStatus = _JuniNextHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1, 1),
    _JuniNextHopRowStatus_Type()
)
juniNextHopRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextHopRowStatus.setStatus("deprecated")


class _JuniNextHopIpAddress_Type(IpAddress):
    """Custom type juniNextHopIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_JuniNextHopIpAddress_Object = MibTableColumn
juniNextHopIpAddress = _JuniNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1, 2),
    _JuniNextHopIpAddress_Type()
)
juniNextHopIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextHopIpAddress.setStatus("deprecated")


class _JuniNextHopClaclId_Type(Integer32):
    """Custom type juniNextHopClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniNextHopClaclId_Type.__name__ = "Integer32"
_JuniNextHopClaclId_Object = MibTableColumn
juniNextHopClaclId = _JuniNextHopClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 4, 1, 3),
    _JuniNextHopClaclId_Type()
)
juniNextHopClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextHopClaclId.setStatus("deprecated")
_JuniFilterRuleTable_Object = MibTable
juniFilterRuleTable = _JuniFilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5)
)
if mibBuilder.loadTexts:
    juniFilterRuleTable.setStatus("deprecated")
_JuniFilterRuleEntry_Object = MibTableRow
juniFilterRuleEntry = _JuniFilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5, 1)
)
juniFilterRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniFilterRuleEntry.setStatus("deprecated")
_JuniFilterRowStatus_Type = RowStatus
_JuniFilterRowStatus_Object = MibTableColumn
juniFilterRowStatus = _JuniFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5, 1, 1),
    _JuniFilterRowStatus_Type()
)
juniFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFilterRowStatus.setStatus("deprecated")


class _JuniFilterClaclId_Type(Integer32):
    """Custom type juniFilterClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniFilterClaclId_Type.__name__ = "Integer32"
_JuniFilterClaclId_Object = MibTableColumn
juniFilterClaclId = _JuniFilterClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 5, 1, 2),
    _JuniFilterClaclId_Type()
)
juniFilterClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFilterClaclId.setStatus("deprecated")
_JuniNextInterfaceRuleTable_Object = MibTable
juniNextInterfaceRuleTable = _JuniNextInterfaceRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6)
)
if mibBuilder.loadTexts:
    juniNextInterfaceRuleTable.setStatus("deprecated")
_JuniNextInterfaceRuleEntry_Object = MibTableRow
juniNextInterfaceRuleEntry = _JuniNextInterfaceRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1)
)
juniNextInterfaceRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniNextInterfaceRuleEntry.setStatus("deprecated")
_JuniNextInterfaceRowStatus_Type = RowStatus
_JuniNextInterfaceRowStatus_Object = MibTableColumn
juniNextInterfaceRowStatus = _JuniNextInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 1),
    _JuniNextInterfaceRowStatus_Type()
)
juniNextInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextInterfaceRowStatus.setStatus("deprecated")
_JuniNextInterfaceId_Type = InterfaceIndex
_JuniNextInterfaceId_Object = MibTableColumn
juniNextInterfaceId = _JuniNextInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 2),
    _JuniNextInterfaceId_Type()
)
juniNextInterfaceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextInterfaceId.setStatus("deprecated")


class _JuniNextInterfaceClaclId_Type(Integer32):
    """Custom type juniNextInterfaceClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniNextInterfaceClaclId_Type.__name__ = "Integer32"
_JuniNextInterfaceClaclId_Object = MibTableColumn
juniNextInterfaceClaclId = _JuniNextInterfaceClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 3),
    _JuniNextInterfaceClaclId_Type()
)
juniNextInterfaceClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextInterfaceClaclId.setStatus("deprecated")


class _JuniNextInterfaceNextHop_Type(IpAddress):
    """Custom type juniNextInterfaceNextHop based on IpAddress"""
    defaultHexValue = "00000000"


_JuniNextInterfaceNextHop_Object = MibTableColumn
juniNextInterfaceNextHop = _JuniNextInterfaceNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 6, 1, 4),
    _JuniNextInterfaceNextHop_Type()
)
juniNextInterfaceNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextInterfaceNextHop.setStatus("deprecated")
_JuniRateLimitRuleTable_Object = MibTable
juniRateLimitRuleTable = _JuniRateLimitRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7)
)
if mibBuilder.loadTexts:
    juniRateLimitRuleTable.setStatus("deprecated")
_JuniRateLimitRuleEntry_Object = MibTableRow
juniRateLimitRuleEntry = _JuniRateLimitRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1)
)
juniRateLimitRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniRateLimitRuleEntry.setStatus("deprecated")
_JuniRateLimitRowStatus_Type = RowStatus
_JuniRateLimitRowStatus_Object = MibTableColumn
juniRateLimitRowStatus = _JuniRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1, 1),
    _JuniRateLimitRowStatus_Type()
)
juniRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRateLimitRowStatus.setStatus("deprecated")


class _JuniRateLimitId_Type(Integer32):
    """Custom type juniRateLimitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniRateLimitId_Type.__name__ = "Integer32"
_JuniRateLimitId_Object = MibTableColumn
juniRateLimitId = _JuniRateLimitId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1, 2),
    _JuniRateLimitId_Type()
)
juniRateLimitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRateLimitId.setStatus("deprecated")


class _JuniRateLimitClaclId_Type(Integer32):
    """Custom type juniRateLimitClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniRateLimitClaclId_Type.__name__ = "Integer32"
_JuniRateLimitClaclId_Object = MibTableColumn
juniRateLimitClaclId = _JuniRateLimitClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 7, 1, 3),
    _JuniRateLimitClaclId_Type()
)
juniRateLimitClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRateLimitClaclId.setStatus("deprecated")
_JuniMarkingRuleTable_Object = MibTable
juniMarkingRuleTable = _JuniMarkingRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8)
)
if mibBuilder.loadTexts:
    juniMarkingRuleTable.setStatus("deprecated")
_JuniMarkingRuleEntry_Object = MibTableRow
juniMarkingRuleEntry = _JuniMarkingRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1)
)
juniMarkingRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniMarkingRuleEntry.setStatus("deprecated")
_JuniMarkingRowStatus_Type = RowStatus
_JuniMarkingRowStatus_Object = MibTableColumn
juniMarkingRowStatus = _JuniMarkingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 1),
    _JuniMarkingRowStatus_Type()
)
juniMarkingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMarkingRowStatus.setStatus("deprecated")


class _JuniMarkingTOSByte_Type(Integer32):
    """Custom type juniMarkingTOSByte based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniMarkingTOSByte_Type.__name__ = "Integer32"
_JuniMarkingTOSByte_Object = MibTableColumn
juniMarkingTOSByte = _JuniMarkingTOSByte_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 2),
    _JuniMarkingTOSByte_Type()
)
juniMarkingTOSByte.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMarkingTOSByte.setStatus("deprecated")


class _JuniMarkingMask_Type(Integer32):
    """Custom type juniMarkingMask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniMarkingMask_Type.__name__ = "Integer32"
_JuniMarkingMask_Object = MibTableColumn
juniMarkingMask = _JuniMarkingMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 3),
    _JuniMarkingMask_Type()
)
juniMarkingMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMarkingMask.setStatus("deprecated")


class _JuniMarkingClaclId_Type(Integer32):
    """Custom type juniMarkingClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniMarkingClaclId_Type.__name__ = "Integer32"
_JuniMarkingClaclId_Object = MibTableColumn
juniMarkingClaclId = _JuniMarkingClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 8, 1, 4),
    _JuniMarkingClaclId_Type()
)
juniMarkingClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMarkingClaclId.setStatus("deprecated")
_JuniForwardRuleTable_Object = MibTable
juniForwardRuleTable = _JuniForwardRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9)
)
if mibBuilder.loadTexts:
    juniForwardRuleTable.setStatus("deprecated")
_JuniForwardRuleEntry_Object = MibTableRow
juniForwardRuleEntry = _JuniForwardRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1)
)
juniForwardRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniForwardRuleEntry.setStatus("deprecated")
_JuniForwardRowStatus_Type = RowStatus
_JuniForwardRowStatus_Object = MibTableColumn
juniForwardRowStatus = _JuniForwardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 1),
    _JuniForwardRowStatus_Type()
)
juniForwardRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardRowStatus.setStatus("deprecated")


class _JuniForwardClaclId_Type(Integer32):
    """Custom type juniForwardClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniForwardClaclId_Type.__name__ = "Integer32"
_JuniForwardClaclId_Object = MibTableColumn
juniForwardClaclId = _JuniForwardClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 2),
    _JuniForwardClaclId_Type()
)
juniForwardClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardClaclId.setStatus("deprecated")
_JuniForwardNextInterfaceId_Type = InterfaceIndex
_JuniForwardNextInterfaceId_Object = MibTableColumn
juniForwardNextInterfaceId = _JuniForwardNextInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 3),
    _JuniForwardNextInterfaceId_Type()
)
juniForwardNextInterfaceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardNextInterfaceId.setStatus("deprecated")


class _JuniForwardNextHop_Type(IpAddress):
    """Custom type juniForwardNextHop based on IpAddress"""
    defaultHexValue = "00000000"


_JuniForwardNextHop_Object = MibTableColumn
juniForwardNextHop = _JuniForwardNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 4),
    _JuniForwardNextHop_Type()
)
juniForwardNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardNextHop.setStatus("deprecated")


class _JuniForwardRouterId_Type(Integer32):
    """Custom type juniForwardRouterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniForwardRouterId_Type.__name__ = "Integer32"
_JuniForwardRouterId_Object = MibTableColumn
juniForwardRouterId = _JuniForwardRouterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 5),
    _JuniForwardRouterId_Type()
)
juniForwardRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniForwardRouterId.setStatus("deprecated")


class _JuniForwardOrder_Type(Integer32):
    """Custom type juniForwardOrder based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_JuniForwardOrder_Type.__name__ = "Integer32"
_JuniForwardOrder_Object = MibTableColumn
juniForwardOrder = _JuniForwardOrder_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 6),
    _JuniForwardOrder_Type()
)
juniForwardOrder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardOrder.setStatus("deprecated")


class _JuniForwardIgnoreDefaultRoute_Type(TruthValue):
    """Custom type juniForwardIgnoreDefaultRoute based on TruthValue"""


_JuniForwardIgnoreDefaultRoute_Object = MibTableColumn
juniForwardIgnoreDefaultRoute = _JuniForwardIgnoreDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 9, 1, 7),
    _JuniForwardIgnoreDefaultRoute_Type()
)
juniForwardIgnoreDefaultRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardIgnoreDefaultRoute.setStatus("deprecated")
_JuniTrafficShapeRuleTable_Object = MibTable
juniTrafficShapeRuleTable = _JuniTrafficShapeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10)
)
if mibBuilder.loadTexts:
    juniTrafficShapeRuleTable.setStatus("obsolete")
_JuniTrafficShapeRuleEntry_Object = MibTableRow
juniTrafficShapeRuleEntry = _JuniTrafficShapeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10, 1)
)
juniTrafficShapeRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniTrafficShapeRuleEntry.setStatus("obsolete")
_JuniTrafficShapeRowStatus_Type = RowStatus
_JuniTrafficShapeRowStatus_Object = MibTableColumn
juniTrafficShapeRowStatus = _JuniTrafficShapeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10, 1, 1),
    _JuniTrafficShapeRowStatus_Type()
)
juniTrafficShapeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficShapeRowStatus.setStatus("obsolete")


class _JuniTrafficShapeId_Type(Integer32):
    """Custom type juniTrafficShapeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniTrafficShapeId_Type.__name__ = "Integer32"
_JuniTrafficShapeId_Object = MibTableColumn
juniTrafficShapeId = _JuniTrafficShapeId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 10, 1, 2),
    _JuniTrafficShapeId_Type()
)
juniTrafficShapeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficShapeId.setStatus("obsolete")
_JuniColorRuleTable_Object = MibTable
juniColorRuleTable = _JuniColorRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11)
)
if mibBuilder.loadTexts:
    juniColorRuleTable.setStatus("deprecated")
_JuniColorRuleEntry_Object = MibTableRow
juniColorRuleEntry = _JuniColorRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1)
)
juniColorRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniColorRuleEntry.setStatus("deprecated")
_JuniColorRowStatus_Type = RowStatus
_JuniColorRowStatus_Object = MibTableColumn
juniColorRowStatus = _JuniColorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1, 1),
    _JuniColorRowStatus_Type()
)
juniColorRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniColorRowStatus.setStatus("deprecated")


class _JuniColor_Type(Integer32):
    """Custom type juniColor based on Integer32"""
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


_JuniColor_Type.__name__ = "Integer32"
_JuniColor_Object = MibTableColumn
juniColor = _JuniColor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1, 2),
    _JuniColor_Type()
)
juniColor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniColor.setStatus("deprecated")


class _JuniColorClaclId_Type(Integer32):
    """Custom type juniColorClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniColorClaclId_Type.__name__ = "Integer32"
_JuniColorClaclId_Object = MibTableColumn
juniColorClaclId = _JuniColorClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 11, 1, 3),
    _JuniColorClaclId_Type()
)
juniColorClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniColorClaclId.setStatus("deprecated")
_JuniLogRuleTable_Object = MibTable
juniLogRuleTable = _JuniLogRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12)
)
if mibBuilder.loadTexts:
    juniLogRuleTable.setStatus("deprecated")
_JuniLogRuleEntry_Object = MibTableRow
juniLogRuleEntry = _JuniLogRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12, 1)
)
juniLogRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniLogRuleEntry.setStatus("deprecated")
_JuniLogRowStatus_Type = RowStatus
_JuniLogRowStatus_Object = MibTableColumn
juniLogRowStatus = _JuniLogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12, 1, 1),
    _JuniLogRowStatus_Type()
)
juniLogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniLogRowStatus.setStatus("deprecated")


class _JuniLogClaclId_Type(Integer32):
    """Custom type juniLogClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniLogClaclId_Type.__name__ = "Integer32"
_JuniLogClaclId_Object = MibTableColumn
juniLogClaclId = _JuniLogClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 12, 1, 2),
    _JuniLogClaclId_Type()
)
juniLogClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniLogClaclId.setStatus("deprecated")
_JuniTrafficClassRuleTable_Object = MibTable
juniTrafficClassRuleTable = _JuniTrafficClassRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13)
)
if mibBuilder.loadTexts:
    juniTrafficClassRuleTable.setStatus("deprecated")
_JuniTrafficClassRuleEntry_Object = MibTableRow
juniTrafficClassRuleEntry = _JuniTrafficClassRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1)
)
juniTrafficClassRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId"),
)
if mibBuilder.loadTexts:
    juniTrafficClassRuleEntry.setStatus("deprecated")
_JuniTrafficClassRowStatus_Type = RowStatus
_JuniTrafficClassRowStatus_Object = MibTableColumn
juniTrafficClassRowStatus = _JuniTrafficClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1, 1),
    _JuniTrafficClassRowStatus_Type()
)
juniTrafficClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficClassRowStatus.setStatus("deprecated")


class _JuniTrafficClassId_Type(Integer32):
    """Custom type juniTrafficClassId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniTrafficClassId_Type.__name__ = "Integer32"
_JuniTrafficClassId_Object = MibTableColumn
juniTrafficClassId = _JuniTrafficClassId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1, 2),
    _JuniTrafficClassId_Type()
)
juniTrafficClassId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficClassId.setStatus("deprecated")


class _JuniTrafficClassClaclId_Type(Integer32):
    """Custom type juniTrafficClassClaclId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniTrafficClassClaclId_Type.__name__ = "Integer32"
_JuniTrafficClassClaclId_Object = MibTableColumn
juniTrafficClassClaclId = _JuniTrafficClassClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 13, 1, 3),
    _JuniTrafficClassClaclId_Type()
)
juniTrafficClassClaclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficClassClaclId.setStatus("deprecated")
_JuniPolicyRule2Table_Object = MibTable
juniPolicyRule2Table = _JuniPolicyRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 14)
)
if mibBuilder.loadTexts:
    juniPolicyRule2Table.setStatus("current")
_JuniPolicyRule2Entry_Object = MibTableRow
juniPolicyRule2Entry = _JuniPolicyRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 14, 1)
)
juniPolicyRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniPolicyRule2Entry.setStatus("current")


class _JuniPolicyRulePolicyId2_Type(Integer32):
    """Custom type juniPolicyRulePolicyId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyRulePolicyId2_Type.__name__ = "Integer32"
_JuniPolicyRulePolicyId2_Object = MibTableColumn
juniPolicyRulePolicyId2 = _JuniPolicyRulePolicyId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 14, 1, 1),
    _JuniPolicyRulePolicyId2_Type()
)
juniPolicyRulePolicyId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyRulePolicyId2.setStatus("current")


class _JuniPolicyRuleClaclId_Type(Integer32):
    """Custom type juniPolicyRuleClaclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyRuleClaclId_Type.__name__ = "Integer32"
_JuniPolicyRuleClaclId_Object = MibTableColumn
juniPolicyRuleClaclId = _JuniPolicyRuleClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 14, 1, 2),
    _JuniPolicyRuleClaclId_Type()
)
juniPolicyRuleClaclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyRuleClaclId.setStatus("current")


class _JuniPolicyRuleId2_Type(Integer32):
    """Custom type juniPolicyRuleId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyRuleId2_Type.__name__ = "Integer32"
_JuniPolicyRuleId2_Object = MibTableColumn
juniPolicyRuleId2 = _JuniPolicyRuleId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 14, 1, 3),
    _JuniPolicyRuleId2_Type()
)
juniPolicyRuleId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyRuleId2.setStatus("current")


class _JuniPolicyRuleType2_Type(Integer32):
    """Custom type juniPolicyRuleType2 based on Integer32"""
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("colorRule", 10),
          ("exceptionRule", 11),
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


_JuniPolicyRuleType2_Type.__name__ = "Integer32"
_JuniPolicyRuleType2_Object = MibTableColumn
juniPolicyRuleType2 = _JuniPolicyRuleType2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 14, 1, 4),
    _JuniPolicyRuleType2_Type()
)
juniPolicyRuleType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyRuleType2.setStatus("current")


class _JuniPolicySuspend2_Type(TruthValue):
    """Custom type juniPolicySuspend2 based on TruthValue"""


_JuniPolicySuspend2_Object = MibTableColumn
juniPolicySuspend2 = _JuniPolicySuspend2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 14, 1, 5),
    _JuniPolicySuspend2_Type()
)
juniPolicySuspend2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPolicySuspend2.setStatus("current")
_JuniNextHopRule2Table_Object = MibTable
juniNextHopRule2Table = _JuniNextHopRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 15)
)
if mibBuilder.loadTexts:
    juniNextHopRule2Table.setStatus("current")
_JuniNextHopRule2Entry_Object = MibTableRow
juniNextHopRule2Entry = _JuniNextHopRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 15, 1)
)
juniNextHopRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniNextHopRule2Entry.setStatus("current")
_JuniNextHopRowStatus2_Type = RowStatus
_JuniNextHopRowStatus2_Object = MibTableColumn
juniNextHopRowStatus2 = _JuniNextHopRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 15, 1, 1),
    _JuniNextHopRowStatus2_Type()
)
juniNextHopRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextHopRowStatus2.setStatus("current")


class _JuniNextHopIpAddress2_Type(IpAddress):
    """Custom type juniNextHopIpAddress2 based on IpAddress"""
    defaultHexValue = "00000000"


_JuniNextHopIpAddress2_Object = MibTableColumn
juniNextHopIpAddress2 = _JuniNextHopIpAddress2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 15, 1, 2),
    _JuniNextHopIpAddress2_Type()
)
juniNextHopIpAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextHopIpAddress2.setStatus("current")
_JuniFilterRule2Table_Object = MibTable
juniFilterRule2Table = _JuniFilterRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 16)
)
if mibBuilder.loadTexts:
    juniFilterRule2Table.setStatus("current")
_JuniFilterRule2Entry_Object = MibTableRow
juniFilterRule2Entry = _JuniFilterRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 16, 1)
)
juniFilterRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniFilterRule2Entry.setStatus("current")
_JuniFilterRowStatus2_Type = RowStatus
_JuniFilterRowStatus2_Object = MibTableColumn
juniFilterRowStatus2 = _JuniFilterRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 16, 1, 1),
    _JuniFilterRowStatus2_Type()
)
juniFilterRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniFilterRowStatus2.setStatus("current")
_JuniNextInterfaceRule2Table_Object = MibTable
juniNextInterfaceRule2Table = _JuniNextInterfaceRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 17)
)
if mibBuilder.loadTexts:
    juniNextInterfaceRule2Table.setStatus("current")
_JuniNextInterfaceRule2Entry_Object = MibTableRow
juniNextInterfaceRule2Entry = _JuniNextInterfaceRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 17, 1)
)
juniNextInterfaceRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniNextInterfaceRule2Entry.setStatus("current")
_JuniNextInterfaceRowStatus2_Type = RowStatus
_JuniNextInterfaceRowStatus2_Object = MibTableColumn
juniNextInterfaceRowStatus2 = _JuniNextInterfaceRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 17, 1, 1),
    _JuniNextInterfaceRowStatus2_Type()
)
juniNextInterfaceRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextInterfaceRowStatus2.setStatus("current")
_JuniNextInterfaceId2_Type = InterfaceIndex
_JuniNextInterfaceId2_Object = MibTableColumn
juniNextInterfaceId2 = _JuniNextInterfaceId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 17, 1, 2),
    _JuniNextInterfaceId2_Type()
)
juniNextInterfaceId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextInterfaceId2.setStatus("current")


class _JuniNextInterfaceNextHop2_Type(IpAddress):
    """Custom type juniNextInterfaceNextHop2 based on IpAddress"""
    defaultHexValue = "00000000"


_JuniNextInterfaceNextHop2_Object = MibTableColumn
juniNextInterfaceNextHop2 = _JuniNextInterfaceNextHop2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 17, 1, 3),
    _JuniNextInterfaceNextHop2_Type()
)
juniNextInterfaceNextHop2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniNextInterfaceNextHop2.setStatus("current")
_JuniRateLimitRule2Table_Object = MibTable
juniRateLimitRule2Table = _JuniRateLimitRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 18)
)
if mibBuilder.loadTexts:
    juniRateLimitRule2Table.setStatus("current")
_JuniRateLimitRule2Entry_Object = MibTableRow
juniRateLimitRule2Entry = _JuniRateLimitRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 18, 1)
)
juniRateLimitRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniRateLimitRule2Entry.setStatus("current")
_JuniRateLimitRowStatus2_Type = RowStatus
_JuniRateLimitRowStatus2_Object = MibTableColumn
juniRateLimitRowStatus2 = _JuniRateLimitRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 18, 1, 1),
    _JuniRateLimitRowStatus2_Type()
)
juniRateLimitRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRateLimitRowStatus2.setStatus("current")


class _JuniRateLimitId2_Type(Integer32):
    """Custom type juniRateLimitId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniRateLimitId2_Type.__name__ = "Integer32"
_JuniRateLimitId2_Object = MibTableColumn
juniRateLimitId2 = _JuniRateLimitId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 18, 1, 2),
    _JuniRateLimitId2_Type()
)
juniRateLimitId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRateLimitId2.setStatus("current")
_JuniMarkingRule2Table_Object = MibTable
juniMarkingRule2Table = _JuniMarkingRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 19)
)
if mibBuilder.loadTexts:
    juniMarkingRule2Table.setStatus("current")
_JuniMarkingRule2Entry_Object = MibTableRow
juniMarkingRule2Entry = _JuniMarkingRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 19, 1)
)
juniMarkingRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniMarkingRule2Entry.setStatus("current")
_JuniMarkingRowStatus2_Type = RowStatus
_JuniMarkingRowStatus2_Object = MibTableColumn
juniMarkingRowStatus2 = _JuniMarkingRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 19, 1, 1),
    _JuniMarkingRowStatus2_Type()
)
juniMarkingRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMarkingRowStatus2.setStatus("current")


class _JuniMarkingTOSByte2_Type(Integer32):
    """Custom type juniMarkingTOSByte2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniMarkingTOSByte2_Type.__name__ = "Integer32"
_JuniMarkingTOSByte2_Object = MibTableColumn
juniMarkingTOSByte2 = _JuniMarkingTOSByte2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 19, 1, 2),
    _JuniMarkingTOSByte2_Type()
)
juniMarkingTOSByte2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMarkingTOSByte2.setStatus("current")


class _JuniMarkingMask2_Type(Integer32):
    """Custom type juniMarkingMask2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniMarkingMask2_Type.__name__ = "Integer32"
_JuniMarkingMask2_Object = MibTableColumn
juniMarkingMask2 = _JuniMarkingMask2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 19, 1, 3),
    _JuniMarkingMask2_Type()
)
juniMarkingMask2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniMarkingMask2.setStatus("current")
_JuniForwardRule2Table_Object = MibTable
juniForwardRule2Table = _JuniForwardRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20)
)
if mibBuilder.loadTexts:
    juniForwardRule2Table.setStatus("current")
_JuniForwardRule2Entry_Object = MibTableRow
juniForwardRule2Entry = _JuniForwardRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20, 1)
)
juniForwardRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniForwardRule2Entry.setStatus("current")
_JuniForwardRowStatus2_Type = RowStatus
_JuniForwardRowStatus2_Object = MibTableColumn
juniForwardRowStatus2 = _JuniForwardRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20, 1, 1),
    _JuniForwardRowStatus2_Type()
)
juniForwardRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardRowStatus2.setStatus("current")
_JuniForwardNextInterfaceId2_Type = InterfaceIndex
_JuniForwardNextInterfaceId2_Object = MibTableColumn
juniForwardNextInterfaceId2 = _JuniForwardNextInterfaceId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20, 1, 2),
    _JuniForwardNextInterfaceId2_Type()
)
juniForwardNextInterfaceId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardNextInterfaceId2.setStatus("current")


class _JuniForwardNextHop2_Type(IpAddress):
    """Custom type juniForwardNextHop2 based on IpAddress"""
    defaultHexValue = "00000000"


_JuniForwardNextHop2_Object = MibTableColumn
juniForwardNextHop2 = _JuniForwardNextHop2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20, 1, 3),
    _JuniForwardNextHop2_Type()
)
juniForwardNextHop2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardNextHop2.setStatus("current")


class _JuniForwardRouterId2_Type(Integer32):
    """Custom type juniForwardRouterId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniForwardRouterId2_Type.__name__ = "Integer32"
_JuniForwardRouterId2_Object = MibTableColumn
juniForwardRouterId2 = _JuniForwardRouterId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20, 1, 4),
    _JuniForwardRouterId2_Type()
)
juniForwardRouterId2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniForwardRouterId2.setStatus("current")


class _JuniForwardOrder2_Type(Integer32):
    """Custom type juniForwardOrder2 based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_JuniForwardOrder2_Type.__name__ = "Integer32"
_JuniForwardOrder2_Object = MibTableColumn
juniForwardOrder2 = _JuniForwardOrder2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20, 1, 5),
    _JuniForwardOrder2_Type()
)
juniForwardOrder2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardOrder2.setStatus("current")


class _JuniForwardIgnoreDefaultRoute2_Type(TruthValue):
    """Custom type juniForwardIgnoreDefaultRoute2 based on TruthValue"""


_JuniForwardIgnoreDefaultRoute2_Object = MibTableColumn
juniForwardIgnoreDefaultRoute2 = _JuniForwardIgnoreDefaultRoute2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 20, 1, 6),
    _JuniForwardIgnoreDefaultRoute2_Type()
)
juniForwardIgnoreDefaultRoute2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniForwardIgnoreDefaultRoute2.setStatus("current")
_JuniColorRule2Table_Object = MibTable
juniColorRule2Table = _JuniColorRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 21)
)
if mibBuilder.loadTexts:
    juniColorRule2Table.setStatus("current")
_JuniColorRule2Entry_Object = MibTableRow
juniColorRule2Entry = _JuniColorRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 21, 1)
)
juniColorRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniColorRule2Entry.setStatus("current")
_JuniColorRowStatus2_Type = RowStatus
_JuniColorRowStatus2_Object = MibTableColumn
juniColorRowStatus2 = _JuniColorRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 21, 1, 1),
    _JuniColorRowStatus2_Type()
)
juniColorRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniColorRowStatus2.setStatus("current")


class _JuniColor2_Type(Integer32):
    """Custom type juniColor2 based on Integer32"""
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


_JuniColor2_Type.__name__ = "Integer32"
_JuniColor2_Object = MibTableColumn
juniColor2 = _JuniColor2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 21, 1, 2),
    _JuniColor2_Type()
)
juniColor2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniColor2.setStatus("current")
_JuniLogRule2Table_Object = MibTable
juniLogRule2Table = _JuniLogRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 22)
)
if mibBuilder.loadTexts:
    juniLogRule2Table.setStatus("current")
_JuniLogRule2Entry_Object = MibTableRow
juniLogRule2Entry = _JuniLogRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 22, 1)
)
juniLogRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniLogRule2Entry.setStatus("current")
_JuniLogRowStatus2_Type = RowStatus
_JuniLogRowStatus2_Object = MibTableColumn
juniLogRowStatus2 = _JuniLogRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 22, 1, 1),
    _JuniLogRowStatus2_Type()
)
juniLogRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniLogRowStatus2.setStatus("current")
_JuniTrafficClassRule2Table_Object = MibTable
juniTrafficClassRule2Table = _JuniTrafficClassRule2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 23)
)
if mibBuilder.loadTexts:
    juniTrafficClassRule2Table.setStatus("current")
_JuniTrafficClassRule2Entry_Object = MibTableRow
juniTrafficClassRule2Entry = _JuniTrafficClassRule2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 23, 1)
)
juniTrafficClassRule2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniTrafficClassRule2Entry.setStatus("current")
_JuniTrafficClassRowStatus2_Type = RowStatus
_JuniTrafficClassRowStatus2_Object = MibTableColumn
juniTrafficClassRowStatus2 = _JuniTrafficClassRowStatus2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 23, 1, 1),
    _JuniTrafficClassRowStatus2_Type()
)
juniTrafficClassRowStatus2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficClassRowStatus2.setStatus("current")


class _JuniTrafficClassId2_Type(Integer32):
    """Custom type juniTrafficClassId2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniTrafficClassId2_Type.__name__ = "Integer32"
_JuniTrafficClassId2_Object = MibTableColumn
juniTrafficClassId2 = _JuniTrafficClassId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 23, 1, 2),
    _JuniTrafficClassId2_Type()
)
juniTrafficClassId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficClassId2.setStatus("current")
_JuniPolicyClassifierGroupTable_Object = MibTable
juniPolicyClassifierGroupTable = _JuniPolicyClassifierGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 24)
)
if mibBuilder.loadTexts:
    juniPolicyClassifierGroupTable.setStatus("current")
_JuniPolicyClassifierGroupEntry_Object = MibTableRow
juniPolicyClassifierGroupEntry = _JuniPolicyClassifierGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 24, 1)
)
juniPolicyClassifierGroupEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyClassifierGroupPolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyClassifierGroupClaclId"),
)
if mibBuilder.loadTexts:
    juniPolicyClassifierGroupEntry.setStatus("current")


class _JuniPolicyClassifierGroupPolicyId_Type(Integer32):
    """Custom type juniPolicyClassifierGroupPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyClassifierGroupPolicyId_Type.__name__ = "Integer32"
_JuniPolicyClassifierGroupPolicyId_Object = MibTableColumn
juniPolicyClassifierGroupPolicyId = _JuniPolicyClassifierGroupPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 24, 1, 1),
    _JuniPolicyClassifierGroupPolicyId_Type()
)
juniPolicyClassifierGroupPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyClassifierGroupPolicyId.setStatus("current")


class _JuniPolicyClassifierGroupClaclId_Type(Integer32):
    """Custom type juniPolicyClassifierGroupClaclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyClassifierGroupClaclId_Type.__name__ = "Integer32"
_JuniPolicyClassifierGroupClaclId_Object = MibTableColumn
juniPolicyClassifierGroupClaclId = _JuniPolicyClassifierGroupClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 24, 1, 2),
    _JuniPolicyClassifierGroupClaclId_Type()
)
juniPolicyClassifierGroupClaclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyClassifierGroupClaclId.setStatus("current")
_JuniPolicyClassifierGroupRowStatus_Type = RowStatus
_JuniPolicyClassifierGroupRowStatus_Object = MibTableColumn
juniPolicyClassifierGroupRowStatus = _JuniPolicyClassifierGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 24, 1, 3),
    _JuniPolicyClassifierGroupRowStatus_Type()
)
juniPolicyClassifierGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyClassifierGroupRowStatus.setStatus("current")


class _JuniPolicyClassifierGroupPrecedence_Type(Integer32):
    """Custom type juniPolicyClassifierGroupPrecedence based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniPolicyClassifierGroupPrecedence_Type.__name__ = "Integer32"
_JuniPolicyClassifierGroupPrecedence_Object = MibTableColumn
juniPolicyClassifierGroupPrecedence = _JuniPolicyClassifierGroupPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 24, 1, 4),
    _JuniPolicyClassifierGroupPrecedence_Type()
)
juniPolicyClassifierGroupPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyClassifierGroupPrecedence.setStatus("current")
_JuniExceptionRuleTable_Object = MibTable
juniExceptionRuleTable = _JuniExceptionRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 25)
)
if mibBuilder.loadTexts:
    juniExceptionRuleTable.setStatus("current")
_JuniExceptionRuleEntry_Object = MibTableRow
juniExceptionRuleEntry = _JuniExceptionRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 25, 1)
)
juniExceptionRuleEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyRulePolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyRuleId2"),
)
if mibBuilder.loadTexts:
    juniExceptionRuleEntry.setStatus("current")
_JuniExceptionRowStatus_Type = RowStatus
_JuniExceptionRowStatus_Object = MibTableColumn
juniExceptionRowStatus = _JuniExceptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 25, 1, 1),
    _JuniExceptionRowStatus_Type()
)
juniExceptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniExceptionRowStatus.setStatus("current")


class _JuniExceptionApplication_Type(Integer32):
    """Custom type juniExceptionApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("http-redirect", 1)
    )


_JuniExceptionApplication_Type.__name__ = "Integer32"
_JuniExceptionApplication_Object = MibTableColumn
juniExceptionApplication = _JuniExceptionApplication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 3, 25, 1, 2),
    _JuniExceptionApplication_Type()
)
juniExceptionApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniExceptionApplication.setStatus("current")
_JuniPolicyIf_ObjectIdentity = ObjectIdentity
juniPolicyIf = _JuniPolicyIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4)
)
_JuniPolicyIfTable_Object = MibTable
juniPolicyIfTable = _JuniPolicyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniPolicyIfTable.setStatus("obsolete")
_JuniPolicyIfEntry_Object = MibTableRow
juniPolicyIfEntry = _JuniPolicyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1)
)
juniPolicyIfEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyIfInterfaceId"),
)
if mibBuilder.loadTexts:
    juniPolicyIfEntry.setStatus("obsolete")
_JuniPolicyIfInterfaceId_Type = Unsigned32
_JuniPolicyIfInterfaceId_Object = MibTableColumn
juniPolicyIfInterfaceId = _JuniPolicyIfInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 1),
    _JuniPolicyIfInterfaceId_Type()
)
juniPolicyIfInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfInterfaceId.setStatus("obsolete")
_JuniPolicyIfRowStatus_Type = RowStatus
_JuniPolicyIfRowStatus_Object = MibTableColumn
juniPolicyIfRowStatus = _JuniPolicyIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 2),
    _JuniPolicyIfRowStatus_Type()
)
juniPolicyIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfRowStatus.setStatus("obsolete")


class _JuniPolicyIfInputPolicyId_Type(Integer32):
    """Custom type juniPolicyIfInputPolicyId based on Integer32"""
    defaultValue = 0


_JuniPolicyIfInputPolicyId_Object = MibTableColumn
juniPolicyIfInputPolicyId = _JuniPolicyIfInputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 3),
    _JuniPolicyIfInputPolicyId_Type()
)
juniPolicyIfInputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfInputPolicyId.setStatus("obsolete")


class _JuniPolicyIfOutputPolicyId_Type(Integer32):
    """Custom type juniPolicyIfOutputPolicyId based on Integer32"""
    defaultValue = 0


_JuniPolicyIfOutputPolicyId_Object = MibTableColumn
juniPolicyIfOutputPolicyId = _JuniPolicyIfOutputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 4),
    _JuniPolicyIfOutputPolicyId_Type()
)
juniPolicyIfOutputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfOutputPolicyId.setStatus("obsolete")


class _JuniPolicyIfInputStatsEnable_Type(TruthValue):
    """Custom type juniPolicyIfInputStatsEnable based on TruthValue"""


_JuniPolicyIfInputStatsEnable_Object = MibTableColumn
juniPolicyIfInputStatsEnable = _JuniPolicyIfInputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 5),
    _JuniPolicyIfInputStatsEnable_Type()
)
juniPolicyIfInputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfInputStatsEnable.setStatus("obsolete")


class _JuniPolicyIfOutputStatsEnable_Type(TruthValue):
    """Custom type juniPolicyIfOutputStatsEnable based on TruthValue"""


_JuniPolicyIfOutputStatsEnable_Object = MibTableColumn
juniPolicyIfOutputStatsEnable = _JuniPolicyIfOutputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 1, 1, 6),
    _JuniPolicyIfOutputStatsEnable_Type()
)
juniPolicyIfOutputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfOutputStatsEnable.setStatus("obsolete")
_JuniPolicyIfAttachTable_Object = MibTable
juniPolicyIfAttachTable = _JuniPolicyIfAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2)
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachTable.setStatus("current")
_JuniPolicyIfAttachEntry_Object = MibTableRow
juniPolicyIfAttachEntry = _JuniPolicyIfAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1)
)
juniPolicyIfAttachEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachInterfaceId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachForwardingType"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachPolicyType"),
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachEntry.setStatus("current")
_JuniPolicyIfAttachInterfaceId_Type = InterfaceIndex
_JuniPolicyIfAttachInterfaceId_Object = MibTableColumn
juniPolicyIfAttachInterfaceId = _JuniPolicyIfAttachInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 1),
    _JuniPolicyIfAttachInterfaceId_Type()
)
juniPolicyIfAttachInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachInterfaceId.setStatus("current")
_JuniPolicyIfAttachForwardingType_Type = JuniPolicyForwardingType
_JuniPolicyIfAttachForwardingType_Object = MibTableColumn
juniPolicyIfAttachForwardingType = _JuniPolicyIfAttachForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 2),
    _JuniPolicyIfAttachForwardingType_Type()
)
juniPolicyIfAttachForwardingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachForwardingType.setStatus("current")
_JuniPolicyIfAttachPolicyType_Type = JuniPolicyAttachmentType
_JuniPolicyIfAttachPolicyType_Object = MibTableColumn
juniPolicyIfAttachPolicyType = _JuniPolicyIfAttachPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 3),
    _JuniPolicyIfAttachPolicyType_Type()
)
juniPolicyIfAttachPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachPolicyType.setStatus("current")
_JuniPolicyIfAttachRowStatus_Type = RowStatus
_JuniPolicyIfAttachRowStatus_Object = MibTableColumn
juniPolicyIfAttachRowStatus = _JuniPolicyIfAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 4),
    _JuniPolicyIfAttachRowStatus_Type()
)
juniPolicyIfAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfAttachRowStatus.setStatus("current")


class _JuniPolicyIfAttachPolicyId_Type(Integer32):
    """Custom type juniPolicyIfAttachPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachPolicyId_Type.__name__ = "Integer32"
_JuniPolicyIfAttachPolicyId_Object = MibTableColumn
juniPolicyIfAttachPolicyId = _JuniPolicyIfAttachPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 5),
    _JuniPolicyIfAttachPolicyId_Type()
)
juniPolicyIfAttachPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfAttachPolicyId.setStatus("current")


class _JuniPolicyIfAttachStatsEnable_Type(TruthValue):
    """Custom type juniPolicyIfAttachStatsEnable based on TruthValue"""


_JuniPolicyIfAttachStatsEnable_Object = MibTableColumn
juniPolicyIfAttachStatsEnable = _JuniPolicyIfAttachStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 6),
    _JuniPolicyIfAttachStatsEnable_Type()
)
juniPolicyIfAttachStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsEnable.setStatus("current")


class _JuniPolicyIfAttachStatsPreserve_Type(TruthValue):
    """Custom type juniPolicyIfAttachStatsPreserve based on TruthValue"""


_JuniPolicyIfAttachStatsPreserve_Object = MibTableColumn
juniPolicyIfAttachStatsPreserve = _JuniPolicyIfAttachStatsPreserve_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 4, 2, 1, 7),
    _JuniPolicyIfAttachStatsPreserve_Type()
)
juniPolicyIfAttachStatsPreserve.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsPreserve.setStatus("current")
_JuniPolicyProfile_ObjectIdentity = ObjectIdentity
juniPolicyProfile = _JuniPolicyProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5)
)
_JuniPolicyProfileTable_Object = MibTable
juniPolicyProfileTable = _JuniPolicyProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniPolicyProfileTable.setStatus("obsolete")
_JuniPolicyProfileEntry_Object = MibTableRow
juniPolicyProfileEntry = _JuniPolicyProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1)
)
juniPolicyProfileEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyProfileId"),
)
if mibBuilder.loadTexts:
    juniPolicyProfileEntry.setStatus("obsolete")
_JuniPolicyProfileId_Type = Unsigned32
_JuniPolicyProfileId_Object = MibTableColumn
juniPolicyProfileId = _JuniPolicyProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 1),
    _JuniPolicyProfileId_Type()
)
juniPolicyProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyProfileId.setStatus("obsolete")
_JuniPolicyProfileRowStatus_Type = RowStatus
_JuniPolicyProfileRowStatus_Object = MibTableColumn
juniPolicyProfileRowStatus = _JuniPolicyProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 2),
    _JuniPolicyProfileRowStatus_Type()
)
juniPolicyProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyProfileRowStatus.setStatus("obsolete")


class _JuniPolicyProfileInputPolicyId_Type(Integer32):
    """Custom type juniPolicyProfileInputPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyProfileInputPolicyId_Type.__name__ = "Integer32"
_JuniPolicyProfileInputPolicyId_Object = MibTableColumn
juniPolicyProfileInputPolicyId = _JuniPolicyProfileInputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 3),
    _JuniPolicyProfileInputPolicyId_Type()
)
juniPolicyProfileInputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyProfileInputPolicyId.setStatus("obsolete")


class _JuniPolicyProfileOutputPolicyId_Type(Integer32):
    """Custom type juniPolicyProfileOutputPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyProfileOutputPolicyId_Type.__name__ = "Integer32"
_JuniPolicyProfileOutputPolicyId_Object = MibTableColumn
juniPolicyProfileOutputPolicyId = _JuniPolicyProfileOutputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 4),
    _JuniPolicyProfileOutputPolicyId_Type()
)
juniPolicyProfileOutputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyProfileOutputPolicyId.setStatus("obsolete")


class _JuniPolicyProfileInputStatsEnable_Type(TruthValue):
    """Custom type juniPolicyProfileInputStatsEnable based on TruthValue"""


_JuniPolicyProfileInputStatsEnable_Object = MibTableColumn
juniPolicyProfileInputStatsEnable = _JuniPolicyProfileInputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 5),
    _JuniPolicyProfileInputStatsEnable_Type()
)
juniPolicyProfileInputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyProfileInputStatsEnable.setStatus("obsolete")


class _JuniPolicyProfileOutputStatsEnable_Type(TruthValue):
    """Custom type juniPolicyProfileOutputStatsEnable based on TruthValue"""


_JuniPolicyProfileOutputStatsEnable_Object = MibTableColumn
juniPolicyProfileOutputStatsEnable = _JuniPolicyProfileOutputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 6),
    _JuniPolicyProfileOutputStatsEnable_Type()
)
juniPolicyProfileOutputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyProfileOutputStatsEnable.setStatus("obsolete")


class _JuniPolicyProfileLocalInputPolicyId_Type(Integer32):
    """Custom type juniPolicyProfileLocalInputPolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyProfileLocalInputPolicyId_Type.__name__ = "Integer32"
_JuniPolicyProfileLocalInputPolicyId_Object = MibTableColumn
juniPolicyProfileLocalInputPolicyId = _JuniPolicyProfileLocalInputPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 7),
    _JuniPolicyProfileLocalInputPolicyId_Type()
)
juniPolicyProfileLocalInputPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyProfileLocalInputPolicyId.setStatus("obsolete")


class _JuniPolicyProfileLocalInputStatsEnable_Type(TruthValue):
    """Custom type juniPolicyProfileLocalInputStatsEnable based on TruthValue"""


_JuniPolicyProfileLocalInputStatsEnable_Object = MibTableColumn
juniPolicyProfileLocalInputStatsEnable = _JuniPolicyProfileLocalInputStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 1, 1, 8),
    _JuniPolicyProfileLocalInputStatsEnable_Type()
)
juniPolicyProfileLocalInputStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyProfileLocalInputStatsEnable.setStatus("obsolete")
_JuniPolicyAttachProfileTable_Object = MibTable
juniPolicyAttachProfileTable = _JuniPolicyAttachProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2)
)
if mibBuilder.loadTexts:
    juniPolicyAttachProfileTable.setStatus("current")
_JuniPolicyAttachProfileEntry_Object = MibTableRow
juniPolicyAttachProfileEntry = _JuniPolicyAttachProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1)
)
juniPolicyAttachProfileEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyAttachProfileId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyAttachProfileForwardingType"),
    (0, "Juniper-POLICY-MIB", "juniPolicyAttachProfilePolicyType"),
)
if mibBuilder.loadTexts:
    juniPolicyAttachProfileEntry.setStatus("current")
_JuniPolicyAttachProfileId_Type = Unsigned32
_JuniPolicyAttachProfileId_Object = MibTableColumn
juniPolicyAttachProfileId = _JuniPolicyAttachProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 1),
    _JuniPolicyAttachProfileId_Type()
)
juniPolicyAttachProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyAttachProfileId.setStatus("current")
_JuniPolicyAttachProfileForwardingType_Type = JuniPolicyForwardingType
_JuniPolicyAttachProfileForwardingType_Object = MibTableColumn
juniPolicyAttachProfileForwardingType = _JuniPolicyAttachProfileForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 2),
    _JuniPolicyAttachProfileForwardingType_Type()
)
juniPolicyAttachProfileForwardingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyAttachProfileForwardingType.setStatus("current")
_JuniPolicyAttachProfilePolicyType_Type = JuniPolicyAttachmentType
_JuniPolicyAttachProfilePolicyType_Object = MibTableColumn
juniPolicyAttachProfilePolicyType = _JuniPolicyAttachProfilePolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 3),
    _JuniPolicyAttachProfilePolicyType_Type()
)
juniPolicyAttachProfilePolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyAttachProfilePolicyType.setStatus("current")
_JuniPolicyAttachProfileRowStatus_Type = RowStatus
_JuniPolicyAttachProfileRowStatus_Object = MibTableColumn
juniPolicyAttachProfileRowStatus = _JuniPolicyAttachProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 4),
    _JuniPolicyAttachProfileRowStatus_Type()
)
juniPolicyAttachProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyAttachProfileRowStatus.setStatus("current")


class _JuniPolicyAttachProfilePolicyId_Type(Integer32):
    """Custom type juniPolicyAttachProfilePolicyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyAttachProfilePolicyId_Type.__name__ = "Integer32"
_JuniPolicyAttachProfilePolicyId_Object = MibTableColumn
juniPolicyAttachProfilePolicyId = _JuniPolicyAttachProfilePolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 5),
    _JuniPolicyAttachProfilePolicyId_Type()
)
juniPolicyAttachProfilePolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyAttachProfilePolicyId.setStatus("current")


class _JuniPolicyAttachProfileStatsEnable_Type(TruthValue):
    """Custom type juniPolicyAttachProfileStatsEnable based on TruthValue"""


_JuniPolicyAttachProfileStatsEnable_Object = MibTableColumn
juniPolicyAttachProfileStatsEnable = _JuniPolicyAttachProfileStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 5, 2, 1, 6),
    _JuniPolicyAttachProfileStatsEnable_Type()
)
juniPolicyAttachProfileStatsEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPolicyAttachProfileStatsEnable.setStatus("current")
_JuniPolicyStatistics_ObjectIdentity = ObjectIdentity
juniPolicyStatistics = _JuniPolicyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6)
)
_JuniPolicyIfStatsTable_Object = MibTable
juniPolicyIfStatsTable = _JuniPolicyIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1)
)
if mibBuilder.loadTexts:
    juniPolicyIfStatsTable.setStatus("obsolete")
_JuniPolicyIfStatsEntry_Object = MibTableRow
juniPolicyIfStatsEntry = _JuniPolicyIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1)
)
juniPolicyIfStatsEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyIfStatsIfId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfStatsPolicyType"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfStatsPolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfStatsRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfStatsRuleId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfStatsClaclEntryNumber"),
)
if mibBuilder.loadTexts:
    juniPolicyIfStatsEntry.setStatus("obsolete")
_JuniPolicyIfStatsIfId_Type = InterfaceIndex
_JuniPolicyIfStatsIfId_Object = MibTableColumn
juniPolicyIfStatsIfId = _JuniPolicyIfStatsIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 1),
    _JuniPolicyIfStatsIfId_Type()
)
juniPolicyIfStatsIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfStatsIfId.setStatus("obsolete")
_JuniPolicyIfStatsPolicyType_Type = JuniPolicyAttachmentType
_JuniPolicyIfStatsPolicyType_Object = MibTableColumn
juniPolicyIfStatsPolicyType = _JuniPolicyIfStatsPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 2),
    _JuniPolicyIfStatsPolicyType_Type()
)
juniPolicyIfStatsPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfStatsPolicyType.setStatus("obsolete")


class _JuniPolicyIfStatsPolicyId_Type(Integer32):
    """Custom type juniPolicyIfStatsPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfStatsPolicyId_Type.__name__ = "Integer32"
_JuniPolicyIfStatsPolicyId_Object = MibTableColumn
juniPolicyIfStatsPolicyId = _JuniPolicyIfStatsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 3),
    _JuniPolicyIfStatsPolicyId_Type()
)
juniPolicyIfStatsPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfStatsPolicyId.setStatus("obsolete")


class _JuniPolicyIfStatsRulePrec_Type(Integer32):
    """Custom type juniPolicyIfStatsRulePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfStatsRulePrec_Type.__name__ = "Integer32"
_JuniPolicyIfStatsRulePrec_Object = MibTableColumn
juniPolicyIfStatsRulePrec = _JuniPolicyIfStatsRulePrec_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 4),
    _JuniPolicyIfStatsRulePrec_Type()
)
juniPolicyIfStatsRulePrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfStatsRulePrec.setStatus("obsolete")


class _JuniPolicyIfStatsRuleId_Type(Integer32):
    """Custom type juniPolicyIfStatsRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfStatsRuleId_Type.__name__ = "Integer32"
_JuniPolicyIfStatsRuleId_Object = MibTableColumn
juniPolicyIfStatsRuleId = _JuniPolicyIfStatsRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 5),
    _JuniPolicyIfStatsRuleId_Type()
)
juniPolicyIfStatsRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfStatsRuleId.setStatus("obsolete")


class _JuniPolicyIfStatsClaclEntryNumber_Type(Integer32):
    """Custom type juniPolicyIfStatsClaclEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfStatsClaclEntryNumber_Type.__name__ = "Integer32"
_JuniPolicyIfStatsClaclEntryNumber_Object = MibTableColumn
juniPolicyIfStatsClaclEntryNumber = _JuniPolicyIfStatsClaclEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 6),
    _JuniPolicyIfStatsClaclEntryNumber_Type()
)
juniPolicyIfStatsClaclEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfStatsClaclEntryNumber.setStatus("obsolete")
_JuniPolicyIfStatsGreenPackets_Type = Counter64
_JuniPolicyIfStatsGreenPackets_Object = MibTableColumn
juniPolicyIfStatsGreenPackets = _JuniPolicyIfStatsGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 7),
    _JuniPolicyIfStatsGreenPackets_Type()
)
juniPolicyIfStatsGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfStatsGreenPackets.setStatus("obsolete")
_JuniPolicyIfStatsYellowPackets_Type = Counter64
_JuniPolicyIfStatsYellowPackets_Object = MibTableColumn
juniPolicyIfStatsYellowPackets = _JuniPolicyIfStatsYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 8),
    _JuniPolicyIfStatsYellowPackets_Type()
)
juniPolicyIfStatsYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfStatsYellowPackets.setStatus("obsolete")
_JuniPolicyIfStatsRedPackets_Type = Counter64
_JuniPolicyIfStatsRedPackets_Object = MibTableColumn
juniPolicyIfStatsRedPackets = _JuniPolicyIfStatsRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 9),
    _JuniPolicyIfStatsRedPackets_Type()
)
juniPolicyIfStatsRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfStatsRedPackets.setStatus("obsolete")
_JuniPolicyIfStatsGreenBytes_Type = Counter64
_JuniPolicyIfStatsGreenBytes_Object = MibTableColumn
juniPolicyIfStatsGreenBytes = _JuniPolicyIfStatsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 10),
    _JuniPolicyIfStatsGreenBytes_Type()
)
juniPolicyIfStatsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfStatsGreenBytes.setStatus("obsolete")
_JuniPolicyIfStatsYellowBytes_Type = Counter64
_JuniPolicyIfStatsYellowBytes_Object = MibTableColumn
juniPolicyIfStatsYellowBytes = _JuniPolicyIfStatsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 11),
    _JuniPolicyIfStatsYellowBytes_Type()
)
juniPolicyIfStatsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfStatsYellowBytes.setStatus("obsolete")
_JuniPolicyIfStatsRedBytes_Type = Counter64
_JuniPolicyIfStatsRedBytes_Object = MibTableColumn
juniPolicyIfStatsRedBytes = _JuniPolicyIfStatsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 1, 1, 12),
    _JuniPolicyIfStatsRedBytes_Type()
)
juniPolicyIfStatsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfStatsRedBytes.setStatus("obsolete")
_JuniPolicyIfAttachStatsTable_Object = MibTable
juniPolicyIfAttachStatsTable = _JuniPolicyIfAttachStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2)
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsTable.setStatus("obsolete")
_JuniPolicyIfAttachStatsEntry_Object = MibTableRow
juniPolicyIfAttachStatsEntry = _JuniPolicyIfAttachStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1)
)
juniPolicyIfAttachStatsEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsIfId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsForwardingType"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsPolicyType"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsPolicyId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsRulePrec"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsRuleId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsClaclEntryNumber"),
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsEntry.setStatus("obsolete")
_JuniPolicyIfAttachStatsIfId_Type = InterfaceIndex
_JuniPolicyIfAttachStatsIfId_Object = MibTableColumn
juniPolicyIfAttachStatsIfId = _JuniPolicyIfAttachStatsIfId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 1),
    _JuniPolicyIfAttachStatsIfId_Type()
)
juniPolicyIfAttachStatsIfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsIfId.setStatus("obsolete")
_JuniPolicyIfAttachStatsForwardingType_Type = JuniPolicyForwardingType
_JuniPolicyIfAttachStatsForwardingType_Object = MibTableColumn
juniPolicyIfAttachStatsForwardingType = _JuniPolicyIfAttachStatsForwardingType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 2),
    _JuniPolicyIfAttachStatsForwardingType_Type()
)
juniPolicyIfAttachStatsForwardingType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsForwardingType.setStatus("obsolete")
_JuniPolicyIfAttachStatsPolicyType_Type = JuniPolicyAttachmentType
_JuniPolicyIfAttachStatsPolicyType_Object = MibTableColumn
juniPolicyIfAttachStatsPolicyType = _JuniPolicyIfAttachStatsPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 3),
    _JuniPolicyIfAttachStatsPolicyType_Type()
)
juniPolicyIfAttachStatsPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsPolicyType.setStatus("obsolete")


class _JuniPolicyIfAttachStatsPolicyId_Type(Integer32):
    """Custom type juniPolicyIfAttachStatsPolicyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachStatsPolicyId_Type.__name__ = "Integer32"
_JuniPolicyIfAttachStatsPolicyId_Object = MibTableColumn
juniPolicyIfAttachStatsPolicyId = _JuniPolicyIfAttachStatsPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 4),
    _JuniPolicyIfAttachStatsPolicyId_Type()
)
juniPolicyIfAttachStatsPolicyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsPolicyId.setStatus("obsolete")


class _JuniPolicyIfAttachStatsRulePrec_Type(Integer32):
    """Custom type juniPolicyIfAttachStatsRulePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachStatsRulePrec_Type.__name__ = "Integer32"
_JuniPolicyIfAttachStatsRulePrec_Object = MibTableColumn
juniPolicyIfAttachStatsRulePrec = _JuniPolicyIfAttachStatsRulePrec_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 5),
    _JuniPolicyIfAttachStatsRulePrec_Type()
)
juniPolicyIfAttachStatsRulePrec.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsRulePrec.setStatus("obsolete")


class _JuniPolicyIfAttachStatsRuleId_Type(Integer32):
    """Custom type juniPolicyIfAttachStatsRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachStatsRuleId_Type.__name__ = "Integer32"
_JuniPolicyIfAttachStatsRuleId_Object = MibTableColumn
juniPolicyIfAttachStatsRuleId = _JuniPolicyIfAttachStatsRuleId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 6),
    _JuniPolicyIfAttachStatsRuleId_Type()
)
juniPolicyIfAttachStatsRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsRuleId.setStatus("obsolete")


class _JuniPolicyIfAttachStatsClaclEntryNumber_Type(Integer32):
    """Custom type juniPolicyIfAttachStatsClaclEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachStatsClaclEntryNumber_Type.__name__ = "Integer32"
_JuniPolicyIfAttachStatsClaclEntryNumber_Object = MibTableColumn
juniPolicyIfAttachStatsClaclEntryNumber = _JuniPolicyIfAttachStatsClaclEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 7),
    _JuniPolicyIfAttachStatsClaclEntryNumber_Type()
)
juniPolicyIfAttachStatsClaclEntryNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsClaclEntryNumber.setStatus("obsolete")
_JuniPolicyIfAttachStatsGreenPackets_Type = Counter64
_JuniPolicyIfAttachStatsGreenPackets_Object = MibTableColumn
juniPolicyIfAttachStatsGreenPackets = _JuniPolicyIfAttachStatsGreenPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 8),
    _JuniPolicyIfAttachStatsGreenPackets_Type()
)
juniPolicyIfAttachStatsGreenPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsGreenPackets.setStatus("obsolete")
_JuniPolicyIfAttachStatsYellowPackets_Type = Counter64
_JuniPolicyIfAttachStatsYellowPackets_Object = MibTableColumn
juniPolicyIfAttachStatsYellowPackets = _JuniPolicyIfAttachStatsYellowPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 9),
    _JuniPolicyIfAttachStatsYellowPackets_Type()
)
juniPolicyIfAttachStatsYellowPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsYellowPackets.setStatus("obsolete")
_JuniPolicyIfAttachStatsRedPackets_Type = Counter64
_JuniPolicyIfAttachStatsRedPackets_Object = MibTableColumn
juniPolicyIfAttachStatsRedPackets = _JuniPolicyIfAttachStatsRedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 10),
    _JuniPolicyIfAttachStatsRedPackets_Type()
)
juniPolicyIfAttachStatsRedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsRedPackets.setStatus("obsolete")
_JuniPolicyIfAttachStatsGreenBytes_Type = Counter64
_JuniPolicyIfAttachStatsGreenBytes_Object = MibTableColumn
juniPolicyIfAttachStatsGreenBytes = _JuniPolicyIfAttachStatsGreenBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 11),
    _JuniPolicyIfAttachStatsGreenBytes_Type()
)
juniPolicyIfAttachStatsGreenBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsGreenBytes.setStatus("obsolete")
_JuniPolicyIfAttachStatsYellowBytes_Type = Counter64
_JuniPolicyIfAttachStatsYellowBytes_Object = MibTableColumn
juniPolicyIfAttachStatsYellowBytes = _JuniPolicyIfAttachStatsYellowBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 12),
    _JuniPolicyIfAttachStatsYellowBytes_Type()
)
juniPolicyIfAttachStatsYellowBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsYellowBytes.setStatus("obsolete")
_JuniPolicyIfAttachStatsRedBytes_Type = Counter64
_JuniPolicyIfAttachStatsRedBytes_Object = MibTableColumn
juniPolicyIfAttachStatsRedBytes = _JuniPolicyIfAttachStatsRedBytes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 2, 1, 13),
    _JuniPolicyIfAttachStatsRedBytes_Type()
)
juniPolicyIfAttachStatsRedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsRedBytes.setStatus("obsolete")
_JuniPolicyIfAttachStats2Table_Object = MibTable
juniPolicyIfAttachStats2Table = _JuniPolicyIfAttachStats2Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3)
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachStats2Table.setStatus("current")
_JuniPolicyIfAttachStats2Entry_Object = MibTableRow
juniPolicyIfAttachStats2Entry = _JuniPolicyIfAttachStats2Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1)
)
juniPolicyIfAttachStats2Entry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsIfId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsForwardingType2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsPolicyType2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsPolicyId2"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsClaclId"),
    (0, "Juniper-POLICY-MIB", "juniPolicyIfAttachStatsClaclEntryNumber2"),
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachStats2Entry.setStatus("current")
_JuniPolicyIfAttachStatsIfId2_Type = InterfaceIndex
_JuniPolicyIfAttachStatsIfId2_Object = MibTableColumn
juniPolicyIfAttachStatsIfId2 = _JuniPolicyIfAttachStatsIfId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 1),
    _JuniPolicyIfAttachStatsIfId2_Type()
)
juniPolicyIfAttachStatsIfId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsIfId2.setStatus("current")
_JuniPolicyIfAttachStatsForwardingType2_Type = JuniPolicyForwardingType
_JuniPolicyIfAttachStatsForwardingType2_Object = MibTableColumn
juniPolicyIfAttachStatsForwardingType2 = _JuniPolicyIfAttachStatsForwardingType2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 2),
    _JuniPolicyIfAttachStatsForwardingType2_Type()
)
juniPolicyIfAttachStatsForwardingType2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsForwardingType2.setStatus("current")
_JuniPolicyIfAttachStatsPolicyType2_Type = JuniPolicyAttachmentType
_JuniPolicyIfAttachStatsPolicyType2_Object = MibTableColumn
juniPolicyIfAttachStatsPolicyType2 = _JuniPolicyIfAttachStatsPolicyType2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 3),
    _JuniPolicyIfAttachStatsPolicyType2_Type()
)
juniPolicyIfAttachStatsPolicyType2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsPolicyType2.setStatus("current")


class _JuniPolicyIfAttachStatsPolicyId2_Type(Integer32):
    """Custom type juniPolicyIfAttachStatsPolicyId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachStatsPolicyId2_Type.__name__ = "Integer32"
_JuniPolicyIfAttachStatsPolicyId2_Object = MibTableColumn
juniPolicyIfAttachStatsPolicyId2 = _JuniPolicyIfAttachStatsPolicyId2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 4),
    _JuniPolicyIfAttachStatsPolicyId2_Type()
)
juniPolicyIfAttachStatsPolicyId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsPolicyId2.setStatus("current")


class _JuniPolicyIfAttachStatsClaclId_Type(Integer32):
    """Custom type juniPolicyIfAttachStatsClaclId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachStatsClaclId_Type.__name__ = "Integer32"
_JuniPolicyIfAttachStatsClaclId_Object = MibTableColumn
juniPolicyIfAttachStatsClaclId = _JuniPolicyIfAttachStatsClaclId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 5),
    _JuniPolicyIfAttachStatsClaclId_Type()
)
juniPolicyIfAttachStatsClaclId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsClaclId.setStatus("current")


class _JuniPolicyIfAttachStatsClaclEntryNumber2_Type(Integer32):
    """Custom type juniPolicyIfAttachStatsClaclEntryNumber2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPolicyIfAttachStatsClaclEntryNumber2_Type.__name__ = "Integer32"
_JuniPolicyIfAttachStatsClaclEntryNumber2_Object = MibTableColumn
juniPolicyIfAttachStatsClaclEntryNumber2 = _JuniPolicyIfAttachStatsClaclEntryNumber2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 6),
    _JuniPolicyIfAttachStatsClaclEntryNumber2_Type()
)
juniPolicyIfAttachStatsClaclEntryNumber2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsClaclEntryNumber2.setStatus("current")
_JuniPolicyIfAttachStatsGreenPackets2_Type = Counter64
_JuniPolicyIfAttachStatsGreenPackets2_Object = MibTableColumn
juniPolicyIfAttachStatsGreenPackets2 = _JuniPolicyIfAttachStatsGreenPackets2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 7),
    _JuniPolicyIfAttachStatsGreenPackets2_Type()
)
juniPolicyIfAttachStatsGreenPackets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsGreenPackets2.setStatus("current")
_JuniPolicyIfAttachStatsYellowPackets2_Type = Counter64
_JuniPolicyIfAttachStatsYellowPackets2_Object = MibTableColumn
juniPolicyIfAttachStatsYellowPackets2 = _JuniPolicyIfAttachStatsYellowPackets2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 8),
    _JuniPolicyIfAttachStatsYellowPackets2_Type()
)
juniPolicyIfAttachStatsYellowPackets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsYellowPackets2.setStatus("current")
_JuniPolicyIfAttachStatsRedPackets2_Type = Counter64
_JuniPolicyIfAttachStatsRedPackets2_Object = MibTableColumn
juniPolicyIfAttachStatsRedPackets2 = _JuniPolicyIfAttachStatsRedPackets2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 9),
    _JuniPolicyIfAttachStatsRedPackets2_Type()
)
juniPolicyIfAttachStatsRedPackets2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsRedPackets2.setStatus("current")
_JuniPolicyIfAttachStatsGreenBytes2_Type = Counter64
_JuniPolicyIfAttachStatsGreenBytes2_Object = MibTableColumn
juniPolicyIfAttachStatsGreenBytes2 = _JuniPolicyIfAttachStatsGreenBytes2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 10),
    _JuniPolicyIfAttachStatsGreenBytes2_Type()
)
juniPolicyIfAttachStatsGreenBytes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsGreenBytes2.setStatus("current")
_JuniPolicyIfAttachStatsYellowBytes2_Type = Counter64
_JuniPolicyIfAttachStatsYellowBytes2_Object = MibTableColumn
juniPolicyIfAttachStatsYellowBytes2 = _JuniPolicyIfAttachStatsYellowBytes2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 11),
    _JuniPolicyIfAttachStatsYellowBytes2_Type()
)
juniPolicyIfAttachStatsYellowBytes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsYellowBytes2.setStatus("current")
_JuniPolicyIfAttachStatsRedBytes2_Type = Counter64
_JuniPolicyIfAttachStatsRedBytes2_Object = MibTableColumn
juniPolicyIfAttachStatsRedBytes2 = _JuniPolicyIfAttachStatsRedBytes2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 6, 3, 1, 12),
    _JuniPolicyIfAttachStatsRedBytes2_Type()
)
juniPolicyIfAttachStatsRedBytes2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPolicyIfAttachStatsRedBytes2.setStatus("current")
_JuniTrafficShapeControlList_ObjectIdentity = ObjectIdentity
juniTrafficShapeControlList = _JuniTrafficShapeControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7)
)


class _JuniTrafficShapeProfileNextIndex_Type(Integer32):
    """Custom type juniTrafficShapeProfileNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniTrafficShapeProfileNextIndex_Type.__name__ = "Integer32"
_JuniTrafficShapeProfileNextIndex_Object = MibScalar
juniTrafficShapeProfileNextIndex = _JuniTrafficShapeProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 1),
    _JuniTrafficShapeProfileNextIndex_Type()
)
juniTrafficShapeProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTrafficShapeProfileNextIndex.setStatus("obsolete")
_JuniTrafficShapeProfileTable_Object = MibTable
juniTrafficShapeProfileTable = _JuniTrafficShapeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2)
)
if mibBuilder.loadTexts:
    juniTrafficShapeProfileTable.setStatus("obsolete")
_JuniTrafficShapeProfileEntry_Object = MibTableRow
juniTrafficShapeProfileEntry = _JuniTrafficShapeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1)
)
juniTrafficShapeProfileEntry.setIndexNames(
    (0, "Juniper-POLICY-MIB", "juniTrafficShapeProfileId"),
)
if mibBuilder.loadTexts:
    juniTrafficShapeProfileEntry.setStatus("obsolete")


class _JuniTrafficShapeProfileId_Type(Integer32):
    """Custom type juniTrafficShapeProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniTrafficShapeProfileId_Type.__name__ = "Integer32"
_JuniTrafficShapeProfileId_Object = MibTableColumn
juniTrafficShapeProfileId = _JuniTrafficShapeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 1),
    _JuniTrafficShapeProfileId_Type()
)
juniTrafficShapeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniTrafficShapeProfileId.setStatus("obsolete")
_JuniTrafficShapeProfileRowStatus_Type = RowStatus
_JuniTrafficShapeProfileRowStatus_Object = MibTableColumn
juniTrafficShapeProfileRowStatus = _JuniTrafficShapeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 2),
    _JuniTrafficShapeProfileRowStatus_Type()
)
juniTrafficShapeProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficShapeProfileRowStatus.setStatus("obsolete")


class _JuniTrafficShapeProfileName_Type(DisplayString):
    """Custom type juniTrafficShapeProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_JuniTrafficShapeProfileName_Type.__name__ = "DisplayString"
_JuniTrafficShapeProfileName_Object = MibTableColumn
juniTrafficShapeProfileName = _JuniTrafficShapeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 3),
    _JuniTrafficShapeProfileName_Type()
)
juniTrafficShapeProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficShapeProfileName.setStatus("obsolete")
_JuniTrafficShapeReferenceCount_Type = Counter32
_JuniTrafficShapeReferenceCount_Object = MibTableColumn
juniTrafficShapeReferenceCount = _JuniTrafficShapeReferenceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 4),
    _JuniTrafficShapeReferenceCount_Type()
)
juniTrafficShapeReferenceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniTrafficShapeReferenceCount.setStatus("obsolete")


class _JuniTrafficShapeRate_Type(Integer32):
    """Custom type juniTrafficShapeRate based on Integer32"""
    defaultValue = 0


_JuniTrafficShapeRate_Object = MibTableColumn
juniTrafficShapeRate = _JuniTrafficShapeRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 5),
    _JuniTrafficShapeRate_Type()
)
juniTrafficShapeRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficShapeRate.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniTrafficShapeRate.setUnits("bits per second")


class _JuniTrafficShapeBurst_Type(Integer32):
    """Custom type juniTrafficShapeBurst based on Integer32"""
    defaultValue = 0


_JuniTrafficShapeBurst_Object = MibTableColumn
juniTrafficShapeBurst = _JuniTrafficShapeBurst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 1, 7, 2, 1, 6),
    _JuniTrafficShapeBurst_Type()
)
juniTrafficShapeBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniTrafficShapeBurst.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniTrafficShapeBurst.setUnits("bytes")
_JuniPolicyConformance_ObjectIdentity = ObjectIdentity
juniPolicyConformance = _JuniPolicyConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2)
)
_JuniPolicyCompliances_ObjectIdentity = ObjectIdentity
juniPolicyCompliances = _JuniPolicyCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1)
)
_JuniPolicyGroups_ObjectIdentity = ObjectIdentity
juniPolicyGroups = _JuniPolicyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2)
)

# Managed Objects groups

juniPolicyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 1)
)
juniPolicyGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyAdminState"),
        ("Juniper-POLICY-MIB", "juniPolicyOperStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyErrorValue"),
        ("Juniper-POLICY-MIB", "juniPolicyName"),
        ("Juniper-POLICY-MIB", "juniPolicyReferenceCount"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleType"),
        ("Juniper-POLICY-MIB", "juniPolicySuspend"),
        ("Juniper-POLICY-MIB", "juniPolicyEclipsed"),
        ("Juniper-POLICY-MIB", "juniNextHopRowStatus"),
        ("Juniper-POLICY-MIB", "juniNextHopIpAddress"),
        ("Juniper-POLICY-MIB", "juniNextHopClaclId"),
        ("Juniper-POLICY-MIB", "juniFilterRowStatus"),
        ("Juniper-POLICY-MIB", "juniFilterClaclId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceRowStatus"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceClaclId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceNextHop"),
        ("Juniper-POLICY-MIB", "juniRateLimitRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitId"),
        ("Juniper-POLICY-MIB", "juniRateLimitClaclId"),
        ("Juniper-POLICY-MIB", "juniMarkingRowStatus"),
        ("Juniper-POLICY-MIB", "juniMarkingTOSByte"),
        ("Juniper-POLICY-MIB", "juniMarkingMask"),
        ("Juniper-POLICY-MIB", "juniMarkingClaclId"),
        ("Juniper-POLICY-MIB", "juniForwardRowStatus"),
        ("Juniper-POLICY-MIB", "juniForwardClaclId"))
)
if mibBuilder.loadTexts:
    juniPolicyGroup.setStatus("obsolete")

juniRateLimitControlListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 2)
)
juniRateLimitControlListGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniRateLimitProfileNextIndex"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileName"),
        ("Juniper-POLICY-MIB", "juniRateLimitReferenceCount"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitMask"))
)
if mibBuilder.loadTexts:
    juniRateLimitControlListGroup.setStatus("obsolete")

juniClassifierControlListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 3)
)
juniClassifierControlListGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniClassifierControlListNextIndex"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListRowStatus"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListName"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListReferenceCount"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNextElementIndex"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListElemRowStatus"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotSrc"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrc"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotDst"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDst"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDstMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotProtocol"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListProtocol"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListTosByte"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcOperator"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcFromPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcToPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestOperator"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestFromPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestToPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListICMPType"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListICMPCode"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIGMPType"))
)
if mibBuilder.loadTexts:
    juniClassifierControlListGroup.setStatus("obsolete")

juniPolicyIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 4)
)
juniPolicyIfGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyIfRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyIfInputPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyIfOutputPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyIfInputStatsEnable"),
        ("Juniper-POLICY-MIB", "juniPolicyIfOutputStatsEnable"))
)
if mibBuilder.loadTexts:
    juniPolicyIfGroup.setStatus("obsolete")

juniPolicyProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 5)
)
juniPolicyProfileGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileInputPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileOutputPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileInputStatsEnable"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileOutputStatsEnable"))
)
if mibBuilder.loadTexts:
    juniPolicyProfileGroup.setStatus("obsolete")

juniPolicyStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 6)
)
juniPolicyStatisticsGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyIfStatsGreenPackets"),
        ("Juniper-POLICY-MIB", "juniPolicyIfStatsYellowPackets"),
        ("Juniper-POLICY-MIB", "juniPolicyIfStatsRedPackets"),
        ("Juniper-POLICY-MIB", "juniPolicyIfStatsGreenBytes"),
        ("Juniper-POLICY-MIB", "juniPolicyIfStatsYellowBytes"),
        ("Juniper-POLICY-MIB", "juniPolicyIfStatsRedBytes"))
)
if mibBuilder.loadTexts:
    juniPolicyStatisticsGroup.setStatus("obsolete")

juniPolicyGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 7)
)
juniPolicyGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyAdminState"),
        ("Juniper-POLICY-MIB", "juniPolicyOperStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyErrorValue"),
        ("Juniper-POLICY-MIB", "juniPolicyName"),
        ("Juniper-POLICY-MIB", "juniPolicyReferenceCount"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleType"),
        ("Juniper-POLICY-MIB", "juniPolicySuspend"),
        ("Juniper-POLICY-MIB", "juniPolicyEclipsed"),
        ("Juniper-POLICY-MIB", "juniNextHopRowStatus"),
        ("Juniper-POLICY-MIB", "juniNextHopIpAddress"),
        ("Juniper-POLICY-MIB", "juniNextHopClaclId"),
        ("Juniper-POLICY-MIB", "juniFilterRowStatus"),
        ("Juniper-POLICY-MIB", "juniFilterClaclId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceRowStatus"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceClaclId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceNextHop"),
        ("Juniper-POLICY-MIB", "juniRateLimitRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitId"),
        ("Juniper-POLICY-MIB", "juniRateLimitClaclId"),
        ("Juniper-POLICY-MIB", "juniMarkingRowStatus"),
        ("Juniper-POLICY-MIB", "juniMarkingTOSByte"),
        ("Juniper-POLICY-MIB", "juniMarkingMask"),
        ("Juniper-POLICY-MIB", "juniMarkingClaclId"),
        ("Juniper-POLICY-MIB", "juniForwardRowStatus"),
        ("Juniper-POLICY-MIB", "juniForwardClaclId"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeRowStatus"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeId"),
        ("Juniper-POLICY-MIB", "juniColorRowStatus"),
        ("Juniper-POLICY-MIB", "juniColor"),
        ("Juniper-POLICY-MIB", "juniColorClaclId"))
)
if mibBuilder.loadTexts:
    juniPolicyGroup2.setStatus("obsolete")

juniTrafficShapeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 8)
)
juniTrafficShapeProfileGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniTrafficShapeProfileNextIndex"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeProfileName"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeReferenceCount"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeRate"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeBurst"))
)
if mibBuilder.loadTexts:
    juniTrafficShapeProfileGroup.setStatus("obsolete")

juniLogRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 9)
)
juniLogRuleGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniLogRowStatus"),
        ("Juniper-POLICY-MIB", "juniLogClaclId"))
)
if mibBuilder.loadTexts:
    juniLogRuleGroup.setStatus("deprecated")

juniPolicyIfAttachGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 10)
)
juniPolicyIfAttachGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyIfAttachRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsEnable"))
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachGroup.setStatus("obsolete")

juniPolicyProfileGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 11)
)
juniPolicyProfileGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileInputPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileOutputPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileInputStatsEnable"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileOutputStatsEnable"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileLocalInputPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyProfileLocalInputStatsEnable"))
)
if mibBuilder.loadTexts:
    juniPolicyProfileGroup2.setStatus("obsolete")

juniPolicyAttachStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 12)
)
juniPolicyAttachStatisticsGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsGreenPackets"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsYellowPackets"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsRedPackets"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsGreenBytes"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsYellowBytes"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsRedBytes"))
)
if mibBuilder.loadTexts:
    juniPolicyAttachStatisticsGroup.setStatus("obsolete")

juniClassifierControlListGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 13)
)
juniClassifierControlListGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniClassifierControlListNextIndex"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListRowStatus"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListName"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListReferenceCount"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNextElementIndex"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListElemRowStatus"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotSrc"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrc"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotDst"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDst"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDstMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotProtocol"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListProtocol"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListTosByte"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcOperator"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcFromPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcToPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestOperator"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestFromPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestToPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListICMPType"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListICMPCode"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIGMPType"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListTcpFlagsValue"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListTcpFlagsMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIpFlagsValue"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIpFlagsMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIpFragValue"))
)
if mibBuilder.loadTexts:
    juniClassifierControlListGroup2.setStatus("obsolete")

juniPolicyAttachProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 14)
)
juniPolicyAttachProfileGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyAttachProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyAttachProfilePolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyAttachProfileStatsEnable"))
)
if mibBuilder.loadTexts:
    juniPolicyAttachProfileGroup.setStatus("current")

juniPolicyBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 15)
)
juniPolicyBaseGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyAdminState"),
        ("Juniper-POLICY-MIB", "juniPolicyOperStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyErrorValue"),
        ("Juniper-POLICY-MIB", "juniPolicyName"),
        ("Juniper-POLICY-MIB", "juniPolicyReferenceCount"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleType"),
        ("Juniper-POLICY-MIB", "juniPolicySuspend"),
        ("Juniper-POLICY-MIB", "juniPolicyEclipsed"))
)
if mibBuilder.loadTexts:
    juniPolicyBaseGroup.setStatus("obsolete")

juniNextHopRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 16)
)
juniNextHopRulesGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniNextHopRowStatus"),
        ("Juniper-POLICY-MIB", "juniNextHopIpAddress"),
        ("Juniper-POLICY-MIB", "juniNextHopClaclId"))
)
if mibBuilder.loadTexts:
    juniNextHopRulesGroup.setStatus("deprecated")

juniFilterRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 17)
)
juniFilterRulesGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniFilterRowStatus"),
        ("Juniper-POLICY-MIB", "juniFilterClaclId"))
)
if mibBuilder.loadTexts:
    juniFilterRulesGroup.setStatus("deprecated")

juniNextInterfaceRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 18)
)
juniNextInterfaceRulesGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniNextInterfaceRowStatus"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceClaclId"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceNextHop"))
)
if mibBuilder.loadTexts:
    juniNextInterfaceRulesGroup.setStatus("deprecated")

juniRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 19)
)
juniRateLimitGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniRateLimitRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitId"),
        ("Juniper-POLICY-MIB", "juniRateLimitClaclId"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileNextIndex"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileName"),
        ("Juniper-POLICY-MIB", "juniRateLimitReferenceCount"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitMask"))
)
if mibBuilder.loadTexts:
    juniRateLimitGroup.setStatus("obsolete")

juniMarkingRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 20)
)
juniMarkingRulesGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniMarkingRowStatus"),
        ("Juniper-POLICY-MIB", "juniMarkingTOSByte"),
        ("Juniper-POLICY-MIB", "juniMarkingMask"),
        ("Juniper-POLICY-MIB", "juniMarkingClaclId"))
)
if mibBuilder.loadTexts:
    juniMarkingRulesGroup.setStatus("deprecated")

juniForwardRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 21)
)
juniForwardRulesGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniForwardRowStatus"),
        ("Juniper-POLICY-MIB", "juniForwardClaclId"))
)
if mibBuilder.loadTexts:
    juniForwardRulesGroup.setStatus("obsolete")

juniTrafficShapeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 22)
)
juniTrafficShapeGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniTrafficShapeRowStatus"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeId"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeProfileNextIndex"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeProfileName"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeReferenceCount"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeRate"),
        ("Juniper-POLICY-MIB", "juniTrafficShapeBurst"))
)
if mibBuilder.loadTexts:
    juniTrafficShapeGroup.setStatus("obsolete")

juniColorRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 23)
)
juniColorRulesGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniColorRowStatus"),
        ("Juniper-POLICY-MIB", "juniColor"),
        ("Juniper-POLICY-MIB", "juniColorClaclId"))
)
if mibBuilder.loadTexts:
    juniColorRulesGroup.setStatus("deprecated")

juniTrafficClassRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 24)
)
juniTrafficClassRulesGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniTrafficClassRowStatus"),
        ("Juniper-POLICY-MIB", "juniTrafficClassId"),
        ("Juniper-POLICY-MIB", "juniTrafficClassClaclId"))
)
if mibBuilder.loadTexts:
    juniTrafficClassRulesGroup.setStatus("deprecated")

juniRateLimitGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 25)
)
juniRateLimitGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniRateLimitRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitId"),
        ("Juniper-POLICY-MIB", "juniRateLimitClaclId"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileNextIndex"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileName"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileType"),
        ("Juniper-POLICY-MIB", "juniRateLimitReferenceCount"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitExcessBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitMask"))
)
if mibBuilder.loadTexts:
    juniRateLimitGroup2.setStatus("deprecated")

juniForwardRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 26)
)
juniForwardRulesGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniForwardRowStatus"),
        ("Juniper-POLICY-MIB", "juniForwardClaclId"),
        ("Juniper-POLICY-MIB", "juniForwardNextInterfaceId"),
        ("Juniper-POLICY-MIB", "juniForwardNextHop"),
        ("Juniper-POLICY-MIB", "juniForwardRouterId"),
        ("Juniper-POLICY-MIB", "juniForwardOrder"),
        ("Juniper-POLICY-MIB", "juniForwardIgnoreDefaultRoute"))
)
if mibBuilder.loadTexts:
    juniForwardRulesGroup2.setStatus("deprecated")

juniNextHopRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 27)
)
juniNextHopRulesGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniNextHopRowStatus2"),
        ("Juniper-POLICY-MIB", "juniNextHopIpAddress2"))
)
if mibBuilder.loadTexts:
    juniNextHopRulesGroup2.setStatus("current")

juniFilterRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 28)
)
juniFilterRulesGroup2.setObjects(
    ("Juniper-POLICY-MIB", "juniFilterRowStatus2")
)
if mibBuilder.loadTexts:
    juniFilterRulesGroup2.setStatus("current")

juniNextInterfaceRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 29)
)
juniNextInterfaceRulesGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniNextInterfaceRowStatus2"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceId2"),
        ("Juniper-POLICY-MIB", "juniNextInterfaceNextHop2"))
)
if mibBuilder.loadTexts:
    juniNextInterfaceRulesGroup2.setStatus("current")

juniMarkingRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 30)
)
juniMarkingRulesGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniMarkingRowStatus2"),
        ("Juniper-POLICY-MIB", "juniMarkingTOSByte2"),
        ("Juniper-POLICY-MIB", "juniMarkingMask2"))
)
if mibBuilder.loadTexts:
    juniMarkingRulesGroup2.setStatus("current")

juniColorRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 31)
)
juniColorRulesGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniColorRowStatus2"),
        ("Juniper-POLICY-MIB", "juniColor2"))
)
if mibBuilder.loadTexts:
    juniColorRulesGroup2.setStatus("current")

juniTrafficClassRulesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 32)
)
juniTrafficClassRulesGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniTrafficClassRowStatus2"),
        ("Juniper-POLICY-MIB", "juniTrafficClassId2"))
)
if mibBuilder.loadTexts:
    juniTrafficClassRulesGroup2.setStatus("current")

juniRateLimitGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 33)
)
juniRateLimitGroup3.setObjects(
      *(("Juniper-POLICY-MIB", "juniRateLimitRowStatus2"),
        ("Juniper-POLICY-MIB", "juniRateLimitId2"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileNextIndex"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileRowStatus"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileName"),
        ("Juniper-POLICY-MIB", "juniRateLimitProfileType"),
        ("Juniper-POLICY-MIB", "juniRateLimitReferenceCount"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBps"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceedBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitExcessBurst"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededAction"),
        ("Juniper-POLICY-MIB", "juniRateLimitCommittedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitConformedMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitExceededMarkVal"),
        ("Juniper-POLICY-MIB", "juniRateLimitMask"))
)
if mibBuilder.loadTexts:
    juniRateLimitGroup3.setStatus("current")

juniPolicyClaclGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 34)
)
juniPolicyClaclGrpGroup.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyClassifierGroupRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyClassifierGroupPrecedence"))
)
if mibBuilder.loadTexts:
    juniPolicyClaclGrpGroup.setStatus("current")

juniPolicyBaseGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 35)
)
juniPolicyBaseGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyAdminState"),
        ("Juniper-POLICY-MIB", "juniPolicyName"),
        ("Juniper-POLICY-MIB", "juniPolicyReferenceCount"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleType2"),
        ("Juniper-POLICY-MIB", "juniPolicySuspend2"))
)
if mibBuilder.loadTexts:
    juniPolicyBaseGroup2.setStatus("obsolete")

juniForwardRulesGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 36)
)
juniForwardRulesGroup3.setObjects(
      *(("Juniper-POLICY-MIB", "juniForwardRowStatus2"),
        ("Juniper-POLICY-MIB", "juniForwardNextInterfaceId2"),
        ("Juniper-POLICY-MIB", "juniForwardNextHop2"),
        ("Juniper-POLICY-MIB", "juniForwardRouterId2"),
        ("Juniper-POLICY-MIB", "juniForwardOrder2"),
        ("Juniper-POLICY-MIB", "juniForwardIgnoreDefaultRoute2"))
)
if mibBuilder.loadTexts:
    juniForwardRulesGroup3.setStatus("current")

juniLogRuleGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 37)
)
juniLogRuleGroup2.setObjects(
    ("Juniper-POLICY-MIB", "juniLogRowStatus2")
)
if mibBuilder.loadTexts:
    juniLogRuleGroup2.setStatus("current")

juniPolicyAttachStatisticsGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 38)
)
juniPolicyAttachStatisticsGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsGreenPackets2"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsYellowPackets2"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsRedPackets2"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsGreenBytes2"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsYellowBytes2"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsRedBytes2"))
)
if mibBuilder.loadTexts:
    juniPolicyAttachStatisticsGroup2.setStatus("current")

juniClassifierControlListGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 39)
)
juniClassifierControlListGroup3.setObjects(
      *(("Juniper-POLICY-MIB", "juniClassifierControlListNextIndex"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListRowStatus"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListName"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListReferenceCount"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNextElementIndex"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListElemRowStatus"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotSrc"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrc"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotDst"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDst"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDstMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListNotProtocol"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListProtocol"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListTosByte"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListLocal"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListLocalPresent"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSaRouteClass"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSaRouteClassPresent"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDaRouteClass"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDaRouteClassPresent"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcOperator"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcFromPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListSrcToPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestOperator"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestFromPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListDestToPort"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListICMPType"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListICMPCode"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIGMPType"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListTcpFlagsValue"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListTcpFlagsMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIpFlagsValue"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIpFlagsMask"),
        ("Juniper-POLICY-MIB", "juniClassifierControlListIpFragValue"))
)
if mibBuilder.loadTexts:
    juniClassifierControlListGroup3.setStatus("current")

juniPolicyIfAttachGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 40)
)
juniPolicyIfAttachGroup2.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyIfAttachRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachPolicyId"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsEnable"),
        ("Juniper-POLICY-MIB", "juniPolicyIfAttachStatsPreserve"))
)
if mibBuilder.loadTexts:
    juniPolicyIfAttachGroup2.setStatus("current")

juniExceptionRulesGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 41)
)
juniExceptionRulesGroup1.setObjects(
      *(("Juniper-POLICY-MIB", "juniExceptionRowStatus"),
        ("Juniper-POLICY-MIB", "juniExceptionApplication"))
)
if mibBuilder.loadTexts:
    juniExceptionRulesGroup1.setStatus("current")

juniPolicyBaseGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 2, 42)
)
juniPolicyBaseGroup3.setObjects(
      *(("Juniper-POLICY-MIB", "juniPolicyNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRowStatus"),
        ("Juniper-POLICY-MIB", "juniPolicyAdminState"),
        ("Juniper-POLICY-MIB", "juniPolicyName"),
        ("Juniper-POLICY-MIB", "juniPolicyReferenceCount"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleNextIndex"),
        ("Juniper-POLICY-MIB", "juniPolicyRuleType2"),
        ("Juniper-POLICY-MIB", "juniPolicySuspend2"),
        ("Juniper-POLICY-MIB", "juniPolicyAtmCellModeEnable"))
)
if mibBuilder.loadTexts:
    juniPolicyBaseGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniPolicyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance.setStatus(
        "obsolete"
    )

juniPolicyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance2.setStatus(
        "obsolete"
    )

juniPolicyCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance3.setStatus(
        "obsolete"
    )

juniPolicyCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance4.setStatus(
        "obsolete"
    )

juniPolicyCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance5.setStatus(
        "obsolete"
    )

juniPolicyCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance6.setStatus(
        "obsolete"
    )

juniPolicyCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 7)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance7.setStatus(
        "obsolete"
    )

juniPolicyCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 8)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance8.setStatus(
        "obsolete"
    )

juniPolicyCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 9)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance9.setStatus(
        "obsolete"
    )

juniPolicyCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 27, 2, 1, 10)
)
if mibBuilder.loadTexts:
    juniPolicyCompliance10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-POLICY-MIB",
    **{"JuniClaclPortOperator": JuniClaclPortOperator,
       "JuniPolicyAttachmentType": JuniPolicyAttachmentType,
       "JuniPolicyForwardingType": JuniPolicyForwardingType,
       "JuniPolicyIpFragValue": JuniPolicyIpFragValue,
       "JuniRateLimitProfileType": JuniRateLimitProfileType,
       "juniPolicyMIB": juniPolicyMIB,
       "juniPolicyObjects": juniPolicyObjects,
       "juniClassifierControlList": juniClassifierControlList,
       "juniClassifierControlListNextIndex": juniClassifierControlListNextIndex,
       "juniClassifierControlListTable": juniClassifierControlListTable,
       "juniClassifierControlListEntry": juniClassifierControlListEntry,
       "juniClassifierControlListId": juniClassifierControlListId,
       "juniClassifierControlListRowStatus": juniClassifierControlListRowStatus,
       "juniClassifierControlListName": juniClassifierControlListName,
       "juniClassifierControlListReferenceCount": juniClassifierControlListReferenceCount,
       "juniClassifierControlListNextElementIndex": juniClassifierControlListNextElementIndex,
       "juniClassifierControlListElementTable": juniClassifierControlListElementTable,
       "juniClassifierControlListElementEntry": juniClassifierControlListElementEntry,
       "juniClassifierControlListElemId": juniClassifierControlListElemId,
       "juniClassifierControlListElemRowStatus": juniClassifierControlListElemRowStatus,
       "juniClassifierControlListNotSrc": juniClassifierControlListNotSrc,
       "juniClassifierControlListSrc": juniClassifierControlListSrc,
       "juniClassifierControlListSrcMask": juniClassifierControlListSrcMask,
       "juniClassifierControlListNotDst": juniClassifierControlListNotDst,
       "juniClassifierControlListDst": juniClassifierControlListDst,
       "juniClassifierControlListDstMask": juniClassifierControlListDstMask,
       "juniClassifierControlListNotProtocol": juniClassifierControlListNotProtocol,
       "juniClassifierControlListProtocol": juniClassifierControlListProtocol,
       "juniClassifierControlListTosByte": juniClassifierControlListTosByte,
       "juniClassifierControlListMask": juniClassifierControlListMask,
       "juniClassifierControlListSrcOperator": juniClassifierControlListSrcOperator,
       "juniClassifierControlListSrcFromPort": juniClassifierControlListSrcFromPort,
       "juniClassifierControlListSrcToPort": juniClassifierControlListSrcToPort,
       "juniClassifierControlListDestOperator": juniClassifierControlListDestOperator,
       "juniClassifierControlListDestFromPort": juniClassifierControlListDestFromPort,
       "juniClassifierControlListDestToPort": juniClassifierControlListDestToPort,
       "juniClassifierControlListICMPType": juniClassifierControlListICMPType,
       "juniClassifierControlListICMPCode": juniClassifierControlListICMPCode,
       "juniClassifierControlListIGMPType": juniClassifierControlListIGMPType,
       "juniClassifierControlListTcpFlagsValue": juniClassifierControlListTcpFlagsValue,
       "juniClassifierControlListTcpFlagsMask": juniClassifierControlListTcpFlagsMask,
       "juniClassifierControlListIpFlagsValue": juniClassifierControlListIpFlagsValue,
       "juniClassifierControlListIpFlagsMask": juniClassifierControlListIpFlagsMask,
       "juniClassifierControlListIpFragValue": juniClassifierControlListIpFragValue,
       "juniClassifierControlListLocal": juniClassifierControlListLocal,
       "juniClassifierControlListLocalPresent": juniClassifierControlListLocalPresent,
       "juniClassifierControlListSaRouteClass": juniClassifierControlListSaRouteClass,
       "juniClassifierControlListSaRouteClassPresent": juniClassifierControlListSaRouteClassPresent,
       "juniClassifierControlListDaRouteClass": juniClassifierControlListDaRouteClass,
       "juniClassifierControlListDaRouteClassPresent": juniClassifierControlListDaRouteClassPresent,
       "juniRateLimitControlList": juniRateLimitControlList,
       "juniRateLimitProfileNextIndex": juniRateLimitProfileNextIndex,
       "juniRateLimitProfileTable": juniRateLimitProfileTable,
       "juniRateLimitProfileEntry": juniRateLimitProfileEntry,
       "juniRateLimitProfileId": juniRateLimitProfileId,
       "juniRateLimitProfileRowStatus": juniRateLimitProfileRowStatus,
       "juniRateLimitProfileName": juniRateLimitProfileName,
       "juniRateLimitReferenceCount": juniRateLimitReferenceCount,
       "juniRateLimitCommittedBps": juniRateLimitCommittedBps,
       "juniRateLimitCommittedBurst": juniRateLimitCommittedBurst,
       "juniRateLimitExceedBps": juniRateLimitExceedBps,
       "juniRateLimitExceedBurst": juniRateLimitExceedBurst,
       "juniRateLimitCommittedAction": juniRateLimitCommittedAction,
       "juniRateLimitConformedAction": juniRateLimitConformedAction,
       "juniRateLimitExceededAction": juniRateLimitExceededAction,
       "juniRateLimitCommittedMarkVal": juniRateLimitCommittedMarkVal,
       "juniRateLimitConformedMarkVal": juniRateLimitConformedMarkVal,
       "juniRateLimitExceededMarkVal": juniRateLimitExceededMarkVal,
       "juniRateLimitMask": juniRateLimitMask,
       "juniRateLimitProfileType": juniRateLimitProfileType,
       "juniRateLimitExcessBurst": juniRateLimitExcessBurst,
       "juniPolicy": juniPolicy,
       "juniPolicyNextIndex": juniPolicyNextIndex,
       "juniPolicyTable": juniPolicyTable,
       "juniPolicyEntry": juniPolicyEntry,
       "juniPolicyId": juniPolicyId,
       "juniPolicyRowStatus": juniPolicyRowStatus,
       "juniPolicyAdminState": juniPolicyAdminState,
       "juniPolicyOperStatus": juniPolicyOperStatus,
       "juniPolicyErrorValue": juniPolicyErrorValue,
       "juniPolicyName": juniPolicyName,
       "juniPolicyReferenceCount": juniPolicyReferenceCount,
       "juniPolicyRuleNextIndex": juniPolicyRuleNextIndex,
       "juniPolicyAtmCellModeEnable": juniPolicyAtmCellModeEnable,
       "juniPolicyRuleTable": juniPolicyRuleTable,
       "juniPolicyRuleEntry": juniPolicyRuleEntry,
       "juniPolicyRulePolicyId": juniPolicyRulePolicyId,
       "juniPolicyRulePrec": juniPolicyRulePrec,
       "juniPolicyRuleId": juniPolicyRuleId,
       "juniPolicyRuleType": juniPolicyRuleType,
       "juniPolicySuspend": juniPolicySuspend,
       "juniPolicyEclipsed": juniPolicyEclipsed,
       "juniNextHopRuleTable": juniNextHopRuleTable,
       "juniNextHopRuleEntry": juniNextHopRuleEntry,
       "juniNextHopRowStatus": juniNextHopRowStatus,
       "juniNextHopIpAddress": juniNextHopIpAddress,
       "juniNextHopClaclId": juniNextHopClaclId,
       "juniFilterRuleTable": juniFilterRuleTable,
       "juniFilterRuleEntry": juniFilterRuleEntry,
       "juniFilterRowStatus": juniFilterRowStatus,
       "juniFilterClaclId": juniFilterClaclId,
       "juniNextInterfaceRuleTable": juniNextInterfaceRuleTable,
       "juniNextInterfaceRuleEntry": juniNextInterfaceRuleEntry,
       "juniNextInterfaceRowStatus": juniNextInterfaceRowStatus,
       "juniNextInterfaceId": juniNextInterfaceId,
       "juniNextInterfaceClaclId": juniNextInterfaceClaclId,
       "juniNextInterfaceNextHop": juniNextInterfaceNextHop,
       "juniRateLimitRuleTable": juniRateLimitRuleTable,
       "juniRateLimitRuleEntry": juniRateLimitRuleEntry,
       "juniRateLimitRowStatus": juniRateLimitRowStatus,
       "juniRateLimitId": juniRateLimitId,
       "juniRateLimitClaclId": juniRateLimitClaclId,
       "juniMarkingRuleTable": juniMarkingRuleTable,
       "juniMarkingRuleEntry": juniMarkingRuleEntry,
       "juniMarkingRowStatus": juniMarkingRowStatus,
       "juniMarkingTOSByte": juniMarkingTOSByte,
       "juniMarkingMask": juniMarkingMask,
       "juniMarkingClaclId": juniMarkingClaclId,
       "juniForwardRuleTable": juniForwardRuleTable,
       "juniForwardRuleEntry": juniForwardRuleEntry,
       "juniForwardRowStatus": juniForwardRowStatus,
       "juniForwardClaclId": juniForwardClaclId,
       "juniForwardNextInterfaceId": juniForwardNextInterfaceId,
       "juniForwardNextHop": juniForwardNextHop,
       "juniForwardRouterId": juniForwardRouterId,
       "juniForwardOrder": juniForwardOrder,
       "juniForwardIgnoreDefaultRoute": juniForwardIgnoreDefaultRoute,
       "juniTrafficShapeRuleTable": juniTrafficShapeRuleTable,
       "juniTrafficShapeRuleEntry": juniTrafficShapeRuleEntry,
       "juniTrafficShapeRowStatus": juniTrafficShapeRowStatus,
       "juniTrafficShapeId": juniTrafficShapeId,
       "juniColorRuleTable": juniColorRuleTable,
       "juniColorRuleEntry": juniColorRuleEntry,
       "juniColorRowStatus": juniColorRowStatus,
       "juniColor": juniColor,
       "juniColorClaclId": juniColorClaclId,
       "juniLogRuleTable": juniLogRuleTable,
       "juniLogRuleEntry": juniLogRuleEntry,
       "juniLogRowStatus": juniLogRowStatus,
       "juniLogClaclId": juniLogClaclId,
       "juniTrafficClassRuleTable": juniTrafficClassRuleTable,
       "juniTrafficClassRuleEntry": juniTrafficClassRuleEntry,
       "juniTrafficClassRowStatus": juniTrafficClassRowStatus,
       "juniTrafficClassId": juniTrafficClassId,
       "juniTrafficClassClaclId": juniTrafficClassClaclId,
       "juniPolicyRule2Table": juniPolicyRule2Table,
       "juniPolicyRule2Entry": juniPolicyRule2Entry,
       "juniPolicyRulePolicyId2": juniPolicyRulePolicyId2,
       "juniPolicyRuleClaclId": juniPolicyRuleClaclId,
       "juniPolicyRuleId2": juniPolicyRuleId2,
       "juniPolicyRuleType2": juniPolicyRuleType2,
       "juniPolicySuspend2": juniPolicySuspend2,
       "juniNextHopRule2Table": juniNextHopRule2Table,
       "juniNextHopRule2Entry": juniNextHopRule2Entry,
       "juniNextHopRowStatus2": juniNextHopRowStatus2,
       "juniNextHopIpAddress2": juniNextHopIpAddress2,
       "juniFilterRule2Table": juniFilterRule2Table,
       "juniFilterRule2Entry": juniFilterRule2Entry,
       "juniFilterRowStatus2": juniFilterRowStatus2,
       "juniNextInterfaceRule2Table": juniNextInterfaceRule2Table,
       "juniNextInterfaceRule2Entry": juniNextInterfaceRule2Entry,
       "juniNextInterfaceRowStatus2": juniNextInterfaceRowStatus2,
       "juniNextInterfaceId2": juniNextInterfaceId2,
       "juniNextInterfaceNextHop2": juniNextInterfaceNextHop2,
       "juniRateLimitRule2Table": juniRateLimitRule2Table,
       "juniRateLimitRule2Entry": juniRateLimitRule2Entry,
       "juniRateLimitRowStatus2": juniRateLimitRowStatus2,
       "juniRateLimitId2": juniRateLimitId2,
       "juniMarkingRule2Table": juniMarkingRule2Table,
       "juniMarkingRule2Entry": juniMarkingRule2Entry,
       "juniMarkingRowStatus2": juniMarkingRowStatus2,
       "juniMarkingTOSByte2": juniMarkingTOSByte2,
       "juniMarkingMask2": juniMarkingMask2,
       "juniForwardRule2Table": juniForwardRule2Table,
       "juniForwardRule2Entry": juniForwardRule2Entry,
       "juniForwardRowStatus2": juniForwardRowStatus2,
       "juniForwardNextInterfaceId2": juniForwardNextInterfaceId2,
       "juniForwardNextHop2": juniForwardNextHop2,
       "juniForwardRouterId2": juniForwardRouterId2,
       "juniForwardOrder2": juniForwardOrder2,
       "juniForwardIgnoreDefaultRoute2": juniForwardIgnoreDefaultRoute2,
       "juniColorRule2Table": juniColorRule2Table,
       "juniColorRule2Entry": juniColorRule2Entry,
       "juniColorRowStatus2": juniColorRowStatus2,
       "juniColor2": juniColor2,
       "juniLogRule2Table": juniLogRule2Table,
       "juniLogRule2Entry": juniLogRule2Entry,
       "juniLogRowStatus2": juniLogRowStatus2,
       "juniTrafficClassRule2Table": juniTrafficClassRule2Table,
       "juniTrafficClassRule2Entry": juniTrafficClassRule2Entry,
       "juniTrafficClassRowStatus2": juniTrafficClassRowStatus2,
       "juniTrafficClassId2": juniTrafficClassId2,
       "juniPolicyClassifierGroupTable": juniPolicyClassifierGroupTable,
       "juniPolicyClassifierGroupEntry": juniPolicyClassifierGroupEntry,
       "juniPolicyClassifierGroupPolicyId": juniPolicyClassifierGroupPolicyId,
       "juniPolicyClassifierGroupClaclId": juniPolicyClassifierGroupClaclId,
       "juniPolicyClassifierGroupRowStatus": juniPolicyClassifierGroupRowStatus,
       "juniPolicyClassifierGroupPrecedence": juniPolicyClassifierGroupPrecedence,
       "juniExceptionRuleTable": juniExceptionRuleTable,
       "juniExceptionRuleEntry": juniExceptionRuleEntry,
       "juniExceptionRowStatus": juniExceptionRowStatus,
       "juniExceptionApplication": juniExceptionApplication,
       "juniPolicyIf": juniPolicyIf,
       "juniPolicyIfTable": juniPolicyIfTable,
       "juniPolicyIfEntry": juniPolicyIfEntry,
       "juniPolicyIfInterfaceId": juniPolicyIfInterfaceId,
       "juniPolicyIfRowStatus": juniPolicyIfRowStatus,
       "juniPolicyIfInputPolicyId": juniPolicyIfInputPolicyId,
       "juniPolicyIfOutputPolicyId": juniPolicyIfOutputPolicyId,
       "juniPolicyIfInputStatsEnable": juniPolicyIfInputStatsEnable,
       "juniPolicyIfOutputStatsEnable": juniPolicyIfOutputStatsEnable,
       "juniPolicyIfAttachTable": juniPolicyIfAttachTable,
       "juniPolicyIfAttachEntry": juniPolicyIfAttachEntry,
       "juniPolicyIfAttachInterfaceId": juniPolicyIfAttachInterfaceId,
       "juniPolicyIfAttachForwardingType": juniPolicyIfAttachForwardingType,
       "juniPolicyIfAttachPolicyType": juniPolicyIfAttachPolicyType,
       "juniPolicyIfAttachRowStatus": juniPolicyIfAttachRowStatus,
       "juniPolicyIfAttachPolicyId": juniPolicyIfAttachPolicyId,
       "juniPolicyIfAttachStatsEnable": juniPolicyIfAttachStatsEnable,
       "juniPolicyIfAttachStatsPreserve": juniPolicyIfAttachStatsPreserve,
       "juniPolicyProfile": juniPolicyProfile,
       "juniPolicyProfileTable": juniPolicyProfileTable,
       "juniPolicyProfileEntry": juniPolicyProfileEntry,
       "juniPolicyProfileId": juniPolicyProfileId,
       "juniPolicyProfileRowStatus": juniPolicyProfileRowStatus,
       "juniPolicyProfileInputPolicyId": juniPolicyProfileInputPolicyId,
       "juniPolicyProfileOutputPolicyId": juniPolicyProfileOutputPolicyId,
       "juniPolicyProfileInputStatsEnable": juniPolicyProfileInputStatsEnable,
       "juniPolicyProfileOutputStatsEnable": juniPolicyProfileOutputStatsEnable,
       "juniPolicyProfileLocalInputPolicyId": juniPolicyProfileLocalInputPolicyId,
       "juniPolicyProfileLocalInputStatsEnable": juniPolicyProfileLocalInputStatsEnable,
       "juniPolicyAttachProfileTable": juniPolicyAttachProfileTable,
       "juniPolicyAttachProfileEntry": juniPolicyAttachProfileEntry,
       "juniPolicyAttachProfileId": juniPolicyAttachProfileId,
       "juniPolicyAttachProfileForwardingType": juniPolicyAttachProfileForwardingType,
       "juniPolicyAttachProfilePolicyType": juniPolicyAttachProfilePolicyType,
       "juniPolicyAttachProfileRowStatus": juniPolicyAttachProfileRowStatus,
       "juniPolicyAttachProfilePolicyId": juniPolicyAttachProfilePolicyId,
       "juniPolicyAttachProfileStatsEnable": juniPolicyAttachProfileStatsEnable,
       "juniPolicyStatistics": juniPolicyStatistics,
       "juniPolicyIfStatsTable": juniPolicyIfStatsTable,
       "juniPolicyIfStatsEntry": juniPolicyIfStatsEntry,
       "juniPolicyIfStatsIfId": juniPolicyIfStatsIfId,
       "juniPolicyIfStatsPolicyType": juniPolicyIfStatsPolicyType,
       "juniPolicyIfStatsPolicyId": juniPolicyIfStatsPolicyId,
       "juniPolicyIfStatsRulePrec": juniPolicyIfStatsRulePrec,
       "juniPolicyIfStatsRuleId": juniPolicyIfStatsRuleId,
       "juniPolicyIfStatsClaclEntryNumber": juniPolicyIfStatsClaclEntryNumber,
       "juniPolicyIfStatsGreenPackets": juniPolicyIfStatsGreenPackets,
       "juniPolicyIfStatsYellowPackets": juniPolicyIfStatsYellowPackets,
       "juniPolicyIfStatsRedPackets": juniPolicyIfStatsRedPackets,
       "juniPolicyIfStatsGreenBytes": juniPolicyIfStatsGreenBytes,
       "juniPolicyIfStatsYellowBytes": juniPolicyIfStatsYellowBytes,
       "juniPolicyIfStatsRedBytes": juniPolicyIfStatsRedBytes,
       "juniPolicyIfAttachStatsTable": juniPolicyIfAttachStatsTable,
       "juniPolicyIfAttachStatsEntry": juniPolicyIfAttachStatsEntry,
       "juniPolicyIfAttachStatsIfId": juniPolicyIfAttachStatsIfId,
       "juniPolicyIfAttachStatsForwardingType": juniPolicyIfAttachStatsForwardingType,
       "juniPolicyIfAttachStatsPolicyType": juniPolicyIfAttachStatsPolicyType,
       "juniPolicyIfAttachStatsPolicyId": juniPolicyIfAttachStatsPolicyId,
       "juniPolicyIfAttachStatsRulePrec": juniPolicyIfAttachStatsRulePrec,
       "juniPolicyIfAttachStatsRuleId": juniPolicyIfAttachStatsRuleId,
       "juniPolicyIfAttachStatsClaclEntryNumber": juniPolicyIfAttachStatsClaclEntryNumber,
       "juniPolicyIfAttachStatsGreenPackets": juniPolicyIfAttachStatsGreenPackets,
       "juniPolicyIfAttachStatsYellowPackets": juniPolicyIfAttachStatsYellowPackets,
       "juniPolicyIfAttachStatsRedPackets": juniPolicyIfAttachStatsRedPackets,
       "juniPolicyIfAttachStatsGreenBytes": juniPolicyIfAttachStatsGreenBytes,
       "juniPolicyIfAttachStatsYellowBytes": juniPolicyIfAttachStatsYellowBytes,
       "juniPolicyIfAttachStatsRedBytes": juniPolicyIfAttachStatsRedBytes,
       "juniPolicyIfAttachStats2Table": juniPolicyIfAttachStats2Table,
       "juniPolicyIfAttachStats2Entry": juniPolicyIfAttachStats2Entry,
       "juniPolicyIfAttachStatsIfId2": juniPolicyIfAttachStatsIfId2,
       "juniPolicyIfAttachStatsForwardingType2": juniPolicyIfAttachStatsForwardingType2,
       "juniPolicyIfAttachStatsPolicyType2": juniPolicyIfAttachStatsPolicyType2,
       "juniPolicyIfAttachStatsPolicyId2": juniPolicyIfAttachStatsPolicyId2,
       "juniPolicyIfAttachStatsClaclId": juniPolicyIfAttachStatsClaclId,
       "juniPolicyIfAttachStatsClaclEntryNumber2": juniPolicyIfAttachStatsClaclEntryNumber2,
       "juniPolicyIfAttachStatsGreenPackets2": juniPolicyIfAttachStatsGreenPackets2,
       "juniPolicyIfAttachStatsYellowPackets2": juniPolicyIfAttachStatsYellowPackets2,
       "juniPolicyIfAttachStatsRedPackets2": juniPolicyIfAttachStatsRedPackets2,
       "juniPolicyIfAttachStatsGreenBytes2": juniPolicyIfAttachStatsGreenBytes2,
       "juniPolicyIfAttachStatsYellowBytes2": juniPolicyIfAttachStatsYellowBytes2,
       "juniPolicyIfAttachStatsRedBytes2": juniPolicyIfAttachStatsRedBytes2,
       "juniTrafficShapeControlList": juniTrafficShapeControlList,
       "juniTrafficShapeProfileNextIndex": juniTrafficShapeProfileNextIndex,
       "juniTrafficShapeProfileTable": juniTrafficShapeProfileTable,
       "juniTrafficShapeProfileEntry": juniTrafficShapeProfileEntry,
       "juniTrafficShapeProfileId": juniTrafficShapeProfileId,
       "juniTrafficShapeProfileRowStatus": juniTrafficShapeProfileRowStatus,
       "juniTrafficShapeProfileName": juniTrafficShapeProfileName,
       "juniTrafficShapeReferenceCount": juniTrafficShapeReferenceCount,
       "juniTrafficShapeRate": juniTrafficShapeRate,
       "juniTrafficShapeBurst": juniTrafficShapeBurst,
       "juniPolicyConformance": juniPolicyConformance,
       "juniPolicyCompliances": juniPolicyCompliances,
       "juniPolicyCompliance": juniPolicyCompliance,
       "juniPolicyCompliance2": juniPolicyCompliance2,
       "juniPolicyCompliance3": juniPolicyCompliance3,
       "juniPolicyCompliance4": juniPolicyCompliance4,
       "juniPolicyCompliance5": juniPolicyCompliance5,
       "juniPolicyCompliance6": juniPolicyCompliance6,
       "juniPolicyCompliance7": juniPolicyCompliance7,
       "juniPolicyCompliance8": juniPolicyCompliance8,
       "juniPolicyCompliance9": juniPolicyCompliance9,
       "juniPolicyCompliance10": juniPolicyCompliance10,
       "juniPolicyGroups": juniPolicyGroups,
       "juniPolicyGroup": juniPolicyGroup,
       "juniRateLimitControlListGroup": juniRateLimitControlListGroup,
       "juniClassifierControlListGroup": juniClassifierControlListGroup,
       "juniPolicyIfGroup": juniPolicyIfGroup,
       "juniPolicyProfileGroup": juniPolicyProfileGroup,
       "juniPolicyStatisticsGroup": juniPolicyStatisticsGroup,
       "juniPolicyGroup2": juniPolicyGroup2,
       "juniTrafficShapeProfileGroup": juniTrafficShapeProfileGroup,
       "juniLogRuleGroup": juniLogRuleGroup,
       "juniPolicyIfAttachGroup": juniPolicyIfAttachGroup,
       "juniPolicyProfileGroup2": juniPolicyProfileGroup2,
       "juniPolicyAttachStatisticsGroup": juniPolicyAttachStatisticsGroup,
       "juniClassifierControlListGroup2": juniClassifierControlListGroup2,
       "juniPolicyAttachProfileGroup": juniPolicyAttachProfileGroup,
       "juniPolicyBaseGroup": juniPolicyBaseGroup,
       "juniNextHopRulesGroup": juniNextHopRulesGroup,
       "juniFilterRulesGroup": juniFilterRulesGroup,
       "juniNextInterfaceRulesGroup": juniNextInterfaceRulesGroup,
       "juniRateLimitGroup": juniRateLimitGroup,
       "juniMarkingRulesGroup": juniMarkingRulesGroup,
       "juniForwardRulesGroup": juniForwardRulesGroup,
       "juniTrafficShapeGroup": juniTrafficShapeGroup,
       "juniColorRulesGroup": juniColorRulesGroup,
       "juniTrafficClassRulesGroup": juniTrafficClassRulesGroup,
       "juniRateLimitGroup2": juniRateLimitGroup2,
       "juniForwardRulesGroup2": juniForwardRulesGroup2,
       "juniNextHopRulesGroup2": juniNextHopRulesGroup2,
       "juniFilterRulesGroup2": juniFilterRulesGroup2,
       "juniNextInterfaceRulesGroup2": juniNextInterfaceRulesGroup2,
       "juniMarkingRulesGroup2": juniMarkingRulesGroup2,
       "juniColorRulesGroup2": juniColorRulesGroup2,
       "juniTrafficClassRulesGroup2": juniTrafficClassRulesGroup2,
       "juniRateLimitGroup3": juniRateLimitGroup3,
       "juniPolicyClaclGrpGroup": juniPolicyClaclGrpGroup,
       "juniPolicyBaseGroup2": juniPolicyBaseGroup2,
       "juniForwardRulesGroup3": juniForwardRulesGroup3,
       "juniLogRuleGroup2": juniLogRuleGroup2,
       "juniPolicyAttachStatisticsGroup2": juniPolicyAttachStatisticsGroup2,
       "juniClassifierControlListGroup3": juniClassifierControlListGroup3,
       "juniPolicyIfAttachGroup2": juniPolicyIfAttachGroup2,
       "juniExceptionRulesGroup1": juniExceptionRulesGroup1,
       "juniPolicyBaseGroup3": juniPolicyBaseGroup3}
)
