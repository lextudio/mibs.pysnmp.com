# SNMP MIB module (CISCO-MLD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MLD-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:43 2024
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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoMldSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721)
)
ciscoMldSnoopingMIB.setRevisions(
        ("2010-07-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoMldPortType(Integer32, TextualConvention):
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
        *(("interface", 2),
          ("pw", 3),
          ("unknown", 1))
    )



class CiscoMldPortIdentifier(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class CiscoMldPortInterface(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class CiscoMldPortPseudowire(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class CiscoMldSnoopingVersion(Integer32, TextualConvention):
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
        *(("unknown", 4),
          ("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoMldSnoopingMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoMldSnoopingMIBNotifs = _CiscoMldSnoopingMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 0)
)
_CiscoMldSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoMldSnoopingMIBObjects = _CiscoMldSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1)
)
_CmsConfiguration_ObjectIdentity = ObjectIdentity
cmsConfiguration = _CmsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1)
)
_CmsProfileTable_Object = MibTable
cmsProfileTable = _CmsProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cmsProfileTable.setStatus("current")
_CmsProfileEntry_Object = MibTableRow
cmsProfileEntry = _CmsProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1)
)
cmsProfileEntry.setIndexNames(
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsProfileName"),
)
if mibBuilder.loadTexts:
    cmsProfileEntry.setStatus("current")
_CmsProfileName_Type = SnmpAdminString
_CmsProfileName_Object = MibTableColumn
cmsProfileName = _CmsProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 1),
    _CmsProfileName_Type()
)
cmsProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmsProfileName.setStatus("current")
_CmsProfileStatus_Type = RowStatus
_CmsProfileStatus_Object = MibTableColumn
cmsProfileStatus = _CmsProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 2),
    _CmsProfileStatus_Type()
)
cmsProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsProfileStatus.setStatus("current")


class _CmsProfileStorageType_Type(StorageType):
    """Custom type cmsProfileStorageType based on StorageType"""


_CmsProfileStorageType_Object = MibTableColumn
cmsProfileStorageType = _CmsProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 3),
    _CmsProfileStorageType_Type()
)
cmsProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsProfileStorageType.setStatus("current")


class _CmsProfileSnoopMinVersion_Type(CiscoMldSnoopingVersion):
    """Custom type cmsProfileSnoopMinVersion based on CiscoMldSnoopingVersion"""


_CmsProfileSnoopMinVersion_Object = MibTableColumn
cmsProfileSnoopMinVersion = _CmsProfileSnoopMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 4),
    _CmsProfileSnoopMinVersion_Type()
)
cmsProfileSnoopMinVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsProfileSnoopMinVersion.setStatus("current")


class _CmsProfileIPAddrType_Type(InetAddressType):
    """Custom type cmsProfileIPAddrType based on InetAddressType"""


_CmsProfileIPAddrType_Object = MibTableColumn
cmsProfileIPAddrType = _CmsProfileIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 5),
    _CmsProfileIPAddrType_Type()
)
cmsProfileIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsProfileIPAddrType.setStatus("current")


class _CmsProfileIPAddress_Type(InetAddress):
    """Custom type cmsProfileIPAddress based on InetAddress"""
    defaultHexValue = "00000000"


_CmsProfileIPAddress_Object = MibTableColumn
cmsProfileIPAddress = _CmsProfileIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 6),
    _CmsProfileIPAddress_Type()
)
cmsProfileIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsProfileIPAddress.setStatus("current")


class _CmsProfileRobustnessVariable_Type(Unsigned32):
    """Custom type cmsProfileRobustnessVariable based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CmsProfileRobustnessVariable_Type.__name__ = "Unsigned32"
_CmsProfileRobustnessVariable_Object = MibTableColumn
cmsProfileRobustnessVariable = _CmsProfileRobustnessVariable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 7),
    _CmsProfileRobustnessVariable_Type()
)
cmsProfileRobustnessVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsProfileRobustnessVariable.setStatus("current")


class _CmsProfileInternalQuerier_Type(TruthValue):
    """Custom type cmsProfileInternalQuerier based on TruthValue"""


_CmsProfileInternalQuerier_Object = MibTableColumn
cmsProfileInternalQuerier = _CmsProfileInternalQuerier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 8),
    _CmsProfileInternalQuerier_Type()
)
cmsProfileInternalQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileInternalQuerier.setStatus("current")


class _CmsProfileLastMemberQueryCount_Type(Unsigned32):
    """Custom type cmsProfileLastMemberQueryCount based on Unsigned32"""
    defaultValue = 2


_CmsProfileLastMemberQueryCount_Object = MibTableColumn
cmsProfileLastMemberQueryCount = _CmsProfileLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 9),
    _CmsProfileLastMemberQueryCount_Type()
)
cmsProfileLastMemberQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileLastMemberQueryCount.setStatus("current")
if mibBuilder.loadTexts:
    cmsProfileLastMemberQueryCount.setUnits("queries")


class _CmsProfileLastMemberQueryInterval_Type(Unsigned32):
    """Custom type cmsProfileLastMemberQueryInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 5000),
    )


_CmsProfileLastMemberQueryInterval_Type.__name__ = "Unsigned32"
_CmsProfileLastMemberQueryInterval_Object = MibTableColumn
cmsProfileLastMemberQueryInterval = _CmsProfileLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 10),
    _CmsProfileLastMemberQueryInterval_Type()
)
cmsProfileLastMemberQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmsProfileLastMemberQueryInterval.setUnits("milliseconds")


class _CmsProfileSuppressReport_Type(TruthValue):
    """Custom type cmsProfileSuppressReport based on TruthValue"""


_CmsProfileSuppressReport_Object = MibTableColumn
cmsProfileSuppressReport = _CmsProfileSuppressReport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 11),
    _CmsProfileSuppressReport_Type()
)
cmsProfileSuppressReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileSuppressReport.setStatus("current")


class _CmsProfileUnsolicitedReportTimer_Type(Unsigned32):
    """Custom type cmsProfileUnsolicitedReportTimer based on Unsigned32"""
    defaultValue = 100


_CmsProfileUnsolicitedReportTimer_Object = MibTableColumn
cmsProfileUnsolicitedReportTimer = _CmsProfileUnsolicitedReportTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 12),
    _CmsProfileUnsolicitedReportTimer_Type()
)
cmsProfileUnsolicitedReportTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileUnsolicitedReportTimer.setStatus("current")
if mibBuilder.loadTexts:
    cmsProfileUnsolicitedReportTimer.setUnits("milliseconds")


class _CmsProfileFloodQueryCount_Type(Unsigned32):
    """Custom type cmsProfileFloodQueryCount based on Unsigned32"""
    defaultValue = 1


_CmsProfileFloodQueryCount_Object = MibTableColumn
cmsProfileFloodQueryCount = _CmsProfileFloodQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 13),
    _CmsProfileFloodQueryCount_Type()
)
cmsProfileFloodQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileFloodQueryCount.setStatus("current")


class _CmsProfileQuerySolicit_Type(TruthValue):
    """Custom type cmsProfileQuerySolicit based on TruthValue"""


_CmsProfileQuerySolicit_Object = MibTableColumn
cmsProfileQuerySolicit = _CmsProfileQuerySolicit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 14),
    _CmsProfileQuerySolicit_Type()
)
cmsProfileQuerySolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileQuerySolicit.setStatus("current")


class _CmsProfileTTLCheck_Type(TruthValue):
    """Custom type cmsProfileTTLCheck based on TruthValue"""


_CmsProfileTTLCheck_Object = MibTableColumn
cmsProfileTTLCheck = _CmsProfileTTLCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 15),
    _CmsProfileTTLCheck_Type()
)
cmsProfileTTLCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileTTLCheck.setStatus("current")


class _CmsProfileRouterAlertCheck_Type(TruthValue):
    """Custom type cmsProfileRouterAlertCheck based on TruthValue"""


_CmsProfileRouterAlertCheck_Object = MibTableColumn
cmsProfileRouterAlertCheck = _CmsProfileRouterAlertCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 16),
    _CmsProfileRouterAlertCheck_Type()
)
cmsProfileRouterAlertCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileRouterAlertCheck.setStatus("current")


class _CmsProfileIntQuerierMaxRespTime_Type(Unsigned32):
    """Custom type cmsProfileIntQuerierMaxRespTime based on Unsigned32"""
    defaultValue = 1


_CmsProfileIntQuerierMaxRespTime_Object = MibTableColumn
cmsProfileIntQuerierMaxRespTime = _CmsProfileIntQuerierMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 17),
    _CmsProfileIntQuerierMaxRespTime_Type()
)
cmsProfileIntQuerierMaxRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierMaxRespTime.setStatus("current")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierMaxRespTime.setUnits("seconds")


class _CmsProfileIntQuerierQueryInterval_Type(Unsigned32):
    """Custom type cmsProfileIntQuerierQueryInterval based on Unsigned32"""
    defaultValue = 1


_CmsProfileIntQuerierQueryInterval_Object = MibTableColumn
cmsProfileIntQuerierQueryInterval = _CmsProfileIntQuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 18),
    _CmsProfileIntQuerierQueryInterval_Type()
)
cmsProfileIntQuerierQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierQueryInterval.setUnits("seconds")


class _CmsProfileIntQuerierTCNQueryCount_Type(Unsigned32):
    """Custom type cmsProfileIntQuerierTCNQueryCount based on Unsigned32"""
    defaultValue = 0


_CmsProfileIntQuerierTCNQueryCount_Object = MibTableColumn
cmsProfileIntQuerierTCNQueryCount = _CmsProfileIntQuerierTCNQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 19),
    _CmsProfileIntQuerierTCNQueryCount_Type()
)
cmsProfileIntQuerierTCNQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierTCNQueryCount.setStatus("current")


class _CmsProfileIntQuerierTCNQueryInterval_Type(Unsigned32):
    """Custom type cmsProfileIntQuerierTCNQueryInterval based on Unsigned32"""
    defaultValue = 1


_CmsProfileIntQuerierTCNQueryInterval_Object = MibTableColumn
cmsProfileIntQuerierTCNQueryInterval = _CmsProfileIntQuerierTCNQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 20),
    _CmsProfileIntQuerierTCNQueryInterval_Type()
)
cmsProfileIntQuerierTCNQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierTCNQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierTCNQueryInterval.setUnits("seconds")


