# SNMP MIB module (CXGIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXGIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:29 2024
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
 ThruputClass,
 cxGim) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "ThruputClass",
    "cxGim")

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





class TypeIndex(Integer32):
    """Custom type TypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class DteIndex(Integer32):
    """Custom type DteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )





class SubRef(Integer32):
    """Custom type SubRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class PacketSize(Integer32):
    """Custom type PacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 10),
          ("bytes128", 7),
          ("bytes16", 4),
          ("bytes2048", 11),
          ("bytes256", 8),
          ("bytes32", 5),
          ("bytes4096", 12),
          ("bytes512", 9),
          ("bytes64", 6))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _GimSysRouteConnectInterval_Type(Integer32):
    """Custom type gimSysRouteConnectInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 900),
    )


_GimSysRouteConnectInterval_Type.__name__ = "Integer32"
_GimSysRouteConnectInterval_Object = MibScalar
gimSysRouteConnectInterval = _GimSysRouteConnectInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 1),
    _GimSysRouteConnectInterval_Type()
)
gimSysRouteConnectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSysRouteConnectInterval.setStatus("mandatory")


class _GimMibLevel_Type(Integer32):
    """Custom type gimMibLevel based on Integer32"""
    defaultValue = 0


_GimMibLevel_Object = MibScalar
gimMibLevel = _GimMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 2),
    _GimMibLevel_Type()
)
gimMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimMibLevel.setStatus("mandatory")
_GimSapTable_Object = MibTable
gimSapTable = _GimSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10)
)
if mibBuilder.loadTexts:
    gimSapTable.setStatus("mandatory")
_GimSapEntry_Object = MibTableRow
gimSapEntry = _GimSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1)
)
gimSapEntry.setIndexNames(
    (0, "CXGIM-MIB", "gimSapType"),
    (0, "CXGIM-MIB", "gimSapNumber"),
)
if mibBuilder.loadTexts:
    gimSapEntry.setStatus("mandatory")
_GimSapType_Type = TypeIndex
_GimSapType_Object = MibTableColumn
gimSapType = _GimSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 1),
    _GimSapType_Type()
)
gimSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapType.setStatus("mandatory")
_GimSapNumber_Type = PSapIndex
_GimSapNumber_Object = MibTableColumn
gimSapNumber = _GimSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 2),
    _GimSapNumber_Type()
)
gimSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapNumber.setStatus("mandatory")


class _GimSapRowStatus_Type(Integer32):
    """Custom type gimSapRowStatus based on Integer32"""
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


_GimSapRowStatus_Type.__name__ = "Integer32"
_GimSapRowStatus_Object = MibTableColumn
gimSapRowStatus = _GimSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 3),
    _GimSapRowStatus_Type()
)
gimSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapRowStatus.setStatus("mandatory")
_GimSapAlias_Type = Alias
_GimSapAlias_Object = MibTableColumn
gimSapAlias = _GimSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 4),
    _GimSapAlias_Type()
)
gimSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapAlias.setStatus("mandatory")
_GimSapCompanionAlias_Type = Alias
_GimSapCompanionAlias_Object = MibTableColumn
gimSapCompanionAlias = _GimSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 5),
    _GimSapCompanionAlias_Type()
)
gimSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapCompanionAlias.setStatus("mandatory")


class _GimSapInactivityTimer_Type(Integer32):
    """Custom type gimSapInactivityTimer based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_GimSapInactivityTimer_Type.__name__ = "Integer32"
_GimSapInactivityTimer_Object = MibTableColumn
gimSapInactivityTimer = _GimSapInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 6),
    _GimSapInactivityTimer_Type()
)
gimSapInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapInactivityTimer.setStatus("mandatory")


class _GimSapProtocolId_Type(DisplayString):
    """Custom type gimSapProtocolId based on DisplayString"""
    defaultValue = OctetString("01,00,00,00")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 11),
    )


