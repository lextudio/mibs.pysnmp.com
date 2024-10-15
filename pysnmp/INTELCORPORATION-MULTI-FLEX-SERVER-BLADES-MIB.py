# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:05 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

multiFlexServerBladesMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 12)
)
multiFlexServerBladesMibModule.setRevisions(
        ("2008-05-19 20:28",
         "2008-05-07 02:40",
         "2007-09-19 15:40",
         "2007-08-31 09:30",
         "2007-08-29 19:30",
         "2007-08-29 14:30",
         "2007-08-27 16:00",
         "2007-08-22 15:45",
         "2007-08-20 15:30",
         "2007-08-16 13:30",
         "2007-07-27 15:30",
         "2007-07-09 12:30",
         "2007-07-05 16:00",
         "2007-05-21 14:00",
         "2007-05-21 14:00",
         "2007-04-09 10:30",
         "2007-03-14 11:00",
         "2007-03-13 18:00",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2006-11-07 07:01",
         "2006-10-01 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MaxBlades_Type = Unsigned32
_MaxBlades_Object = MibScalar
maxBlades = _MaxBlades_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 12),
    _MaxBlades_Type()
)
maxBlades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBlades.setStatus("current")
_NumOfBlades_Type = Integer32
_NumOfBlades_Object = MibScalar
numOfBlades = _NumOfBlades_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 22),
    _NumOfBlades_Type()
)
numOfBlades.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfBlades.setStatus("current")
_BladePresenceMask_Type = DisplayString
_BladePresenceMask_Object = MibScalar
bladePresenceMask = _BladePresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 32),
    _BladePresenceMask_Type()
)
bladePresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePresenceMask.setStatus("current")
_Blades_ObjectIdentity = ObjectIdentity
blades = _Blades_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202)
)
if mibBuilder.loadTexts:
    blades.setStatus("current")
_BladeTable_Object = MibTable
bladeTable = _BladeTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1)
)
if mibBuilder.loadTexts:
    bladeTable.setStatus("current")
_BladeEntry_Object = MibTableRow
bladeEntry = _BladeEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1)
)
bladeEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
)
if mibBuilder.loadTexts:
    bladeEntry.setStatus("current")
_BladeSlotId_Type = Index
_BladeSlotId_Object = MibTableColumn
bladeSlotId = _BladeSlotId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 1),
    _BladeSlotId_Type()
)
bladeSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeSlotId.setStatus("current")
_BladePresence_Type = Presence
_BladePresence_Object = MibTableColumn
bladePresence = _BladePresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 2),
    _BladePresence_Type()
)
bladePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladePresence.setStatus("current")
_MaxFrus_Type = INT32withException
_MaxFrus_Object = MibTableColumn
maxFrus = _MaxFrus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 3),
    _MaxFrus_Type()
)
maxFrus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxFrus.setStatus("current")
_NumOfFrus_Type = INT32withException
_NumOfFrus_Object = MibTableColumn
numOfFrus = _NumOfFrus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 4),
    _NumOfFrus_Type()
)
numOfFrus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfFrus.setStatus("current")
_BladeFruPresenceMask_Type = DisplayString
_BladeFruPresenceMask_Object = MibTableColumn
bladeFruPresenceMask = _BladeFruPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 5),
    _BladeFruPresenceMask_Type()
)
bladeFruPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruPresenceMask.setStatus("current")
_BladePowerLed_Type = PowerLedStates
_BladePowerLed_Object = MibTableColumn
bladePowerLed = _BladePowerLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 6),
    _BladePowerLed_Type()
)
bladePowerLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePowerLed.setStatus("current")
_BladeFaultLed_Type = FaultLedStates
_BladeFaultLed_Object = MibTableColumn
bladeFaultLed = _BladeFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 7),
    _BladeFaultLed_Type()
)
bladeFaultLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFaultLed.setStatus("current")
_BladePresenceLed_Type = PresenceLedStates
_BladePresenceLed_Object = MibTableColumn
bladePresenceLed = _BladePresenceLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 8),
    _BladePresenceLed_Type()
)
bladePresenceLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bladePresenceLed.setStatus("current")
_BladeBmcFirmwareVersion_Type = DisplayString
_BladeBmcFirmwareVersion_Object = MibTableColumn
bladeBmcFirmwareVersion = _BladeBmcFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 9),
    _BladeBmcFirmwareVersion_Type()
)
bladeBmcFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBmcFirmwareVersion.setStatus("current")
_BladeBootBlockVersion_Type = DisplayString
_BladeBootBlockVersion_Object = MibTableColumn
bladeBootBlockVersion = _BladeBootBlockVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 10),
    _BladeBootBlockVersion_Type()
)
bladeBootBlockVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBootBlockVersion.setStatus("current")
_BladeBiosVersion_Type = DisplayString
_BladeBiosVersion_Object = MibTableColumn
bladeBiosVersion = _BladeBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 11),
    _BladeBiosVersion_Type()
)
bladeBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBiosVersion.setStatus("current")


