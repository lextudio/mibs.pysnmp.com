# SNMP MIB module (VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:46 2024
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

(preDot1qVlanMIB,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "preDot1qVlanMIB")

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
 RowStatus,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY

vlanMIBObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VlanConfGroup_ObjectIdentity = ObjectIdentity
vlanConfGroup = _VlanConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1)
)
_VlanConfTable_Object = MibTable
vlanConfTable = _VlanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vlanConfTable.setStatus("current")
_VlanConfEntry_Object = MibTableRow
vlanConfEntry = _VlanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1)
)
vlanConfEntry.setIndexNames(
    (0, "VLAN-MIB", "vlanName"),
)
if mibBuilder.loadTexts:
    vlanConfEntry.setStatus("current")


class _VlanName_Type(DisplayString):
    """Custom type vlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_VlanName_Type.__name__ = "DisplayString"
_VlanName_Object = MibTableColumn
vlanName = _VlanName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 1),
    _VlanName_Type()
)
vlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanName.setStatus("current")
_VlanID_Type = Integer32
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 2),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")
_VlanConfRowStatus_Type = RowStatus
_VlanConfRowStatus_Object = MibTableColumn
vlanConfRowStatus = _VlanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 3),
    _VlanConfRowStatus_Type()
)
vlanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanConfRowStatus.setStatus("current")
_VlanCreatedBy_Type = DisplayString
_VlanCreatedBy_Object = MibTableColumn
vlanCreatedBy = _VlanCreatedBy_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 4),
    _VlanCreatedBy_Type()
)
vlanCreatedBy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanCreatedBy.setStatus("current")


class _VlanType_Type(Integer32):
    """Custom type vlanType based on Integer32"""
    defaultValue = 1


_VlanType_Object = MibTableColumn
vlanType = _VlanType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 5),
    _VlanType_Type()
)
vlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanType.setStatus("current")
_VlanPortGroupInstance_Type = Integer32
_VlanPortGroupInstance_Object = MibTableColumn
vlanPortGroupInstance = _VlanPortGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 6),
    _VlanPortGroupInstance_Type()
)
vlanPortGroupInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortGroupInstance.setStatus("current")


class _VlanMacListInstance_Type(Integer32):
    """Custom type vlanMacListInstance based on Integer32"""
    defaultValue = 0


_VlanMacListInstance_Object = MibTableColumn
vlanMacListInstance = _VlanMacListInstance_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 7),
    _VlanMacListInstance_Type()
)
vlanMacListInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMacListInstance.setStatus("current")


class _VlanProtocolType_Type(Integer32):
    """Custom type vlanProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernetv2", 2),
          ("ieee802dot3", 3),
          ("none", 1))
    )


_VlanProtocolType_Type.__name__ = "Integer32"
_VlanProtocolType_Object = MibTableColumn
vlanProtocolType = _VlanProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 8),
    _VlanProtocolType_Type()
)
vlanProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanProtocolType.setStatus("current")


class _VlanProtocolSubtype_Type(OctetString):
    """Custom type vlanProtocolSubtype based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_VlanProtocolSubtype_Type.__name__ = "OctetString"
_VlanProtocolSubtype_Object = MibTableColumn
vlanProtocolSubtype = _VlanProtocolSubtype_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 9),
    _VlanProtocolSubtype_Type()
)
vlanProtocolSubtype.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanProtocolSubtype.setStatus("current")


class _VlanIPSubnetAddress_Type(IpAddress):
    """Custom type vlanIPSubnetAddress based on IpAddress"""
    defaultValue = 0


_VlanIPSubnetAddress_Object = MibTableColumn
vlanIPSubnetAddress = _VlanIPSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 10),
    _VlanIPSubnetAddress_Type()
)
vlanIPSubnetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanIPSubnetAddress.setStatus("current")


class _VlanBridgeName_Type(DisplayString):
    """Custom type vlanBridgeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VlanBridgeName_Type.__name__ = "DisplayString"
_VlanBridgeName_Object = MibTableColumn
vlanBridgeName = _VlanBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 11),
    _VlanBridgeName_Type()
)
vlanBridgeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanBridgeName.setStatus("current")


class _VlanIPMulticastFilter_Type(Integer32):
    """Custom type vlanIPMulticastFilter based on Integer32"""
    defaultValue = 2

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


_VlanIPMulticastFilter_Type.__name__ = "Integer32"
_VlanIPMulticastFilter_Object = MibTableColumn
vlanIPMulticastFilter = _VlanIPMulticastFilter_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 1, 1, 12),
    _VlanIPMulticastFilter_Type()
)
vlanIPMulticastFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanIPMulticastFilter.setStatus("current")
_VlanPortGroupTable_Object = MibTable
vlanPortGroupTable = _VlanPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vlanPortGroupTable.setStatus("current")
_VlanPortGroupEntry_Object = MibTableRow
vlanPortGroupEntry = _VlanPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1)
)
vlanPortGroupEntry.setIndexNames(
    (0, "VLAN-MIB", "vlanPortGroupIndex"),
    (0, "VLAN-MIB", "vlanPort"),
)
if mibBuilder.loadTexts:
    vlanPortGroupEntry.setStatus("current")
