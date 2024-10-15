# SNMP MIB module (STN-PPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STN-PPTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:13 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(stnTmpProtocols,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-SMI",
    "stnTmpProtocols")

(StnDomainMapType,) = mibBuilder.importSymbols(
    "SPRING-TIDE-NETWORKS-TC",
    "StnDomainMapType")


# MODULE-IDENTITY

stnPptp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliSeconds(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-3"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483646),
    )



# MIB Managed Objects in the order of their OIDs

_StnPptpObjects_ObjectIdentity = ObjectIdentity
stnPptpObjects = _StnPptpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1)
)
_StnPptpScalar_ObjectIdentity = ObjectIdentity
stnPptpScalar = _StnPptpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 1)
)
_StnPptpConfig_ObjectIdentity = ObjectIdentity
stnPptpConfig = _StnPptpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 1, 1)
)


class _StnPptpAdminState_Type(Integer32):
    """Custom type stnPptpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("drain", 3),
          ("enabled", 1))
    )


_StnPptpAdminState_Type.__name__ = "Integer32"
_StnPptpAdminState_Object = MibScalar
stnPptpAdminState = _StnPptpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 1, 1, 1),
    _StnPptpAdminState_Type()
)
stnPptpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpAdminState.setStatus("current")
_StnPptpStats_ObjectIdentity = ObjectIdentity
stnPptpStats = _StnPptpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 1, 2)
)


class _StnPptpProtocolVersion_Type(OctetString):
    """Custom type stnPptpProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 256),
    )


_StnPptpProtocolVersion_Type.__name__ = "OctetString"
_StnPptpProtocolVersion_Object = MibScalar
stnPptpProtocolVersion = _StnPptpProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 1, 2, 1),
    _StnPptpProtocolVersion_Type()
)
stnPptpProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpProtocolVersion.setStatus("current")
_StnPptpVendorName_Type = DisplayString
_StnPptpVendorName_Object = MibScalar
stnPptpVendorName = _StnPptpVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 1, 2, 2),
    _StnPptpVendorName_Type()
)
stnPptpVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpVendorName.setStatus("current")
_StnPptpFirmwareRev_Type = Integer32
_StnPptpFirmwareRev_Object = MibScalar
stnPptpFirmwareRev = _StnPptpFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 1, 2, 3),
    _StnPptpFirmwareRev_Type()
)
stnPptpFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpFirmwareRev.setStatus("current")
_StnPptpDomainConfigTable_Object = MibTable
stnPptpDomainConfigTable = _StnPptpDomainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2)
)
if mibBuilder.loadTexts:
    stnPptpDomainConfigTable.setStatus("current")
_StnPptpDomainConfigEntry_Object = MibTableRow
stnPptpDomainConfigEntry = _StnPptpDomainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1)
)
stnPptpDomainConfigEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpDomainConfigIdentifier"),
)
if mibBuilder.loadTexts:
    stnPptpDomainConfigEntry.setStatus("current")
_StnPptpDomainConfigIdentifier_Type = DisplayString
_StnPptpDomainConfigIdentifier_Object = MibTableColumn
stnPptpDomainConfigIdentifier = _StnPptpDomainConfigIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 1),
    _StnPptpDomainConfigIdentifier_Type()
)
stnPptpDomainConfigIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnPptpDomainConfigIdentifier.setStatus("current")


class _StnPptpDomainConfigAdminState_Type(Integer32):
    """Custom type stnPptpDomainConfigAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("drain", 3),
          ("enabled", 1))
    )


_StnPptpDomainConfigAdminState_Type.__name__ = "Integer32"
_StnPptpDomainConfigAdminState_Object = MibTableColumn
stnPptpDomainConfigAdminState = _StnPptpDomainConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 2),
    _StnPptpDomainConfigAdminState_Type()
)
stnPptpDomainConfigAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigAdminState.setStatus("current")


class _StnPptpDomainConfigAuthentication_Type(Integer32):
    """Custom type stnPptpDomainConfigAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("challenge", 3),
          ("none", 1),
          ("simple", 2))
    )


_StnPptpDomainConfigAuthentication_Type.__name__ = "Integer32"
_StnPptpDomainConfigAuthentication_Object = MibTableColumn
stnPptpDomainConfigAuthentication = _StnPptpDomainConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 3),
    _StnPptpDomainConfigAuthentication_Type()
)
stnPptpDomainConfigAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigAuthentication.setStatus("current")


class _StnPptpDomainConfigSecret_Type(OctetString):
    """Custom type stnPptpDomainConfigSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnPptpDomainConfigSecret_Type.__name__ = "OctetString"
_StnPptpDomainConfigSecret_Object = MibTableColumn
stnPptpDomainConfigSecret = _StnPptpDomainConfigSecret_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 4),
    _StnPptpDomainConfigSecret_Type()
)
stnPptpDomainConfigSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigSecret.setStatus("current")


class _StnPptpDomainConfigTunnelSecurity_Type(Integer32):
    """Custom type stnPptpDomainConfigTunnelSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipSec", 3),
          ("none", 1),
          ("other", 2))
    )


_StnPptpDomainConfigTunnelSecurity_Type.__name__ = "Integer32"
_StnPptpDomainConfigTunnelSecurity_Object = MibTableColumn
stnPptpDomainConfigTunnelSecurity = _StnPptpDomainConfigTunnelSecurity_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 5),
    _StnPptpDomainConfigTunnelSecurity_Type()
)
stnPptpDomainConfigTunnelSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigTunnelSecurity.setStatus("current")


class _StnPptpDomainConfigTunnelHelloInterval_Type(Integer32):
    """Custom type stnPptpDomainConfigTunnelHelloInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_StnPptpDomainConfigTunnelHelloInterval_Type.__name__ = "Integer32"
_StnPptpDomainConfigTunnelHelloInterval_Object = MibTableColumn
stnPptpDomainConfigTunnelHelloInterval = _StnPptpDomainConfigTunnelHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 6),
    _StnPptpDomainConfigTunnelHelloInterval_Type()
)
stnPptpDomainConfigTunnelHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigTunnelHelloInterval.setStatus("current")


class _StnPptpDomainConfigTunnelIdleTimeout_Type(Integer32):
    """Custom type stnPptpDomainConfigTunnelIdleTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_StnPptpDomainConfigTunnelIdleTimeout_Type.__name__ = "Integer32"
_StnPptpDomainConfigTunnelIdleTimeout_Object = MibTableColumn
stnPptpDomainConfigTunnelIdleTimeout = _StnPptpDomainConfigTunnelIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 7),
    _StnPptpDomainConfigTunnelIdleTimeout_Type()
)
stnPptpDomainConfigTunnelIdleTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigTunnelIdleTimeout.setStatus("current")


class _StnPptpDomainConfigControlRWS_Type(Integer32):
    """Custom type stnPptpDomainConfigControlRWS based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_StnPptpDomainConfigControlRWS_Type.__name__ = "Integer32"
_StnPptpDomainConfigControlRWS_Object = MibTableColumn
stnPptpDomainConfigControlRWS = _StnPptpDomainConfigControlRWS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 8),
    _StnPptpDomainConfigControlRWS_Type()
)
stnPptpDomainConfigControlRWS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigControlRWS.setStatus("current")


class _StnPptpDomainConfigControlRetransmissions_Type(Integer32):
    """Custom type stnPptpDomainConfigControlRetransmissions based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_StnPptpDomainConfigControlRetransmissions_Type.__name__ = "Integer32"
_StnPptpDomainConfigControlRetransmissions_Object = MibTableColumn
stnPptpDomainConfigControlRetransmissions = _StnPptpDomainConfigControlRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 9),
    _StnPptpDomainConfigControlRetransmissions_Type()
)
stnPptpDomainConfigControlRetransmissions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigControlRetransmissions.setStatus("current")


class _StnPptpDomainConfigPayloadSequencing_Type(TruthValue):
    """Custom type stnPptpDomainConfigPayloadSequencing based on TruthValue"""


_StnPptpDomainConfigPayloadSequencing_Object = MibTableColumn
stnPptpDomainConfigPayloadSequencing = _StnPptpDomainConfigPayloadSequencing_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 10),
    _StnPptpDomainConfigPayloadSequencing_Type()
)
stnPptpDomainConfigPayloadSequencing.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigPayloadSequencing.setStatus("current")


