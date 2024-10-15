# SNMP MIB module (SWITCHING-EXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SWITCHING-EXTENSION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:20 2024
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
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,
 dot1qFdbId,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex",
    "dot1qFdbId",
    "dot1qVlanIndex")

(AgentPortMask,
 quanta,
 switch) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "AgentPortMask",
    "quanta",
    "switch")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(VlanList,) = mibBuilder.importSymbols(
    "SWITCHING-MIB",
    "VlanList")


# MODULE-IDENTITY

switchingExtension = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BridgeEvbTLVTC(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_AgentInfoGroupExtension_ObjectIdentity = ObjectIdentity
agentInfoGroupExtension = _AgentInfoGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1)
)
_AgentInventoryGroupExtension_ObjectIdentity = ObjectIdentity
agentInventoryGroupExtension = _AgentInventoryGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1)
)
_AgentInventroyHardwareVersion_Type = DisplayString
_AgentInventroyHardwareVersion_Object = MibScalar
agentInventroyHardwareVersion = _AgentInventroyHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 100),
    _AgentInventroyHardwareVersion_Type()
)
agentInventroyHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventroyHardwareVersion.setStatus("current")
_AgentInventoryLoaderVersion_Type = DisplayString
_AgentInventoryLoaderVersion_Object = MibScalar
agentInventoryLoaderVersion = _AgentInventoryLoaderVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 102),
    _AgentInventoryLoaderVersion_Type()
)
agentInventoryLoaderVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryLoaderVersion.setStatus("current")
_AgentInventoryBootRomVersion_Type = DisplayString
_AgentInventoryBootRomVersion_Object = MibScalar
agentInventoryBootRomVersion = _AgentInventoryBootRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 103),
    _AgentInventoryBootRomVersion_Type()
)
agentInventoryBootRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryBootRomVersion.setStatus("current")
_AgentInventoryOpCodeVersion_Type = DisplayString
_AgentInventoryOpCodeVersion_Object = MibScalar
agentInventoryOpCodeVersion = _AgentInventoryOpCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 104),
    _AgentInventoryOpCodeVersion_Type()
)
agentInventoryOpCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryOpCodeVersion.setStatus("current")
_AgentInventoryLabelRevNumber_Type = DisplayString
_AgentInventoryLabelRevNumber_Object = MibScalar
agentInventoryLabelRevNumber = _AgentInventoryLabelRevNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 105),
    _AgentInventoryLabelRevNumber_Type()
)
agentInventoryLabelRevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryLabelRevNumber.setStatus("current")
_AgentTemperatureFanStatusTable_Object = MibTable
agentTemperatureFanStatusTable = _AgentTemperatureFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106)
)
if mibBuilder.loadTexts:
    agentTemperatureFanStatusTable.setStatus("current")
_AgentTemperatureFanStatusEntry_Object = MibTableRow
agentTemperatureFanStatusEntry = _AgentTemperatureFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1)
)
agentTemperatureFanStatusEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentTemperatureFanUnitIndex"),
)
if mibBuilder.loadTexts:
    agentTemperatureFanStatusEntry.setStatus("current")


class _AgentTemperatureFanUnitIndex_Type(Integer32):
    """Custom type agentTemperatureFanUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentTemperatureFanUnitIndex_Type.__name__ = "Integer32"
_AgentTemperatureFanUnitIndex_Object = MibTableColumn
agentTemperatureFanUnitIndex = _AgentTemperatureFanUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 1),
    _AgentTemperatureFanUnitIndex_Type()
)
agentTemperatureFanUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTemperatureFanUnitIndex.setStatus("current")
_AgentTemperature_Type = DisplayString
_AgentTemperature_Object = MibTableColumn
agentTemperature = _AgentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 2),
    _AgentTemperature_Type()
)
agentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTemperature.setStatus("current")
_AgentTemperature1_Type = DisplayString
_AgentTemperature1_Object = MibTableColumn
agentTemperature1 = _AgentTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 11),
    _AgentTemperature1_Type()
)
agentTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTemperature1.setStatus("current")
_AgentTemperature2_Type = DisplayString
_AgentTemperature2_Object = MibTableColumn
agentTemperature2 = _AgentTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 12),
    _AgentTemperature2_Type()
)
agentTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTemperature2.setStatus("current")
_AgentTemperature3_Type = DisplayString
_AgentTemperature3_Object = MibTableColumn
agentTemperature3 = _AgentTemperature3_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 13),
    _AgentTemperature3_Type()
)
agentTemperature3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTemperature3.setStatus("current")
_AgentTemperature4_Type = DisplayString
_AgentTemperature4_Object = MibTableColumn
agentTemperature4 = _AgentTemperature4_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 14),
    _AgentTemperature4_Type()
)
agentTemperature4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTemperature4.setStatus("current")
_AgentTemperature5_Type = DisplayString
_AgentTemperature5_Object = MibTableColumn
agentTemperature5 = _AgentTemperature5_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 15),
    _AgentTemperature5_Type()
)
agentTemperature5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTemperature5.setStatus("current")


class _AgentFAN1_Type(Integer32):
    """Custom type agentFAN1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentFAN1_Type.__name__ = "Integer32"
_AgentFAN1_Object = MibTableColumn
agentFAN1 = _AgentFAN1_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 21),
    _AgentFAN1_Type()
)
agentFAN1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFAN1.setStatus("current")


class _AgentFAN2_Type(Integer32):
    """Custom type agentFAN2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentFAN2_Type.__name__ = "Integer32"
_AgentFAN2_Object = MibTableColumn
agentFAN2 = _AgentFAN2_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 22),
    _AgentFAN2_Type()
)
agentFAN2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFAN2.setStatus("current")


class _AgentFAN3_Type(Integer32):
    """Custom type agentFAN3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentFAN3_Type.__name__ = "Integer32"
_AgentFAN3_Object = MibTableColumn
agentFAN3 = _AgentFAN3_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 23),
    _AgentFAN3_Type()
)
agentFAN3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFAN3.setStatus("current")


class _AgentFAN4_Type(Integer32):
    """Custom type agentFAN4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_AgentFAN4_Type.__name__ = "Integer32"
_AgentFAN4_Object = MibTableColumn
agentFAN4 = _AgentFAN4_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 24),
    _AgentFAN4_Type()
)
agentFAN4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFAN4.setStatus("current")
_AgentFANChipType_Type = DisplayString
_AgentFANChipType_Object = MibTableColumn
agentFANChipType = _AgentFANChipType_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 106, 1, 31),
    _AgentFANChipType_Type()
)
agentFANChipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFANChipType.setStatus("current")
_AgentPowerSupplyStatusTable_Object = MibTable
agentPowerSupplyStatusTable = _AgentPowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107)
)
if mibBuilder.loadTexts:
    agentPowerSupplyStatusTable.setStatus("current")
_AgentPowerSupplyStatusEntry_Object = MibTableRow
agentPowerSupplyStatusEntry = _AgentPowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1)
)
agentPowerSupplyStatusEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentPowerSupplyUnitIndex"),
)
if mibBuilder.loadTexts:
    agentPowerSupplyStatusEntry.setStatus("current")


class _AgentPowerSupplyUnitIndex_Type(Integer32):
    """Custom type agentPowerSupplyUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentPowerSupplyUnitIndex_Type.__name__ = "Integer32"
_AgentPowerSupplyUnitIndex_Object = MibTableColumn
agentPowerSupplyUnitIndex = _AgentPowerSupplyUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 1),
    _AgentPowerSupplyUnitIndex_Type()
)
agentPowerSupplyUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyUnitIndex.setStatus("current")


class _AgentPowerSupplyStatus_Type(Integer32):
    """Custom type agentPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notpresent", 3))
    )


_AgentPowerSupplyStatus_Type.__name__ = "Integer32"
_AgentPowerSupplyStatus_Object = MibTableColumn
agentPowerSupplyStatus = _AgentPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 2),
    _AgentPowerSupplyStatus_Type()
)
agentPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyStatus.setStatus("current")
_AgentPowerSupplyName_Type = DisplayString
_AgentPowerSupplyName_Object = MibTableColumn
agentPowerSupplyName = _AgentPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 3),
    _AgentPowerSupplyName_Type()
)
agentPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyName.setStatus("current")
_AgentPowerSupplyModel_Type = DisplayString
_AgentPowerSupplyModel_Object = MibTableColumn
agentPowerSupplyModel = _AgentPowerSupplyModel_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 4),
    _AgentPowerSupplyModel_Type()
)
agentPowerSupplyModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyModel.setStatus("current")
_AgentPowerSupplyRevisionNumber_Type = DisplayString
_AgentPowerSupplyRevisionNumber_Object = MibTableColumn
agentPowerSupplyRevisionNumber = _AgentPowerSupplyRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 5),
    _AgentPowerSupplyRevisionNumber_Type()
)
agentPowerSupplyRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyRevisionNumber.setStatus("current")
_AgentPowerSupplyManufacturerLocation_Type = DisplayString
_AgentPowerSupplyManufacturerLocation_Object = MibTableColumn
agentPowerSupplyManufacturerLocation = _AgentPowerSupplyManufacturerLocation_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 6),
    _AgentPowerSupplyManufacturerLocation_Type()
)
agentPowerSupplyManufacturerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyManufacturerLocation.setStatus("current")
_AgentPowerSupplyManufacturingDate_Type = DisplayString
_AgentPowerSupplyManufacturingDate_Object = MibTableColumn
agentPowerSupplyManufacturingDate = _AgentPowerSupplyManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 7),
    _AgentPowerSupplyManufacturingDate_Type()
)
agentPowerSupplyManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyManufacturingDate.setStatus("current")
_AgentPowerSupplySerialNumber_Type = DisplayString
_AgentPowerSupplySerialNumber_Object = MibTableColumn
agentPowerSupplySerialNumber = _AgentPowerSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 8),
    _AgentPowerSupplySerialNumber_Type()
)
agentPowerSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplySerialNumber.setStatus("current")
_AgentPowerSupplyTemperature1_Type = DisplayString
_AgentPowerSupplyTemperature1_Object = MibTableColumn
agentPowerSupplyTemperature1 = _AgentPowerSupplyTemperature1_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 9),
    _AgentPowerSupplyTemperature1_Type()
)
agentPowerSupplyTemperature1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyTemperature1.setStatus("current")
_AgentPowerSupplyTemperature2_Type = DisplayString
_AgentPowerSupplyTemperature2_Object = MibTableColumn
agentPowerSupplyTemperature2 = _AgentPowerSupplyTemperature2_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 10),
    _AgentPowerSupplyTemperature2_Type()
)
agentPowerSupplyTemperature2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyTemperature2.setStatus("current")
_AgentPowerSupplyFanSpeed_Type = DisplayString
_AgentPowerSupplyFanSpeed_Object = MibTableColumn
agentPowerSupplyFanSpeed = _AgentPowerSupplyFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 11),
    _AgentPowerSupplyFanSpeed_Type()
)
agentPowerSupplyFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyFanSpeed.setStatus("current")
_AgentPowerSupplyFanDuty_Type = Integer32
_AgentPowerSupplyFanDuty_Object = MibTableColumn
agentPowerSupplyFanDuty = _AgentPowerSupplyFanDuty_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 12),
    _AgentPowerSupplyFanDuty_Type()
)
agentPowerSupplyFanDuty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerSupplyFanDuty.setStatus("current")
_AgentPowerConsumption_Type = DisplayString
_AgentPowerConsumption_Object = MibTableColumn
agentPowerConsumption = _AgentPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 107, 1, 13),
    _AgentPowerConsumption_Type()
)
agentPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPowerConsumption.setStatus("current")
_AgentDOMTable_Object = MibTable
agentDOMTable = _AgentDOMTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108)
)
if mibBuilder.loadTexts:
    agentDOMTable.setStatus("current")
_AgentDOMEntry_Object = MibTableRow
agentDOMEntry = _AgentDOMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1)
)
agentDOMEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentDOMtransceiverIndex"),
)
if mibBuilder.loadTexts:
    agentDOMEntry.setStatus("current")


class _AgentDOMtransceiverIndex_Type(Integer32):
    """Custom type agentDOMtransceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentDOMtransceiverIndex_Type.__name__ = "Integer32"
_AgentDOMtransceiverIndex_Object = MibTableColumn
agentDOMtransceiverIndex = _AgentDOMtransceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 1),
    _AgentDOMtransceiverIndex_Type()
)
agentDOMtransceiverIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtransceiverIndex.setStatus("current")
_AgentDOMTemperature_Type = DisplayString
_AgentDOMTemperature_Object = MibTableColumn
agentDOMTemperature = _AgentDOMTemperature_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 2),
    _AgentDOMTemperature_Type()
)
agentDOMTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMTemperature.setStatus("current")
_AgentDOMVoltage_Type = DisplayString
_AgentDOMVoltage_Object = MibTableColumn
agentDOMVoltage = _AgentDOMVoltage_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 3),
    _AgentDOMVoltage_Type()
)
agentDOMVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMVoltage.setStatus("current")
_AgentDOMBias_Type = DisplayString
_AgentDOMBias_Object = MibTableColumn
agentDOMBias = _AgentDOMBias_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 4),
    _AgentDOMBias_Type()
)
agentDOMBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMBias.setStatus("current")
_AgentDOMTxpower_Type = DisplayString
_AgentDOMTxpower_Object = MibTableColumn
agentDOMTxpower = _AgentDOMTxpower_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 5),
    _AgentDOMTxpower_Type()
)
agentDOMTxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMTxpower.setStatus("current")
_AgentDOMRxpower_Type = DisplayString
_AgentDOMRxpower_Object = MibTableColumn
agentDOMRxpower = _AgentDOMRxpower_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 6),
    _AgentDOMRxpower_Type()
)
agentDOMRxpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMRxpower.setStatus("current")
_AgentDOMtemperatureHighAlarm_Type = DisplayString
_AgentDOMtemperatureHighAlarm_Object = MibTableColumn
agentDOMtemperatureHighAlarm = _AgentDOMtemperatureHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 7),
    _AgentDOMtemperatureHighAlarm_Type()
)
agentDOMtemperatureHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtemperatureHighAlarm.setStatus("current")
_AgentDOMtemperatureHighWarning_Type = DisplayString
_AgentDOMtemperatureHighWarning_Object = MibTableColumn
agentDOMtemperatureHighWarning = _AgentDOMtemperatureHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 8),
    _AgentDOMtemperatureHighWarning_Type()
)
agentDOMtemperatureHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtemperatureHighWarning.setStatus("current")
_AgentDOMtemperatureLowWarning_Type = DisplayString
_AgentDOMtemperatureLowWarning_Object = MibTableColumn
agentDOMtemperatureLowWarning = _AgentDOMtemperatureLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 9),
    _AgentDOMtemperatureLowWarning_Type()
)
agentDOMtemperatureLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtemperatureLowWarning.setStatus("current")
_AgentDOMtemperatureLowAlarm_Type = DisplayString
_AgentDOMtemperatureLowAlarm_Object = MibTableColumn
agentDOMtemperatureLowAlarm = _AgentDOMtemperatureLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 10),
    _AgentDOMtemperatureLowAlarm_Type()
)
agentDOMtemperatureLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtemperatureLowAlarm.setStatus("current")
_AgentDOMvotageHighAlarm_Type = DisplayString
_AgentDOMvotageHighAlarm_Object = MibTableColumn
agentDOMvotageHighAlarm = _AgentDOMvotageHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 11),
    _AgentDOMvotageHighAlarm_Type()
)
agentDOMvotageHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMvotageHighAlarm.setStatus("current")
_AgentDOMvotageHighWarning_Type = DisplayString
_AgentDOMvotageHighWarning_Object = MibTableColumn
agentDOMvotageHighWarning = _AgentDOMvotageHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 12),
    _AgentDOMvotageHighWarning_Type()
)
agentDOMvotageHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMvotageHighWarning.setStatus("current")
_AgentDOMvotageLowWarning_Type = DisplayString
_AgentDOMvotageLowWarning_Object = MibTableColumn
agentDOMvotageLowWarning = _AgentDOMvotageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 13),
    _AgentDOMvotageLowWarning_Type()
)
agentDOMvotageLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMvotageLowWarning.setStatus("current")
_AgentDOMvotageLowAlarm_Type = DisplayString
_AgentDOMvotageLowAlarm_Object = MibTableColumn
agentDOMvotageLowAlarm = _AgentDOMvotageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 14),
    _AgentDOMvotageLowAlarm_Type()
)
agentDOMvotageLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMvotageLowAlarm.setStatus("current")
_AgentDOMbiasHighAlarm_Type = DisplayString
_AgentDOMbiasHighAlarm_Object = MibTableColumn
agentDOMbiasHighAlarm = _AgentDOMbiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 15),
    _AgentDOMbiasHighAlarm_Type()
)
agentDOMbiasHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMbiasHighAlarm.setStatus("current")
_AgentDOMbiasHighWarning_Type = DisplayString
_AgentDOMbiasHighWarning_Object = MibTableColumn
agentDOMbiasHighWarning = _AgentDOMbiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 16),
    _AgentDOMbiasHighWarning_Type()
)
agentDOMbiasHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMbiasHighWarning.setStatus("current")
_AgentDOMbiasLowWarning_Type = DisplayString
_AgentDOMbiasLowWarning_Object = MibTableColumn
agentDOMbiasLowWarning = _AgentDOMbiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 17),
    _AgentDOMbiasLowWarning_Type()
)
agentDOMbiasLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMbiasLowWarning.setStatus("current")
_AgentDOMbiasLowAlarm_Type = DisplayString
_AgentDOMbiasLowAlarm_Object = MibTableColumn
agentDOMbiasLowAlarm = _AgentDOMbiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 18),
    _AgentDOMbiasLowAlarm_Type()
)
agentDOMbiasLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMbiasLowAlarm.setStatus("current")
_AgentDOMtxpowerHighAlarm_Type = DisplayString
_AgentDOMtxpowerHighAlarm_Object = MibTableColumn
agentDOMtxpowerHighAlarm = _AgentDOMtxpowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 19),
    _AgentDOMtxpowerHighAlarm_Type()
)
agentDOMtxpowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtxpowerHighAlarm.setStatus("current")
_AgentDOMtxpowerHighWarning_Type = DisplayString
_AgentDOMtxpowerHighWarning_Object = MibTableColumn
agentDOMtxpowerHighWarning = _AgentDOMtxpowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 20),
    _AgentDOMtxpowerHighWarning_Type()
)
agentDOMtxpowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtxpowerHighWarning.setStatus("current")
_AgentDOMtxpowerLowWarning_Type = DisplayString
_AgentDOMtxpowerLowWarning_Object = MibTableColumn
agentDOMtxpowerLowWarning = _AgentDOMtxpowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 21),
    _AgentDOMtxpowerLowWarning_Type()
)
agentDOMtxpowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtxpowerLowWarning.setStatus("current")
_AgentDOMtxpowerLowAlarm_Type = DisplayString
_AgentDOMtxpowerLowAlarm_Object = MibTableColumn
agentDOMtxpowerLowAlarm = _AgentDOMtxpowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 22),
    _AgentDOMtxpowerLowAlarm_Type()
)
agentDOMtxpowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMtxpowerLowAlarm.setStatus("current")
_AgentDOMrxpowerHighAlarm_Type = DisplayString
_AgentDOMrxpowerHighAlarm_Object = MibTableColumn
agentDOMrxpowerHighAlarm = _AgentDOMrxpowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 23),
    _AgentDOMrxpowerHighAlarm_Type()
)
agentDOMrxpowerHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMrxpowerHighAlarm.setStatus("current")
_AgentDOMrxpowerHighWarning_Type = DisplayString
_AgentDOMrxpowerHighWarning_Object = MibTableColumn
agentDOMrxpowerHighWarning = _AgentDOMrxpowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 24),
    _AgentDOMrxpowerHighWarning_Type()
)
agentDOMrxpowerHighWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMrxpowerHighWarning.setStatus("current")
_AgentDOMrxpowerLowWarning_Type = DisplayString
_AgentDOMrxpowerLowWarning_Object = MibTableColumn
agentDOMrxpowerLowWarning = _AgentDOMrxpowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 25),
    _AgentDOMrxpowerLowWarning_Type()
)
agentDOMrxpowerLowWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMrxpowerLowWarning.setStatus("current")
_AgentDOMrxpowerLowAlarm_Type = DisplayString
_AgentDOMrxpowerLowAlarm_Object = MibTableColumn
agentDOMrxpowerLowAlarm = _AgentDOMrxpowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 1, 108, 1, 26),
    _AgentDOMrxpowerLowAlarm_Type()
)
agentDOMrxpowerLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDOMrxpowerLowAlarm.setStatus("current")
_Agent10GModuleInfoGroupExtension_ObjectIdentity = ObjectIdentity
agent10GModuleInfoGroupExtension = _Agent10GModuleInfoGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2)
)
_Agent10GModuleTable_Object = MibTable
agent10GModuleTable = _Agent10GModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107)
)
if mibBuilder.loadTexts:
    agent10GModuleTable.setStatus("current")
_Agent10GModuleEntry_Object = MibTableRow
agent10GModuleEntry = _Agent10GModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1)
)
agent10GModuleEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agent10GModuleUnitIndex"),
    (0, "SWITCHING-EXTENSION-MIB", "agent10GModuleSlotIndex"),
    (0, "SWITCHING-EXTENSION-MIB", "agent10GModulePortIndex"),
)
if mibBuilder.loadTexts:
    agent10GModuleEntry.setStatus("current")


class _Agent10GModuleUnitIndex_Type(Integer32):
    """Custom type agent10GModuleUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Agent10GModuleUnitIndex_Type.__name__ = "Integer32"
_Agent10GModuleUnitIndex_Object = MibTableColumn
agent10GModuleUnitIndex = _Agent10GModuleUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 1),
    _Agent10GModuleUnitIndex_Type()
)
agent10GModuleUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleUnitIndex.setStatus("current")


class _Agent10GModuleSlotIndex_Type(Integer32):
    """Custom type agent10GModuleSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Agent10GModuleSlotIndex_Type.__name__ = "Integer32"
_Agent10GModuleSlotIndex_Object = MibTableColumn
agent10GModuleSlotIndex = _Agent10GModuleSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 2),
    _Agent10GModuleSlotIndex_Type()
)
agent10GModuleSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleSlotIndex.setStatus("current")


class _Agent10GModulePortIndex_Type(Integer32):
    """Custom type agent10GModulePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Agent10GModulePortIndex_Type.__name__ = "Integer32"
_Agent10GModulePortIndex_Object = MibTableColumn
agent10GModulePortIndex = _Agent10GModulePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 3),
    _Agent10GModulePortIndex_Type()
)
agent10GModulePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModulePortIndex.setStatus("current")


class _Agent10GModuleIndex_Type(Integer32):
    """Custom type agent10GModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Agent10GModuleIndex_Type.__name__ = "Integer32"
_Agent10GModuleIndex_Object = MibTableColumn
agent10GModuleIndex = _Agent10GModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 4),
    _Agent10GModuleIndex_Type()
)
agent10GModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleIndex.setStatus("current")


class _Agent10GModuleInterfaceNumber_Type(Integer32):
    """Custom type agent10GModuleInterfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Agent10GModuleInterfaceNumber_Type.__name__ = "Integer32"
_Agent10GModuleInterfaceNumber_Object = MibTableColumn
agent10GModuleInterfaceNumber = _Agent10GModuleInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 5),
    _Agent10GModuleInterfaceNumber_Type()
)
agent10GModuleInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleInterfaceNumber.setStatus("current")
_Agent10GModuleType_Type = DisplayString
_Agent10GModuleType_Object = MibTableColumn
agent10GModuleType = _Agent10GModuleType_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 6),
    _Agent10GModuleType_Type()
)
agent10GModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleType.setStatus("current")
_Agent10GModuleComplianceCode_Type = DisplayString
_Agent10GModuleComplianceCode_Object = MibTableColumn
agent10GModuleComplianceCode = _Agent10GModuleComplianceCode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 7),
    _Agent10GModuleComplianceCode_Type()
)
agent10GModuleComplianceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleComplianceCode.setStatus("current")
_Agent10GModuleVendorName_Type = DisplayString
_Agent10GModuleVendorName_Object = MibTableColumn
agent10GModuleVendorName = _Agent10GModuleVendorName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 8),
    _Agent10GModuleVendorName_Type()
)
agent10GModuleVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleVendorName.setStatus("current")
_Agent10GModulePartNumber_Type = DisplayString
_Agent10GModulePartNumber_Object = MibTableColumn
agent10GModulePartNumber = _Agent10GModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 9),
    _Agent10GModulePartNumber_Type()
)
agent10GModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModulePartNumber.setStatus("current")
_Agent10GModuleSerialNumber_Type = DisplayString
_Agent10GModuleSerialNumber_Object = MibTableColumn
agent10GModuleSerialNumber = _Agent10GModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 10),
    _Agent10GModuleSerialNumber_Type()
)
agent10GModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleSerialNumber.setStatus("current")
_Agent10GModuleRevisionNumber_Type = DisplayString
_Agent10GModuleRevisionNumber_Object = MibTableColumn
agent10GModuleRevisionNumber = _Agent10GModuleRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 11),
    _Agent10GModuleRevisionNumber_Type()
)
agent10GModuleRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleRevisionNumber.setStatus("current")
_Agent10GModuleManufacturingDate_Type = DisplayString
_Agent10GModuleManufacturingDate_Object = MibTableColumn
agent10GModuleManufacturingDate = _Agent10GModuleManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 2, 107, 1, 12),
    _Agent10GModuleManufacturingDate_Type()
)
agent10GModuleManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent10GModuleManufacturingDate.setStatus("current")
_AgentGBICInfoTable_Object = MibTable
agentGBICInfoTable = _AgentGBICInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3)
)
if mibBuilder.loadTexts:
    agentGBICInfoTable.setStatus("current")
_AgentGBICInfoEntry_Object = MibTableRow
agentGBICInfoEntry = _AgentGBICInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1)
)
agentGBICInfoEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentGBICInfoIndex"),
)
if mibBuilder.loadTexts:
    agentGBICInfoEntry.setStatus("current")


class _AgentGBICInfoIndex_Type(Integer32):
    """Custom type agentGBICInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentGBICInfoIndex_Type.__name__ = "Integer32"
