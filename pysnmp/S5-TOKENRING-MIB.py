# SNMP MIB module (S5-TOKENRING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-TOKENRING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:12 2024
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

(s5Tok,) = mibBuilder.importSymbols(
    "S5-ROOT-MIB",
    "s5Tok")

(SrcIndx,
 TimeIntervalHrd,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "SrcIndx",
    "TimeIntervalHrd",
    "TimeIntervalSec")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5TrCfg_ObjectIdentity = ObjectIdentity
s5TrCfg = _S5TrCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 1)
)
_S5TrStat_ObjectIdentity = ObjectIdentity
s5TrStat = _S5TrStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 2)
)
_S5TrRing_ObjectIdentity = ObjectIdentity
s5TrRing = _S5TrRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3)
)
_S5TrRingInfoTable_Object = MibTable
s5TrRingInfoTable = _S5TrRingInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1)
)
if mibBuilder.loadTexts:
    s5TrRingInfoTable.setStatus("mandatory")
_S5TrRingInfoEntry_Object = MibTableRow
s5TrRingInfoEntry = _S5TrRingInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1)
)
s5TrRingInfoEntry.setIndexNames(
    (0, "S5-TOKENRING-MIB", "s5TrRingInfoSrcIndx"),
)
if mibBuilder.loadTexts:
    s5TrRingInfoEntry.setStatus("mandatory")
_S5TrRingInfoSrcIndx_Type = SrcIndx
_S5TrRingInfoSrcIndx_Object = MibTableColumn
s5TrRingInfoSrcIndx = _S5TrRingInfoSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 1),
    _S5TrRingInfoSrcIndx_Type()
)
s5TrRingInfoSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoSrcIndx.setStatus("mandatory")


class _S5TrRingInfoRingNum_Type(Integer32):
    """Custom type s5TrRingInfoRingNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_S5TrRingInfoRingNum_Type.__name__ = "Integer32"
_S5TrRingInfoRingNum_Object = MibTableColumn
s5TrRingInfoRingNum = _S5TrRingInfoRingNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 2),
    _S5TrRingInfoRingNum_Type()
)
s5TrRingInfoRingNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoRingNum.setStatus("mandatory")


class _S5TrRingInfoStaTableOperSize_Type(Integer32):
    """Custom type s5TrRingInfoStaTableOperSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_S5TrRingInfoStaTableOperSize_Type.__name__ = "Integer32"
_S5TrRingInfoStaTableOperSize_Object = MibTableColumn
s5TrRingInfoStaTableOperSize = _S5TrRingInfoStaTableOperSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 3),
    _S5TrRingInfoStaTableOperSize_Type()
)
s5TrRingInfoStaTableOperSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoStaTableOperSize.setStatus("mandatory")


class _S5TrRingInfoActiveStations_Type(Integer32):
    """Custom type s5TrRingInfoActiveStations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_S5TrRingInfoActiveStations_Type.__name__ = "Integer32"
_S5TrRingInfoActiveStations_Object = MibTableColumn
s5TrRingInfoActiveStations = _S5TrRingInfoActiveStations_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 4),
    _S5TrRingInfoActiveStations_Type()
)
s5TrRingInfoActiveStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoActiveStations.setStatus("mandatory")
_S5TrRingInfoDeletes_Type = Counter32
_S5TrRingInfoDeletes_Object = MibTableColumn
s5TrRingInfoDeletes = _S5TrRingInfoDeletes_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 5),
    _S5TrRingInfoDeletes_Type()
)
s5TrRingInfoDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoDeletes.setStatus("mandatory")
_S5TrRingInfoLastDeleteTime_Type = TimeTicks
_S5TrRingInfoLastDeleteTime_Object = MibTableColumn
s5TrRingInfoLastDeleteTime = _S5TrRingInfoLastDeleteTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 6),
    _S5TrRingInfoLastDeleteTime_Type()
)
s5TrRingInfoLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoLastDeleteTime.setStatus("mandatory")


class _S5TrRingInfoAgeInterval_Type(TimeIntervalSec):
    """Custom type s5TrRingInfoAgeInterval based on TimeIntervalSec"""
    defaultValue = 0


_S5TrRingInfoAgeInterval_Object = MibTableColumn
s5TrRingInfoAgeInterval = _S5TrRingInfoAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 7),
    _S5TrRingInfoAgeInterval_Type()
)
s5TrRingInfoAgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrRingInfoAgeInterval.setStatus("mandatory")
_S5TrRingInfoMonTime_Type = TimeTicks
_S5TrRingInfoMonTime_Object = MibTableColumn
s5TrRingInfoMonTime = _S5TrRingInfoMonTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 8),
    _S5TrRingInfoMonTime_Type()
)
s5TrRingInfoMonTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoMonTime.setStatus("mandatory")


class _S5TrRingInfoRingState_Type(Integer32):
    """Custom type s5TrRingInfoRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("beaconBitStreaming", 5),
          ("beaconFrameStreaming", 4),
          ("beaconRingSignalLoss", 6),
          ("beaconSetRecoveryMode", 7),
          ("monitorContention", 3),
          ("normalOperation", 1),
          ("ringPurge", 2))
    )


