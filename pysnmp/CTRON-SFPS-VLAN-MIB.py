# SNMP MIB module (CTRON-SFPS-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:35 2024
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

(vlanAMRRules,
 vlanAMRStats,
 vlanAMRSubnets,
 vlanAPI,
 vlanCountAPI,
 vlanName,
 vlanPort,
 vlanSystem,
 vlanTestAPI) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "vlanAMRRules",
    "vlanAMRStats",
    "vlanAMRSubnets",
    "vlanAPI",
    "vlanCountAPI",
    "vlanName",
    "vlanPort",
    "vlanSystem",
    "vlanTestAPI")

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



class VlanSwitchInstance(Integer32):
    """Custom type VlanSwitchInstance based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""




class SfpsSwitchPort(Integer32):
    """Custom type SfpsSwitchPort based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SfpsVAPIVerb_Type(Integer32):
    """Custom type sfpsVAPIVerb based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("add-vlan", 2),
          ("auto-register", 14),
          ("auto-unregister", 15),
          ("delete-vlan", 3),
          ("disable-port", 9),
          ("disable-vlan", 5),
          ("enable-port", 8),
          ("enable-vlan", 4),
          ("map-port", 6),
          ("map-user", 10),
          ("other", 1),
          ("tap-vlan", 12),
          ("unmap-port", 7),
          ("unmap-user", 11),
          ("untap-vlan", 13))
    )


_SfpsVAPIVerb_Type.__name__ = "Integer32"
_SfpsVAPIVerb_Object = MibScalar
sfpsVAPIVerb = _SfpsVAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 1),
    _SfpsVAPIVerb_Type()
)
sfpsVAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIVerb.setStatus("mandatory")
_SfpsVAPIInPort_Type = SfpsSwitchPort
_SfpsVAPIInPort_Object = MibScalar
sfpsVAPIInPort = _SfpsVAPIInPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 2),
    _SfpsVAPIInPort_Type()
)
sfpsVAPIInPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIInPort.setStatus("mandatory")
_SfpsVAPIVlanName_Type = DisplayString
_SfpsVAPIVlanName_Object = MibScalar
sfpsVAPIVlanName = _SfpsVAPIVlanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 3),
    _SfpsVAPIVlanName_Type()
)
sfpsVAPIVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIVlanName.setStatus("mandatory")
_SfpsVAPIOutPort_Type = SfpsSwitchPort
_SfpsVAPIOutPort_Object = MibScalar
sfpsVAPIOutPort = _SfpsVAPIOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 4),
    _SfpsVAPIOutPort_Type()
)
sfpsVAPIOutPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIOutPort.setStatus("mandatory")
_SfpsVAPIUserMAC_Type = SfpsAddress
_SfpsVAPIUserMAC_Object = MibScalar
sfpsVAPIUserMAC = _SfpsVAPIUserMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 5),
    _SfpsVAPIUserMAC_Type()
)
sfpsVAPIUserMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIUserMAC.setStatus("mandatory")


class _SfpsVAPIUserAliasTag_Type(Integer32):
    """Custom type sfpsVAPIUserAliasTag based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("aoAtDDP", 11),
          ("aoEmpty", 12),
          ("aoHostName", 14),
          ("aoInetIP", 7),
          ("aoInetIPMask", 16),
          ("aoInetRIP", 9),
          ("aoInetRPC", 8),
          ("aoInetUDP", 5),
          ("aoInetYP", 4),
          ("aoIpxIpx", 6),
          ("aoIpxRIP", 3),
          ("aoIpxSap", 2),
          ("aoMacDXMcast", 10),
          ("aoMacDx", 1),
          ("aoNetBiosName", 15),
          ("aoVlan", 13))
    )


_SfpsVAPIUserAliasTag_Type.__name__ = "Integer32"
_SfpsVAPIUserAliasTag_Object = MibScalar
sfpsVAPIUserAliasTag = _SfpsVAPIUserAliasTag_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 6),
    _SfpsVAPIUserAliasTag_Type()
)
sfpsVAPIUserAliasTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIUserAliasTag.setStatus("mandatory")
_SfpsVAPIUserAlias_Type = DisplayString
_SfpsVAPIUserAlias_Object = MibScalar
sfpsVAPIUserAlias = _SfpsVAPIUserAlias_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 7),
    _SfpsVAPIUserAlias_Type()
)
sfpsVAPIUserAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIUserAlias.setStatus("mandatory")


class _SfpsVAPIAdminStatus_Type(Integer32):
    """Custom type sfpsVAPIAdminStatus based on Integer32"""
    defaultValue = 3

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


_SfpsVAPIAdminStatus_Type.__name__ = "Integer32"
_SfpsVAPIAdminStatus_Object = MibScalar
sfpsVAPIAdminStatus = _SfpsVAPIAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 8),
    _SfpsVAPIAdminStatus_Type()
)
sfpsVAPIAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIAdminStatus.setStatus("mandatory")


class _SfpsVAPIAutoRegisterRule_Type(Integer32):
    """Custom type sfpsVAPIAutoRegisterRule based on Integer32"""
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
        *(("appleTalk", 6),
          ("bpdu", 9),
          ("decNET", 7),
          ("ether-type", 2),
          ("ip-subnet", 3),
          ("ipx-Server", 5),
          ("netBIOS", 4),
          ("other", 1),
          ("vines", 8))
    )


