# SNMP MIB module (CIENA-CES-ACCESS-LIST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-ACCESS-LIST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:52 2024
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

(cienaCesConfig,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesAccessListMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35)
)
cienaCesAccessListMIB.setRevisions(
        ("2015-04-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AclFilterAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )



class AclTrafficDirection(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egress", 2),
          ("ingress", 1))
    )



class AclIpFragmentMatchType(Integer32, TextualConvention):
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
        *(("any", 1),
          ("isfragment", 2),
          ("notfragment", 3))
    )



class AclL4PortMatchType(Integer32, TextualConvention):
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
        *(("any", 1),
          ("range", 3),
          ("single", 2))
    )



class AclInterfaceType(Integer32, TextualConvention):
    status = "current"
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
        *(("ipinterface", 4),
          ("localinterface", 6),
          ("port", 1),
          ("remoteinterface", 5),
          ("virtualswitch", 3),
          ("vlan", 2))
    )



class AclL4DstProtocol(Integer32, TextualConvention):
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
              20,
              21,
              22,
              23,
              24)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("bgp", 2),
          ("bootpclient", 3),
          ("bootpserver", 4),
          ("dhcpclient", 5),
          ("dhcpserver", 6),
          ("dhcpv6client", 7),
          ("dhcpv6server", 8),
          ("dns", 9),
          ("ftp", 10),
          ("http", 11),
          ("ldp", 12),
          ("ntp", 13),
          ("olsr", 14),
          ("rip", 15),
          ("rpc", 16),
          ("snmp", 17),
          ("snmptrap", 18),
          ("ssh", 19),
          ("syslog", 20),
          ("tacacs", 21),
          ("telnet", 22),
          ("tftp", 23),
          ("twampctrl", 24))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesAccessListMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesAccessListMIBObjects = _CienaCesAccessListMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1)
)
_CienaCesAclConfiguration_ObjectIdentity = ObjectIdentity
cienaCesAclConfiguration = _CienaCesAclConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1)
)
_CienaCesAclGlobalConfig_ObjectIdentity = ObjectIdentity
cienaCesAclGlobalConfig = _CienaCesAclGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 1)
)
_CienaCesAclAdminStatus_Type = CienaGlobalState
_CienaCesAclAdminStatus_Object = MibScalar
cienaCesAclAdminStatus = _CienaCesAclAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 1, 1),
    _CienaCesAclAdminStatus_Type()
)
cienaCesAclAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclAdminStatus.setStatus("current")


class _CienaCesAclFilterMode_Type(Integer32):
    """Custom type cienaCesAclFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l2l3combo", 1),
          ("l3only", 2))
    )


_CienaCesAclFilterMode_Type.__name__ = "Integer32"
_CienaCesAclFilterMode_Object = MibScalar
cienaCesAclFilterMode = _CienaCesAclFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 1, 2),
    _CienaCesAclFilterMode_Type()
)
cienaCesAclFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclFilterMode.setStatus("current")
_CienaCesAclNumAclProfileDefs_Type = Unsigned32
_CienaCesAclNumAclProfileDefs_Object = MibScalar
cienaCesAclNumAclProfileDefs = _CienaCesAclNumAclProfileDefs_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 1, 3),
    _CienaCesAclNumAclProfileDefs_Type()
)
cienaCesAclNumAclProfileDefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclNumAclProfileDefs.setStatus("current")
_CienaCesAclRemainingAclProfileDefs_Type = Unsigned32
_CienaCesAclRemainingAclProfileDefs_Object = MibScalar
cienaCesAclRemainingAclProfileDefs = _CienaCesAclRemainingAclProfileDefs_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 1, 4),
    _CienaCesAclRemainingAclProfileDefs_Type()
)
cienaCesAclRemainingAclProfileDefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRemainingAclProfileDefs.setStatus("current")
_CienaCesAclNumAclRuleDefs_Type = Unsigned32
_CienaCesAclNumAclRuleDefs_Object = MibScalar
cienaCesAclNumAclRuleDefs = _CienaCesAclNumAclRuleDefs_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 1, 5),
    _CienaCesAclNumAclRuleDefs_Type()
)
cienaCesAclNumAclRuleDefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclNumAclRuleDefs.setStatus("current")
_CienaCesAclRemainingAclRuleDefs_Type = Unsigned32
_CienaCesAclRemainingAclRuleDefs_Object = MibScalar
cienaCesAclRemainingAclRuleDefs = _CienaCesAclRemainingAclRuleDefs_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 1, 6),
    _CienaCesAclRemainingAclRuleDefs_Type()
)
cienaCesAclRemainingAclRuleDefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRemainingAclRuleDefs.setStatus("current")
_CienaCesAclProfileConfigTable_Object = MibTable
cienaCesAclProfileConfigTable = _CienaCesAclProfileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cienaCesAclProfileConfigTable.setStatus("current")
_CienaCesAclProfileConfigTableEntry_Object = MibTableRow
cienaCesAclProfileConfigTableEntry = _CienaCesAclProfileConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1)
)
cienaCesAclProfileConfigTableEntry.setIndexNames(
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclProfileId"),
)
if mibBuilder.loadTexts:
    cienaCesAclProfileConfigTableEntry.setStatus("current")


class _CienaCesAclProfileId_Type(Integer32):
    """Custom type cienaCesAclProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesAclProfileId_Type.__name__ = "Integer32"
