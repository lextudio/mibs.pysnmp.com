# SNMP MIB module (EQUIPE-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQUIPE-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:17 2024
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

eqAtmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5022, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AtmCauseCode(Integer32, TextualConvention):
    status = "current"
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
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("aalParamsUnsupported30", 37),
          ("aalParamsUnsupported31", 30),
          ("accessInfoDiscarded", 21),
          ("bcapNotAuthorised", 25),
          ("bcapNotImplemented", 28),
          ("bcapUnavailable", 26),
          ("callRejectCLIR", 11),
          ("callRejected", 9),
          ("combinationUnsupported", 29),
          ("destIncompatible", 33),
          ("destOutOfOrder", 12),
          ("dtlNotMyNode", 48),
          ("infoELementMissing", 38),
          ("infoElementNotImplemented", 40),
          ("invalidCallReference", 31),
          ("invalidEndpointRef", 34),
          ("invalidInfoElement", 41),
          ("invalidMsgLen", 44),
          ("invalidNumberFormat", 13),
          ("invalidTransitNet", 35),
          ("msgNotCompatible", 42),
          ("msgTypeNotImplemented", 39),
          ("networkOutOfOrder", 19),
          ("noChannel", 32),
          ("noRouteToDest", 4),
          ("noRouteToNextNode", 47),
          ("noRouteToTransitNet", 3),
          ("noUserResponse", 8),
          ("none", 1),
          ("normalCallCleared31", 6),
          ("normalUnspecified", 15),
          ("numberChanged", 10),
          ("opticalElementError", 46),
          ("protocolError", 45),
          ("qosUnavailable", 23),
          ("rateUnavailable", 24),
          ("rateUnavailable31", 18),
          ("reqVccUnavailable", 16),
          ("resourcesUnavailable", 22),
          ("respToStatusEnquiry", 14),
          ("serviceUnavailable", 27),
          ("tempFailure", 20),
          ("timerRecovery", 43),
          ("tooManyAddPartyRequests", 36),
          ("unallocNumber", 2),
          ("userBusy", 7),
          ("vccFail31", 17),
          ("vccUnacceptable30", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Equipe_ObjectIdentity = ObjectIdentity
equipe = _Equipe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5022)
)
_EqAtmStatsTable_Object = MibTable
eqAtmStatsTable = _EqAtmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1)
)
if mibBuilder.loadTexts:
    eqAtmStatsTable.setStatus("current")
_EqAtmStatsEntry_Object = MibTableRow
eqAtmStatsEntry = _EqAtmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1)
)
eqAtmStatsEntry.setIndexNames(
    (0, "EQUIPE-ATM-MIB", "eqAtmStatsIfIndex"),
)
if mibBuilder.loadTexts:
    eqAtmStatsEntry.setStatus("current")


class _EqAtmStatsIfIndex_Type(Integer32):
    """Custom type eqAtmStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmStatsIfIndex_Type.__name__ = "Integer32"
_EqAtmStatsIfIndex_Object = MibTableColumn
eqAtmStatsIfIndex = _EqAtmStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 1),
    _EqAtmStatsIfIndex_Type()
)
eqAtmStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsIfIndex.setStatus("current")
_EqAtmStatsInCells_Type = Counter64
_EqAtmStatsInCells_Object = MibTableColumn
eqAtmStatsInCells = _EqAtmStatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 2),
    _EqAtmStatsInCells_Type()
)
eqAtmStatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCells.setStatus("current")
_EqAtmStatsInCellsPerSecond_Type = Counter64
_EqAtmStatsInCellsPerSecond_Object = MibTableColumn
eqAtmStatsInCellsPerSecond = _EqAtmStatsInCellsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 3),
    _EqAtmStatsInCellsPerSecond_Type()
)
eqAtmStatsInCellsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsPerSecond.setStatus("current")
_EqAtmStatsInBitsPerSecond_Type = Counter64
_EqAtmStatsInBitsPerSecond_Object = MibTableColumn
eqAtmStatsInBitsPerSecond = _EqAtmStatsInBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 4),
    _EqAtmStatsInBitsPerSecond_Type()
)
eqAtmStatsInBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInBitsPerSecond.setStatus("current")
_EqAtmStatsInCellsClp0_Type = Counter64
_EqAtmStatsInCellsClp0_Object = MibTableColumn
eqAtmStatsInCellsClp0 = _EqAtmStatsInCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 5),
    _EqAtmStatsInCellsClp0_Type()
)
eqAtmStatsInCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsClp0.setStatus("current")
_EqAtmStatsInCellsClp1_Type = Counter64
_EqAtmStatsInCellsClp1_Object = MibTableColumn
eqAtmStatsInCellsClp1 = _EqAtmStatsInCellsClp1_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 6),
    _EqAtmStatsInCellsClp1_Type()
)
eqAtmStatsInCellsClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsClp1.setStatus("current")
_EqAtmStatsInCellsTagged_Type = Counter64
_EqAtmStatsInCellsTagged_Object = MibTableColumn
eqAtmStatsInCellsTagged = _EqAtmStatsInCellsTagged_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 7),
    _EqAtmStatsInCellsTagged_Type()
)
eqAtmStatsInCellsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsTagged.setStatus("current")
_EqAtmStatsInCellsClp0Discards_Type = Counter64
_EqAtmStatsInCellsClp0Discards_Object = MibTableColumn
eqAtmStatsInCellsClp0Discards = _EqAtmStatsInCellsClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 8),
    _EqAtmStatsInCellsClp0Discards_Type()
)
eqAtmStatsInCellsClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsClp0Discards.setStatus("current")
_EqAtmStatsInCellsClp1Discards_Type = Counter64
_EqAtmStatsInCellsClp1Discards_Object = MibTableColumn
eqAtmStatsInCellsClp1Discards = _EqAtmStatsInCellsClp1Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 9),
    _EqAtmStatsInCellsClp1Discards_Type()
)
eqAtmStatsInCellsClp1Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsClp1Discards.setStatus("current")
_EqAtmStatsInCellsOam_Type = Counter64
_EqAtmStatsInCellsOam_Object = MibTableColumn
eqAtmStatsInCellsOam = _EqAtmStatsInCellsOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 10),
    _EqAtmStatsInCellsOam_Type()
)
eqAtmStatsInCellsOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsOam.setStatus("current")
_EqAtmStatsInCellsClp0Oam_Type = Counter64
_EqAtmStatsInCellsClp0Oam_Object = MibTableColumn
eqAtmStatsInCellsClp0Oam = _EqAtmStatsInCellsClp0Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 11),
    _EqAtmStatsInCellsClp0Oam_Type()
)
eqAtmStatsInCellsClp0Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsClp0Oam.setStatus("current")
_EqAtmStatsInCellsClp1Oam_Type = Counter64
_EqAtmStatsInCellsClp1Oam_Object = MibTableColumn
eqAtmStatsInCellsClp1Oam = _EqAtmStatsInCellsClp1Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 12),
    _EqAtmStatsInCellsClp1Oam_Type()
)
eqAtmStatsInCellsClp1Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsClp1Oam.setStatus("current")
_EqAtmStatsInCellsLoopback_Type = Counter64
_EqAtmStatsInCellsLoopback_Object = MibTableColumn
eqAtmStatsInCellsLoopback = _EqAtmStatsInCellsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 13),
    _EqAtmStatsInCellsLoopback_Type()
)
eqAtmStatsInCellsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsLoopback.setStatus("current")
_EqAtmStatsInCellsLoopbackOam_Type = Counter64
_EqAtmStatsInCellsLoopbackOam_Object = MibTableColumn
eqAtmStatsInCellsLoopbackOam = _EqAtmStatsInCellsLoopbackOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 14),
    _EqAtmStatsInCellsLoopbackOam_Type()
)
eqAtmStatsInCellsLoopbackOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsInCellsLoopbackOam.setStatus("current")
_EqAtmStatsOutCells_Type = Counter64
_EqAtmStatsOutCells_Object = MibTableColumn
eqAtmStatsOutCells = _EqAtmStatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 15),
    _EqAtmStatsOutCells_Type()
)
eqAtmStatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCells.setStatus("current")
_EqAtmStatsOutCellsPerSecond_Type = Counter64
_EqAtmStatsOutCellsPerSecond_Object = MibTableColumn
eqAtmStatsOutCellsPerSecond = _EqAtmStatsOutCellsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 16),
    _EqAtmStatsOutCellsPerSecond_Type()
)
eqAtmStatsOutCellsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsPerSecond.setStatus("current")
_EqAtmStatsOutBitsPerSecond_Type = Counter64
_EqAtmStatsOutBitsPerSecond_Object = MibTableColumn
eqAtmStatsOutBitsPerSecond = _EqAtmStatsOutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 17),
    _EqAtmStatsOutBitsPerSecond_Type()
)
eqAtmStatsOutBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutBitsPerSecond.setStatus("current")
_EqAtmStatsOutCellsClp0_Type = Counter64
_EqAtmStatsOutCellsClp0_Object = MibTableColumn
eqAtmStatsOutCellsClp0 = _EqAtmStatsOutCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 18),
    _EqAtmStatsOutCellsClp0_Type()
)
eqAtmStatsOutCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsClp0.setStatus("current")
_EqAtmStatsOutCellsClp1_Type = Counter64
_EqAtmStatsOutCellsClp1_Object = MibTableColumn
eqAtmStatsOutCellsClp1 = _EqAtmStatsOutCellsClp1_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 19),
    _EqAtmStatsOutCellsClp1_Type()
)
eqAtmStatsOutCellsClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsClp1.setStatus("current")
_EqAtmStatsOutCellsTagged_Type = Counter64
_EqAtmStatsOutCellsTagged_Object = MibTableColumn
eqAtmStatsOutCellsTagged = _EqAtmStatsOutCellsTagged_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 20),
    _EqAtmStatsOutCellsTagged_Type()
)
eqAtmStatsOutCellsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsTagged.setStatus("current")
_EqAtmStatsOutCellsClp0Discards_Type = Counter64
_EqAtmStatsOutCellsClp0Discards_Object = MibTableColumn
eqAtmStatsOutCellsClp0Discards = _EqAtmStatsOutCellsClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 21),
    _EqAtmStatsOutCellsClp0Discards_Type()
)
eqAtmStatsOutCellsClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsClp0Discards.setStatus("current")
_EqAtmStatsOutCellsClp1Discards_Type = Counter64
_EqAtmStatsOutCellsClp1Discards_Object = MibTableColumn
eqAtmStatsOutCellsClp1Discards = _EqAtmStatsOutCellsClp1Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 22),
    _EqAtmStatsOutCellsClp1Discards_Type()
)
eqAtmStatsOutCellsClp1Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsClp1Discards.setStatus("current")
_EqAtmStatsOutCellsOam_Type = Counter64
_EqAtmStatsOutCellsOam_Object = MibTableColumn
eqAtmStatsOutCellsOam = _EqAtmStatsOutCellsOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 23),
    _EqAtmStatsOutCellsOam_Type()
)
eqAtmStatsOutCellsOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsOam.setStatus("current")
_EqAtmStatsOutCellsClp0Oam_Type = Counter64
_EqAtmStatsOutCellsClp0Oam_Object = MibTableColumn
eqAtmStatsOutCellsClp0Oam = _EqAtmStatsOutCellsClp0Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 24),
    _EqAtmStatsOutCellsClp0Oam_Type()
)
eqAtmStatsOutCellsClp0Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsClp0Oam.setStatus("current")
_EqAtmStatsOutCellsClp1Oam_Type = Counter64
_EqAtmStatsOutCellsClp1Oam_Object = MibTableColumn
eqAtmStatsOutCellsClp1Oam = _EqAtmStatsOutCellsClp1Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 25),
    _EqAtmStatsOutCellsClp1Oam_Type()
)
eqAtmStatsOutCellsClp1Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsClp1Oam.setStatus("current")
_EqAtmStatsOutCellsLoopback_Type = Counter64
_EqAtmStatsOutCellsLoopback_Object = MibTableColumn
eqAtmStatsOutCellsLoopback = _EqAtmStatsOutCellsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 26),
    _EqAtmStatsOutCellsLoopback_Type()
)
eqAtmStatsOutCellsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsLoopback.setStatus("current")
_EqAtmStatsOutCellsLoopbackOam_Type = Counter64
_EqAtmStatsOutCellsLoopbackOam_Object = MibTableColumn
eqAtmStatsOutCellsLoopbackOam = _EqAtmStatsOutCellsLoopbackOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 27),
    _EqAtmStatsOutCellsLoopbackOam_Type()
)
eqAtmStatsOutCellsLoopbackOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsOutCellsLoopbackOam.setStatus("current")


class _EqAtmStatsCLR_Type(Integer32):
    """Custom type eqAtmStatsCLR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_EqAtmStatsCLR_Type.__name__ = "Integer32"