_S5TrRingInfoRingState_Type.__name__ = "Integer32"
_S5TrRingInfoRingState_Object = MibTableColumn
s5TrRingInfoRingState = _S5TrRingInfoRingState_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 9),
    _S5TrRingInfoRingState_Type()
)
s5TrRingInfoRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoRingState.setStatus("mandatory")
_S5TrRingInfoBeaconSender_Type = MacAddress
_S5TrRingInfoBeaconSender_Object = MibTableColumn
s5TrRingInfoBeaconSender = _S5TrRingInfoBeaconSender_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 10),
    _S5TrRingInfoBeaconSender_Type()
)
s5TrRingInfoBeaconSender.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoBeaconSender.setStatus("mandatory")
_S5TrRingInfoBeaconNaun_Type = MacAddress
_S5TrRingInfoBeaconNaun_Object = MibTableColumn
s5TrRingInfoBeaconNaun = _S5TrRingInfoBeaconNaun_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 11),
    _S5TrRingInfoBeaconNaun_Type()
)
s5TrRingInfoBeaconNaun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoBeaconNaun.setStatus("mandatory")


class _S5TrRingInfoBeaconType_Type(Integer32):
    """Custom type s5TrRingInfoBeaconType based on Integer32"""
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
        *(("bitStreaming", 4),
          ("contentionStreaming", 5),
          ("other", 1),
          ("recovery", 2),
          ("signalLoss", 3))
    )


_S5TrRingInfoBeaconType_Type.__name__ = "Integer32"
_S5TrRingInfoBeaconType_Object = MibTableColumn
s5TrRingInfoBeaconType = _S5TrRingInfoBeaconType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 12),
    _S5TrRingInfoBeaconType_Type()
)
s5TrRingInfoBeaconType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoBeaconType.setStatus("mandatory")
_S5TrRingInfoLastBeaconTime_Type = TimeTicks
_S5TrRingInfoLastBeaconTime_Object = MibTableColumn
s5TrRingInfoLastBeaconTime = _S5TrRingInfoLastBeaconTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 13),
    _S5TrRingInfoLastBeaconTime_Type()
)
s5TrRingInfoLastBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoLastBeaconTime.setStatus("mandatory")
_S5TrRingInfoActiveMonitor_Type = MacAddress
_S5TrRingInfoActiveMonitor_Object = MibTableColumn
s5TrRingInfoActiveMonitor = _S5TrRingInfoActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 14),
    _S5TrRingInfoActiveMonitor_Type()
)
s5TrRingInfoActiveMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoActiveMonitor.setStatus("mandatory")
_S5TrRingInfoChanges_Type = Counter32
_S5TrRingInfoChanges_Object = MibTableColumn
s5TrRingInfoChanges = _S5TrRingInfoChanges_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 15),
    _S5TrRingInfoChanges_Type()
)
s5TrRingInfoChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoChanges.setStatus("mandatory")
_S5TrRingInfoRingPurgeEvents_Type = Counter32
_S5TrRingInfoRingPurgeEvents_Object = MibTableColumn
s5TrRingInfoRingPurgeEvents = _S5TrRingInfoRingPurgeEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 16),
    _S5TrRingInfoRingPurgeEvents_Type()
)
s5TrRingInfoRingPurgeEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoRingPurgeEvents.setStatus("mandatory")
_S5TrRingInfoBeaconEvents_Type = Counter32
_S5TrRingInfoBeaconEvents_Object = MibTableColumn
s5TrRingInfoBeaconEvents = _S5TrRingInfoBeaconEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 17),
    _S5TrRingInfoBeaconEvents_Type()
)
s5TrRingInfoBeaconEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoBeaconEvents.setStatus("mandatory")
_S5TrRingInfoBeaconTime_Type = TimeIntervalHrd
_S5TrRingInfoBeaconTime_Object = MibTableColumn
s5TrRingInfoBeaconTime = _S5TrRingInfoBeaconTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 18),
    _S5TrRingInfoBeaconTime_Type()
)
s5TrRingInfoBeaconTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoBeaconTime.setStatus("mandatory")
_S5TrRingInfoMonitorContentionEvents_Type = Counter32
_S5TrRingInfoMonitorContentionEvents_Object = MibTableColumn
s5TrRingInfoMonitorContentionEvents = _S5TrRingInfoMonitorContentionEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 19),
    _S5TrRingInfoMonitorContentionEvents_Type()
)
s5TrRingInfoMonitorContentionEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoMonitorContentionEvents.setStatus("mandatory")
_S5TrRingInfoNaunChanges_Type = Counter32
_S5TrRingInfoNaunChanges_Object = MibTableColumn
s5TrRingInfoNaunChanges = _S5TrRingInfoNaunChanges_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 20),
    _S5TrRingInfoNaunChanges_Type()
)
s5TrRingInfoNaunChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoNaunChanges.setStatus("mandatory")
_S5TrRingInfoRingPollEvents_Type = Counter32
_S5TrRingInfoRingPollEvents_Object = MibTableColumn
s5TrRingInfoRingPollEvents = _S5TrRingInfoRingPollEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 1, 1, 21),
    _S5TrRingInfoRingPollEvents_Type()
)
s5TrRingInfoRingPollEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrRingInfoRingPollEvents.setStatus("mandatory")
_S5TrStaInfoTable_Object = MibTable
s5TrStaInfoTable = _S5TrStaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2)
)
if mibBuilder.loadTexts:
    s5TrStaInfoTable.setStatus("mandatory")
