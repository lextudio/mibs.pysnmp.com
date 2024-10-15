# SNMP MIB module (IBM6611-DLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM6611-DLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:46 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class FilterType(Integer32):
    """Custom type FilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_Ibm6611_ObjectIdentity = ObjectIdentity
ibm6611 = _Ibm6611_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2)
)
_Ibmdls_ObjectIdentity = ObjectIdentity
ibmdls = _Ibmdls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9)
)


class _IbmdlsVirtualRingSegmentNumber_Type(Integer32):
    """Custom type ibmdlsVirtualRingSegmentNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IbmdlsVirtualRingSegmentNumber_Type.__name__ = "Integer32"
_IbmdlsVirtualRingSegmentNumber_Object = MibScalar
ibmdlsVirtualRingSegmentNumber = _IbmdlsVirtualRingSegmentNumber_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 1),
    _IbmdlsVirtualRingSegmentNumber_Type()
)
ibmdlsVirtualRingSegmentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsVirtualRingSegmentNumber.setStatus("mandatory")
_IbmdlsFrameFilterType_Type = FilterType
_IbmdlsFrameFilterType_Object = MibScalar
ibmdlsFrameFilterType = _IbmdlsFrameFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 2),
    _IbmdlsFrameFilterType_Type()
)
ibmdlsFrameFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsFrameFilterType.setStatus("mandatory")
_IbmdlsNameFilterType_Type = FilterType
_IbmdlsNameFilterType_Object = MibScalar
ibmdlsNameFilterType = _IbmdlsNameFilterType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 3),
    _IbmdlsNameFilterType_Type()
)
ibmdlsNameFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsNameFilterType.setStatus("mandatory")
_IbmdlsRouterTable_Object = MibTable
ibmdlsRouterTable = _IbmdlsRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4)
)
if mibBuilder.loadTexts:
    ibmdlsRouterTable.setStatus("mandatory")
_IbmdlsRouterEntry_Object = MibTableRow
ibmdlsRouterEntry = _IbmdlsRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1)
)
ibmdlsRouterEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsRouterAddress"),
)
if mibBuilder.loadTexts:
    ibmdlsRouterEntry.setStatus("mandatory")
_IbmdlsRouterAddress_Type = IpAddress
_IbmdlsRouterAddress_Object = MibTableColumn
ibmdlsRouterAddress = _IbmdlsRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 1),
    _IbmdlsRouterAddress_Type()
)
ibmdlsRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterAddress.setStatus("mandatory")


class _IbmdlsRouterStatus_Type(Integer32):
    """Custom type ibmdlsRouterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("notActive", 1))
    )


_IbmdlsRouterStatus_Type.__name__ = "Integer32"
_IbmdlsRouterStatus_Object = MibTableColumn
ibmdlsRouterStatus = _IbmdlsRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 2),
    _IbmdlsRouterStatus_Type()
)
ibmdlsRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterStatus.setStatus("mandatory")


class _IbmdlsRouterDefinedBy_Type(Integer32):
    """Custom type ibmdlsRouterDefinedBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("system", 2),
          ("user", 1))
    )


_IbmdlsRouterDefinedBy_Type.__name__ = "Integer32"
_IbmdlsRouterDefinedBy_Object = MibTableColumn
ibmdlsRouterDefinedBy = _IbmdlsRouterDefinedBy_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 4, 1, 3),
    _IbmdlsRouterDefinedBy_Type()
)
ibmdlsRouterDefinedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRouterDefinedBy.setStatus("mandatory")
_IbmdlsLocalFrameFilterTable_Object = MibTable
ibmdlsLocalFrameFilterTable = _IbmdlsLocalFrameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5)
)
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterTable.setStatus("mandatory")
_IbmdlsLocalFrameFilterEntry_Object = MibTableRow
ibmdlsLocalFrameFilterEntry = _IbmdlsLocalFrameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1)
)
ibmdlsLocalFrameFilterEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsLocalFrameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterEntry.setStatus("mandatory")


