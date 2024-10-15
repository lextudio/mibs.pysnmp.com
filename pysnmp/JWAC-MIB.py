# SNMP MIB module (JWAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JWAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:32 2024
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

swJWACMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 39)
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

_SwJWACCtrl_ObjectIdentity = ObjectIdentity
swJWACCtrl = _SwJWACCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1)
)


class _SwJWACState_Type(Integer32):
    """Custom type swJWACState based on Integer32"""
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


_SwJWACState_Type.__name__ = "Integer32"
_SwJWACState_Object = MibScalar
swJWACState = _SwJWACState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 1),
    _SwJWACState_Type()
)
swJWACState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACState.setStatus("current")


class _SwJWACRedirectState_Type(Integer32):
    """Custom type swJWACRedirectState based on Integer32"""
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


_SwJWACRedirectState_Type.__name__ = "Integer32"
_SwJWACRedirectState_Object = MibScalar
swJWACRedirectState = _SwJWACRedirectState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 2),
    _SwJWACRedirectState_Type()
)
swJWACRedirectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACRedirectState.setStatus("current")


class _SwJWACForcibleLogoutState_Type(Integer32):
    """Custom type swJWACForcibleLogoutState based on Integer32"""
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


_SwJWACForcibleLogoutState_Type.__name__ = "Integer32"
_SwJWACForcibleLogoutState_Object = MibScalar
swJWACForcibleLogoutState = _SwJWACForcibleLogoutState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 3),
    _SwJWACForcibleLogoutState_Type()
)
swJWACForcibleLogoutState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACForcibleLogoutState.setStatus("current")


class _SwJWACUDPFilteringState_Type(Integer32):
    """Custom type swJWACUDPFilteringState based on Integer32"""
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


_SwJWACUDPFilteringState_Type.__name__ = "Integer32"
_SwJWACUDPFilteringState_Object = MibScalar
swJWACUDPFilteringState = _SwJWACUDPFilteringState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 4),
    _SwJWACUDPFilteringState_Type()
)
swJWACUDPFilteringState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACUDPFilteringState.setStatus("current")


class _SwJWACQuarantineServerMonitorState_Type(Integer32):
    """Custom type swJWACQuarantineServerMonitorState based on Integer32"""
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


_SwJWACQuarantineServerMonitorState_Type.__name__ = "Integer32"
_SwJWACQuarantineServerMonitorState_Object = MibScalar
swJWACQuarantineServerMonitorState = _SwJWACQuarantineServerMonitorState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 5),
    _SwJWACQuarantineServerMonitorState_Type()
)
swJWACQuarantineServerMonitorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACQuarantineServerMonitorState.setStatus("current")


class _SwJWACQuarantineServerErrorTimeOut_Type(Integer32):
    """Custom type swJWACQuarantineServerErrorTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_SwJWACQuarantineServerErrorTimeOut_Type.__name__ = "Integer32"
_SwJWACQuarantineServerErrorTimeOut_Object = MibScalar
swJWACQuarantineServerErrorTimeOut = _SwJWACQuarantineServerErrorTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 6),
    _SwJWACQuarantineServerErrorTimeOut_Type()
)
swJWACQuarantineServerErrorTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACQuarantineServerErrorTimeOut.setStatus("current")


class _SwJWACRedirectDestination_Type(Integer32):
    """Custom type swJWACRedirectDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jwac_login_page", 2),
          ("quarantine_server", 1))
    )


_SwJWACRedirectDestination_Type.__name__ = "Integer32"
_SwJWACRedirectDestination_Object = MibScalar
swJWACRedirectDestination = _SwJWACRedirectDestination_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 7),
    _SwJWACRedirectDestination_Type()
)
swJWACRedirectDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACRedirectDestination.setStatus("current")


class _SwJWACRedirectDelayTime_Type(Integer32):
    """Custom type swJWACRedirectDelayTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SwJWACRedirectDelayTime_Type.__name__ = "Integer32"
_SwJWACRedirectDelayTime_Object = MibScalar
swJWACRedirectDelayTime = _SwJWACRedirectDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 8),
    _SwJWACRedirectDelayTime_Type()
)
swJWACRedirectDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACRedirectDelayTime.setStatus("current")
_SwJWACVirtualIpAddr_Type = IpAddress
_SwJWACVirtualIpAddr_Object = MibScalar
swJWACVirtualIpAddr = _SwJWACVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 9),
    _SwJWACVirtualIpAddr_Type()
)
swJWACVirtualIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACVirtualIpAddr.setStatus("current")


class _SwJWACQuarantineServerURL_Type(DisplayString):
    """Custom type swJWACQuarantineServerURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACQuarantineServerURL_Type.__name__ = "DisplayString"
_SwJWACQuarantineServerURL_Object = MibScalar
swJWACQuarantineServerURL = _SwJWACQuarantineServerURL_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 10),
    _SwJWACQuarantineServerURL_Type()
)
swJWACQuarantineServerURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACQuarantineServerURL.setStatus("current")


