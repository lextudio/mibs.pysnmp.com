# SNMP MIB module (DL-SLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DL-SLA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:30 2024
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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Digital_link_ObjectIdentity = ObjectIdentity
digital_link = _Digital_link_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300)
)
_Dl_ServiceLevelAgreement_ObjectIdentity = ObjectIdentity
dl_ServiceLevelAgreement = _Dl_ServiceLevelAgreement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260)
)
_DlcSLAConfigurationGroup_ObjectIdentity = ObjectIdentity
dlcSLAConfigurationGroup = _DlcSLAConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260, 1)
)
_UnitSLAConfiguration_ObjectIdentity = ObjectIdentity
unitSLAConfiguration = _UnitSLAConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1)
)


class _ConfigSLA_Type(Integer32):
    """Custom type configSLA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ConfigSLA_Type.__name__ = "Integer32"
_ConfigSLA_Object = MibScalar
configSLA = _ConfigSLA_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 1),
    _ConfigSLA_Type()
)
configSLA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSLA.setStatus("mandatory")


class _UnitSamplingPeriodForFDR_DDR_Type(Integer32):
    """Custom type unitSamplingPeriodForFDR_DDR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UnitSamplingPeriodForFDR_DDR_Type.__name__ = "Integer32"
_UnitSamplingPeriodForFDR_DDR_Object = MibScalar
unitSamplingPeriodForFDR_DDR = _UnitSamplingPeriodForFDR_DDR_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 2),
    _UnitSamplingPeriodForFDR_DDR_Type()
)
unitSamplingPeriodForFDR_DDR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSamplingPeriodForFDR_DDR.setStatus("mandatory")


class _UnitSamplingPeriodForDelayMeasurement_Type(Integer32):
    """Custom type unitSamplingPeriodForDelayMeasurement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UnitSamplingPeriodForDelayMeasurement_Type.__name__ = "Integer32"
_UnitSamplingPeriodForDelayMeasurement_Object = MibScalar
unitSamplingPeriodForDelayMeasurement = _UnitSamplingPeriodForDelayMeasurement_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 3),
    _UnitSamplingPeriodForDelayMeasurement_Type()
)
unitSamplingPeriodForDelayMeasurement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitSamplingPeriodForDelayMeasurement.setStatus("mandatory")


class _UnitThresholdForFDR_Type(Integer32):
    """Custom type unitThresholdForFDR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_UnitThresholdForFDR_Type.__name__ = "Integer32"
_UnitThresholdForFDR_Object = MibScalar
unitThresholdForFDR = _UnitThresholdForFDR_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 4),
    _UnitThresholdForFDR_Type()
)
unitThresholdForFDR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitThresholdForFDR.setStatus("mandatory")


class _UnitThresholdForDDR_Type(Integer32):
    """Custom type unitThresholdForDDR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_UnitThresholdForDDR_Type.__name__ = "Integer32"
_UnitThresholdForDDR_Object = MibScalar
unitThresholdForDDR = _UnitThresholdForDDR_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 5),
    _UnitThresholdForDDR_Type()
)
unitThresholdForDDR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitThresholdForDDR.setStatus("mandatory")


class _UnitDelayMeasurementPacketSize_Type(Integer32):
    """Custom type unitDelayMeasurementPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 1500),
    )


_UnitDelayMeasurementPacketSize_Type.__name__ = "Integer32"
_UnitDelayMeasurementPacketSize_Object = MibScalar
unitDelayMeasurementPacketSize = _UnitDelayMeasurementPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 6),
    _UnitDelayMeasurementPacketSize_Type()
)
unitDelayMeasurementPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitDelayMeasurementPacketSize.setStatus("mandatory")
_UnitOamDomainIdentifier_Type = Counter32
_UnitOamDomainIdentifier_Object = MibScalar
unitOamDomainIdentifier = _UnitOamDomainIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 7),
    _UnitOamDomainIdentifier_Type()
)
unitOamDomainIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOamDomainIdentifier.setStatus("mandatory")
_UnitOamLocationIdentifier_Type = Counter32
_UnitOamLocationIdentifier_Object = MibScalar
unitOamLocationIdentifier = _UnitOamLocationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 1, 8),
    _UnitOamLocationIdentifier_Type()
)
unitOamLocationIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unitOamLocationIdentifier.setStatus("mandatory")
_PerDLCIConfiguration_ObjectIdentity = ObjectIdentity
perDLCIConfiguration = _PerDLCIConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2)
)
_ConfigurationPerDLCITable_Object = MibTable
configurationPerDLCITable = _ConfigurationPerDLCITable_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1)
)
if mibBuilder.loadTexts:
    configurationPerDLCITable.setStatus("mandatory")
