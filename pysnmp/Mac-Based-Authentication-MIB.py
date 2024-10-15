# SNMP MIB module (Mac-Based-Authentication-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Mac-Based-Authentication-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:34 2024
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

swMBAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwMBACtrl_ObjectIdentity = ObjectIdentity
swMBACtrl = _SwMBACtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1)
)


class _SwMacBasedAuthState_Type(Integer32):
    """Custom type swMacBasedAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SwMacBasedAuthState_Type.__name__ = "Integer32"
_SwMacBasedAuthState_Object = MibScalar
swMacBasedAuthState = _SwMacBasedAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 1),
    _SwMacBasedAuthState_Type()
)
swMacBasedAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthState.setStatus("current")


class _SwMacBasedAuthMethod_Type(Integer32):
    """Custom type swMacBasedAuthMethod based on Integer32"""
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


_SwMacBasedAuthMethod_Type.__name__ = "Integer32"
_SwMacBasedAuthMethod_Object = MibScalar
swMacBasedAuthMethod = _SwMacBasedAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 2),
    _SwMacBasedAuthMethod_Type()
)
swMacBasedAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthMethod.setStatus("current")


class _SwMacBasedAuthPWD_Type(DisplayString):
    """Custom type swMacBasedAuthPWD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_SwMacBasedAuthPWD_Type.__name__ = "DisplayString"
_SwMacBasedAuthPWD_Object = MibScalar
swMacBasedAuthPWD = _SwMacBasedAuthPWD_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 3),
    _SwMacBasedAuthPWD_Type()
)
swMacBasedAuthPWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthPWD.setStatus("current")


class _SwMacBasedAuthVlanName_Type(DisplayString):
    """Custom type swMacBasedAuthVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMacBasedAuthVlanName_Type.__name__ = "DisplayString"
_SwMacBasedAuthVlanName_Object = MibScalar
swMacBasedAuthVlanName = _SwMacBasedAuthVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 4),
    _SwMacBasedAuthVlanName_Type()
)
swMacBasedAuthVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthVlanName.setStatus("current")
_SwMacBasedAuthMemberPorts_Type = PortList
_SwMacBasedAuthMemberPorts_Object = MibScalar
swMacBasedAuthMemberPorts = _SwMacBasedAuthMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 5),
    _SwMacBasedAuthMemberPorts_Type()
)
swMacBasedAuthMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthMemberPorts.setStatus("current")


class _SwMacBasedAuthVlanNameDelState_Type(Integer32):
    """Custom type swMacBasedAuthVlanNameDelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwMacBasedAuthVlanNameDelState_Type.__name__ = "Integer32"
_SwMacBasedAuthVlanNameDelState_Object = MibScalar
swMacBasedAuthVlanNameDelState = _SwMacBasedAuthVlanNameDelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 7),
    _SwMacBasedAuthVlanNameDelState_Type()
)
swMacBasedAuthVlanNameDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthVlanNameDelState.setStatus("current")


class _SwMacBasedAuthClearAllAction_Type(Integer32):
    """Custom type swMacBasedAuthClearAllAction based on Integer32"""
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


_SwMacBasedAuthClearAllAction_Type.__name__ = "Integer32"
_SwMacBasedAuthClearAllAction_Object = MibScalar
swMacBasedAuthClearAllAction = _SwMacBasedAuthClearAllAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 8),
    _SwMacBasedAuthClearAllAction_Type()
)
swMacBasedAuthClearAllAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthClearAllAction.setStatus("current")


class _SwMacBasedAuthMaxUser_Type(Integer32):
    """Custom type swMacBasedAuthMaxUser based on Integer32"""
    defaultValue = 128


_SwMacBasedAuthMaxUser_Object = MibScalar
swMacBasedAuthMaxUser = _SwMacBasedAuthMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 9),
    _SwMacBasedAuthMaxUser_Type()
)
swMacBasedAuthMaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthMaxUser.setStatus("current")


class _SwMacBasedAuthFailOver_Type(Integer32):
    """Custom type swMacBasedAuthFailOver based on Integer32"""
    defaultValue = 2

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


