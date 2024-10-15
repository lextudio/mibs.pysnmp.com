# SNMP MIB module (CISCO-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-PAE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:40 2024
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

(CnnEouPostureToken,
 CnnEouPostureTokenString) = mibBuilder.importSymbols(
    "CISCO-NAC-TC-MIB",
    "CnnEouPostureToken",
    "CnnEouPostureTokenString")

(CpgPolicyNameOrEmpty,) = mibBuilder.importSymbols(
    "CISCO-POLICY-GROUP-MIB",
    "CpgPolicyNameOrEmpty")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoURLString,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoURLString")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(PaeControlledPortStatus,
 dot1xAuthConfigEntry,
 dot1xAuthPaeState,
 dot1xPaePortEntry,
 dot1xPaePortNumber) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "PaeControlledPortStatus",
    "dot1xAuthConfigEntry",
    "dot1xAuthPaeState",
    "dot1xPaePortEntry",
    "dot1xPaePortNumber")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoPaeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220)
)
ciscoPaeMIB.setRevisions(
        ("2009-12-10 00:00",
         "2008-07-07 00:00",
         "2008-04-09 00:00",
         "2007-04-25 00:00",
         "2007-04-16 00:00",
         "2007-01-27 00:00",
         "2005-09-22 00:00",
         "2004-04-23 00:00",
         "2004-04-01 00:00",
         "2003-04-08 00:00",
         "2002-10-16 00:00",
         "2001-05-24 10:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ReAuthPeriodSource(Integer32, TextualConvention):
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
        *(("auto", 3),
          ("local", 1),
          ("server", 2))
    )



class CpaeAuthState(Integer32, TextualConvention):
    status = "current"
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 7),
          ("authCResult", 19),
          ("authFailVlan", 12),
          ("authFallback", 18),
          ("authFinished", 16),
          ("authZSuccess", 20),
          ("authenticated", 6),
          ("authenticating", 5),
          ("connecting", 4),
          ("criticalAuth", 13),
          ("disconnected", 3),
          ("forceAuth", 9),
          ("forceUnauth", 10),
          ("guestVlan", 11),
          ("held", 8),
          ("initialize", 2),
          ("ipAwaiting", 14),
          ("other", 1),
          ("policyConfig", 15),
          ("restart", 17))
    )



# MIB Managed Objects in the order of their OIDs

_CpaeMIBNotification_ObjectIdentity = ObjectIdentity
cpaeMIBNotification = _CpaeMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 0)
)
_CpaeMIBObject_ObjectIdentity = ObjectIdentity
cpaeMIBObject = _CpaeMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1)
)
_CpaePortTable_Object = MibTable
cpaePortTable = _CpaePortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1)
)
if mibBuilder.loadTexts:
    cpaePortTable.setStatus("current")
_CpaePortEntry_Object = MibTableRow
cpaePortEntry = _CpaePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpaePortEntry.setStatus("current")
_CpaeMultipleHost_Type = TruthValue
_CpaeMultipleHost_Object = MibTableColumn
cpaeMultipleHost = _CpaeMultipleHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 1),
    _CpaeMultipleHost_Type()
)
cpaeMultipleHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMultipleHost.setStatus("deprecated")


class _CpaePortMode_Type(Integer32):
    """Custom type cpaePortMode based on Integer32"""
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
          ("multiHost", 2),
          ("other", 4),
          ("singleHost", 1))
    )


_CpaePortMode_Type.__name__ = "Integer32"
_CpaePortMode_Object = MibTableColumn
cpaePortMode = _CpaePortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 2),
    _CpaePortMode_Type()
)
cpaePortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaePortMode.setStatus("current")
_CpaeGuestVlanNumber_Type = VlanIndex
_CpaeGuestVlanNumber_Object = MibTableColumn
cpaeGuestVlanNumber = _CpaeGuestVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 3),
    _CpaeGuestVlanNumber_Type()
)
cpaeGuestVlanNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeGuestVlanNumber.setStatus("current")
_CpaeInGuestVlan_Type = TruthValue
_CpaeInGuestVlan_Object = MibTableColumn
cpaeInGuestVlan = _CpaeInGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 4),
    _CpaeInGuestVlan_Type()
)
cpaeInGuestVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeInGuestVlan.setStatus("deprecated")
_CpaeShutdownTimeoutEnabled_Type = TruthValue
_CpaeShutdownTimeoutEnabled_Object = MibTableColumn
cpaeShutdownTimeoutEnabled = _CpaeShutdownTimeoutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 5),
    _CpaeShutdownTimeoutEnabled_Type()
)
cpaeShutdownTimeoutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeShutdownTimeoutEnabled.setStatus("current")
_CpaePortAuthFailVlan_Type = VlanIndex
_CpaePortAuthFailVlan_Object = MibTableColumn
cpaePortAuthFailVlan = _CpaePortAuthFailVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 6),
    _CpaePortAuthFailVlan_Type()
)
cpaePortAuthFailVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaePortAuthFailVlan.setStatus("current")
_CpaePortOperVlan_Type = VlanIndex
_CpaePortOperVlan_Object = MibTableColumn
cpaePortOperVlan = _CpaePortOperVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 7),
    _CpaePortOperVlan_Type()
)
cpaePortOperVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaePortOperVlan.setStatus("current")


class _CpaePortOperVlanType_Type(Integer32):
    """Custom type cpaePortOperVlanType based on Integer32"""
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
        *(("authFail", 4),
          ("guest", 3),
          ("none", 2),
          ("other", 1))
    )


_CpaePortOperVlanType_Type.__name__ = "Integer32"
_CpaePortOperVlanType_Object = MibTableColumn
cpaePortOperVlanType = _CpaePortOperVlanType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 8),
    _CpaePortOperVlanType_Type()
)
cpaePortOperVlanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaePortOperVlanType.setStatus("current")
_CpaeAuthFailVlanMaxAttempts_Type = Unsigned32
_CpaeAuthFailVlanMaxAttempts_Object = MibTableColumn
cpaeAuthFailVlanMaxAttempts = _CpaeAuthFailVlanMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 9),
    _CpaeAuthFailVlanMaxAttempts_Type()
)
cpaeAuthFailVlanMaxAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeAuthFailVlanMaxAttempts.setStatus("current")


class _CpaePortCapabilitiesEnabled_Type(Bits):
    """Custom type cpaePortCapabilitiesEnabled based on Bits"""
    namedValues = NamedValues(
        *(("authenticator", 0),
          ("supplicant", 1))
    )

_CpaePortCapabilitiesEnabled_Type.__name__ = "Bits"
_CpaePortCapabilitiesEnabled_Object = MibTableColumn
cpaePortCapabilitiesEnabled = _CpaePortCapabilitiesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 1, 1, 10),
    _CpaePortCapabilitiesEnabled_Type()
)
cpaePortCapabilitiesEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaePortCapabilitiesEnabled.setStatus("current")
_CpaeGuestVlanId_Type = VlanIndex
_CpaeGuestVlanId_Object = MibScalar
cpaeGuestVlanId = _CpaeGuestVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 2),
    _CpaeGuestVlanId_Type()
)
cpaeGuestVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeGuestVlanId.setStatus("deprecated")


class _CpaeShutdownTimeout_Type(Unsigned32):
    """Custom type cpaeShutdownTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpaeShutdownTimeout_Type.__name__ = "Unsigned32"
_CpaeShutdownTimeout_Object = MibScalar
cpaeShutdownTimeout = _CpaeShutdownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 3),
    _CpaeShutdownTimeout_Type()
)
cpaeShutdownTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeShutdownTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cpaeShutdownTimeout.setUnits("seconds")
_CpaeRadiusAccountingEnabled_Type = TruthValue
_CpaeRadiusAccountingEnabled_Object = MibScalar
cpaeRadiusAccountingEnabled = _CpaeRadiusAccountingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 4),
    _CpaeRadiusAccountingEnabled_Type()
)
cpaeRadiusAccountingEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeRadiusAccountingEnabled.setStatus("current")
_CpaeUserGroupTable_Object = MibTable
cpaeUserGroupTable = _CpaeUserGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5)
)
if mibBuilder.loadTexts:
    cpaeUserGroupTable.setStatus("current")
_CpaeUserGroupEntry_Object = MibTableRow
cpaeUserGroupEntry = _CpaeUserGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1)
)
cpaeUserGroupEntry.setIndexNames(
    (0, "CISCO-PAE-MIB", "cpaeUserGroupName"),
    (0, "CISCO-PAE-MIB", "cpaeUserGroupUserIndex"),
)
if mibBuilder.loadTexts:
    cpaeUserGroupEntry.setStatus("current")


class _CpaeUserGroupName_Type(SnmpAdminString):
    """Custom type cpaeUserGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_CpaeUserGroupName_Type.__name__ = "SnmpAdminString"
_CpaeUserGroupName_Object = MibTableColumn
cpaeUserGroupName = _CpaeUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1, 1),
    _CpaeUserGroupName_Type()
)
cpaeUserGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpaeUserGroupName.setStatus("current")
_CpaeUserGroupUserIndex_Type = Unsigned32
_CpaeUserGroupUserIndex_Object = MibTableColumn
cpaeUserGroupUserIndex = _CpaeUserGroupUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1, 2),
    _CpaeUserGroupUserIndex_Type()
)
cpaeUserGroupUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpaeUserGroupUserIndex.setStatus("current")
_CpaeUserGroupUserName_Type = SnmpAdminString
_CpaeUserGroupUserName_Object = MibTableColumn
cpaeUserGroupUserName = _CpaeUserGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1, 3),
    _CpaeUserGroupUserName_Type()
)
cpaeUserGroupUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeUserGroupUserName.setStatus("current")
_CpaeUserGroupUserAddrType_Type = InetAddressType
_CpaeUserGroupUserAddrType_Object = MibTableColumn
cpaeUserGroupUserAddrType = _CpaeUserGroupUserAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1, 4),
    _CpaeUserGroupUserAddrType_Type()
)
cpaeUserGroupUserAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeUserGroupUserAddrType.setStatus("current")
_CpaeUserGroupUserAddr_Type = InetAddress
_CpaeUserGroupUserAddr_Object = MibTableColumn
cpaeUserGroupUserAddr = _CpaeUserGroupUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1, 5),
    _CpaeUserGroupUserAddr_Type()
)
cpaeUserGroupUserAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeUserGroupUserAddr.setStatus("current")
_CpaeUserGroupUserInterface_Type = InterfaceIndex
_CpaeUserGroupUserInterface_Object = MibTableColumn
cpaeUserGroupUserInterface = _CpaeUserGroupUserInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1, 6),
    _CpaeUserGroupUserInterface_Type()
)
cpaeUserGroupUserInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeUserGroupUserInterface.setStatus("current")
_CpaeUserGroupUserVlan_Type = VlanIndex
_CpaeUserGroupUserVlan_Object = MibTableColumn
cpaeUserGroupUserVlan = _CpaeUserGroupUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 5, 1, 7),
    _CpaeUserGroupUserVlan_Type()
)
cpaeUserGroupUserVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeUserGroupUserVlan.setStatus("current")
_CpaeAuthFailUserTable_Object = MibTable
cpaeAuthFailUserTable = _CpaeAuthFailUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 6)
)
if mibBuilder.loadTexts:
    cpaeAuthFailUserTable.setStatus("current")
