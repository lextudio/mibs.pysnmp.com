# SNMP MIB module (IBM-6611-APPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-6611-APPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:22 2024
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
_Ibmappn_ObjectIdentity = ObjectIdentity
ibmappn = _Ibmappn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13)
)
_IbmappnNode_ObjectIdentity = ObjectIdentity
ibmappnNode = _IbmappnNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1)
)
_IbmappnGeneralInfoAndCaps_ObjectIdentity = ObjectIdentity
ibmappnGeneralInfoAndCaps = _IbmappnGeneralInfoAndCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1)
)


class _IbmappnNodeCpName_Type(DisplayString):
    """Custom type ibmappnNodeCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNodeCpName_Type.__name__ = "DisplayString"
_IbmappnNodeCpName_Object = MibScalar
ibmappnNodeCpName = _IbmappnNodeCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 1),
    _IbmappnNodeCpName_Type()
)
ibmappnNodeCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeCpName.setStatus("mandatory")


class _IbmappnNodeNetid_Type(DisplayString):
    """Custom type ibmappnNodeNetid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeNetid_Type.__name__ = "DisplayString"
_IbmappnNodeNetid_Object = MibScalar
ibmappnNodeNetid = _IbmappnNodeNetid_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 2),
    _IbmappnNodeNetid_Type()
)
ibmappnNodeNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNetid.setStatus("mandatory")


class _IbmappnNodeBlockNum_Type(DisplayString):
    """Custom type ibmappnNodeBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IbmappnNodeBlockNum_Type.__name__ = "DisplayString"
_IbmappnNodeBlockNum_Object = MibScalar
ibmappnNodeBlockNum = _IbmappnNodeBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 3),
    _IbmappnNodeBlockNum_Type()
)
ibmappnNodeBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeBlockNum.setStatus("mandatory")


class _IbmappnNodeIdNum_Type(DisplayString):
    """Custom type ibmappnNodeIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_IbmappnNodeIdNum_Type.__name__ = "DisplayString"
_IbmappnNodeIdNum_Object = MibScalar
ibmappnNodeIdNum = _IbmappnNodeIdNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 4),
    _IbmappnNodeIdNum_Type()
)
ibmappnNodeIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeIdNum.setStatus("mandatory")


class _IbmappnNodeType_Type(Integer32):
    """Custom type ibmappnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endNode", 2),
          ("len", 4),
          ("networkNode", 1))
    )


_IbmappnNodeType_Type.__name__ = "Integer32"
_IbmappnNodeType_Object = MibScalar
ibmappnNodeType = _IbmappnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 5),
    _IbmappnNodeType_Type()
)
ibmappnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeType.setStatus("mandatory")
_IbmappnNodeUpTime_Type = TimeTicks
_IbmappnNodeUpTime_Object = MibScalar
ibmappnNodeUpTime = _IbmappnNodeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 6),
    _IbmappnNodeUpTime_Type()
)
ibmappnNodeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeUpTime.setStatus("mandatory")


class _IbmappnNodeNegotLs_Type(Integer32):
    """Custom type ibmappnNodeNegotLs based on Integer32"""
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


_IbmappnNodeNegotLs_Type.__name__ = "Integer32"
_IbmappnNodeNegotLs_Object = MibScalar
ibmappnNodeNegotLs = _IbmappnNodeNegotLs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 7),
    _IbmappnNodeNegotLs_Type()
)
ibmappnNodeNegotLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNegotLs.setStatus("mandatory")


class _IbmappnNodeSegReasm_Type(Integer32):
    """Custom type ibmappnNodeSegReasm based on Integer32"""
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


_IbmappnNodeSegReasm_Type.__name__ = "Integer32"
_IbmappnNodeSegReasm_Object = MibScalar
ibmappnNodeSegReasm = _IbmappnNodeSegReasm_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 8),
    _IbmappnNodeSegReasm_Type()
)
ibmappnNodeSegReasm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeSegReasm.setStatus("mandatory")


class _IbmappnNodeBindReasm_Type(Integer32):
    """Custom type ibmappnNodeBindReasm based on Integer32"""
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


_IbmappnNodeBindReasm_Type.__name__ = "Integer32"
_IbmappnNodeBindReasm_Object = MibScalar
ibmappnNodeBindReasm = _IbmappnNodeBindReasm_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 9),
    _IbmappnNodeBindReasm_Type()
)
ibmappnNodeBindReasm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeBindReasm.setStatus("mandatory")


class _IbmappnNodeParallelTg_Type(Integer32):
    """Custom type ibmappnNodeParallelTg based on Integer32"""
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


_IbmappnNodeParallelTg_Type.__name__ = "Integer32"
_IbmappnNodeParallelTg_Object = MibScalar
ibmappnNodeParallelTg = _IbmappnNodeParallelTg_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 10),
    _IbmappnNodeParallelTg_Type()
)
ibmappnNodeParallelTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeParallelTg.setStatus("mandatory")


class _IbmappnNodeService_Type(Integer32):
    """Custom type ibmappnNodeService based on Integer32"""
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


_IbmappnNodeService_Type.__name__ = "Integer32"
_IbmappnNodeService_Object = MibScalar
ibmappnNodeService = _IbmappnNodeService_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 11),
    _IbmappnNodeService_Type()
)
ibmappnNodeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeService.setStatus("mandatory")


class _IbmappnNodeAdaptiveBindPacing_Type(Integer32):
    """Custom type ibmappnNodeAdaptiveBindPacing based on Integer32"""
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


_IbmappnNodeAdaptiveBindPacing_Type.__name__ = "Integer32"
_IbmappnNodeAdaptiveBindPacing_Object = MibScalar
ibmappnNodeAdaptiveBindPacing = _IbmappnNodeAdaptiveBindPacing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 1, 12),
    _IbmappnNodeAdaptiveBindPacing_Type()
)
ibmappnNodeAdaptiveBindPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeAdaptiveBindPacing.setStatus("mandatory")
_IbmappnNnUniqueInfoAndCaps_ObjectIdentity = ObjectIdentity
ibmappnNnUniqueInfoAndCaps = _IbmappnNnUniqueInfoAndCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2)
)


class _IbmappnNodeNnRcvRegChar_Type(Integer32):
    """Custom type ibmappnNodeNnRcvRegChar based on Integer32"""
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


_IbmappnNodeNnRcvRegChar_Type.__name__ = "Integer32"
_IbmappnNodeNnRcvRegChar_Object = MibScalar
ibmappnNodeNnRcvRegChar = _IbmappnNodeNnRcvRegChar_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 1),
    _IbmappnNodeNnRcvRegChar_Type()
)
ibmappnNodeNnRcvRegChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnRcvRegChar.setStatus("mandatory")


class _IbmappnNodeNnGateway_Type(Integer32):
    """Custom type ibmappnNodeNnGateway based on Integer32"""
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


_IbmappnNodeNnGateway_Type.__name__ = "Integer32"
_IbmappnNodeNnGateway_Object = MibScalar
ibmappnNodeNnGateway = _IbmappnNodeNnGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 2),
    _IbmappnNodeNnGateway_Type()
)
ibmappnNodeNnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnGateway.setStatus("mandatory")


class _IbmappnNodeNnCentralDirectory_Type(Integer32):
    """Custom type ibmappnNodeNnCentralDirectory based on Integer32"""
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


_IbmappnNodeNnCentralDirectory_Type.__name__ = "Integer32"
_IbmappnNodeNnCentralDirectory_Object = MibScalar
ibmappnNodeNnCentralDirectory = _IbmappnNodeNnCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 3),
    _IbmappnNodeNnCentralDirectory_Type()
)
ibmappnNodeNnCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnCentralDirectory.setStatus("mandatory")


class _IbmappnNodeNnTreeCache_Type(Integer32):
    """Custom type ibmappnNodeNnTreeCache based on Integer32"""
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


_IbmappnNodeNnTreeCache_Type.__name__ = "Integer32"
_IbmappnNodeNnTreeCache_Object = MibScalar
ibmappnNodeNnTreeCache = _IbmappnNodeNnTreeCache_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 4),
    _IbmappnNodeNnTreeCache_Type()
)
ibmappnNodeNnTreeCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnTreeCache.setStatus("mandatory")


class _IbmappnNodeNnTreeUpdate_Type(Integer32):
    """Custom type ibmappnNodeNnTreeUpdate based on Integer32"""
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


_IbmappnNodeNnTreeUpdate_Type.__name__ = "Integer32"
_IbmappnNodeNnTreeUpdate_Object = MibScalar
ibmappnNodeNnTreeUpdate = _IbmappnNodeNnTreeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 5),
    _IbmappnNodeNnTreeUpdate_Type()
)
ibmappnNodeNnTreeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnTreeUpdate.setStatus("mandatory")
_IbmappnNodeNnRouteAddResist_Type = Integer32
_IbmappnNodeNnRouteAddResist_Object = MibScalar
ibmappnNodeNnRouteAddResist = _IbmappnNodeNnRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 6),
    _IbmappnNodeNnRouteAddResist_Type()
)
ibmappnNodeNnRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnRouteAddResist.setStatus("mandatory")


class _IbmappnNodeNnIsr_Type(Integer32):
    """Custom type ibmappnNodeNnIsr based on Integer32"""
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


_IbmappnNodeNnIsr_Type.__name__ = "Integer32"
_IbmappnNodeNnIsr_Object = MibScalar
ibmappnNodeNnIsr = _IbmappnNodeNnIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 7),
    _IbmappnNodeNnIsr_Type()
)
ibmappnNodeNnIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnIsr.setStatus("mandatory")


class _IbmappnNodeNnFrsn_Type(Integer32):
    """Custom type ibmappnNodeNnFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNodeNnFrsn_Type.__name__ = "Integer32"
_IbmappnNodeNnFrsn_Object = MibScalar
ibmappnNodeNnFrsn = _IbmappnNodeNnFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 2, 8),
    _IbmappnNodeNnFrsn_Type()
)
ibmappnNodeNnFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeNnFrsn.setStatus("mandatory")
_IbmappnEnUniqueCaps_ObjectIdentity = ObjectIdentity
ibmappnEnUniqueCaps = _IbmappnEnUniqueCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3)
)


class _IbmappnNodeEnSegGen_Type(Integer32):
    """Custom type ibmappnNodeEnSegGen based on Integer32"""
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


_IbmappnNodeEnSegGen_Type.__name__ = "Integer32"
_IbmappnNodeEnSegGen_Object = MibScalar
ibmappnNodeEnSegGen = _IbmappnNodeEnSegGen_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 1),
    _IbmappnNodeEnSegGen_Type()
)
ibmappnNodeEnSegGen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnSegGen.setStatus("mandatory")


class _IbmappnNodeEnModeCosMap_Type(Integer32):
    """Custom type ibmappnNodeEnModeCosMap based on Integer32"""
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


_IbmappnNodeEnModeCosMap_Type.__name__ = "Integer32"
_IbmappnNodeEnModeCosMap_Object = MibScalar
ibmappnNodeEnModeCosMap = _IbmappnNodeEnModeCosMap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 2),
    _IbmappnNodeEnModeCosMap_Type()
)
ibmappnNodeEnModeCosMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnModeCosMap.setStatus("mandatory")


class _IbmappnNodeEnLocateCdinit_Type(Integer32):
    """Custom type ibmappnNodeEnLocateCdinit based on Integer32"""
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


_IbmappnNodeEnLocateCdinit_Type.__name__ = "Integer32"
_IbmappnNodeEnLocateCdinit_Object = MibScalar
ibmappnNodeEnLocateCdinit = _IbmappnNodeEnLocateCdinit_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 3),
    _IbmappnNodeEnLocateCdinit_Type()
)
ibmappnNodeEnLocateCdinit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnLocateCdinit.setStatus("mandatory")


class _IbmappnNodeEnSendRegNames_Type(Integer32):
    """Custom type ibmappnNodeEnSendRegNames based on Integer32"""
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


_IbmappnNodeEnSendRegNames_Type.__name__ = "Integer32"
_IbmappnNodeEnSendRegNames_Object = MibScalar
ibmappnNodeEnSendRegNames = _IbmappnNodeEnSendRegNames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 4),
    _IbmappnNodeEnSendRegNames_Type()
)
ibmappnNodeEnSendRegNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnSendRegNames.setStatus("mandatory")


class _IbmappnNodeEnSendRegChar_Type(Integer32):
    """Custom type ibmappnNodeEnSendRegChar based on Integer32"""
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


_IbmappnNodeEnSendRegChar_Type.__name__ = "Integer32"
_IbmappnNodeEnSendRegChar_Object = MibScalar
ibmappnNodeEnSendRegChar = _IbmappnNodeEnSendRegChar_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 3, 5),
    _IbmappnNodeEnSendRegChar_Type()
)
ibmappnNodeEnSendRegChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeEnSendRegChar.setStatus("mandatory")
_IbmappnPortInformation_ObjectIdentity = ObjectIdentity
ibmappnPortInformation = _IbmappnPortInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4)
)
_IbmappnNodePortTable_Object = MibTable
ibmappnNodePortTable = _IbmappnNodePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ibmappnNodePortTable.setStatus("mandatory")
_IbmappnNodePortEntry_Object = MibTableRow
ibmappnNodePortEntry = _IbmappnNodePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1)
)
ibmappnNodePortEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodePortName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortEntry.setStatus("mandatory")


class _IbmappnNodePortName_Type(DisplayString):
    """Custom type ibmappnNodePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortName_Type.__name__ = "DisplayString"
_IbmappnNodePortName_Object = MibTableColumn
ibmappnNodePortName = _IbmappnNodePortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 1),
    _IbmappnNodePortName_Type()
)
ibmappnNodePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortName.setStatus("mandatory")


class _IbmappnNodePortState_Type(Integer32):
    """Custom type ibmappnNodePortState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodePortState_Type.__name__ = "Integer32"
_IbmappnNodePortState_Object = MibTableColumn
ibmappnNodePortState = _IbmappnNodePortState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 2),
    _IbmappnNodePortState_Type()
)
ibmappnNodePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnNodePortState.setStatus("mandatory")


class _IbmappnNodePortDlcType_Type(Integer32):
    """Custom type ibmappnNodePortDlcType based on Integer32"""
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
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenRing", 6))
    )


_IbmappnNodePortDlcType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcType_Object = MibTableColumn
ibmappnNodePortDlcType = _IbmappnNodePortDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 3),
    _IbmappnNodePortDlcType_Type()
)
ibmappnNodePortDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcType.setStatus("mandatory")


class _IbmappnNodePortPortType_Type(Integer32):
    """Custom type ibmappnNodePortPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leased", 1),
          ("sharedAccessFacilities", 3),
          ("switched", 2))
    )


_IbmappnNodePortPortType_Type.__name__ = "Integer32"
_IbmappnNodePortPortType_Object = MibTableColumn
ibmappnNodePortPortType = _IbmappnNodePortPortType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 4),
    _IbmappnNodePortPortType_Type()
)
ibmappnNodePortPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortPortType.setStatus("mandatory")


class _IbmappnNodePortSIMRIM_Type(Integer32):
    """Custom type ibmappnNodePortSIMRIM based on Integer32"""
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


_IbmappnNodePortSIMRIM_Type.__name__ = "Integer32"
_IbmappnNodePortSIMRIM_Object = MibTableColumn
ibmappnNodePortSIMRIM = _IbmappnNodePortSIMRIM_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 5),
    _IbmappnNodePortSIMRIM_Type()
)
ibmappnNodePortSIMRIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortSIMRIM.setStatus("mandatory")


class _IbmappnNodePortLsRole_Type(Integer32):
    """Custom type ibmappnNodePortLsRole based on Integer32"""
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
        *(("abm", 4),
          ("negotiable", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_IbmappnNodePortLsRole_Type.__name__ = "Integer32"
_IbmappnNodePortLsRole_Object = MibTableColumn
ibmappnNodePortLsRole = _IbmappnNodePortLsRole_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 6),
    _IbmappnNodePortLsRole_Type()
)
ibmappnNodePortLsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortLsRole.setStatus("mandatory")
_IbmappnNodePortMaxRcvBtuSize_Type = Integer32
_IbmappnNodePortMaxRcvBtuSize_Object = MibTableColumn
ibmappnNodePortMaxRcvBtuSize = _IbmappnNodePortMaxRcvBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 7),
    _IbmappnNodePortMaxRcvBtuSize_Type()
)
ibmappnNodePortMaxRcvBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortMaxRcvBtuSize.setStatus("mandatory")
_IbmappnNodePortMaxIframeWindow_Type = Integer32
_IbmappnNodePortMaxIframeWindow_Object = MibTableColumn
ibmappnNodePortMaxIframeWindow = _IbmappnNodePortMaxIframeWindow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 8),
    _IbmappnNodePortMaxIframeWindow_Type()
)
ibmappnNodePortMaxIframeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortMaxIframeWindow.setStatus("mandatory")
_IbmappnNodePortDefLsGoodXids_Type = Counter32
_IbmappnNodePortDefLsGoodXids_Object = MibTableColumn
ibmappnNodePortDefLsGoodXids = _IbmappnNodePortDefLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 9),
    _IbmappnNodePortDefLsGoodXids_Type()
)
ibmappnNodePortDefLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDefLsGoodXids.setStatus("mandatory")
_IbmappnNodePortDefLsBadXids_Type = Counter32
_IbmappnNodePortDefLsBadXids_Object = MibTableColumn
ibmappnNodePortDefLsBadXids = _IbmappnNodePortDefLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 10),
    _IbmappnNodePortDefLsBadXids_Type()
)
ibmappnNodePortDefLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDefLsBadXids.setStatus("mandatory")
_IbmappnNodePortDynLsGoodXids_Type = Counter32
_IbmappnNodePortDynLsGoodXids_Object = MibTableColumn
ibmappnNodePortDynLsGoodXids = _IbmappnNodePortDynLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 11),
    _IbmappnNodePortDynLsGoodXids_Type()
)
ibmappnNodePortDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDynLsGoodXids.setStatus("mandatory")
_IbmappnNodePortDynLsBadXids_Type = Counter32
_IbmappnNodePortDynLsBadXids_Object = MibTableColumn
ibmappnNodePortDynLsBadXids = _IbmappnNodePortDynLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 12),
    _IbmappnNodePortDynLsBadXids_Type()
)
ibmappnNodePortDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDynLsBadXids.setStatus("mandatory")
_IbmappnNodePortSpecific_Type = ObjectIdentifier
_IbmappnNodePortSpecific_Object = MibTableColumn
ibmappnNodePortSpecific = _IbmappnNodePortSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 1, 1, 13),
    _IbmappnNodePortSpecific_Type()
)
ibmappnNodePortSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortSpecific.setStatus("mandatory")
_IbmappnNodePortIpTable_Object = MibTable
ibmappnNodePortIpTable = _IbmappnNodePortIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ibmappnNodePortIpTable.setStatus("mandatory")
_IbmappnNodePortIpEntry_Object = MibTableRow
ibmappnNodePortIpEntry = _IbmappnNodePortIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2, 1)
)
ibmappnNodePortIpEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodePortIpName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortIpEntry.setStatus("mandatory")


class _IbmappnNodePortIpName_Type(DisplayString):
    """Custom type ibmappnNodePortIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortIpName_Type.__name__ = "DisplayString"
_IbmappnNodePortIpName_Object = MibTableColumn
ibmappnNodePortIpName = _IbmappnNodePortIpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2, 1, 1),
    _IbmappnNodePortIpName_Type()
)
ibmappnNodePortIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortIpName.setStatus("mandatory")
_IbmappnNodePortIpPortNum_Type = Integer32
_IbmappnNodePortIpPortNum_Object = MibTableColumn
ibmappnNodePortIpPortNum = _IbmappnNodePortIpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 2, 1, 2),
    _IbmappnNodePortIpPortNum_Type()
)
ibmappnNodePortIpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortIpPortNum.setStatus("mandatory")
_IbmappnNodePortDlsTable_Object = MibTable
ibmappnNodePortDlsTable = _IbmappnNodePortDlsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlsTable.setStatus("mandatory")
_IbmappnNodePortDlsEntry_Object = MibTableRow
ibmappnNodePortDlsEntry = _IbmappnNodePortDlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1)
)
ibmappnNodePortDlsEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodePortDlsName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlsEntry.setStatus("mandatory")


class _IbmappnNodePortDlsName_Type(DisplayString):
    """Custom type ibmappnNodePortDlsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortDlsName_Type.__name__ = "DisplayString"
_IbmappnNodePortDlsName_Object = MibTableColumn
ibmappnNodePortDlsName = _IbmappnNodePortDlsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1, 1),
    _IbmappnNodePortDlsName_Type()
)
ibmappnNodePortDlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlsName.setStatus("mandatory")


class _IbmappnNodePortDlsMac_Type(OctetString):
    """Custom type ibmappnNodePortDlsMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodePortDlsMac_Type.__name__ = "OctetString"
_IbmappnNodePortDlsMac_Object = MibTableColumn
ibmappnNodePortDlsMac = _IbmappnNodePortDlsMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1, 2),
    _IbmappnNodePortDlsMac_Type()
)
ibmappnNodePortDlsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlsMac.setStatus("mandatory")


class _IbmappnNodePortDlsSap_Type(OctetString):
    """Custom type ibmappnNodePortDlsSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodePortDlsSap_Type.__name__ = "OctetString"
_IbmappnNodePortDlsSap_Object = MibTableColumn
ibmappnNodePortDlsSap = _IbmappnNodePortDlsSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 3, 1, 3),
    _IbmappnNodePortDlsSap_Type()
)
ibmappnNodePortDlsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlsSap.setStatus("mandatory")
_IbmappnNodePortTrTable_Object = MibTable
ibmappnNodePortTrTable = _IbmappnNodePortTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ibmappnNodePortTrTable.setStatus("mandatory")
_IbmappnNodePortTrEntry_Object = MibTableRow
ibmappnNodePortTrEntry = _IbmappnNodePortTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1)
)
ibmappnNodePortTrEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodePortTrName"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortTrEntry.setStatus("mandatory")


class _IbmappnNodePortTrName_Type(DisplayString):
    """Custom type ibmappnNodePortTrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodePortTrName_Type.__name__ = "DisplayString"
_IbmappnNodePortTrName_Object = MibTableColumn
ibmappnNodePortTrName = _IbmappnNodePortTrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1, 1),
    _IbmappnNodePortTrName_Type()
)
ibmappnNodePortTrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortTrName.setStatus("mandatory")


class _IbmappnNodePortTrMac_Type(OctetString):
    """Custom type ibmappnNodePortTrMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodePortTrMac_Type.__name__ = "OctetString"
_IbmappnNodePortTrMac_Object = MibTableColumn
ibmappnNodePortTrMac = _IbmappnNodePortTrMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1, 2),
    _IbmappnNodePortTrMac_Type()
)
ibmappnNodePortTrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortTrMac.setStatus("mandatory")


class _IbmappnNodePortTrSap_Type(OctetString):
    """Custom type ibmappnNodePortTrSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodePortTrSap_Type.__name__ = "OctetString"
_IbmappnNodePortTrSap_Object = MibTableColumn
ibmappnNodePortTrSap = _IbmappnNodePortTrSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 4, 1, 3),
    _IbmappnNodePortTrSap_Type()
)
ibmappnNodePortTrSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortTrSap.setStatus("mandatory")
_IbmappnNodePortDlcTraceTable_Object = MibTable
ibmappnNodePortDlcTraceTable = _IbmappnNodePortDlcTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTraceTable.setStatus("mandatory")
_IbmappnNodePortDlcTraceEntry_Object = MibTableRow
ibmappnNodePortDlcTraceEntry = _IbmappnNodePortDlcTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1)
)
ibmappnNodePortDlcTraceEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodePortDlcTracPortName"),
    (0, "IBM-6611-APPN-MIB", "ibmappnNodePortDlcTracIndex"),
)
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTraceEntry.setStatus("mandatory")
_IbmappnNodePortDlcTracPortName_Type = DisplayString
_IbmappnNodePortDlcTracPortName_Object = MibTableColumn
ibmappnNodePortDlcTracPortName = _IbmappnNodePortDlcTracPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 1),
    _IbmappnNodePortDlcTracPortName_Type()
)
ibmappnNodePortDlcTracPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracPortName.setStatus("mandatory")
_IbmappnNodePortDlcTracIndex_Type = Integer32
_IbmappnNodePortDlcTracIndex_Object = MibTableColumn
ibmappnNodePortDlcTracIndex = _IbmappnNodePortDlcTracIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 2),
    _IbmappnNodePortDlcTracIndex_Type()
)
ibmappnNodePortDlcTracIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracIndex.setStatus("mandatory")


