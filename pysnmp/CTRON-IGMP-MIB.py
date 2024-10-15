# SNMP MIB module (CTRON-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:57 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ctIGMPBranch,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctIGMPBranch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ctIGMP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1)
)
ctIGMP.setRevisions(
        ("2005-05-09 20:30",
         "2005-03-15 20:38",
         "2003-12-10 14:56")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IgmpPortModeTc(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reporter", 1),
          ("source", 2))
    )



class IgmpProtocolClassTc(Integer32, TextualConvention):
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
        *(("ignore", 3),
          ("multicastData", 1),
          ("routingProtocol", 2))
    )



class IgmpProtocolIdTc(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CtIGMPConfig_ObjectIdentity = ObjectIdentity
ctIGMPConfig = _CtIGMPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1)
)


class _CtIGMPNewDefaultState_Type(Integer32):
    """Custom type ctIGMPNewDefaultState based on Integer32"""
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


_CtIGMPNewDefaultState_Type.__name__ = "Integer32"
_CtIGMPNewDefaultState_Object = MibScalar
ctIGMPNewDefaultState = _CtIGMPNewDefaultState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 1),
    _CtIGMPNewDefaultState_Type()
)
ctIGMPNewDefaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIGMPNewDefaultState.setStatus("current")
_CtIGMPMibRev_Type = Integer32
_CtIGMPMibRev_Object = MibScalar
ctIGMPMibRev = _CtIGMPMibRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 2),
    _CtIGMPMibRev_Type()
)
ctIGMPMibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPMibRev.setStatus("current")
_CtIGMPMibRevString_Type = DisplayString
_CtIGMPMibRevString_Object = MibScalar
ctIGMPMibRevString = _CtIGMPMibRevString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 3),
    _CtIGMPMibRevString_Type()
)
ctIGMPMibRevString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPMibRevString.setStatus("current")


class _CtIGMPConfigGroupTblFullAction_Type(Integer32):
    """Custom type ctIGMPConfigGroupTblFullAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flood", 2),
          ("routers", 1))
    )


_CtIGMPConfigGroupTblFullAction_Type.__name__ = "Integer32"
_CtIGMPConfigGroupTblFullAction_Object = MibScalar
ctIGMPConfigGroupTblFullAction = _CtIGMPConfigGroupTblFullAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 1, 4),
    _CtIGMPConfigGroupTblFullAction_Type()
)
ctIGMPConfigGroupTblFullAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIGMPConfigGroupTblFullAction.setStatus("current")
_CtIGMPVlanTable_Object = MibTable
ctIGMPVlanTable = _CtIGMPVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ctIGMPVlanTable.setStatus("current")
_CtIGMPVlanEntry_Object = MibTableRow
ctIGMPVlanEntry = _CtIGMPVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1)
)
ctIGMPVlanEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPVlanId"),
)
if mibBuilder.loadTexts:
    ctIGMPVlanEntry.setStatus("current")
_CtIGMPVlanId_Type = VlanId
_CtIGMPVlanId_Object = MibTableColumn
ctIGMPVlanId = _CtIGMPVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 1),
    _CtIGMPVlanId_Type()
)
ctIGMPVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPVlanId.setStatus("current")


class _CtIGMPVlanQueryInterval_Type(Integer32):
    """Custom type ctIGMPVlanQueryInterval based on Integer32"""
    defaultValue = 125


_CtIGMPVlanQueryInterval_Object = MibTableColumn
ctIGMPVlanQueryInterval = _CtIGMPVlanQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 2),
    _CtIGMPVlanQueryInterval_Type()
)
ctIGMPVlanQueryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPVlanQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPVlanQueryInterval.setUnits("seconds")
_CtIGMPVlanStatus_Type = RowStatus
_CtIGMPVlanStatus_Object = MibTableColumn
ctIGMPVlanStatus = _CtIGMPVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 3),
    _CtIGMPVlanStatus_Type()
)
ctIGMPVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPVlanStatus.setStatus("current")


class _CtIGMPVlanVersion_Type(Integer32):
    """Custom type ctIGMPVlanVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_CtIGMPVlanVersion_Type.__name__ = "Integer32"
_CtIGMPVlanVersion_Object = MibTableColumn
ctIGMPVlanVersion = _CtIGMPVlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 4),
    _CtIGMPVlanVersion_Type()
)
ctIGMPVlanVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPVlanVersion.setStatus("current")
_CtIGMPVlanQuerier_Type = IpAddress
_CtIGMPVlanQuerier_Object = MibTableColumn
ctIGMPVlanQuerier = _CtIGMPVlanQuerier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 5),
    _CtIGMPVlanQuerier_Type()
)
ctIGMPVlanQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPVlanQuerier.setStatus("current")