class _BladeConsoleRedirection_Type(Integer32):
    """Custom type bladeConsoleRedirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("networkSerialPort", 1),
          ("notApplicable", -32),
          ("unknown", -16))
    )


_BladeConsoleRedirection_Type.__name__ = "Integer32"
_BladeConsoleRedirection_Object = MibTableColumn
bladeConsoleRedirection = _BladeConsoleRedirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 12),
    _BladeConsoleRedirection_Type()
)
bladeConsoleRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeConsoleRedirection.setStatus("current")


class _BladeLegacyOsRedirection_Type(Integer32):
    """Custom type bladeLegacyOsRedirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("legacyOsRedirection", 1),
          ("noLegacyOsRedirection", 0),
          ("notApplicable", -32),
          ("unknown", -16))
    )


_BladeLegacyOsRedirection_Type.__name__ = "Integer32"
_BladeLegacyOsRedirection_Object = MibTableColumn
bladeLegacyOsRedirection = _BladeLegacyOsRedirection_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 13),
    _BladeLegacyOsRedirection_Type()
)
bladeLegacyOsRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeLegacyOsRedirection.setStatus("current")
_BladeBootCount_Type = Unsigned32
_BladeBootCount_Object = MibTableColumn
bladeBootCount = _BladeBootCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 1, 1, 14),
    _BladeBootCount_Type()
)
bladeBootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeBootCount.setStatus("current")
_BladeFruTable_Object = MibTable
bladeFruTable = _BladeFruTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2)
)
if mibBuilder.loadTexts:
    bladeFruTable.setStatus("current")
_BladeFruEntry_Object = MibTableRow
bladeFruEntry = _BladeFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1)
)
bladeFruEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruType"),
)
if mibBuilder.loadTexts:
    bladeFruEntry.setStatus("current")


