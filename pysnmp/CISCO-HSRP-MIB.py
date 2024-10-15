# SNMP MIB module (CISCO-HSRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-HSRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoHsrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106)
)
ciscoHsrpMIB.setRevisions(
        ("2010-09-06 00:00",
         "2005-12-20 00:00",
         "1998-08-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HsrpState(Integer32, TextualConvention):
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
        *(("active", 6),
          ("initial", 1),
          ("learn", 2),
          ("listen", 3),
          ("speak", 4),
          ("standby", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoHsrpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoHsrpMIBObjects = _CiscoHsrpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1)
)
_CHsrpGlobalConfig_ObjectIdentity = ObjectIdentity
cHsrpGlobalConfig = _CHsrpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 1)
)


class _CHsrpConfigTimeout_Type(Unsigned32):
    """Custom type cHsrpConfigTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CHsrpConfigTimeout_Type.__name__ = "Unsigned32"
_CHsrpConfigTimeout_Object = MibScalar
cHsrpConfigTimeout = _CHsrpConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 1, 1),
    _CHsrpConfigTimeout_Type()
)
cHsrpConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cHsrpConfigTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cHsrpConfigTimeout.setUnits("minutes")
_CHsrpGroup_ObjectIdentity = ObjectIdentity
cHsrpGroup = _CHsrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2)
)
_CHsrpGrpTable_Object = MibTable
cHsrpGrpTable = _CHsrpGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cHsrpGrpTable.setStatus("current")
_CHsrpGrpEntry_Object = MibTableRow
cHsrpGrpEntry = _CHsrpGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1)
)
cHsrpGrpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-HSRP-MIB", "cHsrpGrpNumber"),
)
if mibBuilder.loadTexts:
    cHsrpGrpEntry.setStatus("current")


class _CHsrpGrpNumber_Type(Unsigned32):
    """Custom type cHsrpGrpNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CHsrpGrpNumber_Type.__name__ = "Unsigned32"
_CHsrpGrpNumber_Object = MibTableColumn
cHsrpGrpNumber = _CHsrpGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 1),
    _CHsrpGrpNumber_Type()
)
cHsrpGrpNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHsrpGrpNumber.setStatus("current")


class _CHsrpGrpAuth_Type(DisplayString):
    """Custom type cHsrpGrpAuth based on DisplayString"""
    defaultValue = OctetString("cisco")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CHsrpGrpAuth_Type.__name__ = "DisplayString"
_CHsrpGrpAuth_Object = MibTableColumn
cHsrpGrpAuth = _CHsrpGrpAuth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 2),
    _CHsrpGrpAuth_Type()
)
cHsrpGrpAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpAuth.setStatus("current")


class _CHsrpGrpPriority_Type(Unsigned32):
    """Custom type cHsrpGrpPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CHsrpGrpPriority_Type.__name__ = "Unsigned32"
_CHsrpGrpPriority_Object = MibTableColumn
cHsrpGrpPriority = _CHsrpGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 3),
    _CHsrpGrpPriority_Type()
)
cHsrpGrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpPriority.setStatus("current")


class _CHsrpGrpPreempt_Type(TruthValue):
    """Custom type cHsrpGrpPreempt based on TruthValue"""


_CHsrpGrpPreempt_Object = MibTableColumn
cHsrpGrpPreempt = _CHsrpGrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 4),
    _CHsrpGrpPreempt_Type()
)
cHsrpGrpPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpPreempt.setStatus("current")


class _CHsrpGrpPreemptDelay_Type(Unsigned32):
    """Custom type cHsrpGrpPreemptDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CHsrpGrpPreemptDelay_Type.__name__ = "Unsigned32"
_CHsrpGrpPreemptDelay_Object = MibTableColumn
cHsrpGrpPreemptDelay = _CHsrpGrpPreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 5),
    _CHsrpGrpPreemptDelay_Type()
)
cHsrpGrpPreemptDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpPreemptDelay.setStatus("current")
if mibBuilder.loadTexts:
    cHsrpGrpPreemptDelay.setUnits("seconds")