class _CtIGMPVlanQueryMaxResponseTime_Type(Integer32):
    """Custom type ctIGMPVlanQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_CtIGMPVlanQueryMaxResponseTime_Type.__name__ = "Integer32"
_CtIGMPVlanQueryMaxResponseTime_Object = MibTableColumn
ctIGMPVlanQueryMaxResponseTime = _CtIGMPVlanQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 6),
    _CtIGMPVlanQueryMaxResponseTime_Type()
)
ctIGMPVlanQueryMaxResponseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPVlanQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPVlanQueryMaxResponseTime.setUnits("seconds")


class _CtIGMPVlanRobustness_Type(Integer32):
    """Custom type ctIGMPVlanRobustness based on Integer32"""
    defaultValue = 2


_CtIGMPVlanRobustness_Object = MibTableColumn
ctIGMPVlanRobustness = _CtIGMPVlanRobustness_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 7),
    _CtIGMPVlanRobustness_Type()
)
ctIGMPVlanRobustness.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPVlanRobustness.setStatus("current")


class _CtIGMPVlanLastMembQueryIntvl_Type(Integer32):
    """Custom type ctIGMPVlanLastMembQueryIntvl based on Integer32"""
    defaultValue = 10


_CtIGMPVlanLastMembQueryIntvl_Object = MibTableColumn
ctIGMPVlanLastMembQueryIntvl = _CtIGMPVlanLastMembQueryIntvl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 8),
    _CtIGMPVlanLastMembQueryIntvl_Type()
)
ctIGMPVlanLastMembQueryIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPVlanLastMembQueryIntvl.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPVlanLastMembQueryIntvl.setUnits("tenths of seconds")
_CtIGMPVlanQuerierUpTime_Type = Integer32
_CtIGMPVlanQuerierUpTime_Object = MibTableColumn
ctIGMPVlanQuerierUpTime = _CtIGMPVlanQuerierUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 9),
    _CtIGMPVlanQuerierUpTime_Type()
)
ctIGMPVlanQuerierUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPVlanQuerierUpTime.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPVlanQuerierUpTime.setUnits("seconds")
_CtIGMPVlanQuerierExpiryTime_Type = Integer32
_CtIGMPVlanQuerierExpiryTime_Object = MibTableColumn
ctIGMPVlanQuerierExpiryTime = _CtIGMPVlanQuerierExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 10),
    _CtIGMPVlanQuerierExpiryTime_Type()
)
ctIGMPVlanQuerierExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPVlanQuerierExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPVlanQuerierExpiryTime.setUnits("seconds")
_CtIGMPVlanQuerierIP_Type = IpAddress
_CtIGMPVlanQuerierIP_Object = MibTableColumn
ctIGMPVlanQuerierIP = _CtIGMPVlanQuerierIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 2, 1, 11),
    _CtIGMPVlanQuerierIP_Type()
)
ctIGMPVlanQuerierIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPVlanQuerierIP.setStatus("current")
_CtIGMPCacheTable_Object = MibTable
ctIGMPCacheTable = _CtIGMPCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3)
)
if mibBuilder.loadTexts:
    ctIGMPCacheTable.setStatus("current")
_CtIGMPCacheEntry_Object = MibTableRow
ctIGMPCacheEntry = _CtIGMPCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1)
)
ctIGMPCacheEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPCacheAddress"),
    (0, "CTRON-IGMP-MIB", "ctIGMPCacheVlanId"),
    (0, "CTRON-IGMP-MIB", "ctIGMPCacheIfIndex"),
)
if mibBuilder.loadTexts:
    ctIGMPCacheEntry.setStatus("current")
_CtIGMPCacheAddress_Type = IpAddress
_CtIGMPCacheAddress_Object = MibTableColumn
ctIGMPCacheAddress = _CtIGMPCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 1),
    _CtIGMPCacheAddress_Type()
)
ctIGMPCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPCacheAddress.setStatus("current")
_CtIGMPCacheVlanId_Type = VlanId
_CtIGMPCacheVlanId_Object = MibTableColumn
ctIGMPCacheVlanId = _CtIGMPCacheVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 2),
    _CtIGMPCacheVlanId_Type()
)
ctIGMPCacheVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPCacheVlanId.setStatus("current")
_CtIGMPCacheIfIndex_Type = InterfaceIndex
_CtIGMPCacheIfIndex_Object = MibTableColumn
ctIGMPCacheIfIndex = _CtIGMPCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 3),
    _CtIGMPCacheIfIndex_Type()
)
ctIGMPCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPCacheIfIndex.setStatus("current")
_CtIGMPCacheLastReporter_Type = IpAddress
_CtIGMPCacheLastReporter_Object = MibTableColumn
ctIGMPCacheLastReporter = _CtIGMPCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 4),
    _CtIGMPCacheLastReporter_Type()
)
ctIGMPCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPCacheLastReporter.setStatus("current")
_CtIGMPCacheUpTime_Type = TimeTicks
_CtIGMPCacheUpTime_Object = MibTableColumn
ctIGMPCacheUpTime = _CtIGMPCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 5),
    _CtIGMPCacheUpTime_Type()
)
ctIGMPCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPCacheUpTime.setStatus("current")
_CtIGMPCacheExpiryTime_Type = TimeTicks
_CtIGMPCacheExpiryTime_Object = MibTableColumn
ctIGMPCacheExpiryTime = _CtIGMPCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 6),
    _CtIGMPCacheExpiryTime_Type()
)
ctIGMPCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPCacheExpiryTime.setStatus("current")
_CtIGMPCacheVersion1HostTimer_Type = Integer32
_CtIGMPCacheVersion1HostTimer_Object = MibTableColumn
ctIGMPCacheVersion1HostTimer = _CtIGMPCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 3, 1, 7),
    _CtIGMPCacheVersion1HostTimer_Type()
)
ctIGMPCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPCacheVersion1HostTimer.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPCacheVersion1HostTimer.setUnits("seconds")
_CtIGMPPolicyTable_Object = MibTable
ctIGMPPolicyTable = _CtIGMPPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4)
)
if mibBuilder.loadTexts:
    ctIGMPPolicyTable.setStatus("deprecated")
_CtIGMPPolicyEntry_Object = MibTableRow
ctIGMPPolicyEntry = _CtIGMPPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1)
)
ctIGMPPolicyEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPPolicyAddress"),
    (0, "CTRON-IGMP-MIB", "ctIGMPPolicyVlanId"),
    (0, "CTRON-IGMP-MIB", "ctIGMPPolicyIfIndex"),
)
if mibBuilder.loadTexts:
    ctIGMPPolicyEntry.setStatus("deprecated")
_CtIGMPPolicyAddress_Type = IpAddress
_CtIGMPPolicyAddress_Object = MibTableColumn
ctIGMPPolicyAddress = _CtIGMPPolicyAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 1),
    _CtIGMPPolicyAddress_Type()
)
ctIGMPPolicyAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPPolicyAddress.setStatus("deprecated")


class _CtIGMPPolicyVlanId_Type(Integer32):
    """Custom type ctIGMPPolicyVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtIGMPPolicyVlanId_Type.__name__ = "Integer32"
