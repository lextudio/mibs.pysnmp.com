# SNMP MIB module (CXAtmDxi-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXAtmDxi-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:05 2024
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
 cxAtmDxi) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxAtmDxi")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
        ValueRangeConstraint(0, 0),
    )





class SubRef(Integer32):
    """Custom type SubRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Dfa(Integer32):
    """Custom type Dfa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )





class DfaX(Integer32):
    """Custom type DfaX based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777216),
    )





class Vpi(Integer32):
    """Custom type Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class Vci(Integer32):
    """Custom type Vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AtmDxiMibLevel_Type(Integer32):
    """Custom type atmDxiMibLevel based on Integer32"""
    defaultValue = 0


_AtmDxiMibLevel_Object = MibScalar
atmDxiMibLevel = _AtmDxiMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 1),
    _AtmDxiMibLevel_Type()
)
atmDxiMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiMibLevel.setStatus("mandatory")
_AtmDxiTranslationDfa_Type = DfaX
_AtmDxiTranslationDfa_Object = MibScalar
atmDxiTranslationDfa = _AtmDxiTranslationDfa_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 2),
    _AtmDxiTranslationDfa_Type()
)
atmDxiTranslationDfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiTranslationDfa.setStatus("mandatory")
_AtmDxiTranslationVpi_Type = Vpi
_AtmDxiTranslationVpi_Object = MibScalar
atmDxiTranslationVpi = _AtmDxiTranslationVpi_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 3),
    _AtmDxiTranslationVpi_Type()
)
atmDxiTranslationVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiTranslationVpi.setStatus("mandatory")
_AtmDxiTranslationVci_Type = Vci
_AtmDxiTranslationVci_Object = MibScalar
atmDxiTranslationVci = _AtmDxiTranslationVci_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 4),
    _AtmDxiTranslationVci_Type()
)
atmDxiTranslationVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiTranslationVci.setStatus("mandatory")


class _AtmDxiTranslationMode_Type(Integer32):
    """Custom type atmDxiTranslationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourbytes", 2),
          ("twobytes", 1))
    )


_AtmDxiTranslationMode_Type.__name__ = "Integer32"
_AtmDxiTranslationMode_Object = MibScalar
atmDxiTranslationMode = _AtmDxiTranslationMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 5),
    _AtmDxiTranslationMode_Type()
)
atmDxiTranslationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiTranslationMode.setStatus("mandatory")
_AtmDxiPSapTable_Object = MibTable
atmDxiPSapTable = _AtmDxiPSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10)
)
if mibBuilder.loadTexts:
    atmDxiPSapTable.setStatus("mandatory")
_AtmDxiPSapEntry_Object = MibTableRow
atmDxiPSapEntry = _AtmDxiPSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1)
)
atmDxiPSapEntry.setIndexNames(
    (0, "CXAtmDxi-MIB", "atmDxiPSapNumber"),
)
if mibBuilder.loadTexts:
    atmDxiPSapEntry.setStatus("mandatory")
_AtmDxiPSapNumber_Type = PSapIndex
_AtmDxiPSapNumber_Object = MibTableColumn
atmDxiPSapNumber = _AtmDxiPSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 1),
    _AtmDxiPSapNumber_Type()
)
atmDxiPSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapNumber.setStatus("mandatory")


class _AtmDxiPSapConnectTimer_Type(Integer32):
    """Custom type atmDxiPSapConnectTimer based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 600),
    )


_AtmDxiPSapConnectTimer_Type.__name__ = "Integer32"
_AtmDxiPSapConnectTimer_Object = MibTableColumn
atmDxiPSapConnectTimer = _AtmDxiPSapConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 5),
    _AtmDxiPSapConnectTimer_Type()
)
atmDxiPSapConnectTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiPSapConnectTimer.setStatus("mandatory")


class _AtmDxiPSapControl_Type(Integer32):
    """Custom type atmDxiPSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_AtmDxiPSapControl_Type.__name__ = "Integer32"
_AtmDxiPSapControl_Object = MibTableColumn
atmDxiPSapControl = _AtmDxiPSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 10),
    _AtmDxiPSapControl_Type()
)
atmDxiPSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmDxiPSapControl.setStatus("mandatory")