_S5TrStaInfoEntry_Object = MibTableRow
s5TrStaInfoEntry = _S5TrStaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1)
)
s5TrStaInfoEntry.setIndexNames(
    (0, "S5-TOKENRING-MIB", "s5TrStaInfoSrcIndx"),
    (0, "S5-TOKENRING-MIB", "s5TrStaInfoAddr"),
)
if mibBuilder.loadTexts:
    s5TrStaInfoEntry.setStatus("mandatory")
_S5TrStaInfoSrcIndx_Type = SrcIndx
_S5TrStaInfoSrcIndx_Object = MibTableColumn
s5TrStaInfoSrcIndx = _S5TrStaInfoSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 1),
    _S5TrStaInfoSrcIndx_Type()
)
s5TrStaInfoSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoSrcIndx.setStatus("mandatory")
_S5TrStaInfoAddr_Type = MacAddress
_S5TrStaInfoAddr_Object = MibTableColumn
s5TrStaInfoAddr = _S5TrStaInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 2),
    _S5TrStaInfoAddr_Type()
)
s5TrStaInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoAddr.setStatus("mandatory")
_S5TrStaInfoLastNaun_Type = MacAddress
_S5TrStaInfoLastNaun_Object = MibTableColumn
s5TrStaInfoLastNaun = _S5TrStaInfoLastNaun_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 3),
    _S5TrStaInfoLastNaun_Type()
)
s5TrStaInfoLastNaun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoLastNaun.setStatus("mandatory")


class _S5TrStaInfoStationStatus_Type(Integer32):
    """Custom type s5TrStaInfoStationStatus based on Integer32"""
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
          ("forcedRemoval", 4),
          ("inactive", 3),
          ("notInRingPoll", 2))
    )