class _IbmdlsLocalFrameFilterID_Type(Integer32):
    """Custom type ibmdlsLocalFrameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsLocalFrameFilterID_Type.__name__ = "Integer32"
_IbmdlsLocalFrameFilterID_Object = MibTableColumn
ibmdlsLocalFrameFilterID = _IbmdlsLocalFrameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 1),
    _IbmdlsLocalFrameFilterID_Type()
)
ibmdlsLocalFrameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterID.setStatus("mandatory")
_IbmdlsLocalFrameFilterSrcAddress_Type = MacAddress
_IbmdlsLocalFrameFilterSrcAddress_Object = MibTableColumn
ibmdlsLocalFrameFilterSrcAddress = _IbmdlsLocalFrameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 2),
    _IbmdlsLocalFrameFilterSrcAddress_Type()
)
ibmdlsLocalFrameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterSrcAddress.setStatus("mandatory")
_IbmdlsLocalFrameFilterSrcMask_Type = MacAddress
_IbmdlsLocalFrameFilterSrcMask_Object = MibTableColumn
ibmdlsLocalFrameFilterSrcMask = _IbmdlsLocalFrameFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 3),
    _IbmdlsLocalFrameFilterSrcMask_Type()
)
ibmdlsLocalFrameFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterSrcMask.setStatus("mandatory")
_IbmdlsLocalFrameFilterDestAddress_Type = MacAddress
_IbmdlsLocalFrameFilterDestAddress_Object = MibTableColumn
ibmdlsLocalFrameFilterDestAddress = _IbmdlsLocalFrameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 4),
    _IbmdlsLocalFrameFilterDestAddress_Type()
)
ibmdlsLocalFrameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterDestAddress.setStatus("mandatory")
_IbmdlsLocalFrameFilterDestMask_Type = MacAddress
_IbmdlsLocalFrameFilterDestMask_Object = MibTableColumn
ibmdlsLocalFrameFilterDestMask = _IbmdlsLocalFrameFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 5, 1, 5),
    _IbmdlsLocalFrameFilterDestMask_Type()
)
ibmdlsLocalFrameFilterDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalFrameFilterDestMask.setStatus("mandatory")
_IbmdlsRemoteFrameFilterTable_Object = MibTable
ibmdlsRemoteFrameFilterTable = _IbmdlsRemoteFrameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6)
)
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterTable.setStatus("mandatory")
_IbmdlsRemoteFrameFilterEntry_Object = MibTableRow
ibmdlsRemoteFrameFilterEntry = _IbmdlsRemoteFrameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1)
)
ibmdlsRemoteFrameFilterEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsRemoteFrameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterEntry.setStatus("mandatory")


class _IbmdlsRemoteFrameFilterID_Type(Integer32):
    """Custom type ibmdlsRemoteFrameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsRemoteFrameFilterID_Type.__name__ = "Integer32"
_IbmdlsRemoteFrameFilterID_Object = MibTableColumn
ibmdlsRemoteFrameFilterID = _IbmdlsRemoteFrameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 1),
    _IbmdlsRemoteFrameFilterID_Type()
)
ibmdlsRemoteFrameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterID.setStatus("mandatory")
_IbmdlsRemoteFrameFilterSrcAddress_Type = MacAddress
_IbmdlsRemoteFrameFilterSrcAddress_Object = MibTableColumn
ibmdlsRemoteFrameFilterSrcAddress = _IbmdlsRemoteFrameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 2),
    _IbmdlsRemoteFrameFilterSrcAddress_Type()
)
ibmdlsRemoteFrameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterSrcAddress.setStatus("mandatory")
_IbmdlsRemoteFrameFilterSrcMask_Type = MacAddress
_IbmdlsRemoteFrameFilterSrcMask_Object = MibTableColumn
ibmdlsRemoteFrameFilterSrcMask = _IbmdlsRemoteFrameFilterSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 3),
    _IbmdlsRemoteFrameFilterSrcMask_Type()
)
ibmdlsRemoteFrameFilterSrcMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterSrcMask.setStatus("mandatory")
_IbmdlsRemoteFrameFilterDestAddress_Type = MacAddress
_IbmdlsRemoteFrameFilterDestAddress_Object = MibTableColumn
ibmdlsRemoteFrameFilterDestAddress = _IbmdlsRemoteFrameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 4),
    _IbmdlsRemoteFrameFilterDestAddress_Type()
)
ibmdlsRemoteFrameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterDestAddress.setStatus("mandatory")
_IbmdlsRemoteFrameFilterDestMask_Type = MacAddress
_IbmdlsRemoteFrameFilterDestMask_Object = MibTableColumn
ibmdlsRemoteFrameFilterDestMask = _IbmdlsRemoteFrameFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 6, 1, 5),
    _IbmdlsRemoteFrameFilterDestMask_Type()
)
ibmdlsRemoteFrameFilterDestMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteFrameFilterDestMask.setStatus("mandatory")
_IbmdlsLocalNameFilterTable_Object = MibTable
ibmdlsLocalNameFilterTable = _IbmdlsLocalNameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7)
)
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterTable.setStatus("mandatory")
_IbmdlsLocalNameFilterEntry_Object = MibTableRow
ibmdlsLocalNameFilterEntry = _IbmdlsLocalNameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1)
)
ibmdlsLocalNameFilterEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsLocalNameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterEntry.setStatus("mandatory")


class _IbmdlsLocalNameFilterID_Type(Integer32):
    """Custom type ibmdlsLocalNameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsLocalNameFilterID_Type.__name__ = "Integer32"
_IbmdlsLocalNameFilterID_Object = MibTableColumn
ibmdlsLocalNameFilterID = _IbmdlsLocalNameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 1),
    _IbmdlsLocalNameFilterID_Type()
)
ibmdlsLocalNameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterID.setStatus("mandatory")


class _IbmdlsLocalNameFilterSrcAddress_Type(DisplayString):
    """Custom type ibmdlsLocalNameFilterSrcAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsLocalNameFilterSrcAddress_Type.__name__ = "DisplayString"
_IbmdlsLocalNameFilterSrcAddress_Object = MibTableColumn
ibmdlsLocalNameFilterSrcAddress = _IbmdlsLocalNameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 2),
    _IbmdlsLocalNameFilterSrcAddress_Type()
)
ibmdlsLocalNameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterSrcAddress.setStatus("mandatory")


