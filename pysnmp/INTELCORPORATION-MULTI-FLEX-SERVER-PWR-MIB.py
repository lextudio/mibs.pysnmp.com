# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:09 2024
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

multiFlexServerPwrMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 17)
)
multiFlexServerPwrMibModule.setRevisions(
        ("2007-08-16 13:30",
         "2007-07-20 15:30",
         "2007-06-19 11:30",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-30 19:00",
         "2007-05-22 14:00",
         "2007-04-27 16:00",
         "2007-04-25 14:00",
         "2007-04-18 19:05",
         "2007-04-09 10:30",
         "2007-04-02 11:00",
         "2007-03-13 10:30",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2006-11-07 07:01",
         "2006-09-29 15:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MaxPwrSupplies_Type = Unsigned32
_MaxPwrSupplies_Object = MibScalar
maxPwrSupplies = _MaxPwrSupplies_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 17),
    _MaxPwrSupplies_Type()
)
maxPwrSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxPwrSupplies.setStatus("current")
_NumOfPwrSupplies_Type = Integer32
_NumOfPwrSupplies_Object = MibScalar
numOfPwrSupplies = _NumOfPwrSupplies_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 27),
    _NumOfPwrSupplies_Type()
)
numOfPwrSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfPwrSupplies.setStatus("current")
_NumOfPwrBlanks_Type = Integer32
_NumOfPwrBlanks_Object = MibScalar
numOfPwrBlanks = _NumOfPwrBlanks_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 28),
    _NumOfPwrBlanks_Type()
)
numOfPwrBlanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfPwrBlanks.setStatus("current")
_NumOfPwrUnknowns_Type = Integer32
_NumOfPwrUnknowns_Object = MibScalar
numOfPwrUnknowns = _NumOfPwrUnknowns_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 29),
    _NumOfPwrUnknowns_Type()
)
numOfPwrUnknowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfPwrUnknowns.setStatus("current")
_PwrSupplyPresenceMask_Type = DisplayString
_PwrSupplyPresenceMask_Object = MibScalar
pwrSupplyPresenceMask = _PwrSupplyPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 37),
    _PwrSupplyPresenceMask_Type()
)
pwrSupplyPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyPresenceMask.setStatus("current")
_PwrSupplyBlankPresenceMask_Type = DisplayString
_PwrSupplyBlankPresenceMask_Object = MibScalar
pwrSupplyBlankPresenceMask = _PwrSupplyBlankPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 38),
    _PwrSupplyBlankPresenceMask_Type()
)
pwrSupplyBlankPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyBlankPresenceMask.setStatus("current")
_PwrSupplyUnknownPresenceMask_Type = DisplayString
_PwrSupplyUnknownPresenceMask_Object = MibScalar
pwrSupplyUnknownPresenceMask = _PwrSupplyUnknownPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 39),
    _PwrSupplyUnknownPresenceMask_Type()
)
pwrSupplyUnknownPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyUnknownPresenceMask.setStatus("current")
_PwrSupplies_ObjectIdentity = ObjectIdentity
pwrSupplies = _PwrSupplies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207)
)
if mibBuilder.loadTexts:
    pwrSupplies.setStatus("current")
_PwrSupplyTable_Object = MibTable
pwrSupplyTable = _PwrSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1)
)
if mibBuilder.loadTexts:
    pwrSupplyTable.setStatus("current")
_PwrSupplyEntry_Object = MibTableRow
pwrSupplyEntry = _PwrSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1)
)
pwrSupplyEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyIndex"),
)
if mibBuilder.loadTexts:
    pwrSupplyEntry.setStatus("current")
