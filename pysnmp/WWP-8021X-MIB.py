# SNMP MIB module (WWP-8021X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-8021X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:35 2024
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

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwp8021xMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Wwp8021xMIB_ObjectIdentity = ObjectIdentity
wwp8021xMIB = _Wwp8021xMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1)
)
_Wwp8021xConf_ObjectIdentity = ObjectIdentity
wwp8021xConf = _Wwp8021xConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 1)
)
_Wwp8021xGroups_ObjectIdentity = ObjectIdentity
wwp8021xGroups = _Wwp8021xGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 1, 1)
)
_Wwp8021xCompls_ObjectIdentity = ObjectIdentity
wwp8021xCompls = _Wwp8021xCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 1, 2)
)
_Wwp8021xObjs_ObjectIdentity = ObjectIdentity
wwp8021xObjs = _Wwp8021xObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2)
)
_Wwp8021xPortTable_Object = MibTable
wwp8021xPortTable = _Wwp8021xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwp8021xPortTable.setStatus("current")
_Wwp8021xPortEntry_Object = MibTableRow
wwp8021xPortEntry = _Wwp8021xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 1, 1)
)
wwp8021xPortEntry.setIndexNames(
    (0, "WWP-8021X-MIB", "wwp8021xPort"),
)
if mibBuilder.loadTexts:
    wwp8021xPortEntry.setStatus("current")


class _Wwp8021xPort_Type(Integer32):
    """Custom type wwp8021xPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Wwp8021xPort_Type.__name__ = "Integer32"
_Wwp8021xPort_Object = MibTableColumn
wwp8021xPort = _Wwp8021xPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 1, 1, 1),
    _Wwp8021xPort_Type()
)
wwp8021xPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwp8021xPort.setStatus("current")


class _Wwp8021xRole_Type(Integer32):
    """Custom type wwp8021xRole based on Integer32"""
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
        *(("authenticator", 3),
          ("both", 4),
          ("none", 1),
          ("supplicant", 2))
    )


_Wwp8021xRole_Type.__name__ = "Integer32"
_Wwp8021xRole_Object = MibTableColumn
wwp8021xRole = _Wwp8021xRole_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 1, 1, 2),
    _Wwp8021xRole_Type()
)
wwp8021xRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwp8021xRole.setStatus("current")
_Wwp8021xRadiusClient_ObjectIdentity = ObjectIdentity
wwp8021xRadiusClient = _Wwp8021xRadiusClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2)
)


class _Wwp8021xRadiusClientTimeout_Type(Integer32):
    """Custom type wwp8021xRadiusClientTimeout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Wwp8021xRadiusClientTimeout_Type.__name__ = "Integer32"
_Wwp8021xRadiusClientTimeout_Object = MibScalar
wwp8021xRadiusClientTimeout = _Wwp8021xRadiusClientTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 1),
    _Wwp8021xRadiusClientTimeout_Type()
)
wwp8021xRadiusClientTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwp8021xRadiusClientTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwp8021xRadiusClientTimeout.setUnits("seconds")


class _Wwp8021xRadiusClientRetries_Type(Integer32):
    """Custom type wwp8021xRadiusClientRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Wwp8021xRadiusClientRetries_Type.__name__ = "Integer32"
_Wwp8021xRadiusClientRetries_Object = MibScalar
wwp8021xRadiusClientRetries = _Wwp8021xRadiusClientRetries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 2),
    _Wwp8021xRadiusClientRetries_Type()
)
wwp8021xRadiusClientRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwp8021xRadiusClientRetries.setStatus("current")


class _Wwp8021xRadiusDeadTime_Type(Integer32):
    """Custom type wwp8021xRadiusDeadTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Wwp8021xRadiusDeadTime_Type.__name__ = "Integer32"
_Wwp8021xRadiusDeadTime_Object = MibScalar
wwp8021xRadiusDeadTime = _Wwp8021xRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 3),
    _Wwp8021xRadiusDeadTime_Type()
)
wwp8021xRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwp8021xRadiusDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    wwp8021xRadiusDeadTime.setUnits("minutes")
_Wwp8021xRadiusServerTable_Object = MibTable
wwp8021xRadiusServerTable = _Wwp8021xRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    wwp8021xRadiusServerTable.setStatus("current")
_Wwp8021xRadiusServerEntry_Object = MibTableRow
wwp8021xRadiusServerEntry = _Wwp8021xRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 4, 1)
)
wwp8021xRadiusServerEntry.setIndexNames(
    (0, "WWP-8021X-MIB", "wwp8021xRadiusServerId"),
)
if mibBuilder.loadTexts:
    wwp8021xRadiusServerEntry.setStatus("current")


class _Wwp8021xRadiusServerId_Type(Integer32):
    """Custom type wwp8021xRadiusServerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Wwp8021xRadiusServerId_Type.__name__ = "Integer32"
_Wwp8021xRadiusServerId_Object = MibTableColumn
wwp8021xRadiusServerId = _Wwp8021xRadiusServerId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 4, 1, 1),
    _Wwp8021xRadiusServerId_Type()
)
wwp8021xRadiusServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwp8021xRadiusServerId.setStatus("current")
_Wwp8021xRadiusServerIpAddr_Type = IpAddress
_Wwp8021xRadiusServerIpAddr_Object = MibTableColumn
wwp8021xRadiusServerIpAddr = _Wwp8021xRadiusServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 4, 1, 2),
    _Wwp8021xRadiusServerIpAddr_Type()
)
wwp8021xRadiusServerIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwp8021xRadiusServerIpAddr.setStatus("current")


class _Wwp8021xRadiusServerAuthPort_Type(Integer32):
    """Custom type wwp8021xRadiusServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Wwp8021xRadiusServerAuthPort_Type.__name__ = "Integer32"