_VlanPortGroupIndex_Type = Integer32
_VlanPortGroupIndex_Object = MibTableColumn
vlanPortGroupIndex = _VlanPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 1),
    _VlanPortGroupIndex_Type()
)
vlanPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPortGroupIndex.setStatus("current")
_VlanPort_Type = Integer32
_VlanPort_Object = MibTableColumn
vlanPort = _VlanPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 2),
    _VlanPort_Type()
)
vlanPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPort.setStatus("current")
_VlanPortGroupRowStatus_Type = RowStatus
_VlanPortGroupRowStatus_Object = MibTableColumn
vlanPortGroupRowStatus = _VlanPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 3),
    _VlanPortGroupRowStatus_Type()
)
vlanPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortGroupRowStatus.setStatus("current")


class _VlanPortStatus_Type(Integer32):
    """Custom type vlanPortStatus based on Integer32"""
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


_VlanPortStatus_Type.__name__ = "Integer32"
_VlanPortStatus_Object = MibTableColumn
vlanPortStatus = _VlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 2, 1, 4),
    _VlanPortStatus_Type()
)
vlanPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortStatus.setStatus("current")
_VlanPortGroupNextIndex_Type = TestAndIncr
_VlanPortGroupNextIndex_Object = MibScalar
vlanPortGroupNextIndex = _VlanPortGroupNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 3),
    _VlanPortGroupNextIndex_Type()
)
vlanPortGroupNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortGroupNextIndex.setStatus("current")
_VlanMacListTable_Object = MibTable
vlanMacListTable = _VlanMacListTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vlanMacListTable.setStatus("current")
_VlanMacListEntry_Object = MibTableRow
vlanMacListEntry = _VlanMacListEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1)
)
vlanMacListEntry.setIndexNames(
    (0, "VLAN-MIB", "vlanMacListIndex"),
    (0, "VLAN-MIB", "vlanMacAddress"),
)
if mibBuilder.loadTexts:
    vlanMacListEntry.setStatus("current")
_VlanMacListIndex_Type = Integer32
_VlanMacListIndex_Object = MibTableColumn
vlanMacListIndex = _VlanMacListIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 1),
    _VlanMacListIndex_Type()
)
vlanMacListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacListIndex.setStatus("current")
_VlanMacAddress_Type = MacAddress
_VlanMacAddress_Object = MibTableColumn
vlanMacAddress = _VlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 2),
    _VlanMacAddress_Type()
)
vlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMacAddress.setStatus("current")
_VlanMacListRowStatus_Type = RowStatus
_VlanMacListRowStatus_Object = MibTableColumn
vlanMacListRowStatus = _VlanMacListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 1, 3),
    _VlanMacListRowStatus_Type()
)
vlanMacListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMacListRowStatus.setStatus("current")
_VlanMacListNextIndex_Type = TestAndIncr
_VlanMacListNextIndex_Object = MibScalar
vlanMacListNextIndex = _VlanMacListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 1, 1, 4, 2),
    _VlanMacListNextIndex_Type()
)
vlanMacListNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanMacListNextIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VLAN-MIB",
    **{"vlanMIBObjects": vlanMIBObjects,
       "vlanConfGroup": vlanConfGroup,
       "vlanConfTable": vlanConfTable,
       "vlanConfEntry": vlanConfEntry,
       "vlanName": vlanName,
       "vlanID": vlanID,
       "vlanConfRowStatus": vlanConfRowStatus,
       "vlanCreatedBy": vlanCreatedBy,
       "vlanType": vlanType,
       "vlanPortGroupInstance": vlanPortGroupInstance,
       "vlanMacListInstance": vlanMacListInstance,
       "vlanProtocolType": vlanProtocolType,
       "vlanProtocolSubtype": vlanProtocolSubtype,
       "vlanIPSubnetAddress": vlanIPSubnetAddress,
       "vlanBridgeName": vlanBridgeName,
       "vlanIPMulticastFilter": vlanIPMulticastFilter,
       "vlanPortGroupTable": vlanPortGroupTable,
       "vlanPortGroupEntry": vlanPortGroupEntry,
       "vlanPortGroupIndex": vlanPortGroupIndex,
       "vlanPort": vlanPort,
       "vlanPortGroupRowStatus": vlanPortGroupRowStatus,
       "vlanPortStatus": vlanPortStatus,
       "vlanPortGroupNextIndex": vlanPortGroupNextIndex,
       "vlanMacListTable": vlanMacListTable,
       "vlanMacListEntry": vlanMacListEntry,
       "vlanMacListIndex": vlanMacListIndex,
       "vlanMacAddress": vlanMacAddress,
       "vlanMacListRowStatus": vlanMacListRowStatus,
       "vlanMacListNextIndex": vlanMacListNextIndex}
)
