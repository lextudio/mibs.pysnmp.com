# SNMP MIB module (RADIO-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADIO-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:21 2024
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

(dot1agCfmMepEntry,) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "dot1agCfmMepEntry")

(ieee8021QBridgeTpFdbEntry,) = mibBuilder.importSymbols(
    "IEEE8021-Q-BRIDGE-MIB",
    "ieee8021QBridgeTpFdbEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("no-alarm", 5),
          ("warning", 4))
    )



class AlarmType(Integer32, TextualConvention):
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cfm-mep-defect", 5),
          ("cinr-out-of-range", 11),
          ("link-down", 1),
          ("loopback-active", 6),
          ("lowest-modulation", 12),
          ("poe-incompatible", 9),
          ("pow-low", 4),
          ("ql-eec1-or-worse", 8),
          ("rssi-out-of-range", 10),
          ("synthesizer-unlock", 3),
          ("temperature-out-of-range", 2),
          ("tx-mute", 7))
    )



# MIB Managed Objects in the order of their OIDs

_RadioBridgeRoot_ObjectIdentity = ObjectIdentity
radioBridgeRoot = _RadioBridgeRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926)
)
_RadioBridgeSystem_ObjectIdentity = ObjectIdentity
radioBridgeSystem = _RadioBridgeSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 1)
)
_RbSysVoltage_Type = Integer32
_RbSysVoltage_Object = MibScalar
rbSysVoltage = _RbSysVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 1),
    _RbSysVoltage_Type()
)
rbSysVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysVoltage.setStatus("current")
_RbSysTemperature_Type = Integer32
_RbSysTemperature_Object = MibScalar
rbSysTemperature = _RbSysTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 2),
    _RbSysTemperature_Type()
)
rbSysTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysTemperature.setStatus("current")
_RbSysSaveConfiguration_Type = Integer32
_RbSysSaveConfiguration_Object = MibScalar
rbSysSaveConfiguration = _RbSysSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 3),
    _RbSysSaveConfiguration_Type()
)
rbSysSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSysSaveConfiguration.setStatus("current")
_RbSysReset_Type = Integer32
_RbSysReset_Object = MibScalar
rbSysReset = _RbSysReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 4),
    _RbSysReset_Type()
)
rbSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSysReset.setStatus("current")
_RbSwBank1Version_Type = DisplayString
_RbSwBank1Version_Object = MibScalar
rbSwBank1Version = _RbSwBank1Version_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 5),
    _RbSwBank1Version_Type()
)
rbSwBank1Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank1Version.setStatus("current")
_RbSwBank2Version_Type = DisplayString
_RbSwBank2Version_Object = MibScalar
rbSwBank2Version = _RbSwBank2Version_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 6),
    _RbSwBank2Version_Type()
)
rbSwBank2Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank2Version.setStatus("current")


class _RbSwBank1Running_Type(Integer32):
    """Custom type rbSwBank1Running based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRunning", 1),
          ("running", 2),
          ("running-wait-accept", 3))
    )


_RbSwBank1Running_Type.__name__ = "Integer32"
_RbSwBank1Running_Object = MibScalar
rbSwBank1Running = _RbSwBank1Running_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 7),
    _RbSwBank1Running_Type()
)
rbSwBank1Running.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank1Running.setStatus("current")


class _RbSwBank2Running_Type(Integer32):
    """Custom type rbSwBank2Running based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRunning", 1),
          ("running", 2),
          ("running-wait-accept", 3))
    )


_RbSwBank2Running_Type.__name__ = "Integer32"
_RbSwBank2Running_Object = MibScalar
rbSwBank2Running = _RbSwBank2Running_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 8),
    _RbSwBank2Running_Type()
)
rbSwBank2Running.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank2Running.setStatus("current")
_RbSwBank1ScheduledToRunNextReset_Type = TruthValue
_RbSwBank1ScheduledToRunNextReset_Object = MibScalar
rbSwBank1ScheduledToRunNextReset = _RbSwBank1ScheduledToRunNextReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 9),
    _RbSwBank1ScheduledToRunNextReset_Type()
)
rbSwBank1ScheduledToRunNextReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank1ScheduledToRunNextReset.setStatus("current")
_RbSwBank2ScheduledToRunNextReset_Type = TruthValue
_RbSwBank2ScheduledToRunNextReset_Object = MibScalar
rbSwBank2ScheduledToRunNextReset = _RbSwBank2ScheduledToRunNextReset_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 10),
    _RbSwBank2ScheduledToRunNextReset_Type()
)
rbSwBank2ScheduledToRunNextReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwBank2ScheduledToRunNextReset.setStatus("current")
_RbSystemUpAbsoluteTime_Type = Counter64
_RbSystemUpAbsoluteTime_Object = MibScalar
rbSystemUpAbsoluteTime = _RbSystemUpAbsoluteTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 11),
    _RbSystemUpAbsoluteTime_Type()
)
rbSystemUpAbsoluteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemUpAbsoluteTime.setStatus("current")


class _RbSystemAuthenticationMode_Type(Integer32):
    """Custom type rbSystemAuthenticationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("tacacs", 3))
    )


_RbSystemAuthenticationMode_Type.__name__ = "Integer32"
_RbSystemAuthenticationMode_Object = MibScalar
rbSystemAuthenticationMode = _RbSystemAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 12),
    _RbSystemAuthenticationMode_Type()
)
rbSystemAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemAuthenticationMode.setStatus("current")
_RbSystemAuthenticationSecret_Type = DisplayString
_RbSystemAuthenticationSecret_Object = MibScalar
rbSystemAuthenticationSecret = _RbSystemAuthenticationSecret_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 13),
    _RbSystemAuthenticationSecret_Type()
)
rbSystemAuthenticationSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSystemAuthenticationSecret.setStatus("current")


class _RbSystemCapabilities_Type(Bits):
    """Custom type rbSystemCapabilities based on Bits"""
    namedValues = NamedValues(
        ("nmsFtp", 0)
    )

_RbSystemCapabilities_Type.__name__ = "Bits"
_RbSystemCapabilities_Object = MibScalar
rbSystemCapabilities = _RbSystemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 14),
    _RbSystemCapabilities_Type()
)
rbSystemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSystemCapabilities.setStatus("current")
_RbDate_Type = DisplayString
_RbDate_Object = MibScalar
rbDate = _RbDate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 15),
    _RbDate_Type()
)
rbDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbDate.setStatus("current")
_RbTime_Type = DisplayString
_RbTime_Object = MibScalar
rbTime = _RbTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 1, 16),
    _RbTime_Type()
)
rbTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbTime.setStatus("current")
_RadioBridgeRf_ObjectIdentity = ObjectIdentity
radioBridgeRf = _RadioBridgeRf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 2)
)
_RbRfTable_Object = MibTable
rbRfTable = _RbRfTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1)
)
if mibBuilder.loadTexts:
    rbRfTable.setStatus("current")
_RbRfEntry_Object = MibTableRow
rbRfEntry = _RbRfEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1)
)
rbRfEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rfIndex"),
)
if mibBuilder.loadTexts:
    rbRfEntry.setStatus("current")
_RfIndex_Type = Integer32
_RfIndex_Object = MibTableColumn
rfIndex = _RfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 1),
    _RfIndex_Type()
)
rfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfIndex.setStatus("current")


class _RfNumOfChannels_Type(Integer32):
    """Custom type rfNumOfChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
    )


_RfNumOfChannels_Type.__name__ = "Integer32"
_RfNumOfChannels_Object = MibTableColumn
rfNumOfChannels = _RfNumOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 2),
    _RfNumOfChannels_Type()
)
rfNumOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfNumOfChannels.setStatus("current")


class _RfChannelWidth_Type(Integer32):
    """Custom type rfChannelWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfWidth250", 1),
          ("rfWidth500", 2))
    )


_RfChannelWidth_Type.__name__ = "Integer32"
_RfChannelWidth_Object = MibTableColumn
rfChannelWidth = _RfChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 3),
    _RfChannelWidth_Type()
)
rfChannelWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfChannelWidth.setStatus("current")
_RfOperationalFrequency_Type = Integer32
_RfOperationalFrequency_Object = MibTableColumn
rfOperationalFrequency = _RfOperationalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 4),
    _RfOperationalFrequency_Type()
)
rfOperationalFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfOperationalFrequency.setStatus("current")


class _RfRole_Type(Integer32):
    """Custom type rfRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfAuto", 3),
          ("rfMaster", 1),
          ("rfSlave", 2))
    )


_RfRole_Type.__name__ = "Integer32"
_RfRole_Object = MibTableColumn
rfRole = _RfRole_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 5),
    _RfRole_Type()
)
rfRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfRole.setStatus("current")


class _RfModeSelector_Type(Integer32):
    """Custom type rfModeSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfModeAdaptive", 1),
          ("rfModeAlign", 3),
          ("rfModeStatic", 2))
    )


_RfModeSelector_Type.__name__ = "Integer32"
_RfModeSelector_Object = MibTableColumn
rfModeSelector = _RfModeSelector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 6),
    _RfModeSelector_Type()
)
rfModeSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfModeSelector.setStatus("current")


class _RfModulationType_Type(Integer32):
    """Custom type rfModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfModulationQAM-16", 2),
          ("rfModulationQAM-64", 3),
          ("rfModulationQPSK", 1))
    )


_RfModulationType_Type.__name__ = "Integer32"
_RfModulationType_Object = MibTableColumn
rfModulationType = _RfModulationType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 7),
    _RfModulationType_Type()
)
rfModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfModulationType.setStatus("current")


class _RfNumOfSubchannels_Type(Integer32):
    """Custom type rfNumOfSubchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RfNumOfSubchannels_Type.__name__ = "Integer32"
_RfNumOfSubchannels_Object = MibTableColumn
rfNumOfSubchannels = _RfNumOfSubchannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 8),
    _RfNumOfSubchannels_Type()
)
rfNumOfSubchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfNumOfSubchannels.setStatus("current")


class _RfNumOfRepetitions_Type(Integer32):
    """Custom type rfNumOfRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_RfNumOfRepetitions_Type.__name__ = "Integer32"
_RfNumOfRepetitions_Object = MibTableColumn
rfNumOfRepetitions = _RfNumOfRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 9),
    _RfNumOfRepetitions_Type()
)
rfNumOfRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfNumOfRepetitions.setStatus("current")


class _RfFecRate_Type(Integer32):
    """Custom type rfFecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfFEC-05", 1),
          ("rfFEC-067", 2),
          ("rfFEC-08", 3))
    )


_RfFecRate_Type.__name__ = "Integer32"
_RfFecRate_Object = MibTableColumn
rfFecRate = _RfFecRate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 10),
    _RfFecRate_Type()
)
rfFecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfFecRate.setStatus("current")
_RfOperationalState_Type = TruthValue
_RfOperationalState_Object = MibTableColumn
rfOperationalState = _RfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 17),
    _RfOperationalState_Type()
)
rfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOperationalState.setStatus("current")
_RfAverageCinr_Type = Integer32
_RfAverageCinr_Object = MibTableColumn
rfAverageCinr = _RfAverageCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 18),
    _RfAverageCinr_Type()
)
rfAverageCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAverageCinr.setStatus("current")
_RfAverageRssi_Type = Integer32
_RfAverageRssi_Object = MibTableColumn
rfAverageRssi = _RfAverageRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 19),
    _RfAverageRssi_Type()
)
rfAverageRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAverageRssi.setStatus("current")


class _RfTxSynthLock_Type(Integer32):
    """Custom type rfTxSynthLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("txSynthLock", 1),
          ("txSynthUnlock", 0))
    )


_RfTxSynthLock_Type.__name__ = "Integer32"
_RfTxSynthLock_Object = MibTableColumn
rfTxSynthLock = _RfTxSynthLock_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 20),
    _RfTxSynthLock_Type()
)
rfTxSynthLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxSynthLock.setStatus("current")


class _RfRxSynthLock_Type(Integer32):
    """Custom type rfRxSynthLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rxSynthLock", 1),
          ("rxSynthUnlock", 0))
    )


_RfRxSynthLock_Type.__name__ = "Integer32"
_RfRxSynthLock_Object = MibTableColumn
rfRxSynthLock = _RfRxSynthLock_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 21),
    _RfRxSynthLock_Type()
)
rfRxSynthLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxSynthLock.setStatus("current")


class _RfRxLinkId_Type(Integer32):
    """Custom type rfRxLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RfRxLinkId_Type.__name__ = "Integer32"
_RfRxLinkId_Object = MibTableColumn
rfRxLinkId = _RfRxLinkId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 22),
    _RfRxLinkId_Type()
)
rfRxLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfRxLinkId.setStatus("current")


class _RfTxLinkId_Type(Integer32):
    """Custom type rfTxLinkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RfTxLinkId_Type.__name__ = "Integer32"
_RfTxLinkId_Object = MibTableColumn
rfTxLinkId = _RfTxLinkId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 23),
    _RfTxLinkId_Type()
)
rfTxLinkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxLinkId.setStatus("current")


class _RfTxState_Type(Integer32):
    """Custom type rfTxState based on Integer32"""
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
        *(("rf-foundCountdown", 3),
          ("rf-normal", 4),
          ("rf-searchCountdown", 2),
          ("rf-sync", 1))
    )


_RfTxState_Type.__name__ = "Integer32"
_RfTxState_Object = MibTableColumn
rfTxState = _RfTxState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 24),
    _RfTxState_Type()
)
rfTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTxState.setStatus("current")


class _RfRxState_Type(Integer32):
    """Custom type rfRxState based on Integer32"""
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
        *(("rf-foundCountdown", 3),
          ("rf-normal", 4),
          ("rf-searchCountdown", 2),
          ("rf-sync", 1))
    )


_RfRxState_Type.__name__ = "Integer32"
_RfRxState_Object = MibTableColumn
rfRxState = _RfRxState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 25),
    _RfRxState_Type()
)
rfRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRxState.setStatus("current")
_RfTemperature_Type = Integer32
_RfTemperature_Object = MibTableColumn
rfTemperature = _RfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 26),
    _RfTemperature_Type()
)
rfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfTemperature.setStatus("current")


class _RfAsymmetry_Type(Integer32):
    """Custom type rfAsymmetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rf-asymmetry-25tx-75rx", 1),
          ("rf-asymmetry-50tx-50rx", 2),
          ("rf-asymmetry-75tx-25rx", 3))
    )


_RfAsymmetry_Type.__name__ = "Integer32"
_RfAsymmetry_Object = MibTableColumn
rfAsymmetry = _RfAsymmetry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 27),
    _RfAsymmetry_Type()
)
rfAsymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAsymmetry.setStatus("current")


class _RfLowestModulationType_Type(Integer32):
    """Custom type rfLowestModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfModulationQAM-16", 2),
          ("rfModulationQAM-64", 3),
          ("rfModulationQPSK", 1))
    )


_RfLowestModulationType_Type.__name__ = "Integer32"
_RfLowestModulationType_Object = MibTableColumn
rfLowestModulationType = _RfLowestModulationType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 30),
    _RfLowestModulationType_Type()
)
rfLowestModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestModulationType.setStatus("current")


class _RfLowestNumOfSubchannels_Type(Integer32):
    """Custom type rfLowestNumOfSubchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RfLowestNumOfSubchannels_Type.__name__ = "Integer32"
_RfLowestNumOfSubchannels_Object = MibTableColumn
rfLowestNumOfSubchannels = _RfLowestNumOfSubchannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 31),
    _RfLowestNumOfSubchannels_Type()
)
rfLowestNumOfSubchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestNumOfSubchannels.setStatus("current")


