# SNMP MIB module (CISCO-ISDN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ISDN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:09 2024
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

(isdnLapdOperStatus,
 isdnSignalingIfIndex,
 isdnSignalingIndex) = mibBuilder.importSymbols(
    "ISDN-MIB",
    "isdnLapdOperStatus",
    "isdnSignalingIfIndex",
    "isdnSignalingIndex")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

ciscoIsdnMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26)
)
ciscoIsdnMib.setRevisions(
        ("2001-02-09 00:00",
         "2000-03-27 00:00",
         "2000-02-23 00:00",
         "1999-05-07 00:00",
         "1996-02-21 00:00",
         "1995-08-15 00:00",
         "1995-01-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIsdnMibObjects_ObjectIdentity = ObjectIdentity
ciscoIsdnMibObjects = _CiscoIsdnMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1)
)
_IsdnNeighbor_ObjectIdentity = ObjectIdentity
isdnNeighbor = _IsdnNeighbor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1)
)
_DemandNbrTable_Object = MibTable
demandNbrTable = _DemandNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    demandNbrTable.setStatus("current")
_DemandNbrEntry_Object = MibTableRow
demandNbrEntry = _DemandNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1)
)
demandNbrEntry.setIndexNames(
    (0, "CISCO-ISDN-MIB", "demandNbrPhysIf"),
    (0, "CISCO-ISDN-MIB", "demandNbrId"),
)
if mibBuilder.loadTexts:
    demandNbrEntry.setStatus("current")


class _DemandNbrPhysIf_Type(Integer32):
    """Custom type demandNbrPhysIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DemandNbrPhysIf_Type.__name__ = "Integer32"
_DemandNbrPhysIf_Object = MibTableColumn
demandNbrPhysIf = _DemandNbrPhysIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 1),
    _DemandNbrPhysIf_Type()
)
demandNbrPhysIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    demandNbrPhysIf.setStatus("current")


class _DemandNbrId_Type(Integer32):
    """Custom type demandNbrId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DemandNbrId_Type.__name__ = "Integer32"
_DemandNbrId_Object = MibTableColumn
demandNbrId = _DemandNbrId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 2),
    _DemandNbrId_Type()
)
demandNbrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    demandNbrId.setStatus("current")


class _DemandNbrLogIf_Type(Integer32):
    """Custom type demandNbrLogIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DemandNbrLogIf_Type.__name__ = "Integer32"
_DemandNbrLogIf_Object = MibTableColumn
demandNbrLogIf = _DemandNbrLogIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 3),
    _DemandNbrLogIf_Type()
)
demandNbrLogIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    demandNbrLogIf.setStatus("current")
_DemandNbrName_Type = DisplayString
_DemandNbrName_Object = MibTableColumn
demandNbrName = _DemandNbrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 4),
    _DemandNbrName_Type()
)
demandNbrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    demandNbrName.setStatus("current")
_DemandNbrAddress_Type = DisplayString
_DemandNbrAddress_Object = MibTableColumn
demandNbrAddress = _DemandNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 5),
    _DemandNbrAddress_Type()
)
demandNbrAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    demandNbrAddress.setStatus("current")


class _DemandNbrPermission_Type(Integer32):
    """Custom type demandNbrPermission based on Integer32"""
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
        *(("heCanCallMe", 2),
          ("iCanCallHim", 1),
          ("weCanCallEachOther", 3))
    )


_DemandNbrPermission_Type.__name__ = "Integer32"
_DemandNbrPermission_Object = MibTableColumn
demandNbrPermission = _DemandNbrPermission_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 6),
    _DemandNbrPermission_Type()
)
demandNbrPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    demandNbrPermission.setStatus("current")


class _DemandNbrMaxDuration_Type(Integer32):
    """Custom type demandNbrMaxDuration based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DemandNbrMaxDuration_Type.__name__ = "Integer32"
_DemandNbrMaxDuration_Object = MibTableColumn
demandNbrMaxDuration = _DemandNbrMaxDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 7),
    _DemandNbrMaxDuration_Type()
)
demandNbrMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    demandNbrMaxDuration.setStatus("current")
if mibBuilder.loadTexts:
    demandNbrMaxDuration.setUnits("seconds")


