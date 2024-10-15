# SNMP MIB module (NBS-SFF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-SFF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:59 2024
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

(nbs,) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "nbs")

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

nbsSffMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 204)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_NbsSffObjects_ObjectIdentity = ObjectIdentity
nbsSffObjects = _NbsSffObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 204, 1)
)
if mibBuilder.loadTexts:
    nbsSffObjects.setStatus("current")
_NbsSffMsaGrp_ObjectIdentity = ObjectIdentity
nbsSffMsaGrp = _NbsSffMsaGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1)
)
if mibBuilder.loadTexts:
    nbsSffMsaGrp.setStatus("current")
_NbsSffMsaTable_Object = MibTable
nbsSffMsaTable = _NbsSffMsaTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1)
)
if mibBuilder.loadTexts:
    nbsSffMsaTable.setStatus("current")
_NbsSffMsaEntry_Object = MibTableRow
nbsSffMsaEntry = _NbsSffMsaEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1)
)
nbsSffMsaEntry.setIndexNames(
    (0, "NBS-SFF-MIB", "nbsSffMsaPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSffMsaEntry.setStatus("current")
_NbsSffMsaPhysicalIfIndex_Type = Integer32
_NbsSffMsaPhysicalIfIndex_Object = MibTableColumn
nbsSffMsaPhysicalIfIndex = _NbsSffMsaPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 1),
    _NbsSffMsaPhysicalIfIndex_Type()
)
nbsSffMsaPhysicalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsSffMsaPhysicalIfIndex.setStatus("current")
_NbsSffMsaIdentifier_Type = Integer32
_NbsSffMsaIdentifier_Object = MibTableColumn
nbsSffMsaIdentifier = _NbsSffMsaIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 2),
    _NbsSffMsaIdentifier_Type()
)
nbsSffMsaIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaIdentifier.setStatus("current")
_NbsSffMsaExtIdentifier_Type = Integer32
_NbsSffMsaExtIdentifier_Object = MibTableColumn
nbsSffMsaExtIdentifier = _NbsSffMsaExtIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 3),
    _NbsSffMsaExtIdentifier_Type()
)
nbsSffMsaExtIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaExtIdentifier.setStatus("current")
_NbsSffMsaOpticalConnector_Type = Integer32
_NbsSffMsaOpticalConnector_Object = MibTableColumn
nbsSffMsaOpticalConnector = _NbsSffMsaOpticalConnector_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 4),
    _NbsSffMsaOpticalConnector_Type()
)
nbsSffMsaOpticalConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaOpticalConnector.setStatus("current")


class _NbsSffMsaTransceiverCodes_Type(OctetString):
    """Custom type nbsSffMsaTransceiverCodes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_NbsSffMsaTransceiverCodes_Type.__name__ = "OctetString"
_NbsSffMsaTransceiverCodes_Object = MibTableColumn
nbsSffMsaTransceiverCodes = _NbsSffMsaTransceiverCodes_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 5),
    _NbsSffMsaTransceiverCodes_Type()
)
nbsSffMsaTransceiverCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaTransceiverCodes.setStatus("current")


class _NbsSffMsaSerialEncoding_Type(Integer32):
    """Custom type nbsSffMsaSerialEncoding based on Integer32"""
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
        *(("lineCode4To5", 3),
          ("lineCode8To10", 2),
          ("manchester", 5),
          ("notSupported", 1),
          ("nrz", 4),
          ("sonetScrambled", 6))
    )


_NbsSffMsaSerialEncoding_Type.__name__ = "Integer32"
_NbsSffMsaSerialEncoding_Object = MibTableColumn
nbsSffMsaSerialEncoding = _NbsSffMsaSerialEncoding_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 6),
    _NbsSffMsaSerialEncoding_Type()
)
nbsSffMsaSerialEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaSerialEncoding.setStatus("current")
_NbsSffMsaNominalBitRate_Type = Integer32
_NbsSffMsaNominalBitRate_Object = MibTableColumn
nbsSffMsaNominalBitRate = _NbsSffMsaNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 7),
    _NbsSffMsaNominalBitRate_Type()
)
nbsSffMsaNominalBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaNominalBitRate.setStatus("current")
_NbsSffMsaLinkLengthSmfKm_Type = Integer32
_NbsSffMsaLinkLengthSmfKm_Object = MibTableColumn
nbsSffMsaLinkLengthSmfKm = _NbsSffMsaLinkLengthSmfKm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 8),
    _NbsSffMsaLinkLengthSmfKm_Type()
)
nbsSffMsaLinkLengthSmfKm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaLinkLengthSmfKm.setStatus("current")
_NbsSffMsaLinkLengthSmf100m_Type = Integer32
_NbsSffMsaLinkLengthSmf100m_Object = MibTableColumn
nbsSffMsaLinkLengthSmf100m = _NbsSffMsaLinkLengthSmf100m_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 9),
    _NbsSffMsaLinkLengthSmf100m_Type()
)
nbsSffMsaLinkLengthSmf100m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaLinkLengthSmf100m.setStatus("current")
_NbsSffMsaLinkLengthMmf10m_Type = Integer32
_NbsSffMsaLinkLengthMmf10m_Object = MibTableColumn
nbsSffMsaLinkLengthMmf10m = _NbsSffMsaLinkLengthMmf10m_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 10),
    _NbsSffMsaLinkLengthMmf10m_Type()
)
nbsSffMsaLinkLengthMmf10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaLinkLengthMmf10m.setStatus("current")
_NbsSffMsaLinkLength625Mmf10m_Type = Integer32
_NbsSffMsaLinkLength625Mmf10m_Object = MibTableColumn
nbsSffMsaLinkLength625Mmf10m = _NbsSffMsaLinkLength625Mmf10m_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 11),
    _NbsSffMsaLinkLength625Mmf10m_Type()
)
nbsSffMsaLinkLength625Mmf10m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaLinkLength625Mmf10m.setStatus("current")
_NbsSffMsaCopperLinkLength_Type = Integer32
_NbsSffMsaCopperLinkLength_Object = MibTableColumn
nbsSffMsaCopperLinkLength = _NbsSffMsaCopperLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 12),
    _NbsSffMsaCopperLinkLength_Type()
)
nbsSffMsaCopperLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaCopperLinkLength.setStatus("current")


class _NbsSffMsaVendorName_Type(DisplayString):
    """Custom type nbsSffMsaVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffMsaVendorName_Type.__name__ = "DisplayString"
_NbsSffMsaVendorName_Object = MibTableColumn
nbsSffMsaVendorName = _NbsSffMsaVendorName_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 13),
    _NbsSffMsaVendorName_Type()
)
nbsSffMsaVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaVendorName.setStatus("current")


class _NbsSffMsaVendorOUI_Type(OctetString):
    """Custom type nbsSffMsaVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_NbsSffMsaVendorOUI_Type.__name__ = "OctetString"
_NbsSffMsaVendorOUI_Object = MibTableColumn
nbsSffMsaVendorOUI = _NbsSffMsaVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 14),
    _NbsSffMsaVendorOUI_Type()
)
nbsSffMsaVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaVendorOUI.setStatus("current")


class _NbsSffMsaVendorPartNumber_Type(DisplayString):
    """Custom type nbsSffMsaVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffMsaVendorPartNumber_Type.__name__ = "DisplayString"
_NbsSffMsaVendorPartNumber_Object = MibTableColumn
nbsSffMsaVendorPartNumber = _NbsSffMsaVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 15),
    _NbsSffMsaVendorPartNumber_Type()
)
nbsSffMsaVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaVendorPartNumber.setStatus("current")


class _NbsSffMsaVendorRevision_Type(DisplayString):
    """Custom type nbsSffMsaVendorRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_NbsSffMsaVendorRevision_Type.__name__ = "DisplayString"
_NbsSffMsaVendorRevision_Object = MibTableColumn
nbsSffMsaVendorRevision = _NbsSffMsaVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 16),
    _NbsSffMsaVendorRevision_Type()
)
nbsSffMsaVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaVendorRevision.setStatus("current")


class _NbsSffMsaBaseChecksumMatch_Type(Integer32):
    """Custom type nbsSffMsaBaseChecksumMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffMsaBaseChecksumMatch_Type.__name__ = "Integer32"
