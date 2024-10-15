# SNMP MIB module (CXLlcFrConv-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXLlcFrConv-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:37 2024
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

(Alias,
 cxLlcFrConv) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxLlcFrConv")

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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class SubRef(Integer32):
    """Custom type SubRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _LlcfrcnvSysRouteConnectInterval_Type(Integer32):
    """Custom type llcfrcnvSysRouteConnectInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 900),
    )


_LlcfrcnvSysRouteConnectInterval_Type.__name__ = "Integer32"
_LlcfrcnvSysRouteConnectInterval_Object = MibScalar
llcfrcnvSysRouteConnectInterval = _LlcfrcnvSysRouteConnectInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 1),
    _LlcfrcnvSysRouteConnectInterval_Type()
)
llcfrcnvSysRouteConnectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSysRouteConnectInterval.setStatus("mandatory")


class _LlcfrcnvMibLevel_Type(Integer32):
    """Custom type llcfrcnvMibLevel based on Integer32"""
    defaultValue = 0


_LlcfrcnvMibLevel_Object = MibScalar
llcfrcnvMibLevel = _LlcfrcnvMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 2),
    _LlcfrcnvMibLevel_Type()
)
llcfrcnvMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvMibLevel.setStatus("mandatory")
_LlcfrcnvSapTable_Object = MibTable
llcfrcnvSapTable = _LlcfrcnvSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10)
)
if mibBuilder.loadTexts:
    llcfrcnvSapTable.setStatus("mandatory")
_LlcfrcnvSapEntry_Object = MibTableRow
llcfrcnvSapEntry = _LlcfrcnvSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1)
)
llcfrcnvSapEntry.setIndexNames(
    (0, "CXLlcFrConv-MIB", "llcfrcnvSapNumber"),
)
if mibBuilder.loadTexts:
    llcfrcnvSapEntry.setStatus("mandatory")


class _LlcfrcnvSapNumber_Type(Integer32):
    """Custom type llcfrcnvSapNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LlcfrcnvSapNumber_Type.__name__ = "Integer32"
_LlcfrcnvSapNumber_Object = MibTableColumn
llcfrcnvSapNumber = _LlcfrcnvSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 1),
    _LlcfrcnvSapNumber_Type()
)
llcfrcnvSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapNumber.setStatus("mandatory")


class _LlcfrcnvSapRowStatus_Type(Integer32):
    """Custom type llcfrcnvSapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_LlcfrcnvSapRowStatus_Type.__name__ = "Integer32"
_LlcfrcnvSapRowStatus_Object = MibTableColumn
llcfrcnvSapRowStatus = _LlcfrcnvSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 2),
    _LlcfrcnvSapRowStatus_Type()
)
llcfrcnvSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSapRowStatus.setStatus("mandatory")
_LlcfrcnvSapAlias_Type = Alias
_LlcfrcnvSapAlias_Object = MibTableColumn
llcfrcnvSapAlias = _LlcfrcnvSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 3),
    _LlcfrcnvSapAlias_Type()
)
llcfrcnvSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSapAlias.setStatus("mandatory")


class _LlcfrcnvSapSrcLlcSap_Type(Integer32):
    """Custom type llcfrcnvSapSrcLlcSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_LlcfrcnvSapSrcLlcSap_Type.__name__ = "Integer32"
_LlcfrcnvSapSrcLlcSap_Object = MibTableColumn
llcfrcnvSapSrcLlcSap = _LlcfrcnvSapSrcLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 4),
    _LlcfrcnvSapSrcLlcSap_Type()
)
llcfrcnvSapSrcLlcSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSapSrcLlcSap.setStatus("mandatory")


class _LlcfrcnvSapDstLlcSap_Type(Integer32):
    """Custom type llcfrcnvSapDstLlcSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_LlcfrcnvSapDstLlcSap_Type.__name__ = "Integer32"
_LlcfrcnvSapDstLlcSap_Object = MibTableColumn
llcfrcnvSapDstLlcSap = _LlcfrcnvSapDstLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 5),
    _LlcfrcnvSapDstLlcSap_Type()
)
llcfrcnvSapDstLlcSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSapDstLlcSap.setStatus("mandatory")