class _IbmdlsLocalNameFilterDestAddress_Type(DisplayString):
    """Custom type ibmdlsLocalNameFilterDestAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsLocalNameFilterDestAddress_Type.__name__ = "DisplayString"
_IbmdlsLocalNameFilterDestAddress_Object = MibTableColumn
ibmdlsLocalNameFilterDestAddress = _IbmdlsLocalNameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 7, 1, 3),
    _IbmdlsLocalNameFilterDestAddress_Type()
)
ibmdlsLocalNameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsLocalNameFilterDestAddress.setStatus("mandatory")
_IbmdlsRemoteNameFilterTable_Object = MibTable
ibmdlsRemoteNameFilterTable = _IbmdlsRemoteNameFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8)
)
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterTable.setStatus("mandatory")
_IbmdlsRemoteNameFilterEntry_Object = MibTableRow
ibmdlsRemoteNameFilterEntry = _IbmdlsRemoteNameFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1)
)
ibmdlsRemoteNameFilterEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsRemoteNameFilterID"),
)
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterEntry.setStatus("mandatory")


class _IbmdlsRemoteNameFilterID_Type(Integer32):
    """Custom type ibmdlsRemoteNameFilterID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsRemoteNameFilterID_Type.__name__ = "Integer32"
_IbmdlsRemoteNameFilterID_Object = MibTableColumn
ibmdlsRemoteNameFilterID = _IbmdlsRemoteNameFilterID_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 1),
    _IbmdlsRemoteNameFilterID_Type()
)
ibmdlsRemoteNameFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterID.setStatus("mandatory")


class _IbmdlsRemoteNameFilterSrcAddress_Type(DisplayString):
    """Custom type ibmdlsRemoteNameFilterSrcAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsRemoteNameFilterSrcAddress_Type.__name__ = "DisplayString"
_IbmdlsRemoteNameFilterSrcAddress_Object = MibTableColumn
ibmdlsRemoteNameFilterSrcAddress = _IbmdlsRemoteNameFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 2),
    _IbmdlsRemoteNameFilterSrcAddress_Type()
)
ibmdlsRemoteNameFilterSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterSrcAddress.setStatus("mandatory")


class _IbmdlsRemoteNameFilterDestAddress_Type(DisplayString):
    """Custom type ibmdlsRemoteNameFilterDestAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsRemoteNameFilterDestAddress_Type.__name__ = "DisplayString"
_IbmdlsRemoteNameFilterDestAddress_Object = MibTableColumn
ibmdlsRemoteNameFilterDestAddress = _IbmdlsRemoteNameFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 8, 1, 3),
    _IbmdlsRemoteNameFilterDestAddress_Type()
)
ibmdlsRemoteNameFilterDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsRemoteNameFilterDestAddress.setStatus("mandatory")
_IbmdlsDefaultDestTable_Object = MibTable
ibmdlsDefaultDestTable = _IbmdlsDefaultDestTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9)
)
if mibBuilder.loadTexts:
    ibmdlsDefaultDestTable.setStatus("mandatory")
_IbmdlsDefaultDestEntry_Object = MibTableRow
ibmdlsDefaultDestEntry = _IbmdlsDefaultDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1)
)
ibmdlsDefaultDestEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsDefaultDestAddress"),
)
if mibBuilder.loadTexts:
    ibmdlsDefaultDestEntry.setStatus("mandatory")
_IbmdlsDefaultDestAddress_Type = MacAddress
_IbmdlsDefaultDestAddress_Object = MibTableColumn
ibmdlsDefaultDestAddress = _IbmdlsDefaultDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1, 1),
    _IbmdlsDefaultDestAddress_Type()
)
ibmdlsDefaultDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultDestAddress.setStatus("mandatory")
_IbmdlsDefaultRouterAddress_Type = IpAddress
_IbmdlsDefaultRouterAddress_Object = MibTableColumn
ibmdlsDefaultRouterAddress = _IbmdlsDefaultRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 9, 1, 2),
    _IbmdlsDefaultRouterAddress_Type()
)
ibmdlsDefaultRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultRouterAddress.setStatus("mandatory")
_IbmdlsDefaultNBDestTable_Object = MibTable
ibmdlsDefaultNBDestTable = _IbmdlsDefaultNBDestTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10)
)
if mibBuilder.loadTexts:
    ibmdlsDefaultNBDestTable.setStatus("mandatory")
_IbmdlsDefaultNBDestEntry_Object = MibTableRow
ibmdlsDefaultNBDestEntry = _IbmdlsDefaultNBDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1)
)
ibmdlsDefaultNBDestEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsDefaultNBDestName"),
)
if mibBuilder.loadTexts:
    ibmdlsDefaultNBDestEntry.setStatus("mandatory")


class _IbmdlsDefaultNBDestName_Type(DisplayString):
    """Custom type ibmdlsDefaultNBDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_IbmdlsDefaultNBDestName_Type.__name__ = "DisplayString"
_IbmdlsDefaultNBDestName_Object = MibTableColumn
ibmdlsDefaultNBDestName = _IbmdlsDefaultNBDestName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1, 1),
    _IbmdlsDefaultNBDestName_Type()
)
ibmdlsDefaultNBDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultNBDestName.setStatus("mandatory")
_IbmdlsDefaultNBRouterAddress_Type = IpAddress
_IbmdlsDefaultNBRouterAddress_Object = MibTableColumn
ibmdlsDefaultNBRouterAddress = _IbmdlsDefaultNBRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 10, 1, 2),
    _IbmdlsDefaultNBRouterAddress_Type()
)
ibmdlsDefaultNBRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsDefaultNBRouterAddress.setStatus("mandatory")
_IbmdlsStationTable_Object = MibTable
ibmdlsStationTable = _IbmdlsStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11)
)
if mibBuilder.loadTexts:
    ibmdlsStationTable.setStatus("mandatory")
_IbmdlsStationEntry_Object = MibTableRow
ibmdlsStationEntry = _IbmdlsStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1)
)
ibmdlsStationEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsStationIfIndex"),
    (0, "IBM6611-DLS-MIB", "ibmdlsStationAddress"),
)
if mibBuilder.loadTexts:
    ibmdlsStationEntry.setStatus("mandatory")
_IbmdlsStationIfIndex_Type = Integer32
_IbmdlsStationIfIndex_Object = MibTableColumn
ibmdlsStationIfIndex = _IbmdlsStationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 1),
    _IbmdlsStationIfIndex_Type()
)
ibmdlsStationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationIfIndex.setStatus("mandatory")


class _IbmdlsStationAddress_Type(Integer32):
    """Custom type ibmdlsStationAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IbmdlsStationAddress_Type.__name__ = "Integer32"
