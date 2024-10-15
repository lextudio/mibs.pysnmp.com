# SNMP MIB module (ASCEND-MIBBGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBBGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:15 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibmibProfBgpGlobal_ObjectIdentity = ObjectIdentity
mibmibProfBgpGlobal = _MibmibProfBgpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 57)
)
_MibmibProfBgpGlobalTable_Object = MibTable
mibmibProfBgpGlobalTable = _MibmibProfBgpGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1)
)
if mibBuilder.loadTexts:
    mibmibProfBgpGlobalTable.setStatus("mandatory")
_MibmibProfBgpGlobalEntry_Object = MibTableRow
mibmibProfBgpGlobalEntry = _MibmibProfBgpGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1)
)
mibmibProfBgpGlobalEntry.setIndexNames(
    (0, "ASCEND-MIBBGP-MIB", "mibProfBgpGlobal-Index-o"),
)
if mibBuilder.loadTexts:
    mibmibProfBgpGlobalEntry.setStatus("mandatory")
_MibProfBgpGlobal_Index_o_Type = Integer32
_MibProfBgpGlobal_Index_o_Object = MibScalar
mibProfBgpGlobal_Index_o = _MibProfBgpGlobal_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 1),
    _MibProfBgpGlobal_Index_o_Type()
)
mibProfBgpGlobal_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_Index_o.setStatus("mandatory")


class _MibProfBgpGlobal_Enable_Type(Integer32):
    """Custom type mibProfBgpGlobal_Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpGlobal_Enable_Type.__name__ = "Integer32"
_MibProfBgpGlobal_Enable_Object = MibScalar
mibProfBgpGlobal_Enable = _MibProfBgpGlobal_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 2),
    _MibProfBgpGlobal_Enable_Type()
)
mibProfBgpGlobal_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_Enable.setStatus("mandatory")
_MibProfBgpGlobal_AutonomousSystem_Type = Integer32
_MibProfBgpGlobal_AutonomousSystem_Object = MibScalar
mibProfBgpGlobal_AutonomousSystem = _MibProfBgpGlobal_AutonomousSystem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 3),
    _MibProfBgpGlobal_AutonomousSystem_Type()
)
mibProfBgpGlobal_AutonomousSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_AutonomousSystem.setStatus("mandatory")
_MibProfBgpGlobal_Id_Type = IpAddress
_MibProfBgpGlobal_Id_Object = MibScalar
mibProfBgpGlobal_Id = _MibProfBgpGlobal_Id_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 4),
    _MibProfBgpGlobal_Id_Type()
)
mibProfBgpGlobal_Id.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_Id.setStatus("mandatory")
_MibProfBgpGlobal_ConnectRetryInterval_Type = Integer32
_MibProfBgpGlobal_ConnectRetryInterval_Object = MibScalar
mibProfBgpGlobal_ConnectRetryInterval = _MibProfBgpGlobal_ConnectRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 5),
    _MibProfBgpGlobal_ConnectRetryInterval_Type()
)
mibProfBgpGlobal_ConnectRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_ConnectRetryInterval.setStatus("mandatory")
_MibProfBgpGlobal_KeepaliveTime_Type = Integer32
_MibProfBgpGlobal_KeepaliveTime_Object = MibScalar
mibProfBgpGlobal_KeepaliveTime = _MibProfBgpGlobal_KeepaliveTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 6),
    _MibProfBgpGlobal_KeepaliveTime_Type()
)
mibProfBgpGlobal_KeepaliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_KeepaliveTime.setStatus("mandatory")
_MibProfBgpGlobal_HoldTime_Type = Integer32
_MibProfBgpGlobal_HoldTime_Object = MibScalar
mibProfBgpGlobal_HoldTime = _MibProfBgpGlobal_HoldTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 7),
    _MibProfBgpGlobal_HoldTime_Type()
)
mibProfBgpGlobal_HoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_HoldTime.setStatus("mandatory")
_MibProfBgpGlobal_ClusterId_Type = IpAddress
_MibProfBgpGlobal_ClusterId_Object = MibScalar
mibProfBgpGlobal_ClusterId = _MibProfBgpGlobal_ClusterId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 9),
    _MibProfBgpGlobal_ClusterId_Type()
)
mibProfBgpGlobal_ClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_ClusterId.setStatus("mandatory")


class _MibProfBgpGlobal_IgpLockstep_Type(Integer32):
    """Custom type mibProfBgpGlobal_IgpLockstep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpGlobal_IgpLockstep_Type.__name__ = "Integer32"