class _StnPptpDomainConfigPayloadRWS_Type(Integer32):
    """Custom type stnPptpDomainConfigPayloadRWS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpDomainConfigPayloadRWS_Type.__name__ = "Integer32"
_StnPptpDomainConfigPayloadRWS_Object = MibTableColumn
stnPptpDomainConfigPayloadRWS = _StnPptpDomainConfigPayloadRWS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 11),
    _StnPptpDomainConfigPayloadRWS_Type()
)
stnPptpDomainConfigPayloadRWS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigPayloadRWS.setStatus("current")


class _StnPptpDomainConfigDelayedAckTimeout_Type(MilliSeconds):
    """Custom type stnPptpDomainConfigDelayedAckTimeout based on MilliSeconds"""
    defaultValue = 0


_StnPptpDomainConfigDelayedAckTimeout_Object = MibTableColumn
stnPptpDomainConfigDelayedAckTimeout = _StnPptpDomainConfigDelayedAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 12),
    _StnPptpDomainConfigDelayedAckTimeout_Type()
)
stnPptpDomainConfigDelayedAckTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigDelayedAckTimeout.setStatus("current")


class _StnPptpDomainConfigReassemblyTimeout_Type(MilliSeconds):
    """Custom type stnPptpDomainConfigReassemblyTimeout based on MilliSeconds"""
    defaultValue = 0


_StnPptpDomainConfigReassemblyTimeout_Object = MibTableColumn
stnPptpDomainConfigReassemblyTimeout = _StnPptpDomainConfigReassemblyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 13),
    _StnPptpDomainConfigReassemblyTimeout_Type()
)
stnPptpDomainConfigReassemblyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigReassemblyTimeout.setStatus("current")
_StnPptpDomainConfigStatus_Type = RowStatus
_StnPptpDomainConfigStatus_Object = MibTableColumn
stnPptpDomainConfigStatus = _StnPptpDomainConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 2, 1, 14),
    _StnPptpDomainConfigStatus_Type()
)
stnPptpDomainConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    stnPptpDomainConfigStatus.setStatus("current")
_StnPptpDomainStatsTable_Object = MibTable
stnPptpDomainStatsTable = _StnPptpDomainStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3)
)
if mibBuilder.loadTexts:
    stnPptpDomainStatsTable.setStatus("current")
_StnPptpDomainStatsEntry_Object = MibTableRow
stnPptpDomainStatsEntry = _StnPptpDomainStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1)
)
stnPptpDomainStatsEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpDomainStatsIdentifier"),
)
if mibBuilder.loadTexts:
    stnPptpDomainStatsEntry.setStatus("current")
_StnPptpDomainStatsIdentifier_Type = DisplayString
_StnPptpDomainStatsIdentifier_Object = MibTableColumn
stnPptpDomainStatsIdentifier = _StnPptpDomainStatsIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 1),
    _StnPptpDomainStatsIdentifier_Type()
)
stnPptpDomainStatsIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnPptpDomainStatsIdentifier.setStatus("current")
_StnPptpDomainStatsTotalTunnels_Type = Counter32
_StnPptpDomainStatsTotalTunnels_Object = MibTableColumn
stnPptpDomainStatsTotalTunnels = _StnPptpDomainStatsTotalTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 2),
    _StnPptpDomainStatsTotalTunnels_Type()
)
stnPptpDomainStatsTotalTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsTotalTunnels.setStatus("current")
_StnPptpDomainStatsFailedTunnels_Type = Counter32
_StnPptpDomainStatsFailedTunnels_Object = MibTableColumn
stnPptpDomainStatsFailedTunnels = _StnPptpDomainStatsFailedTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 3),
    _StnPptpDomainStatsFailedTunnels_Type()
)
stnPptpDomainStatsFailedTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsFailedTunnels.setStatus("current")
_StnPptpDomainStatsFailedAuthentications_Type = Counter32
_StnPptpDomainStatsFailedAuthentications_Object = MibTableColumn
stnPptpDomainStatsFailedAuthentications = _StnPptpDomainStatsFailedAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 4),
    _StnPptpDomainStatsFailedAuthentications_Type()
)
stnPptpDomainStatsFailedAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsFailedAuthentications.setStatus("current")
_StnPptpDomainStatsActiveTunnels_Type = Gauge32
_StnPptpDomainStatsActiveTunnels_Object = MibTableColumn
stnPptpDomainStatsActiveTunnels = _StnPptpDomainStatsActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 5),
    _StnPptpDomainStatsActiveTunnels_Type()
)
stnPptpDomainStatsActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsActiveTunnels.setStatus("current")
_StnPptpDomainStatsTotalSessions_Type = Counter32
_StnPptpDomainStatsTotalSessions_Object = MibTableColumn
stnPptpDomainStatsTotalSessions = _StnPptpDomainStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 6),
    _StnPptpDomainStatsTotalSessions_Type()
)
stnPptpDomainStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsTotalSessions.setStatus("current")
_StnPptpDomainStatsFailedSessions_Type = Counter32
_StnPptpDomainStatsFailedSessions_Object = MibTableColumn
stnPptpDomainStatsFailedSessions = _StnPptpDomainStatsFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 7),
    _StnPptpDomainStatsFailedSessions_Type()
)
stnPptpDomainStatsFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsFailedSessions.setStatus("current")
_StnPptpDomainStatsActiveSessions_Type = Gauge32
_StnPptpDomainStatsActiveSessions_Object = MibTableColumn
stnPptpDomainStatsActiveSessions = _StnPptpDomainStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 8),
    _StnPptpDomainStatsActiveSessions_Type()
)
stnPptpDomainStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsActiveSessions.setStatus("current")
_StnPptpDomainStatsControlRecvOctets_Type = Counter32
_StnPptpDomainStatsControlRecvOctets_Object = MibTableColumn
stnPptpDomainStatsControlRecvOctets = _StnPptpDomainStatsControlRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 9),
    _StnPptpDomainStatsControlRecvOctets_Type()
)
stnPptpDomainStatsControlRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsControlRecvOctets.setStatus("current")
_StnPptpDomainStatsControlRecvPackets_Type = Counter32
_StnPptpDomainStatsControlRecvPackets_Object = MibTableColumn
stnPptpDomainStatsControlRecvPackets = _StnPptpDomainStatsControlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 10),
    _StnPptpDomainStatsControlRecvPackets_Type()
)
stnPptpDomainStatsControlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsControlRecvPackets.setStatus("current")
_StnPptpDomainStatsControlSendOctets_Type = Counter32
_StnPptpDomainStatsControlSendOctets_Object = MibTableColumn
stnPptpDomainStatsControlSendOctets = _StnPptpDomainStatsControlSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 11),
    _StnPptpDomainStatsControlSendOctets_Type()
)
stnPptpDomainStatsControlSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsControlSendOctets.setStatus("current")
_StnPptpDomainStatsControlSendPackets_Type = Counter32
_StnPptpDomainStatsControlSendPackets_Object = MibTableColumn
stnPptpDomainStatsControlSendPackets = _StnPptpDomainStatsControlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 12),
    _StnPptpDomainStatsControlSendPackets_Type()
)
stnPptpDomainStatsControlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsControlSendPackets.setStatus("current")
_StnPptpDomainStatsPayloadRecvOctets_Type = Counter32
_StnPptpDomainStatsPayloadRecvOctets_Object = MibTableColumn
stnPptpDomainStatsPayloadRecvOctets = _StnPptpDomainStatsPayloadRecvOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 13),
    _StnPptpDomainStatsPayloadRecvOctets_Type()
)
stnPptpDomainStatsPayloadRecvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsPayloadRecvOctets.setStatus("current")
_StnPptpDomainStatsPayloadRecvPackets_Type = Counter32
_StnPptpDomainStatsPayloadRecvPackets_Object = MibTableColumn
stnPptpDomainStatsPayloadRecvPackets = _StnPptpDomainStatsPayloadRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 14),
    _StnPptpDomainStatsPayloadRecvPackets_Type()
)
stnPptpDomainStatsPayloadRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsPayloadRecvPackets.setStatus("current")
_StnPptpDomainStatsPayloadRecvDiscards_Type = Counter32
_StnPptpDomainStatsPayloadRecvDiscards_Object = MibTableColumn
stnPptpDomainStatsPayloadRecvDiscards = _StnPptpDomainStatsPayloadRecvDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 15),
    _StnPptpDomainStatsPayloadRecvDiscards_Type()
)
stnPptpDomainStatsPayloadRecvDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsPayloadRecvDiscards.setStatus("current")
_StnPptpDomainStatsPayloadSendOctets_Type = Counter32
_StnPptpDomainStatsPayloadSendOctets_Object = MibTableColumn
stnPptpDomainStatsPayloadSendOctets = _StnPptpDomainStatsPayloadSendOctets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 16),
    _StnPptpDomainStatsPayloadSendOctets_Type()
)
stnPptpDomainStatsPayloadSendOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsPayloadSendOctets.setStatus("current")
_StnPptpDomainStatsPayloadSendPackets_Type = Counter32
_StnPptpDomainStatsPayloadSendPackets_Object = MibTableColumn
stnPptpDomainStatsPayloadSendPackets = _StnPptpDomainStatsPayloadSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 3, 1, 17),
    _StnPptpDomainStatsPayloadSendPackets_Type()
)
stnPptpDomainStatsPayloadSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainStatsPayloadSendPackets.setStatus("current")
_StnPptpTunnelConfigTable_Object = MibTable
stnPptpTunnelConfigTable = _StnPptpTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4)
)
if mibBuilder.loadTexts:
    stnPptpTunnelConfigTable.setStatus("current")
_StnPptpTunnelConfigEntry_Object = MibTableRow
stnPptpTunnelConfigEntry = _StnPptpTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1)
)
stnPptpTunnelConfigEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpTunnelConfigIfIndex"),
)
if mibBuilder.loadTexts:
    stnPptpTunnelConfigEntry.setStatus("current")
_StnPptpTunnelConfigIfIndex_Type = InterfaceIndex
_StnPptpTunnelConfigIfIndex_Object = MibTableColumn
stnPptpTunnelConfigIfIndex = _StnPptpTunnelConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 1),
    _StnPptpTunnelConfigIfIndex_Type()
)
stnPptpTunnelConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigIfIndex.setStatus("current")


class _StnPptpTunnelConfigAuthentication_Type(Integer32):
    """Custom type stnPptpTunnelConfigAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("challenge", 3),
          ("none", 1),
          ("simple", 2))
    )


