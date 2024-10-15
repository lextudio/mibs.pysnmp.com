# SNMP MIB module (PDN-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-SFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:06 2024
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

(pdn_ietf_drafts,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-ietf-drafts")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pdnSfp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3)
)
pdnSfp.setRevisions(
        ("2003-04-23 00:00",
         "2003-02-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpMIBObjects_ObjectIdentity = ObjectIdentity
sfpMIBObjects = _SfpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1)
)
_SfpCompatibleInterfaceCount_Type = Integer32
_SfpCompatibleInterfaceCount_Object = MibScalar
sfpCompatibleInterfaceCount = _SfpCompatibleInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 1),
    _SfpCompatibleInterfaceCount_Type()
)
sfpCompatibleInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpCompatibleInterfaceCount.setStatus("current")
_SfpInfoTable_Object = MibTable
sfpInfoTable = _SfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sfpInfoTable.setStatus("current")
_SfpInfoEntry_Object = MibTableRow
sfpInfoEntry = _SfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1)
)
sfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sfpInfoEntry.setStatus("current")


class _SfpIdentifier_Type(Integer32):
    """Custom type sfpIdentifier based on Integer32"""
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
        *(("fixed", 3),
          ("gbic", 2),
          ("other", 5),
          ("sfp", 4),
          ("unknown", 1))
    )


_SfpIdentifier_Type.__name__ = "Integer32"
_SfpIdentifier_Object = MibTableColumn
sfpIdentifier = _SfpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 1),
    _SfpIdentifier_Type()
)
sfpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpIdentifier.setStatus("current")


class _SfpVendorSpecificIdentifier_Type(OctetString):
    """Custom type sfpVendorSpecificIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SfpVendorSpecificIdentifier_Type.__name__ = "OctetString"
_SfpVendorSpecificIdentifier_Object = MibTableColumn
sfpVendorSpecificIdentifier = _SfpVendorSpecificIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 2),
    _SfpVendorSpecificIdentifier_Type()
)
sfpVendorSpecificIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSpecificIdentifier.setStatus("current")


class _SfpExtIdentifier_Type(Integer32):
    """Custom type sfpExtIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("simd", 2),
          ("unknown", 1))
    )


_SfpExtIdentifier_Type.__name__ = "Integer32"
_SfpExtIdentifier_Object = MibTableColumn
sfpExtIdentifier = _SfpExtIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 3),
    _SfpExtIdentifier_Type()
)
sfpExtIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpExtIdentifier.setStatus("current")


class _SfpConnector_Type(Integer32):
    """Custom type sfpConnector based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("bnctnc", 5),
          ("copperPigtail", 14),
          ("fcch", 6),
          ("fcscc1", 3),
          ("fcscc2", 4),
          ("fiberJack", 7),
          ("hssdcii", 13),
          ("lc", 8),
          ("mtrj", 9),
          ("mu", 10),
          ("opticalPigtail", 12),
          ("other", 15),
          ("sc", 2),
          ("sg", 11),
          ("unknown", 1))
    )


_SfpConnector_Type.__name__ = "Integer32"
_SfpConnector_Object = MibTableColumn
sfpConnector = _SfpConnector_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 4),
    _SfpConnector_Type()
)
sfpConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpConnector.setStatus("current")


class _SfpVendorSpecificConnector_Type(OctetString):
    """Custom type sfpVendorSpecificConnector based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SfpVendorSpecificConnector_Type.__name__ = "OctetString"
_SfpVendorSpecificConnector_Object = MibTableColumn
sfpVendorSpecificConnector = _SfpVendorSpecificConnector_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 5),
    _SfpVendorSpecificConnector_Type()
)
sfpVendorSpecificConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSpecificConnector.setStatus("current")


