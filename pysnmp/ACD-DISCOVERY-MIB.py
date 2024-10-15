# SNMP MIB module (ACD-DISCOVERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACD-DISCOVERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:19 2024
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

(acdMibs,) = mibBuilder.importSymbols(
    "ACCEDIAN-SMI",
    "acdMibs")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

acdDiscovery = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11)
)
acdDiscovery.setRevisions(
        ("2012-10-11 01:00",
         "2011-11-01 01:00",
         "2008-10-01 01:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcdDiscoveryNotifications_ObjectIdentity = ObjectIdentity
acdDiscoveryNotifications = _AcdDiscoveryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 0)
)
_AcdDiscoveryMIBObjects_ObjectIdentity = ObjectIdentity
acdDiscoveryMIBObjects = _AcdDiscoveryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1)
)
_AcdDiscoveryInventory_ObjectIdentity = ObjectIdentity
acdDiscoveryInventory = _AcdDiscoveryInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1)
)
_AcdDiscoveryInventoryTable_Object = MibTable
acdDiscoveryInventoryTable = _AcdDiscoveryInventoryTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acdDiscoveryInventoryTable.setStatus("current")
_AcdDiscoveryInventoryEntry_Object = MibTableRow
acdDiscoveryInventoryEntry = _AcdDiscoveryInventoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1)
)
acdDiscoveryInventoryEntry.setIndexNames(
    (0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"),
)
if mibBuilder.loadTexts:
    acdDiscoveryInventoryEntry.setStatus("current")


class _AcdDiscoveryIndex_Type(Unsigned32):
    """Custom type acdDiscoveryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AcdDiscoveryIndex_Type.__name__ = "Unsigned32"
_AcdDiscoveryIndex_Object = MibTableColumn
acdDiscoveryIndex = _AcdDiscoveryIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 1),
    _AcdDiscoveryIndex_Type()
)
acdDiscoveryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdDiscoveryIndex.setStatus("current")
_AcdDiscoveryMgmtIpAddress_Type = IpAddress
_AcdDiscoveryMgmtIpAddress_Object = MibTableColumn
acdDiscoveryMgmtIpAddress = _AcdDiscoveryMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 2),
    _AcdDiscoveryMgmtIpAddress_Type()
)
acdDiscoveryMgmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryMgmtIpAddress.setStatus("current")


class _AcdDiscoverySystemName_Type(DisplayString):
    """Custom type acdDiscoverySystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoverySystemName_Type.__name__ = "DisplayString"
_AcdDiscoverySystemName_Object = MibTableColumn
acdDiscoverySystemName = _AcdDiscoverySystemName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 3),
    _AcdDiscoverySystemName_Type()
)
acdDiscoverySystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoverySystemName.setStatus("current")


class _AcdDiscoverySystemDesc_Type(DisplayString):
    """Custom type acdDiscoverySystemDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoverySystemDesc_Type.__name__ = "DisplayString"
_AcdDiscoverySystemDesc_Object = MibTableColumn
acdDiscoverySystemDesc = _AcdDiscoverySystemDesc_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 4),
    _AcdDiscoverySystemDesc_Type()
)
acdDiscoverySystemDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoverySystemDesc.setStatus("current")


class _AcdDiscoverySerialNumber_Type(DisplayString):
    """Custom type acdDiscoverySerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoverySerialNumber_Type.__name__ = "DisplayString"
_AcdDiscoverySerialNumber_Object = MibTableColumn
acdDiscoverySerialNumber = _AcdDiscoverySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 5),
    _AcdDiscoverySerialNumber_Type()
)
acdDiscoverySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoverySerialNumber.setStatus("current")
_AcdDiscoveryLastChange_Type = DateAndTime
_AcdDiscoveryLastChange_Object = MibTableColumn
acdDiscoveryLastChange = _AcdDiscoveryLastChange_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 6),
    _AcdDiscoveryLastChange_Type()
)
acdDiscoveryLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryLastChange.setStatus("current")


class _AcdDiscoveryDomain_Type(DisplayString):
    """Custom type acdDiscoveryDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_AcdDiscoveryDomain_Type.__name__ = "DisplayString"
_AcdDiscoveryDomain_Object = MibTableColumn
acdDiscoveryDomain = _AcdDiscoveryDomain_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 7),
    _AcdDiscoveryDomain_Type()
)
acdDiscoveryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryDomain.setStatus("current")


class _AcdDiscoveryFirmware_Type(DisplayString):
    """Custom type acdDiscoveryFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoveryFirmware_Type.__name__ = "DisplayString"
