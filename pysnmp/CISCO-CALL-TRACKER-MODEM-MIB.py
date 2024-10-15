# SNMP MIB module (CISCO-CALL-TRACKER-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CALL-TRACKER-MODEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:49 2024
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

(cctActiveCallId,
 cctHistoryIndex) = mibBuilder.importSymbols(
    "CISCO-CALL-TRACKER-MIB",
    "cctActiveCallId",
    "cctHistoryIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ciscoCallTrackerModemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165)
)
ciscoCallTrackerModemMIB.setRevisions(
        ("2005-12-06 00:00",
         "2001-12-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CctmModulation(Integer32, TextualConvention):
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("bell103a", 2),
          ("bell212a", 3),
          ("k56flex", 14),
          ("other", 1),
          ("v110", 20),
          ("v17", 11),
          ("v21", 4),
          ("v22", 5),
          ("v22bis", 6),
          ("v23", 15),
          ("v27ter", 19),
          ("v29", 12),
          ("v32", 7),
          ("v32bis", 8),
          ("v32terbo", 16),
          ("v33", 13),
          ("v34", 10),
          ("v34plus", 17),
          ("v90", 18),
          ("vfc", 9))
    )



class CctmECProtocol(Integer32, TextualConvention):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("ara1", 7),
          ("ara2", 8),
          ("asyncMode", 6),
          ("direct", 2),
          ("lapmV42", 4),
          ("mnp", 3),
          ("normal", 1),
          ("other", 9),
          ("syncMode", 5))
    )



class CctmDataCompression(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("mnp5", 5),
          ("none", 1),
          ("v42bisBoth", 4),
          ("v42bisRx", 3),
          ("v42bisTx", 2),
          ("v44Both", 8),
          ("v44Rx", 7),
          ("v44Tx", 6))
    )



# MIB Managed Objects in the order of their OIDs

_CctmMIBObjects_ObjectIdentity = ObjectIdentity
cctmMIBObjects = _CctmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1)
)
_CctmActive_ObjectIdentity = ObjectIdentity
cctmActive = _CctmActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1)
)
_CctmActiveTable_Object = MibTable
cctmActiveTable = _CctmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cctmActiveTable.setStatus("current")
_CctmActiveEntry_Object = MibTableRow
cctmActiveEntry = _CctmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1)
)
cctmActiveEntry.setIndexNames(
    (0, "CISCO-CALL-TRACKER-MIB", "cctActiveCallId"),
)
if mibBuilder.loadTexts:
    cctmActiveEntry.setStatus("current")
_CctmActiveProjectedMaxRxRate_Type = Unsigned32
_CctmActiveProjectedMaxRxRate_Object = MibTableColumn
cctmActiveProjectedMaxRxRate = _CctmActiveProjectedMaxRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 1),
    _CctmActiveProjectedMaxRxRate_Type()
)
cctmActiveProjectedMaxRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveProjectedMaxRxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveProjectedMaxRxRate.setUnits("bits per second")
_CctmActiveProjectedMaxTxRate_Type = Unsigned32
_CctmActiveProjectedMaxTxRate_Object = MibTableColumn
cctmActiveProjectedMaxTxRate = _CctmActiveProjectedMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 2),
    _CctmActiveProjectedMaxTxRate_Type()
)
cctmActiveProjectedMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveProjectedMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveProjectedMaxTxRate.setUnits("bits per second")
_CctmActiveRxRate_Type = Unsigned32
_CctmActiveRxRate_Object = MibTableColumn
cctmActiveRxRate = _CctmActiveRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 3),
    _CctmActiveRxRate_Type()
)
cctmActiveRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveRxRate.setUnits("bits per second")
_CctmActiveTxRate_Type = Unsigned32
_CctmActiveTxRate_Object = MibTableColumn
cctmActiveTxRate = _CctmActiveTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 4),
    _CctmActiveTxRate_Type()
)
cctmActiveTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveTxRate.setUnits("bits per second")
_CctmActiveAttemptedModulation_Type = CctmModulation
_CctmActiveAttemptedModulation_Object = MibTableColumn
cctmActiveAttemptedModulation = _CctmActiveAttemptedModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 5),
    _CctmActiveAttemptedModulation_Type()
)
cctmActiveAttemptedModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveAttemptedModulation.setStatus("current")
_CctmActiveInitialModulation_Type = CctmModulation
_CctmActiveInitialModulation_Object = MibTableColumn
cctmActiveInitialModulation = _CctmActiveInitialModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 6),
    _CctmActiveInitialModulation_Type()
)
cctmActiveInitialModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveInitialModulation.setStatus("current")
_CctmActiveModulation_Type = CctmModulation
_CctmActiveModulation_Object = MibTableColumn
cctmActiveModulation = _CctmActiveModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 7),
    _CctmActiveModulation_Type()
)
cctmActiveModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveModulation.setStatus("current")
_CctmActiveAttemptedECProtocol_Type = CctmECProtocol
_CctmActiveAttemptedECProtocol_Object = MibTableColumn
cctmActiveAttemptedECProtocol = _CctmActiveAttemptedECProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 8),
    _CctmActiveAttemptedECProtocol_Type()
)
cctmActiveAttemptedECProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveAttemptedECProtocol.setStatus("current")
_CctmActiveECProtocol_Type = CctmECProtocol
_CctmActiveECProtocol_Object = MibTableColumn
cctmActiveECProtocol = _CctmActiveECProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 9),
    _CctmActiveECProtocol_Type()
)
cctmActiveECProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveECProtocol.setStatus("current")


