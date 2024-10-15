# SNMP MIB module (CISCO-AUTH-FRAMEWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-AUTH-FRAMEWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:56:12 2024
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

(CnnEouPostureTokenString,) = mibBuilder.importSymbols(
    "CISCO-NAC-TC-MIB",
    "CnnEouPostureTokenString")

(VlanIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-PRIVATE-VLAN-MIB",
    "VlanIndexOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoAuthFrameworkMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656)
)
ciscoAuthFrameworkMIB.setRevisions(
        ("2013-08-23 00:00",
         "2010-11-17 00:00",
         "2010-04-01 00:00",
         "2009-04-20 00:00",
         "2008-10-24 00:00",
         "2008-08-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoAuthControlledDirections(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("both", 0),
          ("in", 1))
    )



class CiscoAuthControlledPortControl(Integer32, TextualConvention):
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
        *(("auto", 2),
          ("forceAuthorized", 3),
          ("forceUnauthorized", 1))
    )



class CiscoAuthMethod(Integer32, TextualConvention):
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
        *(("dot1x", 2),
          ("macAuthBypass", 3),
          ("other", 1),
          ("webAuth", 4))
    )



class CiscoAuthMethodList(OctetString, TextualConvention):
    status = "current"


class CiscoAuthHostMode(Integer32, TextualConvention):
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
        *(("multiAuth", 3),
          ("multiDomain", 4),
          ("multiHost", 2),
          ("singleHost", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoAuthFrameworkMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkMIBNotifs = _CiscoAuthFrameworkMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 0)
)
_CiscoAuthFrameworkMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkMIBObjects = _CiscoAuthFrameworkMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1)
)
_CiscoAuthFrameworkSystem_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkSystem = _CiscoAuthFrameworkSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1)
)
_CafAaaNoRespRecoveryDelay_Type = Unsigned32
_CafAaaNoRespRecoveryDelay_Object = MibScalar
cafAaaNoRespRecoveryDelay = _CafAaaNoRespRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 1),
    _CafAaaNoRespRecoveryDelay_Type()
)
cafAaaNoRespRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafAaaNoRespRecoveryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cafAaaNoRespRecoveryDelay.setUnits("milliseconds")
_CafAuthMethodRegTable_Object = MibTable
cafAuthMethodRegTable = _CafAuthMethodRegTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cafAuthMethodRegTable.setStatus("current")
_CafAuthMethodRegEntry_Object = MibTableRow
cafAuthMethodRegEntry = _CafAuthMethodRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1)
)
cafAuthMethodRegEntry.setIndexNames(
    (0, "CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethod"),
)
if mibBuilder.loadTexts:
    cafAuthMethodRegEntry.setStatus("current")
_CafAuthMethod_Type = CiscoAuthMethod
_CafAuthMethod_Object = MibTableColumn
cafAuthMethod = _CafAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1, 1),
    _CafAuthMethod_Type()
)
cafAuthMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cafAuthMethod.setStatus("current")
_CafAuthMethodDefaultPriority_Type = Unsigned32
_CafAuthMethodDefaultPriority_Object = MibTableColumn
cafAuthMethodDefaultPriority = _CafAuthMethodDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1, 2),
    _CafAuthMethodDefaultPriority_Type()
)
cafAuthMethodDefaultPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafAuthMethodDefaultPriority.setStatus("current")
_CafAuthMethodDefaultExecOrder_Type = Unsigned32
_CafAuthMethodDefaultExecOrder_Object = MibTableColumn
cafAuthMethodDefaultExecOrder = _CafAuthMethodDefaultExecOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 2, 1, 3),
    _CafAuthMethodDefaultExecOrder_Type()
)
cafAuthMethodDefaultExecOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafAuthMethodDefaultExecOrder.setStatus("current")