_CienaCesAclProfileId_Object = MibTableColumn
cienaCesAclProfileId = _CienaCesAclProfileId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1, 1),
    _CienaCesAclProfileId_Type()
)
cienaCesAclProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesAclProfileId.setStatus("current")


class _CienaCesAclProfileName_Type(DisplayString):
    """Custom type cienaCesAclProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesAclProfileName_Type.__name__ = "DisplayString"
_CienaCesAclProfileName_Object = MibTableColumn
cienaCesAclProfileName = _CienaCesAclProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1, 2),
    _CienaCesAclProfileName_Type()
)
cienaCesAclProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclProfileName.setStatus("current")
_CienaCesAclProfileAdminState_Type = CienaGlobalState
_CienaCesAclProfileAdminState_Object = MibTableColumn
cienaCesAclProfileAdminState = _CienaCesAclProfileAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1, 3),
    _CienaCesAclProfileAdminState_Type()
)
cienaCesAclProfileAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclProfileAdminState.setStatus("current")
_CienaCesAclProfileOperState_Type = CienaGlobalState
_CienaCesAclProfileOperState_Object = MibTableColumn
cienaCesAclProfileOperState = _CienaCesAclProfileOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1, 4),
    _CienaCesAclProfileOperState_Type()
)
cienaCesAclProfileOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclProfileOperState.setStatus("current")
_CienaCesAclProfileDefaultFilterAction_Type = AclFilterAction
_CienaCesAclProfileDefaultFilterAction_Object = MibTableColumn
cienaCesAclProfileDefaultFilterAction = _CienaCesAclProfileDefaultFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1, 5),
    _CienaCesAclProfileDefaultFilterAction_Type()
)
cienaCesAclProfileDefaultFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclProfileDefaultFilterAction.setStatus("current")


class _CienaCesAclProfileNumRules_Type(Integer32):
    """Custom type cienaCesAclProfileNumRules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CienaCesAclProfileNumRules_Type.__name__ = "Integer32"
_CienaCesAclProfileNumRules_Object = MibTableColumn
cienaCesAclProfileNumRules = _CienaCesAclProfileNumRules_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1, 6),
    _CienaCesAclProfileNumRules_Type()
)
cienaCesAclProfileNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclProfileNumRules.setStatus("current")
_CienaCesAclProfileAttachedInterfaces_Type = Unsigned32
_CienaCesAclProfileAttachedInterfaces_Object = MibTableColumn
cienaCesAclProfileAttachedInterfaces = _CienaCesAclProfileAttachedInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 2, 1, 7),
    _CienaCesAclProfileAttachedInterfaces_Type()
)
cienaCesAclProfileAttachedInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclProfileAttachedInterfaces.setStatus("current")
_CienaCesAclRuleConfigTable_Object = MibTable
cienaCesAclRuleConfigTable = _CienaCesAclRuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cienaCesAclRuleConfigTable.setStatus("current")
_CienaCesAclRuleConfigTableEntry_Object = MibTableRow
cienaCesAclRuleConfigTableEntry = _CienaCesAclRuleConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1)
)
cienaCesAclRuleConfigTableEntry.setIndexNames(
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclProfileId"),
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclRulePrecedence"),
)
if mibBuilder.loadTexts:
    cienaCesAclRuleConfigTableEntry.setStatus("current")


class _CienaCesAclRulePrecedence_Type(Unsigned32):
    """Custom type cienaCesAclRulePrecedence based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CienaCesAclRulePrecedence_Type.__name__ = "Unsigned32"
_CienaCesAclRulePrecedence_Object = MibTableColumn
cienaCesAclRulePrecedence = _CienaCesAclRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 1),
    _CienaCesAclRulePrecedence_Type()
)
cienaCesAclRulePrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesAclRulePrecedence.setStatus("current")


class _CienaCesAclRuleName_Type(DisplayString):
    """Custom type cienaCesAclRuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesAclRuleName_Type.__name__ = "DisplayString"
