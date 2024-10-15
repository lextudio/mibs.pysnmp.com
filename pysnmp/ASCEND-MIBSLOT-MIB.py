# SNMP MIB module (ASCEND-MIBSLOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSLOT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:13 2024
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

_MibappOptionsProfile_ObjectIdentity = ObjectIdentity
mibappOptionsProfile = _MibappOptionsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 109)
)
_MibappOptionsProfileTable_Object = MibTable
mibappOptionsProfileTable = _MibappOptionsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 109, 1)
)
if mibBuilder.loadTexts:
    mibappOptionsProfileTable.setStatus("mandatory")
_MibappOptionsProfileEntry_Object = MibTableRow
mibappOptionsProfileEntry = _MibappOptionsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1)
)
mibappOptionsProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "appOptionsProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibappOptionsProfileEntry.setStatus("mandatory")
_AppOptionsProfile_Index_o_Type = Integer32
_AppOptionsProfile_Index_o_Object = MibScalar
appOptionsProfile_Index_o = _AppOptionsProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 1),
    _AppOptionsProfile_Index_o_Type()
)
appOptionsProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    appOptionsProfile_Index_o.setStatus("mandatory")


class _AppOptionsProfile_PwsEnabled_Type(Integer32):
    """Custom type appOptionsProfile_PwsEnabled based on Integer32"""
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


_AppOptionsProfile_PwsEnabled_Type.__name__ = "Integer32"
_AppOptionsProfile_PwsEnabled_Object = MibScalar
appOptionsProfile_PwsEnabled = _AppOptionsProfile_PwsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 2),
    _AppOptionsProfile_PwsEnabled_Type()
)
appOptionsProfile_PwsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appOptionsProfile_PwsEnabled.setStatus("mandatory")
_AppOptionsProfile_PwsHost_Type = IpAddress
_AppOptionsProfile_PwsHost_Object = MibScalar
appOptionsProfile_PwsHost = _AppOptionsProfile_PwsHost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 3),
    _AppOptionsProfile_PwsHost_Type()
)
appOptionsProfile_PwsHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appOptionsProfile_PwsHost.setStatus("mandatory")
_AppOptionsProfile_PwsPort_Type = Integer32
_AppOptionsProfile_PwsPort_Object = MibScalar
appOptionsProfile_PwsPort = _AppOptionsProfile_PwsPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 4),
    _AppOptionsProfile_PwsPort_Type()
)
appOptionsProfile_PwsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appOptionsProfile_PwsPort.setStatus("mandatory")


class _AppOptionsProfile_Action_o_Type(Integer32):
    """Custom type appOptionsProfile_Action_o based on Integer32"""
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


_AppOptionsProfile_Action_o_Type.__name__ = "Integer32"
_AppOptionsProfile_Action_o_Object = MibScalar
appOptionsProfile_Action_o = _AppOptionsProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 109, 1, 1, 5),
    _AppOptionsProfile_Action_o_Type()
)
appOptionsProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appOptionsProfile_Action_o.setStatus("mandatory")
_MibwanOptionsProfile_ObjectIdentity = ObjectIdentity
mibwanOptionsProfile = _MibwanOptionsProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 110)
)
_MibwanOptionsProfileTable_Object = MibTable
mibwanOptionsProfileTable = _MibwanOptionsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 1)
)
if mibBuilder.loadTexts:
    mibwanOptionsProfileTable.setStatus("mandatory")
_MibwanOptionsProfileEntry_Object = MibTableRow
mibwanOptionsProfileEntry = _MibwanOptionsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1)
)
mibwanOptionsProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "wanOptionsProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibwanOptionsProfileEntry.setStatus("mandatory")
_WanOptionsProfile_Index_o_Type = Integer32
_WanOptionsProfile_Index_o_Object = MibScalar
wanOptionsProfile_Index_o = _WanOptionsProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 1),
    _WanOptionsProfile_Index_o_Type()
)
wanOptionsProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanOptionsProfile_Index_o.setStatus("mandatory")
_WanOptionsProfile_DialPlan_Type = Integer32
_WanOptionsProfile_DialPlan_Object = MibScalar
wanOptionsProfile_DialPlan = _WanOptionsProfile_DialPlan_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 2),
    _WanOptionsProfile_DialPlan_Type()
)
wanOptionsProfile_DialPlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanOptionsProfile_DialPlan.setStatus("mandatory")


class _WanOptionsProfile_TrunkGroupsNa_Type(Integer32):
    """Custom type wanOptionsProfile_TrunkGroupsNa based on Integer32"""
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


_WanOptionsProfile_TrunkGroupsNa_Type.__name__ = "Integer32"
_WanOptionsProfile_TrunkGroupsNa_Object = MibScalar
wanOptionsProfile_TrunkGroupsNa = _WanOptionsProfile_TrunkGroupsNa_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 3),
    _WanOptionsProfile_TrunkGroupsNa_Type()
)
wanOptionsProfile_TrunkGroupsNa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanOptionsProfile_TrunkGroupsNa.setStatus("mandatory")


