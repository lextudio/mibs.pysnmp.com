# SNMP MIB module (NBS-OSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-OSA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:55 2024
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

(ifAlias,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias")

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

nbsOsaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 207)
)


# Types definitions



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsOsaPortGrp_ObjectIdentity = ObjectIdentity
nbsOsaPortGrp = _NbsOsaPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 207, 1)
)
if mibBuilder.loadTexts:
    nbsOsaPortGrp.setStatus("current")
_NbsOsaPortTableSize_Type = Unsigned32
_NbsOsaPortTableSize_Object = MibScalar
nbsOsaPortTableSize = _NbsOsaPortTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 1, 1),
    _NbsOsaPortTableSize_Type()
)
nbsOsaPortTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaPortTableSize.setStatus("current")
_NbsOsaPortTable_Object = MibTable
nbsOsaPortTable = _NbsOsaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 1, 2)
)
if mibBuilder.loadTexts:
    nbsOsaPortTable.setStatus("current")
_NbsOsaPortEntry_Object = MibTableRow
nbsOsaPortEntry = _NbsOsaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1)
)
nbsOsaPortEntry.setIndexNames(
    (0, "NBS-OSA-MIB", "nbsOsaPortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsOsaPortEntry.setStatus("current")
_NbsOsaPortIfIndex_Type = InterfaceIndex
_NbsOsaPortIfIndex_Object = MibTableColumn
nbsOsaPortIfIndex = _NbsOsaPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 2),
    _NbsOsaPortIfIndex_Type()
)
nbsOsaPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOsaPortIfIndex.setStatus("current")


