# SNMP MIB module (ZYXEL-AclV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-AclV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:27 2024
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

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

zyxelAclV2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelAclV2ClassifierStatus_ObjectIdentity = ObjectIdentity
zyxelAclV2ClassifierStatus = _ZyxelAclV2ClassifierStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1)
)
_ZyxelAclV2ClassifierTable_Object = MibTable
zyxelAclV2ClassifierTable = _ZyxelAclV2ClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierTable.setStatus("current")
_ZyxelAclV2ClassifierEntry_Object = MibTableRow
zyxelAclV2ClassifierEntry = _ZyxelAclV2ClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1)
)
zyxelAclV2ClassifierEntry.setIndexNames(
    (0, "ZYXEL-AclV2-MIB", "zyAclV2ClassifierName"),
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierEntry.setStatus("current")
_ZyAclV2ClassifierName_Type = DisplayString
_ZyAclV2ClassifierName_Object = MibTableColumn
zyAclV2ClassifierName = _ZyAclV2ClassifierName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1, 1),
    _ZyAclV2ClassifierName_Type()
)
zyAclV2ClassifierName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAclV2ClassifierName.setStatus("current")
_ZyAclV2ClassifierState_Type = EnabledStatus
_ZyAclV2ClassifierState_Object = MibTableColumn
zyAclV2ClassifierState = _ZyAclV2ClassifierState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1, 2),
    _ZyAclV2ClassifierState_Type()
)
zyAclV2ClassifierState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierState.setStatus("current")
_ZyAclV2ClassifierWeight_Type = Integer32
_ZyAclV2ClassifierWeight_Object = MibTableColumn
zyAclV2ClassifierWeight = _ZyAclV2ClassifierWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1, 3),
    _ZyAclV2ClassifierWeight_Type()
)
zyAclV2ClassifierWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierWeight.setStatus("current")
_ZyAclV2ClassifierCountState_Type = EnabledStatus
_ZyAclV2ClassifierCountState_Object = MibTableColumn
zyAclV2ClassifierCountState = _ZyAclV2ClassifierCountState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1, 4),
    _ZyAclV2ClassifierCountState_Type()
)
zyAclV2ClassifierCountState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierCountState.setStatus("current")
_ZyAclV2ClassifierLogState_Type = EnabledStatus
_ZyAclV2ClassifierLogState_Object = MibTableColumn
zyAclV2ClassifierLogState = _ZyAclV2ClassifierLogState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1, 5),
    _ZyAclV2ClassifierLogState_Type()
)
zyAclV2ClassifierLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierLogState.setStatus("current")
_ZyAclV2ClassifierTimeRange_Type = DisplayString
_ZyAclV2ClassifierTimeRange_Object = MibTableColumn
zyAclV2ClassifierTimeRange = _ZyAclV2ClassifierTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1, 6),
    _ZyAclV2ClassifierTimeRange_Type()
)
zyAclV2ClassifierTimeRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierTimeRange.setStatus("current")
_ZyAclV2ClassifierMatchCount_Type = Counter64
_ZyAclV2ClassifierMatchCount_Object = MibTableColumn
zyAclV2ClassifierMatchCount = _ZyAclV2ClassifierMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 1, 1, 7),
    _ZyAclV2ClassifierMatchCount_Type()
)
zyAclV2ClassifierMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierMatchCount.setStatus("current")
_ZyxelAclV2ClassifierEthernetTable_Object = MibTable
zyxelAclV2ClassifierEthernetTable = _ZyxelAclV2ClassifierEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierEthernetTable.setStatus("current")
_ZyxelAclV2ClassifierEthernetEntry_Object = MibTableRow
zyxelAclV2ClassifierEthernetEntry = _ZyxelAclV2ClassifierEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1)
)
zyxelAclV2ClassifierEthernetEntry.setIndexNames(
    (0, "ZYXEL-AclV2-MIB", "zyAclV2ClassifierName"),
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierEthernetEntry.setStatus("current")
_ZyAclV2ClassifierEthernetSourcePorts_Type = PortList
_ZyAclV2ClassifierEthernetSourcePorts_Object = MibTableColumn
zyAclV2ClassifierEthernetSourcePorts = _ZyAclV2ClassifierEthernetSourcePorts_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 1),
    _ZyAclV2ClassifierEthernetSourcePorts_Type()
)
zyAclV2ClassifierEthernetSourcePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetSourcePorts.setStatus("current")
_ZyAclV2ClassifierEthernetSourceTrunks_Type = PortList
_ZyAclV2ClassifierEthernetSourceTrunks_Object = MibTableColumn
zyAclV2ClassifierEthernetSourceTrunks = _ZyAclV2ClassifierEthernetSourceTrunks_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 2),
    _ZyAclV2ClassifierEthernetSourceTrunks_Type()
)
zyAclV2ClassifierEthernetSourceTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetSourceTrunks.setStatus("current")


class _ZyAclV2ClassifierEthernetPacketFormat_Type(Integer32):
    """Custom type zyAclV2ClassifierEthernetPacketFormat based on Integer32"""
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
        *(("all", 1),
          ("ethernet802dot3Tagged", 5),
          ("ethernet802dot3Untagged", 4),
          ("ethernetIITagged", 3),
          ("ethernetIIUntagged", 2))
    )