_S5TrStaInfoStationStatus_Type.__name__ = "Integer32"
_S5TrStaInfoStationStatus_Object = MibTableColumn
s5TrStaInfoStationStatus = _S5TrStaInfoStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 4),
    _S5TrStaInfoStationStatus_Type()
)
s5TrStaInfoStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoStationStatus.setStatus("mandatory")
_S5TrStaInfoFirstEnterTime_Type = TimeTicks
_S5TrStaInfoFirstEnterTime_Object = MibTableColumn
s5TrStaInfoFirstEnterTime = _S5TrStaInfoFirstEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 5),
    _S5TrStaInfoFirstEnterTime_Type()
)
s5TrStaInfoFirstEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoFirstEnterTime.setStatus("mandatory")
_S5TrStaInfoLastEnterTime_Type = TimeTicks
_S5TrStaInfoLastEnterTime_Object = MibTableColumn
s5TrStaInfoLastEnterTime = _S5TrStaInfoLastEnterTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 6),
    _S5TrStaInfoLastEnterTime_Type()
)
s5TrStaInfoLastEnterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoLastEnterTime.setStatus("mandatory")
_S5TrStaInfoLastExitTime_Type = TimeTicks
_S5TrStaInfoLastExitTime_Object = MibTableColumn
s5TrStaInfoLastExitTime = _S5TrStaInfoLastExitTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 7),
    _S5TrStaInfoLastExitTime_Type()
)
s5TrStaInfoLastExitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoLastExitTime.setStatus("mandatory")
_S5TrStaInfoDupAddrErrs_Type = Counter32
_S5TrStaInfoDupAddrErrs_Object = MibTableColumn
s5TrStaInfoDupAddrErrs = _S5TrStaInfoDupAddrErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 8),
    _S5TrStaInfoDupAddrErrs_Type()
)
s5TrStaInfoDupAddrErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoDupAddrErrs.setStatus("mandatory")
_S5TrStaInfoInLineErrs_Type = Counter32
_S5TrStaInfoInLineErrs_Object = MibTableColumn
s5TrStaInfoInLineErrs = _S5TrStaInfoInLineErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 9),
    _S5TrStaInfoInLineErrs_Type()
)
s5TrStaInfoInLineErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoInLineErrs.setStatus("mandatory")
_S5TrStaInfoOutLineErrs_Type = Counter32
_S5TrStaInfoOutLineErrs_Object = MibTableColumn
s5TrStaInfoOutLineErrs = _S5TrStaInfoOutLineErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 10),
    _S5TrStaInfoOutLineErrs_Type()
)
s5TrStaInfoOutLineErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoOutLineErrs.setStatus("mandatory")
_S5TrStaInfoInternalErrs_Type = Counter32
_S5TrStaInfoInternalErrs_Object = MibTableColumn
s5TrStaInfoInternalErrs = _S5TrStaInfoInternalErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 11),
    _S5TrStaInfoInternalErrs_Type()
)
s5TrStaInfoInternalErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoInternalErrs.setStatus("mandatory")
_S5TrStaInfoInBurstErrs_Type = Counter32
_S5TrStaInfoInBurstErrs_Object = MibTableColumn
s5TrStaInfoInBurstErrs = _S5TrStaInfoInBurstErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 12),
    _S5TrStaInfoInBurstErrs_Type()
)
s5TrStaInfoInBurstErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoInBurstErrs.setStatus("mandatory")
_S5TrStaInfoOutBurstErrs_Type = Counter32
_S5TrStaInfoOutBurstErrs_Object = MibTableColumn
s5TrStaInfoOutBurstErrs = _S5TrStaInfoOutBurstErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 13),
    _S5TrStaInfoOutBurstErrs_Type()
)
s5TrStaInfoOutBurstErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoOutBurstErrs.setStatus("mandatory")
_S5TrStaInfoInACErrs_Type = Counter32
_S5TrStaInfoInACErrs_Object = MibTableColumn
s5TrStaInfoInACErrs = _S5TrStaInfoInACErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 14),
    _S5TrStaInfoInACErrs_Type()
)
s5TrStaInfoInACErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoInACErrs.setStatus("mandatory")
_S5TrStaInfoOutACErrs_Type = Counter32
_S5TrStaInfoOutACErrs_Object = MibTableColumn
s5TrStaInfoOutACErrs = _S5TrStaInfoOutACErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 15),
    _S5TrStaInfoOutACErrs_Type()
)
s5TrStaInfoOutACErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoOutACErrs.setStatus("mandatory")
_S5TrStaInfoAbortErrs_Type = Counter32
_S5TrStaInfoAbortErrs_Object = MibTableColumn
s5TrStaInfoAbortErrs = _S5TrStaInfoAbortErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 16),
    _S5TrStaInfoAbortErrs_Type()
)
s5TrStaInfoAbortErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoAbortErrs.setStatus("mandatory")
_S5TrStaInfoLostFrameErrs_Type = Counter32
_S5TrStaInfoLostFrameErrs_Object = MibTableColumn
s5TrStaInfoLostFrameErrs = _S5TrStaInfoLostFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 17),
    _S5TrStaInfoLostFrameErrs_Type()
)
s5TrStaInfoLostFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoLostFrameErrs.setStatus("mandatory")
_S5TrStaInfoCongestionErrs_Type = Counter32
_S5TrStaInfoCongestionErrs_Object = MibTableColumn
s5TrStaInfoCongestionErrs = _S5TrStaInfoCongestionErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 18),
    _S5TrStaInfoCongestionErrs_Type()
)
s5TrStaInfoCongestionErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoCongestionErrs.setStatus("mandatory")
_S5TrStaInfoFrameCopiedErrs_Type = Counter32
_S5TrStaInfoFrameCopiedErrs_Object = MibTableColumn
s5TrStaInfoFrameCopiedErrs = _S5TrStaInfoFrameCopiedErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 19),
    _S5TrStaInfoFrameCopiedErrs_Type()
)
s5TrStaInfoFrameCopiedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoFrameCopiedErrs.setStatus("mandatory")
_S5TrStaInfoFrequencyErrs_Type = Counter32
_S5TrStaInfoFrequencyErrs_Object = MibTableColumn
s5TrStaInfoFrequencyErrs = _S5TrStaInfoFrequencyErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 20),
    _S5TrStaInfoFrequencyErrs_Type()
)
s5TrStaInfoFrequencyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoFrequencyErrs.setStatus("mandatory")
_S5TrStaInfoTokenErrs_Type = Counter32
_S5TrStaInfoTokenErrs_Object = MibTableColumn
s5TrStaInfoTokenErrs = _S5TrStaInfoTokenErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 21),
    _S5TrStaInfoTokenErrs_Type()
)
s5TrStaInfoTokenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoTokenErrs.setStatus("mandatory")
_S5TrStaInfoInBeaconErrs_Type = Counter32
_S5TrStaInfoInBeaconErrs_Object = MibTableColumn
s5TrStaInfoInBeaconErrs = _S5TrStaInfoInBeaconErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 22),
    _S5TrStaInfoInBeaconErrs_Type()
)
s5TrStaInfoInBeaconErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoInBeaconErrs.setStatus("mandatory")
_S5TrStaInfoOutBeaconErrs_Type = Counter32
_S5TrStaInfoOutBeaconErrs_Object = MibTableColumn
s5TrStaInfoOutBeaconErrs = _S5TrStaInfoOutBeaconErrs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 23),
    _S5TrStaInfoOutBeaconErrs_Type()
)
s5TrStaInfoOutBeaconErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoOutBeaconErrs.setStatus("mandatory")
_S5TrStaInfoInsertions_Type = Counter32
_S5TrStaInfoInsertions_Object = MibTableColumn
s5TrStaInfoInsertions = _S5TrStaInfoInsertions_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 2, 1, 24),
    _S5TrStaInfoInsertions_Type()
)
s5TrStaInfoInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaInfoInsertions.setStatus("mandatory")
_S5TrStaCtlTable_Object = MibTable
s5TrStaCtlTable = _S5TrStaCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3)
)
if mibBuilder.loadTexts:
    s5TrStaCtlTable.setStatus("mandatory")