class _BladeFruType_Type(Integer32):
    """Custom type bladeFruType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blade", 1),
          ("mezzanine", 2))
    )


_BladeFruType_Type.__name__ = "Integer32"
_BladeFruType_Object = MibTableColumn
bladeFruType = _BladeFruType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 1),
    _BladeFruType_Type()
)
bladeFruType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruType.setStatus("current")
_BladeFruPresence_Type = Presence
_BladeFruPresence_Object = MibTableColumn
bladeFruPresence = _BladeFruPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 2),
    _BladeFruPresence_Type()
)
bladeFruPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruPresence.setStatus("current")
_BladeFruVendor_Type = DisplayString
_BladeFruVendor_Object = MibTableColumn
bladeFruVendor = _BladeFruVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 3),
    _BladeFruVendor_Type()
)
bladeFruVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruVendor.setStatus("current")
_BladeFruMfgDate_Type = DisplayString
_BladeFruMfgDate_Object = MibTableColumn
bladeFruMfgDate = _BladeFruMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 4),
    _BladeFruMfgDate_Type()
)
bladeFruMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruMfgDate.setStatus("current")
_BladeFruDeviceName_Type = DisplayString
_BladeFruDeviceName_Object = MibTableColumn
bladeFruDeviceName = _BladeFruDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 5),
    _BladeFruDeviceName_Type()
)
bladeFruDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruDeviceName.setStatus("current")
_BladeFruPart_Type = IdromBinary16
_BladeFruPart_Object = MibTableColumn
bladeFruPart = _BladeFruPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 6),
    _BladeFruPart_Type()
)
bladeFruPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruPart.setStatus("current")
_BladeFruSerialNo_Type = IdromBinary16
_BladeFruSerialNo_Object = MibTableColumn
bladeFruSerialNo = _BladeFruSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 7),
    _BladeFruSerialNo_Type()
)
bladeFruSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruSerialNo.setStatus("current")
_BladeFruMaximumPower_Type = Power
_BladeFruMaximumPower_Object = MibTableColumn
bladeFruMaximumPower = _BladeFruMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 8),
    _BladeFruMaximumPower_Type()
)
bladeFruMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruMaximumPower.setStatus("current")
_BladeFruNominalPower_Type = Power
_BladeFruNominalPower_Object = MibTableColumn
bladeFruNominalPower = _BladeFruNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 9),
    _BladeFruNominalPower_Type()
)
bladeFruNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruNominalPower.setStatus("current")
_BladeFruAssetTag_Type = IdromBinary16
_BladeFruAssetTag_Object = MibTableColumn
bladeFruAssetTag = _BladeFruAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 2, 1, 10),
    _BladeFruAssetTag_Type()
)
bladeFruAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeFruAssetTag.setStatus("current")
_BladeNicTable_Object = MibTable
bladeNicTable = _BladeNicTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 3)
)
if mibBuilder.loadTexts:
    bladeNicTable.setStatus("current")
_BladeNicEntry_Object = MibTableRow
bladeNicEntry = _BladeNicEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 3, 1)
)
bladeNicEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeNic"),
)
if mibBuilder.loadTexts:
    bladeNicEntry.setStatus("current")
_BladeNic_Type = MacAddress
_BladeNic_Object = MibTableColumn
bladeNic = _BladeNic_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 3, 1, 1),
    _BladeNic_Type()
)
bladeNic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeNic.setStatus("current")
_BladeProcessorTable_Object = MibTable
bladeProcessorTable = _BladeProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4)
)
if mibBuilder.loadTexts:
    bladeProcessorTable.setStatus("current")
_BladeProcessorEntry_Object = MibTableRow
bladeProcessorEntry = _BladeProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1)
)
bladeProcessorEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "handle"),
)
if mibBuilder.loadTexts:
    bladeProcessorEntry.setStatus("current")
_Handle_Type = Index
_Handle_Object = MibTableColumn
handle = _Handle_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 1),
    _Handle_Type()
)
handle.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    handle.setStatus("current")
_BladeProcessorSocket_Type = DisplayString
_BladeProcessorSocket_Object = MibTableColumn
bladeProcessorSocket = _BladeProcessorSocket_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 2),
    _BladeProcessorSocket_Type()
)
bladeProcessorSocket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorSocket.setStatus("current")
_BladeProcessorPresence_Type = Presence
_BladeProcessorPresence_Object = MibTableColumn
bladeProcessorPresence = _BladeProcessorPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 3),
    _BladeProcessorPresence_Type()
)
bladeProcessorPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorPresence.setStatus("current")
_BladeProcessorType_Type = DisplayString
_BladeProcessorType_Object = MibTableColumn
bladeProcessorType = _BladeProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 4),
    _BladeProcessorType_Type()
)
bladeProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorType.setStatus("current")
_BladeProcessorFamily_Type = DisplayString
_BladeProcessorFamily_Object = MibTableColumn
bladeProcessorFamily = _BladeProcessorFamily_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 5),
    _BladeProcessorFamily_Type()
)
bladeProcessorFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorFamily.setStatus("current")
_BladeProcessorManufacturer_Type = DisplayString
_BladeProcessorManufacturer_Object = MibTableColumn
bladeProcessorManufacturer = _BladeProcessorManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 6),
    _BladeProcessorManufacturer_Type()
)
bladeProcessorManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorManufacturer.setStatus("current")
_BladeProcessorID_Type = DisplayString
_BladeProcessorID_Object = MibTableColumn
bladeProcessorID = _BladeProcessorID_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 7),
    _BladeProcessorID_Type()
)
bladeProcessorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorID.setStatus("current")
_BladeProcessorVersion_Type = DisplayString
_BladeProcessorVersion_Object = MibTableColumn
bladeProcessorVersion = _BladeProcessorVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 8),
    _BladeProcessorVersion_Type()
)
bladeProcessorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorVersion.setStatus("current")
_BladeProcessorVoltage_Type = DisplayString
_BladeProcessorVoltage_Object = MibTableColumn
bladeProcessorVoltage = _BladeProcessorVoltage_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 9),
    _BladeProcessorVoltage_Type()
)
bladeProcessorVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorVoltage.setStatus("current")
_BladeProcessorExtClock_Type = Unsigned32
_BladeProcessorExtClock_Object = MibTableColumn
bladeProcessorExtClock = _BladeProcessorExtClock_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 10),
    _BladeProcessorExtClock_Type()
)
bladeProcessorExtClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorExtClock.setStatus("current")
_BladeProcessorMaxSpeed_Type = Unsigned32
_BladeProcessorMaxSpeed_Object = MibTableColumn
bladeProcessorMaxSpeed = _BladeProcessorMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 11),
    _BladeProcessorMaxSpeed_Type()
)
bladeProcessorMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorMaxSpeed.setStatus("current")
_BladeProcessorStatus_Type = DisplayString
_BladeProcessorStatus_Object = MibTableColumn
bladeProcessorStatus = _BladeProcessorStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 12),
    _BladeProcessorStatus_Type()
)
bladeProcessorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorStatus.setStatus("current")
_BladeProcessorUpgrade_Type = DisplayString
_BladeProcessorUpgrade_Object = MibTableColumn
bladeProcessorUpgrade = _BladeProcessorUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 13),
    _BladeProcessorUpgrade_Type()
)
bladeProcessorUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorUpgrade.setStatus("current")
_BladeProcessorSerialNo_Type = DisplayString
_BladeProcessorSerialNo_Object = MibTableColumn
bladeProcessorSerialNo = _BladeProcessorSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 14),
    _BladeProcessorSerialNo_Type()
)
bladeProcessorSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorSerialNo.setStatus("current")
_BladeProcessorAssetTag_Type = DisplayString
_BladeProcessorAssetTag_Object = MibTableColumn
bladeProcessorAssetTag = _BladeProcessorAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 15),
    _BladeProcessorAssetTag_Type()
)
bladeProcessorAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorAssetTag.setStatus("current")
_BladeProcessorPartNo_Type = DisplayString
_BladeProcessorPartNo_Object = MibTableColumn
bladeProcessorPartNo = _BladeProcessorPartNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 4, 1, 16),
    _BladeProcessorPartNo_Type()
)
bladeProcessorPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeProcessorPartNo.setStatus("current")
_BladeMemorySummaryTable_Object = MibTable
bladeMemorySummaryTable = _BladeMemorySummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5)
)
if mibBuilder.loadTexts:
    bladeMemorySummaryTable.setStatus("current")
_BladeMemorySummaryEntry_Object = MibTableRow
bladeMemorySummaryEntry = _BladeMemorySummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1)
)
if mibBuilder.loadTexts:
    bladeMemorySummaryEntry.setStatus("current")
_BladeMSMaxDevices_Type = Integer32
_BladeMSMaxDevices_Object = MibTableColumn
bladeMSMaxDevices = _BladeMSMaxDevices_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 1),
    _BladeMSMaxDevices_Type()
)
bladeMSMaxDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSMaxDevices.setStatus("current")
_BladeMSNumOfDevices_Type = Integer32
_BladeMSNumOfDevices_Object = MibTableColumn
bladeMSNumOfDevices = _BladeMSNumOfDevices_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 2),
    _BladeMSNumOfDevices_Type()
)
bladeMSNumOfDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSNumOfDevices.setStatus("current")
_BladeMSCapacity_Type = Unsigned32
_BladeMSCapacity_Object = MibTableColumn
bladeMSCapacity = _BladeMSCapacity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 3),
    _BladeMSCapacity_Type()
)
bladeMSCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSCapacity.setStatus("current")
_BladeMSTotalSize_Type = Unsigned32
_BladeMSTotalSize_Object = MibTableColumn
bladeMSTotalSize = _BladeMSTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 4),
    _BladeMSTotalSize_Type()
)
bladeMSTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSTotalSize.setStatus("current")
_BladeMSEffectiveSize_Type = Unsigned32
_BladeMSEffectiveSize_Object = MibTableColumn
bladeMSEffectiveSize = _BladeMSEffectiveSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 5),
    _BladeMSEffectiveSize_Type()
)
bladeMSEffectiveSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSEffectiveSize.setStatus("current")
_BladeMSNumFailed_Type = Unsigned32
_BladeMSNumFailed_Object = MibTableColumn
bladeMSNumFailed = _BladeMSNumFailed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 6),
    _BladeMSNumFailed_Type()
)
bladeMSNumFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSNumFailed.setStatus("current")
_BladeMSDisabledSize_Type = Unsigned32
_BladeMSDisabledSize_Object = MibTableColumn
bladeMSDisabledSize = _BladeMSDisabledSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 7),
    _BladeMSDisabledSize_Type()
)
bladeMSDisabledSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSDisabledSize.setStatus("current")
_BladeMSSpareSize_Type = Unsigned32
_BladeMSSpareSize_Object = MibTableColumn
bladeMSSpareSize = _BladeMSSpareSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 8),
    _BladeMSSpareSize_Type()
)
bladeMSSpareSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSSpareSize.setStatus("current")


class _BladeMSRasPossible_Type(Integer32):
    """Custom type bladeMSRasPossible based on Integer32"""
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
        *(("notSupported", 0),
          ("supportsBoth", 3),
          ("supportsMirroring", 1),
          ("supportsSparing", 2))
    )


_BladeMSRasPossible_Type.__name__ = "Integer32"
_BladeMSRasPossible_Object = MibTableColumn
bladeMSRasPossible = _BladeMSRasPossible_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 9),
    _BladeMSRasPossible_Type()
)
bladeMSRasPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSRasPossible.setStatus("current")


class _BladeMSRasConfiguration_Type(Integer32):
    """Custom type bladeMSRasConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mirroring", 1),
          ("none", 0),
          ("sparing", 2))
    )