_SfpsVAPIAutoRegisterRule_Type.__name__ = "Integer32"
_SfpsVAPIAutoRegisterRule_Object = MibScalar
sfpsVAPIAutoRegisterRule = _SfpsVAPIAutoRegisterRule_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 9),
    _SfpsVAPIAutoRegisterRule_Type()
)
sfpsVAPIAutoRegisterRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIAutoRegisterRule.setStatus("mandatory")
_SfpsVAPIAutoRegMask_Type = IpAddress
_SfpsVAPIAutoRegMask_Object = MibScalar
sfpsVAPIAutoRegMask = _SfpsVAPIAutoRegMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 10),
    _SfpsVAPIAutoRegMask_Type()
)
sfpsVAPIAutoRegMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIAutoRegMask.setStatus("mandatory")
_SfpsVAPIAutoRegValue_Type = IpAddress
_SfpsVAPIAutoRegValue_Object = MibScalar
sfpsVAPIAutoRegValue = _SfpsVAPIAutoRegValue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 11),
    _SfpsVAPIAutoRegValue_Type()
)
sfpsVAPIAutoRegValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIAutoRegValue.setStatus("mandatory")


class _SfpsVAPIUnicastPolicy_Type(Integer32):
    """Custom type sfpsVAPIUnicastPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 2),
          ("other", 1),
          ("secure", 3))
    )


_SfpsVAPIUnicastPolicy_Type.__name__ = "Integer32"
_SfpsVAPIUnicastPolicy_Object = MibScalar
sfpsVAPIUnicastPolicy = _SfpsVAPIUnicastPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 12),
    _SfpsVAPIUnicastPolicy_Type()
)
sfpsVAPIUnicastPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIUnicastPolicy.setStatus("mandatory")


class _SfpsVAPIPortPolicy_Type(Integer32):
    """Custom type sfpsVAPIPortPolicy based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 3),
          ("normal", 2),
          ("other", 1))
    )


_SfpsVAPIPortPolicy_Type.__name__ = "Integer32"
_SfpsVAPIPortPolicy_Object = MibScalar
sfpsVAPIPortPolicy = _SfpsVAPIPortPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 13),
    _SfpsVAPIPortPolicy_Type()
)
sfpsVAPIPortPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIPortPolicy.setStatus("mandatory")


class _SfpsVAPIFloodPolicy_Type(Integer32):
    """Custom type sfpsVAPIFloodPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flooding-off", 3),
          ("flooding-on", 2),
          ("other", 1))
    )


_SfpsVAPIFloodPolicy_Type.__name__ = "Integer32"
_SfpsVAPIFloodPolicy_Object = MibScalar
sfpsVAPIFloodPolicy = _SfpsVAPIFloodPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 14),
    _SfpsVAPIFloodPolicy_Type()
)
sfpsVAPIFloodPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIFloodPolicy.setStatus("mandatory")


class _SfpsVAPIRouterPort_Type(Integer32):
    """Custom type sfpsVAPIRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-router", 3),
          ("other", 1),
          ("router-port", 2))
    )


_SfpsVAPIRouterPort_Type.__name__ = "Integer32"
_SfpsVAPIRouterPort_Object = MibScalar
sfpsVAPIRouterPort = _SfpsVAPIRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 15),
    _SfpsVAPIRouterPort_Type()
)
sfpsVAPIRouterPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIRouterPort.setStatus("mandatory")
_SfpsVAPIVlanId_Type = Integer32
_SfpsVAPIVlanId_Object = MibScalar
sfpsVAPIVlanId = _SfpsVAPIVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 16),
    _SfpsVAPIVlanId_Type()
)
sfpsVAPIVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIVlanId.setStatus("mandatory")
_SfpsVAPINvramId_Type = Integer32
_SfpsVAPINvramId_Object = MibScalar
sfpsVAPINvramId = _SfpsVAPINvramId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 17),
    _SfpsVAPINvramId_Type()
)
sfpsVAPINvramId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPINvramId.setStatus("mandatory")
_SfpsVAPIRelayAgent_Type = IpAddress
_SfpsVAPIRelayAgent_Object = MibScalar
sfpsVAPIRelayAgent = _SfpsVAPIRelayAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 18),
    _SfpsVAPIRelayAgent_Type()
)
sfpsVAPIRelayAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPIRelayAgent.setStatus("mandatory")


class _SfpsVAPILayer3Learning_Type(Integer32):
    """Custom type sfpsVAPILayer3Learning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learning-disabled", 3),
          ("learning-enabled", 2),
          ("other", 1))
    )


_SfpsVAPILayer3Learning_Type.__name__ = "Integer32"
_SfpsVAPILayer3Learning_Object = MibScalar
sfpsVAPILayer3Learning = _SfpsVAPILayer3Learning_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 1, 19),
    _SfpsVAPILayer3Learning_Type()
)
sfpsVAPILayer3Learning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsVAPILayer3Learning.setStatus("mandatory")
_VlanNameTable_Object = MibTable
vlanNameTable = _VlanNameTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    vlanNameTable.setStatus("mandatory")
_VlanNameEntry_Object = MibTableRow
vlanNameEntry = _VlanNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1)
)
vlanNameEntry.setIndexNames(
    (0, "CTRON-SFPS-VLAN-MIB", "vlanNameNHash"),
    (0, "CTRON-SFPS-VLAN-MIB", "vlanNameIndex"),
)
if mibBuilder.loadTexts:
    vlanNameEntry.setStatus("mandatory")
_VlanNameNHash_Type = HexInteger
_VlanNameNHash_Object = MibTableColumn
vlanNameNHash = _VlanNameNHash_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 1),
    _VlanNameNHash_Type()
)
vlanNameNHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameNHash.setStatus("mandatory")
_VlanNameIndex_Type = Integer32
_VlanNameIndex_Object = MibTableColumn
vlanNameIndex = _VlanNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 2),
    _VlanNameIndex_Type()
)
vlanNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameIndex.setStatus("mandatory")
_VlanNameVlanName_Type = DisplayString
_VlanNameVlanName_Object = MibTableColumn
vlanNameVlanName = _VlanNameVlanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 3),
    _VlanNameVlanName_Type()
)
vlanNameVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameVlanName.setStatus("mandatory")


class _VlanNameAdminStatus_Type(Integer32):
    """Custom type vlanNameAdminStatus based on Integer32"""
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


_VlanNameAdminStatus_Type.__name__ = "Integer32"
_VlanNameAdminStatus_Object = MibTableColumn
vlanNameAdminStatus = _VlanNameAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 4),
    _VlanNameAdminStatus_Type()
)
vlanNameAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameAdminStatus.setStatus("mandatory")


class _VlanNameOperStatus_Type(Integer32):
    """Custom type vlanNameOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("shutdown-pending", 4),
          ("startup-pending", 5),
          ("testing", 7))
    )