_MibProfBgpGlobal_IgpLockstep_Object = MibScalar
mibProfBgpGlobal_IgpLockstep = _MibProfBgpGlobal_IgpLockstep_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 10),
    _MibProfBgpGlobal_IgpLockstep_Type()
)
mibProfBgpGlobal_IgpLockstep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_IgpLockstep.setStatus("mandatory")


class _MibProfBgpGlobal_Action_o_Type(Integer32):
    """Custom type mibProfBgpGlobal_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MibProfBgpGlobal_Action_o_Type.__name__ = "Integer32"
_MibProfBgpGlobal_Action_o_Object = MibScalar
mibProfBgpGlobal_Action_o = _MibProfBgpGlobal_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 11),
    _MibProfBgpGlobal_Action_o_Type()
)
mibProfBgpGlobal_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_Action_o.setStatus("mandatory")
_MibProfBgpGlobal_MaxMultiPaths_Type = Integer32
_MibProfBgpGlobal_MaxMultiPaths_Object = MibScalar
mibProfBgpGlobal_MaxMultiPaths = _MibProfBgpGlobal_MaxMultiPaths_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 13),
    _MibProfBgpGlobal_MaxMultiPaths_Type()
)
mibProfBgpGlobal_MaxMultiPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_MaxMultiPaths.setStatus("mandatory")
_MibProfBgpGlobal_StaticRouteRedistPolicy_Type = DisplayString
_MibProfBgpGlobal_StaticRouteRedistPolicy_Object = MibScalar
mibProfBgpGlobal_StaticRouteRedistPolicy = _MibProfBgpGlobal_StaticRouteRedistPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 14),
    _MibProfBgpGlobal_StaticRouteRedistPolicy_Type()
)
mibProfBgpGlobal_StaticRouteRedistPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_StaticRouteRedistPolicy.setStatus("mandatory")
_MibProfBgpGlobal_ConnRouteRedistPolicy_Type = DisplayString
_MibProfBgpGlobal_ConnRouteRedistPolicy_Object = MibScalar
mibProfBgpGlobal_ConnRouteRedistPolicy = _MibProfBgpGlobal_ConnRouteRedistPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 15),
    _MibProfBgpGlobal_ConnRouteRedistPolicy_Type()
)
mibProfBgpGlobal_ConnRouteRedistPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_ConnRouteRedistPolicy.setStatus("mandatory")
_MibProfBgpGlobal_SubAs_Type = Integer32
_MibProfBgpGlobal_SubAs_Object = MibScalar
mibProfBgpGlobal_SubAs = _MibProfBgpGlobal_SubAs_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 16),
    _MibProfBgpGlobal_SubAs_Type()
)
mibProfBgpGlobal_SubAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_SubAs.setStatus("mandatory")
_MibProfBgpGlobal_LocalPrefDefault_Type = Integer32
_MibProfBgpGlobal_LocalPrefDefault_Object = MibScalar
mibProfBgpGlobal_LocalPrefDefault = _MibProfBgpGlobal_LocalPrefDefault_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 17),
    _MibProfBgpGlobal_LocalPrefDefault_Type()
)
mibProfBgpGlobal_LocalPrefDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_LocalPrefDefault.setStatus("mandatory")


class _MibProfBgpGlobal_AlwaysCompareMed_Type(Integer32):
    """Custom type mibProfBgpGlobal_AlwaysCompareMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpGlobal_AlwaysCompareMed_Type.__name__ = "Integer32"
