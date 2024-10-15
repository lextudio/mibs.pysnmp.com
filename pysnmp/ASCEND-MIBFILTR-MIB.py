# SNMP MIB module (ASCEND-MIBFILTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBFILTR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:34 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibfilterProfile_ObjectIdentity = ObjectIdentity
mibfilterProfile = _MibfilterProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 77)
)
_MibfilterProfileTable_Object = MibTable
mibfilterProfileTable = _MibfilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 1)
)
if mibBuilder.loadTexts:
    mibfilterProfileTable.setStatus("mandatory")
_MibfilterProfileEntry_Object = MibTableRow
mibfilterProfileEntry = _MibfilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 1, 1)
)
mibfilterProfileEntry.setIndexNames(
    (0, "ASCEND-MIBFILTR-MIB", "filterProfile-FilterName"),
)
if mibBuilder.loadTexts:
    mibfilterProfileEntry.setStatus("mandatory")
_FilterProfile_FilterName_Type = DisplayString
_FilterProfile_FilterName_Object = MibScalar
filterProfile_FilterName = _FilterProfile_FilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 1, 1, 1),
    _FilterProfile_FilterName_Type()
)
filterProfile_FilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProfile_FilterName.setStatus("mandatory")


class _FilterProfile_Action_o_Type(Integer32):
    """Custom type filterProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_FilterProfile_Action_o_Type.__name__ = "Integer32"
_FilterProfile_Action_o_Object = MibScalar
filterProfile_Action_o = _FilterProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 1, 1, 2),
    _FilterProfile_Action_o_Type()
)
filterProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_Action_o.setStatus("mandatory")
_MibfilterProfile_OutputFiltersTable_Object = MibTable
mibfilterProfile_OutputFiltersTable = _MibfilterProfile_OutputFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2)
)
if mibBuilder.loadTexts:
    mibfilterProfile_OutputFiltersTable.setStatus("mandatory")
_MibfilterProfile_OutputFiltersEntry_Object = MibTableRow
mibfilterProfile_OutputFiltersEntry = _MibfilterProfile_OutputFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1)
)
mibfilterProfile_OutputFiltersEntry.setIndexNames(
    (0, "ASCEND-MIBFILTR-MIB", "filterProfile-OutputFilters-FilterName"),
    (0, "ASCEND-MIBFILTR-MIB", "filterProfile-OutputFilters-Index-o"),
)
if mibBuilder.loadTexts:
    mibfilterProfile_OutputFiltersEntry.setStatus("mandatory")
_FilterProfile_OutputFilters_FilterName_Type = DisplayString
_FilterProfile_OutputFilters_FilterName_Object = MibScalar
filterProfile_OutputFilters_FilterName = _FilterProfile_OutputFilters_FilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 1),
    _FilterProfile_OutputFilters_FilterName_Type()
)
filterProfile_OutputFilters_FilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_FilterName.setStatus("mandatory")
_FilterProfile_OutputFilters_Index_o_Type = Integer32
_FilterProfile_OutputFilters_Index_o_Object = MibScalar
filterProfile_OutputFilters_Index_o = _FilterProfile_OutputFilters_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 2),
    _FilterProfile_OutputFilters_Index_o_Type()
)
filterProfile_OutputFilters_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_Index_o.setStatus("mandatory")


class _FilterProfile_OutputFilters_ValidEntry_Type(Integer32):
    """Custom type filterProfile_OutputFilters_ValidEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_OutputFilters_ValidEntry_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_ValidEntry_Object = MibScalar
filterProfile_OutputFilters_ValidEntry = _FilterProfile_OutputFilters_ValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 3),
    _FilterProfile_OutputFilters_ValidEntry_Type()
)
filterProfile_OutputFilters_ValidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_ValidEntry.setStatus("mandatory")


class _FilterProfile_OutputFilters_Forward_Type(Integer32):
    """Custom type filterProfile_OutputFilters_Forward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_OutputFilters_Forward_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_Forward_Object = MibScalar
filterProfile_OutputFilters_Forward = _FilterProfile_OutputFilters_Forward_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 4),
    _FilterProfile_OutputFilters_Forward_Type()
)
filterProfile_OutputFilters_Forward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_Forward.setStatus("mandatory")


class _FilterProfile_OutputFilters_oType_Type(Integer32):
    """Custom type filterProfile_OutputFilters_oType based on Integer32"""
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
        *(("genericFilter", 1),
          ("ipFilter", 2),
          ("ipxFilter", 4),
          ("routeFilter", 3),
          ("tosFilter", 5))
    )


_FilterProfile_OutputFilters_oType_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_oType_Object = MibScalar
filterProfile_OutputFilters_oType = _FilterProfile_OutputFilters_oType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 5),
    _FilterProfile_OutputFilters_oType_Type()
)
filterProfile_OutputFilters_oType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_oType.setStatus("mandatory")
_FilterProfile_OutputFilters_GenFilter_Offset_Type = Integer32
_FilterProfile_OutputFilters_GenFilter_Offset_Object = MibScalar
filterProfile_OutputFilters_GenFilter_Offset = _FilterProfile_OutputFilters_GenFilter_Offset_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 6),
    _FilterProfile_OutputFilters_GenFilter_Offset_Type()
)
filterProfile_OutputFilters_GenFilter_Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_GenFilter_Offset.setStatus("mandatory")
_FilterProfile_OutputFilters_GenFilter_Len_Type = Integer32
_FilterProfile_OutputFilters_GenFilter_Len_Object = MibScalar
filterProfile_OutputFilters_GenFilter_Len = _FilterProfile_OutputFilters_GenFilter_Len_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 7),
    _FilterProfile_OutputFilters_GenFilter_Len_Type()
)
filterProfile_OutputFilters_GenFilter_Len.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_GenFilter_Len.setStatus("mandatory")


class _FilterProfile_OutputFilters_GenFilter_More_Type(Integer32):
    """Custom type filterProfile_OutputFilters_GenFilter_More based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_OutputFilters_GenFilter_More_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_GenFilter_More_Object = MibScalar
filterProfile_OutputFilters_GenFilter_More = _FilterProfile_OutputFilters_GenFilter_More_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 8),
    _FilterProfile_OutputFilters_GenFilter_More_Type()
)
filterProfile_OutputFilters_GenFilter_More.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_GenFilter_More.setStatus("mandatory")


