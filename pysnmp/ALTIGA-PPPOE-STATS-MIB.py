# SNMP MIB module (ALTIGA-PPPOE-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALTIGA-PPPOE-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:19 2024
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

(alPPPoEMibModule,) = mibBuilder.importSymbols(
    "ALTIGA-GLOBAL-REG",
    "alPPPoEMibModule")

(alPPPoEGroup,
 alStatsPPPoE) = mibBuilder.importSymbols(
    "ALTIGA-MIB",
    "alPPPoEGroup",
    "alStatsPPPoE")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

altigaPPPoEStatsMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2)
)
altigaPPPoEStatsMibModule.setRevisions(
        ("2007-07-11 00:00",
         "2002-09-05 13:00",
         "2002-07-10 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AltigaPPPoEStatsMibConformance_ObjectIdentity = ObjectIdentity
altigaPPPoEStatsMibConformance = _AltigaPPPoEStatsMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2, 1)
)
_AltigaPPPoEStatsMibCompliances_ObjectIdentity = ObjectIdentity
altigaPPPoEStatsMibCompliances = _AltigaPPPoEStatsMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2, 1, 1)
)
_AlStatsPPPoEGlobal_ObjectIdentity = ObjectIdentity
alStatsPPPoEGlobal = _AlStatsPPPoEGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1)
)
_AlPPPoEStatsActiveSessions_Type = Gauge32
_AlPPPoEStatsActiveSessions_Object = MibScalar
alPPPoEStatsActiveSessions = _AlPPPoEStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1, 1),
    _AlPPPoEStatsActiveSessions_Type()
)
alPPPoEStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsActiveSessions.setStatus("current")
_AlPPPoEStatsTotalSessions_Type = Counter32
_AlPPPoEStatsTotalSessions_Object = MibScalar
alPPPoEStatsTotalSessions = _AlPPPoEStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1, 2),
    _AlPPPoEStatsTotalSessions_Type()
)
alPPPoEStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsTotalSessions.setStatus("current")
_AlPPPoEStatsMaxSessions_Type = Counter32
_AlPPPoEStatsMaxSessions_Object = MibScalar
alPPPoEStatsMaxSessions = _AlPPPoEStatsMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 1, 3),
    _AlPPPoEStatsMaxSessions_Type()
)
alPPPoEStatsMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsMaxSessions.setStatus("current")
_AlPPPoEStatsIfTable_Object = MibTable
alPPPoEStatsIfTable = _AlPPPoEStatsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2)
)
if mibBuilder.loadTexts:
    alPPPoEStatsIfTable.setStatus("current")
_AlPPPoEStatsIfEntry_Object = MibTableRow
alPPPoEStatsIfEntry = _AlPPPoEStatsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1)
)
alPPPoEStatsIfEntry.setIndexNames(
    (0, "ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfIndex"),
)
if mibBuilder.loadTexts:
    alPPPoEStatsIfEntry.setStatus("current")