_ConfigurationPerDLCIEntry_Object = MibTableRow
configurationPerDLCIEntry = _ConfigurationPerDLCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1)
)
configurationPerDLCIEntry.setIndexNames(
    (0, "DL-SLA-MIB", "configurationPerDLCITableIndex"),
)
if mibBuilder.loadTexts:
    configurationPerDLCIEntry.setStatus("mandatory")
_ConfigurationPerDLCITableIndex_Type = Integer32
_ConfigurationPerDLCITableIndex_Object = MibTableColumn
configurationPerDLCITableIndex = _ConfigurationPerDLCITableIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 1),
    _ConfigurationPerDLCITableIndex_Type()
)
configurationPerDLCITableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configurationPerDLCITableIndex.setStatus("mandatory")


class _CommitedInformationRatePerDLCI_Type(Integer32):
    """Custom type commitedInformationRatePerDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1536000),
    )


_CommitedInformationRatePerDLCI_Type.__name__ = "Integer32"
_CommitedInformationRatePerDLCI_Object = MibTableColumn
commitedInformationRatePerDLCI = _CommitedInformationRatePerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 2),
    _CommitedInformationRatePerDLCI_Type()
)
commitedInformationRatePerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    commitedInformationRatePerDLCI.setStatus("mandatory")
_RemoteDLCIPerDLCI_Type = Integer32
_RemoteDLCIPerDLCI_Object = MibTableColumn
remoteDLCIPerDLCI = _RemoteDLCIPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 3),
    _RemoteDLCIPerDLCI_Type()
)
remoteDLCIPerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteDLCIPerDLCI.setStatus("mandatory")
_RemoteIpAddressPerDLCI_Type = IpAddress
_RemoteIpAddressPerDLCI_Object = MibTableColumn
remoteIpAddressPerDLCI = _RemoteIpAddressPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 4),
    _RemoteIpAddressPerDLCI_Type()
)
remoteIpAddressPerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteIpAddressPerDLCI.setStatus("mandatory")


class _ThresholdForDelayMeasurementsPerDLCI_Type(Integer32):
    """Custom type thresholdForDelayMeasurementsPerDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_ThresholdForDelayMeasurementsPerDLCI_Type.__name__ = "Integer32"
_ThresholdForDelayMeasurementsPerDLCI_Object = MibTableColumn
thresholdForDelayMeasurementsPerDLCI = _ThresholdForDelayMeasurementsPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 1, 2, 1, 1, 5),
    _ThresholdForDelayMeasurementsPerDLCI_Type()
)
thresholdForDelayMeasurementsPerDLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdForDelayMeasurementsPerDLCI.setStatus("mandatory")
_DlcSLAStatisticsGroup_ObjectIdentity = ObjectIdentity
dlcSLAStatisticsGroup = _DlcSLAStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260, 2)
)
_DlcDeliveryRatioStatistics_ObjectIdentity = ObjectIdentity
dlcDeliveryRatioStatistics = _DlcDeliveryRatioStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1)
)
_DeliveryRatioPerDLCITable_Object = MibTable
deliveryRatioPerDLCITable = _DeliveryRatioPerDLCITable_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1)
)
if mibBuilder.loadTexts:
    deliveryRatioPerDLCITable.setStatus("mandatory")
_DeliveryRatioPerDLCIEntry_Object = MibTableRow
deliveryRatioPerDLCIEntry = _DeliveryRatioPerDLCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1)
)
deliveryRatioPerDLCIEntry.setIndexNames(
    (0, "DL-SLA-MIB", "deliveryRatioPerDLCITableIndex"),
)
if mibBuilder.loadTexts:
    deliveryRatioPerDLCIEntry.setStatus("mandatory")
