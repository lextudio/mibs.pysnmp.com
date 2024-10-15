# SNMP MIB module (CISCO-METRO-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-METRO-PHY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:27 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMetroPhyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69)
)
ciscoMetroPhyMIB.setRevisions(
        ("2005-09-02 00:00",
         "2004-11-19 00:00",
         "2003-08-25 00:00",
         "2003-01-08 00:00",
         "2002-05-14 00:00",
         "2001-08-31 00:00",
         "2001-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TransmissionType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("optical", 3),
          ("unknown", 1))
    )



class ProtocolType(Integer32, TextualConvention):
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("dvb", 20),
          ("e1", 16),
          ("e3", 18),
          ("escon", 7),
          ("fastEthernet", 14),
          ("fddi", 15),
          ("fibreChannel", 5),
          ("ficon", 6),
          ("gigabitEthernet", 3),
          ("its", 22),
          ("other", 1),
          ("sdh", 9),
          ("sdi", 21),
          ("sonet", 8),
          ("sysplexIscCompatibility", 10),
          ("sysplexIscPeer", 11),
          ("sysplexTimerClo", 13),
          ("sysplexTimerEtr", 12),
          ("t1", 17),
          ("t3", 19),
          ("tenGigabitEthernet", 4),
          ("unknown", 2))
    )



class TriValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notApplicable", 3),
          ("true", 1))
    )



class CmRateType(Integer32, TextualConvention):
    status = "current"
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
        *(("auto", 2),
          ("fourGbps", 5),
          ("oneGbps", 3),
          ("tenGbps", 6),
          ("twoGbps", 4),
          ("unknown", 1))
    )



class CmNegotiatedRateType(Integer32, TextualConvention):
    status = "current"
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
        *(("fourGbps", 5),
          ("negotiating", 2),
          ("notApplicable", 1),
          ("oneGbps", 3),
          ("tenGbps", 6),
          ("twoGbps", 4))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMetroPhyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMetroPhyMIBObjects = _CiscoMetroPhyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1)
)
_CmPhyIf_ObjectIdentity = ObjectIdentity
cmPhyIf = _CmPhyIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1)
)
_CmPhyIfTable_Object = MibTable
cmPhyIfTable = _CmPhyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmPhyIfTable.setStatus("current")
_CmPhyIfEntry_Object = MibTableRow
cmPhyIfEntry = _CmPhyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1)
)
cmPhyIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmPhyIfEntry.setStatus("current")


class _CmPhyIfMode_Type(Integer32):
    """Custom type cmPhyIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mode2R", 1),
          ("mode3R", 2))
    )


_CmPhyIfMode_Type.__name__ = "Integer32"
_CmPhyIfMode_Object = MibTableColumn
cmPhyIfMode = _CmPhyIfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 1),
    _CmPhyIfMode_Type()
)
cmPhyIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfMode.setStatus("current")
_CmPhyIfProtocol_Type = ProtocolType
_CmPhyIfProtocol_Object = MibTableColumn
cmPhyIfProtocol = _CmPhyIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 2),
    _CmPhyIfProtocol_Type()
)
cmPhyIfProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfProtocol.setStatus("current")


class _CmPhyIfClockRate_Type(Integer32):
    """Custom type cmPhyIfClockRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10312000),
    )


_CmPhyIfClockRate_Type.__name__ = "Integer32"
_CmPhyIfClockRate_Object = MibTableColumn
cmPhyIfClockRate = _CmPhyIfClockRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 3),
    _CmPhyIfClockRate_Type()
)
cmPhyIfClockRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfClockRate.setStatus("current")
if mibBuilder.loadTexts:
    cmPhyIfClockRate.setUnits("kHz")
_CmPhyIfMonitor_Type = TruthValue
_CmPhyIfMonitor_Object = MibTableColumn
cmPhyIfMonitor = _CmPhyIfMonitor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 4),
    _CmPhyIfMonitor_Type()
)
cmPhyIfMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfMonitor.setStatus("current")


class _CmPhyIfLoopback_Type(Integer32):
    """Custom type cmPhyIfLoopback based on Integer32"""
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
        *(("diagnosticLoop", 2),
          ("lineLoop", 3),
          ("noLoop", 1),
          ("otherLoop", 4))
    )