class _CctmActiveSupportedDC_Type(Bits):
    """Custom type cctmActiveSupportedDC based on Bits"""
    namedValues = NamedValues(
        *(("mnp5", 0),
          ("v42bisRx", 1),
          ("v42bisTx", 2),
          ("v44Rx", 3),
          ("v44Tx", 4))
    )

_CctmActiveSupportedDC_Type.__name__ = "Bits"
_CctmActiveSupportedDC_Object = MibTableColumn
cctmActiveSupportedDC = _CctmActiveSupportedDC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 10),
    _CctmActiveSupportedDC_Type()
)
cctmActiveSupportedDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveSupportedDC.setStatus("current")
_CctmActiveDataCompression_Type = CctmDataCompression
_CctmActiveDataCompression_Object = MibTableColumn
cctmActiveDataCompression = _CctmActiveDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 11),
    _CctmActiveDataCompression_Type()
)
cctmActiveDataCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveDataCompression.setStatus("current")
_CctmActiveRxHighWatermark_Type = Gauge32
_CctmActiveRxHighWatermark_Object = MibTableColumn
cctmActiveRxHighWatermark = _CctmActiveRxHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 12),
    _CctmActiveRxHighWatermark_Type()
)
cctmActiveRxHighWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveRxHighWatermark.setUnits("bits per second")
_CctmActiveRxLowWatermark_Type = Gauge32
_CctmActiveRxLowWatermark_Object = MibTableColumn
cctmActiveRxLowWatermark = _CctmActiveRxLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 13),
    _CctmActiveRxLowWatermark_Type()
)
cctmActiveRxLowWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveRxLowWatermark.setUnits("bits per second")
_CctmActiveTxHighWatermark_Type = Gauge32
_CctmActiveTxHighWatermark_Object = MibTableColumn
cctmActiveTxHighWatermark = _CctmActiveTxHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 14),
    _CctmActiveTxHighWatermark_Type()
)
cctmActiveTxHighWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveTxHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveTxHighWatermark.setUnits("bits per second")
_CctmActiveTxLowWatermark_Type = Gauge32
_CctmActiveTxLowWatermark_Object = MibTableColumn
cctmActiveTxLowWatermark = _CctmActiveTxLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 15),
    _CctmActiveTxLowWatermark_Type()
)
cctmActiveTxLowWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveTxLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmActiveTxLowWatermark.setUnits("bits per second")
_CctmActiveLocalUpRateShifts_Type = Counter32
_CctmActiveLocalUpRateShifts_Object = MibTableColumn
cctmActiveLocalUpRateShifts = _CctmActiveLocalUpRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 16),
    _CctmActiveLocalUpRateShifts_Type()
)
cctmActiveLocalUpRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveLocalUpRateShifts.setStatus("current")
_CctmActiveLocalDownRateShifts_Type = Counter32
_CctmActiveLocalDownRateShifts_Object = MibTableColumn
cctmActiveLocalDownRateShifts = _CctmActiveLocalDownRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 17),
    _CctmActiveLocalDownRateShifts_Type()
)
cctmActiveLocalDownRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveLocalDownRateShifts.setStatus("current")
_CctmActiveRemoteUpRateShifts_Type = Counter32
_CctmActiveRemoteUpRateShifts_Object = MibTableColumn
cctmActiveRemoteUpRateShifts = _CctmActiveRemoteUpRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 18),
    _CctmActiveRemoteUpRateShifts_Type()
)
cctmActiveRemoteUpRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRemoteUpRateShifts.setStatus("current")
_CctmActiveRemoteDownRateShifts_Type = Counter32
_CctmActiveRemoteDownRateShifts_Object = MibTableColumn
cctmActiveRemoteDownRateShifts = _CctmActiveRemoteDownRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 19),
    _CctmActiveRemoteDownRateShifts_Type()
)
cctmActiveRemoteDownRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRemoteDownRateShifts.setStatus("current")
_CctmActiveRateShiftFailures_Type = Counter32
_CctmActiveRateShiftFailures_Object = MibTableColumn
cctmActiveRateShiftFailures = _CctmActiveRateShiftFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 20),
    _CctmActiveRateShiftFailures_Type()
)
cctmActiveRateShiftFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRateShiftFailures.setStatus("current")
_CctmActiveLocalRetrains_Type = Counter32
_CctmActiveLocalRetrains_Object = MibTableColumn
cctmActiveLocalRetrains = _CctmActiveLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 21),
    _CctmActiveLocalRetrains_Type()
)
cctmActiveLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveLocalRetrains.setStatus("current")
_CctmActiveRemoteRetrains_Type = Counter32
_CctmActiveRemoteRetrains_Object = MibTableColumn
cctmActiveRemoteRetrains = _CctmActiveRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 22),
    _CctmActiveRemoteRetrains_Type()
)
cctmActiveRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRemoteRetrains.setStatus("current")
_CctmActiveRetrainFailures_Type = Counter32
_CctmActiveRetrainFailures_Object = MibTableColumn
cctmActiveRetrainFailures = _CctmActiveRetrainFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 23),
    _CctmActiveRetrainFailures_Type()
)
cctmActiveRetrainFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRetrainFailures.setStatus("current")
_CctmActiveRxLinkOctets_Type = Counter32
_CctmActiveRxLinkOctets_Object = MibTableColumn
cctmActiveRxLinkOctets = _CctmActiveRxLinkOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 24),
    _CctmActiveRxLinkOctets_Type()
)
cctmActiveRxLinkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxLinkOctets.setStatus("current")
_CctmActiveTxLinkOctets_Type = Counter32
_CctmActiveTxLinkOctets_Object = MibTableColumn
cctmActiveTxLinkOctets = _CctmActiveTxLinkOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 25),
    _CctmActiveTxLinkOctets_Type()
)
cctmActiveTxLinkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveTxLinkOctets.setStatus("current")
_CctmActiveRxECFrames_Type = Counter32
_CctmActiveRxECFrames_Object = MibTableColumn
cctmActiveRxECFrames = _CctmActiveRxECFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 26),
    _CctmActiveRxECFrames_Type()
)
cctmActiveRxECFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxECFrames.setStatus("current")
_CctmActiveTxECFrames_Type = Counter32
_CctmActiveTxECFrames_Object = MibTableColumn
cctmActiveTxECFrames = _CctmActiveTxECFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 27),
    _CctmActiveTxECFrames_Type()
)
cctmActiveTxECFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveTxECFrames.setStatus("current")
_CctmActiveRxECNAKs_Type = Counter32
_CctmActiveRxECNAKs_Object = MibTableColumn
cctmActiveRxECNAKs = _CctmActiveRxECNAKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 28),
    _CctmActiveRxECNAKs_Type()
)
cctmActiveRxECNAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxECNAKs.setStatus("current")
_CctmActiveTxECNAKs_Type = Counter32
_CctmActiveTxECNAKs_Object = MibTableColumn
cctmActiveTxECNAKs = _CctmActiveTxECNAKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 29),
    _CctmActiveTxECNAKs_Type()
)
cctmActiveTxECNAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveTxECNAKs.setStatus("current")
_CctmActiveRxECFramesBad_Type = Counter32
_CctmActiveRxECFramesBad_Object = MibTableColumn
cctmActiveRxECFramesBad = _CctmActiveRxECFramesBad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 30),
    _CctmActiveRxECFramesBad_Type()
)
cctmActiveRxECFramesBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxECFramesBad.setStatus("current")
_CctmActiveECFramesResent_Type = Counter32
_CctmActiveECFramesResent_Object = MibTableColumn
cctmActiveECFramesResent = _CctmActiveECFramesResent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 31),
    _CctmActiveECFramesResent_Type()
)
cctmActiveECFramesResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveECFramesResent.setStatus("current")
_CctmActiveECLinkTimeouts_Type = Counter32
_CctmActiveECLinkTimeouts_Object = MibTableColumn
cctmActiveECLinkTimeouts = _CctmActiveECLinkTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 32),
    _CctmActiveECLinkTimeouts_Type()
)
cctmActiveECLinkTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveECLinkTimeouts.setStatus("current")
_CctmActiveRxCharLost_Type = Counter32
_CctmActiveRxCharLost_Object = MibTableColumn
cctmActiveRxCharLost = _CctmActiveRxCharLost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 1, 1, 1, 33),
    _CctmActiveRxCharLost_Type()
)
cctmActiveRxCharLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmActiveRxCharLost.setStatus("current")
_CctmHistory_ObjectIdentity = ObjectIdentity
cctmHistory = _CctmHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2)
)
_CctmHistoryTable_Object = MibTable
cctmHistoryTable = _CctmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cctmHistoryTable.setStatus("current")
_CctmHistoryEntry_Object = MibTableRow
cctmHistoryEntry = _CctmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1)
)
cctmHistoryEntry.setIndexNames(
    (0, "CISCO-CALL-TRACKER-MIB", "cctHistoryIndex"),
)
if mibBuilder.loadTexts:
    cctmHistoryEntry.setStatus("current")