class _DemandNbrLastDuration_Type(Integer32):
    """Custom type demandNbrLastDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DemandNbrLastDuration_Type.__name__ = "Integer32"
_DemandNbrLastDuration_Object = MibTableColumn
demandNbrLastDuration = _DemandNbrLastDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 8),
    _DemandNbrLastDuration_Type()
)
demandNbrLastDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrLastDuration.setStatus("current")
if mibBuilder.loadTexts:
    demandNbrLastDuration.setUnits("seconds")
_DemandNbrClearReason_Type = DisplayString
_DemandNbrClearReason_Object = MibTableColumn
demandNbrClearReason = _DemandNbrClearReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 9),
    _DemandNbrClearReason_Type()
)
demandNbrClearReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrClearReason.setStatus("current")
_DemandNbrClearCode_Type = OctetString
_DemandNbrClearCode_Object = MibTableColumn
demandNbrClearCode = _DemandNbrClearCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 10),
    _DemandNbrClearCode_Type()
)
demandNbrClearCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrClearCode.setStatus("current")
_DemandNbrSuccessCalls_Type = Counter32
_DemandNbrSuccessCalls_Object = MibTableColumn
demandNbrSuccessCalls = _DemandNbrSuccessCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 11),
    _DemandNbrSuccessCalls_Type()
)
demandNbrSuccessCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrSuccessCalls.setStatus("current")
_DemandNbrFailCalls_Type = Counter32
_DemandNbrFailCalls_Object = MibTableColumn
demandNbrFailCalls = _DemandNbrFailCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 12),
    _DemandNbrFailCalls_Type()
)
demandNbrFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrFailCalls.setStatus("current")
_DemandNbrAcceptCalls_Type = Counter32
_DemandNbrAcceptCalls_Object = MibTableColumn
demandNbrAcceptCalls = _DemandNbrAcceptCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 13),
    _DemandNbrAcceptCalls_Type()
)
demandNbrAcceptCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrAcceptCalls.setStatus("current")
_DemandNbrRefuseCalls_Type = Counter32
_DemandNbrRefuseCalls_Object = MibTableColumn
demandNbrRefuseCalls = _DemandNbrRefuseCalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 14),
    _DemandNbrRefuseCalls_Type()
)
demandNbrRefuseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrRefuseCalls.setStatus("current")
_DemandNbrLastAttemptTime_Type = TimeStamp
_DemandNbrLastAttemptTime_Object = MibTableColumn
demandNbrLastAttemptTime = _DemandNbrLastAttemptTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 15),
    _DemandNbrLastAttemptTime_Type()
)
demandNbrLastAttemptTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrLastAttemptTime.setStatus("current")
_DemandNbrStatus_Type = RowStatus
_DemandNbrStatus_Object = MibTableColumn
demandNbrStatus = _DemandNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 16),
    _DemandNbrStatus_Type()
)
demandNbrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    demandNbrStatus.setStatus("current")


class _DemandNbrCallOrigin_Type(Integer32):
    """Custom type demandNbrCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("callback", 3),
          ("originate", 1))
    )


_DemandNbrCallOrigin_Type.__name__ = "Integer32"
_DemandNbrCallOrigin_Object = MibTableColumn
demandNbrCallOrigin = _DemandNbrCallOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 1, 1, 1, 1, 17),
    _DemandNbrCallOrigin_Type()
)
demandNbrCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandNbrCallOrigin.setStatus("current")
_CiscoIsdnMibTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoIsdnMibTrapPrefix = _CiscoIsdnMibTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 2)
)
_CiscoIsdnMibTraps_ObjectIdentity = ObjectIdentity
ciscoIsdnMibTraps = _CiscoIsdnMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0)
)
_CiscoIsdnMibConformance_ObjectIdentity = ObjectIdentity
ciscoIsdnMibConformance = _CiscoIsdnMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 3)
)
_CiscoIsdnMibCompliances_ObjectIdentity = ObjectIdentity
ciscoIsdnMibCompliances = _CiscoIsdnMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 1)
)
_CiscoIsdnMibGroups_ObjectIdentity = ObjectIdentity
ciscoIsdnMibGroups = _CiscoIsdnMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 2)
)

# Managed Objects groups

ciscoIsdnMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 2, 1)
)
ciscoIsdnMibGroup.setObjects(
      *(("CISCO-ISDN-MIB", "demandNbrLogIf"),
        ("CISCO-ISDN-MIB", "demandNbrName"),
        ("CISCO-ISDN-MIB", "demandNbrAddress"),
        ("CISCO-ISDN-MIB", "demandNbrPermission"),
        ("CISCO-ISDN-MIB", "demandNbrMaxDuration"),
        ("CISCO-ISDN-MIB", "demandNbrLastDuration"),
        ("CISCO-ISDN-MIB", "demandNbrClearReason"),
        ("CISCO-ISDN-MIB", "demandNbrClearCode"),
        ("CISCO-ISDN-MIB", "demandNbrSuccessCalls"),
        ("CISCO-ISDN-MIB", "demandNbrFailCalls"),
        ("CISCO-ISDN-MIB", "demandNbrAcceptCalls"),
        ("CISCO-ISDN-MIB", "demandNbrRefuseCalls"),
        ("CISCO-ISDN-MIB", "demandNbrLastAttemptTime"),
        ("CISCO-ISDN-MIB", "demandNbrStatus"))
)
if mibBuilder.loadTexts:
    ciscoIsdnMibGroup.setStatus("current")

ciscoIsdnMibGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 2, 2)
)
ciscoIsdnMibGroupRev1.setObjects(
      *(("CISCO-ISDN-MIB", "demandNbrLogIf"),
        ("CISCO-ISDN-MIB", "demandNbrName"),
        ("CISCO-ISDN-MIB", "demandNbrAddress"),
        ("CISCO-ISDN-MIB", "demandNbrPermission"),
        ("CISCO-ISDN-MIB", "demandNbrMaxDuration"),
        ("CISCO-ISDN-MIB", "demandNbrLastDuration"),
        ("CISCO-ISDN-MIB", "demandNbrClearReason"),
        ("CISCO-ISDN-MIB", "demandNbrClearCode"),
        ("CISCO-ISDN-MIB", "demandNbrSuccessCalls"),
        ("CISCO-ISDN-MIB", "demandNbrFailCalls"),
        ("CISCO-ISDN-MIB", "demandNbrAcceptCalls"),
        ("CISCO-ISDN-MIB", "demandNbrRefuseCalls"),
        ("CISCO-ISDN-MIB", "demandNbrLastAttemptTime"),
        ("CISCO-ISDN-MIB", "demandNbrStatus"),
        ("CISCO-ISDN-MIB", "demandNbrCallOrigin"))
)
if mibBuilder.loadTexts:
    ciscoIsdnMibGroupRev1.setStatus("current")


# Notification objects

demandNbrCallInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0, 1)
)
demandNbrCallInformation.setObjects(
      *(("CISCO-ISDN-MIB", "demandNbrLogIf"),
        ("CISCO-ISDN-MIB", "demandNbrName"),
        ("CISCO-ISDN-MIB", "demandNbrAddress"),
        ("CISCO-ISDN-MIB", "demandNbrLastDuration"),
        ("CISCO-ISDN-MIB", "demandNbrClearReason"),
        ("CISCO-ISDN-MIB", "demandNbrClearCode"))
)
if mibBuilder.loadTexts:
    demandNbrCallInformation.setStatus(
        "obsolete"
    )

demandNbrCallDetails = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0, 2)
)
demandNbrCallDetails.setObjects(
      *(("CISCO-ISDN-MIB", "demandNbrLogIf"),
        ("CISCO-ISDN-MIB", "demandNbrName"),
        ("CISCO-ISDN-MIB", "demandNbrAddress"),
        ("CISCO-ISDN-MIB", "demandNbrLastDuration"),
        ("CISCO-ISDN-MIB", "demandNbrClearReason"),
        ("CISCO-ISDN-MIB", "demandNbrClearCode"),
        ("CISCO-ISDN-MIB", "demandNbrCallOrigin"))
)
if mibBuilder.loadTexts:
    demandNbrCallDetails.setStatus(
        "current"
    )

demandNbrLayer2Change = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0, 3)
)
demandNbrLayer2Change.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ISDN-MIB", "isdnLapdOperStatus"))
)
if mibBuilder.loadTexts:
    demandNbrLayer2Change.setStatus(
        "current"
    )

demandNbrCNANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 2, 0, 4)
)
demandNbrCNANotification.setObjects(
      *(("ISDN-MIB", "isdnSignalingIfIndex"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    demandNbrCNANotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIsdnMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIsdnMibCompliance.setStatus(
        "current"
    )

ciscoIsdnMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 26, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIsdnMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ISDN-MIB",
    **{"ciscoIsdnMib": ciscoIsdnMib,
       "ciscoIsdnMibObjects": ciscoIsdnMibObjects,
       "isdnNeighbor": isdnNeighbor,
       "demandNbrTable": demandNbrTable,
       "demandNbrEntry": demandNbrEntry,
       "demandNbrPhysIf": demandNbrPhysIf,
       "demandNbrId": demandNbrId,
       "demandNbrLogIf": demandNbrLogIf,
       "demandNbrName": demandNbrName,
       "demandNbrAddress": demandNbrAddress,
       "demandNbrPermission": demandNbrPermission,
       "demandNbrMaxDuration": demandNbrMaxDuration,
       "demandNbrLastDuration": demandNbrLastDuration,
       "demandNbrClearReason": demandNbrClearReason,
       "demandNbrClearCode": demandNbrClearCode,
       "demandNbrSuccessCalls": demandNbrSuccessCalls,
       "demandNbrFailCalls": demandNbrFailCalls,
       "demandNbrAcceptCalls": demandNbrAcceptCalls,
       "demandNbrRefuseCalls": demandNbrRefuseCalls,
       "demandNbrLastAttemptTime": demandNbrLastAttemptTime,
       "demandNbrStatus": demandNbrStatus,
       "demandNbrCallOrigin": demandNbrCallOrigin,
       "ciscoIsdnMibTrapPrefix": ciscoIsdnMibTrapPrefix,
       "ciscoIsdnMibTraps": ciscoIsdnMibTraps,
       "demandNbrCallInformation": demandNbrCallInformation,
       "demandNbrCallDetails": demandNbrCallDetails,
       "demandNbrLayer2Change": demandNbrLayer2Change,
       "demandNbrCNANotification": demandNbrCNANotification,
       "ciscoIsdnMibConformance": ciscoIsdnMibConformance,
       "ciscoIsdnMibCompliances": ciscoIsdnMibCompliances,
       "ciscoIsdnMibCompliance": ciscoIsdnMibCompliance,
       "ciscoIsdnMibComplianceRev1": ciscoIsdnMibComplianceRev1,
       "ciscoIsdnMibGroups": ciscoIsdnMibGroups,
       "ciscoIsdnMibGroup": ciscoIsdnMibGroup,
       "ciscoIsdnMibGroupRev1": ciscoIsdnMibGroupRev1}
)
