# SNMP MIB module (CIENA-CES-BFD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-BFD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:56 2024
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
 cienaCesNotifications,
 cienaCesStatistics) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications",
    "cienaCesStatistics")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesBfdMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22)
)
cienaCesBfdMIB.setRevisions(
        ("2014-04-04 00:00",
         "2014-03-19 00:00",
         "2011-07-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BfdRole(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("passive", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CienaCesBfdMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesBfdMIBObjects = _CienaCesBfdMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1)
)
_CienaCesBfdSession_ObjectIdentity = ObjectIdentity
cienaCesBfdSession = _CienaCesBfdSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2)
)
_CienaCesBfdSessionTable_Object = MibTable
cienaCesBfdSessionTable = _CienaCesBfdSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesBfdSessionTable.setStatus("current")
_CienaCesBfdSessionEntry_Object = MibTableRow
cienaCesBfdSessionEntry = _CienaCesBfdSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2, 1, 1)
)
cienaCesBfdSessionEntry.setIndexNames(
    (0, "CIENA-CES-BFD-MIB", "cienaCesBfdSessionIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBfdSessionEntry.setStatus("current")
_CienaCesBfdSessionIndex_Type = Unsigned32
_CienaCesBfdSessionIndex_Object = MibTableColumn
cienaCesBfdSessionIndex = _CienaCesBfdSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2, 1, 1, 1),
    _CienaCesBfdSessionIndex_Type()
)
cienaCesBfdSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBfdSessionIndex.setStatus("current")
_CienaCesBfdSessionName_Type = DisplayString
_CienaCesBfdSessionName_Object = MibTableColumn
cienaCesBfdSessionName = _CienaCesBfdSessionName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2, 1, 1, 2),
    _CienaCesBfdSessionName_Type()
)
cienaCesBfdSessionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionName.setStatus("current")
_CienaCesBfdSessionAdminState_Type = CienaGlobalState
_CienaCesBfdSessionAdminState_Object = MibTableColumn
cienaCesBfdSessionAdminState = _CienaCesBfdSessionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2, 1, 1, 3),
    _CienaCesBfdSessionAdminState_Type()
)
cienaCesBfdSessionAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionAdminState.setStatus("current")
_CienaCesBfdSessionOperState_Type = CienaGlobalState
_CienaCesBfdSessionOperState_Object = MibTableColumn
cienaCesBfdSessionOperState = _CienaCesBfdSessionOperState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2, 1, 1, 4),
    _CienaCesBfdSessionOperState_Type()
)
cienaCesBfdSessionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionOperState.setStatus("current")
_CienaCesBfdSessionProfileIndex_Type = Unsigned32
_CienaCesBfdSessionProfileIndex_Object = MibTableColumn
cienaCesBfdSessionProfileIndex = _CienaCesBfdSessionProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 2, 1, 1, 5),
    _CienaCesBfdSessionProfileIndex_Type()
)
cienaCesBfdSessionProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionProfileIndex.setStatus("current")
_CienaCesBfdProfile_ObjectIdentity = ObjectIdentity
cienaCesBfdProfile = _CienaCesBfdProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3)
)
_CienaCesBfdProfileTable_Object = MibTable
cienaCesBfdProfileTable = _CienaCesBfdProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cienaCesBfdProfileTable.setStatus("current")
_CienaCesBfdProfileEntry_Object = MibTableRow
cienaCesBfdProfileEntry = _CienaCesBfdProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1)
)
cienaCesBfdProfileEntry.setIndexNames(
    (0, "CIENA-CES-BFD-MIB", "cienaCesBfdProfileIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBfdProfileEntry.setStatus("current")
_CienaCesBfdProfileIndex_Type = Unsigned32
_CienaCesBfdProfileIndex_Object = MibTableColumn
cienaCesBfdProfileIndex = _CienaCesBfdProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 1),
    _CienaCesBfdProfileIndex_Type()
)
cienaCesBfdProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesBfdProfileIndex.setStatus("current")
_CienaCesBfdProfileName_Type = DisplayString
_CienaCesBfdProfileName_Object = MibTableColumn
cienaCesBfdProfileName = _CienaCesBfdProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 2),
    _CienaCesBfdProfileName_Type()
)
cienaCesBfdProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdProfileName.setStatus("current")
_CienaCesBfdTransmitInterval_Type = Unsigned32
_CienaCesBfdTransmitInterval_Object = MibTableColumn
cienaCesBfdTransmitInterval = _CienaCesBfdTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 3),
    _CienaCesBfdTransmitInterval_Type()
)
cienaCesBfdTransmitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdTransmitInterval.setStatus("current")
_CienaCesBfdReceiveInterval_Type = Unsigned32
_CienaCesBfdReceiveInterval_Object = MibTableColumn
cienaCesBfdReceiveInterval = _CienaCesBfdReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 4),
    _CienaCesBfdReceiveInterval_Type()
)
cienaCesBfdReceiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdReceiveInterval.setStatus("current")
_CienaCesBfdRole_Type = BfdRole
_CienaCesBfdRole_Object = MibTableColumn
cienaCesBfdRole = _CienaCesBfdRole_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 5),
    _CienaCesBfdRole_Type()
)
cienaCesBfdRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdRole.setStatus("current")
_CienaCesBfdLspGachType_Type = Unsigned32
_CienaCesBfdLspGachType_Object = MibTableColumn
cienaCesBfdLspGachType = _CienaCesBfdLspGachType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 6),
    _CienaCesBfdLspGachType_Type()
)
cienaCesBfdLspGachType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdLspGachType.setStatus("current")
_CienaCesBfdDetectMultiplier_Type = Unsigned32
_CienaCesBfdDetectMultiplier_Object = MibTableColumn
cienaCesBfdDetectMultiplier = _CienaCesBfdDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 7),
    _CienaCesBfdDetectMultiplier_Type()
)
cienaCesBfdDetectMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdDetectMultiplier.setStatus("current")
_CienaCesBfdUseCount_Type = Unsigned32
_CienaCesBfdUseCount_Object = MibTableColumn
cienaCesBfdUseCount = _CienaCesBfdUseCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 22, 1, 3, 1, 1, 8),
    _CienaCesBfdUseCount_Type()
)
cienaCesBfdUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdUseCount.setStatus("current")
_CienaCesBfdSessionMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cienaCesBfdSessionMIBNotificationPrefix = _CienaCesBfdSessionMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 19)
)
_CienaCesBfdSessionMIBNotification_ObjectIdentity = ObjectIdentity
cienaCesBfdSessionMIBNotification = _CienaCesBfdSessionMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 19, 0)
)
_CienaCesBfdSessionStats_ObjectIdentity = ObjectIdentity
cienaCesBfdSessionStats = _CienaCesBfdSessionStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 7)
)
_CienaCesBfdSessionStatsTable_Object = MibTable
cienaCesBfdSessionStatsTable = _CienaCesBfdSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    cienaCesBfdSessionStatsTable.setStatus("current")
_CienaCesBfdSessionStatsEntry_Object = MibTableRow
cienaCesBfdSessionStatsEntry = _CienaCesBfdSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 7, 1, 1)
)
cienaCesBfdSessionStatsEntry.setIndexNames(
    (0, "CIENA-CES-BFD-MIB", "cienaCesBfdSessionIndex"),
)
if mibBuilder.loadTexts:
    cienaCesBfdSessionStatsEntry.setStatus("current")
