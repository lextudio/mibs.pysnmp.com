# SNMP MIB module (Dlink-IMPB-MNG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Dlink-IMPB-MNG
# Produced by pysmi-1.5.4 at Mon Oct 14 21:35:54 2024
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(rlImpbManagment,) = mibBuilder.importSymbols(
    "Dlink-IMPB-FEATURES",
    "rlImpbManagment")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class IMPBPacketType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 2),
          ("ip", 1),
          ("iparp", 3))
    )



class IMPBLockMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("unlocked", 1))
    )



class IMPBDeviceType(Integer32, TextualConvention):
    status = "current"
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
        *(("dhcpSrv", 2),
          ("host", 1),
          ("router", 3),
          ("routerDhcp", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RlIMPBMngTable_Object = MibTable
rlIMPBMngTable = _RlIMPBMngTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1)
)
if mibBuilder.loadTexts:
    rlIMPBMngTable.setStatus("current")
_RlIMPBMngEntry_Object = MibTableRow
rlIMPBMngEntry = _RlIMPBMngEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1)
)
rlIMPBMngEntry.setIndexNames(
    (0, "Dlink-IMPB-MNG", "rlIMPBMngIPAddress"),
)
if mibBuilder.loadTexts:
    rlIMPBMngEntry.setStatus("current")
_RlIMPBMngIPAddress_Type = IpAddress
_RlIMPBMngIPAddress_Object = MibTableColumn
rlIMPBMngIPAddress = _RlIMPBMngIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 1),
    _RlIMPBMngIPAddress_Type()
)
rlIMPBMngIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIMPBMngIPAddress.setStatus("current")


class _RlIMPBMngPacketType_Type(IMPBPacketType):
    """Custom type rlIMPBMngPacketType based on IMPBPacketType"""


_RlIMPBMngPacketType_Object = MibTableColumn
rlIMPBMngPacketType = _RlIMPBMngPacketType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 2),
    _RlIMPBMngPacketType_Type()
)
rlIMPBMngPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngPacketType.setStatus("current")
_RlIMPBMngPMACAddress_Type = MacAddress
_RlIMPBMngPMACAddress_Object = MibTableColumn
rlIMPBMngPMACAddress = _RlIMPBMngPMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 3),
    _RlIMPBMngPMACAddress_Type()
)
rlIMPBMngPMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngPMACAddress.setStatus("current")


class _RlIMPBMngDeviceType_Type(IMPBDeviceType):
    """Custom type rlIMPBMngDeviceType based on IMPBDeviceType"""


_RlIMPBMngDeviceType_Object = MibTableColumn
rlIMPBMngDeviceType = _RlIMPBMngDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 4),
    _RlIMPBMngDeviceType_Type()
)
rlIMPBMngDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngDeviceType.setStatus("current")
_RlIMPBMngPortlist_Type = PortList
_RlIMPBMngPortlist_Object = MibTableColumn
rlIMPBMngPortlist = _RlIMPBMngPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 5),
    _RlIMPBMngPortlist_Type()
)
rlIMPBMngPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngPortlist.setStatus("current")


class _RlIMPBMngMode_Type(IMPBLockMode):
    """Custom type rlIMPBMngMode based on IMPBLockMode"""


_RlIMPBMngMode_Object = MibTableColumn
rlIMPBMngMode = _RlIMPBMngMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 6),
    _RlIMPBMngMode_Type()
)
rlIMPBMngMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngMode.setStatus("current")