_AgentGBICInfoIndex_Object = MibTableColumn
agentGBICInfoIndex = _AgentGBICInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 1),
    _AgentGBICInfoIndex_Type()
)
agentGBICInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoIndex.setStatus("current")
_AgentGBICInfoInterfaceNumber_Type = Integer32
_AgentGBICInfoInterfaceNumber_Object = MibTableColumn
agentGBICInfoInterfaceNumber = _AgentGBICInfoInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 2),
    _AgentGBICInfoInterfaceNumber_Type()
)
agentGBICInfoInterfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoInterfaceNumber.setStatus("current")
_AgentGBICInfoComplianceCode_Type = DisplayString
_AgentGBICInfoComplianceCode_Object = MibTableColumn
agentGBICInfoComplianceCode = _AgentGBICInfoComplianceCode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 3),
    _AgentGBICInfoComplianceCode_Type()
)
agentGBICInfoComplianceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoComplianceCode.setStatus("current")
_AgentGBICInfoVendorName_Type = DisplayString
_AgentGBICInfoVendorName_Object = MibTableColumn
agentGBICInfoVendorName = _AgentGBICInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 4),
    _AgentGBICInfoVendorName_Type()
)
agentGBICInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoVendorName.setStatus("current")
_AgentGBICInfoPartNumber_Type = DisplayString
_AgentGBICInfoPartNumber_Object = MibTableColumn
agentGBICInfoPartNumber = _AgentGBICInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 5),
    _AgentGBICInfoPartNumber_Type()
)
agentGBICInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoPartNumber.setStatus("current")
_AgentGBICInfoSerialNumber_Type = DisplayString
_AgentGBICInfoSerialNumber_Object = MibTableColumn
agentGBICInfoSerialNumber = _AgentGBICInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 6),
    _AgentGBICInfoSerialNumber_Type()
)
agentGBICInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoSerialNumber.setStatus("current")
_AgentGBICInfoRevisionNumber_Type = DisplayString
_AgentGBICInfoRevisionNumber_Object = MibTableColumn
agentGBICInfoRevisionNumber = _AgentGBICInfoRevisionNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 7),
    _AgentGBICInfoRevisionNumber_Type()
)
agentGBICInfoRevisionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoRevisionNumber.setStatus("current")
_AgentGBICInfoManufacturingDate_Type = DisplayString
_AgentGBICInfoManufacturingDate_Object = MibTableColumn
agentGBICInfoManufacturingDate = _AgentGBICInfoManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 1, 3, 1, 8),
    _AgentGBICInfoManufacturingDate_Type()
)
agentGBICInfoManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGBICInfoManufacturingDate.setStatus("current")
_AgentConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentConfigGroupExtension = _AgentConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2)
)
_AgentCLIConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentCLIConfigGroupExtension = _AgentCLIConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1)
)
_AgentSerialGroupExtension_ObjectIdentity = ObjectIdentity
agentSerialGroupExtension = _AgentSerialGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 5)
)


class _AgentSerialPasswdCnt_Type(Integer32):
    """Custom type agentSerialPasswdCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AgentSerialPasswdCnt_Type.__name__ = "Integer32"
_AgentSerialPasswdCnt_Object = MibScalar
agentSerialPasswdCnt = _AgentSerialPasswdCnt_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 5, 100),
    _AgentSerialPasswdCnt_Type()
)
agentSerialPasswdCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialPasswdCnt.setStatus("current")


class _AgentSerialPasswdCntSetToDefault_Type(Integer32):
    """Custom type agentSerialPasswdCntSetToDefault based on Integer32"""
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


_AgentSerialPasswdCntSetToDefault_Type.__name__ = "Integer32"
_AgentSerialPasswdCntSetToDefault_Object = MibScalar
agentSerialPasswdCntSetToDefault = _AgentSerialPasswdCntSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 5, 101),
    _AgentSerialPasswdCntSetToDefault_Type()
)
agentSerialPasswdCntSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialPasswdCntSetToDefault.setStatus("current")


class _AgentSerialSilentTime_Type(Integer32):
    """Custom type agentSerialSilentTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSerialSilentTime_Type.__name__ = "Integer32"
_AgentSerialSilentTime_Object = MibScalar
agentSerialSilentTime = _AgentSerialSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 5, 102),
    _AgentSerialSilentTime_Type()
)
agentSerialSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialSilentTime.setStatus("current")


class _AgentSerialSilentTimeSetToDefault_Type(Integer32):
    """Custom type agentSerialSilentTimeSetToDefault based on Integer32"""
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


_AgentSerialSilentTimeSetToDefault_Type.__name__ = "Integer32"
_AgentSerialSilentTimeSetToDefault_Object = MibScalar
agentSerialSilentTimeSetToDefault = _AgentSerialSilentTimeSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 5, 103),
    _AgentSerialSilentTimeSetToDefault_Type()
)
agentSerialSilentTimeSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSerialSilentTimeSetToDefault.setStatus("current")
_AgentVtyGroupExtension_ObjectIdentity = ObjectIdentity
agentVtyGroupExtension = _AgentVtyGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 6)
)


class _AgentVtyTelnetServerAdminMode_Type(Integer32):
    """Custom type agentVtyTelnetServerAdminMode based on Integer32"""
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


_AgentVtyTelnetServerAdminMode_Type.__name__ = "Integer32"
_AgentVtyTelnetServerAdminMode_Object = MibScalar
agentVtyTelnetServerAdminMode = _AgentVtyTelnetServerAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 6, 103),
    _AgentVtyTelnetServerAdminMode_Type()
)
agentVtyTelnetServerAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVtyTelnetServerAdminMode.setStatus("current")


class _AgentVtyPasswdCnt_Type(Integer32):
    """Custom type agentVtyPasswdCnt based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AgentVtyPasswdCnt_Type.__name__ = "Integer32"
_AgentVtyPasswdCnt_Object = MibScalar
agentVtyPasswdCnt = _AgentVtyPasswdCnt_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 6, 104),
    _AgentVtyPasswdCnt_Type()
)
agentVtyPasswdCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVtyPasswdCnt.setStatus("current")


class _AgentVtyPasswdCntSetToDefault_Type(Integer32):
    """Custom type agentVtyPasswdCntSetToDefault based on Integer32"""
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


_AgentVtyPasswdCntSetToDefault_Type.__name__ = "Integer32"
_AgentVtyPasswdCntSetToDefault_Object = MibScalar
agentVtyPasswdCntSetToDefault = _AgentVtyPasswdCntSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 6, 105),
    _AgentVtyPasswdCntSetToDefault_Type()
)
agentVtyPasswdCntSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVtyPasswdCntSetToDefault.setStatus("current")


class _AgentVtyTerminalLength_Type(Integer32):
    """Custom type agentVtyTerminalLength based on Integer32"""
    defaultValue = 24

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_AgentVtyTerminalLength_Type.__name__ = "Integer32"
_AgentVtyTerminalLength_Object = MibScalar
agentVtyTerminalLength = _AgentVtyTerminalLength_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 6, 106),
    _AgentVtyTerminalLength_Type()
)
agentVtyTerminalLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVtyTerminalLength.setStatus("current")


class _AgentVtyTerminalLengthSetToDefault_Type(Integer32):
    """Custom type agentVtyTerminalLengthSetToDefault based on Integer32"""
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


_AgentVtyTerminalLengthSetToDefault_Type.__name__ = "Integer32"
_AgentVtyTerminalLengthSetToDefault_Object = MibScalar
agentVtyTerminalLengthSetToDefault = _AgentVtyTerminalLengthSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 1, 6, 107),
    _AgentVtyTerminalLengthSetToDefault_Type()
)
agentVtyTerminalLengthSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVtyTerminalLengthSetToDefault.setStatus("current")
_AgentNetworkConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentNetworkConfigGroupExtension = _AgentNetworkConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 3)
)


class _AgentNetworkHttpPort_Type(Integer32):
    """Custom type agentNetworkHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentNetworkHttpPort_Type.__name__ = "Integer32"
_AgentNetworkHttpPort_Object = MibScalar
agentNetworkHttpPort = _AgentNetworkHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 3, 100),
    _AgentNetworkHttpPort_Type()
)
agentNetworkHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkHttpPort.setStatus("current")


class _AgentNetworkDhcpClientIfClientIdFormat_Type(Integer32):
    """Custom type agentNetworkDhcpClientIfClientIdFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hexformat", 1),
          ("textformat", 2))
    )


_AgentNetworkDhcpClientIfClientIdFormat_Type.__name__ = "Integer32"
_AgentNetworkDhcpClientIfClientIdFormat_Object = MibScalar
agentNetworkDhcpClientIfClientIdFormat = _AgentNetworkDhcpClientIfClientIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 3, 101),
    _AgentNetworkDhcpClientIfClientIdFormat_Type()
)
agentNetworkDhcpClientIfClientIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDhcpClientIfClientIdFormat.setStatus("current")


class _AgentNetworkDhcpClientIfClientId_Type(DisplayString):
    """Custom type agentNetworkDhcpClientIfClientId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentNetworkDhcpClientIfClientId_Type.__name__ = "DisplayString"
_AgentNetworkDhcpClientIfClientId_Object = MibScalar
agentNetworkDhcpClientIfClientId = _AgentNetworkDhcpClientIfClientId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 3, 102),
    _AgentNetworkDhcpClientIfClientId_Type()
)
agentNetworkDhcpClientIfClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDhcpClientIfClientId.setStatus("current")


class _AgentNetworkDhcpSetToInventoryClientIfClientId_Type(Integer32):
    """Custom type agentNetworkDhcpSetToInventoryClientIfClientId based on Integer32"""
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


_AgentNetworkDhcpSetToInventoryClientIfClientId_Type.__name__ = "Integer32"
_AgentNetworkDhcpSetToInventoryClientIfClientId_Object = MibScalar
agentNetworkDhcpSetToInventoryClientIfClientId = _AgentNetworkDhcpSetToInventoryClientIfClientId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 3, 103),
    _AgentNetworkDhcpSetToInventoryClientIfClientId_Type()
)
agentNetworkDhcpSetToInventoryClientIfClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDhcpSetToInventoryClientIfClientId.setStatus("current")


class _AgentNetworkDhcpRestart_Type(Integer32):
    """Custom type agentNetworkDhcpRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRestart", 2),
          ("restart", 1))
    )


_AgentNetworkDhcpRestart_Type.__name__ = "Integer32"
_AgentNetworkDhcpRestart_Object = MibScalar
agentNetworkDhcpRestart = _AgentNetworkDhcpRestart_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 3, 104),
    _AgentNetworkDhcpRestart_Type()
)
agentNetworkDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentNetworkDhcpRestart.setStatus("obsolete")
_AgentSwitchConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentSwitchConfigGroupExtension = _AgentSwitchConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8)
)
_AgentSwitchSnoopingGroupExtension_ObjectIdentity = ObjectIdentity
agentSwitchSnoopingGroupExtension = _AgentSwitchSnoopingGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6)
)
_AgentIgmpSnoopL2MulticastStaticTable_Object = MibTable
agentIgmpSnoopL2MulticastStaticTable = _AgentIgmpSnoopL2MulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112)
)
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticTable.setStatus("current")
_AgentIgmpSnoopL2MulticastStaticEntry_Object = MibTableRow
agentIgmpSnoopL2MulticastStaticEntry = _AgentIgmpSnoopL2MulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1)
)
agentIgmpSnoopL2MulticastStaticEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentIgmpSnoopL2MulticastStaticIndex"),
)
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticEntry.setStatus("current")
_AgentIgmpSnoopL2MulticastStaticIndex_Type = Unsigned32
_AgentIgmpSnoopL2MulticastStaticIndex_Object = MibTableColumn
agentIgmpSnoopL2MulticastStaticIndex = _AgentIgmpSnoopL2MulticastStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1, 1),
    _AgentIgmpSnoopL2MulticastStaticIndex_Type()
)
agentIgmpSnoopL2MulticastStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticIndex.setStatus("current")
_AgentIgmpSnoopL2MulticastStaticVlanId_Type = Unsigned32
_AgentIgmpSnoopL2MulticastStaticVlanId_Object = MibTableColumn
agentIgmpSnoopL2MulticastStaticVlanId = _AgentIgmpSnoopL2MulticastStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1, 2),
    _AgentIgmpSnoopL2MulticastStaticVlanId_Type()
)
agentIgmpSnoopL2MulticastStaticVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticVlanId.setStatus("current")
_AgentIgmpSnoopL2MulticastStaticMacAddress_Type = MacAddress
_AgentIgmpSnoopL2MulticastStaticMacAddress_Object = MibTableColumn
agentIgmpSnoopL2MulticastStaticMacAddress = _AgentIgmpSnoopL2MulticastStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1, 3),
    _AgentIgmpSnoopL2MulticastStaticMacAddress_Type()
)
agentIgmpSnoopL2MulticastStaticMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticMacAddress.setStatus("current")


class _AgentIgmpSnoopL2MulticastStaticMemberPortMask_Type(AgentPortMask):
    """Custom type agentIgmpSnoopL2MulticastStaticMemberPortMask based on AgentPortMask"""
    defaultHexValue = "000000000000"


_AgentIgmpSnoopL2MulticastStaticMemberPortMask_Object = MibTableColumn
agentIgmpSnoopL2MulticastStaticMemberPortMask = _AgentIgmpSnoopL2MulticastStaticMemberPortMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1, 4),
    _AgentIgmpSnoopL2MulticastStaticMemberPortMask_Type()
)
agentIgmpSnoopL2MulticastStaticMemberPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticMemberPortMask.setStatus("current")


class _AgentIgmpSnoopL2MulticastStaticActivePortMask_Type(AgentPortMask):
    """Custom type agentIgmpSnoopL2MulticastStaticActivePortMask based on AgentPortMask"""
    defaultHexValue = "000000000000"


_AgentIgmpSnoopL2MulticastStaticActivePortMask_Object = MibTableColumn
agentIgmpSnoopL2MulticastStaticActivePortMask = _AgentIgmpSnoopL2MulticastStaticActivePortMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1, 5),
    _AgentIgmpSnoopL2MulticastStaticActivePortMask_Type()
)
agentIgmpSnoopL2MulticastStaticActivePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticActivePortMask.setStatus("current")


class _AgentIgmpSnoopL2MulticastStaticMemberPorts_Type(OctetString):
    """Custom type agentIgmpSnoopL2MulticastStaticMemberPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentIgmpSnoopL2MulticastStaticMemberPorts_Type.__name__ = "OctetString"
_AgentIgmpSnoopL2MulticastStaticMemberPorts_Object = MibTableColumn
agentIgmpSnoopL2MulticastStaticMemberPorts = _AgentIgmpSnoopL2MulticastStaticMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1, 6),
    _AgentIgmpSnoopL2MulticastStaticMemberPorts_Type()
)
agentIgmpSnoopL2MulticastStaticMemberPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticMemberPorts.setStatus("current")


class _AgentIgmpSnoopL2MulticastStaticActivePorts_Type(OctetString):
    """Custom type agentIgmpSnoopL2MulticastStaticActivePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentIgmpSnoopL2MulticastStaticActivePorts_Type.__name__ = "OctetString"
_AgentIgmpSnoopL2MulticastStaticActivePorts_Object = MibTableColumn
agentIgmpSnoopL2MulticastStaticActivePorts = _AgentIgmpSnoopL2MulticastStaticActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 112, 1, 7),
    _AgentIgmpSnoopL2MulticastStaticActivePorts_Type()
)
agentIgmpSnoopL2MulticastStaticActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIgmpSnoopL2MulticastStaticActivePorts.setStatus("current")
_AgentMldSnoopL2MulticastStaticTable_Object = MibTable
agentMldSnoopL2MulticastStaticTable = _AgentMldSnoopL2MulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113)
)
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticTable.setStatus("current")
_AgentMldSnoopL2MulticastStaticEntry_Object = MibTableRow
agentMldSnoopL2MulticastStaticEntry = _AgentMldSnoopL2MulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1)
)
agentMldSnoopL2MulticastStaticEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentMldSnoopL2MulticastStaticIndex"),
)
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticEntry.setStatus("current")
_AgentMldSnoopL2MulticastStaticIndex_Type = Unsigned32
_AgentMldSnoopL2MulticastStaticIndex_Object = MibTableColumn
agentMldSnoopL2MulticastStaticIndex = _AgentMldSnoopL2MulticastStaticIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1, 1),
    _AgentMldSnoopL2MulticastStaticIndex_Type()
)
agentMldSnoopL2MulticastStaticIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticIndex.setStatus("current")
_AgentMldSnoopL2MulticastStaticVlanId_Type = Unsigned32
_AgentMldSnoopL2MulticastStaticVlanId_Object = MibTableColumn
agentMldSnoopL2MulticastStaticVlanId = _AgentMldSnoopL2MulticastStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1, 2),
    _AgentMldSnoopL2MulticastStaticVlanId_Type()
)
agentMldSnoopL2MulticastStaticVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticVlanId.setStatus("current")
_AgentMldSnoopL2MulticastStaticMacAddress_Type = MacAddress
_AgentMldSnoopL2MulticastStaticMacAddress_Object = MibTableColumn
agentMldSnoopL2MulticastStaticMacAddress = _AgentMldSnoopL2MulticastStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1, 3),
    _AgentMldSnoopL2MulticastStaticMacAddress_Type()
)
agentMldSnoopL2MulticastStaticMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticMacAddress.setStatus("current")


class _AgentMldSnoopL2MulticastStaticMemberPortMask_Type(AgentPortMask):
    """Custom type agentMldSnoopL2MulticastStaticMemberPortMask based on AgentPortMask"""
    defaultHexValue = "000000000000"


_AgentMldSnoopL2MulticastStaticMemberPortMask_Object = MibTableColumn
agentMldSnoopL2MulticastStaticMemberPortMask = _AgentMldSnoopL2MulticastStaticMemberPortMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1, 4),
    _AgentMldSnoopL2MulticastStaticMemberPortMask_Type()
)
agentMldSnoopL2MulticastStaticMemberPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticMemberPortMask.setStatus("current")


class _AgentMldSnoopL2MulticastStaticActivePortMask_Type(AgentPortMask):
    """Custom type agentMldSnoopL2MulticastStaticActivePortMask based on AgentPortMask"""
    defaultHexValue = "000000000000"


_AgentMldSnoopL2MulticastStaticActivePortMask_Object = MibTableColumn
agentMldSnoopL2MulticastStaticActivePortMask = _AgentMldSnoopL2MulticastStaticActivePortMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1, 5),
    _AgentMldSnoopL2MulticastStaticActivePortMask_Type()
)
agentMldSnoopL2MulticastStaticActivePortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticActivePortMask.setStatus("current")


class _AgentMldSnoopL2MulticastStaticMemberPorts_Type(OctetString):
    """Custom type agentMldSnoopL2MulticastStaticMemberPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentMldSnoopL2MulticastStaticMemberPorts_Type.__name__ = "OctetString"
_AgentMldSnoopL2MulticastStaticMemberPorts_Object = MibTableColumn
agentMldSnoopL2MulticastStaticMemberPorts = _AgentMldSnoopL2MulticastStaticMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1, 6),
    _AgentMldSnoopL2MulticastStaticMemberPorts_Type()
)
agentMldSnoopL2MulticastStaticMemberPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticMemberPorts.setStatus("current")


class _AgentMldSnoopL2MulticastStaticActivePorts_Type(OctetString):
    """Custom type agentMldSnoopL2MulticastStaticActivePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentMldSnoopL2MulticastStaticActivePorts_Type.__name__ = "OctetString"
_AgentMldSnoopL2MulticastStaticActivePorts_Object = MibTableColumn
agentMldSnoopL2MulticastStaticActivePorts = _AgentMldSnoopL2MulticastStaticActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 6, 113, 1, 7),
    _AgentMldSnoopL2MulticastStaticActivePorts_Type()
)
agentMldSnoopL2MulticastStaticActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMldSnoopL2MulticastStaticActivePorts.setStatus("current")
_AgentIPFilterConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentIPFilterConfigGroupExtension = _AgentIPFilterConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10)
)


class _AgentIPFilterConfigAdminMode_Type(Integer32):
    """Custom type agentIPFilterConfigAdminMode based on Integer32"""
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


_AgentIPFilterConfigAdminMode_Type.__name__ = "Integer32"
_AgentIPFilterConfigAdminMode_Object = MibScalar
agentIPFilterConfigAdminMode = _AgentIPFilterConfigAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 10),
    _AgentIPFilterConfigAdminMode_Type()
)
agentIPFilterConfigAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIPFilterConfigAdminMode.setStatus("current")
_AgentIpFilterConfigCreate_Type = DisplayString
_AgentIpFilterConfigCreate_Object = MibScalar
agentIpFilterConfigCreate = _AgentIpFilterConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 11),
    _AgentIpFilterConfigCreate_Type()
)
agentIpFilterConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpFilterConfigCreate.setStatus("current")
_AgentIpFilterConfigDelete_Type = DisplayString
_AgentIpFilterConfigDelete_Object = MibScalar
agentIpFilterConfigDelete = _AgentIpFilterConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 12),
    _AgentIpFilterConfigDelete_Type()
)
agentIpFilterConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpFilterConfigDelete.setStatus("current")
_AgentIpFilterConfigTable_Object = MibTable
agentIpFilterConfigTable = _AgentIpFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 30)
)
if mibBuilder.loadTexts:
    agentIpFilterConfigTable.setStatus("current")
_AgentIpFilterConfigEntry_Object = MibTableRow
agentIpFilterConfigEntry = _AgentIpFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 30, 1)
)
agentIpFilterConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentIpFilterConfigIndex"),
)
if mibBuilder.loadTexts:
    agentIpFilterConfigEntry.setStatus("current")


class _AgentIpFilterConfigIndex_Type(Integer32):
    """Custom type agentIpFilterConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentIpFilterConfigIndex_Type.__name__ = "Integer32"
_AgentIpFilterConfigIndex_Object = MibTableColumn
agentIpFilterConfigIndex = _AgentIpFilterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 30, 1, 1),
    _AgentIpFilterConfigIndex_Type()
)
agentIpFilterConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpFilterConfigIndex.setStatus("current")
_AgentIpFilterConfigIP_Type = InetAddress
_AgentIpFilterConfigIP_Object = MibTableColumn
agentIpFilterConfigIP = _AgentIpFilterConfigIP_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 30, 1, 2),
    _AgentIpFilterConfigIP_Type()
)
agentIpFilterConfigIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpFilterConfigIP.setStatus("current")
_AgentIpFilterConfigMask_Type = InetAddress
_AgentIpFilterConfigMask_Object = MibTableColumn
agentIpFilterConfigMask = _AgentIpFilterConfigMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 30, 1, 3),
    _AgentIpFilterConfigMask_Type()
)
agentIpFilterConfigMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpFilterConfigMask.setStatus("current")


class _AgentIpFilterConfigName_Type(DisplayString):
    """Custom type agentIpFilterConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentIpFilterConfigName_Type.__name__ = "DisplayString"
_AgentIpFilterConfigName_Object = MibTableColumn
agentIpFilterConfigName = _AgentIpFilterConfigName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 10, 30, 1, 4),
    _AgentIpFilterConfigName_Type()
)
agentIpFilterConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpFilterConfigName.setStatus("current")
_AgentStormContorlConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentStormContorlConfigGroupExtension = _AgentStormContorlConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18)
)


class _AgentSwitchBroadcastControlMode_Type(Integer32):
    """Custom type agentSwitchBroadcastControlMode based on Integer32"""
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


_AgentSwitchBroadcastControlMode_Type.__name__ = "Integer32"
_AgentSwitchBroadcastControlMode_Object = MibScalar
agentSwitchBroadcastControlMode = _AgentSwitchBroadcastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 1),
    _AgentSwitchBroadcastControlMode_Type()
)
agentSwitchBroadcastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBroadcastControlMode.setStatus("current")


class _AgentSwitchMulticastControlMode_Type(Integer32):
    """Custom type agentSwitchMulticastControlMode based on Integer32"""
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


_AgentSwitchMulticastControlMode_Type.__name__ = "Integer32"
_AgentSwitchMulticastControlMode_Object = MibScalar
agentSwitchMulticastControlMode = _AgentSwitchMulticastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 2),
    _AgentSwitchMulticastControlMode_Type()
)
agentSwitchMulticastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMulticastControlMode.setStatus("current")


class _AgentSwitchUnicastControlMode_Type(Integer32):
    """Custom type agentSwitchUnicastControlMode based on Integer32"""
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


_AgentSwitchUnicastControlMode_Type.__name__ = "Integer32"
_AgentSwitchUnicastControlMode_Object = MibScalar
agentSwitchUnicastControlMode = _AgentSwitchUnicastControlMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 3),
    _AgentSwitchUnicastControlMode_Type()
)
agentSwitchUnicastControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchUnicastControlMode.setStatus("current")


class _AgentSwitchDot3FlowControlMode_Type(Integer32):
    """Custom type agentSwitchDot3FlowControlMode based on Integer32"""
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


_AgentSwitchDot3FlowControlMode_Type.__name__ = "Integer32"
_AgentSwitchDot3FlowControlMode_Object = MibScalar
agentSwitchDot3FlowControlMode = _AgentSwitchDot3FlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 4),
    _AgentSwitchDot3FlowControlMode_Type()
)
agentSwitchDot3FlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchDot3FlowControlMode.setStatus("current")
_AgentSwitchStormControlBroadcastTable_Object = MibTable
agentSwitchStormControlBroadcastTable = _AgentSwitchStormControlBroadcastTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 10)
)
if mibBuilder.loadTexts:
    agentSwitchStormControlBroadcastTable.setStatus("current")
_AgentSwitchStormControlBroadcastEntry_Object = MibTableRow
agentSwitchStormControlBroadcastEntry = _AgentSwitchStormControlBroadcastEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 10, 1)
)
agentSwitchStormControlBroadcastEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentSwitchBcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchStormControlBroadcastEntry.setStatus("current")


class _AgentSwitchBcastStormIfIndex_Type(Integer32):
    """Custom type agentSwitchBcastStormIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchBcastStormIfIndex_Type.__name__ = "Integer32"
_AgentSwitchBcastStormIfIndex_Object = MibTableColumn
agentSwitchBcastStormIfIndex = _AgentSwitchBcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 10, 1, 1),
    _AgentSwitchBcastStormIfIndex_Type()
)
agentSwitchBcastStormIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchBcastStormIfIndex.setStatus("current")


class _AgentSwitchBcastStormExtensionPktRate_Type(Unsigned32):
    """Custom type agentSwitchBcastStormExtensionPktRate based on Unsigned32"""
    defaultValue = 4160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14880000),
    )


_AgentSwitchBcastStormExtensionPktRate_Type.__name__ = "Unsigned32"
_AgentSwitchBcastStormExtensionPktRate_Object = MibTableColumn
agentSwitchBcastStormExtensionPktRate = _AgentSwitchBcastStormExtensionPktRate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 10, 1, 2),
    _AgentSwitchBcastStormExtensionPktRate_Type()
)
agentSwitchBcastStormExtensionPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBcastStormExtensionPktRate.setStatus("current")


class _AgentSwitchBcastStormExtensionAdminMode_Type(Integer32):
    """Custom type agentSwitchBcastStormExtensionAdminMode based on Integer32"""
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


_AgentSwitchBcastStormExtensionAdminMode_Type.__name__ = "Integer32"
_AgentSwitchBcastStormExtensionAdminMode_Object = MibTableColumn
agentSwitchBcastStormExtensionAdminMode = _AgentSwitchBcastStormExtensionAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 10, 1, 3),
    _AgentSwitchBcastStormExtensionAdminMode_Type()
)
agentSwitchBcastStormExtensionAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchBcastStormExtensionAdminMode.setStatus("current")
_AgentSwitchStormControlMulticastTable_Object = MibTable
agentSwitchStormControlMulticastTable = _AgentSwitchStormControlMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 20)
)
if mibBuilder.loadTexts:
    agentSwitchStormControlMulticastTable.setStatus("current")