class _WanOptionsProfile_RingBack_Type(Integer32):
    """Custom type wanOptionsProfile_RingBack based on Integer32"""
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


_WanOptionsProfile_RingBack_Type.__name__ = "Integer32"
_WanOptionsProfile_RingBack_Object = MibScalar
wanOptionsProfile_RingBack = _WanOptionsProfile_RingBack_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 4),
    _WanOptionsProfile_RingBack_Type()
)
wanOptionsProfile_RingBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanOptionsProfile_RingBack.setStatus("mandatory")


class _WanOptionsProfile_Action_o_Type(Integer32):
    """Custom type wanOptionsProfile_Action_o based on Integer32"""
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


_WanOptionsProfile_Action_o_Type.__name__ = "Integer32"
_WanOptionsProfile_Action_o_Object = MibScalar
wanOptionsProfile_Action_o = _WanOptionsProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 1, 1, 5),
    _WanOptionsProfile_Action_o_Type()
)
wanOptionsProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanOptionsProfile_Action_o.setStatus("mandatory")
_MibwanOptionsProfile_EtherAnsNumberTable_Object = MibTable
mibwanOptionsProfile_EtherAnsNumberTable = _MibwanOptionsProfile_EtherAnsNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 2)
)
if mibBuilder.loadTexts:
    mibwanOptionsProfile_EtherAnsNumberTable.setStatus("mandatory")
_MibwanOptionsProfile_EtherAnsNumberEntry_Object = MibTableRow
mibwanOptionsProfile_EtherAnsNumberEntry = _MibwanOptionsProfile_EtherAnsNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1)
)
mibwanOptionsProfile_EtherAnsNumberEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "wanOptionsProfile-EtherAnsNumber-Index-o"),
    (0, "ASCEND-MIBSLOT-MIB", "wanOptionsProfile-EtherAnsNumber-Index1-o"),
)
if mibBuilder.loadTexts:
    mibwanOptionsProfile_EtherAnsNumberEntry.setStatus("mandatory")
_WanOptionsProfile_EtherAnsNumber_Index_o_Type = Integer32
_WanOptionsProfile_EtherAnsNumber_Index_o_Object = MibScalar
wanOptionsProfile_EtherAnsNumber_Index_o = _WanOptionsProfile_EtherAnsNumber_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1, 1),
    _WanOptionsProfile_EtherAnsNumber_Index_o_Type()
)
wanOptionsProfile_EtherAnsNumber_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanOptionsProfile_EtherAnsNumber_Index_o.setStatus("mandatory")
_WanOptionsProfile_EtherAnsNumber_Index1_o_Type = Integer32
_WanOptionsProfile_EtherAnsNumber_Index1_o_Object = MibScalar
wanOptionsProfile_EtherAnsNumber_Index1_o = _WanOptionsProfile_EtherAnsNumber_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1, 2),
    _WanOptionsProfile_EtherAnsNumber_Index1_o_Type()
)
wanOptionsProfile_EtherAnsNumber_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanOptionsProfile_EtherAnsNumber_Index1_o.setStatus("mandatory")
_WanOptionsProfile_EtherAnsNumber_Type = DisplayString
_WanOptionsProfile_EtherAnsNumber_Object = MibScalar
wanOptionsProfile_EtherAnsNumber = _WanOptionsProfile_EtherAnsNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 110, 2, 1, 3),
    _WanOptionsProfile_EtherAnsNumber_Type()
)
wanOptionsProfile_EtherAnsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanOptionsProfile_EtherAnsNumber.setStatus("mandatory")
_MibdhcpServerProfile_ObjectIdentity = ObjectIdentity
mibdhcpServerProfile = _MibdhcpServerProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 111)
)
_MibdhcpServerProfileTable_Object = MibTable
mibdhcpServerProfileTable = _MibdhcpServerProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1)
)
if mibBuilder.loadTexts:
    mibdhcpServerProfileTable.setStatus("mandatory")
_MibdhcpServerProfileEntry_Object = MibTableRow
mibdhcpServerProfileEntry = _MibdhcpServerProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1)
)
mibdhcpServerProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibdhcpServerProfileEntry.setStatus("mandatory")
_DhcpServerProfile_Index_o_Type = Integer32
_DhcpServerProfile_Index_o_Object = MibScalar
dhcpServerProfile_Index_o = _DhcpServerProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 1),
    _DhcpServerProfile_Index_o_Type()
)
dhcpServerProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerProfile_Index_o.setStatus("mandatory")


class _DhcpServerProfile_Enabled_Type(Integer32):
    """Custom type dhcpServerProfile_Enabled based on Integer32"""
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


_DhcpServerProfile_Enabled_Type.__name__ = "Integer32"
_DhcpServerProfile_Enabled_Object = MibScalar
dhcpServerProfile_Enabled = _DhcpServerProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 2),
    _DhcpServerProfile_Enabled_Type()
)
dhcpServerProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_Enabled.setStatus("mandatory")


