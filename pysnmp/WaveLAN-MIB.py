# SNMP MIB module (WaveLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WaveLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:30 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Att_2_ObjectIdentity = ObjectIdentity
att_2 = _Att_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74)
)
_Att_mgmt_ObjectIdentity = ObjectIdentity
att_mgmt = _Att_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2)
)
_Wavelan_ObjectIdentity = ObjectIdentity
wavelan = _Wavelan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 21)
)
_WavelanInterface_ObjectIdentity = ObjectIdentity
wavelanInterface = _WavelanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1)
)
_WliNicTable_Object = MibTable
wliNicTable = _WliNicTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1)
)
if mibBuilder.loadTexts:
    wliNicTable.setStatus("mandatory")
_WliNicEntry_Object = MibTableRow
wliNicEntry = _WliNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1)
)
wliNicEntry.setIndexNames(
    (0, "WaveLAN-MIB", "wliNicIndex"),
)
if mibBuilder.loadTexts:
    wliNicEntry.setStatus("mandatory")
_WliNicIndex_Type = Integer32
_WliNicIndex_Object = MibTableColumn
wliNicIndex = _WliNicIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 1),
    _WliNicIndex_Type()
)
wliNicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliNicIndex.setStatus("mandatory")


class _WliNicBusType_Type(Integer32):
    """Custom type wliNicBusType based on Integer32"""
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
        *(("isaBus", 2),
          ("mcBus", 3),
          ("pcmcia2Bus", 4),
          ("wavepointBus", 5),
          ("xtBus", 1))
    )


_WliNicBusType_Type.__name__ = "Integer32"
_WliNicBusType_Object = MibTableColumn
wliNicBusType = _WliNicBusType_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 2),
    _WliNicBusType_Type()
)
wliNicBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliNicBusType.setStatus("mandatory")


class _WliNicSlot_Type(Integer32):
    """Custom type wliNicSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_WliNicSlot_Type.__name__ = "Integer32"
_WliNicSlot_Object = MibTableColumn
wliNicSlot = _WliNicSlot_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 3),
    _WliNicSlot_Type()
)
wliNicSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliNicSlot.setStatus("mandatory")


class _WliNicIrq_Type(Integer32):
    """Custom type wliNicIrq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WliNicIrq_Type.__name__ = "Integer32"
_WliNicIrq_Object = MibTableColumn
wliNicIrq = _WliNicIrq_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 4),
    _WliNicIrq_Type()
)
wliNicIrq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliNicIrq.setStatus("mandatory")
_WliNicError_Type = Counter32
_WliNicError_Object = MibTableColumn
wliNicError = _WliNicError_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 5),
    _WliNicError_Type()
)
wliNicError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliNicError.setStatus("mandatory")
_WliNicOutOfRxResource_Type = Counter32
_WliNicOutOfRxResource_Object = MibTableColumn
wliNicOutOfRxResource = _WliNicOutOfRxResource_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 1, 1, 6),
    _WliNicOutOfRxResource_Type()
)
wliNicOutOfRxResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliNicOutOfRxResource.setStatus("mandatory")
_WliPhyTable_Object = MibTable
wliPhyTable = _WliPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    wliPhyTable.setStatus("mandatory")
_WliPhyEntry_Object = MibTableRow
wliPhyEntry = _WliPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1)
)
wliPhyEntry.setIndexNames(
    (0, "WaveLAN-MIB", "wliPhyIndex"),
)
if mibBuilder.loadTexts:
    wliPhyEntry.setStatus("mandatory")
_WliPhyIndex_Type = Integer32
_WliPhyIndex_Object = MibTableColumn
wliPhyIndex = _WliPhyIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 1),
    _WliPhyIndex_Type()
)
wliPhyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyIndex.setStatus("mandatory")


class _WliPhyDsp_Type(Integer32):
    """Custom type wliPhyDsp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("daedalus", 2),
          ("icarus", 1))
    )


_WliPhyDsp_Type.__name__ = "Integer32"
_WliPhyDsp_Object = MibTableColumn
wliPhyDsp = _WliPhyDsp_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 2),
    _WliPhyDsp_Type()
)
wliPhyDsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyDsp.setStatus("mandatory")


class _WliPhyFrequency_Type(Integer32):
    """Custom type wliPhyFrequency based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("f2412Mhz", 6),
          ("f2422Mhz", 7),
          ("f2425Mhz", 2),
          ("f2430Mhz", 5),
          ("f2432Mhz", 8),
          ("f2442Mhz", 9),
          ("f2452Mhz", 10),
          ("f2460Mhz", 3),
          ("f2462Mhz", 11),
          ("f2484Mhz", 4),
          ("f915Mhz", 1))
    )


