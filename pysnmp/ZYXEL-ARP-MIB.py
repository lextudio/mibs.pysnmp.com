# SNMP MIB module (ZYXEL-ARP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-ARP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:22 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

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

zyxelArp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelArpSetup_ObjectIdentity = ObjectIdentity
zyxelArpSetup = _ZyxelArpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1)
)
_ZyxelArpLearningPortTable_Object = MibTable
zyxelArpLearningPortTable = _ZyxelArpLearningPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelArpLearningPortTable.setStatus("current")
_ZyxelArpLearningPortEntry_Object = MibTableRow
zyxelArpLearningPortEntry = _ZyxelArpLearningPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 1, 1)
)
zyxelArpLearningPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelArpLearningPortEntry.setStatus("current")


class _ZyArpLearningPortMode_Type(Integer32):
    """Custom type zyArpLearningPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("arpReply", 0),
          ("arpRequest", 2),
          ("gratuitousArp", 1))
    )


_ZyArpLearningPortMode_Type.__name__ = "Integer32"
_ZyArpLearningPortMode_Object = MibTableColumn
zyArpLearningPortMode = _ZyArpLearningPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 1, 1, 1),
    _ZyArpLearningPortMode_Type()
)
zyArpLearningPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpLearningPortMode.setStatus("current")
_ZyArpAgingTime_Type = Integer32
_ZyArpAgingTime_Object = MibScalar
zyArpAgingTime = _ZyArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 2),
    _ZyArpAgingTime_Type()
)
zyArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyArpAgingTime.setStatus("current")
_ZyStaticArpMaxNumberOfArps_Type = Integer32
_ZyStaticArpMaxNumberOfArps_Object = MibScalar
zyStaticArpMaxNumberOfArps = _ZyStaticArpMaxNumberOfArps_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 3),
    _ZyStaticArpMaxNumberOfArps_Type()
)
zyStaticArpMaxNumberOfArps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyStaticArpMaxNumberOfArps.setStatus("current")
_ZyxelStaticArpTable_Object = MibTable
zyxelStaticArpTable = _ZyxelStaticArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelStaticArpTable.setStatus("current")
_ZyxelStaticArpEntry_Object = MibTableRow
zyxelStaticArpEntry = _ZyxelStaticArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 4, 1)
)
zyxelStaticArpEntry.setIndexNames(
    (0, "ZYXEL-ARP-MIB", "zyStaticArpIpAddrress"),
    (0, "ZYXEL-ARP-MIB", "zyStaticArpMacAddress"),
    (0, "ZYXEL-ARP-MIB", "zyStaticArpVlan"),
    (0, "ZYXEL-ARP-MIB", "zyStaticArpPort"),
)
if mibBuilder.loadTexts:
    zyxelStaticArpEntry.setStatus("current")
_ZyStaticArpIpAddrress_Type = IpAddress
_ZyStaticArpIpAddrress_Object = MibTableColumn
zyStaticArpIpAddrress = _ZyStaticArpIpAddrress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 4, 1, 1),
    _ZyStaticArpIpAddrress_Type()
)
zyStaticArpIpAddrress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticArpIpAddrress.setStatus("current")
_ZyStaticArpMacAddress_Type = MacAddress
_ZyStaticArpMacAddress_Object = MibTableColumn
zyStaticArpMacAddress = _ZyStaticArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 4, 1, 2),
    _ZyStaticArpMacAddress_Type()
)
zyStaticArpMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticArpMacAddress.setStatus("current")


class _ZyStaticArpVlan_Type(Integer32):
    """Custom type zyStaticArpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyStaticArpVlan_Type.__name__ = "Integer32"