class _RfLowestNumOfRepetitions_Type(Integer32):
    """Custom type rfLowestNumOfRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_RfLowestNumOfRepetitions_Type.__name__ = "Integer32"
_RfLowestNumOfRepetitions_Object = MibTableColumn
rfLowestNumOfRepetitions = _RfLowestNumOfRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 32),
    _RfLowestNumOfRepetitions_Type()
)
rfLowestNumOfRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestNumOfRepetitions.setStatus("current")


class _RfLowestFecRate_Type(Integer32):
    """Custom type rfLowestFecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfFEC-05", 1),
          ("rfFEC-067", 2),
          ("rfFEC-08", 3))
    )


_RfLowestFecRate_Type.__name__ = "Integer32"
_RfLowestFecRate_Object = MibTableColumn
rfLowestFecRate = _RfLowestFecRate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 33),
    _RfLowestFecRate_Type()
)
rfLowestFecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLowestFecRate.setStatus("current")
_RfTxMute_Type = TruthValue
_RfTxMute_Object = MibTableColumn
rfTxMute = _RfTxMute_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 34),
    _RfTxMute_Type()
)
rfTxMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxMute.setStatus("current")


class _RfRoleStatus_Type(Integer32):
    """Custom type rfRoleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfAuto", 3),
          ("rfMaster", 1),
          ("rfSlave", 2))
    )


_RfRoleStatus_Type.__name__ = "Integer32"
_RfRoleStatus_Object = MibTableColumn
rfRoleStatus = _RfRoleStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 35),
    _RfRoleStatus_Type()
)
rfRoleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfRoleStatus.setStatus("current")


class _RfLoopModeSelector_Type(Integer32):
    """Custom type rfLoopModeSelector based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfLoopDisabled", 1),
          ("rfLoopInternalMacSwap", 2))
    )


_RfLoopModeSelector_Type.__name__ = "Integer32"
_RfLoopModeSelector_Object = MibTableColumn
rfLoopModeSelector = _RfLoopModeSelector_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 36),
    _RfLoopModeSelector_Type()
)
rfLoopModeSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopModeSelector.setStatus("current")


class _RfLoopModulationType_Type(Integer32):
    """Custom type rfLoopModulationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfModulationQAM-16", 2),
          ("rfModulationQAM-64", 3),
          ("rfModulationQPSK", 1))
    )


_RfLoopModulationType_Type.__name__ = "Integer32"
_RfLoopModulationType_Object = MibTableColumn
rfLoopModulationType = _RfLoopModulationType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 37),
    _RfLoopModulationType_Type()
)
rfLoopModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopModulationType.setStatus("current")


class _RfLoopNumOfSubchannels_Type(Integer32):
    """Custom type rfLoopNumOfSubchannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RfLoopNumOfSubchannels_Type.__name__ = "Integer32"
_RfLoopNumOfSubchannels_Object = MibTableColumn
rfLoopNumOfSubchannels = _RfLoopNumOfSubchannels_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 38),
    _RfLoopNumOfSubchannels_Type()
)
rfLoopNumOfSubchannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopNumOfSubchannels.setStatus("current")


class _RfLoopNumOfRepetitions_Type(Integer32):
    """Custom type rfLoopNumOfRepetitions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
    )


_RfLoopNumOfRepetitions_Type.__name__ = "Integer32"
_RfLoopNumOfRepetitions_Object = MibTableColumn
rfLoopNumOfRepetitions = _RfLoopNumOfRepetitions_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 39),
    _RfLoopNumOfRepetitions_Type()
)
rfLoopNumOfRepetitions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopNumOfRepetitions.setStatus("current")


class _RfLoopFecRate_Type(Integer32):
    """Custom type rfLoopFecRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rfFEC-05", 1),
          ("rfFEC-067", 2),
          ("rfFEC-08", 3))
    )


_RfLoopFecRate_Type.__name__ = "Integer32"
_RfLoopFecRate_Object = MibTableColumn
rfLoopFecRate = _RfLoopFecRate_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 40),
    _RfLoopFecRate_Type()
)
rfLoopFecRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopFecRate.setStatus("current")
_RfLoopTimeout_Type = Integer32
_RfLoopTimeout_Object = MibTableColumn
rfLoopTimeout = _RfLoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 41),
    _RfLoopTimeout_Type()
)
rfLoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopTimeout.setStatus("current")


class _RfTxPower_Type(Integer32):
    """Custom type rfTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-35, 8),
    )


_RfTxPower_Type.__name__ = "Integer32"
_RfTxPower_Object = MibTableColumn
rfTxPower = _RfTxPower_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 42),
    _RfTxPower_Type()
)
rfTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxPower.setStatus("current")


class _RfTxMuteTimeout_Type(Integer32):
    """Custom type rfTxMuteTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_RfTxMuteTimeout_Type.__name__ = "Integer32"
_RfTxMuteTimeout_Object = MibTableColumn
rfTxMuteTimeout = _RfTxMuteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 43),
    _RfTxMuteTimeout_Type()
)
rfTxMuteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfTxMuteTimeout.setStatus("current")


class _RfAlignmentStatus_Type(Integer32):
    """Custom type rfAlignmentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rfAlignmentActive", 1),
          ("rfAlignmentInactive", 0))
    )


_RfAlignmentStatus_Type.__name__ = "Integer32"
_RfAlignmentStatus_Object = MibTableColumn
rfAlignmentStatus = _RfAlignmentStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 44),
    _RfAlignmentStatus_Type()
)
rfAlignmentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfAlignmentStatus.setStatus("current")


class _RfLoopDirection_Type(Integer32):
    """Custom type rfLoopDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rfLoop-rx", 2),
          ("rfLoop-tx", 1))
    )


_RfLoopDirection_Type.__name__ = "Integer32"
_RfLoopDirection_Object = MibTableColumn
rfLoopDirection = _RfLoopDirection_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 1, 1, 45),
    _RfLoopDirection_Type()
)
rfLoopDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rfLoopDirection.setStatus("current")
_RbRfStatisticsTable_Object = MibTable
rbRfStatisticsTable = _RbRfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2)
)
if mibBuilder.loadTexts:
    rbRfStatisticsTable.setStatus("current")
_RbRfStatisticsEntry_Object = MibTableRow
rbRfStatisticsEntry = _RbRfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1)
)
rbRfStatisticsEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rfIndex"),
)
if mibBuilder.loadTexts:
    rbRfStatisticsEntry.setStatus("current")
_RfInOctets_Type = Counter64
_RfInOctets_Object = MibTableColumn
rfInOctets = _RfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 1),
    _RfInOctets_Type()
)
rfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInOctets.setStatus("current")
_RfInIdleOctets_Type = Counter64
_RfInIdleOctets_Object = MibTableColumn
rfInIdleOctets = _RfInIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 2),
    _RfInIdleOctets_Type()
)
rfInIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInIdleOctets.setStatus("current")
_RfInGoodOctets_Type = Counter64
_RfInGoodOctets_Object = MibTableColumn
rfInGoodOctets = _RfInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 3),
    _RfInGoodOctets_Type()
)
rfInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInGoodOctets.setStatus("current")
_RfInErroredOctets_Type = Counter64
_RfInErroredOctets_Object = MibTableColumn
rfInErroredOctets = _RfInErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 4),
    _RfInErroredOctets_Type()
)
rfInErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInErroredOctets.setStatus("current")
_RfOutOctets_Type = Counter64
_RfOutOctets_Object = MibTableColumn
rfOutOctets = _RfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 5),
    _RfOutOctets_Type()
)
rfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutOctets.setStatus("current")
_RfOutIdleOctets_Type = Counter64
_RfOutIdleOctets_Object = MibTableColumn
rfOutIdleOctets = _RfOutIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 6),
    _RfOutIdleOctets_Type()
)
rfOutIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutIdleOctets.setStatus("current")
_RfInPkts_Type = Counter64
_RfInPkts_Object = MibTableColumn
rfInPkts = _RfInPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 7),
    _RfInPkts_Type()
)
rfInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInPkts.setStatus("current")
_RfInGoodPkts_Type = Counter64
_RfInGoodPkts_Object = MibTableColumn
rfInGoodPkts = _RfInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 8),
    _RfInGoodPkts_Type()
)
rfInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInGoodPkts.setStatus("current")
_RfInErroredPkts_Type = Counter64
_RfInErroredPkts_Object = MibTableColumn
rfInErroredPkts = _RfInErroredPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 9),
    _RfInErroredPkts_Type()
)
rfInErroredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInErroredPkts.setStatus("current")
_RfInLostPkts_Type = Counter64
_RfInLostPkts_Object = MibTableColumn
rfInLostPkts = _RfInLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 10),
    _RfInLostPkts_Type()
)
rfInLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfInLostPkts.setStatus("current")
_RfOutPkts_Type = Counter64
_RfOutPkts_Object = MibTableColumn
rfOutPkts = _RfOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 11),
    _RfOutPkts_Type()
)
rfOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfOutPkts.setStatus("current")
_RfMinCinr_Type = Counter64
_RfMinCinr_Object = MibTableColumn
rfMinCinr = _RfMinCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 15),
    _RfMinCinr_Type()
)
rfMinCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinCinr.setStatus("current")
_RfMaxCinr_Type = Counter64
_RfMaxCinr_Object = MibTableColumn
rfMaxCinr = _RfMaxCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 16),
    _RfMaxCinr_Type()
)
rfMaxCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxCinr.setStatus("current")
_RfMinRssi_Type = Counter64
_RfMinRssi_Object = MibTableColumn
rfMinRssi = _RfMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 17),
    _RfMinRssi_Type()
)
rfMinRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinRssi.setStatus("current")
_RfMaxRssi_Type = Counter64
_RfMaxRssi_Object = MibTableColumn
rfMaxRssi = _RfMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 18),
    _RfMaxRssi_Type()
)
rfMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxRssi.setStatus("current")
_RfMinModulation_Type = Counter64
_RfMinModulation_Object = MibTableColumn
rfMinModulation = _RfMinModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 19),
    _RfMinModulation_Type()
)
rfMinModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMinModulation.setStatus("current")
_RfMaxModulation_Type = Counter64
_RfMaxModulation_Object = MibTableColumn
rfMaxModulation = _RfMaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 20),
    _RfMaxModulation_Type()
)
rfMaxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfMaxModulation.setStatus("current")
_RfValid_Type = TruthValue
_RfValid_Object = MibTableColumn
rfValid = _RfValid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 21),
    _RfValid_Type()
)
rfValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfValid.setStatus("current")
_RfArqInLoss_Type = Counter64
_RfArqInLoss_Object = MibTableColumn
rfArqInLoss = _RfArqInLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 22),
    _RfArqInLoss_Type()
)
rfArqInLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfArqInLoss.setStatus("current")
_RfArqOutLoss_Type = Counter64
_RfArqOutLoss_Object = MibTableColumn
rfArqOutLoss = _RfArqOutLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 2, 1, 23),
    _RfArqOutLoss_Type()
)
rfArqOutLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfArqOutLoss.setStatus("current")
_RbRfStatisticsDaysTable_Object = MibTable
rbRfStatisticsDaysTable = _RbRfStatisticsDaysTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3)
)
if mibBuilder.loadTexts:
    rbRfStatisticsDaysTable.setStatus("current")
_RbRfStatisticsDaysEntry_Object = MibTableRow
rbRfStatisticsDaysEntry = _RbRfStatisticsDaysEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1)
)
rbRfStatisticsDaysEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rfIndex"),
    (0, "RADIO-BRIDGE-MIB", "rfDayIndex"),
)
if mibBuilder.loadTexts:
    rbRfStatisticsDaysEntry.setStatus("current")
_RfDaysInOctets_Type = Counter64
_RfDaysInOctets_Object = MibTableColumn
rfDaysInOctets = _RfDaysInOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 1),
    _RfDaysInOctets_Type()
)
rfDaysInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInOctets.setStatus("current")
_RfDaysInIdleOctets_Type = Counter64
_RfDaysInIdleOctets_Object = MibTableColumn
rfDaysInIdleOctets = _RfDaysInIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 2),
    _RfDaysInIdleOctets_Type()
)
rfDaysInIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInIdleOctets.setStatus("current")
_RfDaysInGoodOctets_Type = Counter64
_RfDaysInGoodOctets_Object = MibTableColumn
rfDaysInGoodOctets = _RfDaysInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 3),
    _RfDaysInGoodOctets_Type()
)
rfDaysInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInGoodOctets.setStatus("current")
_RfDaysInErroredOctets_Type = Counter64
_RfDaysInErroredOctets_Object = MibTableColumn
rfDaysInErroredOctets = _RfDaysInErroredOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 4),
    _RfDaysInErroredOctets_Type()
)
rfDaysInErroredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInErroredOctets.setStatus("current")
_RfDaysOutOctets_Type = Counter64
_RfDaysOutOctets_Object = MibTableColumn
rfDaysOutOctets = _RfDaysOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 5),
    _RfDaysOutOctets_Type()
)
rfDaysOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysOutOctets.setStatus("current")
_RfDaysOutIdleOctets_Type = Counter64
_RfDaysOutIdleOctets_Object = MibTableColumn
rfDaysOutIdleOctets = _RfDaysOutIdleOctets_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 6),
    _RfDaysOutIdleOctets_Type()
)
rfDaysOutIdleOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysOutIdleOctets.setStatus("current")
_RfDaysInPkts_Type = Counter64
_RfDaysInPkts_Object = MibTableColumn
rfDaysInPkts = _RfDaysInPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 7),
    _RfDaysInPkts_Type()
)
rfDaysInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInPkts.setStatus("current")
_RfDaysInGoodPkts_Type = Counter64
_RfDaysInGoodPkts_Object = MibTableColumn
rfDaysInGoodPkts = _RfDaysInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 8),
    _RfDaysInGoodPkts_Type()
)
rfDaysInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInGoodPkts.setStatus("current")
_RfDaysInErroredPkts_Type = Counter64
_RfDaysInErroredPkts_Object = MibTableColumn
rfDaysInErroredPkts = _RfDaysInErroredPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 9),
    _RfDaysInErroredPkts_Type()
)
rfDaysInErroredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInErroredPkts.setStatus("current")
_RfDaysInLostPkts_Type = Counter64
_RfDaysInLostPkts_Object = MibTableColumn
rfDaysInLostPkts = _RfDaysInLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 10),
    _RfDaysInLostPkts_Type()
)
rfDaysInLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysInLostPkts.setStatus("current")
_RfDaysOutPkts_Type = Counter64
_RfDaysOutPkts_Object = MibTableColumn
rfDaysOutPkts = _RfDaysOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 11),
    _RfDaysOutPkts_Type()
)
rfDaysOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysOutPkts.setStatus("current")
_RfDaysMinCinr_Type = Counter64
_RfDaysMinCinr_Object = MibTableColumn
rfDaysMinCinr = _RfDaysMinCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 15),
    _RfDaysMinCinr_Type()
)
rfDaysMinCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinCinr.setStatus("current")
_RfDaysMaxCinr_Type = Counter64
_RfDaysMaxCinr_Object = MibTableColumn
rfDaysMaxCinr = _RfDaysMaxCinr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 16),
    _RfDaysMaxCinr_Type()
)
rfDaysMaxCinr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxCinr.setStatus("current")
_RfDaysMinRssi_Type = Counter64
_RfDaysMinRssi_Object = MibTableColumn
rfDaysMinRssi = _RfDaysMinRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 17),
    _RfDaysMinRssi_Type()
)
rfDaysMinRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinRssi.setStatus("current")
_RfDaysMaxRssi_Type = Counter64
_RfDaysMaxRssi_Object = MibTableColumn
rfDaysMaxRssi = _RfDaysMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 18),
    _RfDaysMaxRssi_Type()
)
rfDaysMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxRssi.setStatus("current")
_RfDaysMinModulation_Type = Counter64
_RfDaysMinModulation_Object = MibTableColumn
rfDaysMinModulation = _RfDaysMinModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 19),
    _RfDaysMinModulation_Type()
)
rfDaysMinModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMinModulation.setStatus("current")
_RfDaysMaxModulation_Type = Counter64
_RfDaysMaxModulation_Object = MibTableColumn
rfDaysMaxModulation = _RfDaysMaxModulation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 20),
    _RfDaysMaxModulation_Type()
)
rfDaysMaxModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysMaxModulation.setStatus("current")
_RfDaysValid_Type = TruthValue
_RfDaysValid_Object = MibTableColumn
rfDaysValid = _RfDaysValid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 21),
    _RfDaysValid_Type()
)
rfDaysValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysValid.setStatus("current")
_RfDaysArqInLoss_Type = Counter64
_RfDaysArqInLoss_Object = MibTableColumn
rfDaysArqInLoss = _RfDaysArqInLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 22),
    _RfDaysArqInLoss_Type()
)
rfDaysArqInLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysArqInLoss.setStatus("current")
_RfDaysArqOutLoss_Type = Counter64
_RfDaysArqOutLoss_Object = MibTableColumn
rfDaysArqOutLoss = _RfDaysArqOutLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 23),
    _RfDaysArqOutLoss_Type()
)
rfDaysArqOutLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rfDaysArqOutLoss.setStatus("current")
_RfDayIndex_Type = Integer32
_RfDayIndex_Object = MibTableColumn
rfDayIndex = _RfDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 50),
    _RfDayIndex_Type()
)
rfDayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfDayIndex.setStatus("current")
_RfDaysStart_Type = TimeTicks
_RfDaysStart_Object = MibTableColumn
rfDaysStart = _RfDaysStart_Object(
    (1, 3, 6, 1, 4, 1, 31926, 2, 3, 1, 51),
    _RfDaysStart_Type()
)
rfDaysStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rfDaysStart.setStatus("current")
_RadioBridgeTraps_ObjectIdentity = ObjectIdentity
radioBridgeTraps = _RadioBridgeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 3)
)
_RadioBridgeRefClock_ObjectIdentity = ObjectIdentity
radioBridgeRefClock = _RadioBridgeRefClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 4)
)
_RbRefClockTable_Object = MibTable
rbRefClockTable = _RbRefClockTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1)
)
if mibBuilder.loadTexts:
    rbRefClockTable.setStatus("current")
