# SNMP MIB module (JUNIPER-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:26 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(jnxExVlan,) = mibBuilder.importSymbols(
    "JUNIPER-EX-SMI",
    "jnxExVlan")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

jnxVlanMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1)
)
jnxVlanMIBObjects.setRevisions(
        ("2009-01-09 00:00",
         "2009-01-20 00:00",
         "2010-09-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxVlanTable_Object = MibTable
jnxVlanTable = _JnxVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    jnxVlanTable.setStatus("obsolete")
_JnxVlanEntry_Object = MibTableRow
jnxVlanEntry = _JnxVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 1, 1)
)
jnxVlanEntry.setIndexNames(
    (1, "JUNIPER-VLAN-MIB", "jnxVlanName"),
)
if mibBuilder.loadTexts:
    jnxVlanEntry.setStatus("obsolete")


class _JnxVlanName_Type(DisplayString):
    """Custom type jnxVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxVlanName_Type.__name__ = "DisplayString"
_JnxVlanName_Object = MibTableColumn
jnxVlanName = _JnxVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 1, 1, 1),
    _JnxVlanName_Type()
)
jnxVlanName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVlanName.setStatus("obsolete")


class _JnxVlanID_Type(Integer32):
    """Custom type jnxVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_JnxVlanID_Type.__name__ = "Integer32"
_JnxVlanID_Object = MibTableColumn
jnxVlanID = _JnxVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 1, 1, 2),
    _JnxVlanID_Type()
)
jnxVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanID.setStatus("obsolete")


class _JnxVlanType_Type(Integer32):
    """Custom type jnxVlanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_JnxVlanType_Type.__name__ = "Integer32"
_JnxVlanType_Object = MibTableColumn
jnxVlanType = _JnxVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 1, 1, 3),
    _JnxVlanType_Type()
)
jnxVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanType.setStatus("obsolete")
_JnxVlanPortGroupInstance_Type = Integer32
_JnxVlanPortGroupInstance_Object = MibTableColumn
jnxVlanPortGroupInstance = _JnxVlanPortGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 1, 1, 4),
    _JnxVlanPortGroupInstance_Type()
)
jnxVlanPortGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanPortGroupInstance.setStatus("obsolete")


class _JnxVlanMacListInstance_Type(Integer32):
    """Custom type jnxVlanMacListInstance based on Integer32"""
    defaultValue = 0


_JnxVlanMacListInstance_Object = MibTableColumn
jnxVlanMacListInstance = _JnxVlanMacListInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 1, 1, 5),
    _JnxVlanMacListInstance_Type()
)
jnxVlanMacListInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanMacListInstance.setStatus("obsolete")
_JnxVlanInterfaceTable_Object = MibTable
jnxVlanInterfaceTable = _JnxVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    jnxVlanInterfaceTable.setStatus("obsolete")
_JnxVlanInterfaceEntry_Object = MibTableRow
jnxVlanInterfaceEntry = _JnxVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1)
)
jnxVlanInterfaceEntry.setIndexNames(
    (1, "JUNIPER-VLAN-MIB", "jnxVlanName"),
)
if mibBuilder.loadTexts:
    jnxVlanInterfaceEntry.setStatus("obsolete")
_JnxVlanInterfaceIpAddress_Type = InetAddress
_JnxVlanInterfaceIpAddress_Object = MibTableColumn
jnxVlanInterfaceIpAddress = _JnxVlanInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 1),
    _JnxVlanInterfaceIpAddress_Type()
)
jnxVlanInterfaceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanInterfaceIpAddress.setStatus("obsolete")
_JnxVlanInterfaceProtocol_Type = InetAddressType
_JnxVlanInterfaceProtocol_Object = MibTableColumn
jnxVlanInterfaceProtocol = _JnxVlanInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 2),
    _JnxVlanInterfaceProtocol_Type()
)
jnxVlanInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanInterfaceProtocol.setStatus("obsolete")
_JnxVlanInterfaceSubNetMask_Type = IpAddress
_JnxVlanInterfaceSubNetMask_Object = MibTableColumn
jnxVlanInterfaceSubNetMask = _JnxVlanInterfaceSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 3),
    _JnxVlanInterfaceSubNetMask_Type()
)
jnxVlanInterfaceSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanInterfaceSubNetMask.setStatus("obsolete")
_JnxVlanInterfaceBroadcastAddress_Type = IpAddress
_JnxVlanInterfaceBroadcastAddress_Object = MibTableColumn
jnxVlanInterfaceBroadcastAddress = _JnxVlanInterfaceBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 4),
    _JnxVlanInterfaceBroadcastAddress_Type()
)
jnxVlanInterfaceBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanInterfaceBroadcastAddress.setStatus("obsolete")


class _JnxVlanInterfaceDescription_Type(DisplayString):
    """Custom type jnxVlanInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxVlanInterfaceDescription_Type.__name__ = "DisplayString"
