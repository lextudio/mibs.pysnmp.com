# SNMP MIB module (ALCATEL-IND1-DA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:47 2024
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

(softentIND1Da,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "softentIND1Da")

(TmnxEncapVal,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "TmnxEncapVal")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv4,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv4",
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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1DaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1)
)
alcatelIND1DaMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaDaClassificationPolicyType(Integer32, TextualConvention):
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
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67)
        )
    )
    namedValues = NamedValues(
        *(("authFailDefUnp", 7),
          ("authFailDefUnpBlk", 32),
          ("authFailIpRuleUnp", 10),
          ("authFailIpRuleUnpBlk", 51),
          ("authFailIpRuleUnpTagMismatchBlk", 43),
          ("authFailIpVlanRuleUnpTagMismatchBlk", 44),
          ("authFailMacRangeRuleUnp", 9),
          ("authFailMacRangeRuleUnpBlk", 50),
          ("authFailMacRangeRuleUnpTagMismatchBlk", 41),
          ("authFailMacRangeVlanRuleUnpTagMismatchBlk", 42),
          ("authFailMacRangeVlanTagRuleUnp", 12),
          ("authFailMacRuleUnp", 8),
          ("authFailMacRuleUnpBlk", 49),
          ("authFailMacRuleUnpTagMismatchBlk", 39),
          ("authFailMacVlanRuleUnpTagMismatchBlk", 40),
          ("authFailRuleDefUnp", 11),
          ("authFailRuleDefUnpBlk", 33),
          ("authFailVlanRuleUnpTagMismatchBlk", 45),
          ("authPassAltUnp", 1),
          ("authPassAltUnpBlk", 48),
          ("authPassAltUnpTagMismatchBlk", 37),
          ("authPassDefUnp", 2),
          ("authPassDefUnpBlk", 31),
          ("authPassDefUnpTagMismatchBlk", 38),
          ("authPassSrvUnp", 3),
          ("authPassSrvUnpBlk", 47),
          ("authPassSrvUnpTagMismatchBlk", 36),
          ("authSrvDownUnp", 62),
          ("authSrvDownUnpTagMismatchBlk", 59),
          ("defSpbProfile", 66),
          ("defUnp", 63),
          ("defUnpBlk", 46),
          ("lpsUnpBlk", 64),
          ("noAuthIpRuleUnp", 6),
          ("noAuthMacRangeRuleUnp", 5),
          ("noAuthMacRuleUnp", 4),
          ("noMatchingUnpBlk", 60),
          ("noSpbResource", 67),
          ("sysDefSpb", 65),
          ("tagAuthFailIpRuleUnp", 17),
          ("tagAuthFailIpVlanTagRuleUnp", 18),
          ("tagAuthFailMacRangeRuleUnp", 15),
          ("tagAuthFailMacRangeVlanTagRuleUnp", 16),
          ("tagAuthFailMacRuleUnp", 13),
          ("tagAuthFailMacVlanTagRuleUnp", 14),
          ("tagAuthFailVlanTagRuleUnp", 19),
          ("tagAuthPassAltUnp", 20),
          ("tagAuthPassDefUnp", 21),
          ("tagAuthPassDefUnpBlk", 34),
          ("tagAuthPassSrvUnp", 22),
          ("tagIpRuleUnp", 27),
          ("tagIpRuleUnpBlk", 56),
          ("tagIpVlanTagRuleUnp", 28),
          ("tagIpVlanTagRuleUnpBlk", 57),
          ("tagMacRangeRuleUnp", 25),
          ("tagMacRangeRuleUnpBlk", 54),
          ("tagMacRangeVlanTagRuleUnp", 26),
          ("tagMacRangeVlanTagRuleUnpBlk", 55),
          ("tagMacRuleUnp", 23),
          ("tagMacRuleUnpBlk", 52),
          ("tagMacVlanTagRuleUnp", 24),
          ("tagMacVlanTagRuleUnpBlk", 53),
          ("tagRuleDefUnp", 30),
          ("tagRuleDefUnpBlk", 35),
          ("tagVlanTagRuleUnp", 29),
          ("tagVlanTagRuleUnpBlk", 58),
          ("trustTag", 61))
    )



class AlaDaAuthenticationType(Integer32, TextualConvention):
    status = "current"
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
        *(("captivePortal", 4),
          ("dot1XAuthentication", 2),
          ("macAuthentication", 3),
          ("noAuthentication", 1))
    )



class AlaDaAuthenticationResult(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("inProgress", 1),
          ("notApplicable", 0),
          ("success", 2))
    )



class AlaDaMacLearntState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bridging", 0),
          ("filtering", 1))
    )



class AlaMultiChassisConfigStatus(Integer32, TextualConvention):
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
        *(("local", 1),
          ("outOfSync", 3),
          ("sync", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlaIND1DaMIBNotifications_ObjectIdentity = ObjectIdentity
alaIND1DaMIBNotifications = _AlaIND1DaMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 0)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBNotifications.setStatus("current")
_AlaIND1DaMIBObjects_ObjectIdentity = ObjectIdentity
alaIND1DaMIBObjects = _AlaIND1DaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBObjects.setStatus("current")
_AlaDaUserNetProfileTable_Object = MibTable
alaDaUserNetProfileTable = _AlaDaUserNetProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaDaUserNetProfileTable.setStatus("current")
_AlaDaUserNetProfileEntry_Object = MibTableRow
alaDaUserNetProfileEntry = _AlaDaUserNetProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1, 1)
)
alaDaUserNetProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileName"),
)
if mibBuilder.loadTexts:
    alaDaUserNetProfileEntry.setStatus("current")


class _AlaDaUserNetProfileName_Type(SnmpAdminString):
    """Custom type alaDaUserNetProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUserNetProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUserNetProfileName_Object = MibTableColumn
alaDaUserNetProfileName = _AlaDaUserNetProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1, 1, 1),
    _AlaDaUserNetProfileName_Type()
)
alaDaUserNetProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUserNetProfileName.setStatus("current")


class _AlaDaUserNetProfileVlanID_Type(Integer32):
    """Custom type alaDaUserNetProfileVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUserNetProfileVlanID_Type.__name__ = "Integer32"
_AlaDaUserNetProfileVlanID_Object = MibTableColumn
alaDaUserNetProfileVlanID = _AlaDaUserNetProfileVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1, 1, 2),
    _AlaDaUserNetProfileVlanID_Type()
)
alaDaUserNetProfileVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileVlanID.setStatus("current")
_AlaDaUserNetProfileRowStatus_Type = RowStatus
_AlaDaUserNetProfileRowStatus_Object = MibTableColumn
alaDaUserNetProfileRowStatus = _AlaDaUserNetProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1, 1, 3),
    _AlaDaUserNetProfileRowStatus_Type()
)
alaDaUserNetProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileRowStatus.setStatus("current")


class _AlaDaUserNetProfileQosPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaUserNetProfileQosPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUserNetProfileQosPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaUserNetProfileQosPolicyListName_Object = MibTableColumn
alaDaUserNetProfileQosPolicyListName = _AlaDaUserNetProfileQosPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1, 1, 4),
    _AlaDaUserNetProfileQosPolicyListName_Type()
)
alaDaUserNetProfileQosPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileQosPolicyListName.setStatus("current")


class _AlaDaUserNetProfileMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUserNetProfileMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUserNetProfileMCLagConfigStatus_Object = MibTableColumn
alaDaUserNetProfileMCLagConfigStatus = _AlaDaUserNetProfileMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1, 1, 5),
    _AlaDaUserNetProfileMCLagConfigStatus_Type()
)
alaDaUserNetProfileMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUserNetProfileMCLagConfigStatus.setStatus("current")


