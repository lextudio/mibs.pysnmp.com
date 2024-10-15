# SNMP MIB module (ISKRATEL-IPMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISKRATEL-IPMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:52 2024
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

(msanAdditionalConf,) = mibBuilder.importSymbols(
    "ISKRATEL-MSAN-MIB",
    "msanAdditionalConf")

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

msanShMC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MsanShMCImpControllerVariablesTable_Object = MibTable
msanShMCImpControllerVariablesTable = _MsanShMCImpControllerVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1)
)
if mibBuilder.loadTexts:
    msanShMCImpControllerVariablesTable.setStatus("current")
_MsanShMCImpControllerVariablesEntry_Object = MibTableRow
msanShMCImpControllerVariablesEntry = _MsanShMCImpControllerVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1)
)
msanShMCImpControllerVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCImpControllerIndex"),
)
if mibBuilder.loadTexts:
    msanShMCImpControllerVariablesEntry.setStatus("current")


class _MsanShMCImpControllerIndex_Type(Integer32):
    """Custom type msanShMCImpControllerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerIndex_Type.__name__ = "Integer32"
_MsanShMCImpControllerIndex_Object = MibTableColumn
msanShMCImpControllerIndex = _MsanShMCImpControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 1),
    _MsanShMCImpControllerIndex_Type()
)
msanShMCImpControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerIndex.setStatus("current")


class _MsanShMCImpControllerSdrVersion_Type(Integer32):
    """Custom type msanShMCImpControllerSdrVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerSdrVersion_Type.__name__ = "Integer32"
_MsanShMCImpControllerSdrVersion_Object = MibTableColumn
msanShMCImpControllerSdrVersion = _MsanShMCImpControllerSdrVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 2),
    _MsanShMCImpControllerSdrVersion_Type()
)
msanShMCImpControllerSdrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerSdrVersion.setStatus("current")


class _MsanShMCImpControllerPicmgVersion_Type(Integer32):
    """Custom type msanShMCImpControllerPicmgVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerPicmgVersion_Type.__name__ = "Integer32"
_MsanShMCImpControllerPicmgVersion_Object = MibTableColumn
msanShMCImpControllerPicmgVersion = _MsanShMCImpControllerPicmgVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 3),
    _MsanShMCImpControllerPicmgVersion_Type()
)
msanShMCImpControllerPicmgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerPicmgVersion.setStatus("current")


class _MsanShMCImpControllerSlaveAddress_Type(Integer32):
    """Custom type msanShMCImpControllerSlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerSlaveAddress_Type.__name__ = "Integer32"
_MsanShMCImpControllerSlaveAddress_Object = MibTableColumn
msanShMCImpControllerSlaveAddress = _MsanShMCImpControllerSlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 4),
    _MsanShMCImpControllerSlaveAddress_Type()
)
msanShMCImpControllerSlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerSlaveAddress.setStatus("current")


class _MsanShMCImpControllerChannelNumber_Type(Integer32):
    """Custom type msanShMCImpControllerChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerChannelNumber_Type.__name__ = "Integer32"
_MsanShMCImpControllerChannelNumber_Object = MibTableColumn
msanShMCImpControllerChannelNumber = _MsanShMCImpControllerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 5),
    _MsanShMCImpControllerChannelNumber_Type()
)
msanShMCImpControllerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerChannelNumber.setStatus("current")


class _MsanShMCImpControllerPowerStateNotification_Type(Integer32):
    """Custom type msanShMCImpControllerPowerStateNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerPowerStateNotification_Type.__name__ = "Integer32"
_MsanShMCImpControllerPowerStateNotification_Object = MibTableColumn
msanShMCImpControllerPowerStateNotification = _MsanShMCImpControllerPowerStateNotification_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 6),
    _MsanShMCImpControllerPowerStateNotification_Type()
)
msanShMCImpControllerPowerStateNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerPowerStateNotification.setStatus("current")


class _MsanShMCImpControllerGlobalInitialisation_Type(Integer32):
    """Custom type msanShMCImpControllerGlobalInitialisation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerGlobalInitialisation_Type.__name__ = "Integer32"
_MsanShMCImpControllerGlobalInitialisation_Object = MibTableColumn
msanShMCImpControllerGlobalInitialisation = _MsanShMCImpControllerGlobalInitialisation_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 7),
    _MsanShMCImpControllerGlobalInitialisation_Type()
)
msanShMCImpControllerGlobalInitialisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerGlobalInitialisation.setStatus("current")


class _MsanShMCImpControllerCapabilities_Type(Integer32):
    """Custom type msanShMCImpControllerCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerCapabilities_Type.__name__ = "Integer32"
_MsanShMCImpControllerCapabilities_Object = MibTableColumn
msanShMCImpControllerCapabilities = _MsanShMCImpControllerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 8),
    _MsanShMCImpControllerCapabilities_Type()
)
msanShMCImpControllerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerCapabilities.setStatus("current")


class _MsanShMCImpControllerIdString_Type(DisplayString):
    """Custom type msanShMCImpControllerIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCImpControllerIdString_Type.__name__ = "DisplayString"
_MsanShMCImpControllerIdString_Object = MibTableColumn
msanShMCImpControllerIdString = _MsanShMCImpControllerIdString_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 9),
    _MsanShMCImpControllerIdString_Type()
)
msanShMCImpControllerIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerIdString.setStatus("current")


class _MsanShMCImpControllerMaximumFru_Type(Integer32):
    """Custom type msanShMCImpControllerMaximumFru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerMaximumFru_Type.__name__ = "Integer32"
_MsanShMCImpControllerMaximumFru_Object = MibTableColumn
msanShMCImpControllerMaximumFru = _MsanShMCImpControllerMaximumFru_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 10),
    _MsanShMCImpControllerMaximumFru_Type()
)
msanShMCImpControllerMaximumFru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerMaximumFru.setStatus("current")


class _MsanShMCImpControllerOwnFruId_Type(Integer32):
    """Custom type msanShMCImpControllerOwnFruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCImpControllerOwnFruId_Type.__name__ = "Integer32"
_MsanShMCImpControllerOwnFruId_Object = MibTableColumn
msanShMCImpControllerOwnFruId = _MsanShMCImpControllerOwnFruId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 1, 1, 11),
    _MsanShMCImpControllerOwnFruId_Type()
)
msanShMCImpControllerOwnFruId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCImpControllerOwnFruId.setStatus("current")
_MsanShMCFruDeviceVariablesTable_Object = MibTable
msanShMCFruDeviceVariablesTable = _MsanShMCFruDeviceVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2)
)
if mibBuilder.loadTexts:
    msanShMCFruDeviceVariablesTable.setStatus("current")
_MsanShMCFruDeviceVariablesEntry_Object = MibTableRow
msanShMCFruDeviceVariablesEntry = _MsanShMCFruDeviceVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1)
)
msanShMCFruDeviceVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCFruDeviceIndex"),
)
if mibBuilder.loadTexts:
    msanShMCFruDeviceVariablesEntry.setStatus("current")


class _MsanShMCFruDeviceIndex_Type(Integer32):
    """Custom type msanShMCFruDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, -1),
    )


_MsanShMCFruDeviceIndex_Type.__name__ = "Integer32"
_MsanShMCFruDeviceIndex_Object = MibTableColumn
msanShMCFruDeviceIndex = _MsanShMCFruDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 1),
    _MsanShMCFruDeviceIndex_Type()
)
msanShMCFruDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceIndex.setStatus("current")


class _MsanShMCFruDeviceSdrVersion_Type(Integer32):
    """Custom type msanShMCFruDeviceSdrVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceSdrVersion_Type.__name__ = "Integer32"
_MsanShMCFruDeviceSdrVersion_Object = MibTableColumn
msanShMCFruDeviceSdrVersion = _MsanShMCFruDeviceSdrVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 2),
    _MsanShMCFruDeviceSdrVersion_Type()
)
msanShMCFruDeviceSdrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceSdrVersion.setStatus("current")


class _MsanShMCFruDeviceSlaveAddress_Type(Integer32):
    """Custom type msanShMCFruDeviceSlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceSlaveAddress_Type.__name__ = "Integer32"
_MsanShMCFruDeviceSlaveAddress_Object = MibTableColumn
msanShMCFruDeviceSlaveAddress = _MsanShMCFruDeviceSlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 3),
    _MsanShMCFruDeviceSlaveAddress_Type()
)
msanShMCFruDeviceSlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceSlaveAddress.setStatus("current")


class _MsanShMCFruDeviceSFruDeviceId_Type(Integer32):
    """Custom type msanShMCFruDeviceSFruDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceSFruDeviceId_Type.__name__ = "Integer32"
_MsanShMCFruDeviceSFruDeviceId_Object = MibTableColumn
msanShMCFruDeviceSFruDeviceId = _MsanShMCFruDeviceSFruDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 4),
    _MsanShMCFruDeviceSFruDeviceId_Type()
)
msanShMCFruDeviceSFruDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceSFruDeviceId.setStatus("current")


class _MsanShMCFruDeviceChannelNumber_Type(Integer32):
    """Custom type msanShMCFruDeviceChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceChannelNumber_Type.__name__ = "Integer32"
_MsanShMCFruDeviceChannelNumber_Object = MibTableColumn
msanShMCFruDeviceChannelNumber = _MsanShMCFruDeviceChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 5),
    _MsanShMCFruDeviceChannelNumber_Type()
)
msanShMCFruDeviceChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceChannelNumber.setStatus("current")


class _MsanShMCFruDeviceDeviceType_Type(Integer32):
    """Custom type msanShMCFruDeviceDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceDeviceType_Type.__name__ = "Integer32"
_MsanShMCFruDeviceDeviceType_Object = MibTableColumn
msanShMCFruDeviceDeviceType = _MsanShMCFruDeviceDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 6),
    _MsanShMCFruDeviceDeviceType_Type()
)
msanShMCFruDeviceDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceDeviceType.setStatus("current")


class _MsanShMCFruDeviceDeviceTypeModifier_Type(Integer32):
    """Custom type msanShMCFruDeviceDeviceTypeModifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceDeviceTypeModifier_Type.__name__ = "Integer32"
_MsanShMCFruDeviceDeviceTypeModifier_Object = MibTableColumn
msanShMCFruDeviceDeviceTypeModifier = _MsanShMCFruDeviceDeviceTypeModifier_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 7),
    _MsanShMCFruDeviceDeviceTypeModifier_Type()
)
msanShMCFruDeviceDeviceTypeModifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceDeviceTypeModifier.setStatus("current")


class _MsanShMCFruDeviceFruEntityId_Type(Integer32):
    """Custom type msanShMCFruDeviceFruEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceFruEntityId_Type.__name__ = "Integer32"
_MsanShMCFruDeviceFruEntityId_Object = MibTableColumn
msanShMCFruDeviceFruEntityId = _MsanShMCFruDeviceFruEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 8),
    _MsanShMCFruDeviceFruEntityId_Type()
)
msanShMCFruDeviceFruEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceFruEntityId.setStatus("current")


class _MsanShMCFruDeviceFruEntityInstance_Type(Integer32):
    """Custom type msanShMCFruDeviceFruEntityInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceFruEntityInstance_Type.__name__ = "Integer32"
_MsanShMCFruDeviceFruEntityInstance_Object = MibTableColumn
msanShMCFruDeviceFruEntityInstance = _MsanShMCFruDeviceFruEntityInstance_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 9),
    _MsanShMCFruDeviceFruEntityInstance_Type()
)
msanShMCFruDeviceFruEntityInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceFruEntityInstance.setStatus("current")


class _MsanShMCFruDeviceIdString_Type(DisplayString):
    """Custom type msanShMCFruDeviceIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFruDeviceIdString_Type.__name__ = "DisplayString"
_MsanShMCFruDeviceIdString_Object = MibTableColumn
msanShMCFruDeviceIdString = _MsanShMCFruDeviceIdString_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 10),
    _MsanShMCFruDeviceIdString_Type()
)
msanShMCFruDeviceIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceIdString.setStatus("current")


class _MsanShMCFruDeviceHotSwapState_Type(Integer32):
    """Custom type msanShMCFruDeviceHotSwapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceHotSwapState_Type.__name__ = "Integer32"
_MsanShMCFruDeviceHotSwapState_Object = MibTableColumn
msanShMCFruDeviceHotSwapState = _MsanShMCFruDeviceHotSwapState_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 11),
    _MsanShMCFruDeviceHotSwapState_Type()
)
msanShMCFruDeviceHotSwapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruDeviceHotSwapState.setStatus("current")


class _MsanShMCFruDeviceActivated_Type(Integer32):
    """Custom type msanShMCFruDeviceActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruDeviceActivated_Type.__name__ = "Integer32"
_MsanShMCFruDeviceActivated_Object = MibTableColumn
msanShMCFruDeviceActivated = _MsanShMCFruDeviceActivated_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 2, 1, 12),
    _MsanShMCFruDeviceActivated_Type()
)
msanShMCFruDeviceActivated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCFruDeviceActivated.setStatus("current")
_MsanShMCSensorVariablesTable_Object = MibTable
msanShMCSensorVariablesTable = _MsanShMCSensorVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3)
)
if mibBuilder.loadTexts:
    msanShMCSensorVariablesTable.setStatus("current")
_MsanShMCSensorVariablesEntry_Object = MibTableRow
msanShMCSensorVariablesEntry = _MsanShMCSensorVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1)
)
msanShMCSensorVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCSensorIndex"),
)
if mibBuilder.loadTexts:
    msanShMCSensorVariablesEntry.setStatus("current")


class _MsanShMCSensorIndex_Type(Integer32):
    """Custom type msanShMCSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, -1),
    )


_MsanShMCSensorIndex_Type.__name__ = "Integer32"
_MsanShMCSensorIndex_Object = MibTableColumn
msanShMCSensorIndex = _MsanShMCSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 1),
    _MsanShMCSensorIndex_Type()
)
msanShMCSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorIndex.setStatus("current")


class _MsanShMCSensorSdrVersion_Type(Integer32):
    """Custom type msanShMCSensorSdrVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorSdrVersion_Type.__name__ = "Integer32"
_MsanShMCSensorSdrVersion_Object = MibTableColumn
msanShMCSensorSdrVersion = _MsanShMCSensorSdrVersion_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 2),
    _MsanShMCSensorSdrVersion_Type()
)
msanShMCSensorSdrVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorSdrVersion.setStatus("current")


class _MsanShMCSensorRecordType_Type(Integer32):
    """Custom type msanShMCSensorRecordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorRecordType_Type.__name__ = "Integer32"
_MsanShMCSensorRecordType_Object = MibTableColumn
msanShMCSensorRecordType = _MsanShMCSensorRecordType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 3),
    _MsanShMCSensorRecordType_Type()
)
msanShMCSensorRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorRecordType.setStatus("current")


class _MsanShMCSensorOwnerId_Type(Integer32):
    """Custom type msanShMCSensorOwnerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorOwnerId_Type.__name__ = "Integer32"
_MsanShMCSensorOwnerId_Object = MibTableColumn
msanShMCSensorOwnerId = _MsanShMCSensorOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 4),
    _MsanShMCSensorOwnerId_Type()
)
msanShMCSensorOwnerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorOwnerId.setStatus("current")


class _MsanShMCSensorOwnerLun_Type(Integer32):
    """Custom type msanShMCSensorOwnerLun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorOwnerLun_Type.__name__ = "Integer32"
_MsanShMCSensorOwnerLun_Object = MibTableColumn
msanShMCSensorOwnerLun = _MsanShMCSensorOwnerLun_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 5),
    _MsanShMCSensorOwnerLun_Type()
)
msanShMCSensorOwnerLun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorOwnerLun.setStatus("current")