class _CafMacMoveMode_Type(Integer32):
    """Custom type cafMacMoveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_CafMacMoveMode_Type.__name__ = "Integer32"
_CafMacMoveMode_Object = MibScalar
cafMacMoveMode = _CafMacMoveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 3),
    _CafMacMoveMode_Type()
)
cafMacMoveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafMacMoveMode.setStatus("current")
_CafCoABouncePortCommandIgnoreEnabled_Type = TruthValue
_CafCoABouncePortCommandIgnoreEnabled_Object = MibScalar
cafCoABouncePortCommandIgnoreEnabled = _CafCoABouncePortCommandIgnoreEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 4),
    _CafCoABouncePortCommandIgnoreEnabled_Type()
)
cafCoABouncePortCommandIgnoreEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafCoABouncePortCommandIgnoreEnabled.setStatus("current")
_CafCoADisablePortCommandIgnoreEnabled_Type = TruthValue
_CafCoADisablePortCommandIgnoreEnabled_Object = MibScalar
cafCoADisablePortCommandIgnoreEnabled = _CafCoADisablePortCommandIgnoreEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 1, 5),
    _CafCoADisablePortCommandIgnoreEnabled_Type()
)
cafCoADisablePortCommandIgnoreEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafCoADisablePortCommandIgnoreEnabled.setStatus("current")
_CiscoAuthFrwkAuthenticator_ObjectIdentity = ObjectIdentity
ciscoAuthFrwkAuthenticator = _CiscoAuthFrwkAuthenticator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2)
)
_CafPortConfigTable_Object = MibTable
cafPortConfigTable = _CafPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cafPortConfigTable.setStatus("current")
_CafPortConfigEntry_Object = MibTableRow
cafPortConfigEntry = _CafPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1)
)
cafPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cafPortConfigEntry.setStatus("current")
_CafPortControlledDirection_Type = CiscoAuthControlledDirections
_CafPortControlledDirection_Object = MibTableColumn
cafPortControlledDirection = _CafPortControlledDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 1),
    _CafPortControlledDirection_Type()
)
cafPortControlledDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortControlledDirection.setStatus("current")
_CafPortFallBackProfile_Type = SnmpAdminString
_CafPortFallBackProfile_Object = MibTableColumn
cafPortFallBackProfile = _CafPortFallBackProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 2),
    _CafPortFallBackProfile_Type()
)
cafPortFallBackProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortFallBackProfile.setStatus("current")
_CafPortAuthHostMode_Type = CiscoAuthHostMode
_CafPortAuthHostMode_Object = MibTableColumn
cafPortAuthHostMode = _CafPortAuthHostMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 3),
    _CafPortAuthHostMode_Type()
)
cafPortAuthHostMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortAuthHostMode.setStatus("current")
_CafPortPreAuthOpenAccess_Type = TruthValue
_CafPortPreAuthOpenAccess_Object = MibTableColumn
cafPortPreAuthOpenAccess = _CafPortPreAuthOpenAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 4),
    _CafPortPreAuthOpenAccess_Type()
)
cafPortPreAuthOpenAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortPreAuthOpenAccess.setStatus("current")
_CafPortAuthorizeControl_Type = CiscoAuthControlledPortControl
_CafPortAuthorizeControl_Object = MibTableColumn
cafPortAuthorizeControl = _CafPortAuthorizeControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 5),
    _CafPortAuthorizeControl_Type()
)
cafPortAuthorizeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortAuthorizeControl.setStatus("current")
_CafPortReauthEnabled_Type = TruthValue
_CafPortReauthEnabled_Object = MibTableColumn
cafPortReauthEnabled = _CafPortReauthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 6),
    _CafPortReauthEnabled_Type()
)
cafPortReauthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortReauthEnabled.setStatus("current")
_CafPortReauthInterval_Type = Unsigned32
_CafPortReauthInterval_Object = MibTableColumn
cafPortReauthInterval = _CafPortReauthInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 7),
    _CafPortReauthInterval_Type()
)
cafPortReauthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortReauthInterval.setStatus("current")
if mibBuilder.loadTexts:
    cafPortReauthInterval.setUnits("seconds")
_CafPortRestartInterval_Type = Unsigned32
_CafPortRestartInterval_Object = MibTableColumn
cafPortRestartInterval = _CafPortRestartInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 8),
    _CafPortRestartInterval_Type()
)
cafPortRestartInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortRestartInterval.setStatus("current")
if mibBuilder.loadTexts:
    cafPortRestartInterval.setUnits("seconds")


class _CafPortInactivityTimeout_Type(Integer32):
    """Custom type cafPortInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_CafPortInactivityTimeout_Type.__name__ = "Integer32"
_CafPortInactivityTimeout_Object = MibTableColumn
cafPortInactivityTimeout = _CafPortInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 9),
    _CafPortInactivityTimeout_Type()
)
cafPortInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cafPortInactivityTimeout.setUnits("seconds")


class _CafPortViolationAction_Type(Integer32):
    """Custom type cafPortViolationAction based on Integer32"""
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
        *(("protect", 3),
          ("replace", 4),
          ("restrict", 1),
          ("shutdown", 2))
    )


_CafPortViolationAction_Type.__name__ = "Integer32"
_CafPortViolationAction_Object = MibTableColumn
cafPortViolationAction = _CafPortViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 1, 1, 10),
    _CafPortViolationAction_Type()
)
cafPortViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortViolationAction.setStatus("current")
_CafPortMethodTable_Object = MibTable
cafPortMethodTable = _CafPortMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cafPortMethodTable.setStatus("current")
_CafPortMethodEntry_Object = MibTableRow
cafPortMethodEntry = _CafPortMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1)
)
cafPortMethodEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cafPortMethodEntry.setStatus("current")
_CafPortMethodAdminExecOrder_Type = CiscoAuthMethodList
_CafPortMethodAdminExecOrder_Object = MibTableColumn
cafPortMethodAdminExecOrder = _CafPortMethodAdminExecOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 1),
    _CafPortMethodAdminExecOrder_Type()
)
cafPortMethodAdminExecOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortMethodAdminExecOrder.setStatus("current")
_CafPortMethodAdminPriority_Type = CiscoAuthMethodList
_CafPortMethodAdminPriority_Object = MibTableColumn
cafPortMethodAdminPriority = _CafPortMethodAdminPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 2),
    _CafPortMethodAdminPriority_Type()
)
cafPortMethodAdminPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafPortMethodAdminPriority.setStatus("current")
_CafPortMethodAvailable_Type = CiscoAuthMethodList
_CafPortMethodAvailable_Object = MibTableColumn
cafPortMethodAvailable = _CafPortMethodAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 3),
    _CafPortMethodAvailable_Type()
)
cafPortMethodAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafPortMethodAvailable.setStatus("current")
_CafPortMethodOperExecOrder_Type = CiscoAuthMethodList
_CafPortMethodOperExecOrder_Object = MibTableColumn
cafPortMethodOperExecOrder = _CafPortMethodOperExecOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 4),
    _CafPortMethodOperExecOrder_Type()
)
cafPortMethodOperExecOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafPortMethodOperExecOrder.setStatus("current")
_CafPortMethodOperPriority_Type = CiscoAuthMethodList
_CafPortMethodOperPriority_Object = MibTableColumn
cafPortMethodOperPriority = _CafPortMethodOperPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 2, 2, 1, 5),
    _CafPortMethodOperPriority_Type()
)
cafPortMethodOperPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafPortMethodOperPriority.setStatus("current")
_CiscoAuthFrameworkEvent_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkEvent = _CiscoAuthFrameworkEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3)
)
_CafAuthFailedEventPortTable_Object = MibTable
cafAuthFailedEventPortTable = _CafAuthFailedEventPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cafAuthFailedEventPortTable.setStatus("current")
_CafAuthFailedEventPortEntry_Object = MibTableRow
cafAuthFailedEventPortEntry = _CafAuthFailedEventPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1)
)
cafAuthFailedEventPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cafAuthFailedEventPortEntry.setStatus("current")
_CafAuthFailedMaxRetry_Type = Unsigned32
_CafAuthFailedMaxRetry_Object = MibTableColumn
cafAuthFailedMaxRetry = _CafAuthFailedMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 1),
    _CafAuthFailedMaxRetry_Type()
)
cafAuthFailedMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafAuthFailedMaxRetry.setStatus("current")
_CafAuthFailedNoActionEnabled_Type = TruthValue
_CafAuthFailedNoActionEnabled_Object = MibTableColumn
cafAuthFailedNoActionEnabled = _CafAuthFailedNoActionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 2),
    _CafAuthFailedNoActionEnabled_Type()
)
cafAuthFailedNoActionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafAuthFailedNoActionEnabled.setStatus("current")


