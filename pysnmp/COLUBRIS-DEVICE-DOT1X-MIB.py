# SNMP MIB module (COLUBRIS-DEVICE-DOT1X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-DEVICE-DOT1X-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:14 2024
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

(coDevDisIndex,) = mibBuilder.importSymbols(
    "COLUBRIS-DEVICE-MIB",
    "coDevDisIndex")

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubrisDeviceDot1xMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisDeviceDot1xMIBObjects_ObjectIdentity = ObjectIdentity
colubrisDeviceDot1xMIBObjects = _ColubrisDeviceDot1xMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1)
)
_CoDeviceDot1xConfigGroup_ObjectIdentity = ObjectIdentity
coDeviceDot1xConfigGroup = _CoDeviceDot1xConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 1)
)
_CoDeviceDot1xStatusGroup_ObjectIdentity = ObjectIdentity
coDeviceDot1xStatusGroup = _CoDeviceDot1xStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2)
)
_CoDeviceDot1xStatusTable_Object = MibTable
coDeviceDot1xStatusTable = _CoDeviceDot1xStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1)
)
if mibBuilder.loadTexts:
    coDeviceDot1xStatusTable.setStatus("current")
_CoDeviceDot1xStatusEntry_Object = MibTableRow
coDeviceDot1xStatusEntry = _CoDeviceDot1xStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1)
)
coDeviceDot1xStatusEntry.setIndexNames(
    (0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"),
    (0, "COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaIndex"),
)
if mibBuilder.loadTexts:
    coDeviceDot1xStatusEntry.setStatus("current")


class _CoDev1xStaIndex_Type(Integer32):
    """Custom type coDev1xStaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDev1xStaIndex_Type.__name__ = "Integer32"
_CoDev1xStaIndex_Object = MibTableColumn
coDev1xStaIndex = _CoDev1xStaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 1),
    _CoDev1xStaIndex_Type()
)
coDev1xStaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDev1xStaIndex.setStatus("current")
_CoDev1xStaMacAddress_Type = MacAddress
_CoDev1xStaMacAddress_Object = MibTableColumn
coDev1xStaMacAddress = _CoDev1xStaMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 2),
    _CoDev1xStaMacAddress_Type()
)
coDev1xStaMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaMacAddress.setStatus("current")
_CoDev1xStaUserName_Type = DisplayString
_CoDev1xStaUserName_Object = MibTableColumn
coDev1xStaUserName = _CoDev1xStaUserName_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 3),
    _CoDev1xStaUserName_Type()
)
coDev1xStaUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaUserName.setStatus("current")


class _CoDev1xStaPaeState_Type(Integer32):
    """Custom type coDev1xStaPaeState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("aborting", 6),
          ("authenticated", 5),
          ("authenticating", 4),
          ("connecting", 3),
          ("disconnected", 2),
          ("forceAuth", 8),
          ("forceUnauth", 9),
          ("held", 7),
          ("initialize", 1))
    )


_CoDev1xStaPaeState_Type.__name__ = "Integer32"
_CoDev1xStaPaeState_Object = MibTableColumn
coDev1xStaPaeState = _CoDev1xStaPaeState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 4),
    _CoDev1xStaPaeState_Type()
)
coDev1xStaPaeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaPaeState.setStatus("current")


class _CoDev1xStaBackendAuthState_Type(Integer32):
    """Custom type coDev1xStaBackendAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fail", 4),
          ("idle", 6),
          ("initialize", 7),
          ("request", 1),
          ("response", 2),
          ("success", 3),
          ("timeout", 5))
    )


_CoDev1xStaBackendAuthState_Type.__name__ = "Integer32"
_CoDev1xStaBackendAuthState_Object = MibTableColumn
coDev1xStaBackendAuthState = _CoDev1xStaBackendAuthState_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 5),
    _CoDev1xStaBackendAuthState_Type()
)
coDev1xStaBackendAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaBackendAuthState.setStatus("current")


class _CoDev1xStaPortStatus_Type(Integer32):
    """Custom type coDev1xStaPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2))
    )


