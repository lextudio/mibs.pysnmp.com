# SNMP MIB module (ZYXEL-IPSG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-IPSG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:04 2024
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelIpsg = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelArpFreezeSetup_ObjectIdentity = ObjectIdentity
zyxelArpFreezeSetup = _ZyxelArpFreezeSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1)
)
_ZyArpFreeze_Type = Integer32
_ZyArpFreeze_Object = MibScalar
zyArpFreeze = _ZyArpFreeze_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1, 1),
    _ZyArpFreeze_Type()
)
zyArpFreeze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpFreeze.setStatus("current")
_ZyArpFreezePorts_Type = PortList
_ZyArpFreezePorts_Object = MibScalar
zyArpFreezePorts = _ZyArpFreezePorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1, 2),
    _ZyArpFreezePorts_Type()
)
zyArpFreezePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpFreezePorts.setStatus("current")
_ZyArpFreezeVlan_Type = Integer32
_ZyArpFreezeVlan_Object = MibScalar
zyArpFreezeVlan = _ZyArpFreezeVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 1, 3),
    _ZyArpFreezeVlan_Type()
)
zyArpFreezeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpFreezeVlan.setStatus("current")
_ZyxelIpsgStatus_ObjectIdentity = ObjectIdentity
zyxelIpsgStatus = _ZyxelIpsgStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2)
)
_ZyxelIpsgInfoTable_Object = MibTable
zyxelIpsgInfoTable = _ZyxelIpsgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelIpsgInfoTable.setStatus("current")
_ZyxelIpsgInfoEntry_Object = MibTableRow
zyxelIpsgInfoEntry = _ZyxelIpsgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1)
)
zyxelIpsgInfoEntry.setIndexNames(
    (0, "ZYXEL-IPSG-MIB", "zyIpsgInfoMacAddress"),
    (0, "ZYXEL-IPSG-MIB", "zyIpsgInfoVid"),
)
if mibBuilder.loadTexts:
    zyxelIpsgInfoEntry.setStatus("current")
_ZyIpsgInfoMacAddress_Type = MacAddress
_ZyIpsgInfoMacAddress_Object = MibTableColumn
zyIpsgInfoMacAddress = _ZyIpsgInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 1),
    _ZyIpsgInfoMacAddress_Type()
)
zyIpsgInfoMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpsgInfoMacAddress.setStatus("current")


class _ZyIpsgInfoVid_Type(Integer32):
    """Custom type zyIpsgInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyIpsgInfoVid_Type.__name__ = "Integer32"
_ZyIpsgInfoVid_Object = MibTableColumn
zyIpsgInfoVid = _ZyIpsgInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 2),
    _ZyIpsgInfoVid_Type()
)
zyIpsgInfoVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyIpsgInfoVid.setStatus("current")
_ZyIpsgInfoIpAddress_Type = IpAddress
_ZyIpsgInfoIpAddress_Object = MibTableColumn
zyIpsgInfoIpAddress = _ZyIpsgInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 3),
    _ZyIpsgInfoIpAddress_Type()
)
zyIpsgInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpsgInfoIpAddress.setStatus("current")
_ZyIpsgInfoLeaseTime_Type = Integer32
_ZyIpsgInfoLeaseTime_Object = MibTableColumn
zyIpsgInfoLeaseTime = _ZyIpsgInfoLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 4),
    _ZyIpsgInfoLeaseTime_Type()
)
zyIpsgInfoLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpsgInfoLeaseTime.setStatus("current")


class _ZyIpsgInfoType_Type(Integer32):
    """Custom type zyIpsgInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 2),
          ("static", 1))
    )


_ZyIpsgInfoType_Type.__name__ = "Integer32"
_ZyIpsgInfoType_Object = MibTableColumn
zyIpsgInfoType = _ZyIpsgInfoType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 5),
    _ZyIpsgInfoType_Type()
)
zyIpsgInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpsgInfoType.setStatus("current")
_ZyIpsgInfoPort_Type = Integer32
_ZyIpsgInfoPort_Object = MibTableColumn
zyIpsgInfoPort = _ZyIpsgInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 2, 1, 1, 6),
    _ZyIpsgInfoPort_Type()
)
zyIpsgInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyIpsgInfoPort.setStatus("current")
_ZyxelStaticBindingSetup_ObjectIdentity = ObjectIdentity
zyxelStaticBindingSetup = _ZyxelStaticBindingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3)
)
_ZyStaticBindingMaxNumberOfRules_Type = Integer32
_ZyStaticBindingMaxNumberOfRules_Object = MibScalar
zyStaticBindingMaxNumberOfRules = _ZyStaticBindingMaxNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 1),
    _ZyStaticBindingMaxNumberOfRules_Type()
)
zyStaticBindingMaxNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStaticBindingMaxNumberOfRules.setStatus("current")
_ZyxelStaticBindingTable_Object = MibTable
zyxelStaticBindingTable = _ZyxelStaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2)
)
if mibBuilder.loadTexts:
    zyxelStaticBindingTable.setStatus("current")