class _NbsOsaPortAttenuation_Type(Integer32):
    """Custom type nbsOsaPortAttenuation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100000, 100000),
    )


_NbsOsaPortAttenuation_Type.__name__ = "Integer32"
_NbsOsaPortAttenuation_Object = MibTableColumn
nbsOsaPortAttenuation = _NbsOsaPortAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 3),
    _NbsOsaPortAttenuation_Type()
)
nbsOsaPortAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOsaPortAttenuation.setStatus("current")


class _NbsOsaPortChannels_Type(Integer32):
    """Custom type nbsOsaPortChannels based on Integer32"""
    defaultValue = 0


_NbsOsaPortChannels_Object = MibTableColumn
nbsOsaPortChannels = _NbsOsaPortChannels_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 1, 2, 1, 4),
    _NbsOsaPortChannels_Type()
)
nbsOsaPortChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaPortChannels.setStatus("current")
_NbsOsaSpectrumGrp_ObjectIdentity = ObjectIdentity
nbsOsaSpectrumGrp = _NbsOsaSpectrumGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 207, 2)
)
if mibBuilder.loadTexts:
    nbsOsaSpectrumGrp.setStatus("current")
_NbsOsaSpectrumTableSize_Type = Unsigned32
_NbsOsaSpectrumTableSize_Object = MibScalar
nbsOsaSpectrumTableSize = _NbsOsaSpectrumTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 2, 1),
    _NbsOsaSpectrumTableSize_Type()
)
nbsOsaSpectrumTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaSpectrumTableSize.setStatus("current")
_NbsOsaSpectrumTable_Object = MibTable
nbsOsaSpectrumTable = _NbsOsaSpectrumTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 2, 2)
)
if mibBuilder.loadTexts:
    nbsOsaSpectrumTable.setStatus("current")
_NbsOsaSpectrumEntry_Object = MibTableRow
nbsOsaSpectrumEntry = _NbsOsaSpectrumEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1)
)
nbsOsaSpectrumEntry.setIndexNames(
    (0, "NBS-OSA-MIB", "nbsOsaSpectrumIfIndex"),
    (0, "NBS-OSA-MIB", "nbsOsaSpectrumWavelength"),
)
if mibBuilder.loadTexts:
    nbsOsaSpectrumEntry.setStatus("current")
_NbsOsaSpectrumIfIndex_Type = InterfaceIndex
_NbsOsaSpectrumIfIndex_Object = MibTableColumn
nbsOsaSpectrumIfIndex = _NbsOsaSpectrumIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 2),
    _NbsOsaSpectrumIfIndex_Type()
)
nbsOsaSpectrumIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOsaSpectrumIfIndex.setStatus("current")
_NbsOsaSpectrumWavelength_Type = Integer32
_NbsOsaSpectrumWavelength_Object = MibTableColumn
nbsOsaSpectrumWavelength = _NbsOsaSpectrumWavelength_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 3),
    _NbsOsaSpectrumWavelength_Type()
)
nbsOsaSpectrumWavelength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOsaSpectrumWavelength.setStatus("current")
_NbsOsaSpectrumTimestamp_Type = TimeTicks
_NbsOsaSpectrumTimestamp_Object = MibTableColumn
nbsOsaSpectrumTimestamp = _NbsOsaSpectrumTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 4),
    _NbsOsaSpectrumTimestamp_Type()
)
nbsOsaSpectrumTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaSpectrumTimestamp.setStatus("current")
_NbsOsaSpectrumRxPowerOper_Type = Integer32
_NbsOsaSpectrumRxPowerOper_Object = MibTableColumn
nbsOsaSpectrumRxPowerOper = _NbsOsaSpectrumRxPowerOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 2, 2, 1, 5),
    _NbsOsaSpectrumRxPowerOper_Type()
)
nbsOsaSpectrumRxPowerOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaSpectrumRxPowerOper.setStatus("current")
_NbsOsaChannelGrp_ObjectIdentity = ObjectIdentity
nbsOsaChannelGrp = _NbsOsaChannelGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 207, 3)
)
if mibBuilder.loadTexts:
    nbsOsaChannelGrp.setStatus("current")
_NbsOsaChannelTableSize_Type = Unsigned32
_NbsOsaChannelTableSize_Object = MibScalar
nbsOsaChannelTableSize = _NbsOsaChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 1),
    _NbsOsaChannelTableSize_Type()
)
nbsOsaChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelTableSize.setStatus("current")
_NbsOsaChannelTable_Object = MibTable
nbsOsaChannelTable = _NbsOsaChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2)
)
if mibBuilder.loadTexts:
    nbsOsaChannelTable.setStatus("current")
_NbsOsaChannelEntry_Object = MibTableRow
nbsOsaChannelEntry = _NbsOsaChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1)
)
nbsOsaChannelEntry.setIndexNames(
    (0, "NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
    (0, "NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"),
)
if mibBuilder.loadTexts:
    nbsOsaChannelEntry.setStatus("current")
_NbsOsaChannelIfIndex_Type = InterfaceIndex
_NbsOsaChannelIfIndex_Object = MibTableColumn
nbsOsaChannelIfIndex = _NbsOsaChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 1),
    _NbsOsaChannelIfIndex_Type()
)
nbsOsaChannelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOsaChannelIfIndex.setStatus("current")
_NbsOsaChannelFrequencyNominal_Type = Integer32
_NbsOsaChannelFrequencyNominal_Object = MibTableColumn
nbsOsaChannelFrequencyNominal = _NbsOsaChannelFrequencyNominal_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 2),
    _NbsOsaChannelFrequencyNominal_Type()
)
nbsOsaChannelFrequencyNominal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsOsaChannelFrequencyNominal.setStatus("current")


class _NbsOsaChannelBand_Type(Integer32):
    """Custom type nbsOsaChannelBand based on Integer32"""
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
        *(("cBand", 1),
          ("hBand", 2),
          ("lBand", 3),
          ("qBand", 4))
    )


_NbsOsaChannelBand_Type.__name__ = "Integer32"
_NbsOsaChannelBand_Object = MibTableColumn
nbsOsaChannelBand = _NbsOsaChannelBand_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 3),
    _NbsOsaChannelBand_Type()
)
nbsOsaChannelBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelBand.setStatus("current")
_NbsOsaChannelNumber_Type = Integer32
_NbsOsaChannelNumber_Object = MibTableColumn
nbsOsaChannelNumber = _NbsOsaChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 4),
    _NbsOsaChannelNumber_Type()
)
nbsOsaChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelNumber.setStatus("current")


class _NbsOsaChannelStatus_Type(Integer32):
    """Custom type nbsOsaChannelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_NbsOsaChannelStatus_Type.__name__ = "Integer32"
_NbsOsaChannelStatus_Object = MibTableColumn
nbsOsaChannelStatus = _NbsOsaChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 5),
    _NbsOsaChannelStatus_Type()
)
nbsOsaChannelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelStatus.setStatus("current")
_NbsOsaChannelTimestamp_Type = TimeTicks
_NbsOsaChannelTimestamp_Object = MibTableColumn
nbsOsaChannelTimestamp = _NbsOsaChannelTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 6),
    _NbsOsaChannelTimestamp_Type()
)
nbsOsaChannelTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelTimestamp.setStatus("current")
_NbsOsaChannelFrequencyOper_Type = Integer32
_NbsOsaChannelFrequencyOper_Object = MibTableColumn
nbsOsaChannelFrequencyOper = _NbsOsaChannelFrequencyOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 7),
    _NbsOsaChannelFrequencyOper_Type()
)
nbsOsaChannelFrequencyOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelFrequencyOper.setStatus("current")


