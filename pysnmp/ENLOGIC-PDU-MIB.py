# SNMP MIB module (ENLOGIC-PDU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENLOGIC-PDU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:37 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysContact,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysContact",
    "sysLocation",
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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

enlogic = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38446)
)
enlogic.setRevisions(
        ("2014-10-28 00:00",
         "2014-06-05 00:00",
         "2014-04-30 00:00",
         "2013-06-05 00:00",
         "2013-05-31 00:00",
         "2013-03-28 00:00",
         "2013-03-21 00:00",
         "2013-01-24 00:00",
         "2013-01-06 00:00",
         "2012-12-28 00:00",
         "2012-09-28 00:00",
         "2012-09-25 00:00",
         "2012-09-18 00:00",
         "2012-09-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pdu_ObjectIdentity = ObjectIdentity
pdu = _Pdu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1)
)
_PduNamePlate_ObjectIdentity = ObjectIdentity
pduNamePlate = _PduNamePlate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1)
)


class _PduNamePlateTableSize_Type(Integer32):
    """Custom type pduNamePlateTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduNamePlateTableSize_Type.__name__ = "Integer32"
_PduNamePlateTableSize_Object = MibScalar
pduNamePlateTableSize = _PduNamePlateTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 1),
    _PduNamePlateTableSize_Type()
)
pduNamePlateTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateTableSize.setStatus("current")
_PduNamePlateTable_Object = MibTable
pduNamePlateTable = _PduNamePlateTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pduNamePlateTable.setStatus("current")
_PduNamePlateEntry_Object = MibTableRow
pduNamePlateEntry = _PduNamePlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1)
)
pduNamePlateEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduNamePlateIndex"),
)
if mibBuilder.loadTexts:
    pduNamePlateEntry.setStatus("current")


class _PduNamePlateIndex_Type(Integer32):
    """Custom type pduNamePlateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduNamePlateIndex_Type.__name__ = "Integer32"
_PduNamePlateIndex_Object = MibTableColumn
pduNamePlateIndex = _PduNamePlateIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 1),
    _PduNamePlateIndex_Type()
)
pduNamePlateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduNamePlateIndex.setStatus("current")
_PduNamePlateName_Type = DisplayString
_PduNamePlateName_Object = MibTableColumn
pduNamePlateName = _PduNamePlateName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 2),
    _PduNamePlateName_Type()
)
pduNamePlateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateName.setStatus("current")
_PduNamePlateLocation_Type = DisplayString
_PduNamePlateLocation_Object = MibTableColumn
pduNamePlateLocation = _PduNamePlateLocation_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 3),
    _PduNamePlateLocation_Type()
)
pduNamePlateLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateLocation.setStatus("current")
_PduNamePlateInetAddressType_Type = InetAddressType
_PduNamePlateInetAddressType_Object = MibTableColumn
pduNamePlateInetAddressType = _PduNamePlateInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 4),
    _PduNamePlateInetAddressType_Type()
)
pduNamePlateInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateInetAddressType.setStatus("current")
_PduNamePlateIPAddress_Type = InetAddress
_PduNamePlateIPAddress_Object = MibTableColumn
pduNamePlateIPAddress = _PduNamePlateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 5),
    _PduNamePlateIPAddress_Type()
)
pduNamePlateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateIPAddress.setStatus("current")
_PduNamePlateInetNetMask_Type = InetAddress
_PduNamePlateInetNetMask_Object = MibTableColumn
pduNamePlateInetNetMask = _PduNamePlateInetNetMask_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 6),
    _PduNamePlateInetNetMask_Type()
)
pduNamePlateInetNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateInetNetMask.setStatus("current")
_PduNamePlateInetGateway_Type = InetAddress
_PduNamePlateInetGateway_Object = MibTableColumn
pduNamePlateInetGateway = _PduNamePlateInetGateway_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 7),
    _PduNamePlateInetGateway_Type()
)
pduNamePlateInetGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateInetGateway.setStatus("current")
_PduNamePlateMACAddress_Type = MacAddress
_PduNamePlateMACAddress_Object = MibTableColumn
pduNamePlateMACAddress = _PduNamePlateMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 8),
    _PduNamePlateMACAddress_Type()
)
pduNamePlateMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateMACAddress.setStatus("current")
_PduNamePlateUTCTimeOffset_Type = DisplayString
_PduNamePlateUTCTimeOffset_Object = MibTableColumn
pduNamePlateUTCTimeOffset = _PduNamePlateUTCTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 9),
    _PduNamePlateUTCTimeOffset_Type()
)
pduNamePlateUTCTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateUTCTimeOffset.setStatus("current")
_PduNamePlateModelNumber_Type = DisplayString
_PduNamePlateModelNumber_Object = MibTableColumn
pduNamePlateModelNumber = _PduNamePlateModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 10),
    _PduNamePlateModelNumber_Type()
)
pduNamePlateModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateModelNumber.setStatus("current")
_PduNamePlateSerialNumber_Type = DisplayString
_PduNamePlateSerialNumber_Object = MibTableColumn
pduNamePlateSerialNumber = _PduNamePlateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 11),
    _PduNamePlateSerialNumber_Type()
)
pduNamePlateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateSerialNumber.setStatus("current")
_PduNamePlateDateofManufacture_Type = DisplayString
_PduNamePlateDateofManufacture_Object = MibTableColumn
pduNamePlateDateofManufacture = _PduNamePlateDateofManufacture_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 12),
    _PduNamePlateDateofManufacture_Type()
)
pduNamePlateDateofManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateDateofManufacture.setStatus("current")
_PduNamePlateFirmwareVersion_Type = DisplayString
_PduNamePlateFirmwareVersion_Object = MibTableColumn
pduNamePlateFirmwareVersion = _PduNamePlateFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 13),
    _PduNamePlateFirmwareVersion_Type()
)
pduNamePlateFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateFirmwareVersion.setStatus("current")
_PduNamePlateFirmwareVersionTimeStamp_Type = DisplayString
_PduNamePlateFirmwareVersionTimeStamp_Object = MibTableColumn
pduNamePlateFirmwareVersionTimeStamp = _PduNamePlateFirmwareVersionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 14),
    _PduNamePlateFirmwareVersionTimeStamp_Type()
)
pduNamePlateFirmwareVersionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateFirmwareVersionTimeStamp.setStatus("current")


class _PduNamePlateType_Type(Integer32):
    """Custom type pduNamePlateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inlineMeter", 1),
          ("pdu", 0))
    )


_PduNamePlateType_Type.__name__ = "Integer32"
_PduNamePlateType_Object = MibTableColumn
pduNamePlateType = _PduNamePlateType_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 1, 2, 1, 15),
    _PduNamePlateType_Type()
)
pduNamePlateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduNamePlateType.setStatus("current")
_PduUnit_ObjectIdentity = ObjectIdentity
pduUnit = _PduUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2)
)


class _PduUnitTableSize_Type(Integer32):
    """Custom type pduUnitTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitTableSize_Type.__name__ = "Integer32"
_PduUnitTableSize_Object = MibScalar
pduUnitTableSize = _PduUnitTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 1),
    _PduUnitTableSize_Type()
)
pduUnitTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitTableSize.setStatus("current")
_PduUnitConfigTable_Object = MibTable
pduUnitConfigTable = _PduUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2)
)
if mibBuilder.loadTexts:
    pduUnitConfigTable.setStatus("current")
_PduUnitConfigEntry_Object = MibTableRow
pduUnitConfigEntry = _PduUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1)
)
pduUnitConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
)
if mibBuilder.loadTexts:
    pduUnitConfigEntry.setStatus("current")


class _PduUnitConfigIndex_Type(Integer32):
    """Custom type pduUnitConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitConfigIndex_Type.__name__ = "Integer32"
_PduUnitConfigIndex_Object = MibTableColumn
pduUnitConfigIndex = _PduUnitConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 1),
    _PduUnitConfigIndex_Type()
)
pduUnitConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitConfigIndex.setStatus("current")
_PduUnitConfigName_Type = DisplayString
_PduUnitConfigName_Object = MibTableColumn
pduUnitConfigName = _PduUnitConfigName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 2),
    _PduUnitConfigName_Type()
)
pduUnitConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigName.setStatus("current")
_PduUnitConfigLocation_Type = DisplayString
_PduUnitConfigLocation_Object = MibTableColumn
pduUnitConfigLocation = _PduUnitConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 3),
    _PduUnitConfigLocation_Type()
)
pduUnitConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigLocation.setStatus("current")


class _PduUnitConfigDisplayOrientation_Type(Integer32):
    """Custom type pduUnitConfigDisplayOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("displayNormal", 1),
          ("displayReverse", 2))
    )


_PduUnitConfigDisplayOrientation_Type.__name__ = "Integer32"
_PduUnitConfigDisplayOrientation_Object = MibTableColumn
pduUnitConfigDisplayOrientation = _PduUnitConfigDisplayOrientation_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 4),
    _PduUnitConfigDisplayOrientation_Type()
)
pduUnitConfigDisplayOrientation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigDisplayOrientation.setStatus("current")


class _PduUnitConfigColdstartDelay_Type(Unsigned32):
    """Custom type pduUnitConfigColdstartDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_PduUnitConfigColdstartDelay_Type.__name__ = "Unsigned32"
_PduUnitConfigColdstartDelay_Object = MibTableColumn
pduUnitConfigColdstartDelay = _PduUnitConfigColdstartDelay_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 5),
    _PduUnitConfigColdstartDelay_Type()
)
pduUnitConfigColdstartDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigColdstartDelay.setStatus("current")


class _PduUnitConfigGlobalOutletStateOnStartup_Type(Integer32):
    """Custom type pduUnitConfigGlobalOutletStateOnStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lastKnownState", 2),
          ("off", 0),
          ("on", 1))
    )


_PduUnitConfigGlobalOutletStateOnStartup_Type.__name__ = "Integer32"
_PduUnitConfigGlobalOutletStateOnStartup_Object = MibTableColumn
pduUnitConfigGlobalOutletStateOnStartup = _PduUnitConfigGlobalOutletStateOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 6),
    _PduUnitConfigGlobalOutletStateOnStartup_Type()
)
pduUnitConfigGlobalOutletStateOnStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigGlobalOutletStateOnStartup.setStatus("current")
_PduUnitConfigLowerCriticalThreshold_Type = Unsigned32
_PduUnitConfigLowerCriticalThreshold_Object = MibTableColumn
pduUnitConfigLowerCriticalThreshold = _PduUnitConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 7),
    _PduUnitConfigLowerCriticalThreshold_Type()
)
pduUnitConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigLowerCriticalThreshold.setStatus("current")
_PduUnitConfigLowerWarningThreshold_Type = Unsigned32
_PduUnitConfigLowerWarningThreshold_Object = MibTableColumn
pduUnitConfigLowerWarningThreshold = _PduUnitConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 8),
    _PduUnitConfigLowerWarningThreshold_Type()
)
pduUnitConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigLowerWarningThreshold.setStatus("current")
_PduUnitConfigUpperCriticalThreshold_Type = Unsigned32
_PduUnitConfigUpperCriticalThreshold_Object = MibTableColumn
pduUnitConfigUpperCriticalThreshold = _PduUnitConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 9),
    _PduUnitConfigUpperCriticalThreshold_Type()
)
pduUnitConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigUpperCriticalThreshold.setStatus("current")
_PduUnitConfigUpperWarningThreshold_Type = Unsigned32
_PduUnitConfigUpperWarningThreshold_Object = MibTableColumn
pduUnitConfigUpperWarningThreshold = _PduUnitConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 10),
    _PduUnitConfigUpperWarningThreshold_Type()
)
pduUnitConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigUpperWarningThreshold.setStatus("current")
_PduUnitConfigAlarmResetThreshold_Type = Unsigned32
_PduUnitConfigAlarmResetThreshold_Object = MibTableColumn
pduUnitConfigAlarmResetThreshold = _PduUnitConfigAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 11),
    _PduUnitConfigAlarmResetThreshold_Type()
)
pduUnitConfigAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigAlarmResetThreshold.setStatus("current")
_PduUnitConfigAlarmStateChangeDelay_Type = Unsigned32
_PduUnitConfigAlarmStateChangeDelay_Object = MibTableColumn
pduUnitConfigAlarmStateChangeDelay = _PduUnitConfigAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 12),
    _PduUnitConfigAlarmStateChangeDelay_Type()
)
pduUnitConfigAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigAlarmStateChangeDelay.setStatus("current")


class _PduUnitConfigEnabledThresholds_Type(Bits):
    """Custom type pduUnitConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_PduUnitConfigEnabledThresholds_Type.__name__ = "Bits"
_PduUnitConfigEnabledThresholds_Object = MibTableColumn
pduUnitConfigEnabledThresholds = _PduUnitConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 13),
    _PduUnitConfigEnabledThresholds_Type()
)
pduUnitConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigEnabledThresholds.setStatus("current")


class _PduUnitConfigPeakPowerReset_Type(Integer32):
    """Custom type pduUnitConfigPeakPowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("reset", 2))
    )


_PduUnitConfigPeakPowerReset_Type.__name__ = "Integer32"
_PduUnitConfigPeakPowerReset_Object = MibTableColumn
pduUnitConfigPeakPowerReset = _PduUnitConfigPeakPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 14),
    _PduUnitConfigPeakPowerReset_Type()
)
pduUnitConfigPeakPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigPeakPowerReset.setStatus("current")


class _PduUnitConfigEnergyReset_Type(Integer32):
    """Custom type pduUnitConfigEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("notSupported", 3),
          ("reset", 2))
    )


_PduUnitConfigEnergyReset_Type.__name__ = "Integer32"
_PduUnitConfigEnergyReset_Object = MibTableColumn
pduUnitConfigEnergyReset = _PduUnitConfigEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 15),
    _PduUnitConfigEnergyReset_Type()
)
pduUnitConfigEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigEnergyReset.setStatus("current")


class _PduUnitConfigOutletPeakPowerReset_Type(Integer32):
    """Custom type pduUnitConfigOutletPeakPowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("notSupported", 3),
          ("reset", 2))
    )


_PduUnitConfigOutletPeakPowerReset_Type.__name__ = "Integer32"
_PduUnitConfigOutletPeakPowerReset_Object = MibTableColumn
pduUnitConfigOutletPeakPowerReset = _PduUnitConfigOutletPeakPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 16),
    _PduUnitConfigOutletPeakPowerReset_Type()
)
pduUnitConfigOutletPeakPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigOutletPeakPowerReset.setStatus("current")


class _PduUnitConfigOutletEnergyReset_Type(Integer32):
    """Custom type pduUnitConfigOutletEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("notSupported", 3),
          ("reset", 2))
    )


_PduUnitConfigOutletEnergyReset_Type.__name__ = "Integer32"
_PduUnitConfigOutletEnergyReset_Object = MibTableColumn
pduUnitConfigOutletEnergyReset = _PduUnitConfigOutletEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 17),
    _PduUnitConfigOutletEnergyReset_Type()
)
pduUnitConfigOutletEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigOutletEnergyReset.setStatus("current")


class _PduUnitConfigUsb_Type(Integer32):
    """Custom type pduUnitConfigUsb based on Integer32"""
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


_PduUnitConfigUsb_Type.__name__ = "Integer32"
_PduUnitConfigUsb_Object = MibTableColumn
pduUnitConfigUsb = _PduUnitConfigUsb_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 18),
    _PduUnitConfigUsb_Type()
)
pduUnitConfigUsb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigUsb.setStatus("current")


class _PduUnitConfigSsh_Type(Integer32):
    """Custom type pduUnitConfigSsh based on Integer32"""
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


_PduUnitConfigSsh_Type.__name__ = "Integer32"
_PduUnitConfigSsh_Object = MibTableColumn
pduUnitConfigSsh = _PduUnitConfigSsh_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 19),
    _PduUnitConfigSsh_Type()
)
pduUnitConfigSsh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigSsh.setStatus("current")


class _PduUnitConfigResetNetworkManagementCard_Type(Integer32):
    """Custom type pduUnitConfigResetNetworkManagementCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("reset", 1))
    )


_PduUnitConfigResetNetworkManagementCard_Type.__name__ = "Integer32"
_PduUnitConfigResetNetworkManagementCard_Object = MibTableColumn
pduUnitConfigResetNetworkManagementCard = _PduUnitConfigResetNetworkManagementCard_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 20),
    _PduUnitConfigResetNetworkManagementCard_Type()
)
pduUnitConfigResetNetworkManagementCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigResetNetworkManagementCard.setStatus("current")


class _PduUnitConfigDaisyChainState_Type(Integer32):
    """Custom type pduUnitConfigDaisyChainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("daisychain", 0)
    )


_PduUnitConfigDaisyChainState_Type.__name__ = "Integer32"
_PduUnitConfigDaisyChainState_Object = MibTableColumn
pduUnitConfigDaisyChainState = _PduUnitConfigDaisyChainState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 2, 1, 21),
    _PduUnitConfigDaisyChainState_Type()
)
pduUnitConfigDaisyChainState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitConfigDaisyChainState.setStatus("current")
_PduUnitPropertiesTable_Object = MibTable
pduUnitPropertiesTable = _PduUnitPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3)
)
if mibBuilder.loadTexts:
    pduUnitPropertiesTable.setStatus("current")
_PduUnitPropertiesEntry_Object = MibTableRow
pduUnitPropertiesEntry = _PduUnitPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1)
)
pduUnitPropertiesEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduUnitPropertiesEntry.setStatus("current")


class _PduUnitPropertiesIndex_Type(Integer32):
    """Custom type pduUnitPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesIndex_Type.__name__ = "Integer32"
_PduUnitPropertiesIndex_Object = MibTableColumn
pduUnitPropertiesIndex = _PduUnitPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 1),
    _PduUnitPropertiesIndex_Type()
)
pduUnitPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitPropertiesIndex.setStatus("current")
_PduUnitPropertiesName_Type = DisplayString
_PduUnitPropertiesName_Object = MibTableColumn
pduUnitPropertiesName = _PduUnitPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 2),
    _PduUnitPropertiesName_Type()
)
pduUnitPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesName.setStatus("current")


class _PduUnitPropertiesOutletCount_Type(Integer32):
    """Custom type pduUnitPropertiesOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesOutletCount_Type.__name__ = "Integer32"
_PduUnitPropertiesOutletCount_Object = MibTableColumn
pduUnitPropertiesOutletCount = _PduUnitPropertiesOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 3),
    _PduUnitPropertiesOutletCount_Type()
)
pduUnitPropertiesOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesOutletCount.setStatus("current")


class _PduUnitPropertiesSwitchedOutletCount_Type(Integer32):
    """Custom type pduUnitPropertiesSwitchedOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesSwitchedOutletCount_Type.__name__ = "Integer32"
_PduUnitPropertiesSwitchedOutletCount_Object = MibTableColumn
pduUnitPropertiesSwitchedOutletCount = _PduUnitPropertiesSwitchedOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 4),
    _PduUnitPropertiesSwitchedOutletCount_Type()
)
pduUnitPropertiesSwitchedOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesSwitchedOutletCount.setStatus("current")


class _PduUnitPropertiesMeteredOutletCount_Type(Integer32):
    """Custom type pduUnitPropertiesMeteredOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesMeteredOutletCount_Type.__name__ = "Integer32"
_PduUnitPropertiesMeteredOutletCount_Object = MibTableColumn
pduUnitPropertiesMeteredOutletCount = _PduUnitPropertiesMeteredOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 5),
    _PduUnitPropertiesMeteredOutletCount_Type()
)
pduUnitPropertiesMeteredOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesMeteredOutletCount.setStatus("current")


class _PduUnitPropertiesInputPhaseCount_Type(Integer32):
    """Custom type pduUnitPropertiesInputPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitPropertiesInputPhaseCount_Type.__name__ = "Integer32"
_PduUnitPropertiesInputPhaseCount_Object = MibTableColumn
pduUnitPropertiesInputPhaseCount = _PduUnitPropertiesInputPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 6),
    _PduUnitPropertiesInputPhaseCount_Type()
)
pduUnitPropertiesInputPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesInputPhaseCount.setStatus("current")


class _PduUnitPropertiesCircuitBreakerCount_Type(Integer32):
    """Custom type pduUnitPropertiesCircuitBreakerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitPropertiesCircuitBreakerCount_Type.__name__ = "Integer32"
_PduUnitPropertiesCircuitBreakerCount_Object = MibTableColumn
pduUnitPropertiesCircuitBreakerCount = _PduUnitPropertiesCircuitBreakerCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 7),
    _PduUnitPropertiesCircuitBreakerCount_Type()
)
pduUnitPropertiesCircuitBreakerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesCircuitBreakerCount.setStatus("current")


class _PduUnitPropertiesMaxExternalSensorCount_Type(Integer32):
    """Custom type pduUnitPropertiesMaxExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitPropertiesMaxExternalSensorCount_Type.__name__ = "Integer32"
_PduUnitPropertiesMaxExternalSensorCount_Object = MibTableColumn
pduUnitPropertiesMaxExternalSensorCount = _PduUnitPropertiesMaxExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 8),
    _PduUnitPropertiesMaxExternalSensorCount_Type()
)
pduUnitPropertiesMaxExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesMaxExternalSensorCount.setStatus("current")


class _PduUnitPropertiesConnExternalSensorCount_Type(Integer32):
    """Custom type pduUnitPropertiesConnExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitPropertiesConnExternalSensorCount_Type.__name__ = "Integer32"
_PduUnitPropertiesConnExternalSensorCount_Object = MibTableColumn
pduUnitPropertiesConnExternalSensorCount = _PduUnitPropertiesConnExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 9),
    _PduUnitPropertiesConnExternalSensorCount_Type()
)
pduUnitPropertiesConnExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesConnExternalSensorCount.setStatus("current")
_PduUnitPropertiesRatedVoltage_Type = DisplayString
_PduUnitPropertiesRatedVoltage_Object = MibTableColumn
pduUnitPropertiesRatedVoltage = _PduUnitPropertiesRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 10),
    _PduUnitPropertiesRatedVoltage_Type()
)
pduUnitPropertiesRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedVoltage.setStatus("current")
_PduUnitPropertiesRatedMaxCurrent_Type = DisplayString
_PduUnitPropertiesRatedMaxCurrent_Object = MibTableColumn
pduUnitPropertiesRatedMaxCurrent = _PduUnitPropertiesRatedMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 11),
    _PduUnitPropertiesRatedMaxCurrent_Type()
)
pduUnitPropertiesRatedMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedMaxCurrent.setStatus("current")
_PduUnitPropertiesRatedFrequency_Type = DisplayString
_PduUnitPropertiesRatedFrequency_Object = MibTableColumn
pduUnitPropertiesRatedFrequency = _PduUnitPropertiesRatedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 12),
    _PduUnitPropertiesRatedFrequency_Type()
)
pduUnitPropertiesRatedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedFrequency.setStatus("current")
_PduUnitPropertiesRatedPower_Type = DisplayString
_PduUnitPropertiesRatedPower_Object = MibTableColumn
pduUnitPropertiesRatedPower = _PduUnitPropertiesRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 13),
    _PduUnitPropertiesRatedPower_Type()
)
pduUnitPropertiesRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesRatedPower.setStatus("current")


class _PduUnitPropertiesOrientation_Type(Integer32):
    """Custom type pduUnitPropertiesOrientation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 1),
          ("vertical", 2))
    )


_PduUnitPropertiesOrientation_Type.__name__ = "Integer32"
_PduUnitPropertiesOrientation_Object = MibTableColumn
pduUnitPropertiesOrientation = _PduUnitPropertiesOrientation_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 14),
    _PduUnitPropertiesOrientation_Type()
)
pduUnitPropertiesOrientation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesOrientation.setStatus("current")


class _PduUnitPropertiesOutletLayout_Type(Integer32):
    """Custom type pduUnitPropertiesOutletLayout based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("seqNotApplicable", 9),
          ("seqPToN1516PToPGrouped", 6),
          ("seqPhToN2xGrouped", 8),
          ("seqPhToNGrouped", 5),
          ("seqPhToNeu21PhToPh", 3),
          ("seqPhToPh2xGrouped", 7),
          ("seqPhToPhGrouped", 4),
          ("seqPhaseToNuetral", 1),
          ("seqPhaseToPhase", 2))
    )


_PduUnitPropertiesOutletLayout_Type.__name__ = "Integer32"
_PduUnitPropertiesOutletLayout_Object = MibTableColumn
pduUnitPropertiesOutletLayout = _PduUnitPropertiesOutletLayout_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 15),
    _PduUnitPropertiesOutletLayout_Type()
)
pduUnitPropertiesOutletLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesOutletLayout.setStatus("current")


class _PduUnitPropertiesDaisyChainMemberType_Type(Integer32):
    """Custom type pduUnitPropertiesDaisyChainMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("child", 3),
          ("parent", 2),
          ("standalone", 1))
    )


