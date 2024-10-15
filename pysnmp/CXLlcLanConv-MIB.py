# SNMP MIB module (CXLlcLanConv-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXLlcLanConv-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:38 2024
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
 SapIndex,
 cxLlcLanConv) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxLlcLanConv")

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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LlcLanSapTable_Object = MibTable
llcLanSapTable = _LlcLanSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10)
)
if mibBuilder.loadTexts:
    llcLanSapTable.setStatus("mandatory")
_LlcLanSapEntry_Object = MibTableRow
llcLanSapEntry = _LlcLanSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1)
)
llcLanSapEntry.setIndexNames(
    (0, "CXLlcLanConv-MIB", "llcLanSapNumber"),
)
if mibBuilder.loadTexts:
    llcLanSapEntry.setStatus("mandatory")
_LlcLanSapNumber_Type = SapIndex
_LlcLanSapNumber_Object = MibTableColumn
llcLanSapNumber = _LlcLanSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 1),
    _LlcLanSapNumber_Type()
)
llcLanSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcLanSapNumber.setStatus("mandatory")


class _LlcLanSapRowStatus_Type(Integer32):
    """Custom type llcLanSapRowStatus based on Integer32"""
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


_LlcLanSapRowStatus_Type.__name__ = "Integer32"
_LlcLanSapRowStatus_Object = MibTableColumn
llcLanSapRowStatus = _LlcLanSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 2),
    _LlcLanSapRowStatus_Type()
)
llcLanSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapRowStatus.setStatus("mandatory")
_LlcLanSapAlias_Type = Alias
_LlcLanSapAlias_Object = MibTableColumn
llcLanSapAlias = _LlcLanSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 3),
    _LlcLanSapAlias_Type()
)
llcLanSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapAlias.setStatus("mandatory")
_LlcLanSapCompanionAlias_Type = Alias
_LlcLanSapCompanionAlias_Object = MibTableColumn
llcLanSapCompanionAlias = _LlcLanSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 4),
    _LlcLanSapCompanionAlias_Type()
)
llcLanSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapCompanionAlias.setStatus("mandatory")
_LlcLanSapRemoteAddress_Type = MacAddress
_LlcLanSapRemoteAddress_Object = MibTableColumn
llcLanSapRemoteAddress = _LlcLanSapRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 5),
    _LlcLanSapRemoteAddress_Type()
)
llcLanSapRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapRemoteAddress.setStatus("mandatory")


class _LlcLanSapSrcLlcSap_Type(Integer32):
    """Custom type llcLanSapSrcLlcSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_LlcLanSapSrcLlcSap_Type.__name__ = "Integer32"
_LlcLanSapSrcLlcSap_Object = MibTableColumn
llcLanSapSrcLlcSap = _LlcLanSapSrcLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 6),
    _LlcLanSapSrcLlcSap_Type()
)
llcLanSapSrcLlcSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapSrcLlcSap.setStatus("mandatory")


class _LlcLanSapDstLlcSap_Type(Integer32):
    """Custom type llcLanSapDstLlcSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 254),
    )


_LlcLanSapDstLlcSap_Type.__name__ = "Integer32"
_LlcLanSapDstLlcSap_Object = MibTableColumn
llcLanSapDstLlcSap = _LlcLanSapDstLlcSap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 7),
    _LlcLanSapDstLlcSap_Type()
)
llcLanSapDstLlcSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapDstLlcSap.setStatus("mandatory")


class _LlcLanSapControl_Type(Integer32):
    """Custom type llcLanSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearStats", 1),
          ("releaseRemoteAddress", 2))
    )


_LlcLanSapControl_Type.__name__ = "Integer32"
_LlcLanSapControl_Object = MibTableColumn
llcLanSapControl = _LlcLanSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 8),
    _LlcLanSapControl_Type()
)
llcLanSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    llcLanSapControl.setStatus("mandatory")


class _LlcLanSapState_Type(Integer32):
    """Custom type llcLanSapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_LlcLanSapState_Type.__name__ = "Integer32"
