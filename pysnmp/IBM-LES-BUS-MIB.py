# SNMP MIB module (IBM-LES-BUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IBM-LES-BUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:07:35 2024
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

(AtmLaneAddress,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "AtmLaneAddress")

(lesConfEntry,
 lesConfIndex) = mibBuilder.importSymbols(
    "LAN-EMULATION-LES-MIB",
    "lesConfEntry",
    "lesConfIndex")

(AtmPrivateAddrEsi,
 AtmSelector,
 AtmVccTrafficType,
 Bandwidth,
 mssServerLanE) = mibBuilder.importSymbols(
    "NWAYSMSS-MIB",
    "AtmPrivateAddrEsi",
    "AtmSelector",
    "AtmVccTrafficType",
    "Bandwidth",
    "mssServerLanE")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmLesBusMIB_ObjectIdentity = ObjectIdentity
ibmLesBusMIB = _IbmLesBusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1)
)
_IbmLesBusConfGroup_ObjectIdentity = ObjectIdentity
ibmLesBusConfGroup = _IbmLesBusConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1)
)
_IbmLesBusConfTable_Object = MibTable
ibmLesBusConfTable = _IbmLesBusConfTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ibmLesBusConfTable.setStatus("mandatory")
_IbmLesBusConfEntry_Object = MibTableRow
ibmLesBusConfEntry = _IbmLesBusConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1)
)
ibmLesBusConfEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    ibmLesBusConfEntry.setStatus("mandatory")


class _AtmDevNum_Type(Integer32):
    """Custom type atmDevNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AtmDevNum_Type.__name__ = "Integer32"
_AtmDevNum_Object = MibTableColumn
atmDevNum = _AtmDevNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 1),
    _AtmDevNum_Type()
)
atmDevNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmDevNum.setStatus("mandatory")
_UseBurnedInEsi_Type = TruthValue
_UseBurnedInEsi_Object = MibTableColumn
useBurnedInEsi = _UseBurnedInEsi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 2),
    _UseBurnedInEsi_Type()
)
useBurnedInEsi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useBurnedInEsi.setStatus("mandatory")
_ConfiguredEsi_Type = AtmPrivateAddrEsi
_ConfiguredEsi_Object = MibTableColumn
configuredEsi = _ConfiguredEsi_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 3),
    _ConfiguredEsi_Type()
)
configuredEsi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configuredEsi.setStatus("mandatory")
_ConfiguredSelector_Type = AtmSelector
_ConfiguredSelector_Object = MibTableColumn
configuredSelector = _ConfiguredSelector_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 4),
    _ConfiguredSelector_Type()
)
configuredSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configuredSelector.setStatus("mandatory")


class _LeArpResponseDest_Type(Integer32):
    """Custom type leArpResponseDest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allClients", 1),
          ("oneClient", 0))
    )