_ZyStaticArpVlan_Object = MibTableColumn
zyStaticArpVlan = _ZyStaticArpVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 4, 1, 3),
    _ZyStaticArpVlan_Type()
)
zyStaticArpVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticArpVlan.setStatus("current")
_ZyStaticArpPort_Type = Integer32
_ZyStaticArpPort_Object = MibTableColumn
zyStaticArpPort = _ZyStaticArpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 4, 1, 4),
    _ZyStaticArpPort_Type()
)
zyStaticArpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyStaticArpPort.setStatus("current")
_ZyStaticArpRowStatus_Type = RowStatus
_ZyStaticArpRowStatus_Object = MibTableColumn
zyStaticArpRowStatus = _ZyStaticArpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 1, 4, 1, 5),
    _ZyStaticArpRowStatus_Type()
)
zyStaticArpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyStaticArpRowStatus.setStatus("current")
_ZyxelArpStatus_ObjectIdentity = ObjectIdentity
zyxelArpStatus = _ZyxelArpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2)
)
_ZyxelArpTable_Object = MibTable
zyxelArpTable = _ZyxelArpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelArpTable.setStatus("current")
_ZyxelArpEntry_Object = MibTableRow
zyxelArpEntry = _ZyxelArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2, 1, 1)
)
zyxelArpEntry.setIndexNames(
    (0, "ZYXEL-ARP-MIB", "zyArpIpAddress"),
    (0, "ZYXEL-ARP-MIB", "zyArpVid"),
)
if mibBuilder.loadTexts:
    zyxelArpEntry.setStatus("current")
_ZyArpIpAddress_Type = IpAddress
_ZyArpIpAddress_Object = MibTableColumn
zyArpIpAddress = _ZyArpIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2, 1, 1, 1),
    _ZyArpIpAddress_Type()
)
zyArpIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpIpAddress.setStatus("current")
_ZyArpVid_Type = Integer32
_ZyArpVid_Object = MibTableColumn
zyArpVid = _ZyArpVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2, 1, 1, 2),
    _ZyArpVid_Type()
)
zyArpVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyArpVid.setStatus("current")
_ZyArpMacAddress_Type = MacAddress
_ZyArpMacAddress_Object = MibTableColumn
zyArpMacAddress = _ZyArpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2, 1, 1, 3),
    _ZyArpMacAddress_Type()
)
zyArpMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpMacAddress.setStatus("current")
_ZyArpPort_Type = Integer32
_ZyArpPort_Object = MibTableColumn
zyArpPort = _ZyArpPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2, 1, 1, 4),
    _ZyArpPort_Type()
)
zyArpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpPort.setStatus("current")


class _ZyArpType_Type(Integer32):
    """Custom type zyArpType based on Integer32"""
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


_ZyArpType_Type.__name__ = "Integer32"
_ZyArpType_Object = MibTableColumn
zyArpType = _ZyArpType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 11, 2, 1, 1, 5),
    _ZyArpType_Type()
)
zyArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyArpType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ARP-MIB",
    **{"zyxelArp": zyxelArp,
       "zyxelArpSetup": zyxelArpSetup,
       "zyxelArpLearningPortTable": zyxelArpLearningPortTable,
       "zyxelArpLearningPortEntry": zyxelArpLearningPortEntry,
       "zyArpLearningPortMode": zyArpLearningPortMode,
       "zyArpAgingTime": zyArpAgingTime,
       "zyStaticArpMaxNumberOfArps": zyStaticArpMaxNumberOfArps,
       "zyxelStaticArpTable": zyxelStaticArpTable,
       "zyxelStaticArpEntry": zyxelStaticArpEntry,
       "zyStaticArpIpAddrress": zyStaticArpIpAddrress,
       "zyStaticArpMacAddress": zyStaticArpMacAddress,
       "zyStaticArpVlan": zyStaticArpVlan,
       "zyStaticArpPort": zyStaticArpPort,
       "zyStaticArpRowStatus": zyStaticArpRowStatus,
       "zyxelArpStatus": zyxelArpStatus,
       "zyxelArpTable": zyxelArpTable,
       "zyxelArpEntry": zyxelArpEntry,
       "zyArpIpAddress": zyArpIpAddress,
       "zyArpVid": zyArpVid,
       "zyArpMacAddress": zyArpMacAddress,
       "zyArpPort": zyArpPort,
       "zyArpType": zyArpType}
)