_SwMacBasedAuthFailOver_Type.__name__ = "Integer32"
_SwMacBasedAuthFailOver_Object = MibScalar
swMacBasedAuthFailOver = _SwMacBasedAuthFailOver_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 10),
    _SwMacBasedAuthFailOver_Type()
)
swMacBasedAuthFailOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthFailOver.setStatus("current")


class _SwMacBasedAuthRadiusAuthorization_Type(Integer32):
    """Custom type swMacBasedAuthRadiusAuthorization based on Integer32"""
    defaultValue = 1

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


_SwMacBasedAuthRadiusAuthorization_Type.__name__ = "Integer32"
_SwMacBasedAuthRadiusAuthorization_Object = MibScalar
swMacBasedAuthRadiusAuthorization = _SwMacBasedAuthRadiusAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 11),
    _SwMacBasedAuthRadiusAuthorization_Type()
)
swMacBasedAuthRadiusAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthRadiusAuthorization.setStatus("current")


class _SwMacBasedAuthLocalAuthorization_Type(Integer32):
    """Custom type swMacBasedAuthLocalAuthorization based on Integer32"""
    defaultValue = 1

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


_SwMacBasedAuthLocalAuthorization_Type.__name__ = "Integer32"
_SwMacBasedAuthLocalAuthorization_Object = MibScalar
swMacBasedAuthLocalAuthorization = _SwMacBasedAuthLocalAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 12),
    _SwMacBasedAuthLocalAuthorization_Type()
)
swMacBasedAuthLocalAuthorization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthLocalAuthorization.setStatus("current")


class _SwMacBasedAuthTrapState_Type(Integer32):
    """Custom type swMacBasedAuthTrapState based on Integer32"""
    defaultValue = 1

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


_SwMacBasedAuthTrapState_Type.__name__ = "Integer32"
_SwMacBasedAuthTrapState_Object = MibScalar
swMacBasedAuthTrapState = _SwMacBasedAuthTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 13),
    _SwMacBasedAuthTrapState_Type()
)
swMacBasedAuthTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthTrapState.setStatus("current")


class _SwMacBasedAuthLogState_Type(Integer32):
    """Custom type swMacBasedAuthLogState based on Integer32"""
    defaultValue = 1

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


_SwMacBasedAuthLogState_Type.__name__ = "Integer32"
_SwMacBasedAuthLogState_Object = MibScalar
swMacBasedAuthLogState = _SwMacBasedAuthLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 14),
    _SwMacBasedAuthLogState_Type()
)
swMacBasedAuthLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthLogState.setStatus("current")