_Wwp8021xRadiusServerAuthPort_Object = MibTableColumn
wwp8021xRadiusServerAuthPort = _Wwp8021xRadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 4, 1, 3),
    _Wwp8021xRadiusServerAuthPort_Type()
)
wwp8021xRadiusServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwp8021xRadiusServerAuthPort.setStatus("current")


class _Wwp8021xRadiusServerAuthKey_Type(OctetString):
    """Custom type wwp8021xRadiusServerAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 127),
    )


_Wwp8021xRadiusServerAuthKey_Type.__name__ = "OctetString"
_Wwp8021xRadiusServerAuthKey_Object = MibTableColumn
wwp8021xRadiusServerAuthKey = _Wwp8021xRadiusServerAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 4, 1, 4),
    _Wwp8021xRadiusServerAuthKey_Type()
)
wwp8021xRadiusServerAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwp8021xRadiusServerAuthKey.setStatus("current")
_Wwp8021xRadiusServerStatus_Type = RowStatus
_Wwp8021xRadiusServerStatus_Object = MibTableColumn
wwp8021xRadiusServerStatus = _Wwp8021xRadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 2, 4, 1, 5),
    _Wwp8021xRadiusServerStatus_Type()
)
wwp8021xRadiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwp8021xRadiusServerStatus.setStatus("current")
_Wwp8021xSupplicantSecTable_Object = MibTable
wwp8021xSupplicantSecTable = _Wwp8021xSupplicantSecTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwp8021xSupplicantSecTable.setStatus("current")
_Wwp8021xSupplicantSecEntry_Object = MibTableRow
wwp8021xSupplicantSecEntry = _Wwp8021xSupplicantSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 3, 1)
)
wwp8021xSupplicantSecEntry.setIndexNames(
    (0, "WWP-8021X-MIB", "wwp8021xPort"),
)
if mibBuilder.loadTexts:
    wwp8021xSupplicantSecEntry.setStatus("current")


class _Wwp8021xSupplicantSecUserName_Type(OctetString):
    """Custom type wwp8021xSupplicantSecUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Wwp8021xSupplicantSecUserName_Type.__name__ = "OctetString"
_Wwp8021xSupplicantSecUserName_Object = MibTableColumn
wwp8021xSupplicantSecUserName = _Wwp8021xSupplicantSecUserName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 3, 1, 1),
    _Wwp8021xSupplicantSecUserName_Type()
)
wwp8021xSupplicantSecUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwp8021xSupplicantSecUserName.setStatus("current")


class _Wwp8021xSupplicantSecPassword_Type(OctetString):
    """Custom type wwp8021xSupplicantSecPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Wwp8021xSupplicantSecPassword_Type.__name__ = "OctetString"
_Wwp8021xSupplicantSecPassword_Object = MibTableColumn
wwp8021xSupplicantSecPassword = _Wwp8021xSupplicantSecPassword_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 2, 3, 1, 2),
    _Wwp8021xSupplicantSecPassword_Type()
)
wwp8021xSupplicantSecPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwp8021xSupplicantSecPassword.setStatus("current")
_Wwp8021xEvents_ObjectIdentity = ObjectIdentity
wwp8021xEvents = _Wwp8021xEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 3)
)
_Wwp8021xEventsV2_ObjectIdentity = ObjectIdentity
wwp8021xEventsV2 = _Wwp8021xEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 401, 1, 3, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-8021X-MIB",
    **{"wwp8021xMibModule": wwp8021xMibModule,
       "wwp8021xMIB": wwp8021xMIB,
       "wwp8021xConf": wwp8021xConf,
       "wwp8021xGroups": wwp8021xGroups,
       "wwp8021xCompls": wwp8021xCompls,
       "wwp8021xObjs": wwp8021xObjs,
       "wwp8021xPortTable": wwp8021xPortTable,
       "wwp8021xPortEntry": wwp8021xPortEntry,
       "wwp8021xPort": wwp8021xPort,
       "wwp8021xRole": wwp8021xRole,
       "wwp8021xRadiusClient": wwp8021xRadiusClient,
       "wwp8021xRadiusClientTimeout": wwp8021xRadiusClientTimeout,
       "wwp8021xRadiusClientRetries": wwp8021xRadiusClientRetries,
       "wwp8021xRadiusDeadTime": wwp8021xRadiusDeadTime,
       "wwp8021xRadiusServerTable": wwp8021xRadiusServerTable,
       "wwp8021xRadiusServerEntry": wwp8021xRadiusServerEntry,
       "wwp8021xRadiusServerId": wwp8021xRadiusServerId,
       "wwp8021xRadiusServerIpAddr": wwp8021xRadiusServerIpAddr,
       "wwp8021xRadiusServerAuthPort": wwp8021xRadiusServerAuthPort,
       "wwp8021xRadiusServerAuthKey": wwp8021xRadiusServerAuthKey,
       "wwp8021xRadiusServerStatus": wwp8021xRadiusServerStatus,
       "wwp8021xSupplicantSecTable": wwp8021xSupplicantSecTable,
       "wwp8021xSupplicantSecEntry": wwp8021xSupplicantSecEntry,
       "wwp8021xSupplicantSecUserName": wwp8021xSupplicantSecUserName,
       "wwp8021xSupplicantSecPassword": wwp8021xSupplicantSecPassword,
       "wwp8021xEvents": wwp8021xEvents,
       "wwp8021xEventsV2": wwp8021xEventsV2}
)