class _IbmappnNodePortDlcTracDlcType_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracDlcType based on Integer32"""
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
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenRing", 6))
    )


_IbmappnNodePortDlcTracDlcType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracDlcType_Object = MibTableColumn
ibmappnNodePortDlcTracDlcType = _IbmappnNodePortDlcTracDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 3),
    _IbmappnNodePortDlcTracDlcType_Type()
)
ibmappnNodePortDlcTracDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracDlcType.setStatus("mandatory")
_IbmappnNodePortDlcTracLocalAddr_Type = DisplayString
_IbmappnNodePortDlcTracLocalAddr_Object = MibTableColumn
ibmappnNodePortDlcTracLocalAddr = _IbmappnNodePortDlcTracLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 4),
    _IbmappnNodePortDlcTracLocalAddr_Type()
)
ibmappnNodePortDlcTracLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracLocalAddr.setStatus("mandatory")
_IbmappnNodePortDlcTracRemoteAddr_Type = DisplayString
_IbmappnNodePortDlcTracRemoteAddr_Object = MibTableColumn
ibmappnNodePortDlcTracRemoteAddr = _IbmappnNodePortDlcTracRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 5),
    _IbmappnNodePortDlcTracRemoteAddr_Type()
)
ibmappnNodePortDlcTracRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracRemoteAddr.setStatus("mandatory")


class _IbmappnNodePortDlcTracMsgType_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracMsgType based on Integer32"""
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
        *(("confirm", 4),
          ("indication", 5),
          ("other", 1),
          ("request", 3),
          ("response", 6),
          ("unknown", 2))
    )


_IbmappnNodePortDlcTracMsgType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracMsgType_Object = MibTableColumn
ibmappnNodePortDlcTracMsgType = _IbmappnNodePortDlcTracMsgType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 6),
    _IbmappnNodePortDlcTracMsgType_Type()
)
ibmappnNodePortDlcTracMsgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracMsgType.setStatus("mandatory")


class _IbmappnNodePortDlcTracCmdType_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracCmdType based on Integer32"""
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
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2012,
              2013,
              2014,
              2015,
              2016,
              2017,
              2018,
              2019,
              2020,
              2021,
              2022,
              2023,
              2024,
              2025,
              2026,
              4124,
              6001,
              6002,
              6003,
              6004,
              6005,
              6006,
              6007,
              6008,
              6009,
              6010,
              6012,
              6013,
              6014,
              6015,
              6016,
              6017,
              6018,
              6019,
              6020,
              6021,
              6022,
              6023,
              6024,
              6025,
              6026)
        )
    )
    namedValues = NamedValues(
        *(("alterSap", 23),
          ("contFrame", 8),
          ("contedFrame", 9),
          ("curFrame", 3),
          ("dgrmFrame", 6),
          ("dlsIpm", 4124),
          ("enterBusy", 12),
          ("exitBusy", 13),
          ("gnetFrame", 20),
          ("haltFrame", 14),
          ("haltLsNow", 25),
          ("iFrame", 10),
          ("icrFrame", 4),
          ("ipAlterSap", 2023),
          ("ipContFrame", 2008),
          ("ipContedFrame", 2009),
          ("ipCurFrame", 2003),
          ("ipDgrmFrame", 2006),
          ("ipEnterBusy", 2012),
          ("ipExitBusy", 2013),
          ("ipGnetFrame", 2020),
          ("ipHaltFrame", 2014),
          ("ipHaltLsNow", 2025),
          ("ipIFrame", 2010),
          ("ipIcrFrame", 2004),
          ("ipLsHalted", 2015),
          ("ipLsRestarted", 2017),
          ("ipNetBioSnq", 2018),
          ("ipNetBioSnr", 2019),
          ("ipNetdFrame", 2021),
          ("ipOobFrame", 2022),
          ("ipRespAck", 2005),
          ("ipRespFrame", 2002),
          ("ipRestartLs", 2016),
          ("ipTestFrame", 2001),
          ("ipTestReq", 2026),
          ("ipTestRsp", 2024),
          ("ipXidFrame", 2007),
          ("lsHalted", 15),
          ("lsRestarted", 17),
          ("netBioSnq", 18),
          ("netBioSnr", 19),
          ("netdFrame", 21),
          ("oobFrame", 22),
          ("respAck", 5),
          ("respFrame", 2),
          ("restartLs", 16),
          ("testFrame", 1),
          ("testReq", 26),
          ("testRsp", 24),
          ("trAlterSap", 6023),
          ("trContFrame", 6008),
          ("trContedFrame", 6009),
          ("trCurFrame", 6003),
          ("trDgrmFrame", 6006),
          ("trEnterBusy", 6012),
          ("trExitBusy", 6013),
          ("trGnetFrame", 6020),
          ("trHaltFrame", 6014),
          ("trHaltLsNow", 6025),
          ("trIFrame", 6010),
          ("trIcrFrame", 6004),
          ("trLsHalted", 6015),
          ("trLsRestarted", 6017),
          ("trNetBioSnq", 6018),
          ("trNetBioSnr", 6019),
          ("trNetdFrame", 6021),
          ("trOobFrame", 6022),
          ("trRespAck", 6005),
          ("trRespFrame", 6002),
          ("trRestartLs", 6016),
          ("trTestFrame", 6001),
          ("trTestReq", 6026),
          ("trTestRsp", 6024),
          ("trXidFrame", 6007),
          ("xidFrame", 7))
    )


_IbmappnNodePortDlcTracCmdType_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracCmdType_Object = MibTableColumn
ibmappnNodePortDlcTracCmdType = _IbmappnNodePortDlcTracCmdType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 7),
    _IbmappnNodePortDlcTracCmdType_Type()
)
ibmappnNodePortDlcTracCmdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracCmdType.setStatus("mandatory")


class _IbmappnNodePortDlcTracUseWan_Type(Integer32):
    """Custom type ibmappnNodePortDlcTracUseWan based on Integer32"""
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
        *(("notApplicable", 2),
          ("other", 1),
          ("useLan", 5),
          ("useUnknown", 3),
          ("useWan", 4))
    )


_IbmappnNodePortDlcTracUseWan_Type.__name__ = "Integer32"
_IbmappnNodePortDlcTracUseWan_Object = MibTableColumn
ibmappnNodePortDlcTracUseWan = _IbmappnNodePortDlcTracUseWan_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 4, 5, 1, 8),
    _IbmappnNodePortDlcTracUseWan_Type()
)
ibmappnNodePortDlcTracUseWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodePortDlcTracUseWan.setStatus("mandatory")
_IbmappnLinkStationInformation_ObjectIdentity = ObjectIdentity
ibmappnLinkStationInformation = _IbmappnLinkStationInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5)
)
_IbmappnNodeLsTable_Object = MibTable
ibmappnNodeLsTable = _IbmappnNodeLsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsTable.setStatus("mandatory")
_IbmappnNodeLsEntry_Object = MibTableRow
ibmappnNodeLsEntry = _IbmappnNodeLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1)
)
ibmappnNodeLsEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodeLsName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsEntry.setStatus("mandatory")


class _IbmappnNodeLsName_Type(DisplayString):
    """Custom type ibmappnNodeLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsName_Type.__name__ = "DisplayString"
_IbmappnNodeLsName_Object = MibTableColumn
ibmappnNodeLsName = _IbmappnNodeLsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 1),
    _IbmappnNodeLsName_Type()
)
ibmappnNodeLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsName.setStatus("mandatory")


class _IbmappnNodeLsPortName_Type(DisplayString):
    """Custom type ibmappnNodeLsPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsPortName_Type.__name__ = "DisplayString"
_IbmappnNodeLsPortName_Object = MibTableColumn
ibmappnNodeLsPortName = _IbmappnNodeLsPortName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 2),
    _IbmappnNodeLsPortName_Type()
)
ibmappnNodeLsPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsPortName.setStatus("mandatory")


class _IbmappnNodeLsDlcType_Type(Integer32):
    """Custom type ibmappnNodeLsDlcType based on Integer32"""
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
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenRing", 6))
    )


_IbmappnNodeLsDlcType_Type.__name__ = "Integer32"
_IbmappnNodeLsDlcType_Object = MibTableColumn
ibmappnNodeLsDlcType = _IbmappnNodeLsDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 3),
    _IbmappnNodeLsDlcType_Type()
)
ibmappnNodeLsDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDlcType.setStatus("mandatory")


class _IbmappnNodeLsDynamic_Type(Integer32):
    """Custom type ibmappnNodeLsDynamic based on Integer32"""
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


_IbmappnNodeLsDynamic_Type.__name__ = "Integer32"
_IbmappnNodeLsDynamic_Object = MibTableColumn
ibmappnNodeLsDynamic = _IbmappnNodeLsDynamic_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 4),
    _IbmappnNodeLsDynamic_Type()
)
ibmappnNodeLsDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDynamic.setStatus("mandatory")


class _IbmappnNodeLsState_Type(Integer32):
    """Custom type ibmappnNodeLsState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsState_Type.__name__ = "Integer32"
_IbmappnNodeLsState_Object = MibTableColumn
ibmappnNodeLsState = _IbmappnNodeLsState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 5),
    _IbmappnNodeLsState_Type()
)
ibmappnNodeLsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibmappnNodeLsState.setStatus("mandatory")


class _IbmappnNodeLsCpName_Type(DisplayString):
    """Custom type ibmappnNodeLsCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNodeLsCpName_Type.__name__ = "DisplayString"
_IbmappnNodeLsCpName_Object = MibTableColumn
ibmappnNodeLsCpName = _IbmappnNodeLsCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 6),
    _IbmappnNodeLsCpName_Type()
)
ibmappnNodeLsCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCpName.setStatus("mandatory")
_IbmappnNodeLsTgNum_Type = Integer32
_IbmappnNodeLsTgNum_Object = MibTableColumn
ibmappnNodeLsTgNum = _IbmappnNodeLsTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 7),
    _IbmappnNodeLsTgNum_Type()
)
ibmappnNodeLsTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTgNum.setStatus("mandatory")


class _IbmappnNodeLsLimResource_Type(Integer32):
    """Custom type ibmappnNodeLsLimResource based on Integer32"""
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


_IbmappnNodeLsLimResource_Type.__name__ = "Integer32"
_IbmappnNodeLsLimResource_Object = MibTableColumn
ibmappnNodeLsLimResource = _IbmappnNodeLsLimResource_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 8),
    _IbmappnNodeLsLimResource_Type()
)
ibmappnNodeLsLimResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLimResource.setStatus("mandatory")


class _IbmappnNodeLsMigration_Type(Integer32):
    """Custom type ibmappnNodeLsMigration based on Integer32"""
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


_IbmappnNodeLsMigration_Type.__name__ = "Integer32"
_IbmappnNodeLsMigration_Object = MibTableColumn
ibmappnNodeLsMigration = _IbmappnNodeLsMigration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 9),
    _IbmappnNodeLsMigration_Type()
)
ibmappnNodeLsMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMigration.setStatus("mandatory")


class _IbmappnNodeLsBlockNum_Type(DisplayString):
    """Custom type ibmappnNodeLsBlockNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_IbmappnNodeLsBlockNum_Type.__name__ = "DisplayString"
_IbmappnNodeLsBlockNum_Object = MibTableColumn
ibmappnNodeLsBlockNum = _IbmappnNodeLsBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 10),
    _IbmappnNodeLsBlockNum_Type()
)
ibmappnNodeLsBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsBlockNum.setStatus("mandatory")


class _IbmappnNodeLsIdNum_Type(DisplayString):
    """Custom type ibmappnNodeLsIdNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_IbmappnNodeLsIdNum_Type.__name__ = "DisplayString"
_IbmappnNodeLsIdNum_Object = MibTableColumn
ibmappnNodeLsIdNum = _IbmappnNodeLsIdNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 11),
    _IbmappnNodeLsIdNum_Type()
)
ibmappnNodeLsIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsIdNum.setStatus("mandatory")


class _IbmappnNodeLsCpCpSession_Type(Integer32):
    """Custom type ibmappnNodeLsCpCpSession based on Integer32"""
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


_IbmappnNodeLsCpCpSession_Type.__name__ = "Integer32"
_IbmappnNodeLsCpCpSession_Object = MibTableColumn
ibmappnNodeLsCpCpSession = _IbmappnNodeLsCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 12),
    _IbmappnNodeLsCpCpSession_Type()
)
ibmappnNodeLsCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCpCpSession.setStatus("mandatory")
_IbmappnNodeLsTargetPacingCount_Type = Integer32
_IbmappnNodeLsTargetPacingCount_Object = MibTableColumn
ibmappnNodeLsTargetPacingCount = _IbmappnNodeLsTargetPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 13),
    _IbmappnNodeLsTargetPacingCount_Type()
)
ibmappnNodeLsTargetPacingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTargetPacingCount.setStatus("mandatory")
_IbmappnNodeLsMaxSendBtuSize_Type = Integer32
_IbmappnNodeLsMaxSendBtuSize_Object = MibTableColumn
ibmappnNodeLsMaxSendBtuSize = _IbmappnNodeLsMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 14),
    _IbmappnNodeLsMaxSendBtuSize_Type()
)
ibmappnNodeLsMaxSendBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMaxSendBtuSize.setStatus("mandatory")
_IbmappnNodeLsEffCap_Type = Integer32
_IbmappnNodeLsEffCap_Object = MibTableColumn
ibmappnNodeLsEffCap = _IbmappnNodeLsEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 15),
    _IbmappnNodeLsEffCap_Type()
)
ibmappnNodeLsEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsEffCap.setStatus("mandatory")


class _IbmappnNodeLsConnCost_Type(Integer32):
    """Custom type ibmappnNodeLsConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsConnCost_Type.__name__ = "Integer32"
_IbmappnNodeLsConnCost_Object = MibTableColumn
ibmappnNodeLsConnCost = _IbmappnNodeLsConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 16),
    _IbmappnNodeLsConnCost_Type()
)
ibmappnNodeLsConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsConnCost.setStatus("mandatory")


class _IbmappnNodeLsByteCost_Type(Integer32):
    """Custom type ibmappnNodeLsByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsByteCost_Type.__name__ = "Integer32"
_IbmappnNodeLsByteCost_Object = MibTableColumn
ibmappnNodeLsByteCost = _IbmappnNodeLsByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 17),
    _IbmappnNodeLsByteCost_Type()
)
ibmappnNodeLsByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsByteCost.setStatus("mandatory")


class _IbmappnNodeLsSecurity_Type(Integer32):
    """Custom type ibmappnNodeLsSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnNodeLsSecurity_Type.__name__ = "Integer32"
_IbmappnNodeLsSecurity_Object = MibTableColumn
ibmappnNodeLsSecurity = _IbmappnNodeLsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 18),
    _IbmappnNodeLsSecurity_Type()
)
ibmappnNodeLsSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsSecurity.setStatus("mandatory")


class _IbmappnNodeLsDelay_Type(Integer32):
    """Custom type ibmappnNodeLsDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnNodeLsDelay_Type.__name__ = "Integer32"
_IbmappnNodeLsDelay_Object = MibTableColumn
ibmappnNodeLsDelay = _IbmappnNodeLsDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 19),
    _IbmappnNodeLsDelay_Type()
)
ibmappnNodeLsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDelay.setStatus("mandatory")


class _IbmappnNodeLsUsr1_Type(Integer32):
    """Custom type ibmappnNodeLsUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsUsr1_Type.__name__ = "Integer32"
_IbmappnNodeLsUsr1_Object = MibTableColumn
ibmappnNodeLsUsr1 = _IbmappnNodeLsUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 20),
    _IbmappnNodeLsUsr1_Type()
)
ibmappnNodeLsUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsUsr1.setStatus("mandatory")


class _IbmappnNodeLsUsr2_Type(Integer32):
    """Custom type ibmappnNodeLsUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsUsr2_Type.__name__ = "Integer32"
_IbmappnNodeLsUsr2_Object = MibTableColumn
ibmappnNodeLsUsr2 = _IbmappnNodeLsUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 21),
    _IbmappnNodeLsUsr2_Type()
)
ibmappnNodeLsUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsUsr2.setStatus("mandatory")


class _IbmappnNodeLsUsr3_Type(Integer32):
    """Custom type ibmappnNodeLsUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNodeLsUsr3_Type.__name__ = "Integer32"
_IbmappnNodeLsUsr3_Object = MibTableColumn
ibmappnNodeLsUsr3 = _IbmappnNodeLsUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 22),
    _IbmappnNodeLsUsr3_Type()
)
ibmappnNodeLsUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsUsr3.setStatus("mandatory")
_IbmappnNodeLsInXidBytes_Type = Counter32
_IbmappnNodeLsInXidBytes_Object = MibTableColumn
ibmappnNodeLsInXidBytes = _IbmappnNodeLsInXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 23),
    _IbmappnNodeLsInXidBytes_Type()
)
ibmappnNodeLsInXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInXidBytes.setStatus("mandatory")
_IbmappnNodeLsInMsgBytes_Type = Counter32
_IbmappnNodeLsInMsgBytes_Object = MibTableColumn
ibmappnNodeLsInMsgBytes = _IbmappnNodeLsInMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 24),
    _IbmappnNodeLsInMsgBytes_Type()
)
ibmappnNodeLsInMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInMsgBytes.setStatus("mandatory")
_IbmappnNodeLsInXidFrames_Type = Counter32
_IbmappnNodeLsInXidFrames_Object = MibTableColumn
ibmappnNodeLsInXidFrames = _IbmappnNodeLsInXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 25),
    _IbmappnNodeLsInXidFrames_Type()
)
ibmappnNodeLsInXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInXidFrames.setStatus("mandatory")
_IbmappnNodeLsInMsgFrames_Type = Counter32
_IbmappnNodeLsInMsgFrames_Object = MibTableColumn
ibmappnNodeLsInMsgFrames = _IbmappnNodeLsInMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 26),
    _IbmappnNodeLsInMsgFrames_Type()
)
ibmappnNodeLsInMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsInMsgFrames.setStatus("mandatory")
_IbmappnNodeLsOutXidBytes_Type = Counter32
_IbmappnNodeLsOutXidBytes_Object = MibTableColumn
ibmappnNodeLsOutXidBytes = _IbmappnNodeLsOutXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 27),
    _IbmappnNodeLsOutXidBytes_Type()
)
ibmappnNodeLsOutXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutXidBytes.setStatus("mandatory")
_IbmappnNodeLsOutMsgBytes_Type = Counter32
_IbmappnNodeLsOutMsgBytes_Object = MibTableColumn
ibmappnNodeLsOutMsgBytes = _IbmappnNodeLsOutMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 28),
    _IbmappnNodeLsOutMsgBytes_Type()
)
ibmappnNodeLsOutMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutMsgBytes.setStatus("mandatory")
_IbmappnNodeLsOutXidFrames_Type = Counter32
_IbmappnNodeLsOutXidFrames_Object = MibTableColumn
ibmappnNodeLsOutXidFrames = _IbmappnNodeLsOutXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 29),
    _IbmappnNodeLsOutXidFrames_Type()
)
ibmappnNodeLsOutXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutXidFrames.setStatus("mandatory")
_IbmappnNodeLsOutMsgFrames_Type = Counter32
_IbmappnNodeLsOutMsgFrames_Object = MibTableColumn
ibmappnNodeLsOutMsgFrames = _IbmappnNodeLsOutMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 30),
    _IbmappnNodeLsOutMsgFrames_Type()
)
ibmappnNodeLsOutMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsOutMsgFrames.setStatus("mandatory")
_IbmappnNodeLsEchoRsps_Type = Counter32
_IbmappnNodeLsEchoRsps_Object = MibTableColumn
ibmappnNodeLsEchoRsps = _IbmappnNodeLsEchoRsps_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 31),
    _IbmappnNodeLsEchoRsps_Type()
)
ibmappnNodeLsEchoRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsEchoRsps.setStatus("mandatory")
_IbmappnNodeLsCurrentDelay_Type = Integer32
_IbmappnNodeLsCurrentDelay_Object = MibTableColumn
ibmappnNodeLsCurrentDelay = _IbmappnNodeLsCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 32),
    _IbmappnNodeLsCurrentDelay_Type()
)
ibmappnNodeLsCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCurrentDelay.setStatus("mandatory")
_IbmappnNodeLsMaxDelay_Type = Integer32
_IbmappnNodeLsMaxDelay_Object = MibTableColumn
ibmappnNodeLsMaxDelay = _IbmappnNodeLsMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 33),
    _IbmappnNodeLsMaxDelay_Type()
)
ibmappnNodeLsMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMaxDelay.setStatus("mandatory")
_IbmappnNodeLsMinDelay_Type = Integer32
_IbmappnNodeLsMinDelay_Object = MibTableColumn
ibmappnNodeLsMinDelay = _IbmappnNodeLsMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 34),
    _IbmappnNodeLsMinDelay_Type()
)
ibmappnNodeLsMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMinDelay.setStatus("mandatory")
_IbmappnNodeLsMaxDelayTime_Type = TimeTicks
_IbmappnNodeLsMaxDelayTime_Object = MibTableColumn
ibmappnNodeLsMaxDelayTime = _IbmappnNodeLsMaxDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 35),
    _IbmappnNodeLsMaxDelayTime_Type()
)
ibmappnNodeLsMaxDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsMaxDelayTime.setStatus("mandatory")
_IbmappnNodeLsGoodXids_Type = Counter32
_IbmappnNodeLsGoodXids_Object = MibTableColumn
ibmappnNodeLsGoodXids = _IbmappnNodeLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 36),
    _IbmappnNodeLsGoodXids_Type()
)
ibmappnNodeLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsGoodXids.setStatus("mandatory")
_IbmappnNodeLsBadXids_Type = Counter32
_IbmappnNodeLsBadXids_Object = MibTableColumn
ibmappnNodeLsBadXids = _IbmappnNodeLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 37),
    _IbmappnNodeLsBadXids_Type()
)
ibmappnNodeLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsBadXids.setStatus("mandatory")
_IbmappnNodeLsSpecific_Type = ObjectIdentifier
_IbmappnNodeLsSpecific_Object = MibTableColumn
ibmappnNodeLsSpecific = _IbmappnNodeLsSpecific_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 38),
    _IbmappnNodeLsSpecific_Type()
)
ibmappnNodeLsSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsSpecific.setStatus("mandatory")


class _IbmappnNodeLsSubState_Type(Integer32):
    """Custom type ibmappnNodeLsSubState based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("active", 6),
          ("inactive", 1),
          ("pendDeact", 15),
          ("pendRcvConnInd", 12),
          ("pendSendConnRsp", 13),
          ("pendXidExch", 3),
          ("sentActAs", 4),
          ("sentConnReq", 11),
          ("sentConnRsp", 14),
          ("sentCreateTg", 10),
          ("sentDeactAsOrd", 7),
          ("sentDestroyTg", 9),
          ("sentDiscOrd", 8),
          ("sentReqOpnstn", 2),
          ("sentSetMode", 5))
    )


_IbmappnNodeLsSubState_Type.__name__ = "Integer32"
_IbmappnNodeLsSubState_Object = MibTableColumn
ibmappnNodeLsSubState = _IbmappnNodeLsSubState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 39),
    _IbmappnNodeLsSubState_Type()
)
ibmappnNodeLsSubState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsSubState.setStatus("mandatory")
_IbmappnNodeLsStartTime_Type = TimeTicks
_IbmappnNodeLsStartTime_Object = MibTableColumn
ibmappnNodeLsStartTime = _IbmappnNodeLsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 40),
    _IbmappnNodeLsStartTime_Type()
)
ibmappnNodeLsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStartTime.setStatus("mandatory")
_IbmappnNodeLsActiveTime_Type = TimeTicks
_IbmappnNodeLsActiveTime_Object = MibTableColumn
ibmappnNodeLsActiveTime = _IbmappnNodeLsActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 41),
    _IbmappnNodeLsActiveTime_Type()
)
ibmappnNodeLsActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsActiveTime.setStatus("mandatory")
_IbmappnNodeLsCurrentStateTime_Type = TimeTicks
_IbmappnNodeLsCurrentStateTime_Object = MibTableColumn
ibmappnNodeLsCurrentStateTime = _IbmappnNodeLsCurrentStateTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 1, 1, 42),
    _IbmappnNodeLsCurrentStateTime_Type()
)
ibmappnNodeLsCurrentStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsCurrentStateTime.setStatus("mandatory")
_IbmappnNodeLsIpTable_Object = MibTable
ibmappnNodeLsIpTable = _IbmappnNodeLsIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsIpTable.setStatus("mandatory")
_IbmappnNodeLsIpEntry_Object = MibTableRow
ibmappnNodeLsIpEntry = _IbmappnNodeLsIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1)
)
ibmappnNodeLsIpEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodeLsIpName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsIpEntry.setStatus("mandatory")


class _IbmappnNodeLsIpName_Type(DisplayString):
    """Custom type ibmappnNodeLsIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsIpName_Type.__name__ = "DisplayString"
_IbmappnNodeLsIpName_Object = MibTableColumn
ibmappnNodeLsIpName = _IbmappnNodeLsIpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 1),
    _IbmappnNodeLsIpName_Type()
)
ibmappnNodeLsIpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsIpName.setStatus("mandatory")