_CienaCesAclRuleName_Object = MibTableColumn
cienaCesAclRuleName = _CienaCesAclRuleName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 2),
    _CienaCesAclRuleName_Type()
)
cienaCesAclRuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleName.setStatus("current")
_CienaCesAclRuleFilterAction_Type = AclFilterAction
_CienaCesAclRuleFilterAction_Object = MibTableColumn
cienaCesAclRuleFilterAction = _CienaCesAclRuleFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 3),
    _CienaCesAclRuleFilterAction_Type()
)
cienaCesAclRuleFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleFilterAction.setStatus("current")
_CienaCesAclRuleMatchAny_Type = TruthValue
_CienaCesAclRuleMatchAny_Object = MibTableColumn
cienaCesAclRuleMatchAny = _CienaCesAclRuleMatchAny_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 4),
    _CienaCesAclRuleMatchAny_Type()
)
cienaCesAclRuleMatchAny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchAny.setStatus("current")
_CienaCesAclRuleMatchSrcMacAddr_Type = TruthValue
_CienaCesAclRuleMatchSrcMacAddr_Object = MibTableColumn
cienaCesAclRuleMatchSrcMacAddr = _CienaCesAclRuleMatchSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 5),
    _CienaCesAclRuleMatchSrcMacAddr_Type()
)
cienaCesAclRuleMatchSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchSrcMacAddr.setStatus("current")
_CienaCesAclRuleSrcMacAddr_Type = MacAddress
_CienaCesAclRuleSrcMacAddr_Object = MibTableColumn
cienaCesAclRuleSrcMacAddr = _CienaCesAclRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 6),
    _CienaCesAclRuleSrcMacAddr_Type()
)
cienaCesAclRuleSrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleSrcMacAddr.setStatus("current")
_CienaCesAclRuleSrcMacAddrMask_Type = MacAddress
_CienaCesAclRuleSrcMacAddrMask_Object = MibTableColumn
cienaCesAclRuleSrcMacAddrMask = _CienaCesAclRuleSrcMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 7),
    _CienaCesAclRuleSrcMacAddrMask_Type()
)
cienaCesAclRuleSrcMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleSrcMacAddrMask.setStatus("current")
_CienaCesAclRuleMatchDstMacAddr_Type = TruthValue
_CienaCesAclRuleMatchDstMacAddr_Object = MibTableColumn
cienaCesAclRuleMatchDstMacAddr = _CienaCesAclRuleMatchDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 8),
    _CienaCesAclRuleMatchDstMacAddr_Type()
)
cienaCesAclRuleMatchDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchDstMacAddr.setStatus("current")
_CienaCesAclRuleDstMacAddr_Type = MacAddress
_CienaCesAclRuleDstMacAddr_Object = MibTableColumn
cienaCesAclRuleDstMacAddr = _CienaCesAclRuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 9),
    _CienaCesAclRuleDstMacAddr_Type()
)
cienaCesAclRuleDstMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleDstMacAddr.setStatus("current")
_CienaCesAclRuleDstMacAddrMask_Type = MacAddress
_CienaCesAclRuleDstMacAddrMask_Object = MibTableColumn
cienaCesAclRuleDstMacAddrMask = _CienaCesAclRuleDstMacAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 10),
    _CienaCesAclRuleDstMacAddrMask_Type()
)
cienaCesAclRuleDstMacAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleDstMacAddrMask.setStatus("current")
_CienaCesAclRuleMatchOuterVid_Type = TruthValue
_CienaCesAclRuleMatchOuterVid_Object = MibTableColumn
cienaCesAclRuleMatchOuterVid = _CienaCesAclRuleMatchOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 11),
    _CienaCesAclRuleMatchOuterVid_Type()
)
cienaCesAclRuleMatchOuterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchOuterVid.setStatus("current")
_CienaCesAclRuleOuterVid_Type = Unsigned32
_CienaCesAclRuleOuterVid_Object = MibTableColumn
cienaCesAclRuleOuterVid = _CienaCesAclRuleOuterVid_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 12),
    _CienaCesAclRuleOuterVid_Type()
)
cienaCesAclRuleOuterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleOuterVid.setStatus("current")
_CienaCesAclRuleOuterVidMask_Type = Unsigned32
_CienaCesAclRuleOuterVidMask_Object = MibTableColumn
cienaCesAclRuleOuterVidMask = _CienaCesAclRuleOuterVidMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 13),
    _CienaCesAclRuleOuterVidMask_Type()
)
cienaCesAclRuleOuterVidMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleOuterVidMask.setStatus("current")
_CienaCesAclRuleMatchOuterPcp_Type = TruthValue
_CienaCesAclRuleMatchOuterPcp_Object = MibTableColumn
cienaCesAclRuleMatchOuterPcp = _CienaCesAclRuleMatchOuterPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 14),
    _CienaCesAclRuleMatchOuterPcp_Type()
)
cienaCesAclRuleMatchOuterPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchOuterPcp.setStatus("current")


class _CienaCesAclRuleOuterPcp_Type(Unsigned32):
    """Custom type cienaCesAclRuleOuterPcp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesAclRuleOuterPcp_Type.__name__ = "Unsigned32"
_CienaCesAclRuleOuterPcp_Object = MibTableColumn
cienaCesAclRuleOuterPcp = _CienaCesAclRuleOuterPcp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 15),
    _CienaCesAclRuleOuterPcp_Type()
)
cienaCesAclRuleOuterPcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleOuterPcp.setStatus("current")


class _CienaCesAclRuleOuterPcpMask_Type(Unsigned32):
    """Custom type cienaCesAclRuleOuterPcpMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CienaCesAclRuleOuterPcpMask_Type.__name__ = "Unsigned32"
_CienaCesAclRuleOuterPcpMask_Object = MibTableColumn
cienaCesAclRuleOuterPcpMask = _CienaCesAclRuleOuterPcpMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 16),
    _CienaCesAclRuleOuterPcpMask_Type()
)
cienaCesAclRuleOuterPcpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleOuterPcpMask.setStatus("current")
_CienaCesAclRuleMatchOuterDei_Type = TruthValue
_CienaCesAclRuleMatchOuterDei_Object = MibTableColumn
cienaCesAclRuleMatchOuterDei = _CienaCesAclRuleMatchOuterDei_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 17),
    _CienaCesAclRuleMatchOuterDei_Type()
)
cienaCesAclRuleMatchOuterDei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchOuterDei.setStatus("current")