_CoDev1xStaPortStatus_Type.__name__ = "Integer32"
_CoDev1xStaPortStatus_Object = MibTableColumn
coDev1xStaPortStatus = _CoDev1xStaPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 6),
    _CoDev1xStaPortStatus_Type()
)
coDev1xStaPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaPortStatus.setStatus("current")
_CoDev1xStaSessionTime_Type = Counter32
_CoDev1xStaSessionTime_Object = MibTableColumn
coDev1xStaSessionTime = _CoDev1xStaSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 7),
    _CoDev1xStaSessionTime_Type()
)
coDev1xStaSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaSessionTime.setStatus("current")
if mibBuilder.loadTexts:
    coDev1xStaSessionTime.setUnits("seconds")


class _CoDev1xStaTerminateCause_Type(Integer32):
    """Custom type coDev1xStaTerminateCause based on Integer32"""
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
              999)
        )
    )
    namedValues = NamedValues(
        *(("authControlForceUnauth", 5),
          ("notTerminatedYet", 999),
          ("portAdminDisabled", 7),
          ("portFailure", 2),
          ("portReInit", 6),
          ("reauthFailed", 4),
          ("supplicantLogoff", 1),
          ("supplicantRestart", 3))
    )


_CoDev1xStaTerminateCause_Type.__name__ = "Integer32"
_CoDev1xStaTerminateCause_Object = MibTableColumn
coDev1xStaTerminateCause = _CoDev1xStaTerminateCause_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 2, 1, 1, 8),
    _CoDev1xStaTerminateCause_Type()
)
coDev1xStaTerminateCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaTerminateCause.setStatus("current")
_CoDeviceDot1xStatsGroup_ObjectIdentity = ObjectIdentity
coDeviceDot1xStatsGroup = _CoDeviceDot1xStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3)
)
_CoDeviceDot1xStatsTable_Object = MibTable
coDeviceDot1xStatsTable = _CoDeviceDot1xStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDeviceDot1xStatsTable.setStatus("current")
_CoDeviceDot1xStatsEntry_Object = MibTableRow
coDeviceDot1xStatsEntry = _CoDeviceDot1xStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    coDeviceDot1xStatsEntry.setStatus("current")
_CoDev1xStaEapolRxFrame_Type = Counter32
_CoDev1xStaEapolRxFrame_Object = MibTableColumn
coDev1xStaEapolRxFrame = _CoDev1xStaEapolRxFrame_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 1),
    _CoDev1xStaEapolRxFrame_Type()
)
coDev1xStaEapolRxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaEapolRxFrame.setStatus("current")
_CoDev1xStaEapolTxFrame_Type = Counter32
_CoDev1xStaEapolTxFrame_Object = MibTableColumn
coDev1xStaEapolTxFrame = _CoDev1xStaEapolTxFrame_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 2),
    _CoDev1xStaEapolTxFrame_Type()
)
coDev1xStaEapolTxFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaEapolTxFrame.setStatus("current")
_CoDev1xStaBackendResponses_Type = Counter32
_CoDev1xStaBackendResponses_Object = MibTableColumn
coDev1xStaBackendResponses = _CoDev1xStaBackendResponses_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 3),
    _CoDev1xStaBackendResponses_Type()
)
coDev1xStaBackendResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaBackendResponses.setStatus("current")
_CoDev1xStaBackendChallenges_Type = Counter32
_CoDev1xStaBackendChallenges_Object = MibTableColumn
coDev1xStaBackendChallenges = _CoDev1xStaBackendChallenges_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 4),
    _CoDev1xStaBackendChallenges_Type()
)
coDev1xStaBackendChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaBackendChallenges.setStatus("current")
_CoDev1xStaBackendAuthSuccesses_Type = Counter32
_CoDev1xStaBackendAuthSuccesses_Object = MibTableColumn
coDev1xStaBackendAuthSuccesses = _CoDev1xStaBackendAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 5),
    _CoDev1xStaBackendAuthSuccesses_Type()
)
coDev1xStaBackendAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaBackendAuthSuccesses.setStatus("current")
_CoDev1xStaBackendAuthFails_Type = Counter32
_CoDev1xStaBackendAuthFails_Object = MibTableColumn
coDev1xStaBackendAuthFails = _CoDev1xStaBackendAuthFails_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 1, 3, 1, 1, 6),
    _CoDev1xStaBackendAuthFails_Type()
)
coDev1xStaBackendAuthFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDev1xStaBackendAuthFails.setStatus("current")
_ColubrisDeviceDot1xMIBConformance_ObjectIdentity = ObjectIdentity
colubrisDeviceDot1xMIBConformance = _ColubrisDeviceDot1xMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 2)
)
_ColubrisDeviceDot1xMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisDeviceDot1xMIBCompliances = _ColubrisDeviceDot1xMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 1)
)
_ColubrisDeviceDot1xMIBGroups_ObjectIdentity = ObjectIdentity
colubrisDeviceDot1xMIBGroups = _ColubrisDeviceDot1xMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2)
)
coDeviceDot1xStatusEntry.registerAugmentions(
    ("COLUBRIS-DEVICE-DOT1X-MIB",
     "coDeviceDot1xStatsEntry")
)
coDeviceDot1xStatsEntry.setIndexNames(*coDeviceDot1xStatusEntry.getIndexNames())