class _AtmDxiPSapState_Type(Integer32):
    """Custom type atmDxiPSapState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("connected", 4),
          ("offline", 1))
    )


_AtmDxiPSapState_Type.__name__ = "Integer32"
_AtmDxiPSapState_Object = MibTableColumn
atmDxiPSapState = _AtmDxiPSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 15),
    _AtmDxiPSapState_Type()
)
atmDxiPSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapState.setStatus("mandatory")
_AtmDxiPSapTxFrames_Type = Counter32
_AtmDxiPSapTxFrames_Object = MibTableColumn
atmDxiPSapTxFrames = _AtmDxiPSapTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 20),
    _AtmDxiPSapTxFrames_Type()
)
atmDxiPSapTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapTxFrames.setStatus("mandatory")
_AtmDxiPSapRxFrames_Type = Counter32
_AtmDxiPSapRxFrames_Object = MibTableColumn
atmDxiPSapRxFrames = _AtmDxiPSapRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 21),
    _AtmDxiPSapRxFrames_Type()
)
atmDxiPSapRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapRxFrames.setStatus("mandatory")
_AtmDxiPSapTxOctets_Type = Counter32
_AtmDxiPSapTxOctets_Object = MibTableColumn
atmDxiPSapTxOctets = _AtmDxiPSapTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 22),
    _AtmDxiPSapTxOctets_Type()
)
atmDxiPSapTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapTxOctets.setStatus("mandatory")
_AtmDxiPSapRxOctets_Type = Counter32
_AtmDxiPSapRxOctets_Object = MibTableColumn
atmDxiPSapRxOctets = _AtmDxiPSapRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 23),
    _AtmDxiPSapRxOctets_Type()
)
atmDxiPSapRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapRxOctets.setStatus("mandatory")
_AtmDxiPSapOutSuccessfullConnects_Type = Counter32
_AtmDxiPSapOutSuccessfullConnects_Object = MibTableColumn
atmDxiPSapOutSuccessfullConnects = _AtmDxiPSapOutSuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 24),
    _AtmDxiPSapOutSuccessfullConnects_Type()
)
atmDxiPSapOutSuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapOutSuccessfullConnects.setStatus("mandatory")
_AtmDxiPSapOutUnsuccessfullConnects_Type = Counter32
_AtmDxiPSapOutUnsuccessfullConnects_Object = MibTableColumn
atmDxiPSapOutUnsuccessfullConnects = _AtmDxiPSapOutUnsuccessfullConnects_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 25),
    _AtmDxiPSapOutUnsuccessfullConnects_Type()
)
atmDxiPSapOutUnsuccessfullConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapOutUnsuccessfullConnects.setStatus("mandatory")
_AtmDxiPSapInConnectsReceived_Type = Counter32
_AtmDxiPSapInConnectsReceived_Object = MibTableColumn
atmDxiPSapInConnectsReceived = _AtmDxiPSapInConnectsReceived_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 26),
    _AtmDxiPSapInConnectsReceived_Type()
)
atmDxiPSapInConnectsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapInConnectsReceived.setStatus("mandatory")
_AtmDxiPSapTxResets_Type = Counter32
_AtmDxiPSapTxResets_Object = MibTableColumn
atmDxiPSapTxResets = _AtmDxiPSapTxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 27),
    _AtmDxiPSapTxResets_Type()
)
atmDxiPSapTxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapTxResets.setStatus("mandatory")
_AtmDxiPSapRxResets_Type = Counter32
_AtmDxiPSapRxResets_Object = MibTableColumn
atmDxiPSapRxResets = _AtmDxiPSapRxResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 28),
    _AtmDxiPSapRxResets_Type()
)
atmDxiPSapRxResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapRxResets.setStatus("mandatory")
_AtmDxiPSapNoServiceDiscards_Type = Counter32
_AtmDxiPSapNoServiceDiscards_Object = MibTableColumn
atmDxiPSapNoServiceDiscards = _AtmDxiPSapNoServiceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 35),
    _AtmDxiPSapNoServiceDiscards_Type()
)
atmDxiPSapNoServiceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapNoServiceDiscards.setStatus("mandatory")
_AtmDxiPSapCongestionDiscards_Type = Counter32
_AtmDxiPSapCongestionDiscards_Object = MibTableColumn
atmDxiPSapCongestionDiscards = _AtmDxiPSapCongestionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 10, 1, 36),
    _AtmDxiPSapCongestionDiscards_Type()
)
atmDxiPSapCongestionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiPSapCongestionDiscards.setStatus("mandatory")
_AtmDxiSapTable_Object = MibTable
atmDxiSapTable = _AtmDxiSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11)
)
if mibBuilder.loadTexts:
    atmDxiSapTable.setStatus("mandatory")
_AtmDxiSapEntry_Object = MibTableRow
atmDxiSapEntry = _AtmDxiSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1)
)
atmDxiSapEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    atmDxiSapEntry.setStatus("mandatory")


class _AtmDxiSapMode_Type(Integer32):
    """Custom type atmDxiSapMode based on Integer32"""
    defaultValue = 1

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
        *(("mode-1a", 1),
          ("mode-1b", 2),
          ("mode-2", 3),
          ("modeLoopback", 5),
          ("modeTransparent", 4))
    )


_AtmDxiSapMode_Type.__name__ = "Integer32"
_AtmDxiSapMode_Object = MibTableColumn
atmDxiSapMode = _AtmDxiSapMode_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 5),
    _AtmDxiSapMode_Type()
)
atmDxiSapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiSapMode.setStatus("mandatory")
_AtmDxiSapTransparentDfa_Type = Dfa
_AtmDxiSapTransparentDfa_Object = MibTableColumn
atmDxiSapTransparentDfa = _AtmDxiSapTransparentDfa_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 6),
    _AtmDxiSapTransparentDfa_Type()
)
atmDxiSapTransparentDfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiSapTransparentDfa.setStatus("mandatory")


class _AtmDxiSapControl_Type(Integer32):
    """Custom type atmDxiSapControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearStats", 1)
    )