class _IbmappnNodeLsIpState_Type(Integer32):
    """Custom type ibmappnNodeLsIpState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsIpState_Type.__name__ = "Integer32"
_IbmappnNodeLsIpState_Object = MibTableColumn
ibmappnNodeLsIpState = _IbmappnNodeLsIpState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 2),
    _IbmappnNodeLsIpState_Type()
)
ibmappnNodeLsIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsIpState.setStatus("mandatory")
_IbmappnNodeLsLocalIpAddr_Type = IpAddress
_IbmappnNodeLsLocalIpAddr_Object = MibTableColumn
ibmappnNodeLsLocalIpAddr = _IbmappnNodeLsLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 3),
    _IbmappnNodeLsLocalIpAddr_Type()
)
ibmappnNodeLsLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalIpAddr.setStatus("mandatory")
_IbmappnNodeLsLocalIpPortNum_Type = Integer32
_IbmappnNodeLsLocalIpPortNum_Object = MibTableColumn
ibmappnNodeLsLocalIpPortNum = _IbmappnNodeLsLocalIpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 4),
    _IbmappnNodeLsLocalIpPortNum_Type()
)
ibmappnNodeLsLocalIpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalIpPortNum.setStatus("mandatory")
_IbmappnNodeLsRemoteIpAddr_Type = IpAddress
_IbmappnNodeLsRemoteIpAddr_Object = MibTableColumn
ibmappnNodeLsRemoteIpAddr = _IbmappnNodeLsRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 5),
    _IbmappnNodeLsRemoteIpAddr_Type()
)
ibmappnNodeLsRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteIpAddr.setStatus("mandatory")
_IbmappnNodeLsRemoteIpPortNum_Type = Integer32
_IbmappnNodeLsRemoteIpPortNum_Object = MibTableColumn
ibmappnNodeLsRemoteIpPortNum = _IbmappnNodeLsRemoteIpPortNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 2, 1, 6),
    _IbmappnNodeLsRemoteIpPortNum_Type()
)
ibmappnNodeLsRemoteIpPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteIpPortNum.setStatus("mandatory")
_IbmappnNodeLsDlsTable_Object = MibTable
ibmappnNodeLsDlsTable = _IbmappnNodeLsDlsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsTable.setStatus("mandatory")
_IbmappnNodeLsDlsEntry_Object = MibTableRow
ibmappnNodeLsDlsEntry = _IbmappnNodeLsDlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1)
)
ibmappnNodeLsDlsEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodeLsDlsName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsEntry.setStatus("mandatory")


class _IbmappnNodeLsDlsName_Type(DisplayString):
    """Custom type ibmappnNodeLsDlsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsDlsName_Type.__name__ = "DisplayString"
_IbmappnNodeLsDlsName_Object = MibTableColumn
ibmappnNodeLsDlsName = _IbmappnNodeLsDlsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 1),
    _IbmappnNodeLsDlsName_Type()
)
ibmappnNodeLsDlsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsName.setStatus("mandatory")


class _IbmappnNodeLsDlsState_Type(Integer32):
    """Custom type ibmappnNodeLsDlsState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsDlsState_Type.__name__ = "Integer32"
_IbmappnNodeLsDlsState_Object = MibTableColumn
ibmappnNodeLsDlsState = _IbmappnNodeLsDlsState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 2),
    _IbmappnNodeLsDlsState_Type()
)
ibmappnNodeLsDlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsDlsState.setStatus("mandatory")


class _IbmappnNodeLsLocalDlsMac_Type(OctetString):
    """Custom type ibmappnNodeLsLocalDlsMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsLocalDlsMac_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalDlsMac_Object = MibTableColumn
ibmappnNodeLsLocalDlsMac = _IbmappnNodeLsLocalDlsMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 3),
    _IbmappnNodeLsLocalDlsMac_Type()
)
ibmappnNodeLsLocalDlsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalDlsMac.setStatus("mandatory")


class _IbmappnNodeLsLocalDlsSap_Type(OctetString):
    """Custom type ibmappnNodeLsLocalDlsSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsLocalDlsSap_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalDlsSap_Object = MibTableColumn
ibmappnNodeLsLocalDlsSap = _IbmappnNodeLsLocalDlsSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 4),
    _IbmappnNodeLsLocalDlsSap_Type()
)
ibmappnNodeLsLocalDlsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalDlsSap.setStatus("mandatory")


class _IbmappnNodeLsRemoteDlsMac_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteDlsMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsRemoteDlsMac_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteDlsMac_Object = MibTableColumn
ibmappnNodeLsRemoteDlsMac = _IbmappnNodeLsRemoteDlsMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 5),
    _IbmappnNodeLsRemoteDlsMac_Type()
)
ibmappnNodeLsRemoteDlsMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteDlsMac.setStatus("mandatory")


class _IbmappnNodeLsRemoteDlsSap_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteDlsSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsRemoteDlsSap_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteDlsSap_Object = MibTableColumn
ibmappnNodeLsRemoteDlsSap = _IbmappnNodeLsRemoteDlsSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 3, 1, 6),
    _IbmappnNodeLsRemoteDlsSap_Type()
)
ibmappnNodeLsRemoteDlsSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteDlsSap.setStatus("mandatory")
_IbmappnNodeLsTrTable_Object = MibTable
ibmappnNodeLsTrTable = _IbmappnNodeLsTrTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsTrTable.setStatus("mandatory")
_IbmappnNodeLsTrEntry_Object = MibTableRow
ibmappnNodeLsTrEntry = _IbmappnNodeLsTrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1)
)
ibmappnNodeLsTrEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodeLsTrName"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsTrEntry.setStatus("mandatory")


class _IbmappnNodeLsTrName_Type(DisplayString):
    """Custom type ibmappnNodeLsTrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsTrName_Type.__name__ = "DisplayString"
_IbmappnNodeLsTrName_Object = MibTableColumn
ibmappnNodeLsTrName = _IbmappnNodeLsTrName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 1),
    _IbmappnNodeLsTrName_Type()
)
ibmappnNodeLsTrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTrName.setStatus("mandatory")


class _IbmappnNodeLsTrState_Type(Integer32):
    """Custom type ibmappnNodeLsTrState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_IbmappnNodeLsTrState_Type.__name__ = "Integer32"
_IbmappnNodeLsTrState_Object = MibTableColumn
ibmappnNodeLsTrState = _IbmappnNodeLsTrState_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 2),
    _IbmappnNodeLsTrState_Type()
)
ibmappnNodeLsTrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsTrState.setStatus("mandatory")


class _IbmappnNodeLsLocalTrMac_Type(OctetString):
    """Custom type ibmappnNodeLsLocalTrMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsLocalTrMac_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalTrMac_Object = MibTableColumn
ibmappnNodeLsLocalTrMac = _IbmappnNodeLsLocalTrMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 3),
    _IbmappnNodeLsLocalTrMac_Type()
)
ibmappnNodeLsLocalTrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalTrMac.setStatus("mandatory")


class _IbmappnNodeLsLocalTrSap_Type(OctetString):
    """Custom type ibmappnNodeLsLocalTrSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsLocalTrSap_Type.__name__ = "OctetString"
_IbmappnNodeLsLocalTrSap_Object = MibTableColumn
ibmappnNodeLsLocalTrSap = _IbmappnNodeLsLocalTrSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 4),
    _IbmappnNodeLsLocalTrSap_Type()
)
ibmappnNodeLsLocalTrSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsLocalTrSap.setStatus("mandatory")


class _IbmappnNodeLsRemoteTrMac_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteTrMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IbmappnNodeLsRemoteTrMac_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteTrMac_Object = MibTableColumn
ibmappnNodeLsRemoteTrMac = _IbmappnNodeLsRemoteTrMac_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 5),
    _IbmappnNodeLsRemoteTrMac_Type()
)
ibmappnNodeLsRemoteTrMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteTrMac.setStatus("mandatory")


class _IbmappnNodeLsRemoteTrSap_Type(OctetString):
    """Custom type ibmappnNodeLsRemoteTrSap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_IbmappnNodeLsRemoteTrSap_Type.__name__ = "OctetString"
_IbmappnNodeLsRemoteTrSap_Object = MibTableColumn
ibmappnNodeLsRemoteTrSap = _IbmappnNodeLsRemoteTrSap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 4, 1, 6),
    _IbmappnNodeLsRemoteTrSap_Type()
)
ibmappnNodeLsRemoteTrSap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsRemoteTrSap.setStatus("mandatory")
_IbmappnNodeLsStatusTable_Object = MibTable
ibmappnNodeLsStatusTable = _IbmappnNodeLsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5)
)
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusTable.setStatus("mandatory")
_IbmappnNodeLsStatusEntry_Object = MibTableRow
ibmappnNodeLsStatusEntry = _IbmappnNodeLsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1)
)
ibmappnNodeLsStatusEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNodeLsStatusIndex"),
)
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusEntry.setStatus("mandatory")
_IbmappnNodeLsStatusIndex_Type = Integer32
_IbmappnNodeLsStatusIndex_Object = MibTableColumn
ibmappnNodeLsStatusIndex = _IbmappnNodeLsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 1),
    _IbmappnNodeLsStatusIndex_Type()
)
ibmappnNodeLsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusIndex.setStatus("mandatory")
_IbmappnNodeLsStatusTime_Type = TimeTicks
_IbmappnNodeLsStatusTime_Object = MibTableColumn
ibmappnNodeLsStatusTime = _IbmappnNodeLsStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 2),
    _IbmappnNodeLsStatusTime_Type()
)
ibmappnNodeLsStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusTime.setStatus("mandatory")


class _IbmappnNodeLsStatusLsName_Type(DisplayString):
    """Custom type ibmappnNodeLsStatusLsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnNodeLsStatusLsName_Type.__name__ = "DisplayString"
_IbmappnNodeLsStatusLsName_Object = MibTableColumn
ibmappnNodeLsStatusLsName = _IbmappnNodeLsStatusLsName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 3),
    _IbmappnNodeLsStatusLsName_Type()
)
ibmappnNodeLsStatusLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusLsName.setStatus("mandatory")


class _IbmappnNodeLsStatusCpName_Type(DisplayString):
    """Custom type ibmappnNodeLsStatusCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNodeLsStatusCpName_Type.__name__ = "DisplayString"
_IbmappnNodeLsStatusCpName_Object = MibTableColumn
ibmappnNodeLsStatusCpName = _IbmappnNodeLsStatusCpName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 4),
    _IbmappnNodeLsStatusCpName_Type()
)
ibmappnNodeLsStatusCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusCpName.setStatus("mandatory")
_IbmappnNodeLsStatusNodeId_Type = OctetString
_IbmappnNodeLsStatusNodeId_Object = MibTableColumn
ibmappnNodeLsStatusNodeId = _IbmappnNodeLsStatusNodeId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 5),
    _IbmappnNodeLsStatusNodeId_Type()
)
ibmappnNodeLsStatusNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusNodeId.setStatus("mandatory")


class _IbmappnNodeLsStatusTgNum_Type(Integer32):
    """Custom type ibmappnNodeLsStatusTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IbmappnNodeLsStatusTgNum_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusTgNum_Object = MibTableColumn
ibmappnNodeLsStatusTgNum = _IbmappnNodeLsStatusTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 6),
    _IbmappnNodeLsStatusTgNum_Type()
)
ibmappnNodeLsStatusTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusTgNum.setStatus("mandatory")
_IbmappnNodeLsStatusGeneralSense_Type = OctetString
_IbmappnNodeLsStatusGeneralSense_Object = MibTableColumn
ibmappnNodeLsStatusGeneralSense = _IbmappnNodeLsStatusGeneralSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 7),
    _IbmappnNodeLsStatusGeneralSense_Type()
)
ibmappnNodeLsStatusGeneralSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusGeneralSense.setStatus("mandatory")


class _IbmappnNodeLsStatusNofRetry_Type(Integer32):
    """Custom type ibmappnNodeLsStatusNofRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noretry", 2),
          ("retry", 1))
    )


_IbmappnNodeLsStatusNofRetry_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusNofRetry_Object = MibTableColumn
ibmappnNodeLsStatusNofRetry = _IbmappnNodeLsStatusNofRetry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 8),
    _IbmappnNodeLsStatusNofRetry_Type()
)
ibmappnNodeLsStatusNofRetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusNofRetry.setStatus("mandatory")
_IbmappnNodeLsStatusEndSense_Type = OctetString
_IbmappnNodeLsStatusEndSense_Object = MibTableColumn
ibmappnNodeLsStatusEndSense = _IbmappnNodeLsStatusEndSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 9),
    _IbmappnNodeLsStatusEndSense_Type()
)
ibmappnNodeLsStatusEndSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusEndSense.setStatus("mandatory")
_IbmappnNodeLsStatusXidLocalSense_Type = OctetString
_IbmappnNodeLsStatusXidLocalSense_Object = MibTableColumn
ibmappnNodeLsStatusXidLocalSense = _IbmappnNodeLsStatusXidLocalSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 10),
    _IbmappnNodeLsStatusXidLocalSense_Type()
)
ibmappnNodeLsStatusXidLocalSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidLocalSense.setStatus("mandatory")
_IbmappnNodeLsStatusXidRemoteSense_Type = OctetString
_IbmappnNodeLsStatusXidRemoteSense_Object = MibTableColumn
ibmappnNodeLsStatusXidRemoteSense = _IbmappnNodeLsStatusXidRemoteSense_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 11),
    _IbmappnNodeLsStatusXidRemoteSense_Type()
)
ibmappnNodeLsStatusXidRemoteSense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidRemoteSense.setStatus("mandatory")


class _IbmappnNodeLsStatusXidByteInError_Type(Integer32):
    """Custom type ibmappnNodeLsStatusXidByteInError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1000
        )
    )
    namedValues = NamedValues(
        ("na", 1000)
    )


_IbmappnNodeLsStatusXidByteInError_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusXidByteInError_Object = MibTableColumn
ibmappnNodeLsStatusXidByteInError = _IbmappnNodeLsStatusXidByteInError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 12),
    _IbmappnNodeLsStatusXidByteInError_Type()
)
ibmappnNodeLsStatusXidByteInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidByteInError.setStatus("mandatory")


class _IbmappnNodeLsStatusXidBitInError_Type(Integer32):
    """Custom type ibmappnNodeLsStatusXidBitInError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("na", 8)
    )


_IbmappnNodeLsStatusXidBitInError_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusXidBitInError_Object = MibTableColumn
ibmappnNodeLsStatusXidBitInError = _IbmappnNodeLsStatusXidBitInError_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 13),
    _IbmappnNodeLsStatusXidBitInError_Type()
)
ibmappnNodeLsStatusXidBitInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusXidBitInError.setStatus("mandatory")


class _IbmappnNodeLsStatusDlcType_Type(Integer32):
    """Custom type ibmappnNodeLsStatusDlcType based on Integer32"""
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
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tr", 6))
    )


_IbmappnNodeLsStatusDlcType_Type.__name__ = "Integer32"
_IbmappnNodeLsStatusDlcType_Object = MibTableColumn
ibmappnNodeLsStatusDlcType = _IbmappnNodeLsStatusDlcType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 14),
    _IbmappnNodeLsStatusDlcType_Type()
)
ibmappnNodeLsStatusDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusDlcType.setStatus("mandatory")
_IbmappnNodeLsStatusLocalAddr_Type = DisplayString
_IbmappnNodeLsStatusLocalAddr_Object = MibTableColumn
ibmappnNodeLsStatusLocalAddr = _IbmappnNodeLsStatusLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 15),
    _IbmappnNodeLsStatusLocalAddr_Type()
)
ibmappnNodeLsStatusLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusLocalAddr.setStatus("mandatory")
_IbmappnNodeLsStatusRemoteAddr_Type = DisplayString
_IbmappnNodeLsStatusRemoteAddr_Object = MibTableColumn
ibmappnNodeLsStatusRemoteAddr = _IbmappnNodeLsStatusRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 5, 5, 1, 16),
    _IbmappnNodeLsStatusRemoteAddr_Type()
)
ibmappnNodeLsStatusRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeLsStatusRemoteAddr.setStatus("mandatory")
_IbmappnSnmpInformation_ObjectIdentity = ObjectIdentity
ibmappnSnmpInformation = _IbmappnSnmpInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6)
)
_IbmappnSnmpInPkts_Type = Counter32
_IbmappnSnmpInPkts_Object = MibScalar
ibmappnSnmpInPkts = _IbmappnSnmpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 1),
    _IbmappnSnmpInPkts_Type()
)
ibmappnSnmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInPkts.setStatus("mandatory")
_IbmappnSnmpInGetRequests_Type = Counter32
_IbmappnSnmpInGetRequests_Object = MibScalar
ibmappnSnmpInGetRequests = _IbmappnSnmpInGetRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 2),
    _IbmappnSnmpInGetRequests_Type()
)
ibmappnSnmpInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetRequests.setStatus("mandatory")
_IbmappnSnmpInGetNexts_Type = Counter32
_IbmappnSnmpInGetNexts_Object = MibScalar
ibmappnSnmpInGetNexts = _IbmappnSnmpInGetNexts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 3),
    _IbmappnSnmpInGetNexts_Type()
)
ibmappnSnmpInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetNexts.setStatus("mandatory")
_IbmappnSnmpInSetRequests_Type = Counter32
_IbmappnSnmpInSetRequests_Object = MibScalar
ibmappnSnmpInSetRequests = _IbmappnSnmpInSetRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 4),
    _IbmappnSnmpInSetRequests_Type()
)
ibmappnSnmpInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInSetRequests.setStatus("mandatory")
_IbmappnSnmpInTotalVars_Type = Counter32
_IbmappnSnmpInTotalVars_Object = MibScalar
ibmappnSnmpInTotalVars = _IbmappnSnmpInTotalVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 5),
    _IbmappnSnmpInTotalVars_Type()
)
ibmappnSnmpInTotalVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInTotalVars.setStatus("mandatory")
_IbmappnSnmpInGetVars_Type = Counter32
_IbmappnSnmpInGetVars_Object = MibScalar
ibmappnSnmpInGetVars = _IbmappnSnmpInGetVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 6),
    _IbmappnSnmpInGetVars_Type()
)
ibmappnSnmpInGetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetVars.setStatus("mandatory")
_IbmappnSnmpInGetNextVars_Type = Counter32
_IbmappnSnmpInGetNextVars_Object = MibScalar
ibmappnSnmpInGetNextVars = _IbmappnSnmpInGetNextVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 7),
    _IbmappnSnmpInGetNextVars_Type()
)
ibmappnSnmpInGetNextVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInGetNextVars.setStatus("mandatory")
_IbmappnSnmpInSetVars_Type = Counter32
_IbmappnSnmpInSetVars_Object = MibScalar
ibmappnSnmpInSetVars = _IbmappnSnmpInSetVars_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 8),
    _IbmappnSnmpInSetVars_Type()
)
ibmappnSnmpInSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpInSetVars.setStatus("mandatory")
_IbmappnSnmpOutNoSuchNames_Type = Counter32
_IbmappnSnmpOutNoSuchNames_Object = MibScalar
ibmappnSnmpOutNoSuchNames = _IbmappnSnmpOutNoSuchNames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 9),
    _IbmappnSnmpOutNoSuchNames_Type()
)
ibmappnSnmpOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpOutNoSuchNames.setStatus("mandatory")
_IbmappnSnmpOutGenErrs_Type = Counter32
_IbmappnSnmpOutGenErrs_Object = MibScalar
ibmappnSnmpOutGenErrs = _IbmappnSnmpOutGenErrs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 6, 10),
    _IbmappnSnmpOutGenErrs_Type()
)
ibmappnSnmpOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnSnmpOutGenErrs.setStatus("mandatory")
_IbmappnMemoryUse_ObjectIdentity = ObjectIdentity
ibmappnMemoryUse = _IbmappnMemoryUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7)
)
_IbmappnMemorySize_Type = Integer32
_IbmappnMemorySize_Object = MibScalar
ibmappnMemorySize = _IbmappnMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 1),
    _IbmappnMemorySize_Type()
)
ibmappnMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemorySize.setStatus("mandatory")
_IbmappnMemoryUsed_Type = Integer32
_IbmappnMemoryUsed_Object = MibScalar
ibmappnMemoryUsed = _IbmappnMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 2),
    _IbmappnMemoryUsed_Type()
)
ibmappnMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryUsed.setStatus("mandatory")
_IbmappnMemoryWarnThresh_Type = Integer32
_IbmappnMemoryWarnThresh_Object = MibScalar
ibmappnMemoryWarnThresh = _IbmappnMemoryWarnThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 3),
    _IbmappnMemoryWarnThresh_Type()
)
ibmappnMemoryWarnThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryWarnThresh.setStatus("mandatory")
_IbmappnMemoryCritThresh_Type = Integer32
_IbmappnMemoryCritThresh_Object = MibScalar
ibmappnMemoryCritThresh = _IbmappnMemoryCritThresh_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 4),
    _IbmappnMemoryCritThresh_Type()
)
ibmappnMemoryCritThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnMemoryCritThresh.setStatus("mandatory")
_IbmappnXidInformation_ObjectIdentity = ObjectIdentity
ibmappnXidInformation = _IbmappnXidInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8)
)
_IbmappnNodeDefLsGoodXids_Type = Counter32
_IbmappnNodeDefLsGoodXids_Object = MibScalar
ibmappnNodeDefLsGoodXids = _IbmappnNodeDefLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 1),
    _IbmappnNodeDefLsGoodXids_Type()
)
ibmappnNodeDefLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDefLsGoodXids.setStatus("mandatory")
_IbmappnNodeDefLsBadXids_Type = Counter32
_IbmappnNodeDefLsBadXids_Object = MibScalar
ibmappnNodeDefLsBadXids = _IbmappnNodeDefLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 2),
    _IbmappnNodeDefLsBadXids_Type()
)
ibmappnNodeDefLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDefLsBadXids.setStatus("mandatory")
_IbmappnNodeDynLsGoodXids_Type = Counter32
_IbmappnNodeDynLsGoodXids_Object = MibScalar
ibmappnNodeDynLsGoodXids = _IbmappnNodeDynLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 3),
    _IbmappnNodeDynLsGoodXids_Type()
)
ibmappnNodeDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDynLsGoodXids.setStatus("mandatory")
_IbmappnNodeDynLsBadXids_Type = Counter32
_IbmappnNodeDynLsBadXids_Object = MibScalar
ibmappnNodeDynLsBadXids = _IbmappnNodeDynLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 8, 4),
    _IbmappnNodeDynLsBadXids_Type()
)
ibmappnNodeDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNodeDynLsBadXids.setStatus("mandatory")
_IbmappnNn_ObjectIdentity = ObjectIdentity
ibmappnNn = _IbmappnNn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2)
)
_IbmappnNnTopo_ObjectIdentity = ObjectIdentity
ibmappnNnTopo = _IbmappnNnTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1)
)
_IbmappnNnTopoMaxNodes_Type = Integer32
_IbmappnNnTopoMaxNodes_Object = MibScalar
ibmappnNnTopoMaxNodes = _IbmappnNnTopoMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 1),
    _IbmappnNnTopoMaxNodes_Type()
)
ibmappnNnTopoMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoMaxNodes.setStatus("mandatory")
_IbmappnNnTopoCurNumNodes_Type = Gauge32
_IbmappnNnTopoCurNumNodes_Object = MibScalar
ibmappnNnTopoCurNumNodes = _IbmappnNnTopoCurNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 2),
    _IbmappnNnTopoCurNumNodes_Type()
)
ibmappnNnTopoCurNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoCurNumNodes.setStatus("mandatory")
_IbmappnNnTopoInTdus_Type = Counter32
_IbmappnNnTopoInTdus_Object = MibScalar
ibmappnNnTopoInTdus = _IbmappnNnTopoInTdus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 3),
    _IbmappnNnTopoInTdus_Type()
)
ibmappnNnTopoInTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoInTdus.setStatus("mandatory")
_IbmappnNnTopoOutTdus_Type = Counter32
_IbmappnNnTopoOutTdus_Object = MibScalar
ibmappnNnTopoOutTdus = _IbmappnNnTopoOutTdus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 4),
    _IbmappnNnTopoOutTdus_Type()
)
ibmappnNnTopoOutTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoOutTdus.setStatus("mandatory")
_IbmappnNnTopoNodeLowRsns_Type = Counter32
_IbmappnNnTopoNodeLowRsns_Object = MibScalar
ibmappnNnTopoNodeLowRsns = _IbmappnNnTopoNodeLowRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 5),
    _IbmappnNnTopoNodeLowRsns_Type()
)
ibmappnNnTopoNodeLowRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeLowRsns.setStatus("mandatory")
_IbmappnNnTopoNodeEqualRsns_Type = Counter32
_IbmappnNnTopoNodeEqualRsns_Object = MibScalar
ibmappnNnTopoNodeEqualRsns = _IbmappnNnTopoNodeEqualRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 6),
    _IbmappnNnTopoNodeEqualRsns_Type()
)
ibmappnNnTopoNodeEqualRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeEqualRsns.setStatus("mandatory")
_IbmappnNnTopoNodeGoodHighRsns_Type = Counter32
_IbmappnNnTopoNodeGoodHighRsns_Object = MibScalar
ibmappnNnTopoNodeGoodHighRsns = _IbmappnNnTopoNodeGoodHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 7),
    _IbmappnNnTopoNodeGoodHighRsns_Type()
)
ibmappnNnTopoNodeGoodHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeGoodHighRsns.setStatus("mandatory")
_IbmappnNnTopoNodeBadHighRsns_Type = Counter32
_IbmappnNnTopoNodeBadHighRsns_Object = MibScalar
ibmappnNnTopoNodeBadHighRsns = _IbmappnNnTopoNodeBadHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 8),
    _IbmappnNnTopoNodeBadHighRsns_Type()
)
ibmappnNnTopoNodeBadHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeBadHighRsns.setStatus("mandatory")
_IbmappnNnTopoNodeStateUpdates_Type = Counter32
_IbmappnNnTopoNodeStateUpdates_Object = MibScalar
ibmappnNnTopoNodeStateUpdates = _IbmappnNnTopoNodeStateUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 9),
    _IbmappnNnTopoNodeStateUpdates_Type()
)
ibmappnNnTopoNodeStateUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeStateUpdates.setStatus("mandatory")
_IbmappnNnTopoNodeErrors_Type = Counter32
_IbmappnNnTopoNodeErrors_Object = MibScalar
ibmappnNnTopoNodeErrors = _IbmappnNnTopoNodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 10),
    _IbmappnNnTopoNodeErrors_Type()
)
ibmappnNnTopoNodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeErrors.setStatus("mandatory")
_IbmappnNnTopoNodeTimerUpdates_Type = Counter32
_IbmappnNnTopoNodeTimerUpdates_Object = MibScalar
ibmappnNnTopoNodeTimerUpdates = _IbmappnNnTopoNodeTimerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 11),
    _IbmappnNnTopoNodeTimerUpdates_Type()
)
ibmappnNnTopoNodeTimerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodeTimerUpdates.setStatus("mandatory")
_IbmappnNnTopoNodePurges_Type = Counter32
_IbmappnNnTopoNodePurges_Object = MibScalar
ibmappnNnTopoNodePurges = _IbmappnNnTopoNodePurges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 12),
    _IbmappnNnTopoNodePurges_Type()
)
ibmappnNnTopoNodePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoNodePurges.setStatus("mandatory")
_IbmappnNnTopoTgLowRsns_Type = Counter32
_IbmappnNnTopoTgLowRsns_Object = MibScalar
ibmappnNnTopoTgLowRsns = _IbmappnNnTopoTgLowRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 13),
    _IbmappnNnTopoTgLowRsns_Type()
)
ibmappnNnTopoTgLowRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgLowRsns.setStatus("mandatory")
_IbmappnNnTopoTgEqualRsns_Type = Counter32
_IbmappnNnTopoTgEqualRsns_Object = MibScalar
ibmappnNnTopoTgEqualRsns = _IbmappnNnTopoTgEqualRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 14),
    _IbmappnNnTopoTgEqualRsns_Type()
)
ibmappnNnTopoTgEqualRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgEqualRsns.setStatus("mandatory")
_IbmappnNnTopoTgGoodHighRsns_Type = Counter32
_IbmappnNnTopoTgGoodHighRsns_Object = MibScalar
ibmappnNnTopoTgGoodHighRsns = _IbmappnNnTopoTgGoodHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 15),
    _IbmappnNnTopoTgGoodHighRsns_Type()
)
ibmappnNnTopoTgGoodHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgGoodHighRsns.setStatus("mandatory")
_IbmappnNnTopoTgBadHighRsns_Type = Counter32
_IbmappnNnTopoTgBadHighRsns_Object = MibScalar
ibmappnNnTopoTgBadHighRsns = _IbmappnNnTopoTgBadHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 16),
    _IbmappnNnTopoTgBadHighRsns_Type()
)
ibmappnNnTopoTgBadHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgBadHighRsns.setStatus("mandatory")
_IbmappnNnTopoTgStateUpdates_Type = Counter32
_IbmappnNnTopoTgStateUpdates_Object = MibScalar
ibmappnNnTopoTgStateUpdates = _IbmappnNnTopoTgStateUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 17),
    _IbmappnNnTopoTgStateUpdates_Type()
)
ibmappnNnTopoTgStateUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgStateUpdates.setStatus("mandatory")
_IbmappnNnTopoTgErrors_Type = Counter32
_IbmappnNnTopoTgErrors_Object = MibScalar
ibmappnNnTopoTgErrors = _IbmappnNnTopoTgErrors_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 18),
    _IbmappnNnTopoTgErrors_Type()
)
ibmappnNnTopoTgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgErrors.setStatus("mandatory")
_IbmappnNnTopoTgTimerUpdates_Type = Counter32
_IbmappnNnTopoTgTimerUpdates_Object = MibScalar
ibmappnNnTopoTgTimerUpdates = _IbmappnNnTopoTgTimerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 19),
    _IbmappnNnTopoTgTimerUpdates_Type()
)
ibmappnNnTopoTgTimerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgTimerUpdates.setStatus("mandatory")
_IbmappnNnTopoTgPurges_Type = Counter32
_IbmappnNnTopoTgPurges_Object = MibScalar
ibmappnNnTopoTgPurges = _IbmappnNnTopoTgPurges_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 20),
    _IbmappnNnTopoTgPurges_Type()
)
ibmappnNnTopoTgPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTgPurges.setStatus("mandatory")
_IbmappnNnTopoTotalRouteCalcs_Type = Counter32
_IbmappnNnTopoTotalRouteCalcs_Object = MibScalar
ibmappnNnTopoTotalRouteCalcs = _IbmappnNnTopoTotalRouteCalcs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 21),
    _IbmappnNnTopoTotalRouteCalcs_Type()
)
ibmappnNnTopoTotalRouteCalcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTotalRouteCalcs.setStatus("mandatory")
_IbmappnNnTopoTotalRouteRejs_Type = Counter32
_IbmappnNnTopoTotalRouteRejs_Object = MibScalar
ibmappnNnTopoTotalRouteRejs = _IbmappnNnTopoTotalRouteRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 22),
    _IbmappnNnTopoTotalRouteRejs_Type()
)
ibmappnNnTopoTotalRouteRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoTotalRouteRejs.setStatus("mandatory")
_IbmappnNnTopoRouteTable_Object = MibTable
ibmappnNnTopoRouteTable = _IbmappnNnTopoRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23)
)
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteTable.setStatus("mandatory")
_IbmappnNnTopoRouteEntry_Object = MibTableRow
ibmappnNnTopoRouteEntry = _IbmappnNnTopoRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1)
)
ibmappnNnTopoRouteEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTopoRouteCos"),
)
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteEntry.setStatus("mandatory")
_IbmappnNnTopoRouteCos_Type = DisplayString
_IbmappnNnTopoRouteCos_Object = MibTableColumn
ibmappnNnTopoRouteCos = _IbmappnNnTopoRouteCos_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 1),
    _IbmappnNnTopoRouteCos_Type()
)
ibmappnNnTopoRouteCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteCos.setStatus("mandatory")
_IbmappnNnTopoRouteTrees_Type = Counter32
_IbmappnNnTopoRouteTrees_Object = MibTableColumn
ibmappnNnTopoRouteTrees = _IbmappnNnTopoRouteTrees_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 2),
    _IbmappnNnTopoRouteTrees_Type()
)
ibmappnNnTopoRouteTrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteTrees.setStatus("mandatory")
_IbmappnNnTopoRouteCalcs_Type = Counter32
_IbmappnNnTopoRouteCalcs_Object = MibTableColumn
ibmappnNnTopoRouteCalcs = _IbmappnNnTopoRouteCalcs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 3),
    _IbmappnNnTopoRouteCalcs_Type()
)
ibmappnNnTopoRouteCalcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteCalcs.setStatus("mandatory")
_IbmappnNnTopoRouteRejs_Type = Counter32
_IbmappnNnTopoRouteRejs_Object = MibTableColumn
ibmappnNnTopoRouteRejs = _IbmappnNnTopoRouteRejs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 1, 23, 1, 4),
    _IbmappnNnTopoRouteRejs_Type()
)
ibmappnNnTopoRouteRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTopoRouteRejs.setStatus("mandatory")
_IbmappnNnAdjNodeTable_Object = MibTable
ibmappnNnAdjNodeTable = _IbmappnNnAdjNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2)
)
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeTable.setStatus("mandatory")
_IbmappnNnAdjNodeEntry_Object = MibTableRow
ibmappnNnAdjNodeEntry = _IbmappnNnAdjNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1)
)
ibmappnNnAdjNodeEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNnAdjNodeAdjName"),
)
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeEntry.setStatus("mandatory")