_EqAtmStatsCLR_Object = MibTableColumn
eqAtmStatsCLR = _EqAtmStatsCLR_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 1, 1, 28),
    _EqAtmStatsCLR_Type()
)
eqAtmStatsCLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmStatsCLR.setStatus("current")
_EqAtmSvcStatsTable_Object = MibTable
eqAtmSvcStatsTable = _EqAtmSvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2)
)
if mibBuilder.loadTexts:
    eqAtmSvcStatsTable.setStatus("current")
_EqAtmSvcStatsEntry_Object = MibTableRow
eqAtmSvcStatsEntry = _EqAtmSvcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1)
)
eqAtmSvcStatsEntry.setIndexNames(
    (0, "EQUIPE-ATM-MIB", "eqAtmSvcStatsIfIndex"),
)
if mibBuilder.loadTexts:
    eqAtmSvcStatsEntry.setStatus("current")


class _EqAtmSvcStatsIfIndex_Type(Integer32):
    """Custom type eqAtmSvcStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmSvcStatsIfIndex_Type.__name__ = "Integer32"
_EqAtmSvcStatsIfIndex_Object = MibTableColumn
eqAtmSvcStatsIfIndex = _EqAtmSvcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 1),
    _EqAtmSvcStatsIfIndex_Type()
)
eqAtmSvcStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcStatsIfIndex.setStatus("current")
_EqAtmSvcTotal_Type = Counter32
_EqAtmSvcTotal_Object = MibTableColumn
eqAtmSvcTotal = _EqAtmSvcTotal_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 2),
    _EqAtmSvcTotal_Type()
)
eqAtmSvcTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcTotal.setStatus("current")
_EqAtmSvcConnected_Type = Counter32
_EqAtmSvcConnected_Object = MibTableColumn
eqAtmSvcConnected = _EqAtmSvcConnected_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 3),
    _EqAtmSvcConnected_Type()
)
eqAtmSvcConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcConnected.setStatus("current")
_EqAtmSvcFailures_Type = Counter32
_EqAtmSvcFailures_Object = MibTableColumn
eqAtmSvcFailures = _EqAtmSvcFailures_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 4),
    _EqAtmSvcFailures_Type()
)
eqAtmSvcFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcFailures.setStatus("current")
_EqAtmSvcInLastCauseCode_Type = AtmCauseCode
_EqAtmSvcInLastCauseCode_Object = MibTableColumn
eqAtmSvcInLastCauseCode = _EqAtmSvcInLastCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 5),
    _EqAtmSvcInLastCauseCode_Type()
)
eqAtmSvcInLastCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInLastCauseCode.setStatus("current")
_EqAtmSvcInSetupPdus_Type = Counter32
_EqAtmSvcInSetupPdus_Object = MibTableColumn
eqAtmSvcInSetupPdus = _EqAtmSvcInSetupPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 6),
    _EqAtmSvcInSetupPdus_Type()
)
eqAtmSvcInSetupPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInSetupPdus.setStatus("current")
_EqAtmSvcInCallProceeding_Type = Counter32
_EqAtmSvcInCallProceeding_Object = MibTableColumn
eqAtmSvcInCallProceeding = _EqAtmSvcInCallProceeding_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 7),
    _EqAtmSvcInCallProceeding_Type()
)
eqAtmSvcInCallProceeding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInCallProceeding.setStatus("current")
_EqAtmSvcInPdusConnect_Type = Counter32
_EqAtmSvcInPdusConnect_Object = MibTableColumn
eqAtmSvcInPdusConnect = _EqAtmSvcInPdusConnect_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 8),
    _EqAtmSvcInPdusConnect_Type()
)
eqAtmSvcInPdusConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusConnect.setStatus("current")
_EqAtmSvcInPdusConnectAck_Type = Counter32
_EqAtmSvcInPdusConnectAck_Object = MibTableColumn
eqAtmSvcInPdusConnectAck = _EqAtmSvcInPdusConnectAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 9),
    _EqAtmSvcInPdusConnectAck_Type()
)
eqAtmSvcInPdusConnectAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusConnectAck.setStatus("current")
_EqAtmSvcInPdusReleaseComplete_Type = Counter32
_EqAtmSvcInPdusReleaseComplete_Object = MibTableColumn
eqAtmSvcInPdusReleaseComplete = _EqAtmSvcInPdusReleaseComplete_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 10),
    _EqAtmSvcInPdusReleaseComplete_Type()
)
eqAtmSvcInPdusReleaseComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusReleaseComplete.setStatus("current")
_EqAtmSvcInPdusAddParty_Type = Counter32
_EqAtmSvcInPdusAddParty_Object = MibTableColumn
eqAtmSvcInPdusAddParty = _EqAtmSvcInPdusAddParty_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 11),
    _EqAtmSvcInPdusAddParty_Type()
)
eqAtmSvcInPdusAddParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusAddParty.setStatus("current")
_EqAtmSvcInPdusAddPartyAck_Type = Counter32
_EqAtmSvcInPdusAddPartyAck_Object = MibTableColumn
eqAtmSvcInPdusAddPartyAck = _EqAtmSvcInPdusAddPartyAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 12),
    _EqAtmSvcInPdusAddPartyAck_Type()
)
eqAtmSvcInPdusAddPartyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusAddPartyAck.setStatus("current")
_EqAtmSvcInPdusAddPartyReject_Type = Counter32
_EqAtmSvcInPdusAddPartyReject_Object = MibTableColumn
eqAtmSvcInPdusAddPartyReject = _EqAtmSvcInPdusAddPartyReject_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 13),
    _EqAtmSvcInPdusAddPartyReject_Type()
)
eqAtmSvcInPdusAddPartyReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusAddPartyReject.setStatus("current")
_EqAtmSvcInPdusDropParty_Type = Counter32
_EqAtmSvcInPdusDropParty_Object = MibTableColumn
eqAtmSvcInPdusDropParty = _EqAtmSvcInPdusDropParty_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 14),
    _EqAtmSvcInPdusDropParty_Type()
)
eqAtmSvcInPdusDropParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusDropParty.setStatus("current")
_EqAtmSvcInPdusDropPartyAck_Type = Counter32
_EqAtmSvcInPdusDropPartyAck_Object = MibTableColumn
eqAtmSvcInPdusDropPartyAck = _EqAtmSvcInPdusDropPartyAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 15),
    _EqAtmSvcInPdusDropPartyAck_Type()
)
eqAtmSvcInPdusDropPartyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusDropPartyAck.setStatus("current")
_EqAtmSvcInPdusStatusEnquiry_Type = Counter32
_EqAtmSvcInPdusStatusEnquiry_Object = MibTableColumn
eqAtmSvcInPdusStatusEnquiry = _EqAtmSvcInPdusStatusEnquiry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 16),
    _EqAtmSvcInPdusStatusEnquiry_Type()
)
eqAtmSvcInPdusStatusEnquiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusStatusEnquiry.setStatus("current")
_EqAtmSvcInPdusStatus_Type = Counter32
_EqAtmSvcInPdusStatus_Object = MibTableColumn
eqAtmSvcInPdusStatus = _EqAtmSvcInPdusStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 17),
    _EqAtmSvcInPdusStatus_Type()
)
eqAtmSvcInPdusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusStatus.setStatus("current")
_EqAtmSvcInPdusRestart_Type = Counter32
_EqAtmSvcInPdusRestart_Object = MibTableColumn
eqAtmSvcInPdusRestart = _EqAtmSvcInPdusRestart_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 18),
    _EqAtmSvcInPdusRestart_Type()
)
eqAtmSvcInPdusRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusRestart.setStatus("current")
_EqAtmSvcInPdusRestartAck_Type = Counter32
_EqAtmSvcInPdusRestartAck_Object = MibTableColumn
eqAtmSvcInPdusRestartAck = _EqAtmSvcInPdusRestartAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 19),
    _EqAtmSvcInPdusRestartAck_Type()
)
eqAtmSvcInPdusRestartAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusRestartAck.setStatus("current")
_EqAtmSvcInPdusNotify_Type = Counter32
_EqAtmSvcInPdusNotify_Object = MibTableColumn
eqAtmSvcInPdusNotify = _EqAtmSvcInPdusNotify_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 20),
    _EqAtmSvcInPdusNotify_Type()
)
eqAtmSvcInPdusNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusNotify.setStatus("current")
_EqAtmSvcInPdusProgress_Type = Counter32
_EqAtmSvcInPdusProgress_Object = MibTableColumn
eqAtmSvcInPdusProgress = _EqAtmSvcInPdusProgress_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 21),
    _EqAtmSvcInPdusProgress_Type()
)
eqAtmSvcInPdusProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusProgress.setStatus("current")
_EqAtmSvcInPdusAlerting_Type = Counter32
_EqAtmSvcInPdusAlerting_Object = MibTableColumn
eqAtmSvcInPdusAlerting = _EqAtmSvcInPdusAlerting_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 22),
    _EqAtmSvcInPdusAlerting_Type()
)
eqAtmSvcInPdusAlerting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusAlerting.setStatus("current")
_EqAtmSvcInPdusPartyAlerting_Type = Counter32
_EqAtmSvcInPdusPartyAlerting_Object = MibTableColumn
eqAtmSvcInPdusPartyAlerting = _EqAtmSvcInPdusPartyAlerting_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 23),
    _EqAtmSvcInPdusPartyAlerting_Type()
)
eqAtmSvcInPdusPartyAlerting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcInPdusPartyAlerting.setStatus("current")
_EqAtmSvcOutLastCauseCode_Type = AtmCauseCode
_EqAtmSvcOutLastCauseCode_Object = MibTableColumn
eqAtmSvcOutLastCauseCode = _EqAtmSvcOutLastCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 24),
    _EqAtmSvcOutLastCauseCode_Type()
)
eqAtmSvcOutLastCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutLastCauseCode.setStatus("current")
_EqAtmSvcOutSetupPdus_Type = Counter32
_EqAtmSvcOutSetupPdus_Object = MibTableColumn
eqAtmSvcOutSetupPdus = _EqAtmSvcOutSetupPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 25),
    _EqAtmSvcOutSetupPdus_Type()
)
eqAtmSvcOutSetupPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutSetupPdus.setStatus("current")
_EqAtmSvcOutCallProceeding_Type = Counter32
_EqAtmSvcOutCallProceeding_Object = MibTableColumn
eqAtmSvcOutCallProceeding = _EqAtmSvcOutCallProceeding_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 26),
    _EqAtmSvcOutCallProceeding_Type()
)
eqAtmSvcOutCallProceeding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutCallProceeding.setStatus("current")
_EqAtmSvcOutPdusConnect_Type = Counter32
_EqAtmSvcOutPdusConnect_Object = MibTableColumn
eqAtmSvcOutPdusConnect = _EqAtmSvcOutPdusConnect_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 27),
    _EqAtmSvcOutPdusConnect_Type()
)
eqAtmSvcOutPdusConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusConnect.setStatus("current")
_EqAtmSvcOutPdusConnectAck_Type = Counter32
_EqAtmSvcOutPdusConnectAck_Object = MibTableColumn
eqAtmSvcOutPdusConnectAck = _EqAtmSvcOutPdusConnectAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 28),
    _EqAtmSvcOutPdusConnectAck_Type()
)
eqAtmSvcOutPdusConnectAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusConnectAck.setStatus("current")
_EqAtmSvcOutPdusReleaseComplete_Type = Counter32
_EqAtmSvcOutPdusReleaseComplete_Object = MibTableColumn
eqAtmSvcOutPdusReleaseComplete = _EqAtmSvcOutPdusReleaseComplete_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 29),
    _EqAtmSvcOutPdusReleaseComplete_Type()
)
eqAtmSvcOutPdusReleaseComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusReleaseComplete.setStatus("current")
_EqAtmSvcOutPdusAddParty_Type = Counter32
_EqAtmSvcOutPdusAddParty_Object = MibTableColumn
eqAtmSvcOutPdusAddParty = _EqAtmSvcOutPdusAddParty_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 30),
    _EqAtmSvcOutPdusAddParty_Type()
)
eqAtmSvcOutPdusAddParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusAddParty.setStatus("current")
_EqAtmSvcOutPdusAddPartyAck_Type = Counter32
_EqAtmSvcOutPdusAddPartyAck_Object = MibTableColumn
eqAtmSvcOutPdusAddPartyAck = _EqAtmSvcOutPdusAddPartyAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 31),
    _EqAtmSvcOutPdusAddPartyAck_Type()
)
eqAtmSvcOutPdusAddPartyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusAddPartyAck.setStatus("current")
_EqAtmSvcOutPdusAddPartyReject_Type = Counter32
_EqAtmSvcOutPdusAddPartyReject_Object = MibTableColumn
eqAtmSvcOutPdusAddPartyReject = _EqAtmSvcOutPdusAddPartyReject_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 32),
    _EqAtmSvcOutPdusAddPartyReject_Type()
)
eqAtmSvcOutPdusAddPartyReject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusAddPartyReject.setStatus("current")
_EqAtmSvcOutPdusDropParty_Type = Counter32
_EqAtmSvcOutPdusDropParty_Object = MibTableColumn
eqAtmSvcOutPdusDropParty = _EqAtmSvcOutPdusDropParty_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 33),
    _EqAtmSvcOutPdusDropParty_Type()
)
eqAtmSvcOutPdusDropParty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusDropParty.setStatus("current")
_EqAtmSvcOutPdusDropPartyAck_Type = Counter32
_EqAtmSvcOutPdusDropPartyAck_Object = MibTableColumn
eqAtmSvcOutPdusDropPartyAck = _EqAtmSvcOutPdusDropPartyAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 34),
    _EqAtmSvcOutPdusDropPartyAck_Type()
)
eqAtmSvcOutPdusDropPartyAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusDropPartyAck.setStatus("current")
_EqAtmSvcOutPdusStatusEnquiry_Type = Counter32
_EqAtmSvcOutPdusStatusEnquiry_Object = MibTableColumn
eqAtmSvcOutPdusStatusEnquiry = _EqAtmSvcOutPdusStatusEnquiry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 35),
    _EqAtmSvcOutPdusStatusEnquiry_Type()
)
eqAtmSvcOutPdusStatusEnquiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusStatusEnquiry.setStatus("current")
_EqAtmSvcOutPdusStatus_Type = Counter32
_EqAtmSvcOutPdusStatus_Object = MibTableColumn
eqAtmSvcOutPdusStatus = _EqAtmSvcOutPdusStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 36),
    _EqAtmSvcOutPdusStatus_Type()
)
eqAtmSvcOutPdusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusStatus.setStatus("current")
_EqAtmSvcOutPdusRestart_Type = Counter32
_EqAtmSvcOutPdusRestart_Object = MibTableColumn
eqAtmSvcOutPdusRestart = _EqAtmSvcOutPdusRestart_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 37),
    _EqAtmSvcOutPdusRestart_Type()
)
eqAtmSvcOutPdusRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusRestart.setStatus("current")
_EqAtmSvcOutPdusRestartAck_Type = Counter32
_EqAtmSvcOutPdusRestartAck_Object = MibTableColumn
eqAtmSvcOutPdusRestartAck = _EqAtmSvcOutPdusRestartAck_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 38),
    _EqAtmSvcOutPdusRestartAck_Type()
)
eqAtmSvcOutPdusRestartAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusRestartAck.setStatus("current")
_EqAtmSvcOutPdusNotify_Type = Counter32
_EqAtmSvcOutPdusNotify_Object = MibTableColumn
eqAtmSvcOutPdusNotify = _EqAtmSvcOutPdusNotify_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 39),
    _EqAtmSvcOutPdusNotify_Type()
)
eqAtmSvcOutPdusNotify.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusNotify.setStatus("current")
_EqAtmSvcOutPdusProgress_Type = Counter32
_EqAtmSvcOutPdusProgress_Object = MibTableColumn
eqAtmSvcOutPdusProgress = _EqAtmSvcOutPdusProgress_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 40),
    _EqAtmSvcOutPdusProgress_Type()
)
eqAtmSvcOutPdusProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusProgress.setStatus("current")
_EqAtmSvcOutPdusAlerting_Type = Counter32
_EqAtmSvcOutPdusAlerting_Object = MibTableColumn
eqAtmSvcOutPdusAlerting = _EqAtmSvcOutPdusAlerting_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 41),
    _EqAtmSvcOutPdusAlerting_Type()
)
eqAtmSvcOutPdusAlerting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusAlerting.setStatus("current")
_EqAtmSvcOutPdusPartyAlerting_Type = Counter32
_EqAtmSvcOutPdusPartyAlerting_Object = MibTableColumn
eqAtmSvcOutPdusPartyAlerting = _EqAtmSvcOutPdusPartyAlerting_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 2, 1, 42),
    _EqAtmSvcOutPdusPartyAlerting_Type()
)
eqAtmSvcOutPdusPartyAlerting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSvcOutPdusPartyAlerting.setStatus("current")
_EqAtmSaalStatsTable_Object = MibTable
eqAtmSaalStatsTable = _EqAtmSaalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3)
)
if mibBuilder.loadTexts:
    eqAtmSaalStatsTable.setStatus("current")
_EqAtmSaalStatsEntry_Object = MibTableRow
eqAtmSaalStatsEntry = _EqAtmSaalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1)
)
eqAtmSaalStatsEntry.setIndexNames(
    (0, "EQUIPE-ATM-MIB", "eqAtmSaalStatsIfIndex"),
)
if mibBuilder.loadTexts:
    eqAtmSaalStatsEntry.setStatus("current")


class _EqAtmSaalStatsIfIndex_Type(Integer32):
    """Custom type eqAtmSaalStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmSaalStatsIfIndex_Type.__name__ = "Integer32"
