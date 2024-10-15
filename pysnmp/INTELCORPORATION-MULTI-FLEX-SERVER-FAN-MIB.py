# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:07 2024
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

(chassis,) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-MIB",
    "chassis")

(groups,
 regModule) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    "groups",
    "regModule")

(FaultLedStates,
 INT32withException,
 IdromBinary16,
 Index,
 Power,
 PowerLedStates,
 Presence,
 PresenceLedStates) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    "FaultLedStates",
    "INT32withException",
    "IdromBinary16",
    "Index",
    "Power",
    "PowerLedStates",
    "Presence",
    "PresenceLedStates")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

multiFlexServerFanMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 16)
)
multiFlexServerFanMibModule.setRevisions(
        ("2007-08-16 13:00",
         "2007-06-19 00:30",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-30 19:00",
         "2007-05-21 17:00",
         "2007-04-25 17:00",
         "2007-04-24 16:30",
         "2007-04-18 19:05",
         "2007-04-09 10:30",
         "2007-04-02 10:30",
         "2007-03-14 17:00",
         "2007-03-13 15:00",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2006-11-07 11:30",
         "2006-10-02 06:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MaxFanFrus_Type = Unsigned32
_MaxFanFrus_Object = MibScalar
maxFanFrus = _MaxFanFrus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 16),
    _MaxFanFrus_Type()
)
maxFanFrus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFanFrus.setStatus("current")
_NumOfFanFrus_Type = Integer32
_NumOfFanFrus_Object = MibScalar
numOfFanFrus = _NumOfFanFrus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 26),
    _NumOfFanFrus_Type()
)
numOfFanFrus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfFanFrus.setStatus("current")
_FanFruPresenceMask_Type = DisplayString
_FanFruPresenceMask_Object = MibScalar
fanFruPresenceMask = _FanFruPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 36),
    _FanFruPresenceMask_Type()
)
fanFruPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruPresenceMask.setStatus("current")
_Fans_ObjectIdentity = ObjectIdentity
fans = _Fans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206)
)
if mibBuilder.loadTexts:
    fans.setStatus("current")
_FanFruTable_Object = MibTable
fanFruTable = _FanFruTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1)
)
if mibBuilder.loadTexts:
    fanFruTable.setStatus("current")
_FanFruEntry_Object = MibTableRow
fanFruEntry = _FanFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1)
)
fanFruEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruIndex"),
)
if mibBuilder.loadTexts:
    fanFruEntry.setStatus("current")
_FanFruIndex_Type = Index
_FanFruIndex_Object = MibTableColumn
fanFruIndex = _FanFruIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 1),
    _FanFruIndex_Type()
)
fanFruIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruIndex.setStatus("current")
_FanFruPresence_Type = Presence
_FanFruPresence_Object = MibTableColumn
fanFruPresence = _FanFruPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 2),
    _FanFruPresence_Type()
)
fanFruPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruPresence.setStatus("current")
_FanFruVendor_Type = DisplayString
_FanFruVendor_Object = MibTableColumn
fanFruVendor = _FanFruVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 3),
    _FanFruVendor_Type()
)
fanFruVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruVendor.setStatus("current")
_FanFruMfgDate_Type = DisplayString
_FanFruMfgDate_Object = MibTableColumn
fanFruMfgDate = _FanFruMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 4),
    _FanFruMfgDate_Type()
)
fanFruMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruMfgDate.setStatus("current")
_FanFruDeviceName_Type = DisplayString
_FanFruDeviceName_Object = MibTableColumn
fanFruDeviceName = _FanFruDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 5),
    _FanFruDeviceName_Type()
)
fanFruDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruDeviceName.setStatus("current")
_FanFruPart_Type = IdromBinary16
_FanFruPart_Object = MibTableColumn
fanFruPart = _FanFruPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 6),
    _FanFruPart_Type()
)
fanFruPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruPart.setStatus("current")
_FanFruSerialNo_Type = IdromBinary16
_FanFruSerialNo_Object = MibTableColumn
fanFruSerialNo = _FanFruSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 7),
    _FanFruSerialNo_Type()
)
fanFruSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruSerialNo.setStatus("current")
_FanFruMaximumPower_Type = Power
_FanFruMaximumPower_Object = MibTableColumn
fanFruMaximumPower = _FanFruMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 8),
    _FanFruMaximumPower_Type()
)
fanFruMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruMaximumPower.setStatus("current")
_FanFruNominalPower_Type = Power
_FanFruNominalPower_Object = MibTableColumn
fanFruNominalPower = _FanFruNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 9),
    _FanFruNominalPower_Type()
)
fanFruNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruNominalPower.setStatus("current")
_FanFruAssetTag_Type = IdromBinary16
_FanFruAssetTag_Object = MibTableColumn
fanFruAssetTag = _FanFruAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 10),
    _FanFruAssetTag_Type()
)
fanFruAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruAssetTag.setStatus("current")
_FanFruPowerLed_Type = PowerLedStates
_FanFruPowerLed_Object = MibTableColumn
fanFruPowerLed = _FanFruPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 11),
    _FanFruPowerLed_Type()
)
fanFruPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruPowerLed.setStatus("current")
_FanFruFaultLed_Type = FaultLedStates
_FanFruFaultLed_Object = MibTableColumn
fanFruFaultLed = _FanFruFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 12),
    _FanFruFaultLed_Type()
)
fanFruFaultLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruFaultLed.setStatus("current")
_FanFruOpCodeVersion_Type = DisplayString
_FanFruOpCodeVersion_Object = MibTableColumn
fanFruOpCodeVersion = _FanFruOpCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 13),
    _FanFruOpCodeVersion_Type()
)
fanFruOpCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruOpCodeVersion.setStatus("current")
_FanFruBootBlockVersion_Type = DisplayString
_FanFruBootBlockVersion_Object = MibTableColumn
fanFruBootBlockVersion = _FanFruBootBlockVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 14),
    _FanFruBootBlockVersion_Type()
)
fanFruBootBlockVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruBootBlockVersion.setStatus("current")
_FanFruNumOfFans_Type = INT32withException
_FanFruNumOfFans_Object = MibTableColumn
fanFruNumOfFans = _FanFruNumOfFans_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 15),
    _FanFruNumOfFans_Type()
)
fanFruNumOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruNumOfFans.setStatus("current")
_FanFruInletTemperature_Type = INT32withException
_FanFruInletTemperature_Object = MibTableColumn
fanFruInletTemperature = _FanFruInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 1, 1, 16),
    _FanFruInletTemperature_Type()
)
fanFruInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanFruInletTemperature.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 2)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 2, 1)
)
fanEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")
_FanIndex_Type = Index
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 2, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")