class _DhcpServerProfile_PnpEnabled_Type(Integer32):
    """Custom type dhcpServerProfile_PnpEnabled based on Integer32"""
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


_DhcpServerProfile_PnpEnabled_Type.__name__ = "Integer32"
_DhcpServerProfile_PnpEnabled_Object = MibScalar
dhcpServerProfile_PnpEnabled = _DhcpServerProfile_PnpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 3),
    _DhcpServerProfile_PnpEnabled_Type()
)
dhcpServerProfile_PnpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_PnpEnabled.setStatus("mandatory")
_DhcpServerProfile_IpAddress_Type = IpAddress
_DhcpServerProfile_IpAddress_Object = MibScalar
dhcpServerProfile_IpAddress = _DhcpServerProfile_IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 4),
    _DhcpServerProfile_IpAddress_Type()
)
dhcpServerProfile_IpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_IpAddress.setStatus("mandatory")
_DhcpServerProfile_Netmask_Type = IpAddress
_DhcpServerProfile_Netmask_Object = MibScalar
dhcpServerProfile_Netmask = _DhcpServerProfile_Netmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 5),
    _DhcpServerProfile_Netmask_Type()
)
dhcpServerProfile_Netmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_Netmask.setStatus("mandatory")
_DhcpServerProfile_RenewalTime_Type = Integer32
_DhcpServerProfile_RenewalTime_Object = MibScalar
dhcpServerProfile_RenewalTime = _DhcpServerProfile_RenewalTime_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 6),
    _DhcpServerProfile_RenewalTime_Type()
)
dhcpServerProfile_RenewalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_RenewalTime.setStatus("mandatory")


class _DhcpServerProfile_BecomeDefRouter_Type(Integer32):
    """Custom type dhcpServerProfile_BecomeDefRouter based on Integer32"""
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


_DhcpServerProfile_BecomeDefRouter_Type.__name__ = "Integer32"
_DhcpServerProfile_BecomeDefRouter_Object = MibScalar
dhcpServerProfile_BecomeDefRouter = _DhcpServerProfile_BecomeDefRouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 7),
    _DhcpServerProfile_BecomeDefRouter_Type()
)
dhcpServerProfile_BecomeDefRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_BecomeDefRouter.setStatus("mandatory")


class _DhcpServerProfile_DialIfLinkDown_Type(Integer32):
    """Custom type dhcpServerProfile_DialIfLinkDown based on Integer32"""
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


_DhcpServerProfile_DialIfLinkDown_Type.__name__ = "Integer32"
_DhcpServerProfile_DialIfLinkDown_Object = MibScalar
dhcpServerProfile_DialIfLinkDown = _DhcpServerProfile_DialIfLinkDown_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 8),
    _DhcpServerProfile_DialIfLinkDown_Type()
)
dhcpServerProfile_DialIfLinkDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_DialIfLinkDown.setStatus("mandatory")


class _DhcpServerProfile_AlwaysSpoof_Type(Integer32):
    """Custom type dhcpServerProfile_AlwaysSpoof based on Integer32"""
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


_DhcpServerProfile_AlwaysSpoof_Type.__name__ = "Integer32"
_DhcpServerProfile_AlwaysSpoof_Object = MibScalar
dhcpServerProfile_AlwaysSpoof = _DhcpServerProfile_AlwaysSpoof_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 9),
    _DhcpServerProfile_AlwaysSpoof_Type()
)
dhcpServerProfile_AlwaysSpoof.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_AlwaysSpoof.setStatus("mandatory")


class _DhcpServerProfile_ValidateIp_Type(Integer32):
    """Custom type dhcpServerProfile_ValidateIp based on Integer32"""
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


