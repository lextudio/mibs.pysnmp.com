# SNMP MIB module (XYLANPNNI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLANPNNI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:21 2024
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(xylanPnni,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanPnni")


# MODULE-IDENTITY

xylanPnniMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2)
)


# Types definitions



class XPnniNodeId(OctetString):
    """Custom type XPnniNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )





class XPnniNodeLevel(Integer32):
    """Custom type XPnniNodeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 104),
    )





class XPnniAtmAddr(OctetString):
    """Custom type XPnniAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )





class XPnniPortId(Unsigned32):
    """Custom type XPnniPortId based on Unsigned32"""




class XPnniFiltCallType(Integer32):
    """Custom type XPnniFiltCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both-ptop-pmp", 0),
          ("pmp", 2),
          ("ptop", 1))
    )





class XPnniFiltServiceCategory(Integer32):
    """Custom type XPnniFiltServiceCategory based on Integer32"""
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
        *(("abr", 3),
          ("cbr", 1),
          ("none-specified", 0),
          ("rtVbr", 2))
    )





class XPnniFiltMetricConstraint(Integer32):
    """Custom type XPnniFiltMetricConstraint based on Integer32"""
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
        *(("max-burst", 4),
          ("min-cr", 2),
          ("none-specified", 0),
          ("pcr", 1),
          ("scr", 3))
    )





class XPnniFiltExceptionCriteria(Integer32):
    """Custom type XPnniFiltExceptionCriteria based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-addrs-pass-except", 1),
          ("no-addrs-pass-except", 2),
          ("none-specified", 0))
    )





class XPnniFilterPrefixLength(Integer32):
    """Custom type XPnniFilterPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 152),
    )





class XPnniAddrPrefix(OctetString):
    """Custom type XPnniAddrPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanPnniMIBExtens_ObjectIdentity = ObjectIdentity
xylanPnniMIBExtens = _XylanPnniMIBExtens_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1)
)
_XylanPnniMIBObjs_ObjectIdentity = ObjectIdentity
xylanPnniMIBObjs = _XylanPnniMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1)
)
_XPnniAssociativeNameTable_Object = MibTable
xPnniAssociativeNameTable = _XPnniAssociativeNameTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xPnniAssociativeNameTable.setStatus("mandatory")
_XPnniNameEntry_Object = MibTableRow
xPnniNameEntry = _XPnniNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 1, 1)
)
xPnniNameEntry.setIndexNames(
    (0, "XYLANPNNI-MIB", "xPnniNodeIndex"),
)
if mibBuilder.loadTexts:
    xPnniNameEntry.setStatus("mandatory")


class _XPnniNodeIndex_Type(Integer32):
    """Custom type xPnniNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_XPnniNodeIndex_Type.__name__ = "Integer32"
_XPnniNodeIndex_Object = MibTableColumn
xPnniNodeIndex = _XPnniNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 1, 1, 1),
    _XPnniNodeIndex_Type()
)
xPnniNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniNodeIndex.setStatus("mandatory")
_XPnniNodeId_Type = XPnniNodeId
_XPnniNodeId_Object = MibTableColumn
xPnniNodeId = _XPnniNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 1, 1, 2),
    _XPnniNodeId_Type()
)
xPnniNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniNodeId.setStatus("mandatory")
_XPnniNodeName_Type = DisplayString
_XPnniNodeName_Object = MibTableColumn
xPnniNodeName = _XPnniNodeName_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 1, 1, 3),
    _XPnniNodeName_Type()
)
xPnniNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniNodeName.setStatus("mandatory")
_XPnniAddressFilterTable_Object = MibTable
xPnniAddressFilterTable = _XPnniAddressFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xPnniAddressFilterTable.setStatus("mandatory")
_XPnniAddressFilterEntry_Object = MibTableRow
xPnniAddressFilterEntry = _XPnniAddressFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1)
)
xPnniAddressFilterEntry.setIndexNames(
    (0, "XYLANPNNI-MIB", "xPnniFiltIndex"),
)
if mibBuilder.loadTexts:
    xPnniAddressFilterEntry.setStatus("mandatory")
_XPnniFiltIndex_Type = Integer32
_XPnniFiltIndex_Object = MibTableColumn
xPnniFiltIndex = _XPnniFiltIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 1),
    _XPnniFiltIndex_Type()
)
xPnniFiltIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltIndex.setStatus("mandatory")


class _XPnniFiltNodeLevel_Type(XPnniNodeLevel):
    """Custom type xPnniFiltNodeLevel based on XPnniNodeLevel"""
    defaultValue = 80


_XPnniFiltNodeLevel_Object = MibTableColumn
xPnniFiltNodeLevel = _XPnniFiltNodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 2),
    _XPnniFiltNodeLevel_Type()
)
xPnniFiltNodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltNodeLevel.setStatus("mandatory")


class _XPnniFiltSrcPrefLen_Type(XPnniFilterPrefixLength):
    """Custom type xPnniFiltSrcPrefLen based on XPnniFilterPrefixLength"""
    defaultValue = 0


_XPnniFiltSrcPrefLen_Object = MibTableColumn
xPnniFiltSrcPrefLen = _XPnniFiltSrcPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 3),
    _XPnniFiltSrcPrefLen_Type()
)
xPnniFiltSrcPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltSrcPrefLen.setStatus("mandatory")
_XPnniFiltSrcPrefix_Type = XPnniAddrPrefix
_XPnniFiltSrcPrefix_Object = MibTableColumn
xPnniFiltSrcPrefix = _XPnniFiltSrcPrefix_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 4),
    _XPnniFiltSrcPrefix_Type()
)
xPnniFiltSrcPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltSrcPrefix.setStatus("mandatory")