_S5TrStaCtlEntry_Object = MibTableRow
s5TrStaCtlEntry = _S5TrStaCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1)
)
s5TrStaCtlEntry.setIndexNames(
    (0, "S5-TOKENRING-MIB", "s5TrStaCtlSrcIndx"),
    (0, "S5-TOKENRING-MIB", "s5TrStaCtlAddr"),
)
if mibBuilder.loadTexts:
    s5TrStaCtlEntry.setStatus("mandatory")
_S5TrStaCtlSrcIndx_Type = SrcIndx
_S5TrStaCtlSrcIndx_Object = MibTableColumn
s5TrStaCtlSrcIndx = _S5TrStaCtlSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 1),
    _S5TrStaCtlSrcIndx_Type()
)
s5TrStaCtlSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlSrcIndx.setStatus("mandatory")
_S5TrStaCtlAddr_Type = MacAddress
_S5TrStaCtlAddr_Object = MibTableColumn
s5TrStaCtlAddr = _S5TrStaCtlAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 2),
    _S5TrStaCtlAddr_Type()
)
s5TrStaCtlAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlAddr.setStatus("mandatory")


class _S5TrStaCtlRemove_Type(Integer32):
    """Custom type s5TrStaCtlRemove based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("remove", 2),
          ("stable", 1))
    )


_S5TrStaCtlRemove_Type.__name__ = "Integer32"
_S5TrStaCtlRemove_Object = MibTableColumn
s5TrStaCtlRemove = _S5TrStaCtlRemove_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 3),
    _S5TrStaCtlRemove_Type()
)
s5TrStaCtlRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrStaCtlRemove.setStatus("mandatory")


class _S5TrStaCtlUpdateStats_Type(Integer32):
    """Custom type s5TrStaCtlUpdateStats based on Integer32"""
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
        *(("inactive", 2),
          ("other", 1),
          ("stable", 3),
          ("update", 4))
    )


_S5TrStaCtlUpdateStats_Type.__name__ = "Integer32"
_S5TrStaCtlUpdateStats_Object = MibTableColumn
s5TrStaCtlUpdateStats = _S5TrStaCtlUpdateStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 4),
    _S5TrStaCtlUpdateStats_Type()
)
s5TrStaCtlUpdateStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrStaCtlUpdateStats.setStatus("mandatory")
_S5TrStaCtlUpdateTime_Type = TimeTicks
_S5TrStaCtlUpdateTime_Object = MibTableColumn
s5TrStaCtlUpdateTime = _S5TrStaCtlUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 5),
    _S5TrStaCtlUpdateTime_Type()
)
s5TrStaCtlUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlUpdateTime.setStatus("mandatory")


class _S5TrStaCtlProductId_Type(OctetString):
    """Custom type s5TrStaCtlProductId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_S5TrStaCtlProductId_Type.__name__ = "OctetString"
_S5TrStaCtlProductId_Object = MibTableColumn
s5TrStaCtlProductId = _S5TrStaCtlProductId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 6),
    _S5TrStaCtlProductId_Type()
)
s5TrStaCtlProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlProductId.setStatus("mandatory")


class _S5TrStaCtlNodeVersion_Type(OctetString):
    """Custom type s5TrStaCtlNodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_S5TrStaCtlNodeVersion_Type.__name__ = "OctetString"
_S5TrStaCtlNodeVersion_Object = MibTableColumn
s5TrStaCtlNodeVersion = _S5TrStaCtlNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 7),
    _S5TrStaCtlNodeVersion_Type()
)
s5TrStaCtlNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlNodeVersion.setStatus("mandatory")


class _S5TrStaCtlPhysDrop_Type(OctetString):
    """Custom type s5TrStaCtlPhysDrop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_S5TrStaCtlPhysDrop_Type.__name__ = "OctetString"
