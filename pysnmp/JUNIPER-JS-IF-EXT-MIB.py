# SNMP MIB module (JUNIPER-JS-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:17 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(jnxJsIf,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsIf")

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


# MODULE-IDENTITY

jnxJsIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1)
)
jnxJsIfMIB.setRevisions(
        ("2007-05-09 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsIfExtension_ObjectIdentity = ObjectIdentity
jnxJsIfExtension = _JnxJsIfExtension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1)
)
_JnxJsIfMonTable_Object = MibTable
jnxJsIfMonTable = _JnxJsIfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxJsIfMonTable.setStatus("current")
_JnxJsIfMonEntry_Object = MibTableRow
jnxJsIfMonEntry = _JnxJsIfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1)
)
jnxJsIfMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxJsIfMonEntry.setStatus("current")
_JnxJsIfMonInIcmp_Type = Counter32
_JnxJsIfMonInIcmp_Object = MibTableColumn
jnxJsIfMonInIcmp = _JnxJsIfMonInIcmp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 1),
    _JnxJsIfMonInIcmp_Type()
)
jnxJsIfMonInIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonInIcmp.setStatus("current")
_JnxJsIfMonInSelf_Type = Counter32
_JnxJsIfMonInSelf_Object = MibTableColumn
jnxJsIfMonInSelf = _JnxJsIfMonInSelf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 2),
    _JnxJsIfMonInSelf_Type()
)
jnxJsIfMonInSelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonInSelf.setStatus("current")
_JnxJsIfMonInVpn_Type = Counter32
_JnxJsIfMonInVpn_Object = MibTableColumn
jnxJsIfMonInVpn = _JnxJsIfMonInVpn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 3),
    _JnxJsIfMonInVpn_Type()
)
jnxJsIfMonInVpn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonInVpn.setStatus("current")
_JnxJsIfMonInPolicyPermit_Type = Counter64
_JnxJsIfMonInPolicyPermit_Object = MibTableColumn
jnxJsIfMonInPolicyPermit = _JnxJsIfMonInPolicyPermit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 4),
    _JnxJsIfMonInPolicyPermit_Type()
)
jnxJsIfMonInPolicyPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonInPolicyPermit.setStatus("current")
_JnxJsIfMonOutPolicyPermit_Type = Counter64
_JnxJsIfMonOutPolicyPermit_Object = MibTableColumn
jnxJsIfMonOutPolicyPermit = _JnxJsIfMonOutPolicyPermit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 5),
    _JnxJsIfMonOutPolicyPermit_Type()
)
jnxJsIfMonOutPolicyPermit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonOutPolicyPermit.setStatus("current")
_JnxJsIfMonConn_Type = Counter32
_JnxJsIfMonConn_Object = MibTableColumn
jnxJsIfMonConn = _JnxJsIfMonConn_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 6),
    _JnxJsIfMonConn_Type()
)
jnxJsIfMonConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonConn.setStatus("current")
_JnxJsIfMonInMcast_Type = Counter32
_JnxJsIfMonInMcast_Object = MibTableColumn
jnxJsIfMonInMcast = _JnxJsIfMonInMcast_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 7),
    _JnxJsIfMonInMcast_Type()
)
jnxJsIfMonInMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonInMcast.setStatus("current")
_JnxJsIfMonOutMcast_Type = Counter32
_JnxJsIfMonOutMcast_Object = MibTableColumn
jnxJsIfMonOutMcast = _JnxJsIfMonOutMcast_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 8),
    _JnxJsIfMonOutMcast_Type()
)
jnxJsIfMonOutMcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonOutMcast.setStatus("current")
_JnxJsIfMonPolicyDeny_Type = Counter32
_JnxJsIfMonPolicyDeny_Object = MibTableColumn
jnxJsIfMonPolicyDeny = _JnxJsIfMonPolicyDeny_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 9),
    _JnxJsIfMonPolicyDeny_Type()
)
jnxJsIfMonPolicyDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonPolicyDeny.setStatus("current")
_JnxJsIfMonNoGateParent_Type = Counter32
_JnxJsIfMonNoGateParent_Object = MibTableColumn
jnxJsIfMonNoGateParent = _JnxJsIfMonNoGateParent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 10),
    _JnxJsIfMonNoGateParent_Type()
)
jnxJsIfMonNoGateParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoGateParent.setStatus("current")
_JnxJsIfMonTcpProxyDrop_Type = Counter32
_JnxJsIfMonTcpProxyDrop_Object = MibTableColumn
jnxJsIfMonTcpProxyDrop = _JnxJsIfMonTcpProxyDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 11),
    _JnxJsIfMonTcpProxyDrop_Type()
)
jnxJsIfMonTcpProxyDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonTcpProxyDrop.setStatus("current")
_JnxJsIfMonNoDip_Type = Counter32
_JnxJsIfMonNoDip_Object = MibTableColumn
jnxJsIfMonNoDip = _JnxJsIfMonNoDip_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 12),
    _JnxJsIfMonNoDip_Type()
)
jnxJsIfMonNoDip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoDip.setStatus("current")
_JnxJsIfMonNoNspTunnel_Type = Counter32
_JnxJsIfMonNoNspTunnel_Object = MibTableColumn
jnxJsIfMonNoNspTunnel = _JnxJsIfMonNoNspTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 13),
    _JnxJsIfMonNoNspTunnel_Type()
)
jnxJsIfMonNoNspTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoNspTunnel.setStatus("current")
_JnxJsIfMonNoNatCon_Type = Counter32
_JnxJsIfMonNoNatCon_Object = MibTableColumn
jnxJsIfMonNoNatCon = _JnxJsIfMonNoNatCon_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 14),
    _JnxJsIfMonNoNatCon_Type()
)
jnxJsIfMonNoNatCon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoNatCon.setStatus("current")
_JnxJsIfMonInvalidZone_Type = Counter32
_JnxJsIfMonInvalidZone_Object = MibTableColumn
jnxJsIfMonInvalidZone = _JnxJsIfMonInvalidZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 15),
    _JnxJsIfMonInvalidZone_Type()
)
jnxJsIfMonInvalidZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonInvalidZone.setStatus("current")
_JnxJsIfMonIpClsFail_Type = Counter32
_JnxJsIfMonIpClsFail_Object = MibTableColumn
jnxJsIfMonIpClsFail = _JnxJsIfMonIpClsFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 16),
    _JnxJsIfMonIpClsFail_Type()
)
jnxJsIfMonIpClsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonIpClsFail.setStatus("current")
_JnxJsIfMonAuthDrop_Type = Counter32
_JnxJsIfMonAuthDrop_Object = MibTableColumn
jnxJsIfMonAuthDrop = _JnxJsIfMonAuthDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 17),
    _JnxJsIfMonAuthDrop_Type()
)
jnxJsIfMonAuthDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonAuthDrop.setStatus("current")
_JnxJsIfMonMultiUserAuthDrop_Type = Counter32
_JnxJsIfMonMultiUserAuthDrop_Object = MibTableColumn
jnxJsIfMonMultiUserAuthDrop = _JnxJsIfMonMultiUserAuthDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 18),
    _JnxJsIfMonMultiUserAuthDrop_Type()
)
jnxJsIfMonMultiUserAuthDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonMultiUserAuthDrop.setStatus("current")
_JnxJsIfMonLoopMultiDipDrop_Type = Counter32
_JnxJsIfMonLoopMultiDipDrop_Object = MibTableColumn
jnxJsIfMonLoopMultiDipDrop = _JnxJsIfMonLoopMultiDipDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 19),
    _JnxJsIfMonLoopMultiDipDrop_Type()
)
jnxJsIfMonLoopMultiDipDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonLoopMultiDipDrop.setStatus("current")
_JnxJsIfMonAddrSpoof_Type = Counter32
_JnxJsIfMonAddrSpoof_Object = MibTableColumn
jnxJsIfMonAddrSpoof = _JnxJsIfMonAddrSpoof_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 20),
    _JnxJsIfMonAddrSpoof_Type()
)
jnxJsIfMonAddrSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonAddrSpoof.setStatus("current")
_JnxJsIfMonLpDrop_Type = Counter32
_JnxJsIfMonLpDrop_Object = MibTableColumn
jnxJsIfMonLpDrop = _JnxJsIfMonLpDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 21),
    _JnxJsIfMonLpDrop_Type()
)
jnxJsIfMonLpDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonLpDrop.setStatus("current")
_JnxJsIfMonNullZone_Type = Counter32
_JnxJsIfMonNullZone_Object = MibTableColumn
jnxJsIfMonNullZone = _JnxJsIfMonNullZone_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 22),
    _JnxJsIfMonNullZone_Type()
)
jnxJsIfMonNullZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNullZone.setStatus("current")
_JnxJsIfMonNoGate_Type = Counter32
_JnxJsIfMonNoGate_Object = MibTableColumn
jnxJsIfMonNoGate = _JnxJsIfMonNoGate_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 23),
    _JnxJsIfMonNoGate_Type()
)
jnxJsIfMonNoGate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoGate.setStatus("current")
_JnxJsIfMonNoMinorSess_Type = Counter32
_JnxJsIfMonNoMinorSess_Object = MibTableColumn
jnxJsIfMonNoMinorSess = _JnxJsIfMonNoMinorSess_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 24),
    _JnxJsIfMonNoMinorSess_Type()
)
jnxJsIfMonNoMinorSess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoMinorSess.setStatus("current")
_JnxJsIfMonNvecErr_Type = Counter32
_JnxJsIfMonNvecErr_Object = MibTableColumn
jnxJsIfMonNvecErr = _JnxJsIfMonNvecErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 25),
    _JnxJsIfMonNvecErr_Type()
)
jnxJsIfMonNvecErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNvecErr.setStatus("current")
_JnxJsIfMonTcpSeq_Type = Counter32
_JnxJsIfMonTcpSeq_Object = MibTableColumn
jnxJsIfMonTcpSeq = _JnxJsIfMonTcpSeq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 26),
    _JnxJsIfMonTcpSeq_Type()
)
jnxJsIfMonTcpSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonTcpSeq.setStatus("current")
_JnxJsIfMonIllegalPak_Type = Counter32
_JnxJsIfMonIllegalPak_Object = MibTableColumn
jnxJsIfMonIllegalPak = _JnxJsIfMonIllegalPak_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 27),
    _JnxJsIfMonIllegalPak_Type()
)
jnxJsIfMonIllegalPak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonIllegalPak.setStatus("current")
_JnxJsIfMonNoRoute_Type = Counter32
_JnxJsIfMonNoRoute_Object = MibTableColumn
jnxJsIfMonNoRoute = _JnxJsIfMonNoRoute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 28),
    _JnxJsIfMonNoRoute_Type()
)
jnxJsIfMonNoRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoRoute.setStatus("current")
_JnxJsIfMonAuthFail_Type = Counter32
_JnxJsIfMonAuthFail_Object = MibTableColumn
jnxJsIfMonAuthFail = _JnxJsIfMonAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 29),
    _JnxJsIfMonAuthFail_Type()
)
jnxJsIfMonAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonAuthFail.setStatus("current")
_JnxJsIfMonSaInactive_Type = Counter32
_JnxJsIfMonSaInactive_Object = MibTableColumn
jnxJsIfMonSaInactive = _JnxJsIfMonSaInactive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 30),
    _JnxJsIfMonSaInactive_Type()
)
jnxJsIfMonSaInactive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonSaInactive.setStatus("current")
_JnxJsIfMonNoSa_Type = Counter32
_JnxJsIfMonNoSa_Object = MibTableColumn
jnxJsIfMonNoSa = _JnxJsIfMonNoSa_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 31),
    _JnxJsIfMonNoSa_Type()
)
jnxJsIfMonNoSa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonNoSa.setStatus("current")
_JnxJsIfMonSelfPktDrop_Type = Counter32
_JnxJsIfMonSelfPktDrop_Object = MibTableColumn
jnxJsIfMonSelfPktDrop = _JnxJsIfMonSelfPktDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 1, 1, 1, 1, 1, 32),
    _JnxJsIfMonSelfPktDrop_Type()
)
jnxJsIfMonSelfPktDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsIfMonSelfPktDrop.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-IF-EXT-MIB",
    **{"jnxJsIfMIB": jnxJsIfMIB,
       "jnxJsIfExtension": jnxJsIfExtension,
       "jnxJsIfMonTable": jnxJsIfMonTable,
       "jnxJsIfMonEntry": jnxJsIfMonEntry,
       "jnxJsIfMonInIcmp": jnxJsIfMonInIcmp,
       "jnxJsIfMonInSelf": jnxJsIfMonInSelf,
       "jnxJsIfMonInVpn": jnxJsIfMonInVpn,
       "jnxJsIfMonInPolicyPermit": jnxJsIfMonInPolicyPermit,
       "jnxJsIfMonOutPolicyPermit": jnxJsIfMonOutPolicyPermit,
       "jnxJsIfMonConn": jnxJsIfMonConn,
       "jnxJsIfMonInMcast": jnxJsIfMonInMcast,
       "jnxJsIfMonOutMcast": jnxJsIfMonOutMcast,
       "jnxJsIfMonPolicyDeny": jnxJsIfMonPolicyDeny,
       "jnxJsIfMonNoGateParent": jnxJsIfMonNoGateParent,
       "jnxJsIfMonTcpProxyDrop": jnxJsIfMonTcpProxyDrop,
       "jnxJsIfMonNoDip": jnxJsIfMonNoDip,
       "jnxJsIfMonNoNspTunnel": jnxJsIfMonNoNspTunnel,
       "jnxJsIfMonNoNatCon": jnxJsIfMonNoNatCon,
       "jnxJsIfMonInvalidZone": jnxJsIfMonInvalidZone,
       "jnxJsIfMonIpClsFail": jnxJsIfMonIpClsFail,
       "jnxJsIfMonAuthDrop": jnxJsIfMonAuthDrop,
       "jnxJsIfMonMultiUserAuthDrop": jnxJsIfMonMultiUserAuthDrop,
       "jnxJsIfMonLoopMultiDipDrop": jnxJsIfMonLoopMultiDipDrop,
       "jnxJsIfMonAddrSpoof": jnxJsIfMonAddrSpoof,
       "jnxJsIfMonLpDrop": jnxJsIfMonLpDrop,
       "jnxJsIfMonNullZone": jnxJsIfMonNullZone,
       "jnxJsIfMonNoGate": jnxJsIfMonNoGate,
       "jnxJsIfMonNoMinorSess": jnxJsIfMonNoMinorSess,
       "jnxJsIfMonNvecErr": jnxJsIfMonNvecErr,
       "jnxJsIfMonTcpSeq": jnxJsIfMonTcpSeq,
       "jnxJsIfMonIllegalPak": jnxJsIfMonIllegalPak,
       "jnxJsIfMonNoRoute": jnxJsIfMonNoRoute,
       "jnxJsIfMonAuthFail": jnxJsIfMonAuthFail,
       "jnxJsIfMonSaInactive": jnxJsIfMonSaInactive,
       "jnxJsIfMonNoSa": jnxJsIfMonNoSa,
       "jnxJsIfMonSelfPktDrop": jnxJsIfMonSelfPktDrop}
)