class _CafAuthFailedAuthorizedVlan_Type(Integer32):
    """Custom type cafAuthFailedAuthorizedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_CafAuthFailedAuthorizedVlan_Type.__name__ = "Integer32"
_CafAuthFailedAuthorizedVlan_Object = MibTableColumn
cafAuthFailedAuthorizedVlan = _CafAuthFailedAuthorizedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 3),
    _CafAuthFailedAuthorizedVlan_Type()
)
cafAuthFailedAuthorizedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafAuthFailedAuthorizedVlan.setStatus("current")
_CafAuthFailedNextMethodEnabled_Type = TruthValue
_CafAuthFailedNextMethodEnabled_Object = MibTableColumn
cafAuthFailedNextMethodEnabled = _CafAuthFailedNextMethodEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 1, 1, 4),
    _CafAuthFailedNextMethodEnabled_Type()
)
cafAuthFailedNextMethodEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafAuthFailedNextMethodEnabled.setStatus("current")
_CafClientNoRespEventPortTable_Object = MibTable
cafClientNoRespEventPortTable = _CafClientNoRespEventPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cafClientNoRespEventPortTable.setStatus("current")
_CafClientNoRespEventPortEntry_Object = MibTableRow
cafClientNoRespEventPortEntry = _CafClientNoRespEventPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2, 1)
)
cafClientNoRespEventPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cafClientNoRespEventPortEntry.setStatus("current")
_CafClientNoRespNoActionEnabled_Type = TruthValue
_CafClientNoRespNoActionEnabled_Object = MibTableColumn
cafClientNoRespNoActionEnabled = _CafClientNoRespNoActionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2, 1, 1),
    _CafClientNoRespNoActionEnabled_Type()
)
cafClientNoRespNoActionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafClientNoRespNoActionEnabled.setStatus("current")


class _CafClientNoRespAuthorizedVlan_Type(Integer32):
    """Custom type cafClientNoRespAuthorizedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_CafClientNoRespAuthorizedVlan_Type.__name__ = "Integer32"
_CafClientNoRespAuthorizedVlan_Object = MibTableColumn
cafClientNoRespAuthorizedVlan = _CafClientNoRespAuthorizedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 2, 1, 2),
    _CafClientNoRespAuthorizedVlan_Type()
)
cafClientNoRespAuthorizedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafClientNoRespAuthorizedVlan.setStatus("current")
_CafServerEventPortTable_Object = MibTable
cafServerEventPortTable = _CafServerEventPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cafServerEventPortTable.setStatus("current")
_CafServerEventPortEntry_Object = MibTableRow
cafServerEventPortEntry = _CafServerEventPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1)
)
cafServerEventPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cafServerEventPortEntry.setStatus("current")
_CafServerDeadNoActionEnabled_Type = TruthValue
_CafServerDeadNoActionEnabled_Object = MibTableColumn
cafServerDeadNoActionEnabled = _CafServerDeadNoActionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 1),
    _CafServerDeadNoActionEnabled_Type()
)
cafServerDeadNoActionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafServerDeadNoActionEnabled.setStatus("current")
_CafServerDeadRemainAuthorized_Type = TruthValue
_CafServerDeadRemainAuthorized_Object = MibTableColumn
cafServerDeadRemainAuthorized = _CafServerDeadRemainAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 2),
    _CafServerDeadRemainAuthorized_Type()
)
cafServerDeadRemainAuthorized.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafServerDeadRemainAuthorized.setStatus("current")


