# SNMP MIB module (NLS-BBNIDENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NLS-BBNIDENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:30 2024
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


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Gi_ObjectIdentity = ObjectIdentity
gi = _Gi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166)
)
_Giproducts_ObjectIdentity = ObjectIdentity
giproducts = _Giproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1)
)
_Acc4000d_ObjectIdentity = ObjectIdentity
acc4000d = _Acc4000d_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 1)
)
_Anicd_ObjectIdentity = ObjectIdentity
anicd = _Anicd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 2)
)
_Item1000_ObjectIdentity = ObjectIdentity
item1000 = _Item1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 4)
)
_Irt1000_ObjectIdentity = ObjectIdentity
irt1000 = _Irt1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 5)
)
_Nc1500_ObjectIdentity = ObjectIdentity
nc1500 = _Nc1500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 6)
)
_Om1000_ObjectIdentity = ObjectIdentity
om1000 = _Om1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 7)
)
_Im1000_ObjectIdentity = ObjectIdentity
im1000 = _Im1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 8)
)
_Mps_ObjectIdentity = ObjectIdentity
mps = _Mps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 9)
)
_Rpd1000_ObjectIdentity = ObjectIdentity
rpd1000 = _Rpd1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 10)
)
_AcpStatus_ObjectIdentity = ObjectIdentity
acpStatus = _AcpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 11)
)
_SurfBbnh_ObjectIdentity = ObjectIdentity
surfBbnh = _SurfBbnh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 18)
)
_Sb2100_ObjectIdentity = ObjectIdentity
sb2100 = _Sb2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 19)
)
_Sb2100D_ObjectIdentity = ObjectIdentity
sb2100D = _Sb2100D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 20)
)
_Sb2000_ObjectIdentity = ObjectIdentity
sb2000 = _Sb2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 21)
)
_SaDANIS_ObjectIdentity = ObjectIdentity
saDANIS = _SaDANIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 30)
)
_Hdd2000_ObjectIdentity = ObjectIdentity
hdd2000 = _Hdd2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 40)
)
_Merlin_ObjectIdentity = ObjectIdentity
merlin = _Merlin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 50)
)
_NetSentry_ObjectIdentity = ObjectIdentity
netSentry = _NetSentry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 99)
)
_Bti_ObjectIdentity = ObjectIdentity
bti = _Bti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 200)
)
_RfModMIB_ObjectIdentity = ObjectIdentity
rfModMIB = _RfModMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 201)
)
_BtiIntMIB_ObjectIdentity = ObjectIdentity
btiIntMIB = _BtiIntMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 202)
)
_Dct5000_ObjectIdentity = ObjectIdentity
dct5000 = _Dct5000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 300)
)
_MotoIPNSprodID_ObjectIdentity = ObjectIdentity
motoIPNSprodID = _MotoIPNSprodID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 1, 450)
)
_Giproxies_ObjectIdentity = ObjectIdentity
giproxies = _Giproxies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 3)
)
_Gicommon_ObjectIdentity = ObjectIdentity
gicommon = _Gicommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4)
)
_Identity_ObjectIdentity = ObjectIdentity
identity = _Identity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 1)
)
_State_ObjectIdentity = ObjectIdentity
state = _State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 2)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 3)
)
_Logs_ObjectIdentity = ObjectIdentity
logs = _Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 4, 4)
)
_Nlsbbn_ObjectIdentity = ObjectIdentity
nlsbbn = _Nlsbbn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5)
)
_BbnIdent_ObjectIdentity = ObjectIdentity
bbnIdent = _BbnIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1)
)
_IdentSerialNumber_Type = DisplayString
_IdentSerialNumber_Object = MibScalar
identSerialNumber = _IdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 1),
    _IdentSerialNumber_Type()
)
identSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identSerialNumber.setStatus("mandatory")
_IdentChassisNumber_Type = DisplayString
_IdentChassisNumber_Object = MibScalar
identChassisNumber = _IdentChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 2),
    _IdentChassisNumber_Type()
)
identChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identChassisNumber.setStatus("mandatory")
_IdentIfIndex_Type = Integer32
_IdentIfIndex_Object = MibScalar
identIfIndex = _IdentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 3),
    _IdentIfIndex_Type()
)
identIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfIndex.setStatus("mandatory")
_IdentHardwareVersion_Type = DisplayString
_IdentHardwareVersion_Object = MibScalar
identHardwareVersion = _IdentHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 4),
    _IdentHardwareVersion_Type()
)
identHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identHardwareVersion.setStatus("mandatory")
_IdentHardwareFeatures_Type = DisplayString
_IdentHardwareFeatures_Object = MibScalar
identHardwareFeatures = _IdentHardwareFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 5),
    _IdentHardwareFeatures_Type()
)
identHardwareFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identHardwareFeatures.setStatus("mandatory")
_IdentInventoryCode_Type = DisplayString
_IdentInventoryCode_Object = MibScalar
identInventoryCode = _IdentInventoryCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 6),
    _IdentInventoryCode_Type()
)
identInventoryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identInventoryCode.setStatus("mandatory")
_IdentSoftwareVersion_Type = DisplayString
_IdentSoftwareVersion_Object = MibScalar
identSoftwareVersion = _IdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 7),
    _IdentSoftwareVersion_Type()
)
identSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identSoftwareVersion.setStatus("mandatory")
_IdentLocationArea_Type = DisplayString
_IdentLocationArea_Object = MibScalar
identLocationArea = _IdentLocationArea_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 8),
    _IdentLocationArea_Type()
)
identLocationArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identLocationArea.setStatus("mandatory")
_IdentLocationRack_Type = DisplayString
_IdentLocationRack_Object = MibScalar
identLocationRack = _IdentLocationRack_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 9),
    _IdentLocationRack_Type()
)
identLocationRack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identLocationRack.setStatus("mandatory")
_IdentLocationShelf_Type = DisplayString
_IdentLocationShelf_Object = MibScalar
identLocationShelf = _IdentLocationShelf_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 10),
    _IdentLocationShelf_Type()
)
identLocationShelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identLocationShelf.setStatus("mandatory")
_IdentMIBVersion_Type = DisplayString
_IdentMIBVersion_Object = MibScalar
identMIBVersion = _IdentMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 11),
    _IdentMIBVersion_Type()
)
identMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identMIBVersion.setStatus("mandatory")
_IdentAgentVersion_Type = DisplayString
_IdentAgentVersion_Object = MibScalar
identAgentVersion = _IdentAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 12),
    _IdentAgentVersion_Type()
)
identAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identAgentVersion.setStatus("mandatory")