_GimSapProtocolId_Type.__name__ = "DisplayString"
_GimSapProtocolId_Object = MibTableColumn
gimSapProtocolId = _GimSapProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 7),
    _GimSapProtocolId_Type()
)
gimSapProtocolId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapProtocolId.setStatus("mandatory")


class _GimSapAddress_Type(DisplayString):
    """Custom type gimSapAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_GimSapAddress_Type.__name__ = "DisplayString"
_GimSapAddress_Object = MibTableColumn
gimSapAddress = _GimSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 8),
    _GimSapAddress_Type()
)
gimSapAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapAddress.setStatus("mandatory")


class _GimSapControl_Type(Integer32):
    """Custom type gimSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_GimSapControl_Type.__name__ = "Integer32"
_GimSapControl_Object = MibTableColumn
gimSapControl = _GimSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 10),
    _GimSapControl_Type()
)
gimSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gimSapControl.setStatus("mandatory")


class _GimSapState_Type(Integer32):
    """Custom type gimSapState based on Integer32"""
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


_GimSapState_Type.__name__ = "Integer32"
_GimSapState_Object = MibTableColumn
gimSapState = _GimSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 12),
    _GimSapState_Type()
)
gimSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapState.setStatus("mandatory")


class _GimSapLinkState_Type(Integer32):
    """Custom type gimSapLinkState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("inProgress", 2),
          ("notConnected", 1))
    )


_GimSapLinkState_Type.__name__ = "Integer32"
_GimSapLinkState_Object = MibTableColumn
gimSapLinkState = _GimSapLinkState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 13),
    _GimSapLinkState_Type()
)
gimSapLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapLinkState.setStatus("mandatory")
_GimSapTxFrames_Type = Counter32
_GimSapTxFrames_Object = MibTableColumn
gimSapTxFrames = _GimSapTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 15),
    _GimSapTxFrames_Type()
)
gimSapTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapTxFrames.setStatus("mandatory")
_GimSapRxFrames_Type = Counter32
_GimSapRxFrames_Object = MibTableColumn
gimSapRxFrames = _GimSapRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 16),
    _GimSapRxFrames_Type()
)
gimSapRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapRxFrames.setStatus("mandatory")
_GimSapTxOctets_Type = Counter32
_GimSapTxOctets_Object = MibTableColumn
gimSapTxOctets = _GimSapTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 17),
    _GimSapTxOctets_Type()
)
gimSapTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapTxOctets.setStatus("mandatory")
_GimSapRxOctets_Type = Counter32
_GimSapRxOctets_Object = MibTableColumn
gimSapRxOctets = _GimSapRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 18),
    _GimSapRxOctets_Type()
)
gimSapRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapRxOctets.setStatus("mandatory")
_GimSapOutSuccessfullConnects_Type = Counter32
_GimSapOutSuccessfullConnects_Object = MibTableColumn
gimSapOutSuccessfullConnects = _GimSapOutSuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 19),
    _GimSapOutSuccessfullConnects_Type()
)
gimSapOutSuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapOutSuccessfullConnects.setStatus("mandatory")
_GimSapOutUnsuccessfullConnects_Type = Counter32
_GimSapOutUnsuccessfullConnects_Object = MibTableColumn
gimSapOutUnsuccessfullConnects = _GimSapOutUnsuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 20),
    _GimSapOutUnsuccessfullConnects_Type()
)
gimSapOutUnsuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapOutUnsuccessfullConnects.setStatus("mandatory")
_GimSapInSuccessfullConnects_Type = Counter32
_GimSapInSuccessfullConnects_Object = MibTableColumn
gimSapInSuccessfullConnects = _GimSapInSuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 21),
    _GimSapInSuccessfullConnects_Type()
)
gimSapInSuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapInSuccessfullConnects.setStatus("mandatory")
_GimSapInUnsuccessfullConnects_Type = Counter32
_GimSapInUnsuccessfullConnects_Object = MibTableColumn
gimSapInUnsuccessfullConnects = _GimSapInUnsuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 22),
    _GimSapInUnsuccessfullConnects_Type()
)
gimSapInUnsuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapInUnsuccessfullConnects.setStatus("mandatory")
_GimSapUnopenedServiceDiscards_Type = Counter32
_GimSapUnopenedServiceDiscards_Object = MibTableColumn
gimSapUnopenedServiceDiscards = _GimSapUnopenedServiceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 23),
    _GimSapUnopenedServiceDiscards_Type()
)
gimSapUnopenedServiceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapUnopenedServiceDiscards.setStatus("mandatory")
_GimSapTxResets_Type = Counter32
_GimSapTxResets_Object = MibTableColumn
gimSapTxResets = _GimSapTxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 24),
    _GimSapTxResets_Type()
)
gimSapTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapTxResets.setStatus("mandatory")
_GimSapRxResets_Type = Counter32
_GimSapRxResets_Object = MibTableColumn
gimSapRxResets = _GimSapRxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 25),
    _GimSapRxResets_Type()
)
gimSapRxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSapRxResets.setStatus("mandatory")


class _GimSapRxThruputClass_Type(ThruputClass):
    """Custom type gimSapRxThruputClass based on ThruputClass"""


_GimSapRxThruputClass_Object = MibTableColumn
gimSapRxThruputClass = _GimSapRxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 50),
    _GimSapRxThruputClass_Type()
)
gimSapRxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapRxThruputClass.setStatus("mandatory")


class _GimSapTxThruputClass_Type(ThruputClass):
    """Custom type gimSapTxThruputClass based on ThruputClass"""


_GimSapTxThruputClass_Object = MibTableColumn
gimSapTxThruputClass = _GimSapTxThruputClass_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 51),
    _GimSapTxThruputClass_Type()
)
gimSapTxThruputClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapTxThruputClass.setStatus("mandatory")


class _GimSapTxPacketSize_Type(PacketSize):
    """Custom type gimSapTxPacketSize based on PacketSize"""


_GimSapTxPacketSize_Object = MibTableColumn
gimSapTxPacketSize = _GimSapTxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 52),
    _GimSapTxPacketSize_Type()
)
gimSapTxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapTxPacketSize.setStatus("mandatory")


class _GimSapRxPacketSize_Type(PacketSize):
    """Custom type gimSapRxPacketSize based on PacketSize"""


_GimSapRxPacketSize_Object = MibTableColumn
gimSapRxPacketSize = _GimSapRxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 53),
    _GimSapRxPacketSize_Type()
)
gimSapRxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapRxPacketSize.setStatus("mandatory")


class _GimSapTxWindowSize_Type(Integer32):
    """Custom type gimSapTxWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_GimSapTxWindowSize_Type.__name__ = "Integer32"