_CHsrpGrpUseConfiguredTimers_Type = TruthValue
_CHsrpGrpUseConfiguredTimers_Object = MibTableColumn
cHsrpGrpUseConfiguredTimers = _CHsrpGrpUseConfiguredTimers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 6),
    _CHsrpGrpUseConfiguredTimers_Type()
)
cHsrpGrpUseConfiguredTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpUseConfiguredTimers.setStatus("current")


class _CHsrpGrpConfiguredHelloTime_Type(Unsigned32):
    """Custom type cHsrpGrpConfiguredHelloTime based on Unsigned32"""
    defaultValue = 3000


_CHsrpGrpConfiguredHelloTime_Object = MibTableColumn
cHsrpGrpConfiguredHelloTime = _CHsrpGrpConfiguredHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 7),
    _CHsrpGrpConfiguredHelloTime_Type()
)
cHsrpGrpConfiguredHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpConfiguredHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    cHsrpGrpConfiguredHelloTime.setUnits("milliseconds")


class _CHsrpGrpConfiguredHoldTime_Type(Unsigned32):
    """Custom type cHsrpGrpConfiguredHoldTime based on Unsigned32"""
    defaultValue = 10000


_CHsrpGrpConfiguredHoldTime_Object = MibTableColumn
cHsrpGrpConfiguredHoldTime = _CHsrpGrpConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 8),
    _CHsrpGrpConfiguredHoldTime_Type()
)
cHsrpGrpConfiguredHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpConfiguredHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cHsrpGrpConfiguredHoldTime.setUnits("milliseconds")


class _CHsrpGrpLearnedHelloTime_Type(Unsigned32):
    """Custom type cHsrpGrpLearnedHelloTime based on Unsigned32"""
    defaultValue = 3000


_CHsrpGrpLearnedHelloTime_Object = MibTableColumn
cHsrpGrpLearnedHelloTime = _CHsrpGrpLearnedHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 9),
    _CHsrpGrpLearnedHelloTime_Type()
)
cHsrpGrpLearnedHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpLearnedHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    cHsrpGrpLearnedHelloTime.setUnits("milliseconds")


class _CHsrpGrpLearnedHoldTime_Type(Unsigned32):
    """Custom type cHsrpGrpLearnedHoldTime based on Unsigned32"""
    defaultValue = 10000


_CHsrpGrpLearnedHoldTime_Object = MibTableColumn
cHsrpGrpLearnedHoldTime = _CHsrpGrpLearnedHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 10),
    _CHsrpGrpLearnedHoldTime_Type()
)
cHsrpGrpLearnedHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpLearnedHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cHsrpGrpLearnedHoldTime.setUnits("milliseconds")