_MibProfBgpGlobal_AlwaysCompareMed_Object = MibScalar
mibProfBgpGlobal_AlwaysCompareMed = _MibProfBgpGlobal_AlwaysCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 18),
    _MibProfBgpGlobal_AlwaysCompareMed_Type()
)
mibProfBgpGlobal_AlwaysCompareMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpGlobal_AlwaysCompareMed.setStatus("mandatory")
_MibmibProfBgpPeer_ObjectIdentity = ObjectIdentity
mibmibProfBgpPeer = _MibmibProfBgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 58)
)
_MibmibProfBgpPeerTable_Object = MibTable
mibmibProfBgpPeerTable = _MibmibProfBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1)
)
if mibBuilder.loadTexts:
    mibmibProfBgpPeerTable.setStatus("mandatory")
_MibmibProfBgpPeerEntry_Object = MibTableRow
mibmibProfBgpPeerEntry = _MibmibProfBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1)
)
mibmibProfBgpPeerEntry.setIndexNames(
    (0, "ASCEND-MIBBGP-MIB", "mibProfBgpPeer-PeerName"),
)
if mibBuilder.loadTexts:
    mibmibProfBgpPeerEntry.setStatus("mandatory")
_MibProfBgpPeer_AutonomousSystem_Type = Integer32
_MibProfBgpPeer_AutonomousSystem_Object = MibScalar
mibProfBgpPeer_AutonomousSystem = _MibProfBgpPeer_AutonomousSystem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 3),
    _MibProfBgpPeer_AutonomousSystem_Type()
)
mibProfBgpPeer_AutonomousSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_AutonomousSystem.setStatus("mandatory")


class _MibProfBgpPeer_Enable_Type(Integer32):
    """Custom type mibProfBgpPeer_Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpPeer_Enable_Type.__name__ = "Integer32"
_MibProfBgpPeer_Enable_Object = MibScalar
mibProfBgpPeer_Enable = _MibProfBgpPeer_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 4),
    _MibProfBgpPeer_Enable_Type()
)
mibProfBgpPeer_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_Enable.setStatus("mandatory")


class _MibProfBgpPeer_AlwaysNextHop_Type(Integer32):
    """Custom type mibProfBgpPeer_AlwaysNextHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpPeer_AlwaysNextHop_Type.__name__ = "Integer32"
_MibProfBgpPeer_AlwaysNextHop_Object = MibScalar
mibProfBgpPeer_AlwaysNextHop = _MibProfBgpPeer_AlwaysNextHop_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 6),
    _MibProfBgpPeer_AlwaysNextHop_Type()
)
mibProfBgpPeer_AlwaysNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_AlwaysNextHop.setStatus("mandatory")


class _MibProfBgpPeer_RouteReflectorClient_Type(Integer32):
    """Custom type mibProfBgpPeer_RouteReflectorClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpPeer_RouteReflectorClient_Type.__name__ = "Integer32"
_MibProfBgpPeer_RouteReflectorClient_Object = MibScalar
mibProfBgpPeer_RouteReflectorClient = _MibProfBgpPeer_RouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 7),
    _MibProfBgpPeer_RouteReflectorClient_Type()
)
mibProfBgpPeer_RouteReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_RouteReflectorClient.setStatus("mandatory")


class _MibProfBgpPeer_ConfederationMember_Type(Integer32):
    """Custom type mibProfBgpPeer_ConfederationMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpPeer_ConfederationMember_Type.__name__ = "Integer32"
