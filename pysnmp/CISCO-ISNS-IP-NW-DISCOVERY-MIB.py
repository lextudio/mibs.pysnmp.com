# SNMP MIB module (CISCO-ISNS-IP-NW-DISCOVERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ISNS-IP-NW-DISCOVERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:11 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TruthValue")


# MODULE-IDENTITY

ciscoIsnsIpNetDiscoveryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434)
)
ciscoIsnsIpNetDiscoveryMIB.setRevisions(
        ("2004-09-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIsnsIpNetDiscoveryMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIsnsIpNetDiscoveryMIBNotifs = _CiscoIsnsIpNetDiscoveryMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 0)
)
_CiscoIsnsIpNetDiscoveryMIBObjs_ObjectIdentity = ObjectIdentity
ciscoIsnsIpNetDiscoveryMIBObjs = _CiscoIsnsIpNetDiscoveryMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1)
)
_CiscoIsnsIpNetDiscoveryMIBInfo_ObjectIdentity = ObjectIdentity
ciscoIsnsIpNetDiscoveryMIBInfo = _CiscoIsnsIpNetDiscoveryMIBInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1)
)


class _CiscoIsnsIpNetAutomaticDiscovery_Type(TruthValue):
    """Custom type ciscoIsnsIpNetAutomaticDiscovery based on TruthValue"""


_CiscoIsnsIpNetAutomaticDiscovery_Object = MibScalar
ciscoIsnsIpNetAutomaticDiscovery = _CiscoIsnsIpNetAutomaticDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 1),
    _CiscoIsnsIpNetAutomaticDiscovery_Type()
)
ciscoIsnsIpNetAutomaticDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetAutomaticDiscovery.setStatus("current")


class _CiscoIsnsIpNetDiscoveryInterval_Type(Integer32):
    """Custom type ciscoIsnsIpNetDiscoveryInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5184000),
    )


_CiscoIsnsIpNetDiscoveryInterval_Type.__name__ = "Integer32"
_CiscoIsnsIpNetDiscoveryInterval_Object = MibScalar
ciscoIsnsIpNetDiscoveryInterval = _CiscoIsnsIpNetDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 2),
    _CiscoIsnsIpNetDiscoveryInterval_Type()
)
ciscoIsnsIpNetDiscoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryInterval.setStatus("current")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryInterval.setUnits("seconds")
_CiscoIsnsIpNetTable_Object = MibTable
ciscoIsnsIpNetTable = _CiscoIsnsIpNetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoIsnsIpNetTable.setStatus("current")
_CiscoIsnsIpNetEntry_Object = MibTableRow
ciscoIsnsIpNetEntry = _CiscoIsnsIpNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 3, 1)
)
ciscoIsnsIpNetEntry.setIndexNames(
    (0, "CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetName"),
)
if mibBuilder.loadTexts:
    ciscoIsnsIpNetEntry.setStatus("current")


class _CiscoIsnsIpNetName_Type(SnmpAdminString):
    """Custom type ciscoIsnsIpNetName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CiscoIsnsIpNetName_Type.__name__ = "SnmpAdminString"
_CiscoIsnsIpNetName_Object = MibTableColumn
ciscoIsnsIpNetName = _CiscoIsnsIpNetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 3, 1, 1),
    _CiscoIsnsIpNetName_Type()
)
ciscoIsnsIpNetName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetName.setStatus("current")