_RbRefClockEntry_Object = MibTableRow
rbRefClockEntry = _RbRefClockEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1)
)
rbRefClockEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rbRefClockEntry.setStatus("current")


class _RefClockPrio_Type(Integer32):
    """Custom type refClockPrio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RefClockPrio_Type.__name__ = "Integer32"
_RefClockPrio_Object = MibTableColumn
refClockPrio = _RefClockPrio_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 1),
    _RefClockPrio_Type()
)
refClockPrio.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockPrio.setStatus("current")


class _RefClockStatus_Type(Integer32):
    """Custom type refClockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup-1", 2),
          ("backup-2", 3),
          ("backup-3", 4),
          ("down", 0))
    )


_RefClockStatus_Type.__name__ = "Integer32"
_RefClockStatus_Object = MibTableColumn
refClockStatus = _RefClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 2),
    _RefClockStatus_Type()
)
refClockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refClockStatus.setStatus("current")


class _RefClockQualityLevelActual_Type(Integer32):
    """Custom type refClockQualityLevelActual based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RefClockQualityLevelActual_Type.__name__ = "Integer32"
_RefClockQualityLevelActual_Object = MibTableColumn
refClockQualityLevelActual = _RefClockQualityLevelActual_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 3),
    _RefClockQualityLevelActual_Type()
)
refClockQualityLevelActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refClockQualityLevelActual.setStatus("current")


class _RefClockQualityLevelConfig_Type(Integer32):
    """Custom type refClockQualityLevelConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RefClockQualityLevelConfig_Type.__name__ = "Integer32"
_RefClockQualityLevelConfig_Object = MibTableColumn
refClockQualityLevelConfig = _RefClockQualityLevelConfig_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 4),
    _RefClockQualityLevelConfig_Type()
)
refClockQualityLevelConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockQualityLevelConfig.setStatus("current")
_RefClockQualityLevelMode_Type = TruthValue
_RefClockQualityLevelMode_Object = MibTableColumn
refClockQualityLevelMode = _RefClockQualityLevelMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 5),
    _RefClockQualityLevelMode_Type()
)
refClockQualityLevelMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockQualityLevelMode.setStatus("current")
_RefClockSsmCvid_Type = Integer32
_RefClockSsmCvid_Object = MibTableColumn
refClockSsmCvid = _RefClockSsmCvid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 6),
    _RefClockSsmCvid_Type()
)
refClockSsmCvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    refClockSsmCvid.setStatus("current")
_RefClockRowStatus_Type = RowStatus
_RefClockRowStatus_Object = MibTableColumn
refClockRowStatus = _RefClockRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 4, 1, 1, 7),
    _RefClockRowStatus_Type()
)
refClockRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    refClockRowStatus.setStatus("current")
_RadioBridgeEthernet_ObjectIdentity = ObjectIdentity
radioBridgeEthernet = _RadioBridgeEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 5)
)
_RbEthernetTable_Object = MibTable
rbEthernetTable = _RbEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1)
)
if mibBuilder.loadTexts:
    rbEthernetTable.setStatus("current")
_RbEthernetEntry_Object = MibTableRow
rbEthernetEntry = _RbEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1)
)
rbEthernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rbEthernetEntry.setStatus("current")


class _EthernetAlarmPropagation_Type(Integer32):
    """Custom type ethernetAlarmPropagation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backward", 1),
          ("both-direct", 3),
          ("disabled", 0),
          ("forward", 2))
    )


_EthernetAlarmPropagation_Type.__name__ = "Integer32"
_EthernetAlarmPropagation_Object = MibTableColumn
ethernetAlarmPropagation = _EthernetAlarmPropagation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 2),
    _EthernetAlarmPropagation_Type()
)
ethernetAlarmPropagation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetAlarmPropagation.setStatus("current")


class _EthernetLoopMode_Type(Integer32):
    """Custom type ethernetLoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("external", 1),
          ("external-mac-swap", 2),
          ("internal", 3),
          ("internal-mac-swap", 4))
    )


_EthernetLoopMode_Type.__name__ = "Integer32"
_EthernetLoopMode_Object = MibTableColumn
ethernetLoopMode = _EthernetLoopMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 3),
    _EthernetLoopMode_Type()
)
ethernetLoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLoopMode.setStatus("current")
_EthernetLoopTimeout_Type = Integer32
_EthernetLoopTimeout_Object = MibTableColumn
ethernetLoopTimeout = _EthernetLoopTimeout_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 4),
    _EthernetLoopTimeout_Type()
)
ethernetLoopTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLoopTimeout.setStatus("current")


class _EthernetNetworkType_Type(Integer32):
    """Custom type ethernetNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("customer-nni", 3),
          ("customer-uni", 2),
          ("provider-nni", 1))
    )


_EthernetNetworkType_Type.__name__ = "Integer32"
_EthernetNetworkType_Object = MibTableColumn
ethernetNetworkType = _EthernetNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 5),
    _EthernetNetworkType_Type()
)
ethernetNetworkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetNetworkType.setStatus("current")
_EthernetPcpWriteProfileId_Type = Integer32
_EthernetPcpWriteProfileId_Object = MibTableColumn
ethernetPcpWriteProfileId = _EthernetPcpWriteProfileId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 6),
    _EthernetPcpWriteProfileId_Type()
)
ethernetPcpWriteProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetPcpWriteProfileId.setStatus("current")


class _EthernetClassifierMode_Type(Integer32):
    """Custom type ethernetClassifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("classifier-mode-dscp", 1),
          ("classifier-mode-pcp-dscp", 2))
    )


_EthernetClassifierMode_Type.__name__ = "Integer32"
_EthernetClassifierMode_Object = MibTableColumn
ethernetClassifierMode = _EthernetClassifierMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 5, 1, 1, 7),
    _EthernetClassifierMode_Type()
)
ethernetClassifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetClassifierMode.setStatus("current")
_RadioBridgeQosClassifier_ObjectIdentity = ObjectIdentity
radioBridgeQosClassifier = _RadioBridgeQosClassifier_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 6)
)
_RbClassifierCosTable_Object = MibTable
rbClassifierCosTable = _RbClassifierCosTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1)
)
if mibBuilder.loadTexts:
    rbClassifierCosTable.setStatus("current")
_RbClassifierCosEntry_Object = MibTableRow
rbClassifierCosEntry = _RbClassifierCosEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1)
)
rbClassifierCosEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "classifierCosId"),
)
if mibBuilder.loadTexts:
    rbClassifierCosEntry.setStatus("current")


class _ClassifierCosId_Type(Integer32):
    """Custom type classifierCosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_ClassifierCosId_Type.__name__ = "Integer32"
_ClassifierCosId_Object = MibTableColumn
classifierCosId = _ClassifierCosId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 1),
    _ClassifierCosId_Type()
)
classifierCosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    classifierCosId.setStatus("current")
_ClassifierCosPortList_Type = OctetString
_ClassifierCosPortList_Object = MibTableColumn
classifierCosPortList = _ClassifierCosPortList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 2),
    _ClassifierCosPortList_Type()
)
classifierCosPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPortList.setStatus("current")


class _ClassifierCosPrecedence_Type(Integer32):
    """Custom type classifierCosPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ClassifierCosPrecedence_Type.__name__ = "Integer32"
_ClassifierCosPrecedence_Object = MibTableColumn
classifierCosPrecedence = _ClassifierCosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 3),
    _ClassifierCosPrecedence_Type()
)
classifierCosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPrecedence.setStatus("current")
_ClassifierCosVidList_Type = OctetString
_ClassifierCosVidList_Object = MibTableColumn
classifierCosVidList = _ClassifierCosVidList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 4),
    _ClassifierCosVidList_Type()
)
classifierCosVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosVidList.setStatus("current")
_ClassifierCosPcpList_Type = OctetString
_ClassifierCosPcpList_Object = MibTableColumn
classifierCosPcpList = _ClassifierCosPcpList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 5),
    _ClassifierCosPcpList_Type()
)
classifierCosPcpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPcpList.setStatus("current")


class _ClassifierCosCos_Type(Integer32):
    """Custom type classifierCosCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ClassifierCosCos_Type.__name__ = "Integer32"
_ClassifierCosCos_Object = MibTableColumn
classifierCosCos = _ClassifierCosCos_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 6),
    _ClassifierCosCos_Type()
)
classifierCosCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosCos.setStatus("current")


class _ClassifierCosIpCosType_Type(Integer32):
    """Custom type classifierCosIpCosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-cos-dont-care", 3),
          ("ip-cos-dscp", 1),
          ("ip-cos-mpls", 2))
    )


_ClassifierCosIpCosType_Type.__name__ = "Integer32"
_ClassifierCosIpCosType_Object = MibTableColumn
classifierCosIpCosType = _ClassifierCosIpCosType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 7),
    _ClassifierCosIpCosType_Type()
)
classifierCosIpCosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosIpCosType.setStatus("current")
_ClassifierCosIpCosList_Type = OctetString
_ClassifierCosIpCosList_Object = MibTableColumn
classifierCosIpCosList = _ClassifierCosIpCosList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 8),
    _ClassifierCosIpCosList_Type()
)
classifierCosIpCosList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosIpCosList.setStatus("current")
_ClassifierCosRowStatus_Type = RowStatus
_ClassifierCosRowStatus_Object = MibTableColumn
classifierCosRowStatus = _ClassifierCosRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 9),
    _ClassifierCosRowStatus_Type()
)
classifierCosRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosRowStatus.setStatus("current")


class _ClassifierCosPacketType_Type(Integer32):
    """Custom type classifierCosPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("non-unicast", 2),
          ("unicast", 1))
    )


_ClassifierCosPacketType_Type.__name__ = "Integer32"
_ClassifierCosPacketType_Object = MibTableColumn
classifierCosPacketType = _ClassifierCosPacketType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 1, 1, 10),
    _ClassifierCosPacketType_Type()
)
classifierCosPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierCosPacketType.setStatus("current")
_RbClassifierEvcTable_Object = MibTable
rbClassifierEvcTable = _RbClassifierEvcTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2)
)
if mibBuilder.loadTexts:
    rbClassifierEvcTable.setStatus("current")
_RbClassifierEvcEntry_Object = MibTableRow
rbClassifierEvcEntry = _RbClassifierEvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1)
)
rbClassifierEvcEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "classifierEvcId"),
)
if mibBuilder.loadTexts:
    rbClassifierEvcEntry.setStatus("current")


class _ClassifierEvcId_Type(Integer32):
    """Custom type classifierEvcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_ClassifierEvcId_Type.__name__ = "Integer32"
_ClassifierEvcId_Object = MibTableColumn
classifierEvcId = _ClassifierEvcId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 1),
    _ClassifierEvcId_Type()
)
classifierEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    classifierEvcId.setStatus("current")
_ClassifierEvcPortList_Type = OctetString
_ClassifierEvcPortList_Object = MibTableColumn
classifierEvcPortList = _ClassifierEvcPortList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 2),
    _ClassifierEvcPortList_Type()
)
classifierEvcPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPortList.setStatus("current")


class _ClassifierEvcPrecedence_Type(Integer32):
    """Custom type classifierEvcPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ClassifierEvcPrecedence_Type.__name__ = "Integer32"
_ClassifierEvcPrecedence_Object = MibTableColumn
classifierEvcPrecedence = _ClassifierEvcPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 3),
    _ClassifierEvcPrecedence_Type()
)
classifierEvcPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPrecedence.setStatus("current")
_ClassifierEvcVidList_Type = OctetString
_ClassifierEvcVidList_Object = MibTableColumn
classifierEvcVidList = _ClassifierEvcVidList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 4),
    _ClassifierEvcVidList_Type()
)
classifierEvcVidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcVidList.setStatus("current")
_ClassifierEvcPcpList_Type = OctetString
_ClassifierEvcPcpList_Object = MibTableColumn
classifierEvcPcpList = _ClassifierEvcPcpList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 5),
    _ClassifierEvcPcpList_Type()
)
classifierEvcPcpList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPcpList.setStatus("current")


class _ClassifierEvcEvc_Type(Integer32):
    """Custom type classifierEvcEvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ClassifierEvcEvc_Type.__name__ = "Integer32"
_ClassifierEvcEvc_Object = MibTableColumn
classifierEvcEvc = _ClassifierEvcEvc_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 6),
    _ClassifierEvcEvc_Type()
)
classifierEvcEvc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcEvc.setStatus("current")