_DhcpServerProfile_ValidateIp_Type.__name__ = "Integer32"
_DhcpServerProfile_ValidateIp_Object = MibScalar
dhcpServerProfile_ValidateIp = _DhcpServerProfile_ValidateIp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 10),
    _DhcpServerProfile_ValidateIp_Type()
)
dhcpServerProfile_ValidateIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_ValidateIp.setStatus("mandatory")
_DhcpServerProfile_MaxNoReplyWait_Type = Integer32
_DhcpServerProfile_MaxNoReplyWait_Object = MibScalar
dhcpServerProfile_MaxNoReplyWait = _DhcpServerProfile_MaxNoReplyWait_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 11),
    _DhcpServerProfile_MaxNoReplyWait_Type()
)
dhcpServerProfile_MaxNoReplyWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_MaxNoReplyWait.setStatus("mandatory")
_DhcpServerProfile_GroupOneCount_Type = Integer32
_DhcpServerProfile_GroupOneCount_Object = MibScalar
dhcpServerProfile_GroupOneCount = _DhcpServerProfile_GroupOneCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 12),
    _DhcpServerProfile_GroupOneCount_Type()
)
dhcpServerProfile_GroupOneCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_GroupOneCount.setStatus("mandatory")
_DhcpServerProfile_IpGroupTwo_Type = IpAddress
_DhcpServerProfile_IpGroupTwo_Object = MibScalar
dhcpServerProfile_IpGroupTwo = _DhcpServerProfile_IpGroupTwo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 13),
    _DhcpServerProfile_IpGroupTwo_Type()
)
dhcpServerProfile_IpGroupTwo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_IpGroupTwo.setStatus("mandatory")
_DhcpServerProfile_GroupTwoCount_Type = Integer32
_DhcpServerProfile_GroupTwoCount_Object = MibScalar
dhcpServerProfile_GroupTwoCount = _DhcpServerProfile_GroupTwoCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 14),
    _DhcpServerProfile_GroupTwoCount_Type()
)
dhcpServerProfile_GroupTwoCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_GroupTwoCount.setStatus("mandatory")
_DhcpServerProfile_IpGroupTwoNetmask_Type = IpAddress
_DhcpServerProfile_IpGroupTwoNetmask_Object = MibScalar
dhcpServerProfile_IpGroupTwoNetmask = _DhcpServerProfile_IpGroupTwoNetmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 15),
    _DhcpServerProfile_IpGroupTwoNetmask_Type()
)
dhcpServerProfile_IpGroupTwoNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_IpGroupTwoNetmask.setStatus("mandatory")
_DhcpServerProfile_TftpHost_Type = DisplayString
_DhcpServerProfile_TftpHost_Object = MibScalar
dhcpServerProfile_TftpHost = _DhcpServerProfile_TftpHost_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 16),
    _DhcpServerProfile_TftpHost_Type()
)
dhcpServerProfile_TftpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_TftpHost.setStatus("mandatory")
_DhcpServerProfile_BootpPath_Type = DisplayString
_DhcpServerProfile_BootpPath_Object = MibScalar
dhcpServerProfile_BootpPath = _DhcpServerProfile_BootpPath_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 17),
    _DhcpServerProfile_BootpPath_Type()
)
dhcpServerProfile_BootpPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_BootpPath.setStatus("mandatory")


class _DhcpServerProfile_Action_o_Type(Integer32):
    """Custom type dhcpServerProfile_Action_o based on Integer32"""
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


_DhcpServerProfile_Action_o_Type.__name__ = "Integer32"
_DhcpServerProfile_Action_o_Object = MibScalar
dhcpServerProfile_Action_o = _DhcpServerProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 1, 1, 18),
    _DhcpServerProfile_Action_o_Type()
)
dhcpServerProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_Action_o.setStatus("mandatory")
_MibdhcpServerProfile_HostAddrTable_Object = MibTable
mibdhcpServerProfile_HostAddrTable = _MibdhcpServerProfile_HostAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 2)
)
if mibBuilder.loadTexts:
    mibdhcpServerProfile_HostAddrTable.setStatus("mandatory")
_MibdhcpServerProfile_HostAddrEntry_Object = MibTableRow
mibdhcpServerProfile_HostAddrEntry = _MibdhcpServerProfile_HostAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1)
)
mibdhcpServerProfile_HostAddrEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostAddr-Index-o"),
    (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostAddr-Index1-o"),
)
if mibBuilder.loadTexts:
    mibdhcpServerProfile_HostAddrEntry.setStatus("mandatory")
_DhcpServerProfile_HostAddr_Index_o_Type = Integer32
_DhcpServerProfile_HostAddr_Index_o_Object = MibScalar
dhcpServerProfile_HostAddr_Index_o = _DhcpServerProfile_HostAddr_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1, 1),
    _DhcpServerProfile_HostAddr_Index_o_Type()
)
dhcpServerProfile_HostAddr_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostAddr_Index_o.setStatus("mandatory")
_DhcpServerProfile_HostAddr_Index1_o_Type = Integer32
_DhcpServerProfile_HostAddr_Index1_o_Object = MibScalar
dhcpServerProfile_HostAddr_Index1_o = _DhcpServerProfile_HostAddr_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1, 2),
    _DhcpServerProfile_HostAddr_Index1_o_Type()
)
dhcpServerProfile_HostAddr_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostAddr_Index1_o.setStatus("mandatory")
_DhcpServerProfile_HostAddr_Type = DisplayString
_DhcpServerProfile_HostAddr_Object = MibScalar
dhcpServerProfile_HostAddr = _DhcpServerProfile_HostAddr_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 2, 1, 3),
    _DhcpServerProfile_HostAddr_Type()
)
dhcpServerProfile_HostAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostAddr.setStatus("mandatory")
_MibdhcpServerProfile_HostNetmaskTable_Object = MibTable
mibdhcpServerProfile_HostNetmaskTable = _MibdhcpServerProfile_HostNetmaskTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 3)
)
if mibBuilder.loadTexts:
    mibdhcpServerProfile_HostNetmaskTable.setStatus("mandatory")