class _FilterProfile_OutputFilters_GenFilter_CompNeq_Type(Integer32):
    """Custom type filterProfile_OutputFilters_GenFilter_CompNeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_OutputFilters_GenFilter_CompNeq_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_GenFilter_CompNeq_Object = MibScalar
filterProfile_OutputFilters_GenFilter_CompNeq = _FilterProfile_OutputFilters_GenFilter_CompNeq_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 9),
    _FilterProfile_OutputFilters_GenFilter_CompNeq_Type()
)
filterProfile_OutputFilters_GenFilter_CompNeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_GenFilter_CompNeq.setStatus("mandatory")
_FilterProfile_OutputFilters_GenFilter_Mask_Type = DisplayString
_FilterProfile_OutputFilters_GenFilter_Mask_Object = MibScalar
filterProfile_OutputFilters_GenFilter_Mask = _FilterProfile_OutputFilters_GenFilter_Mask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 10),
    _FilterProfile_OutputFilters_GenFilter_Mask_Type()
)
filterProfile_OutputFilters_GenFilter_Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_GenFilter_Mask.setStatus("mandatory")
_FilterProfile_OutputFilters_GenFilter_Value_Type = DisplayString
_FilterProfile_OutputFilters_GenFilter_Value_Object = MibScalar
filterProfile_OutputFilters_GenFilter_Value = _FilterProfile_OutputFilters_GenFilter_Value_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 11),
    _FilterProfile_OutputFilters_GenFilter_Value_Type()
)
filterProfile_OutputFilters_GenFilter_Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_GenFilter_Value.setStatus("mandatory")
_FilterProfile_OutputFilters_IpFilter_Protocol_Type = Integer32
_FilterProfile_OutputFilters_IpFilter_Protocol_Object = MibScalar
filterProfile_OutputFilters_IpFilter_Protocol = _FilterProfile_OutputFilters_IpFilter_Protocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 12),
    _FilterProfile_OutputFilters_IpFilter_Protocol_Type()
)
filterProfile_OutputFilters_IpFilter_Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_Protocol.setStatus("mandatory")
_FilterProfile_OutputFilters_IpFilter_SourceAddressMask_Type = IpAddress
_FilterProfile_OutputFilters_IpFilter_SourceAddressMask_Object = MibScalar
filterProfile_OutputFilters_IpFilter_SourceAddressMask = _FilterProfile_OutputFilters_IpFilter_SourceAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 13),
    _FilterProfile_OutputFilters_IpFilter_SourceAddressMask_Type()
)
filterProfile_OutputFilters_IpFilter_SourceAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_SourceAddressMask.setStatus("mandatory")
_FilterProfile_OutputFilters_IpFilter_SourceAddress_Type = IpAddress
_FilterProfile_OutputFilters_IpFilter_SourceAddress_Object = MibScalar
filterProfile_OutputFilters_IpFilter_SourceAddress = _FilterProfile_OutputFilters_IpFilter_SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 14),
    _FilterProfile_OutputFilters_IpFilter_SourceAddress_Type()
)
filterProfile_OutputFilters_IpFilter_SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_SourceAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_IpFilter_DestAddressMask_Type = IpAddress
_FilterProfile_OutputFilters_IpFilter_DestAddressMask_Object = MibScalar
filterProfile_OutputFilters_IpFilter_DestAddressMask = _FilterProfile_OutputFilters_IpFilter_DestAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 15),
    _FilterProfile_OutputFilters_IpFilter_DestAddressMask_Type()
)
filterProfile_OutputFilters_IpFilter_DestAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_DestAddressMask.setStatus("mandatory")
_FilterProfile_OutputFilters_IpFilter_DestAddress_Type = IpAddress
_FilterProfile_OutputFilters_IpFilter_DestAddress_Object = MibScalar
filterProfile_OutputFilters_IpFilter_DestAddress = _FilterProfile_OutputFilters_IpFilter_DestAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 16),
    _FilterProfile_OutputFilters_IpFilter_DestAddress_Type()
)
filterProfile_OutputFilters_IpFilter_DestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_DestAddress.setStatus("mandatory")


class _FilterProfile_OutputFilters_IpFilter_oSrcPortCmp_Type(Integer32):
    """Custom type filterProfile_OutputFilters_IpFilter_oSrcPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_OutputFilters_IpFilter_oSrcPortCmp_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_IpFilter_oSrcPortCmp_Object = MibScalar
filterProfile_OutputFilters_IpFilter_oSrcPortCmp = _FilterProfile_OutputFilters_IpFilter_oSrcPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 17),
    _FilterProfile_OutputFilters_IpFilter_oSrcPortCmp_Type()
)
filterProfile_OutputFilters_IpFilter_oSrcPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_oSrcPortCmp.setStatus("mandatory")
_FilterProfile_OutputFilters_IpFilter_SourcePort_Type = Integer32
_FilterProfile_OutputFilters_IpFilter_SourcePort_Object = MibScalar
filterProfile_OutputFilters_IpFilter_SourcePort = _FilterProfile_OutputFilters_IpFilter_SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 18),
    _FilterProfile_OutputFilters_IpFilter_SourcePort_Type()
)
filterProfile_OutputFilters_IpFilter_SourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_SourcePort.setStatus("mandatory")


class _FilterProfile_OutputFilters_IpFilter_oDstPortCmp_Type(Integer32):
    """Custom type filterProfile_OutputFilters_IpFilter_oDstPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_OutputFilters_IpFilter_oDstPortCmp_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_IpFilter_oDstPortCmp_Object = MibScalar
filterProfile_OutputFilters_IpFilter_oDstPortCmp = _FilterProfile_OutputFilters_IpFilter_oDstPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 19),
    _FilterProfile_OutputFilters_IpFilter_oDstPortCmp_Type()
)
filterProfile_OutputFilters_IpFilter_oDstPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_oDstPortCmp.setStatus("mandatory")
_FilterProfile_OutputFilters_IpFilter_DestPort_Type = Integer32
_FilterProfile_OutputFilters_IpFilter_DestPort_Object = MibScalar
filterProfile_OutputFilters_IpFilter_DestPort = _FilterProfile_OutputFilters_IpFilter_DestPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 20),
    _FilterProfile_OutputFilters_IpFilter_DestPort_Type()
)
filterProfile_OutputFilters_IpFilter_DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_DestPort.setStatus("mandatory")


class _FilterProfile_OutputFilters_IpFilter_TcpEstab_Type(Integer32):
    """Custom type filterProfile_OutputFilters_IpFilter_TcpEstab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_OutputFilters_IpFilter_TcpEstab_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_IpFilter_TcpEstab_Object = MibScalar
filterProfile_OutputFilters_IpFilter_TcpEstab = _FilterProfile_OutputFilters_IpFilter_TcpEstab_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 21),
    _FilterProfile_OutputFilters_IpFilter_TcpEstab_Type()
)
filterProfile_OutputFilters_IpFilter_TcpEstab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpFilter_TcpEstab.setStatus("mandatory")
_FilterProfile_OutputFilters_RouteFilter_SourceAddressMask_Type = IpAddress
_FilterProfile_OutputFilters_RouteFilter_SourceAddressMask_Object = MibScalar
filterProfile_OutputFilters_RouteFilter_SourceAddressMask = _FilterProfile_OutputFilters_RouteFilter_SourceAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 22),
    _FilterProfile_OutputFilters_RouteFilter_SourceAddressMask_Type()
)
filterProfile_OutputFilters_RouteFilter_SourceAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_RouteFilter_SourceAddressMask.setStatus("mandatory")
_FilterProfile_OutputFilters_RouteFilter_SourceAddress_Type = IpAddress
_FilterProfile_OutputFilters_RouteFilter_SourceAddress_Object = MibScalar
filterProfile_OutputFilters_RouteFilter_SourceAddress = _FilterProfile_OutputFilters_RouteFilter_SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 23),
    _FilterProfile_OutputFilters_RouteFilter_SourceAddress_Type()
)
filterProfile_OutputFilters_RouteFilter_SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_RouteFilter_SourceAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_RouteFilter_RouteMask_Type = IpAddress
_FilterProfile_OutputFilters_RouteFilter_RouteMask_Object = MibScalar
filterProfile_OutputFilters_RouteFilter_RouteMask = _FilterProfile_OutputFilters_RouteFilter_RouteMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 24),
    _FilterProfile_OutputFilters_RouteFilter_RouteMask_Type()
)
filterProfile_OutputFilters_RouteFilter_RouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_RouteFilter_RouteMask.setStatus("mandatory")
_FilterProfile_OutputFilters_RouteFilter_RouteAddress_Type = IpAddress
_FilterProfile_OutputFilters_RouteFilter_RouteAddress_Object = MibScalar
filterProfile_OutputFilters_RouteFilter_RouteAddress = _FilterProfile_OutputFilters_RouteFilter_RouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 25),
    _FilterProfile_OutputFilters_RouteFilter_RouteAddress_Type()
)
filterProfile_OutputFilters_RouteFilter_RouteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_RouteFilter_RouteAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_RouteFilter_AddMetric_Type = Integer32
_FilterProfile_OutputFilters_RouteFilter_AddMetric_Object = MibScalar
filterProfile_OutputFilters_RouteFilter_AddMetric = _FilterProfile_OutputFilters_RouteFilter_AddMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 26),
    _FilterProfile_OutputFilters_RouteFilter_AddMetric_Type()
)
filterProfile_OutputFilters_RouteFilter_AddMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_RouteFilter_AddMetric.setStatus("mandatory")


class _FilterProfile_OutputFilters_RouteFilter_Action_Type(Integer32):
    """Custom type filterProfile_OutputFilters_RouteFilter_Action based on Integer32"""
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
        *(("accept", 2),
          ("add", 4),
          ("deny", 3),
          ("none", 1))
    )