_AgentSwitchStormControlMulticastEntry_Object = MibTableRow
agentSwitchStormControlMulticastEntry = _AgentSwitchStormControlMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 20, 1)
)
agentSwitchStormControlMulticastEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentSwitchMcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchStormControlMulticastEntry.setStatus("current")


class _AgentSwitchMcastStormIfIndex_Type(Integer32):
    """Custom type agentSwitchMcastStormIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchMcastStormIfIndex_Type.__name__ = "Integer32"
_AgentSwitchMcastStormIfIndex_Object = MibTableColumn
agentSwitchMcastStormIfIndex = _AgentSwitchMcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 20, 1, 1),
    _AgentSwitchMcastStormIfIndex_Type()
)
agentSwitchMcastStormIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMcastStormIfIndex.setStatus("current")


class _AgentSwitchMcastStormExtensionPktRate_Type(Unsigned32):
    """Custom type agentSwitchMcastStormExtensionPktRate based on Unsigned32"""
    defaultValue = 4160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14880000),
    )


_AgentSwitchMcastStormExtensionPktRate_Type.__name__ = "Unsigned32"
_AgentSwitchMcastStormExtensionPktRate_Object = MibTableColumn
agentSwitchMcastStormExtensionPktRate = _AgentSwitchMcastStormExtensionPktRate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 20, 1, 2),
    _AgentSwitchMcastStormExtensionPktRate_Type()
)
agentSwitchMcastStormExtensionPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMcastStormExtensionPktRate.setStatus("current")


class _AgentSwitchMcastStormExtensionAdminMode_Type(Integer32):
    """Custom type agentSwitchMcastStormExtensionAdminMode based on Integer32"""
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


_AgentSwitchMcastStormExtensionAdminMode_Type.__name__ = "Integer32"
_AgentSwitchMcastStormExtensionAdminMode_Object = MibTableColumn
agentSwitchMcastStormExtensionAdminMode = _AgentSwitchMcastStormExtensionAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 20, 1, 3),
    _AgentSwitchMcastStormExtensionAdminMode_Type()
)
agentSwitchMcastStormExtensionAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchMcastStormExtensionAdminMode.setStatus("current")
_AgentSwitchStormControlUnicastTable_Object = MibTable
agentSwitchStormControlUnicastTable = _AgentSwitchStormControlUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 30)
)
if mibBuilder.loadTexts:
    agentSwitchStormControlUnicastTable.setStatus("current")
_AgentSwitchStormControlUnicastEntry_Object = MibTableRow
agentSwitchStormControlUnicastEntry = _AgentSwitchStormControlUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 30, 1)
)
agentSwitchStormControlUnicastEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentSwitchUcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchStormControlUnicastEntry.setStatus("current")


class _AgentSwitchUcastStormIfIndex_Type(Integer32):
    """Custom type agentSwitchUcastStormIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchUcastStormIfIndex_Type.__name__ = "Integer32"
_AgentSwitchUcastStormIfIndex_Object = MibTableColumn
agentSwitchUcastStormIfIndex = _AgentSwitchUcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 30, 1, 1),
    _AgentSwitchUcastStormIfIndex_Type()
)
agentSwitchUcastStormIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchUcastStormIfIndex.setStatus("current")


class _AgentSwitchUcastStormExtensionPktRate_Type(Unsigned32):
    """Custom type agentSwitchUcastStormExtensionPktRate based on Unsigned32"""
    defaultValue = 4160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14880000),
    )


_AgentSwitchUcastStormExtensionPktRate_Type.__name__ = "Unsigned32"
_AgentSwitchUcastStormExtensionPktRate_Object = MibTableColumn
agentSwitchUcastStormExtensionPktRate = _AgentSwitchUcastStormExtensionPktRate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 30, 1, 2),
    _AgentSwitchUcastStormExtensionPktRate_Type()
)
agentSwitchUcastStormExtensionPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchUcastStormExtensionPktRate.setStatus("current")


class _AgentSwitchUcastStormExtensionAdminMode_Type(Integer32):
    """Custom type agentSwitchUcastStormExtensionAdminMode based on Integer32"""
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


_AgentSwitchUcastStormExtensionAdminMode_Type.__name__ = "Integer32"
_AgentSwitchUcastStormExtensionAdminMode_Object = MibTableColumn
agentSwitchUcastStormExtensionAdminMode = _AgentSwitchUcastStormExtensionAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 30, 1, 3),
    _AgentSwitchUcastStormExtensionAdminMode_Type()
)
agentSwitchUcastStormExtensionAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchUcastStormExtensionAdminMode.setStatus("current")
_AgentSwitchFlowControlTable_Object = MibTable
agentSwitchFlowControlTable = _AgentSwitchFlowControlTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 40)
)
if mibBuilder.loadTexts:
    agentSwitchFlowControlTable.setStatus("current")
_AgentSwitchFlowControlEntry_Object = MibTableRow
agentSwitchFlowControlEntry = _AgentSwitchFlowControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 40, 1)
)
agentSwitchFlowControlEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentSwitchFlowControlIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchFlowControlEntry.setStatus("current")


class _AgentSwitchFlowControlIfIndex_Type(Integer32):
    """Custom type agentSwitchFlowControlIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchFlowControlIfIndex_Type.__name__ = "Integer32"
_AgentSwitchFlowControlIfIndex_Object = MibTableColumn
agentSwitchFlowControlIfIndex = _AgentSwitchFlowControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 40, 1, 1),
    _AgentSwitchFlowControlIfIndex_Type()
)
agentSwitchFlowControlIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchFlowControlIfIndex.setStatus("current")


class _AgentSwitchFlowControlAdminMode_Type(Integer32):
    """Custom type agentSwitchFlowControlAdminMode based on Integer32"""
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


_AgentSwitchFlowControlAdminMode_Type.__name__ = "Integer32"
_AgentSwitchFlowControlAdminMode_Object = MibTableColumn
agentSwitchFlowControlAdminMode = _AgentSwitchFlowControlAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 40, 1, 2),
    _AgentSwitchFlowControlAdminMode_Type()
)
agentSwitchFlowControlAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchFlowControlAdminMode.setStatus("current")
_AgentSwitchStormControlActionTable_Object = MibTable
agentSwitchStormControlActionTable = _AgentSwitchStormControlActionTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 50)
)
if mibBuilder.loadTexts:
    agentSwitchStormControlActionTable.setStatus("current")
_AgentSwitchStormControlActionEntry_Object = MibTableRow
agentSwitchStormControlActionEntry = _AgentSwitchStormControlActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 50, 1)
)
agentSwitchStormControlActionEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentSwitchStormControlActionIfIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchStormControlActionEntry.setStatus("current")


class _AgentSwitchStormControlActionIfIndex_Type(Integer32):
    """Custom type agentSwitchStormControlActionIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentSwitchStormControlActionIfIndex_Type.__name__ = "Integer32"
_AgentSwitchStormControlActionIfIndex_Object = MibTableColumn
agentSwitchStormControlActionIfIndex = _AgentSwitchStormControlActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 50, 1, 1),
    _AgentSwitchStormControlActionIfIndex_Type()
)
agentSwitchStormControlActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchStormControlActionIfIndex.setStatus("current")


class _AgentSwitchStormControlActionShutdownMode_Type(Integer32):
    """Custom type agentSwitchStormControlActionShutdownMode based on Integer32"""
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


_AgentSwitchStormControlActionShutdownMode_Type.__name__ = "Integer32"
_AgentSwitchStormControlActionShutdownMode_Object = MibTableColumn
agentSwitchStormControlActionShutdownMode = _AgentSwitchStormControlActionShutdownMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 50, 1, 2),
    _AgentSwitchStormControlActionShutdownMode_Type()
)
agentSwitchStormControlActionShutdownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchStormControlActionShutdownMode.setStatus("current")


class _AgentSwitchStormControlActionTrapMode_Type(Integer32):
    """Custom type agentSwitchStormControlActionTrapMode based on Integer32"""
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


_AgentSwitchStormControlActionTrapMode_Type.__name__ = "Integer32"
_AgentSwitchStormControlActionTrapMode_Object = MibTableColumn
agentSwitchStormControlActionTrapMode = _AgentSwitchStormControlActionTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 18, 50, 1, 3),
    _AgentSwitchStormControlActionTrapMode_Type()
)
agentSwitchStormControlActionTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchStormControlActionTrapMode.setStatus("current")
_AgentErrRecoveryConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentErrRecoveryConfigGroupExtension = _AgentErrRecoveryConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28)
)


class _AgentErrRecoveryInterval_Type(Integer32):
    """Custom type agentErrRecoveryInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_AgentErrRecoveryInterval_Type.__name__ = "Integer32"
_AgentErrRecoveryInterval_Object = MibScalar
agentErrRecoveryInterval = _AgentErrRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 1),
    _AgentErrRecoveryInterval_Type()
)
agentErrRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrRecoveryInterval.setStatus("current")


class _AgentErrRecoveryStormCtrlCauseMode_Type(Integer32):
    """Custom type agentErrRecoveryStormCtrlCauseMode based on Integer32"""
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


_AgentErrRecoveryStormCtrlCauseMode_Type.__name__ = "Integer32"
_AgentErrRecoveryStormCtrlCauseMode_Object = MibScalar
agentErrRecoveryStormCtrlCauseMode = _AgentErrRecoveryStormCtrlCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 2),
    _AgentErrRecoveryStormCtrlCauseMode_Type()
)
agentErrRecoveryStormCtrlCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrRecoveryStormCtrlCauseMode.setStatus("current")


class _AgentErrRecoveryUdldCauseMode_Type(Integer32):
    """Custom type agentErrRecoveryUdldCauseMode based on Integer32"""
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


_AgentErrRecoveryUdldCauseMode_Type.__name__ = "Integer32"
_AgentErrRecoveryUdldCauseMode_Object = MibScalar
agentErrRecoveryUdldCauseMode = _AgentErrRecoveryUdldCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 3),
    _AgentErrRecoveryUdldCauseMode_Type()
)
agentErrRecoveryUdldCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrRecoveryUdldCauseMode.setStatus("current")


class _AgentErrRecoveryPortSecurityCauseMode_Type(Integer32):
    """Custom type agentErrRecoveryPortSecurityCauseMode based on Integer32"""
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


_AgentErrRecoveryPortSecurityCauseMode_Type.__name__ = "Integer32"
_AgentErrRecoveryPortSecurityCauseMode_Object = MibScalar
agentErrRecoveryPortSecurityCauseMode = _AgentErrRecoveryPortSecurityCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 4),
    _AgentErrRecoveryPortSecurityCauseMode_Type()
)
agentErrRecoveryPortSecurityCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrRecoveryPortSecurityCauseMode.setStatus("current")


class _AgentErrRecoveryBpduCauseMode_Type(Integer32):
    """Custom type agentErrRecoveryBpduCauseMode based on Integer32"""
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


_AgentErrRecoveryBpduCauseMode_Type.__name__ = "Integer32"
_AgentErrRecoveryBpduCauseMode_Object = MibScalar
agentErrRecoveryBpduCauseMode = _AgentErrRecoveryBpduCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 5),
    _AgentErrRecoveryBpduCauseMode_Type()
)
agentErrRecoveryBpduCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrRecoveryBpduCauseMode.setStatus("current")


class _AgentErrRecoveryLinkFlapCauseMode_Type(Integer32):
    """Custom type agentErrRecoveryLinkFlapCauseMode based on Integer32"""
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


_AgentErrRecoveryLinkFlapCauseMode_Type.__name__ = "Integer32"
_AgentErrRecoveryLinkFlapCauseMode_Object = MibScalar
agentErrRecoveryLinkFlapCauseMode = _AgentErrRecoveryLinkFlapCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 6),
    _AgentErrRecoveryLinkFlapCauseMode_Type()
)
agentErrRecoveryLinkFlapCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrRecoveryLinkFlapCauseMode.setStatus("current")


class _AgentErrRecoveryMacFlapCauseMode_Type(Integer32):
    """Custom type agentErrRecoveryMacFlapCauseMode based on Integer32"""
    defaultValue = 1

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


_AgentErrRecoveryMacFlapCauseMode_Type.__name__ = "Integer32"
_AgentErrRecoveryMacFlapCauseMode_Object = MibScalar
agentErrRecoveryMacFlapCauseMode = _AgentErrRecoveryMacFlapCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 7),
    _AgentErrRecoveryMacFlapCauseMode_Type()
)
agentErrRecoveryMacFlapCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrRecoveryMacFlapCauseMode.setStatus("current")


class _AgentErrDetectLinkFlapCauseMode_Type(Integer32):
    """Custom type agentErrDetectLinkFlapCauseMode based on Integer32"""
    defaultValue = 1

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


_AgentErrDetectLinkFlapCauseMode_Type.__name__ = "Integer32"
_AgentErrDetectLinkFlapCauseMode_Object = MibScalar
agentErrDetectLinkFlapCauseMode = _AgentErrDetectLinkFlapCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 8),
    _AgentErrDetectLinkFlapCauseMode_Type()
)
agentErrDetectLinkFlapCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrDetectLinkFlapCauseMode.setStatus("current")


class _AgentErrDetectMacFlapCauseMode_Type(Integer32):
    """Custom type agentErrDetectMacFlapCauseMode based on Integer32"""
    defaultValue = 1

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


_AgentErrDetectMacFlapCauseMode_Type.__name__ = "Integer32"
_AgentErrDetectMacFlapCauseMode_Object = MibScalar
agentErrDetectMacFlapCauseMode = _AgentErrDetectMacFlapCauseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 8, 28, 9),
    _AgentErrDetectMacFlapCauseMode_Type()
)
agentErrDetectMacFlapCauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentErrDetectMacFlapCauseMode.setStatus("current")
_AgentTransferConfigGroupExtension_ObjectIdentity = ObjectIdentity
agentTransferConfigGroupExtension = _AgentTransferConfigGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9)
)
_AgentTransferCopyGroup_ObjectIdentity = ObjectIdentity
agentTransferCopyGroup = _AgentTransferCopyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 3)
)


class _AgentTransferCopyRunningConfigToSwitchDestFilename_Type(DisplayString):
    """Custom type agentTransferCopyRunningConfigToSwitchDestFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AgentTransferCopyRunningConfigToSwitchDestFilename_Type.__name__ = "DisplayString"
_AgentTransferCopyRunningConfigToSwitchDestFilename_Object = MibScalar
agentTransferCopyRunningConfigToSwitchDestFilename = _AgentTransferCopyRunningConfigToSwitchDestFilename_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 3, 1),
    _AgentTransferCopyRunningConfigToSwitchDestFilename_Type()
)
agentTransferCopyRunningConfigToSwitchDestFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferCopyRunningConfigToSwitchDestFilename.setStatus("current")


class _AgentTransferCopyRunningConfigStart_Type(Integer32):
    """Custom type agentTransferCopyRunningConfigStart based on Integer32"""
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


_AgentTransferCopyRunningConfigStart_Type.__name__ = "Integer32"
_AgentTransferCopyRunningConfigStart_Object = MibScalar
agentTransferCopyRunningConfigStart = _AgentTransferCopyRunningConfigStart_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 3, 2),
    _AgentTransferCopyRunningConfigStart_Type()
)
agentTransferCopyRunningConfigStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferCopyRunningConfigStart.setStatus("current")


class _AgentTransferCopyRunningConfigStatus_Type(Integer32):
    """Custom type agentTransferCopyRunningConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("noPartitionTableEntry", 15),
          ("runByOtherUsers", 16),
          ("success", 0),
          ("wrongFileType", 4))
    )


_AgentTransferCopyRunningConfigStatus_Type.__name__ = "Integer32"
_AgentTransferCopyRunningConfigStatus_Object = MibScalar
agentTransferCopyRunningConfigStatus = _AgentTransferCopyRunningConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 3, 3),
    _AgentTransferCopyRunningConfigStatus_Type()
)
agentTransferCopyRunningConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferCopyRunningConfigStatus.setStatus("current")
_AgentTransferDeleteGroup_ObjectIdentity = ObjectIdentity
agentTransferDeleteGroup = _AgentTransferDeleteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 4)
)


class _AgentTransferDeleteSwitchFilename_Type(DisplayString):
    """Custom type agentTransferDeleteSwitchFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentTransferDeleteSwitchFilename_Type.__name__ = "DisplayString"
_AgentTransferDeleteSwitchFilename_Object = MibScalar
agentTransferDeleteSwitchFilename = _AgentTransferDeleteSwitchFilename_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 4, 1),
    _AgentTransferDeleteSwitchFilename_Type()
)
agentTransferDeleteSwitchFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDeleteSwitchFilename.setStatus("current")


class _AgentTransferDeleteStart_Type(Integer32):
    """Custom type agentTransferDeleteStart based on Integer32"""
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


_AgentTransferDeleteStart_Type.__name__ = "Integer32"
_AgentTransferDeleteStart_Object = MibScalar
agentTransferDeleteStart = _AgentTransferDeleteStart_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 4, 2),
    _AgentTransferDeleteStart_Type()
)
agentTransferDeleteStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTransferDeleteStart.setStatus("current")


class _AgentTransferDeleteStatus_Type(Integer32):
    """Custom type agentTransferDeleteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("failure", 1),
          ("success", 0))
    )


_AgentTransferDeleteStatus_Type.__name__ = "Integer32"
_AgentTransferDeleteStatus_Object = MibScalar
agentTransferDeleteStatus = _AgentTransferDeleteStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 9, 4, 3),
    _AgentTransferDeleteStatus_Type()
)
agentTransferDeleteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTransferDeleteStatus.setStatus("current")
_AgentPortConfigExtensionTable_Object = MibTable
agentPortConfigExtensionTable = _AgentPortConfigExtensionTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13)
)
if mibBuilder.loadTexts:
    agentPortConfigExtensionTable.setStatus("current")
_AgentPortConfigExtensionEntry_Object = MibTableRow
agentPortConfigExtensionEntry = _AgentPortConfigExtensionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13, 1)
)
agentPortConfigExtensionEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentPortConfigExtensionIfIndex"),
)
if mibBuilder.loadTexts:
    agentPortConfigExtensionEntry.setStatus("current")


class _AgentPortConfigExtensionIfIndex_Type(Integer32):
    """Custom type agentPortConfigExtensionIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentPortConfigExtensionIfIndex_Type.__name__ = "Integer32"
_AgentPortConfigExtensionIfIndex_Object = MibTableColumn
agentPortConfigExtensionIfIndex = _AgentPortConfigExtensionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13, 1, 1),
    _AgentPortConfigExtensionIfIndex_Type()
)
agentPortConfigExtensionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortConfigExtensionIfIndex.setStatus("current")


class _AgentPortConfigExtensionAdminMode_Type(Integer32):
    """Custom type agentPortConfigExtensionAdminMode based on Integer32"""
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


_AgentPortConfigExtensionAdminMode_Type.__name__ = "Integer32"
_AgentPortConfigExtensionAdminMode_Object = MibTableColumn
agentPortConfigExtensionAdminMode = _AgentPortConfigExtensionAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13, 1, 6),
    _AgentPortConfigExtensionAdminMode_Type()
)
agentPortConfigExtensionAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortConfigExtensionAdminMode.setStatus("current")


class _AgentPortConfigExtensionLinkTrapMode_Type(Integer32):
    """Custom type agentPortConfigExtensionLinkTrapMode based on Integer32"""
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


_AgentPortConfigExtensionLinkTrapMode_Type.__name__ = "Integer32"
_AgentPortConfigExtensionLinkTrapMode_Object = MibTableColumn
agentPortConfigExtensionLinkTrapMode = _AgentPortConfigExtensionLinkTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13, 1, 9),
    _AgentPortConfigExtensionLinkTrapMode_Type()
)
agentPortConfigExtensionLinkTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortConfigExtensionLinkTrapMode.setStatus("current")


class _AgentPortConfigExtensionClearStats_Type(Integer32):
    """Custom type agentPortConfigExtensionClearStats based on Integer32"""
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


_AgentPortConfigExtensionClearStats_Type.__name__ = "Integer32"
_AgentPortConfigExtensionClearStats_Object = MibTableColumn
agentPortConfigExtensionClearStats = _AgentPortConfigExtensionClearStats_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13, 1, 10),
    _AgentPortConfigExtensionClearStats_Type()
)
agentPortConfigExtensionClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortConfigExtensionClearStats.setStatus("current")


class _AgentPortConfigExtensionMaxFrameSizeLimit_Type(Integer32):
    """Custom type agentPortConfigExtensionMaxFrameSizeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 12288),
    )


_AgentPortConfigExtensionMaxFrameSizeLimit_Type.__name__ = "Integer32"
_AgentPortConfigExtensionMaxFrameSizeLimit_Object = MibTableColumn
agentPortConfigExtensionMaxFrameSizeLimit = _AgentPortConfigExtensionMaxFrameSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13, 1, 18),
    _AgentPortConfigExtensionMaxFrameSizeLimit_Type()
)
agentPortConfigExtensionMaxFrameSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortConfigExtensionMaxFrameSizeLimit.setStatus("current")


class _AgentPortConfigExtensionMaxFrameSize_Type(Integer32):
    """Custom type agentPortConfigExtensionMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 12288),
    )


_AgentPortConfigExtensionMaxFrameSize_Type.__name__ = "Integer32"
_AgentPortConfigExtensionMaxFrameSize_Object = MibTableColumn
agentPortConfigExtensionMaxFrameSize = _AgentPortConfigExtensionMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 2, 13, 1, 19),
    _AgentPortConfigExtensionMaxFrameSize_Type()
)
agentPortConfigExtensionMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortConfigExtensionMaxFrameSize.setStatus("current")
_AgentLinkStateConfigGroup_ObjectIdentity = ObjectIdentity
agentLinkStateConfigGroup = _AgentLinkStateConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15)
)


class _AgentLinkStateConfigAdminMode_Type(Integer32):
    """Custom type agentLinkStateConfigAdminMode based on Integer32"""
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


_AgentLinkStateConfigAdminMode_Type.__name__ = "Integer32"
_AgentLinkStateConfigAdminMode_Object = MibScalar
agentLinkStateConfigAdminMode = _AgentLinkStateConfigAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 1),
    _AgentLinkStateConfigAdminMode_Type()
)
agentLinkStateConfigAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLinkStateConfigAdminMode.setStatus("current")
_AgentLinkStateGroupTable_Object = MibTable
agentLinkStateGroupTable = _AgentLinkStateGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 2)
)
if mibBuilder.loadTexts:
    agentLinkStateGroupTable.setStatus("current")
_AgentLinkStateGroupEntry_Object = MibTableRow
agentLinkStateGroupEntry = _AgentLinkStateGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 2, 1)
)
agentLinkStateGroupEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentLinkStateGroupId"),
)
if mibBuilder.loadTexts:
    agentLinkStateGroupEntry.setStatus("current")


class _AgentLinkStateGroupId_Type(Integer32):
    """Custom type agentLinkStateGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AgentLinkStateGroupId_Type.__name__ = "Integer32"
_AgentLinkStateGroupId_Object = MibTableColumn
agentLinkStateGroupId = _AgentLinkStateGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 2, 1, 1),
    _AgentLinkStateGroupId_Type()
)
agentLinkStateGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentLinkStateGroupId.setStatus("current")


class _AgentLinkStateGroupMode_Type(Integer32):
    """Custom type agentLinkStateGroupMode based on Integer32"""
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


_AgentLinkStateGroupMode_Type.__name__ = "Integer32"
_AgentLinkStateGroupMode_Object = MibTableColumn
agentLinkStateGroupMode = _AgentLinkStateGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 2, 1, 2),
    _AgentLinkStateGroupMode_Type()
)
agentLinkStateGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLinkStateGroupMode.setStatus("current")
_AgentLinkStateGroupUpstreamPort_Type = DisplayString
_AgentLinkStateGroupUpstreamPort_Object = MibTableColumn
agentLinkStateGroupUpstreamPort = _AgentLinkStateGroupUpstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 2, 1, 3),
    _AgentLinkStateGroupUpstreamPort_Type()
)
agentLinkStateGroupUpstreamPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLinkStateGroupUpstreamPort.setStatus("current")
_AgentLinkStateGroupDownstreamPort_Type = DisplayString
_AgentLinkStateGroupDownstreamPort_Object = MibTableColumn
agentLinkStateGroupDownstreamPort = _AgentLinkStateGroupDownstreamPort_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 2, 1, 4),
    _AgentLinkStateGroupDownstreamPort_Type()
)
agentLinkStateGroupDownstreamPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentLinkStateGroupDownstreamPort.setStatus("current")
_AgentLinkStateGroupStatus_Type = RowStatus
_AgentLinkStateGroupStatus_Object = MibTableColumn
agentLinkStateGroupStatus = _AgentLinkStateGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 15, 2, 1, 5),
    _AgentLinkStateGroupStatus_Type()
)
agentLinkStateGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLinkStateGroupStatus.setStatus("current")
_AgentPortBackupConfigGroup_ObjectIdentity = ObjectIdentity
agentPortBackupConfigGroup = _AgentPortBackupConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16)
)


class _AgentPortBackupConfigAdminMode_Type(Integer32):
    """Custom type agentPortBackupConfigAdminMode based on Integer32"""
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


_AgentPortBackupConfigAdminMode_Type.__name__ = "Integer32"
_AgentPortBackupConfigAdminMode_Object = MibScalar
agentPortBackupConfigAdminMode = _AgentPortBackupConfigAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 1),
    _AgentPortBackupConfigAdminMode_Type()
)
agentPortBackupConfigAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBackupConfigAdminMode.setStatus("current")
_AgentPortBackupGroupTable_Object = MibTable
agentPortBackupGroupTable = _AgentPortBackupGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2)
)
if mibBuilder.loadTexts:
    agentPortBackupGroupTable.setStatus("current")
_AgentPortBackupGroupEntry_Object = MibTableRow
agentPortBackupGroupEntry = _AgentPortBackupGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1)
)
agentPortBackupGroupEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentPortBackupGroupId"),
)
if mibBuilder.loadTexts:
    agentPortBackupGroupEntry.setStatus("current")


class _AgentPortBackupGroupId_Type(Integer32):
    """Custom type agentPortBackupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AgentPortBackupGroupId_Type.__name__ = "Integer32"
_AgentPortBackupGroupId_Object = MibTableColumn
agentPortBackupGroupId = _AgentPortBackupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1, 1),
    _AgentPortBackupGroupId_Type()
)
agentPortBackupGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortBackupGroupId.setStatus("current")


class _AgentPortBackupGroupMode_Type(Integer32):
    """Custom type agentPortBackupGroupMode based on Integer32"""
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


_AgentPortBackupGroupMode_Type.__name__ = "Integer32"
_AgentPortBackupGroupMode_Object = MibTableColumn
agentPortBackupGroupMode = _AgentPortBackupGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1, 2),
    _AgentPortBackupGroupMode_Type()
)
agentPortBackupGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBackupGroupMode.setStatus("current")
_AgentPortBackupGroupActivePort_Type = DisplayString
_AgentPortBackupGroupActivePort_Object = MibTableColumn
agentPortBackupGroupActivePort = _AgentPortBackupGroupActivePort_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1, 3),
    _AgentPortBackupGroupActivePort_Type()
)
agentPortBackupGroupActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBackupGroupActivePort.setStatus("current")
_AgentPortBackupGroupBackupPort_Type = DisplayString
_AgentPortBackupGroupBackupPort_Object = MibTableColumn
agentPortBackupGroupBackupPort = _AgentPortBackupGroupBackupPort_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1, 4),
    _AgentPortBackupGroupBackupPort_Type()
)
agentPortBackupGroupBackupPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBackupGroupBackupPort.setStatus("current")