_CpaeAuthFailUserEntry_Object = MibTableRow
cpaeAuthFailUserEntry = _CpaeAuthFailUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 6, 1)
)
cpaeAuthFailUserEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    cpaeAuthFailUserEntry.setStatus("current")
_CpaeAuthFailUserName_Type = SnmpAdminString
_CpaeAuthFailUserName_Object = MibTableColumn
cpaeAuthFailUserName = _CpaeAuthFailUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 6, 1, 1),
    _CpaeAuthFailUserName_Type()
)
cpaeAuthFailUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeAuthFailUserName.setStatus("current")
_CpaeNotificationControl_ObjectIdentity = ObjectIdentity
cpaeNotificationControl = _CpaeNotificationControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 7)
)
_CpaeNoGuestVlanNotifEnable_Type = TruthValue
_CpaeNoGuestVlanNotifEnable_Object = MibScalar
cpaeNoGuestVlanNotifEnable = _CpaeNoGuestVlanNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 7, 1),
    _CpaeNoGuestVlanNotifEnable_Type()
)
cpaeNoGuestVlanNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeNoGuestVlanNotifEnable.setStatus("current")
_CpaeNoAuthFailVlanNotifEnable_Type = TruthValue
_CpaeNoAuthFailVlanNotifEnable_Object = MibScalar
cpaeNoAuthFailVlanNotifEnable = _CpaeNoAuthFailVlanNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 7, 2),
    _CpaeNoAuthFailVlanNotifEnable_Type()
)
cpaeNoAuthFailVlanNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeNoAuthFailVlanNotifEnable.setStatus("current")
_CpaeGuestVlanNotifEnable_Type = TruthValue
_CpaeGuestVlanNotifEnable_Object = MibScalar
cpaeGuestVlanNotifEnable = _CpaeGuestVlanNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 7, 3),
    _CpaeGuestVlanNotifEnable_Type()
)
cpaeGuestVlanNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeGuestVlanNotifEnable.setStatus("current")
_CpaeAuthFailVlanNotifEnable_Type = TruthValue
_CpaeAuthFailVlanNotifEnable_Object = MibScalar
cpaeAuthFailVlanNotifEnable = _CpaeAuthFailVlanNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 7, 4),
    _CpaeAuthFailVlanNotifEnable_Type()
)
cpaeAuthFailVlanNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeAuthFailVlanNotifEnable.setStatus("current")
_CpaeMacAuthBypass_ObjectIdentity = ObjectIdentity
cpaeMacAuthBypass = _CpaeMacAuthBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8)
)
_CpaeMacAuthBypassReAuthTimeout_Type = Unsigned32
_CpaeMacAuthBypassReAuthTimeout_Object = MibScalar
cpaeMacAuthBypassReAuthTimeout = _CpaeMacAuthBypassReAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 1),
    _CpaeMacAuthBypassReAuthTimeout_Type()
)
cpaeMacAuthBypassReAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassReAuthTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassReAuthTimeout.setUnits("seconds")
_CpaeMacAuthBypassReAuthEnabled_Type = TruthValue
_CpaeMacAuthBypassReAuthEnabled_Object = MibScalar
cpaeMacAuthBypassReAuthEnabled = _CpaeMacAuthBypassReAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 2),
    _CpaeMacAuthBypassReAuthEnabled_Type()
)
cpaeMacAuthBypassReAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassReAuthEnabled.setStatus("current")


class _CpaeMacAuthBypassViolation_Type(Integer32):
    """Custom type cpaeMacAuthBypassViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restrict", 1),
          ("shutdown", 2))
    )


_CpaeMacAuthBypassViolation_Type.__name__ = "Integer32"
_CpaeMacAuthBypassViolation_Object = MibScalar
cpaeMacAuthBypassViolation = _CpaeMacAuthBypassViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 3),
    _CpaeMacAuthBypassViolation_Type()
)
cpaeMacAuthBypassViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassViolation.setStatus("current")
_CpaeMacAuthBypassShutdownTimeout_Type = Unsigned32
_CpaeMacAuthBypassShutdownTimeout_Object = MibScalar
cpaeMacAuthBypassShutdownTimeout = _CpaeMacAuthBypassShutdownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 4),
    _CpaeMacAuthBypassShutdownTimeout_Type()
)
cpaeMacAuthBypassShutdownTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassShutdownTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassShutdownTimeout.setUnits("seconds")
_CpaeMacAuthBypassAuthFailTimeout_Type = Unsigned32
_CpaeMacAuthBypassAuthFailTimeout_Object = MibScalar
cpaeMacAuthBypassAuthFailTimeout = _CpaeMacAuthBypassAuthFailTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 5),
    _CpaeMacAuthBypassAuthFailTimeout_Type()
)
cpaeMacAuthBypassAuthFailTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassAuthFailTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassAuthFailTimeout.setUnits("seconds")
_CpaeMacAuthBypassPortTable_Object = MibTable
cpaeMacAuthBypassPortTable = _CpaeMacAuthBypassPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6)
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortTable.setStatus("current")
_CpaeMacAuthBypassPortEntry_Object = MibTableRow
cpaeMacAuthBypassPortEntry = _CpaeMacAuthBypassPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1)
)
cpaeMacAuthBypassPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortEntry.setStatus("current")
_CpaeMacAuthBypassPortEnabled_Type = TruthValue
_CpaeMacAuthBypassPortEnabled_Object = MibTableColumn
cpaeMacAuthBypassPortEnabled = _CpaeMacAuthBypassPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 1),
    _CpaeMacAuthBypassPortEnabled_Type()
)
cpaeMacAuthBypassPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortEnabled.setStatus("current")
_CpaeMacAuthBypassPortInitialize_Type = TruthValue
_CpaeMacAuthBypassPortInitialize_Object = MibTableColumn
cpaeMacAuthBypassPortInitialize = _CpaeMacAuthBypassPortInitialize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 2),
    _CpaeMacAuthBypassPortInitialize_Type()
)
cpaeMacAuthBypassPortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortInitialize.setStatus("current")
_CpaeMacAuthBypassPortReAuth_Type = TruthValue
_CpaeMacAuthBypassPortReAuth_Object = MibTableColumn
cpaeMacAuthBypassPortReAuth = _CpaeMacAuthBypassPortReAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 3),
    _CpaeMacAuthBypassPortReAuth_Type()
)
cpaeMacAuthBypassPortReAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortReAuth.setStatus("current")
_CpaeMacAuthBypassPortMacAddress_Type = MacAddress
_CpaeMacAuthBypassPortMacAddress_Object = MibTableColumn
cpaeMacAuthBypassPortMacAddress = _CpaeMacAuthBypassPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 4),
    _CpaeMacAuthBypassPortMacAddress_Type()
)
cpaeMacAuthBypassPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortMacAddress.setStatus("current")


class _CpaeMacAuthBypassPortAuthState_Type(Integer32):
    """Custom type cpaeMacAuthBypassPortAuthState based on Integer32"""
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
        *(("aaaFail", 7),
          ("authenticated", 4),
          ("authenticating", 3),
          ("fail", 5),
          ("finished", 6),
          ("ipAwaiting", 8),
          ("other", 1),
          ("policyConfig", 9),
          ("waiting", 2))
    )


_CpaeMacAuthBypassPortAuthState_Type.__name__ = "Integer32"
_CpaeMacAuthBypassPortAuthState_Object = MibTableColumn
cpaeMacAuthBypassPortAuthState = _CpaeMacAuthBypassPortAuthState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 5),
    _CpaeMacAuthBypassPortAuthState_Type()
)
cpaeMacAuthBypassPortAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortAuthState.setStatus("current")


class _CpaeMacAuthBypassPortTermAction_Type(Integer32):
    """Custom type cpaeMacAuthBypassPortTermAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 2),
          ("other", 1),
          ("reauth", 3))
    )


_CpaeMacAuthBypassPortTermAction_Type.__name__ = "Integer32"
_CpaeMacAuthBypassPortTermAction_Object = MibTableColumn
cpaeMacAuthBypassPortTermAction = _CpaeMacAuthBypassPortTermAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 6),
    _CpaeMacAuthBypassPortTermAction_Type()
)
cpaeMacAuthBypassPortTermAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortTermAction.setStatus("current")
_CpaeMacAuthBypassSessionTimeLeft_Type = Unsigned32
_CpaeMacAuthBypassSessionTimeLeft_Object = MibTableColumn
cpaeMacAuthBypassSessionTimeLeft = _CpaeMacAuthBypassSessionTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 7),
    _CpaeMacAuthBypassSessionTimeLeft_Type()
)
cpaeMacAuthBypassSessionTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassSessionTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassSessionTimeLeft.setUnits("seconds")