_NbsSffMsaBaseChecksumMatch_Object = MibTableColumn
nbsSffMsaBaseChecksumMatch = _NbsSffMsaBaseChecksumMatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 17),
    _NbsSffMsaBaseChecksumMatch_Type()
)
nbsSffMsaBaseChecksumMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaBaseChecksumMatch.setStatus("current")
_NbsSffMsaLossOfSignalImplemented_Type = Integer32
_NbsSffMsaLossOfSignalImplemented_Object = MibTableColumn
nbsSffMsaLossOfSignalImplemented = _NbsSffMsaLossOfSignalImplemented_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 18),
    _NbsSffMsaLossOfSignalImplemented_Type()
)
nbsSffMsaLossOfSignalImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaLossOfSignalImplemented.setStatus("current")
_NbsSffMsaLossOfSignalInverted_Type = Integer32
_NbsSffMsaLossOfSignalInverted_Object = MibTableColumn
nbsSffMsaLossOfSignalInverted = _NbsSffMsaLossOfSignalInverted_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 19),
    _NbsSffMsaLossOfSignalInverted_Type()
)
nbsSffMsaLossOfSignalInverted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaLossOfSignalInverted.setStatus("current")
_NbsSffMsaTxFault_Type = Integer32
_NbsSffMsaTxFault_Object = MibTableColumn
nbsSffMsaTxFault = _NbsSffMsaTxFault_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 20),
    _NbsSffMsaTxFault_Type()
)
nbsSffMsaTxFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaTxFault.setStatus("current")
_NbsSffMsaTxDisable_Type = Integer32
_NbsSffMsaTxDisable_Object = MibTableColumn
nbsSffMsaTxDisable = _NbsSffMsaTxDisable_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 21),
    _NbsSffMsaTxDisable_Type()
)
nbsSffMsaTxDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaTxDisable.setStatus("current")


class _NbsSffMsaRateSelectImplemented_Type(Integer32):
    """Custom type nbsSffMsaRateSelectImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffMsaRateSelectImplemented_Type.__name__ = "Integer32"
_NbsSffMsaRateSelectImplemented_Object = MibTableColumn
nbsSffMsaRateSelectImplemented = _NbsSffMsaRateSelectImplemented_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 22),
    _NbsSffMsaRateSelectImplemented_Type()
)
nbsSffMsaRateSelectImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaRateSelectImplemented.setStatus("current")
_NbsSffMsaMaxBitRate_Type = Integer32
_NbsSffMsaMaxBitRate_Object = MibTableColumn
nbsSffMsaMaxBitRate = _NbsSffMsaMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 23),
    _NbsSffMsaMaxBitRate_Type()
)
nbsSffMsaMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaMaxBitRate.setStatus("current")
_NbsSffMsaMinBitRate_Type = Integer32
_NbsSffMsaMinBitRate_Object = MibTableColumn
nbsSffMsaMinBitRate = _NbsSffMsaMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 24),
    _NbsSffMsaMinBitRate_Type()
)
nbsSffMsaMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaMinBitRate.setStatus("current")


class _NbsSffMsaVendorSerialNumber_Type(DisplayString):
    """Custom type nbsSffMsaVendorSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffMsaVendorSerialNumber_Type.__name__ = "DisplayString"
_NbsSffMsaVendorSerialNumber_Object = MibTableColumn
nbsSffMsaVendorSerialNumber = _NbsSffMsaVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 25),
    _NbsSffMsaVendorSerialNumber_Type()
)
nbsSffMsaVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaVendorSerialNumber.setStatus("current")


class _NbsSffMsaVendorDateCode_Type(DisplayString):
    """Custom type nbsSffMsaVendorDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 8),
    )


_NbsSffMsaVendorDateCode_Type.__name__ = "DisplayString"
_NbsSffMsaVendorDateCode_Object = MibTableColumn
nbsSffMsaVendorDateCode = _NbsSffMsaVendorDateCode_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 26),
    _NbsSffMsaVendorDateCode_Type()
)
nbsSffMsaVendorDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaVendorDateCode.setStatus("current")


class _NbsSffMsaExtChecksumMatch_Type(Integer32):
    """Custom type nbsSffMsaExtChecksumMatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffMsaExtChecksumMatch_Type.__name__ = "Integer32"
_NbsSffMsaExtChecksumMatch_Object = MibTableColumn
nbsSffMsaExtChecksumMatch = _NbsSffMsaExtChecksumMatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 1, 1, 1, 27),
    _NbsSffMsaExtChecksumMatch_Type()
)
nbsSffMsaExtChecksumMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsaExtChecksumMatch.setStatus("current")
_NbsSffWdmGrp_ObjectIdentity = ObjectIdentity
nbsSffWdmGrp = _NbsSffWdmGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2)
)
if mibBuilder.loadTexts:
    nbsSffWdmGrp.setStatus("current")
_NbsSffWdmTable_Object = MibTable
nbsSffWdmTable = _NbsSffWdmTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nbsSffWdmTable.setStatus("current")
_NbsSffWdmEntry_Object = MibTableRow
nbsSffWdmEntry = _NbsSffWdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1)
)
nbsSffWdmEntry.setIndexNames(
    (0, "NBS-SFF-MIB", "nbsSffMsaPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSffWdmEntry.setStatus("current")


class _NbsSffWdmClassOfPower_Type(Integer32):
    """Custom type nbsSffWdmClassOfPower based on Integer32"""
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
        *(("oneToOneAndHalfW", 2),
          ("overOneAndHalfW", 3),
          ("reserved", 4),
          ("under1W", 1))
    )


_NbsSffWdmClassOfPower_Type.__name__ = "Integer32"
_NbsSffWdmClassOfPower_Object = MibTableColumn
nbsSffWdmClassOfPower = _NbsSffWdmClassOfPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 1),
    _NbsSffWdmClassOfPower_Type()
)
nbsSffWdmClassOfPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmClassOfPower.setStatus("current")


class _NbsSffWdmClassOfTemperature_Type(Integer32):
    """Custom type nbsSffWdmClassOfTemperature based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4))
    )


_NbsSffWdmClassOfTemperature_Type.__name__ = "Integer32"
_NbsSffWdmClassOfTemperature_Object = MibTableColumn
nbsSffWdmClassOfTemperature = _NbsSffWdmClassOfTemperature_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 2),
    _NbsSffWdmClassOfTemperature_Type()
)
nbsSffWdmClassOfTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmClassOfTemperature.setStatus("current")


class _NbsSffWdmClassOfWdm_Type(Integer32):
    """Custom type nbsSffWdmClassOfWdm based on Integer32"""
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
        *(("cwdm", 2),
          ("dwdm", 3),
          ("noWdm", 1),
          ("reserved", 4))
    )


_NbsSffWdmClassOfWdm_Type.__name__ = "Integer32"
_NbsSffWdmClassOfWdm_Object = MibTableColumn
nbsSffWdmClassOfWdm = _NbsSffWdmClassOfWdm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 3),
    _NbsSffWdmClassOfWdm_Type()
)
nbsSffWdmClassOfWdm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmClassOfWdm.setStatus("current")
_NbsSffWdmOpticalReach_Type = Integer32
_NbsSffWdmOpticalReach_Object = MibTableColumn
nbsSffWdmOpticalReach = _NbsSffWdmOpticalReach_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 4),
    _NbsSffWdmOpticalReach_Type()
)
nbsSffWdmOpticalReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmOpticalReach.setStatus("current")


class _NbsSffWdmMaxCaseTemperature_Type(Integer32):
    """Custom type nbsSffWdmMaxCaseTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_NbsSffWdmMaxCaseTemperature_Type.__name__ = "Integer32"
_NbsSffWdmMaxCaseTemperature_Object = MibTableColumn
nbsSffWdmMaxCaseTemperature = _NbsSffWdmMaxCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 5),
    _NbsSffWdmMaxCaseTemperature_Type()
)
nbsSffWdmMaxCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmMaxCaseTemperature.setStatus("current")