_WliPhyFrequency_Type.__name__ = "Integer32"
_WliPhyFrequency_Object = MibTableColumn
wliPhyFrequency = _WliPhyFrequency_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 3),
    _WliPhyFrequency_Type()
)
wliPhyFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyFrequency.setStatus("mandatory")


class _WliPhyNwid_Type(OctetString):
    """Custom type wliPhyNwid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WliPhyNwid_Type.__name__ = "OctetString"
_WliPhyNwid_Object = MibTableColumn
wliPhyNwid = _WliPhyNwid_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 4),
    _WliPhyNwid_Type()
)
wliPhyNwid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wliPhyNwid.setStatus("mandatory")


class _WliPhyRfSilenceLevel_Type(Integer32):
    """Custom type wliPhyRfSilenceLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 36),
    )


_WliPhyRfSilenceLevel_Type.__name__ = "Integer32"
_WliPhyRfSilenceLevel_Object = MibTableColumn
wliPhyRfSilenceLevel = _WliPhyRfSilenceLevel_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 5),
    _WliPhyRfSilenceLevel_Type()
)
wliPhyRfSilenceLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyRfSilenceLevel.setStatus("mandatory")
_WliPhyOwnNwid_Type = Counter32
_WliPhyOwnNwid_Object = MibTableColumn
wliPhyOwnNwid = _WliPhyOwnNwid_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 6),
    _WliPhyOwnNwid_Type()
)
wliPhyOwnNwid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyOwnNwid.setStatus("mandatory")
_WliPhyOtherNwid_Type = Counter32
_WliPhyOtherNwid_Object = MibTableColumn
wliPhyOtherNwid = _WliPhyOtherNwid_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 7),
    _WliPhyOtherNwid_Type()
)
wliPhyOtherNwid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyOtherNwid.setStatus("mandatory")
_WliPhyLowSnr_Type = Counter32
_WliPhyLowSnr_Object = MibTableColumn
wliPhyLowSnr = _WliPhyLowSnr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 8),
    _WliPhyLowSnr_Type()
)
wliPhyLowSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyLowSnr.setStatus("mandatory")
_WliPhyGoodSnr_Type = Counter32
_WliPhyGoodSnr_Object = MibTableColumn
wliPhyGoodSnr = _WliPhyGoodSnr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 9),
    _WliPhyGoodSnr_Type()
)
wliPhyGoodSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyGoodSnr.setStatus("mandatory")
_WliPhyExcellentSnr_Type = Counter32
_WliPhyExcellentSnr_Object = MibTableColumn
wliPhyExcellentSnr = _WliPhyExcellentSnr_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 2, 1, 10),
    _WliPhyExcellentSnr_Type()
)
wliPhyExcellentSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliPhyExcellentSnr.setStatus("mandatory")
_WliMacTable_Object = MibTable
wliMacTable = _WliMacTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3)
)
if mibBuilder.loadTexts:
    wliMacTable.setStatus("mandatory")
_WliMacEntry_Object = MibTableRow
wliMacEntry = _WliMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1)
)
wliMacEntry.setIndexNames(
    (0, "WaveLAN-MIB", "wliMacIndex"),
)
if mibBuilder.loadTexts:
    wliMacEntry.setStatus("mandatory")
_WliMacIndex_Type = Integer32
_WliMacIndex_Object = MibTableColumn
wliMacIndex = _WliMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 1),
    _WliMacIndex_Type()
)
wliMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacIndex.setStatus("mandatory")