class _MsanShMCSensorNumber_Type(Integer32):
    """Custom type msanShMCSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorNumber_Type.__name__ = "Integer32"
_MsanShMCSensorNumber_Object = MibTableColumn
msanShMCSensorNumber = _MsanShMCSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 6),
    _MsanShMCSensorNumber_Type()
)
msanShMCSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorNumber.setStatus("current")


class _MsanShMCSensorEntityInstance_Type(Integer32):
    """Custom type msanShMCSensorEntityInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorEntityInstance_Type.__name__ = "Integer32"
_MsanShMCSensorEntityInstance_Object = MibTableColumn
msanShMCSensorEntityInstance = _MsanShMCSensorEntityInstance_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 7),
    _MsanShMCSensorEntityInstance_Type()
)
msanShMCSensorEntityInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorEntityInstance.setStatus("current")


class _MsanShMCSensorEntityId_Type(Integer32):
    """Custom type msanShMCSensorEntityId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorEntityId_Type.__name__ = "Integer32"
_MsanShMCSensorEntityId_Object = MibTableColumn
msanShMCSensorEntityId = _MsanShMCSensorEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 8),
    _MsanShMCSensorEntityId_Type()
)
msanShMCSensorEntityId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorEntityId.setStatus("current")


class _MsanShMCSensorInitialisation_Type(Integer32):
    """Custom type msanShMCSensorInitialisation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorInitialisation_Type.__name__ = "Integer32"
_MsanShMCSensorInitialisation_Object = MibTableColumn
msanShMCSensorInitialisation = _MsanShMCSensorInitialisation_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 9),
    _MsanShMCSensorInitialisation_Type()
)
msanShMCSensorInitialisation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorInitialisation.setStatus("current")


class _MsanShMCSensorCapabilities_Type(Integer32):
    """Custom type msanShMCSensorCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorCapabilities_Type.__name__ = "Integer32"
_MsanShMCSensorCapabilities_Object = MibTableColumn
msanShMCSensorCapabilities = _MsanShMCSensorCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 10),
    _MsanShMCSensorCapabilities_Type()
)
msanShMCSensorCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorCapabilities.setStatus("current")


class _MsanShMCSensorType_Type(Integer32):
    """Custom type msanShMCSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorType_Type.__name__ = "Integer32"
_MsanShMCSensorType_Object = MibTableColumn
msanShMCSensorType = _MsanShMCSensorType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 11),
    _MsanShMCSensorType_Type()
)
msanShMCSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorType.setStatus("current")


class _MsanShMCSensorEvent_Type(Integer32):
    """Custom type msanShMCSensorEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorEvent_Type.__name__ = "Integer32"
_MsanShMCSensorEvent_Object = MibTableColumn
msanShMCSensorEvent = _MsanShMCSensorEvent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 12),
    _MsanShMCSensorEvent_Type()
)
msanShMCSensorEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorEvent.setStatus("current")


class _MsanShMCSensorAssertionEventMask_Type(Integer32):
    """Custom type msanShMCSensorAssertionEventMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanShMCSensorAssertionEventMask_Type.__name__ = "Integer32"
_MsanShMCSensorAssertionEventMask_Object = MibTableColumn
msanShMCSensorAssertionEventMask = _MsanShMCSensorAssertionEventMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 13),
    _MsanShMCSensorAssertionEventMask_Type()
)
msanShMCSensorAssertionEventMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorAssertionEventMask.setStatus("current")


class _MsanShMCSensorDeassertionEventMask_Type(Integer32):
    """Custom type msanShMCSensorDeassertionEventMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanShMCSensorDeassertionEventMask_Type.__name__ = "Integer32"
_MsanShMCSensorDeassertionEventMask_Object = MibTableColumn
msanShMCSensorDeassertionEventMask = _MsanShMCSensorDeassertionEventMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 14),
    _MsanShMCSensorDeassertionEventMask_Type()
)
msanShMCSensorDeassertionEventMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorDeassertionEventMask.setStatus("current")


class _MsanShMCSensorMask_Type(Integer32):
    """Custom type msanShMCSensorMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorMask_Type.__name__ = "Integer32"
_MsanShMCSensorMask_Object = MibTableColumn
msanShMCSensorMask = _MsanShMCSensorMask_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 15),
    _MsanShMCSensorMask_Type()
)
msanShMCSensorMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorMask.setStatus("current")


class _MsanShMCSensorUnit1_Type(Integer32):
    """Custom type msanShMCSensorUnit1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorUnit1_Type.__name__ = "Integer32"
_MsanShMCSensorUnit1_Object = MibTableColumn
msanShMCSensorUnit1 = _MsanShMCSensorUnit1_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 16),
    _MsanShMCSensorUnit1_Type()
)
msanShMCSensorUnit1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorUnit1.setStatus("current")


class _MsanShMCSensorUnit2_Type(Integer32):
    """Custom type msanShMCSensorUnit2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorUnit2_Type.__name__ = "Integer32"
_MsanShMCSensorUnit2_Object = MibTableColumn
msanShMCSensorUnit2 = _MsanShMCSensorUnit2_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 17),
    _MsanShMCSensorUnit2_Type()
)
msanShMCSensorUnit2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorUnit2.setStatus("current")


class _MsanShMCSensorUnit3_Type(Integer32):
    """Custom type msanShMCSensorUnit3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorUnit3_Type.__name__ = "Integer32"
_MsanShMCSensorUnit3_Object = MibTableColumn
msanShMCSensorUnit3 = _MsanShMCSensorUnit3_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 18),
    _MsanShMCSensorUnit3_Type()
)
msanShMCSensorUnit3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorUnit3.setStatus("current")


class _MsanShMCSensorLinearization_Type(Integer32):
    """Custom type msanShMCSensorLinearization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorLinearization_Type.__name__ = "Integer32"
_MsanShMCSensorLinearization_Object = MibTableColumn
msanShMCSensorLinearization = _MsanShMCSensorLinearization_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 19),
    _MsanShMCSensorLinearization_Type()
)
msanShMCSensorLinearization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorLinearization.setStatus("current")


class _MsanShMCSensorM_Type(Integer32):
    """Custom type msanShMCSensorM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorM_Type.__name__ = "Integer32"
_MsanShMCSensorM_Object = MibTableColumn
msanShMCSensorM = _MsanShMCSensorM_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 20),
    _MsanShMCSensorM_Type()
)
msanShMCSensorM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorM.setStatus("current")


class _MsanShMCSensorTolerance_Type(Integer32):
    """Custom type msanShMCSensorTolerance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorTolerance_Type.__name__ = "Integer32"
_MsanShMCSensorTolerance_Object = MibTableColumn
msanShMCSensorTolerance = _MsanShMCSensorTolerance_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 21),
    _MsanShMCSensorTolerance_Type()
)
msanShMCSensorTolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorTolerance.setStatus("current")


class _MsanShMCSensorB_Type(Integer32):
    """Custom type msanShMCSensorB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorB_Type.__name__ = "Integer32"
_MsanShMCSensorB_Object = MibTableColumn
msanShMCSensorB = _MsanShMCSensorB_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 22),
    _MsanShMCSensorB_Type()
)
msanShMCSensorB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorB.setStatus("current")


class _MsanShMCSensorAccuracy_Type(Integer32):
    """Custom type msanShMCSensorAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorAccuracy_Type.__name__ = "Integer32"
_MsanShMCSensorAccuracy_Object = MibTableColumn
msanShMCSensorAccuracy = _MsanShMCSensorAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 23),
    _MsanShMCSensorAccuracy_Type()
)
msanShMCSensorAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorAccuracy.setStatus("current")


class _MsanShMCSensorAccuracyExp_Type(Integer32):
    """Custom type msanShMCSensorAccuracyExp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorAccuracyExp_Type.__name__ = "Integer32"
_MsanShMCSensorAccuracyExp_Object = MibTableColumn
msanShMCSensorAccuracyExp = _MsanShMCSensorAccuracyExp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 24),
    _MsanShMCSensorAccuracyExp_Type()
)
msanShMCSensorAccuracyExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorAccuracyExp.setStatus("current")


class _MsanShMCSensorRexp_Type(Integer32):
    """Custom type msanShMCSensorRexp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorRexp_Type.__name__ = "Integer32"
_MsanShMCSensorRexp_Object = MibTableColumn
msanShMCSensorRexp = _MsanShMCSensorRexp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 25),
    _MsanShMCSensorRexp_Type()
)
msanShMCSensorRexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorRexp.setStatus("current")


class _MsanShMCSensorBexp_Type(Integer32):
    """Custom type msanShMCSensorBexp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorBexp_Type.__name__ = "Integer32"
_MsanShMCSensorBexp_Object = MibTableColumn
msanShMCSensorBexp = _MsanShMCSensorBexp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 26),
    _MsanShMCSensorBexp_Type()
)
msanShMCSensorBexp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorBexp.setStatus("current")


class _MsanShMCSensorCharacteristicFlags_Type(Integer32):
    """Custom type msanShMCSensorCharacteristicFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorCharacteristicFlags_Type.__name__ = "Integer32"
_MsanShMCSensorCharacteristicFlags_Object = MibTableColumn
msanShMCSensorCharacteristicFlags = _MsanShMCSensorCharacteristicFlags_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 27),
    _MsanShMCSensorCharacteristicFlags_Type()
)
msanShMCSensorCharacteristicFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorCharacteristicFlags.setStatus("current")


class _MsanShMCSensorReading_Type(Integer32):
    """Custom type msanShMCSensorReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorReading_Type.__name__ = "Integer32"
_MsanShMCSensorReading_Object = MibTableColumn
msanShMCSensorReading = _MsanShMCSensorReading_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 28),
    _MsanShMCSensorReading_Type()
)
msanShMCSensorReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorReading.setStatus("current")


class _MsanShMCSensorProcessedReading_Type(DisplayString):
    """Custom type msanShMCSensorProcessedReading based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCSensorProcessedReading_Type.__name__ = "DisplayString"
_MsanShMCSensorProcessedReading_Object = MibTableColumn
msanShMCSensorProcessedReading = _MsanShMCSensorProcessedReading_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 29),
    _MsanShMCSensorProcessedReading_Type()
)
msanShMCSensorProcessedReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorProcessedReading.setStatus("current")


class _MsanShMCSensorNominalReading_Type(Integer32):
    """Custom type msanShMCSensorNominalReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorNominalReading_Type.__name__ = "Integer32"
_MsanShMCSensorNominalReading_Object = MibTableColumn
msanShMCSensorNominalReading = _MsanShMCSensorNominalReading_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 30),
    _MsanShMCSensorNominalReading_Type()
)
msanShMCSensorNominalReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorNominalReading.setStatus("current")


class _MsanShMCSensorNormalMaximum_Type(Integer32):
    """Custom type msanShMCSensorNormalMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorNormalMaximum_Type.__name__ = "Integer32"
_MsanShMCSensorNormalMaximum_Object = MibTableColumn
msanShMCSensorNormalMaximum = _MsanShMCSensorNormalMaximum_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 31),
    _MsanShMCSensorNormalMaximum_Type()
)
msanShMCSensorNormalMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorNormalMaximum.setStatus("current")


class _MsanShMCSensorNormalMinimum_Type(Integer32):
    """Custom type msanShMCSensorNormalMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorNormalMinimum_Type.__name__ = "Integer32"
_MsanShMCSensorNormalMinimum_Object = MibTableColumn
msanShMCSensorNormalMinimum = _MsanShMCSensorNormalMinimum_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 32),
    _MsanShMCSensorNormalMinimum_Type()
)
msanShMCSensorNormalMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorNormalMinimum.setStatus("current")


class _MsanShMCSensorMaximumReading_Type(Integer32):
    """Custom type msanShMCSensorMaximumReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorMaximumReading_Type.__name__ = "Integer32"
_MsanShMCSensorMaximumReading_Object = MibTableColumn
msanShMCSensorMaximumReading = _MsanShMCSensorMaximumReading_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 33),
    _MsanShMCSensorMaximumReading_Type()
)
msanShMCSensorMaximumReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorMaximumReading.setStatus("current")


class _MsanShMCSensorMinimumReading_Type(Integer32):
    """Custom type msanShMCSensorMinimumReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorMinimumReading_Type.__name__ = "Integer32"
_MsanShMCSensorMinimumReading_Object = MibTableColumn
msanShMCSensorMinimumReading = _MsanShMCSensorMinimumReading_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 34),
    _MsanShMCSensorMinimumReading_Type()
)
msanShMCSensorMinimumReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorMinimumReading.setStatus("current")


class _MsanShMCSensorUpperNonRecoverableThr_Type(Integer32):
    """Custom type msanShMCSensorUpperNonRecoverableThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorUpperNonRecoverableThr_Type.__name__ = "Integer32"
_MsanShMCSensorUpperNonRecoverableThr_Object = MibTableColumn
msanShMCSensorUpperNonRecoverableThr = _MsanShMCSensorUpperNonRecoverableThr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 35),
    _MsanShMCSensorUpperNonRecoverableThr_Type()
)
msanShMCSensorUpperNonRecoverableThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorUpperNonRecoverableThr.setStatus("current")


class _MsanShMCSensorUpperCriticalThr_Type(Integer32):
    """Custom type msanShMCSensorUpperCriticalThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorUpperCriticalThr_Type.__name__ = "Integer32"
_MsanShMCSensorUpperCriticalThr_Object = MibTableColumn
msanShMCSensorUpperCriticalThr = _MsanShMCSensorUpperCriticalThr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 36),
    _MsanShMCSensorUpperCriticalThr_Type()
)
msanShMCSensorUpperCriticalThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorUpperCriticalThr.setStatus("current")


class _MsanShMCSensorUpperNonCriticalThr_Type(Integer32):
    """Custom type msanShMCSensorUpperNonCriticalThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorUpperNonCriticalThr_Type.__name__ = "Integer32"
_MsanShMCSensorUpperNonCriticalThr_Object = MibTableColumn
msanShMCSensorUpperNonCriticalThr = _MsanShMCSensorUpperNonCriticalThr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 37),
    _MsanShMCSensorUpperNonCriticalThr_Type()
)
msanShMCSensorUpperNonCriticalThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorUpperNonCriticalThr.setStatus("current")


class _MsanShMCSensorLowerNonRecoverableThr_Type(Integer32):
    """Custom type msanShMCSensorLowerNonRecoverableThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorLowerNonRecoverableThr_Type.__name__ = "Integer32"
_MsanShMCSensorLowerNonRecoverableThr_Object = MibTableColumn
msanShMCSensorLowerNonRecoverableThr = _MsanShMCSensorLowerNonRecoverableThr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 38),
    _MsanShMCSensorLowerNonRecoverableThr_Type()
)
msanShMCSensorLowerNonRecoverableThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorLowerNonRecoverableThr.setStatus("current")


class _MsanShMCSensorLowerCriticalThr_Type(Integer32):
    """Custom type msanShMCSensorLowerCriticalThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorLowerCriticalThr_Type.__name__ = "Integer32"
_MsanShMCSensorLowerCriticalThr_Object = MibTableColumn
msanShMCSensorLowerCriticalThr = _MsanShMCSensorLowerCriticalThr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 39),
    _MsanShMCSensorLowerCriticalThr_Type()
)
msanShMCSensorLowerCriticalThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorLowerCriticalThr.setStatus("current")


class _MsanShMCSensorLowerNonCriticalThr_Type(Integer32):
    """Custom type msanShMCSensorLowerNonCriticalThr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorLowerNonCriticalThr_Type.__name__ = "Integer32"
_MsanShMCSensorLowerNonCriticalThr_Object = MibTableColumn
msanShMCSensorLowerNonCriticalThr = _MsanShMCSensorLowerNonCriticalThr_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 40),
    _MsanShMCSensorLowerNonCriticalThr_Type()
)
msanShMCSensorLowerNonCriticalThr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorLowerNonCriticalThr.setStatus("current")


class _MsanShMCSensorPositiveGoingThrHysteresis_Type(Integer32):
    """Custom type msanShMCSensorPositiveGoingThrHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorPositiveGoingThrHysteresis_Type.__name__ = "Integer32"
