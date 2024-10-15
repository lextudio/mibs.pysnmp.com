# SNMP MIB module (INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:12 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 OwnerString) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "OwnerString")

(chassis,) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-MIB",
    "chassis")

(groups,
 regModule) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-REG",
    "groups",
    "regModule")

(EnabledStatus,
 FaultLedStates,
 IdromBinary16,
 Index,
 JackType,
 PortList,
 Power,
 PowerLedStates,
 Presence,
 PresenceLedStates,
 TimeFilter,
 VlanIndex) = mibBuilder.importSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-TC",
    "EnabledStatus",
    "FaultLedStates",
    "IdromBinary16",
    "Index",
    "JackType",
    "PortList",
    "Power",
    "PowerLedStates",
    "Presence",
    "PresenceLedStates",
    "TimeFilter",
    "VlanIndex")

(EntryStatus,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus")

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
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

multiFlexServerSwitchMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 1, 1, 13)
)
multiFlexServerSwitchMibModule.setRevisions(
        ("2007-08-15 19:00",
         "2007-06-18 20:30",
         "2007-06-07 20:30",
         "2007-06-07 13:30",
         "2007-05-21 15:00",
         "2007-04-18 19:05",
         "2007-03-27 12:30",
         "2007-03-06 10:30",
         "2007-02-22 17:00",
         "2007-02-07 19:00",
         "2006-12-27 12:30",
         "2006-11-07 11:27",
         "2006-10-02 06:29")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MaxSwitches_Type = Unsigned32
_MaxSwitches_Object = MibScalar
maxSwitches = _MaxSwitches_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 13),
    _MaxSwitches_Type()
)
maxSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxSwitches.setStatus("current")
_NumOfSwitches_Type = Integer32
_NumOfSwitches_Object = MibScalar
numOfSwitches = _NumOfSwitches_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 23),
    _NumOfSwitches_Type()
)
numOfSwitches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfSwitches.setStatus("current")
_SwitchPresenceMask_Type = DisplayString
_SwitchPresenceMask_Object = MibScalar
switchPresenceMask = _SwitchPresenceMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 33),
    _SwitchPresenceMask_Type()
)
switchPresenceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPresenceMask.setStatus("current")
_Switches_ObjectIdentity = ObjectIdentity
switches = _Switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203)
)
if mibBuilder.loadTexts:
    switches.setStatus("current")
_SwitchTable_Object = MibTable
switchTable = _SwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1)
)
if mibBuilder.loadTexts:
    switchTable.setStatus("current")
_SwitchEntry_Object = MibTableRow
switchEntry = _SwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1)
)
switchEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
)
if mibBuilder.loadTexts:
    switchEntry.setStatus("current")
_SwitchIndex_Type = Index
_SwitchIndex_Object = MibTableColumn
switchIndex = _SwitchIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 1),
    _SwitchIndex_Type()
)
switchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchIndex.setStatus("current")
_SwitchPresence_Type = Presence
_SwitchPresence_Object = MibTableColumn
switchPresence = _SwitchPresence_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 2),
    _SwitchPresence_Type()
)
switchPresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPresence.setStatus("current")
_SwitchVendor_Type = DisplayString
_SwitchVendor_Object = MibTableColumn
switchVendor = _SwitchVendor_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 3),
    _SwitchVendor_Type()
)
switchVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVendor.setStatus("current")
_SwitchMfgDate_Type = DisplayString
_SwitchMfgDate_Object = MibTableColumn
switchMfgDate = _SwitchMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 4),
    _SwitchMfgDate_Type()
)
switchMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchMfgDate.setStatus("current")
_SwitchDeviceName_Type = DisplayString
_SwitchDeviceName_Object = MibTableColumn
switchDeviceName = _SwitchDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 5),
    _SwitchDeviceName_Type()
)
switchDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDeviceName.setStatus("current")
_SwitchPart_Type = IdromBinary16
_SwitchPart_Object = MibTableColumn
switchPart = _SwitchPart_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 6),
    _SwitchPart_Type()
)
switchPart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPart.setStatus("current")
_SwitchSerialNo_Type = IdromBinary16
_SwitchSerialNo_Object = MibTableColumn
switchSerialNo = _SwitchSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 7),
    _SwitchSerialNo_Type()
)
switchSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchSerialNo.setStatus("current")
_SwitchMaximumPower_Type = Power
_SwitchMaximumPower_Object = MibTableColumn
switchMaximumPower = _SwitchMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 8),
    _SwitchMaximumPower_Type()
)
switchMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchMaximumPower.setStatus("current")
_SwitchNominalPower_Type = Power
_SwitchNominalPower_Object = MibTableColumn
switchNominalPower = _SwitchNominalPower_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 9),
    _SwitchNominalPower_Type()
)
switchNominalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNominalPower.setStatus("current")
_SwitchAssetTag_Type = IdromBinary16
_SwitchAssetTag_Object = MibTableColumn
switchAssetTag = _SwitchAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 10),
    _SwitchAssetTag_Type()
)
switchAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAssetTag.setStatus("current")
_SwitchFirmwareVersion_Type = DisplayString
_SwitchFirmwareVersion_Object = MibTableColumn
switchFirmwareVersion = _SwitchFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 11),
    _SwitchFirmwareVersion_Type()
)
switchFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFirmwareVersion.setStatus("current")
_SwitchVersion_Type = DisplayString
_SwitchVersion_Object = MibTableColumn
switchVersion = _SwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 12),
    _SwitchVersion_Type()
)
switchVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchVersion.setStatus("current")
_SwitchPowerLed_Type = PowerLedStates
_SwitchPowerLed_Object = MibTableColumn
switchPowerLed = _SwitchPowerLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 13),
    _SwitchPowerLed_Type()
)
switchPowerLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPowerLed.setStatus("current")
_SwitchFaultLed_Type = FaultLedStates
_SwitchFaultLed_Object = MibTableColumn
switchFaultLed = _SwitchFaultLed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 1, 1, 14),
    _SwitchFaultLed_Type()
)
switchFaultLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFaultLed.setStatus("current")
_SwitchPhyPortsTable_Object = MibTable
switchPhyPortsTable = _SwitchPhyPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2)
)
if mibBuilder.loadTexts:
    switchPhyPortsTable.setStatus("current")
_SwitchPhyPortsEntry_Object = MibTableRow
switchPhyPortsEntry = _SwitchPhyPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1)
)
switchPhyPortsEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsIfIndex"),
)
if mibBuilder.loadTexts:
    switchPhyPortsEntry.setStatus("current")