_StnPptpTunnelConfigAuthentication_Type.__name__ = "Integer32"
_StnPptpTunnelConfigAuthentication_Object = MibTableColumn
stnPptpTunnelConfigAuthentication = _StnPptpTunnelConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 2),
    _StnPptpTunnelConfigAuthentication_Type()
)
stnPptpTunnelConfigAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigAuthentication.setStatus("current")


class _StnPptpTunnelConfigSecret_Type(OctetString):
    """Custom type stnPptpTunnelConfigSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_StnPptpTunnelConfigSecret_Type.__name__ = "OctetString"
_StnPptpTunnelConfigSecret_Object = MibTableColumn
stnPptpTunnelConfigSecret = _StnPptpTunnelConfigSecret_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 3),
    _StnPptpTunnelConfigSecret_Type()
)
stnPptpTunnelConfigSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigSecret.setStatus("current")


class _StnPptpTunnelConfigSecurity_Type(Integer32):
    """Custom type stnPptpTunnelConfigSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ipsec", 3),
          ("none", 1),
          ("other", 2))
    )


_StnPptpTunnelConfigSecurity_Type.__name__ = "Integer32"
_StnPptpTunnelConfigSecurity_Object = MibTableColumn
stnPptpTunnelConfigSecurity = _StnPptpTunnelConfigSecurity_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 4),
    _StnPptpTunnelConfigSecurity_Type()
)
stnPptpTunnelConfigSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigSecurity.setStatus("current")


class _StnPptpTunnelConfigHelloInterval_Type(Integer32):
    """Custom type stnPptpTunnelConfigHelloInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_StnPptpTunnelConfigHelloInterval_Type.__name__ = "Integer32"
_StnPptpTunnelConfigHelloInterval_Object = MibTableColumn
stnPptpTunnelConfigHelloInterval = _StnPptpTunnelConfigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 5),
    _StnPptpTunnelConfigHelloInterval_Type()
)
stnPptpTunnelConfigHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigHelloInterval.setStatus("current")


class _StnPptpTunnelConfigIdleTimeout_Type(Integer32):
    """Custom type stnPptpTunnelConfigIdleTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_StnPptpTunnelConfigIdleTimeout_Type.__name__ = "Integer32"
_StnPptpTunnelConfigIdleTimeout_Object = MibTableColumn
stnPptpTunnelConfigIdleTimeout = _StnPptpTunnelConfigIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 6),
    _StnPptpTunnelConfigIdleTimeout_Type()
)
stnPptpTunnelConfigIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigIdleTimeout.setStatus("current")


class _StnPptpTunnelConfigControlRWS_Type(Integer32):
    """Custom type stnPptpTunnelConfigControlRWS based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_StnPptpTunnelConfigControlRWS_Type.__name__ = "Integer32"
_StnPptpTunnelConfigControlRWS_Object = MibTableColumn
stnPptpTunnelConfigControlRWS = _StnPptpTunnelConfigControlRWS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 7),
    _StnPptpTunnelConfigControlRWS_Type()
)
stnPptpTunnelConfigControlRWS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigControlRWS.setStatus("current")


class _StnPptpTunnelConfigControlRetransmissions_Type(Integer32):
    """Custom type stnPptpTunnelConfigControlRetransmissions based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_StnPptpTunnelConfigControlRetransmissions_Type.__name__ = "Integer32"
_StnPptpTunnelConfigControlRetransmissions_Object = MibTableColumn
stnPptpTunnelConfigControlRetransmissions = _StnPptpTunnelConfigControlRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 8),
    _StnPptpTunnelConfigControlRetransmissions_Type()
)
stnPptpTunnelConfigControlRetransmissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigControlRetransmissions.setStatus("current")


class _StnPptpTunnelConfigPayloadSequencing_Type(TruthValue):
    """Custom type stnPptpTunnelConfigPayloadSequencing based on TruthValue"""


_StnPptpTunnelConfigPayloadSequencing_Object = MibTableColumn
stnPptpTunnelConfigPayloadSequencing = _StnPptpTunnelConfigPayloadSequencing_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 9),
    _StnPptpTunnelConfigPayloadSequencing_Type()
)
stnPptpTunnelConfigPayloadSequencing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigPayloadSequencing.setStatus("current")


class _StnPptpTunnelConfigPayloadRWS_Type(Integer32):
    """Custom type stnPptpTunnelConfigPayloadRWS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpTunnelConfigPayloadRWS_Type.__name__ = "Integer32"
_StnPptpTunnelConfigPayloadRWS_Object = MibTableColumn
stnPptpTunnelConfigPayloadRWS = _StnPptpTunnelConfigPayloadRWS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 10),
    _StnPptpTunnelConfigPayloadRWS_Type()
)
stnPptpTunnelConfigPayloadRWS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigPayloadRWS.setStatus("current")


class _StnPptpTunnelConfigDelayedAckTimeout_Type(MilliSeconds):
    """Custom type stnPptpTunnelConfigDelayedAckTimeout based on MilliSeconds"""
    defaultValue = 0


_StnPptpTunnelConfigDelayedAckTimeout_Object = MibTableColumn
stnPptpTunnelConfigDelayedAckTimeout = _StnPptpTunnelConfigDelayedAckTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 11),
    _StnPptpTunnelConfigDelayedAckTimeout_Type()
)
stnPptpTunnelConfigDelayedAckTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigDelayedAckTimeout.setStatus("current")


class _StnPptpTunnelConfigReassemblyTimeout_Type(MilliSeconds):
    """Custom type stnPptpTunnelConfigReassemblyTimeout based on MilliSeconds"""
    defaultValue = 0


_StnPptpTunnelConfigReassemblyTimeout_Object = MibTableColumn
stnPptpTunnelConfigReassemblyTimeout = _StnPptpTunnelConfigReassemblyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 12),
    _StnPptpTunnelConfigReassemblyTimeout_Type()
)
stnPptpTunnelConfigReassemblyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigReassemblyTimeout.setStatus("current")


class _StnPptpTunnelConfigTransport_Type(Integer32):
    """Custom type stnPptpTunnelConfigTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipGre", 1)
    )


_StnPptpTunnelConfigTransport_Type.__name__ = "Integer32"
_StnPptpTunnelConfigTransport_Object = MibTableColumn
stnPptpTunnelConfigTransport = _StnPptpTunnelConfigTransport_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 4, 1, 13),
    _StnPptpTunnelConfigTransport_Type()
)
stnPptpTunnelConfigTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stnPptpTunnelConfigTransport.setStatus("current")
_StnPptpTunnelStatsTable_Object = MibTable
stnPptpTunnelStatsTable = _StnPptpTunnelStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5)
)
if mibBuilder.loadTexts:
    stnPptpTunnelStatsTable.setStatus("current")
_StnPptpTunnelStatsEntry_Object = MibTableRow
stnPptpTunnelStatsEntry = _StnPptpTunnelStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1)
)
stnPptpTunnelStatsEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpTunnelStatsIfIndex"),
)
if mibBuilder.loadTexts:
    stnPptpTunnelStatsEntry.setStatus("current")
_StnPptpTunnelStatsIfIndex_Type = InterfaceIndex
_StnPptpTunnelStatsIfIndex_Object = MibTableColumn
stnPptpTunnelStatsIfIndex = _StnPptpTunnelStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 1),
    _StnPptpTunnelStatsIfIndex_Type()
)
stnPptpTunnelStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsIfIndex.setStatus("current")


