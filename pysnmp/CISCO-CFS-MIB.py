# SNMP MIB module (CISCO-CFS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CFS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:23 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
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

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoCFSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433)
)
ciscoCFSMIB.setRevisions(
        ("2006-06-13 00:00",
         "2005-11-30 00:00",
         "2005-04-27 00:00",
         "2004-12-24 00:00",
         "2004-12-03 00:00",
         "2004-09-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoCFSAction(Integer32, TextualConvention):
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
        *(("abort", 5),
          ("clear", 6),
          ("commit", 4),
          ("disable", 3),
          ("enable", 2),
          ("noop", 1))
    )



class CiscoCFSFeatureStatus(Integer32, TextualConvention):
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
        *(("disabled", 3),
          ("enabled", 2),
          ("unknown", 1))
    )



class CiscoCFSFeatureActionResult(Integer32, TextualConvention):
    status = "current"
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
        *(("failed", 3),
          ("inProgress", 4),
          ("none", 1),
          ("partialSuccess", 5),
          ("success", 2))
    )



class CiscoCFSScopeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vsanID", 2))
    )



class CiscoCFSScopeValue(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoCFSMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCFSMIBNotifs = _CiscoCFSMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 0)
)
_CiscoCFSMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCFSMIBObjects = _CiscoCFSMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1)
)
_CfsFeature_ObjectIdentity = ObjectIdentity
cfsFeature = _CfsFeature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1)
)
_CfsFeatureOpTable_Object = MibTable
cfsFeatureOpTable = _CfsFeatureOpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfsFeatureOpTable.setStatus("current")
_CfsFeatureOpEntry_Object = MibTableRow
cfsFeatureOpEntry = _CfsFeatureOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1)
)
cfsFeatureOpEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsFeatureOpName"),
)
if mibBuilder.loadTexts:
    cfsFeatureOpEntry.setStatus("current")


class _CfsFeatureOpName_Type(SnmpAdminString):
    """Custom type cfsFeatureOpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsFeatureOpName_Type.__name__ = "SnmpAdminString"
_CfsFeatureOpName_Object = MibTableColumn
cfsFeatureOpName = _CfsFeatureOpName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 1),
    _CfsFeatureOpName_Type()
)
cfsFeatureOpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsFeatureOpName.setStatus("current")
_CfsFeatureOpAction_Type = CiscoCFSAction
_CfsFeatureOpAction_Object = MibTableColumn
cfsFeatureOpAction = _CfsFeatureOpAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 2),
    _CfsFeatureOpAction_Type()
)
cfsFeatureOpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsFeatureOpAction.setStatus("current")


class _CfsFeatureOpScopeType_Type(CiscoCFSScopeType):
    """Custom type cfsFeatureOpScopeType based on CiscoCFSScopeType"""


_CfsFeatureOpScopeType_Object = MibTableColumn
cfsFeatureOpScopeType = _CfsFeatureOpScopeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 3),
    _CfsFeatureOpScopeType_Type()
)
cfsFeatureOpScopeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsFeatureOpScopeType.setStatus("current")


class _CfsFeatureOpScopeVal_Type(CiscoCFSScopeValue):
    """Custom type cfsFeatureOpScopeVal based on CiscoCFSScopeValue"""
    defaultHexValue = ""

    subtypeSpec = CiscoCFSScopeValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsFeatureOpScopeVal_Type.__name__ = "CiscoCFSScopeValue"
_CfsFeatureOpScopeVal_Object = MibTableColumn
cfsFeatureOpScopeVal = _CfsFeatureOpScopeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 4),
    _CfsFeatureOpScopeVal_Type()
)
cfsFeatureOpScopeVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsFeatureOpScopeVal.setStatus("current")
_CfsFeatureOpLastAction_Type = CiscoCFSAction
_CfsFeatureOpLastAction_Object = MibTableColumn
cfsFeatureOpLastAction = _CfsFeatureOpLastAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 5),
    _CfsFeatureOpLastAction_Type()
)
cfsFeatureOpLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpLastAction.setStatus("current")
_CfsFeatureOpLastScopeType_Type = CiscoCFSScopeType
_CfsFeatureOpLastScopeType_Object = MibTableColumn
cfsFeatureOpLastScopeType = _CfsFeatureOpLastScopeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 6),
    _CfsFeatureOpLastScopeType_Type()
)
cfsFeatureOpLastScopeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpLastScopeType.setStatus("current")


class _CfsFeatureOpLastScopeVal_Type(CiscoCFSScopeValue):
    """Custom type cfsFeatureOpLastScopeVal based on CiscoCFSScopeValue"""
    subtypeSpec = CiscoCFSScopeValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsFeatureOpLastScopeVal_Type.__name__ = "CiscoCFSScopeValue"
_CfsFeatureOpLastScopeVal_Object = MibTableColumn
cfsFeatureOpLastScopeVal = _CfsFeatureOpLastScopeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 7),
    _CfsFeatureOpLastScopeVal_Type()
)
cfsFeatureOpLastScopeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpLastScopeVal.setStatus("current")
_CfsFeatureOpLastActionResult_Type = CiscoCFSFeatureActionResult
_CfsFeatureOpLastActionResult_Object = MibTableColumn
cfsFeatureOpLastActionResult = _CfsFeatureOpLastActionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 8),
    _CfsFeatureOpLastActionResult_Type()
)
cfsFeatureOpLastActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpLastActionResult.setStatus("current")
_CfsFeatureOpLastFailureReason_Type = SnmpAdminString
_CfsFeatureOpLastFailureReason_Object = MibTableColumn
cfsFeatureOpLastFailureReason = _CfsFeatureOpLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 9),
    _CfsFeatureOpLastFailureReason_Type()
)
cfsFeatureOpLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpLastFailureReason.setStatus("current")


class _CfsFeatureOpShowCfgOption_Type(Integer32):
    """Custom type cfsFeatureOpShowCfgOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pendingConfig", 2),
          ("runningConfig", 1))
    )