_EqAtmSaalStatsIfIndex_Object = MibTableColumn
eqAtmSaalStatsIfIndex = _EqAtmSaalStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 1),
    _EqAtmSaalStatsIfIndex_Type()
)
eqAtmSaalStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalStatsIfIndex.setStatus("current")
_EqAtmSaalInErrors_Type = Counter32
_EqAtmSaalInErrors_Object = MibTableColumn
eqAtmSaalInErrors = _EqAtmSaalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 2),
    _EqAtmSaalInErrors_Type()
)
eqAtmSaalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInErrors.setStatus("current")
_EqAtmSaalInDiscards_Type = Counter32
_EqAtmSaalInDiscards_Object = MibTableColumn
eqAtmSaalInDiscards = _EqAtmSaalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 3),
    _EqAtmSaalInDiscards_Type()
)
eqAtmSaalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInDiscards.setStatus("current")
_EqAtmSaalInBeginPdus_Type = Counter32
_EqAtmSaalInBeginPdus_Object = MibTableColumn
eqAtmSaalInBeginPdus = _EqAtmSaalInBeginPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 4),
    _EqAtmSaalInBeginPdus_Type()
)
eqAtmSaalInBeginPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInBeginPdus.setStatus("current")
_EqAtmSaalInBeginAckPdus_Type = Counter32
_EqAtmSaalInBeginAckPdus_Object = MibTableColumn
eqAtmSaalInBeginAckPdus = _EqAtmSaalInBeginAckPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 5),
    _EqAtmSaalInBeginAckPdus_Type()
)
eqAtmSaalInBeginAckPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInBeginAckPdus.setStatus("current")
_EqAtmSaalInBeginRejectPdus_Type = Counter32
_EqAtmSaalInBeginRejectPdus_Object = MibTableColumn
eqAtmSaalInBeginRejectPdus = _EqAtmSaalInBeginRejectPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 6),
    _EqAtmSaalInBeginRejectPdus_Type()
)
eqAtmSaalInBeginRejectPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInBeginRejectPdus.setStatus("current")
_EqAtmSaalInEndPdus_Type = Counter32
_EqAtmSaalInEndPdus_Object = MibTableColumn
eqAtmSaalInEndPdus = _EqAtmSaalInEndPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 7),
    _EqAtmSaalInEndPdus_Type()
)
eqAtmSaalInEndPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInEndPdus.setStatus("current")
_EqAtmSaalInEndAckPdus_Type = Counter32
_EqAtmSaalInEndAckPdus_Object = MibTableColumn
eqAtmSaalInEndAckPdus = _EqAtmSaalInEndAckPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 8),
    _EqAtmSaalInEndAckPdus_Type()
)
eqAtmSaalInEndAckPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInEndAckPdus.setStatus("current")
_EqAtmSaalInResyncPdus_Type = Counter32
_EqAtmSaalInResyncPdus_Object = MibTableColumn
eqAtmSaalInResyncPdus = _EqAtmSaalInResyncPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 9),
    _EqAtmSaalInResyncPdus_Type()
)
eqAtmSaalInResyncPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInResyncPdus.setStatus("current")
_EqAtmSaalInResyncAckPdus_Type = Counter32
_EqAtmSaalInResyncAckPdus_Object = MibTableColumn
eqAtmSaalInResyncAckPdus = _EqAtmSaalInResyncAckPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 10),
    _EqAtmSaalInResyncAckPdus_Type()
)
eqAtmSaalInResyncAckPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInResyncAckPdus.setStatus("current")
_EqAtmSaalInErrRecoveryPdus_Type = Counter32
_EqAtmSaalInErrRecoveryPdus_Object = MibTableColumn
eqAtmSaalInErrRecoveryPdus = _EqAtmSaalInErrRecoveryPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 11),
    _EqAtmSaalInErrRecoveryPdus_Type()
)
eqAtmSaalInErrRecoveryPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInErrRecoveryPdus.setStatus("current")
_EqAtmSaalInSeqDataPdus_Type = Counter32
_EqAtmSaalInSeqDataPdus_Object = MibTableColumn
eqAtmSaalInSeqDataPdus = _EqAtmSaalInSeqDataPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 12),
    _EqAtmSaalInSeqDataPdus_Type()
)
eqAtmSaalInSeqDataPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInSeqDataPdus.setStatus("current")
_EqAtmSaalInPollPdus_Type = Counter32
_EqAtmSaalInPollPdus_Object = MibTableColumn
eqAtmSaalInPollPdus = _EqAtmSaalInPollPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 13),
    _EqAtmSaalInPollPdus_Type()
)
eqAtmSaalInPollPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInPollPdus.setStatus("current")
_EqAtmSaalInStatusPdus_Type = Counter32
_EqAtmSaalInStatusPdus_Object = MibTableColumn
eqAtmSaalInStatusPdus = _EqAtmSaalInStatusPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 14),
    _EqAtmSaalInStatusPdus_Type()
)
eqAtmSaalInStatusPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInStatusPdus.setStatus("current")
_EqAtmSaalInUnsolicitedStatusPdus_Type = Counter32
_EqAtmSaalInUnsolicitedStatusPdus_Object = MibTableColumn
eqAtmSaalInUnsolicitedStatusPdus = _EqAtmSaalInUnsolicitedStatusPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 15),
    _EqAtmSaalInUnsolicitedStatusPdus_Type()
)
eqAtmSaalInUnsolicitedStatusPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInUnsolicitedStatusPdus.setStatus("current")
_EqAtmSaalInUnsolicitedUserPdus_Type = Counter32
_EqAtmSaalInUnsolicitedUserPdus_Object = MibTableColumn
eqAtmSaalInUnsolicitedUserPdus = _EqAtmSaalInUnsolicitedUserPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 16),
    _EqAtmSaalInUnsolicitedUserPdus_Type()
)
eqAtmSaalInUnsolicitedUserPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInUnsolicitedUserPdus.setStatus("current")
_EqAtmSaalInUnnumberedUserPdus_Type = Counter32
_EqAtmSaalInUnnumberedUserPdus_Object = MibTableColumn
eqAtmSaalInUnnumberedUserPdus = _EqAtmSaalInUnnumberedUserPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 17),
    _EqAtmSaalInUnnumberedUserPdus_Type()
)
eqAtmSaalInUnnumberedUserPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInUnnumberedUserPdus.setStatus("current")
_EqAtmSaalInUnnumberedMgmtPdus_Type = Counter32
_EqAtmSaalInUnnumberedMgmtPdus_Object = MibTableColumn
eqAtmSaalInUnnumberedMgmtPdus = _EqAtmSaalInUnnumberedMgmtPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 18),
    _EqAtmSaalInUnnumberedMgmtPdus_Type()
)
eqAtmSaalInUnnumberedMgmtPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInUnnumberedMgmtPdus.setStatus("current")
_EqAtmSaalInSignalOctets_Type = Counter32
_EqAtmSaalInSignalOctets_Object = MibTableColumn
eqAtmSaalInSignalOctets = _EqAtmSaalInSignalOctets_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 19),
    _EqAtmSaalInSignalOctets_Type()
)
eqAtmSaalInSignalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalInSignalOctets.setStatus("current")
_EqAtmSaalOutDiscards_Type = Counter32
_EqAtmSaalOutDiscards_Object = MibTableColumn
eqAtmSaalOutDiscards = _EqAtmSaalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 20),
    _EqAtmSaalOutDiscards_Type()
)
eqAtmSaalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutDiscards.setStatus("current")
_EqAtmSaalOutBeginPdus_Type = Counter32
_EqAtmSaalOutBeginPdus_Object = MibTableColumn
eqAtmSaalOutBeginPdus = _EqAtmSaalOutBeginPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 21),
    _EqAtmSaalOutBeginPdus_Type()
)
eqAtmSaalOutBeginPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutBeginPdus.setStatus("current")
_EqAtmSaalOutBeginAckPdus_Type = Counter32
_EqAtmSaalOutBeginAckPdus_Object = MibTableColumn
eqAtmSaalOutBeginAckPdus = _EqAtmSaalOutBeginAckPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 22),
    _EqAtmSaalOutBeginAckPdus_Type()
)
eqAtmSaalOutBeginAckPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutBeginAckPdus.setStatus("current")
_EqAtmSaalOutBeginRejectPdus_Type = Counter32
_EqAtmSaalOutBeginRejectPdus_Object = MibTableColumn
eqAtmSaalOutBeginRejectPdus = _EqAtmSaalOutBeginRejectPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 23),
    _EqAtmSaalOutBeginRejectPdus_Type()
)
eqAtmSaalOutBeginRejectPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutBeginRejectPdus.setStatus("current")
_EqAtmSaalOutEndPdus_Type = Counter32
_EqAtmSaalOutEndPdus_Object = MibTableColumn
eqAtmSaalOutEndPdus = _EqAtmSaalOutEndPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 24),
    _EqAtmSaalOutEndPdus_Type()
)
eqAtmSaalOutEndPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutEndPdus.setStatus("current")
_EqAtmSaalOutEndAckPdus_Type = Counter32
_EqAtmSaalOutEndAckPdus_Object = MibTableColumn
eqAtmSaalOutEndAckPdus = _EqAtmSaalOutEndAckPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 25),
    _EqAtmSaalOutEndAckPdus_Type()
)
eqAtmSaalOutEndAckPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutEndAckPdus.setStatus("current")
_EqAtmSaalOutResyncPdus_Type = Counter32
_EqAtmSaalOutResyncPdus_Object = MibTableColumn
eqAtmSaalOutResyncPdus = _EqAtmSaalOutResyncPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 26),
    _EqAtmSaalOutResyncPdus_Type()
)
eqAtmSaalOutResyncPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutResyncPdus.setStatus("current")
_EqAtmSaalOutResyncAckPdus_Type = Counter32
_EqAtmSaalOutResyncAckPdus_Object = MibTableColumn
eqAtmSaalOutResyncAckPdus = _EqAtmSaalOutResyncAckPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 27),
    _EqAtmSaalOutResyncAckPdus_Type()
)
eqAtmSaalOutResyncAckPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutResyncAckPdus.setStatus("current")
_EqAtmSaalOutErrRecoveryPdus_Type = Counter32
_EqAtmSaalOutErrRecoveryPdus_Object = MibTableColumn
eqAtmSaalOutErrRecoveryPdus = _EqAtmSaalOutErrRecoveryPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 28),
    _EqAtmSaalOutErrRecoveryPdus_Type()
)
eqAtmSaalOutErrRecoveryPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutErrRecoveryPdus.setStatus("current")
_EqAtmSaalOutSeqDataPdus_Type = Counter32
_EqAtmSaalOutSeqDataPdus_Object = MibTableColumn
eqAtmSaalOutSeqDataPdus = _EqAtmSaalOutSeqDataPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 29),
    _EqAtmSaalOutSeqDataPdus_Type()
)
eqAtmSaalOutSeqDataPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutSeqDataPdus.setStatus("current")
_EqAtmSaalOutPollPdus_Type = Counter32
_EqAtmSaalOutPollPdus_Object = MibTableColumn
eqAtmSaalOutPollPdus = _EqAtmSaalOutPollPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 30),
    _EqAtmSaalOutPollPdus_Type()
)
eqAtmSaalOutPollPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutPollPdus.setStatus("current")
_EqAtmSaalOutStatusPdus_Type = Counter32
_EqAtmSaalOutStatusPdus_Object = MibTableColumn
eqAtmSaalOutStatusPdus = _EqAtmSaalOutStatusPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 31),
    _EqAtmSaalOutStatusPdus_Type()
)
eqAtmSaalOutStatusPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutStatusPdus.setStatus("current")
_EqAtmSaalOutUnsolicitedStatusPdus_Type = Counter32
_EqAtmSaalOutUnsolicitedStatusPdus_Object = MibTableColumn
eqAtmSaalOutUnsolicitedStatusPdus = _EqAtmSaalOutUnsolicitedStatusPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 32),
    _EqAtmSaalOutUnsolicitedStatusPdus_Type()
)
eqAtmSaalOutUnsolicitedStatusPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutUnsolicitedStatusPdus.setStatus("current")
_EqAtmSaalOutUnsolicitedUserPdus_Type = Counter32
_EqAtmSaalOutUnsolicitedUserPdus_Object = MibTableColumn
eqAtmSaalOutUnsolicitedUserPdus = _EqAtmSaalOutUnsolicitedUserPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 33),
    _EqAtmSaalOutUnsolicitedUserPdus_Type()
)
eqAtmSaalOutUnsolicitedUserPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutUnsolicitedUserPdus.setStatus("current")
_EqAtmSaalOutUnnumberedUserPdus_Type = Counter32
_EqAtmSaalOutUnnumberedUserPdus_Object = MibTableColumn
eqAtmSaalOutUnnumberedUserPdus = _EqAtmSaalOutUnnumberedUserPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 34),
    _EqAtmSaalOutUnnumberedUserPdus_Type()
)
eqAtmSaalOutUnnumberedUserPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutUnnumberedUserPdus.setStatus("current")
_EqAtmSaalOutUnnumberedMgmtPdus_Type = Counter32
_EqAtmSaalOutUnnumberedMgmtPdus_Object = MibTableColumn
eqAtmSaalOutUnnumberedMgmtPdus = _EqAtmSaalOutUnnumberedMgmtPdus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 35),
    _EqAtmSaalOutUnnumberedMgmtPdus_Type()
)
eqAtmSaalOutUnnumberedMgmtPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutUnnumberedMgmtPdus.setStatus("current")
_EqAtmSaalOutSignalOctets_Type = Counter32
_EqAtmSaalOutSignalOctets_Object = MibTableColumn
eqAtmSaalOutSignalOctets = _EqAtmSaalOutSignalOctets_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 36),
    _EqAtmSaalOutSignalOctets_Type()
)
eqAtmSaalOutSignalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutSignalOctets.setStatus("current")