class _CmsProfileIntQuerierExpiry_Type(Unsigned32):
    """Custom type cmsProfileIntQuerierExpiry based on Unsigned32"""
    defaultValue = 60


_CmsProfileIntQuerierExpiry_Object = MibTableColumn
cmsProfileIntQuerierExpiry = _CmsProfileIntQuerierExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 21),
    _CmsProfileIntQuerierExpiry_Type()
)
cmsProfileIntQuerierExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierExpiry.setStatus("current")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierExpiry.setUnits("seconds")


class _CmsProfileIntQuerierVersion_Type(CiscoMldSnoopingVersion):
    """Custom type cmsProfileIntQuerierVersion based on CiscoMldSnoopingVersion"""


_CmsProfileIntQuerierVersion_Object = MibTableColumn
cmsProfileIntQuerierVersion = _CmsProfileIntQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 22),
    _CmsProfileIntQuerierVersion_Type()
)
cmsProfileIntQuerierVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsProfileIntQuerierVersion.setStatus("current")


class _CmsProfileRouterGuard_Type(TruthValue):
    """Custom type cmsProfileRouterGuard based on TruthValue"""


_CmsProfileRouterGuard_Object = MibTableColumn
cmsProfileRouterGuard = _CmsProfileRouterGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 23),
    _CmsProfileRouterGuard_Type()
)
cmsProfileRouterGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileRouterGuard.setStatus("current")


class _CmsProfileStaticMRouter_Type(TruthValue):
    """Custom type cmsProfileStaticMRouter based on TruthValue"""


_CmsProfileStaticMRouter_Object = MibTableColumn
cmsProfileStaticMRouter = _CmsProfileStaticMRouter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 24),
    _CmsProfileStaticMRouter_Type()
)
cmsProfileStaticMRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileStaticMRouter.setStatus("current")


class _CmsProfileImmediateLeave_Type(TruthValue):
    """Custom type cmsProfileImmediateLeave based on TruthValue"""


_CmsProfileImmediateLeave_Object = MibTableColumn
cmsProfileImmediateLeave = _CmsProfileImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 1, 1, 25),
    _CmsProfileImmediateLeave_Type()
)
cmsProfileImmediateLeave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsProfileImmediateLeave.setStatus("current")
_CmsConfigPortTable_Object = MibTable
cmsConfigPortTable = _CmsConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cmsConfigPortTable.setStatus("current")
_CmsConfigPortEntry_Object = MibTableRow
cmsConfigPortEntry = _CmsConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 2, 1)
)
cmsConfigPortEntry.setIndexNames(
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortType"),
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortId"),
)
if mibBuilder.loadTexts:
    cmsConfigPortEntry.setStatus("current")
_CmsPortType_Type = CiscoMldPortType
_CmsPortType_Object = MibTableColumn
cmsPortType = _CmsPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 2, 1, 1),
    _CmsPortType_Type()
)
cmsPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmsPortType.setStatus("current")
_CmsPortId_Type = CiscoMldPortIdentifier
_CmsPortId_Object = MibTableColumn
cmsPortId = _CmsPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 2, 1, 2),
    _CmsPortId_Type()
)
cmsPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmsPortId.setStatus("current")
_CmsConfigPortStatus_Type = RowStatus
_CmsConfigPortStatus_Object = MibTableColumn
cmsConfigPortStatus = _CmsConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 2, 1, 3),
    _CmsConfigPortStatus_Type()
)
cmsConfigPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsConfigPortStatus.setStatus("current")


class _CmsConfigPortStorageType_Type(StorageType):
    """Custom type cmsConfigPortStorageType based on StorageType"""


_CmsConfigPortStorageType_Object = MibTableColumn
cmsConfigPortStorageType = _CmsConfigPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 2, 1, 4),
    _CmsConfigPortStorageType_Type()
)
cmsConfigPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsConfigPortStorageType.setStatus("current")
_CmsConfigPortProfileName_Type = SnmpAdminString
_CmsConfigPortProfileName_Object = MibTableColumn
cmsConfigPortProfileName = _CmsConfigPortProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 2, 1, 5),
    _CmsConfigPortProfileName_Type()
)
cmsConfigPortProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cmsConfigPortProfileName.setStatus("current")
_CmsConfigSystemProfileName_Type = SnmpAdminString
_CmsConfigSystemProfileName_Object = MibScalar
cmsConfigSystemProfileName = _CmsConfigSystemProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 1, 3),
    _CmsConfigSystemProfileName_Type()
)
cmsConfigSystemProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsConfigSystemProfileName.setStatus("current")
_CmsSystemInfo_ObjectIdentity = ObjectIdentity
cmsSystemInfo = _CmsSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 2)
)
_CmsOperInfo_ObjectIdentity = ObjectIdentity
cmsOperInfo = _CmsOperInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3)
)
_CmsQuerierIPAddrType_Type = InetAddressType
_CmsQuerierIPAddrType_Object = MibScalar
cmsQuerierIPAddrType = _CmsQuerierIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 1),
    _CmsQuerierIPAddrType_Type()
)
cmsQuerierIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierIPAddrType.setStatus("current")
_CmsQuerierIPAddr_Type = InetAddress
_CmsQuerierIPAddr_Object = MibScalar
cmsQuerierIPAddr = _CmsQuerierIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 2),
    _CmsQuerierIPAddr_Type()
)
cmsQuerierIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierIPAddr.setStatus("current")
_CmsQuerierPortType_Type = CiscoMldPortType
_CmsQuerierPortType_Object = MibScalar
cmsQuerierPortType = _CmsQuerierPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 3),
    _CmsQuerierPortType_Type()
)
cmsQuerierPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierPortType.setStatus("current")
_CmsQuerierPortId_Type = CiscoMldPortIdentifier
_CmsQuerierPortId_Object = MibScalar
cmsQuerierPortId = _CmsQuerierPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 4),
    _CmsQuerierPortId_Type()
)
cmsQuerierPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierPortId.setStatus("current")
_CmsQuerierVersion_Type = CiscoMldSnoopingVersion
_CmsQuerierVersion_Object = MibScalar
cmsQuerierVersion = _CmsQuerierVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 5),
    _CmsQuerierVersion_Type()
)
cmsQuerierVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierVersion.setStatus("current")
_CmsQuerierQueryInterval_Type = Unsigned32
_CmsQuerierQueryInterval_Object = MibScalar
cmsQuerierQueryInterval = _CmsQuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 6),
    _CmsQuerierQueryInterval_Type()
)
cmsQuerierQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cmsQuerierQueryInterval.setUnits("seconds")
_CmsQuerierRobustness_Type = Unsigned32
_CmsQuerierRobustness_Object = MibScalar
cmsQuerierRobustness = _CmsQuerierRobustness_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 7),
    _CmsQuerierRobustness_Type()
)
cmsQuerierRobustness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierRobustness.setStatus("current")
_CmsQuerierMaxRespTime_Type = Unsigned32
_CmsQuerierMaxRespTime_Object = MibScalar
cmsQuerierMaxRespTime = _CmsQuerierMaxRespTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 8),
    _CmsQuerierMaxRespTime_Type()
)
cmsQuerierMaxRespTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierMaxRespTime.setStatus("current")
if mibBuilder.loadTexts:
    cmsQuerierMaxRespTime.setUnits("seconds")
_CmsQuerierTimeSinceLastGQuery_Type = Unsigned32
_CmsQuerierTimeSinceLastGQuery_Object = MibScalar
cmsQuerierTimeSinceLastGQuery = _CmsQuerierTimeSinceLastGQuery_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 9),
    _CmsQuerierTimeSinceLastGQuery_Type()
)
cmsQuerierTimeSinceLastGQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsQuerierTimeSinceLastGQuery.setStatus("current")
if mibBuilder.loadTexts:
    cmsQuerierTimeSinceLastGQuery.setUnits("seconds")
_CmsMcastInfoTable_Object = MibTable
cmsMcastInfoTable = _CmsMcastInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10)
)
if mibBuilder.loadTexts:
    cmsMcastInfoTable.setStatus("current")
_CmsMcastInfoEntry_Object = MibTableRow
cmsMcastInfoEntry = _CmsMcastInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10, 1)
)
cmsMcastInfoEntry.setIndexNames(
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortType"),
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortId"),
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsMcastInfoGroupAddrType"),
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsMcastInfoGroupAddr"),
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsMcastInfoSourceAddr"),
)
if mibBuilder.loadTexts:
    cmsMcastInfoEntry.setStatus("current")
_CmsMcastInfoGroupAddrType_Type = InetAddressType
_CmsMcastInfoGroupAddrType_Object = MibTableColumn
cmsMcastInfoGroupAddrType = _CmsMcastInfoGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10, 1, 1),
    _CmsMcastInfoGroupAddrType_Type()
)
cmsMcastInfoGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmsMcastInfoGroupAddrType.setStatus("current")
_CmsMcastInfoGroupAddr_Type = InetAddress
_CmsMcastInfoGroupAddr_Object = MibTableColumn
cmsMcastInfoGroupAddr = _CmsMcastInfoGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10, 1, 2),
    _CmsMcastInfoGroupAddr_Type()
)
cmsMcastInfoGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmsMcastInfoGroupAddr.setStatus("current")
_CmsMcastInfoSourceAddr_Type = InetAddress
_CmsMcastInfoSourceAddr_Object = MibTableColumn
cmsMcastInfoSourceAddr = _CmsMcastInfoSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10, 1, 3),
    _CmsMcastInfoSourceAddr_Type()
)
cmsMcastInfoSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cmsMcastInfoSourceAddr.setStatus("current")


