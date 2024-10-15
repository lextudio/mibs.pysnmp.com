# SNMP MIB module (REDSTONE-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:47 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rsSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16)
)
rsSnmpMIB.setRevisions(
        ("1999-07-27 00:00",
         "1998-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsSnmpCommunityName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class RsSnmpTrapMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_RsSnmpObjects_ObjectIdentity = ObjectIdentity
rsSnmpObjects = _RsSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1)
)
_RsSnmpGeneral_ObjectIdentity = ObjectIdentity
rsSnmpGeneral = _RsSnmpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 1)
)


class _RsSnmpMaxPduSize_Type(Integer32):
    """Custom type rsSnmpMaxPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 8192),
    )


_RsSnmpMaxPduSize_Type.__name__ = "Integer32"
_RsSnmpMaxPduSize_Object = MibScalar
rsSnmpMaxPduSize = _RsSnmpMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 1, 1),
    _RsSnmpMaxPduSize_Type()
)
rsSnmpMaxPduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSnmpMaxPduSize.setStatus("current")
_RsSnmpCommunity_ObjectIdentity = ObjectIdentity
rsSnmpCommunity = _RsSnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 2)
)
_RsSnmpCommunityTable_Object = MibTable
rsSnmpCommunityTable = _RsSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rsSnmpCommunityTable.setStatus("current")
_RsSnmpCommunityEntry_Object = MibTableRow
rsSnmpCommunityEntry = _RsSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 2, 1, 1)
)
rsSnmpCommunityEntry.setIndexNames(
    (1, "REDSTONE-SNMP-MIB", "rsSnmpCommunityName"),
)
if mibBuilder.loadTexts:
    rsSnmpCommunityEntry.setStatus("current")
_RsSnmpCommunityName_Type = RsSnmpCommunityName
_RsSnmpCommunityName_Object = MibTableColumn
rsSnmpCommunityName = _RsSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 2, 1, 1, 1),
    _RsSnmpCommunityName_Type()
)
rsSnmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpCommunityName.setStatus("current")
_RsSnmpCommunityRowStatus_Type = RowStatus
_RsSnmpCommunityRowStatus_Object = MibTableColumn
rsSnmpCommunityRowStatus = _RsSnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 2, 1, 1, 2),
    _RsSnmpCommunityRowStatus_Type()
)
rsSnmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpCommunityRowStatus.setStatus("current")


class _RsSnmpCommunityPrivilege_Type(Integer32):
    """Custom type rsSnmpCommunityPrivilege based on Integer32"""
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
        *(("admin", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_RsSnmpCommunityPrivilege_Type.__name__ = "Integer32"
_RsSnmpCommunityPrivilege_Object = MibTableColumn
rsSnmpCommunityPrivilege = _RsSnmpCommunityPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 2, 1, 1, 3),
    _RsSnmpCommunityPrivilege_Type()
)
rsSnmpCommunityPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpCommunityPrivilege.setStatus("current")


class _RsSnmpCommunityAccessList_Type(Integer32):
    """Custom type rsSnmpCommunityAccessList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_RsSnmpCommunityAccessList_Type.__name__ = "Integer32"
_RsSnmpCommunityAccessList_Object = MibTableColumn
rsSnmpCommunityAccessList = _RsSnmpCommunityAccessList_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 2, 1, 1, 4),
    _RsSnmpCommunityAccessList_Type()
)
rsSnmpCommunityAccessList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpCommunityAccessList.setStatus("current")
_RsSnmpTrap_ObjectIdentity = ObjectIdentity
rsSnmpTrap = _RsSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3)
)
_RsSnmpTrapGlobalFilter_Type = RsSnmpTrapMask
_RsSnmpTrapGlobalFilter_Object = MibScalar
rsSnmpTrapGlobalFilter = _RsSnmpTrapGlobalFilter_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 1),
    _RsSnmpTrapGlobalFilter_Type()
)
rsSnmpTrapGlobalFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSnmpTrapGlobalFilter.setStatus("current")