_BladeMSRasConfiguration_Type.__name__ = "Integer32"
_BladeMSRasConfiguration_Object = MibTableColumn
bladeMSRasConfiguration = _BladeMSRasConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 10),
    _BladeMSRasConfiguration_Type()
)
bladeMSRasConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSRasConfiguration.setStatus("current")


class _BladeMSErrorCorrection_Type(Integer32):
    """Custom type bladeMSErrorCorrection based on Integer32"""
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
        *(("crc", 7),
          ("multiBitEcc", 6),
          ("none", 3),
          ("other", 1),
          ("parity", 4),
          ("singleBitEcc", 5),
          ("unknown", 2))
    )


_BladeMSErrorCorrection_Type.__name__ = "Integer32"
_BladeMSErrorCorrection_Object = MibTableColumn
bladeMSErrorCorrection = _BladeMSErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 5, 1, 11),
    _BladeMSErrorCorrection_Type()
)
bladeMSErrorCorrection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMSErrorCorrection.setStatus("current")
_BladeMemoryTable_Object = MibTable
bladeMemoryTable = _BladeMemoryTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6)
)
if mibBuilder.loadTexts:
    bladeMemoryTable.setStatus("current")
_BladeMemoryEntry_Object = MibTableRow
bladeMemoryEntry = _BladeMemoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1)
)
bladeMemoryEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "handle"),
)
if mibBuilder.loadTexts:
    bladeMemoryEntry.setStatus("current")