_PduUnitPropertiesDaisyChainMemberType_Type.__name__ = "Integer32"
_PduUnitPropertiesDaisyChainMemberType_Object = MibTableColumn
pduUnitPropertiesDaisyChainMemberType = _PduUnitPropertiesDaisyChainMemberType_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 16),
    _PduUnitPropertiesDaisyChainMemberType_Type()
)
pduUnitPropertiesDaisyChainMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesDaisyChainMemberType.setStatus("current")


class _PduUnitPropertiesServerCount_Type(Integer32):
    """Custom type pduUnitPropertiesServerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitPropertiesServerCount_Type.__name__ = "Integer32"
_PduUnitPropertiesServerCount_Object = MibTableColumn
pduUnitPropertiesServerCount = _PduUnitPropertiesServerCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 3, 1, 17),
    _PduUnitPropertiesServerCount_Type()
)
pduUnitPropertiesServerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitPropertiesServerCount.setStatus("current")
_PduUnitStatusTable_Object = MibTable
pduUnitStatusTable = _PduUnitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pduUnitStatusTable.setStatus("current")
_PduUnitStatusEntry_Object = MibTableRow
pduUnitStatusEntry = _PduUnitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1)
)
pduUnitStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitStatusIndex"),
)
if mibBuilder.loadTexts:
    pduUnitStatusEntry.setStatus("current")


class _PduUnitStatusIndex_Type(Integer32):
    """Custom type pduUnitStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitStatusIndex_Type.__name__ = "Integer32"
_PduUnitStatusIndex_Object = MibTableColumn
pduUnitStatusIndex = _PduUnitStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 1),
    _PduUnitStatusIndex_Type()
)
pduUnitStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitStatusIndex.setStatus("current")
_PduUnitStatusName_Type = DisplayString
_PduUnitStatusName_Object = MibTableColumn
pduUnitStatusName = _PduUnitStatusName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 2),
    _PduUnitStatusName_Type()
)
pduUnitStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusName.setStatus("current")


class _PduUnitStatusLoadState_Type(Integer32):
    """Custom type pduUnitStatusLoadState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_PduUnitStatusLoadState_Type.__name__ = "Integer32"
_PduUnitStatusLoadState_Object = MibTableColumn
pduUnitStatusLoadState = _PduUnitStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 3),
    _PduUnitStatusLoadState_Type()
)
pduUnitStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusLoadState.setStatus("current")
_PduUnitStatusActivePower_Type = Integer32
_PduUnitStatusActivePower_Object = MibTableColumn
pduUnitStatusActivePower = _PduUnitStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 4),
    _PduUnitStatusActivePower_Type()
)
pduUnitStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusActivePower.setStatus("current")
_PduUnitStatusApparentPower_Type = Integer32
_PduUnitStatusApparentPower_Object = MibTableColumn
pduUnitStatusApparentPower = _PduUnitStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 5),
    _PduUnitStatusApparentPower_Type()
)
pduUnitStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusApparentPower.setStatus("current")
_PduUnitStatusPeakPower_Type = Integer32
_PduUnitStatusPeakPower_Object = MibTableColumn
pduUnitStatusPeakPower = _PduUnitStatusPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 6),
    _PduUnitStatusPeakPower_Type()
)
pduUnitStatusPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusPeakPower.setStatus("current")
_PduUnitStatusPeakPowerTimestamp_Type = DisplayString
_PduUnitStatusPeakPowerTimestamp_Object = MibTableColumn
pduUnitStatusPeakPowerTimestamp = _PduUnitStatusPeakPowerTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 7),
    _PduUnitStatusPeakPowerTimestamp_Type()
)
pduUnitStatusPeakPowerTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusPeakPowerTimestamp.setStatus("current")
_PduUnitStatusPeakPowerStartTime_Type = DisplayString
_PduUnitStatusPeakPowerStartTime_Object = MibTableColumn
pduUnitStatusPeakPowerStartTime = _PduUnitStatusPeakPowerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 8),
    _PduUnitStatusPeakPowerStartTime_Type()
)
pduUnitStatusPeakPowerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusPeakPowerStartTime.setStatus("current")
_PduUnitStatusEnergy_Type = Integer32
_PduUnitStatusEnergy_Object = MibTableColumn
pduUnitStatusEnergy = _PduUnitStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 9),
    _PduUnitStatusEnergy_Type()
)
pduUnitStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusEnergy.setStatus("current")
_PduUnitStatusResettableEnergy_Type = Integer32
_PduUnitStatusResettableEnergy_Object = MibTableColumn
pduUnitStatusResettableEnergy = _PduUnitStatusResettableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 10),
    _PduUnitStatusResettableEnergy_Type()
)
pduUnitStatusResettableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusResettableEnergy.setStatus("current")
_PduUnitStatusEnergyStartTime_Type = DisplayString
_PduUnitStatusEnergyStartTime_Object = MibTableColumn
pduUnitStatusEnergyStartTime = _PduUnitStatusEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 11),
    _PduUnitStatusEnergyStartTime_Type()
)
pduUnitStatusEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusEnergyStartTime.setStatus("current")
_PduUnitStatusOutletsEnergyStartTime_Type = DisplayString
_PduUnitStatusOutletsEnergyStartTime_Object = MibTableColumn
pduUnitStatusOutletsEnergyStartTime = _PduUnitStatusOutletsEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 2, 4, 1, 12),
    _PduUnitStatusOutletsEnergyStartTime_Type()
)
pduUnitStatusOutletsEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitStatusOutletsEnergyStartTime.setStatus("current")
_PduInputPhase_ObjectIdentity = ObjectIdentity
pduInputPhase = _PduInputPhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3)
)


class _PduInputPhaseTableSize_Type(Integer32):
    """Custom type pduInputPhaseTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseTableSize_Type.__name__ = "Integer32"
_PduInputPhaseTableSize_Object = MibScalar
pduInputPhaseTableSize = _PduInputPhaseTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 1),
    _PduInputPhaseTableSize_Type()
)
pduInputPhaseTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseTableSize.setStatus("current")
_PduInputPhaseConfigTable_Object = MibTable
pduInputPhaseConfigTable = _PduInputPhaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pduInputPhaseConfigTable.setStatus("current")
_PduInputPhaseConfigEntry_Object = MibTableRow
pduInputPhaseConfigEntry = _PduInputPhaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1)
)
pduInputPhaseConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduInputPhaseConfigIndex"),
)
if mibBuilder.loadTexts:
    pduInputPhaseConfigEntry.setStatus("current")


class _PduInputPhaseConfigIndex_Type(Integer32):
    """Custom type pduInputPhaseConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseConfigIndex_Type.__name__ = "Integer32"
_PduInputPhaseConfigIndex_Object = MibTableColumn
pduInputPhaseConfigIndex = _PduInputPhaseConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 1),
    _PduInputPhaseConfigIndex_Type()
)
pduInputPhaseConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputPhaseConfigIndex.setStatus("current")


class _PduInputPhaseConfigCount_Type(Integer32):
    """Custom type pduInputPhaseConfigCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseConfigCount_Type.__name__ = "Integer32"
_PduInputPhaseConfigCount_Object = MibTableColumn
pduInputPhaseConfigCount = _PduInputPhaseConfigCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 2),
    _PduInputPhaseConfigCount_Type()
)
pduInputPhaseConfigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCount.setStatus("current")


class _PduInputPhaseConfigOverloadRestriction_Type(Integer32):
    """Custom type pduInputPhaseConfigOverloadRestriction based on Integer32"""
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
        *(("alwaysAllowTurnOn", 1),
          ("notSupported", 4),
          ("restrictOnUpperCritical", 3),
          ("restrictOnUpperWarning", 2))
    )


_PduInputPhaseConfigOverloadRestriction_Type.__name__ = "Integer32"
_PduInputPhaseConfigOverloadRestriction_Object = MibTableColumn
pduInputPhaseConfigOverloadRestriction = _PduInputPhaseConfigOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 3),
    _PduInputPhaseConfigOverloadRestriction_Type()
)
pduInputPhaseConfigOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigOverloadRestriction.setStatus("current")
_PduInputPhaseConfigCurrentLowerCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentLowerCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentLowerCriticalThreshold = _PduInputPhaseConfigCurrentLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 4),
    _PduInputPhaseConfigCurrentLowerCriticalThreshold_Type()
)
pduInputPhaseConfigCurrentLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentLowerCriticalThreshold.setStatus("current")
_PduInputPhaseConfigCurrentLowerWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentLowerWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentLowerWarningThreshold = _PduInputPhaseConfigCurrentLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 5),
    _PduInputPhaseConfigCurrentLowerWarningThreshold_Type()
)
pduInputPhaseConfigCurrentLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentLowerWarningThreshold.setStatus("current")
_PduInputPhaseConfigCurrentUpperCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentUpperCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentUpperCriticalThreshold = _PduInputPhaseConfigCurrentUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 6),
    _PduInputPhaseConfigCurrentUpperCriticalThreshold_Type()
)
pduInputPhaseConfigCurrentUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentUpperCriticalThreshold.setStatus("current")
_PduInputPhaseConfigCurrentUpperWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentUpperWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentUpperWarningThreshold = _PduInputPhaseConfigCurrentUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 7),
    _PduInputPhaseConfigCurrentUpperWarningThreshold_Type()
)
pduInputPhaseConfigCurrentUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentUpperWarningThreshold.setStatus("current")
_PduInputPhaseConfigVoltageLowerCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageLowerCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageLowerCriticalThreshold = _PduInputPhaseConfigVoltageLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 8),
    _PduInputPhaseConfigVoltageLowerCriticalThreshold_Type()
)
pduInputPhaseConfigVoltageLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageLowerCriticalThreshold.setStatus("current")
_PduInputPhaseConfigVoltageLowerWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageLowerWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageLowerWarningThreshold = _PduInputPhaseConfigVoltageLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 9),
    _PduInputPhaseConfigVoltageLowerWarningThreshold_Type()
)
pduInputPhaseConfigVoltageLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageLowerWarningThreshold.setStatus("current")
_PduInputPhaseConfigVoltageUpperCriticalThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageUpperCriticalThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageUpperCriticalThreshold = _PduInputPhaseConfigVoltageUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 10),
    _PduInputPhaseConfigVoltageUpperCriticalThreshold_Type()
)
pduInputPhaseConfigVoltageUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageUpperCriticalThreshold.setStatus("current")
_PduInputPhaseConfigVoltageUpperWarningThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageUpperWarningThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageUpperWarningThreshold = _PduInputPhaseConfigVoltageUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 11),
    _PduInputPhaseConfigVoltageUpperWarningThreshold_Type()
)
pduInputPhaseConfigVoltageUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageUpperWarningThreshold.setStatus("current")
_PduInputPhaseConfigCurrentAlarmResetThreshold_Type = Unsigned32
_PduInputPhaseConfigCurrentAlarmResetThreshold_Object = MibTableColumn
pduInputPhaseConfigCurrentAlarmResetThreshold = _PduInputPhaseConfigCurrentAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 12),
    _PduInputPhaseConfigCurrentAlarmResetThreshold_Type()
)
pduInputPhaseConfigCurrentAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentAlarmResetThreshold.setStatus("current")
_PduInputPhaseConfigCurrentAlarmStateChangeDelay_Type = Integer32
_PduInputPhaseConfigCurrentAlarmStateChangeDelay_Object = MibTableColumn
pduInputPhaseConfigCurrentAlarmStateChangeDelay = _PduInputPhaseConfigCurrentAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 13),
    _PduInputPhaseConfigCurrentAlarmStateChangeDelay_Type()
)
pduInputPhaseConfigCurrentAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentAlarmStateChangeDelay.setStatus("current")


class _PduInputPhaseConfigCurrentEnabledThresholds_Type(Bits):
    """Custom type pduInputPhaseConfigCurrentEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_PduInputPhaseConfigCurrentEnabledThresholds_Type.__name__ = "Bits"
_PduInputPhaseConfigCurrentEnabledThresholds_Object = MibTableColumn
pduInputPhaseConfigCurrentEnabledThresholds = _PduInputPhaseConfigCurrentEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 14),
    _PduInputPhaseConfigCurrentEnabledThresholds_Type()
)
pduInputPhaseConfigCurrentEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigCurrentEnabledThresholds.setStatus("current")
_PduInputPhaseConfigVoltageAlarmResetThreshold_Type = Unsigned32
_PduInputPhaseConfigVoltageAlarmResetThreshold_Object = MibTableColumn
pduInputPhaseConfigVoltageAlarmResetThreshold = _PduInputPhaseConfigVoltageAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 15),
    _PduInputPhaseConfigVoltageAlarmResetThreshold_Type()
)
pduInputPhaseConfigVoltageAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageAlarmResetThreshold.setStatus("current")
_PduInputPhaseConfigVoltageAlarmStateChangeDelay_Type = Integer32
_PduInputPhaseConfigVoltageAlarmStateChangeDelay_Object = MibTableColumn
pduInputPhaseConfigVoltageAlarmStateChangeDelay = _PduInputPhaseConfigVoltageAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 16),
    _PduInputPhaseConfigVoltageAlarmStateChangeDelay_Type()
)
pduInputPhaseConfigVoltageAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageAlarmStateChangeDelay.setStatus("current")


class _PduInputPhaseConfigVoltageEnabledThresholds_Type(Bits):
    """Custom type pduInputPhaseConfigVoltageEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_PduInputPhaseConfigVoltageEnabledThresholds_Type.__name__ = "Bits"
_PduInputPhaseConfigVoltageEnabledThresholds_Object = MibTableColumn
pduInputPhaseConfigVoltageEnabledThresholds = _PduInputPhaseConfigVoltageEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 2, 1, 17),
    _PduInputPhaseConfigVoltageEnabledThresholds_Type()
)
pduInputPhaseConfigVoltageEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduInputPhaseConfigVoltageEnabledThresholds.setStatus("current")
_PduInputPhasePropertiesTable_Object = MibTable
pduInputPhasePropertiesTable = _PduInputPhasePropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 3)
)
if mibBuilder.loadTexts:
    pduInputPhasePropertiesTable.setStatus("current")
_PduInputPhasePropertiesEntry_Object = MibTableRow
pduInputPhasePropertiesEntry = _PduInputPhasePropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 3, 1)
)
pduInputPhasePropertiesEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitPropertiesIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduInputPhasePropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduInputPhasePropertiesEntry.setStatus("current")


class _PduInputPhasePropertiesIndex_Type(Integer32):
    """Custom type pduInputPhasePropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhasePropertiesIndex_Type.__name__ = "Integer32"
_PduInputPhasePropertiesIndex_Object = MibTableColumn
pduInputPhasePropertiesIndex = _PduInputPhasePropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 3, 1, 1),
    _PduInputPhasePropertiesIndex_Type()
)
pduInputPhasePropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputPhasePropertiesIndex.setStatus("current")


class _PduInputPhasePropertiesCount_Type(Integer32):
    """Custom type pduInputPhasePropertiesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhasePropertiesCount_Type.__name__ = "Integer32"
_PduInputPhasePropertiesCount_Object = MibTableColumn
pduInputPhasePropertiesCount = _PduInputPhasePropertiesCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 3, 1, 2),
    _PduInputPhasePropertiesCount_Type()
)
pduInputPhasePropertiesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhasePropertiesCount.setStatus("current")
_PduInputPhaseStatusTable_Object = MibTable
pduInputPhaseStatusTable = _PduInputPhaseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4)
)
if mibBuilder.loadTexts:
    pduInputPhaseStatusTable.setStatus("current")
_PduInputPhaseStatusEntry_Object = MibTableRow
pduInputPhaseStatusEntry = _PduInputPhaseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1)
)
pduInputPhaseStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduInputPhaseStatusIndex"),
)
if mibBuilder.loadTexts:
    pduInputPhaseStatusEntry.setStatus("current")


class _PduInputPhaseStatusIndex_Type(Integer32):
    """Custom type pduInputPhaseStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseStatusIndex_Type.__name__ = "Integer32"
_PduInputPhaseStatusIndex_Object = MibTableColumn
pduInputPhaseStatusIndex = _PduInputPhaseStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 1),
    _PduInputPhaseStatusIndex_Type()
)
pduInputPhaseStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduInputPhaseStatusIndex.setStatus("current")


class _PduInputPhaseStatusCount_Type(Integer32):
    """Custom type pduInputPhaseStatusCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduInputPhaseStatusCount_Type.__name__ = "Integer32"
_PduInputPhaseStatusCount_Object = MibTableColumn
pduInputPhaseStatusCount = _PduInputPhaseStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 2),
    _PduInputPhaseStatusCount_Type()
)
pduInputPhaseStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusCount.setStatus("current")


class _PduInputPhaseStatusCurrentState_Type(Integer32):
    """Custom type pduInputPhaseStatusCurrentState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_PduInputPhaseStatusCurrentState_Type.__name__ = "Integer32"
_PduInputPhaseStatusCurrentState_Object = MibTableColumn
pduInputPhaseStatusCurrentState = _PduInputPhaseStatusCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 3),
    _PduInputPhaseStatusCurrentState_Type()
)
pduInputPhaseStatusCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusCurrentState.setStatus("current")


class _PduInputPhaseStatusVoltageState_Type(Integer32):
    """Custom type pduInputPhaseStatusVoltageState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_PduInputPhaseStatusVoltageState_Type.__name__ = "Integer32"
_PduInputPhaseStatusVoltageState_Object = MibTableColumn
pduInputPhaseStatusVoltageState = _PduInputPhaseStatusVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 4),
    _PduInputPhaseStatusVoltageState_Type()
)
pduInputPhaseStatusVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusVoltageState.setStatus("current")
_PduInputPhaseStatusCurrent_Type = Integer32
_PduInputPhaseStatusCurrent_Object = MibTableColumn
pduInputPhaseStatusCurrent = _PduInputPhaseStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 5),
    _PduInputPhaseStatusCurrent_Type()
)
pduInputPhaseStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusCurrent.setStatus("current")
_PduInputPhaseStatusVoltage_Type = Integer32
_PduInputPhaseStatusVoltage_Object = MibTableColumn
pduInputPhaseStatusVoltage = _PduInputPhaseStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 6),
    _PduInputPhaseStatusVoltage_Type()
)
pduInputPhaseStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusVoltage.setStatus("current")
_PduInputPhaseStatusActivePower_Type = Integer32
_PduInputPhaseStatusActivePower_Object = MibTableColumn
pduInputPhaseStatusActivePower = _PduInputPhaseStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 7),
    _PduInputPhaseStatusActivePower_Type()
)
pduInputPhaseStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusActivePower.setStatus("current")
_PduInputPhaseStatusApparentPower_Type = Integer32
_PduInputPhaseStatusApparentPower_Object = MibTableColumn
pduInputPhaseStatusApparentPower = _PduInputPhaseStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 8),
    _PduInputPhaseStatusApparentPower_Type()
)
pduInputPhaseStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusApparentPower.setStatus("current")
_PduInputPhaseStatusPowerFactor_Type = Integer32
_PduInputPhaseStatusPowerFactor_Object = MibTableColumn
pduInputPhaseStatusPowerFactor = _PduInputPhaseStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 3, 4, 1, 9),
    _PduInputPhaseStatusPowerFactor_Type()
)
pduInputPhaseStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduInputPhaseStatusPowerFactor.setStatus("current")
_PduCircuitBreaker_ObjectIdentity = ObjectIdentity
pduCircuitBreaker = _PduCircuitBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4)
)


class _PduCircuitBreakerTableSize_Type(Integer32):
    """Custom type pduCircuitBreakerTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerTableSize_Type.__name__ = "Integer32"
_PduCircuitBreakerTableSize_Object = MibScalar
pduCircuitBreakerTableSize = _PduCircuitBreakerTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 1),
    _PduCircuitBreakerTableSize_Type()
)
pduCircuitBreakerTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerTableSize.setStatus("current")
_PduCircuitBreakerConfigTable_Object = MibTable
pduCircuitBreakerConfigTable = _PduCircuitBreakerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2)
)
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigTable.setStatus("current")
_PduCircuitBreakerConfigEntry_Object = MibTableRow
pduCircuitBreakerConfigEntry = _PduCircuitBreakerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1)
)
pduCircuitBreakerConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduCircuitBreakerConfigIndex"),
)
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigEntry.setStatus("current")


class _PduCircuitBreakerConfigIndex_Type(Integer32):
    """Custom type pduCircuitBreakerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerConfigIndex_Type.__name__ = "Integer32"
_PduCircuitBreakerConfigIndex_Object = MibTableColumn
pduCircuitBreakerConfigIndex = _PduCircuitBreakerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 1),
    _PduCircuitBreakerConfigIndex_Type()
)
pduCircuitBreakerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigIndex.setStatus("current")


class _PduCircuitBreakerConfigCount_Type(Integer32):
    """Custom type pduCircuitBreakerConfigCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduCircuitBreakerConfigCount_Type.__name__ = "Integer32"
_PduCircuitBreakerConfigCount_Object = MibTableColumn
pduCircuitBreakerConfigCount = _PduCircuitBreakerConfigCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 2),
    _PduCircuitBreakerConfigCount_Type()
)
pduCircuitBreakerConfigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigCount.setStatus("current")
_PduCircuitBreakerName_Type = DisplayString
_PduCircuitBreakerName_Object = MibTableColumn
pduCircuitBreakerName = _PduCircuitBreakerName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 3),
    _PduCircuitBreakerName_Type()
)
pduCircuitBreakerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerName.setStatus("current")


class _PduCircuitBreakerConfigOverloadRestriction_Type(Integer32):
    """Custom type pduCircuitBreakerConfigOverloadRestriction based on Integer32"""
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
        *(("alwaysAllowTurnOn", 1),
          ("notSupported", 4),
          ("restrictOnUpperCritical", 3),
          ("restrictOnUpperWarning", 2))
    )


_PduCircuitBreakerConfigOverloadRestriction_Type.__name__ = "Integer32"
_PduCircuitBreakerConfigOverloadRestriction_Object = MibTableColumn
pduCircuitBreakerConfigOverloadRestriction = _PduCircuitBreakerConfigOverloadRestriction_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 4),
    _PduCircuitBreakerConfigOverloadRestriction_Type()
)
pduCircuitBreakerConfigOverloadRestriction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigOverloadRestriction.setStatus("current")
_PduCircuitBreakerConfigLowerCriticalThreshold_Type = Unsigned32
_PduCircuitBreakerConfigLowerCriticalThreshold_Object = MibTableColumn
pduCircuitBreakerConfigLowerCriticalThreshold = _PduCircuitBreakerConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 5),
    _PduCircuitBreakerConfigLowerCriticalThreshold_Type()
)
pduCircuitBreakerConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigLowerCriticalThreshold.setStatus("current")
_PduCircuitBreakerConfigLowerWarningThreshold_Type = Unsigned32
_PduCircuitBreakerConfigLowerWarningThreshold_Object = MibTableColumn
pduCircuitBreakerConfigLowerWarningThreshold = _PduCircuitBreakerConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 6),
    _PduCircuitBreakerConfigLowerWarningThreshold_Type()
)
pduCircuitBreakerConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigLowerWarningThreshold.setStatus("current")
_PduCircuitBreakerConfigUpperCriticalThreshold_Type = Unsigned32
_PduCircuitBreakerConfigUpperCriticalThreshold_Object = MibTableColumn
pduCircuitBreakerConfigUpperCriticalThreshold = _PduCircuitBreakerConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 7),
    _PduCircuitBreakerConfigUpperCriticalThreshold_Type()
)
pduCircuitBreakerConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigUpperCriticalThreshold.setStatus("current")
_PduCircuitBreakerConfigUpperWarningThreshold_Type = Unsigned32
_PduCircuitBreakerConfigUpperWarningThreshold_Object = MibTableColumn
pduCircuitBreakerConfigUpperWarningThreshold = _PduCircuitBreakerConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 8),
    _PduCircuitBreakerConfigUpperWarningThreshold_Type()
)
pduCircuitBreakerConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigUpperWarningThreshold.setStatus("current")
_PduCircuitBreakerConfigAlarmResetThreshold_Type = Unsigned32
_PduCircuitBreakerConfigAlarmResetThreshold_Object = MibTableColumn
pduCircuitBreakerConfigAlarmResetThreshold = _PduCircuitBreakerConfigAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 9),
    _PduCircuitBreakerConfigAlarmResetThreshold_Type()
)
pduCircuitBreakerConfigAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigAlarmResetThreshold.setStatus("current")
_PduCircuitBreakerConfigAlarmStateChangeDelay_Type = Unsigned32
_PduCircuitBreakerConfigAlarmStateChangeDelay_Object = MibTableColumn
pduCircuitBreakerConfigAlarmStateChangeDelay = _PduCircuitBreakerConfigAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 10),
    _PduCircuitBreakerConfigAlarmStateChangeDelay_Type()
)
pduCircuitBreakerConfigAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigAlarmStateChangeDelay.setStatus("current")


class _PduCircuitBreakerConfigEnabledThresholds_Type(Bits):
    """Custom type pduCircuitBreakerConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_PduCircuitBreakerConfigEnabledThresholds_Type.__name__ = "Bits"