class _SwitchPhyPortsIfIndex_Type(Integer32):
    """Custom type switchPhyPortsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwitchPhyPortsIfIndex_Type.__name__ = "Integer32"
_SwitchPhyPortsIfIndex_Object = MibTableColumn
switchPhyPortsIfIndex = _SwitchPhyPortsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 1),
    _SwitchPhyPortsIfIndex_Type()
)
switchPhyPortsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortsIfIndex.setStatus("current")


class _SwitchPhyPortsIfIndexName_Type(DisplayString):
    """Custom type switchPhyPortsIfIndexName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SwitchPhyPortsIfIndexName_Type.__name__ = "DisplayString"
_SwitchPhyPortsIfIndexName_Object = MibTableColumn
switchPhyPortsIfIndexName = _SwitchPhyPortsIfIndexName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 2),
    _SwitchPhyPortsIfIndexName_Type()
)
switchPhyPortsIfIndexName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortsIfIndexName.setStatus("current")


class _SwitchPhyPortsMediaType_Type(Integer32):
    """Custom type switchPhyPortsMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("combo", 3),
          ("copper", 1),
          ("opticfiber", 2))
    )


_SwitchPhyPortsMediaType_Type.__name__ = "Integer32"
_SwitchPhyPortsMediaType_Object = MibTableColumn
switchPhyPortsMediaType = _SwitchPhyPortsMediaType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 3),
    _SwitchPhyPortsMediaType_Type()
)
switchPhyPortsMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortsMediaType.setStatus("current")
_SwitchPhyPortsStackUnit_Type = Integer32
_SwitchPhyPortsStackUnit_Object = MibTableColumn
switchPhyPortsStackUnit = _SwitchPhyPortsStackUnit_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 4),
    _SwitchPhyPortsStackUnit_Type()
)
switchPhyPortsStackUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortsStackUnit.setStatus("current")
_SwitchPhyPortsModuleNumber_Type = Integer32
_SwitchPhyPortsModuleNumber_Object = MibTableColumn
switchPhyPortsModuleNumber = _SwitchPhyPortsModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 5),
    _SwitchPhyPortsModuleNumber_Type()
)
switchPhyPortsModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortsModuleNumber.setStatus("current")
_SwitchPhyPortsRow_Type = Integer32
_SwitchPhyPortsRow_Object = MibTableColumn
switchPhyPortsRow = _SwitchPhyPortsRow_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 6),
    _SwitchPhyPortsRow_Type()
)
switchPhyPortsRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortsRow.setStatus("current")
_SwitchPhyPortsColumn_Type = Integer32
_SwitchPhyPortsColumn_Object = MibTableColumn
switchPhyPortsColumn = _SwitchPhyPortsColumn_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 7),
    _SwitchPhyPortsColumn_Type()
)
switchPhyPortsColumn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortsColumn.setStatus("current")
_SwitchPhyConnectorType_Type = JackType
_SwitchPhyConnectorType_Object = MibTableColumn
switchPhyConnectorType = _SwitchPhyConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 8),
    _SwitchPhyConnectorType_Type()
)
switchPhyConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyConnectorType.setStatus("current")


class _SwitchPhyPortHaul_Type(Integer32):
    """Custom type switchPhyPortHaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("long", 3),
          ("not-relevant", 1),
          ("short", 2))
    )


_SwitchPhyPortHaul_Type.__name__ = "Integer32"
_SwitchPhyPortHaul_Object = MibTableColumn
switchPhyPortHaul = _SwitchPhyPortHaul_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 2, 1, 9),
    _SwitchPhyPortHaul_Type()
)
switchPhyPortHaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchPhyPortHaul.setStatus("current")
_SwitchIfTable_Object = MibTable
switchIfTable = _SwitchIfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3)
)
if mibBuilder.loadTexts:
    switchIfTable.setStatus("current")
_SwitchIfEntry_Object = MibTableRow
switchIfEntry = _SwitchIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1)
)
switchIfEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfIndex"),
)
if mibBuilder.loadTexts:
    switchIfEntry.setStatus("current")
_SwitchIfIndex_Type = InterfaceIndex
_SwitchIfIndex_Object = MibTableColumn
switchIfIndex = _SwitchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 1),
    _SwitchIfIndex_Type()
)
switchIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfIndex.setStatus("current")


class _SwitchIfDescr_Type(DisplayString):
    """Custom type switchIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwitchIfDescr_Type.__name__ = "DisplayString"
_SwitchIfDescr_Object = MibTableColumn
switchIfDescr = _SwitchIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 2),
    _SwitchIfDescr_Type()
)
switchIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfDescr.setStatus("current")
_SwitchIfType_Type = IANAifType
_SwitchIfType_Object = MibTableColumn
switchIfType = _SwitchIfType_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 3),
    _SwitchIfType_Type()
)
switchIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfType.setStatus("current")
_SwitchIfMtu_Type = Integer32
_SwitchIfMtu_Object = MibTableColumn
switchIfMtu = _SwitchIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 4),
    _SwitchIfMtu_Type()
)
switchIfMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfMtu.setStatus("current")
_SwitchIfSpeed_Type = Gauge32
_SwitchIfSpeed_Object = MibTableColumn
switchIfSpeed = _SwitchIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 5),
    _SwitchIfSpeed_Type()
)
switchIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfSpeed.setStatus("current")
_SwitchIfPhysAddress_Type = PhysAddress
_SwitchIfPhysAddress_Object = MibTableColumn
switchIfPhysAddress = _SwitchIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 6),
    _SwitchIfPhysAddress_Type()
)
switchIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfPhysAddress.setStatus("current")


class _SwitchIfAdminStatus_Type(Integer32):
    """Custom type switchIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SwitchIfAdminStatus_Type.__name__ = "Integer32"
_SwitchIfAdminStatus_Object = MibTableColumn
switchIfAdminStatus = _SwitchIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 7),
    _SwitchIfAdminStatus_Type()
)
switchIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfAdminStatus.setStatus("current")