class _AlPPPoEStatsIfIndex_Type(Integer32):
    """Custom type alPPPoEStatsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AlPPPoEStatsIfIndex_Type.__name__ = "Integer32"
_AlPPPoEStatsIfIndex_Object = MibTableColumn
alPPPoEStatsIfIndex = _AlPPPoEStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 1),
    _AlPPPoEStatsIfIndex_Type()
)
alPPPoEStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfIndex.setStatus("current")
_AlPPPoEStatsIfPADTRx_Type = Counter32
_AlPPPoEStatsIfPADTRx_Object = MibTableColumn
alPPPoEStatsIfPADTRx = _AlPPPoEStatsIfPADTRx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 2),
    _AlPPPoEStatsIfPADTRx_Type()
)
alPPPoEStatsIfPADTRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfPADTRx.setStatus("current")
_AlPPPoEStatsIfPADTTx_Type = Counter32
_AlPPPoEStatsIfPADTTx_Object = MibTableColumn
alPPPoEStatsIfPADTTx = _AlPPPoEStatsIfPADTTx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 3),
    _AlPPPoEStatsIfPADTTx_Type()
)
alPPPoEStatsIfPADTTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfPADTTx.setStatus("current")
_AlPPPoEStatsIfGenericErrorsRx_Type = Counter32
_AlPPPoEStatsIfGenericErrorsRx_Object = MibTableColumn
alPPPoEStatsIfGenericErrorsRx = _AlPPPoEStatsIfGenericErrorsRx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 4),
    _AlPPPoEStatsIfGenericErrorsRx_Type()
)
alPPPoEStatsIfGenericErrorsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfGenericErrorsRx.setStatus("current")
_AlPPPoEStatsIfMalformedPacketsRx_Type = Counter32
_AlPPPoEStatsIfMalformedPacketsRx_Object = MibTableColumn
alPPPoEStatsIfMalformedPacketsRx = _AlPPPoEStatsIfMalformedPacketsRx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 5),
    _AlPPPoEStatsIfMalformedPacketsRx_Type()
)
alPPPoEStatsIfMalformedPacketsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfMalformedPacketsRx.setStatus("current")
_AlPPPoEStatsIfPADITimeouts_Type = Counter32
_AlPPPoEStatsIfPADITimeouts_Object = MibTableColumn
alPPPoEStatsIfPADITimeouts = _AlPPPoEStatsIfPADITimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 6),
    _AlPPPoEStatsIfPADITimeouts_Type()
)
alPPPoEStatsIfPADITimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfPADITimeouts.setStatus("current")
_AlPPPoEStatsIfPADRTimeouts_Type = Counter32
_AlPPPoEStatsIfPADRTimeouts_Object = MibTableColumn
alPPPoEStatsIfPADRTimeouts = _AlPPPoEStatsIfPADRTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 7),
    _AlPPPoEStatsIfPADRTimeouts_Type()
)
alPPPoEStatsIfPADRTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfPADRTimeouts.setStatus("current")
_AlPPPoEStatsIfMultPADORx_Type = Counter32
_AlPPPoEStatsIfMultPADORx_Object = MibTableColumn
alPPPoEStatsIfMultPADORx = _AlPPPoEStatsIfMultPADORx_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 8),
    _AlPPPoEStatsIfMultPADORx_Type()
)
alPPPoEStatsIfMultPADORx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfMultPADORx.setStatus("current")
_AlPPPoEStatsIfSessionID_Type = Integer32
_AlPPPoEStatsIfSessionID_Object = MibTableColumn
alPPPoEStatsIfSessionID = _AlPPPoEStatsIfSessionID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 9),
    _AlPPPoEStatsIfSessionID_Type()
)
alPPPoEStatsIfSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfSessionID.setStatus("current")
_AlPPPoEStatsIfPeerAddr_Type = MacAddress
_AlPPPoEStatsIfPeerAddr_Object = MibTableColumn
alPPPoEStatsIfPeerAddr = _AlPPPoEStatsIfPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 10),
    _AlPPPoEStatsIfPeerAddr_Type()
)
alPPPoEStatsIfPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfPeerAddr.setStatus("current")


class _AlPPPoEStatsIfSessionState_Type(Integer32):
    """Custom type alPPPoEStatsIfSessionState based on Integer32"""
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
        *(("noState", 1),
          ("pADIRcvd", 3),
          ("pADISent", 2),
          ("pADORcvd", 5),
          ("pADOSent", 4),
          ("pADRRcvd", 7),
          ("pADRSent", 6),
          ("pADSRcvd", 9),
          ("pADSSent", 8),
          ("sessionStage", 10))
    )


_AlPPPoEStatsIfSessionState_Type.__name__ = "Integer32"
_AlPPPoEStatsIfSessionState_Object = MibTableColumn
alPPPoEStatsIfSessionState = _AlPPPoEStatsIfSessionState_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 11),
    _AlPPPoEStatsIfSessionState_Type()
)
alPPPoEStatsIfSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfSessionState.setStatus("current")
_AlPPPoEStatsIfVersion_Type = Integer32
_AlPPPoEStatsIfVersion_Object = MibTableColumn
alPPPoEStatsIfVersion = _AlPPPoEStatsIfVersion_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 12),
    _AlPPPoEStatsIfVersion_Type()
)
alPPPoEStatsIfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfVersion.setStatus("current")
_AlPPPoEStatsIfType_Type = Integer32
_AlPPPoEStatsIfType_Object = MibTableColumn
alPPPoEStatsIfType = _AlPPPoEStatsIfType_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 13),
    _AlPPPoEStatsIfType_Type()
)
alPPPoEStatsIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfType.setStatus("current")
_AlPPPoEStatsIfConnectTime_Type = Unsigned32
_AlPPPoEStatsIfConnectTime_Object = MibTableColumn
alPPPoEStatsIfConnectTime = _AlPPPoEStatsIfConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 14),
    _AlPPPoEStatsIfConnectTime_Type()
)
alPPPoEStatsIfConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfConnectTime.setStatus("current")
_AlPPPoEStatsIfDuration_Type = Unsigned32
_AlPPPoEStatsIfDuration_Object = MibTableColumn
alPPPoEStatsIfDuration = _AlPPPoEStatsIfDuration_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 15),
    _AlPPPoEStatsIfDuration_Type()
)
alPPPoEStatsIfDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfDuration.setStatus("current")
_AlPPPoEStatsIfPeerName_Type = DisplayString
_AlPPPoEStatsIfPeerName_Object = MibTableColumn
alPPPoEStatsIfPeerName = _AlPPPoEStatsIfPeerName_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 16),
    _AlPPPoEStatsIfPeerName_Type()
)
alPPPoEStatsIfPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfPeerName.setStatus("current")


class _AlPPPoEStatsIfACCookie_Type(OctetString):
    """Custom type alPPPoEStatsIfACCookie based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlPPPoEStatsIfACCookie_Type.__name__ = "OctetString"
