# SNMP MIB module (ZYXEL-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-DHCP-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:34 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelDhcpSnooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDhcpSnoopingSetup_ObjectIdentity = ObjectIdentity
zyxelDhcpSnoopingSetup = _ZyxelDhcpSnoopingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1)
)
_ZyDhcpSnoopingState_Type = EnabledStatus
_ZyDhcpSnoopingState_Object = MibScalar
zyDhcpSnoopingState = _ZyDhcpSnoopingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 1),
    _ZyDhcpSnoopingState_Type()
)
zyDhcpSnoopingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingState.setStatus("current")
_ZyxelDhcpSnoopingVlanTable_Object = MibTable
zyxelDhcpSnoopingVlanTable = _ZyxelDhcpSnoopingVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelDhcpSnoopingVlanTable.setStatus("current")
_ZyxelDhcpSnoopingVlanEntry_Object = MibTableRow
zyxelDhcpSnoopingVlanEntry = _ZyxelDhcpSnoopingVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1)
)
zyxelDhcpSnoopingVlanEntry.setIndexNames(
    (0, "ZYXEL-DHCP-SNOOPING-MIB", "zyDhcpSnoopingVlanVid"),
)
if mibBuilder.loadTexts:
    zyxelDhcpSnoopingVlanEntry.setStatus("current")


class _ZyDhcpSnoopingVlanVid_Type(Integer32):
    """Custom type zyDhcpSnoopingVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyDhcpSnoopingVlanVid_Type.__name__ = "Integer32"
_ZyDhcpSnoopingVlanVid_Object = MibTableColumn
zyDhcpSnoopingVlanVid = _ZyDhcpSnoopingVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1, 1),
    _ZyDhcpSnoopingVlanVid_Type()
)
zyDhcpSnoopingVlanVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyDhcpSnoopingVlanVid.setStatus("current")
_ZyDhcpSnoopingVlanState_Type = EnabledStatus
_ZyDhcpSnoopingVlanState_Object = MibTableColumn
zyDhcpSnoopingVlanState = _ZyDhcpSnoopingVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1, 2),
    _ZyDhcpSnoopingVlanState_Type()
)
zyDhcpSnoopingVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingVlanState.setStatus("current")
_ZyDhcpSnoopingVlanOption82Profile_Type = DisplayString
_ZyDhcpSnoopingVlanOption82Profile_Object = MibTableColumn
zyDhcpSnoopingVlanOption82Profile = _ZyDhcpSnoopingVlanOption82Profile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 2, 1, 3),
    _ZyDhcpSnoopingVlanOption82Profile_Type()
)
zyDhcpSnoopingVlanOption82Profile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingVlanOption82Profile.setStatus("current")
_ZyxelDhcpSnoopingPortTable_Object = MibTable
zyxelDhcpSnoopingPortTable = _ZyxelDhcpSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelDhcpSnoopingPortTable.setStatus("current")
_ZyxelDhcpSnoopingPortEntry_Object = MibTableRow
zyxelDhcpSnoopingPortEntry = _ZyxelDhcpSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3, 1)
)
zyxelDhcpSnoopingPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelDhcpSnoopingPortEntry.setStatus("current")
_ZyDhcpSnoopingPortTrustState_Type = EnabledStatus
_ZyDhcpSnoopingPortTrustState_Object = MibTableColumn
zyDhcpSnoopingPortTrustState = _ZyDhcpSnoopingPortTrustState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3, 1, 1),
    _ZyDhcpSnoopingPortTrustState_Type()
)
zyDhcpSnoopingPortTrustState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingPortTrustState.setStatus("current")


class _ZyDhcpSnoopingPortRate_Type(Integer32):
    """Custom type zyDhcpSnoopingPortRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_ZyDhcpSnoopingPortRate_Type.__name__ = "Integer32"
_ZyDhcpSnoopingPortRate_Object = MibTableColumn
zyDhcpSnoopingPortRate = _ZyDhcpSnoopingPortRate_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 3, 1, 2),
    _ZyDhcpSnoopingPortRate_Type()
)
zyDhcpSnoopingPortRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingPortRate.setStatus("current")
_ZyxelDhcpSnoopingDb_ObjectIdentity = ObjectIdentity
zyxelDhcpSnoopingDb = _ZyxelDhcpSnoopingDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4)
)