_VlanNameOperStatus_Type.__name__ = "Integer32"
_VlanNameOperStatus_Object = MibTableColumn
vlanNameOperStatus = _VlanNameOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 5),
    _VlanNameOperStatus_Type()
)
vlanNameOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameOperStatus.setStatus("mandatory")


class _VlanNameUniPolicy_Type(Integer32):
    """Custom type vlanNameUniPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 2),
          ("other", 1),
          ("secure", 3))
    )


_VlanNameUniPolicy_Type.__name__ = "Integer32"
_VlanNameUniPolicy_Object = MibTableColumn
vlanNameUniPolicy = _VlanNameUniPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 6),
    _VlanNameUniPolicy_Type()
)
vlanNameUniPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameUniPolicy.setStatus("mandatory")


class _VlanNameFloodPolicy_Type(Integer32):
    """Custom type vlanNameFloodPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flood-off", 2),
          ("flood-on", 3),
          ("other", 1))
    )


_VlanNameFloodPolicy_Type.__name__ = "Integer32"
_VlanNameFloodPolicy_Object = MibTableColumn
vlanNameFloodPolicy = _VlanNameFloodPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 7),
    _VlanNameFloodPolicy_Type()
)
vlanNameFloodPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameFloodPolicy.setStatus("mandatory")
_VlanNameStatusTime_Type = TimeTicks
_VlanNameStatusTime_Object = MibTableColumn
vlanNameStatusTime = _VlanNameStatusTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 8),
    _VlanNameStatusTime_Type()
)
vlanNameStatusTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameStatusTime.setStatus("mandatory")
_VlanNameNumUsers_Type = DisplayString
_VlanNameNumUsers_Object = MibTableColumn
vlanNameNumUsers = _VlanNameNumUsers_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 9),
    _VlanNameNumUsers_Type()
)
vlanNameNumUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameNumUsers.setStatus("mandatory")
_VlanNameEnabledPorts_Type = DisplayString
_VlanNameEnabledPorts_Object = MibTableColumn
vlanNameEnabledPorts = _VlanNameEnabledPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 10),
    _VlanNameEnabledPorts_Type()
)
vlanNameEnabledPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameEnabledPorts.setStatus("mandatory")
_VlanNameMappedPorts_Type = DisplayString
_VlanNameMappedPorts_Object = MibTableColumn
vlanNameMappedPorts = _VlanNameMappedPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 11),
    _VlanNameMappedPorts_Type()
)
vlanNameMappedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameMappedPorts.setStatus("mandatory")
_VlanNameVlanRule_Type = Integer32
_VlanNameVlanRule_Object = MibTableColumn
vlanNameVlanRule = _VlanNameVlanRule_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 12),
    _VlanNameVlanRule_Type()
)
vlanNameVlanRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameVlanRule.setStatus("mandatory")
_VlanNameFloodPorts_Type = DisplayString
_VlanNameFloodPorts_Object = MibTableColumn
vlanNameFloodPorts = _VlanNameFloodPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 13),
    _VlanNameFloodPorts_Type()
)
vlanNameFloodPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameFloodPorts.setStatus("mandatory")
_VlanNameVlanId_Type = Integer32
_VlanNameVlanId_Object = MibTableColumn
vlanNameVlanId = _VlanNameVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 14),
    _VlanNameVlanId_Type()
)
vlanNameVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameVlanId.setStatus("mandatory")
_VlanNameRelayAgent_Type = IpAddress
_VlanNameRelayAgent_Object = MibTableColumn
vlanNameRelayAgent = _VlanNameRelayAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 1, 1, 1, 15),
    _VlanNameRelayAgent_Type()
)
vlanNameRelayAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNameRelayAgent.setStatus("mandatory")
_VlanSystemTable_Object = MibTable
vlanSystemTable = _VlanSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    vlanSystemTable.setStatus("mandatory")
_VlanSystemEntry_Object = MibTableRow
vlanSystemEntry = _VlanSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1)
)
vlanSystemEntry.setIndexNames(
    (0, "CTRON-SFPS-VLAN-MIB", "vlanSystemSwitchInstance"),
)
if mibBuilder.loadTexts:
    vlanSystemEntry.setStatus("mandatory")