_AlPPPoEStatsIfACCookie_Object = MibTableColumn
alPPPoEStatsIfACCookie = _AlPPPoEStatsIfACCookie_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 17),
    _AlPPPoEStatsIfACCookie_Type()
)
alPPPoEStatsIfACCookie.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfACCookie.setStatus("current")


class _AlPPPoEStatsIfHostUnique_Type(OctetString):
    """Custom type alPPPoEStatsIfHostUnique based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AlPPPoEStatsIfHostUnique_Type.__name__ = "OctetString"
_AlPPPoEStatsIfHostUnique_Object = MibTableColumn
alPPPoEStatsIfHostUnique = _AlPPPoEStatsIfHostUnique_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 18),
    _AlPPPoEStatsIfHostUnique_Type()
)
alPPPoEStatsIfHostUnique.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfHostUnique.setStatus("current")


class _AlPPPoEStatsIfRelaySessID_Type(OctetString):
    """Custom type alPPPoEStatsIfRelaySessID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_AlPPPoEStatsIfRelaySessID_Type.__name__ = "OctetString"
_AlPPPoEStatsIfRelaySessID_Object = MibTableColumn
alPPPoEStatsIfRelaySessID = _AlPPPoEStatsIfRelaySessID_Object(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 2, 40, 2, 1, 19),
    _AlPPPoEStatsIfRelaySessID_Type()
)
alPPPoEStatsIfRelaySessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alPPPoEStatsIfRelaySessID.setStatus("current")

# Managed Objects groups

altigaPPPoEStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3076, 2, 1, 1, 1, 40, 2)
)
altigaPPPoEStatsGroup.setObjects(
      *(("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsActiveSessions"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsTotalSessions"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsMaxSessions"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfIndex"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADTRx"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADTTx"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfGenericErrorsRx"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfMalformedPacketsRx"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADITimeouts"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPADRTimeouts"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfMultPADORx"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfSessionID"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPeerAddr"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfSessionState"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfVersion"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfType"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfConnectTime"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfDuration"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfPeerName"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfACCookie"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfHostUnique"),
        ("ALTIGA-PPPOE-STATS-MIB", "alPPPoEStatsIfRelaySessID"))
)
if mibBuilder.loadTexts:
    altigaPPPoEStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

altigaPPPoEStatsMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3076, 1, 1, 45, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    altigaPPPoEStatsMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALTIGA-PPPOE-STATS-MIB",
    **{"altigaPPPoEStatsMibModule": altigaPPPoEStatsMibModule,
       "altigaPPPoEStatsMibConformance": altigaPPPoEStatsMibConformance,
       "altigaPPPoEStatsMibCompliances": altigaPPPoEStatsMibCompliances,
       "altigaPPPoEStatsMibCompliance": altigaPPPoEStatsMibCompliance,
       "altigaPPPoEStatsGroup": altigaPPPoEStatsGroup,
       "alStatsPPPoEGlobal": alStatsPPPoEGlobal,
       "alPPPoEStatsActiveSessions": alPPPoEStatsActiveSessions,
       "alPPPoEStatsTotalSessions": alPPPoEStatsTotalSessions,
       "alPPPoEStatsMaxSessions": alPPPoEStatsMaxSessions,
       "alPPPoEStatsIfTable": alPPPoEStatsIfTable,
       "alPPPoEStatsIfEntry": alPPPoEStatsIfEntry,
       "alPPPoEStatsIfIndex": alPPPoEStatsIfIndex,
       "alPPPoEStatsIfPADTRx": alPPPoEStatsIfPADTRx,
       "alPPPoEStatsIfPADTTx": alPPPoEStatsIfPADTTx,
       "alPPPoEStatsIfGenericErrorsRx": alPPPoEStatsIfGenericErrorsRx,
       "alPPPoEStatsIfMalformedPacketsRx": alPPPoEStatsIfMalformedPacketsRx,
       "alPPPoEStatsIfPADITimeouts": alPPPoEStatsIfPADITimeouts,
       "alPPPoEStatsIfPADRTimeouts": alPPPoEStatsIfPADRTimeouts,
       "alPPPoEStatsIfMultPADORx": alPPPoEStatsIfMultPADORx,
       "alPPPoEStatsIfSessionID": alPPPoEStatsIfSessionID,
       "alPPPoEStatsIfPeerAddr": alPPPoEStatsIfPeerAddr,
       "alPPPoEStatsIfSessionState": alPPPoEStatsIfSessionState,
       "alPPPoEStatsIfVersion": alPPPoEStatsIfVersion,
       "alPPPoEStatsIfType": alPPPoEStatsIfType,
       "alPPPoEStatsIfConnectTime": alPPPoEStatsIfConnectTime,
       "alPPPoEStatsIfDuration": alPPPoEStatsIfDuration,
       "alPPPoEStatsIfPeerName": alPPPoEStatsIfPeerName,
       "alPPPoEStatsIfACCookie": alPPPoEStatsIfACCookie,
       "alPPPoEStatsIfHostUnique": alPPPoEStatsIfHostUnique,
       "alPPPoEStatsIfRelaySessID": alPPPoEStatsIfRelaySessID}
)