_AcdDiscoveryFirmware_Object = MibTableColumn
acdDiscoveryFirmware = _AcdDiscoveryFirmware_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 8),
    _AcdDiscoveryFirmware_Type()
)
acdDiscoveryFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryFirmware.setStatus("current")
_AcdDiscoveryBaseMacAddress_Type = MacAddress
_AcdDiscoveryBaseMacAddress_Object = MibTableColumn
acdDiscoveryBaseMacAddress = _AcdDiscoveryBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 9),
    _AcdDiscoveryBaseMacAddress_Type()
)
acdDiscoveryBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryBaseMacAddress.setStatus("current")
_AcdDiscoveryInterfaceMacAddress_Type = MacAddress
_AcdDiscoveryInterfaceMacAddress_Object = MibTableColumn
acdDiscoveryInterfaceMacAddress = _AcdDiscoveryInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 10),
    _AcdDiscoveryInterfaceMacAddress_Type()
)
acdDiscoveryInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryInterfaceMacAddress.setStatus("current")


class _AcdDiscoveryChassisIdSubtype_Type(Unsigned32):
    """Custom type acdDiscoveryChassisIdSubtype based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdDiscoveryChassisIdSubtype_Type.__name__ = "Unsigned32"
_AcdDiscoveryChassisIdSubtype_Object = MibTableColumn
acdDiscoveryChassisIdSubtype = _AcdDiscoveryChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 11),
    _AcdDiscoveryChassisIdSubtype_Type()
)
acdDiscoveryChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryChassisIdSubtype.setStatus("current")


class _AcdDiscoveryChassisId_Type(DisplayString):
    """Custom type acdDiscoveryChassisId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoveryChassisId_Type.__name__ = "DisplayString"
_AcdDiscoveryChassisId_Object = MibTableColumn
acdDiscoveryChassisId = _AcdDiscoveryChassisId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 12),
    _AcdDiscoveryChassisId_Type()
)
acdDiscoveryChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryChassisId.setStatus("current")


class _AcdDiscoveryLocalPortId_Type(DisplayString):
    """Custom type acdDiscoveryLocalPortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoveryLocalPortId_Type.__name__ = "DisplayString"
_AcdDiscoveryLocalPortId_Object = MibTableColumn
acdDiscoveryLocalPortId = _AcdDiscoveryLocalPortId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 13),
    _AcdDiscoveryLocalPortId_Type()
)
acdDiscoveryLocalPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryLocalPortId.setStatus("current")


class _AcdDiscoveryRemotePortId_Type(DisplayString):
    """Custom type acdDiscoveryRemotePortId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoveryRemotePortId_Type.__name__ = "DisplayString"
_AcdDiscoveryRemotePortId_Object = MibTableColumn
acdDiscoveryRemotePortId = _AcdDiscoveryRemotePortId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 14),
    _AcdDiscoveryRemotePortId_Type()
)
acdDiscoveryRemotePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryRemotePortId.setStatus("current")


class _AcdDiscoveryWebServerPort_Type(Unsigned32):
    """Custom type acdDiscoveryWebServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdDiscoveryWebServerPort_Type.__name__ = "Unsigned32"
_AcdDiscoveryWebServerPort_Object = MibTableColumn
acdDiscoveryWebServerPort = _AcdDiscoveryWebServerPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 15),
    _AcdDiscoveryWebServerPort_Type()
)
acdDiscoveryWebServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryWebServerPort.setStatus("current")


class _AcdDiscoverySnmpAgentPort_Type(Unsigned32):
    """Custom type acdDiscoverySnmpAgentPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdDiscoverySnmpAgentPort_Type.__name__ = "Unsigned32"
_AcdDiscoverySnmpAgentPort_Object = MibTableColumn
acdDiscoverySnmpAgentPort = _AcdDiscoverySnmpAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 16),
    _AcdDiscoverySnmpAgentPort_Type()
)
acdDiscoverySnmpAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoverySnmpAgentPort.setStatus("current")


class _AcdDiscoverySshPort_Type(Unsigned32):
    """Custom type acdDiscoverySshPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdDiscoverySshPort_Type.__name__ = "Unsigned32"
_AcdDiscoverySshPort_Object = MibTableColumn
acdDiscoverySshPort = _AcdDiscoverySshPort_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 17),
    _AcdDiscoverySshPort_Type()
)
acdDiscoverySshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoverySshPort.setStatus("current")


class _AcdDiscoveryVlan1_Type(Unsigned32):
    """Custom type acdDiscoveryVlan1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdDiscoveryVlan1_Type.__name__ = "Unsigned32"
