# SNMP MIB module (CIENA-CES-ICL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-ICL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:58 2024
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

(cienaGlobalMacAddress,
 cienaGlobalSeverity) = mibBuilder.importSymbols(
    "CIENA-GLOBAL-MIB",
    "cienaGlobalMacAddress",
    "cienaGlobalSeverity")

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,
 CienaMacAddress,
 CienaStatsClear) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState",
    "CienaMacAddress",
    "CienaStatsClear")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

cienaCesIclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32)
)
cienaCesIclMIB.setRevisions(
        ("2013-11-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesIclMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesIclMIBObjects = _CienaCesIclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1)
)
_CienaCesIcl_ObjectIdentity = ObjectIdentity
cienaCesIcl = _CienaCesIcl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1)
)
_CienaCesIclTable_Object = MibTable
cienaCesIclTable = _CienaCesIclTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cienaCesIclTable.setStatus("current")
_CienaCesIclEntry_Object = MibTableRow
cienaCesIclEntry = _CienaCesIclEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1)
)
cienaCesIclEntry.setIndexNames(
    (0, "CIENA-CES-ICL-MIB", "cienaCesIclIndex"),
)
if mibBuilder.loadTexts:
    cienaCesIclEntry.setStatus("current")


class _CienaCesIclIndex_Type(Unsigned32):
    """Custom type cienaCesIclIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 47),
    )


_CienaCesIclIndex_Type.__name__ = "Unsigned32"
_CienaCesIclIndex_Object = MibTableColumn
cienaCesIclIndex = _CienaCesIclIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 1),
    _CienaCesIclIndex_Type()
)
cienaCesIclIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclIndex.setStatus("current")
_CienaCesIclName_Type = DisplayString
_CienaCesIclName_Object = MibTableColumn
cienaCesIclName = _CienaCesIclName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 2),
    _CienaCesIclName_Type()
)
cienaCesIclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclName.setStatus("current")
_CienaCesIclRemoteMacAddress_Type = MacAddress
_CienaCesIclRemoteMacAddress_Object = MibTableColumn
cienaCesIclRemoteMacAddress = _CienaCesIclRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 3),
    _CienaCesIclRemoteMacAddress_Type()
)
cienaCesIclRemoteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclRemoteMacAddress.setStatus("current")


class _CienaCesIclType_Type(Integer32):
    """Custom type cienaCesIclType based on Integer32"""
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
        *(("mplsVs", 2),
          ("none", 4),
          ("qinqVs", 3),
          ("vlan", 1))
    )


_CienaCesIclType_Type.__name__ = "Integer32"
_CienaCesIclType_Object = MibTableColumn
cienaCesIclType = _CienaCesIclType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 4),
    _CienaCesIclType_Type()
)
cienaCesIclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclType.setStatus("current")
_CienaCesIclVlan_Type = Unsigned32
_CienaCesIclVlan_Object = MibTableColumn
cienaCesIclVlan = _CienaCesIclVlan_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 5),
    _CienaCesIclVlan_Type()
)
cienaCesIclVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclVlan.setStatus("current")
_CienaCesIclVsName_Type = DisplayString
_CienaCesIclVsName_Object = MibTableColumn
cienaCesIclVsName = _CienaCesIclVsName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 6),
    _CienaCesIclVsName_Type()
)
cienaCesIclVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclVsName.setStatus("current")
_CienaCesIclCfmServicePrimary_Type = DisplayString
_CienaCesIclCfmServicePrimary_Object = MibTableColumn
cienaCesIclCfmServicePrimary = _CienaCesIclCfmServicePrimary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 7),
    _CienaCesIclCfmServicePrimary_Type()
)
cienaCesIclCfmServicePrimary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclCfmServicePrimary.setStatus("current")
_CienaCesIclCfmServiceSecondary_Type = DisplayString
_CienaCesIclCfmServiceSecondary_Object = MibTableColumn
cienaCesIclCfmServiceSecondary = _CienaCesIclCfmServiceSecondary_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 8),
    _CienaCesIclCfmServiceSecondary_Type()
)
cienaCesIclCfmServiceSecondary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclCfmServiceSecondary.setStatus("current")
_CienaCesIclOperState_Type = CienaGlobalState
_CienaCesIclOperState_Object = MibTableColumn
cienaCesIclOperState = _CienaCesIclOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 9),
    _CienaCesIclOperState_Type()
)
cienaCesIclOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclOperState.setStatus("current")


class _CienaCesIclStatus_Type(Integer32):
    """Custom type cienaCesIclStatus based on Integer32"""
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
        *(("active", 2),
          ("down", 4),
          ("failed", 3),
          ("init", 1),
          ("none", 5))
    )


_CienaCesIclStatus_Type.__name__ = "Integer32"
_CienaCesIclStatus_Object = MibTableColumn
cienaCesIclStatus = _CienaCesIclStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 10),
    _CienaCesIclStatus_Type()
)
cienaCesIclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclStatus.setStatus("current")
_CienaCesIclAdminState_Type = CienaGlobalState
_CienaCesIclAdminState_Object = MibTableColumn
cienaCesIclAdminState = _CienaCesIclAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 11),
    _CienaCesIclAdminState_Type()
)
cienaCesIclAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclAdminState.setStatus("current")


class _CienaCesIclCfmFault_Type(Integer32):
    """Custom type cienaCesIclCfmFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CienaCesIclCfmFault_Type.__name__ = "Integer32"