class _CpaeMacAuthBypassPortAuthMethod_Type(Integer32):
    """Custom type cpaeMacAuthBypassPortAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eap", 2),
          ("radius", 1))
    )


_CpaeMacAuthBypassPortAuthMethod_Type.__name__ = "Integer32"
_CpaeMacAuthBypassPortAuthMethod_Object = MibTableColumn
cpaeMacAuthBypassPortAuthMethod = _CpaeMacAuthBypassPortAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 8),
    _CpaeMacAuthBypassPortAuthMethod_Type()
)
cpaeMacAuthBypassPortAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortAuthMethod.setStatus("current")
_CpaeMacAuthBypassPortSessionId_Type = SnmpAdminString
_CpaeMacAuthBypassPortSessionId_Object = MibTableColumn
cpaeMacAuthBypassPortSessionId = _CpaeMacAuthBypassPortSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 9),
    _CpaeMacAuthBypassPortSessionId_Type()
)
cpaeMacAuthBypassPortSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortSessionId.setStatus("current")
_CpaeMacAuthBypassPortUrlRedirect_Type = SnmpAdminString
_CpaeMacAuthBypassPortUrlRedirect_Object = MibTableColumn
cpaeMacAuthBypassPortUrlRedirect = _CpaeMacAuthBypassPortUrlRedirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 10),
    _CpaeMacAuthBypassPortUrlRedirect_Type()
)
cpaeMacAuthBypassPortUrlRedirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortUrlRedirect.setStatus("current")


class _CpaeMacAuthBypassPortPostureTok_Type(CnnEouPostureTokenString):
    """Custom type cpaeMacAuthBypassPortPostureTok based on CnnEouPostureTokenString"""
    subtypeSpec = CnnEouPostureTokenString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CpaeMacAuthBypassPortPostureTok_Type.__name__ = "CnnEouPostureTokenString"
_CpaeMacAuthBypassPortPostureTok_Object = MibTableColumn
cpaeMacAuthBypassPortPostureTok = _CpaeMacAuthBypassPortPostureTok_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 6, 1, 11),
    _CpaeMacAuthBypassPortPostureTok_Type()
)
cpaeMacAuthBypassPortPostureTok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortPostureTok.setStatus("current")
_CpaeMacAuthBypassAcctEnable_Type = TruthValue
_CpaeMacAuthBypassAcctEnable_Object = MibScalar
cpaeMacAuthBypassAcctEnable = _CpaeMacAuthBypassAcctEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 7),
    _CpaeMacAuthBypassAcctEnable_Type()
)
cpaeMacAuthBypassAcctEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMacAuthBypassAcctEnable.setStatus("current")
_CpaeMabCriticalRecoveryDelay_Type = Unsigned32
_CpaeMabCriticalRecoveryDelay_Object = MibScalar
cpaeMabCriticalRecoveryDelay = _CpaeMabCriticalRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 8),
    _CpaeMabCriticalRecoveryDelay_Type()
)
cpaeMabCriticalRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMabCriticalRecoveryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cpaeMabCriticalRecoveryDelay.setUnits("milli-seconds")
_CpaeMabPortIpDevTrackConfTable_Object = MibTable
cpaeMabPortIpDevTrackConfTable = _CpaeMabPortIpDevTrackConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 9)
)
if mibBuilder.loadTexts:
    cpaeMabPortIpDevTrackConfTable.setStatus("current")
_CpaeMabPortIpDevTrackConfEntry_Object = MibTableRow
cpaeMabPortIpDevTrackConfEntry = _CpaeMabPortIpDevTrackConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 9, 1)
)
cpaeMabPortIpDevTrackConfEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    cpaeMabPortIpDevTrackConfEntry.setStatus("current")
_CpaeMabPortIpDevTrackEnabled_Type = TruthValue
_CpaeMabPortIpDevTrackEnabled_Object = MibTableColumn
cpaeMabPortIpDevTrackEnabled = _CpaeMabPortIpDevTrackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 8, 9, 1, 1),
    _CpaeMabPortIpDevTrackEnabled_Type()
)
cpaeMabPortIpDevTrackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeMabPortIpDevTrackEnabled.setStatus("current")
_CpaeWebAuth_ObjectIdentity = ObjectIdentity
cpaeWebAuth = _CpaeWebAuth_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9)
)
_CpaeWebAuthEnabled_Type = TruthValue
_CpaeWebAuthEnabled_Object = MibScalar
cpaeWebAuthEnabled = _CpaeWebAuthEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 1),
    _CpaeWebAuthEnabled_Type()
)
cpaeWebAuthEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthEnabled.setStatus("current")
_CpaeWebAuthSessionPeriod_Type = Unsigned32
_CpaeWebAuthSessionPeriod_Object = MibScalar
cpaeWebAuthSessionPeriod = _CpaeWebAuthSessionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 2),
    _CpaeWebAuthSessionPeriod_Type()
)
cpaeWebAuthSessionPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthSessionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpaeWebAuthSessionPeriod.setUnits("seconds")
_CpaeWebAuthLoginPage_Type = CiscoURLString
_CpaeWebAuthLoginPage_Object = MibScalar
cpaeWebAuthLoginPage = _CpaeWebAuthLoginPage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 3),
    _CpaeWebAuthLoginPage_Type()
)
cpaeWebAuthLoginPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthLoginPage.setStatus("current")
_CpaeWebAuthLoginFailedPage_Type = CiscoURLString
_CpaeWebAuthLoginFailedPage_Object = MibScalar
cpaeWebAuthLoginFailedPage = _CpaeWebAuthLoginFailedPage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 4),
    _CpaeWebAuthLoginFailedPage_Type()
)
cpaeWebAuthLoginFailedPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthLoginFailedPage.setStatus("current")
_CpaeWebAuthQuietPeriod_Type = Unsigned32
_CpaeWebAuthQuietPeriod_Object = MibScalar
cpaeWebAuthQuietPeriod = _CpaeWebAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 5),
    _CpaeWebAuthQuietPeriod_Type()
)
cpaeWebAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthQuietPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpaeWebAuthQuietPeriod.setUnits("seconds")
_CpaeWebAuthMaxRetries_Type = Unsigned32
_CpaeWebAuthMaxRetries_Object = MibScalar
cpaeWebAuthMaxRetries = _CpaeWebAuthMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 6),
    _CpaeWebAuthMaxRetries_Type()
)
cpaeWebAuthMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthMaxRetries.setStatus("current")
_CpaeWebAuthPortTable_Object = MibTable
cpaeWebAuthPortTable = _CpaeWebAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 7)
)
if mibBuilder.loadTexts:
    cpaeWebAuthPortTable.setStatus("current")
_CpaeWebAuthPortEntry_Object = MibTableRow
cpaeWebAuthPortEntry = _CpaeWebAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 7, 1)
)
cpaeWebAuthPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    cpaeWebAuthPortEntry.setStatus("current")
_CpaeWebAuthPortEnabled_Type = TruthValue
_CpaeWebAuthPortEnabled_Object = MibTableColumn
cpaeWebAuthPortEnabled = _CpaeWebAuthPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 7, 1, 1),
    _CpaeWebAuthPortEnabled_Type()
)
cpaeWebAuthPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthPortEnabled.setStatus("current")
_CpaeWebAuthPortInitialize_Type = TruthValue
_CpaeWebAuthPortInitialize_Object = MibTableColumn
cpaeWebAuthPortInitialize = _CpaeWebAuthPortInitialize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 7, 1, 2),
    _CpaeWebAuthPortInitialize_Type()
)
cpaeWebAuthPortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthPortInitialize.setStatus("current")
_CpaeWebAuthPortAaaFailPolicy_Type = CpgPolicyNameOrEmpty
_CpaeWebAuthPortAaaFailPolicy_Object = MibTableColumn
cpaeWebAuthPortAaaFailPolicy = _CpaeWebAuthPortAaaFailPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 7, 1, 3),
    _CpaeWebAuthPortAaaFailPolicy_Type()
)
cpaeWebAuthPortAaaFailPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthPortAaaFailPolicy.setStatus("current")
_CpaeWebAuthPortIpDevTrackEnabled_Type = TruthValue
_CpaeWebAuthPortIpDevTrackEnabled_Object = MibTableColumn
cpaeWebAuthPortIpDevTrackEnabled = _CpaeWebAuthPortIpDevTrackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 7, 1, 4),
    _CpaeWebAuthPortIpDevTrackEnabled_Type()
)
cpaeWebAuthPortIpDevTrackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthPortIpDevTrackEnabled.setStatus("current")
_CpaeWebAuthHostTable_Object = MibTable
cpaeWebAuthHostTable = _CpaeWebAuthHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8)
)
if mibBuilder.loadTexts:
    cpaeWebAuthHostTable.setStatus("current")
_CpaeWebAuthHostEntry_Object = MibTableRow
cpaeWebAuthHostEntry = _CpaeWebAuthHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8, 1)
)
cpaeWebAuthHostEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
    (0, "CISCO-PAE-MIB", "cpaeWebAuthHostAddrType"),
    (0, "CISCO-PAE-MIB", "cpaeWebAuthHostAddress"),
)
if mibBuilder.loadTexts:
    cpaeWebAuthHostEntry.setStatus("current")
_CpaeWebAuthHostAddrType_Type = InetAddressType
_CpaeWebAuthHostAddrType_Object = MibTableColumn
cpaeWebAuthHostAddrType = _CpaeWebAuthHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8, 1, 1),
    _CpaeWebAuthHostAddrType_Type()
)
cpaeWebAuthHostAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpaeWebAuthHostAddrType.setStatus("current")


class _CpaeWebAuthHostAddress_Type(InetAddress):
    """Custom type cpaeWebAuthHostAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CpaeWebAuthHostAddress_Type.__name__ = "InetAddress"
_CpaeWebAuthHostAddress_Object = MibTableColumn
cpaeWebAuthHostAddress = _CpaeWebAuthHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8, 1, 2),
    _CpaeWebAuthHostAddress_Type()
)
cpaeWebAuthHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpaeWebAuthHostAddress.setStatus("current")
_CpaeWebAuthAaaSessionPeriod_Type = Unsigned32
_CpaeWebAuthAaaSessionPeriod_Object = MibTableColumn
cpaeWebAuthAaaSessionPeriod = _CpaeWebAuthAaaSessionPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8, 1, 3),
    _CpaeWebAuthAaaSessionPeriod_Type()
)
cpaeWebAuthAaaSessionPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeWebAuthAaaSessionPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cpaeWebAuthAaaSessionPeriod.setUnits("seconds")
_CpaeWebAuthHostSessionTimeLeft_Type = Unsigned32
_CpaeWebAuthHostSessionTimeLeft_Object = MibTableColumn
cpaeWebAuthHostSessionTimeLeft = _CpaeWebAuthHostSessionTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8, 1, 4),
    _CpaeWebAuthHostSessionTimeLeft_Type()
)
cpaeWebAuthHostSessionTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeWebAuthHostSessionTimeLeft.setStatus("current")
if mibBuilder.loadTexts:
    cpaeWebAuthHostSessionTimeLeft.setUnits("seconds")


class _CpaeWebAuthHostState_Type(Integer32):
    """Custom type cpaeWebAuthHostState based on Integer32"""
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
        *(("aaaFail", 9),
          ("authFailed", 5),
          ("authenticated", 4),
          ("authenticating", 3),
          ("blackListed", 8),
          ("connecting", 2),
          ("initialize", 1),
          ("parseError", 6),
          ("sessionTimeout", 7))
    )


_CpaeWebAuthHostState_Type.__name__ = "Integer32"
_CpaeWebAuthHostState_Object = MibTableColumn
cpaeWebAuthHostState = _CpaeWebAuthHostState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8, 1, 5),
    _CpaeWebAuthHostState_Type()
)
cpaeWebAuthHostState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeWebAuthHostState.setStatus("current")
_CpaeWebAuthHostInitialize_Type = TruthValue
_CpaeWebAuthHostInitialize_Object = MibTableColumn
cpaeWebAuthHostInitialize = _CpaeWebAuthHostInitialize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 8, 1, 6),
    _CpaeWebAuthHostInitialize_Type()
)
cpaeWebAuthHostInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthHostInitialize.setStatus("current")
_CpaeWebAuthCriticalRecoveryDelay_Type = Unsigned32
_CpaeWebAuthCriticalRecoveryDelay_Object = MibScalar
cpaeWebAuthCriticalRecoveryDelay = _CpaeWebAuthCriticalRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 9),
    _CpaeWebAuthCriticalRecoveryDelay_Type()
)
cpaeWebAuthCriticalRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthCriticalRecoveryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cpaeWebAuthCriticalRecoveryDelay.setUnits("milli-seconds")