_AcdDiscoveryVlan1_Object = MibTableColumn
acdDiscoveryVlan1 = _AcdDiscoveryVlan1_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 18),
    _AcdDiscoveryVlan1_Type()
)
acdDiscoveryVlan1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryVlan1.setStatus("current")


class _AcdDiscoveryVlan2_Type(Unsigned32):
    """Custom type acdDiscoveryVlan2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdDiscoveryVlan2_Type.__name__ = "Unsigned32"
_AcdDiscoveryVlan2_Object = MibTableColumn
acdDiscoveryVlan2 = _AcdDiscoveryVlan2_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 19),
    _AcdDiscoveryVlan2_Type()
)
acdDiscoveryVlan2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryVlan2.setStatus("current")
_AcdDiscoveryIpListTable_Object = MibTable
acdDiscoveryIpListTable = _AcdDiscoveryIpListTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acdDiscoveryIpListTable.setStatus("current")
_AcdDiscoveryIpListEntry_Object = MibTableRow
acdDiscoveryIpListEntry = _AcdDiscoveryIpListEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1)
)
acdDiscoveryIpListEntry.setIndexNames(
    (0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"),
    (0, "ACD-DISCOVERY-MIB", "acdDiscoveryIpListIndex"),
)
if mibBuilder.loadTexts:
    acdDiscoveryIpListEntry.setStatus("current")


class _AcdDiscoveryIpListIndex_Type(Unsigned32):
    """Custom type acdDiscoveryIpListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdDiscoveryIpListIndex_Type.__name__ = "Unsigned32"
_AcdDiscoveryIpListIndex_Object = MibTableColumn
acdDiscoveryIpListIndex = _AcdDiscoveryIpListIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1, 1),
    _AcdDiscoveryIpListIndex_Type()
)
acdDiscoveryIpListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdDiscoveryIpListIndex.setStatus("current")
_AcdDiscoveryIpListAddress_Type = IpAddress
_AcdDiscoveryIpListAddress_Object = MibTableColumn
acdDiscoveryIpListAddress = _AcdDiscoveryIpListAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1, 2),
    _AcdDiscoveryIpListAddress_Type()
)
acdDiscoveryIpListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryIpListAddress.setStatus("current")
_AcdDiscoveryMacAddressListTable_Object = MibTable
acdDiscoveryMacAddressListTable = _AcdDiscoveryMacAddressListTable_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListTable.setStatus("current")
_AcdDiscoveryMacAddressListEntry_Object = MibTableRow
acdDiscoveryMacAddressListEntry = _AcdDiscoveryMacAddressListEntry_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1)
)
acdDiscoveryMacAddressListEntry.setIndexNames(
    (0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"),
    (0, "ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListIndex"),
)
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListEntry.setStatus("current")


class _AcdDiscoveryMacAddressListIndex_Type(Unsigned32):
    """Custom type acdDiscoveryMacAddressListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdDiscoveryMacAddressListIndex_Type.__name__ = "Unsigned32"
_AcdDiscoveryMacAddressListIndex_Object = MibTableColumn
acdDiscoveryMacAddressListIndex = _AcdDiscoveryMacAddressListIndex_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 1),
    _AcdDiscoveryMacAddressListIndex_Type()
)
acdDiscoveryMacAddressListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListIndex.setStatus("current")


class _AcdDiscoveryMacAddressListSystemSlotId_Type(Unsigned32):
    """Custom type acdDiscoveryMacAddressListSystemSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcdDiscoveryMacAddressListSystemSlotId_Type.__name__ = "Unsigned32"
_AcdDiscoveryMacAddressListSystemSlotId_Object = MibTableColumn
acdDiscoveryMacAddressListSystemSlotId = _AcdDiscoveryMacAddressListSystemSlotId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 2),
    _AcdDiscoveryMacAddressListSystemSlotId_Type()
)
acdDiscoveryMacAddressListSystemSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListSystemSlotId.setStatus("current")


class _AcdDiscoveryMacAddressListPortId_Type(Unsigned32):
    """Custom type acdDiscoveryMacAddressListPortId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcdDiscoveryMacAddressListPortId_Type.__name__ = "Unsigned32"
_AcdDiscoveryMacAddressListPortId_Object = MibTableColumn
acdDiscoveryMacAddressListPortId = _AcdDiscoveryMacAddressListPortId_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 3),
    _AcdDiscoveryMacAddressListPortId_Type()
)
acdDiscoveryMacAddressListPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListPortId.setStatus("current")


class _AcdDiscoveryMacAddressListPortName_Type(DisplayString):
    """Custom type acdDiscoveryMacAddressListPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AcdDiscoveryMacAddressListPortName_Type.__name__ = "DisplayString"