_CienaCesIclCfmFault_Object = MibTableColumn
cienaCesIclCfmFault = _CienaCesIclCfmFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 12),
    _CienaCesIclCfmFault_Type()
)
cienaCesIclCfmFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclCfmFault.setStatus("current")


class _CienaCesIclVplsFault_Type(Integer32):
    """Custom type cienaCesIclVplsFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CienaCesIclVplsFault_Type.__name__ = "Integer32"
_CienaCesIclVplsFault_Object = MibTableColumn
cienaCesIclVplsFault = _CienaCesIclVplsFault_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 13),
    _CienaCesIclVplsFault_Type()
)
cienaCesIclVplsFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclVplsFault.setStatus("current")


class _CienaCesIclRxTimeout_Type(Integer32):
    """Custom type cienaCesIclRxTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CienaCesIclRxTimeout_Type.__name__ = "Integer32"
_CienaCesIclRxTimeout_Object = MibTableColumn
cienaCesIclRxTimeout = _CienaCesIclRxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 14),
    _CienaCesIclRxTimeout_Type()
)
cienaCesIclRxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclRxTimeout.setStatus("current")


class _CienaCesIclIntervalMismatch_Type(Integer32):
    """Custom type cienaCesIclIntervalMismatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_CienaCesIclIntervalMismatch_Type.__name__ = "Integer32"
_CienaCesIclIntervalMismatch_Object = MibTableColumn
cienaCesIclIntervalMismatch = _CienaCesIclIntervalMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 15),
    _CienaCesIclIntervalMismatch_Type()
)
cienaCesIclIntervalMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclIntervalMismatch.setStatus("current")
_CienaCesIclHeartbeatInterval_Type = Unsigned32
_CienaCesIclHeartbeatInterval_Object = MibTableColumn
cienaCesIclHeartbeatInterval = _CienaCesIclHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 16),
    _CienaCesIclHeartbeatInterval_Type()
)
cienaCesIclHeartbeatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclHeartbeatInterval.setStatus("current")
_CienaCesIclUpTime_Type = Unsigned32
_CienaCesIclUpTime_Object = MibTableColumn
cienaCesIclUpTime = _CienaCesIclUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 17),
    _CienaCesIclUpTime_Type()
)
cienaCesIclUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclUpTime.setStatus("current")
_CienaCesIclTotalDownTime_Type = Unsigned32
_CienaCesIclTotalDownTime_Object = MibTableColumn
cienaCesIclTotalDownTime = _CienaCesIclTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 18),
    _CienaCesIclTotalDownTime_Type()
)
cienaCesIclTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclTotalDownTime.setStatus("current")
_CienaCesIclRxFrames_Type = Counter32
_CienaCesIclRxFrames_Object = MibTableColumn
cienaCesIclRxFrames = _CienaCesIclRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 19),
    _CienaCesIclRxFrames_Type()
)
cienaCesIclRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclRxFrames.setStatus("current")
_CienaCesIclTxFrames_Type = Counter32
_CienaCesIclTxFrames_Object = MibTableColumn
cienaCesIclTxFrames = _CienaCesIclTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 20),
    _CienaCesIclTxFrames_Type()
)
cienaCesIclTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclTxFrames.setStatus("current")
_CienaCesIclRxUnknownFrames_Type = Counter32
_CienaCesIclRxUnknownFrames_Object = MibTableColumn
cienaCesIclRxUnknownFrames = _CienaCesIclRxUnknownFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 21),
    _CienaCesIclRxUnknownFrames_Type()
)
cienaCesIclRxUnknownFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclRxUnknownFrames.setStatus("current")
_CienaCesIclRxHtbtFrames_Type = Counter32
_CienaCesIclRxHtbtFrames_Object = MibTableColumn
cienaCesIclRxHtbtFrames = _CienaCesIclRxHtbtFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 22),
    _CienaCesIclRxHtbtFrames_Type()
)
cienaCesIclRxHtbtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclRxHtbtFrames.setStatus("current")
_CienaCesIclTxHtbtFrames_Type = Counter32
_CienaCesIclTxHtbtFrames_Object = MibTableColumn
cienaCesIclTxHtbtFrames = _CienaCesIclTxHtbtFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 23),
    _CienaCesIclTxHtbtFrames_Type()
)
cienaCesIclTxHtbtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclTxHtbtFrames.setStatus("current")
_CienaCesIclTxFailedFrames_Type = Counter32
_CienaCesIclTxFailedFrames_Object = MibTableColumn
cienaCesIclTxFailedFrames = _CienaCesIclTxFailedFrames_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 24),
    _CienaCesIclTxFailedFrames_Type()
)
cienaCesIclTxFailedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclTxFailedFrames.setStatus("current")
_CienaCesIclNumberFailures_Type = Counter32
_CienaCesIclNumberFailures_Object = MibTableColumn
cienaCesIclNumberFailures = _CienaCesIclNumberFailures_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 25),
    _CienaCesIclNumberFailures_Type()
)
cienaCesIclNumberFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclNumberFailures.setStatus("current")
_CienaCesIclRxConfigMismatch_Type = Counter32
_CienaCesIclRxConfigMismatch_Object = MibTableColumn
cienaCesIclRxConfigMismatch = _CienaCesIclRxConfigMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 1, 1, 1, 1, 26),
    _CienaCesIclRxConfigMismatch_Type()
)
cienaCesIclRxConfigMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesIclRxConfigMismatch.setStatus("current")
_CienaCesIclMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesIclMIBNotificationPrefix = _CienaCesIclMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 2)
)
_CienaCesIclMIBNotifications_ObjectIdentity = ObjectIdentity
cienaCesIclMIBNotifications = _CienaCesIclMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 2, 0)
)
_CienaCesIclMIBConformance_ObjectIdentity = ObjectIdentity
cienaCesIclMIBConformance = _CienaCesIclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 3)
)
_CienaCesIclMIBCompliances_ObjectIdentity = ObjectIdentity
cienaCesIclMIBCompliances = _CienaCesIclMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 3, 1)
)
_CienaCesIclMIBGroups_ObjectIdentity = ObjectIdentity
cienaCesIclMIBGroups = _CienaCesIclMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 3, 2)
)

# Managed Objects groups


# Notification objects

cienaCesIclStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 32, 2, 0, 1)
)
cienaCesIclStateChange.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-ICL-MIB", "cienaCesIclIndex"),
        ("CIENA-CES-ICL-MIB", "cienaCesIclName"),
        ("CIENA-CES-ICL-MIB", "cienaCesIclAdminState"),
        ("CIENA-CES-ICL-MIB", "cienaCesIclOperState"))
)
if mibBuilder.loadTexts:
    cienaCesIclStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-ICL-MIB",
    **{"cienaCesIclMIB": cienaCesIclMIB,
       "cienaCesIclMIBObjects": cienaCesIclMIBObjects,
       "cienaCesIcl": cienaCesIcl,
       "cienaCesIclTable": cienaCesIclTable,
       "cienaCesIclEntry": cienaCesIclEntry,
       "cienaCesIclIndex": cienaCesIclIndex,
       "cienaCesIclName": cienaCesIclName,
       "cienaCesIclRemoteMacAddress": cienaCesIclRemoteMacAddress,
       "cienaCesIclType": cienaCesIclType,
       "cienaCesIclVlan": cienaCesIclVlan,
       "cienaCesIclVsName": cienaCesIclVsName,
       "cienaCesIclCfmServicePrimary": cienaCesIclCfmServicePrimary,
       "cienaCesIclCfmServiceSecondary": cienaCesIclCfmServiceSecondary,
       "cienaCesIclOperState": cienaCesIclOperState,
       "cienaCesIclStatus": cienaCesIclStatus,
       "cienaCesIclAdminState": cienaCesIclAdminState,
       "cienaCesIclCfmFault": cienaCesIclCfmFault,
       "cienaCesIclVplsFault": cienaCesIclVplsFault,
       "cienaCesIclRxTimeout": cienaCesIclRxTimeout,
       "cienaCesIclIntervalMismatch": cienaCesIclIntervalMismatch,
       "cienaCesIclHeartbeatInterval": cienaCesIclHeartbeatInterval,
       "cienaCesIclUpTime": cienaCesIclUpTime,
       "cienaCesIclTotalDownTime": cienaCesIclTotalDownTime,
       "cienaCesIclRxFrames": cienaCesIclRxFrames,
       "cienaCesIclTxFrames": cienaCesIclTxFrames,
       "cienaCesIclRxUnknownFrames": cienaCesIclRxUnknownFrames,
       "cienaCesIclRxHtbtFrames": cienaCesIclRxHtbtFrames,
       "cienaCesIclTxHtbtFrames": cienaCesIclTxHtbtFrames,
       "cienaCesIclTxFailedFrames": cienaCesIclTxFailedFrames,
       "cienaCesIclNumberFailures": cienaCesIclNumberFailures,
       "cienaCesIclRxConfigMismatch": cienaCesIclRxConfigMismatch,
       "cienaCesIclMIBNotificationPrefix": cienaCesIclMIBNotificationPrefix,
       "cienaCesIclMIBNotifications": cienaCesIclMIBNotifications,
       "cienaCesIclStateChange": cienaCesIclStateChange,
       "cienaCesIclMIBConformance": cienaCesIclMIBConformance,
       "cienaCesIclMIBCompliances": cienaCesIclMIBCompliances,
       "cienaCesIclMIBGroups": cienaCesIclMIBGroups}
)