_IbmdlsStationAddress_Object = MibTableColumn
ibmdlsStationAddress = _IbmdlsStationAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 2),
    _IbmdlsStationAddress_Type()
)
ibmdlsStationAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationAddress.setStatus("mandatory")


class _IbmdlsStationTransmitWindowCount_Type(Integer32):
    """Custom type ibmdlsStationTransmitWindowCount based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_IbmdlsStationTransmitWindowCount_Type.__name__ = "Integer32"
_IbmdlsStationTransmitWindowCount_Object = MibTableColumn
ibmdlsStationTransmitWindowCount = _IbmdlsStationTransmitWindowCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 3),
    _IbmdlsStationTransmitWindowCount_Type()
)
ibmdlsStationTransmitWindowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationTransmitWindowCount.setStatus("mandatory")


class _IbmdlsStationRetransmitCount_Type(Integer32):
    """Custom type ibmdlsStationRetransmitCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_IbmdlsStationRetransmitCount_Type.__name__ = "Integer32"
_IbmdlsStationRetransmitCount_Object = MibTableColumn
ibmdlsStationRetransmitCount = _IbmdlsStationRetransmitCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 4),
    _IbmdlsStationRetransmitCount_Type()
)
ibmdlsStationRetransmitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationRetransmitCount.setStatus("mandatory")


class _IbmdlsStationRetransmitThreshold_Type(Integer32):
    """Custom type ibmdlsStationRetransmitThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsStationRetransmitThreshold_Type.__name__ = "Integer32"
_IbmdlsStationRetransmitThreshold_Object = MibTableColumn
ibmdlsStationRetransmitThreshold = _IbmdlsStationRetransmitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 5),
    _IbmdlsStationRetransmitThreshold_Type()
)
ibmdlsStationRetransmitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationRetransmitThreshold.setStatus("mandatory")


class _IbmdlsStationForceDisconnectTimeout_Type(Integer32):
    """Custom type ibmdlsStationForceDisconnectTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_IbmdlsStationForceDisconnectTimeout_Type.__name__ = "Integer32"
_IbmdlsStationForceDisconnectTimeout_Object = MibTableColumn
ibmdlsStationForceDisconnectTimeout = _IbmdlsStationForceDisconnectTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 6),
    _IbmdlsStationForceDisconnectTimeout_Type()
)
ibmdlsStationForceDisconnectTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationForceDisconnectTimeout.setStatus("mandatory")


class _IbmdlsStationMaxIfieldSize_Type(Integer32):
    """Custom type ibmdlsStationMaxIfieldSize based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(265, 30729),
    )


_IbmdlsStationMaxIfieldSize_Type.__name__ = "Integer32"
_IbmdlsStationMaxIfieldSize_Object = MibTableColumn
ibmdlsStationMaxIfieldSize = _IbmdlsStationMaxIfieldSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 7),
    _IbmdlsStationMaxIfieldSize_Type()
)
ibmdlsStationMaxIfieldSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationMaxIfieldSize.setStatus("mandatory")


class _IbmdlsStationPrimaryRepollTimeout_Type(Integer32):
    """Custom type ibmdlsStationPrimaryRepollTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_IbmdlsStationPrimaryRepollTimeout_Type.__name__ = "Integer32"
_IbmdlsStationPrimaryRepollTimeout_Object = MibTableColumn
ibmdlsStationPrimaryRepollTimeout = _IbmdlsStationPrimaryRepollTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 8),
    _IbmdlsStationPrimaryRepollTimeout_Type()
)
ibmdlsStationPrimaryRepollTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimaryRepollTimeout.setStatus("mandatory")


class _IbmdlsStationPrimaryRepollCount_Type(Integer32):
    """Custom type ibmdlsStationPrimaryRepollCount based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_IbmdlsStationPrimaryRepollCount_Type.__name__ = "Integer32"
_IbmdlsStationPrimaryRepollCount_Object = MibTableColumn
ibmdlsStationPrimaryRepollCount = _IbmdlsStationPrimaryRepollCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 9),
    _IbmdlsStationPrimaryRepollCount_Type()
)
ibmdlsStationPrimaryRepollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimaryRepollCount.setStatus("mandatory")


class _IbmdlsStationPrimaryRepollThreshold_Type(Integer32):
    """Custom type ibmdlsStationPrimaryRepollThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_IbmdlsStationPrimaryRepollThreshold_Type.__name__ = "Integer32"