_MsanShMCSensorPositiveGoingThrHysteresis_Object = MibTableColumn
msanShMCSensorPositiveGoingThrHysteresis = _MsanShMCSensorPositiveGoingThrHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 41),
    _MsanShMCSensorPositiveGoingThrHysteresis_Type()
)
msanShMCSensorPositiveGoingThrHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorPositiveGoingThrHysteresis.setStatus("current")


class _MsanShMCSensorNegativeGoingThrHysteresis_Type(Integer32):
    """Custom type msanShMCSensorNegativeGoingThrHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSensorNegativeGoingThrHysteresis_Type.__name__ = "Integer32"
_MsanShMCSensorNegativeGoingThrHysteresis_Object = MibTableColumn
msanShMCSensorNegativeGoingThrHysteresis = _MsanShMCSensorNegativeGoingThrHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 42),
    _MsanShMCSensorNegativeGoingThrHysteresis_Type()
)
msanShMCSensorNegativeGoingThrHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorNegativeGoingThrHysteresis.setStatus("current")


class _MsanShMCSensorIdString_Type(DisplayString):
    """Custom type msanShMCSensorIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCSensorIdString_Type.__name__ = "DisplayString"
_MsanShMCSensorIdString_Object = MibTableColumn
msanShMCSensorIdString = _MsanShMCSensorIdString_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 43),
    _MsanShMCSensorIdString_Type()
)
msanShMCSensorIdString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorIdString.setStatus("current")


class _MsanShMCSensorEntireSensorData_Type(OctetString):
    """Custom type msanShMCSensorEntireSensorData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCSensorEntireSensorData_Type.__name__ = "OctetString"
_MsanShMCSensorEntireSensorData_Object = MibTableColumn
msanShMCSensorEntireSensorData = _MsanShMCSensorEntireSensorData_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 3, 1, 44),
    _MsanShMCSensorEntireSensorData_Type()
)
msanShMCSensorEntireSensorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSensorEntireSensorData.setStatus("current")
_MsanShMCBoardsTable_Object = MibTable
msanShMCBoardsTable = _MsanShMCBoardsTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4)
)
if mibBuilder.loadTexts:
    msanShMCBoardsTable.setStatus("current")
_MsanShMCBoardsEntry_Object = MibTableRow
msanShMCBoardsEntry = _MsanShMCBoardsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4, 1)
)
msanShMCBoardsEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCBoardsIndex"),
)
if mibBuilder.loadTexts:
    msanShMCBoardsEntry.setStatus("current")


class _MsanShMCBoardsIndex_Type(Integer32):
    """Custom type msanShMCBoardsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCBoardsIndex_Type.__name__ = "Integer32"
_MsanShMCBoardsIndex_Object = MibTableColumn
msanShMCBoardsIndex = _MsanShMCBoardsIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4, 1, 1),
    _MsanShMCBoardsIndex_Type()
)
msanShMCBoardsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardsIndex.setStatus("current")


class _MsanShMCBoardsBoardBasicPresent_Type(Integer32):
    """Custom type msanShMCBoardsBoardBasicPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_MsanShMCBoardsBoardBasicPresent_Type.__name__ = "Integer32"
_MsanShMCBoardsBoardBasicPresent_Object = MibTableColumn
msanShMCBoardsBoardBasicPresent = _MsanShMCBoardsBoardBasicPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4, 1, 2),
    _MsanShMCBoardsBoardBasicPresent_Type()
)
msanShMCBoardsBoardBasicPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardsBoardBasicPresent.setStatus("current")


class _MsanShMCBoardsBoardBasicHealthy_Type(Integer32):
    """Custom type msanShMCBoardsBoardBasicHealthy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCBoardsBoardBasicHealthy_Type.__name__ = "Integer32"
_MsanShMCBoardsBoardBasicHealthy_Object = MibTableColumn
msanShMCBoardsBoardBasicHealthy = _MsanShMCBoardsBoardBasicHealthy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4, 1, 3),
    _MsanShMCBoardsBoardBasicHealthy_Type()
)
msanShMCBoardsBoardBasicHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardsBoardBasicHealthy.setStatus("current")


class _MsanShMCBoardsBoardBasicReset_Type(Integer32):
    """Custom type msanShMCBoardsBoardBasicReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("none", 0))
    )


_MsanShMCBoardsBoardBasicReset_Type.__name__ = "Integer32"
_MsanShMCBoardsBoardBasicReset_Object = MibTableColumn
msanShMCBoardsBoardBasicReset = _MsanShMCBoardsBoardBasicReset_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4, 1, 4),
    _MsanShMCBoardsBoardBasicReset_Type()
)
msanShMCBoardsBoardBasicReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCBoardsBoardBasicReset.setStatus("current")


class _MsanShMCBoardsBoardBasicSlaveAddress_Type(Integer32):
    """Custom type msanShMCBoardsBoardBasicSlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCBoardsBoardBasicSlaveAddress_Type.__name__ = "Integer32"
_MsanShMCBoardsBoardBasicSlaveAddress_Object = MibTableColumn
msanShMCBoardsBoardBasicSlaveAddress = _MsanShMCBoardsBoardBasicSlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4, 1, 5),
    _MsanShMCBoardsBoardBasicSlaveAddress_Type()
)
msanShMCBoardsBoardBasicSlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardsBoardBasicSlaveAddress.setStatus("current")


class _MsanShMCBoardsBoardBasicFruDeviceId_Type(Integer32):
    """Custom type msanShMCBoardsBoardBasicFruDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCBoardsBoardBasicFruDeviceId_Type.__name__ = "Integer32"
_MsanShMCBoardsBoardBasicFruDeviceId_Object = MibTableColumn
msanShMCBoardsBoardBasicFruDeviceId = _MsanShMCBoardsBoardBasicFruDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 4, 1, 7),
    _MsanShMCBoardsBoardBasicFruDeviceId_Type()
)
msanShMCBoardsBoardBasicFruDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardsBoardBasicFruDeviceId.setStatus("current")
_MsanShMCSelTable_Object = MibTable
msanShMCSelTable = _MsanShMCSelTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 5)
)
if mibBuilder.loadTexts:
    msanShMCSelTable.setStatus("current")
_MsanShMCSelEntry_Object = MibTableRow
msanShMCSelEntry = _MsanShMCSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 5, 1)
)
msanShMCSelEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCSelIndex"),
)
if mibBuilder.loadTexts:
    msanShMCSelEntry.setStatus("current")


class _MsanShMCSelIndex_Type(Integer32):
    """Custom type msanShMCSelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCSelIndex_Type.__name__ = "Integer32"
_MsanShMCSelIndex_Object = MibTableColumn
msanShMCSelIndex = _MsanShMCSelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 5, 1, 1),
    _MsanShMCSelIndex_Type()
)
msanShMCSelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSelIndex.setStatus("current")


class _MsanShMCSelcontents_Type(OctetString):
    """Custom type msanShMCSelcontents based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCSelcontents_Type.__name__ = "OctetString"
_MsanShMCSelcontents_Object = MibTableColumn
msanShMCSelcontents = _MsanShMCSelcontents_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 5, 1, 2),
    _MsanShMCSelcontents_Type()
)
msanShMCSelcontents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCSelcontents.setStatus("current")
_MsanShMCShelfTable_Object = MibTable
msanShMCShelfTable = _MsanShMCShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 6)
)
if mibBuilder.loadTexts:
    msanShMCShelfTable.setStatus("current")
_MsanShMCShelfEntry_Object = MibTableRow
msanShMCShelfEntry = _MsanShMCShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 6, 1)
)
msanShMCShelfEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCShelfIndex"),
)
if mibBuilder.loadTexts:
    msanShMCShelfEntry.setStatus("current")


class _MsanShMCShelfIndex_Type(Integer32):
    """Custom type msanShMCShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCShelfIndex_Type.__name__ = "Integer32"
_MsanShMCShelfIndex_Object = MibTableColumn
msanShMCShelfIndex = _MsanShMCShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 6, 1, 1),
    _MsanShMCShelfIndex_Type()
)
msanShMCShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfIndex.setStatus("current")


class _MsanShMCShelfHealthy_Type(Integer32):
    """Custom type msanShMCShelfHealthy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCShelfHealthy_Type.__name__ = "Integer32"
_MsanShMCShelfHealthy_Object = MibTableColumn
msanShMCShelfHealthy = _MsanShMCShelfHealthy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 6, 1, 2),
    _MsanShMCShelfHealthy_Type()
)
msanShMCShelfHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfHealthy.setStatus("current")
_MsanShMCPefConfiguration_ObjectIdentity = ObjectIdentity
msanShMCPefConfiguration = _MsanShMCPefConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8)
)


class _MsanShMCPefConfigurationSetInProgress_Type(Integer32):
    """Custom type msanShMCPefConfigurationSetInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationSetInProgress_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationSetInProgress_Object = MibScalar
msanShMCPefConfigurationSetInProgress = _MsanShMCPefConfigurationSetInProgress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 1),
    _MsanShMCPefConfigurationSetInProgress_Type()
)
msanShMCPefConfigurationSetInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationSetInProgress.setStatus("current")


class _MsanShMCPefConfigurationControl_Type(Integer32):
    """Custom type msanShMCPefConfigurationControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationControl_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationControl_Object = MibScalar
msanShMCPefConfigurationControl = _MsanShMCPefConfigurationControl_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 2),
    _MsanShMCPefConfigurationControl_Type()
)
msanShMCPefConfigurationControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationControl.setStatus("current")


class _MsanShMCPefConfigurationActionGlobalControl_Type(Integer32):
    """Custom type msanShMCPefConfigurationActionGlobalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationActionGlobalControl_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationActionGlobalControl_Object = MibScalar
msanShMCPefConfigurationActionGlobalControl = _MsanShMCPefConfigurationActionGlobalControl_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 3),
    _MsanShMCPefConfigurationActionGlobalControl_Type()
)
msanShMCPefConfigurationActionGlobalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationActionGlobalControl.setStatus("current")


class _MsanShMCPefConfigurationStartupDelay_Type(Integer32):
    """Custom type msanShMCPefConfigurationStartupDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationStartupDelay_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationStartupDelay_Object = MibScalar
msanShMCPefConfigurationStartupDelay = _MsanShMCPefConfigurationStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 4),
    _MsanShMCPefConfigurationStartupDelay_Type()
)
msanShMCPefConfigurationStartupDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationStartupDelay.setStatus("current")


class _MsanShMCPefConfigurationAlertStartupDelay_Type(Integer32):
    """Custom type msanShMCPefConfigurationAlertStartupDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationAlertStartupDelay_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationAlertStartupDelay_Object = MibScalar
msanShMCPefConfigurationAlertStartupDelay = _MsanShMCPefConfigurationAlertStartupDelay_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 5),
    _MsanShMCPefConfigurationAlertStartupDelay_Type()
)
msanShMCPefConfigurationAlertStartupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationAlertStartupDelay.setStatus("current")


class _MsanShMCPefConfigurationNumberOfEventFilters_Type(Integer32):
    """Custom type msanShMCPefConfigurationNumberOfEventFilters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationNumberOfEventFilters_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationNumberOfEventFilters_Object = MibScalar
msanShMCPefConfigurationNumberOfEventFilters = _MsanShMCPefConfigurationNumberOfEventFilters_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 6),
    _MsanShMCPefConfigurationNumberOfEventFilters_Type()
)
msanShMCPefConfigurationNumberOfEventFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationNumberOfEventFilters.setStatus("current")


class _MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Type(Integer32):
    """Custom type msanShMCPefConfigurationNumberOfAlertPoliciEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Object = MibScalar
msanShMCPefConfigurationNumberOfAlertPoliciEntries = _MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 7),
    _MsanShMCPefConfigurationNumberOfAlertPoliciEntries_Type()
)
msanShMCPefConfigurationNumberOfAlertPoliciEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationNumberOfAlertPoliciEntries.setStatus("current")


class _MsanShMCPefConfigurationSystemGuid_Type(Integer32):
    """Custom type msanShMCPefConfigurationSystemGuid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationSystemGuid_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationSystemGuid_Object = MibScalar
msanShMCPefConfigurationSystemGuid = _MsanShMCPefConfigurationSystemGuid_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 8),
    _MsanShMCPefConfigurationSystemGuid_Type()
)
msanShMCPefConfigurationSystemGuid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationSystemGuid.setStatus("current")


class _MsanShMCPefConfigurationNumberOfAlertStrings_Type(Integer32):
    """Custom type msanShMCPefConfigurationNumberOfAlertStrings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPefConfigurationNumberOfAlertStrings_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationNumberOfAlertStrings_Object = MibScalar
msanShMCPefConfigurationNumberOfAlertStrings = _MsanShMCPefConfigurationNumberOfAlertStrings_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 8, 9),
    _MsanShMCPefConfigurationNumberOfAlertStrings_Type()
)
msanShMCPefConfigurationNumberOfAlertStrings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationNumberOfAlertStrings.setStatus("current")
_MsanShMCPefConfigurationEventFilterTable_Object = MibTable
msanShMCPefConfigurationEventFilterTable = _MsanShMCPefConfigurationEventFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 14)
)
if mibBuilder.loadTexts:
    msanShMCPefConfigurationEventFilterTable.setStatus("current")
_MsanShMCPefConfigurationEventFilterEntry_Object = MibTableRow
msanShMCPefConfigurationEventFilterEntry = _MsanShMCPefConfigurationEventFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 14, 1)
)
msanShMCPefConfigurationEventFilterEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCPefConfigurationEventFilterIndex"),
)
if mibBuilder.loadTexts:
    msanShMCPefConfigurationEventFilterEntry.setStatus("current")


class _MsanShMCPefConfigurationEventFilterIndex_Type(Integer32):
    """Custom type msanShMCPefConfigurationEventFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCPefConfigurationEventFilterIndex_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationEventFilterIndex_Object = MibTableColumn
msanShMCPefConfigurationEventFilterIndex = _MsanShMCPefConfigurationEventFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 14, 1, 1),
    _MsanShMCPefConfigurationEventFilterIndex_Type()
)
msanShMCPefConfigurationEventFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationEventFilterIndex.setStatus("current")


class _MsanShMCPefConfigurationEventFilterData_Type(OctetString):
    """Custom type msanShMCPefConfigurationEventFilterData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_MsanShMCPefConfigurationEventFilterData_Type.__name__ = "OctetString"
_MsanShMCPefConfigurationEventFilterData_Object = MibTableColumn
msanShMCPefConfigurationEventFilterData = _MsanShMCPefConfigurationEventFilterData_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 14, 1, 2),
    _MsanShMCPefConfigurationEventFilterData_Type()
)
msanShMCPefConfigurationEventFilterData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationEventFilterData.setStatus("current")
_MsanShMCPefConfigurationAlertStringTable_Object = MibTable
msanShMCPefConfigurationAlertStringTable = _MsanShMCPefConfigurationAlertStringTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 19)
)
if mibBuilder.loadTexts:
    msanShMCPefConfigurationAlertStringTable.setStatus("current")
_MsanShMCPefConfigurationAlertStringEntry_Object = MibTableRow
msanShMCPefConfigurationAlertStringEntry = _MsanShMCPefConfigurationAlertStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 19, 1)
)
msanShMCPefConfigurationAlertStringEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCPefConfigurationAlertStringIndex"),
)
if mibBuilder.loadTexts:
    msanShMCPefConfigurationAlertStringEntry.setStatus("current")


