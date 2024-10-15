# SNMP MIB module (ONEACCESS-SNMP-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-SNMP-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:03 2024
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

(oacExpIMIpAcl,
 oacExpIMManagement,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIpAcl",
    "oacExpIMManagement",
    "oacMIBModules")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oacSnmpConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 2002)
)
oacSnmpConfigMIB.setRevisions(
        ("2011-07-29 00:00",
         "2011-07-26 00:00",
         "2011-06-15 00:00",
         "2010-07-08 00:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacSnmpConfig_ObjectIdentity = ObjectIdentity
oacSnmpConfig = _OacSnmpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20)
)
_OacSnmpConfigObjects_ObjectIdentity = ObjectIdentity
oacSnmpConfigObjects = _OacSnmpConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1)
)


class _OacSnmpSource_Type(OctetString):
    """Custom type oacSnmpSource based on OctetString"""
    defaultValue = OctetString("any")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSnmpSource_Type.__name__ = "OctetString"
_OacSnmpSource_Object = MibScalar
oacSnmpSource = _OacSnmpSource_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 1),
    _OacSnmpSource_Type()
)
oacSnmpSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSnmpSource.setStatus("current")


class _OacSnmpTrapSource_Type(OctetString):
    """Custom type oacSnmpTrapSource based on OctetString"""
    defaultValue = OctetString("any")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSnmpTrapSource_Type.__name__ = "OctetString"
_OacSnmpTrapSource_Object = MibScalar
oacSnmpTrapSource = _OacSnmpTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 2),
    _OacSnmpTrapSource_Type()
)
oacSnmpTrapSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSnmpTrapSource.setStatus("current")


class _OacSnmpMibIfDescrShort_Type(TruthValue):
    """Custom type oacSnmpMibIfDescrShort based on TruthValue"""


_OacSnmpMibIfDescrShort_Object = MibScalar
oacSnmpMibIfDescrShort = _OacSnmpMibIfDescrShort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 3),
    _OacSnmpMibIfDescrShort_Type()
)
oacSnmpMibIfDescrShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSnmpMibIfDescrShort.setStatus("current")


class _OacSnmpChassisId_Type(OctetString):
    """Custom type oacSnmpChassisId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSnmpChassisId_Type.__name__ = "OctetString"
_OacSnmpChassisId_Object = MibScalar
oacSnmpChassisId = _OacSnmpChassisId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 4),
    _OacSnmpChassisId_Type()
)
oacSnmpChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSnmpChassisId.setStatus("current")


class _OacSnmpMaxMsgSize_Type(Integer32):
    """Custom type oacSnmpMaxMsgSize based on Integer32"""
    defaultValue = 8192


_OacSnmpMaxMsgSize_Object = MibScalar
oacSnmpMaxMsgSize = _OacSnmpMaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 5),
    _OacSnmpMaxMsgSize_Type()
)
oacSnmpMaxMsgSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSnmpMaxMsgSize.setStatus("current")
_OacSnmpCommunityConfigTable_Object = MibTable
oacSnmpCommunityConfigTable = _OacSnmpCommunityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6)
)
if mibBuilder.loadTexts:
    oacSnmpCommunityConfigTable.setStatus("current")
_OacSnmpCommunityConfigEntry_Object = MibTableRow
oacSnmpCommunityConfigEntry = _OacSnmpCommunityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1)
)
oacSnmpCommunityConfigEntry.setIndexNames(
    (0, "ONEACCESS-SNMP-CONFIG-MIB", "oacSnmpCommunityString"),
    (0, "ONEACCESS-SNMP-CONFIG-MIB", "oacSnmpCommunityAccessType"),
)
if mibBuilder.loadTexts:
    oacSnmpCommunityConfigEntry.setStatus("current")


class _OacSnmpCommunityString_Type(OctetString):
    """Custom type oacSnmpCommunityString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSnmpCommunityString_Type.__name__ = "OctetString"
_OacSnmpCommunityString_Object = MibTableColumn
oacSnmpCommunityString = _OacSnmpCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1, 1),
    _OacSnmpCommunityString_Type()
)
oacSnmpCommunityString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacSnmpCommunityString.setStatus("current")