_CctmHistoryProjectedMaxRxRate_Type = Unsigned32
_CctmHistoryProjectedMaxRxRate_Object = MibTableColumn
cctmHistoryProjectedMaxRxRate = _CctmHistoryProjectedMaxRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 1),
    _CctmHistoryProjectedMaxRxRate_Type()
)
cctmHistoryProjectedMaxRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryProjectedMaxRxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryProjectedMaxRxRate.setUnits("bits per second")
_CctmHistoryProjectedMaxTxRate_Type = Unsigned32
_CctmHistoryProjectedMaxTxRate_Object = MibTableColumn
cctmHistoryProjectedMaxTxRate = _CctmHistoryProjectedMaxTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 2),
    _CctmHistoryProjectedMaxTxRate_Type()
)
cctmHistoryProjectedMaxTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryProjectedMaxTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryProjectedMaxTxRate.setUnits("bits per second")
_CctmHistoryFinalRxRate_Type = Unsigned32
_CctmHistoryFinalRxRate_Object = MibTableColumn
cctmHistoryFinalRxRate = _CctmHistoryFinalRxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 3),
    _CctmHistoryFinalRxRate_Type()
)
cctmHistoryFinalRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryFinalRxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryFinalRxRate.setUnits("bits per second")
_CctmHistoryFinalTxRate_Type = Unsigned32
_CctmHistoryFinalTxRate_Object = MibTableColumn
cctmHistoryFinalTxRate = _CctmHistoryFinalTxRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 4),
    _CctmHistoryFinalTxRate_Type()
)
cctmHistoryFinalTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryFinalTxRate.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryFinalTxRate.setUnits("bits per second")
_CctmHistoryAttemptedModulation_Type = CctmModulation
_CctmHistoryAttemptedModulation_Object = MibTableColumn
cctmHistoryAttemptedModulation = _CctmHistoryAttemptedModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 5),
    _CctmHistoryAttemptedModulation_Type()
)
cctmHistoryAttemptedModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryAttemptedModulation.setStatus("current")
_CctmHistoryInitialModulation_Type = CctmModulation
_CctmHistoryInitialModulation_Object = MibTableColumn
cctmHistoryInitialModulation = _CctmHistoryInitialModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 6),
    _CctmHistoryInitialModulation_Type()
)
cctmHistoryInitialModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryInitialModulation.setStatus("current")
_CctmHistoryFinalModulation_Type = CctmModulation
_CctmHistoryFinalModulation_Object = MibTableColumn
cctmHistoryFinalModulation = _CctmHistoryFinalModulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 7),
    _CctmHistoryFinalModulation_Type()
)
cctmHistoryFinalModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryFinalModulation.setStatus("current")
_CctmHistoryAttemptedECProtocol_Type = CctmECProtocol
_CctmHistoryAttemptedECProtocol_Object = MibTableColumn
cctmHistoryAttemptedECProtocol = _CctmHistoryAttemptedECProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 8),
    _CctmHistoryAttemptedECProtocol_Type()
)
cctmHistoryAttemptedECProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryAttemptedECProtocol.setStatus("current")
_CctmHistoryECProtocol_Type = CctmECProtocol
_CctmHistoryECProtocol_Object = MibTableColumn
cctmHistoryECProtocol = _CctmHistoryECProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 9),
    _CctmHistoryECProtocol_Type()
)
cctmHistoryECProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryECProtocol.setStatus("current")


