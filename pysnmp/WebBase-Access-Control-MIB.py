# SNMP MIB module (WebBase-Access-Control-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WebBase-Access-Control-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:32 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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


# MODULE-IDENTITY

swWACMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 27)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwWACCtrl_ObjectIdentity = ObjectIdentity
swWACCtrl = _SwWACCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1)
)


class _SwWebAuthAdminState_Type(Integer32):
    """Custom type swWebAuthAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwWebAuthAdminState_Type.__name__ = "Integer32"
_SwWebAuthAdminState_Object = MibScalar
swWebAuthAdminState = _SwWebAuthAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 1),
    _SwWebAuthAdminState_Type()
)
swWebAuthAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWebAuthAdminState.setStatus("current")


class _SwWebAuthMethod_Type(Integer32):
    """Custom type swWebAuthMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2))
    )


_SwWebAuthMethod_Type.__name__ = "Integer32"
_SwWebAuthMethod_Object = MibScalar
swWebAuthMethod = _SwWebAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 2),
    _SwWebAuthMethod_Type()
)
swWebAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWebAuthMethod.setStatus("current")


class _SwWebAuthVlanName_Type(DisplayString):
    """Custom type swWebAuthVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwWebAuthVlanName_Type.__name__ = "DisplayString"
_SwWebAuthVlanName_Object = MibScalar
swWebAuthVlanName = _SwWebAuthVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 3),
    _SwWebAuthVlanName_Type()
)
swWebAuthVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWebAuthVlanName.setStatus("obsolete")


class _SwWebAuthAllPortstate_Type(Integer32):
    """Custom type swWebAuthAllPortstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwWebAuthAllPortstate_Type.__name__ = "Integer32"
_SwWebAuthAllPortstate_Object = MibScalar
swWebAuthAllPortstate = _SwWebAuthAllPortstate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 4),
    _SwWebAuthAllPortstate_Type()
)
swWebAuthAllPortstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWebAuthAllPortstate.setStatus("obsolete")


class _SwWebAuthDefaultredirpath_Type(DisplayString):
    """Custom type swWebAuthDefaultredirpath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwWebAuthDefaultredirpath_Type.__name__ = "DisplayString"
_SwWebAuthDefaultredirpath_Object = MibScalar
swWebAuthDefaultredirpath = _SwWebAuthDefaultredirpath_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 5),
    _SwWebAuthDefaultredirpath_Type()
)
swWebAuthDefaultredirpath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWebAuthDefaultredirpath.setStatus("current")


class _SwWebAuthLogouttimer_Type(Integer32):
    """Custom type swWebAuthLogouttimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SwWebAuthLogouttimer_Type.__name__ = "Integer32"
_SwWebAuthLogouttimer_Object = MibScalar
swWebAuthLogouttimer = _SwWebAuthLogouttimer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 6),
    _SwWebAuthLogouttimer_Type()
)
swWebAuthLogouttimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWebAuthLogouttimer.setStatus("obsolete")
_SwWACVirtualIpAddr_Type = IpAddress
_SwWACVirtualIpAddr_Object = MibScalar
swWACVirtualIpAddr = _SwWACVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 7),
    _SwWACVirtualIpAddr_Type()
)
swWACVirtualIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACVirtualIpAddr.setStatus("current")


class _SwWACSwitchHttpProtocol_Type(Integer32):
    """Custom type swWACSwitchHttpProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 1),
          ("https", 2))
    )


_SwWACSwitchHttpProtocol_Type.__name__ = "Integer32"
_SwWACSwitchHttpProtocol_Object = MibScalar
swWACSwitchHttpProtocol = _SwWACSwitchHttpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 8),
    _SwWACSwitchHttpProtocol_Type()
)
swWACSwitchHttpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACSwitchHttpProtocol.setStatus("current")


class _SwWACSwitchHttpPort_Type(Integer32):
    """Custom type swWACSwitchHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwWACSwitchHttpPort_Type.__name__ = "Integer32"
_SwWACSwitchHttpPort_Object = MibScalar
swWACSwitchHttpPort = _SwWACSwitchHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 9),
    _SwWACSwitchHttpPort_Type()
)
swWACSwitchHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACSwitchHttpPort.setStatus("current")