class _WliMacAddressSelect_Type(Integer32):
    """Custom type wliMacAddressSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("universal", 1))
    )


_WliMacAddressSelect_Type.__name__ = "Integer32"
_WliMacAddressSelect_Object = MibTableColumn
wliMacAddressSelect = _WliMacAddressSelect_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 2),
    _WliMacAddressSelect_Type()
)
wliMacAddressSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacAddressSelect.setStatus("mandatory")
_WliMacCaDefers_Type = Counter32
_WliMacCaDefers_Object = MibTableColumn
wliMacCaDefers = _WliMacCaDefers_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 3),
    _WliMacCaDefers_Type()
)
wliMacCaDefers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacCaDefers.setStatus("mandatory")
_WliMacDeferredTransmissions_Type = Counter32
_WliMacDeferredTransmissions_Object = MibTableColumn
wliMacDeferredTransmissions = _WliMacDeferredTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 4),
    _WliMacDeferredTransmissions_Type()
)
wliMacDeferredTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacDeferredTransmissions.setStatus("mandatory")
_WliMacFCSErrors_Type = Counter32
_WliMacFCSErrors_Object = MibTableColumn
wliMacFCSErrors = _WliMacFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 5),
    _WliMacFCSErrors_Type()
)
wliMacFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacFCSErrors.setStatus("mandatory")
_WliMacFrameTooLongs_Type = Counter32
_WliMacFrameTooLongs_Object = MibTableColumn
wliMacFrameTooLongs = _WliMacFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 6),
    _WliMacFrameTooLongs_Type()
)
wliMacFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacFrameTooLongs.setStatus("mandatory")
_WliMacFrameTooShorts_Type = Counter32
_WliMacFrameTooShorts_Object = MibTableColumn
wliMacFrameTooShorts = _WliMacFrameTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 7),
    _WliMacFrameTooShorts_Type()
)
wliMacFrameTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacFrameTooShorts.setStatus("mandatory")
_WliMacDeferLimits_Type = Counter32
_WliMacDeferLimits_Object = MibTableColumn
wliMacDeferLimits = _WliMacDeferLimits_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 3, 1, 8),
    _WliMacDeferLimits_Type()
)
wliMacDeferLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMacDeferLimits.setStatus("mandatory")
_WliDriverTable_Object = MibTable
wliDriverTable = _WliDriverTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    wliDriverTable.setStatus("mandatory")
_WliDriverEntry_Object = MibTableRow
wliDriverEntry = _WliDriverEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1)
)
wliDriverEntry.setIndexNames(
    (0, "WaveLAN-MIB", "wliDriverIndex"),
)
if mibBuilder.loadTexts:
    wliDriverEntry.setStatus("mandatory")
_WliDriverIndex_Type = Integer32
_WliDriverIndex_Object = MibTableColumn
wliDriverIndex = _WliDriverIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1, 1),
    _WliDriverIndex_Type()
)
wliDriverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliDriverIndex.setStatus("mandatory")


class _WliDriverName_Type(DisplayString):
    """Custom type wliDriverName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_WliDriverName_Type.__name__ = "DisplayString"
_WliDriverName_Object = MibTableColumn
wliDriverName = _WliDriverName_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1, 2),
    _WliDriverName_Type()
)
wliDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliDriverName.setStatus("mandatory")


class _WliDriverVersion_Type(DisplayString):
    """Custom type wliDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_WliDriverVersion_Type.__name__ = "DisplayString"
_WliDriverVersion_Object = MibTableColumn
wliDriverVersion = _WliDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 4, 1, 3),
    _WliDriverVersion_Type()
)
wliDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliDriverVersion.setStatus("mandatory")
_WliEncTable_Object = MibTable
wliEncTable = _WliEncTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5)
)
if mibBuilder.loadTexts:
    wliEncTable.setStatus("mandatory")
_WliEncEntry_Object = MibTableRow
wliEncEntry = _WliEncEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1)
)
wliEncEntry.setIndexNames(
    (0, "WaveLAN-MIB", "wliEncIndex"),
)
if mibBuilder.loadTexts:
    wliEncEntry.setStatus("mandatory")
_WliEncIndex_Type = Integer32
_WliEncIndex_Object = MibTableColumn
wliEncIndex = _WliEncIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 1),
    _WliEncIndex_Type()
)
wliEncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliEncIndex.setStatus("mandatory")


class _WliEncInstalled_Type(Integer32):
    """Custom type wliEncInstalled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("des", 2),
          ("none", 1))
    )


_WliEncInstalled_Type.__name__ = "Integer32"
_WliEncInstalled_Object = MibTableColumn
wliEncInstalled = _WliEncInstalled_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 2),
    _WliEncInstalled_Type()
)
wliEncInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliEncInstalled.setStatus("mandatory")


class _WliEncSelect_Type(Integer32):
    """Custom type wliEncSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WliEncSelect_Type.__name__ = "Integer32"
_WliEncSelect_Object = MibTableColumn
wliEncSelect = _WliEncSelect_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 3),
    _WliEncSelect_Type()
)
wliEncSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliEncSelect.setStatus("mandatory")


class _WliEncKey_Type(OctetString):
    """Custom type wliEncKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_WliEncKey_Type.__name__ = "OctetString"
_WliEncKey_Object = MibTableColumn
wliEncKey = _WliEncKey_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 5, 1, 4),
    _WliEncKey_Type()
)
wliEncKey.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    wliEncKey.setStatus("mandatory")
_WliMcastDelayTable_Object = MibTable
wliMcastDelayTable = _WliMcastDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6)
)
if mibBuilder.loadTexts:
    wliMcastDelayTable.setStatus("mandatory")
_WliMcastDelayEntry_Object = MibTableRow
wliMcastDelayEntry = _WliMcastDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1)
)
wliMcastDelayEntry.setIndexNames(
    (0, "WaveLAN-MIB", "wliMcastDelayIndex"),
)
if mibBuilder.loadTexts:
    wliMcastDelayEntry.setStatus("mandatory")