class _NbsSffWdmMinCaseTemperature_Type(Integer32):
    """Custom type nbsSffWdmMinCaseTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_NbsSffWdmMinCaseTemperature_Type.__name__ = "Integer32"
_NbsSffWdmMinCaseTemperature_Object = MibTableColumn
nbsSffWdmMinCaseTemperature = _NbsSffWdmMinCaseTemperature_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 6),
    _NbsSffWdmMinCaseTemperature_Type()
)
nbsSffWdmMinCaseTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmMinCaseTemperature.setStatus("current")
_NbsSffWdmMaxSupplyCurrent_Type = Integer32
_NbsSffWdmMaxSupplyCurrent_Object = MibTableColumn
nbsSffWdmMaxSupplyCurrent = _NbsSffWdmMaxSupplyCurrent_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 7),
    _NbsSffWdmMaxSupplyCurrent_Type()
)
nbsSffWdmMaxSupplyCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmMaxSupplyCurrent.setStatus("current")
_NbsSffWdmNumberOfChannels_Type = Integer32
_NbsSffWdmNumberOfChannels_Object = MibTableColumn
nbsSffWdmNumberOfChannels = _NbsSffWdmNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 8),
    _NbsSffWdmNumberOfChannels_Type()
)
nbsSffWdmNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmNumberOfChannels.setStatus("current")


class _NbsSffWdmChannelSpacing_Type(Integer32):
    """Custom type nbsSffWdmChannelSpacing based on Integer32"""
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
        *(("ghz100", 3),
          ("ghz200", 4),
          ("ghz50", 2),
          ("notTunable", 1))
    )


_NbsSffWdmChannelSpacing_Type.__name__ = "Integer32"
_NbsSffWdmChannelSpacing_Object = MibTableColumn
nbsSffWdmChannelSpacing = _NbsSffWdmChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 9),
    _NbsSffWdmChannelSpacing_Type()
)
nbsSffWdmChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmChannelSpacing.setStatus("current")


class _NbsSffWdmVariableDecisionThreshold_Type(Integer32):
    """Custom type nbsSffWdmVariableDecisionThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbsSffWdmVariableDecisionThreshold_Type.__name__ = "Integer32"
_NbsSffWdmVariableDecisionThreshold_Object = MibTableColumn
nbsSffWdmVariableDecisionThreshold = _NbsSffWdmVariableDecisionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 10),
    _NbsSffWdmVariableDecisionThreshold_Type()
)
nbsSffWdmVariableDecisionThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmVariableDecisionThreshold.setStatus("current")


class _NbsSffWdmWavelengthMonitorType_Type(Integer32):
    """Custom type nbsSffWdmWavelengthMonitorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("laserTemperature", 2),
          ("wavelength", 1))
    )


_NbsSffWdmWavelengthMonitorType_Type.__name__ = "Integer32"
_NbsSffWdmWavelengthMonitorType_Object = MibTableColumn
nbsSffWdmWavelengthMonitorType = _NbsSffWdmWavelengthMonitorType_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 11),
    _NbsSffWdmWavelengthMonitorType_Type()
)
nbsSffWdmWavelengthMonitorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmWavelengthMonitorType.setStatus("current")


class _NbsSffWdmExtTransmitPowerType_Type(Integer32):
    """Custom type nbsSffWdmExtTransmitPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pwrDefault", 1),
          ("pwrExtended", 2))
    )


_NbsSffWdmExtTransmitPowerType_Type.__name__ = "Integer32"
_NbsSffWdmExtTransmitPowerType_Object = MibTableColumn
nbsSffWdmExtTransmitPowerType = _NbsSffWdmExtTransmitPowerType_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 12),
    _NbsSffWdmExtTransmitPowerType_Type()
)
nbsSffWdmExtTransmitPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmExtTransmitPowerType.setStatus("current")


class _NbsSffWdmVariableOpticalAttenuator_Type(Integer32):
    """Custom type nbsSffWdmVariableOpticalAttenuator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffWdmVariableOpticalAttenuator_Type.__name__ = "Integer32"
_NbsSffWdmVariableOpticalAttenuator_Object = MibTableColumn
nbsSffWdmVariableOpticalAttenuator = _NbsSffWdmVariableOpticalAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 13),
    _NbsSffWdmVariableOpticalAttenuator_Type()
)
nbsSffWdmVariableOpticalAttenuator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmVariableOpticalAttenuator.setStatus("current")


class _NbsSffWdmPilotToneFunctionality_Type(Integer32):
    """Custom type nbsSffWdmPilotToneFunctionality based on Integer32"""
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
        *(("pilotToneDetection", 2),
          ("pilotToneEnhanced", 5),
          ("pilotToneInjection", 3),
          ("pilotToneInjectionDetection", 4),
          ("pilotToneNone", 1))
    )


_NbsSffWdmPilotToneFunctionality_Type.__name__ = "Integer32"
_NbsSffWdmPilotToneFunctionality_Object = MibTableColumn
nbsSffWdmPilotToneFunctionality = _NbsSffWdmPilotToneFunctionality_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 14),
    _NbsSffWdmPilotToneFunctionality_Type()
)
nbsSffWdmPilotToneFunctionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmPilotToneFunctionality.setStatus("current")


class _NbsSffWdmOptionalInterruptPin_Type(Integer32):
    """Custom type nbsSffWdmOptionalInterruptPin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbsSffWdmOptionalInterruptPin_Type.__name__ = "Integer32"
_NbsSffWdmOptionalInterruptPin_Object = MibTableColumn
nbsSffWdmOptionalInterruptPin = _NbsSffWdmOptionalInterruptPin_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 15),
    _NbsSffWdmOptionalInterruptPin_Type()
)
nbsSffWdmOptionalInterruptPin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmOptionalInterruptPin.setStatus("current")


class _NbsSffWdmLaserWavelength_Type(DisplayString):
    """Custom type nbsSffWdmLaserWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_NbsSffWdmLaserWavelength_Type.__name__ = "DisplayString"
_NbsSffWdmLaserWavelength_Object = MibTableColumn
nbsSffWdmLaserWavelength = _NbsSffWdmLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 2, 1, 1, 16),
    _NbsSffWdmLaserWavelength_Type()
)
nbsSffWdmLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffWdmLaserWavelength.setStatus("current")
_NbsSffDiagnosticsGrp_ObjectIdentity = ObjectIdentity
nbsSffDiagnosticsGrp = _NbsSffDiagnosticsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3)
)
if mibBuilder.loadTexts:
    nbsSffDiagnosticsGrp.setStatus("current")
_NbsSffDiagsTable_Object = MibTable
nbsSffDiagsTable = _NbsSffDiagsTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1)
)
if mibBuilder.loadTexts:
    nbsSffDiagsTable.setStatus("current")
_NbsSffDiagsEntry_Object = MibTableRow
nbsSffDiagsEntry = _NbsSffDiagsEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1)
)
nbsSffDiagsEntry.setIndexNames(
    (0, "NBS-SFF-MIB", "nbsSffMsaPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSffDiagsEntry.setStatus("current")


class _NbsSffDiagsRateIdentifier_Type(Integer32):
    """Custom type nbsSffDiagsRateIdentifier based on Integer32"""
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
        *(("notSupported", 1),
          ("rate421G", 2),
          ("rate842GRx", 3),
          ("rate842GRxTx", 4),
          ("rate842GTx", 5))
    )


_NbsSffDiagsRateIdentifier_Type.__name__ = "Integer32"
_NbsSffDiagsRateIdentifier_Object = MibTableColumn
nbsSffDiagsRateIdentifier = _NbsSffDiagsRateIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 1),
    _NbsSffDiagsRateIdentifier_Type()
)
nbsSffDiagsRateIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRateIdentifier.setStatus("current")
_NbsSffDiagsLinkLengthOm3_Type = Integer32
_NbsSffDiagsLinkLengthOm3_Object = MibTableColumn
nbsSffDiagsLinkLengthOm3 = _NbsSffDiagsLinkLengthOm3_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 2),
    _NbsSffDiagsLinkLengthOm3_Type()
)
nbsSffDiagsLinkLengthOm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsLinkLengthOm3.setStatus("current")
_NbsSffDiagsLaserWavelength_Type = Integer32
_NbsSffDiagsLaserWavelength_Object = MibTableColumn
nbsSffDiagsLaserWavelength = _NbsSffDiagsLaserWavelength_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 3),
    _NbsSffDiagsLaserWavelength_Type()
)
nbsSffDiagsLaserWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsLaserWavelength.setStatus("current")


class _NbsSffDiagsLROutputImplemented_Type(Integer32):
    """Custom type nbsSffDiagsLROutputImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffDiagsLROutputImplemented_Type.__name__ = "Integer32"
