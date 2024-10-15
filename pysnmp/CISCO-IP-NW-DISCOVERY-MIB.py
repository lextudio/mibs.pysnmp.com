# SNMP MIB module (CISCO-IP-NW-DISCOVERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IP-NW-DISCOVERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:41 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcNameId,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DisplayString,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

ciscoIpNetworkDiscoveryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434)
)
ciscoIpNetworkDiscoveryMIB.setRevisions(
        ("2006-10-03 00:00",
         "2005-08-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CIpNetworkDiscoveryMIBNotifs_ObjectIdentity = ObjectIdentity
cIpNetworkDiscoveryMIBNotifs = _CIpNetworkDiscoveryMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 0)
)
_CIpNetworkDiscoveryMIBObjs_ObjectIdentity = ObjectIdentity
cIpNetworkDiscoveryMIBObjs = _CIpNetworkDiscoveryMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1)
)
_CIpNetworkDiscoveryConfig_ObjectIdentity = ObjectIdentity
cIpNetworkDiscoveryConfig = _CIpNetworkDiscoveryConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1)
)


class _CIpNetworkAutomaticDiscovery_Type(TruthValue):
    """Custom type cIpNetworkAutomaticDiscovery based on TruthValue"""


_CIpNetworkAutomaticDiscovery_Object = MibScalar
cIpNetworkAutomaticDiscovery = _CIpNetworkAutomaticDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 1),
    _CIpNetworkAutomaticDiscovery_Type()
)
cIpNetworkAutomaticDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkAutomaticDiscovery.setStatus("current")


class _CIpNetworkDiscoveryDelay_Type(Integer32):
    """Custom type cIpNetworkDiscoveryDelay based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5184000),
    )


_CIpNetworkDiscoveryDelay_Type.__name__ = "Integer32"
_CIpNetworkDiscoveryDelay_Object = MibScalar
cIpNetworkDiscoveryDelay = _CIpNetworkDiscoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 2),
    _CIpNetworkDiscoveryDelay_Type()
)
cIpNetworkDiscoveryDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryDelay.setUnits("seconds")
_CIpNetworkDiscoveryTypeSpinLock_Type = TestAndIncr
_CIpNetworkDiscoveryTypeSpinLock_Object = MibScalar
cIpNetworkDiscoveryTypeSpinLock = _CIpNetworkDiscoveryTypeSpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 3),
    _CIpNetworkDiscoveryTypeSpinLock_Type()
)
cIpNetworkDiscoveryTypeSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryTypeSpinLock.setStatus("current")


class _CIpNetworkDiscoveryType_Type(Integer32):
    """Custom type cIpNetworkDiscoveryType based on Integer32"""
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
        *(("icmp", 1),
          ("tcp", 2),
          ("udp", 3))
    )


_CIpNetworkDiscoveryType_Type.__name__ = "Integer32"
_CIpNetworkDiscoveryType_Object = MibScalar
cIpNetworkDiscoveryType = _CIpNetworkDiscoveryType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 4),
    _CIpNetworkDiscoveryType_Type()
)
cIpNetworkDiscoveryType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryType.setStatus("current")
_CIpNetworkDiscoveryPort_Type = InetPortNumber
_CIpNetworkDiscoveryPort_Object = MibScalar
cIpNetworkDiscoveryPort = _CIpNetworkDiscoveryPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 5),
    _CIpNetworkDiscoveryPort_Type()
)
cIpNetworkDiscoveryPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryPort.setStatus("current")
_CIpNetworkDiscoverySpinLock_Type = TestAndIncr
_CIpNetworkDiscoverySpinLock_Object = MibScalar
cIpNetworkDiscoverySpinLock = _CIpNetworkDiscoverySpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 6),
    _CIpNetworkDiscoverySpinLock_Type()
)
cIpNetworkDiscoverySpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkDiscoverySpinLock.setStatus("current")
_CIpNetworkGigEIfIndexToDiscover_Type = InterfaceIndexOrZero
_CIpNetworkGigEIfIndexToDiscover_Object = MibScalar
cIpNetworkGigEIfIndexToDiscover = _CIpNetworkGigEIfIndexToDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 7),
    _CIpNetworkGigEIfIndexToDiscover_Type()
)
cIpNetworkGigEIfIndexToDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkGigEIfIndexToDiscover.setStatus("current")


class _CIpNetworkInetAddrTypeToDiscover_Type(InetAddressType):
    """Custom type cIpNetworkInetAddrTypeToDiscover based on InetAddressType"""


_CIpNetworkInetAddrTypeToDiscover_Object = MibScalar
cIpNetworkInetAddrTypeToDiscover = _CIpNetworkInetAddrTypeToDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 8),
    _CIpNetworkInetAddrTypeToDiscover_Type()
)
cIpNetworkInetAddrTypeToDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkInetAddrTypeToDiscover.setStatus("current")
_CIpNetworkGigEInetAddrToDiscover_Type = InetAddress
_CIpNetworkGigEInetAddrToDiscover_Object = MibScalar
cIpNetworkGigEInetAddrToDiscover = _CIpNetworkGigEInetAddrToDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 9),
    _CIpNetworkGigEInetAddrToDiscover_Type()
)
cIpNetworkGigEInetAddrToDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkGigEInetAddrToDiscover.setStatus("current")


class _CIpNetworkDiscoveryCommand_Type(Integer32):
    """Custom type cIpNetworkDiscoveryCommand based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("interfaceSpecific", 3),
          ("noOp", 2))
    )