class _AgentMacMoveUpdatetMode_Type(Integer32):
    """Custom type agentMacMoveUpdatetMode based on Integer32"""
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


_AgentMacMoveUpdatetMode_Type.__name__ = "Integer32"
_AgentMacMoveUpdatetMode_Object = MibTableColumn
agentMacMoveUpdatetMode = _AgentMacMoveUpdatetMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1, 5),
    _AgentMacMoveUpdatetMode_Type()
)
agentMacMoveUpdatetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMacMoveUpdatetMode.setStatus("current")
_AgentPortBackupGroupStatus_Type = RowStatus
_AgentPortBackupGroupStatus_Object = MibTableColumn
agentPortBackupGroupStatus = _AgentPortBackupGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1, 6),
    _AgentPortBackupGroupStatus_Type()
)
agentPortBackupGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentPortBackupGroupStatus.setStatus("current")


class _AgentPortBackupGroupFailBackTime_Type(Integer32):
    """Custom type agentPortBackupGroupFailBackTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AgentPortBackupGroupFailBackTime_Type.__name__ = "Integer32"
_AgentPortBackupGroupFailBackTime_Object = MibTableColumn
agentPortBackupGroupFailBackTime = _AgentPortBackupGroupFailBackTime_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 16, 2, 1, 7),
    _AgentPortBackupGroupFailBackTime_Type()
)
agentPortBackupGroupFailBackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortBackupGroupFailBackTime.setStatus("current")
_AgentDOMGroup_ObjectIdentity = ObjectIdentity
agentDOMGroup = _AgentDOMGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 100)
)


class _AgentDOMAdminMode_Type(Integer32):
    """Custom type agentDOMAdminMode based on Integer32"""
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


_AgentDOMAdminMode_Type.__name__ = "Integer32"
_AgentDOMAdminMode_Object = MibScalar
agentDOMAdminMode = _AgentDOMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 100, 1),
    _AgentDOMAdminMode_Type()
)
agentDOMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDOMAdminMode.setStatus("current")


class _AgentDOMInterval_Type(Integer32):
    """Custom type agentDOMInterval based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 1800),
    )


_AgentDOMInterval_Type.__name__ = "Integer32"
_AgentDOMInterval_Object = MibScalar
agentDOMInterval = _AgentDOMInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 100, 2),
    _AgentDOMInterval_Type()
)
agentDOMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDOMInterval.setStatus("current")
_AgentSwitchCurrBootFilesGroupExtension_ObjectIdentity = ObjectIdentity
agentSwitchCurrBootFilesGroupExtension = _AgentSwitchCurrBootFilesGroupExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103)
)


class _AgentSwitchCurrBootRomFileName_Type(DisplayString):
    """Custom type agentSwitchCurrBootRomFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AgentSwitchCurrBootRomFileName_Type.__name__ = "DisplayString"
_AgentSwitchCurrBootRomFileName_Object = MibScalar
agentSwitchCurrBootRomFileName = _AgentSwitchCurrBootRomFileName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103, 1),
    _AgentSwitchCurrBootRomFileName_Type()
)
agentSwitchCurrBootRomFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCurrBootRomFileName.setStatus("current")
_AgentSwitchCurrBootLoaderFileName_Type = DisplayString
_AgentSwitchCurrBootLoaderFileName_Object = MibScalar
agentSwitchCurrBootLoaderFileName = _AgentSwitchCurrBootLoaderFileName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103, 3),
    _AgentSwitchCurrBootLoaderFileName_Type()
)
agentSwitchCurrBootLoaderFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCurrBootLoaderFileName.setStatus("current")


class _AgentSwitchCurrBootConfigFileName_Type(DisplayString):
    """Custom type agentSwitchCurrBootConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AgentSwitchCurrBootConfigFileName_Type.__name__ = "DisplayString"
_AgentSwitchCurrBootConfigFileName_Object = MibScalar
agentSwitchCurrBootConfigFileName = _AgentSwitchCurrBootConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103, 5),
    _AgentSwitchCurrBootConfigFileName_Type()
)
agentSwitchCurrBootConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCurrBootConfigFileName.setStatus("current")


class _AgentSwitchCurrBootOpCodeFileName_Type(DisplayString):
    """Custom type agentSwitchCurrBootOpCodeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AgentSwitchCurrBootOpCodeFileName_Type.__name__ = "DisplayString"
_AgentSwitchCurrBootOpCodeFileName_Object = MibScalar
agentSwitchCurrBootOpCodeFileName = _AgentSwitchCurrBootOpCodeFileName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103, 7),
    _AgentSwitchCurrBootOpCodeFileName_Type()
)
agentSwitchCurrBootOpCodeFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchCurrBootOpCodeFileName.setStatus("current")
_AgentSwitchCurrUBootFileName_Type = DisplayString
_AgentSwitchCurrUBootFileName_Object = MibScalar
agentSwitchCurrUBootFileName = _AgentSwitchCurrUBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103, 9),
    _AgentSwitchCurrUBootFileName_Type()
)
agentSwitchCurrUBootFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCurrUBootFileName.setStatus("current")
_AgentSwitchCurrKernelFileName_Type = DisplayString
_AgentSwitchCurrKernelFileName_Object = MibScalar
agentSwitchCurrKernelFileName = _AgentSwitchCurrKernelFileName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103, 11),
    _AgentSwitchCurrKernelFileName_Type()
)
agentSwitchCurrKernelFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCurrKernelFileName.setStatus("current")
_AgentSwitchCurrVMTracerFileName_Type = DisplayString
_AgentSwitchCurrVMTracerFileName_Object = MibScalar
agentSwitchCurrVMTracerFileName = _AgentSwitchCurrVMTracerFileName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 103, 12),
    _AgentSwitchCurrVMTracerFileName_Type()
)
agentSwitchCurrVMTracerFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCurrVMTracerFileName.setStatus("current")
_AgentCDPConfigGroup_ObjectIdentity = ObjectIdentity
agentCDPConfigGroup = _AgentCDPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110)
)


class _AgentCDPConfigAdminMode_Type(Integer32):
    """Custom type agentCDPConfigAdminMode based on Integer32"""
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


_AgentCDPConfigAdminMode_Type.__name__ = "Integer32"
_AgentCDPConfigAdminMode_Object = MibScalar
agentCDPConfigAdminMode = _AgentCDPConfigAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 1),
    _AgentCDPConfigAdminMode_Type()
)
agentCDPConfigAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCDPConfigAdminMode.setStatus("current")


class _AgentCDPConfigTimeToLive_Type(Unsigned32):
    """Custom type agentCDPConfigTimeToLive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 255),
    )


_AgentCDPConfigTimeToLive_Type.__name__ = "Unsigned32"
_AgentCDPConfigTimeToLive_Object = MibScalar
agentCDPConfigTimeToLive = _AgentCDPConfigTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 2),
    _AgentCDPConfigTimeToLive_Type()
)
agentCDPConfigTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCDPConfigTimeToLive.setStatus("current")


class _AgentCDPConfigTransmitInterval_Type(Unsigned32):
    """Custom type agentCDPConfigTransmitInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 254),
    )


_AgentCDPConfigTransmitInterval_Type.__name__ = "Unsigned32"
_AgentCDPConfigTransmitInterval_Object = MibScalar
agentCDPConfigTransmitInterval = _AgentCDPConfigTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 3),
    _AgentCDPConfigTransmitInterval_Type()
)
agentCDPConfigTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCDPConfigTransmitInterval.setStatus("current")


class _AgentCDPConfigNumInPkts_Type(Integer32):
    """Custom type agentCDPConfigNumInPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentCDPConfigNumInPkts_Type.__name__ = "Integer32"
_AgentCDPConfigNumInPkts_Object = MibScalar
agentCDPConfigNumInPkts = _AgentCDPConfigNumInPkts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 4),
    _AgentCDPConfigNumInPkts_Type()
)
agentCDPConfigNumInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNumInPkts.setStatus("current")


class _AgentCDPConfigNumOutPkts_Type(Integer32):
    """Custom type agentCDPConfigNumOutPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentCDPConfigNumOutPkts_Type.__name__ = "Integer32"
_AgentCDPConfigNumOutPkts_Object = MibScalar
agentCDPConfigNumOutPkts = _AgentCDPConfigNumOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 5),
    _AgentCDPConfigNumOutPkts_Type()
)
agentCDPConfigNumOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNumOutPkts.setStatus("current")


class _AgentCDPConfigNumErrPkts_Type(Integer32):
    """Custom type agentCDPConfigNumErrPkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentCDPConfigNumErrPkts_Type.__name__ = "Integer32"
_AgentCDPConfigNumErrPkts_Object = MibScalar
agentCDPConfigNumErrPkts = _AgentCDPConfigNumErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 6),
    _AgentCDPConfigNumErrPkts_Type()
)
agentCDPConfigNumErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNumErrPkts.setStatus("current")


class _AgentCDPConfigResetNumPkts_Type(Integer32):
    """Custom type agentCDPConfigResetNumPkts based on Integer32"""
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


_AgentCDPConfigResetNumPkts_Type.__name__ = "Integer32"
_AgentCDPConfigResetNumPkts_Object = MibScalar
agentCDPConfigResetNumPkts = _AgentCDPConfigResetNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 7),
    _AgentCDPConfigResetNumPkts_Type()
)
agentCDPConfigResetNumPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCDPConfigResetNumPkts.setStatus("current")


class _AgentCDPConfigResetDeviceInformation_Type(Integer32):
    """Custom type agentCDPConfigResetDeviceInformation based on Integer32"""
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


_AgentCDPConfigResetDeviceInformation_Type.__name__ = "Integer32"
_AgentCDPConfigResetDeviceInformation_Object = MibScalar
agentCDPConfigResetDeviceInformation = _AgentCDPConfigResetDeviceInformation_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 8),
    _AgentCDPConfigResetDeviceInformation_Type()
)
agentCDPConfigResetDeviceInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCDPConfigResetDeviceInformation.setStatus("current")
_AgentCDPConfigPortModeTable_Object = MibTable
agentCDPConfigPortModeTable = _AgentCDPConfigPortModeTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 10)
)
if mibBuilder.loadTexts:
    agentCDPConfigPortModeTable.setStatus("current")
_AgentCDPConfigPortModeEntry_Object = MibTableRow
agentCDPConfigPortModeEntry = _AgentCDPConfigPortModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 10, 1)
)
agentCDPConfigPortModeEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentCDPConfigPortModeIfIndex"),
)
if mibBuilder.loadTexts:
    agentCDPConfigPortModeEntry.setStatus("current")


class _AgentCDPConfigPortModeIfIndex_Type(Integer32):
    """Custom type agentCDPConfigPortModeIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentCDPConfigPortModeIfIndex_Type.__name__ = "Integer32"
_AgentCDPConfigPortModeIfIndex_Object = MibTableColumn
agentCDPConfigPortModeIfIndex = _AgentCDPConfigPortModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 10, 1, 1),
    _AgentCDPConfigPortModeIfIndex_Type()
)
agentCDPConfigPortModeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigPortModeIfIndex.setStatus("current")


class _AgentCDPConfigPortModeAdminMode_Type(Integer32):
    """Custom type agentCDPConfigPortModeAdminMode based on Integer32"""
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


_AgentCDPConfigPortModeAdminMode_Type.__name__ = "Integer32"
_AgentCDPConfigPortModeAdminMode_Object = MibTableColumn
agentCDPConfigPortModeAdminMode = _AgentCDPConfigPortModeAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 10, 1, 2),
    _AgentCDPConfigPortModeAdminMode_Type()
)
agentCDPConfigPortModeAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCDPConfigPortModeAdminMode.setStatus("current")
_AgentCDPConfigNeighborInfoTable_Object = MibTable
agentCDPConfigNeighborInfoTable = _AgentCDPConfigNeighborInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20)
)
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoTable.setStatus("current")
_AgentCDPConfigNeighborInfoEntry_Object = MibTableRow
agentCDPConfigNeighborInfoEntry = _AgentCDPConfigNeighborInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1)
)
agentCDPConfigNeighborInfoEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentCDPConfigNeighborInfoIndex"),
)
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoEntry.setStatus("current")


class _AgentCDPConfigNeighborInfoIndex_Type(Integer32):
    """Custom type agentCDPConfigNeighborInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentCDPConfigNeighborInfoIndex_Type.__name__ = "Integer32"
_AgentCDPConfigNeighborInfoIndex_Object = MibTableColumn
agentCDPConfigNeighborInfoIndex = _AgentCDPConfigNeighborInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 1),
    _AgentCDPConfigNeighborInfoIndex_Type()
)
agentCDPConfigNeighborInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoIndex.setStatus("current")
_AgentCDPConfigNeighborInfoDeviceID_Type = DisplayString
_AgentCDPConfigNeighborInfoDeviceID_Object = MibTableColumn
agentCDPConfigNeighborInfoDeviceID = _AgentCDPConfigNeighborInfoDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 2),
    _AgentCDPConfigNeighborInfoDeviceID_Type()
)
agentCDPConfigNeighborInfoDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoDeviceID.setStatus("current")


class _AgentCDPConfigNeighborInfoLocalIF_Type(Integer32):
    """Custom type agentCDPConfigNeighborInfoLocalIF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentCDPConfigNeighborInfoLocalIF_Type.__name__ = "Integer32"
_AgentCDPConfigNeighborInfoLocalIF_Object = MibTableColumn
agentCDPConfigNeighborInfoLocalIF = _AgentCDPConfigNeighborInfoLocalIF_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 3),
    _AgentCDPConfigNeighborInfoLocalIF_Type()
)
agentCDPConfigNeighborInfoLocalIF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoLocalIF.setStatus("current")


class _AgentCDPConfigNeighborInfoHoldTime_Type(Integer32):
    """Custom type agentCDPConfigNeighborInfoHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentCDPConfigNeighborInfoHoldTime_Type.__name__ = "Integer32"
_AgentCDPConfigNeighborInfoHoldTime_Object = MibTableColumn
agentCDPConfigNeighborInfoHoldTime = _AgentCDPConfigNeighborInfoHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 4),
    _AgentCDPConfigNeighborInfoHoldTime_Type()
)
agentCDPConfigNeighborInfoHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoHoldTime.setStatus("current")
_AgentCDPConfigNeighborInfoCapability_Type = DisplayString
_AgentCDPConfigNeighborInfoCapability_Object = MibTableColumn
agentCDPConfigNeighborInfoCapability = _AgentCDPConfigNeighborInfoCapability_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 5),
    _AgentCDPConfigNeighborInfoCapability_Type()
)
agentCDPConfigNeighborInfoCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoCapability.setStatus("current")
_AgentCDPConfigNeighborInfoPlatform_Type = DisplayString
_AgentCDPConfigNeighborInfoPlatform_Object = MibTableColumn
agentCDPConfigNeighborInfoPlatform = _AgentCDPConfigNeighborInfoPlatform_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 6),
    _AgentCDPConfigNeighborInfoPlatform_Type()
)
agentCDPConfigNeighborInfoPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoPlatform.setStatus("current")
_AgentCDPConfigNeighborInfoPortID_Type = DisplayString
_AgentCDPConfigNeighborInfoPortID_Object = MibTableColumn
agentCDPConfigNeighborInfoPortID = _AgentCDPConfigNeighborInfoPortID_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 7),
    _AgentCDPConfigNeighborInfoPortID_Type()
)
agentCDPConfigNeighborInfoPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoPortID.setStatus("current")
_AgentCDPConfigNeighborInfoManagementAddress_Type = IpAddress
_AgentCDPConfigNeighborInfoManagementAddress_Object = MibTableColumn
agentCDPConfigNeighborInfoManagementAddress = _AgentCDPConfigNeighborInfoManagementAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 110, 20, 1, 8),
    _AgentCDPConfigNeighborInfoManagementAddress_Type()
)
agentCDPConfigNeighborInfoManagementAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCDPConfigNeighborInfoManagementAddress.setStatus("current")
_AgentVlanVoiceConfigGroup_ObjectIdentity = ObjectIdentity
agentVlanVoiceConfigGroup = _AgentVlanVoiceConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111)
)


class _AgentVlanVoiceVlanIDCreate_Type(Integer32):
    """Custom type agentVlanVoiceVlanIDCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_AgentVlanVoiceVlanIDCreate_Type.__name__ = "Integer32"
_AgentVlanVoiceVlanIDCreate_Object = MibScalar
agentVlanVoiceVlanIDCreate = _AgentVlanVoiceVlanIDCreate_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 1),
    _AgentVlanVoiceVlanIDCreate_Type()
)
agentVlanVoiceVlanIDCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVlanVoiceVlanIDCreate.setStatus("current")


class _AgentVlanVoiceAdminMode_Type(Integer32):
    """Custom type agentVlanVoiceAdminMode based on Integer32"""
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


_AgentVlanVoiceAdminMode_Type.__name__ = "Integer32"
_AgentVlanVoiceAdminMode_Object = MibScalar
agentVlanVoiceAdminMode = _AgentVlanVoiceAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 2),
    _AgentVlanVoiceAdminMode_Type()
)
agentVlanVoiceAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVlanVoiceAdminMode.setStatus("current")
_AgentVlanVoiceMacAddress_Type = DisplayString
_AgentVlanVoiceMacAddress_Object = MibScalar
agentVlanVoiceMacAddress = _AgentVlanVoiceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 3),
    _AgentVlanVoiceMacAddress_Type()
)
agentVlanVoiceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVlanVoiceMacAddress.setStatus("current")


class _AgentVlanVoiceMacMask_Type(Integer32):
    """Custom type agentVlanVoiceMacMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
        ValueRangeConstraint(254, 254),
        ValueRangeConstraint(255, 255),
    )


_AgentVlanVoiceMacMask_Type.__name__ = "Integer32"
_AgentVlanVoiceMacMask_Object = MibScalar
agentVlanVoiceMacMask = _AgentVlanVoiceMacMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 4),
    _AgentVlanVoiceMacMask_Type()
)
agentVlanVoiceMacMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVlanVoiceMacMask.setStatus("current")


class _AgentVlanVoicePriority_Type(Integer32):
    """Custom type agentVlanVoicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentVlanVoicePriority_Type.__name__ = "Integer32"
_AgentVlanVoicePriority_Object = MibScalar
agentVlanVoicePriority = _AgentVlanVoicePriority_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 5),
    _AgentVlanVoicePriority_Type()
)
agentVlanVoicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVlanVoicePriority.setStatus("current")
_AgentVlanVoiceName_Type = DisplayString
_AgentVlanVoiceName_Object = MibScalar
agentVlanVoiceName = _AgentVlanVoiceName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 6),
    _AgentVlanVoiceName_Type()
)
agentVlanVoiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVlanVoiceName.setStatus("current")
_AgentVlanVoiceConfigTable_Object = MibTable
agentVlanVoiceConfigTable = _AgentVlanVoiceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7)
)
if mibBuilder.loadTexts:
    agentVlanVoiceConfigTable.setStatus("current")
_AgentVlanVoiceConfigEntry_Object = MibTableRow
agentVlanVoiceConfigEntry = _AgentVlanVoiceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7, 1)
)
agentVlanVoiceConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentVlanVoiceConfigIndex"),
)
if mibBuilder.loadTexts:
    agentVlanVoiceConfigEntry.setStatus("current")


class _AgentVlanVoiceConfigIndex_Type(Integer32):
    """Custom type agentVlanVoiceConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentVlanVoiceConfigIndex_Type.__name__ = "Integer32"
_AgentVlanVoiceConfigIndex_Object = MibTableColumn
agentVlanVoiceConfigIndex = _AgentVlanVoiceConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7, 1, 1),
    _AgentVlanVoiceConfigIndex_Type()
)
agentVlanVoiceConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVlanVoiceConfigIndex.setStatus("current")
_AgentVlanVoiceConfigName_Type = DisplayString
_AgentVlanVoiceConfigName_Object = MibTableColumn
agentVlanVoiceConfigName = _AgentVlanVoiceConfigName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7, 1, 2),
    _AgentVlanVoiceConfigName_Type()
)
agentVlanVoiceConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVlanVoiceConfigName.setStatus("current")
_AgentVlanVoiceConfigMacAddress_Type = DisplayString
_AgentVlanVoiceConfigMacAddress_Object = MibTableColumn
agentVlanVoiceConfigMacAddress = _AgentVlanVoiceConfigMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7, 1, 3),
    _AgentVlanVoiceConfigMacAddress_Type()
)
agentVlanVoiceConfigMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVlanVoiceConfigMacAddress.setStatus("current")


class _AgentVlanVoiceConfigMacMask_Type(Integer32):
    """Custom type agentVlanVoiceConfigMacMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(192, 192),
        ValueRangeConstraint(224, 224),
        ValueRangeConstraint(240, 240),
        ValueRangeConstraint(248, 248),
        ValueRangeConstraint(252, 252),
        ValueRangeConstraint(254, 254),
        ValueRangeConstraint(255, 255),
    )


_AgentVlanVoiceConfigMacMask_Type.__name__ = "Integer32"
_AgentVlanVoiceConfigMacMask_Object = MibTableColumn
agentVlanVoiceConfigMacMask = _AgentVlanVoiceConfigMacMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7, 1, 4),
    _AgentVlanVoiceConfigMacMask_Type()
)
agentVlanVoiceConfigMacMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVlanVoiceConfigMacMask.setStatus("current")


class _AgentVlanVoiceConfigPriority_Type(Integer32):
    """Custom type agentVlanVoiceConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AgentVlanVoiceConfigPriority_Type.__name__ = "Integer32"
_AgentVlanVoiceConfigPriority_Object = MibTableColumn
agentVlanVoiceConfigPriority = _AgentVlanVoiceConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7, 1, 5),
    _AgentVlanVoiceConfigPriority_Type()
)
agentVlanVoiceConfigPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVlanVoiceConfigPriority.setStatus("current")


class _AgentVlanVoiceConfigDelete_Type(Integer32):
    """Custom type agentVlanVoiceConfigDelete based on Integer32"""
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


_AgentVlanVoiceConfigDelete_Type.__name__ = "Integer32"
_AgentVlanVoiceConfigDelete_Object = MibTableColumn
agentVlanVoiceConfigDelete = _AgentVlanVoiceConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 111, 7, 1, 6),
    _AgentVlanVoiceConfigDelete_Type()
)
agentVlanVoiceConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVlanVoiceConfigDelete.setStatus("current")
_AgentVoiceVlanConfigGroup_ObjectIdentity = ObjectIdentity
agentVoiceVlanConfigGroup = _AgentVoiceVlanConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114)
)


class _AgentVoiceVlanAdminMode_Type(Integer32):
    """Custom type agentVoiceVlanAdminMode based on Integer32"""
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


_AgentVoiceVlanAdminMode_Type.__name__ = "Integer32"
_AgentVoiceVlanAdminMode_Object = MibScalar
agentVoiceVlanAdminMode = _AgentVoiceVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 1),
    _AgentVoiceVlanAdminMode_Type()
)
agentVoiceVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVoiceVlanAdminMode.setStatus("current")
_AgentVoiceVlanConfigTable_Object = MibTable
agentVoiceVlanConfigTable = _AgentVoiceVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 2)
)
if mibBuilder.loadTexts:
    agentVoiceVlanConfigTable.setStatus("current")
_AgentVoiceVlanConfigEntry_Object = MibTableRow
agentVoiceVlanConfigEntry = _AgentVoiceVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 2, 1)
)
agentVoiceVlanConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentVoiceVlanConfigIndex"),
)
if mibBuilder.loadTexts:
    agentVoiceVlanConfigEntry.setStatus("current")


class _AgentVoiceVlanConfigIndex_Type(Integer32):
    """Custom type agentVoiceVlanConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4093),
    )


_AgentVoiceVlanConfigIndex_Type.__name__ = "Integer32"
_AgentVoiceVlanConfigIndex_Object = MibTableColumn
agentVoiceVlanConfigIndex = _AgentVoiceVlanConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 2, 1, 1),
    _AgentVoiceVlanConfigIndex_Type()
)
agentVoiceVlanConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVoiceVlanConfigIndex.setStatus("current")


class _AgentVoiceVlanConfigIfMode_Type(Integer32):
    """Custom type agentVoiceVlanConfigIfMode based on Integer32"""
    defaultValue = 0

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
        *(("disable", 0),
          ("dot1p", 2),
          ("none", 3),
          ("untagged", 4),
          ("vlanid", 1))
    )


_AgentVoiceVlanConfigIfMode_Type.__name__ = "Integer32"
_AgentVoiceVlanConfigIfMode_Object = MibTableColumn
agentVoiceVlanConfigIfMode = _AgentVoiceVlanConfigIfMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 2, 1, 2),
    _AgentVoiceVlanConfigIfMode_Type()
)
agentVoiceVlanConfigIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVoiceVlanConfigIfMode.setStatus("current")


class _AgentVoiceVlanConfigIfModeValue_Type(Integer32):
    """Custom type agentVoiceVlanConfigIfModeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentVoiceVlanConfigIfModeValue_Type.__name__ = "Integer32"
_AgentVoiceVlanConfigIfModeValue_Object = MibTableColumn
agentVoiceVlanConfigIfModeValue = _AgentVoiceVlanConfigIfModeValue_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 2, 1, 3),
    _AgentVoiceVlanConfigIfModeValue_Type()
)
agentVoiceVlanConfigIfModeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVoiceVlanConfigIfModeValue.setStatus("current")


class _AgentVoiceVlanConfigCosOverrideMode_Type(Integer32):
    """Custom type agentVoiceVlanConfigCosOverrideMode based on Integer32"""
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


_AgentVoiceVlanConfigCosOverrideMode_Type.__name__ = "Integer32"
_AgentVoiceVlanConfigCosOverrideMode_Object = MibTableColumn
agentVoiceVlanConfigCosOverrideMode = _AgentVoiceVlanConfigCosOverrideMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 2, 1, 4),
    _AgentVoiceVlanConfigCosOverrideMode_Type()
)
agentVoiceVlanConfigCosOverrideMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVoiceVlanConfigCosOverrideMode.setStatus("current")


class _AgentVoiceVlanConfigOperState_Type(Integer32):
    """Custom type agentVoiceVlanConfigOperState based on Integer32"""
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


_AgentVoiceVlanConfigOperState_Type.__name__ = "Integer32"
_AgentVoiceVlanConfigOperState_Object = MibTableColumn
agentVoiceVlanConfigOperState = _AgentVoiceVlanConfigOperState_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 114, 2, 1, 5),
    _AgentVoiceVlanConfigOperState_Type()
)
agentVoiceVlanConfigOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVoiceVlanConfigOperState.setStatus("current")
_AgentVTPConfigGroup_ObjectIdentity = ObjectIdentity
agentVTPConfigGroup = _AgentVTPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115)
)


class _AgentVTPAdminMode_Type(Integer32):
    """Custom type agentVTPAdminMode based on Integer32"""
    defaultValue = 1

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