_DeliveryRatioPerDLCITableIndex_Type = Integer32
_DeliveryRatioPerDLCITableIndex_Object = MibTableColumn
deliveryRatioPerDLCITableIndex = _DeliveryRatioPerDLCITableIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 1),
    _DeliveryRatioPerDLCITableIndex_Type()
)
deliveryRatioPerDLCITableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deliveryRatioPerDLCITableIndex.setStatus("mandatory")
_DeliveryTableEncodedValue_Type = OctetString
_DeliveryTableEncodedValue_Object = MibTableColumn
deliveryTableEncodedValue = _DeliveryTableEncodedValue_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 2),
    _DeliveryTableEncodedValue_Type()
)
deliveryTableEncodedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deliveryTableEncodedValue.setStatus("mandatory")
_DeliveryTableTimestamp_Type = Counter32
_DeliveryTableTimestamp_Object = MibTableColumn
deliveryTableTimestamp = _DeliveryTableTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 3),
    _DeliveryTableTimestamp_Type()
)
deliveryTableTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deliveryTableTimestamp.setStatus("obsolete")
_FTCLperDLCI_Type = Counter32
_FTCLperDLCI_Object = MibTableColumn
fTCLperDLCI = _FTCLperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 4),
    _FTCLperDLCI_Type()
)
fTCLperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTCLperDLCI.setStatus("mandatory")
_FTELperDLCI_Type = Counter32
_FTELperDLCI_Object = MibTableColumn
fTELperDLCI = _FTELperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 5),
    _FTELperDLCI_Type()
)
fTELperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTELperDLCI.setStatus("mandatory")
_FRCLperDLCI_Type = Counter32
_FRCLperDLCI_Object = MibTableColumn
fRCLperDLCI = _FRCLperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 6),
    _FRCLperDLCI_Type()
)
fRCLperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRCLperDLCI.setStatus("mandatory")
_FRELperDLCI_Type = Counter32
_FRELperDLCI_Object = MibTableColumn
fRELperDLCI = _FRELperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 7),
    _FRELperDLCI_Type()
)
fRELperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRELperDLCI.setStatus("mandatory")
_FTCRperDLCI_Type = Counter32
_FTCRperDLCI_Object = MibTableColumn
fTCRperDLCI = _FTCRperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 8),
    _FTCRperDLCI_Type()
)
fTCRperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTCRperDLCI.setStatus("mandatory")
_FTERperDLCI_Type = Counter32
_FTERperDLCI_Object = MibTableColumn
fTERperDLCI = _FTERperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 9),
    _FTERperDLCI_Type()
)
fTERperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTERperDLCI.setStatus("mandatory")
_FRCRperDLCI_Type = Counter32
_FRCRperDLCI_Object = MibTableColumn
fRCRperDLCI = _FRCRperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 10),
    _FRCRperDLCI_Type()
)
fRCRperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRCRperDLCI.setStatus("mandatory")
_FRERperDLCI_Type = Counter32
_FRERperDLCI_Object = MibTableColumn
fRERperDLCI = _FRERperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 11),
    _FRERperDLCI_Type()
)
fRERperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRERperDLCI.setStatus("mandatory")
_FDRNumberOfSamplesTaken_Type = Counter32
_FDRNumberOfSamplesTaken_Object = MibTableColumn
fDRNumberOfSamplesTaken = _FDRNumberOfSamplesTaken_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 12),
    _FDRNumberOfSamplesTaken_Type()
)
fDRNumberOfSamplesTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fDRNumberOfSamplesTaken.setStatus("obsolete")
_FDRNumberOfThresholdViolations_Type = Counter32
_FDRNumberOfThresholdViolations_Object = MibTableColumn
fDRNumberOfThresholdViolations = _FDRNumberOfThresholdViolations_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 13),
    _FDRNumberOfThresholdViolations_Type()
)
fDRNumberOfThresholdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fDRNumberOfThresholdViolations.setStatus("obsolete")
_DTCLperDLCI_Type = Counter32
_DTCLperDLCI_Object = MibTableColumn
dTCLperDLCI = _DTCLperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 14),
    _DTCLperDLCI_Type()
)
dTCLperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTCLperDLCI.setStatus("mandatory")
_DTELperDLCI_Type = Counter32
_DTELperDLCI_Object = MibTableColumn
dTELperDLCI = _DTELperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 15),
    _DTELperDLCI_Type()
)
dTELperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTELperDLCI.setStatus("mandatory")
_DRCLperDLCI_Type = Counter32
_DRCLperDLCI_Object = MibTableColumn
dRCLperDLCI = _DRCLperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 16),
    _DRCLperDLCI_Type()
)
dRCLperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dRCLperDLCI.setStatus("mandatory")
_DRELperDLCI_Type = Counter32
_DRELperDLCI_Object = MibTableColumn
dRELperDLCI = _DRELperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 17),
    _DRELperDLCI_Type()
)
dRELperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dRELperDLCI.setStatus("mandatory")
_DTCRperDLCI_Type = Counter32
_DTCRperDLCI_Object = MibTableColumn
dTCRperDLCI = _DTCRperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 18),
    _DTCRperDLCI_Type()
)
dTCRperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTCRperDLCI.setStatus("mandatory")
_DTERperDLCI_Type = Counter32
_DTERperDLCI_Object = MibTableColumn
dTERperDLCI = _DTERperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 19),
    _DTERperDLCI_Type()
)
dTERperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTERperDLCI.setStatus("mandatory")
_DRCRperDLCI_Type = Counter32
_DRCRperDLCI_Object = MibTableColumn
dRCRperDLCI = _DRCRperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 20),
    _DRCRperDLCI_Type()
)
dRCRperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dRCRperDLCI.setStatus("mandatory")
_DRERperDLCI_Type = Counter32
_DRERperDLCI_Object = MibTableColumn
dRERperDLCI = _DRERperDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 21),
    _DRERperDLCI_Type()
)
dRERperDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dRERperDLCI.setStatus("mandatory")
_DDRNumberOfSamplesTaken_Type = Counter32
_DDRNumberOfSamplesTaken_Object = MibTableColumn
dDRNumberOfSamplesTaken = _DDRNumberOfSamplesTaken_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 22),
    _DDRNumberOfSamplesTaken_Type()
)
dDRNumberOfSamplesTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDRNumberOfSamplesTaken.setStatus("obsolete")
_DDRNumberOfThresholdViolations_Type = Counter32
_DDRNumberOfThresholdViolations_Object = MibTableColumn
dDRNumberOfThresholdViolations = _DDRNumberOfThresholdViolations_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 23),
    _DDRNumberOfThresholdViolations_Type()
)
dDRNumberOfThresholdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dDRNumberOfThresholdViolations.setStatus("obsolete")
_TxFDRTimestamp_Type = Counter32
_TxFDRTimestamp_Object = MibTableColumn
txFDRTimestamp = _TxFDRTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 24),
    _TxFDRTimestamp_Type()
)
txFDRTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFDRTimestamp.setStatus("mandatory")
_TxFDRNumberOfSamplesTaken_Type = Counter32
_TxFDRNumberOfSamplesTaken_Object = MibTableColumn
txFDRNumberOfSamplesTaken = _TxFDRNumberOfSamplesTaken_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 25),
    _TxFDRNumberOfSamplesTaken_Type()
)
txFDRNumberOfSamplesTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFDRNumberOfSamplesTaken.setStatus("mandatory")
_TxFDRNumberOfThresholdViolations_Type = Counter32
_TxFDRNumberOfThresholdViolations_Object = MibTableColumn
txFDRNumberOfThresholdViolations = _TxFDRNumberOfThresholdViolations_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 26),
    _TxFDRNumberOfThresholdViolations_Type()
)
txFDRNumberOfThresholdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFDRNumberOfThresholdViolations.setStatus("mandatory")
_RxFDRTimestamp_Type = Counter32
_RxFDRTimestamp_Object = MibTableColumn
rxFDRTimestamp = _RxFDRTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 27),
    _RxFDRTimestamp_Type()
)
rxFDRTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFDRTimestamp.setStatus("mandatory")
_RxFDRNumberOfSamplesTaken_Type = Counter32
_RxFDRNumberOfSamplesTaken_Object = MibTableColumn
rxFDRNumberOfSamplesTaken = _RxFDRNumberOfSamplesTaken_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 28),
    _RxFDRNumberOfSamplesTaken_Type()
)
rxFDRNumberOfSamplesTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFDRNumberOfSamplesTaken.setStatus("mandatory")
_RxFDRNumberOfThresholdViolations_Type = Counter32
_RxFDRNumberOfThresholdViolations_Object = MibTableColumn
rxFDRNumberOfThresholdViolations = _RxFDRNumberOfThresholdViolations_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 29),
    _RxFDRNumberOfThresholdViolations_Type()
)
rxFDRNumberOfThresholdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFDRNumberOfThresholdViolations.setStatus("mandatory")
_TxDDRTimestamp_Type = Counter32
_TxDDRTimestamp_Object = MibTableColumn
txDDRTimestamp = _TxDDRTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 30),
    _TxDDRTimestamp_Type()
)
txDDRTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDDRTimestamp.setStatus("mandatory")
_TxDDRNumberOfSamplesTaken_Type = Counter32
_TxDDRNumberOfSamplesTaken_Object = MibTableColumn
txDDRNumberOfSamplesTaken = _TxDDRNumberOfSamplesTaken_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 31),
    _TxDDRNumberOfSamplesTaken_Type()
)
txDDRNumberOfSamplesTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDDRNumberOfSamplesTaken.setStatus("mandatory")
_TxDDRNumberOfThresholdViolations_Type = Counter32
_TxDDRNumberOfThresholdViolations_Object = MibTableColumn
txDDRNumberOfThresholdViolations = _TxDDRNumberOfThresholdViolations_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 32),
    _TxDDRNumberOfThresholdViolations_Type()
)
txDDRNumberOfThresholdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDDRNumberOfThresholdViolations.setStatus("mandatory")
_RxDDRTimestamp_Type = Counter32
_RxDDRTimestamp_Object = MibTableColumn
rxDDRTimestamp = _RxDDRTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 33),
    _RxDDRTimestamp_Type()
)
rxDDRTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDDRTimestamp.setStatus("mandatory")
_RxDDRNumberOfSamplesTaken_Type = Counter32
_RxDDRNumberOfSamplesTaken_Object = MibTableColumn
rxDDRNumberOfSamplesTaken = _RxDDRNumberOfSamplesTaken_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 34),
    _RxDDRNumberOfSamplesTaken_Type()
)
rxDDRNumberOfSamplesTaken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDDRNumberOfSamplesTaken.setStatus("mandatory")
_RxDDRNumberOfThresholdViolations_Type = Counter32
_RxDDRNumberOfThresholdViolations_Object = MibTableColumn
rxDDRNumberOfThresholdViolations = _RxDDRNumberOfThresholdViolations_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 35),
    _RxDDRNumberOfThresholdViolations_Type()
)
rxDDRNumberOfThresholdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDDRNumberOfThresholdViolations.setStatus("mandatory")
_TxDiscardEligible_Type = Counter32
_TxDiscardEligible_Object = MibTableColumn
txDiscardEligible = _TxDiscardEligible_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 36),
    _TxDiscardEligible_Type()
)
txDiscardEligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDiscardEligible.setStatus("mandatory")
_RxDiscardEligible_Type = Counter32
_RxDiscardEligible_Object = MibTableColumn
rxDiscardEligible = _RxDiscardEligible_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 37),
    _RxDiscardEligible_Type()
)
rxDiscardEligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDiscardEligible.setStatus("mandatory")
_TxFECN_Type = Counter32
_TxFECN_Object = MibTableColumn
txFECN = _TxFECN_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 38),
    _TxFECN_Type()
)
txFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txFECN.setStatus("mandatory")
_RxFECN_Type = Counter32
_RxFECN_Object = MibTableColumn
rxFECN = _RxFECN_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 39),
    _RxFECN_Type()
)
rxFECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxFECN.setStatus("mandatory")
_TxBECN_Type = Counter32
_TxBECN_Object = MibTableColumn
txBECN = _TxBECN_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 40),
    _TxBECN_Type()
)
txBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txBECN.setStatus("mandatory")
_RxBECN_Type = Counter32
_RxBECN_Object = MibTableColumn
rxBECN = _RxBECN_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 1, 1, 1, 41),
    _RxBECN_Type()
)
rxBECN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxBECN.setStatus("mandatory")
_DlcDelayStatistics_ObjectIdentity = ObjectIdentity
dlcDelayStatistics = _DlcDelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2)
)
_DelayPerDLCITable_Object = MibTable
delayPerDLCITable = _DelayPerDLCITable_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1)
)
if mibBuilder.loadTexts:
    delayPerDLCITable.setStatus("mandatory")