class _OacSnmpCommunityAccessType_Type(Integer32):
    """Custom type oacSnmpCommunityAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set-read-community", 1),
          ("set-write-community", 2))
    )


_OacSnmpCommunityAccessType_Type.__name__ = "Integer32"
_OacSnmpCommunityAccessType_Object = MibTableColumn
oacSnmpCommunityAccessType = _OacSnmpCommunityAccessType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1, 2),
    _OacSnmpCommunityAccessType_Type()
)
oacSnmpCommunityAccessType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacSnmpCommunityAccessType.setStatus("current")


class _OacSnmpCommunityAclType_Type(Integer32):
    """Custom type oacSnmpCommunityAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_OacSnmpCommunityAclType_Type.__name__ = "Integer32"
_OacSnmpCommunityAclType_Object = MibTableColumn
oacSnmpCommunityAclType = _OacSnmpCommunityAclType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1, 3),
    _OacSnmpCommunityAclType_Type()
)
oacSnmpCommunityAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpCommunityAclType.setStatus("current")


class _OacSnmpCommunityAclName_Type(OctetString):
    """Custom type oacSnmpCommunityAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSnmpCommunityAclName_Type.__name__ = "OctetString"
_OacSnmpCommunityAclName_Object = MibTableColumn
oacSnmpCommunityAclName = _OacSnmpCommunityAclName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1, 4),
    _OacSnmpCommunityAclName_Type()
)
oacSnmpCommunityAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpCommunityAclName.setStatus("current")


class _OacSnmpCommunityV2GroupName_Type(OctetString):
    """Custom type oacSnmpCommunityV2GroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_OacSnmpCommunityV2GroupName_Type.__name__ = "OctetString"
_OacSnmpCommunityV2GroupName_Object = MibTableColumn
oacSnmpCommunityV2GroupName = _OacSnmpCommunityV2GroupName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1, 5),
    _OacSnmpCommunityV2GroupName_Type()
)
oacSnmpCommunityV2GroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpCommunityV2GroupName.setStatus("current")
_OacSnmpCommunityisEncrypted_Type = TruthValue
_OacSnmpCommunityisEncrypted_Object = MibTableColumn
oacSnmpCommunityisEncrypted = _OacSnmpCommunityisEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1, 6),
    _OacSnmpCommunityisEncrypted_Type()
)
oacSnmpCommunityisEncrypted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpCommunityisEncrypted.setStatus("current")
_OacSnmpCommunityRowStatus_Type = RowStatus
_OacSnmpCommunityRowStatus_Object = MibTableColumn
oacSnmpCommunityRowStatus = _OacSnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 6, 1, 7),
    _OacSnmpCommunityRowStatus_Type()
)
oacSnmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpCommunityRowStatus.setStatus("current")


class _OacSnmpEngineId_Type(OctetString):
    """Custom type oacSnmpEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSnmpEngineId_Type.__name__ = "OctetString"
_OacSnmpEngineId_Object = MibScalar
oacSnmpEngineId = _OacSnmpEngineId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 7),
    _OacSnmpEngineId_Type()
)
oacSnmpEngineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSnmpEngineId.setStatus("current")


class _OacSnmpRemoteAgentIpAddr_Type(IpAddress):
    """Custom type oacSnmpRemoteAgentIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_OacSnmpRemoteAgentIpAddr_Object = MibScalar
oacSnmpRemoteAgentIpAddr = _OacSnmpRemoteAgentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 8),
    _OacSnmpRemoteAgentIpAddr_Type()
)
oacSnmpRemoteAgentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacSnmpRemoteAgentIpAddr.setStatus("current")
_OacSnmpRemoteEngineIdConfigTable_Object = MibTable
oacSnmpRemoteEngineIdConfigTable = _OacSnmpRemoteEngineIdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 9)
)
if mibBuilder.loadTexts:
    oacSnmpRemoteEngineIdConfigTable.setStatus("current")