class _StnPptpTunnelStatsLocalTID_Type(Integer32):
    """Custom type stnPptpTunnelStatsLocalTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpTunnelStatsLocalTID_Type.__name__ = "Integer32"
_StnPptpTunnelStatsLocalTID_Object = MibTableColumn
stnPptpTunnelStatsLocalTID = _StnPptpTunnelStatsLocalTID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 2),
    _StnPptpTunnelStatsLocalTID_Type()
)
stnPptpTunnelStatsLocalTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsLocalTID.setStatus("current")


class _StnPptpTunnelStatsState_Type(Integer32):
    """Custom type stnPptpTunnelStatsState based on Integer32"""
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
        *(("tunnelConnecting", 2),
          ("tunnelDisconnecting", 4),
          ("tunnelEstablished", 3),
          ("tunnelIdle", 1))
    )


_StnPptpTunnelStatsState_Type.__name__ = "Integer32"
_StnPptpTunnelStatsState_Object = MibTableColumn
stnPptpTunnelStatsState = _StnPptpTunnelStatsState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 3),
    _StnPptpTunnelStatsState_Type()
)
stnPptpTunnelStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsState.setStatus("current")


class _StnPptpTunnelStatsInitiated_Type(Integer32):
    """Custom type stnPptpTunnelStatsInitiated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locally", 1),
          ("remotely", 2))
    )


_StnPptpTunnelStatsInitiated_Type.__name__ = "Integer32"
_StnPptpTunnelStatsInitiated_Object = MibTableColumn
stnPptpTunnelStatsInitiated = _StnPptpTunnelStatsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 4),
    _StnPptpTunnelStatsInitiated_Type()
)
stnPptpTunnelStatsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsInitiated.setStatus("current")
_StnPptpTunnelStatsRemoteHostName_Type = DisplayString
_StnPptpTunnelStatsRemoteHostName_Object = MibTableColumn
stnPptpTunnelStatsRemoteHostName = _StnPptpTunnelStatsRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 5),
    _StnPptpTunnelStatsRemoteHostName_Type()
)
stnPptpTunnelStatsRemoteHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsRemoteHostName.setStatus("current")
_StnPptpTunnelStatsRemoteVendorName_Type = DisplayString
_StnPptpTunnelStatsRemoteVendorName_Object = MibTableColumn
stnPptpTunnelStatsRemoteVendorName = _StnPptpTunnelStatsRemoteVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 6),
    _StnPptpTunnelStatsRemoteVendorName_Type()
)
stnPptpTunnelStatsRemoteVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsRemoteVendorName.setStatus("current")
_StnPptpTunnelStatsRemoteFirmwareRevision_Type = Integer32
_StnPptpTunnelStatsRemoteFirmwareRevision_Object = MibTableColumn
stnPptpTunnelStatsRemoteFirmwareRevision = _StnPptpTunnelStatsRemoteFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 7),
    _StnPptpTunnelStatsRemoteFirmwareRevision_Type()
)
stnPptpTunnelStatsRemoteFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsRemoteFirmwareRevision.setStatus("current")


class _StnPptpTunnelStatsRemoteProtocolVersion_Type(OctetString):
    """Custom type stnPptpTunnelStatsRemoteProtocolVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_StnPptpTunnelStatsRemoteProtocolVersion_Type.__name__ = "OctetString"
_StnPptpTunnelStatsRemoteProtocolVersion_Object = MibTableColumn
stnPptpTunnelStatsRemoteProtocolVersion = _StnPptpTunnelStatsRemoteProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 8),
    _StnPptpTunnelStatsRemoteProtocolVersion_Type()
)
stnPptpTunnelStatsRemoteProtocolVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsRemoteProtocolVersion.setStatus("current")


class _StnPptpTunnelStatsBearerCapabilities_Type(Integer32):
    """Custom type stnPptpTunnelStatsBearerCapabilities based on Integer32"""
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
        *(("analog", 3),
          ("digital", 2),
          ("digitalAnalog", 4),
          ("none", 1))
    )


_StnPptpTunnelStatsBearerCapabilities_Type.__name__ = "Integer32"
_StnPptpTunnelStatsBearerCapabilities_Object = MibTableColumn
stnPptpTunnelStatsBearerCapabilities = _StnPptpTunnelStatsBearerCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 9),
    _StnPptpTunnelStatsBearerCapabilities_Type()
)
stnPptpTunnelStatsBearerCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsBearerCapabilities.setStatus("current")


class _StnPptpTunnelStatsFramingCapabilities_Type(Integer32):
    """Custom type stnPptpTunnelStatsFramingCapabilities based on Integer32"""
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
        *(("async", 3),
          ("none", 1),
          ("sync", 2),
          ("syncAsync", 4))
    )


_StnPptpTunnelStatsFramingCapabilities_Type.__name__ = "Integer32"
_StnPptpTunnelStatsFramingCapabilities_Object = MibTableColumn
stnPptpTunnelStatsFramingCapabilities = _StnPptpTunnelStatsFramingCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 10),
    _StnPptpTunnelStatsFramingCapabilities_Type()
)
stnPptpTunnelStatsFramingCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsFramingCapabilities.setStatus("current")
_StnPptpTunnelStatsControlRecvPackets_Type = Counter32
_StnPptpTunnelStatsControlRecvPackets_Object = MibTableColumn
stnPptpTunnelStatsControlRecvPackets = _StnPptpTunnelStatsControlRecvPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 11),
    _StnPptpTunnelStatsControlRecvPackets_Type()
)
stnPptpTunnelStatsControlRecvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsControlRecvPackets.setStatus("current")
_StnPptpTunnelStatsControlSendPackets_Type = Counter32
_StnPptpTunnelStatsControlSendPackets_Object = MibTableColumn
stnPptpTunnelStatsControlSendPackets = _StnPptpTunnelStatsControlSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 12),
    _StnPptpTunnelStatsControlSendPackets_Type()
)
stnPptpTunnelStatsControlSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsControlSendPackets.setStatus("current")
_StnPptpTunnelStatsTotalSessions_Type = Counter32
_StnPptpTunnelStatsTotalSessions_Object = MibTableColumn
stnPptpTunnelStatsTotalSessions = _StnPptpTunnelStatsTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 13),
    _StnPptpTunnelStatsTotalSessions_Type()
)
stnPptpTunnelStatsTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsTotalSessions.setStatus("current")
_StnPptpTunnelStatsFailedSessions_Type = Counter32
_StnPptpTunnelStatsFailedSessions_Object = MibTableColumn
stnPptpTunnelStatsFailedSessions = _StnPptpTunnelStatsFailedSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 14),
    _StnPptpTunnelStatsFailedSessions_Type()
)
stnPptpTunnelStatsFailedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsFailedSessions.setStatus("current")
_StnPptpTunnelStatsActiveSessions_Type = Gauge32
_StnPptpTunnelStatsActiveSessions_Object = MibTableColumn
stnPptpTunnelStatsActiveSessions = _StnPptpTunnelStatsActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 15),
    _StnPptpTunnelStatsActiveSessions_Type()
)
stnPptpTunnelStatsActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsActiveSessions.setStatus("current")


class _StnPptpTunnelStatsLastResultCode_Type(Integer32):
    """Custom type stnPptpTunnelStatsLastResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpTunnelStatsLastResultCode_Type.__name__ = "Integer32"
_StnPptpTunnelStatsLastResultCode_Object = MibTableColumn
stnPptpTunnelStatsLastResultCode = _StnPptpTunnelStatsLastResultCode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 16),
    _StnPptpTunnelStatsLastResultCode_Type()
)
stnPptpTunnelStatsLastResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsLastResultCode.setStatus("current")


class _StnPptpTunnelStatsLastErrorCode_Type(Integer32):
    """Custom type stnPptpTunnelStatsLastErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpTunnelStatsLastErrorCode_Type.__name__ = "Integer32"
_StnPptpTunnelStatsLastErrorCode_Object = MibTableColumn
stnPptpTunnelStatsLastErrorCode = _StnPptpTunnelStatsLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 17),
    _StnPptpTunnelStatsLastErrorCode_Type()
)
stnPptpTunnelStatsLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsLastErrorCode.setStatus("current")
_StnPptpTunnelStatsLastErrorMessage_Type = DisplayString
_StnPptpTunnelStatsLastErrorMessage_Object = MibTableColumn
stnPptpTunnelStatsLastErrorMessage = _StnPptpTunnelStatsLastErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 5, 1, 18),
    _StnPptpTunnelStatsLastErrorMessage_Type()
)
stnPptpTunnelStatsLastErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelStatsLastErrorMessage.setStatus("current")
_StnPptpSessionStatsTable_Object = MibTable
stnPptpSessionStatsTable = _StnPptpSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7)
)
if mibBuilder.loadTexts:
    stnPptpSessionStatsTable.setStatus("current")
_StnPptpSessionStatsEntry_Object = MibTableRow
stnPptpSessionStatsEntry = _StnPptpSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1)
)
stnPptpSessionStatsEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpSessionStatsTunnelIfIndex"),
    (0, "STN-PPTP-MIB", "stnPptpSessionStatsLocalCID"),
)
if mibBuilder.loadTexts:
    stnPptpSessionStatsEntry.setStatus("current")
_StnPptpSessionStatsTunnelIfIndex_Type = InterfaceIndex
_StnPptpSessionStatsTunnelIfIndex_Object = MibTableColumn
stnPptpSessionStatsTunnelIfIndex = _StnPptpSessionStatsTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 1),
    _StnPptpSessionStatsTunnelIfIndex_Type()
)
stnPptpSessionStatsTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsTunnelIfIndex.setStatus("current")
_StnPptpSessionStatsHLIfIndex_Type = InterfaceIndex
_StnPptpSessionStatsHLIfIndex_Object = MibTableColumn
stnPptpSessionStatsHLIfIndex = _StnPptpSessionStatsHLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 2),
    _StnPptpSessionStatsHLIfIndex_Type()
)
stnPptpSessionStatsHLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsHLIfIndex.setStatus("current")


class _StnPptpSessionStatsLocalCID_Type(Integer32):
    """Custom type stnPptpSessionStatsLocalCID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsLocalCID_Type.__name__ = "Integer32"