_MibdhcpServerProfile_HostNetmaskEntry_Object = MibTableRow
mibdhcpServerProfile_HostNetmaskEntry = _MibdhcpServerProfile_HostNetmaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1)
)
mibdhcpServerProfile_HostNetmaskEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostNetmask-Index-o"),
    (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostNetmask-Index1-o"),
)
if mibBuilder.loadTexts:
    mibdhcpServerProfile_HostNetmaskEntry.setStatus("mandatory")
_DhcpServerProfile_HostNetmask_Index_o_Type = Integer32
_DhcpServerProfile_HostNetmask_Index_o_Object = MibScalar
dhcpServerProfile_HostNetmask_Index_o = _DhcpServerProfile_HostNetmask_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1, 1),
    _DhcpServerProfile_HostNetmask_Index_o_Type()
)
dhcpServerProfile_HostNetmask_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostNetmask_Index_o.setStatus("mandatory")
_DhcpServerProfile_HostNetmask_Index1_o_Type = Integer32
_DhcpServerProfile_HostNetmask_Index1_o_Object = MibScalar
dhcpServerProfile_HostNetmask_Index1_o = _DhcpServerProfile_HostNetmask_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1, 2),
    _DhcpServerProfile_HostNetmask_Index1_o_Type()
)
dhcpServerProfile_HostNetmask_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostNetmask_Index1_o.setStatus("mandatory")
_DhcpServerProfile_HostNetmask_Type = IpAddress
_DhcpServerProfile_HostNetmask_Object = MibScalar
dhcpServerProfile_HostNetmask = _DhcpServerProfile_HostNetmask_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 3, 1, 3),
    _DhcpServerProfile_HostNetmask_Type()
)
dhcpServerProfile_HostNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostNetmask.setStatus("mandatory")
_MibdhcpServerProfile_HostIpTable_Object = MibTable
mibdhcpServerProfile_HostIpTable = _MibdhcpServerProfile_HostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 4)
)
if mibBuilder.loadTexts:
    mibdhcpServerProfile_HostIpTable.setStatus("mandatory")
_MibdhcpServerProfile_HostIpEntry_Object = MibTableRow
mibdhcpServerProfile_HostIpEntry = _MibdhcpServerProfile_HostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1)
)
mibdhcpServerProfile_HostIpEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostIp-Index-o"),
    (0, "ASCEND-MIBSLOT-MIB", "dhcpServerProfile-HostIp-Index1-o"),
)
if mibBuilder.loadTexts:
    mibdhcpServerProfile_HostIpEntry.setStatus("mandatory")
_DhcpServerProfile_HostIp_Index_o_Type = Integer32
_DhcpServerProfile_HostIp_Index_o_Object = MibScalar
dhcpServerProfile_HostIp_Index_o = _DhcpServerProfile_HostIp_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1, 1),
    _DhcpServerProfile_HostIp_Index_o_Type()
)
dhcpServerProfile_HostIp_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostIp_Index_o.setStatus("mandatory")
_DhcpServerProfile_HostIp_Index1_o_Type = Integer32
_DhcpServerProfile_HostIp_Index1_o_Object = MibScalar
dhcpServerProfile_HostIp_Index1_o = _DhcpServerProfile_HostIp_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1, 2),
    _DhcpServerProfile_HostIp_Index1_o_Type()
)
dhcpServerProfile_HostIp_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostIp_Index1_o.setStatus("mandatory")
_DhcpServerProfile_HostIp_Type = IpAddress
_DhcpServerProfile_HostIp_Object = MibScalar
dhcpServerProfile_HostIp = _DhcpServerProfile_HostIp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 111, 4, 1, 3),
    _DhcpServerProfile_HostIp_Type()
)
dhcpServerProfile_HostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerProfile_HostIp.setStatus("mandatory")
_MibtcpModemProfile_ObjectIdentity = ObjectIdentity
mibtcpModemProfile = _MibtcpModemProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 112)
)
_MibtcpModemProfileTable_Object = MibTable
mibtcpModemProfileTable = _MibtcpModemProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 112, 1)
)
if mibBuilder.loadTexts:
    mibtcpModemProfileTable.setStatus("mandatory")
_MibtcpModemProfileEntry_Object = MibTableRow
mibtcpModemProfileEntry = _MibtcpModemProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1)
)
mibtcpModemProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "tcpModemProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibtcpModemProfileEntry.setStatus("mandatory")
_TcpModemProfile_Index_o_Type = Integer32
_TcpModemProfile_Index_o_Object = MibScalar
tcpModemProfile_Index_o = _TcpModemProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 1),
    _TcpModemProfile_Index_o_Type()
)
tcpModemProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpModemProfile_Index_o.setStatus("mandatory")


class _TcpModemProfile_Enabled_Type(Integer32):
    """Custom type tcpModemProfile_Enabled based on Integer32"""
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


