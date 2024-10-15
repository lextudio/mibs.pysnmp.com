# SNMP MIB module (NBS-SIGLANE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-SIGLANE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:01 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(NbsCmmcChannelBand,) = mibBuilder.importSymbols(
    "NBS-CMMCENUM-MIB",
    "NbsCmmcChannelBand")

(NbsTcMHz,
 NbsTcMicroAmp,
 NbsTcMilliDb,
 NbsTcTemperature,
 nbs) = mibBuilder.importSymbols(
    "NBS-MIB",
    "NbsTcMHz",
    "NbsTcMicroAmp",
    "NbsTcMilliDb",
    "NbsTcTemperature",
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

nbsSigLaneMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsSigLanePortGrp_ObjectIdentity = ObjectIdentity
nbsSigLanePortGrp = _NbsSigLanePortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 10)
)
if mibBuilder.loadTexts:
    nbsSigLanePortGrp.setStatus("current")
_NbsSigLanePortTable_Object = MibTable
nbsSigLanePortTable = _NbsSigLanePortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1)
)
if mibBuilder.loadTexts:
    nbsSigLanePortTable.setStatus("current")
_NbsSigLanePortEntry_Object = MibTableRow
nbsSigLanePortEntry = _NbsSigLanePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1)
)
nbsSigLanePortEntry.setIndexNames(
    (0, "NBS-SIGLANE-MIB", "nbsSigLanePortIfIndex"),
)
if mibBuilder.loadTexts:
    nbsSigLanePortEntry.setStatus("current")
_NbsSigLanePortIfIndex_Type = InterfaceIndex
_NbsSigLanePortIfIndex_Object = MibTableColumn
nbsSigLanePortIfIndex = _NbsSigLanePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 1),
    _NbsSigLanePortIfIndex_Type()
)
nbsSigLanePortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLanePortIfIndex.setStatus("current")


class _NbsSigLanePortFacility_Type(Integer32):
    """Custom type nbsSigLanePortFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 2),
          ("lambda", 3),
          ("other", 1))
    )


_NbsSigLanePortFacility_Type.__name__ = "Integer32"
_NbsSigLanePortFacility_Object = MibTableColumn
nbsSigLanePortFacility = _NbsSigLanePortFacility_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 10),
    _NbsSigLanePortFacility_Type()
)
nbsSigLanePortFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLanePortFacility.setStatus("current")
_NbsSigLanePortLanes_Type = Integer32
_NbsSigLanePortLanes_Object = MibTableColumn
nbsSigLanePortLanes = _NbsSigLanePortLanes_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 10, 1, 1, 20),
    _NbsSigLanePortLanes_Type()
)
nbsSigLanePortLanes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLanePortLanes.setStatus("current")
_NbsSigLaneLaneGrp_ObjectIdentity = ObjectIdentity
nbsSigLaneLaneGrp = _NbsSigLaneLaneGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 20)
)
if mibBuilder.loadTexts:
    nbsSigLaneLaneGrp.setStatus("current")
_NbsSigLaneLaneTable_Object = MibTable
nbsSigLaneLaneTable = _NbsSigLaneLaneTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1)
)
if mibBuilder.loadTexts:
    nbsSigLaneLaneTable.setStatus("current")
_NbsSigLaneLaneEntry_Object = MibTableRow
nbsSigLaneLaneEntry = _NbsSigLaneLaneEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1)
)
nbsSigLaneLaneEntry.setIndexNames(
    (0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIfIndex"),
    (0, "NBS-SIGLANE-MIB", "nbsSigLaneLaneIndex"),
)
if mibBuilder.loadTexts:
    nbsSigLaneLaneEntry.setStatus("current")
_NbsSigLaneLaneIfIndex_Type = InterfaceIndex
_NbsSigLaneLaneIfIndex_Object = MibTableColumn
nbsSigLaneLaneIfIndex = _NbsSigLaneLaneIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 1),
    _NbsSigLaneLaneIfIndex_Type()
)
nbsSigLaneLaneIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneIfIndex.setStatus("current")
_NbsSigLaneLaneIndex_Type = Integer32
_NbsSigLaneLaneIndex_Object = MibTableColumn
nbsSigLaneLaneIndex = _NbsSigLaneLaneIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 2),
    _NbsSigLaneLaneIndex_Type()
)
nbsSigLaneLaneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneIndex.setStatus("current")
_NbsSigLaneLaneFrequency_Type = NbsTcMHz
_NbsSigLaneLaneFrequency_Object = MibTableColumn
nbsSigLaneLaneFrequency = _NbsSigLaneLaneFrequency_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 10),
    _NbsSigLaneLaneFrequency_Type()
)
nbsSigLaneLaneFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneFrequency.setStatus("current")


class _NbsSigLaneLaneWavelengthX_Type(DisplayString):
    """Custom type nbsSigLaneLaneWavelengthX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 8),
    )


