# SNMP MIB module (HP-ICF-GPPCV2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-GPPCV2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:30 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfGppcv2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61)
)
hpicfGppcv2MIB.setRevisions(
        ("2016-01-15 00:00",
         "2015-06-23 00:00",
         "2015-01-21 00:00",
         "2014-09-09 00:00",
         "2014-04-24 00:00",
         "2010-11-12 00:00",
         "2010-09-28 00:00",
         "2010-03-01 22:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpicfGppcv2PolicyName(OctetString, TextualConvention):
    status = "current"
    displayHint = "70a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 70),
    )



class HpicfGppcv2PolicyType(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aclIpv4", 1),
          ("aclIpv6", 2),
          ("aclMac", 7),
          ("classifierClassIpv4", 3),
          ("classifierClassIpv6", 4),
          ("classifierClassMac", 8),
          ("classifierPolicy", 5),
          ("connectionRateFilterIpv4", 6))
    )



class HpicfGppcv2LastErrorCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              50,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111)
        )
    )
    namedValues = NamedValues(
        *(("gppcv2AceCfgLimitReachedError", 74),
          ("gppcv2AceConflictingRuleError", 71),
          ("gppcv2AceCreateError", 70),
          ("gppcv2AceDuplicateError", 72),
          ("gppcv2AceDuplicateSequenceNumError", 73),
          ("gppcv2AceNotFoundError", 75),
          ("gppcv2AclApplyError", 79),
          ("gppcv2AclCfgLimitReachedError", 81),
          ("gppcv2AclCreateError", 80),
          ("gppcv2AclDuplcateNameError", 76),
          ("gppcv2AclMaxSequenceNumError", 77),
          ("gppcv2AclMgmtVlanConflictError", 78),
          ("gppcv2AclNotAppliedPortError", 84),
          ("gppcv2AclNotAppliedVlanError", 83),
          ("gppcv2AclNotFoundError", 82),
          ("gppcv2AclResequenceLimitError", 86),
          ("gppcv2AlreadyReserved", 9),
          ("gppcv2AppUsingPolicy", 12),
          ("gppcv2CfgError", 50),
          ("gppcv2ClassConflictingRuleError", 95),
          ("gppcv2ClassCreateError", 89),
          ("gppcv2ClassDuplicateNameError", 92),
          ("gppcv2ClassEntryAddError", 93),
          ("gppcv2ClassEntryCfgLimitReachedError", 90),
          ("gppcv2ClassEntryNotFoundError", 94),
          ("gppcv2ClassListCfgLimitReachedError", 91),
          ("gppcv2ClassMaxSequenceNumError", 87),
          ("gppcv2ClassNoMixMacAndIPError", 110),
          ("gppcv2ClassNotFoundError", 88),
          ("gppcv2EntryExists", 10),
          ("gppcv2GenericError", 1),
          ("gppcv2InvalidEtherTypeError", 111),
          ("gppcv2InvalidPolicyType", 13),
          ("gppcv2InvalidTypeForCrfError", 85),
          ("gppcv2LengthError", 2),
          ("gppcv2MallocError", 6),
          ("gppcv2NameError", 3),
          ("gppcv2NoPolicy", 15),
          ("gppcv2NotImplemented", 5),
          ("gppcv2NotReserved", 14),
          ("gppcv2ParameterError", 4),
          ("gppcv2PlatformError", 11),
          ("gppcv2PolicyAddClassError", 100),
          ("gppcv2PolicyApplyDetailedError", 109),
          ("gppcv2PolicyApplyError", 104),
          ("gppcv2PolicyCfgLimitReachedError", 108),
          ("gppcv2PolicyClassNotFoundError", 102),
          ("gppcv2PolicyClassifiedVlanOnVlanError", 107),
          ("gppcv2PolicyCreateError", 99),
          ("gppcv2PolicyDeleteClassError", 101),
          ("gppcv2PolicyDeleteError", 103),
          ("gppcv2PolicyDuplicateClassError", 106),
          ("gppcv2PolicyHasRules", 17),
          ("gppcv2PolicyIsAppliedCannotDeleteError", 105),
          ("gppcv2PolicyNameConflictError", 97),
          ("gppcv2PolicyNotActive", 16),
          ("gppcv2PolicyNotAppliedError", 98),
          ("gppcv2PolicyNotFoundError", 96),
          ("gppcv2ReleaseAppCtrlEntry", 20),
          ("gppcv2ReleaseRules", 19),
          ("gppcv2RuleExists", 18),
          ("gppcv2TooManyApps", 7),
          ("gppcv2TooManyPolicies", 8),
          ("noError", 0))
    )