class _SwMacBasedAuthPwdType_Type(Integer32):
    """Custom type swMacBasedAuthPwdType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client_mac_address", 2),
          ("manual_string", 1))
    )


_SwMacBasedAuthPwdType_Type.__name__ = "Integer32"
_SwMacBasedAuthPwdType_Object = MibScalar
swMacBasedAuthPwdType = _SwMacBasedAuthPwdType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 1, 15),
    _SwMacBasedAuthPwdType_Type()
)
swMacBasedAuthPwdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthPwdType.setStatus("current")
_SwMBAInfo_ObjectIdentity = ObjectIdentity
swMBAInfo = _SwMBAInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2)
)
_SwMacBasedAuthPortInfoTable_Object = MibTable
swMacBasedAuthPortInfoTable = _SwMacBasedAuthPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1)
)
if mibBuilder.loadTexts:
    swMacBasedAuthPortInfoTable.setStatus("current")
_SwMacBasedAuthPortInfoEntry_Object = MibTableRow
swMacBasedAuthPortInfoEntry = _SwMacBasedAuthPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1)
)
swMacBasedAuthPortInfoEntry.setIndexNames(
    (0, "Mac-Based-Authentication-MIB", "swMacBasedAuthInfoPortIndex"),
    (0, "Mac-Based-Authentication-MIB", "swMacBasedAuthInfoMacIndex"),
)
if mibBuilder.loadTexts:
    swMacBasedAuthPortInfoEntry.setStatus("current")
_SwMacBasedAuthInfoPortIndex_Type = Integer32
_SwMacBasedAuthInfoPortIndex_Object = MibTableColumn
swMacBasedAuthInfoPortIndex = _SwMacBasedAuthInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 1),
    _SwMacBasedAuthInfoPortIndex_Type()
)
swMacBasedAuthInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoPortIndex.setStatus("current")
_SwMacBasedAuthInfoMacIndex_Type = MacAddress
_SwMacBasedAuthInfoMacIndex_Object = MibTableColumn
swMacBasedAuthInfoMacIndex = _SwMacBasedAuthInfoMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 2),
    _SwMacBasedAuthInfoMacIndex_Type()
)
swMacBasedAuthInfoMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoMacIndex.setStatus("current")


class _SwMacBasedAuthInfoStatus_Type(Integer32):
    """Custom type swMacBasedAuthInfoStatus based on Integer32"""
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
        *(("authenticated", 4),
          ("authenticating", 3),
          ("blocked", 5),
          ("connecting", 2),
          ("unconnected", 1))
    )


_SwMacBasedAuthInfoStatus_Type.__name__ = "Integer32"
_SwMacBasedAuthInfoStatus_Object = MibTableColumn
swMacBasedAuthInfoStatus = _SwMacBasedAuthInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 3),
    _SwMacBasedAuthInfoStatus_Type()
)
swMacBasedAuthInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoStatus.setStatus("current")


class _SwMacBasedAuthInfoAssignVLANName_Type(DisplayString):
    """Custom type swMacBasedAuthInfoAssignVLANName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwMacBasedAuthInfoAssignVLANName_Type.__name__ = "DisplayString"
_SwMacBasedAuthInfoAssignVLANName_Object = MibTableColumn
swMacBasedAuthInfoAssignVLANName = _SwMacBasedAuthInfoAssignVLANName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 4),
    _SwMacBasedAuthInfoAssignVLANName_Type()
)
swMacBasedAuthInfoAssignVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoAssignVLANName.setStatus("current")


class _SwMacBasedAuthClearMacAction_Type(Integer32):
    """Custom type swMacBasedAuthClearMacAction based on Integer32"""
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


_SwMacBasedAuthClearMacAction_Type.__name__ = "Integer32"
_SwMacBasedAuthClearMacAction_Object = MibTableColumn
swMacBasedAuthClearMacAction = _SwMacBasedAuthClearMacAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 5),
    _SwMacBasedAuthClearMacAction_Type()
)
swMacBasedAuthClearMacAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthClearMacAction.setStatus("current")
_SwMacBasedAuthInfoPriority_Type = Integer32
_SwMacBasedAuthInfoPriority_Object = MibTableColumn
swMacBasedAuthInfoPriority = _SwMacBasedAuthInfoPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 6),
    _SwMacBasedAuthInfoPriority_Type()
)
swMacBasedAuthInfoPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoPriority.setStatus("current")
_SwMacBasedAuthInfoAgingTime_Type = Integer32
_SwMacBasedAuthInfoAgingTime_Object = MibTableColumn
swMacBasedAuthInfoAgingTime = _SwMacBasedAuthInfoAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 7),
    _SwMacBasedAuthInfoAgingTime_Type()
)
swMacBasedAuthInfoAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoAgingTime.setUnits("minutes")
_SwMacBasedAuthInfoBlockTime_Type = Integer32
_SwMacBasedAuthInfoBlockTime_Object = MibTableColumn
swMacBasedAuthInfoBlockTime = _SwMacBasedAuthInfoBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 8),
    _SwMacBasedAuthInfoBlockTime_Type()
)
swMacBasedAuthInfoBlockTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoBlockTime.setStatus("current")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoBlockTime.setUnits("seconds")


