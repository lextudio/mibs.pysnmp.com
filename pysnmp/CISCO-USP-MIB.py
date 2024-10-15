# SNMP MIB module (CISCO-USP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-USP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:35 2024
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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoUspMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827)
)
ciscoUspMIB.setRevisions(
        ("2015-07-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoUspMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoUspMIBNotifs = _CiscoUspMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0)
)
_CiscoUspMIBObjects_ObjectIdentity = ObjectIdentity
ciscoUspMIBObjects = _CiscoUspMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1)
)
_CuspScalar_ObjectIdentity = ObjectIdentity
cuspScalar = _CuspScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1)
)
_CuspLastCounterResetTime_Type = DateAndTime
_CuspLastCounterResetTime_Object = MibScalar
cuspLastCounterResetTime = _CuspLastCounterResetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 1),
    _CuspLastCounterResetTime_Type()
)
cuspLastCounterResetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspLastCounterResetTime.setStatus("current")


class _CuspSystemState_Type(Integer32):
    """Custom type cuspSystemState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CuspSystemState_Type.__name__ = "Integer32"
_CuspSystemState_Object = MibScalar
cuspSystemState = _CuspSystemState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 2),
    _CuspSystemState_Type()
)
cuspSystemState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspSystemState.setStatus("current")
_CuspSystemUpTime_Type = TimeStamp
_CuspSystemUpTime_Object = MibScalar
cuspSystemUpTime = _CuspSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 3),
    _CuspSystemUpTime_Type()
)
cuspSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspSystemUpTime.setStatus("current")


class _CuspLicenseLimit_Type(Unsigned32):
    """Custom type cuspLicenseLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_CuspLicenseLimit_Type.__name__ = "Unsigned32"
_CuspLicenseLimit_Object = MibScalar
cuspLicenseLimit = _CuspLicenseLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 4),
    _CuspLicenseLimit_Type()
)
cuspLicenseLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspLicenseLimit.setStatus("current")
if mibBuilder.loadTexts:
    cuspLicenseLimit.setUnits("CPS")