class _SwWACAuthFailOverState_Type(Integer32):
    """Custom type swWACAuthFailOverState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwWACAuthFailOverState_Type.__name__ = "Integer32"
_SwWACAuthFailOverState_Object = MibScalar
swWACAuthFailOverState = _SwWACAuthFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 10),
    _SwWACAuthFailOverState_Type()
)
swWACAuthFailOverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACAuthFailOverState.setStatus("current")


class _SwWACRadiusAuthorizationState_Type(Integer32):
    """Custom type swWACRadiusAuthorizationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwWACRadiusAuthorizationState_Type.__name__ = "Integer32"
_SwWACRadiusAuthorizationState_Object = MibScalar
swWACRadiusAuthorizationState = _SwWACRadiusAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 11),
    _SwWACRadiusAuthorizationState_Type()
)
swWACRadiusAuthorizationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACRadiusAuthorizationState.setStatus("current")


class _SwWACLocalAuthorizationState_Type(Integer32):
    """Custom type swWACLocalAuthorizationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwWACLocalAuthorizationState_Type.__name__ = "Integer32"
_SwWACLocalAuthorizationState_Object = MibScalar
swWACLocalAuthorizationState = _SwWACLocalAuthorizationState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 12),
    _SwWACLocalAuthorizationState_Type()
)
swWACLocalAuthorizationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACLocalAuthorizationState.setStatus("current")


class _SwWACAuthClearDefaultredirpath_Type(Integer32):
    """Custom type swWACAuthClearDefaultredirpath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwWACAuthClearDefaultredirpath_Type.__name__ = "Integer32"
_SwWACAuthClearDefaultredirpath_Object = MibScalar
swWACAuthClearDefaultredirpath = _SwWACAuthClearDefaultredirpath_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 13),
    _SwWACAuthClearDefaultredirpath_Type()
)
swWACAuthClearDefaultredirpath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACAuthClearDefaultredirpath.setStatus("current")
_SwWACVirtualIPv6Addr_Type = Ipv6Address
_SwWACVirtualIPv6Addr_Object = MibScalar
swWACVirtualIPv6Addr = _SwWACVirtualIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 1, 14),
    _SwWACVirtualIPv6Addr_Type()
)
swWACVirtualIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACVirtualIPv6Addr.setStatus("current")
_SwWACInfo_ObjectIdentity = ObjectIdentity
swWACInfo = _SwWACInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2)
)
_SwWACAuthInfoTable_Object = MibTable
swWACAuthInfoTable = _SwWACAuthInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1)
)
if mibBuilder.loadTexts:
    swWACAuthInfoTable.setStatus("current")
_SwWACAuthInfoEntry_Object = MibTableRow
swWACAuthInfoEntry = _SwWACAuthInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1)
)
swWACAuthInfoEntry.setIndexNames(
    (0, "WebBase-Access-Control-MIB", "swWACAuthInfoPort"),
    (0, "WebBase-Access-Control-MIB", "swWACAuthInfoAuthStatus"),
    (0, "WebBase-Access-Control-MIB", "swWACAuthInfoMACAddr"),
)
if mibBuilder.loadTexts:
    swWACAuthInfoEntry.setStatus("current")
_SwWACAuthInfoPort_Type = Integer32
_SwWACAuthInfoPort_Object = MibTableColumn
swWACAuthInfoPort = _SwWACAuthInfoPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 1),
    _SwWACAuthInfoPort_Type()
)
swWACAuthInfoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoPort.setStatus("current")