class _IdentCommand_Type(Integer32):
    """Custom type identCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("currentlyRestarting", 2),
          ("restart", 1),
          ("unspecified", 3))
    )


_IdentCommand_Type.__name__ = "Integer32"
_IdentCommand_Object = MibScalar
identCommand = _IdentCommand_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 13),
    _IdentCommand_Type()
)
identCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identCommand.setStatus("mandatory")
_IdentIfExtensionTable_Object = MibTable
identIfExtensionTable = _IdentIfExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14)
)
if mibBuilder.loadTexts:
    identIfExtensionTable.setStatus("mandatory")
_IdentIfExtensionEntry_Object = MibTableRow
identIfExtensionEntry = _IdentIfExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1)
)
identIfExtensionEntry.setIndexNames(
    (0, "NLS-BBNIDENT-MIB", "identIfExtensionIndex"),
)
if mibBuilder.loadTexts:
    identIfExtensionEntry.setStatus("mandatory")
_IdentIfExtensionIndex_Type = Integer32
_IdentIfExtensionIndex_Object = MibTableColumn
identIfExtensionIndex = _IdentIfExtensionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 1),
    _IdentIfExtensionIndex_Type()
)
identIfExtensionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfExtensionIndex.setStatus("mandatory")
_IdentIfSerialNumber_Type = DisplayString
_IdentIfSerialNumber_Object = MibTableColumn
identIfSerialNumber = _IdentIfSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 2),
    _IdentIfSerialNumber_Type()
)
identIfSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfSerialNumber.setStatus("mandatory")
_IdentIfHardwareVersion_Type = DisplayString
_IdentIfHardwareVersion_Object = MibTableColumn
identIfHardwareVersion = _IdentIfHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 3),
    _IdentIfHardwareVersion_Type()
)
identIfHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfHardwareVersion.setStatus("mandatory")
_IdentIfHardwareFeatures_Type = DisplayString
_IdentIfHardwareFeatures_Object = MibTableColumn
identIfHardwareFeatures = _IdentIfHardwareFeatures_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 4),
    _IdentIfHardwareFeatures_Type()
)
identIfHardwareFeatures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfHardwareFeatures.setStatus("mandatory")
_IdentIfInventoryCode_Type = DisplayString
_IdentIfInventoryCode_Object = MibTableColumn
identIfInventoryCode = _IdentIfInventoryCode_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 5),
    _IdentIfInventoryCode_Type()
)
identIfInventoryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfInventoryCode.setStatus("mandatory")
_IdentIfFirmwareVersion1_Type = DisplayString
_IdentIfFirmwareVersion1_Object = MibTableColumn
identIfFirmwareVersion1 = _IdentIfFirmwareVersion1_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 6),
    _IdentIfFirmwareVersion1_Type()
)
identIfFirmwareVersion1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion1.setStatus("mandatory")
_IdentIfFirmwareVersion2_Type = DisplayString
_IdentIfFirmwareVersion2_Object = MibTableColumn
identIfFirmwareVersion2 = _IdentIfFirmwareVersion2_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 7),
    _IdentIfFirmwareVersion2_Type()
)
identIfFirmwareVersion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion2.setStatus("mandatory")
_IdentIfFirmwareVersion3_Type = DisplayString
_IdentIfFirmwareVersion3_Object = MibTableColumn
identIfFirmwareVersion3 = _IdentIfFirmwareVersion3_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 8),
    _IdentIfFirmwareVersion3_Type()
)
identIfFirmwareVersion3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion3.setStatus("mandatory")
_IdentIfFirmwareVersion4_Type = DisplayString
_IdentIfFirmwareVersion4_Object = MibTableColumn
identIfFirmwareVersion4 = _IdentIfFirmwareVersion4_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 9),
    _IdentIfFirmwareVersion4_Type()
)
identIfFirmwareVersion4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfFirmwareVersion4.setStatus("mandatory")
_IdentIfSlotId_Type = Integer32
_IdentIfSlotId_Object = MibTableColumn
identIfSlotId = _IdentIfSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 10),
    _IdentIfSlotId_Type()
)
identIfSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfSlotId.setStatus("mandatory")


class _IdentIfCommand_Type(Integer32):
    """Custom type identIfCommand based on Integer32"""
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
        *(("halt", 4),
          ("reset", 2),
          ("restart", 3),
          ("unspecified", 1))
    )


_IdentIfCommand_Type.__name__ = "Integer32"
_IdentIfCommand_Object = MibTableColumn
identIfCommand = _IdentIfCommand_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 11),
    _IdentIfCommand_Type()
)
identIfCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfCommand.setStatus("mandatory")


class _IdentIfAdministrativeState_Type(Integer32):
    """Custom type identIfAdministrativeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("shuttingDown", 3),
          ("unlocked", 2))
    )