class _CuspLicenseState_Type(Integer32):
    """Custom type cuspLicenseState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("authorizedperiodexpired", 12),
          ("disabled", 11),
          ("eval", 10),
          ("evalexpired", 9),
          ("incompliance", 8),
          ("init", 7),
          ("invalid", 6),
          ("invalidtag", 5),
          ("notapplicable", 4),
          ("outofcompliance", 3),
          ("overage", 2),
          ("waiting", 1))
    )


_CuspLicenseState_Type.__name__ = "Integer32"
_CuspLicenseState_Object = MibScalar
cuspLicenseState = _CuspLicenseState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 5),
    _CuspLicenseState_Type()
)
cuspLicenseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspLicenseState.setStatus("current")


class _CuspSmartAgentState_Type(Integer32):
    """Custom type cuspSmartAgentState based on Integer32"""
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
        *(("authorizationexpiry", 7),
          ("authorized", 6),
          ("evalexpired", 3),
          ("outofcomplaince", 5),
          ("registered", 4),
          ("transient", 8),
          ("unconfigured", 1),
          ("unidentified", 2))
    )


_CuspSmartAgentState_Type.__name__ = "Integer32"
_CuspSmartAgentState_Object = MibScalar
cuspSmartAgentState = _CuspSmartAgentState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 6),
    _CuspSmartAgentState_Type()
)
cuspSmartAgentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspSmartAgentState.setStatus("current")
_CuspConfiguredMemory_Type = Unsigned32
_CuspConfiguredMemory_Object = MibScalar
cuspConfiguredMemory = _CuspConfiguredMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 7),
    _CuspConfiguredMemory_Type()
)
cuspConfiguredMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspConfiguredMemory.setStatus("current")
if mibBuilder.loadTexts:
    cuspConfiguredMemory.setUnits("MegaByte")
_CuspMemoryUsed_Type = Unsigned32
_CuspMemoryUsed_Object = MibScalar
cuspMemoryUsed = _CuspMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 8),
    _CuspMemoryUsed_Type()
)
cuspMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    cuspMemoryUsed.setUnits("MegaByte")
_CuspDiskSpaceUsed_Type = Integer32
_CuspDiskSpaceUsed_Object = MibScalar
cuspDiskSpaceUsed = _CuspDiskSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 9),
    _CuspDiskSpaceUsed_Type()
)
cuspDiskSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspDiskSpaceUsed.setStatus("current")
_CuspCallStats_ObjectIdentity = ObjectIdentity
cuspCallStats = _CuspCallStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10)
)
_CuspTotalCalls_Type = Counter32
_CuspTotalCalls_Object = MibScalar
cuspTotalCalls = _CuspTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 1),
    _CuspTotalCalls_Type()
)
cuspTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspTotalCalls.setStatus("current")
_CuspTotalFailedCalls_Type = Counter32
_CuspTotalFailedCalls_Object = MibScalar
cuspTotalFailedCalls = _CuspTotalFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 2),
    _CuspTotalFailedCalls_Type()
)
cuspTotalFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspTotalFailedCalls.setStatus("current")
_CuspCPS_Type = Unsigned32
_CuspCPS_Object = MibScalar
cuspCPS = _CuspCPS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 3),
    _CuspCPS_Type()
)
cuspCPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspCPS.setStatus("current")
if mibBuilder.loadTexts:
    cuspCPS.setUnits("CPS")
_CuspAvgCPSOneMin_Type = Unsigned32
_CuspAvgCPSOneMin_Object = MibScalar
cuspAvgCPSOneMin = _CuspAvgCPSOneMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 4),
    _CuspAvgCPSOneMin_Type()
)
cuspAvgCPSOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspAvgCPSOneMin.setStatus("current")
if mibBuilder.loadTexts:
    cuspAvgCPSOneMin.setUnits("CPS")
_CuspMaxCPSOneMin_Type = Unsigned32
_CuspMaxCPSOneMin_Object = MibScalar
cuspMaxCPSOneMin = _CuspMaxCPSOneMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 5),
    _CuspMaxCPSOneMin_Type()
)
cuspMaxCPSOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspMaxCPSOneMin.setStatus("current")
if mibBuilder.loadTexts:
    cuspMaxCPSOneMin.setUnits("CPS")
_CuspDroppedCallsOneSec_Type = Unsigned32
_CuspDroppedCallsOneSec_Object = MibScalar
cuspDroppedCallsOneSec = _CuspDroppedCallsOneSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 6),
    _CuspDroppedCallsOneSec_Type()
)
cuspDroppedCallsOneSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspDroppedCallsOneSec.setStatus("current")
_CuspAvgDroppedCPSOneMin_Type = Unsigned32
_CuspAvgDroppedCPSOneMin_Object = MibScalar
cuspAvgDroppedCPSOneMin = _CuspAvgDroppedCPSOneMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 7),
    _CuspAvgDroppedCPSOneMin_Type()
)
cuspAvgDroppedCPSOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspAvgDroppedCPSOneMin.setStatus("current")
_CuspMaxDroppedCPSOneMin_Type = Unsigned32
_CuspMaxDroppedCPSOneMin_Object = MibScalar
cuspMaxDroppedCPSOneMin = _CuspMaxDroppedCPSOneMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 8),
    _CuspMaxDroppedCPSOneMin_Type()
)
cuspMaxDroppedCPSOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspMaxDroppedCPSOneMin.setStatus("current")
_CuspCallsRoutedOneSec_Type = Unsigned32
_CuspCallsRoutedOneSec_Object = MibScalar
cuspCallsRoutedOneSec = _CuspCallsRoutedOneSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 9),
    _CuspCallsRoutedOneSec_Type()
)
cuspCallsRoutedOneSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspCallsRoutedOneSec.setStatus("current")
_CuspAvgCallsRoutedOneMin_Type = Unsigned32
_CuspAvgCallsRoutedOneMin_Object = MibScalar
cuspAvgCallsRoutedOneMin = _CuspAvgCallsRoutedOneMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 10),
    _CuspAvgCallsRoutedOneMin_Type()
)
cuspAvgCallsRoutedOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspAvgCallsRoutedOneMin.setStatus("current")
_CuspMaxCallsRoutedOneMin_Type = Unsigned32
_CuspMaxCallsRoutedOneMin_Object = MibScalar
cuspMaxCallsRoutedOneMin = _CuspMaxCallsRoutedOneMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 11),
    _CuspMaxCallsRoutedOneMin_Type()
)
cuspMaxCallsRoutedOneMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspMaxCallsRoutedOneMin.setStatus("current")
_CuspCallsDroppedExceedingLicense_Type = Unsigned32
_CuspCallsDroppedExceedingLicense_Object = MibScalar
cuspCallsDroppedExceedingLicense = _CuspCallsDroppedExceedingLicense_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 10, 12),
    _CuspCallsDroppedExceedingLicense_Type()
)
cuspCallsDroppedExceedingLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspCallsDroppedExceedingLicense.setStatus("current")
if mibBuilder.loadTexts:
    cuspCallsDroppedExceedingLicense.setUnits("CPS")
_CuspMessageStats_ObjectIdentity = ObjectIdentity
cuspMessageStats = _CuspMessageStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 11)
)
_CuspStrayMessageCount_Type = Unsigned32
_CuspStrayMessageCount_Object = MibScalar
cuspStrayMessageCount = _CuspStrayMessageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 11, 1),
    _CuspStrayMessageCount_Type()
)
cuspStrayMessageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspStrayMessageCount.setStatus("current")
if mibBuilder.loadTexts:
    cuspStrayMessageCount.setUnits("Messages")
_CuspNoOfMessagesRecieved_Type = Unsigned32
_CuspNoOfMessagesRecieved_Object = MibScalar
cuspNoOfMessagesRecieved = _CuspNoOfMessagesRecieved_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 11, 2),
    _CuspNoOfMessagesRecieved_Type()
)
cuspNoOfMessagesRecieved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspNoOfMessagesRecieved.setStatus("current")
_CuspThresholdValues_ObjectIdentity = ObjectIdentity
cuspThresholdValues = _CuspThresholdValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 12)
)


class _CuspDiskSpaceThresholdValue_Type(Integer32):
    """Custom type cuspDiskSpaceThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CuspDiskSpaceThresholdValue_Type.__name__ = "Integer32"
