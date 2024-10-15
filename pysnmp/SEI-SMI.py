# SNMP MIB module (SEI-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SEI-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:50:18 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

sei = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 20364)
)
sei.setRevisions(
        ("2004-06-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuiceBoxPse_ObjectIdentity = ObjectIdentity
juiceBoxPse = _JuiceBoxPse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20364, 1)
)
_JuiceBoxObjects_ObjectIdentity = ObjectIdentity
juiceBoxObjects = _JuiceBoxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1)
)
_JuiceBoxPortTable_Object = MibTable
juiceBoxPortTable = _JuiceBoxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juiceBoxPortTable.setStatus("current")
_JuiceBoxPortEntry_Object = MibTableRow
juiceBoxPortEntry = _JuiceBoxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1)
)
juiceBoxPortEntry.setIndexNames(
    (0, "SEI-SMI", "juiceBoxPortIndex"),
)
if mibBuilder.loadTexts:
    juiceBoxPortEntry.setStatus("current")


class _JuiceBoxPortIndex_Type(Integer32):
    """Custom type juiceBoxPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuiceBoxPortIndex_Type.__name__ = "Integer32"
_JuiceBoxPortIndex_Object = MibTableColumn
juiceBoxPortIndex = _JuiceBoxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1, 1),
    _JuiceBoxPortIndex_Type()
)
juiceBoxPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juiceBoxPortIndex.setStatus("current")


class _JuiceBoxPortDetectionSetting_Type(Integer32):
    """Custom type juiceBoxPortDetectionSetting based on Integer32"""
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
        *(("disabled", 1),
          ("forcedon", 4),
          ("ieee8023afandlegacy", 3),
          ("ieee8023afonly", 2))
    )


_JuiceBoxPortDetectionSetting_Type.__name__ = "Integer32"
_JuiceBoxPortDetectionSetting_Object = MibTableColumn
juiceBoxPortDetectionSetting = _JuiceBoxPortDetectionSetting_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1, 2),
    _JuiceBoxPortDetectionSetting_Type()
)
juiceBoxPortDetectionSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxPortDetectionSetting.setStatus("current")


class _JuiceBoxPortMaxPower_Type(Integer32):
    """Custom type juiceBoxPortMaxPower based on Integer32"""
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
        *(("max10W", 10),
          ("max11W", 11),
          ("max12W", 12),
          ("max13W", 13),
          ("max14W", 14),
          ("max15W", 15),
          ("max1W", 1),
          ("max2W", 2),
          ("max3W", 3),
          ("max4W", 4),
          ("max5W", 5),
          ("max6W", 6),
          ("max7W", 7),
          ("max8W", 8),
          ("max9W", 9))
    )


_JuiceBoxPortMaxPower_Type.__name__ = "Integer32"
_JuiceBoxPortMaxPower_Object = MibTableColumn
juiceBoxPortMaxPower = _JuiceBoxPortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1, 3),
    _JuiceBoxPortMaxPower_Type()
)
juiceBoxPortMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxPortMaxPower.setStatus("current")
_JuiceBoxPortDescription_Type = SnmpAdminString
_JuiceBoxPortDescription_Object = MibTableColumn
juiceBoxPortDescription = _JuiceBoxPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1, 4),
    _JuiceBoxPortDescription_Type()
)
juiceBoxPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxPortDescription.setStatus("current")


class _JuiceBoxPortStatus_Type(Integer32):
    """Custom type juiceBoxPortStatus based on Integer32"""
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
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("deliveringPower", 2),
          ("disabled", 1),
          ("disconnect", 10),
          ("insufficientPower", 15),
          ("invalidDetect", 9),
          ("open", 6),
          ("overCurrentFault", 4),
          ("overPowerFault", 14),
          ("overPowerWarning", 13),
          ("powerup", 12),
          ("rsignatureHi", 7),
          ("rsignatureLow", 8),
          ("short", 5),
          ("startupFault", 3))
    )


_JuiceBoxPortStatus_Type.__name__ = "Integer32"
_JuiceBoxPortStatus_Object = MibTableColumn
juiceBoxPortStatus = _JuiceBoxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1, 5),
    _JuiceBoxPortStatus_Type()
)
juiceBoxPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxPortStatus.setStatus("current")


class _JuiceBoxPortClassifications_Type(Integer32):
    """Custom type juiceBoxPortClassifications based on Integer32"""
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
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("legacy", 6))
    )


_JuiceBoxPortClassifications_Type.__name__ = "Integer32"
_JuiceBoxPortClassifications_Object = MibTableColumn
juiceBoxPortClassifications = _JuiceBoxPortClassifications_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1, 6),
    _JuiceBoxPortClassifications_Type()
)
juiceBoxPortClassifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxPortClassifications.setStatus("current")
_JuiceBoxPortPowerDelivered_Type = Gauge32
_JuiceBoxPortPowerDelivered_Object = MibTableColumn
juiceBoxPortPowerDelivered = _JuiceBoxPortPowerDelivered_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 1, 1, 7),
    _JuiceBoxPortPowerDelivered_Type()
)
juiceBoxPortPowerDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxPortPowerDelivered.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxPortPowerDelivered.setUnits("milliWatts")
_JuiceBoxMainObjects_ObjectIdentity = ObjectIdentity
juiceBoxMainObjects = _JuiceBoxMainObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2)
)
_JuiceBoxMainSystemVoltage_Type = Gauge32
_JuiceBoxMainSystemVoltage_Object = MibScalar
juiceBoxMainSystemVoltage = _JuiceBoxMainSystemVoltage_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 1),
    _JuiceBoxMainSystemVoltage_Type()
)
juiceBoxMainSystemVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxMainSystemVoltage.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxMainSystemVoltage.setUnits("milliVolts")
_JuiceBoxMainTemperature_Type = Gauge32
_JuiceBoxMainTemperature_Object = MibScalar
juiceBoxMainTemperature = _JuiceBoxMainTemperature_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 2),
    _JuiceBoxMainTemperature_Type()
)
juiceBoxMainTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxMainTemperature.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxMainTemperature.setUnits("degrees C")


class _JuiceBoxMainPowerAvailable_Type(Gauge32):
    """Custom type juiceBoxMainPowerAvailable based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuiceBoxMainPowerAvailable_Type.__name__ = "Gauge32"