class _CiscoIsnsIpNetDiscoveryMechanism_Type(Integer32):
    """Custom type ciscoIsnsIpNetDiscoveryMechanism based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoGenerated", 1),
          ("userConfigured", 2))
    )


_CiscoIsnsIpNetDiscoveryMechanism_Type.__name__ = "Integer32"
_CiscoIsnsIpNetDiscoveryMechanism_Object = MibTableColumn
ciscoIsnsIpNetDiscoveryMechanism = _CiscoIsnsIpNetDiscoveryMechanism_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 3, 1, 2),
    _CiscoIsnsIpNetDiscoveryMechanism_Type()
)
ciscoIsnsIpNetDiscoveryMechanism.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryMechanism.setStatus("current")
_CiscoIsnsIpNetRowStatus_Type = RowStatus
_CiscoIsnsIpNetRowStatus_Object = MibTableColumn
ciscoIsnsIpNetRowStatus = _CiscoIsnsIpNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 3, 1, 3),
    _CiscoIsnsIpNetRowStatus_Type()
)
ciscoIsnsIpNetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetRowStatus.setStatus("current")
_CiscoIsnsIpNetInterfaceTable_Object = MibTable
ciscoIsnsIpNetInterfaceTable = _CiscoIsnsIpNetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoIsnsIpNetInterfaceTable.setStatus("current")
_CiscoIsnsIpNetInterfaceEntry_Object = MibTableRow
ciscoIsnsIpNetInterfaceEntry = _CiscoIsnsIpNetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 4, 1)
)
ciscoIsnsIpNetInterfaceEntry.setIndexNames(
    (0, "CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetName"),
    (0, "CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsGigEPortDeviceName"),
    (0, "CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsGigEPortIfIndex"),
)
if mibBuilder.loadTexts:
    ciscoIsnsIpNetInterfaceEntry.setStatus("current")
_CiscoIsnsGigEPortDeviceName_Type = FcNameId
_CiscoIsnsGigEPortDeviceName_Object = MibTableColumn
ciscoIsnsGigEPortDeviceName = _CiscoIsnsGigEPortDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 4, 1, 1),
    _CiscoIsnsGigEPortDeviceName_Type()
)
ciscoIsnsGigEPortDeviceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoIsnsGigEPortDeviceName.setStatus("current")
_CiscoIsnsGigEPortIfIndex_Type = InterfaceIndex
_CiscoIsnsGigEPortIfIndex_Object = MibTableColumn
ciscoIsnsGigEPortIfIndex = _CiscoIsnsGigEPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 4, 1, 2),
    _CiscoIsnsGigEPortIfIndex_Type()
)
ciscoIsnsGigEPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoIsnsGigEPortIfIndex.setStatus("current")
_CiscoIsnsIpNetInterfaceRowStatus_Type = RowStatus
_CiscoIsnsIpNetInterfaceRowStatus_Object = MibTableColumn
ciscoIsnsIpNetInterfaceRowStatus = _CiscoIsnsIpNetInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 1, 4, 1, 3),
    _CiscoIsnsIpNetInterfaceRowStatus_Type()
)
ciscoIsnsIpNetInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetInterfaceRowStatus.setStatus("current")
_CiscoIsnsIpNetDiscoveryMIBConfig_ObjectIdentity = ObjectIdentity
ciscoIsnsIpNetDiscoveryMIBConfig = _CiscoIsnsIpNetDiscoveryMIBConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2)
)
_CiscoIsnsIpNetDiscoverySpinLock_Type = TestAndIncr
_CiscoIsnsIpNetDiscoverySpinLock_Object = MibScalar
ciscoIsnsIpNetDiscoverySpinLock = _CiscoIsnsIpNetDiscoverySpinLock_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 1),
    _CiscoIsnsIpNetDiscoverySpinLock_Type()
)
ciscoIsnsIpNetDiscoverySpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoverySpinLock.setStatus("current")


class _CiscoIsnsIpNetToDiscover_Type(SnmpAdminString):
    """Custom type ciscoIsnsIpNetToDiscover based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CiscoIsnsIpNetToDiscover_Type.__name__ = "SnmpAdminString"
_CiscoIsnsIpNetToDiscover_Object = MibScalar
ciscoIsnsIpNetToDiscover = _CiscoIsnsIpNetToDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 2),
    _CiscoIsnsIpNetToDiscover_Type()
)
ciscoIsnsIpNetToDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetToDiscover.setStatus("current")


class _CiscoIsnsGigEInterfaceToDiscover_Type(InterfaceIndexOrZero):
    """Custom type ciscoIsnsGigEInterfaceToDiscover based on InterfaceIndexOrZero"""
    defaultValue = 0


_CiscoIsnsGigEInterfaceToDiscover_Object = MibScalar
ciscoIsnsGigEInterfaceToDiscover = _CiscoIsnsGigEInterfaceToDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 3),
    _CiscoIsnsGigEInterfaceToDiscover_Type()
)
ciscoIsnsGigEInterfaceToDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoIsnsGigEInterfaceToDiscover.setStatus("current")


class _CiscoIsnsIpNetDiscoveryCommand_Type(Integer32):
    """Custom type ciscoIsnsIpNetDiscoveryCommand based on Integer32"""
    defaultValue = 2

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
        *(("all", 1),
          ("interfaceSpecific", 4),
          ("ipNetworkSpecific", 3),
          ("noOp", 2))
    )


_CiscoIsnsIpNetDiscoveryCommand_Type.__name__ = "Integer32"
_CiscoIsnsIpNetDiscoveryCommand_Object = MibScalar
ciscoIsnsIpNetDiscoveryCommand = _CiscoIsnsIpNetDiscoveryCommand_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 4),
    _CiscoIsnsIpNetDiscoveryCommand_Type()
)
ciscoIsnsIpNetDiscoveryCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryCommand.setStatus("current")