_AgentVTPAdminMode_Type.__name__ = "Integer32"
_AgentVTPAdminMode_Object = MibScalar
agentVTPAdminMode = _AgentVTPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 1),
    _AgentVTPAdminMode_Type()
)
agentVTPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVTPAdminMode.setStatus("current")


class _AgentVTPVersion_Type(Integer32):
    """Custom type agentVTPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentVTPVersion_Type.__name__ = "Integer32"
_AgentVTPVersion_Object = MibScalar
agentVTPVersion = _AgentVTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 2),
    _AgentVTPVersion_Type()
)
agentVTPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVTPVersion.setStatus("current")


class _AgentVTPConfigRevision_Type(Integer32):
    """Custom type agentVTPConfigRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentVTPConfigRevision_Type.__name__ = "Integer32"
_AgentVTPConfigRevision_Object = MibScalar
agentVTPConfigRevision = _AgentVTPConfigRevision_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 3),
    _AgentVTPConfigRevision_Type()
)
agentVTPConfigRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVTPConfigRevision.setStatus("current")


class _AgentVTPMaxVlanNumSupported_Type(Integer32):
    """Custom type agentVTPMaxVlanNumSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentVTPMaxVlanNumSupported_Type.__name__ = "Integer32"
_AgentVTPMaxVlanNumSupported_Object = MibScalar
agentVTPMaxVlanNumSupported = _AgentVTPMaxVlanNumSupported_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 4),
    _AgentVTPMaxVlanNumSupported_Type()
)
agentVTPMaxVlanNumSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVTPMaxVlanNumSupported.setStatus("current")


class _AgentVTPVlanNumSupported_Type(Integer32):
    """Custom type agentVTPVlanNumSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentVTPVlanNumSupported_Type.__name__ = "Integer32"
_AgentVTPVlanNumSupported_Object = MibScalar
agentVTPVlanNumSupported = _AgentVTPVlanNumSupported_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 5),
    _AgentVTPVlanNumSupported_Type()
)
agentVTPVlanNumSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVTPVlanNumSupported.setStatus("current")


class _AgentVTPOperatingMode_Type(Integer32):
    """Custom type agentVTPOperatingMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 0),
          ("transparent", 2))
    )


_AgentVTPOperatingMode_Type.__name__ = "Integer32"
_AgentVTPOperatingMode_Object = MibScalar
agentVTPOperatingMode = _AgentVTPOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 6),
    _AgentVTPOperatingMode_Type()
)
agentVTPOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVTPOperatingMode.setStatus("current")


class _AgentVTPDomainName_Type(DisplayString):
    """Custom type agentVTPDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentVTPDomainName_Type.__name__ = "DisplayString"
_AgentVTPDomainName_Object = MibScalar
agentVTPDomainName = _AgentVTPDomainName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 7),
    _AgentVTPDomainName_Type()
)
agentVTPDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVTPDomainName.setStatus("current")


class _AgentVTPPruningMode_Type(Integer32):
    """Custom type agentVTPPruningMode based on Integer32"""
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


_AgentVTPPruningMode_Type.__name__ = "Integer32"
_AgentVTPPruningMode_Object = MibScalar
agentVTPPruningMode = _AgentVTPPruningMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 8),
    _AgentVTPPruningMode_Type()
)
agentVTPPruningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVTPPruningMode.setStatus("current")


class _AgentVTPDomainPassword_Type(DisplayString):
    """Custom type agentVTPDomainPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentVTPDomainPassword_Type.__name__ = "DisplayString"
_AgentVTPDomainPassword_Object = MibScalar
agentVTPDomainPassword = _AgentVTPDomainPassword_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 9),
    _AgentVTPDomainPassword_Type()
)
agentVTPDomainPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVTPDomainPassword.setStatus("current")


class _AgentVTPV2Mode_Type(Integer32):
    """Custom type agentVTPV2Mode based on Integer32"""
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


_AgentVTPV2Mode_Type.__name__ = "Integer32"
_AgentVTPV2Mode_Object = MibScalar
agentVTPV2Mode = _AgentVTPV2Mode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 10),
    _AgentVTPV2Mode_Type()
)
agentVTPV2Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVTPV2Mode.setStatus("current")


class _AgentVTPMD5Digest_Type(DisplayString):
    """Custom type agentVTPMD5Digest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentVTPMD5Digest_Type.__name__ = "DisplayString"
_AgentVTPMD5Digest_Object = MibScalar
agentVTPMD5Digest = _AgentVTPMD5Digest_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 11),
    _AgentVTPMD5Digest_Type()
)
agentVTPMD5Digest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVTPMD5Digest.setStatus("current")


class _AgentVTPConfigLastModified_Type(DisplayString):
    """Custom type agentVTPConfigLastModified based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentVTPConfigLastModified_Type.__name__ = "DisplayString"
_AgentVTPConfigLastModified_Object = MibScalar
agentVTPConfigLastModified = _AgentVTPConfigLastModified_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 12),
    _AgentVTPConfigLastModified_Type()
)
agentVTPConfigLastModified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVTPConfigLastModified.setStatus("current")


class _AgentVTPLocalUpdaterID_Type(DisplayString):
    """Custom type agentVTPLocalUpdaterID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentVTPLocalUpdaterID_Type.__name__ = "DisplayString"
_AgentVTPLocalUpdaterID_Object = MibScalar
agentVTPLocalUpdaterID = _AgentVTPLocalUpdaterID_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 13),
    _AgentVTPLocalUpdaterID_Type()
)
agentVTPLocalUpdaterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVTPLocalUpdaterID.setStatus("current")
_AgentVTPPortConfigTable_Object = MibTable
agentVTPPortConfigTable = _AgentVTPPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 14)
)
if mibBuilder.loadTexts:
    agentVTPPortConfigTable.setStatus("current")
_AgentVTPPortConfigEntry_Object = MibTableRow
agentVTPPortConfigEntry = _AgentVTPPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 14, 1)
)
agentVTPPortConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentVTPPortConfigIndex"),
)
if mibBuilder.loadTexts:
    agentVTPPortConfigEntry.setStatus("current")


class _AgentVTPPortConfigIndex_Type(Integer32):
    """Custom type agentVTPPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentVTPPortConfigIndex_Type.__name__ = "Integer32"
_AgentVTPPortConfigIndex_Object = MibTableColumn
agentVTPPortConfigIndex = _AgentVTPPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 14, 1, 1),
    _AgentVTPPortConfigIndex_Type()
)
agentVTPPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentVTPPortConfigIndex.setStatus("current")


class _AgentVTPPortConfigTrunkMode_Type(Integer32):
    """Custom type agentVTPPortConfigTrunkMode based on Integer32"""
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


_AgentVTPPortConfigTrunkMode_Type.__name__ = "Integer32"
_AgentVTPPortConfigTrunkMode_Object = MibTableColumn
agentVTPPortConfigTrunkMode = _AgentVTPPortConfigTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 115, 14, 1, 2),
    _AgentVTPPortConfigTrunkMode_Type()
)
agentVTPPortConfigTrunkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVTPPortConfigTrunkMode.setStatus("current")
_AgentFIPSnoopingGroup_ObjectIdentity = ObjectIdentity
agentFIPSnoopingGroup = _AgentFIPSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116)
)


class _AgentFIPSnoopingAdminMode_Type(Integer32):
    """Custom type agentFIPSnoopingAdminMode based on Integer32"""
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


_AgentFIPSnoopingAdminMode_Type.__name__ = "Integer32"
_AgentFIPSnoopingAdminMode_Object = MibScalar
agentFIPSnoopingAdminMode = _AgentFIPSnoopingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 1),
    _AgentFIPSnoopingAdminMode_Type()
)
agentFIPSnoopingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFIPSnoopingAdminMode.setStatus("current")
_AgentFIPSnoopingVlanConfigTable_Object = MibTable
agentFIPSnoopingVlanConfigTable = _AgentFIPSnoopingVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 2)
)
if mibBuilder.loadTexts:
    agentFIPSnoopingVlanConfigTable.setStatus("current")
_AgentFIPSnoopingVlanConfigEntry_Object = MibTableRow
agentFIPSnoopingVlanConfigEntry = _AgentFIPSnoopingVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 2, 1)
)
agentFIPSnoopingVlanConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentFIPSnoopingVlanIndex"),
)
if mibBuilder.loadTexts:
    agentFIPSnoopingVlanConfigEntry.setStatus("current")


class _AgentFIPSnoopingVlanIndex_Type(Integer32):
    """Custom type agentFIPSnoopingVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentFIPSnoopingVlanIndex_Type.__name__ = "Integer32"
_AgentFIPSnoopingVlanIndex_Object = MibTableColumn
agentFIPSnoopingVlanIndex = _AgentFIPSnoopingVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 2, 1, 1),
    _AgentFIPSnoopingVlanIndex_Type()
)
agentFIPSnoopingVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingVlanIndex.setStatus("current")


class _AgentFIPSnoopingVlanAdminMode_Type(Integer32):
    """Custom type agentFIPSnoopingVlanAdminMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentFIPSnoopingVlanAdminMode_Type.__name__ = "Integer32"
_AgentFIPSnoopingVlanAdminMode_Object = MibTableColumn
agentFIPSnoopingVlanAdminMode = _AgentFIPSnoopingVlanAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 2, 1, 2),
    _AgentFIPSnoopingVlanAdminMode_Type()
)
agentFIPSnoopingVlanAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFIPSnoopingVlanAdminMode.setStatus("current")
_AgentFIPSnoopingSessionTable_Object = MibTable
agentFIPSnoopingSessionTable = _AgentFIPSnoopingSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 5)
)
if mibBuilder.loadTexts:
    agentFIPSnoopingSessionTable.setStatus("current")
_AgentFIPSnoopingSessionEntry_Object = MibTableRow
agentFIPSnoopingSessionEntry = _AgentFIPSnoopingSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 5, 1)
)
agentFIPSnoopingSessionEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentFIPSnoopingSessionKey"),
)
if mibBuilder.loadTexts:
    agentFIPSnoopingSessionEntry.setStatus("current")
_AgentFIPSnoopingSessionKey_Type = PhysAddress
_AgentFIPSnoopingSessionKey_Object = MibTableColumn
agentFIPSnoopingSessionKey = _AgentFIPSnoopingSessionKey_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 5, 1, 1),
    _AgentFIPSnoopingSessionKey_Type()
)
agentFIPSnoopingSessionKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingSessionKey.setStatus("current")
_AgentFIPSnoopingSessionIfIndex_Type = Integer32
_AgentFIPSnoopingSessionIfIndex_Object = MibTableColumn
agentFIPSnoopingSessionIfIndex = _AgentFIPSnoopingSessionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 5, 1, 2),
    _AgentFIPSnoopingSessionIfIndex_Type()
)
agentFIPSnoopingSessionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingSessionIfIndex.setStatus("current")
_AgentFIPSnoopingSessionFCFMacAddress_Type = PhysAddress
_AgentFIPSnoopingSessionFCFMacAddress_Object = MibTableColumn
agentFIPSnoopingSessionFCFMacAddress = _AgentFIPSnoopingSessionFCFMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 5, 1, 3),
    _AgentFIPSnoopingSessionFCFMacAddress_Type()
)
agentFIPSnoopingSessionFCFMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingSessionFCFMacAddress.setStatus("current")
_AgentFIPSnoopingSessionENodeMacAddress_Type = PhysAddress
_AgentFIPSnoopingSessionENodeMacAddress_Object = MibTableColumn
agentFIPSnoopingSessionENodeMacAddress = _AgentFIPSnoopingSessionENodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 5, 1, 4),
    _AgentFIPSnoopingSessionENodeMacAddress_Type()
)
agentFIPSnoopingSessionENodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingSessionENodeMacAddress.setStatus("current")
_AgentFIPSnoopingSessionENodeIfIndex_Type = Integer32
_AgentFIPSnoopingSessionENodeIfIndex_Object = MibTableColumn
agentFIPSnoopingSessionENodeIfIndex = _AgentFIPSnoopingSessionENodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 5, 1, 5),
    _AgentFIPSnoopingSessionENodeIfIndex_Type()
)
agentFIPSnoopingSessionENodeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingSessionENodeIfIndex.setStatus("current")
_AgentFIPSnoopingFCFTable_Object = MibTable
agentFIPSnoopingFCFTable = _AgentFIPSnoopingFCFTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6)
)
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFTable.setStatus("current")
_AgentFIPSnoopingFCFEntry_Object = MibTableRow
agentFIPSnoopingFCFEntry = _AgentFIPSnoopingFCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1)
)
agentFIPSnoopingFCFEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentFIPSnoopingFCFKey"),
)
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFEntry.setStatus("current")
_AgentFIPSnoopingFCFKey_Type = PhysAddress
_AgentFIPSnoopingFCFKey_Object = MibTableColumn
agentFIPSnoopingFCFKey = _AgentFIPSnoopingFCFKey_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1, 1),
    _AgentFIPSnoopingFCFKey_Type()
)
agentFIPSnoopingFCFKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFKey.setStatus("current")
_AgentFIPSnoopingFCFIfIndex_Type = Integer32
_AgentFIPSnoopingFCFIfIndex_Object = MibTableColumn
agentFIPSnoopingFCFIfIndex = _AgentFIPSnoopingFCFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1, 2),
    _AgentFIPSnoopingFCFIfIndex_Type()
)
agentFIPSnoopingFCFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFIfIndex.setStatus("current")
_AgentFIPSnoopingFCFVlan_Type = VlanIndex
_AgentFIPSnoopingFCFVlan_Object = MibTableColumn
agentFIPSnoopingFCFVlan = _AgentFIPSnoopingFCFVlan_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1, 3),
    _AgentFIPSnoopingFCFVlan_Type()
)
agentFIPSnoopingFCFVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFVlan.setStatus("current")
_AgentFIPSnoopingFCFENodeNumber_Type = Integer32
_AgentFIPSnoopingFCFENodeNumber_Object = MibTableColumn
agentFIPSnoopingFCFENodeNumber = _AgentFIPSnoopingFCFENodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1, 4),
    _AgentFIPSnoopingFCFENodeNumber_Type()
)
agentFIPSnoopingFCFENodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFENodeNumber.setStatus("current")
_AgentFIPSnoopingFCFFCMap_Type = Integer32
_AgentFIPSnoopingFCFFCMap_Object = MibTableColumn
agentFIPSnoopingFCFFCMap = _AgentFIPSnoopingFCFFCMap_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1, 5),
    _AgentFIPSnoopingFCFFCMap_Type()
)
agentFIPSnoopingFCFFCMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFFCMap.setStatus("current")
_AgentFIPSnoopingFCFSwitchName_Type = DisplayString
_AgentFIPSnoopingFCFSwitchName_Object = MibTableColumn
agentFIPSnoopingFCFSwitchName = _AgentFIPSnoopingFCFSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1, 6),
    _AgentFIPSnoopingFCFSwitchName_Type()
)
agentFIPSnoopingFCFSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFSwitchName.setStatus("current")
_AgentFIPSnoopingFCFFabricName_Type = DisplayString
_AgentFIPSnoopingFCFFabricName_Object = MibTableColumn
agentFIPSnoopingFCFFabricName = _AgentFIPSnoopingFCFFabricName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 6, 1, 7),
    _AgentFIPSnoopingFCFFabricName_Type()
)
agentFIPSnoopingFCFFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingFCFFabricName.setStatus("current")
_AgentFIPSnoopingENodeTable_Object = MibTable
agentFIPSnoopingENodeTable = _AgentFIPSnoopingENodeTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 7)
)
if mibBuilder.loadTexts:
    agentFIPSnoopingENodeTable.setStatus("current")
_AgentFIPSnoopingENodeEntry_Object = MibTableRow
agentFIPSnoopingENodeEntry = _AgentFIPSnoopingENodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 7, 1)
)
agentFIPSnoopingENodeEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentFIPSnoopingENodeKey"),
)
if mibBuilder.loadTexts:
    agentFIPSnoopingENodeEntry.setStatus("current")
_AgentFIPSnoopingENodeKey_Type = PhysAddress
_AgentFIPSnoopingENodeKey_Object = MibTableColumn
agentFIPSnoopingENodeKey = _AgentFIPSnoopingENodeKey_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 7, 1, 1),
    _AgentFIPSnoopingENodeKey_Type()
)
agentFIPSnoopingENodeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingENodeKey.setStatus("current")
_AgentFIPSnoopingENodeIfIndex_Type = Integer32
_AgentFIPSnoopingENodeIfIndex_Object = MibTableColumn
agentFIPSnoopingENodeIfIndex = _AgentFIPSnoopingENodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 7, 1, 2),
    _AgentFIPSnoopingENodeIfIndex_Type()
)
agentFIPSnoopingENodeIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingENodeIfIndex.setStatus("current")
_AgentFIPSnoopingENodeVlan_Type = VlanIndex
_AgentFIPSnoopingENodeVlan_Object = MibTableColumn
agentFIPSnoopingENodeVlan = _AgentFIPSnoopingENodeVlan_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 7, 1, 3),
    _AgentFIPSnoopingENodeVlan_Type()
)
agentFIPSnoopingENodeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingENodeVlan.setStatus("current")
_AgentFIPSnoopingENodeNameID_Type = DisplayString
_AgentFIPSnoopingENodeNameID_Object = MibTableColumn
agentFIPSnoopingENodeNameID = _AgentFIPSnoopingENodeNameID_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 116, 7, 1, 4),
    _AgentFIPSnoopingENodeNameID_Type()
)
agentFIPSnoopingENodeNameID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFIPSnoopingENodeNameID.setStatus("current")
_AgentMLAGGroup_ObjectIdentity = ObjectIdentity
agentMLAGGroup = _AgentMLAGGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117)
)


class _AgentMLAGAdminMode_Type(Integer32):
    """Custom type agentMLAGAdminMode based on Integer32"""
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


_AgentMLAGAdminMode_Type.__name__ = "Integer32"
_AgentMLAGAdminMode_Object = MibScalar
agentMLAGAdminMode = _AgentMLAGAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 1),
    _AgentMLAGAdminMode_Type()
)
agentMLAGAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGAdminMode.setStatus("current")


class _AgentMLAGDomainId_Type(Integer32):
    """Custom type agentMLAGDomainId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AgentMLAGDomainId_Type.__name__ = "Integer32"
_AgentMLAGDomainId_Object = MibScalar
agentMLAGDomainId = _AgentMLAGDomainId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 2),
    _AgentMLAGDomainId_Type()
)
agentMLAGDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGDomainId.setStatus("current")


class _AgentMLAGConfigurationConsistancyStatus_Type(Integer32):
    """Custom type agentMLAGConfigurationConsistancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_AgentMLAGConfigurationConsistancyStatus_Type.__name__ = "Integer32"
_AgentMLAGConfigurationConsistancyStatus_Object = MibScalar
agentMLAGConfigurationConsistancyStatus = _AgentMLAGConfigurationConsistancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 3),
    _AgentMLAGConfigurationConsistancyStatus_Type()
)
agentMLAGConfigurationConsistancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGConfigurationConsistancyStatus.setStatus("current")


class _AgentMLAGMemberCount_Type(Unsigned32):
    """Custom type agentMLAGMemberCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMLAGMemberCount_Type.__name__ = "Unsigned32"
_AgentMLAGMemberCount_Object = MibScalar
agentMLAGMemberCount = _AgentMLAGMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 4),
    _AgentMLAGMemberCount_Type()
)
agentMLAGMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGMemberCount.setStatus("current")
_AgentMLAGSystemMac_Type = MacAddress
_AgentMLAGSystemMac_Object = MibScalar
agentMLAGSystemMac = _AgentMLAGSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 5),
    _AgentMLAGSystemMac_Type()
)
agentMLAGSystemMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGSystemMac.setStatus("current")


class _AgentMLAGKeepaliveTimeout_Type(Integer32):
    """Custom type agentMLAGKeepaliveTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 600),
    )


_AgentMLAGKeepaliveTimeout_Type.__name__ = "Integer32"
_AgentMLAGKeepaliveTimeout_Object = MibScalar
agentMLAGKeepaliveTimeout = _AgentMLAGKeepaliveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 6),
    _AgentMLAGKeepaliveTimeout_Type()
)
agentMLAGKeepaliveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGKeepaliveTimeout.setStatus("current")


class _AgentMLAGPeerGatewayMode_Type(Integer32):
    """Custom type agentMLAGPeerGatewayMode based on Integer32"""
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


_AgentMLAGPeerGatewayMode_Type.__name__ = "Integer32"
_AgentMLAGPeerGatewayMode_Object = MibScalar
agentMLAGPeerGatewayMode = _AgentMLAGPeerGatewayMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 7),
    _AgentMLAGPeerGatewayMode_Type()
)
agentMLAGPeerGatewayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGPeerGatewayMode.setStatus("current")


class _AgentMLAGDelayRestore_Type(Integer32):
    """Custom type agentMLAGDelayRestore based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AgentMLAGDelayRestore_Type.__name__ = "Integer32"
_AgentMLAGDelayRestore_Object = MibScalar
agentMLAGDelayRestore = _AgentMLAGDelayRestore_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 8),
    _AgentMLAGDelayRestore_Type()
)
agentMLAGDelayRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGDelayRestore.setStatus("current")


class _AgentMLAGMemberLinkdownMode_Type(Integer32):
    """Custom type agentMLAGMemberLinkdownMode based on Integer32"""
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


_AgentMLAGMemberLinkdownMode_Type.__name__ = "Integer32"
_AgentMLAGMemberLinkdownMode_Object = MibScalar
agentMLAGMemberLinkdownMode = _AgentMLAGMemberLinkdownMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 9),
    _AgentMLAGMemberLinkdownMode_Type()
)
agentMLAGMemberLinkdownMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGMemberLinkdownMode.setStatus("current")
_AgentMLAGPeerLinkGroup_ObjectIdentity = ObjectIdentity
agentMLAGPeerLinkGroup = _AgentMLAGPeerLinkGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 10)
)


class _AgentMLAGPeerLinkifIndex_Type(Integer32):
    """Custom type agentMLAGPeerLinkifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AgentMLAGPeerLinkifIndex_Type.__name__ = "Integer32"
_AgentMLAGPeerLinkifIndex_Object = MibScalar
agentMLAGPeerLinkifIndex = _AgentMLAGPeerLinkifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 10, 1),
    _AgentMLAGPeerLinkifIndex_Type()
)
agentMLAGPeerLinkifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGPeerLinkifIndex.setStatus("current")


class _AgentMLAGPeerLinkifStatus_Type(Integer32):
    """Custom type agentMLAGPeerLinkifStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AgentMLAGPeerLinkifStatus_Type.__name__ = "Integer32"
_AgentMLAGPeerLinkifStatus_Object = MibScalar
agentMLAGPeerLinkifStatus = _AgentMLAGPeerLinkifStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 10, 2),
    _AgentMLAGPeerLinkifStatus_Type()
)
agentMLAGPeerLinkifStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGPeerLinkifStatus.setStatus("current")
_AgentMLAGPeerLinkActiveVlans_Type = DisplayString
_AgentMLAGPeerLinkActiveVlans_Object = MibScalar
agentMLAGPeerLinkActiveVlans = _AgentMLAGPeerLinkActiveVlans_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 10, 3),
    _AgentMLAGPeerLinkActiveVlans_Type()
)
agentMLAGPeerLinkActiveVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGPeerLinkActiveVlans.setStatus("current")
_AgentMLAGPeerLinkForbiddenVlans_Type = DisplayString
_AgentMLAGPeerLinkForbiddenVlans_Object = MibScalar
agentMLAGPeerLinkForbiddenVlans = _AgentMLAGPeerLinkForbiddenVlans_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 10, 4),
    _AgentMLAGPeerLinkForbiddenVlans_Type()
)
agentMLAGPeerLinkForbiddenVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGPeerLinkForbiddenVlans.setStatus("current")
_AgentMLAGPortChannelTable_Object = MibTable
agentMLAGPortChannelTable = _AgentMLAGPortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 11)
)
if mibBuilder.loadTexts:
    agentMLAGPortChannelTable.setStatus("current")
_AgentMLAGPortChannelEntry_Object = MibTableRow
agentMLAGPortChannelEntry = _AgentMLAGPortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 11, 1)
)
agentMLAGPortChannelEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentMLAGPortChannelifIndex"),
)
if mibBuilder.loadTexts:
    agentMLAGPortChannelEntry.setStatus("current")
_AgentMLAGPortChannelifIndex_Type = InterfaceIndex
_AgentMLAGPortChannelifIndex_Object = MibTableColumn
agentMLAGPortChannelifIndex = _AgentMLAGPortChannelifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 11, 1, 1),
    _AgentMLAGPortChannelifIndex_Type()
)
agentMLAGPortChannelifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGPortChannelifIndex.setStatus("current")


class _AgentMLAGPortChannelId_Type(Integer32):
    """Custom type agentMLAGPortChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AgentMLAGPortChannelId_Type.__name__ = "Integer32"
_AgentMLAGPortChannelId_Object = MibTableColumn
agentMLAGPortChannelId = _AgentMLAGPortChannelId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 11, 1, 2),
    _AgentMLAGPortChannelId_Type()
)
agentMLAGPortChannelId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentMLAGPortChannelId.setStatus("current")


class _AgentMLAGPortChannelifIndexStatus_Type(Integer32):
    """Custom type agentMLAGPortChannelifIndexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AgentMLAGPortChannelifIndexStatus_Type.__name__ = "Integer32"
_AgentMLAGPortChannelifIndexStatus_Object = MibTableColumn
agentMLAGPortChannelifIndexStatus = _AgentMLAGPortChannelifIndexStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 11, 1, 3),
    _AgentMLAGPortChannelifIndexStatus_Type()
)
agentMLAGPortChannelifIndexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGPortChannelifIndexStatus.setStatus("current")