_NbsSigLaneLaneWavelengthX_Type.__name__ = "DisplayString"
_NbsSigLaneLaneWavelengthX_Object = MibTableColumn
nbsSigLaneLaneWavelengthX = _NbsSigLaneLaneWavelengthX_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 11),
    _NbsSigLaneLaneWavelengthX_Type()
)
nbsSigLaneLaneWavelengthX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneWavelengthX.setStatus("current")
_NbsSigLaneLaneChannelBand_Type = NbsCmmcChannelBand
_NbsSigLaneLaneChannelBand_Object = MibTableColumn
nbsSigLaneLaneChannelBand = _NbsSigLaneLaneChannelBand_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 12),
    _NbsSigLaneLaneChannelBand_Type()
)
nbsSigLaneLaneChannelBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneChannelBand.setStatus("current")
_NbsSigLaneLaneChannelNumber_Type = Integer32
_NbsSigLaneLaneChannelNumber_Object = MibTableColumn
nbsSigLaneLaneChannelNumber = _NbsSigLaneLaneChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 13),
    _NbsSigLaneLaneChannelNumber_Type()
)
nbsSigLaneLaneChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneChannelNumber.setStatus("current")


class _NbsSigLaneLaneTxPowerLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneTxPowerLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsSigLaneLaneTxPowerLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneTxPowerLevel_Object = MibTableColumn
nbsSigLaneLaneTxPowerLevel = _NbsSigLaneLaneTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 20),
    _NbsSigLaneLaneTxPowerLevel_Type()
)
nbsSigLaneLaneTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneTxPowerLevel.setStatus("current")


class _NbsSigLaneLaneTxPower_Type(NbsTcMilliDb):
    """Custom type nbsSigLaneLaneTxPower based on NbsTcMilliDb"""
    defaultValue = -2147483648


_NbsSigLaneLaneTxPower_Object = MibTableColumn
nbsSigLaneLaneTxPower = _NbsSigLaneLaneTxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 21),
    _NbsSigLaneLaneTxPower_Type()
)
nbsSigLaneLaneTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneTxPower.setStatus("current")


class _NbsSigLaneLaneRxPowerLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneRxPowerLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsSigLaneLaneRxPowerLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneRxPowerLevel_Object = MibTableColumn
nbsSigLaneLaneRxPowerLevel = _NbsSigLaneLaneRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 30),
    _NbsSigLaneLaneRxPowerLevel_Type()
)
nbsSigLaneLaneRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneRxPowerLevel.setStatus("current")


class _NbsSigLaneLaneRxPower_Type(NbsTcMilliDb):
    """Custom type nbsSigLaneLaneRxPower based on NbsTcMilliDb"""
    defaultValue = -2147483648


_NbsSigLaneLaneRxPower_Object = MibTableColumn
nbsSigLaneLaneRxPower = _NbsSigLaneLaneRxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 31),
    _NbsSigLaneLaneRxPower_Type()
)
nbsSigLaneLaneRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneRxPower.setStatus("current")


class _NbsSigLaneLaneBiasAmpsLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneBiasAmpsLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsSigLaneLaneBiasAmpsLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneBiasAmpsLevel_Object = MibTableColumn
nbsSigLaneLaneBiasAmpsLevel = _NbsSigLaneLaneBiasAmpsLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 40),
    _NbsSigLaneLaneBiasAmpsLevel_Type()
)
nbsSigLaneLaneBiasAmpsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneBiasAmpsLevel.setStatus("current")


class _NbsSigLaneLaneBiasAmps_Type(NbsTcMicroAmp):
    """Custom type nbsSigLaneLaneBiasAmps based on NbsTcMicroAmp"""
    defaultValue = -1