class _IbmappnNnAdjNodeAdjName_Type(DisplayString):
    """Custom type ibmappnNnAdjNodeAdjName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnAdjNodeAdjName_Type.__name__ = "DisplayString"
_IbmappnNnAdjNodeAdjName_Object = MibTableColumn
ibmappnNnAdjNodeAdjName = _IbmappnNnAdjNodeAdjName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 1),
    _IbmappnNnAdjNodeAdjName_Type()
)
ibmappnNnAdjNodeAdjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeAdjName.setStatus("mandatory")


class _IbmappnNnAdjNodeCpCpSessStatus_Type(Integer32):
    """Custom type ibmappnNnAdjNodeCpCpSessStatus based on Integer32"""
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
        *(("active", 1),
          ("conLoserActive", 2),
          ("conWinnerActive", 3),
          ("inactive", 4))
    )


_IbmappnNnAdjNodeCpCpSessStatus_Type.__name__ = "Integer32"
_IbmappnNnAdjNodeCpCpSessStatus_Object = MibTableColumn
ibmappnNnAdjNodeCpCpSessStatus = _IbmappnNnAdjNodeCpCpSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 2),
    _IbmappnNnAdjNodeCpCpSessStatus_Type()
)
ibmappnNnAdjNodeCpCpSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeCpCpSessStatus.setStatus("mandatory")
_IbmappnNnAdjNodeOutOfSeqTdus_Type = Gauge32
_IbmappnNnAdjNodeOutOfSeqTdus_Object = MibTableColumn
ibmappnNnAdjNodeOutOfSeqTdus = _IbmappnNnAdjNodeOutOfSeqTdus_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 3),
    _IbmappnNnAdjNodeOutOfSeqTdus_Type()
)
ibmappnNnAdjNodeOutOfSeqTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeOutOfSeqTdus.setStatus("mandatory")


class _IbmappnNnAdjNodeLastFrsnSent_Type(Integer32):
    """Custom type ibmappnNnAdjNodeLastFrsnSent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnAdjNodeLastFrsnSent_Type.__name__ = "Integer32"
_IbmappnNnAdjNodeLastFrsnSent_Object = MibTableColumn
ibmappnNnAdjNodeLastFrsnSent = _IbmappnNnAdjNodeLastFrsnSent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 4),
    _IbmappnNnAdjNodeLastFrsnSent_Type()
)
ibmappnNnAdjNodeLastFrsnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeLastFrsnSent.setStatus("mandatory")


class _IbmappnNnAdjNodeLastFrsnRcvd_Type(Integer32):
    """Custom type ibmappnNnAdjNodeLastFrsnRcvd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnAdjNodeLastFrsnRcvd_Type.__name__ = "Integer32"
_IbmappnNnAdjNodeLastFrsnRcvd_Object = MibTableColumn
ibmappnNnAdjNodeLastFrsnRcvd = _IbmappnNnAdjNodeLastFrsnRcvd_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 2, 1, 5),
    _IbmappnNnAdjNodeLastFrsnRcvd_Type()
)
ibmappnNnAdjNodeLastFrsnRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnAdjNodeLastFrsnRcvd.setStatus("mandatory")
_IbmappnNnTopology_ObjectIdentity = ObjectIdentity
ibmappnNnTopology = _IbmappnNnTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3)
)
_IbmappnNnTopologyTable_Object = MibTable
ibmappnNnTopologyTable = _IbmappnNnTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyTable.setStatus("mandatory")
_IbmappnNnTopologyEntry_Object = MibTableRow
ibmappnNnTopologyEntry = _IbmappnNnTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1)
)
ibmappnNnTopologyEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNnNodeName"),
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyEntry.setStatus("mandatory")


class _IbmappnNnNodeName_Type(DisplayString):
    """Custom type ibmappnNnNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnNodeName_Type.__name__ = "DisplayString"
_IbmappnNnNodeName_Object = MibTableColumn
ibmappnNnNodeName = _IbmappnNnNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 1),
    _IbmappnNnNodeName_Type()
)
ibmappnNnNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeName.setStatus("mandatory")


class _IbmappnNnNodeFrsn_Type(Integer32):
    """Custom type ibmappnNnNodeFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnNodeFrsn_Type.__name__ = "Integer32"
_IbmappnNnNodeFrsn_Object = MibTableColumn
ibmappnNnNodeFrsn = _IbmappnNnNodeFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 2),
    _IbmappnNnNodeFrsn_Type()
)
ibmappnNnNodeFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFrsn.setStatus("mandatory")


class _IbmappnNnNodeEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnNodeEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnNodeEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnNodeEntryTimeLeft_Object = MibTableColumn
ibmappnNnNodeEntryTimeLeft = _IbmappnNnNodeEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 3),
    _IbmappnNnNodeEntryTimeLeft_Type()
)
ibmappnNnNodeEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeEntryTimeLeft.setStatus("mandatory")


class _IbmappnNnNodeType_Type(Integer32):
    """Custom type ibmappnNnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networknode", 1),
          ("virtualnode", 3))
    )


_IbmappnNnNodeType_Type.__name__ = "Integer32"
_IbmappnNnNodeType_Object = MibTableColumn
ibmappnNnNodeType = _IbmappnNnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 4),
    _IbmappnNnNodeType_Type()
)
ibmappnNnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeType.setStatus("mandatory")
_IbmappnNnNodeRsn_Type = Integer32
_IbmappnNnNodeRsn_Object = MibTableColumn
ibmappnNnNodeRsn = _IbmappnNnNodeRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 5),
    _IbmappnNnNodeRsn_Type()
)
ibmappnNnNodeRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeRsn.setStatus("mandatory")
_IbmappnNnNodeRouteAddResist_Type = Integer32
_IbmappnNnNodeRouteAddResist_Object = MibTableColumn
ibmappnNnNodeRouteAddResist = _IbmappnNnNodeRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 6),
    _IbmappnNnNodeRouteAddResist_Type()
)
ibmappnNnNodeRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeRouteAddResist.setStatus("mandatory")


class _IbmappnNnNodeCongested_Type(Integer32):
    """Custom type ibmappnNnNodeCongested based on Integer32"""
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


_IbmappnNnNodeCongested_Type.__name__ = "Integer32"
_IbmappnNnNodeCongested_Object = MibTableColumn
ibmappnNnNodeCongested = _IbmappnNnNodeCongested_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 7),
    _IbmappnNnNodeCongested_Type()
)
ibmappnNnNodeCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeCongested.setStatus("mandatory")


class _IbmappnNnNodeIsrDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeIsrDepleted based on Integer32"""
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


_IbmappnNnNodeIsrDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeIsrDepleted_Object = MibTableColumn
ibmappnNnNodeIsrDepleted = _IbmappnNnNodeIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 8),
    _IbmappnNnNodeIsrDepleted_Type()
)
ibmappnNnNodeIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeIsrDepleted.setStatus("mandatory")


class _IbmappnNnNodeEndptDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeEndptDepleted based on Integer32"""
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


_IbmappnNnNodeEndptDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeEndptDepleted_Object = MibTableColumn
ibmappnNnNodeEndptDepleted = _IbmappnNnNodeEndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 9),
    _IbmappnNnNodeEndptDepleted_Type()
)
ibmappnNnNodeEndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeEndptDepleted.setStatus("mandatory")


class _IbmappnNnNodeQuiescing_Type(Integer32):
    """Custom type ibmappnNnNodeQuiescing based on Integer32"""
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


_IbmappnNnNodeQuiescing_Type.__name__ = "Integer32"
_IbmappnNnNodeQuiescing_Object = MibTableColumn
ibmappnNnNodeQuiescing = _IbmappnNnNodeQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 10),
    _IbmappnNnNodeQuiescing_Type()
)
ibmappnNnNodeQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeQuiescing.setStatus("mandatory")


class _IbmappnNnNodeGateway_Type(Integer32):
    """Custom type ibmappnNnNodeGateway based on Integer32"""
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


_IbmappnNnNodeGateway_Type.__name__ = "Integer32"
_IbmappnNnNodeGateway_Object = MibTableColumn
ibmappnNnNodeGateway = _IbmappnNnNodeGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 11),
    _IbmappnNnNodeGateway_Type()
)
ibmappnNnNodeGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeGateway.setStatus("mandatory")


class _IbmappnNnNodeCentralDirectory_Type(Integer32):
    """Custom type ibmappnNnNodeCentralDirectory based on Integer32"""
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


_IbmappnNnNodeCentralDirectory_Type.__name__ = "Integer32"
_IbmappnNnNodeCentralDirectory_Object = MibTableColumn
ibmappnNnNodeCentralDirectory = _IbmappnNnNodeCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 12),
    _IbmappnNnNodeCentralDirectory_Type()
)
ibmappnNnNodeCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeCentralDirectory.setStatus("mandatory")


class _IbmappnNnNodeIsr_Type(Integer32):
    """Custom type ibmappnNnNodeIsr based on Integer32"""
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


_IbmappnNnNodeIsr_Type.__name__ = "Integer32"
_IbmappnNnNodeIsr_Object = MibTableColumn
ibmappnNnNodeIsr = _IbmappnNnNodeIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 13),
    _IbmappnNnNodeIsr_Type()
)
ibmappnNnNodeIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeIsr.setStatus("mandatory")


class _IbmappnNnNodeChainSupport_Type(Integer32):
    """Custom type ibmappnNnNodeChainSupport based on Integer32"""
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


_IbmappnNnNodeChainSupport_Type.__name__ = "Integer32"
_IbmappnNnNodeChainSupport_Object = MibTableColumn
ibmappnNnNodeChainSupport = _IbmappnNnNodeChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 1, 1, 14),
    _IbmappnNnNodeChainSupport_Type()
)
ibmappnNnNodeChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeChainSupport.setStatus("mandatory")
_IbmappnNnTgTopologyTable_Object = MibTable
ibmappnNnTgTopologyTable = _IbmappnNnTgTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2)
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyTable.setStatus("mandatory")
_IbmappnNnTgTopologyEntry_Object = MibTableRow
ibmappnNnTgTopologyEntry = _IbmappnNnTgTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1)
)
ibmappnNnTgTopologyEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTgOwner"),
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTgDest"),
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTgNum"),
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyEntry.setStatus("mandatory")


class _IbmappnNnTgOwner_Type(DisplayString):
    """Custom type ibmappnNnTgOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgOwner_Type.__name__ = "DisplayString"
_IbmappnNnTgOwner_Object = MibTableColumn
ibmappnNnTgOwner = _IbmappnNnTgOwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 1),
    _IbmappnNnTgOwner_Type()
)
ibmappnNnTgOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgOwner.setStatus("mandatory")


class _IbmappnNnTgDest_Type(DisplayString):
    """Custom type ibmappnNnTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgDest_Type.__name__ = "DisplayString"
_IbmappnNnTgDest_Object = MibTableColumn
ibmappnNnTgDest = _IbmappnNnTgDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 2),
    _IbmappnNnTgDest_Type()
)
ibmappnNnTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDest.setStatus("mandatory")


class _IbmappnNnTgNum_Type(Integer32):
    """Custom type ibmappnNnTgNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgNum_Type.__name__ = "Integer32"
_IbmappnNnTgNum_Object = MibTableColumn
ibmappnNnTgNum = _IbmappnNnTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 3),
    _IbmappnNnTgNum_Type()
)
ibmappnNnTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgNum.setStatus("mandatory")


class _IbmappnNnTgFrsn_Type(Integer32):
    """Custom type ibmappnNnTgFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgFrsn_Type.__name__ = "Integer32"
_IbmappnNnTgFrsn_Object = MibTableColumn
ibmappnNnTgFrsn = _IbmappnNnTgFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 4),
    _IbmappnNnTgFrsn_Type()
)
ibmappnNnTgFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFrsn.setStatus("mandatory")


class _IbmappnNnTgEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnTgEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnTgEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnTgEntryTimeLeft_Object = MibTableColumn
ibmappnNnTgEntryTimeLeft = _IbmappnNnTgEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 5),
    _IbmappnNnTgEntryTimeLeft_Type()
)
ibmappnNnTgEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgEntryTimeLeft.setStatus("mandatory")


class _IbmappnNnTgDestVirtual_Type(Integer32):
    """Custom type ibmappnNnTgDestVirtual based on Integer32"""
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


_IbmappnNnTgDestVirtual_Type.__name__ = "Integer32"
_IbmappnNnTgDestVirtual_Object = MibTableColumn
ibmappnNnTgDestVirtual = _IbmappnNnTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 6),
    _IbmappnNnTgDestVirtual_Type()
)
ibmappnNnTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDestVirtual.setStatus("mandatory")


class _IbmappnNnTgDlcData_Type(OctetString):
    """Custom type ibmappnNnTgDlcData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_IbmappnNnTgDlcData_Type.__name__ = "OctetString"
_IbmappnNnTgDlcData_Object = MibTableColumn
ibmappnNnTgDlcData = _IbmappnNnTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 7),
    _IbmappnNnTgDlcData_Type()
)
ibmappnNnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDlcData.setStatus("mandatory")
_IbmappnNnTgRsn_Type = Integer32
_IbmappnNnTgRsn_Object = MibTableColumn
ibmappnNnTgRsn = _IbmappnNnTgRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 8),
    _IbmappnNnTgRsn_Type()
)
ibmappnNnTgRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgRsn.setStatus("mandatory")


class _IbmappnNnTgOperational_Type(Integer32):
    """Custom type ibmappnNnTgOperational based on Integer32"""
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


_IbmappnNnTgOperational_Type.__name__ = "Integer32"
_IbmappnNnTgOperational_Object = MibTableColumn
ibmappnNnTgOperational = _IbmappnNnTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 9),
    _IbmappnNnTgOperational_Type()
)
ibmappnNnTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgOperational.setStatus("mandatory")


class _IbmappnNnTgQuiescing_Type(Integer32):
    """Custom type ibmappnNnTgQuiescing based on Integer32"""
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


_IbmappnNnTgQuiescing_Type.__name__ = "Integer32"
_IbmappnNnTgQuiescing_Object = MibTableColumn
ibmappnNnTgQuiescing = _IbmappnNnTgQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 10),
    _IbmappnNnTgQuiescing_Type()
)
ibmappnNnTgQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgQuiescing.setStatus("mandatory")


class _IbmappnNnTgCpCpSession_Type(Integer32):
    """Custom type ibmappnNnTgCpCpSession based on Integer32"""
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


_IbmappnNnTgCpCpSession_Type.__name__ = "Integer32"
_IbmappnNnTgCpCpSession_Object = MibTableColumn
ibmappnNnTgCpCpSession = _IbmappnNnTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 11),
    _IbmappnNnTgCpCpSession_Type()
)
ibmappnNnTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgCpCpSession.setStatus("mandatory")
_IbmappnNnTgEffCap_Type = Integer32
_IbmappnNnTgEffCap_Object = MibTableColumn
ibmappnNnTgEffCap = _IbmappnNnTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 12),
    _IbmappnNnTgEffCap_Type()
)
ibmappnNnTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgEffCap.setStatus("mandatory")


class _IbmappnNnTgConnCost_Type(Integer32):
    """Custom type ibmappnNnTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgConnCost_Type.__name__ = "Integer32"
_IbmappnNnTgConnCost_Object = MibTableColumn
ibmappnNnTgConnCost = _IbmappnNnTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 13),
    _IbmappnNnTgConnCost_Type()
)
ibmappnNnTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgConnCost.setStatus("mandatory")


class _IbmappnNnTgByteCost_Type(Integer32):
    """Custom type ibmappnNnTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgByteCost_Type.__name__ = "Integer32"
_IbmappnNnTgByteCost_Object = MibTableColumn
ibmappnNnTgByteCost = _IbmappnNnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 14),
    _IbmappnNnTgByteCost_Type()
)
ibmappnNnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgByteCost.setStatus("mandatory")


class _IbmappnNnTgSecurity_Type(Integer32):
    """Custom type ibmappnNnTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnNnTgSecurity_Type.__name__ = "Integer32"
_IbmappnNnTgSecurity_Object = MibTableColumn
ibmappnNnTgSecurity = _IbmappnNnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 15),
    _IbmappnNnTgSecurity_Type()
)
ibmappnNnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgSecurity.setStatus("mandatory")


class _IbmappnNnTgDelay_Type(Integer32):
    """Custom type ibmappnNnTgDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnNnTgDelay_Type.__name__ = "Integer32"
_IbmappnNnTgDelay_Object = MibTableColumn
ibmappnNnTgDelay = _IbmappnNnTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 16),
    _IbmappnNnTgDelay_Type()
)
ibmappnNnTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgDelay.setStatus("mandatory")


class _IbmappnNnTgModemClass_Type(Integer32):
    """Custom type ibmappnNnTgModemClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgModemClass_Type.__name__ = "Integer32"
_IbmappnNnTgModemClass_Object = MibTableColumn
ibmappnNnTgModemClass = _IbmappnNnTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 17),
    _IbmappnNnTgModemClass_Type()
)
ibmappnNnTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgModemClass.setStatus("mandatory")


class _IbmappnNnTgUsr1_Type(Integer32):
    """Custom type ibmappnNnTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgUsr1_Type.__name__ = "Integer32"
_IbmappnNnTgUsr1_Object = MibTableColumn
ibmappnNnTgUsr1 = _IbmappnNnTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 18),
    _IbmappnNnTgUsr1_Type()
)
ibmappnNnTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgUsr1.setStatus("mandatory")


class _IbmappnNnTgUsr2_Type(Integer32):
    """Custom type ibmappnNnTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgUsr2_Type.__name__ = "Integer32"