_AtmDxiSapControl_Type.__name__ = "Integer32"
_AtmDxiSapControl_Object = MibTableColumn
atmDxiSapControl = _AtmDxiSapControl_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 10),
    _AtmDxiSapControl_Type()
)
atmDxiSapControl.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    atmDxiSapControl.setStatus("mandatory")
_AtmDxiSapRxLmiFrames_Type = Counter32
_AtmDxiSapRxLmiFrames_Object = MibTableColumn
atmDxiSapRxLmiFrames = _AtmDxiSapRxLmiFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 20),
    _AtmDxiSapRxLmiFrames_Type()
)
atmDxiSapRxLmiFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSapRxLmiFrames.setStatus("mandatory")
_AtmDxiSapNoRouteDiscards_Type = Counter32
_AtmDxiSapNoRouteDiscards_Object = MibTableColumn
atmDxiSapNoRouteDiscards = _AtmDxiSapNoRouteDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 21),
    _AtmDxiSapNoRouteDiscards_Type()
)
atmDxiSapNoRouteDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSapNoRouteDiscards.setStatus("mandatory")
_AtmDxiSapRxInvalidDiscards_Type = Counter32
_AtmDxiSapRxInvalidDiscards_Object = MibTableColumn
atmDxiSapRxInvalidDiscards = _AtmDxiSapRxInvalidDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 22),
    _AtmDxiSapRxInvalidDiscards_Type()
)
atmDxiSapRxInvalidDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSapRxInvalidDiscards.setStatus("mandatory")
_AtmDxiSapCongestionDiscards_Type = Counter32
_AtmDxiSapCongestionDiscards_Object = MibTableColumn
atmDxiSapCongestionDiscards = _AtmDxiSapCongestionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 23),
    _AtmDxiSapCongestionDiscards_Type()
)
atmDxiSapCongestionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSapCongestionDiscards.setStatus("mandatory")
_AtmDxiSapFlowControlDiscards_Type = Counter32
_AtmDxiSapFlowControlDiscards_Object = MibTableColumn
atmDxiSapFlowControlDiscards = _AtmDxiSapFlowControlDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 11, 1, 24),
    _AtmDxiSapFlowControlDiscards_Type()
)
atmDxiSapFlowControlDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSapFlowControlDiscards.setStatus("mandatory")
_AtmDxiSysRouteTable_Object = MibTable
atmDxiSysRouteTable = _AtmDxiSysRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12)
)
if mibBuilder.loadTexts:
    atmDxiSysRouteTable.setStatus("mandatory")