_NbsSigLaneLaneBiasAmps_Object = MibTableColumn
nbsSigLaneLaneBiasAmps = _NbsSigLaneLaneBiasAmps_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 41),
    _NbsSigLaneLaneBiasAmps_Type()
)
nbsSigLaneLaneBiasAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneBiasAmps.setStatus("current")


class _NbsSigLaneLaneLaserTempLevel_Type(Integer32):
    """Custom type nbsSigLaneLaneLaserTempLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsSigLaneLaneLaserTempLevel_Type.__name__ = "Integer32"
_NbsSigLaneLaneLaserTempLevel_Object = MibTableColumn
nbsSigLaneLaneLaserTempLevel = _NbsSigLaneLaneLaserTempLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 50),
    _NbsSigLaneLaneLaserTempLevel_Type()
)
nbsSigLaneLaneLaserTempLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneLaserTempLevel.setStatus("current")


class _NbsSigLaneLaneLaserTemp_Type(NbsTcTemperature):
    """Custom type nbsSigLaneLaneLaserTemp based on NbsTcTemperature"""
    defaultValue = -2147483648


_NbsSigLaneLaneLaserTemp_Object = MibTableColumn
nbsSigLaneLaneLaserTemp = _NbsSigLaneLaneLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 629, 236, 20, 1, 1, 51),
    _NbsSigLaneLaneLaserTemp_Type()
)
nbsSigLaneLaneLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsSigLaneLaneLaserTemp.setStatus("current")
_NbsSigLaneTraps_ObjectIdentity = ObjectIdentity
nbsSigLaneTraps = _NbsSigLaneTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 100)
)
if mibBuilder.loadTexts:
    nbsSigLaneTraps.setStatus("current")
_NbsSigLaneTraps0_ObjectIdentity = ObjectIdentity
nbsSigLaneTraps0 = _NbsSigLaneTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 236, 100, 0)
)
if mibBuilder.loadTexts:
    nbsSigLaneTraps0.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-SIGLANE-MIB",
    **{"nbsSigLaneMib": nbsSigLaneMib,
       "nbsSigLanePortGrp": nbsSigLanePortGrp,
       "nbsSigLanePortTable": nbsSigLanePortTable,
       "nbsSigLanePortEntry": nbsSigLanePortEntry,
       "nbsSigLanePortIfIndex": nbsSigLanePortIfIndex,
       "nbsSigLanePortFacility": nbsSigLanePortFacility,
       "nbsSigLanePortLanes": nbsSigLanePortLanes,
       "nbsSigLaneLaneGrp": nbsSigLaneLaneGrp,
       "nbsSigLaneLaneTable": nbsSigLaneLaneTable,
       "nbsSigLaneLaneEntry": nbsSigLaneLaneEntry,
       "nbsSigLaneLaneIfIndex": nbsSigLaneLaneIfIndex,
       "nbsSigLaneLaneIndex": nbsSigLaneLaneIndex,
       "nbsSigLaneLaneFrequency": nbsSigLaneLaneFrequency,
       "nbsSigLaneLaneWavelengthX": nbsSigLaneLaneWavelengthX,
       "nbsSigLaneLaneChannelBand": nbsSigLaneLaneChannelBand,
       "nbsSigLaneLaneChannelNumber": nbsSigLaneLaneChannelNumber,
       "nbsSigLaneLaneTxPowerLevel": nbsSigLaneLaneTxPowerLevel,
       "nbsSigLaneLaneTxPower": nbsSigLaneLaneTxPower,
       "nbsSigLaneLaneRxPowerLevel": nbsSigLaneLaneRxPowerLevel,
       "nbsSigLaneLaneRxPower": nbsSigLaneLaneRxPower,
       "nbsSigLaneLaneBiasAmpsLevel": nbsSigLaneLaneBiasAmpsLevel,
       "nbsSigLaneLaneBiasAmps": nbsSigLaneLaneBiasAmps,
       "nbsSigLaneLaneLaserTempLevel": nbsSigLaneLaneLaserTempLevel,
       "nbsSigLaneLaneLaserTemp": nbsSigLaneLaneLaserTemp,
       "nbsSigLaneTraps": nbsSigLaneTraps,
       "nbsSigLaneTraps0": nbsSigLaneTraps0}
)