_IbmappnNnTgUsr2_Object = MibTableColumn
ibmappnNnTgUsr2 = _IbmappnNnTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 19),
    _IbmappnNnTgUsr2_Type()
)
ibmappnNnTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgUsr2.setStatus("mandatory")


class _IbmappnNnTgUsr3_Type(Integer32):
    """Custom type ibmappnNnTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgUsr3_Type.__name__ = "Integer32"
_IbmappnNnTgUsr3_Object = MibTableColumn
ibmappnNnTgUsr3 = _IbmappnNnTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 2, 1, 20),
    _IbmappnNnTgUsr3_Type()
)
ibmappnNnTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgUsr3.setStatus("mandatory")
_IbmappnNnTopologyFRTable_Object = MibTable
ibmappnNnTopologyFRTable = _IbmappnNnTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3)
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyFRTable.setStatus("mandatory")
_IbmappnNnTopologyFREntry_Object = MibTableRow
ibmappnNnTopologyFREntry = _IbmappnNnTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1)
)
ibmappnNnTopologyFREntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNnNodeFRFrsn"),
    (0, "IBM-6611-APPN-MIB", "ibmappnNnNodeFRName"),
)
if mibBuilder.loadTexts:
    ibmappnNnTopologyFREntry.setStatus("mandatory")


class _IbmappnNnNodeFRName_Type(DisplayString):
    """Custom type ibmappnNnNodeFRName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnNodeFRName_Type.__name__ = "DisplayString"
_IbmappnNnNodeFRName_Object = MibTableColumn
ibmappnNnNodeFRName = _IbmappnNnNodeFRName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 1),
    _IbmappnNnNodeFRName_Type()
)
ibmappnNnNodeFRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRName.setStatus("mandatory")


class _IbmappnNnNodeFRFrsn_Type(Integer32):
    """Custom type ibmappnNnNodeFRFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnNodeFRFrsn_Type.__name__ = "Integer32"
_IbmappnNnNodeFRFrsn_Object = MibTableColumn
ibmappnNnNodeFRFrsn = _IbmappnNnNodeFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 2),
    _IbmappnNnNodeFRFrsn_Type()
)
ibmappnNnNodeFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRFrsn.setStatus("mandatory")


class _IbmappnNnNodeFREntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnNodeFREntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnNodeFREntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnNodeFREntryTimeLeft_Object = MibTableColumn
ibmappnNnNodeFREntryTimeLeft = _IbmappnNnNodeFREntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 3),
    _IbmappnNnNodeFREntryTimeLeft_Type()
)
ibmappnNnNodeFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFREntryTimeLeft.setStatus("mandatory")


class _IbmappnNnNodeFRType_Type(Integer32):
    """Custom type ibmappnNnNodeFRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networknode", 1),
          ("virtualnode", 3))
    )


_IbmappnNnNodeFRType_Type.__name__ = "Integer32"
_IbmappnNnNodeFRType_Object = MibTableColumn
ibmappnNnNodeFRType = _IbmappnNnNodeFRType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 4),
    _IbmappnNnNodeFRType_Type()
)
ibmappnNnNodeFRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRType.setStatus("mandatory")
_IbmappnNnNodeFRRsn_Type = Integer32
_IbmappnNnNodeFRRsn_Object = MibTableColumn
ibmappnNnNodeFRRsn = _IbmappnNnNodeFRRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 5),
    _IbmappnNnNodeFRRsn_Type()
)
ibmappnNnNodeFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRRsn.setStatus("mandatory")
_IbmappnNnNodeFRRouteAddResist_Type = Integer32
_IbmappnNnNodeFRRouteAddResist_Object = MibTableColumn
ibmappnNnNodeFRRouteAddResist = _IbmappnNnNodeFRRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 6),
    _IbmappnNnNodeFRRouteAddResist_Type()
)
ibmappnNnNodeFRRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRRouteAddResist.setStatus("mandatory")


class _IbmappnNnNodeFRCongested_Type(Integer32):
    """Custom type ibmappnNnNodeFRCongested based on Integer32"""
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


_IbmappnNnNodeFRCongested_Type.__name__ = "Integer32"
_IbmappnNnNodeFRCongested_Object = MibTableColumn
ibmappnNnNodeFRCongested = _IbmappnNnNodeFRCongested_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 7),
    _IbmappnNnNodeFRCongested_Type()
)
ibmappnNnNodeFRCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRCongested.setStatus("mandatory")


class _IbmappnNnNodeFRIsrDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeFRIsrDepleted based on Integer32"""
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


_IbmappnNnNodeFRIsrDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeFRIsrDepleted_Object = MibTableColumn
ibmappnNnNodeFRIsrDepleted = _IbmappnNnNodeFRIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 8),
    _IbmappnNnNodeFRIsrDepleted_Type()
)
ibmappnNnNodeFRIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRIsrDepleted.setStatus("mandatory")


class _IbmappnNnNodeFREndptDepleted_Type(Integer32):
    """Custom type ibmappnNnNodeFREndptDepleted based on Integer32"""
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


_IbmappnNnNodeFREndptDepleted_Type.__name__ = "Integer32"
_IbmappnNnNodeFREndptDepleted_Object = MibTableColumn
ibmappnNnNodeFREndptDepleted = _IbmappnNnNodeFREndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 9),
    _IbmappnNnNodeFREndptDepleted_Type()
)
ibmappnNnNodeFREndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFREndptDepleted.setStatus("mandatory")


class _IbmappnNnNodeFRQuiescing_Type(Integer32):
    """Custom type ibmappnNnNodeFRQuiescing based on Integer32"""
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


_IbmappnNnNodeFRQuiescing_Type.__name__ = "Integer32"
_IbmappnNnNodeFRQuiescing_Object = MibTableColumn
ibmappnNnNodeFRQuiescing = _IbmappnNnNodeFRQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 10),
    _IbmappnNnNodeFRQuiescing_Type()
)
ibmappnNnNodeFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRQuiescing.setStatus("mandatory")


class _IbmappnNnNodeFRGateway_Type(Integer32):
    """Custom type ibmappnNnNodeFRGateway based on Integer32"""
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


_IbmappnNnNodeFRGateway_Type.__name__ = "Integer32"
_IbmappnNnNodeFRGateway_Object = MibTableColumn
ibmappnNnNodeFRGateway = _IbmappnNnNodeFRGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 11),
    _IbmappnNnNodeFRGateway_Type()
)
ibmappnNnNodeFRGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRGateway.setStatus("mandatory")


class _IbmappnNnNodeFRCentralDirectory_Type(Integer32):
    """Custom type ibmappnNnNodeFRCentralDirectory based on Integer32"""
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


_IbmappnNnNodeFRCentralDirectory_Type.__name__ = "Integer32"
_IbmappnNnNodeFRCentralDirectory_Object = MibTableColumn
ibmappnNnNodeFRCentralDirectory = _IbmappnNnNodeFRCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 12),
    _IbmappnNnNodeFRCentralDirectory_Type()
)
ibmappnNnNodeFRCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRCentralDirectory.setStatus("mandatory")


class _IbmappnNnNodeFRIsr_Type(Integer32):
    """Custom type ibmappnNnNodeFRIsr based on Integer32"""
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


_IbmappnNnNodeFRIsr_Type.__name__ = "Integer32"
_IbmappnNnNodeFRIsr_Object = MibTableColumn
ibmappnNnNodeFRIsr = _IbmappnNnNodeFRIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 13),
    _IbmappnNnNodeFRIsr_Type()
)
ibmappnNnNodeFRIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRIsr.setStatus("mandatory")


class _IbmappnNnNodeFRChainSupport_Type(Integer32):
    """Custom type ibmappnNnNodeFRChainSupport based on Integer32"""
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


_IbmappnNnNodeFRChainSupport_Type.__name__ = "Integer32"
_IbmappnNnNodeFRChainSupport_Object = MibTableColumn
ibmappnNnNodeFRChainSupport = _IbmappnNnNodeFRChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 3, 1, 14),
    _IbmappnNnNodeFRChainSupport_Type()
)
ibmappnNnNodeFRChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnNodeFRChainSupport.setStatus("mandatory")
_IbmappnNnTgTopologyFRTable_Object = MibTable
ibmappnNnTgTopologyFRTable = _IbmappnNnTgTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4)
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyFRTable.setStatus("mandatory")
_IbmappnNnTgTopologyFREntry_Object = MibTableRow
ibmappnNnTgTopologyFREntry = _IbmappnNnTgTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1)
)
ibmappnNnTgTopologyFREntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTgFRFrsn"),
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTgFROwner"),
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTgFRDest"),
    (0, "IBM-6611-APPN-MIB", "ibmappnNnTgFRNum"),
)
if mibBuilder.loadTexts:
    ibmappnNnTgTopologyFREntry.setStatus("mandatory")


class _IbmappnNnTgFROwner_Type(DisplayString):
    """Custom type ibmappnNnTgFROwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgFROwner_Type.__name__ = "DisplayString"
_IbmappnNnTgFROwner_Object = MibTableColumn
ibmappnNnTgFROwner = _IbmappnNnTgFROwner_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 1),
    _IbmappnNnTgFROwner_Type()
)
ibmappnNnTgFROwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFROwner.setStatus("mandatory")


class _IbmappnNnTgFRDest_Type(DisplayString):
    """Custom type ibmappnNnTgFRDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnNnTgFRDest_Type.__name__ = "DisplayString"
_IbmappnNnTgFRDest_Object = MibTableColumn
ibmappnNnTgFRDest = _IbmappnNnTgFRDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 2),
    _IbmappnNnTgFRDest_Type()
)
ibmappnNnTgFRDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDest.setStatus("mandatory")


class _IbmappnNnTgFRNum_Type(Integer32):
    """Custom type ibmappnNnTgFRNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRNum_Type.__name__ = "Integer32"
_IbmappnNnTgFRNum_Object = MibTableColumn
ibmappnNnTgFRNum = _IbmappnNnTgFRNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 3),
    _IbmappnNnTgFRNum_Type()
)
ibmappnNnTgFRNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRNum.setStatus("mandatory")


class _IbmappnNnTgFRFrsn_Type(Integer32):
    """Custom type ibmappnNnTgFRFrsn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgFRFrsn_Type.__name__ = "Integer32"
_IbmappnNnTgFRFrsn_Object = MibTableColumn
ibmappnNnTgFRFrsn = _IbmappnNnTgFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 4),
    _IbmappnNnTgFRFrsn_Type()
)
ibmappnNnTgFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRFrsn.setStatus("mandatory")


class _IbmappnNnTgFREntryTimeLeft_Type(Integer32):
    """Custom type ibmappnNnTgFREntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnNnTgFREntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnNnTgFREntryTimeLeft_Object = MibTableColumn
ibmappnNnTgFREntryTimeLeft = _IbmappnNnTgFREntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 5),
    _IbmappnNnTgFREntryTimeLeft_Type()
)
ibmappnNnTgFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFREntryTimeLeft.setStatus("mandatory")


class _IbmappnNnTgFRDestVirtual_Type(Integer32):
    """Custom type ibmappnNnTgFRDestVirtual based on Integer32"""
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


_IbmappnNnTgFRDestVirtual_Type.__name__ = "Integer32"
_IbmappnNnTgFRDestVirtual_Object = MibTableColumn
ibmappnNnTgFRDestVirtual = _IbmappnNnTgFRDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 6),
    _IbmappnNnTgFRDestVirtual_Type()
)
ibmappnNnTgFRDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDestVirtual.setStatus("mandatory")


class _IbmappnNnTgFRDlcData_Type(OctetString):
    """Custom type ibmappnNnTgFRDlcData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_IbmappnNnTgFRDlcData_Type.__name__ = "OctetString"
_IbmappnNnTgFRDlcData_Object = MibTableColumn
ibmappnNnTgFRDlcData = _IbmappnNnTgFRDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 7),
    _IbmappnNnTgFRDlcData_Type()
)
ibmappnNnTgFRDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDlcData.setStatus("mandatory")
_IbmappnNnTgFRRsn_Type = Integer32
_IbmappnNnTgFRRsn_Object = MibTableColumn
ibmappnNnTgFRRsn = _IbmappnNnTgFRRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 8),
    _IbmappnNnTgFRRsn_Type()
)
ibmappnNnTgFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRRsn.setStatus("mandatory")


class _IbmappnNnTgFROperational_Type(Integer32):
    """Custom type ibmappnNnTgFROperational based on Integer32"""
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


_IbmappnNnTgFROperational_Type.__name__ = "Integer32"
_IbmappnNnTgFROperational_Object = MibTableColumn
ibmappnNnTgFROperational = _IbmappnNnTgFROperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 9),
    _IbmappnNnTgFROperational_Type()
)
ibmappnNnTgFROperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFROperational.setStatus("mandatory")


class _IbmappnNnTgFRQuiescing_Type(Integer32):
    """Custom type ibmappnNnTgFRQuiescing based on Integer32"""
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


_IbmappnNnTgFRQuiescing_Type.__name__ = "Integer32"
_IbmappnNnTgFRQuiescing_Object = MibTableColumn
ibmappnNnTgFRQuiescing = _IbmappnNnTgFRQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 10),
    _IbmappnNnTgFRQuiescing_Type()
)
ibmappnNnTgFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRQuiescing.setStatus("mandatory")


class _IbmappnNnTgFRCpCpSession_Type(Integer32):
    """Custom type ibmappnNnTgFRCpCpSession based on Integer32"""
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


_IbmappnNnTgFRCpCpSession_Type.__name__ = "Integer32"
_IbmappnNnTgFRCpCpSession_Object = MibTableColumn
ibmappnNnTgFRCpCpSession = _IbmappnNnTgFRCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 11),
    _IbmappnNnTgFRCpCpSession_Type()
)
ibmappnNnTgFRCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRCpCpSession.setStatus("mandatory")
_IbmappnNnTgFREffCap_Type = Integer32
_IbmappnNnTgFREffCap_Object = MibTableColumn
ibmappnNnTgFREffCap = _IbmappnNnTgFREffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 12),
    _IbmappnNnTgFREffCap_Type()
)
ibmappnNnTgFREffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFREffCap.setStatus("mandatory")


class _IbmappnNnTgFRConnCost_Type(Integer32):
    """Custom type ibmappnNnTgFRConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRConnCost_Type.__name__ = "Integer32"
_IbmappnNnTgFRConnCost_Object = MibTableColumn
ibmappnNnTgFRConnCost = _IbmappnNnTgFRConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 13),
    _IbmappnNnTgFRConnCost_Type()
)
ibmappnNnTgFRConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRConnCost.setStatus("mandatory")


class _IbmappnNnTgFRByteCost_Type(Integer32):
    """Custom type ibmappnNnTgFRByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRByteCost_Type.__name__ = "Integer32"
_IbmappnNnTgFRByteCost_Object = MibTableColumn
ibmappnNnTgFRByteCost = _IbmappnNnTgFRByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 14),
    _IbmappnNnTgFRByteCost_Type()
)
ibmappnNnTgFRByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRByteCost.setStatus("mandatory")


class _IbmappnNnTgFRSecurity_Type(Integer32):
    """Custom type ibmappnNnTgFRSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnNnTgFRSecurity_Type.__name__ = "Integer32"
_IbmappnNnTgFRSecurity_Object = MibTableColumn
ibmappnNnTgFRSecurity = _IbmappnNnTgFRSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 15),
    _IbmappnNnTgFRSecurity_Type()
)
ibmappnNnTgFRSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRSecurity.setStatus("mandatory")


class _IbmappnNnTgFRDelay_Type(Integer32):
    """Custom type ibmappnNnTgFRDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnNnTgFRDelay_Type.__name__ = "Integer32"
_IbmappnNnTgFRDelay_Object = MibTableColumn
ibmappnNnTgFRDelay = _IbmappnNnTgFRDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 16),
    _IbmappnNnTgFRDelay_Type()
)
ibmappnNnTgFRDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRDelay.setStatus("mandatory")


class _IbmappnNnTgFRModemClass_Type(Integer32):
    """Custom type ibmappnNnTgFRModemClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnNnTgFRModemClass_Type.__name__ = "Integer32"
_IbmappnNnTgFRModemClass_Object = MibTableColumn
ibmappnNnTgFRModemClass = _IbmappnNnTgFRModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 17),
    _IbmappnNnTgFRModemClass_Type()
)
ibmappnNnTgFRModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRModemClass.setStatus("mandatory")


class _IbmappnNnTgFRUsr1_Type(Integer32):
    """Custom type ibmappnNnTgFRUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRUsr1_Type.__name__ = "Integer32"
_IbmappnNnTgFRUsr1_Object = MibTableColumn
ibmappnNnTgFRUsr1 = _IbmappnNnTgFRUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 18),
    _IbmappnNnTgFRUsr1_Type()
)
ibmappnNnTgFRUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRUsr1.setStatus("mandatory")


class _IbmappnNnTgFRUsr2_Type(Integer32):
    """Custom type ibmappnNnTgFRUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRUsr2_Type.__name__ = "Integer32"
_IbmappnNnTgFRUsr2_Object = MibTableColumn
ibmappnNnTgFRUsr2 = _IbmappnNnTgFRUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 19),
    _IbmappnNnTgFRUsr2_Type()
)
ibmappnNnTgFRUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRUsr2.setStatus("mandatory")


class _IbmappnNnTgFRUsr3_Type(Integer32):
    """Custom type ibmappnNnTgFRUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnNnTgFRUsr3_Type.__name__ = "Integer32"
_IbmappnNnTgFRUsr3_Object = MibTableColumn
ibmappnNnTgFRUsr3 = _IbmappnNnTgFRUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 2, 3, 4, 1, 20),
    _IbmappnNnTgFRUsr3_Type()
)
ibmappnNnTgFRUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnNnTgFRUsr3.setStatus("mandatory")
_IbmappnLocalTopology_ObjectIdentity = ObjectIdentity
ibmappnLocalTopology = _IbmappnLocalTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3)
)
_IbmappnLocalThisNode_ObjectIdentity = ObjectIdentity
ibmappnLocalThisNode = _IbmappnLocalThisNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1)
)
_IbmappnLocalGeneral_ObjectIdentity = ObjectIdentity
ibmappnLocalGeneral = _IbmappnLocalGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 1)
)


class _IbmappnLocalNodeName_Type(DisplayString):
    """Custom type ibmappnLocalNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalNodeName_Type.__name__ = "DisplayString"
_IbmappnLocalNodeName_Object = MibScalar
ibmappnLocalNodeName = _IbmappnLocalNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 1, 1),
    _IbmappnLocalNodeName_Type()
)
ibmappnLocalNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNodeName.setStatus("mandatory")


class _IbmappnLocalNodeType_Type(Integer32):
    """Custom type ibmappnLocalNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endnode", 2),
          ("len", 4),
          ("networknode", 1))
    )


_IbmappnLocalNodeType_Type.__name__ = "Integer32"
_IbmappnLocalNodeType_Object = MibScalar
ibmappnLocalNodeType = _IbmappnLocalNodeType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 1, 2),
    _IbmappnLocalNodeType_Type()
)
ibmappnLocalNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNodeType.setStatus("mandatory")
_IbmappnLocalNnSpecific_ObjectIdentity = ObjectIdentity
ibmappnLocalNnSpecific = _IbmappnLocalNnSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2)
)
_IbmappnLocalNnRsn_Type = Integer32
_IbmappnLocalNnRsn_Object = MibScalar
ibmappnLocalNnRsn = _IbmappnLocalNnRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 1),
    _IbmappnLocalNnRsn_Type()
)
ibmappnLocalNnRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnRsn.setStatus("mandatory")
_IbmappnLocalNnRouteAddResist_Type = Integer32
_IbmappnLocalNnRouteAddResist_Object = MibScalar
ibmappnLocalNnRouteAddResist = _IbmappnLocalNnRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 2),
    _IbmappnLocalNnRouteAddResist_Type()
)
ibmappnLocalNnRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnRouteAddResist.setStatus("mandatory")


class _IbmappnLocalNnCongested_Type(Integer32):
    """Custom type ibmappnLocalNnCongested based on Integer32"""
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


_IbmappnLocalNnCongested_Type.__name__ = "Integer32"
_IbmappnLocalNnCongested_Object = MibScalar
ibmappnLocalNnCongested = _IbmappnLocalNnCongested_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 3),
    _IbmappnLocalNnCongested_Type()
)
ibmappnLocalNnCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnCongested.setStatus("mandatory")


class _IbmappnLocalNnIsrDepleted_Type(Integer32):
    """Custom type ibmappnLocalNnIsrDepleted based on Integer32"""
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


_IbmappnLocalNnIsrDepleted_Type.__name__ = "Integer32"
_IbmappnLocalNnIsrDepleted_Object = MibScalar
ibmappnLocalNnIsrDepleted = _IbmappnLocalNnIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 4),
    _IbmappnLocalNnIsrDepleted_Type()
)
ibmappnLocalNnIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnIsrDepleted.setStatus("mandatory")


class _IbmappnLocalNnEndptDepleted_Type(Integer32):
    """Custom type ibmappnLocalNnEndptDepleted based on Integer32"""
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


_IbmappnLocalNnEndptDepleted_Type.__name__ = "Integer32"
_IbmappnLocalNnEndptDepleted_Object = MibScalar
ibmappnLocalNnEndptDepleted = _IbmappnLocalNnEndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 5),
    _IbmappnLocalNnEndptDepleted_Type()
)
ibmappnLocalNnEndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnEndptDepleted.setStatus("mandatory")


class _IbmappnLocalNnQuiescing_Type(Integer32):
    """Custom type ibmappnLocalNnQuiescing based on Integer32"""
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


_IbmappnLocalNnQuiescing_Type.__name__ = "Integer32"
_IbmappnLocalNnQuiescing_Object = MibScalar
ibmappnLocalNnQuiescing = _IbmappnLocalNnQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 6),
    _IbmappnLocalNnQuiescing_Type()
)
ibmappnLocalNnQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnQuiescing.setStatus("mandatory")


class _IbmappnLocalNnGateway_Type(Integer32):
    """Custom type ibmappnLocalNnGateway based on Integer32"""
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


_IbmappnLocalNnGateway_Type.__name__ = "Integer32"
_IbmappnLocalNnGateway_Object = MibScalar
ibmappnLocalNnGateway = _IbmappnLocalNnGateway_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 7),
    _IbmappnLocalNnGateway_Type()
)
ibmappnLocalNnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnGateway.setStatus("mandatory")


class _IbmappnLocalNnCentralDirectory_Type(Integer32):
    """Custom type ibmappnLocalNnCentralDirectory based on Integer32"""
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


_IbmappnLocalNnCentralDirectory_Type.__name__ = "Integer32"
_IbmappnLocalNnCentralDirectory_Object = MibScalar
ibmappnLocalNnCentralDirectory = _IbmappnLocalNnCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 8),
    _IbmappnLocalNnCentralDirectory_Type()
)
ibmappnLocalNnCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnCentralDirectory.setStatus("mandatory")


class _IbmappnLocalNnIsr_Type(Integer32):
    """Custom type ibmappnLocalNnIsr based on Integer32"""
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


_IbmappnLocalNnIsr_Type.__name__ = "Integer32"
_IbmappnLocalNnIsr_Object = MibScalar
ibmappnLocalNnIsr = _IbmappnLocalNnIsr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 9),
    _IbmappnLocalNnIsr_Type()
)
ibmappnLocalNnIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnIsr.setStatus("mandatory")


class _IbmappnLocalNnChainSupport_Type(Integer32):
    """Custom type ibmappnLocalNnChainSupport based on Integer32"""
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


_IbmappnLocalNnChainSupport_Type.__name__ = "Integer32"
_IbmappnLocalNnChainSupport_Object = MibScalar
ibmappnLocalNnChainSupport = _IbmappnLocalNnChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 10),
    _IbmappnLocalNnChainSupport_Type()
)
ibmappnLocalNnChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnChainSupport.setStatus("mandatory")
_IbmappnLocalNnFrsn_Type = Integer32
_IbmappnLocalNnFrsn_Object = MibScalar
ibmappnLocalNnFrsn = _IbmappnLocalNnFrsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 2, 11),
    _IbmappnLocalNnFrsn_Type()
)
ibmappnLocalNnFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalNnFrsn.setStatus("mandatory")
_IbmappnLocalTg_ObjectIdentity = ObjectIdentity
ibmappnLocalTg = _IbmappnLocalTg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3)
)
_IbmappnLocalTgTable_Object = MibTable
ibmappnLocalTgTable = _IbmappnLocalTgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ibmappnLocalTgTable.setStatus("mandatory")
_IbmappnLocalTgEntry_Object = MibTableRow
ibmappnLocalTgEntry = _IbmappnLocalTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1)
)
ibmappnLocalTgEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnLocalTgDest"),
    (0, "IBM-6611-APPN-MIB", "ibmappnLocalTgNum"),
)
if mibBuilder.loadTexts:
    ibmappnLocalTgEntry.setStatus("mandatory")


class _IbmappnLocalTgDest_Type(DisplayString):
    """Custom type ibmappnLocalTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalTgDest_Type.__name__ = "DisplayString"