_LeArpResponseDest_Type.__name__ = "Integer32"
_LeArpResponseDest_Object = MibTableColumn
leArpResponseDest = _LeArpResponseDest_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 5),
    _LeArpResponseDest_Type()
)
leArpResponseDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leArpResponseDest.setStatus("mandatory")
_Use2ControlDistributeVccs_Type = TruthValue
_Use2ControlDistributeVccs_Object = MibTableColumn
use2ControlDistributeVccs = _Use2ControlDistributeVccs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 6),
    _Use2ControlDistributeVccs_Type()
)
use2ControlDistributeVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    use2ControlDistributeVccs.setStatus("mandatory")
_Use2MulticastForwardVccs_Type = TruthValue
_Use2MulticastForwardVccs_Object = MibTableColumn
use2MulticastForwardVccs = _Use2MulticastForwardVccs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 7),
    _Use2MulticastForwardVccs_Type()
)
use2MulticastForwardVccs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    use2MulticastForwardVccs.setStatus("mandatory")
_ValidateBestEffortPcr_Type = TruthValue
_ValidateBestEffortPcr_Object = MibTableColumn
validateBestEffortPcr = _ValidateBestEffortPcr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 8),
    _ValidateBestEffortPcr_Type()
)
validateBestEffortPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validateBestEffortPcr.setStatus("mandatory")
_ControlDirectMaxReservedBw_Type = Bandwidth
_ControlDirectMaxReservedBw_Object = MibTableColumn
controlDirectMaxReservedBw = _ControlDirectMaxReservedBw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 9),
    _ControlDirectMaxReservedBw_Type()
)
controlDirectMaxReservedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlDirectMaxReservedBw.setStatus("mandatory")
_MulticastSendMaxReservedBw_Type = Bandwidth
_MulticastSendMaxReservedBw_Object = MibTableColumn
multicastSendMaxReservedBw = _MulticastSendMaxReservedBw_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 10),
    _MulticastSendMaxReservedBw_Type()
)
multicastSendMaxReservedBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastSendMaxReservedBw.setStatus("mandatory")
_ControlDistributeVccType_Type = AtmVccTrafficType
_ControlDistributeVccType_Object = MibTableColumn
controlDistributeVccType = _ControlDistributeVccType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 11),
    _ControlDistributeVccType_Type()
)
controlDistributeVccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlDistributeVccType.setStatus("mandatory")
_ControlDistributePcr_Type = Bandwidth
_ControlDistributePcr_Object = MibTableColumn
controlDistributePcr = _ControlDistributePcr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 12),
    _ControlDistributePcr_Type()
)
controlDistributePcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlDistributePcr.setStatus("mandatory")
_ControlDistributeScr_Type = Bandwidth
_ControlDistributeScr_Object = MibTableColumn
controlDistributeScr = _ControlDistributeScr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 13),
    _ControlDistributeScr_Type()
)
controlDistributeScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    controlDistributeScr.setStatus("mandatory")
_MulticastForwardVccType_Type = AtmVccTrafficType
_MulticastForwardVccType_Object = MibTableColumn
multicastForwardVccType = _MulticastForwardVccType_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 14),
    _MulticastForwardVccType_Type()
)
multicastForwardVccType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastForwardVccType.setStatus("mandatory")
_MulticastForwardPcr_Type = Bandwidth
_MulticastForwardPcr_Object = MibTableColumn
multicastForwardPcr = _MulticastForwardPcr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 15),
    _MulticastForwardPcr_Type()
)
multicastForwardPcr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastForwardPcr.setStatus("mandatory")
_MulticastForwardScr_Type = Bandwidth
_MulticastForwardScr_Object = MibTableColumn
multicastForwardScr = _MulticastForwardScr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 16),
    _MulticastForwardScr_Type()
)
multicastForwardScr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastForwardScr.setStatus("mandatory")
_ValidateJoinsWithLecs_Type = TruthValue
_ValidateJoinsWithLecs_Object = MibTableColumn
validateJoinsWithLecs = _ValidateJoinsWithLecs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 17),
    _ValidateJoinsWithLecs_Type()
)
validateJoinsWithLecs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    validateJoinsWithLecs.setStatus("mandatory")
_RedundancyEnabled_Type = TruthValue
_RedundancyEnabled_Object = MibTableColumn
redundancyEnabled = _RedundancyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 18),
    _RedundancyEnabled_Type()
)
redundancyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyEnabled.setStatus("mandatory")


class _RedundancyRole_Type(Integer32):
    """Custom type redundancyRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backupLesBus", 2),
          ("neverSet", 0),
          ("primaryLesBus", 1))
    )


_RedundancyRole_Type.__name__ = "Integer32"
_RedundancyRole_Object = MibTableColumn
redundancyRole = _RedundancyRole_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 19),
    _RedundancyRole_Type()
)
redundancyRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyRole.setStatus("mandatory")
_RedundancyAtmAddr_Type = AtmLaneAddress
_RedundancyAtmAddr_Object = MibTableColumn
redundancyAtmAddr = _RedundancyAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 20),
    _RedundancyAtmAddr_Type()
)
redundancyAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    redundancyAtmAddr.setStatus("mandatory")
_BmonEnabled_Type = TruthValue
_BmonEnabled_Object = MibTableColumn
bmonEnabled = _BmonEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 21),
    _BmonEnabled_Type()
)
bmonEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmonEnabled.setStatus("mandatory")


class _NumTopMacs_Type(Integer32):
    """Custom type numTopMacs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NumTopMacs_Type.__name__ = "Integer32"