class _LlcfrcnvSapRouteIndex_Type(Integer32):
    """Custom type llcfrcnvSapRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_LlcfrcnvSapRouteIndex_Type.__name__ = "Integer32"
_LlcfrcnvSapRouteIndex_Object = MibTableColumn
llcfrcnvSapRouteIndex = _LlcfrcnvSapRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 6),
    _LlcfrcnvSapRouteIndex_Type()
)
llcfrcnvSapRouteIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSapRouteIndex.setStatus("mandatory")


class _LlcfrcnvSapControl_Type(Integer32):
    """Custom type llcfrcnvSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_LlcfrcnvSapControl_Type.__name__ = "Integer32"
_LlcfrcnvSapControl_Object = MibTableColumn
llcfrcnvSapControl = _LlcfrcnvSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 7),
    _LlcfrcnvSapControl_Type()
)
llcfrcnvSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    llcfrcnvSapControl.setStatus("mandatory")


class _LlcfrcnvSapState_Type(Integer32):
    """Custom type llcfrcnvSapState based on Integer32"""
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
        *(("bound", 3),
          ("connected", 4),
          ("offLine", 1),
          ("unbound", 2))
    )


_LlcfrcnvSapState_Type.__name__ = "Integer32"
_LlcfrcnvSapState_Object = MibTableColumn
llcfrcnvSapState = _LlcfrcnvSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 8),
    _LlcfrcnvSapState_Type()
)
llcfrcnvSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapState.setStatus("mandatory")
_LlcfrcnvSapTxFrames_Type = Counter32
_LlcfrcnvSapTxFrames_Object = MibTableColumn
llcfrcnvSapTxFrames = _LlcfrcnvSapTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 9),
    _LlcfrcnvSapTxFrames_Type()
)
llcfrcnvSapTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapTxFrames.setStatus("mandatory")
_LlcfrcnvSapRxFrames_Type = Counter32
_LlcfrcnvSapRxFrames_Object = MibTableColumn
llcfrcnvSapRxFrames = _LlcfrcnvSapRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 10),
    _LlcfrcnvSapRxFrames_Type()
)
llcfrcnvSapRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapRxFrames.setStatus("mandatory")
_LlcfrcnvSapTxOctets_Type = Counter32
_LlcfrcnvSapTxOctets_Object = MibTableColumn
llcfrcnvSapTxOctets = _LlcfrcnvSapTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 11),
    _LlcfrcnvSapTxOctets_Type()
)
llcfrcnvSapTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapTxOctets.setStatus("mandatory")
_LlcfrcnvSapRxOctets_Type = Counter32
_LlcfrcnvSapRxOctets_Object = MibTableColumn
llcfrcnvSapRxOctets = _LlcfrcnvSapRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 12),
    _LlcfrcnvSapRxOctets_Type()
)
llcfrcnvSapRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapRxOctets.setStatus("mandatory")
_LlcfrcnvSapUnopenedServiceDiscards_Type = Counter32
_LlcfrcnvSapUnopenedServiceDiscards_Object = MibTableColumn
llcfrcnvSapUnopenedServiceDiscards = _LlcfrcnvSapUnopenedServiceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 13),
    _LlcfrcnvSapUnopenedServiceDiscards_Type()
)
llcfrcnvSapUnopenedServiceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapUnopenedServiceDiscards.setStatus("mandatory")
_LlcfrcnvSapTxResets_Type = Counter32
_LlcfrcnvSapTxResets_Object = MibTableColumn
llcfrcnvSapTxResets = _LlcfrcnvSapTxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 14),
    _LlcfrcnvSapTxResets_Type()
)
llcfrcnvSapTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapTxResets.setStatus("mandatory")
_LlcfrcnvSapRxResets_Type = Counter32
_LlcfrcnvSapRxResets_Object = MibTableColumn
llcfrcnvSapRxResets = _LlcfrcnvSapRxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 15),
    _LlcfrcnvSapRxResets_Type()
)
llcfrcnvSapRxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSapRxResets.setStatus("mandatory")
_LlcfrcnvSapHostMacAddr_Type = MacAddress
_LlcfrcnvSapHostMacAddr_Object = MibTableColumn
llcfrcnvSapHostMacAddr = _LlcfrcnvSapHostMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 16),
    _LlcfrcnvSapHostMacAddr_Type()
)
llcfrcnvSapHostMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSapHostMacAddr.setStatus("mandatory")
_LlcfrcnvSapCntrMacAddr_Type = MacAddress
_LlcfrcnvSapCntrMacAddr_Object = MibTableColumn
llcfrcnvSapCntrMacAddr = _LlcfrcnvSapCntrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 10, 1, 17),
    _LlcfrcnvSapCntrMacAddr_Type()
)
llcfrcnvSapCntrMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSapCntrMacAddr.setStatus("mandatory")
_LlcfrcnvSysRouteTable_Object = MibTable
llcfrcnvSysRouteTable = _LlcfrcnvSysRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11)
)
if mibBuilder.loadTexts:
    llcfrcnvSysRouteTable.setStatus("mandatory")