_JuiceBoxMainPowerAvailable_Object = MibScalar
juiceBoxMainPowerAvailable = _JuiceBoxMainPowerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 3),
    _JuiceBoxMainPowerAvailable_Type()
)
juiceBoxMainPowerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxMainPowerAvailable.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxMainPowerAvailable.setUnits("Watts")
_JuiceBoxMainPowerDelivered_Type = Gauge32
_JuiceBoxMainPowerDelivered_Object = MibScalar
juiceBoxMainPowerDelivered = _JuiceBoxMainPowerDelivered_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 4),
    _JuiceBoxMainPowerDelivered_Type()
)
juiceBoxMainPowerDelivered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxMainPowerDelivered.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxMainPowerDelivered.setUnits("Watts")
_JuiceBoxMainAllocatedPower_Type = Gauge32
_JuiceBoxMainAllocatedPower_Object = MibScalar
juiceBoxMainAllocatedPower = _JuiceBoxMainAllocatedPower_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 5),
    _JuiceBoxMainAllocatedPower_Type()
)
juiceBoxMainAllocatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxMainAllocatedPower.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxMainAllocatedPower.setUnits("Watts")


class _JuiceBoxMainAllocatedPowerThreshold_Type(Integer32):
    """Custom type juiceBoxMainAllocatedPowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_JuiceBoxMainAllocatedPowerThreshold_Type.__name__ = "Integer32"
_JuiceBoxMainAllocatedPowerThreshold_Object = MibScalar
juiceBoxMainAllocatedPowerThreshold = _JuiceBoxMainAllocatedPowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 6),
    _JuiceBoxMainAllocatedPowerThreshold_Type()
)
juiceBoxMainAllocatedPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxMainAllocatedPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxMainAllocatedPowerThreshold.setUnits("%")
_JuiceBoxMainTrapDestinationIPAddr_Type = IpAddress
_JuiceBoxMainTrapDestinationIPAddr_Object = MibScalar
juiceBoxMainTrapDestinationIPAddr = _JuiceBoxMainTrapDestinationIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 7),
    _JuiceBoxMainTrapDestinationIPAddr_Type()
)
juiceBoxMainTrapDestinationIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxMainTrapDestinationIPAddr.setStatus("current")


class _JuiceBoxMainTrapReXmitPeriod_Type(Integer32):
    """Custom type juiceBoxMainTrapReXmitPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuiceBoxMainTrapReXmitPeriod_Type.__name__ = "Integer32"
_JuiceBoxMainTrapReXmitPeriod_Object = MibScalar
juiceBoxMainTrapReXmitPeriod = _JuiceBoxMainTrapReXmitPeriod_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 8),
    _JuiceBoxMainTrapReXmitPeriod_Type()
)
juiceBoxMainTrapReXmitPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxMainTrapReXmitPeriod.setStatus("current")
if mibBuilder.loadTexts:
    juiceBoxMainTrapReXmitPeriod.setUnits("seconds")


class _JuiceBoxMainGlobalPortDetectionSetting_Type(Integer32):
    """Custom type juiceBoxMainGlobalPortDetectionSetting based on Integer32"""
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
        *(("disabled", 1),
          ("forcedon", 4),
          ("ieee8023afandlegacy", 3),
          ("ieee8023afonly", 2))
    )


_JuiceBoxMainGlobalPortDetectionSetting_Type.__name__ = "Integer32"
_JuiceBoxMainGlobalPortDetectionSetting_Object = MibScalar
juiceBoxMainGlobalPortDetectionSetting = _JuiceBoxMainGlobalPortDetectionSetting_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 9),
    _JuiceBoxMainGlobalPortDetectionSetting_Type()
)
juiceBoxMainGlobalPortDetectionSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxMainGlobalPortDetectionSetting.setStatus("current")