_NumTopMacs_Object = MibTableColumn
numTopMacs = _NumTopMacs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 22),
    _NumTopMacs_Type()
)
numTopMacs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    numTopMacs.setStatus("mandatory")


class _SampleDuration_Type(Integer32):
    """Custom type sampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_SampleDuration_Type.__name__ = "Integer32"
_SampleDuration_Object = MibTableColumn
sampleDuration = _SampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 23),
    _SampleDuration_Type()
)
sampleDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sampleDuration.setStatus("mandatory")


class _InterSampleTime_Type(Integer32):
    """Custom type interSampleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_InterSampleTime_Type.__name__ = "Integer32"
_InterSampleTime_Object = MibTableColumn
interSampleTime = _InterSampleTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 24),
    _InterSampleTime_Type()
)
interSampleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interSampleTime.setStatus("mandatory")


class _SampleRate_Type(Integer32):
    """Custom type sampleRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SampleRate_Type.__name__ = "Integer32"
_SampleRate_Object = MibTableColumn
sampleRate = _SampleRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 25),
    _SampleRate_Type()
)
sampleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sampleRate.setStatus("mandatory")


class _BusMode_Type(Integer32):
    """Custom type busMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("adapterBusMode", 2),
          ("systemBusMode", 1),
          ("vccSpliceBusMode", 3))
    )


_BusMode_Type.__name__ = "Integer32"
_BusMode_Object = MibTableColumn
busMode = _BusMode_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 1, 1, 1, 26),
    _BusMode_Type()
)
busMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    busMode.setStatus("mandatory")
_IbmLesBusStatGroup_ObjectIdentity = ObjectIdentity
ibmLesBusStatGroup = _IbmLesBusStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 2)
)
_IbmLesBusStatTable_Object = MibTable
ibmLesBusStatTable = _IbmLesBusStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ibmLesBusStatTable.setStatus("mandatory")
_IbmLesBusStatEntry_Object = MibTableRow
ibmLesBusStatEntry = _IbmLesBusStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 2, 1, 1)
)
ibmLesBusStatEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    ibmLesBusStatEntry.setStatus("mandatory")
_RedundancyVccRefused_Type = Counter32
_RedundancyVccRefused_Object = MibTableColumn
redundancyVccRefused = _RedundancyVccRefused_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 2, 1, 1, 1),
    _RedundancyVccRefused_Type()
)
redundancyVccRefused.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyVccRefused.setStatus("mandatory")
_RedundancyVccReleased_Type = Counter32
_RedundancyVccReleased_Object = MibTableColumn
redundancyVccReleased = _RedundancyVccReleased_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 2, 1, 1, 2),
    _RedundancyVccReleased_Type()
)
redundancyVccReleased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyVccReleased.setStatus("mandatory")
_RedundancyVccFailure_Type = Counter32
_RedundancyVccFailure_Object = MibTableColumn
redundancyVccFailure = _RedundancyVccFailure_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 2, 1, 1, 3),
    _RedundancyVccFailure_Type()
)
redundancyVccFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyVccFailure.setStatus("mandatory")
_IbmBusMonStatGroup_ObjectIdentity = ObjectIdentity
ibmBusMonStatGroup = _IbmBusMonStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3)
)
_BmonSampleInfoTable_Object = MibTable
bmonSampleInfoTable = _BmonSampleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    bmonSampleInfoTable.setStatus("mandatory")
_BmonSampleInfoEntry_Object = MibTableRow
bmonSampleInfoEntry = _BmonSampleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1, 1)
)
bmonSampleInfoEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
)
if mibBuilder.loadTexts:
    bmonSampleInfoEntry.setStatus("mandatory")
