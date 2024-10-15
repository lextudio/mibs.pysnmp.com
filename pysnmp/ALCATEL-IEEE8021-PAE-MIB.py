# SNMP MIB module (ALCATEL-IEEE8021-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IEEE8021-PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:33 2024
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

(dot1xAuthConfigEntry,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthConfigEntry")

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

(alcatelCommonMIBModules,
 alcatelConformance,
 alcatelNotifyPrefix,
 alcatelObjects) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "alcatelCommonMIBModules",
    "alcatelConformance",
    "alcatelNotifyPrefix",
    "alcatelObjects")

(ServiceAdminStatus,
 TNamedItem,
 TPolicyStatementNameOrEmpty) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "ServiceAdminStatus",
    "TNamedItem",
    "TPolicyStatementNameOrEmpty")


# MODULE-IDENTITY

alcatelIEEE8021PaeMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 5, 3)
)
alcatelIEEE8021PaeMIBModule.setRevisions(
        ("1907-01-01 00:00",
         "1905-08-31 00:00",
         "1905-03-29 00:00",
         "1904-08-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlxDot1xRadiusServerType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 1),
          ("authorization", 0),
          ("combined", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlxDot1xConformance_ObjectIdentity = ObjectIdentity
alxDot1xConformance = _AlxDot1xConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3)
)
_AlxDot1xAuthenticatorConformance_ObjectIdentity = ObjectIdentity
alxDot1xAuthenticatorConformance = _AlxDot1xAuthenticatorConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1)
)
_AlxDot1xAuthenticatorCompliancs_ObjectIdentity = ObjectIdentity
alxDot1xAuthenticatorCompliancs = _AlxDot1xAuthenticatorCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 1)
)
_AlxDot1xAuthenticatorGroups_ObjectIdentity = ObjectIdentity
alxDot1xAuthenticatorGroups = _AlxDot1xAuthenticatorGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 2)
)
_AlxDot1xRadiusConformance_ObjectIdentity = ObjectIdentity
alxDot1xRadiusConformance = _AlxDot1xRadiusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2)
)
_AlxDot1xRadiusCompliancs_ObjectIdentity = ObjectIdentity
alxDot1xRadiusCompliancs = _AlxDot1xRadiusCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2, 1)
)
_AlxDot1xRadiusGroups_ObjectIdentity = ObjectIdentity
alxDot1xRadiusGroups = _AlxDot1xRadiusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2, 2)
)
_AlxDot1xObjs_ObjectIdentity = ObjectIdentity
alxDot1xObjs = _AlxDot1xObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3)
)
_AlxDot1xAuthenticatorObjs_ObjectIdentity = ObjectIdentity
alxDot1xAuthenticatorObjs = _AlxDot1xAuthenticatorObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1)
)
_Alxdot1xAuthConfigTable_Object = MibTable
alxdot1xAuthConfigTable = _Alxdot1xAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alxdot1xAuthConfigTable.setStatus("current")
_AlxDot1xAuthConfigEntry_Object = MibTableRow
alxDot1xAuthConfigEntry = _AlxDot1xAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alxDot1xAuthConfigEntry.setStatus("current")
_AlxDot1xAuthRadiusPlcy_Type = TPolicyStatementNameOrEmpty
_AlxDot1xAuthRadiusPlcy_Object = MibTableColumn
alxDot1xAuthRadiusPlcy = _AlxDot1xAuthRadiusPlcy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 1, 1, 1, 50),
    _AlxDot1xAuthRadiusPlcy_Type()
)
alxDot1xAuthRadiusPlcy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alxDot1xAuthRadiusPlcy.setStatus("current")
_AlxDot1xRadiusObjs_ObjectIdentity = ObjectIdentity
alxDot1xRadiusObjs = _AlxDot1xRadiusObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2)
)
_AlxDot1xRadiusServerPlcyTable_Object = MibTable
alxDot1xRadiusServerPlcyTable = _AlxDot1xRadiusServerPlcyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    alxDot1xRadiusServerPlcyTable.setStatus("current")
_AlxDot1xRadiusServerPlcyEntry_Object = MibTableRow
alxDot1xRadiusServerPlcyEntry = _AlxDot1xRadiusServerPlcyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1)
)
alxDot1xRadiusServerPlcyEntry.setIndexNames(
    (0, "ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyName"),
)
if mibBuilder.loadTexts:
    alxDot1xRadiusServerPlcyEntry.setStatus("current")