class _BladeMemTotalWidth_Type(Integer32):
    """Custom type bladeMemTotalWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("unknown", -1)
    )


_BladeMemTotalWidth_Type.__name__ = "Integer32"
_BladeMemTotalWidth_Object = MibTableColumn
bladeMemTotalWidth = _BladeMemTotalWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 1),
    _BladeMemTotalWidth_Type()
)
bladeMemTotalWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemTotalWidth.setStatus("current")


class _BladeMemDataWidth_Type(Integer32):
    """Custom type bladeMemDataWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("unknown", -1)
    )


_BladeMemDataWidth_Type.__name__ = "Integer32"
_BladeMemDataWidth_Object = MibTableColumn
bladeMemDataWidth = _BladeMemDataWidth_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 2),
    _BladeMemDataWidth_Type()
)
bladeMemDataWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemDataWidth.setStatus("current")


class _BladeMemSize_Type(Integer32):
    """Custom type bladeMemSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 0),
          ("unknown", -1))
    )


_BladeMemSize_Type.__name__ = "Integer32"
_BladeMemSize_Object = MibTableColumn
bladeMemSize = _BladeMemSize_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 3),
    _BladeMemSize_Type()
)
bladeMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemSize.setStatus("current")


class _BladeMemGranularity_Type(Integer32):
    """Custom type bladeMemGranularity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kilobytes", 1),
          ("megabytes", 0),
          ("unknown", -1))
    )