class _EqAtmSaalOutWindowSize_Type(Integer32):
    """Custom type eqAtmSaalOutWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EqAtmSaalOutWindowSize_Type.__name__ = "Integer32"
_EqAtmSaalOutWindowSize_Object = MibTableColumn
eqAtmSaalOutWindowSize = _EqAtmSaalOutWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 3, 1, 37),
    _EqAtmSaalOutWindowSize_Type()
)
eqAtmSaalOutWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmSaalOutWindowSize.setStatus("current")
_EqAtmVcStatsTable_Object = MibTable
eqAtmVcStatsTable = _EqAtmVcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4)
)
if mibBuilder.loadTexts:
    eqAtmVcStatsTable.setStatus("current")
_EqAtmVcStatsEntry_Object = MibTableRow
eqAtmVcStatsEntry = _EqAtmVcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1)
)
eqAtmVcStatsEntry.setIndexNames(
    (0, "EQUIPE-ATM-MIB", "eqAtmVcStatsIfIndex"),
    (0, "EQUIPE-ATM-MIB", "eqAtmVcStatsVpi"),
    (0, "EQUIPE-ATM-MIB", "eqAtmVcStatsVci"),
)
if mibBuilder.loadTexts:
    eqAtmVcStatsEntry.setStatus("current")


class _EqAtmVcStatsIfIndex_Type(Integer32):
    """Custom type eqAtmVcStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmVcStatsIfIndex_Type.__name__ = "Integer32"
_EqAtmVcStatsIfIndex_Object = MibTableColumn
eqAtmVcStatsIfIndex = _EqAtmVcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 1),
    _EqAtmVcStatsIfIndex_Type()
)
eqAtmVcStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsIfIndex.setStatus("current")


class _EqAtmVcStatsVpi_Type(Integer32):
    """Custom type eqAtmVcStatsVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EqAtmVcStatsVpi_Type.__name__ = "Integer32"
_EqAtmVcStatsVpi_Object = MibTableColumn
eqAtmVcStatsVpi = _EqAtmVcStatsVpi_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 2),
    _EqAtmVcStatsVpi_Type()
)
eqAtmVcStatsVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsVpi.setStatus("current")


class _EqAtmVcStatsVci_Type(Integer32):
    """Custom type eqAtmVcStatsVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EqAtmVcStatsVci_Type.__name__ = "Integer32"