_JnxVlanInterfaceDescription_Object = MibTableColumn
jnxVlanInterfaceDescription = _JnxVlanInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 5),
    _JnxVlanInterfaceDescription_Type()
)
jnxVlanInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanInterfaceDescription.setStatus("obsolete")
_JnxVlanInterfaceAdminStatus_Type = TruthValue
_JnxVlanInterfaceAdminStatus_Object = MibTableColumn
jnxVlanInterfaceAdminStatus = _JnxVlanInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 6),
    _JnxVlanInterfaceAdminStatus_Type()
)
jnxVlanInterfaceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanInterfaceAdminStatus.setStatus("obsolete")
_JnxVlanInterfaceOperStatus_Type = DisplayString
_JnxVlanInterfaceOperStatus_Object = MibTableColumn
jnxVlanInterfaceOperStatus = _JnxVlanInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 7),
    _JnxVlanInterfaceOperStatus_Type()
)
jnxVlanInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanInterfaceOperStatus.setStatus("obsolete")
_JnxVlanSnmpIfIndex_Type = InterfaceIndex
_JnxVlanSnmpIfIndex_Object = MibTableColumn
jnxVlanSnmpIfIndex = _JnxVlanSnmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 2, 1, 8),
    _JnxVlanSnmpIfIndex_Type()
)
jnxVlanSnmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanSnmpIfIndex.setStatus("obsolete")
_JnxVlanPortGroupTable_Object = MibTable
jnxVlanPortGroupTable = _JnxVlanPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    jnxVlanPortGroupTable.setStatus("obsolete")
_JnxVlanPortGroupEntry_Object = MibTableRow
jnxVlanPortGroupEntry = _JnxVlanPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 3, 1)
)
jnxVlanPortGroupEntry.setIndexNames(
    (0, "JUNIPER-VLAN-MIB", "jnxVlanPortGroupIndex"),
    (0, "JUNIPER-VLAN-MIB", "jnxVlanPort"),
)
if mibBuilder.loadTexts:
    jnxVlanPortGroupEntry.setStatus("obsolete")
_JnxVlanPortGroupIndex_Type = Integer32
_JnxVlanPortGroupIndex_Object = MibTableColumn
jnxVlanPortGroupIndex = _JnxVlanPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 3, 1, 1),
    _JnxVlanPortGroupIndex_Type()
)
jnxVlanPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVlanPortGroupIndex.setStatus("obsolete")
_JnxVlanPort_Type = Integer32
_JnxVlanPort_Object = MibTableColumn
jnxVlanPort = _JnxVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 3, 1, 2),
    _JnxVlanPort_Type()
)
jnxVlanPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVlanPort.setStatus("obsolete")


class _JnxVlanPortStatus_Type(Integer32):
    """Custom type jnxVlanPortStatus based on Integer32"""
    defaultValue = 2

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
        *(("allowed", 2),
          ("allowedActive", 3),
          ("allowedNotAvail", 4),
          ("autoActive", 1),
          ("notAssociated", 5))
    )


_JnxVlanPortStatus_Type.__name__ = "Integer32"
_JnxVlanPortStatus_Object = MibTableColumn
jnxVlanPortStatus = _JnxVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 3, 1, 3),
    _JnxVlanPortStatus_Type()
)
jnxVlanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanPortStatus.setStatus("obsolete")
_JnxVlanMacListTable_Object = MibTable
jnxVlanMacListTable = _JnxVlanMacListTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    jnxVlanMacListTable.setStatus("current")
_JnxVlanMacListEntry_Object = MibTableRow
jnxVlanMacListEntry = _JnxVlanMacListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 4, 1)
)
jnxVlanMacListEntry.setIndexNames(
    (0, "JUNIPER-VLAN-MIB", "jnxVlanMacListIndex"),
)
if mibBuilder.loadTexts:
    jnxVlanMacListEntry.setStatus("current")
_JnxVlanMacListIndex_Type = Integer32
_JnxVlanMacListIndex_Object = MibTableColumn
jnxVlanMacListIndex = _JnxVlanMacListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 4, 1, 1),
    _JnxVlanMacListIndex_Type()
)
jnxVlanMacListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxVlanMacListIndex.setStatus("current")
_JnxVlanMacAddress_Type = MacAddress
_JnxVlanMacAddress_Object = MibTableColumn
jnxVlanMacAddress = _JnxVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 4, 1, 2),
    _JnxVlanMacAddress_Type()
)
jnxVlanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVlanMacAddress.setStatus("current")
_JnxExVlanTable_Object = MibTable
jnxExVlanTable = _JnxExVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 5)
)
if mibBuilder.loadTexts:
    jnxExVlanTable.setStatus("current")