_NbsSffDiagsLROutputImplemented_Object = MibTableColumn
nbsSffDiagsLROutputImplemented = _NbsSffDiagsLROutputImplemented_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 4),
    _NbsSffDiagsLROutputImplemented_Type()
)
nbsSffDiagsLROutputImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsLROutputImplemented.setStatus("current")


class _NbsSffDiagsPowerLevelDeclaration_Type(Integer32):
    """Custom type nbsSffDiagsPowerLevelDeclaration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_NbsSffDiagsPowerLevelDeclaration_Type.__name__ = "Integer32"
_NbsSffDiagsPowerLevelDeclaration_Object = MibTableColumn
nbsSffDiagsPowerLevelDeclaration = _NbsSffDiagsPowerLevelDeclaration_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 5),
    _NbsSffDiagsPowerLevelDeclaration_Type()
)
nbsSffDiagsPowerLevelDeclaration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsPowerLevelDeclaration.setStatus("current")


class _NbsSffDiagsCooledTranDeclaration_Type(Integer32):
    """Custom type nbsSffDiagsCooledTranDeclaration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cooled", 2),
          ("uncooled", 1))
    )


_NbsSffDiagsCooledTranDeclaration_Type.__name__ = "Integer32"
_NbsSffDiagsCooledTranDeclaration_Object = MibTableColumn
nbsSffDiagsCooledTranDeclaration = _NbsSffDiagsCooledTranDeclaration_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 6),
    _NbsSffDiagsCooledTranDeclaration_Type()
)
nbsSffDiagsCooledTranDeclaration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsCooledTranDeclaration.setStatus("current")


class _NbsSffDiagsAddressChangeRequired_Type(Integer32):
    """Custom type nbsSffDiagsAddressChangeRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffDiagsAddressChangeRequired_Type.__name__ = "Integer32"
_NbsSffDiagsAddressChangeRequired_Object = MibTableColumn
nbsSffDiagsAddressChangeRequired = _NbsSffDiagsAddressChangeRequired_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 7),
    _NbsSffDiagsAddressChangeRequired_Type()
)
nbsSffDiagsAddressChangeRequired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsAddressChangeRequired.setStatus("current")


class _NbsSffDiagsPowerMeasurementType_Type(Integer32):
    """Custom type nbsSffDiagsPowerMeasurementType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("averagePower", 2),
          ("oma", 1))
    )


_NbsSffDiagsPowerMeasurementType_Type.__name__ = "Integer32"
_NbsSffDiagsPowerMeasurementType_Object = MibTableColumn
nbsSffDiagsPowerMeasurementType = _NbsSffDiagsPowerMeasurementType_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 8),
    _NbsSffDiagsPowerMeasurementType_Type()
)
nbsSffDiagsPowerMeasurementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsPowerMeasurementType.setStatus("current")


class _NbsSffDiagsExternallyCalibrated_Type(Integer32):
    """Custom type nbsSffDiagsExternallyCalibrated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffDiagsExternallyCalibrated_Type.__name__ = "Integer32"
_NbsSffDiagsExternallyCalibrated_Object = MibTableColumn
nbsSffDiagsExternallyCalibrated = _NbsSffDiagsExternallyCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 9),
    _NbsSffDiagsExternallyCalibrated_Type()
)
nbsSffDiagsExternallyCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsExternallyCalibrated.setStatus("current")


class _NbsSffDiagsInternallyCalibrated_Type(Integer32):
    """Custom type nbsSffDiagsInternallyCalibrated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffDiagsInternallyCalibrated_Type.__name__ = "Integer32"
_NbsSffDiagsInternallyCalibrated_Object = MibTableColumn
nbsSffDiagsInternallyCalibrated = _NbsSffDiagsInternallyCalibrated_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 10),
    _NbsSffDiagsInternallyCalibrated_Type()
)
nbsSffDiagsInternallyCalibrated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsInternallyCalibrated.setStatus("current")


class _NbsSffDiagsDDMonitoringImplemented_Type(Integer32):
    """Custom type nbsSffDiagsDDMonitoringImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsSffDiagsDDMonitoringImplemented_Type.__name__ = "Integer32"
_NbsSffDiagsDDMonitoringImplemented_Object = MibTableColumn
nbsSffDiagsDDMonitoringImplemented = _NbsSffDiagsDDMonitoringImplemented_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 11),
    _NbsSffDiagsDDMonitoringImplemented_Type()
)
nbsSffDiagsDDMonitoringImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsDDMonitoringImplemented.setStatus("current")


class _NbsSffDiagsOptRateSelectControl_Type(Integer32):
    """Custom type nbsSffDiagsOptRateSelectControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffDiagsOptRateSelectControl_Type.__name__ = "Integer32"
_NbsSffDiagsOptRateSelectControl_Object = MibTableColumn
nbsSffDiagsOptRateSelectControl = _NbsSffDiagsOptRateSelectControl_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 12),
    _NbsSffDiagsOptRateSelectControl_Type()
)
nbsSffDiagsOptRateSelectControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsOptRateSelectControl.setStatus("current")


class _NbsSffDiagsOptAppSelectControl_Type(Integer32):
    """Custom type nbsSffDiagsOptAppSelectControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffDiagsOptAppSelectControl_Type.__name__ = "Integer32"
_NbsSffDiagsOptAppSelectControl_Object = MibTableColumn
nbsSffDiagsOptAppSelectControl = _NbsSffDiagsOptAppSelectControl_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 13),
    _NbsSffDiagsOptAppSelectControl_Type()
)
nbsSffDiagsOptAppSelectControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsOptAppSelectControl.setStatus("current")


class _NbsSffDiagsOptSoftRSControlMon_Type(Integer32):
    """Custom type nbsSffDiagsOptSoftRSControlMon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffDiagsOptSoftRSControlMon_Type.__name__ = "Integer32"
_NbsSffDiagsOptSoftRSControlMon_Object = MibTableColumn
nbsSffDiagsOptSoftRSControlMon = _NbsSffDiagsOptSoftRSControlMon_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 14),
    _NbsSffDiagsOptSoftRSControlMon_Type()
)
nbsSffDiagsOptSoftRSControlMon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsOptSoftRSControlMon.setStatus("current")


class _NbsSffDiagsOptSoftRxLoSMonitoring_Type(Integer32):
    """Custom type nbsSffDiagsOptSoftRxLoSMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffDiagsOptSoftRxLoSMonitoring_Type.__name__ = "Integer32"
_NbsSffDiagsOptSoftRxLoSMonitoring_Object = MibTableColumn
nbsSffDiagsOptSoftRxLoSMonitoring = _NbsSffDiagsOptSoftRxLoSMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 15),
    _NbsSffDiagsOptSoftRxLoSMonitoring_Type()
)
nbsSffDiagsOptSoftRxLoSMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsOptSoftRxLoSMonitoring.setStatus("current")


class _NbsSffDiagsOptSoftTxFaultMonitoring_Type(Integer32):
    """Custom type nbsSffDiagsOptSoftTxFaultMonitoring based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffDiagsOptSoftTxFaultMonitoring_Type.__name__ = "Integer32"
_NbsSffDiagsOptSoftTxFaultMonitoring_Object = MibTableColumn
nbsSffDiagsOptSoftTxFaultMonitoring = _NbsSffDiagsOptSoftTxFaultMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 16),
    _NbsSffDiagsOptSoftTxFaultMonitoring_Type()
)
nbsSffDiagsOptSoftTxFaultMonitoring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsOptSoftTxFaultMonitoring.setStatus("current")


class _NbsSffDiagsOptSoftTxDisable_Type(Integer32):
    """Custom type nbsSffDiagsOptSoftTxDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffDiagsOptSoftTxDisable_Type.__name__ = "Integer32"
_NbsSffDiagsOptSoftTxDisable_Object = MibTableColumn
nbsSffDiagsOptSoftTxDisable = _NbsSffDiagsOptSoftTxDisable_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 17),
    _NbsSffDiagsOptSoftTxDisable_Type()
)
nbsSffDiagsOptSoftTxDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsOptSoftTxDisable.setStatus("current")


class _NbsSffDiagsOptAlarmWarningFlags_Type(Integer32):
    """Custom type nbsSffDiagsOptAlarmWarningFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("implemented", 2),
          ("notImplemented", 1))
    )