class _RsSnmpTrapSource_Type(Integer32):
    """Custom type rsSnmpTrapSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsSnmpTrapSource_Type.__name__ = "Integer32"
_RsSnmpTrapSource_Object = MibScalar
rsSnmpTrapSource = _RsSnmpTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 2),
    _RsSnmpTrapSource_Type()
)
rsSnmpTrapSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsSnmpTrapSource.setStatus("current")
_RsSnmpTrapHostTable_Object = MibTable
rsSnmpTrapHostTable = _RsSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3)
)
if mibBuilder.loadTexts:
    rsSnmpTrapHostTable.setStatus("current")
_RsSnmpTrapHostEntry_Object = MibTableRow
rsSnmpTrapHostEntry = _RsSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1)
)
rsSnmpTrapHostEntry.setIndexNames(
    (0, "REDSTONE-SNMP-MIB", "rsSnmpTrapHostIpAddress"),
)
if mibBuilder.loadTexts:
    rsSnmpTrapHostEntry.setStatus("current")
_RsSnmpTrapHostIpAddress_Type = IpAddress
_RsSnmpTrapHostIpAddress_Object = MibTableColumn
rsSnmpTrapHostIpAddress = _RsSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1, 1),
    _RsSnmpTrapHostIpAddress_Type()
)
rsSnmpTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpTrapHostIpAddress.setStatus("current")
_RsSnmpTrapHostRowStatus_Type = RowStatus
_RsSnmpTrapHostRowStatus_Object = MibTableColumn
rsSnmpTrapHostRowStatus = _RsSnmpTrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1, 2),
    _RsSnmpTrapHostRowStatus_Type()
)
rsSnmpTrapHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpTrapHostRowStatus.setStatus("current")


class _RsSnmpTrapHostUdpPort_Type(Integer32):
    """Custom type rsSnmpTrapHostUdpPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RsSnmpTrapHostUdpPort_Type.__name__ = "Integer32"
_RsSnmpTrapHostUdpPort_Object = MibTableColumn
rsSnmpTrapHostUdpPort = _RsSnmpTrapHostUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1, 3),
    _RsSnmpTrapHostUdpPort_Type()
)
rsSnmpTrapHostUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpTrapHostUdpPort.setStatus("current")
_RsSnmpTrapHostCommunity_Type = RsSnmpCommunityName
_RsSnmpTrapHostCommunity_Object = MibTableColumn
rsSnmpTrapHostCommunity = _RsSnmpTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1, 4),
    _RsSnmpTrapHostCommunity_Type()
)
rsSnmpTrapHostCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpTrapHostCommunity.setStatus("current")


class _RsSnmpTrapHostProtocolVersion_Type(Integer32):
    """Custom type rsSnmpTrapHostProtocolVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1))
    )


_RsSnmpTrapHostProtocolVersion_Type.__name__ = "Integer32"
_RsSnmpTrapHostProtocolVersion_Object = MibTableColumn
rsSnmpTrapHostProtocolVersion = _RsSnmpTrapHostProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1, 5),
    _RsSnmpTrapHostProtocolVersion_Type()
)
rsSnmpTrapHostProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpTrapHostProtocolVersion.setStatus("current")
_RsSnmpTrapHostFilter_Type = RsSnmpTrapMask
_RsSnmpTrapHostFilter_Object = MibTableColumn
rsSnmpTrapHostFilter = _RsSnmpTrapHostFilter_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1, 6),
    _RsSnmpTrapHostFilter_Type()
)
rsSnmpTrapHostFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsSnmpTrapHostFilter.setStatus("current")
_RsSnmpTrapHostSends_Type = Counter32
_RsSnmpTrapHostSends_Object = MibTableColumn
rsSnmpTrapHostSends = _RsSnmpTrapHostSends_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 3, 3, 1, 7),
    _RsSnmpTrapHostSends_Type()
)
rsSnmpTrapHostSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSnmpTrapHostSends.setStatus("current")
_RsSnmpAuthFailId_ObjectIdentity = ObjectIdentity
rsSnmpAuthFailId = _RsSnmpAuthFailId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 4)
)
_RsSnmpAuthFailIdIpAddress_Type = IpAddress
_RsSnmpAuthFailIdIpAddress_Object = MibScalar
rsSnmpAuthFailIdIpAddress = _RsSnmpAuthFailIdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 4, 1),
    _RsSnmpAuthFailIdIpAddress_Type()
)
rsSnmpAuthFailIdIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rsSnmpAuthFailIdIpAddress.setStatus("current")
_RsSnmpAuthFailIdUdpPort_Type = Integer32
_RsSnmpAuthFailIdUdpPort_Object = MibScalar
rsSnmpAuthFailIdUdpPort = _RsSnmpAuthFailIdUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 4, 2),
    _RsSnmpAuthFailIdUdpPort_Type()
)
rsSnmpAuthFailIdUdpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rsSnmpAuthFailIdUdpPort.setStatus("current")
_RsSnmpAuthFailIdCommunity_Type = OctetString
_RsSnmpAuthFailIdCommunity_Object = MibScalar
rsSnmpAuthFailIdCommunity = _RsSnmpAuthFailIdCommunity_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 4, 3),
    _RsSnmpAuthFailIdCommunity_Type()
)
rsSnmpAuthFailIdCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rsSnmpAuthFailIdCommunity.setStatus("current")


class _RsSnmpAuthFailIdReason_Type(Integer32):
    """Custom type rsSnmpAuthFailIdReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("badCommmunityUse", 2),
          ("badCommunityName", 1),
          ("hostDenied", 3),
          ("other", 0))
    )