_IbmappnLocalTgDest_Object = MibTableColumn
ibmappnLocalTgDest = _IbmappnLocalTgDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 1),
    _IbmappnLocalTgDest_Type()
)
ibmappnLocalTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDest.setStatus("mandatory")
_IbmappnLocalTgNum_Type = Integer32
_IbmappnLocalTgNum_Object = MibTableColumn
ibmappnLocalTgNum = _IbmappnLocalTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 2),
    _IbmappnLocalTgNum_Type()
)
ibmappnLocalTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgNum.setStatus("mandatory")


class _IbmappnLocalTgDestVirtual_Type(Integer32):
    """Custom type ibmappnLocalTgDestVirtual based on Integer32"""
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


_IbmappnLocalTgDestVirtual_Type.__name__ = "Integer32"
_IbmappnLocalTgDestVirtual_Object = MibTableColumn
ibmappnLocalTgDestVirtual = _IbmappnLocalTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 3),
    _IbmappnLocalTgDestVirtual_Type()
)
ibmappnLocalTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDestVirtual.setStatus("mandatory")


class _IbmappnLocalTgDlcData_Type(OctetString):
    """Custom type ibmappnLocalTgDlcData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_IbmappnLocalTgDlcData_Type.__name__ = "OctetString"
_IbmappnLocalTgDlcData_Object = MibTableColumn
ibmappnLocalTgDlcData = _IbmappnLocalTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 4),
    _IbmappnLocalTgDlcData_Type()
)
ibmappnLocalTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDlcData.setStatus("mandatory")
_IbmappnLocalTgRsn_Type = Integer32
_IbmappnLocalTgRsn_Object = MibTableColumn
ibmappnLocalTgRsn = _IbmappnLocalTgRsn_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 5),
    _IbmappnLocalTgRsn_Type()
)
ibmappnLocalTgRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgRsn.setStatus("mandatory")


class _IbmappnLocalTgQuiescing_Type(Integer32):
    """Custom type ibmappnLocalTgQuiescing based on Integer32"""
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


_IbmappnLocalTgQuiescing_Type.__name__ = "Integer32"
_IbmappnLocalTgQuiescing_Object = MibTableColumn
ibmappnLocalTgQuiescing = _IbmappnLocalTgQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 6),
    _IbmappnLocalTgQuiescing_Type()
)
ibmappnLocalTgQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgQuiescing.setStatus("mandatory")


class _IbmappnLocalTgOperational_Type(Integer32):
    """Custom type ibmappnLocalTgOperational based on Integer32"""
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


_IbmappnLocalTgOperational_Type.__name__ = "Integer32"
_IbmappnLocalTgOperational_Object = MibTableColumn
ibmappnLocalTgOperational = _IbmappnLocalTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 7),
    _IbmappnLocalTgOperational_Type()
)
ibmappnLocalTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgOperational.setStatus("mandatory")


class _IbmappnLocalTgCpCpSession_Type(Integer32):
    """Custom type ibmappnLocalTgCpCpSession based on Integer32"""
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


_IbmappnLocalTgCpCpSession_Type.__name__ = "Integer32"
_IbmappnLocalTgCpCpSession_Object = MibTableColumn
ibmappnLocalTgCpCpSession = _IbmappnLocalTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 8),
    _IbmappnLocalTgCpCpSession_Type()
)
ibmappnLocalTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgCpCpSession.setStatus("mandatory")
_IbmappnLocalTgEffCap_Type = Integer32
_IbmappnLocalTgEffCap_Object = MibTableColumn
ibmappnLocalTgEffCap = _IbmappnLocalTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 9),
    _IbmappnLocalTgEffCap_Type()
)
ibmappnLocalTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgEffCap.setStatus("mandatory")


class _IbmappnLocalTgConnCost_Type(Integer32):
    """Custom type ibmappnLocalTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgConnCost_Type.__name__ = "Integer32"
_IbmappnLocalTgConnCost_Object = MibTableColumn
ibmappnLocalTgConnCost = _IbmappnLocalTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 10),
    _IbmappnLocalTgConnCost_Type()
)
ibmappnLocalTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgConnCost.setStatus("mandatory")


class _IbmappnLocalTgByteCost_Type(Integer32):
    """Custom type ibmappnLocalTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgByteCost_Type.__name__ = "Integer32"
_IbmappnLocalTgByteCost_Object = MibTableColumn
ibmappnLocalTgByteCost = _IbmappnLocalTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 11),
    _IbmappnLocalTgByteCost_Type()
)
ibmappnLocalTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgByteCost.setStatus("mandatory")


class _IbmappnLocalTgSecurity_Type(Integer32):
    """Custom type ibmappnLocalTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnLocalTgSecurity_Type.__name__ = "Integer32"
_IbmappnLocalTgSecurity_Object = MibTableColumn
ibmappnLocalTgSecurity = _IbmappnLocalTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 12),
    _IbmappnLocalTgSecurity_Type()
)
ibmappnLocalTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgSecurity.setStatus("mandatory")


class _IbmappnLocalTgDelay_Type(Integer32):
    """Custom type ibmappnLocalTgDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnLocalTgDelay_Type.__name__ = "Integer32"
_IbmappnLocalTgDelay_Object = MibTableColumn
ibmappnLocalTgDelay = _IbmappnLocalTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 13),
    _IbmappnLocalTgDelay_Type()
)
ibmappnLocalTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgDelay.setStatus("mandatory")
_IbmappnLocalTgModemClass_Type = Integer32
_IbmappnLocalTgModemClass_Object = MibTableColumn
ibmappnLocalTgModemClass = _IbmappnLocalTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 14),
    _IbmappnLocalTgModemClass_Type()
)
ibmappnLocalTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgModemClass.setStatus("mandatory")


class _IbmappnLocalTgUsr1_Type(Integer32):
    """Custom type ibmappnLocalTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgUsr1_Type.__name__ = "Integer32"
_IbmappnLocalTgUsr1_Object = MibTableColumn
ibmappnLocalTgUsr1 = _IbmappnLocalTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 15),
    _IbmappnLocalTgUsr1_Type()
)
ibmappnLocalTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgUsr1.setStatus("mandatory")


class _IbmappnLocalTgUsr2_Type(Integer32):
    """Custom type ibmappnLocalTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgUsr2_Type.__name__ = "Integer32"
_IbmappnLocalTgUsr2_Object = MibTableColumn
ibmappnLocalTgUsr2 = _IbmappnLocalTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 16),
    _IbmappnLocalTgUsr2_Type()
)
ibmappnLocalTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgUsr2.setStatus("mandatory")


class _IbmappnLocalTgUsr3_Type(Integer32):
    """Custom type ibmappnLocalTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalTgUsr3_Type.__name__ = "Integer32"
_IbmappnLocalTgUsr3_Object = MibTableColumn
ibmappnLocalTgUsr3 = _IbmappnLocalTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 1, 3, 1, 1, 17),
    _IbmappnLocalTgUsr3_Type()
)
ibmappnLocalTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalTgUsr3.setStatus("mandatory")
_IbmappnLocalEnTopology_ObjectIdentity = ObjectIdentity
ibmappnLocalEnTopology = _IbmappnLocalEnTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2)
)
_IbmappnLocalEnTable_Object = MibTable
ibmappnLocalEnTable = _IbmappnLocalEnTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ibmappnLocalEnTable.setStatus("mandatory")
_IbmappnLocalEnEntry_Object = MibTableRow
ibmappnLocalEnEntry = _IbmappnLocalEnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1)
)
ibmappnLocalEnEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnLocalEnName"),
)
if mibBuilder.loadTexts:
    ibmappnLocalEnEntry.setStatus("mandatory")


class _IbmappnLocalEnName_Type(DisplayString):
    """Custom type ibmappnLocalEnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalEnName_Type.__name__ = "DisplayString"
_IbmappnLocalEnName_Object = MibTableColumn
ibmappnLocalEnName = _IbmappnLocalEnName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1, 1),
    _IbmappnLocalEnName_Type()
)
ibmappnLocalEnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnName.setStatus("mandatory")


class _IbmappnLocalEnEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnLocalEnEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnLocalEnEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnLocalEnEntryTimeLeft_Object = MibTableColumn
ibmappnLocalEnEntryTimeLeft = _IbmappnLocalEnEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1, 2),
    _IbmappnLocalEnEntryTimeLeft_Type()
)
ibmappnLocalEnEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnEntryTimeLeft.setStatus("mandatory")


class _IbmappnLocalEnType_Type(Integer32):
    """Custom type ibmappnLocalEnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("endnode", 2),
          ("len", 4))
    )


_IbmappnLocalEnType_Type.__name__ = "Integer32"
_IbmappnLocalEnType_Object = MibTableColumn
ibmappnLocalEnType = _IbmappnLocalEnType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 1, 1, 3),
    _IbmappnLocalEnType_Type()
)
ibmappnLocalEnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnType.setStatus("mandatory")
_IbmappnLocalEnTgTable_Object = MibTable
ibmappnLocalEnTgTable = _IbmappnLocalEnTgTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2)
)
if mibBuilder.loadTexts:
    ibmappnLocalEnTgTable.setStatus("mandatory")
_IbmappnLocalEnTgEntry_Object = MibTableRow
ibmappnLocalEnTgEntry = _IbmappnLocalEnTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1)
)
ibmappnLocalEnTgEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnLocalEnTgOrigin"),
    (0, "IBM-6611-APPN-MIB", "ibmappnLocalEnTgDest"),
    (0, "IBM-6611-APPN-MIB", "ibmappnLocalEnTgNum"),
)
if mibBuilder.loadTexts:
    ibmappnLocalEnTgEntry.setStatus("mandatory")


class _IbmappnLocalEnTgOrigin_Type(DisplayString):
    """Custom type ibmappnLocalEnTgOrigin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalEnTgOrigin_Type.__name__ = "DisplayString"
_IbmappnLocalEnTgOrigin_Object = MibTableColumn
ibmappnLocalEnTgOrigin = _IbmappnLocalEnTgOrigin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 1),
    _IbmappnLocalEnTgOrigin_Type()
)
ibmappnLocalEnTgOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgOrigin.setStatus("mandatory")


class _IbmappnLocalEnTgDest_Type(DisplayString):
    """Custom type ibmappnLocalEnTgDest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnLocalEnTgDest_Type.__name__ = "DisplayString"
_IbmappnLocalEnTgDest_Object = MibTableColumn
ibmappnLocalEnTgDest = _IbmappnLocalEnTgDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 2),
    _IbmappnLocalEnTgDest_Type()
)
ibmappnLocalEnTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDest.setStatus("mandatory")
_IbmappnLocalEnTgNum_Type = Integer32
_IbmappnLocalEnTgNum_Object = MibTableColumn
ibmappnLocalEnTgNum = _IbmappnLocalEnTgNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 3),
    _IbmappnLocalEnTgNum_Type()
)
ibmappnLocalEnTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgNum.setStatus("mandatory")


class _IbmappnLocalEnTgEntryTimeLeft_Type(Integer32):
    """Custom type ibmappnLocalEnTgEntryTimeLeft based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IbmappnLocalEnTgEntryTimeLeft_Type.__name__ = "Integer32"
_IbmappnLocalEnTgEntryTimeLeft_Object = MibTableColumn
ibmappnLocalEnTgEntryTimeLeft = _IbmappnLocalEnTgEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 4),
    _IbmappnLocalEnTgEntryTimeLeft_Type()
)
ibmappnLocalEnTgEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgEntryTimeLeft.setStatus("mandatory")


class _IbmappnLocalEnTgDestVirtual_Type(Integer32):
    """Custom type ibmappnLocalEnTgDestVirtual based on Integer32"""
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


_IbmappnLocalEnTgDestVirtual_Type.__name__ = "Integer32"
_IbmappnLocalEnTgDestVirtual_Object = MibTableColumn
ibmappnLocalEnTgDestVirtual = _IbmappnLocalEnTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 5),
    _IbmappnLocalEnTgDestVirtual_Type()
)
ibmappnLocalEnTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDestVirtual.setStatus("mandatory")
_IbmappnLocalEnTgDlcData_Type = OctetString
_IbmappnLocalEnTgDlcData_Object = MibTableColumn
ibmappnLocalEnTgDlcData = _IbmappnLocalEnTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 6),
    _IbmappnLocalEnTgDlcData_Type()
)
ibmappnLocalEnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDlcData.setStatus("mandatory")


class _IbmappnLocalEnTgOperational_Type(Integer32):
    """Custom type ibmappnLocalEnTgOperational based on Integer32"""
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


_IbmappnLocalEnTgOperational_Type.__name__ = "Integer32"
_IbmappnLocalEnTgOperational_Object = MibTableColumn
ibmappnLocalEnTgOperational = _IbmappnLocalEnTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 7),
    _IbmappnLocalEnTgOperational_Type()
)
ibmappnLocalEnTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgOperational.setStatus("mandatory")


class _IbmappnLocalEnTgCpCpSession_Type(Integer32):
    """Custom type ibmappnLocalEnTgCpCpSession based on Integer32"""
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


_IbmappnLocalEnTgCpCpSession_Type.__name__ = "Integer32"
_IbmappnLocalEnTgCpCpSession_Object = MibTableColumn
ibmappnLocalEnTgCpCpSession = _IbmappnLocalEnTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 8),
    _IbmappnLocalEnTgCpCpSession_Type()
)
ibmappnLocalEnTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgCpCpSession.setStatus("mandatory")
_IbmappnLocalEnTgEffCap_Type = Integer32
_IbmappnLocalEnTgEffCap_Object = MibTableColumn
ibmappnLocalEnTgEffCap = _IbmappnLocalEnTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 9),
    _IbmappnLocalEnTgEffCap_Type()
)
ibmappnLocalEnTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgEffCap.setStatus("mandatory")


class _IbmappnLocalEnTgConnCost_Type(Integer32):
    """Custom type ibmappnLocalEnTgConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgConnCost_Type.__name__ = "Integer32"
_IbmappnLocalEnTgConnCost_Object = MibTableColumn
ibmappnLocalEnTgConnCost = _IbmappnLocalEnTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 10),
    _IbmappnLocalEnTgConnCost_Type()
)
ibmappnLocalEnTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgConnCost.setStatus("mandatory")


class _IbmappnLocalEnTgByteCost_Type(Integer32):
    """Custom type ibmappnLocalEnTgByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgByteCost_Type.__name__ = "Integer32"
_IbmappnLocalEnTgByteCost_Object = MibTableColumn
ibmappnLocalEnTgByteCost = _IbmappnLocalEnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 11),
    _IbmappnLocalEnTgByteCost_Type()
)
ibmappnLocalEnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgByteCost.setStatus("mandatory")


class _IbmappnLocalEnTgSecurity_Type(Integer32):
    """Custom type ibmappnLocalEnTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnLocalEnTgSecurity_Type.__name__ = "Integer32"
_IbmappnLocalEnTgSecurity_Object = MibTableColumn
ibmappnLocalEnTgSecurity = _IbmappnLocalEnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 12),
    _IbmappnLocalEnTgSecurity_Type()
)
ibmappnLocalEnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgSecurity.setStatus("mandatory")


class _IbmappnLocalEnTgDelay_Type(Integer32):
    """Custom type ibmappnLocalEnTgDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnLocalEnTgDelay_Type.__name__ = "Integer32"
_IbmappnLocalEnTgDelay_Object = MibTableColumn
ibmappnLocalEnTgDelay = _IbmappnLocalEnTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 13),
    _IbmappnLocalEnTgDelay_Type()
)
ibmappnLocalEnTgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgDelay.setStatus("mandatory")


class _IbmappnLocalEnTgModemClass_Type(Integer32):
    """Custom type ibmappnLocalEnTgModemClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IbmappnLocalEnTgModemClass_Type.__name__ = "Integer32"
_IbmappnLocalEnTgModemClass_Object = MibTableColumn
ibmappnLocalEnTgModemClass = _IbmappnLocalEnTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 14),
    _IbmappnLocalEnTgModemClass_Type()
)
ibmappnLocalEnTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgModemClass.setStatus("mandatory")


class _IbmappnLocalEnTgUsr1_Type(Integer32):
    """Custom type ibmappnLocalEnTgUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgUsr1_Type.__name__ = "Integer32"
_IbmappnLocalEnTgUsr1_Object = MibTableColumn
ibmappnLocalEnTgUsr1 = _IbmappnLocalEnTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 15),
    _IbmappnLocalEnTgUsr1_Type()
)
ibmappnLocalEnTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgUsr1.setStatus("mandatory")


class _IbmappnLocalEnTgUsr2_Type(Integer32):
    """Custom type ibmappnLocalEnTgUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgUsr2_Type.__name__ = "Integer32"
_IbmappnLocalEnTgUsr2_Object = MibTableColumn
ibmappnLocalEnTgUsr2 = _IbmappnLocalEnTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 16),
    _IbmappnLocalEnTgUsr2_Type()
)
ibmappnLocalEnTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgUsr2.setStatus("mandatory")


class _IbmappnLocalEnTgUsr3_Type(Integer32):
    """Custom type ibmappnLocalEnTgUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnLocalEnTgUsr3_Type.__name__ = "Integer32"
_IbmappnLocalEnTgUsr3_Object = MibTableColumn
ibmappnLocalEnTgUsr3 = _IbmappnLocalEnTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 3, 2, 2, 1, 17),
    _IbmappnLocalEnTgUsr3_Type()
)
ibmappnLocalEnTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnLocalEnTgUsr3.setStatus("mandatory")
_IbmappnDir_ObjectIdentity = ObjectIdentity
ibmappnDir = _IbmappnDir_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5)
)
_IbmappnDirPerf_ObjectIdentity = ObjectIdentity
ibmappnDirPerf = _IbmappnDirPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1)
)
_IbmappnDirMaxCaches_Type = Integer32
_IbmappnDirMaxCaches_Object = MibScalar
ibmappnDirMaxCaches = _IbmappnDirMaxCaches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 1),
    _IbmappnDirMaxCaches_Type()
)
ibmappnDirMaxCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirMaxCaches.setStatus("mandatory")
_IbmappnDirCurCaches_Type = Gauge32
_IbmappnDirCurCaches_Object = MibScalar
ibmappnDirCurCaches = _IbmappnDirCurCaches_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 2),
    _IbmappnDirCurCaches_Type()
)
ibmappnDirCurCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirCurCaches.setStatus("mandatory")
_IbmappnDirCurHomeEntries_Type = Gauge32
_IbmappnDirCurHomeEntries_Object = MibScalar
ibmappnDirCurHomeEntries = _IbmappnDirCurHomeEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 3),
    _IbmappnDirCurHomeEntries_Type()
)
ibmappnDirCurHomeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirCurHomeEntries.setStatus("mandatory")
_IbmappnDirRegEntries_Type = Gauge32
_IbmappnDirRegEntries_Object = MibScalar
ibmappnDirRegEntries = _IbmappnDirRegEntries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 4),
    _IbmappnDirRegEntries_Type()
)
ibmappnDirRegEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirRegEntries.setStatus("mandatory")
_IbmappnDirInLocates_Type = Counter32
_IbmappnDirInLocates_Object = MibScalar
ibmappnDirInLocates = _IbmappnDirInLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 5),
    _IbmappnDirInLocates_Type()
)
ibmappnDirInLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirInLocates.setStatus("mandatory")
_IbmappnDirInBcastLocates_Type = Counter32
_IbmappnDirInBcastLocates_Object = MibScalar
ibmappnDirInBcastLocates = _IbmappnDirInBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 6),
    _IbmappnDirInBcastLocates_Type()
)
ibmappnDirInBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirInBcastLocates.setStatus("mandatory")
_IbmappnDirOutLocates_Type = Counter32
_IbmappnDirOutLocates_Object = MibScalar
ibmappnDirOutLocates = _IbmappnDirOutLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 7),
    _IbmappnDirOutLocates_Type()
)
ibmappnDirOutLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirOutLocates.setStatus("mandatory")
_IbmappnDirOutBcastLocates_Type = Counter32
_IbmappnDirOutBcastLocates_Object = MibScalar
ibmappnDirOutBcastLocates = _IbmappnDirOutBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 8),
    _IbmappnDirOutBcastLocates_Type()
)
ibmappnDirOutBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirOutBcastLocates.setStatus("mandatory")
_IbmappnDirNotFoundLocates_Type = Counter32
_IbmappnDirNotFoundLocates_Object = MibScalar
ibmappnDirNotFoundLocates = _IbmappnDirNotFoundLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 9),
    _IbmappnDirNotFoundLocates_Type()
)
ibmappnDirNotFoundLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirNotFoundLocates.setStatus("mandatory")
_IbmappnDirNotFoundBcastLocates_Type = Counter32
_IbmappnDirNotFoundBcastLocates_Object = MibScalar
ibmappnDirNotFoundBcastLocates = _IbmappnDirNotFoundBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 10),
    _IbmappnDirNotFoundBcastLocates_Type()
)
ibmappnDirNotFoundBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirNotFoundBcastLocates.setStatus("mandatory")
_IbmappnDirLocateOutstands_Type = Gauge32
_IbmappnDirLocateOutstands_Object = MibScalar
ibmappnDirLocateOutstands = _IbmappnDirLocateOutstands_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 1, 11),
    _IbmappnDirLocateOutstands_Type()
)
ibmappnDirLocateOutstands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLocateOutstands.setStatus("mandatory")
_IbmappnDirTable_Object = MibTable
ibmappnDirTable = _IbmappnDirTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2)
)
if mibBuilder.loadTexts:
    ibmappnDirTable.setStatus("mandatory")
_IbmappnDirEntry_Object = MibTableRow
ibmappnDirEntry = _IbmappnDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1)
)
ibmappnDirEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnDirLuName"),
)
if mibBuilder.loadTexts:
    ibmappnDirEntry.setStatus("mandatory")


class _IbmappnDirLuName_Type(DisplayString):
    """Custom type ibmappnDirLuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnDirLuName_Type.__name__ = "DisplayString"
_IbmappnDirLuName_Object = MibTableColumn
ibmappnDirLuName = _IbmappnDirLuName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 1),
    _IbmappnDirLuName_Type()
)
ibmappnDirLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLuName.setStatus("mandatory")


class _IbmappnDirServerName_Type(DisplayString):
    """Custom type ibmappnDirServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnDirServerName_Type.__name__ = "DisplayString"
_IbmappnDirServerName_Object = MibTableColumn
ibmappnDirServerName = _IbmappnDirServerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 2),
    _IbmappnDirServerName_Type()
)
ibmappnDirServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirServerName.setStatus("mandatory")


class _IbmappnDirLuOwnerName_Type(DisplayString):
    """Custom type ibmappnDirLuOwnerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 17),
    )


_IbmappnDirLuOwnerName_Type.__name__ = "DisplayString"
_IbmappnDirLuOwnerName_Object = MibTableColumn
ibmappnDirLuOwnerName = _IbmappnDirLuOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 3),
    _IbmappnDirLuOwnerName_Type()
)
ibmappnDirLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLuOwnerName.setStatus("mandatory")


class _IbmappnDirLuLocation_Type(Integer32):
    """Custom type ibmappnDirLuLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("local", 1),
          ("xdomain", 3))
    )


_IbmappnDirLuLocation_Type.__name__ = "Integer32"
_IbmappnDirLuLocation_Object = MibTableColumn
ibmappnDirLuLocation = _IbmappnDirLuLocation_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 4),
    _IbmappnDirLuLocation_Type()
)
ibmappnDirLuLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirLuLocation.setStatus("mandatory")


class _IbmappnDirType_Type(Integer32):
    """Custom type ibmappnDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cache", 2),
          ("home", 1),
          ("registered", 3))
    )


_IbmappnDirType_Type.__name__ = "Integer32"
_IbmappnDirType_Object = MibTableColumn
ibmappnDirType = _IbmappnDirType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 5),
    _IbmappnDirType_Type()
)
ibmappnDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirType.setStatus("mandatory")


class _IbmappnDirWildCard_Type(Integer32):
    """Custom type ibmappnDirWildCard based on Integer32"""
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
        *(("explicit-entry", 2),
          ("full-wildcard", 4),
          ("other", 1),
          ("partial-wildcard", 3))
    )


_IbmappnDirWildCard_Type.__name__ = "Integer32"
_IbmappnDirWildCard_Object = MibTableColumn
ibmappnDirWildCard = _IbmappnDirWildCard_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 5, 2, 1, 6),
    _IbmappnDirWildCard_Type()
)
ibmappnDirWildCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnDirWildCard.setStatus("mandatory")
_IbmappnCos_ObjectIdentity = ObjectIdentity
ibmappnCos = _IbmappnCos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6)
)
_IbmappnCosModeTable_Object = MibTable
ibmappnCosModeTable = _IbmappnCosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1)
)
if mibBuilder.loadTexts:
    ibmappnCosModeTable.setStatus("mandatory")
_IbmappnCosModeEntry_Object = MibTableRow
ibmappnCosModeEntry = _IbmappnCosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1, 1)
)
ibmappnCosModeEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnCosModeName"),
)
if mibBuilder.loadTexts:
    ibmappnCosModeEntry.setStatus("mandatory")