_PduCircuitBreakerConfigEnabledThresholds_Object = MibTableColumn
pduCircuitBreakerConfigEnabledThresholds = _PduCircuitBreakerConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 2, 1, 11),
    _PduCircuitBreakerConfigEnabledThresholds_Type()
)
pduCircuitBreakerConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduCircuitBreakerConfigEnabledThresholds.setStatus("current")
_PduCircuitBreakerPropertiesTable_Object = MibTable
pduCircuitBreakerPropertiesTable = _PduCircuitBreakerPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 3)
)
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesTable.setStatus("current")
_PduCircuitBreakerPropertiesEntry_Object = MibTableRow
pduCircuitBreakerPropertiesEntry = _PduCircuitBreakerPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 3, 1)
)
pduCircuitBreakerPropertiesEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitPropertiesIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduCircuitBreakerPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesEntry.setStatus("current")


class _PduCircuitBreakerPropertiesIndex_Type(Integer32):
    """Custom type pduCircuitBreakerPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerPropertiesIndex_Type.__name__ = "Integer32"
_PduCircuitBreakerPropertiesIndex_Object = MibTableColumn
pduCircuitBreakerPropertiesIndex = _PduCircuitBreakerPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 3, 1, 1),
    _PduCircuitBreakerPropertiesIndex_Type()
)
pduCircuitBreakerPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesIndex.setStatus("current")


class _PduCircuitBreakerPropertiesCount_Type(Integer32):
    """Custom type pduCircuitBreakerPropertiesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduCircuitBreakerPropertiesCount_Type.__name__ = "Integer32"
_PduCircuitBreakerPropertiesCount_Object = MibTableColumn
pduCircuitBreakerPropertiesCount = _PduCircuitBreakerPropertiesCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 3, 1, 2),
    _PduCircuitBreakerPropertiesCount_Type()
)
pduCircuitBreakerPropertiesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesCount.setStatus("current")


class _PduCircuitBreakerPropertiesInputLayout_Type(Integer32):
    """Custom type pduCircuitBreakerPropertiesInputLayout based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase3ToPhase1", 6))
    )


_PduCircuitBreakerPropertiesInputLayout_Type.__name__ = "Integer32"
_PduCircuitBreakerPropertiesInputLayout_Object = MibTableColumn
pduCircuitBreakerPropertiesInputLayout = _PduCircuitBreakerPropertiesInputLayout_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 3, 1, 3),
    _PduCircuitBreakerPropertiesInputLayout_Type()
)
pduCircuitBreakerPropertiesInputLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerPropertiesInputLayout.setStatus("current")
_PduCircuitBreakerStatusTable_Object = MibTable
pduCircuitBreakerStatusTable = _PduCircuitBreakerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 4)
)
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusTable.setStatus("current")
_PduCircuitBreakerStatusEntry_Object = MibTableRow
pduCircuitBreakerStatusEntry = _PduCircuitBreakerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 4, 1)
)
pduCircuitBreakerStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduCircuitBreakerStatusIndex"),
)
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusEntry.setStatus("current")


class _PduCircuitBreakerStatusIndex_Type(Integer32):
    """Custom type pduCircuitBreakerStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduCircuitBreakerStatusIndex_Type.__name__ = "Integer32"
_PduCircuitBreakerStatusIndex_Object = MibTableColumn
pduCircuitBreakerStatusIndex = _PduCircuitBreakerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 4, 1, 1),
    _PduCircuitBreakerStatusIndex_Type()
)
pduCircuitBreakerStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusIndex.setStatus("current")


class _PduCircuitBreakerStatusCount_Type(Integer32):
    """Custom type pduCircuitBreakerStatusCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduCircuitBreakerStatusCount_Type.__name__ = "Integer32"
_PduCircuitBreakerStatusCount_Object = MibTableColumn
pduCircuitBreakerStatusCount = _PduCircuitBreakerStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 4, 1, 2),
    _PduCircuitBreakerStatusCount_Type()
)
pduCircuitBreakerStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusCount.setStatus("current")
_PduCircuitBreakerLabel_Type = DisplayString
_PduCircuitBreakerLabel_Object = MibTableColumn
pduCircuitBreakerLabel = _PduCircuitBreakerLabel_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 4, 1, 3),
    _PduCircuitBreakerLabel_Type()
)
pduCircuitBreakerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerLabel.setStatus("current")


class _PduCircuitBreakerStatusLoadState_Type(Integer32):
    """Custom type pduCircuitBreakerStatusLoadState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("off", 6),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_PduCircuitBreakerStatusLoadState_Type.__name__ = "Integer32"
_PduCircuitBreakerStatusLoadState_Object = MibTableColumn
pduCircuitBreakerStatusLoadState = _PduCircuitBreakerStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 4, 1, 4),
    _PduCircuitBreakerStatusLoadState_Type()
)
pduCircuitBreakerStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusLoadState.setStatus("current")
_PduCircuitBreakerStatusCurrent_Type = Integer32
_PduCircuitBreakerStatusCurrent_Object = MibTableColumn
pduCircuitBreakerStatusCurrent = _PduCircuitBreakerStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 4, 4, 1, 5),
    _PduCircuitBreakerStatusCurrent_Type()
)
pduCircuitBreakerStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduCircuitBreakerStatusCurrent.setStatus("current")
_PduOutlet_ObjectIdentity = ObjectIdentity
pduOutlet = _PduOutlet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5)
)


class _PduOutletSwitchedTableSize_Type(Integer32):
    """Custom type pduOutletSwitchedTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedTableSize_Type.__name__ = "Integer32"
_PduOutletSwitchedTableSize_Object = MibScalar
pduOutletSwitchedTableSize = _PduOutletSwitchedTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 1),
    _PduOutletSwitchedTableSize_Type()
)
pduOutletSwitchedTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedTableSize.setStatus("current")
_PduOutletSwitchedConfigTable_Object = MibTable
pduOutletSwitchedConfigTable = _PduOutletSwitchedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigTable.setStatus("current")
_PduOutletSwitchedConfigEntry_Object = MibTableRow
pduOutletSwitchedConfigEntry = _PduOutletSwitchedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2, 1)
)
pduOutletSwitchedConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduOutletSwitchedConfigIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigEntry.setStatus("current")


class _PduOutletSwitchedConfigIndex_Type(Integer32):
    """Custom type pduOutletSwitchedConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedConfigIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedConfigIndex_Object = MibTableColumn
pduOutletSwitchedConfigIndex = _PduOutletSwitchedConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2, 1, 1),
    _PduOutletSwitchedConfigIndex_Type()
)
pduOutletSwitchedConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigIndex.setStatus("current")
_PduOutletSwitchedName_Type = DisplayString
_PduOutletSwitchedName_Object = MibTableColumn
pduOutletSwitchedName = _PduOutletSwitchedName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2, 1, 2),
    _PduOutletSwitchedName_Type()
)
pduOutletSwitchedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedName.setStatus("current")


class _PduOutletSwitchedStateOnStartup_Type(Integer32):
    """Custom type pduOutletSwitchedStateOnStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lastKnownState", 2),
          ("off", 0),
          ("on", 1))
    )


_PduOutletSwitchedStateOnStartup_Type.__name__ = "Integer32"
_PduOutletSwitchedStateOnStartup_Object = MibTableColumn
pduOutletSwitchedStateOnStartup = _PduOutletSwitchedStateOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2, 1, 3),
    _PduOutletSwitchedStateOnStartup_Type()
)
pduOutletSwitchedStateOnStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedStateOnStartup.setStatus("current")
_PduOutletSwitchedConfigPowerOnTime_Type = Integer32
_PduOutletSwitchedConfigPowerOnTime_Object = MibTableColumn
pduOutletSwitchedConfigPowerOnTime = _PduOutletSwitchedConfigPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2, 1, 4),
    _PduOutletSwitchedConfigPowerOnTime_Type()
)
pduOutletSwitchedConfigPowerOnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigPowerOnTime.setStatus("current")
_PduOutletSwitchedConfigPowerOffTime_Type = Integer32
_PduOutletSwitchedConfigPowerOffTime_Object = MibTableColumn
pduOutletSwitchedConfigPowerOffTime = _PduOutletSwitchedConfigPowerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2, 1, 5),
    _PduOutletSwitchedConfigPowerOffTime_Type()
)
pduOutletSwitchedConfigPowerOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigPowerOffTime.setStatus("current")
_PduOutletSwitchedConfigRebootDuration_Type = Integer32
_PduOutletSwitchedConfigRebootDuration_Object = MibTableColumn
pduOutletSwitchedConfigRebootDuration = _PduOutletSwitchedConfigRebootDuration_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 2, 1, 6),
    _PduOutletSwitchedConfigRebootDuration_Type()
)
pduOutletSwitchedConfigRebootDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedConfigRebootDuration.setStatus("current")
_PduOutletSwitchedPropertiesTable_Object = MibTable
pduOutletSwitchedPropertiesTable = _PduOutletSwitchedPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 3)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesTable.setStatus("current")
_PduOutletSwitchedPropertiesEntry_Object = MibTableRow
pduOutletSwitchedPropertiesEntry = _PduOutletSwitchedPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 3, 1)
)
pduOutletSwitchedPropertiesEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitPropertiesIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduOutletSwitchedPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesEntry.setStatus("current")


class _PduOutletSwitchedPropertiesIndex_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedPropertiesIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesIndex_Object = MibTableColumn
pduOutletSwitchedPropertiesIndex = _PduOutletSwitchedPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 3, 1, 1),
    _PduOutletSwitchedPropertiesIndex_Type()
)
pduOutletSwitchedPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesIndex.setStatus("current")


class _PduOutletSwitchedPropertiesNumber_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedPropertiesNumber_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesNumber_Object = MibTableColumn
pduOutletSwitchedPropertiesNumber = _PduOutletSwitchedPropertiesNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 3, 1, 2),
    _PduOutletSwitchedPropertiesNumber_Type()
)
pduOutletSwitchedPropertiesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesNumber.setStatus("current")
_PduOutletSwitchedPropertiesName_Type = DisplayString
_PduOutletSwitchedPropertiesName_Object = MibTableColumn
pduOutletSwitchedPropertiesName = _PduOutletSwitchedPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 3, 1, 3),
    _PduOutletSwitchedPropertiesName_Type()
)
pduOutletSwitchedPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesName.setStatus("current")


class _PduOutletSwitchedPropertiesInputPhaseLayout_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesInputPhaseLayout based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase3ToPhase1", 6))
    )


_PduOutletSwitchedPropertiesInputPhaseLayout_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesInputPhaseLayout_Object = MibTableColumn
pduOutletSwitchedPropertiesInputPhaseLayout = _PduOutletSwitchedPropertiesInputPhaseLayout_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 3, 1, 4),
    _PduOutletSwitchedPropertiesInputPhaseLayout_Type()
)
pduOutletSwitchedPropertiesInputPhaseLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesInputPhaseLayout.setStatus("current")


class _PduOutletSwitchedPropertiesCircuitBreaker_Type(Integer32):
    """Custom type pduOutletSwitchedPropertiesCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedPropertiesCircuitBreaker_Type.__name__ = "Integer32"
_PduOutletSwitchedPropertiesCircuitBreaker_Object = MibTableColumn
pduOutletSwitchedPropertiesCircuitBreaker = _PduOutletSwitchedPropertiesCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 3, 1, 5),
    _PduOutletSwitchedPropertiesCircuitBreaker_Type()
)
pduOutletSwitchedPropertiesCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedPropertiesCircuitBreaker.setStatus("current")
_PduOutletSwitchedStatusTable_Object = MibTable
pduOutletSwitchedStatusTable = _PduOutletSwitchedStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 4)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusTable.setStatus("current")
_PduOutletSwitchedStatusEntry_Object = MibTableRow
pduOutletSwitchedStatusEntry = _PduOutletSwitchedStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 4, 1)
)
pduOutletSwitchedStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduOutletSwitchedStatusIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusEntry.setStatus("current")


class _PduOutletSwitchedStatusIndex_Type(Integer32):
    """Custom type pduOutletSwitchedStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedStatusIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedStatusIndex_Object = MibTableColumn
pduOutletSwitchedStatusIndex = _PduOutletSwitchedStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 4, 1, 1),
    _PduOutletSwitchedStatusIndex_Type()
)
pduOutletSwitchedStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusIndex.setStatus("current")


class _PduOutletSwitchedStatusNumber_Type(Integer32):
    """Custom type pduOutletSwitchedStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedStatusNumber_Type.__name__ = "Integer32"
_PduOutletSwitchedStatusNumber_Object = MibTableColumn
pduOutletSwitchedStatusNumber = _PduOutletSwitchedStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 4, 1, 2),
    _PduOutletSwitchedStatusNumber_Type()
)
pduOutletSwitchedStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusNumber.setStatus("current")
_PduOutletSwitchedStatusName_Type = DisplayString
_PduOutletSwitchedStatusName_Object = MibTableColumn
pduOutletSwitchedStatusName = _PduOutletSwitchedStatusName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 4, 1, 3),
    _PduOutletSwitchedStatusName_Type()
)
pduOutletSwitchedStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusName.setStatus("current")


class _PduOutletSwitchedStatusState_Type(Integer32):
    """Custom type pduOutletSwitchedStatusState based on Integer32"""
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


_PduOutletSwitchedStatusState_Type.__name__ = "Integer32"
_PduOutletSwitchedStatusState_Object = MibTableColumn
pduOutletSwitchedStatusState = _PduOutletSwitchedStatusState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 4, 1, 4),
    _PduOutletSwitchedStatusState_Type()
)
pduOutletSwitchedStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedStatusState.setStatus("current")
_PduOutletSwitchedControlTable_Object = MibTable
pduOutletSwitchedControlTable = _PduOutletSwitchedControlTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 5)
)
if mibBuilder.loadTexts:
    pduOutletSwitchedControlTable.setStatus("current")
_PduOutletSwitchedControlEntry_Object = MibTableRow
pduOutletSwitchedControlEntry = _PduOutletSwitchedControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 5, 1)
)
pduOutletSwitchedControlEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduOutletSwitchedControlIndex"),
)
if mibBuilder.loadTexts:
    pduOutletSwitchedControlEntry.setStatus("current")


class _PduOutletSwitchedControlIndex_Type(Integer32):
    """Custom type pduOutletSwitchedControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedControlIndex_Type.__name__ = "Integer32"
_PduOutletSwitchedControlIndex_Object = MibTableColumn
pduOutletSwitchedControlIndex = _PduOutletSwitchedControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 5, 1, 1),
    _PduOutletSwitchedControlIndex_Type()
)
pduOutletSwitchedControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlIndex.setStatus("current")


class _PduOutletSwitchedControlNumber_Type(Integer32):
    """Custom type pduOutletSwitchedControlNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletSwitchedControlNumber_Type.__name__ = "Integer32"
_PduOutletSwitchedControlNumber_Object = MibTableColumn
pduOutletSwitchedControlNumber = _PduOutletSwitchedControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 5, 1, 2),
    _PduOutletSwitchedControlNumber_Type()
)
pduOutletSwitchedControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlNumber.setStatus("current")
_PduOutletSwitchedControlName_Type = DisplayString
_PduOutletSwitchedControlName_Object = MibTableColumn
pduOutletSwitchedControlName = _PduOutletSwitchedControlName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 5, 1, 3),
    _PduOutletSwitchedControlName_Type()
)
pduOutletSwitchedControlName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlName.setStatus("current")


class _PduOutletSwitchedControlCommand_Type(Integer32):
    """Custom type pduOutletSwitchedControlCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("delayedOff", 3),
          ("delayedOn", 4),
          ("delayedReboot", 6),
          ("immediateOff", 1),
          ("immediateOn", 2),
          ("immediateReboot", 5),
          ("outletUnknown", 7))
    )


_PduOutletSwitchedControlCommand_Type.__name__ = "Integer32"
_PduOutletSwitchedControlCommand_Object = MibTableColumn
pduOutletSwitchedControlCommand = _PduOutletSwitchedControlCommand_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 5, 1, 4),
    _PduOutletSwitchedControlCommand_Type()
)
pduOutletSwitchedControlCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletSwitchedControlCommand.setStatus("current")


class _PduOutletMeteredTableSize_Type(Integer32):
    """Custom type pduOutletMeteredTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredTableSize_Type.__name__ = "Integer32"
_PduOutletMeteredTableSize_Object = MibScalar
pduOutletMeteredTableSize = _PduOutletMeteredTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 6),
    _PduOutletMeteredTableSize_Type()
)
pduOutletMeteredTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredTableSize.setStatus("current")
_PduOutletMeteredConfigTable_Object = MibTable
pduOutletMeteredConfigTable = _PduOutletMeteredConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7)
)
if mibBuilder.loadTexts:
    pduOutletMeteredConfigTable.setStatus("current")
_PduOutletMeteredConfigEntry_Object = MibTableRow
pduOutletMeteredConfigEntry = _PduOutletMeteredConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1)
)
pduOutletMeteredConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduOutletMeteredConfigIndex"),
)
if mibBuilder.loadTexts:
    pduOutletMeteredConfigEntry.setStatus("current")


class _PduOutletMeteredConfigIndex_Type(Integer32):
    """Custom type pduOutletMeteredConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredConfigIndex_Type.__name__ = "Integer32"
_PduOutletMeteredConfigIndex_Object = MibTableColumn
pduOutletMeteredConfigIndex = _PduOutletMeteredConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 1),
    _PduOutletMeteredConfigIndex_Type()
)
pduOutletMeteredConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigIndex.setStatus("current")
_PduOutletMeteredName_Type = DisplayString
_PduOutletMeteredName_Object = MibTableColumn
pduOutletMeteredName = _PduOutletMeteredName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 2),
    _PduOutletMeteredName_Type()
)
pduOutletMeteredName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredName.setStatus("current")
_PduOutletMeteredConfigLowerCriticalThreshold_Type = Unsigned32
_PduOutletMeteredConfigLowerCriticalThreshold_Object = MibTableColumn
pduOutletMeteredConfigLowerCriticalThreshold = _PduOutletMeteredConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 3),
    _PduOutletMeteredConfigLowerCriticalThreshold_Type()
)
pduOutletMeteredConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigLowerCriticalThreshold.setStatus("current")
_PduOutletMeteredConfigLowerWarningThreshold_Type = Unsigned32
_PduOutletMeteredConfigLowerWarningThreshold_Object = MibTableColumn
pduOutletMeteredConfigLowerWarningThreshold = _PduOutletMeteredConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 4),
    _PduOutletMeteredConfigLowerWarningThreshold_Type()
)
pduOutletMeteredConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigLowerWarningThreshold.setStatus("current")
_PduOutletMeteredConfigUpperCriticalThreshold_Type = Unsigned32
_PduOutletMeteredConfigUpperCriticalThreshold_Object = MibTableColumn
pduOutletMeteredConfigUpperCriticalThreshold = _PduOutletMeteredConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 5),
    _PduOutletMeteredConfigUpperCriticalThreshold_Type()
)
pduOutletMeteredConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigUpperCriticalThreshold.setStatus("current")
_PduOutletMeteredConfigUpperWarningThreshold_Type = Unsigned32
_PduOutletMeteredConfigUpperWarningThreshold_Object = MibTableColumn
pduOutletMeteredConfigUpperWarningThreshold = _PduOutletMeteredConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 6),
    _PduOutletMeteredConfigUpperWarningThreshold_Type()
)
pduOutletMeteredConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigUpperWarningThreshold.setStatus("current")
_PduOutletMeteredConfigAlarmResetThreshold_Type = Unsigned32
_PduOutletMeteredConfigAlarmResetThreshold_Object = MibTableColumn
pduOutletMeteredConfigAlarmResetThreshold = _PduOutletMeteredConfigAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 7),
    _PduOutletMeteredConfigAlarmResetThreshold_Type()
)
pduOutletMeteredConfigAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigAlarmResetThreshold.setStatus("current")
_PduOutletMeteredConfigAlarmStateChangeDelay_Type = Unsigned32
_PduOutletMeteredConfigAlarmStateChangeDelay_Object = MibTableColumn
pduOutletMeteredConfigAlarmStateChangeDelay = _PduOutletMeteredConfigAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 8),
    _PduOutletMeteredConfigAlarmStateChangeDelay_Type()
)
pduOutletMeteredConfigAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigAlarmStateChangeDelay.setStatus("current")


class _PduOutletMeteredConfigEnabledThresholds_Type(Bits):
    """Custom type pduOutletMeteredConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_PduOutletMeteredConfigEnabledThresholds_Type.__name__ = "Bits"
_PduOutletMeteredConfigEnabledThresholds_Object = MibTableColumn
pduOutletMeteredConfigEnabledThresholds = _PduOutletMeteredConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 7, 1, 9),
    _PduOutletMeteredConfigEnabledThresholds_Type()
)
pduOutletMeteredConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduOutletMeteredConfigEnabledThresholds.setStatus("current")
_PduOutletMeteredPropertiesTable_Object = MibTable
pduOutletMeteredPropertiesTable = _PduOutletMeteredPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8)
)
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesTable.setStatus("current")
_PduOutletMeteredPropertiesEntry_Object = MibTableRow
pduOutletMeteredPropertiesEntry = _PduOutletMeteredPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8, 1)
)
pduOutletMeteredPropertiesEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitPropertiesIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduOutletMeteredPropertiesIndex"),
)
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesEntry.setStatus("current")


class _PduOutletMeteredPropertiesIndex_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredPropertiesIndex_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesIndex_Object = MibTableColumn
pduOutletMeteredPropertiesIndex = _PduOutletMeteredPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8, 1, 1),
    _PduOutletMeteredPropertiesIndex_Type()
)
pduOutletMeteredPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesIndex.setStatus("current")


class _PduOutletMeteredPropertiesNumber_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredPropertiesNumber_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesNumber_Object = MibTableColumn
pduOutletMeteredPropertiesNumber = _PduOutletMeteredPropertiesNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8, 1, 2),
    _PduOutletMeteredPropertiesNumber_Type()
)
pduOutletMeteredPropertiesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesNumber.setStatus("current")
_PduOutletMeteredPropertiesName_Type = DisplayString
_PduOutletMeteredPropertiesName_Object = MibTableColumn
pduOutletMeteredPropertiesName = _PduOutletMeteredPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8, 1, 3),
    _PduOutletMeteredPropertiesName_Type()
)
pduOutletMeteredPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesName.setStatus("current")


class _PduOutletMeteredPropertiesInputPhaseLayout_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesInputPhaseLayout based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase3ToPhase1", 6))
    )


_PduOutletMeteredPropertiesInputPhaseLayout_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesInputPhaseLayout_Object = MibTableColumn
pduOutletMeteredPropertiesInputPhaseLayout = _PduOutletMeteredPropertiesInputPhaseLayout_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8, 1, 4),
    _PduOutletMeteredPropertiesInputPhaseLayout_Type()
)
pduOutletMeteredPropertiesInputPhaseLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesInputPhaseLayout.setStatus("current")