_CienaCesBfdSessionStatsTotalTx_Type = Unsigned32
_CienaCesBfdSessionStatsTotalTx_Object = MibTableColumn
cienaCesBfdSessionStatsTotalTx = _CienaCesBfdSessionStatsTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 7, 1, 1, 1),
    _CienaCesBfdSessionStatsTotalTx_Type()
)
cienaCesBfdSessionStatsTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionStatsTotalTx.setStatus("current")
_CienaCesBfdSessionStatsTotalRx_Type = Unsigned32
_CienaCesBfdSessionStatsTotalRx_Object = MibTableColumn
cienaCesBfdSessionStatsTotalRx = _CienaCesBfdSessionStatsTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 7, 1, 1, 2),
    _CienaCesBfdSessionStatsTotalRx_Type()
)
cienaCesBfdSessionStatsTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionStatsTotalRx.setStatus("current")
_CienaCesBfdSessionUpTime_Type = Unsigned32
_CienaCesBfdSessionUpTime_Object = MibTableColumn
cienaCesBfdSessionUpTime = _CienaCesBfdSessionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 7, 1, 1, 3),
    _CienaCesBfdSessionUpTime_Type()
)
cienaCesBfdSessionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionUpTime.setStatus("current")
_CienaCesBfdSessionDownTimeCount_Type = Unsigned32
_CienaCesBfdSessionDownTimeCount_Object = MibTableColumn
cienaCesBfdSessionDownTimeCount = _CienaCesBfdSessionDownTimeCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 3, 7, 1, 1, 4),
    _CienaCesBfdSessionDownTimeCount_Type()
)
cienaCesBfdSessionDownTimeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesBfdSessionDownTimeCount.setStatus("current")

