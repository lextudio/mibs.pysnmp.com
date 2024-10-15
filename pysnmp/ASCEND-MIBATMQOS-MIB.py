# SNMP MIB module (ASCEND-MIBATMQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBATMQOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:12 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibatmQosProfile_ObjectIdentity = ObjectIdentity
mibatmQosProfile = _MibatmQosProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 21)
)
_MibatmQosProfileTable_Object = MibTable
mibatmQosProfileTable = _MibatmQosProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1)
)
if mibBuilder.loadTexts:
    mibatmQosProfileTable.setStatus("mandatory")
_MibatmQosProfileEntry_Object = MibTableRow
mibatmQosProfileEntry = _MibatmQosProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1)
)
mibatmQosProfileEntry.setIndexNames(
    (0, "ASCEND-MIBATMQOS-MIB", "atmQosProfile-ContractName"),
)
if mibBuilder.loadTexts:
    mibatmQosProfileEntry.setStatus("mandatory")
_AtmQosProfile_ContractName_Type = DisplayString
_AtmQosProfile_ContractName_Object = MibScalar
atmQosProfile_ContractName = _AtmQosProfile_ContractName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 1),
    _AtmQosProfile_ContractName_Type()
)
atmQosProfile_ContractName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmQosProfile_ContractName.setStatus("mandatory")
_AtmQosProfile_TrafficDescriptorIndex_Type = Integer32
_AtmQosProfile_TrafficDescriptorIndex_Object = MibScalar
atmQosProfile_TrafficDescriptorIndex = _AtmQosProfile_TrafficDescriptorIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 2),
    _AtmQosProfile_TrafficDescriptorIndex_Type()
)
atmQosProfile_TrafficDescriptorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atmQosProfile_TrafficDescriptorIndex.setStatus("mandatory")