class _AlaDaUserNetProfileSaaProfileName_Type(SnmpAdminString):
    """Custom type alaDaUserNetProfileSaaProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUserNetProfileSaaProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUserNetProfileSaaProfileName_Object = MibTableColumn
alaDaUserNetProfileSaaProfileName = _AlaDaUserNetProfileSaaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 1, 1, 6),
    _AlaDaUserNetProfileSaaProfileName_Type()
)
alaDaUserNetProfileSaaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUserNetProfileSaaProfileName.setStatus("current")
_AlaDaUNPIpNetRuleTable_Object = MibTable
alaDaUNPIpNetRuleTable = _AlaDaUNPIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleTable.setStatus("deprecated")
_AlaDaUNPIpNetRuleEntry_Object = MibTableRow
alaDaUNPIpNetRuleEntry = _AlaDaUNPIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1)
)
alaDaUNPIpNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleMask"),
)
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleEntry.setStatus("deprecated")
_AlaDaUNPIpNetRuleAddrType_Type = InetAddressType
_AlaDaUNPIpNetRuleAddrType_Object = MibTableColumn
alaDaUNPIpNetRuleAddrType = _AlaDaUNPIpNetRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1, 1),
    _AlaDaUNPIpNetRuleAddrType_Type()
)
alaDaUNPIpNetRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleAddrType.setStatus("deprecated")
_AlaDaUNPIpNetRuleAddr_Type = InetAddress
_AlaDaUNPIpNetRuleAddr_Object = MibTableColumn
alaDaUNPIpNetRuleAddr = _AlaDaUNPIpNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1, 2),
    _AlaDaUNPIpNetRuleAddr_Type()
)
alaDaUNPIpNetRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleAddr.setStatus("deprecated")
_AlaDaUNPIpNetRuleMask_Type = InetAddress
_AlaDaUNPIpNetRuleMask_Object = MibTableColumn
alaDaUNPIpNetRuleMask = _AlaDaUNPIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1, 3),
    _AlaDaUNPIpNetRuleMask_Type()
)
alaDaUNPIpNetRuleMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleMask.setStatus("deprecated")


class _AlaDaUNPIpNetRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPIpNetRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPIpNetRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPIpNetRuleProfileName_Object = MibTableColumn
alaDaUNPIpNetRuleProfileName = _AlaDaUNPIpNetRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1, 4),
    _AlaDaUNPIpNetRuleProfileName_Type()
)
alaDaUNPIpNetRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleProfileName.setStatus("deprecated")


class _AlaDaUNPIpNetRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPIpNetRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPIpNetRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPIpNetRuleVlanTag_Object = MibTableColumn
alaDaUNPIpNetRuleVlanTag = _AlaDaUNPIpNetRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1, 5),
    _AlaDaUNPIpNetRuleVlanTag_Type()
)
alaDaUNPIpNetRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleVlanTag.setStatus("deprecated")
_AlaDaUNPIpNetRuleRowStatus_Type = RowStatus
_AlaDaUNPIpNetRuleRowStatus_Object = MibTableColumn
alaDaUNPIpNetRuleRowStatus = _AlaDaUNPIpNetRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1, 6),
    _AlaDaUNPIpNetRuleRowStatus_Type()
)
alaDaUNPIpNetRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPIpNetRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPIpNetRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPIpNetRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPIpNetRuleMCLagConfigStatus = _AlaDaUNPIpNetRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 2, 1, 7),
    _AlaDaUNPIpNetRuleMCLagConfigStatus_Type()
)
alaDaUNPIpNetRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaUNPMacRuleTable_Object = MibTable
alaDaUNPMacRuleTable = _AlaDaUNPMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaDaUNPMacRuleTable.setStatus("deprecated")
_AlaDaUNPMacRuleEntry_Object = MibTableRow
alaDaUNPMacRuleEntry = _AlaDaUNPMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 3, 1)
)
alaDaUNPMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacRuleEntry.setStatus("deprecated")
_AlaDaUNPMacRuleAddr_Type = MacAddress
_AlaDaUNPMacRuleAddr_Object = MibTableColumn
alaDaUNPMacRuleAddr = _AlaDaUNPMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 3, 1, 1),
    _AlaDaUNPMacRuleAddr_Type()
)
alaDaUNPMacRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleAddr.setStatus("deprecated")


class _AlaDaUNPMacRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPMacRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacRuleProfileName_Object = MibTableColumn
alaDaUNPMacRuleProfileName = _AlaDaUNPMacRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 3, 1, 2),
    _AlaDaUNPMacRuleProfileName_Type()
)
alaDaUNPMacRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleProfileName.setStatus("deprecated")


class _AlaDaUNPMacRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacRuleVlanTag_Object = MibTableColumn
alaDaUNPMacRuleVlanTag = _AlaDaUNPMacRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 3, 1, 3),
    _AlaDaUNPMacRuleVlanTag_Type()
)
alaDaUNPMacRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleVlanTag.setStatus("deprecated")
_AlaDaUNPMacRuleRowStatus_Type = RowStatus
_AlaDaUNPMacRuleRowStatus_Object = MibTableColumn
alaDaUNPMacRuleRowStatus = _AlaDaUNPMacRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 3, 1, 4),
    _AlaDaUNPMacRuleRowStatus_Type()
)
alaDaUNPMacRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPMacRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPMacRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPMacRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPMacRuleMCLagConfigStatus = _AlaDaUNPMacRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 3, 1, 5),
    _AlaDaUNPMacRuleMCLagConfigStatus_Type()
)
alaDaUNPMacRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPMacRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaUNPMacRangeRuleTable_Object = MibTable
alaDaUNPMacRangeRuleTable = _AlaDaUNPMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleTable.setStatus("deprecated")
_AlaDaUNPMacRangeRuleEntry_Object = MibTableRow
alaDaUNPMacRangeRuleEntry = _AlaDaUNPMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4, 1)
)
alaDaUNPMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleEntry.setStatus("deprecated")
_AlaDaUNPMacRangeRuleLoAddr_Type = MacAddress
_AlaDaUNPMacRangeRuleLoAddr_Object = MibTableColumn
alaDaUNPMacRangeRuleLoAddr = _AlaDaUNPMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4, 1, 1),
    _AlaDaUNPMacRangeRuleLoAddr_Type()
)
alaDaUNPMacRangeRuleLoAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleLoAddr.setStatus("deprecated")
_AlaDaUNPMacRangeRuleHiAddr_Type = MacAddress
_AlaDaUNPMacRangeRuleHiAddr_Object = MibTableColumn
alaDaUNPMacRangeRuleHiAddr = _AlaDaUNPMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4, 1, 2),
    _AlaDaUNPMacRangeRuleHiAddr_Type()
)
alaDaUNPMacRangeRuleHiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleHiAddr.setStatus("deprecated")


class _AlaDaUNPMacRangeRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPMacRangeRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPMacRangeRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPMacRangeRuleProfileName_Object = MibTableColumn
alaDaUNPMacRangeRuleProfileName = _AlaDaUNPMacRangeRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4, 1, 3),
    _AlaDaUNPMacRangeRuleProfileName_Type()
)
alaDaUNPMacRangeRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleProfileName.setStatus("deprecated")


class _AlaDaUNPMacRangeRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPMacRangeRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPMacRangeRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPMacRangeRuleVlanTag_Object = MibTableColumn
alaDaUNPMacRangeRuleVlanTag = _AlaDaUNPMacRangeRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4, 1, 4),
    _AlaDaUNPMacRangeRuleVlanTag_Type()
)
alaDaUNPMacRangeRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleVlanTag.setStatus("deprecated")
_AlaDaUNPMacRangeRuleRowStatus_Type = RowStatus
_AlaDaUNPMacRangeRuleRowStatus_Object = MibTableColumn
alaDaUNPMacRangeRuleRowStatus = _AlaDaUNPMacRangeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4, 1, 5),
    _AlaDaUNPMacRangeRuleRowStatus_Type()
)
alaDaUNPMacRangeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPMacRangeRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPMacRangeRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPMacRangeRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPMacRangeRuleMCLagConfigStatus = _AlaDaUNPMacRangeRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 4, 1, 6),
    _AlaDaUNPMacRangeRuleMCLagConfigStatus_Type()
)
alaDaUNPMacRangeRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPMacRangeRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaUNPVlanTagRuleTable_Object = MibTable
alaDaUNPVlanTagRuleTable = _AlaDaUNPVlanTagRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 5)
)
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleTable.setStatus("deprecated")
_AlaDaUNPVlanTagRuleEntry_Object = MibTableRow
alaDaUNPVlanTagRuleEntry = _AlaDaUNPVlanTagRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 5, 1)
)
alaDaUNPVlanTagRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleVlan"),
)
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleEntry.setStatus("deprecated")


class _AlaDaUNPVlanTagRuleVlan_Type(Integer32):
    """Custom type alaDaUNPVlanTagRuleVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPVlanTagRuleVlan_Type.__name__ = "Integer32"
_AlaDaUNPVlanTagRuleVlan_Object = MibTableColumn
alaDaUNPVlanTagRuleVlan = _AlaDaUNPVlanTagRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 5, 1, 1),
    _AlaDaUNPVlanTagRuleVlan_Type()
)
alaDaUNPVlanTagRuleVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleVlan.setStatus("deprecated")


class _AlaDaUNPVlanTagRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPVlanTagRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPVlanTagRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPVlanTagRuleProfileName_Object = MibTableColumn
alaDaUNPVlanTagRuleProfileName = _AlaDaUNPVlanTagRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 5, 1, 2),
    _AlaDaUNPVlanTagRuleProfileName_Type()
)
alaDaUNPVlanTagRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleProfileName.setStatus("deprecated")
_AlaDaUNPVlanTagRuleRowStatus_Type = RowStatus
_AlaDaUNPVlanTagRuleRowStatus_Object = MibTableColumn
alaDaUNPVlanTagRuleRowStatus = _AlaDaUNPVlanTagRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 5, 1, 3),
    _AlaDaUNPVlanTagRuleRowStatus_Type()
)
alaDaUNPVlanTagRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleRowStatus.setStatus("deprecated")


class _AlaDaUNPVlanTagRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPVlanTagRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPVlanTagRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPVlanTagRuleMCLagConfigStatus = _AlaDaUNPVlanTagRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 5, 1, 4),
    _AlaDaUNPVlanTagRuleMCLagConfigStatus_Type()
)
alaDaUNPVlanTagRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPVlanTagRuleMCLagConfigStatus.setStatus("deprecated")
_AlaDaMacUserTable_Object = MibTable
alaDaMacUserTable = _AlaDaMacUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6)
)
if mibBuilder.loadTexts:
    alaDaMacUserTable.setStatus("current")
_AlaDaMacUserEntry_Object = MibTableRow
alaDaMacUserEntry = _AlaDaMacUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1)
)
alaDaMacUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacUserIntfNum"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacUserMACAddress"),
)
if mibBuilder.loadTexts:
    alaDaMacUserEntry.setStatus("current")
_AlaDaMacUserIntfNum_Type = InterfaceIndex
_AlaDaMacUserIntfNum_Object = MibTableColumn
alaDaMacUserIntfNum = _AlaDaMacUserIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 1),
    _AlaDaMacUserIntfNum_Type()
)
alaDaMacUserIntfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacUserIntfNum.setStatus("current")
_AlaDaMacUserMACAddress_Type = MacAddress
_AlaDaMacUserMACAddress_Object = MibTableColumn
alaDaMacUserMACAddress = _AlaDaMacUserMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 2),
    _AlaDaMacUserMACAddress_Type()
)
alaDaMacUserMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacUserMACAddress.setStatus("current")


class _AlaDaMacUserVlanID_Type(Integer32):
    """Custom type alaDaMacUserVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaMacUserVlanID_Type.__name__ = "Integer32"
_AlaDaMacUserVlanID_Object = MibTableColumn
alaDaMacUserVlanID = _AlaDaMacUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 3),
    _AlaDaMacUserVlanID_Type()
)
alaDaMacUserVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserVlanID.setStatus("current")


class _AlaDaAuthenticationStatus_Type(Integer32):
    """Custom type alaDaAuthenticationStatus based on Integer32"""
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
        *(("authenticated", 3),
          ("failed", 4),
          ("failedNoResources", 7),
          ("failedNoServer", 6),
          ("failedTimeout", 5),
          ("idle", 1),
          ("inProgress", 2))
    )


_AlaDaAuthenticationStatus_Type.__name__ = "Integer32"
_AlaDaAuthenticationStatus_Object = MibTableColumn
alaDaAuthenticationStatus = _AlaDaAuthenticationStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 4),
    _AlaDaAuthenticationStatus_Type()
)
alaDaAuthenticationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaAuthenticationStatus.setStatus("current")
_AlaDaMacUserIpAddress_Type = IpAddress
_AlaDaMacUserIpAddress_Object = MibTableColumn
alaDaMacUserIpAddress = _AlaDaMacUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 5),
    _AlaDaMacUserIpAddress_Type()
)
alaDaMacUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserIpAddress.setStatus("current")
_AlaDaMacUserUnpUsed_Type = SnmpAdminString
_AlaDaMacUserUnpUsed_Object = MibTableColumn
alaDaMacUserUnpUsed = _AlaDaMacUserUnpUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 6),
    _AlaDaMacUserUnpUsed_Type()
)
alaDaMacUserUnpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserUnpUsed.setStatus("current")
_AlaDaMacUserLoginTimeStamp_Type = DateAndTime
_AlaDaMacUserLoginTimeStamp_Object = MibTableColumn
alaDaMacUserLoginTimeStamp = _AlaDaMacUserLoginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 7),
    _AlaDaMacUserLoginTimeStamp_Type()
)
alaDaMacUserLoginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserLoginTimeStamp.setStatus("current")


class _AlaDaMacUserAuthtype_Type(Integer32):
    """Custom type alaDaMacUserAuthtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("macAuthentication", 0),
          ("others", 1))
    )


_AlaDaMacUserAuthtype_Type.__name__ = "Integer32"
_AlaDaMacUserAuthtype_Object = MibTableColumn
alaDaMacUserAuthtype = _AlaDaMacUserAuthtype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 8),
    _AlaDaMacUserAuthtype_Type()
)
alaDaMacUserAuthtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserAuthtype.setStatus("current")
_AlaDaMacUserClassificationSource_Type = AlaDaClassificationPolicyType
_AlaDaMacUserClassificationSource_Object = MibTableColumn
alaDaMacUserClassificationSource = _AlaDaMacUserClassificationSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 6, 1, 9),
    _AlaDaMacUserClassificationSource_Type()
)
alaDaMacUserClassificationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacUserClassificationSource.setStatus("current")
_AlaDaUNPPortTable_Object = MibTable
alaDaUNPPortTable = _AlaDaUNPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaDaUNPPortTable.setStatus("current")
_AlaDaUNPPortEntry_Object = MibTableRow
alaDaUNPPortEntry = _AlaDaUNPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1)
)
alaDaUNPPortEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPPortIfIndex"),
)
if mibBuilder.loadTexts:
    alaDaUNPPortEntry.setStatus("current")