_CIpNetworkDiscoveryCommand_Type.__name__ = "Integer32"
_CIpNetworkDiscoveryCommand_Object = MibScalar
cIpNetworkDiscoveryCommand = _CIpNetworkDiscoveryCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 10),
    _CIpNetworkDiscoveryCommand_Type()
)
cIpNetworkDiscoveryCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryCommand.setStatus("current")


class _CIpNetworkDiscoveryCmdStatus_Type(Integer32):
    """Custom type cIpNetworkDiscoveryCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("generalFailure", 10),
          ("inProgress", 3),
          ("invalidGigEInetAddr", 9),
          ("invalidGigEInetAddrType", 8),
          ("invalidGigEInterfaceIndex", 7),
          ("noGigEInetAddrSpecified", 5),
          ("noGigEInterfaceIndexSpecified", 4),
          ("noGigESwitchWWNSpecified", 6),
          ("none", 2),
          ("success", 1))
    )


_CIpNetworkDiscoveryCmdStatus_Type.__name__ = "Integer32"
_CIpNetworkDiscoveryCmdStatus_Object = MibScalar
cIpNetworkDiscoveryCmdStatus = _CIpNetworkDiscoveryCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 11),
    _CIpNetworkDiscoveryCmdStatus_Type()
)
cIpNetworkDiscoveryCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryCmdStatus.setStatus("current")
_CIpNetworkDiscoveryInfo_ObjectIdentity = ObjectIdentity
cIpNetworkDiscoveryInfo = _CIpNetworkDiscoveryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2)
)
_CIpNetworkTable_Object = MibTable
cIpNetworkTable = _CIpNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIpNetworkTable.setStatus("current")
_CIpNetworkEntry_Object = MibTableRow
cIpNetworkEntry = _CIpNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1, 1)
)
cIpNetworkEntry.setIndexNames(
    (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkIndex"),
)
if mibBuilder.loadTexts:
    cIpNetworkEntry.setStatus("current")


class _CIpNetworkIndex_Type(Integer32):
    """Custom type cIpNetworkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIpNetworkIndex_Type.__name__ = "Integer32"