_AtmDxiSysRouteEntry_Object = MibTableRow
atmDxiSysRouteEntry = _AtmDxiSysRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12, 1)
)
atmDxiSysRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CXAtmDxi-MIB", "atmDxiSRDxiFrameAddress"),
)
if mibBuilder.loadTexts:
    atmDxiSysRouteEntry.setStatus("mandatory")
_AtmDxiSRDxiFrameAddress_Type = Dfa
_AtmDxiSRDxiFrameAddress_Object = MibTableColumn
atmDxiSRDxiFrameAddress = _AtmDxiSRDxiFrameAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12, 1, 1),
    _AtmDxiSRDxiFrameAddress_Type()
)
atmDxiSRDxiFrameAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRDxiFrameAddress.setStatus("mandatory")


class _AtmDxiSRRowStatus_Type(Integer32):
    """Custom type atmDxiSRRowStatus based on Integer32"""
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


_AtmDxiSRRowStatus_Type.__name__ = "Integer32"
_AtmDxiSRRowStatus_Object = MibTableColumn
atmDxiSRRowStatus = _AtmDxiSRRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12, 1, 2),
    _AtmDxiSRRowStatus_Type()
)
atmDxiSRRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiSRRowStatus.setStatus("mandatory")
_AtmDxiSRDestAlias_Type = Alias
_AtmDxiSRDestAlias_Object = MibTableColumn
atmDxiSRDestAlias = _AtmDxiSRDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12, 1, 3),
    _AtmDxiSRDestAlias_Type()
)
atmDxiSRDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiSRDestAlias.setStatus("mandatory")


class _AtmDxiSRSubRef_Type(SubRef):
    """Custom type atmDxiSRSubRef based on SubRef"""
    defaultValue = 0


_AtmDxiSRSubRef_Object = MibTableColumn
atmDxiSRSubRef = _AtmDxiSRSubRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12, 1, 4),
    _AtmDxiSRSubRef_Type()
)
atmDxiSRSubRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDxiSRSubRef.setStatus("mandatory")


class _AtmDxiSRRouteState_Type(Integer32):
    """Custom type atmDxiSRRouteState based on Integer32"""
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
        *(("connected", 4),
          ("connectedFlowOff", 5),
          ("inProgress", 3),
          ("notConnected", 2),
          ("offLine", 1))
    )


_AtmDxiSRRouteState_Type.__name__ = "Integer32"
_AtmDxiSRRouteState_Object = MibTableColumn
atmDxiSRRouteState = _AtmDxiSRRouteState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12, 1, 10),
    _AtmDxiSRRouteState_Type()
)
atmDxiSRRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRRouteState.setStatus("mandatory")