_FilterProfile_OutputFilters_RouteFilter_Action_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_RouteFilter_Action_Object = MibScalar
filterProfile_OutputFilters_RouteFilter_Action = _FilterProfile_OutputFilters_RouteFilter_Action_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 27),
    _FilterProfile_OutputFilters_RouteFilter_Action_Type()
)
filterProfile_OutputFilters_RouteFilter_Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_RouteFilter_Action.setStatus("mandatory")
_FilterProfile_OutputFilters_IpxFilter_SrcNetAddress_Type = DisplayString
_FilterProfile_OutputFilters_IpxFilter_SrcNetAddress_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_SrcNetAddress = _FilterProfile_OutputFilters_IpxFilter_SrcNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 28),
    _FilterProfile_OutputFilters_IpxFilter_SrcNetAddress_Type()
)
filterProfile_OutputFilters_IpxFilter_SrcNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_SrcNetAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_IpxFilter_DestNetAddress_Type = DisplayString
_FilterProfile_OutputFilters_IpxFilter_DestNetAddress_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_DestNetAddress = _FilterProfile_OutputFilters_IpxFilter_DestNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 29),
    _FilterProfile_OutputFilters_IpxFilter_DestNetAddress_Type()
)
filterProfile_OutputFilters_IpxFilter_DestNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_DestNetAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_IpxFilter_SrcNodeAddress_Type = DisplayString
_FilterProfile_OutputFilters_IpxFilter_SrcNodeAddress_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_SrcNodeAddress = _FilterProfile_OutputFilters_IpxFilter_SrcNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 30),
    _FilterProfile_OutputFilters_IpxFilter_SrcNodeAddress_Type()
)
filterProfile_OutputFilters_IpxFilter_SrcNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_SrcNodeAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_IpxFilter_DestNodeAddress_Type = DisplayString
_FilterProfile_OutputFilters_IpxFilter_DestNodeAddress_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_DestNodeAddress = _FilterProfile_OutputFilters_IpxFilter_DestNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 31),
    _FilterProfile_OutputFilters_IpxFilter_DestNodeAddress_Type()
)
filterProfile_OutputFilters_IpxFilter_DestNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_DestNodeAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_IpxFilter_SrcSocket_Type = DisplayString
_FilterProfile_OutputFilters_IpxFilter_SrcSocket_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_SrcSocket = _FilterProfile_OutputFilters_IpxFilter_SrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 32),
    _FilterProfile_OutputFilters_IpxFilter_SrcSocket_Type()
)
filterProfile_OutputFilters_IpxFilter_SrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_SrcSocket.setStatus("mandatory")


class _FilterProfile_OutputFilters_IpxFilter_SrcSocketCmp_Type(Integer32):
    """Custom type filterProfile_OutputFilters_IpxFilter_SrcSocketCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_OutputFilters_IpxFilter_SrcSocketCmp_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_IpxFilter_SrcSocketCmp_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_SrcSocketCmp = _FilterProfile_OutputFilters_IpxFilter_SrcSocketCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 33),
    _FilterProfile_OutputFilters_IpxFilter_SrcSocketCmp_Type()
)
filterProfile_OutputFilters_IpxFilter_SrcSocketCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_SrcSocketCmp.setStatus("mandatory")
_FilterProfile_OutputFilters_IpxFilter_DestSocket_Type = Integer32
_FilterProfile_OutputFilters_IpxFilter_DestSocket_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_DestSocket = _FilterProfile_OutputFilters_IpxFilter_DestSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 34),
    _FilterProfile_OutputFilters_IpxFilter_DestSocket_Type()
)
filterProfile_OutputFilters_IpxFilter_DestSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_DestSocket.setStatus("mandatory")


class _FilterProfile_OutputFilters_IpxFilter_DstSocketCmp_Type(Integer32):
    """Custom type filterProfile_OutputFilters_IpxFilter_DstSocketCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_OutputFilters_IpxFilter_DstSocketCmp_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_IpxFilter_DstSocketCmp_Object = MibScalar
filterProfile_OutputFilters_IpxFilter_DstSocketCmp = _FilterProfile_OutputFilters_IpxFilter_DstSocketCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 35),
    _FilterProfile_OutputFilters_IpxFilter_DstSocketCmp_Type()
)
filterProfile_OutputFilters_IpxFilter_DstSocketCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_IpxFilter_DstSocketCmp.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_Protocol_Type = Integer32
_FilterProfile_OutputFilters_TosFilter_Protocol_Object = MibScalar
filterProfile_OutputFilters_TosFilter_Protocol = _FilterProfile_OutputFilters_TosFilter_Protocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 36),
    _FilterProfile_OutputFilters_TosFilter_Protocol_Type()
)
filterProfile_OutputFilters_TosFilter_Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_Protocol.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_SourceAddressMask_Type = IpAddress
_FilterProfile_OutputFilters_TosFilter_SourceAddressMask_Object = MibScalar
filterProfile_OutputFilters_TosFilter_SourceAddressMask = _FilterProfile_OutputFilters_TosFilter_SourceAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 37),
    _FilterProfile_OutputFilters_TosFilter_SourceAddressMask_Type()
)
filterProfile_OutputFilters_TosFilter_SourceAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_SourceAddressMask.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_SourceAddress_Type = IpAddress
_FilterProfile_OutputFilters_TosFilter_SourceAddress_Object = MibScalar
filterProfile_OutputFilters_TosFilter_SourceAddress = _FilterProfile_OutputFilters_TosFilter_SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 38),
    _FilterProfile_OutputFilters_TosFilter_SourceAddress_Type()
)
filterProfile_OutputFilters_TosFilter_SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_SourceAddress.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_DestAddressMask_Type = IpAddress
_FilterProfile_OutputFilters_TosFilter_DestAddressMask_Object = MibScalar
filterProfile_OutputFilters_TosFilter_DestAddressMask = _FilterProfile_OutputFilters_TosFilter_DestAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 39),
    _FilterProfile_OutputFilters_TosFilter_DestAddressMask_Type()
)
filterProfile_OutputFilters_TosFilter_DestAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_DestAddressMask.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_DestAddress_Type = IpAddress
_FilterProfile_OutputFilters_TosFilter_DestAddress_Object = MibScalar
filterProfile_OutputFilters_TosFilter_DestAddress = _FilterProfile_OutputFilters_TosFilter_DestAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 40),
    _FilterProfile_OutputFilters_TosFilter_DestAddress_Type()
)
filterProfile_OutputFilters_TosFilter_DestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_DestAddress.setStatus("mandatory")


class _FilterProfile_OutputFilters_TosFilter_oSrcPortCmp_Type(Integer32):
    """Custom type filterProfile_OutputFilters_TosFilter_oSrcPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_OutputFilters_TosFilter_oSrcPortCmp_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_TosFilter_oSrcPortCmp_Object = MibScalar
filterProfile_OutputFilters_TosFilter_oSrcPortCmp = _FilterProfile_OutputFilters_TosFilter_oSrcPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 41),
    _FilterProfile_OutputFilters_TosFilter_oSrcPortCmp_Type()
)
filterProfile_OutputFilters_TosFilter_oSrcPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_oSrcPortCmp.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_SourcePort_Type = Integer32
_FilterProfile_OutputFilters_TosFilter_SourcePort_Object = MibScalar
filterProfile_OutputFilters_TosFilter_SourcePort = _FilterProfile_OutputFilters_TosFilter_SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 42),
    _FilterProfile_OutputFilters_TosFilter_SourcePort_Type()
)
filterProfile_OutputFilters_TosFilter_SourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_SourcePort.setStatus("mandatory")


class _FilterProfile_OutputFilters_TosFilter_oDstPortCmp_Type(Integer32):
    """Custom type filterProfile_OutputFilters_TosFilter_oDstPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_OutputFilters_TosFilter_oDstPortCmp_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_TosFilter_oDstPortCmp_Object = MibScalar
filterProfile_OutputFilters_TosFilter_oDstPortCmp = _FilterProfile_OutputFilters_TosFilter_oDstPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 43),
    _FilterProfile_OutputFilters_TosFilter_oDstPortCmp_Type()
)
filterProfile_OutputFilters_TosFilter_oDstPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_oDstPortCmp.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_DestPort_Type = Integer32
_FilterProfile_OutputFilters_TosFilter_DestPort_Object = MibScalar
filterProfile_OutputFilters_TosFilter_DestPort = _FilterProfile_OutputFilters_TosFilter_DestPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 44),
    _FilterProfile_OutputFilters_TosFilter_DestPort_Type()
)
filterProfile_OutputFilters_TosFilter_DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_DestPort.setStatus("mandatory")