_LlcLanSapState_Object = MibTableColumn
llcLanSapState = _LlcLanSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 9),
    _LlcLanSapState_Type()
)
llcLanSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcLanSapState.setStatus("mandatory")
_LlcLanSapTxFrames_Type = Counter32
_LlcLanSapTxFrames_Object = MibTableColumn
llcLanSapTxFrames = _LlcLanSapTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 10),
    _LlcLanSapTxFrames_Type()
)
llcLanSapTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcLanSapTxFrames.setStatus("mandatory")
_LlcLanSapRxFrames_Type = Counter32
_LlcLanSapRxFrames_Object = MibTableColumn
llcLanSapRxFrames = _LlcLanSapRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 11),
    _LlcLanSapRxFrames_Type()
)
llcLanSapRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcLanSapRxFrames.setStatus("mandatory")
_LlcLanSapTxOctets_Type = Counter32
_LlcLanSapTxOctets_Object = MibTableColumn
llcLanSapTxOctets = _LlcLanSapTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 12),
    _LlcLanSapTxOctets_Type()
)
llcLanSapTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcLanSapTxOctets.setStatus("mandatory")
_LlcLanSapRxOctets_Type = Counter32
_LlcLanSapRxOctets_Object = MibTableColumn
llcLanSapRxOctets = _LlcLanSapRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 13),
    _LlcLanSapRxOctets_Type()
)
llcLanSapRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    llcLanSapRxOctets.setStatus("mandatory")
_LlcLanSapLocalAddress_Type = MacAddress
_LlcLanSapLocalAddress_Object = MibTableColumn
llcLanSapLocalAddress = _LlcLanSapLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 19),
    _LlcLanSapLocalAddress_Type()
)
llcLanSapLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapLocalAddress.setStatus("mandatory")


class _LlcLanSapPhysicalInterface_Type(Integer32):
    """Custom type llcLanSapPhysicalInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("tokenring", 2))
    )


_LlcLanSapPhysicalInterface_Type.__name__ = "Integer32"
_LlcLanSapPhysicalInterface_Object = MibTableColumn
llcLanSapPhysicalInterface = _LlcLanSapPhysicalInterface_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 10, 1, 20),
    _LlcLanSapPhysicalInterface_Type()
)
llcLanSapPhysicalInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    llcLanSapPhysicalInterface.setStatus("mandatory")


class _CxLlcLanConvMibLevel_Type(Integer32):
    """Custom type cxLlcLanConvMibLevel based on Integer32"""
    defaultValue = 0


_CxLlcLanConvMibLevel_Object = MibScalar
cxLlcLanConvMibLevel = _CxLlcLanConvMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 47, 20),
    _CxLlcLanConvMibLevel_Type()
)
cxLlcLanConvMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxLlcLanConvMibLevel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXLlcLanConv-MIB",
    **{"MacAddress": MacAddress,
       "llcLanSapTable": llcLanSapTable,
       "llcLanSapEntry": llcLanSapEntry,
       "llcLanSapNumber": llcLanSapNumber,
       "llcLanSapRowStatus": llcLanSapRowStatus,
       "llcLanSapAlias": llcLanSapAlias,
       "llcLanSapCompanionAlias": llcLanSapCompanionAlias,
       "llcLanSapRemoteAddress": llcLanSapRemoteAddress,
       "llcLanSapSrcLlcSap": llcLanSapSrcLlcSap,
       "llcLanSapDstLlcSap": llcLanSapDstLlcSap,
       "llcLanSapControl": llcLanSapControl,
       "llcLanSapState": llcLanSapState,
       "llcLanSapTxFrames": llcLanSapTxFrames,
       "llcLanSapRxFrames": llcLanSapRxFrames,
       "llcLanSapTxOctets": llcLanSapTxOctets,
       "llcLanSapRxOctets": llcLanSapRxOctets,
       "llcLanSapLocalAddress": llcLanSapLocalAddress,
       "llcLanSapPhysicalInterface": llcLanSapPhysicalInterface,
       "cxLlcLanConvMibLevel": cxLlcLanConvMibLevel}
)