class _RlIMPBMngRouterBandwidth_Type(Unsigned32):
    """Custom type rlIMPBMngRouterBandwidth based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 1000000),
    )


_RlIMPBMngRouterBandwidth_Type.__name__ = "Unsigned32"
_RlIMPBMngRouterBandwidth_Object = MibTableColumn
rlIMPBMngRouterBandwidth = _RlIMPBMngRouterBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 7),
    _RlIMPBMngRouterBandwidth_Type()
)
rlIMPBMngRouterBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngRouterBandwidth.setStatus("current")
_RlIMPBMngRowStatus_Type = RowStatus
_RlIMPBMngRowStatus_Object = MibTableColumn
rlIMPBMngRowStatus = _RlIMPBMngRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 1, 1, 8),
    _RlIMPBMngRowStatus_Type()
)
rlIMPBMngRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngRowStatus.setStatus("current")


class _RlIMPBMngAction_Type(Integer32):
    """Custom type rlIMPBMngAction based on Integer32"""
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
        *(("deleteAll", 5),
          ("deleteUnlock", 4),
          ("lockAll", 2),
          ("noAction", 1),
          ("unlockAll", 3))
    )


_RlIMPBMngAction_Type.__name__ = "Integer32"
_RlIMPBMngAction_Object = MibScalar
rlIMPBMngAction = _RlIMPBMngAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 2),
    _RlIMPBMngAction_Type()
)
rlIMPBMngAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngAction.setStatus("current")
_RlIMPBMngPortBandwidthTable_Object = MibTable
rlIMPBMngPortBandwidthTable = _RlIMPBMngPortBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 3)
)
if mibBuilder.loadTexts:
    rlIMPBMngPortBandwidthTable.setStatus("current")
_RlIMPBMngPortBandwidthEntry_Object = MibTableRow
rlIMPBMngPortBandwidthEntry = _RlIMPBMngPortBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 3, 1)
)
rlIMPBMngPortBandwidthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlIMPBMngPortBandwidthEntry.setStatus("current")


class _RlIMPBMngBandwidth_Type(Unsigned32):
    """Custom type rlIMPBMngBandwidth based on Unsigned32"""
    defaultValue = 0


_RlIMPBMngBandwidth_Object = MibTableColumn
rlIMPBMngBandwidth = _RlIMPBMngBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 3, 1, 1),
    _RlIMPBMngBandwidth_Type()
)
rlIMPBMngBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIMPBMngBandwidth.setStatus("current")
_RlIMPBMngRouterBandwidthTable_Object = MibTable
rlIMPBMngRouterBandwidthTable = _RlIMPBMngRouterBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4)
)
if mibBuilder.loadTexts:
    rlIMPBMngRouterBandwidthTable.setStatus("current")
_RlIMPBMngRouterBandwidthEntry_Object = MibTableRow
rlIMPBMngRouterBandwidthEntry = _RlIMPBMngRouterBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1)
)
rlIMPBMngRouterBandwidthEntry.setIndexNames(
    (0, "Dlink-IMPB-MNG", "rlIMPBRouterIPAddress"),
)
if mibBuilder.loadTexts:
    rlIMPBMngRouterBandwidthEntry.setStatus("current")
_RlIMPBRouterIPAddress_Type = IpAddress
_RlIMPBRouterIPAddress_Object = MibTableColumn
rlIMPBRouterIPAddress = _RlIMPBRouterIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1, 1),
    _RlIMPBRouterIPAddress_Type()
)
rlIMPBRouterIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIMPBRouterIPAddress.setStatus("current")
_RlIMPBRouterPortlist_Type = PortList
_RlIMPBRouterPortlist_Object = MibTableColumn
rlIMPBRouterPortlist = _RlIMPBRouterPortlist_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1, 2),
    _RlIMPBRouterPortlist_Type()
)
rlIMPBRouterPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIMPBRouterPortlist.setStatus("current")


class _RlIMPBRouterBandwidth_Type(Unsigned32):
    """Custom type rlIMPBRouterBandwidth based on Unsigned32"""
    defaultValue = 0


_RlIMPBRouterBandwidth_Object = MibTableColumn
rlIMPBRouterBandwidth = _RlIMPBRouterBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 4, 1, 3),
    _RlIMPBRouterBandwidth_Type()
)
rlIMPBRouterBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIMPBRouterBandwidth.setStatus("current")


class _RlIMPBMngDiscoveryLearningStatus_Type(Integer32):
    """Custom type rlIMPBMngDiscoveryLearningStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learning", 1),
          ("noLearning", 2))
    )