_S5TrStaCtlPhysDrop_Object = MibTableColumn
s5TrStaCtlPhysDrop = _S5TrStaCtlPhysDrop_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 8),
    _S5TrStaCtlPhysDrop_Type()
)
s5TrStaCtlPhysDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlPhysDrop.setStatus("mandatory")
_S5TrStaCtlFuncAddr_Type = MacAddress
_S5TrStaCtlFuncAddr_Object = MibTableColumn
s5TrStaCtlFuncAddr = _S5TrStaCtlFuncAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 9),
    _S5TrStaCtlFuncAddr_Type()
)
s5TrStaCtlFuncAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlFuncAddr.setStatus("mandatory")


class _S5TrStaCtlAuthFuncClass_Type(OctetString):
    """Custom type s5TrStaCtlAuthFuncClass based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_S5TrStaCtlAuthFuncClass_Type.__name__ = "OctetString"
_S5TrStaCtlAuthFuncClass_Object = MibTableColumn
s5TrStaCtlAuthFuncClass = _S5TrStaCtlAuthFuncClass_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 10),
    _S5TrStaCtlAuthFuncClass_Type()
)
s5TrStaCtlAuthFuncClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlAuthFuncClass.setStatus("mandatory")


class _S5TrStaCtlAuthAccPriority_Type(OctetString):
    """Custom type s5TrStaCtlAuthAccPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_S5TrStaCtlAuthAccPriority_Type.__name__ = "OctetString"
_S5TrStaCtlAuthAccPriority_Object = MibTableColumn
s5TrStaCtlAuthAccPriority = _S5TrStaCtlAuthAccPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 11),
    _S5TrStaCtlAuthAccPriority_Type()
)
s5TrStaCtlAuthAccPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlAuthAccPriority.setStatus("mandatory")
_S5TrStaCtlStationId_Type = MacAddress
_S5TrStaCtlStationId_Object = MibTableColumn
s5TrStaCtlStationId = _S5TrStaCtlStationId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 12),
    _S5TrStaCtlStationId_Type()
)
s5TrStaCtlStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlStationId.setStatus("mandatory")
_S5TrStaCtlNumGrpAddr_Type = MacAddress
_S5TrStaCtlNumGrpAddr_Object = MibTableColumn
s5TrStaCtlNumGrpAddr = _S5TrStaCtlNumGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 3, 3, 1, 13),
    _S5TrStaCtlNumGrpAddr_Type()
)
s5TrStaCtlNumGrpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrStaCtlNumGrpAddr.setStatus("mandatory")
_S5TrTest_ObjectIdentity = ObjectIdentity
s5TrTest = _S5TrTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4)
)


class _S5TrTestPathTestTimer_Type(TimeIntervalHrd):
    """Custom type s5TrTestPathTestTimer based on TimeIntervalHrd"""
    defaultValue = 400


_S5TrTestPathTestTimer_Object = MibScalar
s5TrTestPathTestTimer = _S5TrTestPathTestTimer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 1),
    _S5TrTestPathTestTimer_Type()
)
s5TrTestPathTestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrTestPathTestTimer.setStatus("mandatory")


class _S5TrTestPathAgeTimer_Type(TimeIntervalSec):
    """Custom type s5TrTestPathAgeTimer based on TimeIntervalSec"""
    defaultValue = 300

    subtypeSpec = TimeIntervalSec.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S5TrTestPathAgeTimer_Type.__name__ = "TimeIntervalSec"
_S5TrTestPathAgeTimer_Object = MibScalar
s5TrTestPathAgeTimer = _S5TrTestPathAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 2),
    _S5TrTestPathAgeTimer_Type()
)
s5TrTestPathAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrTestPathAgeTimer.setStatus("mandatory")
_S5TrTestPathTable_Object = MibTable
s5TrTestPathTable = _S5TrTestPathTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3)
)
if mibBuilder.loadTexts:
    s5TrTestPathTable.setStatus("mandatory")
_S5TrTestPathEntry_Object = MibTableRow
s5TrTestPathEntry = _S5TrTestPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1)
)
s5TrTestPathEntry.setIndexNames(
    (0, "S5-TOKENRING-MIB", "s5TrTestTpIfIndex"),
    (0, "S5-TOKENRING-MIB", "s5TrTestTpAddrTo"),
)
if mibBuilder.loadTexts:
    s5TrTestPathEntry.setStatus("mandatory")