# MIB Managed Objects in the order of their OIDs

_HpicfGppcv2Conformance_ObjectIdentity = ObjectIdentity
hpicfGppcv2Conformance = _HpicfGppcv2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 1)
)
_HpicfGppcv2MIBCompliances_ObjectIdentity = ObjectIdentity
hpicfGppcv2MIBCompliances = _HpicfGppcv2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 1, 1)
)
_HpicfGppcv2MIBGroups_ObjectIdentity = ObjectIdentity
hpicfGppcv2MIBGroups = _HpicfGppcv2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 1, 2)
)
_HpicfGppcv2AppControlTable_Object = MibTable
hpicfGppcv2AppControlTable = _HpicfGppcv2AppControlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2)
)
if mibBuilder.loadTexts:
    hpicfGppcv2AppControlTable.setStatus("current")
_HpicfGppcv2AppControlEntry_Object = MibTableRow
hpicfGppcv2AppControlEntry = _HpicfGppcv2AppControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1)
)
hpicfGppcv2AppControlEntry.setIndexNames(
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcAppName"),
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcAppInstance"),
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcPolicyType"),
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcPolicyName"),
)
if mibBuilder.loadTexts:
    hpicfGppcv2AppControlEntry.setStatus("current")


class _HpicfGppcv2AcAppName_Type(SnmpAdminString):
    """Custom type hpicfGppcv2AcAppName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpicfGppcv2AcAppName_Type.__name__ = "SnmpAdminString"
_HpicfGppcv2AcAppName_Object = MibTableColumn
hpicfGppcv2AcAppName = _HpicfGppcv2AcAppName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 1),
    _HpicfGppcv2AcAppName_Type()
)
hpicfGppcv2AcAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcv2AcAppName.setStatus("current")


class _HpicfGppcv2AcAppInstance_Type(SnmpAdminString):
    """Custom type hpicfGppcv2AcAppInstance based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_HpicfGppcv2AcAppInstance_Type.__name__ = "SnmpAdminString"
_HpicfGppcv2AcAppInstance_Object = MibTableColumn
hpicfGppcv2AcAppInstance = _HpicfGppcv2AcAppInstance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 2),
    _HpicfGppcv2AcAppInstance_Type()
)
hpicfGppcv2AcAppInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcv2AcAppInstance.setStatus("current")
_HpicfGppcv2AcPolicyType_Type = HpicfGppcv2PolicyType
_HpicfGppcv2AcPolicyType_Object = MibTableColumn
hpicfGppcv2AcPolicyType = _HpicfGppcv2AcPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 3),
    _HpicfGppcv2AcPolicyType_Type()
)
hpicfGppcv2AcPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcv2AcPolicyType.setStatus("current")
_HpicfGppcv2AcPolicyName_Type = HpicfGppcv2PolicyName
_HpicfGppcv2AcPolicyName_Object = MibTableColumn
hpicfGppcv2AcPolicyName = _HpicfGppcv2AcPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 4),
    _HpicfGppcv2AcPolicyName_Type()
)
hpicfGppcv2AcPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcv2AcPolicyName.setStatus("current")
_HpicfGppcv2AcIngressIfList_Type = PortList
_HpicfGppcv2AcIngressIfList_Object = MibTableColumn
hpicfGppcv2AcIngressIfList = _HpicfGppcv2AcIngressIfList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 5),
    _HpicfGppcv2AcIngressIfList_Type()
)
hpicfGppcv2AcIngressIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcIngressIfList.setStatus("current")