_CfsFeatureOpShowCfgOption_Type.__name__ = "Integer32"
_CfsFeatureOpShowCfgOption_Object = MibTableColumn
cfsFeatureOpShowCfgOption = _CfsFeatureOpShowCfgOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 10),
    _CfsFeatureOpShowCfgOption_Type()
)
cfsFeatureOpShowCfgOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsFeatureOpShowCfgOption.setStatus("deprecated")
_CfsFeatureOpStatus_Type = CiscoCFSFeatureStatus
_CfsFeatureOpStatus_Object = MibTableColumn
cfsFeatureOpStatus = _CfsFeatureOpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 11),
    _CfsFeatureOpStatus_Type()
)
cfsFeatureOpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpStatus.setStatus("current")


class _CfsFeatureOpAttribs_Type(Bits):
    """Custom type cfsFeatureOpAttribs based on Bits"""
    namedValues = NamedValues(
        *(("fcFabric", 0),
          ("ipNetwork", 1),
          ("vsanScope", 2))
    )

_CfsFeatureOpAttribs_Type.__name__ = "Bits"
_CfsFeatureOpAttribs_Object = MibTableColumn
cfsFeatureOpAttribs = _CfsFeatureOpAttribs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 1, 1, 12),
    _CfsFeatureOpAttribs_Type()
)
cfsFeatureOpAttribs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpAttribs.setStatus("current")
_CfsPendingConfOwnerTable_Object = MibTable
cfsPendingConfOwnerTable = _CfsPendingConfOwnerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfsPendingConfOwnerTable.setStatus("current")
_CfsPendingConfOwnerEntry_Object = MibTableRow
cfsPendingConfOwnerEntry = _CfsPendingConfOwnerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2, 1)
)
cfsPendingConfOwnerEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsFeatureOpName"),
    (0, "CISCO-CFS-MIB", "cfsPendingConfOwnerScopeType"),
    (0, "CISCO-CFS-MIB", "cfsPendingConfOwnerScopeVal"),
)
if mibBuilder.loadTexts:
    cfsPendingConfOwnerEntry.setStatus("current")
_CfsPendingConfOwnerScopeType_Type = CiscoCFSScopeType
_CfsPendingConfOwnerScopeType_Object = MibTableColumn
cfsPendingConfOwnerScopeType = _CfsPendingConfOwnerScopeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2, 1, 1),
    _CfsPendingConfOwnerScopeType_Type()
)
cfsPendingConfOwnerScopeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsPendingConfOwnerScopeType.setStatus("current")


class _CfsPendingConfOwnerScopeVal_Type(CiscoCFSScopeValue):
    """Custom type cfsPendingConfOwnerScopeVal based on CiscoCFSScopeValue"""
    subtypeSpec = CiscoCFSScopeValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsPendingConfOwnerScopeVal_Type.__name__ = "CiscoCFSScopeValue"
_CfsPendingConfOwnerScopeVal_Object = MibTableColumn
cfsPendingConfOwnerScopeVal = _CfsPendingConfOwnerScopeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2, 1, 2),
    _CfsPendingConfOwnerScopeVal_Type()
)
cfsPendingConfOwnerScopeVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsPendingConfOwnerScopeVal.setStatus("current")
_CfsPendingConfOwnerAddrType_Type = InetAddressType
_CfsPendingConfOwnerAddrType_Object = MibTableColumn
cfsPendingConfOwnerAddrType = _CfsPendingConfOwnerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2, 1, 3),
    _CfsPendingConfOwnerAddrType_Type()
)
cfsPendingConfOwnerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsPendingConfOwnerAddrType.setStatus("current")
_CfsPendingConfOwnerAddr_Type = InetAddress
_CfsPendingConfOwnerAddr_Object = MibTableColumn
cfsPendingConfOwnerAddr = _CfsPendingConfOwnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2, 1, 4),
    _CfsPendingConfOwnerAddr_Type()
)
cfsPendingConfOwnerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsPendingConfOwnerAddr.setStatus("current")


class _CfsPendingConfOwnerIDType_Type(Bits):
    """Custom type cfsPendingConfOwnerIDType based on Bits"""
    namedValues = NamedValues(
        *(("cliLoginName", 3),
          ("other", 0),
          ("snmpCommunityName", 1),
          ("snmpv3SecurityName", 2))
    )

_CfsPendingConfOwnerIDType_Type.__name__ = "Bits"
_CfsPendingConfOwnerIDType_Object = MibTableColumn
cfsPendingConfOwnerIDType = _CfsPendingConfOwnerIDType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2, 1, 5),
    _CfsPendingConfOwnerIDType_Type()
)
cfsPendingConfOwnerIDType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsPendingConfOwnerIDType.setStatus("current")
_CfsPendingConfOwnerID_Type = SnmpAdminString
_CfsPendingConfOwnerID_Object = MibTableColumn
cfsPendingConfOwnerID = _CfsPendingConfOwnerID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 2, 1, 6),
    _CfsPendingConfOwnerID_Type()
)
cfsPendingConfOwnerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsPendingConfOwnerID.setStatus("current")
_CfsMergeStatusTable_Object = MibTable
cfsMergeStatusTable = _CfsMergeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfsMergeStatusTable.setStatus("current")
_CfsMergeStatusEntry_Object = MibTableRow
cfsMergeStatusEntry = _CfsMergeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 3, 1)
)
cfsMergeStatusEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsFeatureOpName"),
    (0, "CISCO-CFS-MIB", "cfsMergeStatusScopeType"),
    (0, "CISCO-CFS-MIB", "cfsMergeStatusScopeVal"),
)
if mibBuilder.loadTexts:
    cfsMergeStatusEntry.setStatus("current")