class _MsanShMCPefConfigurationAlertStringIndex_Type(Integer32):
    """Custom type msanShMCPefConfigurationAlertStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCPefConfigurationAlertStringIndex_Type.__name__ = "Integer32"
_MsanShMCPefConfigurationAlertStringIndex_Object = MibTableColumn
msanShMCPefConfigurationAlertStringIndex = _MsanShMCPefConfigurationAlertStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 19, 1, 1),
    _MsanShMCPefConfigurationAlertStringIndex_Type()
)
msanShMCPefConfigurationAlertStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationAlertStringIndex.setStatus("current")


class _MsanShMCPefConfigurationAlertStringKey_Type(OctetString):
    """Custom type msanShMCPefConfigurationAlertStringKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MsanShMCPefConfigurationAlertStringKey_Type.__name__ = "OctetString"
_MsanShMCPefConfigurationAlertStringKey_Object = MibTableColumn
msanShMCPefConfigurationAlertStringKey = _MsanShMCPefConfigurationAlertStringKey_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 19, 1, 2),
    _MsanShMCPefConfigurationAlertStringKey_Type()
)
msanShMCPefConfigurationAlertStringKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationAlertStringKey.setStatus("current")


class _MsanShMCPefConfigurationAlertString_Type(DisplayString):
    """Custom type msanShMCPefConfigurationAlertString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_MsanShMCPefConfigurationAlertString_Type.__name__ = "DisplayString"
_MsanShMCPefConfigurationAlertString_Object = MibTableColumn
msanShMCPefConfigurationAlertString = _MsanShMCPefConfigurationAlertString_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 19, 1, 3),
    _MsanShMCPefConfigurationAlertString_Type()
)
msanShMCPefConfigurationAlertString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPefConfigurationAlertString.setStatus("current")
_MsanShMCFruInfoTable_Object = MibTable
msanShMCFruInfoTable = _MsanShMCFruInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 20)
)
if mibBuilder.loadTexts:
    msanShMCFruInfoTable.setStatus("current")
_MsanShMCFruInfoEntry_Object = MibTableRow
msanShMCFruInfoEntry = _MsanShMCFruInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 20, 1)
)
msanShMCFruInfoEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCFruInfoIndex"),
)
if mibBuilder.loadTexts:
    msanShMCFruInfoEntry.setStatus("current")


class _MsanShMCFruInfoIndex_Type(Integer32):
    """Custom type msanShMCFruInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFruInfoIndex_Type.__name__ = "Integer32"
_MsanShMCFruInfoIndex_Object = MibTableColumn
msanShMCFruInfoIndex = _MsanShMCFruInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 20, 1, 1),
    _MsanShMCFruInfoIndex_Type()
)
msanShMCFruInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruInfoIndex.setStatus("current")


class _MsanShMCFruInfoData_Type(OctetString):
    """Custom type msanShMCFruInfoData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanShMCFruInfoData_Type.__name__ = "OctetString"
_MsanShMCFruInfoData_Object = MibTableColumn
msanShMCFruInfoData = _MsanShMCFruInfoData_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 20, 1, 2),
    _MsanShMCFruInfoData_Type()
)
msanShMCFruInfoData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFruInfoData.setStatus("current")


class _MsanShMCFruInfoDataWo_Type(OctetString):
    """Custom type msanShMCFruInfoDataWo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MsanShMCFruInfoDataWo_Type.__name__ = "OctetString"
_MsanShMCFruInfoDataWo_Object = MibTableColumn
msanShMCFruInfoDataWo = _MsanShMCFruInfoDataWo_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 20, 1, 3),
    _MsanShMCFruInfoDataWo_Type()
)
msanShMCFruInfoDataWo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCFruInfoDataWo.setStatus("current")
_MsanShMCBoardVariablesTable_Object = MibTable
msanShMCBoardVariablesTable = _MsanShMCBoardVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32)
)
if mibBuilder.loadTexts:
    msanShMCBoardVariablesTable.setStatus("current")
_MsanShMCBoardVariablesEntry_Object = MibTableRow
msanShMCBoardVariablesEntry = _MsanShMCBoardVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1)
)
msanShMCBoardVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCBoardVariablesBoardBasicSlotNumber"),
)
if mibBuilder.loadTexts:
    msanShMCBoardVariablesEntry.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicSlotNumber_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicSlotNumber_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicSlotNumber_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicSlotNumber = _MsanShMCBoardVariablesBoardBasicSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 1),
    _MsanShMCBoardVariablesBoardBasicSlotNumber_Type()
)
msanShMCBoardVariablesBoardBasicSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicSlotNumber.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicPresent_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_MsanShMCBoardVariablesBoardBasicPresent_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicPresent_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicPresent = _MsanShMCBoardVariablesBoardBasicPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 2),
    _MsanShMCBoardVariablesBoardBasicPresent_Type()
)
msanShMCBoardVariablesBoardBasicPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicPresent.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicHealthy_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicHealthy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCBoardVariablesBoardBasicHealthy_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicHealthy_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicHealthy = _MsanShMCBoardVariablesBoardBasicHealthy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 3),
    _MsanShMCBoardVariablesBoardBasicHealthy_Type()
)
msanShMCBoardVariablesBoardBasicHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicHealthy.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicReset_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("none", 0))
    )


_MsanShMCBoardVariablesBoardBasicReset_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicReset_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicReset = _MsanShMCBoardVariablesBoardBasicReset_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 4),
    _MsanShMCBoardVariablesBoardBasicReset_Type()
)
msanShMCBoardVariablesBoardBasicReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicReset.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicPowered_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicPowered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("powered", 1))
    )


_MsanShMCBoardVariablesBoardBasicPowered_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicPowered_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicPowered = _MsanShMCBoardVariablesBoardBasicPowered_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 5),
    _MsanShMCBoardVariablesBoardBasicPowered_Type()
)
msanShMCBoardVariablesBoardBasicPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicPowered.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicSlaveAddress_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicSlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicSlaveAddress_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicSlaveAddress_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicSlaveAddress = _MsanShMCBoardVariablesBoardBasicSlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 6),
    _MsanShMCBoardVariablesBoardBasicSlaveAddress_Type()
)
msanShMCBoardVariablesBoardBasicSlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicSlaveAddress.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicFruDeviceId_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicFruDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicFruDeviceId_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicFruDeviceId_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicFruDeviceId = _MsanShMCBoardVariablesBoardBasicFruDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 7),
    _MsanShMCBoardVariablesBoardBasicFruDeviceId_Type()
)
msanShMCBoardVariablesBoardBasicFruDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicFruDeviceId.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent = _MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 8),
    _MsanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent_Type()
)
msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicProductManufacturer_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicProductManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicProductManufacturer_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicProductManufacturer_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicProductManufacturer = _MsanShMCBoardVariablesBoardBasicProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 9),
    _MsanShMCBoardVariablesBoardBasicProductManufacturer_Type()
)
msanShMCBoardVariablesBoardBasicProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicProductManufacturer.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicProductName_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicProductName_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicProductName_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicProductName = _MsanShMCBoardVariablesBoardBasicProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 10),
    _MsanShMCBoardVariablesBoardBasicProductName_Type()
)
msanShMCBoardVariablesBoardBasicProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicProductName.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicProductPartModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicProductPartModelNumber = _MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 11),
    _MsanShMCBoardVariablesBoardBasicProductPartModelNumber_Type()
)
msanShMCBoardVariablesBoardBasicProductPartModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicProductPartModelNumber.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicProductVersionNumber_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicProductVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicProductVersionNumber_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicProductVersionNumber_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicProductVersionNumber = _MsanShMCBoardVariablesBoardBasicProductVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 12),
    _MsanShMCBoardVariablesBoardBasicProductVersionNumber_Type()
)
msanShMCBoardVariablesBoardBasicProductVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicProductVersionNumber.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicProductSerialNumber_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicProductSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicProductSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicProductSerialNumber_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicProductSerialNumber = _MsanShMCBoardVariablesBoardBasicProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 13),
    _MsanShMCBoardVariablesBoardBasicProductSerialNumber_Type()
)
msanShMCBoardVariablesBoardBasicProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicProductSerialNumber.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicBoardAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicBoardAreaPresent = _MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 14),
    _MsanShMCBoardVariablesBoardBasicBoardAreaPresent_Type()
)
msanShMCBoardVariablesBoardBasicBoardAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicBoardAreaPresent.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicBoardManufacturer_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicBoardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicBoardManufacturer_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicBoardManufacturer_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicBoardManufacturer = _MsanShMCBoardVariablesBoardBasicBoardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 15),
    _MsanShMCBoardVariablesBoardBasicBoardManufacturer_Type()
)
msanShMCBoardVariablesBoardBasicBoardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicBoardManufacturer.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicBoardProductName_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicBoardProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicBoardProductName_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicBoardProductName_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicBoardProductName = _MsanShMCBoardVariablesBoardBasicBoardProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 16),
    _MsanShMCBoardVariablesBoardBasicBoardProductName_Type()
)
msanShMCBoardVariablesBoardBasicBoardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicBoardProductName.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicBoardSerialNumber = _MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 17),
    _MsanShMCBoardVariablesBoardBasicBoardSerialNumber_Type()
)
msanShMCBoardVariablesBoardBasicBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicBoardSerialNumber.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicBoardPartNumber_Type(DisplayString):
    """Custom type msanShMCBoardVariablesBoardBasicBoardPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCBoardVariablesBoardBasicBoardPartNumber_Type.__name__ = "DisplayString"
_MsanShMCBoardVariablesBoardBasicBoardPartNumber_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicBoardPartNumber = _MsanShMCBoardVariablesBoardBasicBoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 18),
    _MsanShMCBoardVariablesBoardBasicBoardPartNumber_Type()
)
msanShMCBoardVariablesBoardBasicBoardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicBoardPartNumber.setStatus("current")


class _MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Type(Integer32):
    """Custom type msanShMCBoardVariablesBoardBasicBoardManufactureTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Object = MibTableColumn
msanShMCBoardVariablesBoardBasicBoardManufactureTime = _MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 19),
    _MsanShMCBoardVariablesBoardBasicBoardManufactureTime_Type()
)
msanShMCBoardVariablesBoardBasicBoardManufactureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesBoardBasicBoardManufactureTime.setStatus("current")


class _MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Type(Integer32):
    """Custom type msanShMCBoardVariablesSelectivePowerOffSwitchOffType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("switchOff", 2),
          ("switchOn", 3))
    )


_MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Type.__name__ = "Integer32"
_MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Object = MibTableColumn
msanShMCBoardVariablesSelectivePowerOffSwitchOffType = _MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 32, 1, 20),
    _MsanShMCBoardVariablesSelectivePowerOffSwitchOffType_Type()
)
msanShMCBoardVariablesSelectivePowerOffSwitchOffType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCBoardVariablesSelectivePowerOffSwitchOffType.setStatus("current")
_MsanShMCFanTrayVariablesTable_Object = MibTable
msanShMCFanTrayVariablesTable = _MsanShMCFanTrayVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33)
)
if mibBuilder.loadTexts:
    msanShMCFanTrayVariablesTable.setStatus("current")
_MsanShMCFanTrayVariablesEntry_Object = MibTableRow
msanShMCFanTrayVariablesEntry = _MsanShMCFanTrayVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1)
)
msanShMCFanTrayVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCFanTraySlotNumber"),
)
if mibBuilder.loadTexts:
    msanShMCFanTrayVariablesEntry.setStatus("current")


class _MsanShMCFanTraySlotNumber_Type(Integer32):
    """Custom type msanShMCFanTraySlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanShMCFanTraySlotNumber_Type.__name__ = "Integer32"
_MsanShMCFanTraySlotNumber_Object = MibTableColumn
msanShMCFanTraySlotNumber = _MsanShMCFanTraySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 1),
    _MsanShMCFanTraySlotNumber_Type()
)
msanShMCFanTraySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTraySlotNumber.setStatus("current")


class _MsanShMCFanTrayPresent_Type(Integer32):
    """Custom type msanShMCFanTrayPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_MsanShMCFanTrayPresent_Type.__name__ = "Integer32"
_MsanShMCFanTrayPresent_Object = MibTableColumn
msanShMCFanTrayPresent = _MsanShMCFanTrayPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 2),
    _MsanShMCFanTrayPresent_Type()
)
msanShMCFanTrayPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayPresent.setStatus("current")


class _MsanShMCFanTrayHealthy_Type(Integer32):
    """Custom type msanShMCFanTrayHealthy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCFanTrayHealthy_Type.__name__ = "Integer32"
_MsanShMCFanTrayHealthy_Object = MibTableColumn
msanShMCFanTrayHealthy = _MsanShMCFanTrayHealthy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 3),
    _MsanShMCFanTrayHealthy_Type()
)
msanShMCFanTrayHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayHealthy.setStatus("current")


class _MsanShMCFanTrayHealthLed_Type(Integer32):
    """Custom type msanShMCFanTrayHealthLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCFanTrayHealthLed_Type.__name__ = "Integer32"
_MsanShMCFanTrayHealthLed_Object = MibTableColumn
msanShMCFanTrayHealthLed = _MsanShMCFanTrayHealthLed_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 4),
    _MsanShMCFanTrayHealthLed_Type()
)
msanShMCFanTrayHealthLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCFanTrayHealthLed.setStatus("current")


class _MsanShMCFanTraySlaveAddress_Type(Integer32):
    """Custom type msanShMCFanTraySlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFanTraySlaveAddress_Type.__name__ = "Integer32"
_MsanShMCFanTraySlaveAddress_Object = MibTableColumn
msanShMCFanTraySlaveAddress = _MsanShMCFanTraySlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 5),
    _MsanShMCFanTraySlaveAddress_Type()
)
msanShMCFanTraySlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTraySlaveAddress.setStatus("current")


class _MsanShMCFanTrayFruDeviceId_Type(Integer32):
    """Custom type msanShMCFanTrayFruDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCFanTrayFruDeviceId_Type.__name__ = "Integer32"
_MsanShMCFanTrayFruDeviceId_Object = MibTableColumn
msanShMCFanTrayFruDeviceId = _MsanShMCFanTrayFruDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 6),
    _MsanShMCFanTrayFruDeviceId_Type()
)
msanShMCFanTrayFruDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruDeviceId.setStatus("current")


class _MsanShMCFanTrayFruinfoProductAreaPresent_Type(Integer32):
    """Custom type msanShMCFanTrayFruinfoProductAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCFanTrayFruinfoProductAreaPresent_Type.__name__ = "Integer32"
_MsanShMCFanTrayFruinfoProductAreaPresent_Object = MibTableColumn
msanShMCFanTrayFruinfoProductAreaPresent = _MsanShMCFanTrayFruinfoProductAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 7),
    _MsanShMCFanTrayFruinfoProductAreaPresent_Type()
)
msanShMCFanTrayFruinfoProductAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoProductAreaPresent.setStatus("current")


class _MsanShMCFanTrayFruinfoProductManufacturer_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoProductManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoProductManufacturer_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoProductManufacturer_Object = MibTableColumn
msanShMCFanTrayFruinfoProductManufacturer = _MsanShMCFanTrayFruinfoProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 8),
    _MsanShMCFanTrayFruinfoProductManufacturer_Type()
)
msanShMCFanTrayFruinfoProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoProductManufacturer.setStatus("current")


class _MsanShMCFanTrayFruinfoProductName_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoProductName_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoProductName_Object = MibTableColumn
msanShMCFanTrayFruinfoProductName = _MsanShMCFanTrayFruinfoProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 9),
    _MsanShMCFanTrayFruinfoProductName_Type()
)
msanShMCFanTrayFruinfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoProductName.setStatus("current")