class _AtmDxiSRFailureReason_Type(Integer32):
    """Custom type atmDxiSRFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              10,
              11,
              12,
              13,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("internalError", 2),
          ("localAllocFailure", 3),
          ("localDsnFailure", 13),
          ("localFcnFailure", 11),
          ("localNoAccess", 5),
          ("mpeInvalidSubref", 17),
          ("noFailure", 1),
          ("remoteAliasNotFound", 15),
          ("remoteAllocFailure", 4),
          ("remoteFcnFailure", 12),
          ("remoteNoAccess", 6),
          ("remoteNoPvcService", 16),
          ("remotePvcBusy", 10),
          ("remotePvcDown", 8),
          ("routeStalled", 18))
    )


_AtmDxiSRFailureReason_Type.__name__ = "Integer32"
_AtmDxiSRFailureReason_Object = MibTableColumn
atmDxiSRFailureReason = _AtmDxiSRFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 12, 1, 11),
    _AtmDxiSRFailureReason_Type()
)
atmDxiSRFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRFailureReason.setStatus("mandatory")
_AtmDxiSysRouteStatsTable_Object = MibTable
atmDxiSysRouteStatsTable = _AtmDxiSysRouteStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13)
)
if mibBuilder.loadTexts:
    atmDxiSysRouteStatsTable.setStatus("mandatory")
_AtmDxiSysRouteStatsEntry_Object = MibTableRow
atmDxiSysRouteStatsEntry = _AtmDxiSysRouteStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1)
)
atmDxiSysRouteStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CXAtmDxi-MIB", "atmDxiSRStatsDxiFrameAddress"),
)
if mibBuilder.loadTexts:
    atmDxiSysRouteStatsEntry.setStatus("mandatory")
_AtmDxiSRStatsDxiFrameAddress_Type = Dfa
_AtmDxiSRStatsDxiFrameAddress_Object = MibTableColumn
atmDxiSRStatsDxiFrameAddress = _AtmDxiSRStatsDxiFrameAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 1),
    _AtmDxiSRStatsDxiFrameAddress_Type()
)
atmDxiSRStatsDxiFrameAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsDxiFrameAddress.setStatus("mandatory")
_AtmDxiSRStatsCreationTime_Type = TimeTicks
_AtmDxiSRStatsCreationTime_Object = MibTableColumn
atmDxiSRStatsCreationTime = _AtmDxiSRStatsCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 2),
    _AtmDxiSRStatsCreationTime_Type()
)
atmDxiSRStatsCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsCreationTime.setStatus("mandatory")


class _AtmDxiSRStatsNegotiatedDataSize_Type(Integer32):
    """Custom type atmDxiSRStatsNegotiatedDataSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AtmDxiSRStatsNegotiatedDataSize_Type.__name__ = "Integer32"