_StnPptpSessionStatsLocalCID_Object = MibTableColumn
stnPptpSessionStatsLocalCID = _StnPptpSessionStatsLocalCID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 3),
    _StnPptpSessionStatsLocalCID_Type()
)
stnPptpSessionStatsLocalCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsLocalCID.setStatus("current")


class _StnPptpSessionStatsRemoteCID_Type(Integer32):
    """Custom type stnPptpSessionStatsRemoteCID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsRemoteCID_Type.__name__ = "Integer32"
_StnPptpSessionStatsRemoteCID_Object = MibTableColumn
stnPptpSessionStatsRemoteCID = _StnPptpSessionStatsRemoteCID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 4),
    _StnPptpSessionStatsRemoteCID_Type()
)
stnPptpSessionStatsRemoteCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsRemoteCID.setStatus("current")
_StnPptpSessionStatsUserName_Type = DisplayString
_StnPptpSessionStatsUserName_Object = MibTableColumn
stnPptpSessionStatsUserName = _StnPptpSessionStatsUserName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 5),
    _StnPptpSessionStatsUserName_Type()
)
stnPptpSessionStatsUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsUserName.setStatus("current")


class _StnPptpSessionStatsState_Type(Integer32):
    """Custom type stnPptpSessionStatsState based on Integer32"""
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
        *(("sessionConnecting", 2),
          ("sessionDisconnecting", 4),
          ("sessionEstablished", 3),
          ("sessionIdle", 1))
    )


_StnPptpSessionStatsState_Type.__name__ = "Integer32"
_StnPptpSessionStatsState_Object = MibTableColumn
stnPptpSessionStatsState = _StnPptpSessionStatsState_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 6),
    _StnPptpSessionStatsState_Type()
)
stnPptpSessionStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsState.setStatus("current")


class _StnPptpSessionStatsCallType_Type(Integer32):
    """Custom type stnPptpSessionStatsCallType based on Integer32"""
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
        *(("pacIncoming", 1),
          ("pacOutgoing", 3),
          ("pnsIncoming", 2),
          ("pnsOutgoing", 4))
    )


_StnPptpSessionStatsCallType_Type.__name__ = "Integer32"
_StnPptpSessionStatsCallType_Object = MibTableColumn
stnPptpSessionStatsCallType = _StnPptpSessionStatsCallType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 7),
    _StnPptpSessionStatsCallType_Type()
)
stnPptpSessionStatsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsCallType.setStatus("current")
_StnPptpSessionStatsCallSerialNumber_Type = Integer32
_StnPptpSessionStatsCallSerialNumber_Object = MibTableColumn
stnPptpSessionStatsCallSerialNumber = _StnPptpSessionStatsCallSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 8),
    _StnPptpSessionStatsCallSerialNumber_Type()
)
stnPptpSessionStatsCallSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsCallSerialNumber.setStatus("current")
_StnPptpSessionStatsTxConnectSpeed_Type = Integer32
_StnPptpSessionStatsTxConnectSpeed_Object = MibTableColumn
stnPptpSessionStatsTxConnectSpeed = _StnPptpSessionStatsTxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 9),
    _StnPptpSessionStatsTxConnectSpeed_Type()
)
stnPptpSessionStatsTxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsTxConnectSpeed.setStatus("current")
_StnPptpSessionStatsRxConnectSpeed_Type = Integer32
_StnPptpSessionStatsRxConnectSpeed_Object = MibTableColumn
stnPptpSessionStatsRxConnectSpeed = _StnPptpSessionStatsRxConnectSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 10),
    _StnPptpSessionStatsRxConnectSpeed_Type()
)
stnPptpSessionStatsRxConnectSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsRxConnectSpeed.setStatus("current")


class _StnPptpSessionStatsCallBearerType_Type(Integer32):
    """Custom type stnPptpSessionStatsCallBearerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 3),
          ("digital", 2),
          ("none", 1))
    )


_StnPptpSessionStatsCallBearerType_Type.__name__ = "Integer32"
_StnPptpSessionStatsCallBearerType_Object = MibTableColumn
stnPptpSessionStatsCallBearerType = _StnPptpSessionStatsCallBearerType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 11),
    _StnPptpSessionStatsCallBearerType_Type()
)
stnPptpSessionStatsCallBearerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsCallBearerType.setStatus("current")


class _StnPptpSessionStatsFramingType_Type(Integer32):
    """Custom type stnPptpSessionStatsFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("async", 3),
          ("none", 1),
          ("sync", 2))
    )


_StnPptpSessionStatsFramingType_Type.__name__ = "Integer32"
_StnPptpSessionStatsFramingType_Object = MibTableColumn
stnPptpSessionStatsFramingType = _StnPptpSessionStatsFramingType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 12),
    _StnPptpSessionStatsFramingType_Type()
)
stnPptpSessionStatsFramingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsFramingType.setStatus("current")
_StnPptpSessionStatsPhysChanId_Type = Integer32
_StnPptpSessionStatsPhysChanId_Object = MibTableColumn
stnPptpSessionStatsPhysChanId = _StnPptpSessionStatsPhysChanId_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 13),
    _StnPptpSessionStatsPhysChanId_Type()
)
stnPptpSessionStatsPhysChanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsPhysChanId.setStatus("current")
_StnPptpSessionStatsDNIS_Type = DisplayString
_StnPptpSessionStatsDNIS_Object = MibTableColumn
stnPptpSessionStatsDNIS = _StnPptpSessionStatsDNIS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 14),
    _StnPptpSessionStatsDNIS_Type()
)
stnPptpSessionStatsDNIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsDNIS.setStatus("current")
_StnPptpSessionStatsCLID_Type = DisplayString
_StnPptpSessionStatsCLID_Object = MibTableColumn
stnPptpSessionStatsCLID = _StnPptpSessionStatsCLID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 15),
    _StnPptpSessionStatsCLID_Type()
)
stnPptpSessionStatsCLID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsCLID.setStatus("current")
_StnPptpSessionStatsSubAddress_Type = DisplayString
_StnPptpSessionStatsSubAddress_Object = MibTableColumn
stnPptpSessionStatsSubAddress = _StnPptpSessionStatsSubAddress_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 16),
    _StnPptpSessionStatsSubAddress_Type()
)
stnPptpSessionStatsSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsSubAddress.setStatus("current")
_StnPptpSessionStatsPrivateGroupID_Type = DisplayString
_StnPptpSessionStatsPrivateGroupID_Object = MibTableColumn
stnPptpSessionStatsPrivateGroupID = _StnPptpSessionStatsPrivateGroupID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 17),
    _StnPptpSessionStatsPrivateGroupID_Type()
)
stnPptpSessionStatsPrivateGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsPrivateGroupID.setStatus("current")


class _StnPptpSessionStatsLocalRWS_Type(Integer32):
    """Custom type stnPptpSessionStatsLocalRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsLocalRWS_Type.__name__ = "Integer32"
_StnPptpSessionStatsLocalRWS_Object = MibTableColumn
stnPptpSessionStatsLocalRWS = _StnPptpSessionStatsLocalRWS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 18),
    _StnPptpSessionStatsLocalRWS_Type()
)
stnPptpSessionStatsLocalRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsLocalRWS.setStatus("current")