class _AgentMLAGPortChannelConsistancy_Type(Integer32):
    """Custom type agentMLAGPortChannelConsistancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_AgentMLAGPortChannelConsistancy_Type.__name__ = "Integer32"
_AgentMLAGPortChannelConsistancy_Object = MibTableColumn
agentMLAGPortChannelConsistancy = _AgentMLAGPortChannelConsistancy_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 11, 1, 4),
    _AgentMLAGPortChannelConsistancy_Type()
)
agentMLAGPortChannelConsistancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGPortChannelConsistancy.setStatus("current")
_AgentMLAGPortChannelActiveVlans_Type = DisplayString
_AgentMLAGPortChannelActiveVlans_Object = MibTableColumn
agentMLAGPortChannelActiveVlans = _AgentMLAGPortChannelActiveVlans_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 11, 1, 5),
    _AgentMLAGPortChannelActiveVlans_Type()
)
agentMLAGPortChannelActiveVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGPortChannelActiveVlans.setStatus("current")
_AgentMLAGVlanRoutingPortTable_Object = MibTable
agentMLAGVlanRoutingPortTable = _AgentMLAGVlanRoutingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 12)
)
if mibBuilder.loadTexts:
    agentMLAGVlanRoutingPortTable.setStatus("current")
_AgentMLAGVlanRoutingPortEntry_Object = MibTableRow
agentMLAGVlanRoutingPortEntry = _AgentMLAGVlanRoutingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 12, 1)
)
agentMLAGVlanRoutingPortEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentMLAGVlanRoutingPortifIndex"),
)
if mibBuilder.loadTexts:
    agentMLAGVlanRoutingPortEntry.setStatus("current")
_AgentMLAGVlanRoutingPortifIndex_Type = InterfaceIndex
_AgentMLAGVlanRoutingPortifIndex_Object = MibTableColumn
agentMLAGVlanRoutingPortifIndex = _AgentMLAGVlanRoutingPortifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 12, 1, 1),
    _AgentMLAGVlanRoutingPortifIndex_Type()
)
agentMLAGVlanRoutingPortifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMLAGVlanRoutingPortifIndex.setStatus("current")


class _AgentMLAGVlanRoutingPortForbiddenMode_Type(Integer32):
    """Custom type agentMLAGVlanRoutingPortForbiddenMode based on Integer32"""
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


_AgentMLAGVlanRoutingPortForbiddenMode_Type.__name__ = "Integer32"
_AgentMLAGVlanRoutingPortForbiddenMode_Object = MibTableColumn
agentMLAGVlanRoutingPortForbiddenMode = _AgentMLAGVlanRoutingPortForbiddenMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 117, 12, 1, 2),
    _AgentMLAGVlanRoutingPortForbiddenMode_Type()
)
agentMLAGVlanRoutingPortForbiddenMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMLAGVlanRoutingPortForbiddenMode.setStatus("current")
_AgentDCBXGroup_ObjectIdentity = ObjectIdentity
agentDCBXGroup = _AgentDCBXGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118)
)
_AgentDCBXConfigTable_Object = MibTable
agentDCBXConfigTable = _AgentDCBXConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 1)
)
if mibBuilder.loadTexts:
    agentDCBXConfigTable.setStatus("current")
_AgentDCBXConfigEntry_Object = MibTableRow
agentDCBXConfigEntry = _AgentDCBXConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 1, 1)
)
agentDCBXConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentDCBXifIndex"),
)
if mibBuilder.loadTexts:
    agentDCBXConfigEntry.setStatus("current")
_AgentDCBXifIndex_Type = InterfaceIndex
_AgentDCBXifIndex_Object = MibTableColumn
agentDCBXifIndex = _AgentDCBXifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 1, 1, 1),
    _AgentDCBXifIndex_Type()
)
agentDCBXifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXifIndex.setStatus("current")


class _AgentDCBXAdminMode_Type(Integer32):
    """Custom type agentDCBXAdminMode based on Integer32"""
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


_AgentDCBXAdminMode_Type.__name__ = "Integer32"
_AgentDCBXAdminMode_Object = MibTableColumn
agentDCBXAdminMode = _AgentDCBXAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 1, 1, 2),
    _AgentDCBXAdminMode_Type()
)
agentDCBXAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDCBXAdminMode.setStatus("current")


class _AgentDCBXVersion_Type(Integer32):
    """Custom type agentDCBXVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("cee", 1),
          ("ieee", 2))
    )


_AgentDCBXVersion_Type.__name__ = "Integer32"
_AgentDCBXVersion_Object = MibTableColumn
agentDCBXVersion = _AgentDCBXVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 1, 1, 3),
    _AgentDCBXVersion_Type()
)
agentDCBXVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDCBXVersion.setStatus("current")
_AgentDCBXPFCConfigTable_Object = MibTable
agentDCBXPFCConfigTable = _AgentDCBXPFCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2)
)
if mibBuilder.loadTexts:
    agentDCBXPFCConfigTable.setStatus("current")
_AgentDCBXPFCConfigEntry_Object = MibTableRow
agentDCBXPFCConfigEntry = _AgentDCBXPFCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1)
)
agentDCBXPFCConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentDCBXifIndex"),
)
if mibBuilder.loadTexts:
    agentDCBXPFCConfigEntry.setStatus("current")


class _AgentDCBXPFCEnableMode_Type(Integer32):
    """Custom type agentDCBXPFCEnableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPFCEnableMode_Type.__name__ = "Integer32"
_AgentDCBXPFCEnableMode_Object = MibTableColumn
agentDCBXPFCEnableMode = _AgentDCBXPFCEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 1),
    _AgentDCBXPFCEnableMode_Type()
)
agentDCBXPFCEnableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCEnableMode.setStatus("current")


class _AgentDCBXPFCAdvertiseMode_Type(Integer32):
    """Custom type agentDCBXPFCAdvertiseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPFCAdvertiseMode_Type.__name__ = "Integer32"
_AgentDCBXPFCAdvertiseMode_Object = MibTableColumn
agentDCBXPFCAdvertiseMode = _AgentDCBXPFCAdvertiseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 2),
    _AgentDCBXPFCAdvertiseMode_Type()
)
agentDCBXPFCAdvertiseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCAdvertiseMode.setStatus("current")


class _AgentDCBXPFCWillingMode_Type(Integer32):
    """Custom type agentDCBXPFCWillingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPFCWillingMode_Type.__name__ = "Integer32"
_AgentDCBXPFCWillingMode_Object = MibTableColumn
agentDCBXPFCWillingMode = _AgentDCBXPFCWillingMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 3),
    _AgentDCBXPFCWillingMode_Type()
)
agentDCBXPFCWillingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDCBXPFCWillingMode.setStatus("current")


class _AgentDCBXPFCPriorityMask_Type(Unsigned32):
    """Custom type agentDCBXPFCPriorityMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCPriorityMask_Type.__name__ = "Unsigned32"
_AgentDCBXPFCPriorityMask_Object = MibTableColumn
agentDCBXPFCPriorityMask = _AgentDCBXPFCPriorityMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 4),
    _AgentDCBXPFCPriorityMask_Type()
)
agentDCBXPFCPriorityMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCPriorityMask.setStatus("current")


class _AgentDCBXPFCMaxTrafficClass_Type(Unsigned32):
    """Custom type agentDCBXPFCMaxTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCMaxTrafficClass_Type.__name__ = "Unsigned32"
_AgentDCBXPFCMaxTrafficClass_Object = MibTableColumn
agentDCBXPFCMaxTrafficClass = _AgentDCBXPFCMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 5),
    _AgentDCBXPFCMaxTrafficClass_Type()
)
agentDCBXPFCMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCMaxTrafficClass.setStatus("current")


class _AgentDCBXPFCOperVersion_Type(Unsigned32):
    """Custom type agentDCBXPFCOperVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCOperVersion_Type.__name__ = "Unsigned32"
_AgentDCBXPFCOperVersion_Object = MibTableColumn
agentDCBXPFCOperVersion = _AgentDCBXPFCOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 6),
    _AgentDCBXPFCOperVersion_Type()
)
agentDCBXPFCOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCOperVersion.setStatus("current")


class _AgentDCBXPFCOperMaxVersion_Type(Unsigned32):
    """Custom type agentDCBXPFCOperMaxVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCOperMaxVersion_Type.__name__ = "Unsigned32"
_AgentDCBXPFCOperMaxVersion_Object = MibTableColumn
agentDCBXPFCOperMaxVersion = _AgentDCBXPFCOperMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 7),
    _AgentDCBXPFCOperMaxVersion_Type()
)
agentDCBXPFCOperMaxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCOperMaxVersion.setStatus("current")
_AgentDCBXPFCOperErrors_Type = DisplayString
_AgentDCBXPFCOperErrors_Object = MibTableColumn
agentDCBXPFCOperErrors = _AgentDCBXPFCOperErrors_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 8),
    _AgentDCBXPFCOperErrors_Type()
)
agentDCBXPFCOperErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCOperErrors.setStatus("current")


class _AgentDCBXPFCOperMode_Type(Integer32):
    """Custom type agentDCBXPFCOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPFCOperMode_Type.__name__ = "Integer32"
_AgentDCBXPFCOperMode_Object = MibTableColumn
agentDCBXPFCOperMode = _AgentDCBXPFCOperMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 9),
    _AgentDCBXPFCOperMode_Type()
)
agentDCBXPFCOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCOperMode.setStatus("current")


class _AgentDCBXPFCOperPeerSyncd_Type(Integer32):
    """Custom type agentDCBXPFCOperPeerSyncd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPFCOperPeerSyncd_Type.__name__ = "Integer32"
_AgentDCBXPFCOperPeerSyncd_Object = MibTableColumn
agentDCBXPFCOperPeerSyncd = _AgentDCBXPFCOperPeerSyncd_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 10),
    _AgentDCBXPFCOperPeerSyncd_Type()
)
agentDCBXPFCOperPeerSyncd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCOperPeerSyncd.setStatus("current")


class _AgentDCBXPFCOperPriorityMask_Type(Unsigned32):
    """Custom type agentDCBXPFCOperPriorityMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCOperPriorityMask_Type.__name__ = "Unsigned32"
_AgentDCBXPFCOperPriorityMask_Object = MibTableColumn
agentDCBXPFCOperPriorityMask = _AgentDCBXPFCOperPriorityMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 11),
    _AgentDCBXPFCOperPriorityMask_Type()
)
agentDCBXPFCOperPriorityMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCOperPriorityMask.setStatus("current")


class _AgentDCBXPFCOperMaxTrafficClass_Type(Unsigned32):
    """Custom type agentDCBXPFCOperMaxTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCOperMaxTrafficClass_Type.__name__ = "Unsigned32"
_AgentDCBXPFCOperMaxTrafficClass_Object = MibTableColumn
agentDCBXPFCOperMaxTrafficClass = _AgentDCBXPFCOperMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 12),
    _AgentDCBXPFCOperMaxTrafficClass_Type()
)
agentDCBXPFCOperMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCOperMaxTrafficClass.setStatus("current")
_AgentDCBXPFCPeerLocalifIndex_Type = InterfaceIndex
_AgentDCBXPFCPeerLocalifIndex_Object = MibTableColumn
agentDCBXPFCPeerLocalifIndex = _AgentDCBXPFCPeerLocalifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 13),
    _AgentDCBXPFCPeerLocalifIndex_Type()
)
agentDCBXPFCPeerLocalifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCPeerLocalifIndex.setStatus("current")


class _AgentDCBXPFCPeerStatus_Type(Integer32):
    """Custom type agentDCBXPFCPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("successful", 1),
          ("unsuccessful", 2))
    )


_AgentDCBXPFCPeerStatus_Type.__name__ = "Integer32"
_AgentDCBXPFCPeerStatus_Object = MibTableColumn
agentDCBXPFCPeerStatus = _AgentDCBXPFCPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 14),
    _AgentDCBXPFCPeerStatus_Type()
)
agentDCBXPFCPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCPeerStatus.setStatus("current")


class _AgentDCBXPFCPeerEnableMode_Type(Integer32):
    """Custom type agentDCBXPFCPeerEnableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPFCPeerEnableMode_Type.__name__ = "Integer32"
_AgentDCBXPFCPeerEnableMode_Object = MibTableColumn
agentDCBXPFCPeerEnableMode = _AgentDCBXPFCPeerEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 15),
    _AgentDCBXPFCPeerEnableMode_Type()
)
agentDCBXPFCPeerEnableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCPeerEnableMode.setStatus("current")


class _AgentDCBXPFCPeerWillingMode_Type(Integer32):
    """Custom type agentDCBXPFCPeerWillingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPFCPeerWillingMode_Type.__name__ = "Integer32"
_AgentDCBXPFCPeerWillingMode_Object = MibTableColumn
agentDCBXPFCPeerWillingMode = _AgentDCBXPFCPeerWillingMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 16),
    _AgentDCBXPFCPeerWillingMode_Type()
)
agentDCBXPFCPeerWillingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCPeerWillingMode.setStatus("current")


class _AgentDCBXPFCPeerPriorityMask_Type(Unsigned32):
    """Custom type agentDCBXPFCPeerPriorityMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCPeerPriorityMask_Type.__name__ = "Unsigned32"
_AgentDCBXPFCPeerPriorityMask_Object = MibTableColumn
agentDCBXPFCPeerPriorityMask = _AgentDCBXPFCPeerPriorityMask_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 17),
    _AgentDCBXPFCPeerPriorityMask_Type()
)
agentDCBXPFCPeerPriorityMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCPeerPriorityMask.setStatus("current")


class _AgentDCBXPFCPeerMaxTrafficClass_Type(Unsigned32):
    """Custom type agentDCBXPFCPeerMaxTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPFCPeerMaxTrafficClass_Type.__name__ = "Unsigned32"
_AgentDCBXPFCPeerMaxTrafficClass_Object = MibTableColumn
agentDCBXPFCPeerMaxTrafficClass = _AgentDCBXPFCPeerMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 18),
    _AgentDCBXPFCPeerMaxTrafficClass_Type()
)
agentDCBXPFCPeerMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCPeerMaxTrafficClass.setStatus("current")


class _AgentDCBXPFCDCBXOperVersion_Type(Integer32):
    """Custom type agentDCBXPFCDCBXOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cee", 1),
          ("ieee", 2))
    )


_AgentDCBXPFCDCBXOperVersion_Type.__name__ = "Integer32"
_AgentDCBXPFCDCBXOperVersion_Object = MibTableColumn
agentDCBXPFCDCBXOperVersion = _AgentDCBXPFCDCBXOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 2, 1, 19),
    _AgentDCBXPFCDCBXOperVersion_Type()
)
agentDCBXPFCDCBXOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPFCDCBXOperVersion.setStatus("current")
_AgentDCBXPgConfigTable_Object = MibTable
agentDCBXPgConfigTable = _AgentDCBXPgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3)
)
if mibBuilder.loadTexts:
    agentDCBXPgConfigTable.setStatus("current")
_AgentDCBXPgConfigEntry_Object = MibTableRow
agentDCBXPgConfigEntry = _AgentDCBXPgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1)
)
agentDCBXPgConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentDCBXifIndex"),
)
if mibBuilder.loadTexts:
    agentDCBXPgConfigEntry.setStatus("current")


class _AgentDCBXPgEnableMode_Type(Integer32):
    """Custom type agentDCBXPgEnableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPgEnableMode_Type.__name__ = "Integer32"
_AgentDCBXPgEnableMode_Object = MibTableColumn
agentDCBXPgEnableMode = _AgentDCBXPgEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 1),
    _AgentDCBXPgEnableMode_Type()
)
agentDCBXPgEnableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgEnableMode.setStatus("current")


class _AgentDCBXPgAdvertiseMode_Type(Integer32):
    """Custom type agentDCBXPgAdvertiseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPgAdvertiseMode_Type.__name__ = "Integer32"
_AgentDCBXPgAdvertiseMode_Object = MibTableColumn
agentDCBXPgAdvertiseMode = _AgentDCBXPgAdvertiseMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 2),
    _AgentDCBXPgAdvertiseMode_Type()
)
agentDCBXPgAdvertiseMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgAdvertiseMode.setStatus("current")


class _AgentDCBXPgWillingMode_Type(Integer32):
    """Custom type agentDCBXPgWillingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPgWillingMode_Type.__name__ = "Integer32"
_AgentDCBXPgWillingMode_Object = MibTableColumn
agentDCBXPgWillingMode = _AgentDCBXPgWillingMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 3),
    _AgentDCBXPgWillingMode_Type()
)
agentDCBXPgWillingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDCBXPgWillingMode.setStatus("current")
_AgentDCBXPgGroupBandwidth_Type = DisplayString
_AgentDCBXPgGroupBandwidth_Object = MibTableColumn
agentDCBXPgGroupBandwidth = _AgentDCBXPgGroupBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 4),
    _AgentDCBXPgGroupBandwidth_Type()
)
agentDCBXPgGroupBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgGroupBandwidth.setStatus("current")
_AgentDCBXPgPriorityGroupId_Type = DisplayString
_AgentDCBXPgPriorityGroupId_Object = MibTableColumn
agentDCBXPgPriorityGroupId = _AgentDCBXPgPriorityGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 5),
    _AgentDCBXPgPriorityGroupId_Type()
)
agentDCBXPgPriorityGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgPriorityGroupId.setStatus("current")


class _AgentDCBXPgMaxTrafficClass_Type(Unsigned32):
    """Custom type agentDCBXPgMaxTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPgMaxTrafficClass_Type.__name__ = "Unsigned32"
_AgentDCBXPgMaxTrafficClass_Object = MibTableColumn
agentDCBXPgMaxTrafficClass = _AgentDCBXPgMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 6),
    _AgentDCBXPgMaxTrafficClass_Type()
)
agentDCBXPgMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgMaxTrafficClass.setStatus("current")


class _AgentDCBXPgOperVersion_Type(Unsigned32):
    """Custom type agentDCBXPgOperVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPgOperVersion_Type.__name__ = "Unsigned32"
_AgentDCBXPgOperVersion_Object = MibTableColumn
agentDCBXPgOperVersion = _AgentDCBXPgOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 7),
    _AgentDCBXPgOperVersion_Type()
)
agentDCBXPgOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgOperVersion.setStatus("current")


class _AgentDCBXPgMaxVersion_Type(Unsigned32):
    """Custom type agentDCBXPgMaxVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPgMaxVersion_Type.__name__ = "Unsigned32"
_AgentDCBXPgMaxVersion_Object = MibTableColumn
agentDCBXPgMaxVersion = _AgentDCBXPgMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 8),
    _AgentDCBXPgMaxVersion_Type()
)
agentDCBXPgMaxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgMaxVersion.setStatus("current")
_AgentDCBXPgErrorReason_Type = DisplayString
_AgentDCBXPgErrorReason_Object = MibTableColumn
agentDCBXPgErrorReason = _AgentDCBXPgErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 9),
    _AgentDCBXPgErrorReason_Type()
)
agentDCBXPgErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgErrorReason.setStatus("current")


class _AgentDCBXPgIsOperational_Type(Integer32):
    """Custom type agentDCBXPgIsOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPgIsOperational_Type.__name__ = "Integer32"
_AgentDCBXPgIsOperational_Object = MibTableColumn
agentDCBXPgIsOperational = _AgentDCBXPgIsOperational_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 10),
    _AgentDCBXPgIsOperational_Type()
)
agentDCBXPgIsOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgIsOperational.setStatus("current")


class _AgentDCBXPgSyncedMode_Type(Integer32):
    """Custom type agentDCBXPgSyncedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPgSyncedMode_Type.__name__ = "Integer32"
_AgentDCBXPgSyncedMode_Object = MibTableColumn
agentDCBXPgSyncedMode = _AgentDCBXPgSyncedMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 11),
    _AgentDCBXPgSyncedMode_Type()
)
agentDCBXPgSyncedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgSyncedMode.setStatus("current")
_AgentDCBXPgOperGroupBandwidth_Type = DisplayString
_AgentDCBXPgOperGroupBandwidth_Object = MibTableColumn
agentDCBXPgOperGroupBandwidth = _AgentDCBXPgOperGroupBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 12),
    _AgentDCBXPgOperGroupBandwidth_Type()
)
agentDCBXPgOperGroupBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgOperGroupBandwidth.setStatus("current")
_AgentDCBXPgOperPriorityGroupId_Type = DisplayString
_AgentDCBXPgOperPriorityGroupId_Object = MibTableColumn
agentDCBXPgOperPriorityGroupId = _AgentDCBXPgOperPriorityGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 13),
    _AgentDCBXPgOperPriorityGroupId_Type()
)
agentDCBXPgOperPriorityGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgOperPriorityGroupId.setStatus("current")


class _AgentDCBXPgOperMaxTrafficClass_Type(Unsigned32):
    """Custom type agentDCBXPgOperMaxTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPgOperMaxTrafficClass_Type.__name__ = "Unsigned32"
_AgentDCBXPgOperMaxTrafficClass_Object = MibTableColumn
agentDCBXPgOperMaxTrafficClass = _AgentDCBXPgOperMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 14),
    _AgentDCBXPgOperMaxTrafficClass_Type()
)
agentDCBXPgOperMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgOperMaxTrafficClass.setStatus("current")


class _AgentDCBXPgPeerStatus_Type(Integer32):
    """Custom type agentDCBXPgPeerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 0),
          ("successful", 1),
          ("unsuccessful", 2))
    )


_AgentDCBXPgPeerStatus_Type.__name__ = "Integer32"
_AgentDCBXPgPeerStatus_Object = MibTableColumn
agentDCBXPgPeerStatus = _AgentDCBXPgPeerStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 15),
    _AgentDCBXPgPeerStatus_Type()
)
agentDCBXPgPeerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgPeerStatus.setStatus("current")


class _AgentDCBXPgPeerEnableMode_Type(Integer32):
    """Custom type agentDCBXPgPeerEnableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPgPeerEnableMode_Type.__name__ = "Integer32"
_AgentDCBXPgPeerEnableMode_Object = MibTableColumn
agentDCBXPgPeerEnableMode = _AgentDCBXPgPeerEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 16),
    _AgentDCBXPgPeerEnableMode_Type()
)
agentDCBXPgPeerEnableMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgPeerEnableMode.setStatus("current")


class _AgentDCBXPgPeerWillingMode_Type(Integer32):
    """Custom type agentDCBXPgPeerWillingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_AgentDCBXPgPeerWillingMode_Type.__name__ = "Integer32"
_AgentDCBXPgPeerWillingMode_Object = MibTableColumn
agentDCBXPgPeerWillingMode = _AgentDCBXPgPeerWillingMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 17),
    _AgentDCBXPgPeerWillingMode_Type()
)
agentDCBXPgPeerWillingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgPeerWillingMode.setStatus("current")
_AgentDCBXPgPeerGroupBandwidth_Type = DisplayString
_AgentDCBXPgPeerGroupBandwidth_Object = MibTableColumn
agentDCBXPgPeerGroupBandwidth = _AgentDCBXPgPeerGroupBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 18),
    _AgentDCBXPgPeerGroupBandwidth_Type()
)
agentDCBXPgPeerGroupBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgPeerGroupBandwidth.setStatus("current")
_AgentDCBXPgPeerPriorityGroupId_Type = DisplayString
_AgentDCBXPgPeerPriorityGroupId_Object = MibTableColumn
agentDCBXPgPeerPriorityGroupId = _AgentDCBXPgPeerPriorityGroupId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 19),
    _AgentDCBXPgPeerPriorityGroupId_Type()
)
agentDCBXPgPeerPriorityGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgPeerPriorityGroupId.setStatus("current")


class _AgentDCBXPgPeerMaxTrafficClass_Type(Unsigned32):
    """Custom type agentDCBXPgPeerMaxTrafficClass based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AgentDCBXPgPeerMaxTrafficClass_Type.__name__ = "Unsigned32"
_AgentDCBXPgPeerMaxTrafficClass_Object = MibTableColumn
agentDCBXPgPeerMaxTrafficClass = _AgentDCBXPgPeerMaxTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 20),
    _AgentDCBXPgPeerMaxTrafficClass_Type()
)
agentDCBXPgPeerMaxTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgPeerMaxTrafficClass.setStatus("current")


class _AgentDCBXPgDCBXOperVersion_Type(Integer32):
    """Custom type agentDCBXPgDCBXOperVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cee", 1),
          ("ieee", 2))
    )


_AgentDCBXPgDCBXOperVersion_Type.__name__ = "Integer32"
_AgentDCBXPgDCBXOperVersion_Object = MibTableColumn
agentDCBXPgDCBXOperVersion = _AgentDCBXPgDCBXOperVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 118, 3, 1, 21),
    _AgentDCBXPgDCBXOperVersion_Type()
)
agentDCBXPgDCBXOperVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDCBXPgDCBXOperVersion.setStatus("current")
_AgentEvbGroup_ObjectIdentity = ObjectIdentity
agentEvbGroup = _AgentEvbGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119)
)
_AgentEvbConfigTable_Object = MibTable
agentEvbConfigTable = _AgentEvbConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1)
)
if mibBuilder.loadTexts:
    agentEvbConfigTable.setStatus("current")
_AgentEvbConfigEntry_Object = MibTableRow
agentEvbConfigEntry = _AgentEvbConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1)
)
agentEvbConfigEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentEvbifIndex"),
)
if mibBuilder.loadTexts:
    agentEvbConfigEntry.setStatus("current")


class _AgentEvbifIndex_Type(Integer32):
    """Custom type agentEvbifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 53),
    )


_AgentEvbifIndex_Type.__name__ = "Integer32"
_AgentEvbifIndex_Object = MibTableColumn
agentEvbifIndex = _AgentEvbifIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 1),
    _AgentEvbifIndex_Type()
)
agentEvbifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbifIndex.setStatus("current")


class _AgentEvbAdminMode_Type(Integer32):
    """Custom type agentEvbAdminMode based on Integer32"""
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


_AgentEvbAdminMode_Type.__name__ = "Integer32"
_AgentEvbAdminMode_Object = MibTableColumn
agentEvbAdminMode = _AgentEvbAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 2),
    _AgentEvbAdminMode_Type()
)
agentEvbAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentEvbAdminMode.setStatus("current")
_AgentEvbCapability_Type = BridgeEvbTLVTC
_AgentEvbCapability_Object = MibTableColumn
agentEvbCapability = _AgentEvbCapability_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 3),
    _AgentEvbCapability_Type()
)
agentEvbCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbCapability.setStatus("current")
_AgentEvbForwardingMode_Type = BridgeEvbTLVTC
_AgentEvbForwardingMode_Object = MibTableColumn
agentEvbForwardingMode = _AgentEvbForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 4),
    _AgentEvbForwardingMode_Type()
)
agentEvbForwardingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbForwardingMode.setStatus("current")
_AgentEvbRetransmissionExp_Type = Unsigned32
_AgentEvbRetransmissionExp_Object = MibTableColumn
agentEvbRetransmissionExp = _AgentEvbRetransmissionExp_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 5),
    _AgentEvbRetransmissionExp_Type()
)
agentEvbRetransmissionExp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentEvbRetransmissionExp.setStatus("current")
_AgentEvbOperCapability_Type = BridgeEvbTLVTC
_AgentEvbOperCapability_Object = MibTableColumn
agentEvbOperCapability = _AgentEvbOperCapability_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 6),
    _AgentEvbOperCapability_Type()
)
agentEvbOperCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbOperCapability.setStatus("current")
_AgentEvbOperForwardingMode_Type = BridgeEvbTLVTC
_AgentEvbOperForwardingMode_Object = MibTableColumn
agentEvbOperForwardingMode = _AgentEvbOperForwardingMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 7),
    _AgentEvbOperForwardingMode_Type()
)
agentEvbOperForwardingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbOperForwardingMode.setStatus("current")
_AgentEvbOperRetransmissionExp_Type = Unsigned32
_AgentEvbOperRetransmissionExp_Object = MibTableColumn
agentEvbOperRetransmissionExp = _AgentEvbOperRetransmissionExp_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 1, 1, 8),
    _AgentEvbOperRetransmissionExp_Type()
)
agentEvbOperRetransmissionExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbOperRetransmissionExp.setStatus("current")
_AgentEvbVsiGroup_ObjectIdentity = ObjectIdentity
agentEvbVsiGroup = _AgentEvbVsiGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2)
)
_AgentEvbVsiTable_Object = MibTable
agentEvbVsiTable = _AgentEvbVsiTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1)
)
if mibBuilder.loadTexts:
    agentEvbVsiTable.setStatus("current")
_AgentEvbVsiEntry_Object = MibTableRow
agentEvbVsiEntry = _AgentEvbVsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1)
)
agentEvbVsiEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentEvbifIndex"),
    (0, "SWITCHING-EXTENSION-MIB", "agentEvbVsiInstanceId"),
)
if mibBuilder.loadTexts:
    agentEvbVsiEntry.setStatus("current")