_AlaDaUNPPortIfIndex_Type = InterfaceIndexOrZero
_AlaDaUNPPortIfIndex_Object = MibTableColumn
alaDaUNPPortIfIndex = _AlaDaUNPPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 1),
    _AlaDaUNPPortIfIndex_Type()
)
alaDaUNPPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPPortIfIndex.setStatus("current")


class _AlaDaUNPPortDefaultProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortDefaultProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortDefaultProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortDefaultProfileName_Object = MibTableColumn
alaDaUNPPortDefaultProfileName = _AlaDaUNPPortDefaultProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 2),
    _AlaDaUNPPortDefaultProfileName_Type()
)
alaDaUNPPortDefaultProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDefaultProfileName.setStatus("current")


class _AlaDaUNPPortPassAltProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortPassAltProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortPassAltProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortPassAltProfileName_Object = MibTableColumn
alaDaUNPPortPassAltProfileName = _AlaDaUNPPortPassAltProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 3),
    _AlaDaUNPPortPassAltProfileName_Type()
)
alaDaUNPPortPassAltProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortPassAltProfileName.setStatus("current")
_AlaDaUNPPortRowStatus_Type = RowStatus
_AlaDaUNPPortRowStatus_Object = MibTableColumn
alaDaUNPPortRowStatus = _AlaDaUNPPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 4),
    _AlaDaUNPPortRowStatus_Type()
)
alaDaUNPPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortRowStatus.setStatus("current")


class _AlaDaUNPPortMacAuthFlag_Type(Integer32):
    """Custom type alaDaUNPPortMacAuthFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDaUNPPortMacAuthFlag_Type.__name__ = "Integer32"
_AlaDaUNPPortMacAuthFlag_Object = MibTableColumn
alaDaUNPPortMacAuthFlag = _AlaDaUNPPortMacAuthFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 5),
    _AlaDaUNPPortMacAuthFlag_Type()
)
alaDaUNPPortMacAuthFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortMacAuthFlag.setStatus("current")


class _AlaDaUNPPortClassificationFlag_Type(Integer32):
    """Custom type alaDaUNPPortClassificationFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDaUNPPortClassificationFlag_Type.__name__ = "Integer32"
_AlaDaUNPPortClassificationFlag_Object = MibTableColumn
alaDaUNPPortClassificationFlag = _AlaDaUNPPortClassificationFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 6),
    _AlaDaUNPPortClassificationFlag_Type()
)
alaDaUNPPortClassificationFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortClassificationFlag.setStatus("current")


class _AlaDaUNPPortTrustTagStatus_Type(Integer32):
    """Custom type alaDaUNPPortTrustTagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDaUNPPortTrustTagStatus_Type.__name__ = "Integer32"
_AlaDaUNPPortTrustTagStatus_Object = MibTableColumn
alaDaUNPPortTrustTagStatus = _AlaDaUNPPortTrustTagStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 7),
    _AlaDaUNPPortTrustTagStatus_Type()
)
alaDaUNPPortTrustTagStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortTrustTagStatus.setStatus("current")


class _AlaDaUNPPortMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPPortMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPPortMCLagConfigStatus_Object = MibTableColumn
alaDaUNPPortMCLagConfigStatus = _AlaDaUNPPortMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 8),
    _AlaDaUNPPortMCLagConfigStatus_Type()
)
alaDaUNPPortMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPPortMCLagConfigStatus.setStatus("current")


class _AlaDaUNPPortCustomerDomainId_Type(Unsigned32):
    """Custom type alaDaUNPPortCustomerDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPPortCustomerDomainId_Type.__name__ = "Unsigned32"
_AlaDaUNPPortCustomerDomainId_Object = MibTableColumn
alaDaUNPPortCustomerDomainId = _AlaDaUNPPortCustomerDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 9),
    _AlaDaUNPPortCustomerDomainId_Type()
)
alaDaUNPPortCustomerDomainId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortCustomerDomainId.setStatus("current")


class _AlaDaUNPPortType_Type(Integer32):
    """Custom type alaDaUNPPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridgePort", 1),
          ("spbAccessPort", 2))
    )


_AlaDaUNPPortType_Type.__name__ = "Integer32"
_AlaDaUNPPortType_Object = MibTableColumn
alaDaUNPPortType = _AlaDaUNPPortType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 10),
    _AlaDaUNPPortType_Type()
)
alaDaUNPPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortType.setStatus("current")


class _AlaDaUNPPortPassAltSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortPassAltSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortPassAltSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortPassAltSpbProfileName_Object = MibTableColumn
alaDaUNPPortPassAltSpbProfileName = _AlaDaUNPPortPassAltSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 11),
    _AlaDaUNPPortPassAltSpbProfileName_Type()
)
alaDaUNPPortPassAltSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortPassAltSpbProfileName.setStatus("current")


class _AlaDaUNPPortDefaultSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPPortDefaultSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPPortDefaultSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPPortDefaultSpbProfileName_Object = MibTableColumn
alaDaUNPPortDefaultSpbProfileName = _AlaDaUNPPortDefaultSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 7, 1, 12),
    _AlaDaUNPPortDefaultSpbProfileName_Type()
)
alaDaUNPPortDefaultSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPPortDefaultSpbProfileName.setStatus("current")
_AlaDaUNPGlobalConfiguration_ObjectIdentity = ObjectIdentity
alaDaUNPGlobalConfiguration = _AlaDaUNPGlobalConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8)
)


class _AlaDaUNPDynamicVlanConfigFlag_Type(Integer32):
    """Custom type alaDaUNPDynamicVlanConfigFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDaUNPDynamicVlanConfigFlag_Type.__name__ = "Integer32"
_AlaDaUNPDynamicVlanConfigFlag_Object = MibScalar
alaDaUNPDynamicVlanConfigFlag = _AlaDaUNPDynamicVlanConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 1),
    _AlaDaUNPDynamicVlanConfigFlag_Type()
)
alaDaUNPDynamicVlanConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPDynamicVlanConfigFlag.setStatus("current")


class _AlaDaUNPAuthServerDownUnp_Type(SnmpAdminString):
    """Custom type alaDaUNPAuthServerDownUnp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPAuthServerDownUnp_Type.__name__ = "SnmpAdminString"
_AlaDaUNPAuthServerDownUnp_Object = MibScalar
alaDaUNPAuthServerDownUnp = _AlaDaUNPAuthServerDownUnp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 2),
    _AlaDaUNPAuthServerDownUnp_Type()
)
alaDaUNPAuthServerDownUnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownUnp.setStatus("current")


class _AlaDaUNPAuthServerDownTimeout_Type(Integer32):
    """Custom type alaDaUNPAuthServerDownTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_AlaDaUNPAuthServerDownTimeout_Type.__name__ = "Integer32"
_AlaDaUNPAuthServerDownTimeout_Object = MibScalar
alaDaUNPAuthServerDownTimeout = _AlaDaUNPAuthServerDownTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 3),
    _AlaDaUNPAuthServerDownTimeout_Type()
)
alaDaUNPAuthServerDownTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownTimeout.setUnits("Seconds")


class _AlaDaUNPDynamicVlanMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPDynamicVlanMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPDynamicVlanMCLagConfigStatus_Object = MibScalar
alaDaUNPDynamicVlanMCLagConfigStatus = _AlaDaUNPDynamicVlanMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 4),
    _AlaDaUNPDynamicVlanMCLagConfigStatus_Type()
)
alaDaUNPDynamicVlanMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPDynamicVlanMCLagConfigStatus.setStatus("current")


class _AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPAuthServerDownUNPMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Object = MibScalar
alaDaUNPAuthServerDownUNPMCLagConfigStatus = _AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 5),
    _AlaDaUNPAuthServerDownUNPMCLagConfigStatus_Type()
)
alaDaUNPAuthServerDownUNPMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownUNPMCLagConfigStatus.setStatus("current")


class _AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPAuthServerDownTimeoutMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Object = MibScalar
alaDaUNPAuthServerDownTimeoutMCLagConfigStatus = _AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 6),
    _AlaDaUNPAuthServerDownTimeoutMCLagConfigStatus_Type()
)
alaDaUNPAuthServerDownTimeoutMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPAuthServerDownTimeoutMCLagConfigStatus.setStatus("current")


class _AlaDaUNPDynamicProfileConfigFlag_Type(Integer32):
    """Custom type alaDaUNPDynamicProfileConfigFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDaUNPDynamicProfileConfigFlag_Type.__name__ = "Integer32"
_AlaDaUNPDynamicProfileConfigFlag_Object = MibScalar
alaDaUNPDynamicProfileConfigFlag = _AlaDaUNPDynamicProfileConfigFlag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 7),
    _AlaDaUNPDynamicProfileConfigFlag_Type()
)
alaDaUNPDynamicProfileConfigFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPDynamicProfileConfigFlag.setStatus("current")


class _AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPDynamicProfileConfigMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Object = MibScalar
alaDaUNPDynamicProfileConfigMCLagConfigStatus = _AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 8),
    _AlaDaUNPDynamicProfileConfigMCLagConfigStatus_Type()
)
alaDaUNPDynamicProfileConfigMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPDynamicProfileConfigMCLagConfigStatus.setStatus("current")


class _AlaDaUNPReloadVsiTypeDB_Type(Integer32):
    """Custom type alaDaUNPReloadVsiTypeDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("true", 1))
    )


_AlaDaUNPReloadVsiTypeDB_Type.__name__ = "Integer32"
_AlaDaUNPReloadVsiTypeDB_Object = MibScalar
alaDaUNPReloadVsiTypeDB = _AlaDaUNPReloadVsiTypeDB_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 8, 9),
    _AlaDaUNPReloadVsiTypeDB_Type()
)
alaDaUNPReloadVsiTypeDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDaUNPReloadVsiTypeDB.setStatus("current")
_AlaDaMacVlanUserTable_Object = MibTable
alaDaMacVlanUserTable = _AlaDaMacVlanUserTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserTable.setStatus("current")
_AlaDaMacVlanUserEntry_Object = MibTableRow
alaDaMacVlanUserEntry = _AlaDaMacVlanUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1)
)
alaDaMacVlanUserEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserIntfNum"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserMACAddress"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserVlanID"),
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserEntry.setStatus("current")
_AlaDaMacVlanUserIntfNum_Type = InterfaceIndex
_AlaDaMacVlanUserIntfNum_Object = MibTableColumn
alaDaMacVlanUserIntfNum = _AlaDaMacVlanUserIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 1),
    _AlaDaMacVlanUserIntfNum_Type()
)
alaDaMacVlanUserIntfNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserIntfNum.setStatus("current")
_AlaDaMacVlanUserMACAddress_Type = MacAddress
_AlaDaMacVlanUserMACAddress_Object = MibTableColumn
alaDaMacVlanUserMACAddress = _AlaDaMacVlanUserMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 2),
    _AlaDaMacVlanUserMACAddress_Type()
)
alaDaMacVlanUserMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserMACAddress.setStatus("current")