class _StnPptpSessionStatsRemoteInitialRWS_Type(Integer32):
    """Custom type stnPptpSessionStatsRemoteInitialRWS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsRemoteInitialRWS_Type.__name__ = "Integer32"
_StnPptpSessionStatsRemoteInitialRWS_Object = MibTableColumn
stnPptpSessionStatsRemoteInitialRWS = _StnPptpSessionStatsRemoteInitialRWS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 19),
    _StnPptpSessionStatsRemoteInitialRWS_Type()
)
stnPptpSessionStatsRemoteInitialRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsRemoteInitialRWS.setStatus("current")
_StnPptpSessionStatsRemotePPD_Type = Integer32
_StnPptpSessionStatsRemotePPD_Object = MibTableColumn
stnPptpSessionStatsRemotePPD = _StnPptpSessionStatsRemotePPD_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 20),
    _StnPptpSessionStatsRemotePPD_Type()
)
stnPptpSessionStatsRemotePPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsRemotePPD.setStatus("current")
_StnPptpSessionStatsRecvZLB_Type = Counter32
_StnPptpSessionStatsRecvZLB_Object = MibTableColumn
stnPptpSessionStatsRecvZLB = _StnPptpSessionStatsRecvZLB_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 21),
    _StnPptpSessionStatsRecvZLB_Type()
)
stnPptpSessionStatsRecvZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsRecvZLB.setStatus("current")
_StnPptpSessionStatsOutSequence_Type = Counter32
_StnPptpSessionStatsOutSequence_Object = MibTableColumn
stnPptpSessionStatsOutSequence = _StnPptpSessionStatsOutSequence_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 22),
    _StnPptpSessionStatsOutSequence_Type()
)
stnPptpSessionStatsOutSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsOutSequence.setStatus("current")
_StnPptpSessionStatsSendZLB_Type = Counter32
_StnPptpSessionStatsSendZLB_Object = MibTableColumn
stnPptpSessionStatsSendZLB = _StnPptpSessionStatsSendZLB_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 23),
    _StnPptpSessionStatsSendZLB_Type()
)
stnPptpSessionStatsSendZLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsSendZLB.setStatus("current")
_StnPptpSessionStatsAckTimeouts_Type = Counter32
_StnPptpSessionStatsAckTimeouts_Object = MibTableColumn
stnPptpSessionStatsAckTimeouts = _StnPptpSessionStatsAckTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 24),
    _StnPptpSessionStatsAckTimeouts_Type()
)
stnPptpSessionStatsAckTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsAckTimeouts.setStatus("current")


class _StnPptpSesssionStatsCurrentRemoteRWS_Type(Gauge32):
    """Custom type stnPptpSesssionStatsCurrentRemoteRWS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSesssionStatsCurrentRemoteRWS_Type.__name__ = "Gauge32"
_StnPptpSesssionStatsCurrentRemoteRWS_Object = MibTableColumn
stnPptpSesssionStatsCurrentRemoteRWS = _StnPptpSesssionStatsCurrentRemoteRWS_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 25),
    _StnPptpSesssionStatsCurrentRemoteRWS_Type()
)
stnPptpSesssionStatsCurrentRemoteRWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSesssionStatsCurrentRemoteRWS.setStatus("current")


class _StnPptpSessionStatsSendSeq_Type(Integer32):
    """Custom type stnPptpSessionStatsSendSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsSendSeq_Type.__name__ = "Integer32"
_StnPptpSessionStatsSendSeq_Object = MibTableColumn
stnPptpSessionStatsSendSeq = _StnPptpSessionStatsSendSeq_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 26),
    _StnPptpSessionStatsSendSeq_Type()
)
stnPptpSessionStatsSendSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsSendSeq.setStatus("current")


class _StnPptpSessionStatsSendSeqAck_Type(Integer32):
    """Custom type stnPptpSessionStatsSendSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsSendSeqAck_Type.__name__ = "Integer32"
_StnPptpSessionStatsSendSeqAck_Object = MibTableColumn
stnPptpSessionStatsSendSeqAck = _StnPptpSessionStatsSendSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 27),
    _StnPptpSessionStatsSendSeqAck_Type()
)
stnPptpSessionStatsSendSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsSendSeqAck.setStatus("current")


class _StnPptpSessionStatsRecvSeq_Type(Integer32):
    """Custom type stnPptpSessionStatsRecvSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsRecvSeq_Type.__name__ = "Integer32"
_StnPptpSessionStatsRecvSeq_Object = MibTableColumn
stnPptpSessionStatsRecvSeq = _StnPptpSessionStatsRecvSeq_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 28),
    _StnPptpSessionStatsRecvSeq_Type()
)
stnPptpSessionStatsRecvSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsRecvSeq.setStatus("current")


class _StnPptpSessionStatsRecvSeqAck_Type(Integer32):
    """Custom type stnPptpSessionStatsRecvSeqAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionStatsRecvSeqAck_Type.__name__ = "Integer32"
_StnPptpSessionStatsRecvSeqAck_Object = MibTableColumn
stnPptpSessionStatsRecvSeqAck = _StnPptpSessionStatsRecvSeqAck_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 7, 1, 29),
    _StnPptpSessionStatsRecvSeqAck_Type()
)
stnPptpSessionStatsRecvSeqAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionStatsRecvSeqAck.setStatus("current")
_StnPptpTunnelMapTable_Object = MibTable
stnPptpTunnelMapTable = _StnPptpTunnelMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 8)
)
if mibBuilder.loadTexts:
    stnPptpTunnelMapTable.setStatus("current")
_StnPptpTunnelMapEntry_Object = MibTableRow
stnPptpTunnelMapEntry = _StnPptpTunnelMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 8, 1)
)
stnPptpTunnelMapEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpTunnelMapLocalTID"),
)
if mibBuilder.loadTexts:
    stnPptpTunnelMapEntry.setStatus("current")


class _StnPptpTunnelMapLocalTID_Type(Integer32):
    """Custom type stnPptpTunnelMapLocalTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpTunnelMapLocalTID_Type.__name__ = "Integer32"
_StnPptpTunnelMapLocalTID_Object = MibTableColumn
stnPptpTunnelMapLocalTID = _StnPptpTunnelMapLocalTID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 8, 1, 1),
    _StnPptpTunnelMapLocalTID_Type()
)
stnPptpTunnelMapLocalTID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelMapLocalTID.setStatus("current")
_StnPptpTunnelMapIfIndex_Type = InterfaceIndex
_StnPptpTunnelMapIfIndex_Object = MibTableColumn
stnPptpTunnelMapIfIndex = _StnPptpTunnelMapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 8, 1, 2),
    _StnPptpTunnelMapIfIndex_Type()
)
stnPptpTunnelMapIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpTunnelMapIfIndex.setStatus("current")
_StnPptpSessionMapTable_Object = MibTable
stnPptpSessionMapTable = _StnPptpSessionMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 9)
)
if mibBuilder.loadTexts:
    stnPptpSessionMapTable.setStatus("current")
_StnPptpSessionMapEntry_Object = MibTableRow
stnPptpSessionMapEntry = _StnPptpSessionMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 9, 1)
)
stnPptpSessionMapEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpSessionMapHLIfIndex"),
)
if mibBuilder.loadTexts:
    stnPptpSessionMapEntry.setStatus("current")
_StnPptpSessionMapHLIfIndex_Type = InterfaceIndex
_StnPptpSessionMapHLIfIndex_Object = MibTableColumn
stnPptpSessionMapHLIfIndex = _StnPptpSessionMapHLIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 9, 1, 1),
    _StnPptpSessionMapHLIfIndex_Type()
)
stnPptpSessionMapHLIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionMapHLIfIndex.setStatus("current")
_StnPptpSessionMapTunnelIfIndex_Type = InterfaceIndex
_StnPptpSessionMapTunnelIfIndex_Object = MibTableColumn
stnPptpSessionMapTunnelIfIndex = _StnPptpSessionMapTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 9, 1, 2),
    _StnPptpSessionMapTunnelIfIndex_Type()
)
stnPptpSessionMapTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionMapTunnelIfIndex.setStatus("current")


class _StnPptpSessionMapLocalCID_Type(Integer32):
    """Custom type stnPptpSessionMapLocalCID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StnPptpSessionMapLocalCID_Type.__name__ = "Integer32"
_StnPptpSessionMapLocalCID_Object = MibTableColumn
stnPptpSessionMapLocalCID = _StnPptpSessionMapLocalCID_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 9, 1, 3),
    _StnPptpSessionMapLocalCID_Type()
)
stnPptpSessionMapLocalCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpSessionMapLocalCID.setStatus("current")
_StnPptpDomainMapTable_Object = MibTable
stnPptpDomainMapTable = _StnPptpDomainMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 10)
)
if mibBuilder.loadTexts:
    stnPptpDomainMapTable.setStatus("current")
_StnPptpDomainMapTableEntry_Object = MibTableRow
stnPptpDomainMapTableEntry = _StnPptpDomainMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 10, 1)
)
stnPptpDomainMapTableEntry.setIndexNames(
    (0, "STN-PPTP-MIB", "stnPptpDomainMapIdentifier"),
)
if mibBuilder.loadTexts:
    stnPptpDomainMapTableEntry.setStatus("current")