_JnxExVlanEntry_Object = MibTableRow
jnxExVlanEntry = _JnxExVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 5, 1)
)
jnxExVlanEntry.setIndexNames(
    (0, "JUNIPER-VLAN-MIB", "jnxExVlanID"),
)
if mibBuilder.loadTexts:
    jnxExVlanEntry.setStatus("current")


class _JnxExVlanID_Type(Integer32):
    """Custom type jnxExVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_JnxExVlanID_Type.__name__ = "Integer32"
_JnxExVlanID_Object = MibTableColumn
jnxExVlanID = _JnxExVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 5, 1, 1),
    _JnxExVlanID_Type()
)
jnxExVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxExVlanID.setStatus("current")


class _JnxExVlanName_Type(DisplayString):
    """Custom type jnxExVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxExVlanName_Type.__name__ = "DisplayString"
_JnxExVlanName_Object = MibTableColumn
jnxExVlanName = _JnxExVlanName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 5, 1, 2),
    _JnxExVlanName_Type()
)
jnxExVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanName.setStatus("current")


class _JnxExVlanType_Type(Integer32):
    """Custom type jnxExVlanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_JnxExVlanType_Type.__name__ = "Integer32"
_JnxExVlanType_Object = MibTableColumn
jnxExVlanType = _JnxExVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 5, 1, 3),
    _JnxExVlanType_Type()
)
jnxExVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanType.setStatus("current")
_JnxExVlanPortGroupInstance_Type = Integer32
_JnxExVlanPortGroupInstance_Object = MibTableColumn
jnxExVlanPortGroupInstance = _JnxExVlanPortGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 5, 1, 4),
    _JnxExVlanPortGroupInstance_Type()
)
jnxExVlanPortGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanPortGroupInstance.setStatus("current")
_JnxExVlanTag_Type = Unsigned32
_JnxExVlanTag_Object = MibTableColumn
jnxExVlanTag = _JnxExVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 5, 1, 5),
    _JnxExVlanTag_Type()
)
jnxExVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanTag.setStatus("current")
_JnxExVlanInterfaceTable_Object = MibTable
jnxExVlanInterfaceTable = _JnxExVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6)
)
if mibBuilder.loadTexts:
    jnxExVlanInterfaceTable.setStatus("current")
_JnxExVlanInterfaceEntry_Object = MibTableRow
jnxExVlanInterfaceEntry = _JnxExVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1)
)
jnxExVlanInterfaceEntry.setIndexNames(
    (0, "JUNIPER-VLAN-MIB", "jnxExVlanID"),
)
if mibBuilder.loadTexts:
    jnxExVlanInterfaceEntry.setStatus("current")
_JnxExVlanInterfaceProtocol_Type = InetAddressType
_JnxExVlanInterfaceProtocol_Object = MibTableColumn
jnxExVlanInterfaceProtocol = _JnxExVlanInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 1),
    _JnxExVlanInterfaceProtocol_Type()
)
jnxExVlanInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanInterfaceProtocol.setStatus("current")
_JnxExVlanInterfaceIpAddress_Type = InetAddress
_JnxExVlanInterfaceIpAddress_Object = MibTableColumn
jnxExVlanInterfaceIpAddress = _JnxExVlanInterfaceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 2),
    _JnxExVlanInterfaceIpAddress_Type()
)
jnxExVlanInterfaceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanInterfaceIpAddress.setStatus("current")
_JnxExVlanInterfacePrefixLength_Type = InetAddressPrefixLength
_JnxExVlanInterfacePrefixLength_Object = MibTableColumn
jnxExVlanInterfacePrefixLength = _JnxExVlanInterfacePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 3),
    _JnxExVlanInterfacePrefixLength_Type()
)
jnxExVlanInterfacePrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanInterfacePrefixLength.setStatus("current")
_JnxExVlanInterfaceBroadcastAddress_Type = InetAddress
_JnxExVlanInterfaceBroadcastAddress_Object = MibTableColumn
jnxExVlanInterfaceBroadcastAddress = _JnxExVlanInterfaceBroadcastAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 4),
    _JnxExVlanInterfaceBroadcastAddress_Type()
)
jnxExVlanInterfaceBroadcastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanInterfaceBroadcastAddress.setStatus("current")


class _JnxExVlanInterfaceDescription_Type(DisplayString):
    """Custom type jnxExVlanInterfaceDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxExVlanInterfaceDescription_Type.__name__ = "DisplayString"