class _SwMacBasedAuthInfoAssignVID_Type(Integer32):
    """Custom type swMacBasedAuthInfoAssignVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SwMacBasedAuthInfoAssignVID_Type.__name__ = "Integer32"
_SwMacBasedAuthInfoAssignVID_Object = MibTableColumn
swMacBasedAuthInfoAssignVID = _SwMacBasedAuthInfoAssignVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 1, 1, 9),
    _SwMacBasedAuthInfoAssignVID_Type()
)
swMacBasedAuthInfoAssignVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthInfoAssignVID.setStatus("current")
_SwMacBasedAuthStateTable_Object = MibTable
swMacBasedAuthStateTable = _SwMacBasedAuthStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2)
)
if mibBuilder.loadTexts:
    swMacBasedAuthStateTable.setStatus("current")
_SwMacBasedAuthStateEntry_Object = MibTableRow
swMacBasedAuthStateEntry = _SwMacBasedAuthStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1)
)
swMacBasedAuthStateEntry.setIndexNames(
    (0, "Mac-Based-Authentication-MIB", "swMacBasedAuthStatePort"),
    (0, "Mac-Based-Authentication-MIB", "swMacBasedAuthStateOriginalVID"),
    (0, "Mac-Based-Authentication-MIB", "swMacBasedAuthStateMacAddr"),
)
if mibBuilder.loadTexts:
    swMacBasedAuthStateEntry.setStatus("current")
_SwMacBasedAuthStatePort_Type = Integer32
_SwMacBasedAuthStatePort_Object = MibTableColumn
swMacBasedAuthStatePort = _SwMacBasedAuthStatePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 1),
    _SwMacBasedAuthStatePort_Type()
)
swMacBasedAuthStatePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMacBasedAuthStatePort.setStatus("current")
_SwMacBasedAuthStateOriginalVID_Type = VlanId
_SwMacBasedAuthStateOriginalVID_Object = MibTableColumn
swMacBasedAuthStateOriginalVID = _SwMacBasedAuthStateOriginalVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 2),
    _SwMacBasedAuthStateOriginalVID_Type()
)
swMacBasedAuthStateOriginalVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMacBasedAuthStateOriginalVID.setStatus("current")
_SwMacBasedAuthStateMacAddr_Type = MacAddress
_SwMacBasedAuthStateMacAddr_Object = MibTableColumn
swMacBasedAuthStateMacAddr = _SwMacBasedAuthStateMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 3),
    _SwMacBasedAuthStateMacAddr_Type()
)
swMacBasedAuthStateMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swMacBasedAuthStateMacAddr.setStatus("current")


class _SwMacBasedAuthStateAuthStatus_Type(Integer32):
    """Custom type swMacBasedAuthStateAuthStatus based on Integer32"""
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


_SwMacBasedAuthStateAuthStatus_Type.__name__ = "Integer32"
_SwMacBasedAuthStateAuthStatus_Object = MibTableColumn
swMacBasedAuthStateAuthStatus = _SwMacBasedAuthStateAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 4),
    _SwMacBasedAuthStateAuthStatus_Type()
)
swMacBasedAuthStateAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthStateAuthStatus.setStatus("current")
_SwMacBasedAuthStateAssignVID_Type = VlanId
_SwMacBasedAuthStateAssignVID_Object = MibTableColumn
swMacBasedAuthStateAssignVID = _SwMacBasedAuthStateAssignVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 5),
    _SwMacBasedAuthStateAssignVID_Type()
)
swMacBasedAuthStateAssignVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthStateAssignVID.setStatus("current")
_SwMacBasedAuthStateAssignPriority_Type = Integer32
_SwMacBasedAuthStateAssignPriority_Object = MibTableColumn
swMacBasedAuthStateAssignPriority = _SwMacBasedAuthStateAssignPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 6),
    _SwMacBasedAuthStateAssignPriority_Type()
)
swMacBasedAuthStateAssignPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthStateAssignPriority.setStatus("current")
_SwMacBasedAuthStateRemainTime_Type = Integer32
_SwMacBasedAuthStateRemainTime_Object = MibTableColumn
swMacBasedAuthStateRemainTime = _SwMacBasedAuthStateRemainTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 7),
    _SwMacBasedAuthStateRemainTime_Type()
)
swMacBasedAuthStateRemainTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthStateRemainTime.setStatus("current")
if mibBuilder.loadTexts:
    swMacBasedAuthStateRemainTime.setUnits("minutes/seconds")


class _SwMacBasedAuthStateDelAction_Type(Integer32):
    """Custom type swMacBasedAuthStateDelAction based on Integer32"""
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


_SwMacBasedAuthStateDelAction_Type.__name__ = "Integer32"
_SwMacBasedAuthStateDelAction_Object = MibTableColumn
swMacBasedAuthStateDelAction = _SwMacBasedAuthStateDelAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 2, 2, 1, 25),
    _SwMacBasedAuthStateDelAction_Type()
)
swMacBasedAuthStateDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthStateDelAction.setStatus("current")
_SwMBAPortMgmt_ObjectIdentity = ObjectIdentity
swMBAPortMgmt = _SwMBAPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3)
)
_SwMacBasedAuthPortTable_Object = MibTable
swMacBasedAuthPortTable = _SwMacBasedAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1)
)
if mibBuilder.loadTexts:
    swMacBasedAuthPortTable.setStatus("current")
_SwMacBasedAuthPortEntry_Object = MibTableRow
swMacBasedAuthPortEntry = _SwMacBasedAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1)
)
swMacBasedAuthPortEntry.setIndexNames(
    (0, "Mac-Based-Authentication-MIB", "swMacBasedAuthPortIndex"),
)
if mibBuilder.loadTexts:
    swMacBasedAuthPortEntry.setStatus("current")


class _SwMacBasedAuthPortIndex_Type(Integer32):
    """Custom type swMacBasedAuthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwMacBasedAuthPortIndex_Type.__name__ = "Integer32"