_CtIGMPPolicyVlanId_Object = MibTableColumn
ctIGMPPolicyVlanId = _CtIGMPPolicyVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 2),
    _CtIGMPPolicyVlanId_Type()
)
ctIGMPPolicyVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPPolicyVlanId.setStatus("deprecated")
_CtIGMPPolicyIfIndex_Type = InterfaceIndex
_CtIGMPPolicyIfIndex_Object = MibTableColumn
ctIGMPPolicyIfIndex = _CtIGMPPolicyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 3),
    _CtIGMPPolicyIfIndex_Type()
)
ctIGMPPolicyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPPolicyIfIndex.setStatus("deprecated")
_CtIGMPPolicyStatus_Type = RowStatus
_CtIGMPPolicyStatus_Object = MibTableColumn
ctIGMPPolicyStatus = _CtIGMPPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 4),
    _CtIGMPPolicyStatus_Type()
)
ctIGMPPolicyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPPolicyStatus.setStatus("deprecated")


class _CtIGMPPolicyInclusion_Type(Integer32):
    """Custom type ctIGMPPolicyInclusion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_CtIGMPPolicyInclusion_Type.__name__ = "Integer32"
_CtIGMPPolicyInclusion_Object = MibTableColumn
ctIGMPPolicyInclusion = _CtIGMPPolicyInclusion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 4, 1, 5),
    _CtIGMPPolicyInclusion_Type()
)
ctIGMPPolicyInclusion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPPolicyInclusion.setStatus("deprecated")
_CtIGMPStaticTable_Object = MibTable
ctIGMPStaticTable = _CtIGMPStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5)
)
if mibBuilder.loadTexts:
    ctIGMPStaticTable.setStatus("deprecated")
_CtIGMPStaticEntry_Object = MibTableRow
ctIGMPStaticEntry = _CtIGMPStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1)
)
ctIGMPStaticEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupAddress"),
    (0, "CTRON-IGMP-MIB", "ctIGMPStaticVlanId"),
)
if mibBuilder.loadTexts:
    ctIGMPStaticEntry.setStatus("deprecated")
_CtIGMPStaticGroupAddress_Type = IpAddress
_CtIGMPStaticGroupAddress_Object = MibTableColumn
ctIGMPStaticGroupAddress = _CtIGMPStaticGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 1),
    _CtIGMPStaticGroupAddress_Type()
)
ctIGMPStaticGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPStaticGroupAddress.setStatus("deprecated")


class _CtIGMPStaticVlanId_Type(Integer32):
    """Custom type ctIGMPStaticVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_CtIGMPStaticVlanId_Type.__name__ = "Integer32"
_CtIGMPStaticVlanId_Object = MibTableColumn
ctIGMPStaticVlanId = _CtIGMPStaticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 2),
    _CtIGMPStaticVlanId_Type()
)
ctIGMPStaticVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPStaticVlanId.setStatus("deprecated")
_CtIGMPStaticOutPortList_Type = PortList
_CtIGMPStaticOutPortList_Object = MibTableColumn
ctIGMPStaticOutPortList = _CtIGMPStaticOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 3),
    _CtIGMPStaticOutPortList_Type()
)
ctIGMPStaticOutPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIGMPStaticOutPortList.setStatus("deprecated")
_CtIGMPStaticRowStatus_Type = RowStatus
_CtIGMPStaticRowStatus_Object = MibTableColumn
ctIGMPStaticRowStatus = _CtIGMPStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 5, 1, 4),
    _CtIGMPStaticRowStatus_Type()
)
ctIGMPStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPStaticRowStatus.setStatus("deprecated")
_CtIGMPStaticGroupTable_Object = MibTable
ctIGMPStaticGroupTable = _CtIGMPStaticGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6)
)
if mibBuilder.loadTexts:
    ctIGMPStaticGroupTable.setStatus("current")
_CtIGMPStaticGroupEntry_Object = MibTableRow
ctIGMPStaticGroupEntry = _CtIGMPStaticGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1)
)
ctIGMPStaticGroupEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupIPAddress"),
    (0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupVlanId"),
    (0, "CTRON-IGMP-MIB", "ctIGMPStaticGroupSourceIPAddress"),
)
if mibBuilder.loadTexts:
    ctIGMPStaticGroupEntry.setStatus("current")