class _XPnniFiltDestPrefLen_Type(XPnniFilterPrefixLength):
    """Custom type xPnniFiltDestPrefLen based on XPnniFilterPrefixLength"""
    defaultValue = 0


_XPnniFiltDestPrefLen_Object = MibTableColumn
xPnniFiltDestPrefLen = _XPnniFiltDestPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 5),
    _XPnniFiltDestPrefLen_Type()
)
xPnniFiltDestPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltDestPrefLen.setStatus("mandatory")
_XPnniFiltDestPrefix_Type = XPnniAddrPrefix
_XPnniFiltDestPrefix_Object = MibTableColumn
xPnniFiltDestPrefix = _XPnniFiltDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 6),
    _XPnniFiltDestPrefix_Type()
)
xPnniFiltDestPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltDestPrefix.setStatus("mandatory")


class _XPnniFiltCallType_Type(XPnniFiltCallType):
    """Custom type xPnniFiltCallType based on XPnniFiltCallType"""


_XPnniFiltCallType_Object = MibTableColumn
xPnniFiltCallType = _XPnniFiltCallType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 7),
    _XPnniFiltCallType_Type()
)
xPnniFiltCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltCallType.setStatus("mandatory")


class _XPnniFiltCallSrvCls_Type(XPnniFiltServiceCategory):
    """Custom type xPnniFiltCallSrvCls based on XPnniFiltServiceCategory"""


_XPnniFiltCallSrvCls_Object = MibTableColumn
xPnniFiltCallSrvCls = _XPnniFiltCallSrvCls_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 8),
    _XPnniFiltCallSrvCls_Type()
)
xPnniFiltCallSrvCls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltCallSrvCls.setStatus("mandatory")


class _XPnniFiltCallMtrcConstrnt_Type(XPnniFiltMetricConstraint):
    """Custom type xPnniFiltCallMtrcConstrnt based on XPnniFiltMetricConstraint"""


_XPnniFiltCallMtrcConstrnt_Object = MibTableColumn
xPnniFiltCallMtrcConstrnt = _XPnniFiltCallMtrcConstrnt_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 9),
    _XPnniFiltCallMtrcConstrnt_Type()
)
xPnniFiltCallMtrcConstrnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltCallMtrcConstrnt.setStatus("mandatory")
_XPnniFiltCallMtrcThresh_Type = Integer32
_XPnniFiltCallMtrcThresh_Object = MibTableColumn
xPnniFiltCallMtrcThresh = _XPnniFiltCallMtrcThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 10),
    _XPnniFiltCallMtrcThresh_Type()
)
xPnniFiltCallMtrcThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltCallMtrcThresh.setStatus("mandatory")


class _XPnniFiltTrapThresh_Type(Integer32):
    """Custom type xPnniFiltTrapThresh based on Integer32"""
    defaultValue = 0


_XPnniFiltTrapThresh_Object = MibTableColumn
xPnniFiltTrapThresh = _XPnniFiltTrapThresh_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 11),
    _XPnniFiltTrapThresh_Type()
)
xPnniFiltTrapThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltTrapThresh.setStatus("mandatory")


class _XPnniFiltSrcExceptionCriteria_Type(XPnniFiltExceptionCriteria):
    """Custom type xPnniFiltSrcExceptionCriteria based on XPnniFiltExceptionCriteria"""


_XPnniFiltSrcExceptionCriteria_Object = MibTableColumn
xPnniFiltSrcExceptionCriteria = _XPnniFiltSrcExceptionCriteria_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 12),
    _XPnniFiltSrcExceptionCriteria_Type()
)
xPnniFiltSrcExceptionCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltSrcExceptionCriteria.setStatus("mandatory")
_XPnniFiltSrcExceptionLen_Type = XPnniFilterPrefixLength
_XPnniFiltSrcExceptionLen_Object = MibTableColumn
xPnniFiltSrcExceptionLen = _XPnniFiltSrcExceptionLen_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 13),
    _XPnniFiltSrcExceptionLen_Type()
)
xPnniFiltSrcExceptionLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltSrcExceptionLen.setStatus("mandatory")
_XPnniFiltSrcException_Type = XPnniAddrPrefix
_XPnniFiltSrcException_Object = MibTableColumn
xPnniFiltSrcException = _XPnniFiltSrcException_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 14),
    _XPnniFiltSrcException_Type()
)
xPnniFiltSrcException.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltSrcException.setStatus("mandatory")


class _XPnniFiltDestExceptionCriteria_Type(XPnniFiltExceptionCriteria):
    """Custom type xPnniFiltDestExceptionCriteria based on XPnniFiltExceptionCriteria"""