_CfsMergeStatusScopeType_Type = CiscoCFSScopeType
_CfsMergeStatusScopeType_Object = MibTableColumn
cfsMergeStatusScopeType = _CfsMergeStatusScopeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 3, 1, 1),
    _CfsMergeStatusScopeType_Type()
)
cfsMergeStatusScopeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsMergeStatusScopeType.setStatus("current")


class _CfsMergeStatusScopeVal_Type(CiscoCFSScopeValue):
    """Custom type cfsMergeStatusScopeVal based on CiscoCFSScopeValue"""
    subtypeSpec = CiscoCFSScopeValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsMergeStatusScopeVal_Type.__name__ = "CiscoCFSScopeValue"
_CfsMergeStatusScopeVal_Object = MibTableColumn
cfsMergeStatusScopeVal = _CfsMergeStatusScopeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 3, 1, 2),
    _CfsMergeStatusScopeVal_Type()
)
cfsMergeStatusScopeVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsMergeStatusScopeVal.setStatus("current")


class _CfsMergeStatusValue_Type(Integer32):
    """Custom type cfsMergeStatusValue based on Integer32"""
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
        *(("failure", 3),
          ("inProgress", 2),
          ("other", 5),
          ("success", 1),
          ("waiting", 4))
    )


_CfsMergeStatusValue_Type.__name__ = "Integer32"
_CfsMergeStatusValue_Object = MibTableColumn
cfsMergeStatusValue = _CfsMergeStatusValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 3, 1, 3),
    _CfsMergeStatusValue_Type()
)
cfsMergeStatusValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsMergeStatusValue.setStatus("current")
_CfsMergeMembersTable_Object = MibTable
cfsMergeMembersTable = _CfsMergeMembersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cfsMergeMembersTable.setStatus("current")
_CfsMergeMembersEntry_Object = MibTableRow
cfsMergeMembersEntry = _CfsMergeMembersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 4, 1)
)
cfsMergeMembersEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsFeatureOpName"),
    (0, "CISCO-CFS-MIB", "cfsMergeStatusScopeType"),
    (0, "CISCO-CFS-MIB", "cfsMergeStatusScopeVal"),
    (0, "CISCO-CFS-MIB", "cfsMergeMemberAddrType"),
    (0, "CISCO-CFS-MIB", "cfsMergeMemberAddr"),
)
if mibBuilder.loadTexts:
    cfsMergeMembersEntry.setStatus("current")
_CfsMergeMemberAddrType_Type = InetAddressType
_CfsMergeMemberAddrType_Object = MibTableColumn
cfsMergeMemberAddrType = _CfsMergeMemberAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 4, 1, 1),
    _CfsMergeMemberAddrType_Type()
)
cfsMergeMemberAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsMergeMemberAddrType.setStatus("current")


class _CfsMergeMemberAddr_Type(InetAddress):
    """Custom type cfsMergeMemberAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsMergeMemberAddr_Type.__name__ = "InetAddress"
_CfsMergeMemberAddr_Object = MibTableColumn
cfsMergeMemberAddr = _CfsMergeMemberAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 4, 1, 2),
    _CfsMergeMemberAddr_Type()
)
cfsMergeMemberAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsMergeMemberAddr.setStatus("current")


class _CfsMergeMemberFabricType_Type(Integer32):
    """Custom type cfsMergeMemberFabricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("remote", 3),
          ("unknown", 1))
    )


_CfsMergeMemberFabricType_Type.__name__ = "Integer32"
_CfsMergeMemberFabricType_Object = MibTableColumn
cfsMergeMemberFabricType = _CfsMergeMemberFabricType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 4, 1, 3),
    _CfsMergeMemberFabricType_Type()
)
cfsMergeMemberFabricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsMergeMemberFabricType.setStatus("current")


class _CfsMergeMemberRole_Type(Integer32):
    """Custom type cfsMergeMemberRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("peer", 3),
          ("unknown", 1))
    )


_CfsMergeMemberRole_Type.__name__ = "Integer32"
_CfsMergeMemberRole_Object = MibTableColumn
cfsMergeMemberRole = _CfsMergeMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 4, 1, 4),
    _CfsMergeMemberRole_Type()
)
cfsMergeMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsMergeMemberRole.setStatus("current")
_CfsPeersTable_Object = MibTable
cfsPeersTable = _CfsPeersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfsPeersTable.setStatus("current")
_CfsPeersEntry_Object = MibTableRow
cfsPeersEntry = _CfsPeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 5, 1)
)
cfsPeersEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsPeerAddrType"),
    (0, "CISCO-CFS-MIB", "cfsPeerAddr"),
)
if mibBuilder.loadTexts:
    cfsPeersEntry.setStatus("current")
_CfsPeerAddrType_Type = InetAddressType
_CfsPeerAddrType_Object = MibTableColumn
cfsPeerAddrType = _CfsPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 5, 1, 1),
    _CfsPeerAddrType_Type()
)
cfsPeerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsPeerAddrType.setStatus("current")


class _CfsPeerAddr_Type(InetAddress):
    """Custom type cfsPeerAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsPeerAddr_Type.__name__ = "InetAddress"