class _MsanShMCFanTrayFruinfoProductPartModelNumber_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoProductPartModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoProductPartModelNumber_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoProductPartModelNumber_Object = MibTableColumn
msanShMCFanTrayFruinfoProductPartModelNumber = _MsanShMCFanTrayFruinfoProductPartModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 10),
    _MsanShMCFanTrayFruinfoProductPartModelNumber_Type()
)
msanShMCFanTrayFruinfoProductPartModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoProductPartModelNumber.setStatus("current")


class _MsanShMCFanTrayFruinfoProductVersionNumber_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoProductVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoProductVersionNumber_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoProductVersionNumber_Object = MibTableColumn
msanShMCFanTrayFruinfoProductVersionNumber = _MsanShMCFanTrayFruinfoProductVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 11),
    _MsanShMCFanTrayFruinfoProductVersionNumber_Type()
)
msanShMCFanTrayFruinfoProductVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoProductVersionNumber.setStatus("current")


class _MsanShMCFanTrayFruinfoProductSerialNumber_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoProductSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoProductSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoProductSerialNumber_Object = MibTableColumn
msanShMCFanTrayFruinfoProductSerialNumber = _MsanShMCFanTrayFruinfoProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 12),
    _MsanShMCFanTrayFruinfoProductSerialNumber_Type()
)
msanShMCFanTrayFruinfoProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoProductSerialNumber.setStatus("current")


class _MsanShMCFanTrayFruinfoBoardAreaPresent_Type(Integer32):
    """Custom type msanShMCFanTrayFruinfoBoardAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCFanTrayFruinfoBoardAreaPresent_Type.__name__ = "Integer32"
_MsanShMCFanTrayFruinfoBoardAreaPresent_Object = MibTableColumn
msanShMCFanTrayFruinfoBoardAreaPresent = _MsanShMCFanTrayFruinfoBoardAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 13),
    _MsanShMCFanTrayFruinfoBoardAreaPresent_Type()
)
msanShMCFanTrayFruinfoBoardAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoBoardAreaPresent.setStatus("current")


class _MsanShMCFanTrayFruinfoBoardManufacturer_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoBoardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoBoardManufacturer_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoBoardManufacturer_Object = MibTableColumn
msanShMCFanTrayFruinfoBoardManufacturer = _MsanShMCFanTrayFruinfoBoardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 14),
    _MsanShMCFanTrayFruinfoBoardManufacturer_Type()
)
msanShMCFanTrayFruinfoBoardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoBoardManufacturer.setStatus("current")


class _MsanShMCFanTrayFruinfoBoardProductName_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoBoardProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoBoardProductName_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoBoardProductName_Object = MibTableColumn
msanShMCFanTrayFruinfoBoardProductName = _MsanShMCFanTrayFruinfoBoardProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 15),
    _MsanShMCFanTrayFruinfoBoardProductName_Type()
)
msanShMCFanTrayFruinfoBoardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoBoardProductName.setStatus("current")


class _MsanShMCFanTrayFruinfoBoardSerialNumber_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoBoardSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoBoardSerialNumber_Object = MibTableColumn
msanShMCFanTrayFruinfoBoardSerialNumber = _MsanShMCFanTrayFruinfoBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 16),
    _MsanShMCFanTrayFruinfoBoardSerialNumber_Type()
)
msanShMCFanTrayFruinfoBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoBoardSerialNumber.setStatus("current")


class _MsanShMCFanTrayFruinfoBoardPartNumber_Type(DisplayString):
    """Custom type msanShMCFanTrayFruinfoBoardPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCFanTrayFruinfoBoardPartNumber_Type.__name__ = "DisplayString"
_MsanShMCFanTrayFruinfoBoardPartNumber_Object = MibTableColumn
msanShMCFanTrayFruinfoBoardPartNumber = _MsanShMCFanTrayFruinfoBoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 17),
    _MsanShMCFanTrayFruinfoBoardPartNumber_Type()
)
msanShMCFanTrayFruinfoBoardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoBoardPartNumber.setStatus("current")


class _MsanShMCFanTrayFruinfoBoardManufactureTime_Type(Integer32):
    """Custom type msanShMCFanTrayFruinfoBoardManufactureTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsanShMCFanTrayFruinfoBoardManufactureTime_Type.__name__ = "Integer32"
_MsanShMCFanTrayFruinfoBoardManufactureTime_Object = MibTableColumn
msanShMCFanTrayFruinfoBoardManufactureTime = _MsanShMCFanTrayFruinfoBoardManufactureTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 33, 1, 18),
    _MsanShMCFanTrayFruinfoBoardManufactureTime_Type()
)
msanShMCFanTrayFruinfoBoardManufactureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCFanTrayFruinfoBoardManufactureTime.setStatus("current")
_MsanShMCPowerSupplyVariablesTable_Object = MibTable
msanShMCPowerSupplyVariablesTable = _MsanShMCPowerSupplyVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34)
)
if mibBuilder.loadTexts:
    msanShMCPowerSupplyVariablesTable.setStatus("current")
_MsanShMCPowerSupplyVariablesEntry_Object = MibTableRow
msanShMCPowerSupplyVariablesEntry = _MsanShMCPowerSupplyVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1)
)
msanShMCPowerSupplyVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCPowerSupplySlotNumber"),
)
if mibBuilder.loadTexts:
    msanShMCPowerSupplyVariablesEntry.setStatus("current")


class _MsanShMCPowerSupplySlotNumber_Type(Integer32):
    """Custom type msanShMCPowerSupplySlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanShMCPowerSupplySlotNumber_Type.__name__ = "Integer32"
_MsanShMCPowerSupplySlotNumber_Object = MibTableColumn
msanShMCPowerSupplySlotNumber = _MsanShMCPowerSupplySlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 1),
    _MsanShMCPowerSupplySlotNumber_Type()
)
msanShMCPowerSupplySlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplySlotNumber.setStatus("current")


class _MsanShMCPowerSupplyDegrade_Type(Integer32):
    """Custom type msanShMCPowerSupplyDegrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_MsanShMCPowerSupplyDegrade_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyDegrade_Object = MibTableColumn
msanShMCPowerSupplyDegrade = _MsanShMCPowerSupplyDegrade_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 2),
    _MsanShMCPowerSupplyDegrade_Type()
)
msanShMCPowerSupplyDegrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyDegrade.setStatus("current")


class _MsanShMCPowerSupplyFail_Type(Integer32):
    """Custom type msanShMCPowerSupplyFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPowerSupplyFail_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyFail_Object = MibTableColumn
msanShMCPowerSupplyFail = _MsanShMCPowerSupplyFail_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 3),
    _MsanShMCPowerSupplyFail_Type()
)
msanShMCPowerSupplyFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFail.setStatus("current")


class _MsanShMCPowerSupplyInhibit_Type(Integer32):
    """Custom type msanShMCPowerSupplyInhibit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("on", 0))
    )


_MsanShMCPowerSupplyInhibit_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyInhibit_Object = MibTableColumn
msanShMCPowerSupplyInhibit = _MsanShMCPowerSupplyInhibit_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 4),
    _MsanShMCPowerSupplyInhibit_Type()
)
msanShMCPowerSupplyInhibit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyInhibit.setStatus("current")


class _MsanShMCPowerSupplyHealthy_Type(Integer32):
    """Custom type msanShMCPowerSupplyHealthy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCPowerSupplyHealthy_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyHealthy_Object = MibTableColumn
msanShMCPowerSupplyHealthy = _MsanShMCPowerSupplyHealthy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 5),
    _MsanShMCPowerSupplyHealthy_Type()
)
msanShMCPowerSupplyHealthy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyHealthy.setStatus("current")


class _MsanShMCPowerSupplySlaveAddress_Type(Integer32):
    """Custom type msanShMCPowerSupplySlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCPowerSupplySlaveAddress_Type.__name__ = "Integer32"
_MsanShMCPowerSupplySlaveAddress_Object = MibTableColumn
msanShMCPowerSupplySlaveAddress = _MsanShMCPowerSupplySlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 6),
    _MsanShMCPowerSupplySlaveAddress_Type()
)
msanShMCPowerSupplySlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplySlaveAddress.setStatus("current")


class _MsanShMCPowerSupplyFruDeviceId_Type(Integer32):
    """Custom type msanShMCPowerSupplyFruDeviceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruDeviceId_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyFruDeviceId_Object = MibTableColumn
msanShMCPowerSupplyFruDeviceId = _MsanShMCPowerSupplyFruDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 7),
    _MsanShMCPowerSupplyFruDeviceId_Type()
)
msanShMCPowerSupplyFruDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruDeviceId.setStatus("current")


class _MsanShMCPowerSupplyFruinfoProductAreaPresent_Type(Integer32):
    """Custom type msanShMCPowerSupplyFruinfoProductAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCPowerSupplyFruinfoProductAreaPresent_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyFruinfoProductAreaPresent_Object = MibTableColumn
msanShMCPowerSupplyFruinfoProductAreaPresent = _MsanShMCPowerSupplyFruinfoProductAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 8),
    _MsanShMCPowerSupplyFruinfoProductAreaPresent_Type()
)
msanShMCPowerSupplyFruinfoProductAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoProductAreaPresent.setStatus("current")


class _MsanShMCPowerSupplyFruinfoProductManufacturer_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoProductManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoProductManufacturer_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoProductManufacturer_Object = MibTableColumn
msanShMCPowerSupplyFruinfoProductManufacturer = _MsanShMCPowerSupplyFruinfoProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 9),
    _MsanShMCPowerSupplyFruinfoProductManufacturer_Type()
)
msanShMCPowerSupplyFruinfoProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoProductManufacturer.setStatus("current")


class _MsanShMCPowerSupplyFruinfoProductName_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoProductName_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoProductName_Object = MibTableColumn
msanShMCPowerSupplyFruinfoProductName = _MsanShMCPowerSupplyFruinfoProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 10),
    _MsanShMCPowerSupplyFruinfoProductName_Type()
)
msanShMCPowerSupplyFruinfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoProductName.setStatus("current")


class _MsanShMCPowerSupplyFruinfoProductPartModelNumber_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoProductPartModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoProductPartModelNumber_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoProductPartModelNumber_Object = MibTableColumn
msanShMCPowerSupplyFruinfoProductPartModelNumber = _MsanShMCPowerSupplyFruinfoProductPartModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 11),
    _MsanShMCPowerSupplyFruinfoProductPartModelNumber_Type()
)
msanShMCPowerSupplyFruinfoProductPartModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoProductPartModelNumber.setStatus("current")


class _MsanShMCPowerSupplyFruinfoProductVersionNumber_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoProductVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoProductVersionNumber_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoProductVersionNumber_Object = MibTableColumn
msanShMCPowerSupplyFruinfoProductVersionNumber = _MsanShMCPowerSupplyFruinfoProductVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 12),
    _MsanShMCPowerSupplyFruinfoProductVersionNumber_Type()
)
msanShMCPowerSupplyFruinfoProductVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoProductVersionNumber.setStatus("current")


class _MsanShMCPowerSupplyFruinfoProductSerialNumber_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoProductSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoProductSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoProductSerialNumber_Object = MibTableColumn
msanShMCPowerSupplyFruinfoProductSerialNumber = _MsanShMCPowerSupplyFruinfoProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 13),
    _MsanShMCPowerSupplyFruinfoProductSerialNumber_Type()
)
msanShMCPowerSupplyFruinfoProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoProductSerialNumber.setStatus("current")


class _MsanShMCPowerSupplyFruinfoBoardAreaPresent_Type(Integer32):
    """Custom type msanShMCPowerSupplyFruinfoBoardAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCPowerSupplyFruinfoBoardAreaPresent_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyFruinfoBoardAreaPresent_Object = MibTableColumn
msanShMCPowerSupplyFruinfoBoardAreaPresent = _MsanShMCPowerSupplyFruinfoBoardAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 14),
    _MsanShMCPowerSupplyFruinfoBoardAreaPresent_Type()
)
msanShMCPowerSupplyFruinfoBoardAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoBoardAreaPresent.setStatus("current")


class _MsanShMCPowerSupplyFruinfoBoardManufacturer_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoBoardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoBoardManufacturer_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoBoardManufacturer_Object = MibTableColumn
msanShMCPowerSupplyFruinfoBoardManufacturer = _MsanShMCPowerSupplyFruinfoBoardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 15),
    _MsanShMCPowerSupplyFruinfoBoardManufacturer_Type()
)
msanShMCPowerSupplyFruinfoBoardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoBoardManufacturer.setStatus("current")


class _MsanShMCPowerSupplyFruinfoBoardProductName_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoBoardProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoBoardProductName_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoBoardProductName_Object = MibTableColumn
msanShMCPowerSupplyFruinfoBoardProductName = _MsanShMCPowerSupplyFruinfoBoardProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 16),
    _MsanShMCPowerSupplyFruinfoBoardProductName_Type()
)
msanShMCPowerSupplyFruinfoBoardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoBoardProductName.setStatus("current")


class _MsanShMCPowerSupplyFruinfoBoardSerialNumber_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoBoardSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoBoardSerialNumber_Object = MibTableColumn
msanShMCPowerSupplyFruinfoBoardSerialNumber = _MsanShMCPowerSupplyFruinfoBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 17),
    _MsanShMCPowerSupplyFruinfoBoardSerialNumber_Type()
)
msanShMCPowerSupplyFruinfoBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoBoardSerialNumber.setStatus("current")


class _MsanShMCPowerSupplyFruinfoBoardPartNumber_Type(DisplayString):
    """Custom type msanShMCPowerSupplyFruinfoBoardPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCPowerSupplyFruinfoBoardPartNumber_Type.__name__ = "DisplayString"
_MsanShMCPowerSupplyFruinfoBoardPartNumber_Object = MibTableColumn
msanShMCPowerSupplyFruinfoBoardPartNumber = _MsanShMCPowerSupplyFruinfoBoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 18),
    _MsanShMCPowerSupplyFruinfoBoardPartNumber_Type()
)
msanShMCPowerSupplyFruinfoBoardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoBoardPartNumber.setStatus("current")


class _MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Type(Integer32):
    """Custom type msanShMCPowerSupplyFruinfoBoardmanufactureTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Type.__name__ = "Integer32"
_MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Object = MibTableColumn
msanShMCPowerSupplyFruinfoBoardmanufactureTime = _MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 34, 1, 19),
    _MsanShMCPowerSupplyFruinfoBoardmanufactureTime_Type()
)
msanShMCPowerSupplyFruinfoBoardmanufactureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCPowerSupplyFruinfoBoardmanufactureTime.setStatus("current")
_MsanShMCShelfManagerVariablesTable_Object = MibTable
msanShMCShelfManagerVariablesTable = _MsanShMCShelfManagerVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35)
)
if mibBuilder.loadTexts:
    msanShMCShelfManagerVariablesTable.setStatus("current")
_MsanShMCShelfManagerVariablesEntry_Object = MibTableRow
msanShMCShelfManagerVariablesEntry = _MsanShMCShelfManagerVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1)
)
msanShMCShelfManagerVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCShelfManagerSlotNumber"),
)
if mibBuilder.loadTexts:
    msanShMCShelfManagerVariablesEntry.setStatus("current")


class _MsanShMCShelfManagerSlotNumber_Type(Integer32):
    """Custom type msanShMCShelfManagerSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsanShMCShelfManagerSlotNumber_Type.__name__ = "Integer32"
_MsanShMCShelfManagerSlotNumber_Object = MibTableColumn
msanShMCShelfManagerSlotNumber = _MsanShMCShelfManagerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 1),
    _MsanShMCShelfManagerSlotNumber_Type()
)
msanShMCShelfManagerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerSlotNumber.setStatus("current")


class _MsanShMCShelfManagerSlaveAddress_Type(Integer32):
    """Custom type msanShMCShelfManagerSlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCShelfManagerSlaveAddress_Type.__name__ = "Integer32"