class _SwJWACSwitchHttpPortNumber_Type(Integer32):
    """Custom type swJWACSwitchHttpPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwJWACSwitchHttpPortNumber_Type.__name__ = "Integer32"
_SwJWACSwitchHttpPortNumber_Object = MibScalar
swJWACSwitchHttpPortNumber = _SwJWACSwitchHttpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 11),
    _SwJWACSwitchHttpPortNumber_Type()
)
swJWACSwitchHttpPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACSwitchHttpPortNumber.setStatus("current")


class _SwJWACSwitchHttpProtocol_Type(Integer32):
    """Custom type swJWACSwitchHttpProtocol based on Integer32"""
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


_SwJWACSwitchHttpProtocol_Type.__name__ = "Integer32"
_SwJWACSwitchHttpProtocol_Object = MibScalar
swJWACSwitchHttpProtocol = _SwJWACSwitchHttpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 12),
    _SwJWACSwitchHttpProtocol_Type()
)
swJWACSwitchHttpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACSwitchHttpProtocol.setStatus("current")


class _SwJWACRadiusProtocol_Type(Integer32):
    """Custom type swJWACRadiusProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("chap", 3),
          ("eap_md5", 6),
          ("local", 1),
          ("ms_chap", 4),
          ("ms_chapv2", 5),
          ("pap", 2))
    )


_SwJWACRadiusProtocol_Type.__name__ = "Integer32"
_SwJWACRadiusProtocol_Object = MibScalar
swJWACRadiusProtocol = _SwJWACRadiusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 13),
    _SwJWACRadiusProtocol_Type()
)
swJWACRadiusProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACRadiusProtocol.setStatus("current")
_SwJWACUpdateServerTable_Object = MibTable
swJWACUpdateServerTable = _SwJWACUpdateServerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14)
)
if mibBuilder.loadTexts:
    swJWACUpdateServerTable.setStatus("obsolete")
_SwJWACUpdateServerEntry_Object = MibTableRow
swJWACUpdateServerEntry = _SwJWACUpdateServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1)
)
swJWACUpdateServerEntry.setIndexNames(
    (0, "JWAC-MIB", "swJWACUpdateServerIpAddr"),
    (0, "JWAC-MIB", "swJWACUpdateServerMask"),
)
if mibBuilder.loadTexts:
    swJWACUpdateServerEntry.setStatus("obsolete")
_SwJWACUpdateServerIpAddr_Type = IpAddress
_SwJWACUpdateServerIpAddr_Object = MibTableColumn
swJWACUpdateServerIpAddr = _SwJWACUpdateServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1, 1),
    _SwJWACUpdateServerIpAddr_Type()
)
swJWACUpdateServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACUpdateServerIpAddr.setStatus("obsolete")
_SwJWACUpdateServerMask_Type = IpAddress
_SwJWACUpdateServerMask_Object = MibTableColumn
swJWACUpdateServerMask = _SwJWACUpdateServerMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1, 2),
    _SwJWACUpdateServerMask_Type()
)
swJWACUpdateServerMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACUpdateServerMask.setStatus("obsolete")
_SwJWACUpdateServerStatus_Type = RowStatus
_SwJWACUpdateServerStatus_Object = MibTableColumn
swJWACUpdateServerStatus = _SwJWACUpdateServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 14, 1, 3),
    _SwJWACUpdateServerStatus_Type()
)
swJWACUpdateServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swJWACUpdateServerStatus.setStatus("obsolete")


class _SwJWACAuthenticatePage_Type(Integer32):
    """Custom type swJWACAuthenticatePage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("japanese", 1))
    )


_SwJWACAuthenticatePage_Type.__name__ = "Integer32"
_SwJWACAuthenticatePage_Object = MibScalar
swJWACAuthenticatePage = _SwJWACAuthenticatePage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 15),
    _SwJWACAuthenticatePage_Type()
)
swJWACAuthenticatePage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACAuthenticatePage.setStatus("current")


class _SwJWACAuthFailOverState_Type(Integer32):
    """Custom type swJWACAuthFailOverState based on Integer32"""
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


_SwJWACAuthFailOverState_Type.__name__ = "Integer32"
_SwJWACAuthFailOverState_Object = MibScalar
swJWACAuthFailOverState = _SwJWACAuthFailOverState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 16),
    _SwJWACAuthFailOverState_Type()
)
swJWACAuthFailOverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACAuthFailOverState.setStatus("current")


class _SwJWACRadiusAuthorizeState_Type(Integer32):
    """Custom type swJWACRadiusAuthorizeState based on Integer32"""
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


_SwJWACRadiusAuthorizeState_Type.__name__ = "Integer32"
_SwJWACRadiusAuthorizeState_Object = MibScalar
swJWACRadiusAuthorizeState = _SwJWACRadiusAuthorizeState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 17),
    _SwJWACRadiusAuthorizeState_Type()
)
swJWACRadiusAuthorizeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACRadiusAuthorizeState.setStatus("current")


class _SwJWACLocalAuthorizeState_Type(Integer32):
    """Custom type swJWACLocalAuthorizeState based on Integer32"""
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


_SwJWACLocalAuthorizeState_Type.__name__ = "Integer32"
_SwJWACLocalAuthorizeState_Object = MibScalar
swJWACLocalAuthorizeState = _SwJWACLocalAuthorizeState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 18),
    _SwJWACLocalAuthorizeState_Type()
)
swJWACLocalAuthorizeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACLocalAuthorizeState.setStatus("current")
_SwJWACUpdateSVRTable_Object = MibTable
swJWACUpdateSVRTable = _SwJWACUpdateSVRTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19)
)
if mibBuilder.loadTexts:
    swJWACUpdateSVRTable.setStatus("current")
_SwJWACUpdateSVREntry_Object = MibTableRow
swJWACUpdateSVREntry = _SwJWACUpdateSVREntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1)
)
swJWACUpdateSVREntry.setIndexNames(
    (0, "JWAC-MIB", "swJWACUpdateSVRIpAddr"),
    (0, "JWAC-MIB", "swJWACUpdateSVRMask"),
    (0, "JWAC-MIB", "swJWACUpdateSVRProtocol"),
    (0, "JWAC-MIB", "swJWACUpdateSVRPort"),
)
if mibBuilder.loadTexts:
    swJWACUpdateSVREntry.setStatus("current")
_SwJWACUpdateSVRIpAddr_Type = IpAddress
_SwJWACUpdateSVRIpAddr_Object = MibTableColumn
swJWACUpdateSVRIpAddr = _SwJWACUpdateSVRIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 1),
    _SwJWACUpdateSVRIpAddr_Type()
)
swJWACUpdateSVRIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACUpdateSVRIpAddr.setStatus("current")
_SwJWACUpdateSVRMask_Type = IpAddress
_SwJWACUpdateSVRMask_Object = MibTableColumn
swJWACUpdateSVRMask = _SwJWACUpdateSVRMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 2),
    _SwJWACUpdateSVRMask_Type()
)
swJWACUpdateSVRMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACUpdateSVRMask.setStatus("current")


class _SwJWACUpdateSVRProtocol_Type(Integer32):
    """Custom type swJWACUpdateSVRProtocol based on Integer32"""
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
          ("tcp", 2),
          ("udp", 3))
    )


_SwJWACUpdateSVRProtocol_Type.__name__ = "Integer32"
_SwJWACUpdateSVRProtocol_Object = MibTableColumn
swJWACUpdateSVRProtocol = _SwJWACUpdateSVRProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 3),
    _SwJWACUpdateSVRProtocol_Type()
)
swJWACUpdateSVRProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACUpdateSVRProtocol.setStatus("current")


class _SwJWACUpdateSVRPort_Type(Integer32):
    """Custom type swJWACUpdateSVRPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwJWACUpdateSVRPort_Type.__name__ = "Integer32"