class _AgentEvbVsiInstanceId_Type(DisplayString):
    """Custom type agentEvbVsiInstanceId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_AgentEvbVsiInstanceId_Type.__name__ = "DisplayString"
_AgentEvbVsiInstanceId_Object = MibTableColumn
agentEvbVsiInstanceId = _AgentEvbVsiInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1, 1),
    _AgentEvbVsiInstanceId_Type()
)
agentEvbVsiInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiInstanceId.setStatus("current")
_AgentEvbVsiMgrId_Type = Unsigned32
_AgentEvbVsiMgrId_Object = MibTableColumn
agentEvbVsiMgrId = _AgentEvbVsiMgrId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1, 2),
    _AgentEvbVsiMgrId_Type()
)
agentEvbVsiMgrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiMgrId.setStatus("current")
_AgentEvbVsiId_Type = Unsigned32
_AgentEvbVsiId_Object = MibTableColumn
agentEvbVsiId = _AgentEvbVsiId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1, 3),
    _AgentEvbVsiId_Type()
)
agentEvbVsiId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiId.setStatus("current")
_AgentEvbVsiVersion_Type = Unsigned32
_AgentEvbVsiVersion_Object = MibTableColumn
agentEvbVsiVersion = _AgentEvbVsiVersion_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1, 4),
    _AgentEvbVsiVersion_Type()
)
agentEvbVsiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiVersion.setStatus("current")


class _AgentEvbVsiMode_Type(Integer32):
    """Custom type agentEvbVsiMode based on Integer32"""
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
        *(("associate", 3),
          ("deassociate", 4),
          ("preassocerr", 2),
          ("preassociate", 1))
    )


_AgentEvbVsiMode_Type.__name__ = "Integer32"
_AgentEvbVsiMode_Object = MibTableColumn
agentEvbVsiMode = _AgentEvbVsiMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1, 5),
    _AgentEvbVsiMode_Type()
)
agentEvbVsiMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiMode.setStatus("current")


class _AgentEvbVsiState_Type(Integer32):
    """Custom type agentEvbVsiState based on Integer32"""
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
        *(("associated", 3),
          ("assocprocessing", 2),
          ("deassocprocessing", 6),
          ("exit", 7),
          ("preassociated", 5),
          ("preassocprocessing", 4),
          ("unassociated", 1))
    )


_AgentEvbVsiState_Type.__name__ = "Integer32"
_AgentEvbVsiState_Object = MibTableColumn
agentEvbVsiState = _AgentEvbVsiState_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1, 6),
    _AgentEvbVsiState_Type()
)
agentEvbVsiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiState.setStatus("current")
_AgentEvbVsiNumMacs_Type = Unsigned32
_AgentEvbVsiNumMacs_Object = MibTableColumn
agentEvbVsiNumMacs = _AgentEvbVsiNumMacs_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 1, 1, 7),
    _AgentEvbVsiNumMacs_Type()
)
agentEvbVsiNumMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiNumMacs.setStatus("current")
_AgentEvbVsiMacTable_Object = MibTable
agentEvbVsiMacTable = _AgentEvbVsiMacTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 2)
)
if mibBuilder.loadTexts:
    agentEvbVsiMacTable.setStatus("current")
_AgentEvbVsiMacEntry_Object = MibTableRow
agentEvbVsiMacEntry = _AgentEvbVsiMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 2, 1)
)
agentEvbVsiMacEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentEvbifIndex"),
    (0, "SWITCHING-EXTENSION-MIB", "agentEvbVsiInstanceId"),
    (0, "SWITCHING-EXTENSION-MIB", "agentEvbVsiMacAddress"),
    (0, "SWITCHING-EXTENSION-MIB", "agentEvbVsiVlanId"),
)
if mibBuilder.loadTexts:
    agentEvbVsiMacEntry.setStatus("current")
_AgentEvbVsiMacAddress_Type = MacAddress
_AgentEvbVsiMacAddress_Object = MibTableColumn
agentEvbVsiMacAddress = _AgentEvbVsiMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 2, 1, 1),
    _AgentEvbVsiMacAddress_Type()
)
agentEvbVsiMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiMacAddress.setStatus("current")


class _AgentEvbVsiVlanId_Type(Integer32):
    """Custom type agentEvbVsiVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AgentEvbVsiVlanId_Type.__name__ = "Integer32"
_AgentEvbVsiVlanId_Object = MibTableColumn
agentEvbVsiVlanId = _AgentEvbVsiVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 119, 2, 2, 1, 2),
    _AgentEvbVsiVlanId_Type()
)
agentEvbVsiVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentEvbVsiVlanId.setStatus("current")
_AgentVMTracerGroup_ObjectIdentity = ObjectIdentity
agentVMTracerGroup = _AgentVMTracerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120)
)
_AgentVMTracerIfCtlTable_Object = MibTable
agentVMTracerIfCtlTable = _AgentVMTracerIfCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 1)
)
if mibBuilder.loadTexts:
    agentVMTracerIfCtlTable.setStatus("current")
_AgentVMTracerIfCtlEntry_Object = MibTableRow
agentVMTracerIfCtlEntry = _AgentVMTracerIfCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 1, 1)
)
agentVMTracerIfCtlEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentVMTracerIfIndex"),
)
if mibBuilder.loadTexts:
    agentVMTracerIfCtlEntry.setStatus("current")


class _AgentVMTracerIfIndex_Type(Integer32):
    """Custom type agentVMTracerIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentVMTracerIfIndex_Type.__name__ = "Integer32"
_AgentVMTracerIfIndex_Object = MibTableColumn
agentVMTracerIfIndex = _AgentVMTracerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 1, 1, 1),
    _AgentVMTracerIfIndex_Type()
)
agentVMTracerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerIfIndex.setStatus("current")


class _AgentVMTracerAdminMode_Type(Integer32):
    """Custom type agentVMTracerAdminMode based on Integer32"""
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


_AgentVMTracerAdminMode_Type.__name__ = "Integer32"
_AgentVMTracerAdminMode_Object = MibTableColumn
agentVMTracerAdminMode = _AgentVMTracerAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 1, 1, 2),
    _AgentVMTracerAdminMode_Type()
)
agentVMTracerAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerAdminMode.setStatus("current")
_AgentVMTracerSessionTable_Object = MibTable
agentVMTracerSessionTable = _AgentVMTracerSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2)
)
if mibBuilder.loadTexts:
    agentVMTracerSessionTable.setStatus("current")
_AgentVMTracerSessionEntry_Object = MibTableRow
agentVMTracerSessionEntry = _AgentVMTracerSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1)
)
agentVMTracerSessionEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentVMTracerSessionIndex"),
)
if mibBuilder.loadTexts:
    agentVMTracerSessionEntry.setStatus("current")


class _AgentVMTracerSessionIndex_Type(Integer32):
    """Custom type agentVMTracerSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AgentVMTracerSessionIndex_Type.__name__ = "Integer32"
_AgentVMTracerSessionIndex_Object = MibTableColumn
agentVMTracerSessionIndex = _AgentVMTracerSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 1),
    _AgentVMTracerSessionIndex_Type()
)
agentVMTracerSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerSessionIndex.setStatus("current")


class _AgentVMTracerSessionName_Type(DisplayString):
    """Custom type agentVMTracerSessionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentVMTracerSessionName_Type.__name__ = "DisplayString"
_AgentVMTracerSessionName_Object = MibTableColumn
agentVMTracerSessionName = _AgentVMTracerSessionName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 2),
    _AgentVMTracerSessionName_Type()
)
agentVMTracerSessionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerSessionName.setStatus("current")


class _AgentVMTracerSessionUrl_Type(DisplayString):
    """Custom type agentVMTracerSessionUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentVMTracerSessionUrl_Type.__name__ = "DisplayString"
_AgentVMTracerSessionUrl_Object = MibTableColumn
agentVMTracerSessionUrl = _AgentVMTracerSessionUrl_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 3),
    _AgentVMTracerSessionUrl_Type()
)
agentVMTracerSessionUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerSessionUrl.setStatus("current")


class _AgentVMTracerSessionUsername_Type(DisplayString):
    """Custom type agentVMTracerSessionUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentVMTracerSessionUsername_Type.__name__ = "DisplayString"
_AgentVMTracerSessionUsername_Object = MibTableColumn
agentVMTracerSessionUsername = _AgentVMTracerSessionUsername_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 4),
    _AgentVMTracerSessionUsername_Type()
)
agentVMTracerSessionUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerSessionUsername.setStatus("current")


class _AgentVMTracerSessionPassword_Type(DisplayString):
    """Custom type agentVMTracerSessionPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentVMTracerSessionPassword_Type.__name__ = "DisplayString"
_AgentVMTracerSessionPassword_Object = MibTableColumn
agentVMTracerSessionPassword = _AgentVMTracerSessionPassword_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 5),
    _AgentVMTracerSessionPassword_Type()
)
agentVMTracerSessionPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerSessionPassword.setStatus("current")


class _AgentVMTracerSessionAutoVlanMode_Type(Integer32):
    """Custom type agentVMTracerSessionAutoVlanMode based on Integer32"""
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


_AgentVMTracerSessionAutoVlanMode_Type.__name__ = "Integer32"
_AgentVMTracerSessionAutoVlanMode_Object = MibTableColumn
agentVMTracerSessionAutoVlanMode = _AgentVMTracerSessionAutoVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 6),
    _AgentVMTracerSessionAutoVlanMode_Type()
)
agentVMTracerSessionAutoVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerSessionAutoVlanMode.setStatus("current")
_AgentVMTracerSessionAllowVlan_Type = VlanList
_AgentVMTracerSessionAllowVlan_Object = MibTableColumn
agentVMTracerSessionAllowVlan = _AgentVMTracerSessionAllowVlan_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 7),
    _AgentVMTracerSessionAllowVlan_Type()
)
agentVMTracerSessionAllowVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerSessionAllowVlan.setStatus("current")


class _AgentVMTracerSessionConnectionStatus_Type(Integer32):
    """Custom type agentVMTracerSessionConnectionStatus based on Integer32"""
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


_AgentVMTracerSessionConnectionStatus_Type.__name__ = "Integer32"
_AgentVMTracerSessionConnectionStatus_Object = MibTableColumn
agentVMTracerSessionConnectionStatus = _AgentVMTracerSessionConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 8),
    _AgentVMTracerSessionConnectionStatus_Type()
)
agentVMTracerSessionConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerSessionConnectionStatus.setStatus("current")


class _AgentVMTracerSessionClear_Type(Integer32):
    """Custom type agentVMTracerSessionClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AgentVMTracerSessionClear_Type.__name__ = "Integer32"
_AgentVMTracerSessionClear_Object = MibTableColumn
agentVMTracerSessionClear = _AgentVMTracerSessionClear_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 2, 1, 9),
    _AgentVMTracerSessionClear_Type()
)
agentVMTracerSessionClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentVMTracerSessionClear.setStatus("current")
_AgentVMTracerVMTable_Object = MibTable
agentVMTracerVMTable = _AgentVMTracerVMTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3)
)
if mibBuilder.loadTexts:
    agentVMTracerVMTable.setStatus("current")
_AgentVMTracerVMEntry_Object = MibTableRow
agentVMTracerVMEntry = _AgentVMTracerVMEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1)
)
agentVMTracerVMEntry.setIndexNames(
    (0, "SWITCHING-EXTENSION-MIB", "agentVMTracerSessionIndex"),
    (0, "SWITCHING-EXTENSION-MIB", "agentVMTracerVMIndex"),
)
if mibBuilder.loadTexts:
    agentVMTracerVMEntry.setStatus("current")


class _AgentVMTracerVMIndex_Type(Integer32):
    """Custom type agentVMTracerVMIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentVMTracerVMIndex_Type.__name__ = "Integer32"
