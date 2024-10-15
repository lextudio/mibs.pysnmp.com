# SNMP MIB module (ZHONE-SFF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-SFF
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:45 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneModules,
 zhoneSFF) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneModules",
    "zhoneSFF")

(ZhoneAdminString,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString")


# MODULE-IDENTITY

zhoneSFFModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 114)
)
zhoneSFFModule.setRevisions(
        ("2014-04-07 12:13",
         "2009-04-27 16:52",
         "2008-05-21 12:47",
         "2008-02-13 10:49",
         "2007-11-07 19:07")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneSFFObjects_ObjectIdentity = ObjectIdentity
zhoneSFFObjects = _ZhoneSFFObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1)
)
if mibBuilder.loadTexts:
    zhoneSFFObjects.setStatus("current")
_ZhoneSFPTable_Object = MibTable
zhoneSFPTable = _ZhoneSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneSFPTable.setStatus("current")
_ZhoneSFPEntry_Object = MibTableRow
zhoneSFPEntry = _ZhoneSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1)
)
zhoneSFPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneSFPEntry.setStatus("current")
_ZhoneSFPVendorName_Type = ZhoneAdminString
_ZhoneSFPVendorName_Object = MibTableColumn
zhoneSFPVendorName = _ZhoneSFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 1),
    _ZhoneSFPVendorName_Type()
)
zhoneSFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPVendorName.setStatus("current")
_ZhoneSFPVendorOUI_Type = ZhoneAdminString
_ZhoneSFPVendorOUI_Object = MibTableColumn
zhoneSFPVendorOUI = _ZhoneSFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 2),
    _ZhoneSFPVendorOUI_Type()
)
zhoneSFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPVendorOUI.setStatus("current")
_ZhoneSFPVendorPartNumber_Type = ZhoneAdminString
_ZhoneSFPVendorPartNumber_Object = MibTableColumn
zhoneSFPVendorPartNumber = _ZhoneSFPVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 3),
    _ZhoneSFPVendorPartNumber_Type()
)
zhoneSFPVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPVendorPartNumber.setStatus("current")
_ZhoneSFPVendorRevisionLevel_Type = ZhoneAdminString
_ZhoneSFPVendorRevisionLevel_Object = MibTableColumn
zhoneSFPVendorRevisionLevel = _ZhoneSFPVendorRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 4),
    _ZhoneSFPVendorRevisionLevel_Type()
)
zhoneSFPVendorRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPVendorRevisionLevel.setStatus("current")
_ZhoneSFPSerialNumber_Type = ZhoneAdminString
_ZhoneSFPSerialNumber_Object = MibTableColumn
zhoneSFPSerialNumber = _ZhoneSFPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 5),
    _ZhoneSFPSerialNumber_Type()
)
zhoneSFPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPSerialNumber.setStatus("current")
_ZhoneSFPManufacturingDateCode_Type = ZhoneAdminString
_ZhoneSFPManufacturingDateCode_Object = MibTableColumn
zhoneSFPManufacturingDateCode = _ZhoneSFPManufacturingDateCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 6),
    _ZhoneSFPManufacturingDateCode_Type()
)
zhoneSFPManufacturingDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPManufacturingDateCode.setStatus("current")


class _ZhoneSFPGigeComplianceCode_Type(Bits):
    """Custom type zhoneSFPGigeComplianceCode based on Bits"""
    namedValues = NamedValues(
        *(("base-100-BX", 6),
          ("base-100-FX", 5),
          ("base-100-LX", 4),
          ("base-1000-CX", 2),
          ("base-1000-LX", 1),
          ("base-1000-SX", 0),
          ("base-1000-T", 3),
          ("base-PX", 7))
    )

_ZhoneSFPGigeComplianceCode_Type.__name__ = "Bits"
_ZhoneSFPGigeComplianceCode_Object = MibTableColumn
zhoneSFPGigeComplianceCode = _ZhoneSFPGigeComplianceCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 7),
    _ZhoneSFPGigeComplianceCode_Type()
)
zhoneSFPGigeComplianceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPGigeComplianceCode.setStatus("current")