class _HpicfGppcv2AcIngressVIDList_Type(OctetString):
    """Custom type hpicfGppcv2AcIngressVIDList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpicfGppcv2AcIngressVIDList_Type.__name__ = "OctetString"
_HpicfGppcv2AcIngressVIDList_Object = MibTableColumn
hpicfGppcv2AcIngressVIDList = _HpicfGppcv2AcIngressVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 6),
    _HpicfGppcv2AcIngressVIDList_Type()
)
hpicfGppcv2AcIngressVIDList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcIngressVIDList.setStatus("current")
_HpicfGppcv2AcEgressIfList_Type = PortList
_HpicfGppcv2AcEgressIfList_Object = MibTableColumn
hpicfGppcv2AcEgressIfList = _HpicfGppcv2AcEgressIfList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 7),
    _HpicfGppcv2AcEgressIfList_Type()
)
hpicfGppcv2AcEgressIfList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcEgressIfList.setStatus("current")


class _HpicfGppcv2AcEgressVIDList_Type(OctetString):
    """Custom type hpicfGppcv2AcEgressVIDList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpicfGppcv2AcEgressVIDList_Type.__name__ = "OctetString"
_HpicfGppcv2AcEgressVIDList_Object = MibTableColumn
hpicfGppcv2AcEgressVIDList = _HpicfGppcv2AcEgressVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 8),
    _HpicfGppcv2AcEgressVIDList_Type()
)
hpicfGppcv2AcEgressVIDList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcEgressVIDList.setStatus("current")


class _HpicfGppcv2AcVIDList_Type(OctetString):
    """Custom type hpicfGppcv2AcVIDList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpicfGppcv2AcVIDList_Type.__name__ = "OctetString"
_HpicfGppcv2AcVIDList_Object = MibTableColumn
hpicfGppcv2AcVIDList = _HpicfGppcv2AcVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 9),
    _HpicfGppcv2AcVIDList_Type()
)
hpicfGppcv2AcVIDList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcVIDList.setStatus("current")


class _HpicfGppcv2AcExpPolicy_Type(Integer32):
    """Custom type hpicfGppcv2AcExpPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("permanent", 1)
    )


_HpicfGppcv2AcExpPolicy_Type.__name__ = "Integer32"
_HpicfGppcv2AcExpPolicy_Object = MibTableColumn
hpicfGppcv2AcExpPolicy = _HpicfGppcv2AcExpPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 10),
    _HpicfGppcv2AcExpPolicy_Type()
)
hpicfGppcv2AcExpPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcExpPolicy.setStatus("current")


class _HpicfGppcv2AcExpString_Type(OctetString):
    """Custom type hpicfGppcv2AcExpString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_HpicfGppcv2AcExpString_Type.__name__ = "OctetString"
_HpicfGppcv2AcExpString_Object = MibTableColumn
hpicfGppcv2AcExpString = _HpicfGppcv2AcExpString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 11),
    _HpicfGppcv2AcExpString_Type()
)
hpicfGppcv2AcExpString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcExpString.setStatus("current")
_HpicfGppcv2AcLastErrorCode_Type = HpicfGppcv2LastErrorCode
_HpicfGppcv2AcLastErrorCode_Object = MibTableColumn
hpicfGppcv2AcLastErrorCode = _HpicfGppcv2AcLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 12),
    _HpicfGppcv2AcLastErrorCode_Type()
)
hpicfGppcv2AcLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGppcv2AcLastErrorCode.setStatus("current")


class _HpicfGppcv2AcLastErrorString_Type(SnmpAdminString):
    """Custom type hpicfGppcv2AcLastErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfGppcv2AcLastErrorString_Type.__name__ = "SnmpAdminString"
_HpicfGppcv2AcLastErrorString_Object = MibTableColumn
hpicfGppcv2AcLastErrorString = _HpicfGppcv2AcLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 13),
    _HpicfGppcv2AcLastErrorString_Type()
)
hpicfGppcv2AcLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGppcv2AcLastErrorString.setStatus("current")


class _HpicfGppcv2AcRowAdminStatus_Type(Integer32):
    """Custom type hpicfGppcv2AcRowAdminStatus based on Integer32"""
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


_HpicfGppcv2AcRowAdminStatus_Type.__name__ = "Integer32"
_HpicfGppcv2AcRowAdminStatus_Object = MibTableColumn
hpicfGppcv2AcRowAdminStatus = _HpicfGppcv2AcRowAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 14),
    _HpicfGppcv2AcRowAdminStatus_Type()
)
hpicfGppcv2AcRowAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcRowAdminStatus.setStatus("current")
_HpicfGppcv2AcRowStatus_Type = RowStatus
_HpicfGppcv2AcRowStatus_Object = MibTableColumn
hpicfGppcv2AcRowStatus = _HpicfGppcv2AcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 15),
    _HpicfGppcv2AcRowStatus_Type()
)
hpicfGppcv2AcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcRowStatus.setStatus("current")