_BladeMemGranularity_Type.__name__ = "Integer32"
_BladeMemGranularity_Object = MibTableColumn
bladeMemGranularity = _BladeMemGranularity_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 4),
    _BladeMemGranularity_Type()
)
bladeMemGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemGranularity.setStatus("current")


class _BladeMemFormFactor_Type(Integer32):
    """Custom type bladeMemFormFactor based on Integer32"""
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
        *(("chip", 5),
          ("dimm", 9),
          ("dip", 6),
          ("fbdimm", 15),
          ("other", 1),
          ("proprietaryCard", 8),
          ("rimm", 12),
          ("rowOfChips", 11),
          ("simm", 3),
          ("sip", 4),
          ("sodimm", 13),
          ("srimm", 14),
          ("tsop", 10),
          ("unknown", 2),
          ("zip", 7))
    )


_BladeMemFormFactor_Type.__name__ = "Integer32"
_BladeMemFormFactor_Object = MibTableColumn
bladeMemFormFactor = _BladeMemFormFactor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 5),
    _BladeMemFormFactor_Type()
)
bladeMemFormFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemFormFactor.setStatus("current")


class _BladeMemDeviceSet_Type(Integer32):
    """Custom type bladeMemDeviceSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("noSet", 0),
          ("unknown", -1))
    )


_BladeMemDeviceSet_Type.__name__ = "Integer32"
_BladeMemDeviceSet_Object = MibTableColumn
bladeMemDeviceSet = _BladeMemDeviceSet_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 6),
    _BladeMemDeviceSet_Type()
)
bladeMemDeviceSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemDeviceSet.setStatus("current")
_BladeMemLocation_Type = DisplayString
_BladeMemLocation_Object = MibTableColumn
bladeMemLocation = _BladeMemLocation_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 7),
    _BladeMemLocation_Type()
)
bladeMemLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemLocation.setStatus("current")
_BladeMemBank_Type = DisplayString
_BladeMemBank_Object = MibTableColumn
bladeMemBank = _BladeMemBank_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 8),
    _BladeMemBank_Type()
)
bladeMemBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemBank.setStatus("current")


class _BladeMemType_Type(Integer32):
    """Custom type bladeMemType based on Integer32"""
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
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("cdram", 13),
          ("ddr", 18),
          ("ddr2", 19),
          ("ddr2fbdimm", 20),
          ("dram", 3),
          ("dram3", 14),
          ("edram", 4),
          ("eeprom", 10),
          ("eprom", 12),
          ("feprom", 11),
          ("flash", 9),
          ("other", 1),
          ("ram", 7),
          ("rdram", 17),
          ("rom", 8),
          ("sdram", 15),
          ("sgram", 16),
          ("sram", 6),
          ("unknown", 2),
          ("vram", 5))
    )


_BladeMemType_Type.__name__ = "Integer32"
_BladeMemType_Object = MibTableColumn
bladeMemType = _BladeMemType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 9),
    _BladeMemType_Type()
)
bladeMemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemType.setStatus("current")


class _BladeMemTypeDetail_Type(Bits):
    """Custom type bladeMemTypeDetail based on Bits"""
    namedValues = NamedValues(
        *(("cacheDram", 11),
          ("cmos", 8),
          ("edo", 9),
          ("fastPaged", 3),
          ("nonVolatile", 12),
          ("other", 1),
          ("pseudoStatic", 5),
          ("rambus", 6),
          ("reserved", 0),
          ("staticColumn", 4),
          ("synchronous", 7),
          ("unknown", 2),
          ("windowDram", 10))
    )

_BladeMemTypeDetail_Type.__name__ = "Bits"
_BladeMemTypeDetail_Object = MibTableColumn
bladeMemTypeDetail = _BladeMemTypeDetail_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 10),
    _BladeMemTypeDetail_Type()
)
bladeMemTypeDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemTypeDetail.setStatus("current")


class _BladeMemSpeed_Type(Integer32):
    """Custom type bladeMemSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("unknown", 0)
    )