_NbsSffDiagsOptAlarmWarningFlags_Type.__name__ = "Integer32"
_NbsSffDiagsOptAlarmWarningFlags_Object = MibTableColumn
nbsSffDiagsOptAlarmWarningFlags = _NbsSffDiagsOptAlarmWarningFlags_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 18),
    _NbsSffDiagsOptAlarmWarningFlags_Type()
)
nbsSffDiagsOptAlarmWarningFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsOptAlarmWarningFlags.setStatus("current")


class _NbsSffDiags8472Compliance_Type(Integer32):
    """Custom type nbsSffDiags8472Compliance based on Integer32"""
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
        *(("notSupported", 1),
          ("rev10dot2of8472", 4),
          ("rev9dot3of8472", 2),
          ("rev9dot5of8472", 3))
    )


_NbsSffDiags8472Compliance_Type.__name__ = "Integer32"
_NbsSffDiags8472Compliance_Object = MibTableColumn
nbsSffDiags8472Compliance = _NbsSffDiags8472Compliance_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 19),
    _NbsSffDiags8472Compliance_Type()
)
nbsSffDiags8472Compliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiags8472Compliance.setStatus("current")


class _NbsSffDiagsTemperature_Type(Integer32):
    """Custom type nbsSffDiagsTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_NbsSffDiagsTemperature_Type.__name__ = "Integer32"
_NbsSffDiagsTemperature_Object = MibTableColumn
nbsSffDiagsTemperature = _NbsSffDiagsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 20),
    _NbsSffDiagsTemperature_Type()
)
nbsSffDiagsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTemperature.setStatus("current")
_NbsSffDiagsTempLowAlarm_Type = Integer32
_NbsSffDiagsTempLowAlarm_Object = MibTableColumn
nbsSffDiagsTempLowAlarm = _NbsSffDiagsTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 21),
    _NbsSffDiagsTempLowAlarm_Type()
)
nbsSffDiagsTempLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTempLowAlarm.setStatus("current")
_NbsSffDiagsTempLowWarn_Type = Integer32
_NbsSffDiagsTempLowWarn_Object = MibTableColumn
nbsSffDiagsTempLowWarn = _NbsSffDiagsTempLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 22),
    _NbsSffDiagsTempLowWarn_Type()
)
nbsSffDiagsTempLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTempLowWarn.setStatus("current")
_NbsSffDiagsTempHighWarn_Type = Integer32
_NbsSffDiagsTempHighWarn_Object = MibTableColumn
nbsSffDiagsTempHighWarn = _NbsSffDiagsTempHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 23),
    _NbsSffDiagsTempHighWarn_Type()
)
nbsSffDiagsTempHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTempHighWarn.setStatus("current")
_NbsSffDiagsTempHighAlarm_Type = Integer32
_NbsSffDiagsTempHighAlarm_Object = MibTableColumn
nbsSffDiagsTempHighAlarm = _NbsSffDiagsTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 24),
    _NbsSffDiagsTempHighAlarm_Type()
)
nbsSffDiagsTempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTempHighAlarm.setStatus("current")


class _NbsSffDiagsVoltage_Type(DisplayString):
    """Custom type nbsSffDiagsVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsVoltage_Type.__name__ = "DisplayString"
_NbsSffDiagsVoltage_Object = MibTableColumn
nbsSffDiagsVoltage = _NbsSffDiagsVoltage_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 25),
    _NbsSffDiagsVoltage_Type()
)
nbsSffDiagsVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsVoltage.setStatus("current")
_NbsSffDiagsVoltLowAlarm_Type = Integer32
_NbsSffDiagsVoltLowAlarm_Object = MibTableColumn
nbsSffDiagsVoltLowAlarm = _NbsSffDiagsVoltLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 26),
    _NbsSffDiagsVoltLowAlarm_Type()
)
nbsSffDiagsVoltLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsVoltLowAlarm.setStatus("current")
_NbsSffDiagsVoltLowWarn_Type = Integer32
_NbsSffDiagsVoltLowWarn_Object = MibTableColumn
nbsSffDiagsVoltLowWarn = _NbsSffDiagsVoltLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 27),
    _NbsSffDiagsVoltLowWarn_Type()
)
nbsSffDiagsVoltLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsVoltLowWarn.setStatus("current")
_NbsSffDiagsVoltHighWarn_Type = Integer32
_NbsSffDiagsVoltHighWarn_Object = MibTableColumn
nbsSffDiagsVoltHighWarn = _NbsSffDiagsVoltHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 28),
    _NbsSffDiagsVoltHighWarn_Type()
)
nbsSffDiagsVoltHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsVoltHighWarn.setStatus("current")
_NbsSffDiagsVoltHighAlarm_Type = Integer32
_NbsSffDiagsVoltHighAlarm_Object = MibTableColumn
nbsSffDiagsVoltHighAlarm = _NbsSffDiagsVoltHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 29),
    _NbsSffDiagsVoltHighAlarm_Type()
)
nbsSffDiagsVoltHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsVoltHighAlarm.setStatus("current")


class _NbsSffDiagsBiasCurrent_Type(DisplayString):
    """Custom type nbsSffDiagsBiasCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsBiasCurrent_Type.__name__ = "DisplayString"
_NbsSffDiagsBiasCurrent_Object = MibTableColumn
nbsSffDiagsBiasCurrent = _NbsSffDiagsBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 30),
    _NbsSffDiagsBiasCurrent_Type()
)
nbsSffDiagsBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsBiasCurrent.setStatus("current")
_NbsSffDiagsBiasLowAlarm_Type = Integer32
_NbsSffDiagsBiasLowAlarm_Object = MibTableColumn
nbsSffDiagsBiasLowAlarm = _NbsSffDiagsBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 31),
    _NbsSffDiagsBiasLowAlarm_Type()
)
nbsSffDiagsBiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsBiasLowAlarm.setStatus("current")
_NbsSffDiagsBiasLowWarn_Type = Integer32
_NbsSffDiagsBiasLowWarn_Object = MibTableColumn
nbsSffDiagsBiasLowWarn = _NbsSffDiagsBiasLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 32),
    _NbsSffDiagsBiasLowWarn_Type()
)
nbsSffDiagsBiasLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsBiasLowWarn.setStatus("current")
_NbsSffDiagsBiasHighWarn_Type = Integer32
_NbsSffDiagsBiasHighWarn_Object = MibTableColumn
nbsSffDiagsBiasHighWarn = _NbsSffDiagsBiasHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 33),
    _NbsSffDiagsBiasHighWarn_Type()
)
nbsSffDiagsBiasHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsBiasHighWarn.setStatus("current")
_NbsSffDiagsBiasHighAlarm_Type = Integer32
_NbsSffDiagsBiasHighAlarm_Object = MibTableColumn
nbsSffDiagsBiasHighAlarm = _NbsSffDiagsBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 34),
    _NbsSffDiagsBiasHighAlarm_Type()
)
nbsSffDiagsBiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsBiasHighAlarm.setStatus("current")


class _NbsSffDiagsTxPower_Type(DisplayString):
    """Custom type nbsSffDiagsTxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsTxPower_Type.__name__ = "DisplayString"
_NbsSffDiagsTxPower_Object = MibTableColumn
nbsSffDiagsTxPower = _NbsSffDiagsTxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 35),
    _NbsSffDiagsTxPower_Type()
)
nbsSffDiagsTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxPower.setStatus("current")
_NbsSffDiagsTxPowerLowAlarm_Type = Integer32
_NbsSffDiagsTxPowerLowAlarm_Object = MibTableColumn
nbsSffDiagsTxPowerLowAlarm = _NbsSffDiagsTxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 36),
    _NbsSffDiagsTxPowerLowAlarm_Type()
)
nbsSffDiagsTxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxPowerLowAlarm.setStatus("current")
_NbsSffDiagsTxPowerLowWarn_Type = Integer32
_NbsSffDiagsTxPowerLowWarn_Object = MibTableColumn
nbsSffDiagsTxPowerLowWarn = _NbsSffDiagsTxPowerLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 37),
    _NbsSffDiagsTxPowerLowWarn_Type()
)
nbsSffDiagsTxPowerLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxPowerLowWarn.setStatus("current")
_NbsSffDiagsTxPowerHighWarn_Type = Integer32
_NbsSffDiagsTxPowerHighWarn_Object = MibTableColumn
nbsSffDiagsTxPowerHighWarn = _NbsSffDiagsTxPowerHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 38),
    _NbsSffDiagsTxPowerHighWarn_Type()
)
nbsSffDiagsTxPowerHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxPowerHighWarn.setStatus("current")
_NbsSffDiagsTxPowerHighAlarm_Type = Integer32
_NbsSffDiagsTxPowerHighAlarm_Object = MibTableColumn
nbsSffDiagsTxPowerHighAlarm = _NbsSffDiagsTxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 39),
    _NbsSffDiagsTxPowerHighAlarm_Type()
)
nbsSffDiagsTxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxPowerHighAlarm.setStatus("current")