class _SwWACAuthInfoAuthStatus_Type(Integer32):
    """Custom type swWACAuthInfoAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 1),
          ("authenticating", 2),
          ("blocked", 3))
    )


_SwWACAuthInfoAuthStatus_Type.__name__ = "Integer32"
_SwWACAuthInfoAuthStatus_Object = MibTableColumn
swWACAuthInfoAuthStatus = _SwWACAuthInfoAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 2),
    _SwWACAuthInfoAuthStatus_Type()
)
swWACAuthInfoAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoAuthStatus.setStatus("current")
_SwWACAuthInfoMACAddr_Type = MacAddress
_SwWACAuthInfoMACAddr_Object = MibTableColumn
swWACAuthInfoMACAddr = _SwWACAuthInfoMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 3),
    _SwWACAuthInfoMACAddr_Type()
)
swWACAuthInfoMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoMACAddr.setStatus("current")
_SwWACAuthInfoVID_Type = VlanId
_SwWACAuthInfoVID_Object = MibTableColumn
swWACAuthInfoVID = _SwWACAuthInfoVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 4),
    _SwWACAuthInfoVID_Type()
)
swWACAuthInfoVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoVID.setStatus("current")
_SwWACAuthInfoRemainAgeTime_Type = Integer32
_SwWACAuthInfoRemainAgeTime_Object = MibTableColumn
swWACAuthInfoRemainAgeTime = _SwWACAuthInfoRemainAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 5),
    _SwWACAuthInfoRemainAgeTime_Type()
)
swWACAuthInfoRemainAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoRemainAgeTime.setStatus("current")
_SwWACAuthInfoIdleTime_Type = Integer32
_SwWACAuthInfoIdleTime_Object = MibTableColumn
swWACAuthInfoIdleTime = _SwWACAuthInfoIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 6),
    _SwWACAuthInfoIdleTime_Type()
)
swWACAuthInfoIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoIdleTime.setStatus("current")
_SwWACAuthInfoBlockTime_Type = Integer32
_SwWACAuthInfoBlockTime_Object = MibTableColumn
swWACAuthInfoBlockTime = _SwWACAuthInfoBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 7),
    _SwWACAuthInfoBlockTime_Type()
)
swWACAuthInfoBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoBlockTime.setStatus("current")


class _SwWACAuthInfoStatus_Type(Integer32):
    """Custom type swWACAuthInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_SwWACAuthInfoStatus_Type.__name__ = "Integer32"
_SwWACAuthInfoStatus_Object = MibTableColumn
swWACAuthInfoStatus = _SwWACAuthInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 8),
    _SwWACAuthInfoStatus_Type()
)
swWACAuthInfoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACAuthInfoStatus.setStatus("current")
_SwWACAuthInfoPriority_Type = Integer32
_SwWACAuthInfoPriority_Object = MibTableColumn
swWACAuthInfoPriority = _SwWACAuthInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 1, 1, 9),
    _SwWACAuthInfoPriority_Type()
)
swWACAuthInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthInfoPriority.setStatus("current")
_SwWACAuthStateTable_Object = MibTable
swWACAuthStateTable = _SwWACAuthStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2)
)
if mibBuilder.loadTexts:
    swWACAuthStateTable.setStatus("current")
_SwWACAuthStateEntry_Object = MibTableRow
swWACAuthStateEntry = _SwWACAuthStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1)
)
swWACAuthStateEntry.setIndexNames(
    (0, "WebBase-Access-Control-MIB", "swWACAuthStatePort"),
    (0, "WebBase-Access-Control-MIB", "swWACAuthStateOriginalVid"),
    (0, "WebBase-Access-Control-MIB", "swWACAuthStateMACAddr"),
)
if mibBuilder.loadTexts:
    swWACAuthStateEntry.setStatus("current")
_SwWACAuthStatePort_Type = Integer32
_SwWACAuthStatePort_Object = MibTableColumn
swWACAuthStatePort = _SwWACAuthStatePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 1),
    _SwWACAuthStatePort_Type()
)
swWACAuthStatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStatePort.setStatus("current")
_SwWACAuthStateOriginalVid_Type = VlanId
_SwWACAuthStateOriginalVid_Object = MibTableColumn
swWACAuthStateOriginalVid = _SwWACAuthStateOriginalVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 2),
    _SwWACAuthStateOriginalVid_Type()
)
swWACAuthStateOriginalVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStateOriginalVid.setStatus("current")
_SwWACAuthStateMACAddr_Type = MacAddress
_SwWACAuthStateMACAddr_Object = MibTableColumn
swWACAuthStateMACAddr = _SwWACAuthStateMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 3),
    _SwWACAuthStateMACAddr_Type()
)
swWACAuthStateMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStateMACAddr.setStatus("current")