_GimSapTxWindowSize_Object = MibTableColumn
gimSapTxWindowSize = _GimSapTxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 54),
    _GimSapTxWindowSize_Type()
)
gimSapTxWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapTxWindowSize.setStatus("mandatory")


class _GimSapRxWindowSize_Type(Integer32):
    """Custom type gimSapRxWindowSize based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_GimSapRxWindowSize_Type.__name__ = "Integer32"
_GimSapRxWindowSize_Object = MibTableColumn
gimSapRxWindowSize = _GimSapRxWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 10, 1, 55),
    _GimSapRxWindowSize_Type()
)
gimSapRxWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSapRxWindowSize.setStatus("mandatory")
_GimSysRouteTable_Object = MibTable
gimSysRouteTable = _GimSysRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11)
)
if mibBuilder.loadTexts:
    gimSysRouteTable.setStatus("mandatory")
_GimSysRouteEntry_Object = MibTableRow
gimSysRouteEntry = _GimSysRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1)
)
gimSysRouteEntry.setIndexNames(
    (0, "CXGIM-MIB", "gimSRSapType"),
    (0, "CXGIM-MIB", "gimSRSapNumber"),
)
if mibBuilder.loadTexts:
    gimSysRouteEntry.setStatus("mandatory")
_GimSRSapType_Type = TypeIndex
_GimSRSapType_Object = MibTableColumn
gimSRSapType = _GimSRSapType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 1),
    _GimSRSapType_Type()
)
gimSRSapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSRSapType.setStatus("mandatory")
_GimSRSapNumber_Type = SapIndex
_GimSRSapNumber_Object = MibTableColumn
gimSRSapNumber = _GimSRSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 2),
    _GimSRSapNumber_Type()
)
gimSRSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSRSapNumber.setStatus("mandatory")


class _GimSRRowStatus_Type(Integer32):
    """Custom type gimSRRowStatus based on Integer32"""
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


_GimSRRowStatus_Type.__name__ = "Integer32"
_GimSRRowStatus_Object = MibTableColumn
gimSRRowStatus = _GimSRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 3),
    _GimSRRowStatus_Type()
)
gimSRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSRRowStatus.setStatus("mandatory")
_GimSRDestAlias_Type = Alias
_GimSRDestAlias_Object = MibTableColumn
gimSRDestAlias = _GimSRDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 4),
    _GimSRDestAlias_Type()
)
gimSRDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSRDestAlias.setStatus("mandatory")
_GimSRSubRef_Type = SubRef
_GimSRSubRef_Object = MibTableColumn
gimSRSubRef = _GimSRSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 5),
    _GimSRSubRef_Type()
)
gimSRSubRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gimSRSubRef.setStatus("mandatory")


class _GimSRRouteStatus_Type(Integer32):
    """Custom type gimSRRouteStatus based on Integer32"""
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


_GimSRRouteStatus_Type.__name__ = "Integer32"
_GimSRRouteStatus_Object = MibTableColumn
gimSRRouteStatus = _GimSRRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 10),
    _GimSRRouteStatus_Type()
)
gimSRRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSRRouteStatus.setStatus("mandatory")


class _GimSRClearStatus_Type(Integer32):
    """Custom type gimSRClearStatus based on Integer32"""
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


_GimSRClearStatus_Type.__name__ = "Integer32"
_GimSRClearStatus_Object = MibTableColumn
gimSRClearStatus = _GimSRClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 11, 1, 11),
    _GimSRClearStatus_Type()
)
gimSRClearStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gimSRClearStatus.setStatus("mandatory")
_XimDteTable_Object = MibTable
ximDteTable = _XimDteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12)
)
if mibBuilder.loadTexts:
    ximDteTable.setStatus("mandatory")
_XimDteEntry_Object = MibTableRow
ximDteEntry = _XimDteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1)
)
ximDteEntry.setIndexNames(
    (0, "CXGIM-MIB", "ximDteSapNumber"),
    (0, "CXGIM-MIB", "ximDteDteNumber"),
)
if mibBuilder.loadTexts:
    ximDteEntry.setStatus("mandatory")
_XimDteSapNumber_Type = SapIndex
_XimDteSapNumber_Object = MibTableColumn
ximDteSapNumber = _XimDteSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 1),
    _XimDteSapNumber_Type()
)
ximDteSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ximDteSapNumber.setStatus("mandatory")
_XimDteDteNumber_Type = DteIndex
_XimDteDteNumber_Object = MibTableColumn
ximDteDteNumber = _XimDteDteNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 2),
    _XimDteDteNumber_Type()
)
ximDteDteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ximDteDteNumber.setStatus("mandatory")


class _XimDteRowStatus_Type(Integer32):
    """Custom type ximDteRowStatus based on Integer32"""
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


_XimDteRowStatus_Type.__name__ = "Integer32"
_XimDteRowStatus_Object = MibTableColumn
ximDteRowStatus = _XimDteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 3),
    _XimDteRowStatus_Type()
)
ximDteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ximDteRowStatus.setStatus("mandatory")


class _XimDteCalledAddress_Type(DisplayString):
    """Custom type ximDteCalledAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_XimDteCalledAddress_Type.__name__ = "DisplayString"