class _ZyDhcpSnoopingDbAbort_Type(Integer32):
    """Custom type zyDhcpSnoopingDbAbort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZyDhcpSnoopingDbAbort_Type.__name__ = "Integer32"
_ZyDhcpSnoopingDbAbort_Object = MibScalar
zyDhcpSnoopingDbAbort = _ZyDhcpSnoopingDbAbort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 1),
    _ZyDhcpSnoopingDbAbort_Type()
)
zyDhcpSnoopingDbAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbAbort.setStatus("current")


class _ZyDhcpSnoopingDbWriteDelay_Type(Integer32):
    """Custom type zyDhcpSnoopingDbWriteDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZyDhcpSnoopingDbWriteDelay_Type.__name__ = "Integer32"
_ZyDhcpSnoopingDbWriteDelay_Object = MibScalar
zyDhcpSnoopingDbWriteDelay = _ZyDhcpSnoopingDbWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 2),
    _ZyDhcpSnoopingDbWriteDelay_Type()
)
zyDhcpSnoopingDbWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbWriteDelay.setStatus("current")


class _ZyDhcpSnoopingDbUrl_Type(DisplayString):
    """Custom type zyDhcpSnoopingDbUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZyDhcpSnoopingDbUrl_Type.__name__ = "DisplayString"
_ZyDhcpSnoopingDbUrl_Object = MibScalar
zyDhcpSnoopingDbUrl = _ZyDhcpSnoopingDbUrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 3),
    _ZyDhcpSnoopingDbUrl_Type()
)
zyDhcpSnoopingDbUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbUrl.setStatus("current")


class _ZyDhcpSnoopingDbUrlRenew_Type(DisplayString):
    """Custom type zyDhcpSnoopingDbUrlRenew based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ZyDhcpSnoopingDbUrlRenew_Type.__name__ = "DisplayString"
_ZyDhcpSnoopingDbUrlRenew_Object = MibScalar
zyDhcpSnoopingDbUrlRenew = _ZyDhcpSnoopingDbUrlRenew_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 4, 4),
    _ZyDhcpSnoopingDbUrlRenew_Type()
)
zyDhcpSnoopingDbUrlRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbUrlRenew.setStatus("current")
_ZyxelDhcpSnoopingDhcpVlan_ObjectIdentity = ObjectIdentity
zyxelDhcpSnoopingDhcpVlan = _ZyxelDhcpSnoopingDhcpVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 5)
)


class _ZyDhcpSnoopingDhcpVlanVid_Type(Integer32):
    """Custom type zyDhcpSnoopingDhcpVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZyDhcpSnoopingDhcpVlanVid_Type.__name__ = "Integer32"
_ZyDhcpSnoopingDhcpVlanVid_Object = MibScalar
zyDhcpSnoopingDhcpVlanVid = _ZyDhcpSnoopingDhcpVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 5, 1),
    _ZyDhcpSnoopingDhcpVlanVid_Type()
)
zyDhcpSnoopingDhcpVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDhcpVlanVid.setStatus("current")
_ZyDhcpSnoopingMaxNumberOfOption82VlanPort_Type = Integer32
_ZyDhcpSnoopingMaxNumberOfOption82VlanPort_Object = MibScalar
zyDhcpSnoopingMaxNumberOfOption82VlanPort = _ZyDhcpSnoopingMaxNumberOfOption82VlanPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 6),
    _ZyDhcpSnoopingMaxNumberOfOption82VlanPort_Type()
)
zyDhcpSnoopingMaxNumberOfOption82VlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingMaxNumberOfOption82VlanPort.setStatus("current")
_ZyxelDhcpSnoopingOption82VlanPortTable_Object = MibTable
zyxelDhcpSnoopingOption82VlanPortTable = _ZyxelDhcpSnoopingOption82VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 7)
)
if mibBuilder.loadTexts:
    zyxelDhcpSnoopingOption82VlanPortTable.setStatus("current")
_ZyxelDhcpSnoopingOption82VlanPortEntry_Object = MibTableRow
zyxelDhcpSnoopingOption82VlanPortEntry = _ZyxelDhcpSnoopingOption82VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 7, 1)
)
zyxelDhcpSnoopingOption82VlanPortEntry.setIndexNames(
    (0, "ZYXEL-DHCP-SNOOPING-MIB", "zyDhcpSnoopingVlanVid"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelDhcpSnoopingOption82VlanPortEntry.setStatus("current")
_ZyDhcpSnoopingOption82VlanPortProfile_Type = DisplayString
_ZyDhcpSnoopingOption82VlanPortProfile_Object = MibTableColumn
zyDhcpSnoopingOption82VlanPortProfile = _ZyDhcpSnoopingOption82VlanPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 1, 7, 1, 1),
    _ZyDhcpSnoopingOption82VlanPortProfile_Type()
)
zyDhcpSnoopingOption82VlanPortProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyDhcpSnoopingOption82VlanPortProfile.setStatus("current")
_ZyxelDhcpSnoopingStatus_ObjectIdentity = ObjectIdentity
zyxelDhcpSnoopingStatus = _ZyxelDhcpSnoopingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2)
)
_ZyDhcpSnoopingDbStatisticsClear_Type = EnabledStatus
_ZyDhcpSnoopingDbStatisticsClear_Object = MibScalar
zyDhcpSnoopingDbStatisticsClear = _ZyDhcpSnoopingDbStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 1),
    _ZyDhcpSnoopingDbStatisticsClear_Type()
)
zyDhcpSnoopingDbStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsClear.setStatus("current")
_ZyxelDhcpSnoopingDbStatistics_ObjectIdentity = ObjectIdentity
zyxelDhcpSnoopingDbStatistics = _ZyxelDhcpSnoopingDbStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2)
)


class _ZyDhcpSnoopingDbStatisticsAgentRunning_Type(Integer32):
    """Custom type zyDhcpSnoopingDbStatisticsAgentRunning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_ZyDhcpSnoopingDbStatisticsAgentRunning_Type.__name__ = "Integer32"