# Managed Objects groups

colubrisDeviceDot1xStatusMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2, 1)
)
colubrisDeviceDot1xStatusMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaMacAddress"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaUserName"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaPaeState"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthState"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaPortStatus"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaSessionTime"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaTerminateCause"))
)
if mibBuilder.loadTexts:
    colubrisDeviceDot1xStatusMIBGroup.setStatus("current")

colubrisDeviceDot1xStatsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 2, 2)
)
colubrisDeviceDot1xStatsMIBGroup.setObjects(
      *(("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaEapolRxFrame"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaEapolTxFrame"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendResponses"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendChallenges"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthSuccesses"),
        ("COLUBRIS-DEVICE-DOT1X-MIB", "coDev1xStaBackendAuthFails"))
)
if mibBuilder.loadTexts:
    colubrisDeviceDot1xStatsMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisDeviceDot1xMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 32, 2, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisDeviceDot1xMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-DEVICE-DOT1X-MIB",
    **{"colubrisDeviceDot1xMIB": colubrisDeviceDot1xMIB,
       "colubrisDeviceDot1xMIBObjects": colubrisDeviceDot1xMIBObjects,
       "coDeviceDot1xConfigGroup": coDeviceDot1xConfigGroup,
       "coDeviceDot1xStatusGroup": coDeviceDot1xStatusGroup,
       "coDeviceDot1xStatusTable": coDeviceDot1xStatusTable,
       "coDeviceDot1xStatusEntry": coDeviceDot1xStatusEntry,
       "coDev1xStaIndex": coDev1xStaIndex,
       "coDev1xStaMacAddress": coDev1xStaMacAddress,
       "coDev1xStaUserName": coDev1xStaUserName,
       "coDev1xStaPaeState": coDev1xStaPaeState,
       "coDev1xStaBackendAuthState": coDev1xStaBackendAuthState,
       "coDev1xStaPortStatus": coDev1xStaPortStatus,
       "coDev1xStaSessionTime": coDev1xStaSessionTime,
       "coDev1xStaTerminateCause": coDev1xStaTerminateCause,
       "coDeviceDot1xStatsGroup": coDeviceDot1xStatsGroup,
       "coDeviceDot1xStatsTable": coDeviceDot1xStatsTable,
       "coDeviceDot1xStatsEntry": coDeviceDot1xStatsEntry,
       "coDev1xStaEapolRxFrame": coDev1xStaEapolRxFrame,
       "coDev1xStaEapolTxFrame": coDev1xStaEapolTxFrame,
       "coDev1xStaBackendResponses": coDev1xStaBackendResponses,
       "coDev1xStaBackendChallenges": coDev1xStaBackendChallenges,
       "coDev1xStaBackendAuthSuccesses": coDev1xStaBackendAuthSuccesses,
       "coDev1xStaBackendAuthFails": coDev1xStaBackendAuthFails,
       "colubrisDeviceDot1xMIBConformance": colubrisDeviceDot1xMIBConformance,
       "colubrisDeviceDot1xMIBCompliances": colubrisDeviceDot1xMIBCompliances,
       "colubrisDeviceDot1xMIBCompliance": colubrisDeviceDot1xMIBCompliance,
       "colubrisDeviceDot1xMIBGroups": colubrisDeviceDot1xMIBGroups,
       "colubrisDeviceDot1xStatusMIBGroup": colubrisDeviceDot1xStatusMIBGroup,
       "colubrisDeviceDot1xStatsMIBGroup": colubrisDeviceDot1xStatsMIBGroup}
)