class _CafServerDeadAuthorizedVlan_Type(Integer32):
    """Custom type cafServerDeadAuthorizedVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_CafServerDeadAuthorizedVlan_Type.__name__ = "Integer32"
_CafServerDeadAuthorizedVlan_Object = MibTableColumn
cafServerDeadAuthorizedVlan = _CafServerDeadAuthorizedVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 3),
    _CafServerDeadAuthorizedVlan_Type()
)
cafServerDeadAuthorizedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafServerDeadAuthorizedVlan.setStatus("current")


class _CafServerAliveAction_Type(Integer32):
    """Custom type cafServerAliveAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reinitialize", 2))
    )


_CafServerAliveAction_Type.__name__ = "Integer32"
_CafServerAliveAction_Object = MibTableColumn
cafServerAliveAction = _CafServerAliveAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 3, 3, 1, 4),
    _CafServerAliveAction_Type()
)
cafServerAliveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafServerAliveAction.setStatus("current")
_CiscoAuthFrameworkSession_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkSession = _CiscoAuthFrameworkSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4)
)
_CafSessionTable_Object = MibTable
cafSessionTable = _CafSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cafSessionTable.setStatus("current")
_CafSessionEntry_Object = MibTableRow
cafSessionEntry = _CafSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1)
)
cafSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (1, "CISCO-AUTH-FRAMEWORK-MIB", "cafSessionId"),
)
if mibBuilder.loadTexts:
    cafSessionEntry.setStatus("current")


class _CafSessionId_Type(OctetString):
    """Custom type cafSessionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CafSessionId_Type.__name__ = "OctetString"
_CafSessionId_Object = MibTableColumn
cafSessionId = _CafSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 1),
    _CafSessionId_Type()
)
cafSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cafSessionId.setStatus("current")
_CafSessionClientMacAddress_Type = MacAddress
_CafSessionClientMacAddress_Object = MibTableColumn
cafSessionClientMacAddress = _CafSessionClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 2),
    _CafSessionClientMacAddress_Type()
)
cafSessionClientMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionClientMacAddress.setStatus("current")
_CafSessionClientAddrType_Type = InetAddressType
_CafSessionClientAddrType_Object = MibTableColumn
cafSessionClientAddrType = _CafSessionClientAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 3),
    _CafSessionClientAddrType_Type()
)
cafSessionClientAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionClientAddrType.setStatus("current")
_CafSessionClientAddress_Type = InetAddress
_CafSessionClientAddress_Object = MibTableColumn
cafSessionClientAddress = _CafSessionClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 4),
    _CafSessionClientAddress_Type()
)
cafSessionClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionClientAddress.setStatus("current")


class _CafSessionStatus_Type(Integer32):
    """Custom type cafSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("authenticationFailed", 5),
          ("authenticationSuccess", 4),
          ("authorizationFailed", 7),
          ("authorizationSuccess", 6),
          ("idle", 1),
          ("noMethod", 3),
          ("running", 2))
    )


_CafSessionStatus_Type.__name__ = "Integer32"
_CafSessionStatus_Object = MibTableColumn
cafSessionStatus = _CafSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 5),
    _CafSessionStatus_Type()
)
cafSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionStatus.setStatus("current")


class _CafSessionDomain_Type(Integer32):
    """Custom type cafSessionDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("data", 2),
          ("other", 1),
          ("voice", 3))
    )


_CafSessionDomain_Type.__name__ = "Integer32"
_CafSessionDomain_Object = MibTableColumn
cafSessionDomain = _CafSessionDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 6),
    _CafSessionDomain_Type()
)
cafSessionDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionDomain.setStatus("current")
_CafSessionAuthHostMode_Type = CiscoAuthHostMode
_CafSessionAuthHostMode_Object = MibTableColumn
cafSessionAuthHostMode = _CafSessionAuthHostMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 7),
    _CafSessionAuthHostMode_Type()
)
cafSessionAuthHostMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionAuthHostMode.setStatus("current")
_CafSessionControlledDirection_Type = CiscoAuthControlledDirections
_CafSessionControlledDirection_Object = MibTableColumn
cafSessionControlledDirection = _CafSessionControlledDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 8),
    _CafSessionControlledDirection_Type()
)
cafSessionControlledDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionControlledDirection.setStatus("current")
_CafSessionPostureToken_Type = CnnEouPostureTokenString
_CafSessionPostureToken_Object = MibTableColumn
cafSessionPostureToken = _CafSessionPostureToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 9),
    _CafSessionPostureToken_Type()
)
cafSessionPostureToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionPostureToken.setStatus("current")
_CafSessionAuthUserName_Type = SnmpAdminString
_CafSessionAuthUserName_Object = MibTableColumn
cafSessionAuthUserName = _CafSessionAuthUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 10),
    _CafSessionAuthUserName_Type()
)
cafSessionAuthUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionAuthUserName.setStatus("current")
_CafSessionClientFramedIpPool_Type = SnmpAdminString
_CafSessionClientFramedIpPool_Object = MibTableColumn
cafSessionClientFramedIpPool = _CafSessionClientFramedIpPool_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 11),
    _CafSessionClientFramedIpPool_Type()
)
cafSessionClientFramedIpPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionClientFramedIpPool.setStatus("current")
_CafSessionAuthorizedBy_Type = SnmpAdminString
_CafSessionAuthorizedBy_Object = MibTableColumn
cafSessionAuthorizedBy = _CafSessionAuthorizedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 12),
    _CafSessionAuthorizedBy_Type()
)
cafSessionAuthorizedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionAuthorizedBy.setStatus("current")
_CafSessionCriticalTimeLeft_Type = Unsigned32
_CafSessionCriticalTimeLeft_Object = MibTableColumn
cafSessionCriticalTimeLeft = _CafSessionCriticalTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 13),
    _CafSessionCriticalTimeLeft_Type()
)
cafSessionCriticalTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionCriticalTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    cafSessionCriticalTimeLeft.setUnits("seconds")
_CafSessionAuthVlan_Type = VlanIndexOrZero
_CafSessionAuthVlan_Object = MibTableColumn
cafSessionAuthVlan = _CafSessionAuthVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 14),
    _CafSessionAuthVlan_Type()
)
cafSessionAuthVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionAuthVlan.setStatus("current")
_CafSessionTimeout_Type = Unsigned32
_CafSessionTimeout_Object = MibTableColumn
cafSessionTimeout = _CafSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 15),
    _CafSessionTimeout_Type()
)
cafSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cafSessionTimeout.setUnits("seconds")
_CafSessionTimeLeft_Type = Unsigned32
_CafSessionTimeLeft_Object = MibTableColumn
cafSessionTimeLeft = _CafSessionTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 16),
    _CafSessionTimeLeft_Type()
)
cafSessionTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    cafSessionTimeLeft.setUnits("seconds")


class _CafSessionTimeoutAction_Type(Integer32):
    """Custom type cafSessionTimeoutAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reauthenticate", 3),
          ("terminate", 2),
          ("unknown", 1))
    )