_ZyAclV2ClassifierEthernetPacketFormat_Type.__name__ = "Integer32"
_ZyAclV2ClassifierEthernetPacketFormat_Object = MibTableColumn
zyAclV2ClassifierEthernetPacketFormat = _ZyAclV2ClassifierEthernetPacketFormat_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 3),
    _ZyAclV2ClassifierEthernetPacketFormat_Type()
)
zyAclV2ClassifierEthernetPacketFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetPacketFormat.setStatus("current")
_ZyAclV2ClassifierEthernet8021pPriority_Type = Integer32
_ZyAclV2ClassifierEthernet8021pPriority_Object = MibTableColumn
zyAclV2ClassifierEthernet8021pPriority = _ZyAclV2ClassifierEthernet8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 4),
    _ZyAclV2ClassifierEthernet8021pPriority_Type()
)
zyAclV2ClassifierEthernet8021pPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernet8021pPriority.setStatus("current")
_ZyAclV2ClassifierEthernetInner8021pPriority_Type = Integer32
_ZyAclV2ClassifierEthernetInner8021pPriority_Object = MibTableColumn
zyAclV2ClassifierEthernetInner8021pPriority = _ZyAclV2ClassifierEthernetInner8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 5),
    _ZyAclV2ClassifierEthernetInner8021pPriority_Type()
)
zyAclV2ClassifierEthernetInner8021pPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetInner8021pPriority.setStatus("current")
_ZyAclV2ClassifierEthernetType_Type = Integer32
_ZyAclV2ClassifierEthernetType_Object = MibTableColumn
zyAclV2ClassifierEthernetType = _ZyAclV2ClassifierEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 6),
    _ZyAclV2ClassifierEthernetType_Type()
)
zyAclV2ClassifierEthernetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetType.setStatus("current")
_ZyAclV2ClassifierEthernetSourceMacAddress_Type = MacAddress
_ZyAclV2ClassifierEthernetSourceMacAddress_Object = MibTableColumn
zyAclV2ClassifierEthernetSourceMacAddress = _ZyAclV2ClassifierEthernetSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 7),
    _ZyAclV2ClassifierEthernetSourceMacAddress_Type()
)
zyAclV2ClassifierEthernetSourceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetSourceMacAddress.setStatus("current")
_ZyAclV2ClassifierEthernetSourceMACMask_Type = MacAddress
_ZyAclV2ClassifierEthernetSourceMACMask_Object = MibTableColumn
zyAclV2ClassifierEthernetSourceMACMask = _ZyAclV2ClassifierEthernetSourceMACMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 8),
    _ZyAclV2ClassifierEthernetSourceMACMask_Type()
)
zyAclV2ClassifierEthernetSourceMACMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetSourceMACMask.setStatus("current")
_ZyAclV2ClassifierEthernetDestinationMacAddress_Type = MacAddress
_ZyAclV2ClassifierEthernetDestinationMacAddress_Object = MibTableColumn
zyAclV2ClassifierEthernetDestinationMacAddress = _ZyAclV2ClassifierEthernetDestinationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 9),
    _ZyAclV2ClassifierEthernetDestinationMacAddress_Type()
)
zyAclV2ClassifierEthernetDestinationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetDestinationMacAddress.setStatus("current")
_ZyAclV2ClassifierEthernetDestinationMACMask_Type = MacAddress
_ZyAclV2ClassifierEthernetDestinationMACMask_Object = MibTableColumn
zyAclV2ClassifierEthernetDestinationMACMask = _ZyAclV2ClassifierEthernetDestinationMACMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 2, 1, 10),
    _ZyAclV2ClassifierEthernetDestinationMACMask_Type()
)
zyAclV2ClassifierEthernetDestinationMACMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierEthernetDestinationMACMask.setStatus("current")
_ZyxelAclV2ClassifierVlanTable_Object = MibTable
zyxelAclV2ClassifierVlanTable = _ZyxelAclV2ClassifierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierVlanTable.setStatus("current")
_ZyxelAclV2ClassifierVlanEntry_Object = MibTableRow
zyxelAclV2ClassifierVlanEntry = _ZyxelAclV2ClassifierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 3, 1)
)
zyxelAclV2ClassifierVlanEntry.setIndexNames(
    (0, "ZYXEL-AclV2-MIB", "zyAclV2ClassifierName"),
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierVlanEntry.setStatus("current")


class _ZyAclV2ClassifierVlanMap1k_Type(OctetString):
    """Custom type zyAclV2ClassifierVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierVlanMap1k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierVlanMap1k_Object = MibTableColumn
zyAclV2ClassifierVlanMap1k = _ZyAclV2ClassifierVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 3, 1, 1),
    _ZyAclV2ClassifierVlanMap1k_Type()
)
zyAclV2ClassifierVlanMap1k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierVlanMap1k.setStatus("current")


class _ZyAclV2ClassifierVlanMap2k_Type(OctetString):
    """Custom type zyAclV2ClassifierVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierVlanMap2k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierVlanMap2k_Object = MibTableColumn
zyAclV2ClassifierVlanMap2k = _ZyAclV2ClassifierVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 3, 1, 2),
    _ZyAclV2ClassifierVlanMap2k_Type()
)
zyAclV2ClassifierVlanMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierVlanMap2k.setStatus("current")


class _ZyAclV2ClassifierVlanMap3k_Type(OctetString):
    """Custom type zyAclV2ClassifierVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierVlanMap3k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierVlanMap3k_Object = MibTableColumn
zyAclV2ClassifierVlanMap3k = _ZyAclV2ClassifierVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 3, 1, 3),
    _ZyAclV2ClassifierVlanMap3k_Type()
)
zyAclV2ClassifierVlanMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierVlanMap3k.setStatus("current")


class _ZyAclV2ClassifierVlanMap4k_Type(OctetString):
    """Custom type zyAclV2ClassifierVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierVlanMap4k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierVlanMap4k_Object = MibTableColumn