_CfsPeerAddr_Object = MibTableColumn
cfsPeerAddr = _CfsPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 5, 1, 2),
    _CfsPeerAddr_Type()
)
cfsPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsPeerAddr.setStatus("current")
_CfsFeaturePeersTable_Object = MibTable
cfsFeaturePeersTable = _CfsFeaturePeersTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cfsFeaturePeersTable.setStatus("current")
_CfsFeaturePeersEntry_Object = MibTableRow
cfsFeaturePeersEntry = _CfsFeaturePeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 6, 1)
)
cfsFeaturePeersEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsFeatureOpName"),
    (0, "CISCO-CFS-MIB", "cfsFeaturePeersScopeType"),
    (0, "CISCO-CFS-MIB", "cfsFeaturePeersScopeVal"),
    (0, "CISCO-CFS-MIB", "cfsFeaturePeersAddrType"),
    (0, "CISCO-CFS-MIB", "cfsFeaturePeersAddr"),
)
if mibBuilder.loadTexts:
    cfsFeaturePeersEntry.setStatus("current")
_CfsFeaturePeersScopeType_Type = CiscoCFSScopeType
_CfsFeaturePeersScopeType_Object = MibTableColumn
cfsFeaturePeersScopeType = _CfsFeaturePeersScopeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 6, 1, 1),
    _CfsFeaturePeersScopeType_Type()
)
cfsFeaturePeersScopeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsFeaturePeersScopeType.setStatus("current")


class _CfsFeaturePeersScopeVal_Type(CiscoCFSScopeValue):
    """Custom type cfsFeaturePeersScopeVal based on CiscoCFSScopeValue"""
    subtypeSpec = CiscoCFSScopeValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsFeaturePeersScopeVal_Type.__name__ = "CiscoCFSScopeValue"
_CfsFeaturePeersScopeVal_Object = MibTableColumn
cfsFeaturePeersScopeVal = _CfsFeaturePeersScopeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 6, 1, 2),
    _CfsFeaturePeersScopeVal_Type()
)
cfsFeaturePeersScopeVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsFeaturePeersScopeVal.setStatus("current")
_CfsFeaturePeersAddrType_Type = InetAddressType
_CfsFeaturePeersAddrType_Object = MibTableColumn
cfsFeaturePeersAddrType = _CfsFeaturePeersAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 6, 1, 3),
    _CfsFeaturePeersAddrType_Type()
)
cfsFeaturePeersAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsFeaturePeersAddrType.setStatus("current")


class _CfsFeaturePeersAddr_Type(InetAddress):
    """Custom type cfsFeaturePeersAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsFeaturePeersAddr_Type.__name__ = "InetAddress"
_CfsFeaturePeersAddr_Object = MibTableColumn
cfsFeaturePeersAddr = _CfsFeaturePeersAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 6, 1, 4),
    _CfsFeaturePeersAddr_Type()
)
cfsFeaturePeersAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeaturePeersAddr.setStatus("current")
_CfsFeatureOpExtTable_Object = MibTable
cfsFeatureOpExtTable = _CfsFeatureOpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cfsFeatureOpExtTable.setStatus("current")
_CfsFeatureOpExtEntry_Object = MibTableRow
cfsFeatureOpExtEntry = _CfsFeatureOpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1)
)
cfsFeatureOpExtEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsFeatureOpName"),
    (0, "CISCO-CFS-MIB", "cfsFeatureOpExtScopeType"),
    (0, "CISCO-CFS-MIB", "cfsFeatureOpExtScopeVal"),
)
if mibBuilder.loadTexts:
    cfsFeatureOpExtEntry.setStatus("current")
_CfsFeatureOpExtScopeType_Type = CiscoCFSScopeType
_CfsFeatureOpExtScopeType_Object = MibTableColumn
cfsFeatureOpExtScopeType = _CfsFeatureOpExtScopeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1, 1),
    _CfsFeatureOpExtScopeType_Type()
)
cfsFeatureOpExtScopeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsFeatureOpExtScopeType.setStatus("current")


class _CfsFeatureOpExtScopeVal_Type(CiscoCFSScopeValue):
    """Custom type cfsFeatureOpExtScopeVal based on CiscoCFSScopeValue"""
    subtypeSpec = CiscoCFSScopeValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsFeatureOpExtScopeVal_Type.__name__ = "CiscoCFSScopeValue"
_CfsFeatureOpExtScopeVal_Object = MibTableColumn
cfsFeatureOpExtScopeVal = _CfsFeatureOpExtScopeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1, 2),
    _CfsFeatureOpExtScopeVal_Type()
)
cfsFeatureOpExtScopeVal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsFeatureOpExtScopeVal.setStatus("current")
_CfsFeatureOpExtLastAction_Type = CiscoCFSAction
_CfsFeatureOpExtLastAction_Object = MibTableColumn
cfsFeatureOpExtLastAction = _CfsFeatureOpExtLastAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1, 3),
    _CfsFeatureOpExtLastAction_Type()
)
cfsFeatureOpExtLastAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpExtLastAction.setStatus("current")
_CfsFeatureOpExtLastActionResult_Type = CiscoCFSFeatureActionResult
_CfsFeatureOpExtLastActionResult_Object = MibTableColumn
cfsFeatureOpExtLastActionResult = _CfsFeatureOpExtLastActionResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1, 4),
    _CfsFeatureOpExtLastActionResult_Type()
)
cfsFeatureOpExtLastActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpExtLastActionResult.setStatus("current")
_CfsFeatureOpExtLastFailureReason_Type = SnmpAdminString
_CfsFeatureOpExtLastFailureReason_Object = MibTableColumn
cfsFeatureOpExtLastFailureReason = _CfsFeatureOpExtLastFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1, 5),
    _CfsFeatureOpExtLastFailureReason_Type()
)
cfsFeatureOpExtLastFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpExtLastFailureReason.setStatus("current")


class _CfsFeatureOpExtShowCfgOption_Type(Integer32):
    """Custom type cfsFeatureOpExtShowCfgOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pendingConfig", 2),
          ("runningConfig", 1))
    )