_XPnniFiltDestExceptionCriteria_Object = MibTableColumn
xPnniFiltDestExceptionCriteria = _XPnniFiltDestExceptionCriteria_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 15),
    _XPnniFiltDestExceptionCriteria_Type()
)
xPnniFiltDestExceptionCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltDestExceptionCriteria.setStatus("mandatory")
_XPnniFiltDestExceptionLen_Type = XPnniFilterPrefixLength
_XPnniFiltDestExceptionLen_Object = MibTableColumn
xPnniFiltDestExceptionLen = _XPnniFiltDestExceptionLen_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 16),
    _XPnniFiltDestExceptionLen_Type()
)
xPnniFiltDestExceptionLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltDestExceptionLen.setStatus("mandatory")
_XPnniFiltDestException_Type = XPnniAddrPrefix
_XPnniFiltDestException_Object = MibTableColumn
xPnniFiltDestException = _XPnniFiltDestException_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 17),
    _XPnniFiltDestException_Type()
)
xPnniFiltDestException.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltDestException.setStatus("mandatory")
_XPnniFiltDeniedHitCount_Type = Counter32
_XPnniFiltDeniedHitCount_Object = MibTableColumn
xPnniFiltDeniedHitCount = _XPnniFiltDeniedHitCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 18),
    _XPnniFiltDeniedHitCount_Type()
)
xPnniFiltDeniedHitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltDeniedHitCount.setStatus("mandatory")
_XPnniFiltExceptionHitCount_Type = Counter32
_XPnniFiltExceptionHitCount_Object = MibTableColumn
xPnniFiltExceptionHitCount = _XPnniFiltExceptionHitCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 19),
    _XPnniFiltExceptionHitCount_Type()
)
xPnniFiltExceptionHitCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltExceptionHitCount.setStatus("mandatory")


class _XPnniFiltTODStartHr_Type(Integer32):
    """Custom type xPnniFiltTODStartHr based on Integer32"""
    defaultValue = 0


_XPnniFiltTODStartHr_Object = MibTableColumn
xPnniFiltTODStartHr = _XPnniFiltTODStartHr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 20),
    _XPnniFiltTODStartHr_Type()
)
xPnniFiltTODStartHr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltTODStartHr.setStatus("mandatory")


class _XPnniFiltTODStartMin_Type(Integer32):
    """Custom type xPnniFiltTODStartMin based on Integer32"""
    defaultValue = 0


_XPnniFiltTODStartMin_Object = MibTableColumn
xPnniFiltTODStartMin = _XPnniFiltTODStartMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 21),
    _XPnniFiltTODStartMin_Type()
)
xPnniFiltTODStartMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltTODStartMin.setStatus("mandatory")


class _XPnniFiltTODStartSec_Type(Integer32):
    """Custom type xPnniFiltTODStartSec based on Integer32"""
    defaultValue = 0


_XPnniFiltTODStartSec_Object = MibTableColumn
xPnniFiltTODStartSec = _XPnniFiltTODStartSec_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 22),
    _XPnniFiltTODStartSec_Type()
)
xPnniFiltTODStartSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltTODStartSec.setStatus("mandatory")


class _XPnniFiltTODStopHr_Type(Integer32):
    """Custom type xPnniFiltTODStopHr based on Integer32"""
    defaultValue = 0


_XPnniFiltTODStopHr_Object = MibTableColumn
xPnniFiltTODStopHr = _XPnniFiltTODStopHr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 23),
    _XPnniFiltTODStopHr_Type()
)
xPnniFiltTODStopHr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltTODStopHr.setStatus("mandatory")


class _XPnniFiltTODStopMin_Type(Integer32):
    """Custom type xPnniFiltTODStopMin based on Integer32"""
    defaultValue = 0


_XPnniFiltTODStopMin_Object = MibTableColumn
xPnniFiltTODStopMin = _XPnniFiltTODStopMin_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 24),
    _XPnniFiltTODStopMin_Type()
)
xPnniFiltTODStopMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltTODStopMin.setStatus("mandatory")


class _XPnniFiltTODStopSec_Type(Integer32):
    """Custom type xPnniFiltTODStopSec based on Integer32"""
    defaultValue = 0


_XPnniFiltTODStopSec_Object = MibTableColumn
xPnniFiltTODStopSec = _XPnniFiltTODStopSec_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 2, 1, 25),
    _XPnniFiltTODStopSec_Type()
)
xPnniFiltTODStopSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniFiltTODStopSec.setStatus("mandatory")
_XPnniIAdjMIBObjects_ObjectIdentity = ObjectIdentity
xPnniIAdjMIBObjects = _XPnniIAdjMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3)
)
_XPnniIAdjGroup_ObjectIdentity = ObjectIdentity
xPnniIAdjGroup = _XPnniIAdjGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1)
)
_XPnniNumIAdj_Type = Counter32
_XPnniNumIAdj_Object = MibScalar
xPnniNumIAdj = _XPnniNumIAdj_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 1),
    _XPnniNumIAdj_Type()
)
xPnniNumIAdj.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniNumIAdj.setStatus("mandatory")
_XPnniIAdjTable_Object = MibTable
xPnniIAdjTable = _XPnniIAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xPnniIAdjTable.setStatus("mandatory")
_XPnniIAdjEntry_Object = MibTableRow
xPnniIAdjEntry = _XPnniIAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1)
)
xPnniIAdjEntry.setIndexNames(
    (0, "XYLANPNNI-MIB", "xPnniIAdjIndex"),
)
if mibBuilder.loadTexts:
    xPnniIAdjEntry.setStatus("mandatory")