zyAclV2ClassifierVlanMap4k = _ZyAclV2ClassifierVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 3, 1, 4),
    _ZyAclV2ClassifierVlanMap4k_Type()
)
zyAclV2ClassifierVlanMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierVlanMap4k.setStatus("current")
_ZyxelAclV2ClassifierInnerVlanTable_Object = MibTable
zyxelAclV2ClassifierInnerVlanTable = _ZyxelAclV2ClassifierInnerVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierInnerVlanTable.setStatus("current")
_ZyxelAclV2ClassifierInnerVlanEntry_Object = MibTableRow
zyxelAclV2ClassifierInnerVlanEntry = _ZyxelAclV2ClassifierInnerVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 4, 1)
)
zyxelAclV2ClassifierInnerVlanEntry.setIndexNames(
    (0, "ZYXEL-AclV2-MIB", "zyAclV2ClassifierName"),
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierInnerVlanEntry.setStatus("current")


class _ZyAclV2ClassifierInnerVlanMap1k_Type(OctetString):
    """Custom type zyAclV2ClassifierInnerVlanMap1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierInnerVlanMap1k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierInnerVlanMap1k_Object = MibTableColumn
zyAclV2ClassifierInnerVlanMap1k = _ZyAclV2ClassifierInnerVlanMap1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 4, 1, 1),
    _ZyAclV2ClassifierInnerVlanMap1k_Type()
)
zyAclV2ClassifierInnerVlanMap1k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierInnerVlanMap1k.setStatus("current")


class _ZyAclV2ClassifierInnerVlanMap2k_Type(OctetString):
    """Custom type zyAclV2ClassifierInnerVlanMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierInnerVlanMap2k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierInnerVlanMap2k_Object = MibTableColumn
zyAclV2ClassifierInnerVlanMap2k = _ZyAclV2ClassifierInnerVlanMap2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 4, 1, 2),
    _ZyAclV2ClassifierInnerVlanMap2k_Type()
)
zyAclV2ClassifierInnerVlanMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierInnerVlanMap2k.setStatus("current")


class _ZyAclV2ClassifierInnerVlanMap3k_Type(OctetString):
    """Custom type zyAclV2ClassifierInnerVlanMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierInnerVlanMap3k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierInnerVlanMap3k_Object = MibTableColumn
zyAclV2ClassifierInnerVlanMap3k = _ZyAclV2ClassifierInnerVlanMap3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 4, 1, 3),
    _ZyAclV2ClassifierInnerVlanMap3k_Type()
)
zyAclV2ClassifierInnerVlanMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierInnerVlanMap3k.setStatus("current")


class _ZyAclV2ClassifierInnerVlanMap4k_Type(OctetString):
    """Custom type zyAclV2ClassifierInnerVlanMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyAclV2ClassifierInnerVlanMap4k_Type.__name__ = "OctetString"