_WliMcastDelayIndex_Type = Integer32
_WliMcastDelayIndex_Object = MibTableColumn
wliMcastDelayIndex = _WliMcastDelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 1),
    _WliMcastDelayIndex_Type()
)
wliMcastDelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wliMcastDelayIndex.setStatus("mandatory")


class _WliMcastNumberOfAps_Type(Integer32):
    """Custom type wliMcastNumberOfAps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WliMcastNumberOfAps_Type.__name__ = "Integer32"
_WliMcastNumberOfAps_Object = MibTableColumn
wliMcastNumberOfAps = _WliMcastNumberOfAps_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 2),
    _WliMcastNumberOfAps_Type()
)
wliMcastNumberOfAps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wliMcastNumberOfAps.setStatus("mandatory")


class _WliMcastApSequenceNumber_Type(Integer32):
    """Custom type wliMcastApSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WliMcastApSequenceNumber_Type.__name__ = "Integer32"
_WliMcastApSequenceNumber_Object = MibTableColumn
wliMcastApSequenceNumber = _WliMcastApSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 3),
    _WliMcastApSequenceNumber_Type()
)
wliMcastApSequenceNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wliMcastApSequenceNumber.setStatus("mandatory")


class _WliMcastRepeatCount_Type(Integer32):
    """Custom type wliMcastRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_WliMcastRepeatCount_Type.__name__ = "Integer32"
_WliMcastRepeatCount_Object = MibTableColumn
wliMcastRepeatCount = _WliMcastRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 74, 2, 21, 1, 6, 1, 4),
    _WliMcastRepeatCount_Type()
)
wliMcastRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wliMcastRepeatCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WaveLAN-MIB",
    **{"att-2": att_2,
       "att-mgmt": att_mgmt,
       "wavelan": wavelan,
       "wavelanInterface": wavelanInterface,
       "wliNicTable": wliNicTable,
       "wliNicEntry": wliNicEntry,
       "wliNicIndex": wliNicIndex,
       "wliNicBusType": wliNicBusType,
       "wliNicSlot": wliNicSlot,
       "wliNicIrq": wliNicIrq,
       "wliNicError": wliNicError,
       "wliNicOutOfRxResource": wliNicOutOfRxResource,
       "wliPhyTable": wliPhyTable,
       "wliPhyEntry": wliPhyEntry,
       "wliPhyIndex": wliPhyIndex,
       "wliPhyDsp": wliPhyDsp,
       "wliPhyFrequency": wliPhyFrequency,
       "wliPhyNwid": wliPhyNwid,
       "wliPhyRfSilenceLevel": wliPhyRfSilenceLevel,
       "wliPhyOwnNwid": wliPhyOwnNwid,
       "wliPhyOtherNwid": wliPhyOtherNwid,
       "wliPhyLowSnr": wliPhyLowSnr,
       "wliPhyGoodSnr": wliPhyGoodSnr,
       "wliPhyExcellentSnr": wliPhyExcellentSnr,
       "wliMacTable": wliMacTable,
       "wliMacEntry": wliMacEntry,
       "wliMacIndex": wliMacIndex,
       "wliMacAddressSelect": wliMacAddressSelect,
       "wliMacCaDefers": wliMacCaDefers,
       "wliMacDeferredTransmissions": wliMacDeferredTransmissions,
       "wliMacFCSErrors": wliMacFCSErrors,
       "wliMacFrameTooLongs": wliMacFrameTooLongs,
       "wliMacFrameTooShorts": wliMacFrameTooShorts,
       "wliMacDeferLimits": wliMacDeferLimits,
       "wliDriverTable": wliDriverTable,
       "wliDriverEntry": wliDriverEntry,
       "wliDriverIndex": wliDriverIndex,
       "wliDriverName": wliDriverName,
       "wliDriverVersion": wliDriverVersion,
       "wliEncTable": wliEncTable,
       "wliEncEntry": wliEncEntry,
       "wliEncIndex": wliEncIndex,
       "wliEncInstalled": wliEncInstalled,
       "wliEncSelect": wliEncSelect,
       "wliEncKey": wliEncKey,
       "wliMcastDelayTable": wliMcastDelayTable,
       "wliMcastDelayEntry": wliMcastDelayEntry,
       "wliMcastDelayIndex": wliMcastDelayIndex,
       "wliMcastNumberOfAps": wliMcastNumberOfAps,
       "wliMcastApSequenceNumber": wliMcastApSequenceNumber,
       "wliMcastRepeatCount": wliMcastRepeatCount}
)