class _IbmappnCosModeName_Type(DisplayString):
    """Custom type ibmappnCosModeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosModeName_Type.__name__ = "DisplayString"
_IbmappnCosModeName_Object = MibTableColumn
ibmappnCosModeName = _IbmappnCosModeName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1, 1, 1),
    _IbmappnCosModeName_Type()
)
ibmappnCosModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosModeName.setStatus("mandatory")


class _IbmappnCosModeCosName_Type(DisplayString):
    """Custom type ibmappnCosModeCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosModeCosName_Type.__name__ = "DisplayString"
_IbmappnCosModeCosName_Object = MibTableColumn
ibmappnCosModeCosName = _IbmappnCosModeCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 1, 1, 2),
    _IbmappnCosModeCosName_Type()
)
ibmappnCosModeCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosModeCosName.setStatus("mandatory")
_IbmappnCosNameTable_Object = MibTable
ibmappnCosNameTable = _IbmappnCosNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2)
)
if mibBuilder.loadTexts:
    ibmappnCosNameTable.setStatus("mandatory")
_IbmappnCosNameEntry_Object = MibTableRow
ibmappnCosNameEntry = _IbmappnCosNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2, 1)
)
ibmappnCosNameEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnCosName"),
)
if mibBuilder.loadTexts:
    ibmappnCosNameEntry.setStatus("mandatory")


class _IbmappnCosName_Type(DisplayString):
    """Custom type ibmappnCosName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosName_Type.__name__ = "DisplayString"
_IbmappnCosName_Object = MibTableColumn
ibmappnCosName = _IbmappnCosName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2, 1, 1),
    _IbmappnCosName_Type()
)
ibmappnCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosName.setStatus("mandatory")


class _IbmappnCosTransPriority_Type(Integer32):
    """Custom type ibmappnCosTransPriority based on Integer32"""
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
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_IbmappnCosTransPriority_Type.__name__ = "Integer32"
_IbmappnCosTransPriority_Object = MibTableColumn
ibmappnCosTransPriority = _IbmappnCosTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 2, 1, 2),
    _IbmappnCosTransPriority_Type()
)
ibmappnCosTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTransPriority.setStatus("mandatory")
_IbmappnCosNodeRowTable_Object = MibTable
ibmappnCosNodeRowTable = _IbmappnCosNodeRowTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3)
)
if mibBuilder.loadTexts:
    ibmappnCosNodeRowTable.setStatus("mandatory")
_IbmappnCosNodeRowEntry_Object = MibTableRow
ibmappnCosNodeRowEntry = _IbmappnCosNodeRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1)
)
ibmappnCosNodeRowEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnCosNodeRowName"),
    (0, "IBM-6611-APPN-MIB", "ibmappnCosNodeRowIndex"),
)
if mibBuilder.loadTexts:
    ibmappnCosNodeRowEntry.setStatus("mandatory")


class _IbmappnCosNodeRowName_Type(DisplayString):
    """Custom type ibmappnCosNodeRowName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosNodeRowName_Type.__name__ = "DisplayString"
_IbmappnCosNodeRowName_Object = MibTableColumn
ibmappnCosNodeRowName = _IbmappnCosNodeRowName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 1),
    _IbmappnCosNodeRowName_Type()
)
ibmappnCosNodeRowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowName.setStatus("mandatory")


class _IbmappnCosNodeRowIndex_Type(Integer32):
    """Custom type ibmappnCosNodeRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosNodeRowIndex_Type.__name__ = "Integer32"
_IbmappnCosNodeRowIndex_Object = MibTableColumn
ibmappnCosNodeRowIndex = _IbmappnCosNodeRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 2),
    _IbmappnCosNodeRowIndex_Type()
)
ibmappnCosNodeRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowIndex.setStatus("mandatory")
_IbmappnCosNodeRowWgt_Type = DisplayString
_IbmappnCosNodeRowWgt_Object = MibTableColumn
ibmappnCosNodeRowWgt = _IbmappnCosNodeRowWgt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 3),
    _IbmappnCosNodeRowWgt_Type()
)
ibmappnCosNodeRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowWgt.setStatus("mandatory")


class _IbmappnCosNodeRowResistMin_Type(Integer32):
    """Custom type ibmappnCosNodeRowResistMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosNodeRowResistMin_Type.__name__ = "Integer32"
_IbmappnCosNodeRowResistMin_Object = MibTableColumn
ibmappnCosNodeRowResistMin = _IbmappnCosNodeRowResistMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 4),
    _IbmappnCosNodeRowResistMin_Type()
)
ibmappnCosNodeRowResistMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowResistMin.setStatus("mandatory")


class _IbmappnCosNodeRowResistMax_Type(Integer32):
    """Custom type ibmappnCosNodeRowResistMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosNodeRowResistMax_Type.__name__ = "Integer32"
_IbmappnCosNodeRowResistMax_Object = MibTableColumn
ibmappnCosNodeRowResistMax = _IbmappnCosNodeRowResistMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 5),
    _IbmappnCosNodeRowResistMax_Type()
)
ibmappnCosNodeRowResistMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowResistMax.setStatus("mandatory")


class _IbmappnCosNodeRowMinCongestAllow_Type(Integer32):
    """Custom type ibmappnCosNodeRowMinCongestAllow based on Integer32"""
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


_IbmappnCosNodeRowMinCongestAllow_Type.__name__ = "Integer32"
_IbmappnCosNodeRowMinCongestAllow_Object = MibTableColumn
ibmappnCosNodeRowMinCongestAllow = _IbmappnCosNodeRowMinCongestAllow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 6),
    _IbmappnCosNodeRowMinCongestAllow_Type()
)
ibmappnCosNodeRowMinCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowMinCongestAllow.setStatus("mandatory")


class _IbmappnCosNodeRowMaxCongestAllow_Type(Integer32):
    """Custom type ibmappnCosNodeRowMaxCongestAllow based on Integer32"""
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


_IbmappnCosNodeRowMaxCongestAllow_Type.__name__ = "Integer32"
_IbmappnCosNodeRowMaxCongestAllow_Object = MibTableColumn
ibmappnCosNodeRowMaxCongestAllow = _IbmappnCosNodeRowMaxCongestAllow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 3, 1, 7),
    _IbmappnCosNodeRowMaxCongestAllow_Type()
)
ibmappnCosNodeRowMaxCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosNodeRowMaxCongestAllow.setStatus("mandatory")
_IbmappnCosTgRowTable_Object = MibTable
ibmappnCosTgRowTable = _IbmappnCosTgRowTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4)
)
if mibBuilder.loadTexts:
    ibmappnCosTgRowTable.setStatus("mandatory")
_IbmappnCosTgRowEntry_Object = MibTableRow
ibmappnCosTgRowEntry = _IbmappnCosTgRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1)
)
ibmappnCosTgRowEntry.setIndexNames(
    (0, "IBM-6611-APPN-MIB", "ibmappnCosTgRowName"),
    (0, "IBM-6611-APPN-MIB", "ibmappnCosTgRowIndex"),
)
if mibBuilder.loadTexts:
    ibmappnCosTgRowEntry.setStatus("mandatory")


class _IbmappnCosTgRowName_Type(DisplayString):
    """Custom type ibmappnCosTgRowName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_IbmappnCosTgRowName_Type.__name__ = "DisplayString"
_IbmappnCosTgRowName_Object = MibTableColumn
ibmappnCosTgRowName = _IbmappnCosTgRowName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 1),
    _IbmappnCosTgRowName_Type()
)
ibmappnCosTgRowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowName.setStatus("mandatory")


class _IbmappnCosTgRowIndex_Type(Integer32):
    """Custom type ibmappnCosTgRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowIndex_Type.__name__ = "Integer32"
_IbmappnCosTgRowIndex_Object = MibTableColumn
ibmappnCosTgRowIndex = _IbmappnCosTgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 2),
    _IbmappnCosTgRowIndex_Type()
)
ibmappnCosTgRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowIndex.setStatus("mandatory")
_IbmappnCosTgRowWgt_Type = DisplayString
_IbmappnCosTgRowWgt_Object = MibTableColumn
ibmappnCosTgRowWgt = _IbmappnCosTgRowWgt_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 3),
    _IbmappnCosTgRowWgt_Type()
)
ibmappnCosTgRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowWgt.setStatus("mandatory")
_IbmappnCosTgRowEffCapMin_Type = Integer32
_IbmappnCosTgRowEffCapMin_Object = MibTableColumn
ibmappnCosTgRowEffCapMin = _IbmappnCosTgRowEffCapMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 4),
    _IbmappnCosTgRowEffCapMin_Type()
)
ibmappnCosTgRowEffCapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowEffCapMin.setStatus("mandatory")
_IbmappnCosTgRowEffCapMax_Type = Integer32
_IbmappnCosTgRowEffCapMax_Object = MibTableColumn
ibmappnCosTgRowEffCapMax = _IbmappnCosTgRowEffCapMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 5),
    _IbmappnCosTgRowEffCapMax_Type()
)
ibmappnCosTgRowEffCapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowEffCapMax.setStatus("mandatory")


class _IbmappnCosTgRowConnCostMin_Type(Integer32):
    """Custom type ibmappnCosTgRowConnCostMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowConnCostMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowConnCostMin_Object = MibTableColumn
ibmappnCosTgRowConnCostMin = _IbmappnCosTgRowConnCostMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 6),
    _IbmappnCosTgRowConnCostMin_Type()
)
ibmappnCosTgRowConnCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowConnCostMin.setStatus("mandatory")


class _IbmappnCosTgRowConnCostMax_Type(Integer32):
    """Custom type ibmappnCosTgRowConnCostMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowConnCostMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowConnCostMax_Object = MibTableColumn
ibmappnCosTgRowConnCostMax = _IbmappnCosTgRowConnCostMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 7),
    _IbmappnCosTgRowConnCostMax_Type()
)
ibmappnCosTgRowConnCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowConnCostMax.setStatus("mandatory")


class _IbmappnCosTgRowByteCostMin_Type(Integer32):
    """Custom type ibmappnCosTgRowByteCostMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowByteCostMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowByteCostMin_Object = MibTableColumn
ibmappnCosTgRowByteCostMin = _IbmappnCosTgRowByteCostMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 8),
    _IbmappnCosTgRowByteCostMin_Type()
)
ibmappnCosTgRowByteCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowByteCostMin.setStatus("mandatory")


class _IbmappnCosTgRowByteCostMax_Type(Integer32):
    """Custom type ibmappnCosTgRowByteCostMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowByteCostMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowByteCostMax_Object = MibTableColumn
ibmappnCosTgRowByteCostMax = _IbmappnCosTgRowByteCostMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 9),
    _IbmappnCosTgRowByteCostMax_Type()
)
ibmappnCosTgRowByteCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowByteCostMax.setStatus("mandatory")


class _IbmappnCosTgRowSecurityMin_Type(Integer32):
    """Custom type ibmappnCosTgRowSecurityMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnCosTgRowSecurityMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowSecurityMin_Object = MibTableColumn
ibmappnCosTgRowSecurityMin = _IbmappnCosTgRowSecurityMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 10),
    _IbmappnCosTgRowSecurityMin_Type()
)
ibmappnCosTgRowSecurityMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowSecurityMin.setStatus("mandatory")


class _IbmappnCosTgRowSecurityMax_Type(Integer32):
    """Custom type ibmappnCosTgRowSecurityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              32,
              64,
              96,
              128,
              160,
              192)
        )
    )
    namedValues = NamedValues(
        *(("encrypted", 160),
          ("guardedConduit", 128),
          ("guardedRadiation", 192),
          ("nonsecure", 1),
          ("publicSwitchedNetwork", 32),
          ("secureConduit", 96),
          ("undergroundCable", 64))
    )


_IbmappnCosTgRowSecurityMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowSecurityMax_Object = MibTableColumn
ibmappnCosTgRowSecurityMax = _IbmappnCosTgRowSecurityMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 11),
    _IbmappnCosTgRowSecurityMax_Type()
)
ibmappnCosTgRowSecurityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowSecurityMax.setStatus("mandatory")


class _IbmappnCosTgRowDelayMin_Type(Integer32):
    """Custom type ibmappnCosTgRowDelayMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnCosTgRowDelayMin_Type.__name__ = "Integer32"
_IbmappnCosTgRowDelayMin_Object = MibTableColumn
ibmappnCosTgRowDelayMin = _IbmappnCosTgRowDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 12),
    _IbmappnCosTgRowDelayMin_Type()
)
ibmappnCosTgRowDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowDelayMin.setStatus("mandatory")


class _IbmappnCosTgRowDelayMax_Type(Integer32):
    """Custom type ibmappnCosTgRowDelayMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              384,
              9216,
              147456,
              294912,
              2013265920)
        )
    )
    namedValues = NamedValues(
        *(("long", 294912),
          ("maximum", 2013265920),
          ("minimum", 0),
          ("negligible", 384),
          ("packet", 147456),
          ("terrestrial", 9216))
    )


_IbmappnCosTgRowDelayMax_Type.__name__ = "Integer32"
_IbmappnCosTgRowDelayMax_Object = MibTableColumn
ibmappnCosTgRowDelayMax = _IbmappnCosTgRowDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 13),
    _IbmappnCosTgRowDelayMax_Type()
)
ibmappnCosTgRowDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowDelayMax.setStatus("mandatory")


class _IbmappnCosTgRowUsr1Min_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr1Min_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr1Min_Object = MibTableColumn
ibmappnCosTgRowUsr1Min = _IbmappnCosTgRowUsr1Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 14),
    _IbmappnCosTgRowUsr1Min_Type()
)
ibmappnCosTgRowUsr1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr1Min.setStatus("mandatory")


class _IbmappnCosTgRowUsr1Max_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr1Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr1Max_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr1Max_Object = MibTableColumn
ibmappnCosTgRowUsr1Max = _IbmappnCosTgRowUsr1Max_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 15),
    _IbmappnCosTgRowUsr1Max_Type()
)
ibmappnCosTgRowUsr1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr1Max.setStatus("mandatory")


class _IbmappnCosTgRowUsr2Min_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr2Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr2Min_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr2Min_Object = MibTableColumn
ibmappnCosTgRowUsr2Min = _IbmappnCosTgRowUsr2Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 16),
    _IbmappnCosTgRowUsr2Min_Type()
)
ibmappnCosTgRowUsr2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr2Min.setStatus("mandatory")


class _IbmappnCosTgRowUsr2Max_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr2Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr2Max_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr2Max_Object = MibTableColumn
ibmappnCosTgRowUsr2Max = _IbmappnCosTgRowUsr2Max_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 17),
    _IbmappnCosTgRowUsr2Max_Type()
)
ibmappnCosTgRowUsr2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr2Max.setStatus("mandatory")


class _IbmappnCosTgRowUsr3Min_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr3Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr3Min_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr3Min_Object = MibTableColumn
ibmappnCosTgRowUsr3Min = _IbmappnCosTgRowUsr3Min_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 18),
    _IbmappnCosTgRowUsr3Min_Type()
)
ibmappnCosTgRowUsr3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr3Min.setStatus("mandatory")


class _IbmappnCosTgRowUsr3Max_Type(Integer32):
    """Custom type ibmappnCosTgRowUsr3Max based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IbmappnCosTgRowUsr3Max_Type.__name__ = "Integer32"