class _HpicfGppcv2AcIngressTunnelList_Type(OctetString):
    """Custom type hpicfGppcv2AcIngressTunnelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfGppcv2AcIngressTunnelList_Type.__name__ = "OctetString"
_HpicfGppcv2AcIngressTunnelList_Object = MibTableColumn
hpicfGppcv2AcIngressTunnelList = _HpicfGppcv2AcIngressTunnelList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 16),
    _HpicfGppcv2AcIngressTunnelList_Type()
)
hpicfGppcv2AcIngressTunnelList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcIngressTunnelList.setStatus("current")


class _HpicfGppcv2AcEgressTunnelList_Type(OctetString):
    """Custom type hpicfGppcv2AcEgressTunnelList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfGppcv2AcEgressTunnelList_Type.__name__ = "OctetString"
_HpicfGppcv2AcEgressTunnelList_Object = MibTableColumn
hpicfGppcv2AcEgressTunnelList = _HpicfGppcv2AcEgressTunnelList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 17),
    _HpicfGppcv2AcEgressTunnelList_Type()
)
hpicfGppcv2AcEgressTunnelList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcEgressTunnelList.setStatus("current")


class _HpicfGppcv2AcVACLEgressVIDList_Type(OctetString):
    """Custom type hpicfGppcv2AcVACLEgressVIDList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpicfGppcv2AcVACLEgressVIDList_Type.__name__ = "OctetString"
_HpicfGppcv2AcVACLEgressVIDList_Object = MibTableColumn
hpicfGppcv2AcVACLEgressVIDList = _HpicfGppcv2AcVACLEgressVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 18),
    _HpicfGppcv2AcVACLEgressVIDList_Type()
)
hpicfGppcv2AcVACLEgressVIDList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcVACLEgressVIDList.setStatus("current")
_HpicfGppcv2AcSharedFlag_Type = TruthValue
_HpicfGppcv2AcSharedFlag_Object = MibTableColumn
hpicfGppcv2AcSharedFlag = _HpicfGppcv2AcSharedFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 2, 1, 19),
    _HpicfGppcv2AcSharedFlag_Type()
)
hpicfGppcv2AcSharedFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2AcSharedFlag.setStatus("current")
_HpicfGppcv2NamedPolicyTable_Object = MibTable
hpicfGppcv2NamedPolicyTable = _HpicfGppcv2NamedPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3)
)
if mibBuilder.loadTexts:
    hpicfGppcv2NamedPolicyTable.setStatus("current")
_HpicfGppcv2NamedPolicyEntry_Object = MibTableRow
hpicfGppcv2NamedPolicyEntry = _HpicfGppcv2NamedPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1)
)
hpicfGppcv2NamedPolicyEntry.setIndexNames(
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpPolicyName"),
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpPolicyType"),
)
if mibBuilder.loadTexts:
    hpicfGppcv2NamedPolicyEntry.setStatus("current")
_HpicfGppcv2NpPolicyName_Type = HpicfGppcv2PolicyName
_HpicfGppcv2NpPolicyName_Object = MibTableColumn
hpicfGppcv2NpPolicyName = _HpicfGppcv2NpPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 1),
    _HpicfGppcv2NpPolicyName_Type()
)
hpicfGppcv2NpPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcv2NpPolicyName.setStatus("current")
_HpicfGppcv2NpPolicyType_Type = HpicfGppcv2PolicyType
_HpicfGppcv2NpPolicyType_Object = MibTableColumn
hpicfGppcv2NpPolicyType = _HpicfGppcv2NpPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 2),
    _HpicfGppcv2NpPolicyType_Type()
)
hpicfGppcv2NpPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcv2NpPolicyType.setStatus("current")


class _HpicfGppcv2NpSubType_Type(Integer32):
    """Custom type hpicfGppcv2NpSubType based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("aclConnectionRateFilter", 4),
          ("aclExtended", 3),
          ("aclExtendedIpv6", 6),
          ("aclIdm", 5),
          ("aclMacExtended", 12),
          ("aclMacStandard", 11),
          ("aclStandard", 2),
          ("policyIpsec", 10),
          ("policyMirror", 8),
          ("policyPbr", 9),
          ("policyQos", 7),
          ("policyUser", 13),
          ("subtypeNone", 1))
    )