_IdentIfAdministrativeState_Type.__name__ = "Integer32"
_IdentIfAdministrativeState_Object = MibTableColumn
identIfAdministrativeState = _IdentIfAdministrativeState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 12),
    _IdentIfAdministrativeState_Type()
)
identIfAdministrativeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfAdministrativeState.setStatus("mandatory")


class _IdentIfOperationalState_Type(Integer32):
    """Custom type identIfOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IdentIfOperationalState_Type.__name__ = "Integer32"
_IdentIfOperationalState_Object = MibTableColumn
identIfOperationalState = _IdentIfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 13),
    _IdentIfOperationalState_Type()
)
identIfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfOperationalState.setStatus("mandatory")


class _IdentIfAlarmStatus_Type(Integer32):
    """Custom type identIfAlarmStatus based on Integer32"""
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
        *(("alarmOutstanding", 5),
          ("critical", 2),
          ("idle", 6),
          ("major", 3),
          ("minor", 4),
          ("underRepair", 1))
    )


_IdentIfAlarmStatus_Type.__name__ = "Integer32"
_IdentIfAlarmStatus_Object = MibTableColumn
identIfAlarmStatus = _IdentIfAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 14),
    _IdentIfAlarmStatus_Type()
)
identIfAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfAlarmStatus.setStatus("mandatory")


class _IdentIfAvailabilityStatus_Type(Integer32):
    """Custom type identIfAvailabilityStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("available", 10),
          ("degraded", 7),
          ("dependency", 6),
          ("failed", 2),
          ("inTest", 1),
          ("logFull", 9),
          ("notInstalled", 8),
          ("offDuty", 5),
          ("offLine", 4),
          ("powerOff", 3))
    )


_IdentIfAvailabilityStatus_Type.__name__ = "Integer32"
_IdentIfAvailabilityStatus_Object = MibTableColumn
identIfAvailabilityStatus = _IdentIfAvailabilityStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 15),
    _IdentIfAvailabilityStatus_Type()
)
identIfAvailabilityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfAvailabilityStatus.setStatus("mandatory")
_IdentIfSpecific_Type = ObjectIdentifier
_IdentIfSpecific_Object = MibTableColumn
identIfSpecific = _IdentIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 16),
    _IdentIfSpecific_Type()
)
identIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identIfSpecific.setStatus("mandatory")


