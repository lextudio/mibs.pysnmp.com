# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:06 2024
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
 IdromBinary16,
 Index,
 Power,
 PowerLedStates,
 Presence,
 PresenceLedStates) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    "FaultLedStates",
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

multiFlexServerCmmMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 11)
)
multiFlexServerCmmMibModule.setRevisions(
        ("2007-08-16 13:30",
         "2007-07-11 12:30",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-29 20:00",
         "2007-05-09 11:30",
         "2007-04-09 10:30",
         "2007-03-12 18:00",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2006-11-07 07:01",
         "2006-09-29 15:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MaxCmms_Type = Unsigned32
_MaxCmms_Object = MibScalar
maxCmms = _MaxCmms_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 11),
    _MaxCmms_Type()
)
maxCmms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxCmms.setStatus("current")
_NumOfCmms_Type = Integer32
_NumOfCmms_Object = MibScalar
numOfCmms = _NumOfCmms_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 21),
    _NumOfCmms_Type()
)
numOfCmms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfCmms.setStatus("current")
_CmmPresenceMask_Type = DisplayString
_CmmPresenceMask_Object = MibScalar
cmmPresenceMask = _CmmPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 31),
    _CmmPresenceMask_Type()
)
cmmPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPresenceMask.setStatus("current")
_Cmms_ObjectIdentity = ObjectIdentity
cmms = _Cmms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201)
)
if mibBuilder.loadTexts:
    cmms.setStatus("current")
_FirmwareBundleId_Type = DisplayString
_FirmwareBundleId_Object = MibScalar
firmwareBundleId = _FirmwareBundleId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 1),
    _FirmwareBundleId_Type()
)
firmwareBundleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareBundleId.setStatus("current")
_CmmTable_Object = MibTable
cmmTable = _CmmTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2)
)
if mibBuilder.loadTexts:
    cmmTable.setStatus("current")
_CmmEntry_Object = MibTableRow
cmmEntry = _CmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1)
)
cmmEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmIndex"),
)
if mibBuilder.loadTexts:
    cmmEntry.setStatus("current")
_CmmIndex_Type = Index
_CmmIndex_Object = MibTableColumn
cmmIndex = _CmmIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 1),
    _CmmIndex_Type()
)
cmmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmIndex.setStatus("current")
_CmmPresence_Type = Presence
_CmmPresence_Object = MibTableColumn
cmmPresence = _CmmPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 2),
    _CmmPresence_Type()
)
cmmPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPresence.setStatus("current")
_CmmVendor_Type = DisplayString
_CmmVendor_Object = MibTableColumn
cmmVendor = _CmmVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 3),
    _CmmVendor_Type()
)
cmmVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmVendor.setStatus("current")
_CmmMfgDate_Type = DisplayString
_CmmMfgDate_Object = MibTableColumn
cmmMfgDate = _CmmMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 4),
    _CmmMfgDate_Type()
)
cmmMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmMfgDate.setStatus("current")
_CmmDeviceName_Type = DisplayString
_CmmDeviceName_Object = MibTableColumn
cmmDeviceName = _CmmDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 5),
    _CmmDeviceName_Type()
)
cmmDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmDeviceName.setStatus("current")
_CmmPart_Type = IdromBinary16
_CmmPart_Object = MibTableColumn
cmmPart = _CmmPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 6),
    _CmmPart_Type()
)
cmmPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPart.setStatus("current")
_CmmSerialNo_Type = IdromBinary16
_CmmSerialNo_Object = MibTableColumn
cmmSerialNo = _CmmSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 7),
    _CmmSerialNo_Type()
)
cmmSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmSerialNo.setStatus("current")
_CmmMaximumPower_Type = Power
_CmmMaximumPower_Object = MibTableColumn
cmmMaximumPower = _CmmMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 8),
    _CmmMaximumPower_Type()
)
cmmMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmMaximumPower.setStatus("current")
_CmmNominalPower_Type = Power
_CmmNominalPower_Object = MibTableColumn
cmmNominalPower = _CmmNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 9),
    _CmmNominalPower_Type()
)
cmmNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmNominalPower.setStatus("current")
_CmmAssetTag_Type = IdromBinary16
_CmmAssetTag_Object = MibTableColumn
cmmAssetTag = _CmmAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 10),
    _CmmAssetTag_Type()
)
cmmAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmAssetTag.setStatus("current")
_CmmExternalMac_Type = PhysAddress
_CmmExternalMac_Object = MibTableColumn
cmmExternalMac = _CmmExternalMac_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 11),
    _CmmExternalMac_Type()
)
cmmExternalMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmExternalMac.setStatus("current")
_CmmChassisMac_Type = PhysAddress
_CmmChassisMac_Object = MibTableColumn
cmmChassisMac = _CmmChassisMac_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 12),
    _CmmChassisMac_Type()
)
cmmChassisMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmChassisMac.setStatus("current")
_CmmPowerLed_Type = PowerLedStates
_CmmPowerLed_Object = MibTableColumn
cmmPowerLed = _CmmPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 13),
    _CmmPowerLed_Type()
)
cmmPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmPowerLed.setStatus("current")
_CmmFaultLed_Type = FaultLedStates
_CmmFaultLed_Object = MibTableColumn
cmmFaultLed = _CmmFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 14),
    _CmmFaultLed_Type()
)
cmmFaultLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmFaultLed.setStatus("current")
_CmmPresenceLed_Type = PresenceLedStates
_CmmPresenceLed_Object = MibTableColumn
cmmPresenceLed = _CmmPresenceLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 15),
    _CmmPresenceLed_Type()
)
cmmPresenceLed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cmmPresenceLed.setStatus("current")
_CmmEbfFirmwareVersion_Type = DisplayString
_CmmEbfFirmwareVersion_Object = MibTableColumn
cmmEbfFirmwareVersion = _CmmEbfFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 201, 2, 1, 16),
    _CmmEbfFirmwareVersion_Type()
)
cmmEbfFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmmEbfFirmwareVersion.setStatus("current")

# Managed Objects groups

cmmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 11)
)
cmmGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "maxCmms"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "numOfCmms"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "firmwareBundleId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmExternalMac"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmChassisMac"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPowerLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmFaultLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmPresenceLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB", "cmmEbfFirmwareVersion"))
)
if mibBuilder.loadTexts:
    cmmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-CMM-MIB",
    **{"multiFlexServerCmmMibModule": multiFlexServerCmmMibModule,
       "cmmGroup": cmmGroup,
       "maxCmms": maxCmms,
       "numOfCmms": numOfCmms,
       "cmmPresenceMask": cmmPresenceMask,
       "cmms": cmms,
       "firmwareBundleId": firmwareBundleId,
       "cmmTable": cmmTable,
       "cmmEntry": cmmEntry,
       "cmmIndex": cmmIndex,
       "cmmPresence": cmmPresence,
       "cmmVendor": cmmVendor,
       "cmmMfgDate": cmmMfgDate,
       "cmmDeviceName": cmmDeviceName,
       "cmmPart": cmmPart,
       "cmmSerialNo": cmmSerialNo,
       "cmmMaximumPower": cmmMaximumPower,
       "cmmNominalPower": cmmNominalPower,
       "cmmAssetTag": cmmAssetTag,
       "cmmExternalMac": cmmExternalMac,
       "cmmChassisMac": cmmChassisMac,
       "cmmPowerLed": cmmPowerLed,
       "cmmFaultLed": cmmFaultLed,
       "cmmPresenceLed": cmmPresenceLed,
       "cmmEbfFirmwareVersion": cmmEbfFirmwareVersion}
)