_AcdDiscoveryMacAddressListPortName_Object = MibTableColumn
acdDiscoveryMacAddressListPortName = _AcdDiscoveryMacAddressListPortName_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 4),
    _AcdDiscoveryMacAddressListPortName_Type()
)
acdDiscoveryMacAddressListPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListPortName.setStatus("current")
_AcdDiscoveryMacAddressListPortMacAddress_Type = MacAddress
_AcdDiscoveryMacAddressListPortMacAddress_Object = MibTableColumn
acdDiscoveryMacAddressListPortMacAddress = _AcdDiscoveryMacAddressListPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 5),
    _AcdDiscoveryMacAddressListPortMacAddress_Type()
)
acdDiscoveryMacAddressListPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListPortMacAddress.setStatus("current")


class _AcdDiscoveryInventoryInserts_Type(Unsigned32):
    """Custom type acdDiscoveryInventoryInserts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcdDiscoveryInventoryInserts_Type.__name__ = "Unsigned32"
_AcdDiscoveryInventoryInserts_Object = MibScalar
acdDiscoveryInventoryInserts = _AcdDiscoveryInventoryInserts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 4),
    _AcdDiscoveryInventoryInserts_Type()
)
acdDiscoveryInventoryInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryInventoryInserts.setStatus("current")
if mibBuilder.loadTexts:
    acdDiscoveryInventoryInserts.setUnits("table entries")


class _AcdDiscoveryInventoryAgeouts_Type(Unsigned32):
    """Custom type acdDiscoveryInventoryAgeouts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcdDiscoveryInventoryAgeouts_Type.__name__ = "Unsigned32"
_AcdDiscoveryInventoryAgeouts_Object = MibScalar
acdDiscoveryInventoryAgeouts = _AcdDiscoveryInventoryAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 5),
    _AcdDiscoveryInventoryAgeouts_Type()
)
acdDiscoveryInventoryAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdDiscoveryInventoryAgeouts.setStatus("current")
if mibBuilder.loadTexts:
    acdDiscoveryInventoryAgeouts.setUnits("table entries")
_AcdDiscoveryConformance_ObjectIdentity = ObjectIdentity
acdDiscoveryConformance = _AcdDiscoveryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2)
)
_AcdDiscoveryCompliances_ObjectIdentity = ObjectIdentity
acdDiscoveryCompliances = _AcdDiscoveryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 1)
)
_AcdDiscoveryGroups_ObjectIdentity = ObjectIdentity
acdDiscoveryGroups = _AcdDiscoveryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2)
)

# Managed Objects groups

acdDiscoveryInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 1)
)
acdDiscoveryInventoryGroup.setObjects(
      *(("ACD-DISCOVERY-MIB", "acdDiscoveryMgmtIpAddress"),
        ("ACD-DISCOVERY-MIB", "acdDiscoverySystemName"),
        ("ACD-DISCOVERY-MIB", "acdDiscoverySystemDesc"),
        ("ACD-DISCOVERY-MIB", "acdDiscoverySerialNumber"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryLastChange"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryDomain"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryFirmware"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryBaseMacAddress"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryInterfaceMacAddress"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryChassisIdSubtype"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryChassisId"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryLocalPortId"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryRemotePortId"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryWebServerPort"),
        ("ACD-DISCOVERY-MIB", "acdDiscoverySnmpAgentPort"),
        ("ACD-DISCOVERY-MIB", "acdDiscoverySshPort"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryVlan1"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryVlan2"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryInventoryInserts"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryInventoryAgeouts"))
)
if mibBuilder.loadTexts:
    acdDiscoveryInventoryGroup.setStatus("current")

acdDiscoveryIpListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 2)
)
acdDiscoveryIpListGroup.setObjects(
    ("ACD-DISCOVERY-MIB", "acdDiscoveryIpListAddress")
)
if mibBuilder.loadTexts:
    acdDiscoveryIpListGroup.setStatus("current")

acdDiscoveryMacAddressListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 3)
)
acdDiscoveryMacAddressListGroup.setObjects(
      *(("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListSystemSlotId"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortId"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortName"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortMacAddress"))
)
if mibBuilder.loadTexts:
    acdDiscoveryMacAddressListGroup.setStatus("current")


# Notification objects

acdDiscoveryInventoryChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 0, 1)
)
acdDiscoveryInventoryChange.setObjects(
      *(("ACD-DISCOVERY-MIB", "acdDiscoveryInventoryInserts"),
        ("ACD-DISCOVERY-MIB", "acdDiscoveryInventoryAgeouts"))
)
if mibBuilder.loadTexts:
    acdDiscoveryInventoryChange.setStatus(
        "current"
    )