_SwJWACUpdateSVRPort_Object = MibTableColumn
swJWACUpdateSVRPort = _SwJWACUpdateSVRPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 4),
    _SwJWACUpdateSVRPort_Type()
)
swJWACUpdateSVRPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACUpdateSVRPort.setStatus("current")
_SwJWACUpdateSVRStatus_Type = RowStatus
_SwJWACUpdateSVRStatus_Object = MibTableColumn
swJWACUpdateSVRStatus = _SwJWACUpdateSVRStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 5),
    _SwJWACUpdateSVRStatus_Type()
)
swJWACUpdateSVRStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swJWACUpdateSVRStatus.setStatus("current")


class _SwJWACUpdateSVRState_Type(Integer32):
    """Custom type swJWACUpdateSVRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwJWACUpdateSVRState_Type.__name__ = "Integer32"
_SwJWACUpdateSVRState_Object = MibTableColumn
swJWACUpdateSVRState = _SwJWACUpdateSVRState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 19, 1, 6),
    _SwJWACUpdateSVRState_Type()
)
swJWACUpdateSVRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACUpdateSVRState.setStatus("current")


class _SwJWACVirtualIpURL_Type(DisplayString):
    """Custom type swJWACVirtualIpURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACVirtualIpURL_Type.__name__ = "DisplayString"
_SwJWACVirtualIpURL_Object = MibScalar
swJWACVirtualIpURL = _SwJWACVirtualIpURL_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 1, 20),
    _SwJWACVirtualIpURL_Type()
)
swJWACVirtualIpURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACVirtualIpURL.setStatus("current")
_SwJWACInfo_ObjectIdentity = ObjectIdentity
swJWACInfo = _SwJWACInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 2)
)
_SwJWACPortMgmt_ObjectIdentity = ObjectIdentity
swJWACPortMgmt = _SwJWACPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3)
)
_SwJWACPortTable_Object = MibTable
swJWACPortTable = _SwJWACPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1)
)
if mibBuilder.loadTexts:
    swJWACPortTable.setStatus("current")
_SwJWACPortEntry_Object = MibTableRow
swJWACPortEntry = _SwJWACPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1)
)
swJWACPortEntry.setIndexNames(
    (0, "JWAC-MIB", "swJWACPortIndex"),
)
if mibBuilder.loadTexts:
    swJWACPortEntry.setStatus("current")
_SwJWACPortIndex_Type = Integer32
_SwJWACPortIndex_Object = MibTableColumn
swJWACPortIndex = _SwJWACPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 1),
    _SwJWACPortIndex_Type()
)
swJWACPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACPortIndex.setStatus("current")


class _SwJWACPortState_Type(Integer32):
    """Custom type swJWACPortState based on Integer32"""
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


_SwJWACPortState_Type.__name__ = "Integer32"
_SwJWACPortState_Object = MibTableColumn
swJWACPortState = _SwJWACPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 2),
    _SwJWACPortState_Type()
)
swJWACPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPortState.setStatus("current")
_SwJWACPortMaxAuthHost_Type = Integer32
_SwJWACPortMaxAuthHost_Object = MibTableColumn
swJWACPortMaxAuthHost = _SwJWACPortMaxAuthHost_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 3),
    _SwJWACPortMaxAuthHost_Type()
)
swJWACPortMaxAuthHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPortMaxAuthHost.setStatus("current")