_SwMacBasedAuthPortIndex_Object = MibTableColumn
swMacBasedAuthPortIndex = _SwMacBasedAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1, 1),
    _SwMacBasedAuthPortIndex_Type()
)
swMacBasedAuthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthPortIndex.setStatus("current")


class _SwMacBasedAuthPortState_Type(Integer32):
    """Custom type swMacBasedAuthPortState based on Integer32"""
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


_SwMacBasedAuthPortState_Type.__name__ = "Integer32"
_SwMacBasedAuthPortState_Object = MibTableColumn
swMacBasedAuthPortState = _SwMacBasedAuthPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1, 2),
    _SwMacBasedAuthPortState_Type()
)
swMacBasedAuthPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthPortState.setStatus("current")


class _SwMacBasedAuthPortMode_Type(Integer32):
    """Custom type swMacBasedAuthPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("host_based", 2),
          ("port_based", 1))
    )


_SwMacBasedAuthPortMode_Type.__name__ = "Integer32"
_SwMacBasedAuthPortMode_Object = MibTableColumn
swMacBasedAuthPortMode = _SwMacBasedAuthPortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1, 3),
    _SwMacBasedAuthPortMode_Type()
)
swMacBasedAuthPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthPortMode.setStatus("current")


class _SwMacBasedAuthPortAgingTime_Type(Integer32):
    """Custom type swMacBasedAuthPortAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SwMacBasedAuthPortAgingTime_Type.__name__ = "Integer32"
_SwMacBasedAuthPortAgingTime_Object = MibTableColumn
swMacBasedAuthPortAgingTime = _SwMacBasedAuthPortAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1, 4),
    _SwMacBasedAuthPortAgingTime_Type()
)
swMacBasedAuthPortAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthPortAgingTime.setStatus("current")