_BmonSampleStartTime_Type = TimeStamp
_BmonSampleStartTime_Object = MibTableColumn
bmonSampleStartTime = _BmonSampleStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1, 1, 1),
    _BmonSampleStartTime_Type()
)
bmonSampleStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonSampleStartTime.setStatus("mandatory")
_BmonSampleDuration_Type = Counter32
_BmonSampleDuration_Object = MibTableColumn
bmonSampleDuration = _BmonSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1, 1, 2),
    _BmonSampleDuration_Type()
)
bmonSampleDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonSampleDuration.setStatus("mandatory")
_BmonNumTopMacs_Type = Counter32
_BmonNumTopMacs_Object = MibTableColumn
bmonNumTopMacs = _BmonNumTopMacs_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1, 1, 3),
    _BmonNumTopMacs_Type()
)
bmonNumTopMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonNumTopMacs.setStatus("mandatory")
_BmonReceivedFrames_Type = Counter32
_BmonReceivedFrames_Object = MibTableColumn
bmonReceivedFrames = _BmonReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1, 1, 4),
    _BmonReceivedFrames_Type()
)
bmonReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonReceivedFrames.setStatus("mandatory")
_BmonSampledFrames_Type = Counter32
_BmonSampledFrames_Object = MibTableColumn
bmonSampledFrames = _BmonSampledFrames_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1, 1, 5),
    _BmonSampledFrames_Type()
)
bmonSampledFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonSampledFrames.setStatus("mandatory")
_BmonSamplingRate_Type = Counter32
_BmonSamplingRate_Object = MibTableColumn
bmonSamplingRate = _BmonSamplingRate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 1, 1, 6),
    _BmonSamplingRate_Type()
)
bmonSamplingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonSamplingRate.setStatus("mandatory")
_BmonStatTable_Object = MibTable
bmonStatTable = _BmonStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    bmonStatTable.setStatus("mandatory")
_BmonStatEntry_Object = MibTableRow
bmonStatEntry = _BmonStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 2, 1)
)
bmonStatEntry.setIndexNames(
    (0, "LAN-EMULATION-LES-MIB", "lesConfIndex"),
    (0, "IBM-LES-BUS-MIB", "bmonTopNRank"),
)
if mibBuilder.loadTexts:
    bmonStatEntry.setStatus("mandatory")