class _FanRpmMinimum_Type(Integer32):
    """Custom type fanRpmMinimum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -2),
          ("unknown", -1))
    )


_FanRpmMinimum_Type.__name__ = "Integer32"
_FanRpmMinimum_Object = MibTableColumn
fanRpmMinimum = _FanRpmMinimum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 2, 1, 2),
    _FanRpmMinimum_Type()
)
fanRpmMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMinimum.setStatus("current")


class _FanRpmMaximum_Type(Integer32):
    """Custom type fanRpmMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -2),
          ("unknown", -1))
    )


_FanRpmMaximum_Type.__name__ = "Integer32"
_FanRpmMaximum_Object = MibTableColumn
fanRpmMaximum = _FanRpmMaximum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 2, 1, 3),
    _FanRpmMaximum_Type()
)
fanRpmMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmMaximum.setStatus("current")


class _FanRpmReading_Type(Integer32):
    """Custom type fanRpmReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -2),
          ("notspinning", 0),
          ("unknown", -1))
    )


_FanRpmReading_Type.__name__ = "Integer32"
_FanRpmReading_Object = MibTableColumn
fanRpmReading = _FanRpmReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 206, 2, 1, 4),
    _FanRpmReading_Type()
)
fanRpmReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanRpmReading.setStatus("current")

# Managed Objects groups

fanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 16)
)
fanGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "maxFanFrus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "numOfFanFrus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruPowerLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruFaultLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruOpCodeVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruBootBlockVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruNumOfFans"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanFruInletTemperature"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanRpmMinimum"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanRpmMaximum"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB", "fanRpmReading"))
)
if mibBuilder.loadTexts:
    fanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-FAN-MIB",
    **{"multiFlexServerFanMibModule": multiFlexServerFanMibModule,
       "fanGroup": fanGroup,
       "maxFanFrus": maxFanFrus,
       "numOfFanFrus": numOfFanFrus,
       "fanFruPresenceMask": fanFruPresenceMask,
       "fans": fans,
       "fanFruTable": fanFruTable,
       "fanFruEntry": fanFruEntry,
       "fanFruIndex": fanFruIndex,
       "fanFruPresence": fanFruPresence,
       "fanFruVendor": fanFruVendor,
       "fanFruMfgDate": fanFruMfgDate,
       "fanFruDeviceName": fanFruDeviceName,
       "fanFruPart": fanFruPart,
       "fanFruSerialNo": fanFruSerialNo,
       "fanFruMaximumPower": fanFruMaximumPower,
       "fanFruNominalPower": fanFruNominalPower,
       "fanFruAssetTag": fanFruAssetTag,
       "fanFruPowerLed": fanFruPowerLed,
       "fanFruFaultLed": fanFruFaultLed,
       "fanFruOpCodeVersion": fanFruOpCodeVersion,
       "fanFruBootBlockVersion": fanFruBootBlockVersion,
       "fanFruNumOfFans": fanFruNumOfFans,
       "fanFruInletTemperature": fanFruInletTemperature,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanRpmMinimum": fanRpmMinimum,
       "fanRpmMaximum": fanRpmMaximum,
       "fanRpmReading": fanRpmReading}
)