_DelayPerDLCIEntry_Object = MibTableRow
delayPerDLCIEntry = _DelayPerDLCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1)
)
delayPerDLCIEntry.setIndexNames(
    (0, "DL-SLA-MIB", "delayPerDLCITableIndex"),
)
if mibBuilder.loadTexts:
    delayPerDLCIEntry.setStatus("mandatory")
_DelayPerDLCITableIndex_Type = Integer32
_DelayPerDLCITableIndex_Object = MibTableColumn
delayPerDLCITableIndex = _DelayPerDLCITableIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 1),
    _DelayPerDLCITableIndex_Type()
)
delayPerDLCITableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayPerDLCITableIndex.setStatus("mandatory")
_DelayTableEncodedValue_Type = OctetString
_DelayTableEncodedValue_Object = MibTableColumn
delayTableEncodedValue = _DelayTableEncodedValue_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 2),
    _DelayTableEncodedValue_Type()
)
delayTableEncodedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayTableEncodedValue.setStatus("mandatory")
_DelayTableTimestamp_Type = Counter32
_DelayTableTimestamp_Object = MibTableColumn
delayTableTimestamp = _DelayTableTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 3),
    _DelayTableTimestamp_Type()
)
delayTableTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayTableTimestamp.setStatus("mandatory")
_TotalRoundTripDelayPerDLCI_Type = Counter32
_TotalRoundTripDelayPerDLCI_Object = MibTableColumn
totalRoundTripDelayPerDLCI = _TotalRoundTripDelayPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 4),
    _TotalRoundTripDelayPerDLCI_Type()
)
totalRoundTripDelayPerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalRoundTripDelayPerDLCI.setStatus("mandatory")
_MaximumRoundTripDelayNSamplesPerDLCI_Type = Counter32
_MaximumRoundTripDelayNSamplesPerDLCI_Object = MibTableColumn
maximumRoundTripDelayNSamplesPerDLCI = _MaximumRoundTripDelayNSamplesPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 5),
    _MaximumRoundTripDelayNSamplesPerDLCI_Type()
)
maximumRoundTripDelayNSamplesPerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumRoundTripDelayNSamplesPerDLCI.setStatus("mandatory")
_MaximumRoundTripDelay2NSamplesPerDLCI_Type = Counter32
_MaximumRoundTripDelay2NSamplesPerDLCI_Object = MibTableColumn
maximumRoundTripDelay2NSamplesPerDLCI = _MaximumRoundTripDelay2NSamplesPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 6),
    _MaximumRoundTripDelay2NSamplesPerDLCI_Type()
)
maximumRoundTripDelay2NSamplesPerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumRoundTripDelay2NSamplesPerDLCI.setStatus("mandatory")
_MaximumRoundTripDelay4NSamplesPerDLCI_Type = Counter32
_MaximumRoundTripDelay4NSamplesPerDLCI_Object = MibTableColumn
maximumRoundTripDelay4NSamplesPerDLCI = _MaximumRoundTripDelay4NSamplesPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 7),
    _MaximumRoundTripDelay4NSamplesPerDLCI_Type()
)
maximumRoundTripDelay4NSamplesPerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumRoundTripDelay4NSamplesPerDLCI.setStatus("mandatory")
_NumberOfDelayMeasurementsPerDLCI_Type = Counter32
_NumberOfDelayMeasurementsPerDLCI_Object = MibTableColumn
numberOfDelayMeasurementsPerDLCI = _NumberOfDelayMeasurementsPerDLCI_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 8),
    _NumberOfDelayMeasurementsPerDLCI_Type()
)
numberOfDelayMeasurementsPerDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfDelayMeasurementsPerDLCI.setStatus("mandatory")
_DelayNumberOfThresholdViolations_Type = Counter32
_DelayNumberOfThresholdViolations_Object = MibTableColumn
delayNumberOfThresholdViolations = _DelayNumberOfThresholdViolations_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 2, 1, 1, 9),
    _DelayNumberOfThresholdViolations_Type()
)
delayNumberOfThresholdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    delayNumberOfThresholdViolations.setStatus("mandatory")
_DlcOutageStatistics_ObjectIdentity = ObjectIdentity
dlcOutageStatistics = _DlcOutageStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3)
)
_OutagePerDLCITable_Object = MibTable
outagePerDLCITable = _OutagePerDLCITable_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1)
)
if mibBuilder.loadTexts:
    outagePerDLCITable.setStatus("mandatory")