class _ZhoneSFPConnectorType_Type(Integer32):
    """Custom type zhoneSFPConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("bnc-tnc", 4),
          ("copperPigtail", 33),
          ("fiberJack", 6),
          ("fibreCoaxialHeaders", 5),
          ("fibreStyle1Copper", 2),
          ("fibreStyle2Copper", 3),
          ("hssdc-II", 32),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("opticalPigtail", 11),
          ("sc", 1),
          ("sg", 10),
          ("unknownOrUnspecified", 0))
    )


_ZhoneSFPConnectorType_Type.__name__ = "Integer32"
_ZhoneSFPConnectorType_Object = MibTableColumn
zhoneSFPConnectorType = _ZhoneSFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 8),
    _ZhoneSFPConnectorType_Type()
)
zhoneSFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPConnectorType.setStatus("current")


class _ZhoneSFPIdTransceiverType_Type(Integer32):
    """Custom type zhoneSFPIdTransceiverType based on Integer32"""
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
        *(("connector", 2),
          ("gbic", 1),
          ("sfp", 3),
          ("unknownOrUnspecified", 0))
    )


_ZhoneSFPIdTransceiverType_Type.__name__ = "Integer32"
_ZhoneSFPIdTransceiverType_Object = MibTableColumn
zhoneSFPIdTransceiverType = _ZhoneSFPIdTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 9),
    _ZhoneSFPIdTransceiverType_Type()
)
zhoneSFPIdTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPIdTransceiverType.setStatus("current")
_ZhoneSFPExtendedIdentifier_Type = Unsigned32
_ZhoneSFPExtendedIdentifier_Object = MibTableColumn
zhoneSFPExtendedIdentifier = _ZhoneSFPExtendedIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 10),
    _ZhoneSFPExtendedIdentifier_Type()
)
zhoneSFPExtendedIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPExtendedIdentifier.setStatus("current")


class _ZhoneSFPSerialEncodingAlgorithm_Type(Integer32):
    """Custom type zhoneSFPSerialEncodingAlgorithm based on Integer32"""
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
        *(("eightB10B", 1),
          ("fourB5B", 2),
          ("manchester", 4),
          ("nrz", 3),
          ("unspecified", 0))
    )


_ZhoneSFPSerialEncodingAlgorithm_Type.__name__ = "Integer32"
_ZhoneSFPSerialEncodingAlgorithm_Object = MibTableColumn
zhoneSFPSerialEncodingAlgorithm = _ZhoneSFPSerialEncodingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 11),
    _ZhoneSFPSerialEncodingAlgorithm_Type()
)
zhoneSFPSerialEncodingAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPSerialEncodingAlgorithm.setStatus("current")


class _ZhoneSFPFiberChannelLinkLength_Type(Bits):
    """Custom type zhoneSFPFiberChannelLinkLength based on Bits"""
    namedValues = NamedValues(
        *(("intermediateDistance", 5),
          ("longDistance", 4),
          ("shortDistance", 6),
          ("unused0", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("unused3", 3),
          ("veryLongDistance", 7))
    )

_ZhoneSFPFiberChannelLinkLength_Type.__name__ = "Bits"
_ZhoneSFPFiberChannelLinkLength_Object = MibTableColumn
zhoneSFPFiberChannelLinkLength = _ZhoneSFPFiberChannelLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 12),
    _ZhoneSFPFiberChannelLinkLength_Type()
)
zhoneSFPFiberChannelLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPFiberChannelLinkLength.setStatus("current")


class _ZhoneSFPFiberChannelTransmitterTechnology_Type(Bits):
    """Custom type zhoneSFPFiberChannelTransmitterTechnology based on Bits"""
    namedValues = NamedValues(
        *(("electrical-Inter-Enclosure", 8),
          ("electrical-Intra-Enclosure", 7),
          ("longwabeLaserLC", 9),
          ("longwaveLaserLL", 4),
          ("shortwaveLaserWithOFC", 5),
          ("shortwaveLaserWithoutOFC", 6),
          ("unused0", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("unused3", 3))
    )

_ZhoneSFPFiberChannelTransmitterTechnology_Type.__name__ = "Bits"
_ZhoneSFPFiberChannelTransmitterTechnology_Object = MibTableColumn
zhoneSFPFiberChannelTransmitterTechnology = _ZhoneSFPFiberChannelTransmitterTechnology_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 13),
    _ZhoneSFPFiberChannelTransmitterTechnology_Type()
)
zhoneSFPFiberChannelTransmitterTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPFiberChannelTransmitterTechnology.setStatus("current")


class _ZhoneSFPFiberChannelTransmissionMedia_Type(Bits):
    """Custom type zhoneSFPFiberChannelTransmissionMedia based on Bits"""
    namedValues = NamedValues(
        *(("miniatureCoax", 5),
          ("multiMode-50m", 2),
          ("multiMode-62dot5m", 3),
          ("shieldedTwistedPair", 6),
          ("singleMode", 0),
          ("twinAxialPair", 7),
          ("unused1", 1),
          ("videoCoax", 4))
    )

_ZhoneSFPFiberChannelTransmissionMedia_Type.__name__ = "Bits"
_ZhoneSFPFiberChannelTransmissionMedia_Object = MibTableColumn
zhoneSFPFiberChannelTransmissionMedia = _ZhoneSFPFiberChannelTransmissionMedia_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 14),
    _ZhoneSFPFiberChannelTransmissionMedia_Type()
)
zhoneSFPFiberChannelTransmissionMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPFiberChannelTransmissionMedia.setStatus("current")


class _ZhoneSFPFiberChannelSpeed_Type(Bits):
    """Custom type zhoneSFPFiberChannelSpeed based on Bits"""
    namedValues = NamedValues(
        *(("fourHundredMbytesperSec", 3),
          ("oneHundredMbytesperSec", 0),
          ("twoHundredMbytesperSec", 2),
          ("unused1", 1))
    )

_ZhoneSFPFiberChannelSpeed_Type.__name__ = "Bits"
_ZhoneSFPFiberChannelSpeed_Object = MibTableColumn
zhoneSFPFiberChannelSpeed = _ZhoneSFPFiberChannelSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 15),
    _ZhoneSFPFiberChannelSpeed_Type()
)
zhoneSFPFiberChannelSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPFiberChannelSpeed.setStatus("current")
_ZhoneSFP9To125mmFiberLinkLengthKm_Type = Unsigned32
_ZhoneSFP9To125mmFiberLinkLengthKm_Object = MibTableColumn
zhoneSFP9To125mmFiberLinkLengthKm = _ZhoneSFP9To125mmFiberLinkLengthKm_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 16),
    _ZhoneSFP9To125mmFiberLinkLengthKm_Type()
)
zhoneSFP9To125mmFiberLinkLengthKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFP9To125mmFiberLinkLengthKm.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSFP9To125mmFiberLinkLengthKm.setUnits("Km")
_ZhoneSFP9To125mmFiberLinkLength100m_Type = Unsigned32
_ZhoneSFP9To125mmFiberLinkLength100m_Object = MibTableColumn
zhoneSFP9To125mmFiberLinkLength100m = _ZhoneSFP9To125mmFiberLinkLength100m_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 17),
    _ZhoneSFP9To125mmFiberLinkLength100m_Type()
)
zhoneSFP9To125mmFiberLinkLength100m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFP9To125mmFiberLinkLength100m.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSFP9To125mmFiberLinkLength100m.setUnits("100m")
_ZhoneSFP50To125mmFiberLinkLength10m_Type = Unsigned32
_ZhoneSFP50To125mmFiberLinkLength10m_Object = MibTableColumn
zhoneSFP50To125mmFiberLinkLength10m = _ZhoneSFP50To125mmFiberLinkLength10m_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 18),
    _ZhoneSFP50To125mmFiberLinkLength10m_Type()
)
zhoneSFP50To125mmFiberLinkLength10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFP50To125mmFiberLinkLength10m.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSFP50To125mmFiberLinkLength10m.setUnits("10m")
_ZhoneSFP62Dot5To125FiberLinkLength10m_Type = Unsigned32
_ZhoneSFP62Dot5To125FiberLinkLength10m_Object = MibTableColumn
zhoneSFP62Dot5To125FiberLinkLength10m = _ZhoneSFP62Dot5To125FiberLinkLength10m_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 19),
    _ZhoneSFP62Dot5To125FiberLinkLength10m_Type()
)
zhoneSFP62Dot5To125FiberLinkLength10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFP62Dot5To125FiberLinkLength10m.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSFP62Dot5To125FiberLinkLength10m.setUnits("10m")
_ZhoneSFPNominalBitRate_Type = Unsigned32
_ZhoneSFPNominalBitRate_Object = MibTableColumn
zhoneSFPNominalBitRate = _ZhoneSFPNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 20),
    _ZhoneSFPNominalBitRate_Type()
)
zhoneSFPNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPNominalBitRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSFPNominalBitRate.setUnits("100 Mbits/sec")
_ZhoneSFPUpperBitRateMarginPercentage_Type = Unsigned32
_ZhoneSFPUpperBitRateMarginPercentage_Object = MibTableColumn
zhoneSFPUpperBitRateMarginPercentage = _ZhoneSFPUpperBitRateMarginPercentage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 21),
    _ZhoneSFPUpperBitRateMarginPercentage_Type()
)
zhoneSFPUpperBitRateMarginPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPUpperBitRateMarginPercentage.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSFPUpperBitRateMarginPercentage.setUnits("Percentage")
_ZhoneSFPLowerBitRatePercentage_Type = Unsigned32
_ZhoneSFPLowerBitRatePercentage_Object = MibTableColumn
zhoneSFPLowerBitRatePercentage = _ZhoneSFPLowerBitRatePercentage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 22),
    _ZhoneSFPLowerBitRatePercentage_Type()
)
zhoneSFPLowerBitRatePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPLowerBitRatePercentage.setStatus("current")
if mibBuilder.loadTexts:
    zhoneSFPLowerBitRatePercentage.setUnits("Percentage")
_ZhoneSFPCopperLinkLength_Type = Unsigned32
_ZhoneSFPCopperLinkLength_Object = MibTableColumn
zhoneSFPCopperLinkLength = _ZhoneSFPCopperLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 23),
    _ZhoneSFPCopperLinkLength_Type()
)
zhoneSFPCopperLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPCopperLinkLength.setStatus("current")
_ZhoneSFPIsPresent_Type = TruthValue
_ZhoneSFPIsPresent_Object = MibTableColumn
zhoneSFPIsPresent = _ZhoneSFPIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 1, 1, 24),
    _ZhoneSFPIsPresent_Type()
)
zhoneSFPIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneSFPIsPresent.setStatus("current")
_ZhoneXFPTable_Object = MibTable
zhoneXFPTable = _ZhoneXFPTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneXFPTable.setStatus("current")
_ZhoneXFPEntry_Object = MibTableRow
zhoneXFPEntry = _ZhoneXFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1)
)
zhoneXFPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneXFPEntry.setStatus("current")
_ZhoneXFPVendorName_Type = ZhoneAdminString
_ZhoneXFPVendorName_Object = MibTableColumn
zhoneXFPVendorName = _ZhoneXFPVendorName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 1),
    _ZhoneXFPVendorName_Type()
)
zhoneXFPVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPVendorName.setStatus("current")
_ZhoneXFPVendorOUI_Type = ZhoneAdminString
_ZhoneXFPVendorOUI_Object = MibTableColumn
zhoneXFPVendorOUI = _ZhoneXFPVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 2),
    _ZhoneXFPVendorOUI_Type()
)
zhoneXFPVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPVendorOUI.setStatus("current")
_ZhoneXFPManufacturingDateCode_Type = ZhoneAdminString
_ZhoneXFPManufacturingDateCode_Object = MibTableColumn
zhoneXFPManufacturingDateCode = _ZhoneXFPManufacturingDateCode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 3),
    _ZhoneXFPManufacturingDateCode_Type()
)
zhoneXFPManufacturingDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPManufacturingDateCode.setStatus("current")


class _ZhoneXFPComplianceCode10GbEthernet_Type(Bits):
    """Custom type zhoneXFPComplianceCode10GbEthernet based on Bits"""
    namedValues = NamedValues(
        *(("er", 5),
          ("ew", 1),
          ("lr", 6),
          ("lrm", 4),
          ("lw", 2),
          ("sr", 7),
          ("sw", 3),
          ("unused", 0))
    )

_ZhoneXFPComplianceCode10GbEthernet_Type.__name__ = "Bits"
_ZhoneXFPComplianceCode10GbEthernet_Object = MibTableColumn
zhoneXFPComplianceCode10GbEthernet = _ZhoneXFPComplianceCode10GbEthernet_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 4),
    _ZhoneXFPComplianceCode10GbEthernet_Type()
)
zhoneXFPComplianceCode10GbEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPComplianceCode10GbEthernet.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPComplianceCode10GbEthernet.setUnits("10Gb")


class _ZhoneXFPComplianceCode10GbFiber_Type(Bits):
    """Custom type zhoneXFPComplianceCode10GbFiber based on Bits"""
    namedValues = NamedValues(
        *(("extReach1550nm", 5),
          ("intReach100nmFp", 4),
          ("mX-SN-I-1200", 7),
          ("sM-LL-L-1200", 6),
          ("unused0", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("unused3", 3))
    )

_ZhoneXFPComplianceCode10GbFiber_Type.__name__ = "Bits"
_ZhoneXFPComplianceCode10GbFiber_Object = MibTableColumn
zhoneXFPComplianceCode10GbFiber = _ZhoneXFPComplianceCode10GbFiber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 5),
    _ZhoneXFPComplianceCode10GbFiber_Type()
)
zhoneXFPComplianceCode10GbFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPComplianceCode10GbFiber.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPComplianceCode10GbFiber.setUnits("10Gb")


class _ZhoneXFPLowerSpeed_Type(Bits):
    """Custom type zhoneXFPLowerSpeed based on Bits"""
    namedValues = NamedValues(
        *(("base100Lx-1xFcSmf", 6),
          ("base100Sx-1xFcMmf", 7),
          ("oC-48-IR", 2),
          ("oC-48-LR", 1),
          ("oC-48-SR", 3),
          ("sMF-2xFC", 4),
          ("sMFM-2xFC", 5),
          ("unused0", 0))
    )

_ZhoneXFPLowerSpeed_Type.__name__ = "Bits"
_ZhoneXFPLowerSpeed_Object = MibTableColumn
zhoneXFPLowerSpeed = _ZhoneXFPLowerSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 6),
    _ZhoneXFPLowerSpeed_Type()
)
zhoneXFPLowerSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPLowerSpeed.setStatus("current")


class _ZhoneXFPConnectorType_Type(Integer32):
    """Custom type zhoneXFPConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("bnc-tnc", 4),
          ("copperPigtail", 33),
          ("fiberJack", 6),
          ("fibreCoaxialHeaders", 5),
          ("fibreStyle1Copper", 2),
          ("fibreStyle2Copper", 3),
          ("hssdc-ii", 32),
          ("lc", 7),
          ("mt-rj", 8),
          ("mu", 9),
          ("opticalPigtail", 11),
          ("sc", 1),
          ("sg", 10),
          ("unknownOrUnspecified", 0))
    )