_XimDteCalledAddress_Object = MibTableColumn
ximDteCalledAddress = _XimDteCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 5),
    _XimDteCalledAddress_Type()
)
ximDteCalledAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ximDteCalledAddress.setStatus("mandatory")


class _XimDteFacilityField_Type(DisplayString):
    """Custom type ximDteFacilityField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_XimDteFacilityField_Type.__name__ = "DisplayString"
_XimDteFacilityField_Object = MibTableColumn
ximDteFacilityField = _XimDteFacilityField_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 12),
    _XimDteFacilityField_Type()
)
ximDteFacilityField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ximDteFacilityField.setStatus("mandatory")


class _XimDteUserDataField_Type(DisplayString):
    """Custom type ximDteUserDataField based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_XimDteUserDataField_Type.__name__ = "DisplayString"
_XimDteUserDataField_Object = MibTableColumn
ximDteUserDataField = _XimDteUserDataField_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 55, 12, 1, 13),
    _XimDteUserDataField_Type()
)
ximDteUserDataField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ximDteUserDataField.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXGIM-MIB",
    **{"PSapIndex": PSapIndex,
       "TypeIndex": TypeIndex,
       "DteIndex": DteIndex,
       "SubRef": SubRef,
       "PacketSize": PacketSize,
       "gimSysRouteConnectInterval": gimSysRouteConnectInterval,
       "gimMibLevel": gimMibLevel,
       "gimSapTable": gimSapTable,
       "gimSapEntry": gimSapEntry,
       "gimSapType": gimSapType,
       "gimSapNumber": gimSapNumber,
       "gimSapRowStatus": gimSapRowStatus,
       "gimSapAlias": gimSapAlias,
       "gimSapCompanionAlias": gimSapCompanionAlias,
       "gimSapInactivityTimer": gimSapInactivityTimer,
       "gimSapProtocolId": gimSapProtocolId,
       "gimSapAddress": gimSapAddress,
       "gimSapControl": gimSapControl,
       "gimSapState": gimSapState,
       "gimSapLinkState": gimSapLinkState,
       "gimSapTxFrames": gimSapTxFrames,
       "gimSapRxFrames": gimSapRxFrames,
       "gimSapTxOctets": gimSapTxOctets,
       "gimSapRxOctets": gimSapRxOctets,
       "gimSapOutSuccessfullConnects": gimSapOutSuccessfullConnects,
       "gimSapOutUnsuccessfullConnects": gimSapOutUnsuccessfullConnects,
       "gimSapInSuccessfullConnects": gimSapInSuccessfullConnects,
       "gimSapInUnsuccessfullConnects": gimSapInUnsuccessfullConnects,
       "gimSapUnopenedServiceDiscards": gimSapUnopenedServiceDiscards,
       "gimSapTxResets": gimSapTxResets,
       "gimSapRxResets": gimSapRxResets,
       "gimSapRxThruputClass": gimSapRxThruputClass,
       "gimSapTxThruputClass": gimSapTxThruputClass,
       "gimSapTxPacketSize": gimSapTxPacketSize,
       "gimSapRxPacketSize": gimSapRxPacketSize,
       "gimSapTxWindowSize": gimSapTxWindowSize,
       "gimSapRxWindowSize": gimSapRxWindowSize,
       "gimSysRouteTable": gimSysRouteTable,
       "gimSysRouteEntry": gimSysRouteEntry,
       "gimSRSapType": gimSRSapType,
       "gimSRSapNumber": gimSRSapNumber,
       "gimSRRowStatus": gimSRRowStatus,
       "gimSRDestAlias": gimSRDestAlias,
       "gimSRSubRef": gimSRSubRef,
       "gimSRRouteStatus": gimSRRouteStatus,
       "gimSRClearStatus": gimSRClearStatus,
       "ximDteTable": ximDteTable,
       "ximDteEntry": ximDteEntry,
       "ximDteSapNumber": ximDteSapNumber,
       "ximDteDteNumber": ximDteDteNumber,
       "ximDteRowStatus": ximDteRowStatus,
       "ximDteCalledAddress": ximDteCalledAddress,
       "ximDteFacilityField": ximDteFacilityField,
       "ximDteUserDataField": ximDteUserDataField}
)