_ZyAclV2ClassifierInnerVlanMap4k_Object = MibTableColumn
zyAclV2ClassifierInnerVlanMap4k = _ZyAclV2ClassifierInnerVlanMap4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 4, 1, 4),
    _ZyAclV2ClassifierInnerVlanMap4k_Type()
)
zyAclV2ClassifierInnerVlanMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierInnerVlanMap4k.setStatus("current")
_ZyxelAclV2ClassifierIpTable_Object = MibTable
zyxelAclV2ClassifierIpTable = _ZyxelAclV2ClassifierIpTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierIpTable.setStatus("current")
_ZyxelAclV2ClassifierIpEntry_Object = MibTableRow
zyxelAclV2ClassifierIpEntry = _ZyxelAclV2ClassifierIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1)
)
zyxelAclV2ClassifierIpEntry.setIndexNames(
    (0, "ZYXEL-AclV2-MIB", "zyAclV2ClassifierName"),
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierIpEntry.setStatus("current")
_ZyAclV2ClassifierIpPacketLenRangeStart_Type = Integer32
_ZyAclV2ClassifierIpPacketLenRangeStart_Object = MibTableColumn
zyAclV2ClassifierIpPacketLenRangeStart = _ZyAclV2ClassifierIpPacketLenRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 1),
    _ZyAclV2ClassifierIpPacketLenRangeStart_Type()
)
zyAclV2ClassifierIpPacketLenRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpPacketLenRangeStart.setStatus("current")
_ZyAclV2ClassifierIpPacketLenRangeEnd_Type = Integer32
_ZyAclV2ClassifierIpPacketLenRangeEnd_Object = MibTableColumn
zyAclV2ClassifierIpPacketLenRangeEnd = _ZyAclV2ClassifierIpPacketLenRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 2),
    _ZyAclV2ClassifierIpPacketLenRangeEnd_Type()
)
zyAclV2ClassifierIpPacketLenRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpPacketLenRangeEnd.setStatus("current")
_ZyAclV2ClassifierIpDSCP_Type = Integer32
_ZyAclV2ClassifierIpDSCP_Object = MibTableColumn
zyAclV2ClassifierIpDSCP = _ZyAclV2ClassifierIpDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 3),
    _ZyAclV2ClassifierIpDSCP_Type()
)
zyAclV2ClassifierIpDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpDSCP.setStatus("current")
_ZyAclV2ClassifierIpPrecedence_Type = Integer32
_ZyAclV2ClassifierIpPrecedence_Object = MibTableColumn
zyAclV2ClassifierIpPrecedence = _ZyAclV2ClassifierIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 4),
    _ZyAclV2ClassifierIpPrecedence_Type()
)
zyAclV2ClassifierIpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpPrecedence.setStatus("current")
_ZyAclV2ClassifierIpToS_Type = Integer32
_ZyAclV2ClassifierIpToS_Object = MibTableColumn
zyAclV2ClassifierIpToS = _ZyAclV2ClassifierIpToS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 5),
    _ZyAclV2ClassifierIpToS_Type()
)
zyAclV2ClassifierIpToS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpToS.setStatus("current")
_ZyAclV2ClassifierIpProtocol_Type = Integer32
_ZyAclV2ClassifierIpProtocol_Object = MibTableColumn
zyAclV2ClassifierIpProtocol = _ZyAclV2ClassifierIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 6),
    _ZyAclV2ClassifierIpProtocol_Type()
)
zyAclV2ClassifierIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpProtocol.setStatus("current")
_ZyAclV2ClassifierIpEstablishOnly_Type = EnabledStatus
_ZyAclV2ClassifierIpEstablishOnly_Object = MibTableColumn
zyAclV2ClassifierIpEstablishOnly = _ZyAclV2ClassifierIpEstablishOnly_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 7),
    _ZyAclV2ClassifierIpEstablishOnly_Type()
)
zyAclV2ClassifierIpEstablishOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpEstablishOnly.setStatus("current")
_ZyAclV2ClassifierIpSourceIpAddress_Type = IpAddress
_ZyAclV2ClassifierIpSourceIpAddress_Object = MibTableColumn
zyAclV2ClassifierIpSourceIpAddress = _ZyAclV2ClassifierIpSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 8),
    _ZyAclV2ClassifierIpSourceIpAddress_Type()
)
zyAclV2ClassifierIpSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpSourceIpAddress.setStatus("current")
_ZyAclV2ClassifierIpSourceIpMaskBits_Type = Integer32
_ZyAclV2ClassifierIpSourceIpMaskBits_Object = MibTableColumn
zyAclV2ClassifierIpSourceIpMaskBits = _ZyAclV2ClassifierIpSourceIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 9),
    _ZyAclV2ClassifierIpSourceIpMaskBits_Type()
)
zyAclV2ClassifierIpSourceIpMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpSourceIpMaskBits.setStatus("current")
_ZyAclV2ClassifierIpDestinationIpAddress_Type = IpAddress
_ZyAclV2ClassifierIpDestinationIpAddress_Object = MibTableColumn
zyAclV2ClassifierIpDestinationIpAddress = _ZyAclV2ClassifierIpDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 10),
    _ZyAclV2ClassifierIpDestinationIpAddress_Type()
)
zyAclV2ClassifierIpDestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpDestinationIpAddress.setStatus("current")
_ZyAclV2ClassifierIpDestinationIpMaskBits_Type = Integer32
_ZyAclV2ClassifierIpDestinationIpMaskBits_Object = MibTableColumn
zyAclV2ClassifierIpDestinationIpMaskBits = _ZyAclV2ClassifierIpDestinationIpMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 11),
    _ZyAclV2ClassifierIpDestinationIpMaskBits_Type()
)
zyAclV2ClassifierIpDestinationIpMaskBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpDestinationIpMaskBits.setStatus("current")
_ZyAclV2ClassifierIpSourceSocketRangeStart_Type = Integer32
_ZyAclV2ClassifierIpSourceSocketRangeStart_Object = MibTableColumn
zyAclV2ClassifierIpSourceSocketRangeStart = _ZyAclV2ClassifierIpSourceSocketRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 12),
    _ZyAclV2ClassifierIpSourceSocketRangeStart_Type()
)
zyAclV2ClassifierIpSourceSocketRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpSourceSocketRangeStart.setStatus("current")
_ZyAclV2ClassifierIpSourceSocketRangeEnd_Type = Integer32
_ZyAclV2ClassifierIpSourceSocketRangeEnd_Object = MibTableColumn
zyAclV2ClassifierIpSourceSocketRangeEnd = _ZyAclV2ClassifierIpSourceSocketRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 13),
    _ZyAclV2ClassifierIpSourceSocketRangeEnd_Type()
)
zyAclV2ClassifierIpSourceSocketRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpSourceSocketRangeEnd.setStatus("current")
_ZyAclV2ClassifierIpDestinationSocketRangeStart_Type = Integer32
_ZyAclV2ClassifierIpDestinationSocketRangeStart_Object = MibTableColumn
zyAclV2ClassifierIpDestinationSocketRangeStart = _ZyAclV2ClassifierIpDestinationSocketRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 14),
    _ZyAclV2ClassifierIpDestinationSocketRangeStart_Type()
)
zyAclV2ClassifierIpDestinationSocketRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpDestinationSocketRangeStart.setStatus("current")
_ZyAclV2ClassifierIpDestinationSocketRangeEnd_Type = Integer32
_ZyAclV2ClassifierIpDestinationSocketRangeEnd_Object = MibTableColumn
zyAclV2ClassifierIpDestinationSocketRangeEnd = _ZyAclV2ClassifierIpDestinationSocketRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 5, 1, 15),
    _ZyAclV2ClassifierIpDestinationSocketRangeEnd_Type()
)
zyAclV2ClassifierIpDestinationSocketRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIpDestinationSocketRangeEnd.setStatus("current")
_ZyxelAclV2ClassifierIpv6Table_Object = MibTable
zyxelAclV2ClassifierIpv6Table = _ZyxelAclV2ClassifierIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierIpv6Table.setStatus("current")
_ZyxelAclV2ClassifierIpv6Entry_Object = MibTableRow
zyxelAclV2ClassifierIpv6Entry = _ZyxelAclV2ClassifierIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1)
)
zyxelAclV2ClassifierIpv6Entry.setIndexNames(
    (0, "ZYXEL-AclV2-MIB", "zyAclV2ClassifierName"),
)
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierIpv6Entry.setStatus("current")
_ZyAclV2ClassifierIPv6DSCP_Type = Integer32
_ZyAclV2ClassifierIPv6DSCP_Object = MibTableColumn
zyAclV2ClassifierIPv6DSCP = _ZyAclV2ClassifierIPv6DSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1, 1),
    _ZyAclV2ClassifierIPv6DSCP_Type()
)
zyAclV2ClassifierIPv6DSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIPv6DSCP.setStatus("current")
_ZyAclV2ClassifierIPv6NextHeader_Type = Integer32
_ZyAclV2ClassifierIPv6NextHeader_Object = MibTableColumn
zyAclV2ClassifierIPv6NextHeader = _ZyAclV2ClassifierIPv6NextHeader_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1, 2),
    _ZyAclV2ClassifierIPv6NextHeader_Type()
)
zyAclV2ClassifierIPv6NextHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIPv6NextHeader.setStatus("current")
_ZyAclV2ClassifierIPv6EstablishOnly_Type = EnabledStatus
_ZyAclV2ClassifierIPv6EstablishOnly_Object = MibTableColumn
zyAclV2ClassifierIPv6EstablishOnly = _ZyAclV2ClassifierIPv6EstablishOnly_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1, 3),
    _ZyAclV2ClassifierIPv6EstablishOnly_Type()
)
zyAclV2ClassifierIPv6EstablishOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIPv6EstablishOnly.setStatus("current")
_ZyAclV2ClassifierIPv6SourceIpAddress_Type = InetAddress
_ZyAclV2ClassifierIPv6SourceIpAddress_Object = MibTableColumn
zyAclV2ClassifierIPv6SourceIpAddress = _ZyAclV2ClassifierIPv6SourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1, 4),
    _ZyAclV2ClassifierIPv6SourceIpAddress_Type()
)
zyAclV2ClassifierIPv6SourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIPv6SourceIpAddress.setStatus("current")
_ZyAclV2ClassifierIPv6SourceIpPrefixLength_Type = Integer32
_ZyAclV2ClassifierIPv6SourceIpPrefixLength_Object = MibTableColumn
zyAclV2ClassifierIPv6SourceIpPrefixLength = _ZyAclV2ClassifierIPv6SourceIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1, 5),
    _ZyAclV2ClassifierIPv6SourceIpPrefixLength_Type()
)
zyAclV2ClassifierIPv6SourceIpPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIPv6SourceIpPrefixLength.setStatus("current")
_ZyAclV2ClassifierIPv6DestinationIpAddress_Type = InetAddress
_ZyAclV2ClassifierIPv6DestinationIpAddress_Object = MibTableColumn
zyAclV2ClassifierIPv6DestinationIpAddress = _ZyAclV2ClassifierIPv6DestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1, 6),
    _ZyAclV2ClassifierIPv6DestinationIpAddress_Type()
)
zyAclV2ClassifierIPv6DestinationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIPv6DestinationIpAddress.setStatus("current")
_ZyAclV2ClassifierIPv6DestinationIpPrefixLength_Type = Integer32
_ZyAclV2ClassifierIPv6DestinationIpPrefixLength_Object = MibTableColumn
zyAclV2ClassifierIPv6DestinationIpPrefixLength = _ZyAclV2ClassifierIPv6DestinationIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 6, 1, 7),
    _ZyAclV2ClassifierIPv6DestinationIpPrefixLength_Type()
)
zyAclV2ClassifierIPv6DestinationIpPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2ClassifierIPv6DestinationIpPrefixLength.setStatus("current")