_CtIGMPStaticGroupIPAddress_Type = IpAddress
_CtIGMPStaticGroupIPAddress_Object = MibTableColumn
ctIGMPStaticGroupIPAddress = _CtIGMPStaticGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 1),
    _CtIGMPStaticGroupIPAddress_Type()
)
ctIGMPStaticGroupIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPStaticGroupIPAddress.setStatus("current")
_CtIGMPStaticGroupVlanId_Type = VlanId
_CtIGMPStaticGroupVlanId_Object = MibTableColumn
ctIGMPStaticGroupVlanId = _CtIGMPStaticGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 2),
    _CtIGMPStaticGroupVlanId_Type()
)
ctIGMPStaticGroupVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPStaticGroupVlanId.setStatus("current")
_CtIGMPStaticGroupSourceIPAddress_Type = IpAddress
_CtIGMPStaticGroupSourceIPAddress_Object = MibTableColumn
ctIGMPStaticGroupSourceIPAddress = _CtIGMPStaticGroupSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 3),
    _CtIGMPStaticGroupSourceIPAddress_Type()
)
ctIGMPStaticGroupSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPStaticGroupSourceIPAddress.setStatus("current")
_CtIGMPStaticGroupIncludeList_Type = PortList
_CtIGMPStaticGroupIncludeList_Object = MibTableColumn
ctIGMPStaticGroupIncludeList = _CtIGMPStaticGroupIncludeList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 4),
    _CtIGMPStaticGroupIncludeList_Type()
)
ctIGMPStaticGroupIncludeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIGMPStaticGroupIncludeList.setStatus("current")
_CtIGMPStaticGroupExcludeList_Type = PortList
_CtIGMPStaticGroupExcludeList_Object = MibTableColumn
ctIGMPStaticGroupExcludeList = _CtIGMPStaticGroupExcludeList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 5),
    _CtIGMPStaticGroupExcludeList_Type()
)
ctIGMPStaticGroupExcludeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIGMPStaticGroupExcludeList.setStatus("current")
_CtIGMPStaticGroupRowStatus_Type = RowStatus
_CtIGMPStaticGroupRowStatus_Object = MibTableColumn
ctIGMPStaticGroupRowStatus = _CtIGMPStaticGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 6, 1, 6),
    _CtIGMPStaticGroupRowStatus_Type()
)
ctIGMPStaticGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctIGMPStaticGroupRowStatus.setStatus("current")
_CtIGMPExtCacheTable_Object = MibTable
ctIGMPExtCacheTable = _CtIGMPExtCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7)
)
if mibBuilder.loadTexts:
    ctIGMPExtCacheTable.setStatus("current")
_CtIGMPExtCacheEntry_Object = MibTableRow
ctIGMPExtCacheEntry = _CtIGMPExtCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1)
)
ctIGMPExtCacheEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPExtCacheAddress"),
    (0, "CTRON-IGMP-MIB", "ctIGMPExtCacheVlanId"),
    (0, "CTRON-IGMP-MIB", "ctIGMPExtCacheSourceIPAddress"),
)
if mibBuilder.loadTexts:
    ctIGMPExtCacheEntry.setStatus("current")
_CtIGMPExtCacheAddress_Type = IpAddress
_CtIGMPExtCacheAddress_Object = MibTableColumn
ctIGMPExtCacheAddress = _CtIGMPExtCacheAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 1),
    _CtIGMPExtCacheAddress_Type()
)
ctIGMPExtCacheAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPExtCacheAddress.setStatus("current")
_CtIGMPExtCacheVlanId_Type = VlanId
_CtIGMPExtCacheVlanId_Object = MibTableColumn
ctIGMPExtCacheVlanId = _CtIGMPExtCacheVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 2),
    _CtIGMPExtCacheVlanId_Type()
)
ctIGMPExtCacheVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPExtCacheVlanId.setStatus("current")
_CtIGMPExtCacheSourceIPAddress_Type = IpAddress
_CtIGMPExtCacheSourceIPAddress_Object = MibTableColumn
ctIGMPExtCacheSourceIPAddress = _CtIGMPExtCacheSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 3),
    _CtIGMPExtCacheSourceIPAddress_Type()
)
ctIGMPExtCacheSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPExtCacheSourceIPAddress.setStatus("current")
_CtIGMPExtCacheLastReporter_Type = IpAddress
_CtIGMPExtCacheLastReporter_Object = MibTableColumn
ctIGMPExtCacheLastReporter = _CtIGMPExtCacheLastReporter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 4),
    _CtIGMPExtCacheLastReporter_Type()
)
ctIGMPExtCacheLastReporter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPExtCacheLastReporter.setStatus("current")
_CtIGMPExtCacheUpTime_Type = TimeTicks
_CtIGMPExtCacheUpTime_Object = MibTableColumn
ctIGMPExtCacheUpTime = _CtIGMPExtCacheUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 5),
    _CtIGMPExtCacheUpTime_Type()
)
ctIGMPExtCacheUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPExtCacheUpTime.setStatus("current")
_CtIGMPExtCacheExpiryTime_Type = TimeTicks
_CtIGMPExtCacheExpiryTime_Object = MibTableColumn
ctIGMPExtCacheExpiryTime = _CtIGMPExtCacheExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 6),
    _CtIGMPExtCacheExpiryTime_Type()
)
ctIGMPExtCacheExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPExtCacheExpiryTime.setStatus("current")
_CtIGMPExtCacheVersion1HostTimer_Type = Integer32
_CtIGMPExtCacheVersion1HostTimer_Object = MibTableColumn
ctIGMPExtCacheVersion1HostTimer = _CtIGMPExtCacheVersion1HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 7),
    _CtIGMPExtCacheVersion1HostTimer_Type()
)
ctIGMPExtCacheVersion1HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPExtCacheVersion1HostTimer.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPExtCacheVersion1HostTimer.setUnits("seconds")
_CtIGMPExtCacheOutPortList_Type = PortList
_CtIGMPExtCacheOutPortList_Object = MibTableColumn
ctIGMPExtCacheOutPortList = _CtIGMPExtCacheOutPortList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 8),
    _CtIGMPExtCacheOutPortList_Type()
)
ctIGMPExtCacheOutPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPExtCacheOutPortList.setStatus("current")