_VlanSystemSwitchInstance_Type = VlanSwitchInstance
_VlanSystemSwitchInstance_Object = MibTableColumn
vlanSystemSwitchInstance = _VlanSystemSwitchInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 1),
    _VlanSystemSwitchInstance_Type()
)
vlanSystemSwitchInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemSwitchInstance.setStatus("mandatory")


class _VlanSystemAdminStatus_Type(Integer32):
    """Custom type vlanSystemAdminStatus based on Integer32"""
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


_VlanSystemAdminStatus_Type.__name__ = "Integer32"
_VlanSystemAdminStatus_Object = MibTableColumn
vlanSystemAdminStatus = _VlanSystemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 2),
    _VlanSystemAdminStatus_Type()
)
vlanSystemAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSystemAdminStatus.setStatus("mandatory")


class _VlanSystemAdminReset_Type(Integer32):
    """Custom type vlanSystemAdminReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_VlanSystemAdminReset_Type.__name__ = "Integer32"
_VlanSystemAdminReset_Object = MibTableColumn
vlanSystemAdminReset = _VlanSystemAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 3),
    _VlanSystemAdminReset_Type()
)
vlanSystemAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSystemAdminReset.setStatus("mandatory")


class _VlanSystemOperStatus_Type(Integer32):
    """Custom type vlanSystemOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_VlanSystemOperStatus_Type.__name__ = "Integer32"
_VlanSystemOperStatus_Object = MibTableColumn
vlanSystemOperStatus = _VlanSystemOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 4),
    _VlanSystemOperStatus_Type()
)
vlanSystemOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemOperStatus.setStatus("mandatory")
_VlanSystemOperTime_Type = TimeTicks
_VlanSystemOperTime_Object = MibTableColumn
vlanSystemOperTime = _VlanSystemOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 5),
    _VlanSystemOperTime_Type()
)
vlanSystemOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemOperTime.setStatus("mandatory")
_VlanSystemLastChange_Type = TimeTicks
_VlanSystemLastChange_Object = MibTableColumn
vlanSystemLastChange = _VlanSystemLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 6),
    _VlanSystemLastChange_Type()
)
vlanSystemLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemLastChange.setStatus("mandatory")
_VlanSystemVersion_Type = DisplayString
_VlanSystemVersion_Object = MibTableColumn
vlanSystemVersion = _VlanSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 7),
    _VlanSystemVersion_Type()
)
vlanSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemVersion.setStatus("mandatory")
_VlanSystemMibRev_Type = DisplayString
_VlanSystemMibRev_Object = MibTableColumn
vlanSystemMibRev = _VlanSystemMibRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 8),
    _VlanSystemMibRev_Type()
)
vlanSystemMibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemMibRev.setStatus("mandatory")
_VlanSystemAgentIP_Type = IpAddress
_VlanSystemAgentIP_Object = MibTableColumn
vlanSystemAgentIP = _VlanSystemAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 9),
    _VlanSystemAgentIP_Type()
)
vlanSystemAgentIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSystemAgentIP.setStatus("mandatory")
_VlanSystemDomainName_Type = DisplayString
_VlanSystemDomainName_Object = MibTableColumn
vlanSystemDomainName = _VlanSystemDomainName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 10),
    _VlanSystemDomainName_Type()
)
vlanSystemDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSystemDomainName.setStatus("mandatory")
_VlanSystemPollCount_Type = Integer32
_VlanSystemPollCount_Object = MibTableColumn
vlanSystemPollCount = _VlanSystemPollCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 11),
    _VlanSystemPollCount_Type()
)
vlanSystemPollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemPollCount.setStatus("mandatory")
_VlanSystemFirstPollTime_Type = TimeTicks
_VlanSystemFirstPollTime_Object = MibTableColumn
vlanSystemFirstPollTime = _VlanSystemFirstPollTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 12),
    _VlanSystemFirstPollTime_Type()
)
vlanSystemFirstPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemFirstPollTime.setStatus("mandatory")
_VlanSystemLastPollTime_Type = TimeTicks
_VlanSystemLastPollTime_Object = MibTableColumn
vlanSystemLastPollTime = _VlanSystemLastPollTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 13),
    _VlanSystemLastPollTime_Type()
)
vlanSystemLastPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemLastPollTime.setStatus("mandatory")
_VlanSystemPriorPollTime_Type = TimeTicks
_VlanSystemPriorPollTime_Object = MibTableColumn
vlanSystemPriorPollTime = _VlanSystemPriorPollTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 14),
    _VlanSystemPriorPollTime_Type()
)
vlanSystemPriorPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemPriorPollTime.setStatus("mandatory")
_VlanSystemDeltaPollTime_Type = TimeTicks
_VlanSystemDeltaPollTime_Object = MibTableColumn
vlanSystemDeltaPollTime = _VlanSystemDeltaPollTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 5, 1, 1, 15),
    _VlanSystemDeltaPollTime_Type()
)
vlanSystemDeltaPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSystemDeltaPollTime.setStatus("mandatory")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("mandatory")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1)
)
vlanPortEntry.setIndexNames(
    (0, "CTRON-SFPS-VLAN-MIB", "vlanPortPortNum"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("mandatory")
_VlanPortPortNum_Type = Integer32
_VlanPortPortNum_Object = MibTableColumn
vlanPortPortNum = _VlanPortPortNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 1),
    _VlanPortPortNum_Type()
)
vlanPortPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortPortNum.setStatus("mandatory")


class _VlanPortPortStatus_Type(Integer32):
    """Custom type vlanPortPortStatus based on Integer32"""
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


