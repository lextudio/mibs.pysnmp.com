# SNMP MIB module (CXLapBConv-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXLapBConv-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:35 2024
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
 cxLapBConv) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxLapBConv")

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



class PSapIndex(Integer32):
    """Custom type PSapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class SubRef(Integer32):
    """Custom type SubRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _LapbcnvSysRouteConnectInterval_Type(Integer32):
    """Custom type lapbcnvSysRouteConnectInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 900),
    )


_LapbcnvSysRouteConnectInterval_Type.__name__ = "Integer32"
_LapbcnvSysRouteConnectInterval_Object = MibScalar
lapbcnvSysRouteConnectInterval = _LapbcnvSysRouteConnectInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 1),
    _LapbcnvSysRouteConnectInterval_Type()
)
lapbcnvSysRouteConnectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbcnvSysRouteConnectInterval.setStatus("mandatory")
_LapbcnvSapTable_Object = MibTable
lapbcnvSapTable = _LapbcnvSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10)
)
if mibBuilder.loadTexts:
    lapbcnvSapTable.setStatus("mandatory")
_LapbcnvSapEntry_Object = MibTableRow
lapbcnvSapEntry = _LapbcnvSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1)
)
lapbcnvSapEntry.setIndexNames(
    (0, "CXLapBConv-MIB", "lapbcnvSapNumber"),
)
if mibBuilder.loadTexts:
    lapbcnvSapEntry.setStatus("mandatory")
_LapbcnvSapNumber_Type = PSapIndex
_LapbcnvSapNumber_Object = MibTableColumn
lapbcnvSapNumber = _LapbcnvSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 1),
    _LapbcnvSapNumber_Type()
)
lapbcnvSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapNumber.setStatus("mandatory")


class _LapbcnvSapRowStatus_Type(Integer32):
    """Custom type lapbcnvSapRowStatus based on Integer32"""
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


_LapbcnvSapRowStatus_Type.__name__ = "Integer32"
_LapbcnvSapRowStatus_Object = MibTableColumn
lapbcnvSapRowStatus = _LapbcnvSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 2),
    _LapbcnvSapRowStatus_Type()
)
lapbcnvSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbcnvSapRowStatus.setStatus("mandatory")
_LapbcnvSapAlias_Type = Alias
_LapbcnvSapAlias_Object = MibTableColumn
lapbcnvSapAlias = _LapbcnvSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 3),
    _LapbcnvSapAlias_Type()
)
lapbcnvSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbcnvSapAlias.setStatus("mandatory")


class _LapbcnvSapControl_Type(Integer32):
    """Custom type lapbcnvSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_LapbcnvSapControl_Type.__name__ = "Integer32"
_LapbcnvSapControl_Object = MibTableColumn
lapbcnvSapControl = _LapbcnvSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 5),
    _LapbcnvSapControl_Type()
)
lapbcnvSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    lapbcnvSapControl.setStatus("mandatory")


class _LapbcnvSapState_Type(Integer32):
    """Custom type lapbcnvSapState based on Integer32"""
    defaultValue = 2

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
        *(("connected", 5),
          ("inProgress", 4),
          ("notConnected", 3),
          ("offLine", 1),
          ("unbound", 2))
    )