class _AlaDaMacVlanUserVlanID_Type(Integer32):
    """Custom type alaDaMacVlanUserVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AlaDaMacVlanUserVlanID_Type.__name__ = "Integer32"
_AlaDaMacVlanUserVlanID_Object = MibTableColumn
alaDaMacVlanUserVlanID = _AlaDaMacVlanUserVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 3),
    _AlaDaMacVlanUserVlanID_Type()
)
alaDaMacVlanUserVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaMacVlanUserVlanID.setStatus("current")


class _AlaDaMacVlanUserAuthStatus_Type(Integer32):
    """Custom type alaDaMacVlanUserAuthStatus based on Integer32"""
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
        *(("authenticated", 3),
          ("failed", 4),
          ("failedNoResources", 7),
          ("failedNoServer", 6),
          ("failedTimeout", 5),
          ("idle", 1),
          ("inProgress", 2))
    )


_AlaDaMacVlanUserAuthStatus_Type.__name__ = "Integer32"
_AlaDaMacVlanUserAuthStatus_Object = MibTableColumn
alaDaMacVlanUserAuthStatus = _AlaDaMacVlanUserAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 4),
    _AlaDaMacVlanUserAuthStatus_Type()
)
alaDaMacVlanUserAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthStatus.setStatus("current")
_AlaDaMacVlanUserIpAddressType_Type = InetAddressType
_AlaDaMacVlanUserIpAddressType_Object = MibTableColumn
alaDaMacVlanUserIpAddressType = _AlaDaMacVlanUserIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 5),
    _AlaDaMacVlanUserIpAddressType_Type()
)
alaDaMacVlanUserIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserIpAddressType.setStatus("current")
_AlaDaMacVlanUserIpAddress_Type = InetAddress
_AlaDaMacVlanUserIpAddress_Object = MibTableColumn
alaDaMacVlanUserIpAddress = _AlaDaMacVlanUserIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 6),
    _AlaDaMacVlanUserIpAddress_Type()
)
alaDaMacVlanUserIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserIpAddress.setStatus("current")
_AlaDaMacVlanUserUnpUsed_Type = SnmpAdminString
_AlaDaMacVlanUserUnpUsed_Object = MibTableColumn
alaDaMacVlanUserUnpUsed = _AlaDaMacVlanUserUnpUsed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 7),
    _AlaDaMacVlanUserUnpUsed_Type()
)
alaDaMacVlanUserUnpUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserUnpUsed.setStatus("current")
_AlaDaMacVlanUserLoginTimeStamp_Type = DateAndTime
_AlaDaMacVlanUserLoginTimeStamp_Object = MibTableColumn
alaDaMacVlanUserLoginTimeStamp = _AlaDaMacVlanUserLoginTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 8),
    _AlaDaMacVlanUserLoginTimeStamp_Type()
)
alaDaMacVlanUserLoginTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserLoginTimeStamp.setStatus("current")


class _AlaDaMacVlanUserAuthtype_Type(Integer32):
    """Custom type alaDaMacVlanUserAuthtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("macAuthentication", 0),
          ("others", 1))
    )


_AlaDaMacVlanUserAuthtype_Type.__name__ = "Integer32"
_AlaDaMacVlanUserAuthtype_Object = MibTableColumn
alaDaMacVlanUserAuthtype = _AlaDaMacVlanUserAuthtype_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 9),
    _AlaDaMacVlanUserAuthtype_Type()
)
alaDaMacVlanUserAuthtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserAuthtype.setStatus("current")
_AlaDaMacVlanUserClassificationSource_Type = AlaDaClassificationPolicyType
_AlaDaMacVlanUserClassificationSource_Object = MibTableColumn
alaDaMacVlanUserClassificationSource = _AlaDaMacVlanUserClassificationSource_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 10),
    _AlaDaMacVlanUserClassificationSource_Type()
)
alaDaMacVlanUserClassificationSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserClassificationSource.setStatus("current")


class _AlaDaMacVlanUserMCLagLearningLoc_Type(Integer32):
    """Custom type alaDaMacVlanUserMCLagLearningLoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_AlaDaMacVlanUserMCLagLearningLoc_Type.__name__ = "Integer32"
_AlaDaMacVlanUserMCLagLearningLoc_Object = MibTableColumn
alaDaMacVlanUserMCLagLearningLoc = _AlaDaMacVlanUserMCLagLearningLoc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 9, 1, 11),
    _AlaDaMacVlanUserMCLagLearningLoc_Type()
)
alaDaMacVlanUserMCLagLearningLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaMacVlanUserMCLagLearningLoc.setStatus("current")
_AlaDaUNPNotificationObjects_ObjectIdentity = ObjectIdentity
alaDaUNPNotificationObjects = _AlaDaUNPNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10)
)
_AlaDaUnpMacAddr_Type = MacAddress
_AlaDaUnpMacAddr_Object = MibScalar
alaDaUnpMacAddr = _AlaDaUnpMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 1),
    _AlaDaUnpMacAddr_Type()
)
alaDaUnpMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMacAddr.setStatus("current")
_AlaDaUnpSourceIpAddr_Type = IpAddress
_AlaDaUnpSourceIpAddr_Object = MibScalar
alaDaUnpSourceIpAddr = _AlaDaUnpSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 2),
    _AlaDaUnpSourceIpAddr_Type()
)
alaDaUnpSourceIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpSourceIpAddr.setStatus("current")
_AlaDaUnpNativeVlan_Type = Integer32
_AlaDaUnpNativeVlan_Object = MibScalar
alaDaUnpNativeVlan = _AlaDaUnpNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 3),
    _AlaDaUnpNativeVlan_Type()
)
alaDaUnpNativeVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpNativeVlan.setStatus("current")


class _AlaDaUnpVlan_Type(Integer32):
    """Custom type alaDaUnpVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUnpVlan_Type.__name__ = "Integer32"
_AlaDaUnpVlan_Object = MibScalar
alaDaUnpVlan = _AlaDaUnpVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 4),
    _AlaDaUnpVlan_Type()
)
alaDaUnpVlan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpVlan.setStatus("current")
_AlaDaUnpMCLAGId_Type = Integer32
_AlaDaUnpMCLAGId_Object = MibScalar
alaDaUnpMCLAGId = _AlaDaUnpMCLAGId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 5),
    _AlaDaUnpMCLAGId_Type()
)
alaDaUnpMCLAGId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMCLAGId.setStatus("current")


class _AlaDaUnpCommandType_Type(Integer32):
    """Custom type alaDaUnpCommandType based on Integer32"""
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
        *(("authServerTimerConfigCmd", 7),
          ("authServerUnpConfigCmd", 6),
          ("dynamicProfileConfigCmd", 10),
          ("dynamicVlanConfigCmd", 8),
          ("ipRuleConfigCmd", 4),
          ("lagConfigCmd", 9),
          ("macRangeRuleConfigCmd", 3),
          ("macRuleConfigCmd", 2),
          ("unpConfigCmd", 1),
          ("vlanTagRuleConfigCmd", 5))
    )


_AlaDaUnpCommandType_Type.__name__ = "Integer32"
_AlaDaUnpCommandType_Object = MibScalar
alaDaUnpCommandType = _AlaDaUnpCommandType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 6),
    _AlaDaUnpCommandType_Type()
)
alaDaUnpCommandType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpCommandType.setStatus("current")


class _AlaDaUnpName_Type(SnmpAdminString):
    """Custom type alaDaUnpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUnpName_Type.__name__ = "SnmpAdminString"
_AlaDaUnpName_Object = MibScalar
alaDaUnpName = _AlaDaUnpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 7),
    _AlaDaUnpName_Type()
)
alaDaUnpName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpName.setStatus("current")
_AlaDaUnpMacAddr1_Type = MacAddress
_AlaDaUnpMacAddr1_Object = MibScalar
alaDaUnpMacAddr1 = _AlaDaUnpMacAddr1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 8),
    _AlaDaUnpMacAddr1_Type()
)
alaDaUnpMacAddr1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMacAddr1.setStatus("current")
_AlaDaUnpMacAddr2_Type = MacAddress
_AlaDaUnpMacAddr2_Object = MibScalar
alaDaUnpMacAddr2 = _AlaDaUnpMacAddr2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 9),
    _AlaDaUnpMacAddr2_Type()
)
alaDaUnpMacAddr2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpMacAddr2.setStatus("current")
_AlaDaUnpIpAddr_Type = IpAddress
_AlaDaUnpIpAddr_Object = MibScalar
alaDaUnpIpAddr = _AlaDaUnpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 10),
    _AlaDaUnpIpAddr_Type()
)
alaDaUnpIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpIpAddr.setStatus("current")
_AlaDaUnpIpMask_Type = InetAddress
_AlaDaUnpIpMask_Object = MibScalar
alaDaUnpIpMask = _AlaDaUnpIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 11),
    _AlaDaUnpIpMask_Type()
)
alaDaUnpIpMask.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpIpMask.setStatus("current")


class _AlaDaUnpVlanTag_Type(Integer32):
    """Custom type alaDaUnpVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUnpVlanTag_Type.__name__ = "Integer32"
_AlaDaUnpVlanTag_Object = MibScalar
alaDaUnpVlanTag = _AlaDaUnpVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 10, 12),
    _AlaDaUnpVlanTag_Type()
)
alaDaUnpVlanTag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDaUnpVlanTag.setStatus("current")
_AlaDaUnpCustomerDomainTable_Object = MibTable
alaDaUnpCustomerDomainTable = _AlaDaUnpCustomerDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainTable.setStatus("current")
_AlaDaUnpCustomerDomainEntry_Object = MibTableRow
alaDaUnpCustomerDomainEntry = _AlaDaUnpCustomerDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 11, 1)
)
alaDaUnpCustomerDomainEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUnpCustomerDomainId"),
)
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainEntry.setStatus("current")


class _AlaDaUnpCustomerDomainId_Type(Unsigned32):
    """Custom type alaDaUnpCustomerDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUnpCustomerDomainId_Type.__name__ = "Unsigned32"
_AlaDaUnpCustomerDomainId_Object = MibTableColumn
alaDaUnpCustomerDomainId = _AlaDaUnpCustomerDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 11, 1, 1),
    _AlaDaUnpCustomerDomainId_Type()
)
alaDaUnpCustomerDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainId.setStatus("current")


class _AlaDaUnpCustomerDomainDesc_Type(SnmpAdminString):
    """Custom type alaDaUnpCustomerDomainDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AlaDaUnpCustomerDomainDesc_Type.__name__ = "SnmpAdminString"
_AlaDaUnpCustomerDomainDesc_Object = MibTableColumn
alaDaUnpCustomerDomainDesc = _AlaDaUnpCustomerDomainDesc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 11, 1, 2),
    _AlaDaUnpCustomerDomainDesc_Type()
)
alaDaUnpCustomerDomainDesc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainDesc.setStatus("current")
_AlaDaUnpCustomerDomainRowStatus_Type = RowStatus
_AlaDaUnpCustomerDomainRowStatus_Object = MibTableColumn
alaDaUnpCustomerDomainRowStatus = _AlaDaUnpCustomerDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 11, 1, 3),
    _AlaDaUnpCustomerDomainRowStatus_Type()
)
alaDaUnpCustomerDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainRowStatus.setStatus("current")
_AlaDaSpbProfileTable_Object = MibTable
alaDaSpbProfileTable = _AlaDaSpbProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaDaSpbProfileTable.setStatus("current")
_AlaDaSpbProfileEntry_Object = MibTableRow
alaDaSpbProfileEntry = _AlaDaSpbProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1)
)
alaDaSpbProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaSpbProfileName"),
)
if mibBuilder.loadTexts:
    alaDaSpbProfileEntry.setStatus("current")


class _AlaDaSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaSpbProfileName_Object = MibTableColumn
alaDaSpbProfileName = _AlaDaSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 1),
    _AlaDaSpbProfileName_Type()
)
alaDaSpbProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaSpbProfileName.setStatus("current")
_AlaDaSpbProfileEncapVal_Type = TmnxEncapVal
_AlaDaSpbProfileEncapVal_Object = MibTableColumn
alaDaSpbProfileEncapVal = _AlaDaSpbProfileEncapVal_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 2),
    _AlaDaSpbProfileEncapVal_Type()
)
alaDaSpbProfileEncapVal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileEncapVal.setStatus("current")