_LlcfrcnvSysRouteEntry_Object = MibTableRow
llcfrcnvSysRouteEntry = _LlcfrcnvSysRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1)
)
llcfrcnvSysRouteEntry.setIndexNames(
    (0, "CXLlcFrConv-MIB", "llcfrcnvSRIndex"),
)
if mibBuilder.loadTexts:
    llcfrcnvSysRouteEntry.setStatus("mandatory")


class _LlcfrcnvSRIndex_Type(Integer32):
    """Custom type llcfrcnvSRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_LlcfrcnvSRIndex_Type.__name__ = "Integer32"
_LlcfrcnvSRIndex_Object = MibTableColumn
llcfrcnvSRIndex = _LlcfrcnvSRIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 1),
    _LlcfrcnvSRIndex_Type()
)
llcfrcnvSRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSRIndex.setStatus("mandatory")


class _LlcfrcnvSRRowStatus_Type(Integer32):
    """Custom type llcfrcnvSRRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_LlcfrcnvSRRowStatus_Type.__name__ = "Integer32"
_LlcfrcnvSRRowStatus_Object = MibTableColumn
llcfrcnvSRRowStatus = _LlcfrcnvSRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 2),
    _LlcfrcnvSRRowStatus_Type()
)
llcfrcnvSRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSRRowStatus.setStatus("mandatory")
_LlcfrcnvSRDestAlias_Type = Alias
_LlcfrcnvSRDestAlias_Object = MibTableColumn
llcfrcnvSRDestAlias = _LlcfrcnvSRDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 3),
    _LlcfrcnvSRDestAlias_Type()
)
llcfrcnvSRDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSRDestAlias.setStatus("mandatory")


class _LlcfrcnvSRControl_Type(Integer32):
    """Custom type llcfrcnvSRControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_LlcfrcnvSRControl_Type.__name__ = "Integer32"
_LlcfrcnvSRControl_Object = MibTableColumn
llcfrcnvSRControl = _LlcfrcnvSRControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 4),
    _LlcfrcnvSRControl_Type()
)
llcfrcnvSRControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    llcfrcnvSRControl.setStatus("mandatory")


class _LlcfrcnvSRPriority_Type(Integer32):
    """Custom type llcfrcnvSRPriority based on Integer32"""
    defaultValue = 2

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
        *(("discard", 1),
          ("forward", 2),
          ("priority-high", 4),
          ("priority-low", 3))
    )


_LlcfrcnvSRPriority_Type.__name__ = "Integer32"
_LlcfrcnvSRPriority_Object = MibTableColumn
llcfrcnvSRPriority = _LlcfrcnvSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 5),
    _LlcfrcnvSRPriority_Type()
)
llcfrcnvSRPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSRPriority.setStatus("mandatory")
_LlcfrcnvSRSubRef_Type = SubRef
_LlcfrcnvSRSubRef_Object = MibTableColumn
llcfrcnvSRSubRef = _LlcfrcnvSRSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 6),
    _LlcfrcnvSRSubRef_Type()
)
llcfrcnvSRSubRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcfrcnvSRSubRef.setStatus("mandatory")


class _LlcfrcnvSRRouteStatus_Type(Integer32):
    """Custom type llcfrcnvSRRouteStatus based on Integer32"""
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
        *(("connected", 4),
          ("inProgress", 3),
          ("notConnected", 2),
          ("offLine", 1))
    )


_LlcfrcnvSRRouteStatus_Type.__name__ = "Integer32"
_LlcfrcnvSRRouteStatus_Object = MibTableColumn
llcfrcnvSRRouteStatus = _LlcfrcnvSRRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 10),
    _LlcfrcnvSRRouteStatus_Type()
)
llcfrcnvSRRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSRRouteStatus.setStatus("mandatory")


class _LlcfrcnvSRClearStatus_Type(Integer32):
    """Custom type llcfrcnvSRClearStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 2),
          ("localFcnFailure", 7),
          ("noFailure", 1),
          ("remoteAliasNotFound", 9),
          ("remoteAllocFailure", 3),
          ("remoteFcnFailure", 8),
          ("remoteNoAccess", 4),
          ("remotePvcBusy", 6),
          ("remotePvcDown", 5))
    )