_XPnniIAdjIndex_Type = Integer32
_XPnniIAdjIndex_Object = MibTableColumn
xPnniIAdjIndex = _XPnniIAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 1),
    _XPnniIAdjIndex_Type()
)
xPnniIAdjIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xPnniIAdjIndex.setStatus("mandatory")
_XPnniIAdjAtmAddress_Type = XPnniAtmAddr
_XPnniIAdjAtmAddress_Object = MibTableColumn
xPnniIAdjAtmAddress = _XPnniIAdjAtmAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 2),
    _XPnniIAdjAtmAddress_Type()
)
xPnniIAdjAtmAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjAtmAddress.setStatus("mandatory")
_XPnniIAdjSlot_Type = Integer32
_XPnniIAdjSlot_Object = MibTableColumn
xPnniIAdjSlot = _XPnniIAdjSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 3),
    _XPnniIAdjSlot_Type()
)
xPnniIAdjSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjSlot.setStatus("mandatory")
_XPnniIAdjPort_Type = Integer32
_XPnniIAdjPort_Object = MibTableColumn
xPnniIAdjPort = _XPnniIAdjPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 4),
    _XPnniIAdjPort_Type()
)
xPnniIAdjPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjPort.setStatus("mandatory")
_XPnniIAdjInst_Type = Integer32
_XPnniIAdjInst_Object = MibTableColumn
xPnniIAdjInst = _XPnniIAdjInst_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 5),
    _XPnniIAdjInst_Type()
)
xPnniIAdjInst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjInst.setStatus("mandatory")
_XPnniIAdjCsmPPort_Type = Integer32
_XPnniIAdjCsmPPort_Object = MibTableColumn
xPnniIAdjCsmPPort = _XPnniIAdjCsmPPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 6),
    _XPnniIAdjCsmPPort_Type()
)
xPnniIAdjCsmPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjCsmPPort.setStatus("mandatory")
_XPnniIAdjAdvertised_Type = TruthValue
_XPnniIAdjAdvertised_Object = MibTableColumn
xPnniIAdjAdvertised = _XPnniIAdjAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 7),
    _XPnniIAdjAdvertised_Type()
)
xPnniIAdjAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjAdvertised.setStatus("mandatory")
_XPnniIAdjSummarized_Type = TruthValue
_XPnniIAdjSummarized_Object = MibTableColumn
xPnniIAdjSummarized = _XPnniIAdjSummarized_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 8),
    _XPnniIAdjSummarized_Type()
)
xPnniIAdjSummarized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjSummarized.setStatus("mandatory")
_XPnniIAdjLearned_Type = DisplayString
_XPnniIAdjLearned_Object = MibTableColumn
xPnniIAdjLearned = _XPnniIAdjLearned_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 3, 1, 2, 1, 9),
    _XPnniIAdjLearned_Type()
)
xPnniIAdjLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniIAdjLearned.setStatus("mandatory")
_XPnniTestMIBObjects_ObjectIdentity = ObjectIdentity
xPnniTestMIBObjects = _XPnniTestMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4)
)
_XPnniRtstMIBGroup_ObjectIdentity = ObjectIdentity
xPnniRtstMIBGroup = _XPnniRtstMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1)
)
_XPnniRtstTable_Object = MibTable
xPnniRtstTable = _XPnniRtstTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xPnniRtstTable.setStatus("mandatory")
_XPnniRtstEntry_Object = MibTableRow
xPnniRtstEntry = _XPnniRtstEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1)
)
xPnniRtstEntry.setIndexNames(
    (0, "XYLANPNNI-MIB", "xPnniNodeIndex"),
    (0, "XYLANPNNI-MIB", "xPnniRtstClass"),
    (0, "XYLANPNNI-MIB", "xPnniRtstType"),
    (0, "XYLANPNNI-MIB", "xPnniRtstDest"),
)
if mibBuilder.loadTexts:
    xPnniRtstEntry.setStatus("mandatory")


class _XPnniRtstClass_Type(Integer32):
    """Custom type xPnniRtstClass based on Integer32"""
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
        *(("abr", 5),
          ("cbr", 2),
          ("ubr", 1),
          ("vbrNrt", 4),
          ("vbrRt", 3))
    )


_XPnniRtstClass_Type.__name__ = "Integer32"
_XPnniRtstClass_Object = MibTableColumn
xPnniRtstClass = _XPnniRtstClass_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 1),
    _XPnniRtstClass_Type()
)
xPnniRtstClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xPnniRtstClass.setStatus("mandatory")


class _XPnniRtstType_Type(Integer32):
    """Custom type xPnniRtstType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pmp", 2),
          ("ptpt", 1))
    )


_XPnniRtstType_Type.__name__ = "Integer32"
_XPnniRtstType_Object = MibTableColumn
xPnniRtstType = _XPnniRtstType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 2),
    _XPnniRtstType_Type()
)
xPnniRtstType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xPnniRtstType.setStatus("mandatory")


class _XPnniRtstDest_Type(OctetString):
    """Custom type xPnniRtstDest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_XPnniRtstDest_Type.__name__ = "OctetString"
_XPnniRtstDest_Object = MibTableColumn
xPnniRtstDest = _XPnniRtstDest_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 3),
    _XPnniRtstDest_Type()
)
xPnniRtstDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xPnniRtstDest.setStatus("mandatory")


class _XPnniRtstError_Type(Integer32):
    """Custom type xPnniRtstError based on Integer32"""
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
        *(("dtlExhaustion", 2),
          ("noRouteToDest", 1),
          ("other", 3),
          ("success", 0))
    )


_XPnniRtstError_Type.__name__ = "Integer32"
_XPnniRtstError_Object = MibTableColumn
xPnniRtstError = _XPnniRtstError_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 4),
    _XPnniRtstError_Type()
)
xPnniRtstError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstError.setStatus("mandatory")


class _XPnniRtstFlags_Type(Integer32):
    """Custom type xPnniRtstFlags based on Integer32"""
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
        *(("direct", 2),
          ("directEreach", 4),
          ("dtlAdded", 1),
          ("myself", 3))
    )