class _FilterProfile_OutputFilters_TosFilter_Precedence_Type(Integer32):
    """Custom type filterProfile_OutputFilters_TosFilter_Precedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              33,
              65,
              97,
              129,
              161,
              193,
              225)
        )
    )
    namedValues = NamedValues(
        *(("n-000", 1),
          ("n-001", 33),
          ("n-010", 65),
          ("n-011", 97),
          ("n-100", 129),
          ("n-101", 161),
          ("n-110", 193),
          ("n-111", 225))
    )


_FilterProfile_OutputFilters_TosFilter_Precedence_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_TosFilter_Precedence_Object = MibScalar
filterProfile_OutputFilters_TosFilter_Precedence = _FilterProfile_OutputFilters_TosFilter_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 45),
    _FilterProfile_OutputFilters_TosFilter_Precedence_Type()
)
filterProfile_OutputFilters_TosFilter_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_Precedence.setStatus("mandatory")


class _FilterProfile_OutputFilters_TosFilter_TypeOfService_Type(Integer32):
    """Custom type filterProfile_OutputFilters_TosFilter_TypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17)
        )
    )
    namedValues = NamedValues(
        *(("cost", 3),
          ("latency", 17),
          ("normal", 1),
          ("reliability", 5),
          ("throughput", 9))
    )


_FilterProfile_OutputFilters_TosFilter_TypeOfService_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_TosFilter_TypeOfService_Object = MibScalar
filterProfile_OutputFilters_TosFilter_TypeOfService = _FilterProfile_OutputFilters_TosFilter_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 46),
    _FilterProfile_OutputFilters_TosFilter_TypeOfService_Type()
)
filterProfile_OutputFilters_TosFilter_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_TypeOfService.setStatus("mandatory")


class _FilterProfile_OutputFilters_TosFilter_MarkingType_Type(Integer32):
    """Custom type filterProfile_OutputFilters_TosFilter_MarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedenceTos", 1))
    )


_FilterProfile_OutputFilters_TosFilter_MarkingType_Type.__name__ = "Integer32"
_FilterProfile_OutputFilters_TosFilter_MarkingType_Object = MibScalar
filterProfile_OutputFilters_TosFilter_MarkingType = _FilterProfile_OutputFilters_TosFilter_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 47),
    _FilterProfile_OutputFilters_TosFilter_MarkingType_Type()
)
filterProfile_OutputFilters_TosFilter_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_MarkingType.setStatus("mandatory")
_FilterProfile_OutputFilters_TosFilter_Dscp_Type = DisplayString
_FilterProfile_OutputFilters_TosFilter_Dscp_Object = MibScalar
filterProfile_OutputFilters_TosFilter_Dscp = _FilterProfile_OutputFilters_TosFilter_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 2, 1, 48),
    _FilterProfile_OutputFilters_TosFilter_Dscp_Type()
)
filterProfile_OutputFilters_TosFilter_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_OutputFilters_TosFilter_Dscp.setStatus("mandatory")
_MibfilterProfile_InputFiltersTable_Object = MibTable
mibfilterProfile_InputFiltersTable = _MibfilterProfile_InputFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3)
)
if mibBuilder.loadTexts:
    mibfilterProfile_InputFiltersTable.setStatus("mandatory")
_MibfilterProfile_InputFiltersEntry_Object = MibTableRow
mibfilterProfile_InputFiltersEntry = _MibfilterProfile_InputFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1)
)
mibfilterProfile_InputFiltersEntry.setIndexNames(
    (0, "ASCEND-MIBFILTR-MIB", "filterProfile-InputFilters-FilterName"),
    (0, "ASCEND-MIBFILTR-MIB", "filterProfile-InputFilters-Index-o"),
)
if mibBuilder.loadTexts:
    mibfilterProfile_InputFiltersEntry.setStatus("mandatory")
_FilterProfile_InputFilters_FilterName_Type = DisplayString
_FilterProfile_InputFilters_FilterName_Object = MibScalar
filterProfile_InputFilters_FilterName = _FilterProfile_InputFilters_FilterName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 1),
    _FilterProfile_InputFilters_FilterName_Type()
)
filterProfile_InputFilters_FilterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_FilterName.setStatus("mandatory")
_FilterProfile_InputFilters_Index_o_Type = Integer32
_FilterProfile_InputFilters_Index_o_Object = MibScalar
filterProfile_InputFilters_Index_o = _FilterProfile_InputFilters_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 2),
    _FilterProfile_InputFilters_Index_o_Type()
)
filterProfile_InputFilters_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_Index_o.setStatus("mandatory")


class _FilterProfile_InputFilters_ValidEntry_Type(Integer32):
    """Custom type filterProfile_InputFilters_ValidEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_InputFilters_ValidEntry_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_ValidEntry_Object = MibScalar
filterProfile_InputFilters_ValidEntry = _FilterProfile_InputFilters_ValidEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 3),
    _FilterProfile_InputFilters_ValidEntry_Type()
)
filterProfile_InputFilters_ValidEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_ValidEntry.setStatus("mandatory")


class _FilterProfile_InputFilters_Forward_Type(Integer32):
    """Custom type filterProfile_InputFilters_Forward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_InputFilters_Forward_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_Forward_Object = MibScalar
filterProfile_InputFilters_Forward = _FilterProfile_InputFilters_Forward_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 4),
    _FilterProfile_InputFilters_Forward_Type()
)
filterProfile_InputFilters_Forward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_Forward.setStatus("mandatory")


class _FilterProfile_InputFilters_oType_Type(Integer32):
    """Custom type filterProfile_InputFilters_oType based on Integer32"""
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
        *(("genericFilter", 1),
          ("ipFilter", 2),
          ("ipxFilter", 4),
          ("routeFilter", 3),
          ("tosFilter", 5))
    )


_FilterProfile_InputFilters_oType_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_oType_Object = MibScalar
filterProfile_InputFilters_oType = _FilterProfile_InputFilters_oType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 5),
    _FilterProfile_InputFilters_oType_Type()
)
filterProfile_InputFilters_oType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_oType.setStatus("mandatory")
_FilterProfile_InputFilters_GenFilter_Offset_Type = Integer32
_FilterProfile_InputFilters_GenFilter_Offset_Object = MibScalar
filterProfile_InputFilters_GenFilter_Offset = _FilterProfile_InputFilters_GenFilter_Offset_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 6),
    _FilterProfile_InputFilters_GenFilter_Offset_Type()
)
filterProfile_InputFilters_GenFilter_Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_GenFilter_Offset.setStatus("mandatory")
_FilterProfile_InputFilters_GenFilter_Len_Type = Integer32
_FilterProfile_InputFilters_GenFilter_Len_Object = MibScalar
filterProfile_InputFilters_GenFilter_Len = _FilterProfile_InputFilters_GenFilter_Len_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 7),
    _FilterProfile_InputFilters_GenFilter_Len_Type()
)
filterProfile_InputFilters_GenFilter_Len.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_GenFilter_Len.setStatus("mandatory")


class _FilterProfile_InputFilters_GenFilter_More_Type(Integer32):
    """Custom type filterProfile_InputFilters_GenFilter_More based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_InputFilters_GenFilter_More_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_GenFilter_More_Object = MibScalar
filterProfile_InputFilters_GenFilter_More = _FilterProfile_InputFilters_GenFilter_More_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 8),
    _FilterProfile_InputFilters_GenFilter_More_Type()
)
filterProfile_InputFilters_GenFilter_More.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_GenFilter_More.setStatus("mandatory")