class _SwitchIfOperStatus_Type(Integer32):
    """Custom type switchIfOperStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 2),
          ("lowerLayerDown", 7),
          ("notPresent", 6),
          ("testing", 3),
          ("unknown", 4),
          ("up", 1))
    )


_SwitchIfOperStatus_Type.__name__ = "Integer32"
_SwitchIfOperStatus_Object = MibTableColumn
switchIfOperStatus = _SwitchIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 8),
    _SwitchIfOperStatus_Type()
)
switchIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOperStatus.setStatus("current")
_SwitchIfLastChange_Type = TimeTicks
_SwitchIfLastChange_Object = MibTableColumn
switchIfLastChange = _SwitchIfLastChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 9),
    _SwitchIfLastChange_Type()
)
switchIfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfLastChange.setStatus("current")
_SwitchIfInOctets_Type = Counter32
_SwitchIfInOctets_Object = MibTableColumn
switchIfInOctets = _SwitchIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 10),
    _SwitchIfInOctets_Type()
)
switchIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInOctets.setStatus("current")
_SwitchIfInUcastPkts_Type = Counter32
_SwitchIfInUcastPkts_Object = MibTableColumn
switchIfInUcastPkts = _SwitchIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 11),
    _SwitchIfInUcastPkts_Type()
)
switchIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInUcastPkts.setStatus("current")
_SwitchIfInNUcastPkts_Type = Counter32
_SwitchIfInNUcastPkts_Object = MibTableColumn
switchIfInNUcastPkts = _SwitchIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 12),
    _SwitchIfInNUcastPkts_Type()
)
switchIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInNUcastPkts.setStatus("deprecated")
_SwitchIfInDiscards_Type = Counter32
_SwitchIfInDiscards_Object = MibTableColumn
switchIfInDiscards = _SwitchIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 13),
    _SwitchIfInDiscards_Type()
)
switchIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInDiscards.setStatus("current")
_SwitchIfInErrors_Type = Counter32
_SwitchIfInErrors_Object = MibTableColumn
switchIfInErrors = _SwitchIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 14),
    _SwitchIfInErrors_Type()
)
switchIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInErrors.setStatus("current")
_SwitchIfInUnknownProtos_Type = Counter32
_SwitchIfInUnknownProtos_Object = MibTableColumn
switchIfInUnknownProtos = _SwitchIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 15),
    _SwitchIfInUnknownProtos_Type()
)
switchIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInUnknownProtos.setStatus("current")
_SwitchIfOutOctets_Type = Counter32
_SwitchIfOutOctets_Object = MibTableColumn
switchIfOutOctets = _SwitchIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 16),
    _SwitchIfOutOctets_Type()
)
switchIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutOctets.setStatus("current")
_SwitchIfOutUcastPkts_Type = Counter32
_SwitchIfOutUcastPkts_Object = MibTableColumn
switchIfOutUcastPkts = _SwitchIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 17),
    _SwitchIfOutUcastPkts_Type()
)
switchIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutUcastPkts.setStatus("current")
_SwitchIfOutNUcastPkts_Type = Counter32
_SwitchIfOutNUcastPkts_Object = MibTableColumn
switchIfOutNUcastPkts = _SwitchIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 18),
    _SwitchIfOutNUcastPkts_Type()
)
switchIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutNUcastPkts.setStatus("deprecated")
_SwitchIfOutDiscards_Type = Counter32
_SwitchIfOutDiscards_Object = MibTableColumn
switchIfOutDiscards = _SwitchIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 19),
    _SwitchIfOutDiscards_Type()
)
switchIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutDiscards.setStatus("current")
_SwitchIfOutErrors_Type = Counter32
_SwitchIfOutErrors_Object = MibTableColumn
switchIfOutErrors = _SwitchIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 20),
    _SwitchIfOutErrors_Type()
)
switchIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutErrors.setStatus("current")
_SwitchIfOutQLen_Type = Gauge32
_SwitchIfOutQLen_Object = MibTableColumn
switchIfOutQLen = _SwitchIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 21),
    _SwitchIfOutQLen_Type()
)
switchIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutQLen.setStatus("deprecated")
_SwitchIfSpecific_Type = ObjectIdentifier
_SwitchIfSpecific_Object = MibTableColumn
switchIfSpecific = _SwitchIfSpecific_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 3, 1, 22),
    _SwitchIfSpecific_Type()
)
switchIfSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfSpecific.setStatus("deprecated")
_SwitchIfXTable_Object = MibTable
switchIfXTable = _SwitchIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4)
)
if mibBuilder.loadTexts:
    switchIfXTable.setStatus("current")
_SwitchIfXEntry_Object = MibTableRow
switchIfXEntry = _SwitchIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1)
)
if mibBuilder.loadTexts:
    switchIfXEntry.setStatus("current")
_SwitchIfName_Type = DisplayString
_SwitchIfName_Object = MibTableColumn
switchIfName = _SwitchIfName_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 1),
    _SwitchIfName_Type()
)
switchIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfName.setStatus("current")
_SwitchIfInMulticastPkts_Type = Counter32
_SwitchIfInMulticastPkts_Object = MibTableColumn
switchIfInMulticastPkts = _SwitchIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 2),
    _SwitchIfInMulticastPkts_Type()
)
switchIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInMulticastPkts.setStatus("current")
_SwitchIfInBroadcastPkts_Type = Counter32
_SwitchIfInBroadcastPkts_Object = MibTableColumn
switchIfInBroadcastPkts = _SwitchIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 3),
    _SwitchIfInBroadcastPkts_Type()
)
switchIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfInBroadcastPkts.setStatus("current")
_SwitchIfOutMulticastPkts_Type = Counter32
_SwitchIfOutMulticastPkts_Object = MibTableColumn
switchIfOutMulticastPkts = _SwitchIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 4),
    _SwitchIfOutMulticastPkts_Type()
)
switchIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutMulticastPkts.setStatus("current")
_SwitchIfOutBroadcastPkts_Type = Counter32
_SwitchIfOutBroadcastPkts_Object = MibTableColumn
switchIfOutBroadcastPkts = _SwitchIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 5),
    _SwitchIfOutBroadcastPkts_Type()
)
switchIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfOutBroadcastPkts.setStatus("current")
_SwitchIfHCInOctets_Type = Counter64
_SwitchIfHCInOctets_Object = MibTableColumn
switchIfHCInOctets = _SwitchIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 6),
    _SwitchIfHCInOctets_Type()
)
switchIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCInOctets.setStatus("current")
_SwitchIfHCInUcastPkts_Type = Counter64
_SwitchIfHCInUcastPkts_Object = MibTableColumn
switchIfHCInUcastPkts = _SwitchIfHCInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 7),
    _SwitchIfHCInUcastPkts_Type()
)
switchIfHCInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCInUcastPkts.setStatus("current")
_SwitchIfHCInMulticastPkts_Type = Counter64
_SwitchIfHCInMulticastPkts_Object = MibTableColumn
switchIfHCInMulticastPkts = _SwitchIfHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 8),
    _SwitchIfHCInMulticastPkts_Type()
)
switchIfHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCInMulticastPkts.setStatus("current")
_SwitchIfHCInBroadcastPkts_Type = Counter64
_SwitchIfHCInBroadcastPkts_Object = MibTableColumn
switchIfHCInBroadcastPkts = _SwitchIfHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 9),
    _SwitchIfHCInBroadcastPkts_Type()
)
switchIfHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCInBroadcastPkts.setStatus("current")
_SwitchIfHCOutOctets_Type = Counter64
_SwitchIfHCOutOctets_Object = MibTableColumn
switchIfHCOutOctets = _SwitchIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 10),
    _SwitchIfHCOutOctets_Type()
)
switchIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCOutOctets.setStatus("current")
_SwitchIfHCOutUcastPkts_Type = Counter64
_SwitchIfHCOutUcastPkts_Object = MibTableColumn
switchIfHCOutUcastPkts = _SwitchIfHCOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 11),
    _SwitchIfHCOutUcastPkts_Type()
)
switchIfHCOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCOutUcastPkts.setStatus("current")
_SwitchIfHCOutMulticastPkts_Type = Counter64
_SwitchIfHCOutMulticastPkts_Object = MibTableColumn
switchIfHCOutMulticastPkts = _SwitchIfHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 12),
    _SwitchIfHCOutMulticastPkts_Type()
)
switchIfHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCOutMulticastPkts.setStatus("current")
_SwitchIfHCOutBroadcastPkts_Type = Counter64
_SwitchIfHCOutBroadcastPkts_Object = MibTableColumn
switchIfHCOutBroadcastPkts = _SwitchIfHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 13),
    _SwitchIfHCOutBroadcastPkts_Type()
)
switchIfHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHCOutBroadcastPkts.setStatus("current")


class _SwitchIfLinkUpDownTrapEnable_Type(Integer32):
    """Custom type switchIfLinkUpDownTrapEnable based on Integer32"""
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


_SwitchIfLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_SwitchIfLinkUpDownTrapEnable_Object = MibTableColumn
switchIfLinkUpDownTrapEnable = _SwitchIfLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 14),
    _SwitchIfLinkUpDownTrapEnable_Type()
)
switchIfLinkUpDownTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfLinkUpDownTrapEnable.setStatus("current")
_SwitchIfHighSpeed_Type = Gauge32
_SwitchIfHighSpeed_Object = MibTableColumn
switchIfHighSpeed = _SwitchIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 15),
    _SwitchIfHighSpeed_Type()
)
switchIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfHighSpeed.setStatus("current")
_SwitchIfPromiscuousMode_Type = TruthValue
_SwitchIfPromiscuousMode_Object = MibTableColumn
switchIfPromiscuousMode = _SwitchIfPromiscuousMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 16),
    _SwitchIfPromiscuousMode_Type()
)
switchIfPromiscuousMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfPromiscuousMode.setStatus("current")
_SwitchIfConnectorPresent_Type = TruthValue
_SwitchIfConnectorPresent_Object = MibTableColumn
switchIfConnectorPresent = _SwitchIfConnectorPresent_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 17),
    _SwitchIfConnectorPresent_Type()
)
switchIfConnectorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfConnectorPresent.setStatus("current")


class _SwitchIfAlias_Type(DisplayString):
    """Custom type switchIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwitchIfAlias_Type.__name__ = "DisplayString"