class _CctmHistorySupportedDC_Type(Bits):
    """Custom type cctmHistorySupportedDC based on Bits"""
    namedValues = NamedValues(
        *(("mnp5", 0),
          ("v42bisRx", 1),
          ("v42bisTx", 2),
          ("v44Rx", 3),
          ("v44Tx", 4))
    )

_CctmHistorySupportedDC_Type.__name__ = "Bits"
_CctmHistorySupportedDC_Object = MibTableColumn
cctmHistorySupportedDC = _CctmHistorySupportedDC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 10),
    _CctmHistorySupportedDC_Type()
)
cctmHistorySupportedDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistorySupportedDC.setStatus("current")
_CctmHistoryDataCompression_Type = CctmDataCompression
_CctmHistoryDataCompression_Object = MibTableColumn
cctmHistoryDataCompression = _CctmHistoryDataCompression_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 11),
    _CctmHistoryDataCompression_Type()
)
cctmHistoryDataCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryDataCompression.setStatus("current")
_CctmHistoryRxHighWatermark_Type = Gauge32
_CctmHistoryRxHighWatermark_Object = MibTableColumn
cctmHistoryRxHighWatermark = _CctmHistoryRxHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 12),
    _CctmHistoryRxHighWatermark_Type()
)
cctmHistoryRxHighWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRxHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryRxHighWatermark.setUnits("bits per second")
_CctmHistoryRxLowWatermark_Type = Gauge32
_CctmHistoryRxLowWatermark_Object = MibTableColumn
cctmHistoryRxLowWatermark = _CctmHistoryRxLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 13),
    _CctmHistoryRxLowWatermark_Type()
)
cctmHistoryRxLowWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRxLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryRxLowWatermark.setUnits("bits per second")
_CctmHistoryTxHighWatermark_Type = Gauge32
_CctmHistoryTxHighWatermark_Object = MibTableColumn
cctmHistoryTxHighWatermark = _CctmHistoryTxHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 14),
    _CctmHistoryTxHighWatermark_Type()
)
cctmHistoryTxHighWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryTxHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryTxHighWatermark.setUnits("bits per second")
_CctmHistoryTxLowWatermark_Type = Gauge32
_CctmHistoryTxLowWatermark_Object = MibTableColumn
cctmHistoryTxLowWatermark = _CctmHistoryTxLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 15),
    _CctmHistoryTxLowWatermark_Type()
)
cctmHistoryTxLowWatermark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryTxLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    cctmHistoryTxLowWatermark.setUnits("bits per second")
_CctmHistoryLocalUpRateShifts_Type = Counter32
_CctmHistoryLocalUpRateShifts_Object = MibTableColumn
cctmHistoryLocalUpRateShifts = _CctmHistoryLocalUpRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 16),
    _CctmHistoryLocalUpRateShifts_Type()
)
cctmHistoryLocalUpRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryLocalUpRateShifts.setStatus("current")
_CctmHistoryLocalDownRateShifts_Type = Counter32
_CctmHistoryLocalDownRateShifts_Object = MibTableColumn
cctmHistoryLocalDownRateShifts = _CctmHistoryLocalDownRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 17),
    _CctmHistoryLocalDownRateShifts_Type()
)
cctmHistoryLocalDownRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryLocalDownRateShifts.setStatus("current")
_CctmHistoryRemoteUpRateShifts_Type = Counter32
_CctmHistoryRemoteUpRateShifts_Object = MibTableColumn
cctmHistoryRemoteUpRateShifts = _CctmHistoryRemoteUpRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 18),
    _CctmHistoryRemoteUpRateShifts_Type()
)
cctmHistoryRemoteUpRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRemoteUpRateShifts.setStatus("current")
_CctmHistoryRemoteDownRateShifts_Type = Counter32
_CctmHistoryRemoteDownRateShifts_Object = MibTableColumn
cctmHistoryRemoteDownRateShifts = _CctmHistoryRemoteDownRateShifts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 19),
    _CctmHistoryRemoteDownRateShifts_Type()
)
cctmHistoryRemoteDownRateShifts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRemoteDownRateShifts.setStatus("current")
_CctmHistoryRateShiftFailures_Type = Counter32
_CctmHistoryRateShiftFailures_Object = MibTableColumn
cctmHistoryRateShiftFailures = _CctmHistoryRateShiftFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 20),
    _CctmHistoryRateShiftFailures_Type()
)
cctmHistoryRateShiftFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRateShiftFailures.setStatus("current")
_CctmHistoryLocalRetrains_Type = Counter32
_CctmHistoryLocalRetrains_Object = MibTableColumn
cctmHistoryLocalRetrains = _CctmHistoryLocalRetrains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 21),
    _CctmHistoryLocalRetrains_Type()
)
cctmHistoryLocalRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryLocalRetrains.setStatus("current")
_CctmHistoryRemoteRetrains_Type = Counter32
_CctmHistoryRemoteRetrains_Object = MibTableColumn
cctmHistoryRemoteRetrains = _CctmHistoryRemoteRetrains_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 22),
    _CctmHistoryRemoteRetrains_Type()
)
cctmHistoryRemoteRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRemoteRetrains.setStatus("current")
_CctmHistoryRetrainFailures_Type = Counter32
_CctmHistoryRetrainFailures_Object = MibTableColumn
cctmHistoryRetrainFailures = _CctmHistoryRetrainFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 23),
    _CctmHistoryRetrainFailures_Type()
)
cctmHistoryRetrainFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRetrainFailures.setStatus("current")
_CctmHistoryRxLinkOctets_Type = Counter32
_CctmHistoryRxLinkOctets_Object = MibTableColumn
cctmHistoryRxLinkOctets = _CctmHistoryRxLinkOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 24),
    _CctmHistoryRxLinkOctets_Type()
)
cctmHistoryRxLinkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRxLinkOctets.setStatus("current")
_CctmHistoryTxLinkOctets_Type = Counter32
_CctmHistoryTxLinkOctets_Object = MibTableColumn
cctmHistoryTxLinkOctets = _CctmHistoryTxLinkOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 25),
    _CctmHistoryTxLinkOctets_Type()
)
cctmHistoryTxLinkOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryTxLinkOctets.setStatus("current")
_CctmHistoryRxECFrames_Type = Counter32
_CctmHistoryRxECFrames_Object = MibTableColumn
cctmHistoryRxECFrames = _CctmHistoryRxECFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 26),
    _CctmHistoryRxECFrames_Type()
)
cctmHistoryRxECFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRxECFrames.setStatus("current")
_CctmHistoryTxECFrames_Type = Counter32
_CctmHistoryTxECFrames_Object = MibTableColumn
cctmHistoryTxECFrames = _CctmHistoryTxECFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 27),
    _CctmHistoryTxECFrames_Type()
)
cctmHistoryTxECFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryTxECFrames.setStatus("current")
_CctmHistoryRxECNAKs_Type = Counter32
_CctmHistoryRxECNAKs_Object = MibTableColumn
cctmHistoryRxECNAKs = _CctmHistoryRxECNAKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 28),
    _CctmHistoryRxECNAKs_Type()
)
cctmHistoryRxECNAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRxECNAKs.setStatus("current")
_CctmHistoryTxECNAKs_Type = Counter32
_CctmHistoryTxECNAKs_Object = MibTableColumn
cctmHistoryTxECNAKs = _CctmHistoryTxECNAKs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 29),
    _CctmHistoryTxECNAKs_Type()
)
cctmHistoryTxECNAKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryTxECNAKs.setStatus("current")
_CctmHistoryRxECFramesBad_Type = Counter32
_CctmHistoryRxECFramesBad_Object = MibTableColumn
cctmHistoryRxECFramesBad = _CctmHistoryRxECFramesBad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 30),
    _CctmHistoryRxECFramesBad_Type()
)
cctmHistoryRxECFramesBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRxECFramesBad.setStatus("current")
_CctmHistoryECFramesResent_Type = Counter32
_CctmHistoryECFramesResent_Object = MibTableColumn
cctmHistoryECFramesResent = _CctmHistoryECFramesResent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 31),
    _CctmHistoryECFramesResent_Type()
)
cctmHistoryECFramesResent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryECFramesResent.setStatus("current")
_CctmHistoryECLinkTimeouts_Type = Counter32
_CctmHistoryECLinkTimeouts_Object = MibTableColumn
cctmHistoryECLinkTimeouts = _CctmHistoryECLinkTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 32),
    _CctmHistoryECLinkTimeouts_Type()
)
cctmHistoryECLinkTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryECLinkTimeouts.setStatus("current")
_CctmHistoryRxCharLost_Type = Counter32
_CctmHistoryRxCharLost_Object = MibTableColumn
cctmHistoryRxCharLost = _CctmHistoryRxCharLost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 33),
    _CctmHistoryRxCharLost_Type()
)
cctmHistoryRxCharLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryRxCharLost.setStatus("current")
_CctmHistoryDisconnectReason_Type = Unsigned32
_CctmHistoryDisconnectReason_Object = MibTableColumn
cctmHistoryDisconnectReason = _CctmHistoryDisconnectReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 34),
    _CctmHistoryDisconnectReason_Type()
)
cctmHistoryDisconnectReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryDisconnectReason.setStatus("current")