_AtmDxiSRStatsNegotiatedDataSize_Object = MibTableColumn
atmDxiSRStatsNegotiatedDataSize = _AtmDxiSRStatsNegotiatedDataSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 3),
    _AtmDxiSRStatsNegotiatedDataSize_Type()
)
atmDxiSRStatsNegotiatedDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsNegotiatedDataSize.setStatus("mandatory")
_AtmDxiSRStatsTxFrames_Type = Counter32
_AtmDxiSRStatsTxFrames_Object = MibTableColumn
atmDxiSRStatsTxFrames = _AtmDxiSRStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 4),
    _AtmDxiSRStatsTxFrames_Type()
)
atmDxiSRStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsTxFrames.setStatus("mandatory")
_AtmDxiSRStatsRxFrames_Type = Counter32
_AtmDxiSRStatsRxFrames_Object = MibTableColumn
atmDxiSRStatsRxFrames = _AtmDxiSRStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 5),
    _AtmDxiSRStatsRxFrames_Type()
)
atmDxiSRStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsRxFrames.setStatus("mandatory")
_AtmDxiSRStatsTxOctets_Type = Counter32
_AtmDxiSRStatsTxOctets_Object = MibTableColumn
atmDxiSRStatsTxOctets = _AtmDxiSRStatsTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 6),
    _AtmDxiSRStatsTxOctets_Type()
)
atmDxiSRStatsTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsTxOctets.setStatus("mandatory")
_AtmDxiSRStatsRxOctets_Type = Counter32
_AtmDxiSRStatsRxOctets_Object = MibTableColumn
atmDxiSRStatsRxOctets = _AtmDxiSRStatsRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 7),
    _AtmDxiSRStatsRxOctets_Type()
)
atmDxiSRStatsRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsRxOctets.setStatus("mandatory")
_AtmDxiSRStatsFlowControlDiscards_Type = Counter32
_AtmDxiSRStatsFlowControlDiscards_Object = MibTableColumn
atmDxiSRStatsFlowControlDiscards = _AtmDxiSRStatsFlowControlDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 58, 13, 1, 8),
    _AtmDxiSRStatsFlowControlDiscards_Type()
)
atmDxiSRStatsFlowControlDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmDxiSRStatsFlowControlDiscards.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXAtmDxi-MIB",
    **{"PSapIndex": PSapIndex,
       "SubRef": SubRef,
       "Dfa": Dfa,
       "DfaX": DfaX,
       "Vpi": Vpi,
       "Vci": Vci,
       "atmDxiMibLevel": atmDxiMibLevel,
       "atmDxiTranslationDfa": atmDxiTranslationDfa,
       "atmDxiTranslationVpi": atmDxiTranslationVpi,
       "atmDxiTranslationVci": atmDxiTranslationVci,
       "atmDxiTranslationMode": atmDxiTranslationMode,
       "atmDxiPSapTable": atmDxiPSapTable,
       "atmDxiPSapEntry": atmDxiPSapEntry,
       "atmDxiPSapNumber": atmDxiPSapNumber,
       "atmDxiPSapConnectTimer": atmDxiPSapConnectTimer,
       "atmDxiPSapControl": atmDxiPSapControl,
       "atmDxiPSapState": atmDxiPSapState,
       "atmDxiPSapTxFrames": atmDxiPSapTxFrames,
       "atmDxiPSapRxFrames": atmDxiPSapRxFrames,
       "atmDxiPSapTxOctets": atmDxiPSapTxOctets,
       "atmDxiPSapRxOctets": atmDxiPSapRxOctets,
       "atmDxiPSapOutSuccessfullConnects": atmDxiPSapOutSuccessfullConnects,
       "atmDxiPSapOutUnsuccessfullConnects": atmDxiPSapOutUnsuccessfullConnects,
       "atmDxiPSapInConnectsReceived": atmDxiPSapInConnectsReceived,
       "atmDxiPSapTxResets": atmDxiPSapTxResets,
       "atmDxiPSapRxResets": atmDxiPSapRxResets,
       "atmDxiPSapNoServiceDiscards": atmDxiPSapNoServiceDiscards,
       "atmDxiPSapCongestionDiscards": atmDxiPSapCongestionDiscards,
       "atmDxiSapTable": atmDxiSapTable,
       "atmDxiSapEntry": atmDxiSapEntry,
       "atmDxiSapMode": atmDxiSapMode,
       "atmDxiSapTransparentDfa": atmDxiSapTransparentDfa,
       "atmDxiSapControl": atmDxiSapControl,
       "atmDxiSapRxLmiFrames": atmDxiSapRxLmiFrames,
       "atmDxiSapNoRouteDiscards": atmDxiSapNoRouteDiscards,
       "atmDxiSapRxInvalidDiscards": atmDxiSapRxInvalidDiscards,
       "atmDxiSapCongestionDiscards": atmDxiSapCongestionDiscards,
       "atmDxiSapFlowControlDiscards": atmDxiSapFlowControlDiscards,
       "atmDxiSysRouteTable": atmDxiSysRouteTable,
       "atmDxiSysRouteEntry": atmDxiSysRouteEntry,
       "atmDxiSRDxiFrameAddress": atmDxiSRDxiFrameAddress,
       "atmDxiSRRowStatus": atmDxiSRRowStatus,
       "atmDxiSRDestAlias": atmDxiSRDestAlias,
       "atmDxiSRSubRef": atmDxiSRSubRef,
       "atmDxiSRRouteState": atmDxiSRRouteState,
       "atmDxiSRFailureReason": atmDxiSRFailureReason,
       "atmDxiSysRouteStatsTable": atmDxiSysRouteStatsTable,
       "atmDxiSysRouteStatsEntry": atmDxiSysRouteStatsEntry,
       "atmDxiSRStatsDxiFrameAddress": atmDxiSRStatsDxiFrameAddress,
       "atmDxiSRStatsCreationTime": atmDxiSRStatsCreationTime,
       "atmDxiSRStatsNegotiatedDataSize": atmDxiSRStatsNegotiatedDataSize,
       "atmDxiSRStatsTxFrames": atmDxiSRStatsTxFrames,
       "atmDxiSRStatsRxFrames": atmDxiSRStatsRxFrames,
       "atmDxiSRStatsTxOctets": atmDxiSRStatsTxOctets,
       "atmDxiSRStatsRxOctets": atmDxiSRStatsRxOctets,
       "atmDxiSRStatsFlowControlDiscards": atmDxiSRStatsFlowControlDiscards}
)