_LapbcnvSapState_Type.__name__ = "Integer32"
_LapbcnvSapState_Object = MibTableColumn
lapbcnvSapState = _LapbcnvSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 6),
    _LapbcnvSapState_Type()
)
lapbcnvSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapState.setStatus("mandatory")
_LapbcnvSapTxFrames_Type = Counter32
_LapbcnvSapTxFrames_Object = MibTableColumn
lapbcnvSapTxFrames = _LapbcnvSapTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 7),
    _LapbcnvSapTxFrames_Type()
)
lapbcnvSapTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapTxFrames.setStatus("mandatory")
_LapbcnvSapRxFrames_Type = Counter32
_LapbcnvSapRxFrames_Object = MibTableColumn
lapbcnvSapRxFrames = _LapbcnvSapRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 8),
    _LapbcnvSapRxFrames_Type()
)
lapbcnvSapRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapRxFrames.setStatus("mandatory")
_LapbcnvSapTxOctets_Type = Counter32
_LapbcnvSapTxOctets_Object = MibTableColumn
lapbcnvSapTxOctets = _LapbcnvSapTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 9),
    _LapbcnvSapTxOctets_Type()
)
lapbcnvSapTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapTxOctets.setStatus("mandatory")
_LapbcnvSapRxOctets_Type = Counter32
_LapbcnvSapRxOctets_Object = MibTableColumn
lapbcnvSapRxOctets = _LapbcnvSapRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 10),
    _LapbcnvSapRxOctets_Type()
)
lapbcnvSapRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapRxOctets.setStatus("mandatory")
_LapbcnvSapOutSuccessfullConnects_Type = Counter32
_LapbcnvSapOutSuccessfullConnects_Object = MibTableColumn
lapbcnvSapOutSuccessfullConnects = _LapbcnvSapOutSuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 11),
    _LapbcnvSapOutSuccessfullConnects_Type()
)
lapbcnvSapOutSuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapOutSuccessfullConnects.setStatus("mandatory")
_LapbcnvSapOutUnsuccessfullConnects_Type = Counter32
_LapbcnvSapOutUnsuccessfullConnects_Object = MibTableColumn
lapbcnvSapOutUnsuccessfullConnects = _LapbcnvSapOutUnsuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 12),
    _LapbcnvSapOutUnsuccessfullConnects_Type()
)
lapbcnvSapOutUnsuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapOutUnsuccessfullConnects.setStatus("mandatory")
_LapbcnvSapInSuccessfullConnects_Type = Counter32
_LapbcnvSapInSuccessfullConnects_Object = MibTableColumn
lapbcnvSapInSuccessfullConnects = _LapbcnvSapInSuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 13),
    _LapbcnvSapInSuccessfullConnects_Type()
)
lapbcnvSapInSuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapInSuccessfullConnects.setStatus("mandatory")
_LapbcnvSapInUnsuccessfullConnects_Type = Counter32
_LapbcnvSapInUnsuccessfullConnects_Object = MibTableColumn
lapbcnvSapInUnsuccessfullConnects = _LapbcnvSapInUnsuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 14),
    _LapbcnvSapInUnsuccessfullConnects_Type()
)
lapbcnvSapInUnsuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapInUnsuccessfullConnects.setStatus("mandatory")
_LapbcnvSapUnopenedServiceDiscards_Type = Counter32
_LapbcnvSapUnopenedServiceDiscards_Object = MibTableColumn
lapbcnvSapUnopenedServiceDiscards = _LapbcnvSapUnopenedServiceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 15),
    _LapbcnvSapUnopenedServiceDiscards_Type()
)
lapbcnvSapUnopenedServiceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapUnopenedServiceDiscards.setStatus("mandatory")
_LapbcnvSapTxResets_Type = Counter32
_LapbcnvSapTxResets_Object = MibTableColumn
lapbcnvSapTxResets = _LapbcnvSapTxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 16),
    _LapbcnvSapTxResets_Type()
)
lapbcnvSapTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapTxResets.setStatus("mandatory")
_LapbcnvSapRxResets_Type = Counter32
_LapbcnvSapRxResets_Object = MibTableColumn
lapbcnvSapRxResets = _LapbcnvSapRxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 10, 1, 17),
    _LapbcnvSapRxResets_Type()
)
lapbcnvSapRxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSapRxResets.setStatus("mandatory")
_LapbcnvSysRouteTable_Object = MibTable
lapbcnvSysRouteTable = _LapbcnvSysRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11)
)
if mibBuilder.loadTexts:
    lapbcnvSysRouteTable.setStatus("mandatory")
_LapbcnvSysRouteEntry_Object = MibTableRow
lapbcnvSysRouteEntry = _LapbcnvSysRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1)
)
lapbcnvSysRouteEntry.setIndexNames(
    (0, "CXLapBConv-MIB", "lapbcnvSRSapNumber"),
)
if mibBuilder.loadTexts:
    lapbcnvSysRouteEntry.setStatus("mandatory")
_LapbcnvSRSapNumber_Type = SapIndex
_LapbcnvSRSapNumber_Object = MibTableColumn
lapbcnvSRSapNumber = _LapbcnvSRSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 1),
    _LapbcnvSRSapNumber_Type()
)
lapbcnvSRSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSRSapNumber.setStatus("mandatory")


class _LapbcnvSRRowStatus_Type(Integer32):
    """Custom type lapbcnvSRRowStatus based on Integer32"""
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