_SwitchIfAlias_Object = MibTableColumn
switchIfAlias = _SwitchIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 18),
    _SwitchIfAlias_Type()
)
switchIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfAlias.setStatus("current")
_SwitchIfCounterDiscontinuityTime_Type = TimeStamp
_SwitchIfCounterDiscontinuityTime_Object = MibTableColumn
switchIfCounterDiscontinuityTime = _SwitchIfCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 4, 1, 19),
    _SwitchIfCounterDiscontinuityTime_Type()
)
switchIfCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIfCounterDiscontinuityTime.setStatus("current")
_SwitchEtherStatsTable_Object = MibTable
switchEtherStatsTable = _SwitchEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5)
)
if mibBuilder.loadTexts:
    switchEtherStatsTable.setStatus("current")
_SwitchEtherStatsEntry_Object = MibTableRow
switchEtherStatsEntry = _SwitchEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1)
)
switchEtherStatsEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsIndex"),
)
if mibBuilder.loadTexts:
    switchEtherStatsEntry.setStatus("current")


class _SwitchEtherStatsIndex_Type(Integer32):
    """Custom type switchEtherStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchEtherStatsIndex_Type.__name__ = "Integer32"
_SwitchEtherStatsIndex_Object = MibTableColumn
switchEtherStatsIndex = _SwitchEtherStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 1),
    _SwitchEtherStatsIndex_Type()
)
switchEtherStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsIndex.setStatus("current")
_SwitchEtherStatsDataSource_Type = ObjectIdentifier
_SwitchEtherStatsDataSource_Object = MibTableColumn
switchEtherStatsDataSource = _SwitchEtherStatsDataSource_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 2),
    _SwitchEtherStatsDataSource_Type()
)
switchEtherStatsDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchEtherStatsDataSource.setStatus("current")
_SwitchEtherStatsDropEvents_Type = Counter32
_SwitchEtherStatsDropEvents_Object = MibTableColumn
switchEtherStatsDropEvents = _SwitchEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 3),
    _SwitchEtherStatsDropEvents_Type()
)
switchEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsDropEvents.setStatus("current")
_SwitchEtherStatsOctets_Type = Counter32
_SwitchEtherStatsOctets_Object = MibTableColumn
switchEtherStatsOctets = _SwitchEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 4),
    _SwitchEtherStatsOctets_Type()
)
switchEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsOctets.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsOctets.setUnits("Octets")
_SwitchEtherStatsPkts_Type = Counter32
_SwitchEtherStatsPkts_Object = MibTableColumn
switchEtherStatsPkts = _SwitchEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 5),
    _SwitchEtherStatsPkts_Type()
)
switchEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsPkts.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsPkts.setUnits("Packets")
_SwitchEtherStatsBroadcastPkts_Type = Counter32
_SwitchEtherStatsBroadcastPkts_Object = MibTableColumn
switchEtherStatsBroadcastPkts = _SwitchEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 6),
    _SwitchEtherStatsBroadcastPkts_Type()
)
switchEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsBroadcastPkts.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsBroadcastPkts.setUnits("Packets")
_SwitchEtherStatsMulticastPkts_Type = Counter32
_SwitchEtherStatsMulticastPkts_Object = MibTableColumn
switchEtherStatsMulticastPkts = _SwitchEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 7),
    _SwitchEtherStatsMulticastPkts_Type()
)
switchEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsMulticastPkts.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsMulticastPkts.setUnits("Packets")
_SwitchEtherStatsCRCAlignErrors_Type = Counter32
_SwitchEtherStatsCRCAlignErrors_Object = MibTableColumn
switchEtherStatsCRCAlignErrors = _SwitchEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 8),
    _SwitchEtherStatsCRCAlignErrors_Type()
)
switchEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsCRCAlignErrors.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsCRCAlignErrors.setUnits("Packets")
_SwitchEtherStatsUndersizePkts_Type = Counter32
_SwitchEtherStatsUndersizePkts_Object = MibTableColumn
switchEtherStatsUndersizePkts = _SwitchEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 9),
    _SwitchEtherStatsUndersizePkts_Type()
)
switchEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsUndersizePkts.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsUndersizePkts.setUnits("Packets")
_SwitchEtherStatsOversizePkts_Type = Counter32
_SwitchEtherStatsOversizePkts_Object = MibTableColumn
switchEtherStatsOversizePkts = _SwitchEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 10),
    _SwitchEtherStatsOversizePkts_Type()
)
switchEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsOversizePkts.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsOversizePkts.setUnits("Packets")
_SwitchEtherStatsFragments_Type = Counter32
_SwitchEtherStatsFragments_Object = MibTableColumn
switchEtherStatsFragments = _SwitchEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 11),
    _SwitchEtherStatsFragments_Type()
)
switchEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsFragments.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsFragments.setUnits("Packets")
_SwitchEtherStatsJabbers_Type = Counter32
_SwitchEtherStatsJabbers_Object = MibTableColumn
switchEtherStatsJabbers = _SwitchEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 12),
    _SwitchEtherStatsJabbers_Type()
)
switchEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsJabbers.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsJabbers.setUnits("Packets")
_SwitchEtherStatsCollisions_Type = Counter32
_SwitchEtherStatsCollisions_Object = MibTableColumn
switchEtherStatsCollisions = _SwitchEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 13),
    _SwitchEtherStatsCollisions_Type()
)
switchEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsCollisions.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsCollisions.setUnits("Collisions")
_SwitchEtherStatsPkts64Octets_Type = Counter32
_SwitchEtherStatsPkts64Octets_Object = MibTableColumn
switchEtherStatsPkts64Octets = _SwitchEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 14),
    _SwitchEtherStatsPkts64Octets_Type()
)
switchEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsPkts64Octets.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsPkts64Octets.setUnits("Packets")
_SwitchEtherStatsPkts65to127Octets_Type = Counter32
_SwitchEtherStatsPkts65to127Octets_Object = MibTableColumn
switchEtherStatsPkts65to127Octets = _SwitchEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 15),
    _SwitchEtherStatsPkts65to127Octets_Type()
)
switchEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsPkts65to127Octets.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsPkts65to127Octets.setUnits("Packets")
_SwitchEtherStatsPkts128to255Octets_Type = Counter32
_SwitchEtherStatsPkts128to255Octets_Object = MibTableColumn
switchEtherStatsPkts128to255Octets = _SwitchEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 16),
    _SwitchEtherStatsPkts128to255Octets_Type()
)
switchEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsPkts128to255Octets.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsPkts128to255Octets.setUnits("Packets")
_SwitchEtherStatsPkts256to511Octets_Type = Counter32
_SwitchEtherStatsPkts256to511Octets_Object = MibTableColumn
switchEtherStatsPkts256to511Octets = _SwitchEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 17),
    _SwitchEtherStatsPkts256to511Octets_Type()
)
switchEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsPkts256to511Octets.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsPkts256to511Octets.setUnits("Packets")
_SwitchEtherStatsPkts512to1023Octets_Type = Counter32
_SwitchEtherStatsPkts512to1023Octets_Object = MibTableColumn
switchEtherStatsPkts512to1023Octets = _SwitchEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 18),
    _SwitchEtherStatsPkts512to1023Octets_Type()
)
switchEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsPkts512to1023Octets.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsPkts512to1023Octets.setUnits("Packets")
_SwitchEtherStatsPkts1024to1518Octets_Type = Counter32
_SwitchEtherStatsPkts1024to1518Octets_Object = MibTableColumn
switchEtherStatsPkts1024to1518Octets = _SwitchEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 19),
    _SwitchEtherStatsPkts1024to1518Octets_Type()
)
switchEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchEtherStatsPkts1024to1518Octets.setStatus("current")
if mibBuilder.loadTexts:
    switchEtherStatsPkts1024to1518Octets.setUnits("Packets")
_SwitchEtherStatsOwner_Type = OwnerString
_SwitchEtherStatsOwner_Object = MibTableColumn
switchEtherStatsOwner = _SwitchEtherStatsOwner_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 20),
    _SwitchEtherStatsOwner_Type()
)
switchEtherStatsOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchEtherStatsOwner.setStatus("current")
_SwitchEtherStatsStatus_Type = EntryStatus
_SwitchEtherStatsStatus_Object = MibTableColumn
switchEtherStatsStatus = _SwitchEtherStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 5, 1, 21),
    _SwitchEtherStatsStatus_Type()
)
switchEtherStatsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchEtherStatsStatus.setStatus("current")
_SwitchDot1dTpFdbTable_Object = MibTable
switchDot1dTpFdbTable = _SwitchDot1dTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 6)
)
if mibBuilder.loadTexts:
    switchDot1dTpFdbTable.setStatus("current")
_SwitchDot1dTpFdbEntry_Object = MibTableRow
switchDot1dTpFdbEntry = _SwitchDot1dTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 6, 1)
)
switchDot1dTpFdbEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1dTpFdbAddress"),
)
if mibBuilder.loadTexts:
    switchDot1dTpFdbEntry.setStatus("current")
_SwitchDot1dTpFdbAddress_Type = MacAddress
_SwitchDot1dTpFdbAddress_Object = MibTableColumn
switchDot1dTpFdbAddress = _SwitchDot1dTpFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 6, 1, 1),
    _SwitchDot1dTpFdbAddress_Type()
)
switchDot1dTpFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1dTpFdbAddress.setStatus("current")
_SwitchDot1dTpFdbPort_Type = Integer32
_SwitchDot1dTpFdbPort_Object = MibTableColumn
switchDot1dTpFdbPort = _SwitchDot1dTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 6, 1, 2),
    _SwitchDot1dTpFdbPort_Type()
)
switchDot1dTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1dTpFdbPort.setStatus("current")


class _SwitchDot1dTpFdbStatus_Type(Integer32):
    """Custom type switchDot1dTpFdbStatus based on Integer32"""
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
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_SwitchDot1dTpFdbStatus_Type.__name__ = "Integer32"
_SwitchDot1dTpFdbStatus_Object = MibTableColumn
switchDot1dTpFdbStatus = _SwitchDot1dTpFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 6, 1, 3),
    _SwitchDot1dTpFdbStatus_Type()
)
switchDot1dTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1dTpFdbStatus.setStatus("current")
_SwitchDot1qVlanCurrentTable_Object = MibTable
switchDot1qVlanCurrentTable = _SwitchDot1qVlanCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7)
)
if mibBuilder.loadTexts:
    switchDot1qVlanCurrentTable.setStatus("current")
_SwitchDot1qVlanCurrentEntry_Object = MibTableRow
switchDot1qVlanCurrentEntry = _SwitchDot1qVlanCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1)
)
switchDot1qVlanCurrentEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qVlanTimeMark"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    switchDot1qVlanCurrentEntry.setStatus("current")
_SwitchDot1qVlanTimeMark_Type = TimeFilter
_SwitchDot1qVlanTimeMark_Object = MibTableColumn
switchDot1qVlanTimeMark = _SwitchDot1qVlanTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1, 1),
    _SwitchDot1qVlanTimeMark_Type()
)
switchDot1qVlanTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchDot1qVlanTimeMark.setStatus("current")
_SwitchDot1qVlanIndex_Type = VlanIndex
_SwitchDot1qVlanIndex_Object = MibTableColumn
switchDot1qVlanIndex = _SwitchDot1qVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1, 2),
    _SwitchDot1qVlanIndex_Type()
)
switchDot1qVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchDot1qVlanIndex.setStatus("current")
_SwitchDot1qVlanFdbId_Type = Unsigned32
_SwitchDot1qVlanFdbId_Object = MibTableColumn
switchDot1qVlanFdbId = _SwitchDot1qVlanFdbId_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1, 3),
    _SwitchDot1qVlanFdbId_Type()
)
switchDot1qVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qVlanFdbId.setStatus("current")
_SwitchDot1qVlanCurrentEgressPorts_Type = PortList
_SwitchDot1qVlanCurrentEgressPorts_Object = MibTableColumn
switchDot1qVlanCurrentEgressPorts = _SwitchDot1qVlanCurrentEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1, 4),
    _SwitchDot1qVlanCurrentEgressPorts_Type()
)
switchDot1qVlanCurrentEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qVlanCurrentEgressPorts.setStatus("current")
_SwitchDot1qVlanCurrentUntaggedPorts_Type = PortList
_SwitchDot1qVlanCurrentUntaggedPorts_Object = MibTableColumn
switchDot1qVlanCurrentUntaggedPorts = _SwitchDot1qVlanCurrentUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1, 5),
    _SwitchDot1qVlanCurrentUntaggedPorts_Type()
)
switchDot1qVlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qVlanCurrentUntaggedPorts.setStatus("current")


class _SwitchDot1qVlanStatus_Type(Integer32):
    """Custom type switchDot1qVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 3),
          ("other", 1),
          ("permanent", 2))
    )