_OacSnmpRemoteEngineIdConfigEntry_Object = MibTableRow
oacSnmpRemoteEngineIdConfigEntry = _OacSnmpRemoteEngineIdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 9, 1)
)
oacSnmpRemoteEngineIdConfigEntry.setIndexNames(
    (0, "ONEACCESS-SNMP-CONFIG-MIB", "oacSnmpRemoteEngineId"),
)
if mibBuilder.loadTexts:
    oacSnmpRemoteEngineIdConfigEntry.setStatus("current")


class _OacSnmpRemoteEngineId_Type(OctetString):
    """Custom type oacSnmpRemoteEngineId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_OacSnmpRemoteEngineId_Type.__name__ = "OctetString"
_OacSnmpRemoteEngineId_Object = MibTableColumn
oacSnmpRemoteEngineId = _OacSnmpRemoteEngineId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 9, 1, 1),
    _OacSnmpRemoteEngineId_Type()
)
oacSnmpRemoteEngineId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacSnmpRemoteEngineId.setStatus("current")
_OacSnmpRemoteEngineIpAddr_Type = IpAddress
_OacSnmpRemoteEngineIpAddr_Object = MibTableColumn
oacSnmpRemoteEngineIpAddr = _OacSnmpRemoteEngineIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 9, 1, 2),
    _OacSnmpRemoteEngineIpAddr_Type()
)
oacSnmpRemoteEngineIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpRemoteEngineIpAddr.setStatus("current")


class _OacSnmpRemoteEngineMaxMsgSize_Type(Integer32):
    """Custom type oacSnmpRemoteEngineMaxMsgSize based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 8192),
    )


_OacSnmpRemoteEngineMaxMsgSize_Type.__name__ = "Integer32"
_OacSnmpRemoteEngineMaxMsgSize_Object = MibTableColumn
oacSnmpRemoteEngineMaxMsgSize = _OacSnmpRemoteEngineMaxMsgSize_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 9, 1, 3),
    _OacSnmpRemoteEngineMaxMsgSize_Type()
)
oacSnmpRemoteEngineMaxMsgSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpRemoteEngineMaxMsgSize.setStatus("current")
_OacSnmpRemoteEngineRowstatus_Type = RowStatus
_OacSnmpRemoteEngineRowstatus_Object = MibTableColumn
oacSnmpRemoteEngineRowstatus = _OacSnmpRemoteEngineRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 9, 1, 4),
    _OacSnmpRemoteEngineRowstatus_Type()
)
oacSnmpRemoteEngineRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpRemoteEngineRowstatus.setStatus("current")
_OacSnmpTrapConfigTable_Object = MibTable
oacSnmpTrapConfigTable = _OacSnmpTrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 10)
)
if mibBuilder.loadTexts:
    oacSnmpTrapConfigTable.setStatus("current")
_OacSnmpTrapConfigEntry_Object = MibTableRow
oacSnmpTrapConfigEntry = _OacSnmpTrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 10, 1)
)
oacSnmpTrapConfigEntry.setIndexNames(
    (0, "ONEACCESS-SNMP-CONFIG-MIB", "oacSnmpTrapConfigType"),
)
if mibBuilder.loadTexts:
    oacSnmpTrapConfigEntry.setStatus("current")