_EqAtmVcStatsVci_Object = MibTableColumn
eqAtmVcStatsVci = _EqAtmVcStatsVci_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 3),
    _EqAtmVcStatsVci_Type()
)
eqAtmVcStatsVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsVci.setStatus("current")
_EqAtmVcStatsInCells_Type = Counter64
_EqAtmVcStatsInCells_Object = MibTableColumn
eqAtmVcStatsInCells = _EqAtmVcStatsInCells_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 4),
    _EqAtmVcStatsInCells_Type()
)
eqAtmVcStatsInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCells.setStatus("current")
_EqAtmVcStatsInCellsPerSecond_Type = Counter64
_EqAtmVcStatsInCellsPerSecond_Object = MibTableColumn
eqAtmVcStatsInCellsPerSecond = _EqAtmVcStatsInCellsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 5),
    _EqAtmVcStatsInCellsPerSecond_Type()
)
eqAtmVcStatsInCellsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsPerSecond.setStatus("current")
_EqAtmVcStatsInBitsPerSecond_Type = Counter64
_EqAtmVcStatsInBitsPerSecond_Object = MibTableColumn
eqAtmVcStatsInBitsPerSecond = _EqAtmVcStatsInBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 6),
    _EqAtmVcStatsInBitsPerSecond_Type()
)
eqAtmVcStatsInBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInBitsPerSecond.setStatus("current")
_EqAtmVcStatsInCellsClp0_Type = Counter64
_EqAtmVcStatsInCellsClp0_Object = MibTableColumn
eqAtmVcStatsInCellsClp0 = _EqAtmVcStatsInCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 7),
    _EqAtmVcStatsInCellsClp0_Type()
)
eqAtmVcStatsInCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsClp0.setStatus("current")
_EqAtmVcStatsInCellsClp1_Type = Counter64
_EqAtmVcStatsInCellsClp1_Object = MibTableColumn
eqAtmVcStatsInCellsClp1 = _EqAtmVcStatsInCellsClp1_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 8),
    _EqAtmVcStatsInCellsClp1_Type()
)
eqAtmVcStatsInCellsClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsClp1.setStatus("current")
_EqAtmVcStatsInCellsTagged_Type = Counter64
_EqAtmVcStatsInCellsTagged_Object = MibTableColumn
eqAtmVcStatsInCellsTagged = _EqAtmVcStatsInCellsTagged_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 9),
    _EqAtmVcStatsInCellsTagged_Type()
)
eqAtmVcStatsInCellsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsTagged.setStatus("current")
_EqAtmVcStatsInCellsClp0Discards_Type = Counter64
_EqAtmVcStatsInCellsClp0Discards_Object = MibTableColumn
eqAtmVcStatsInCellsClp0Discards = _EqAtmVcStatsInCellsClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 10),
    _EqAtmVcStatsInCellsClp0Discards_Type()
)
eqAtmVcStatsInCellsClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsClp0Discards.setStatus("current")
_EqAtmVcStatsInCellsClp1Discards_Type = Counter64
_EqAtmVcStatsInCellsClp1Discards_Object = MibTableColumn
eqAtmVcStatsInCellsClp1Discards = _EqAtmVcStatsInCellsClp1Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 11),
    _EqAtmVcStatsInCellsClp1Discards_Type()
)
eqAtmVcStatsInCellsClp1Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsClp1Discards.setStatus("current")
_EqAtmVcStatsInCellsOam_Type = Counter64
_EqAtmVcStatsInCellsOam_Object = MibTableColumn
eqAtmVcStatsInCellsOam = _EqAtmVcStatsInCellsOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 12),
    _EqAtmVcStatsInCellsOam_Type()
)
eqAtmVcStatsInCellsOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsOam.setStatus("current")
_EqAtmVcStatsInCellsClp0Oam_Type = Counter64
_EqAtmVcStatsInCellsClp0Oam_Object = MibTableColumn
eqAtmVcStatsInCellsClp0Oam = _EqAtmVcStatsInCellsClp0Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 13),
    _EqAtmVcStatsInCellsClp0Oam_Type()
)
eqAtmVcStatsInCellsClp0Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsClp0Oam.setStatus("current")
_EqAtmVcStatsInCellsClp1Oam_Type = Counter64
_EqAtmVcStatsInCellsClp1Oam_Object = MibTableColumn
eqAtmVcStatsInCellsClp1Oam = _EqAtmVcStatsInCellsClp1Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 14),
    _EqAtmVcStatsInCellsClp1Oam_Type()
)
eqAtmVcStatsInCellsClp1Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsClp1Oam.setStatus("current")
_EqAtmVcStatsInCellsLoopback_Type = Counter64
_EqAtmVcStatsInCellsLoopback_Object = MibTableColumn
eqAtmVcStatsInCellsLoopback = _EqAtmVcStatsInCellsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 15),
    _EqAtmVcStatsInCellsLoopback_Type()
)
eqAtmVcStatsInCellsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsLoopback.setStatus("current")
_EqAtmVcStatsInCellsLoopbackOam_Type = Counter64
_EqAtmVcStatsInCellsLoopbackOam_Object = MibTableColumn
eqAtmVcStatsInCellsLoopbackOam = _EqAtmVcStatsInCellsLoopbackOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 16),
    _EqAtmVcStatsInCellsLoopbackOam_Type()
)
eqAtmVcStatsInCellsLoopbackOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsInCellsLoopbackOam.setStatus("current")
_EqAtmVcStatsOutCells_Type = Counter64
_EqAtmVcStatsOutCells_Object = MibTableColumn
eqAtmVcStatsOutCells = _EqAtmVcStatsOutCells_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 17),
    _EqAtmVcStatsOutCells_Type()
)
eqAtmVcStatsOutCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCells.setStatus("current")
_EqAtmVcStatsOutCellsPerSecond_Type = Counter64
_EqAtmVcStatsOutCellsPerSecond_Object = MibTableColumn
eqAtmVcStatsOutCellsPerSecond = _EqAtmVcStatsOutCellsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 18),
    _EqAtmVcStatsOutCellsPerSecond_Type()
)
eqAtmVcStatsOutCellsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsPerSecond.setStatus("current")
_EqAtmVcStatsOutBitsPerSecond_Type = Counter64
_EqAtmVcStatsOutBitsPerSecond_Object = MibTableColumn
eqAtmVcStatsOutBitsPerSecond = _EqAtmVcStatsOutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 19),
    _EqAtmVcStatsOutBitsPerSecond_Type()
)
eqAtmVcStatsOutBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutBitsPerSecond.setStatus("current")
_EqAtmVcStatsOutCellsClp0_Type = Counter64
_EqAtmVcStatsOutCellsClp0_Object = MibTableColumn
eqAtmVcStatsOutCellsClp0 = _EqAtmVcStatsOutCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 20),
    _EqAtmVcStatsOutCellsClp0_Type()
)
eqAtmVcStatsOutCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsClp0.setStatus("current")
_EqAtmVcStatsOutCellsClp1_Type = Counter64
_EqAtmVcStatsOutCellsClp1_Object = MibTableColumn
eqAtmVcStatsOutCellsClp1 = _EqAtmVcStatsOutCellsClp1_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 21),
    _EqAtmVcStatsOutCellsClp1_Type()
)
eqAtmVcStatsOutCellsClp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsClp1.setStatus("current")
_EqAtmVcStatsOutCellsTagged_Type = Counter64
_EqAtmVcStatsOutCellsTagged_Object = MibTableColumn
eqAtmVcStatsOutCellsTagged = _EqAtmVcStatsOutCellsTagged_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 22),
    _EqAtmVcStatsOutCellsTagged_Type()
)
eqAtmVcStatsOutCellsTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsTagged.setStatus("current")
_EqAtmVcStatsOutCellsClp0Discards_Type = Counter64
_EqAtmVcStatsOutCellsClp0Discards_Object = MibTableColumn
eqAtmVcStatsOutCellsClp0Discards = _EqAtmVcStatsOutCellsClp0Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 23),
    _EqAtmVcStatsOutCellsClp0Discards_Type()
)
eqAtmVcStatsOutCellsClp0Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsClp0Discards.setStatus("current")
_EqAtmVcStatsOutCellsClp1Discards_Type = Counter64
_EqAtmVcStatsOutCellsClp1Discards_Object = MibTableColumn
eqAtmVcStatsOutCellsClp1Discards = _EqAtmVcStatsOutCellsClp1Discards_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 24),
    _EqAtmVcStatsOutCellsClp1Discards_Type()
)
eqAtmVcStatsOutCellsClp1Discards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsClp1Discards.setStatus("current")
_EqAtmVcStatsOutCellsOam_Type = Counter64
_EqAtmVcStatsOutCellsOam_Object = MibTableColumn
eqAtmVcStatsOutCellsOam = _EqAtmVcStatsOutCellsOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 25),
    _EqAtmVcStatsOutCellsOam_Type()
)
eqAtmVcStatsOutCellsOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsOam.setStatus("current")
_EqAtmVcStatsOutCellsClp0Oam_Type = Counter64
_EqAtmVcStatsOutCellsClp0Oam_Object = MibTableColumn
eqAtmVcStatsOutCellsClp0Oam = _EqAtmVcStatsOutCellsClp0Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 26),
    _EqAtmVcStatsOutCellsClp0Oam_Type()
)
eqAtmVcStatsOutCellsClp0Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsClp0Oam.setStatus("current")
_EqAtmVcStatsOutCellsClp1Oam_Type = Counter64
_EqAtmVcStatsOutCellsClp1Oam_Object = MibTableColumn
eqAtmVcStatsOutCellsClp1Oam = _EqAtmVcStatsOutCellsClp1Oam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 27),
    _EqAtmVcStatsOutCellsClp1Oam_Type()
)
eqAtmVcStatsOutCellsClp1Oam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsClp1Oam.setStatus("current")
_EqAtmVcStatsOutCellsLoopback_Type = Counter64
_EqAtmVcStatsOutCellsLoopback_Object = MibTableColumn
eqAtmVcStatsOutCellsLoopback = _EqAtmVcStatsOutCellsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 28),
    _EqAtmVcStatsOutCellsLoopback_Type()
)
eqAtmVcStatsOutCellsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsLoopback.setStatus("current")
_EqAtmVcStatsOutCellsLoopbackOam_Type = Counter64
_EqAtmVcStatsOutCellsLoopbackOam_Object = MibTableColumn
eqAtmVcStatsOutCellsLoopbackOam = _EqAtmVcStatsOutCellsLoopbackOam_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 29),
    _EqAtmVcStatsOutCellsLoopbackOam_Type()
)
eqAtmVcStatsOutCellsLoopbackOam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsOutCellsLoopbackOam.setStatus("current")


class _EqAtmVcStatsCLR_Type(Integer32):
    """Custom type eqAtmVcStatsCLR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_EqAtmVcStatsCLR_Type.__name__ = "Integer32"
_EqAtmVcStatsCLR_Object = MibTableColumn
eqAtmVcStatsCLR = _EqAtmVcStatsCLR_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 4, 1, 30),
    _EqAtmVcStatsCLR_Type()
)
eqAtmVcStatsCLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmVcStatsCLR.setStatus("current")
_EqAtmOamPmTable_Object = MibTable
eqAtmOamPmTable = _EqAtmOamPmTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5)
)
if mibBuilder.loadTexts:
    eqAtmOamPmTable.setStatus("current")
_EqAtmOamPmEntry_Object = MibTableRow
eqAtmOamPmEntry = _EqAtmOamPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1)
)
eqAtmOamPmEntry.setIndexNames(
    (0, "EQUIPE-ATM-MIB", "eqAtmOamPmIfIndex"),
    (0, "EQUIPE-ATM-MIB", "eqAtmOamPmVpi"),
    (0, "EQUIPE-ATM-MIB", "eqAtmOamPmVci"),
)
if mibBuilder.loadTexts:
    eqAtmOamPmEntry.setStatus("current")


class _EqAtmOamPmIfIndex_Type(Integer32):
    """Custom type eqAtmOamPmIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmOamPmIfIndex_Type.__name__ = "Integer32"
_EqAtmOamPmIfIndex_Object = MibTableColumn
eqAtmOamPmIfIndex = _EqAtmOamPmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 1),
    _EqAtmOamPmIfIndex_Type()
)
eqAtmOamPmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmIfIndex.setStatus("current")


class _EqAtmOamPmVpi_Type(Integer32):
    """Custom type eqAtmOamPmVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EqAtmOamPmVpi_Type.__name__ = "Integer32"
_EqAtmOamPmVpi_Object = MibTableColumn
eqAtmOamPmVpi = _EqAtmOamPmVpi_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 2),
    _EqAtmOamPmVpi_Type()
)
eqAtmOamPmVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmVpi.setStatus("current")


class _EqAtmOamPmVci_Type(Integer32):
    """Custom type eqAtmOamPmVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EqAtmOamPmVci_Type.__name__ = "Integer32"
_EqAtmOamPmVci_Object = MibTableColumn
eqAtmOamPmVci = _EqAtmOamPmVci_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 3),
    _EqAtmOamPmVci_Type()
)
eqAtmOamPmVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmVci.setStatus("current")