class _SfpTransceiverComplianceCodes_Type(Bits):
    """Custom type sfpTransceiverComplianceCodes based on Bits"""
    namedValues = NamedValues(
        *(("base1000CX", 20),
          ("base1000LX", 21),
          ("base1000SX", 22),
          ("base1000T", 19),
          ("copperActive1x", 25),
          ("copperPassive1x", 26),
          ("lx1x", 24),
          ("oc12MMShortReach", 12),
          ("oc12SMIntermediateReach1", 10),
          ("oc12SMIntermediateReach2", 11),
          ("oc12SMLongReach1", 7),
          ("oc12SMLongReach2", 8),
          ("oc12SMLongReach3", 9),
          ("oc3MMShortReach", 18),
          ("oc3SMIntermediateReach1", 16),
          ("oc3SMIntermediateReach2", 17),
          ("oc3SMLongReach1", 13),
          ("oc3SMLongReach2", 14),
          ("oc3SMLongReach3", 15),
          ("oc48IntermediateReach1", 4),
          ("oc48IntermediateReach2", 5),
          ("oc48LongReach1", 1),
          ("oc48LongReach2", 2),
          ("oc48LongReach3", 3),
          ("oc48ShortReach", 6),
          ("sx1x", 23),
          ("unknown", 0))
    )

_SfpTransceiverComplianceCodes_Type.__name__ = "Bits"
_SfpTransceiverComplianceCodes_Object = MibTableColumn
sfpTransceiverComplianceCodes = _SfpTransceiverComplianceCodes_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 6),
    _SfpTransceiverComplianceCodes_Type()
)
sfpTransceiverComplianceCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTransceiverComplianceCodes.setStatus("current")


class _SfpFibreChannelLinkLength_Type(Bits):
    """Custom type sfpFibreChannelLinkLength based on Bits"""
    namedValues = NamedValues(
        *(("intermediate", 3),
          ("long", 4),
          ("short", 2),
          ("unknown", 0),
          ("veryLong", 1))
    )

_SfpFibreChannelLinkLength_Type.__name__ = "Bits"
_SfpFibreChannelLinkLength_Object = MibTableColumn
sfpFibreChannelLinkLength = _SfpFibreChannelLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 7),
    _SfpFibreChannelLinkLength_Type()
)
sfpFibreChannelLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpFibreChannelLinkLength.setStatus("current")


class _SfpFibreChannelTransmitterTechnology_Type(Bits):
    """Custom type sfpFibreChannelTransmitterTechnology based on Bits"""
    namedValues = NamedValues(
        *(("el1", 2),
          ("el2", 3),
          ("lc", 1),
          ("ll", 6),
          ("sl", 5),
          ("sn", 4),
          ("unknown", 0))
    )

_SfpFibreChannelTransmitterTechnology_Type.__name__ = "Bits"
_SfpFibreChannelTransmitterTechnology_Object = MibTableColumn
sfpFibreChannelTransmitterTechnology = _SfpFibreChannelTransmitterTechnology_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 8),
    _SfpFibreChannelTransmitterTechnology_Type()
)
sfpFibreChannelTransmitterTechnology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpFibreChannelTransmitterTechnology.setStatus("current")


class _SfpFibreChannelTransmissionMedia_Type(Bits):
    """Custom type sfpFibreChannelTransmissionMedia based on Bits"""
    namedValues = NamedValues(
        *(("m5", 6),
          ("m6", 5),
          ("mi", 3),
          ("sm", 7),
          ("tp", 2),
          ("tv", 4),
          ("tw", 1),
          ("unknown", 0))
    )

_SfpFibreChannelTransmissionMedia_Type.__name__ = "Bits"
_SfpFibreChannelTransmissionMedia_Object = MibTableColumn
sfpFibreChannelTransmissionMedia = _SfpFibreChannelTransmissionMedia_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 9),
    _SfpFibreChannelTransmissionMedia_Type()
)
sfpFibreChannelTransmissionMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpFibreChannelTransmissionMedia.setStatus("current")