_ZyxelStaticBindingEntry_Object = MibTableRow
zyxelStaticBindingEntry = _ZyxelStaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1)
)
zyxelStaticBindingEntry.setIndexNames(
    (0, "ZYXEL-IPSG-MIB", "zyStaticBindingMacAddress"),
    (0, "ZYXEL-IPSG-MIB", "zyStaticBindingVid"),
)
if mibBuilder.loadTexts:
    zyxelStaticBindingEntry.setStatus("current")
_ZyStaticBindingMacAddress_Type = MacAddress
_ZyStaticBindingMacAddress_Object = MibTableColumn
zyStaticBindingMacAddress = _ZyStaticBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 1),
    _ZyStaticBindingMacAddress_Type()
)
zyStaticBindingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticBindingMacAddress.setStatus("current")


class _ZyStaticBindingVid_Type(Integer32):
    """Custom type zyStaticBindingVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyStaticBindingVid_Type.__name__ = "Integer32"
_ZyStaticBindingVid_Object = MibTableColumn
zyStaticBindingVid = _ZyStaticBindingVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 2),
    _ZyStaticBindingVid_Type()
)
zyStaticBindingVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticBindingVid.setStatus("current")
_ZyStaticBindingIpAddress_Type = IpAddress
_ZyStaticBindingIpAddress_Object = MibTableColumn
zyStaticBindingIpAddress = _ZyStaticBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 3),
    _ZyStaticBindingIpAddress_Type()
)
zyStaticBindingIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStaticBindingIpAddress.setStatus("current")
_ZyStaticBindingPort_Type = Integer32
_ZyStaticBindingPort_Object = MibTableColumn
zyStaticBindingPort = _ZyStaticBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 4),
    _ZyStaticBindingPort_Type()
)
zyStaticBindingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyStaticBindingPort.setStatus("current")
_ZyStaticBindingRowStatus_Type = RowStatus
_ZyStaticBindingRowStatus_Object = MibTableColumn
zyStaticBindingRowStatus = _ZyStaticBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 33, 3, 2, 1, 5),
    _ZyStaticBindingRowStatus_Type()
)
zyStaticBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyStaticBindingRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-IPSG-MIB",
    **{"zyxelIpsg": zyxelIpsg,
       "zyxelArpFreezeSetup": zyxelArpFreezeSetup,
       "zyArpFreeze": zyArpFreeze,
       "zyArpFreezePorts": zyArpFreezePorts,
       "zyArpFreezeVlan": zyArpFreezeVlan,
       "zyxelIpsgStatus": zyxelIpsgStatus,
       "zyxelIpsgInfoTable": zyxelIpsgInfoTable,
       "zyxelIpsgInfoEntry": zyxelIpsgInfoEntry,
       "zyIpsgInfoMacAddress": zyIpsgInfoMacAddress,
       "zyIpsgInfoVid": zyIpsgInfoVid,
       "zyIpsgInfoIpAddress": zyIpsgInfoIpAddress,
       "zyIpsgInfoLeaseTime": zyIpsgInfoLeaseTime,
       "zyIpsgInfoType": zyIpsgInfoType,
       "zyIpsgInfoPort": zyIpsgInfoPort,
       "zyxelStaticBindingSetup": zyxelStaticBindingSetup,
       "zyStaticBindingMaxNumberOfRules": zyStaticBindingMaxNumberOfRules,
       "zyxelStaticBindingTable": zyxelStaticBindingTable,
       "zyxelStaticBindingEntry": zyxelStaticBindingEntry,
       "zyStaticBindingMacAddress": zyStaticBindingMacAddress,
       "zyStaticBindingVid": zyStaticBindingVid,
       "zyStaticBindingIpAddress": zyStaticBindingIpAddress,
       "zyStaticBindingPort": zyStaticBindingPort,
       "zyStaticBindingRowStatus": zyStaticBindingRowStatus}
)