_StnPptpDomainMapIdentifier_Type = DisplayString
_StnPptpDomainMapIdentifier_Object = MibTableColumn
stnPptpDomainMapIdentifier = _StnPptpDomainMapIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 10, 1, 1),
    _StnPptpDomainMapIdentifier_Type()
)
stnPptpDomainMapIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stnPptpDomainMapIdentifier.setStatus("current")
_StnPptpDomainMapHostName_Type = DisplayString
_StnPptpDomainMapHostName_Object = MibTableColumn
stnPptpDomainMapHostName = _StnPptpDomainMapHostName_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 10, 1, 2),
    _StnPptpDomainMapHostName_Type()
)
stnPptpDomainMapHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainMapHostName.setStatus("current")
_StnPptpDomainMapType_Type = StnDomainMapType
_StnPptpDomainMapType_Object = MibTableColumn
stnPptpDomainMapType = _StnPptpDomainMapType_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 10, 1, 3),
    _StnPptpDomainMapType_Type()
)
stnPptpDomainMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainMapType.setStatus("current")
_StnPptpDomainMapTypeInfo_Type = DisplayString
_StnPptpDomainMapTypeInfo_Object = MibTableColumn
stnPptpDomainMapTypeInfo = _StnPptpDomainMapTypeInfo_Object(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 1, 10, 1, 4),
    _StnPptpDomainMapTypeInfo_Type()
)
stnPptpDomainMapTypeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stnPptpDomainMapTypeInfo.setStatus("current")
_StnPptpMibConformance_ObjectIdentity = ObjectIdentity
stnPptpMibConformance = _StnPptpMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2)
)
_StnPptpGroups_ObjectIdentity = ObjectIdentity
stnPptpGroups = _StnPptpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2, 1)
)
_StnPptpCompliances_ObjectIdentity = ObjectIdentity
stnPptpCompliances = _StnPptpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2, 2)
)
_StnPptpTraps_ObjectIdentity = ObjectIdentity
stnPptpTraps = _StnPptpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 3)
)

# Managed Objects groups

stnPptpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2, 1, 1)
)
stnPptpConfigGroup.setObjects(
      *(("STN-PPTP-MIB", "stnPptpAdminState"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigAuthentication"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigSecret"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigSecurity"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigHelloInterval"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigIdleTimeout"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigControlRWS"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigControlRetransmissions"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigPayloadSequencing"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigPayloadRWS"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigDelayedAckTimeout"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigReassemblyTimeout"),
        ("STN-PPTP-MIB", "stnPptpTunnelConfigTransport"))
)
if mibBuilder.loadTexts:
    stnPptpConfigGroup.setStatus("current")

stnPptpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2, 1, 2)
)
stnPptpStatsGroup.setObjects(
      *(("STN-PPTP-MIB", "stnPptpProtocolVersion"),
        ("STN-PPTP-MIB", "stnPptpVendorName"),
        ("STN-PPTP-MIB", "stnPptpFirmwareRev"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsIfIndex"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsLocalTID"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsState"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsInitiated"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsRemoteHostName"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsRemoteVendorName"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsRemoteFirmwareRevision"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsRemoteProtocolVersion"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsBearerCapabilities"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsFramingCapabilities"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsControlRecvPackets"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsControlSendPackets"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsTotalSessions"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsFailedSessions"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsActiveSessions"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsLastResultCode"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsLastErrorCode"),
        ("STN-PPTP-MIB", "stnPptpTunnelStatsLastErrorMessage"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsTunnelIfIndex"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsHLIfIndex"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsLocalCID"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsRemoteCID"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsUserName"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsState"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsCallType"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsCallSerialNumber"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsTxConnectSpeed"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsRxConnectSpeed"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsCallBearerType"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsFramingType"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsPhysChanId"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsDNIS"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsCLID"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsSubAddress"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsPrivateGroupID"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsLocalRWS"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsRemoteInitialRWS"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsRemotePPD"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsRecvZLB"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsOutSequence"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsSendZLB"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsAckTimeouts"),
        ("STN-PPTP-MIB", "stnPptpSesssionStatsCurrentRemoteRWS"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsSendSeq"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsSendSeqAck"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsRecvSeq"),
        ("STN-PPTP-MIB", "stnPptpSessionStatsRecvSeqAck"))
)
if mibBuilder.loadTexts:
    stnPptpStatsGroup.setStatus("current")

stnPptpDomainGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2, 1, 4)
)
stnPptpDomainGroup.setObjects(
      *(("STN-PPTP-MIB", "stnPptpDomainConfigAdminState"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigAuthentication"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigSecret"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigTunnelSecurity"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigTunnelHelloInterval"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigTunnelIdleTimeout"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigControlRWS"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigControlRetransmissions"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigPayloadSequencing"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigPayloadRWS"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigDelayedAckTimeout"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigReassemblyTimeout"),
        ("STN-PPTP-MIB", "stnPptpDomainConfigStatus"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsTotalTunnels"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsFailedTunnels"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsFailedAuthentications"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsActiveTunnels"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsTotalSessions"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsFailedSessions"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsActiveSessions"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsControlRecvOctets"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsControlRecvPackets"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsControlSendOctets"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsControlSendPackets"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsPayloadRecvOctets"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsPayloadRecvPackets"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsPayloadRecvDiscards"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsPayloadSendOctets"),
        ("STN-PPTP-MIB", "stnPptpDomainStatsPayloadSendPackets"))
)
if mibBuilder.loadTexts:
    stnPptpDomainGroup.setStatus("current")

stnPptpMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2, 1, 5)
)
stnPptpMappingGroup.setObjects(
      *(("STN-PPTP-MIB", "stnPptpTunnelMapLocalTID"),
        ("STN-PPTP-MIB", "stnPptpTunnelMapIfIndex"),
        ("STN-PPTP-MIB", "stnPptpSessionMapHLIfIndex"),
        ("STN-PPTP-MIB", "stnPptpSessionMapTunnelIfIndex"),
        ("STN-PPTP-MIB", "stnPptpSessionMapLocalCID"))
)
if mibBuilder.loadTexts:
    stnPptpMappingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

stnPptpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3551, 4, 1, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    stnPptpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STN-PPTP-MIB",
    **{"MilliSeconds": MilliSeconds,
       "stnPptp": stnPptp,
       "stnPptpObjects": stnPptpObjects,
       "stnPptpScalar": stnPptpScalar,
       "stnPptpConfig": stnPptpConfig,
       "stnPptpAdminState": stnPptpAdminState,
       "stnPptpStats": stnPptpStats,
       "stnPptpProtocolVersion": stnPptpProtocolVersion,
       "stnPptpVendorName": stnPptpVendorName,
       "stnPptpFirmwareRev": stnPptpFirmwareRev,
       "stnPptpDomainConfigTable": stnPptpDomainConfigTable,
       "stnPptpDomainConfigEntry": stnPptpDomainConfigEntry,
       "stnPptpDomainConfigIdentifier": stnPptpDomainConfigIdentifier,
       "stnPptpDomainConfigAdminState": stnPptpDomainConfigAdminState,
       "stnPptpDomainConfigAuthentication": stnPptpDomainConfigAuthentication,
       "stnPptpDomainConfigSecret": stnPptpDomainConfigSecret,
       "stnPptpDomainConfigTunnelSecurity": stnPptpDomainConfigTunnelSecurity,
       "stnPptpDomainConfigTunnelHelloInterval": stnPptpDomainConfigTunnelHelloInterval,
       "stnPptpDomainConfigTunnelIdleTimeout": stnPptpDomainConfigTunnelIdleTimeout,
       "stnPptpDomainConfigControlRWS": stnPptpDomainConfigControlRWS,
       "stnPptpDomainConfigControlRetransmissions": stnPptpDomainConfigControlRetransmissions,
       "stnPptpDomainConfigPayloadSequencing": stnPptpDomainConfigPayloadSequencing,
       "stnPptpDomainConfigPayloadRWS": stnPptpDomainConfigPayloadRWS,
       "stnPptpDomainConfigDelayedAckTimeout": stnPptpDomainConfigDelayedAckTimeout,
       "stnPptpDomainConfigReassemblyTimeout": stnPptpDomainConfigReassemblyTimeout,
       "stnPptpDomainConfigStatus": stnPptpDomainConfigStatus,
       "stnPptpDomainStatsTable": stnPptpDomainStatsTable,
       "stnPptpDomainStatsEntry": stnPptpDomainStatsEntry,
       "stnPptpDomainStatsIdentifier": stnPptpDomainStatsIdentifier,
       "stnPptpDomainStatsTotalTunnels": stnPptpDomainStatsTotalTunnels,
       "stnPptpDomainStatsFailedTunnels": stnPptpDomainStatsFailedTunnels,
       "stnPptpDomainStatsFailedAuthentications": stnPptpDomainStatsFailedAuthentications,
       "stnPptpDomainStatsActiveTunnels": stnPptpDomainStatsActiveTunnels,
       "stnPptpDomainStatsTotalSessions": stnPptpDomainStatsTotalSessions,
       "stnPptpDomainStatsFailedSessions": stnPptpDomainStatsFailedSessions,
       "stnPptpDomainStatsActiveSessions": stnPptpDomainStatsActiveSessions,
       "stnPptpDomainStatsControlRecvOctets": stnPptpDomainStatsControlRecvOctets,
       "stnPptpDomainStatsControlRecvPackets": stnPptpDomainStatsControlRecvPackets,
       "stnPptpDomainStatsControlSendOctets": stnPptpDomainStatsControlSendOctets,
       "stnPptpDomainStatsControlSendPackets": stnPptpDomainStatsControlSendPackets,
       "stnPptpDomainStatsPayloadRecvOctets": stnPptpDomainStatsPayloadRecvOctets,
       "stnPptpDomainStatsPayloadRecvPackets": stnPptpDomainStatsPayloadRecvPackets,
       "stnPptpDomainStatsPayloadRecvDiscards": stnPptpDomainStatsPayloadRecvDiscards,
       "stnPptpDomainStatsPayloadSendOctets": stnPptpDomainStatsPayloadSendOctets,
       "stnPptpDomainStatsPayloadSendPackets": stnPptpDomainStatsPayloadSendPackets,
       "stnPptpTunnelConfigTable": stnPptpTunnelConfigTable,
       "stnPptpTunnelConfigEntry": stnPptpTunnelConfigEntry,
       "stnPptpTunnelConfigIfIndex": stnPptpTunnelConfigIfIndex,
       "stnPptpTunnelConfigAuthentication": stnPptpTunnelConfigAuthentication,
       "stnPptpTunnelConfigSecret": stnPptpTunnelConfigSecret,
       "stnPptpTunnelConfigSecurity": stnPptpTunnelConfigSecurity,
       "stnPptpTunnelConfigHelloInterval": stnPptpTunnelConfigHelloInterval,
       "stnPptpTunnelConfigIdleTimeout": stnPptpTunnelConfigIdleTimeout,
       "stnPptpTunnelConfigControlRWS": stnPptpTunnelConfigControlRWS,
       "stnPptpTunnelConfigControlRetransmissions": stnPptpTunnelConfigControlRetransmissions,
       "stnPptpTunnelConfigPayloadSequencing": stnPptpTunnelConfigPayloadSequencing,
       "stnPptpTunnelConfigPayloadRWS": stnPptpTunnelConfigPayloadRWS,
       "stnPptpTunnelConfigDelayedAckTimeout": stnPptpTunnelConfigDelayedAckTimeout,
       "stnPptpTunnelConfigReassemblyTimeout": stnPptpTunnelConfigReassemblyTimeout,
       "stnPptpTunnelConfigTransport": stnPptpTunnelConfigTransport,
       "stnPptpTunnelStatsTable": stnPptpTunnelStatsTable,
       "stnPptpTunnelStatsEntry": stnPptpTunnelStatsEntry,
       "stnPptpTunnelStatsIfIndex": stnPptpTunnelStatsIfIndex,
       "stnPptpTunnelStatsLocalTID": stnPptpTunnelStatsLocalTID,
       "stnPptpTunnelStatsState": stnPptpTunnelStatsState,
       "stnPptpTunnelStatsInitiated": stnPptpTunnelStatsInitiated,
       "stnPptpTunnelStatsRemoteHostName": stnPptpTunnelStatsRemoteHostName,
       "stnPptpTunnelStatsRemoteVendorName": stnPptpTunnelStatsRemoteVendorName,
       "stnPptpTunnelStatsRemoteFirmwareRevision": stnPptpTunnelStatsRemoteFirmwareRevision,
       "stnPptpTunnelStatsRemoteProtocolVersion": stnPptpTunnelStatsRemoteProtocolVersion,
       "stnPptpTunnelStatsBearerCapabilities": stnPptpTunnelStatsBearerCapabilities,
       "stnPptpTunnelStatsFramingCapabilities": stnPptpTunnelStatsFramingCapabilities,
       "stnPptpTunnelStatsControlRecvPackets": stnPptpTunnelStatsControlRecvPackets,
       "stnPptpTunnelStatsControlSendPackets": stnPptpTunnelStatsControlSendPackets,
       "stnPptpTunnelStatsTotalSessions": stnPptpTunnelStatsTotalSessions,
       "stnPptpTunnelStatsFailedSessions": stnPptpTunnelStatsFailedSessions,
       "stnPptpTunnelStatsActiveSessions": stnPptpTunnelStatsActiveSessions,
       "stnPptpTunnelStatsLastResultCode": stnPptpTunnelStatsLastResultCode,
       "stnPptpTunnelStatsLastErrorCode": stnPptpTunnelStatsLastErrorCode,
       "stnPptpTunnelStatsLastErrorMessage": stnPptpTunnelStatsLastErrorMessage,
       "stnPptpSessionStatsTable": stnPptpSessionStatsTable,
       "stnPptpSessionStatsEntry": stnPptpSessionStatsEntry,
       "stnPptpSessionStatsTunnelIfIndex": stnPptpSessionStatsTunnelIfIndex,
       "stnPptpSessionStatsHLIfIndex": stnPptpSessionStatsHLIfIndex,
       "stnPptpSessionStatsLocalCID": stnPptpSessionStatsLocalCID,
       "stnPptpSessionStatsRemoteCID": stnPptpSessionStatsRemoteCID,
       "stnPptpSessionStatsUserName": stnPptpSessionStatsUserName,
       "stnPptpSessionStatsState": stnPptpSessionStatsState,
       "stnPptpSessionStatsCallType": stnPptpSessionStatsCallType,
       "stnPptpSessionStatsCallSerialNumber": stnPptpSessionStatsCallSerialNumber,
       "stnPptpSessionStatsTxConnectSpeed": stnPptpSessionStatsTxConnectSpeed,
       "stnPptpSessionStatsRxConnectSpeed": stnPptpSessionStatsRxConnectSpeed,
       "stnPptpSessionStatsCallBearerType": stnPptpSessionStatsCallBearerType,
       "stnPptpSessionStatsFramingType": stnPptpSessionStatsFramingType,
       "stnPptpSessionStatsPhysChanId": stnPptpSessionStatsPhysChanId,
       "stnPptpSessionStatsDNIS": stnPptpSessionStatsDNIS,
       "stnPptpSessionStatsCLID": stnPptpSessionStatsCLID,
       "stnPptpSessionStatsSubAddress": stnPptpSessionStatsSubAddress,
       "stnPptpSessionStatsPrivateGroupID": stnPptpSessionStatsPrivateGroupID,
       "stnPptpSessionStatsLocalRWS": stnPptpSessionStatsLocalRWS,
       "stnPptpSessionStatsRemoteInitialRWS": stnPptpSessionStatsRemoteInitialRWS,
       "stnPptpSessionStatsRemotePPD": stnPptpSessionStatsRemotePPD,
       "stnPptpSessionStatsRecvZLB": stnPptpSessionStatsRecvZLB,
       "stnPptpSessionStatsOutSequence": stnPptpSessionStatsOutSequence,
       "stnPptpSessionStatsSendZLB": stnPptpSessionStatsSendZLB,
       "stnPptpSessionStatsAckTimeouts": stnPptpSessionStatsAckTimeouts,
       "stnPptpSesssionStatsCurrentRemoteRWS": stnPptpSesssionStatsCurrentRemoteRWS,
       "stnPptpSessionStatsSendSeq": stnPptpSessionStatsSendSeq,
       "stnPptpSessionStatsSendSeqAck": stnPptpSessionStatsSendSeqAck,
       "stnPptpSessionStatsRecvSeq": stnPptpSessionStatsRecvSeq,
       "stnPptpSessionStatsRecvSeqAck": stnPptpSessionStatsRecvSeqAck,
       "stnPptpTunnelMapTable": stnPptpTunnelMapTable,
       "stnPptpTunnelMapEntry": stnPptpTunnelMapEntry,
       "stnPptpTunnelMapLocalTID": stnPptpTunnelMapLocalTID,
       "stnPptpTunnelMapIfIndex": stnPptpTunnelMapIfIndex,
       "stnPptpSessionMapTable": stnPptpSessionMapTable,
       "stnPptpSessionMapEntry": stnPptpSessionMapEntry,
       "stnPptpSessionMapHLIfIndex": stnPptpSessionMapHLIfIndex,
       "stnPptpSessionMapTunnelIfIndex": stnPptpSessionMapTunnelIfIndex,
       "stnPptpSessionMapLocalCID": stnPptpSessionMapLocalCID,
       "stnPptpDomainMapTable": stnPptpDomainMapTable,
       "stnPptpDomainMapTableEntry": stnPptpDomainMapTableEntry,
       "stnPptpDomainMapIdentifier": stnPptpDomainMapIdentifier,
       "stnPptpDomainMapHostName": stnPptpDomainMapHostName,
       "stnPptpDomainMapType": stnPptpDomainMapType,
       "stnPptpDomainMapTypeInfo": stnPptpDomainMapTypeInfo,
       "stnPptpMibConformance": stnPptpMibConformance,
       "stnPptpGroups": stnPptpGroups,
       "stnPptpConfigGroup": stnPptpConfigGroup,
       "stnPptpStatsGroup": stnPptpStatsGroup,
       "stnPptpDomainGroup": stnPptpDomainGroup,
       "stnPptpMappingGroup": stnPptpMappingGroup,
       "stnPptpCompliances": stnPptpCompliances,
       "stnPptpCompliance": stnPptpCompliance,
       "stnPptpTraps": stnPptpTraps}
)
