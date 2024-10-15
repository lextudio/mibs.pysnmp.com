# SNMP MIB module (KEEPALIVED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KEEPALIVED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:38 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber,
 InetScopeType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber",
    "InetScopeType")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

keepalived = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5)
)
keepalived.setRevisions(
        ("2009-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VrrpState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("backup", 1),
          ("fault", 3),
          ("init", 0),
          ("master", 2),
          ("unknown", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Debian_ObjectIdentity = ObjectIdentity
debian = _Debian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586)
)
_Project_ObjectIdentity = ObjectIdentity
project = _Project_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100)
)
__pysmi_global_ObjectIdentity = ObjectIdentity
_pysmi_global = __pysmi_global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1)
)
_Version_Type = DisplayString
_Version_Object = MibScalar
version = _Version_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 1),
    _Version_Type()
)
version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    version.setStatus("current")
_RouterId_Type = DisplayString
_RouterId_Object = MibScalar
routerId = _RouterId_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 2),
    _RouterId_Type()
)
routerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerId.setStatus("current")
_Mail_ObjectIdentity = ObjectIdentity
mail = _Mail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3)
)
_SmtpServerAddressType_Type = InetAddressType
_SmtpServerAddressType_Object = MibScalar
smtpServerAddressType = _SmtpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 1),
    _SmtpServerAddressType_Type()
)
smtpServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerAddressType.setStatus("current")
_SmtpServerAddress_Type = InetAddress
_SmtpServerAddress_Object = MibScalar
smtpServerAddress = _SmtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 2),
    _SmtpServerAddress_Type()
)
smtpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerAddress.setStatus("current")
_SmtpServerTimeout_Type = Unsigned32
_SmtpServerTimeout_Object = MibScalar
smtpServerTimeout = _SmtpServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 3),
    _SmtpServerTimeout_Type()
)
smtpServerTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    smtpServerTimeout.setUnits("seconds")
_EmailFrom_Type = DisplayString
_EmailFrom_Object = MibScalar
emailFrom = _EmailFrom_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 4),
    _EmailFrom_Type()
)
emailFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailFrom.setStatus("current")
_EmailTable_Object = MibTable
emailTable = _EmailTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 5)
)
if mibBuilder.loadTexts:
    emailTable.setStatus("current")
_EmailEntry_Object = MibTableRow
emailEntry = _EmailEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 5, 1)
)
emailEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "emailIndex"),
)
if mibBuilder.loadTexts:
    emailEntry.setStatus("current")


class _EmailIndex_Type(Integer32):
    """Custom type emailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EmailIndex_Type.__name__ = "Integer32"
_EmailIndex_Object = MibTableColumn
emailIndex = _EmailIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 5, 1, 1),
    _EmailIndex_Type()
)
emailIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    emailIndex.setStatus("current")
_EmailAddress_Type = DisplayString
_EmailAddress_Object = MibTableColumn
emailAddress = _EmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 3, 5, 1, 2),
    _EmailAddress_Type()
)
emailAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailAddress.setStatus("current")


class _TrapEnable_Type(Integer32):
    """Custom type trapEnable based on Integer32"""
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


_TrapEnable_Type.__name__ = "Integer32"
_TrapEnable_Object = MibScalar
trapEnable = _TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 4),
    _TrapEnable_Type()
)
trapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEnable.setStatus("current")


class _LinkBeat_Type(Integer32):
    """Custom type linkBeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("netlink", 1),
          ("polling", 2))
    )


_LinkBeat_Type.__name__ = "Integer32"
_LinkBeat_Object = MibScalar
linkBeat = _LinkBeat_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 1, 5),
    _LinkBeat_Type()
)
linkBeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkBeat.setStatus("current")
_Vrrp_ObjectIdentity = ObjectIdentity
vrrp = _Vrrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2)
)
_VrrpSyncGroupTable_Object = MibTable
vrrpSyncGroupTable = _VrrpSyncGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1)
)
if mibBuilder.loadTexts:
    vrrpSyncGroupTable.setStatus("current")
_VrrpSyncGroupEntry_Object = MibTableRow
vrrpSyncGroupEntry = _VrrpSyncGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1)
)
vrrpSyncGroupEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpSyncGroupIndex"),
)
if mibBuilder.loadTexts:
    vrrpSyncGroupEntry.setStatus("current")


class _VrrpSyncGroupIndex_Type(Integer32):
    """Custom type vrrpSyncGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrrpSyncGroupIndex_Type.__name__ = "Integer32"
_VrrpSyncGroupIndex_Object = MibTableColumn
vrrpSyncGroupIndex = _VrrpSyncGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 1),
    _VrrpSyncGroupIndex_Type()
)
vrrpSyncGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpSyncGroupIndex.setStatus("current")
_VrrpSyncGroupName_Type = DisplayString
_VrrpSyncGroupName_Object = MibTableColumn
vrrpSyncGroupName = _VrrpSyncGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 2),
    _VrrpSyncGroupName_Type()
)
vrrpSyncGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupName.setStatus("current")
_VrrpSyncGroupState_Type = VrrpState
_VrrpSyncGroupState_Object = MibTableColumn
vrrpSyncGroupState = _VrrpSyncGroupState_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 3),
    _VrrpSyncGroupState_Type()
)
vrrpSyncGroupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupState.setStatus("current")


class _VrrpSyncGroupSmtpAlert_Type(Integer32):
    """Custom type vrrpSyncGroupSmtpAlert based on Integer32"""
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


_VrrpSyncGroupSmtpAlert_Type.__name__ = "Integer32"
_VrrpSyncGroupSmtpAlert_Object = MibTableColumn
vrrpSyncGroupSmtpAlert = _VrrpSyncGroupSmtpAlert_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 4),
    _VrrpSyncGroupSmtpAlert_Type()
)
vrrpSyncGroupSmtpAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupSmtpAlert.setStatus("current")


class _VrrpSyncGroupNotifyExec_Type(Integer32):
    """Custom type vrrpSyncGroupNotifyExec based on Integer32"""
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


_VrrpSyncGroupNotifyExec_Type.__name__ = "Integer32"
_VrrpSyncGroupNotifyExec_Object = MibTableColumn
vrrpSyncGroupNotifyExec = _VrrpSyncGroupNotifyExec_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 5),
    _VrrpSyncGroupNotifyExec_Type()
)
vrrpSyncGroupNotifyExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupNotifyExec.setStatus("current")
_VrrpSyncGroupScriptMaster_Type = DisplayString
_VrrpSyncGroupScriptMaster_Object = MibTableColumn
vrrpSyncGroupScriptMaster = _VrrpSyncGroupScriptMaster_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 6),
    _VrrpSyncGroupScriptMaster_Type()
)
vrrpSyncGroupScriptMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupScriptMaster.setStatus("current")
_VrrpSyncGroupScriptBackup_Type = DisplayString
_VrrpSyncGroupScriptBackup_Object = MibTableColumn
vrrpSyncGroupScriptBackup = _VrrpSyncGroupScriptBackup_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 7),
    _VrrpSyncGroupScriptBackup_Type()
)
vrrpSyncGroupScriptBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupScriptBackup.setStatus("current")
_VrrpSyncGroupScriptFault_Type = DisplayString
_VrrpSyncGroupScriptFault_Object = MibTableColumn
vrrpSyncGroupScriptFault = _VrrpSyncGroupScriptFault_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 8),
    _VrrpSyncGroupScriptFault_Type()
)
vrrpSyncGroupScriptFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupScriptFault.setStatus("current")
_VrrpSyncGroupScript_Type = DisplayString
_VrrpSyncGroupScript_Object = MibTableColumn
vrrpSyncGroupScript = _VrrpSyncGroupScript_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 1, 1, 9),
    _VrrpSyncGroupScript_Type()
)
vrrpSyncGroupScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupScript.setStatus("current")
_VrrpSyncGroupMemberTable_Object = MibTable
vrrpSyncGroupMemberTable = _VrrpSyncGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 2)
)
if mibBuilder.loadTexts:
    vrrpSyncGroupMemberTable.setStatus("current")
_VrrpSyncGroupMemberEntry_Object = MibTableRow
vrrpSyncGroupMemberEntry = _VrrpSyncGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 2, 1)
)
vrrpSyncGroupMemberEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpSyncGroupIndex"),
    (0, "KEEPALIVED-MIB", "vrrpSyncGroupMemberInstanceIndex"),
)
if mibBuilder.loadTexts:
    vrrpSyncGroupMemberEntry.setStatus("current")


class _VrrpSyncGroupMemberInstanceIndex_Type(Integer32):
    """Custom type vrrpSyncGroupMemberInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrrpSyncGroupMemberInstanceIndex_Type.__name__ = "Integer32"
_VrrpSyncGroupMemberInstanceIndex_Object = MibTableColumn
vrrpSyncGroupMemberInstanceIndex = _VrrpSyncGroupMemberInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 2, 1, 1),
    _VrrpSyncGroupMemberInstanceIndex_Type()
)
vrrpSyncGroupMemberInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpSyncGroupMemberInstanceIndex.setStatus("current")
_VrrpSyncGroupMemberName_Type = DisplayString
_VrrpSyncGroupMemberName_Object = MibTableColumn
vrrpSyncGroupMemberName = _VrrpSyncGroupMemberName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 2, 1, 2),
    _VrrpSyncGroupMemberName_Type()
)
vrrpSyncGroupMemberName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpSyncGroupMemberName.setStatus("current")
_VrrpInstanceTable_Object = MibTable
vrrpInstanceTable = _VrrpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3)
)
if mibBuilder.loadTexts:
    vrrpInstanceTable.setStatus("current")
_VrrpInstanceEntry_Object = MibTableRow
vrrpInstanceEntry = _VrrpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1)
)
vrrpInstanceEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpInstanceIndex"),
)
if mibBuilder.loadTexts:
    vrrpInstanceEntry.setStatus("current")


class _VrrpInstanceIndex_Type(Integer32):
    """Custom type vrrpInstanceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("static", 0)
    )


_VrrpInstanceIndex_Type.__name__ = "Integer32"
_VrrpInstanceIndex_Object = MibTableColumn
vrrpInstanceIndex = _VrrpInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 1),
    _VrrpInstanceIndex_Type()
)
vrrpInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpInstanceIndex.setStatus("current")
_VrrpInstanceName_Type = DisplayString
_VrrpInstanceName_Object = MibTableColumn
vrrpInstanceName = _VrrpInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 2),
    _VrrpInstanceName_Type()
)
vrrpInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceName.setStatus("current")
_VrrpInstanceVirtualRouterId_Type = Unsigned32
_VrrpInstanceVirtualRouterId_Object = MibTableColumn
vrrpInstanceVirtualRouterId = _VrrpInstanceVirtualRouterId_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 3),
    _VrrpInstanceVirtualRouterId_Type()
)
vrrpInstanceVirtualRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceVirtualRouterId.setStatus("current")
_VrrpInstanceState_Type = VrrpState
_VrrpInstanceState_Object = MibTableColumn
vrrpInstanceState = _VrrpInstanceState_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 4),
    _VrrpInstanceState_Type()
)
vrrpInstanceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceState.setStatus("current")
_VrrpInstanceInitialState_Type = VrrpState
_VrrpInstanceInitialState_Object = MibTableColumn
vrrpInstanceInitialState = _VrrpInstanceInitialState_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 5),
    _VrrpInstanceInitialState_Type()
)
vrrpInstanceInitialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceInitialState.setStatus("current")
_VrrpInstanceWantedState_Type = VrrpState
_VrrpInstanceWantedState_Object = MibTableColumn
vrrpInstanceWantedState = _VrrpInstanceWantedState_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 6),
    _VrrpInstanceWantedState_Type()
)
vrrpInstanceWantedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceWantedState.setStatus("current")
_VrrpInstanceBasePriority_Type = Integer32
_VrrpInstanceBasePriority_Object = MibTableColumn
vrrpInstanceBasePriority = _VrrpInstanceBasePriority_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 7),
    _VrrpInstanceBasePriority_Type()
)
vrrpInstanceBasePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpInstanceBasePriority.setStatus("current")
_VrrpInstanceEffectivePriority_Type = Integer32
_VrrpInstanceEffectivePriority_Object = MibTableColumn
vrrpInstanceEffectivePriority = _VrrpInstanceEffectivePriority_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 8),
    _VrrpInstanceEffectivePriority_Type()
)
vrrpInstanceEffectivePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceEffectivePriority.setStatus("current")


class _VrrpInstanceVipsStatus_Type(Integer32):
    """Custom type vrrpInstanceVipsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allSet", 1),
          ("notAllSet", 2))
    )