_SwitchDot1qVlanStatus_Type.__name__ = "Integer32"
_SwitchDot1qVlanStatus_Object = MibTableColumn
switchDot1qVlanStatus = _SwitchDot1qVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1, 6),
    _SwitchDot1qVlanStatus_Type()
)
switchDot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qVlanStatus.setStatus("current")
_SwitchDot1qVlanCreationTime_Type = TimeTicks
_SwitchDot1qVlanCreationTime_Object = MibTableColumn
switchDot1qVlanCreationTime = _SwitchDot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 7, 1, 7),
    _SwitchDot1qVlanCreationTime_Type()
)
switchDot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qVlanCreationTime.setStatus("current")
_SwitchDot1qPortVlanTable_Object = MibTable
switchDot1qPortVlanTable = _SwitchDot1qPortVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8)
)
if mibBuilder.loadTexts:
    switchDot1qPortVlanTable.setStatus("current")
_SwitchDot1qPortVlanEntry_Object = MibTableRow
switchDot1qPortVlanEntry = _SwitchDot1qPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1)
)
switchDot1qPortVlanEntry.setIndexNames(
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
    (0, "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1dBasePort"),
)
if mibBuilder.loadTexts:
    switchDot1qPortVlanEntry.setStatus("current")


class _SwitchDot1dBasePort_Type(Integer32):
    """Custom type switchDot1dBasePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwitchDot1dBasePort_Type.__name__ = "Integer32"
_SwitchDot1dBasePort_Object = MibTableColumn
switchDot1dBasePort = _SwitchDot1dBasePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1, 1),
    _SwitchDot1dBasePort_Type()
)
switchDot1dBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1dBasePort.setStatus("current")
_SwitchDot1qPvid_Type = VlanIndex
_SwitchDot1qPvid_Object = MibTableColumn
switchDot1qPvid = _SwitchDot1qPvid_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1, 2),
    _SwitchDot1qPvid_Type()
)
switchDot1qPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qPvid.setStatus("current")


class _SwitchDot1qPortAcceptableFrameTypes_Type(Integer32):
    """Custom type switchDot1qPortAcceptableFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2))
    )