_CuspDiskSpaceThresholdValue_Object = MibScalar
cuspDiskSpaceThresholdValue = _CuspDiskSpaceThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 12, 1),
    _CuspDiskSpaceThresholdValue_Type()
)
cuspDiskSpaceThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspDiskSpaceThresholdValue.setStatus("current")


class _CuspMemoryThresholdValue_Type(Integer32):
    """Custom type cuspMemoryThresholdValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CuspMemoryThresholdValue_Type.__name__ = "Integer32"
_CuspMemoryThresholdValue_Object = MibScalar
cuspMemoryThresholdValue = _CuspMemoryThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 1, 12, 2),
    _CuspMemoryThresholdValue_Type()
)
cuspMemoryThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspMemoryThresholdValue.setStatus("current")
_CuspTable_ObjectIdentity = ObjectIdentity
cuspTable = _CuspTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2)
)
_CuspServerGroupTable_Object = MibTable
cuspServerGroupTable = _CuspServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cuspServerGroupTable.setStatus("current")
_CuspServerGroupEntry_Object = MibTableRow
cuspServerGroupEntry = _CuspServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1)
)
cuspServerGroupEntry.setIndexNames(
    (0, "CISCO-USP-MIB", "cuspServerGroupIndex"),
)
if mibBuilder.loadTexts:
    cuspServerGroupEntry.setStatus("current")
_CuspServerGroupIndex_Type = Unsigned32
_CuspServerGroupIndex_Object = MibTableColumn
cuspServerGroupIndex = _CuspServerGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 1),
    _CuspServerGroupIndex_Type()
)
cuspServerGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuspServerGroupIndex.setStatus("current")
_CuspServerGroupName_Type = OctetString
_CuspServerGroupName_Object = MibTableColumn
cuspServerGroupName = _CuspServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 2),
    _CuspServerGroupName_Type()
)
cuspServerGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspServerGroupName.setStatus("current")
_CuspServerGroupNetwork_Type = OctetString
_CuspServerGroupNetwork_Object = MibTableColumn
cuspServerGroupNetwork = _CuspServerGroupNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 3),
    _CuspServerGroupNetwork_Type()
)
cuspServerGroupNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspServerGroupNetwork.setStatus("current")


class _CuspServerGroupStatus_Type(Integer32):
    """Custom type cuspServerGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("partialdown", 2),
          ("up", 1))
    )


_CuspServerGroupStatus_Type.__name__ = "Integer32"
_CuspServerGroupStatus_Object = MibTableColumn
cuspServerGroupStatus = _CuspServerGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 4),
    _CuspServerGroupStatus_Type()
)
cuspServerGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspServerGroupStatus.setStatus("current")
_CuspServerGroupPingStatus_Type = TruthValue
_CuspServerGroupPingStatus_Object = MibTableColumn
cuspServerGroupPingStatus = _CuspServerGroupPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 5),
    _CuspServerGroupPingStatus_Type()
)
cuspServerGroupPingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspServerGroupPingStatus.setStatus("current")


class _CuspServerGroupLBType_Type(Integer32):
    """Custom type cuspServerGroupLBType based on Integer32"""
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
        *(("callid", 4),
          ("global", 1),
          ("highestq", 2),
          ("requesturi", 3),
          ("touri", 5),
          ("weight", 6))
    )