class _CpaeWebAuthUnAuthStateTimeout_Type(Unsigned32):
    """Custom type cpaeWebAuthUnAuthStateTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpaeWebAuthUnAuthStateTimeout_Type.__name__ = "Unsigned32"
_CpaeWebAuthUnAuthStateTimeout_Object = MibScalar
cpaeWebAuthUnAuthStateTimeout = _CpaeWebAuthUnAuthStateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 9, 10),
    _CpaeWebAuthUnAuthStateTimeout_Type()
)
cpaeWebAuthUnAuthStateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeWebAuthUnAuthStateTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cpaeWebAuthUnAuthStateTimeout.setUnits("minutes")
_CpaeAuthConfigTable_Object = MibTable
cpaeAuthConfigTable = _CpaeAuthConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10)
)
if mibBuilder.loadTexts:
    cpaeAuthConfigTable.setStatus("current")
_CpaeAuthConfigEntry_Object = MibTableRow
cpaeAuthConfigEntry = _CpaeAuthConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cpaeAuthConfigEntry.setStatus("current")
_CpaeAuthReAuthPeriodSrcAdmin_Type = ReAuthPeriodSource
_CpaeAuthReAuthPeriodSrcAdmin_Object = MibTableColumn
cpaeAuthReAuthPeriodSrcAdmin = _CpaeAuthReAuthPeriodSrcAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 1),
    _CpaeAuthReAuthPeriodSrcAdmin_Type()
)
cpaeAuthReAuthPeriodSrcAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeAuthReAuthPeriodSrcAdmin.setStatus("current")
_CpaeAuthReAuthPeriodSrcOper_Type = ReAuthPeriodSource
_CpaeAuthReAuthPeriodSrcOper_Object = MibTableColumn
cpaeAuthReAuthPeriodSrcOper = _CpaeAuthReAuthPeriodSrcOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 2),
    _CpaeAuthReAuthPeriodSrcOper_Type()
)
cpaeAuthReAuthPeriodSrcOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeAuthReAuthPeriodSrcOper.setStatus("current")
_CpaeAuthReAuthPeriodOper_Type = Unsigned32
_CpaeAuthReAuthPeriodOper_Object = MibTableColumn
cpaeAuthReAuthPeriodOper = _CpaeAuthReAuthPeriodOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 3),
    _CpaeAuthReAuthPeriodOper_Type()
)
cpaeAuthReAuthPeriodOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeAuthReAuthPeriodOper.setStatus("current")
if mibBuilder.loadTexts:
    cpaeAuthReAuthPeriodOper.setUnits("seconds")
_CpaeAuthTimeToNextReAuth_Type = Unsigned32
_CpaeAuthTimeToNextReAuth_Object = MibTableColumn
cpaeAuthTimeToNextReAuth = _CpaeAuthTimeToNextReAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 4),
    _CpaeAuthTimeToNextReAuth_Type()
)
cpaeAuthTimeToNextReAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeAuthTimeToNextReAuth.setStatus("current")
if mibBuilder.loadTexts:
    cpaeAuthTimeToNextReAuth.setUnits("seconds")


class _CpaeAuthReAuthAction_Type(Integer32):
    """Custom type cpaeAuthReAuthAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReAuth", 3),
          ("reAuth", 2),
          ("terminate", 1))
    )


_CpaeAuthReAuthAction_Type.__name__ = "Integer32"
_CpaeAuthReAuthAction_Object = MibTableColumn
cpaeAuthReAuthAction = _CpaeAuthReAuthAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 5),
    _CpaeAuthReAuthAction_Type()
)
cpaeAuthReAuthAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeAuthReAuthAction.setStatus("current")
_CpaeAuthReAuthMax_Type = Unsigned32
_CpaeAuthReAuthMax_Object = MibTableColumn
cpaeAuthReAuthMax = _CpaeAuthReAuthMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 6),
    _CpaeAuthReAuthMax_Type()
)
cpaeAuthReAuthMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeAuthReAuthMax.setStatus("current")
_CpaeAuthIabEnabled_Type = TruthValue
_CpaeAuthIabEnabled_Object = MibTableColumn
cpaeAuthIabEnabled = _CpaeAuthIabEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 7),
    _CpaeAuthIabEnabled_Type()
)
cpaeAuthIabEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeAuthIabEnabled.setStatus("current")
_CpaeAuthPaeState_Type = CpaeAuthState
_CpaeAuthPaeState_Object = MibTableColumn
cpaeAuthPaeState = _CpaeAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 10, 1, 8),
    _CpaeAuthPaeState_Type()
)
cpaeAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeAuthPaeState.setStatus("current")
_CpaeHostInfoTable_Object = MibTable
cpaeHostInfoTable = _CpaeHostInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11)
)
if mibBuilder.loadTexts:
    cpaeHostInfoTable.setStatus("current")
_CpaeHostInfoEntry_Object = MibTableRow
cpaeHostInfoEntry = _CpaeHostInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1)
)
cpaeHostInfoEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
    (0, "CISCO-PAE-MIB", "cpaeHostInfoHostIndex"),
)
if mibBuilder.loadTexts:
    cpaeHostInfoEntry.setStatus("current")
_CpaeHostInfoHostIndex_Type = Unsigned32
_CpaeHostInfoHostIndex_Object = MibTableColumn
cpaeHostInfoHostIndex = _CpaeHostInfoHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 1),
    _CpaeHostInfoHostIndex_Type()
)
cpaeHostInfoHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpaeHostInfoHostIndex.setStatus("current")
_CpaeHostInfoMacAddress_Type = MacAddress
_CpaeHostInfoMacAddress_Object = MibTableColumn
cpaeHostInfoMacAddress = _CpaeHostInfoMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 2),
    _CpaeHostInfoMacAddress_Type()
)
cpaeHostInfoMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostInfoMacAddress.setStatus("current")
_CpaeHostInfoPostureToken_Type = CnnEouPostureToken
_CpaeHostInfoPostureToken_Object = MibTableColumn
cpaeHostInfoPostureToken = _CpaeHostInfoPostureToken_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 3),
    _CpaeHostInfoPostureToken_Type()
)
cpaeHostInfoPostureToken.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostInfoPostureToken.setStatus("obsolete")
_CpaeHostInfoUserName_Type = SnmpAdminString
_CpaeHostInfoUserName_Object = MibTableColumn
cpaeHostInfoUserName = _CpaeHostInfoUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 4),
    _CpaeHostInfoUserName_Type()
)
cpaeHostInfoUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostInfoUserName.setStatus("current")
_CpaeHostInfoAddrType_Type = InetAddressType
_CpaeHostInfoAddrType_Object = MibTableColumn
cpaeHostInfoAddrType = _CpaeHostInfoAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 5),
    _CpaeHostInfoAddrType_Type()
)
cpaeHostInfoAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostInfoAddrType.setStatus("current")
_CpaeHostInfoAddr_Type = InetAddress
_CpaeHostInfoAddr_Object = MibTableColumn
cpaeHostInfoAddr = _CpaeHostInfoAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 6),
    _CpaeHostInfoAddr_Type()
)
cpaeHostInfoAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostInfoAddr.setStatus("current")
_CpaeHostPostureTokenStr_Type = CnnEouPostureTokenString
_CpaeHostPostureTokenStr_Object = MibTableColumn
cpaeHostPostureTokenStr = _CpaeHostPostureTokenStr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 7),
    _CpaeHostPostureTokenStr_Type()
)
cpaeHostPostureTokenStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostPostureTokenStr.setStatus("current")
_CpaeHostUrlRedirection_Type = SnmpAdminString
_CpaeHostUrlRedirection_Object = MibTableColumn
cpaeHostUrlRedirection = _CpaeHostUrlRedirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 8),
    _CpaeHostUrlRedirection_Type()
)
cpaeHostUrlRedirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostUrlRedirection.setStatus("current")
_CpaeHostAuthPaeState_Type = CpaeAuthState
_CpaeHostAuthPaeState_Object = MibTableColumn
cpaeHostAuthPaeState = _CpaeHostAuthPaeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 9),
    _CpaeHostAuthPaeState_Type()
)
cpaeHostAuthPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostAuthPaeState.setStatus("current")


class _CpaeHostBackendState_Type(Integer32):
    """Custom type cpaeHostBackendState based on Integer32"""
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
        *(("fail", 4),
          ("idle", 6),
          ("ignore", 8),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_CpaeHostBackendState_Type.__name__ = "Integer32"
_CpaeHostBackendState_Object = MibTableColumn
cpaeHostBackendState = _CpaeHostBackendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 10),
    _CpaeHostBackendState_Type()
)
cpaeHostBackendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostBackendState.setStatus("current")


class _CpaeHostSessionId_Type(OctetString):
    """Custom type cpaeHostSessionId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CpaeHostSessionId_Type.__name__ = "OctetString"
_CpaeHostSessionId_Object = MibTableColumn
cpaeHostSessionId = _CpaeHostSessionId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 11, 1, 11),
    _CpaeHostSessionId_Type()
)
cpaeHostSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeHostSessionId.setStatus("current")
_CpaePortEapolTestLimits_Type = Unsigned32
_CpaePortEapolTestLimits_Object = MibScalar
cpaePortEapolTestLimits = _CpaePortEapolTestLimits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 12),
    _CpaePortEapolTestLimits_Type()
)
cpaePortEapolTestLimits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaePortEapolTestLimits.setStatus("current")
_CpaePortEapolTestTable_Object = MibTable
cpaePortEapolTestTable = _CpaePortEapolTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 13)
)
if mibBuilder.loadTexts:
    cpaePortEapolTestTable.setStatus("current")
_CpaePortEapolTestEntry_Object = MibTableRow
cpaePortEapolTestEntry = _CpaePortEapolTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 13, 1)
)
cpaePortEapolTestEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    cpaePortEapolTestEntry.setStatus("current")


class _CpaePortEapolTestResult_Type(Integer32):
    """Custom type cpaePortEapolTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("capable", 3),
          ("inProgress", 1),
          ("notCapable", 2))
    )


_CpaePortEapolTestResult_Type.__name__ = "Integer32"
_CpaePortEapolTestResult_Object = MibTableColumn
cpaePortEapolTestResult = _CpaePortEapolTestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 13, 1, 1),
    _CpaePortEapolTestResult_Type()
)
cpaePortEapolTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaePortEapolTestResult.setStatus("current")
_CpaePortEapolTestStatus_Type = RowStatus
_CpaePortEapolTestStatus_Object = MibTableColumn
cpaePortEapolTestStatus = _CpaePortEapolTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 13, 1, 2),
    _CpaePortEapolTestStatus_Type()
)
cpaePortEapolTestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpaePortEapolTestStatus.setStatus("current")
_CpaeCriticalConfig_ObjectIdentity = ObjectIdentity
cpaeCriticalConfig = _CpaeCriticalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 14)
)
_CpaeCriticalEapolEnabled_Type = TruthValue
_CpaeCriticalEapolEnabled_Object = MibScalar
cpaeCriticalEapolEnabled = _CpaeCriticalEapolEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 14, 1),
    _CpaeCriticalEapolEnabled_Type()
)
cpaeCriticalEapolEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeCriticalEapolEnabled.setStatus("current")
_CpaeCriticalRecoveryDelay_Type = Unsigned32
_CpaeCriticalRecoveryDelay_Object = MibScalar
cpaeCriticalRecoveryDelay = _CpaeCriticalRecoveryDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 14, 2),
    _CpaeCriticalRecoveryDelay_Type()
)
cpaeCriticalRecoveryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeCriticalRecoveryDelay.setStatus("current")
if mibBuilder.loadTexts:
    cpaeCriticalRecoveryDelay.setUnits("milli-seconds")
_CpaePortIpDevTrackConfigTable_Object = MibTable
cpaePortIpDevTrackConfigTable = _CpaePortIpDevTrackConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 15)
)
if mibBuilder.loadTexts:
    cpaePortIpDevTrackConfigTable.setStatus("current")
_CpaePortIpDevTrackConfigEntry_Object = MibTableRow
cpaePortIpDevTrackConfigEntry = _CpaePortIpDevTrackConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 15, 1)
)
cpaePortIpDevTrackConfigEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    cpaePortIpDevTrackConfigEntry.setStatus("current")
_CpaePortIpDevTrackEnabled_Type = TruthValue
_CpaePortIpDevTrackEnabled_Object = MibTableColumn
cpaePortIpDevTrackEnabled = _CpaePortIpDevTrackEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 15, 1, 1),
    _CpaePortIpDevTrackEnabled_Type()
)
cpaePortIpDevTrackEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaePortIpDevTrackEnabled.setStatus("current")


