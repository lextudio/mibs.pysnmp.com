# SNMP MIB module (CIENA-CES-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:59 2024
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

(cienaCesConfig,
 cienaCesNotifications) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig",
    "cienaCesNotifications")

(CienaGlobalState,) = mibBuilder.importSymbols(
    "CIENA-TC",
    "CienaGlobalState")

(MplsLdpIdentifier,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLdpIdentifier")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cienaCesLdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17)
)
cienaCesLdpMIB.setRevisions(
        ("2016-07-15 00:00",
         "2016-07-11 00:00",
         "2013-04-18 00:00",
         "2011-02-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CienaCesLdpMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesLdpMIBObjects = _CienaCesLdpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1)
)
_CienaCesLdpObjects_ObjectIdentity = ObjectIdentity
cienaCesLdpObjects = _CienaCesLdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1)
)
_CienaCesLdpAdminStatus_Type = CienaGlobalState
_CienaCesLdpAdminStatus_Object = MibScalar
cienaCesLdpAdminStatus = _CienaCesLdpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 1),
    _CienaCesLdpAdminStatus_Type()
)
cienaCesLdpAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpAdminStatus.setStatus("current")


class _CienaCesLdpOperStatus_Type(Integer32):
    """Custom type cienaCesLdpOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 0),
          ("up", 1))
    )


_CienaCesLdpOperStatus_Type.__name__ = "Integer32"
_CienaCesLdpOperStatus_Object = MibScalar
cienaCesLdpOperStatus = _CienaCesLdpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 2),
    _CienaCesLdpOperStatus_Type()
)
cienaCesLdpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpOperStatus.setStatus("current")


class _CienaCesLdpHelloHoldTime_Type(Unsigned32):
    """Custom type cienaCesLdpHelloHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesLdpHelloHoldTime_Type.__name__ = "Unsigned32"
_CienaCesLdpHelloHoldTime_Object = MibScalar
cienaCesLdpHelloHoldTime = _CienaCesLdpHelloHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 3),
    _CienaCesLdpHelloHoldTime_Type()
)
cienaCesLdpHelloHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpHelloHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesLdpHelloHoldTime.setUnits("seconds")


class _CienaCesLdpKeepAliveHoldTime_Type(Unsigned32):
    """Custom type cienaCesLdpKeepAliveHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CienaCesLdpKeepAliveHoldTime_Type.__name__ = "Unsigned32"
_CienaCesLdpKeepAliveHoldTime_Object = MibScalar
cienaCesLdpKeepAliveHoldTime = _CienaCesLdpKeepAliveHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 4),
    _CienaCesLdpKeepAliveHoldTime_Type()
)
cienaCesLdpKeepAliveHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpKeepAliveHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesLdpKeepAliveHoldTime.setUnits("seconds")
_CienaCesLdpGRAdminStatus_Type = CienaGlobalState
_CienaCesLdpGRAdminStatus_Object = MibScalar
cienaCesLdpGRAdminStatus = _CienaCesLdpGRAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 5),
    _CienaCesLdpGRAdminStatus_Type()
)
cienaCesLdpGRAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpGRAdminStatus.setStatus("current")


class _CienaCesLdpGRMode_Type(Integer32):
    """Custom type cienaCesLdpGRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("helpNeighbor", 1),
          ("notApplicable", 3),
          ("restartCapable", 2))
    )


_CienaCesLdpGRMode_Type.__name__ = "Integer32"
_CienaCesLdpGRMode_Object = MibScalar
cienaCesLdpGRMode = _CienaCesLdpGRMode_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 6),
    _CienaCesLdpGRMode_Type()
)
cienaCesLdpGRMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpGRMode.setStatus("current")


class _CienaCesLdpReconnectTime_Type(Unsigned32):
    """Custom type cienaCesLdpReconnectTime based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CienaCesLdpReconnectTime_Type.__name__ = "Unsigned32"
_CienaCesLdpReconnectTime_Object = MibScalar
cienaCesLdpReconnectTime = _CienaCesLdpReconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 7),
    _CienaCesLdpReconnectTime_Type()
)
cienaCesLdpReconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpReconnectTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesLdpReconnectTime.setUnits("milliseconds")


class _CienaCesLdpRecoveryTime_Type(Unsigned32):
    """Custom type cienaCesLdpRecoveryTime based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CienaCesLdpRecoveryTime_Type.__name__ = "Unsigned32"
_CienaCesLdpRecoveryTime_Object = MibScalar
cienaCesLdpRecoveryTime = _CienaCesLdpRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 8),
    _CienaCesLdpRecoveryTime_Type()
)
cienaCesLdpRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesLdpRecoveryTime.setUnits("milliseconds")


class _CienaCesLdpMaxPeerReconnect_Type(Unsigned32):
    """Custom type cienaCesLdpMaxPeerReconnect based on Unsigned32"""
    defaultValue = 180000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CienaCesLdpMaxPeerReconnect_Type.__name__ = "Unsigned32"