_VrrpInstanceVipsStatus_Type.__name__ = "Integer32"
_VrrpInstanceVipsStatus_Object = MibTableColumn
vrrpInstanceVipsStatus = _VrrpInstanceVipsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 9),
    _VrrpInstanceVipsStatus_Type()
)
vrrpInstanceVipsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceVipsStatus.setStatus("current")
_VrrpInstancePrimaryInterface_Type = DisplayString
_VrrpInstancePrimaryInterface_Object = MibTableColumn
vrrpInstancePrimaryInterface = _VrrpInstancePrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 10),
    _VrrpInstancePrimaryInterface_Type()
)
vrrpInstancePrimaryInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstancePrimaryInterface.setStatus("current")


class _VrrpInstanceTrackPrimaryIf_Type(Integer32):
    """Custom type vrrpInstanceTrackPrimaryIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTracked", 2),
          ("tracked", 1))
    )


_VrrpInstanceTrackPrimaryIf_Type.__name__ = "Integer32"
_VrrpInstanceTrackPrimaryIf_Object = MibTableColumn
vrrpInstanceTrackPrimaryIf = _VrrpInstanceTrackPrimaryIf_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 11),
    _VrrpInstanceTrackPrimaryIf_Type()
)
vrrpInstanceTrackPrimaryIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceTrackPrimaryIf.setStatus("current")
_VrrpInstanceAdvertisementsInt_Type = Unsigned32
_VrrpInstanceAdvertisementsInt_Object = MibTableColumn
vrrpInstanceAdvertisementsInt = _VrrpInstanceAdvertisementsInt_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 12),
    _VrrpInstanceAdvertisementsInt_Type()
)
vrrpInstanceAdvertisementsInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceAdvertisementsInt.setStatus("current")
if mibBuilder.loadTexts:
    vrrpInstanceAdvertisementsInt.setUnits("seconds")


class _VrrpInstancePreempt_Type(Integer32):
    """Custom type vrrpInstancePreempt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPreempt", 2),
          ("preempt", 1))
    )


_VrrpInstancePreempt_Type.__name__ = "Integer32"
_VrrpInstancePreempt_Object = MibTableColumn
vrrpInstancePreempt = _VrrpInstancePreempt_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 13),
    _VrrpInstancePreempt_Type()
)
vrrpInstancePreempt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrrpInstancePreempt.setStatus("current")
_VrrpInstancePreemptDelay_Type = Unsigned32
_VrrpInstancePreemptDelay_Object = MibTableColumn
vrrpInstancePreemptDelay = _VrrpInstancePreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 14),
    _VrrpInstancePreemptDelay_Type()
)
vrrpInstancePreemptDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstancePreemptDelay.setStatus("current")
if mibBuilder.loadTexts:
    vrrpInstancePreemptDelay.setUnits("seconds")


class _VrrpInstanceAuthType_Type(Integer32):
    """Custom type vrrpInstanceAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ah", 2),
          ("none", 0),
          ("password", 1))
    )


_VrrpInstanceAuthType_Type.__name__ = "Integer32"
_VrrpInstanceAuthType_Object = MibTableColumn
vrrpInstanceAuthType = _VrrpInstanceAuthType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 15),
    _VrrpInstanceAuthType_Type()
)
vrrpInstanceAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceAuthType.setStatus("current")


class _VrrpInstanceLvsSyncDaemon_Type(Integer32):
    """Custom type vrrpInstanceLvsSyncDaemon based on Integer32"""
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


_VrrpInstanceLvsSyncDaemon_Type.__name__ = "Integer32"
_VrrpInstanceLvsSyncDaemon_Object = MibTableColumn
vrrpInstanceLvsSyncDaemon = _VrrpInstanceLvsSyncDaemon_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 16),
    _VrrpInstanceLvsSyncDaemon_Type()
)
vrrpInstanceLvsSyncDaemon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceLvsSyncDaemon.setStatus("current")
_VrrpInstanceLvsSyncInterface_Type = DisplayString
_VrrpInstanceLvsSyncInterface_Object = MibTableColumn
vrrpInstanceLvsSyncInterface = _VrrpInstanceLvsSyncInterface_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 17),
    _VrrpInstanceLvsSyncInterface_Type()
)
vrrpInstanceLvsSyncInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceLvsSyncInterface.setStatus("current")
_VrrpInstanceSyncGroup_Type = DisplayString
_VrrpInstanceSyncGroup_Object = MibTableColumn
vrrpInstanceSyncGroup = _VrrpInstanceSyncGroup_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 18),
    _VrrpInstanceSyncGroup_Type()
)
vrrpInstanceSyncGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceSyncGroup.setStatus("current")
_VrrpInstanceGarpDelay_Type = Unsigned32
_VrrpInstanceGarpDelay_Object = MibTableColumn
vrrpInstanceGarpDelay = _VrrpInstanceGarpDelay_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 19),
    _VrrpInstanceGarpDelay_Type()
)
vrrpInstanceGarpDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceGarpDelay.setStatus("current")
if mibBuilder.loadTexts:
    vrrpInstanceGarpDelay.setUnits("seconds")


class _VrrpInstanceSmtpAlert_Type(Integer32):
    """Custom type vrrpInstanceSmtpAlert based on Integer32"""
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


_VrrpInstanceSmtpAlert_Type.__name__ = "Integer32"
_VrrpInstanceSmtpAlert_Object = MibTableColumn
vrrpInstanceSmtpAlert = _VrrpInstanceSmtpAlert_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 20),
    _VrrpInstanceSmtpAlert_Type()
)
vrrpInstanceSmtpAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceSmtpAlert.setStatus("current")


class _VrrpInstanceNotifyExec_Type(Integer32):
    """Custom type vrrpInstanceNotifyExec based on Integer32"""
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


_VrrpInstanceNotifyExec_Type.__name__ = "Integer32"
_VrrpInstanceNotifyExec_Object = MibTableColumn
vrrpInstanceNotifyExec = _VrrpInstanceNotifyExec_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 21),
    _VrrpInstanceNotifyExec_Type()
)
vrrpInstanceNotifyExec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceNotifyExec.setStatus("current")
_VrrpInstanceScriptMaster_Type = DisplayString
_VrrpInstanceScriptMaster_Object = MibTableColumn
vrrpInstanceScriptMaster = _VrrpInstanceScriptMaster_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 22),
    _VrrpInstanceScriptMaster_Type()
)
vrrpInstanceScriptMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceScriptMaster.setStatus("current")
_VrrpInstanceScriptBackup_Type = DisplayString
_VrrpInstanceScriptBackup_Object = MibTableColumn
vrrpInstanceScriptBackup = _VrrpInstanceScriptBackup_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 23),
    _VrrpInstanceScriptBackup_Type()
)
vrrpInstanceScriptBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceScriptBackup.setStatus("current")
_VrrpInstanceScriptFault_Type = DisplayString
_VrrpInstanceScriptFault_Object = MibTableColumn
vrrpInstanceScriptFault = _VrrpInstanceScriptFault_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 24),
    _VrrpInstanceScriptFault_Type()
)
vrrpInstanceScriptFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceScriptFault.setStatus("current")
_VrrpInstanceScriptStop_Type = DisplayString
_VrrpInstanceScriptStop_Object = MibTableColumn
vrrpInstanceScriptStop = _VrrpInstanceScriptStop_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 25),
    _VrrpInstanceScriptStop_Type()
)
vrrpInstanceScriptStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceScriptStop.setStatus("current")
_VrrpInstanceScript_Type = DisplayString
_VrrpInstanceScript_Object = MibTableColumn
vrrpInstanceScript = _VrrpInstanceScript_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 3, 1, 26),
    _VrrpInstanceScript_Type()
)
vrrpInstanceScript.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpInstanceScript.setStatus("current")
_VrrpTrackedInterfaceTable_Object = MibTable
vrrpTrackedInterfaceTable = _VrrpTrackedInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 4)
)
if mibBuilder.loadTexts:
    vrrpTrackedInterfaceTable.setStatus("current")
_VrrpTrackedInterfaceEntry_Object = MibTableRow
vrrpTrackedInterfaceEntry = _VrrpTrackedInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 4, 1)
)
vrrpTrackedInterfaceEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpInstanceIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vrrpTrackedInterfaceEntry.setStatus("current")
_VrrpTrackedInterfaceName_Type = DisplayString
_VrrpTrackedInterfaceName_Object = MibTableColumn
vrrpTrackedInterfaceName = _VrrpTrackedInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 4, 1, 1),
    _VrrpTrackedInterfaceName_Type()
)
vrrpTrackedInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpTrackedInterfaceName.setStatus("current")
_VrrpTrackedInterfaceWeight_Type = Integer32
_VrrpTrackedInterfaceWeight_Object = MibTableColumn
vrrpTrackedInterfaceWeight = _VrrpTrackedInterfaceWeight_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 4, 1, 2),
    _VrrpTrackedInterfaceWeight_Type()
)
vrrpTrackedInterfaceWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpTrackedInterfaceWeight.setStatus("current")
_VrrpTrackedScriptTable_Object = MibTable
vrrpTrackedScriptTable = _VrrpTrackedScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 5)
)
if mibBuilder.loadTexts:
    vrrpTrackedScriptTable.setStatus("current")
_VrrpTrackedScriptEntry_Object = MibTableRow
vrrpTrackedScriptEntry = _VrrpTrackedScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 5, 1)
)
vrrpTrackedScriptEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpInstanceIndex"),
    (0, "KEEPALIVED-MIB", "vrrpTrackedScriptIndex"),
)
if mibBuilder.loadTexts:
    vrrpTrackedScriptEntry.setStatus("current")


class _VrrpTrackedScriptIndex_Type(Integer32):
    """Custom type vrrpTrackedScriptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrrpTrackedScriptIndex_Type.__name__ = "Integer32"