class _AlaDaSpbProfileQosPolicyListName_Type(SnmpAdminString):
    """Custom type alaDaSpbProfileQosPolicyListName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaSpbProfileQosPolicyListName_Type.__name__ = "SnmpAdminString"
_AlaDaSpbProfileQosPolicyListName_Object = MibTableColumn
alaDaSpbProfileQosPolicyListName = _AlaDaSpbProfileQosPolicyListName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 3),
    _AlaDaSpbProfileQosPolicyListName_Type()
)
alaDaSpbProfileQosPolicyListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileQosPolicyListName.setStatus("current")


class _AlaDaSpbProfileIsid_Type(Unsigned32):
    """Custom type alaDaSpbProfileIsid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 16777214),
    )


_AlaDaSpbProfileIsid_Type.__name__ = "Unsigned32"
_AlaDaSpbProfileIsid_Object = MibTableColumn
alaDaSpbProfileIsid = _AlaDaSpbProfileIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 4),
    _AlaDaSpbProfileIsid_Type()
)
alaDaSpbProfileIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileIsid.setStatus("current")


class _AlaDaSpbProfileBVlan_Type(Unsigned32):
    """Custom type alaDaSpbProfileBVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaSpbProfileBVlan_Type.__name__ = "Unsigned32"
_AlaDaSpbProfileBVlan_Object = MibTableColumn
alaDaSpbProfileBVlan = _AlaDaSpbProfileBVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 5),
    _AlaDaSpbProfileBVlan_Type()
)
alaDaSpbProfileBVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileBVlan.setStatus("current")
_AlaDaSpbProfileRowStatus_Type = RowStatus
_AlaDaSpbProfileRowStatus_Object = MibTableColumn
alaDaSpbProfileRowStatus = _AlaDaSpbProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 6),
    _AlaDaSpbProfileRowStatus_Type()
)
alaDaSpbProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileRowStatus.setStatus("current")


class _AlaDaSpbProfileMulticastMode_Type(Integer32):
    """Custom type alaDaSpbProfileMulticastMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("headend", 1),
          ("tandem", 2))
    )


_AlaDaSpbProfileMulticastMode_Type.__name__ = "Integer32"
_AlaDaSpbProfileMulticastMode_Object = MibTableColumn
alaDaSpbProfileMulticastMode = _AlaDaSpbProfileMulticastMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 7),
    _AlaDaSpbProfileMulticastMode_Type()
)
alaDaSpbProfileMulticastMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileMulticastMode.setStatus("current")


class _AlaDaSpbProfileSapVlanXlation_Type(Integer32):
    """Custom type alaDaSpbProfileSapVlanXlation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AlaDaSpbProfileSapVlanXlation_Type.__name__ = "Integer32"
_AlaDaSpbProfileSapVlanXlation_Object = MibTableColumn
alaDaSpbProfileSapVlanXlation = _AlaDaSpbProfileSapVlanXlation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 12, 1, 8),
    _AlaDaSpbProfileSapVlanXlation_Type()
)
alaDaSpbProfileSapVlanXlation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSpbProfileSapVlanXlation.setStatus("current")
_AlaDaUNPCustDomainEvbGpIdRuleTable_Object = MibTable
alaDaUNPCustDomainEvbGpIdRuleTable = _AlaDaUNPCustDomainEvbGpIdRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleTable.setStatus("current")
_AlaDaUNPCustDomainEvbGpIdRuleEntry_Object = MibTableRow
alaDaUNPCustDomainEvbGpIdRuleEntry = _AlaDaUNPCustDomainEvbGpIdRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 13, 1)
)
alaDaUNPCustDomainEvbGpIdRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleGroupId"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Type(Unsigned32):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Type.__name__ = "Unsigned32"
_AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId = _AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 13, 1, 1),
    _AlaDaUNPCustDomainEvbGpIdRuleCustomerDomainId_Type()
)
alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleGroupId_Type(Unsigned32):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleGroupId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainEvbGpIdRuleGroupId_Type.__name__ = "Unsigned32"
_AlaDaUNPCustDomainEvbGpIdRuleGroupId_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleGroupId = _AlaDaUNPCustDomainEvbGpIdRuleGroupId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 13, 1, 2),
    _AlaDaUNPCustDomainEvbGpIdRuleGroupId_Type()
)
alaDaUNPCustDomainEvbGpIdRuleGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleGroupId.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleVlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleVlanProfileName = _AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 13, 1, 3),
    _AlaDaUNPCustDomainEvbGpIdRuleVlanProfileName_Type()
)
alaDaUNPCustDomainEvbGpIdRuleVlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleVlanProfileName.setStatus("current")


class _AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainEvbGpIdRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleSpbProfileName = _AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 13, 1, 4),
    _AlaDaUNPCustDomainEvbGpIdRuleSpbProfileName_Type()
)
alaDaUNPCustDomainEvbGpIdRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleSpbProfileName.setStatus("current")
_AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainEvbGpIdRuleRowStatus = _AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 13, 1, 5),
    _AlaDaUNPCustDomainEvbGpIdRuleRowStatus_Type()
)
alaDaUNPCustDomainEvbGpIdRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleRowStatus.setStatus("current")
_AlaDaUNPCustDomainVlanTagRuleTable_Object = MibTable
alaDaUNPCustDomainVlanTagRuleTable = _AlaDaUNPCustDomainVlanTagRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleTable.setStatus("current")
_AlaDaUNPCustDomainVlanTagRuleEntry_Object = MibTableRow
alaDaUNPCustDomainVlanTagRuleEntry = _AlaDaUNPCustDomainVlanTagRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1)
)
alaDaUNPCustDomainVlanTagRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleVlan"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainVlanTagRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainVlanTagRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainVlanTagRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleDomainId = _AlaDaUNPCustDomainVlanTagRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1, 1),
    _AlaDaUNPCustDomainVlanTagRuleDomainId_Type()
)
alaDaUNPCustDomainVlanTagRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleDomainId.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleVlan_Type(Integer32):
    """Custom type alaDaUNPCustDomainVlanTagRuleVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AlaDaUNPCustDomainVlanTagRuleVlan_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainVlanTagRuleVlan_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleVlan = _AlaDaUNPCustDomainVlanTagRuleVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1, 2),
    _AlaDaUNPCustDomainVlanTagRuleVlan_Type()
)
alaDaUNPCustDomainVlanTagRuleVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleVlan.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleVlanProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleVlanProfileName = _AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1, 3),
    _AlaDaUNPCustDomainVlanTagRuleVlanProfileName_Type()
)
alaDaUNPCustDomainVlanTagRuleVlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleVlanProfileName.setStatus("current")
_AlaDaUNPCustDomainVlanTagRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainVlanTagRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleRowStatus = _AlaDaUNPCustDomainVlanTagRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1, 4),
    _AlaDaUNPCustDomainVlanTagRuleRowStatus_Type()
)
alaDaUNPCustDomainVlanTagRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus = _AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1, 5),
    _AlaDaUNPCustDomainVlanTagRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainVlanTagRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleSpbProfileName = _AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1, 6),
    _AlaDaUNPCustDomainVlanTagRuleSpbProfileName_Type()
)
alaDaUNPCustDomainVlanTagRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleSpbProfileName.setStatus("current")


class _AlaDaUNPCustDomainVlanTagRuleTagPosition_Type(Integer32):
    """Custom type alaDaUNPCustDomainVlanTagRuleTagPosition based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("innerTag", 2),
          ("notApplicable", 0),
          ("outerTag", 1))
    )


_AlaDaUNPCustDomainVlanTagRuleTagPosition_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainVlanTagRuleTagPosition_Object = MibTableColumn
alaDaUNPCustDomainVlanTagRuleTagPosition = _AlaDaUNPCustDomainVlanTagRuleTagPosition_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 14, 1, 7),
    _AlaDaUNPCustDomainVlanTagRuleTagPosition_Type()
)
alaDaUNPCustDomainVlanTagRuleTagPosition.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleTagPosition.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleTable_Object = MibTable
alaDaUNPCustDomainIpNetRuleTable = _AlaDaUNPCustDomainIpNetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleTable.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleEntry_Object = MibTableRow
alaDaUNPCustDomainIpNetRuleEntry = _AlaDaUNPCustDomainIpNetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1)
)
alaDaUNPCustDomainIpNetRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleAddrType"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleAddr"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleMask"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainIpNetRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainIpNetRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainIpNetRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleDomainId = _AlaDaUNPCustDomainIpNetRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 1),
    _AlaDaUNPCustDomainIpNetRuleDomainId_Type()
)
alaDaUNPCustDomainIpNetRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleDomainId.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleAddrType_Type = InetAddressType
_AlaDaUNPCustDomainIpNetRuleAddrType_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleAddrType = _AlaDaUNPCustDomainIpNetRuleAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 2),
    _AlaDaUNPCustDomainIpNetRuleAddrType_Type()
)
alaDaUNPCustDomainIpNetRuleAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleAddrType.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleAddr_Type(InetAddress):
    """Custom type alaDaUNPCustDomainIpNetRuleAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPCustDomainIpNetRuleAddr_Type.__name__ = "InetAddress"