class _S5TrTestTpIfIndex_Type(Integer32):
    """Custom type s5TrTestTpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_S5TrTestTpIfIndex_Type.__name__ = "Integer32"
_S5TrTestTpIfIndex_Object = MibTableColumn
s5TrTestTpIfIndex = _S5TrTestTpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 1),
    _S5TrTestTpIfIndex_Type()
)
s5TrTestTpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTestTpIfIndex.setStatus("mandatory")


class _S5TrTestTpAddrTo_Type(OctetString):
    """Custom type s5TrTestTpAddrTo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S5TrTestTpAddrTo_Type.__name__ = "OctetString"
_S5TrTestTpAddrTo_Object = MibTableColumn
s5TrTestTpAddrTo = _S5TrTestTpAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 2),
    _S5TrTestTpAddrTo_Type()
)
s5TrTestTpAddrTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTestTpAddrTo.setStatus("mandatory")


class _S5TrTestTpStart_Type(Integer32):
    """Custom type s5TrTestTpStart based on Integer32"""
    defaultValue = 2

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
        *(("clearTest", 6),
          ("other", 1),
          ("retryTestSourceRoute", 4),
          ("retryTestTransparent", 5),
          ("startTestSourceRoute", 2),
          ("startTestTransparent", 3))
    )


_S5TrTestTpStart_Type.__name__ = "Integer32"
_S5TrTestTpStart_Object = MibTableColumn
s5TrTestTpStart = _S5TrTestTpStart_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 3),
    _S5TrTestTpStart_Type()
)
s5TrTestTpStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrTestTpStart.setStatus("mandatory")


class _S5TrTestTpStatus_Type(Integer32):
    """Custom type s5TrTestTpStatus based on Integer32"""
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
        *(("other", 1),
          ("testFailed", 4),
          ("testInProgress", 2),
          ("testPassed", 3))
    )


_S5TrTestTpStatus_Type.__name__ = "Integer32"
_S5TrTestTpStatus_Object = MibTableColumn
s5TrTestTpStatus = _S5TrTestTpStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 4),
    _S5TrTestTpStatus_Type()
)
s5TrTestTpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTestTpStatus.setStatus("mandatory")