class _PduOutletMeteredPropertiesCircuitBreaker_Type(Integer32):
    """Custom type pduOutletMeteredPropertiesCircuitBreaker based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredPropertiesCircuitBreaker_Type.__name__ = "Integer32"
_PduOutletMeteredPropertiesCircuitBreaker_Object = MibTableColumn
pduOutletMeteredPropertiesCircuitBreaker = _PduOutletMeteredPropertiesCircuitBreaker_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8, 1, 5),
    _PduOutletMeteredPropertiesCircuitBreaker_Type()
)
pduOutletMeteredPropertiesCircuitBreaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesCircuitBreaker.setStatus("current")
_PduOutletMeteredPropertiesPowerRating_Type = Integer32
_PduOutletMeteredPropertiesPowerRating_Object = MibTableColumn
pduOutletMeteredPropertiesPowerRating = _PduOutletMeteredPropertiesPowerRating_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 8, 1, 6),
    _PduOutletMeteredPropertiesPowerRating_Type()
)
pduOutletMeteredPropertiesPowerRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredPropertiesPowerRating.setStatus("current")
_PduOutletMeteredStatusTable_Object = MibTable
pduOutletMeteredStatusTable = _PduOutletMeteredStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9)
)
if mibBuilder.loadTexts:
    pduOutletMeteredStatusTable.setStatus("current")
_PduOutletMeteredStatusEntry_Object = MibTableRow
pduOutletMeteredStatusEntry = _PduOutletMeteredStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1)
)
pduOutletMeteredStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduOutletMeteredStatusIndex"),
)
if mibBuilder.loadTexts:
    pduOutletMeteredStatusEntry.setStatus("current")


class _PduOutletMeteredStatusIndex_Type(Integer32):
    """Custom type pduOutletMeteredStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredStatusIndex_Type.__name__ = "Integer32"
_PduOutletMeteredStatusIndex_Object = MibTableColumn
pduOutletMeteredStatusIndex = _PduOutletMeteredStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 1),
    _PduOutletMeteredStatusIndex_Type()
)
pduOutletMeteredStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusIndex.setStatus("current")


class _PduOutletMeteredStatusNumber_Type(Integer32):
    """Custom type pduOutletMeteredStatusNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduOutletMeteredStatusNumber_Type.__name__ = "Integer32"
_PduOutletMeteredStatusNumber_Object = MibTableColumn
pduOutletMeteredStatusNumber = _PduOutletMeteredStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 2),
    _PduOutletMeteredStatusNumber_Type()
)
pduOutletMeteredStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusNumber.setStatus("current")
_PduOutletMeteredStatusName_Type = DisplayString
_PduOutletMeteredStatusName_Object = MibTableColumn
pduOutletMeteredStatusName = _PduOutletMeteredStatusName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 3),
    _PduOutletMeteredStatusName_Type()
)
pduOutletMeteredStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusName.setStatus("current")


class _PduOutletMeteredStatusLoadState_Type(Integer32):
    """Custom type pduOutletMeteredStatusLoadState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_PduOutletMeteredStatusLoadState_Type.__name__ = "Integer32"
_PduOutletMeteredStatusLoadState_Object = MibTableColumn
pduOutletMeteredStatusLoadState = _PduOutletMeteredStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 4),
    _PduOutletMeteredStatusLoadState_Type()
)
pduOutletMeteredStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusLoadState.setStatus("current")
_PduOutletMeteredStatusCurrent_Type = Integer32
_PduOutletMeteredStatusCurrent_Object = MibTableColumn
pduOutletMeteredStatusCurrent = _PduOutletMeteredStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 5),
    _PduOutletMeteredStatusCurrent_Type()
)
pduOutletMeteredStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusCurrent.setStatus("current")
_PduOutletMeteredStatusActivePower_Type = Integer32
_PduOutletMeteredStatusActivePower_Object = MibTableColumn
pduOutletMeteredStatusActivePower = _PduOutletMeteredStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 6),
    _PduOutletMeteredStatusActivePower_Type()
)
pduOutletMeteredStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusActivePower.setStatus("current")
_PduOutletMeteredStatusPowerFactor_Type = Integer32
_PduOutletMeteredStatusPowerFactor_Object = MibTableColumn
pduOutletMeteredStatusPowerFactor = _PduOutletMeteredStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 7),
    _PduOutletMeteredStatusPowerFactor_Type()
)
pduOutletMeteredStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPowerFactor.setStatus("current")
_PduOutletMeteredStatusPeakPower_Type = Integer32
_PduOutletMeteredStatusPeakPower_Object = MibTableColumn
pduOutletMeteredStatusPeakPower = _PduOutletMeteredStatusPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 8),
    _PduOutletMeteredStatusPeakPower_Type()
)
pduOutletMeteredStatusPeakPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPeakPower.setStatus("current")
_PduOutletMeteredStatusPeakPowerTimeStamp_Type = DisplayString
_PduOutletMeteredStatusPeakPowerTimeStamp_Object = MibTableColumn
pduOutletMeteredStatusPeakPowerTimeStamp = _PduOutletMeteredStatusPeakPowerTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 9),
    _PduOutletMeteredStatusPeakPowerTimeStamp_Type()
)
pduOutletMeteredStatusPeakPowerTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPeakPowerTimeStamp.setStatus("current")
_PduOutletMeteredStatusPeakPowerStartTime_Type = DisplayString
_PduOutletMeteredStatusPeakPowerStartTime_Object = MibTableColumn
pduOutletMeteredStatusPeakPowerStartTime = _PduOutletMeteredStatusPeakPowerStartTime_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 10),
    _PduOutletMeteredStatusPeakPowerStartTime_Type()
)
pduOutletMeteredStatusPeakPowerStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusPeakPowerStartTime.setStatus("current")
_PduOutletMeteredStatusResettableEnergy_Type = Integer32
_PduOutletMeteredStatusResettableEnergy_Object = MibTableColumn
pduOutletMeteredStatusResettableEnergy = _PduOutletMeteredStatusResettableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 5, 9, 1, 11),
    _PduOutletMeteredStatusResettableEnergy_Type()
)
pduOutletMeteredStatusResettableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduOutletMeteredStatusResettableEnergy.setStatus("current")
_PduExternalSensor_ObjectIdentity = ObjectIdentity
pduExternalSensor = _PduExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6)
)


class _PduExternalSensorTableSize_Type(Integer32):
    """Custom type pduExternalSensorTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduExternalSensorTableSize_Type.__name__ = "Integer32"
_PduExternalSensorTableSize_Object = MibScalar
pduExternalSensorTableSize = _PduExternalSensorTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 1),
    _PduExternalSensorTableSize_Type()
)
pduExternalSensorTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorTableSize.setStatus("current")
_PduExternalSensorNamePlateTable_Object = MibTable
pduExternalSensorNamePlateTable = _PduExternalSensorNamePlateTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2)
)
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateTable.setStatus("current")
_PduExternalSensorNamePlateEntry_Object = MibTableRow
pduExternalSensorNamePlateEntry = _PduExternalSensorNamePlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1)
)
pduExternalSensorNamePlateEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduNamePlateIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduExternalSensorNamePlateIndex"),
)
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateEntry.setStatus("current")


class _PduExternalSensorNamePlateIndex_Type(Integer32):
    """Custom type pduExternalSensorNamePlateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExternalSensorNamePlateIndex_Type.__name__ = "Integer32"
_PduExternalSensorNamePlateIndex_Object = MibTableColumn
pduExternalSensorNamePlateIndex = _PduExternalSensorNamePlateIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 1),
    _PduExternalSensorNamePlateIndex_Type()
)
pduExternalSensorNamePlateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateIndex.setStatus("current")
_PduExternalSensorNamePlateName_Type = DisplayString
_PduExternalSensorNamePlateName_Object = MibTableColumn
pduExternalSensorNamePlateName = _PduExternalSensorNamePlateName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 2),
    _PduExternalSensorNamePlateName_Type()
)
pduExternalSensorNamePlateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateName.setStatus("current")
_PduExternalSensorNamePlateDescription_Type = DisplayString
_PduExternalSensorNamePlateDescription_Object = MibTableColumn
pduExternalSensorNamePlateDescription = _PduExternalSensorNamePlateDescription_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 3),
    _PduExternalSensorNamePlateDescription_Type()
)
pduExternalSensorNamePlateDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateDescription.setStatus("current")
_PduExternalSensorNamePlateLocation_Type = DisplayString
_PduExternalSensorNamePlateLocation_Object = MibTableColumn
pduExternalSensorNamePlateLocation = _PduExternalSensorNamePlateLocation_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 4),
    _PduExternalSensorNamePlateLocation_Type()
)
pduExternalSensorNamePlateLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateLocation.setStatus("current")
_PduExternalSensorNamePlateSerialNumber_Type = DisplayString
_PduExternalSensorNamePlateSerialNumber_Object = MibTableColumn
pduExternalSensorNamePlateSerialNumber = _PduExternalSensorNamePlateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 5),
    _PduExternalSensorNamePlateSerialNumber_Type()
)
pduExternalSensorNamePlateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateSerialNumber.setStatus("current")


class _PduExternalSensorNamePlateType_Type(Integer32):
    """Custom type pduExternalSensorNamePlateType based on Integer32"""
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
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("airVelocity", 9),
          ("beacon", 8),
          ("doorSwitch", 3),
          ("dryContact", 4),
          ("hidAdapter", 18),
          ("humidity", 2),
          ("modbusAdapter", 17),
          ("ropeFluid", 6),
          ("smoke", 7),
          ("spotFluid", 5),
          ("temperature", 1))
    )


_PduExternalSensorNamePlateType_Type.__name__ = "Integer32"
_PduExternalSensorNamePlateType_Object = MibTableColumn
pduExternalSensorNamePlateType = _PduExternalSensorNamePlateType_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 6),
    _PduExternalSensorNamePlateType_Type()
)
pduExternalSensorNamePlateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateType.setStatus("current")


class _PduExternalSensorNamePlateUnits_Type(Integer32):
    """Custom type pduExternalSensorNamePlateUnits based on Integer32"""
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
        *(("degreeC", 1),
          ("degreeF", 2),
          ("logic", 0),
          ("mps", 4),
          ("percent", 3))
    )


_PduExternalSensorNamePlateUnits_Type.__name__ = "Integer32"
_PduExternalSensorNamePlateUnits_Object = MibTableColumn
pduExternalSensorNamePlateUnits = _PduExternalSensorNamePlateUnits_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 7),
    _PduExternalSensorNamePlateUnits_Type()
)
pduExternalSensorNamePlateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateUnits.setStatus("current")
_PduExternalSensorNamePlateIdentifier_Type = Integer32
_PduExternalSensorNamePlateIdentifier_Object = MibTableColumn
pduExternalSensorNamePlateIdentifier = _PduExternalSensorNamePlateIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 2, 1, 8),
    _PduExternalSensorNamePlateIdentifier_Type()
)
pduExternalSensorNamePlateIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorNamePlateIdentifier.setStatus("current")
_PduExternalSensorConfigTable_Object = MibTable
pduExternalSensorConfigTable = _PduExternalSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3)
)
if mibBuilder.loadTexts:
    pduExternalSensorConfigTable.setStatus("current")
_PduExternalSensorConfigEntry_Object = MibTableRow
pduExternalSensorConfigEntry = _PduExternalSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1)
)
pduExternalSensorConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduExternalSensorConfigIndex"),
)
if mibBuilder.loadTexts:
    pduExternalSensorConfigEntry.setStatus("current")


class _PduExternalSensorConfigIndex_Type(Integer32):
    """Custom type pduExternalSensorConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExternalSensorConfigIndex_Type.__name__ = "Integer32"
_PduExternalSensorConfigIndex_Object = MibTableColumn
pduExternalSensorConfigIndex = _PduExternalSensorConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 1),
    _PduExternalSensorConfigIndex_Type()
)
pduExternalSensorConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExternalSensorConfigIndex.setStatus("current")
_PduExternalSensorConfigLowerCriticalThreshold_Type = Unsigned32
_PduExternalSensorConfigLowerCriticalThreshold_Object = MibTableColumn
pduExternalSensorConfigLowerCriticalThreshold = _PduExternalSensorConfigLowerCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 2),
    _PduExternalSensorConfigLowerCriticalThreshold_Type()
)
pduExternalSensorConfigLowerCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigLowerCriticalThreshold.setStatus("current")
_PduExternalSensorConfigLowerWarningThreshold_Type = Unsigned32
_PduExternalSensorConfigLowerWarningThreshold_Object = MibTableColumn
pduExternalSensorConfigLowerWarningThreshold = _PduExternalSensorConfigLowerWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 3),
    _PduExternalSensorConfigLowerWarningThreshold_Type()
)
pduExternalSensorConfigLowerWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigLowerWarningThreshold.setStatus("current")
_PduExternalSensorConfigUpperCriticalThreshold_Type = Unsigned32
_PduExternalSensorConfigUpperCriticalThreshold_Object = MibTableColumn
pduExternalSensorConfigUpperCriticalThreshold = _PduExternalSensorConfigUpperCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 4),
    _PduExternalSensorConfigUpperCriticalThreshold_Type()
)
pduExternalSensorConfigUpperCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigUpperCriticalThreshold.setStatus("current")
_PduExternalSensorConfigUpperWarningThreshold_Type = Unsigned32
_PduExternalSensorConfigUpperWarningThreshold_Object = MibTableColumn
pduExternalSensorConfigUpperWarningThreshold = _PduExternalSensorConfigUpperWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 5),
    _PduExternalSensorConfigUpperWarningThreshold_Type()
)
pduExternalSensorConfigUpperWarningThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigUpperWarningThreshold.setStatus("current")
_PduExternalSensorConfigAlarmResetThreshold_Type = Unsigned32
_PduExternalSensorConfigAlarmResetThreshold_Object = MibTableColumn
pduExternalSensorConfigAlarmResetThreshold = _PduExternalSensorConfigAlarmResetThreshold_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 6),
    _PduExternalSensorConfigAlarmResetThreshold_Type()
)
pduExternalSensorConfigAlarmResetThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigAlarmResetThreshold.setStatus("current")
_PduExternalSensorConfigAlarmStateChangeDelay_Type = Unsigned32
_PduExternalSensorConfigAlarmStateChangeDelay_Object = MibTableColumn
pduExternalSensorConfigAlarmStateChangeDelay = _PduExternalSensorConfigAlarmStateChangeDelay_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 7),
    _PduExternalSensorConfigAlarmStateChangeDelay_Type()
)
pduExternalSensorConfigAlarmStateChangeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigAlarmStateChangeDelay.setStatus("current")


class _PduExternalSensorConfigEnabledThresholds_Type(Bits):
    """Custom type pduExternalSensorConfigEnabledThresholds based on Bits"""
    namedValues = NamedValues(
        *(("binarySensorAlarm", 4),
          ("lowerCritical", 0),
          ("lowerWarning", 1),
          ("upperCritical", 3),
          ("upperWarning", 2))
    )

_PduExternalSensorConfigEnabledThresholds_Type.__name__ = "Bits"
_PduExternalSensorConfigEnabledThresholds_Object = MibTableColumn
pduExternalSensorConfigEnabledThresholds = _PduExternalSensorConfigEnabledThresholds_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 8),
    _PduExternalSensorConfigEnabledThresholds_Type()
)
pduExternalSensorConfigEnabledThresholds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigEnabledThresholds.setStatus("current")


class _PduExternalSensorConfigAlarmState_Type(Integer32):
    """Custom type pduExternalSensorConfigAlarmState based on Integer32"""
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


_PduExternalSensorConfigAlarmState_Type.__name__ = "Integer32"
_PduExternalSensorConfigAlarmState_Object = MibTableColumn
pduExternalSensorConfigAlarmState = _PduExternalSensorConfigAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 3, 1, 9),
    _PduExternalSensorConfigAlarmState_Type()
)
pduExternalSensorConfigAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorConfigAlarmState.setStatus("current")
_PduExternalSensorStatusTable_Object = MibTable
pduExternalSensorStatusTable = _PduExternalSensorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4)
)
if mibBuilder.loadTexts:
    pduExternalSensorStatusTable.setStatus("current")
_PduExternalSensorStatusEntry_Object = MibTableRow
pduExternalSensorStatusEntry = _PduExternalSensorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1)
)
pduExternalSensorStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduExternalSensorStatusIndex"),
)
if mibBuilder.loadTexts:
    pduExternalSensorStatusEntry.setStatus("current")


class _PduExternalSensorStatusIndex_Type(Integer32):
    """Custom type pduExternalSensorStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduExternalSensorStatusIndex_Type.__name__ = "Integer32"
_PduExternalSensorStatusIndex_Object = MibTableColumn
pduExternalSensorStatusIndex = _PduExternalSensorStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 1),
    _PduExternalSensorStatusIndex_Type()
)
pduExternalSensorStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduExternalSensorStatusIndex.setStatus("current")
_PduExternalSensorStatusName_Type = DisplayString
_PduExternalSensorStatusName_Object = MibTableColumn
pduExternalSensorStatusName = _PduExternalSensorStatusName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 2),
    _PduExternalSensorStatusName_Type()
)
pduExternalSensorStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusName.setStatus("current")


class _PduExternalSensorStatusAisle_Type(Integer32):
    """Custom type pduExternalSensorStatusAisle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldAisle", 2),
          ("hotAisle", 1))
    )


_PduExternalSensorStatusAisle_Type.__name__ = "Integer32"
_PduExternalSensorStatusAisle_Object = MibTableColumn
pduExternalSensorStatusAisle = _PduExternalSensorStatusAisle_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 3),
    _PduExternalSensorStatusAisle_Type()
)
pduExternalSensorStatusAisle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduExternalSensorStatusAisle.setStatus("current")


class _PduExternalSensorStatusCommStatus_Type(Integer32):
    """Custom type pduExternalSensorStatusCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commsLost", 3),
          ("commsOk", 2),
          ("notInstalled", 1))
    )


_PduExternalSensorStatusCommStatus_Type.__name__ = "Integer32"
_PduExternalSensorStatusCommStatus_Object = MibTableColumn
pduExternalSensorStatusCommStatus = _PduExternalSensorStatusCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 4),
    _PduExternalSensorStatusCommStatus_Type()
)
pduExternalSensorStatusCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusCommStatus.setStatus("current")


class _PduExternalSensorStatusState_Type(Integer32):
    """Custom type pduExternalSensorStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aboveUpperCritical", 6),
          ("aboveUpperWarning", 5),
          ("alarmed", 1),
          ("belowLowerCritical", 3),
          ("belowLowerWarning", 4),
          ("normal", 2),
          ("notPresent", 0))
    )


_PduExternalSensorStatusState_Type.__name__ = "Integer32"
_PduExternalSensorStatusState_Object = MibTableColumn
pduExternalSensorStatusState = _PduExternalSensorStatusState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 5),
    _PduExternalSensorStatusState_Type()
)
pduExternalSensorStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusState.setStatus("current")
_PduExternalSensorStatusValue_Type = Integer32
_PduExternalSensorStatusValue_Object = MibTableColumn
pduExternalSensorStatusValue = _PduExternalSensorStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 6),
    _PduExternalSensorStatusValue_Type()
)
pduExternalSensorStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusValue.setStatus("current")
_PduExternalSensorStatusTimeStamp_Type = DisplayString
_PduExternalSensorStatusTimeStamp_Object = MibTableColumn
pduExternalSensorStatusTimeStamp = _PduExternalSensorStatusTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 7),
    _PduExternalSensorStatusTimeStamp_Type()
)
pduExternalSensorStatusTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusTimeStamp.setStatus("current")
_PduExternalSensorStatusHighPrecisionValue_Type = Integer32
_PduExternalSensorStatusHighPrecisionValue_Object = MibTableColumn
pduExternalSensorStatusHighPrecisionValue = _PduExternalSensorStatusHighPrecisionValue_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 6, 4, 1, 8),
    _PduExternalSensorStatusHighPrecisionValue_Type()
)
pduExternalSensorStatusHighPrecisionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduExternalSensorStatusHighPrecisionValue.setStatus("current")
_PduServerPing_ObjectIdentity = ObjectIdentity
pduServerPing = _PduServerPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 7)
)


class _PduServerPingTableSize_Type(Integer32):
    """Custom type pduServerPingTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduServerPingTableSize_Type.__name__ = "Integer32"
_PduServerPingTableSize_Object = MibScalar
pduServerPingTableSize = _PduServerPingTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 7, 1),
    _PduServerPingTableSize_Type()
)
pduServerPingTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduServerPingTableSize.setStatus("current")
_PduServerPingTable_Object = MibTable
pduServerPingTable = _PduServerPingTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 7, 2)
)
if mibBuilder.loadTexts:
    pduServerPingTable.setStatus("current")
_PduServerPingEntry_Object = MibTableRow
pduServerPingEntry = _PduServerPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 7, 2, 1)
)
pduServerPingEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduServerPingIndex"),
)
if mibBuilder.loadTexts:
    pduServerPingEntry.setStatus("current")


class _PduServerPingIndex_Type(Integer32):
    """Custom type pduServerPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduServerPingIndex_Type.__name__ = "Integer32"
_PduServerPingIndex_Object = MibTableColumn
pduServerPingIndex = _PduServerPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 7, 2, 1, 1),
    _PduServerPingIndex_Type()
)
pduServerPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduServerPingIndex.setStatus("current")
_PduServerPingServerIPAddress_Type = DisplayString
_PduServerPingServerIPAddress_Object = MibTableColumn
pduServerPingServerIPAddress = _PduServerPingServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 7, 2, 1, 2),
    _PduServerPingServerIPAddress_Type()
)
pduServerPingServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduServerPingServerIPAddress.setStatus("current")


class _PduServerPingEnabled_Type(Integer32):
    """Custom type pduServerPingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PduServerPingEnabled_Type.__name__ = "Integer32"
_PduServerPingEnabled_Object = MibTableColumn
pduServerPingEnabled = _PduServerPingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 7, 2, 1, 3),
    _PduServerPingEnabled_Type()
)
pduServerPingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduServerPingEnabled.setStatus("current")
_PduSmartCabinet_ObjectIdentity = ObjectIdentity
pduSmartCabinet = _PduSmartCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8)
)


class _PduUnitSmartCabinetTableSize_Type(Integer32):
    """Custom type pduUnitSmartCabinetTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PduUnitSmartCabinetTableSize_Type.__name__ = "Integer32"
_PduUnitSmartCabinetTableSize_Object = MibScalar
pduUnitSmartCabinetTableSize = _PduUnitSmartCabinetTableSize_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 1),
    _PduUnitSmartCabinetTableSize_Type()
)
pduUnitSmartCabinetTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetTableSize.setStatus("current")
_PduUnitSmartCabinetTable_Object = MibTable
pduUnitSmartCabinetTable = _PduUnitSmartCabinetTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 2)
)
if mibBuilder.loadTexts:
    pduUnitSmartCabinetTable.setStatus("current")
_PduUnitSmartCabinetEntry_Object = MibTableRow
pduUnitSmartCabinetEntry = _PduUnitSmartCabinetEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 2, 1)
)
pduUnitSmartCabinetEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "pduUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "pduUnitSmartCabinetIndex"),
)
if mibBuilder.loadTexts:
    pduUnitSmartCabinetEntry.setStatus("current")


class _PduUnitSmartCabinetIndex_Type(Integer32):
    """Custom type pduUnitSmartCabinetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_PduUnitSmartCabinetIndex_Type.__name__ = "Integer32"
_PduUnitSmartCabinetIndex_Object = MibTableColumn
pduUnitSmartCabinetIndex = _PduUnitSmartCabinetIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 2, 1, 1),
    _PduUnitSmartCabinetIndex_Type()
)
pduUnitSmartCabinetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetIndex.setStatus("current")
_PduUnitSmartCabinetCardUserName_Type = DisplayString
_PduUnitSmartCabinetCardUserName_Object = MibTableColumn
pduUnitSmartCabinetCardUserName = _PduUnitSmartCabinetCardUserName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 2, 1, 2),
    _PduUnitSmartCabinetCardUserName_Type()
)
pduUnitSmartCabinetCardUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetCardUserName.setStatus("current")
_PduUnitSmartCabinetCardID_Type = Integer32
_PduUnitSmartCabinetCardID_Object = MibTableColumn
pduUnitSmartCabinetCardID = _PduUnitSmartCabinetCardID_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 2, 1, 3),
    _PduUnitSmartCabinetCardID_Type()
)
pduUnitSmartCabinetCardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetCardID.setStatus("current")
_PduUnitSmartCabinetTimestamp_Type = DisplayString
_PduUnitSmartCabinetTimestamp_Object = MibTableColumn
pduUnitSmartCabinetTimestamp = _PduUnitSmartCabinetTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 2, 1, 4),
    _PduUnitSmartCabinetTimestamp_Type()
)
pduUnitSmartCabinetTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetTimestamp.setStatus("current")