class _IdentIfEntryStatus_Type(EntryStatus):
    """Custom type identIfEntryStatus based on EntryStatus"""


_IdentIfEntryStatus_Object = MibTableColumn
identIfEntryStatus = _IdentIfEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 14, 1, 17),
    _IdentIfEntryStatus_Type()
)
identIfEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    identIfEntryStatus.setStatus("mandatory")
_IdentUnitModel_Type = DisplayString
_IdentUnitModel_Object = MibScalar
identUnitModel = _IdentUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 1166, 5, 1, 15),
    _IdentUnitModel_Type()
)
identUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    identUnitModel.setStatus("mandatory")
_BbnState_ObjectIdentity = ObjectIdentity
bbnState = _BbnState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5, 2)
)
_BbnTraps_ObjectIdentity = ObjectIdentity
bbnTraps = _BbnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5, 3)
)
_BbnLogs_ObjectIdentity = ObjectIdentity
bbnLogs = _BbnLogs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5, 4)
)
_Dns_ObjectIdentity = ObjectIdentity
dns = _Dns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 5, 5)
)
_Motproxies_ObjectIdentity = ObjectIdentity
motproxies = _Motproxies_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1166, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NLS-BBNIDENT-MIB",
    **{"EntryStatus": EntryStatus,
       "gi": gi,
       "giproducts": giproducts,
       "acc4000d": acc4000d,
       "anicd": anicd,
       "item1000": item1000,
       "irt1000": irt1000,
       "nc1500": nc1500,
       "om1000": om1000,
       "im1000": im1000,
       "mps": mps,
       "rpd1000": rpd1000,
       "acpStatus": acpStatus,
       "surfBbnh": surfBbnh,
       "sb2100": sb2100,
       "sb2100D": sb2100D,
       "sb2000": sb2000,
       "saDANIS": saDANIS,
       "hdd2000": hdd2000,
       "merlin": merlin,
       "netSentry": netSentry,
       "bti": bti,
       "rfModMIB": rfModMIB,
       "btiIntMIB": btiIntMIB,
       "dct5000": dct5000,
       "motoIPNSprodID": motoIPNSprodID,
       "giproxies": giproxies,
       "gicommon": gicommon,
       "identity": identity,
       "state": state,
       "traps": traps,
       "logs": logs,
       "nlsbbn": nlsbbn,
       "bbnIdent": bbnIdent,
       "identSerialNumber": identSerialNumber,
       "identChassisNumber": identChassisNumber,
       "identIfIndex": identIfIndex,
       "identHardwareVersion": identHardwareVersion,
       "identHardwareFeatures": identHardwareFeatures,
       "identInventoryCode": identInventoryCode,
       "identSoftwareVersion": identSoftwareVersion,
       "identLocationArea": identLocationArea,
       "identLocationRack": identLocationRack,
       "identLocationShelf": identLocationShelf,
       "identMIBVersion": identMIBVersion,
       "identAgentVersion": identAgentVersion,
       "identCommand": identCommand,
       "identIfExtensionTable": identIfExtensionTable,
       "identIfExtensionEntry": identIfExtensionEntry,
       "identIfExtensionIndex": identIfExtensionIndex,
       "identIfSerialNumber": identIfSerialNumber,
       "identIfHardwareVersion": identIfHardwareVersion,
       "identIfHardwareFeatures": identIfHardwareFeatures,
       "identIfInventoryCode": identIfInventoryCode,
       "identIfFirmwareVersion1": identIfFirmwareVersion1,
       "identIfFirmwareVersion2": identIfFirmwareVersion2,
       "identIfFirmwareVersion3": identIfFirmwareVersion3,
       "identIfFirmwareVersion4": identIfFirmwareVersion4,
       "identIfSlotId": identIfSlotId,
       "identIfCommand": identIfCommand,
       "identIfAdministrativeState": identIfAdministrativeState,
       "identIfOperationalState": identIfOperationalState,
       "identIfAlarmStatus": identIfAlarmStatus,
       "identIfAvailabilityStatus": identIfAvailabilityStatus,
       "identIfSpecific": identIfSpecific,
       "identIfEntryStatus": identIfEntryStatus,
       "identUnitModel": identUnitModel,
       "bbnState": bbnState,
       "bbnTraps": bbnTraps,
       "bbnLogs": bbnLogs,
       "dns": dns,
       "motproxies": motproxies}
)