_CuspServerGroupLBType_Type.__name__ = "Integer32"
_CuspServerGroupLBType_Object = MibTableColumn
cuspServerGroupLBType = _CuspServerGroupLBType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 1, 1, 6),
    _CuspServerGroupLBType_Type()
)
cuspServerGroupLBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspServerGroupLBType.setStatus("current")
_CuspElementTable_Object = MibTable
cuspElementTable = _CuspElementTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cuspElementTable.setStatus("current")
_CuspElementEntry_Object = MibTableRow
cuspElementEntry = _CuspElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1)
)
cuspElementEntry.setIndexNames(
    (0, "CISCO-USP-MIB", "cuspServerGroupIndex"),
    (0, "CISCO-USP-MIB", "cuspElementIndex"),
)
if mibBuilder.loadTexts:
    cuspElementEntry.setStatus("current")
_CuspElementIndex_Type = Unsigned32
_CuspElementIndex_Object = MibTableColumn
cuspElementIndex = _CuspElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 1),
    _CuspElementIndex_Type()
)
cuspElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cuspElementIndex.setStatus("current")


class _CuspElementName_Type(OctetString):
    """Custom type cuspElementName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CuspElementName_Type.__name__ = "OctetString"
_CuspElementName_Object = MibTableColumn
cuspElementName = _CuspElementName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 2),
    _CuspElementName_Type()
)
cuspElementName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementName.setStatus("current")


class _CuspElementStatus_Type(Integer32):
    """Custom type cuspElementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CuspElementStatus_Type.__name__ = "Integer32"
_CuspElementStatus_Object = MibTableColumn
cuspElementStatus = _CuspElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 3),
    _CuspElementStatus_Type()
)
cuspElementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementStatus.setStatus("current")
_CuspElementQValue_Type = OctetString
_CuspElementQValue_Object = MibTableColumn
cuspElementQValue = _CuspElementQValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 4),
    _CuspElementQValue_Type()
)
cuspElementQValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementQValue.setStatus("current")


class _CuspElementWeight_Type(Integer32):
    """Custom type cuspElementWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CuspElementWeight_Type.__name__ = "Integer32"
_CuspElementWeight_Object = MibTableColumn
cuspElementWeight = _CuspElementWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 5),
    _CuspElementWeight_Type()
)
cuspElementWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementWeight.setStatus("current")


class _CuspElementPort_Type(Integer32):
    """Custom type cuspElementPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CuspElementPort_Type.__name__ = "Integer32"
_CuspElementPort_Object = MibTableColumn
cuspElementPort = _CuspElementPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 6),
    _CuspElementPort_Type()
)
cuspElementPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementPort.setStatus("current")


class _CuspElementTransport_Type(Integer32):
    """Custom type cuspElementTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 2),
          ("tls", 3),
          ("udp", 1))
    )


_CuspElementTransport_Type.__name__ = "Integer32"
_CuspElementTransport_Object = MibTableColumn
cuspElementTransport = _CuspElementTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 7),
    _CuspElementTransport_Type()
)
cuspElementTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementTransport.setStatus("current")
_CuspElementTotalCalls_Type = Unsigned32
_CuspElementTotalCalls_Object = MibTableColumn
cuspElementTotalCalls = _CuspElementTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 8),
    _CuspElementTotalCalls_Type()
)
cuspElementTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementTotalCalls.setStatus("current")
_CuspElementFailedCalls_Type = Unsigned32
_CuspElementFailedCalls_Object = MibTableColumn
cuspElementFailedCalls = _CuspElementFailedCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 2, 2, 1, 9),
    _CuspElementFailedCalls_Type()
)
cuspElementFailedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cuspElementFailedCalls.setStatus("current")
_CuspNotifControlInfo_ObjectIdentity = ObjectIdentity
cuspNotifControlInfo = _CuspNotifControlInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3)
)


class _CuspNotifSeverity_Type(Integer32):
    """Custom type cuspNotifSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("informational", 3),
          ("warning", 2))
    )


_CuspNotifSeverity_Type.__name__ = "Integer32"
_CuspNotifSeverity_Object = MibScalar
cuspNotifSeverity = _CuspNotifSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 1),
    _CuspNotifSeverity_Type()
)
cuspNotifSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuspNotifSeverity.setStatus("current")