_JnxExVlanInterfaceDescription_Object = MibTableColumn
jnxExVlanInterfaceDescription = _JnxExVlanInterfaceDescription_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 5),
    _JnxExVlanInterfaceDescription_Type()
)
jnxExVlanInterfaceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanInterfaceDescription.setStatus("current")


class _JnxExVlanInterfaceAdminStatus_Type(Integer32):
    """Custom type jnxExVlanInterfaceAdminStatus based on Integer32"""
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


_JnxExVlanInterfaceAdminStatus_Type.__name__ = "Integer32"
_JnxExVlanInterfaceAdminStatus_Object = MibTableColumn
jnxExVlanInterfaceAdminStatus = _JnxExVlanInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 6),
    _JnxExVlanInterfaceAdminStatus_Type()
)
jnxExVlanInterfaceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanInterfaceAdminStatus.setStatus("current")


class _JnxExVlanInterfaceOperStatus_Type(Integer32):
    """Custom type jnxExVlanInterfaceOperStatus based on Integer32"""
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


_JnxExVlanInterfaceOperStatus_Type.__name__ = "Integer32"
_JnxExVlanInterfaceOperStatus_Object = MibTableColumn
jnxExVlanInterfaceOperStatus = _JnxExVlanInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 7),
    _JnxExVlanInterfaceOperStatus_Type()
)
jnxExVlanInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanInterfaceOperStatus.setStatus("current")
_JnxExVlanSnmpIfIndex_Type = InterfaceIndex
_JnxExVlanSnmpIfIndex_Object = MibTableColumn
jnxExVlanSnmpIfIndex = _JnxExVlanSnmpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 6, 1, 8),
    _JnxExVlanSnmpIfIndex_Type()
)
jnxExVlanSnmpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanSnmpIfIndex.setStatus("current")
_JnxExVlanPortGroupTable_Object = MibTable
jnxExVlanPortGroupTable = _JnxExVlanPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 7)
)
if mibBuilder.loadTexts:
    jnxExVlanPortGroupTable.setStatus("current")
_JnxExVlanPortGroupEntry_Object = MibTableRow
jnxExVlanPortGroupEntry = _JnxExVlanPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 7, 1)
)
jnxExVlanPortGroupEntry.setIndexNames(
    (0, "JUNIPER-VLAN-MIB", "jnxExVlanPortGroupIndex"),
    (0, "JUNIPER-VLAN-MIB", "jnxExVlanPort"),
)
if mibBuilder.loadTexts:
    jnxExVlanPortGroupEntry.setStatus("current")


class _JnxExVlanPortGroupIndex_Type(Integer32):
    """Custom type jnxExVlanPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxExVlanPortGroupIndex_Type.__name__ = "Integer32"
_JnxExVlanPortGroupIndex_Object = MibTableColumn
jnxExVlanPortGroupIndex = _JnxExVlanPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 7, 1, 1),
    _JnxExVlanPortGroupIndex_Type()
)
jnxExVlanPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxExVlanPortGroupIndex.setStatus("current")


class _JnxExVlanPort_Type(Integer32):
    """Custom type jnxExVlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxExVlanPort_Type.__name__ = "Integer32"
_JnxExVlanPort_Object = MibTableColumn
jnxExVlanPort = _JnxExVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 7, 1, 2),
    _JnxExVlanPort_Type()
)
jnxExVlanPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxExVlanPort.setStatus("current")


class _JnxExVlanPortStatus_Type(Integer32):
    """Custom type jnxExVlanPortStatus based on Integer32"""
    defaultValue = 2

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
        *(("allowed", 2),
          ("allowedActive", 3),
          ("allowedNotAvail", 4),
          ("autoActive", 1),
          ("notAssociated", 5))
    )


_JnxExVlanPortStatus_Type.__name__ = "Integer32"
_JnxExVlanPortStatus_Object = MibTableColumn
jnxExVlanPortStatus = _JnxExVlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 7, 1, 3),
    _JnxExVlanPortStatus_Type()
)
jnxExVlanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanPortStatus.setStatus("current")


class _JnxExVlanPortTagness_Type(Integer32):
    """Custom type jnxExVlanPortTagness based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_JnxExVlanPortTagness_Type.__name__ = "Integer32"
_JnxExVlanPortTagness_Object = MibTableColumn
jnxExVlanPortTagness = _JnxExVlanPortTagness_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 7, 1, 4),
    _JnxExVlanPortTagness_Type()
)
jnxExVlanPortTagness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanPortTagness.setStatus("current")


class _JnxExVlanPortAccessMode_Type(Integer32):
    """Custom type jnxExVlanPortAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2))
    )