# Notifications groups

acdDiscoveryNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 4)
)
acdDiscoveryNotificationsGroup.setObjects(
    ("ACD-DISCOVERY-MIB", "acdDiscoveryInventoryChange")
)
if mibBuilder.loadTexts:
    acdDiscoveryNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

acdDiscoveryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 1, 1)
)
if mibBuilder.loadTexts:
    acdDiscoveryCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACD-DISCOVERY-MIB",
    **{"acdDiscovery": acdDiscovery,
       "acdDiscoveryNotifications": acdDiscoveryNotifications,
       "acdDiscoveryInventoryChange": acdDiscoveryInventoryChange,
       "acdDiscoveryMIBObjects": acdDiscoveryMIBObjects,
       "acdDiscoveryInventory": acdDiscoveryInventory,
       "acdDiscoveryInventoryTable": acdDiscoveryInventoryTable,
       "acdDiscoveryInventoryEntry": acdDiscoveryInventoryEntry,
       "acdDiscoveryIndex": acdDiscoveryIndex,
       "acdDiscoveryMgmtIpAddress": acdDiscoveryMgmtIpAddress,
       "acdDiscoverySystemName": acdDiscoverySystemName,
       "acdDiscoverySystemDesc": acdDiscoverySystemDesc,
       "acdDiscoverySerialNumber": acdDiscoverySerialNumber,
       "acdDiscoveryLastChange": acdDiscoveryLastChange,
       "acdDiscoveryDomain": acdDiscoveryDomain,
       "acdDiscoveryFirmware": acdDiscoveryFirmware,
       "acdDiscoveryBaseMacAddress": acdDiscoveryBaseMacAddress,
       "acdDiscoveryInterfaceMacAddress": acdDiscoveryInterfaceMacAddress,
       "acdDiscoveryChassisIdSubtype": acdDiscoveryChassisIdSubtype,
       "acdDiscoveryChassisId": acdDiscoveryChassisId,
       "acdDiscoveryLocalPortId": acdDiscoveryLocalPortId,
       "acdDiscoveryRemotePortId": acdDiscoveryRemotePortId,
       "acdDiscoveryWebServerPort": acdDiscoveryWebServerPort,
       "acdDiscoverySnmpAgentPort": acdDiscoverySnmpAgentPort,
       "acdDiscoverySshPort": acdDiscoverySshPort,
       "acdDiscoveryVlan1": acdDiscoveryVlan1,
       "acdDiscoveryVlan2": acdDiscoveryVlan2,
       "acdDiscoveryIpListTable": acdDiscoveryIpListTable,
       "acdDiscoveryIpListEntry": acdDiscoveryIpListEntry,
       "acdDiscoveryIpListIndex": acdDiscoveryIpListIndex,
       "acdDiscoveryIpListAddress": acdDiscoveryIpListAddress,
       "acdDiscoveryMacAddressListTable": acdDiscoveryMacAddressListTable,
       "acdDiscoveryMacAddressListEntry": acdDiscoveryMacAddressListEntry,
       "acdDiscoveryMacAddressListIndex": acdDiscoveryMacAddressListIndex,
       "acdDiscoveryMacAddressListSystemSlotId": acdDiscoveryMacAddressListSystemSlotId,
       "acdDiscoveryMacAddressListPortId": acdDiscoveryMacAddressListPortId,
       "acdDiscoveryMacAddressListPortName": acdDiscoveryMacAddressListPortName,
       "acdDiscoveryMacAddressListPortMacAddress": acdDiscoveryMacAddressListPortMacAddress,
       "acdDiscoveryInventoryInserts": acdDiscoveryInventoryInserts,
       "acdDiscoveryInventoryAgeouts": acdDiscoveryInventoryAgeouts,
       "acdDiscoveryConformance": acdDiscoveryConformance,
       "acdDiscoveryCompliances": acdDiscoveryCompliances,
       "acdDiscoveryCompliance": acdDiscoveryCompliance,
       "acdDiscoveryGroups": acdDiscoveryGroups,
       "acdDiscoveryInventoryGroup": acdDiscoveryInventoryGroup,
       "acdDiscoveryIpListGroup": acdDiscoveryIpListGroup,
       "acdDiscoveryMacAddressListGroup": acdDiscoveryMacAddressListGroup,
       "acdDiscoveryNotificationsGroup": acdDiscoveryNotificationsGroup}
)