_HpicfGppcv2NpSubType_Type.__name__ = "Integer32"
_HpicfGppcv2NpSubType_Object = MibTableColumn
hpicfGppcv2NpSubType = _HpicfGppcv2NpSubType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 3),
    _HpicfGppcv2NpSubType_Type()
)
hpicfGppcv2NpSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2NpSubType.setStatus("current")


class _HpicfGppcv2NpReseqStart_Type(Integer32):
    """Custom type hpicfGppcv2NpReseqStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfGppcv2NpReseqStart_Type.__name__ = "Integer32"
_HpicfGppcv2NpReseqStart_Object = MibTableColumn
hpicfGppcv2NpReseqStart = _HpicfGppcv2NpReseqStart_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 4),
    _HpicfGppcv2NpReseqStart_Type()
)
hpicfGppcv2NpReseqStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2NpReseqStart.setStatus("current")


class _HpicfGppcv2NpReseqIncr_Type(Integer32):
    """Custom type hpicfGppcv2NpReseqIncr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfGppcv2NpReseqIncr_Type.__name__ = "Integer32"
_HpicfGppcv2NpReseqIncr_Object = MibTableColumn
hpicfGppcv2NpReseqIncr = _HpicfGppcv2NpReseqIncr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 5),
    _HpicfGppcv2NpReseqIncr_Type()
)
hpicfGppcv2NpReseqIncr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2NpReseqIncr.setStatus("current")


class _HpicfGppcv2NpLastSeqNo_Type(Integer32):
    """Custom type hpicfGppcv2NpLastSeqNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpicfGppcv2NpLastSeqNo_Type.__name__ = "Integer32"
_HpicfGppcv2NpLastSeqNo_Object = MibTableColumn
hpicfGppcv2NpLastSeqNo = _HpicfGppcv2NpLastSeqNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 6),
    _HpicfGppcv2NpLastSeqNo_Type()
)
hpicfGppcv2NpLastSeqNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGppcv2NpLastSeqNo.setStatus("current")
_HpicfGppcv2NpLastErrorCode_Type = HpicfGppcv2LastErrorCode
_HpicfGppcv2NpLastErrorCode_Object = MibTableColumn
hpicfGppcv2NpLastErrorCode = _HpicfGppcv2NpLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 7),
    _HpicfGppcv2NpLastErrorCode_Type()
)
hpicfGppcv2NpLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGppcv2NpLastErrorCode.setStatus("current")


class _HpicfGppcv2NpLastErrorString_Type(SnmpAdminString):
    """Custom type hpicfGppcv2NpLastErrorString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfGppcv2NpLastErrorString_Type.__name__ = "SnmpAdminString"
_HpicfGppcv2NpLastErrorString_Object = MibTableColumn
hpicfGppcv2NpLastErrorString = _HpicfGppcv2NpLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 8),
    _HpicfGppcv2NpLastErrorString_Type()
)
hpicfGppcv2NpLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfGppcv2NpLastErrorString.setStatus("current")
_HpicfGppcv2NpRowStatus_Type = RowStatus
_HpicfGppcv2NpRowStatus_Object = MibTableColumn
hpicfGppcv2NpRowStatus = _HpicfGppcv2NpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 3, 1, 9),
    _HpicfGppcv2NpRowStatus_Type()
)
hpicfGppcv2NpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2NpRowStatus.setStatus("current")
_HpicfGppcv2PolicyRulesTable_Object = MibTable
hpicfGppcv2PolicyRulesTable = _HpicfGppcv2PolicyRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 4)
)
if mibBuilder.loadTexts:
    hpicfGppcv2PolicyRulesTable.setStatus("current")
_HpicfGppcv2PolicyRulesEntry_Object = MibTableRow
hpicfGppcv2PolicyRulesEntry = _HpicfGppcv2PolicyRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 4, 1)
)
hpicfGppcv2PolicyRulesEntry.setIndexNames(
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpPolicyName"),
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpPolicyType"),
    (0, "HP-ICF-GPPCV2-MIB", "hpicfGppcv2PrRuleId"),
)
if mibBuilder.loadTexts:
    hpicfGppcv2PolicyRulesEntry.setStatus("current")