_MibProfBgpPeer_ConfederationMember_Object = MibScalar
mibProfBgpPeer_ConfederationMember = _MibProfBgpPeer_ConfederationMember_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 8),
    _MibProfBgpPeer_ConfederationMember_Type()
)
mibProfBgpPeer_ConfederationMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_ConfederationMember.setStatus("mandatory")
_MibProfBgpPeer_AcceptPolicy_Type = DisplayString
_MibProfBgpPeer_AcceptPolicy_Object = MibScalar
mibProfBgpPeer_AcceptPolicy = _MibProfBgpPeer_AcceptPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 10),
    _MibProfBgpPeer_AcceptPolicy_Type()
)
mibProfBgpPeer_AcceptPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_AcceptPolicy.setStatus("mandatory")
_MibProfBgpPeer_InjectPolicy_Type = DisplayString
_MibProfBgpPeer_InjectPolicy_Object = MibScalar
mibProfBgpPeer_InjectPolicy = _MibProfBgpPeer_InjectPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 11),
    _MibProfBgpPeer_InjectPolicy_Type()
)
mibProfBgpPeer_InjectPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_InjectPolicy.setStatus("mandatory")
_MibProfBgpPeer_AdvertisePolicy_Type = DisplayString
_MibProfBgpPeer_AdvertisePolicy_Object = MibScalar
mibProfBgpPeer_AdvertisePolicy = _MibProfBgpPeer_AdvertisePolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 12),
    _MibProfBgpPeer_AdvertisePolicy_Type()
)
mibProfBgpPeer_AdvertisePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_AdvertisePolicy.setStatus("mandatory")


class _MibProfBgpPeer_Action_o_Type(Integer32):
    """Custom type mibProfBgpPeer_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MibProfBgpPeer_Action_o_Type.__name__ = "Integer32"
_MibProfBgpPeer_Action_o_Object = MibScalar
mibProfBgpPeer_Action_o = _MibProfBgpPeer_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 13),
    _MibProfBgpPeer_Action_o_Type()
)
mibProfBgpPeer_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_Action_o.setStatus("mandatory")
_MibProfBgpPeer_PeerName_Type = DisplayString
_MibProfBgpPeer_PeerName_Object = MibScalar
mibProfBgpPeer_PeerName = _MibProfBgpPeer_PeerName_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 14),
    _MibProfBgpPeer_PeerName_Type()
)
mibProfBgpPeer_PeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfBgpPeer_PeerName.setStatus("mandatory")
_MibProfBgpPeer_PeerIpAddress_Type = IpAddress
_MibProfBgpPeer_PeerIpAddress_Object = MibScalar
mibProfBgpPeer_PeerIpAddress = _MibProfBgpPeer_PeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 15),
    _MibProfBgpPeer_PeerIpAddress_Type()
)
mibProfBgpPeer_PeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_PeerIpAddress.setStatus("mandatory")
_MibProfBgpPeer_MyIpAddress_Type = IpAddress
_MibProfBgpPeer_MyIpAddress_Object = MibScalar
mibProfBgpPeer_MyIpAddress = _MibProfBgpPeer_MyIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 16),
    _MibProfBgpPeer_MyIpAddress_Type()
)
mibProfBgpPeer_MyIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_MyIpAddress.setStatus("mandatory")
_MibProfBgpPeer_DefaultGatewayMetric_Type = Integer32
_MibProfBgpPeer_DefaultGatewayMetric_Object = MibScalar
mibProfBgpPeer_DefaultGatewayMetric = _MibProfBgpPeer_DefaultGatewayMetric_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 17),
    _MibProfBgpPeer_DefaultGatewayMetric_Type()
)
mibProfBgpPeer_DefaultGatewayMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPeer_DefaultGatewayMetric.setStatus("mandatory")
_MibmibProfBgpSummary_ObjectIdentity = ObjectIdentity
mibmibProfBgpSummary = _MibmibProfBgpSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 59)
)
_MibmibProfBgpSummaryTable_Object = MibTable
mibmibProfBgpSummaryTable = _MibmibProfBgpSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 59, 1)
)
if mibBuilder.loadTexts:
    mibmibProfBgpSummaryTable.setStatus("mandatory")
_MibmibProfBgpSummaryEntry_Object = MibTableRow
mibmibProfBgpSummaryEntry = _MibmibProfBgpSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1)
)
mibmibProfBgpSummaryEntry.setIndexNames(
    (0, "ASCEND-MIBBGP-MIB", "mibProfBgpSummary-Prefix-IpAddress"),
    (0, "ASCEND-MIBBGP-MIB", "mibProfBgpSummary-Prefix-Netmask"),
)
if mibBuilder.loadTexts:
    mibmibProfBgpSummaryEntry.setStatus("mandatory")


class _MibProfBgpSummary_Action_o_Type(Integer32):
    """Custom type mibProfBgpSummary_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MibProfBgpSummary_Action_o_Type.__name__ = "Integer32"