class _NbsOsaChannelRxPowerOper_Type(Integer32):
    """Custom type nbsOsaChannelRxPowerOper based on Integer32"""
    defaultValue = -100000


_NbsOsaChannelRxPowerOper_Object = MibTableColumn
nbsOsaChannelRxPowerOper = _NbsOsaChannelRxPowerOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 8),
    _NbsOsaChannelRxPowerOper_Type()
)
nbsOsaChannelRxPowerOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelRxPowerOper.setStatus("current")


class _NbsOsaChannelRxPowerMin_Type(Integer32):
    """Custom type nbsOsaChannelRxPowerMin based on Integer32"""
    defaultValue = 0


_NbsOsaChannelRxPowerMin_Object = MibTableColumn
nbsOsaChannelRxPowerMin = _NbsOsaChannelRxPowerMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 9),
    _NbsOsaChannelRxPowerMin_Type()
)
nbsOsaChannelRxPowerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOsaChannelRxPowerMin.setStatus("current")


class _NbsOsaChannelRxPowerMax_Type(Integer32):
    """Custom type nbsOsaChannelRxPowerMax based on Integer32"""
    defaultValue = 0


_NbsOsaChannelRxPowerMax_Object = MibTableColumn
nbsOsaChannelRxPowerMax = _NbsOsaChannelRxPowerMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 10),
    _NbsOsaChannelRxPowerMax_Type()
)
nbsOsaChannelRxPowerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOsaChannelRxPowerMax.setStatus("current")
_NbsOsaChannelOSNROper_Type = Integer32
_NbsOsaChannelOSNROper_Object = MibTableColumn
nbsOsaChannelOSNROper = _NbsOsaChannelOSNROper_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 11),
    _NbsOsaChannelOSNROper_Type()
)
nbsOsaChannelOSNROper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsOsaChannelOSNROper.setStatus("current")


class _NbsOsaChannelOSNRMin_Type(Integer32):
    """Custom type nbsOsaChannelOSNRMin based on Integer32"""
    defaultValue = 1000


_NbsOsaChannelOSNRMin_Object = MibTableColumn
nbsOsaChannelOSNRMin = _NbsOsaChannelOSNRMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 12),
    _NbsOsaChannelOSNRMin_Type()
)
nbsOsaChannelOSNRMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOsaChannelOSNRMin.setStatus("current")


class _NbsOsaChannelOSNRMax_Type(Integer32):
    """Custom type nbsOsaChannelOSNRMax based on Integer32"""
    defaultValue = 1000


_NbsOsaChannelOSNRMax_Object = MibTableColumn
nbsOsaChannelOSNRMax = _NbsOsaChannelOSNRMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 207, 3, 2, 1, 13),
    _NbsOsaChannelOSNRMax_Type()
)
nbsOsaChannelOSNRMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsOsaChannelOSNRMax.setStatus("current")
_NbsOsaTraps_ObjectIdentity = ObjectIdentity
nbsOsaTraps = _NbsOsaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 207, 4)
)
if mibBuilder.loadTexts:
    nbsOsaTraps.setStatus("current")

# Managed Objects groups


# Notification objects

nbsOsaTrapPortChannelAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 1)
)
nbsOsaTrapPortChannelAdded.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortChannelAdded.setStatus(
        "current"
    )

nbsOsaTrapPortChannelDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 2)
)
nbsOsaTrapPortChannelDropped.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelFrequencyNominal"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortChannelDropped.setStatus(
        "current"
    )

nbsOsaTrapPortRxPowerTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 3)
)
nbsOsaTrapPortRxPowerTooLow.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelRxPowerMin"),
        ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortRxPowerTooLow.setStatus(
        "current"
    )

nbsOsaTrapPortRxPowerOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 4)
)
nbsOsaTrapPortRxPowerOK.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortRxPowerOK.setStatus(
        "current"
    )

nbsOsaTrapPortRxPowerTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 5)
)
nbsOsaTrapPortRxPowerTooHigh.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelRxPowerMax"),
        ("NBS-OSA-MIB", "nbsOsaChannelRxPowerOper"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortRxPowerTooHigh.setStatus(
        "current"
    )

nbsOsaTrapPortOSNRTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 6)
)
nbsOsaTrapPortOSNRTooLow.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelOSNRMin"),
        ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortOSNRTooLow.setStatus(
        "current"
    )