class _ClassifierEvcIpCosType_Type(Integer32):
    """Custom type classifierEvcIpCosType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip-cos-dont-care", 3),
          ("ip-cos-dscp", 1),
          ("ip-cos-mpls", 2))
    )


_ClassifierEvcIpCosType_Type.__name__ = "Integer32"
_ClassifierEvcIpCosType_Object = MibTableColumn
classifierEvcIpCosType = _ClassifierEvcIpCosType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 7),
    _ClassifierEvcIpCosType_Type()
)
classifierEvcIpCosType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcIpCosType.setStatus("current")
_ClassifierEvcIpCosList_Type = OctetString
_ClassifierEvcIpCosList_Object = MibTableColumn
classifierEvcIpCosList = _ClassifierEvcIpCosList_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 8),
    _ClassifierEvcIpCosList_Type()
)
classifierEvcIpCosList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcIpCosList.setStatus("current")
_ClassifierEvcRowStatus_Type = RowStatus
_ClassifierEvcRowStatus_Object = MibTableColumn
classifierEvcRowStatus = _ClassifierEvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 9),
    _ClassifierEvcRowStatus_Type()
)
classifierEvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcRowStatus.setStatus("current")


class _ClassifierEvcPacketType_Type(Integer32):
    """Custom type classifierEvcPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("non-unicast", 2),
          ("unicast", 1))
    )


_ClassifierEvcPacketType_Type.__name__ = "Integer32"
_ClassifierEvcPacketType_Object = MibTableColumn
classifierEvcPacketType = _ClassifierEvcPacketType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 6, 2, 1, 10),
    _ClassifierEvcPacketType_Type()
)
classifierEvcPacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    classifierEvcPacketType.setStatus("current")
_RadioBridgeQosIngressQueue_ObjectIdentity = ObjectIdentity
radioBridgeQosIngressQueue = _RadioBridgeQosIngressQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 7)
)
_RbQosIngressQueueTable_Object = MibTable
rbQosIngressQueueTable = _RbQosIngressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1)
)
if mibBuilder.loadTexts:
    rbQosIngressQueueTable.setStatus("current")
_RbQosIngressQueueEntry_Object = MibTableRow
rbQosIngressQueueEntry = _RbQosIngressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1)
)
rbQosIngressQueueEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "qosIngressQueueEvcId"),
    (0, "RADIO-BRIDGE-MIB", "qosIngressQueueCosId"),
)
if mibBuilder.loadTexts:
    rbQosIngressQueueEntry.setStatus("current")
_QosIngressQueueEvcId_Type = Integer32
_QosIngressQueueEvcId_Object = MibTableColumn
qosIngressQueueEvcId = _QosIngressQueueEvcId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 1),
    _QosIngressQueueEvcId_Type()
)
qosIngressQueueEvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIngressQueueEvcId.setStatus("current")
_QosIngressQueueCosId_Type = Integer32
_QosIngressQueueCosId_Object = MibTableColumn
qosIngressQueueCosId = _QosIngressQueueCosId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 2),
    _QosIngressQueueCosId_Type()
)
qosIngressQueueCosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosIngressQueueCosId.setStatus("current")
_QosIngressQueueMeterId_Type = Integer32
_QosIngressQueueMeterId_Object = MibTableColumn
qosIngressQueueMeterId = _QosIngressQueueMeterId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 3),
    _QosIngressQueueMeterId_Type()
)
qosIngressQueueMeterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIngressQueueMeterId.setStatus("current")
_QosIngressQueueMarking_Type = TruthValue
_QosIngressQueueMarking_Object = MibTableColumn
qosIngressQueueMarking = _QosIngressQueueMarking_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 4),
    _QosIngressQueueMarking_Type()
)
qosIngressQueueMarking.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIngressQueueMarking.setStatus("current")
_QosIngressQueueRowStatus_Type = RowStatus
_QosIngressQueueRowStatus_Object = MibTableColumn
qosIngressQueueRowStatus = _QosIngressQueueRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 7, 1, 1, 6),
    _QosIngressQueueRowStatus_Type()
)
qosIngressQueueRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosIngressQueueRowStatus.setStatus("current")
_RadioBridgeQosEgressQueue_ObjectIdentity = ObjectIdentity
radioBridgeQosEgressQueue = _RadioBridgeQosEgressQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 8)
)
_RbQosEgressQueueTable_Object = MibTable
rbQosEgressQueueTable = _RbQosEgressQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1)
)
if mibBuilder.loadTexts:
    rbQosEgressQueueTable.setStatus("current")
_RbQosEgressQueueEntry_Object = MibTableRow
rbQosEgressQueueEntry = _RbQosEgressQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1)
)
rbQosEgressQueueEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "qosEgressQueuePortNum"),
    (0, "RADIO-BRIDGE-MIB", "qosEgressQueueCosId"),
)
if mibBuilder.loadTexts:
    rbQosEgressQueueEntry.setStatus("current")
_QosEgressQueuePortNum_Type = Integer32
_QosEgressQueuePortNum_Object = MibTableColumn
qosEgressQueuePortNum = _QosEgressQueuePortNum_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 1),
    _QosEgressQueuePortNum_Type()
)
qosEgressQueuePortNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosEgressQueuePortNum.setStatus("current")
_QosEgressQueueCosId_Type = Integer32
_QosEgressQueueCosId_Object = MibTableColumn
qosEgressQueueCosId = _QosEgressQueueCosId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 2),
    _QosEgressQueueCosId_Type()
)
qosEgressQueueCosId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qosEgressQueueCosId.setStatus("current")


class _QosEgressQueueWfqWeight_Type(Integer32):
    """Custom type qosEgressQueueWfqWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_QosEgressQueueWfqWeight_Type.__name__ = "Integer32"
_QosEgressQueueWfqWeight_Object = MibTableColumn
qosEgressQueueWfqWeight = _QosEgressQueueWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 4),
    _QosEgressQueueWfqWeight_Type()
)
qosEgressQueueWfqWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressQueueWfqWeight.setStatus("current")


class _QosEgressQueueCir_Type(Integer32):
    """Custom type qosEgressQueueCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_QosEgressQueueCir_Type.__name__ = "Integer32"
_QosEgressQueueCir_Object = MibTableColumn
qosEgressQueueCir = _QosEgressQueueCir_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 5),
    _QosEgressQueueCir_Type()
)
qosEgressQueueCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressQueueCir.setStatus("current")


class _QosEgressQueueMode_Type(Integer32):
    """Custom type qosEgressQueueMode based on Integer32"""
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
        *(("priority-shaper", 3),
          ("strictPriority", 1),
          ("wfg", 2),
          ("wfq-shaper", 4))
    )


_QosEgressQueueMode_Type.__name__ = "Integer32"
_QosEgressQueueMode_Object = MibTableColumn
qosEgressQueueMode = _QosEgressQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 6),
    _QosEgressQueueMode_Type()
)
qosEgressQueueMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosEgressQueueMode.setStatus("current")


class _QosEgressQueueColorDrop_Type(Integer32):
    """Custom type qosEgressQueueColorDrop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-drop", 2))
    )


_QosEgressQueueColorDrop_Type.__name__ = "Integer32"
_QosEgressQueueColorDrop_Object = MibTableColumn
qosEgressQueueColorDrop = _QosEgressQueueColorDrop_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 7),
    _QosEgressQueueColorDrop_Type()
)
qosEgressQueueColorDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressQueueColorDrop.setStatus("current")
_QosEgressDropMode_Type = Integer32
_QosEgressDropMode_Object = MibTableColumn
qosEgressDropMode = _QosEgressDropMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 8, 1, 1, 8),
    _QosEgressDropMode_Type()
)
qosEgressDropMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosEgressDropMode.setStatus("current")
_RadioBridgeIp_ObjectIdentity = ObjectIdentity
radioBridgeIp = _RadioBridgeIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 9)
)
_RbIpTable_Object = MibTable
rbIpTable = _RbIpTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1)
)
if mibBuilder.loadTexts:
    rbIpTable.setStatus("current")
_RbIpEntry_Object = MibTableRow
rbIpEntry = _RbIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1)
)
rbIpEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbIpIndex"),
)
if mibBuilder.loadTexts:
    rbIpEntry.setStatus("current")
_RbIpIndex_Type = Integer32
_RbIpIndex_Object = MibTableColumn
rbIpIndex = _RbIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 1),
    _RbIpIndex_Type()
)
rbIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbIpIndex.setStatus("current")
_RbIpAddress_Type = IpAddress
_RbIpAddress_Object = MibTableColumn
rbIpAddress = _RbIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 2),
    _RbIpAddress_Type()
)
rbIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpAddress.setStatus("current")


class _RbIpPrefixLen_Type(Integer32):
    """Custom type rbIpPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RbIpPrefixLen_Type.__name__ = "Integer32"
_RbIpPrefixLen_Object = MibTableColumn
rbIpPrefixLen = _RbIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 3),
    _RbIpPrefixLen_Type()
)
rbIpPrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbIpPrefixLen.setStatus("current")
_RbIpVlanId_Type = Integer32
_RbIpVlanId_Object = MibTableColumn
rbIpVlanId = _RbIpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 4),
    _RbIpVlanId_Type()
)
rbIpVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpVlanId.setStatus("current")
_RbIpRowStatus_Type = RowStatus
_RbIpRowStatus_Object = MibTableColumn
rbIpRowStatus = _RbIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 5),
    _RbIpRowStatus_Type()
)
rbIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpRowStatus.setStatus("current")


class _RbIpType_Type(Integer32):
    """Custom type rbIpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip-dhcp", 2),
          ("ip-static", 1))
    )


_RbIpType_Type.__name__ = "Integer32"
_RbIpType_Object = MibTableColumn
rbIpType = _RbIpType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 6),
    _RbIpType_Type()
)
rbIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbIpType.setStatus("current")
_RbIpGateway_Type = IpAddress
_RbIpGateway_Object = MibTableColumn
rbIpGateway = _RbIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 31926, 9, 1, 1, 7),
    _RbIpGateway_Type()
)
rbIpGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbIpGateway.setStatus("current")
_RadioBridgeCfm_ObjectIdentity = ObjectIdentity
radioBridgeCfm = _RadioBridgeCfm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 10)
)
_RbPeerMep_Object = MibTable
rbPeerMep = _RbPeerMep_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1)
)
if mibBuilder.loadTexts:
    rbPeerMep.setStatus("current")
_RbPeerMepEntry_Object = MibTableRow
rbPeerMepEntry = _RbPeerMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1)
)
rbPeerMepEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbMdIndex"),
    (0, "RADIO-BRIDGE-MIB", "rbMaIndex"),
    (0, "RADIO-BRIDGE-MIB", "rbMepId"),
    (0, "RADIO-BRIDGE-MIB", "rbPeerMepId"),
)
if mibBuilder.loadTexts:
    rbPeerMepEntry.setStatus("current")
_RbMdIndex_Type = Integer32
_RbMdIndex_Object = MibTableColumn
rbMdIndex = _RbMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 1),
    _RbMdIndex_Type()
)
rbMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMdIndex.setStatus("current")
_RbMaIndex_Type = Integer32
_RbMaIndex_Object = MibTableColumn
rbMaIndex = _RbMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 2),
    _RbMaIndex_Type()
)
rbMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMaIndex.setStatus("current")
_RbMepId_Type = Integer32
_RbMepId_Object = MibTableColumn
rbMepId = _RbMepId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 3),
    _RbMepId_Type()
)
rbMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMepId.setStatus("current")
_RbPeerMepId_Type = Integer32
_RbPeerMepId_Object = MibTableColumn
rbPeerMepId = _RbPeerMepId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 4),
    _RbPeerMepId_Type()
)
rbPeerMepId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepId.setStatus("current")
_RbPeerMepFarEndLoss_Type = Counter64
_RbPeerMepFarEndLoss_Object = MibTableColumn
rbPeerMepFarEndLoss = _RbPeerMepFarEndLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 5),
    _RbPeerMepFarEndLoss_Type()
)
rbPeerMepFarEndLoss.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepFarEndLoss.setStatus("current")
_RbPeerMepNearEndLoss_Type = Counter64
_RbPeerMepNearEndLoss_Object = MibTableColumn
rbPeerMepNearEndLoss = _RbPeerMepNearEndLoss_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 6),
    _RbPeerMepNearEndLoss_Type()
)
rbPeerMepNearEndLoss.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepNearEndLoss.setStatus("current")
_RbPeerMepTotalTxFarEnd_Type = Counter64
_RbPeerMepTotalTxFarEnd_Object = MibTableColumn
rbPeerMepTotalTxFarEnd = _RbPeerMepTotalTxFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 7),
    _RbPeerMepTotalTxFarEnd_Type()
)
rbPeerMepTotalTxFarEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepTotalTxFarEnd.setStatus("current")
_RbPeerMepTotalTxNearEnd_Type = Counter64
_RbPeerMepTotalTxNearEnd_Object = MibTableColumn
rbPeerMepTotalTxNearEnd = _RbPeerMepTotalTxNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 8),
    _RbPeerMepTotalTxNearEnd_Type()
)
rbPeerMepTotalTxNearEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepTotalTxNearEnd.setStatus("current")
_RbPeerMepFrameDelay_Type = Counter64
_RbPeerMepFrameDelay_Object = MibTableColumn
rbPeerMepFrameDelay = _RbPeerMepFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 9),
    _RbPeerMepFrameDelay_Type()
)
rbPeerMepFrameDelay.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepFrameDelay.setStatus("current")
_RbPeerMepFrameDelayVariation_Type = Counter64
_RbPeerMepFrameDelayVariation_Object = MibTableColumn
rbPeerMepFrameDelayVariation = _RbPeerMepFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 1, 1, 10),
    _RbPeerMepFrameDelayVariation_Type()
)
rbPeerMepFrameDelayVariation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPeerMepFrameDelayVariation.setStatus("current")
_RbMep_Object = MibTable
rbMep = _RbMep_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2)
)
if mibBuilder.loadTexts:
    rbMep.setStatus("current")
_RbMepEntry_Object = MibTableRow
rbMepEntry = _RbMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1)
)
if mibBuilder.loadTexts:
    rbMepEntry.setStatus("current")
_RbMepAisEnable_Type = TruthValue
_RbMepAisEnable_Object = MibTableColumn
rbMepAisEnable = _RbMepAisEnable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 1),
    _RbMepAisEnable_Type()
)
rbMepAisEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisEnable.setStatus("current")


class _RbMepAisPeriod_Type(Integer32):
    """Custom type rbMepAisPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aisPeriod-1-min", 6),
          ("aisPeriod-1-sec", 4))
    )


_RbMepAisPeriod_Type.__name__ = "Integer32"
_RbMepAisPeriod_Object = MibTableColumn
rbMepAisPeriod = _RbMepAisPeriod_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 2),
    _RbMepAisPeriod_Type()
)
rbMepAisPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisPeriod.setStatus("current")
_RbMepAisSuppress_Type = TruthValue
_RbMepAisSuppress_Object = MibTableColumn
rbMepAisSuppress = _RbMepAisSuppress_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 3),
    _RbMepAisSuppress_Type()
)
rbMepAisSuppress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisSuppress.setStatus("current")
_RbMepAisLevel_Type = Integer32
_RbMepAisLevel_Object = MibTableColumn
rbMepAisLevel = _RbMepAisLevel_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 4),
    _RbMepAisLevel_Type()
)
rbMepAisLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMepAisLevel.setStatus("current")
_RbMepAisDefects_Type = TruthValue
_RbMepAisDefects_Object = MibTableColumn
rbMepAisDefects = _RbMepAisDefects_Object(
    (1, 3, 6, 1, 4, 1, 31926, 10, 2, 1, 5),
    _RbMepAisDefects_Type()
)
rbMepAisDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMepAisDefects.setStatus("current")
_RadioBridgeAlarms_ObjectIdentity = ObjectIdentity
radioBridgeAlarms = _RadioBridgeAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 11)
)
_RbAlarmsCommon_ObjectIdentity = ObjectIdentity
rbAlarmsCommon = _RbAlarmsCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1)
)
_RbCurrentAlarmChangeCounter_Type = Integer32
_RbCurrentAlarmChangeCounter_Object = MibScalar
rbCurrentAlarmChangeCounter = _RbCurrentAlarmChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 1),
    _RbCurrentAlarmChangeCounter_Type()
)
rbCurrentAlarmChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmChangeCounter.setStatus("current")
_RbCurrentAlarmMostSevere_Type = AlarmSeverity
_RbCurrentAlarmMostSevere_Object = MibScalar
rbCurrentAlarmMostSevere = _RbCurrentAlarmMostSevere_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 2),
    _RbCurrentAlarmMostSevere_Type()
)
rbCurrentAlarmMostSevere.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmMostSevere.setStatus("current")
_RbCurrentAlarmLastIndex_Type = Integer32
_RbCurrentAlarmLastIndex_Object = MibScalar
rbCurrentAlarmLastIndex = _RbCurrentAlarmLastIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 3),
    _RbCurrentAlarmLastIndex_Type()
)
rbCurrentAlarmLastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmLastIndex.setStatus("current")