_ZhoneXFPConnectorType_Type.__name__ = "Integer32"
_ZhoneXFPConnectorType_Object = MibTableColumn
zhoneXFPConnectorType = _ZhoneXFPConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 7),
    _ZhoneXFPConnectorType_Type()
)
zhoneXFPConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPConnectorType.setStatus("current")


class _ZhoneXFPIdTransceiverType_Type(Integer32):
    """Custom type zhoneXFPIdTransceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("connector", 2),
          ("gbic", 1),
          ("sfp", 3),
          ("unknownOrUnspecified", 0),
          ("x2", 10),
          ("xenpak", 5),
          ("xff", 7),
          ("xfp", 6),
          ("xfpE", 8),
          ("xpak", 9),
          ("xpi300Pin", 4))
    )


_ZhoneXFPIdTransceiverType_Type.__name__ = "Integer32"
_ZhoneXFPIdTransceiverType_Object = MibTableColumn
zhoneXFPIdTransceiverType = _ZhoneXFPIdTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 8),
    _ZhoneXFPIdTransceiverType_Type()
)
zhoneXFPIdTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPIdTransceiverType.setStatus("current")
_ZhoneXFPExtendedIdentifier_Type = Unsigned32
_ZhoneXFPExtendedIdentifier_Object = MibTableColumn
zhoneXFPExtendedIdentifier = _ZhoneXFPExtendedIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 9),
    _ZhoneXFPExtendedIdentifier_Type()
)
zhoneXFPExtendedIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPExtendedIdentifier.setStatus("current")


class _ZhoneXFPEncodingSupport_Type(Bits):
    """Custom type zhoneXFPEncodingSupport based on Bits"""
    namedValues = NamedValues(
        *(("eightB10B", 6),
          ("nrz", 4),
          ("rz", 3),
          ("sixtyFourBper66B", 7),
          ("sonetScrambled", 5),
          ("unused0", 0),
          ("unused1", 1),
          ("unused2", 2))
    )

_ZhoneXFPEncodingSupport_Type.__name__ = "Bits"
_ZhoneXFPEncodingSupport_Object = MibTableColumn
zhoneXFPEncodingSupport = _ZhoneXFPEncodingSupport_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 10),
    _ZhoneXFPEncodingSupport_Type()
)
zhoneXFPEncodingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPEncodingSupport.setStatus("current")
_ZhoneXFPDeviceTechnology_Type = Unsigned32
_ZhoneXFPDeviceTechnology_Object = MibTableColumn
zhoneXFPDeviceTechnology = _ZhoneXFPDeviceTechnology_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 11),
    _ZhoneXFPDeviceTechnology_Type()
)
zhoneXFPDeviceTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPDeviceTechnology.setStatus("current")
_ZhoneXFPSMFiberLinkLength1Km_Type = Unsigned32
_ZhoneXFPSMFiberLinkLength1Km_Object = MibTableColumn
zhoneXFPSMFiberLinkLength1Km = _ZhoneXFPSMFiberLinkLength1Km_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 12),
    _ZhoneXFPSMFiberLinkLength1Km_Type()
)
zhoneXFPSMFiberLinkLength1Km.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPSMFiberLinkLength1Km.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPSMFiberLinkLength1Km.setUnits("Km")
_ZhoneXFPMMExtendedFiberLinkLength_Type = Unsigned32
_ZhoneXFPMMExtendedFiberLinkLength_Object = MibTableColumn
zhoneXFPMMExtendedFiberLinkLength = _ZhoneXFPMMExtendedFiberLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 13),
    _ZhoneXFPMMExtendedFiberLinkLength_Type()
)
zhoneXFPMMExtendedFiberLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPMMExtendedFiberLinkLength.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPMMExtendedFiberLinkLength.setUnits("2m")
_ZhoneXFPMM50umFiberLinkLength1m_Type = Unsigned32
_ZhoneXFPMM50umFiberLinkLength1m_Object = MibTableColumn
zhoneXFPMM50umFiberLinkLength1m = _ZhoneXFPMM50umFiberLinkLength1m_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 14),
    _ZhoneXFPMM50umFiberLinkLength1m_Type()
)
zhoneXFPMM50umFiberLinkLength1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPMM50umFiberLinkLength1m.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPMM50umFiberLinkLength1m.setUnits("1m")
_ZhoneXFPMM62Dot5umFiberLinkLength1m_Type = Unsigned32
_ZhoneXFPMM62Dot5umFiberLinkLength1m_Object = MibTableColumn
zhoneXFPMM62Dot5umFiberLinkLength1m = _ZhoneXFPMM62Dot5umFiberLinkLength1m_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 15),
    _ZhoneXFPMM62Dot5umFiberLinkLength1m_Type()
)
zhoneXFPMM62Dot5umFiberLinkLength1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPMM62Dot5umFiberLinkLength1m.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPMM62Dot5umFiberLinkLength1m.setUnits("1m")
_ZhoneXFPMinimumBitRate_Type = Unsigned32
_ZhoneXFPMinimumBitRate_Object = MibTableColumn
zhoneXFPMinimumBitRate = _ZhoneXFPMinimumBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 16),
    _ZhoneXFPMinimumBitRate_Type()
)
zhoneXFPMinimumBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPMinimumBitRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPMinimumBitRate.setUnits("100Mbits/sec")
_ZhoneXFPMaximumBitRate_Type = Unsigned32
_ZhoneXFPMaximumBitRate_Object = MibTableColumn
zhoneXFPMaximumBitRate = _ZhoneXFPMaximumBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 17),
    _ZhoneXFPMaximumBitRate_Type()
)
zhoneXFPMaximumBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPMaximumBitRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneXFPMaximumBitRate.setUnits("100Mbits/sec")


class _ZhoneXFPEnhancedOptions_Type(Bits):
    """Custom type zhoneXFPEnhancedOptions based on Bits"""
    namedValues = NamedValues(
        *(("activeFEC-Control", 2),
          ("cMU-Support", 0),
          ("soft-P-Down", 5),
          ("soft-Tx-Disable", 6),
          ("vPS-BypassedRegulator", 3),
          ("vPS-LVRegulator", 4),
          ("vps", 7),
          ("wavelengthTurnability", 1))
    )

_ZhoneXFPEnhancedOptions_Type.__name__ = "Bits"
_ZhoneXFPEnhancedOptions_Object = MibTableColumn
zhoneXFPEnhancedOptions = _ZhoneXFPEnhancedOptions_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 18),
    _ZhoneXFPEnhancedOptions_Type()
)
zhoneXFPEnhancedOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPEnhancedOptions.setStatus("current")
_ZhoneXFPVendorPartNumber_Type = ZhoneAdminString
_ZhoneXFPVendorPartNumber_Object = MibTableColumn
zhoneXFPVendorPartNumber = _ZhoneXFPVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 19),
    _ZhoneXFPVendorPartNumber_Type()
)
zhoneXFPVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPVendorPartNumber.setStatus("current")
_ZhoneXFPVendorRevisionLevel_Type = ZhoneAdminString
_ZhoneXFPVendorRevisionLevel_Object = MibTableColumn
zhoneXFPVendorRevisionLevel = _ZhoneXFPVendorRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 20),
    _ZhoneXFPVendorRevisionLevel_Type()
)
zhoneXFPVendorRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPVendorRevisionLevel.setStatus("current")
_ZhoneXFPSerialNumber_Type = ZhoneAdminString
_ZhoneXFPSerialNumber_Object = MibTableColumn
zhoneXFPSerialNumber = _ZhoneXFPSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 21),
    _ZhoneXFPSerialNumber_Type()
)
zhoneXFPSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPSerialNumber.setStatus("current")
_ZhoneXFPIsPresent_Type = TruthValue
_ZhoneXFPIsPresent_Object = MibTableColumn
zhoneXFPIsPresent = _ZhoneXFPIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 2, 1, 22),
    _ZhoneXFPIsPresent_Type()
)
zhoneXFPIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneXFPIsPresent.setStatus("current")
_ZhoneDDMStatusTable_Object = MibTable
zhoneDDMStatusTable = _ZhoneDDMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneDDMStatusTable.setStatus("current")
_ZhoneDDMStatusEntry_Object = MibTableRow
zhoneDDMStatusEntry = _ZhoneDDMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1)
)
zhoneDDMStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zhoneDDMStatusEntry.setStatus("current")


class _ZhoneDDMTemperature_Type(Integer32):
    """Custom type zhoneDDMTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 128),
    )