class _FilterProfile_InputFilters_GenFilter_CompNeq_Type(Integer32):
    """Custom type filterProfile_InputFilters_GenFilter_CompNeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_InputFilters_GenFilter_CompNeq_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_GenFilter_CompNeq_Object = MibScalar
filterProfile_InputFilters_GenFilter_CompNeq = _FilterProfile_InputFilters_GenFilter_CompNeq_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 9),
    _FilterProfile_InputFilters_GenFilter_CompNeq_Type()
)
filterProfile_InputFilters_GenFilter_CompNeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_GenFilter_CompNeq.setStatus("mandatory")
_FilterProfile_InputFilters_GenFilter_Mask_Type = DisplayString
_FilterProfile_InputFilters_GenFilter_Mask_Object = MibScalar
filterProfile_InputFilters_GenFilter_Mask = _FilterProfile_InputFilters_GenFilter_Mask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 10),
    _FilterProfile_InputFilters_GenFilter_Mask_Type()
)
filterProfile_InputFilters_GenFilter_Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_GenFilter_Mask.setStatus("mandatory")
_FilterProfile_InputFilters_GenFilter_Value_Type = DisplayString
_FilterProfile_InputFilters_GenFilter_Value_Object = MibScalar
filterProfile_InputFilters_GenFilter_Value = _FilterProfile_InputFilters_GenFilter_Value_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 11),
    _FilterProfile_InputFilters_GenFilter_Value_Type()
)
filterProfile_InputFilters_GenFilter_Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_GenFilter_Value.setStatus("mandatory")
_FilterProfile_InputFilters_IpFilter_Protocol_Type = Integer32
_FilterProfile_InputFilters_IpFilter_Protocol_Object = MibScalar
filterProfile_InputFilters_IpFilter_Protocol = _FilterProfile_InputFilters_IpFilter_Protocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 12),
    _FilterProfile_InputFilters_IpFilter_Protocol_Type()
)
filterProfile_InputFilters_IpFilter_Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_Protocol.setStatus("mandatory")
_FilterProfile_InputFilters_IpFilter_SourceAddressMask_Type = IpAddress
_FilterProfile_InputFilters_IpFilter_SourceAddressMask_Object = MibScalar
filterProfile_InputFilters_IpFilter_SourceAddressMask = _FilterProfile_InputFilters_IpFilter_SourceAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 13),
    _FilterProfile_InputFilters_IpFilter_SourceAddressMask_Type()
)
filterProfile_InputFilters_IpFilter_SourceAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_SourceAddressMask.setStatus("mandatory")
_FilterProfile_InputFilters_IpFilter_SourceAddress_Type = IpAddress
_FilterProfile_InputFilters_IpFilter_SourceAddress_Object = MibScalar
filterProfile_InputFilters_IpFilter_SourceAddress = _FilterProfile_InputFilters_IpFilter_SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 14),
    _FilterProfile_InputFilters_IpFilter_SourceAddress_Type()
)
filterProfile_InputFilters_IpFilter_SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_SourceAddress.setStatus("mandatory")
_FilterProfile_InputFilters_IpFilter_DestAddressMask_Type = IpAddress
_FilterProfile_InputFilters_IpFilter_DestAddressMask_Object = MibScalar
filterProfile_InputFilters_IpFilter_DestAddressMask = _FilterProfile_InputFilters_IpFilter_DestAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 15),
    _FilterProfile_InputFilters_IpFilter_DestAddressMask_Type()
)
filterProfile_InputFilters_IpFilter_DestAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_DestAddressMask.setStatus("mandatory")
_FilterProfile_InputFilters_IpFilter_DestAddress_Type = IpAddress
_FilterProfile_InputFilters_IpFilter_DestAddress_Object = MibScalar
filterProfile_InputFilters_IpFilter_DestAddress = _FilterProfile_InputFilters_IpFilter_DestAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 16),
    _FilterProfile_InputFilters_IpFilter_DestAddress_Type()
)
filterProfile_InputFilters_IpFilter_DestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_DestAddress.setStatus("mandatory")


class _FilterProfile_InputFilters_IpFilter_oSrcPortCmp_Type(Integer32):
    """Custom type filterProfile_InputFilters_IpFilter_oSrcPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_InputFilters_IpFilter_oSrcPortCmp_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_IpFilter_oSrcPortCmp_Object = MibScalar
filterProfile_InputFilters_IpFilter_oSrcPortCmp = _FilterProfile_InputFilters_IpFilter_oSrcPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 17),
    _FilterProfile_InputFilters_IpFilter_oSrcPortCmp_Type()
)
filterProfile_InputFilters_IpFilter_oSrcPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_oSrcPortCmp.setStatus("mandatory")
_FilterProfile_InputFilters_IpFilter_SourcePort_Type = Integer32
_FilterProfile_InputFilters_IpFilter_SourcePort_Object = MibScalar
filterProfile_InputFilters_IpFilter_SourcePort = _FilterProfile_InputFilters_IpFilter_SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 18),
    _FilterProfile_InputFilters_IpFilter_SourcePort_Type()
)
filterProfile_InputFilters_IpFilter_SourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_SourcePort.setStatus("mandatory")


class _FilterProfile_InputFilters_IpFilter_oDstPortCmp_Type(Integer32):
    """Custom type filterProfile_InputFilters_IpFilter_oDstPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_InputFilters_IpFilter_oDstPortCmp_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_IpFilter_oDstPortCmp_Object = MibScalar
filterProfile_InputFilters_IpFilter_oDstPortCmp = _FilterProfile_InputFilters_IpFilter_oDstPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 19),
    _FilterProfile_InputFilters_IpFilter_oDstPortCmp_Type()
)
filterProfile_InputFilters_IpFilter_oDstPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_oDstPortCmp.setStatus("mandatory")
_FilterProfile_InputFilters_IpFilter_DestPort_Type = Integer32
_FilterProfile_InputFilters_IpFilter_DestPort_Object = MibScalar
filterProfile_InputFilters_IpFilter_DestPort = _FilterProfile_InputFilters_IpFilter_DestPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 20),
    _FilterProfile_InputFilters_IpFilter_DestPort_Type()
)
filterProfile_InputFilters_IpFilter_DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_DestPort.setStatus("mandatory")


class _FilterProfile_InputFilters_IpFilter_TcpEstab_Type(Integer32):
    """Custom type filterProfile_InputFilters_IpFilter_TcpEstab based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FilterProfile_InputFilters_IpFilter_TcpEstab_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_IpFilter_TcpEstab_Object = MibScalar
filterProfile_InputFilters_IpFilter_TcpEstab = _FilterProfile_InputFilters_IpFilter_TcpEstab_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 21),
    _FilterProfile_InputFilters_IpFilter_TcpEstab_Type()
)
filterProfile_InputFilters_IpFilter_TcpEstab.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpFilter_TcpEstab.setStatus("mandatory")
_FilterProfile_InputFilters_RouteFilter_SourceAddressMask_Type = IpAddress
_FilterProfile_InputFilters_RouteFilter_SourceAddressMask_Object = MibScalar
filterProfile_InputFilters_RouteFilter_SourceAddressMask = _FilterProfile_InputFilters_RouteFilter_SourceAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 22),
    _FilterProfile_InputFilters_RouteFilter_SourceAddressMask_Type()
)
filterProfile_InputFilters_RouteFilter_SourceAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_RouteFilter_SourceAddressMask.setStatus("mandatory")
_FilterProfile_InputFilters_RouteFilter_SourceAddress_Type = IpAddress
_FilterProfile_InputFilters_RouteFilter_SourceAddress_Object = MibScalar
filterProfile_InputFilters_RouteFilter_SourceAddress = _FilterProfile_InputFilters_RouteFilter_SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 23),
    _FilterProfile_InputFilters_RouteFilter_SourceAddress_Type()
)
filterProfile_InputFilters_RouteFilter_SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_RouteFilter_SourceAddress.setStatus("mandatory")
_FilterProfile_InputFilters_RouteFilter_RouteMask_Type = IpAddress
_FilterProfile_InputFilters_RouteFilter_RouteMask_Object = MibScalar
filterProfile_InputFilters_RouteFilter_RouteMask = _FilterProfile_InputFilters_RouteFilter_RouteMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 24),
    _FilterProfile_InputFilters_RouteFilter_RouteMask_Type()
)
filterProfile_InputFilters_RouteFilter_RouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_RouteFilter_RouteMask.setStatus("mandatory")
_FilterProfile_InputFilters_RouteFilter_RouteAddress_Type = IpAddress
_FilterProfile_InputFilters_RouteFilter_RouteAddress_Object = MibScalar
filterProfile_InputFilters_RouteFilter_RouteAddress = _FilterProfile_InputFilters_RouteFilter_RouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 25),
    _FilterProfile_InputFilters_RouteFilter_RouteAddress_Type()
)
filterProfile_InputFilters_RouteFilter_RouteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_RouteFilter_RouteAddress.setStatus("mandatory")
_FilterProfile_InputFilters_RouteFilter_AddMetric_Type = Integer32
_FilterProfile_InputFilters_RouteFilter_AddMetric_Object = MibScalar
filterProfile_InputFilters_RouteFilter_AddMetric = _FilterProfile_InputFilters_RouteFilter_AddMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 26),
    _FilterProfile_InputFilters_RouteFilter_AddMetric_Type()
)
filterProfile_InputFilters_RouteFilter_AddMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_RouteFilter_AddMetric.setStatus("mandatory")


class _FilterProfile_InputFilters_RouteFilter_Action_Type(Integer32):
    """Custom type filterProfile_InputFilters_RouteFilter_Action based on Integer32"""
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
        *(("accept", 2),
          ("add", 4),
          ("deny", 3),
          ("none", 1))
    )