class _HpicfGppcv2PrRuleId_Type(Integer32):
    """Custom type hpicfGppcv2PrRuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfGppcv2PrRuleId_Type.__name__ = "Integer32"
_HpicfGppcv2PrRuleId_Object = MibTableColumn
hpicfGppcv2PrRuleId = _HpicfGppcv2PrRuleId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 4, 1, 1),
    _HpicfGppcv2PrRuleId_Type()
)
hpicfGppcv2PrRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfGppcv2PrRuleId.setStatus("current")


class _HpicfGppcv2PrPolicyRule_Type(OctetString):
    """Custom type hpicfGppcv2PrPolicyRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_HpicfGppcv2PrPolicyRule_Type.__name__ = "OctetString"
_HpicfGppcv2PrPolicyRule_Object = MibTableColumn
hpicfGppcv2PrPolicyRule = _HpicfGppcv2PrPolicyRule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 4, 1, 2),
    _HpicfGppcv2PrPolicyRule_Type()
)
hpicfGppcv2PrPolicyRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2PrPolicyRule.setStatus("current")


class _HpicfGppcv2PrRemark_Type(OctetString):
    """Custom type hpicfGppcv2PrRemark based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HpicfGppcv2PrRemark_Type.__name__ = "OctetString"
_HpicfGppcv2PrRemark_Object = MibTableColumn
hpicfGppcv2PrRemark = _HpicfGppcv2PrRemark_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 4, 1, 3),
    _HpicfGppcv2PrRemark_Type()
)
hpicfGppcv2PrRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2PrRemark.setStatus("current")
_HpicfGppcv2PrRowStatus_Type = RowStatus
_HpicfGppcv2PrRowStatus_Object = MibTableColumn
hpicfGppcv2PrRowStatus = _HpicfGppcv2PrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 4, 1, 4),
    _HpicfGppcv2PrRowStatus_Type()
)
hpicfGppcv2PrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfGppcv2PrRowStatus.setStatus("current")

# Managed Objects groups

hpicfGppcv2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 1, 2, 1)
)
hpicfGppcv2Group.setObjects(
      *(("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcIngressIfList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcIngressVIDList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcEgressIfList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcEgressVIDList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcVIDList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcExpPolicy"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcExpString"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcLastErrorCode"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcLastErrorString"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcRowAdminStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcRowStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpSubType"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpReseqStart"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpReseqIncr"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpLastSeqNo"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpLastErrorCode"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpLastErrorString"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpRowStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2PrPolicyRule"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2PrRemark"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2PrRowStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcIngressTunnelList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcEgressTunnelList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcVACLEgressVIDList"))
)
if mibBuilder.loadTexts:
    hpicfGppcv2Group.setStatus("deprecated")

hpicfGppcv2Group1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 1, 2, 2)
)
hpicfGppcv2Group1.setObjects(
      *(("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcIngressIfList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcIngressVIDList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcEgressIfList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcEgressVIDList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcVIDList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcExpPolicy"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcExpString"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcLastErrorCode"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcLastErrorString"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcRowAdminStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcRowStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpSubType"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpReseqStart"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpReseqIncr"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpLastSeqNo"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpLastErrorCode"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpLastErrorString"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2NpRowStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2PrPolicyRule"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2PrRemark"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2PrRowStatus"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcIngressTunnelList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcEgressTunnelList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcVACLEgressVIDList"),
        ("HP-ICF-GPPCV2-MIB", "hpicfGppcv2AcSharedFlag"))
)
if mibBuilder.loadTexts:
    hpicfGppcv2Group1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfGppcv2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfGppcv2MIBCompliance.setStatus(
        "deprecated"
    )

hpicfGppcv2MIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 61, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfGppcv2MIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-GPPCV2-MIB",
    **{"HpicfGppcv2PolicyName": HpicfGppcv2PolicyName,
       "HpicfGppcv2PolicyType": HpicfGppcv2PolicyType,
       "HpicfGppcv2LastErrorCode": HpicfGppcv2LastErrorCode,
       "hpicfGppcv2MIB": hpicfGppcv2MIB,
       "hpicfGppcv2Conformance": hpicfGppcv2Conformance,
       "hpicfGppcv2MIBCompliances": hpicfGppcv2MIBCompliances,
       "hpicfGppcv2MIBCompliance": hpicfGppcv2MIBCompliance,
       "hpicfGppcv2MIBCompliance1": hpicfGppcv2MIBCompliance1,
       "hpicfGppcv2MIBGroups": hpicfGppcv2MIBGroups,
       "hpicfGppcv2Group": hpicfGppcv2Group,
       "hpicfGppcv2Group1": hpicfGppcv2Group1,
       "hpicfGppcv2AppControlTable": hpicfGppcv2AppControlTable,
       "hpicfGppcv2AppControlEntry": hpicfGppcv2AppControlEntry,
       "hpicfGppcv2AcAppName": hpicfGppcv2AcAppName,
       "hpicfGppcv2AcAppInstance": hpicfGppcv2AcAppInstance,
       "hpicfGppcv2AcPolicyType": hpicfGppcv2AcPolicyType,
       "hpicfGppcv2AcPolicyName": hpicfGppcv2AcPolicyName,
       "hpicfGppcv2AcIngressIfList": hpicfGppcv2AcIngressIfList,
       "hpicfGppcv2AcIngressVIDList": hpicfGppcv2AcIngressVIDList,
       "hpicfGppcv2AcEgressIfList": hpicfGppcv2AcEgressIfList,
       "hpicfGppcv2AcEgressVIDList": hpicfGppcv2AcEgressVIDList,
       "hpicfGppcv2AcVIDList": hpicfGppcv2AcVIDList,
       "hpicfGppcv2AcExpPolicy": hpicfGppcv2AcExpPolicy,
       "hpicfGppcv2AcExpString": hpicfGppcv2AcExpString,
       "hpicfGppcv2AcLastErrorCode": hpicfGppcv2AcLastErrorCode,
       "hpicfGppcv2AcLastErrorString": hpicfGppcv2AcLastErrorString,
       "hpicfGppcv2AcRowAdminStatus": hpicfGppcv2AcRowAdminStatus,
       "hpicfGppcv2AcRowStatus": hpicfGppcv2AcRowStatus,
       "hpicfGppcv2AcIngressTunnelList": hpicfGppcv2AcIngressTunnelList,
       "hpicfGppcv2AcEgressTunnelList": hpicfGppcv2AcEgressTunnelList,
       "hpicfGppcv2AcVACLEgressVIDList": hpicfGppcv2AcVACLEgressVIDList,
       "hpicfGppcv2AcSharedFlag": hpicfGppcv2AcSharedFlag,
       "hpicfGppcv2NamedPolicyTable": hpicfGppcv2NamedPolicyTable,
       "hpicfGppcv2NamedPolicyEntry": hpicfGppcv2NamedPolicyEntry,
       "hpicfGppcv2NpPolicyName": hpicfGppcv2NpPolicyName,
       "hpicfGppcv2NpPolicyType": hpicfGppcv2NpPolicyType,
       "hpicfGppcv2NpSubType": hpicfGppcv2NpSubType,
       "hpicfGppcv2NpReseqStart": hpicfGppcv2NpReseqStart,
       "hpicfGppcv2NpReseqIncr": hpicfGppcv2NpReseqIncr,
       "hpicfGppcv2NpLastSeqNo": hpicfGppcv2NpLastSeqNo,
       "hpicfGppcv2NpLastErrorCode": hpicfGppcv2NpLastErrorCode,
       "hpicfGppcv2NpLastErrorString": hpicfGppcv2NpLastErrorString,
       "hpicfGppcv2NpRowStatus": hpicfGppcv2NpRowStatus,
       "hpicfGppcv2PolicyRulesTable": hpicfGppcv2PolicyRulesTable,
       "hpicfGppcv2PolicyRulesEntry": hpicfGppcv2PolicyRulesEntry,
       "hpicfGppcv2PrRuleId": hpicfGppcv2PrRuleId,
       "hpicfGppcv2PrPolicyRule": hpicfGppcv2PrPolicyRule,
       "hpicfGppcv2PrRemark": hpicfGppcv2PrRemark,
       "hpicfGppcv2PrRowStatus": hpicfGppcv2PrRowStatus}
)