_CIpNetworkIndex_Object = MibTableColumn
cIpNetworkIndex = _CIpNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1, 1, 1),
    _CIpNetworkIndex_Type()
)
cIpNetworkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpNetworkIndex.setStatus("current")
_CIpNetworkSwitchWWN_Type = FcNameId
_CIpNetworkSwitchWWN_Object = MibTableColumn
cIpNetworkSwitchWWN = _CIpNetworkSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1, 1, 2),
    _CIpNetworkSwitchWWN_Type()
)
cIpNetworkSwitchWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetworkSwitchWWN.setStatus("current")
_CIpNetworkInterfaceTable_Object = MibTable
cIpNetworkInterfaceTable = _CIpNetworkInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cIpNetworkInterfaceTable.setStatus("current")
_CIpNetworkInterfaceEntry_Object = MibTableRow
cIpNetworkInterfaceEntry = _CIpNetworkInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1)
)
cIpNetworkInterfaceEntry.setIndexNames(
    (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkIndex"),
    (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortSwitchWWN"),
    (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortIfIndex"),
    (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortInetAddrType"),
    (0, "CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortInetAddr"),
)
if mibBuilder.loadTexts:
    cIpNetworkInterfaceEntry.setStatus("current")


class _CIpNetworkGigEPortSwitchWWN_Type(FcNameId):
    """Custom type cIpNetworkGigEPortSwitchWWN based on FcNameId"""
    subtypeSpec = FcNameId.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_CIpNetworkGigEPortSwitchWWN_Type.__name__ = "FcNameId"
_CIpNetworkGigEPortSwitchWWN_Object = MibTableColumn
cIpNetworkGigEPortSwitchWWN = _CIpNetworkGigEPortSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 1),
    _CIpNetworkGigEPortSwitchWWN_Type()
)
cIpNetworkGigEPortSwitchWWN.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpNetworkGigEPortSwitchWWN.setStatus("current")
_CIpNetworkGigEPortIfIndex_Type = InterfaceIndex
_CIpNetworkGigEPortIfIndex_Object = MibTableColumn
cIpNetworkGigEPortIfIndex = _CIpNetworkGigEPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 2),
    _CIpNetworkGigEPortIfIndex_Type()
)
cIpNetworkGigEPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpNetworkGigEPortIfIndex.setStatus("current")
_CIpNetworkGigEPortInetAddrType_Type = InetAddressType
_CIpNetworkGigEPortInetAddrType_Object = MibTableColumn
cIpNetworkGigEPortInetAddrType = _CIpNetworkGigEPortInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 3),
    _CIpNetworkGigEPortInetAddrType_Type()
)
cIpNetworkGigEPortInetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIpNetworkGigEPortInetAddrType.setStatus("current")