# Managed Objects groups


# Notification objects

cienaCesBfdSessionOperStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 1271, 2, 2, 19, 0, 1)
)
cienaCesBfdSessionOperStateChangeTrap.setObjects(
      *(("CIENA-GLOBAL-MIB", "cienaGlobalSeverity"),
        ("CIENA-GLOBAL-MIB", "cienaGlobalMacAddress"),
        ("CIENA-CES-BFD-MIB", "cienaCesBfdSessionName"),
        ("CIENA-CES-BFD-MIB", "cienaCesBfdSessionIndex"),
        ("CIENA-CES-BFD-MIB", "cienaCesBfdSessionAdminState"),
        ("CIENA-CES-BFD-MIB", "cienaCesBfdSessionOperState"))
)
if mibBuilder.loadTexts:
    cienaCesBfdSessionOperStateChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-BFD-MIB",
    **{"BfdRole": BfdRole,
       "cienaCesBfdMIB": cienaCesBfdMIB,
       "cienaCesBfdMIBObjects": cienaCesBfdMIBObjects,
       "cienaCesBfdSession": cienaCesBfdSession,
       "cienaCesBfdSessionTable": cienaCesBfdSessionTable,
       "cienaCesBfdSessionEntry": cienaCesBfdSessionEntry,
       "cienaCesBfdSessionIndex": cienaCesBfdSessionIndex,
       "cienaCesBfdSessionName": cienaCesBfdSessionName,
       "cienaCesBfdSessionAdminState": cienaCesBfdSessionAdminState,
       "cienaCesBfdSessionOperState": cienaCesBfdSessionOperState,
       "cienaCesBfdSessionProfileIndex": cienaCesBfdSessionProfileIndex,
       "cienaCesBfdProfile": cienaCesBfdProfile,
       "cienaCesBfdProfileTable": cienaCesBfdProfileTable,
       "cienaCesBfdProfileEntry": cienaCesBfdProfileEntry,
       "cienaCesBfdProfileIndex": cienaCesBfdProfileIndex,
       "cienaCesBfdProfileName": cienaCesBfdProfileName,
       "cienaCesBfdTransmitInterval": cienaCesBfdTransmitInterval,
       "cienaCesBfdReceiveInterval": cienaCesBfdReceiveInterval,
       "cienaCesBfdRole": cienaCesBfdRole,
       "cienaCesBfdLspGachType": cienaCesBfdLspGachType,
       "cienaCesBfdDetectMultiplier": cienaCesBfdDetectMultiplier,
       "cienaCesBfdUseCount": cienaCesBfdUseCount,
       "cienaCesBfdSessionMIBNotificationPrefix": cienaCesBfdSessionMIBNotificationPrefix,
       "cienaCesBfdSessionMIBNotification": cienaCesBfdSessionMIBNotification,
       "cienaCesBfdSessionOperStateChangeTrap": cienaCesBfdSessionOperStateChangeTrap,
       "cienaCesBfdSessionStats": cienaCesBfdSessionStats,
       "cienaCesBfdSessionStatsTable": cienaCesBfdSessionStatsTable,
       "cienaCesBfdSessionStatsEntry": cienaCesBfdSessionStatsEntry,
       "cienaCesBfdSessionStatsTotalTx": cienaCesBfdSessionStatsTotalTx,
       "cienaCesBfdSessionStatsTotalRx": cienaCesBfdSessionStatsTotalRx,
       "cienaCesBfdSessionUpTime": cienaCesBfdSessionUpTime,
       "cienaCesBfdSessionDownTimeCount": cienaCesBfdSessionDownTimeCount}
)