class _RbCurrentAlarmLastTrapType_Type(Integer32):
    """Custom type rbCurrentAlarmLastTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm-down", 2),
          ("alarm-up", 1))
    )


_RbCurrentAlarmLastTrapType_Type.__name__ = "Integer32"
_RbCurrentAlarmLastTrapType_Object = MibScalar
rbCurrentAlarmLastTrapType = _RbCurrentAlarmLastTrapType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 4),
    _RbCurrentAlarmLastTrapType_Type()
)
rbCurrentAlarmLastTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmLastTrapType.setStatus("current")
_RbCurrentAlarmSourceAddr_Type = IpAddress
_RbCurrentAlarmSourceAddr_Object = MibScalar
rbCurrentAlarmSourceAddr = _RbCurrentAlarmSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 1, 10),
    _RbCurrentAlarmSourceAddr_Type()
)
rbCurrentAlarmSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSourceAddr.setStatus("current")
_RbCurrentAlarmTable_Object = MibTable
rbCurrentAlarmTable = _RbCurrentAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2)
)
if mibBuilder.loadTexts:
    rbCurrentAlarmTable.setStatus("current")
_RbCurrentAlarmEntry_Object = MibTableRow
rbCurrentAlarmEntry = _RbCurrentAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1)
)
rbCurrentAlarmEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbCurrentAlarmIndex"),
)
if mibBuilder.loadTexts:
    rbCurrentAlarmEntry.setStatus("current")
_RbCurrentAlarmIndex_Type = Integer32
_RbCurrentAlarmIndex_Object = MibTableColumn
rbCurrentAlarmIndex = _RbCurrentAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 1),
    _RbCurrentAlarmIndex_Type()
)
rbCurrentAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmIndex.setStatus("current")
_RbCurrentAlarmType_Type = AlarmType
_RbCurrentAlarmType_Object = MibTableColumn
rbCurrentAlarmType = _RbCurrentAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 2),
    _RbCurrentAlarmType_Type()
)
rbCurrentAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmType.setStatus("current")
_RbCurrentAlarmTypeName_Type = DisplayString
_RbCurrentAlarmTypeName_Object = MibTableColumn
rbCurrentAlarmTypeName = _RbCurrentAlarmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 3),
    _RbCurrentAlarmTypeName_Type()
)
rbCurrentAlarmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmTypeName.setStatus("current")
_RbCurrentAlarmSource_Type = DisplayString
_RbCurrentAlarmSource_Object = MibTableColumn
rbCurrentAlarmSource = _RbCurrentAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 4),
    _RbCurrentAlarmSource_Type()
)
rbCurrentAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSource.setStatus("current")
_RbCurrentAlarmSeverity_Type = AlarmSeverity
_RbCurrentAlarmSeverity_Object = MibTableColumn
rbCurrentAlarmSeverity = _RbCurrentAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 5),
    _RbCurrentAlarmSeverity_Type()
)
rbCurrentAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmSeverity.setStatus("current")
_RbCurrentAlarmRaisedTime_Type = TimeTicks
_RbCurrentAlarmRaisedTime_Object = MibTableColumn
rbCurrentAlarmRaisedTime = _RbCurrentAlarmRaisedTime_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 6),
    _RbCurrentAlarmRaisedTime_Type()
)
rbCurrentAlarmRaisedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmRaisedTime.setStatus("current")
_RbCurrentAlarmDesc_Type = DisplayString
_RbCurrentAlarmDesc_Object = MibTableColumn
rbCurrentAlarmDesc = _RbCurrentAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 7),
    _RbCurrentAlarmDesc_Type()
)
rbCurrentAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmDesc.setStatus("current")
_RbCurrentAlarmCause_Type = DisplayString
_RbCurrentAlarmCause_Object = MibTableColumn
rbCurrentAlarmCause = _RbCurrentAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 8),
    _RbCurrentAlarmCause_Type()
)
rbCurrentAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmCause.setStatus("current")
_RbCurrentAlarmAction_Type = DisplayString
_RbCurrentAlarmAction_Object = MibTableColumn
rbCurrentAlarmAction = _RbCurrentAlarmAction_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 9),
    _RbCurrentAlarmAction_Type()
)
rbCurrentAlarmAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmAction.setStatus("current")
_RbCurrentAlarmIfIndex_Type = Integer32
_RbCurrentAlarmIfIndex_Object = MibTableColumn
rbCurrentAlarmIfIndex = _RbCurrentAlarmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 11, 2, 1, 10),
    _RbCurrentAlarmIfIndex_Type()
)
rbCurrentAlarmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentAlarmIfIndex.setStatus("current")
_RadioBridgeScheduler_ObjectIdentity = ObjectIdentity
radioBridgeScheduler = _RadioBridgeScheduler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 12)
)


class _RbSchedulerMode_Type(Integer32):
    """Custom type rbSchedulerMode based on Integer32"""
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
        *(("priority-shaper", 3),
          ("strictPriority", 1),
          ("wfg", 2),
          ("wfq-shaper", 4))
    )


_RbSchedulerMode_Type.__name__ = "Integer32"
_RbSchedulerMode_Object = MibScalar
rbSchedulerMode = _RbSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 12, 1),
    _RbSchedulerMode_Type()
)
rbSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSchedulerMode.setStatus("current")
_RadioBridgeEncryption_ObjectIdentity = ObjectIdentity
radioBridgeEncryption = _RadioBridgeEncryption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 13)
)
_RbRfEncryption_Type = TruthValue
_RbRfEncryption_Object = MibScalar
rbRfEncryption = _RbRfEncryption_Object(
    (1, 3, 6, 1, 4, 1, 31926, 13, 1),
    _RbRfEncryption_Type()
)
rbRfEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRfEncryption.setStatus("current")
_RbRfStaticKey_Type = OctetString
_RbRfStaticKey_Object = MibScalar
rbRfStaticKey = _RbRfStaticKey_Object(
    (1, 3, 6, 1, 4, 1, 31926, 13, 2),
    _RbRfStaticKey_Type()
)
rbRfStaticKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRfStaticKey.setStatus("current")
_RbRfAuthenticationString_Type = OctetString
_RbRfAuthenticationString_Object = MibScalar
rbRfAuthenticationString = _RbRfAuthenticationString_Object(
    (1, 3, 6, 1, 4, 1, 31926, 13, 3),
    _RbRfAuthenticationString_Type()
)
rbRfAuthenticationString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRfAuthenticationString.setStatus("current")
_RadioBridgeMeter_ObjectIdentity = ObjectIdentity
radioBridgeMeter = _RadioBridgeMeter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 14)
)
_RbMeterTable_Object = MibTable
rbMeterTable = _RbMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1)
)
if mibBuilder.loadTexts:
    rbMeterTable.setStatus("current")
_RbMeterEntry_Object = MibTableRow
rbMeterEntry = _RbMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1)
)
rbMeterEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbMeterId"),
)
if mibBuilder.loadTexts:
    rbMeterEntry.setStatus("current")


class _RbMeterId_Type(Integer32):
    """Custom type rbMeterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 248),
    )


_RbMeterId_Type.__name__ = "Integer32"
_RbMeterId_Object = MibTableColumn
rbMeterId = _RbMeterId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 1),
    _RbMeterId_Type()
)
rbMeterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbMeterId.setStatus("current")


class _RbMeterCir_Type(Integer32):
    """Custom type rbMeterCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RbMeterCir_Type.__name__ = "Integer32"
_RbMeterCir_Object = MibTableColumn
rbMeterCir = _RbMeterCir_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 2),
    _RbMeterCir_Type()
)
rbMeterCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterCir.setStatus("current")


class _RbMeterCbs_Type(Integer32):
    """Custom type rbMeterCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9216, 50000),
    )


_RbMeterCbs_Type.__name__ = "Integer32"
_RbMeterCbs_Object = MibTableColumn
rbMeterCbs = _RbMeterCbs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 3),
    _RbMeterCbs_Type()
)
rbMeterCbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterCbs.setStatus("current")


class _RbMeterEir_Type(Integer32):
    """Custom type rbMeterEir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RbMeterEir_Type.__name__ = "Integer32"
_RbMeterEir_Object = MibTableColumn
rbMeterEir = _RbMeterEir_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 4),
    _RbMeterEir_Type()
)
rbMeterEir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterEir.setStatus("current")


class _RbMeterEbs_Type(Integer32):
    """Custom type rbMeterEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9216, 100000),
    )


_RbMeterEbs_Type.__name__ = "Integer32"
_RbMeterEbs_Object = MibTableColumn
rbMeterEbs = _RbMeterEbs_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 5),
    _RbMeterEbs_Type()
)
rbMeterEbs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterEbs.setStatus("current")


class _RbMeterColorMode_Type(Integer32):
    """Custom type rbMeterColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("color-aware", 1),
          ("color-blind", 2))
    )


_RbMeterColorMode_Type.__name__ = "Integer32"
_RbMeterColorMode_Object = MibTableColumn
rbMeterColorMode = _RbMeterColorMode_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 6),
    _RbMeterColorMode_Type()
)
rbMeterColorMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterColorMode.setStatus("current")
_RbMeterRowStatus_Type = RowStatus
_RbMeterRowStatus_Object = MibTableColumn
rbMeterRowStatus = _RbMeterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 14, 1, 1, 7),
    _RbMeterRowStatus_Type()
)
rbMeterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbMeterRowStatus.setStatus("current")
_RadioBridgeEventConfig_ObjectIdentity = ObjectIdentity
radioBridgeEventConfig = _RadioBridgeEventConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 15)
)
_RbEventConfigTable_Object = MibTable
rbEventConfigTable = _RbEventConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1)
)
if mibBuilder.loadTexts:
    rbEventConfigTable.setStatus("current")
_RbEventConfigEntry_Object = MibTableRow
rbEventConfigEntry = _RbEventConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1)
)
rbEventConfigEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbEventConfigIndex"),
)
if mibBuilder.loadTexts:
    rbEventConfigEntry.setStatus("current")
_RbEventConfigIndex_Type = Integer32
_RbEventConfigIndex_Object = MibTableColumn
rbEventConfigIndex = _RbEventConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1, 1),
    _RbEventConfigIndex_Type()
)
rbEventConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbEventConfigIndex.setStatus("current")
_RbEventConfigId_Type = OctetString
_RbEventConfigId_Object = MibTableColumn
rbEventConfigId = _RbEventConfigId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1, 2),
    _RbEventConfigId_Type()
)
rbEventConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbEventConfigId.setStatus("current")
_RbEventConfigMask_Type = TruthValue
_RbEventConfigMask_Object = MibTableColumn
rbEventConfigMask = _RbEventConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 31926, 15, 1, 1, 3),
    _RbEventConfigMask_Type()
)
rbEventConfigMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbEventConfigMask.setStatus("current")
_RadioBridgeSnmp_ObjectIdentity = ObjectIdentity
radioBridgeSnmp = _RadioBridgeSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 17)
)
_RbAgentReadCommunity_Type = DisplayString
_RbAgentReadCommunity_Object = MibScalar
rbAgentReadCommunity = _RbAgentReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 17, 1),
    _RbAgentReadCommunity_Type()
)
rbAgentReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAgentReadCommunity.setStatus("current")
_RbAgentWriteCommunity_Type = DisplayString
_RbAgentWriteCommunity_Object = MibScalar
rbAgentWriteCommunity = _RbAgentWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 31926, 17, 2),
    _RbAgentWriteCommunity_Type()
)
rbAgentWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAgentWriteCommunity.setStatus("current")


class _RbAgentSnmpVersion_Type(Integer32):
    """Custom type rbAgentSnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2c", 2),
          ("v3", 3))
    )


_RbAgentSnmpVersion_Type.__name__ = "Integer32"
_RbAgentSnmpVersion_Object = MibScalar
rbAgentSnmpVersion = _RbAgentSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 31926, 17, 3),
    _RbAgentSnmpVersion_Type()
)
rbAgentSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAgentSnmpVersion.setStatus("current")
_RbSysFileOperationTable_Object = MibTable
rbSysFileOperationTable = _RbSysFileOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18)
)
if mibBuilder.loadTexts:
    rbSysFileOperationTable.setStatus("current")
_RbSysFileOperationEntry_Object = MibTableRow
rbSysFileOperationEntry = _RbSysFileOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1)
)
rbSysFileOperationEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "fileSessionIndex"),
)
if mibBuilder.loadTexts:
    rbSysFileOperationEntry.setStatus("current")
_FileSessionIndex_Type = Integer32
_FileSessionIndex_Object = MibTableColumn
fileSessionIndex = _FileSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 1),
    _FileSessionIndex_Type()
)
fileSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileSessionIndex.setStatus("current")


class _FileSessionCommand_Type(Integer32):
    """Custom type fileSessionCommand based on Integer32"""
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
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("acceptSw", 5),
          ("copyDirToRemote", 7),
          ("copyEventLog", 9),
          ("copyFileFromLocalToRemote", 4),
          ("copyFileFromRemoteToLocal", 3),
          ("copyInventory", 12),
          ("copyLicenseFromRemote", 2),
          ("copyStatsHistory", 13),
          ("copySwFromRemote", 1),
          ("copyUserActivityLog", 10),
          ("runScript", 11),
          ("runSw", 6))
    )


_FileSessionCommand_Type.__name__ = "Integer32"
_FileSessionCommand_Object = MibTableColumn
fileSessionCommand = _FileSessionCommand_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 2),
    _FileSessionCommand_Type()
)
fileSessionCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionCommand.setStatus("current")
_FileSessionLocalParams_Type = DisplayString
_FileSessionLocalParams_Object = MibTableColumn
fileSessionLocalParams = _FileSessionLocalParams_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 3),
    _FileSessionLocalParams_Type()
)
fileSessionLocalParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionLocalParams.setStatus("current")
_FileSessionRemotePath_Type = DisplayString
_FileSessionRemotePath_Object = MibTableColumn
fileSessionRemotePath = _FileSessionRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 4),
    _FileSessionRemotePath_Type()
)
fileSessionRemotePath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionRemotePath.setStatus("current")
_FileSessionServer_Type = DisplayString
_FileSessionServer_Object = MibTableColumn
fileSessionServer = _FileSessionServer_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 5),
    _FileSessionServer_Type()
)
fileSessionServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionServer.setStatus("current")
_FileSessionUser_Type = DisplayString
_FileSessionUser_Object = MibTableColumn
fileSessionUser = _FileSessionUser_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 6),
    _FileSessionUser_Type()
)
fileSessionUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionUser.setStatus("current")
_FileSessionPassword_Type = DisplayString
_FileSessionPassword_Object = MibTableColumn
fileSessionPassword = _FileSessionPassword_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 7),
    _FileSessionPassword_Type()
)
fileSessionPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionPassword.setStatus("current")
_FileSessionResult_Type = DisplayString
_FileSessionResult_Object = MibTableColumn
fileSessionResult = _FileSessionResult_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 8),
    _FileSessionResult_Type()
)
fileSessionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSessionResult.setStatus("current")