nbsOsaTrapPortOSNROK = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 7)
)
nbsOsaTrapPortOSNROK.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortOSNROK.setStatus(
        "current"
    )

nbsOsaTrapPortOSNRTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 207, 4, 8)
)
nbsOsaTrapPortOSNRTooHigh.setObjects(
      *(("NBS-OSA-MIB", "nbsOsaChannelIfIndex"),
        ("IF-MIB", "ifAlias"),
        ("NBS-OSA-MIB", "nbsOsaChannelBand"),
        ("NBS-OSA-MIB", "nbsOsaChannelNumber"),
        ("NBS-OSA-MIB", "nbsOsaChannelOSNRMax"),
        ("NBS-OSA-MIB", "nbsOsaChannelOSNROper"))
)
if mibBuilder.loadTexts:
    nbsOsaTrapPortOSNRTooHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-OSA-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "nbsOsaMib": nbsOsaMib,
       "nbsOsaPortGrp": nbsOsaPortGrp,
       "nbsOsaPortTableSize": nbsOsaPortTableSize,
       "nbsOsaPortTable": nbsOsaPortTable,
       "nbsOsaPortEntry": nbsOsaPortEntry,
       "nbsOsaPortIfIndex": nbsOsaPortIfIndex,
       "nbsOsaPortAttenuation": nbsOsaPortAttenuation,
       "nbsOsaPortChannels": nbsOsaPortChannels,
       "nbsOsaSpectrumGrp": nbsOsaSpectrumGrp,
       "nbsOsaSpectrumTableSize": nbsOsaSpectrumTableSize,
       "nbsOsaSpectrumTable": nbsOsaSpectrumTable,
       "nbsOsaSpectrumEntry": nbsOsaSpectrumEntry,
       "nbsOsaSpectrumIfIndex": nbsOsaSpectrumIfIndex,
       "nbsOsaSpectrumWavelength": nbsOsaSpectrumWavelength,
       "nbsOsaSpectrumTimestamp": nbsOsaSpectrumTimestamp,
       "nbsOsaSpectrumRxPowerOper": nbsOsaSpectrumRxPowerOper,
       "nbsOsaChannelGrp": nbsOsaChannelGrp,
       "nbsOsaChannelTableSize": nbsOsaChannelTableSize,
       "nbsOsaChannelTable": nbsOsaChannelTable,
       "nbsOsaChannelEntry": nbsOsaChannelEntry,
       "nbsOsaChannelIfIndex": nbsOsaChannelIfIndex,
       "nbsOsaChannelFrequencyNominal": nbsOsaChannelFrequencyNominal,
       "nbsOsaChannelBand": nbsOsaChannelBand,
       "nbsOsaChannelNumber": nbsOsaChannelNumber,
       "nbsOsaChannelStatus": nbsOsaChannelStatus,
       "nbsOsaChannelTimestamp": nbsOsaChannelTimestamp,
       "nbsOsaChannelFrequencyOper": nbsOsaChannelFrequencyOper,
       "nbsOsaChannelRxPowerOper": nbsOsaChannelRxPowerOper,
       "nbsOsaChannelRxPowerMin": nbsOsaChannelRxPowerMin,
       "nbsOsaChannelRxPowerMax": nbsOsaChannelRxPowerMax,
       "nbsOsaChannelOSNROper": nbsOsaChannelOSNROper,
       "nbsOsaChannelOSNRMin": nbsOsaChannelOSNRMin,
       "nbsOsaChannelOSNRMax": nbsOsaChannelOSNRMax,
       "nbsOsaTraps": nbsOsaTraps,
       "nbsOsaTrapPortChannelAdded": nbsOsaTrapPortChannelAdded,
       "nbsOsaTrapPortChannelDropped": nbsOsaTrapPortChannelDropped,
       "nbsOsaTrapPortRxPowerTooLow": nbsOsaTrapPortRxPowerTooLow,
       "nbsOsaTrapPortRxPowerOK": nbsOsaTrapPortRxPowerOK,
       "nbsOsaTrapPortRxPowerTooHigh": nbsOsaTrapPortRxPowerTooHigh,
       "nbsOsaTrapPortOSNRTooLow": nbsOsaTrapPortOSNRTooLow,
       "nbsOsaTrapPortOSNROK": nbsOsaTrapPortOSNROK,
       "nbsOsaTrapPortOSNRTooHigh": nbsOsaTrapPortOSNRTooHigh}
)