_PwrSupplyIndex_Type = Index
_PwrSupplyIndex_Object = MibTableColumn
pwrSupplyIndex = _PwrSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 1),
    _PwrSupplyIndex_Type()
)
pwrSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyIndex.setStatus("current")
_PwrSupplyPresence_Type = Presence
_PwrSupplyPresence_Object = MibTableColumn
pwrSupplyPresence = _PwrSupplyPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 2),
    _PwrSupplyPresence_Type()
)
pwrSupplyPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyPresence.setStatus("current")
_PwrSupplyVendor_Type = DisplayString
_PwrSupplyVendor_Object = MibTableColumn
pwrSupplyVendor = _PwrSupplyVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 3),
    _PwrSupplyVendor_Type()
)
pwrSupplyVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyVendor.setStatus("current")
_PwrSupplyMfgDate_Type = DisplayString
_PwrSupplyMfgDate_Object = MibTableColumn
pwrSupplyMfgDate = _PwrSupplyMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 4),
    _PwrSupplyMfgDate_Type()
)
pwrSupplyMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyMfgDate.setStatus("current")
_PwrSupplyDeviceName_Type = DisplayString
_PwrSupplyDeviceName_Object = MibTableColumn
pwrSupplyDeviceName = _PwrSupplyDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 5),
    _PwrSupplyDeviceName_Type()
)
pwrSupplyDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyDeviceName.setStatus("current")
_PwrSupplyPart_Type = IdromBinary16
_PwrSupplyPart_Object = MibTableColumn
pwrSupplyPart = _PwrSupplyPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 6),
    _PwrSupplyPart_Type()
)
pwrSupplyPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyPart.setStatus("current")
_PwrSupplySerialNo_Type = IdromBinary16
_PwrSupplySerialNo_Object = MibTableColumn
pwrSupplySerialNo = _PwrSupplySerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 7),
    _PwrSupplySerialNo_Type()
)
pwrSupplySerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplySerialNo.setStatus("current")
_PwrSupplyMaximumPower_Type = Power
_PwrSupplyMaximumPower_Object = MibTableColumn
pwrSupplyMaximumPower = _PwrSupplyMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 8),
    _PwrSupplyMaximumPower_Type()
)
pwrSupplyMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyMaximumPower.setStatus("current")
_PwrSupplyNominalPower_Type = Power
_PwrSupplyNominalPower_Object = MibTableColumn
pwrSupplyNominalPower = _PwrSupplyNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 9),
    _PwrSupplyNominalPower_Type()
)
pwrSupplyNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyNominalPower.setStatus("current")
_PwrSupplyAssetTag_Type = IdromBinary16
_PwrSupplyAssetTag_Object = MibTableColumn
pwrSupplyAssetTag = _PwrSupplyAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 10),
    _PwrSupplyAssetTag_Type()
)
pwrSupplyAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyAssetTag.setStatus("current")
_PwrSupplyPowerLed_Type = PowerLedStates
_PwrSupplyPowerLed_Object = MibTableColumn
pwrSupplyPowerLed = _PwrSupplyPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 11),
    _PwrSupplyPowerLed_Type()
)
pwrSupplyPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyPowerLed.setStatus("current")
_PwrSupplyFaultLed_Type = FaultLedStates
_PwrSupplyFaultLed_Object = MibTableColumn
pwrSupplyFaultLed = _PwrSupplyFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 12),
    _PwrSupplyFaultLed_Type()
)
pwrSupplyFaultLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyFaultLed.setStatus("current")
_PwrSupplyOpCodeVersion_Type = DisplayString
_PwrSupplyOpCodeVersion_Object = MibTableColumn
pwrSupplyOpCodeVersion = _PwrSupplyOpCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 13),
    _PwrSupplyOpCodeVersion_Type()
)
pwrSupplyOpCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyOpCodeVersion.setStatus("current")
_PwrSupplyBootBlockVersion_Type = DisplayString
_PwrSupplyBootBlockVersion_Object = MibTableColumn
pwrSupplyBootBlockVersion = _PwrSupplyBootBlockVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 14),
    _PwrSupplyBootBlockVersion_Type()
)
pwrSupplyBootBlockVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyBootBlockVersion.setStatus("current")