class _CtIGMPExtCacheSrcPort_Type(Integer32):
    """Custom type ctIGMPExtCacheSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CtIGMPExtCacheSrcPort_Type.__name__ = "Integer32"
_CtIGMPExtCacheSrcPort_Object = MibTableColumn
ctIGMPExtCacheSrcPort = _CtIGMPExtCacheSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 7, 1, 9),
    _CtIGMPExtCacheSrcPort_Type()
)
ctIGMPExtCacheSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPExtCacheSrcPort.setStatus("current")
_CtIGMPDiscoveredRouterTable_Object = MibTable
ctIGMPDiscoveredRouterTable = _CtIGMPDiscoveredRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8)
)
if mibBuilder.loadTexts:
    ctIGMPDiscoveredRouterTable.setStatus("current")
_CtIGMPDiscoveredRouterEntry_Object = MibTableRow
ctIGMPDiscoveredRouterEntry = _CtIGMPDiscoveredRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1)
)
ctIGMPDiscoveredRouterEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPDiscoveredRouterVlanId"),
)
if mibBuilder.loadTexts:
    ctIGMPDiscoveredRouterEntry.setStatus("current")
_CtIGMPDiscoveredRouterVlanId_Type = VlanId
_CtIGMPDiscoveredRouterVlanId_Object = MibTableColumn
ctIGMPDiscoveredRouterVlanId = _CtIGMPDiscoveredRouterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 2),
    _CtIGMPDiscoveredRouterVlanId_Type()
)
ctIGMPDiscoveredRouterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPDiscoveredRouterVlanId.setStatus("current")
_CtIGMPDiscoveredRouterPortList_Type = PortList
_CtIGMPDiscoveredRouterPortList_Object = MibTableColumn
ctIGMPDiscoveredRouterPortList = _CtIGMPDiscoveredRouterPortList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 3),
    _CtIGMPDiscoveredRouterPortList_Type()
)
ctIGMPDiscoveredRouterPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPDiscoveredRouterPortList.setStatus("current")
_CtIGMPDiscoveredRouterEgressPortList_Type = PortList
_CtIGMPDiscoveredRouterEgressPortList_Object = MibTableColumn
ctIGMPDiscoveredRouterEgressPortList = _CtIGMPDiscoveredRouterEgressPortList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 4),
    _CtIGMPDiscoveredRouterEgressPortList_Type()
)
ctIGMPDiscoveredRouterEgressPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPDiscoveredRouterEgressPortList.setStatus("current")
_CtIGMPDiscoveredRouterStaticPortList_Type = PortList
_CtIGMPDiscoveredRouterStaticPortList_Object = MibTableColumn
ctIGMPDiscoveredRouterStaticPortList = _CtIGMPDiscoveredRouterStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 8, 1, 5),
    _CtIGMPDiscoveredRouterStaticPortList_Type()
)
ctIGMPDiscoveredRouterStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIGMPDiscoveredRouterStaticPortList.setStatus("current")
_CtIGMPPortTable_Object = MibTable
ctIGMPPortTable = _CtIGMPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9)
)
if mibBuilder.loadTexts:
    ctIGMPPortTable.setStatus("current")
_CtIGMPPortTableEntry_Object = MibTableRow
ctIGMPPortTableEntry = _CtIGMPPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1)
)
ctIGMPPortTableEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPPortMode"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "CTRON-IGMP-MIB", "ctIGMPPortTableGroupAddress"),
    (0, "CTRON-IGMP-MIB", "ctIGMPPortTableVlanId"),
    (0, "CTRON-IGMP-MIB", "ctIGMPPortTableSourceIPAddress"),
)
if mibBuilder.loadTexts:
    ctIGMPPortTableEntry.setStatus("current")
_CtIGMPPortMode_Type = IgmpPortModeTc
_CtIGMPPortMode_Object = MibTableColumn
ctIGMPPortMode = _CtIGMPPortMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 1),
    _CtIGMPPortMode_Type()
)
ctIGMPPortMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPPortMode.setStatus("current")
_CtIGMPPortTableGroupAddress_Type = IpAddress
_CtIGMPPortTableGroupAddress_Object = MibTableColumn
ctIGMPPortTableGroupAddress = _CtIGMPPortTableGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 2),
    _CtIGMPPortTableGroupAddress_Type()
)
ctIGMPPortTableGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPPortTableGroupAddress.setStatus("current")
_CtIGMPPortTableVlanId_Type = VlanId
_CtIGMPPortTableVlanId_Object = MibTableColumn
ctIGMPPortTableVlanId = _CtIGMPPortTableVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 3),
    _CtIGMPPortTableVlanId_Type()
)
ctIGMPPortTableVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPPortTableVlanId.setStatus("current")
_CtIGMPPortTableSourceIPAddress_Type = IpAddress
_CtIGMPPortTableSourceIPAddress_Object = MibTableColumn
ctIGMPPortTableSourceIPAddress = _CtIGMPPortTableSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 4),
    _CtIGMPPortTableSourceIPAddress_Type()
)
ctIGMPPortTableSourceIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPPortTableSourceIPAddress.setStatus("current")
_CtIGMPPortTableExpireTime_Type = Integer32
_CtIGMPPortTableExpireTime_Object = MibTableColumn
ctIGMPPortTableExpireTime = _CtIGMPPortTableExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 9, 1, 5),
    _CtIGMPPortTableExpireTime_Type()
)
ctIGMPPortTableExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPPortTableExpireTime.setStatus("current")
if mibBuilder.loadTexts:
    ctIGMPPortTableExpireTime.setUnits("seconds")
_CtIGMPStatsCntrs_ObjectIdentity = ObjectIdentity
ctIGMPStatsCntrs = _CtIGMPStatsCntrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10)
)
_CtIGMPStatsCntrsGroupFull_Type = TruthValue
_CtIGMPStatsCntrsGroupFull_Object = MibScalar
ctIGMPStatsCntrsGroupFull = _CtIGMPStatsCntrsGroupFull_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 1),
    _CtIGMPStatsCntrsGroupFull_Type()
)
ctIGMPStatsCntrsGroupFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsGroupFull.setStatus("current")
_CtIGMPStatsCntrsNumV1QueriesSent_Type = Counter32
_CtIGMPStatsCntrsNumV1QueriesSent_Object = MibScalar
ctIGMPStatsCntrsNumV1QueriesSent = _CtIGMPStatsCntrsNumV1QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 2),
    _CtIGMPStatsCntrsNumV1QueriesSent_Type()
)
ctIGMPStatsCntrsNumV1QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumV1QueriesSent.setStatus("current")
_CtIGMPStatsCntrsNumV2QueriesSent_Type = Counter32
_CtIGMPStatsCntrsNumV2QueriesSent_Object = MibScalar
ctIGMPStatsCntrsNumV2QueriesSent = _CtIGMPStatsCntrsNumV2QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 3),
    _CtIGMPStatsCntrsNumV2QueriesSent_Type()
)
ctIGMPStatsCntrsNumV2QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumV2QueriesSent.setStatus("current")
_CtIGMPStatsCntrsNumV3QueriesSent_Type = Counter32
_CtIGMPStatsCntrsNumV3QueriesSent_Object = MibScalar
ctIGMPStatsCntrsNumV3QueriesSent = _CtIGMPStatsCntrsNumV3QueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 4),
    _CtIGMPStatsCntrsNumV3QueriesSent_Type()
)
ctIGMPStatsCntrsNumV3QueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumV3QueriesSent.setStatus("current")
_CtIGMPStatsCntrsNumGSQueriesSent_Type = Counter32
_CtIGMPStatsCntrsNumGSQueriesSent_Object = MibScalar
ctIGMPStatsCntrsNumGSQueriesSent = _CtIGMPStatsCntrsNumGSQueriesSent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 5),
    _CtIGMPStatsCntrsNumGSQueriesSent_Type()
)
ctIGMPStatsCntrsNumGSQueriesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumGSQueriesSent.setStatus("current")
_CtIGMPStatsCntrsNumQueriesRcvd_Type = Counter32
_CtIGMPStatsCntrsNumQueriesRcvd_Object = MibScalar
ctIGMPStatsCntrsNumQueriesRcvd = _CtIGMPStatsCntrsNumQueriesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 6),
    _CtIGMPStatsCntrsNumQueriesRcvd_Type()
)
ctIGMPStatsCntrsNumQueriesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumQueriesRcvd.setStatus("current")
_CtIGMPStatsCntrsNumV1ReportsRcvd_Type = Counter32
_CtIGMPStatsCntrsNumV1ReportsRcvd_Object = MibScalar
ctIGMPStatsCntrsNumV1ReportsRcvd = _CtIGMPStatsCntrsNumV1ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 7),
    _CtIGMPStatsCntrsNumV1ReportsRcvd_Type()
)
ctIGMPStatsCntrsNumV1ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumV1ReportsRcvd.setStatus("current")
_CtIGMPStatsCntrsNumV2ReportsRcvd_Type = Counter32
_CtIGMPStatsCntrsNumV2ReportsRcvd_Object = MibScalar
ctIGMPStatsCntrsNumV2ReportsRcvd = _CtIGMPStatsCntrsNumV2ReportsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 8),
    _CtIGMPStatsCntrsNumV2ReportsRcvd_Type()
)
ctIGMPStatsCntrsNumV2ReportsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumV2ReportsRcvd.setStatus("current")
_CtIGMPStatsCntrsNumV3ReportsReceived_Type = Counter32
_CtIGMPStatsCntrsNumV3ReportsReceived_Object = MibScalar
ctIGMPStatsCntrsNumV3ReportsReceived = _CtIGMPStatsCntrsNumV3ReportsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 9),
    _CtIGMPStatsCntrsNumV3ReportsReceived_Type()
)
ctIGMPStatsCntrsNumV3ReportsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumV3ReportsReceived.setStatus("current")
_CtIGMPStatsCntrsNumLeavesReceived_Type = Counter32
_CtIGMPStatsCntrsNumLeavesReceived_Object = MibScalar
ctIGMPStatsCntrsNumLeavesReceived = _CtIGMPStatsCntrsNumLeavesReceived_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 10),
    _CtIGMPStatsCntrsNumLeavesReceived_Type()
)
ctIGMPStatsCntrsNumLeavesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumLeavesReceived.setStatus("current")
_CtIGMPStatsCntrsNumDroppedFrames_Type = Counter32
_CtIGMPStatsCntrsNumDroppedFrames_Object = MibScalar
ctIGMPStatsCntrsNumDroppedFrames = _CtIGMPStatsCntrsNumDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 10, 11),
    _CtIGMPStatsCntrsNumDroppedFrames_Type()
)
ctIGMPStatsCntrsNumDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctIGMPStatsCntrsNumDroppedFrames.setStatus("current")
_CtIGMPProtocolClassificationTable_Object = MibTable
ctIGMPProtocolClassificationTable = _CtIGMPProtocolClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11)
)
if mibBuilder.loadTexts:
    ctIGMPProtocolClassificationTable.setStatus("current")
_CtIGMPProtocolClassificationEntry_Object = MibTableRow
ctIGMPProtocolClassificationEntry = _CtIGMPProtocolClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11, 1)
)
ctIGMPProtocolClassificationEntry.setIndexNames(
    (0, "CTRON-IGMP-MIB", "ctIGMPProtocolClassification"),
)
if mibBuilder.loadTexts:
    ctIGMPProtocolClassificationEntry.setStatus("current")
_CtIGMPProtocolClassification_Type = IgmpProtocolClassTc
_CtIGMPProtocolClassification_Object = MibTableColumn
ctIGMPProtocolClassification = _CtIGMPProtocolClassification_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11, 1, 1),
    _CtIGMPProtocolClassification_Type()
)
ctIGMPProtocolClassification.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctIGMPProtocolClassification.setStatus("current")
_CtIGMPProtocolIdentifier_Type = IgmpProtocolIdTc
_CtIGMPProtocolIdentifier_Object = MibTableColumn
ctIGMPProtocolIdentifier = _CtIGMPProtocolIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5, 1, 11, 1, 2),
    _CtIGMPProtocolIdentifier_Type()
)
ctIGMPProtocolIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctIGMPProtocolIdentifier.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-IGMP-MIB",
    **{"IgmpPortModeTc": IgmpPortModeTc,
       "IgmpProtocolClassTc": IgmpProtocolClassTc,
       "IgmpProtocolIdTc": IgmpProtocolIdTc,
       "ctIGMP": ctIGMP,
       "ctIGMPConfig": ctIGMPConfig,
       "ctIGMPNewDefaultState": ctIGMPNewDefaultState,
       "ctIGMPMibRev": ctIGMPMibRev,
       "ctIGMPMibRevString": ctIGMPMibRevString,
       "ctIGMPConfigGroupTblFullAction": ctIGMPConfigGroupTblFullAction,
       "ctIGMPVlanTable": ctIGMPVlanTable,
       "ctIGMPVlanEntry": ctIGMPVlanEntry,
       "ctIGMPVlanId": ctIGMPVlanId,
       "ctIGMPVlanQueryInterval": ctIGMPVlanQueryInterval,
       "ctIGMPVlanStatus": ctIGMPVlanStatus,
       "ctIGMPVlanVersion": ctIGMPVlanVersion,
       "ctIGMPVlanQuerier": ctIGMPVlanQuerier,
       "ctIGMPVlanQueryMaxResponseTime": ctIGMPVlanQueryMaxResponseTime,
       "ctIGMPVlanRobustness": ctIGMPVlanRobustness,
       "ctIGMPVlanLastMembQueryIntvl": ctIGMPVlanLastMembQueryIntvl,
       "ctIGMPVlanQuerierUpTime": ctIGMPVlanQuerierUpTime,
       "ctIGMPVlanQuerierExpiryTime": ctIGMPVlanQuerierExpiryTime,
       "ctIGMPVlanQuerierIP": ctIGMPVlanQuerierIP,
       "ctIGMPCacheTable": ctIGMPCacheTable,
       "ctIGMPCacheEntry": ctIGMPCacheEntry,
       "ctIGMPCacheAddress": ctIGMPCacheAddress,
       "ctIGMPCacheVlanId": ctIGMPCacheVlanId,
       "ctIGMPCacheIfIndex": ctIGMPCacheIfIndex,
       "ctIGMPCacheLastReporter": ctIGMPCacheLastReporter,
       "ctIGMPCacheUpTime": ctIGMPCacheUpTime,
       "ctIGMPCacheExpiryTime": ctIGMPCacheExpiryTime,
       "ctIGMPCacheVersion1HostTimer": ctIGMPCacheVersion1HostTimer,
       "ctIGMPPolicyTable": ctIGMPPolicyTable,
       "ctIGMPPolicyEntry": ctIGMPPolicyEntry,
       "ctIGMPPolicyAddress": ctIGMPPolicyAddress,
       "ctIGMPPolicyVlanId": ctIGMPPolicyVlanId,
       "ctIGMPPolicyIfIndex": ctIGMPPolicyIfIndex,
       "ctIGMPPolicyStatus": ctIGMPPolicyStatus,
       "ctIGMPPolicyInclusion": ctIGMPPolicyInclusion,
       "ctIGMPStaticTable": ctIGMPStaticTable,
       "ctIGMPStaticEntry": ctIGMPStaticEntry,
       "ctIGMPStaticGroupAddress": ctIGMPStaticGroupAddress,
       "ctIGMPStaticVlanId": ctIGMPStaticVlanId,
       "ctIGMPStaticOutPortList": ctIGMPStaticOutPortList,
       "ctIGMPStaticRowStatus": ctIGMPStaticRowStatus,
       "ctIGMPStaticGroupTable": ctIGMPStaticGroupTable,
       "ctIGMPStaticGroupEntry": ctIGMPStaticGroupEntry,
       "ctIGMPStaticGroupIPAddress": ctIGMPStaticGroupIPAddress,
       "ctIGMPStaticGroupVlanId": ctIGMPStaticGroupVlanId,
       "ctIGMPStaticGroupSourceIPAddress": ctIGMPStaticGroupSourceIPAddress,
       "ctIGMPStaticGroupIncludeList": ctIGMPStaticGroupIncludeList,
       "ctIGMPStaticGroupExcludeList": ctIGMPStaticGroupExcludeList,
       "ctIGMPStaticGroupRowStatus": ctIGMPStaticGroupRowStatus,
       "ctIGMPExtCacheTable": ctIGMPExtCacheTable,
       "ctIGMPExtCacheEntry": ctIGMPExtCacheEntry,
       "ctIGMPExtCacheAddress": ctIGMPExtCacheAddress,
       "ctIGMPExtCacheVlanId": ctIGMPExtCacheVlanId,
       "ctIGMPExtCacheSourceIPAddress": ctIGMPExtCacheSourceIPAddress,
       "ctIGMPExtCacheLastReporter": ctIGMPExtCacheLastReporter,
       "ctIGMPExtCacheUpTime": ctIGMPExtCacheUpTime,
       "ctIGMPExtCacheExpiryTime": ctIGMPExtCacheExpiryTime,
       "ctIGMPExtCacheVersion1HostTimer": ctIGMPExtCacheVersion1HostTimer,
       "ctIGMPExtCacheOutPortList": ctIGMPExtCacheOutPortList,
       "ctIGMPExtCacheSrcPort": ctIGMPExtCacheSrcPort,
       "ctIGMPDiscoveredRouterTable": ctIGMPDiscoveredRouterTable,
       "ctIGMPDiscoveredRouterEntry": ctIGMPDiscoveredRouterEntry,
       "ctIGMPDiscoveredRouterVlanId": ctIGMPDiscoveredRouterVlanId,
       "ctIGMPDiscoveredRouterPortList": ctIGMPDiscoveredRouterPortList,
       "ctIGMPDiscoveredRouterEgressPortList": ctIGMPDiscoveredRouterEgressPortList,
       "ctIGMPDiscoveredRouterStaticPortList": ctIGMPDiscoveredRouterStaticPortList,
       "ctIGMPPortTable": ctIGMPPortTable,
       "ctIGMPPortTableEntry": ctIGMPPortTableEntry,
       "ctIGMPPortMode": ctIGMPPortMode,
       "ctIGMPPortTableGroupAddress": ctIGMPPortTableGroupAddress,
       "ctIGMPPortTableVlanId": ctIGMPPortTableVlanId,
       "ctIGMPPortTableSourceIPAddress": ctIGMPPortTableSourceIPAddress,
       "ctIGMPPortTableExpireTime": ctIGMPPortTableExpireTime,
       "ctIGMPStatsCntrs": ctIGMPStatsCntrs,
       "ctIGMPStatsCntrsGroupFull": ctIGMPStatsCntrsGroupFull,
       "ctIGMPStatsCntrsNumV1QueriesSent": ctIGMPStatsCntrsNumV1QueriesSent,
       "ctIGMPStatsCntrsNumV2QueriesSent": ctIGMPStatsCntrsNumV2QueriesSent,
       "ctIGMPStatsCntrsNumV3QueriesSent": ctIGMPStatsCntrsNumV3QueriesSent,
       "ctIGMPStatsCntrsNumGSQueriesSent": ctIGMPStatsCntrsNumGSQueriesSent,
       "ctIGMPStatsCntrsNumQueriesRcvd": ctIGMPStatsCntrsNumQueriesRcvd,
       "ctIGMPStatsCntrsNumV1ReportsRcvd": ctIGMPStatsCntrsNumV1ReportsRcvd,
       "ctIGMPStatsCntrsNumV2ReportsRcvd": ctIGMPStatsCntrsNumV2ReportsRcvd,
       "ctIGMPStatsCntrsNumV3ReportsReceived": ctIGMPStatsCntrsNumV3ReportsReceived,
       "ctIGMPStatsCntrsNumLeavesReceived": ctIGMPStatsCntrsNumLeavesReceived,
       "ctIGMPStatsCntrsNumDroppedFrames": ctIGMPStatsCntrsNumDroppedFrames,
       "ctIGMPProtocolClassificationTable": ctIGMPProtocolClassificationTable,
       "ctIGMPProtocolClassificationEntry": ctIGMPProtocolClassificationEntry,
       "ctIGMPProtocolClassification": ctIGMPProtocolClassification,
       "ctIGMPProtocolIdentifier": ctIGMPProtocolIdentifier}
)