_AlaDaUNPCustDomainIpNetRuleAddr_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleAddr = _AlaDaUNPCustDomainIpNetRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 3),
    _AlaDaUNPCustDomainIpNetRuleAddr_Type()
)
alaDaUNPCustDomainIpNetRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleAddr.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleMask_Type(InetAddress):
    """Custom type alaDaUNPCustDomainIpNetRuleMask based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDaUNPCustDomainIpNetRuleMask_Type.__name__ = "InetAddress"
_AlaDaUNPCustDomainIpNetRuleMask_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleMask = _AlaDaUNPCustDomainIpNetRuleMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 4),
    _AlaDaUNPCustDomainIpNetRuleMask_Type()
)
alaDaUNPCustDomainIpNetRuleMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleMask.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainIpNetRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleProfileName_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleProfileName = _AlaDaUNPCustDomainIpNetRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 5),
    _AlaDaUNPCustDomainIpNetRuleProfileName_Type()
)
alaDaUNPCustDomainIpNetRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleProfileName.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainIpNetRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainIpNetRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainIpNetRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleVlanTag = _AlaDaUNPCustDomainIpNetRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 6),
    _AlaDaUNPCustDomainIpNetRuleVlanTag_Type()
)
alaDaUNPCustDomainIpNetRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleVlanTag.setStatus("current")
_AlaDaUNPCustDomainIpNetRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainIpNetRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleRowStatus = _AlaDaUNPCustDomainIpNetRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 7),
    _AlaDaUNPCustDomainIpNetRuleRowStatus_Type()
)
alaDaUNPCustDomainIpNetRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainIpNetRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleMCLagConfigStatus = _AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 8),
    _AlaDaUNPCustDomainIpNetRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainIpNetRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainIpNetRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainIpNetRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainIpNetRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainIpNetRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainIpNetRuleSpbProfileName = _AlaDaUNPCustDomainIpNetRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 15, 1, 9),
    _AlaDaUNPCustDomainIpNetRuleSpbProfileName_Type()
)
alaDaUNPCustDomainIpNetRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleSpbProfileName.setStatus("current")
_AlaDaUNPCustDomainMacRuleTable_Object = MibTable
alaDaUNPCustDomainMacRuleTable = _AlaDaUNPCustDomainMacRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleTable.setStatus("current")
_AlaDaUNPCustDomainMacRuleEntry_Object = MibTableRow
alaDaUNPCustDomainMacRuleEntry = _AlaDaUNPCustDomainMacRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1)
)
alaDaUNPCustDomainMacRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainMacRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainMacRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainMacRuleDomainId = _AlaDaUNPCustDomainMacRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1, 1),
    _AlaDaUNPCustDomainMacRuleDomainId_Type()
)
alaDaUNPCustDomainMacRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleDomainId.setStatus("current")
_AlaDaUNPCustDomainMacRuleAddr_Type = MacAddress
_AlaDaUNPCustDomainMacRuleAddr_Object = MibTableColumn
alaDaUNPCustDomainMacRuleAddr = _AlaDaUNPCustDomainMacRuleAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1, 2),
    _AlaDaUNPCustDomainMacRuleAddr_Type()
)
alaDaUNPCustDomainMacRuleAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleAddr.setStatus("current")


class _AlaDaUNPCustDomainMacRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRuleProfileName = _AlaDaUNPCustDomainMacRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1, 3),
    _AlaDaUNPCustDomainMacRuleProfileName_Type()
)
alaDaUNPCustDomainMacRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleProfileName.setStatus("current")


class _AlaDaUNPCustDomainMacRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainMacRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainMacRuleVlanTag = _AlaDaUNPCustDomainMacRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1, 4),
    _AlaDaUNPCustDomainMacRuleVlanTag_Type()
)
alaDaUNPCustDomainMacRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleVlanTag.setStatus("current")
_AlaDaUNPCustDomainMacRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainMacRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRuleRowStatus = _AlaDaUNPCustDomainMacRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1, 5),
    _AlaDaUNPCustDomainMacRuleRowStatus_Type()
)
alaDaUNPCustDomainMacRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainMacRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRuleMCLagConfigStatus = _AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1, 6),
    _AlaDaUNPCustDomainMacRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainMacRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaUNPCustDomainMacRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRuleSpbProfileName = _AlaDaUNPCustDomainMacRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 16, 1, 7),
    _AlaDaUNPCustDomainMacRuleSpbProfileName_Type()
)
alaDaUNPCustDomainMacRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleSpbProfileName.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleTable_Object = MibTable
alaDaUNPCustDomainMacRangeRuleTable = _AlaDaUNPCustDomainMacRangeRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17)
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleTable.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleEntry_Object = MibTableRow
alaDaUNPCustDomainMacRangeRuleEntry = _AlaDaUNPCustDomainMacRangeRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1)
)
alaDaUNPCustDomainMacRangeRuleEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleDomainId"),
    (0, "ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleLoAddr"),
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleEntry.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleDomainId_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRangeRuleDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AlaDaUNPCustDomainMacRangeRuleDomainId_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRangeRuleDomainId_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleDomainId = _AlaDaUNPCustDomainMacRangeRuleDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 1),
    _AlaDaUNPCustDomainMacRangeRuleDomainId_Type()
)
alaDaUNPCustDomainMacRangeRuleDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleDomainId.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleLoAddr_Type = MacAddress
_AlaDaUNPCustDomainMacRangeRuleLoAddr_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleLoAddr = _AlaDaUNPCustDomainMacRangeRuleLoAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 2),
    _AlaDaUNPCustDomainMacRangeRuleLoAddr_Type()
)
alaDaUNPCustDomainMacRangeRuleLoAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleLoAddr.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleHiAddr_Type = MacAddress
_AlaDaUNPCustDomainMacRangeRuleHiAddr_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleHiAddr = _AlaDaUNPCustDomainMacRangeRuleHiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 3),
    _AlaDaUNPCustDomainMacRangeRuleHiAddr_Type()
)
alaDaUNPCustDomainMacRangeRuleHiAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleHiAddr.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleProfileName = _AlaDaUNPCustDomainMacRangeRuleProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 4),
    _AlaDaUNPCustDomainMacRangeRuleProfileName_Type()
)
alaDaUNPCustDomainMacRangeRuleProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleProfileName.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleVlanTag_Type(Integer32):
    """Custom type alaDaUNPCustDomainMacRangeRuleVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDaUNPCustDomainMacRangeRuleVlanTag_Type.__name__ = "Integer32"
_AlaDaUNPCustDomainMacRangeRuleVlanTag_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleVlanTag = _AlaDaUNPCustDomainMacRangeRuleVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 5),
    _AlaDaUNPCustDomainMacRangeRuleVlanTag_Type()
)
alaDaUNPCustDomainMacRangeRuleVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleVlanTag.setStatus("current")
_AlaDaUNPCustDomainMacRangeRuleRowStatus_Type = RowStatus
_AlaDaUNPCustDomainMacRangeRuleRowStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleRowStatus = _AlaDaUNPCustDomainMacRangeRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 6),
    _AlaDaUNPCustDomainMacRangeRuleRowStatus_Type()
)
alaDaUNPCustDomainMacRangeRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleRowStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Type(AlaMultiChassisConfigStatus):
    """Custom type alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus based on AlaMultiChassisConfigStatus"""


_AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus = _AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 7),
    _AlaDaUNPCustDomainMacRangeRuleMCLagConfigStatus_Type()
)
alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus.setStatus("current")


class _AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Type(SnmpAdminString):
    """Custom type alaDaUNPCustDomainMacRangeRuleSpbProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Object = MibTableColumn
alaDaUNPCustDomainMacRangeRuleSpbProfileName = _AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 17, 1, 8),
    _AlaDaUNPCustDomainMacRangeRuleSpbProfileName_Type()
)
alaDaUNPCustDomainMacRangeRuleSpbProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeRuleSpbProfileName.setStatus("current")
_AlaDaSaaProfileTable_Object = MibTable
alaDaSaaProfileTable = _AlaDaSaaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 18)
)
if mibBuilder.loadTexts:
    alaDaSaaProfileTable.setStatus("current")
_AlaDaSaaProfileEntry_Object = MibTableRow
alaDaSaaProfileEntry = _AlaDaSaaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 18, 1)
)
alaDaSaaProfileEntry.setIndexNames(
    (0, "ALCATEL-IND1-DA-MIB", "alaDaSaaProfileName"),
)
if mibBuilder.loadTexts:
    alaDaSaaProfileEntry.setStatus("current")


class _AlaDaSaaProfileName_Type(SnmpAdminString):
    """Custom type alaDaSaaProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaDaSaaProfileName_Type.__name__ = "SnmpAdminString"
_AlaDaSaaProfileName_Object = MibTableColumn
alaDaSaaProfileName = _AlaDaSaaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 18, 1, 1),
    _AlaDaSaaProfileName_Type()
)
alaDaSaaProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDaSaaProfileName.setStatus("current")


class _AlaDaSaaProfileLatencyThreshold_Type(Integer32):
    """Custom type alaDaSaaProfileLatencyThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AlaDaSaaProfileLatencyThreshold_Type.__name__ = "Integer32"
_AlaDaSaaProfileLatencyThreshold_Object = MibTableColumn
alaDaSaaProfileLatencyThreshold = _AlaDaSaaProfileLatencyThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 18, 1, 4),
    _AlaDaSaaProfileLatencyThreshold_Type()
)
alaDaSaaProfileLatencyThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSaaProfileLatencyThreshold.setStatus("current")


class _AlaDaSaaProfileJitterThreshold_Type(Integer32):
    """Custom type alaDaSaaProfileJitterThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_AlaDaSaaProfileJitterThreshold_Type.__name__ = "Integer32"
_AlaDaSaaProfileJitterThreshold_Object = MibTableColumn
alaDaSaaProfileJitterThreshold = _AlaDaSaaProfileJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 18, 1, 5),
    _AlaDaSaaProfileJitterThreshold_Type()
)
alaDaSaaProfileJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSaaProfileJitterThreshold.setStatus("current")
_AlaDaSaaProfileRowStatus_Type = RowStatus
_AlaDaSaaProfileRowStatus_Object = MibTableColumn
alaDaSaaProfileRowStatus = _AlaDaSaaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 1, 18, 1, 6),
    _AlaDaSaaProfileRowStatus_Type()
)
alaDaSaaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDaSaaProfileRowStatus.setStatus("current")
_AlaIND1DaMIBConformance_ObjectIdentity = ObjectIdentity
alaIND1DaMIBConformance = _AlaIND1DaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBConformance.setStatus("current")
_AlaIND1DaMIBGroups_ObjectIdentity = ObjectIdentity
alaIND1DaMIBGroups = _AlaIND1DaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBGroups.setStatus("current")

# Managed Objects groups

alaDaUserNetProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 1)
)
alaDaUserNetProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileVlanID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileQosPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUserNetProfileSaaProfileName"))
)
if mibBuilder.loadTexts:
    alaDaUserNetProfileGroup.setStatus("current")

alaDaUNPIpNetRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 2)
)
alaDaUNPIpNetRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPIpNetRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPIpNetRuleGroup.setStatus("current")

alaDaUNPMacRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 3)
)
alaDaUNPMacRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacRuleGroup.setStatus("current")

alaDaUNPMacRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 4)
)
alaDaUNPMacRangeGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleHiAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPMacRangeRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPMacRangeGroup.setStatus("current")

alaDaUNPVlanTagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 5)
)
alaDaUNPVlanTagGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPVlanTagRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPVlanTagGroup.setStatus("current")

alaDaMacUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 6)
)
alaDaMacUserGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaMacUserVlanID"),
        ("ALCATEL-IND1-DA-MIB", "alaDaAuthenticationStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserUnpUsed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserLoginTimeStamp"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserAuthtype"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacUserClassificationSource"))
)
if mibBuilder.loadTexts:
    alaDaMacUserGroup.setStatus("current")

alaDaUNPPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 7)
)
alaDaUNPPortGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDefaultProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortPassAltProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMacAuthFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortClassificationFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortTrustTagStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPPortGroup.setStatus("current")

alaDaUNPGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 8)
)
alaDaUNPGlobalGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicVlanConfigFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownUnp"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownTimeout"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicVlanMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownUNPMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPAuthServerDownTimeoutMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicProfileConfigFlag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPDynamicProfileConfigMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPReloadVsiTypeDB"))
)
if mibBuilder.loadTexts:
    alaDaUNPGlobalGroup.setStatus("current")

alaDaNotificationObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 9)
)
alaDaNotificationObjectGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpSourceIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpNativeVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMCLAGId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpCommandType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpMask"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlanTag"))
)
if mibBuilder.loadTexts:
    alaDaNotificationObjectGroup.setStatus("current")

alaDaMacVlanUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 11)
)
alaDaMacVlanUserGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserIpAddressType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserIpAddress"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserUnpUsed"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserLoginTimeStamp"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserAuthtype"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserClassificationSource"),
        ("ALCATEL-IND1-DA-MIB", "alaDaMacVlanUserMCLagLearningLoc"))
)
if mibBuilder.loadTexts:
    alaDaMacVlanUserGroup.setStatus("current")

alaDaUnpCustomerDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 12)
)
alaDaUnpCustomerDomainGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpCustomerDomainDesc"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpCustomerDomainRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaUnpCustomerDomainGroup.setStatus("current")

alaDaSpbProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 13)
)
alaDaSpbProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileEncapVal"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileQosPolicyListName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileIsid"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileBVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileMulticastMode"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSpbProfileSapVlanXlation"))
)
if mibBuilder.loadTexts:
    alaDaSpbProfileGroup.setStatus("current")

alaDaUNPCustDomainEvbGpIdRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 14)
)
alaDaUNPCustDomainEvbGpIdRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleVlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainEvbGpIdRuleSpbProfileName"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainEvbGpIdRuleGroup.setStatus("current")

alaDaUNPCustDomainVlanTagRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 15)
)
alaDaUNPCustDomainVlanTagRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleVlanProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainVlanTagRuleTagPosition"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainVlanTagRuleGroup.setStatus("current")

alaDaUNPCustDomainIpNetRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 16)
)
alaDaUNPCustDomainIpNetRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainIpNetRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainIpNetRuleGroup.setStatus("current")

alaDaUNPCustDomainMacRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 17)
)
alaDaUNPCustDomainMacRuleGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRuleGroup.setStatus("current")

alaDaUNPCustDomainMacRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 18)
)
alaDaUNPCustDomainMacRangeGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleHiAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleRowStatus"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus"))
)
if mibBuilder.loadTexts:
    alaDaUNPCustDomainMacRangeGroup.setStatus("current")

alaDaUNPGroupObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 19)
)
alaDaUNPGroupObjects.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUNPPortCustomerDomainId"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortPassAltSpbProfileName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUNPPortDefaultSpbProfileName"))
)
if mibBuilder.loadTexts:
    alaDaUNPGroupObjects.setStatus("current")

alaDaSaaProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 20)
)
alaDaSaaProfileGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaSaaProfileLatencyThreshold"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSaaProfileJitterThreshold"),
        ("ALCATEL-IND1-DA-MIB", "alaDaSaaProfileRowStatus"))
)
if mibBuilder.loadTexts:
    alaDaSaaProfileGroup.setStatus("current")


# Notification objects

unpMcLagMacIgnored = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 0, 1)
)
unpMcLagMacIgnored.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpSourceIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpNativeVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlan"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMCLAGId"))
)
if mibBuilder.loadTexts:
    unpMcLagMacIgnored.setStatus(
        "current"
    )

unpMcLagConfigInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 0, 2)
)
unpMcLagConfigInconsistency.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "alaDaUnpCommandType"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpName"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr1"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMacAddr2"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpAddr"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpIpMask"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpVlanTag"),
        ("ALCATEL-IND1-DA-MIB", "alaDaUnpMCLAGId"))
)
if mibBuilder.loadTexts:
    unpMcLagConfigInconsistency.setStatus(
        "current"
    )


# Notifications groups

alaDaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 1, 10)
)
alaDaNotificationsGroup.setObjects(
      *(("ALCATEL-IND1-DA-MIB", "unpMcLagMacIgnored"),
        ("ALCATEL-IND1-DA-MIB", "unpMcLagConfigInconsistency"))
)
if mibBuilder.loadTexts:
    alaDaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIND1DaMIBCompliances = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 63, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alaIND1DaMIBCompliances.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DA-MIB",
    **{"AlaDaClassificationPolicyType": AlaDaClassificationPolicyType,
       "AlaDaAuthenticationType": AlaDaAuthenticationType,
       "AlaDaAuthenticationResult": AlaDaAuthenticationResult,
       "AlaDaMacLearntState": AlaDaMacLearntState,
       "AlaMultiChassisConfigStatus": AlaMultiChassisConfigStatus,
       "alcatelIND1DaMIB": alcatelIND1DaMIB,
       "alaIND1DaMIBNotifications": alaIND1DaMIBNotifications,
       "unpMcLagMacIgnored": unpMcLagMacIgnored,
       "unpMcLagConfigInconsistency": unpMcLagConfigInconsistency,
       "alaIND1DaMIBObjects": alaIND1DaMIBObjects,
       "alaDaUserNetProfileTable": alaDaUserNetProfileTable,
       "alaDaUserNetProfileEntry": alaDaUserNetProfileEntry,
       "alaDaUserNetProfileName": alaDaUserNetProfileName,
       "alaDaUserNetProfileVlanID": alaDaUserNetProfileVlanID,
       "alaDaUserNetProfileRowStatus": alaDaUserNetProfileRowStatus,
       "alaDaUserNetProfileQosPolicyListName": alaDaUserNetProfileQosPolicyListName,
       "alaDaUserNetProfileMCLagConfigStatus": alaDaUserNetProfileMCLagConfigStatus,
       "alaDaUserNetProfileSaaProfileName": alaDaUserNetProfileSaaProfileName,
       "alaDaUNPIpNetRuleTable": alaDaUNPIpNetRuleTable,
       "alaDaUNPIpNetRuleEntry": alaDaUNPIpNetRuleEntry,
       "alaDaUNPIpNetRuleAddrType": alaDaUNPIpNetRuleAddrType,
       "alaDaUNPIpNetRuleAddr": alaDaUNPIpNetRuleAddr,
       "alaDaUNPIpNetRuleMask": alaDaUNPIpNetRuleMask,
       "alaDaUNPIpNetRuleProfileName": alaDaUNPIpNetRuleProfileName,
       "alaDaUNPIpNetRuleVlanTag": alaDaUNPIpNetRuleVlanTag,
       "alaDaUNPIpNetRuleRowStatus": alaDaUNPIpNetRuleRowStatus,
       "alaDaUNPIpNetRuleMCLagConfigStatus": alaDaUNPIpNetRuleMCLagConfigStatus,
       "alaDaUNPMacRuleTable": alaDaUNPMacRuleTable,
       "alaDaUNPMacRuleEntry": alaDaUNPMacRuleEntry,
       "alaDaUNPMacRuleAddr": alaDaUNPMacRuleAddr,
       "alaDaUNPMacRuleProfileName": alaDaUNPMacRuleProfileName,
       "alaDaUNPMacRuleVlanTag": alaDaUNPMacRuleVlanTag,
       "alaDaUNPMacRuleRowStatus": alaDaUNPMacRuleRowStatus,
       "alaDaUNPMacRuleMCLagConfigStatus": alaDaUNPMacRuleMCLagConfigStatus,
       "alaDaUNPMacRangeRuleTable": alaDaUNPMacRangeRuleTable,
       "alaDaUNPMacRangeRuleEntry": alaDaUNPMacRangeRuleEntry,
       "alaDaUNPMacRangeRuleLoAddr": alaDaUNPMacRangeRuleLoAddr,
       "alaDaUNPMacRangeRuleHiAddr": alaDaUNPMacRangeRuleHiAddr,
       "alaDaUNPMacRangeRuleProfileName": alaDaUNPMacRangeRuleProfileName,
       "alaDaUNPMacRangeRuleVlanTag": alaDaUNPMacRangeRuleVlanTag,
       "alaDaUNPMacRangeRuleRowStatus": alaDaUNPMacRangeRuleRowStatus,
       "alaDaUNPMacRangeRuleMCLagConfigStatus": alaDaUNPMacRangeRuleMCLagConfigStatus,
       "alaDaUNPVlanTagRuleTable": alaDaUNPVlanTagRuleTable,
       "alaDaUNPVlanTagRuleEntry": alaDaUNPVlanTagRuleEntry,
       "alaDaUNPVlanTagRuleVlan": alaDaUNPVlanTagRuleVlan,
       "alaDaUNPVlanTagRuleProfileName": alaDaUNPVlanTagRuleProfileName,
       "alaDaUNPVlanTagRuleRowStatus": alaDaUNPVlanTagRuleRowStatus,
       "alaDaUNPVlanTagRuleMCLagConfigStatus": alaDaUNPVlanTagRuleMCLagConfigStatus,
       "alaDaMacUserTable": alaDaMacUserTable,
       "alaDaMacUserEntry": alaDaMacUserEntry,
       "alaDaMacUserIntfNum": alaDaMacUserIntfNum,
       "alaDaMacUserMACAddress": alaDaMacUserMACAddress,
       "alaDaMacUserVlanID": alaDaMacUserVlanID,
       "alaDaAuthenticationStatus": alaDaAuthenticationStatus,
       "alaDaMacUserIpAddress": alaDaMacUserIpAddress,
       "alaDaMacUserUnpUsed": alaDaMacUserUnpUsed,
       "alaDaMacUserLoginTimeStamp": alaDaMacUserLoginTimeStamp,
       "alaDaMacUserAuthtype": alaDaMacUserAuthtype,
       "alaDaMacUserClassificationSource": alaDaMacUserClassificationSource,
       "alaDaUNPPortTable": alaDaUNPPortTable,
       "alaDaUNPPortEntry": alaDaUNPPortEntry,
       "alaDaUNPPortIfIndex": alaDaUNPPortIfIndex,
       "alaDaUNPPortDefaultProfileName": alaDaUNPPortDefaultProfileName,
       "alaDaUNPPortPassAltProfileName": alaDaUNPPortPassAltProfileName,
       "alaDaUNPPortRowStatus": alaDaUNPPortRowStatus,
       "alaDaUNPPortMacAuthFlag": alaDaUNPPortMacAuthFlag,
       "alaDaUNPPortClassificationFlag": alaDaUNPPortClassificationFlag,
       "alaDaUNPPortTrustTagStatus": alaDaUNPPortTrustTagStatus,
       "alaDaUNPPortMCLagConfigStatus": alaDaUNPPortMCLagConfigStatus,
       "alaDaUNPPortCustomerDomainId": alaDaUNPPortCustomerDomainId,
       "alaDaUNPPortType": alaDaUNPPortType,
       "alaDaUNPPortPassAltSpbProfileName": alaDaUNPPortPassAltSpbProfileName,
       "alaDaUNPPortDefaultSpbProfileName": alaDaUNPPortDefaultSpbProfileName,
       "alaDaUNPGlobalConfiguration": alaDaUNPGlobalConfiguration,
       "alaDaUNPDynamicVlanConfigFlag": alaDaUNPDynamicVlanConfigFlag,
       "alaDaUNPAuthServerDownUnp": alaDaUNPAuthServerDownUnp,
       "alaDaUNPAuthServerDownTimeout": alaDaUNPAuthServerDownTimeout,
       "alaDaUNPDynamicVlanMCLagConfigStatus": alaDaUNPDynamicVlanMCLagConfigStatus,
       "alaDaUNPAuthServerDownUNPMCLagConfigStatus": alaDaUNPAuthServerDownUNPMCLagConfigStatus,
       "alaDaUNPAuthServerDownTimeoutMCLagConfigStatus": alaDaUNPAuthServerDownTimeoutMCLagConfigStatus,
       "alaDaUNPDynamicProfileConfigFlag": alaDaUNPDynamicProfileConfigFlag,
       "alaDaUNPDynamicProfileConfigMCLagConfigStatus": alaDaUNPDynamicProfileConfigMCLagConfigStatus,
       "alaDaUNPReloadVsiTypeDB": alaDaUNPReloadVsiTypeDB,
       "alaDaMacVlanUserTable": alaDaMacVlanUserTable,
       "alaDaMacVlanUserEntry": alaDaMacVlanUserEntry,
       "alaDaMacVlanUserIntfNum": alaDaMacVlanUserIntfNum,
       "alaDaMacVlanUserMACAddress": alaDaMacVlanUserMACAddress,
       "alaDaMacVlanUserVlanID": alaDaMacVlanUserVlanID,
       "alaDaMacVlanUserAuthStatus": alaDaMacVlanUserAuthStatus,
       "alaDaMacVlanUserIpAddressType": alaDaMacVlanUserIpAddressType,
       "alaDaMacVlanUserIpAddress": alaDaMacVlanUserIpAddress,
       "alaDaMacVlanUserUnpUsed": alaDaMacVlanUserUnpUsed,
       "alaDaMacVlanUserLoginTimeStamp": alaDaMacVlanUserLoginTimeStamp,
       "alaDaMacVlanUserAuthtype": alaDaMacVlanUserAuthtype,
       "alaDaMacVlanUserClassificationSource": alaDaMacVlanUserClassificationSource,
       "alaDaMacVlanUserMCLagLearningLoc": alaDaMacVlanUserMCLagLearningLoc,
       "alaDaUNPNotificationObjects": alaDaUNPNotificationObjects,
       "alaDaUnpMacAddr": alaDaUnpMacAddr,
       "alaDaUnpSourceIpAddr": alaDaUnpSourceIpAddr,
       "alaDaUnpNativeVlan": alaDaUnpNativeVlan,
       "alaDaUnpVlan": alaDaUnpVlan,
       "alaDaUnpMCLAGId": alaDaUnpMCLAGId,
       "alaDaUnpCommandType": alaDaUnpCommandType,
       "alaDaUnpName": alaDaUnpName,
       "alaDaUnpMacAddr1": alaDaUnpMacAddr1,
       "alaDaUnpMacAddr2": alaDaUnpMacAddr2,
       "alaDaUnpIpAddr": alaDaUnpIpAddr,
       "alaDaUnpIpMask": alaDaUnpIpMask,
       "alaDaUnpVlanTag": alaDaUnpVlanTag,
       "alaDaUnpCustomerDomainTable": alaDaUnpCustomerDomainTable,
       "alaDaUnpCustomerDomainEntry": alaDaUnpCustomerDomainEntry,
       "alaDaUnpCustomerDomainId": alaDaUnpCustomerDomainId,
       "alaDaUnpCustomerDomainDesc": alaDaUnpCustomerDomainDesc,
       "alaDaUnpCustomerDomainRowStatus": alaDaUnpCustomerDomainRowStatus,
       "alaDaSpbProfileTable": alaDaSpbProfileTable,
       "alaDaSpbProfileEntry": alaDaSpbProfileEntry,
       "alaDaSpbProfileName": alaDaSpbProfileName,
       "alaDaSpbProfileEncapVal": alaDaSpbProfileEncapVal,
       "alaDaSpbProfileQosPolicyListName": alaDaSpbProfileQosPolicyListName,
       "alaDaSpbProfileIsid": alaDaSpbProfileIsid,
       "alaDaSpbProfileBVlan": alaDaSpbProfileBVlan,
       "alaDaSpbProfileRowStatus": alaDaSpbProfileRowStatus,
       "alaDaSpbProfileMulticastMode": alaDaSpbProfileMulticastMode,
       "alaDaSpbProfileSapVlanXlation": alaDaSpbProfileSapVlanXlation,
       "alaDaUNPCustDomainEvbGpIdRuleTable": alaDaUNPCustDomainEvbGpIdRuleTable,
       "alaDaUNPCustDomainEvbGpIdRuleEntry": alaDaUNPCustDomainEvbGpIdRuleEntry,
       "alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId": alaDaUNPCustDomainEvbGpIdRuleCustomerDomainId,
       "alaDaUNPCustDomainEvbGpIdRuleGroupId": alaDaUNPCustDomainEvbGpIdRuleGroupId,
       "alaDaUNPCustDomainEvbGpIdRuleVlanProfileName": alaDaUNPCustDomainEvbGpIdRuleVlanProfileName,
       "alaDaUNPCustDomainEvbGpIdRuleSpbProfileName": alaDaUNPCustDomainEvbGpIdRuleSpbProfileName,
       "alaDaUNPCustDomainEvbGpIdRuleRowStatus": alaDaUNPCustDomainEvbGpIdRuleRowStatus,
       "alaDaUNPCustDomainVlanTagRuleTable": alaDaUNPCustDomainVlanTagRuleTable,
       "alaDaUNPCustDomainVlanTagRuleEntry": alaDaUNPCustDomainVlanTagRuleEntry,
       "alaDaUNPCustDomainVlanTagRuleDomainId": alaDaUNPCustDomainVlanTagRuleDomainId,
       "alaDaUNPCustDomainVlanTagRuleVlan": alaDaUNPCustDomainVlanTagRuleVlan,
       "alaDaUNPCustDomainVlanTagRuleVlanProfileName": alaDaUNPCustDomainVlanTagRuleVlanProfileName,
       "alaDaUNPCustDomainVlanTagRuleRowStatus": alaDaUNPCustDomainVlanTagRuleRowStatus,
       "alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus": alaDaUNPCustDomainVlanTagRuleMCLagConfigStatus,
       "alaDaUNPCustDomainVlanTagRuleSpbProfileName": alaDaUNPCustDomainVlanTagRuleSpbProfileName,
       "alaDaUNPCustDomainVlanTagRuleTagPosition": alaDaUNPCustDomainVlanTagRuleTagPosition,
       "alaDaUNPCustDomainIpNetRuleTable": alaDaUNPCustDomainIpNetRuleTable,
       "alaDaUNPCustDomainIpNetRuleEntry": alaDaUNPCustDomainIpNetRuleEntry,
       "alaDaUNPCustDomainIpNetRuleDomainId": alaDaUNPCustDomainIpNetRuleDomainId,
       "alaDaUNPCustDomainIpNetRuleAddrType": alaDaUNPCustDomainIpNetRuleAddrType,
       "alaDaUNPCustDomainIpNetRuleAddr": alaDaUNPCustDomainIpNetRuleAddr,
       "alaDaUNPCustDomainIpNetRuleMask": alaDaUNPCustDomainIpNetRuleMask,
       "alaDaUNPCustDomainIpNetRuleProfileName": alaDaUNPCustDomainIpNetRuleProfileName,
       "alaDaUNPCustDomainIpNetRuleVlanTag": alaDaUNPCustDomainIpNetRuleVlanTag,
       "alaDaUNPCustDomainIpNetRuleRowStatus": alaDaUNPCustDomainIpNetRuleRowStatus,
       "alaDaUNPCustDomainIpNetRuleMCLagConfigStatus": alaDaUNPCustDomainIpNetRuleMCLagConfigStatus,
       "alaDaUNPCustDomainIpNetRuleSpbProfileName": alaDaUNPCustDomainIpNetRuleSpbProfileName,
       "alaDaUNPCustDomainMacRuleTable": alaDaUNPCustDomainMacRuleTable,
       "alaDaUNPCustDomainMacRuleEntry": alaDaUNPCustDomainMacRuleEntry,
       "alaDaUNPCustDomainMacRuleDomainId": alaDaUNPCustDomainMacRuleDomainId,
       "alaDaUNPCustDomainMacRuleAddr": alaDaUNPCustDomainMacRuleAddr,
       "alaDaUNPCustDomainMacRuleProfileName": alaDaUNPCustDomainMacRuleProfileName,
       "alaDaUNPCustDomainMacRuleVlanTag": alaDaUNPCustDomainMacRuleVlanTag,
       "alaDaUNPCustDomainMacRuleRowStatus": alaDaUNPCustDomainMacRuleRowStatus,
       "alaDaUNPCustDomainMacRuleMCLagConfigStatus": alaDaUNPCustDomainMacRuleMCLagConfigStatus,
       "alaDaUNPCustDomainMacRuleSpbProfileName": alaDaUNPCustDomainMacRuleSpbProfileName,
       "alaDaUNPCustDomainMacRangeRuleTable": alaDaUNPCustDomainMacRangeRuleTable,
       "alaDaUNPCustDomainMacRangeRuleEntry": alaDaUNPCustDomainMacRangeRuleEntry,
       "alaDaUNPCustDomainMacRangeRuleDomainId": alaDaUNPCustDomainMacRangeRuleDomainId,
       "alaDaUNPCustDomainMacRangeRuleLoAddr": alaDaUNPCustDomainMacRangeRuleLoAddr,
       "alaDaUNPCustDomainMacRangeRuleHiAddr": alaDaUNPCustDomainMacRangeRuleHiAddr,
       "alaDaUNPCustDomainMacRangeRuleProfileName": alaDaUNPCustDomainMacRangeRuleProfileName,
       "alaDaUNPCustDomainMacRangeRuleVlanTag": alaDaUNPCustDomainMacRangeRuleVlanTag,
       "alaDaUNPCustDomainMacRangeRuleRowStatus": alaDaUNPCustDomainMacRangeRuleRowStatus,
       "alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus": alaDaUNPCustDomainMacRangeRuleMCLagConfigStatus,
       "alaDaUNPCustDomainMacRangeRuleSpbProfileName": alaDaUNPCustDomainMacRangeRuleSpbProfileName,
       "alaDaSaaProfileTable": alaDaSaaProfileTable,
       "alaDaSaaProfileEntry": alaDaSaaProfileEntry,
       "alaDaSaaProfileName": alaDaSaaProfileName,
       "alaDaSaaProfileLatencyThreshold": alaDaSaaProfileLatencyThreshold,
       "alaDaSaaProfileJitterThreshold": alaDaSaaProfileJitterThreshold,
       "alaDaSaaProfileRowStatus": alaDaSaaProfileRowStatus,
       "alaIND1DaMIBConformance": alaIND1DaMIBConformance,
       "alaIND1DaMIBGroups": alaIND1DaMIBGroups,
       "alaDaUserNetProfileGroup": alaDaUserNetProfileGroup,
       "alaDaUNPIpNetRuleGroup": alaDaUNPIpNetRuleGroup,
       "alaDaUNPMacRuleGroup": alaDaUNPMacRuleGroup,
       "alaDaUNPMacRangeGroup": alaDaUNPMacRangeGroup,
       "alaDaUNPVlanTagGroup": alaDaUNPVlanTagGroup,
       "alaDaMacUserGroup": alaDaMacUserGroup,
       "alaDaUNPPortGroup": alaDaUNPPortGroup,
       "alaDaUNPGlobalGroup": alaDaUNPGlobalGroup,
       "alaDaNotificationObjectGroup": alaDaNotificationObjectGroup,
       "alaDaNotificationsGroup": alaDaNotificationsGroup,
       "alaDaMacVlanUserGroup": alaDaMacVlanUserGroup,
       "alaDaUnpCustomerDomainGroup": alaDaUnpCustomerDomainGroup,
       "alaDaSpbProfileGroup": alaDaSpbProfileGroup,
       "alaDaUNPCustDomainEvbGpIdRuleGroup": alaDaUNPCustDomainEvbGpIdRuleGroup,
       "alaDaUNPCustDomainVlanTagRuleGroup": alaDaUNPCustDomainVlanTagRuleGroup,
       "alaDaUNPCustDomainIpNetRuleGroup": alaDaUNPCustDomainIpNetRuleGroup,
       "alaDaUNPCustDomainMacRuleGroup": alaDaUNPCustDomainMacRuleGroup,
       "alaDaUNPCustDomainMacRangeGroup": alaDaUNPCustDomainMacRangeGroup,
       "alaDaUNPGroupObjects": alaDaUNPGroupObjects,
       "alaDaSaaProfileGroup": alaDaSaaProfileGroup,
       "alaIND1DaMIBCompliances": alaIND1DaMIBCompliances}
)