_SwitchDot1qPortAcceptableFrameTypes_Type.__name__ = "Integer32"
_SwitchDot1qPortAcceptableFrameTypes_Object = MibTableColumn
switchDot1qPortAcceptableFrameTypes = _SwitchDot1qPortAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1, 3),
    _SwitchDot1qPortAcceptableFrameTypes_Type()
)
switchDot1qPortAcceptableFrameTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qPortAcceptableFrameTypes.setStatus("current")


class _SwitchDot1qPortIngressFiltering_Type(TruthValue):
    """Custom type switchDot1qPortIngressFiltering based on TruthValue"""


_SwitchDot1qPortIngressFiltering_Object = MibTableColumn
switchDot1qPortIngressFiltering = _SwitchDot1qPortIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1, 4),
    _SwitchDot1qPortIngressFiltering_Type()
)
switchDot1qPortIngressFiltering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qPortIngressFiltering.setStatus("current")
_SwitchDot1qPortGvrpStatus_Type = EnabledStatus
_SwitchDot1qPortGvrpStatus_Object = MibTableColumn
switchDot1qPortGvrpStatus = _SwitchDot1qPortGvrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1, 5),
    _SwitchDot1qPortGvrpStatus_Type()
)
switchDot1qPortGvrpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qPortGvrpStatus.setStatus("current")
_SwitchDot1qPortGvrpFailedRegistrations_Type = Counter32
_SwitchDot1qPortGvrpFailedRegistrations_Object = MibTableColumn
switchDot1qPortGvrpFailedRegistrations = _SwitchDot1qPortGvrpFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1, 6),
    _SwitchDot1qPortGvrpFailedRegistrations_Type()
)
switchDot1qPortGvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qPortGvrpFailedRegistrations.setStatus("current")
_SwitchDot1qPortGvrpLastPduOrigin_Type = MacAddress
_SwitchDot1qPortGvrpLastPduOrigin_Object = MibTableColumn
switchDot1qPortGvrpLastPduOrigin = _SwitchDot1qPortGvrpLastPduOrigin_Object(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 10, 203, 8, 1, 7),
    _SwitchDot1qPortGvrpLastPduOrigin_Type()
)
switchDot1qPortGvrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchDot1qPortGvrpLastPduOrigin.setStatus("current")
switchIfEntry.registerAugmentions(
    ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB",
     "switchIfXEntry")
)
switchIfXEntry.setIndexNames(*switchIfEntry.getIndexNames())