class _CpaeGlobalAuthFailMaxAttempts_Type(Unsigned32):
    """Custom type cpaeGlobalAuthFailMaxAttempts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CpaeGlobalAuthFailMaxAttempts_Type.__name__ = "Unsigned32"
_CpaeGlobalAuthFailMaxAttempts_Object = MibScalar
cpaeGlobalAuthFailMaxAttempts = _CpaeGlobalAuthFailMaxAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 16),
    _CpaeGlobalAuthFailMaxAttempts_Type()
)
cpaeGlobalAuthFailMaxAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeGlobalAuthFailMaxAttempts.setStatus("current")


class _CpaeGlobalSecViolationAction_Type(Integer32):
    """Custom type cpaeGlobalSecViolationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restrict", 1),
          ("shutdown", 2))
    )


_CpaeGlobalSecViolationAction_Type.__name__ = "Integer32"
_CpaeGlobalSecViolationAction_Object = MibScalar
cpaeGlobalSecViolationAction = _CpaeGlobalSecViolationAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 17),
    _CpaeGlobalSecViolationAction_Type()
)
cpaeGlobalSecViolationAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeGlobalSecViolationAction.setStatus("current")
_CpaeDot1xSuppToGuestVlanAllowed_Type = TruthValue
_CpaeDot1xSuppToGuestVlanAllowed_Object = MibScalar
cpaeDot1xSuppToGuestVlanAllowed = _CpaeDot1xSuppToGuestVlanAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 18),
    _CpaeDot1xSuppToGuestVlanAllowed_Type()
)
cpaeDot1xSuppToGuestVlanAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeDot1xSuppToGuestVlanAllowed.setStatus("current")
_CpaeSupplicantObjects_ObjectIdentity = ObjectIdentity
cpaeSupplicantObjects = _CpaeSupplicantObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19)
)
_CpaeSuppPortTable_Object = MibTable
cpaeSuppPortTable = _CpaeSuppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 1)
)
if mibBuilder.loadTexts:
    cpaeSuppPortTable.setStatus("current")
_CpaeSuppPortEntry_Object = MibTableRow
cpaeSuppPortEntry = _CpaeSuppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 1, 1)
)
cpaeSuppPortEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
)
if mibBuilder.loadTexts:
    cpaeSuppPortEntry.setStatus("current")
_CpaeSuppPortCredentialProfileName_Type = SnmpAdminString
_CpaeSuppPortCredentialProfileName_Object = MibTableColumn
cpaeSuppPortCredentialProfileName = _CpaeSuppPortCredentialProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 1, 1, 1),
    _CpaeSuppPortCredentialProfileName_Type()
)
cpaeSuppPortCredentialProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeSuppPortCredentialProfileName.setStatus("current")
_CpaeSuppPortEapProfileName_Type = SnmpAdminString
_CpaeSuppPortEapProfileName_Object = MibTableColumn
cpaeSuppPortEapProfileName = _CpaeSuppPortEapProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 1, 1, 2),
    _CpaeSuppPortEapProfileName_Type()
)
cpaeSuppPortEapProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpaeSuppPortEapProfileName.setStatus("current")
_CpaeSuppHostInfoTable_Object = MibTable
cpaeSuppHostInfoTable = _CpaeSuppHostInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 2)
)
if mibBuilder.loadTexts:
    cpaeSuppHostInfoTable.setStatus("current")
_CpaeSuppHostInfoEntry_Object = MibTableRow
cpaeSuppHostInfoEntry = _CpaeSuppHostInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 2, 1)
)
cpaeSuppHostInfoEntry.setIndexNames(
    (0, "IEEE8021-PAE-MIB", "dot1xPaePortNumber"),
    (0, "CISCO-PAE-MIB", "cpaeSuppHostInfoSuppIndex"),
)
if mibBuilder.loadTexts:
    cpaeSuppHostInfoEntry.setStatus("current")