class _SfpFibreChannelTransmissionSpeed_Type(Bits):
    """Custom type sfpFibreChannelTransmissionSpeed based on Bits"""
    namedValues = NamedValues(
        *(("mbps100", 3),
          ("mbps200", 2),
          ("mbps400", 1),
          ("unknown", 0))
    )

_SfpFibreChannelTransmissionSpeed_Type.__name__ = "Bits"
_SfpFibreChannelTransmissionSpeed_Object = MibTableColumn
sfpFibreChannelTransmissionSpeed = _SfpFibreChannelTransmissionSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 10),
    _SfpFibreChannelTransmissionSpeed_Type()
)
sfpFibreChannelTransmissionSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpFibreChannelTransmissionSpeed.setStatus("current")


class _SfpEncoding_Type(Integer32):
    """Custom type sfpEncoding based on Integer32"""
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
        *(("b4b5", 3),
          ("b8b10", 2),
          ("manchester", 5),
          ("nrz", 4),
          ("sonetScrambled", 6),
          ("unknown", 1))
    )


_SfpEncoding_Type.__name__ = "Integer32"
_SfpEncoding_Object = MibTableColumn
sfpEncoding = _SfpEncoding_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 11),
    _SfpEncoding_Type()
)
sfpEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpEncoding.setStatus("current")
_SfpBRNominal100Mbps_Type = Integer32
_SfpBRNominal100Mbps_Object = MibTableColumn
sfpBRNominal100Mbps = _SfpBRNominal100Mbps_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 12),
    _SfpBRNominal100Mbps_Type()
)
sfpBRNominal100Mbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpBRNominal100Mbps.setStatus("current")
if mibBuilder.loadTexts:
    sfpBRNominal100Mbps.setUnits("100 Megabits per second (Mbps)")
_SfpLength9MiKm_Type = Integer32
_SfpLength9MiKm_Object = MibTableColumn
sfpLength9MiKm = _SfpLength9MiKm_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 13),
    _SfpLength9MiKm_Type()
)
sfpLength9MiKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLength9MiKm.setStatus("current")
if mibBuilder.loadTexts:
    sfpLength9MiKm.setUnits("Kilometer(Km)")
_SfpLength9Mi100M_Type = Integer32
_SfpLength9Mi100M_Object = MibTableColumn
sfpLength9Mi100M = _SfpLength9Mi100M_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 14),
    _SfpLength9Mi100M_Type()
)
sfpLength9Mi100M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLength9Mi100M.setStatus("current")
if mibBuilder.loadTexts:
    sfpLength9Mi100M.setUnits("100 Meters(M)")
_SfpLength50Mi10M_Type = Integer32
_SfpLength50Mi10M_Object = MibTableColumn
sfpLength50Mi10M = _SfpLength50Mi10M_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 15),
    _SfpLength50Mi10M_Type()
)
sfpLength50Mi10M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLength50Mi10M.setStatus("current")
if mibBuilder.loadTexts:
    sfpLength50Mi10M.setUnits("10 Meters(M)")
_SfpLength62Pt5Mi10M_Type = Integer32
_SfpLength62Pt5Mi10M_Object = MibTableColumn
sfpLength62Pt5Mi10M = _SfpLength62Pt5Mi10M_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 16),
    _SfpLength62Pt5Mi10M_Type()
)
sfpLength62Pt5Mi10M.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLength62Pt5Mi10M.setStatus("current")
if mibBuilder.loadTexts:
    sfpLength62Pt5Mi10M.setUnits("10 Meters(M)")
_SfpLengthCopperM_Type = Integer32
_SfpLengthCopperM_Object = MibTableColumn
sfpLengthCopperM = _SfpLengthCopperM_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 17),
    _SfpLengthCopperM_Type()
)
sfpLengthCopperM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLengthCopperM.setStatus("current")
if mibBuilder.loadTexts:
    sfpLengthCopperM.setUnits("1 Meter(M)")