_TcpModemProfile_Enabled_Type.__name__ = "Integer32"
_TcpModemProfile_Enabled_Object = MibScalar
tcpModemProfile_Enabled = _TcpModemProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 2),
    _TcpModemProfile_Enabled_Type()
)
tcpModemProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpModemProfile_Enabled.setStatus("mandatory")
_TcpModemProfile_Port_Type = Integer32
_TcpModemProfile_Port_Object = MibScalar
tcpModemProfile_Port = _TcpModemProfile_Port_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 3),
    _TcpModemProfile_Port_Type()
)
tcpModemProfile_Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpModemProfile_Port.setStatus("mandatory")


class _TcpModemProfile_Action_o_Type(Integer32):
    """Custom type tcpModemProfile_Action_o based on Integer32"""
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


_TcpModemProfile_Action_o_Type.__name__ = "Integer32"
_TcpModemProfile_Action_o_Object = MibScalar
tcpModemProfile_Action_o = _TcpModemProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 112, 1, 1, 4),
    _TcpModemProfile_Action_o_Type()
)
tcpModemProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpModemProfile_Action_o.setStatus("mandatory")
_MibdnisProfile_ObjectIdentity = ObjectIdentity
mibdnisProfile = _MibdnisProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 113)
)
_MibdnisProfileTable_Object = MibTable
mibdnisProfileTable = _MibdnisProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 1)
)
if mibBuilder.loadTexts:
    mibdnisProfileTable.setStatus("mandatory")
_MibdnisProfileEntry_Object = MibTableRow
mibdnisProfileEntry = _MibdnisProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1)
)
mibdnisProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "dnisProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibdnisProfileEntry.setStatus("mandatory")
_DnisProfile_Index_o_Type = Integer32
_DnisProfile_Index_o_Object = MibScalar
dnisProfile_Index_o = _DnisProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1, 1),
    _DnisProfile_Index_o_Type()
)
dnisProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisProfile_Index_o.setStatus("mandatory")


class _DnisProfile_Enabled_Type(Integer32):
    """Custom type dnisProfile_Enabled based on Integer32"""
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


_DnisProfile_Enabled_Type.__name__ = "Integer32"
_DnisProfile_Enabled_Object = MibScalar
dnisProfile_Enabled = _DnisProfile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1, 2),
    _DnisProfile_Enabled_Type()
)
dnisProfile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisProfile_Enabled.setStatus("mandatory")


class _DnisProfile_Action_o_Type(Integer32):
    """Custom type dnisProfile_Action_o based on Integer32"""
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


_DnisProfile_Action_o_Type.__name__ = "Integer32"
_DnisProfile_Action_o_Object = MibScalar
dnisProfile_Action_o = _DnisProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 1, 1, 3),
    _DnisProfile_Action_o_Type()
)
dnisProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisProfile_Action_o.setStatus("mandatory")
_MibdnisProfile_DnisTabTable_Object = MibTable
mibdnisProfile_DnisTabTable = _MibdnisProfile_DnisTabTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2)
)
if mibBuilder.loadTexts:
    mibdnisProfile_DnisTabTable.setStatus("mandatory")
_MibdnisProfile_DnisTabEntry_Object = MibTableRow
mibdnisProfile_DnisTabEntry = _MibdnisProfile_DnisTabEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1)
)
mibdnisProfile_DnisTabEntry.setIndexNames(
    (0, "ASCEND-MIBSLOT-MIB", "dnisProfile-DnisTab-Index-o"),
    (0, "ASCEND-MIBSLOT-MIB", "dnisProfile-DnisTab-Index1-o"),
)
if mibBuilder.loadTexts:
    mibdnisProfile_DnisTabEntry.setStatus("mandatory")