_VlanPortPortStatus_Type.__name__ = "Integer32"
_VlanPortPortStatus_Object = MibTableColumn
vlanPortPortStatus = _VlanPortPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 2),
    _VlanPortPortStatus_Type()
)
vlanPortPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortPortStatus.setStatus("mandatory")


class _VlanPortPortPolicy_Type(Integer32):
    """Custom type vlanPortPortPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 3),
          ("normal", 2),
          ("other", 1))
    )


_VlanPortPortPolicy_Type.__name__ = "Integer32"
_VlanPortPortPolicy_Object = MibTableColumn
vlanPortPortPolicy = _VlanPortPortPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 3),
    _VlanPortPortPolicy_Type()
)
vlanPortPortPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortPortPolicy.setStatus("mandatory")
_VlanPortVlanName_Type = DisplayString
_VlanPortVlanName_Object = MibTableColumn
vlanPortVlanName = _VlanPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 4),
    _VlanPortVlanName_Type()
)
vlanPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortVlanName.setStatus("mandatory")


class _VlanPortAdminStatus_Type(Integer32):
    """Custom type vlanPortAdminStatus based on Integer32"""
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


_VlanPortAdminStatus_Type.__name__ = "Integer32"
_VlanPortAdminStatus_Object = MibTableColumn
vlanPortAdminStatus = _VlanPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 5),
    _VlanPortAdminStatus_Type()
)
vlanPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortAdminStatus.setStatus("mandatory")


class _VlanPortUniPolicy_Type(Integer32):
    """Custom type vlanPortUniPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 2),
          ("other", 1),
          ("secure", 3))
    )


_VlanPortUniPolicy_Type.__name__ = "Integer32"
_VlanPortUniPolicy_Object = MibTableColumn
vlanPortUniPolicy = _VlanPortUniPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 6),
    _VlanPortUniPolicy_Type()
)
vlanPortUniPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortUniPolicy.setStatus("mandatory")


class _VlanPortFloodPolicy_Type(Integer32):
    """Custom type vlanPortFloodPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("floodOff", 3),
          ("floodOn", 2),
          ("other", 1))
    )


_VlanPortFloodPolicy_Type.__name__ = "Integer32"
_VlanPortFloodPolicy_Object = MibTableColumn
vlanPortFloodPolicy = _VlanPortFloodPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 7),
    _VlanPortFloodPolicy_Type()
)
vlanPortFloodPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortFloodPolicy.setStatus("mandatory")


class _VlanPortRouterPort_Type(Integer32):
    """Custom type vlanPortRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRouter", 3),
          ("other", 1),
          ("routerPort", 2))
    )


_VlanPortRouterPort_Type.__name__ = "Integer32"
_VlanPortRouterPort_Object = MibTableColumn
vlanPortRouterPort = _VlanPortRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 8),
    _VlanPortRouterPort_Type()
)
vlanPortRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortRouterPort.setStatus("mandatory")
_VlanPortVlanId_Type = Integer32
_VlanPortVlanId_Object = MibTableColumn
vlanPortVlanId = _VlanPortVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 9),
    _VlanPortVlanId_Type()
)
vlanPortVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortVlanId.setStatus("mandatory")
_VlanPortRelayAgent_Type = IpAddress
_VlanPortRelayAgent_Object = MibTableColumn
vlanPortRelayAgent = _VlanPortRelayAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 10),
    _VlanPortRelayAgent_Type()
)
vlanPortRelayAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortRelayAgent.setStatus("mandatory")


class _VlanPortLayer3Learning_Type(Integer32):
    """Custom type vlanPortLayer3Learning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabed", 3),
          ("enabled", 2),
          ("other", 1))
    )


_VlanPortLayer3Learning_Type.__name__ = "Integer32"
_VlanPortLayer3Learning_Object = MibTableColumn
vlanPortLayer3Learning = _VlanPortLayer3Learning_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 6, 1, 1, 11),
    _VlanPortLayer3Learning_Type()
)
vlanPortLayer3Learning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortLayer3Learning.setStatus("mandatory")


class _VlanTestAPIVerb_Type(Integer32):
    """Custom type vlanTestAPIVerb based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("add-vlan", 2),
          ("delete-vlan", 3),
          ("disable-vlan", 5),
          ("disable-vlan-port", 9),
          ("empty-table", 17),
          ("enable-vlan", 4),
          ("enable-vlan-port", 8),
          ("fill-table", 16),
          ("get-port-info", 15),
          ("get-vlan-info", 14),
          ("map-vlan-port", 10),
          ("open-vlan", 6),
          ("other", 1),
          ("secure-vlan", 7),
          ("tap-vlan-port", 12),
          ("unmap-vlan-port", 11),
          ("untap-vlan-port", 13))
    )


_VlanTestAPIVerb_Type.__name__ = "Integer32"
_VlanTestAPIVerb_Object = MibScalar
vlanTestAPIVerb = _VlanTestAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 1),
    _VlanTestAPIVerb_Type()
)
vlanTestAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTestAPIVerb.setStatus("mandatory")
_VlanTestAPIVlanName_Type = DisplayString
_VlanTestAPIVlanName_Object = MibScalar
vlanTestAPIVlanName = _VlanTestAPIVlanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 2),
    _VlanTestAPIVlanName_Type()
)
vlanTestAPIVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTestAPIVlanName.setStatus("mandatory")
_VlanTestAPIPort_Type = Integer32
_VlanTestAPIPort_Object = MibScalar
vlanTestAPIPort = _VlanTestAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 3),
    _VlanTestAPIPort_Type()
)
vlanTestAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTestAPIPort.setStatus("mandatory")
_VlanTestAPIOutputTable_Object = MibTable
vlanTestAPIOutputTable = _VlanTestAPIOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4)
)
if mibBuilder.loadTexts:
    vlanTestAPIOutputTable.setStatus("mandatory")