_OutagePerDLCIEntry_Object = MibTableRow
outagePerDLCIEntry = _OutagePerDLCIEntry_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1)
)
outagePerDLCIEntry.setIndexNames(
    (0, "DL-SLA-MIB", "outageTableIndex"),
)
if mibBuilder.loadTexts:
    outagePerDLCIEntry.setStatus("mandatory")
_OutageTableIndex_Type = Integer32
_OutageTableIndex_Object = MibTableColumn
outageTableIndex = _OutageTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 1),
    _OutageTableIndex_Type()
)
outageTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outageTableIndex.setStatus("mandatory")
_OutageTableEncodedValue_Type = OctetString
_OutageTableEncodedValue_Object = MibTableColumn
outageTableEncodedValue = _OutageTableEncodedValue_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 2),
    _OutageTableEncodedValue_Type()
)
outageTableEncodedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outageTableEncodedValue.setStatus("mandatory")
_OutageTableTimestamp_Type = Counter32
_OutageTableTimestamp_Object = MibTableColumn
outageTableTimestamp = _OutageTableTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 3),
    _OutageTableTimestamp_Type()
)
outageTableTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outageTableTimestamp.setStatus("mandatory")


class _OutageStatus_Type(Integer32):
    """Custom type outageStatus based on Integer32"""
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
        *(("excluded-outage", 3),
          ("included-outage", 4),
          ("no-outage", 2),
          ("unknown", 1))
    )