class _NbsSffDiagsRxPower_Type(DisplayString):
    """Custom type nbsSffDiagsRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsRxPower_Type.__name__ = "DisplayString"
_NbsSffDiagsRxPower_Object = MibTableColumn
nbsSffDiagsRxPower = _NbsSffDiagsRxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 40),
    _NbsSffDiagsRxPower_Type()
)
nbsSffDiagsRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRxPower.setStatus("current")
_NbsSffDiagsRxPowerLowAlarm_Type = Integer32
_NbsSffDiagsRxPowerLowAlarm_Object = MibTableColumn
nbsSffDiagsRxPowerLowAlarm = _NbsSffDiagsRxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 41),
    _NbsSffDiagsRxPowerLowAlarm_Type()
)
nbsSffDiagsRxPowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRxPowerLowAlarm.setStatus("current")
_NbsSffDiagsRxPowerLowWarn_Type = Integer32
_NbsSffDiagsRxPowerLowWarn_Object = MibTableColumn
nbsSffDiagsRxPowerLowWarn = _NbsSffDiagsRxPowerLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 42),
    _NbsSffDiagsRxPowerLowWarn_Type()
)
nbsSffDiagsRxPowerLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRxPowerLowWarn.setStatus("current")
_NbsSffDiagsRxPowerHighWarn_Type = Integer32
_NbsSffDiagsRxPowerHighWarn_Object = MibTableColumn
nbsSffDiagsRxPowerHighWarn = _NbsSffDiagsRxPowerHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 43),
    _NbsSffDiagsRxPowerHighWarn_Type()
)
nbsSffDiagsRxPowerHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRxPowerHighWarn.setStatus("current")
_NbsSffDiagsRxPowerHighAlarm_Type = Integer32
_NbsSffDiagsRxPowerHighAlarm_Object = MibTableColumn
nbsSffDiagsRxPowerHighAlarm = _NbsSffDiagsRxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 44),
    _NbsSffDiagsRxPowerHighAlarm_Type()
)
nbsSffDiagsRxPowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRxPowerHighAlarm.setStatus("current")
_NbsSffDiagsDataReadyBarState_Type = Integer32
_NbsSffDiagsDataReadyBarState_Object = MibTableColumn
nbsSffDiagsDataReadyBarState = _NbsSffDiagsDataReadyBarState_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 45),
    _NbsSffDiagsDataReadyBarState_Type()
)
nbsSffDiagsDataReadyBarState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsDataReadyBarState.setStatus("current")
_NbsSffDiagsRxLosState_Type = Integer32
_NbsSffDiagsRxLosState_Object = MibTableColumn
nbsSffDiagsRxLosState = _NbsSffDiagsRxLosState_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 46),
    _NbsSffDiagsRxLosState_Type()
)
nbsSffDiagsRxLosState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRxLosState.setStatus("current")
_NbsSffDiagsTxFaultState_Type = Integer32
_NbsSffDiagsTxFaultState_Object = MibTableColumn
nbsSffDiagsTxFaultState = _NbsSffDiagsTxFaultState_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 47),
    _NbsSffDiagsTxFaultState_Type()
)
nbsSffDiagsTxFaultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxFaultState.setStatus("current")
_NbsSffDiagsSoftRateSelect_Type = Integer32
_NbsSffDiagsSoftRateSelect_Object = MibTableColumn
nbsSffDiagsSoftRateSelect = _NbsSffDiagsSoftRateSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 48),
    _NbsSffDiagsSoftRateSelect_Type()
)
nbsSffDiagsSoftRateSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsSoftRateSelect.setStatus("current")
_NbsSffDiagsRateSelectState0_Type = Integer32
_NbsSffDiagsRateSelectState0_Object = MibTableColumn
nbsSffDiagsRateSelectState0 = _NbsSffDiagsRateSelectState0_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 49),
    _NbsSffDiagsRateSelectState0_Type()
)
nbsSffDiagsRateSelectState0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRateSelectState0.setStatus("current")
_NbsSffDiagsRS1State_Type = Integer32
_NbsSffDiagsRS1State_Object = MibTableColumn
nbsSffDiagsRS1State = _NbsSffDiagsRS1State_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 50),
    _NbsSffDiagsRS1State_Type()
)
nbsSffDiagsRS1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsRS1State.setStatus("current")
_NbsSffDiagsSoftTxDisableSelect_Type = Integer32
_NbsSffDiagsSoftTxDisableSelect_Object = MibTableColumn
nbsSffDiagsSoftTxDisableSelect = _NbsSffDiagsSoftTxDisableSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 51),
    _NbsSffDiagsSoftTxDisableSelect_Type()
)
nbsSffDiagsSoftTxDisableSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsSoftTxDisableSelect.setStatus("current")
_NbsSffDiagsTxDisableState_Type = Integer32
_NbsSffDiagsTxDisableState_Object = MibTableColumn
nbsSffDiagsTxDisableState = _NbsSffDiagsTxDisableState_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 52),
    _NbsSffDiagsTxDisableState_Type()
)
nbsSffDiagsTxDisableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxDisableState.setStatus("current")


class _NbsSffDiagsBiasCurrentSlope_Type(DisplayString):
    """Custom type nbsSffDiagsBiasCurrentSlope based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsBiasCurrentSlope_Type.__name__ = "DisplayString"
_NbsSffDiagsBiasCurrentSlope_Object = MibTableColumn
nbsSffDiagsBiasCurrentSlope = _NbsSffDiagsBiasCurrentSlope_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 53),
    _NbsSffDiagsBiasCurrentSlope_Type()
)
nbsSffDiagsBiasCurrentSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsBiasCurrentSlope.setStatus("current")
_NbsSffDiagsBiasCurrentOffset_Type = Integer32
_NbsSffDiagsBiasCurrentOffset_Object = MibTableColumn
nbsSffDiagsBiasCurrentOffset = _NbsSffDiagsBiasCurrentOffset_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 54),
    _NbsSffDiagsBiasCurrentOffset_Type()
)
nbsSffDiagsBiasCurrentOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsBiasCurrentOffset.setStatus("current")


class _NbsSffDiagsTxPowerSlope_Type(DisplayString):
    """Custom type nbsSffDiagsTxPowerSlope based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsTxPowerSlope_Type.__name__ = "DisplayString"
_NbsSffDiagsTxPowerSlope_Object = MibTableColumn
nbsSffDiagsTxPowerSlope = _NbsSffDiagsTxPowerSlope_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 55),
    _NbsSffDiagsTxPowerSlope_Type()
)
nbsSffDiagsTxPowerSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxPowerSlope.setStatus("current")
_NbsSffDiagsTxPowerOffset_Type = Integer32
_NbsSffDiagsTxPowerOffset_Object = MibTableColumn
nbsSffDiagsTxPowerOffset = _NbsSffDiagsTxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 56),
    _NbsSffDiagsTxPowerOffset_Type()
)
nbsSffDiagsTxPowerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTxPowerOffset.setStatus("current")


class _NbsSffDiagsTemperatureSlope_Type(DisplayString):
    """Custom type nbsSffDiagsTemperatureSlope based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsTemperatureSlope_Type.__name__ = "DisplayString"
_NbsSffDiagsTemperatureSlope_Object = MibTableColumn
nbsSffDiagsTemperatureSlope = _NbsSffDiagsTemperatureSlope_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 57),
    _NbsSffDiagsTemperatureSlope_Type()
)
nbsSffDiagsTemperatureSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTemperatureSlope.setStatus("current")
_NbsSffDiagsTemperatureOffset_Type = Integer32
_NbsSffDiagsTemperatureOffset_Object = MibTableColumn
nbsSffDiagsTemperatureOffset = _NbsSffDiagsTemperatureOffset_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 58),
    _NbsSffDiagsTemperatureOffset_Type()
)
nbsSffDiagsTemperatureOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsTemperatureOffset.setStatus("current")