_CafSessionTimeoutAction_Type.__name__ = "Integer32"
_CafSessionTimeoutAction_Object = MibTableColumn
cafSessionTimeoutAction = _CafSessionTimeoutAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 17),
    _CafSessionTimeoutAction_Type()
)
cafSessionTimeoutAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionTimeoutAction.setStatus("current")
_CafSessionInactivityTimeout_Type = Unsigned32
_CafSessionInactivityTimeout_Object = MibTableColumn
cafSessionInactivityTimeout = _CafSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 18),
    _CafSessionInactivityTimeout_Type()
)
cafSessionInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cafSessionInactivityTimeout.setUnits("seconds")
_CafSessionInactivityTimeLeft_Type = Unsigned32
_CafSessionInactivityTimeLeft_Object = MibTableColumn
cafSessionInactivityTimeLeft = _CafSessionInactivityTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 19),
    _CafSessionInactivityTimeLeft_Type()
)
cafSessionInactivityTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionInactivityTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    cafSessionInactivityTimeLeft.setUnits("seconds")
_CafSessionReauth_Type = TruthValue
_CafSessionReauth_Object = MibTableColumn
cafSessionReauth = _CafSessionReauth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 20),
    _CafSessionReauth_Type()
)
cafSessionReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafSessionReauth.setStatus("current")
_CafSessionTerminate_Type = TruthValue
_CafSessionTerminate_Object = MibTableColumn
cafSessionTerminate = _CafSessionTerminate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 21),
    _CafSessionTerminate_Type()
)
cafSessionTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafSessionTerminate.setStatus("current")
_CafSessionVlanGroupName_Type = SnmpAdminString
_CafSessionVlanGroupName_Object = MibTableColumn
cafSessionVlanGroupName = _CafSessionVlanGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 1, 1, 22),
    _CafSessionVlanGroupName_Type()
)
cafSessionVlanGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionVlanGroupName.setStatus("current")
_CafSessionMethodsInfoTable_Object = MibTable
cafSessionMethodsInfoTable = _CafSessionMethodsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cafSessionMethodsInfoTable.setStatus("current")
_CafSessionMethodsInfoEntry_Object = MibTableRow
cafSessionMethodsInfoEntry = _CafSessionMethodsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2, 1)
)
cafSessionMethodsInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-AUTH-FRAMEWORK-MIB", "cafSessionId"),
    (0, "CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethod"),
)
if mibBuilder.loadTexts:
    cafSessionMethodsInfoEntry.setStatus("current")
_CafSessionMethod_Type = CiscoAuthMethod
_CafSessionMethod_Object = MibTableColumn
cafSessionMethod = _CafSessionMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2, 1, 1),
    _CafSessionMethod_Type()
)
cafSessionMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cafSessionMethod.setStatus("current")


class _CafSessionMethodState_Type(Integer32):
    """Custom type cafSessionMethodState based on Integer32"""
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
        *(("authcFailed", 5),
          ("authcSuccess", 4),
          ("failedOver", 3),
          ("notRun", 1),
          ("running", 2))
    )