_AlxDot1xRadiusPlcyName_Type = TNamedItem
_AlxDot1xRadiusPlcyName_Object = MibTableColumn
alxDot1xRadiusPlcyName = _AlxDot1xRadiusPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 1),
    _AlxDot1xRadiusPlcyName_Type()
)
alxDot1xRadiusPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcyName.setStatus("current")


class _AlxDot1xRadiusPlcySrceAddr_Type(IpAddress):
    """Custom type alxDot1xRadiusPlcySrceAddr based on IpAddress"""
    defaultHexValue = "00000000"


_AlxDot1xRadiusPlcySrceAddr_Object = MibTableColumn
alxDot1xRadiusPlcySrceAddr = _AlxDot1xRadiusPlcySrceAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 2),
    _AlxDot1xRadiusPlcySrceAddr_Type()
)
alxDot1xRadiusPlcySrceAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcySrceAddr.setStatus("current")


class _AlxDot1xRadiusPlcyAdminState_Type(ServiceAdminStatus):
    """Custom type alxDot1xRadiusPlcyAdminState based on ServiceAdminStatus"""


_AlxDot1xRadiusPlcyAdminState_Object = MibTableColumn
alxDot1xRadiusPlcyAdminState = _AlxDot1xRadiusPlcyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 3),
    _AlxDot1xRadiusPlcyAdminState_Type()
)
alxDot1xRadiusPlcyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcyAdminState.setStatus("current")
_AlxDot1xRadiusPlcyRowStatus_Type = RowStatus
_AlxDot1xRadiusPlcyRowStatus_Object = MibTableColumn
alxDot1xRadiusPlcyRowStatus = _AlxDot1xRadiusPlcyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 4),
    _AlxDot1xRadiusPlcyRowStatus_Type()
)
alxDot1xRadiusPlcyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcyRowStatus.setStatus("current")


class _AlxDot1xRadiusPlcyRetryAttempts_Type(Unsigned32):
    """Custom type alxDot1xRadiusPlcyRetryAttempts based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AlxDot1xRadiusPlcyRetryAttempts_Type.__name__ = "Unsigned32"
_AlxDot1xRadiusPlcyRetryAttempts_Object = MibTableColumn
alxDot1xRadiusPlcyRetryAttempts = _AlxDot1xRadiusPlcyRetryAttempts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 5),
    _AlxDot1xRadiusPlcyRetryAttempts_Type()
)
alxDot1xRadiusPlcyRetryAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcyRetryAttempts.setStatus("current")


class _AlxDot1xRadiusPlcyTimeout_Type(Unsigned32):
    """Custom type alxDot1xRadiusPlcyTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 90),
    )


_AlxDot1xRadiusPlcyTimeout_Type.__name__ = "Unsigned32"
_AlxDot1xRadiusPlcyTimeout_Object = MibTableColumn
alxDot1xRadiusPlcyTimeout = _AlxDot1xRadiusPlcyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 1, 1, 6),
    _AlxDot1xRadiusPlcyTimeout_Type()
)
alxDot1xRadiusPlcyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcyTimeout.setUnits("seconds")
_AlxDot1xRadiusServerTable_Object = MibTable
alxDot1xRadiusServerTable = _AlxDot1xRadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    alxDot1xRadiusServerTable.setStatus("current")
_AlxDot1xRadiusServerEntry_Object = MibTableRow
alxDot1xRadiusServerEntry = _AlxDot1xRadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1)
)
alxDot1xRadiusServerEntry.setIndexNames(
    (0, "ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerPlcyName"),
    (0, "ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    alxDot1xRadiusServerEntry.setStatus("current")
_AlxDot1xRadiusServerPlcyName_Type = TNamedItem
_AlxDot1xRadiusServerPlcyName_Object = MibTableColumn
alxDot1xRadiusServerPlcyName = _AlxDot1xRadiusServerPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 1),
    _AlxDot1xRadiusServerPlcyName_Type()
)
alxDot1xRadiusServerPlcyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerPlcyName.setStatus("current")