_DnisProfile_DnisTab_Index_o_Type = Integer32
_DnisProfile_DnisTab_Index_o_Object = MibScalar
dnisProfile_DnisTab_Index_o = _DnisProfile_DnisTab_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 1),
    _DnisProfile_DnisTab_Index_o_Type()
)
dnisProfile_DnisTab_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisProfile_DnisTab_Index_o.setStatus("mandatory")
_DnisProfile_DnisTab_Index1_o_Type = Integer32
_DnisProfile_DnisTab_Index1_o_Object = MibScalar
dnisProfile_DnisTab_Index1_o = _DnisProfile_DnisTab_Index1_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 2),
    _DnisProfile_DnisTab_Index1_o_Type()
)
dnisProfile_DnisTab_Index1_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnisProfile_DnisTab_Index1_o.setStatus("mandatory")
_DnisProfile_DnisTab_DnisNumber_Type = DisplayString
_DnisProfile_DnisTab_DnisNumber_Object = MibScalar
dnisProfile_DnisTab_DnisNumber = _DnisProfile_DnisTab_DnisNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 3),
    _DnisProfile_DnisTab_DnisNumber_Type()
)
dnisProfile_DnisTab_DnisNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisProfile_DnisTab_DnisNumber.setStatus("mandatory")
_DnisProfile_DnisTab_DnisMaxCalls_Type = Integer32
_DnisProfile_DnisTab_DnisMaxCalls_Object = MibScalar
dnisProfile_DnisTab_DnisMaxCalls = _DnisProfile_DnisTab_DnisMaxCalls_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 4),
    _DnisProfile_DnisTab_DnisMaxCalls_Type()
)
dnisProfile_DnisTab_DnisMaxCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisProfile_DnisTab_DnisMaxCalls.setStatus("mandatory")
_DnisProfile_DnisTab_DnisMaxCallsModem_Type = Integer32
_DnisProfile_DnisTab_DnisMaxCallsModem_Object = MibScalar
dnisProfile_DnisTab_DnisMaxCallsModem = _DnisProfile_DnisTab_DnisMaxCallsModem_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 5),
    _DnisProfile_DnisTab_DnisMaxCallsModem_Type()
)
dnisProfile_DnisTab_DnisMaxCallsModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisProfile_DnisTab_DnisMaxCallsModem.setStatus("mandatory")
_DnisProfile_DnisTab_DnisMaxCallsHdlc_Type = Integer32
_DnisProfile_DnisTab_DnisMaxCallsHdlc_Object = MibScalar
dnisProfile_DnisTab_DnisMaxCallsHdlc = _DnisProfile_DnisTab_DnisMaxCallsHdlc_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 6),
    _DnisProfile_DnisTab_DnisMaxCallsHdlc_Type()
)
dnisProfile_DnisTab_DnisMaxCallsHdlc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisProfile_DnisTab_DnisMaxCallsHdlc.setStatus("mandatory")
_DnisProfile_DnisTab_DnisMaxCallsV110_Type = Integer32
_DnisProfile_DnisTab_DnisMaxCallsV110_Object = MibScalar
dnisProfile_DnisTab_DnisMaxCallsV110 = _DnisProfile_DnisTab_DnisMaxCallsV110_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 113, 2, 1, 7),
    _DnisProfile_DnisTab_DnisMaxCallsV110_Type()
)
dnisProfile_DnisTab_DnisMaxCallsV110.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnisProfile_DnisTab_DnisMaxCallsV110.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSLOT-MIB",
    **{"DisplayString": DisplayString,
       "mibappOptionsProfile": mibappOptionsProfile,
       "mibappOptionsProfileTable": mibappOptionsProfileTable,
       "mibappOptionsProfileEntry": mibappOptionsProfileEntry,
       "appOptionsProfile-Index-o": appOptionsProfile_Index_o,
       "appOptionsProfile-PwsEnabled": appOptionsProfile_PwsEnabled,
       "appOptionsProfile-PwsHost": appOptionsProfile_PwsHost,
       "appOptionsProfile-PwsPort": appOptionsProfile_PwsPort,
       "appOptionsProfile-Action-o": appOptionsProfile_Action_o,
       "mibwanOptionsProfile": mibwanOptionsProfile,
       "mibwanOptionsProfileTable": mibwanOptionsProfileTable,
       "mibwanOptionsProfileEntry": mibwanOptionsProfileEntry,
       "wanOptionsProfile-Index-o": wanOptionsProfile_Index_o,
       "wanOptionsProfile-DialPlan": wanOptionsProfile_DialPlan,
       "wanOptionsProfile-TrunkGroupsNa": wanOptionsProfile_TrunkGroupsNa,
       "wanOptionsProfile-RingBack": wanOptionsProfile_RingBack,
       "wanOptionsProfile-Action-o": wanOptionsProfile_Action_o,
       "mibwanOptionsProfile-EtherAnsNumberTable": mibwanOptionsProfile_EtherAnsNumberTable,
       "mibwanOptionsProfile-EtherAnsNumberEntry": mibwanOptionsProfile_EtherAnsNumberEntry,
       "wanOptionsProfile-EtherAnsNumber-Index-o": wanOptionsProfile_EtherAnsNumber_Index_o,
       "wanOptionsProfile-EtherAnsNumber-Index1-o": wanOptionsProfile_EtherAnsNumber_Index1_o,
       "wanOptionsProfile-EtherAnsNumber": wanOptionsProfile_EtherAnsNumber,
       "mibdhcpServerProfile": mibdhcpServerProfile,
       "mibdhcpServerProfileTable": mibdhcpServerProfileTable,
       "mibdhcpServerProfileEntry": mibdhcpServerProfileEntry,
       "dhcpServerProfile-Index-o": dhcpServerProfile_Index_o,
       "dhcpServerProfile-Enabled": dhcpServerProfile_Enabled,
       "dhcpServerProfile-PnpEnabled": dhcpServerProfile_PnpEnabled,
       "dhcpServerProfile-IpAddress": dhcpServerProfile_IpAddress,
       "dhcpServerProfile-Netmask": dhcpServerProfile_Netmask,
       "dhcpServerProfile-RenewalTime": dhcpServerProfile_RenewalTime,
       "dhcpServerProfile-BecomeDefRouter": dhcpServerProfile_BecomeDefRouter,
       "dhcpServerProfile-DialIfLinkDown": dhcpServerProfile_DialIfLinkDown,
       "dhcpServerProfile-AlwaysSpoof": dhcpServerProfile_AlwaysSpoof,
       "dhcpServerProfile-ValidateIp": dhcpServerProfile_ValidateIp,
       "dhcpServerProfile-MaxNoReplyWait": dhcpServerProfile_MaxNoReplyWait,
       "dhcpServerProfile-GroupOneCount": dhcpServerProfile_GroupOneCount,
       "dhcpServerProfile-IpGroupTwo": dhcpServerProfile_IpGroupTwo,
       "dhcpServerProfile-GroupTwoCount": dhcpServerProfile_GroupTwoCount,
       "dhcpServerProfile-IpGroupTwoNetmask": dhcpServerProfile_IpGroupTwoNetmask,
       "dhcpServerProfile-TftpHost": dhcpServerProfile_TftpHost,
       "dhcpServerProfile-BootpPath": dhcpServerProfile_BootpPath,
       "dhcpServerProfile-Action-o": dhcpServerProfile_Action_o,
       "mibdhcpServerProfile-HostAddrTable": mibdhcpServerProfile_HostAddrTable,
       "mibdhcpServerProfile-HostAddrEntry": mibdhcpServerProfile_HostAddrEntry,
       "dhcpServerProfile-HostAddr-Index-o": dhcpServerProfile_HostAddr_Index_o,
       "dhcpServerProfile-HostAddr-Index1-o": dhcpServerProfile_HostAddr_Index1_o,
       "dhcpServerProfile-HostAddr": dhcpServerProfile_HostAddr,
       "mibdhcpServerProfile-HostNetmaskTable": mibdhcpServerProfile_HostNetmaskTable,
       "mibdhcpServerProfile-HostNetmaskEntry": mibdhcpServerProfile_HostNetmaskEntry,
       "dhcpServerProfile-HostNetmask-Index-o": dhcpServerProfile_HostNetmask_Index_o,
       "dhcpServerProfile-HostNetmask-Index1-o": dhcpServerProfile_HostNetmask_Index1_o,
       "dhcpServerProfile-HostNetmask": dhcpServerProfile_HostNetmask,
       "mibdhcpServerProfile-HostIpTable": mibdhcpServerProfile_HostIpTable,
       "mibdhcpServerProfile-HostIpEntry": mibdhcpServerProfile_HostIpEntry,
       "dhcpServerProfile-HostIp-Index-o": dhcpServerProfile_HostIp_Index_o,
       "dhcpServerProfile-HostIp-Index1-o": dhcpServerProfile_HostIp_Index1_o,
       "dhcpServerProfile-HostIp": dhcpServerProfile_HostIp,
       "mibtcpModemProfile": mibtcpModemProfile,
       "mibtcpModemProfileTable": mibtcpModemProfileTable,
       "mibtcpModemProfileEntry": mibtcpModemProfileEntry,
       "tcpModemProfile-Index-o": tcpModemProfile_Index_o,
       "tcpModemProfile-Enabled": tcpModemProfile_Enabled,
       "tcpModemProfile-Port": tcpModemProfile_Port,
       "tcpModemProfile-Action-o": tcpModemProfile_Action_o,
       "mibdnisProfile": mibdnisProfile,
       "mibdnisProfileTable": mibdnisProfileTable,
       "mibdnisProfileEntry": mibdnisProfileEntry,
       "dnisProfile-Index-o": dnisProfile_Index_o,
       "dnisProfile-Enabled": dnisProfile_Enabled,
       "dnisProfile-Action-o": dnisProfile_Action_o,
       "mibdnisProfile-DnisTabTable": mibdnisProfile_DnisTabTable,
       "mibdnisProfile-DnisTabEntry": mibdnisProfile_DnisTabEntry,
       "dnisProfile-DnisTab-Index-o": dnisProfile_DnisTab_Index_o,
       "dnisProfile-DnisTab-Index1-o": dnisProfile_DnisTab_Index1_o,
       "dnisProfile-DnisTab-DnisNumber": dnisProfile_DnisTab_DnisNumber,
       "dnisProfile-DnisTab-DnisMaxCalls": dnisProfile_DnisTab_DnisMaxCalls,
       "dnisProfile-DnisTab-DnisMaxCallsModem": dnisProfile_DnisTab_DnisMaxCallsModem,
       "dnisProfile-DnisTab-DnisMaxCallsHdlc": dnisProfile_DnisTab_DnisMaxCallsHdlc,
       "dnisProfile-DnisTab-DnisMaxCallsV110": dnisProfile_DnisTab_DnisMaxCallsV110}
)