class _OacSnmpTrapConfigType_Type(Integer32):
    """Custom type oacSnmpTrapConfigType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("acl", 2),
          ("bgp", 3),
          ("ipsec", 4),
          ("isakmp", 5),
          ("isdn", 6),
          ("nat", 7),
          ("pstn", 8),
          ("standard", 1),
          ("vrrp", 9))
    )


_OacSnmpTrapConfigType_Type.__name__ = "Integer32"
_OacSnmpTrapConfigType_Object = MibTableColumn
oacSnmpTrapConfigType = _OacSnmpTrapConfigType_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 10, 1, 1),
    _OacSnmpTrapConfigType_Type()
)
oacSnmpTrapConfigType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacSnmpTrapConfigType.setStatus("current")
_OacSnmpTrapConfigisEnabled_Type = TruthValue
_OacSnmpTrapConfigisEnabled_Object = MibTableColumn
oacSnmpTrapConfigisEnabled = _OacSnmpTrapConfigisEnabled_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 10, 1, 2),
    _OacSnmpTrapConfigisEnabled_Type()
)
oacSnmpTrapConfigisEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpTrapConfigisEnabled.setStatus("current")
_OacSnmpTrapConfigRowStatus_Type = RowStatus
_OacSnmpTrapConfigRowStatus_Object = MibTableColumn
oacSnmpTrapConfigRowStatus = _OacSnmpTrapConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 1, 10, 1, 3),
    _OacSnmpTrapConfigRowStatus_Type()
)
oacSnmpTrapConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacSnmpTrapConfigRowStatus.setStatus("current")
_OacSnmpConfigConformance_ObjectIdentity = ObjectIdentity
oacSnmpConfigConformance = _OacSnmpConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 2)
)
_OacSnmpConfigGroups_ObjectIdentity = ObjectIdentity
oacSnmpConfigGroups = _OacSnmpConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 2, 1)
)
_OacSnmpCompls_ObjectIdentity = ObjectIdentity
oacSnmpCompls = _OacSnmpCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 2, 2)
)

# Managed Objects groups

oacSnmpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 20, 2, 1, 1)
)
oacSnmpConfigGroup.setObjects(
    ("ONEACCESS-SNMP-CONFIG-MIB", "oacSnmpTrapConfigisEnabled")
)
if mibBuilder.loadTexts:
    oacSnmpConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-SNMP-CONFIG-MIB",
    **{"oacSnmpConfigMIB": oacSnmpConfigMIB,
       "oacSnmpConfig": oacSnmpConfig,
       "oacSnmpConfigObjects": oacSnmpConfigObjects,
       "oacSnmpSource": oacSnmpSource,
       "oacSnmpTrapSource": oacSnmpTrapSource,
       "oacSnmpMibIfDescrShort": oacSnmpMibIfDescrShort,
       "oacSnmpChassisId": oacSnmpChassisId,
       "oacSnmpMaxMsgSize": oacSnmpMaxMsgSize,
       "oacSnmpCommunityConfigTable": oacSnmpCommunityConfigTable,
       "oacSnmpCommunityConfigEntry": oacSnmpCommunityConfigEntry,
       "oacSnmpCommunityString": oacSnmpCommunityString,
       "oacSnmpCommunityAccessType": oacSnmpCommunityAccessType,
       "oacSnmpCommunityAclType": oacSnmpCommunityAclType,
       "oacSnmpCommunityAclName": oacSnmpCommunityAclName,
       "oacSnmpCommunityV2GroupName": oacSnmpCommunityV2GroupName,
       "oacSnmpCommunityisEncrypted": oacSnmpCommunityisEncrypted,
       "oacSnmpCommunityRowStatus": oacSnmpCommunityRowStatus,
       "oacSnmpEngineId": oacSnmpEngineId,
       "oacSnmpRemoteAgentIpAddr": oacSnmpRemoteAgentIpAddr,
       "oacSnmpRemoteEngineIdConfigTable": oacSnmpRemoteEngineIdConfigTable,
       "oacSnmpRemoteEngineIdConfigEntry": oacSnmpRemoteEngineIdConfigEntry,
       "oacSnmpRemoteEngineId": oacSnmpRemoteEngineId,
       "oacSnmpRemoteEngineIpAddr": oacSnmpRemoteEngineIpAddr,
       "oacSnmpRemoteEngineMaxMsgSize": oacSnmpRemoteEngineMaxMsgSize,
       "oacSnmpRemoteEngineRowstatus": oacSnmpRemoteEngineRowstatus,
       "oacSnmpTrapConfigTable": oacSnmpTrapConfigTable,
       "oacSnmpTrapConfigEntry": oacSnmpTrapConfigEntry,
       "oacSnmpTrapConfigType": oacSnmpTrapConfigType,
       "oacSnmpTrapConfigisEnabled": oacSnmpTrapConfigisEnabled,
       "oacSnmpTrapConfigRowStatus": oacSnmpTrapConfigRowStatus,
       "oacSnmpConfigConformance": oacSnmpConfigConformance,
       "oacSnmpConfigGroups": oacSnmpConfigGroups,
       "oacSnmpConfigGroup": oacSnmpConfigGroup,
       "oacSnmpCompls": oacSnmpCompls}
)