class _SwJWACPortAgeingTime_Type(Integer32):
    """Custom type swJWACPortAgeingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SwJWACPortAgeingTime_Type.__name__ = "Integer32"
_SwJWACPortAgeingTime_Object = MibTableColumn
swJWACPortAgeingTime = _SwJWACPortAgeingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 4),
    _SwJWACPortAgeingTime_Type()
)
swJWACPortAgeingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPortAgeingTime.setStatus("current")


class _SwJWACPortIdleTime_Type(Integer32):
    """Custom type swJWACPortIdleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SwJWACPortIdleTime_Type.__name__ = "Integer32"
_SwJWACPortIdleTime_Object = MibTableColumn
swJWACPortIdleTime = _SwJWACPortIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 5),
    _SwJWACPortIdleTime_Type()
)
swJWACPortIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPortIdleTime.setStatus("current")


class _SwJWACPortBlockTime_Type(Integer32):
    """Custom type swJWACPortBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SwJWACPortBlockTime_Type.__name__ = "Integer32"
_SwJWACPortBlockTime_Object = MibTableColumn
swJWACPortBlockTime = _SwJWACPortBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 6),
    _SwJWACPortBlockTime_Type()
)
swJWACPortBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPortBlockTime.setStatus("current")


class _SwJWACPortAuthMode_Type(Integer32):
    """Custom type swJWACPortAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hostbased", 1),
          ("portbased", 2))
    )


_SwJWACPortAuthMode_Type.__name__ = "Integer32"
_SwJWACPortAuthMode_Object = MibTableColumn
swJWACPortAuthMode = _SwJWACPortAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 3, 1, 1, 7),
    _SwJWACPortAuthMode_Type()
)
swJWACPortAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPortAuthMode.setStatus("current")
_SwJWACMgmt_ObjectIdentity = ObjectIdentity
swJWACMgmt = _SwJWACMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4)
)
_SwJWACHostTable_Object = MibTable
swJWACHostTable = _SwJWACHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1)
)
if mibBuilder.loadTexts:
    swJWACHostTable.setStatus("current")
_SwJWACHostEntry_Object = MibTableRow
swJWACHostEntry = _SwJWACHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1)
)
swJWACHostEntry.setIndexNames(
    (0, "JWAC-MIB", "swJWACHostPort"),
    (0, "JWAC-MIB", "swJWACHostAuthStatus"),
    (0, "JWAC-MIB", "swJWACHostMACAddr"),
)
if mibBuilder.loadTexts:
    swJWACHostEntry.setStatus("current")
_SwJWACHostPort_Type = Integer32
_SwJWACHostPort_Object = MibTableColumn
swJWACHostPort = _SwJWACHostPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 1),
    _SwJWACHostPort_Type()
)
swJWACHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostPort.setStatus("current")


class _SwJWACHostAuthStatus_Type(Integer32):
    """Custom type swJWACHostAuthStatus based on Integer32"""
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


_SwJWACHostAuthStatus_Type.__name__ = "Integer32"
_SwJWACHostAuthStatus_Object = MibTableColumn
swJWACHostAuthStatus = _SwJWACHostAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 2),
    _SwJWACHostAuthStatus_Type()
)
swJWACHostAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostAuthStatus.setStatus("current")
_SwJWACHostMACAddr_Type = MacAddress
_SwJWACHostMACAddr_Object = MibTableColumn
swJWACHostMACAddr = _SwJWACHostMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 3),
    _SwJWACHostMACAddr_Type()
)
swJWACHostMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostMACAddr.setStatus("current")
_SwJWACHostVID_Type = VlanId
_SwJWACHostVID_Object = MibTableColumn
swJWACHostVID = _SwJWACHostVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 4),
    _SwJWACHostVID_Type()
)
swJWACHostVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostVID.setStatus("current")
_SwJWACHostRemainAgeTime_Type = Integer32
_SwJWACHostRemainAgeTime_Object = MibTableColumn
swJWACHostRemainAgeTime = _SwJWACHostRemainAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 5),
    _SwJWACHostRemainAgeTime_Type()
)
swJWACHostRemainAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostRemainAgeTime.setStatus("current")
_SwJWACHostIdleTime_Type = Integer32
_SwJWACHostIdleTime_Object = MibTableColumn
swJWACHostIdleTime = _SwJWACHostIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 6),
    _SwJWACHostIdleTime_Type()
)
swJWACHostIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostIdleTime.setStatus("current")
_SwJWACHostBlockTime_Type = Integer32
_SwJWACHostBlockTime_Object = MibTableColumn
swJWACHostBlockTime = _SwJWACHostBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 7),
    _SwJWACHostBlockTime_Type()
)
swJWACHostBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostBlockTime.setStatus("current")


class _SwJWACHostStatus_Type(Integer32):
    """Custom type swJWACHostStatus based on Integer32"""
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