_CmPhyIfLoopback_Type.__name__ = "Integer32"
_CmPhyIfLoopback_Object = MibTableColumn
cmPhyIfLoopback = _CmPhyIfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 5),
    _CmPhyIfLoopback_Type()
)
cmPhyIfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfLoopback.setStatus("current")
_CmPhyIfOFC_Type = TruthValue
_CmPhyIfOFC_Object = MibTableColumn
cmPhyIfOFC = _CmPhyIfOFC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 6),
    _CmPhyIfOFC_Type()
)
cmPhyIfOFC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfOFC.setStatus("current")
_CmPhyIfLaserSafetyControl_Type = TruthValue
_CmPhyIfLaserSafetyControl_Object = MibTableColumn
cmPhyIfLaserSafetyControl = _CmPhyIfLaserSafetyControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 7),
    _CmPhyIfLaserSafetyControl_Type()
)
cmPhyIfLaserSafetyControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfLaserSafetyControl.setStatus("deprecated")
_CmPhyIfForwardLaserControl_Type = TruthValue
_CmPhyIfForwardLaserControl_Object = MibTableColumn
cmPhyIfForwardLaserControl = _CmPhyIfForwardLaserControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 8),
    _CmPhyIfForwardLaserControl_Type()
)
cmPhyIfForwardLaserControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfForwardLaserControl.setStatus("deprecated")


class _CmPhyIfTxBufferSize_Type(Unsigned32):
    """Custom type cmPhyIfTxBufferSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_CmPhyIfTxBufferSize_Type.__name__ = "Unsigned32"
_CmPhyIfTxBufferSize_Object = MibTableColumn
cmPhyIfTxBufferSize = _CmPhyIfTxBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 9),
    _CmPhyIfTxBufferSize_Type()
)
cmPhyIfTxBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfTxBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cmPhyIfTxBufferSize.setUnits("bytes")
_CmPhyIfAutoNegotiation_Type = TriValue
_CmPhyIfAutoNegotiation_Object = MibTableColumn
cmPhyIfAutoNegotiation = _CmPhyIfAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 10),
    _CmPhyIfAutoNegotiation_Type()
)
cmPhyIfAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfAutoNegotiation.setStatus("current")
_CmPhyIfTransType_Type = TransmissionType
_CmPhyIfTransType_Object = MibTableColumn
cmPhyIfTransType = _CmPhyIfTransType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 11),
    _CmPhyIfTransType_Type()
)
cmPhyIfTransType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyIfTransType.setStatus("current")
_CmPhyIfRate_Type = CmRateType
_CmPhyIfRate_Object = MibTableColumn
cmPhyIfRate = _CmPhyIfRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 12),
    _CmPhyIfRate_Type()
)
cmPhyIfRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfRate.setStatus("current")
_CmPhyIfNegotiatedRate_Type = CmNegotiatedRateType
_CmPhyIfNegotiatedRate_Object = MibTableColumn
cmPhyIfNegotiatedRate = _CmPhyIfNegotiatedRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 13),
    _CmPhyIfNegotiatedRate_Type()
)
cmPhyIfNegotiatedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyIfNegotiatedRate.setStatus("current")


class _CmPhyIfOverSubscription_Type(TriValue):
    """Custom type cmPhyIfOverSubscription based on TriValue"""


_CmPhyIfOverSubscription_Object = MibTableColumn
cmPhyIfOverSubscription = _CmPhyIfOverSubscription_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 14),
    _CmPhyIfOverSubscription_Type()
)
cmPhyIfOverSubscription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfOverSubscription.setStatus("current")


class _CmPhyIfClientSubrate_Type(Unsigned32):
    """Custom type cmPhyIfClientSubrate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4240),
    )


_CmPhyIfClientSubrate_Type.__name__ = "Unsigned32"
_CmPhyIfClientSubrate_Object = MibTableColumn
cmPhyIfClientSubrate = _CmPhyIfClientSubrate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 15),
    _CmPhyIfClientSubrate_Type()
)
cmPhyIfClientSubrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfClientSubrate.setStatus("current")
if mibBuilder.loadTexts:
    cmPhyIfClientSubrate.setUnits("mega-bytes-per-second")


class _CmPhyIfClientSubrateLock_Type(TruthValue):
    """Custom type cmPhyIfClientSubrateLock based on TruthValue"""