_CfsFeatureOpExtShowCfgOption_Type.__name__ = "Integer32"
_CfsFeatureOpExtShowCfgOption_Object = MibTableColumn
cfsFeatureOpExtShowCfgOption = _CfsFeatureOpExtShowCfgOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1, 6),
    _CfsFeatureOpExtShowCfgOption_Type()
)
cfsFeatureOpExtShowCfgOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsFeatureOpExtShowCfgOption.setStatus("current")
_CfsFeatureOpExtLastActionTime_Type = TimeStamp
_CfsFeatureOpExtLastActionTime_Object = MibTableColumn
cfsFeatureOpExtLastActionTime = _CfsFeatureOpExtLastActionTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 1, 7, 1, 7),
    _CfsFeatureOpExtLastActionTime_Type()
)
cfsFeatureOpExtLastActionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsFeatureOpExtLastActionTime.setStatus("current")
_CfsNotifObjects_ObjectIdentity = ObjectIdentity
cfsNotifObjects = _CfsNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 2)
)


class _CfsMergeFailFeatureName_Type(SnmpAdminString):
    """Custom type cfsMergeFailFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsMergeFailFeatureName_Type.__name__ = "SnmpAdminString"
_CfsMergeFailFeatureName_Object = MibScalar
cfsMergeFailFeatureName = _CfsMergeFailFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 2, 1),
    _CfsMergeFailFeatureName_Type()
)
cfsMergeFailFeatureName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfsMergeFailFeatureName.setStatus("current")
_CfsMergeFailScopeType_Type = CiscoCFSScopeType
_CfsMergeFailScopeType_Object = MibScalar
cfsMergeFailScopeType = _CfsMergeFailScopeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 2, 2),
    _CfsMergeFailScopeType_Type()
)
cfsMergeFailScopeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfsMergeFailScopeType.setStatus("current")


class _CfsMergeFailScopeVal_Type(CiscoCFSScopeValue):
    """Custom type cfsMergeFailScopeVal based on CiscoCFSScopeValue"""
    subtypeSpec = CiscoCFSScopeValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CfsMergeFailScopeVal_Type.__name__ = "CiscoCFSScopeValue"
_CfsMergeFailScopeVal_Object = MibScalar
cfsMergeFailScopeVal = _CfsMergeFailScopeVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 2, 3),
    _CfsMergeFailScopeVal_Type()
)
cfsMergeFailScopeVal.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfsMergeFailScopeVal.setStatus("current")
_CfsMergeFailReasonDescription_Type = SnmpAdminString
_CfsMergeFailReasonDescription_Object = MibScalar
cfsMergeFailReasonDescription = _CfsMergeFailReasonDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 2, 4),
    _CfsMergeFailReasonDescription_Type()
)
cfsMergeFailReasonDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cfsMergeFailReasonDescription.setStatus("current")
_CfsDiscoveryObjects_ObjectIdentity = ObjectIdentity
cfsDiscoveryObjects = _CfsDiscoveryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 3)
)


class _CfsStartPeersDiscovery_Type(Integer32):
    """Custom type cfsStartPeersDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 2),
          ("startDiscovery", 1))
    )


_CfsStartPeersDiscovery_Type.__name__ = "Integer32"
_CfsStartPeersDiscovery_Object = MibScalar
cfsStartPeersDiscovery = _CfsStartPeersDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 3, 1),
    _CfsStartPeersDiscovery_Type()
)
cfsStartPeersDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsStartPeersDiscovery.setStatus("current")