_MibProfBgpSummary_Action_o_Object = MibScalar
mibProfBgpSummary_Action_o = _MibProfBgpSummary_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 7),
    _MibProfBgpSummary_Action_o_Type()
)
mibProfBgpSummary_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpSummary_Action_o.setStatus("mandatory")
_MibProfBgpSummary_Prefix_IpAddress_Type = IpAddress
_MibProfBgpSummary_Prefix_IpAddress_Object = MibScalar
mibProfBgpSummary_Prefix_IpAddress = _MibProfBgpSummary_Prefix_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 8),
    _MibProfBgpSummary_Prefix_IpAddress_Type()
)
mibProfBgpSummary_Prefix_IpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfBgpSummary_Prefix_IpAddress.setStatus("mandatory")


class _MibProfBgpSummary_Enable_Type(Integer32):
    """Custom type mibProfBgpSummary_Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MibProfBgpSummary_Enable_Type.__name__ = "Integer32"
_MibProfBgpSummary_Enable_Object = MibScalar
mibProfBgpSummary_Enable = _MibProfBgpSummary_Enable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 9),
    _MibProfBgpSummary_Enable_Type()
)
mibProfBgpSummary_Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpSummary_Enable.setStatus("mandatory")
_MibProfBgpSummary_Prefix_Netmask_Type = IpAddress
_MibProfBgpSummary_Prefix_Netmask_Object = MibScalar
mibProfBgpSummary_Prefix_Netmask = _MibProfBgpSummary_Prefix_Netmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 11),
    _MibProfBgpSummary_Prefix_Netmask_Type()
)
mibProfBgpSummary_Prefix_Netmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfBgpSummary_Prefix_Netmask.setStatus("mandatory")
_MibProfBgpSummary_SummarizationPolicy_Type = DisplayString
_MibProfBgpSummary_SummarizationPolicy_Object = MibScalar
mibProfBgpSummary_SummarizationPolicy = _MibProfBgpSummary_SummarizationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 12),
    _MibProfBgpSummary_SummarizationPolicy_Type()
)
mibProfBgpSummary_SummarizationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpSummary_SummarizationPolicy.setStatus("mandatory")
_MibmibProfBgpPolicy_ObjectIdentity = ObjectIdentity
mibmibProfBgpPolicy = _MibmibProfBgpPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 60)
)
_MibmibProfBgpPolicyTable_Object = MibTable
mibmibProfBgpPolicyTable = _MibmibProfBgpPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 1)
)
if mibBuilder.loadTexts:
    mibmibProfBgpPolicyTable.setStatus("mandatory")
_MibmibProfBgpPolicyEntry_Object = MibTableRow
mibmibProfBgpPolicyEntry = _MibmibProfBgpPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1)
)
mibmibProfBgpPolicyEntry.setIndexNames(
    (0, "ASCEND-MIBBGP-MIB", "mibProfBgpPolicy-Name"),
)
if mibBuilder.loadTexts:
    mibmibProfBgpPolicyEntry.setStatus("mandatory")
_MibProfBgpPolicy_Name_Type = DisplayString
_MibProfBgpPolicy_Name_Object = MibScalar
mibProfBgpPolicy_Name = _MibProfBgpPolicy_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1, 1),
    _MibProfBgpPolicy_Name_Type()
)
mibProfBgpPolicy_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfBgpPolicy_Name.setStatus("mandatory")


class _MibProfBgpPolicy_Action_o_Type(Integer32):
    """Custom type mibProfBgpPolicy_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_MibProfBgpPolicy_Action_o_Type.__name__ = "Integer32"