_SwJWACHostStatus_Type.__name__ = "Integer32"
_SwJWACHostStatus_Object = MibTableColumn
swJWACHostStatus = _SwJWACHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 8),
    _SwJWACHostStatus_Type()
)
swJWACHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACHostStatus.setStatus("current")
_SwJWACHostPriority_Type = Integer32
_SwJWACHostPriority_Object = MibTableColumn
swJWACHostPriority = _SwJWACHostPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 9),
    _SwJWACHostPriority_Type()
)
swJWACHostPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostPriority.setStatus("current")
_SwJWACHostUserName_Type = DisplayString
_SwJWACHostUserName_Object = MibTableColumn
swJWACHostUserName = _SwJWACHostUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 10),
    _SwJWACHostUserName_Type()
)
swJWACHostUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostUserName.setStatus("current")
_SwJWACHostIP_Type = IpAddress
_SwJWACHostIP_Object = MibTableColumn
swJWACHostIP = _SwJWACHostIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 1, 1, 11),
    _SwJWACHostIP_Type()
)
swJWACHostIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACHostIP.setStatus("current")
_SwJWACPageElementTable_Object = MibTable
swJWACPageElementTable = _SwJWACPageElementTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2)
)
if mibBuilder.loadTexts:
    swJWACPageElementTable.setStatus("current")
_SwJWACPageElementEntry_Object = MibTableRow
swJWACPageElementEntry = _SwJWACPageElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1)
)
swJWACPageElementEntry.setIndexNames(
    (0, "JWAC-MIB", "swJWACPageElementPage"),
)
if mibBuilder.loadTexts:
    swJWACPageElementEntry.setStatus("current")


class _SwJWACPageElementPage_Type(Integer32):
    """Custom type swJWACPageElementPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("english", 2),
          ("japanese", 1))
    )


_SwJWACPageElementPage_Type.__name__ = "Integer32"
_SwJWACPageElementPage_Object = MibTableColumn
swJWACPageElementPage = _SwJWACPageElementPage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 1),
    _SwJWACPageElementPage_Type()
)
swJWACPageElementPage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACPageElementPage.setStatus("current")


class _SwJWACPageElementPageTitle_Type(DisplayString):
    """Custom type swJWACPageElementPageTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACPageElementPageTitle_Type.__name__ = "DisplayString"
_SwJWACPageElementPageTitle_Object = MibTableColumn
swJWACPageElementPageTitle = _SwJWACPageElementPageTitle_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 2),
    _SwJWACPageElementPageTitle_Type()
)
swJWACPageElementPageTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementPageTitle.setStatus("current")


class _SwJWACPageElementLoginWindowTitle_Type(DisplayString):
    """Custom type swJWACPageElementLoginWindowTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwJWACPageElementLoginWindowTitle_Type.__name__ = "DisplayString"
_SwJWACPageElementLoginWindowTitle_Object = MibTableColumn
swJWACPageElementLoginWindowTitle = _SwJWACPageElementLoginWindowTitle_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 3),
    _SwJWACPageElementLoginWindowTitle_Type()
)
swJWACPageElementLoginWindowTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementLoginWindowTitle.setStatus("current")


class _SwJWACPageElementUserName_Type(DisplayString):
    """Custom type swJWACPageElementUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwJWACPageElementUserName_Type.__name__ = "DisplayString"
_SwJWACPageElementUserName_Object = MibTableColumn
swJWACPageElementUserName = _SwJWACPageElementUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 4),
    _SwJWACPageElementUserName_Type()
)
swJWACPageElementUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementUserName.setStatus("current")


class _SwJWACPageElementPassWord_Type(DisplayString):
    """Custom type swJWACPageElementPassWord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SwJWACPageElementPassWord_Type.__name__ = "DisplayString"
_SwJWACPageElementPassWord_Object = MibTableColumn
swJWACPageElementPassWord = _SwJWACPageElementPassWord_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 5),
    _SwJWACPageElementPassWord_Type()
)
swJWACPageElementPassWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementPassWord.setStatus("current")


class _SwJWACPageElementLogoutWindowTitle_Type(DisplayString):
    """Custom type swJWACPageElementLogoutWindowTitle based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwJWACPageElementLogoutWindowTitle_Type.__name__ = "DisplayString"
_SwJWACPageElementLogoutWindowTitle_Object = MibTableColumn
swJWACPageElementLogoutWindowTitle = _SwJWACPageElementLogoutWindowTitle_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 6),
    _SwJWACPageElementLogoutWindowTitle_Type()
)
swJWACPageElementLogoutWindowTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementLogoutWindowTitle.setStatus("current")


class _SwJWACPageElementNotificationLine1_Type(DisplayString):
    """Custom type swJWACPageElementNotificationLine1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACPageElementNotificationLine1_Type.__name__ = "DisplayString"
_SwJWACPageElementNotificationLine1_Object = MibTableColumn
swJWACPageElementNotificationLine1 = _SwJWACPageElementNotificationLine1_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 7),
    _SwJWACPageElementNotificationLine1_Type()
)
swJWACPageElementNotificationLine1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementNotificationLine1.setStatus("current")


class _SwJWACPageElementNotificationLine2_Type(DisplayString):
    """Custom type swJWACPageElementNotificationLine2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACPageElementNotificationLine2_Type.__name__ = "DisplayString"
_SwJWACPageElementNotificationLine2_Object = MibTableColumn
swJWACPageElementNotificationLine2 = _SwJWACPageElementNotificationLine2_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 8),
    _SwJWACPageElementNotificationLine2_Type()
)
swJWACPageElementNotificationLine2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementNotificationLine2.setStatus("current")