_RsSnmpAuthFailIdReason_Type.__name__ = "Integer32"
_RsSnmpAuthFailIdReason_Object = MibScalar
rsSnmpAuthFailIdReason = _RsSnmpAuthFailIdReason_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 1, 4, 4),
    _RsSnmpAuthFailIdReason_Type()
)
rsSnmpAuthFailIdReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rsSnmpAuthFailIdReason.setStatus("current")
_RsSnmpConformance_ObjectIdentity = ObjectIdentity
rsSnmpConformance = _RsSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 2)
)
_RsSnmpCompliances_ObjectIdentity = ObjectIdentity
rsSnmpCompliances = _RsSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 2, 1)
)
_RsSnmpGroups_ObjectIdentity = ObjectIdentity
rsSnmpGroups = _RsSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 2, 2)
)

# Managed Objects groups

rsSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 2, 2, 1)
)
rsSnmpGroup.setObjects(
      *(("REDSTONE-SNMP-MIB", "rsSnmpMaxPduSize"),
        ("REDSTONE-SNMP-MIB", "rsSnmpCommunityName"),
        ("REDSTONE-SNMP-MIB", "rsSnmpCommunityRowStatus"),
        ("REDSTONE-SNMP-MIB", "rsSnmpCommunityPrivilege"),
        ("REDSTONE-SNMP-MIB", "rsSnmpCommunityAccessList"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapGlobalFilter"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapSource"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapHostRowStatus"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapHostUdpPort"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapHostCommunity"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapHostProtocolVersion"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapHostFilter"),
        ("REDSTONE-SNMP-MIB", "rsSnmpTrapHostSends"))
)
if mibBuilder.loadTexts:
    rsSnmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsSnmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rsSnmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-SNMP-MIB",
    **{"RsSnmpCommunityName": RsSnmpCommunityName,
       "RsSnmpTrapMask": RsSnmpTrapMask,
       "rsSnmpMIB": rsSnmpMIB,
       "rsSnmpObjects": rsSnmpObjects,
       "rsSnmpGeneral": rsSnmpGeneral,
       "rsSnmpMaxPduSize": rsSnmpMaxPduSize,
       "rsSnmpCommunity": rsSnmpCommunity,
       "rsSnmpCommunityTable": rsSnmpCommunityTable,
       "rsSnmpCommunityEntry": rsSnmpCommunityEntry,
       "rsSnmpCommunityName": rsSnmpCommunityName,
       "rsSnmpCommunityRowStatus": rsSnmpCommunityRowStatus,
       "rsSnmpCommunityPrivilege": rsSnmpCommunityPrivilege,
       "rsSnmpCommunityAccessList": rsSnmpCommunityAccessList,
       "rsSnmpTrap": rsSnmpTrap,
       "rsSnmpTrapGlobalFilter": rsSnmpTrapGlobalFilter,
       "rsSnmpTrapSource": rsSnmpTrapSource,
       "rsSnmpTrapHostTable": rsSnmpTrapHostTable,
       "rsSnmpTrapHostEntry": rsSnmpTrapHostEntry,
       "rsSnmpTrapHostIpAddress": rsSnmpTrapHostIpAddress,
       "rsSnmpTrapHostRowStatus": rsSnmpTrapHostRowStatus,
       "rsSnmpTrapHostUdpPort": rsSnmpTrapHostUdpPort,
       "rsSnmpTrapHostCommunity": rsSnmpTrapHostCommunity,
       "rsSnmpTrapHostProtocolVersion": rsSnmpTrapHostProtocolVersion,
       "rsSnmpTrapHostFilter": rsSnmpTrapHostFilter,
       "rsSnmpTrapHostSends": rsSnmpTrapHostSends,
       "rsSnmpAuthFailId": rsSnmpAuthFailId,
       "rsSnmpAuthFailIdIpAddress": rsSnmpAuthFailIdIpAddress,
       "rsSnmpAuthFailIdUdpPort": rsSnmpAuthFailIdUdpPort,
       "rsSnmpAuthFailIdCommunity": rsSnmpAuthFailIdCommunity,
       "rsSnmpAuthFailIdReason": rsSnmpAuthFailIdReason,
       "rsSnmpConformance": rsSnmpConformance,
       "rsSnmpCompliances": rsSnmpCompliances,
       "rsSnmpCompliance": rsSnmpCompliance,
       "rsSnmpGroups": rsSnmpGroups,
       "rsSnmpGroup": rsSnmpGroup}
)