class _SwMacBasedAuthPortBlockTime_Type(Integer32):
    """Custom type swMacBasedAuthPortBlockTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_SwMacBasedAuthPortBlockTime_Type.__name__ = "Integer32"
_SwMacBasedAuthPortBlockTime_Object = MibTableColumn
swMacBasedAuthPortBlockTime = _SwMacBasedAuthPortBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1, 5),
    _SwMacBasedAuthPortBlockTime_Type()
)
swMacBasedAuthPortBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthPortBlockTime.setStatus("current")


class _SwMacBasedAuthClearPortAction_Type(Integer32):
    """Custom type swMacBasedAuthClearPortAction based on Integer32"""
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


_SwMacBasedAuthClearPortAction_Type.__name__ = "Integer32"
_SwMacBasedAuthClearPortAction_Object = MibTableColumn
swMacBasedAuthClearPortAction = _SwMacBasedAuthClearPortAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1, 6),
    _SwMacBasedAuthClearPortAction_Type()
)
swMacBasedAuthClearPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthClearPortAction.setStatus("current")


class _SwMacBasedAuthPortMaxUser_Type(Integer32):
    """Custom type swMacBasedAuthPortMaxUser based on Integer32"""
    defaultValue = 128


_SwMacBasedAuthPortMaxUser_Object = MibTableColumn
swMacBasedAuthPortMaxUser = _SwMacBasedAuthPortMaxUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 3, 1, 1, 7),
    _SwMacBasedAuthPortMaxUser_Type()
)
swMacBasedAuthPortMaxUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMacBasedAuthPortMaxUser.setStatus("current")
_SwMBAMgmt_ObjectIdentity = ObjectIdentity
swMBAMgmt = _SwMBAMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 4)
)
_SwMacBasedAuthDatabaseTable_Object = MibTable
swMacBasedAuthDatabaseTable = _SwMacBasedAuthDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 4, 1)
)
if mibBuilder.loadTexts:
    swMacBasedAuthDatabaseTable.setStatus("current")
_SwMacBasedAuthDatabaseEntry_Object = MibTableRow
swMacBasedAuthDatabaseEntry = _SwMacBasedAuthDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 4, 1, 1)
)
swMacBasedAuthDatabaseEntry.setIndexNames(
    (0, "Mac-Based-Authentication-MIB", "swMacBasedAuthDatabaseMacIndex"),
)
if mibBuilder.loadTexts:
    swMacBasedAuthDatabaseEntry.setStatus("current")
_SwMacBasedAuthDatabaseMacIndex_Type = MacAddress
_SwMacBasedAuthDatabaseMacIndex_Object = MibTableColumn
swMacBasedAuthDatabaseMacIndex = _SwMacBasedAuthDatabaseMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 4, 1, 1, 1),
    _SwMacBasedAuthDatabaseMacIndex_Type()
)
swMacBasedAuthDatabaseMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMacBasedAuthDatabaseMacIndex.setStatus("current")


class _SwMacBasedAuthDatabaseVlanName_Type(DisplayString):
    """Custom type swMacBasedAuthDatabaseVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwMacBasedAuthDatabaseVlanName_Type.__name__ = "DisplayString"
_SwMacBasedAuthDatabaseVlanName_Object = MibTableColumn
swMacBasedAuthDatabaseVlanName = _SwMacBasedAuthDatabaseVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 4, 1, 1, 2),
    _SwMacBasedAuthDatabaseVlanName_Type()
)
swMacBasedAuthDatabaseVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMacBasedAuthDatabaseVlanName.setStatus("obsolete")
_SwMacBasedAuthDatabaseStatus_Type = RowStatus
_SwMacBasedAuthDatabaseStatus_Object = MibTableColumn
swMacBasedAuthDatabaseStatus = _SwMacBasedAuthDatabaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 4, 1, 1, 3),
    _SwMacBasedAuthDatabaseStatus_Type()
)
swMacBasedAuthDatabaseStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMacBasedAuthDatabaseStatus.setStatus("current")