class _NbsSffDiagsVoltageSlope_Type(DisplayString):
    """Custom type nbsSffDiagsVoltageSlope based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsSffDiagsVoltageSlope_Type.__name__ = "DisplayString"
_NbsSffDiagsVoltageSlope_Object = MibTableColumn
nbsSffDiagsVoltageSlope = _NbsSffDiagsVoltageSlope_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 59),
    _NbsSffDiagsVoltageSlope_Type()
)
nbsSffDiagsVoltageSlope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsVoltageSlope.setStatus("current")
_NbsSffDiagsVoltageOffset_Type = Integer32
_NbsSffDiagsVoltageOffset_Object = MibTableColumn
nbsSffDiagsVoltageOffset = _NbsSffDiagsVoltageOffset_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 60),
    _NbsSffDiagsVoltageOffset_Type()
)
nbsSffDiagsVoltageOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsVoltageOffset.setStatus("current")


class _NbsSffDiagsPowerLevelSelect_Type(Integer32):
    """Custom type nbsSffDiagsPowerLevelSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NbsSffDiagsPowerLevelSelect_Type.__name__ = "Integer32"
_NbsSffDiagsPowerLevelSelect_Object = MibTableColumn
nbsSffDiagsPowerLevelSelect = _NbsSffDiagsPowerLevelSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 61),
    _NbsSffDiagsPowerLevelSelect_Type()
)
nbsSffDiagsPowerLevelSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsPowerLevelSelect.setStatus("current")


class _NbsSffDiagsPowerLevelOpState_Type(Integer32):
    """Custom type nbsSffDiagsPowerLevelOpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NbsSffDiagsPowerLevelOpState_Type.__name__ = "Integer32"
_NbsSffDiagsPowerLevelOpState_Object = MibTableColumn
nbsSffDiagsPowerLevelOpState = _NbsSffDiagsPowerLevelOpState_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 62),
    _NbsSffDiagsPowerLevelOpState_Type()
)
nbsSffDiagsPowerLevelOpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsPowerLevelOpState.setStatus("current")


class _NbsSffDiagsSoftRSSelect_Type(Integer32):
    """Custom type nbsSffDiagsSoftRSSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_NbsSffDiagsSoftRSSelect_Type.__name__ = "Integer32"
_NbsSffDiagsSoftRSSelect_Object = MibTableColumn
nbsSffDiagsSoftRSSelect = _NbsSffDiagsSoftRSSelect_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 3, 1, 1, 63),
    _NbsSffDiagsSoftRSSelect_Type()
)
nbsSffDiagsSoftRSSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffDiagsSoftRSSelect.setStatus("current")
_NbsSffMsxGrp_ObjectIdentity = ObjectIdentity
nbsSffMsxGrp = _NbsSffMsxGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 4)
)
if mibBuilder.loadTexts:
    nbsSffMsxGrp.setStatus("current")
_NbsSffMsxTableSize_Type = Unsigned32
_NbsSffMsxTableSize_Object = MibScalar
nbsSffMsxTableSize = _NbsSffMsxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 1),
    _NbsSffMsxTableSize_Type()
)
nbsSffMsxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsxTableSize.setStatus("current")
_NbsSffMsxTable_Object = MibTable
nbsSffMsxTable = _NbsSffMsxTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2)
)
if mibBuilder.loadTexts:
    nbsSffMsxTable.setStatus("current")
_NbsSffMsxEntry_Object = MibTableRow
nbsSffMsxEntry = _NbsSffMsxEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2, 1)
)
nbsSffMsxEntry.setIndexNames(
    (0, "NBS-SFF-MIB", "nbsSffMsxPhysicalIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSffMsxEntry.setStatus("current")
_NbsSffMsxPhysicalIfIndex_Type = Integer32
_NbsSffMsxPhysicalIfIndex_Object = MibTableColumn
nbsSffMsxPhysicalIfIndex = _NbsSffMsxPhysicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2, 1, 1),
    _NbsSffMsxPhysicalIfIndex_Type()
)
nbsSffMsxPhysicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSffMsxPhysicalIfIndex.setStatus("current")