class _FileSessionState_Type(Integer32):
    """Custom type fileSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("terminated-error", 3),
          ("terminated-ok", 2))
    )


_FileSessionState_Type.__name__ = "Integer32"
_FileSessionState_Object = MibTableColumn
fileSessionState = _FileSessionState_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 9),
    _FileSessionState_Type()
)
fileSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSessionState.setStatus("current")
_FileSessionRowStatus_Type = RowStatus
_FileSessionRowStatus_Object = MibTableColumn
fileSessionRowStatus = _FileSessionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 10),
    _FileSessionRowStatus_Type()
)
fileSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fileSessionRowStatus.setStatus("current")


class _FileSessionProtocol_Type(Integer32):
    """Custom type fileSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("sftp", 2))
    )


_FileSessionProtocol_Type.__name__ = "Integer32"
_FileSessionProtocol_Object = MibTableColumn
fileSessionProtocol = _FileSessionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 31926, 18, 1, 13),
    _FileSessionProtocol_Type()
)
fileSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSessionProtocol.setStatus("current")
_RadioBridgeLldp_ObjectIdentity = ObjectIdentity
radioBridgeLldp = _RadioBridgeLldp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 19)
)
_RbLldpPortExtensionTable_Object = MibTable
rbLldpPortExtensionTable = _RbLldpPortExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1)
)
if mibBuilder.loadTexts:
    rbLldpPortExtensionTable.setStatus("current")
_RbLldpPortExtensionEntry_Object = MibTableRow
rbLldpPortExtensionEntry = _RbLldpPortExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1)
)
rbLldpPortExtensionEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbLldpPortIfIndex"),
    (0, "RADIO-BRIDGE-MIB", "rbLldpPortDestAddressIndex"),
)
if mibBuilder.loadTexts:
    rbLldpPortExtensionEntry.setStatus("current")
_RbLldpPortIfIndex_Type = InterfaceIndex
_RbLldpPortIfIndex_Object = MibTableColumn
rbLldpPortIfIndex = _RbLldpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 1),
    _RbLldpPortIfIndex_Type()
)
rbLldpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbLldpPortIfIndex.setStatus("current")
_RbLldpPortDestAddressIndex_Type = Unsigned32
_RbLldpPortDestAddressIndex_Object = MibTableColumn
rbLldpPortDestAddressIndex = _RbLldpPortDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 2),
    _RbLldpPortDestAddressIndex_Type()
)
rbLldpPortDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbLldpPortDestAddressIndex.setStatus("current")
_RbLldpPortVid_Type = Unsigned32
_RbLldpPortVid_Object = MibTableColumn
rbLldpPortVid = _RbLldpPortVid_Object(
    (1, 3, 6, 1, 4, 1, 31926, 19, 1, 1, 3),
    _RbLldpPortVid_Type()
)
rbLldpPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbLldpPortVid.setStatus("current")
_RadioBridgeWred_ObjectIdentity = ObjectIdentity
radioBridgeWred = _RadioBridgeWred_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 20)
)
_RbWredTable_Object = MibTable
rbWredTable = _RbWredTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1)
)
if mibBuilder.loadTexts:
    rbWredTable.setStatus("current")
_RbWredEntry_Object = MibTableRow
rbWredEntry = _RbWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1)
)
rbWredEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbWredId"),
)
if mibBuilder.loadTexts:
    rbWredEntry.setStatus("current")
_RbWredId_Type = Integer32
_RbWredId_Object = MibTableColumn
rbWredId = _RbWredId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 1),
    _RbWredId_Type()
)
rbWredId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbWredId.setStatus("current")


class _RbWredNfactor_Type(Integer32):
    """Custom type rbWredNfactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RbWredNfactor_Type.__name__ = "Integer32"
_RbWredNfactor_Object = MibTableColumn
rbWredNfactor = _RbWredNfactor_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 2),
    _RbWredNfactor_Type()
)
rbWredNfactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredNfactor.setStatus("current")
_RbWredMinThreshold_Type = Integer32
_RbWredMinThreshold_Object = MibTableColumn
rbWredMinThreshold = _RbWredMinThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 3),
    _RbWredMinThreshold_Type()
)
rbWredMinThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMinThreshold.setStatus("current")
_RbWredMaxThreshold_Type = Integer32
_RbWredMaxThreshold_Object = MibTableColumn
rbWredMaxThreshold = _RbWredMaxThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 4),
    _RbWredMaxThreshold_Type()
)
rbWredMaxThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMaxThreshold.setStatus("current")


class _RbWredProbability_Type(Integer32):
    """Custom type rbWredProbability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RbWredProbability_Type.__name__ = "Integer32"
_RbWredProbability_Object = MibTableColumn
rbWredProbability = _RbWredProbability_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 5),
    _RbWredProbability_Type()
)
rbWredProbability.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredProbability.setStatus("current")
_RbWredMinThresholdYellow_Type = Integer32
_RbWredMinThresholdYellow_Object = MibTableColumn
rbWredMinThresholdYellow = _RbWredMinThresholdYellow_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 6),
    _RbWredMinThresholdYellow_Type()
)
rbWredMinThresholdYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMinThresholdYellow.setStatus("current")
_RbWredMaxThresholdYellow_Type = Integer32
_RbWredMaxThresholdYellow_Object = MibTableColumn
rbWredMaxThresholdYellow = _RbWredMaxThresholdYellow_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 7),
    _RbWredMaxThresholdYellow_Type()
)
rbWredMaxThresholdYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredMaxThresholdYellow.setStatus("current")


class _RbWredProbabilityYellow_Type(Integer32):
    """Custom type rbWredProbabilityYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RbWredProbabilityYellow_Type.__name__ = "Integer32"
_RbWredProbabilityYellow_Object = MibTableColumn
rbWredProbabilityYellow = _RbWredProbabilityYellow_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 8),
    _RbWredProbabilityYellow_Type()
)
rbWredProbabilityYellow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredProbabilityYellow.setStatus("current")
_RbWredRowStatus_Type = RowStatus
_RbWredRowStatus_Object = MibTableColumn
rbWredRowStatus = _RbWredRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 20, 1, 1, 9),
    _RbWredRowStatus_Type()
)
rbWredRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbWredRowStatus.setStatus("current")
_RadioBridgeAuthentication_ObjectIdentity = ObjectIdentity
radioBridgeAuthentication = _RadioBridgeAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 21)
)
_RbAuthServersTable_Object = MibTable
rbAuthServersTable = _RbAuthServersTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1)
)
if mibBuilder.loadTexts:
    rbAuthServersTable.setStatus("current")
_RbAuthServersEntry_Object = MibTableRow
rbAuthServersEntry = _RbAuthServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1)
)
rbAuthServersEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbAuthServerId"),
)
if mibBuilder.loadTexts:
    rbAuthServersEntry.setStatus("current")


class _RbAuthServerId_Type(Integer32):
    """Custom type rbAuthServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RbAuthServerId_Type.__name__ = "Integer32"
_RbAuthServerId_Object = MibTableColumn
rbAuthServerId = _RbAuthServerId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 1),
    _RbAuthServerId_Type()
)
rbAuthServerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbAuthServerId.setStatus("current")
_RbAuthServerIpAddress_Type = IpAddress
_RbAuthServerIpAddress_Object = MibTableColumn
rbAuthServerIpAddress = _RbAuthServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 2),
    _RbAuthServerIpAddress_Type()
)
rbAuthServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbAuthServerIpAddress.setStatus("current")
_RbAuthServerPort_Type = Integer32
_RbAuthServerPort_Object = MibTableColumn
rbAuthServerPort = _RbAuthServerPort_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 3),
    _RbAuthServerPort_Type()
)
rbAuthServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbAuthServerPort.setStatus("current")
_RbAuthServerRowStatus_Type = RowStatus
_RbAuthServerRowStatus_Object = MibTableColumn
rbAuthServerRowStatus = _RbAuthServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 21, 1, 1, 4),
    _RbAuthServerRowStatus_Type()
)
rbAuthServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbAuthServerRowStatus.setStatus("current")
_RadioBridgeQuota_ObjectIdentity = ObjectIdentity
radioBridgeQuota = _RadioBridgeQuota_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 22)
)
_RbFdbQuotaTable_Object = MibTable
rbFdbQuotaTable = _RbFdbQuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1)
)
if mibBuilder.loadTexts:
    rbFdbQuotaTable.setStatus("current")
_RbFdbQuotaEntry_Object = MibTableRow
rbFdbQuotaEntry = _RbFdbQuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1)
)
rbFdbQuotaEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbFdbQuotaId"),
)
if mibBuilder.loadTexts:
    rbFdbQuotaEntry.setStatus("current")


class _RbFdbQuotaId_Type(Integer32):
    """Custom type rbFdbQuotaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbFdbQuotaId_Type.__name__ = "Integer32"
_RbFdbQuotaId_Object = MibTableColumn
rbFdbQuotaId = _RbFdbQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 1),
    _RbFdbQuotaId_Type()
)
rbFdbQuotaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbFdbQuotaId.setStatus("current")


class _RbFdbQuotaSize_Type(Integer32):
    """Custom type rbFdbQuotaSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4000),
    )


_RbFdbQuotaSize_Type.__name__ = "Integer32"
_RbFdbQuotaSize_Object = MibTableColumn
rbFdbQuotaSize = _RbFdbQuotaSize_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 2),
    _RbFdbQuotaSize_Type()
)
rbFdbQuotaSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbFdbQuotaSize.setStatus("current")
_RbFdbQuotaRowStatus_Type = RowStatus
_RbFdbQuotaRowStatus_Object = MibTableColumn
rbFdbQuotaRowStatus = _RbFdbQuotaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 3),
    _RbFdbQuotaRowStatus_Type()
)
rbFdbQuotaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbFdbQuotaRowStatus.setStatus("current")
_RbFdbQuotaMaxSize_Type = Counter64
_RbFdbQuotaMaxSize_Object = MibTableColumn
rbFdbQuotaMaxSize = _RbFdbQuotaMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 11),
    _RbFdbQuotaMaxSize_Type()
)
rbFdbQuotaMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaMaxSize.setStatus("current")
_RbFdbQuotaUsedEntries_Type = Counter64
_RbFdbQuotaUsedEntries_Object = MibTableColumn
rbFdbQuotaUsedEntries = _RbFdbQuotaUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 12),
    _RbFdbQuotaUsedEntries_Type()
)
rbFdbQuotaUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaUsedEntries.setStatus("current")
_RbFdbQuotaStaticEntries_Type = Counter64
_RbFdbQuotaStaticEntries_Object = MibTableColumn
rbFdbQuotaStaticEntries = _RbFdbQuotaStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 13),
    _RbFdbQuotaStaticEntries_Type()
)
rbFdbQuotaStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaStaticEntries.setStatus("current")
_RbFdbQuotaDynamicEntries_Type = Counter64
_RbFdbQuotaDynamicEntries_Object = MibTableColumn
rbFdbQuotaDynamicEntries = _RbFdbQuotaDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 14),
    _RbFdbQuotaDynamicEntries_Type()
)
rbFdbQuotaDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaDynamicEntries.setStatus("current")
_RbFdbQuotaUnusedEntries_Type = Counter64
_RbFdbQuotaUnusedEntries_Object = MibTableColumn
rbFdbQuotaUnusedEntries = _RbFdbQuotaUnusedEntries_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 1, 1, 15),
    _RbFdbQuotaUnusedEntries_Type()
)
rbFdbQuotaUnusedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFdbQuotaUnusedEntries.setStatus("current")
_RbFdbEvcQuotaTable_Object = MibTable
rbFdbEvcQuotaTable = _RbFdbEvcQuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2)
)
if mibBuilder.loadTexts:
    rbFdbEvcQuotaTable.setStatus("current")
_RbFdbEvcQuotaEntry_Object = MibTableRow
rbFdbEvcQuotaEntry = _RbFdbEvcQuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1)
)
rbFdbEvcQuotaEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbFdbEvcQuotaId"),
)
if mibBuilder.loadTexts:
    rbFdbEvcQuotaEntry.setStatus("current")


class _RbFdbEvcQuotaId_Type(Integer32):
    """Custom type rbFdbEvcQuotaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbFdbEvcQuotaId_Type.__name__ = "Integer32"
_RbFdbEvcQuotaId_Object = MibTableColumn
rbFdbEvcQuotaId = _RbFdbEvcQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 1),
    _RbFdbEvcQuotaId_Type()
)
rbFdbEvcQuotaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbFdbEvcQuotaId.setStatus("current")
_RbRefEvcId_Type = Integer32
_RbRefEvcId_Object = MibTableColumn
rbRefEvcId = _RbRefEvcId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 2),
    _RbRefEvcId_Type()
)
rbRefEvcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRefEvcId.setStatus("current")
_RbRefFdbQuotaId_Type = Integer32
_RbRefFdbQuotaId_Object = MibTableColumn
rbRefFdbQuotaId = _RbRefFdbQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 3),
    _RbRefFdbQuotaId_Type()
)
rbRefFdbQuotaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbRefFdbQuotaId.setStatus("current")
_RbFdbEvcQuotaRowStatus_Type = RowStatus
_RbFdbEvcQuotaRowStatus_Object = MibTableColumn
rbFdbEvcQuotaRowStatus = _RbFdbEvcQuotaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 2, 1, 4),
    _RbFdbEvcQuotaRowStatus_Type()
)
rbFdbEvcQuotaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbFdbEvcQuotaRowStatus.setStatus("current")
_RbFdbExtensionTable_Object = MibTable
rbFdbExtensionTable = _RbFdbExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 3)
)
if mibBuilder.loadTexts:
    rbFdbExtensionTable.setStatus("current")
_RbFdbExtensionEntry_Object = MibTableRow
rbFdbExtensionEntry = _RbFdbExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 3, 1)
)
if mibBuilder.loadTexts:
    rbFdbExtensionEntry.setStatus("current")
_RbRefExtFdbQuotaId_Type = Integer32
_RbRefExtFdbQuotaId_Object = MibTableColumn
rbRefExtFdbQuotaId = _RbRefExtFdbQuotaId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 22, 3, 1, 1),
    _RbRefExtFdbQuotaId_Type()
)
rbRefExtFdbQuotaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRefExtFdbQuotaId.setStatus("current")
_RadioBridgePcpProfile_ObjectIdentity = ObjectIdentity
radioBridgePcpProfile = _RadioBridgePcpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 23)
)
_RbPcpWriteProfileTable_Object = MibTable
rbPcpWriteProfileTable = _RbPcpWriteProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1)
)
if mibBuilder.loadTexts:
    rbPcpWriteProfileTable.setStatus("current")
_RbPcpWriteProfileEntry_Object = MibTableRow
rbPcpWriteProfileEntry = _RbPcpWriteProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1)
)
rbPcpWriteProfileEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbPcpWriteProfileId"),
)
if mibBuilder.loadTexts:
    rbPcpWriteProfileEntry.setStatus("current")


class _RbPcpWriteProfileId_Type(Integer32):
    """Custom type rbPcpWriteProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbPcpWriteProfileId_Type.__name__ = "Integer32"