_VrrpTrackedScriptIndex_Object = MibTableColumn
vrrpTrackedScriptIndex = _VrrpTrackedScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 5, 1, 1),
    _VrrpTrackedScriptIndex_Type()
)
vrrpTrackedScriptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpTrackedScriptIndex.setStatus("current")
_VrrpTrackedScriptName_Type = DisplayString
_VrrpTrackedScriptName_Object = MibTableColumn
vrrpTrackedScriptName = _VrrpTrackedScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 5, 1, 2),
    _VrrpTrackedScriptName_Type()
)
vrrpTrackedScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpTrackedScriptName.setStatus("current")
_VrrpTrackedScriptWeight_Type = Integer32
_VrrpTrackedScriptWeight_Object = MibTableColumn
vrrpTrackedScriptWeight = _VrrpTrackedScriptWeight_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 5, 1, 3),
    _VrrpTrackedScriptWeight_Type()
)
vrrpTrackedScriptWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpTrackedScriptWeight.setStatus("current")
_VrrpAddressTable_Object = MibTable
vrrpAddressTable = _VrrpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6)
)
if mibBuilder.loadTexts:
    vrrpAddressTable.setStatus("current")
_VrrpAddressEntry_Object = MibTableRow
vrrpAddressEntry = _VrrpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1)
)
vrrpAddressEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpInstanceIndex"),
    (0, "KEEPALIVED-MIB", "vrrpAddressIndex"),
)
if mibBuilder.loadTexts:
    vrrpAddressEntry.setStatus("current")


class _VrrpAddressIndex_Type(Integer32):
    """Custom type vrrpAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrrpAddressIndex_Type.__name__ = "Integer32"
_VrrpAddressIndex_Object = MibTableColumn
vrrpAddressIndex = _VrrpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 1),
    _VrrpAddressIndex_Type()
)
vrrpAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpAddressIndex.setStatus("current")
_VrrpAddressType_Type = InetAddressType
_VrrpAddressType_Object = MibTableColumn
vrrpAddressType = _VrrpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 2),
    _VrrpAddressType_Type()
)
vrrpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressType.setStatus("current")
_VrrpAddressValue_Type = InetAddress
_VrrpAddressValue_Object = MibTableColumn
vrrpAddressValue = _VrrpAddressValue_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 3),
    _VrrpAddressValue_Type()
)
vrrpAddressValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressValue.setStatus("current")
_VrrpAddressBroadcast_Type = InetAddress
_VrrpAddressBroadcast_Object = MibTableColumn
vrrpAddressBroadcast = _VrrpAddressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 4),
    _VrrpAddressBroadcast_Type()
)
vrrpAddressBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressBroadcast.setStatus("current")
_VrrpAddressMask_Type = InetAddressPrefixLength
_VrrpAddressMask_Object = MibTableColumn
vrrpAddressMask = _VrrpAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 5),
    _VrrpAddressMask_Type()
)
vrrpAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressMask.setStatus("current")
_VrrpAddressScope_Type = InetScopeType
_VrrpAddressScope_Object = MibTableColumn
vrrpAddressScope = _VrrpAddressScope_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 6),
    _VrrpAddressScope_Type()
)
vrrpAddressScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressScope.setStatus("current")
_VrrpAddressIfIndex_Type = InterfaceIndex
_VrrpAddressIfIndex_Object = MibTableColumn
vrrpAddressIfIndex = _VrrpAddressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 7),
    _VrrpAddressIfIndex_Type()
)
vrrpAddressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressIfIndex.setStatus("current")
_VrrpAddressIfName_Type = DisplayString
_VrrpAddressIfName_Object = MibTableColumn
vrrpAddressIfName = _VrrpAddressIfName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 8),
    _VrrpAddressIfName_Type()
)
vrrpAddressIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressIfName.setStatus("current")
_VrrpAddressIfAlias_Type = DisplayString
_VrrpAddressIfAlias_Object = MibTableColumn
vrrpAddressIfAlias = _VrrpAddressIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 9),
    _VrrpAddressIfAlias_Type()
)
vrrpAddressIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressIfAlias.setStatus("current")


class _VrrpAddressStatus_Type(Integer32):
    """Custom type vrrpAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_VrrpAddressStatus_Type.__name__ = "Integer32"
_VrrpAddressStatus_Object = MibTableColumn
vrrpAddressStatus = _VrrpAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 10),
    _VrrpAddressStatus_Type()
)
vrrpAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressStatus.setStatus("current")


class _VrrpAddressAdvertising_Type(Integer32):
    """Custom type vrrpAddressAdvertising based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertised", 1),
          ("notAdvertised", 2))
    )


_VrrpAddressAdvertising_Type.__name__ = "Integer32"
_VrrpAddressAdvertising_Object = MibTableColumn
vrrpAddressAdvertising = _VrrpAddressAdvertising_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 6, 1, 11),
    _VrrpAddressAdvertising_Type()
)
vrrpAddressAdvertising.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpAddressAdvertising.setStatus("current")
_VrrpRouteTable_Object = MibTable
vrrpRouteTable = _VrrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7)
)
if mibBuilder.loadTexts:
    vrrpRouteTable.setStatus("current")
_VrrpRouteEntry_Object = MibTableRow
vrrpRouteEntry = _VrrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1)
)
vrrpRouteEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpInstanceIndex"),
    (0, "KEEPALIVED-MIB", "vrrpRouteIndex"),
)
if mibBuilder.loadTexts:
    vrrpRouteEntry.setStatus("current")


class _VrrpRouteIndex_Type(Integer32):
    """Custom type vrrpRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrrpRouteIndex_Type.__name__ = "Integer32"
_VrrpRouteIndex_Object = MibTableColumn
vrrpRouteIndex = _VrrpRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 1),
    _VrrpRouteIndex_Type()
)
vrrpRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpRouteIndex.setStatus("current")
_VrrpRouteAddressType_Type = InetAddressType
_VrrpRouteAddressType_Object = MibTableColumn
vrrpRouteAddressType = _VrrpRouteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 2),
    _VrrpRouteAddressType_Type()
)
vrrpRouteAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteAddressType.setStatus("current")
_VrrpRouteDestination_Type = InetAddress
_VrrpRouteDestination_Object = MibTableColumn
vrrpRouteDestination = _VrrpRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 3),
    _VrrpRouteDestination_Type()
)
vrrpRouteDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteDestination.setStatus("current")
_VrrpRouteDestinationMask_Type = InetAddressPrefixLength
_VrrpRouteDestinationMask_Object = MibTableColumn
vrrpRouteDestinationMask = _VrrpRouteDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 4),
    _VrrpRouteDestinationMask_Type()
)
vrrpRouteDestinationMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteDestinationMask.setStatus("current")
_VrrpRouteGateway_Type = InetAddress
_VrrpRouteGateway_Object = MibTableColumn
vrrpRouteGateway = _VrrpRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 5),
    _VrrpRouteGateway_Type()
)
vrrpRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteGateway.setStatus("current")
_VrrpRouteSecondaryGateway_Type = InetAddress
_VrrpRouteSecondaryGateway_Object = MibTableColumn
vrrpRouteSecondaryGateway = _VrrpRouteSecondaryGateway_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 6),
    _VrrpRouteSecondaryGateway_Type()
)
vrrpRouteSecondaryGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteSecondaryGateway.setStatus("current")
_VrrpRouteSource_Type = InetAddress
_VrrpRouteSource_Object = MibTableColumn
vrrpRouteSource = _VrrpRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 7),
    _VrrpRouteSource_Type()
)
vrrpRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteSource.setStatus("current")
_VrrpRouteMetric_Type = Unsigned32
_VrrpRouteMetric_Object = MibTableColumn
vrrpRouteMetric = _VrrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 8),
    _VrrpRouteMetric_Type()
)
vrrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteMetric.setStatus("current")
_VrrpRouteScope_Type = InetScopeType
_VrrpRouteScope_Object = MibTableColumn
vrrpRouteScope = _VrrpRouteScope_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 9),
    _VrrpRouteScope_Type()
)
vrrpRouteScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteScope.setStatus("current")


class _VrrpRouteType_Type(Integer32):
    """Custom type vrrpRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blackhole", 3),
          ("ecmp", 2),
          ("normal", 1))
    )


_VrrpRouteType_Type.__name__ = "Integer32"
_VrrpRouteType_Object = MibTableColumn
vrrpRouteType = _VrrpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 10),
    _VrrpRouteType_Type()
)
vrrpRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteType.setStatus("current")
_VrrpRouteIfIndex_Type = InterfaceIndex
_VrrpRouteIfIndex_Object = MibTableColumn
vrrpRouteIfIndex = _VrrpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 11),
    _VrrpRouteIfIndex_Type()
)
vrrpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteIfIndex.setStatus("current")
_VrrpRouteIfName_Type = DisplayString
_VrrpRouteIfName_Object = MibTableColumn
vrrpRouteIfName = _VrrpRouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 12),
    _VrrpRouteIfName_Type()
)
vrrpRouteIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteIfName.setStatus("current")
_VrrpRouteRoutingTable_Type = Unsigned32
_VrrpRouteRoutingTable_Object = MibTableColumn
vrrpRouteRoutingTable = _VrrpRouteRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 13),
    _VrrpRouteRoutingTable_Type()
)
vrrpRouteRoutingTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteRoutingTable.setStatus("current")


class _VrrpRouteStatus_Type(Integer32):
    """Custom type vrrpRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("unset", 2))
    )


_VrrpRouteStatus_Type.__name__ = "Integer32"
_VrrpRouteStatus_Object = MibTableColumn
vrrpRouteStatus = _VrrpRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 7, 1, 14),
    _VrrpRouteStatus_Type()
)
vrrpRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpRouteStatus.setStatus("current")
_VrrpScriptTable_Object = MibTable
vrrpScriptTable = _VrrpScriptTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8)
)
if mibBuilder.loadTexts:
    vrrpScriptTable.setStatus("current")
_VrrpScriptEntry_Object = MibTableRow
vrrpScriptEntry = _VrrpScriptEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1)
)
vrrpScriptEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "vrrpScriptIndex"),
)
if mibBuilder.loadTexts:
    vrrpScriptEntry.setStatus("current")


class _VrrpScriptIndex_Type(Integer32):
    """Custom type vrrpScriptIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VrrpScriptIndex_Type.__name__ = "Integer32"
_VrrpScriptIndex_Object = MibTableColumn
vrrpScriptIndex = _VrrpScriptIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 1),
    _VrrpScriptIndex_Type()
)
vrrpScriptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrrpScriptIndex.setStatus("current")
_VrrpScriptName_Type = DisplayString
_VrrpScriptName_Object = MibTableColumn
vrrpScriptName = _VrrpScriptName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 2),
    _VrrpScriptName_Type()
)
vrrpScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpScriptName.setStatus("current")
_VrrpScriptCommand_Type = DisplayString
_VrrpScriptCommand_Object = MibTableColumn
vrrpScriptCommand = _VrrpScriptCommand_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 3),
    _VrrpScriptCommand_Type()
)
vrrpScriptCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpScriptCommand.setStatus("current")
_VrrpScriptInterval_Type = Integer32
_VrrpScriptInterval_Object = MibTableColumn
vrrpScriptInterval = _VrrpScriptInterval_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 4),
    _VrrpScriptInterval_Type()
)
vrrpScriptInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpScriptInterval.setStatus("current")
if mibBuilder.loadTexts:
    vrrpScriptInterval.setUnits("seconds")
_VrrpScriptWeight_Type = Integer32
_VrrpScriptWeight_Object = MibTableColumn
vrrpScriptWeight = _VrrpScriptWeight_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 5),
    _VrrpScriptWeight_Type()
)
vrrpScriptWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpScriptWeight.setStatus("current")


class _VrrpScriptResult_Type(Integer32):
    """Custom type vrrpScriptResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("disabled", 0),
          ("good", 3),
          ("init", 1),
          ("initgood", 4))
    )