_LlcfrcnvSRClearStatus_Type.__name__ = "Integer32"
_LlcfrcnvSRClearStatus_Object = MibTableColumn
llcfrcnvSRClearStatus = _LlcfrcnvSRClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 11),
    _LlcfrcnvSRClearStatus_Type()
)
llcfrcnvSRClearStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSRClearStatus.setStatus("mandatory")
_LlcfrcnvSROutSuccessfullConnects_Type = Counter32
_LlcfrcnvSROutSuccessfullConnects_Object = MibTableColumn
llcfrcnvSROutSuccessfullConnects = _LlcfrcnvSROutSuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 12),
    _LlcfrcnvSROutSuccessfullConnects_Type()
)
llcfrcnvSROutSuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSROutSuccessfullConnects.setStatus("mandatory")
_LlcfrcnvSROutUnsuccessfullConnects_Type = Counter32
_LlcfrcnvSROutUnsuccessfullConnects_Object = MibTableColumn
llcfrcnvSROutUnsuccessfullConnects = _LlcfrcnvSROutUnsuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 33, 11, 1, 13),
    _LlcfrcnvSROutUnsuccessfullConnects_Type()
)
llcfrcnvSROutUnsuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcfrcnvSROutUnsuccessfullConnects.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXLlcFrConv-MIB",
    **{"MacAddress": MacAddress,
       "SubRef": SubRef,
       "llcfrcnvSysRouteConnectInterval": llcfrcnvSysRouteConnectInterval,
       "llcfrcnvMibLevel": llcfrcnvMibLevel,
       "llcfrcnvSapTable": llcfrcnvSapTable,
       "llcfrcnvSapEntry": llcfrcnvSapEntry,
       "llcfrcnvSapNumber": llcfrcnvSapNumber,
       "llcfrcnvSapRowStatus": llcfrcnvSapRowStatus,
       "llcfrcnvSapAlias": llcfrcnvSapAlias,
       "llcfrcnvSapSrcLlcSap": llcfrcnvSapSrcLlcSap,
       "llcfrcnvSapDstLlcSap": llcfrcnvSapDstLlcSap,
       "llcfrcnvSapRouteIndex": llcfrcnvSapRouteIndex,
       "llcfrcnvSapControl": llcfrcnvSapControl,
       "llcfrcnvSapState": llcfrcnvSapState,
       "llcfrcnvSapTxFrames": llcfrcnvSapTxFrames,
       "llcfrcnvSapRxFrames": llcfrcnvSapRxFrames,
       "llcfrcnvSapTxOctets": llcfrcnvSapTxOctets,
       "llcfrcnvSapRxOctets": llcfrcnvSapRxOctets,
       "llcfrcnvSapUnopenedServiceDiscards": llcfrcnvSapUnopenedServiceDiscards,
       "llcfrcnvSapTxResets": llcfrcnvSapTxResets,
       "llcfrcnvSapRxResets": llcfrcnvSapRxResets,
       "llcfrcnvSapHostMacAddr": llcfrcnvSapHostMacAddr,
       "llcfrcnvSapCntrMacAddr": llcfrcnvSapCntrMacAddr,
       "llcfrcnvSysRouteTable": llcfrcnvSysRouteTable,
       "llcfrcnvSysRouteEntry": llcfrcnvSysRouteEntry,
       "llcfrcnvSRIndex": llcfrcnvSRIndex,
       "llcfrcnvSRRowStatus": llcfrcnvSRRowStatus,
       "llcfrcnvSRDestAlias": llcfrcnvSRDestAlias,
       "llcfrcnvSRControl": llcfrcnvSRControl,
       "llcfrcnvSRPriority": llcfrcnvSRPriority,
       "llcfrcnvSRSubRef": llcfrcnvSRSubRef,
       "llcfrcnvSRRouteStatus": llcfrcnvSRRouteStatus,
       "llcfrcnvSRClearStatus": llcfrcnvSRClearStatus,
       "llcfrcnvSROutSuccessfullConnects": llcfrcnvSROutSuccessfullConnects,
       "llcfrcnvSROutUnsuccessfullConnects": llcfrcnvSROutUnsuccessfullConnects}
)