_RbPcpWriteProfileId_Object = MibTableColumn
rbPcpWriteProfileId = _RbPcpWriteProfileId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1, 1),
    _RbPcpWriteProfileId_Type()
)
rbPcpWriteProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbPcpWriteProfileId.setStatus("current")


class _RbPcpWriteProfilePcp_Type(OctetString):
    """Custom type rbPcpWriteProfilePcp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_RbPcpWriteProfilePcp_Type.__name__ = "OctetString"
_RbPcpWriteProfilePcp_Object = MibTableColumn
rbPcpWriteProfilePcp = _RbPcpWriteProfilePcp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1, 2),
    _RbPcpWriteProfilePcp_Type()
)
rbPcpWriteProfilePcp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbPcpWriteProfilePcp.setStatus("current")
_RbPcpWriteProfileRowStatus_Type = RowStatus
_RbPcpWriteProfileRowStatus_Object = MibTableColumn
rbPcpWriteProfileRowStatus = _RbPcpWriteProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 23, 1, 1, 3),
    _RbPcpWriteProfileRowStatus_Type()
)
rbPcpWriteProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbPcpWriteProfileRowStatus.setStatus("current")
_RadioBridgeSyslog_ObjectIdentity = ObjectIdentity
radioBridgeSyslog = _RadioBridgeSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 24)
)
_RbSyslogTable_Object = MibTable
rbSyslogTable = _RbSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1)
)
if mibBuilder.loadTexts:
    rbSyslogTable.setStatus("current")
_RbSyslogEntry_Object = MibTableRow
rbSyslogEntry = _RbSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1)
)
rbSyslogEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbSyslogId"),
)
if mibBuilder.loadTexts:
    rbSyslogEntry.setStatus("current")
_RbSyslogId_Type = Integer32
_RbSyslogId_Object = MibTableColumn
rbSyslogId = _RbSyslogId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1, 1),
    _RbSyslogId_Type()
)
rbSyslogId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbSyslogId.setStatus("current")
_RbSyslogServerIp_Type = IpAddress
_RbSyslogServerIp_Object = MibTableColumn
rbSyslogServerIp = _RbSyslogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1, 2),
    _RbSyslogServerIp_Type()
)
rbSyslogServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbSyslogServerIp.setStatus("current")
_RbSyslogRowStatus_Type = RowStatus
_RbSyslogRowStatus_Object = MibTableColumn
rbSyslogRowStatus = _RbSyslogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 24, 1, 1, 3),
    _RbSyslogRowStatus_Type()
)
rbSyslogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbSyslogRowStatus.setStatus("current")
_RadioBridgeNtp_ObjectIdentity = ObjectIdentity
radioBridgeNtp = _RadioBridgeNtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 25)
)
_RbNtpTable_Object = MibTable
rbNtpTable = _RbNtpTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1)
)
if mibBuilder.loadTexts:
    rbNtpTable.setStatus("current")
_RbNtpEntry_Object = MibTableRow
rbNtpEntry = _RbNtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1)
)
rbNtpEntry.setIndexNames(
    (0, "RADIO-BRIDGE-MIB", "rbNtpId"),
)
if mibBuilder.loadTexts:
    rbNtpEntry.setStatus("current")
_RbNtpId_Type = Integer32
_RbNtpId_Object = MibTableColumn
rbNtpId = _RbNtpId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 1),
    _RbNtpId_Type()
)
rbNtpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbNtpId.setStatus("current")
_RbNtpServerIp_Type = IpAddress
_RbNtpServerIp_Object = MibTableColumn
rbNtpServerIp = _RbNtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 2),
    _RbNtpServerIp_Type()
)
rbNtpServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpServerIp.setStatus("current")
_RbNtpSecondaryServerIp_Type = IpAddress
_RbNtpSecondaryServerIp_Object = MibTableColumn
rbNtpSecondaryServerIp = _RbNtpSecondaryServerIp_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 3),
    _RbNtpSecondaryServerIp_Type()
)
rbNtpSecondaryServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpSecondaryServerIp.setStatus("current")


class _RbNtpTmz_Type(Integer32):
    """Custom type rbNtpTmz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 14),
    )


_RbNtpTmz_Type.__name__ = "Integer32"
_RbNtpTmz_Object = MibTableColumn
rbNtpTmz = _RbNtpTmz_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 4),
    _RbNtpTmz_Type()
)
rbNtpTmz.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpTmz.setStatus("current")
_RbNtpRowStatus_Type = RowStatus
_RbNtpRowStatus_Object = MibTableColumn
rbNtpRowStatus = _RbNtpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 31926, 25, 1, 1, 5),
    _RbNtpRowStatus_Type()
)
rbNtpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rbNtpRowStatus.setStatus("current")
_RadioBridgeLicense_ObjectIdentity = ObjectIdentity
radioBridgeLicense = _RadioBridgeLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31926, 26)
)
_RbLicenseTable_Object = MibTable
rbLicenseTable = _RbLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1)
)
if mibBuilder.loadTexts:
    rbLicenseTable.setStatus("current")
_RbLicenseEntry_Object = MibTableRow
rbLicenseEntry = _RbLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1)
)
rbLicenseEntry.setIndexNames(
    (1, "RADIO-BRIDGE-MIB", "rbLicenseId"),
)
if mibBuilder.loadTexts:
    rbLicenseEntry.setStatus("current")