_CienaCesLdpMaxPeerReconnect_Object = MibScalar
cienaCesLdpMaxPeerReconnect = _CienaCesLdpMaxPeerReconnect_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 9),
    _CienaCesLdpMaxPeerReconnect_Type()
)
cienaCesLdpMaxPeerReconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpMaxPeerReconnect.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesLdpMaxPeerReconnect.setUnits("milliseconds")


class _CienaCesLdpMaxPeerRecovery_Type(Unsigned32):
    """Custom type cienaCesLdpMaxPeerRecovery based on Unsigned32"""
    defaultValue = 240000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600000),
    )


_CienaCesLdpMaxPeerRecovery_Type.__name__ = "Unsigned32"
_CienaCesLdpMaxPeerRecovery_Object = MibScalar
cienaCesLdpMaxPeerRecovery = _CienaCesLdpMaxPeerRecovery_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 1, 10),
    _CienaCesLdpMaxPeerRecovery_Type()
)
cienaCesLdpMaxPeerRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpMaxPeerRecovery.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesLdpMaxPeerRecovery.setUnits("milliseconds")
_CienaCesLdp_ObjectIdentity = ObjectIdentity
cienaCesLdp = _CienaCesLdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2)
)
_CienaCesLdpSessionTable_Object = MibTable
cienaCesLdpSessionTable = _CienaCesLdpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesLdpSessionTable.setStatus("current")
_CienaCesLdpSessionEntry_Object = MibTableRow
cienaCesLdpSessionEntry = _CienaCesLdpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1, 1)
)
cienaCesLdpSessionEntry.setIndexNames(
    (0, "CIENA-CES-LDP-MIB", "cienaCesLdpEntityLdpId"),
    (0, "CIENA-CES-LDP-MIB", "cienaCesLdpEntityIndex"),
    (0, "CIENA-CES-LDP-MIB", "cienaCesLdpPeerLdpId"),
)
if mibBuilder.loadTexts:
    cienaCesLdpSessionEntry.setStatus("current")
_CienaCesLdpEntityLdpId_Type = MplsLdpIdentifier
_CienaCesLdpEntityLdpId_Object = MibTableColumn
cienaCesLdpEntityLdpId = _CienaCesLdpEntityLdpId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1, 1, 1),
    _CienaCesLdpEntityLdpId_Type()
)
cienaCesLdpEntityLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesLdpEntityLdpId.setStatus("current")
_CienaCesLdpEntityIndex_Type = Unsigned32
_CienaCesLdpEntityIndex_Object = MibTableColumn
cienaCesLdpEntityIndex = _CienaCesLdpEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1, 1, 2),
    _CienaCesLdpEntityIndex_Type()
)
cienaCesLdpEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesLdpEntityIndex.setStatus("current")
_CienaCesLdpPeerLdpId_Type = MplsLdpIdentifier
_CienaCesLdpPeerLdpId_Object = MibTableColumn
cienaCesLdpPeerLdpId = _CienaCesLdpPeerLdpId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1, 1, 3),
    _CienaCesLdpPeerLdpId_Type()
)
cienaCesLdpPeerLdpId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesLdpPeerLdpId.setStatus("current")
_CienaCesLdpSessionConfiguredHoldTime_Type = Unsigned32
_CienaCesLdpSessionConfiguredHoldTime_Object = MibTableColumn
cienaCesLdpSessionConfiguredHoldTime = _CienaCesLdpSessionConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1, 1, 4),
    _CienaCesLdpSessionConfiguredHoldTime_Type()
)
cienaCesLdpSessionConfiguredHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpSessionConfiguredHoldTime.setStatus("current")
_CienaCesLdpSessionPeerHoldTime_Type = Unsigned32
_CienaCesLdpSessionPeerHoldTime_Object = MibTableColumn
cienaCesLdpSessionPeerHoldTime = _CienaCesLdpSessionPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1, 1, 5),
    _CienaCesLdpSessionPeerHoldTime_Type()
)
cienaCesLdpSessionPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpSessionPeerHoldTime.setStatus("current")
_CienaCesLdpSessionHoldTimeInUse_Type = Unsigned32
_CienaCesLdpSessionHoldTimeInUse_Object = MibTableColumn
cienaCesLdpSessionHoldTimeInUse = _CienaCesLdpSessionHoldTimeInUse_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 1, 1, 6),
    _CienaCesLdpSessionHoldTimeInUse_Type()
)
cienaCesLdpSessionHoldTimeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpSessionHoldTimeInUse.setStatus("current")
_CienaCesLdpHelloAdjacencyTable_Object = MibTable
cienaCesLdpHelloAdjacencyTable = _CienaCesLdpHelloAdjacencyTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesLdpHelloAdjacencyTable.setStatus("current")
_CienaCesLdpHelloAdjacencyEntry_Object = MibTableRow
cienaCesLdpHelloAdjacencyEntry = _CienaCesLdpHelloAdjacencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 2, 1)
)
cienaCesLdpHelloAdjacencyEntry.setIndexNames(
    (0, "CIENA-CES-LDP-MIB", "cienaCesLdpEntityLdpId"),
    (0, "CIENA-CES-LDP-MIB", "cienaCesLdpEntityIndex"),
    (0, "CIENA-CES-LDP-MIB", "cienaCesLdpPeerLdpId"),
    (0, "CIENA-CES-LDP-MIB", "cienaCesLdpHelloAdjacencyIndex"),
)
if mibBuilder.loadTexts:
    cienaCesLdpHelloAdjacencyEntry.setStatus("current")