_VlanTestAPIOutputEntry_Object = MibTableRow
vlanTestAPIOutputEntry = _VlanTestAPIOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1)
)
vlanTestAPIOutputEntry.setIndexNames(
    (0, "CTRON-SFPS-VLAN-MIB", "vlanTestAPIOutputIndex"),
)
if mibBuilder.loadTexts:
    vlanTestAPIOutputEntry.setStatus("mandatory")
_VlanTestAPIOutputIndex_Type = Integer32
_VlanTestAPIOutputIndex_Object = MibTableColumn
vlanTestAPIOutputIndex = _VlanTestAPIOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 1),
    _VlanTestAPIOutputIndex_Type()
)
vlanTestAPIOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputIndex.setStatus("mandatory")
_VlanTestAPIOutputVlanName_Type = DisplayString
_VlanTestAPIOutputVlanName_Object = MibTableColumn
vlanTestAPIOutputVlanName = _VlanTestAPIOutputVlanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 2),
    _VlanTestAPIOutputVlanName_Type()
)
vlanTestAPIOutputVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputVlanName.setStatus("mandatory")
_VlanTestAPIOutputUserCnt_Type = Integer32
_VlanTestAPIOutputUserCnt_Object = MibTableColumn
vlanTestAPIOutputUserCnt = _VlanTestAPIOutputUserCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 3),
    _VlanTestAPIOutputUserCnt_Type()
)
vlanTestAPIOutputUserCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputUserCnt.setStatus("mandatory")


class _VlanTestAPIOutputStatus_Type(Integer32):
    """Custom type vlanTestAPIOutputStatus based on Integer32"""
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


_VlanTestAPIOutputStatus_Type.__name__ = "Integer32"
_VlanTestAPIOutputStatus_Object = MibTableColumn
vlanTestAPIOutputStatus = _VlanTestAPIOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 4),
    _VlanTestAPIOutputStatus_Type()
)
vlanTestAPIOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputStatus.setStatus("mandatory")


class _VlanTestAPIOutputPolicy_Type(Integer32):
    """Custom type vlanTestAPIOutputPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("other", 1),
          ("secure", 3))
    )


_VlanTestAPIOutputPolicy_Type.__name__ = "Integer32"
_VlanTestAPIOutputPolicy_Object = MibTableColumn
vlanTestAPIOutputPolicy = _VlanTestAPIOutputPolicy_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 5),
    _VlanTestAPIOutputPolicy_Type()
)
vlanTestAPIOutputPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputPolicy.setStatus("mandatory")
_VlanTestAPIOutputPort_Type = Integer32
_VlanTestAPIOutputPort_Object = MibTableColumn
vlanTestAPIOutputPort = _VlanTestAPIOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 6),
    _VlanTestAPIOutputPort_Type()
)
vlanTestAPIOutputPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputPort.setStatus("mandatory")


class _VlanTestAPIOutputMap_Type(Integer32):
    """Custom type vlanTestAPIOutputMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mapped", 3),
          ("other", 1),
          ("unmapped", 2))
    )


_VlanTestAPIOutputMap_Type.__name__ = "Integer32"
_VlanTestAPIOutputMap_Object = MibTableColumn
vlanTestAPIOutputMap = _VlanTestAPIOutputMap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 7),
    _VlanTestAPIOutputMap_Type()
)
vlanTestAPIOutputMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputMap.setStatus("mandatory")


class _VlanTestAPIOutputAble_Type(Integer32):
    """Custom type vlanTestAPIOutputAble based on Integer32"""
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


_VlanTestAPIOutputAble_Type.__name__ = "Integer32"
_VlanTestAPIOutputAble_Object = MibTableColumn
vlanTestAPIOutputAble = _VlanTestAPIOutputAble_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 8),
    _VlanTestAPIOutputAble_Type()
)
vlanTestAPIOutputAble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputAble.setStatus("mandatory")