class _CctmHistoryDisconnectReasonText_Type(DisplayString):
    """Custom type cctmHistoryDisconnectReasonText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CctmHistoryDisconnectReasonText_Type.__name__ = "DisplayString"
_CctmHistoryDisconnectReasonText_Object = MibTableColumn
cctmHistoryDisconnectReasonText = _CctmHistoryDisconnectReasonText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 1, 1, 35),
    _CctmHistoryDisconnectReasonText_Type()
)
cctmHistoryDisconnectReasonText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmHistoryDisconnectReasonText.setStatus("current")
_CctmXHistoryTable_Object = MibTable
cctmXHistoryTable = _CctmXHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cctmXHistoryTable.setStatus("current")
_CctmXHistoryEntry_Object = MibTableRow
cctmXHistoryEntry = _CctmXHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cctmXHistoryEntry.setStatus("current")
_CctmXHistoryRxECInfoFrameSize_Type = Unsigned32
_CctmXHistoryRxECInfoFrameSize_Object = MibTableColumn
cctmXHistoryRxECInfoFrameSize = _CctmXHistoryRxECInfoFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 1),
    _CctmXHistoryRxECInfoFrameSize_Type()
)
cctmXHistoryRxECInfoFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryRxECInfoFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    cctmXHistoryRxECInfoFrameSize.setUnits("octets")
_CctmXHistoryTxECInfoFrameSize_Type = Unsigned32
_CctmXHistoryTxECInfoFrameSize_Object = MibTableColumn
cctmXHistoryTxECInfoFrameSize = _CctmXHistoryTxECInfoFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 2),
    _CctmXHistoryTxECInfoFrameSize_Type()
)
cctmXHistoryTxECInfoFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryTxECInfoFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    cctmXHistoryTxECInfoFrameSize.setUnits("octets")
_CctmXHistoryRxECWindowSize_Type = Unsigned32
_CctmXHistoryRxECWindowSize_Object = MibTableColumn
cctmXHistoryRxECWindowSize = _CctmXHistoryRxECWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 3),
    _CctmXHistoryRxECWindowSize_Type()
)
cctmXHistoryRxECWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryRxECWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    cctmXHistoryRxECWindowSize.setUnits("frames")
_CctmXHistoryTxECWindowSize_Type = Unsigned32
_CctmXHistoryTxECWindowSize_Object = MibTableColumn
cctmXHistoryTxECWindowSize = _CctmXHistoryTxECWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 4),
    _CctmXHistoryTxECWindowSize_Type()
)
cctmXHistoryTxECWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryTxECWindowSize.setStatus("current")
if mibBuilder.loadTexts:
    cctmXHistoryTxECWindowSize.setUnits("frames")


class _CctmXHistoryRxLevel_Type(Integer32):
    """Custom type cctmXHistoryRxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 0),
    )