_CmPhyIfClientSubrateLock_Object = MibTableColumn
cmPhyIfClientSubrateLock = _CmPhyIfClientSubrateLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 1, 1, 1, 16),
    _CmPhyIfClientSubrateLock_Type()
)
cmPhyIfClientSubrateLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhyIfClientSubrateLock.setStatus("current")
_CmPhyStatistics_ObjectIdentity = ObjectIdentity
cmPhyStatistics = _CmPhyStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2)
)
_CmPhyStatisticsTable_Object = MibTable
cmPhyStatisticsTable = _CmPhyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cmPhyStatisticsTable.setStatus("current")
_CmPhyStatisticsEntry_Object = MibTableRow
cmPhyStatisticsEntry = _CmPhyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1)
)
cmPhyStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmPhyStatisticsEntry.setStatus("current")


class _CmPhyRxPower_Type(Integer32):
    """Custom type cmPhyRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4000, 0),
    )


_CmPhyRxPower_Type.__name__ = "Integer32"
_CmPhyRxPower_Object = MibTableColumn
cmPhyRxPower = _CmPhyRxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 1),
    _CmPhyRxPower_Type()
)
cmPhyRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyRxPower.setStatus("deprecated")
if mibBuilder.loadTexts:
    cmPhyRxPower.setUnits("dBm")
_CmPhyRxCVRD_Type = Counter32
_CmPhyRxCVRD_Object = MibTableColumn
cmPhyRxCVRD = _CmPhyRxCVRD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 2),
    _CmPhyRxCVRD_Type()
)
cmPhyRxCVRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyRxCVRD.setStatus("current")
_CmPhyRxCVRDOverflow_Type = Counter32
_CmPhyRxCVRDOverflow_Object = MibTableColumn
cmPhyRxCVRDOverflow = _CmPhyRxCVRDOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 3),
    _CmPhyRxCVRDOverflow_Type()
)
cmPhyRxCVRDOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyRxCVRDOverflow.setStatus("current")
_CmPhyHCRxCVRD_Type = Counter64
_CmPhyHCRxCVRD_Object = MibTableColumn
cmPhyHCRxCVRD = _CmPhyHCRxCVRD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 4),
    _CmPhyHCRxCVRD_Type()
)
cmPhyHCRxCVRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyHCRxCVRD.setStatus("current")
_CmPhyRxHEC_Type = Counter32
_CmPhyRxHEC_Object = MibTableColumn
cmPhyRxHEC = _CmPhyRxHEC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 5),
    _CmPhyRxHEC_Type()
)
cmPhyRxHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyRxHEC.setStatus("deprecated")
_CmPhyRxHECOverflow_Type = Counter32
_CmPhyRxHECOverflow_Object = MibTableColumn
cmPhyRxHECOverflow = _CmPhyRxHECOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 6),
    _CmPhyRxHECOverflow_Type()
)
cmPhyRxHECOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyRxHECOverflow.setStatus("deprecated")
_CmPhyHCRxHEC_Type = Counter64
_CmPhyHCRxHEC_Object = MibTableColumn
cmPhyHCRxHEC = _CmPhyHCRxHEC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 7),
    _CmPhyHCRxHEC_Type()
)
cmPhyHCRxHEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyHCRxHEC.setStatus("deprecated")
_CmPhyRxCRC_Type = Counter32
_CmPhyRxCRC_Object = MibTableColumn
cmPhyRxCRC = _CmPhyRxCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 8),
    _CmPhyRxCRC_Type()
)
cmPhyRxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyRxCRC.setStatus("current")
_CmPhyRxCRCOverflow_Type = Counter32
_CmPhyRxCRCOverflow_Object = MibTableColumn
cmPhyRxCRCOverflow = _CmPhyRxCRCOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 9),
    _CmPhyRxCRCOverflow_Type()
)
cmPhyRxCRCOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyRxCRCOverflow.setStatus("current")
_CmPhyHCRxCRC_Type = Counter64
_CmPhyHCRxCRC_Object = MibTableColumn
cmPhyHCRxCRC = _CmPhyHCRxCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 10),
    _CmPhyHCRxCRC_Type()
)
cmPhyHCRxCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyHCRxCRC.setStatus("current")
_CmPhyTxEncapFarEndPktErrors_Type = Counter32
_CmPhyTxEncapFarEndPktErrors_Object = MibTableColumn
cmPhyTxEncapFarEndPktErrors = _CmPhyTxEncapFarEndPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 11),
    _CmPhyTxEncapFarEndPktErrors_Type()
)
cmPhyTxEncapFarEndPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyTxEncapFarEndPktErrors.setStatus("current")
_CmPhyTxEncapFarEndPktErrOverflow_Type = Counter32
_CmPhyTxEncapFarEndPktErrOverflow_Object = MibTableColumn
cmPhyTxEncapFarEndPktErrOverflow = _CmPhyTxEncapFarEndPktErrOverflow_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 12),
    _CmPhyTxEncapFarEndPktErrOverflow_Type()
)
cmPhyTxEncapFarEndPktErrOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyTxEncapFarEndPktErrOverflow.setStatus("current")
_CmPhyHCTxEncapFarEndPktErrors_Type = Counter64
_CmPhyHCTxEncapFarEndPktErrors_Object = MibTableColumn
cmPhyHCTxEncapFarEndPktErrors = _CmPhyHCTxEncapFarEndPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 2, 1, 1, 13),
    _CmPhyHCTxEncapFarEndPktErrors_Type()
)
cmPhyHCTxEncapFarEndPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhyHCTxEncapFarEndPktErrors.setStatus("current")
_CmPhySonetSectionTrace_ObjectIdentity = ObjectIdentity
cmPhySonetSectionTrace = _CmPhySonetSectionTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3)
)
_CmPhySonetSectionTraceTable_Object = MibTable
cmPhySonetSectionTraceTable = _CmPhySonetSectionTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cmPhySonetSectionTraceTable.setStatus("current")
_CmPhySonetSectionTraceEntry_Object = MibTableRow
cmPhySonetSectionTraceEntry = _CmPhySonetSectionTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1)
)
cmPhySonetSectionTraceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cmPhySonetSectionTraceEntry.setStatus("current")


class _CmPhySonetSectionTraceReceived_Type(OctetString):
    """Custom type cmPhySonetSectionTraceReceived based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CmPhySonetSectionTraceReceived_Type.__name__ = "OctetString"