class _SfpVendorName_Type(DisplayString):
    """Custom type sfpVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorName_Type.__name__ = "DisplayString"
_SfpVendorName_Object = MibTableColumn
sfpVendorName = _SfpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 18),
    _SfpVendorName_Type()
)
sfpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorName.setStatus("current")


class _SfpVendorOUI_Type(OctetString):
    """Custom type sfpVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SfpVendorOUI_Type.__name__ = "OctetString"
_SfpVendorOUI_Object = MibTableColumn
sfpVendorOUI = _SfpVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 19),
    _SfpVendorOUI_Type()
)
sfpVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorOUI.setStatus("current")


class _SfpVendorPN_Type(DisplayString):
    """Custom type sfpVendorPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorPN_Type.__name__ = "DisplayString"
_SfpVendorPN_Object = MibTableColumn
sfpVendorPN = _SfpVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 20),
    _SfpVendorPN_Type()
)
sfpVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorPN.setStatus("current")


class _SfpVendorSN_Type(DisplayString):
    """Custom type sfpVendorSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SfpVendorSN_Type.__name__ = "DisplayString"
_SfpVendorSN_Object = MibTableColumn
sfpVendorSN = _SfpVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 21),
    _SfpVendorSN_Type()
)
sfpVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSN.setStatus("current")


class _SfpVendorRev_Type(DisplayString):
    """Custom type sfpVendorRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_SfpVendorRev_Type.__name__ = "DisplayString"
_SfpVendorRev_Object = MibTableColumn
sfpVendorRev = _SfpVendorRev_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 22),
    _SfpVendorRev_Type()
)
sfpVendorRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorRev.setStatus("current")
_SfpLaserWavelength_Type = Integer32
_SfpLaserWavelength_Object = MibTableColumn
sfpLaserWavelength = _SfpLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 23),
    _SfpLaserWavelength_Type()
)
sfpLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpLaserWavelength.setStatus("current")
if mibBuilder.loadTexts:
    sfpLaserWavelength.setUnits("Nano Meter(NM)")


class _SfpOptions_Type(Bits):
    """Custom type sfpOptions based on Bits"""
    namedValues = NamedValues(
        *(("losInverted", 4),
          ("losNormal", 5),
          ("rateSelect", 1),
          ("txDisable", 2),
          ("txFault", 3),
          ("unknown", 0))
    )

_SfpOptions_Type.__name__ = "Bits"
_SfpOptions_Object = MibTableColumn
sfpOptions = _SfpOptions_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 24),
    _SfpOptions_Type()
)
sfpOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpOptions.setStatus("current")
_SfpBRMin_Type = Integer32
_SfpBRMin_Object = MibTableColumn
sfpBRMin = _SfpBRMin_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 25),
    _SfpBRMin_Type()
)
sfpBRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpBRMin.setStatus("current")
if mibBuilder.loadTexts:
    sfpBRMin.setUnits("percent below sfpBRNominal")
_SfpBRMax_Type = Integer32
_SfpBRMax_Object = MibTableColumn
sfpBRMax = _SfpBRMax_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 26),
    _SfpBRMax_Type()
)
sfpBRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpBRMax.setStatus("current")
if mibBuilder.loadTexts:
    sfpBRMax.setUnits("percent above sfpBRNominal")
_SfpVendorDate_Type = DateAndTime
_SfpVendorDate_Object = MibTableColumn
sfpVendorDate = _SfpVendorDate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 27),
    _SfpVendorDate_Type()
)
sfpVendorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorDate.setStatus("current")


class _SfpVendorSpecificLotCode_Type(OctetString):
    """Custom type sfpVendorSpecificLotCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SfpVendorSpecificLotCode_Type.__name__ = "OctetString"
_SfpVendorSpecificLotCode_Object = MibTableColumn
sfpVendorSpecificLotCode = _SfpVendorSpecificLotCode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 28),
    _SfpVendorSpecificLotCode_Type()
)
sfpVendorSpecificLotCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSpecificLotCode.setStatus("current")