_RlIMPBMngDiscoveryLearningStatus_Type.__name__ = "Integer32"
_RlIMPBMngDiscoveryLearningStatus_Object = MibScalar
rlIMPBMngDiscoveryLearningStatus = _RlIMPBMngDiscoveryLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 5),
    _RlIMPBMngDiscoveryLearningStatus_Type()
)
rlIMPBMngDiscoveryLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIMPBMngDiscoveryLearningStatus.setStatus("current")
_RlIMPBMngUncheckPorts_Type = PortList
_RlIMPBMngUncheckPorts_Object = MibScalar
rlIMPBMngUncheckPorts = _RlIMPBMngUncheckPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 6),
    _RlIMPBMngUncheckPorts_Type()
)
rlIMPBMngUncheckPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngUncheckPorts.setStatus("current")
_RlIMPBMngLockedStations_Type = Integer32
_RlIMPBMngLockedStations_Object = MibScalar
rlIMPBMngLockedStations = _RlIMPBMngLockedStations_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 7),
    _RlIMPBMngLockedStations_Type()
)
rlIMPBMngLockedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIMPBMngLockedStations.setStatus("current")


class _RlIMPBMngGratARPPeriodTimeout_Type(Unsigned32):
    """Custom type rlIMPBMngGratARPPeriodTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 300),
    )


_RlIMPBMngGratARPPeriodTimeout_Type.__name__ = "Unsigned32"
_RlIMPBMngGratARPPeriodTimeout_Object = MibScalar
rlIMPBMngGratARPPeriodTimeout = _RlIMPBMngGratARPPeriodTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 139, 1, 8),
    _RlIMPBMngGratARPPeriodTimeout_Type()
)
rlIMPBMngGratARPPeriodTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIMPBMngGratARPPeriodTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rlIMPBMngGratARPPeriodTimeout.setUnits("seconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Dlink-IMPB-MNG",
    **{"IMPBPacketType": IMPBPacketType,
       "IMPBLockMode": IMPBLockMode,
       "IMPBDeviceType": IMPBDeviceType,
       "rlIMPBMngTable": rlIMPBMngTable,
       "rlIMPBMngEntry": rlIMPBMngEntry,
       "rlIMPBMngIPAddress": rlIMPBMngIPAddress,
       "rlIMPBMngPacketType": rlIMPBMngPacketType,
       "rlIMPBMngPMACAddress": rlIMPBMngPMACAddress,
       "rlIMPBMngDeviceType": rlIMPBMngDeviceType,
       "rlIMPBMngPortlist": rlIMPBMngPortlist,
       "rlIMPBMngMode": rlIMPBMngMode,
       "rlIMPBMngRouterBandwidth": rlIMPBMngRouterBandwidth,
       "rlIMPBMngRowStatus": rlIMPBMngRowStatus,
       "rlIMPBMngAction": rlIMPBMngAction,
       "rlIMPBMngPortBandwidthTable": rlIMPBMngPortBandwidthTable,
       "rlIMPBMngPortBandwidthEntry": rlIMPBMngPortBandwidthEntry,
       "rlIMPBMngBandwidth": rlIMPBMngBandwidth,
       "rlIMPBMngRouterBandwidthTable": rlIMPBMngRouterBandwidthTable,
       "rlIMPBMngRouterBandwidthEntry": rlIMPBMngRouterBandwidthEntry,
       "rlIMPBRouterIPAddress": rlIMPBRouterIPAddress,
       "rlIMPBRouterPortlist": rlIMPBRouterPortlist,
       "rlIMPBRouterBandwidth": rlIMPBRouterBandwidth,
       "rlIMPBMngDiscoveryLearningStatus": rlIMPBMngDiscoveryLearningStatus,
       "rlIMPBMngUncheckPorts": rlIMPBMngUncheckPorts,
       "rlIMPBMngLockedStations": rlIMPBMngLockedStations,
       "rlIMPBMngGratARPPeriodTimeout": rlIMPBMngGratARPPeriodTimeout}
)