_ZyDhcpSnoopingDbStatisticsAgentRunning_Object = MibScalar
zyDhcpSnoopingDbStatisticsAgentRunning = _ZyDhcpSnoopingDbStatisticsAgentRunning_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 1),
    _ZyDhcpSnoopingDbStatisticsAgentRunning_Type()
)
zyDhcpSnoopingDbStatisticsAgentRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsAgentRunning.setStatus("current")
_ZyDhcpSnoopingDbStatisticsDelayExpiry_Type = Integer32
_ZyDhcpSnoopingDbStatisticsDelayExpiry_Object = MibScalar
zyDhcpSnoopingDbStatisticsDelayExpiry = _ZyDhcpSnoopingDbStatisticsDelayExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 2),
    _ZyDhcpSnoopingDbStatisticsDelayExpiry_Type()
)
zyDhcpSnoopingDbStatisticsDelayExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsDelayExpiry.setStatus("current")
_ZyDhcpSnoopingDbStatisticsAbortExpiry_Type = Integer32
_ZyDhcpSnoopingDbStatisticsAbortExpiry_Object = MibScalar
zyDhcpSnoopingDbStatisticsAbortExpiry = _ZyDhcpSnoopingDbStatisticsAbortExpiry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 3),
    _ZyDhcpSnoopingDbStatisticsAbortExpiry_Type()
)
zyDhcpSnoopingDbStatisticsAbortExpiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsAbortExpiry.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastSuccessTime_Type = DisplayString
_ZyDhcpSnoopingDbStatisticsLastSuccessTime_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastSuccessTime = _ZyDhcpSnoopingDbStatisticsLastSuccessTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 4),
    _ZyDhcpSnoopingDbStatisticsLastSuccessTime_Type()
)
zyDhcpSnoopingDbStatisticsLastSuccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastSuccessTime.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastFailTime_Type = DisplayString
_ZyDhcpSnoopingDbStatisticsLastFailTime_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastFailTime = _ZyDhcpSnoopingDbStatisticsLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 5),
    _ZyDhcpSnoopingDbStatisticsLastFailTime_Type()
)
zyDhcpSnoopingDbStatisticsLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastFailTime.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastFailReasonType_Type = DisplayString
_ZyDhcpSnoopingDbStatisticsLastFailReasonType_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastFailReasonType = _ZyDhcpSnoopingDbStatisticsLastFailReasonType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 6),
    _ZyDhcpSnoopingDbStatisticsLastFailReasonType_Type()
)
zyDhcpSnoopingDbStatisticsLastFailReasonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastFailReasonType.setStatus("current")
_ZyDhcpSnoopingDbStatisticsTotalAttempt_Type = Integer32
_ZyDhcpSnoopingDbStatisticsTotalAttempt_Object = MibScalar
zyDhcpSnoopingDbStatisticsTotalAttempt = _ZyDhcpSnoopingDbStatisticsTotalAttempt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 7),
    _ZyDhcpSnoopingDbStatisticsTotalAttempt_Type()
)
zyDhcpSnoopingDbStatisticsTotalAttempt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsTotalAttempt.setStatus("current")
_ZyDhcpSnoopingDbStatisticsStartupFail_Type = Integer32
_ZyDhcpSnoopingDbStatisticsStartupFail_Object = MibScalar
zyDhcpSnoopingDbStatisticsStartupFail = _ZyDhcpSnoopingDbStatisticsStartupFail_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 8),
    _ZyDhcpSnoopingDbStatisticsStartupFail_Type()
)
zyDhcpSnoopingDbStatisticsStartupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsStartupFail.setStatus("current")
_ZyDhcpSnoopingDbStatisticsSuccessTrans_Type = Integer32
_ZyDhcpSnoopingDbStatisticsSuccessTrans_Object = MibScalar
zyDhcpSnoopingDbStatisticsSuccessTrans = _ZyDhcpSnoopingDbStatisticsSuccessTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 9),
    _ZyDhcpSnoopingDbStatisticsSuccessTrans_Type()
)
zyDhcpSnoopingDbStatisticsSuccessTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsSuccessTrans.setStatus("current")
_ZyDhcpSnoopingDbStatisticsFailTrans_Type = Integer32
_ZyDhcpSnoopingDbStatisticsFailTrans_Object = MibScalar
zyDhcpSnoopingDbStatisticsFailTrans = _ZyDhcpSnoopingDbStatisticsFailTrans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 10),
    _ZyDhcpSnoopingDbStatisticsFailTrans_Type()
)
zyDhcpSnoopingDbStatisticsFailTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsFailTrans.setStatus("current")
_ZyDhcpSnoopingDbStatisticsSuccessRead_Type = Integer32
_ZyDhcpSnoopingDbStatisticsSuccessRead_Object = MibScalar
zyDhcpSnoopingDbStatisticsSuccessRead = _ZyDhcpSnoopingDbStatisticsSuccessRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 11),
    _ZyDhcpSnoopingDbStatisticsSuccessRead_Type()
)
zyDhcpSnoopingDbStatisticsSuccessRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsSuccessRead.setStatus("current")
_ZyDhcpSnoopingDbStatisticsFailRead_Type = Integer32
_ZyDhcpSnoopingDbStatisticsFailRead_Object = MibScalar
zyDhcpSnoopingDbStatisticsFailRead = _ZyDhcpSnoopingDbStatisticsFailRead_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 12),
    _ZyDhcpSnoopingDbStatisticsFailRead_Type()
)
zyDhcpSnoopingDbStatisticsFailRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsFailRead.setStatus("current")
_ZyDhcpSnoopingDbStatisticsSuccessWrite_Type = Integer32
_ZyDhcpSnoopingDbStatisticsSuccessWrite_Object = MibScalar
zyDhcpSnoopingDbStatisticsSuccessWrite = _ZyDhcpSnoopingDbStatisticsSuccessWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 13),
    _ZyDhcpSnoopingDbStatisticsSuccessWrite_Type()
)
zyDhcpSnoopingDbStatisticsSuccessWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsSuccessWrite.setStatus("current")
_ZyDhcpSnoopingDbStatisticsFailWrite_Type = Integer32
_ZyDhcpSnoopingDbStatisticsFailWrite_Object = MibScalar
zyDhcpSnoopingDbStatisticsFailWrite = _ZyDhcpSnoopingDbStatisticsFailWrite_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 14),
    _ZyDhcpSnoopingDbStatisticsFailWrite_Type()
)
zyDhcpSnoopingDbStatisticsFailWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsFailWrite.setStatus("current")