class _ZyxelAclV2ClassifierMatchOrder_Type(Integer32):
    """Custom type zyxelAclV2ClassifierMatchOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_ZyxelAclV2ClassifierMatchOrder_Type.__name__ = "Integer32"
_ZyxelAclV2ClassifierMatchOrder_Object = MibScalar
zyxelAclV2ClassifierMatchOrder = _ZyxelAclV2ClassifierMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 7),
    _ZyxelAclV2ClassifierMatchOrder_Type()
)
zyxelAclV2ClassifierMatchOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierMatchOrder.setStatus("current")
_ZyxelAclV2ClassifierLoggingState_Type = EnabledStatus
_ZyxelAclV2ClassifierLoggingState_Object = MibScalar
zyxelAclV2ClassifierLoggingState = _ZyxelAclV2ClassifierLoggingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 8),
    _ZyxelAclV2ClassifierLoggingState_Type()
)
zyxelAclV2ClassifierLoggingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierLoggingState.setStatus("current")
_ZyxelAclV2ClassifierLoggingInterval_Type = Integer32
_ZyxelAclV2ClassifierLoggingInterval_Object = MibScalar
zyxelAclV2ClassifierLoggingInterval = _ZyxelAclV2ClassifierLoggingInterval_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 1, 9),
    _ZyxelAclV2ClassifierLoggingInterval_Type()
)
zyxelAclV2ClassifierLoggingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyxelAclV2ClassifierLoggingInterval.setStatus("current")
_ZyxelAclV2PolicyStatus_ObjectIdentity = ObjectIdentity
zyxelAclV2PolicyStatus = _ZyxelAclV2PolicyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2)
)
_ZyxelAclV2PolicyTable_Object = MibTable
zyxelAclV2PolicyTable = _ZyxelAclV2PolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1)
)
if mibBuilder.loadTexts:
    zyxelAclV2PolicyTable.setStatus("current")
_ZyxelAclV2PolicyEntry_Object = MibTableRow
zyxelAclV2PolicyEntry = _ZyxelAclV2PolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1)
)
zyxelAclV2PolicyEntry.setIndexNames(
    (0, "ZYXEL-AclV2-MIB", "zyAclV2PolicyName"),
)
if mibBuilder.loadTexts:
    zyxelAclV2PolicyEntry.setStatus("current")
_ZyAclV2PolicyName_Type = DisplayString
_ZyAclV2PolicyName_Object = MibTableColumn
zyAclV2PolicyName = _ZyAclV2PolicyName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 1),
    _ZyAclV2PolicyName_Type()
)
zyAclV2PolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAclV2PolicyName.setStatus("current")
_ZyAclV2PolicyState_Type = EnabledStatus
_ZyAclV2PolicyState_Object = MibTableColumn
zyAclV2PolicyState = _ZyAclV2PolicyState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 2),
    _ZyAclV2PolicyState_Type()
)
zyAclV2PolicyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyState.setStatus("current")
_ZyAclV2PolicyClassifier_Type = DisplayString
_ZyAclV2PolicyClassifier_Object = MibTableColumn
zyAclV2PolicyClassifier = _ZyAclV2PolicyClassifier_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 3),
    _ZyAclV2PolicyClassifier_Type()
)
zyAclV2PolicyClassifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyClassifier.setStatus("current")
_ZyAclV2PolicyVid_Type = Integer32
_ZyAclV2PolicyVid_Object = MibTableColumn
zyAclV2PolicyVid = _ZyAclV2PolicyVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 4),
    _ZyAclV2PolicyVid_Type()
)
zyAclV2PolicyVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyVid.setStatus("current")
_ZyAclV2PolicyEgressPort_Type = Integer32
_ZyAclV2PolicyEgressPort_Object = MibTableColumn
zyAclV2PolicyEgressPort = _ZyAclV2PolicyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 5),
    _ZyAclV2PolicyEgressPort_Type()
)
zyAclV2PolicyEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyEgressPort.setStatus("current")
_ZyAclV2Policy8021pPriority_Type = Integer32
_ZyAclV2Policy8021pPriority_Object = MibTableColumn
zyAclV2Policy8021pPriority = _ZyAclV2Policy8021pPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 6),
    _ZyAclV2Policy8021pPriority_Type()
)
zyAclV2Policy8021pPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2Policy8021pPriority.setStatus("current")
_ZyAclV2PolicyDSCP_Type = Integer32
_ZyAclV2PolicyDSCP_Object = MibTableColumn
zyAclV2PolicyDSCP = _ZyAclV2PolicyDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 7),
    _ZyAclV2PolicyDSCP_Type()
)
zyAclV2PolicyDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyDSCP.setStatus("current")
_ZyAclV2PolicyTOS_Type = Integer32
_ZyAclV2PolicyTOS_Object = MibTableColumn
zyAclV2PolicyTOS = _ZyAclV2PolicyTOS_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 8),
    _ZyAclV2PolicyTOS_Type()
)
zyAclV2PolicyTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyTOS.setStatus("current")
_ZyAclV2PolicyBandwidth_Type = Integer32
_ZyAclV2PolicyBandwidth_Object = MibTableColumn
zyAclV2PolicyBandwidth = _ZyAclV2PolicyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 9),
    _ZyAclV2PolicyBandwidth_Type()
)
zyAclV2PolicyBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyBandwidth.setStatus("current")
_ZyAclV2PolicyOutOfProfileDSCP_Type = Integer32
_ZyAclV2PolicyOutOfProfileDSCP_Object = MibTableColumn
zyAclV2PolicyOutOfProfileDSCP = _ZyAclV2PolicyOutOfProfileDSCP_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 10),
    _ZyAclV2PolicyOutOfProfileDSCP_Type()
)
zyAclV2PolicyOutOfProfileDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyOutOfProfileDSCP.setStatus("current")


class _ZyAclV2PolicyForwardingAction_Type(Integer32):
    """Custom type zyAclV2PolicyForwardingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discardThePacket", 2),
          ("doNotDropTheMatchingFramePreviouslyMarkedForDropping", 3),
          ("noChange", 1))
    )


