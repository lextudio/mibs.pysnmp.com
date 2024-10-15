# SNMP MIB module (TPLINK-PRIVATE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-PRIVATE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:32 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkPrivateVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18)
)
tplinkPrivateVlanMIB.setRevisions(
        ("2010-12-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkPrivateVlanMIBObjects_ObjectIdentity = ObjectIdentity
tplinkPrivateVlanMIBObjects = _TplinkPrivateVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1)
)
_PrivateVlanTable_Object = MibTable
privateVlanTable = _PrivateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 1)
)
if mibBuilder.loadTexts:
    privateVlanTable.setStatus("current")
_PrivateVlanEntry_Object = MibTableRow
privateVlanEntry = _PrivateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 1, 1)
)
privateVlanEntry.setIndexNames(
    (0, "TPLINK-PRIVATE-VLAN-MIB", "secondaryVlan"),
)
if mibBuilder.loadTexts:
    privateVlanEntry.setStatus("current")


class _SecondaryVlan_Type(Integer32):
    """Custom type secondaryVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_SecondaryVlan_Type.__name__ = "Integer32"
_SecondaryVlan_Object = MibTableColumn
secondaryVlan = _SecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 1, 1, 1),
    _SecondaryVlan_Type()
)
secondaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secondaryVlan.setStatus("current")


class _PrimaryVlan_Type(Integer32):
    """Custom type primaryVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_PrimaryVlan_Type.__name__ = "Integer32"
_PrimaryVlan_Object = MibTableColumn
primaryVlan = _PrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 1, 1, 2),
    _PrimaryVlan_Type()
)
primaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    primaryVlan.setStatus("current")


class _PrivateVlanPort_Type(OctetString):
    """Custom type privateVlanPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PrivateVlanPort_Type.__name__ = "OctetString"
_PrivateVlanPort_Object = MibTableColumn
privateVlanPort = _PrivateVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 1, 1, 3),
    _PrivateVlanPort_Type()
)
privateVlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPort.setStatus("current")


class _PrivateVlanType_Type(Integer32):
    """Custom type privateVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("community", 1),
          ("isolated", 2))
    )


_PrivateVlanType_Type.__name__ = "Integer32"
_PrivateVlanType_Object = MibTableColumn
privateVlanType = _PrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 1, 1, 4),
    _PrivateVlanType_Type()
)
privateVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanType.setStatus("current")
_PrivateVlanStatus_Type = TPRowStatus
_PrivateVlanStatus_Object = MibTableColumn
privateVlanStatus = _PrivateVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 1, 1, 5),
    _PrivateVlanStatus_Type()
)
privateVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanStatus.setStatus("current")
_PrivateVlanPortTable_Object = MibTable
privateVlanPortTable = _PrivateVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 2)
)
if mibBuilder.loadTexts:
    privateVlanPortTable.setStatus("current")
_PrivateVlanPortEntry_Object = MibTableRow
privateVlanPortEntry = _PrivateVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 2, 1)
)
privateVlanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    privateVlanPortEntry.setStatus("current")


class _PortNum_Type(OctetString):
    """Custom type portNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortNum_Type.__name__ = "OctetString"
_PortNum_Object = MibTableColumn
portNum = _PortNum_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 2, 1, 1),
    _PortNum_Type()
)
portNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portNum.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host", 2),
          ("promiscuous", 1))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 2, 1, 2),
    _PortType_Type()
)
portType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortConfigPrimaryVlan_Type(Integer32):
    """Custom type portConfigPrimaryVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_PortConfigPrimaryVlan_Type.__name__ = "Integer32"
_PortConfigPrimaryVlan_Object = MibTableColumn
portConfigPrimaryVlan = _PortConfigPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 2, 1, 3),
    _PortConfigPrimaryVlan_Type()
)
portConfigPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portConfigPrimaryVlan.setStatus("current")


class _PortConfigsecondaryVlan_Type(Integer32):
    """Custom type portConfigsecondaryVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_PortConfigsecondaryVlan_Type.__name__ = "Integer32"
_PortConfigsecondaryVlan_Object = MibTableColumn
portConfigsecondaryVlan = _PortConfigsecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 2, 1, 4),
    _PortConfigsecondaryVlan_Type()
)
portConfigsecondaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portConfigsecondaryVlan.setStatus("current")
_VlanPortStatus_Type = TPRowStatus
_VlanPortStatus_Object = MibTableColumn
vlanPortStatus = _VlanPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 1, 2, 1, 5),
    _VlanPortStatus_Type()
)
vlanPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanPortStatus.setStatus("current")
_TplinkPrivateVlanMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkPrivateVlanMIBNotifications = _TplinkPrivateVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 18, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-PRIVATE-VLAN-MIB",
    **{"tplinkPrivateVlanMIB": tplinkPrivateVlanMIB,
       "tplinkPrivateVlanMIBObjects": tplinkPrivateVlanMIBObjects,
       "privateVlanTable": privateVlanTable,
       "privateVlanEntry": privateVlanEntry,
       "secondaryVlan": secondaryVlan,
       "primaryVlan": primaryVlan,
       "privateVlanPort": privateVlanPort,
       "privateVlanType": privateVlanType,
       "privateVlanStatus": privateVlanStatus,
       "privateVlanPortTable": privateVlanPortTable,
       "privateVlanPortEntry": privateVlanPortEntry,
       "portNum": portNum,
       "portType": portType,
       "portConfigPrimaryVlan": portConfigPrimaryVlan,
       "portConfigsecondaryVlan": portConfigsecondaryVlan,
       "vlanPortStatus": vlanPortStatus,
       "tplinkPrivateVlanMIBNotifications": tplinkPrivateVlanMIBNotifications}
)