_LapbcnvSRRowStatus_Type.__name__ = "Integer32"
_LapbcnvSRRowStatus_Object = MibTableColumn
lapbcnvSRRowStatus = _LapbcnvSRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 2),
    _LapbcnvSRRowStatus_Type()
)
lapbcnvSRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbcnvSRRowStatus.setStatus("mandatory")
_LapbcnvSRDestAlias_Type = Alias
_LapbcnvSRDestAlias_Object = MibTableColumn
lapbcnvSRDestAlias = _LapbcnvSRDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 3),
    _LapbcnvSRDestAlias_Type()
)
lapbcnvSRDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbcnvSRDestAlias.setStatus("mandatory")
_LapbcnvSRSubRef_Type = SubRef
_LapbcnvSRSubRef_Object = MibTableColumn
lapbcnvSRSubRef = _LapbcnvSRSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 4),
    _LapbcnvSRSubRef_Type()
)
lapbcnvSRSubRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lapbcnvSRSubRef.setStatus("mandatory")


class _LapbcnvSRRouteStatus_Type(Integer32):
    """Custom type lapbcnvSRRouteStatus based on Integer32"""
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


_LapbcnvSRRouteStatus_Type.__name__ = "Integer32"
_LapbcnvSRRouteStatus_Object = MibTableColumn
lapbcnvSRRouteStatus = _LapbcnvSRRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 10),
    _LapbcnvSRRouteStatus_Type()
)
lapbcnvSRRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSRRouteStatus.setStatus("mandatory")


class _LapbcnvSRClearStatus_Type(Integer32):
    """Custom type lapbcnvSRClearStatus based on Integer32"""
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
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 2),
          ("localAllocFailure", 3),
          ("localDsnFailure", 13),
          ("localFcnFailure", 11),
          ("localNoAccess", 5),
          ("localPvcBusy", 9),
          ("localPvcDown", 7),
          ("localRefInUse", 14),
          ("mpeInvalidSubref", 17),
          ("noFailure", 1),
          ("remoteAliasNotFound", 15),
          ("remoteAllocFailure", 4),
          ("remoteFcnFailure", 12),
          ("remoteNoAccess", 6),
          ("remoteNoPvcService", 16),
          ("remotePvcBusy", 10),
          ("remotePvcDown", 8))
    )


_LapbcnvSRClearStatus_Type.__name__ = "Integer32"
_LapbcnvSRClearStatus_Object = MibTableColumn
lapbcnvSRClearStatus = _LapbcnvSRClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 28, 11, 1, 11),
    _LapbcnvSRClearStatus_Type()
)
lapbcnvSRClearStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lapbcnvSRClearStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXLapBConv-MIB",
    **{"PSapIndex": PSapIndex,
       "SubRef": SubRef,
       "lapbcnvSysRouteConnectInterval": lapbcnvSysRouteConnectInterval,
       "lapbcnvSapTable": lapbcnvSapTable,
       "lapbcnvSapEntry": lapbcnvSapEntry,
       "lapbcnvSapNumber": lapbcnvSapNumber,
       "lapbcnvSapRowStatus": lapbcnvSapRowStatus,
       "lapbcnvSapAlias": lapbcnvSapAlias,
       "lapbcnvSapControl": lapbcnvSapControl,
       "lapbcnvSapState": lapbcnvSapState,
       "lapbcnvSapTxFrames": lapbcnvSapTxFrames,
       "lapbcnvSapRxFrames": lapbcnvSapRxFrames,
       "lapbcnvSapTxOctets": lapbcnvSapTxOctets,
       "lapbcnvSapRxOctets": lapbcnvSapRxOctets,
       "lapbcnvSapOutSuccessfullConnects": lapbcnvSapOutSuccessfullConnects,
       "lapbcnvSapOutUnsuccessfullConnects": lapbcnvSapOutUnsuccessfullConnects,
       "lapbcnvSapInSuccessfullConnects": lapbcnvSapInSuccessfullConnects,
       "lapbcnvSapInUnsuccessfullConnects": lapbcnvSapInUnsuccessfullConnects,
       "lapbcnvSapUnopenedServiceDiscards": lapbcnvSapUnopenedServiceDiscards,
       "lapbcnvSapTxResets": lapbcnvSapTxResets,
       "lapbcnvSapRxResets": lapbcnvSapRxResets,
       "lapbcnvSysRouteTable": lapbcnvSysRouteTable,
       "lapbcnvSysRouteEntry": lapbcnvSysRouteEntry,
       "lapbcnvSRSapNumber": lapbcnvSRSapNumber,
       "lapbcnvSRRowStatus": lapbcnvSRRowStatus,
       "lapbcnvSRDestAlias": lapbcnvSRDestAlias,
       "lapbcnvSRSubRef": lapbcnvSRSubRef,
       "lapbcnvSRRouteStatus": lapbcnvSRRouteStatus,
       "lapbcnvSRClearStatus": lapbcnvSRClearStatus}
)