_FilterProfile_InputFilters_RouteFilter_Action_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_RouteFilter_Action_Object = MibScalar
filterProfile_InputFilters_RouteFilter_Action = _FilterProfile_InputFilters_RouteFilter_Action_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 27),
    _FilterProfile_InputFilters_RouteFilter_Action_Type()
)
filterProfile_InputFilters_RouteFilter_Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_RouteFilter_Action.setStatus("mandatory")
_FilterProfile_InputFilters_IpxFilter_SrcNetAddress_Type = DisplayString
_FilterProfile_InputFilters_IpxFilter_SrcNetAddress_Object = MibScalar
filterProfile_InputFilters_IpxFilter_SrcNetAddress = _FilterProfile_InputFilters_IpxFilter_SrcNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 28),
    _FilterProfile_InputFilters_IpxFilter_SrcNetAddress_Type()
)
filterProfile_InputFilters_IpxFilter_SrcNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_SrcNetAddress.setStatus("mandatory")
_FilterProfile_InputFilters_IpxFilter_DestNetAddress_Type = DisplayString
_FilterProfile_InputFilters_IpxFilter_DestNetAddress_Object = MibScalar
filterProfile_InputFilters_IpxFilter_DestNetAddress = _FilterProfile_InputFilters_IpxFilter_DestNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 29),
    _FilterProfile_InputFilters_IpxFilter_DestNetAddress_Type()
)
filterProfile_InputFilters_IpxFilter_DestNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_DestNetAddress.setStatus("mandatory")
_FilterProfile_InputFilters_IpxFilter_SrcNodeAddress_Type = DisplayString
_FilterProfile_InputFilters_IpxFilter_SrcNodeAddress_Object = MibScalar
filterProfile_InputFilters_IpxFilter_SrcNodeAddress = _FilterProfile_InputFilters_IpxFilter_SrcNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 30),
    _FilterProfile_InputFilters_IpxFilter_SrcNodeAddress_Type()
)
filterProfile_InputFilters_IpxFilter_SrcNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_SrcNodeAddress.setStatus("mandatory")
_FilterProfile_InputFilters_IpxFilter_DestNodeAddress_Type = DisplayString
_FilterProfile_InputFilters_IpxFilter_DestNodeAddress_Object = MibScalar
filterProfile_InputFilters_IpxFilter_DestNodeAddress = _FilterProfile_InputFilters_IpxFilter_DestNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 31),
    _FilterProfile_InputFilters_IpxFilter_DestNodeAddress_Type()
)
filterProfile_InputFilters_IpxFilter_DestNodeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_DestNodeAddress.setStatus("mandatory")
_FilterProfile_InputFilters_IpxFilter_SrcSocket_Type = DisplayString
_FilterProfile_InputFilters_IpxFilter_SrcSocket_Object = MibScalar
filterProfile_InputFilters_IpxFilter_SrcSocket = _FilterProfile_InputFilters_IpxFilter_SrcSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 32),
    _FilterProfile_InputFilters_IpxFilter_SrcSocket_Type()
)
filterProfile_InputFilters_IpxFilter_SrcSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_SrcSocket.setStatus("mandatory")


class _FilterProfile_InputFilters_IpxFilter_SrcSocketCmp_Type(Integer32):
    """Custom type filterProfile_InputFilters_IpxFilter_SrcSocketCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_InputFilters_IpxFilter_SrcSocketCmp_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_IpxFilter_SrcSocketCmp_Object = MibScalar
filterProfile_InputFilters_IpxFilter_SrcSocketCmp = _FilterProfile_InputFilters_IpxFilter_SrcSocketCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 33),
    _FilterProfile_InputFilters_IpxFilter_SrcSocketCmp_Type()
)
filterProfile_InputFilters_IpxFilter_SrcSocketCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_SrcSocketCmp.setStatus("mandatory")
_FilterProfile_InputFilters_IpxFilter_DestSocket_Type = Integer32
_FilterProfile_InputFilters_IpxFilter_DestSocket_Object = MibScalar
filterProfile_InputFilters_IpxFilter_DestSocket = _FilterProfile_InputFilters_IpxFilter_DestSocket_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 34),
    _FilterProfile_InputFilters_IpxFilter_DestSocket_Type()
)
filterProfile_InputFilters_IpxFilter_DestSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_DestSocket.setStatus("mandatory")


class _FilterProfile_InputFilters_IpxFilter_DstSocketCmp_Type(Integer32):
    """Custom type filterProfile_InputFilters_IpxFilter_DstSocketCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_InputFilters_IpxFilter_DstSocketCmp_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_IpxFilter_DstSocketCmp_Object = MibScalar
filterProfile_InputFilters_IpxFilter_DstSocketCmp = _FilterProfile_InputFilters_IpxFilter_DstSocketCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 35),
    _FilterProfile_InputFilters_IpxFilter_DstSocketCmp_Type()
)
filterProfile_InputFilters_IpxFilter_DstSocketCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_IpxFilter_DstSocketCmp.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_Protocol_Type = Integer32
_FilterProfile_InputFilters_TosFilter_Protocol_Object = MibScalar
filterProfile_InputFilters_TosFilter_Protocol = _FilterProfile_InputFilters_TosFilter_Protocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 36),
    _FilterProfile_InputFilters_TosFilter_Protocol_Type()
)
filterProfile_InputFilters_TosFilter_Protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_Protocol.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_SourceAddressMask_Type = IpAddress
_FilterProfile_InputFilters_TosFilter_SourceAddressMask_Object = MibScalar
filterProfile_InputFilters_TosFilter_SourceAddressMask = _FilterProfile_InputFilters_TosFilter_SourceAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 37),
    _FilterProfile_InputFilters_TosFilter_SourceAddressMask_Type()
)
filterProfile_InputFilters_TosFilter_SourceAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_SourceAddressMask.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_SourceAddress_Type = IpAddress
_FilterProfile_InputFilters_TosFilter_SourceAddress_Object = MibScalar
filterProfile_InputFilters_TosFilter_SourceAddress = _FilterProfile_InputFilters_TosFilter_SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 38),
    _FilterProfile_InputFilters_TosFilter_SourceAddress_Type()
)
filterProfile_InputFilters_TosFilter_SourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_SourceAddress.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_DestAddressMask_Type = IpAddress
_FilterProfile_InputFilters_TosFilter_DestAddressMask_Object = MibScalar
filterProfile_InputFilters_TosFilter_DestAddressMask = _FilterProfile_InputFilters_TosFilter_DestAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 39),
    _FilterProfile_InputFilters_TosFilter_DestAddressMask_Type()
)
filterProfile_InputFilters_TosFilter_DestAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_DestAddressMask.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_DestAddress_Type = IpAddress
_FilterProfile_InputFilters_TosFilter_DestAddress_Object = MibScalar
filterProfile_InputFilters_TosFilter_DestAddress = _FilterProfile_InputFilters_TosFilter_DestAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 40),
    _FilterProfile_InputFilters_TosFilter_DestAddress_Type()
)
filterProfile_InputFilters_TosFilter_DestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_DestAddress.setStatus("mandatory")


class _FilterProfile_InputFilters_TosFilter_oSrcPortCmp_Type(Integer32):
    """Custom type filterProfile_InputFilters_TosFilter_oSrcPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_InputFilters_TosFilter_oSrcPortCmp_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_TosFilter_oSrcPortCmp_Object = MibScalar
filterProfile_InputFilters_TosFilter_oSrcPortCmp = _FilterProfile_InputFilters_TosFilter_oSrcPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 41),
    _FilterProfile_InputFilters_TosFilter_oSrcPortCmp_Type()
)
filterProfile_InputFilters_TosFilter_oSrcPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_oSrcPortCmp.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_SourcePort_Type = Integer32
_FilterProfile_InputFilters_TosFilter_SourcePort_Object = MibScalar
filterProfile_InputFilters_TosFilter_SourcePort = _FilterProfile_InputFilters_TosFilter_SourcePort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 42),
    _FilterProfile_InputFilters_TosFilter_SourcePort_Type()
)
filterProfile_InputFilters_TosFilter_SourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_SourcePort.setStatus("mandatory")


class _FilterProfile_InputFilters_TosFilter_oDstPortCmp_Type(Integer32):
    """Custom type filterProfile_InputFilters_TosFilter_oDstPortCmp based on Integer32"""
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
        *(("eql", 3),
          ("gtr", 4),
          ("less", 2),
          ("neq", 5),
          ("none", 1))
    )


_FilterProfile_InputFilters_TosFilter_oDstPortCmp_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_TosFilter_oDstPortCmp_Object = MibScalar
filterProfile_InputFilters_TosFilter_oDstPortCmp = _FilterProfile_InputFilters_TosFilter_oDstPortCmp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 43),
    _FilterProfile_InputFilters_TosFilter_oDstPortCmp_Type()
)
filterProfile_InputFilters_TosFilter_oDstPortCmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_oDstPortCmp.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_DestPort_Type = Integer32
_FilterProfile_InputFilters_TosFilter_DestPort_Object = MibScalar
filterProfile_InputFilters_TosFilter_DestPort = _FilterProfile_InputFilters_TosFilter_DestPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 44),
    _FilterProfile_InputFilters_TosFilter_DestPort_Type()
)
filterProfile_InputFilters_TosFilter_DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_DestPort.setStatus("mandatory")


class _FilterProfile_InputFilters_TosFilter_Precedence_Type(Integer32):
    """Custom type filterProfile_InputFilters_TosFilter_Precedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              33,
              65,
              97,
              129,
              161,
              193,
              225)
        )
    )
    namedValues = NamedValues(
        *(("n-000", 1),
          ("n-001", 33),
          ("n-010", 65),
          ("n-011", 97),
          ("n-100", 129),
          ("n-101", 161),
          ("n-110", 193),
          ("n-111", 225))
    )