class _S5TrTestTpRoute_Type(OctetString):
    """Custom type s5TrTestTpRoute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_S5TrTestTpRoute_Type.__name__ = "OctetString"
_S5TrTestTpRoute_Object = MibTableColumn
s5TrTestTpRoute = _S5TrTestTpRoute_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 5),
    _S5TrTestTpRoute_Type()
)
s5TrTestTpRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5TrTestTpRoute.setStatus("mandatory")
_S5TrTestTpDuration_Type = TimeIntervalHrd
_S5TrTestTpDuration_Object = MibTableColumn
s5TrTestTpDuration = _S5TrTestTpDuration_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 6),
    _S5TrTestTpDuration_Type()
)
s5TrTestTpDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTestTpDuration.setStatus("mandatory")
_S5TrTestTpTimeStamp_Type = TimeTicks
_S5TrTestTpTimeStamp_Object = MibTableColumn
s5TrTestTpTimeStamp = _S5TrTestTpTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 7, 4, 3, 1, 7),
    _S5TrTestTpTimeStamp_Type()
)
s5TrTestTpTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5TrTestTpTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-TOKENRING-MIB",
    **{"s5TrCfg": s5TrCfg,
       "s5TrStat": s5TrStat,
       "s5TrRing": s5TrRing,
       "s5TrRingInfoTable": s5TrRingInfoTable,
       "s5TrRingInfoEntry": s5TrRingInfoEntry,
       "s5TrRingInfoSrcIndx": s5TrRingInfoSrcIndx,
       "s5TrRingInfoRingNum": s5TrRingInfoRingNum,
       "s5TrRingInfoStaTableOperSize": s5TrRingInfoStaTableOperSize,
       "s5TrRingInfoActiveStations": s5TrRingInfoActiveStations,
       "s5TrRingInfoDeletes": s5TrRingInfoDeletes,
       "s5TrRingInfoLastDeleteTime": s5TrRingInfoLastDeleteTime,
       "s5TrRingInfoAgeInterval": s5TrRingInfoAgeInterval,
       "s5TrRingInfoMonTime": s5TrRingInfoMonTime,
       "s5TrRingInfoRingState": s5TrRingInfoRingState,
       "s5TrRingInfoBeaconSender": s5TrRingInfoBeaconSender,
       "s5TrRingInfoBeaconNaun": s5TrRingInfoBeaconNaun,
       "s5TrRingInfoBeaconType": s5TrRingInfoBeaconType,
       "s5TrRingInfoLastBeaconTime": s5TrRingInfoLastBeaconTime,
       "s5TrRingInfoActiveMonitor": s5TrRingInfoActiveMonitor,
       "s5TrRingInfoChanges": s5TrRingInfoChanges,
       "s5TrRingInfoRingPurgeEvents": s5TrRingInfoRingPurgeEvents,
       "s5TrRingInfoBeaconEvents": s5TrRingInfoBeaconEvents,
       "s5TrRingInfoBeaconTime": s5TrRingInfoBeaconTime,
       "s5TrRingInfoMonitorContentionEvents": s5TrRingInfoMonitorContentionEvents,
       "s5TrRingInfoNaunChanges": s5TrRingInfoNaunChanges,
       "s5TrRingInfoRingPollEvents": s5TrRingInfoRingPollEvents,
       "s5TrStaInfoTable": s5TrStaInfoTable,
       "s5TrStaInfoEntry": s5TrStaInfoEntry,
       "s5TrStaInfoSrcIndx": s5TrStaInfoSrcIndx,
       "s5TrStaInfoAddr": s5TrStaInfoAddr,
       "s5TrStaInfoLastNaun": s5TrStaInfoLastNaun,
       "s5TrStaInfoStationStatus": s5TrStaInfoStationStatus,
       "s5TrStaInfoFirstEnterTime": s5TrStaInfoFirstEnterTime,
       "s5TrStaInfoLastEnterTime": s5TrStaInfoLastEnterTime,
       "s5TrStaInfoLastExitTime": s5TrStaInfoLastExitTime,
       "s5TrStaInfoDupAddrErrs": s5TrStaInfoDupAddrErrs,
       "s5TrStaInfoInLineErrs": s5TrStaInfoInLineErrs,
       "s5TrStaInfoOutLineErrs": s5TrStaInfoOutLineErrs,
       "s5TrStaInfoInternalErrs": s5TrStaInfoInternalErrs,
       "s5TrStaInfoInBurstErrs": s5TrStaInfoInBurstErrs,
       "s5TrStaInfoOutBurstErrs": s5TrStaInfoOutBurstErrs,
       "s5TrStaInfoInACErrs": s5TrStaInfoInACErrs,
       "s5TrStaInfoOutACErrs": s5TrStaInfoOutACErrs,
       "s5TrStaInfoAbortErrs": s5TrStaInfoAbortErrs,
       "s5TrStaInfoLostFrameErrs": s5TrStaInfoLostFrameErrs,
       "s5TrStaInfoCongestionErrs": s5TrStaInfoCongestionErrs,
       "s5TrStaInfoFrameCopiedErrs": s5TrStaInfoFrameCopiedErrs,
       "s5TrStaInfoFrequencyErrs": s5TrStaInfoFrequencyErrs,
       "s5TrStaInfoTokenErrs": s5TrStaInfoTokenErrs,
       "s5TrStaInfoInBeaconErrs": s5TrStaInfoInBeaconErrs,
       "s5TrStaInfoOutBeaconErrs": s5TrStaInfoOutBeaconErrs,
       "s5TrStaInfoInsertions": s5TrStaInfoInsertions,
       "s5TrStaCtlTable": s5TrStaCtlTable,
       "s5TrStaCtlEntry": s5TrStaCtlEntry,
       "s5TrStaCtlSrcIndx": s5TrStaCtlSrcIndx,
       "s5TrStaCtlAddr": s5TrStaCtlAddr,
       "s5TrStaCtlRemove": s5TrStaCtlRemove,
       "s5TrStaCtlUpdateStats": s5TrStaCtlUpdateStats,
       "s5TrStaCtlUpdateTime": s5TrStaCtlUpdateTime,
       "s5TrStaCtlProductId": s5TrStaCtlProductId,
       "s5TrStaCtlNodeVersion": s5TrStaCtlNodeVersion,
       "s5TrStaCtlPhysDrop": s5TrStaCtlPhysDrop,
       "s5TrStaCtlFuncAddr": s5TrStaCtlFuncAddr,
       "s5TrStaCtlAuthFuncClass": s5TrStaCtlAuthFuncClass,
       "s5TrStaCtlAuthAccPriority": s5TrStaCtlAuthAccPriority,
       "s5TrStaCtlStationId": s5TrStaCtlStationId,
       "s5TrStaCtlNumGrpAddr": s5TrStaCtlNumGrpAddr,
       "s5TrTest": s5TrTest,
       "s5TrTestPathTestTimer": s5TrTestPathTestTimer,
       "s5TrTestPathAgeTimer": s5TrTestPathAgeTimer,
       "s5TrTestPathTable": s5TrTestPathTable,
       "s5TrTestPathEntry": s5TrTestPathEntry,
       "s5TrTestTpIfIndex": s5TrTestTpIfIndex,
       "s5TrTestTpAddrTo": s5TrTestTpAddrTo,
       "s5TrTestTpStart": s5TrTestTpStart,
       "s5TrTestTpStatus": s5TrTestTpStatus,
       "s5TrTestTpRoute": s5TrTestTpRoute,
       "s5TrTestTpDuration": s5TrTestTpDuration,
       "s5TrTestTpTimeStamp": s5TrTestTpTimeStamp}
)