class _CIpNetworkGigEPortInetAddr_Type(InetAddress):
    """Custom type cIpNetworkGigEPortInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CIpNetworkGigEPortInetAddr_Type.__name__ = "InetAddress"
_CIpNetworkGigEPortInetAddr_Object = MibTableColumn
cIpNetworkGigEPortInetAddr = _CIpNetworkGigEPortInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2, 1, 4),
    _CIpNetworkGigEPortInetAddr_Type()
)
cIpNetworkGigEPortInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIpNetworkGigEPortInetAddr.setStatus("current")
_CIpNetworkDiscoveryConform_ObjectIdentity = ObjectIdentity
cIpNetworkDiscoveryConform = _CIpNetworkDiscoveryConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2)
)
_CIpNetworkDiscoverCompliance_ObjectIdentity = ObjectIdentity
cIpNetworkDiscoverCompliance = _CIpNetworkDiscoverCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 1)
)
_CIpNetworkDiscoveryMIBGroups_ObjectIdentity = ObjectIdentity
cIpNetworkDiscoveryMIBGroups = _CIpNetworkDiscoveryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2)
)

# Managed Objects groups

cIpNetworkDiscoveryInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2, 1)
)
cIpNetworkDiscoveryInfoGroup.setObjects(
      *(("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkSwitchWWN"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEPortInetAddr"))
)
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryInfoGroup.setStatus("current")

cIpNetworkDiscoveryCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2, 2)
)
cIpNetworkDiscoveryCfgGroup.setObjects(
      *(("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkAutomaticDiscovery"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryDelay"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryTypeSpinLock"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryType"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryPort"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoverySpinLock"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEIfIndexToDiscover"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkInetAddrTypeToDiscover"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkGigEInetAddrToDiscover"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryCommand"),
        ("CISCO-IP-NW-DISCOVERY-MIB", "cIpNetworkDiscoveryCmdStatus"))
)
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cIpNetworkDiscoveryMIBComp = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cIpNetworkDiscoveryMIBComp.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IP-NW-DISCOVERY-MIB",
    **{"ciscoIpNetworkDiscoveryMIB": ciscoIpNetworkDiscoveryMIB,
       "cIpNetworkDiscoveryMIBNotifs": cIpNetworkDiscoveryMIBNotifs,
       "cIpNetworkDiscoveryMIBObjs": cIpNetworkDiscoveryMIBObjs,
       "cIpNetworkDiscoveryConfig": cIpNetworkDiscoveryConfig,
       "cIpNetworkAutomaticDiscovery": cIpNetworkAutomaticDiscovery,
       "cIpNetworkDiscoveryDelay": cIpNetworkDiscoveryDelay,
       "cIpNetworkDiscoveryTypeSpinLock": cIpNetworkDiscoveryTypeSpinLock,
       "cIpNetworkDiscoveryType": cIpNetworkDiscoveryType,
       "cIpNetworkDiscoveryPort": cIpNetworkDiscoveryPort,
       "cIpNetworkDiscoverySpinLock": cIpNetworkDiscoverySpinLock,
       "cIpNetworkGigEIfIndexToDiscover": cIpNetworkGigEIfIndexToDiscover,
       "cIpNetworkInetAddrTypeToDiscover": cIpNetworkInetAddrTypeToDiscover,
       "cIpNetworkGigEInetAddrToDiscover": cIpNetworkGigEInetAddrToDiscover,
       "cIpNetworkDiscoveryCommand": cIpNetworkDiscoveryCommand,
       "cIpNetworkDiscoveryCmdStatus": cIpNetworkDiscoveryCmdStatus,
       "cIpNetworkDiscoveryInfo": cIpNetworkDiscoveryInfo,
       "cIpNetworkTable": cIpNetworkTable,
       "cIpNetworkEntry": cIpNetworkEntry,
       "cIpNetworkIndex": cIpNetworkIndex,
       "cIpNetworkSwitchWWN": cIpNetworkSwitchWWN,
       "cIpNetworkInterfaceTable": cIpNetworkInterfaceTable,
       "cIpNetworkInterfaceEntry": cIpNetworkInterfaceEntry,
       "cIpNetworkGigEPortSwitchWWN": cIpNetworkGigEPortSwitchWWN,
       "cIpNetworkGigEPortIfIndex": cIpNetworkGigEPortIfIndex,
       "cIpNetworkGigEPortInetAddrType": cIpNetworkGigEPortInetAddrType,
       "cIpNetworkGigEPortInetAddr": cIpNetworkGigEPortInetAddr,
       "cIpNetworkDiscoveryConform": cIpNetworkDiscoveryConform,
       "cIpNetworkDiscoverCompliance": cIpNetworkDiscoverCompliance,
       "cIpNetworkDiscoveryMIBComp": cIpNetworkDiscoveryMIBComp,
       "cIpNetworkDiscoveryMIBGroups": cIpNetworkDiscoveryMIBGroups,
       "cIpNetworkDiscoveryInfoGroup": cIpNetworkDiscoveryInfoGroup,
       "cIpNetworkDiscoveryCfgGroup": cIpNetworkDiscoveryCfgGroup}
)