_FilterProfile_InputFilters_TosFilter_Precedence_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_TosFilter_Precedence_Object = MibScalar
filterProfile_InputFilters_TosFilter_Precedence = _FilterProfile_InputFilters_TosFilter_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 45),
    _FilterProfile_InputFilters_TosFilter_Precedence_Type()
)
filterProfile_InputFilters_TosFilter_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_Precedence.setStatus("mandatory")


class _FilterProfile_InputFilters_TosFilter_TypeOfService_Type(Integer32):
    """Custom type filterProfile_InputFilters_TosFilter_TypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17)
        )
    )
    namedValues = NamedValues(
        *(("cost", 3),
          ("latency", 17),
          ("normal", 1),
          ("reliability", 5),
          ("throughput", 9))
    )


_FilterProfile_InputFilters_TosFilter_TypeOfService_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_TosFilter_TypeOfService_Object = MibScalar
filterProfile_InputFilters_TosFilter_TypeOfService = _FilterProfile_InputFilters_TosFilter_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 46),
    _FilterProfile_InputFilters_TosFilter_TypeOfService_Type()
)
filterProfile_InputFilters_TosFilter_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_TypeOfService.setStatus("mandatory")


class _FilterProfile_InputFilters_TosFilter_MarkingType_Type(Integer32):
    """Custom type filterProfile_InputFilters_TosFilter_MarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedenceTos", 1))
    )