class _CfsPeersDiscoveryResult_Type(Integer32):
    """Custom type cfsPeersDiscoveryResult based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("notInitiated", 1),
          ("successful", 3))
    )


_CfsPeersDiscoveryResult_Type.__name__ = "Integer32"
_CfsPeersDiscoveryResult_Object = MibScalar
cfsPeersDiscoveryResult = _CfsPeersDiscoveryResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 3, 2),
    _CfsPeersDiscoveryResult_Type()
)
cfsPeersDiscoveryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsPeersDiscoveryResult.setStatus("current")
_CfsPeersDiscoveryFailureReason_Type = SnmpAdminString
_CfsPeersDiscoveryFailureReason_Object = MibScalar
cfsPeersDiscoveryFailureReason = _CfsPeersDiscoveryFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 3, 3),
    _CfsPeersDiscoveryFailureReason_Type()
)
cfsPeersDiscoveryFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfsPeersDiscoveryFailureReason.setStatus("current")
_CfsDistCtrlObjects_ObjectIdentity = ObjectIdentity
cfsDistCtrlObjects = _CfsDistCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 4)
)


class _CfsDistCtrl_Type(Integer32):
    """Custom type cfsDistCtrl based on Integer32"""
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


_CfsDistCtrl_Type.__name__ = "Integer32"
_CfsDistCtrl_Object = MibScalar
cfsDistCtrl = _CfsDistCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 4, 1),
    _CfsDistCtrl_Type()
)
cfsDistCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsDistCtrl.setStatus("current")
_CfsDistCtrlTable_Object = MibTable
cfsDistCtrlTable = _CfsDistCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cfsDistCtrlTable.setStatus("current")
_CfsDistCtrlEntry_Object = MibTableRow
cfsDistCtrlEntry = _CfsDistCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 4, 2, 1)
)
cfsDistCtrlEntry.setIndexNames(
    (0, "CISCO-CFS-MIB", "cfsDistCtrlAddrType"),
)
if mibBuilder.loadTexts:
    cfsDistCtrlEntry.setStatus("current")
_CfsDistCtrlAddrType_Type = InetAddressType
_CfsDistCtrlAddrType_Object = MibTableColumn
cfsDistCtrlAddrType = _CfsDistCtrlAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 4, 2, 1, 1),
    _CfsDistCtrlAddrType_Type()
)
cfsDistCtrlAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfsDistCtrlAddrType.setStatus("current")
_CfsDistCtrlAddr_Type = InetAddress
_CfsDistCtrlAddr_Object = MibTableColumn
cfsDistCtrlAddr = _CfsDistCtrlAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 4, 2, 1, 2),
    _CfsDistCtrlAddr_Type()
)
cfsDistCtrlAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsDistCtrlAddr.setStatus("current")


class _CfsDistCtrlAction_Type(Integer32):
    """Custom type cfsDistCtrlAction based on Integer32"""
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


_CfsDistCtrlAction_Type.__name__ = "Integer32"
_CfsDistCtrlAction_Object = MibTableColumn
cfsDistCtrlAction = _CfsDistCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 1, 4, 2, 1, 3),
    _CfsDistCtrlAction_Type()
)
cfsDistCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfsDistCtrlAction.setStatus("current")
_CiscoCFSMIBConformance_ObjectIdentity = ObjectIdentity
ciscoCFSMIBConformance = _CiscoCFSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2)
)
_CiscoCFSMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCFSMIBCompliances = _CiscoCFSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 1)
)
_CiscoCFSMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCFSMIBGroups = _CiscoCFSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2)
)

# Managed Objects groups

cfsFeatureOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 1)
)
cfsFeatureOpGroup.setObjects(
      *(("CISCO-CFS-MIB", "cfsFeatureOpAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpScopeType"),
        ("CISCO-CFS-MIB", "cfsFeatureOpScopeVal"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeType"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeVal"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastActionResult"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastFailureReason"),
        ("CISCO-CFS-MIB", "cfsFeatureOpShowCfgOption"),
        ("CISCO-CFS-MIB", "cfsFeatureOpStatus"),
        ("CISCO-CFS-MIB", "cfsMergeStatusValue"))
)
if mibBuilder.loadTexts:
    cfsFeatureOpGroup.setStatus("deprecated")

cfsPendingConfOwnerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 2)
)
cfsPendingConfOwnerGroup.setObjects(
      *(("CISCO-CFS-MIB", "cfsPendingConfOwnerAddrType"),
        ("CISCO-CFS-MIB", "cfsPendingConfOwnerAddr"),
        ("CISCO-CFS-MIB", "cfsPendingConfOwnerIDType"),
        ("CISCO-CFS-MIB", "cfsPendingConfOwnerID"))
)
if mibBuilder.loadTexts:
    cfsPendingConfOwnerGroup.setStatus("current")

cfsFeatureNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 3)
)
cfsFeatureNotifObjectsGroup.setObjects(
      *(("CISCO-CFS-MIB", "cfsMergeFailFeatureName"),
        ("CISCO-CFS-MIB", "cfsMergeFailScopeType"),
        ("CISCO-CFS-MIB", "cfsMergeFailScopeVal"),
        ("CISCO-CFS-MIB", "cfsMergeFailReasonDescription"))
)
if mibBuilder.loadTexts:
    cfsFeatureNotifObjectsGroup.setStatus("current")

cfsMembersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 6)
)
cfsMembersGroup.setObjects(
      *(("CISCO-CFS-MIB", "cfsMergeMemberFabricType"),
        ("CISCO-CFS-MIB", "cfsMergeMemberRole"),
        ("CISCO-CFS-MIB", "cfsStartPeersDiscovery"),
        ("CISCO-CFS-MIB", "cfsPeersDiscoveryResult"),
        ("CISCO-CFS-MIB", "cfsPeersDiscoveryFailureReason"),
        ("CISCO-CFS-MIB", "cfsPeerAddr"),
        ("CISCO-CFS-MIB", "cfsFeaturePeersAddr"))
)
if mibBuilder.loadTexts:
    cfsMembersGroup.setStatus("current")

cfsFeatureOpExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 7)
)
cfsFeatureOpExtGroup.setObjects(
      *(("CISCO-CFS-MIB", "cfsFeatureOpExtLastAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpExtLastActionResult"),
        ("CISCO-CFS-MIB", "cfsFeatureOpExtLastFailureReason"),
        ("CISCO-CFS-MIB", "cfsFeatureOpExtShowCfgOption"))
)
if mibBuilder.loadTexts:
    cfsFeatureOpExtGroup.setStatus("deprecated")

cfsFeatureOpGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 9)
)
cfsFeatureOpGroupRev1.setObjects(
      *(("CISCO-CFS-MIB", "cfsFeatureOpAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpScopeType"),
        ("CISCO-CFS-MIB", "cfsFeatureOpScopeVal"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeType"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeVal"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastActionResult"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastFailureReason"),
        ("CISCO-CFS-MIB", "cfsFeatureOpStatus"),
        ("CISCO-CFS-MIB", "cfsMergeStatusValue"))
)
if mibBuilder.loadTexts:
    cfsFeatureOpGroupRev1.setStatus("deprecated")

cfsDistCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 10)
)
cfsDistCtrlGroup.setObjects(
    ("CISCO-CFS-MIB", "cfsDistCtrl")
)
if mibBuilder.loadTexts:
    cfsDistCtrlGroup.setStatus("current")

cfsDistCtrlInetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 11)
)
cfsDistCtrlInetGroup.setObjects(
      *(("CISCO-CFS-MIB", "cfsDistCtrlAddr"),
        ("CISCO-CFS-MIB", "cfsDistCtrlAction"))
)
if mibBuilder.loadTexts:
    cfsDistCtrlInetGroup.setStatus("current")

cfsFeatureOpGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 12)
)
cfsFeatureOpGroupRev2.setObjects(
      *(("CISCO-CFS-MIB", "cfsFeatureOpAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpScopeType"),
        ("CISCO-CFS-MIB", "cfsFeatureOpScopeVal"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeType"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeVal"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastActionResult"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastFailureReason"),
        ("CISCO-CFS-MIB", "cfsFeatureOpStatus"),
        ("CISCO-CFS-MIB", "cfsMergeStatusValue"),
        ("CISCO-CFS-MIB", "cfsFeatureOpAttribs"))
)
if mibBuilder.loadTexts:
    cfsFeatureOpGroupRev2.setStatus("current")

cfsFeatureOpExtGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 13)
)
cfsFeatureOpExtGroupRev1.setObjects(
      *(("CISCO-CFS-MIB", "cfsFeatureOpExtLastAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpExtLastActionTime"),
        ("CISCO-CFS-MIB", "cfsFeatureOpExtLastActionResult"),
        ("CISCO-CFS-MIB", "cfsFeatureOpExtLastFailureReason"),
        ("CISCO-CFS-MIB", "cfsFeatureOpExtShowCfgOption"))
)
if mibBuilder.loadTexts:
    cfsFeatureOpExtGroupRev1.setStatus("current")


# Notification objects

ciscoCFSFeatureActionNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 0, 1)
)
ciscoCFSFeatureActionNotif.setObjects(
      *(("CISCO-CFS-MIB", "cfsFeatureOpLastAction"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeType"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastScopeVal"),
        ("CISCO-CFS-MIB", "cfsFeatureOpLastActionResult"))
)
if mibBuilder.loadTexts:
    ciscoCFSFeatureActionNotif.setStatus(
        "current"
    )

ciscoCFSMergeFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 0, 2)
)
ciscoCFSMergeFailNotif.setObjects(
      *(("CISCO-CFS-MIB", "cfsMergeFailFeatureName"),
        ("CISCO-CFS-MIB", "cfsMergeFailScopeType"),
        ("CISCO-CFS-MIB", "cfsMergeFailScopeVal"),
        ("CISCO-CFS-MIB", "cfsMergeFailReasonDescription"))
)
if mibBuilder.loadTexts:
    ciscoCFSMergeFailNotif.setStatus(
        "current"
    )

ciscoCFSDiscoveryCompleteNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 0, 3)
)
ciscoCFSDiscoveryCompleteNotif.setObjects(
      *(("CISCO-CFS-MIB", "cfsPeersDiscoveryResult"),
        ("CISCO-CFS-MIB", "cfsPeersDiscoveryFailureReason"))
)
if mibBuilder.loadTexts:
    ciscoCFSDiscoveryCompleteNotif.setStatus(
        "current"
    )


# Notifications groups

cfsFeatureActionNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 4)
)
cfsFeatureActionNotifGroup.setObjects(
    ("CISCO-CFS-MIB", "ciscoCFSFeatureActionNotif")
)
if mibBuilder.loadTexts:
    cfsFeatureActionNotifGroup.setStatus(
        "current"
    )

cfsMergeFailNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 5)
)
cfsMergeFailNotifGroup.setObjects(
    ("CISCO-CFS-MIB", "ciscoCFSMergeFailNotif")
)
if mibBuilder.loadTexts:
    cfsMergeFailNotifGroup.setStatus(
        "current"
    )

cfsPeerDiscoveryNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 2, 8)
)
cfsPeerDiscoveryNotifGroup.setObjects(
    ("CISCO-CFS-MIB", "ciscoCFSDiscoveryCompleteNotif")
)
if mibBuilder.loadTexts:
    cfsPeerDiscoveryNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoCFSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCFSMIBCompliance.setStatus(
        "deprecated"
    )

ciscoCFSMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCFSMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoCFSMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCFSMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoCFSMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 433, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoCFSMIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CFS-MIB",
    **{"CiscoCFSAction": CiscoCFSAction,
       "CiscoCFSFeatureStatus": CiscoCFSFeatureStatus,
       "CiscoCFSFeatureActionResult": CiscoCFSFeatureActionResult,
       "CiscoCFSScopeType": CiscoCFSScopeType,
       "CiscoCFSScopeValue": CiscoCFSScopeValue,
       "ciscoCFSMIB": ciscoCFSMIB,
       "ciscoCFSMIBNotifs": ciscoCFSMIBNotifs,
       "ciscoCFSFeatureActionNotif": ciscoCFSFeatureActionNotif,
       "ciscoCFSMergeFailNotif": ciscoCFSMergeFailNotif,
       "ciscoCFSDiscoveryCompleteNotif": ciscoCFSDiscoveryCompleteNotif,
       "ciscoCFSMIBObjects": ciscoCFSMIBObjects,
       "cfsFeature": cfsFeature,
       "cfsFeatureOpTable": cfsFeatureOpTable,
       "cfsFeatureOpEntry": cfsFeatureOpEntry,
       "cfsFeatureOpName": cfsFeatureOpName,
       "cfsFeatureOpAction": cfsFeatureOpAction,
       "cfsFeatureOpScopeType": cfsFeatureOpScopeType,
       "cfsFeatureOpScopeVal": cfsFeatureOpScopeVal,
       "cfsFeatureOpLastAction": cfsFeatureOpLastAction,
       "cfsFeatureOpLastScopeType": cfsFeatureOpLastScopeType,
       "cfsFeatureOpLastScopeVal": cfsFeatureOpLastScopeVal,
       "cfsFeatureOpLastActionResult": cfsFeatureOpLastActionResult,
       "cfsFeatureOpLastFailureReason": cfsFeatureOpLastFailureReason,
       "cfsFeatureOpShowCfgOption": cfsFeatureOpShowCfgOption,
       "cfsFeatureOpStatus": cfsFeatureOpStatus,
       "cfsFeatureOpAttribs": cfsFeatureOpAttribs,
       "cfsPendingConfOwnerTable": cfsPendingConfOwnerTable,
       "cfsPendingConfOwnerEntry": cfsPendingConfOwnerEntry,
       "cfsPendingConfOwnerScopeType": cfsPendingConfOwnerScopeType,
       "cfsPendingConfOwnerScopeVal": cfsPendingConfOwnerScopeVal,
       "cfsPendingConfOwnerAddrType": cfsPendingConfOwnerAddrType,
       "cfsPendingConfOwnerAddr": cfsPendingConfOwnerAddr,
       "cfsPendingConfOwnerIDType": cfsPendingConfOwnerIDType,
       "cfsPendingConfOwnerID": cfsPendingConfOwnerID,
       "cfsMergeStatusTable": cfsMergeStatusTable,
       "cfsMergeStatusEntry": cfsMergeStatusEntry,
       "cfsMergeStatusScopeType": cfsMergeStatusScopeType,
       "cfsMergeStatusScopeVal": cfsMergeStatusScopeVal,
       "cfsMergeStatusValue": cfsMergeStatusValue,
       "cfsMergeMembersTable": cfsMergeMembersTable,
       "cfsMergeMembersEntry": cfsMergeMembersEntry,
       "cfsMergeMemberAddrType": cfsMergeMemberAddrType,
       "cfsMergeMemberAddr": cfsMergeMemberAddr,
       "cfsMergeMemberFabricType": cfsMergeMemberFabricType,
       "cfsMergeMemberRole": cfsMergeMemberRole,
       "cfsPeersTable": cfsPeersTable,
       "cfsPeersEntry": cfsPeersEntry,
       "cfsPeerAddrType": cfsPeerAddrType,
       "cfsPeerAddr": cfsPeerAddr,
       "cfsFeaturePeersTable": cfsFeaturePeersTable,
       "cfsFeaturePeersEntry": cfsFeaturePeersEntry,
       "cfsFeaturePeersScopeType": cfsFeaturePeersScopeType,
       "cfsFeaturePeersScopeVal": cfsFeaturePeersScopeVal,
       "cfsFeaturePeersAddrType": cfsFeaturePeersAddrType,
       "cfsFeaturePeersAddr": cfsFeaturePeersAddr,
       "cfsFeatureOpExtTable": cfsFeatureOpExtTable,
       "cfsFeatureOpExtEntry": cfsFeatureOpExtEntry,
       "cfsFeatureOpExtScopeType": cfsFeatureOpExtScopeType,
       "cfsFeatureOpExtScopeVal": cfsFeatureOpExtScopeVal,
       "cfsFeatureOpExtLastAction": cfsFeatureOpExtLastAction,
       "cfsFeatureOpExtLastActionResult": cfsFeatureOpExtLastActionResult,
       "cfsFeatureOpExtLastFailureReason": cfsFeatureOpExtLastFailureReason,
       "cfsFeatureOpExtShowCfgOption": cfsFeatureOpExtShowCfgOption,
       "cfsFeatureOpExtLastActionTime": cfsFeatureOpExtLastActionTime,
       "cfsNotifObjects": cfsNotifObjects,
       "cfsMergeFailFeatureName": cfsMergeFailFeatureName,
       "cfsMergeFailScopeType": cfsMergeFailScopeType,
       "cfsMergeFailScopeVal": cfsMergeFailScopeVal,
       "cfsMergeFailReasonDescription": cfsMergeFailReasonDescription,
       "cfsDiscoveryObjects": cfsDiscoveryObjects,
       "cfsStartPeersDiscovery": cfsStartPeersDiscovery,
       "cfsPeersDiscoveryResult": cfsPeersDiscoveryResult,
       "cfsPeersDiscoveryFailureReason": cfsPeersDiscoveryFailureReason,
       "cfsDistCtrlObjects": cfsDistCtrlObjects,
       "cfsDistCtrl": cfsDistCtrl,
       "cfsDistCtrlTable": cfsDistCtrlTable,
       "cfsDistCtrlEntry": cfsDistCtrlEntry,
       "cfsDistCtrlAddrType": cfsDistCtrlAddrType,
       "cfsDistCtrlAddr": cfsDistCtrlAddr,
       "cfsDistCtrlAction": cfsDistCtrlAction,
       "ciscoCFSMIBConformance": ciscoCFSMIBConformance,
       "ciscoCFSMIBCompliances": ciscoCFSMIBCompliances,
       "ciscoCFSMIBCompliance": ciscoCFSMIBCompliance,
       "ciscoCFSMIBComplianceRev1": ciscoCFSMIBComplianceRev1,
       "ciscoCFSMIBComplianceRev2": ciscoCFSMIBComplianceRev2,
       "ciscoCFSMIBComplianceRev3": ciscoCFSMIBComplianceRev3,
       "ciscoCFSMIBGroups": ciscoCFSMIBGroups,
       "cfsFeatureOpGroup": cfsFeatureOpGroup,
       "cfsPendingConfOwnerGroup": cfsPendingConfOwnerGroup,
       "cfsFeatureNotifObjectsGroup": cfsFeatureNotifObjectsGroup,
       "cfsFeatureActionNotifGroup": cfsFeatureActionNotifGroup,
       "cfsMergeFailNotifGroup": cfsMergeFailNotifGroup,
       "cfsMembersGroup": cfsMembersGroup,
       "cfsFeatureOpExtGroup": cfsFeatureOpExtGroup,
       "cfsPeerDiscoveryNotifGroup": cfsPeerDiscoveryNotifGroup,
       "cfsFeatureOpGroupRev1": cfsFeatureOpGroupRev1,
       "cfsDistCtrlGroup": cfsDistCtrlGroup,
       "cfsDistCtrlInetGroup": cfsDistCtrlInetGroup,
       "cfsFeatureOpGroupRev2": cfsFeatureOpGroupRev2,
       "cfsFeatureOpExtGroupRev1": cfsFeatureOpExtGroupRev1}
)