class _EqAtmOamPmStatus_Type(Integer32):
    """Custom type eqAtmOamPmStatus based on Integer32"""
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
        *(("activating", 1),
          ("connected", 2),
          ("failConnect", 3),
          ("failNoResource", 4))
    )


_EqAtmOamPmStatus_Type.__name__ = "Integer32"
_EqAtmOamPmStatus_Object = MibTableColumn
eqAtmOamPmStatus = _EqAtmOamPmStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 4),
    _EqAtmOamPmStatus_Type()
)
eqAtmOamPmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmStatus.setStatus("current")


class _EqAtmOamPmSessionType_Type(Integer32):
    """Custom type eqAtmOamPmSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("contCheck", 1),
          ("perfMonitoring", 2))
    )


_EqAtmOamPmSessionType_Type.__name__ = "Integer32"
_EqAtmOamPmSessionType_Object = MibTableColumn
eqAtmOamPmSessionType = _EqAtmOamPmSessionType_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 5),
    _EqAtmOamPmSessionType_Type()
)
eqAtmOamPmSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmSessionType.setStatus("current")


class _EqAtmOamPmSinkSource_Type(Integer32):
    """Custom type eqAtmOamPmSinkSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("sink", 1),
          ("source", 2))
    )


_EqAtmOamPmSinkSource_Type.__name__ = "Integer32"
_EqAtmOamPmSinkSource_Object = MibTableColumn
eqAtmOamPmSinkSource = _EqAtmOamPmSinkSource_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 6),
    _EqAtmOamPmSinkSource_Type()
)
eqAtmOamPmSinkSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmSinkSource.setStatus("current")


class _EqAtmOamPmBlockSize_Type(Integer32):
    """Custom type eqAtmOamPmBlockSize based on Integer32"""
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
        *(("bytes128", 1),
          ("bytes16K", 8),
          ("bytes1K", 4),
          ("bytes256", 2),
          ("bytes2K", 5),
          ("bytes32K", 9),
          ("bytes4K", 6),
          ("bytes512", 3),
          ("bytes8K", 7))
    )


_EqAtmOamPmBlockSize_Type.__name__ = "Integer32"
_EqAtmOamPmBlockSize_Object = MibTableColumn
eqAtmOamPmBlockSize = _EqAtmOamPmBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 7),
    _EqAtmOamPmBlockSize_Type()
)
eqAtmOamPmBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmBlockSize.setStatus("current")


class _EqAtmOamPmEndPt_Type(Integer32):
    """Custom type eqAtmOamPmEndPt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("segment", 1))
    )


_EqAtmOamPmEndPt_Type.__name__ = "Integer32"
_EqAtmOamPmEndPt_Object = MibTableColumn
eqAtmOamPmEndPt = _EqAtmOamPmEndPt_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 8),
    _EqAtmOamPmEndPt_Type()
)
eqAtmOamPmEndPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmEndPt.setStatus("current")


class _EqAtmOamPmFlow_Type(Integer32):
    """Custom type eqAtmOamPmFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f4", 1),
          ("f5", 2))
    )


_EqAtmOamPmFlow_Type.__name__ = "Integer32"
_EqAtmOamPmFlow_Object = MibTableColumn
eqAtmOamPmFlow = _EqAtmOamPmFlow_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 9),
    _EqAtmOamPmFlow_Type()
)
eqAtmOamPmFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmFlow.setStatus("current")


class _EqAtmOamPmDirection_Type(Integer32):
    """Custom type eqAtmOamPmDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("segment", 1))
    )


_EqAtmOamPmDirection_Type.__name__ = "Integer32"
_EqAtmOamPmDirection_Object = MibTableColumn
eqAtmOamPmDirection = _EqAtmOamPmDirection_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 10),
    _EqAtmOamPmDirection_Type()
)
eqAtmOamPmDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmDirection.setStatus("current")


class _EqAtmOamPmTimeout_Type(Integer32):
    """Custom type eqAtmOamPmTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_EqAtmOamPmTimeout_Type.__name__ = "Integer32"
_EqAtmOamPmTimeout_Object = MibTableColumn
eqAtmOamPmTimeout = _EqAtmOamPmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 11),
    _EqAtmOamPmTimeout_Type()
)
eqAtmOamPmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmTimeout.setStatus("current")


class _EqAtmOamPmRetryCount_Type(Integer32):
    """Custom type eqAtmOamPmRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_EqAtmOamPmRetryCount_Type.__name__ = "Integer32"
_EqAtmOamPmRetryCount_Object = MibTableColumn
eqAtmOamPmRetryCount = _EqAtmOamPmRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 12),
    _EqAtmOamPmRetryCount_Type()
)
eqAtmOamPmRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmRetryCount.setStatus("current")
_EqAtmOamPmFwdTxUserCellsClp0_Type = Counter32
_EqAtmOamPmFwdTxUserCellsClp0_Object = MibTableColumn
eqAtmOamPmFwdTxUserCellsClp0 = _EqAtmOamPmFwdTxUserCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 13),
    _EqAtmOamPmFwdTxUserCellsClp0_Type()
)
eqAtmOamPmFwdTxUserCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmFwdTxUserCellsClp0.setStatus("current")
_EqAtmOamPmFwdTxUserCellsClp01_Type = Counter32
_EqAtmOamPmFwdTxUserCellsClp01_Object = MibTableColumn
eqAtmOamPmFwdTxUserCellsClp01 = _EqAtmOamPmFwdTxUserCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 14),
    _EqAtmOamPmFwdTxUserCellsClp01_Type()
)
eqAtmOamPmFwdTxUserCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmFwdTxUserCellsClp01.setStatus("current")
_EqAtmOamPmFwdTxLostCellsClp0_Type = Counter32
_EqAtmOamPmFwdTxLostCellsClp0_Object = MibTableColumn
eqAtmOamPmFwdTxLostCellsClp0 = _EqAtmOamPmFwdTxLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 15),
    _EqAtmOamPmFwdTxLostCellsClp0_Type()
)
eqAtmOamPmFwdTxLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmFwdTxLostCellsClp0.setStatus("current")
_EqAtmOamPmFwdTxLostCellsClp01_Type = Counter32
_EqAtmOamPmFwdTxLostCellsClp01_Object = MibTableColumn
eqAtmOamPmFwdTxLostCellsClp01 = _EqAtmOamPmFwdTxLostCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 16),
    _EqAtmOamPmFwdTxLostCellsClp01_Type()
)
eqAtmOamPmFwdTxLostCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmFwdTxLostCellsClp01.setStatus("current")
_EqAtmOamPmFwdSECBs_Type = Counter32
_EqAtmOamPmFwdSECBs_Object = MibTableColumn
eqAtmOamPmFwdSECBs = _EqAtmOamPmFwdSECBs_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 17),
    _EqAtmOamPmFwdSECBs_Type()
)
eqAtmOamPmFwdSECBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmFwdSECBs.setStatus("current")
_EqAtmOamPmBwdTxUserCellsClp0_Type = Counter32
_EqAtmOamPmBwdTxUserCellsClp0_Object = MibTableColumn
eqAtmOamPmBwdTxUserCellsClp0 = _EqAtmOamPmBwdTxUserCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 18),
    _EqAtmOamPmBwdTxUserCellsClp0_Type()
)
eqAtmOamPmBwdTxUserCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmBwdTxUserCellsClp0.setStatus("current")
_EqAtmOamPmBwdTxUserCellsClp01_Type = Counter32
_EqAtmOamPmBwdTxUserCellsClp01_Object = MibTableColumn
eqAtmOamPmBwdTxUserCellsClp01 = _EqAtmOamPmBwdTxUserCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 19),
    _EqAtmOamPmBwdTxUserCellsClp01_Type()
)
eqAtmOamPmBwdTxUserCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmBwdTxUserCellsClp01.setStatus("current")
_EqAtmOamPmBwdTxLostCellsClp0_Type = Counter32
_EqAtmOamPmBwdTxLostCellsClp0_Object = MibTableColumn
eqAtmOamPmBwdTxLostCellsClp0 = _EqAtmOamPmBwdTxLostCellsClp0_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 20),
    _EqAtmOamPmBwdTxLostCellsClp0_Type()
)
eqAtmOamPmBwdTxLostCellsClp0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmBwdTxLostCellsClp0.setStatus("current")
_EqAtmOamPmBwdTxLostCellsClp01_Type = Counter32
_EqAtmOamPmBwdTxLostCellsClp01_Object = MibTableColumn
eqAtmOamPmBwdTxLostCellsClp01 = _EqAtmOamPmBwdTxLostCellsClp01_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 21),
    _EqAtmOamPmBwdTxLostCellsClp01_Type()
)
eqAtmOamPmBwdTxLostCellsClp01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmBwdTxLostCellsClp01.setStatus("current")
_EqAtmOamPmBwdSECBs_Type = Counter32
_EqAtmOamPmBwdSECBs_Object = MibTableColumn
eqAtmOamPmBwdSECBs = _EqAtmOamPmBwdSECBs_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 5, 1, 22),
    _EqAtmOamPmBwdSECBs_Type()
)
eqAtmOamPmBwdSECBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamPmBwdSECBs.setStatus("current")
_EqAtmOamLoopbackTable_Object = MibTable
eqAtmOamLoopbackTable = _EqAtmOamLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6)
)
if mibBuilder.loadTexts:
    eqAtmOamLoopbackTable.setStatus("current")
_EqAtmOamLoopbackEntry_Object = MibTableRow
eqAtmOamLoopbackEntry = _EqAtmOamLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1)
)
eqAtmOamLoopbackEntry.setIndexNames(
    (0, "EQUIPE-ATM-MIB", "eqAtmOamLoopbackIfIndex"),
    (0, "EQUIPE-ATM-MIB", "eqAtmOamLoopbackVpi"),
    (0, "EQUIPE-ATM-MIB", "eqAtmOamLoopbackVci"),
)
if mibBuilder.loadTexts:
    eqAtmOamLoopbackEntry.setStatus("current")


class _EqAtmOamLoopbackIfIndex_Type(Integer32):
    """Custom type eqAtmOamLoopbackIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmOamLoopbackIfIndex_Type.__name__ = "Integer32"
_EqAtmOamLoopbackIfIndex_Object = MibTableColumn
eqAtmOamLoopbackIfIndex = _EqAtmOamLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 1),
    _EqAtmOamLoopbackIfIndex_Type()
)
eqAtmOamLoopbackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackIfIndex.setStatus("current")


class _EqAtmOamLoopbackVpi_Type(Integer32):
    """Custom type eqAtmOamLoopbackVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EqAtmOamLoopbackVpi_Type.__name__ = "Integer32"
_EqAtmOamLoopbackVpi_Object = MibTableColumn
eqAtmOamLoopbackVpi = _EqAtmOamLoopbackVpi_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 2),
    _EqAtmOamLoopbackVpi_Type()
)
eqAtmOamLoopbackVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackVpi.setStatus("current")


class _EqAtmOamLoopbackVci_Type(Integer32):
    """Custom type eqAtmOamLoopbackVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EqAtmOamLoopbackVci_Type.__name__ = "Integer32"
_EqAtmOamLoopbackVci_Object = MibTableColumn
eqAtmOamLoopbackVci = _EqAtmOamLoopbackVci_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 3),
    _EqAtmOamLoopbackVci_Type()
)
eqAtmOamLoopbackVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackVci.setStatus("current")


class _EqAtmOamLoopbackStatus_Type(Integer32):
    """Custom type eqAtmOamLoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("completed", 2),
          ("inProgress", 1))
    )


_EqAtmOamLoopbackStatus_Type.__name__ = "Integer32"
_EqAtmOamLoopbackStatus_Object = MibTableColumn
eqAtmOamLoopbackStatus = _EqAtmOamLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 4),
    _EqAtmOamLoopbackStatus_Type()
)
eqAtmOamLoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackStatus.setStatus("current")


class _EqAtmOamLoopbackSendCount_Type(Integer32):
    """Custom type eqAtmOamLoopbackSendCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EqAtmOamLoopbackSendCount_Type.__name__ = "Integer32"