class _ZyDhcpSnoopingDbStatisticsFirstSuccessAccess_Type(Integer32):
    """Custom type zyDhcpSnoopingDbStatisticsFirstSuccessAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("read", 1),
          ("write", 2))
    )


_ZyDhcpSnoopingDbStatisticsFirstSuccessAccess_Type.__name__ = "Integer32"
_ZyDhcpSnoopingDbStatisticsFirstSuccessAccess_Object = MibScalar
zyDhcpSnoopingDbStatisticsFirstSuccessAccess = _ZyDhcpSnoopingDbStatisticsFirstSuccessAccess_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 15),
    _ZyDhcpSnoopingDbStatisticsFirstSuccessAccess_Type()
)
zyDhcpSnoopingDbStatisticsFirstSuccessAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsFirstSuccessAccess.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastIgnoreBindCollision_Type = Integer32
_ZyDhcpSnoopingDbStatisticsLastIgnoreBindCollision_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision = _ZyDhcpSnoopingDbStatisticsLastIgnoreBindCollision_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 16),
    _ZyDhcpSnoopingDbStatisticsLastIgnoreBindCollision_Type()
)
zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastIgnoreExpireLease_Type = Integer32
_ZyDhcpSnoopingDbStatisticsLastIgnoreExpireLease_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease = _ZyDhcpSnoopingDbStatisticsLastIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 17),
    _ZyDhcpSnoopingDbStatisticsLastIgnoreExpireLease_Type()
)
zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface_Type = Integer32
_ZyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface = _ZyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 18),
    _ZyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface_Type()
)
zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan_Type = Integer32
_ZyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan = _ZyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 19),
    _ZyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan_Type()
)
zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan.setStatus("current")
_ZyDhcpSnoopingDbStatisticsLastIgnoreParse_Type = Integer32
_ZyDhcpSnoopingDbStatisticsLastIgnoreParse_Object = MibScalar
zyDhcpSnoopingDbStatisticsLastIgnoreParse = _ZyDhcpSnoopingDbStatisticsLastIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 20),
    _ZyDhcpSnoopingDbStatisticsLastIgnoreParse_Type()
)
zyDhcpSnoopingDbStatisticsLastIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsLastIgnoreParse.setStatus("current")
_ZyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision_Type = Integer32
_ZyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision_Object = MibScalar
zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision = _ZyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 21),
    _ZyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision_Type()
)
zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision.setStatus("current")
_ZyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease_Type = Integer32
_ZyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease_Object = MibScalar
zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease = _ZyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 22),
    _ZyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease_Type()
)
zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease.setStatus("current")
_ZyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface_Type = Integer32
_ZyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface_Object = MibScalar
zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface = _ZyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 23),
    _ZyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface_Type()
)
zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface.setStatus("current")
_ZyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan_Type = Integer32
_ZyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan_Object = MibScalar
zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan = _ZyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 24),
    _ZyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan_Type()
)
zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan.setStatus("current")
_ZyDhcpSnoopingDbStatisticsTotalIgnoreParse_Type = Integer32
_ZyDhcpSnoopingDbStatisticsTotalIgnoreParse_Object = MibScalar
zyDhcpSnoopingDbStatisticsTotalIgnoreParse = _ZyDhcpSnoopingDbStatisticsTotalIgnoreParse_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 20, 2, 2, 25),
    _ZyDhcpSnoopingDbStatisticsTotalIgnoreParse_Type()
)
zyDhcpSnoopingDbStatisticsTotalIgnoreParse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyDhcpSnoopingDbStatisticsTotalIgnoreParse.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DHCP-SNOOPING-MIB",
    **{"zyxelDhcpSnooping": zyxelDhcpSnooping,
       "zyxelDhcpSnoopingSetup": zyxelDhcpSnoopingSetup,
       "zyDhcpSnoopingState": zyDhcpSnoopingState,
       "zyxelDhcpSnoopingVlanTable": zyxelDhcpSnoopingVlanTable,
       "zyxelDhcpSnoopingVlanEntry": zyxelDhcpSnoopingVlanEntry,
       "zyDhcpSnoopingVlanVid": zyDhcpSnoopingVlanVid,
       "zyDhcpSnoopingVlanState": zyDhcpSnoopingVlanState,
       "zyDhcpSnoopingVlanOption82Profile": zyDhcpSnoopingVlanOption82Profile,
       "zyxelDhcpSnoopingPortTable": zyxelDhcpSnoopingPortTable,
       "zyxelDhcpSnoopingPortEntry": zyxelDhcpSnoopingPortEntry,
       "zyDhcpSnoopingPortTrustState": zyDhcpSnoopingPortTrustState,
       "zyDhcpSnoopingPortRate": zyDhcpSnoopingPortRate,
       "zyxelDhcpSnoopingDb": zyxelDhcpSnoopingDb,
       "zyDhcpSnoopingDbAbort": zyDhcpSnoopingDbAbort,
       "zyDhcpSnoopingDbWriteDelay": zyDhcpSnoopingDbWriteDelay,
       "zyDhcpSnoopingDbUrl": zyDhcpSnoopingDbUrl,
       "zyDhcpSnoopingDbUrlRenew": zyDhcpSnoopingDbUrlRenew,
       "zyxelDhcpSnoopingDhcpVlan": zyxelDhcpSnoopingDhcpVlan,
       "zyDhcpSnoopingDhcpVlanVid": zyDhcpSnoopingDhcpVlanVid,
       "zyDhcpSnoopingMaxNumberOfOption82VlanPort": zyDhcpSnoopingMaxNumberOfOption82VlanPort,
       "zyxelDhcpSnoopingOption82VlanPortTable": zyxelDhcpSnoopingOption82VlanPortTable,
       "zyxelDhcpSnoopingOption82VlanPortEntry": zyxelDhcpSnoopingOption82VlanPortEntry,
       "zyDhcpSnoopingOption82VlanPortProfile": zyDhcpSnoopingOption82VlanPortProfile,
       "zyxelDhcpSnoopingStatus": zyxelDhcpSnoopingStatus,
       "zyDhcpSnoopingDbStatisticsClear": zyDhcpSnoopingDbStatisticsClear,
       "zyxelDhcpSnoopingDbStatistics": zyxelDhcpSnoopingDbStatistics,
       "zyDhcpSnoopingDbStatisticsAgentRunning": zyDhcpSnoopingDbStatisticsAgentRunning,
       "zyDhcpSnoopingDbStatisticsDelayExpiry": zyDhcpSnoopingDbStatisticsDelayExpiry,
       "zyDhcpSnoopingDbStatisticsAbortExpiry": zyDhcpSnoopingDbStatisticsAbortExpiry,
       "zyDhcpSnoopingDbStatisticsLastSuccessTime": zyDhcpSnoopingDbStatisticsLastSuccessTime,
       "zyDhcpSnoopingDbStatisticsLastFailTime": zyDhcpSnoopingDbStatisticsLastFailTime,
       "zyDhcpSnoopingDbStatisticsLastFailReasonType": zyDhcpSnoopingDbStatisticsLastFailReasonType,
       "zyDhcpSnoopingDbStatisticsTotalAttempt": zyDhcpSnoopingDbStatisticsTotalAttempt,
       "zyDhcpSnoopingDbStatisticsStartupFail": zyDhcpSnoopingDbStatisticsStartupFail,
       "zyDhcpSnoopingDbStatisticsSuccessTrans": zyDhcpSnoopingDbStatisticsSuccessTrans,
       "zyDhcpSnoopingDbStatisticsFailTrans": zyDhcpSnoopingDbStatisticsFailTrans,
       "zyDhcpSnoopingDbStatisticsSuccessRead": zyDhcpSnoopingDbStatisticsSuccessRead,
       "zyDhcpSnoopingDbStatisticsFailRead": zyDhcpSnoopingDbStatisticsFailRead,
       "zyDhcpSnoopingDbStatisticsSuccessWrite": zyDhcpSnoopingDbStatisticsSuccessWrite,
       "zyDhcpSnoopingDbStatisticsFailWrite": zyDhcpSnoopingDbStatisticsFailWrite,
       "zyDhcpSnoopingDbStatisticsFirstSuccessAccess": zyDhcpSnoopingDbStatisticsFirstSuccessAccess,
       "zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision": zyDhcpSnoopingDbStatisticsLastIgnoreBindCollision,
       "zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease": zyDhcpSnoopingDbStatisticsLastIgnoreExpireLease,
       "zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface": zyDhcpSnoopingDbStatisticsLastIgnoreInvalidInterface,
       "zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan": zyDhcpSnoopingDbStatisticsLastIgnoreUnsupportedVlan,
       "zyDhcpSnoopingDbStatisticsLastIgnoreParse": zyDhcpSnoopingDbStatisticsLastIgnoreParse,
       "zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision": zyDhcpSnoopingDbStatisticsTotalIgnoreBindCollision,
       "zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease": zyDhcpSnoopingDbStatisticsTotalIgnoreExpireLease,
       "zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface": zyDhcpSnoopingDbStatisticsTotalIgnoreInvalidInterface,
       "zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan": zyDhcpSnoopingDbStatisticsTotalIgnoreUnsupportedVlan,
       "zyDhcpSnoopingDbStatisticsTotalIgnoreParse": zyDhcpSnoopingDbStatisticsTotalIgnoreParse}
)