_MsanShMCShelfManagerSlaveAddress_Object = MibTableColumn
msanShMCShelfManagerSlaveAddress = _MsanShMCShelfManagerSlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 2),
    _MsanShMCShelfManagerSlaveAddress_Type()
)
msanShMCShelfManagerSlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerSlaveAddress.setStatus("current")


class _MsanShMCShelfManagerPresent_Type(Integer32):
    """Custom type msanShMCShelfManagerPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("present", 1))
    )


_MsanShMCShelfManagerPresent_Type.__name__ = "Integer32"
_MsanShMCShelfManagerPresent_Object = MibTableColumn
msanShMCShelfManagerPresent = _MsanShMCShelfManagerPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 3),
    _MsanShMCShelfManagerPresent_Type()
)
msanShMCShelfManagerPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerPresent.setStatus("current")


class _MsanShMCShelfManagerHealthy_Type(Integer32):
    """Custom type msanShMCShelfManagerHealthy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MsanShMCShelfManagerHealthy_Type.__name__ = "Integer32"
_MsanShMCShelfManagerHealthy_Object = MibTableColumn
msanShMCShelfManagerHealthy = _MsanShMCShelfManagerHealthy_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 4),
    _MsanShMCShelfManagerHealthy_Type()
)
msanShMCShelfManagerHealthy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerHealthy.setStatus("current")


class _MsanShMCShelfManagerActive_Type(Integer32):
    """Custom type msanShMCShelfManagerActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 0))
    )


_MsanShMCShelfManagerActive_Type.__name__ = "Integer32"
_MsanShMCShelfManagerActive_Object = MibTableColumn
msanShMCShelfManagerActive = _MsanShMCShelfManagerActive_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 5),
    _MsanShMCShelfManagerActive_Type()
)
msanShMCShelfManagerActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCShelfManagerActive.setStatus("current")


class _MsanShMCShelfManagerReset_Type(Integer32):
    """Custom type msanShMCShelfManagerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cold", 1),
          ("none", 0))
    )


_MsanShMCShelfManagerReset_Type.__name__ = "Integer32"
_MsanShMCShelfManagerReset_Object = MibTableColumn
msanShMCShelfManagerReset = _MsanShMCShelfManagerReset_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 6),
    _MsanShMCShelfManagerReset_Type()
)
msanShMCShelfManagerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCShelfManagerReset.setStatus("current")


class _MsanShMCShelfManagerFruinfoProductAreaPresent_Type(Integer32):
    """Custom type msanShMCShelfManagerFruinfoProductAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCShelfManagerFruinfoProductAreaPresent_Type.__name__ = "Integer32"
_MsanShMCShelfManagerFruinfoProductAreaPresent_Object = MibTableColumn
msanShMCShelfManagerFruinfoProductAreaPresent = _MsanShMCShelfManagerFruinfoProductAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 7),
    _MsanShMCShelfManagerFruinfoProductAreaPresent_Type()
)
msanShMCShelfManagerFruinfoProductAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoProductAreaPresent.setStatus("current")


class _MsanShMCShelfManagerFruinfoProductManufacturer_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoProductManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoProductManufacturer_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoProductManufacturer_Object = MibTableColumn
msanShMCShelfManagerFruinfoProductManufacturer = _MsanShMCShelfManagerFruinfoProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 8),
    _MsanShMCShelfManagerFruinfoProductManufacturer_Type()
)
msanShMCShelfManagerFruinfoProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoProductManufacturer.setStatus("current")


class _MsanShMCShelfManagerFruinfoProductName_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoProductName_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoProductName_Object = MibTableColumn
msanShMCShelfManagerFruinfoProductName = _MsanShMCShelfManagerFruinfoProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 9),
    _MsanShMCShelfManagerFruinfoProductName_Type()
)
msanShMCShelfManagerFruinfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoProductName.setStatus("current")


class _MsanShMCShelfManagerFruinfoProductPartModelNumber_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoProductPartModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoProductPartModelNumber_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoProductPartModelNumber_Object = MibTableColumn
msanShMCShelfManagerFruinfoProductPartModelNumber = _MsanShMCShelfManagerFruinfoProductPartModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 10),
    _MsanShMCShelfManagerFruinfoProductPartModelNumber_Type()
)
msanShMCShelfManagerFruinfoProductPartModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoProductPartModelNumber.setStatus("current")


class _MsanShMCShelfManagerFruinfoProductVersionNumber_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoProductVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoProductVersionNumber_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoProductVersionNumber_Object = MibTableColumn
msanShMCShelfManagerFruinfoProductVersionNumber = _MsanShMCShelfManagerFruinfoProductVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 11),
    _MsanShMCShelfManagerFruinfoProductVersionNumber_Type()
)
msanShMCShelfManagerFruinfoProductVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoProductVersionNumber.setStatus("current")


class _MsanShMCShelfManagerFruinfoProductSerialNumber_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoProductSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoProductSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoProductSerialNumber_Object = MibTableColumn
msanShMCShelfManagerFruinfoProductSerialNumber = _MsanShMCShelfManagerFruinfoProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 12),
    _MsanShMCShelfManagerFruinfoProductSerialNumber_Type()
)
msanShMCShelfManagerFruinfoProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoProductSerialNumber.setStatus("current")


class _MsanShMCShelfManagerFruinfoBoardAreaPresent_Type(Integer32):
    """Custom type msanShMCShelfManagerFruinfoBoardAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCShelfManagerFruinfoBoardAreaPresent_Type.__name__ = "Integer32"
_MsanShMCShelfManagerFruinfoBoardAreaPresent_Object = MibTableColumn
msanShMCShelfManagerFruinfoBoardAreaPresent = _MsanShMCShelfManagerFruinfoBoardAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 13),
    _MsanShMCShelfManagerFruinfoBoardAreaPresent_Type()
)
msanShMCShelfManagerFruinfoBoardAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoBoardAreaPresent.setStatus("current")


class _MsanShMCShelfManagerFruinfoBoardManufacturer_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoBoardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoBoardManufacturer_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoBoardManufacturer_Object = MibTableColumn
msanShMCShelfManagerFruinfoBoardManufacturer = _MsanShMCShelfManagerFruinfoBoardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 14),
    _MsanShMCShelfManagerFruinfoBoardManufacturer_Type()
)
msanShMCShelfManagerFruinfoBoardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoBoardManufacturer.setStatus("current")


class _MsanShMCShelfManagerFruinfoBoardProductName_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoBoardProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoBoardProductName_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoBoardProductName_Object = MibTableColumn
msanShMCShelfManagerFruinfoBoardProductName = _MsanShMCShelfManagerFruinfoBoardProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 15),
    _MsanShMCShelfManagerFruinfoBoardProductName_Type()
)
msanShMCShelfManagerFruinfoBoardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoBoardProductName.setStatus("current")


class _MsanShMCShelfManagerFruinfoBoardSerialNumber_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoBoardSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoBoardSerialNumber_Object = MibTableColumn
msanShMCShelfManagerFruinfoBoardSerialNumber = _MsanShMCShelfManagerFruinfoBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 16),
    _MsanShMCShelfManagerFruinfoBoardSerialNumber_Type()
)
msanShMCShelfManagerFruinfoBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoBoardSerialNumber.setStatus("current")


class _MsanShMCShelfManagerFruinfoBoardPartNumber_Type(DisplayString):
    """Custom type msanShMCShelfManagerFruinfoBoardPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCShelfManagerFruinfoBoardPartNumber_Type.__name__ = "DisplayString"
_MsanShMCShelfManagerFruinfoBoardPartNumber_Object = MibTableColumn
msanShMCShelfManagerFruinfoBoardPartNumber = _MsanShMCShelfManagerFruinfoBoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 17),
    _MsanShMCShelfManagerFruinfoBoardPartNumber_Type()
)
msanShMCShelfManagerFruinfoBoardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoBoardPartNumber.setStatus("current")


class _MsanShMCShelfManagerFruinfoBoardmanufactureTime_Type(Integer32):
    """Custom type msanShMCShelfManagerFruinfoBoardmanufactureTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsanShMCShelfManagerFruinfoBoardmanufactureTime_Type.__name__ = "Integer32"
_MsanShMCShelfManagerFruinfoBoardmanufactureTime_Object = MibTableColumn
msanShMCShelfManagerFruinfoBoardmanufactureTime = _MsanShMCShelfManagerFruinfoBoardmanufactureTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 35, 1, 18),
    _MsanShMCShelfManagerFruinfoBoardmanufactureTime_Type()
)
msanShMCShelfManagerFruinfoBoardmanufactureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCShelfManagerFruinfoBoardmanufactureTime.setStatus("current")
_MsanShMCChassisVariablesTable_Object = MibTable
msanShMCChassisVariablesTable = _MsanShMCChassisVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36)
)
if mibBuilder.loadTexts:
    msanShMCChassisVariablesTable.setStatus("current")
_MsanShMCChassisVariablesEntry_Object = MibTableRow
msanShMCChassisVariablesEntry = _MsanShMCChassisVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1)
)
msanShMCChassisVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCChassisId"),
)
if mibBuilder.loadTexts:
    msanShMCChassisVariablesEntry.setStatus("current")


class _MsanShMCChassisId_Type(Integer32):
    """Custom type msanShMCChassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCChassisId_Type.__name__ = "Integer32"
_MsanShMCChassisId_Object = MibTableColumn
msanShMCChassisId = _MsanShMCChassisId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 1),
    _MsanShMCChassisId_Type()
)
msanShMCChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisId.setStatus("current")


class _MsanShMCChassisType_Type(Integer32):
    """Custom type msanShMCChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCChassisType_Type.__name__ = "Integer32"
_MsanShMCChassisType_Object = MibTableColumn
msanShMCChassisType = _MsanShMCChassisType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 2),
    _MsanShMCChassisType_Type()
)
msanShMCChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisType.setStatus("current")


class _MsanShMCChassisPartNumber_Type(DisplayString):
    """Custom type msanShMCChassisPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisPartNumber_Type.__name__ = "DisplayString"
_MsanShMCChassisPartNumber_Object = MibTableColumn
msanShMCChassisPartNumber = _MsanShMCChassisPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 3),
    _MsanShMCChassisPartNumber_Type()
)
msanShMCChassisPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisPartNumber.setStatus("current")


class _MsanShMCChassisSerialNumber_Type(DisplayString):
    """Custom type msanShMCChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCChassisSerialNumber_Object = MibTableColumn
msanShMCChassisSerialNumber = _MsanShMCChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 4),
    _MsanShMCChassisSerialNumber_Type()
)
msanShMCChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisSerialNumber.setStatus("current")


class _MsanShMCChassisProductAreaPresent_Type(Integer32):
    """Custom type msanShMCChassisProductAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCChassisProductAreaPresent_Type.__name__ = "Integer32"
_MsanShMCChassisProductAreaPresent_Object = MibTableColumn
msanShMCChassisProductAreaPresent = _MsanShMCChassisProductAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 5),
    _MsanShMCChassisProductAreaPresent_Type()
)
msanShMCChassisProductAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisProductAreaPresent.setStatus("current")


class _MsanShMCChassisProductManufacturer_Type(DisplayString):
    """Custom type msanShMCChassisProductManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisProductManufacturer_Type.__name__ = "DisplayString"
_MsanShMCChassisProductManufacturer_Object = MibTableColumn
msanShMCChassisProductManufacturer = _MsanShMCChassisProductManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 6),
    _MsanShMCChassisProductManufacturer_Type()
)
msanShMCChassisProductManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisProductManufacturer.setStatus("current")


class _MsanShMCChassisProductName_Type(DisplayString):
    """Custom type msanShMCChassisProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisProductName_Type.__name__ = "DisplayString"
_MsanShMCChassisProductName_Object = MibTableColumn
msanShMCChassisProductName = _MsanShMCChassisProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 7),
    _MsanShMCChassisProductName_Type()
)
msanShMCChassisProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisProductName.setStatus("current")


class _MsanShMCChassisProductPartModelNumber_Type(DisplayString):
    """Custom type msanShMCChassisProductPartModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisProductPartModelNumber_Type.__name__ = "DisplayString"
_MsanShMCChassisProductPartModelNumber_Object = MibTableColumn
msanShMCChassisProductPartModelNumber = _MsanShMCChassisProductPartModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 8),
    _MsanShMCChassisProductPartModelNumber_Type()
)
msanShMCChassisProductPartModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisProductPartModelNumber.setStatus("current")


class _MsanShMCChassisProductVersionNumber_Type(DisplayString):
    """Custom type msanShMCChassisProductVersionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisProductVersionNumber_Type.__name__ = "DisplayString"
_MsanShMCChassisProductVersionNumber_Object = MibTableColumn
msanShMCChassisProductVersionNumber = _MsanShMCChassisProductVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 9),
    _MsanShMCChassisProductVersionNumber_Type()
)
msanShMCChassisProductVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisProductVersionNumber.setStatus("current")


class _MsanShMCChassisProductSerialNumber_Type(DisplayString):
    """Custom type msanShMCChassisProductSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisProductSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCChassisProductSerialNumber_Object = MibTableColumn
msanShMCChassisProductSerialNumber = _MsanShMCChassisProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 10),
    _MsanShMCChassisProductSerialNumber_Type()
)
msanShMCChassisProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisProductSerialNumber.setStatus("current")


class _MsanShMCChassisBoardAreaPresent_Type(Integer32):
    """Custom type msanShMCChassisBoardAreaPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MsanShMCChassisBoardAreaPresent_Type.__name__ = "Integer32"
_MsanShMCChassisBoardAreaPresent_Object = MibTableColumn
msanShMCChassisBoardAreaPresent = _MsanShMCChassisBoardAreaPresent_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 11),
    _MsanShMCChassisBoardAreaPresent_Type()
)
msanShMCChassisBoardAreaPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisBoardAreaPresent.setStatus("current")


class _MsanShMCChassisBoardManufacturer_Type(DisplayString):
    """Custom type msanShMCChassisBoardManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisBoardManufacturer_Type.__name__ = "DisplayString"
_MsanShMCChassisBoardManufacturer_Object = MibTableColumn
msanShMCChassisBoardManufacturer = _MsanShMCChassisBoardManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 12),
    _MsanShMCChassisBoardManufacturer_Type()
)
msanShMCChassisBoardManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisBoardManufacturer.setStatus("current")


class _MsanShMCChassisBoardProductName_Type(DisplayString):
    """Custom type msanShMCChassisBoardProductName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisBoardProductName_Type.__name__ = "DisplayString"
_MsanShMCChassisBoardProductName_Object = MibTableColumn
msanShMCChassisBoardProductName = _MsanShMCChassisBoardProductName_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 13),
    _MsanShMCChassisBoardProductName_Type()
)
msanShMCChassisBoardProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisBoardProductName.setStatus("current")


class _MsanShMCChassisBoardSerialNumber_Type(DisplayString):
    """Custom type msanShMCChassisBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisBoardSerialNumber_Type.__name__ = "DisplayString"
_MsanShMCChassisBoardSerialNumber_Object = MibTableColumn
msanShMCChassisBoardSerialNumber = _MsanShMCChassisBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 14),
    _MsanShMCChassisBoardSerialNumber_Type()
)
msanShMCChassisBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisBoardSerialNumber.setStatus("current")


class _MsanShMCChassisBoardPartNumber_Type(DisplayString):
    """Custom type msanShMCChassisBoardPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MsanShMCChassisBoardPartNumber_Type.__name__ = "DisplayString"
_MsanShMCChassisBoardPartNumber_Object = MibTableColumn
msanShMCChassisBoardPartNumber = _MsanShMCChassisBoardPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 15),
    _MsanShMCChassisBoardPartNumber_Type()
)
msanShMCChassisBoardPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisBoardPartNumber.setStatus("current")


class _MsanShMCChassisBoardmanufactureTime_Type(Integer32):
    """Custom type msanShMCChassisBoardmanufactureTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsanShMCChassisBoardmanufactureTime_Type.__name__ = "Integer32"
