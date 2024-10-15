# SNMP MIB module (TPLINK-VLAN-QINQ-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-VLAN-QINQ-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:49 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkQinqVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17)
)
tplinkQinqVlanMIB.setRevisions(
        ("2008-12-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkQinqVlanMIBObjects_ObjectIdentity = ObjectIdentity
tplinkQinqVlanMIBObjects = _TplinkQinqVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1)
)


class _VpnConfigVpnMode_Type(Integer32):
    """Custom type vpnConfigVpnMode based on Integer32"""
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


_VpnConfigVpnMode_Type.__name__ = "Integer32"
_VpnConfigVpnMode_Object = MibScalar
vpnConfigVpnMode = _VpnConfigVpnMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 1),
    _VpnConfigVpnMode_Type()
)
vpnConfigVpnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigVpnMode.setStatus("current")


class _VpnConfigTpid_Type(OctetString):
    """Custom type vpnConfigTpid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VpnConfigTpid_Type.__name__ = "OctetString"
_VpnConfigTpid_Object = MibScalar
vpnConfigTpid = _VpnConfigTpid_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 2),
    _VpnConfigTpid_Type()
)
vpnConfigTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigTpid.setStatus("current")
_VpnConfigUplinkPortTable_Object = MibTable
vpnConfigUplinkPortTable = _VpnConfigUplinkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3)
)
if mibBuilder.loadTexts:
    vpnConfigUplinkPortTable.setStatus("current")
_VpnConfigUplinkPortEntry_Object = MibTableRow
vpnConfigUplinkPortEntry = _VpnConfigUplinkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 1)
)
vpnConfigUplinkPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vpnConfigUplinkPortEntry.setStatus("current")


class _VpnConfigUplinkPortEnable_Type(Integer32):
    """Custom type vpnConfigUplinkPortEnable based on Integer32"""
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


_VpnConfigUplinkPortEnable_Type.__name__ = "Integer32"
_VpnConfigUplinkPortEnable_Object = MibTableColumn
vpnConfigUplinkPortEnable = _VpnConfigUplinkPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 3, 1, 1),
    _VpnConfigUplinkPortEnable_Type()
)
vpnConfigUplinkPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigUplinkPortEnable.setStatus("current")
_VpnConfigPort_ObjectIdentity = ObjectIdentity
vpnConfigPort = _VpnConfigPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 4)
)
_VpnConfigPortEnableTable_Object = MibTable
vpnConfigPortEnableTable = _VpnConfigPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 4, 1)
)
if mibBuilder.loadTexts:
    vpnConfigPortEnableTable.setStatus("current")
_VpnConfigPortEnableEntry_Object = MibTableRow
vpnConfigPortEnableEntry = _VpnConfigPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 4, 1, 1)
)
vpnConfigPortEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vpnConfigPortEnableEntry.setStatus("current")


class _VpnConfigPortEnable_Type(Integer32):
    """Custom type vpnConfigPortEnable based on Integer32"""
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


_VpnConfigPortEnable_Type.__name__ = "Integer32"
_VpnConfigPortEnable_Object = MibTableColumn
vpnConfigPortEnable = _VpnConfigPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 4, 1, 1, 1),
    _VpnConfigPortEnable_Type()
)
vpnConfigPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigPortEnable.setStatus("current")
_VpnConfigVlanMapping_ObjectIdentity = ObjectIdentity
vpnConfigVlanMapping = _VpnConfigVlanMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5)
)


class _VpnConfigVlanMappingMode_Type(Integer32):
    """Custom type vpnConfigVlanMappingMode based on Integer32"""
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


_VpnConfigVlanMappingMode_Type.__name__ = "Integer32"
_VpnConfigVlanMappingMode_Object = MibScalar
vpnConfigVlanMappingMode = _VpnConfigVlanMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 1),
    _VpnConfigVlanMappingMode_Type()
)
vpnConfigVlanMappingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingMode.setStatus("current")
_VpnConfigVlanMappingTable_Object = MibTable
vpnConfigVlanMappingTable = _VpnConfigVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 2)
)
if mibBuilder.loadTexts:
    vpnConfigVlanMappingTable.setStatus("current")
_VpnConfigVlanMappingEntry_Object = MibTableRow
vpnConfigVlanMappingEntry = _VpnConfigVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 2, 1)
)
vpnConfigVlanMappingEntry.setIndexNames(
    (0, "TPLINK-VLAN-QINQ-MIB", "vpnConfigVlanMappingCVlan"),
    (0, "TPLINK-VLAN-QINQ-MIB", "vpnConfigVlanMappingPort"),
)
if mibBuilder.loadTexts:
    vpnConfigVlanMappingEntry.setStatus("current")
_VpnConfigVlanMappingPort_Type = OctetString
_VpnConfigVlanMappingPort_Object = MibTableColumn
vpnConfigVlanMappingPort = _VpnConfigVlanMappingPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 2, 1, 1),
    _VpnConfigVlanMappingPort_Type()
)
vpnConfigVlanMappingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingPort.setStatus("current")


class _VpnConfigVlanMappingCVlan_Type(Integer32):
    """Custom type vpnConfigVlanMappingCVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VpnConfigVlanMappingCVlan_Type.__name__ = "Integer32"