_ZyAclV2PolicyForwardingAction_Type.__name__ = "Integer32"
_ZyAclV2PolicyForwardingAction_Object = MibTableColumn
zyAclV2PolicyForwardingAction = _ZyAclV2PolicyForwardingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 11),
    _ZyAclV2PolicyForwardingAction_Type()
)
zyAclV2PolicyForwardingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyForwardingAction.setStatus("current")


class _ZyAclV2PolicyPriorityAction_Type(Integer32):
    """Custom type zyAclV2PolicyPriorityAction based on Integer32"""
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
        *(("noChange", 1),
          ("replaceThe802dot1PriorityByInner802dot1Priority", 5),
          ("replaceThe802dot1PriorityFieldWithTheIpTosValue", 4),
          ("sendThePacketToPriorityQueue", 3),
          ("setThePackets802dot1Priority", 2))
    )


_ZyAclV2PolicyPriorityAction_Type.__name__ = "Integer32"
_ZyAclV2PolicyPriorityAction_Object = MibTableColumn
zyAclV2PolicyPriorityAction = _ZyAclV2PolicyPriorityAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 12),
    _ZyAclV2PolicyPriorityAction_Type()
)
zyAclV2PolicyPriorityAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyPriorityAction.setStatus("current")


class _ZyAclV2PolicyDiffServAction_Type(Integer32):
    """Custom type zyAclV2PolicyDiffServAction based on Integer32"""
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
        *(("noChange", 1),
          ("replaceTheIpTosFieldWithThe802dot1PriorityValue", 3),
          ("setTheDiffservCodepointFieldInTheFrame", 4),
          ("setThePacketsTosField", 2))
    )


_ZyAclV2PolicyDiffServAction_Type.__name__ = "Integer32"
_ZyAclV2PolicyDiffServAction_Object = MibTableColumn
zyAclV2PolicyDiffServAction = _ZyAclV2PolicyDiffServAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 13),
    _ZyAclV2PolicyDiffServAction_Type()
)
zyAclV2PolicyDiffServAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyDiffServAction.setStatus("current")


class _ZyAclV2PolicyOutgoingAction_Type(Bits):
    """Custom type zyAclV2PolicyOutgoingAction based on Bits"""
    namedValues = NamedValues(
        *(("sendTheMatchingFramesToTheEgressPort", 2),
          ("sendThePacketToTheEgressPort", 1),
          ("sendThePacketToTheMirrorPort", 0),
          ("setThePacketVlanId", 3))
    )

_ZyAclV2PolicyOutgoingAction_Type.__name__ = "Bits"
_ZyAclV2PolicyOutgoingAction_Object = MibTableColumn
zyAclV2PolicyOutgoingAction = _ZyAclV2PolicyOutgoingAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 14),
    _ZyAclV2PolicyOutgoingAction_Type()
)
zyAclV2PolicyOutgoingAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyOutgoingAction.setStatus("current")
_ZyAclV2PolicyMeteringState_Type = Integer32
_ZyAclV2PolicyMeteringState_Object = MibTableColumn
zyAclV2PolicyMeteringState = _ZyAclV2PolicyMeteringState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 15),
    _ZyAclV2PolicyMeteringState_Type()
)
zyAclV2PolicyMeteringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyMeteringState.setStatus("current")


class _ZyAclV2PolicyOutOfProfileAction_Type(Bits):
    """Custom type zyAclV2PolicyOutOfProfileAction based on Bits"""
    namedValues = NamedValues(
        *(("changeTheDscpValue", 1),
          ("doNotDropTheMatchingFramePreviouslyMarkedForDropping", 3),
          ("dropThePacket", 0),
          ("setOutDropPrecedence", 2))
    )