class _SfpVendorSpecificData_Type(OctetString):
    """Custom type sfpVendorSpecificData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SfpVendorSpecificData_Type.__name__ = "OctetString"
_SfpVendorSpecificData_Object = MibTableColumn
sfpVendorSpecificData = _SfpVendorSpecificData_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 29),
    _SfpVendorSpecificData_Type()
)
sfpVendorSpecificData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVendorSpecificData.setStatus("current")


class _SfpStatusCurrent_Type(Bits):
    """Custom type sfpStatusCurrent based on Bits"""
    namedValues = NamedValues(
        *(("disabled", 6),
          ("enabled", 5),
          ("faulty", 3),
          ("inValidCCBase", 7),
          ("inValidCCExt", 8),
          ("installed", 2),
          ("notInstalled", 1),
          ("operational", 4),
          ("unknown", 0))
    )

_SfpStatusCurrent_Type.__name__ = "Bits"
_SfpStatusCurrent_Object = MibTableColumn
sfpStatusCurrent = _SfpStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 2, 1, 30),
    _SfpStatusCurrent_Type()
)
sfpStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpStatusCurrent.setStatus("current")
_SfpCommandTable_Object = MibTable
sfpCommandTable = _SfpCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 3)
)
if mibBuilder.loadTexts:
    sfpCommandTable.setStatus("current")
_SfpCommandEntry_Object = MibTableRow
sfpCommandEntry = _SfpCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 3, 1)
)
sfpCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sfpCommandEntry.setStatus("current")


class _SfpCommand_Type(Integer32):
    """Custom type sfpCommand based on Integer32"""
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
        *(("disable", 3),
          ("enable", 2),
          ("noCmd", 1),
          ("reset", 4))
    )


_SfpCommand_Type.__name__ = "Integer32"
_SfpCommand_Object = MibTableColumn
sfpCommand = _SfpCommand_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 3, 1, 1),
    _SfpCommand_Type()
)
sfpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpCommand.setStatus("current")


class _SfpNotificationEnable_Type(Bits):
    """Custom type sfpNotificationEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("faulty", 0),
          ("inserted", 2),
          ("operational", 1),
          ("removed", 3))
    )

_SfpNotificationEnable_Type.__name__ = "Bits"
_SfpNotificationEnable_Object = MibScalar
sfpNotificationEnable = _SfpNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 1, 4),
    _SfpNotificationEnable_Type()
)
sfpNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpNotificationEnable.setStatus("current")
_SfpMIBNotifications_ObjectIdentity = ObjectIdentity
sfpMIBNotifications = _SfpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2)
)
_SfpNotificationsPrefix_ObjectIdentity = ObjectIdentity
sfpNotificationsPrefix = _SfpNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0)
)
_SfpMIBConformance_ObjectIdentity = ObjectIdentity
sfpMIBConformance = _SfpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3)
)
_SfpGroups_ObjectIdentity = ObjectIdentity
sfpGroups = _SfpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1)
)
_SfpCompliances_ObjectIdentity = ObjectIdentity
sfpCompliances = _SfpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2)
)

# Managed Objects groups

sfpMIBObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 1)
)
sfpMIBObjectsGroup.setObjects(
    ("PDN-SFP-MIB", "sfpCompatibleInterfaceCount")
)
if mibBuilder.loadTexts:
    sfpMIBObjectsGroup.setStatus("current")

sfpInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 2)
)
sfpInformationGroup.setObjects(
      *(("PDN-SFP-MIB", "sfpIdentifier"),
        ("PDN-SFP-MIB", "sfpVendorSpecificIdentifier"),
        ("PDN-SFP-MIB", "sfpExtIdentifier"),
        ("PDN-SFP-MIB", "sfpConnector"),
        ("PDN-SFP-MIB", "sfpVendorSpecificConnector"),
        ("PDN-SFP-MIB", "sfpTransceiverComplianceCodes"),
        ("PDN-SFP-MIB", "sfpFibreChannelLinkLength"),
        ("PDN-SFP-MIB", "sfpFibreChannelTransmitterTechnology"),
        ("PDN-SFP-MIB", "sfpFibreChannelTransmissionMedia"),
        ("PDN-SFP-MIB", "sfpFibreChannelTransmissionSpeed"),
        ("PDN-SFP-MIB", "sfpEncoding"),
        ("PDN-SFP-MIB", "sfpBRNominal100Mbps"),
        ("PDN-SFP-MIB", "sfpLength9MiKm"),
        ("PDN-SFP-MIB", "sfpLength9Mi100M"),
        ("PDN-SFP-MIB", "sfpLength50Mi10M"),
        ("PDN-SFP-MIB", "sfpLength62Pt5Mi10M"),
        ("PDN-SFP-MIB", "sfpLengthCopperM"),
        ("PDN-SFP-MIB", "sfpVendorName"),
        ("PDN-SFP-MIB", "sfpVendorOUI"),
        ("PDN-SFP-MIB", "sfpVendorPN"),
        ("PDN-SFP-MIB", "sfpVendorSN"),
        ("PDN-SFP-MIB", "sfpVendorRev"),
        ("PDN-SFP-MIB", "sfpLaserWavelength"),
        ("PDN-SFP-MIB", "sfpOptions"),
        ("PDN-SFP-MIB", "sfpBRMin"),
        ("PDN-SFP-MIB", "sfpBRMax"),
        ("PDN-SFP-MIB", "sfpVendorDate"),
        ("PDN-SFP-MIB", "sfpVendorSpecificLotCode"),
        ("PDN-SFP-MIB", "sfpVendorSpecificData"),
        ("PDN-SFP-MIB", "sfpStatusCurrent"))
)
if mibBuilder.loadTexts:
    sfpInformationGroup.setStatus("current")

sfpCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 3)
)
sfpCommandGroup.setObjects(
    ("PDN-SFP-MIB", "sfpCommand")
)
if mibBuilder.loadTexts:
    sfpCommandGroup.setStatus("current")

sfpNotificationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 4)
)
sfpNotificationsGroup.setObjects(
    ("PDN-SFP-MIB", "sfpNotificationEnable")
)
if mibBuilder.loadTexts:
    sfpNotificationsGroup.setStatus("current")


# Notification objects

sfpEventFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 1)
)
sfpEventFaulty.setObjects(
    ("PDN-SFP-MIB", "sfpStatusCurrent")
)
if mibBuilder.loadTexts:
    sfpEventFaulty.setStatus(
        "current"
    )

sfpEventOperational = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 2)
)
sfpEventOperational.setObjects(
    ("PDN-SFP-MIB", "sfpStatusCurrent")
)
if mibBuilder.loadTexts:
    sfpEventOperational.setStatus(
        "current"
    )

sfpEventInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 3)
)
sfpEventInserted.setObjects(
    ("PDN-SFP-MIB", "sfpStatusCurrent")
)
if mibBuilder.loadTexts:
    sfpEventInserted.setStatus(
        "current"
    )

sfpEventRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 2, 0, 4)
)
sfpEventRemoved.setObjects(
    ("PDN-SFP-MIB", "sfpStatusCurrent")
)
if mibBuilder.loadTexts:
    sfpEventRemoved.setStatus(
        "current"
    )


# Notifications groups

sfpEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 1, 5)
)
sfpEventGroup.setObjects(
      *(("PDN-SFP-MIB", "sfpEventFaulty"),
        ("PDN-SFP-MIB", "sfpEventOperational"),
        ("PDN-SFP-MIB", "sfpEventInserted"),
        ("PDN-SFP-MIB", "sfpEventRemoved"))
)
if mibBuilder.loadTexts:
    sfpEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

sfpReadWriteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sfpReadWriteCompliance.setStatus(
        "current"
    )

sfpReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sfpReadOnlyCompliance.setStatus(
        "current"
    )

sfpNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 14, 3, 3, 2, 3)
)
if mibBuilder.loadTexts:
    sfpNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-SFP-MIB",
    **{"pdnSfp": pdnSfp,
       "sfpMIBObjects": sfpMIBObjects,
       "sfpCompatibleInterfaceCount": sfpCompatibleInterfaceCount,
       "sfpInfoTable": sfpInfoTable,
       "sfpInfoEntry": sfpInfoEntry,
       "sfpIdentifier": sfpIdentifier,
       "sfpVendorSpecificIdentifier": sfpVendorSpecificIdentifier,
       "sfpExtIdentifier": sfpExtIdentifier,
       "sfpConnector": sfpConnector,
       "sfpVendorSpecificConnector": sfpVendorSpecificConnector,
       "sfpTransceiverComplianceCodes": sfpTransceiverComplianceCodes,
       "sfpFibreChannelLinkLength": sfpFibreChannelLinkLength,
       "sfpFibreChannelTransmitterTechnology": sfpFibreChannelTransmitterTechnology,
       "sfpFibreChannelTransmissionMedia": sfpFibreChannelTransmissionMedia,
       "sfpFibreChannelTransmissionSpeed": sfpFibreChannelTransmissionSpeed,
       "sfpEncoding": sfpEncoding,
       "sfpBRNominal100Mbps": sfpBRNominal100Mbps,
       "sfpLength9MiKm": sfpLength9MiKm,
       "sfpLength9Mi100M": sfpLength9Mi100M,
       "sfpLength50Mi10M": sfpLength50Mi10M,
       "sfpLength62Pt5Mi10M": sfpLength62Pt5Mi10M,
       "sfpLengthCopperM": sfpLengthCopperM,
       "sfpVendorName": sfpVendorName,
       "sfpVendorOUI": sfpVendorOUI,
       "sfpVendorPN": sfpVendorPN,
       "sfpVendorSN": sfpVendorSN,
       "sfpVendorRev": sfpVendorRev,
       "sfpLaserWavelength": sfpLaserWavelength,
       "sfpOptions": sfpOptions,
       "sfpBRMin": sfpBRMin,
       "sfpBRMax": sfpBRMax,
       "sfpVendorDate": sfpVendorDate,
       "sfpVendorSpecificLotCode": sfpVendorSpecificLotCode,
       "sfpVendorSpecificData": sfpVendorSpecificData,
       "sfpStatusCurrent": sfpStatusCurrent,
       "sfpCommandTable": sfpCommandTable,
       "sfpCommandEntry": sfpCommandEntry,
       "sfpCommand": sfpCommand,
       "sfpNotificationEnable": sfpNotificationEnable,
       "sfpMIBNotifications": sfpMIBNotifications,
       "sfpNotificationsPrefix": sfpNotificationsPrefix,
       "sfpEventFaulty": sfpEventFaulty,
       "sfpEventOperational": sfpEventOperational,
       "sfpEventInserted": sfpEventInserted,
       "sfpEventRemoved": sfpEventRemoved,
       "sfpMIBConformance": sfpMIBConformance,
       "sfpGroups": sfpGroups,
       "sfpMIBObjectsGroup": sfpMIBObjectsGroup,
       "sfpInformationGroup": sfpInformationGroup,
       "sfpCommandGroup": sfpCommandGroup,
       "sfpNotificationsGroup": sfpNotificationsGroup,
       "sfpEventGroup": sfpEventGroup,
       "sfpCompliances": sfpCompliances,
       "sfpReadWriteCompliance": sfpReadWriteCompliance,
       "sfpReadOnlyCompliance": sfpReadOnlyCompliance,
       "sfpNotificationCompliance": sfpNotificationCompliance}
)