class _AtmQosProfile_TrafficDescriptorType_Type(Integer32):
    """Custom type atmQosProfile_TrafficDescriptorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              6,
              7,
              8,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("clpNotaggingScr", 7),
          ("clpNotaggingScrCdvt", 15),
          ("clpTaggingScr", 8),
          ("clpTaggingScrCdvt", 16),
          ("clpTransparentNoscr", 10),
          ("clpTransparentScr", 11),
          ("noclpNoscr", 3),
          ("noclpNoscrCdvt", 13),
          ("noclpScr", 6),
          ("noclpScrCdvt", 14),
          ("noclpTaggingNoscr", 12),
          ("unknownTrafficDescr", 17))
    )


_AtmQosProfile_TrafficDescriptorType_Type.__name__ = "Integer32"
_AtmQosProfile_TrafficDescriptorType_Object = MibScalar
atmQosProfile_TrafficDescriptorType = _AtmQosProfile_TrafficDescriptorType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 3),
    _AtmQosProfile_TrafficDescriptorType_Type()
)
atmQosProfile_TrafficDescriptorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_TrafficDescriptorType.setStatus("mandatory")


class _AtmQosProfile_AtmServiceCategory_Type(Integer32):
    """Custom type atmQosProfile_AtmServiceCategory based on Integer32"""
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
        *(("cbr", 1),
          ("nonRealTimeVbr", 3),
          ("realTimeVbr", 2),
          ("ubr", 4))
    )


_AtmQosProfile_AtmServiceCategory_Type.__name__ = "Integer32"
_AtmQosProfile_AtmServiceCategory_Object = MibScalar
atmQosProfile_AtmServiceCategory = _AtmQosProfile_AtmServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 4),
    _AtmQosProfile_AtmServiceCategory_Type()
)
atmQosProfile_AtmServiceCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_AtmServiceCategory.setStatus("mandatory")
_AtmQosProfile_PeakRateKbitsPerSec_Type = Integer32
_AtmQosProfile_PeakRateKbitsPerSec_Object = MibScalar
atmQosProfile_PeakRateKbitsPerSec = _AtmQosProfile_PeakRateKbitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 6),
    _AtmQosProfile_PeakRateKbitsPerSec_Type()
)
atmQosProfile_PeakRateKbitsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_PeakRateKbitsPerSec.setStatus("mandatory")
_AtmQosProfile_PeakCellRateCellsPerSec_Type = Integer32
_AtmQosProfile_PeakCellRateCellsPerSec_Object = MibScalar
atmQosProfile_PeakCellRateCellsPerSec = _AtmQosProfile_PeakCellRateCellsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 7),
    _AtmQosProfile_PeakCellRateCellsPerSec_Type()
)
atmQosProfile_PeakCellRateCellsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_PeakCellRateCellsPerSec.setStatus("mandatory")
_AtmQosProfile_SustainableRateKbitsPerSec_Type = Integer32
_AtmQosProfile_SustainableRateKbitsPerSec_Object = MibScalar
atmQosProfile_SustainableRateKbitsPerSec = _AtmQosProfile_SustainableRateKbitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 9),
    _AtmQosProfile_SustainableRateKbitsPerSec_Type()
)
atmQosProfile_SustainableRateKbitsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_SustainableRateKbitsPerSec.setStatus("mandatory")
_AtmQosProfile_SustainableCellRateCellsPerSec_Type = Integer32
_AtmQosProfile_SustainableCellRateCellsPerSec_Object = MibScalar
atmQosProfile_SustainableCellRateCellsPerSec = _AtmQosProfile_SustainableCellRateCellsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 10),
    _AtmQosProfile_SustainableCellRateCellsPerSec_Type()
)
atmQosProfile_SustainableCellRateCellsPerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_SustainableCellRateCellsPerSec.setStatus("mandatory")


class _AtmQosProfile_IgnoreCellDelayVariationTolerance_Type(Integer32):
    """Custom type atmQosProfile_IgnoreCellDelayVariationTolerance based on Integer32"""
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


_AtmQosProfile_IgnoreCellDelayVariationTolerance_Type.__name__ = "Integer32"
_AtmQosProfile_IgnoreCellDelayVariationTolerance_Object = MibScalar
atmQosProfile_IgnoreCellDelayVariationTolerance = _AtmQosProfile_IgnoreCellDelayVariationTolerance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 11),
    _AtmQosProfile_IgnoreCellDelayVariationTolerance_Type()
)
atmQosProfile_IgnoreCellDelayVariationTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_IgnoreCellDelayVariationTolerance.setStatus("mandatory")
_AtmQosProfile_CellDelayVariationTolerance_Type = Integer32
_AtmQosProfile_CellDelayVariationTolerance_Object = MibScalar
atmQosProfile_CellDelayVariationTolerance = _AtmQosProfile_CellDelayVariationTolerance_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 12),
    _AtmQosProfile_CellDelayVariationTolerance_Type()
)
atmQosProfile_CellDelayVariationTolerance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_CellDelayVariationTolerance.setStatus("mandatory")


class _AtmQosProfile_IgnoreMaxBurstSize_Type(Integer32):
    """Custom type atmQosProfile_IgnoreMaxBurstSize based on Integer32"""
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


_AtmQosProfile_IgnoreMaxBurstSize_Type.__name__ = "Integer32"
_AtmQosProfile_IgnoreMaxBurstSize_Object = MibScalar
atmQosProfile_IgnoreMaxBurstSize = _AtmQosProfile_IgnoreMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 13),
    _AtmQosProfile_IgnoreMaxBurstSize_Type()
)
atmQosProfile_IgnoreMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_IgnoreMaxBurstSize.setStatus("mandatory")
_AtmQosProfile_MaxBurstSize_Type = Integer32
_AtmQosProfile_MaxBurstSize_Object = MibScalar
atmQosProfile_MaxBurstSize = _AtmQosProfile_MaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 14),
    _AtmQosProfile_MaxBurstSize_Type()
)
atmQosProfile_MaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_MaxBurstSize.setStatus("mandatory")


class _AtmQosProfile_AalType_Type(Integer32):
    """Custom type atmQosProfile_AalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aal0", 1),
          ("aal5", 2),
          ("unspecified", 3))
    )


_AtmQosProfile_AalType_Type.__name__ = "Integer32"
_AtmQosProfile_AalType_Object = MibScalar
atmQosProfile_AalType = _AtmQosProfile_AalType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 16),
    _AtmQosProfile_AalType_Type()
)
atmQosProfile_AalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_AalType.setStatus("mandatory")


class _AtmQosProfile_EarlyPacketDiscard_Type(Integer32):
    """Custom type atmQosProfile_EarlyPacketDiscard based on Integer32"""
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