_IbmdlsStationPrimaryRepollThreshold_Object = MibTableColumn
ibmdlsStationPrimaryRepollThreshold = _IbmdlsStationPrimaryRepollThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 10),
    _IbmdlsStationPrimaryRepollThreshold_Type()
)
ibmdlsStationPrimaryRepollThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimaryRepollThreshold.setStatus("mandatory")


class _IbmdlsStationPrimarySlowListTimeout_Type(Integer32):
    """Custom type ibmdlsStationPrimarySlowListTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_IbmdlsStationPrimarySlowListTimeout_Type.__name__ = "Integer32"
_IbmdlsStationPrimarySlowListTimeout_Object = MibTableColumn
ibmdlsStationPrimarySlowListTimeout = _IbmdlsStationPrimarySlowListTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 11),
    _IbmdlsStationPrimarySlowListTimeout_Type()
)
ibmdlsStationPrimarySlowListTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationPrimarySlowListTimeout.setStatus("mandatory")
_IbmdlsStationSrcAddress_Type = MacAddress
_IbmdlsStationSrcAddress_Object = MibTableColumn
ibmdlsStationSrcAddress = _IbmdlsStationSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 12),
    _IbmdlsStationSrcAddress_Type()
)
ibmdlsStationSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationSrcAddress.setStatus("mandatory")
_IbmdlsStationDestAddress_Type = MacAddress
_IbmdlsStationDestAddress_Object = MibTableColumn
ibmdlsStationDestAddress = _IbmdlsStationDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 11, 1, 13),
    _IbmdlsStationDestAddress_Type()
)
ibmdlsStationDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsStationDestAddress.setStatus("mandatory")
_IbmdlsCirTable_Object = MibTable
ibmdlsCirTable = _IbmdlsCirTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12)
)
if mibBuilder.loadTexts:
    ibmdlsCirTable.setStatus("mandatory")
_IbmdlsCirEntry_Object = MibTableRow
ibmdlsCirEntry = _IbmdlsCirEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1)
)
ibmdlsCirEntry.setIndexNames(
    (0, "IBM6611-DLS-MIB", "ibmdlsCirIfIndex"),
    (0, "IBM6611-DLS-MIB", "ibmdlsCirSrcAddress"),
    (0, "IBM6611-DLS-MIB", "ibmdlsCirSrcSap"),
    (0, "IBM6611-DLS-MIB", "ibmdlsCirDestAddress"),
    (0, "IBM6611-DLS-MIB", "ibmdlsCirDestSap"),
)
if mibBuilder.loadTexts:
    ibmdlsCirEntry.setStatus("mandatory")
_IbmdlsCirIfIndex_Type = Integer32
_IbmdlsCirIfIndex_Object = MibTableColumn
ibmdlsCirIfIndex = _IbmdlsCirIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 1),
    _IbmdlsCirIfIndex_Type()
)
ibmdlsCirIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirIfIndex.setStatus("mandatory")
_IbmdlsCirSrcAddress_Type = MacAddress
_IbmdlsCirSrcAddress_Object = MibTableColumn
ibmdlsCirSrcAddress = _IbmdlsCirSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 2),
    _IbmdlsCirSrcAddress_Type()
)
ibmdlsCirSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirSrcAddress.setStatus("mandatory")
_IbmdlsCirSrcSap_Type = Integer32
_IbmdlsCirSrcSap_Object = MibTableColumn
ibmdlsCirSrcSap = _IbmdlsCirSrcSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 3),
    _IbmdlsCirSrcSap_Type()
)
ibmdlsCirSrcSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirSrcSap.setStatus("mandatory")
_IbmdlsCirDestAddress_Type = MacAddress
_IbmdlsCirDestAddress_Object = MibTableColumn
ibmdlsCirDestAddress = _IbmdlsCirDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 4),
    _IbmdlsCirDestAddress_Type()
)
ibmdlsCirDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirDestAddress.setStatus("mandatory")
_IbmdlsCirDestSap_Type = Integer32
_IbmdlsCirDestSap_Object = MibTableColumn
ibmdlsCirDestSap = _IbmdlsCirDestSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 5),
    _IbmdlsCirDestSap_Type()
)
ibmdlsCirDestSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirDestSap.setStatus("mandatory")
_IbmdlsCirPartnerRouterAddress_Type = IpAddress
_IbmdlsCirPartnerRouterAddress_Object = MibTableColumn
ibmdlsCirPartnerRouterAddress = _IbmdlsCirPartnerRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 6),
    _IbmdlsCirPartnerRouterAddress_Type()
)
ibmdlsCirPartnerRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirPartnerRouterAddress.setStatus("mandatory")


class _IbmdlsCirLocalLinkState_Type(Integer32):
    """Custom type ibmdlsCirLocalLinkState based on Integer32"""
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
        *(("closing", 3),
          ("inactive", 4),
          ("opened", 2),
          ("opening", 1))
    )


_IbmdlsCirLocalLinkState_Type.__name__ = "Integer32"
_IbmdlsCirLocalLinkState_Object = MibTableColumn
ibmdlsCirLocalLinkState = _IbmdlsCirLocalLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 7),
    _IbmdlsCirLocalLinkState_Type()
)
ibmdlsCirLocalLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkState.setStatus("mandatory")


class _IbmdlsCirLocalLinkSubState_Type(Integer32):
    """Custom type ibmdlsCirLocalLinkSubState based on Integer32"""
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
        *(("calling", 1),
          ("contacted", 3),
          ("listening", 2),
          ("localBusy", 4),
          ("remoteBusy", 5))
    )


_IbmdlsCirLocalLinkSubState_Type.__name__ = "Integer32"
_IbmdlsCirLocalLinkSubState_Object = MibTableColumn
ibmdlsCirLocalLinkSubState = _IbmdlsCirLocalLinkSubState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 8),
    _IbmdlsCirLocalLinkSubState_Type()
)
ibmdlsCirLocalLinkSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkSubState.setStatus("mandatory")


class _IbmdlsCirLocalLinkRouting_Type(OctetString):
    """Custom type ibmdlsCirLocalLinkRouting based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 18),
    )