_FilterProfile_InputFilters_TosFilter_MarkingType_Type.__name__ = "Integer32"
_FilterProfile_InputFilters_TosFilter_MarkingType_Object = MibScalar
filterProfile_InputFilters_TosFilter_MarkingType = _FilterProfile_InputFilters_TosFilter_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 47),
    _FilterProfile_InputFilters_TosFilter_MarkingType_Type()
)
filterProfile_InputFilters_TosFilter_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_MarkingType.setStatus("mandatory")
_FilterProfile_InputFilters_TosFilter_Dscp_Type = DisplayString
_FilterProfile_InputFilters_TosFilter_Dscp_Object = MibScalar
filterProfile_InputFilters_TosFilter_Dscp = _FilterProfile_InputFilters_TosFilter_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 77, 3, 1, 48),
    _FilterProfile_InputFilters_TosFilter_Dscp_Type()
)
filterProfile_InputFilters_TosFilter_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterProfile_InputFilters_TosFilter_Dscp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBFILTR-MIB",
    **{"DisplayString": DisplayString,
       "mibfilterProfile": mibfilterProfile,
       "mibfilterProfileTable": mibfilterProfileTable,
       "mibfilterProfileEntry": mibfilterProfileEntry,
       "filterProfile-FilterName": filterProfile_FilterName,
       "filterProfile-Action-o": filterProfile_Action_o,
       "mibfilterProfile-OutputFiltersTable": mibfilterProfile_OutputFiltersTable,
       "mibfilterProfile-OutputFiltersEntry": mibfilterProfile_OutputFiltersEntry,
       "filterProfile-OutputFilters-FilterName": filterProfile_OutputFilters_FilterName,
       "filterProfile-OutputFilters-Index-o": filterProfile_OutputFilters_Index_o,
       "filterProfile-OutputFilters-ValidEntry": filterProfile_OutputFilters_ValidEntry,
       "filterProfile-OutputFilters-Forward": filterProfile_OutputFilters_Forward,
       "filterProfile-OutputFilters-oType": filterProfile_OutputFilters_oType,
       "filterProfile-OutputFilters-GenFilter-Offset": filterProfile_OutputFilters_GenFilter_Offset,
       "filterProfile-OutputFilters-GenFilter-Len": filterProfile_OutputFilters_GenFilter_Len,
       "filterProfile-OutputFilters-GenFilter-More": filterProfile_OutputFilters_GenFilter_More,
       "filterProfile-OutputFilters-GenFilter-CompNeq": filterProfile_OutputFilters_GenFilter_CompNeq,
       "filterProfile-OutputFilters-GenFilter-Mask": filterProfile_OutputFilters_GenFilter_Mask,
       "filterProfile-OutputFilters-GenFilter-Value": filterProfile_OutputFilters_GenFilter_Value,
       "filterProfile-OutputFilters-IpFilter-Protocol": filterProfile_OutputFilters_IpFilter_Protocol,
       "filterProfile-OutputFilters-IpFilter-SourceAddressMask": filterProfile_OutputFilters_IpFilter_SourceAddressMask,
       "filterProfile-OutputFilters-IpFilter-SourceAddress": filterProfile_OutputFilters_IpFilter_SourceAddress,
       "filterProfile-OutputFilters-IpFilter-DestAddressMask": filterProfile_OutputFilters_IpFilter_DestAddressMask,
       "filterProfile-OutputFilters-IpFilter-DestAddress": filterProfile_OutputFilters_IpFilter_DestAddress,
       "filterProfile-OutputFilters-IpFilter-oSrcPortCmp": filterProfile_OutputFilters_IpFilter_oSrcPortCmp,
       "filterProfile-OutputFilters-IpFilter-SourcePort": filterProfile_OutputFilters_IpFilter_SourcePort,
       "filterProfile-OutputFilters-IpFilter-oDstPortCmp": filterProfile_OutputFilters_IpFilter_oDstPortCmp,
       "filterProfile-OutputFilters-IpFilter-DestPort": filterProfile_OutputFilters_IpFilter_DestPort,
       "filterProfile-OutputFilters-IpFilter-TcpEstab": filterProfile_OutputFilters_IpFilter_TcpEstab,
       "filterProfile-OutputFilters-RouteFilter-SourceAddressMask": filterProfile_OutputFilters_RouteFilter_SourceAddressMask,
       "filterProfile-OutputFilters-RouteFilter-SourceAddress": filterProfile_OutputFilters_RouteFilter_SourceAddress,
       "filterProfile-OutputFilters-RouteFilter-RouteMask": filterProfile_OutputFilters_RouteFilter_RouteMask,
       "filterProfile-OutputFilters-RouteFilter-RouteAddress": filterProfile_OutputFilters_RouteFilter_RouteAddress,
       "filterProfile-OutputFilters-RouteFilter-AddMetric": filterProfile_OutputFilters_RouteFilter_AddMetric,
       "filterProfile-OutputFilters-RouteFilter-Action": filterProfile_OutputFilters_RouteFilter_Action,
       "filterProfile-OutputFilters-IpxFilter-SrcNetAddress": filterProfile_OutputFilters_IpxFilter_SrcNetAddress,
       "filterProfile-OutputFilters-IpxFilter-DestNetAddress": filterProfile_OutputFilters_IpxFilter_DestNetAddress,
       "filterProfile-OutputFilters-IpxFilter-SrcNodeAddress": filterProfile_OutputFilters_IpxFilter_SrcNodeAddress,
       "filterProfile-OutputFilters-IpxFilter-DestNodeAddress": filterProfile_OutputFilters_IpxFilter_DestNodeAddress,
       "filterProfile-OutputFilters-IpxFilter-SrcSocket": filterProfile_OutputFilters_IpxFilter_SrcSocket,
       "filterProfile-OutputFilters-IpxFilter-SrcSocketCmp": filterProfile_OutputFilters_IpxFilter_SrcSocketCmp,
       "filterProfile-OutputFilters-IpxFilter-DestSocket": filterProfile_OutputFilters_IpxFilter_DestSocket,
       "filterProfile-OutputFilters-IpxFilter-DstSocketCmp": filterProfile_OutputFilters_IpxFilter_DstSocketCmp,
       "filterProfile-OutputFilters-TosFilter-Protocol": filterProfile_OutputFilters_TosFilter_Protocol,
       "filterProfile-OutputFilters-TosFilter-SourceAddressMask": filterProfile_OutputFilters_TosFilter_SourceAddressMask,
       "filterProfile-OutputFilters-TosFilter-SourceAddress": filterProfile_OutputFilters_TosFilter_SourceAddress,
       "filterProfile-OutputFilters-TosFilter-DestAddressMask": filterProfile_OutputFilters_TosFilter_DestAddressMask,
       "filterProfile-OutputFilters-TosFilter-DestAddress": filterProfile_OutputFilters_TosFilter_DestAddress,
       "filterProfile-OutputFilters-TosFilter-oSrcPortCmp": filterProfile_OutputFilters_TosFilter_oSrcPortCmp,
       "filterProfile-OutputFilters-TosFilter-SourcePort": filterProfile_OutputFilters_TosFilter_SourcePort,
       "filterProfile-OutputFilters-TosFilter-oDstPortCmp": filterProfile_OutputFilters_TosFilter_oDstPortCmp,
       "filterProfile-OutputFilters-TosFilter-DestPort": filterProfile_OutputFilters_TosFilter_DestPort,
       "filterProfile-OutputFilters-TosFilter-Precedence": filterProfile_OutputFilters_TosFilter_Precedence,
       "filterProfile-OutputFilters-TosFilter-TypeOfService": filterProfile_OutputFilters_TosFilter_TypeOfService,
       "filterProfile-OutputFilters-TosFilter-MarkingType": filterProfile_OutputFilters_TosFilter_MarkingType,
       "filterProfile-OutputFilters-TosFilter-Dscp": filterProfile_OutputFilters_TosFilter_Dscp,
       "mibfilterProfile-InputFiltersTable": mibfilterProfile_InputFiltersTable,
       "mibfilterProfile-InputFiltersEntry": mibfilterProfile_InputFiltersEntry,
       "filterProfile-InputFilters-FilterName": filterProfile_InputFilters_FilterName,
       "filterProfile-InputFilters-Index-o": filterProfile_InputFilters_Index_o,
       "filterProfile-InputFilters-ValidEntry": filterProfile_InputFilters_ValidEntry,
       "filterProfile-InputFilters-Forward": filterProfile_InputFilters_Forward,
       "filterProfile-InputFilters-oType": filterProfile_InputFilters_oType,
       "filterProfile-InputFilters-GenFilter-Offset": filterProfile_InputFilters_GenFilter_Offset,
       "filterProfile-InputFilters-GenFilter-Len": filterProfile_InputFilters_GenFilter_Len,
       "filterProfile-InputFilters-GenFilter-More": filterProfile_InputFilters_GenFilter_More,
       "filterProfile-InputFilters-GenFilter-CompNeq": filterProfile_InputFilters_GenFilter_CompNeq,
       "filterProfile-InputFilters-GenFilter-Mask": filterProfile_InputFilters_GenFilter_Mask,
       "filterProfile-InputFilters-GenFilter-Value": filterProfile_InputFilters_GenFilter_Value,
       "filterProfile-InputFilters-IpFilter-Protocol": filterProfile_InputFilters_IpFilter_Protocol,
       "filterProfile-InputFilters-IpFilter-SourceAddressMask": filterProfile_InputFilters_IpFilter_SourceAddressMask,
       "filterProfile-InputFilters-IpFilter-SourceAddress": filterProfile_InputFilters_IpFilter_SourceAddress,
       "filterProfile-InputFilters-IpFilter-DestAddressMask": filterProfile_InputFilters_IpFilter_DestAddressMask,
       "filterProfile-InputFilters-IpFilter-DestAddress": filterProfile_InputFilters_IpFilter_DestAddress,
       "filterProfile-InputFilters-IpFilter-oSrcPortCmp": filterProfile_InputFilters_IpFilter_oSrcPortCmp,
       "filterProfile-InputFilters-IpFilter-SourcePort": filterProfile_InputFilters_IpFilter_SourcePort,
       "filterProfile-InputFilters-IpFilter-oDstPortCmp": filterProfile_InputFilters_IpFilter_oDstPortCmp,
       "filterProfile-InputFilters-IpFilter-DestPort": filterProfile_InputFilters_IpFilter_DestPort,
       "filterProfile-InputFilters-IpFilter-TcpEstab": filterProfile_InputFilters_IpFilter_TcpEstab,
       "filterProfile-InputFilters-RouteFilter-SourceAddressMask": filterProfile_InputFilters_RouteFilter_SourceAddressMask,
       "filterProfile-InputFilters-RouteFilter-SourceAddress": filterProfile_InputFilters_RouteFilter_SourceAddress,
       "filterProfile-InputFilters-RouteFilter-RouteMask": filterProfile_InputFilters_RouteFilter_RouteMask,
       "filterProfile-InputFilters-RouteFilter-RouteAddress": filterProfile_InputFilters_RouteFilter_RouteAddress,
       "filterProfile-InputFilters-RouteFilter-AddMetric": filterProfile_InputFilters_RouteFilter_AddMetric,
       "filterProfile-InputFilters-RouteFilter-Action": filterProfile_InputFilters_RouteFilter_Action,
       "filterProfile-InputFilters-IpxFilter-SrcNetAddress": filterProfile_InputFilters_IpxFilter_SrcNetAddress,
       "filterProfile-InputFilters-IpxFilter-DestNetAddress": filterProfile_InputFilters_IpxFilter_DestNetAddress,
       "filterProfile-InputFilters-IpxFilter-SrcNodeAddress": filterProfile_InputFilters_IpxFilter_SrcNodeAddress,
       "filterProfile-InputFilters-IpxFilter-DestNodeAddress": filterProfile_InputFilters_IpxFilter_DestNodeAddress,
       "filterProfile-InputFilters-IpxFilter-SrcSocket": filterProfile_InputFilters_IpxFilter_SrcSocket,
       "filterProfile-InputFilters-IpxFilter-SrcSocketCmp": filterProfile_InputFilters_IpxFilter_SrcSocketCmp,
       "filterProfile-InputFilters-IpxFilter-DestSocket": filterProfile_InputFilters_IpxFilter_DestSocket,
       "filterProfile-InputFilters-IpxFilter-DstSocketCmp": filterProfile_InputFilters_IpxFilter_DstSocketCmp,
       "filterProfile-InputFilters-TosFilter-Protocol": filterProfile_InputFilters_TosFilter_Protocol,
       "filterProfile-InputFilters-TosFilter-SourceAddressMask": filterProfile_InputFilters_TosFilter_SourceAddressMask,
       "filterProfile-InputFilters-TosFilter-SourceAddress": filterProfile_InputFilters_TosFilter_SourceAddress,
       "filterProfile-InputFilters-TosFilter-DestAddressMask": filterProfile_InputFilters_TosFilter_DestAddressMask,
       "filterProfile-InputFilters-TosFilter-DestAddress": filterProfile_InputFilters_TosFilter_DestAddress,
       "filterProfile-InputFilters-TosFilter-oSrcPortCmp": filterProfile_InputFilters_TosFilter_oSrcPortCmp,
       "filterProfile-InputFilters-TosFilter-SourcePort": filterProfile_InputFilters_TosFilter_SourcePort,
       "filterProfile-InputFilters-TosFilter-oDstPortCmp": filterProfile_InputFilters_TosFilter_oDstPortCmp,
       "filterProfile-InputFilters-TosFilter-DestPort": filterProfile_InputFilters_TosFilter_DestPort,
       "filterProfile-InputFilters-TosFilter-Precedence": filterProfile_InputFilters_TosFilter_Precedence,
       "filterProfile-InputFilters-TosFilter-TypeOfService": filterProfile_InputFilters_TosFilter_TypeOfService,
       "filterProfile-InputFilters-TosFilter-MarkingType": filterProfile_InputFilters_TosFilter_MarkingType,
       "filterProfile-InputFilters-TosFilter-Dscp": filterProfile_InputFilters_TosFilter_Dscp}
)