class _CuspNotifDetail_Type(OctetString):
    """Custom type cuspNotifDetail based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CuspNotifDetail_Type.__name__ = "OctetString"
_CuspNotifDetail_Object = MibScalar
cuspNotifDetail = _CuspNotifDetail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 2),
    _CuspNotifDetail_Type()
)
cuspNotifDetail.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cuspNotifDetail.setStatus("current")
_CuspSystemStateAlertEnable_Type = TruthValue
_CuspSystemStateAlertEnable_Object = MibScalar
cuspSystemStateAlertEnable = _CuspSystemStateAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 3),
    _CuspSystemStateAlertEnable_Type()
)
cuspSystemStateAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspSystemStateAlertEnable.setStatus("current")
_CuspServerGroupAlertEnable_Type = TruthValue
_CuspServerGroupAlertEnable_Object = MibScalar
cuspServerGroupAlertEnable = _CuspServerGroupAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 4),
    _CuspServerGroupAlertEnable_Type()
)
cuspServerGroupAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspServerGroupAlertEnable.setStatus("current")
_CuspServerGroupElementAlertEnable_Type = TruthValue
_CuspServerGroupElementAlertEnable_Object = MibScalar
cuspServerGroupElementAlertEnable = _CuspServerGroupElementAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 5),
    _CuspServerGroupElementAlertEnable_Type()
)
cuspServerGroupElementAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspServerGroupElementAlertEnable.setStatus("current")
_CuspLicenseExceededAlertEnable_Type = TruthValue
_CuspLicenseExceededAlertEnable_Object = MibScalar
cuspLicenseExceededAlertEnable = _CuspLicenseExceededAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 6),
    _CuspLicenseExceededAlertEnable_Type()
)
cuspLicenseExceededAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspLicenseExceededAlertEnable.setStatus("current")
_CuspLicenseStateAlertEnable_Type = TruthValue
_CuspLicenseStateAlertEnable_Object = MibScalar
cuspLicenseStateAlertEnable = _CuspLicenseStateAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 7),
    _CuspLicenseStateAlertEnable_Type()
)
cuspLicenseStateAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspLicenseStateAlertEnable.setStatus("current")
_CuspExtensiveLoggingAlertEnable_Type = TruthValue
_CuspExtensiveLoggingAlertEnable_Object = MibScalar
cuspExtensiveLoggingAlertEnable = _CuspExtensiveLoggingAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 8),
    _CuspExtensiveLoggingAlertEnable_Type()
)
cuspExtensiveLoggingAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspExtensiveLoggingAlertEnable.setStatus("current")
_CuspDiskSpaceThresholdAlertEnable_Type = TruthValue
_CuspDiskSpaceThresholdAlertEnable_Object = MibScalar
cuspDiskSpaceThresholdAlertEnable = _CuspDiskSpaceThresholdAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 9),
    _CuspDiskSpaceThresholdAlertEnable_Type()
)
cuspDiskSpaceThresholdAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspDiskSpaceThresholdAlertEnable.setStatus("current")
_CuspMemoryThresholdAlertEnable_Type = TruthValue
_CuspMemoryThresholdAlertEnable_Object = MibScalar
cuspMemoryThresholdAlertEnable = _CuspMemoryThresholdAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 10),
    _CuspMemoryThresholdAlertEnable_Type()
)
cuspMemoryThresholdAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspMemoryThresholdAlertEnable.setStatus("current")
_CuspBackupProcessFailAlertEnable_Type = TruthValue
_CuspBackupProcessFailAlertEnable_Object = MibScalar
cuspBackupProcessFailAlertEnable = _CuspBackupProcessFailAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 11),
    _CuspBackupProcessFailAlertEnable_Type()
)
cuspBackupProcessFailAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspBackupProcessFailAlertEnable.setStatus("current")
_CuspConnectionExceptionAlertEnable_Type = TruthValue
_CuspConnectionExceptionAlertEnable_Object = MibScalar
cuspConnectionExceptionAlertEnable = _CuspConnectionExceptionAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 1, 3, 12),
    _CuspConnectionExceptionAlertEnable_Type()
)
cuspConnectionExceptionAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cuspConnectionExceptionAlertEnable.setStatus("current")
_CiscoUspMIBConform_ObjectIdentity = ObjectIdentity
ciscoUspMIBConform = _CiscoUspMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 2)
)
_CiscoUspMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoUspMIBCompliances = _CiscoUspMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 1)
)
_CiscoUspMIBGroups_ObjectIdentity = ObjectIdentity
ciscoUspMIBGroups = _CiscoUspMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 2)
)

# Managed Objects groups

ciscoUspMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 2, 1)
)
ciscoUspMIBMainObjectGroup.setObjects(
      *(("CISCO-USP-MIB", "cuspLicenseLimit"),
        ("CISCO-USP-MIB", "cuspLastCounterResetTime"),
        ("CISCO-USP-MIB", "cuspTotalCalls"),
        ("CISCO-USP-MIB", "cuspTotalFailedCalls"),
        ("CISCO-USP-MIB", "cuspCPS"),
        ("CISCO-USP-MIB", "cuspAvgCPSOneMin"),
        ("CISCO-USP-MIB", "cuspMaxCPSOneMin"),
        ("CISCO-USP-MIB", "cuspDroppedCallsOneSec"),
        ("CISCO-USP-MIB", "cuspAvgDroppedCPSOneMin"),
        ("CISCO-USP-MIB", "cuspMaxDroppedCPSOneMin"),
        ("CISCO-USP-MIB", "cuspCallsRoutedOneSec"),
        ("CISCO-USP-MIB", "cuspAvgCallsRoutedOneMin"),
        ("CISCO-USP-MIB", "cuspMaxCallsRoutedOneMin"),
        ("CISCO-USP-MIB", "cuspCallsDroppedExceedingLicense"),
        ("CISCO-USP-MIB", "cuspSystemState"),
        ("CISCO-USP-MIB", "cuspSystemUpTime"),
        ("CISCO-USP-MIB", "cuspNoOfMessagesRecieved"),
        ("CISCO-USP-MIB", "cuspSmartAgentState"),
        ("CISCO-USP-MIB", "cuspStrayMessageCount"),
        ("CISCO-USP-MIB", "cuspConfiguredMemory"),
        ("CISCO-USP-MIB", "cuspMemoryUsed"),
        ("CISCO-USP-MIB", "cuspSystemStateAlertEnable"),
        ("CISCO-USP-MIB", "cuspServerGroupAlertEnable"),
        ("CISCO-USP-MIB", "cuspDiskSpaceThresholdAlertEnable"),
        ("CISCO-USP-MIB", "cuspBackupProcessFailAlertEnable"),
        ("CISCO-USP-MIB", "cuspExtensiveLoggingAlertEnable"),
        ("CISCO-USP-MIB", "cuspMemoryThresholdValue"),
        ("CISCO-USP-MIB", "cuspDiskSpaceThresholdValue"),
        ("CISCO-USP-MIB", "cuspServerGroupName"),
        ("CISCO-USP-MIB", "cuspServerGroupNetwork"),
        ("CISCO-USP-MIB", "cuspServerGroupStatus"),
        ("CISCO-USP-MIB", "cuspElementName"),
        ("CISCO-USP-MIB", "cuspElementStatus"),
        ("CISCO-USP-MIB", "cuspElementQValue"),
        ("CISCO-USP-MIB", "cuspElementWeight"),
        ("CISCO-USP-MIB", "cuspElementTransport"),
        ("CISCO-USP-MIB", "cuspElementTotalCalls"),
        ("CISCO-USP-MIB", "cuspElementFailedCalls"),
        ("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspNotifDetail"),
        ("CISCO-USP-MIB", "cuspLicenseExceededAlertEnable"),
        ("CISCO-USP-MIB", "cuspServerGroupPingStatus"),
        ("CISCO-USP-MIB", "cuspServerGroupLBType"),
        ("CISCO-USP-MIB", "cuspDiskSpaceUsed"),
        ("CISCO-USP-MIB", "cuspElementPort"),
        ("CISCO-USP-MIB", "cuspServerGroupElementAlertEnable"),
        ("CISCO-USP-MIB", "cuspLicenseStateAlertEnable"),
        ("CISCO-USP-MIB", "cuspMemoryThresholdAlertEnable"),
        ("CISCO-USP-MIB", "cuspConnectionExceptionAlertEnable"),
        ("CISCO-USP-MIB", "cuspLicenseState"))
)
if mibBuilder.loadTexts:
    ciscoUspMIBMainObjectGroup.setStatus("current")


# Notification objects

cuspSystemStateAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 1)
)
cuspSystemStateAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspNotifDetail"),
        ("CISCO-USP-MIB", "cuspSystemState"))
)
if mibBuilder.loadTexts:
    cuspSystemStateAlert.setStatus(
        "current"
    )

cuspServerGroupElementAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 2)
)
cuspServerGroupElementAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspElementName"),
        ("CISCO-USP-MIB", "cuspElementStatus"))
)
if mibBuilder.loadTexts:
    cuspServerGroupElementAlert.setStatus(
        "current"
    )

cuspServerGroupAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 3)
)
cuspServerGroupAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspServerGroupName"),
        ("CISCO-USP-MIB", "cuspServerGroupStatus"))
)
if mibBuilder.loadTexts:
    cuspServerGroupAlert.setStatus(
        "current"
    )

cuspMemoryThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 4)
)
cuspMemoryThresholdAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspMemoryThresholdValue"),
        ("CISCO-USP-MIB", "cuspConfiguredMemory"),
        ("CISCO-USP-MIB", "cuspMemoryUsed"))
)
if mibBuilder.loadTexts:
    cuspMemoryThresholdAlert.setStatus(
        "current"
    )

cuspLicenseExceededAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 5)
)
cuspLicenseExceededAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspCPS"),
        ("CISCO-USP-MIB", "cuspLicenseLimit"))
)
if mibBuilder.loadTexts:
    cuspLicenseExceededAlert.setStatus(
        "current"
    )

cuspLicenseStateAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 6)
)
cuspLicenseStateAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspLicenseState"))
)
if mibBuilder.loadTexts:
    cuspLicenseStateAlert.setStatus(
        "current"
    )

cuspExtensiveLoggingAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 7)
)
cuspExtensiveLoggingAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspNotifDetail"))
)
if mibBuilder.loadTexts:
    cuspExtensiveLoggingAlert.setStatus(
        "current"
    )

cuspDiskSpaceThresholdAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 8)
)
cuspDiskSpaceThresholdAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspDiskSpaceThresholdValue"),
        ("CISCO-USP-MIB", "cuspDiskSpaceUsed"))
)
if mibBuilder.loadTexts:
    cuspDiskSpaceThresholdAlert.setStatus(
        "current"
    )

cuspBackupProcessFailAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 9)
)
cuspBackupProcessFailAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspNotifDetail"))
)
if mibBuilder.loadTexts:
    cuspBackupProcessFailAlert.setStatus(
        "current"
    )

cuspConnectionExceptionAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 0, 10)
)
cuspConnectionExceptionAlert.setObjects(
      *(("CISCO-USP-MIB", "cuspNotifSeverity"),
        ("CISCO-USP-MIB", "cuspNotifDetail"))
)
if mibBuilder.loadTexts:
    cuspConnectionExceptionAlert.setStatus(
        "current"
    )


# Notifications groups

ciscoUspMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 2, 2)
)
ciscoUspMIBNotifyGroup.setObjects(
      *(("CISCO-USP-MIB", "cuspSystemStateAlert"),
        ("CISCO-USP-MIB", "cuspBackupProcessFailAlert"),
        ("CISCO-USP-MIB", "cuspDiskSpaceThresholdAlert"),
        ("CISCO-USP-MIB", "cuspConnectionExceptionAlert"),
        ("CISCO-USP-MIB", "cuspServerGroupElementAlert"),
        ("CISCO-USP-MIB", "cuspServerGroupAlert"),
        ("CISCO-USP-MIB", "cuspMemoryThresholdAlert"),
        ("CISCO-USP-MIB", "cuspLicenseExceededAlert"),
        ("CISCO-USP-MIB", "cuspExtensiveLoggingAlert"),
        ("CISCO-USP-MIB", "cuspLicenseStateAlert"))
)
if mibBuilder.loadTexts:
    ciscoUspMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoUspMIBModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 827, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoUspMIBModuleCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-USP-MIB",
    **{"ciscoUspMIB": ciscoUspMIB,
       "ciscoUspMIBNotifs": ciscoUspMIBNotifs,
       "cuspSystemStateAlert": cuspSystemStateAlert,
       "cuspServerGroupElementAlert": cuspServerGroupElementAlert,
       "cuspServerGroupAlert": cuspServerGroupAlert,
       "cuspMemoryThresholdAlert": cuspMemoryThresholdAlert,
       "cuspLicenseExceededAlert": cuspLicenseExceededAlert,
       "cuspLicenseStateAlert": cuspLicenseStateAlert,
       "cuspExtensiveLoggingAlert": cuspExtensiveLoggingAlert,
       "cuspDiskSpaceThresholdAlert": cuspDiskSpaceThresholdAlert,
       "cuspBackupProcessFailAlert": cuspBackupProcessFailAlert,
       "cuspConnectionExceptionAlert": cuspConnectionExceptionAlert,
       "ciscoUspMIBObjects": ciscoUspMIBObjects,
       "cuspScalar": cuspScalar,
       "cuspLastCounterResetTime": cuspLastCounterResetTime,
       "cuspSystemState": cuspSystemState,
       "cuspSystemUpTime": cuspSystemUpTime,
       "cuspLicenseLimit": cuspLicenseLimit,
       "cuspLicenseState": cuspLicenseState,
       "cuspSmartAgentState": cuspSmartAgentState,
       "cuspConfiguredMemory": cuspConfiguredMemory,
       "cuspMemoryUsed": cuspMemoryUsed,
       "cuspDiskSpaceUsed": cuspDiskSpaceUsed,
       "cuspCallStats": cuspCallStats,
       "cuspTotalCalls": cuspTotalCalls,
       "cuspTotalFailedCalls": cuspTotalFailedCalls,
       "cuspCPS": cuspCPS,
       "cuspAvgCPSOneMin": cuspAvgCPSOneMin,
       "cuspMaxCPSOneMin": cuspMaxCPSOneMin,
       "cuspDroppedCallsOneSec": cuspDroppedCallsOneSec,
       "cuspAvgDroppedCPSOneMin": cuspAvgDroppedCPSOneMin,
       "cuspMaxDroppedCPSOneMin": cuspMaxDroppedCPSOneMin,
       "cuspCallsRoutedOneSec": cuspCallsRoutedOneSec,
       "cuspAvgCallsRoutedOneMin": cuspAvgCallsRoutedOneMin,
       "cuspMaxCallsRoutedOneMin": cuspMaxCallsRoutedOneMin,
       "cuspCallsDroppedExceedingLicense": cuspCallsDroppedExceedingLicense,
       "cuspMessageStats": cuspMessageStats,
       "cuspStrayMessageCount": cuspStrayMessageCount,
       "cuspNoOfMessagesRecieved": cuspNoOfMessagesRecieved,
       "cuspThresholdValues": cuspThresholdValues,
       "cuspDiskSpaceThresholdValue": cuspDiskSpaceThresholdValue,
       "cuspMemoryThresholdValue": cuspMemoryThresholdValue,
       "cuspTable": cuspTable,
       "cuspServerGroupTable": cuspServerGroupTable,
       "cuspServerGroupEntry": cuspServerGroupEntry,
       "cuspServerGroupIndex": cuspServerGroupIndex,
       "cuspServerGroupName": cuspServerGroupName,
       "cuspServerGroupNetwork": cuspServerGroupNetwork,
       "cuspServerGroupStatus": cuspServerGroupStatus,
       "cuspServerGroupPingStatus": cuspServerGroupPingStatus,
       "cuspServerGroupLBType": cuspServerGroupLBType,
       "cuspElementTable": cuspElementTable,
       "cuspElementEntry": cuspElementEntry,
       "cuspElementIndex": cuspElementIndex,
       "cuspElementName": cuspElementName,
       "cuspElementStatus": cuspElementStatus,
       "cuspElementQValue": cuspElementQValue,
       "cuspElementWeight": cuspElementWeight,
       "cuspElementPort": cuspElementPort,
       "cuspElementTransport": cuspElementTransport,
       "cuspElementTotalCalls": cuspElementTotalCalls,
       "cuspElementFailedCalls": cuspElementFailedCalls,
       "cuspNotifControlInfo": cuspNotifControlInfo,
       "cuspNotifSeverity": cuspNotifSeverity,
       "cuspNotifDetail": cuspNotifDetail,
       "cuspSystemStateAlertEnable": cuspSystemStateAlertEnable,
       "cuspServerGroupAlertEnable": cuspServerGroupAlertEnable,
       "cuspServerGroupElementAlertEnable": cuspServerGroupElementAlertEnable,
       "cuspLicenseExceededAlertEnable": cuspLicenseExceededAlertEnable,
       "cuspLicenseStateAlertEnable": cuspLicenseStateAlertEnable,
       "cuspExtensiveLoggingAlertEnable": cuspExtensiveLoggingAlertEnable,
       "cuspDiskSpaceThresholdAlertEnable": cuspDiskSpaceThresholdAlertEnable,
       "cuspMemoryThresholdAlertEnable": cuspMemoryThresholdAlertEnable,
       "cuspBackupProcessFailAlertEnable": cuspBackupProcessFailAlertEnable,
       "cuspConnectionExceptionAlertEnable": cuspConnectionExceptionAlertEnable,
       "ciscoUspMIBConform": ciscoUspMIBConform,
       "ciscoUspMIBCompliances": ciscoUspMIBCompliances,
       "ciscoUspMIBModuleCompliance": ciscoUspMIBModuleCompliance,
       "ciscoUspMIBGroups": ciscoUspMIBGroups,
       "ciscoUspMIBMainObjectGroup": ciscoUspMIBMainObjectGroup,
       "ciscoUspMIBNotifyGroup": ciscoUspMIBNotifyGroup}
)