_IbmdlsCirLocalLinkRouting_Type.__name__ = "OctetString"
_IbmdlsCirLocalLinkRouting_Object = MibTableColumn
ibmdlsCirLocalLinkRouting = _IbmdlsCirLocalLinkRouting_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 9),
    _IbmdlsCirLocalLinkRouting_Type()
)
ibmdlsCirLocalLinkRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkRouting.setStatus("mandatory")
_IbmdlsCirLocalLinkTestCmdsSent_Type = Counter32
_IbmdlsCirLocalLinkTestCmdsSent_Object = MibTableColumn
ibmdlsCirLocalLinkTestCmdsSent = _IbmdlsCirLocalLinkTestCmdsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 10),
    _IbmdlsCirLocalLinkTestCmdsSent_Type()
)
ibmdlsCirLocalLinkTestCmdsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkTestCmdsSent.setStatus("mandatory")
_IbmdlsCirLocalLinkTestCmdsFail_Type = Counter32
_IbmdlsCirLocalLinkTestCmdsFail_Object = MibTableColumn
ibmdlsCirLocalLinkTestCmdsFail = _IbmdlsCirLocalLinkTestCmdsFail_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 11),
    _IbmdlsCirLocalLinkTestCmdsFail_Type()
)
ibmdlsCirLocalLinkTestCmdsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkTestCmdsFail.setStatus("mandatory")
_IbmdlsCirLocalLinkTestCmdsRcv_Type = Counter32
_IbmdlsCirLocalLinkTestCmdsRcv_Object = MibTableColumn
ibmdlsCirLocalLinkTestCmdsRcv = _IbmdlsCirLocalLinkTestCmdsRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 12),
    _IbmdlsCirLocalLinkTestCmdsRcv_Type()
)
ibmdlsCirLocalLinkTestCmdsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkTestCmdsRcv.setStatus("mandatory")
_IbmdlsCirLocalLinkDataPktSent_Type = Counter32
_IbmdlsCirLocalLinkDataPktSent_Object = MibTableColumn
ibmdlsCirLocalLinkDataPktSent = _IbmdlsCirLocalLinkDataPktSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 13),
    _IbmdlsCirLocalLinkDataPktSent_Type()
)
ibmdlsCirLocalLinkDataPktSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkDataPktSent.setStatus("mandatory")
_IbmdlsCirLocalLinkDataPktResent_Type = Counter32
_IbmdlsCirLocalLinkDataPktResent_Object = MibTableColumn
ibmdlsCirLocalLinkDataPktResent = _IbmdlsCirLocalLinkDataPktResent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 14),
    _IbmdlsCirLocalLinkDataPktResent_Type()
)
ibmdlsCirLocalLinkDataPktResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkDataPktResent.setStatus("mandatory")
_IbmdlsCirLocalLinkMaxContResent_Type = Counter32
_IbmdlsCirLocalLinkMaxContResent_Object = MibTableColumn
ibmdlsCirLocalLinkMaxContResent = _IbmdlsCirLocalLinkMaxContResent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 15),
    _IbmdlsCirLocalLinkMaxContResent_Type()
)
ibmdlsCirLocalLinkMaxContResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkMaxContResent.setStatus("mandatory")
_IbmdlsCirLocalLinkDataPktRcv_Type = Counter32
_IbmdlsCirLocalLinkDataPktRcv_Object = MibTableColumn
ibmdlsCirLocalLinkDataPktRcv = _IbmdlsCirLocalLinkDataPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 16),
    _IbmdlsCirLocalLinkDataPktRcv_Type()
)
ibmdlsCirLocalLinkDataPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkDataPktRcv.setStatus("mandatory")
_IbmdlsCirLocalLinkInvalidPktRcv_Type = Counter32
_IbmdlsCirLocalLinkInvalidPktRcv_Object = MibTableColumn
ibmdlsCirLocalLinkInvalidPktRcv = _IbmdlsCirLocalLinkInvalidPktRcv_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 17),
    _IbmdlsCirLocalLinkInvalidPktRcv_Type()
)
ibmdlsCirLocalLinkInvalidPktRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkInvalidPktRcv.setStatus("mandatory")
_IbmdlsCirLocalLinkAdpRcvErr_Type = Counter32
_IbmdlsCirLocalLinkAdpRcvErr_Object = MibTableColumn
ibmdlsCirLocalLinkAdpRcvErr = _IbmdlsCirLocalLinkAdpRcvErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 18),
    _IbmdlsCirLocalLinkAdpRcvErr_Type()
)
ibmdlsCirLocalLinkAdpRcvErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkAdpRcvErr.setStatus("mandatory")
_IbmdlsCirLocalLinkAdpSendErr_Type = Counter32
_IbmdlsCirLocalLinkAdpSendErr_Object = MibTableColumn
ibmdlsCirLocalLinkAdpSendErr = _IbmdlsCirLocalLinkAdpSendErr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 19),
    _IbmdlsCirLocalLinkAdpSendErr_Type()
)
ibmdlsCirLocalLinkAdpSendErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkAdpSendErr.setStatus("mandatory")
_IbmdlsCirLocalLinkRcvInactiveTimeouts_Type = Counter32
_IbmdlsCirLocalLinkRcvInactiveTimeouts_Object = MibTableColumn
ibmdlsCirLocalLinkRcvInactiveTimeouts = _IbmdlsCirLocalLinkRcvInactiveTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 20),
    _IbmdlsCirLocalLinkRcvInactiveTimeouts_Type()
)
ibmdlsCirLocalLinkRcvInactiveTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkRcvInactiveTimeouts.setStatus("mandatory")
_IbmdlsCirLocalLinkCmdPollsSent_Type = Counter32
_IbmdlsCirLocalLinkCmdPollsSent_Object = MibTableColumn
ibmdlsCirLocalLinkCmdPollsSent = _IbmdlsCirLocalLinkCmdPollsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 21),
    _IbmdlsCirLocalLinkCmdPollsSent_Type()
)
ibmdlsCirLocalLinkCmdPollsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkCmdPollsSent.setStatus("mandatory")
_IbmdlsCirLocalLinkCmdRepollsSent_Type = Counter32
_IbmdlsCirLocalLinkCmdRepollsSent_Object = MibTableColumn
ibmdlsCirLocalLinkCmdRepollsSent = _IbmdlsCirLocalLinkCmdRepollsSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 22),
    _IbmdlsCirLocalLinkCmdRepollsSent_Type()
)
ibmdlsCirLocalLinkCmdRepollsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkCmdRepollsSent.setStatus("mandatory")
_IbmdlsCirLocalLinkCmdContRepolls_Type = Counter32
_IbmdlsCirLocalLinkCmdContRepolls_Object = MibTableColumn
ibmdlsCirLocalLinkCmdContRepolls = _IbmdlsCirLocalLinkCmdContRepolls_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 9, 12, 1, 23),
    _IbmdlsCirLocalLinkCmdContRepolls_Type()
)
ibmdlsCirLocalLinkCmdContRepolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmdlsCirLocalLinkCmdContRepolls.setStatus("mandatory")
_Ibmappn_ObjectIdentity = ObjectIdentity
ibmappn = _Ibmappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM6611-DLS-MIB",
    **{"MacAddress": MacAddress,
       "FilterType": FilterType,
       "ibm": ibm,
       "ibmProd": ibmProd,
       "ibm6611": ibm6611,
       "ibmdls": ibmdls,
       "ibmdlsVirtualRingSegmentNumber": ibmdlsVirtualRingSegmentNumber,
       "ibmdlsFrameFilterType": ibmdlsFrameFilterType,
       "ibmdlsNameFilterType": ibmdlsNameFilterType,
       "ibmdlsRouterTable": ibmdlsRouterTable,
       "ibmdlsRouterEntry": ibmdlsRouterEntry,
       "ibmdlsRouterAddress": ibmdlsRouterAddress,
       "ibmdlsRouterStatus": ibmdlsRouterStatus,
       "ibmdlsRouterDefinedBy": ibmdlsRouterDefinedBy,
       "ibmdlsLocalFrameFilterTable": ibmdlsLocalFrameFilterTable,
       "ibmdlsLocalFrameFilterEntry": ibmdlsLocalFrameFilterEntry,
       "ibmdlsLocalFrameFilterID": ibmdlsLocalFrameFilterID,
       "ibmdlsLocalFrameFilterSrcAddress": ibmdlsLocalFrameFilterSrcAddress,
       "ibmdlsLocalFrameFilterSrcMask": ibmdlsLocalFrameFilterSrcMask,
       "ibmdlsLocalFrameFilterDestAddress": ibmdlsLocalFrameFilterDestAddress,
       "ibmdlsLocalFrameFilterDestMask": ibmdlsLocalFrameFilterDestMask,
       "ibmdlsRemoteFrameFilterTable": ibmdlsRemoteFrameFilterTable,
       "ibmdlsRemoteFrameFilterEntry": ibmdlsRemoteFrameFilterEntry,
       "ibmdlsRemoteFrameFilterID": ibmdlsRemoteFrameFilterID,
       "ibmdlsRemoteFrameFilterSrcAddress": ibmdlsRemoteFrameFilterSrcAddress,
       "ibmdlsRemoteFrameFilterSrcMask": ibmdlsRemoteFrameFilterSrcMask,
       "ibmdlsRemoteFrameFilterDestAddress": ibmdlsRemoteFrameFilterDestAddress,
       "ibmdlsRemoteFrameFilterDestMask": ibmdlsRemoteFrameFilterDestMask,
       "ibmdlsLocalNameFilterTable": ibmdlsLocalNameFilterTable,
       "ibmdlsLocalNameFilterEntry": ibmdlsLocalNameFilterEntry,
       "ibmdlsLocalNameFilterID": ibmdlsLocalNameFilterID,
       "ibmdlsLocalNameFilterSrcAddress": ibmdlsLocalNameFilterSrcAddress,
       "ibmdlsLocalNameFilterDestAddress": ibmdlsLocalNameFilterDestAddress,
       "ibmdlsRemoteNameFilterTable": ibmdlsRemoteNameFilterTable,
       "ibmdlsRemoteNameFilterEntry": ibmdlsRemoteNameFilterEntry,
       "ibmdlsRemoteNameFilterID": ibmdlsRemoteNameFilterID,
       "ibmdlsRemoteNameFilterSrcAddress": ibmdlsRemoteNameFilterSrcAddress,
       "ibmdlsRemoteNameFilterDestAddress": ibmdlsRemoteNameFilterDestAddress,
       "ibmdlsDefaultDestTable": ibmdlsDefaultDestTable,
       "ibmdlsDefaultDestEntry": ibmdlsDefaultDestEntry,
       "ibmdlsDefaultDestAddress": ibmdlsDefaultDestAddress,
       "ibmdlsDefaultRouterAddress": ibmdlsDefaultRouterAddress,
       "ibmdlsDefaultNBDestTable": ibmdlsDefaultNBDestTable,
       "ibmdlsDefaultNBDestEntry": ibmdlsDefaultNBDestEntry,
       "ibmdlsDefaultNBDestName": ibmdlsDefaultNBDestName,
       "ibmdlsDefaultNBRouterAddress": ibmdlsDefaultNBRouterAddress,
       "ibmdlsStationTable": ibmdlsStationTable,
       "ibmdlsStationEntry": ibmdlsStationEntry,
       "ibmdlsStationIfIndex": ibmdlsStationIfIndex,
       "ibmdlsStationAddress": ibmdlsStationAddress,
       "ibmdlsStationTransmitWindowCount": ibmdlsStationTransmitWindowCount,
       "ibmdlsStationRetransmitCount": ibmdlsStationRetransmitCount,
       "ibmdlsStationRetransmitThreshold": ibmdlsStationRetransmitThreshold,
       "ibmdlsStationForceDisconnectTimeout": ibmdlsStationForceDisconnectTimeout,
       "ibmdlsStationMaxIfieldSize": ibmdlsStationMaxIfieldSize,
       "ibmdlsStationPrimaryRepollTimeout": ibmdlsStationPrimaryRepollTimeout,
       "ibmdlsStationPrimaryRepollCount": ibmdlsStationPrimaryRepollCount,
       "ibmdlsStationPrimaryRepollThreshold": ibmdlsStationPrimaryRepollThreshold,
       "ibmdlsStationPrimarySlowListTimeout": ibmdlsStationPrimarySlowListTimeout,
       "ibmdlsStationSrcAddress": ibmdlsStationSrcAddress,
       "ibmdlsStationDestAddress": ibmdlsStationDestAddress,
       "ibmdlsCirTable": ibmdlsCirTable,
       "ibmdlsCirEntry": ibmdlsCirEntry,
       "ibmdlsCirIfIndex": ibmdlsCirIfIndex,
       "ibmdlsCirSrcAddress": ibmdlsCirSrcAddress,
       "ibmdlsCirSrcSap": ibmdlsCirSrcSap,
       "ibmdlsCirDestAddress": ibmdlsCirDestAddress,
       "ibmdlsCirDestSap": ibmdlsCirDestSap,
       "ibmdlsCirPartnerRouterAddress": ibmdlsCirPartnerRouterAddress,
       "ibmdlsCirLocalLinkState": ibmdlsCirLocalLinkState,
       "ibmdlsCirLocalLinkSubState": ibmdlsCirLocalLinkSubState,
       "ibmdlsCirLocalLinkRouting": ibmdlsCirLocalLinkRouting,
       "ibmdlsCirLocalLinkTestCmdsSent": ibmdlsCirLocalLinkTestCmdsSent,
       "ibmdlsCirLocalLinkTestCmdsFail": ibmdlsCirLocalLinkTestCmdsFail,
       "ibmdlsCirLocalLinkTestCmdsRcv": ibmdlsCirLocalLinkTestCmdsRcv,
       "ibmdlsCirLocalLinkDataPktSent": ibmdlsCirLocalLinkDataPktSent,
       "ibmdlsCirLocalLinkDataPktResent": ibmdlsCirLocalLinkDataPktResent,
       "ibmdlsCirLocalLinkMaxContResent": ibmdlsCirLocalLinkMaxContResent,
       "ibmdlsCirLocalLinkDataPktRcv": ibmdlsCirLocalLinkDataPktRcv,
       "ibmdlsCirLocalLinkInvalidPktRcv": ibmdlsCirLocalLinkInvalidPktRcv,
       "ibmdlsCirLocalLinkAdpRcvErr": ibmdlsCirLocalLinkAdpRcvErr,
       "ibmdlsCirLocalLinkAdpSendErr": ibmdlsCirLocalLinkAdpSendErr,
       "ibmdlsCirLocalLinkRcvInactiveTimeouts": ibmdlsCirLocalLinkRcvInactiveTimeouts,
       "ibmdlsCirLocalLinkCmdPollsSent": ibmdlsCirLocalLinkCmdPollsSent,
       "ibmdlsCirLocalLinkCmdRepollsSent": ibmdlsCirLocalLinkCmdRepollsSent,
       "ibmdlsCirLocalLinkCmdContRepolls": ibmdlsCirLocalLinkCmdContRepolls,
       "ibmappn": ibmappn}
)