class _AlxDot1xRadiusServerIndex_Type(Unsigned32):
    """Custom type alxDot1xRadiusServerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AlxDot1xRadiusServerIndex_Type.__name__ = "Unsigned32"
_AlxDot1xRadiusServerIndex_Object = MibTableColumn
alxDot1xRadiusServerIndex = _AlxDot1xRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 2),
    _AlxDot1xRadiusServerIndex_Type()
)
alxDot1xRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerIndex.setStatus("current")
_AlxDot1xRadiusServerAddress_Type = IpAddress
_AlxDot1xRadiusServerAddress_Object = MibTableColumn
alxDot1xRadiusServerAddress = _AlxDot1xRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 3),
    _AlxDot1xRadiusServerAddress_Type()
)
alxDot1xRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerAddress.setStatus("current")


class _AlxDot1xRadiusServerSecret_Type(OctetString):
    """Custom type alxDot1xRadiusServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AlxDot1xRadiusServerSecret_Type.__name__ = "OctetString"
_AlxDot1xRadiusServerSecret_Object = MibTableColumn
alxDot1xRadiusServerSecret = _AlxDot1xRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 4),
    _AlxDot1xRadiusServerSecret_Type()
)
alxDot1xRadiusServerSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerSecret.setStatus("current")


class _AlxDot1xRadiusServerAuthPort_Type(Unsigned32):
    """Custom type alxDot1xRadiusServerAuthPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlxDot1xRadiusServerAuthPort_Type.__name__ = "Unsigned32"
_AlxDot1xRadiusServerAuthPort_Object = MibTableColumn
alxDot1xRadiusServerAuthPort = _AlxDot1xRadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 5),
    _AlxDot1xRadiusServerAuthPort_Type()
)
alxDot1xRadiusServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerAuthPort.setStatus("current")


class _AlxDot1xRadiusServerOperStatus_Type(Integer32):
    """Custom type alxDot1xRadiusServerOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_AlxDot1xRadiusServerOperStatus_Type.__name__ = "Integer32"
_AlxDot1xRadiusServerOperStatus_Object = MibTableColumn
alxDot1xRadiusServerOperStatus = _AlxDot1xRadiusServerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 6),
    _AlxDot1xRadiusServerOperStatus_Type()
)
alxDot1xRadiusServerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerOperStatus.setStatus("current")
_AlxDot1xRadiusServerRowStatus_Type = RowStatus
_AlxDot1xRadiusServerRowStatus_Object = MibTableColumn
alxDot1xRadiusServerRowStatus = _AlxDot1xRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 7),
    _AlxDot1xRadiusServerRowStatus_Type()
)
alxDot1xRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerRowStatus.setStatus("current")
_AlxDot1xRadiusServerType_Type = AlxDot1xRadiusServerType
_AlxDot1xRadiusServerType_Object = MibTableColumn
alxDot1xRadiusServerType = _AlxDot1xRadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 8),
    _AlxDot1xRadiusServerType_Type()
)
alxDot1xRadiusServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerType.setStatus("current")