_XPnniRtstFlags_Type.__name__ = "Integer32"
_XPnniRtstFlags_Object = MibTableColumn
xPnniRtstFlags = _XPnniRtstFlags_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 5),
    _XPnniRtstFlags_Type()
)
xPnniRtstFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstFlags.setStatus("mandatory")
_XPnniRtstOutboundPort_Type = XPnniPortId
_XPnniRtstOutboundPort_Object = MibTableColumn
xPnniRtstOutboundPort = _XPnniRtstOutboundPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 6),
    _XPnniRtstOutboundPort_Type()
)
xPnniRtstOutboundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstOutboundPort.setStatus("mandatory")
_XPnniRtstVPI_Type = Integer32
_XPnniRtstVPI_Object = MibTableColumn
xPnniRtstVPI = _XPnniRtstVPI_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 7),
    _XPnniRtstVPI_Type()
)
xPnniRtstVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstVPI.setStatus("mandatory")


class _XPnniRtstE164_Type(OctetString):
    """Custom type xPnniRtstE164 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_XPnniRtstE164_Type.__name__ = "OctetString"
_XPnniRtstE164_Object = MibTableColumn
xPnniRtstE164 = _XPnniRtstE164_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 8),
    _XPnniRtstE164_Type()
)
xPnniRtstE164.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstE164.setStatus("mandatory")
_XPnniRtstE164len_Type = Integer32
_XPnniRtstE164len_Object = MibTableColumn
xPnniRtstE164len = _XPnniRtstE164len_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 9),
    _XPnniRtstE164len_Type()
)
xPnniRtstE164len.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstE164len.setStatus("mandatory")


class _XPnniRtstHopCount_Type(Integer32):
    """Custom type xPnniRtstHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_XPnniRtstHopCount_Type.__name__ = "Integer32"
_XPnniRtstHopCount_Object = MibTableColumn
xPnniRtstHopCount = _XPnniRtstHopCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 10),
    _XPnniRtstHopCount_Type()
)
xPnniRtstHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstHopCount.setStatus("mandatory")


class _XPnniRtstDTL_Type(OctetString):
    """Custom type xPnniRtstDTL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(52, 1500),
    )


_XPnniRtstDTL_Type.__name__ = "OctetString"
_XPnniRtstDTL_Object = MibTableColumn
xPnniRtstDTL = _XPnniRtstDTL_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 11),
    _XPnniRtstDTL_Type()
)
xPnniRtstDTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstDTL.setStatus("mandatory")
_XPnniRtstCurPointer_Type = Integer32
_XPnniRtstCurPointer_Object = MibTableColumn
xPnniRtstCurPointer = _XPnniRtstCurPointer_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 1, 1, 1, 12),
    _XPnniRtstCurPointer_Type()
)
xPnniRtstCurPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniRtstCurPointer.setStatus("mandatory")
_XPnniTrcMIBGroup_ObjectIdentity = ObjectIdentity
xPnniTrcMIBGroup = _XPnniTrcMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2)
)
_XPnniTrcBufSiz_Type = Integer32
_XPnniTrcBufSiz_Object = MibScalar
xPnniTrcBufSiz = _XPnniTrcBufSiz_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 1),
    _XPnniTrcBufSiz_Type()
)
xPnniTrcBufSiz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniTrcBufSiz.setStatus("mandatory")


class _XPnniTrcBufTrigger_Type(Integer32):
    """Custom type xPnniTrcBufTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("haltOnFull", 2),
          ("loop", 1))
    )


_XPnniTrcBufTrigger_Type.__name__ = "Integer32"
_XPnniTrcBufTrigger_Object = MibScalar
xPnniTrcBufTrigger = _XPnniTrcBufTrigger_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 2),
    _XPnniTrcBufTrigger_Type()
)
xPnniTrcBufTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniTrcBufTrigger.setStatus("mandatory")


class _XPnniTrcBufControl_Type(Integer32):
    """Custom type xPnniTrcBufControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("freeze", 2),
          ("start", 1),
          ("stopAndFreeBuf", 3))
    )


_XPnniTrcBufControl_Type.__name__ = "Integer32"
_XPnniTrcBufControl_Object = MibScalar
xPnniTrcBufControl = _XPnniTrcBufControl_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 3),
    _XPnniTrcBufControl_Type()
)
xPnniTrcBufControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniTrcBufControl.setStatus("mandatory")
_XPnniTrcNodeIndex_Type = Integer32
_XPnniTrcNodeIndex_Object = MibScalar
xPnniTrcNodeIndex = _XPnniTrcNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 4),
    _XPnniTrcNodeIndex_Type()
)
xPnniTrcNodeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniTrcNodeIndex.setStatus("mandatory")
_XPnniTrcTable_Object = MibTable
xPnniTrcTable = _XPnniTrcTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5)
)
if mibBuilder.loadTexts:
    xPnniTrcTable.setStatus("mandatory")
_XPnniTrcEntry_Object = MibTableRow
xPnniTrcEntry = _XPnniTrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1)
)
xPnniTrcEntry.setIndexNames(
    (0, "XYLANPNNI-MIB", "xPnniTrcFrameIndex"),
    (0, "XYLANPNNI-MIB", "xPnniTrcFrameFrag"),
)
if mibBuilder.loadTexts:
    xPnniTrcEntry.setStatus("mandatory")
_XPnniTrcFrameIndex_Type = Integer32
_XPnniTrcFrameIndex_Object = MibTableColumn
xPnniTrcFrameIndex = _XPnniTrcFrameIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 1),
    _XPnniTrcFrameIndex_Type()
)
xPnniTrcFrameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcFrameIndex.setStatus("mandatory")
_XPnniTrcFrameFrag_Type = Integer32
_XPnniTrcFrameFrag_Object = MibTableColumn
xPnniTrcFrameFrag = _XPnniTrcFrameFrag_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 2),
    _XPnniTrcFrameFrag_Type()
)
xPnniTrcFrameFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcFrameFrag.setStatus("mandatory")


class _XPnniTrcDirection_Type(Integer32):
    """Custom type xPnniTrcDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_XPnniTrcDirection_Type.__name__ = "Integer32"