_VrrpScriptResult_Type.__name__ = "Integer32"
_VrrpScriptResult_Object = MibTableColumn
vrrpScriptResult = _VrrpScriptResult_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 6),
    _VrrpScriptResult_Type()
)
vrrpScriptResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpScriptResult.setStatus("current")
_VrrpScriptRise_Type = Unsigned32
_VrrpScriptRise_Object = MibTableColumn
vrrpScriptRise = _VrrpScriptRise_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 7),
    _VrrpScriptRise_Type()
)
vrrpScriptRise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpScriptRise.setStatus("current")
_VrrpScriptFall_Type = Unsigned32
_VrrpScriptFall_Object = MibTableColumn
vrrpScriptFall = _VrrpScriptFall_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 8, 1, 8),
    _VrrpScriptFall_Type()
)
vrrpScriptFall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpScriptFall.setStatus("current")
_VrrpTrap_ObjectIdentity = ObjectIdentity
vrrpTrap = _VrrpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 9)
)
_VrrpTraps_ObjectIdentity = ObjectIdentity
vrrpTraps = _VrrpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 9, 0)
)
_VrrpTrapControl_ObjectIdentity = ObjectIdentity
vrrpTrapControl = _VrrpTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 9, 1)
)
_Check_ObjectIdentity = ObjectIdentity
check = _Check_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3)
)
_VirtualServerGroupTable_Object = MibTable
virtualServerGroupTable = _VirtualServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 1)
)
if mibBuilder.loadTexts:
    virtualServerGroupTable.setStatus("current")
_VirtualServerGroupEntry_Object = MibTableRow
virtualServerGroupEntry = _VirtualServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 1, 1)
)
virtualServerGroupEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "virtualServerGroupIndex"),
)
if mibBuilder.loadTexts:
    virtualServerGroupEntry.setStatus("current")


class _VirtualServerGroupIndex_Type(Integer32):
    """Custom type virtualServerGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VirtualServerGroupIndex_Type.__name__ = "Integer32"
_VirtualServerGroupIndex_Object = MibTableColumn
virtualServerGroupIndex = _VirtualServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 1, 1, 1),
    _VirtualServerGroupIndex_Type()
)
virtualServerGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualServerGroupIndex.setStatus("current")
_VirtualServerGroupName_Type = DisplayString
_VirtualServerGroupName_Object = MibTableColumn
virtualServerGroupName = _VirtualServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 1, 1, 2),
    _VirtualServerGroupName_Type()
)
virtualServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupName.setStatus("current")
_VirtualServerGroupMemberTable_Object = MibTable
virtualServerGroupMemberTable = _VirtualServerGroupMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2)
)
if mibBuilder.loadTexts:
    virtualServerGroupMemberTable.setStatus("current")
_VirtualServerGroupMemberEntry_Object = MibTableRow
virtualServerGroupMemberEntry = _VirtualServerGroupMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1)
)
virtualServerGroupMemberEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "virtualServerGroupIndex"),
    (0, "KEEPALIVED-MIB", "virtualServerGroupMemberIndex"),
)
if mibBuilder.loadTexts:
    virtualServerGroupMemberEntry.setStatus("current")


class _VirtualServerGroupMemberIndex_Type(Integer32):
    """Custom type virtualServerGroupMemberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VirtualServerGroupMemberIndex_Type.__name__ = "Integer32"
_VirtualServerGroupMemberIndex_Object = MibTableColumn
virtualServerGroupMemberIndex = _VirtualServerGroupMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 1),
    _VirtualServerGroupMemberIndex_Type()
)
virtualServerGroupMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualServerGroupMemberIndex.setStatus("current")


class _VirtualServerGroupMemberType_Type(Integer32):
    """Custom type virtualServerGroupMemberType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fwmark", 1),
          ("ip", 2),
          ("iprange", 3))
    )


_VirtualServerGroupMemberType_Type.__name__ = "Integer32"
_VirtualServerGroupMemberType_Object = MibTableColumn
virtualServerGroupMemberType = _VirtualServerGroupMemberType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 2),
    _VirtualServerGroupMemberType_Type()
)
virtualServerGroupMemberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupMemberType.setStatus("current")
_VirtualServerGroupMemberFwMark_Type = Unsigned32
_VirtualServerGroupMemberFwMark_Object = MibTableColumn
virtualServerGroupMemberFwMark = _VirtualServerGroupMemberFwMark_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 3),
    _VirtualServerGroupMemberFwMark_Type()
)
virtualServerGroupMemberFwMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupMemberFwMark.setStatus("current")
_VirtualServerGroupMemberAddrType_Type = InetAddressType
_VirtualServerGroupMemberAddrType_Object = MibTableColumn
virtualServerGroupMemberAddrType = _VirtualServerGroupMemberAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 4),
    _VirtualServerGroupMemberAddrType_Type()
)
virtualServerGroupMemberAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupMemberAddrType.setStatus("current")
_VirtualServerGroupMemberAddress_Type = InetAddress
_VirtualServerGroupMemberAddress_Object = MibTableColumn
virtualServerGroupMemberAddress = _VirtualServerGroupMemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 5),
    _VirtualServerGroupMemberAddress_Type()
)
virtualServerGroupMemberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupMemberAddress.setStatus("current")
_VirtualServerGroupMemberAddr1_Type = InetAddress
_VirtualServerGroupMemberAddr1_Object = MibTableColumn
virtualServerGroupMemberAddr1 = _VirtualServerGroupMemberAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 6),
    _VirtualServerGroupMemberAddr1_Type()
)
virtualServerGroupMemberAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupMemberAddr1.setStatus("current")
_VirtualServerGroupMemberAddr2_Type = InetAddress
_VirtualServerGroupMemberAddr2_Object = MibTableColumn
virtualServerGroupMemberAddr2 = _VirtualServerGroupMemberAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 7),
    _VirtualServerGroupMemberAddr2_Type()
)
virtualServerGroupMemberAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupMemberAddr2.setStatus("current")
_VirtualServerGroupMemberPort_Type = InetPortNumber
_VirtualServerGroupMemberPort_Object = MibTableColumn
virtualServerGroupMemberPort = _VirtualServerGroupMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 2, 1, 8),
    _VirtualServerGroupMemberPort_Type()
)
virtualServerGroupMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerGroupMemberPort.setStatus("current")
_VirtualServerTable_Object = MibTable
virtualServerTable = _VirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3)
)
if mibBuilder.loadTexts:
    virtualServerTable.setStatus("current")
_VirtualServerEntry_Object = MibTableRow
virtualServerEntry = _VirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1)
)
virtualServerEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "virtualServerIndex"),
)
if mibBuilder.loadTexts:
    virtualServerEntry.setStatus("current")


class _VirtualServerIndex_Type(Integer32):
    """Custom type virtualServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VirtualServerIndex_Type.__name__ = "Integer32"
_VirtualServerIndex_Object = MibTableColumn
virtualServerIndex = _VirtualServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 1),
    _VirtualServerIndex_Type()
)
virtualServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    virtualServerIndex.setStatus("current")


class _VirtualServerType_Type(Integer32):
    """Custom type virtualServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fwmark", 1),
          ("group", 3),
          ("ip", 2))
    )


_VirtualServerType_Type.__name__ = "Integer32"
_VirtualServerType_Object = MibTableColumn
virtualServerType = _VirtualServerType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 2),
    _VirtualServerType_Type()
)
virtualServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerType.setStatus("current")
_VirtualServerNameOfGroup_Type = DisplayString
_VirtualServerNameOfGroup_Object = MibTableColumn
virtualServerNameOfGroup = _VirtualServerNameOfGroup_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 3),
    _VirtualServerNameOfGroup_Type()
)
virtualServerNameOfGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerNameOfGroup.setStatus("current")
_VirtualServerFwMark_Type = Unsigned32
_VirtualServerFwMark_Object = MibTableColumn
virtualServerFwMark = _VirtualServerFwMark_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 4),
    _VirtualServerFwMark_Type()
)
virtualServerFwMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerFwMark.setStatus("current")
_VirtualServerAddrType_Type = InetAddressType
_VirtualServerAddrType_Object = MibTableColumn
virtualServerAddrType = _VirtualServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 5),
    _VirtualServerAddrType_Type()
)
virtualServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAddrType.setStatus("current")
_VirtualServerAddress_Type = InetAddress
_VirtualServerAddress_Object = MibTableColumn
virtualServerAddress = _VirtualServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 6),
    _VirtualServerAddress_Type()
)
virtualServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAddress.setStatus("current")
_VirtualServerPort_Type = InetPortNumber
_VirtualServerPort_Object = MibTableColumn
virtualServerPort = _VirtualServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 7),
    _VirtualServerPort_Type()
)
virtualServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPort.setStatus("current")


class _VirtualServerProtocol_Type(Integer32):
    """Custom type virtualServerProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_VirtualServerProtocol_Type.__name__ = "Integer32"
_VirtualServerProtocol_Object = MibTableColumn
virtualServerProtocol = _VirtualServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 8),
    _VirtualServerProtocol_Type()
)
virtualServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerProtocol.setStatus("current")


class _VirtualServerLoadBalancingAlgo_Type(Integer32):
    """Custom type virtualServerLoadBalancingAlgo based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("dh", 7),
          ("lblc", 5),
          ("lblcr", 6),
          ("lc", 3),
          ("nq", 10),
          ("rr", 1),
          ("sed", 9),
          ("sh", 8),
          ("unknown", 99),
          ("wlc", 4),
          ("wrr", 2))
    )


_VirtualServerLoadBalancingAlgo_Type.__name__ = "Integer32"
_VirtualServerLoadBalancingAlgo_Object = MibTableColumn
virtualServerLoadBalancingAlgo = _VirtualServerLoadBalancingAlgo_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 9),
    _VirtualServerLoadBalancingAlgo_Type()
)
virtualServerLoadBalancingAlgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerLoadBalancingAlgo.setStatus("current")


class _VirtualServerLoadBalancingKind_Type(Integer32):
    """Custom type virtualServerLoadBalancingKind based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dr", 2),
          ("nat", 1),
          ("tun", 3))
    )


_VirtualServerLoadBalancingKind_Type.__name__ = "Integer32"
_VirtualServerLoadBalancingKind_Object = MibTableColumn
virtualServerLoadBalancingKind = _VirtualServerLoadBalancingKind_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 10),
    _VirtualServerLoadBalancingKind_Type()
)
virtualServerLoadBalancingKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerLoadBalancingKind.setStatus("current")