class _CienaCesAclRuleOuterDei_Type(Unsigned32):
    """Custom type cienaCesAclRuleOuterDei based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_CienaCesAclRuleOuterDei_Type.__name__ = "Unsigned32"
_CienaCesAclRuleOuterDei_Object = MibTableColumn
cienaCesAclRuleOuterDei = _CienaCesAclRuleOuterDei_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 18),
    _CienaCesAclRuleOuterDei_Type()
)
cienaCesAclRuleOuterDei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleOuterDei.setStatus("current")
_CienaCesAclRuleMatchBaseEtype_Type = TruthValue
_CienaCesAclRuleMatchBaseEtype_Object = MibTableColumn
cienaCesAclRuleMatchBaseEtype = _CienaCesAclRuleMatchBaseEtype_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 19),
    _CienaCesAclRuleMatchBaseEtype_Type()
)
cienaCesAclRuleMatchBaseEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchBaseEtype.setStatus("current")


class _CienaCesAclRuleBaseEtype_Type(Unsigned32):
    """Custom type cienaCesAclRuleBaseEtype based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CienaCesAclRuleBaseEtype_Type.__name__ = "Unsigned32"
_CienaCesAclRuleBaseEtype_Object = MibTableColumn
cienaCesAclRuleBaseEtype = _CienaCesAclRuleBaseEtype_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 20),
    _CienaCesAclRuleBaseEtype_Type()
)
cienaCesAclRuleBaseEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleBaseEtype.setStatus("current")
_CienaCesAclRuleMatchSrcIpAddr_Type = TruthValue
_CienaCesAclRuleMatchSrcIpAddr_Object = MibTableColumn
cienaCesAclRuleMatchSrcIpAddr = _CienaCesAclRuleMatchSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 21),
    _CienaCesAclRuleMatchSrcIpAddr_Type()
)
cienaCesAclRuleMatchSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchSrcIpAddr.setStatus("current")
_CienaCesAclRuleSrcIpAddrType_Type = InetAddressType
_CienaCesAclRuleSrcIpAddrType_Object = MibTableColumn
cienaCesAclRuleSrcIpAddrType = _CienaCesAclRuleSrcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 22),
    _CienaCesAclRuleSrcIpAddrType_Type()
)
cienaCesAclRuleSrcIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleSrcIpAddrType.setStatus("current")
_CienaCesAclRuleSrcIpAddr_Type = InetAddress
_CienaCesAclRuleSrcIpAddr_Object = MibTableColumn
cienaCesAclRuleSrcIpAddr = _CienaCesAclRuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 23),
    _CienaCesAclRuleSrcIpAddr_Type()
)
cienaCesAclRuleSrcIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleSrcIpAddr.setStatus("current")
_CienaCesAclRuleSrcIpAddrPrefixLength_Type = InetAddressPrefixLength
_CienaCesAclRuleSrcIpAddrPrefixLength_Object = MibTableColumn
cienaCesAclRuleSrcIpAddrPrefixLength = _CienaCesAclRuleSrcIpAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 24),
    _CienaCesAclRuleSrcIpAddrPrefixLength_Type()
)
cienaCesAclRuleSrcIpAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleSrcIpAddrPrefixLength.setStatus("current")
_CienaCesAclRuleMatchDstIpAddr_Type = TruthValue
_CienaCesAclRuleMatchDstIpAddr_Object = MibTableColumn
cienaCesAclRuleMatchDstIpAddr = _CienaCesAclRuleMatchDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 25),
    _CienaCesAclRuleMatchDstIpAddr_Type()
)
cienaCesAclRuleMatchDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchDstIpAddr.setStatus("current")
_CienaCesAclRuleDstIpAddrType_Type = InetAddressType
_CienaCesAclRuleDstIpAddrType_Object = MibTableColumn
cienaCesAclRuleDstIpAddrType = _CienaCesAclRuleDstIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 26),
    _CienaCesAclRuleDstIpAddrType_Type()
)
cienaCesAclRuleDstIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleDstIpAddrType.setStatus("current")
_CienaCesAclRuleDstIpAddr_Type = InetAddress
_CienaCesAclRuleDstIpAddr_Object = MibTableColumn
cienaCesAclRuleDstIpAddr = _CienaCesAclRuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 27),
    _CienaCesAclRuleDstIpAddr_Type()
)
cienaCesAclRuleDstIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleDstIpAddr.setStatus("current")
_CienaCesAclRuleDstIpAddrPrefixLength_Type = InetAddressPrefixLength
_CienaCesAclRuleDstIpAddrPrefixLength_Object = MibTableColumn
cienaCesAclRuleDstIpAddrPrefixLength = _CienaCesAclRuleDstIpAddrPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 28),
    _CienaCesAclRuleDstIpAddrPrefixLength_Type()
)
cienaCesAclRuleDstIpAddrPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleDstIpAddrPrefixLength.setStatus("current")
_CienaCesAclRuleMatchIpProtocol_Type = TruthValue
_CienaCesAclRuleMatchIpProtocol_Object = MibTableColumn
cienaCesAclRuleMatchIpProtocol = _CienaCesAclRuleMatchIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 29),
    _CienaCesAclRuleMatchIpProtocol_Type()
)
cienaCesAclRuleMatchIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchIpProtocol.setStatus("current")