_MibProfBgpPolicy_Action_o_Object = MibScalar
mibProfBgpPolicy_Action_o = _MibProfBgpPolicy_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1, 2),
    _MibProfBgpPolicy_Action_o_Type()
)
mibProfBgpPolicy_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPolicy_Action_o.setStatus("mandatory")
_MibProfBgpPolicy_NextPolicy_Type = DisplayString
_MibProfBgpPolicy_NextPolicy_Object = MibScalar
mibProfBgpPolicy_NextPolicy = _MibProfBgpPolicy_NextPolicy_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1, 3),
    _MibProfBgpPolicy_NextPolicy_Type()
)
mibProfBgpPolicy_NextPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPolicy_NextPolicy.setStatus("mandatory")
_MibmibProfBgpPolicy_RuleTable_Object = MibTable
mibmibProfBgpPolicy_RuleTable = _MibmibProfBgpPolicy_RuleTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 2)
)
if mibBuilder.loadTexts:
    mibmibProfBgpPolicy_RuleTable.setStatus("mandatory")
_MibmibProfBgpPolicy_RuleEntry_Object = MibTableRow
mibmibProfBgpPolicy_RuleEntry = _MibmibProfBgpPolicy_RuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1)
)
mibmibProfBgpPolicy_RuleEntry.setIndexNames(
    (0, "ASCEND-MIBBGP-MIB", "mibProfBgpPolicy-Rule-Name"),
    (0, "ASCEND-MIBBGP-MIB", "mibProfBgpPolicy-Rule-Index-o"),
)
if mibBuilder.loadTexts:
    mibmibProfBgpPolicy_RuleEntry.setStatus("mandatory")