class _CiscoIsnsIpNetDiscoveryCmdStatus_Type(Integer32):
    """Custom type ciscoIsnsIpNetDiscoveryCmdStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("generalFailure", 8),
          ("inProgress", 3),
          ("invalidGigEInterfaceIndex", 7),
          ("invalidIpNetworkName", 5),
          ("noGigEInterfaceIndexSpecified", 6),
          ("noIpNetworkNameSpecified", 4),
          ("none", 2),
          ("success", 1))
    )


_CiscoIsnsIpNetDiscoveryCmdStatus_Type.__name__ = "Integer32"
_CiscoIsnsIpNetDiscoveryCmdStatus_Object = MibScalar
ciscoIsnsIpNetDiscoveryCmdStatus = _CiscoIsnsIpNetDiscoveryCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 1, 2, 5),
    _CiscoIsnsIpNetDiscoveryCmdStatus_Type()
)
ciscoIsnsIpNetDiscoveryCmdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryCmdStatus.setStatus("current")
_CiscoIsnsIpNetDiscoveryConform_ObjectIdentity = ObjectIdentity
ciscoIsnsIpNetDiscoveryConform = _CiscoIsnsIpNetDiscoveryConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2)
)
_CiscoIsnsIpNetDiscoverCompliance_ObjectIdentity = ObjectIdentity
ciscoIsnsIpNetDiscoverCompliance = _CiscoIsnsIpNetDiscoverCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 1)
)
_CiscoIsnsIpNetDiscoveryMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIsnsIpNetDiscoveryMIBGroups = _CiscoIsnsIpNetDiscoveryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2)
)

# Managed Objects groups

ciscoIsnsIpNetDiscoveryInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2, 1)
)
ciscoIsnsIpNetDiscoveryInfoGroup.setObjects(
      *(("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetAutomaticDiscovery"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetDiscoveryInterval"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetDiscoveryMechanism"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetRowStatus"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetInterfaceRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryInfoGroup.setStatus("current")

ciscoIsnsIpNetDiscoveryCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 2, 2)
)
ciscoIsnsIpNetDiscoveryCfgGroup.setObjects(
      *(("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetDiscoverySpinLock"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetToDiscover"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsGigEInterfaceToDiscover"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetDiscoveryCommand"),
        ("CISCO-ISNS-IP-NW-DISCOVERY-MIB", "ciscoIsnsIpNetDiscoveryCmdStatus"))
)
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIsnsIpNetDiscoveryMIBComp = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 434, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIsnsIpNetDiscoveryMIBComp.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ISNS-IP-NW-DISCOVERY-MIB",
    **{"ciscoIsnsIpNetDiscoveryMIB": ciscoIsnsIpNetDiscoveryMIB,
       "ciscoIsnsIpNetDiscoveryMIBNotifs": ciscoIsnsIpNetDiscoveryMIBNotifs,
       "ciscoIsnsIpNetDiscoveryMIBObjs": ciscoIsnsIpNetDiscoveryMIBObjs,
       "ciscoIsnsIpNetDiscoveryMIBInfo": ciscoIsnsIpNetDiscoveryMIBInfo,
       "ciscoIsnsIpNetAutomaticDiscovery": ciscoIsnsIpNetAutomaticDiscovery,
       "ciscoIsnsIpNetDiscoveryInterval": ciscoIsnsIpNetDiscoveryInterval,
       "ciscoIsnsIpNetTable": ciscoIsnsIpNetTable,
       "ciscoIsnsIpNetEntry": ciscoIsnsIpNetEntry,
       "ciscoIsnsIpNetName": ciscoIsnsIpNetName,
       "ciscoIsnsIpNetDiscoveryMechanism": ciscoIsnsIpNetDiscoveryMechanism,
       "ciscoIsnsIpNetRowStatus": ciscoIsnsIpNetRowStatus,
       "ciscoIsnsIpNetInterfaceTable": ciscoIsnsIpNetInterfaceTable,
       "ciscoIsnsIpNetInterfaceEntry": ciscoIsnsIpNetInterfaceEntry,
       "ciscoIsnsGigEPortDeviceName": ciscoIsnsGigEPortDeviceName,
       "ciscoIsnsGigEPortIfIndex": ciscoIsnsGigEPortIfIndex,
       "ciscoIsnsIpNetInterfaceRowStatus": ciscoIsnsIpNetInterfaceRowStatus,
       "ciscoIsnsIpNetDiscoveryMIBConfig": ciscoIsnsIpNetDiscoveryMIBConfig,
       "ciscoIsnsIpNetDiscoverySpinLock": ciscoIsnsIpNetDiscoverySpinLock,
       "ciscoIsnsIpNetToDiscover": ciscoIsnsIpNetToDiscover,
       "ciscoIsnsGigEInterfaceToDiscover": ciscoIsnsGigEInterfaceToDiscover,
       "ciscoIsnsIpNetDiscoveryCommand": ciscoIsnsIpNetDiscoveryCommand,
       "ciscoIsnsIpNetDiscoveryCmdStatus": ciscoIsnsIpNetDiscoveryCmdStatus,
       "ciscoIsnsIpNetDiscoveryConform": ciscoIsnsIpNetDiscoveryConform,
       "ciscoIsnsIpNetDiscoverCompliance": ciscoIsnsIpNetDiscoverCompliance,
       "ciscoIsnsIpNetDiscoveryMIBComp": ciscoIsnsIpNetDiscoveryMIBComp,
       "ciscoIsnsIpNetDiscoveryMIBGroups": ciscoIsnsIpNetDiscoveryMIBGroups,
       "ciscoIsnsIpNetDiscoveryInfoGroup": ciscoIsnsIpNetDiscoveryInfoGroup,
       "ciscoIsnsIpNetDiscoveryCfgGroup": ciscoIsnsIpNetDiscoveryCfgGroup}
)