class _CienaCesAclRuleIpProtocol_Type(Unsigned32):
    """Custom type cienaCesAclRuleIpProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CienaCesAclRuleIpProtocol_Type.__name__ = "Unsigned32"
_CienaCesAclRuleIpProtocol_Object = MibTableColumn
cienaCesAclRuleIpProtocol = _CienaCesAclRuleIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 30),
    _CienaCesAclRuleIpProtocol_Type()
)
cienaCesAclRuleIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleIpProtocol.setStatus("current")
_CienaCesAclRuleMatchDscp_Type = TruthValue
_CienaCesAclRuleMatchDscp_Object = MibTableColumn
cienaCesAclRuleMatchDscp = _CienaCesAclRuleMatchDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 31),
    _CienaCesAclRuleMatchDscp_Type()
)
cienaCesAclRuleMatchDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchDscp.setStatus("current")


class _CienaCesAclRuleDscp_Type(Unsigned32):
    """Custom type cienaCesAclRuleDscp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CienaCesAclRuleDscp_Type.__name__ = "Unsigned32"
_CienaCesAclRuleDscp_Object = MibTableColumn
cienaCesAclRuleDscp = _CienaCesAclRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 32),
    _CienaCesAclRuleDscp_Type()
)
cienaCesAclRuleDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleDscp.setStatus("current")


class _CienaCesAclRuleDscpMask_Type(Unsigned32):
    """Custom type cienaCesAclRuleDscpMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_CienaCesAclRuleDscpMask_Type.__name__ = "Unsigned32"
_CienaCesAclRuleDscpMask_Object = MibTableColumn
cienaCesAclRuleDscpMask = _CienaCesAclRuleDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 33),
    _CienaCesAclRuleDscpMask_Type()
)
cienaCesAclRuleDscpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleDscpMask.setStatus("current")
_CienaCesAclRuleMatchL4SrcPort_Type = AclL4PortMatchType
_CienaCesAclRuleMatchL4SrcPort_Object = MibTableColumn
cienaCesAclRuleMatchL4SrcPort = _CienaCesAclRuleMatchL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 34),
    _CienaCesAclRuleMatchL4SrcPort_Type()
)
cienaCesAclRuleMatchL4SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchL4SrcPort.setStatus("current")
_CienaCesAclRuleL4SrcPort_Type = InetPortNumber
_CienaCesAclRuleL4SrcPort_Object = MibTableColumn
cienaCesAclRuleL4SrcPort = _CienaCesAclRuleL4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 35),
    _CienaCesAclRuleL4SrcPort_Type()
)
cienaCesAclRuleL4SrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleL4SrcPort.setStatus("current")
_CienaCesAclRuleL4SrcPortUpper_Type = InetPortNumber
_CienaCesAclRuleL4SrcPortUpper_Object = MibTableColumn
cienaCesAclRuleL4SrcPortUpper = _CienaCesAclRuleL4SrcPortUpper_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 36),
    _CienaCesAclRuleL4SrcPortUpper_Type()
)
cienaCesAclRuleL4SrcPortUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleL4SrcPortUpper.setStatus("current")
_CienaCesAclRuleMatchL4DstPort_Type = AclL4PortMatchType
_CienaCesAclRuleMatchL4DstPort_Object = MibTableColumn
cienaCesAclRuleMatchL4DstPort = _CienaCesAclRuleMatchL4DstPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 37),
    _CienaCesAclRuleMatchL4DstPort_Type()
)
cienaCesAclRuleMatchL4DstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchL4DstPort.setStatus("current")
_CienaCesAclRuleL4DstPort_Type = InetPortNumber
_CienaCesAclRuleL4DstPort_Object = MibTableColumn
cienaCesAclRuleL4DstPort = _CienaCesAclRuleL4DstPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 38),
    _CienaCesAclRuleL4DstPort_Type()
)
cienaCesAclRuleL4DstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleL4DstPort.setStatus("current")
_CienaCesAclRuleL4DstPortUpper_Type = InetPortNumber
_CienaCesAclRuleL4DstPortUpper_Object = MibTableColumn
cienaCesAclRuleL4DstPortUpper = _CienaCesAclRuleL4DstPortUpper_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 39),
    _CienaCesAclRuleL4DstPortUpper_Type()
)
cienaCesAclRuleL4DstPortUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleL4DstPortUpper.setStatus("current")
_CienaCesAclRuleMatchL4DstProtocol_Type = AclL4DstProtocol
_CienaCesAclRuleMatchL4DstProtocol_Object = MibTableColumn
cienaCesAclRuleMatchL4DstProtocol = _CienaCesAclRuleMatchL4DstProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 40),
    _CienaCesAclRuleMatchL4DstProtocol_Type()
)
cienaCesAclRuleMatchL4DstProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchL4DstProtocol.setStatus("current")
_CienaCesAclRuleMatchIpFragment_Type = AclIpFragmentMatchType
_CienaCesAclRuleMatchIpFragment_Object = MibTableColumn
cienaCesAclRuleMatchIpFragment = _CienaCesAclRuleMatchIpFragment_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 41),
    _CienaCesAclRuleMatchIpFragment_Type()
)
cienaCesAclRuleMatchIpFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchIpFragment.setStatus("current")
_CienaCesAclRuleMatchTcpFlags_Type = TruthValue
_CienaCesAclRuleMatchTcpFlags_Object = MibTableColumn
cienaCesAclRuleMatchTcpFlags = _CienaCesAclRuleMatchTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 42),
    _CienaCesAclRuleMatchTcpFlags_Type()
)
cienaCesAclRuleMatchTcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleMatchTcpFlags.setStatus("current")
_CienaCesAclRuleTcpFlags_Type = DisplayString
_CienaCesAclRuleTcpFlags_Object = MibTableColumn
cienaCesAclRuleTcpFlags = _CienaCesAclRuleTcpFlags_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 3, 1, 43),
    _CienaCesAclRuleTcpFlags_Type()
)
cienaCesAclRuleTcpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleTcpFlags.setStatus("current")
_CienaCesAclProfileAttachmentTable_Object = MibTable
cienaCesAclProfileAttachmentTable = _CienaCesAclProfileAttachmentTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cienaCesAclProfileAttachmentTable.setStatus("current")
_CienaCesAclProfileAttachmentTableEntry_Object = MibTableRow
cienaCesAclProfileAttachmentTableEntry = _CienaCesAclProfileAttachmentTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 4, 1)
)
cienaCesAclProfileAttachmentTableEntry.setIndexNames(
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclProfileId"),
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclInterfaceType"),
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclInterfaceId"),
)
if mibBuilder.loadTexts:
    cienaCesAclProfileAttachmentTableEntry.setStatus("current")
_CienaCesAclInterfaceType_Type = AclInterfaceType
_CienaCesAclInterfaceType_Object = MibTableColumn
cienaCesAclInterfaceType = _CienaCesAclInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 4, 1, 1),
    _CienaCesAclInterfaceType_Type()
)
cienaCesAclInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesAclInterfaceType.setStatus("current")


class _CienaCesAclInterfaceId_Type(Integer32):
    """Custom type cienaCesAclInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1048576),
    )