_CmPhySonetSectionTraceReceived_Object = MibTableColumn
cmPhySonetSectionTraceReceived = _CmPhySonetSectionTraceReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1, 1),
    _CmPhySonetSectionTraceReceived_Type()
)
cmPhySonetSectionTraceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmPhySonetSectionTraceReceived.setStatus("current")


class _CmPhySonetSectionTraceExpected_Type(OctetString):
    """Custom type cmPhySonetSectionTraceExpected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(64, 64),
    )


_CmPhySonetSectionTraceExpected_Type.__name__ = "OctetString"
_CmPhySonetSectionTraceExpected_Object = MibTableColumn
cmPhySonetSectionTraceExpected = _CmPhySonetSectionTraceExpected_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 1, 3, 1, 1, 2),
    _CmPhySonetSectionTraceExpected_Type()
)
cmPhySonetSectionTraceExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmPhySonetSectionTraceExpected.setStatus("current")
_CiscoMetroPhyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoMetroPhyMIBConformance = _CiscoMetroPhyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3)
)
_CiscoMetroPhyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMetroPhyMIBCompliances = _CiscoMetroPhyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1)
)
_CiscoMetroPhyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMetroPhyMIBGroups = _CiscoMetroPhyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2)
)

# Managed Objects groups

cmPhyIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 1)
)
cmPhyIfGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyIfMode"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfProtocol"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfClockRate"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfMonitor"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfLoopback"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfOFC"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfLaserSafetyControl"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfForwardLaserControl"))
)
if mibBuilder.loadTexts:
    cmPhyIfGroup.setStatus("deprecated")

cmPhyStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 2)
)
cmPhyStatisticsGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyRxPower"),
        ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRD"),
        ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRDOverflow"),
        ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCVRD"),
        ("CISCO-METRO-PHY-MIB", "cmPhyRxHEC"),
        ("CISCO-METRO-PHY-MIB", "cmPhyRxHECOverflow"),
        ("CISCO-METRO-PHY-MIB", "cmPhyHCRxHEC"))
)
if mibBuilder.loadTexts:
    cmPhyStatisticsGroup.setStatus("deprecated")

cmPhySonetSectionTraceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 3)
)
cmPhySonetSectionTraceGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceReceived"),
        ("CISCO-METRO-PHY-MIB", "cmPhySonetSectionTraceExpected"))
)
if mibBuilder.loadTexts:
    cmPhySonetSectionTraceGroup.setStatus("current")

cmPhyIf2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 4)
)
cmPhyIf2Group.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyIfMode"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfProtocol"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfClockRate"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfMonitor"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfLoopback"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfOFC"))
)
if mibBuilder.loadTexts:
    cmPhyIf2Group.setStatus("current")

cmPhyCVRDErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 5)
)
cmPhyCVRDErrorsGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyRxCVRD"),
        ("CISCO-METRO-PHY-MIB", "cmPhyRxCVRDOverflow"),
        ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCVRD"))
)
if mibBuilder.loadTexts:
    cmPhyCVRDErrorsGroup.setStatus("current")

cmPhyCRCErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 6)
)
cmPhyCRCErrorsGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyRxCRC"),
        ("CISCO-METRO-PHY-MIB", "cmPhyRxCRCOverflow"),
        ("CISCO-METRO-PHY-MIB", "cmPhyHCRxCRC"))
)
if mibBuilder.loadTexts:
    cmPhyCRCErrorsGroup.setStatus("current")

cmPhyEncapFarEndPktErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 7)
)
cmPhyEncapFarEndPktErrorsGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyTxEncapFarEndPktErrors"),
        ("CISCO-METRO-PHY-MIB", "cmPhyTxEncapFarEndPktErrOverflow"),
        ("CISCO-METRO-PHY-MIB", "cmPhyHCTxEncapFarEndPktErrors"))
)
if mibBuilder.loadTexts:
    cmPhyEncapFarEndPktErrorsGroup.setStatus("current")

cmPhyIfTxBufferSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 8)
)
cmPhyIfTxBufferSizeGroup.setObjects(
    ("CISCO-METRO-PHY-MIB", "cmPhyIfTxBufferSize")
)
if mibBuilder.loadTexts:
    cmPhyIfTxBufferSizeGroup.setStatus("current")

cmPhyIfAutoNegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 9)
)
cmPhyIfAutoNegGroup.setObjects(
    ("CISCO-METRO-PHY-MIB", "cmPhyIfAutoNegotiation")
)
if mibBuilder.loadTexts:
    cmPhyIfAutoNegGroup.setStatus("current")

cmPhyIfGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 10)
)
cmPhyIfGroupSup1.setObjects(
    ("CISCO-METRO-PHY-MIB", "cmPhyIfTransType")
)
if mibBuilder.loadTexts:
    cmPhyIfGroupSup1.setStatus("current")

cmPhyIfRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 11)
)
cmPhyIfRateGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyIfRate"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfNegotiatedRate"))
)
if mibBuilder.loadTexts:
    cmPhyIfRateGroup.setStatus("current")

cmPhyIfClientOvsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 12)
)
cmPhyIfClientOvsGroup.setObjects(
    ("CISCO-METRO-PHY-MIB", "cmPhyIfOverSubscription")
)
if mibBuilder.loadTexts:
    cmPhyIfClientOvsGroup.setStatus("current")

cmPhyIfClientSubrateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 2, 13)
)
cmPhyIfClientSubrateGroup.setObjects(
      *(("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrate"),
        ("CISCO-METRO-PHY-MIB", "cmPhyIfClientSubrateLock"))
)
if mibBuilder.loadTexts:
    cmPhyIfClientSubrateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cmPhyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cmPhyMIBCompliance.setStatus(
        "deprecated"
    )

cmPhyMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cmPhyMIBCompliance2.setStatus(
        "deprecated"
    )

cmPhyMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cmPhyMIBCompliance3.setStatus(
        "deprecated"
    )

cmPhyMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cmPhyMIBComplianceRev4.setStatus(
        "deprecated"
    )

cmPhyMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cmPhyMIBComplianceRev5.setStatus(
        "deprecated"
    )

cmPhyMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 69, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cmPhyMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-METRO-PHY-MIB",
    **{"TransmissionType": TransmissionType,
       "ProtocolType": ProtocolType,
       "TriValue": TriValue,
       "CmRateType": CmRateType,
       "CmNegotiatedRateType": CmNegotiatedRateType,
       "ciscoMetroPhyMIB": ciscoMetroPhyMIB,
       "ciscoMetroPhyMIBObjects": ciscoMetroPhyMIBObjects,
       "cmPhyIf": cmPhyIf,
       "cmPhyIfTable": cmPhyIfTable,
       "cmPhyIfEntry": cmPhyIfEntry,
       "cmPhyIfMode": cmPhyIfMode,
       "cmPhyIfProtocol": cmPhyIfProtocol,
       "cmPhyIfClockRate": cmPhyIfClockRate,
       "cmPhyIfMonitor": cmPhyIfMonitor,
       "cmPhyIfLoopback": cmPhyIfLoopback,
       "cmPhyIfOFC": cmPhyIfOFC,
       "cmPhyIfLaserSafetyControl": cmPhyIfLaserSafetyControl,
       "cmPhyIfForwardLaserControl": cmPhyIfForwardLaserControl,
       "cmPhyIfTxBufferSize": cmPhyIfTxBufferSize,
       "cmPhyIfAutoNegotiation": cmPhyIfAutoNegotiation,
       "cmPhyIfTransType": cmPhyIfTransType,
       "cmPhyIfRate": cmPhyIfRate,
       "cmPhyIfNegotiatedRate": cmPhyIfNegotiatedRate,
       "cmPhyIfOverSubscription": cmPhyIfOverSubscription,
       "cmPhyIfClientSubrate": cmPhyIfClientSubrate,
       "cmPhyIfClientSubrateLock": cmPhyIfClientSubrateLock,
       "cmPhyStatistics": cmPhyStatistics,
       "cmPhyStatisticsTable": cmPhyStatisticsTable,
       "cmPhyStatisticsEntry": cmPhyStatisticsEntry,
       "cmPhyRxPower": cmPhyRxPower,
       "cmPhyRxCVRD": cmPhyRxCVRD,
       "cmPhyRxCVRDOverflow": cmPhyRxCVRDOverflow,
       "cmPhyHCRxCVRD": cmPhyHCRxCVRD,
       "cmPhyRxHEC": cmPhyRxHEC,
       "cmPhyRxHECOverflow": cmPhyRxHECOverflow,
       "cmPhyHCRxHEC": cmPhyHCRxHEC,
       "cmPhyRxCRC": cmPhyRxCRC,
       "cmPhyRxCRCOverflow": cmPhyRxCRCOverflow,
       "cmPhyHCRxCRC": cmPhyHCRxCRC,
       "cmPhyTxEncapFarEndPktErrors": cmPhyTxEncapFarEndPktErrors,
       "cmPhyTxEncapFarEndPktErrOverflow": cmPhyTxEncapFarEndPktErrOverflow,
       "cmPhyHCTxEncapFarEndPktErrors": cmPhyHCTxEncapFarEndPktErrors,
       "cmPhySonetSectionTrace": cmPhySonetSectionTrace,
       "cmPhySonetSectionTraceTable": cmPhySonetSectionTraceTable,
       "cmPhySonetSectionTraceEntry": cmPhySonetSectionTraceEntry,
       "cmPhySonetSectionTraceReceived": cmPhySonetSectionTraceReceived,
       "cmPhySonetSectionTraceExpected": cmPhySonetSectionTraceExpected,
       "ciscoMetroPhyMIBConformance": ciscoMetroPhyMIBConformance,
       "ciscoMetroPhyMIBCompliances": ciscoMetroPhyMIBCompliances,
       "cmPhyMIBCompliance": cmPhyMIBCompliance,
       "cmPhyMIBCompliance2": cmPhyMIBCompliance2,
       "cmPhyMIBCompliance3": cmPhyMIBCompliance3,
       "cmPhyMIBComplianceRev4": cmPhyMIBComplianceRev4,
       "cmPhyMIBComplianceRev5": cmPhyMIBComplianceRev5,
       "cmPhyMIBComplianceRev6": cmPhyMIBComplianceRev6,
       "ciscoMetroPhyMIBGroups": ciscoMetroPhyMIBGroups,
       "cmPhyIfGroup": cmPhyIfGroup,
       "cmPhyStatisticsGroup": cmPhyStatisticsGroup,
       "cmPhySonetSectionTraceGroup": cmPhySonetSectionTraceGroup,
       "cmPhyIf2Group": cmPhyIf2Group,
       "cmPhyCVRDErrorsGroup": cmPhyCVRDErrorsGroup,
       "cmPhyCRCErrorsGroup": cmPhyCRCErrorsGroup,
       "cmPhyEncapFarEndPktErrorsGroup": cmPhyEncapFarEndPktErrorsGroup,
       "cmPhyIfTxBufferSizeGroup": cmPhyIfTxBufferSizeGroup,
       "cmPhyIfAutoNegGroup": cmPhyIfAutoNegGroup,
       "cmPhyIfGroupSup1": cmPhyIfGroupSup1,
       "cmPhyIfRateGroup": cmPhyIfRateGroup,
       "cmPhyIfClientOvsGroup": cmPhyIfClientOvsGroup,
       "cmPhyIfClientSubrateGroup": cmPhyIfClientSubrateGroup}
)