_XPnniTrcDirection_Object = MibTableColumn
xPnniTrcDirection = _XPnniTrcDirection_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 3),
    _XPnniTrcDirection_Type()
)
xPnniTrcDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcDirection.setStatus("mandatory")
_XPnniTrcSlot_Type = Integer32
_XPnniTrcSlot_Object = MibTableColumn
xPnniTrcSlot = _XPnniTrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 4),
    _XPnniTrcSlot_Type()
)
xPnniTrcSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcSlot.setStatus("mandatory")
_XPnniTrcPort_Type = Integer32
_XPnniTrcPort_Object = MibTableColumn
xPnniTrcPort = _XPnniTrcPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 5),
    _XPnniTrcPort_Type()
)
xPnniTrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcPort.setStatus("mandatory")
_XPnniTrcCsmPPort_Type = Integer32
_XPnniTrcCsmPPort_Object = MibTableColumn
xPnniTrcCsmPPort = _XPnniTrcCsmPPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 6),
    _XPnniTrcCsmPPort_Type()
)
xPnniTrcCsmPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcCsmPPort.setStatus("mandatory")


class _XPnniTrcFrType_Type(Integer32):
    """Custom type xPnniTrcFrType based on Integer32"""
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
        *(("dbSumm", 4),
          ("hello", 1),
          ("ptseAck", 3),
          ("ptseReq", 5),
          ("ptsp", 2))
    )


_XPnniTrcFrType_Type.__name__ = "Integer32"
_XPnniTrcFrType_Object = MibTableColumn
xPnniTrcFrType = _XPnniTrcFrType_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 7),
    _XPnniTrcFrType_Type()
)
xPnniTrcFrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcFrType.setStatus("mandatory")
_XPnniTrcFrLen_Type = Integer32
_XPnniTrcFrLen_Object = MibTableColumn
xPnniTrcFrLen = _XPnniTrcFrLen_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 8),
    _XPnniTrcFrLen_Type()
)
xPnniTrcFrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcFrLen.setStatus("mandatory")
_XPnniTrcLearned_Type = TimeStamp
_XPnniTrcLearned_Object = MibTableColumn
xPnniTrcLearned = _XPnniTrcLearned_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 9),
    _XPnniTrcLearned_Type()
)
xPnniTrcLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcLearned.setStatus("mandatory")


class _XPnniTrcFrame_Type(OctetString):
    """Custom type xPnniTrcFrame based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1000, 1000),
    )


_XPnniTrcFrame_Type.__name__ = "OctetString"
_XPnniTrcFrame_Object = MibTableColumn
xPnniTrcFrame = _XPnniTrcFrame_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 4, 2, 5, 1, 10),
    _XPnniTrcFrame_Type()
)
xPnniTrcFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrcFrame.setStatus("mandatory")
_XPnniAliasTable_Object = MibTable
xPnniAliasTable = _XPnniAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    xPnniAliasTable.setStatus("mandatory")
_XPnniAliasEntry_Object = MibTableRow
xPnniAliasEntry = _XPnniAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 5, 1)
)
xPnniAliasEntry.setIndexNames(
    (0, "XYLANPNNI-MIB", "xPnniAliasIndex"),
)
if mibBuilder.loadTexts:
    xPnniAliasEntry.setStatus("mandatory")
_XPnniAliasIndex_Type = Integer32
_XPnniAliasIndex_Object = MibTableColumn
xPnniAliasIndex = _XPnniAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 5, 1, 1),
    _XPnniAliasIndex_Type()
)
xPnniAliasIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniAliasIndex.setStatus("mandatory")
_XPnniAliasName_Type = DisplayString
_XPnniAliasName_Object = MibTableColumn
xPnniAliasName = _XPnniAliasName_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 5, 1, 2),
    _XPnniAliasName_Type()
)
xPnniAliasName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniAliasName.setStatus("mandatory")
_XPnniAliasPrefLen_Type = Integer32
_XPnniAliasPrefLen_Object = MibTableColumn
xPnniAliasPrefLen = _XPnniAliasPrefLen_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 5, 1, 3),
    _XPnniAliasPrefLen_Type()
)
xPnniAliasPrefLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniAliasPrefLen.setStatus("mandatory")


class _XPnniAliasPrefixBinding_Type(OctetString):
    """Custom type xPnniAliasPrefixBinding based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )


_XPnniAliasPrefixBinding_Type.__name__ = "OctetString"
_XPnniAliasPrefixBinding_Object = MibTableColumn
xPnniAliasPrefixBinding = _XPnniAliasPrefixBinding_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 5, 1, 4),
    _XPnniAliasPrefixBinding_Type()
)
xPnniAliasPrefixBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xPnniAliasPrefixBinding.setStatus("mandatory")
_XPnniTrapMIBObjects_ObjectIdentity = ObjectIdentity
xPnniTrapMIBObjects = _XPnniTrapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6)
)
_XPnniTrapPnPortId_Type = Integer32
_XPnniTrapPnPortId_Object = MibScalar
xPnniTrapPnPortId = _XPnniTrapPnPortId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 1),
    _XPnniTrapPnPortId_Type()
)
xPnniTrapPnPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapPnPortId.setStatus("mandatory")
_XPnniTrapRouteAddrAddress_Type = XPnniAddrPrefix
_XPnniTrapRouteAddrAddress_Object = MibScalar
xPnniTrapRouteAddrAddress = _XPnniTrapRouteAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 2),
    _XPnniTrapRouteAddrAddress_Type()
)
xPnniTrapRouteAddrAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapRouteAddrAddress.setStatus("mandatory")
_XPnniTrapRouteAddrPrefixLength_Type = XPnniFilterPrefixLength
_XPnniTrapRouteAddrPrefixLength_Object = MibScalar
xPnniTrapRouteAddrPrefixLength = _XPnniTrapRouteAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 3),
    _XPnniTrapRouteAddrPrefixLength_Type()
)
xPnniTrapRouteAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapRouteAddrPrefixLength.setStatus("mandatory")
_XPnniTrapFiltIndex_Type = Integer32
_XPnniTrapFiltIndex_Object = MibScalar
xPnniTrapFiltIndex = _XPnniTrapFiltIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 4),
    _XPnniTrapFiltIndex_Type()
)
xPnniTrapFiltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapFiltIndex.setStatus("mandatory")
_XPnniTrapNeighborId_Type = XPnniNodeId
_XPnniTrapNeighborId_Object = MibScalar
xPnniTrapNeighborId = _XPnniTrapNeighborId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 5),
    _XPnniTrapNeighborId_Type()
)
xPnniTrapNeighborId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapNeighborId.setStatus("mandatory")
_XPnniTrapNodeId_Type = XPnniNodeId
_XPnniTrapNodeId_Object = MibScalar
xPnniTrapNodeId = _XPnniTrapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 6),
    _XPnniTrapNodeId_Type()
)
xPnniTrapNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapNodeId.setStatus("mandatory")


class _XPnniTrapNodeDownReason_Type(Integer32):
    """Custom type xPnniTrapNodeDownReason based on Integer32"""
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
        *(("localUiAdmin", 1),
          ("mgmt", 3),
          ("other", 4),
          ("remoteTelnet", 2))
    )