class _VirtualServerStatus_Type(Integer32):
    """Custom type virtualServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_VirtualServerStatus_Type.__name__ = "Integer32"
_VirtualServerStatus_Object = MibTableColumn
virtualServerStatus = _VirtualServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 11),
    _VirtualServerStatus_Type()
)
virtualServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatus.setStatus("current")
_VirtualServerVirtualHost_Type = DisplayString
_VirtualServerVirtualHost_Object = MibTableColumn
virtualServerVirtualHost = _VirtualServerVirtualHost_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 12),
    _VirtualServerVirtualHost_Type()
)
virtualServerVirtualHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerVirtualHost.setStatus("current")


class _VirtualServerPersist_Type(Integer32):
    """Custom type virtualServerPersist based on Integer32"""
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


_VirtualServerPersist_Type.__name__ = "Integer32"
_VirtualServerPersist_Object = MibTableColumn
virtualServerPersist = _VirtualServerPersist_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 13),
    _VirtualServerPersist_Type()
)
virtualServerPersist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPersist.setStatus("current")
_VirtualServerPersistTimeout_Type = Unsigned32
_VirtualServerPersistTimeout_Object = MibTableColumn
virtualServerPersistTimeout = _VirtualServerPersistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 14),
    _VirtualServerPersistTimeout_Type()
)
virtualServerPersistTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPersistTimeout.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerPersistTimeout.setUnits("seconds")
_VirtualServerPersistGranularity_Type = InetAddress
_VirtualServerPersistGranularity_Object = MibTableColumn
virtualServerPersistGranularity = _VirtualServerPersistGranularity_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 15),
    _VirtualServerPersistGranularity_Type()
)
virtualServerPersistGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPersistGranularity.setStatus("current")
_VirtualServerDelayLoop_Type = Unsigned32
_VirtualServerDelayLoop_Object = MibTableColumn
virtualServerDelayLoop = _VirtualServerDelayLoop_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 16),
    _VirtualServerDelayLoop_Type()
)
virtualServerDelayLoop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerDelayLoop.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerDelayLoop.setUnits("seconds")
_VirtualServerHaSuspend_Type = TruthValue
_VirtualServerHaSuspend_Object = MibTableColumn
virtualServerHaSuspend = _VirtualServerHaSuspend_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 17),
    _VirtualServerHaSuspend_Type()
)
virtualServerHaSuspend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerHaSuspend.setStatus("current")


class _VirtualServerAlpha_Type(Integer32):
    """Custom type virtualServerAlpha based on Integer32"""
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


_VirtualServerAlpha_Type.__name__ = "Integer32"
_VirtualServerAlpha_Object = MibTableColumn
virtualServerAlpha = _VirtualServerAlpha_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 18),
    _VirtualServerAlpha_Type()
)
virtualServerAlpha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAlpha.setStatus("current")


class _VirtualServerOmega_Type(Integer32):
    """Custom type virtualServerOmega based on Integer32"""
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


_VirtualServerOmega_Type.__name__ = "Integer32"
_VirtualServerOmega_Object = MibTableColumn
virtualServerOmega = _VirtualServerOmega_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 19),
    _VirtualServerOmega_Type()
)
virtualServerOmega.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOmega.setStatus("current")
_VirtualServerRealServersTotal_Type = Unsigned32
_VirtualServerRealServersTotal_Object = MibTableColumn
virtualServerRealServersTotal = _VirtualServerRealServersTotal_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 20),
    _VirtualServerRealServersTotal_Type()
)
virtualServerRealServersTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRealServersTotal.setStatus("current")
_VirtualServerRealServersUp_Type = Unsigned32
_VirtualServerRealServersUp_Object = MibTableColumn
virtualServerRealServersUp = _VirtualServerRealServersUp_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 21),
    _VirtualServerRealServersUp_Type()
)
virtualServerRealServersUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRealServersUp.setStatus("current")
_VirtualServerQuorum_Type = Unsigned32
_VirtualServerQuorum_Object = MibTableColumn
virtualServerQuorum = _VirtualServerQuorum_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 22),
    _VirtualServerQuorum_Type()
)
virtualServerQuorum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerQuorum.setStatus("current")


class _VirtualServerQuorumStatus_Type(Integer32):
    """Custom type virtualServerQuorumStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("met", 1),
          ("notMet", 2))
    )


_VirtualServerQuorumStatus_Type.__name__ = "Integer32"
_VirtualServerQuorumStatus_Object = MibTableColumn
virtualServerQuorumStatus = _VirtualServerQuorumStatus_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 23),
    _VirtualServerQuorumStatus_Type()
)
virtualServerQuorumStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerQuorumStatus.setStatus("current")
_VirtualServerQuorumUp_Type = DisplayString
_VirtualServerQuorumUp_Object = MibTableColumn
virtualServerQuorumUp = _VirtualServerQuorumUp_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 24),
    _VirtualServerQuorumUp_Type()
)
virtualServerQuorumUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerQuorumUp.setStatus("current")
_VirtualServerQuorumDown_Type = DisplayString
_VirtualServerQuorumDown_Object = MibTableColumn
virtualServerQuorumDown = _VirtualServerQuorumDown_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 25),
    _VirtualServerQuorumDown_Type()
)
virtualServerQuorumDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerQuorumDown.setStatus("current")
_VirtualServerHysteresis_Type = Unsigned32
_VirtualServerHysteresis_Object = MibTableColumn
virtualServerHysteresis = _VirtualServerHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 26),
    _VirtualServerHysteresis_Type()
)
virtualServerHysteresis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerHysteresis.setStatus("current")
_VirtualServerStatsConns_Type = Gauge32
_VirtualServerStatsConns_Object = MibTableColumn
virtualServerStatsConns = _VirtualServerStatsConns_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 27),
    _VirtualServerStatsConns_Type()
)
virtualServerStatsConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatsConns.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerStatsConns.setUnits("connections")
_VirtualServerStatsInPkts_Type = Counter32
_VirtualServerStatsInPkts_Object = MibTableColumn
virtualServerStatsInPkts = _VirtualServerStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 28),
    _VirtualServerStatsInPkts_Type()
)
virtualServerStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatsInPkts.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerStatsInPkts.setUnits("packets")
_VirtualServerStatsOutPkts_Type = Counter32
_VirtualServerStatsOutPkts_Object = MibTableColumn
virtualServerStatsOutPkts = _VirtualServerStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 29),
    _VirtualServerStatsOutPkts_Type()
)
virtualServerStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatsOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerStatsOutPkts.setUnits("packets")
_VirtualServerStatsInBytes_Type = Counter64
_VirtualServerStatsInBytes_Object = MibTableColumn
virtualServerStatsInBytes = _VirtualServerStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 30),
    _VirtualServerStatsInBytes_Type()
)
virtualServerStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatsInBytes.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerStatsInBytes.setUnits("bytes")
_VirtualServerStatsOutBytes_Type = Counter64
_VirtualServerStatsOutBytes_Object = MibTableColumn
virtualServerStatsOutBytes = _VirtualServerStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 31),
    _VirtualServerStatsOutBytes_Type()
)
virtualServerStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatsOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerStatsOutBytes.setUnits("bytes")
_VirtualServerRateCps_Type = Gauge32
_VirtualServerRateCps_Object = MibTableColumn
virtualServerRateCps = _VirtualServerRateCps_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 32),
    _VirtualServerRateCps_Type()
)
virtualServerRateCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRateCps.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerRateCps.setUnits("connections/s")
_VirtualServerRateInPPS_Type = Gauge32
_VirtualServerRateInPPS_Object = MibTableColumn
virtualServerRateInPPS = _VirtualServerRateInPPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 33),
    _VirtualServerRateInPPS_Type()
)
virtualServerRateInPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRateInPPS.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerRateInPPS.setUnits("packets/s")
_VirtualServerRateOutPPS_Type = Gauge32
_VirtualServerRateOutPPS_Object = MibTableColumn
virtualServerRateOutPPS = _VirtualServerRateOutPPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 34),
    _VirtualServerRateOutPPS_Type()
)
virtualServerRateOutPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRateOutPPS.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerRateOutPPS.setUnits("packets/s")
_VirtualServerRateInBPS_Type = Gauge32
_VirtualServerRateInBPS_Object = MibTableColumn
virtualServerRateInBPS = _VirtualServerRateInBPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 35),
    _VirtualServerRateInBPS_Type()
)
virtualServerRateInBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRateInBPS.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerRateInBPS.setUnits("bytes/s")
_VirtualServerRateOutBPS_Type = Gauge32
_VirtualServerRateOutBPS_Object = MibTableColumn
virtualServerRateOutBPS = _VirtualServerRateOutBPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 3, 1, 36),
    _VirtualServerRateOutBPS_Type()
)
virtualServerRateOutBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRateOutBPS.setStatus("current")
if mibBuilder.loadTexts:
    virtualServerRateOutBPS.setUnits("bytes/s")
_RealServerTable_Object = MibTable
realServerTable = _RealServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4)
)
if mibBuilder.loadTexts:
    realServerTable.setStatus("current")
_RealServerEntry_Object = MibTableRow
realServerEntry = _RealServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1)
)
realServerEntry.setIndexNames(
    (0, "KEEPALIVED-MIB", "virtualServerIndex"),
    (0, "KEEPALIVED-MIB", "realServerIndex"),
)
if mibBuilder.loadTexts:
    realServerEntry.setStatus("current")


class _RealServerIndex_Type(Integer32):
    """Custom type realServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RealServerIndex_Type.__name__ = "Integer32"
_RealServerIndex_Object = MibTableColumn
realServerIndex = _RealServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 1),
    _RealServerIndex_Type()
)
realServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    realServerIndex.setStatus("current")


class _RealServerType_Type(Integer32):
    """Custom type realServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 1),
          ("sorry", 2))
    )


_RealServerType_Type.__name__ = "Integer32"
_RealServerType_Object = MibTableColumn
realServerType = _RealServerType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 2),
    _RealServerType_Type()
)
realServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerType.setStatus("current")
_RealServerAddrType_Type = InetAddressType
_RealServerAddrType_Object = MibTableColumn
realServerAddrType = _RealServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 3),
    _RealServerAddrType_Type()
)
realServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerAddrType.setStatus("current")
_RealServerAddress_Type = InetAddress
_RealServerAddress_Object = MibTableColumn
realServerAddress = _RealServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 4),
    _RealServerAddress_Type()
)
realServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerAddress.setStatus("current")
_RealServerPort_Type = InetPortNumber
_RealServerPort_Object = MibTableColumn
realServerPort = _RealServerPort_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 5),
    _RealServerPort_Type()
)
realServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerPort.setStatus("current")


class _RealServerStatus_Type(Integer32):
    """Custom type realServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_RealServerStatus_Type.__name__ = "Integer32"
_RealServerStatus_Object = MibTableColumn
realServerStatus = _RealServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 6),
    _RealServerStatus_Type()
)
realServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatus.setStatus("current")
_RealServerWeight_Type = Integer32
_RealServerWeight_Object = MibTableColumn
realServerWeight = _RealServerWeight_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 7),
    _RealServerWeight_Type()
)
realServerWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    realServerWeight.setStatus("current")
_RealServerUpperConnectionLimit_Type = Unsigned32
_RealServerUpperConnectionLimit_Object = MibTableColumn
realServerUpperConnectionLimit = _RealServerUpperConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 8),
    _RealServerUpperConnectionLimit_Type()
)
realServerUpperConnectionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerUpperConnectionLimit.setStatus("current")
_RealServerLowerConnectionLimit_Type = Unsigned32
_RealServerLowerConnectionLimit_Object = MibTableColumn
realServerLowerConnectionLimit = _RealServerLowerConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 9),
    _RealServerLowerConnectionLimit_Type()
)
realServerLowerConnectionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerLowerConnectionLimit.setStatus("current")


class _RealServerActionWhenDown_Type(Integer32):
    """Custom type realServerActionWhenDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 2),
          ("remove", 1))
    )