_ZyAclV2PolicyOutOfProfileAction_Type.__name__ = "Bits"
_ZyAclV2PolicyOutOfProfileAction_Object = MibTableColumn
zyAclV2PolicyOutOfProfileAction = _ZyAclV2PolicyOutOfProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 16),
    _ZyAclV2PolicyOutOfProfileAction_Type()
)
zyAclV2PolicyOutOfProfileAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyOutOfProfileAction.setStatus("current")
_ZyAclV2PolicyRowstatus_Type = RowStatus
_ZyAclV2PolicyRowstatus_Object = MibTableColumn
zyAclV2PolicyRowstatus = _ZyAclV2PolicyRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 17),
    _ZyAclV2PolicyRowstatus_Type()
)
zyAclV2PolicyRowstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyRowstatus.setStatus("current")


class _ZyAclV2PolicyQueueAction_Type(Integer32):
    """Custom type zyAclV2PolicyQueueAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noChange", 1),
          ("sendThePacketToPriorityQueue", 2))
    )


_ZyAclV2PolicyQueueAction_Type.__name__ = "Integer32"
_ZyAclV2PolicyQueueAction_Object = MibTableColumn
zyAclV2PolicyQueueAction = _ZyAclV2PolicyQueueAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 2, 1, 1, 18),
    _ZyAclV2PolicyQueueAction_Type()
)
zyAclV2PolicyQueueAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyAclV2PolicyQueueAction.setStatus("current")
_ZyxelAclV2TrapInfoObjects_ObjectIdentity = ObjectIdentity
zyxelAclV2TrapInfoObjects = _ZyxelAclV2TrapInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 3)
)
_ZyAclV2TrapClassifierLogMatchCount_Type = Integer32
_ZyAclV2TrapClassifierLogMatchCount_Object = MibScalar
zyAclV2TrapClassifierLogMatchCount = _ZyAclV2TrapClassifierLogMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 3, 1),
    _ZyAclV2TrapClassifierLogMatchCount_Type()
)
zyAclV2TrapClassifierLogMatchCount.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyAclV2TrapClassifierLogMatchCount.setStatus("current")
_ZyxelAclV2Notifications_ObjectIdentity = ObjectIdentity
zyxelAclV2Notifications = _ZyxelAclV2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 4)
)

# Managed Objects groups


# Notification objects

zyAclV2ClassifierLogNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 105, 4, 1)
)
zyAclV2ClassifierLogNotification.setObjects(
      *(("ZYXEL-AclV2-MIB", "zyAclV2ClassifierName"),
        ("ZYXEL-AclV2-MIB", "zyAclV2TrapClassifierLogMatchCount"))
)
if mibBuilder.loadTexts:
    zyAclV2ClassifierLogNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-AclV2-MIB",
    **{"zyxelAclV2": zyxelAclV2,
       "zyxelAclV2ClassifierStatus": zyxelAclV2ClassifierStatus,
       "zyxelAclV2ClassifierTable": zyxelAclV2ClassifierTable,
       "zyxelAclV2ClassifierEntry": zyxelAclV2ClassifierEntry,
       "zyAclV2ClassifierName": zyAclV2ClassifierName,
       "zyAclV2ClassifierState": zyAclV2ClassifierState,
       "zyAclV2ClassifierWeight": zyAclV2ClassifierWeight,
       "zyAclV2ClassifierCountState": zyAclV2ClassifierCountState,
       "zyAclV2ClassifierLogState": zyAclV2ClassifierLogState,
       "zyAclV2ClassifierTimeRange": zyAclV2ClassifierTimeRange,
       "zyAclV2ClassifierMatchCount": zyAclV2ClassifierMatchCount,
       "zyxelAclV2ClassifierEthernetTable": zyxelAclV2ClassifierEthernetTable,
       "zyxelAclV2ClassifierEthernetEntry": zyxelAclV2ClassifierEthernetEntry,
       "zyAclV2ClassifierEthernetSourcePorts": zyAclV2ClassifierEthernetSourcePorts,
       "zyAclV2ClassifierEthernetSourceTrunks": zyAclV2ClassifierEthernetSourceTrunks,
       "zyAclV2ClassifierEthernetPacketFormat": zyAclV2ClassifierEthernetPacketFormat,
       "zyAclV2ClassifierEthernet8021pPriority": zyAclV2ClassifierEthernet8021pPriority,
       "zyAclV2ClassifierEthernetInner8021pPriority": zyAclV2ClassifierEthernetInner8021pPriority,
       "zyAclV2ClassifierEthernetType": zyAclV2ClassifierEthernetType,
       "zyAclV2ClassifierEthernetSourceMacAddress": zyAclV2ClassifierEthernetSourceMacAddress,
       "zyAclV2ClassifierEthernetSourceMACMask": zyAclV2ClassifierEthernetSourceMACMask,
       "zyAclV2ClassifierEthernetDestinationMacAddress": zyAclV2ClassifierEthernetDestinationMacAddress,
       "zyAclV2ClassifierEthernetDestinationMACMask": zyAclV2ClassifierEthernetDestinationMACMask,
       "zyxelAclV2ClassifierVlanTable": zyxelAclV2ClassifierVlanTable,
       "zyxelAclV2ClassifierVlanEntry": zyxelAclV2ClassifierVlanEntry,
       "zyAclV2ClassifierVlanMap1k": zyAclV2ClassifierVlanMap1k,
       "zyAclV2ClassifierVlanMap2k": zyAclV2ClassifierVlanMap2k,
       "zyAclV2ClassifierVlanMap3k": zyAclV2ClassifierVlanMap3k,
       "zyAclV2ClassifierVlanMap4k": zyAclV2ClassifierVlanMap4k,
       "zyxelAclV2ClassifierInnerVlanTable": zyxelAclV2ClassifierInnerVlanTable,
       "zyxelAclV2ClassifierInnerVlanEntry": zyxelAclV2ClassifierInnerVlanEntry,
       "zyAclV2ClassifierInnerVlanMap1k": zyAclV2ClassifierInnerVlanMap1k,
       "zyAclV2ClassifierInnerVlanMap2k": zyAclV2ClassifierInnerVlanMap2k,
       "zyAclV2ClassifierInnerVlanMap3k": zyAclV2ClassifierInnerVlanMap3k,
       "zyAclV2ClassifierInnerVlanMap4k": zyAclV2ClassifierInnerVlanMap4k,
       "zyxelAclV2ClassifierIpTable": zyxelAclV2ClassifierIpTable,
       "zyxelAclV2ClassifierIpEntry": zyxelAclV2ClassifierIpEntry,
       "zyAclV2ClassifierIpPacketLenRangeStart": zyAclV2ClassifierIpPacketLenRangeStart,
       "zyAclV2ClassifierIpPacketLenRangeEnd": zyAclV2ClassifierIpPacketLenRangeEnd,
       "zyAclV2ClassifierIpDSCP": zyAclV2ClassifierIpDSCP,
       "zyAclV2ClassifierIpPrecedence": zyAclV2ClassifierIpPrecedence,
       "zyAclV2ClassifierIpToS": zyAclV2ClassifierIpToS,
       "zyAclV2ClassifierIpProtocol": zyAclV2ClassifierIpProtocol,
       "zyAclV2ClassifierIpEstablishOnly": zyAclV2ClassifierIpEstablishOnly,
       "zyAclV2ClassifierIpSourceIpAddress": zyAclV2ClassifierIpSourceIpAddress,
       "zyAclV2ClassifierIpSourceIpMaskBits": zyAclV2ClassifierIpSourceIpMaskBits,
       "zyAclV2ClassifierIpDestinationIpAddress": zyAclV2ClassifierIpDestinationIpAddress,
       "zyAclV2ClassifierIpDestinationIpMaskBits": zyAclV2ClassifierIpDestinationIpMaskBits,
       "zyAclV2ClassifierIpSourceSocketRangeStart": zyAclV2ClassifierIpSourceSocketRangeStart,
       "zyAclV2ClassifierIpSourceSocketRangeEnd": zyAclV2ClassifierIpSourceSocketRangeEnd,
       "zyAclV2ClassifierIpDestinationSocketRangeStart": zyAclV2ClassifierIpDestinationSocketRangeStart,
       "zyAclV2ClassifierIpDestinationSocketRangeEnd": zyAclV2ClassifierIpDestinationSocketRangeEnd,
       "zyxelAclV2ClassifierIpv6Table": zyxelAclV2ClassifierIpv6Table,
       "zyxelAclV2ClassifierIpv6Entry": zyxelAclV2ClassifierIpv6Entry,
       "zyAclV2ClassifierIPv6DSCP": zyAclV2ClassifierIPv6DSCP,
       "zyAclV2ClassifierIPv6NextHeader": zyAclV2ClassifierIPv6NextHeader,
       "zyAclV2ClassifierIPv6EstablishOnly": zyAclV2ClassifierIPv6EstablishOnly,
       "zyAclV2ClassifierIPv6SourceIpAddress": zyAclV2ClassifierIPv6SourceIpAddress,
       "zyAclV2ClassifierIPv6SourceIpPrefixLength": zyAclV2ClassifierIPv6SourceIpPrefixLength,
       "zyAclV2ClassifierIPv6DestinationIpAddress": zyAclV2ClassifierIPv6DestinationIpAddress,
       "zyAclV2ClassifierIPv6DestinationIpPrefixLength": zyAclV2ClassifierIPv6DestinationIpPrefixLength,
       "zyxelAclV2ClassifierMatchOrder": zyxelAclV2ClassifierMatchOrder,
       "zyxelAclV2ClassifierLoggingState": zyxelAclV2ClassifierLoggingState,
       "zyxelAclV2ClassifierLoggingInterval": zyxelAclV2ClassifierLoggingInterval,
       "zyxelAclV2PolicyStatus": zyxelAclV2PolicyStatus,
       "zyxelAclV2PolicyTable": zyxelAclV2PolicyTable,
       "zyxelAclV2PolicyEntry": zyxelAclV2PolicyEntry,
       "zyAclV2PolicyName": zyAclV2PolicyName,
       "zyAclV2PolicyState": zyAclV2PolicyState,
       "zyAclV2PolicyClassifier": zyAclV2PolicyClassifier,
       "zyAclV2PolicyVid": zyAclV2PolicyVid,
       "zyAclV2PolicyEgressPort": zyAclV2PolicyEgressPort,
       "zyAclV2Policy8021pPriority": zyAclV2Policy8021pPriority,
       "zyAclV2PolicyDSCP": zyAclV2PolicyDSCP,
       "zyAclV2PolicyTOS": zyAclV2PolicyTOS,
       "zyAclV2PolicyBandwidth": zyAclV2PolicyBandwidth,
       "zyAclV2PolicyOutOfProfileDSCP": zyAclV2PolicyOutOfProfileDSCP,
       "zyAclV2PolicyForwardingAction": zyAclV2PolicyForwardingAction,
       "zyAclV2PolicyPriorityAction": zyAclV2PolicyPriorityAction,
       "zyAclV2PolicyDiffServAction": zyAclV2PolicyDiffServAction,
       "zyAclV2PolicyOutgoingAction": zyAclV2PolicyOutgoingAction,
       "zyAclV2PolicyMeteringState": zyAclV2PolicyMeteringState,
       "zyAclV2PolicyOutOfProfileAction": zyAclV2PolicyOutOfProfileAction,
       "zyAclV2PolicyRowstatus": zyAclV2PolicyRowstatus,
       "zyAclV2PolicyQueueAction": zyAclV2PolicyQueueAction,
       "zyxelAclV2TrapInfoObjects": zyxelAclV2TrapInfoObjects,
       "zyAclV2TrapClassifierLogMatchCount": zyAclV2TrapClassifierLogMatchCount,
       "zyxelAclV2Notifications": zyxelAclV2Notifications,
       "zyAclV2ClassifierLogNotification": zyAclV2ClassifierLogNotification}
)