class _PduUnitSmartCabinetDoor_Type(Integer32):
    """Custom type pduUnitSmartCabinetDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ColdAisle", 2),
          ("HotAisle", 1))
    )


_PduUnitSmartCabinetDoor_Type.__name__ = "Integer32"
_PduUnitSmartCabinetDoor_Object = MibTableColumn
pduUnitSmartCabinetDoor = _PduUnitSmartCabinetDoor_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 2, 1, 5),
    _PduUnitSmartCabinetDoor_Type()
)
pduUnitSmartCabinetDoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetDoor.setStatus("current")
_PduUnitSmartCabinetControl_ObjectIdentity = ObjectIdentity
pduUnitSmartCabinetControl = _PduUnitSmartCabinetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3)
)
_PduUnitSmartCabinetControlUserName_Type = DisplayString
_PduUnitSmartCabinetControlUserName_Object = MibScalar
pduUnitSmartCabinetControlUserName = _PduUnitSmartCabinetControlUserName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3, 1),
    _PduUnitSmartCabinetControlUserName_Type()
)
pduUnitSmartCabinetControlUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlUserName.setStatus("current")
_PduUnitSmartCabinetControlCardID_Type = Integer32
_PduUnitSmartCabinetControlCardID_Object = MibScalar
pduUnitSmartCabinetControlCardID = _PduUnitSmartCabinetControlCardID_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3, 2),
    _PduUnitSmartCabinetControlCardID_Type()
)
pduUnitSmartCabinetControlCardID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlCardID.setStatus("current")
_PduUnitSmartCabinetControlTimestamp_Type = DisplayString
_PduUnitSmartCabinetControlTimestamp_Object = MibScalar
pduUnitSmartCabinetControlTimestamp = _PduUnitSmartCabinetControlTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3, 3),
    _PduUnitSmartCabinetControlTimestamp_Type()
)
pduUnitSmartCabinetControlTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlTimestamp.setStatus("current")


class _PduUnitSmartCabinetControlDoor_Type(Integer32):
    """Custom type pduUnitSmartCabinetControlDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ColdAisle", 2),
          ("HotAisle", 1))
    )


_PduUnitSmartCabinetControlDoor_Type.__name__ = "Integer32"
_PduUnitSmartCabinetControlDoor_Object = MibScalar
pduUnitSmartCabinetControlDoor = _PduUnitSmartCabinetControlDoor_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3, 4),
    _PduUnitSmartCabinetControlDoor_Type()
)
pduUnitSmartCabinetControlDoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetControlDoor.setStatus("current")


class _PduUnitSmartCabinetCardIDEdit_Type(Integer32):
    """Custom type pduUnitSmartCabinetCardIDEdit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("grant", 0),
          ("remove", 1))
    )


_PduUnitSmartCabinetCardIDEdit_Type.__name__ = "Integer32"
_PduUnitSmartCabinetCardIDEdit_Object = MibScalar
pduUnitSmartCabinetCardIDEdit = _PduUnitSmartCabinetCardIDEdit_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3, 5),
    _PduUnitSmartCabinetCardIDEdit_Type()
)
pduUnitSmartCabinetCardIDEdit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetCardIDEdit.setStatus("current")


class _PduUnitSmartCabinetColdAisleLockState_Type(Integer32):
    """Custom type pduUnitSmartCabinetColdAisleLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("notPresent", 2),
          ("unlock", 0))
    )


_PduUnitSmartCabinetColdAisleLockState_Type.__name__ = "Integer32"
_PduUnitSmartCabinetColdAisleLockState_Object = MibScalar
pduUnitSmartCabinetColdAisleLockState = _PduUnitSmartCabinetColdAisleLockState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3, 6),
    _PduUnitSmartCabinetColdAisleLockState_Type()
)
pduUnitSmartCabinetColdAisleLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetColdAisleLockState.setStatus("current")


class _PduUnitSmartCabinetHotAisleLockState_Type(Integer32):
    """Custom type pduUnitSmartCabinetHotAisleLockState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("notPresent", 2),
          ("unlock", 0))
    )


_PduUnitSmartCabinetHotAisleLockState_Type.__name__ = "Integer32"
_PduUnitSmartCabinetHotAisleLockState_Object = MibScalar
pduUnitSmartCabinetHotAisleLockState = _PduUnitSmartCabinetHotAisleLockState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 8, 3, 7),
    _PduUnitSmartCabinetHotAisleLockState_Type()
)
pduUnitSmartCabinetHotAisleLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pduUnitSmartCabinetHotAisleLockState.setStatus("current")
_PduTraps_ObjectIdentity = ObjectIdentity
pduTraps = _PduTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9)
)
_TrapsInfo_ObjectIdentity = ObjectIdentity
trapsInfo = _TrapsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1)
)
_TrapsInfoTable_Object = MibTable
trapsInfoTable = _TrapsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    trapsInfoTable.setStatus("current")
_TrapsInfoEntry_Object = MibTableRow
trapsInfoEntry = _TrapsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1)
)
trapsInfoEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "trapsInfoIndex"),
)
if mibBuilder.loadTexts:
    trapsInfoEntry.setStatus("current")


class _TrapsInfoIndex_Type(Integer32):
    """Custom type trapsInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_TrapsInfoIndex_Type.__name__ = "Integer32"
_TrapsInfoIndex_Object = MibTableColumn
trapsInfoIndex = _TrapsInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1, 1),
    _TrapsInfoIndex_Type()
)
trapsInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapsInfoIndex.setStatus("current")
_UserName_Type = DisplayString
_UserName_Object = MibTableColumn
userName = _UserName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1, 2),
    _UserName_Type()
)
userName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userName.setStatus("current")
_UserUpdated_Type = DisplayString
_UserUpdated_Object = MibTableColumn
userUpdated = _UserUpdated_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1, 3),
    _UserUpdated_Type()
)
userUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    userUpdated.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_RoleUpdated_Type = DisplayString
_RoleUpdated_Object = MibTableColumn
roleUpdated = _RoleUpdated_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1, 5),
    _RoleUpdated_Type()
)
roleUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    roleUpdated.setStatus("current")
_SmtpRecipients_Type = DisplayString
_SmtpRecipients_Object = MibTableColumn
smtpRecipients = _SmtpRecipients_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1, 6),
    _SmtpRecipients_Type()
)
smtpRecipients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpRecipients.setStatus("current")
_SmtpServer_Type = DisplayString
_SmtpServer_Object = MibTableColumn
smtpServer = _SmtpServer_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 1, 1, 7),
    _SmtpServer_Type()
)
smtpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServer.setStatus("current")
_PduIndex_Type = Integer32
_PduIndex_Object = MibScalar
pduIndex = _PduIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 2),
    _PduIndex_Type()
)
pduIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pduIndex.setStatus("current")
_ExternalSensorIndex_Type = Integer32
_ExternalSensorIndex_Object = MibScalar
externalSensorIndex = _ExternalSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 3),
    _ExternalSensorIndex_Type()
)
externalSensorIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    externalSensorIndex.setStatus("current")


class _ServerPing_Type(Integer32):
    """Custom type serverPing based on Integer32"""
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
        *(("pingDisable", 2),
          ("pingEnable", 1),
          ("serverNotReachable", 4),
          ("serverReachable", 3))
    )


_ServerPing_Type.__name__ = "Integer32"
_ServerPing_Object = MibScalar
serverPing = _ServerPing_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 4),
    _ServerPing_Type()
)
serverPing.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    serverPing.setStatus("current")


class _UsbDevice_Type(Integer32):
    """Custom type usbDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_UsbDevice_Type.__name__ = "Integer32"
_UsbDevice_Object = MibScalar
usbDevice = _UsbDevice_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 5),
    _UsbDevice_Type()
)
usbDevice.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usbDevice.setStatus("current")
_ErrorDescription_Type = DisplayString
_ErrorDescription_Object = MibScalar
errorDescription = _ErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 6),
    _ErrorDescription_Type()
)
errorDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    errorDescription.setStatus("current")


class _DaisyChain_Type(Integer32):
    """Custom type daisyChain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_DaisyChain_Type.__name__ = "Integer32"
_DaisyChain_Object = MibScalar
daisyChain = _DaisyChain_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 7),
    _DaisyChain_Type()
)
daisyChain.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    daisyChain.setStatus("current")


class _SystemCommunication_Type(Integer32):
    """Custom type systemCommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lost", 2),
          ("ok", 1))
    )


_SystemCommunication_Type.__name__ = "Integer32"
_SystemCommunication_Object = MibScalar
systemCommunication = _SystemCommunication_Object(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 1, 8),
    _SystemCommunication_Type()
)
systemCommunication.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemCommunication.setStatus("current")
_Esp_ObjectIdentity = ObjectIdentity
esp = _Esp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 2)
)
_EspNamePlate_ObjectIdentity = ObjectIdentity
espNamePlate = _EspNamePlate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1)
)
_EspNamePlateTable_Object = MibTable
espNamePlateTable = _EspNamePlateTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2)
)
if mibBuilder.loadTexts:
    espNamePlateTable.setStatus("current")
_EspNamePlateEntry_Object = MibTableRow
espNamePlateEntry = _EspNamePlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1)
)
espNamePlateEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espNamePlateIndex"),
)
if mibBuilder.loadTexts:
    espNamePlateEntry.setStatus("current")


class _EspNamePlateIndex_Type(Integer32):
    """Custom type espNamePlateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspNamePlateIndex_Type.__name__ = "Integer32"
_EspNamePlateIndex_Object = MibTableColumn
espNamePlateIndex = _EspNamePlateIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 1),
    _EspNamePlateIndex_Type()
)
espNamePlateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espNamePlateIndex.setStatus("current")
_EspNamePlateName_Type = DisplayString
_EspNamePlateName_Object = MibTableColumn
espNamePlateName = _EspNamePlateName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 2),
    _EspNamePlateName_Type()
)
espNamePlateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateName.setStatus("current")
_EspNamePlateLocation_Type = DisplayString
_EspNamePlateLocation_Object = MibTableColumn
espNamePlateLocation = _EspNamePlateLocation_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 3),
    _EspNamePlateLocation_Type()
)
espNamePlateLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateLocation.setStatus("current")
_EspNamePlateInetAddressType_Type = InetAddressType
_EspNamePlateInetAddressType_Object = MibTableColumn
espNamePlateInetAddressType = _EspNamePlateInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 4),
    _EspNamePlateInetAddressType_Type()
)
espNamePlateInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateInetAddressType.setStatus("current")
_EspNamePlateIPAddress_Type = InetAddress
_EspNamePlateIPAddress_Object = MibTableColumn
espNamePlateIPAddress = _EspNamePlateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 5),
    _EspNamePlateIPAddress_Type()
)
espNamePlateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateIPAddress.setStatus("current")
_EspNamePlateInetNetMask_Type = InetAddress
_EspNamePlateInetNetMask_Object = MibTableColumn
espNamePlateInetNetMask = _EspNamePlateInetNetMask_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 6),
    _EspNamePlateInetNetMask_Type()
)
espNamePlateInetNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateInetNetMask.setStatus("current")
_EspNamePlateInetGateway_Type = InetAddress
_EspNamePlateInetGateway_Object = MibTableColumn
espNamePlateInetGateway = _EspNamePlateInetGateway_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 7),
    _EspNamePlateInetGateway_Type()
)
espNamePlateInetGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateInetGateway.setStatus("current")
_EspNamePlateMACAddress_Type = MacAddress
_EspNamePlateMACAddress_Object = MibTableColumn
espNamePlateMACAddress = _EspNamePlateMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 8),
    _EspNamePlateMACAddress_Type()
)
espNamePlateMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateMACAddress.setStatus("current")
_EspNamePlateUTCTimeOffset_Type = DisplayString
_EspNamePlateUTCTimeOffset_Object = MibTableColumn
espNamePlateUTCTimeOffset = _EspNamePlateUTCTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 9),
    _EspNamePlateUTCTimeOffset_Type()
)
espNamePlateUTCTimeOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateUTCTimeOffset.setStatus("current")
_EspNamePlateModelNumber_Type = DisplayString
_EspNamePlateModelNumber_Object = MibTableColumn
espNamePlateModelNumber = _EspNamePlateModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 10),
    _EspNamePlateModelNumber_Type()
)
espNamePlateModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateModelNumber.setStatus("current")
_EspNamePlateSerialNumber_Type = DisplayString
_EspNamePlateSerialNumber_Object = MibTableColumn
espNamePlateSerialNumber = _EspNamePlateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 11),
    _EspNamePlateSerialNumber_Type()
)
espNamePlateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateSerialNumber.setStatus("current")
_EspNamePlateDateofManufacture_Type = DisplayString
_EspNamePlateDateofManufacture_Object = MibTableColumn
espNamePlateDateofManufacture = _EspNamePlateDateofManufacture_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 12),
    _EspNamePlateDateofManufacture_Type()
)
espNamePlateDateofManufacture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateDateofManufacture.setStatus("current")
_EspNamePlateFirmwareVersion_Type = DisplayString
_EspNamePlateFirmwareVersion_Object = MibTableColumn
espNamePlateFirmwareVersion = _EspNamePlateFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 13),
    _EspNamePlateFirmwareVersion_Type()
)
espNamePlateFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateFirmwareVersion.setStatus("current")
_EspNamePlateFirmwareVersionTimeStamp_Type = DisplayString
_EspNamePlateFirmwareVersionTimeStamp_Object = MibTableColumn
espNamePlateFirmwareVersionTimeStamp = _EspNamePlateFirmwareVersionTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 14),
    _EspNamePlateFirmwareVersionTimeStamp_Type()
)
espNamePlateFirmwareVersionTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateFirmwareVersionTimeStamp.setStatus("current")


class _EspNamePlateType_Type(Integer32):
    """Custom type espNamePlateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inlineMeter", 1),
          ("pdu", 0))
    )


_EspNamePlateType_Type.__name__ = "Integer32"
_EspNamePlateType_Object = MibTableColumn
espNamePlateType = _EspNamePlateType_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 1, 2, 1, 15),
    _EspNamePlateType_Type()
)
espNamePlateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espNamePlateType.setStatus("current")
_EspUnit_ObjectIdentity = ObjectIdentity
espUnit = _EspUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2)
)
_EspUnitConfigTable_Object = MibTable
espUnitConfigTable = _EspUnitConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 2)
)
if mibBuilder.loadTexts:
    espUnitConfigTable.setStatus("current")
_EspUnitConfigEntry_Object = MibTableRow
espUnitConfigEntry = _EspUnitConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 2, 1)
)
espUnitConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitConfigIndex"),
)
if mibBuilder.loadTexts:
    espUnitConfigEntry.setStatus("current")


class _EspUnitConfigIndex_Type(Integer32):
    """Custom type espUnitConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspUnitConfigIndex_Type.__name__ = "Integer32"
_EspUnitConfigIndex_Object = MibTableColumn
espUnitConfigIndex = _EspUnitConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 2, 1, 1),
    _EspUnitConfigIndex_Type()
)
espUnitConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espUnitConfigIndex.setStatus("current")
_EspUnitConfigName_Type = DisplayString
_EspUnitConfigName_Object = MibTableColumn
espUnitConfigName = _EspUnitConfigName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 2, 1, 2),
    _EspUnitConfigName_Type()
)
espUnitConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espUnitConfigName.setStatus("current")
_EspUnitConfigLocation_Type = DisplayString
_EspUnitConfigLocation_Object = MibTableColumn
espUnitConfigLocation = _EspUnitConfigLocation_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 2, 1, 3),
    _EspUnitConfigLocation_Type()
)
espUnitConfigLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espUnitConfigLocation.setStatus("current")


class _EspUnitConfigEnergyReset_Type(Integer32):
    """Custom type espUnitConfigEnergyReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 1),
          ("notSupported", 3),
          ("reset", 2))
    )


_EspUnitConfigEnergyReset_Type.__name__ = "Integer32"
_EspUnitConfigEnergyReset_Object = MibTableColumn
espUnitConfigEnergyReset = _EspUnitConfigEnergyReset_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 2, 1, 15),
    _EspUnitConfigEnergyReset_Type()
)
espUnitConfigEnergyReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espUnitConfigEnergyReset.setStatus("current")


class _EspUnitConfigResetNetworkManagementCard_Type(Integer32):
    """Custom type espUnitConfigResetNetworkManagementCard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("reset", 1))
    )


_EspUnitConfigResetNetworkManagementCard_Type.__name__ = "Integer32"
_EspUnitConfigResetNetworkManagementCard_Object = MibTableColumn
espUnitConfigResetNetworkManagementCard = _EspUnitConfigResetNetworkManagementCard_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 2, 1, 20),
    _EspUnitConfigResetNetworkManagementCard_Type()
)
espUnitConfigResetNetworkManagementCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espUnitConfigResetNetworkManagementCard.setStatus("current")
_EspUnitPropertiesTable_Object = MibTable
espUnitPropertiesTable = _EspUnitPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3)
)
if mibBuilder.loadTexts:
    espUnitPropertiesTable.setStatus("current")
_EspUnitPropertiesEntry_Object = MibTableRow
espUnitPropertiesEntry = _EspUnitPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1)
)
espUnitPropertiesEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitPropertiesIndex"),
)
if mibBuilder.loadTexts:
    espUnitPropertiesEntry.setStatus("current")


class _EspUnitPropertiesIndex_Type(Integer32):
    """Custom type espUnitPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspUnitPropertiesIndex_Type.__name__ = "Integer32"
_EspUnitPropertiesIndex_Object = MibTableColumn
espUnitPropertiesIndex = _EspUnitPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 1),
    _EspUnitPropertiesIndex_Type()
)
espUnitPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espUnitPropertiesIndex.setStatus("current")
_EspUnitPropertiesName_Type = DisplayString
_EspUnitPropertiesName_Object = MibTableColumn
espUnitPropertiesName = _EspUnitPropertiesName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 2),
    _EspUnitPropertiesName_Type()
)
espUnitPropertiesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesName.setStatus("current")


class _EspUnitPropertiesOutletCount_Type(Integer32):
    """Custom type espUnitPropertiesOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspUnitPropertiesOutletCount_Type.__name__ = "Integer32"
_EspUnitPropertiesOutletCount_Object = MibTableColumn
espUnitPropertiesOutletCount = _EspUnitPropertiesOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 3),
    _EspUnitPropertiesOutletCount_Type()
)
espUnitPropertiesOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesOutletCount.setStatus("current")


class _EspUnitPropertiesSwitchedOutletCount_Type(Integer32):
    """Custom type espUnitPropertiesSwitchedOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspUnitPropertiesSwitchedOutletCount_Type.__name__ = "Integer32"
_EspUnitPropertiesSwitchedOutletCount_Object = MibTableColumn
espUnitPropertiesSwitchedOutletCount = _EspUnitPropertiesSwitchedOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 4),
    _EspUnitPropertiesSwitchedOutletCount_Type()
)
espUnitPropertiesSwitchedOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesSwitchedOutletCount.setStatus("current")


class _EspUnitPropertiesMeteredOutletCount_Type(Integer32):
    """Custom type espUnitPropertiesMeteredOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspUnitPropertiesMeteredOutletCount_Type.__name__ = "Integer32"
_EspUnitPropertiesMeteredOutletCount_Object = MibTableColumn
espUnitPropertiesMeteredOutletCount = _EspUnitPropertiesMeteredOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 5),
    _EspUnitPropertiesMeteredOutletCount_Type()
)
espUnitPropertiesMeteredOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesMeteredOutletCount.setStatus("current")


class _EspUnitPropertiesInputPhaseCount_Type(Integer32):
    """Custom type espUnitPropertiesInputPhaseCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspUnitPropertiesInputPhaseCount_Type.__name__ = "Integer32"
_EspUnitPropertiesInputPhaseCount_Object = MibTableColumn
espUnitPropertiesInputPhaseCount = _EspUnitPropertiesInputPhaseCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 6),
    _EspUnitPropertiesInputPhaseCount_Type()
)
espUnitPropertiesInputPhaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesInputPhaseCount.setStatus("current")


class _EspUnitPropertiesCircuitBreakerCount_Type(Integer32):
    """Custom type espUnitPropertiesCircuitBreakerCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspUnitPropertiesCircuitBreakerCount_Type.__name__ = "Integer32"
_EspUnitPropertiesCircuitBreakerCount_Object = MibTableColumn
espUnitPropertiesCircuitBreakerCount = _EspUnitPropertiesCircuitBreakerCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 7),
    _EspUnitPropertiesCircuitBreakerCount_Type()
)
espUnitPropertiesCircuitBreakerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesCircuitBreakerCount.setStatus("current")


class _EspUnitPropertiesMaxExternalSensorCount_Type(Integer32):
    """Custom type espUnitPropertiesMaxExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspUnitPropertiesMaxExternalSensorCount_Type.__name__ = "Integer32"
_EspUnitPropertiesMaxExternalSensorCount_Object = MibTableColumn
espUnitPropertiesMaxExternalSensorCount = _EspUnitPropertiesMaxExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 8),
    _EspUnitPropertiesMaxExternalSensorCount_Type()
)
espUnitPropertiesMaxExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesMaxExternalSensorCount.setStatus("current")


class _EspUnitPropertiesConnExternalSensorCount_Type(Integer32):
    """Custom type espUnitPropertiesConnExternalSensorCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspUnitPropertiesConnExternalSensorCount_Type.__name__ = "Integer32"
_EspUnitPropertiesConnExternalSensorCount_Object = MibTableColumn
espUnitPropertiesConnExternalSensorCount = _EspUnitPropertiesConnExternalSensorCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 9),
    _EspUnitPropertiesConnExternalSensorCount_Type()
)
espUnitPropertiesConnExternalSensorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesConnExternalSensorCount.setStatus("current")
_EspUnitPropertiesRatedVoltage_Type = DisplayString
_EspUnitPropertiesRatedVoltage_Object = MibTableColumn
espUnitPropertiesRatedVoltage = _EspUnitPropertiesRatedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 10),
    _EspUnitPropertiesRatedVoltage_Type()
)
espUnitPropertiesRatedVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesRatedVoltage.setStatus("current")
_EspUnitPropertiesRatedMaxCurrent_Type = DisplayString
_EspUnitPropertiesRatedMaxCurrent_Object = MibTableColumn
espUnitPropertiesRatedMaxCurrent = _EspUnitPropertiesRatedMaxCurrent_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 11),
    _EspUnitPropertiesRatedMaxCurrent_Type()
)
espUnitPropertiesRatedMaxCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesRatedMaxCurrent.setStatus("current")
_EspUnitPropertiesRatedFrequency_Type = DisplayString
_EspUnitPropertiesRatedFrequency_Object = MibTableColumn
espUnitPropertiesRatedFrequency = _EspUnitPropertiesRatedFrequency_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 12),
    _EspUnitPropertiesRatedFrequency_Type()
)
espUnitPropertiesRatedFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesRatedFrequency.setStatus("current")
_EspUnitPropertiesRatedPower_Type = DisplayString
_EspUnitPropertiesRatedPower_Object = MibTableColumn
espUnitPropertiesRatedPower = _EspUnitPropertiesRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 3, 1, 13),
    _EspUnitPropertiesRatedPower_Type()
)
espUnitPropertiesRatedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitPropertiesRatedPower.setStatus("current")
_EspUnitStatusTable_Object = MibTable
espUnitStatusTable = _EspUnitStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4)
)
if mibBuilder.loadTexts:
    espUnitStatusTable.setStatus("current")
_EspUnitStatusEntry_Object = MibTableRow
espUnitStatusEntry = _EspUnitStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1)
)
espUnitStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitStatusIndex"),
)
if mibBuilder.loadTexts:
    espUnitStatusEntry.setStatus("current")