class _JuiceBoxMainGlobalPortMaxPower_Type(Integer32):
    """Custom type juiceBoxMainGlobalPortMaxPower based on Integer32"""
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
        *(("max10W", 10),
          ("max11W", 11),
          ("max12W", 12),
          ("max13W", 13),
          ("max14W", 14),
          ("max15W", 15),
          ("max1W", 1),
          ("max2W", 2),
          ("max3W", 3),
          ("max4W", 4),
          ("max5W", 5),
          ("max6W", 6),
          ("max7W", 7),
          ("max8W", 8),
          ("max9W", 9))
    )


_JuiceBoxMainGlobalPortMaxPower_Type.__name__ = "Integer32"
_JuiceBoxMainGlobalPortMaxPower_Object = MibScalar
juiceBoxMainGlobalPortMaxPower = _JuiceBoxMainGlobalPortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 10),
    _JuiceBoxMainGlobalPortMaxPower_Type()
)
juiceBoxMainGlobalPortMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juiceBoxMainGlobalPortMaxPower.setStatus("current")
_JuiceBoxMainNetworkControllerFirmware_Type = SnmpAdminString
_JuiceBoxMainNetworkControllerFirmware_Object = MibScalar
juiceBoxMainNetworkControllerFirmware = _JuiceBoxMainNetworkControllerFirmware_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 11),
    _JuiceBoxMainNetworkControllerFirmware_Type()
)
juiceBoxMainNetworkControllerFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxMainNetworkControllerFirmware.setStatus("current")
_JuiceBoxMainSystemControllerFirmware_Type = SnmpAdminString
_JuiceBoxMainSystemControllerFirmware_Object = MibScalar
juiceBoxMainSystemControllerFirmware = _JuiceBoxMainSystemControllerFirmware_Object(
    (1, 3, 6, 1, 4, 1, 20364, 1, 1, 2, 12),
    _JuiceBoxMainSystemControllerFirmware_Type()
)
juiceBoxMainSystemControllerFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juiceBoxMainSystemControllerFirmware.setStatus("current")

# Managed Objects groups


# Notification objects

juiceBoxAllocatedPowerThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 20364, 0, 10)
)
juiceBoxAllocatedPowerThresholdReached.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SEI-SMI", "juiceBoxMainAllocatedPower"),
        ("SEI-SMI", "juiceBoxMainPowerDelivered"))
)
if mibBuilder.loadTexts:
    juiceBoxAllocatedPowerThresholdReached.setStatus(
        ""
    )

juiceBoxPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 20364, 0, 20)
)
juiceBoxPortStatusChange.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("SEI-SMI", "juiceBoxPortIndex"),
        ("SEI-SMI", "juiceBoxPortStatus"))
)
if mibBuilder.loadTexts:
    juiceBoxPortStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SEI-SMI",
    **{"sei": sei,
       "juiceBoxAllocatedPowerThresholdReached": juiceBoxAllocatedPowerThresholdReached,
       "juiceBoxPortStatusChange": juiceBoxPortStatusChange,
       "juiceBoxPse": juiceBoxPse,
       "juiceBoxObjects": juiceBoxObjects,
       "juiceBoxPortTable": juiceBoxPortTable,
       "juiceBoxPortEntry": juiceBoxPortEntry,
       "juiceBoxPortIndex": juiceBoxPortIndex,
       "juiceBoxPortDetectionSetting": juiceBoxPortDetectionSetting,
       "juiceBoxPortMaxPower": juiceBoxPortMaxPower,
       "juiceBoxPortDescription": juiceBoxPortDescription,
       "juiceBoxPortStatus": juiceBoxPortStatus,
       "juiceBoxPortClassifications": juiceBoxPortClassifications,
       "juiceBoxPortPowerDelivered": juiceBoxPortPowerDelivered,
       "juiceBoxMainObjects": juiceBoxMainObjects,
       "juiceBoxMainSystemVoltage": juiceBoxMainSystemVoltage,
       "juiceBoxMainTemperature": juiceBoxMainTemperature,
       "juiceBoxMainPowerAvailable": juiceBoxMainPowerAvailable,
       "juiceBoxMainPowerDelivered": juiceBoxMainPowerDelivered,
       "juiceBoxMainAllocatedPower": juiceBoxMainAllocatedPower,
       "juiceBoxMainAllocatedPowerThreshold": juiceBoxMainAllocatedPowerThreshold,
       "juiceBoxMainTrapDestinationIPAddr": juiceBoxMainTrapDestinationIPAddr,
       "juiceBoxMainTrapReXmitPeriod": juiceBoxMainTrapReXmitPeriod,
       "juiceBoxMainGlobalPortDetectionSetting": juiceBoxMainGlobalPortDetectionSetting,
       "juiceBoxMainGlobalPortMaxPower": juiceBoxMainGlobalPortMaxPower,
       "juiceBoxMainNetworkControllerFirmware": juiceBoxMainNetworkControllerFirmware,
       "juiceBoxMainSystemControllerFirmware": juiceBoxMainSystemControllerFirmware}
)