_MibProfBgpPolicy_Rule_Name_Type = DisplayString
_MibProfBgpPolicy_Rule_Name_Object = MibScalar
mibProfBgpPolicy_Rule_Name = _MibProfBgpPolicy_Rule_Name_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1, 1),
    _MibProfBgpPolicy_Rule_Name_Type()
)
mibProfBgpPolicy_Rule_Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfBgpPolicy_Rule_Name.setStatus("mandatory")
_MibProfBgpPolicy_Rule_Index_o_Type = Integer32
_MibProfBgpPolicy_Rule_Index_o_Object = MibScalar
mibProfBgpPolicy_Rule_Index_o = _MibProfBgpPolicy_Rule_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1, 2),
    _MibProfBgpPolicy_Rule_Index_o_Type()
)
mibProfBgpPolicy_Rule_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibProfBgpPolicy_Rule_Index_o.setStatus("mandatory")
_MibProfBgpPolicy_Rule_Type = DisplayString
_MibProfBgpPolicy_Rule_Object = MibScalar
mibProfBgpPolicy_Rule = _MibProfBgpPolicy_Rule_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1, 3),
    _MibProfBgpPolicy_Rule_Type()
)
mibProfBgpPolicy_Rule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mibProfBgpPolicy_Rule.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBBGP-MIB",
    **{"DisplayString": DisplayString,
       "mibmibProfBgpGlobal": mibmibProfBgpGlobal,
       "mibmibProfBgpGlobalTable": mibmibProfBgpGlobalTable,
       "mibmibProfBgpGlobalEntry": mibmibProfBgpGlobalEntry,
       "mibProfBgpGlobal-Index-o": mibProfBgpGlobal_Index_o,
       "mibProfBgpGlobal-Enable": mibProfBgpGlobal_Enable,
       "mibProfBgpGlobal-AutonomousSystem": mibProfBgpGlobal_AutonomousSystem,
       "mibProfBgpGlobal-Id": mibProfBgpGlobal_Id,
       "mibProfBgpGlobal-ConnectRetryInterval": mibProfBgpGlobal_ConnectRetryInterval,
       "mibProfBgpGlobal-KeepaliveTime": mibProfBgpGlobal_KeepaliveTime,
       "mibProfBgpGlobal-HoldTime": mibProfBgpGlobal_HoldTime,
       "mibProfBgpGlobal-ClusterId": mibProfBgpGlobal_ClusterId,
       "mibProfBgpGlobal-IgpLockstep": mibProfBgpGlobal_IgpLockstep,
       "mibProfBgpGlobal-Action-o": mibProfBgpGlobal_Action_o,
       "mibProfBgpGlobal-MaxMultiPaths": mibProfBgpGlobal_MaxMultiPaths,
       "mibProfBgpGlobal-StaticRouteRedistPolicy": mibProfBgpGlobal_StaticRouteRedistPolicy,
       "mibProfBgpGlobal-ConnRouteRedistPolicy": mibProfBgpGlobal_ConnRouteRedistPolicy,
       "mibProfBgpGlobal-SubAs": mibProfBgpGlobal_SubAs,
       "mibProfBgpGlobal-LocalPrefDefault": mibProfBgpGlobal_LocalPrefDefault,
       "mibProfBgpGlobal-AlwaysCompareMed": mibProfBgpGlobal_AlwaysCompareMed,
       "mibmibProfBgpPeer": mibmibProfBgpPeer,
       "mibmibProfBgpPeerTable": mibmibProfBgpPeerTable,
       "mibmibProfBgpPeerEntry": mibmibProfBgpPeerEntry,
       "mibProfBgpPeer-AutonomousSystem": mibProfBgpPeer_AutonomousSystem,
       "mibProfBgpPeer-Enable": mibProfBgpPeer_Enable,
       "mibProfBgpPeer-AlwaysNextHop": mibProfBgpPeer_AlwaysNextHop,
       "mibProfBgpPeer-RouteReflectorClient": mibProfBgpPeer_RouteReflectorClient,
       "mibProfBgpPeer-ConfederationMember": mibProfBgpPeer_ConfederationMember,
       "mibProfBgpPeer-AcceptPolicy": mibProfBgpPeer_AcceptPolicy,
       "mibProfBgpPeer-InjectPolicy": mibProfBgpPeer_InjectPolicy,
       "mibProfBgpPeer-AdvertisePolicy": mibProfBgpPeer_AdvertisePolicy,
       "mibProfBgpPeer-Action-o": mibProfBgpPeer_Action_o,
       "mibProfBgpPeer-PeerName": mibProfBgpPeer_PeerName,
       "mibProfBgpPeer-PeerIpAddress": mibProfBgpPeer_PeerIpAddress,
       "mibProfBgpPeer-MyIpAddress": mibProfBgpPeer_MyIpAddress,
       "mibProfBgpPeer-DefaultGatewayMetric": mibProfBgpPeer_DefaultGatewayMetric,
       "mibmibProfBgpSummary": mibmibProfBgpSummary,
       "mibmibProfBgpSummaryTable": mibmibProfBgpSummaryTable,
       "mibmibProfBgpSummaryEntry": mibmibProfBgpSummaryEntry,
       "mibProfBgpSummary-Action-o": mibProfBgpSummary_Action_o,
       "mibProfBgpSummary-Prefix-IpAddress": mibProfBgpSummary_Prefix_IpAddress,
       "mibProfBgpSummary-Enable": mibProfBgpSummary_Enable,
       "mibProfBgpSummary-Prefix-Netmask": mibProfBgpSummary_Prefix_Netmask,
       "mibProfBgpSummary-SummarizationPolicy": mibProfBgpSummary_SummarizationPolicy,
       "mibmibProfBgpPolicy": mibmibProfBgpPolicy,
       "mibmibProfBgpPolicyTable": mibmibProfBgpPolicyTable,
       "mibmibProfBgpPolicyEntry": mibmibProfBgpPolicyEntry,
       "mibProfBgpPolicy-Name": mibProfBgpPolicy_Name,
       "mibProfBgpPolicy-Action-o": mibProfBgpPolicy_Action_o,
       "mibProfBgpPolicy-NextPolicy": mibProfBgpPolicy_NextPolicy,
       "mibmibProfBgpPolicy-RuleTable": mibmibProfBgpPolicy_RuleTable,
       "mibmibProfBgpPolicy-RuleEntry": mibmibProfBgpPolicy_RuleEntry,
       "mibProfBgpPolicy-Rule-Name": mibProfBgpPolicy_Rule_Name,
       "mibProfBgpPolicy-Rule-Index-o": mibProfBgpPolicy_Rule_Index_o,
       "mibProfBgpPolicy-Rule": mibProfBgpPolicy_Rule}
)