class _SwJWACPageElementNotificationLine3_Type(DisplayString):
    """Custom type swJWACPageElementNotificationLine3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACPageElementNotificationLine3_Type.__name__ = "DisplayString"
_SwJWACPageElementNotificationLine3_Object = MibTableColumn
swJWACPageElementNotificationLine3 = _SwJWACPageElementNotificationLine3_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 9),
    _SwJWACPageElementNotificationLine3_Type()
)
swJWACPageElementNotificationLine3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementNotificationLine3.setStatus("current")


class _SwJWACPageElementNotificationLine4_Type(DisplayString):
    """Custom type swJWACPageElementNotificationLine4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACPageElementNotificationLine4_Type.__name__ = "DisplayString"
_SwJWACPageElementNotificationLine4_Object = MibTableColumn
swJWACPageElementNotificationLine4 = _SwJWACPageElementNotificationLine4_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 10),
    _SwJWACPageElementNotificationLine4_Type()
)
swJWACPageElementNotificationLine4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementNotificationLine4.setStatus("current")


class _SwJWACPageElementNotificationLine5_Type(DisplayString):
    """Custom type swJWACPageElementNotificationLine5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SwJWACPageElementNotificationLine5_Type.__name__ = "DisplayString"
_SwJWACPageElementNotificationLine5_Object = MibTableColumn
swJWACPageElementNotificationLine5 = _SwJWACPageElementNotificationLine5_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 2, 1, 11),
    _SwJWACPageElementNotificationLine5_Type()
)
swJWACPageElementNotificationLine5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACPageElementNotificationLine5.setStatus("current")
_SwJWACWebAuthUserTable_Object = MibTable
swJWACWebAuthUserTable = _SwJWACWebAuthUserTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3)
)
if mibBuilder.loadTexts:
    swJWACWebAuthUserTable.setStatus("current")
_SwJWACWebAuthUserEntry_Object = MibTableRow
swJWACWebAuthUserEntry = _SwJWACWebAuthUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1)
)
swJWACWebAuthUserEntry.setIndexNames(
    (0, "JWAC-MIB", "swJWACWebAuthUserNameIndex"),
)
if mibBuilder.loadTexts:
    swJWACWebAuthUserEntry.setStatus("current")


class _SwJWACWebAuthUserNameIndex_Type(DisplayString):
    """Custom type swJWACWebAuthUserNameIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwJWACWebAuthUserNameIndex_Type.__name__ = "DisplayString"
_SwJWACWebAuthUserNameIndex_Object = MibTableColumn
swJWACWebAuthUserNameIndex = _SwJWACWebAuthUserNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 1),
    _SwJWACWebAuthUserNameIndex_Type()
)
swJWACWebAuthUserNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACWebAuthUserNameIndex.setStatus("current")