_MsanShMCChassisBoardmanufactureTime_Object = MibTableColumn
msanShMCChassisBoardmanufactureTime = _MsanShMCChassisBoardmanufactureTime_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 36, 1, 16),
    _MsanShMCChassisBoardmanufactureTime_Type()
)
msanShMCChassisBoardmanufactureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCChassisBoardmanufactureTime.setStatus("current")
_MsanShMCEventVariablesTable_Object = MibTable
msanShMCEventVariablesTable = _MsanShMCEventVariablesTable_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37)
)
if mibBuilder.loadTexts:
    msanShMCEventVariablesTable.setStatus("current")
_MsanShMCEventVariablesEntry_Object = MibTableRow
msanShMCEventVariablesEntry = _MsanShMCEventVariablesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1)
)
msanShMCEventVariablesEntry.setIndexNames(
    (0, "ISKRATEL-IPMI-MIB", "msanShMCEventIndex"),
)
if mibBuilder.loadTexts:
    msanShMCEventVariablesEntry.setStatus("current")


class _MsanShMCEventIndex_Type(Integer32):
    """Custom type msanShMCEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCEventIndex_Type.__name__ = "Integer32"
_MsanShMCEventIndex_Object = MibTableColumn
msanShMCEventIndex = _MsanShMCEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 1),
    _MsanShMCEventIndex_Type()
)
msanShMCEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventIndex.setStatus("current")


class _MsanShMCEventDelete_Type(Integer32):
    """Custom type msanShMCEventDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCEventDelete_Type.__name__ = "Integer32"
_MsanShMCEventDelete_Object = MibTableColumn
msanShMCEventDelete = _MsanShMCEventDelete_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 2),
    _MsanShMCEventDelete_Type()
)
msanShMCEventDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCEventDelete.setStatus("current")


class _MsanShMCEventTimeStamp_Type(Integer32):
    """Custom type msanShMCEventTimeStamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MsanShMCEventTimeStamp_Type.__name__ = "Integer32"
_MsanShMCEventTimeStamp_Object = MibTableColumn
msanShMCEventTimeStamp = _MsanShMCEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 3),
    _MsanShMCEventTimeStamp_Type()
)
msanShMCEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventTimeStamp.setStatus("current")


class _MsanShMCEventClass_Type(Integer32):
    """Custom type msanShMCEventClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              225,
              240)
        )
    )
    namedValues = NamedValues(
        *(("current", 3),
          ("fan", 4),
          ("hotswap", 240),
          ("other", 0),
          ("powerstate", 225),
          ("temperature", 1),
          ("voltage", 2))
    )


_MsanShMCEventClass_Type.__name__ = "Integer32"
_MsanShMCEventClass_Object = MibTableColumn
msanShMCEventClass = _MsanShMCEventClass_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 4),
    _MsanShMCEventClass_Type()
)
msanShMCEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventClass.setStatus("current")


class _MsanShMCEventType_Type(Integer32):
    """Custom type msanShMCEventType based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("aboveUpperCritical", 2),
          ("aboveUpperNonCritical", 3),
          ("aboveUpperNonRecoverable", 1),
          ("activated", 8),
          ("belowLowerCritical", 5),
          ("belowLowerNonCritical", 6),
          ("belowLowerNonrecoverable", 4),
          ("communicationLost", 9),
          ("communicationRestored", 10),
          ("deactivated", 11),
          ("extracted", 12),
          ("inserted", 7),
          ("other", 0),
          ("powerDegrade", 13),
          ("powerFail", 14),
          ("powerInhibit", 15))
    )


_MsanShMCEventType_Type.__name__ = "Integer32"
_MsanShMCEventType_Object = MibTableColumn
msanShMCEventType = _MsanShMCEventType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 5),
    _MsanShMCEventType_Type()
)
msanShMCEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventType.setStatus("current")


class _MsanShMCEventAsserted_Type(Integer32):
    """Custom type msanShMCEventAsserted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("asserted", 1),
          ("deasserted", 0))
    )


_MsanShMCEventAsserted_Type.__name__ = "Integer32"
_MsanShMCEventAsserted_Object = MibTableColumn
msanShMCEventAsserted = _MsanShMCEventAsserted_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 6),
    _MsanShMCEventAsserted_Type()
)
msanShMCEventAsserted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventAsserted.setStatus("current")


class _MsanShMCEventOriginSiteType_Type(Integer32):
    """Custom type msanShMCEventOriginSiteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCEventOriginSiteType_Type.__name__ = "Integer32"
_MsanShMCEventOriginSiteType_Object = MibTableColumn
msanShMCEventOriginSiteType = _MsanShMCEventOriginSiteType_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 7),
    _MsanShMCEventOriginSiteType_Type()
)
msanShMCEventOriginSiteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventOriginSiteType.setStatus("current")


class _MsanShMCEventOriginSiteNumber_Type(Integer32):
    """Custom type msanShMCEventOriginSiteNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCEventOriginSiteNumber_Type.__name__ = "Integer32"
_MsanShMCEventOriginSiteNumber_Object = MibTableColumn
msanShMCEventOriginSiteNumber = _MsanShMCEventOriginSiteNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 8),
    _MsanShMCEventOriginSiteNumber_Type()
)
msanShMCEventOriginSiteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventOriginSiteNumber.setStatus("current")


class _MsanShMCEventOriginSlaveAddress_Type(Integer32):
    """Custom type msanShMCEventOriginSlaveAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCEventOriginSlaveAddress_Type.__name__ = "Integer32"
_MsanShMCEventOriginSlaveAddress_Object = MibTableColumn
msanShMCEventOriginSlaveAddress = _MsanShMCEventOriginSlaveAddress_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 9),
    _MsanShMCEventOriginSlaveAddress_Type()
)
msanShMCEventOriginSlaveAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventOriginSlaveAddress.setStatus("current")


class _MsanShMCEventOriginFruId_Type(Integer32):
    """Custom type msanShMCEventOriginFruId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCEventOriginFruId_Type.__name__ = "Integer32"
_MsanShMCEventOriginFruId_Object = MibTableColumn
msanShMCEventOriginFruId = _MsanShMCEventOriginFruId_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 10),
    _MsanShMCEventOriginFruId_Type()
)
msanShMCEventOriginFruId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventOriginFruId.setStatus("current")


class _MsanShMCEventOriginSensorNumber_Type(Integer32):
    """Custom type msanShMCEventOriginSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MsanShMCEventOriginSensorNumber_Type.__name__ = "Integer32"
_MsanShMCEventOriginSensorNumber_Object = MibTableColumn
msanShMCEventOriginSensorNumber = _MsanShMCEventOriginSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 37, 1, 11),
    _MsanShMCEventOriginSensorNumber_Type()
)
msanShMCEventOriginSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    msanShMCEventOriginSensorNumber.setStatus("current")
_MsanShMCGlobal_ObjectIdentity = ObjectIdentity
msanShMCGlobal = _MsanShMCGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 38)
)


class _MsanShMCSelectivePowerOffAdminMode_Type(Integer32):
    """Custom type msanShMCSelectivePowerOffAdminMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_MsanShMCSelectivePowerOffAdminMode_Type.__name__ = "Integer32"
_MsanShMCSelectivePowerOffAdminMode_Object = MibScalar
msanShMCSelectivePowerOffAdminMode = _MsanShMCSelectivePowerOffAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 38, 1),
    _MsanShMCSelectivePowerOffAdminMode_Type()
)
msanShMCSelectivePowerOffAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanShMCSelectivePowerOffAdminMode.setStatus("current")


class _MsanSHMCSelectivePowerOffOffDelay_Type(Integer32):
    """Custom type msanSHMCSelectivePowerOffOffDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MsanSHMCSelectivePowerOffOffDelay_Type.__name__ = "Integer32"
_MsanSHMCSelectivePowerOffOffDelay_Object = MibScalar
msanSHMCSelectivePowerOffOffDelay = _MsanSHMCSelectivePowerOffOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 38, 2),
    _MsanSHMCSelectivePowerOffOffDelay_Type()
)
msanSHMCSelectivePowerOffOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSHMCSelectivePowerOffOffDelay.setStatus("current")
if mibBuilder.loadTexts:
    msanSHMCSelectivePowerOffOffDelay.setUnits("minutes")


class _MsanSHMCSelectivePowerOffOnDelay_Type(Integer32):
    """Custom type msanSHMCSelectivePowerOffOnDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MsanSHMCSelectivePowerOffOnDelay_Type.__name__ = "Integer32"