_ZhoneDDMTemperature_Type.__name__ = "Integer32"
_ZhoneDDMTemperature_Object = MibTableColumn
zhoneDDMTemperature = _ZhoneDDMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1, 1),
    _ZhoneDDMTemperature_Type()
)
zhoneDDMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDDMTemperature.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDDMTemperature.setUnits("Degrees celcius")


class _ZhoneDDMVoltage_Type(Unsigned32):
    """Custom type zhoneDDMVoltage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 655),
    )


_ZhoneDDMVoltage_Type.__name__ = "Unsigned32"
_ZhoneDDMVoltage_Object = MibTableColumn
zhoneDDMVoltage = _ZhoneDDMVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1, 2),
    _ZhoneDDMVoltage_Type()
)
zhoneDDMVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDDMVoltage.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDDMVoltage.setUnits("Hundredths of volts")


class _ZhoneDDMTxBiasCurrent_Type(Integer32):
    """Custom type zhoneDDMTxBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131),
    )


_ZhoneDDMTxBiasCurrent_Type.__name__ = "Integer32"
_ZhoneDDMTxBiasCurrent_Object = MibTableColumn
zhoneDDMTxBiasCurrent = _ZhoneDDMTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1, 3),
    _ZhoneDDMTxBiasCurrent_Type()
)
zhoneDDMTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDDMTxBiasCurrent.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDDMTxBiasCurrent.setUnits("milliamperes")