class _SwWACAuthStateAuthStatus_Type(Integer32):
    """Custom type swWACAuthStateAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 1),
          ("authenticating", 2),
          ("blocked", 3))
    )


_SwWACAuthStateAuthStatus_Type.__name__ = "Integer32"
_SwWACAuthStateAuthStatus_Object = MibTableColumn
swWACAuthStateAuthStatus = _SwWACAuthStateAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 5),
    _SwWACAuthStateAuthStatus_Type()
)
swWACAuthStateAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStateAuthStatus.setStatus("current")
_SwWACAuthStateAssignVid_Type = VlanId
_SwWACAuthStateAssignVid_Object = MibTableColumn
swWACAuthStateAssignVid = _SwWACAuthStateAssignVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 7),
    _SwWACAuthStateAssignVid_Type()
)
swWACAuthStateAssignVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStateAssignVid.setStatus("current")
_SwWACAuthStateAssignPriority_Type = Integer32
_SwWACAuthStateAssignPriority_Object = MibTableColumn
swWACAuthStateAssignPriority = _SwWACAuthStateAssignPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 8),
    _SwWACAuthStateAssignPriority_Type()
)
swWACAuthStateAssignPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStateAssignPriority.setStatus("current")
_SwWACAuthStateRemainTime_Type = Integer32
_SwWACAuthStateRemainTime_Object = MibTableColumn
swWACAuthStateRemainTime = _SwWACAuthStateRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 12),
    _SwWACAuthStateRemainTime_Type()
)
swWACAuthStateRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStateRemainTime.setStatus("current")
_SwWACAuthStateIdleTime_Type = Integer32
_SwWACAuthStateIdleTime_Object = MibTableColumn
swWACAuthStateIdleTime = _SwWACAuthStateIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 14),
    _SwWACAuthStateIdleTime_Type()
)
swWACAuthStateIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWACAuthStateIdleTime.setStatus("current")


class _SwWACAuthStateDelAction_Type(Integer32):
    """Custom type swWACAuthStateDelAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_SwWACAuthStateDelAction_Type.__name__ = "Integer32"
_SwWACAuthStateDelAction_Object = MibTableColumn
swWACAuthStateDelAction = _SwWACAuthStateDelAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 2, 2, 1, 25),
    _SwWACAuthStateDelAction_Type()
)
swWACAuthStateDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACAuthStateDelAction.setStatus("current")
_SwWACMgmt_ObjectIdentity = ObjectIdentity
swWACMgmt = _SwWACMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3)
)
_SwWebAuthPortTable_Object = MibTable
swWebAuthPortTable = _SwWebAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1)
)
if mibBuilder.loadTexts:
    swWebAuthPortTable.setStatus("current")
_SwWebAuthPortEntry_Object = MibTableRow
swWebAuthPortEntry = _SwWebAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1)
)
swWebAuthPortEntry.setIndexNames(
    (0, "WebBase-Access-Control-MIB", "swWebAuthPortIndex"),
)
if mibBuilder.loadTexts:
    swWebAuthPortEntry.setStatus("current")
_SwWebAuthPortIndex_Type = Integer32
_SwWebAuthPortIndex_Object = MibTableColumn
swWebAuthPortIndex = _SwWebAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 1),
    _SwWebAuthPortIndex_Type()
)
swWebAuthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWebAuthPortIndex.setStatus("current")


class _SwWebAuthPortState_Type(Integer32):
    """Custom type swWebAuthPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwWebAuthPortState_Type.__name__ = "Integer32"
_SwWebAuthPortState_Object = MibTableColumn
swWebAuthPortState = _SwWebAuthPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 2),
    _SwWebAuthPortState_Type()
)
swWebAuthPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWebAuthPortState.setStatus("current")
_SwWebAuthPortUserName_Type = DisplayString
_SwWebAuthPortUserName_Object = MibTableColumn
swWebAuthPortUserName = _SwWebAuthPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 3),
    _SwWebAuthPortUserName_Type()
)
swWebAuthPortUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWebAuthPortUserName.setStatus("obsolete")


class _SwWebAuthAuthStatus_Type(Integer32):
    """Custom type swWebAuthAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authenticated", 2),
          ("unauthenticated", 1))
    )