_CafSessionMethodState_Type.__name__ = "Integer32"
_CafSessionMethodState_Object = MibTableColumn
cafSessionMethodState = _CafSessionMethodState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 4, 2, 1, 2),
    _CafSessionMethodState_Type()
)
cafSessionMethodState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cafSessionMethodState.setStatus("current")
_CiscoAuthFrwkNotifControl_ObjectIdentity = ObjectIdentity
ciscoAuthFrwkNotifControl = _CiscoAuthFrwkNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 5)
)
_CafSecurityViolationNotifEnable_Type = TruthValue
_CafSecurityViolationNotifEnable_Object = MibScalar
cafSecurityViolationNotifEnable = _CafSecurityViolationNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 5, 1),
    _CafSecurityViolationNotifEnable_Type()
)
cafSecurityViolationNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafSecurityViolationNotifEnable.setStatus("current")
_CafAuthFailNotifEnable_Type = TruthValue
_CafAuthFailNotifEnable_Object = MibScalar
cafAuthFailNotifEnable = _CafAuthFailNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 5, 2),
    _CafAuthFailNotifEnable_Type()
)
cafAuthFailNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cafAuthFailNotifEnable.setStatus("current")
_CiscoAuthFrwkNotifInfo_ObjectIdentity = ObjectIdentity
ciscoAuthFrwkNotifInfo = _CiscoAuthFrwkNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 6)
)
_CafSecurityViolationClient_Type = MacAddress
_CafSecurityViolationClient_Object = MibScalar
cafSecurityViolationClient = _CafSecurityViolationClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 6, 1),
    _CafSecurityViolationClient_Type()
)
cafSecurityViolationClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cafSecurityViolationClient.setStatus("current")
_CafAuthFailClient_Type = MacAddress
_CafAuthFailClient_Object = MibScalar
cafAuthFailClient = _CafAuthFailClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 1, 6, 2),
    _CafAuthFailClient_Type()
)
cafAuthFailClient.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cafAuthFailClient.setStatus("current")
_CiscoAuthFrameworkMIBConform_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkMIBConform = _CiscoAuthFrameworkMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2)
)
_CiscoAuthFrameworkMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkMIBCompliances = _CiscoAuthFrameworkMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1)
)
_CiscoAuthFrameworkMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAuthFrameworkMIBGroups = _CiscoAuthFrameworkMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2)
)

# Managed Objects groups

cafAuthMethodRegGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 1)
)
cafAuthMethodRegGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodDefaultPriority"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthMethodDefaultExecOrder"))
)
if mibBuilder.loadTexts:
    cafAuthMethodRegGroup.setStatus("current")

cafAaaNoRespRecoveryDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 2)
)
cafAaaNoRespRecoveryDelayGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafAaaNoRespRecoveryDelay")
)
if mibBuilder.loadTexts:
    cafAaaNoRespRecoveryDelayGroup.setStatus("current")

cafAuthPortConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 3)
)
cafAuthPortConfigGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafPortControlledDirection"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortFallBackProfile"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortAuthHostMode"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortPreAuthOpenAccess"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortAuthorizeControl"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortReauthEnabled"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortReauthInterval"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortRestartInterval"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortInactivityTimeout"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortViolationAction"))
)
if mibBuilder.loadTexts:
    cafAuthPortConfigGroup.setStatus("current")

cafPortMethodGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 4)
)
cafPortMethodGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodAdminExecOrder"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodAdminPriority"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodAvailable"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodOperExecOrder"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafPortMethodOperPriority"))
)
if mibBuilder.loadTexts:
    cafPortMethodGroup.setStatus("current")

cafAuthFailedEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 5)
)
cafAuthFailedEventGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedMaxRetry"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedNoActionEnabled"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedAuthorizedVlan"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailedNextMethodEnabled"))
)
if mibBuilder.loadTexts:
    cafAuthFailedEventGroup.setStatus("current")

cafClientNoRespEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 6)
)
cafClientNoRespEventGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespNoActionEnabled"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafClientNoRespAuthorizedVlan"))
)
if mibBuilder.loadTexts:
    cafClientNoRespEventGroup.setStatus("current")

cafServerEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 7)
)
cafServerEventGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafServerDeadNoActionEnabled"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerDeadRemainAuthorized"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerDeadAuthorizedVlan"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafServerAliveAction"))
)
if mibBuilder.loadTexts:
    cafServerEventGroup.setStatus("current")

cafSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 8)
)
cafSessionGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientMacAddress"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientAddrType"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientAddress"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionDomain"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionStatus"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthHostMode"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionControlledDirection"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionPostureToken"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthUserName"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionClientFramedIpPool"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthorizedBy"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionCriticalTimeLeft"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionAuthVlan"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTimeout"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTimeLeft"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTimeoutAction"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionInactivityTimeout"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionInactivityTimeLeft"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionReauth"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionTerminate"))
)
if mibBuilder.loadTexts:
    cafSessionGroup.setStatus("current")

cafSessionMethodInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 9)
)
cafSessionMethodInfoGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionMethodState")
)
if mibBuilder.loadTexts:
    cafSessionMethodInfoGroup.setStatus("current")

cafSecViolationNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 10)
)
cafSecViolationNotifEnableGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotifEnable")
)
if mibBuilder.loadTexts:
    cafSecViolationNotifEnableGroup.setStatus("current")

cafSecurityViolationClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 12)
)
cafSecurityViolationClientGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClient")
)
if mibBuilder.loadTexts:
    cafSecurityViolationClientGroup.setStatus("current")

cafSessionVlanGroupNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 13)
)
cafSessionVlanGroupNameGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafSessionVlanGroupName")
)
if mibBuilder.loadTexts:
    cafSessionVlanGroupNameGroup.setStatus("current")

cafMacMoveConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 14)
)
cafMacMoveConfigGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafMacMoveMode")
)
if mibBuilder.loadTexts:
    cafMacMoveConfigGroup.setStatus("current")

cafCoACommandConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 15)
)
cafCoACommandConfigGroup.setObjects(
      *(("CISCO-AUTH-FRAMEWORK-MIB", "cafCoABouncePortCommandIgnoreEnabled"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafCoADisablePortCommandIgnoreEnabled"))
)
if mibBuilder.loadTexts:
    cafCoACommandConfigGroup.setStatus("current")

cafAuthFailNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 17)
)
cafAuthFailNotifEnableGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailNotifEnable")
)
if mibBuilder.loadTexts:
    cafAuthFailNotifEnableGroup.setStatus("current")

cafAuthFailClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 18)
)
cafAuthFailClientGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailClient")
)
if mibBuilder.loadTexts:
    cafAuthFailClientGroup.setStatus("current")


# Notification objects

cafSecurityViolationNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 0, 1)
)
cafSecurityViolationNotif.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationClient"))
)
if mibBuilder.loadTexts:
    cafSecurityViolationNotif.setStatus(
        "current"
    )

cafAuthFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 0, 2)
)
cafAuthFailNotif.setObjects(
      *(("IF-MIB", "ifName"),
        ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailClient"))
)
if mibBuilder.loadTexts:
    cafAuthFailNotif.setStatus(
        "current"
    )


# Notifications groups

cafSecurityViolationNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 11)
)
cafSecurityViolationNotifGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafSecurityViolationNotif")
)
if mibBuilder.loadTexts:
    cafSecurityViolationNotifGroup.setStatus(
        "current"
    )

cafAuthFailNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 2, 16)
)
cafAuthFailNotifGroup.setObjects(
    ("CISCO-AUTH-FRAMEWORK-MIB", "cafAuthFailNotif")
)
if mibBuilder.loadTexts:
    cafAuthFailNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoAuthFrameworkMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoAuthFrameworkMIBCompliance.setStatus(
        "deprecated"
    )

ciscoAuthFrameworkMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoAuthFrameworkMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoAuthFrameworkMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoAuthFrameworkMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoAuthFrameworkMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 656, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoAuthFrameworkMIBCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-AUTH-FRAMEWORK-MIB",
    **{"CiscoAuthControlledDirections": CiscoAuthControlledDirections,
       "CiscoAuthControlledPortControl": CiscoAuthControlledPortControl,
       "CiscoAuthMethod": CiscoAuthMethod,
       "CiscoAuthMethodList": CiscoAuthMethodList,
       "CiscoAuthHostMode": CiscoAuthHostMode,
       "ciscoAuthFrameworkMIB": ciscoAuthFrameworkMIB,
       "ciscoAuthFrameworkMIBNotifs": ciscoAuthFrameworkMIBNotifs,
       "cafSecurityViolationNotif": cafSecurityViolationNotif,
       "cafAuthFailNotif": cafAuthFailNotif,
       "ciscoAuthFrameworkMIBObjects": ciscoAuthFrameworkMIBObjects,
       "ciscoAuthFrameworkSystem": ciscoAuthFrameworkSystem,
       "cafAaaNoRespRecoveryDelay": cafAaaNoRespRecoveryDelay,
       "cafAuthMethodRegTable": cafAuthMethodRegTable,
       "cafAuthMethodRegEntry": cafAuthMethodRegEntry,
       "cafAuthMethod": cafAuthMethod,
       "cafAuthMethodDefaultPriority": cafAuthMethodDefaultPriority,
       "cafAuthMethodDefaultExecOrder": cafAuthMethodDefaultExecOrder,
       "cafMacMoveMode": cafMacMoveMode,
       "cafCoABouncePortCommandIgnoreEnabled": cafCoABouncePortCommandIgnoreEnabled,
       "cafCoADisablePortCommandIgnoreEnabled": cafCoADisablePortCommandIgnoreEnabled,
       "ciscoAuthFrwkAuthenticator": ciscoAuthFrwkAuthenticator,
       "cafPortConfigTable": cafPortConfigTable,
       "cafPortConfigEntry": cafPortConfigEntry,
       "cafPortControlledDirection": cafPortControlledDirection,
       "cafPortFallBackProfile": cafPortFallBackProfile,
       "cafPortAuthHostMode": cafPortAuthHostMode,
       "cafPortPreAuthOpenAccess": cafPortPreAuthOpenAccess,
       "cafPortAuthorizeControl": cafPortAuthorizeControl,
       "cafPortReauthEnabled": cafPortReauthEnabled,
       "cafPortReauthInterval": cafPortReauthInterval,
       "cafPortRestartInterval": cafPortRestartInterval,
       "cafPortInactivityTimeout": cafPortInactivityTimeout,
       "cafPortViolationAction": cafPortViolationAction,
       "cafPortMethodTable": cafPortMethodTable,
       "cafPortMethodEntry": cafPortMethodEntry,
       "cafPortMethodAdminExecOrder": cafPortMethodAdminExecOrder,
       "cafPortMethodAdminPriority": cafPortMethodAdminPriority,
       "cafPortMethodAvailable": cafPortMethodAvailable,
       "cafPortMethodOperExecOrder": cafPortMethodOperExecOrder,
       "cafPortMethodOperPriority": cafPortMethodOperPriority,
       "ciscoAuthFrameworkEvent": ciscoAuthFrameworkEvent,
       "cafAuthFailedEventPortTable": cafAuthFailedEventPortTable,
       "cafAuthFailedEventPortEntry": cafAuthFailedEventPortEntry,
       "cafAuthFailedMaxRetry": cafAuthFailedMaxRetry,
       "cafAuthFailedNoActionEnabled": cafAuthFailedNoActionEnabled,
       "cafAuthFailedAuthorizedVlan": cafAuthFailedAuthorizedVlan,
       "cafAuthFailedNextMethodEnabled": cafAuthFailedNextMethodEnabled,
       "cafClientNoRespEventPortTable": cafClientNoRespEventPortTable,
       "cafClientNoRespEventPortEntry": cafClientNoRespEventPortEntry,
       "cafClientNoRespNoActionEnabled": cafClientNoRespNoActionEnabled,
       "cafClientNoRespAuthorizedVlan": cafClientNoRespAuthorizedVlan,
       "cafServerEventPortTable": cafServerEventPortTable,
       "cafServerEventPortEntry": cafServerEventPortEntry,
       "cafServerDeadNoActionEnabled": cafServerDeadNoActionEnabled,
       "cafServerDeadRemainAuthorized": cafServerDeadRemainAuthorized,
       "cafServerDeadAuthorizedVlan": cafServerDeadAuthorizedVlan,
       "cafServerAliveAction": cafServerAliveAction,
       "ciscoAuthFrameworkSession": ciscoAuthFrameworkSession,
       "cafSessionTable": cafSessionTable,
       "cafSessionEntry": cafSessionEntry,
       "cafSessionId": cafSessionId,
       "cafSessionClientMacAddress": cafSessionClientMacAddress,
       "cafSessionClientAddrType": cafSessionClientAddrType,
       "cafSessionClientAddress": cafSessionClientAddress,
       "cafSessionStatus": cafSessionStatus,
       "cafSessionDomain": cafSessionDomain,
       "cafSessionAuthHostMode": cafSessionAuthHostMode,
       "cafSessionControlledDirection": cafSessionControlledDirection,
       "cafSessionPostureToken": cafSessionPostureToken,
       "cafSessionAuthUserName": cafSessionAuthUserName,
       "cafSessionClientFramedIpPool": cafSessionClientFramedIpPool,
       "cafSessionAuthorizedBy": cafSessionAuthorizedBy,
       "cafSessionCriticalTimeLeft": cafSessionCriticalTimeLeft,
       "cafSessionAuthVlan": cafSessionAuthVlan,
       "cafSessionTimeout": cafSessionTimeout,
       "cafSessionTimeLeft": cafSessionTimeLeft,
       "cafSessionTimeoutAction": cafSessionTimeoutAction,
       "cafSessionInactivityTimeout": cafSessionInactivityTimeout,
       "cafSessionInactivityTimeLeft": cafSessionInactivityTimeLeft,
       "cafSessionReauth": cafSessionReauth,
       "cafSessionTerminate": cafSessionTerminate,
       "cafSessionVlanGroupName": cafSessionVlanGroupName,
       "cafSessionMethodsInfoTable": cafSessionMethodsInfoTable,
       "cafSessionMethodsInfoEntry": cafSessionMethodsInfoEntry,
       "cafSessionMethod": cafSessionMethod,
       "cafSessionMethodState": cafSessionMethodState,
       "ciscoAuthFrwkNotifControl": ciscoAuthFrwkNotifControl,
       "cafSecurityViolationNotifEnable": cafSecurityViolationNotifEnable,
       "cafAuthFailNotifEnable": cafAuthFailNotifEnable,
       "ciscoAuthFrwkNotifInfo": ciscoAuthFrwkNotifInfo,
       "cafSecurityViolationClient": cafSecurityViolationClient,
       "cafAuthFailClient": cafAuthFailClient,
       "ciscoAuthFrameworkMIBConform": ciscoAuthFrameworkMIBConform,
       "ciscoAuthFrameworkMIBCompliances": ciscoAuthFrameworkMIBCompliances,
       "ciscoAuthFrameworkMIBCompliance": ciscoAuthFrameworkMIBCompliance,
       "ciscoAuthFrameworkMIBCompliance2": ciscoAuthFrameworkMIBCompliance2,
       "ciscoAuthFrameworkMIBCompliance3": ciscoAuthFrameworkMIBCompliance3,
       "ciscoAuthFrameworkMIBCompliance4": ciscoAuthFrameworkMIBCompliance4,
       "ciscoAuthFrameworkMIBGroups": ciscoAuthFrameworkMIBGroups,
       "cafAuthMethodRegGroup": cafAuthMethodRegGroup,
       "cafAaaNoRespRecoveryDelayGroup": cafAaaNoRespRecoveryDelayGroup,
       "cafAuthPortConfigGroup": cafAuthPortConfigGroup,
       "cafPortMethodGroup": cafPortMethodGroup,
       "cafAuthFailedEventGroup": cafAuthFailedEventGroup,
       "cafClientNoRespEventGroup": cafClientNoRespEventGroup,
       "cafServerEventGroup": cafServerEventGroup,
       "cafSessionGroup": cafSessionGroup,
       "cafSessionMethodInfoGroup": cafSessionMethodInfoGroup,
       "cafSecViolationNotifEnableGroup": cafSecViolationNotifEnableGroup,
       "cafSecurityViolationNotifGroup": cafSecurityViolationNotifGroup,
       "cafSecurityViolationClientGroup": cafSecurityViolationClientGroup,
       "cafSessionVlanGroupNameGroup": cafSessionVlanGroupNameGroup,
       "cafMacMoveConfigGroup": cafMacMoveConfigGroup,
       "cafCoACommandConfigGroup": cafCoACommandConfigGroup,
       "cafAuthFailNotifGroup": cafAuthFailNotifGroup,
       "cafAuthFailNotifEnableGroup": cafAuthFailNotifEnableGroup,
       "cafAuthFailClientGroup": cafAuthFailClientGroup}
)