_EqAtmOamLoopbackSendCount_Object = MibTableColumn
eqAtmOamLoopbackSendCount = _EqAtmOamLoopbackSendCount_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 5),
    _EqAtmOamLoopbackSendCount_Type()
)
eqAtmOamLoopbackSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackSendCount.setStatus("current")


class _EqAtmOamLoopbackSendTrap_Type(Integer32):
    """Custom type eqAtmOamLoopbackSendTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 2),
          ("send", 1))
    )


_EqAtmOamLoopbackSendTrap_Type.__name__ = "Integer32"
_EqAtmOamLoopbackSendTrap_Object = MibTableColumn
eqAtmOamLoopbackSendTrap = _EqAtmOamLoopbackSendTrap_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 6),
    _EqAtmOamLoopbackSendTrap_Type()
)
eqAtmOamLoopbackSendTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackSendTrap.setStatus("current")


class _EqAtmOamLoopbackEndPoint_Type(Integer32):
    """Custom type eqAtmOamLoopbackEndPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("segment", 1))
    )


_EqAtmOamLoopbackEndPoint_Type.__name__ = "Integer32"
_EqAtmOamLoopbackEndPoint_Object = MibTableColumn
eqAtmOamLoopbackEndPoint = _EqAtmOamLoopbackEndPoint_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 7),
    _EqAtmOamLoopbackEndPoint_Type()
)
eqAtmOamLoopbackEndPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackEndPoint.setStatus("current")


class _EqAtmOamLoopbackFlow_Type(Integer32):
    """Custom type eqAtmOamLoopbackFlow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f4", 1),
          ("f5", 2))
    )


_EqAtmOamLoopbackFlow_Type.__name__ = "Integer32"
_EqAtmOamLoopbackFlow_Object = MibTableColumn
eqAtmOamLoopbackFlow = _EqAtmOamLoopbackFlow_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 8),
    _EqAtmOamLoopbackFlow_Type()
)
eqAtmOamLoopbackFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackFlow.setStatus("current")


class _EqAtmOamLoopbackDirection_Type(Integer32):
    """Custom type eqAtmOamLoopbackDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("segment", 1))
    )


_EqAtmOamLoopbackDirection_Type.__name__ = "Integer32"
_EqAtmOamLoopbackDirection_Object = MibTableColumn
eqAtmOamLoopbackDirection = _EqAtmOamLoopbackDirection_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 9),
    _EqAtmOamLoopbackDirection_Type()
)
eqAtmOamLoopbackDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackDirection.setStatus("current")


class _EqAtmOamLoopbackTimeout_Type(Integer32):
    """Custom type eqAtmOamLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_EqAtmOamLoopbackTimeout_Type.__name__ = "Integer32"
_EqAtmOamLoopbackTimeout_Object = MibTableColumn
eqAtmOamLoopbackTimeout = _EqAtmOamLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 10),
    _EqAtmOamLoopbackTimeout_Type()
)
eqAtmOamLoopbackTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackTimeout.setStatus("current")
_EqAtmOamLoopbackCellsReceived_Type = Counter32
_EqAtmOamLoopbackCellsReceived_Object = MibTableColumn
eqAtmOamLoopbackCellsReceived = _EqAtmOamLoopbackCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 11),
    _EqAtmOamLoopbackCellsReceived_Type()
)
eqAtmOamLoopbackCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackCellsReceived.setStatus("current")
_EqAtmOamLoopbackCellsTimedOut_Type = Counter32
_EqAtmOamLoopbackCellsTimedOut_Object = MibTableColumn
eqAtmOamLoopbackCellsTimedOut = _EqAtmOamLoopbackCellsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 12),
    _EqAtmOamLoopbackCellsTimedOut_Type()
)
eqAtmOamLoopbackCellsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackCellsTimedOut.setStatus("current")


class _EqAtmOamLoopbackAveCellTime_Type(Integer32):
    """Custom type eqAtmOamLoopbackAveCellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmOamLoopbackAveCellTime_Type.__name__ = "Integer32"
_EqAtmOamLoopbackAveCellTime_Object = MibTableColumn
eqAtmOamLoopbackAveCellTime = _EqAtmOamLoopbackAveCellTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 13),
    _EqAtmOamLoopbackAveCellTime_Type()
)
eqAtmOamLoopbackAveCellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackAveCellTime.setStatus("current")


class _EqAtmOamLoopbackMinCellTime_Type(Integer32):
    """Custom type eqAtmOamLoopbackMinCellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmOamLoopbackMinCellTime_Type.__name__ = "Integer32"
_EqAtmOamLoopbackMinCellTime_Object = MibTableColumn
eqAtmOamLoopbackMinCellTime = _EqAtmOamLoopbackMinCellTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 14),
    _EqAtmOamLoopbackMinCellTime_Type()
)
eqAtmOamLoopbackMinCellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackMinCellTime.setStatus("current")


class _EqAtmOamLoopbackMaxCellTime_Type(Integer32):
    """Custom type eqAtmOamLoopbackMaxCellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmOamLoopbackMaxCellTime_Type.__name__ = "Integer32"
_EqAtmOamLoopbackMaxCellTime_Object = MibTableColumn
eqAtmOamLoopbackMaxCellTime = _EqAtmOamLoopbackMaxCellTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 15),
    _EqAtmOamLoopbackMaxCellTime_Type()
)
eqAtmOamLoopbackMaxCellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackMaxCellTime.setStatus("current")