class _SwMacBasedAuthDatabaseVID_Type(Integer32):
    """Custom type swMacBasedAuthDatabaseVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_SwMacBasedAuthDatabaseVID_Type.__name__ = "Integer32"
_SwMacBasedAuthDatabaseVID_Object = MibTableColumn
swMacBasedAuthDatabaseVID = _SwMacBasedAuthDatabaseVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 4, 1, 1, 5),
    _SwMacBasedAuthDatabaseVID_Type()
)
swMacBasedAuthDatabaseVID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swMacBasedAuthDatabaseVID.setStatus("current")
_SwMBATrap_ObjectIdentity = ObjectIdentity
swMBATrap = _SwMBATrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11)
)
_SwMBANotify_ObjectIdentity = ObjectIdentity
swMBANotify = _SwMBANotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11, 1)
)
_SwMBANotifyPrefix_ObjectIdentity = ObjectIdentity
swMBANotifyPrefix = _SwMBANotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11, 1, 0)
)
_SwMBANotifyBidings_ObjectIdentity = ObjectIdentity
swMBANotifyBidings = _SwMBANotifyBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11, 1, 1)
)
_SwMacBasedAuthVID_Type = Integer32
_SwMacBasedAuthVID_Object = MibScalar
swMacBasedAuthVID = _SwMacBasedAuthVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11, 1, 1, 1),
    _SwMacBasedAuthVID_Type()
)
swMacBasedAuthVID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swMacBasedAuthVID.setStatus("current")

# Managed Objects groups


# Notification objects

swMacBasedAccessControlLoggedSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11, 1, 0, 1)
)
swMacBasedAccessControlLoggedSuccess.setObjects(
      *(("Mac-Based-Authentication-MIB", "swMacBasedAuthInfoMacIndex"),
        ("Mac-Based-Authentication-MIB", "swMacBasedAuthInfoPortIndex"),
        ("Mac-Based-Authentication-MIB", "swMacBasedAuthVID"))
)
if mibBuilder.loadTexts:
    swMacBasedAccessControlLoggedSuccess.setStatus(
        "current"
    )

swMacBasedAccessControlLoggedFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11, 1, 0, 2)
)
swMacBasedAccessControlLoggedFail.setObjects(
      *(("Mac-Based-Authentication-MIB", "swMacBasedAuthInfoMacIndex"),
        ("Mac-Based-Authentication-MIB", "swMacBasedAuthInfoPortIndex"),
        ("Mac-Based-Authentication-MIB", "swMacBasedAuthVID"))
)
if mibBuilder.loadTexts:
    swMacBasedAccessControlLoggedFail.setStatus(
        "current"
    )

swMacBasedAccessControlAgesOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 35, 11, 1, 0, 3)
)
swMacBasedAccessControlAgesOut.setObjects(
      *(("Mac-Based-Authentication-MIB", "swMacBasedAuthInfoMacIndex"),
        ("Mac-Based-Authentication-MIB", "swMacBasedAuthInfoPortIndex"),
        ("Mac-Based-Authentication-MIB", "swMacBasedAuthVID"))
)
if mibBuilder.loadTexts:
    swMacBasedAccessControlAgesOut.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Mac-Based-Authentication-MIB",
    **{"PortList": PortList,
       "swMBAMIB": swMBAMIB,
       "swMBACtrl": swMBACtrl,
       "swMacBasedAuthState": swMacBasedAuthState,
       "swMacBasedAuthMethod": swMacBasedAuthMethod,
       "swMacBasedAuthPWD": swMacBasedAuthPWD,
       "swMacBasedAuthVlanName": swMacBasedAuthVlanName,
       "swMacBasedAuthMemberPorts": swMacBasedAuthMemberPorts,
       "swMacBasedAuthVlanNameDelState": swMacBasedAuthVlanNameDelState,
       "swMacBasedAuthClearAllAction": swMacBasedAuthClearAllAction,
       "swMacBasedAuthMaxUser": swMacBasedAuthMaxUser,
       "swMacBasedAuthFailOver": swMacBasedAuthFailOver,
       "swMacBasedAuthRadiusAuthorization": swMacBasedAuthRadiusAuthorization,
       "swMacBasedAuthLocalAuthorization": swMacBasedAuthLocalAuthorization,
       "swMacBasedAuthTrapState": swMacBasedAuthTrapState,
       "swMacBasedAuthLogState": swMacBasedAuthLogState,
       "swMacBasedAuthPwdType": swMacBasedAuthPwdType,
       "swMBAInfo": swMBAInfo,
       "swMacBasedAuthPortInfoTable": swMacBasedAuthPortInfoTable,
       "swMacBasedAuthPortInfoEntry": swMacBasedAuthPortInfoEntry,
       "swMacBasedAuthInfoPortIndex": swMacBasedAuthInfoPortIndex,
       "swMacBasedAuthInfoMacIndex": swMacBasedAuthInfoMacIndex,
       "swMacBasedAuthInfoStatus": swMacBasedAuthInfoStatus,
       "swMacBasedAuthInfoAssignVLANName": swMacBasedAuthInfoAssignVLANName,
       "swMacBasedAuthClearMacAction": swMacBasedAuthClearMacAction,
       "swMacBasedAuthInfoPriority": swMacBasedAuthInfoPriority,
       "swMacBasedAuthInfoAgingTime": swMacBasedAuthInfoAgingTime,
       "swMacBasedAuthInfoBlockTime": swMacBasedAuthInfoBlockTime,
       "swMacBasedAuthInfoAssignVID": swMacBasedAuthInfoAssignVID,
       "swMacBasedAuthStateTable": swMacBasedAuthStateTable,
       "swMacBasedAuthStateEntry": swMacBasedAuthStateEntry,
       "swMacBasedAuthStatePort": swMacBasedAuthStatePort,
       "swMacBasedAuthStateOriginalVID": swMacBasedAuthStateOriginalVID,
       "swMacBasedAuthStateMacAddr": swMacBasedAuthStateMacAddr,
       "swMacBasedAuthStateAuthStatus": swMacBasedAuthStateAuthStatus,
       "swMacBasedAuthStateAssignVID": swMacBasedAuthStateAssignVID,
       "swMacBasedAuthStateAssignPriority": swMacBasedAuthStateAssignPriority,
       "swMacBasedAuthStateRemainTime": swMacBasedAuthStateRemainTime,
       "swMacBasedAuthStateDelAction": swMacBasedAuthStateDelAction,
       "swMBAPortMgmt": swMBAPortMgmt,
       "swMacBasedAuthPortTable": swMacBasedAuthPortTable,
       "swMacBasedAuthPortEntry": swMacBasedAuthPortEntry,
       "swMacBasedAuthPortIndex": swMacBasedAuthPortIndex,
       "swMacBasedAuthPortState": swMacBasedAuthPortState,
       "swMacBasedAuthPortMode": swMacBasedAuthPortMode,
       "swMacBasedAuthPortAgingTime": swMacBasedAuthPortAgingTime,
       "swMacBasedAuthPortBlockTime": swMacBasedAuthPortBlockTime,
       "swMacBasedAuthClearPortAction": swMacBasedAuthClearPortAction,
       "swMacBasedAuthPortMaxUser": swMacBasedAuthPortMaxUser,
       "swMBAMgmt": swMBAMgmt,
       "swMacBasedAuthDatabaseTable": swMacBasedAuthDatabaseTable,
       "swMacBasedAuthDatabaseEntry": swMacBasedAuthDatabaseEntry,
       "swMacBasedAuthDatabaseMacIndex": swMacBasedAuthDatabaseMacIndex,
       "swMacBasedAuthDatabaseVlanName": swMacBasedAuthDatabaseVlanName,
       "swMacBasedAuthDatabaseStatus": swMacBasedAuthDatabaseStatus,
       "swMacBasedAuthDatabaseVID": swMacBasedAuthDatabaseVID,
       "swMBATrap": swMBATrap,
       "swMBANotify": swMBANotify,
       "swMBANotifyPrefix": swMBANotifyPrefix,
       "swMacBasedAccessControlLoggedSuccess": swMacBasedAccessControlLoggedSuccess,
       "swMacBasedAccessControlLoggedFail": swMacBasedAccessControlLoggedFail,
       "swMacBasedAccessControlAgesOut": swMacBasedAccessControlAgesOut,
       "swMBANotifyBidings": swMBANotifyBidings,
       "swMacBasedAuthVID": swMacBasedAuthVID}
)