_BmonTopNRank_Type = Counter32
_BmonTopNRank_Object = MibTableColumn
bmonTopNRank = _BmonTopNRank_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 2, 1, 1),
    _BmonTopNRank_Type()
)
bmonTopNRank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonTopNRank.setStatus("mandatory")
_BmonTopNSrcMacAddr_Type = MacAddress
_BmonTopNSrcMacAddr_Object = MibTableColumn
bmonTopNSrcMacAddr = _BmonTopNSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 2, 1, 2),
    _BmonTopNSrcMacAddr_Type()
)
bmonTopNSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonTopNSrcMacAddr.setStatus("mandatory")
_BmonTopNLecAtmAddr_Type = AtmLaneAddress
_BmonTopNLecAtmAddr_Object = MibTableColumn
bmonTopNLecAtmAddr = _BmonTopNLecAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 2, 1, 3),
    _BmonTopNLecAtmAddr_Type()
)
bmonTopNLecAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonTopNLecAtmAddr.setStatus("mandatory")
_BmonTopNFramesSampled_Type = Counter32
_BmonTopNFramesSampled_Object = MibTableColumn
bmonTopNFramesSampled = _BmonTopNFramesSampled_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 3, 2, 1, 4),
    _BmonTopNFramesSampled_Type()
)
bmonTopNFramesSampled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmonTopNFramesSampled.setStatus("mandatory")
_IbmLesBusMIBConformance_ObjectIdentity = ObjectIdentity
ibmLesBusMIBConformance = _IbmLesBusMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 4)
)
_IbmLesBusMIBGroups_ObjectIdentity = ObjectIdentity
ibmLesBusMIBGroups = _IbmLesBusMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 4, 1)
)
_IbmLesBusCConfGroup_ObjectIdentity = ObjectIdentity
ibmLesBusCConfGroup = _IbmLesBusCConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 4, 1, 1)
)
_IbmLesBusCStatGroup_ObjectIdentity = ObjectIdentity
ibmLesBusCStatGroup = _IbmLesBusCStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 4, 1, 2)
)
_IbmBusMonCStatGroup_ObjectIdentity = ObjectIdentity
ibmBusMonCStatGroup = _IbmBusMonCStatGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 4, 1, 3)
)
_IbmLesBusMIBCompliances_ObjectIdentity = ObjectIdentity
ibmLesBusMIBCompliances = _IbmLesBusMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 4, 2)
)
_IbmLesBusMIBCompliance_ObjectIdentity = ObjectIdentity
ibmLesBusMIBCompliance = _IbmLesBusMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 118, 1, 2, 1, 1, 4, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IBM-LES-BUS-MIB",
    **{"ibmLesBusMIB": ibmLesBusMIB,
       "ibmLesBusConfGroup": ibmLesBusConfGroup,
       "ibmLesBusConfTable": ibmLesBusConfTable,
       "ibmLesBusConfEntry": ibmLesBusConfEntry,
       "atmDevNum": atmDevNum,
       "useBurnedInEsi": useBurnedInEsi,
       "configuredEsi": configuredEsi,
       "configuredSelector": configuredSelector,
       "leArpResponseDest": leArpResponseDest,
       "use2ControlDistributeVccs": use2ControlDistributeVccs,
       "use2MulticastForwardVccs": use2MulticastForwardVccs,
       "validateBestEffortPcr": validateBestEffortPcr,
       "controlDirectMaxReservedBw": controlDirectMaxReservedBw,
       "multicastSendMaxReservedBw": multicastSendMaxReservedBw,
       "controlDistributeVccType": controlDistributeVccType,
       "controlDistributePcr": controlDistributePcr,
       "controlDistributeScr": controlDistributeScr,
       "multicastForwardVccType": multicastForwardVccType,
       "multicastForwardPcr": multicastForwardPcr,
       "multicastForwardScr": multicastForwardScr,
       "validateJoinsWithLecs": validateJoinsWithLecs,
       "redundancyEnabled": redundancyEnabled,
       "redundancyRole": redundancyRole,
       "redundancyAtmAddr": redundancyAtmAddr,
       "bmonEnabled": bmonEnabled,
       "numTopMacs": numTopMacs,
       "sampleDuration": sampleDuration,
       "interSampleTime": interSampleTime,
       "sampleRate": sampleRate,
       "busMode": busMode,
       "ibmLesBusStatGroup": ibmLesBusStatGroup,
       "ibmLesBusStatTable": ibmLesBusStatTable,
       "ibmLesBusStatEntry": ibmLesBusStatEntry,
       "redundancyVccRefused": redundancyVccRefused,
       "redundancyVccReleased": redundancyVccReleased,
       "redundancyVccFailure": redundancyVccFailure,
       "ibmBusMonStatGroup": ibmBusMonStatGroup,
       "bmonSampleInfoTable": bmonSampleInfoTable,
       "bmonSampleInfoEntry": bmonSampleInfoEntry,
       "bmonSampleStartTime": bmonSampleStartTime,
       "bmonSampleDuration": bmonSampleDuration,
       "bmonNumTopMacs": bmonNumTopMacs,
       "bmonReceivedFrames": bmonReceivedFrames,
       "bmonSampledFrames": bmonSampledFrames,
       "bmonSamplingRate": bmonSamplingRate,
       "bmonStatTable": bmonStatTable,
       "bmonStatEntry": bmonStatEntry,
       "bmonTopNRank": bmonTopNRank,
       "bmonTopNSrcMacAddr": bmonTopNSrcMacAddr,
       "bmonTopNLecAtmAddr": bmonTopNLecAtmAddr,
       "bmonTopNFramesSampled": bmonTopNFramesSampled,
       "ibmLesBusMIBConformance": ibmLesBusMIBConformance,
       "ibmLesBusMIBGroups": ibmLesBusMIBGroups,
       "ibmLesBusCConfGroup": ibmLesBusCConfGroup,
       "ibmLesBusCStatGroup": ibmLesBusCStatGroup,
       "ibmBusMonCStatGroup": ibmBusMonCStatGroup,
       "ibmLesBusMIBCompliances": ibmLesBusMIBCompliances,
       "ibmLesBusMIBCompliance": ibmLesBusMIBCompliance}
)