_OutageStatus_Type.__name__ = "Integer32"
_OutageStatus_Object = MibTableColumn
outageStatus = _OutageStatus_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 4),
    _OutageStatus_Type()
)
outageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outageStatus.setStatus("mandatory")
_NumberOfOutageCounter_Type = Counter32
_NumberOfOutageCounter_Object = MibTableColumn
numberOfOutageCounter = _NumberOfOutageCounter_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 5),
    _NumberOfOutageCounter_Type()
)
numberOfOutageCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfOutageCounter.setStatus("mandatory")
_PeriodOfOutages_Type = Counter32
_PeriodOfOutages_Object = MibTableColumn
periodOfOutages = _PeriodOfOutages_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 6),
    _PeriodOfOutages_Type()
)
periodOfOutages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    periodOfOutages.setStatus("mandatory")
_NumberOfExcludedOutageCounter_Type = Counter32
_NumberOfExcludedOutageCounter_Object = MibTableColumn
numberOfExcludedOutageCounter = _NumberOfExcludedOutageCounter_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 7),
    _NumberOfExcludedOutageCounter_Type()
)
numberOfExcludedOutageCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfExcludedOutageCounter.setStatus("mandatory")
_PeriodOfExcludedOutages_Type = Counter32
_PeriodOfExcludedOutages_Object = MibTableColumn
periodOfExcludedOutages = _PeriodOfExcludedOutages_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 1, 1, 8),
    _PeriodOfExcludedOutages_Type()
)
periodOfExcludedOutages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    periodOfExcludedOutages.setStatus("mandatory")
_OutageTableLastTimestamp_Type = Counter32
_OutageTableLastTimestamp_Object = MibScalar
outageTableLastTimestamp = _OutageTableLastTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 300, 260, 2, 3, 2),
    _OutageTableLastTimestamp_Type()
)
outageTableLastTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outageTableLastTimestamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects

fDRThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 260, 0, 1)
)
fDRThresholdTrap.setObjects(
    ("DL-SLA-MIB", "deliveryRatioPerDLCITableIndex")
)
if mibBuilder.loadTexts:
    fDRThresholdTrap.setStatus(
        ""
    )

dDRThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 260, 0, 2)
)
dDRThresholdTrap.setObjects(
    ("DL-SLA-MIB", "deliveryRatioPerDLCITableIndex")
)
if mibBuilder.loadTexts:
    dDRThresholdTrap.setStatus(
        ""
    )

delayThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 300, 260, 0, 3)
)
delayThresholdTrap.setObjects(
    ("DL-SLA-MIB", "delayPerDLCITableIndex")
)
if mibBuilder.loadTexts:
    delayThresholdTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DL-SLA-MIB",
    **{"digital-link": digital_link,
       "dl-ServiceLevelAgreement": dl_ServiceLevelAgreement,
       "fDRThresholdTrap": fDRThresholdTrap,
       "dDRThresholdTrap": dDRThresholdTrap,
       "delayThresholdTrap": delayThresholdTrap,
       "dlcSLAConfigurationGroup": dlcSLAConfigurationGroup,
       "unitSLAConfiguration": unitSLAConfiguration,
       "configSLA": configSLA,
       "unitSamplingPeriodForFDR-DDR": unitSamplingPeriodForFDR_DDR,
       "unitSamplingPeriodForDelayMeasurement": unitSamplingPeriodForDelayMeasurement,
       "unitThresholdForFDR": unitThresholdForFDR,
       "unitThresholdForDDR": unitThresholdForDDR,
       "unitDelayMeasurementPacketSize": unitDelayMeasurementPacketSize,
       "unitOamDomainIdentifier": unitOamDomainIdentifier,
       "unitOamLocationIdentifier": unitOamLocationIdentifier,
       "perDLCIConfiguration": perDLCIConfiguration,
       "configurationPerDLCITable": configurationPerDLCITable,
       "configurationPerDLCIEntry": configurationPerDLCIEntry,
       "configurationPerDLCITableIndex": configurationPerDLCITableIndex,
       "commitedInformationRatePerDLCI": commitedInformationRatePerDLCI,
       "remoteDLCIPerDLCI": remoteDLCIPerDLCI,
       "remoteIpAddressPerDLCI": remoteIpAddressPerDLCI,
       "thresholdForDelayMeasurementsPerDLCI": thresholdForDelayMeasurementsPerDLCI,
       "dlcSLAStatisticsGroup": dlcSLAStatisticsGroup,
       "dlcDeliveryRatioStatistics": dlcDeliveryRatioStatistics,
       "deliveryRatioPerDLCITable": deliveryRatioPerDLCITable,
       "deliveryRatioPerDLCIEntry": deliveryRatioPerDLCIEntry,
       "deliveryRatioPerDLCITableIndex": deliveryRatioPerDLCITableIndex,
       "deliveryTableEncodedValue": deliveryTableEncodedValue,
       "deliveryTableTimestamp": deliveryTableTimestamp,
       "fTCLperDLCI": fTCLperDLCI,
       "fTELperDLCI": fTELperDLCI,
       "fRCLperDLCI": fRCLperDLCI,
       "fRELperDLCI": fRELperDLCI,
       "fTCRperDLCI": fTCRperDLCI,
       "fTERperDLCI": fTERperDLCI,
       "fRCRperDLCI": fRCRperDLCI,
       "fRERperDLCI": fRERperDLCI,
       "fDRNumberOfSamplesTaken": fDRNumberOfSamplesTaken,
       "fDRNumberOfThresholdViolations": fDRNumberOfThresholdViolations,
       "dTCLperDLCI": dTCLperDLCI,
       "dTELperDLCI": dTELperDLCI,
       "dRCLperDLCI": dRCLperDLCI,
       "dRELperDLCI": dRELperDLCI,
       "dTCRperDLCI": dTCRperDLCI,
       "dTERperDLCI": dTERperDLCI,
       "dRCRperDLCI": dRCRperDLCI,
       "dRERperDLCI": dRERperDLCI,
       "dDRNumberOfSamplesTaken": dDRNumberOfSamplesTaken,
       "dDRNumberOfThresholdViolations": dDRNumberOfThresholdViolations,
       "txFDRTimestamp": txFDRTimestamp,
       "txFDRNumberOfSamplesTaken": txFDRNumberOfSamplesTaken,
       "txFDRNumberOfThresholdViolations": txFDRNumberOfThresholdViolations,
       "rxFDRTimestamp": rxFDRTimestamp,
       "rxFDRNumberOfSamplesTaken": rxFDRNumberOfSamplesTaken,
       "rxFDRNumberOfThresholdViolations": rxFDRNumberOfThresholdViolations,
       "txDDRTimestamp": txDDRTimestamp,
       "txDDRNumberOfSamplesTaken": txDDRNumberOfSamplesTaken,
       "txDDRNumberOfThresholdViolations": txDDRNumberOfThresholdViolations,
       "rxDDRTimestamp": rxDDRTimestamp,
       "rxDDRNumberOfSamplesTaken": rxDDRNumberOfSamplesTaken,
       "rxDDRNumberOfThresholdViolations": rxDDRNumberOfThresholdViolations,
       "txDiscardEligible": txDiscardEligible,
       "rxDiscardEligible": rxDiscardEligible,
       "txFECN": txFECN,
       "rxFECN": rxFECN,
       "txBECN": txBECN,
       "rxBECN": rxBECN,
       "dlcDelayStatistics": dlcDelayStatistics,
       "delayPerDLCITable": delayPerDLCITable,
       "delayPerDLCIEntry": delayPerDLCIEntry,
       "delayPerDLCITableIndex": delayPerDLCITableIndex,
       "delayTableEncodedValue": delayTableEncodedValue,
       "delayTableTimestamp": delayTableTimestamp,
       "totalRoundTripDelayPerDLCI": totalRoundTripDelayPerDLCI,
       "maximumRoundTripDelayNSamplesPerDLCI": maximumRoundTripDelayNSamplesPerDLCI,
       "maximumRoundTripDelay2NSamplesPerDLCI": maximumRoundTripDelay2NSamplesPerDLCI,
       "maximumRoundTripDelay4NSamplesPerDLCI": maximumRoundTripDelay4NSamplesPerDLCI,
       "numberOfDelayMeasurementsPerDLCI": numberOfDelayMeasurementsPerDLCI,
       "delayNumberOfThresholdViolations": delayNumberOfThresholdViolations,
       "dlcOutageStatistics": dlcOutageStatistics,
       "outagePerDLCITable": outagePerDLCITable,
       "outagePerDLCIEntry": outagePerDLCIEntry,
       "outageTableIndex": outageTableIndex,
       "outageTableEncodedValue": outageTableEncodedValue,
       "outageTableTimestamp": outageTableTimestamp,
       "outageStatus": outageStatus,
       "numberOfOutageCounter": numberOfOutageCounter,
       "periodOfOutages": periodOfOutages,
       "numberOfExcludedOutageCounter": numberOfExcludedOutageCounter,
       "periodOfExcludedOutages": periodOfExcludedOutages,
       "outageTableLastTimestamp": outageTableLastTimestamp}
)