_CctmXHistoryRxLevel_Type.__name__ = "Integer32"
_CctmXHistoryRxLevel_Object = MibTableColumn
cctmXHistoryRxLevel = _CctmXHistoryRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 5),
    _CctmXHistoryRxLevel_Type()
)
cctmXHistoryRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryRxLevel.setStatus("current")
if mibBuilder.loadTexts:
    cctmXHistoryRxLevel.setUnits("dB")


class _CctmXHistoryTxLevel_Type(Integer32):
    """Custom type cctmXHistoryTxLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 0),
    )


_CctmXHistoryTxLevel_Type.__name__ = "Integer32"
_CctmXHistoryTxLevel_Object = MibTableColumn
cctmXHistoryTxLevel = _CctmXHistoryTxLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 6),
    _CctmXHistoryTxLevel_Type()
)
cctmXHistoryTxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryTxLevel.setStatus("current")
if mibBuilder.loadTexts:
    cctmXHistoryTxLevel.setUnits("dB")


class _CctmXHistoryConstellation_Type(Integer32):
    """Custom type cctmXHistoryConstellation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("points16", 2),
          ("points4", 1))
    )


_CctmXHistoryConstellation_Type.__name__ = "Integer32"
_CctmXHistoryConstellation_Object = MibTableColumn
cctmXHistoryConstellation = _CctmXHistoryConstellation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 7),
    _CctmXHistoryConstellation_Type()
)
cctmXHistoryConstellation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryConstellation.setStatus("current")


class _CctmXHistoryV90Status_Type(Integer32):
    """Custom type cctmXHistoryV90Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("notAttempted", 1),
          ("success", 3))
    )


_CctmXHistoryV90Status_Type.__name__ = "Integer32"
_CctmXHistoryV90Status_Object = MibTableColumn
cctmXHistoryV90Status = _CctmXHistoryV90Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 8),
    _CctmXHistoryV90Status_Type()
)
cctmXHistoryV90Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryV90Status.setStatus("current")


class _CctmXHistoryV90Failure_Type(Integer32):
    """Custom type cctmXHistoryV90Failure based on Integer32"""
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
        *(("clientFallback", 3),
          ("clientNonPCM", 2),
          ("noFailure", 1),
          ("serverV90Disabled", 4))
    )


_CctmXHistoryV90Failure_Type.__name__ = "Integer32"
_CctmXHistoryV90Failure_Object = MibTableColumn
cctmXHistoryV90Failure = _CctmXHistoryV90Failure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 9),
    _CctmXHistoryV90Failure_Type()
)
cctmXHistoryV90Failure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryV90Failure.setStatus("current")


class _CctmXHistoryV90ClientId_Type(Unsigned32):
    """Custom type cctmXHistoryV90ClientId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CctmXHistoryV90ClientId_Type.__name__ = "Unsigned32"
_CctmXHistoryV90ClientId_Object = MibTableColumn
cctmXHistoryV90ClientId = _CctmXHistoryV90ClientId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 10),
    _CctmXHistoryV90ClientId_Type()
)
cctmXHistoryV90ClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryV90ClientId.setStatus("current")
_CctmXHistoryECWindowClosures_Type = Counter32
_CctmXHistoryECWindowClosures_Object = MibTableColumn
cctmXHistoryECWindowClosures = _CctmXHistoryECWindowClosures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 1, 2, 2, 1, 11),
    _CctmXHistoryECWindowClosures_Type()
)
cctmXHistoryECWindowClosures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cctmXHistoryECWindowClosures.setStatus("current")
_CctmMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cctmMIBNotificationPrefix = _CctmMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 2)
)
_CctmMIBNotifications_ObjectIdentity = ObjectIdentity
cctmMIBNotifications = _CctmMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 2, 0)
)
_CctmMIBConformance_ObjectIdentity = ObjectIdentity
cctmMIBConformance = _CctmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 3)
)
_CctmMIBCompliances_ObjectIdentity = ObjectIdentity
cctmMIBCompliances = _CctmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 3, 1)
)
_CctmMIBGroups_ObjectIdentity = ObjectIdentity
cctmMIBGroups = _CctmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 3, 2)
)
cctmHistoryEntry.registerAugmentions(
    ("CISCO-CALL-TRACKER-MODEM-MIB",
     "cctmXHistoryEntry")
)
cctmXHistoryEntry.setIndexNames(*cctmHistoryEntry.getIndexNames())