_AgentVMTracerVMIndex_Object = MibTableColumn
agentVMTracerVMIndex = _AgentVMTracerVMIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 1),
    _AgentVMTracerVMIndex_Type()
)
agentVMTracerVMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMIndex.setStatus("current")
_AgentVMTracerVMName_Type = DisplayString
_AgentVMTracerVMName_Object = MibTableColumn
agentVMTracerVMName = _AgentVMTracerVMName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 2),
    _AgentVMTracerVMName_Type()
)
agentVMTracerVMName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMName.setStatus("current")
_AgentVMTracerVMInterface_Type = DisplayString
_AgentVMTracerVMInterface_Object = MibTableColumn
agentVMTracerVMInterface = _AgentVMTracerVMInterface_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 3),
    _AgentVMTracerVMInterface_Type()
)
agentVMTracerVMInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMInterface.setStatus("current")
_AgentVMTracerVMAdapter_Type = DisplayString
_AgentVMTracerVMAdapter_Object = MibTableColumn
agentVMTracerVMAdapter = _AgentVMTracerVMAdapter_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 4),
    _AgentVMTracerVMAdapter_Type()
)
agentVMTracerVMAdapter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMAdapter.setStatus("current")
_AgentVMTracerVMMacAddress_Type = DisplayString
_AgentVMTracerVMMacAddress_Object = MibTableColumn
agentVMTracerVMMacAddress = _AgentVMTracerVMMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 5),
    _AgentVMTracerVMMacAddress_Type()
)
agentVMTracerVMMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMMacAddress.setStatus("current")
_AgentVMTracerVMPortGroup_Type = DisplayString
_AgentVMTracerVMPortGroup_Object = MibTableColumn
agentVMTracerVMPortGroup = _AgentVMTracerVMPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 6),
    _AgentVMTracerVMPortGroup_Type()
)
agentVMTracerVMPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMPortGroup.setStatus("current")
_AgentVMTracerVMVlanId_Type = Unsigned32
_AgentVMTracerVMVlanId_Object = MibTableColumn
agentVMTracerVMVlanId = _AgentVMTracerVMVlanId_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 7),
    _AgentVMTracerVMVlanId_Type()
)
agentVMTracerVMVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMVlanId.setStatus("current")
_AgentVMTracerVMSwitch_Type = DisplayString
_AgentVMTracerVMSwitch_Object = MibTableColumn
agentVMTracerVMSwitch = _AgentVMTracerVMSwitch_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 8),
    _AgentVMTracerVMSwitch_Type()
)
agentVMTracerVMSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMSwitch.setStatus("current")
_AgentVMTracerVMHost_Type = DisplayString
_AgentVMTracerVMHost_Object = MibTableColumn
agentVMTracerVMHost = _AgentVMTracerVMHost_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 9),
    _AgentVMTracerVMHost_Type()
)
agentVMTracerVMHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMHost.setStatus("current")
_AgentVMTracerVMHostCpuSpeed_Type = DisplayString
_AgentVMTracerVMHostCpuSpeed_Object = MibTableColumn
agentVMTracerVMHostCpuSpeed = _AgentVMTracerVMHostCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 10),
    _AgentVMTracerVMHostCpuSpeed_Type()
)
agentVMTracerVMHostCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMHostCpuSpeed.setStatus("current")
_AgentVMTracerVMHostMemory_Type = DisplayString
_AgentVMTracerVMHostMemory_Object = MibTableColumn
agentVMTracerVMHostMemory = _AgentVMTracerVMHostMemory_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 11),
    _AgentVMTracerVMHostMemory_Type()
)
agentVMTracerVMHostMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMHostMemory.setStatus("current")
_AgentVMTracerVMHostSystem_Type = DisplayString
_AgentVMTracerVMHostSystem_Object = MibTableColumn
agentVMTracerVMHostSystem = _AgentVMTracerVMHostSystem_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 12),
    _AgentVMTracerVMHostSystem_Type()
)
agentVMTracerVMHostSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMHostSystem.setStatus("current")
_AgentVMTracerVMHostVendor_Type = DisplayString
_AgentVMTracerVMHostVendor_Object = MibTableColumn
agentVMTracerVMHostVendor = _AgentVMTracerVMHostVendor_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 13),
    _AgentVMTracerVMHostVendor_Type()
)
agentVMTracerVMHostVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMHostVendor.setStatus("current")
_AgentVMTracerVMHostCpuCores_Type = Unsigned32
_AgentVMTracerVMHostCpuCores_Object = MibTableColumn
agentVMTracerVMHostCpuCores = _AgentVMTracerVMHostCpuCores_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 14),
    _AgentVMTracerVMHostCpuCores_Type()
)
agentVMTracerVMHostCpuCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMHostCpuCores.setStatus("current")
_AgentVMTracerVMHostCpuPackages_Type = Unsigned32
_AgentVMTracerVMHostCpuPackages_Object = MibTableColumn
agentVMTracerVMHostCpuPackages = _AgentVMTracerVMHostCpuPackages_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 101, 120, 3, 1, 15),
    _AgentVMTracerVMHostCpuPackages_Type()
)
agentVMTracerVMHostCpuPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentVMTracerVMHostCpuPackages.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCHING-EXTENSION-MIB",
    **{"BridgeEvbTLVTC": BridgeEvbTLVTC,
       "switchingExtension": switchingExtension,
       "agentInfoGroupExtension": agentInfoGroupExtension,
       "agentInventoryGroupExtension": agentInventoryGroupExtension,
       "agentInventroyHardwareVersion": agentInventroyHardwareVersion,
       "agentInventoryLoaderVersion": agentInventoryLoaderVersion,
       "agentInventoryBootRomVersion": agentInventoryBootRomVersion,
       "agentInventoryOpCodeVersion": agentInventoryOpCodeVersion,
       "agentInventoryLabelRevNumber": agentInventoryLabelRevNumber,
       "agentTemperatureFanStatusTable": agentTemperatureFanStatusTable,
       "agentTemperatureFanStatusEntry": agentTemperatureFanStatusEntry,
       "agentTemperatureFanUnitIndex": agentTemperatureFanUnitIndex,
       "agentTemperature": agentTemperature,
       "agentTemperature1": agentTemperature1,
       "agentTemperature2": agentTemperature2,
       "agentTemperature3": agentTemperature3,
       "agentTemperature4": agentTemperature4,
       "agentTemperature5": agentTemperature5,
       "agentFAN1": agentFAN1,
       "agentFAN2": agentFAN2,
       "agentFAN3": agentFAN3,
       "agentFAN4": agentFAN4,
       "agentFANChipType": agentFANChipType,
       "agentPowerSupplyStatusTable": agentPowerSupplyStatusTable,
       "agentPowerSupplyStatusEntry": agentPowerSupplyStatusEntry,
       "agentPowerSupplyUnitIndex": agentPowerSupplyUnitIndex,
       "agentPowerSupplyStatus": agentPowerSupplyStatus,
       "agentPowerSupplyName": agentPowerSupplyName,
       "agentPowerSupplyModel": agentPowerSupplyModel,
       "agentPowerSupplyRevisionNumber": agentPowerSupplyRevisionNumber,
       "agentPowerSupplyManufacturerLocation": agentPowerSupplyManufacturerLocation,
       "agentPowerSupplyManufacturingDate": agentPowerSupplyManufacturingDate,
       "agentPowerSupplySerialNumber": agentPowerSupplySerialNumber,
       "agentPowerSupplyTemperature1": agentPowerSupplyTemperature1,
       "agentPowerSupplyTemperature2": agentPowerSupplyTemperature2,
       "agentPowerSupplyFanSpeed": agentPowerSupplyFanSpeed,
       "agentPowerSupplyFanDuty": agentPowerSupplyFanDuty,
       "agentPowerConsumption": agentPowerConsumption,
       "agentDOMTable": agentDOMTable,
       "agentDOMEntry": agentDOMEntry,
       "agentDOMtransceiverIndex": agentDOMtransceiverIndex,
       "agentDOMTemperature": agentDOMTemperature,
       "agentDOMVoltage": agentDOMVoltage,
       "agentDOMBias": agentDOMBias,
       "agentDOMTxpower": agentDOMTxpower,
       "agentDOMRxpower": agentDOMRxpower,
       "agentDOMtemperatureHighAlarm": agentDOMtemperatureHighAlarm,
       "agentDOMtemperatureHighWarning": agentDOMtemperatureHighWarning,
       "agentDOMtemperatureLowWarning": agentDOMtemperatureLowWarning,
       "agentDOMtemperatureLowAlarm": agentDOMtemperatureLowAlarm,
       "agentDOMvotageHighAlarm": agentDOMvotageHighAlarm,
       "agentDOMvotageHighWarning": agentDOMvotageHighWarning,
       "agentDOMvotageLowWarning": agentDOMvotageLowWarning,
       "agentDOMvotageLowAlarm": agentDOMvotageLowAlarm,
       "agentDOMbiasHighAlarm": agentDOMbiasHighAlarm,
       "agentDOMbiasHighWarning": agentDOMbiasHighWarning,
       "agentDOMbiasLowWarning": agentDOMbiasLowWarning,
       "agentDOMbiasLowAlarm": agentDOMbiasLowAlarm,
       "agentDOMtxpowerHighAlarm": agentDOMtxpowerHighAlarm,
       "agentDOMtxpowerHighWarning": agentDOMtxpowerHighWarning,
       "agentDOMtxpowerLowWarning": agentDOMtxpowerLowWarning,
       "agentDOMtxpowerLowAlarm": agentDOMtxpowerLowAlarm,
       "agentDOMrxpowerHighAlarm": agentDOMrxpowerHighAlarm,
       "agentDOMrxpowerHighWarning": agentDOMrxpowerHighWarning,
       "agentDOMrxpowerLowWarning": agentDOMrxpowerLowWarning,
       "agentDOMrxpowerLowAlarm": agentDOMrxpowerLowAlarm,
       "agent10GModuleInfoGroupExtension": agent10GModuleInfoGroupExtension,
       "agent10GModuleTable": agent10GModuleTable,
       "agent10GModuleEntry": agent10GModuleEntry,
       "agent10GModuleUnitIndex": agent10GModuleUnitIndex,
       "agent10GModuleSlotIndex": agent10GModuleSlotIndex,
       "agent10GModulePortIndex": agent10GModulePortIndex,
       "agent10GModuleIndex": agent10GModuleIndex,
       "agent10GModuleInterfaceNumber": agent10GModuleInterfaceNumber,
       "agent10GModuleType": agent10GModuleType,
       "agent10GModuleComplianceCode": agent10GModuleComplianceCode,
       "agent10GModuleVendorName": agent10GModuleVendorName,
       "agent10GModulePartNumber": agent10GModulePartNumber,
       "agent10GModuleSerialNumber": agent10GModuleSerialNumber,
       "agent10GModuleRevisionNumber": agent10GModuleRevisionNumber,
       "agent10GModuleManufacturingDate": agent10GModuleManufacturingDate,
       "agentGBICInfoTable": agentGBICInfoTable,
       "agentGBICInfoEntry": agentGBICInfoEntry,
       "agentGBICInfoIndex": agentGBICInfoIndex,
       "agentGBICInfoInterfaceNumber": agentGBICInfoInterfaceNumber,
       "agentGBICInfoComplianceCode": agentGBICInfoComplianceCode,
       "agentGBICInfoVendorName": agentGBICInfoVendorName,
       "agentGBICInfoPartNumber": agentGBICInfoPartNumber,
       "agentGBICInfoSerialNumber": agentGBICInfoSerialNumber,
       "agentGBICInfoRevisionNumber": agentGBICInfoRevisionNumber,
       "agentGBICInfoManufacturingDate": agentGBICInfoManufacturingDate,
       "agentConfigGroupExtension": agentConfigGroupExtension,
       "agentCLIConfigGroupExtension": agentCLIConfigGroupExtension,
       "agentSerialGroupExtension": agentSerialGroupExtension,
       "agentSerialPasswdCnt": agentSerialPasswdCnt,
       "agentSerialPasswdCntSetToDefault": agentSerialPasswdCntSetToDefault,
       "agentSerialSilentTime": agentSerialSilentTime,
       "agentSerialSilentTimeSetToDefault": agentSerialSilentTimeSetToDefault,
       "agentVtyGroupExtension": agentVtyGroupExtension,
       "agentVtyTelnetServerAdminMode": agentVtyTelnetServerAdminMode,
       "agentVtyPasswdCnt": agentVtyPasswdCnt,
       "agentVtyPasswdCntSetToDefault": agentVtyPasswdCntSetToDefault,
       "agentVtyTerminalLength": agentVtyTerminalLength,
       "agentVtyTerminalLengthSetToDefault": agentVtyTerminalLengthSetToDefault,
       "agentNetworkConfigGroupExtension": agentNetworkConfigGroupExtension,
       "agentNetworkHttpPort": agentNetworkHttpPort,
       "agentNetworkDhcpClientIfClientIdFormat": agentNetworkDhcpClientIfClientIdFormat,
       "agentNetworkDhcpClientIfClientId": agentNetworkDhcpClientIfClientId,
       "agentNetworkDhcpSetToInventoryClientIfClientId": agentNetworkDhcpSetToInventoryClientIfClientId,
       "agentNetworkDhcpRestart": agentNetworkDhcpRestart,
       "agentSwitchConfigGroupExtension": agentSwitchConfigGroupExtension,
       "agentSwitchSnoopingGroupExtension": agentSwitchSnoopingGroupExtension,
       "agentIgmpSnoopL2MulticastStaticTable": agentIgmpSnoopL2MulticastStaticTable,
       "agentIgmpSnoopL2MulticastStaticEntry": agentIgmpSnoopL2MulticastStaticEntry,
       "agentIgmpSnoopL2MulticastStaticIndex": agentIgmpSnoopL2MulticastStaticIndex,
       "agentIgmpSnoopL2MulticastStaticVlanId": agentIgmpSnoopL2MulticastStaticVlanId,
       "agentIgmpSnoopL2MulticastStaticMacAddress": agentIgmpSnoopL2MulticastStaticMacAddress,
       "agentIgmpSnoopL2MulticastStaticMemberPortMask": agentIgmpSnoopL2MulticastStaticMemberPortMask,
       "agentIgmpSnoopL2MulticastStaticActivePortMask": agentIgmpSnoopL2MulticastStaticActivePortMask,
       "agentIgmpSnoopL2MulticastStaticMemberPorts": agentIgmpSnoopL2MulticastStaticMemberPorts,
       "agentIgmpSnoopL2MulticastStaticActivePorts": agentIgmpSnoopL2MulticastStaticActivePorts,
       "agentMldSnoopL2MulticastStaticTable": agentMldSnoopL2MulticastStaticTable,
       "agentMldSnoopL2MulticastStaticEntry": agentMldSnoopL2MulticastStaticEntry,
       "agentMldSnoopL2MulticastStaticIndex": agentMldSnoopL2MulticastStaticIndex,
       "agentMldSnoopL2MulticastStaticVlanId": agentMldSnoopL2MulticastStaticVlanId,
       "agentMldSnoopL2MulticastStaticMacAddress": agentMldSnoopL2MulticastStaticMacAddress,
       "agentMldSnoopL2MulticastStaticMemberPortMask": agentMldSnoopL2MulticastStaticMemberPortMask,
       "agentMldSnoopL2MulticastStaticActivePortMask": agentMldSnoopL2MulticastStaticActivePortMask,
       "agentMldSnoopL2MulticastStaticMemberPorts": agentMldSnoopL2MulticastStaticMemberPorts,
       "agentMldSnoopL2MulticastStaticActivePorts": agentMldSnoopL2MulticastStaticActivePorts,
       "agentIPFilterConfigGroupExtension": agentIPFilterConfigGroupExtension,
       "agentIPFilterConfigAdminMode": agentIPFilterConfigAdminMode,
       "agentIpFilterConfigCreate": agentIpFilterConfigCreate,
       "agentIpFilterConfigDelete": agentIpFilterConfigDelete,
       "agentIpFilterConfigTable": agentIpFilterConfigTable,
       "agentIpFilterConfigEntry": agentIpFilterConfigEntry,
       "agentIpFilterConfigIndex": agentIpFilterConfigIndex,
       "agentIpFilterConfigIP": agentIpFilterConfigIP,
       "agentIpFilterConfigMask": agentIpFilterConfigMask,
       "agentIpFilterConfigName": agentIpFilterConfigName,
       "agentStormContorlConfigGroupExtension": agentStormContorlConfigGroupExtension,
       "agentSwitchBroadcastControlMode": agentSwitchBroadcastControlMode,
       "agentSwitchMulticastControlMode": agentSwitchMulticastControlMode,
       "agentSwitchUnicastControlMode": agentSwitchUnicastControlMode,
       "agentSwitchDot3FlowControlMode": agentSwitchDot3FlowControlMode,
       "agentSwitchStormControlBroadcastTable": agentSwitchStormControlBroadcastTable,
       "agentSwitchStormControlBroadcastEntry": agentSwitchStormControlBroadcastEntry,
       "agentSwitchBcastStormIfIndex": agentSwitchBcastStormIfIndex,
       "agentSwitchBcastStormExtensionPktRate": agentSwitchBcastStormExtensionPktRate,
       "agentSwitchBcastStormExtensionAdminMode": agentSwitchBcastStormExtensionAdminMode,
       "agentSwitchStormControlMulticastTable": agentSwitchStormControlMulticastTable,
       "agentSwitchStormControlMulticastEntry": agentSwitchStormControlMulticastEntry,
       "agentSwitchMcastStormIfIndex": agentSwitchMcastStormIfIndex,
       "agentSwitchMcastStormExtensionPktRate": agentSwitchMcastStormExtensionPktRate,
       "agentSwitchMcastStormExtensionAdminMode": agentSwitchMcastStormExtensionAdminMode,
       "agentSwitchStormControlUnicastTable": agentSwitchStormControlUnicastTable,
       "agentSwitchStormControlUnicastEntry": agentSwitchStormControlUnicastEntry,
       "agentSwitchUcastStormIfIndex": agentSwitchUcastStormIfIndex,
       "agentSwitchUcastStormExtensionPktRate": agentSwitchUcastStormExtensionPktRate,
       "agentSwitchUcastStormExtensionAdminMode": agentSwitchUcastStormExtensionAdminMode,
       "agentSwitchFlowControlTable": agentSwitchFlowControlTable,
       "agentSwitchFlowControlEntry": agentSwitchFlowControlEntry,
       "agentSwitchFlowControlIfIndex": agentSwitchFlowControlIfIndex,
       "agentSwitchFlowControlAdminMode": agentSwitchFlowControlAdminMode,
       "agentSwitchStormControlActionTable": agentSwitchStormControlActionTable,
       "agentSwitchStormControlActionEntry": agentSwitchStormControlActionEntry,
       "agentSwitchStormControlActionIfIndex": agentSwitchStormControlActionIfIndex,
       "agentSwitchStormControlActionShutdownMode": agentSwitchStormControlActionShutdownMode,
       "agentSwitchStormControlActionTrapMode": agentSwitchStormControlActionTrapMode,
       "agentErrRecoveryConfigGroupExtension": agentErrRecoveryConfigGroupExtension,
       "agentErrRecoveryInterval": agentErrRecoveryInterval,
       "agentErrRecoveryStormCtrlCauseMode": agentErrRecoveryStormCtrlCauseMode,
       "agentErrRecoveryUdldCauseMode": agentErrRecoveryUdldCauseMode,
       "agentErrRecoveryPortSecurityCauseMode": agentErrRecoveryPortSecurityCauseMode,
       "agentErrRecoveryBpduCauseMode": agentErrRecoveryBpduCauseMode,
       "agentErrRecoveryLinkFlapCauseMode": agentErrRecoveryLinkFlapCauseMode,
       "agentErrRecoveryMacFlapCauseMode": agentErrRecoveryMacFlapCauseMode,
       "agentErrDetectLinkFlapCauseMode": agentErrDetectLinkFlapCauseMode,
       "agentErrDetectMacFlapCauseMode": agentErrDetectMacFlapCauseMode,
       "agentTransferConfigGroupExtension": agentTransferConfigGroupExtension,
       "agentTransferCopyGroup": agentTransferCopyGroup,
       "agentTransferCopyRunningConfigToSwitchDestFilename": agentTransferCopyRunningConfigToSwitchDestFilename,
       "agentTransferCopyRunningConfigStart": agentTransferCopyRunningConfigStart,
       "agentTransferCopyRunningConfigStatus": agentTransferCopyRunningConfigStatus,
       "agentTransferDeleteGroup": agentTransferDeleteGroup,
       "agentTransferDeleteSwitchFilename": agentTransferDeleteSwitchFilename,
       "agentTransferDeleteStart": agentTransferDeleteStart,
       "agentTransferDeleteStatus": agentTransferDeleteStatus,
       "agentPortConfigExtensionTable": agentPortConfigExtensionTable,
       "agentPortConfigExtensionEntry": agentPortConfigExtensionEntry,
       "agentPortConfigExtensionIfIndex": agentPortConfigExtensionIfIndex,
       "agentPortConfigExtensionAdminMode": agentPortConfigExtensionAdminMode,
       "agentPortConfigExtensionLinkTrapMode": agentPortConfigExtensionLinkTrapMode,
       "agentPortConfigExtensionClearStats": agentPortConfigExtensionClearStats,
       "agentPortConfigExtensionMaxFrameSizeLimit": agentPortConfigExtensionMaxFrameSizeLimit,
       "agentPortConfigExtensionMaxFrameSize": agentPortConfigExtensionMaxFrameSize,
       "agentLinkStateConfigGroup": agentLinkStateConfigGroup,
       "agentLinkStateConfigAdminMode": agentLinkStateConfigAdminMode,
       "agentLinkStateGroupTable": agentLinkStateGroupTable,
       "agentLinkStateGroupEntry": agentLinkStateGroupEntry,
       "agentLinkStateGroupId": agentLinkStateGroupId,
       "agentLinkStateGroupMode": agentLinkStateGroupMode,
       "agentLinkStateGroupUpstreamPort": agentLinkStateGroupUpstreamPort,
       "agentLinkStateGroupDownstreamPort": agentLinkStateGroupDownstreamPort,
       "agentLinkStateGroupStatus": agentLinkStateGroupStatus,
       "agentPortBackupConfigGroup": agentPortBackupConfigGroup,
       "agentPortBackupConfigAdminMode": agentPortBackupConfigAdminMode,
       "agentPortBackupGroupTable": agentPortBackupGroupTable,
       "agentPortBackupGroupEntry": agentPortBackupGroupEntry,
       "agentPortBackupGroupId": agentPortBackupGroupId,
       "agentPortBackupGroupMode": agentPortBackupGroupMode,
       "agentPortBackupGroupActivePort": agentPortBackupGroupActivePort,
       "agentPortBackupGroupBackupPort": agentPortBackupGroupBackupPort,
       "agentMacMoveUpdatetMode": agentMacMoveUpdatetMode,
       "agentPortBackupGroupStatus": agentPortBackupGroupStatus,
       "agentPortBackupGroupFailBackTime": agentPortBackupGroupFailBackTime,
       "agentDOMGroup": agentDOMGroup,
       "agentDOMAdminMode": agentDOMAdminMode,
       "agentDOMInterval": agentDOMInterval,
       "agentSwitchCurrBootFilesGroupExtension": agentSwitchCurrBootFilesGroupExtension,
       "agentSwitchCurrBootRomFileName": agentSwitchCurrBootRomFileName,
       "agentSwitchCurrBootLoaderFileName": agentSwitchCurrBootLoaderFileName,
       "agentSwitchCurrBootConfigFileName": agentSwitchCurrBootConfigFileName,
       "agentSwitchCurrBootOpCodeFileName": agentSwitchCurrBootOpCodeFileName,
       "agentSwitchCurrUBootFileName": agentSwitchCurrUBootFileName,
       "agentSwitchCurrKernelFileName": agentSwitchCurrKernelFileName,
       "agentSwitchCurrVMTracerFileName": agentSwitchCurrVMTracerFileName,
       "agentCDPConfigGroup": agentCDPConfigGroup,
       "agentCDPConfigAdminMode": agentCDPConfigAdminMode,
       "agentCDPConfigTimeToLive": agentCDPConfigTimeToLive,
       "agentCDPConfigTransmitInterval": agentCDPConfigTransmitInterval,
       "agentCDPConfigNumInPkts": agentCDPConfigNumInPkts,
       "agentCDPConfigNumOutPkts": agentCDPConfigNumOutPkts,
       "agentCDPConfigNumErrPkts": agentCDPConfigNumErrPkts,
       "agentCDPConfigResetNumPkts": agentCDPConfigResetNumPkts,
       "agentCDPConfigResetDeviceInformation": agentCDPConfigResetDeviceInformation,
       "agentCDPConfigPortModeTable": agentCDPConfigPortModeTable,
       "agentCDPConfigPortModeEntry": agentCDPConfigPortModeEntry,
       "agentCDPConfigPortModeIfIndex": agentCDPConfigPortModeIfIndex,
       "agentCDPConfigPortModeAdminMode": agentCDPConfigPortModeAdminMode,
       "agentCDPConfigNeighborInfoTable": agentCDPConfigNeighborInfoTable,
       "agentCDPConfigNeighborInfoEntry": agentCDPConfigNeighborInfoEntry,
       "agentCDPConfigNeighborInfoIndex": agentCDPConfigNeighborInfoIndex,
       "agentCDPConfigNeighborInfoDeviceID": agentCDPConfigNeighborInfoDeviceID,
       "agentCDPConfigNeighborInfoLocalIF": agentCDPConfigNeighborInfoLocalIF,
       "agentCDPConfigNeighborInfoHoldTime": agentCDPConfigNeighborInfoHoldTime,
       "agentCDPConfigNeighborInfoCapability": agentCDPConfigNeighborInfoCapability,
       "agentCDPConfigNeighborInfoPlatform": agentCDPConfigNeighborInfoPlatform,
       "agentCDPConfigNeighborInfoPortID": agentCDPConfigNeighborInfoPortID,
       "agentCDPConfigNeighborInfoManagementAddress": agentCDPConfigNeighborInfoManagementAddress,
       "agentVlanVoiceConfigGroup": agentVlanVoiceConfigGroup,
       "agentVlanVoiceVlanIDCreate": agentVlanVoiceVlanIDCreate,
       "agentVlanVoiceAdminMode": agentVlanVoiceAdminMode,
       "agentVlanVoiceMacAddress": agentVlanVoiceMacAddress,
       "agentVlanVoiceMacMask": agentVlanVoiceMacMask,
       "agentVlanVoicePriority": agentVlanVoicePriority,
       "agentVlanVoiceName": agentVlanVoiceName,
       "agentVlanVoiceConfigTable": agentVlanVoiceConfigTable,
       "agentVlanVoiceConfigEntry": agentVlanVoiceConfigEntry,
       "agentVlanVoiceConfigIndex": agentVlanVoiceConfigIndex,
       "agentVlanVoiceConfigName": agentVlanVoiceConfigName,
       "agentVlanVoiceConfigMacAddress": agentVlanVoiceConfigMacAddress,
       "agentVlanVoiceConfigMacMask": agentVlanVoiceConfigMacMask,
       "agentVlanVoiceConfigPriority": agentVlanVoiceConfigPriority,
       "agentVlanVoiceConfigDelete": agentVlanVoiceConfigDelete,
       "agentVoiceVlanConfigGroup": agentVoiceVlanConfigGroup,
       "agentVoiceVlanAdminMode": agentVoiceVlanAdminMode,
       "agentVoiceVlanConfigTable": agentVoiceVlanConfigTable,
       "agentVoiceVlanConfigEntry": agentVoiceVlanConfigEntry,
       "agentVoiceVlanConfigIndex": agentVoiceVlanConfigIndex,
       "agentVoiceVlanConfigIfMode": agentVoiceVlanConfigIfMode,
       "agentVoiceVlanConfigIfModeValue": agentVoiceVlanConfigIfModeValue,
       "agentVoiceVlanConfigCosOverrideMode": agentVoiceVlanConfigCosOverrideMode,
       "agentVoiceVlanConfigOperState": agentVoiceVlanConfigOperState,
       "agentVTPConfigGroup": agentVTPConfigGroup,
       "agentVTPAdminMode": agentVTPAdminMode,
       "agentVTPVersion": agentVTPVersion,
       "agentVTPConfigRevision": agentVTPConfigRevision,
       "agentVTPMaxVlanNumSupported": agentVTPMaxVlanNumSupported,
       "agentVTPVlanNumSupported": agentVTPVlanNumSupported,
       "agentVTPOperatingMode": agentVTPOperatingMode,
       "agentVTPDomainName": agentVTPDomainName,
       "agentVTPPruningMode": agentVTPPruningMode,
       "agentVTPDomainPassword": agentVTPDomainPassword,
       "agentVTPV2Mode": agentVTPV2Mode,
       "agentVTPMD5Digest": agentVTPMD5Digest,
       "agentVTPConfigLastModified": agentVTPConfigLastModified,
       "agentVTPLocalUpdaterID": agentVTPLocalUpdaterID,
       "agentVTPPortConfigTable": agentVTPPortConfigTable,
       "agentVTPPortConfigEntry": agentVTPPortConfigEntry,
       "agentVTPPortConfigIndex": agentVTPPortConfigIndex,
       "agentVTPPortConfigTrunkMode": agentVTPPortConfigTrunkMode,
       "agentFIPSnoopingGroup": agentFIPSnoopingGroup,
       "agentFIPSnoopingAdminMode": agentFIPSnoopingAdminMode,
       "agentFIPSnoopingVlanConfigTable": agentFIPSnoopingVlanConfigTable,
       "agentFIPSnoopingVlanConfigEntry": agentFIPSnoopingVlanConfigEntry,
       "agentFIPSnoopingVlanIndex": agentFIPSnoopingVlanIndex,
       "agentFIPSnoopingVlanAdminMode": agentFIPSnoopingVlanAdminMode,
       "agentFIPSnoopingSessionTable": agentFIPSnoopingSessionTable,
       "agentFIPSnoopingSessionEntry": agentFIPSnoopingSessionEntry,
       "agentFIPSnoopingSessionKey": agentFIPSnoopingSessionKey,
       "agentFIPSnoopingSessionIfIndex": agentFIPSnoopingSessionIfIndex,
       "agentFIPSnoopingSessionFCFMacAddress": agentFIPSnoopingSessionFCFMacAddress,
       "agentFIPSnoopingSessionENodeMacAddress": agentFIPSnoopingSessionENodeMacAddress,
       "agentFIPSnoopingSessionENodeIfIndex": agentFIPSnoopingSessionENodeIfIndex,
       "agentFIPSnoopingFCFTable": agentFIPSnoopingFCFTable,
       "agentFIPSnoopingFCFEntry": agentFIPSnoopingFCFEntry,
       "agentFIPSnoopingFCFKey": agentFIPSnoopingFCFKey,
       "agentFIPSnoopingFCFIfIndex": agentFIPSnoopingFCFIfIndex,
       "agentFIPSnoopingFCFVlan": agentFIPSnoopingFCFVlan,
       "agentFIPSnoopingFCFENodeNumber": agentFIPSnoopingFCFENodeNumber,
       "agentFIPSnoopingFCFFCMap": agentFIPSnoopingFCFFCMap,
       "agentFIPSnoopingFCFSwitchName": agentFIPSnoopingFCFSwitchName,
       "agentFIPSnoopingFCFFabricName": agentFIPSnoopingFCFFabricName,
       "agentFIPSnoopingENodeTable": agentFIPSnoopingENodeTable,
       "agentFIPSnoopingENodeEntry": agentFIPSnoopingENodeEntry,
       "agentFIPSnoopingENodeKey": agentFIPSnoopingENodeKey,
       "agentFIPSnoopingENodeIfIndex": agentFIPSnoopingENodeIfIndex,
       "agentFIPSnoopingENodeVlan": agentFIPSnoopingENodeVlan,
       "agentFIPSnoopingENodeNameID": agentFIPSnoopingENodeNameID,
       "agentMLAGGroup": agentMLAGGroup,
       "agentMLAGAdminMode": agentMLAGAdminMode,
       "agentMLAGDomainId": agentMLAGDomainId,
       "agentMLAGConfigurationConsistancyStatus": agentMLAGConfigurationConsistancyStatus,
       "agentMLAGMemberCount": agentMLAGMemberCount,
       "agentMLAGSystemMac": agentMLAGSystemMac,
       "agentMLAGKeepaliveTimeout": agentMLAGKeepaliveTimeout,
       "agentMLAGPeerGatewayMode": agentMLAGPeerGatewayMode,
       "agentMLAGDelayRestore": agentMLAGDelayRestore,
       "agentMLAGMemberLinkdownMode": agentMLAGMemberLinkdownMode,
       "agentMLAGPeerLinkGroup": agentMLAGPeerLinkGroup,
       "agentMLAGPeerLinkifIndex": agentMLAGPeerLinkifIndex,
       "agentMLAGPeerLinkifStatus": agentMLAGPeerLinkifStatus,
       "agentMLAGPeerLinkActiveVlans": agentMLAGPeerLinkActiveVlans,
       "agentMLAGPeerLinkForbiddenVlans": agentMLAGPeerLinkForbiddenVlans,
       "agentMLAGPortChannelTable": agentMLAGPortChannelTable,
       "agentMLAGPortChannelEntry": agentMLAGPortChannelEntry,
       "agentMLAGPortChannelifIndex": agentMLAGPortChannelifIndex,
       "agentMLAGPortChannelId": agentMLAGPortChannelId,
       "agentMLAGPortChannelifIndexStatus": agentMLAGPortChannelifIndexStatus,
       "agentMLAGPortChannelConsistancy": agentMLAGPortChannelConsistancy,
       "agentMLAGPortChannelActiveVlans": agentMLAGPortChannelActiveVlans,
       "agentMLAGVlanRoutingPortTable": agentMLAGVlanRoutingPortTable,
       "agentMLAGVlanRoutingPortEntry": agentMLAGVlanRoutingPortEntry,
       "agentMLAGVlanRoutingPortifIndex": agentMLAGVlanRoutingPortifIndex,
       "agentMLAGVlanRoutingPortForbiddenMode": agentMLAGVlanRoutingPortForbiddenMode,
       "agentDCBXGroup": agentDCBXGroup,
       "agentDCBXConfigTable": agentDCBXConfigTable,
       "agentDCBXConfigEntry": agentDCBXConfigEntry,
       "agentDCBXifIndex": agentDCBXifIndex,
       "agentDCBXAdminMode": agentDCBXAdminMode,
       "agentDCBXVersion": agentDCBXVersion,
       "agentDCBXPFCConfigTable": agentDCBXPFCConfigTable,
       "agentDCBXPFCConfigEntry": agentDCBXPFCConfigEntry,
       "agentDCBXPFCEnableMode": agentDCBXPFCEnableMode,
       "agentDCBXPFCAdvertiseMode": agentDCBXPFCAdvertiseMode,
       "agentDCBXPFCWillingMode": agentDCBXPFCWillingMode,
       "agentDCBXPFCPriorityMask": agentDCBXPFCPriorityMask,
       "agentDCBXPFCMaxTrafficClass": agentDCBXPFCMaxTrafficClass,
       "agentDCBXPFCOperVersion": agentDCBXPFCOperVersion,
       "agentDCBXPFCOperMaxVersion": agentDCBXPFCOperMaxVersion,
       "agentDCBXPFCOperErrors": agentDCBXPFCOperErrors,
       "agentDCBXPFCOperMode": agentDCBXPFCOperMode,
       "agentDCBXPFCOperPeerSyncd": agentDCBXPFCOperPeerSyncd,
       "agentDCBXPFCOperPriorityMask": agentDCBXPFCOperPriorityMask,
       "agentDCBXPFCOperMaxTrafficClass": agentDCBXPFCOperMaxTrafficClass,
       "agentDCBXPFCPeerLocalifIndex": agentDCBXPFCPeerLocalifIndex,
       "agentDCBXPFCPeerStatus": agentDCBXPFCPeerStatus,
       "agentDCBXPFCPeerEnableMode": agentDCBXPFCPeerEnableMode,
       "agentDCBXPFCPeerWillingMode": agentDCBXPFCPeerWillingMode,
       "agentDCBXPFCPeerPriorityMask": agentDCBXPFCPeerPriorityMask,
       "agentDCBXPFCPeerMaxTrafficClass": agentDCBXPFCPeerMaxTrafficClass,
       "agentDCBXPFCDCBXOperVersion": agentDCBXPFCDCBXOperVersion,
       "agentDCBXPgConfigTable": agentDCBXPgConfigTable,
       "agentDCBXPgConfigEntry": agentDCBXPgConfigEntry,
       "agentDCBXPgEnableMode": agentDCBXPgEnableMode,
       "agentDCBXPgAdvertiseMode": agentDCBXPgAdvertiseMode,
       "agentDCBXPgWillingMode": agentDCBXPgWillingMode,
       "agentDCBXPgGroupBandwidth": agentDCBXPgGroupBandwidth,
       "agentDCBXPgPriorityGroupId": agentDCBXPgPriorityGroupId,
       "agentDCBXPgMaxTrafficClass": agentDCBXPgMaxTrafficClass,
       "agentDCBXPgOperVersion": agentDCBXPgOperVersion,
       "agentDCBXPgMaxVersion": agentDCBXPgMaxVersion,
       "agentDCBXPgErrorReason": agentDCBXPgErrorReason,
       "agentDCBXPgIsOperational": agentDCBXPgIsOperational,
       "agentDCBXPgSyncedMode": agentDCBXPgSyncedMode,
       "agentDCBXPgOperGroupBandwidth": agentDCBXPgOperGroupBandwidth,
       "agentDCBXPgOperPriorityGroupId": agentDCBXPgOperPriorityGroupId,
       "agentDCBXPgOperMaxTrafficClass": agentDCBXPgOperMaxTrafficClass,
       "agentDCBXPgPeerStatus": agentDCBXPgPeerStatus,
       "agentDCBXPgPeerEnableMode": agentDCBXPgPeerEnableMode,
       "agentDCBXPgPeerWillingMode": agentDCBXPgPeerWillingMode,
       "agentDCBXPgPeerGroupBandwidth": agentDCBXPgPeerGroupBandwidth,
       "agentDCBXPgPeerPriorityGroupId": agentDCBXPgPeerPriorityGroupId,
       "agentDCBXPgPeerMaxTrafficClass": agentDCBXPgPeerMaxTrafficClass,
       "agentDCBXPgDCBXOperVersion": agentDCBXPgDCBXOperVersion,
       "agentEvbGroup": agentEvbGroup,
       "agentEvbConfigTable": agentEvbConfigTable,
       "agentEvbConfigEntry": agentEvbConfigEntry,
       "agentEvbifIndex": agentEvbifIndex,
       "agentEvbAdminMode": agentEvbAdminMode,
       "agentEvbCapability": agentEvbCapability,
       "agentEvbForwardingMode": agentEvbForwardingMode,
       "agentEvbRetransmissionExp": agentEvbRetransmissionExp,
       "agentEvbOperCapability": agentEvbOperCapability,
       "agentEvbOperForwardingMode": agentEvbOperForwardingMode,
       "agentEvbOperRetransmissionExp": agentEvbOperRetransmissionExp,
       "agentEvbVsiGroup": agentEvbVsiGroup,
       "agentEvbVsiTable": agentEvbVsiTable,
       "agentEvbVsiEntry": agentEvbVsiEntry,
       "agentEvbVsiInstanceId": agentEvbVsiInstanceId,
       "agentEvbVsiMgrId": agentEvbVsiMgrId,
       "agentEvbVsiId": agentEvbVsiId,
       "agentEvbVsiVersion": agentEvbVsiVersion,
       "agentEvbVsiMode": agentEvbVsiMode,
       "agentEvbVsiState": agentEvbVsiState,
       "agentEvbVsiNumMacs": agentEvbVsiNumMacs,
       "agentEvbVsiMacTable": agentEvbVsiMacTable,
       "agentEvbVsiMacEntry": agentEvbVsiMacEntry,
       "agentEvbVsiMacAddress": agentEvbVsiMacAddress,
       "agentEvbVsiVlanId": agentEvbVsiVlanId,
       "agentVMTracerGroup": agentVMTracerGroup,
       "agentVMTracerIfCtlTable": agentVMTracerIfCtlTable,
       "agentVMTracerIfCtlEntry": agentVMTracerIfCtlEntry,
       "agentVMTracerIfIndex": agentVMTracerIfIndex,
       "agentVMTracerAdminMode": agentVMTracerAdminMode,
       "agentVMTracerSessionTable": agentVMTracerSessionTable,
       "agentVMTracerSessionEntry": agentVMTracerSessionEntry,
       "agentVMTracerSessionIndex": agentVMTracerSessionIndex,
       "agentVMTracerSessionName": agentVMTracerSessionName,
       "agentVMTracerSessionUrl": agentVMTracerSessionUrl,
       "agentVMTracerSessionUsername": agentVMTracerSessionUsername,
       "agentVMTracerSessionPassword": agentVMTracerSessionPassword,
       "agentVMTracerSessionAutoVlanMode": agentVMTracerSessionAutoVlanMode,
       "agentVMTracerSessionAllowVlan": agentVMTracerSessionAllowVlan,
       "agentVMTracerSessionConnectionStatus": agentVMTracerSessionConnectionStatus,
       "agentVMTracerSessionClear": agentVMTracerSessionClear,
       "agentVMTracerVMTable": agentVMTracerVMTable,
       "agentVMTracerVMEntry": agentVMTracerVMEntry,
       "agentVMTracerVMIndex": agentVMTracerVMIndex,
       "agentVMTracerVMName": agentVMTracerVMName,
       "agentVMTracerVMInterface": agentVMTracerVMInterface,
       "agentVMTracerVMAdapter": agentVMTracerVMAdapter,
       "agentVMTracerVMMacAddress": agentVMTracerVMMacAddress,
       "agentVMTracerVMPortGroup": agentVMTracerVMPortGroup,
       "agentVMTracerVMVlanId": agentVMTracerVMVlanId,
       "agentVMTracerVMSwitch": agentVMTracerVMSwitch,
       "agentVMTracerVMHost": agentVMTracerVMHost,
       "agentVMTracerVMHostCpuSpeed": agentVMTracerVMHostCpuSpeed,
       "agentVMTracerVMHostMemory": agentVMTracerVMHostMemory,
       "agentVMTracerVMHostSystem": agentVMTracerVMHostSystem,
       "agentVMTracerVMHostVendor": agentVMTracerVMHostVendor,
       "agentVMTracerVMHostCpuCores": agentVMTracerVMHostCpuCores,
       "agentVMTracerVMHostCpuPackages": agentVMTracerVMHostCpuPackages}
)