_MsanSHMCSelectivePowerOffOnDelay_Object = MibScalar
msanSHMCSelectivePowerOffOnDelay = _MsanSHMCSelectivePowerOffOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 1332, 1, 1, 5, 3, 33, 38, 3),
    _MsanSHMCSelectivePowerOffOnDelay_Type()
)
msanSHMCSelectivePowerOffOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    msanSHMCSelectivePowerOffOnDelay.setStatus("current")
if mibBuilder.loadTexts:
    msanSHMCSelectivePowerOffOnDelay.setUnits("minutes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISKRATEL-IPMI-MIB",
    **{"msanShMC": msanShMC,
       "msanShMCImpControllerVariablesTable": msanShMCImpControllerVariablesTable,
       "msanShMCImpControllerVariablesEntry": msanShMCImpControllerVariablesEntry,
       "msanShMCImpControllerIndex": msanShMCImpControllerIndex,
       "msanShMCImpControllerSdrVersion": msanShMCImpControllerSdrVersion,
       "msanShMCImpControllerPicmgVersion": msanShMCImpControllerPicmgVersion,
       "msanShMCImpControllerSlaveAddress": msanShMCImpControllerSlaveAddress,
       "msanShMCImpControllerChannelNumber": msanShMCImpControllerChannelNumber,
       "msanShMCImpControllerPowerStateNotification": msanShMCImpControllerPowerStateNotification,
       "msanShMCImpControllerGlobalInitialisation": msanShMCImpControllerGlobalInitialisation,
       "msanShMCImpControllerCapabilities": msanShMCImpControllerCapabilities,
       "msanShMCImpControllerIdString": msanShMCImpControllerIdString,
       "msanShMCImpControllerMaximumFru": msanShMCImpControllerMaximumFru,
       "msanShMCImpControllerOwnFruId": msanShMCImpControllerOwnFruId,
       "msanShMCFruDeviceVariablesTable": msanShMCFruDeviceVariablesTable,
       "msanShMCFruDeviceVariablesEntry": msanShMCFruDeviceVariablesEntry,
       "msanShMCFruDeviceIndex": msanShMCFruDeviceIndex,
       "msanShMCFruDeviceSdrVersion": msanShMCFruDeviceSdrVersion,
       "msanShMCFruDeviceSlaveAddress": msanShMCFruDeviceSlaveAddress,
       "msanShMCFruDeviceSFruDeviceId": msanShMCFruDeviceSFruDeviceId,
       "msanShMCFruDeviceChannelNumber": msanShMCFruDeviceChannelNumber,
       "msanShMCFruDeviceDeviceType": msanShMCFruDeviceDeviceType,
       "msanShMCFruDeviceDeviceTypeModifier": msanShMCFruDeviceDeviceTypeModifier,
       "msanShMCFruDeviceFruEntityId": msanShMCFruDeviceFruEntityId,
       "msanShMCFruDeviceFruEntityInstance": msanShMCFruDeviceFruEntityInstance,
       "msanShMCFruDeviceIdString": msanShMCFruDeviceIdString,
       "msanShMCFruDeviceHotSwapState": msanShMCFruDeviceHotSwapState,
       "msanShMCFruDeviceActivated": msanShMCFruDeviceActivated,
       "msanShMCSensorVariablesTable": msanShMCSensorVariablesTable,
       "msanShMCSensorVariablesEntry": msanShMCSensorVariablesEntry,
       "msanShMCSensorIndex": msanShMCSensorIndex,
       "msanShMCSensorSdrVersion": msanShMCSensorSdrVersion,
       "msanShMCSensorRecordType": msanShMCSensorRecordType,
       "msanShMCSensorOwnerId": msanShMCSensorOwnerId,
       "msanShMCSensorOwnerLun": msanShMCSensorOwnerLun,
       "msanShMCSensorNumber": msanShMCSensorNumber,
       "msanShMCSensorEntityInstance": msanShMCSensorEntityInstance,
       "msanShMCSensorEntityId": msanShMCSensorEntityId,
       "msanShMCSensorInitialisation": msanShMCSensorInitialisation,
       "msanShMCSensorCapabilities": msanShMCSensorCapabilities,
       "msanShMCSensorType": msanShMCSensorType,
       "msanShMCSensorEvent": msanShMCSensorEvent,
       "msanShMCSensorAssertionEventMask": msanShMCSensorAssertionEventMask,
       "msanShMCSensorDeassertionEventMask": msanShMCSensorDeassertionEventMask,
       "msanShMCSensorMask": msanShMCSensorMask,
       "msanShMCSensorUnit1": msanShMCSensorUnit1,
       "msanShMCSensorUnit2": msanShMCSensorUnit2,
       "msanShMCSensorUnit3": msanShMCSensorUnit3,
       "msanShMCSensorLinearization": msanShMCSensorLinearization,
       "msanShMCSensorM": msanShMCSensorM,
       "msanShMCSensorTolerance": msanShMCSensorTolerance,
       "msanShMCSensorB": msanShMCSensorB,
       "msanShMCSensorAccuracy": msanShMCSensorAccuracy,
       "msanShMCSensorAccuracyExp": msanShMCSensorAccuracyExp,
       "msanShMCSensorRexp": msanShMCSensorRexp,
       "msanShMCSensorBexp": msanShMCSensorBexp,
       "msanShMCSensorCharacteristicFlags": msanShMCSensorCharacteristicFlags,
       "msanShMCSensorReading": msanShMCSensorReading,
       "msanShMCSensorProcessedReading": msanShMCSensorProcessedReading,
       "msanShMCSensorNominalReading": msanShMCSensorNominalReading,
       "msanShMCSensorNormalMaximum": msanShMCSensorNormalMaximum,
       "msanShMCSensorNormalMinimum": msanShMCSensorNormalMinimum,
       "msanShMCSensorMaximumReading": msanShMCSensorMaximumReading,
       "msanShMCSensorMinimumReading": msanShMCSensorMinimumReading,
       "msanShMCSensorUpperNonRecoverableThr": msanShMCSensorUpperNonRecoverableThr,
       "msanShMCSensorUpperCriticalThr": msanShMCSensorUpperCriticalThr,
       "msanShMCSensorUpperNonCriticalThr": msanShMCSensorUpperNonCriticalThr,
       "msanShMCSensorLowerNonRecoverableThr": msanShMCSensorLowerNonRecoverableThr,
       "msanShMCSensorLowerCriticalThr": msanShMCSensorLowerCriticalThr,
       "msanShMCSensorLowerNonCriticalThr": msanShMCSensorLowerNonCriticalThr,
       "msanShMCSensorPositiveGoingThrHysteresis": msanShMCSensorPositiveGoingThrHysteresis,
       "msanShMCSensorNegativeGoingThrHysteresis": msanShMCSensorNegativeGoingThrHysteresis,
       "msanShMCSensorIdString": msanShMCSensorIdString,
       "msanShMCSensorEntireSensorData": msanShMCSensorEntireSensorData,
       "msanShMCBoardsTable": msanShMCBoardsTable,
       "msanShMCBoardsEntry": msanShMCBoardsEntry,
       "msanShMCBoardsIndex": msanShMCBoardsIndex,
       "msanShMCBoardsBoardBasicPresent": msanShMCBoardsBoardBasicPresent,
       "msanShMCBoardsBoardBasicHealthy": msanShMCBoardsBoardBasicHealthy,
       "msanShMCBoardsBoardBasicReset": msanShMCBoardsBoardBasicReset,
       "msanShMCBoardsBoardBasicSlaveAddress": msanShMCBoardsBoardBasicSlaveAddress,
       "msanShMCBoardsBoardBasicFruDeviceId": msanShMCBoardsBoardBasicFruDeviceId,
       "msanShMCSelTable": msanShMCSelTable,
       "msanShMCSelEntry": msanShMCSelEntry,
       "msanShMCSelIndex": msanShMCSelIndex,
       "msanShMCSelcontents": msanShMCSelcontents,
       "msanShMCShelfTable": msanShMCShelfTable,
       "msanShMCShelfEntry": msanShMCShelfEntry,
       "msanShMCShelfIndex": msanShMCShelfIndex,
       "msanShMCShelfHealthy": msanShMCShelfHealthy,
       "msanShMCPefConfiguration": msanShMCPefConfiguration,
       "msanShMCPefConfigurationSetInProgress": msanShMCPefConfigurationSetInProgress,
       "msanShMCPefConfigurationControl": msanShMCPefConfigurationControl,
       "msanShMCPefConfigurationActionGlobalControl": msanShMCPefConfigurationActionGlobalControl,
       "msanShMCPefConfigurationStartupDelay": msanShMCPefConfigurationStartupDelay,
       "msanShMCPefConfigurationAlertStartupDelay": msanShMCPefConfigurationAlertStartupDelay,
       "msanShMCPefConfigurationNumberOfEventFilters": msanShMCPefConfigurationNumberOfEventFilters,
       "msanShMCPefConfigurationNumberOfAlertPoliciEntries": msanShMCPefConfigurationNumberOfAlertPoliciEntries,
       "msanShMCPefConfigurationSystemGuid": msanShMCPefConfigurationSystemGuid,
       "msanShMCPefConfigurationNumberOfAlertStrings": msanShMCPefConfigurationNumberOfAlertStrings,
       "msanShMCPefConfigurationEventFilterTable": msanShMCPefConfigurationEventFilterTable,
       "msanShMCPefConfigurationEventFilterEntry": msanShMCPefConfigurationEventFilterEntry,
       "msanShMCPefConfigurationEventFilterIndex": msanShMCPefConfigurationEventFilterIndex,
       "msanShMCPefConfigurationEventFilterData": msanShMCPefConfigurationEventFilterData,
       "msanShMCPefConfigurationAlertStringTable": msanShMCPefConfigurationAlertStringTable,
       "msanShMCPefConfigurationAlertStringEntry": msanShMCPefConfigurationAlertStringEntry,
       "msanShMCPefConfigurationAlertStringIndex": msanShMCPefConfigurationAlertStringIndex,
       "msanShMCPefConfigurationAlertStringKey": msanShMCPefConfigurationAlertStringKey,
       "msanShMCPefConfigurationAlertString": msanShMCPefConfigurationAlertString,
       "msanShMCFruInfoTable": msanShMCFruInfoTable,
       "msanShMCFruInfoEntry": msanShMCFruInfoEntry,
       "msanShMCFruInfoIndex": msanShMCFruInfoIndex,
       "msanShMCFruInfoData": msanShMCFruInfoData,
       "msanShMCFruInfoDataWo": msanShMCFruInfoDataWo,
       "msanShMCBoardVariablesTable": msanShMCBoardVariablesTable,
       "msanShMCBoardVariablesEntry": msanShMCBoardVariablesEntry,
       "msanShMCBoardVariablesBoardBasicSlotNumber": msanShMCBoardVariablesBoardBasicSlotNumber,
       "msanShMCBoardVariablesBoardBasicPresent": msanShMCBoardVariablesBoardBasicPresent,
       "msanShMCBoardVariablesBoardBasicHealthy": msanShMCBoardVariablesBoardBasicHealthy,
       "msanShMCBoardVariablesBoardBasicReset": msanShMCBoardVariablesBoardBasicReset,
       "msanShMCBoardVariablesBoardBasicPowered": msanShMCBoardVariablesBoardBasicPowered,
       "msanShMCBoardVariablesBoardBasicSlaveAddress": msanShMCBoardVariablesBoardBasicSlaveAddress,
       "msanShMCBoardVariablesBoardBasicFruDeviceId": msanShMCBoardVariablesBoardBasicFruDeviceId,
       "msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent": msanShMCBoardVariablesBoardBasicFruinfoProductAreaPresent,
       "msanShMCBoardVariablesBoardBasicProductManufacturer": msanShMCBoardVariablesBoardBasicProductManufacturer,
       "msanShMCBoardVariablesBoardBasicProductName": msanShMCBoardVariablesBoardBasicProductName,
       "msanShMCBoardVariablesBoardBasicProductPartModelNumber": msanShMCBoardVariablesBoardBasicProductPartModelNumber,
       "msanShMCBoardVariablesBoardBasicProductVersionNumber": msanShMCBoardVariablesBoardBasicProductVersionNumber,
       "msanShMCBoardVariablesBoardBasicProductSerialNumber": msanShMCBoardVariablesBoardBasicProductSerialNumber,
       "msanShMCBoardVariablesBoardBasicBoardAreaPresent": msanShMCBoardVariablesBoardBasicBoardAreaPresent,
       "msanShMCBoardVariablesBoardBasicBoardManufacturer": msanShMCBoardVariablesBoardBasicBoardManufacturer,
       "msanShMCBoardVariablesBoardBasicBoardProductName": msanShMCBoardVariablesBoardBasicBoardProductName,
       "msanShMCBoardVariablesBoardBasicBoardSerialNumber": msanShMCBoardVariablesBoardBasicBoardSerialNumber,
       "msanShMCBoardVariablesBoardBasicBoardPartNumber": msanShMCBoardVariablesBoardBasicBoardPartNumber,
       "msanShMCBoardVariablesBoardBasicBoardManufactureTime": msanShMCBoardVariablesBoardBasicBoardManufactureTime,
       "msanShMCBoardVariablesSelectivePowerOffSwitchOffType": msanShMCBoardVariablesSelectivePowerOffSwitchOffType,
       "msanShMCFanTrayVariablesTable": msanShMCFanTrayVariablesTable,
       "msanShMCFanTrayVariablesEntry": msanShMCFanTrayVariablesEntry,
       "msanShMCFanTraySlotNumber": msanShMCFanTraySlotNumber,
       "msanShMCFanTrayPresent": msanShMCFanTrayPresent,
       "msanShMCFanTrayHealthy": msanShMCFanTrayHealthy,
       "msanShMCFanTrayHealthLed": msanShMCFanTrayHealthLed,
       "msanShMCFanTraySlaveAddress": msanShMCFanTraySlaveAddress,
       "msanShMCFanTrayFruDeviceId": msanShMCFanTrayFruDeviceId,
       "msanShMCFanTrayFruinfoProductAreaPresent": msanShMCFanTrayFruinfoProductAreaPresent,
       "msanShMCFanTrayFruinfoProductManufacturer": msanShMCFanTrayFruinfoProductManufacturer,
       "msanShMCFanTrayFruinfoProductName": msanShMCFanTrayFruinfoProductName,
       "msanShMCFanTrayFruinfoProductPartModelNumber": msanShMCFanTrayFruinfoProductPartModelNumber,
       "msanShMCFanTrayFruinfoProductVersionNumber": msanShMCFanTrayFruinfoProductVersionNumber,
       "msanShMCFanTrayFruinfoProductSerialNumber": msanShMCFanTrayFruinfoProductSerialNumber,
       "msanShMCFanTrayFruinfoBoardAreaPresent": msanShMCFanTrayFruinfoBoardAreaPresent,
       "msanShMCFanTrayFruinfoBoardManufacturer": msanShMCFanTrayFruinfoBoardManufacturer,
       "msanShMCFanTrayFruinfoBoardProductName": msanShMCFanTrayFruinfoBoardProductName,
       "msanShMCFanTrayFruinfoBoardSerialNumber": msanShMCFanTrayFruinfoBoardSerialNumber,
       "msanShMCFanTrayFruinfoBoardPartNumber": msanShMCFanTrayFruinfoBoardPartNumber,
       "msanShMCFanTrayFruinfoBoardManufactureTime": msanShMCFanTrayFruinfoBoardManufactureTime,
       "msanShMCPowerSupplyVariablesTable": msanShMCPowerSupplyVariablesTable,
       "msanShMCPowerSupplyVariablesEntry": msanShMCPowerSupplyVariablesEntry,
       "msanShMCPowerSupplySlotNumber": msanShMCPowerSupplySlotNumber,
       "msanShMCPowerSupplyDegrade": msanShMCPowerSupplyDegrade,
       "msanShMCPowerSupplyFail": msanShMCPowerSupplyFail,
       "msanShMCPowerSupplyInhibit": msanShMCPowerSupplyInhibit,
       "msanShMCPowerSupplyHealthy": msanShMCPowerSupplyHealthy,
       "msanShMCPowerSupplySlaveAddress": msanShMCPowerSupplySlaveAddress,
       "msanShMCPowerSupplyFruDeviceId": msanShMCPowerSupplyFruDeviceId,
       "msanShMCPowerSupplyFruinfoProductAreaPresent": msanShMCPowerSupplyFruinfoProductAreaPresent,
       "msanShMCPowerSupplyFruinfoProductManufacturer": msanShMCPowerSupplyFruinfoProductManufacturer,
       "msanShMCPowerSupplyFruinfoProductName": msanShMCPowerSupplyFruinfoProductName,
       "msanShMCPowerSupplyFruinfoProductPartModelNumber": msanShMCPowerSupplyFruinfoProductPartModelNumber,
       "msanShMCPowerSupplyFruinfoProductVersionNumber": msanShMCPowerSupplyFruinfoProductVersionNumber,
       "msanShMCPowerSupplyFruinfoProductSerialNumber": msanShMCPowerSupplyFruinfoProductSerialNumber,
       "msanShMCPowerSupplyFruinfoBoardAreaPresent": msanShMCPowerSupplyFruinfoBoardAreaPresent,
       "msanShMCPowerSupplyFruinfoBoardManufacturer": msanShMCPowerSupplyFruinfoBoardManufacturer,
       "msanShMCPowerSupplyFruinfoBoardProductName": msanShMCPowerSupplyFruinfoBoardProductName,
       "msanShMCPowerSupplyFruinfoBoardSerialNumber": msanShMCPowerSupplyFruinfoBoardSerialNumber,
       "msanShMCPowerSupplyFruinfoBoardPartNumber": msanShMCPowerSupplyFruinfoBoardPartNumber,
       "msanShMCPowerSupplyFruinfoBoardmanufactureTime": msanShMCPowerSupplyFruinfoBoardmanufactureTime,
       "msanShMCShelfManagerVariablesTable": msanShMCShelfManagerVariablesTable,
       "msanShMCShelfManagerVariablesEntry": msanShMCShelfManagerVariablesEntry,
       "msanShMCShelfManagerSlotNumber": msanShMCShelfManagerSlotNumber,
       "msanShMCShelfManagerSlaveAddress": msanShMCShelfManagerSlaveAddress,
       "msanShMCShelfManagerPresent": msanShMCShelfManagerPresent,
       "msanShMCShelfManagerHealthy": msanShMCShelfManagerHealthy,
       "msanShMCShelfManagerActive": msanShMCShelfManagerActive,
       "msanShMCShelfManagerReset": msanShMCShelfManagerReset,
       "msanShMCShelfManagerFruinfoProductAreaPresent": msanShMCShelfManagerFruinfoProductAreaPresent,
       "msanShMCShelfManagerFruinfoProductManufacturer": msanShMCShelfManagerFruinfoProductManufacturer,
       "msanShMCShelfManagerFruinfoProductName": msanShMCShelfManagerFruinfoProductName,
       "msanShMCShelfManagerFruinfoProductPartModelNumber": msanShMCShelfManagerFruinfoProductPartModelNumber,
       "msanShMCShelfManagerFruinfoProductVersionNumber": msanShMCShelfManagerFruinfoProductVersionNumber,
       "msanShMCShelfManagerFruinfoProductSerialNumber": msanShMCShelfManagerFruinfoProductSerialNumber,
       "msanShMCShelfManagerFruinfoBoardAreaPresent": msanShMCShelfManagerFruinfoBoardAreaPresent,
       "msanShMCShelfManagerFruinfoBoardManufacturer": msanShMCShelfManagerFruinfoBoardManufacturer,
       "msanShMCShelfManagerFruinfoBoardProductName": msanShMCShelfManagerFruinfoBoardProductName,
       "msanShMCShelfManagerFruinfoBoardSerialNumber": msanShMCShelfManagerFruinfoBoardSerialNumber,
       "msanShMCShelfManagerFruinfoBoardPartNumber": msanShMCShelfManagerFruinfoBoardPartNumber,
       "msanShMCShelfManagerFruinfoBoardmanufactureTime": msanShMCShelfManagerFruinfoBoardmanufactureTime,
       "msanShMCChassisVariablesTable": msanShMCChassisVariablesTable,
       "msanShMCChassisVariablesEntry": msanShMCChassisVariablesEntry,
       "msanShMCChassisId": msanShMCChassisId,
       "msanShMCChassisType": msanShMCChassisType,
       "msanShMCChassisPartNumber": msanShMCChassisPartNumber,
       "msanShMCChassisSerialNumber": msanShMCChassisSerialNumber,
       "msanShMCChassisProductAreaPresent": msanShMCChassisProductAreaPresent,
       "msanShMCChassisProductManufacturer": msanShMCChassisProductManufacturer,
       "msanShMCChassisProductName": msanShMCChassisProductName,
       "msanShMCChassisProductPartModelNumber": msanShMCChassisProductPartModelNumber,
       "msanShMCChassisProductVersionNumber": msanShMCChassisProductVersionNumber,
       "msanShMCChassisProductSerialNumber": msanShMCChassisProductSerialNumber,
       "msanShMCChassisBoardAreaPresent": msanShMCChassisBoardAreaPresent,
       "msanShMCChassisBoardManufacturer": msanShMCChassisBoardManufacturer,
       "msanShMCChassisBoardProductName": msanShMCChassisBoardProductName,
       "msanShMCChassisBoardSerialNumber": msanShMCChassisBoardSerialNumber,
       "msanShMCChassisBoardPartNumber": msanShMCChassisBoardPartNumber,
       "msanShMCChassisBoardmanufactureTime": msanShMCChassisBoardmanufactureTime,
       "msanShMCEventVariablesTable": msanShMCEventVariablesTable,
       "msanShMCEventVariablesEntry": msanShMCEventVariablesEntry,
       "msanShMCEventIndex": msanShMCEventIndex,
       "msanShMCEventDelete": msanShMCEventDelete,
       "msanShMCEventTimeStamp": msanShMCEventTimeStamp,
       "msanShMCEventClass": msanShMCEventClass,
       "msanShMCEventType": msanShMCEventType,
       "msanShMCEventAsserted": msanShMCEventAsserted,
       "msanShMCEventOriginSiteType": msanShMCEventOriginSiteType,
       "msanShMCEventOriginSiteNumber": msanShMCEventOriginSiteNumber,
       "msanShMCEventOriginSlaveAddress": msanShMCEventOriginSlaveAddress,
       "msanShMCEventOriginFruId": msanShMCEventOriginFruId,
       "msanShMCEventOriginSensorNumber": msanShMCEventOriginSensorNumber,
       "msanShMCGlobal": msanShMCGlobal,
       "msanShMCSelectivePowerOffAdminMode": msanShMCSelectivePowerOffAdminMode,
       "msanSHMCSelectivePowerOffOffDelay": msanSHMCSelectivePowerOffOffDelay,
       "msanSHMCSelectivePowerOffOnDelay": msanSHMCSelectivePowerOffOnDelay}
)