class _PwrSupplyType_Type(Integer32):
    """Custom type pwrSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("powerSupplyBank", 2),
          ("powerSuppy", 1),
          ("unknown", -16))
    )


_PwrSupplyType_Type.__name__ = "Integer32"
_PwrSupplyType_Object = MibTableColumn
pwrSupplyType = _PwrSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 15),
    _PwrSupplyType_Type()
)
pwrSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyType.setStatus("current")
_PwrSupplyNumOfFans_Type = INT32withException
_PwrSupplyNumOfFans_Object = MibTableColumn
pwrSupplyNumOfFans = _PwrSupplyNumOfFans_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 16),
    _PwrSupplyNumOfFans_Type()
)
pwrSupplyNumOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyNumOfFans.setStatus("current")
_PwrSupplyInletTemperature_Type = INT32withException
_PwrSupplyInletTemperature_Object = MibTableColumn
pwrSupplyInletTemperature = _PwrSupplyInletTemperature_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 17),
    _PwrSupplyInletTemperature_Type()
)
pwrSupplyInletTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyInletTemperature.setStatus("current")
_PwrSupplyOutputVdc_Type = INT32withException
_PwrSupplyOutputVdc_Object = MibTableColumn
pwrSupplyOutputVdc = _PwrSupplyOutputVdc_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 18),
    _PwrSupplyOutputVdc_Type()
)
pwrSupplyOutputVdc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyOutputVdc.setStatus("current")
_PwrSupplyOutputAmp_Type = INT32withException
_PwrSupplyOutputAmp_Object = MibTableColumn
pwrSupplyOutputAmp = _PwrSupplyOutputAmp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 19),
    _PwrSupplyOutputAmp_Type()
)
pwrSupplyOutputAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyOutputAmp.setStatus("current")
_PwrSupplyOutputPickAmp_Type = INT32withException
_PwrSupplyOutputPickAmp_Object = MibTableColumn
pwrSupplyOutputPickAmp = _PwrSupplyOutputPickAmp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 20),
    _PwrSupplyOutputPickAmp_Type()
)
pwrSupplyOutputPickAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyOutputPickAmp.setStatus("current")
_PwrSupplyHotspotTemp_Type = INT32withException
_PwrSupplyHotspotTemp_Object = MibTableColumn
pwrSupplyHotspotTemp = _PwrSupplyHotspotTemp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 21),
    _PwrSupplyHotspotTemp_Type()
)
pwrSupplyHotspotTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyHotspotTemp.setStatus("current")
_PwrSupplyEmbTemp_Type = INT32withException
_PwrSupplyEmbTemp_Object = MibTableColumn
pwrSupplyEmbTemp = _PwrSupplyEmbTemp_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 22),
    _PwrSupplyEmbTemp_Type()
)
pwrSupplyEmbTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyEmbTemp.setStatus("current")


class _PwrSupplyStatus_Type(Bits):
    """Custom type pwrSupplyStatus based on Bits"""
    namedValues = NamedValues(
        *(("overCurrent", 6),
          ("overTemp", 5),
          ("powerOK", 3),
          ("powerSupplyOn", 2),
          ("supplyFault", 7),
          ("unused", 4),
          ("unused1", 0),
          ("unused2", 1))
    )

_PwrSupplyStatus_Type.__name__ = "Bits"
_PwrSupplyStatus_Object = MibTableColumn
pwrSupplyStatus = _PwrSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 1, 1, 23),
    _PwrSupplyStatus_Type()
)
pwrSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyStatus.setStatus("current")
_PwrSupplyFanTable_Object = MibTable
pwrSupplyFanTable = _PwrSupplyFanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2)
)
if mibBuilder.loadTexts:
    pwrSupplyFanTable.setStatus("current")
_PwrSupplyFanEntry_Object = MibTableRow
pwrSupplyFanEntry = _PwrSupplyFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1)
)
pwrSupplyFanEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanIndex"),
)
if mibBuilder.loadTexts:
    pwrSupplyFanEntry.setStatus("current")
_PwrSupplyFanIndex_Type = Index
_PwrSupplyFanIndex_Object = MibTableColumn
pwrSupplyFanIndex = _PwrSupplyFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 1),
    _PwrSupplyFanIndex_Type()
)
pwrSupplyFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyFanIndex.setStatus("current")
_PwrSupplyFanRpmMinimum_Type = Integer32
_PwrSupplyFanRpmMinimum_Object = MibTableColumn
pwrSupplyFanRpmMinimum = _PwrSupplyFanRpmMinimum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 2),
    _PwrSupplyFanRpmMinimum_Type()
)
pwrSupplyFanRpmMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyFanRpmMinimum.setStatus("current")
_PwrSupplyFanRpmMaximum_Type = Integer32
_PwrSupplyFanRpmMaximum_Object = MibTableColumn
pwrSupplyFanRpmMaximum = _PwrSupplyFanRpmMaximum_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 3),
    _PwrSupplyFanRpmMaximum_Type()
)
pwrSupplyFanRpmMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyFanRpmMaximum.setStatus("current")


class _PwrSupplyFanRpmReading_Type(Integer32):
    """Custom type pwrSupplyFanRpmReading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-32,
              -16,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", -32),
          ("notspinning", 0),
          ("unknown", -16))
    )