_BladeMemSpeed_Type.__name__ = "Integer32"
_BladeMemSpeed_Object = MibTableColumn
bladeMemSpeed = _BladeMemSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 11),
    _BladeMemSpeed_Type()
)
bladeMemSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemSpeed.setStatus("current")
_BladeMemManufacturer_Type = DisplayString
_BladeMemManufacturer_Object = MibTableColumn
bladeMemManufacturer = _BladeMemManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 12),
    _BladeMemManufacturer_Type()
)
bladeMemManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemManufacturer.setStatus("current")
_BladeMemSerialNo_Type = DisplayString
_BladeMemSerialNo_Object = MibTableColumn
bladeMemSerialNo = _BladeMemSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 13),
    _BladeMemSerialNo_Type()
)
bladeMemSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemSerialNo.setStatus("current")
_BladeMemAssetTag_Type = DisplayString
_BladeMemAssetTag_Object = MibTableColumn
bladeMemAssetTag = _BladeMemAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 14),
    _BladeMemAssetTag_Type()
)
bladeMemAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemAssetTag.setStatus("current")
_BladeMemPart_Type = DisplayString
_BladeMemPart_Object = MibTableColumn
bladeMemPart = _BladeMemPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 202, 6, 1, 15),
    _BladeMemPart_Type()
)
bladeMemPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bladeMemPart.setStatus("current")
bladeEntry.registerAugmentions(
    ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB",
     "bladeMemorySummaryEntry")
)
bladeMemorySummaryEntry.setIndexNames(*bladeEntry.getIndexNames())

# Managed Objects groups

bladeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 12)
)
bladeGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "maxBlades"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "numOfBlades"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladePresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeSlotId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "maxFrus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "numOfFrus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladePresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladePowerLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFaultLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladePresenceLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeBmcFirmwareVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeBootBlockVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeBiosVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeConsoleRedirection"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeLegacyOsRedirection"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeBootCount"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeFruAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeNic"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorSocket"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorFamily"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorManufacturer"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorID"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorVoltage"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorExtClock"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorMaxSpeed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorUpgrade"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeProcessorPartNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSMaxDevices"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSNumOfDevices"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSCapacity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSErrorCorrection"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSTotalSize"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSNumFailed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSDisabledSize"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSSpareSize"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSEffectiveSize"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSRasPossible"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMSRasConfiguration"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemTotalWidth"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemDataWidth"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemSize"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemGranularity"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemFormFactor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemDeviceSet"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemLocation"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemBank"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemTypeDetail"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemSpeed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemManufacturer"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB", "bladeMemPart"))
)
if mibBuilder.loadTexts:
    bladeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-BLADES-MIB",
    **{"multiFlexServerBladesMibModule": multiFlexServerBladesMibModule,
       "bladeGroup": bladeGroup,
       "maxBlades": maxBlades,
       "numOfBlades": numOfBlades,
       "bladePresenceMask": bladePresenceMask,
       "blades": blades,
       "bladeTable": bladeTable,
       "bladeEntry": bladeEntry,
       "bladeSlotId": bladeSlotId,
       "bladePresence": bladePresence,
       "maxFrus": maxFrus,
       "numOfFrus": numOfFrus,
       "bladeFruPresenceMask": bladeFruPresenceMask,
       "bladePowerLed": bladePowerLed,
       "bladeFaultLed": bladeFaultLed,
       "bladePresenceLed": bladePresenceLed,
       "bladeBmcFirmwareVersion": bladeBmcFirmwareVersion,
       "bladeBootBlockVersion": bladeBootBlockVersion,
       "bladeBiosVersion": bladeBiosVersion,
       "bladeConsoleRedirection": bladeConsoleRedirection,
       "bladeLegacyOsRedirection": bladeLegacyOsRedirection,
       "bladeBootCount": bladeBootCount,
       "bladeFruTable": bladeFruTable,
       "bladeFruEntry": bladeFruEntry,
       "bladeFruType": bladeFruType,
       "bladeFruPresence": bladeFruPresence,
       "bladeFruVendor": bladeFruVendor,
       "bladeFruMfgDate": bladeFruMfgDate,
       "bladeFruDeviceName": bladeFruDeviceName,
       "bladeFruPart": bladeFruPart,
       "bladeFruSerialNo": bladeFruSerialNo,
       "bladeFruMaximumPower": bladeFruMaximumPower,
       "bladeFruNominalPower": bladeFruNominalPower,
       "bladeFruAssetTag": bladeFruAssetTag,
       "bladeNicTable": bladeNicTable,
       "bladeNicEntry": bladeNicEntry,
       "bladeNic": bladeNic,
       "bladeProcessorTable": bladeProcessorTable,
       "bladeProcessorEntry": bladeProcessorEntry,
       "handle": handle,
       "bladeProcessorSocket": bladeProcessorSocket,
       "bladeProcessorPresence": bladeProcessorPresence,
       "bladeProcessorType": bladeProcessorType,
       "bladeProcessorFamily": bladeProcessorFamily,
       "bladeProcessorManufacturer": bladeProcessorManufacturer,
       "bladeProcessorID": bladeProcessorID,
       "bladeProcessorVersion": bladeProcessorVersion,
       "bladeProcessorVoltage": bladeProcessorVoltage,
       "bladeProcessorExtClock": bladeProcessorExtClock,
       "bladeProcessorMaxSpeed": bladeProcessorMaxSpeed,
       "bladeProcessorStatus": bladeProcessorStatus,
       "bladeProcessorUpgrade": bladeProcessorUpgrade,
       "bladeProcessorSerialNo": bladeProcessorSerialNo,
       "bladeProcessorAssetTag": bladeProcessorAssetTag,
       "bladeProcessorPartNo": bladeProcessorPartNo,
       "bladeMemorySummaryTable": bladeMemorySummaryTable,
       "bladeMemorySummaryEntry": bladeMemorySummaryEntry,
       "bladeMSMaxDevices": bladeMSMaxDevices,
       "bladeMSNumOfDevices": bladeMSNumOfDevices,
       "bladeMSCapacity": bladeMSCapacity,
       "bladeMSTotalSize": bladeMSTotalSize,
       "bladeMSEffectiveSize": bladeMSEffectiveSize,
       "bladeMSNumFailed": bladeMSNumFailed,
       "bladeMSDisabledSize": bladeMSDisabledSize,
       "bladeMSSpareSize": bladeMSSpareSize,
       "bladeMSRasPossible": bladeMSRasPossible,
       "bladeMSRasConfiguration": bladeMSRasConfiguration,
       "bladeMSErrorCorrection": bladeMSErrorCorrection,
       "bladeMemoryTable": bladeMemoryTable,
       "bladeMemoryEntry": bladeMemoryEntry,
       "bladeMemTotalWidth": bladeMemTotalWidth,
       "bladeMemDataWidth": bladeMemDataWidth,
       "bladeMemSize": bladeMemSize,
       "bladeMemGranularity": bladeMemGranularity,
       "bladeMemFormFactor": bladeMemFormFactor,
       "bladeMemDeviceSet": bladeMemDeviceSet,
       "bladeMemLocation": bladeMemLocation,
       "bladeMemBank": bladeMemBank,
       "bladeMemType": bladeMemType,
       "bladeMemTypeDetail": bladeMemTypeDetail,
       "bladeMemSpeed": bladeMemSpeed,
       "bladeMemManufacturer": bladeMemManufacturer,
       "bladeMemSerialNo": bladeMemSerialNo,
       "bladeMemAssetTag": bladeMemAssetTag,
       "bladeMemPart": bladeMemPart}
)