class _EqAtmOamLoopbackTotalCellTime_Type(Integer32):
    """Custom type eqAtmOamLoopbackTotalCellTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqAtmOamLoopbackTotalCellTime_Type.__name__ = "Integer32"
_EqAtmOamLoopbackTotalCellTime_Object = MibTableColumn
eqAtmOamLoopbackTotalCellTime = _EqAtmOamLoopbackTotalCellTime_Object(
    (1, 3, 6, 1, 4, 1, 5022, 2, 6, 1, 16),
    _EqAtmOamLoopbackTotalCellTime_Type()
)
eqAtmOamLoopbackTotalCellTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqAtmOamLoopbackTotalCellTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQUIPE-ATM-MIB",
    **{"AtmCauseCode": AtmCauseCode,
       "equipe": equipe,
       "eqAtmMib": eqAtmMib,
       "eqAtmStatsTable": eqAtmStatsTable,
       "eqAtmStatsEntry": eqAtmStatsEntry,
       "eqAtmStatsIfIndex": eqAtmStatsIfIndex,
       "eqAtmStatsInCells": eqAtmStatsInCells,
       "eqAtmStatsInCellsPerSecond": eqAtmStatsInCellsPerSecond,
       "eqAtmStatsInBitsPerSecond": eqAtmStatsInBitsPerSecond,
       "eqAtmStatsInCellsClp0": eqAtmStatsInCellsClp0,
       "eqAtmStatsInCellsClp1": eqAtmStatsInCellsClp1,
       "eqAtmStatsInCellsTagged": eqAtmStatsInCellsTagged,
       "eqAtmStatsInCellsClp0Discards": eqAtmStatsInCellsClp0Discards,
       "eqAtmStatsInCellsClp1Discards": eqAtmStatsInCellsClp1Discards,
       "eqAtmStatsInCellsOam": eqAtmStatsInCellsOam,
       "eqAtmStatsInCellsClp0Oam": eqAtmStatsInCellsClp0Oam,
       "eqAtmStatsInCellsClp1Oam": eqAtmStatsInCellsClp1Oam,
       "eqAtmStatsInCellsLoopback": eqAtmStatsInCellsLoopback,
       "eqAtmStatsInCellsLoopbackOam": eqAtmStatsInCellsLoopbackOam,
       "eqAtmStatsOutCells": eqAtmStatsOutCells,
       "eqAtmStatsOutCellsPerSecond": eqAtmStatsOutCellsPerSecond,
       "eqAtmStatsOutBitsPerSecond": eqAtmStatsOutBitsPerSecond,
       "eqAtmStatsOutCellsClp0": eqAtmStatsOutCellsClp0,
       "eqAtmStatsOutCellsClp1": eqAtmStatsOutCellsClp1,
       "eqAtmStatsOutCellsTagged": eqAtmStatsOutCellsTagged,
       "eqAtmStatsOutCellsClp0Discards": eqAtmStatsOutCellsClp0Discards,
       "eqAtmStatsOutCellsClp1Discards": eqAtmStatsOutCellsClp1Discards,
       "eqAtmStatsOutCellsOam": eqAtmStatsOutCellsOam,
       "eqAtmStatsOutCellsClp0Oam": eqAtmStatsOutCellsClp0Oam,
       "eqAtmStatsOutCellsClp1Oam": eqAtmStatsOutCellsClp1Oam,
       "eqAtmStatsOutCellsLoopback": eqAtmStatsOutCellsLoopback,
       "eqAtmStatsOutCellsLoopbackOam": eqAtmStatsOutCellsLoopbackOam,
       "eqAtmStatsCLR": eqAtmStatsCLR,
       "eqAtmSvcStatsTable": eqAtmSvcStatsTable,
       "eqAtmSvcStatsEntry": eqAtmSvcStatsEntry,
       "eqAtmSvcStatsIfIndex": eqAtmSvcStatsIfIndex,
       "eqAtmSvcTotal": eqAtmSvcTotal,
       "eqAtmSvcConnected": eqAtmSvcConnected,
       "eqAtmSvcFailures": eqAtmSvcFailures,
       "eqAtmSvcInLastCauseCode": eqAtmSvcInLastCauseCode,
       "eqAtmSvcInSetupPdus": eqAtmSvcInSetupPdus,
       "eqAtmSvcInCallProceeding": eqAtmSvcInCallProceeding,
       "eqAtmSvcInPdusConnect": eqAtmSvcInPdusConnect,
       "eqAtmSvcInPdusConnectAck": eqAtmSvcInPdusConnectAck,
       "eqAtmSvcInPdusReleaseComplete": eqAtmSvcInPdusReleaseComplete,
       "eqAtmSvcInPdusAddParty": eqAtmSvcInPdusAddParty,
       "eqAtmSvcInPdusAddPartyAck": eqAtmSvcInPdusAddPartyAck,
       "eqAtmSvcInPdusAddPartyReject": eqAtmSvcInPdusAddPartyReject,
       "eqAtmSvcInPdusDropParty": eqAtmSvcInPdusDropParty,
       "eqAtmSvcInPdusDropPartyAck": eqAtmSvcInPdusDropPartyAck,
       "eqAtmSvcInPdusStatusEnquiry": eqAtmSvcInPdusStatusEnquiry,
       "eqAtmSvcInPdusStatus": eqAtmSvcInPdusStatus,
       "eqAtmSvcInPdusRestart": eqAtmSvcInPdusRestart,
       "eqAtmSvcInPdusRestartAck": eqAtmSvcInPdusRestartAck,
       "eqAtmSvcInPdusNotify": eqAtmSvcInPdusNotify,
       "eqAtmSvcInPdusProgress": eqAtmSvcInPdusProgress,
       "eqAtmSvcInPdusAlerting": eqAtmSvcInPdusAlerting,
       "eqAtmSvcInPdusPartyAlerting": eqAtmSvcInPdusPartyAlerting,
       "eqAtmSvcOutLastCauseCode": eqAtmSvcOutLastCauseCode,
       "eqAtmSvcOutSetupPdus": eqAtmSvcOutSetupPdus,
       "eqAtmSvcOutCallProceeding": eqAtmSvcOutCallProceeding,
       "eqAtmSvcOutPdusConnect": eqAtmSvcOutPdusConnect,
       "eqAtmSvcOutPdusConnectAck": eqAtmSvcOutPdusConnectAck,
       "eqAtmSvcOutPdusReleaseComplete": eqAtmSvcOutPdusReleaseComplete,
       "eqAtmSvcOutPdusAddParty": eqAtmSvcOutPdusAddParty,
       "eqAtmSvcOutPdusAddPartyAck": eqAtmSvcOutPdusAddPartyAck,
       "eqAtmSvcOutPdusAddPartyReject": eqAtmSvcOutPdusAddPartyReject,
       "eqAtmSvcOutPdusDropParty": eqAtmSvcOutPdusDropParty,
       "eqAtmSvcOutPdusDropPartyAck": eqAtmSvcOutPdusDropPartyAck,
       "eqAtmSvcOutPdusStatusEnquiry": eqAtmSvcOutPdusStatusEnquiry,
       "eqAtmSvcOutPdusStatus": eqAtmSvcOutPdusStatus,
       "eqAtmSvcOutPdusRestart": eqAtmSvcOutPdusRestart,
       "eqAtmSvcOutPdusRestartAck": eqAtmSvcOutPdusRestartAck,
       "eqAtmSvcOutPdusNotify": eqAtmSvcOutPdusNotify,
       "eqAtmSvcOutPdusProgress": eqAtmSvcOutPdusProgress,
       "eqAtmSvcOutPdusAlerting": eqAtmSvcOutPdusAlerting,
       "eqAtmSvcOutPdusPartyAlerting": eqAtmSvcOutPdusPartyAlerting,
       "eqAtmSaalStatsTable": eqAtmSaalStatsTable,
       "eqAtmSaalStatsEntry": eqAtmSaalStatsEntry,
       "eqAtmSaalStatsIfIndex": eqAtmSaalStatsIfIndex,
       "eqAtmSaalInErrors": eqAtmSaalInErrors,
       "eqAtmSaalInDiscards": eqAtmSaalInDiscards,
       "eqAtmSaalInBeginPdus": eqAtmSaalInBeginPdus,
       "eqAtmSaalInBeginAckPdus": eqAtmSaalInBeginAckPdus,
       "eqAtmSaalInBeginRejectPdus": eqAtmSaalInBeginRejectPdus,
       "eqAtmSaalInEndPdus": eqAtmSaalInEndPdus,
       "eqAtmSaalInEndAckPdus": eqAtmSaalInEndAckPdus,
       "eqAtmSaalInResyncPdus": eqAtmSaalInResyncPdus,
       "eqAtmSaalInResyncAckPdus": eqAtmSaalInResyncAckPdus,
       "eqAtmSaalInErrRecoveryPdus": eqAtmSaalInErrRecoveryPdus,
       "eqAtmSaalInSeqDataPdus": eqAtmSaalInSeqDataPdus,
       "eqAtmSaalInPollPdus": eqAtmSaalInPollPdus,
       "eqAtmSaalInStatusPdus": eqAtmSaalInStatusPdus,
       "eqAtmSaalInUnsolicitedStatusPdus": eqAtmSaalInUnsolicitedStatusPdus,
       "eqAtmSaalInUnsolicitedUserPdus": eqAtmSaalInUnsolicitedUserPdus,
       "eqAtmSaalInUnnumberedUserPdus": eqAtmSaalInUnnumberedUserPdus,
       "eqAtmSaalInUnnumberedMgmtPdus": eqAtmSaalInUnnumberedMgmtPdus,
       "eqAtmSaalInSignalOctets": eqAtmSaalInSignalOctets,
       "eqAtmSaalOutDiscards": eqAtmSaalOutDiscards,
       "eqAtmSaalOutBeginPdus": eqAtmSaalOutBeginPdus,
       "eqAtmSaalOutBeginAckPdus": eqAtmSaalOutBeginAckPdus,
       "eqAtmSaalOutBeginRejectPdus": eqAtmSaalOutBeginRejectPdus,
       "eqAtmSaalOutEndPdus": eqAtmSaalOutEndPdus,
       "eqAtmSaalOutEndAckPdus": eqAtmSaalOutEndAckPdus,
       "eqAtmSaalOutResyncPdus": eqAtmSaalOutResyncPdus,
       "eqAtmSaalOutResyncAckPdus": eqAtmSaalOutResyncAckPdus,
       "eqAtmSaalOutErrRecoveryPdus": eqAtmSaalOutErrRecoveryPdus,
       "eqAtmSaalOutSeqDataPdus": eqAtmSaalOutSeqDataPdus,
       "eqAtmSaalOutPollPdus": eqAtmSaalOutPollPdus,
       "eqAtmSaalOutStatusPdus": eqAtmSaalOutStatusPdus,
       "eqAtmSaalOutUnsolicitedStatusPdus": eqAtmSaalOutUnsolicitedStatusPdus,
       "eqAtmSaalOutUnsolicitedUserPdus": eqAtmSaalOutUnsolicitedUserPdus,
       "eqAtmSaalOutUnnumberedUserPdus": eqAtmSaalOutUnnumberedUserPdus,
       "eqAtmSaalOutUnnumberedMgmtPdus": eqAtmSaalOutUnnumberedMgmtPdus,
       "eqAtmSaalOutSignalOctets": eqAtmSaalOutSignalOctets,
       "eqAtmSaalOutWindowSize": eqAtmSaalOutWindowSize,
       "eqAtmVcStatsTable": eqAtmVcStatsTable,
       "eqAtmVcStatsEntry": eqAtmVcStatsEntry,
       "eqAtmVcStatsIfIndex": eqAtmVcStatsIfIndex,
       "eqAtmVcStatsVpi": eqAtmVcStatsVpi,
       "eqAtmVcStatsVci": eqAtmVcStatsVci,
       "eqAtmVcStatsInCells": eqAtmVcStatsInCells,
       "eqAtmVcStatsInCellsPerSecond": eqAtmVcStatsInCellsPerSecond,
       "eqAtmVcStatsInBitsPerSecond": eqAtmVcStatsInBitsPerSecond,
       "eqAtmVcStatsInCellsClp0": eqAtmVcStatsInCellsClp0,
       "eqAtmVcStatsInCellsClp1": eqAtmVcStatsInCellsClp1,
       "eqAtmVcStatsInCellsTagged": eqAtmVcStatsInCellsTagged,
       "eqAtmVcStatsInCellsClp0Discards": eqAtmVcStatsInCellsClp0Discards,
       "eqAtmVcStatsInCellsClp1Discards": eqAtmVcStatsInCellsClp1Discards,
       "eqAtmVcStatsInCellsOam": eqAtmVcStatsInCellsOam,
       "eqAtmVcStatsInCellsClp0Oam": eqAtmVcStatsInCellsClp0Oam,
       "eqAtmVcStatsInCellsClp1Oam": eqAtmVcStatsInCellsClp1Oam,
       "eqAtmVcStatsInCellsLoopback": eqAtmVcStatsInCellsLoopback,
       "eqAtmVcStatsInCellsLoopbackOam": eqAtmVcStatsInCellsLoopbackOam,
       "eqAtmVcStatsOutCells": eqAtmVcStatsOutCells,
       "eqAtmVcStatsOutCellsPerSecond": eqAtmVcStatsOutCellsPerSecond,
       "eqAtmVcStatsOutBitsPerSecond": eqAtmVcStatsOutBitsPerSecond,
       "eqAtmVcStatsOutCellsClp0": eqAtmVcStatsOutCellsClp0,
       "eqAtmVcStatsOutCellsClp1": eqAtmVcStatsOutCellsClp1,
       "eqAtmVcStatsOutCellsTagged": eqAtmVcStatsOutCellsTagged,
       "eqAtmVcStatsOutCellsClp0Discards": eqAtmVcStatsOutCellsClp0Discards,
       "eqAtmVcStatsOutCellsClp1Discards": eqAtmVcStatsOutCellsClp1Discards,
       "eqAtmVcStatsOutCellsOam": eqAtmVcStatsOutCellsOam,
       "eqAtmVcStatsOutCellsClp0Oam": eqAtmVcStatsOutCellsClp0Oam,
       "eqAtmVcStatsOutCellsClp1Oam": eqAtmVcStatsOutCellsClp1Oam,
       "eqAtmVcStatsOutCellsLoopback": eqAtmVcStatsOutCellsLoopback,
       "eqAtmVcStatsOutCellsLoopbackOam": eqAtmVcStatsOutCellsLoopbackOam,
       "eqAtmVcStatsCLR": eqAtmVcStatsCLR,
       "eqAtmOamPmTable": eqAtmOamPmTable,
       "eqAtmOamPmEntry": eqAtmOamPmEntry,
       "eqAtmOamPmIfIndex": eqAtmOamPmIfIndex,
       "eqAtmOamPmVpi": eqAtmOamPmVpi,
       "eqAtmOamPmVci": eqAtmOamPmVci,
       "eqAtmOamPmStatus": eqAtmOamPmStatus,
       "eqAtmOamPmSessionType": eqAtmOamPmSessionType,
       "eqAtmOamPmSinkSource": eqAtmOamPmSinkSource,
       "eqAtmOamPmBlockSize": eqAtmOamPmBlockSize,
       "eqAtmOamPmEndPt": eqAtmOamPmEndPt,
       "eqAtmOamPmFlow": eqAtmOamPmFlow,
       "eqAtmOamPmDirection": eqAtmOamPmDirection,
       "eqAtmOamPmTimeout": eqAtmOamPmTimeout,
       "eqAtmOamPmRetryCount": eqAtmOamPmRetryCount,
       "eqAtmOamPmFwdTxUserCellsClp0": eqAtmOamPmFwdTxUserCellsClp0,
       "eqAtmOamPmFwdTxUserCellsClp01": eqAtmOamPmFwdTxUserCellsClp01,
       "eqAtmOamPmFwdTxLostCellsClp0": eqAtmOamPmFwdTxLostCellsClp0,
       "eqAtmOamPmFwdTxLostCellsClp01": eqAtmOamPmFwdTxLostCellsClp01,
       "eqAtmOamPmFwdSECBs": eqAtmOamPmFwdSECBs,
       "eqAtmOamPmBwdTxUserCellsClp0": eqAtmOamPmBwdTxUserCellsClp0,
       "eqAtmOamPmBwdTxUserCellsClp01": eqAtmOamPmBwdTxUserCellsClp01,
       "eqAtmOamPmBwdTxLostCellsClp0": eqAtmOamPmBwdTxLostCellsClp0,
       "eqAtmOamPmBwdTxLostCellsClp01": eqAtmOamPmBwdTxLostCellsClp01,
       "eqAtmOamPmBwdSECBs": eqAtmOamPmBwdSECBs,
       "eqAtmOamLoopbackTable": eqAtmOamLoopbackTable,
       "eqAtmOamLoopbackEntry": eqAtmOamLoopbackEntry,
       "eqAtmOamLoopbackIfIndex": eqAtmOamLoopbackIfIndex,
       "eqAtmOamLoopbackVpi": eqAtmOamLoopbackVpi,
       "eqAtmOamLoopbackVci": eqAtmOamLoopbackVci,
       "eqAtmOamLoopbackStatus": eqAtmOamLoopbackStatus,
       "eqAtmOamLoopbackSendCount": eqAtmOamLoopbackSendCount,
       "eqAtmOamLoopbackSendTrap": eqAtmOamLoopbackSendTrap,
       "eqAtmOamLoopbackEndPoint": eqAtmOamLoopbackEndPoint,
       "eqAtmOamLoopbackFlow": eqAtmOamLoopbackFlow,
       "eqAtmOamLoopbackDirection": eqAtmOamLoopbackDirection,
       "eqAtmOamLoopbackTimeout": eqAtmOamLoopbackTimeout,
       "eqAtmOamLoopbackCellsReceived": eqAtmOamLoopbackCellsReceived,
       "eqAtmOamLoopbackCellsTimedOut": eqAtmOamLoopbackCellsTimedOut,
       "eqAtmOamLoopbackAveCellTime": eqAtmOamLoopbackAveCellTime,
       "eqAtmOamLoopbackMinCellTime": eqAtmOamLoopbackMinCellTime,
       "eqAtmOamLoopbackMaxCellTime": eqAtmOamLoopbackMaxCellTime,
       "eqAtmOamLoopbackTotalCellTime": eqAtmOamLoopbackTotalCellTime}
)