_PwrSupplyFanRpmReading_Type.__name__ = "Integer32"
_PwrSupplyFanRpmReading_Object = MibTableColumn
pwrSupplyFanRpmReading = _PwrSupplyFanRpmReading_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 207, 2, 1, 4),
    _PwrSupplyFanRpmReading_Type()
)
pwrSupplyFanRpmReading.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pwrSupplyFanRpmReading.setStatus("current")

# Managed Objects groups

pwrSupplyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 17)
)
pwrSupplyGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "maxPwrSupplies"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "numOfPwrSupplies"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "numOfPwrBlanks"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "numOfPwrUnknowns"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyBlankPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyUnknownPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplySerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPowerLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFaultLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOpCodeVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyBootBlockVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyNumOfFans"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyInletTemperature"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOutputVdc"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOutputAmp"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyOutputPickAmp"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyHotspotTemp"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyEmbTemp"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanRpmMinimum"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanRpmMaximum"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB", "pwrSupplyFanRpmReading"))
)
if mibBuilder.loadTexts:
    pwrSupplyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-PWR-MIB",
    **{"multiFlexServerPwrMibModule": multiFlexServerPwrMibModule,
       "pwrSupplyGroup": pwrSupplyGroup,
       "maxPwrSupplies": maxPwrSupplies,
       "numOfPwrSupplies": numOfPwrSupplies,
       "numOfPwrBlanks": numOfPwrBlanks,
       "numOfPwrUnknowns": numOfPwrUnknowns,
       "pwrSupplyPresenceMask": pwrSupplyPresenceMask,
       "pwrSupplyBlankPresenceMask": pwrSupplyBlankPresenceMask,
       "pwrSupplyUnknownPresenceMask": pwrSupplyUnknownPresenceMask,
       "pwrSupplies": pwrSupplies,
       "pwrSupplyTable": pwrSupplyTable,
       "pwrSupplyEntry": pwrSupplyEntry,
       "pwrSupplyIndex": pwrSupplyIndex,
       "pwrSupplyPresence": pwrSupplyPresence,
       "pwrSupplyVendor": pwrSupplyVendor,
       "pwrSupplyMfgDate": pwrSupplyMfgDate,
       "pwrSupplyDeviceName": pwrSupplyDeviceName,
       "pwrSupplyPart": pwrSupplyPart,
       "pwrSupplySerialNo": pwrSupplySerialNo,
       "pwrSupplyMaximumPower": pwrSupplyMaximumPower,
       "pwrSupplyNominalPower": pwrSupplyNominalPower,
       "pwrSupplyAssetTag": pwrSupplyAssetTag,
       "pwrSupplyPowerLed": pwrSupplyPowerLed,
       "pwrSupplyFaultLed": pwrSupplyFaultLed,
       "pwrSupplyOpCodeVersion": pwrSupplyOpCodeVersion,
       "pwrSupplyBootBlockVersion": pwrSupplyBootBlockVersion,
       "pwrSupplyType": pwrSupplyType,
       "pwrSupplyNumOfFans": pwrSupplyNumOfFans,
       "pwrSupplyInletTemperature": pwrSupplyInletTemperature,
       "pwrSupplyOutputVdc": pwrSupplyOutputVdc,
       "pwrSupplyOutputAmp": pwrSupplyOutputAmp,
       "pwrSupplyOutputPickAmp": pwrSupplyOutputPickAmp,
       "pwrSupplyHotspotTemp": pwrSupplyHotspotTemp,
       "pwrSupplyEmbTemp": pwrSupplyEmbTemp,
       "pwrSupplyStatus": pwrSupplyStatus,
       "pwrSupplyFanTable": pwrSupplyFanTable,
       "pwrSupplyFanEntry": pwrSupplyFanEntry,
       "pwrSupplyFanIndex": pwrSupplyFanIndex,
       "pwrSupplyFanRpmMinimum": pwrSupplyFanRpmMinimum,
       "pwrSupplyFanRpmMaximum": pwrSupplyFanRpmMaximum,
       "pwrSupplyFanRpmReading": pwrSupplyFanRpmReading}
)