class _EspUnitStatusIndex_Type(Integer32):
    """Custom type espUnitStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspUnitStatusIndex_Type.__name__ = "Integer32"
_EspUnitStatusIndex_Object = MibTableColumn
espUnitStatusIndex = _EspUnitStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 1),
    _EspUnitStatusIndex_Type()
)
espUnitStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espUnitStatusIndex.setStatus("current")
_EspUnitStatusName_Type = DisplayString
_EspUnitStatusName_Object = MibTableColumn
espUnitStatusName = _EspUnitStatusName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 2),
    _EspUnitStatusName_Type()
)
espUnitStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitStatusName.setStatus("current")


class _EspUnitStatusLoadState_Type(Integer32):
    """Custom type espUnitStatusLoadState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_EspUnitStatusLoadState_Type.__name__ = "Integer32"
_EspUnitStatusLoadState_Object = MibTableColumn
espUnitStatusLoadState = _EspUnitStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 3),
    _EspUnitStatusLoadState_Type()
)
espUnitStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitStatusLoadState.setStatus("current")
_EspUnitStatusActivePower_Type = Integer32
_EspUnitStatusActivePower_Object = MibTableColumn
espUnitStatusActivePower = _EspUnitStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 4),
    _EspUnitStatusActivePower_Type()
)
espUnitStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitStatusActivePower.setStatus("current")
_EspUnitStatusApparentPower_Type = Integer32
_EspUnitStatusApparentPower_Object = MibTableColumn
espUnitStatusApparentPower = _EspUnitStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 5),
    _EspUnitStatusApparentPower_Type()
)
espUnitStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitStatusApparentPower.setStatus("current")
_EspUnitStatusEnergy_Type = Integer32
_EspUnitStatusEnergy_Object = MibTableColumn
espUnitStatusEnergy = _EspUnitStatusEnergy_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 9),
    _EspUnitStatusEnergy_Type()
)
espUnitStatusEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitStatusEnergy.setStatus("current")
_EspUnitStatusResettableEnergy_Type = Integer32
_EspUnitStatusResettableEnergy_Object = MibTableColumn
espUnitStatusResettableEnergy = _EspUnitStatusResettableEnergy_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 10),
    _EspUnitStatusResettableEnergy_Type()
)
espUnitStatusResettableEnergy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitStatusResettableEnergy.setStatus("current")
_EspUnitStatusEnergyStartTime_Type = DisplayString
_EspUnitStatusEnergyStartTime_Object = MibTableColumn
espUnitStatusEnergyStartTime = _EspUnitStatusEnergyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 2, 4, 1, 11),
    _EspUnitStatusEnergyStartTime_Type()
)
espUnitStatusEnergyStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUnitStatusEnergyStartTime.setStatus("current")
_EspInputPhase_ObjectIdentity = ObjectIdentity
espInputPhase = _EspInputPhase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3)
)
_EspInputPhaseConfigTable_Object = MibTable
espInputPhaseConfigTable = _EspInputPhaseConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 2)
)
if mibBuilder.loadTexts:
    espInputPhaseConfigTable.setStatus("current")
_EspInputPhaseConfigEntry_Object = MibTableRow
espInputPhaseConfigEntry = _EspInputPhaseConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 2, 1)
)
espInputPhaseConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "espInputPhaseConfigIndex"),
)
if mibBuilder.loadTexts:
    espInputPhaseConfigEntry.setStatus("current")


class _EspInputPhaseConfigIndex_Type(Integer32):
    """Custom type espInputPhaseConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspInputPhaseConfigIndex_Type.__name__ = "Integer32"
_EspInputPhaseConfigIndex_Object = MibTableColumn
espInputPhaseConfigIndex = _EspInputPhaseConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 2, 1, 1),
    _EspInputPhaseConfigIndex_Type()
)
espInputPhaseConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espInputPhaseConfigIndex.setStatus("current")


class _EspInputPhaseConfigCount_Type(Integer32):
    """Custom type espInputPhaseConfigCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspInputPhaseConfigCount_Type.__name__ = "Integer32"
_EspInputPhaseConfigCount_Object = MibTableColumn
espInputPhaseConfigCount = _EspInputPhaseConfigCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 2, 1, 2),
    _EspInputPhaseConfigCount_Type()
)
espInputPhaseConfigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseConfigCount.setStatus("current")
_EspInputPhaseStatusTable_Object = MibTable
espInputPhaseStatusTable = _EspInputPhaseStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4)
)
if mibBuilder.loadTexts:
    espInputPhaseStatusTable.setStatus("current")
_EspInputPhaseStatusEntry_Object = MibTableRow
espInputPhaseStatusEntry = _EspInputPhaseStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1)
)
espInputPhaseStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "espInputPhaseStatusIndex"),
)
if mibBuilder.loadTexts:
    espInputPhaseStatusEntry.setStatus("current")


class _EspInputPhaseStatusIndex_Type(Integer32):
    """Custom type espInputPhaseStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspInputPhaseStatusIndex_Type.__name__ = "Integer32"
_EspInputPhaseStatusIndex_Object = MibTableColumn
espInputPhaseStatusIndex = _EspInputPhaseStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 1),
    _EspInputPhaseStatusIndex_Type()
)
espInputPhaseStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espInputPhaseStatusIndex.setStatus("current")


class _EspInputPhaseStatusCount_Type(Integer32):
    """Custom type espInputPhaseStatusCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspInputPhaseStatusCount_Type.__name__ = "Integer32"
_EspInputPhaseStatusCount_Object = MibTableColumn
espInputPhaseStatusCount = _EspInputPhaseStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 2),
    _EspInputPhaseStatusCount_Type()
)
espInputPhaseStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusCount.setStatus("current")


class _EspInputPhaseStatusCurrentState_Type(Integer32):
    """Custom type espInputPhaseStatusCurrentState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_EspInputPhaseStatusCurrentState_Type.__name__ = "Integer32"
_EspInputPhaseStatusCurrentState_Object = MibTableColumn
espInputPhaseStatusCurrentState = _EspInputPhaseStatusCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 3),
    _EspInputPhaseStatusCurrentState_Type()
)
espInputPhaseStatusCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusCurrentState.setStatus("current")


class _EspInputPhaseStatusVoltageState_Type(Integer32):
    """Custom type espInputPhaseStatusVoltageState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_EspInputPhaseStatusVoltageState_Type.__name__ = "Integer32"
_EspInputPhaseStatusVoltageState_Object = MibTableColumn
espInputPhaseStatusVoltageState = _EspInputPhaseStatusVoltageState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 4),
    _EspInputPhaseStatusVoltageState_Type()
)
espInputPhaseStatusVoltageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusVoltageState.setStatus("current")
_EspInputPhaseStatusCurrent_Type = Integer32
_EspInputPhaseStatusCurrent_Object = MibTableColumn
espInputPhaseStatusCurrent = _EspInputPhaseStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 5),
    _EspInputPhaseStatusCurrent_Type()
)
espInputPhaseStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusCurrent.setStatus("current")
_EspInputPhaseStatusVoltage_Type = Integer32
_EspInputPhaseStatusVoltage_Object = MibTableColumn
espInputPhaseStatusVoltage = _EspInputPhaseStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 6),
    _EspInputPhaseStatusVoltage_Type()
)
espInputPhaseStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusVoltage.setStatus("current")
_EspInputPhaseStatusActivePower_Type = Integer32
_EspInputPhaseStatusActivePower_Object = MibTableColumn
espInputPhaseStatusActivePower = _EspInputPhaseStatusActivePower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 7),
    _EspInputPhaseStatusActivePower_Type()
)
espInputPhaseStatusActivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusActivePower.setStatus("current")
_EspInputPhaseStatusApparentPower_Type = Integer32
_EspInputPhaseStatusApparentPower_Object = MibTableColumn
espInputPhaseStatusApparentPower = _EspInputPhaseStatusApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 8),
    _EspInputPhaseStatusApparentPower_Type()
)
espInputPhaseStatusApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusApparentPower.setStatus("current")
_EspInputPhaseStatusPowerFactor_Type = Integer32
_EspInputPhaseStatusPowerFactor_Object = MibTableColumn
espInputPhaseStatusPowerFactor = _EspInputPhaseStatusPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 3, 4, 1, 9),
    _EspInputPhaseStatusPowerFactor_Type()
)
espInputPhaseStatusPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espInputPhaseStatusPowerFactor.setStatus("current")
_EspCircuitBreaker_ObjectIdentity = ObjectIdentity
espCircuitBreaker = _EspCircuitBreaker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4)
)
_EspCircuitBreakerConfigTable_Object = MibTable
espCircuitBreakerConfigTable = _EspCircuitBreakerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 2)
)
if mibBuilder.loadTexts:
    espCircuitBreakerConfigTable.setStatus("current")
_EspCircuitBreakerConfigEntry_Object = MibTableRow
espCircuitBreakerConfigEntry = _EspCircuitBreakerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 2, 1)
)
espCircuitBreakerConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "espCircuitBreakerConfigIndex"),
)
if mibBuilder.loadTexts:
    espCircuitBreakerConfigEntry.setStatus("current")


class _EspCircuitBreakerConfigIndex_Type(Integer32):
    """Custom type espCircuitBreakerConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspCircuitBreakerConfigIndex_Type.__name__ = "Integer32"
_EspCircuitBreakerConfigIndex_Object = MibTableColumn
espCircuitBreakerConfigIndex = _EspCircuitBreakerConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 2, 1, 1),
    _EspCircuitBreakerConfigIndex_Type()
)
espCircuitBreakerConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espCircuitBreakerConfigIndex.setStatus("current")


class _EspCircuitBreakerConfigCount_Type(Integer32):
    """Custom type espCircuitBreakerConfigCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspCircuitBreakerConfigCount_Type.__name__ = "Integer32"
_EspCircuitBreakerConfigCount_Object = MibTableColumn
espCircuitBreakerConfigCount = _EspCircuitBreakerConfigCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 2, 1, 2),
    _EspCircuitBreakerConfigCount_Type()
)
espCircuitBreakerConfigCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerConfigCount.setStatus("current")
_EspCircuitBreakerName_Type = DisplayString
_EspCircuitBreakerName_Object = MibTableColumn
espCircuitBreakerName = _EspCircuitBreakerName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 2, 1, 3),
    _EspCircuitBreakerName_Type()
)
espCircuitBreakerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerName.setStatus("current")
_EspCircuitBreakerPropertiesTable_Object = MibTable
espCircuitBreakerPropertiesTable = _EspCircuitBreakerPropertiesTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 3)
)
if mibBuilder.loadTexts:
    espCircuitBreakerPropertiesTable.setStatus("current")
_EspCircuitBreakerPropertiesEntry_Object = MibTableRow
espCircuitBreakerPropertiesEntry = _EspCircuitBreakerPropertiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 3, 1)
)
espCircuitBreakerPropertiesEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitPropertiesIndex"),
    (0, "ENLOGIC-PDU-MIB", "espCircuitBreakerPropertiesIndex"),
)
if mibBuilder.loadTexts:
    espCircuitBreakerPropertiesEntry.setStatus("current")


class _EspCircuitBreakerPropertiesIndex_Type(Integer32):
    """Custom type espCircuitBreakerPropertiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspCircuitBreakerPropertiesIndex_Type.__name__ = "Integer32"
_EspCircuitBreakerPropertiesIndex_Object = MibTableColumn
espCircuitBreakerPropertiesIndex = _EspCircuitBreakerPropertiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 3, 1, 1),
    _EspCircuitBreakerPropertiesIndex_Type()
)
espCircuitBreakerPropertiesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espCircuitBreakerPropertiesIndex.setStatus("current")


class _EspCircuitBreakerPropertiesCount_Type(Integer32):
    """Custom type espCircuitBreakerPropertiesCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspCircuitBreakerPropertiesCount_Type.__name__ = "Integer32"
_EspCircuitBreakerPropertiesCount_Object = MibTableColumn
espCircuitBreakerPropertiesCount = _EspCircuitBreakerPropertiesCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 3, 1, 2),
    _EspCircuitBreakerPropertiesCount_Type()
)
espCircuitBreakerPropertiesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerPropertiesCount.setStatus("current")


class _EspCircuitBreakerPropertiesInputLayout_Type(Integer32):
    """Custom type espCircuitBreakerPropertiesInputLayout based on Integer32"""
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
        *(("seqPhase1ToNeutral", 1),
          ("seqPhase1ToPhase2", 4),
          ("seqPhase2ToNeutral", 2),
          ("seqPhase2ToPhase3", 5),
          ("seqPhase3ToNeutral", 3),
          ("seqPhase3ToPhase1", 6))
    )


_EspCircuitBreakerPropertiesInputLayout_Type.__name__ = "Integer32"
_EspCircuitBreakerPropertiesInputLayout_Object = MibTableColumn
espCircuitBreakerPropertiesInputLayout = _EspCircuitBreakerPropertiesInputLayout_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 3, 1, 3),
    _EspCircuitBreakerPropertiesInputLayout_Type()
)
espCircuitBreakerPropertiesInputLayout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerPropertiesInputLayout.setStatus("current")
_EspCircuitBreakerStatusTable_Object = MibTable
espCircuitBreakerStatusTable = _EspCircuitBreakerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 4)
)
if mibBuilder.loadTexts:
    espCircuitBreakerStatusTable.setStatus("current")
_EspCircuitBreakerStatusEntry_Object = MibTableRow
espCircuitBreakerStatusEntry = _EspCircuitBreakerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 4, 1)
)
espCircuitBreakerStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "espCircuitBreakerStatusIndex"),
)
if mibBuilder.loadTexts:
    espCircuitBreakerStatusEntry.setStatus("current")


class _EspCircuitBreakerStatusIndex_Type(Integer32):
    """Custom type espCircuitBreakerStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspCircuitBreakerStatusIndex_Type.__name__ = "Integer32"
_EspCircuitBreakerStatusIndex_Object = MibTableColumn
espCircuitBreakerStatusIndex = _EspCircuitBreakerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 4, 1, 1),
    _EspCircuitBreakerStatusIndex_Type()
)
espCircuitBreakerStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espCircuitBreakerStatusIndex.setStatus("current")


class _EspCircuitBreakerStatusCount_Type(Integer32):
    """Custom type espCircuitBreakerStatusCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspCircuitBreakerStatusCount_Type.__name__ = "Integer32"
_EspCircuitBreakerStatusCount_Object = MibTableColumn
espCircuitBreakerStatusCount = _EspCircuitBreakerStatusCount_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 4, 1, 2),
    _EspCircuitBreakerStatusCount_Type()
)
espCircuitBreakerStatusCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerStatusCount.setStatus("current")
_EspCircuitBreakerLabel_Type = DisplayString
_EspCircuitBreakerLabel_Object = MibTableColumn
espCircuitBreakerLabel = _EspCircuitBreakerLabel_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 4, 1, 3),
    _EspCircuitBreakerLabel_Type()
)
espCircuitBreakerLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerLabel.setStatus("current")


class _EspCircuitBreakerStatusLoadState_Type(Integer32):
    """Custom type espCircuitBreakerStatusLoadState based on Integer32"""
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
        *(("lowerCritical", 4),
          ("lowerWarning", 3),
          ("normal", 5),
          ("off", 6),
          ("upperCritical", 1),
          ("upperWarning", 2))
    )


_EspCircuitBreakerStatusLoadState_Type.__name__ = "Integer32"
_EspCircuitBreakerStatusLoadState_Object = MibTableColumn
espCircuitBreakerStatusLoadState = _EspCircuitBreakerStatusLoadState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 4, 1, 4),
    _EspCircuitBreakerStatusLoadState_Type()
)
espCircuitBreakerStatusLoadState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerStatusLoadState.setStatus("current")
_EspCircuitBreakerStatusCurrent_Type = Integer32
_EspCircuitBreakerStatusCurrent_Object = MibTableColumn
espCircuitBreakerStatusCurrent = _EspCircuitBreakerStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 4, 4, 1, 5),
    _EspCircuitBreakerStatusCurrent_Type()
)
espCircuitBreakerStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espCircuitBreakerStatusCurrent.setStatus("current")
_EspExternalSensor_ObjectIdentity = ObjectIdentity
espExternalSensor = _EspExternalSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6)
)
_EspExternalSensorNamePlateTable_Object = MibTable
espExternalSensorNamePlateTable = _EspExternalSensorNamePlateTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 2)
)
if mibBuilder.loadTexts:
    espExternalSensorNamePlateTable.setStatus("current")
_EspExternalSensorNamePlateEntry_Object = MibTableRow
espExternalSensorNamePlateEntry = _EspExternalSensorNamePlateEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 2, 1)
)
espExternalSensorNamePlateEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espNamePlateIndex"),
    (0, "ENLOGIC-PDU-MIB", "espExternalSensorNamePlateIndex"),
)
if mibBuilder.loadTexts:
    espExternalSensorNamePlateEntry.setStatus("current")


class _EspExternalSensorNamePlateIndex_Type(Integer32):
    """Custom type espExternalSensorNamePlateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspExternalSensorNamePlateIndex_Type.__name__ = "Integer32"
_EspExternalSensorNamePlateIndex_Object = MibTableColumn
espExternalSensorNamePlateIndex = _EspExternalSensorNamePlateIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 2, 1, 1),
    _EspExternalSensorNamePlateIndex_Type()
)
espExternalSensorNamePlateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espExternalSensorNamePlateIndex.setStatus("current")
_EspExternalSensorNamePlateName_Type = DisplayString
_EspExternalSensorNamePlateName_Object = MibTableColumn
espExternalSensorNamePlateName = _EspExternalSensorNamePlateName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 2, 1, 2),
    _EspExternalSensorNamePlateName_Type()
)
espExternalSensorNamePlateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorNamePlateName.setStatus("current")
_EspExternalSensorNamePlateSerialNumber_Type = DisplayString
_EspExternalSensorNamePlateSerialNumber_Object = MibTableColumn
espExternalSensorNamePlateSerialNumber = _EspExternalSensorNamePlateSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 2, 1, 5),
    _EspExternalSensorNamePlateSerialNumber_Type()
)
espExternalSensorNamePlateSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorNamePlateSerialNumber.setStatus("current")


class _EspExternalSensorNamePlateType_Type(Integer32):
    """Custom type espExternalSensorNamePlateType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("beacon", 8),
          ("doorSwitch", 3),
          ("dryContact", 4),
          ("humidity", 2),
          ("ropeFluid", 6),
          ("smoke", 7),
          ("spotFluid", 5),
          ("temperature", 1))
    )


_EspExternalSensorNamePlateType_Type.__name__ = "Integer32"
_EspExternalSensorNamePlateType_Object = MibTableColumn
espExternalSensorNamePlateType = _EspExternalSensorNamePlateType_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 2, 1, 6),
    _EspExternalSensorNamePlateType_Type()
)
espExternalSensorNamePlateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorNamePlateType.setStatus("current")


class _EspExternalSensorNamePlateUnits_Type(Integer32):
    """Custom type espExternalSensorNamePlateUnits based on Integer32"""
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
        *(("degreeC", 1),
          ("degreeF", 2),
          ("logic", 0),
          ("percent", 3))
    )


_EspExternalSensorNamePlateUnits_Type.__name__ = "Integer32"
_EspExternalSensorNamePlateUnits_Object = MibTableColumn
espExternalSensorNamePlateUnits = _EspExternalSensorNamePlateUnits_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 2, 1, 7),
    _EspExternalSensorNamePlateUnits_Type()
)
espExternalSensorNamePlateUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorNamePlateUnits.setStatus("current")
_EspExternalSensorConfigTable_Object = MibTable
espExternalSensorConfigTable = _EspExternalSensorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 3)
)
if mibBuilder.loadTexts:
    espExternalSensorConfigTable.setStatus("current")
_EspExternalSensorConfigEntry_Object = MibTableRow
espExternalSensorConfigEntry = _EspExternalSensorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 3, 1)
)
espExternalSensorConfigEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitConfigIndex"),
    (0, "ENLOGIC-PDU-MIB", "espExternalSensorConfigIndex"),
)
if mibBuilder.loadTexts:
    espExternalSensorConfigEntry.setStatus("current")


class _EspExternalSensorConfigIndex_Type(Integer32):
    """Custom type espExternalSensorConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspExternalSensorConfigIndex_Type.__name__ = "Integer32"
_EspExternalSensorConfigIndex_Object = MibTableColumn
espExternalSensorConfigIndex = _EspExternalSensorConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 3, 1, 1),
    _EspExternalSensorConfigIndex_Type()
)
espExternalSensorConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espExternalSensorConfigIndex.setStatus("current")


class _EspExternalSensorConfigAlarmState_Type(Integer32):
    """Custom type espExternalSensorConfigAlarmState based on Integer32"""
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


_EspExternalSensorConfigAlarmState_Type.__name__ = "Integer32"
_EspExternalSensorConfigAlarmState_Object = MibTableColumn
espExternalSensorConfigAlarmState = _EspExternalSensorConfigAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 3, 1, 9),
    _EspExternalSensorConfigAlarmState_Type()
)
espExternalSensorConfigAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espExternalSensorConfigAlarmState.setStatus("current")
_EspExternalSensorStatusTable_Object = MibTable
espExternalSensorStatusTable = _EspExternalSensorStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4)
)
if mibBuilder.loadTexts:
    espExternalSensorStatusTable.setStatus("current")
_EspExternalSensorStatusEntry_Object = MibTableRow
espExternalSensorStatusEntry = _EspExternalSensorStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1)
)
espExternalSensorStatusEntry.setIndexNames(
    (0, "ENLOGIC-PDU-MIB", "espUnitStatusIndex"),
    (0, "ENLOGIC-PDU-MIB", "espExternalSensorStatusIndex"),
)
if mibBuilder.loadTexts:
    espExternalSensorStatusEntry.setStatus("current")


class _EspExternalSensorStatusIndex_Type(Integer32):
    """Custom type espExternalSensorStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EspExternalSensorStatusIndex_Type.__name__ = "Integer32"
_EspExternalSensorStatusIndex_Object = MibTableColumn
espExternalSensorStatusIndex = _EspExternalSensorStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1, 1),
    _EspExternalSensorStatusIndex_Type()
)
espExternalSensorStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espExternalSensorStatusIndex.setStatus("current")
_EspExternalSensorStatusName_Type = DisplayString
_EspExternalSensorStatusName_Object = MibTableColumn
espExternalSensorStatusName = _EspExternalSensorStatusName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1, 2),
    _EspExternalSensorStatusName_Type()
)
espExternalSensorStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorStatusName.setStatus("current")


class _EspExternalSensorStatusAisle_Type(Integer32):
    """Custom type espExternalSensorStatusAisle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldAisle", 2),
          ("hotAisle", 1))
    )


_EspExternalSensorStatusAisle_Type.__name__ = "Integer32"
_EspExternalSensorStatusAisle_Object = MibTableColumn
espExternalSensorStatusAisle = _EspExternalSensorStatusAisle_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1, 3),
    _EspExternalSensorStatusAisle_Type()
)
espExternalSensorStatusAisle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espExternalSensorStatusAisle.setStatus("current")


class _EspExternalSensorStatusCommStatus_Type(Integer32):
    """Custom type espExternalSensorStatusCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commsLost", 3),
          ("commsOk", 2),
          ("notInstalled", 1))
    )


_EspExternalSensorStatusCommStatus_Type.__name__ = "Integer32"
_EspExternalSensorStatusCommStatus_Object = MibTableColumn
espExternalSensorStatusCommStatus = _EspExternalSensorStatusCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1, 4),
    _EspExternalSensorStatusCommStatus_Type()
)
espExternalSensorStatusCommStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorStatusCommStatus.setStatus("current")