class _CmsMcastInfoGroupFilter_Type(Integer32):
    """Custom type cmsMcastInfoGroupFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 1),
          ("include", 2))
    )


_CmsMcastInfoGroupFilter_Type.__name__ = "Integer32"
_CmsMcastInfoGroupFilter_Object = MibTableColumn
cmsMcastInfoGroupFilter = _CmsMcastInfoGroupFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10, 1, 4),
    _CmsMcastInfoGroupFilter_Type()
)
cmsMcastInfoGroupFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsMcastInfoGroupFilter.setStatus("current")
_CmsMcastInfoExpiry_Type = Unsigned32
_CmsMcastInfoExpiry_Object = MibTableColumn
cmsMcastInfoExpiry = _CmsMcastInfoExpiry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10, 1, 5),
    _CmsMcastInfoExpiry_Type()
)
cmsMcastInfoExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsMcastInfoExpiry.setStatus("current")
if mibBuilder.loadTexts:
    cmsMcastInfoExpiry.setUnits("seconds")


class _CmsMcastInfoFlag_Type(Integer32):
    """Custom type cmsMcastInfoFlag based on Integer32"""
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
        *(("dynamic", 2),
          ("static", 1),
          ("staticAndDynamic", 3),
          ("unknown", 4))
    )


_CmsMcastInfoFlag_Type.__name__ = "Integer32"
_CmsMcastInfoFlag_Object = MibTableColumn
cmsMcastInfoFlag = _CmsMcastInfoFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 10, 1, 6),
    _CmsMcastInfoFlag_Type()
)
cmsMcastInfoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsMcastInfoFlag.setStatus("current")
_CmsMRouterPortInfoTable_Object = MibTable
cmsMRouterPortInfoTable = _CmsMRouterPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 11)
)
if mibBuilder.loadTexts:
    cmsMRouterPortInfoTable.setStatus("current")
_CmsMRouterPortInfoEntry_Object = MibTableRow
cmsMRouterPortInfoEntry = _CmsMRouterPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 11, 1)
)
cmsMRouterPortInfoEntry.setIndexNames(
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortType"),
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortId"),
)
if mibBuilder.loadTexts:
    cmsMRouterPortInfoEntry.setStatus("current")


class _CmsMRouterType_Type(Integer32):
    """Custom type cmsMRouterType based on Integer32"""
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
        *(("dynamic", 2),
          ("static", 1),
          ("staticAndDynamic", 3),
          ("unknown", 4))
    )


_CmsMRouterType_Type.__name__ = "Integer32"
_CmsMRouterType_Object = MibTableColumn
cmsMRouterType = _CmsMRouterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 3, 11, 1, 1),
    _CmsMRouterType_Type()
)
cmsMRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsMRouterType.setStatus("current")
_CmsSystemStats_ObjectIdentity = ObjectIdentity
cmsSystemStats = _CmsSystemStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4)
)
_CmsSysIntQuerierRxGeneralQueries_Type = Counter32
_CmsSysIntQuerierRxGeneralQueries_Object = MibScalar
cmsSysIntQuerierRxGeneralQueries = _CmsSysIntQuerierRxGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 1),
    _CmsSysIntQuerierRxGeneralQueries_Type()
)
cmsSysIntQuerierRxGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueries.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueries.setUnits("packets")
_CmsSysIntQuerierRxGeneralQueriesWhenDisabled_Type = Counter32
_CmsSysIntQuerierRxGeneralQueriesWhenDisabled_Object = MibScalar
cmsSysIntQuerierRxGeneralQueriesWhenDisabled = _CmsSysIntQuerierRxGeneralQueriesWhenDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 2),
    _CmsSysIntQuerierRxGeneralQueriesWhenDisabled_Type()
)
cmsSysIntQuerierRxGeneralQueriesWhenDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesWhenDisabled.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesWhenDisabled.setUnits("packets")
_CmsSysIntQuerierRxGeneralQueriesAsQuerier_Type = Counter32
_CmsSysIntQuerierRxGeneralQueriesAsQuerier_Object = MibScalar
cmsSysIntQuerierRxGeneralQueriesAsQuerier = _CmsSysIntQuerierRxGeneralQueriesAsQuerier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 3),
    _CmsSysIntQuerierRxGeneralQueriesAsQuerier_Type()
)
cmsSysIntQuerierRxGeneralQueriesAsQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsQuerier.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsQuerier.setUnits("packets")
_CmsSysIntQuerierRxGeneralQueriesAsNonQuerier_Type = Counter32
_CmsSysIntQuerierRxGeneralQueriesAsNonQuerier_Object = MibScalar
cmsSysIntQuerierRxGeneralQueriesAsNonQuerier = _CmsSysIntQuerierRxGeneralQueriesAsNonQuerier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 4),
    _CmsSysIntQuerierRxGeneralQueriesAsNonQuerier_Type()
)
cmsSysIntQuerierRxGeneralQueriesAsNonQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsNonQuerier.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsNonQuerier.setUnits("packets")
_CmsSysIntQuerierRxGeneralQueriesAsWinner_Type = Counter32
_CmsSysIntQuerierRxGeneralQueriesAsWinner_Object = MibScalar
cmsSysIntQuerierRxGeneralQueriesAsWinner = _CmsSysIntQuerierRxGeneralQueriesAsWinner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 5),
    _CmsSysIntQuerierRxGeneralQueriesAsWinner_Type()
)
cmsSysIntQuerierRxGeneralQueriesAsWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsWinner.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsWinner.setUnits("packets")
_CmsSysIntQuerierRxGeneralQueriesAsLoser_Type = Counter32
_CmsSysIntQuerierRxGeneralQueriesAsLoser_Object = MibScalar
cmsSysIntQuerierRxGeneralQueriesAsLoser = _CmsSysIntQuerierRxGeneralQueriesAsLoser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 6),
    _CmsSysIntQuerierRxGeneralQueriesAsLoser_Type()
)
cmsSysIntQuerierRxGeneralQueriesAsLoser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsLoser.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGeneralQueriesAsLoser.setUnits("packets")
_CmsSysIntQuerierRxGlobalLeaves_Type = Counter32
_CmsSysIntQuerierRxGlobalLeaves_Object = MibScalar
cmsSysIntQuerierRxGlobalLeaves = _CmsSysIntQuerierRxGlobalLeaves_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 7),
    _CmsSysIntQuerierRxGlobalLeaves_Type()
)
cmsSysIntQuerierRxGlobalLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeaves.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeaves.setUnits("packets")
_CmsSysIntQuerierRxGlobalLeavesWhenDisabled_Type = Counter32
_CmsSysIntQuerierRxGlobalLeavesWhenDisabled_Object = MibScalar
cmsSysIntQuerierRxGlobalLeavesWhenDisabled = _CmsSysIntQuerierRxGlobalLeavesWhenDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 8),
    _CmsSysIntQuerierRxGlobalLeavesWhenDisabled_Type()
)
cmsSysIntQuerierRxGlobalLeavesWhenDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeavesWhenDisabled.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeavesWhenDisabled.setUnits("packets")
_CmsSysIntQuerierRxGlobalLeavsAsNonQuerier_Type = Counter32
_CmsSysIntQuerierRxGlobalLeavsAsNonQuerier_Object = MibScalar
cmsSysIntQuerierRxGlobalLeavsAsNonQuerier = _CmsSysIntQuerierRxGlobalLeavsAsNonQuerier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 9),
    _CmsSysIntQuerierRxGlobalLeavsAsNonQuerier_Type()
)
cmsSysIntQuerierRxGlobalLeavsAsNonQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeavsAsNonQuerier.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeavsAsNonQuerier.setUnits("packets")
_CmsSysIntQuerierRxGlobalLeavesIgnored_Type = Counter32
_CmsSysIntQuerierRxGlobalLeavesIgnored_Object = MibScalar
cmsSysIntQuerierRxGlobalLeavesIgnored = _CmsSysIntQuerierRxGlobalLeavesIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 10),
    _CmsSysIntQuerierRxGlobalLeavesIgnored_Type()
)
cmsSysIntQuerierRxGlobalLeavesIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeavesIgnored.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxGlobalLeavesIgnored.setUnits("packets")
_CmsSysIntQuerierRxPimEnabledNotifications_Type = Counter32
_CmsSysIntQuerierRxPimEnabledNotifications_Object = MibScalar
cmsSysIntQuerierRxPimEnabledNotifications = _CmsSysIntQuerierRxPimEnabledNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 11),
    _CmsSysIntQuerierRxPimEnabledNotifications_Type()
)
cmsSysIntQuerierRxPimEnabledNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxPimEnabledNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxPimEnabledNotifications.setUnits("packets")
_CmsSysIntQuerierRxPimDisabledNotifications_Type = Counter32
_CmsSysIntQuerierRxPimDisabledNotifications_Object = MibScalar
cmsSysIntQuerierRxPimDisabledNotifications = _CmsSysIntQuerierRxPimDisabledNotifications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 12),
    _CmsSysIntQuerierRxPimDisabledNotifications_Type()
)
cmsSysIntQuerierRxPimDisabledNotifications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxPimDisabledNotifications.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxPimDisabledNotifications.setUnits("packets")
_CmsSysIntQuerierRxLocalQuerySolicitations_Type = Counter32
_CmsSysIntQuerierRxLocalQuerySolicitations_Object = MibScalar
cmsSysIntQuerierRxLocalQuerySolicitations = _CmsSysIntQuerierRxLocalQuerySolicitations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 13),
    _CmsSysIntQuerierRxLocalQuerySolicitations_Type()
)
cmsSysIntQuerierRxLocalQuerySolicitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxLocalQuerySolicitations.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierRxLocalQuerySolicitations.setUnits("packets")
_CmsSysIntQuerierTxGeneralQueries_Type = Counter32
_CmsSysIntQuerierTxGeneralQueries_Object = MibScalar
cmsSysIntQuerierTxGeneralQueries = _CmsSysIntQuerierTxGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 14),
    _CmsSysIntQuerierTxGeneralQueries_Type()
)
cmsSysIntQuerierTxGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysIntQuerierTxGeneralQueries.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysIntQuerierTxGeneralQueries.setUnits("packets")
_CmsSysTrfGeneralQueriesReceived_Type = Counter32
_CmsSysTrfGeneralQueriesReceived_Object = MibScalar
cmsSysTrfGeneralQueriesReceived = _CmsSysTrfGeneralQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 15),
    _CmsSysTrfGeneralQueriesReceived_Type()
)
cmsSysTrfGeneralQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGeneralQueriesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGeneralQueriesReceived.setUnits("packets")
_CmsSysTrfGeneralQueriesReinjected_Type = Counter32
_CmsSysTrfGeneralQueriesReinjected_Object = MibScalar
cmsSysTrfGeneralQueriesReinjected = _CmsSysTrfGeneralQueriesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 16),
    _CmsSysTrfGeneralQueriesReinjected_Type()
)
cmsSysTrfGeneralQueriesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGeneralQueriesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGeneralQueriesReinjected.setUnits("packets")
_CmsSysTrfGeneralQueriesGenerated_Type = Counter32
_CmsSysTrfGeneralQueriesGenerated_Object = MibScalar
cmsSysTrfGeneralQueriesGenerated = _CmsSysTrfGeneralQueriesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 17),
    _CmsSysTrfGeneralQueriesGenerated_Type()
)
cmsSysTrfGeneralQueriesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGeneralQueriesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGeneralQueriesGenerated.setUnits("packets")
_CmsSysTrfGrpSpecificQueriesReceived_Type = Counter32
_CmsSysTrfGrpSpecificQueriesReceived_Object = MibScalar
cmsSysTrfGrpSpecificQueriesReceived = _CmsSysTrfGrpSpecificQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 18),
    _CmsSysTrfGrpSpecificQueriesReceived_Type()
)
cmsSysTrfGrpSpecificQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGrpSpecificQueriesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGrpSpecificQueriesReceived.setUnits("packets")
_CmsSysTrfGrpSpecificQueriesReinjected_Type = Unsigned32
_CmsSysTrfGrpSpecificQueriesReinjected_Object = MibScalar
cmsSysTrfGrpSpecificQueriesReinjected = _CmsSysTrfGrpSpecificQueriesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 19),
    _CmsSysTrfGrpSpecificQueriesReinjected_Type()
)
cmsSysTrfGrpSpecificQueriesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGrpSpecificQueriesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGrpSpecificQueriesReinjected.setUnits("packets")
_CmsSysTrfGrpSpecificQueriesGenerated_Type = Counter32
_CmsSysTrfGrpSpecificQueriesGenerated_Object = MibScalar
cmsSysTrfGrpSpecificQueriesGenerated = _CmsSysTrfGrpSpecificQueriesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 20),
    _CmsSysTrfGrpSpecificQueriesGenerated_Type()
)
cmsSysTrfGrpSpecificQueriesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGrpSpecificQueriesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGrpSpecificQueriesGenerated.setUnits("packets")
_CmsSysTrfGSSpecificQueriesReceived_Type = Counter32
_CmsSysTrfGSSpecificQueriesReceived_Object = MibScalar
cmsSysTrfGSSpecificQueriesReceived = _CmsSysTrfGSSpecificQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 21),
    _CmsSysTrfGSSpecificQueriesReceived_Type()
)
cmsSysTrfGSSpecificQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGSSpecificQueriesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGSSpecificQueriesReceived.setUnits("packets")
_CmsSysTrfGSSpecificQueriesReinjected_Type = Counter32
_CmsSysTrfGSSpecificQueriesReinjected_Object = MibScalar
cmsSysTrfGSSpecificQueriesReinjected = _CmsSysTrfGSSpecificQueriesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 22),
    _CmsSysTrfGSSpecificQueriesReinjected_Type()
)
cmsSysTrfGSSpecificQueriesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGSSpecificQueriesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGSSpecificQueriesReinjected.setUnits("packets")
_CmsSysTrfGSSpecificQueriesGenerated_Type = Counter32
_CmsSysTrfGSSpecificQueriesGenerated_Object = MibScalar
cmsSysTrfGSSpecificQueriesGenerated = _CmsSysTrfGSSpecificQueriesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 23),
    _CmsSysTrfGSSpecificQueriesGenerated_Type()
)
cmsSysTrfGSSpecificQueriesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGSSpecificQueriesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGSSpecificQueriesGenerated.setUnits("packets")
_CmsSysTrfV2ReportReceived_Type = Counter32
_CmsSysTrfV2ReportReceived_Object = MibScalar
cmsSysTrfV2ReportReceived = _CmsSysTrfV2ReportReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 24),
    _CmsSysTrfV2ReportReceived_Type()
)
cmsSysTrfV2ReportReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfV2ReportReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfV2ReportReceived.setUnits("packets")
_CmsSysTrfV2ReportReinjected_Type = Counter32
_CmsSysTrfV2ReportReinjected_Object = MibScalar
cmsSysTrfV2ReportReinjected = _CmsSysTrfV2ReportReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 25),
    _CmsSysTrfV2ReportReinjected_Type()
)
cmsSysTrfV2ReportReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfV2ReportReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfV2ReportReinjected.setUnits("packets")
_CmsSysTrfV2ReportGenerated_Type = Counter32
_CmsSysTrfV2ReportGenerated_Object = MibScalar
cmsSysTrfV2ReportGenerated = _CmsSysTrfV2ReportGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 26),
    _CmsSysTrfV2ReportGenerated_Type()
)
cmsSysTrfV2ReportGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfV2ReportGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfV2ReportGenerated.setUnits("packets")
_CmsSysTrfV3ReportReceived_Type = Counter32
_CmsSysTrfV3ReportReceived_Object = MibScalar
cmsSysTrfV3ReportReceived = _CmsSysTrfV3ReportReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 27),
    _CmsSysTrfV3ReportReceived_Type()
)
cmsSysTrfV3ReportReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfV3ReportReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfV3ReportReceived.setUnits("packets")
_CmsSysTrfV3ReportReinjected_Type = Counter32
_CmsSysTrfV3ReportReinjected_Object = MibScalar
cmsSysTrfV3ReportReinjected = _CmsSysTrfV3ReportReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 28),
    _CmsSysTrfV3ReportReinjected_Type()
)
cmsSysTrfV3ReportReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfV3ReportReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfV3ReportReinjected.setUnits("packets")
_CmsSysTrfV3ReportGenerated_Type = Counter32
_CmsSysTrfV3ReportGenerated_Object = MibScalar
cmsSysTrfV3ReportGenerated = _CmsSysTrfV3ReportGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 29),
    _CmsSysTrfV3ReportGenerated_Type()
)
cmsSysTrfV3ReportGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfV3ReportGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfV3ReportGenerated.setUnits("packets")
_CmsSysTrfGlobalLeavesReceived_Type = Counter32
_CmsSysTrfGlobalLeavesReceived_Object = MibScalar
cmsSysTrfGlobalLeavesReceived = _CmsSysTrfGlobalLeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 30),
    _CmsSysTrfGlobalLeavesReceived_Type()
)
cmsSysTrfGlobalLeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGlobalLeavesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGlobalLeavesReceived.setUnits("packets")
_CmsSysTrfGlobalLeavesReinjected_Type = Counter32
_CmsSysTrfGlobalLeavesReinjected_Object = MibScalar
cmsSysTrfGlobalLeavesReinjected = _CmsSysTrfGlobalLeavesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 31),
    _CmsSysTrfGlobalLeavesReinjected_Type()
)
cmsSysTrfGlobalLeavesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGlobalLeavesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGlobalLeavesReinjected.setUnits("packets")
_CmsSysTrfGlobalLeavesGenerated_Type = Counter32
_CmsSysTrfGlobalLeavesGenerated_Object = MibScalar
cmsSysTrfGlobalLeavesGenerated = _CmsSysTrfGlobalLeavesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 32),
    _CmsSysTrfGlobalLeavesGenerated_Type()
)
cmsSysTrfGlobalLeavesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfGlobalLeavesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfGlobalLeavesGenerated.setUnits("packets")
_CmsSysTrfPIMHellosReceived_Type = Counter32
_CmsSysTrfPIMHellosReceived_Object = MibScalar
cmsSysTrfPIMHellosReceived = _CmsSysTrfPIMHellosReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 33),
    _CmsSysTrfPIMHellosReceived_Type()
)
cmsSysTrfPIMHellosReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfPIMHellosReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfPIMHellosReceived.setUnits("packets")
_CmsSysTrfPIMHellosReinjected_Type = Counter32
_CmsSysTrfPIMHellosReinjected_Object = MibScalar
cmsSysTrfPIMHellosReinjected = _CmsSysTrfPIMHellosReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 34),
    _CmsSysTrfPIMHellosReinjected_Type()
)
cmsSysTrfPIMHellosReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfPIMHellosReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfPIMHellosReinjected.setUnits("packets")
_CmsSysTrfPIMHellosGenerated_Type = Unsigned32
_CmsSysTrfPIMHellosGenerated_Object = MibScalar
cmsSysTrfPIMHellosGenerated = _CmsSysTrfPIMHellosGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 35),
    _CmsSysTrfPIMHellosGenerated_Type()
)
cmsSysTrfPIMHellosGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfPIMHellosGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfPIMHellosGenerated.setUnits("packets")
_CmsSysTrfRxPcktsFlooded_Type = Counter32
_CmsSysTrfRxPcktsFlooded_Object = MibScalar
cmsSysTrfRxPcktsFlooded = _CmsSysTrfRxPcktsFlooded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 36),
    _CmsSysTrfRxPcktsFlooded_Type()
)
cmsSysTrfRxPcktsFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsFlooded.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsFlooded.setUnits("packets")
_CmsSysTrfRxPcktsFwdToMembers_Type = Counter32
_CmsSysTrfRxPcktsFwdToMembers_Object = MibScalar
cmsSysTrfRxPcktsFwdToMembers = _CmsSysTrfRxPcktsFwdToMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 37),
    _CmsSysTrfRxPcktsFwdToMembers_Type()
)
cmsSysTrfRxPcktsFwdToMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsFwdToMembers.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsFwdToMembers.setUnits("packets")
_CmsSysTrfRxPcktsFwdToMrouters_Type = Counter32
_CmsSysTrfRxPcktsFwdToMrouters_Object = MibScalar
cmsSysTrfRxPcktsFwdToMrouters = _CmsSysTrfRxPcktsFwdToMrouters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 38),
    _CmsSysTrfRxPcktsFwdToMrouters_Type()
)
cmsSysTrfRxPcktsFwdToMrouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsFwdToMrouters.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsFwdToMrouters.setUnits("packets")
_CmsSysTrfRxPcktsConsumed_Type = Counter32
_CmsSysTrfRxPcktsConsumed_Object = MibScalar
cmsSysTrfRxPcktsConsumed = _CmsSysTrfRxPcktsConsumed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 39),
    _CmsSysTrfRxPcktsConsumed_Type()
)
cmsSysTrfRxPcktsConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsConsumed.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfRxPcktsConsumed.setUnits("packets")
_CmsSysTrfRxErrors_Type = Counter32
_CmsSysTrfRxErrors_Object = MibScalar
cmsSysTrfRxErrors = _CmsSysTrfRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 40),
    _CmsSysTrfRxErrors_Type()
)
cmsSysTrfRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfRxErrors.setUnits("packets")
_CmsSysTrfRxOther_Type = Counter32
_CmsSysTrfRxOther_Object = MibScalar
cmsSysTrfRxOther = _CmsSysTrfRxOther_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 41),
    _CmsSysTrfRxOther_Type()
)
cmsSysTrfRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfRxOther.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfRxOther.setUnits("packets")
_CmsSysTrfTxErrors_Type = Counter32
_CmsSysTrfTxErrors_Object = MibScalar
cmsSysTrfTxErrors = _CmsSysTrfTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 42),
    _CmsSysTrfTxErrors_Type()
)
cmsSysTrfTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysTrfTxErrors.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysTrfTxErrors.setUnits("packets")
_CmsSysRxV3RepIsInclude_Type = Counter32
_CmsSysRxV3RepIsInclude_Object = MibScalar
cmsSysRxV3RepIsInclude = _CmsSysRxV3RepIsInclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 43),
    _CmsSysRxV3RepIsInclude_Type()
)
cmsSysRxV3RepIsInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysRxV3RepIsInclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysRxV3RepIsInclude.setUnits("packets")
_CmsSysRxV3RepChangeToInclude_Type = Counter32
_CmsSysRxV3RepChangeToInclude_Object = MibScalar
cmsSysRxV3RepChangeToInclude = _CmsSysRxV3RepChangeToInclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 44),
    _CmsSysRxV3RepChangeToInclude_Type()
)
cmsSysRxV3RepChangeToInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysRxV3RepChangeToInclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysRxV3RepChangeToInclude.setUnits("packets")
_CmsSysRxV3RepIsExclude_Type = Counter32
_CmsSysRxV3RepIsExclude_Object = MibScalar
cmsSysRxV3RepIsExclude = _CmsSysRxV3RepIsExclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 45),
    _CmsSysRxV3RepIsExclude_Type()
)
cmsSysRxV3RepIsExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysRxV3RepIsExclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysRxV3RepIsExclude.setUnits("packets")
_CmsSysRxV3RepChangeToExclude_Type = Counter32
_CmsSysRxV3RepChangeToExclude_Object = MibScalar
cmsSysRxV3RepChangeToExclude = _CmsSysRxV3RepChangeToExclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 46),
    _CmsSysRxV3RepChangeToExclude_Type()
)
cmsSysRxV3RepChangeToExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysRxV3RepChangeToExclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysRxV3RepChangeToExclude.setUnits("packets")
_CmsSysRxV3RepAllowNewSrc_Type = Counter32
_CmsSysRxV3RepAllowNewSrc_Object = MibScalar
cmsSysRxV3RepAllowNewSrc = _CmsSysRxV3RepAllowNewSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 47),
    _CmsSysRxV3RepAllowNewSrc_Type()
)
cmsSysRxV3RepAllowNewSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysRxV3RepAllowNewSrc.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysRxV3RepAllowNewSrc.setUnits("packets")
_CmsSysRxV3RepBlockOldSrc_Type = Counter32
_CmsSysRxV3RepBlockOldSrc_Object = MibScalar
cmsSysRxV3RepBlockOldSrc = _CmsSysRxV3RepBlockOldSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 4, 48),
    _CmsSysRxV3RepBlockOldSrc_Type()
)
cmsSysRxV3RepBlockOldSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsSysRxV3RepBlockOldSrc.setStatus("current")
if mibBuilder.loadTexts:
    cmsSysRxV3RepBlockOldSrc.setUnits("packets")
_CmsPortStats_ObjectIdentity = ObjectIdentity
cmsPortStats = _CmsPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5)
)
_CmsStatsPortTrfTable_Object = MibTable
cmsStatsPortTrfTable = _CmsStatsPortTrfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cmsStatsPortTrfTable.setStatus("current")
_CmsStatsPortTrfEntry_Object = MibTableRow
cmsStatsPortTrfEntry = _CmsStatsPortTrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1)
)
cmsStatsPortTrfEntry.setIndexNames(
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortType"),
    (0, "CISCO-MLD-SNOOPING-MIB", "cmsPortId"),
)
if mibBuilder.loadTexts:
    cmsStatsPortTrfEntry.setStatus("current")
_CmsStsPortTrfGeneralQueriesReceived_Type = Counter32
_CmsStsPortTrfGeneralQueriesReceived_Object = MibTableColumn
cmsStsPortTrfGeneralQueriesReceived = _CmsStsPortTrfGeneralQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 1),
    _CmsStsPortTrfGeneralQueriesReceived_Type()
)
cmsStsPortTrfGeneralQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGeneralQueriesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGeneralQueriesReceived.setUnits("packets")
_CmsStsPortTrfGeneralQueriesReinjected_Type = Counter32
_CmsStsPortTrfGeneralQueriesReinjected_Object = MibTableColumn
cmsStsPortTrfGeneralQueriesReinjected = _CmsStsPortTrfGeneralQueriesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 2),
    _CmsStsPortTrfGeneralQueriesReinjected_Type()
)
cmsStsPortTrfGeneralQueriesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGeneralQueriesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGeneralQueriesReinjected.setUnits("packets")
_CmsStsPortTrfGeneralQueriesGenerated_Type = Counter32
_CmsStsPortTrfGeneralQueriesGenerated_Object = MibTableColumn
cmsStsPortTrfGeneralQueriesGenerated = _CmsStsPortTrfGeneralQueriesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 3),
    _CmsStsPortTrfGeneralQueriesGenerated_Type()
)
cmsStsPortTrfGeneralQueriesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGeneralQueriesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGeneralQueriesGenerated.setUnits("packets")
_CmsStsPortTrfGrpSpecificQueriesReceived_Type = Counter32
_CmsStsPortTrfGrpSpecificQueriesReceived_Object = MibTableColumn
cmsStsPortTrfGrpSpecificQueriesReceived = _CmsStsPortTrfGrpSpecificQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 4),
    _CmsStsPortTrfGrpSpecificQueriesReceived_Type()
)
cmsStsPortTrfGrpSpecificQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGrpSpecificQueriesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGrpSpecificQueriesReceived.setUnits("packets")
_CmsStsPortTrfGrpSpecificQueriesReinjected_Type = Counter32
_CmsStsPortTrfGrpSpecificQueriesReinjected_Object = MibTableColumn
cmsStsPortTrfGrpSpecificQueriesReinjected = _CmsStsPortTrfGrpSpecificQueriesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 5),
    _CmsStsPortTrfGrpSpecificQueriesReinjected_Type()
)
cmsStsPortTrfGrpSpecificQueriesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGrpSpecificQueriesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGrpSpecificQueriesReinjected.setUnits("packets")
_CmsStsPortTrfGrpSpecificQueriesGenerated_Type = Counter32
_CmsStsPortTrfGrpSpecificQueriesGenerated_Object = MibTableColumn
cmsStsPortTrfGrpSpecificQueriesGenerated = _CmsStsPortTrfGrpSpecificQueriesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 6),
    _CmsStsPortTrfGrpSpecificQueriesGenerated_Type()
)
cmsStsPortTrfGrpSpecificQueriesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGrpSpecificQueriesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGrpSpecificQueriesGenerated.setUnits("packets")
_CmsStsPortTrfGSSpecificQueriesReceived_Type = Counter32
_CmsStsPortTrfGSSpecificQueriesReceived_Object = MibTableColumn
cmsStsPortTrfGSSpecificQueriesReceived = _CmsStsPortTrfGSSpecificQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 7),
    _CmsStsPortTrfGSSpecificQueriesReceived_Type()
)
cmsStsPortTrfGSSpecificQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGSSpecificQueriesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGSSpecificQueriesReceived.setUnits("packets")
_CmsStsPortTrfGSSpecificQueriesReinjected_Type = Counter32
_CmsStsPortTrfGSSpecificQueriesReinjected_Object = MibTableColumn
cmsStsPortTrfGSSpecificQueriesReinjected = _CmsStsPortTrfGSSpecificQueriesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 8),
    _CmsStsPortTrfGSSpecificQueriesReinjected_Type()
)
cmsStsPortTrfGSSpecificQueriesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGSSpecificQueriesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGSSpecificQueriesReinjected.setUnits("packets")
_CmsStsPortTrfGSSpecificQueriesGenerated_Type = Counter32
_CmsStsPortTrfGSSpecificQueriesGenerated_Object = MibTableColumn
cmsStsPortTrfGSSpecificQueriesGenerated = _CmsStsPortTrfGSSpecificQueriesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 9),
    _CmsStsPortTrfGSSpecificQueriesGenerated_Type()
)
cmsStsPortTrfGSSpecificQueriesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGSSpecificQueriesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGSSpecificQueriesGenerated.setUnits("packets")
_CmsStsPortTrfV2ReportReceived_Type = Counter32
_CmsStsPortTrfV2ReportReceived_Object = MibTableColumn
cmsStsPortTrfV2ReportReceived = _CmsStsPortTrfV2ReportReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 10),
    _CmsStsPortTrfV2ReportReceived_Type()
)
cmsStsPortTrfV2ReportReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfV2ReportReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfV2ReportReceived.setUnits("packets")
_CmsStsPortTrfV2ReportReinjected_Type = Counter32
_CmsStsPortTrfV2ReportReinjected_Object = MibTableColumn
cmsStsPortTrfV2ReportReinjected = _CmsStsPortTrfV2ReportReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 11),
    _CmsStsPortTrfV2ReportReinjected_Type()
)
cmsStsPortTrfV2ReportReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfV2ReportReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfV2ReportReinjected.setUnits("packets")
_CmsStsPortTrfV2ReportGenerated_Type = Counter32
_CmsStsPortTrfV2ReportGenerated_Object = MibTableColumn
cmsStsPortTrfV2ReportGenerated = _CmsStsPortTrfV2ReportGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 12),
    _CmsStsPortTrfV2ReportGenerated_Type()
)
cmsStsPortTrfV2ReportGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfV2ReportGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfV2ReportGenerated.setUnits("packets")
_CmsStsPortTrfV3ReportReceived_Type = Counter32
_CmsStsPortTrfV3ReportReceived_Object = MibTableColumn
cmsStsPortTrfV3ReportReceived = _CmsStsPortTrfV3ReportReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 13),
    _CmsStsPortTrfV3ReportReceived_Type()
)
cmsStsPortTrfV3ReportReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfV3ReportReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfV3ReportReceived.setUnits("packets")
_CmsStsPortTrfV3ReportReinjected_Type = Counter32
_CmsStsPortTrfV3ReportReinjected_Object = MibTableColumn
cmsStsPortTrfV3ReportReinjected = _CmsStsPortTrfV3ReportReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 14),
    _CmsStsPortTrfV3ReportReinjected_Type()
)
cmsStsPortTrfV3ReportReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfV3ReportReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfV3ReportReinjected.setUnits("packets")
_CmsStsPortTrfV3ReportGenerated_Type = Counter32
_CmsStsPortTrfV3ReportGenerated_Object = MibTableColumn
cmsStsPortTrfV3ReportGenerated = _CmsStsPortTrfV3ReportGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 15),
    _CmsStsPortTrfV3ReportGenerated_Type()
)
cmsStsPortTrfV3ReportGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfV3ReportGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfV3ReportGenerated.setUnits("packets")
_CmsStsPortTrfGlobalLeavesReceived_Type = Counter32
_CmsStsPortTrfGlobalLeavesReceived_Object = MibTableColumn
cmsStsPortTrfGlobalLeavesReceived = _CmsStsPortTrfGlobalLeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 16),
    _CmsStsPortTrfGlobalLeavesReceived_Type()
)
cmsStsPortTrfGlobalLeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGlobalLeavesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGlobalLeavesReceived.setUnits("packets")
_CmsStsPortTrfGlobalLeavesReinjected_Type = Counter32
_CmsStsPortTrfGlobalLeavesReinjected_Object = MibTableColumn
cmsStsPortTrfGlobalLeavesReinjected = _CmsStsPortTrfGlobalLeavesReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 17),
    _CmsStsPortTrfGlobalLeavesReinjected_Type()
)
cmsStsPortTrfGlobalLeavesReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGlobalLeavesReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGlobalLeavesReinjected.setUnits("packets")
_CmsStsPortTrfGlobalLeavesGenerated_Type = Counter32
_CmsStsPortTrfGlobalLeavesGenerated_Object = MibTableColumn
cmsStsPortTrfGlobalLeavesGenerated = _CmsStsPortTrfGlobalLeavesGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 18),
    _CmsStsPortTrfGlobalLeavesGenerated_Type()
)
cmsStsPortTrfGlobalLeavesGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfGlobalLeavesGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfGlobalLeavesGenerated.setUnits("packets")
_CmsStsPortTrfPIMHellosReceived_Type = Counter32
_CmsStsPortTrfPIMHellosReceived_Object = MibTableColumn
cmsStsPortTrfPIMHellosReceived = _CmsStsPortTrfPIMHellosReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 19),
    _CmsStsPortTrfPIMHellosReceived_Type()
)
cmsStsPortTrfPIMHellosReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfPIMHellosReceived.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfPIMHellosReceived.setUnits("packets")
_CmsStsPortTrfPIMHellosReinjected_Type = Counter32
_CmsStsPortTrfPIMHellosReinjected_Object = MibTableColumn
cmsStsPortTrfPIMHellosReinjected = _CmsStsPortTrfPIMHellosReinjected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 20),
    _CmsStsPortTrfPIMHellosReinjected_Type()
)
cmsStsPortTrfPIMHellosReinjected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfPIMHellosReinjected.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfPIMHellosReinjected.setUnits("packets")
_CmsStsPortTrfPIMHellosGenerated_Type = Counter32
_CmsStsPortTrfPIMHellosGenerated_Object = MibTableColumn
cmsStsPortTrfPIMHellosGenerated = _CmsStsPortTrfPIMHellosGenerated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 21),
    _CmsStsPortTrfPIMHellosGenerated_Type()
)
cmsStsPortTrfPIMHellosGenerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfPIMHellosGenerated.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfPIMHellosGenerated.setUnits("packets")
_CmsStsPortTrfRxPcktsFlooded_Type = Counter32
_CmsStsPortTrfRxPcktsFlooded_Object = MibTableColumn
cmsStsPortTrfRxPcktsFlooded = _CmsStsPortTrfRxPcktsFlooded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 22),
    _CmsStsPortTrfRxPcktsFlooded_Type()
)
cmsStsPortTrfRxPcktsFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsFlooded.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsFlooded.setUnits("packets")
_CmsStsPortTrfRxPcktsFwdToMembers_Type = Counter32
_CmsStsPortTrfRxPcktsFwdToMembers_Object = MibTableColumn
cmsStsPortTrfRxPcktsFwdToMembers = _CmsStsPortTrfRxPcktsFwdToMembers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 23),
    _CmsStsPortTrfRxPcktsFwdToMembers_Type()
)
cmsStsPortTrfRxPcktsFwdToMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsFwdToMembers.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsFwdToMembers.setUnits("packets")
_CmsStsPortTrfRxPcktsFwdToMrouters_Type = Counter32
_CmsStsPortTrfRxPcktsFwdToMrouters_Object = MibTableColumn
cmsStsPortTrfRxPcktsFwdToMrouters = _CmsStsPortTrfRxPcktsFwdToMrouters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 24),
    _CmsStsPortTrfRxPcktsFwdToMrouters_Type()
)
cmsStsPortTrfRxPcktsFwdToMrouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsFwdToMrouters.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsFwdToMrouters.setUnits("packets")
_CmsStsPortTrfRxPcktsConsumed_Type = Counter32
_CmsStsPortTrfRxPcktsConsumed_Object = MibTableColumn
cmsStsPortTrfRxPcktsConsumed = _CmsStsPortTrfRxPcktsConsumed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 25),
    _CmsStsPortTrfRxPcktsConsumed_Type()
)
cmsStsPortTrfRxPcktsConsumed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsConsumed.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxPcktsConsumed.setUnits("packets")
_CmsStsPortTrfRxErrors_Type = Counter32
_CmsStsPortTrfRxErrors_Object = MibTableColumn
cmsStsPortTrfRxErrors = _CmsStsPortTrfRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 26),
    _CmsStsPortTrfRxErrors_Type()
)
cmsStsPortTrfRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxErrors.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxErrors.setUnits("packets")
_CmsStsPortTrfRxOther_Type = Counter32
_CmsStsPortTrfRxOther_Object = MibTableColumn
cmsStsPortTrfRxOther = _CmsStsPortTrfRxOther_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 27),
    _CmsStsPortTrfRxOther_Type()
)
cmsStsPortTrfRxOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxOther.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfRxOther.setUnits("packets")
_CmsStsPortTrfTxErrors_Type = Counter32
_CmsStsPortTrfTxErrors_Object = MibTableColumn
cmsStsPortTrfTxErrors = _CmsStsPortTrfTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 28),
    _CmsStsPortTrfTxErrors_Type()
)
cmsStsPortTrfTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortTrfTxErrors.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortTrfTxErrors.setUnits("packets")
_CmsStsPortRxV3RepIsInclude_Type = Counter32
_CmsStsPortRxV3RepIsInclude_Object = MibTableColumn
cmsStsPortRxV3RepIsInclude = _CmsStsPortRxV3RepIsInclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 29),
    _CmsStsPortRxV3RepIsInclude_Type()
)
cmsStsPortRxV3RepIsInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepIsInclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepIsInclude.setUnits("packets")
_CmsStsPortRxV3RepChangeToInclude_Type = Counter32
_CmsStsPortRxV3RepChangeToInclude_Object = MibTableColumn
cmsStsPortRxV3RepChangeToInclude = _CmsStsPortRxV3RepChangeToInclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 30),
    _CmsStsPortRxV3RepChangeToInclude_Type()
)
cmsStsPortRxV3RepChangeToInclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepChangeToInclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepChangeToInclude.setUnits("packets")
_CmsStsPortRxV3RepIsExclude_Type = Counter32
_CmsStsPortRxV3RepIsExclude_Object = MibTableColumn
cmsStsPortRxV3RepIsExclude = _CmsStsPortRxV3RepIsExclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 31),
    _CmsStsPortRxV3RepIsExclude_Type()
)
cmsStsPortRxV3RepIsExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepIsExclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepIsExclude.setUnits("packets")
_CmsStsPortRxV3RepChangeToExclude_Type = Counter32
_CmsStsPortRxV3RepChangeToExclude_Object = MibTableColumn
cmsStsPortRxV3RepChangeToExclude = _CmsStsPortRxV3RepChangeToExclude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 32),
    _CmsStsPortRxV3RepChangeToExclude_Type()
)
cmsStsPortRxV3RepChangeToExclude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepChangeToExclude.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepChangeToExclude.setUnits("packets")
_CmsStsPortRxV3RepAllowNewSrc_Type = Counter32
_CmsStsPortRxV3RepAllowNewSrc_Object = MibTableColumn
cmsStsPortRxV3RepAllowNewSrc = _CmsStsPortRxV3RepAllowNewSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 33),
    _CmsStsPortRxV3RepAllowNewSrc_Type()
)
cmsStsPortRxV3RepAllowNewSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepAllowNewSrc.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepAllowNewSrc.setUnits("packets")
_CmsStsPortRxV3RepBlockOldSrc_Type = Counter32
_CmsStsPortRxV3RepBlockOldSrc_Object = MibTableColumn
cmsStsPortRxV3RepBlockOldSrc = _CmsStsPortRxV3RepBlockOldSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 34),
    _CmsStsPortRxV3RepBlockOldSrc_Type()
)
cmsStsPortRxV3RepBlockOldSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepBlockOldSrc.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortRxV3RepBlockOldSrc.setUnits("packets")
_CmsStsPortGrps_Type = Counter32
_CmsStsPortGrps_Object = MibTableColumn
cmsStsPortGrps = _CmsStsPortGrps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 35),
    _CmsStsPortGrps_Type()
)
cmsStsPortGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortGrps.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortGrps.setUnits("groups")
_CmsStsPortSGs_Type = Counter32
_CmsStsPortSGs_Object = MibTableColumn
cmsStsPortSGs = _CmsStsPortSGs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 1, 5, 1, 1, 36),
    _CmsStsPortSGs_Type()
)
cmsStsPortSGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmsStsPortSGs.setStatus("current")
if mibBuilder.loadTexts:
    cmsStsPortSGs.setUnits("sources")
_CiscoMldSnoopingMIBConform_ObjectIdentity = ObjectIdentity
ciscoMldSnoopingMIBConform = _CiscoMldSnoopingMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2)
)
_CiscoMldSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoMldSnoopingMIBCompliances = _CiscoMldSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 1)
)
_CiscoMldSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
ciscoMldSnoopingMIBGroups = _CiscoMldSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 2)
)

# Managed Objects groups

ciscoMldSnoopingMIBConfigMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 2, 1)
)
ciscoMldSnoopingMIBConfigMainObjectGroup.setObjects(
      *(("CISCO-MLD-SNOOPING-MIB", "cmsProfileInternalQuerier"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileSuppressReport"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileRouterGuard"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileStaticMRouter"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileImmediateLeave"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsConfigSystemProfileName"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsConfigPortProfileName"))
)
if mibBuilder.loadTexts:
    ciscoMldSnoopingMIBConfigMainObjectGroup.setStatus("current")

ciscoMldSnoopingMIBConfigDetailedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 2, 2)
)
ciscoMldSnoopingMIBConfigDetailedObjectGroup.setObjects(
      *(("CISCO-MLD-SNOOPING-MIB", "cmsProfileSnoopMinVersion"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileStatus"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileStorageType"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIPAddress"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileRobustnessVariable"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileLastMemberQueryCount"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileLastMemberQueryInterval"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileUnsolicitedReportTimer"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileFloodQueryCount"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileQuerySolicit"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileTTLCheck"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileRouterAlertCheck"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIntQuerierMaxRespTime"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIntQuerierQueryInterval"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIntQuerierTCNQueryCount"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIntQuerierTCNQueryInterval"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIntQuerierExpiry"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIntQuerierVersion"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsProfileIPAddrType"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsConfigPortStatus"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsConfigPortStorageType"))
)
if mibBuilder.loadTexts:
    ciscoMldSnoopingMIBConfigDetailedObjectGroup.setStatus("current")

ciscoMldSnoopingMIBInfoMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 2, 3)
)
ciscoMldSnoopingMIBInfoMainObjectGroup.setObjects(
      *(("CISCO-MLD-SNOOPING-MIB", "cmsMcastInfoGroupFilter"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsMcastInfoExpiry"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsMcastInfoFlag"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierPortId"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierVersion"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierQueryInterval"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierRobustness"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierMaxRespTime"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierTimeSinceLastGQuery"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsMRouterType"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierIPAddr"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierIPAddrType"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsQuerierPortType"))
)
if mibBuilder.loadTexts:
    ciscoMldSnoopingMIBInfoMainObjectGroup.setStatus("current")

ciscoMldSnoopingMIBStatsMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 2, 4)
)
ciscoMldSnoopingMIBStatsMainObjectGroup.setObjects(
      *(("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGeneralQueriesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGeneralQueriesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGeneralQueriesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGlobalLeavesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGlobalLeavesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGlobalLeavesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfPIMHellosReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfPIMHellosReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfPIMHellosGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfRxErrors"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfTxErrors"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfV2ReportReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfV2ReportReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfV2ReportGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfV3ReportReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfV3ReportReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfV3ReportGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfRxErrors"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfTxErrors"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysRxV3RepIsInclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysRxV3RepChangeToInclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysRxV3RepIsExclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysRxV3RepChangeToExclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysRxV3RepAllowNewSrc"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysRxV3RepBlockOldSrc"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortRxV3RepIsInclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortRxV3RepChangeToInclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortRxV3RepIsExclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortRxV3RepChangeToExclude"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortRxV3RepAllowNewSrc"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortRxV3RepBlockOldSrc"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortGrps"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortSGs"))
)
if mibBuilder.loadTexts:
    ciscoMldSnoopingMIBStatsMainObjectGroup.setStatus("current")

ciscoMldSnoopingMIBStatsDetailedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 2, 5)
)
ciscoMldSnoopingMIBStatsDetailedObjectGroup.setObjects(
      *(("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGrpSpecificQueriesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGrpSpecificQueriesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGrpSpecificQueriesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGSSpecificQueriesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGSSpecificQueriesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfGSSpecificQueriesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfV2ReportReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfV2ReportReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfV2ReportGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfV3ReportReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfV3ReportReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfV3ReportGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfRxPcktsFlooded"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfRxPcktsFwdToMembers"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfRxPcktsFwdToMrouters"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfRxPcktsConsumed"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysTrfRxOther"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGeneralQueriesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGeneralQueriesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGeneralQueriesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGrpSpecificQueriesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGrpSpecificQueriesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGrpSpecificQueriesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGSSpecificQueriesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGSSpecificQueriesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGSSpecificQueriesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGlobalLeavesReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGlobalLeavesReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfGlobalLeavesGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfPIMHellosReceived"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfPIMHellosReinjected"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfPIMHellosGenerated"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfRxPcktsFlooded"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfRxPcktsFwdToMembers"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfRxPcktsFwdToMrouters"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfRxPcktsConsumed"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsStsPortTrfRxOther"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGeneralQueries"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGeneralQueriesWhenDisabled"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGeneralQueriesAsQuerier"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGeneralQueriesAsNonQuerier"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGeneralQueriesAsWinner"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGeneralQueriesAsLoser"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGlobalLeaves"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGlobalLeavesWhenDisabled"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGlobalLeavsAsNonQuerier"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxGlobalLeavesIgnored"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxPimEnabledNotifications"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxPimDisabledNotifications"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierRxLocalQuerySolicitations"),
        ("CISCO-MLD-SNOOPING-MIB", "cmsSysIntQuerierTxGeneralQueries"))
)
if mibBuilder.loadTexts:
    ciscoMldSnoopingMIBStatsDetailedObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoMldSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 721, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoMldSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MLD-SNOOPING-MIB",
    **{"CiscoMldPortType": CiscoMldPortType,
       "CiscoMldPortIdentifier": CiscoMldPortIdentifier,
       "CiscoMldPortInterface": CiscoMldPortInterface,
       "CiscoMldPortPseudowire": CiscoMldPortPseudowire,
       "CiscoMldSnoopingVersion": CiscoMldSnoopingVersion,
       "ciscoMldSnoopingMIB": ciscoMldSnoopingMIB,
       "ciscoMldSnoopingMIBNotifs": ciscoMldSnoopingMIBNotifs,
       "ciscoMldSnoopingMIBObjects": ciscoMldSnoopingMIBObjects,
       "cmsConfiguration": cmsConfiguration,
       "cmsProfileTable": cmsProfileTable,
       "cmsProfileEntry": cmsProfileEntry,
       "cmsProfileName": cmsProfileName,
       "cmsProfileStatus": cmsProfileStatus,
       "cmsProfileStorageType": cmsProfileStorageType,
       "cmsProfileSnoopMinVersion": cmsProfileSnoopMinVersion,
       "cmsProfileIPAddrType": cmsProfileIPAddrType,
       "cmsProfileIPAddress": cmsProfileIPAddress,
       "cmsProfileRobustnessVariable": cmsProfileRobustnessVariable,
       "cmsProfileInternalQuerier": cmsProfileInternalQuerier,
       "cmsProfileLastMemberQueryCount": cmsProfileLastMemberQueryCount,
       "cmsProfileLastMemberQueryInterval": cmsProfileLastMemberQueryInterval,
       "cmsProfileSuppressReport": cmsProfileSuppressReport,
       "cmsProfileUnsolicitedReportTimer": cmsProfileUnsolicitedReportTimer,
       "cmsProfileFloodQueryCount": cmsProfileFloodQueryCount,
       "cmsProfileQuerySolicit": cmsProfileQuerySolicit,
       "cmsProfileTTLCheck": cmsProfileTTLCheck,
       "cmsProfileRouterAlertCheck": cmsProfileRouterAlertCheck,
       "cmsProfileIntQuerierMaxRespTime": cmsProfileIntQuerierMaxRespTime,
       "cmsProfileIntQuerierQueryInterval": cmsProfileIntQuerierQueryInterval,
       "cmsProfileIntQuerierTCNQueryCount": cmsProfileIntQuerierTCNQueryCount,
       "cmsProfileIntQuerierTCNQueryInterval": cmsProfileIntQuerierTCNQueryInterval,
       "cmsProfileIntQuerierExpiry": cmsProfileIntQuerierExpiry,
       "cmsProfileIntQuerierVersion": cmsProfileIntQuerierVersion,
       "cmsProfileRouterGuard": cmsProfileRouterGuard,
       "cmsProfileStaticMRouter": cmsProfileStaticMRouter,
       "cmsProfileImmediateLeave": cmsProfileImmediateLeave,
       "cmsConfigPortTable": cmsConfigPortTable,
       "cmsConfigPortEntry": cmsConfigPortEntry,
       "cmsPortType": cmsPortType,
       "cmsPortId": cmsPortId,
       "cmsConfigPortStatus": cmsConfigPortStatus,
       "cmsConfigPortStorageType": cmsConfigPortStorageType,
       "cmsConfigPortProfileName": cmsConfigPortProfileName,
       "cmsConfigSystemProfileName": cmsConfigSystemProfileName,
       "cmsSystemInfo": cmsSystemInfo,
       "cmsOperInfo": cmsOperInfo,
       "cmsQuerierIPAddrType": cmsQuerierIPAddrType,
       "cmsQuerierIPAddr": cmsQuerierIPAddr,
       "cmsQuerierPortType": cmsQuerierPortType,
       "cmsQuerierPortId": cmsQuerierPortId,
       "cmsQuerierVersion": cmsQuerierVersion,
       "cmsQuerierQueryInterval": cmsQuerierQueryInterval,
       "cmsQuerierRobustness": cmsQuerierRobustness,
       "cmsQuerierMaxRespTime": cmsQuerierMaxRespTime,
       "cmsQuerierTimeSinceLastGQuery": cmsQuerierTimeSinceLastGQuery,
       "cmsMcastInfoTable": cmsMcastInfoTable,
       "cmsMcastInfoEntry": cmsMcastInfoEntry,
       "cmsMcastInfoGroupAddrType": cmsMcastInfoGroupAddrType,
       "cmsMcastInfoGroupAddr": cmsMcastInfoGroupAddr,
       "cmsMcastInfoSourceAddr": cmsMcastInfoSourceAddr,
       "cmsMcastInfoGroupFilter": cmsMcastInfoGroupFilter,
       "cmsMcastInfoExpiry": cmsMcastInfoExpiry,
       "cmsMcastInfoFlag": cmsMcastInfoFlag,
       "cmsMRouterPortInfoTable": cmsMRouterPortInfoTable,
       "cmsMRouterPortInfoEntry": cmsMRouterPortInfoEntry,
       "cmsMRouterType": cmsMRouterType,
       "cmsSystemStats": cmsSystemStats,
       "cmsSysIntQuerierRxGeneralQueries": cmsSysIntQuerierRxGeneralQueries,
       "cmsSysIntQuerierRxGeneralQueriesWhenDisabled": cmsSysIntQuerierRxGeneralQueriesWhenDisabled,
       "cmsSysIntQuerierRxGeneralQueriesAsQuerier": cmsSysIntQuerierRxGeneralQueriesAsQuerier,
       "cmsSysIntQuerierRxGeneralQueriesAsNonQuerier": cmsSysIntQuerierRxGeneralQueriesAsNonQuerier,
       "cmsSysIntQuerierRxGeneralQueriesAsWinner": cmsSysIntQuerierRxGeneralQueriesAsWinner,
       "cmsSysIntQuerierRxGeneralQueriesAsLoser": cmsSysIntQuerierRxGeneralQueriesAsLoser,
       "cmsSysIntQuerierRxGlobalLeaves": cmsSysIntQuerierRxGlobalLeaves,
       "cmsSysIntQuerierRxGlobalLeavesWhenDisabled": cmsSysIntQuerierRxGlobalLeavesWhenDisabled,
       "cmsSysIntQuerierRxGlobalLeavsAsNonQuerier": cmsSysIntQuerierRxGlobalLeavsAsNonQuerier,
       "cmsSysIntQuerierRxGlobalLeavesIgnored": cmsSysIntQuerierRxGlobalLeavesIgnored,
       "cmsSysIntQuerierRxPimEnabledNotifications": cmsSysIntQuerierRxPimEnabledNotifications,
       "cmsSysIntQuerierRxPimDisabledNotifications": cmsSysIntQuerierRxPimDisabledNotifications,
       "cmsSysIntQuerierRxLocalQuerySolicitations": cmsSysIntQuerierRxLocalQuerySolicitations,
       "cmsSysIntQuerierTxGeneralQueries": cmsSysIntQuerierTxGeneralQueries,
       "cmsSysTrfGeneralQueriesReceived": cmsSysTrfGeneralQueriesReceived,
       "cmsSysTrfGeneralQueriesReinjected": cmsSysTrfGeneralQueriesReinjected,
       "cmsSysTrfGeneralQueriesGenerated": cmsSysTrfGeneralQueriesGenerated,
       "cmsSysTrfGrpSpecificQueriesReceived": cmsSysTrfGrpSpecificQueriesReceived,
       "cmsSysTrfGrpSpecificQueriesReinjected": cmsSysTrfGrpSpecificQueriesReinjected,
       "cmsSysTrfGrpSpecificQueriesGenerated": cmsSysTrfGrpSpecificQueriesGenerated,
       "cmsSysTrfGSSpecificQueriesReceived": cmsSysTrfGSSpecificQueriesReceived,
       "cmsSysTrfGSSpecificQueriesReinjected": cmsSysTrfGSSpecificQueriesReinjected,
       "cmsSysTrfGSSpecificQueriesGenerated": cmsSysTrfGSSpecificQueriesGenerated,
       "cmsSysTrfV2ReportReceived": cmsSysTrfV2ReportReceived,
       "cmsSysTrfV2ReportReinjected": cmsSysTrfV2ReportReinjected,
       "cmsSysTrfV2ReportGenerated": cmsSysTrfV2ReportGenerated,
       "cmsSysTrfV3ReportReceived": cmsSysTrfV3ReportReceived,
       "cmsSysTrfV3ReportReinjected": cmsSysTrfV3ReportReinjected,
       "cmsSysTrfV3ReportGenerated": cmsSysTrfV3ReportGenerated,
       "cmsSysTrfGlobalLeavesReceived": cmsSysTrfGlobalLeavesReceived,
       "cmsSysTrfGlobalLeavesReinjected": cmsSysTrfGlobalLeavesReinjected,
       "cmsSysTrfGlobalLeavesGenerated": cmsSysTrfGlobalLeavesGenerated,
       "cmsSysTrfPIMHellosReceived": cmsSysTrfPIMHellosReceived,
       "cmsSysTrfPIMHellosReinjected": cmsSysTrfPIMHellosReinjected,
       "cmsSysTrfPIMHellosGenerated": cmsSysTrfPIMHellosGenerated,
       "cmsSysTrfRxPcktsFlooded": cmsSysTrfRxPcktsFlooded,
       "cmsSysTrfRxPcktsFwdToMembers": cmsSysTrfRxPcktsFwdToMembers,
       "cmsSysTrfRxPcktsFwdToMrouters": cmsSysTrfRxPcktsFwdToMrouters,
       "cmsSysTrfRxPcktsConsumed": cmsSysTrfRxPcktsConsumed,
       "cmsSysTrfRxErrors": cmsSysTrfRxErrors,
       "cmsSysTrfRxOther": cmsSysTrfRxOther,
       "cmsSysTrfTxErrors": cmsSysTrfTxErrors,
       "cmsSysRxV3RepIsInclude": cmsSysRxV3RepIsInclude,
       "cmsSysRxV3RepChangeToInclude": cmsSysRxV3RepChangeToInclude,
       "cmsSysRxV3RepIsExclude": cmsSysRxV3RepIsExclude,
       "cmsSysRxV3RepChangeToExclude": cmsSysRxV3RepChangeToExclude,
       "cmsSysRxV3RepAllowNewSrc": cmsSysRxV3RepAllowNewSrc,
       "cmsSysRxV3RepBlockOldSrc": cmsSysRxV3RepBlockOldSrc,
       "cmsPortStats": cmsPortStats,
       "cmsStatsPortTrfTable": cmsStatsPortTrfTable,
       "cmsStatsPortTrfEntry": cmsStatsPortTrfEntry,
       "cmsStsPortTrfGeneralQueriesReceived": cmsStsPortTrfGeneralQueriesReceived,
       "cmsStsPortTrfGeneralQueriesReinjected": cmsStsPortTrfGeneralQueriesReinjected,
       "cmsStsPortTrfGeneralQueriesGenerated": cmsStsPortTrfGeneralQueriesGenerated,
       "cmsStsPortTrfGrpSpecificQueriesReceived": cmsStsPortTrfGrpSpecificQueriesReceived,
       "cmsStsPortTrfGrpSpecificQueriesReinjected": cmsStsPortTrfGrpSpecificQueriesReinjected,
       "cmsStsPortTrfGrpSpecificQueriesGenerated": cmsStsPortTrfGrpSpecificQueriesGenerated,
       "cmsStsPortTrfGSSpecificQueriesReceived": cmsStsPortTrfGSSpecificQueriesReceived,
       "cmsStsPortTrfGSSpecificQueriesReinjected": cmsStsPortTrfGSSpecificQueriesReinjected,
       "cmsStsPortTrfGSSpecificQueriesGenerated": cmsStsPortTrfGSSpecificQueriesGenerated,
       "cmsStsPortTrfV2ReportReceived": cmsStsPortTrfV2ReportReceived,
       "cmsStsPortTrfV2ReportReinjected": cmsStsPortTrfV2ReportReinjected,
       "cmsStsPortTrfV2ReportGenerated": cmsStsPortTrfV2ReportGenerated,
       "cmsStsPortTrfV3ReportReceived": cmsStsPortTrfV3ReportReceived,
       "cmsStsPortTrfV3ReportReinjected": cmsStsPortTrfV3ReportReinjected,
       "cmsStsPortTrfV3ReportGenerated": cmsStsPortTrfV3ReportGenerated,
       "cmsStsPortTrfGlobalLeavesReceived": cmsStsPortTrfGlobalLeavesReceived,
       "cmsStsPortTrfGlobalLeavesReinjected": cmsStsPortTrfGlobalLeavesReinjected,
       "cmsStsPortTrfGlobalLeavesGenerated": cmsStsPortTrfGlobalLeavesGenerated,
       "cmsStsPortTrfPIMHellosReceived": cmsStsPortTrfPIMHellosReceived,
       "cmsStsPortTrfPIMHellosReinjected": cmsStsPortTrfPIMHellosReinjected,
       "cmsStsPortTrfPIMHellosGenerated": cmsStsPortTrfPIMHellosGenerated,
       "cmsStsPortTrfRxPcktsFlooded": cmsStsPortTrfRxPcktsFlooded,
       "cmsStsPortTrfRxPcktsFwdToMembers": cmsStsPortTrfRxPcktsFwdToMembers,
       "cmsStsPortTrfRxPcktsFwdToMrouters": cmsStsPortTrfRxPcktsFwdToMrouters,
       "cmsStsPortTrfRxPcktsConsumed": cmsStsPortTrfRxPcktsConsumed,
       "cmsStsPortTrfRxErrors": cmsStsPortTrfRxErrors,
       "cmsStsPortTrfRxOther": cmsStsPortTrfRxOther,
       "cmsStsPortTrfTxErrors": cmsStsPortTrfTxErrors,
       "cmsStsPortRxV3RepIsInclude": cmsStsPortRxV3RepIsInclude,
       "cmsStsPortRxV3RepChangeToInclude": cmsStsPortRxV3RepChangeToInclude,
       "cmsStsPortRxV3RepIsExclude": cmsStsPortRxV3RepIsExclude,
       "cmsStsPortRxV3RepChangeToExclude": cmsStsPortRxV3RepChangeToExclude,
       "cmsStsPortRxV3RepAllowNewSrc": cmsStsPortRxV3RepAllowNewSrc,
       "cmsStsPortRxV3RepBlockOldSrc": cmsStsPortRxV3RepBlockOldSrc,
       "cmsStsPortGrps": cmsStsPortGrps,
       "cmsStsPortSGs": cmsStsPortSGs,
       "ciscoMldSnoopingMIBConform": ciscoMldSnoopingMIBConform,
       "ciscoMldSnoopingMIBCompliances": ciscoMldSnoopingMIBCompliances,
       "ciscoMldSnoopingMIBCompliance": ciscoMldSnoopingMIBCompliance,
       "ciscoMldSnoopingMIBGroups": ciscoMldSnoopingMIBGroups,
       "ciscoMldSnoopingMIBConfigMainObjectGroup": ciscoMldSnoopingMIBConfigMainObjectGroup,
       "ciscoMldSnoopingMIBConfigDetailedObjectGroup": ciscoMldSnoopingMIBConfigDetailedObjectGroup,
       "ciscoMldSnoopingMIBInfoMainObjectGroup": ciscoMldSnoopingMIBInfoMainObjectGroup,
       "ciscoMldSnoopingMIBStatsMainObjectGroup": ciscoMldSnoopingMIBStatsMainObjectGroup,
       "ciscoMldSnoopingMIBStatsDetailedObjectGroup": ciscoMldSnoopingMIBStatsDetailedObjectGroup}
)