_XPnniTrapNodeDownReason_Type.__name__ = "Integer32"
_XPnniTrapNodeDownReason_Object = MibScalar
xPnniTrapNodeDownReason = _XPnniTrapNodeDownReason_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 7),
    _XPnniTrapNodeDownReason_Type()
)
xPnniTrapNodeDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapNodeDownReason.setStatus("mandatory")
_XPnniTrapNodeDownRemoteIPAddr_Type = Integer32
_XPnniTrapNodeDownRemoteIPAddr_Object = MibScalar
xPnniTrapNodeDownRemoteIPAddr = _XPnniTrapNodeDownRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 3, 2, 1, 2, 1, 1, 6, 8),
    _XPnniTrapNodeDownRemoteIPAddr_Type()
)
xPnniTrapNodeDownRemoteIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xPnniTrapNodeDownRemoteIPAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLANPNNI-MIB",
    **{"XPnniNodeId": XPnniNodeId,
       "XPnniNodeLevel": XPnniNodeLevel,
       "XPnniAtmAddr": XPnniAtmAddr,
       "XPnniPortId": XPnniPortId,
       "XPnniFiltCallType": XPnniFiltCallType,
       "XPnniFiltServiceCategory": XPnniFiltServiceCategory,
       "XPnniFiltMetricConstraint": XPnniFiltMetricConstraint,
       "XPnniFiltExceptionCriteria": XPnniFiltExceptionCriteria,
       "XPnniFilterPrefixLength": XPnniFilterPrefixLength,
       "XPnniAddrPrefix": XPnniAddrPrefix,
       "xylanPnniMIB": xylanPnniMIB,
       "xylanPnniMIBExtens": xylanPnniMIBExtens,
       "xylanPnniMIBObjs": xylanPnniMIBObjs,
       "xPnniAssociativeNameTable": xPnniAssociativeNameTable,
       "xPnniNameEntry": xPnniNameEntry,
       "xPnniNodeIndex": xPnniNodeIndex,
       "xPnniNodeId": xPnniNodeId,
       "xPnniNodeName": xPnniNodeName,
       "xPnniAddressFilterTable": xPnniAddressFilterTable,
       "xPnniAddressFilterEntry": xPnniAddressFilterEntry,
       "xPnniFiltIndex": xPnniFiltIndex,
       "xPnniFiltNodeLevel": xPnniFiltNodeLevel,
       "xPnniFiltSrcPrefLen": xPnniFiltSrcPrefLen,
       "xPnniFiltSrcPrefix": xPnniFiltSrcPrefix,
       "xPnniFiltDestPrefLen": xPnniFiltDestPrefLen,
       "xPnniFiltDestPrefix": xPnniFiltDestPrefix,
       "xPnniFiltCallType": xPnniFiltCallType,
       "xPnniFiltCallSrvCls": xPnniFiltCallSrvCls,
       "xPnniFiltCallMtrcConstrnt": xPnniFiltCallMtrcConstrnt,
       "xPnniFiltCallMtrcThresh": xPnniFiltCallMtrcThresh,
       "xPnniFiltTrapThresh": xPnniFiltTrapThresh,
       "xPnniFiltSrcExceptionCriteria": xPnniFiltSrcExceptionCriteria,
       "xPnniFiltSrcExceptionLen": xPnniFiltSrcExceptionLen,
       "xPnniFiltSrcException": xPnniFiltSrcException,
       "xPnniFiltDestExceptionCriteria": xPnniFiltDestExceptionCriteria,
       "xPnniFiltDestExceptionLen": xPnniFiltDestExceptionLen,
       "xPnniFiltDestException": xPnniFiltDestException,
       "xPnniFiltDeniedHitCount": xPnniFiltDeniedHitCount,
       "xPnniFiltExceptionHitCount": xPnniFiltExceptionHitCount,
       "xPnniFiltTODStartHr": xPnniFiltTODStartHr,
       "xPnniFiltTODStartMin": xPnniFiltTODStartMin,
       "xPnniFiltTODStartSec": xPnniFiltTODStartSec,
       "xPnniFiltTODStopHr": xPnniFiltTODStopHr,
       "xPnniFiltTODStopMin": xPnniFiltTODStopMin,
       "xPnniFiltTODStopSec": xPnniFiltTODStopSec,
       "xPnniIAdjMIBObjects": xPnniIAdjMIBObjects,
       "xPnniIAdjGroup": xPnniIAdjGroup,
       "xPnniNumIAdj": xPnniNumIAdj,
       "xPnniIAdjTable": xPnniIAdjTable,
       "xPnniIAdjEntry": xPnniIAdjEntry,
       "xPnniIAdjIndex": xPnniIAdjIndex,
       "xPnniIAdjAtmAddress": xPnniIAdjAtmAddress,
       "xPnniIAdjSlot": xPnniIAdjSlot,
       "xPnniIAdjPort": xPnniIAdjPort,
       "xPnniIAdjInst": xPnniIAdjInst,
       "xPnniIAdjCsmPPort": xPnniIAdjCsmPPort,
       "xPnniIAdjAdvertised": xPnniIAdjAdvertised,
       "xPnniIAdjSummarized": xPnniIAdjSummarized,
       "xPnniIAdjLearned": xPnniIAdjLearned,
       "xPnniTestMIBObjects": xPnniTestMIBObjects,
       "xPnniRtstMIBGroup": xPnniRtstMIBGroup,
       "xPnniRtstTable": xPnniRtstTable,
       "xPnniRtstEntry": xPnniRtstEntry,
       "xPnniRtstClass": xPnniRtstClass,
       "xPnniRtstType": xPnniRtstType,
       "xPnniRtstDest": xPnniRtstDest,
       "xPnniRtstError": xPnniRtstError,
       "xPnniRtstFlags": xPnniRtstFlags,
       "xPnniRtstOutboundPort": xPnniRtstOutboundPort,
       "xPnniRtstVPI": xPnniRtstVPI,
       "xPnniRtstE164": xPnniRtstE164,
       "xPnniRtstE164len": xPnniRtstE164len,
       "xPnniRtstHopCount": xPnniRtstHopCount,
       "xPnniRtstDTL": xPnniRtstDTL,
       "xPnniRtstCurPointer": xPnniRtstCurPointer,
       "xPnniTrcMIBGroup": xPnniTrcMIBGroup,
       "xPnniTrcBufSiz": xPnniTrcBufSiz,
       "xPnniTrcBufTrigger": xPnniTrcBufTrigger,
       "xPnniTrcBufControl": xPnniTrcBufControl,
       "xPnniTrcNodeIndex": xPnniTrcNodeIndex,
       "xPnniTrcTable": xPnniTrcTable,
       "xPnniTrcEntry": xPnniTrcEntry,
       "xPnniTrcFrameIndex": xPnniTrcFrameIndex,
       "xPnniTrcFrameFrag": xPnniTrcFrameFrag,
       "xPnniTrcDirection": xPnniTrcDirection,
       "xPnniTrcSlot": xPnniTrcSlot,
       "xPnniTrcPort": xPnniTrcPort,
       "xPnniTrcCsmPPort": xPnniTrcCsmPPort,
       "xPnniTrcFrType": xPnniTrcFrType,
       "xPnniTrcFrLen": xPnniTrcFrLen,
       "xPnniTrcLearned": xPnniTrcLearned,
       "xPnniTrcFrame": xPnniTrcFrame,
       "xPnniAliasTable": xPnniAliasTable,
       "xPnniAliasEntry": xPnniAliasEntry,
       "xPnniAliasIndex": xPnniAliasIndex,
       "xPnniAliasName": xPnniAliasName,
       "xPnniAliasPrefLen": xPnniAliasPrefLen,
       "xPnniAliasPrefixBinding": xPnniAliasPrefixBinding,
       "xPnniTrapMIBObjects": xPnniTrapMIBObjects,
       "xPnniTrapPnPortId": xPnniTrapPnPortId,
       "xPnniTrapRouteAddrAddress": xPnniTrapRouteAddrAddress,
       "xPnniTrapRouteAddrPrefixLength": xPnniTrapRouteAddrPrefixLength,
       "xPnniTrapFiltIndex": xPnniTrapFiltIndex,
       "xPnniTrapNeighborId": xPnniTrapNeighborId,
       "xPnniTrapNodeId": xPnniTrapNodeId,
       "xPnniTrapNodeDownReason": xPnniTrapNodeDownReason,
       "xPnniTrapNodeDownRemoteIPAddr": xPnniTrapNodeDownRemoteIPAddr}
)