_SwWebAuthAuthStatus_Type.__name__ = "Integer32"
_SwWebAuthAuthStatus_Object = MibTableColumn
swWebAuthAuthStatus = _SwWebAuthAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 4),
    _SwWebAuthAuthStatus_Type()
)
swWebAuthAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWebAuthAuthStatus.setStatus("obsolete")
_SwWebAuthAssignedVID_Type = Integer32
_SwWebAuthAssignedVID_Object = MibTableColumn
swWebAuthAssignedVID = _SwWebAuthAssignedVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 5),
    _SwWebAuthAssignedVID_Type()
)
swWebAuthAssignedVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWebAuthAssignedVID.setStatus("obsolete")


class _SwWACPortAgeingTime_Type(Integer32):
    """Custom type swWACPortAgeingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SwWACPortAgeingTime_Type.__name__ = "Integer32"
_SwWACPortAgeingTime_Object = MibTableColumn
swWACPortAgeingTime = _SwWACPortAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 6),
    _SwWACPortAgeingTime_Type()
)
swWACPortAgeingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACPortAgeingTime.setStatus("current")


class _SwWACPortIdleTime_Type(Integer32):
    """Custom type swWACPortIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SwWACPortIdleTime_Type.__name__ = "Integer32"
_SwWACPortIdleTime_Object = MibTableColumn
swWACPortIdleTime = _SwWACPortIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 7),
    _SwWACPortIdleTime_Type()
)
swWACPortIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACPortIdleTime.setStatus("current")


class _SwWACPortBlockTime_Type(Integer32):
    """Custom type swWACPortBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SwWACPortBlockTime_Type.__name__ = "Integer32"
_SwWACPortBlockTime_Object = MibTableColumn
swWACPortBlockTime = _SwWACPortBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 1, 1, 8),
    _SwWACPortBlockTime_Type()
)
swWACPortBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swWACPortBlockTime.setStatus("current")
_SwWebAuthUserTable_Object = MibTable
swWebAuthUserTable = _SwWebAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2)
)
if mibBuilder.loadTexts:
    swWebAuthUserTable.setStatus("current")
_SwWebAuthUserEntry_Object = MibTableRow
swWebAuthUserEntry = _SwWebAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1)
)
swWebAuthUserEntry.setIndexNames(
    (0, "WebBase-Access-Control-MIB", "swWebAuthUserNameIndex"),
)
if mibBuilder.loadTexts:
    swWebAuthUserEntry.setStatus("current")


class _SwWebAuthUserNameIndex_Type(DisplayString):
    """Custom type swWebAuthUserNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwWebAuthUserNameIndex_Type.__name__ = "DisplayString"
_SwWebAuthUserNameIndex_Object = MibTableColumn
swWebAuthUserNameIndex = _SwWebAuthUserNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 1),
    _SwWebAuthUserNameIndex_Type()
)
swWebAuthUserNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swWebAuthUserNameIndex.setStatus("current")


class _SwWebAuthUserPWD_Type(DisplayString):
    """Custom type swWebAuthUserPWD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwWebAuthUserPWD_Type.__name__ = "DisplayString"
_SwWebAuthUserPWD_Object = MibTableColumn
swWebAuthUserPWD = _SwWebAuthUserPWD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 2),
    _SwWebAuthUserPWD_Type()
)
swWebAuthUserPWD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swWebAuthUserPWD.setStatus("current")


class _SwWebAuthUserVlanName_Type(DisplayString):
    """Custom type swWebAuthUserVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwWebAuthUserVlanName_Type.__name__ = "DisplayString"
_SwWebAuthUserVlanName_Object = MibTableColumn
swWebAuthUserVlanName = _SwWebAuthUserVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 3),
    _SwWebAuthUserVlanName_Type()
)
swWebAuthUserVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swWebAuthUserVlanName.setStatus("obsolete")
_SwWebAuthUserStatus_Type = RowStatus
_SwWebAuthUserStatus_Object = MibTableColumn
swWebAuthUserStatus = _SwWebAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 4),
    _SwWebAuthUserStatus_Type()
)
swWebAuthUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swWebAuthUserStatus.setStatus("current")