_JnxExVlanPortAccessMode_Type.__name__ = "Integer32"
_JnxExVlanPortAccessMode_Object = MibTableColumn
jnxExVlanPortAccessMode = _JnxExVlanPortAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 40, 1, 5, 1, 7, 1, 5),
    _JnxExVlanPortAccessMode_Type()
)
jnxExVlanPortAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxExVlanPortAccessMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-VLAN-MIB",
    **{"jnxVlanMIBObjects": jnxVlanMIBObjects,
       "jnxVlanTable": jnxVlanTable,
       "jnxVlanEntry": jnxVlanEntry,
       "jnxVlanName": jnxVlanName,
       "jnxVlanID": jnxVlanID,
       "jnxVlanType": jnxVlanType,
       "jnxVlanPortGroupInstance": jnxVlanPortGroupInstance,
       "jnxVlanMacListInstance": jnxVlanMacListInstance,
       "jnxVlanInterfaceTable": jnxVlanInterfaceTable,
       "jnxVlanInterfaceEntry": jnxVlanInterfaceEntry,
       "jnxVlanInterfaceIpAddress": jnxVlanInterfaceIpAddress,
       "jnxVlanInterfaceProtocol": jnxVlanInterfaceProtocol,
       "jnxVlanInterfaceSubNetMask": jnxVlanInterfaceSubNetMask,
       "jnxVlanInterfaceBroadcastAddress": jnxVlanInterfaceBroadcastAddress,
       "jnxVlanInterfaceDescription": jnxVlanInterfaceDescription,
       "jnxVlanInterfaceAdminStatus": jnxVlanInterfaceAdminStatus,
       "jnxVlanInterfaceOperStatus": jnxVlanInterfaceOperStatus,
       "jnxVlanSnmpIfIndex": jnxVlanSnmpIfIndex,
       "jnxVlanPortGroupTable": jnxVlanPortGroupTable,
       "jnxVlanPortGroupEntry": jnxVlanPortGroupEntry,
       "jnxVlanPortGroupIndex": jnxVlanPortGroupIndex,
       "jnxVlanPort": jnxVlanPort,
       "jnxVlanPortStatus": jnxVlanPortStatus,
       "jnxVlanMacListTable": jnxVlanMacListTable,
       "jnxVlanMacListEntry": jnxVlanMacListEntry,
       "jnxVlanMacListIndex": jnxVlanMacListIndex,
       "jnxVlanMacAddress": jnxVlanMacAddress,
       "jnxExVlanTable": jnxExVlanTable,
       "jnxExVlanEntry": jnxExVlanEntry,
       "jnxExVlanID": jnxExVlanID,
       "jnxExVlanName": jnxExVlanName,
       "jnxExVlanType": jnxExVlanType,
       "jnxExVlanPortGroupInstance": jnxExVlanPortGroupInstance,
       "jnxExVlanTag": jnxExVlanTag,
       "jnxExVlanInterfaceTable": jnxExVlanInterfaceTable,
       "jnxExVlanInterfaceEntry": jnxExVlanInterfaceEntry,
       "jnxExVlanInterfaceProtocol": jnxExVlanInterfaceProtocol,
       "jnxExVlanInterfaceIpAddress": jnxExVlanInterfaceIpAddress,
       "jnxExVlanInterfacePrefixLength": jnxExVlanInterfacePrefixLength,
       "jnxExVlanInterfaceBroadcastAddress": jnxExVlanInterfaceBroadcastAddress,
       "jnxExVlanInterfaceDescription": jnxExVlanInterfaceDescription,
       "jnxExVlanInterfaceAdminStatus": jnxExVlanInterfaceAdminStatus,
       "jnxExVlanInterfaceOperStatus": jnxExVlanInterfaceOperStatus,
       "jnxExVlanSnmpIfIndex": jnxExVlanSnmpIfIndex,
       "jnxExVlanPortGroupTable": jnxExVlanPortGroupTable,
       "jnxExVlanPortGroupEntry": jnxExVlanPortGroupEntry,
       "jnxExVlanPortGroupIndex": jnxExVlanPortGroupIndex,
       "jnxExVlanPort": jnxExVlanPort,
       "jnxExVlanPortStatus": jnxExVlanPortStatus,
       "jnxExVlanPortTagness": jnxExVlanPortTagness,
       "jnxExVlanPortAccessMode": jnxExVlanPortAccessMode}
)