class _AlxDot1xRadiusServerAcctPort_Type(Unsigned32):
    """Custom type alxDot1xRadiusServerAcctPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlxDot1xRadiusServerAcctPort_Type.__name__ = "Unsigned32"
_AlxDot1xRadiusServerAcctPort_Object = MibTableColumn
alxDot1xRadiusServerAcctPort = _AlxDot1xRadiusServerAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 2, 3, 2, 2, 1, 9),
    _AlxDot1xRadiusServerAcctPort_Type()
)
alxDot1xRadiusServerAcctPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alxDot1xRadiusServerAcctPort.setStatus("current")
_AlxDot1xNotificationsPrefix_ObjectIdentity = ObjectIdentity
alxDot1xNotificationsPrefix = _AlxDot1xNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 3)
)
_AlxDot1xNotifications_ObjectIdentity = ObjectIdentity
alxDot1xNotifications = _AlxDot1xNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 3, 3, 0)
)
dot1xAuthConfigEntry.registerAugmentions(
    ("ALCATEL-IEEE8021-PAE-MIB",
     "alxDot1xAuthConfigEntry")
)
alxDot1xAuthConfigEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())

# Managed Objects groups

alxDot1xAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 2, 1)
)
alxDot1xAuthConfigGroup.setObjects(
    ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xAuthRadiusPlcy")
)
if mibBuilder.loadTexts:
    alxDot1xAuthConfigGroup.setStatus("current")

alxDot1xRadiusPlcyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 2, 2, 1)
)
alxDot1xRadiusPlcyGroup.setObjects(
      *(("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcySrceAddr"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyAdminState"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyRowStatus"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyRetryAttempts"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusPlcyTimeout"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerAddress"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerSecret"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerAuthPort"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerAcctPort"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerOperStatus"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerRowStatus"),
        ("ALCATEL-IEEE8021-PAE-MIB", "alxDot1xRadiusServerType"))
)
if mibBuilder.loadTexts:
    alxDot1xRadiusPlcyGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alxDot1xAuthenticatorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 3, 1, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alxDot1xAuthenticatorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IEEE8021-PAE-MIB",
    **{"AlxDot1xRadiusServerType": AlxDot1xRadiusServerType,
       "alcatelIEEE8021PaeMIBModule": alcatelIEEE8021PaeMIBModule,
       "alxDot1xConformance": alxDot1xConformance,
       "alxDot1xAuthenticatorConformance": alxDot1xAuthenticatorConformance,
       "alxDot1xAuthenticatorCompliancs": alxDot1xAuthenticatorCompliancs,
       "alxDot1xAuthenticatorCompliance": alxDot1xAuthenticatorCompliance,
       "alxDot1xAuthenticatorGroups": alxDot1xAuthenticatorGroups,
       "alxDot1xAuthConfigGroup": alxDot1xAuthConfigGroup,
       "alxDot1xRadiusConformance": alxDot1xRadiusConformance,
       "alxDot1xRadiusCompliancs": alxDot1xRadiusCompliancs,
       "alxDot1xRadiusGroups": alxDot1xRadiusGroups,
       "alxDot1xRadiusPlcyGroup": alxDot1xRadiusPlcyGroup,
       "alxDot1xObjs": alxDot1xObjs,
       "alxDot1xAuthenticatorObjs": alxDot1xAuthenticatorObjs,
       "alxdot1xAuthConfigTable": alxdot1xAuthConfigTable,
       "alxDot1xAuthConfigEntry": alxDot1xAuthConfigEntry,
       "alxDot1xAuthRadiusPlcy": alxDot1xAuthRadiusPlcy,
       "alxDot1xRadiusObjs": alxDot1xRadiusObjs,
       "alxDot1xRadiusServerPlcyTable": alxDot1xRadiusServerPlcyTable,
       "alxDot1xRadiusServerPlcyEntry": alxDot1xRadiusServerPlcyEntry,
       "alxDot1xRadiusPlcyName": alxDot1xRadiusPlcyName,
       "alxDot1xRadiusPlcySrceAddr": alxDot1xRadiusPlcySrceAddr,
       "alxDot1xRadiusPlcyAdminState": alxDot1xRadiusPlcyAdminState,
       "alxDot1xRadiusPlcyRowStatus": alxDot1xRadiusPlcyRowStatus,
       "alxDot1xRadiusPlcyRetryAttempts": alxDot1xRadiusPlcyRetryAttempts,
       "alxDot1xRadiusPlcyTimeout": alxDot1xRadiusPlcyTimeout,
       "alxDot1xRadiusServerTable": alxDot1xRadiusServerTable,
       "alxDot1xRadiusServerEntry": alxDot1xRadiusServerEntry,
       "alxDot1xRadiusServerPlcyName": alxDot1xRadiusServerPlcyName,
       "alxDot1xRadiusServerIndex": alxDot1xRadiusServerIndex,
       "alxDot1xRadiusServerAddress": alxDot1xRadiusServerAddress,
       "alxDot1xRadiusServerSecret": alxDot1xRadiusServerSecret,
       "alxDot1xRadiusServerAuthPort": alxDot1xRadiusServerAuthPort,
       "alxDot1xRadiusServerOperStatus": alxDot1xRadiusServerOperStatus,
       "alxDot1xRadiusServerRowStatus": alxDot1xRadiusServerRowStatus,
       "alxDot1xRadiusServerType": alxDot1xRadiusServerType,
       "alxDot1xRadiusServerAcctPort": alxDot1xRadiusServerAcctPort,
       "alxDot1xNotificationsPrefix": alxDot1xNotificationsPrefix,
       "alxDot1xNotifications": alxDot1xNotifications}
)