class _SwWebAuthUserVID_Type(Integer32):
    """Custom type swWebAuthUserVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SwWebAuthUserVID_Type.__name__ = "Integer32"
_SwWebAuthUserVID_Object = MibTableColumn
swWebAuthUserVID = _SwWebAuthUserVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 27, 3, 2, 1, 5),
    _SwWebAuthUserVID_Type()
)
swWebAuthUserVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swWebAuthUserVID.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WebBase-Access-Control-MIB",
    **{"VlanId": VlanId,
       "swWACMIB": swWACMIB,
       "swWACCtrl": swWACCtrl,
       "swWebAuthAdminState": swWebAuthAdminState,
       "swWebAuthMethod": swWebAuthMethod,
       "swWebAuthVlanName": swWebAuthVlanName,
       "swWebAuthAllPortstate": swWebAuthAllPortstate,
       "swWebAuthDefaultredirpath": swWebAuthDefaultredirpath,
       "swWebAuthLogouttimer": swWebAuthLogouttimer,
       "swWACVirtualIpAddr": swWACVirtualIpAddr,
       "swWACSwitchHttpProtocol": swWACSwitchHttpProtocol,
       "swWACSwitchHttpPort": swWACSwitchHttpPort,
       "swWACAuthFailOverState": swWACAuthFailOverState,
       "swWACRadiusAuthorizationState": swWACRadiusAuthorizationState,
       "swWACLocalAuthorizationState": swWACLocalAuthorizationState,
       "swWACAuthClearDefaultredirpath": swWACAuthClearDefaultredirpath,
       "swWACVirtualIPv6Addr": swWACVirtualIPv6Addr,
       "swWACInfo": swWACInfo,
       "swWACAuthInfoTable": swWACAuthInfoTable,
       "swWACAuthInfoEntry": swWACAuthInfoEntry,
       "swWACAuthInfoPort": swWACAuthInfoPort,
       "swWACAuthInfoAuthStatus": swWACAuthInfoAuthStatus,
       "swWACAuthInfoMACAddr": swWACAuthInfoMACAddr,
       "swWACAuthInfoVID": swWACAuthInfoVID,
       "swWACAuthInfoRemainAgeTime": swWACAuthInfoRemainAgeTime,
       "swWACAuthInfoIdleTime": swWACAuthInfoIdleTime,
       "swWACAuthInfoBlockTime": swWACAuthInfoBlockTime,
       "swWACAuthInfoStatus": swWACAuthInfoStatus,
       "swWACAuthInfoPriority": swWACAuthInfoPriority,
       "swWACAuthStateTable": swWACAuthStateTable,
       "swWACAuthStateEntry": swWACAuthStateEntry,
       "swWACAuthStatePort": swWACAuthStatePort,
       "swWACAuthStateOriginalVid": swWACAuthStateOriginalVid,
       "swWACAuthStateMACAddr": swWACAuthStateMACAddr,
       "swWACAuthStateAuthStatus": swWACAuthStateAuthStatus,
       "swWACAuthStateAssignVid": swWACAuthStateAssignVid,
       "swWACAuthStateAssignPriority": swWACAuthStateAssignPriority,
       "swWACAuthStateRemainTime": swWACAuthStateRemainTime,
       "swWACAuthStateIdleTime": swWACAuthStateIdleTime,
       "swWACAuthStateDelAction": swWACAuthStateDelAction,
       "swWACMgmt": swWACMgmt,
       "swWebAuthPortTable": swWebAuthPortTable,
       "swWebAuthPortEntry": swWebAuthPortEntry,
       "swWebAuthPortIndex": swWebAuthPortIndex,
       "swWebAuthPortState": swWebAuthPortState,
       "swWebAuthPortUserName": swWebAuthPortUserName,
       "swWebAuthAuthStatus": swWebAuthAuthStatus,
       "swWebAuthAssignedVID": swWebAuthAssignedVID,
       "swWACPortAgeingTime": swWACPortAgeingTime,
       "swWACPortIdleTime": swWACPortIdleTime,
       "swWACPortBlockTime": swWACPortBlockTime,
       "swWebAuthUserTable": swWebAuthUserTable,
       "swWebAuthUserEntry": swWebAuthUserEntry,
       "swWebAuthUserNameIndex": swWebAuthUserNameIndex,
       "swWebAuthUserPWD": swWebAuthUserPWD,
       "swWebAuthUserVlanName": swWebAuthUserVlanName,
       "swWebAuthUserStatus": swWebAuthUserStatus,
       "swWebAuthUserVID": swWebAuthUserVID}
)