_CienaCesAclInterfaceId_Type.__name__ = "Integer32"
_CienaCesAclInterfaceId_Object = MibTableColumn
cienaCesAclInterfaceId = _CienaCesAclInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 4, 1, 2),
    _CienaCesAclInterfaceId_Type()
)
cienaCesAclInterfaceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesAclInterfaceId.setStatus("current")


class _CienaCesAclInterfaceName_Type(DisplayString):
    """Custom type cienaCesAclInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_CienaCesAclInterfaceName_Type.__name__ = "DisplayString"
_CienaCesAclInterfaceName_Object = MibTableColumn
cienaCesAclInterfaceName = _CienaCesAclInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 4, 1, 3),
    _CienaCesAclInterfaceName_Type()
)
cienaCesAclInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclInterfaceName.setStatus("current")
_CienaCesAclDirection_Type = AclTrafficDirection
_CienaCesAclDirection_Object = MibTableColumn
cienaCesAclDirection = _CienaCesAclDirection_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 1, 4, 1, 4),
    _CienaCesAclDirection_Type()
)
cienaCesAclDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclDirection.setStatus("current")
_CienaCesAclStatistics_ObjectIdentity = ObjectIdentity
cienaCesAclStatistics = _CienaCesAclStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2)
)
_CienaCesAclProfileGlobalRuleStatsTable_Object = MibTable
cienaCesAclProfileGlobalRuleStatsTable = _CienaCesAclProfileGlobalRuleStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesAclProfileGlobalRuleStatsTable.setStatus("current")
_CienaCesAclProfileGlobalRuleStatsTableEntry_Object = MibTableRow
cienaCesAclProfileGlobalRuleStatsTableEntry = _CienaCesAclProfileGlobalRuleStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 1, 1)
)
cienaCesAclProfileGlobalRuleStatsTableEntry.setIndexNames(
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclProfileId"),
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclRulePrecedence"),
)
if mibBuilder.loadTexts:
    cienaCesAclProfileGlobalRuleStatsTableEntry.setStatus("current")
_CienaCesAclGlobalRuleStatsPacketCount_Type = Counter64
_CienaCesAclGlobalRuleStatsPacketCount_Object = MibTableColumn
cienaCesAclGlobalRuleStatsPacketCount = _CienaCesAclGlobalRuleStatsPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 1, 1, 1),
    _CienaCesAclGlobalRuleStatsPacketCount_Type()
)
cienaCesAclGlobalRuleStatsPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclGlobalRuleStatsPacketCount.setStatus("current")
_CienaCesAclGlobalRuleStatsByteCount_Type = Counter64
_CienaCesAclGlobalRuleStatsByteCount_Object = MibTableColumn
cienaCesAclGlobalRuleStatsByteCount = _CienaCesAclGlobalRuleStatsByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 1, 1, 2),
    _CienaCesAclGlobalRuleStatsByteCount_Type()
)
cienaCesAclGlobalRuleStatsByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclGlobalRuleStatsByteCount.setStatus("current")
_CienaCesAclProfileRuleInstanceStatsTable_Object = MibTable
cienaCesAclProfileRuleInstanceStatsTable = _CienaCesAclProfileRuleInstanceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesAclProfileRuleInstanceStatsTable.setStatus("current")
_CienaCesAclProfileRuleInstanceStatsTableEntry_Object = MibTableRow
cienaCesAclProfileRuleInstanceStatsTableEntry = _CienaCesAclProfileRuleInstanceStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 2, 1)
)
cienaCesAclProfileRuleInstanceStatsTableEntry.setIndexNames(
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclProfileId"),
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclInterfaceType"),
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclInterfaceId"),
    (0, "CIENA-CES-ACCESS-LIST-MIB", "cienaCesAclRulePrecedence"),
)
if mibBuilder.loadTexts:
    cienaCesAclProfileRuleInstanceStatsTableEntry.setStatus("current")
_CienaCesAclRuleInstanceStatsPacketCount_Type = Counter64
_CienaCesAclRuleInstanceStatsPacketCount_Object = MibTableColumn
cienaCesAclRuleInstanceStatsPacketCount = _CienaCesAclRuleInstanceStatsPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 2, 1, 1),
    _CienaCesAclRuleInstanceStatsPacketCount_Type()
)
cienaCesAclRuleInstanceStatsPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleInstanceStatsPacketCount.setStatus("current")
_CienaCesAclRuleInstanceStatsByteCount_Type = Counter64
_CienaCesAclRuleInstanceStatsByteCount_Object = MibTableColumn
cienaCesAclRuleInstanceStatsByteCount = _CienaCesAclRuleInstanceStatsByteCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 1, 2, 2, 1, 2),
    _CienaCesAclRuleInstanceStatsByteCount_Type()
)
cienaCesAclRuleInstanceStatsByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesAclRuleInstanceStatsByteCount.setStatus("current")
_CienaCesAccessListMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesAccessListMIBConformance = _CienaCesAccessListMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 2)
)
_CienaCesAccessListMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesAccessListMIBCompliances = _CienaCesAccessListMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 2, 1)
)
_CienaCesAccessListMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesAccessListMIBGroups = _CienaCesAccessListMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 35, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-ACCESS-LIST-MIB",
    **{"AclFilterAction": AclFilterAction,
       "AclTrafficDirection": AclTrafficDirection,
       "AclIpFragmentMatchType": AclIpFragmentMatchType,
       "AclL4PortMatchType": AclL4PortMatchType,
       "AclInterfaceType": AclInterfaceType,
       "AclL4DstProtocol": AclL4DstProtocol,
       "cienaCesAccessListMIB": cienaCesAccessListMIB,
       "cienaCesAccessListMIBObjects": cienaCesAccessListMIBObjects,
       "cienaCesAclConfiguration": cienaCesAclConfiguration,
       "cienaCesAclGlobalConfig": cienaCesAclGlobalConfig,
       "cienaCesAclAdminStatus": cienaCesAclAdminStatus,
       "cienaCesAclFilterMode": cienaCesAclFilterMode,
       "cienaCesAclNumAclProfileDefs": cienaCesAclNumAclProfileDefs,
       "cienaCesAclRemainingAclProfileDefs": cienaCesAclRemainingAclProfileDefs,
       "cienaCesAclNumAclRuleDefs": cienaCesAclNumAclRuleDefs,
       "cienaCesAclRemainingAclRuleDefs": cienaCesAclRemainingAclRuleDefs,
       "cienaCesAclProfileConfigTable": cienaCesAclProfileConfigTable,
       "cienaCesAclProfileConfigTableEntry": cienaCesAclProfileConfigTableEntry,
       "cienaCesAclProfileId": cienaCesAclProfileId,
       "cienaCesAclProfileName": cienaCesAclProfileName,
       "cienaCesAclProfileAdminState": cienaCesAclProfileAdminState,
       "cienaCesAclProfileOperState": cienaCesAclProfileOperState,
       "cienaCesAclProfileDefaultFilterAction": cienaCesAclProfileDefaultFilterAction,
       "cienaCesAclProfileNumRules": cienaCesAclProfileNumRules,
       "cienaCesAclProfileAttachedInterfaces": cienaCesAclProfileAttachedInterfaces,
       "cienaCesAclRuleConfigTable": cienaCesAclRuleConfigTable,
       "cienaCesAclRuleConfigTableEntry": cienaCesAclRuleConfigTableEntry,
       "cienaCesAclRulePrecedence": cienaCesAclRulePrecedence,
       "cienaCesAclRuleName": cienaCesAclRuleName,
       "cienaCesAclRuleFilterAction": cienaCesAclRuleFilterAction,
       "cienaCesAclRuleMatchAny": cienaCesAclRuleMatchAny,
       "cienaCesAclRuleMatchSrcMacAddr": cienaCesAclRuleMatchSrcMacAddr,
       "cienaCesAclRuleSrcMacAddr": cienaCesAclRuleSrcMacAddr,
       "cienaCesAclRuleSrcMacAddrMask": cienaCesAclRuleSrcMacAddrMask,
       "cienaCesAclRuleMatchDstMacAddr": cienaCesAclRuleMatchDstMacAddr,
       "cienaCesAclRuleDstMacAddr": cienaCesAclRuleDstMacAddr,
       "cienaCesAclRuleDstMacAddrMask": cienaCesAclRuleDstMacAddrMask,
       "cienaCesAclRuleMatchOuterVid": cienaCesAclRuleMatchOuterVid,
       "cienaCesAclRuleOuterVid": cienaCesAclRuleOuterVid,
       "cienaCesAclRuleOuterVidMask": cienaCesAclRuleOuterVidMask,
       "cienaCesAclRuleMatchOuterPcp": cienaCesAclRuleMatchOuterPcp,
       "cienaCesAclRuleOuterPcp": cienaCesAclRuleOuterPcp,
       "cienaCesAclRuleOuterPcpMask": cienaCesAclRuleOuterPcpMask,
       "cienaCesAclRuleMatchOuterDei": cienaCesAclRuleMatchOuterDei,
       "cienaCesAclRuleOuterDei": cienaCesAclRuleOuterDei,
       "cienaCesAclRuleMatchBaseEtype": cienaCesAclRuleMatchBaseEtype,
       "cienaCesAclRuleBaseEtype": cienaCesAclRuleBaseEtype,
       "cienaCesAclRuleMatchSrcIpAddr": cienaCesAclRuleMatchSrcIpAddr,
       "cienaCesAclRuleSrcIpAddrType": cienaCesAclRuleSrcIpAddrType,
       "cienaCesAclRuleSrcIpAddr": cienaCesAclRuleSrcIpAddr,
       "cienaCesAclRuleSrcIpAddrPrefixLength": cienaCesAclRuleSrcIpAddrPrefixLength,
       "cienaCesAclRuleMatchDstIpAddr": cienaCesAclRuleMatchDstIpAddr,
       "cienaCesAclRuleDstIpAddrType": cienaCesAclRuleDstIpAddrType,
       "cienaCesAclRuleDstIpAddr": cienaCesAclRuleDstIpAddr,
       "cienaCesAclRuleDstIpAddrPrefixLength": cienaCesAclRuleDstIpAddrPrefixLength,
       "cienaCesAclRuleMatchIpProtocol": cienaCesAclRuleMatchIpProtocol,
       "cienaCesAclRuleIpProtocol": cienaCesAclRuleIpProtocol,
       "cienaCesAclRuleMatchDscp": cienaCesAclRuleMatchDscp,
       "cienaCesAclRuleDscp": cienaCesAclRuleDscp,
       "cienaCesAclRuleDscpMask": cienaCesAclRuleDscpMask,
       "cienaCesAclRuleMatchL4SrcPort": cienaCesAclRuleMatchL4SrcPort,
       "cienaCesAclRuleL4SrcPort": cienaCesAclRuleL4SrcPort,
       "cienaCesAclRuleL4SrcPortUpper": cienaCesAclRuleL4SrcPortUpper,
       "cienaCesAclRuleMatchL4DstPort": cienaCesAclRuleMatchL4DstPort,
       "cienaCesAclRuleL4DstPort": cienaCesAclRuleL4DstPort,
       "cienaCesAclRuleL4DstPortUpper": cienaCesAclRuleL4DstPortUpper,
       "cienaCesAclRuleMatchL4DstProtocol": cienaCesAclRuleMatchL4DstProtocol,
       "cienaCesAclRuleMatchIpFragment": cienaCesAclRuleMatchIpFragment,
       "cienaCesAclRuleMatchTcpFlags": cienaCesAclRuleMatchTcpFlags,
       "cienaCesAclRuleTcpFlags": cienaCesAclRuleTcpFlags,
       "cienaCesAclProfileAttachmentTable": cienaCesAclProfileAttachmentTable,
       "cienaCesAclProfileAttachmentTableEntry": cienaCesAclProfileAttachmentTableEntry,
       "cienaCesAclInterfaceType": cienaCesAclInterfaceType,
       "cienaCesAclInterfaceId": cienaCesAclInterfaceId,
       "cienaCesAclInterfaceName": cienaCesAclInterfaceName,
       "cienaCesAclDirection": cienaCesAclDirection,
       "cienaCesAclStatistics": cienaCesAclStatistics,
       "cienaCesAclProfileGlobalRuleStatsTable": cienaCesAclProfileGlobalRuleStatsTable,
       "cienaCesAclProfileGlobalRuleStatsTableEntry": cienaCesAclProfileGlobalRuleStatsTableEntry,
       "cienaCesAclGlobalRuleStatsPacketCount": cienaCesAclGlobalRuleStatsPacketCount,
       "cienaCesAclGlobalRuleStatsByteCount": cienaCesAclGlobalRuleStatsByteCount,
       "cienaCesAclProfileRuleInstanceStatsTable": cienaCesAclProfileRuleInstanceStatsTable,
       "cienaCesAclProfileRuleInstanceStatsTableEntry": cienaCesAclProfileRuleInstanceStatsTableEntry,
       "cienaCesAclRuleInstanceStatsPacketCount": cienaCesAclRuleInstanceStatsPacketCount,
       "cienaCesAclRuleInstanceStatsByteCount": cienaCesAclRuleInstanceStatsByteCount,
       "cienaCesAccessListMIBConformance": cienaCesAccessListMIBConformance,
       "cienaCesAccessListMIBCompliances": cienaCesAccessListMIBCompliances,
       "cienaCesAccessListMIBGroups": cienaCesAccessListMIBGroups}
)