_RealServerActionWhenDown_Type.__name__ = "Integer32"
_RealServerActionWhenDown_Object = MibTableColumn
realServerActionWhenDown = _RealServerActionWhenDown_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 10),
    _RealServerActionWhenDown_Type()
)
realServerActionWhenDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerActionWhenDown.setStatus("current")
_RealServerNotifyUp_Type = DisplayString
_RealServerNotifyUp_Object = MibTableColumn
realServerNotifyUp = _RealServerNotifyUp_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 11),
    _RealServerNotifyUp_Type()
)
realServerNotifyUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerNotifyUp.setStatus("current")
_RealServerNotifyDown_Type = DisplayString
_RealServerNotifyDown_Object = MibTableColumn
realServerNotifyDown = _RealServerNotifyDown_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 12),
    _RealServerNotifyDown_Type()
)
realServerNotifyDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerNotifyDown.setStatus("current")
_RealServerFailedChecks_Type = Unsigned32
_RealServerFailedChecks_Object = MibTableColumn
realServerFailedChecks = _RealServerFailedChecks_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 13),
    _RealServerFailedChecks_Type()
)
realServerFailedChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerFailedChecks.setStatus("current")
_RealServerStatsConns_Type = Gauge32
_RealServerStatsConns_Object = MibTableColumn
realServerStatsConns = _RealServerStatsConns_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 14),
    _RealServerStatsConns_Type()
)
realServerStatsConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsConns.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsConns.setUnits("connections")
_RealServerStatsActiveConns_Type = Gauge32
_RealServerStatsActiveConns_Object = MibTableColumn
realServerStatsActiveConns = _RealServerStatsActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 15),
    _RealServerStatsActiveConns_Type()
)
realServerStatsActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsActiveConns.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsActiveConns.setUnits("connections")
_RealServerStatsInactiveConns_Type = Gauge32
_RealServerStatsInactiveConns_Object = MibTableColumn
realServerStatsInactiveConns = _RealServerStatsInactiveConns_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 16),
    _RealServerStatsInactiveConns_Type()
)
realServerStatsInactiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsInactiveConns.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsInactiveConns.setUnits("connections")
_RealServerStatsPersistentConns_Type = Gauge32
_RealServerStatsPersistentConns_Object = MibTableColumn
realServerStatsPersistentConns = _RealServerStatsPersistentConns_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 17),
    _RealServerStatsPersistentConns_Type()
)
realServerStatsPersistentConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsPersistentConns.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsPersistentConns.setUnits("connections")
_RealServerStatsInPkts_Type = Counter32
_RealServerStatsInPkts_Object = MibTableColumn
realServerStatsInPkts = _RealServerStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 18),
    _RealServerStatsInPkts_Type()
)
realServerStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsInPkts.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsInPkts.setUnits("packets")
_RealServerStatsOutPkts_Type = Counter32
_RealServerStatsOutPkts_Object = MibTableColumn
realServerStatsOutPkts = _RealServerStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 19),
    _RealServerStatsOutPkts_Type()
)
realServerStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsOutPkts.setUnits("packets")
_RealServerStatsInBytes_Type = Counter64
_RealServerStatsInBytes_Object = MibTableColumn
realServerStatsInBytes = _RealServerStatsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 20),
    _RealServerStatsInBytes_Type()
)
realServerStatsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsInBytes.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsInBytes.setUnits("bytes")
_RealServerStatsOutBytes_Type = Counter64
_RealServerStatsOutBytes_Object = MibTableColumn
realServerStatsOutBytes = _RealServerStatsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 21),
    _RealServerStatsOutBytes_Type()
)
realServerStatsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerStatsOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    realServerStatsOutBytes.setUnits("bytes")
_RealServerRateCps_Type = Gauge32
_RealServerRateCps_Object = MibTableColumn
realServerRateCps = _RealServerRateCps_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 22),
    _RealServerRateCps_Type()
)
realServerRateCps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerRateCps.setStatus("current")
if mibBuilder.loadTexts:
    realServerRateCps.setUnits("connections/s")
_RealServerRateInPPS_Type = Gauge32
_RealServerRateInPPS_Object = MibTableColumn
realServerRateInPPS = _RealServerRateInPPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 23),
    _RealServerRateInPPS_Type()
)
realServerRateInPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerRateInPPS.setStatus("current")
if mibBuilder.loadTexts:
    realServerRateInPPS.setUnits("packets/s")
_RealServerRateOutPPS_Type = Gauge32
_RealServerRateOutPPS_Object = MibTableColumn
realServerRateOutPPS = _RealServerRateOutPPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 24),
    _RealServerRateOutPPS_Type()
)
realServerRateOutPPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerRateOutPPS.setStatus("current")
if mibBuilder.loadTexts:
    realServerRateOutPPS.setUnits("packets/s")
_RealServerRateInBPS_Type = Gauge32
_RealServerRateInBPS_Object = MibTableColumn
realServerRateInBPS = _RealServerRateInBPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 25),
    _RealServerRateInBPS_Type()
)
realServerRateInBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerRateInBPS.setStatus("current")
if mibBuilder.loadTexts:
    realServerRateInBPS.setUnits("bytes/s")
_RealServerRateOutBPS_Type = Gauge32
_RealServerRateOutBPS_Object = MibTableColumn
realServerRateOutBPS = _RealServerRateOutBPS_Object(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 4, 1, 26),
    _RealServerRateOutBPS_Type()
)
realServerRateOutBPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    realServerRateOutBPS.setStatus("current")
if mibBuilder.loadTexts:
    realServerRateOutBPS.setUnits("bytes/s")
_CheckTrap_ObjectIdentity = ObjectIdentity
checkTrap = _CheckTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 5)
)
_CheckTraps_ObjectIdentity = ObjectIdentity
checkTraps = _CheckTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 5, 0)
)
_CheckTrapControl_ObjectIdentity = ObjectIdentity
checkTrapControl = _CheckTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 5, 1)
)
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4)
)
_Compliances_ObjectIdentity = ObjectIdentity
compliances = _Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 1)
)
_Groups_ObjectIdentity = ObjectIdentity
groups = _Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2)
)
_VrrpGroups_ObjectIdentity = ObjectIdentity
vrrpGroups = _VrrpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 2)
)
_CheckGroups_ObjectIdentity = ObjectIdentity
checkGroups = _CheckGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 3)
)

# Managed Objects groups

globalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 1)
)
globalGroup.setObjects(
      *(("KEEPALIVED-MIB", "version"),
        ("KEEPALIVED-MIB", "routerId"),
        ("KEEPALIVED-MIB", "smtpServerAddressType"),
        ("KEEPALIVED-MIB", "smtpServerAddress"),
        ("KEEPALIVED-MIB", "smtpServerTimeout"),
        ("KEEPALIVED-MIB", "emailFrom"),
        ("KEEPALIVED-MIB", "emailAddress"),
        ("KEEPALIVED-MIB", "trapEnable"),
        ("KEEPALIVED-MIB", "linkBeat"))
)
if mibBuilder.loadTexts:
    globalGroup.setStatus("current")

vrrpSyncGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 2, 1)
)
vrrpSyncGroup.setObjects(
      *(("KEEPALIVED-MIB", "vrrpSyncGroupName"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupState"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupSmtpAlert"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupNotifyExec"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupScriptMaster"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupScriptBackup"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupScriptFault"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupScript"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupMemberName"))
)
if mibBuilder.loadTexts:
    vrrpSyncGroup.setStatus("current")

vrrpInstanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 2, 2)
)
vrrpInstanceGroup.setObjects(
      *(("KEEPALIVED-MIB", "vrrpInstanceName"),
        ("KEEPALIVED-MIB", "vrrpInstanceVirtualRouterId"),
        ("KEEPALIVED-MIB", "vrrpInstanceState"),
        ("KEEPALIVED-MIB", "vrrpInstanceInitialState"),
        ("KEEPALIVED-MIB", "vrrpInstanceWantedState"),
        ("KEEPALIVED-MIB", "vrrpInstanceBasePriority"),
        ("KEEPALIVED-MIB", "vrrpInstanceEffectivePriority"),
        ("KEEPALIVED-MIB", "vrrpInstanceVipsStatus"),
        ("KEEPALIVED-MIB", "vrrpInstancePrimaryInterface"),
        ("KEEPALIVED-MIB", "vrrpInstanceTrackPrimaryIf"),
        ("KEEPALIVED-MIB", "vrrpInstanceAdvertisementsInt"),
        ("KEEPALIVED-MIB", "vrrpInstancePreempt"),
        ("KEEPALIVED-MIB", "vrrpInstancePreemptDelay"),
        ("KEEPALIVED-MIB", "vrrpInstanceAuthType"),
        ("KEEPALIVED-MIB", "vrrpInstanceLvsSyncDaemon"),
        ("KEEPALIVED-MIB", "vrrpInstanceLvsSyncInterface"),
        ("KEEPALIVED-MIB", "vrrpInstanceSyncGroup"),
        ("KEEPALIVED-MIB", "vrrpInstanceGarpDelay"),
        ("KEEPALIVED-MIB", "vrrpInstanceSmtpAlert"),
        ("KEEPALIVED-MIB", "vrrpInstanceNotifyExec"),
        ("KEEPALIVED-MIB", "vrrpInstanceScriptMaster"),
        ("KEEPALIVED-MIB", "vrrpInstanceScriptBackup"),
        ("KEEPALIVED-MIB", "vrrpInstanceScriptFault"),
        ("KEEPALIVED-MIB", "vrrpInstanceScriptStop"),
        ("KEEPALIVED-MIB", "vrrpInstanceScript"),
        ("KEEPALIVED-MIB", "vrrpTrackedInterfaceName"),
        ("KEEPALIVED-MIB", "vrrpTrackedInterfaceWeight"),
        ("KEEPALIVED-MIB", "vrrpTrackedScriptName"),
        ("KEEPALIVED-MIB", "vrrpTrackedScriptWeight"),
        ("KEEPALIVED-MIB", "vrrpAddressType"),
        ("KEEPALIVED-MIB", "vrrpAddressValue"),
        ("KEEPALIVED-MIB", "vrrpAddressBroadcast"),
        ("KEEPALIVED-MIB", "vrrpAddressMask"),
        ("KEEPALIVED-MIB", "vrrpAddressScope"),
        ("KEEPALIVED-MIB", "vrrpAddressIfIndex"),
        ("KEEPALIVED-MIB", "vrrpAddressIfName"),
        ("KEEPALIVED-MIB", "vrrpAddressIfAlias"),
        ("KEEPALIVED-MIB", "vrrpAddressStatus"),
        ("KEEPALIVED-MIB", "vrrpAddressAdvertising"),
        ("KEEPALIVED-MIB", "vrrpRouteAddressType"),
        ("KEEPALIVED-MIB", "vrrpRouteDestination"),
        ("KEEPALIVED-MIB", "vrrpRouteDestinationMask"),
        ("KEEPALIVED-MIB", "vrrpRouteGateway"),
        ("KEEPALIVED-MIB", "vrrpRouteSecondaryGateway"),
        ("KEEPALIVED-MIB", "vrrpRouteSource"),
        ("KEEPALIVED-MIB", "vrrpRouteMetric"),
        ("KEEPALIVED-MIB", "vrrpRouteScope"),
        ("KEEPALIVED-MIB", "vrrpRouteType"),
        ("KEEPALIVED-MIB", "vrrpRouteIfIndex"),
        ("KEEPALIVED-MIB", "vrrpRouteIfName"),
        ("KEEPALIVED-MIB", "vrrpRouteRoutingTable"),
        ("KEEPALIVED-MIB", "vrrpRouteStatus"))
)
if mibBuilder.loadTexts:
    vrrpInstanceGroup.setStatus("current")

vrrpScriptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 2, 3)
)
vrrpScriptGroup.setObjects(
      *(("KEEPALIVED-MIB", "vrrpScriptName"),
        ("KEEPALIVED-MIB", "vrrpScriptCommand"),
        ("KEEPALIVED-MIB", "vrrpScriptInterval"),
        ("KEEPALIVED-MIB", "vrrpScriptWeight"),
        ("KEEPALIVED-MIB", "vrrpScriptResult"),
        ("KEEPALIVED-MIB", "vrrpScriptRise"),
        ("KEEPALIVED-MIB", "vrrpScriptFall"))
)
if mibBuilder.loadTexts:
    vrrpScriptGroup.setStatus("current")

virtualServerGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 3, 1)
)
virtualServerGroupGroup.setObjects(
      *(("KEEPALIVED-MIB", "virtualServerGroupName"),
        ("KEEPALIVED-MIB", "virtualServerGroupMemberType"),
        ("KEEPALIVED-MIB", "virtualServerGroupMemberFwMark"),
        ("KEEPALIVED-MIB", "virtualServerGroupMemberAddrType"),
        ("KEEPALIVED-MIB", "virtualServerGroupMemberAddress"),
        ("KEEPALIVED-MIB", "virtualServerGroupMemberAddr1"),
        ("KEEPALIVED-MIB", "virtualServerGroupMemberAddr2"),
        ("KEEPALIVED-MIB", "virtualServerGroupMemberPort"))
)
if mibBuilder.loadTexts:
    virtualServerGroupGroup.setStatus("current")

virtualServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 3, 2)
)
virtualServerGroup.setObjects(
      *(("KEEPALIVED-MIB", "virtualServerType"),
        ("KEEPALIVED-MIB", "virtualServerNameOfGroup"),
        ("KEEPALIVED-MIB", "virtualServerFwMark"),
        ("KEEPALIVED-MIB", "virtualServerAddrType"),
        ("KEEPALIVED-MIB", "virtualServerAddress"),
        ("KEEPALIVED-MIB", "virtualServerPort"),
        ("KEEPALIVED-MIB", "virtualServerProtocol"),
        ("KEEPALIVED-MIB", "virtualServerLoadBalancingAlgo"),
        ("KEEPALIVED-MIB", "virtualServerLoadBalancingKind"),
        ("KEEPALIVED-MIB", "virtualServerStatus"),
        ("KEEPALIVED-MIB", "virtualServerVirtualHost"),
        ("KEEPALIVED-MIB", "virtualServerPersist"),
        ("KEEPALIVED-MIB", "virtualServerPersistTimeout"),
        ("KEEPALIVED-MIB", "virtualServerPersistGranularity"),
        ("KEEPALIVED-MIB", "virtualServerDelayLoop"),
        ("KEEPALIVED-MIB", "virtualServerHaSuspend"),
        ("KEEPALIVED-MIB", "virtualServerAlpha"),
        ("KEEPALIVED-MIB", "virtualServerOmega"),
        ("KEEPALIVED-MIB", "virtualServerRealServersTotal"),
        ("KEEPALIVED-MIB", "virtualServerRealServersUp"),
        ("KEEPALIVED-MIB", "virtualServerQuorum"),
        ("KEEPALIVED-MIB", "virtualServerQuorumStatus"),
        ("KEEPALIVED-MIB", "virtualServerQuorumUp"),
        ("KEEPALIVED-MIB", "virtualServerQuorumDown"),
        ("KEEPALIVED-MIB", "virtualServerHysteresis"),
        ("KEEPALIVED-MIB", "virtualServerStatsConns"),
        ("KEEPALIVED-MIB", "virtualServerStatsInPkts"),
        ("KEEPALIVED-MIB", "virtualServerStatsOutPkts"),
        ("KEEPALIVED-MIB", "virtualServerStatsInBytes"),
        ("KEEPALIVED-MIB", "virtualServerStatsOutBytes"),
        ("KEEPALIVED-MIB", "virtualServerRateCps"),
        ("KEEPALIVED-MIB", "virtualServerRateInPPS"),
        ("KEEPALIVED-MIB", "virtualServerRateOutPPS"),
        ("KEEPALIVED-MIB", "virtualServerRateInBPS"),
        ("KEEPALIVED-MIB", "virtualServerRateOutBPS"))
)
if mibBuilder.loadTexts:
    virtualServerGroup.setStatus("current")

realServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 3, 3)
)
realServerGroup.setObjects(
      *(("KEEPALIVED-MIB", "realServerType"),
        ("KEEPALIVED-MIB", "realServerAddrType"),
        ("KEEPALIVED-MIB", "realServerAddress"),
        ("KEEPALIVED-MIB", "realServerPort"),
        ("KEEPALIVED-MIB", "realServerStatus"),
        ("KEEPALIVED-MIB", "realServerWeight"),
        ("KEEPALIVED-MIB", "realServerUpperConnectionLimit"),
        ("KEEPALIVED-MIB", "realServerLowerConnectionLimit"),
        ("KEEPALIVED-MIB", "realServerActionWhenDown"),
        ("KEEPALIVED-MIB", "realServerNotifyUp"),
        ("KEEPALIVED-MIB", "realServerNotifyDown"),
        ("KEEPALIVED-MIB", "realServerFailedChecks"),
        ("KEEPALIVED-MIB", "realServerStatsConns"),
        ("KEEPALIVED-MIB", "realServerStatsActiveConns"),
        ("KEEPALIVED-MIB", "realServerStatsInactiveConns"),
        ("KEEPALIVED-MIB", "realServerStatsPersistentConns"),
        ("KEEPALIVED-MIB", "realServerStatsInPkts"),
        ("KEEPALIVED-MIB", "realServerStatsOutPkts"),
        ("KEEPALIVED-MIB", "realServerStatsInBytes"),
        ("KEEPALIVED-MIB", "realServerStatsOutBytes"),
        ("KEEPALIVED-MIB", "realServerRateCps"),
        ("KEEPALIVED-MIB", "realServerRateInPPS"),
        ("KEEPALIVED-MIB", "realServerRateOutPPS"),
        ("KEEPALIVED-MIB", "realServerRateInBPS"),
        ("KEEPALIVED-MIB", "realServerRateOutBPS"))
)
if mibBuilder.loadTexts:
    realServerGroup.setStatus("current")


# Notification objects

vrrpSyncGroupStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 9, 0, 1)
)
vrrpSyncGroupStateChange.setObjects(
      *(("KEEPALIVED-MIB", "vrrpSyncGroupName"),
        ("KEEPALIVED-MIB", "vrrpSyncGroupState"))
)
if mibBuilder.loadTexts:
    vrrpSyncGroupStateChange.setStatus(
        "current"
    )

vrrpInstanceStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 2, 9, 0, 2)
)
vrrpInstanceStateChange.setObjects(
      *(("KEEPALIVED-MIB", "vrrpInstanceName"),
        ("KEEPALIVED-MIB", "vrrpInstanceState"),
        ("KEEPALIVED-MIB", "vrrpInstanceInitialState"))
)
if mibBuilder.loadTexts:
    vrrpInstanceStateChange.setStatus(
        "current"
    )

realServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 5, 0, 1)
)
realServerStateChange.setObjects(
      *(("KEEPALIVED-MIB", "realServerAddrType"),
        ("KEEPALIVED-MIB", "realServerAddress"),
        ("KEEPALIVED-MIB", "realServerPort"),
        ("KEEPALIVED-MIB", "realServerStatus"),
        ("KEEPALIVED-MIB", "virtualServerType"),
        ("KEEPALIVED-MIB", "virtualServerProtocol"),
        ("KEEPALIVED-MIB", "virtualServerRealServersUp"),
        ("KEEPALIVED-MIB", "virtualServerRealServersTotal"))
)
if mibBuilder.loadTexts:
    realServerStateChange.setStatus(
        "current"
    )

virtualServerQuorumStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 3, 5, 0, 2)
)
virtualServerQuorumStateChange.setObjects(
      *(("KEEPALIVED-MIB", "virtualServerType"),
        ("KEEPALIVED-MIB", "virtualServerProtocol"),
        ("KEEPALIVED-MIB", "virtualServerQuorumStatus"),
        ("KEEPALIVED-MIB", "virtualServerQuorum"),
        ("KEEPALIVED-MIB", "virtualServerRealServersUp"),
        ("KEEPALIVED-MIB", "virtualServerRealServersTotal"))
)
if mibBuilder.loadTexts:
    virtualServerQuorumStateChange.setStatus(
        "current"
    )


# Notifications groups

vrrpTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 2, 4)
)
vrrpTrapsGroup.setObjects(
      *(("KEEPALIVED-MIB", "vrrpSyncGroupStateChange"),
        ("KEEPALIVED-MIB", "vrrpInstanceStateChange"))
)
if mibBuilder.loadTexts:
    vrrpTrapsGroup.setStatus(
        "current"
    )

checkTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 2, 3, 4)
)
checkTrapsGroup.setObjects(
      *(("KEEPALIVED-MIB", "realServerStateChange"),
        ("KEEPALIVED-MIB", "virtualServerQuorumStateChange"))
)
if mibBuilder.loadTexts:
    checkTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

globalCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    globalCompliances.setStatus(
        "current"
    )

vrrpCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    vrrpCompliances.setStatus(
        "current"
    )

checkCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9586, 100, 5, 4, 1, 3)
)
if mibBuilder.loadTexts:
    checkCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KEEPALIVED-MIB",
    **{"VrrpState": VrrpState,
       "debian": debian,
       "project": project,
       "keepalived": keepalived,
       "global": _pysmi_global,
       "version": version,
       "routerId": routerId,
       "mail": mail,
       "smtpServerAddressType": smtpServerAddressType,
       "smtpServerAddress": smtpServerAddress,
       "smtpServerTimeout": smtpServerTimeout,
       "emailFrom": emailFrom,
       "emailTable": emailTable,
       "emailEntry": emailEntry,
       "emailIndex": emailIndex,
       "emailAddress": emailAddress,
       "trapEnable": trapEnable,
       "linkBeat": linkBeat,
       "vrrp": vrrp,
       "vrrpSyncGroupTable": vrrpSyncGroupTable,
       "vrrpSyncGroupEntry": vrrpSyncGroupEntry,
       "vrrpSyncGroupIndex": vrrpSyncGroupIndex,
       "vrrpSyncGroupName": vrrpSyncGroupName,
       "vrrpSyncGroupState": vrrpSyncGroupState,
       "vrrpSyncGroupSmtpAlert": vrrpSyncGroupSmtpAlert,
       "vrrpSyncGroupNotifyExec": vrrpSyncGroupNotifyExec,
       "vrrpSyncGroupScriptMaster": vrrpSyncGroupScriptMaster,
       "vrrpSyncGroupScriptBackup": vrrpSyncGroupScriptBackup,
       "vrrpSyncGroupScriptFault": vrrpSyncGroupScriptFault,
       "vrrpSyncGroupScript": vrrpSyncGroupScript,
       "vrrpSyncGroupMemberTable": vrrpSyncGroupMemberTable,
       "vrrpSyncGroupMemberEntry": vrrpSyncGroupMemberEntry,
       "vrrpSyncGroupMemberInstanceIndex": vrrpSyncGroupMemberInstanceIndex,
       "vrrpSyncGroupMemberName": vrrpSyncGroupMemberName,
       "vrrpInstanceTable": vrrpInstanceTable,
       "vrrpInstanceEntry": vrrpInstanceEntry,
       "vrrpInstanceIndex": vrrpInstanceIndex,
       "vrrpInstanceName": vrrpInstanceName,
       "vrrpInstanceVirtualRouterId": vrrpInstanceVirtualRouterId,
       "vrrpInstanceState": vrrpInstanceState,
       "vrrpInstanceInitialState": vrrpInstanceInitialState,
       "vrrpInstanceWantedState": vrrpInstanceWantedState,
       "vrrpInstanceBasePriority": vrrpInstanceBasePriority,
       "vrrpInstanceEffectivePriority": vrrpInstanceEffectivePriority,
       "vrrpInstanceVipsStatus": vrrpInstanceVipsStatus,
       "vrrpInstancePrimaryInterface": vrrpInstancePrimaryInterface,
       "vrrpInstanceTrackPrimaryIf": vrrpInstanceTrackPrimaryIf,
       "vrrpInstanceAdvertisementsInt": vrrpInstanceAdvertisementsInt,
       "vrrpInstancePreempt": vrrpInstancePreempt,
       "vrrpInstancePreemptDelay": vrrpInstancePreemptDelay,
       "vrrpInstanceAuthType": vrrpInstanceAuthType,
       "vrrpInstanceLvsSyncDaemon": vrrpInstanceLvsSyncDaemon,
       "vrrpInstanceLvsSyncInterface": vrrpInstanceLvsSyncInterface,
       "vrrpInstanceSyncGroup": vrrpInstanceSyncGroup,
       "vrrpInstanceGarpDelay": vrrpInstanceGarpDelay,
       "vrrpInstanceSmtpAlert": vrrpInstanceSmtpAlert,
       "vrrpInstanceNotifyExec": vrrpInstanceNotifyExec,
       "vrrpInstanceScriptMaster": vrrpInstanceScriptMaster,
       "vrrpInstanceScriptBackup": vrrpInstanceScriptBackup,
       "vrrpInstanceScriptFault": vrrpInstanceScriptFault,
       "vrrpInstanceScriptStop": vrrpInstanceScriptStop,
       "vrrpInstanceScript": vrrpInstanceScript,
       "vrrpTrackedInterfaceTable": vrrpTrackedInterfaceTable,
       "vrrpTrackedInterfaceEntry": vrrpTrackedInterfaceEntry,
       "vrrpTrackedInterfaceName": vrrpTrackedInterfaceName,
       "vrrpTrackedInterfaceWeight": vrrpTrackedInterfaceWeight,
       "vrrpTrackedScriptTable": vrrpTrackedScriptTable,
       "vrrpTrackedScriptEntry": vrrpTrackedScriptEntry,
       "vrrpTrackedScriptIndex": vrrpTrackedScriptIndex,
       "vrrpTrackedScriptName": vrrpTrackedScriptName,
       "vrrpTrackedScriptWeight": vrrpTrackedScriptWeight,
       "vrrpAddressTable": vrrpAddressTable,
       "vrrpAddressEntry": vrrpAddressEntry,
       "vrrpAddressIndex": vrrpAddressIndex,
       "vrrpAddressType": vrrpAddressType,
       "vrrpAddressValue": vrrpAddressValue,
       "vrrpAddressBroadcast": vrrpAddressBroadcast,
       "vrrpAddressMask": vrrpAddressMask,
       "vrrpAddressScope": vrrpAddressScope,
       "vrrpAddressIfIndex": vrrpAddressIfIndex,
       "vrrpAddressIfName": vrrpAddressIfName,
       "vrrpAddressIfAlias": vrrpAddressIfAlias,
       "vrrpAddressStatus": vrrpAddressStatus,
       "vrrpAddressAdvertising": vrrpAddressAdvertising,
       "vrrpRouteTable": vrrpRouteTable,
       "vrrpRouteEntry": vrrpRouteEntry,
       "vrrpRouteIndex": vrrpRouteIndex,
       "vrrpRouteAddressType": vrrpRouteAddressType,
       "vrrpRouteDestination": vrrpRouteDestination,
       "vrrpRouteDestinationMask": vrrpRouteDestinationMask,
       "vrrpRouteGateway": vrrpRouteGateway,
       "vrrpRouteSecondaryGateway": vrrpRouteSecondaryGateway,
       "vrrpRouteSource": vrrpRouteSource,
       "vrrpRouteMetric": vrrpRouteMetric,
       "vrrpRouteScope": vrrpRouteScope,
       "vrrpRouteType": vrrpRouteType,
       "vrrpRouteIfIndex": vrrpRouteIfIndex,
       "vrrpRouteIfName": vrrpRouteIfName,
       "vrrpRouteRoutingTable": vrrpRouteRoutingTable,
       "vrrpRouteStatus": vrrpRouteStatus,
       "vrrpScriptTable": vrrpScriptTable,
       "vrrpScriptEntry": vrrpScriptEntry,
       "vrrpScriptIndex": vrrpScriptIndex,
       "vrrpScriptName": vrrpScriptName,
       "vrrpScriptCommand": vrrpScriptCommand,
       "vrrpScriptInterval": vrrpScriptInterval,
       "vrrpScriptWeight": vrrpScriptWeight,
       "vrrpScriptResult": vrrpScriptResult,
       "vrrpScriptRise": vrrpScriptRise,
       "vrrpScriptFall": vrrpScriptFall,
       "vrrpTrap": vrrpTrap,
       "vrrpTraps": vrrpTraps,
       "vrrpSyncGroupStateChange": vrrpSyncGroupStateChange,
       "vrrpInstanceStateChange": vrrpInstanceStateChange,
       "vrrpTrapControl": vrrpTrapControl,
       "check": check,
       "virtualServerGroupTable": virtualServerGroupTable,
       "virtualServerGroupEntry": virtualServerGroupEntry,
       "virtualServerGroupIndex": virtualServerGroupIndex,
       "virtualServerGroupName": virtualServerGroupName,
       "virtualServerGroupMemberTable": virtualServerGroupMemberTable,
       "virtualServerGroupMemberEntry": virtualServerGroupMemberEntry,
       "virtualServerGroupMemberIndex": virtualServerGroupMemberIndex,
       "virtualServerGroupMemberType": virtualServerGroupMemberType,
       "virtualServerGroupMemberFwMark": virtualServerGroupMemberFwMark,
       "virtualServerGroupMemberAddrType": virtualServerGroupMemberAddrType,
       "virtualServerGroupMemberAddress": virtualServerGroupMemberAddress,
       "virtualServerGroupMemberAddr1": virtualServerGroupMemberAddr1,
       "virtualServerGroupMemberAddr2": virtualServerGroupMemberAddr2,
       "virtualServerGroupMemberPort": virtualServerGroupMemberPort,
       "virtualServerTable": virtualServerTable,
       "virtualServerEntry": virtualServerEntry,
       "virtualServerIndex": virtualServerIndex,
       "virtualServerType": virtualServerType,
       "virtualServerNameOfGroup": virtualServerNameOfGroup,
       "virtualServerFwMark": virtualServerFwMark,
       "virtualServerAddrType": virtualServerAddrType,
       "virtualServerAddress": virtualServerAddress,
       "virtualServerPort": virtualServerPort,
       "virtualServerProtocol": virtualServerProtocol,
       "virtualServerLoadBalancingAlgo": virtualServerLoadBalancingAlgo,
       "virtualServerLoadBalancingKind": virtualServerLoadBalancingKind,
       "virtualServerStatus": virtualServerStatus,
       "virtualServerVirtualHost": virtualServerVirtualHost,
       "virtualServerPersist": virtualServerPersist,
       "virtualServerPersistTimeout": virtualServerPersistTimeout,
       "virtualServerPersistGranularity": virtualServerPersistGranularity,
       "virtualServerDelayLoop": virtualServerDelayLoop,
       "virtualServerHaSuspend": virtualServerHaSuspend,
       "virtualServerAlpha": virtualServerAlpha,
       "virtualServerOmega": virtualServerOmega,
       "virtualServerRealServersTotal": virtualServerRealServersTotal,
       "virtualServerRealServersUp": virtualServerRealServersUp,
       "virtualServerQuorum": virtualServerQuorum,
       "virtualServerQuorumStatus": virtualServerQuorumStatus,
       "virtualServerQuorumUp": virtualServerQuorumUp,
       "virtualServerQuorumDown": virtualServerQuorumDown,
       "virtualServerHysteresis": virtualServerHysteresis,
       "virtualServerStatsConns": virtualServerStatsConns,
       "virtualServerStatsInPkts": virtualServerStatsInPkts,
       "virtualServerStatsOutPkts": virtualServerStatsOutPkts,
       "virtualServerStatsInBytes": virtualServerStatsInBytes,
       "virtualServerStatsOutBytes": virtualServerStatsOutBytes,
       "virtualServerRateCps": virtualServerRateCps,
       "virtualServerRateInPPS": virtualServerRateInPPS,
       "virtualServerRateOutPPS": virtualServerRateOutPPS,
       "virtualServerRateInBPS": virtualServerRateInBPS,
       "virtualServerRateOutBPS": virtualServerRateOutBPS,
       "realServerTable": realServerTable,
       "realServerEntry": realServerEntry,
       "realServerIndex": realServerIndex,
       "realServerType": realServerType,
       "realServerAddrType": realServerAddrType,
       "realServerAddress": realServerAddress,
       "realServerPort": realServerPort,
       "realServerStatus": realServerStatus,
       "realServerWeight": realServerWeight,
       "realServerUpperConnectionLimit": realServerUpperConnectionLimit,
       "realServerLowerConnectionLimit": realServerLowerConnectionLimit,
       "realServerActionWhenDown": realServerActionWhenDown,
       "realServerNotifyUp": realServerNotifyUp,
       "realServerNotifyDown": realServerNotifyDown,
       "realServerFailedChecks": realServerFailedChecks,
       "realServerStatsConns": realServerStatsConns,
       "realServerStatsActiveConns": realServerStatsActiveConns,
       "realServerStatsInactiveConns": realServerStatsInactiveConns,
       "realServerStatsPersistentConns": realServerStatsPersistentConns,
       "realServerStatsInPkts": realServerStatsInPkts,
       "realServerStatsOutPkts": realServerStatsOutPkts,
       "realServerStatsInBytes": realServerStatsInBytes,
       "realServerStatsOutBytes": realServerStatsOutBytes,
       "realServerRateCps": realServerRateCps,
       "realServerRateInPPS": realServerRateInPPS,
       "realServerRateOutPPS": realServerRateOutPPS,
       "realServerRateInBPS": realServerRateInBPS,
       "realServerRateOutBPS": realServerRateOutBPS,
       "checkTrap": checkTrap,
       "checkTraps": checkTraps,
       "realServerStateChange": realServerStateChange,
       "virtualServerQuorumStateChange": virtualServerQuorumStateChange,
       "checkTrapControl": checkTrapControl,
       "conformance": conformance,
       "compliances": compliances,
       "globalCompliances": globalCompliances,
       "vrrpCompliances": vrrpCompliances,
       "checkCompliances": checkCompliances,
       "groups": groups,
       "globalGroup": globalGroup,
       "vrrpGroups": vrrpGroups,
       "vrrpSyncGroup": vrrpSyncGroup,
       "vrrpInstanceGroup": vrrpInstanceGroup,
       "vrrpScriptGroup": vrrpScriptGroup,
       "vrrpTrapsGroup": vrrpTrapsGroup,
       "checkGroups": checkGroups,
       "virtualServerGroupGroup": virtualServerGroupGroup,
       "virtualServerGroup": virtualServerGroup,
       "realServerGroup": realServerGroup,
       "checkTrapsGroup": checkTrapsGroup}
)