class _ZhoneDDMTxPower_Type(Integer32):
    """Custom type zhoneDDMTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 200),
    )


_ZhoneDDMTxPower_Type.__name__ = "Integer32"
_ZhoneDDMTxPower_Object = MibTableColumn
zhoneDDMTxPower = _ZhoneDDMTxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1, 4),
    _ZhoneDDMTxPower_Type()
)
zhoneDDMTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDDMTxPower.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDDMTxPower.setUnits("tenths of dB")


class _ZhoneDDMRxPower_Type(Integer32):
    """Custom type zhoneDDMRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, 200),
    )


_ZhoneDDMRxPower_Type.__name__ = "Integer32"
_ZhoneDDMRxPower_Object = MibTableColumn
zhoneDDMRxPower = _ZhoneDDMRxPower_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1, 5),
    _ZhoneDDMRxPower_Type()
)
zhoneDDMRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDDMRxPower.setStatus("current")
if mibBuilder.loadTexts:
    zhoneDDMRxPower.setUnits("tenths of dB")


class _ZhoneDDMStatusWord_Type(Integer32):
    """Custom type zhoneDDMStatusWord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 4),
          ("ddmnotsupported", 16),
          ("ok", 1),
          ("sfpnotpresent", 8),
          ("warning", 2))
    )


_ZhoneDDMStatusWord_Type.__name__ = "Integer32"
_ZhoneDDMStatusWord_Object = MibTableColumn
zhoneDDMStatusWord = _ZhoneDDMStatusWord_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1, 6),
    _ZhoneDDMStatusWord_Type()
)
zhoneDDMStatusWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDDMStatusWord.setStatus("current")


class _ZhoneDDMAlarms_Type(Bits):
    """Custom type zhoneDDMAlarms based on Bits"""
    namedValues = NamedValues(
        *(("rxPwrHigh", 8),
          ("rxPwrLow", 9),
          ("tempHigh", 0),
          ("tempLow", 1),
          ("txBiasHigh", 4),
          ("txBiasLow", 5),
          ("txPwrHigh", 6),
          ("txPwrLow", 7),
          ("vccHigh", 2),
          ("vccLow", 3))
    )

_ZhoneDDMAlarms_Type.__name__ = "Bits"
_ZhoneDDMAlarms_Object = MibTableColumn
zhoneDDMAlarms = _ZhoneDDMAlarms_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 12, 1, 3, 1, 7),
    _ZhoneDDMAlarms_Type()
)
zhoneDDMAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneDDMAlarms.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-SFF",
    **{"zhoneSFFObjects": zhoneSFFObjects,
       "zhoneSFPTable": zhoneSFPTable,
       "zhoneSFPEntry": zhoneSFPEntry,
       "zhoneSFPVendorName": zhoneSFPVendorName,
       "zhoneSFPVendorOUI": zhoneSFPVendorOUI,
       "zhoneSFPVendorPartNumber": zhoneSFPVendorPartNumber,
       "zhoneSFPVendorRevisionLevel": zhoneSFPVendorRevisionLevel,
       "zhoneSFPSerialNumber": zhoneSFPSerialNumber,
       "zhoneSFPManufacturingDateCode": zhoneSFPManufacturingDateCode,
       "zhoneSFPGigeComplianceCode": zhoneSFPGigeComplianceCode,
       "zhoneSFPConnectorType": zhoneSFPConnectorType,
       "zhoneSFPIdTransceiverType": zhoneSFPIdTransceiverType,
       "zhoneSFPExtendedIdentifier": zhoneSFPExtendedIdentifier,
       "zhoneSFPSerialEncodingAlgorithm": zhoneSFPSerialEncodingAlgorithm,
       "zhoneSFPFiberChannelLinkLength": zhoneSFPFiberChannelLinkLength,
       "zhoneSFPFiberChannelTransmitterTechnology": zhoneSFPFiberChannelTransmitterTechnology,
       "zhoneSFPFiberChannelTransmissionMedia": zhoneSFPFiberChannelTransmissionMedia,
       "zhoneSFPFiberChannelSpeed": zhoneSFPFiberChannelSpeed,
       "zhoneSFP9To125mmFiberLinkLengthKm": zhoneSFP9To125mmFiberLinkLengthKm,
       "zhoneSFP9To125mmFiberLinkLength100m": zhoneSFP9To125mmFiberLinkLength100m,
       "zhoneSFP50To125mmFiberLinkLength10m": zhoneSFP50To125mmFiberLinkLength10m,
       "zhoneSFP62Dot5To125FiberLinkLength10m": zhoneSFP62Dot5To125FiberLinkLength10m,
       "zhoneSFPNominalBitRate": zhoneSFPNominalBitRate,
       "zhoneSFPUpperBitRateMarginPercentage": zhoneSFPUpperBitRateMarginPercentage,
       "zhoneSFPLowerBitRatePercentage": zhoneSFPLowerBitRatePercentage,
       "zhoneSFPCopperLinkLength": zhoneSFPCopperLinkLength,
       "zhoneSFPIsPresent": zhoneSFPIsPresent,
       "zhoneXFPTable": zhoneXFPTable,
       "zhoneXFPEntry": zhoneXFPEntry,
       "zhoneXFPVendorName": zhoneXFPVendorName,
       "zhoneXFPVendorOUI": zhoneXFPVendorOUI,
       "zhoneXFPManufacturingDateCode": zhoneXFPManufacturingDateCode,
       "zhoneXFPComplianceCode10GbEthernet": zhoneXFPComplianceCode10GbEthernet,
       "zhoneXFPComplianceCode10GbFiber": zhoneXFPComplianceCode10GbFiber,
       "zhoneXFPLowerSpeed": zhoneXFPLowerSpeed,
       "zhoneXFPConnectorType": zhoneXFPConnectorType,
       "zhoneXFPIdTransceiverType": zhoneXFPIdTransceiverType,
       "zhoneXFPExtendedIdentifier": zhoneXFPExtendedIdentifier,
       "zhoneXFPEncodingSupport": zhoneXFPEncodingSupport,
       "zhoneXFPDeviceTechnology": zhoneXFPDeviceTechnology,
       "zhoneXFPSMFiberLinkLength1Km": zhoneXFPSMFiberLinkLength1Km,
       "zhoneXFPMMExtendedFiberLinkLength": zhoneXFPMMExtendedFiberLinkLength,
       "zhoneXFPMM50umFiberLinkLength1m": zhoneXFPMM50umFiberLinkLength1m,
       "zhoneXFPMM62Dot5umFiberLinkLength1m": zhoneXFPMM62Dot5umFiberLinkLength1m,
       "zhoneXFPMinimumBitRate": zhoneXFPMinimumBitRate,
       "zhoneXFPMaximumBitRate": zhoneXFPMaximumBitRate,
       "zhoneXFPEnhancedOptions": zhoneXFPEnhancedOptions,
       "zhoneXFPVendorPartNumber": zhoneXFPVendorPartNumber,
       "zhoneXFPVendorRevisionLevel": zhoneXFPVendorRevisionLevel,
       "zhoneXFPSerialNumber": zhoneXFPSerialNumber,
       "zhoneXFPIsPresent": zhoneXFPIsPresent,
       "zhoneDDMStatusTable": zhoneDDMStatusTable,
       "zhoneDDMStatusEntry": zhoneDDMStatusEntry,
       "zhoneDDMTemperature": zhoneDDMTemperature,
       "zhoneDDMVoltage": zhoneDDMVoltage,
       "zhoneDDMTxBiasCurrent": zhoneDDMTxBiasCurrent,
       "zhoneDDMTxPower": zhoneDDMTxPower,
       "zhoneDDMRxPower": zhoneDDMRxPower,
       "zhoneDDMStatusWord": zhoneDDMStatusWord,
       "zhoneDDMAlarms": zhoneDDMAlarms,
       "zhoneSFFModule": zhoneSFFModule}
)