class _NbsSffMsxHasSgmiiPhy_Type(Integer32):
    """Custom type nbsSffMsxHasSgmiiPhy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notSupported", 1),
          ("yes", 3))
    )


_NbsSffMsxHasSgmiiPhy_Type.__name__ = "Integer32"
_NbsSffMsxHasSgmiiPhy_Object = MibTableColumn
nbsSffMsxHasSgmiiPhy = _NbsSffMsxHasSgmiiPhy_Object(
    (1, 3, 6, 1, 4, 1, 629, 204, 1, 4, 2, 1, 2),
    _NbsSffMsxHasSgmiiPhy_Type()
)
nbsSffMsxHasSgmiiPhy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsSffMsxHasSgmiiPhy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-SFF-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "nbsSffMib": nbsSffMib,
       "nbsSffObjects": nbsSffObjects,
       "nbsSffMsaGrp": nbsSffMsaGrp,
       "nbsSffMsaTable": nbsSffMsaTable,
       "nbsSffMsaEntry": nbsSffMsaEntry,
       "nbsSffMsaPhysicalIfIndex": nbsSffMsaPhysicalIfIndex,
       "nbsSffMsaIdentifier": nbsSffMsaIdentifier,
       "nbsSffMsaExtIdentifier": nbsSffMsaExtIdentifier,
       "nbsSffMsaOpticalConnector": nbsSffMsaOpticalConnector,
       "nbsSffMsaTransceiverCodes": nbsSffMsaTransceiverCodes,
       "nbsSffMsaSerialEncoding": nbsSffMsaSerialEncoding,
       "nbsSffMsaNominalBitRate": nbsSffMsaNominalBitRate,
       "nbsSffMsaLinkLengthSmfKm": nbsSffMsaLinkLengthSmfKm,
       "nbsSffMsaLinkLengthSmf100m": nbsSffMsaLinkLengthSmf100m,
       "nbsSffMsaLinkLengthMmf10m": nbsSffMsaLinkLengthMmf10m,
       "nbsSffMsaLinkLength625Mmf10m": nbsSffMsaLinkLength625Mmf10m,
       "nbsSffMsaCopperLinkLength": nbsSffMsaCopperLinkLength,
       "nbsSffMsaVendorName": nbsSffMsaVendorName,
       "nbsSffMsaVendorOUI": nbsSffMsaVendorOUI,
       "nbsSffMsaVendorPartNumber": nbsSffMsaVendorPartNumber,
       "nbsSffMsaVendorRevision": nbsSffMsaVendorRevision,
       "nbsSffMsaBaseChecksumMatch": nbsSffMsaBaseChecksumMatch,
       "nbsSffMsaLossOfSignalImplemented": nbsSffMsaLossOfSignalImplemented,
       "nbsSffMsaLossOfSignalInverted": nbsSffMsaLossOfSignalInverted,
       "nbsSffMsaTxFault": nbsSffMsaTxFault,
       "nbsSffMsaTxDisable": nbsSffMsaTxDisable,
       "nbsSffMsaRateSelectImplemented": nbsSffMsaRateSelectImplemented,
       "nbsSffMsaMaxBitRate": nbsSffMsaMaxBitRate,
       "nbsSffMsaMinBitRate": nbsSffMsaMinBitRate,
       "nbsSffMsaVendorSerialNumber": nbsSffMsaVendorSerialNumber,
       "nbsSffMsaVendorDateCode": nbsSffMsaVendorDateCode,
       "nbsSffMsaExtChecksumMatch": nbsSffMsaExtChecksumMatch,
       "nbsSffWdmGrp": nbsSffWdmGrp,
       "nbsSffWdmTable": nbsSffWdmTable,
       "nbsSffWdmEntry": nbsSffWdmEntry,
       "nbsSffWdmClassOfPower": nbsSffWdmClassOfPower,
       "nbsSffWdmClassOfTemperature": nbsSffWdmClassOfTemperature,
       "nbsSffWdmClassOfWdm": nbsSffWdmClassOfWdm,
       "nbsSffWdmOpticalReach": nbsSffWdmOpticalReach,
       "nbsSffWdmMaxCaseTemperature": nbsSffWdmMaxCaseTemperature,
       "nbsSffWdmMinCaseTemperature": nbsSffWdmMinCaseTemperature,
       "nbsSffWdmMaxSupplyCurrent": nbsSffWdmMaxSupplyCurrent,
       "nbsSffWdmNumberOfChannels": nbsSffWdmNumberOfChannels,
       "nbsSffWdmChannelSpacing": nbsSffWdmChannelSpacing,
       "nbsSffWdmVariableDecisionThreshold": nbsSffWdmVariableDecisionThreshold,
       "nbsSffWdmWavelengthMonitorType": nbsSffWdmWavelengthMonitorType,
       "nbsSffWdmExtTransmitPowerType": nbsSffWdmExtTransmitPowerType,
       "nbsSffWdmVariableOpticalAttenuator": nbsSffWdmVariableOpticalAttenuator,
       "nbsSffWdmPilotToneFunctionality": nbsSffWdmPilotToneFunctionality,
       "nbsSffWdmOptionalInterruptPin": nbsSffWdmOptionalInterruptPin,
       "nbsSffWdmLaserWavelength": nbsSffWdmLaserWavelength,
       "nbsSffDiagnosticsGrp": nbsSffDiagnosticsGrp,
       "nbsSffDiagsTable": nbsSffDiagsTable,
       "nbsSffDiagsEntry": nbsSffDiagsEntry,
       "nbsSffDiagsRateIdentifier": nbsSffDiagsRateIdentifier,
       "nbsSffDiagsLinkLengthOm3": nbsSffDiagsLinkLengthOm3,
       "nbsSffDiagsLaserWavelength": nbsSffDiagsLaserWavelength,
       "nbsSffDiagsLROutputImplemented": nbsSffDiagsLROutputImplemented,
       "nbsSffDiagsPowerLevelDeclaration": nbsSffDiagsPowerLevelDeclaration,
       "nbsSffDiagsCooledTranDeclaration": nbsSffDiagsCooledTranDeclaration,
       "nbsSffDiagsAddressChangeRequired": nbsSffDiagsAddressChangeRequired,
       "nbsSffDiagsPowerMeasurementType": nbsSffDiagsPowerMeasurementType,
       "nbsSffDiagsExternallyCalibrated": nbsSffDiagsExternallyCalibrated,
       "nbsSffDiagsInternallyCalibrated": nbsSffDiagsInternallyCalibrated,
       "nbsSffDiagsDDMonitoringImplemented": nbsSffDiagsDDMonitoringImplemented,
       "nbsSffDiagsOptRateSelectControl": nbsSffDiagsOptRateSelectControl,
       "nbsSffDiagsOptAppSelectControl": nbsSffDiagsOptAppSelectControl,
       "nbsSffDiagsOptSoftRSControlMon": nbsSffDiagsOptSoftRSControlMon,
       "nbsSffDiagsOptSoftRxLoSMonitoring": nbsSffDiagsOptSoftRxLoSMonitoring,
       "nbsSffDiagsOptSoftTxFaultMonitoring": nbsSffDiagsOptSoftTxFaultMonitoring,
       "nbsSffDiagsOptSoftTxDisable": nbsSffDiagsOptSoftTxDisable,
       "nbsSffDiagsOptAlarmWarningFlags": nbsSffDiagsOptAlarmWarningFlags,
       "nbsSffDiags8472Compliance": nbsSffDiags8472Compliance,
       "nbsSffDiagsTemperature": nbsSffDiagsTemperature,
       "nbsSffDiagsTempLowAlarm": nbsSffDiagsTempLowAlarm,
       "nbsSffDiagsTempLowWarn": nbsSffDiagsTempLowWarn,
       "nbsSffDiagsTempHighWarn": nbsSffDiagsTempHighWarn,
       "nbsSffDiagsTempHighAlarm": nbsSffDiagsTempHighAlarm,
       "nbsSffDiagsVoltage": nbsSffDiagsVoltage,
       "nbsSffDiagsVoltLowAlarm": nbsSffDiagsVoltLowAlarm,
       "nbsSffDiagsVoltLowWarn": nbsSffDiagsVoltLowWarn,
       "nbsSffDiagsVoltHighWarn": nbsSffDiagsVoltHighWarn,
       "nbsSffDiagsVoltHighAlarm": nbsSffDiagsVoltHighAlarm,
       "nbsSffDiagsBiasCurrent": nbsSffDiagsBiasCurrent,
       "nbsSffDiagsBiasLowAlarm": nbsSffDiagsBiasLowAlarm,
       "nbsSffDiagsBiasLowWarn": nbsSffDiagsBiasLowWarn,
       "nbsSffDiagsBiasHighWarn": nbsSffDiagsBiasHighWarn,
       "nbsSffDiagsBiasHighAlarm": nbsSffDiagsBiasHighAlarm,
       "nbsSffDiagsTxPower": nbsSffDiagsTxPower,
       "nbsSffDiagsTxPowerLowAlarm": nbsSffDiagsTxPowerLowAlarm,
       "nbsSffDiagsTxPowerLowWarn": nbsSffDiagsTxPowerLowWarn,
       "nbsSffDiagsTxPowerHighWarn": nbsSffDiagsTxPowerHighWarn,
       "nbsSffDiagsTxPowerHighAlarm": nbsSffDiagsTxPowerHighAlarm,
       "nbsSffDiagsRxPower": nbsSffDiagsRxPower,
       "nbsSffDiagsRxPowerLowAlarm": nbsSffDiagsRxPowerLowAlarm,
       "nbsSffDiagsRxPowerLowWarn": nbsSffDiagsRxPowerLowWarn,
       "nbsSffDiagsRxPowerHighWarn": nbsSffDiagsRxPowerHighWarn,
       "nbsSffDiagsRxPowerHighAlarm": nbsSffDiagsRxPowerHighAlarm,
       "nbsSffDiagsDataReadyBarState": nbsSffDiagsDataReadyBarState,
       "nbsSffDiagsRxLosState": nbsSffDiagsRxLosState,
       "nbsSffDiagsTxFaultState": nbsSffDiagsTxFaultState,
       "nbsSffDiagsSoftRateSelect": nbsSffDiagsSoftRateSelect,
       "nbsSffDiagsRateSelectState0": nbsSffDiagsRateSelectState0,
       "nbsSffDiagsRS1State": nbsSffDiagsRS1State,
       "nbsSffDiagsSoftTxDisableSelect": nbsSffDiagsSoftTxDisableSelect,
       "nbsSffDiagsTxDisableState": nbsSffDiagsTxDisableState,
       "nbsSffDiagsBiasCurrentSlope": nbsSffDiagsBiasCurrentSlope,
       "nbsSffDiagsBiasCurrentOffset": nbsSffDiagsBiasCurrentOffset,
       "nbsSffDiagsTxPowerSlope": nbsSffDiagsTxPowerSlope,
       "nbsSffDiagsTxPowerOffset": nbsSffDiagsTxPowerOffset,
       "nbsSffDiagsTemperatureSlope": nbsSffDiagsTemperatureSlope,
       "nbsSffDiagsTemperatureOffset": nbsSffDiagsTemperatureOffset,
       "nbsSffDiagsVoltageSlope": nbsSffDiagsVoltageSlope,
       "nbsSffDiagsVoltageOffset": nbsSffDiagsVoltageOffset,
       "nbsSffDiagsPowerLevelSelect": nbsSffDiagsPowerLevelSelect,
       "nbsSffDiagsPowerLevelOpState": nbsSffDiagsPowerLevelOpState,
       "nbsSffDiagsSoftRSSelect": nbsSffDiagsSoftRSSelect,
       "nbsSffMsxGrp": nbsSffMsxGrp,
       "nbsSffMsxTableSize": nbsSffMsxTableSize,
       "nbsSffMsxTable": nbsSffMsxTable,
       "nbsSffMsxEntry": nbsSffMsxEntry,
       "nbsSffMsxPhysicalIfIndex": nbsSffMsxPhysicalIfIndex,
       "nbsSffMsxHasSgmiiPhy": nbsSffMsxHasSgmiiPhy}
)