class _EspExternalSensorStatusState_Type(Integer32):
    """Custom type espExternalSensorStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("aboveUpperCritical", 6),
          ("aboveUpperWarning", 5),
          ("alarmed", 1),
          ("belowLowerCritical", 3),
          ("belowLowerWarning", 4),
          ("normal", 2),
          ("notPresent", 0))
    )


_EspExternalSensorStatusState_Type.__name__ = "Integer32"
_EspExternalSensorStatusState_Object = MibTableColumn
espExternalSensorStatusState = _EspExternalSensorStatusState_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1, 5),
    _EspExternalSensorStatusState_Type()
)
espExternalSensorStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorStatusState.setStatus("current")
_EspExternalSensorStatusValue_Type = Integer32
_EspExternalSensorStatusValue_Object = MibTableColumn
espExternalSensorStatusValue = _EspExternalSensorStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1, 6),
    _EspExternalSensorStatusValue_Type()
)
espExternalSensorStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorStatusValue.setStatus("current")
_EspExternalSensorStatusHighPrecisionValue_Type = Integer32
_EspExternalSensorStatusHighPrecisionValue_Object = MibTableColumn
espExternalSensorStatusHighPrecisionValue = _EspExternalSensorStatusHighPrecisionValue_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 6, 4, 1, 8),
    _EspExternalSensorStatusHighPrecisionValue_Type()
)
espExternalSensorStatusHighPrecisionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espExternalSensorStatusHighPrecisionValue.setStatus("current")
_EspTraps_ObjectIdentity = ObjectIdentity
espTraps = _EspTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9)
)


class _EspTrapsInfoIndex_Type(Integer32):
    """Custom type espTrapsInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_EspTrapsInfoIndex_Type.__name__ = "Integer32"
_EspTrapsInfoIndex_Object = MibScalar
espTrapsInfoIndex = _EspTrapsInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 1),
    _EspTrapsInfoIndex_Type()
)
espTrapsInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    espTrapsInfoIndex.setStatus("current")
_EspUserName_Type = DisplayString
_EspUserName_Object = MibScalar
espUserName = _EspUserName_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 2),
    _EspUserName_Type()
)
espUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espUserName.setStatus("current")
_EspFirmwareVersion_Type = DisplayString
_EspFirmwareVersion_Object = MibScalar
espFirmwareVersion = _EspFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 4),
    _EspFirmwareVersion_Type()
)
espFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espFirmwareVersion.setStatus("current")
_EspIndex_Type = Integer32
_EspIndex_Object = MibScalar
espIndex = _EspIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 5),
    _EspIndex_Type()
)
espIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    espIndex.setStatus("current")
_EspExternalSensorIndex_Type = Integer32
_EspExternalSensorIndex_Object = MibScalar
espExternalSensorIndex = _EspExternalSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 6),
    _EspExternalSensorIndex_Type()
)
espExternalSensorIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    espExternalSensorIndex.setStatus("current")
_EspErrorDescription_Type = DisplayString
_EspErrorDescription_Object = MibScalar
espErrorDescription = _EspErrorDescription_Object(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 7),
    _EspErrorDescription_Type()
)
espErrorDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    espErrorDescription.setStatus("current")

# Managed Objects groups


# Notification objects

networkCardStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 2)
)
networkCardStart.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    networkCardStart.setStatus(
        "current"
    )

networkCardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 3)
)
networkCardReset.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    networkCardReset.setStatus(
        "current"
    )

userLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 4)
)
userLogin.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userLogin.setStatus(
        "current"
    )

userLogoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 5)
)
userLogoff.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userLogoff.setStatus(
        "current"
    )

userAuthenticationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 6)
)
userAuthenticationFailed.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userAuthenticationFailed.setStatus(
        "current"
    )

userSessionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 7)
)
userSessionTimeout.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userSessionTimeout.setStatus(
        "current"
    )

userAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 8)
)
userAdded.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "userUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userAdded.setStatus(
        "current"
    )

userModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 9)
)
userModified.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "userUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userModified.setStatus(
        "current"
    )

userDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 10)
)
userDeleted.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "userUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userDeleted.setStatus(
        "current"
    )

roleAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 11)
)
roleAdded.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "roleUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    roleAdded.setStatus(
        "current"
    )

roleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 12)
)
roleModified.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "roleUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    roleModified.setStatus(
        "current"
    )

roleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 13)
)
roleDeleted.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "roleUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    roleDeleted.setStatus(
        "current"
    )

firmwareUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 14)
)
firmwareUpdateStarted.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "firmwareVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    firmwareUpdateStarted.setStatus(
        "current"
    )

firmwareUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 15)
)
firmwareUpdateCompleted.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "firmwareVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    firmwareUpdateCompleted.setStatus(
        "current"
    )

userBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 16)
)
userBlocked.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userBlocked.setStatus(
        "current"
    )

outletControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 17)
)
outletControl.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduOutletSwitchedControlNumber"),
        ("ENLOGIC-PDU-MIB", "pduOutletSwitchedStatusState"),
        ("ENLOGIC-PDU-MIB", "pduOutletSwitchedControlCommand"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    outletControl.setStatus(
        "current"
    )

userPasswordChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 18)
)
userPasswordChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "userUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    userPasswordChange.setStatus(
        "current"
    )

passwordSettingsChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 19)
)
passwordSettingsChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    passwordSettingsChange.setStatus(
        "current"
    )

logFileCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 21)
)
logFileCleared.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    logFileCleared.setStatus(
        "current"
    )

pduConfigurationFileImported = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 22)
)
pduConfigurationFileImported.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduConfigurationFileImported.setStatus(
        "current"
    )

pduConfigurationFileExported = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 23)
)
pduConfigurationFileExported.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduConfigurationFileExported.setStatus(
        "current"
    )

pduUnitActivePowerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 24)
)
pduUnitActivePowerStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduUnitStatusLoadState"),
        ("ENLOGIC-PDU-MIB", "pduUnitStatusActivePower"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduUnitActivePowerStateChange.setStatus(
        "current"
    )

pduInputphaseVoltageStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 25)
)
pduInputphaseVoltageStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduInputPhaseStatusCount"),
        ("ENLOGIC-PDU-MIB", "pduInputPhaseStatusVoltageState"),
        ("ENLOGIC-PDU-MIB", "pduInputPhaseStatusVoltage"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduInputphaseVoltageStateChange.setStatus(
        "current"
    )

pduInputphaseCurrentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 26)
)
pduInputphaseCurrentStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduInputPhaseStatusCount"),
        ("ENLOGIC-PDU-MIB", "pduInputPhaseStatusCurrentState"),
        ("ENLOGIC-PDU-MIB", "pduInputPhaseStatusCurrent"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduInputphaseCurrentStateChange.setStatus(
        "current"
    )

pduCircuitBreakerCurrentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 27)
)
pduCircuitBreakerCurrentStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduCircuitBreakerStatusIndex"),
        ("ENLOGIC-PDU-MIB", "pduCircuitBreakerStatusLoadState"),
        ("ENLOGIC-PDU-MIB", "pduCircuitBreakerStatusCurrent"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduCircuitBreakerCurrentStateChange.setStatus(
        "current"
    )

pduOutletActivePowerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 28)
)
pduOutletActivePowerStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduOutletMeteredStatusIndex"),
        ("ENLOGIC-PDU-MIB", "pduOutletMeteredStatusLoadState"),
        ("ENLOGIC-PDU-MIB", "pduOutletMeteredStatusActivePower"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduOutletActivePowerStateChange.setStatus(
        "current"
    )

pduExternalSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 29)
)
pduExternalSensorStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusIndex"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusName"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorNamePlateType"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusAisle"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorNamePlateUnits"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusState"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    pduExternalSensorStateChange.setStatus(
        "current"
    )

smtpTransmissionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 30)
)
smtpTransmissionFailure.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "smtpRecipients"),
        ("ENLOGIC-PDU-MIB", "smtpServer"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    smtpTransmissionFailure.setStatus(
        "current"
    )

ldapError = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 31)
)
ldapError.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "errorDescription"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    ldapError.setStatus(
        "current"
    )

firmwareUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 32)
)
firmwareUpdateFailed.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "firmwareVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    firmwareUpdateFailed.setStatus(
        "current"
    )

serverPingState = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 33)
)
serverPingState.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduServerPingServerIPAddress"),
        ("ENLOGIC-PDU-MIB", "serverPing"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    serverPingState.setStatus(
        "current"
    )

bootloaderState = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 34)
)
bootloaderState.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    bootloaderState.setStatus(
        "current"
    )

daisyChainState = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 35)
)
daisyChainState.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "daisyChain"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    daisyChainState.setStatus(
        "current"
    )

systemInternalCommunicationLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 36)
)
systemInternalCommunicationLost.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "systemCommunication"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    systemInternalCommunicationLost.setStatus(
        "current"
    )

SmartCabinetLockUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 37)
)
SmartCabinetLockUnlocked.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduUnitSmartCabinetDoor"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    SmartCabinetLockUnlocked.setStatus(
        "current"
    )

SmartCabinetLockLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 38)
)
SmartCabinetLockLocked.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduUnitSmartCabinetDoor"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    SmartCabinetLockLocked.setStatus(
        "current"
    )

SmartCabinetSwapCard = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 39)
)
SmartCabinetSwapCard.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduUnitSmartCabinetDoor"),
        ("ENLOGIC-PDU-MIB", "pduUnitSmartCabinetCardID"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    SmartCabinetSwapCard.setStatus(
        "current"
    )

SmartCabinetLockerLockDoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 40)
)
SmartCabinetLockerLockDoorOpen.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduUnitSmartCabinetDoor"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    SmartCabinetLockerLockDoorOpen.setStatus(
        "current"
    )

SmartCabinetLockerUnlockDoorClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 41)
)
SmartCabinetLockerUnlockDoorClose.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "pduUnitSmartCabinetDoor"),
        ("ENLOGIC-PDU-MIB", "pduExternalSensorStatusValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    SmartCabinetLockerUnlockDoorClose.setStatus(
        "current"
    )

systemReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 1, 9, 50)
)
systemReboot.setObjects(
      *(("ENLOGIC-PDU-MIB", "pduIndex"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateName"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "pduNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    systemReboot.setStatus(
        "current"
    )

espNetworkCardStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 8)
)
espNetworkCardStart.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espNetworkCardStart.setStatus(
        "current"
    )

espNetworkCardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 9)
)
espNetworkCardReset.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espNetworkCardReset.setStatus(
        "current"
    )

espFirmwareUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 10)
)
espFirmwareUpdateCompleted.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "firmwareVersion"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espFirmwareUpdateCompleted.setStatus(
        "current"
    )

espUserPasswordChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 11)
)
espUserPasswordChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "userUpdated"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espUserPasswordChange.setStatus(
        "current"
    )

espLogFileCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 12)
)
espLogFileCleared.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espLogFileCleared.setStatus(
        "current"
    )

espConfigurationFileExported = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 13)
)
espConfigurationFileExported.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espConfigurationFileExported.setStatus(
        "current"
    )

espUnitActivePowerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 14)
)
espUnitActivePowerStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "espUnitStatusLoadState"),
        ("ENLOGIC-PDU-MIB", "espUnitStatusActivePower"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espUnitActivePowerStateChange.setStatus(
        "current"
    )

espInputphaseVoltageStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 15)
)
espInputphaseVoltageStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "espInputPhaseStatusCount"),
        ("ENLOGIC-PDU-MIB", "espInputPhaseStatusVoltageState"),
        ("ENLOGIC-PDU-MIB", "espInputPhaseStatusVoltage"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espInputphaseVoltageStateChange.setStatus(
        "current"
    )

espInputphaseCurrentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 16)
)
espInputphaseCurrentStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "espInputPhaseStatusCount"),
        ("ENLOGIC-PDU-MIB", "espInputPhaseStatusCurrentState"),
        ("ENLOGIC-PDU-MIB", "espInputPhaseStatusCurrent"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espInputphaseCurrentStateChange.setStatus(
        "current"
    )

espCircuitBreakerCurrentStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 17)
)
espCircuitBreakerCurrentStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "espCircuitBreakerStatusIndex"),
        ("ENLOGIC-PDU-MIB", "espCircuitBreakerStatusLoadState"),
        ("ENLOGIC-PDU-MIB", "espCircuitBreakerStatusCurrent"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espCircuitBreakerCurrentStateChange.setStatus(
        "current"
    )

espExternalSensorStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 18)
)
espExternalSensorStateChange.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("ENLOGIC-PDU-MIB", "espExternalSensorStatusIndex"),
        ("ENLOGIC-PDU-MIB", "espExternalSensorStatusName"),
        ("ENLOGIC-PDU-MIB", "espExternalSensorNamePlateType"),
        ("ENLOGIC-PDU-MIB", "espExternalSensorStatusAisle"),
        ("ENLOGIC-PDU-MIB", "espExternalSensorNamePlateUnits"),
        ("ENLOGIC-PDU-MIB", "espExternalSensorStatusState"),
        ("ENLOGIC-PDU-MIB", "espExternalSensorStatusValue"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espExternalSensorStateChange.setStatus(
        "current"
    )

espConfigurationFileImported = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 19)
)
espConfigurationFileImported.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espConfigurationFileImported.setStatus(
        "current"
    )

espNetworkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 38446, 2, 9, 20)
)
espNetworkUp.setObjects(
      *(("ENLOGIC-PDU-MIB", "espIndex"),
        ("ENLOGIC-PDU-MIB", "espNamePlateName"),
        ("ENLOGIC-PDU-MIB", "userName"),
        ("ENLOGIC-PDU-MIB", "espNamePlateInetAddressType"),
        ("ENLOGIC-PDU-MIB", "espNamePlateIPAddress"),
        ("SNMPv2-MIB", "sysContact"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    espNetworkUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENLOGIC-PDU-MIB",
    **{"enlogic": enlogic,
       "pdu": pdu,
       "pduNamePlate": pduNamePlate,
       "pduNamePlateTableSize": pduNamePlateTableSize,
       "pduNamePlateTable": pduNamePlateTable,
       "pduNamePlateEntry": pduNamePlateEntry,
       "pduNamePlateIndex": pduNamePlateIndex,
       "pduNamePlateName": pduNamePlateName,
       "pduNamePlateLocation": pduNamePlateLocation,
       "pduNamePlateInetAddressType": pduNamePlateInetAddressType,
       "pduNamePlateIPAddress": pduNamePlateIPAddress,
       "pduNamePlateInetNetMask": pduNamePlateInetNetMask,
       "pduNamePlateInetGateway": pduNamePlateInetGateway,
       "pduNamePlateMACAddress": pduNamePlateMACAddress,
       "pduNamePlateUTCTimeOffset": pduNamePlateUTCTimeOffset,
       "pduNamePlateModelNumber": pduNamePlateModelNumber,
       "pduNamePlateSerialNumber": pduNamePlateSerialNumber,
       "pduNamePlateDateofManufacture": pduNamePlateDateofManufacture,
       "pduNamePlateFirmwareVersion": pduNamePlateFirmwareVersion,
       "pduNamePlateFirmwareVersionTimeStamp": pduNamePlateFirmwareVersionTimeStamp,
       "pduNamePlateType": pduNamePlateType,
       "pduUnit": pduUnit,
       "pduUnitTableSize": pduUnitTableSize,
       "pduUnitConfigTable": pduUnitConfigTable,
       "pduUnitConfigEntry": pduUnitConfigEntry,
       "pduUnitConfigIndex": pduUnitConfigIndex,
       "pduUnitConfigName": pduUnitConfigName,
       "pduUnitConfigLocation": pduUnitConfigLocation,
       "pduUnitConfigDisplayOrientation": pduUnitConfigDisplayOrientation,
       "pduUnitConfigColdstartDelay": pduUnitConfigColdstartDelay,
       "pduUnitConfigGlobalOutletStateOnStartup": pduUnitConfigGlobalOutletStateOnStartup,
       "pduUnitConfigLowerCriticalThreshold": pduUnitConfigLowerCriticalThreshold,
       "pduUnitConfigLowerWarningThreshold": pduUnitConfigLowerWarningThreshold,
       "pduUnitConfigUpperCriticalThreshold": pduUnitConfigUpperCriticalThreshold,
       "pduUnitConfigUpperWarningThreshold": pduUnitConfigUpperWarningThreshold,
       "pduUnitConfigAlarmResetThreshold": pduUnitConfigAlarmResetThreshold,
       "pduUnitConfigAlarmStateChangeDelay": pduUnitConfigAlarmStateChangeDelay,
       "pduUnitConfigEnabledThresholds": pduUnitConfigEnabledThresholds,
       "pduUnitConfigPeakPowerReset": pduUnitConfigPeakPowerReset,
       "pduUnitConfigEnergyReset": pduUnitConfigEnergyReset,
       "pduUnitConfigOutletPeakPowerReset": pduUnitConfigOutletPeakPowerReset,
       "pduUnitConfigOutletEnergyReset": pduUnitConfigOutletEnergyReset,
       "pduUnitConfigUsb": pduUnitConfigUsb,
       "pduUnitConfigSsh": pduUnitConfigSsh,
       "pduUnitConfigResetNetworkManagementCard": pduUnitConfigResetNetworkManagementCard,
       "pduUnitConfigDaisyChainState": pduUnitConfigDaisyChainState,
       "pduUnitPropertiesTable": pduUnitPropertiesTable,
       "pduUnitPropertiesEntry": pduUnitPropertiesEntry,
       "pduUnitPropertiesIndex": pduUnitPropertiesIndex,
       "pduUnitPropertiesName": pduUnitPropertiesName,
       "pduUnitPropertiesOutletCount": pduUnitPropertiesOutletCount,
       "pduUnitPropertiesSwitchedOutletCount": pduUnitPropertiesSwitchedOutletCount,
       "pduUnitPropertiesMeteredOutletCount": pduUnitPropertiesMeteredOutletCount,
       "pduUnitPropertiesInputPhaseCount": pduUnitPropertiesInputPhaseCount,
       "pduUnitPropertiesCircuitBreakerCount": pduUnitPropertiesCircuitBreakerCount,
       "pduUnitPropertiesMaxExternalSensorCount": pduUnitPropertiesMaxExternalSensorCount,
       "pduUnitPropertiesConnExternalSensorCount": pduUnitPropertiesConnExternalSensorCount,
       "pduUnitPropertiesRatedVoltage": pduUnitPropertiesRatedVoltage,
       "pduUnitPropertiesRatedMaxCurrent": pduUnitPropertiesRatedMaxCurrent,
       "pduUnitPropertiesRatedFrequency": pduUnitPropertiesRatedFrequency,
       "pduUnitPropertiesRatedPower": pduUnitPropertiesRatedPower,
       "pduUnitPropertiesOrientation": pduUnitPropertiesOrientation,
       "pduUnitPropertiesOutletLayout": pduUnitPropertiesOutletLayout,
       "pduUnitPropertiesDaisyChainMemberType": pduUnitPropertiesDaisyChainMemberType,
       "pduUnitPropertiesServerCount": pduUnitPropertiesServerCount,
       "pduUnitStatusTable": pduUnitStatusTable,
       "pduUnitStatusEntry": pduUnitStatusEntry,
       "pduUnitStatusIndex": pduUnitStatusIndex,
       "pduUnitStatusName": pduUnitStatusName,
       "pduUnitStatusLoadState": pduUnitStatusLoadState,
       "pduUnitStatusActivePower": pduUnitStatusActivePower,
       "pduUnitStatusApparentPower": pduUnitStatusApparentPower,
       "pduUnitStatusPeakPower": pduUnitStatusPeakPower,
       "pduUnitStatusPeakPowerTimestamp": pduUnitStatusPeakPowerTimestamp,
       "pduUnitStatusPeakPowerStartTime": pduUnitStatusPeakPowerStartTime,
       "pduUnitStatusEnergy": pduUnitStatusEnergy,
       "pduUnitStatusResettableEnergy": pduUnitStatusResettableEnergy,
       "pduUnitStatusEnergyStartTime": pduUnitStatusEnergyStartTime,
       "pduUnitStatusOutletsEnergyStartTime": pduUnitStatusOutletsEnergyStartTime,
       "pduInputPhase": pduInputPhase,
       "pduInputPhaseTableSize": pduInputPhaseTableSize,
       "pduInputPhaseConfigTable": pduInputPhaseConfigTable,
       "pduInputPhaseConfigEntry": pduInputPhaseConfigEntry,
       "pduInputPhaseConfigIndex": pduInputPhaseConfigIndex,
       "pduInputPhaseConfigCount": pduInputPhaseConfigCount,
       "pduInputPhaseConfigOverloadRestriction": pduInputPhaseConfigOverloadRestriction,
       "pduInputPhaseConfigCurrentLowerCriticalThreshold": pduInputPhaseConfigCurrentLowerCriticalThreshold,
       "pduInputPhaseConfigCurrentLowerWarningThreshold": pduInputPhaseConfigCurrentLowerWarningThreshold,
       "pduInputPhaseConfigCurrentUpperCriticalThreshold": pduInputPhaseConfigCurrentUpperCriticalThreshold,
       "pduInputPhaseConfigCurrentUpperWarningThreshold": pduInputPhaseConfigCurrentUpperWarningThreshold,
       "pduInputPhaseConfigVoltageLowerCriticalThreshold": pduInputPhaseConfigVoltageLowerCriticalThreshold,
       "pduInputPhaseConfigVoltageLowerWarningThreshold": pduInputPhaseConfigVoltageLowerWarningThreshold,
       "pduInputPhaseConfigVoltageUpperCriticalThreshold": pduInputPhaseConfigVoltageUpperCriticalThreshold,
       "pduInputPhaseConfigVoltageUpperWarningThreshold": pduInputPhaseConfigVoltageUpperWarningThreshold,
       "pduInputPhaseConfigCurrentAlarmResetThreshold": pduInputPhaseConfigCurrentAlarmResetThreshold,
       "pduInputPhaseConfigCurrentAlarmStateChangeDelay": pduInputPhaseConfigCurrentAlarmStateChangeDelay,
       "pduInputPhaseConfigCurrentEnabledThresholds": pduInputPhaseConfigCurrentEnabledThresholds,
       "pduInputPhaseConfigVoltageAlarmResetThreshold": pduInputPhaseConfigVoltageAlarmResetThreshold,
       "pduInputPhaseConfigVoltageAlarmStateChangeDelay": pduInputPhaseConfigVoltageAlarmStateChangeDelay,
       "pduInputPhaseConfigVoltageEnabledThresholds": pduInputPhaseConfigVoltageEnabledThresholds,
       "pduInputPhasePropertiesTable": pduInputPhasePropertiesTable,
       "pduInputPhasePropertiesEntry": pduInputPhasePropertiesEntry,
       "pduInputPhasePropertiesIndex": pduInputPhasePropertiesIndex,
       "pduInputPhasePropertiesCount": pduInputPhasePropertiesCount,
       "pduInputPhaseStatusTable": pduInputPhaseStatusTable,
       "pduInputPhaseStatusEntry": pduInputPhaseStatusEntry,
       "pduInputPhaseStatusIndex": pduInputPhaseStatusIndex,
       "pduInputPhaseStatusCount": pduInputPhaseStatusCount,
       "pduInputPhaseStatusCurrentState": pduInputPhaseStatusCurrentState,
       "pduInputPhaseStatusVoltageState": pduInputPhaseStatusVoltageState,
       "pduInputPhaseStatusCurrent": pduInputPhaseStatusCurrent,
       "pduInputPhaseStatusVoltage": pduInputPhaseStatusVoltage,
       "pduInputPhaseStatusActivePower": pduInputPhaseStatusActivePower,
       "pduInputPhaseStatusApparentPower": pduInputPhaseStatusApparentPower,
       "pduInputPhaseStatusPowerFactor": pduInputPhaseStatusPowerFactor,
       "pduCircuitBreaker": pduCircuitBreaker,
       "pduCircuitBreakerTableSize": pduCircuitBreakerTableSize,
       "pduCircuitBreakerConfigTable": pduCircuitBreakerConfigTable,
       "pduCircuitBreakerConfigEntry": pduCircuitBreakerConfigEntry,
       "pduCircuitBreakerConfigIndex": pduCircuitBreakerConfigIndex,
       "pduCircuitBreakerConfigCount": pduCircuitBreakerConfigCount,
       "pduCircuitBreakerName": pduCircuitBreakerName,
       "pduCircuitBreakerConfigOverloadRestriction": pduCircuitBreakerConfigOverloadRestriction,
       "pduCircuitBreakerConfigLowerCriticalThreshold": pduCircuitBreakerConfigLowerCriticalThreshold,
       "pduCircuitBreakerConfigLowerWarningThreshold": pduCircuitBreakerConfigLowerWarningThreshold,
       "pduCircuitBreakerConfigUpperCriticalThreshold": pduCircuitBreakerConfigUpperCriticalThreshold,
       "pduCircuitBreakerConfigUpperWarningThreshold": pduCircuitBreakerConfigUpperWarningThreshold,
       "pduCircuitBreakerConfigAlarmResetThreshold": pduCircuitBreakerConfigAlarmResetThreshold,
       "pduCircuitBreakerConfigAlarmStateChangeDelay": pduCircuitBreakerConfigAlarmStateChangeDelay,
       "pduCircuitBreakerConfigEnabledThresholds": pduCircuitBreakerConfigEnabledThresholds,
       "pduCircuitBreakerPropertiesTable": pduCircuitBreakerPropertiesTable,
       "pduCircuitBreakerPropertiesEntry": pduCircuitBreakerPropertiesEntry,
       "pduCircuitBreakerPropertiesIndex": pduCircuitBreakerPropertiesIndex,
       "pduCircuitBreakerPropertiesCount": pduCircuitBreakerPropertiesCount,
       "pduCircuitBreakerPropertiesInputLayout": pduCircuitBreakerPropertiesInputLayout,
       "pduCircuitBreakerStatusTable": pduCircuitBreakerStatusTable,
       "pduCircuitBreakerStatusEntry": pduCircuitBreakerStatusEntry,
       "pduCircuitBreakerStatusIndex": pduCircuitBreakerStatusIndex,
       "pduCircuitBreakerStatusCount": pduCircuitBreakerStatusCount,
       "pduCircuitBreakerLabel": pduCircuitBreakerLabel,
       "pduCircuitBreakerStatusLoadState": pduCircuitBreakerStatusLoadState,
       "pduCircuitBreakerStatusCurrent": pduCircuitBreakerStatusCurrent,
       "pduOutlet": pduOutlet,
       "pduOutletSwitchedTableSize": pduOutletSwitchedTableSize,
       "pduOutletSwitchedConfigTable": pduOutletSwitchedConfigTable,
       "pduOutletSwitchedConfigEntry": pduOutletSwitchedConfigEntry,
       "pduOutletSwitchedConfigIndex": pduOutletSwitchedConfigIndex,
       "pduOutletSwitchedName": pduOutletSwitchedName,
       "pduOutletSwitchedStateOnStartup": pduOutletSwitchedStateOnStartup,
       "pduOutletSwitchedConfigPowerOnTime": pduOutletSwitchedConfigPowerOnTime,
       "pduOutletSwitchedConfigPowerOffTime": pduOutletSwitchedConfigPowerOffTime,
       "pduOutletSwitchedConfigRebootDuration": pduOutletSwitchedConfigRebootDuration,
       "pduOutletSwitchedPropertiesTable": pduOutletSwitchedPropertiesTable,
       "pduOutletSwitchedPropertiesEntry": pduOutletSwitchedPropertiesEntry,
       "pduOutletSwitchedPropertiesIndex": pduOutletSwitchedPropertiesIndex,
       "pduOutletSwitchedPropertiesNumber": pduOutletSwitchedPropertiesNumber,
       "pduOutletSwitchedPropertiesName": pduOutletSwitchedPropertiesName,
       "pduOutletSwitchedPropertiesInputPhaseLayout": pduOutletSwitchedPropertiesInputPhaseLayout,
       "pduOutletSwitchedPropertiesCircuitBreaker": pduOutletSwitchedPropertiesCircuitBreaker,
       "pduOutletSwitchedStatusTable": pduOutletSwitchedStatusTable,
       "pduOutletSwitchedStatusEntry": pduOutletSwitchedStatusEntry,
       "pduOutletSwitchedStatusIndex": pduOutletSwitchedStatusIndex,
       "pduOutletSwitchedStatusNumber": pduOutletSwitchedStatusNumber,
       "pduOutletSwitchedStatusName": pduOutletSwitchedStatusName,
       "pduOutletSwitchedStatusState": pduOutletSwitchedStatusState,
       "pduOutletSwitchedControlTable": pduOutletSwitchedControlTable,
       "pduOutletSwitchedControlEntry": pduOutletSwitchedControlEntry,
       "pduOutletSwitchedControlIndex": pduOutletSwitchedControlIndex,
       "pduOutletSwitchedControlNumber": pduOutletSwitchedControlNumber,
       "pduOutletSwitchedControlName": pduOutletSwitchedControlName,
       "pduOutletSwitchedControlCommand": pduOutletSwitchedControlCommand,
       "pduOutletMeteredTableSize": pduOutletMeteredTableSize,
       "pduOutletMeteredConfigTable": pduOutletMeteredConfigTable,
       "pduOutletMeteredConfigEntry": pduOutletMeteredConfigEntry,
       "pduOutletMeteredConfigIndex": pduOutletMeteredConfigIndex,
       "pduOutletMeteredName": pduOutletMeteredName,
       "pduOutletMeteredConfigLowerCriticalThreshold": pduOutletMeteredConfigLowerCriticalThreshold,
       "pduOutletMeteredConfigLowerWarningThreshold": pduOutletMeteredConfigLowerWarningThreshold,
       "pduOutletMeteredConfigUpperCriticalThreshold": pduOutletMeteredConfigUpperCriticalThreshold,
       "pduOutletMeteredConfigUpperWarningThreshold": pduOutletMeteredConfigUpperWarningThreshold,
       "pduOutletMeteredConfigAlarmResetThreshold": pduOutletMeteredConfigAlarmResetThreshold,
       "pduOutletMeteredConfigAlarmStateChangeDelay": pduOutletMeteredConfigAlarmStateChangeDelay,
       "pduOutletMeteredConfigEnabledThresholds": pduOutletMeteredConfigEnabledThresholds,
       "pduOutletMeteredPropertiesTable": pduOutletMeteredPropertiesTable,
       "pduOutletMeteredPropertiesEntry": pduOutletMeteredPropertiesEntry,
       "pduOutletMeteredPropertiesIndex": pduOutletMeteredPropertiesIndex,
       "pduOutletMeteredPropertiesNumber": pduOutletMeteredPropertiesNumber,
       "pduOutletMeteredPropertiesName": pduOutletMeteredPropertiesName,
       "pduOutletMeteredPropertiesInputPhaseLayout": pduOutletMeteredPropertiesInputPhaseLayout,
       "pduOutletMeteredPropertiesCircuitBreaker": pduOutletMeteredPropertiesCircuitBreaker,
       "pduOutletMeteredPropertiesPowerRating": pduOutletMeteredPropertiesPowerRating,
       "pduOutletMeteredStatusTable": pduOutletMeteredStatusTable,
       "pduOutletMeteredStatusEntry": pduOutletMeteredStatusEntry,
       "pduOutletMeteredStatusIndex": pduOutletMeteredStatusIndex,
       "pduOutletMeteredStatusNumber": pduOutletMeteredStatusNumber,
       "pduOutletMeteredStatusName": pduOutletMeteredStatusName,
       "pduOutletMeteredStatusLoadState": pduOutletMeteredStatusLoadState,
       "pduOutletMeteredStatusCurrent": pduOutletMeteredStatusCurrent,
       "pduOutletMeteredStatusActivePower": pduOutletMeteredStatusActivePower,
       "pduOutletMeteredStatusPowerFactor": pduOutletMeteredStatusPowerFactor,
       "pduOutletMeteredStatusPeakPower": pduOutletMeteredStatusPeakPower,
       "pduOutletMeteredStatusPeakPowerTimeStamp": pduOutletMeteredStatusPeakPowerTimeStamp,
       "pduOutletMeteredStatusPeakPowerStartTime": pduOutletMeteredStatusPeakPowerStartTime,
       "pduOutletMeteredStatusResettableEnergy": pduOutletMeteredStatusResettableEnergy,
       "pduExternalSensor": pduExternalSensor,
       "pduExternalSensorTableSize": pduExternalSensorTableSize,
       "pduExternalSensorNamePlateTable": pduExternalSensorNamePlateTable,
       "pduExternalSensorNamePlateEntry": pduExternalSensorNamePlateEntry,
       "pduExternalSensorNamePlateIndex": pduExternalSensorNamePlateIndex,
       "pduExternalSensorNamePlateName": pduExternalSensorNamePlateName,
       "pduExternalSensorNamePlateDescription": pduExternalSensorNamePlateDescription,
       "pduExternalSensorNamePlateLocation": pduExternalSensorNamePlateLocation,
       "pduExternalSensorNamePlateSerialNumber": pduExternalSensorNamePlateSerialNumber,
       "pduExternalSensorNamePlateType": pduExternalSensorNamePlateType,
       "pduExternalSensorNamePlateUnits": pduExternalSensorNamePlateUnits,
       "pduExternalSensorNamePlateIdentifier": pduExternalSensorNamePlateIdentifier,
       "pduExternalSensorConfigTable": pduExternalSensorConfigTable,
       "pduExternalSensorConfigEntry": pduExternalSensorConfigEntry,
       "pduExternalSensorConfigIndex": pduExternalSensorConfigIndex,
       "pduExternalSensorConfigLowerCriticalThreshold": pduExternalSensorConfigLowerCriticalThreshold,
       "pduExternalSensorConfigLowerWarningThreshold": pduExternalSensorConfigLowerWarningThreshold,
       "pduExternalSensorConfigUpperCriticalThreshold": pduExternalSensorConfigUpperCriticalThreshold,
       "pduExternalSensorConfigUpperWarningThreshold": pduExternalSensorConfigUpperWarningThreshold,
       "pduExternalSensorConfigAlarmResetThreshold": pduExternalSensorConfigAlarmResetThreshold,
       "pduExternalSensorConfigAlarmStateChangeDelay": pduExternalSensorConfigAlarmStateChangeDelay,
       "pduExternalSensorConfigEnabledThresholds": pduExternalSensorConfigEnabledThresholds,
       "pduExternalSensorConfigAlarmState": pduExternalSensorConfigAlarmState,
       "pduExternalSensorStatusTable": pduExternalSensorStatusTable,
       "pduExternalSensorStatusEntry": pduExternalSensorStatusEntry,
       "pduExternalSensorStatusIndex": pduExternalSensorStatusIndex,
       "pduExternalSensorStatusName": pduExternalSensorStatusName,
       "pduExternalSensorStatusAisle": pduExternalSensorStatusAisle,
       "pduExternalSensorStatusCommStatus": pduExternalSensorStatusCommStatus,
       "pduExternalSensorStatusState": pduExternalSensorStatusState,
       "pduExternalSensorStatusValue": pduExternalSensorStatusValue,
       "pduExternalSensorStatusTimeStamp": pduExternalSensorStatusTimeStamp,
       "pduExternalSensorStatusHighPrecisionValue": pduExternalSensorStatusHighPrecisionValue,
       "pduServerPing": pduServerPing,
       "pduServerPingTableSize": pduServerPingTableSize,
       "pduServerPingTable": pduServerPingTable,
       "pduServerPingEntry": pduServerPingEntry,
       "pduServerPingIndex": pduServerPingIndex,
       "pduServerPingServerIPAddress": pduServerPingServerIPAddress,
       "pduServerPingEnabled": pduServerPingEnabled,
       "pduSmartCabinet": pduSmartCabinet,
       "pduUnitSmartCabinetTableSize": pduUnitSmartCabinetTableSize,
       "pduUnitSmartCabinetTable": pduUnitSmartCabinetTable,
       "pduUnitSmartCabinetEntry": pduUnitSmartCabinetEntry,
       "pduUnitSmartCabinetIndex": pduUnitSmartCabinetIndex,
       "pduUnitSmartCabinetCardUserName": pduUnitSmartCabinetCardUserName,
       "pduUnitSmartCabinetCardID": pduUnitSmartCabinetCardID,
       "pduUnitSmartCabinetTimestamp": pduUnitSmartCabinetTimestamp,
       "pduUnitSmartCabinetDoor": pduUnitSmartCabinetDoor,
       "pduUnitSmartCabinetControl": pduUnitSmartCabinetControl,
       "pduUnitSmartCabinetControlUserName": pduUnitSmartCabinetControlUserName,
       "pduUnitSmartCabinetControlCardID": pduUnitSmartCabinetControlCardID,
       "pduUnitSmartCabinetControlTimestamp": pduUnitSmartCabinetControlTimestamp,
       "pduUnitSmartCabinetControlDoor": pduUnitSmartCabinetControlDoor,
       "pduUnitSmartCabinetCardIDEdit": pduUnitSmartCabinetCardIDEdit,
       "pduUnitSmartCabinetColdAisleLockState": pduUnitSmartCabinetColdAisleLockState,
       "pduUnitSmartCabinetHotAisleLockState": pduUnitSmartCabinetHotAisleLockState,
       "pduTraps": pduTraps,
       "trapsInfo": trapsInfo,
       "trapsInfoTable": trapsInfoTable,
       "trapsInfoEntry": trapsInfoEntry,
       "trapsInfoIndex": trapsInfoIndex,
       "userName": userName,
       "userUpdated": userUpdated,
       "firmwareVersion": firmwareVersion,
       "roleUpdated": roleUpdated,
       "smtpRecipients": smtpRecipients,
       "smtpServer": smtpServer,
       "pduIndex": pduIndex,
       "externalSensorIndex": externalSensorIndex,
       "serverPing": serverPing,
       "usbDevice": usbDevice,
       "errorDescription": errorDescription,
       "daisyChain": daisyChain,
       "systemCommunication": systemCommunication,
       "networkCardStart": networkCardStart,
       "networkCardReset": networkCardReset,
       "userLogin": userLogin,
       "userLogoff": userLogoff,
       "userAuthenticationFailed": userAuthenticationFailed,
       "userSessionTimeout": userSessionTimeout,
       "userAdded": userAdded,
       "userModified": userModified,
       "userDeleted": userDeleted,
       "roleAdded": roleAdded,
       "roleModified": roleModified,
       "roleDeleted": roleDeleted,
       "firmwareUpdateStarted": firmwareUpdateStarted,
       "firmwareUpdateCompleted": firmwareUpdateCompleted,
       "userBlocked": userBlocked,
       "outletControl": outletControl,
       "userPasswordChange": userPasswordChange,
       "passwordSettingsChange": passwordSettingsChange,
       "logFileCleared": logFileCleared,
       "pduConfigurationFileImported": pduConfigurationFileImported,
       "pduConfigurationFileExported": pduConfigurationFileExported,
       "pduUnitActivePowerStateChange": pduUnitActivePowerStateChange,
       "pduInputphaseVoltageStateChange": pduInputphaseVoltageStateChange,
       "pduInputphaseCurrentStateChange": pduInputphaseCurrentStateChange,
       "pduCircuitBreakerCurrentStateChange": pduCircuitBreakerCurrentStateChange,
       "pduOutletActivePowerStateChange": pduOutletActivePowerStateChange,
       "pduExternalSensorStateChange": pduExternalSensorStateChange,
       "smtpTransmissionFailure": smtpTransmissionFailure,
       "ldapError": ldapError,
       "firmwareUpdateFailed": firmwareUpdateFailed,
       "serverPingState": serverPingState,
       "bootloaderState": bootloaderState,
       "daisyChainState": daisyChainState,
       "systemInternalCommunicationLost": systemInternalCommunicationLost,
       "SmartCabinetLockUnlocked": SmartCabinetLockUnlocked,
       "SmartCabinetLockLocked": SmartCabinetLockLocked,
       "SmartCabinetSwapCard": SmartCabinetSwapCard,
       "SmartCabinetLockerLockDoorOpen": SmartCabinetLockerLockDoorOpen,
       "SmartCabinetLockerUnlockDoorClose": SmartCabinetLockerUnlockDoorClose,
       "systemReboot": systemReboot,
       "esp": esp,
       "espNamePlate": espNamePlate,
       "espNamePlateTable": espNamePlateTable,
       "espNamePlateEntry": espNamePlateEntry,
       "espNamePlateIndex": espNamePlateIndex,
       "espNamePlateName": espNamePlateName,
       "espNamePlateLocation": espNamePlateLocation,
       "espNamePlateInetAddressType": espNamePlateInetAddressType,
       "espNamePlateIPAddress": espNamePlateIPAddress,
       "espNamePlateInetNetMask": espNamePlateInetNetMask,
       "espNamePlateInetGateway": espNamePlateInetGateway,
       "espNamePlateMACAddress": espNamePlateMACAddress,
       "espNamePlateUTCTimeOffset": espNamePlateUTCTimeOffset,
       "espNamePlateModelNumber": espNamePlateModelNumber,
       "espNamePlateSerialNumber": espNamePlateSerialNumber,
       "espNamePlateDateofManufacture": espNamePlateDateofManufacture,
       "espNamePlateFirmwareVersion": espNamePlateFirmwareVersion,
       "espNamePlateFirmwareVersionTimeStamp": espNamePlateFirmwareVersionTimeStamp,
       "espNamePlateType": espNamePlateType,
       "espUnit": espUnit,
       "espUnitConfigTable": espUnitConfigTable,
       "espUnitConfigEntry": espUnitConfigEntry,
       "espUnitConfigIndex": espUnitConfigIndex,
       "espUnitConfigName": espUnitConfigName,
       "espUnitConfigLocation": espUnitConfigLocation,
       "espUnitConfigEnergyReset": espUnitConfigEnergyReset,
       "espUnitConfigResetNetworkManagementCard": espUnitConfigResetNetworkManagementCard,
       "espUnitPropertiesTable": espUnitPropertiesTable,
       "espUnitPropertiesEntry": espUnitPropertiesEntry,
       "espUnitPropertiesIndex": espUnitPropertiesIndex,
       "espUnitPropertiesName": espUnitPropertiesName,
       "espUnitPropertiesOutletCount": espUnitPropertiesOutletCount,
       "espUnitPropertiesSwitchedOutletCount": espUnitPropertiesSwitchedOutletCount,
       "espUnitPropertiesMeteredOutletCount": espUnitPropertiesMeteredOutletCount,
       "espUnitPropertiesInputPhaseCount": espUnitPropertiesInputPhaseCount,
       "espUnitPropertiesCircuitBreakerCount": espUnitPropertiesCircuitBreakerCount,
       "espUnitPropertiesMaxExternalSensorCount": espUnitPropertiesMaxExternalSensorCount,
       "espUnitPropertiesConnExternalSensorCount": espUnitPropertiesConnExternalSensorCount,
       "espUnitPropertiesRatedVoltage": espUnitPropertiesRatedVoltage,
       "espUnitPropertiesRatedMaxCurrent": espUnitPropertiesRatedMaxCurrent,
       "espUnitPropertiesRatedFrequency": espUnitPropertiesRatedFrequency,
       "espUnitPropertiesRatedPower": espUnitPropertiesRatedPower,
       "espUnitStatusTable": espUnitStatusTable,
       "espUnitStatusEntry": espUnitStatusEntry,
       "espUnitStatusIndex": espUnitStatusIndex,
       "espUnitStatusName": espUnitStatusName,
       "espUnitStatusLoadState": espUnitStatusLoadState,
       "espUnitStatusActivePower": espUnitStatusActivePower,
       "espUnitStatusApparentPower": espUnitStatusApparentPower,
       "espUnitStatusEnergy": espUnitStatusEnergy,
       "espUnitStatusResettableEnergy": espUnitStatusResettableEnergy,
       "espUnitStatusEnergyStartTime": espUnitStatusEnergyStartTime,
       "espInputPhase": espInputPhase,
       "espInputPhaseConfigTable": espInputPhaseConfigTable,
       "espInputPhaseConfigEntry": espInputPhaseConfigEntry,
       "espInputPhaseConfigIndex": espInputPhaseConfigIndex,
       "espInputPhaseConfigCount": espInputPhaseConfigCount,
       "espInputPhaseStatusTable": espInputPhaseStatusTable,
       "espInputPhaseStatusEntry": espInputPhaseStatusEntry,
       "espInputPhaseStatusIndex": espInputPhaseStatusIndex,
       "espInputPhaseStatusCount": espInputPhaseStatusCount,
       "espInputPhaseStatusCurrentState": espInputPhaseStatusCurrentState,
       "espInputPhaseStatusVoltageState": espInputPhaseStatusVoltageState,
       "espInputPhaseStatusCurrent": espInputPhaseStatusCurrent,
       "espInputPhaseStatusVoltage": espInputPhaseStatusVoltage,
       "espInputPhaseStatusActivePower": espInputPhaseStatusActivePower,
       "espInputPhaseStatusApparentPower": espInputPhaseStatusApparentPower,
       "espInputPhaseStatusPowerFactor": espInputPhaseStatusPowerFactor,
       "espCircuitBreaker": espCircuitBreaker,
       "espCircuitBreakerConfigTable": espCircuitBreakerConfigTable,
       "espCircuitBreakerConfigEntry": espCircuitBreakerConfigEntry,
       "espCircuitBreakerConfigIndex": espCircuitBreakerConfigIndex,
       "espCircuitBreakerConfigCount": espCircuitBreakerConfigCount,
       "espCircuitBreakerName": espCircuitBreakerName,
       "espCircuitBreakerPropertiesTable": espCircuitBreakerPropertiesTable,
       "espCircuitBreakerPropertiesEntry": espCircuitBreakerPropertiesEntry,
       "espCircuitBreakerPropertiesIndex": espCircuitBreakerPropertiesIndex,
       "espCircuitBreakerPropertiesCount": espCircuitBreakerPropertiesCount,
       "espCircuitBreakerPropertiesInputLayout": espCircuitBreakerPropertiesInputLayout,
       "espCircuitBreakerStatusTable": espCircuitBreakerStatusTable,
       "espCircuitBreakerStatusEntry": espCircuitBreakerStatusEntry,
       "espCircuitBreakerStatusIndex": espCircuitBreakerStatusIndex,
       "espCircuitBreakerStatusCount": espCircuitBreakerStatusCount,
       "espCircuitBreakerLabel": espCircuitBreakerLabel,
       "espCircuitBreakerStatusLoadState": espCircuitBreakerStatusLoadState,
       "espCircuitBreakerStatusCurrent": espCircuitBreakerStatusCurrent,
       "espExternalSensor": espExternalSensor,
       "espExternalSensorNamePlateTable": espExternalSensorNamePlateTable,
       "espExternalSensorNamePlateEntry": espExternalSensorNamePlateEntry,
       "espExternalSensorNamePlateIndex": espExternalSensorNamePlateIndex,
       "espExternalSensorNamePlateName": espExternalSensorNamePlateName,
       "espExternalSensorNamePlateSerialNumber": espExternalSensorNamePlateSerialNumber,
       "espExternalSensorNamePlateType": espExternalSensorNamePlateType,
       "espExternalSensorNamePlateUnits": espExternalSensorNamePlateUnits,
       "espExternalSensorConfigTable": espExternalSensorConfigTable,
       "espExternalSensorConfigEntry": espExternalSensorConfigEntry,
       "espExternalSensorConfigIndex": espExternalSensorConfigIndex,
       "espExternalSensorConfigAlarmState": espExternalSensorConfigAlarmState,
       "espExternalSensorStatusTable": espExternalSensorStatusTable,
       "espExternalSensorStatusEntry": espExternalSensorStatusEntry,
       "espExternalSensorStatusIndex": espExternalSensorStatusIndex,
       "espExternalSensorStatusName": espExternalSensorStatusName,
       "espExternalSensorStatusAisle": espExternalSensorStatusAisle,
       "espExternalSensorStatusCommStatus": espExternalSensorStatusCommStatus,
       "espExternalSensorStatusState": espExternalSensorStatusState,
       "espExternalSensorStatusValue": espExternalSensorStatusValue,
       "espExternalSensorStatusHighPrecisionValue": espExternalSensorStatusHighPrecisionValue,
       "espTraps": espTraps,
       "espTrapsInfoIndex": espTrapsInfoIndex,
       "espUserName": espUserName,
       "espFirmwareVersion": espFirmwareVersion,
       "espIndex": espIndex,
       "espExternalSensorIndex": espExternalSensorIndex,
       "espErrorDescription": espErrorDescription,
       "espNetworkCardStart": espNetworkCardStart,
       "espNetworkCardReset": espNetworkCardReset,
       "espFirmwareUpdateCompleted": espFirmwareUpdateCompleted,
       "espUserPasswordChange": espUserPasswordChange,
       "espLogFileCleared": espLogFileCleared,
       "espConfigurationFileExported": espConfigurationFileExported,
       "espUnitActivePowerStateChange": espUnitActivePowerStateChange,
       "espInputphaseVoltageStateChange": espInputphaseVoltageStateChange,
       "espInputphaseCurrentStateChange": espInputphaseCurrentStateChange,
       "espCircuitBreakerCurrentStateChange": espCircuitBreakerCurrentStateChange,
       "espExternalSensorStateChange": espExternalSensorStateChange,
       "espConfigurationFileImported": espConfigurationFileImported,
       "espNetworkUp": espNetworkUp}
)