class _CHsrpGrpVirtualIpAddr_Type(IpAddress):
    """Custom type cHsrpGrpVirtualIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CHsrpGrpVirtualIpAddr_Object = MibTableColumn
cHsrpGrpVirtualIpAddr = _CHsrpGrpVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 11),
    _CHsrpGrpVirtualIpAddr_Type()
)
cHsrpGrpVirtualIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpVirtualIpAddr.setStatus("current")
_CHsrpGrpUseConfigVirtualIpAddr_Type = TruthValue
_CHsrpGrpUseConfigVirtualIpAddr_Object = MibTableColumn
cHsrpGrpUseConfigVirtualIpAddr = _CHsrpGrpUseConfigVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 12),
    _CHsrpGrpUseConfigVirtualIpAddr_Type()
)
cHsrpGrpUseConfigVirtualIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpUseConfigVirtualIpAddr.setStatus("current")
_CHsrpGrpActiveRouter_Type = IpAddress
_CHsrpGrpActiveRouter_Object = MibTableColumn
cHsrpGrpActiveRouter = _CHsrpGrpActiveRouter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 13),
    _CHsrpGrpActiveRouter_Type()
)
cHsrpGrpActiveRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpActiveRouter.setStatus("current")
_CHsrpGrpStandbyRouter_Type = IpAddress
_CHsrpGrpStandbyRouter_Object = MibTableColumn
cHsrpGrpStandbyRouter = _CHsrpGrpStandbyRouter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 14),
    _CHsrpGrpStandbyRouter_Type()
)
cHsrpGrpStandbyRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpStandbyRouter.setStatus("current")
_CHsrpGrpStandbyState_Type = HsrpState
_CHsrpGrpStandbyState_Object = MibTableColumn
cHsrpGrpStandbyState = _CHsrpGrpStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 15),
    _CHsrpGrpStandbyState_Type()
)
cHsrpGrpStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpStandbyState.setStatus("current")
_CHsrpGrpVirtualMacAddr_Type = MacAddress
_CHsrpGrpVirtualMacAddr_Object = MibTableColumn
cHsrpGrpVirtualMacAddr = _CHsrpGrpVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 16),
    _CHsrpGrpVirtualMacAddr_Type()
)
cHsrpGrpVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpVirtualMacAddr.setStatus("current")
_CHsrpGrpEntryRowStatus_Type = RowStatus
_CHsrpGrpEntryRowStatus_Object = MibTableColumn
cHsrpGrpEntryRowStatus = _CHsrpGrpEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 17),
    _CHsrpGrpEntryRowStatus_Type()
)
cHsrpGrpEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpEntryRowStatus.setStatus("current")


class _CHsrpGrpIpNone_Type(TruthValue):
    """Custom type cHsrpGrpIpNone based on TruthValue"""


_CHsrpGrpIpNone_Object = MibTableColumn
cHsrpGrpIpNone = _CHsrpGrpIpNone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 1, 2, 1, 1, 18),
    _CHsrpGrpIpNone_Type()
)
cHsrpGrpIpNone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpIpNone.setStatus("current")
_CHsrpMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cHsrpMIBNotificationPrefix = _CHsrpMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 2)
)
_CHsrpMIBNotifications_ObjectIdentity = ObjectIdentity
cHsrpMIBNotifications = _CHsrpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 2, 0)
)
_CHsrpConformance_ObjectIdentity = ObjectIdentity
cHsrpConformance = _CHsrpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3)
)
_CHsrpCompliances_ObjectIdentity = ObjectIdentity
cHsrpCompliances = _CHsrpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1)
)
_CHsrpComplianceGroups_ObjectIdentity = ObjectIdentity
cHsrpComplianceGroups = _CHsrpComplianceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2)
)

# Managed Objects groups

cHsrpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 1)
)
cHsrpConfigGroup.setObjects(
    ("CISCO-HSRP-MIB", "cHsrpConfigTimeout")
)
if mibBuilder.loadTexts:
    cHsrpConfigGroup.setStatus("current")

cHsrpGrpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 2)
)
cHsrpGrpGroup.setObjects(
      *(("CISCO-HSRP-MIB", "cHsrpGrpAuth"),
        ("CISCO-HSRP-MIB", "cHsrpGrpPriority"),
        ("CISCO-HSRP-MIB", "cHsrpGrpPreempt"),
        ("CISCO-HSRP-MIB", "cHsrpGrpPreemptDelay"),
        ("CISCO-HSRP-MIB", "cHsrpGrpUseConfiguredTimers"),
        ("CISCO-HSRP-MIB", "cHsrpGrpConfiguredHelloTime"),
        ("CISCO-HSRP-MIB", "cHsrpGrpConfiguredHoldTime"),
        ("CISCO-HSRP-MIB", "cHsrpGrpLearnedHelloTime"),
        ("CISCO-HSRP-MIB", "cHsrpGrpLearnedHoldTime"),
        ("CISCO-HSRP-MIB", "cHsrpGrpVirtualIpAddr"),
        ("CISCO-HSRP-MIB", "cHsrpGrpUseConfigVirtualIpAddr"),
        ("CISCO-HSRP-MIB", "cHsrpGrpActiveRouter"),
        ("CISCO-HSRP-MIB", "cHsrpGrpStandbyRouter"),
        ("CISCO-HSRP-MIB", "cHsrpGrpStandbyState"),
        ("CISCO-HSRP-MIB", "cHsrpGrpVirtualMacAddr"),
        ("CISCO-HSRP-MIB", "cHsrpGrpEntryRowStatus"))
)
if mibBuilder.loadTexts:
    cHsrpGrpGroup.setStatus("current")

cHsrpGrpGroupSup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 4)
)
cHsrpGrpGroupSup.setObjects(
    ("CISCO-HSRP-MIB", "cHsrpGrpIpNone")
)
if mibBuilder.loadTexts:
    cHsrpGrpGroupSup.setStatus("current")


# Notification objects

cHsrpStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 2, 0, 1)
)
cHsrpStateChange.setObjects(
    ("CISCO-HSRP-MIB", "cHsrpGrpStandbyState")
)
if mibBuilder.loadTexts:
    cHsrpStateChange.setStatus(
        "current"
    )


# Notifications groups

cHsrpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 2, 3)
)
cHsrpNotificationsGroup.setObjects(
    ("CISCO-HSRP-MIB", "cHsrpStateChange")
)
if mibBuilder.loadTexts:
    cHsrpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cHsrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cHsrpCompliance.setStatus(
        "deprecated"
    )

cHsrpComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cHsrpComplianceRev1.setStatus(
        "deprecated"
    )

cHsrpComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 106, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cHsrpComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-HSRP-MIB",
    **{"HsrpState": HsrpState,
       "ciscoHsrpMIB": ciscoHsrpMIB,
       "ciscoHsrpMIBObjects": ciscoHsrpMIBObjects,
       "cHsrpGlobalConfig": cHsrpGlobalConfig,
       "cHsrpConfigTimeout": cHsrpConfigTimeout,
       "cHsrpGroup": cHsrpGroup,
       "cHsrpGrpTable": cHsrpGrpTable,
       "cHsrpGrpEntry": cHsrpGrpEntry,
       "cHsrpGrpNumber": cHsrpGrpNumber,
       "cHsrpGrpAuth": cHsrpGrpAuth,
       "cHsrpGrpPriority": cHsrpGrpPriority,
       "cHsrpGrpPreempt": cHsrpGrpPreempt,
       "cHsrpGrpPreemptDelay": cHsrpGrpPreemptDelay,
       "cHsrpGrpUseConfiguredTimers": cHsrpGrpUseConfiguredTimers,
       "cHsrpGrpConfiguredHelloTime": cHsrpGrpConfiguredHelloTime,
       "cHsrpGrpConfiguredHoldTime": cHsrpGrpConfiguredHoldTime,
       "cHsrpGrpLearnedHelloTime": cHsrpGrpLearnedHelloTime,
       "cHsrpGrpLearnedHoldTime": cHsrpGrpLearnedHoldTime,
       "cHsrpGrpVirtualIpAddr": cHsrpGrpVirtualIpAddr,
       "cHsrpGrpUseConfigVirtualIpAddr": cHsrpGrpUseConfigVirtualIpAddr,
       "cHsrpGrpActiveRouter": cHsrpGrpActiveRouter,
       "cHsrpGrpStandbyRouter": cHsrpGrpStandbyRouter,
       "cHsrpGrpStandbyState": cHsrpGrpStandbyState,
       "cHsrpGrpVirtualMacAddr": cHsrpGrpVirtualMacAddr,
       "cHsrpGrpEntryRowStatus": cHsrpGrpEntryRowStatus,
       "cHsrpGrpIpNone": cHsrpGrpIpNone,
       "cHsrpMIBNotificationPrefix": cHsrpMIBNotificationPrefix,
       "cHsrpMIBNotifications": cHsrpMIBNotifications,
       "cHsrpStateChange": cHsrpStateChange,
       "cHsrpConformance": cHsrpConformance,
       "cHsrpCompliances": cHsrpCompliances,
       "cHsrpCompliance": cHsrpCompliance,
       "cHsrpComplianceRev1": cHsrpComplianceRev1,
       "cHsrpComplianceRev2": cHsrpComplianceRev2,
       "cHsrpComplianceGroups": cHsrpComplianceGroups,
       "cHsrpConfigGroup": cHsrpConfigGroup,
       "cHsrpGrpGroup": cHsrpGrpGroup,
       "cHsrpNotificationsGroup": cHsrpNotificationsGroup,
       "cHsrpGrpGroupSup": cHsrpGrpGroupSup}
)