class _VlanTestAPIOutputTap_Type(Integer32):
    """Custom type vlanTestAPIOutputTap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("tapped", 3),
          ("untapped", 2))
    )


_VlanTestAPIOutputTap_Type.__name__ = "Integer32"
_VlanTestAPIOutputTap_Object = MibTableColumn
vlanTestAPIOutputTap = _VlanTestAPIOutputTap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 9),
    _VlanTestAPIOutputTap_Type()
)
vlanTestAPIOutputTap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputTap.setStatus("mandatory")
_VlanTestAPIOutputVlanId_Type = Integer32
_VlanTestAPIOutputVlanId_Object = MibTableColumn
vlanTestAPIOutputVlanId = _VlanTestAPIOutputVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 4, 1, 10),
    _VlanTestAPIOutputVlanId_Type()
)
vlanTestAPIOutputVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTestAPIOutputVlanId.setStatus("mandatory")
_VlanTestAPIVlanId_Type = Integer32
_VlanTestAPIVlanId_Object = MibScalar
vlanTestAPIVlanId = _VlanTestAPIVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 9, 5),
    _VlanTestAPIVlanId_Type()
)
vlanTestAPIVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanTestAPIVlanId.setStatus("mandatory")
_VlanCountAPITotal_Type = Integer32
_VlanCountAPITotal_Object = MibScalar
vlanCountAPITotal = _VlanCountAPITotal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 1),
    _VlanCountAPITotal_Type()
)
vlanCountAPITotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCountAPITotal.setStatus("mandatory")
_VlanCountAPIAdmin_Type = Integer32
_VlanCountAPIAdmin_Object = MibScalar
vlanCountAPIAdmin = _VlanCountAPIAdmin_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 2),
    _VlanCountAPIAdmin_Type()
)
vlanCountAPIAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCountAPIAdmin.setStatus("mandatory")
_VlanCountAPIAutoreg_Type = Integer32
_VlanCountAPIAutoreg_Object = MibScalar
vlanCountAPIAutoreg = _VlanCountAPIAutoreg_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 10, 1, 3),
    _VlanCountAPIAutoreg_Type()
)
vlanCountAPIAutoreg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanCountAPIAutoreg.setStatus("mandatory")
_VlanAMRRulesTable_Object = MibTable
vlanAMRRulesTable = _VlanAMRRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1)
)
if mibBuilder.loadTexts:
    vlanAMRRulesTable.setStatus("mandatory")
_VlanAMRRulesEntry_Object = MibTableRow
vlanAMRRulesEntry = _VlanAMRRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1)
)
vlanAMRRulesEntry.setIndexNames(
    (0, "CTRON-SFPS-VLAN-MIB", "vlanAMRRulesRule"),
)
if mibBuilder.loadTexts:
    vlanAMRRulesEntry.setStatus("mandatory")


class _VlanAMRRulesRule_Type(Integer32):
    """Custom type vlanAMRRulesRule based on Integer32"""
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
        *(("appleTalk", 6),
          ("bpdu", 9),
          ("decNET", 7),
          ("etherType", 2),
          ("ipSubNet", 3),
          ("ipxServer", 5),
          ("netBIOS", 4),
          ("other", 1),
          ("vines", 8))
    )


_VlanAMRRulesRule_Type.__name__ = "Integer32"
_VlanAMRRulesRule_Object = MibTableColumn
vlanAMRRulesRule = _VlanAMRRulesRule_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1, 1),
    _VlanAMRRulesRule_Type()
)
vlanAMRRulesRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAMRRulesRule.setStatus("mandatory")


class _VlanAMRRulesStatus_Type(Integer32):
    """Custom type vlanAMRRulesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_VlanAMRRulesStatus_Type.__name__ = "Integer32"