_AtmQosProfile_EarlyPacketDiscard_Type.__name__ = "Integer32"
_AtmQosProfile_EarlyPacketDiscard_Object = MibScalar
atmQosProfile_EarlyPacketDiscard = _AtmQosProfile_EarlyPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 17),
    _AtmQosProfile_EarlyPacketDiscard_Type()
)
atmQosProfile_EarlyPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_EarlyPacketDiscard.setStatus("mandatory")


class _AtmQosProfile_PartialPacketDiscard_Type(Integer32):
    """Custom type atmQosProfile_PartialPacketDiscard based on Integer32"""
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


_AtmQosProfile_PartialPacketDiscard_Type.__name__ = "Integer32"
_AtmQosProfile_PartialPacketDiscard_Object = MibScalar
atmQosProfile_PartialPacketDiscard = _AtmQosProfile_PartialPacketDiscard_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 18),
    _AtmQosProfile_PartialPacketDiscard_Type()
)
atmQosProfile_PartialPacketDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_PartialPacketDiscard.setStatus("mandatory")


class _AtmQosProfile_TagOrDiscard_Type(Integer32):
    """Custom type atmQosProfile_TagOrDiscard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 2),
          ("tag", 1))
    )


_AtmQosProfile_TagOrDiscard_Type.__name__ = "Integer32"
_AtmQosProfile_TagOrDiscard_Object = MibScalar
atmQosProfile_TagOrDiscard = _AtmQosProfile_TagOrDiscard_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 19),
    _AtmQosProfile_TagOrDiscard_Type()
)
atmQosProfile_TagOrDiscard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_TagOrDiscard.setStatus("mandatory")


class _AtmQosProfile_Action_o_Type(Integer32):
    """Custom type atmQosProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_AtmQosProfile_Action_o_Type.__name__ = "Integer32"
_AtmQosProfile_Action_o_Object = MibScalar
atmQosProfile_Action_o = _AtmQosProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 20),
    _AtmQosProfile_Action_o_Type()
)
atmQosProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_Action_o.setStatus("mandatory")
_AtmQosProfile_SubChannel_Type = Integer32
_AtmQosProfile_SubChannel_Object = MibScalar
atmQosProfile_SubChannel = _AtmQosProfile_SubChannel_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 21, 1, 1, 21),
    _AtmQosProfile_SubChannel_Type()
)
atmQosProfile_SubChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atmQosProfile_SubChannel.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBATMQOS-MIB",
    **{"DisplayString": DisplayString,
       "mibatmQosProfile": mibatmQosProfile,
       "mibatmQosProfileTable": mibatmQosProfileTable,
       "mibatmQosProfileEntry": mibatmQosProfileEntry,
       "atmQosProfile-ContractName": atmQosProfile_ContractName,
       "atmQosProfile-TrafficDescriptorIndex": atmQosProfile_TrafficDescriptorIndex,
       "atmQosProfile-TrafficDescriptorType": atmQosProfile_TrafficDescriptorType,
       "atmQosProfile-AtmServiceCategory": atmQosProfile_AtmServiceCategory,
       "atmQosProfile-PeakRateKbitsPerSec": atmQosProfile_PeakRateKbitsPerSec,
       "atmQosProfile-PeakCellRateCellsPerSec": atmQosProfile_PeakCellRateCellsPerSec,
       "atmQosProfile-SustainableRateKbitsPerSec": atmQosProfile_SustainableRateKbitsPerSec,
       "atmQosProfile-SustainableCellRateCellsPerSec": atmQosProfile_SustainableCellRateCellsPerSec,
       "atmQosProfile-IgnoreCellDelayVariationTolerance": atmQosProfile_IgnoreCellDelayVariationTolerance,
       "atmQosProfile-CellDelayVariationTolerance": atmQosProfile_CellDelayVariationTolerance,
       "atmQosProfile-IgnoreMaxBurstSize": atmQosProfile_IgnoreMaxBurstSize,
       "atmQosProfile-MaxBurstSize": atmQosProfile_MaxBurstSize,
       "atmQosProfile-AalType": atmQosProfile_AalType,
       "atmQosProfile-EarlyPacketDiscard": atmQosProfile_EarlyPacketDiscard,
       "atmQosProfile-PartialPacketDiscard": atmQosProfile_PartialPacketDiscard,
       "atmQosProfile-TagOrDiscard": atmQosProfile_TagOrDiscard,
       "atmQosProfile-Action-o": atmQosProfile_Action_o,
       "atmQosProfile-SubChannel": atmQosProfile_SubChannel}
)