class _CpaeSuppHostInfoSuppIndex_Type(Unsigned32):
    """Custom type cpaeSuppHostInfoSuppIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpaeSuppHostInfoSuppIndex_Type.__name__ = "Unsigned32"
_CpaeSuppHostInfoSuppIndex_Object = MibTableColumn
cpaeSuppHostInfoSuppIndex = _CpaeSuppHostInfoSuppIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 2, 1, 1),
    _CpaeSuppHostInfoSuppIndex_Type()
)
cpaeSuppHostInfoSuppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpaeSuppHostInfoSuppIndex.setStatus("current")
_CpaeSuppHostAuthMacAddress_Type = MacAddress
_CpaeSuppHostAuthMacAddress_Object = MibTableColumn
cpaeSuppHostAuthMacAddress = _CpaeSuppHostAuthMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 2, 1, 2),
    _CpaeSuppHostAuthMacAddress_Type()
)
cpaeSuppHostAuthMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeSuppHostAuthMacAddress.setStatus("current")


class _CpaeSuppHostPaeState_Type(Integer32):
    """Custom type cpaeSuppHostPaeState based on Integer32"""
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
        *(("acquired", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 1),
          ("held", 7),
          ("logoff", 2),
          ("restart", 8),
          ("sForceAuth", 9),
          ("sForceUnauth", 10))
    )


_CpaeSuppHostPaeState_Type.__name__ = "Integer32"
_CpaeSuppHostPaeState_Object = MibTableColumn
cpaeSuppHostPaeState = _CpaeSuppHostPaeState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 2, 1, 3),
    _CpaeSuppHostPaeState_Type()
)
cpaeSuppHostPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeSuppHostPaeState.setStatus("current")


class _CpaeSuppHostBackendState_Type(Integer32):
    """Custom type cpaeSuppHostBackendState based on Integer32"""
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
        *(("fail", 6),
          ("idle", 2),
          ("initialize", 1),
          ("receive", 5),
          ("request", 3),
          ("response", 4),
          ("success", 7),
          ("timeout", 8))
    )


_CpaeSuppHostBackendState_Type.__name__ = "Integer32"
_CpaeSuppHostBackendState_Object = MibTableColumn
cpaeSuppHostBackendState = _CpaeSuppHostBackendState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 2, 1, 4),
    _CpaeSuppHostBackendState_Type()
)
cpaeSuppHostBackendState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeSuppHostBackendState.setStatus("current")
_CpaeSuppHostStatus_Type = PaeControlledPortStatus
_CpaeSuppHostStatus_Object = MibTableColumn
cpaeSuppHostStatus = _CpaeSuppHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 1, 19, 2, 1, 5),
    _CpaeSuppHostStatus_Type()
)
cpaeSuppHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpaeSuppHostStatus.setStatus("current")
_CpaeMIBConformance_ObjectIdentity = ObjectIdentity
cpaeMIBConformance = _CpaeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2)
)
_CpaeMIBCompliances_ObjectIdentity = ObjectIdentity
cpaeMIBCompliances = _CpaeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1)
)
_CpaeMIBGroups_ObjectIdentity = ObjectIdentity
cpaeMIBGroups = _CpaeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2)
)
dot1xPaePortEntry.registerAugmentions(
    ("CISCO-PAE-MIB",
     "cpaePortEntry")
)
cpaePortEntry.setIndexNames(*dot1xPaePortEntry.getIndexNames())
dot1xAuthConfigEntry.registerAugmentions(
    ("CISCO-PAE-MIB",
     "cpaeAuthConfigEntry")
)
cpaeAuthConfigEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())

# Managed Objects groups

cpaeMultipleHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 1)
)
cpaeMultipleHostGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeMultipleHost")
)
if mibBuilder.loadTexts:
    cpaeMultipleHostGroup.setStatus("deprecated")

cpaePortEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 2)
)
cpaePortEntryGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaePortMode")
)
if mibBuilder.loadTexts:
    cpaePortEntryGroup.setStatus("current")

cpaeGuestVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 3)
)
cpaeGuestVlanGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeGuestVlanId")
)
if mibBuilder.loadTexts:
    cpaeGuestVlanGroup.setStatus("deprecated")

cpaeGuestVlanGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 4)
)
cpaeGuestVlanGroup2.setObjects(
      *(("CISCO-PAE-MIB", "cpaeGuestVlanNumber"),
        ("CISCO-PAE-MIB", "cpaeInGuestVlan"))
)
if mibBuilder.loadTexts:
    cpaeGuestVlanGroup2.setStatus("deprecated")

cpaeShutdownTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 5)
)
cpaeShutdownTimeoutGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeShutdownTimeout"),
        ("CISCO-PAE-MIB", "cpaeShutdownTimeoutEnabled"))
)
if mibBuilder.loadTexts:
    cpaeShutdownTimeoutGroup.setStatus("current")

cpaeRadiusConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 6)
)
cpaeRadiusConfigGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeRadiusAccountingEnabled")
)
if mibBuilder.loadTexts:
    cpaeRadiusConfigGroup.setStatus("current")

cpaeUserGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 7)
)
cpaeUserGroupGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeUserGroupUserName"),
        ("CISCO-PAE-MIB", "cpaeUserGroupUserAddrType"),
        ("CISCO-PAE-MIB", "cpaeUserGroupUserAddr"),
        ("CISCO-PAE-MIB", "cpaeUserGroupUserInterface"),
        ("CISCO-PAE-MIB", "cpaeUserGroupUserVlan"))
)
if mibBuilder.loadTexts:
    cpaeUserGroupGroup.setStatus("current")

cpaeGuestVlanGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 8)
)
cpaeGuestVlanGroup3.setObjects(
    ("CISCO-PAE-MIB", "cpaeGuestVlanNumber")
)
if mibBuilder.loadTexts:
    cpaeGuestVlanGroup3.setStatus("current")

cpaePortOperVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 9)
)
cpaePortOperVlanGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaePortOperVlan"),
        ("CISCO-PAE-MIB", "cpaePortOperVlanType"))
)
if mibBuilder.loadTexts:
    cpaePortOperVlanGroup.setStatus("current")

cpaePortAuthFailVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 10)
)
cpaePortAuthFailVlanGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaePortAuthFailVlan"),
        ("CISCO-PAE-MIB", "cpaeAuthFailUserName"))
)
if mibBuilder.loadTexts:
    cpaePortAuthFailVlanGroup.setStatus("deprecated")

cpaeNoGuestVlanNotifEnableGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 11)
)
cpaeNoGuestVlanNotifEnableGrp.setObjects(
    ("CISCO-PAE-MIB", "cpaeNoGuestVlanNotifEnable")
)
if mibBuilder.loadTexts:
    cpaeNoGuestVlanNotifEnableGrp.setStatus("current")

cpaeNoAuthFailVlanNotifEnableGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 12)
)
cpaeNoAuthFailVlanNotifEnableGrp.setObjects(
    ("CISCO-PAE-MIB", "cpaeNoAuthFailVlanNotifEnable")
)
if mibBuilder.loadTexts:
    cpaeNoAuthFailVlanNotifEnableGrp.setStatus("current")

cpaeMacAuthBypassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 15)
)
cpaeMacAuthBypassGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeMacAuthBypassReAuthTimeout"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassReAuthEnabled"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassViolation"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassShutdownTimeout"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassAuthFailTimeout"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortEnabled"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortInitialize"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortReAuth"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortMacAddress"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortAuthState"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassAcctEnable"))
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassGroup.setStatus("deprecated")

cpaeWebAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 16)
)
cpaeWebAuthGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeWebAuthEnabled"),
        ("CISCO-PAE-MIB", "cpaeWebAuthSessionPeriod"),
        ("CISCO-PAE-MIB", "cpaeWebAuthLoginPage"),
        ("CISCO-PAE-MIB", "cpaeWebAuthLoginFailedPage"),
        ("CISCO-PAE-MIB", "cpaeWebAuthQuietPeriod"),
        ("CISCO-PAE-MIB", "cpaeWebAuthMaxRetries"),
        ("CISCO-PAE-MIB", "cpaeWebAuthPortEnabled"),
        ("CISCO-PAE-MIB", "cpaeWebAuthPortInitialize"),
        ("CISCO-PAE-MIB", "cpaeWebAuthAaaSessionPeriod"),
        ("CISCO-PAE-MIB", "cpaeWebAuthHostSessionTimeLeft"),
        ("CISCO-PAE-MIB", "cpaeWebAuthHostState"),
        ("CISCO-PAE-MIB", "cpaeWebAuthHostInitialize"))
)
if mibBuilder.loadTexts:
    cpaeWebAuthGroup.setStatus("current")

cpaeAuthConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 17)
)
cpaeAuthConfigGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeAuthReAuthPeriodSrcAdmin"),
        ("CISCO-PAE-MIB", "cpaeAuthReAuthPeriodSrcOper"),
        ("CISCO-PAE-MIB", "cpaeAuthReAuthPeriodOper"),
        ("CISCO-PAE-MIB", "cpaeAuthTimeToNextReAuth"),
        ("CISCO-PAE-MIB", "cpaeAuthReAuthAction"),
        ("CISCO-PAE-MIB", "cpaeAuthReAuthMax"),
        ("CISCO-PAE-MIB", "cpaeAuthIabEnabled"))
)
if mibBuilder.loadTexts:
    cpaeAuthConfigGroup.setStatus("deprecated")

cpaeHostInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 18)
)
cpaeHostInfoGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeHostInfoMacAddress"),
        ("CISCO-PAE-MIB", "cpaeHostInfoPostureToken"))
)
if mibBuilder.loadTexts:
    cpaeHostInfoGroup.setStatus("obsolete")

cpaeWebAuthAaaFailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 19)
)
cpaeWebAuthAaaFailGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeWebAuthPortAaaFailPolicy")
)
if mibBuilder.loadTexts:
    cpaeWebAuthAaaFailGroup.setStatus("current")

cpaeMacAuthBypassGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 20)
)
cpaeMacAuthBypassGroup2.setObjects(
      *(("CISCO-PAE-MIB", "cpaeMacAuthBypassPortTermAction"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassSessionTimeLeft"))
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassGroup2.setStatus("current")

cpaePortEapolTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 21)
)
cpaePortEapolTestGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaePortEapolTestLimits"),
        ("CISCO-PAE-MIB", "cpaePortEapolTestResult"),
        ("CISCO-PAE-MIB", "cpaePortEapolTestStatus"))
)
if mibBuilder.loadTexts:
    cpaePortEapolTestGroup.setStatus("current")

cpaeHostInfoGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 22)
)
cpaeHostInfoGroup2.setObjects(
    ("CISCO-PAE-MIB", "cpaeHostInfoMacAddress")
)
if mibBuilder.loadTexts:
    cpaeHostInfoGroup2.setStatus("current")

cpaeMacAuthBypassGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 23)
)
cpaeMacAuthBypassGroup3.setObjects(
    ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortAuthMethod")
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassGroup3.setStatus("current")

cpaePortAuthFailVlanGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 24)
)
cpaePortAuthFailVlanGroup2.setObjects(
    ("CISCO-PAE-MIB", "cpaeAuthFailVlanMaxAttempts")
)
if mibBuilder.loadTexts:
    cpaePortAuthFailVlanGroup2.setStatus("current")

cpaeAuthConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 25)
)
cpaeAuthConfigGroup2.setObjects(
    ("CISCO-PAE-MIB", "cpaeAuthPaeState")
)
if mibBuilder.loadTexts:
    cpaeAuthConfigGroup2.setStatus("current")

cpaeCriticalRecoveryDelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 26)
)
cpaeCriticalRecoveryDelayGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeCriticalRecoveryDelay")
)
if mibBuilder.loadTexts:
    cpaeCriticalRecoveryDelayGroup.setStatus("current")

cpaeAuthConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 27)
)
cpaeAuthConfigGroup3.setObjects(
      *(("CISCO-PAE-MIB", "cpaeAuthReAuthPeriodSrcAdmin"),
        ("CISCO-PAE-MIB", "cpaeAuthReAuthPeriodSrcOper"),
        ("CISCO-PAE-MIB", "cpaeAuthReAuthPeriodOper"),
        ("CISCO-PAE-MIB", "cpaeAuthTimeToNextReAuth"),
        ("CISCO-PAE-MIB", "cpaeAuthReAuthAction"))
)
if mibBuilder.loadTexts:
    cpaeAuthConfigGroup3.setStatus("current")

cpaeAuthConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 28)
)
cpaeAuthConfigGroup4.setObjects(
    ("CISCO-PAE-MIB", "cpaeAuthReAuthMax")
)
if mibBuilder.loadTexts:
    cpaeAuthConfigGroup4.setStatus("current")

cpaeAuthIabConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 29)
)
cpaeAuthIabConfigGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeAuthIabEnabled")
)
if mibBuilder.loadTexts:
    cpaeAuthIabConfigGroup.setStatus("current")

cpaeGlobalAuthFailVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 30)
)
cpaeGlobalAuthFailVlanGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeGlobalAuthFailMaxAttempts")
)
if mibBuilder.loadTexts:
    cpaeGlobalAuthFailVlanGroup.setStatus("current")

cpaeMacAuthBypassCriticalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 31)
)
cpaeMacAuthBypassCriticalGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeMabCriticalRecoveryDelay")
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassCriticalGroup.setStatus("current")

cpaeWebAuthCriticalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 32)
)
cpaeWebAuthCriticalGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeWebAuthCriticalRecoveryDelay")
)
if mibBuilder.loadTexts:
    cpaeWebAuthCriticalGroup.setStatus("current")

cpaeCriticalEapolConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 33)
)
cpaeCriticalEapolConfigGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeCriticalEapolEnabled")
)
if mibBuilder.loadTexts:
    cpaeCriticalEapolConfigGroup.setStatus("current")

cpaeHostPostureTokenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 34)
)
cpaeHostPostureTokenGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeHostPostureTokenStr")
)
if mibBuilder.loadTexts:
    cpaeHostPostureTokenGroup.setStatus("current")

cpaeMabAuditInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 35)
)
cpaeMabAuditInfoGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeMacAuthBypassPortSessionId"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortUrlRedirect"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortPostureTok"))
)
if mibBuilder.loadTexts:
    cpaeMabAuditInfoGroup.setStatus("current")

cpaeMabPortIpDevTrackConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 36)
)
cpaeMabPortIpDevTrackConfGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeMabPortIpDevTrackEnabled")
)
if mibBuilder.loadTexts:
    cpaeMabPortIpDevTrackConfGroup.setStatus("current")

cpaePortIpDevTrackConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 37)
)
cpaePortIpDevTrackConfGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaePortIpDevTrackEnabled")
)
if mibBuilder.loadTexts:
    cpaePortIpDevTrackConfGroup.setStatus("current")

cpaeHostUrlRedirectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 38)
)
cpaeHostUrlRedirectGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeHostUrlRedirection")
)
if mibBuilder.loadTexts:
    cpaeHostUrlRedirectGroup.setStatus("current")

cpaeWebAuthIpDevTrackingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 39)
)
cpaeWebAuthIpDevTrackingGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeWebAuthPortIpDevTrackEnabled")
)
if mibBuilder.loadTexts:
    cpaeWebAuthIpDevTrackingGroup.setStatus("current")

cpaeWebAuthUnAuthTimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 40)
)
cpaeWebAuthUnAuthTimeoutGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeWebAuthUnAuthStateTimeout")
)
if mibBuilder.loadTexts:
    cpaeWebAuthUnAuthTimeoutGroup.setStatus("current")

cpaeHostInfoGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 41)
)
cpaeHostInfoGroup3.setObjects(
      *(("CISCO-PAE-MIB", "cpaeHostInfoUserName"),
        ("CISCO-PAE-MIB", "cpaeHostInfoAddrType"),
        ("CISCO-PAE-MIB", "cpaeHostInfoAddr"))
)
if mibBuilder.loadTexts:
    cpaeHostInfoGroup3.setStatus("current")

cpaeGlobalSecViolationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 42)
)
cpaeGlobalSecViolationGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeGlobalSecViolationAction")
)
if mibBuilder.loadTexts:
    cpaeGlobalSecViolationGroup.setStatus("current")

cpaeMacAuthBypassPortEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 43)
)
cpaeMacAuthBypassPortEnableGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortEnabled")
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassPortEnableGroup.setStatus("current")

cpaeMacAuthBypassGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 44)
)
cpaeMacAuthBypassGroup4.setObjects(
      *(("CISCO-PAE-MIB", "cpaeMacAuthBypassReAuthEnabled"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassReAuthTimeout"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassViolation"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassShutdownTimeout"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassAuthFailTimeout"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortInitialize"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortReAuth"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortMacAddress"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassPortAuthState"),
        ("CISCO-PAE-MIB", "cpaeMacAuthBypassAcctEnable"))
)
if mibBuilder.loadTexts:
    cpaeMacAuthBypassGroup4.setStatus("current")

cpaeHostSessionIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 45)
)
cpaeHostSessionIdGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeHostSessionId")
)
if mibBuilder.loadTexts:
    cpaeHostSessionIdGroup.setStatus("current")

cpaeHostAuthInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 46)
)
cpaeHostAuthInfoGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeHostAuthPaeState"),
        ("CISCO-PAE-MIB", "cpaeHostBackendState"))
)
if mibBuilder.loadTexts:
    cpaeHostAuthInfoGroup.setStatus("current")

cpaePortCapabilitiesConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 47)
)
cpaePortCapabilitiesConfigGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaePortCapabilitiesEnabled")
)
if mibBuilder.loadTexts:
    cpaePortCapabilitiesConfigGroup.setStatus("current")

cpaeDot1xSuppToGuestVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 48)
)
cpaeDot1xSuppToGuestVlanGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeDot1xSuppToGuestVlanAllowed")
)
if mibBuilder.loadTexts:
    cpaeDot1xSuppToGuestVlanGroup.setStatus("current")

cpaeGuestVlanNotifEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 49)
)
cpaeGuestVlanNotifEnableGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeGuestVlanNotifEnable")
)
if mibBuilder.loadTexts:
    cpaeGuestVlanNotifEnableGroup.setStatus("current")

cpaeAuthFailVlanNotifEnableGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 51)
)
cpaeAuthFailVlanNotifEnableGrp.setObjects(
    ("CISCO-PAE-MIB", "cpaeAuthFailVlanNotifEnable")
)
if mibBuilder.loadTexts:
    cpaeAuthFailVlanNotifEnableGrp.setStatus("current")

cpaePortAuthFailVlanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 53)
)
cpaePortAuthFailVlanConfigGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaePortAuthFailVlan")
)
if mibBuilder.loadTexts:
    cpaePortAuthFailVlanConfigGroup.setStatus("current")

cpaePortAuthFailUserInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 54)
)
cpaePortAuthFailUserInfoGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeAuthFailUserName")
)
if mibBuilder.loadTexts:
    cpaePortAuthFailUserInfoGroup.setStatus("current")

cpaeSuppPortProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 55)
)
cpaeSuppPortProfileGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeSuppPortCredentialProfileName"),
        ("CISCO-PAE-MIB", "cpaeSuppPortEapProfileName"))
)
if mibBuilder.loadTexts:
    cpaeSuppPortProfileGroup.setStatus("current")

cpaeSuppHostInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 56)
)
cpaeSuppHostInfoGroup.setObjects(
      *(("CISCO-PAE-MIB", "cpaeSuppHostAuthMacAddress"),
        ("CISCO-PAE-MIB", "cpaeSuppHostPaeState"),
        ("CISCO-PAE-MIB", "cpaeSuppHostBackendState"),
        ("CISCO-PAE-MIB", "cpaeSuppHostStatus"))
)
if mibBuilder.loadTexts:
    cpaeSuppHostInfoGroup.setStatus("current")


# Notification objects

cpaeNoGuestVlanNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 0, 1)
)
cpaeNoGuestVlanNotif.setObjects(
    ("IEEE8021-PAE-MIB", "dot1xAuthPaeState")
)
if mibBuilder.loadTexts:
    cpaeNoGuestVlanNotif.setStatus(
        "current"
    )

cpaeNoAuthFailVlanNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 0, 2)
)
cpaeNoAuthFailVlanNotif.setObjects(
    ("IEEE8021-PAE-MIB", "dot1xAuthPaeState")
)
if mibBuilder.loadTexts:
    cpaeNoAuthFailVlanNotif.setStatus(
        "current"
    )

cpaeGuestVlanNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 0, 3)
)
cpaeGuestVlanNotif.setObjects(
      *(("CISCO-PAE-MIB", "cpaeGuestVlanNumber"),
        ("IEEE8021-PAE-MIB", "dot1xAuthPaeState"))
)
if mibBuilder.loadTexts:
    cpaeGuestVlanNotif.setStatus(
        "current"
    )

cpaeAuthFailVlanNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 0, 4)
)
cpaeAuthFailVlanNotif.setObjects(
      *(("CISCO-PAE-MIB", "cpaePortAuthFailVlan"),
        ("IEEE8021-PAE-MIB", "dot1xAuthPaeState"))
)
if mibBuilder.loadTexts:
    cpaeAuthFailVlanNotif.setStatus(
        "current"
    )


# Notifications groups

cpaeNoGuestVlanNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 13)
)
cpaeNoGuestVlanNotifGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeNoGuestVlanNotif")
)
if mibBuilder.loadTexts:
    cpaeNoGuestVlanNotifGroup.setStatus(
        "current"
    )

cpaeNoAuthFailVlanNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 14)
)
cpaeNoAuthFailVlanNotifGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeNoAuthFailVlanNotif")
)
if mibBuilder.loadTexts:
    cpaeNoAuthFailVlanNotifGroup.setStatus(
        "current"
    )

cpaeGuestVlanNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 50)
)
cpaeGuestVlanNotifGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeGuestVlanNotif")
)
if mibBuilder.loadTexts:
    cpaeGuestVlanNotifGroup.setStatus(
        "current"
    )

cpaeAuthFailVlanNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 2, 52)
)
cpaeAuthFailVlanNotifGroup.setObjects(
    ("CISCO-PAE-MIB", "cpaeAuthFailVlanNotif")
)
if mibBuilder.loadTexts:
    cpaeAuthFailVlanNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cpaeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpaeCompliance.setStatus(
        "deprecated"
    )

cpaeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cpaeCompliance2.setStatus(
        "deprecated"
    )

cpaeCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cpaeCompliance3.setStatus(
        "deprecated"
    )

cpaeCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cpaeCompliance4.setStatus(
        "deprecated"
    )

cpaeCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cpaeCompliance5.setStatus(
        "obsolete"
    )

cpaeCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 6)
)
if mibBuilder.loadTexts:
    cpaeCompliance6.setStatus(
        "deprecated"
    )

cpaeCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 7)
)
if mibBuilder.loadTexts:
    cpaeCompliance7.setStatus(
        "deprecated"
    )

cpaeCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 8)
)
if mibBuilder.loadTexts:
    cpaeCompliance8.setStatus(
        "deprecated"
    )

cpaeCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 9)
)
if mibBuilder.loadTexts:
    cpaeCompliance9.setStatus(
        "deprecated"
    )

cpaeCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 220, 2, 1, 10)
)
if mibBuilder.loadTexts:
    cpaeCompliance10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-PAE-MIB",
    **{"ReAuthPeriodSource": ReAuthPeriodSource,
       "CpaeAuthState": CpaeAuthState,
       "ciscoPaeMIB": ciscoPaeMIB,
       "cpaeMIBNotification": cpaeMIBNotification,
       "cpaeNoGuestVlanNotif": cpaeNoGuestVlanNotif,
       "cpaeNoAuthFailVlanNotif": cpaeNoAuthFailVlanNotif,
       "cpaeGuestVlanNotif": cpaeGuestVlanNotif,
       "cpaeAuthFailVlanNotif": cpaeAuthFailVlanNotif,
       "cpaeMIBObject": cpaeMIBObject,
       "cpaePortTable": cpaePortTable,
       "cpaePortEntry": cpaePortEntry,
       "cpaeMultipleHost": cpaeMultipleHost,
       "cpaePortMode": cpaePortMode,
       "cpaeGuestVlanNumber": cpaeGuestVlanNumber,
       "cpaeInGuestVlan": cpaeInGuestVlan,
       "cpaeShutdownTimeoutEnabled": cpaeShutdownTimeoutEnabled,
       "cpaePortAuthFailVlan": cpaePortAuthFailVlan,
       "cpaePortOperVlan": cpaePortOperVlan,
       "cpaePortOperVlanType": cpaePortOperVlanType,
       "cpaeAuthFailVlanMaxAttempts": cpaeAuthFailVlanMaxAttempts,
       "cpaePortCapabilitiesEnabled": cpaePortCapabilitiesEnabled,
       "cpaeGuestVlanId": cpaeGuestVlanId,
       "cpaeShutdownTimeout": cpaeShutdownTimeout,
       "cpaeRadiusAccountingEnabled": cpaeRadiusAccountingEnabled,
       "cpaeUserGroupTable": cpaeUserGroupTable,
       "cpaeUserGroupEntry": cpaeUserGroupEntry,
       "cpaeUserGroupName": cpaeUserGroupName,
       "cpaeUserGroupUserIndex": cpaeUserGroupUserIndex,
       "cpaeUserGroupUserName": cpaeUserGroupUserName,
       "cpaeUserGroupUserAddrType": cpaeUserGroupUserAddrType,
       "cpaeUserGroupUserAddr": cpaeUserGroupUserAddr,
       "cpaeUserGroupUserInterface": cpaeUserGroupUserInterface,
       "cpaeUserGroupUserVlan": cpaeUserGroupUserVlan,
       "cpaeAuthFailUserTable": cpaeAuthFailUserTable,
       "cpaeAuthFailUserEntry": cpaeAuthFailUserEntry,
       "cpaeAuthFailUserName": cpaeAuthFailUserName,
       "cpaeNotificationControl": cpaeNotificationControl,
       "cpaeNoGuestVlanNotifEnable": cpaeNoGuestVlanNotifEnable,
       "cpaeNoAuthFailVlanNotifEnable": cpaeNoAuthFailVlanNotifEnable,
       "cpaeGuestVlanNotifEnable": cpaeGuestVlanNotifEnable,
       "cpaeAuthFailVlanNotifEnable": cpaeAuthFailVlanNotifEnable,
       "cpaeMacAuthBypass": cpaeMacAuthBypass,
       "cpaeMacAuthBypassReAuthTimeout": cpaeMacAuthBypassReAuthTimeout,
       "cpaeMacAuthBypassReAuthEnabled": cpaeMacAuthBypassReAuthEnabled,
       "cpaeMacAuthBypassViolation": cpaeMacAuthBypassViolation,
       "cpaeMacAuthBypassShutdownTimeout": cpaeMacAuthBypassShutdownTimeout,
       "cpaeMacAuthBypassAuthFailTimeout": cpaeMacAuthBypassAuthFailTimeout,
       "cpaeMacAuthBypassPortTable": cpaeMacAuthBypassPortTable,
       "cpaeMacAuthBypassPortEntry": cpaeMacAuthBypassPortEntry,
       "cpaeMacAuthBypassPortEnabled": cpaeMacAuthBypassPortEnabled,
       "cpaeMacAuthBypassPortInitialize": cpaeMacAuthBypassPortInitialize,
       "cpaeMacAuthBypassPortReAuth": cpaeMacAuthBypassPortReAuth,
       "cpaeMacAuthBypassPortMacAddress": cpaeMacAuthBypassPortMacAddress,
       "cpaeMacAuthBypassPortAuthState": cpaeMacAuthBypassPortAuthState,
       "cpaeMacAuthBypassPortTermAction": cpaeMacAuthBypassPortTermAction,
       "cpaeMacAuthBypassSessionTimeLeft": cpaeMacAuthBypassSessionTimeLeft,
       "cpaeMacAuthBypassPortAuthMethod": cpaeMacAuthBypassPortAuthMethod,
       "cpaeMacAuthBypassPortSessionId": cpaeMacAuthBypassPortSessionId,
       "cpaeMacAuthBypassPortUrlRedirect": cpaeMacAuthBypassPortUrlRedirect,
       "cpaeMacAuthBypassPortPostureTok": cpaeMacAuthBypassPortPostureTok,
       "cpaeMacAuthBypassAcctEnable": cpaeMacAuthBypassAcctEnable,
       "cpaeMabCriticalRecoveryDelay": cpaeMabCriticalRecoveryDelay,
       "cpaeMabPortIpDevTrackConfTable": cpaeMabPortIpDevTrackConfTable,
       "cpaeMabPortIpDevTrackConfEntry": cpaeMabPortIpDevTrackConfEntry,
       "cpaeMabPortIpDevTrackEnabled": cpaeMabPortIpDevTrackEnabled,
       "cpaeWebAuth": cpaeWebAuth,
       "cpaeWebAuthEnabled": cpaeWebAuthEnabled,
       "cpaeWebAuthSessionPeriod": cpaeWebAuthSessionPeriod,
       "cpaeWebAuthLoginPage": cpaeWebAuthLoginPage,
       "cpaeWebAuthLoginFailedPage": cpaeWebAuthLoginFailedPage,
       "cpaeWebAuthQuietPeriod": cpaeWebAuthQuietPeriod,
       "cpaeWebAuthMaxRetries": cpaeWebAuthMaxRetries,
       "cpaeWebAuthPortTable": cpaeWebAuthPortTable,
       "cpaeWebAuthPortEntry": cpaeWebAuthPortEntry,
       "cpaeWebAuthPortEnabled": cpaeWebAuthPortEnabled,
       "cpaeWebAuthPortInitialize": cpaeWebAuthPortInitialize,
       "cpaeWebAuthPortAaaFailPolicy": cpaeWebAuthPortAaaFailPolicy,
       "cpaeWebAuthPortIpDevTrackEnabled": cpaeWebAuthPortIpDevTrackEnabled,
       "cpaeWebAuthHostTable": cpaeWebAuthHostTable,
       "cpaeWebAuthHostEntry": cpaeWebAuthHostEntry,
       "cpaeWebAuthHostAddrType": cpaeWebAuthHostAddrType,
       "cpaeWebAuthHostAddress": cpaeWebAuthHostAddress,
       "cpaeWebAuthAaaSessionPeriod": cpaeWebAuthAaaSessionPeriod,
       "cpaeWebAuthHostSessionTimeLeft": cpaeWebAuthHostSessionTimeLeft,
       "cpaeWebAuthHostState": cpaeWebAuthHostState,
       "cpaeWebAuthHostInitialize": cpaeWebAuthHostInitialize,
       "cpaeWebAuthCriticalRecoveryDelay": cpaeWebAuthCriticalRecoveryDelay,
       "cpaeWebAuthUnAuthStateTimeout": cpaeWebAuthUnAuthStateTimeout,
       "cpaeAuthConfigTable": cpaeAuthConfigTable,
       "cpaeAuthConfigEntry": cpaeAuthConfigEntry,
       "cpaeAuthReAuthPeriodSrcAdmin": cpaeAuthReAuthPeriodSrcAdmin,
       "cpaeAuthReAuthPeriodSrcOper": cpaeAuthReAuthPeriodSrcOper,
       "cpaeAuthReAuthPeriodOper": cpaeAuthReAuthPeriodOper,
       "cpaeAuthTimeToNextReAuth": cpaeAuthTimeToNextReAuth,
       "cpaeAuthReAuthAction": cpaeAuthReAuthAction,
       "cpaeAuthReAuthMax": cpaeAuthReAuthMax,
       "cpaeAuthIabEnabled": cpaeAuthIabEnabled,
       "cpaeAuthPaeState": cpaeAuthPaeState,
       "cpaeHostInfoTable": cpaeHostInfoTable,
       "cpaeHostInfoEntry": cpaeHostInfoEntry,
       "cpaeHostInfoHostIndex": cpaeHostInfoHostIndex,
       "cpaeHostInfoMacAddress": cpaeHostInfoMacAddress,
       "cpaeHostInfoPostureToken": cpaeHostInfoPostureToken,
       "cpaeHostInfoUserName": cpaeHostInfoUserName,
       "cpaeHostInfoAddrType": cpaeHostInfoAddrType,
       "cpaeHostInfoAddr": cpaeHostInfoAddr,
       "cpaeHostPostureTokenStr": cpaeHostPostureTokenStr,
       "cpaeHostUrlRedirection": cpaeHostUrlRedirection,
       "cpaeHostAuthPaeState": cpaeHostAuthPaeState,
       "cpaeHostBackendState": cpaeHostBackendState,
       "cpaeHostSessionId": cpaeHostSessionId,
       "cpaePortEapolTestLimits": cpaePortEapolTestLimits,
       "cpaePortEapolTestTable": cpaePortEapolTestTable,
       "cpaePortEapolTestEntry": cpaePortEapolTestEntry,
       "cpaePortEapolTestResult": cpaePortEapolTestResult,
       "cpaePortEapolTestStatus": cpaePortEapolTestStatus,
       "cpaeCriticalConfig": cpaeCriticalConfig,
       "cpaeCriticalEapolEnabled": cpaeCriticalEapolEnabled,
       "cpaeCriticalRecoveryDelay": cpaeCriticalRecoveryDelay,
       "cpaePortIpDevTrackConfigTable": cpaePortIpDevTrackConfigTable,
       "cpaePortIpDevTrackConfigEntry": cpaePortIpDevTrackConfigEntry,
       "cpaePortIpDevTrackEnabled": cpaePortIpDevTrackEnabled,
       "cpaeGlobalAuthFailMaxAttempts": cpaeGlobalAuthFailMaxAttempts,
       "cpaeGlobalSecViolationAction": cpaeGlobalSecViolationAction,
       "cpaeDot1xSuppToGuestVlanAllowed": cpaeDot1xSuppToGuestVlanAllowed,
       "cpaeSupplicantObjects": cpaeSupplicantObjects,
       "cpaeSuppPortTable": cpaeSuppPortTable,
       "cpaeSuppPortEntry": cpaeSuppPortEntry,
       "cpaeSuppPortCredentialProfileName": cpaeSuppPortCredentialProfileName,
       "cpaeSuppPortEapProfileName": cpaeSuppPortEapProfileName,
       "cpaeSuppHostInfoTable": cpaeSuppHostInfoTable,
       "cpaeSuppHostInfoEntry": cpaeSuppHostInfoEntry,
       "cpaeSuppHostInfoSuppIndex": cpaeSuppHostInfoSuppIndex,
       "cpaeSuppHostAuthMacAddress": cpaeSuppHostAuthMacAddress,
       "cpaeSuppHostPaeState": cpaeSuppHostPaeState,
       "cpaeSuppHostBackendState": cpaeSuppHostBackendState,
       "cpaeSuppHostStatus": cpaeSuppHostStatus,
       "cpaeMIBConformance": cpaeMIBConformance,
       "cpaeMIBCompliances": cpaeMIBCompliances,
       "cpaeCompliance": cpaeCompliance,
       "cpaeCompliance2": cpaeCompliance2,
       "cpaeCompliance3": cpaeCompliance3,
       "cpaeCompliance4": cpaeCompliance4,
       "cpaeCompliance5": cpaeCompliance5,
       "cpaeCompliance6": cpaeCompliance6,
       "cpaeCompliance7": cpaeCompliance7,
       "cpaeCompliance8": cpaeCompliance8,
       "cpaeCompliance9": cpaeCompliance9,
       "cpaeCompliance10": cpaeCompliance10,
       "cpaeMIBGroups": cpaeMIBGroups,
       "cpaeMultipleHostGroup": cpaeMultipleHostGroup,
       "cpaePortEntryGroup": cpaePortEntryGroup,
       "cpaeGuestVlanGroup": cpaeGuestVlanGroup,
       "cpaeGuestVlanGroup2": cpaeGuestVlanGroup2,
       "cpaeShutdownTimeoutGroup": cpaeShutdownTimeoutGroup,
       "cpaeRadiusConfigGroup": cpaeRadiusConfigGroup,
       "cpaeUserGroupGroup": cpaeUserGroupGroup,
       "cpaeGuestVlanGroup3": cpaeGuestVlanGroup3,
       "cpaePortOperVlanGroup": cpaePortOperVlanGroup,
       "cpaePortAuthFailVlanGroup": cpaePortAuthFailVlanGroup,
       "cpaeNoGuestVlanNotifEnableGrp": cpaeNoGuestVlanNotifEnableGrp,
       "cpaeNoAuthFailVlanNotifEnableGrp": cpaeNoAuthFailVlanNotifEnableGrp,
       "cpaeNoGuestVlanNotifGroup": cpaeNoGuestVlanNotifGroup,
       "cpaeNoAuthFailVlanNotifGroup": cpaeNoAuthFailVlanNotifGroup,
       "cpaeMacAuthBypassGroup": cpaeMacAuthBypassGroup,
       "cpaeWebAuthGroup": cpaeWebAuthGroup,
       "cpaeAuthConfigGroup": cpaeAuthConfigGroup,
       "cpaeHostInfoGroup": cpaeHostInfoGroup,
       "cpaeWebAuthAaaFailGroup": cpaeWebAuthAaaFailGroup,
       "cpaeMacAuthBypassGroup2": cpaeMacAuthBypassGroup2,
       "cpaePortEapolTestGroup": cpaePortEapolTestGroup,
       "cpaeHostInfoGroup2": cpaeHostInfoGroup2,
       "cpaeMacAuthBypassGroup3": cpaeMacAuthBypassGroup3,
       "cpaePortAuthFailVlanGroup2": cpaePortAuthFailVlanGroup2,
       "cpaeAuthConfigGroup2": cpaeAuthConfigGroup2,
       "cpaeCriticalRecoveryDelayGroup": cpaeCriticalRecoveryDelayGroup,
       "cpaeAuthConfigGroup3": cpaeAuthConfigGroup3,
       "cpaeAuthConfigGroup4": cpaeAuthConfigGroup4,
       "cpaeAuthIabConfigGroup": cpaeAuthIabConfigGroup,
       "cpaeGlobalAuthFailVlanGroup": cpaeGlobalAuthFailVlanGroup,
       "cpaeMacAuthBypassCriticalGroup": cpaeMacAuthBypassCriticalGroup,
       "cpaeWebAuthCriticalGroup": cpaeWebAuthCriticalGroup,
       "cpaeCriticalEapolConfigGroup": cpaeCriticalEapolConfigGroup,
       "cpaeHostPostureTokenGroup": cpaeHostPostureTokenGroup,
       "cpaeMabAuditInfoGroup": cpaeMabAuditInfoGroup,
       "cpaeMabPortIpDevTrackConfGroup": cpaeMabPortIpDevTrackConfGroup,
       "cpaePortIpDevTrackConfGroup": cpaePortIpDevTrackConfGroup,
       "cpaeHostUrlRedirectGroup": cpaeHostUrlRedirectGroup,
       "cpaeWebAuthIpDevTrackingGroup": cpaeWebAuthIpDevTrackingGroup,
       "cpaeWebAuthUnAuthTimeoutGroup": cpaeWebAuthUnAuthTimeoutGroup,
       "cpaeHostInfoGroup3": cpaeHostInfoGroup3,
       "cpaeGlobalSecViolationGroup": cpaeGlobalSecViolationGroup,
       "cpaeMacAuthBypassPortEnableGroup": cpaeMacAuthBypassPortEnableGroup,
       "cpaeMacAuthBypassGroup4": cpaeMacAuthBypassGroup4,
       "cpaeHostSessionIdGroup": cpaeHostSessionIdGroup,
       "cpaeHostAuthInfoGroup": cpaeHostAuthInfoGroup,
       "cpaePortCapabilitiesConfigGroup": cpaePortCapabilitiesConfigGroup,
       "cpaeDot1xSuppToGuestVlanGroup": cpaeDot1xSuppToGuestVlanGroup,
       "cpaeGuestVlanNotifEnableGroup": cpaeGuestVlanNotifEnableGroup,
       "cpaeGuestVlanNotifGroup": cpaeGuestVlanNotifGroup,
       "cpaeAuthFailVlanNotifEnableGrp": cpaeAuthFailVlanNotifEnableGrp,
       "cpaeAuthFailVlanNotifGroup": cpaeAuthFailVlanNotifGroup,
       "cpaePortAuthFailVlanConfigGroup": cpaePortAuthFailVlanConfigGroup,
       "cpaePortAuthFailUserInfoGroup": cpaePortAuthFailUserInfoGroup,
       "cpaeSuppPortProfileGroup": cpaeSuppPortProfileGroup,
       "cpaeSuppHostInfoGroup": cpaeSuppHostInfoGroup}
)