_VlanAMRRulesStatus_Object = MibTableColumn
vlanAMRRulesStatus = _VlanAMRRulesStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 6, 1, 1, 2),
    _VlanAMRRulesStatus_Type()
)
vlanAMRRulesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAMRRulesStatus.setStatus("mandatory")
_VlanAMRSubnetsPrefix_Type = IpAddress
_VlanAMRSubnetsPrefix_Object = MibScalar
vlanAMRSubnetsPrefix = _VlanAMRSubnetsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 7, 1),
    _VlanAMRSubnetsPrefix_Type()
)
vlanAMRSubnetsPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAMRSubnetsPrefix.setStatus("mandatory")
_VlanAMRSubnetsMask_Type = IpAddress
_VlanAMRSubnetsMask_Object = MibScalar
vlanAMRSubnetsMask = _VlanAMRSubnetsMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 7, 2),
    _VlanAMRSubnetsMask_Type()
)
vlanAMRSubnetsMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAMRSubnetsMask.setStatus("mandatory")
_VlanAMRStatsNumRulesEnabled_Type = Integer32
_VlanAMRStatsNumRulesEnabled_Object = MibScalar
vlanAMRStatsNumRulesEnabled = _VlanAMRStatsNumRulesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 8, 1),
    _VlanAMRStatsNumRulesEnabled_Type()
)
vlanAMRStatsNumRulesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAMRStatsNumRulesEnabled.setStatus("mandatory")
_VlanAMRStatsSingleMask_Type = IpAddress
_VlanAMRStatsSingleMask_Object = MibScalar
vlanAMRStatsSingleMask = _VlanAMRStatsSingleMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 3, 8, 2),
    _VlanAMRStatsSingleMask_Type()
)
vlanAMRStatsSingleMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAMRStatsSingleMask.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-VLAN-MIB",
    **{"VlanSwitchInstance": VlanSwitchInstance,
       "SfpsAddress": SfpsAddress,
       "HexInteger": HexInteger,
       "SfpsSwitchPort": SfpsSwitchPort,
       "sfpsVAPIVerb": sfpsVAPIVerb,
       "sfpsVAPIInPort": sfpsVAPIInPort,
       "sfpsVAPIVlanName": sfpsVAPIVlanName,
       "sfpsVAPIOutPort": sfpsVAPIOutPort,
       "sfpsVAPIUserMAC": sfpsVAPIUserMAC,
       "sfpsVAPIUserAliasTag": sfpsVAPIUserAliasTag,
       "sfpsVAPIUserAlias": sfpsVAPIUserAlias,
       "sfpsVAPIAdminStatus": sfpsVAPIAdminStatus,
       "sfpsVAPIAutoRegisterRule": sfpsVAPIAutoRegisterRule,
       "sfpsVAPIAutoRegMask": sfpsVAPIAutoRegMask,
       "sfpsVAPIAutoRegValue": sfpsVAPIAutoRegValue,
       "sfpsVAPIUnicastPolicy": sfpsVAPIUnicastPolicy,
       "sfpsVAPIPortPolicy": sfpsVAPIPortPolicy,
       "sfpsVAPIFloodPolicy": sfpsVAPIFloodPolicy,
       "sfpsVAPIRouterPort": sfpsVAPIRouterPort,
       "sfpsVAPIVlanId": sfpsVAPIVlanId,
       "sfpsVAPINvramId": sfpsVAPINvramId,
       "sfpsVAPIRelayAgent": sfpsVAPIRelayAgent,
       "sfpsVAPILayer3Learning": sfpsVAPILayer3Learning,
       "vlanNameTable": vlanNameTable,
       "vlanNameEntry": vlanNameEntry,
       "vlanNameNHash": vlanNameNHash,
       "vlanNameIndex": vlanNameIndex,
       "vlanNameVlanName": vlanNameVlanName,
       "vlanNameAdminStatus": vlanNameAdminStatus,
       "vlanNameOperStatus": vlanNameOperStatus,
       "vlanNameUniPolicy": vlanNameUniPolicy,
       "vlanNameFloodPolicy": vlanNameFloodPolicy,
       "vlanNameStatusTime": vlanNameStatusTime,
       "vlanNameNumUsers": vlanNameNumUsers,
       "vlanNameEnabledPorts": vlanNameEnabledPorts,
       "vlanNameMappedPorts": vlanNameMappedPorts,
       "vlanNameVlanRule": vlanNameVlanRule,
       "vlanNameFloodPorts": vlanNameFloodPorts,
       "vlanNameVlanId": vlanNameVlanId,
       "vlanNameRelayAgent": vlanNameRelayAgent,
       "vlanSystemTable": vlanSystemTable,
       "vlanSystemEntry": vlanSystemEntry,
       "vlanSystemSwitchInstance": vlanSystemSwitchInstance,
       "vlanSystemAdminStatus": vlanSystemAdminStatus,
       "vlanSystemAdminReset": vlanSystemAdminReset,
       "vlanSystemOperStatus": vlanSystemOperStatus,
       "vlanSystemOperTime": vlanSystemOperTime,
       "vlanSystemLastChange": vlanSystemLastChange,
       "vlanSystemVersion": vlanSystemVersion,
       "vlanSystemMibRev": vlanSystemMibRev,
       "vlanSystemAgentIP": vlanSystemAgentIP,
       "vlanSystemDomainName": vlanSystemDomainName,
       "vlanSystemPollCount": vlanSystemPollCount,
       "vlanSystemFirstPollTime": vlanSystemFirstPollTime,
       "vlanSystemLastPollTime": vlanSystemLastPollTime,
       "vlanSystemPriorPollTime": vlanSystemPriorPollTime,
       "vlanSystemDeltaPollTime": vlanSystemDeltaPollTime,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortPortNum": vlanPortPortNum,
       "vlanPortPortStatus": vlanPortPortStatus,
       "vlanPortPortPolicy": vlanPortPortPolicy,
       "vlanPortVlanName": vlanPortVlanName,
       "vlanPortAdminStatus": vlanPortAdminStatus,
       "vlanPortUniPolicy": vlanPortUniPolicy,
       "vlanPortFloodPolicy": vlanPortFloodPolicy,
       "vlanPortRouterPort": vlanPortRouterPort,
       "vlanPortVlanId": vlanPortVlanId,
       "vlanPortRelayAgent": vlanPortRelayAgent,
       "vlanPortLayer3Learning": vlanPortLayer3Learning,
       "vlanTestAPIVerb": vlanTestAPIVerb,
       "vlanTestAPIVlanName": vlanTestAPIVlanName,
       "vlanTestAPIPort": vlanTestAPIPort,
       "vlanTestAPIOutputTable": vlanTestAPIOutputTable,
       "vlanTestAPIOutputEntry": vlanTestAPIOutputEntry,
       "vlanTestAPIOutputIndex": vlanTestAPIOutputIndex,
       "vlanTestAPIOutputVlanName": vlanTestAPIOutputVlanName,
       "vlanTestAPIOutputUserCnt": vlanTestAPIOutputUserCnt,
       "vlanTestAPIOutputStatus": vlanTestAPIOutputStatus,
       "vlanTestAPIOutputPolicy": vlanTestAPIOutputPolicy,
       "vlanTestAPIOutputPort": vlanTestAPIOutputPort,
       "vlanTestAPIOutputMap": vlanTestAPIOutputMap,
       "vlanTestAPIOutputAble": vlanTestAPIOutputAble,
       "vlanTestAPIOutputTap": vlanTestAPIOutputTap,
       "vlanTestAPIOutputVlanId": vlanTestAPIOutputVlanId,
       "vlanTestAPIVlanId": vlanTestAPIVlanId,
       "vlanCountAPITotal": vlanCountAPITotal,
       "vlanCountAPIAdmin": vlanCountAPIAdmin,
       "vlanCountAPIAutoreg": vlanCountAPIAutoreg,
       "vlanAMRRulesTable": vlanAMRRulesTable,
       "vlanAMRRulesEntry": vlanAMRRulesEntry,
       "vlanAMRRulesRule": vlanAMRRulesRule,
       "vlanAMRRulesStatus": vlanAMRRulesStatus,
       "vlanAMRSubnetsPrefix": vlanAMRSubnetsPrefix,
       "vlanAMRSubnetsMask": vlanAMRSubnetsMask,
       "vlanAMRStatsNumRulesEnabled": vlanAMRStatsNumRulesEnabled,
       "vlanAMRStatsSingleMask": vlanAMRStatsSingleMask}
)