class _RbLicenseId_Type(DisplayString):
    """Custom type rbLicenseId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbLicenseId_Type.__name__ = "DisplayString"
_RbLicenseId_Object = MibTableColumn
rbLicenseId = _RbLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1, 1),
    _RbLicenseId_Type()
)
rbLicenseId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbLicenseId.setStatus("current")
_RbLicenseCurrentValue_Type = Integer32
_RbLicenseCurrentValue_Object = MibTableColumn
rbLicenseCurrentValue = _RbLicenseCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1, 2),
    _RbLicenseCurrentValue_Type()
)
rbLicenseCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbLicenseCurrentValue.setStatus("current")
_RbLicenseMaxValue_Type = Integer32
_RbLicenseMaxValue_Object = MibTableColumn
rbLicenseMaxValue = _RbLicenseMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 31926, 26, 1, 1, 3),
    _RbLicenseMaxValue_Type()
)
rbLicenseMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbLicenseMaxValue.setStatus("current")
dot1agCfmMepEntry.registerAugmentions(
    ("RADIO-BRIDGE-MIB",
     "rbMepEntry")
)
rbMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
ieee8021QBridgeTpFdbEntry.registerAugmentions(
    ("RADIO-BRIDGE-MIB",
     "rbFdbExtensionEntry")
)
rbFdbExtensionEntry.setIndexNames(*ieee8021QBridgeTpFdbEntry.getIndexNames())

# Managed Objects groups


# Notification objects

trapModulationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 1)
)
trapModulationChange.setObjects(
      *(("RADIO-BRIDGE-MIB", "rfModulationType"),
        ("RADIO-BRIDGE-MIB", "rfNumOfSubchannels"),
        ("RADIO-BRIDGE-MIB", "rfNumOfRepetitions"),
        ("RADIO-BRIDGE-MIB", "rfFecRate"))
)
if mibBuilder.loadTexts:
    trapModulationChange.setStatus(
        "current"
    )

trapTemperatureOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 2)
)
if mibBuilder.loadTexts:
    trapTemperatureOutOfRange.setStatus(
        "current"
    )

trapTemperatureInRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 3)
)
if mibBuilder.loadTexts:
    trapTemperatureInRange.setStatus(
        "current"
    )

trapSfpIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 4)
)
trapSfpIn.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapSfpIn.setStatus(
        "current"
    )

trapSfpOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 5)
)
trapSfpOut.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapSfpOut.setStatus(
        "current"
    )

trapRefClockChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 6)
)
trapRefClockChanged.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RADIO-BRIDGE-MIB", "refClockQualityLevelActual"))
)
if mibBuilder.loadTexts:
    trapRefClockChanged.setStatus(
        "current"
    )

trapCurrentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 11)
)
trapCurrentAlarm.setObjects(
      *(("RADIO-BRIDGE-MIB", "rbCurrentAlarmChangeCounter"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmMostSevere"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmType"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmTypeName"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmSourceAddr"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmSource"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmSeverity"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmRaisedTime"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmIfIndex"),
        ("RADIO-BRIDGE-MIB", "rbCurrentAlarmLastTrapType"))
)
if mibBuilder.loadTexts:
    trapCurrentAlarm.setStatus(
        "current"
    )

trapLoopEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 12)
)
trapLoopEnabled.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapLoopEnabled.setStatus(
        "current"
    )

trapLoopDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 13)
)
trapLoopDisabled.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    trapLoopDisabled.setStatus(
        "current"
    )

trapTxMuteEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 14)
)
if mibBuilder.loadTexts:
    trapTxMuteEnabled.setStatus(
        "current"
    )

trapTxMuteDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 15)
)
if mibBuilder.loadTexts:
    trapTxMuteDisabled.setStatus(
        "current"
    )

trapCinrOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 19)
)
if mibBuilder.loadTexts:
    trapCinrOutOfRange.setStatus(
        "current"
    )

trapCinrInRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 20)
)
if mibBuilder.loadTexts:
    trapCinrInRange.setStatus(
        "current"
    )

trapRssiOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 21)
)
if mibBuilder.loadTexts:
    trapRssiOutOfRange.setStatus(
        "current"
    )

trapRssiInRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 22)
)
if mibBuilder.loadTexts:
    trapRssiInRange.setStatus(
        "current"
    )

trapLowestModulation = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 23)
)
if mibBuilder.loadTexts:
    trapLowestModulation.setStatus(
        "current"
    )

trapNoLowestModulation = NotificationType(
    (1, 3, 6, 1, 4, 1, 31926, 3, 24)
)
if mibBuilder.loadTexts:
    trapNoLowestModulation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADIO-BRIDGE-MIB",
    **{"AlarmSeverity": AlarmSeverity,
       "AlarmType": AlarmType,
       "radioBridgeRoot": radioBridgeRoot,
       "radioBridgeSystem": radioBridgeSystem,
       "rbSysVoltage": rbSysVoltage,
       "rbSysTemperature": rbSysTemperature,
       "rbSysSaveConfiguration": rbSysSaveConfiguration,
       "rbSysReset": rbSysReset,
       "rbSwBank1Version": rbSwBank1Version,
       "rbSwBank2Version": rbSwBank2Version,
       "rbSwBank1Running": rbSwBank1Running,
       "rbSwBank2Running": rbSwBank2Running,
       "rbSwBank1ScheduledToRunNextReset": rbSwBank1ScheduledToRunNextReset,
       "rbSwBank2ScheduledToRunNextReset": rbSwBank2ScheduledToRunNextReset,
       "rbSystemUpAbsoluteTime": rbSystemUpAbsoluteTime,
       "rbSystemAuthenticationMode": rbSystemAuthenticationMode,
       "rbSystemAuthenticationSecret": rbSystemAuthenticationSecret,
       "rbSystemCapabilities": rbSystemCapabilities,
       "rbDate": rbDate,
       "rbTime": rbTime,
       "radioBridgeRf": radioBridgeRf,
       "rbRfTable": rbRfTable,
       "rbRfEntry": rbRfEntry,
       "rfIndex": rfIndex,
       "rfNumOfChannels": rfNumOfChannels,
       "rfChannelWidth": rfChannelWidth,
       "rfOperationalFrequency": rfOperationalFrequency,
       "rfRole": rfRole,
       "rfModeSelector": rfModeSelector,
       "rfModulationType": rfModulationType,
       "rfNumOfSubchannels": rfNumOfSubchannels,
       "rfNumOfRepetitions": rfNumOfRepetitions,
       "rfFecRate": rfFecRate,
       "rfOperationalState": rfOperationalState,
       "rfAverageCinr": rfAverageCinr,
       "rfAverageRssi": rfAverageRssi,
       "rfTxSynthLock": rfTxSynthLock,
       "rfRxSynthLock": rfRxSynthLock,
       "rfRxLinkId": rfRxLinkId,
       "rfTxLinkId": rfTxLinkId,
       "rfTxState": rfTxState,
       "rfRxState": rfRxState,
       "rfTemperature": rfTemperature,
       "rfAsymmetry": rfAsymmetry,
       "rfLowestModulationType": rfLowestModulationType,
       "rfLowestNumOfSubchannels": rfLowestNumOfSubchannels,
       "rfLowestNumOfRepetitions": rfLowestNumOfRepetitions,
       "rfLowestFecRate": rfLowestFecRate,
       "rfTxMute": rfTxMute,
       "rfRoleStatus": rfRoleStatus,
       "rfLoopModeSelector": rfLoopModeSelector,
       "rfLoopModulationType": rfLoopModulationType,
       "rfLoopNumOfSubchannels": rfLoopNumOfSubchannels,
       "rfLoopNumOfRepetitions": rfLoopNumOfRepetitions,
       "rfLoopFecRate": rfLoopFecRate,
       "rfLoopTimeout": rfLoopTimeout,
       "rfTxPower": rfTxPower,
       "rfTxMuteTimeout": rfTxMuteTimeout,
       "rfAlignmentStatus": rfAlignmentStatus,
       "rfLoopDirection": rfLoopDirection,
       "rbRfStatisticsTable": rbRfStatisticsTable,
       "rbRfStatisticsEntry": rbRfStatisticsEntry,
       "rfInOctets": rfInOctets,
       "rfInIdleOctets": rfInIdleOctets,
       "rfInGoodOctets": rfInGoodOctets,
       "rfInErroredOctets": rfInErroredOctets,
       "rfOutOctets": rfOutOctets,
       "rfOutIdleOctets": rfOutIdleOctets,
       "rfInPkts": rfInPkts,
       "rfInGoodPkts": rfInGoodPkts,
       "rfInErroredPkts": rfInErroredPkts,
       "rfInLostPkts": rfInLostPkts,
       "rfOutPkts": rfOutPkts,
       "rfMinCinr": rfMinCinr,
       "rfMaxCinr": rfMaxCinr,
       "rfMinRssi": rfMinRssi,
       "rfMaxRssi": rfMaxRssi,
       "rfMinModulation": rfMinModulation,
       "rfMaxModulation": rfMaxModulation,
       "rfValid": rfValid,
       "rfArqInLoss": rfArqInLoss,
       "rfArqOutLoss": rfArqOutLoss,
       "rbRfStatisticsDaysTable": rbRfStatisticsDaysTable,
       "rbRfStatisticsDaysEntry": rbRfStatisticsDaysEntry,
       "rfDaysInOctets": rfDaysInOctets,
       "rfDaysInIdleOctets": rfDaysInIdleOctets,
       "rfDaysInGoodOctets": rfDaysInGoodOctets,
       "rfDaysInErroredOctets": rfDaysInErroredOctets,
       "rfDaysOutOctets": rfDaysOutOctets,
       "rfDaysOutIdleOctets": rfDaysOutIdleOctets,
       "rfDaysInPkts": rfDaysInPkts,
       "rfDaysInGoodPkts": rfDaysInGoodPkts,
       "rfDaysInErroredPkts": rfDaysInErroredPkts,
       "rfDaysInLostPkts": rfDaysInLostPkts,
       "rfDaysOutPkts": rfDaysOutPkts,
       "rfDaysMinCinr": rfDaysMinCinr,
       "rfDaysMaxCinr": rfDaysMaxCinr,
       "rfDaysMinRssi": rfDaysMinRssi,
       "rfDaysMaxRssi": rfDaysMaxRssi,
       "rfDaysMinModulation": rfDaysMinModulation,
       "rfDaysMaxModulation": rfDaysMaxModulation,
       "rfDaysValid": rfDaysValid,
       "rfDaysArqInLoss": rfDaysArqInLoss,
       "rfDaysArqOutLoss": rfDaysArqOutLoss,
       "rfDayIndex": rfDayIndex,
       "rfDaysStart": rfDaysStart,
       "radioBridgeTraps": radioBridgeTraps,
       "trapModulationChange": trapModulationChange,
       "trapTemperatureOutOfRange": trapTemperatureOutOfRange,
       "trapTemperatureInRange": trapTemperatureInRange,
       "trapSfpIn": trapSfpIn,
       "trapSfpOut": trapSfpOut,
       "trapRefClockChanged": trapRefClockChanged,
       "trapCurrentAlarm": trapCurrentAlarm,
       "trapLoopEnabled": trapLoopEnabled,
       "trapLoopDisabled": trapLoopDisabled,
       "trapTxMuteEnabled": trapTxMuteEnabled,
       "trapTxMuteDisabled": trapTxMuteDisabled,
       "trapCinrOutOfRange": trapCinrOutOfRange,
       "trapCinrInRange": trapCinrInRange,
       "trapRssiOutOfRange": trapRssiOutOfRange,
       "trapRssiInRange": trapRssiInRange,
       "trapLowestModulation": trapLowestModulation,
       "trapNoLowestModulation": trapNoLowestModulation,
       "radioBridgeRefClock": radioBridgeRefClock,
       "rbRefClockTable": rbRefClockTable,
       "rbRefClockEntry": rbRefClockEntry,
       "refClockPrio": refClockPrio,
       "refClockStatus": refClockStatus,
       "refClockQualityLevelActual": refClockQualityLevelActual,
       "refClockQualityLevelConfig": refClockQualityLevelConfig,
       "refClockQualityLevelMode": refClockQualityLevelMode,
       "refClockSsmCvid": refClockSsmCvid,
       "refClockRowStatus": refClockRowStatus,
       "radioBridgeEthernet": radioBridgeEthernet,
       "rbEthernetTable": rbEthernetTable,
       "rbEthernetEntry": rbEthernetEntry,
       "ethernetAlarmPropagation": ethernetAlarmPropagation,
       "ethernetLoopMode": ethernetLoopMode,
       "ethernetLoopTimeout": ethernetLoopTimeout,
       "ethernetNetworkType": ethernetNetworkType,
       "ethernetPcpWriteProfileId": ethernetPcpWriteProfileId,
       "ethernetClassifierMode": ethernetClassifierMode,
       "radioBridgeQosClassifier": radioBridgeQosClassifier,
       "rbClassifierCosTable": rbClassifierCosTable,
       "rbClassifierCosEntry": rbClassifierCosEntry,
       "classifierCosId": classifierCosId,
       "classifierCosPortList": classifierCosPortList,
       "classifierCosPrecedence": classifierCosPrecedence,
       "classifierCosVidList": classifierCosVidList,
       "classifierCosPcpList": classifierCosPcpList,
       "classifierCosCos": classifierCosCos,
       "classifierCosIpCosType": classifierCosIpCosType,
       "classifierCosIpCosList": classifierCosIpCosList,
       "classifierCosRowStatus": classifierCosRowStatus,
       "classifierCosPacketType": classifierCosPacketType,
       "rbClassifierEvcTable": rbClassifierEvcTable,
       "rbClassifierEvcEntry": rbClassifierEvcEntry,
       "classifierEvcId": classifierEvcId,
       "classifierEvcPortList": classifierEvcPortList,
       "classifierEvcPrecedence": classifierEvcPrecedence,
       "classifierEvcVidList": classifierEvcVidList,
       "classifierEvcPcpList": classifierEvcPcpList,
       "classifierEvcEvc": classifierEvcEvc,
       "classifierEvcIpCosType": classifierEvcIpCosType,
       "classifierEvcIpCosList": classifierEvcIpCosList,
       "classifierEvcRowStatus": classifierEvcRowStatus,
       "classifierEvcPacketType": classifierEvcPacketType,
       "radioBridgeQosIngressQueue": radioBridgeQosIngressQueue,
       "rbQosIngressQueueTable": rbQosIngressQueueTable,
       "rbQosIngressQueueEntry": rbQosIngressQueueEntry,
       "qosIngressQueueEvcId": qosIngressQueueEvcId,
       "qosIngressQueueCosId": qosIngressQueueCosId,
       "qosIngressQueueMeterId": qosIngressQueueMeterId,
       "qosIngressQueueMarking": qosIngressQueueMarking,
       "qosIngressQueueRowStatus": qosIngressQueueRowStatus,
       "radioBridgeQosEgressQueue": radioBridgeQosEgressQueue,
       "rbQosEgressQueueTable": rbQosEgressQueueTable,
       "rbQosEgressQueueEntry": rbQosEgressQueueEntry,
       "qosEgressQueuePortNum": qosEgressQueuePortNum,
       "qosEgressQueueCosId": qosEgressQueueCosId,
       "qosEgressQueueWfqWeight": qosEgressQueueWfqWeight,
       "qosEgressQueueCir": qosEgressQueueCir,
       "qosEgressQueueMode": qosEgressQueueMode,
       "qosEgressQueueColorDrop": qosEgressQueueColorDrop,
       "qosEgressDropMode": qosEgressDropMode,
       "radioBridgeIp": radioBridgeIp,
       "rbIpTable": rbIpTable,
       "rbIpEntry": rbIpEntry,
       "rbIpIndex": rbIpIndex,
       "rbIpAddress": rbIpAddress,
       "rbIpPrefixLen": rbIpPrefixLen,
       "rbIpVlanId": rbIpVlanId,
       "rbIpRowStatus": rbIpRowStatus,
       "rbIpType": rbIpType,
       "rbIpGateway": rbIpGateway,
       "radioBridgeCfm": radioBridgeCfm,
       "rbPeerMep": rbPeerMep,
       "rbPeerMepEntry": rbPeerMepEntry,
       "rbMdIndex": rbMdIndex,
       "rbMaIndex": rbMaIndex,
       "rbMepId": rbMepId,
       "rbPeerMepId": rbPeerMepId,
       "rbPeerMepFarEndLoss": rbPeerMepFarEndLoss,
       "rbPeerMepNearEndLoss": rbPeerMepNearEndLoss,
       "rbPeerMepTotalTxFarEnd": rbPeerMepTotalTxFarEnd,
       "rbPeerMepTotalTxNearEnd": rbPeerMepTotalTxNearEnd,
       "rbPeerMepFrameDelay": rbPeerMepFrameDelay,
       "rbPeerMepFrameDelayVariation": rbPeerMepFrameDelayVariation,
       "rbMep": rbMep,
       "rbMepEntry": rbMepEntry,
       "rbMepAisEnable": rbMepAisEnable,
       "rbMepAisPeriod": rbMepAisPeriod,
       "rbMepAisSuppress": rbMepAisSuppress,
       "rbMepAisLevel": rbMepAisLevel,
       "rbMepAisDefects": rbMepAisDefects,
       "radioBridgeAlarms": radioBridgeAlarms,
       "rbAlarmsCommon": rbAlarmsCommon,
       "rbCurrentAlarmChangeCounter": rbCurrentAlarmChangeCounter,
       "rbCurrentAlarmMostSevere": rbCurrentAlarmMostSevere,
       "rbCurrentAlarmLastIndex": rbCurrentAlarmLastIndex,
       "rbCurrentAlarmLastTrapType": rbCurrentAlarmLastTrapType,
       "rbCurrentAlarmSourceAddr": rbCurrentAlarmSourceAddr,
       "rbCurrentAlarmTable": rbCurrentAlarmTable,
       "rbCurrentAlarmEntry": rbCurrentAlarmEntry,
       "rbCurrentAlarmIndex": rbCurrentAlarmIndex,
       "rbCurrentAlarmType": rbCurrentAlarmType,
       "rbCurrentAlarmTypeName": rbCurrentAlarmTypeName,
       "rbCurrentAlarmSource": rbCurrentAlarmSource,
       "rbCurrentAlarmSeverity": rbCurrentAlarmSeverity,
       "rbCurrentAlarmRaisedTime": rbCurrentAlarmRaisedTime,
       "rbCurrentAlarmDesc": rbCurrentAlarmDesc,
       "rbCurrentAlarmCause": rbCurrentAlarmCause,
       "rbCurrentAlarmAction": rbCurrentAlarmAction,
       "rbCurrentAlarmIfIndex": rbCurrentAlarmIfIndex,
       "radioBridgeScheduler": radioBridgeScheduler,
       "rbSchedulerMode": rbSchedulerMode,
       "radioBridgeEncryption": radioBridgeEncryption,
       "rbRfEncryption": rbRfEncryption,
       "rbRfStaticKey": rbRfStaticKey,
       "rbRfAuthenticationString": rbRfAuthenticationString,
       "radioBridgeMeter": radioBridgeMeter,
       "rbMeterTable": rbMeterTable,
       "rbMeterEntry": rbMeterEntry,
       "rbMeterId": rbMeterId,
       "rbMeterCir": rbMeterCir,
       "rbMeterCbs": rbMeterCbs,
       "rbMeterEir": rbMeterEir,
       "rbMeterEbs": rbMeterEbs,
       "rbMeterColorMode": rbMeterColorMode,
       "rbMeterRowStatus": rbMeterRowStatus,
       "radioBridgeEventConfig": radioBridgeEventConfig,
       "rbEventConfigTable": rbEventConfigTable,
       "rbEventConfigEntry": rbEventConfigEntry,
       "rbEventConfigIndex": rbEventConfigIndex,
       "rbEventConfigId": rbEventConfigId,
       "rbEventConfigMask": rbEventConfigMask,
       "radioBridgeSnmp": radioBridgeSnmp,
       "rbAgentReadCommunity": rbAgentReadCommunity,
       "rbAgentWriteCommunity": rbAgentWriteCommunity,
       "rbAgentSnmpVersion": rbAgentSnmpVersion,
       "rbSysFileOperationTable": rbSysFileOperationTable,
       "rbSysFileOperationEntry": rbSysFileOperationEntry,
       "fileSessionIndex": fileSessionIndex,
       "fileSessionCommand": fileSessionCommand,
       "fileSessionLocalParams": fileSessionLocalParams,
       "fileSessionRemotePath": fileSessionRemotePath,
       "fileSessionServer": fileSessionServer,
       "fileSessionUser": fileSessionUser,
       "fileSessionPassword": fileSessionPassword,
       "fileSessionResult": fileSessionResult,
       "fileSessionState": fileSessionState,
       "fileSessionRowStatus": fileSessionRowStatus,
       "fileSessionProtocol": fileSessionProtocol,
       "radioBridgeLldp": radioBridgeLldp,
       "rbLldpPortExtensionTable": rbLldpPortExtensionTable,
       "rbLldpPortExtensionEntry": rbLldpPortExtensionEntry,
       "rbLldpPortIfIndex": rbLldpPortIfIndex,
       "rbLldpPortDestAddressIndex": rbLldpPortDestAddressIndex,
       "rbLldpPortVid": rbLldpPortVid,
       "radioBridgeWred": radioBridgeWred,
       "rbWredTable": rbWredTable,
       "rbWredEntry": rbWredEntry,
       "rbWredId": rbWredId,
       "rbWredNfactor": rbWredNfactor,
       "rbWredMinThreshold": rbWredMinThreshold,
       "rbWredMaxThreshold": rbWredMaxThreshold,
       "rbWredProbability": rbWredProbability,
       "rbWredMinThresholdYellow": rbWredMinThresholdYellow,
       "rbWredMaxThresholdYellow": rbWredMaxThresholdYellow,
       "rbWredProbabilityYellow": rbWredProbabilityYellow,
       "rbWredRowStatus": rbWredRowStatus,
       "radioBridgeAuthentication": radioBridgeAuthentication,
       "rbAuthServersTable": rbAuthServersTable,
       "rbAuthServersEntry": rbAuthServersEntry,
       "rbAuthServerId": rbAuthServerId,
       "rbAuthServerIpAddress": rbAuthServerIpAddress,
       "rbAuthServerPort": rbAuthServerPort,
       "rbAuthServerRowStatus": rbAuthServerRowStatus,
       "radioBridgeQuota": radioBridgeQuota,
       "rbFdbQuotaTable": rbFdbQuotaTable,
       "rbFdbQuotaEntry": rbFdbQuotaEntry,
       "rbFdbQuotaId": rbFdbQuotaId,
       "rbFdbQuotaSize": rbFdbQuotaSize,
       "rbFdbQuotaRowStatus": rbFdbQuotaRowStatus,
       "rbFdbQuotaMaxSize": rbFdbQuotaMaxSize,
       "rbFdbQuotaUsedEntries": rbFdbQuotaUsedEntries,
       "rbFdbQuotaStaticEntries": rbFdbQuotaStaticEntries,
       "rbFdbQuotaDynamicEntries": rbFdbQuotaDynamicEntries,
       "rbFdbQuotaUnusedEntries": rbFdbQuotaUnusedEntries,
       "rbFdbEvcQuotaTable": rbFdbEvcQuotaTable,
       "rbFdbEvcQuotaEntry": rbFdbEvcQuotaEntry,
       "rbFdbEvcQuotaId": rbFdbEvcQuotaId,
       "rbRefEvcId": rbRefEvcId,
       "rbRefFdbQuotaId": rbRefFdbQuotaId,
       "rbFdbEvcQuotaRowStatus": rbFdbEvcQuotaRowStatus,
       "rbFdbExtensionTable": rbFdbExtensionTable,
       "rbFdbExtensionEntry": rbFdbExtensionEntry,
       "rbRefExtFdbQuotaId": rbRefExtFdbQuotaId,
       "radioBridgePcpProfile": radioBridgePcpProfile,
       "rbPcpWriteProfileTable": rbPcpWriteProfileTable,
       "rbPcpWriteProfileEntry": rbPcpWriteProfileEntry,
       "rbPcpWriteProfileId": rbPcpWriteProfileId,
       "rbPcpWriteProfilePcp": rbPcpWriteProfilePcp,
       "rbPcpWriteProfileRowStatus": rbPcpWriteProfileRowStatus,
       "radioBridgeSyslog": radioBridgeSyslog,
       "rbSyslogTable": rbSyslogTable,
       "rbSyslogEntry": rbSyslogEntry,
       "rbSyslogId": rbSyslogId,
       "rbSyslogServerIp": rbSyslogServerIp,
       "rbSyslogRowStatus": rbSyslogRowStatus,
       "radioBridgeNtp": radioBridgeNtp,
       "rbNtpTable": rbNtpTable,
       "rbNtpEntry": rbNtpEntry,
       "rbNtpId": rbNtpId,
       "rbNtpServerIp": rbNtpServerIp,
       "rbNtpSecondaryServerIp": rbNtpSecondaryServerIp,
       "rbNtpTmz": rbNtpTmz,
       "rbNtpRowStatus": rbNtpRowStatus,
       "radioBridgeLicense": radioBridgeLicense,
       "rbLicenseTable": rbLicenseTable,
       "rbLicenseEntry": rbLicenseEntry,
       "rbLicenseId": rbLicenseId,
       "rbLicenseCurrentValue": rbLicenseCurrentValue,
       "rbLicenseMaxValue": rbLicenseMaxValue}
)