_IbmappnCosTgRowUsr3Max_Object = MibTableColumn
ibmappnCosTgRowUsr3Max = _IbmappnCosTgRowUsr3Max_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 6, 4, 1, 19),
    _IbmappnCosTgRowUsr3Max_Type()
)
ibmappnCosTgRowUsr3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ibmappnCosTgRowUsr3Max.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-6611-APPN-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "ibm6611": ibm6611,
       "ibmappn": ibmappn,
       "ibmappnNode": ibmappnNode,
       "ibmappnGeneralInfoAndCaps": ibmappnGeneralInfoAndCaps,
       "ibmappnNodeCpName": ibmappnNodeCpName,
       "ibmappnNodeNetid": ibmappnNodeNetid,
       "ibmappnNodeBlockNum": ibmappnNodeBlockNum,
       "ibmappnNodeIdNum": ibmappnNodeIdNum,
       "ibmappnNodeType": ibmappnNodeType,
       "ibmappnNodeUpTime": ibmappnNodeUpTime,
       "ibmappnNodeNegotLs": ibmappnNodeNegotLs,
       "ibmappnNodeSegReasm": ibmappnNodeSegReasm,
       "ibmappnNodeBindReasm": ibmappnNodeBindReasm,
       "ibmappnNodeParallelTg": ibmappnNodeParallelTg,
       "ibmappnNodeService": ibmappnNodeService,
       "ibmappnNodeAdaptiveBindPacing": ibmappnNodeAdaptiveBindPacing,
       "ibmappnNnUniqueInfoAndCaps": ibmappnNnUniqueInfoAndCaps,
       "ibmappnNodeNnRcvRegChar": ibmappnNodeNnRcvRegChar,
       "ibmappnNodeNnGateway": ibmappnNodeNnGateway,
       "ibmappnNodeNnCentralDirectory": ibmappnNodeNnCentralDirectory,
       "ibmappnNodeNnTreeCache": ibmappnNodeNnTreeCache,
       "ibmappnNodeNnTreeUpdate": ibmappnNodeNnTreeUpdate,
       "ibmappnNodeNnRouteAddResist": ibmappnNodeNnRouteAddResist,
       "ibmappnNodeNnIsr": ibmappnNodeNnIsr,
       "ibmappnNodeNnFrsn": ibmappnNodeNnFrsn,
       "ibmappnEnUniqueCaps": ibmappnEnUniqueCaps,
       "ibmappnNodeEnSegGen": ibmappnNodeEnSegGen,
       "ibmappnNodeEnModeCosMap": ibmappnNodeEnModeCosMap,
       "ibmappnNodeEnLocateCdinit": ibmappnNodeEnLocateCdinit,
       "ibmappnNodeEnSendRegNames": ibmappnNodeEnSendRegNames,
       "ibmappnNodeEnSendRegChar": ibmappnNodeEnSendRegChar,
       "ibmappnPortInformation": ibmappnPortInformation,
       "ibmappnNodePortTable": ibmappnNodePortTable,
       "ibmappnNodePortEntry": ibmappnNodePortEntry,
       "ibmappnNodePortName": ibmappnNodePortName,
       "ibmappnNodePortState": ibmappnNodePortState,
       "ibmappnNodePortDlcType": ibmappnNodePortDlcType,
       "ibmappnNodePortPortType": ibmappnNodePortPortType,
       "ibmappnNodePortSIMRIM": ibmappnNodePortSIMRIM,
       "ibmappnNodePortLsRole": ibmappnNodePortLsRole,
       "ibmappnNodePortMaxRcvBtuSize": ibmappnNodePortMaxRcvBtuSize,
       "ibmappnNodePortMaxIframeWindow": ibmappnNodePortMaxIframeWindow,
       "ibmappnNodePortDefLsGoodXids": ibmappnNodePortDefLsGoodXids,
       "ibmappnNodePortDefLsBadXids": ibmappnNodePortDefLsBadXids,
       "ibmappnNodePortDynLsGoodXids": ibmappnNodePortDynLsGoodXids,
       "ibmappnNodePortDynLsBadXids": ibmappnNodePortDynLsBadXids,
       "ibmappnNodePortSpecific": ibmappnNodePortSpecific,
       "ibmappnNodePortIpTable": ibmappnNodePortIpTable,
       "ibmappnNodePortIpEntry": ibmappnNodePortIpEntry,
       "ibmappnNodePortIpName": ibmappnNodePortIpName,
       "ibmappnNodePortIpPortNum": ibmappnNodePortIpPortNum,
       "ibmappnNodePortDlsTable": ibmappnNodePortDlsTable,
       "ibmappnNodePortDlsEntry": ibmappnNodePortDlsEntry,
       "ibmappnNodePortDlsName": ibmappnNodePortDlsName,
       "ibmappnNodePortDlsMac": ibmappnNodePortDlsMac,
       "ibmappnNodePortDlsSap": ibmappnNodePortDlsSap,
       "ibmappnNodePortTrTable": ibmappnNodePortTrTable,
       "ibmappnNodePortTrEntry": ibmappnNodePortTrEntry,
       "ibmappnNodePortTrName": ibmappnNodePortTrName,
       "ibmappnNodePortTrMac": ibmappnNodePortTrMac,
       "ibmappnNodePortTrSap": ibmappnNodePortTrSap,
       "ibmappnNodePortDlcTraceTable": ibmappnNodePortDlcTraceTable,
       "ibmappnNodePortDlcTraceEntry": ibmappnNodePortDlcTraceEntry,
       "ibmappnNodePortDlcTracPortName": ibmappnNodePortDlcTracPortName,
       "ibmappnNodePortDlcTracIndex": ibmappnNodePortDlcTracIndex,
       "ibmappnNodePortDlcTracDlcType": ibmappnNodePortDlcTracDlcType,
       "ibmappnNodePortDlcTracLocalAddr": ibmappnNodePortDlcTracLocalAddr,
       "ibmappnNodePortDlcTracRemoteAddr": ibmappnNodePortDlcTracRemoteAddr,
       "ibmappnNodePortDlcTracMsgType": ibmappnNodePortDlcTracMsgType,
       "ibmappnNodePortDlcTracCmdType": ibmappnNodePortDlcTracCmdType,
       "ibmappnNodePortDlcTracUseWan": ibmappnNodePortDlcTracUseWan,
       "ibmappnLinkStationInformation": ibmappnLinkStationInformation,
       "ibmappnNodeLsTable": ibmappnNodeLsTable,
       "ibmappnNodeLsEntry": ibmappnNodeLsEntry,
       "ibmappnNodeLsName": ibmappnNodeLsName,
       "ibmappnNodeLsPortName": ibmappnNodeLsPortName,
       "ibmappnNodeLsDlcType": ibmappnNodeLsDlcType,
       "ibmappnNodeLsDynamic": ibmappnNodeLsDynamic,
       "ibmappnNodeLsState": ibmappnNodeLsState,
       "ibmappnNodeLsCpName": ibmappnNodeLsCpName,
       "ibmappnNodeLsTgNum": ibmappnNodeLsTgNum,
       "ibmappnNodeLsLimResource": ibmappnNodeLsLimResource,
       "ibmappnNodeLsMigration": ibmappnNodeLsMigration,
       "ibmappnNodeLsBlockNum": ibmappnNodeLsBlockNum,
       "ibmappnNodeLsIdNum": ibmappnNodeLsIdNum,
       "ibmappnNodeLsCpCpSession": ibmappnNodeLsCpCpSession,
       "ibmappnNodeLsTargetPacingCount": ibmappnNodeLsTargetPacingCount,
       "ibmappnNodeLsMaxSendBtuSize": ibmappnNodeLsMaxSendBtuSize,
       "ibmappnNodeLsEffCap": ibmappnNodeLsEffCap,
       "ibmappnNodeLsConnCost": ibmappnNodeLsConnCost,
       "ibmappnNodeLsByteCost": ibmappnNodeLsByteCost,
       "ibmappnNodeLsSecurity": ibmappnNodeLsSecurity,
       "ibmappnNodeLsDelay": ibmappnNodeLsDelay,
       "ibmappnNodeLsUsr1": ibmappnNodeLsUsr1,
       "ibmappnNodeLsUsr2": ibmappnNodeLsUsr2,
       "ibmappnNodeLsUsr3": ibmappnNodeLsUsr3,
       "ibmappnNodeLsInXidBytes": ibmappnNodeLsInXidBytes,
       "ibmappnNodeLsInMsgBytes": ibmappnNodeLsInMsgBytes,
       "ibmappnNodeLsInXidFrames": ibmappnNodeLsInXidFrames,
       "ibmappnNodeLsInMsgFrames": ibmappnNodeLsInMsgFrames,
       "ibmappnNodeLsOutXidBytes": ibmappnNodeLsOutXidBytes,
       "ibmappnNodeLsOutMsgBytes": ibmappnNodeLsOutMsgBytes,
       "ibmappnNodeLsOutXidFrames": ibmappnNodeLsOutXidFrames,
       "ibmappnNodeLsOutMsgFrames": ibmappnNodeLsOutMsgFrames,
       "ibmappnNodeLsEchoRsps": ibmappnNodeLsEchoRsps,
       "ibmappnNodeLsCurrentDelay": ibmappnNodeLsCurrentDelay,
       "ibmappnNodeLsMaxDelay": ibmappnNodeLsMaxDelay,
       "ibmappnNodeLsMinDelay": ibmappnNodeLsMinDelay,
       "ibmappnNodeLsMaxDelayTime": ibmappnNodeLsMaxDelayTime,
       "ibmappnNodeLsGoodXids": ibmappnNodeLsGoodXids,
       "ibmappnNodeLsBadXids": ibmappnNodeLsBadXids,
       "ibmappnNodeLsSpecific": ibmappnNodeLsSpecific,
       "ibmappnNodeLsSubState": ibmappnNodeLsSubState,
       "ibmappnNodeLsStartTime": ibmappnNodeLsStartTime,
       "ibmappnNodeLsActiveTime": ibmappnNodeLsActiveTime,
       "ibmappnNodeLsCurrentStateTime": ibmappnNodeLsCurrentStateTime,
       "ibmappnNodeLsIpTable": ibmappnNodeLsIpTable,
       "ibmappnNodeLsIpEntry": ibmappnNodeLsIpEntry,
       "ibmappnNodeLsIpName": ibmappnNodeLsIpName,
       "ibmappnNodeLsIpState": ibmappnNodeLsIpState,
       "ibmappnNodeLsLocalIpAddr": ibmappnNodeLsLocalIpAddr,
       "ibmappnNodeLsLocalIpPortNum": ibmappnNodeLsLocalIpPortNum,
       "ibmappnNodeLsRemoteIpAddr": ibmappnNodeLsRemoteIpAddr,
       "ibmappnNodeLsRemoteIpPortNum": ibmappnNodeLsRemoteIpPortNum,
       "ibmappnNodeLsDlsTable": ibmappnNodeLsDlsTable,
       "ibmappnNodeLsDlsEntry": ibmappnNodeLsDlsEntry,
       "ibmappnNodeLsDlsName": ibmappnNodeLsDlsName,
       "ibmappnNodeLsDlsState": ibmappnNodeLsDlsState,
       "ibmappnNodeLsLocalDlsMac": ibmappnNodeLsLocalDlsMac,
       "ibmappnNodeLsLocalDlsSap": ibmappnNodeLsLocalDlsSap,
       "ibmappnNodeLsRemoteDlsMac": ibmappnNodeLsRemoteDlsMac,
       "ibmappnNodeLsRemoteDlsSap": ibmappnNodeLsRemoteDlsSap,
       "ibmappnNodeLsTrTable": ibmappnNodeLsTrTable,
       "ibmappnNodeLsTrEntry": ibmappnNodeLsTrEntry,
       "ibmappnNodeLsTrName": ibmappnNodeLsTrName,
       "ibmappnNodeLsTrState": ibmappnNodeLsTrState,
       "ibmappnNodeLsLocalTrMac": ibmappnNodeLsLocalTrMac,
       "ibmappnNodeLsLocalTrSap": ibmappnNodeLsLocalTrSap,
       "ibmappnNodeLsRemoteTrMac": ibmappnNodeLsRemoteTrMac,
       "ibmappnNodeLsRemoteTrSap": ibmappnNodeLsRemoteTrSap,
       "ibmappnNodeLsStatusTable": ibmappnNodeLsStatusTable,
       "ibmappnNodeLsStatusEntry": ibmappnNodeLsStatusEntry,
       "ibmappnNodeLsStatusIndex": ibmappnNodeLsStatusIndex,
       "ibmappnNodeLsStatusTime": ibmappnNodeLsStatusTime,
       "ibmappnNodeLsStatusLsName": ibmappnNodeLsStatusLsName,
       "ibmappnNodeLsStatusCpName": ibmappnNodeLsStatusCpName,
       "ibmappnNodeLsStatusNodeId": ibmappnNodeLsStatusNodeId,
       "ibmappnNodeLsStatusTgNum": ibmappnNodeLsStatusTgNum,
       "ibmappnNodeLsStatusGeneralSense": ibmappnNodeLsStatusGeneralSense,
       "ibmappnNodeLsStatusNofRetry": ibmappnNodeLsStatusNofRetry,
       "ibmappnNodeLsStatusEndSense": ibmappnNodeLsStatusEndSense,
       "ibmappnNodeLsStatusXidLocalSense": ibmappnNodeLsStatusXidLocalSense,
       "ibmappnNodeLsStatusXidRemoteSense": ibmappnNodeLsStatusXidRemoteSense,
       "ibmappnNodeLsStatusXidByteInError": ibmappnNodeLsStatusXidByteInError,
       "ibmappnNodeLsStatusXidBitInError": ibmappnNodeLsStatusXidBitInError,
       "ibmappnNodeLsStatusDlcType": ibmappnNodeLsStatusDlcType,
       "ibmappnNodeLsStatusLocalAddr": ibmappnNodeLsStatusLocalAddr,
       "ibmappnNodeLsStatusRemoteAddr": ibmappnNodeLsStatusRemoteAddr,
       "ibmappnSnmpInformation": ibmappnSnmpInformation,
       "ibmappnSnmpInPkts": ibmappnSnmpInPkts,
       "ibmappnSnmpInGetRequests": ibmappnSnmpInGetRequests,
       "ibmappnSnmpInGetNexts": ibmappnSnmpInGetNexts,
       "ibmappnSnmpInSetRequests": ibmappnSnmpInSetRequests,
       "ibmappnSnmpInTotalVars": ibmappnSnmpInTotalVars,
       "ibmappnSnmpInGetVars": ibmappnSnmpInGetVars,
       "ibmappnSnmpInGetNextVars": ibmappnSnmpInGetNextVars,
       "ibmappnSnmpInSetVars": ibmappnSnmpInSetVars,
       "ibmappnSnmpOutNoSuchNames": ibmappnSnmpOutNoSuchNames,
       "ibmappnSnmpOutGenErrs": ibmappnSnmpOutGenErrs,
       "ibmappnMemoryUse": ibmappnMemoryUse,
       "ibmappnMemorySize": ibmappnMemorySize,
       "ibmappnMemoryUsed": ibmappnMemoryUsed,
       "ibmappnMemoryWarnThresh": ibmappnMemoryWarnThresh,
       "ibmappnMemoryCritThresh": ibmappnMemoryCritThresh,
       "ibmappnXidInformation": ibmappnXidInformation,
       "ibmappnNodeDefLsGoodXids": ibmappnNodeDefLsGoodXids,
       "ibmappnNodeDefLsBadXids": ibmappnNodeDefLsBadXids,
       "ibmappnNodeDynLsGoodXids": ibmappnNodeDynLsGoodXids,
       "ibmappnNodeDynLsBadXids": ibmappnNodeDynLsBadXids,
       "ibmappnNn": ibmappnNn,
       "ibmappnNnTopo": ibmappnNnTopo,
       "ibmappnNnTopoMaxNodes": ibmappnNnTopoMaxNodes,
       "ibmappnNnTopoCurNumNodes": ibmappnNnTopoCurNumNodes,
       "ibmappnNnTopoInTdus": ibmappnNnTopoInTdus,
       "ibmappnNnTopoOutTdus": ibmappnNnTopoOutTdus,
       "ibmappnNnTopoNodeLowRsns": ibmappnNnTopoNodeLowRsns,
       "ibmappnNnTopoNodeEqualRsns": ibmappnNnTopoNodeEqualRsns,
       "ibmappnNnTopoNodeGoodHighRsns": ibmappnNnTopoNodeGoodHighRsns,
       "ibmappnNnTopoNodeBadHighRsns": ibmappnNnTopoNodeBadHighRsns,
       "ibmappnNnTopoNodeStateUpdates": ibmappnNnTopoNodeStateUpdates,
       "ibmappnNnTopoNodeErrors": ibmappnNnTopoNodeErrors,
       "ibmappnNnTopoNodeTimerUpdates": ibmappnNnTopoNodeTimerUpdates,
       "ibmappnNnTopoNodePurges": ibmappnNnTopoNodePurges,
       "ibmappnNnTopoTgLowRsns": ibmappnNnTopoTgLowRsns,
       "ibmappnNnTopoTgEqualRsns": ibmappnNnTopoTgEqualRsns,
       "ibmappnNnTopoTgGoodHighRsns": ibmappnNnTopoTgGoodHighRsns,
       "ibmappnNnTopoTgBadHighRsns": ibmappnNnTopoTgBadHighRsns,
       "ibmappnNnTopoTgStateUpdates": ibmappnNnTopoTgStateUpdates,
       "ibmappnNnTopoTgErrors": ibmappnNnTopoTgErrors,
       "ibmappnNnTopoTgTimerUpdates": ibmappnNnTopoTgTimerUpdates,
       "ibmappnNnTopoTgPurges": ibmappnNnTopoTgPurges,
       "ibmappnNnTopoTotalRouteCalcs": ibmappnNnTopoTotalRouteCalcs,
       "ibmappnNnTopoTotalRouteRejs": ibmappnNnTopoTotalRouteRejs,
       "ibmappnNnTopoRouteTable": ibmappnNnTopoRouteTable,
       "ibmappnNnTopoRouteEntry": ibmappnNnTopoRouteEntry,
       "ibmappnNnTopoRouteCos": ibmappnNnTopoRouteCos,
       "ibmappnNnTopoRouteTrees": ibmappnNnTopoRouteTrees,
       "ibmappnNnTopoRouteCalcs": ibmappnNnTopoRouteCalcs,
       "ibmappnNnTopoRouteRejs": ibmappnNnTopoRouteRejs,
       "ibmappnNnAdjNodeTable": ibmappnNnAdjNodeTable,
       "ibmappnNnAdjNodeEntry": ibmappnNnAdjNodeEntry,
       "ibmappnNnAdjNodeAdjName": ibmappnNnAdjNodeAdjName,
       "ibmappnNnAdjNodeCpCpSessStatus": ibmappnNnAdjNodeCpCpSessStatus,
       "ibmappnNnAdjNodeOutOfSeqTdus": ibmappnNnAdjNodeOutOfSeqTdus,
       "ibmappnNnAdjNodeLastFrsnSent": ibmappnNnAdjNodeLastFrsnSent,
       "ibmappnNnAdjNodeLastFrsnRcvd": ibmappnNnAdjNodeLastFrsnRcvd,
       "ibmappnNnTopology": ibmappnNnTopology,
       "ibmappnNnTopologyTable": ibmappnNnTopologyTable,
       "ibmappnNnTopologyEntry": ibmappnNnTopologyEntry,
       "ibmappnNnNodeName": ibmappnNnNodeName,
       "ibmappnNnNodeFrsn": ibmappnNnNodeFrsn,
       "ibmappnNnNodeEntryTimeLeft": ibmappnNnNodeEntryTimeLeft,
       "ibmappnNnNodeType": ibmappnNnNodeType,
       "ibmappnNnNodeRsn": ibmappnNnNodeRsn,
       "ibmappnNnNodeRouteAddResist": ibmappnNnNodeRouteAddResist,
       "ibmappnNnNodeCongested": ibmappnNnNodeCongested,
       "ibmappnNnNodeIsrDepleted": ibmappnNnNodeIsrDepleted,
       "ibmappnNnNodeEndptDepleted": ibmappnNnNodeEndptDepleted,
       "ibmappnNnNodeQuiescing": ibmappnNnNodeQuiescing,
       "ibmappnNnNodeGateway": ibmappnNnNodeGateway,
       "ibmappnNnNodeCentralDirectory": ibmappnNnNodeCentralDirectory,
       "ibmappnNnNodeIsr": ibmappnNnNodeIsr,
       "ibmappnNnNodeChainSupport": ibmappnNnNodeChainSupport,
       "ibmappnNnTgTopologyTable": ibmappnNnTgTopologyTable,
       "ibmappnNnTgTopologyEntry": ibmappnNnTgTopologyEntry,
       "ibmappnNnTgOwner": ibmappnNnTgOwner,
       "ibmappnNnTgDest": ibmappnNnTgDest,
       "ibmappnNnTgNum": ibmappnNnTgNum,
       "ibmappnNnTgFrsn": ibmappnNnTgFrsn,
       "ibmappnNnTgEntryTimeLeft": ibmappnNnTgEntryTimeLeft,
       "ibmappnNnTgDestVirtual": ibmappnNnTgDestVirtual,
       "ibmappnNnTgDlcData": ibmappnNnTgDlcData,
       "ibmappnNnTgRsn": ibmappnNnTgRsn,
       "ibmappnNnTgOperational": ibmappnNnTgOperational,
       "ibmappnNnTgQuiescing": ibmappnNnTgQuiescing,
       "ibmappnNnTgCpCpSession": ibmappnNnTgCpCpSession,
       "ibmappnNnTgEffCap": ibmappnNnTgEffCap,
       "ibmappnNnTgConnCost": ibmappnNnTgConnCost,
       "ibmappnNnTgByteCost": ibmappnNnTgByteCost,
       "ibmappnNnTgSecurity": ibmappnNnTgSecurity,
       "ibmappnNnTgDelay": ibmappnNnTgDelay,
       "ibmappnNnTgModemClass": ibmappnNnTgModemClass,
       "ibmappnNnTgUsr1": ibmappnNnTgUsr1,
       "ibmappnNnTgUsr2": ibmappnNnTgUsr2,
       "ibmappnNnTgUsr3": ibmappnNnTgUsr3,
       "ibmappnNnTopologyFRTable": ibmappnNnTopologyFRTable,
       "ibmappnNnTopologyFREntry": ibmappnNnTopologyFREntry,
       "ibmappnNnNodeFRName": ibmappnNnNodeFRName,
       "ibmappnNnNodeFRFrsn": ibmappnNnNodeFRFrsn,
       "ibmappnNnNodeFREntryTimeLeft": ibmappnNnNodeFREntryTimeLeft,
       "ibmappnNnNodeFRType": ibmappnNnNodeFRType,
       "ibmappnNnNodeFRRsn": ibmappnNnNodeFRRsn,
       "ibmappnNnNodeFRRouteAddResist": ibmappnNnNodeFRRouteAddResist,
       "ibmappnNnNodeFRCongested": ibmappnNnNodeFRCongested,
       "ibmappnNnNodeFRIsrDepleted": ibmappnNnNodeFRIsrDepleted,
       "ibmappnNnNodeFREndptDepleted": ibmappnNnNodeFREndptDepleted,
       "ibmappnNnNodeFRQuiescing": ibmappnNnNodeFRQuiescing,
       "ibmappnNnNodeFRGateway": ibmappnNnNodeFRGateway,
       "ibmappnNnNodeFRCentralDirectory": ibmappnNnNodeFRCentralDirectory,
       "ibmappnNnNodeFRIsr": ibmappnNnNodeFRIsr,
       "ibmappnNnNodeFRChainSupport": ibmappnNnNodeFRChainSupport,
       "ibmappnNnTgTopologyFRTable": ibmappnNnTgTopologyFRTable,
       "ibmappnNnTgTopologyFREntry": ibmappnNnTgTopologyFREntry,
       "ibmappnNnTgFROwner": ibmappnNnTgFROwner,
       "ibmappnNnTgFRDest": ibmappnNnTgFRDest,
       "ibmappnNnTgFRNum": ibmappnNnTgFRNum,
       "ibmappnNnTgFRFrsn": ibmappnNnTgFRFrsn,
       "ibmappnNnTgFREntryTimeLeft": ibmappnNnTgFREntryTimeLeft,
       "ibmappnNnTgFRDestVirtual": ibmappnNnTgFRDestVirtual,
       "ibmappnNnTgFRDlcData": ibmappnNnTgFRDlcData,
       "ibmappnNnTgFRRsn": ibmappnNnTgFRRsn,
       "ibmappnNnTgFROperational": ibmappnNnTgFROperational,
       "ibmappnNnTgFRQuiescing": ibmappnNnTgFRQuiescing,
       "ibmappnNnTgFRCpCpSession": ibmappnNnTgFRCpCpSession,
       "ibmappnNnTgFREffCap": ibmappnNnTgFREffCap,
       "ibmappnNnTgFRConnCost": ibmappnNnTgFRConnCost,
       "ibmappnNnTgFRByteCost": ibmappnNnTgFRByteCost,
       "ibmappnNnTgFRSecurity": ibmappnNnTgFRSecurity,
       "ibmappnNnTgFRDelay": ibmappnNnTgFRDelay,
       "ibmappnNnTgFRModemClass": ibmappnNnTgFRModemClass,
       "ibmappnNnTgFRUsr1": ibmappnNnTgFRUsr1,
       "ibmappnNnTgFRUsr2": ibmappnNnTgFRUsr2,
       "ibmappnNnTgFRUsr3": ibmappnNnTgFRUsr3,
       "ibmappnLocalTopology": ibmappnLocalTopology,
       "ibmappnLocalThisNode": ibmappnLocalThisNode,
       "ibmappnLocalGeneral": ibmappnLocalGeneral,
       "ibmappnLocalNodeName": ibmappnLocalNodeName,
       "ibmappnLocalNodeType": ibmappnLocalNodeType,
       "ibmappnLocalNnSpecific": ibmappnLocalNnSpecific,
       "ibmappnLocalNnRsn": ibmappnLocalNnRsn,
       "ibmappnLocalNnRouteAddResist": ibmappnLocalNnRouteAddResist,
       "ibmappnLocalNnCongested": ibmappnLocalNnCongested,
       "ibmappnLocalNnIsrDepleted": ibmappnLocalNnIsrDepleted,
       "ibmappnLocalNnEndptDepleted": ibmappnLocalNnEndptDepleted,
       "ibmappnLocalNnQuiescing": ibmappnLocalNnQuiescing,
       "ibmappnLocalNnGateway": ibmappnLocalNnGateway,
       "ibmappnLocalNnCentralDirectory": ibmappnLocalNnCentralDirectory,
       "ibmappnLocalNnIsr": ibmappnLocalNnIsr,
       "ibmappnLocalNnChainSupport": ibmappnLocalNnChainSupport,
       "ibmappnLocalNnFrsn": ibmappnLocalNnFrsn,
       "ibmappnLocalTg": ibmappnLocalTg,
       "ibmappnLocalTgTable": ibmappnLocalTgTable,
       "ibmappnLocalTgEntry": ibmappnLocalTgEntry,
       "ibmappnLocalTgDest": ibmappnLocalTgDest,
       "ibmappnLocalTgNum": ibmappnLocalTgNum,
       "ibmappnLocalTgDestVirtual": ibmappnLocalTgDestVirtual,
       "ibmappnLocalTgDlcData": ibmappnLocalTgDlcData,
       "ibmappnLocalTgRsn": ibmappnLocalTgRsn,
       "ibmappnLocalTgQuiescing": ibmappnLocalTgQuiescing,
       "ibmappnLocalTgOperational": ibmappnLocalTgOperational,
       "ibmappnLocalTgCpCpSession": ibmappnLocalTgCpCpSession,
       "ibmappnLocalTgEffCap": ibmappnLocalTgEffCap,
       "ibmappnLocalTgConnCost": ibmappnLocalTgConnCost,
       "ibmappnLocalTgByteCost": ibmappnLocalTgByteCost,
       "ibmappnLocalTgSecurity": ibmappnLocalTgSecurity,
       "ibmappnLocalTgDelay": ibmappnLocalTgDelay,
       "ibmappnLocalTgModemClass": ibmappnLocalTgModemClass,
       "ibmappnLocalTgUsr1": ibmappnLocalTgUsr1,
       "ibmappnLocalTgUsr2": ibmappnLocalTgUsr2,
       "ibmappnLocalTgUsr3": ibmappnLocalTgUsr3,
       "ibmappnLocalEnTopology": ibmappnLocalEnTopology,
       "ibmappnLocalEnTable": ibmappnLocalEnTable,
       "ibmappnLocalEnEntry": ibmappnLocalEnEntry,
       "ibmappnLocalEnName": ibmappnLocalEnName,
       "ibmappnLocalEnEntryTimeLeft": ibmappnLocalEnEntryTimeLeft,
       "ibmappnLocalEnType": ibmappnLocalEnType,
       "ibmappnLocalEnTgTable": ibmappnLocalEnTgTable,
       "ibmappnLocalEnTgEntry": ibmappnLocalEnTgEntry,
       "ibmappnLocalEnTgOrigin": ibmappnLocalEnTgOrigin,
       "ibmappnLocalEnTgDest": ibmappnLocalEnTgDest,
       "ibmappnLocalEnTgNum": ibmappnLocalEnTgNum,
       "ibmappnLocalEnTgEntryTimeLeft": ibmappnLocalEnTgEntryTimeLeft,
       "ibmappnLocalEnTgDestVirtual": ibmappnLocalEnTgDestVirtual,
       "ibmappnLocalEnTgDlcData": ibmappnLocalEnTgDlcData,
       "ibmappnLocalEnTgOperational": ibmappnLocalEnTgOperational,
       "ibmappnLocalEnTgCpCpSession": ibmappnLocalEnTgCpCpSession,
       "ibmappnLocalEnTgEffCap": ibmappnLocalEnTgEffCap,
       "ibmappnLocalEnTgConnCost": ibmappnLocalEnTgConnCost,
       "ibmappnLocalEnTgByteCost": ibmappnLocalEnTgByteCost,
       "ibmappnLocalEnTgSecurity": ibmappnLocalEnTgSecurity,
       "ibmappnLocalEnTgDelay": ibmappnLocalEnTgDelay,
       "ibmappnLocalEnTgModemClass": ibmappnLocalEnTgModemClass,
       "ibmappnLocalEnTgUsr1": ibmappnLocalEnTgUsr1,
       "ibmappnLocalEnTgUsr2": ibmappnLocalEnTgUsr2,
       "ibmappnLocalEnTgUsr3": ibmappnLocalEnTgUsr3,
       "ibmappnDir": ibmappnDir,
       "ibmappnDirPerf": ibmappnDirPerf,
       "ibmappnDirMaxCaches": ibmappnDirMaxCaches,
       "ibmappnDirCurCaches": ibmappnDirCurCaches,
       "ibmappnDirCurHomeEntries": ibmappnDirCurHomeEntries,
       "ibmappnDirRegEntries": ibmappnDirRegEntries,
       "ibmappnDirInLocates": ibmappnDirInLocates,
       "ibmappnDirInBcastLocates": ibmappnDirInBcastLocates,
       "ibmappnDirOutLocates": ibmappnDirOutLocates,
       "ibmappnDirOutBcastLocates": ibmappnDirOutBcastLocates,
       "ibmappnDirNotFoundLocates": ibmappnDirNotFoundLocates,
       "ibmappnDirNotFoundBcastLocates": ibmappnDirNotFoundBcastLocates,
       "ibmappnDirLocateOutstands": ibmappnDirLocateOutstands,
       "ibmappnDirTable": ibmappnDirTable,
       "ibmappnDirEntry": ibmappnDirEntry,
       "ibmappnDirLuName": ibmappnDirLuName,
       "ibmappnDirServerName": ibmappnDirServerName,
       "ibmappnDirLuOwnerName": ibmappnDirLuOwnerName,
       "ibmappnDirLuLocation": ibmappnDirLuLocation,
       "ibmappnDirType": ibmappnDirType,
       "ibmappnDirWildCard": ibmappnDirWildCard,
       "ibmappnCos": ibmappnCos,
       "ibmappnCosModeTable": ibmappnCosModeTable,
       "ibmappnCosModeEntry": ibmappnCosModeEntry,
       "ibmappnCosModeName": ibmappnCosModeName,
       "ibmappnCosModeCosName": ibmappnCosModeCosName,
       "ibmappnCosNameTable": ibmappnCosNameTable,
       "ibmappnCosNameEntry": ibmappnCosNameEntry,
       "ibmappnCosName": ibmappnCosName,
       "ibmappnCosTransPriority": ibmappnCosTransPriority,
       "ibmappnCosNodeRowTable": ibmappnCosNodeRowTable,
       "ibmappnCosNodeRowEntry": ibmappnCosNodeRowEntry,
       "ibmappnCosNodeRowName": ibmappnCosNodeRowName,
       "ibmappnCosNodeRowIndex": ibmappnCosNodeRowIndex,
       "ibmappnCosNodeRowWgt": ibmappnCosNodeRowWgt,
       "ibmappnCosNodeRowResistMin": ibmappnCosNodeRowResistMin,
       "ibmappnCosNodeRowResistMax": ibmappnCosNodeRowResistMax,
       "ibmappnCosNodeRowMinCongestAllow": ibmappnCosNodeRowMinCongestAllow,
       "ibmappnCosNodeRowMaxCongestAllow": ibmappnCosNodeRowMaxCongestAllow,
       "ibmappnCosTgRowTable": ibmappnCosTgRowTable,
       "ibmappnCosTgRowEntry": ibmappnCosTgRowEntry,
       "ibmappnCosTgRowName": ibmappnCosTgRowName,
       "ibmappnCosTgRowIndex": ibmappnCosTgRowIndex,
       "ibmappnCosTgRowWgt": ibmappnCosTgRowWgt,
       "ibmappnCosTgRowEffCapMin": ibmappnCosTgRowEffCapMin,
       "ibmappnCosTgRowEffCapMax": ibmappnCosTgRowEffCapMax,
       "ibmappnCosTgRowConnCostMin": ibmappnCosTgRowConnCostMin,
       "ibmappnCosTgRowConnCostMax": ibmappnCosTgRowConnCostMax,
       "ibmappnCosTgRowByteCostMin": ibmappnCosTgRowByteCostMin,
       "ibmappnCosTgRowByteCostMax": ibmappnCosTgRowByteCostMax,
       "ibmappnCosTgRowSecurityMin": ibmappnCosTgRowSecurityMin,
       "ibmappnCosTgRowSecurityMax": ibmappnCosTgRowSecurityMax,
       "ibmappnCosTgRowDelayMin": ibmappnCosTgRowDelayMin,
       "ibmappnCosTgRowDelayMax": ibmappnCosTgRowDelayMax,
       "ibmappnCosTgRowUsr1Min": ibmappnCosTgRowUsr1Min,
       "ibmappnCosTgRowUsr1Max": ibmappnCosTgRowUsr1Max,
       "ibmappnCosTgRowUsr2Min": ibmappnCosTgRowUsr2Min,
       "ibmappnCosTgRowUsr2Max": ibmappnCosTgRowUsr2Max,
       "ibmappnCosTgRowUsr3Min": ibmappnCosTgRowUsr3Min,
       "ibmappnCosTgRowUsr3Max": ibmappnCosTgRowUsr3Max}
)