# Managed Objects groups

switchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 343, 2, 19, 1, 2, 2, 2, 13)
)
switchGroup.setObjects(
      *(("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "maxSwitches"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "numOfSwitches"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPresenceMask"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchVendor"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchMfgDate"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDeviceName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPart"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchSerialNo"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchMaximumPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchNominalPower"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchAssetTag"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchFirmwareVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchVersion"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPresence"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPowerLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchFaultLed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsIfIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsIfIndexName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsMediaType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsStackUnit"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsModuleNumber"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsRow"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortsColumn"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyConnectorType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchPhyPortHaul"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfDescr"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfType"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfMtu"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfSpeed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfPhysAddress"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfAdminStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfOperStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfLastChange"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfInOctets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfInUcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfInDiscards"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfInErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfInUnknownProtos"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfOutOctets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfOutUcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfOutDiscards"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfOutErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfName"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfInMulticastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfInBroadcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfOutMulticastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfOutBroadcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCInOctets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCInUcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCInMulticastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCInBroadcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCOutOctets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCOutUcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCOutMulticastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHCOutBroadcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfLinkUpDownTrapEnable"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfHighSpeed"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfPromiscuousMode"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfConnectorPresent"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfAlias"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchIfCounterDiscontinuityTime"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsIndex"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsDataSource"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsDropEvents"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsOctets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsBroadcastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsMulticastPkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsCRCAlignErrors"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsUndersizePkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsOversizePkts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsFragments"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsJabbers"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsCollisions"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsPkts64Octets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsPkts65to127Octets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsPkts128to255Octets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsPkts256to511Octets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsPkts512to1023Octets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsPkts1024to1518Octets"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsOwner"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchEtherStatsStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1dTpFdbAddress"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1dTpFdbPort"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1dTpFdbStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qVlanFdbId"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qVlanCurrentEgressPorts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qVlanCurrentUntaggedPorts"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qVlanStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qVlanCreationTime"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1dBasePort"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qPvid"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qPortAcceptableFrameTypes"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qPortIngressFiltering"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qPortGvrpStatus"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qPortGvrpFailedRegistrations"),
        ("INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB", "switchDot1qPortGvrpLastPduOrigin"))
)
if mibBuilder.loadTexts:
    switchGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTELCORPORATION-MULTI-FLEX-SERVER-SWITCH-MIB",
    **{"multiFlexServerSwitchMibModule": multiFlexServerSwitchMibModule,
       "switchGroup": switchGroup,
       "maxSwitches": maxSwitches,
       "numOfSwitches": numOfSwitches,
       "switchPresenceMask": switchPresenceMask,
       "switches": switches,
       "switchTable": switchTable,
       "switchEntry": switchEntry,
       "switchIndex": switchIndex,
       "switchPresence": switchPresence,
       "switchVendor": switchVendor,
       "switchMfgDate": switchMfgDate,
       "switchDeviceName": switchDeviceName,
       "switchPart": switchPart,
       "switchSerialNo": switchSerialNo,
       "switchMaximumPower": switchMaximumPower,
       "switchNominalPower": switchNominalPower,
       "switchAssetTag": switchAssetTag,
       "switchFirmwareVersion": switchFirmwareVersion,
       "switchVersion": switchVersion,
       "switchPowerLed": switchPowerLed,
       "switchFaultLed": switchFaultLed,
       "switchPhyPortsTable": switchPhyPortsTable,
       "switchPhyPortsEntry": switchPhyPortsEntry,
       "switchPhyPortsIfIndex": switchPhyPortsIfIndex,
       "switchPhyPortsIfIndexName": switchPhyPortsIfIndexName,
       "switchPhyPortsMediaType": switchPhyPortsMediaType,
       "switchPhyPortsStackUnit": switchPhyPortsStackUnit,
       "switchPhyPortsModuleNumber": switchPhyPortsModuleNumber,
       "switchPhyPortsRow": switchPhyPortsRow,
       "switchPhyPortsColumn": switchPhyPortsColumn,
       "switchPhyConnectorType": switchPhyConnectorType,
       "switchPhyPortHaul": switchPhyPortHaul,
       "switchIfTable": switchIfTable,
       "switchIfEntry": switchIfEntry,
       "switchIfIndex": switchIfIndex,
       "switchIfDescr": switchIfDescr,
       "switchIfType": switchIfType,
       "switchIfMtu": switchIfMtu,
       "switchIfSpeed": switchIfSpeed,
       "switchIfPhysAddress": switchIfPhysAddress,
       "switchIfAdminStatus": switchIfAdminStatus,
       "switchIfOperStatus": switchIfOperStatus,
       "switchIfLastChange": switchIfLastChange,
       "switchIfInOctets": switchIfInOctets,
       "switchIfInUcastPkts": switchIfInUcastPkts,
       "switchIfInNUcastPkts": switchIfInNUcastPkts,
       "switchIfInDiscards": switchIfInDiscards,
       "switchIfInErrors": switchIfInErrors,
       "switchIfInUnknownProtos": switchIfInUnknownProtos,
       "switchIfOutOctets": switchIfOutOctets,
       "switchIfOutUcastPkts": switchIfOutUcastPkts,
       "switchIfOutNUcastPkts": switchIfOutNUcastPkts,
       "switchIfOutDiscards": switchIfOutDiscards,
       "switchIfOutErrors": switchIfOutErrors,
       "switchIfOutQLen": switchIfOutQLen,
       "switchIfSpecific": switchIfSpecific,
       "switchIfXTable": switchIfXTable,
       "switchIfXEntry": switchIfXEntry,
       "switchIfName": switchIfName,
       "switchIfInMulticastPkts": switchIfInMulticastPkts,
       "switchIfInBroadcastPkts": switchIfInBroadcastPkts,
       "switchIfOutMulticastPkts": switchIfOutMulticastPkts,
       "switchIfOutBroadcastPkts": switchIfOutBroadcastPkts,
       "switchIfHCInOctets": switchIfHCInOctets,
       "switchIfHCInUcastPkts": switchIfHCInUcastPkts,
       "switchIfHCInMulticastPkts": switchIfHCInMulticastPkts,
       "switchIfHCInBroadcastPkts": switchIfHCInBroadcastPkts,
       "switchIfHCOutOctets": switchIfHCOutOctets,
       "switchIfHCOutUcastPkts": switchIfHCOutUcastPkts,
       "switchIfHCOutMulticastPkts": switchIfHCOutMulticastPkts,
       "switchIfHCOutBroadcastPkts": switchIfHCOutBroadcastPkts,
       "switchIfLinkUpDownTrapEnable": switchIfLinkUpDownTrapEnable,
       "switchIfHighSpeed": switchIfHighSpeed,
       "switchIfPromiscuousMode": switchIfPromiscuousMode,
       "switchIfConnectorPresent": switchIfConnectorPresent,
       "switchIfAlias": switchIfAlias,
       "switchIfCounterDiscontinuityTime": switchIfCounterDiscontinuityTime,
       "switchEtherStatsTable": switchEtherStatsTable,
       "switchEtherStatsEntry": switchEtherStatsEntry,
       "switchEtherStatsIndex": switchEtherStatsIndex,
       "switchEtherStatsDataSource": switchEtherStatsDataSource,
       "switchEtherStatsDropEvents": switchEtherStatsDropEvents,
       "switchEtherStatsOctets": switchEtherStatsOctets,
       "switchEtherStatsPkts": switchEtherStatsPkts,
       "switchEtherStatsBroadcastPkts": switchEtherStatsBroadcastPkts,
       "switchEtherStatsMulticastPkts": switchEtherStatsMulticastPkts,
       "switchEtherStatsCRCAlignErrors": switchEtherStatsCRCAlignErrors,
       "switchEtherStatsUndersizePkts": switchEtherStatsUndersizePkts,
       "switchEtherStatsOversizePkts": switchEtherStatsOversizePkts,
       "switchEtherStatsFragments": switchEtherStatsFragments,
       "switchEtherStatsJabbers": switchEtherStatsJabbers,
       "switchEtherStatsCollisions": switchEtherStatsCollisions,
       "switchEtherStatsPkts64Octets": switchEtherStatsPkts64Octets,
       "switchEtherStatsPkts65to127Octets": switchEtherStatsPkts65to127Octets,
       "switchEtherStatsPkts128to255Octets": switchEtherStatsPkts128to255Octets,
       "switchEtherStatsPkts256to511Octets": switchEtherStatsPkts256to511Octets,
       "switchEtherStatsPkts512to1023Octets": switchEtherStatsPkts512to1023Octets,
       "switchEtherStatsPkts1024to1518Octets": switchEtherStatsPkts1024to1518Octets,
       "switchEtherStatsOwner": switchEtherStatsOwner,
       "switchEtherStatsStatus": switchEtherStatsStatus,
       "switchDot1dTpFdbTable": switchDot1dTpFdbTable,
       "switchDot1dTpFdbEntry": switchDot1dTpFdbEntry,
       "switchDot1dTpFdbAddress": switchDot1dTpFdbAddress,
       "switchDot1dTpFdbPort": switchDot1dTpFdbPort,
       "switchDot1dTpFdbStatus": switchDot1dTpFdbStatus,
       "switchDot1qVlanCurrentTable": switchDot1qVlanCurrentTable,
       "switchDot1qVlanCurrentEntry": switchDot1qVlanCurrentEntry,
       "switchDot1qVlanTimeMark": switchDot1qVlanTimeMark,
       "switchDot1qVlanIndex": switchDot1qVlanIndex,
       "switchDot1qVlanFdbId": switchDot1qVlanFdbId,
       "switchDot1qVlanCurrentEgressPorts": switchDot1qVlanCurrentEgressPorts,
       "switchDot1qVlanCurrentUntaggedPorts": switchDot1qVlanCurrentUntaggedPorts,
       "switchDot1qVlanStatus": switchDot1qVlanStatus,
       "switchDot1qVlanCreationTime": switchDot1qVlanCreationTime,
       "switchDot1qPortVlanTable": switchDot1qPortVlanTable,
       "switchDot1qPortVlanEntry": switchDot1qPortVlanEntry,
       "switchDot1dBasePort": switchDot1dBasePort,
       "switchDot1qPvid": switchDot1qPvid,
       "switchDot1qPortAcceptableFrameTypes": switchDot1qPortAcceptableFrameTypes,
       "switchDot1qPortIngressFiltering": switchDot1qPortIngressFiltering,
       "switchDot1qPortGvrpStatus": switchDot1qPortGvrpStatus,
       "switchDot1qPortGvrpFailedRegistrations": switchDot1qPortGvrpFailedRegistrations,
       "switchDot1qPortGvrpLastPduOrigin": switchDot1qPortGvrpLastPduOrigin}
)