class _CienaCesLdpHelloAdjacencyIndex_Type(Unsigned32):
    """Custom type cienaCesLdpHelloAdjacencyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CienaCesLdpHelloAdjacencyIndex_Type.__name__ = "Unsigned32"
_CienaCesLdpHelloAdjacencyIndex_Object = MibTableColumn
cienaCesLdpHelloAdjacencyIndex = _CienaCesLdpHelloAdjacencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 2, 1, 1),
    _CienaCesLdpHelloAdjacencyIndex_Type()
)
cienaCesLdpHelloAdjacencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesLdpHelloAdjacencyIndex.setStatus("current")
_CienaCesLdpHelloAdjacencyConfiguredHoldTime_Type = Unsigned32
_CienaCesLdpHelloAdjacencyConfiguredHoldTime_Object = MibTableColumn
cienaCesLdpHelloAdjacencyConfiguredHoldTime = _CienaCesLdpHelloAdjacencyConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 2, 1, 2),
    _CienaCesLdpHelloAdjacencyConfiguredHoldTime_Type()
)
cienaCesLdpHelloAdjacencyConfiguredHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpHelloAdjacencyConfiguredHoldTime.setStatus("current")
_CienaCesLdpHelloAdjacencyPeerHoldTime_Type = Unsigned32
_CienaCesLdpHelloAdjacencyPeerHoldTime_Object = MibTableColumn
cienaCesLdpHelloAdjacencyPeerHoldTime = _CienaCesLdpHelloAdjacencyPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 17, 1, 2, 2, 1, 3),
    _CienaCesLdpHelloAdjacencyPeerHoldTime_Type()
)
cienaCesLdpHelloAdjacencyPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesLdpHelloAdjacencyPeerHoldTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-LDP-MIB",
    **{"cienaCesLdpMIB": cienaCesLdpMIB,
       "cienaCesLdpMIBObjects": cienaCesLdpMIBObjects,
       "cienaCesLdpObjects": cienaCesLdpObjects,
       "cienaCesLdpAdminStatus": cienaCesLdpAdminStatus,
       "cienaCesLdpOperStatus": cienaCesLdpOperStatus,
       "cienaCesLdpHelloHoldTime": cienaCesLdpHelloHoldTime,
       "cienaCesLdpKeepAliveHoldTime": cienaCesLdpKeepAliveHoldTime,
       "cienaCesLdpGRAdminStatus": cienaCesLdpGRAdminStatus,
       "cienaCesLdpGRMode": cienaCesLdpGRMode,
       "cienaCesLdpReconnectTime": cienaCesLdpReconnectTime,
       "cienaCesLdpRecoveryTime": cienaCesLdpRecoveryTime,
       "cienaCesLdpMaxPeerReconnect": cienaCesLdpMaxPeerReconnect,
       "cienaCesLdpMaxPeerRecovery": cienaCesLdpMaxPeerRecovery,
       "cienaCesLdp": cienaCesLdp,
       "cienaCesLdpSessionTable": cienaCesLdpSessionTable,
       "cienaCesLdpSessionEntry": cienaCesLdpSessionEntry,
       "cienaCesLdpEntityLdpId": cienaCesLdpEntityLdpId,
       "cienaCesLdpEntityIndex": cienaCesLdpEntityIndex,
       "cienaCesLdpPeerLdpId": cienaCesLdpPeerLdpId,
       "cienaCesLdpSessionConfiguredHoldTime": cienaCesLdpSessionConfiguredHoldTime,
       "cienaCesLdpSessionPeerHoldTime": cienaCesLdpSessionPeerHoldTime,
       "cienaCesLdpSessionHoldTimeInUse": cienaCesLdpSessionHoldTimeInUse,
       "cienaCesLdpHelloAdjacencyTable": cienaCesLdpHelloAdjacencyTable,
       "cienaCesLdpHelloAdjacencyEntry": cienaCesLdpHelloAdjacencyEntry,
       "cienaCesLdpHelloAdjacencyIndex": cienaCesLdpHelloAdjacencyIndex,
       "cienaCesLdpHelloAdjacencyConfiguredHoldTime": cienaCesLdpHelloAdjacencyConfiguredHoldTime,
       "cienaCesLdpHelloAdjacencyPeerHoldTime": cienaCesLdpHelloAdjacencyPeerHoldTime}
)