_VpnConfigVlanMappingCVlan_Object = MibTableColumn
vpnConfigVlanMappingCVlan = _VpnConfigVlanMappingCVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 2, 1, 2),
    _VpnConfigVlanMappingCVlan_Type()
)
vpnConfigVlanMappingCVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingCVlan.setStatus("current")


class _VpnConfigVlanMappingSPVlan_Type(Integer32):
    """Custom type vpnConfigVlanMappingSPVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VpnConfigVlanMappingSPVlan_Type.__name__ = "Integer32"
_VpnConfigVlanMappingSPVlan_Object = MibTableColumn
vpnConfigVlanMappingSPVlan = _VpnConfigVlanMappingSPVlan_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 2, 1, 3),
    _VpnConfigVlanMappingSPVlan_Type()
)
vpnConfigVlanMappingSPVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingSPVlan.setStatus("current")
_VpnConfigVlanMappingDesc_Type = OctetString
_VpnConfigVlanMappingDesc_Object = MibTableColumn
vpnConfigVlanMappingDesc = _VpnConfigVlanMappingDesc_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 2, 1, 4),
    _VpnConfigVlanMappingDesc_Type()
)
vpnConfigVlanMappingDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingDesc.setStatus("current")
_VpnConfigVlanMappingStatus_Type = TPRowStatus
_VpnConfigVlanMappingStatus_Object = MibTableColumn
vpnConfigVlanMappingStatus = _VpnConfigVlanMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 1, 5, 2, 1, 5),
    _VpnConfigVlanMappingStatus_Type()
)
vpnConfigVlanMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpnConfigVlanMappingStatus.setStatus("current")
_TplinkQinqVlanMIBNotifications_ObjectIdentity = ObjectIdentity
tplinkQinqVlanMIBNotifications = _TplinkQinqVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 17, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-VLAN-QINQ-MIB",
    **{"tplinkQinqVlanMIB": tplinkQinqVlanMIB,
       "tplinkQinqVlanMIBObjects": tplinkQinqVlanMIBObjects,
       "vpnConfigVpnMode": vpnConfigVpnMode,
       "vpnConfigTpid": vpnConfigTpid,
       "vpnConfigUplinkPortTable": vpnConfigUplinkPortTable,
       "vpnConfigUplinkPortEntry": vpnConfigUplinkPortEntry,
       "vpnConfigUplinkPortEnable": vpnConfigUplinkPortEnable,
       "vpnConfigPort": vpnConfigPort,
       "vpnConfigPortEnableTable": vpnConfigPortEnableTable,
       "vpnConfigPortEnableEntry": vpnConfigPortEnableEntry,
       "vpnConfigPortEnable": vpnConfigPortEnable,
       "vpnConfigVlanMapping": vpnConfigVlanMapping,
       "vpnConfigVlanMappingMode": vpnConfigVlanMappingMode,
       "vpnConfigVlanMappingTable": vpnConfigVlanMappingTable,
       "vpnConfigVlanMappingEntry": vpnConfigVlanMappingEntry,
       "vpnConfigVlanMappingPort": vpnConfigVlanMappingPort,
       "vpnConfigVlanMappingCVlan": vpnConfigVlanMappingCVlan,
       "vpnConfigVlanMappingSPVlan": vpnConfigVlanMappingSPVlan,
       "vpnConfigVlanMappingDesc": vpnConfigVlanMappingDesc,
       "vpnConfigVlanMappingStatus": vpnConfigVlanMappingStatus,
       "tplinkQinqVlanMIBNotifications": tplinkQinqVlanMIBNotifications}
)