class _SwJWACWebAuthUserPWD_Type(DisplayString):
    """Custom type swJWACWebAuthUserPWD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SwJWACWebAuthUserPWD_Type.__name__ = "DisplayString"
_SwJWACWebAuthUserPWD_Object = MibTableColumn
swJWACWebAuthUserPWD = _SwJWACWebAuthUserPWD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 2),
    _SwJWACWebAuthUserPWD_Type()
)
swJWACWebAuthUserPWD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swJWACWebAuthUserPWD.setStatus("current")
_SwJWACWebAuthUserVID_Type = VlanId
_SwJWACWebAuthUserVID_Object = MibTableColumn
swJWACWebAuthUserVID = _SwJWACWebAuthUserVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 3),
    _SwJWACWebAuthUserVID_Type()
)
swJWACWebAuthUserVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swJWACWebAuthUserVID.setStatus("current")
_SwJWACWebAuthUserStatus_Type = RowStatus
_SwJWACWebAuthUserStatus_Object = MibTableColumn
swJWACWebAuthUserStatus = _SwJWACWebAuthUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 3, 1, 4),
    _SwJWACWebAuthUserStatus_Type()
)
swJWACWebAuthUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swJWACWebAuthUserStatus.setStatus("current")
_SwJWACAuthStateTable_Object = MibTable
swJWACAuthStateTable = _SwJWACAuthStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4)
)
if mibBuilder.loadTexts:
    swJWACAuthStateTable.setStatus("current")
_SwJWACAuthStateEntry_Object = MibTableRow
swJWACAuthStateEntry = _SwJWACAuthStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1)
)
swJWACAuthStateEntry.setIndexNames(
    (0, "JWAC-MIB", "swJWACAuthStatePort"),
    (0, "JWAC-MIB", "swJWACAuthStateOriginalVid"),
    (0, "JWAC-MIB", "swJWACAuthStateMACAddr"),
)
if mibBuilder.loadTexts:
    swJWACAuthStateEntry.setStatus("current")
_SwJWACAuthStatePort_Type = Integer32
_SwJWACAuthStatePort_Object = MibTableColumn
swJWACAuthStatePort = _SwJWACAuthStatePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 1),
    _SwJWACAuthStatePort_Type()
)
swJWACAuthStatePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swJWACAuthStatePort.setStatus("current")
_SwJWACAuthStateOriginalVid_Type = VlanId
_SwJWACAuthStateOriginalVid_Object = MibTableColumn
swJWACAuthStateOriginalVid = _SwJWACAuthStateOriginalVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 2),
    _SwJWACAuthStateOriginalVid_Type()
)
swJWACAuthStateOriginalVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swJWACAuthStateOriginalVid.setStatus("current")
_SwJWACAuthStateMACAddr_Type = MacAddress
_SwJWACAuthStateMACAddr_Object = MibTableColumn
swJWACAuthStateMACAddr = _SwJWACAuthStateMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 3),
    _SwJWACAuthStateMACAddr_Type()
)
swJWACAuthStateMACAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swJWACAuthStateMACAddr.setStatus("current")


class _SwJWACAuthStateAuthStatus_Type(Integer32):
    """Custom type swJWACAuthStateAuthStatus based on Integer32"""
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


_SwJWACAuthStateAuthStatus_Type.__name__ = "Integer32"
_SwJWACAuthStateAuthStatus_Object = MibTableColumn
swJWACAuthStateAuthStatus = _SwJWACAuthStateAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 5),
    _SwJWACAuthStateAuthStatus_Type()
)
swJWACAuthStateAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACAuthStateAuthStatus.setStatus("current")
_SwJWACAuthStateAssignVid_Type = VlanId
_SwJWACAuthStateAssignVid_Object = MibTableColumn
swJWACAuthStateAssignVid = _SwJWACAuthStateAssignVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 7),
    _SwJWACAuthStateAssignVid_Type()
)
swJWACAuthStateAssignVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACAuthStateAssignVid.setStatus("current")
_SwJWACAuthStateAssignPriority_Type = Integer32
_SwJWACAuthStateAssignPriority_Object = MibTableColumn
swJWACAuthStateAssignPriority = _SwJWACAuthStateAssignPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 8),
    _SwJWACAuthStateAssignPriority_Type()
)
swJWACAuthStateAssignPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACAuthStateAssignPriority.setStatus("current")
_SwJWACAuthStateRemainTime_Type = Integer32
_SwJWACAuthStateRemainTime_Object = MibTableColumn
swJWACAuthStateRemainTime = _SwJWACAuthStateRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 12),
    _SwJWACAuthStateRemainTime_Type()
)
swJWACAuthStateRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACAuthStateRemainTime.setStatus("current")
if mibBuilder.loadTexts:
    swJWACAuthStateRemainTime.setUnits("minutes/seconds")
_SwJWACAuthStateIdleTime_Type = Integer32
_SwJWACAuthStateIdleTime_Object = MibTableColumn
swJWACAuthStateIdleTime = _SwJWACAuthStateIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 14),
    _SwJWACAuthStateIdleTime_Type()
)
swJWACAuthStateIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACAuthStateIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    swJWACAuthStateIdleTime.setUnits("seconds")
_SwJWACAuthStateUserName_Type = DisplayString
_SwJWACAuthStateUserName_Object = MibTableColumn
swJWACAuthStateUserName = _SwJWACAuthStateUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 18),
    _SwJWACAuthStateUserName_Type()
)
swJWACAuthStateUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACAuthStateUserName.setStatus("current")
_SwJWACAuthStateIP_Type = IpAddress
_SwJWACAuthStateIP_Object = MibTableColumn
swJWACAuthStateIP = _SwJWACAuthStateIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 20),
    _SwJWACAuthStateIP_Type()
)
swJWACAuthStateIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swJWACAuthStateIP.setStatus("current")


class _SwJWACAuthStateDelAction_Type(Integer32):
    """Custom type swJWACAuthStateDelAction based on Integer32"""
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


_SwJWACAuthStateDelAction_Type.__name__ = "Integer32"
_SwJWACAuthStateDelAction_Object = MibTableColumn
swJWACAuthStateDelAction = _SwJWACAuthStateDelAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 4, 4, 1, 30),
    _SwJWACAuthStateDelAction_Type()
)
swJWACAuthStateDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swJWACAuthStateDelAction.setStatus("current")
_SwJWACNotify_ObjectIdentity = ObjectIdentity
swJWACNotify = _SwJWACNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 39, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JWAC-MIB",
    **{"VlanId": VlanId,
       "swJWACMIB": swJWACMIB,
       "swJWACCtrl": swJWACCtrl,
       "swJWACState": swJWACState,
       "swJWACRedirectState": swJWACRedirectState,
       "swJWACForcibleLogoutState": swJWACForcibleLogoutState,
       "swJWACUDPFilteringState": swJWACUDPFilteringState,
       "swJWACQuarantineServerMonitorState": swJWACQuarantineServerMonitorState,
       "swJWACQuarantineServerErrorTimeOut": swJWACQuarantineServerErrorTimeOut,
       "swJWACRedirectDestination": swJWACRedirectDestination,
       "swJWACRedirectDelayTime": swJWACRedirectDelayTime,
       "swJWACVirtualIpAddr": swJWACVirtualIpAddr,
       "swJWACQuarantineServerURL": swJWACQuarantineServerURL,
       "swJWACSwitchHttpPortNumber": swJWACSwitchHttpPortNumber,
       "swJWACSwitchHttpProtocol": swJWACSwitchHttpProtocol,
       "swJWACRadiusProtocol": swJWACRadiusProtocol,
       "swJWACUpdateServerTable": swJWACUpdateServerTable,
       "swJWACUpdateServerEntry": swJWACUpdateServerEntry,
       "swJWACUpdateServerIpAddr": swJWACUpdateServerIpAddr,
       "swJWACUpdateServerMask": swJWACUpdateServerMask,
       "swJWACUpdateServerStatus": swJWACUpdateServerStatus,
       "swJWACAuthenticatePage": swJWACAuthenticatePage,
       "swJWACAuthFailOverState": swJWACAuthFailOverState,
       "swJWACRadiusAuthorizeState": swJWACRadiusAuthorizeState,
       "swJWACLocalAuthorizeState": swJWACLocalAuthorizeState,
       "swJWACUpdateSVRTable": swJWACUpdateSVRTable,
       "swJWACUpdateSVREntry": swJWACUpdateSVREntry,
       "swJWACUpdateSVRIpAddr": swJWACUpdateSVRIpAddr,
       "swJWACUpdateSVRMask": swJWACUpdateSVRMask,
       "swJWACUpdateSVRProtocol": swJWACUpdateSVRProtocol,
       "swJWACUpdateSVRPort": swJWACUpdateSVRPort,
       "swJWACUpdateSVRStatus": swJWACUpdateSVRStatus,
       "swJWACUpdateSVRState": swJWACUpdateSVRState,
       "swJWACVirtualIpURL": swJWACVirtualIpURL,
       "swJWACInfo": swJWACInfo,
       "swJWACPortMgmt": swJWACPortMgmt,
       "swJWACPortTable": swJWACPortTable,
       "swJWACPortEntry": swJWACPortEntry,
       "swJWACPortIndex": swJWACPortIndex,
       "swJWACPortState": swJWACPortState,
       "swJWACPortMaxAuthHost": swJWACPortMaxAuthHost,
       "swJWACPortAgeingTime": swJWACPortAgeingTime,
       "swJWACPortIdleTime": swJWACPortIdleTime,
       "swJWACPortBlockTime": swJWACPortBlockTime,
       "swJWACPortAuthMode": swJWACPortAuthMode,
       "swJWACMgmt": swJWACMgmt,
       "swJWACHostTable": swJWACHostTable,
       "swJWACHostEntry": swJWACHostEntry,
       "swJWACHostPort": swJWACHostPort,
       "swJWACHostAuthStatus": swJWACHostAuthStatus,
       "swJWACHostMACAddr": swJWACHostMACAddr,
       "swJWACHostVID": swJWACHostVID,
       "swJWACHostRemainAgeTime": swJWACHostRemainAgeTime,
       "swJWACHostIdleTime": swJWACHostIdleTime,
       "swJWACHostBlockTime": swJWACHostBlockTime,
       "swJWACHostStatus": swJWACHostStatus,
       "swJWACHostPriority": swJWACHostPriority,
       "swJWACHostUserName": swJWACHostUserName,
       "swJWACHostIP": swJWACHostIP,
       "swJWACPageElementTable": swJWACPageElementTable,
       "swJWACPageElementEntry": swJWACPageElementEntry,
       "swJWACPageElementPage": swJWACPageElementPage,
       "swJWACPageElementPageTitle": swJWACPageElementPageTitle,
       "swJWACPageElementLoginWindowTitle": swJWACPageElementLoginWindowTitle,
       "swJWACPageElementUserName": swJWACPageElementUserName,
       "swJWACPageElementPassWord": swJWACPageElementPassWord,
       "swJWACPageElementLogoutWindowTitle": swJWACPageElementLogoutWindowTitle,
       "swJWACPageElementNotificationLine1": swJWACPageElementNotificationLine1,
       "swJWACPageElementNotificationLine2": swJWACPageElementNotificationLine2,
       "swJWACPageElementNotificationLine3": swJWACPageElementNotificationLine3,
       "swJWACPageElementNotificationLine4": swJWACPageElementNotificationLine4,
       "swJWACPageElementNotificationLine5": swJWACPageElementNotificationLine5,
       "swJWACWebAuthUserTable": swJWACWebAuthUserTable,
       "swJWACWebAuthUserEntry": swJWACWebAuthUserEntry,
       "swJWACWebAuthUserNameIndex": swJWACWebAuthUserNameIndex,
       "swJWACWebAuthUserPWD": swJWACWebAuthUserPWD,
       "swJWACWebAuthUserVID": swJWACWebAuthUserVID,
       "swJWACWebAuthUserStatus": swJWACWebAuthUserStatus,
       "swJWACAuthStateTable": swJWACAuthStateTable,
       "swJWACAuthStateEntry": swJWACAuthStateEntry,
       "swJWACAuthStatePort": swJWACAuthStatePort,
       "swJWACAuthStateOriginalVid": swJWACAuthStateOriginalVid,
       "swJWACAuthStateMACAddr": swJWACAuthStateMACAddr,
       "swJWACAuthStateAuthStatus": swJWACAuthStateAuthStatus,
       "swJWACAuthStateAssignVid": swJWACAuthStateAssignVid,
       "swJWACAuthStateAssignPriority": swJWACAuthStateAssignPriority,
       "swJWACAuthStateRemainTime": swJWACAuthStateRemainTime,
       "swJWACAuthStateIdleTime": swJWACAuthStateIdleTime,
       "swJWACAuthStateUserName": swJWACAuthStateUserName,
       "swJWACAuthStateIP": swJWACAuthStateIP,
       "swJWACAuthStateDelAction": swJWACAuthStateDelAction,
       "swJWACNotify": swJWACNotify}
)