# Managed Objects groups

cctmActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 3, 2, 2)
)
cctmActiveGroup.setObjects(
      *(("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveProjectedMaxRxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveProjectedMaxTxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveTxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveAttemptedModulation"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveInitialModulation"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveModulation"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveAttemptedECProtocol"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveECProtocol"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveSupportedDC"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveDataCompression"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxHighWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxLowWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveTxHighWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveTxLowWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveLocalUpRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRemoteUpRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveLocalDownRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRemoteDownRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRateShiftFailures"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveLocalRetrains"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRemoteRetrains"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRetrainFailures"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxLinkOctets"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveTxLinkOctets"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxECFrames"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveTxECFrames"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxECNAKs"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveTxECNAKs"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxECFramesBad"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveECFramesResent"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveECLinkTimeouts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmActiveRxCharLost"))
)
if mibBuilder.loadTexts:
    cctmActiveGroup.setStatus("current")

cctmHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 3, 2, 3)
)
cctmHistoryGroup.setObjects(
      *(("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryProjectedMaxRxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryProjectedMaxTxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryFinalRxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryFinalTxRate"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryAttemptedModulation"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryInitialModulation"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryFinalModulation"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryAttemptedECProtocol"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryECProtocol"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistorySupportedDC"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryDataCompression"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRxHighWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRxLowWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryTxHighWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryTxLowWatermark"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryLocalUpRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRemoteUpRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryLocalDownRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRemoteDownRateShifts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRateShiftFailures"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryLocalRetrains"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRemoteRetrains"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRetrainFailures"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRxLinkOctets"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryTxLinkOctets"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRxECFrames"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryTxECFrames"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRxECNAKs"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryTxECNAKs"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRxECFramesBad"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryECFramesResent"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryECLinkTimeouts"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryRxCharLost"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryDisconnectReason"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmHistoryDisconnectReasonText"))
)
if mibBuilder.loadTexts:
    cctmHistoryGroup.setStatus("current")

cctmXHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 3, 2, 4)
)
cctmXHistoryGroup.setObjects(
      *(("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryRxECInfoFrameSize"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryTxECInfoFrameSize"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryRxECWindowSize"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryTxECWindowSize"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryRxLevel"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryTxLevel"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryConstellation"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryV90Status"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryV90Failure"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryV90ClientId"),
        ("CISCO-CALL-TRACKER-MODEM-MIB", "cctmXHistoryECWindowClosures"))
)
if mibBuilder.loadTexts:
    cctmXHistoryGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cctmMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 165, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cctmMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CALL-TRACKER-MODEM-MIB",
    **{"CctmModulation": CctmModulation,
       "CctmECProtocol": CctmECProtocol,
       "CctmDataCompression": CctmDataCompression,
       "ciscoCallTrackerModemMIB": ciscoCallTrackerModemMIB,
       "cctmMIBObjects": cctmMIBObjects,
       "cctmActive": cctmActive,
       "cctmActiveTable": cctmActiveTable,
       "cctmActiveEntry": cctmActiveEntry,
       "cctmActiveProjectedMaxRxRate": cctmActiveProjectedMaxRxRate,
       "cctmActiveProjectedMaxTxRate": cctmActiveProjectedMaxTxRate,
       "cctmActiveRxRate": cctmActiveRxRate,
       "cctmActiveTxRate": cctmActiveTxRate,
       "cctmActiveAttemptedModulation": cctmActiveAttemptedModulation,
       "cctmActiveInitialModulation": cctmActiveInitialModulation,
       "cctmActiveModulation": cctmActiveModulation,
       "cctmActiveAttemptedECProtocol": cctmActiveAttemptedECProtocol,
       "cctmActiveECProtocol": cctmActiveECProtocol,
       "cctmActiveSupportedDC": cctmActiveSupportedDC,
       "cctmActiveDataCompression": cctmActiveDataCompression,
       "cctmActiveRxHighWatermark": cctmActiveRxHighWatermark,
       "cctmActiveRxLowWatermark": cctmActiveRxLowWatermark,
       "cctmActiveTxHighWatermark": cctmActiveTxHighWatermark,
       "cctmActiveTxLowWatermark": cctmActiveTxLowWatermark,
       "cctmActiveLocalUpRateShifts": cctmActiveLocalUpRateShifts,
       "cctmActiveLocalDownRateShifts": cctmActiveLocalDownRateShifts,
       "cctmActiveRemoteUpRateShifts": cctmActiveRemoteUpRateShifts,
       "cctmActiveRemoteDownRateShifts": cctmActiveRemoteDownRateShifts,
       "cctmActiveRateShiftFailures": cctmActiveRateShiftFailures,
       "cctmActiveLocalRetrains": cctmActiveLocalRetrains,
       "cctmActiveRemoteRetrains": cctmActiveRemoteRetrains,
       "cctmActiveRetrainFailures": cctmActiveRetrainFailures,
       "cctmActiveRxLinkOctets": cctmActiveRxLinkOctets,
       "cctmActiveTxLinkOctets": cctmActiveTxLinkOctets,
       "cctmActiveRxECFrames": cctmActiveRxECFrames,
       "cctmActiveTxECFrames": cctmActiveTxECFrames,
       "cctmActiveRxECNAKs": cctmActiveRxECNAKs,
       "cctmActiveTxECNAKs": cctmActiveTxECNAKs,
       "cctmActiveRxECFramesBad": cctmActiveRxECFramesBad,
       "cctmActiveECFramesResent": cctmActiveECFramesResent,
       "cctmActiveECLinkTimeouts": cctmActiveECLinkTimeouts,
       "cctmActiveRxCharLost": cctmActiveRxCharLost,
       "cctmHistory": cctmHistory,
       "cctmHistoryTable": cctmHistoryTable,
       "cctmHistoryEntry": cctmHistoryEntry,
       "cctmHistoryProjectedMaxRxRate": cctmHistoryProjectedMaxRxRate,
       "cctmHistoryProjectedMaxTxRate": cctmHistoryProjectedMaxTxRate,
       "cctmHistoryFinalRxRate": cctmHistoryFinalRxRate,
       "cctmHistoryFinalTxRate": cctmHistoryFinalTxRate,
       "cctmHistoryAttemptedModulation": cctmHistoryAttemptedModulation,
       "cctmHistoryInitialModulation": cctmHistoryInitialModulation,
       "cctmHistoryFinalModulation": cctmHistoryFinalModulation,
       "cctmHistoryAttemptedECProtocol": cctmHistoryAttemptedECProtocol,
       "cctmHistoryECProtocol": cctmHistoryECProtocol,
       "cctmHistorySupportedDC": cctmHistorySupportedDC,
       "cctmHistoryDataCompression": cctmHistoryDataCompression,
       "cctmHistoryRxHighWatermark": cctmHistoryRxHighWatermark,
       "cctmHistoryRxLowWatermark": cctmHistoryRxLowWatermark,
       "cctmHistoryTxHighWatermark": cctmHistoryTxHighWatermark,
       "cctmHistoryTxLowWatermark": cctmHistoryTxLowWatermark,
       "cctmHistoryLocalUpRateShifts": cctmHistoryLocalUpRateShifts,
       "cctmHistoryLocalDownRateShifts": cctmHistoryLocalDownRateShifts,
       "cctmHistoryRemoteUpRateShifts": cctmHistoryRemoteUpRateShifts,
       "cctmHistoryRemoteDownRateShifts": cctmHistoryRemoteDownRateShifts,
       "cctmHistoryRateShiftFailures": cctmHistoryRateShiftFailures,
       "cctmHistoryLocalRetrains": cctmHistoryLocalRetrains,
       "cctmHistoryRemoteRetrains": cctmHistoryRemoteRetrains,
       "cctmHistoryRetrainFailures": cctmHistoryRetrainFailures,
       "cctmHistoryRxLinkOctets": cctmHistoryRxLinkOctets,
       "cctmHistoryTxLinkOctets": cctmHistoryTxLinkOctets,
       "cctmHistoryRxECFrames": cctmHistoryRxECFrames,
       "cctmHistoryTxECFrames": cctmHistoryTxECFrames,
       "cctmHistoryRxECNAKs": cctmHistoryRxECNAKs,
       "cctmHistoryTxECNAKs": cctmHistoryTxECNAKs,
       "cctmHistoryRxECFramesBad": cctmHistoryRxECFramesBad,
       "cctmHistoryECFramesResent": cctmHistoryECFramesResent,
       "cctmHistoryECLinkTimeouts": cctmHistoryECLinkTimeouts,
       "cctmHistoryRxCharLost": cctmHistoryRxCharLost,
       "cctmHistoryDisconnectReason": cctmHistoryDisconnectReason,
       "cctmHistoryDisconnectReasonText": cctmHistoryDisconnectReasonText,
       "cctmXHistoryTable": cctmXHistoryTable,
       "cctmXHistoryEntry": cctmXHistoryEntry,
       "cctmXHistoryRxECInfoFrameSize": cctmXHistoryRxECInfoFrameSize,
       "cctmXHistoryTxECInfoFrameSize": cctmXHistoryTxECInfoFrameSize,
       "cctmXHistoryRxECWindowSize": cctmXHistoryRxECWindowSize,
       "cctmXHistoryTxECWindowSize": cctmXHistoryTxECWindowSize,
       "cctmXHistoryRxLevel": cctmXHistoryRxLevel,
       "cctmXHistoryTxLevel": cctmXHistoryTxLevel,
       "cctmXHistoryConstellation": cctmXHistoryConstellation,
       "cctmXHistoryV90Status": cctmXHistoryV90Status,
       "cctmXHistoryV90Failure": cctmXHistoryV90Failure,
       "cctmXHistoryV90ClientId": cctmXHistoryV90ClientId,
       "cctmXHistoryECWindowClosures": cctmXHistoryECWindowClosures,
       "cctmMIBNotificationPrefix": cctmMIBNotificationPrefix,
       "cctmMIBNotifications": cctmMIBNotifications,
       "cctmMIBConformance": cctmMIBConformance,
       "cctmMIBCompliances": cctmMIBCompliances,
       "cctmMIBCompliance": cctmMIBCompliance,
       "cctmMIBGroups": cctmMIBGroups,
       "cctmActiveGroup": cctmActiveGroup,
       "cctmHistoryGroup": cctmHistoryGroup,
       "cctmXHistoryGroup": cctmXHistoryGroup}
)
